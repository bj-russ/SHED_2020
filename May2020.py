from maq20 import MAQ20
import time
import sys
from time import sleep
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import *
import threading
from tkinter import ttk
from simple_pid import PID
#from PIL import Image, ImageTk
import xlrd

########################################################################################################################
# This code is organized to include the setup, background process, and GUI process. The GUI requires background
# functions to update the text in the GUI. These are refreshed at a rate noted in each function. The actions taken in
# the GUI change values which control using the output values function.
#--------------------------- Setup --------------------------#
exit_case = False   # used to exit multiple threads by using window [x] button
refresh = 100


loc= ("config.xlsx")
wb=xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
ip = sheet.cell_value(1, 1)
refresh = int(sheet.cell_value(2,1))
XX = int(sheet.cell_value(3,1))
YY = int(sheet.cell_value(4,1))
ppg = [0]*8
for n in range (0,8):
    ppg[n] = sheet.cell_value(5,n+1)
cal1 = sheet.cell_value(12, 1)
cal2 = sheet.cell_value(13, 1)
cal3 = sheet.cell_value(14, 1)
cal4 = sheet.cell_value(15, 1)


# Display Settings ####in config file
# XX = 1024
# YY = 600


maq20 = MAQ20(ip_address=ip, port=502)     # Set communication with MAQ20
AI_mod = maq20[1]       # Analog input module
TTC_mod = maq20[2]      # Thermocouple input module.
DIV20_mod = maq20[4]    # 20 digital discrete inputs
DIOL_mod1 = maq20[5]    # 5 Digital discrete inputs, 5 Digital outputs
DIOL_mod2 = maq20[6]    # 5 Digital discrete inputs, 5 Digital outputs
DIOL_mod3 = maq20[7]    # 5 Digital discrete inputs, 5 Digital outputs
DIOL_mod4 = maq20[8]    # 5 Digital discrete inputs, 5 Digital outputs

# Read input values from Modules
DIOL_1 = (DIOL_mod1.read_data_counts(0, number_of_channels=DIOL_mod1.get_number_of_channels()))
DIOL_2 = (DIOL_mod2.read_data_counts(0, number_of_channels=DIOL_mod2.get_number_of_channels()))
DIOL_3 = (DIOL_mod3.read_data_counts(0, number_of_channels=DIOL_mod3.get_number_of_channels()))
DIOL_4 = (DIOL_mod4.read_data_counts(0, number_of_channels=DIOL_mod4.get_number_of_channels()))
T = (TTC_mod.read_data(0, number_of_channels=TTC_mod.get_number_of_channels()))
AI = (AI_mod.read_data(0, number_of_channels=AI_mod.get_number_of_channels()))

##########################################################
#              Global Flow Rate Variables                #
##########################################################
current_in = [DIOL_1[5], DIOL_1[6], DIOL_1[7], DIOL_1[8], DIOL_1[9], DIOL_2[5], DIOL_2[6],
              DIOL_2[7]]  # used to compare to new_in for flow rate pulse status
pulse_count = [0] * 8  # Total counts since program start, increments from ZERO
flowrate = [0.0] * 8  # flow rate calculated from pulse count and time
# ppg = [151.4, 151.4, 75.7, 75.7, 75.7, 151.4, 151.4, 151.4]  # pulses per gallon as per flow meter specs [corrected]
prev_count = [0] * 8  # Previous pulse count used in calculation of flow rate
prev_time = [time.time()] * 8 # initialize previous time for glow rate calculation


##########################################################
#                     GUI variables                      #
#  These variables are required to be global as they are #
#  referred to in the background as well as foreground   #
##########################################################
pump_text = [0]*8
header = [None] * 8
header2 = [None] * 8
temp_text = [0] * 8     # Tab 1
temp_text2 = [0] * 8    # Tab 2
flow_text = [0] * 8     # Tab 1
flow_text2 = [0] * 8    # Tab 2
shed_temp_text = [0] * 2
shed_temp_text2 = [0] * 2
shed_temp_text21 = [0] * 2
flow_rate_text = [0] * 8
flow_rate_text2 = [0] * 8
delta_t_text = [0]*2
comb_avg = [0]*2        # Combined average for L and R temperature measures inside of SHED
valve_text2 = [0]*2     # Valve position Text
flow_status_gui = [0] * 3   # Flow status as text for each SHED. Cases are further discussed in code
flow_status = [0] *3        # Flow status as a value for each SHED.

SHED1 = False   #SHED1 is off to start
SHED2 = False   #SHED2 is off to start
SHED3 = False   #SHED3 is off to start


