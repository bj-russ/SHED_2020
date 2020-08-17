import tkinter as tk
from tkinter import ttk
from matplotlib import pyplot as plt

LARGE_FONT = ("Verdana",12)
class MainApplication(tk.Tk):

    def __init__(self):
        #tk.Tk.__init__(self)  # Was causing extra frame to pop up

        self.root = tk.Tk() # create instance of Tk
        self.root.title("SHED Auxiliary Control V2")
        self.tabControl = ttk.Notebook(self.root)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text='Auxiliary Health')
        self.tabControl.add(self.tab2, text="Automatic SHED control")
        self.tabControl.add(self.tab3, text='Flow Diagram')
        self.tabControl.pack(expand=1, fill='both')

        self.frame_tab1 = Tab1(self.tab1,self)
        self.frame_tab1.pack()

        self.frame_tab2 = Tab2(self.tab2,self)
        self.frame_tab2.pack()

        self.frame_tab3 = Tab3(self.tab3,self)
        self.frame_tab3.pack()


        self.root.geometry("1024x600")
        self.root.mainloop()





class Tab1(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        lbl1 = tk.Label(self,text = "Tab1")
        lbl1.pack()


class Tab2(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        lbl2 = tk.Label(self,text = "Tab2")
        lbl2.pack()


class Tab3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lbl3 = tk.Label(self,text="Tab3")
        lbl3.pack()



app = MainApplication()
