from maq20 import MAQ20
import os
#from multiprocessing import Process, current_process
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
import multiprocessing

exit_case = False
refresh = 1


config = ("config/config.xlsx")
wb = xlrd.open_workbook(config)
sheet1 = wb.sheet_by_index(0)




########################################################################################################################
#                                  Initiate values from DATAFORTH MAQ20                                                #
########################################################################################################################
ip = sheet1.cell_value(1,1)
maq20 = MAQ20(ip_address=ip, port=502)     # Set communication with MAQ20
AI_mod = maq20[1]       # Analog input module
TTC_mod = maq20[2]      # Thermocouple input module.
AO_mod = maq20[3]
DIV20_mod = maq20[4]    # 20 digital discrete inputs
DIOL_mod1 = maq20[5]    # 5 Digital discrete inputs, 5 Digital outputs
DIOL_mod2 = maq20[6]    # 5 Digital discrete inputs, 5 Digital outputs
DIOL_mod3 = maq20[7]    # 5 Digital discrete inputs, 5 Digital outputs
DIOL_mod4 = maq20[8]    # 5 Digital discrete inputs, 5 Digital outputs

# Read input/output values from Modules
DIOL_1 = (DIOL_mod1.read_data_counts(0, number_of_channels=DIOL_mod1.get_number_of_channels()))
DIOL_2 = (DIOL_mod2.read_data_counts(0, number_of_channels=DIOL_mod2.get_number_of_channels()))
DIOL_3 = (DIOL_mod3.read_data_counts(0, number_of_channels=DIOL_mod3.get_number_of_channels()))
DIOL_4 = (DIOL_mod4.read_data_counts(0, number_of_channels=DIOL_mod4.get_number_of_channels()))
T = (TTC_mod.read_data(0, number_of_channels=TTC_mod.get_number_of_channels()))
AI = (AI_mod.read_data(0, number_of_channels=AI_mod.get_number_of_channels()))
#analog out
AO = AO_mod[:]


print(maq20)

##########################################################
#              Global Flow Rate Variables                #
##########################################################
current_in = [DIOL_1[5], DIOL_1[6], DIOL_1[7], DIOL_1[8], DIOL_1[9], DIOL_2[5], DIOL_2[6],
              DIOL_2[7]]  # used to compare to new_in for flow rate pulse status
pulse_count = [0] * 8  # Total counts since program start, increments from ZERO
flowrate = [0.0] * 8  # flow rate calculated from pulse count and time
ppg = [151.4, 151.4, 75.7, 75.7, 75.7, 151.4, 151.4, 151.4]  # pulses per gallon as per flow meter specs [corrected]
prev_count = [0] * 8  # Previous pulse count used in calculation of flow rate
prev_time = [time.time()] * 8 # initialize previous time for glow rate calculation
flow_text1 = [0] * 8     # Tab 1


##########################################################
#           Global Output Control Variables              #
##########################################################

pump_io=[0]*8
valve_V = AO
valve_V = [0]*8
##########################################################
#                   GUI Tab 1 Variables                  #
##########################################################
flow_text1 = [0] *8     # Tab 1
flow_temp_text1 = [0] *8
flow_valve_text1 = [0] *8
shed_temp_text1 = [0] *2
pump_text1 = [0] *8


print(ip)
print(valve_V)
print (DIOL_1)
print(AO)

flash_index=0
flash_delay = 0.5
flash_timer = 0
index=0
def flash_(): # used as index for flashing. changes from 0-1 at interval of flash_delay (seconds)
    global flash_index, flash_timer

    if flash_timer < time.time():
        flash_index = 1-flash_index
        flash_timer = time.time()+flash_delay
def pulse_totalizer():

    while True:
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
                 print('error')
        if exit_case == True:
            sys.exit()

        #print(flowrate)
def flow_calculate(flow_text, n):
    def flow_update():
        txt = ''
        # for n in range(0,8):
        flow_text[n].configure(text="Flowrate \n" + str(round(flowrate[n], 2)) + " GPM")
        #print(flowrate[n])
        flow_text[n].after(refresh, flow_update)
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
            if pump_error == 0:
                pump_text[i].configure(text=txt, bg="green", fg="black")  # Pump text 1 for ON 0 for Off

            if pump_error[i] == 1:
                bgflash = ("black", "red")
                pump_text[i].configure(bg=bgflash[flash_index])
        else:
            txt = "error"
        pump_text[i].configure(text=txt)  # Pump text 1 for ON 0 for Off
        pump_text[i].after(refresh, pump_text_update)

    pump_text_update()

def flow_temp_status(temp_text,n):
    def temp_text_update():
        txt = ""
        txt = "Temp." + str(n + 1) + "\n" +str(round(T[n],2)) + u'\N{DEGREE SIGN}'+"C"
        temp_text[n].configure(text=txt, bg="black", fg="white")  # Pump text 1 for ON 0 for Off
        temp_text[n].after(refresh, temp_text_update)
    temp_text_update()