##########################################################
#                 Variables for smoothing                #
##########################################################
smoothing_size = 50     # size of list used for smoothing average
smooth_t2 = 0
smooth_t3 = 0
T_shed2 = [0] * smoothing_size      # initiate list as size of smoothing_size
T_shed3 = [0] * smoothing_size

##########################################################
#                  Variables for output                  #
##########################################################
pump_io = [0]*8     # pump status as value [  1 for on, 0 for off ]
set_temp = [43,43] # Set temp can be changed in the GUI. Currently only options are 43 and 23 degrees
delta_t = [0]*2 # the difference between measured SHED temperature and set temp
pid_vout = [10] * 2 # Power Voltage to each valve - 10V is open
alarm_status = [False] *3 # Alarm status starts off as false
door_seal = [0] * 2 # not used in current setup (2020)
exhaust_valve = [0] * 2 # exhaust valve on back of
good_to_start = [0] * 3
extractor_fan = 0 # 0 for off, 1 for on
exhaust_damper = 0 # 0 for open, 1 for closed

##########################################################
#                      Analog Out                        #
##########################################################
AO_mod = maq20.find("VO")
##########################################################
#                     Digital Out                        #
##########################################################

##########################################################
#                  PID Setup values                      #
##########################################################
pid1 = 0
pid2=0
P1 = int(sheet.cell_value(8,1))
I1 = int(sheet.cell_value(9,1))
D1 = int(sheet.cell_value(10,1))
P2 = int(sheet.cell_value(8,2))
I2 = int(sheet.cell_value(9,2))
D2 = int(sheet.cell_value(10,2))

pid1 = PID(P1, I1, D1, set_temp[0]) # PID for SHED2
pid1.output_limits = (0, 10)
pid2 = PID(P2, I2, D2, set_temp[1]) # PID for SHED3
pid2.output_limits = (0, 10)

def flow_check():
    # ---------- Flow / Temperature Status --------- #
    # SHED 1 Flow Status
    if SHED1 is True: #and flowrate[6] > 0 and flowrate[5] > 0:
        if flowrate[5] > flowrate[6]:
            flow_status[0] = 1      # Flow Rate Normal
        else:
            flow_status[0] = 2      # Back Flow in Cold Loop
    elif SHED1 is False:
        flow_status[0] = 0          # SHED off - No Check needed

    #SHED 2 Flow Status
    # This is set up to check both cold and hot flows
    if SHED2 is True:# and flowrate[2] > 0 and flowrate[3] > 0 and flowrate[4] > 0 and flowrate[5] > 0:
        if flowrate[5] > flowrate[3] and flowrate[4] > flowrate[2]:
            flow_status[1] = 1  # Flow rate normal
        else:
            if flowrate[5] < flowrate[3]:
                flow_status[1] = 2  # Back Flow in cold loop
            elif flowrate[4] < flowrate[2]:
                flow_status[1] = 3  # Back Flow in Hot loop
            else:
                flow_status[1] = 4  # unknown Error
    else:
        flow_status[1] = 0  # SHED 2 not on

    # SHED3 Flow Status
    if SHED3 is True:# and flowrate[4] > 0 and flowrate[0] > 0:
        if flowrate[4] > flowrate[0]:
            flow_status[2] = 1  # Flow rate normal
        else:
            flow_status[2] = 3  # Back Flow in Hot Loop
    else:
        flow_status[2] = 0  # SHED 3 not on


def valve_pid1(): # PID for SHED2
    global pid_vout

    if SHED2 == True:
        pid1.setpoint = set_temp[0]
        pid_vout[0] = pid1(comb_avg[0])
        print("current temp SHED2: " + str(comb_avg[0]))
        print( "set point SHED2: " + str(set_temp[0]))
        print ("valve % SHED2: " + str(pid_vout[0] * 10))
        #sleep(1)
    else:
        pid_vout[0] = 10    # set valves open by default


def valve_pid2(): # PID for SHED3
    global pid_vout
    if SHED3 is True:
        pid2.setpoint = set_temp[1]
        pid_vout[1] = pid2(comb_avg[1])
        print("current temp SHED3: " +str(comb_avg[1])+ " deg C")
        print( "set point SHED3: " + str (set_temp[1]) + " deg C")
        print ("valve % SHED3: " + str(pid_vout[1] * 10))
        #sleep(1)
    else:
        pid_vout[1] = 10     # set valves open by default


def update_pump_text(pump_text,i):
    def pump_text_update():
        pump_text[i].configure(text=str(pump_io[i]))    # Pump text 1 for ON 0 for Off
        pump_text[i].after(refresh, pump_text_update)
    pump_text_update()


