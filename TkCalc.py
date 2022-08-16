"""
*********************************************************************************
|                                                                               |
|                             Linux System Toolbox                              |
|                 --------------------------------------------                  |   
|                         Written by: Lothar TheQuiet                           |
|                          lotharthequiet@gmail.com                             |
|                      Hounding about caMELCase: Rilvyk                         |
|                                                                               |
*********************************************************************************

Logging Levels:
------------------------------------------------------------
DEBUG: Detailed info
INFO: Confirmation of things working correctly
WARNING: (Default level) Indication things are not so good
ERROR: More serious prob preventing app from running
CRITICAL: Serious error
"""

import tkinter as tk
import tksheet
import logging

class GlobalVars():
    shortname = "TkCalc"
    ver = "0.1a1" 
    appname = (shortname + " " + ver)
    btnsz = 2
    pad = 2
    calcmem = 0

class TkCalc():
    def mrc(mem=None):
        print("MRC")

    def memmin(mem=None):
        print("M-")
    
    def memplus(mem=None):
        print("M+")
    
    def memce(mem=None):
        print("CE")

    def seven(number=7):
        print(number)
        GlobalVars.calcmem = number
        #usrentrylbl.insert(0, number)
    
    def eight(number=8):
        print(number)
    
    def nine(number=9):
        print(number)
    
    def percent(operator="%"):
        print(operator)
    
    def sqrt(operator="sqrt"):
        print(operator)

    def four(number=4):
        print(number)

    def five(number=5):
        print(number)
    
    def six(number=6):
        print(number)

    def mult(operator="x"):
        print(operator)

    def div(operator="/"):
        print(operator)

    def one(number=1):
        print(number)

    def two(number=2):
        print(number)

    def three(number=3):
        print(number)

    def minus(operator="-"):
        print(operator)

    def equal(operator="="):
        print(operator)
        print(GlobalVars.calcmem)

    def zero(number=0):
        print(number)

    def period(operator="."):
        print(operator)

    def plusminus(operator="+/-"):
        print(operator)

    def plus(operator="+"):
        print(operator)

    root = tk.Tk()
    root.title(GlobalVars.appname)
    root.geometry("260x210")
    usrentrylbl = tk.Entry(root, state="disabled", width=27, textvariable=GlobalVars.calcmem)
    usrentrylbl.grid(column=0, row=0, columnspan=5, padx=GlobalVars.pad, pady=GlobalVars.pad)
    mrcbtn = tk.Button(root, text="MRC", width=GlobalVars.btnsz, command=mrc)
    mrcbtn.grid(column=0, row=1, padx=GlobalVars.pad, pady=GlobalVars.pad)
    mminusbtn = tk.Button(root, text="M-", width=GlobalVars.btnsz, command=memmin)
    mminusbtn.grid(column=1, row=1, padx=GlobalVars.pad, pady=GlobalVars.pad)
    mplusbtn = tk.Button(root, text="M+", width=GlobalVars.btnsz, command=memplus)
    mplusbtn.grid(column=2, row=1, padx=GlobalVars.pad, pady=GlobalVars.pad)
    mrcbtn = tk.Button(root, text="CE", width=GlobalVars.btnsz, command=memce)
    mrcbtn.grid(column=3, row=1, padx=GlobalVars.pad, pady=GlobalVars.pad)

    btn7 = tk.Button(root, text="7", width=GlobalVars.btnsz, command=seven)
    btn7.grid(column=0, row=2, padx=GlobalVars.pad, pady=GlobalVars.pad)
    btn8 = tk.Button(root, text="8", width=GlobalVars.btnsz, command=eight)
    btn8.grid(column=1, row=2, padx=GlobalVars.pad, pady=GlobalVars.pad)
    btn9 = tk.Button(root, text="9", width=GlobalVars.btnsz, command=nine)
    btn9.grid(column=2, row=2, padx=GlobalVars.pad, pady=GlobalVars.pad)
    percbtn = tk.Button(root, text="%", width=GlobalVars.btnsz, command=percent)
    percbtn.grid(column=3, row=2, padx=GlobalVars.pad, pady=GlobalVars.pad)
    sqrtbtn = tk.Button(root, text="SqRt", width=GlobalVars.btnsz, command=sqrt)
    sqrtbtn.grid(column=4, row=2, padx=GlobalVars.pad, pady=GlobalVars.pad)

    btn4 = tk.Button(root, text="4", width=GlobalVars.btnsz, command=four)
    btn4.grid(column=0, row=3, padx=GlobalVars.pad, pady=GlobalVars.pad)
    btn5 = tk.Button(root, text="5", width=GlobalVars.btnsz, command=five)
    btn5.grid(column=1, row=3, padx=GlobalVars.pad, pady=GlobalVars.pad)
    btn6 = tk.Button(root, text="6", width=GlobalVars.btnsz, command=six)
    btn6.grid(column=2, row=3, padx=GlobalVars.pad, pady=GlobalVars.pad)
    multbtn = tk.Button(root, text="X", width=GlobalVars.btnsz, command=mult)
    multbtn.grid(column=3, row=3, padx=GlobalVars.pad, pady=GlobalVars.pad)
    divbtn = tk.Button(root, text="/", width=GlobalVars.btnsz, command=div)
    divbtn.grid(column=4, row=3, padx=GlobalVars.pad, pady=GlobalVars.pad)

    btn1 = tk.Button(root, text="1", width=GlobalVars.btnsz, command=one)
    btn1.grid(column=0, row=4, padx=GlobalVars.pad, pady=GlobalVars.pad)
    btn2 = tk.Button(root, text="2", width=GlobalVars.btnsz, command=two)
    btn2.grid(column=1, row=4, padx=GlobalVars.pad, pady=GlobalVars.pad)
    btn3 = tk.Button(root, text="3", width=GlobalVars.btnsz, command=three)
    btn3.grid(column=2, row=4, padx=GlobalVars.pad, pady=GlobalVars.pad)
    minbtn = tk.Button(root, text="-", width=GlobalVars.btnsz, command=minus)
    minbtn.grid(column=3, row=4, padx=GlobalVars.pad, pady=GlobalVars.pad)
    eqbtn = tk.Button(root, text="=", width=GlobalVars.btnsz, command=equal, height=3)
    eqbtn.grid(column=4, row=4, padx=GlobalVars.pad, pady=GlobalVars.pad, rowspan=2)

    btn0 = tk.Button(root, text="0", width=GlobalVars.btnsz, command=zero)
    btn0.grid(column=0, row=5, padx=GlobalVars.pad, pady=GlobalVars.pad)
    perbtn = tk.Button(root, text=".", width=GlobalVars.btnsz, command=period)
    perbtn.grid(column=1, row=5, padx=GlobalVars.pad, pady=GlobalVars.pad)
    plusminbtn = tk.Button(root, text="+/-", width=GlobalVars.btnsz, command=plusminus)
    plusminbtn.grid(column=2, row=5, padx=GlobalVars.pad, pady=GlobalVars.pad)
    plusbtn = tk.Button(root, text="+", width=GlobalVars.btnsz, command=plus)
    plusbtn.grid(column=3, row=5, padx=GlobalVars.pad, pady=GlobalVars.pad)
    root.mainloop()


app=TkCalc()