def valve_position(valve_text,n):
    def valve_text_update():
        txt=""
        txt="Valve Pos." + str(n+1) + "\n" + str(round(100*valve_V[n]/10,2)) +"%"
        valve_text[n].configure(text=txt)
        valve_text[n].after(refresh, valve_text_update)
    valve_text_update()
x = 0
y=0
def read_write_MAQ20():
    global DIOL_1, DIOL_2, DIOL_3, DIOL_4, T, AI, AO, AO_mod,x

    while True:

        try:
            #read
            DIOL_1 = (DIOL_mod1.read_data_counts(0, number_of_channels=DIOL_mod1.get_number_of_channels()))
            DIOL_2 = (DIOL_mod2.read_data_counts(0, number_of_channels=DIOL_mod2.get_number_of_channels()))
            DIOL_3 = (DIOL_mod3.read_data_counts(0, number_of_channels=DIOL_mod3.get_number_of_channels()))
            DIOL_4 = (DIOL_mod4.read_data_counts(0, number_of_channels=DIOL_mod4.get_number_of_channels()))
            T = (TTC_mod.read_data(0, number_of_channels=TTC_mod.get_number_of_channels()))
            AI = (AI_mod.read_data(0, number_of_channels=AI_mod.get_number_of_channels()))

            #Write
            AO_mod=valve_V
            print("sample#: "+ str(y))
            y= y+1
        except:
            x = x+1
            print('runtime error PASSED '+str(x))
            pass
        if exit_case == True: # Set all values to OFF
            pump_io = [0] * 8
            DIOL_mod1[0] = 0
            DIOL_mod1[1] = 0
            DIOL_mod1[2] = 0
            DIOL_mod1[3] = 0
            DIOL_mod1[4] = 0
            DIOL_mod2[0] = 0
            DIOL_mod2[1] = 0
            DIOL_mod2[2] = 0
            AO_mod[:] = 0
            sys.exit()