def read_valve_text(valve_text, i):
    def valve_text_update():
        valve_text[i].configure(text=str(round(pid_vout[i], 2)))
        valve_text[i].after(refresh, valve_text_update)
    valve_text_update()

def pulse_totalizer():
    new_in = [DIOL_1[5], DIOL_1[6], DIOL_1[7], DIOL_1[8], DIOL_1[9], DIOL_2[5], DIOL_2[6],
              DIOL_2[7]]  # used to compare to current_in
    for n in range(0, 8):
        if new_in[n] != current_in[n]:      # Compare New input to current input, if not the same then increase pulse count
            pulse_count[n] += 1             # Increase pulse count
            print("Count" + str(n) + ": " + str(pulse_count[n]))
            current_in[n] = new_in[n]
            flowrate[n] = (((pulse_count[n] - prev_count[n]) / ppg[n]) * 60) / ((time.time() - prev_time[n]))
            prev_count[n] = pulse_count[n]
            prev_time[n] = time.time()
        elif new_in[n] == current_in[n] and (time.time() - prev_time[n]) > .5:
            flowrate[n] = 0.0
        else:
            pass  # print('error')

def flow_calculate(flow_text, n):
    def flow_update():
        # for n in range(0,8):
        flow_text[n].configure(text=round(flowrate[n], 2))
        #print(flowrate[n])
        flow_text[n].after(refresh, flow_update)
    flow_update()


def read_flow_temp(temp_text, i): # used for range i=(0,8) for channel 1-8
    def temp_update():
        # add smoothing function?
        temp_text[i].configure(text=str(round(T[i], 2))) #edits temp_text[i] value
        temp_text[i].after(refresh, temp_update)    # reschedules temp_update function after 100 miliseconds
    temp_update()

    # print(T[0])
    # Thermocouples notation: in list T[n]
    # T0: Shed 3 Hot
    # T1: Shed 3 Cold
    # T2:Shed 2 Hot
    # T3: Shed 2 Cold
    # T4: Main Hot
    # T5: Main Cold
    # T6: Shed1 Cold
    # T7: Shed1 Hot


def read_shed_temp(shed_temp_text, i):  # i to be 0 for SHED2 and 1 for SHED3
    def shed_temp_update():
        global comb_avg, smooth_t2, smooth_t3
        if smooth_t2 == len(T_shed2):
            smooth_t2 = 0
        if smooth_t3 == len(T_shed3):
            smooth_t3 = 0

        # AI = (AI_mod.read_data(0, number_of_channels=AI_mod.get_number_of_channels()))
        # read data from 0-3 for analog input 1-4

        sum2 = (AI[0]*cal1+AI[1]*cal2)/2   # Calibration in Config file
        sum3 = (AI[2]*cal3+AI[3]*cal4)/2   # Calibration in config file

        if 1 > AI[0] > 0.15:
            instant_t2 = sum2  ## Need to calibrate

            # for design purposes Shed 2 is AI0 and Shed 3 is AI1
            T_shed2[smooth_t2] = instant_t2
            smooth_t2 = smooth_t2 + 1

        if 1 > AI[1] > 0.15:
            instant_t3 = sum3  ## Need to calibrate
            T_shed3[smooth_t3] = instant_t3
            smooth_t3 = smooth_t3 + 1
        else:
            None

        ave_T_shed2 = round(sum(T_shed2) / float(len(T_shed2)), 2)
        ave_T_shed3 = round(sum(T_shed3) / float(len(T_shed3)), 2)
        comb_avg = [ave_T_shed2, ave_T_shed3]
        shed_temp_text[i].configure(text=str(comb_avg[i]))
        shed_temp_text[i].after(refresh, shed_temp_update)

    shed_temp_update()


def calc_delta_t(delta_t_text,h):
    def delta_t_update():
        global delta_t
        delta_t[h] = float(comb_avg[h]) - int(set_temp[h])
        delta_t_text[h].configure(text=str(round(delta_t[h], 2)))
        delta_t_text[h].after(refresh,delta_t_update)
    delta_t_update()


def alarm_function():
    global SHED1, SHED2, SHED3, pump_text, extractor_fan, exhaust_valve, exhaust_damper
    if alarm_status[0] == 1:
        exhaust_damper = 1 # closed
        extractor_fan = 1
        SHED1 = False
    else:
        pass

    if alarm_status[1] == 1:    #SHED2 Alarm Activated
        extractor_fan = 1
        exhaust_damper = 1  # closed
        exhaust_valve[0] = 1     # valve open
        SHED2 = False
    else:
        pass

    if alarm_status[2] == 1:
        extractor_fan = 1
        exhaust_damper = 1  # closed
        exhaust_valve[1] = 1
        SHED3 = False
    else:
        pass

