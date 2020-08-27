import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import *
import threading
from simple_pid import PID
import xlrd
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from pandas import *
import pandas as pd
import csv
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import random

LARGE_FONT = ("Verdana", 12)
REG_FONT = ("Verdana", 9)


exit_case = False  # when set to true all threads will close properly
SHED1 = False      # to keep track of SHED status
SHED2 = False
SHED3 = False
ref_rate = 100  # refresh rate of value on GUI, might be updated via config file
loc = ("config/config.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
ip = sheet.cell_value(1, 1)
ref_rate = int(sheet.cell_value(2, 1))
XX = int(sheet.cell_value(3, 1))
YY = int(sheet.cell_value(4, 1))
ppg = [0] * 8
for n in range(0, 8):
    ppg[n] = float(        sheet.cell_value(6, n + 1))  # Update Pulses per gallon according to the Manufacturer's Specs
##########################################################
#                  PID Setup values                      #
##########################################################
pid1 = 0
pid2 = 0
P1 = int(sheet.cell_value(8,1))
I1 = int(sheet.cell_value(9,1))
D1 = int(sheet.cell_value(10,1))
P2 = int(sheet.cell_value(8,2))
I2 = int(sheet.cell_value(9,2))
D2 = int(sheet.cell_value(10,2))

set_temp = [25,25]
pid1 = PID(P1, I1, D1, set_temp[0]) # PID for SHED2
pid1.output_limits = (0, 10)
pid2 = PID(P2, I2, D2, set_temp[1]) # PID for SHED3
pid2.output_limits = (0, 10)

###################################################################################
###                 Temperature Sensor smoothing and calibration                ###
###################################################################################
smoothing_size = int(sheet.cell_value(17,1))    # size of list used for smoothing average
smooth_t2 = 0
smooth_t3 = 0
T_shed2 = [20] * smoothing_size      # initiate list as size of smoothing_size with base
T_shed3 = [20] * smoothing_size


# Calibration Values for SHED temperature sensors
cal1 = sheet.cell_value(12, 1)
cal2 = sheet.cell_value(13, 1)
cal3 = sheet.cell_value(14, 1)
cal4 = sheet.cell_value(15, 1)


#######################################################################################################################
###                                              GUI stuff                                                          ###
#######################################################################################################################
index=0
flash_index = 0

flow_width = 8
pump_width = 5
flow_temp_width = 8
valve_width = 10



def flash__(): # flash function for GUI flashing
    global flash_index
    flash_index = 1- flash_index

#######################################################################################################################
###                                   Input Variable Definition                                                     ###
#######################################################################################################################
demo = 1
if demo == 0:
    from maq20 import MAQ20

    maq20 = MAQ20(ip_address=ip, port=502)  # Set communication with MAQ20
    AI_mod = maq20[1]  # Analog input module
    TTC_mod = maq20[2]  # Thermocouple input module.
    DIV20_mod = maq20[4]  # 20 digital discrete inputs
    DIOL_mod1 = maq20[5]  # 5 Digital discrete inputs, 5 Digital outputs
    DIOL_mod2 = maq20[6]  # 5 Digital discrete inputs, 5 Digital outputs
    DIOL_mod3 = maq20[7]  # 5 Digital discrete inputs, 5 Digital outputs
    DIOL_mod4 = maq20[8]  # 5 Digital discrete inputs, 5 Digital outputs
    AO_mod = maq20.find("VO")

    # Read input values from Modules
    DIOL_1 = (DIOL_mod1.read_data_counts(0, number_of_channels=DIOL_mod1.get_number_of_channels()))
    DIOL_2 = (DIOL_mod2.read_data_counts(0, number_of_channels=DIOL_mod2.get_number_of_channels()))
    DIOL_3 = (DIOL_mod3.read_data_counts(0, number_of_channels=DIOL_mod3.get_number_of_channels()))
    DIOL_4 = (DIOL_mod4.read_data_counts(0, number_of_channels=DIOL_mod4.get_number_of_channels()))
    T = (TTC_mod.read_data(0, number_of_channels=TTC_mod.get_number_of_channels()))
    AI = (AI_mod.read_data(0, number_of_channels=AI_mod.get_number_of_channels()))

    ser = serial.Serial(
        port='/dev/ttyS0',  # Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
if demo == 1:
    AI_mod = [0] * 8  # Analog input module
    TTC_mod = [0] * 8  # Thermocouple input module.
    DIV20_mod = [0] * 20  # 20 digital discrete inputs
    DIOL_mod1 = [0] * 10  # 5 Digital discrete inputs, 5 Digital outputs
    DIOL_mod2 = [0] * 10  # 5 Digital discrete inputs, 5 Digital outputs
    DIOL_mod3 = [0] * 10  # 5 Digital discrete inputs, 5 Digital outputs
    DIOL_mod4 = [0] * 10  # 5 Digital discrete inputs, 5 Digital outputs
    AO_mod = [0] * 10

    # Read input values from Modules
    DIOL_1 = [0] * 10
    DIOL_2 = [0] * 10
    DIOL_3 = [0] * 10
    DIOL_4 = [0] * 10
    T = [0] * 8
    AI = [0] * 8
    flowrate_value = [0]*8


def read_serial():
    global frequency, flowrate, prev_count, prev_time
    current_time = time.time()
    sample_time = current_time - prev_time

    # while 1:  # not needed  if function is in while loop
    readchar = ser.readline().decode().rstrip("\n")  # Read Serial, decode, take off '\n' character at end of input
    # print("Decoded Input: " + readchar)
    split_char = readchar.split(',')  # split sting into list by commas
    fixed_str = [i.strip('"\x00#') for i in split_char]  # take off "\x00#" from anywhere in list
    try:  # to prevent " ValueError: invalid literal for int() with base 10: ''"
        current_count = list(map(int, fixed_str))  # change string to integers for purpose of use in calculations
        # print (current_count)
        for n in range(0, 8):
            frequency[n] = (current_count[n] - prev_count[n]) * 60 / sample_time  # pulse per minute
            flowrate.at[n, 'Raw Value'] = frequency[n] / ppg[n]  # Flowrate in Gallons/min
            # print("Pump number " + str(n) + "\nFrequency is: " + str(frequency[n]) + " Pulses Per Minute!\nFlowrate is: " + str(flowrate[n]) + " GPM")

        prev_count = current_count
        prev_time = current_time

        return flowrate
    except:
        return
    # print(fixed_str)
    # print( fixed_str[1], type(fixed_str[1]))
    # print(current_count, type(current_count))
    # print(fixed_int[1],type(fixed_int[1]))
# update functions to be used for demo or non-demo
def update_maq20():# include function if connected to MAQ20
    global DIOL_1,DIOL_2,DIOL_3,DIOL_4, T, AI
    DIOL_1 = (DIOL_mod1.read_data(0, number_of_channels=DIOL_mod1.get_number_of_channels()))
    DIOL_2 = (DIOL_mod2.read_data(0, number_of_channels=DIOL_mod2.get_number_of_channels()))
    DIOL_3 = (DIOL_mod3.read_data_counts(0, number_of_channels=DIOL_mod3.get_number_of_channels()))
    DIOL_4 = (DIOL_mod4.read_data_counts(0, number_of_channels=DIOL_mod4.get_number_of_channels()))
    T = (TTC_mod.read_data(0, number_of_channels=TTC_mod.get_number_of_channels()))
    AI = (AI_mod.read_data(0, number_of_channels=AI_mod.get_number_of_channels()))
    read_serial()
def update_unhooked(): # update data with random integers to check functionality
    global DIOL_1, DIOL_2, DIOL_3, DIOL_4, T, AI
    for i in range (0,5):
        DIOL_1[i] = random.randint(0,1)
        DIOL_2[i] = random.randint(0,1)
        DIOL_3[i] = random.randint(0,1)
        DIOL_4[i] = random.randint(0,1)
    for i in range (0,8):
        T[i] = random.uniform(10,65)
        AI[i] = random.uniform(0.5,.6)
        flowrate_value[i] = random.uniform(4.5,5)

# RAW Values for IO to/from maq20
pump_io = [0]*8               # output digital: p1 is 0 in list
valve_pos = [0]*8             # output analog
flow_pulse = [0]*8          # input From Serial Port
SHED_req_to_start = [False]*3   # 0: SHED1, 1:SHED2, 2:SHED3 |  | digital input: 0 for no request, 1 for request
SHED_good_to_start = [False]*3  # 0: SHED2, 1: SHED2 |  | digital output: 0 for not ready, 1 for ready
door_seal = [0]*2           # 0: SHED2, 1: SHED2 |  | digital output: 0 for open, 1 for seal
exhaustfan_request = 0      # Main Fan |  | digital output: 0 for no request, 1 for request
exhaustfan_feedback = 0     # Main Fan feedback |  | digital input: 0 for off, 1 for on
exhaust_damper = 1          # Main Fan Bypass |  | digital output: 0 for closed, 1 for open (closed for alarms)
SHED_exhaust_valve = [0]*2  # 0:SHED2, 1:SHED3 |  | digital output: 0 for closed, 1 for open


#calculated values:
flowrate_value = [0.0] *8   # Flowrate calculated from read_serial Function
SHED_temp = [0.0]*2         # 0: SHED2, 1: SHED3
SHED_pid = [0]*8            # 0: SHED2, 1: SHED3 calculated pid value

# text values from RAW Values
pump_text = ['']*8          # on, off interpreted from raw value
valve_text = ['']*8         # Valve position as text
flowrate_text = ['']*8
flow_temp_text = [''] *8
SHED_temp_text = [''] *2
SHED_exhaust_valve_text = ['']*2
exhaustfan_request_text = ''
exhaustfan_feedback_text = ''

flowrate_text_tab1 = [''] * 8
pump_text_tab1 = [''] * 8
flow_temp_text_tab1 = [''] * 8
valve_text_tab1 = [''] * 8
flow_valve_text_tab1 = ['']*8


def calculated_values_update():
    global SHED_temp, smooth_t2, smooth_t3
    if smooth_t2 == len(T_shed2):
        smooth_t2 = 0
    if smooth_t3 == len(T_shed3):
        smooth_t3 = 0

    # AI = (AI_mod.read_data(0, number_of_channels=AI_mod.get_number_of_channels()))
    # read data from 0-3 for analog input 1-4

    sum2 = ((AI[0]) * cal1 + (AI[1]) * cal2) / 2  # Calibration in Config file
    sum3 = ((AI[2]) * cal3 + (AI[3]) * cal4) / 2  # Calibration in config file

    if 1 > AI[0] > 0.15:  # To filter outliers
        instant_t2 = sum2  ## Need to calibrate

        # for design purposes Shed 2 is AI0 and Shed 3 is AI1
        T_shed2[smooth_t2] = instant_t2
        smooth_t2 = smooth_t2 + 1

    if 1 > AI[1] > 0.15:  # To filter outliers
        instant_t3 = sum3  ## Need to calibrate
        T_shed3[smooth_t3] = instant_t3
        smooth_t3 = smooth_t3 + 1
    else:
        None

    ave_T_shed2 = round(sum(T_shed2) / float(len(T_shed2)), 2)
    ave_T_shed3 = round(sum(T_shed3) / float(len(T_shed3)), 2)
    SHED_temp = [ave_T_shed2, ave_T_shed3]

def text_update(): #Variable update function. to be used to update variables
    global pump_text, valve_text, flowrate_text, flow_temp_text, SHED_temp_text
    if demo == 1:
        update_unhooked()
    if demo == 0:
        update_maq20()

    for i in range(0,8):
        # pumps
        if pump_io[i] == 0:
            pump_text[i] = 'off'
        elif pump_io[i] == 1:
            pump_text[i] = 'on'
        else:
            pump_text[i] = 'error'
        # valves:
        valve_text[i] = str(round(100*valve_pos[i]/10,2)) +'%'
        flowrate_text[i] = str(round(flowrate_value[i],2)) + ' GPM'
        flow_temp_text[i] = str(round(T[i], 2))+ u' \N{DEGREE SIGN}'+"C"

    for i in range(0,2):
        SHED_temp_text[i] = str(SHED_temp[i])+ u' \N{DEGREE SIGN}'+"C"








text_update()

class SHEDoperation(tk.Frame):

    def __init__(self,parent, controller):

        def SHED_btn1_clicked():
            global SHED1, SHED_req_to_start
            SHED1 = True
            SHED_req_to_start[0] = True
            if SHED_good_to_start[0]:
                start_btn1.configure(text='SHED1: Operational', bg='green', command=SHED_btn1_stop)
            else:
                start_btn1.configure(text='SHED1: Start Request SENT', bg = 'yellow', command = SHED_btn1_stop)

        def SHED_btn1_stop():
            global SHED1, SHED_req_to_start
            SHED1 = False
            SHED_req_to_start[0] = False
            start_btn1.configure(text="SHED1: Request to Start", command=SHED_btn1_clicked,
                                 bg="red")

        def SHED_btn2_clicked():
            global SHED2, SHED_req_to_start
            SHED2 = True
            SHED_req_to_start[1] = True
            if SHED_good_to_start[1]:
                start_btn2.configure(text='SHED2: Operational', bg='green', command=SHED_btn2_stop)
            else:
                start_btn2.configure(text='SHED2: Start Request SENT', bg = 'yellow', command = SHED_btn2_stop)

        def SHED_btn2_stop():
            global SHED2, SHED_req_to_start
            SHED2 = False
            SHED_req_to_start[1] = False
            start_btn2.configure(text="SHED2: Request to Start", command=SHED_btn2_clicked,
                                 bg="red")

        def SHED_btn3_clicked():
            global SHED3, SHED_req_to_start
            SHED3 = True
            SHED_req_to_start[2] = True
            if SHED_good_to_start[2]:
                start_btn3.configure(text='SHED3: Operational', bg='green', command=SHED_btn3_stop)
            else:
                start_btn3.configure(text='SHED3: Start Request SENT', bg = 'yellow', command = SHED_btn3_stop)

        def SHED_btn3_stop():
            global SHED3, SHED_req_to_start
            SHED3 = False
            SHED_req_to_start[2] = False
            start_btn3.configure(text="SHED3: Request to Start", command=SHED_btn3_clicked,
                                 bg="red")
        tk.Frame.__init__(self,parent)
        start_btn1 = Button(self, width=25, font =LARGE_FONT)
        start_btn2 = Button(self, width=24, font =LARGE_FONT)
        start_btn3 = Button(self, width=24, font =LARGE_FONT)
        manual_btn = Button(self, width=25, font =LARGE_FONT, text = "Enter Manual Mode")

        if not SHED1:
            start_btn1.configure(text="SHED1: Request to Start", command=SHED_btn1_clicked, bg = 'red', font =LARGE_FONT)
        else:
            if SHED_good_to_start[0]:
                start_btn1.configure (text="SHED1: Request to Start Sent", bg = 'yellow', command=SHED_btn1_stop)
            else:
                start_btn1 = Button()

        if not SHED2:
            start_btn2.configure(text="SHED2: Request to Start", command=SHED_btn2_clicked, bg = 'red', font =LARGE_FONT)
        else:
            if SHED_good_to_start[1]:
                start_btn2.configure (text="SHED2: Request to Start Sent", bg = 'yellow', command=SHED_btn2_stop)
            else:
                start_btn2 = Button()

        if not SHED3:
            start_btn3.configure(text="SHED3: Request to Start", command=SHED_btn3_clicked, bg = 'red', font =LARGE_FONT)
        else:
            if SHED_good_to_start[2]:
                start_btn3.configure (text="SHED3: Request to Start Sent", bg = 'yellow', command=SHED_btn3_stop)
            else:
                start_btn3 = Button()

        start_btn1.grid(column=0, row=0)

        start_btn2.grid(column=1, row=0)

        start_btn3.grid(column=2, row=0)

        manual_btn.grid(column=3, row=0)

class FlowDisplay(tk.Frame):
    def __init__(self, parent, controller):
        ttk.LabelFrame.__init__(self, parent, text = "Main Loop")
        mainframe = FlowMain(parent, self)
        mainframe.pack()

def flow_calculate(flow_text, n):
    def flow_update():
        txt = ''
        # for n in range(0,8):
        flow_text[n].configure(text="Flowrate \n" + str(round(flowrate_value[n], 2)) + " GPM")
        #print(flowrate[n])
        flow_text[n].after(ref_rate, flow_update)
    flow_update()
def pump_status(pump_text,i):
    def pump_text_update():
        x = 0
        txt = ""

        if pump_io[i] == 0:
            txt = "Pump" + str(i + 1) + "\nOFF"
            pump_text[i].configure(text=txt, bg="black", fg="white")  # Pump text 1 for ON 0 for Off


        elif pump_io[i] == 1:
            txt = "Pump" + str(i + 1) + "\nON"
            if pump_error[i] == 0:
                pump_text[i].configure(text=txt, bg="green", fg="black")  # Pump text 1 for ON 0 for Off

            if pump_error[i] == 1:
                bgflash = ("black", "red")
                pump_text[i].configure(bg=bgflash[flash_index])
        else:
            txt = "error"
        pump_text[i].configure(text=txt)  # Pump text 1 for ON 0 for Off
        pump_text[i].after(ref_rate, pump_text_update)

    pump_text_update()

def flow_temp_status(temp_text,n):
    def temp_text_update():
        txt = ""
        txt = "Temp." + str(n + 1) + "\n" +str(round(T[n],2)) + u'\N{DEGREE SIGN}'+"C"
        temp_text[n].configure(text=txt, bg="black", fg="white")  # Pump text 1 for ON 0 for Off
        temp_text[n].after(ref_rate, temp_text_update)
    temp_text_update()

def valve_position(valve_text,n):
    def valve_text_update():
        txt=""
        txt="Valve Pos." + str(n+1) + "\n" + str(round(100*valve_pos[n]/10,2)) +"%"
        valve_text[n].configure(text=txt)
        valve_text[n].after(ref_rate, valve_text_update)
    valve_text_update()


class FlowMain(tk.Frame):

    def __init__(self,parent,controller):
        ttk.LabelFrame.__init__(self, text = "Main Loop")
        hotLabel0 = Label(self, text="Hot", font=("Bold", 10), padx=9)
        coldLabel0 = Label(self, text="Cold", font=("Bold", 10), padx=9)
        hotLabel0.grid(row=2, column=0)
        coldLabel0.grid(row=3, column=0)
        flowrate_text_tab1[4] = Label(self, padx=10, width=flow_width)
        flowrate_text_tab1[5] = Label( self, padx=10, width=flow_width)
        flowrate_text_tab1[4].grid(row=2, column=2)
        flowrate_text_tab1[5].grid(row=3, column=2)
        pump_text_tab1[4] = Label(self, padx=10, width=pump_width)
        pump_text_tab1[5] = Label(self, padx=10, width=pump_width)
        pump_text_tab1[4].grid(row=2, column=1)
        pump_text_tab1[5].grid(row=3, column=1)
        flow_temp_text_tab1[4] = Label(self, padx=10, width=flow_temp_width)
        flow_temp_text_tab1[5] = Label(self, padx=10, width=flow_temp_width)
        flow_temp_text_tab1[4].grid(row=2, column=3)
        flow_temp_text_tab1[5].grid(row=3, column=3)
        flow_valve_text_tab1[4] = Label(self, padx=10, width=valve_width)
        flow_valve_text_tab1[5] = Label(self, padx=10, width=valve_width)
        flow_valve_text_tab1[4].grid(row=2, column=4)
        flow_valve_text_tab1[5].grid(row=3, column=4)

        for n in range(4, 6):
            pump_status(pump_text_tab1, n)
            flow_calculate(flowrate_text_tab1, n)
            flow_temp_status(flow_temp_text_tab1, n)
            valve_position(flow_valve_text_tab1, n)




class MainApplication(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)  # Was causing extra frame to pop up

        self.root = tk.Frame()  # create instance of Tk
        self.root.pack()
        self.start_frame = ttk.Frame(self.root)
        self.start_frame.pack(pady = 10)
        self.start_btns = SHEDoperation(self.start_frame,self)
        self.start_btns.pack()
        #self.root.title("SHED Auxiliary Control V2")
        self.tabControl = ttk.Notebook(self.root)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text='Auxiliary Health')
        self.tabControl.add(self.tab2, text="Automatic SHED control")
        self.tabControl.add(self.tab3, text='Flow Diagram')
        self.tabControl.pack(expand = True, fill = 'both')

        self.frame_tab1 = Tab1(self.tab1, self)
        self.frame_tab1.grid(row = 0, column = 0, sticky = "nsew")

        self.frame_tab2 = Tab2(self.tab2, self)
        self.frame_tab2.grid(row = 0, column = 0, sticky = "nsew")

        self.frame_tab3 = Tab3(self.tab3, self)
        self.frame_tab3.grid(row = 0, column = 0, sticky = "nsew")

        self.geometry("1024x600")
        self.protocol('WM_DELETE_WINDOW', stop_program)
        self.root.mainloop()


class Tab1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        flow_frame = ttk.LabelFrame(self, text = "Flow Monitoring")
        flow_frame.grid(column = 0, row = 0, padx = 10, pady = 10, )
        #mainflow = FlowDisplay(self, self)
        #mainflow.pack()
        lbl1= tk.Label(flow_frame, text="Tab1", font=LARGE_FONT)
        lbl1.grid(column =1, row=0, sticky = 'WE')
        shed_frame = ttk.LabelFrame(self, text = "SHED status")
        shed_frame.grid(column = 0,row = 1)
        SHED1_lbl = tk.Label(shed_frame, text = SHED_req_to_start)
        SHED1_lbl.grid(column = 0, row = 1)
        def update_SHED_lbl(SHED_lbl):
            def update():
                SHED_lbl.configure(text = SHED_req_to_start)
                SHED_lbl.after(10, update)
            update()
        update_SHED_lbl(SHED1_lbl)
        #main_fr
        #label_label1 = tk.Label(self, text = "Where will this label go?!")
        #label_label1.grid(column = 1, row = 0)


class Tab2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #start_frame = ttk.Frame(self)
        #start_frame.grid(column=0,row=0, columnspan=1000, sticky = 'EW')
        #start_btns = SHEDoperation(start_frame,self)
        #start_btns.pack()
        lbl2 = tk.Label(self, text="Tab2")
        lbl2.grid(column = 0, row = 0 )

        #lbl1 = tk.Label(self, text="Tab1", font=LARGE_FONT)
        #lbl1.grid(column=1, row=0, sticky='WE')
        SHED1_lbl = tk.Label(self, text=SHED_req_to_start)
        SHED1_lbl.grid(column=0, row=1)

        def update_SHED_lbl(SHED_lbl):
            def update():
                SHED_lbl.configure(text=SHED_req_to_start)
                SHED_lbl.after(10, update)

            update()

        update_SHED_lbl(SHED1_lbl)


class Tab3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lbl3 = tk.Label(self, text="Tab3")
        lbl3.grid(column = 0, row = 0)
        #lbl1 = tk.Label(self, text="Tab1", font=LARGE_FONT)
        #lbl1.grid(column=1, row=0, sticky='WE')
        SHED1_lbl = tk.Label(self, text=SHED_req_to_start)
        SHED1_lbl.grid(column=0, row=1)

        def update_SHED_lbl(SHED_lbl):
            def update():
                SHED_lbl.configure(text=SHED_req_to_start)
                SHED_lbl.after(10, update)

            update()

        update_SHED_lbl(SHED1_lbl)

def Dataset_save():
    pass


def stop_program():
    global exit_case, SHED1,SHED2,SHED3
    # if okay is selected, the program will terminate itself appropriately
    if messagebox.askokcancel("Quit","Do you want to quit?\nThis will terminate everything including data recording"):
        SHED1 = False
        SHED2 = False
        SHED3 = False
        exit_case = True
        sys.exit()
sched = BackgroundScheduler()
sched.start()
# sched.add_job(background_communication)
app = MainApplication()