def GUI():
    window = tk.Tk()
    window.title('SHED AUX test')
    window.minsize(600,600)
    tab_control = ttk.Notebook(window) # Tabs on top of page
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab3 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Auxiliary Health')
    tab_control.add(tab2, text="Automatic SHED control")
    tab_control.add(tab3, text='Flow Diagram')
    tab_control.pack(expand=2, fill='both')
    application_window = tab1 #Application set to tab1 for Tab 1 of window

    lf0 = ttk.LabelFrame(application_window, text="Main Loop")  # , width=100,height=100)
    lf0.grid(row=0, column=0, padx=10, pady=10)  # ,rowspan=5, columnspan=4)
    lf1 = ttk.LabelFrame(application_window, text="SHED1 Loop")  # , width=100,height=100)
    lf1.grid(row=1, column=0, padx=10, pady=10)
    lf2 = ttk.LabelFrame(application_window, text="SHED2 Loop")  # , width=100,height=100)
    lf2.grid(row=2, column=0, padx=10, pady=10)
    lf3 = ttk.LabelFrame(application_window, text="SHED3 Loop")  # , width=100,height=100)
    lf3.grid(row=3, column=0, padx=10, pady=10)

    def MAIN_tab1(): # MAIN Loop

        application_window=lf0
        hotLabel0 = Label(application_window, text="Hot", font=("Bold", 10), padx=10)
        coldLabel0 = Label(application_window, text="Cold", font=("Bold", 10), padx=10)
        hotLabel0.grid(row=2, column=0)
        coldLabel0.grid(row=3, column=0)
        flow_text1[4] = Label(application_window, padx=10)
        flow_text1[5] = Label(application_window, padx=10)
        flow_text1[4].grid(row=2, column=2)
        flow_text1[5].grid(row=3, column=2)
        pump_text1[4] = Label(application_window, padx=10)
        pump_text1[5] = Label(application_window, padx=10)
        pump_text1[4].grid(row=2, column=1)
        pump_text1[5].grid(row=3, column=1)
        flow_temp_text1[4] = Label(application_window, padx=10)
        flow_temp_text1[5] = Label(application_window, padx=10)
        flow_temp_text1[4].grid(row=2, column=3)
        flow_temp_text1[5].grid(row=3, column=3)
        flow_valve_text1[4] = Label(application_window, padx=10)
        flow_valve_text1[5] = Label(application_window, padx=10)
        flow_valve_text1[4].grid(row=2,column=4)
        flow_valve_text1[5].grid(row=3, column=4)

        for n in range(4, 6):
            pump_status(pump_text1,n)
            flow_calculate(flow_text1, n)
            flow_temp_status(flow_temp_text1,n)
            valve_position(flow_valve_text1,n)
    def SHED3_tab1():
        application_window = lf3
        hotLabel3 = Label(application_window, text="Hot", font=("Bold", 10), padx=10)
        coldLabel3 = Label(application_window, text="Cold", font=("Bold", 10), padx=10)
        hotLabel3.grid(row=2, column=0)
        coldLabel3.grid(row=3, column=0)
        flow_text1[0] = Label(application_window, padx=10)
        flow_text1[1] = Label(application_window, padx=10)
        flow_text1[0].grid(row=2, column=2)
        flow_text1[1].grid(row=3, column=2)
        pump_text1[0] = Label(application_window, padx=10)
        pump_text1[1] = Label(application_window, padx=10)
        pump_text1[0].grid(row=2, column=1)
        pump_text1[1].grid(row=3, column=1)
        flow_temp_text1[0] = Label(application_window, padx=10)
        flow_temp_text1[1] = Label(application_window, padx=10)
        flow_temp_text1[0].grid(row=2, column=3)
        flow_temp_text1[1].grid(row=3, column=3)
        flow_valve_text1[0] = Label(application_window, padx=10)
        flow_valve_text1[1] = Label(application_window, padx=10)
        flow_valve_text1[0].grid(row=2,column=4)
        flow_valve_text1[1].grid(row=3, column=4)

        for n in range(0, 2):
            pump_status(pump_text1,n)
            flow_calculate(flow_text1, n)
            flow_temp_status(flow_temp_text1,n)
            valve_position(flow_valve_text1,n)
    def SHED2_tab1():
        application_window = lf2
        hotLabel2 = Label(application_window, text="Hot", font=("Bold", 10), padx=10)
        coldLabel2 = Label(application_window, text="Cold", font=("Bold", 10), padx=10)
        hotLabel2.grid(row=2, column=0)
        coldLabel2.grid(row=3, column=0)
        flow_text1[2] = Label(application_window, padx=10)
        flow_text1[3] = Label(application_window, padx=10)
        flow_text1[2].grid(row=2, column=2)
        flow_text1[3].grid(row=3, column=2)
        pump_text1[2] = Label(application_window, padx=10)
        pump_text1[3] = Label(application_window, padx=10)
        pump_text1[2].grid(row=2, column=1)
        pump_text1[3].grid(row=3, column=1)
        flow_temp_text1[2] = Label(application_window, padx=10)
        flow_temp_text1[3] = Label(application_window, padx=10)
        flow_temp_text1[2].grid(row=2, column=3)
        flow_temp_text1[3].grid(row=3, column=3)
        flow_valve_text1[2] = Label(application_window, padx=10)
        flow_valve_text1[3] = Label(application_window, padx=10)
        flow_valve_text1[2].grid(row=2,column=4)
        flow_valve_text1[3].grid(row=3, column=4)

        for n in range(2, 4):
            pump_status(pump_text1,n)
            flow_calculate(flow_text1, n)
            flow_temp_status(flow_temp_text1,n)
            valve_position(flow_valve_text1,n)
    def SHED1_tab1():
        application_window= lf1
        hotLabel1 = Label(application_window, text="Hot", font=("Bold", 10), padx=10)
        coldLabel1 = Label(application_window, text="Cold", font=("Bold", 10), padx=10)
        hotLabel1.grid(row=2, column=0)
        coldLabel1.grid(row=3, column=0)

        flow_text1[7] = Label(application_window, padx=10)
        flow_text1[6] = Label(application_window, padx=10)
        flow_text1[7].grid(row=2, column=2)
        flow_text1[6].grid(row=3, column=2)
        pump_text1[7] = Label(application_window, padx=10)
        pump_text1[6] = Label(application_window, padx=10)
        pump_text1[7].grid(row=2, column=1)
        pump_text1[6].grid(row=3, column=1)
        flow_temp_text1[7] = Label(application_window, padx=10)
        flow_temp_text1[6] = Label(application_window, padx=10)
        flow_temp_text1[7].grid(row=2, column=3)
        flow_temp_text1[6].grid(row=3, column=3)
        flow_valve_text1[7] = Label(application_window, padx=10)
        flow_valve_text1[6] = Label(application_window, padx=10)
        flow_valve_text1[7].grid(row=2, column=4)
        flow_valve_text1[6].grid(row=3, column=4)

        for n in range(6, 8):
            pump_status(pump_text1, n)
            flow_calculate(flow_text1, n)
            flow_temp_status(flow_temp_text1, n)
            valve_position(flow_valve_text1, n)



    MAIN_tab1()
    SHED1_tab1()
    SHED2_tab1()
    SHED3_tab1()
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

p1 = multiprocessing.Process(target=pulse_totalizer)
p2 = multiprocessing.Process(target=read_write_MAQ20)
p3 = multiprocessing.Process(target=GUI)
p0 = multiprocessing.Process(target=flash_)

print("initiating values. . . ")
sleep(.5)
print("updating fields. . .")
sleep(.5)
print('start')

p3.start()
p0.start()
p1.start()
p2.start()