def output_control():
    global pump_io, extractor_fan, exhaust_damper, exhaust_valve
    deadhead_protection = 0.1
    valve_op_volt = 5  # operational valve voltage -> changed to 5 for testing on 5V system .

    if SHED1 is True:
        #Valve control
        AO_mod[6] = 10 * valve_op_volt / 10 # Make sure Cold loop for SHED 1 is open 100%
        AO_mod[5] = 5 * valve_op_volt / 10  # adjust Main loop to half open

        if AO_mod[6] > deadhead_protection:
            pump_io[6] = 1
        else:
            pump_io[6] = 0
    else: #IF SHED1 is off turn off pump and make sure valve is in default state and main valve is 100% open
        AO_mod[5] = 10 * valve_op_volt / 10
        AO_mod[6] = 10 * valve_op_volt / 10
        pump_io[6] = 0
        pump_io[5] = 0

    if SHED2 is True: # FOR TESTING PURPOSES. (SHED 2 is not active)

        AO_mod[2] = pid_vout[1] * valve_op_volt / 10
        AO_mod[4] = valve_op_volt - pid_vout[1] * valve_op_volt / 10
        exhaust_valve[0] = 1
        pump_io[3] = 1
        pump_io[2] = 1
    else:
        pump_io[2] = 0 # Hot
        pump_io[3] = 0 # Cold

    if SHED3 is True:
        AO_mod[0] = pid_vout[1] * valve_op_volt / 10
        AO_mod[4] = valve_op_volt - pid_vout[1] * valve_op_volt / 10
        exhaust_valve[1] = 0
        if pid_vout[1] * valve_op_volt > deadhead_protection:
            pump_io[0] = 1
        else:
            pump_io[0] = 0

    else:
        AO_mod[4] = 10 * valve_op_volt / 10     #Valve position open
        AO_mod[0] = 10 * valve_op_volt / 10     #Valve position open
        pump_io[0] = 0

    # main pumps control
    if pump_io[0] + pump_io[2] + pump_io[7] > 0 or SHED3 is True or SHED2 is True:
        pump_io[4] = 1 # Main Hot on if any of the hot pumps are on
    else:
        pump_io[4] = 0

    if pump_io[1] + pump_io[3] + pump_io[6] > 0 or SHED1 is True or SHED2 is True:
        pump_io[5] = 1 # Main Cold pump on if any Cold pump is on
    else:
        pump_io[5] = 0

    def DIOL_output_function():

        DIOL_mod1[0] = pump_io[0] # SHED3 Hot
        DIOL_mod1[1] = pump_io[1] # SHED3 Cool
        DIOL_mod1[2] = pump_io[2] # SHED2 Hot
        DIOL_mod1[3] = pump_io[3] # SHED2 Cool
        DIOL_mod1[4] = pump_io[4] # MAIN Hot
        DIOL_mod2[0] = pump_io[5] # MAIN Cool
        DIOL_mod2[1] = pump_io[6] # SHED1 Cool
        DIOL_mod2[2] = pump_io[7] # SHED1 Hot
        DIOL_mod2[3] = door_seal[0]
        DIOL_mod2[4] = exhaust_valve[0]
        DIOL_mod3[0] = good_to_start[0]
        DIOL_mod3[1] = good_to_start[1]
        DIOL_mod3[2] = good_to_start[2]
        DIOL_mod3[3] = door_seal[1]
        DIOL_mod3[4] = exhaust_valve[1]
        DIOL_mod4[0] = exhaust_damper
        DIOL_mod4[1] = extractor_fan
        DIOL_mod4[2] = 0
        DIOL_mod4[3] = 0
        DIOL_mod4[4] = 0
    DIOL_output_function()

    if SHED1 is True or SHED2 is True or SHED3 is True:
        extractor_fan = 1
        exhaust_damper = 1

        pass

    else:
        extractor_fan = 0
        exhaust_damper = 0


