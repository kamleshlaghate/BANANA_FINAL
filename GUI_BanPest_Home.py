from tkinter import *
from tkinter import ttk
import time
import xlsxwriter
from datetime import date
import sys
import os
from os import listdir
from os.path import isfile, join

import xlrd
from tkinter import filedialog
from tkinter import messagebox
import tkinter.messagebox

import math
from collections import Counter
import pandas as pd
import numpy as np
import numpy
import random


seed = 7
numpy.random.seed(seed)


import argparse

window = Tk()
window.title("PESTICIDE DETECTION ON BANANA")
window.geometry('1000x500')

tab_control = ttk.Notebook(window)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='LOGIN')

#############################################################################################################################################################


def RST():
      messagebox.showerror('CLOSE', 'CLOSE')
      window.quit()
      window.destroy()



# INPUT FORM:diaryofagameaddict.com
   
def ARUNMODEL1():
    KK=np.loadtxt('aa.txt')
    if KK[0]==1:
       lbl2.configure(text='TESTING--')
       window.quit()
       window.destroy()
       import MAIN_CODE_TST
    else:
       lbl1.configure(text='ACCESS DENIED')
          
   


 	 
#############################################################################################################################################################
lbl = Label(tab2, text="TEST",font=("Arial Bold", 30),foreground =("red"),background  =("white"))
lbl.grid(column=0, row=0)
lbl = Label(tab2, text="PANEL",font=("Arial Bold", 30),foreground =("red"),background  =("white"))
lbl.grid(column=1, row=0)



lbl2= Label(tab2, text="  STATUS   ",font=("Arial Bold", 10),foreground =("black"),background  =("white"))
lbl2.grid(column=1, row=5)

Button(tab2, text='TEST FRUIT', command=ARUNMODEL1,font=("Arial Bold", 15),foreground =("yellow"),background  =("brown")).grid(row=1, column=1, sticky=W, pady=4)

Button(tab2, text='CANCEL', command=RST,font=("Arial Bold", 15),foreground =("yellow"),background  =("brown")).grid(row=3, column=1, sticky=W, pady=4)

#############################################################################################################################################################
tab_control.pack(expand=1, fill='both')
window.mainloop()