def background_communication():
    global current_in, pulse_count, DIOL_1,DIOL_2,DIOL_3,DIOL_4,T,AI, flowrate,pump_io,  DIOL_mod1

    while True:

        DIOL_1 = (DIOL_mod1.read_data(0, number_of_channels=DIOL_mod1.get_number_of_channels()))
        DIOL_2 = (DIOL_mod2.read_data(0, number_of_channels=DIOL_mod2.get_number_of_channels()))
        DIOL_3 = (DIOL_mod3.read_data_counts(0, number_of_channels=DIOL_mod3.get_number_of_channels()))
        DIOL_4 = (DIOL_mod4.read_data_counts(0, number_of_channels=DIOL_mod4.get_number_of_channels()))
        T = (TTC_mod.read_data(0, number_of_channels=TTC_mod.get_number_of_channels()))
        AI = (AI_mod.read_data(0, number_of_channels=AI_mod.get_number_of_channels()))
        valve_pid1()
        valve_pid2()
        output_control()
        flow_check()
        alarm_function()
        new_in = [DIOL_1[5], DIOL_1[6], DIOL_1[7], DIOL_1[8], DIOL_1[9], DIOL_2[5], DIOL_2[6],
                  DIOL_2[7]]  # used to compare to current_in
        for n in range(0, 8):
            if new_in[n] != current_in[n]:
                pulse_count[n] += 1  # should it be .5? .5 for each up or down?
                print("Count" + str(n) + ": " + str(pulse_count[n]))
                current_in[n] = new_in[n]
                flowrate[n] = (((pulse_count[n] - prev_count[n]) / ppg[n]) * 60) / ((time.time() - prev_time[n]))
                prev_count[n] = pulse_count[n]
                prev_time[n] = time.time()
            elif new_in[n] == current_in[n] and (time.time()-prev_time[n]) > .5:
                flowrate[n] = 0.0
            else:
                pass#print('error')
        if exit_case == True:
            pump_io = [0] * 8
            DIOL_mod1[0] = 0
            DIOL_mod1[1] = 0
            DIOL_mod1[2] = 0
            DIOL_mod1[3] = 0
            DIOL_mod1[4] = 0
            DIOL_mod2[0] = 0
            DIOL_mod2[1] = 0
            DIOL_mod2[2] = 0
            sys.exit()





def GUI():
    window = tk.Tk()
    window.title('SHED Auxiliary Control')
    #window.iconbitmap('CAicon.ico')
    window.maxsize(XX, YY)
    window.minsize(XX,YY)
    #window.wm_attributes("-transparentcolor", 'gold')   #Set transparent colour - makes screen transparent to desktop
    tab_control = ttk.Notebook(window)
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab3 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Auxiliary Health')
    tab_control.add(tab2, text="Automatic SHED control")
    tab_control.add(tab3, text='Flow Diagram')
    tab_control.pack(expand=2, fill='both')

########################################################################################################################

    application_window = tab1

########################################################################################################################
    temp_label = Label(application_window, text='Flow Temperatures:', font=("Bold", 15))
    temp_label.grid(column=0, row=1)
    flow_label = Label(application_window, text="Flow Rate (GPM)", font=("Bold", 15))
    flow_label.grid(column=0, row=2)
    header[0] = Label(application_window, text="SHED3 HOT")
    header[1] = Label(application_window, text="SHED3 COLD")
    header[2] = Label(application_window, text="SHED2 HOT")
    header[3] = Label(application_window, text="SHED2 COLD")
    header[4] = Label(application_window, text="Main HOT")
    header[5] = Label(application_window, text="Main COLD")
    header[6] = Label(application_window, text="SHED1 COLD")
    header[7] = Label(application_window, text="SHED1 HOT")
    header2[0] = Label(application_window, text="SHED1 Temp")
    header2[1] = Label(application_window, text="SHED2 Temp")
    header2[2] = Label(application_window, text="SHED3 Temp")
    for h in range(0, 2):
        header2[h + 1].grid(column=h + 1, row=4)
        shed_temp_text[h] = Label(application_window)
        shed_temp_text[h].grid(column=h + 1, row=5)
        read_shed_temp(shed_temp_text, h)
    for n in range(0, 8):
        header[n].grid(column=n + 1, row=0, padx=10, pady=5)
        temp_text[n] = Label(application_window)
        temp_text[n].grid(column=n + 1, row=1)
        read_flow_temp(temp_text, n)
        flow_text[n] = Label(application_window)  # str(flowrate[0]))
        flow_text[n].grid(row=2, column=n+1)
        flow_calculate(flow_text, n)
########################################################################################################################
    application_window = tab2
########################################################################################################################

    def start_btn1_clicked():
        global SHED1
        start_btn1.configure(text="Stop", command=start_btn1_stop,
                             bg="red")  # = Button(application_window, text="Start", command=start_btn1_clicked)
        SHED1 = True

        for j in range(0, 8):
            pump_text[j].configure(text=str(pump_io[j]))
        # Check Flowrate and Temperatures

        # Temp SHED1 Cold <15 degC, Main Cold <15 degC (FOR MORE THAN 5 MINS)
        # Flowrate SHED1 COLD >____________ PROGRESS BAR
        # Flowrate SHED1 COLD < MAIN COLD
        # Alarm = False
        # If Above is complete then Ready to run signal can be sent

    def start_btn1_stop():
        global SHED1
        SHED1 = False
        start_btn1.configure(text="Start", command=start_btn1_clicked,
                             bg="green")  # = Button(application_window, text="Start", command=start_btn1_clicked)
        # start_btn1.grid(column=1, row=1)

        for j in range(0, 8):
            pump_text[j].configure(text=str(pump_io[j]))

    def start_btn2_clicked():
        global SHED2
        SHED2 = True
        start_btn2.configure(text="Stop", command=start_btn2_stop,
                             bg="red")  # = Button(application_window, text="Start", command=start_btn1_clicked)


        for j in range(0, 8):
            pump_text[j].configure(text=str(pump_io[j]))
        # Exhaust Fan ON
        # Check Exhaust Flow
        # Check Flowrate and Temperatures
        # Temp SHED3 Hot > 45 degC, Main Hot >45 degC
        # Delta SHED3 Hot, Main Hot < 5 degC
        # Flowrate SHED3 HOT >____________
        # Flowrate SHED3 HOT < MAIN
        # SHED3 Temperature = Setpoint +/- 3 degC
        # Alarm = False
    def start_btn2_stop():
        global SHED2
        start_btn2.configure(text="Start", command=start_btn2_clicked,
                             bg="green")  # = Button(application_window, text="Start", command=start_btn1_clicked)
        SHED2 = False

        for j in range(0, 8):
            pump_text[j].configure(text=str(pump_io[j]))

    def start_btn3_clicked():
        global SHED3
        SHED3 = True
        start_btn3.configure(text="Stop", command=start_btn3_stop,
                             bg="red")  # = Button(application_window, text="Start", command=start_btn1_clicked)

        # Main Pump HOT ON, SHED3 Pump hot ON

        for j in range(0, 8):
            pump_text[j].configure(text=str(pump_io[j]))
        # Exhaust Fan ON
        # Check Exhaust Flow
        # Check Flowrate and Temperatures
        # Temp SHED3 Hot > 45 degC, Main Hot >45 degC
        # Delta SHED3 Hot, Main Hot < 5 degC
        # Flowrate SHED3 HOT >____________
        # Flowrate SHED3 HOT < MAIN
        # SHED3 Temperature = Setpoint +/- 3 degC
        # Alarm = False
    def start_btn3_stop():
        global SHED3
        SHED3 = False
        start_btn3.configure(text="Start", command=start_btn3_clicked,
                             bg="green")  # = Button(application_window, text="Start", command=start_btn1_clicked)
        # start_btn1.grid(column=1, row=1)


        for j in range(0, 8):
            pump_text[j].configure(text=str(pump_io[j]))

    table_label = ["Request to Start",
                   "SHED Temp. Status",
                   "SHED Temp. (deg C)",
                   "SHED set point (deg C)",
                   "Delta T",
                   "Valve (V)",
                   "Flow Temp. Status",
                   "Flow Status",
                   "Request for Exhaust Fan",
                   "Exhaust Damper Position",
                   "LEL Alarm"
                   ]
    Label(application_window, text = "SHED 1").grid(column=1, row=0)
    Label(application_window, text = "SHED 2").grid(column=2, row=0)
    Label(application_window, text = "SHED 3").grid(column=3, row=0)
    Label(application_window, text = "Status").grid(column=0, row=1)
    for j in range(0,len(table_label)):
        Label(application_window, text=table_label[j], padx=5, pady=5).grid(column=0, row=(j+1))

    start_btn1 = Button(application_window, text="Start", command=start_btn1_clicked, bg='green')
    start_btn2 = Button(application_window, text="Start", command=start_btn2_clicked, bg='green')
    start_btn3 = Button(application_window, text="Start", command=start_btn3_clicked, bg='green')
    start_btn1.grid(column=1, row=1)
    start_btn2.grid(column=2, row=1)
    start_btn3.grid(column=3, row=1)

    if alarm_status[1] == 1:
        start_btn2_stop()
    if alarm_status[2] == 1:
        start_btn3_stop()

    pump_label = ["SHED3 Hot",
                  "SHED3 Cold",
                  "SHED2 Hot",
                  "SHED2 Cold",
                  "MAIN Hot",
                  "MAIN Cold",
                  "SHED1 Cold",
                  "SHED1 Hot"
                  ]
    for j in range(0, len(pump_label)):
        Label(application_window, text=pump_label[j], padx=20, pady=5).grid(column=5, row=1+j)
    component_list = ["Pump Status",
                      "Temperature",
                      "Flow Rate"
                      ]
    for j in range(0, len(component_list)):
        Label(application_window, text = component_list[j], padx=10, pady=10).grid(column= 6+j, row = 0)


    for n in range(0, 8):
        pump_text[n] = Label(application_window, text= str(pump_io[n]), padx=5,pady=5)
        pump_text[n].grid(column=6, row=1+n)
        update_pump_text(pump_text,n)
        temp_text2[n] = Label(application_window)
        temp_text2[n].grid(column=7, row=1+n)
        read_flow_temp(temp_text2, n)
        flow_text2[n] = Label(application_window)
        flow_text2[n].grid(column=8, row=1+n)
        flow_calculate(flow_text2, n)

    ##SHED TEMPERATURE ###
    for h in range(0, 2):
        shed_temp_text2[h] = Label(application_window)
        shed_temp_text2[h].grid(column=h + 2, row=3)
        read_shed_temp(shed_temp_text2, h)
    def get_set_temp2(event):
        global set_temp
        set_temp[0] = float(temp_set2.get())
    def get_set_temp3(event):
        global set_temp
        set_temp[1] = float(temp_set3.get())
    ## SHED SET POINT ###
    temp_set2 = Combobox(application_window, width = 5, justify = CENTER , state= "readonly", values = [23,43])
    temp_set2.current(1)
    temp_set2.bind("<<ComboboxSelected>>", get_set_temp2)
    temp_set2.grid(column=2,row=4)
    temp_set3 = Combobox(application_window, width = 5, justify = CENTER, state= "readonly", values = [23,25,26,27,28,29,30,35,40,43])
    temp_set3.current(1)
    temp_set3.bind("<<ComboboxSelected>>", get_set_temp3)
    temp_set3.grid(column=3,row=4)


    ## DELTA T ##
    for h in range (0,2):
        delta_t_text[h] = Label(application_window)
        delta_t_text[h].grid(column=h + 2, row=5)
        calc_delta_t(delta_t_text,h)
    ##Valve Voltage ##
    for h in range(0,2):
        valve_text2[h] = Label(application_window)
        valve_text2[h].grid(column= h+2, row = 6)
        read_valve_text(valve_text2,h)


    # Progress bar for SHED2 and SHED3 Temperature
    progress_temp2 = Progressbar(application_window, orient=HORIZONTAL, length=75)#, mode = 'indeterminate')
    progress_temp3 = Progressbar(application_window, orient=HORIZONTAL, length=75)
    progress_temp2.grid(column=2, row=2)
    progress_temp3.grid(column= 3, row =2)

    def bar_temp():
        def refresh_val():
            progress_temp2.configure(value=75 * comb_avg[0] / float(temp_set2.get()))
            progress_temp3.configure(value=75 * comb_avg[1] / float(temp_set3.get()))
            progress_temp2.after(10, refresh_val)
        refresh_val()
    bar_temp()

    progress_flowtemp1 = Progressbar(application_window, orient=HORIZONTAL, length=75)
    progress_flowtemp2 = Progressbar(application_window, orient=HORIZONTAL, length=75)
    progress_flowtemp3 = Progressbar(application_window, orient=HORIZONTAL, length=75)
    progress_flowtemp1.grid(column=1, row=7)
    progress_flowtemp2.grid(column=2, row=7)
    progress_flowtemp3.grid(column= 3, row =7)

    def flow_status_update(flow_status_gui, h):
        def update():
            global flow_status_gui
            if flow_status[h] == 0:
                flow_status_gui[h].configure(text="SHED"+str(h+1)+ " off", bg = "light grey")
            if flow_status[h] == 1:
                flow_status_gui[h].configure(text="Flow is Good")
            if flow_status[h] == 2:
                flow_status_gui[h].configure(text="Back flow in Cool Loop", bg = "red")
            if flow_status[h] == 3:
                flow_status_gui[h].configure(text="Back flow in Hot Loop", bg= "red")
            if flow_status[h] == 4:
                flow_status_gui[h].configure(text="Unknown Error", bg = "red")
            flow_status_gui[h].after(refresh, update)
        update()
    for h in range (0,3):
        flow_status_gui[h] = Label(application_window)
        flow_status_gui[h].grid(column = h+1, row=8)
        flow_status_update(flow_status_gui,h)

    def extractor_status(extractor_fan_label):
        def update():
            if extractor_fan == 1:
                extractor_fan_label.configure(text="                             Exhaust Fan ON                             ", bg = 'green', fg='black')
            else:
                extractor_fan_label.configure(
                    text="                             Exhaust Fan OFF                             ", bg='black',
                    fg='white')
            extractor_fan_label.after(refresh, update)
        update()
    extractor_fan_label = Label(application_window)
    extractor_fan_label.grid(column = 1, columnspan = 3, row = 9)
    extractor_status(extractor_fan_label)

    def exhaust_damper_status(exhaust_damper_label):
        def update():
            if exhaust_damper == 1:
                exhaust_damper_label.configure(
                    text="                      Exhaust Damper CLOSED                       ", bg='green',
                    fg='black')
            else:
                exhaust_damper_label.configure(
                    text="                            Exhaust Damper OPEN                           ", bg='black',
                    fg='white')
            exhaust_damper_label.after(refresh, update)

        update()

    exhaust_damper_label = Label(application_window)
    exhaust_damper_label.grid(column=1, columnspan=3, row=10)
    exhaust_damper_status(exhaust_damper_label)


    def reset_alarm():
        global alarm_status

        alarm_status = [0, 0, 0]
        LEL_btn1.configure(text="Test Alarm", command=alarm1, bg='green')
        LEL_btn2.configure(text="Test Alarm", command=alarm2, bg='green')
        LEL_btn3.configure(text="Test Alarm", command=alarm3, bg='green')

    def alarm1():
        global extractor_fan
        alarm_status[0] = 1
        start_btn1_stop()
        pump_io[5]
        pump_io[6] = 1
        LEL_btn1.configure(text = "reset Alarm", command = reset_alarm, bg='red')
        messagebox.showerror("Warning", "Please acknowledge Alarm for SHED1")



    def alarm2():
        alarm_status[1] = 1
        start_btn2_stop()
        LEL_btn2.configure(text="reset Alarm", command=reset_alarm, bg='red')
        messagebox.showerror("Warning", "Please acknowledge Alarm for SHED2")

    def alarm3():
        alarm_status[2] = 1
        start_btn3_stop()
        LEL_btn3.configure(text="reset Alarm", command=reset_alarm, bg='red')

        messagebox.showerror("Warning", "Please acknowledge Alarm for SHED3")

    LEL_btn1 = Button(application_window, text="Alarm Test1", command=alarm1, bg='green')
    LEL_btn2 = Button(application_window, text="Alarm Test2", command=alarm2, bg='green')
    LEL_btn3 = Button(application_window, text="Alarm Test3", command=alarm3, bg='green')
    LEL_btn1.grid(column=1, row=11)
 hEL_btn3.grid(column=3, row=11)

########################################################################################################################
    application_window = tab3
    canvas = Canvas(application_window, width = XX-50,height=YY-50,bg='grey')
    canvas.pack()
    #image = Image.open("display/Pump.png")
    #image = image.rotate(-90)
    #pump_vert = ImageTk.PhotoImage(image.resize((30,30)))

    #image = image.rotate(180)
    #pump_main_image = ImageTk.PhotoImage(image.resize((30,30)))



    #symb_pump = (img2)

########################################################################################################################


    p1x = 250
    p2x = p1x+50
    p3x = p2x+100
    p4x = p3x+50
    p7x = p4x+100
    p8x = p7x+50
    p5x = 100
    p6x = p5x+0
 72 p1y = 100
    p5y = 300
    #canvas.create_image(p1x, p1y, image=pump_vert, anchor=NW)
    #canvas.create_image(p2x, p1y, image=pump_vert, anchor=NW)
    #canvas.create_image(p3x, p1y, image=pump_vert, anchor=NW)
    #canvas.create_image(p4x, p1y, image=pump_vert, anchor=NW)
    #canvas.create_image(p5x, p5y, image=pump_main_image, anchor=NW)
    #canvas.create_image(p6x, p5y, image=pump_main_image, anchor=NW)
    #canvas.create_image(p7x, p1y, image=pump_vert, anchor=NW)
    #canvas.create_image(p8x, p1y, image=pump_vert, anchor=NW)

    def stop_program():
        global DIOL_mod1,exit_case,  AO_mod, pump_io, SHED1, SHED2, SHED3
        if messagebox.askokcancel("Quit", "       Do you want to quit?\nThis will terminate everything"):
            SHED1 = False
            SHED2 = False
            SHED3 = False
            exit_case = True
            sys.exit()
    window.protocol('WM_DELETE_WINDOW',stop_program)
    window.mainloop()


if maq20[1] is None:
    raise TypeError("Module Not Found.\n Connect DATAFORTH system and ensure proper IP address!")

background_thread = threading.Thread(target=background_communication)
GUI_thread = threading.Thread(target=GUI)


background_thread.start()
GUI_thread.start()
