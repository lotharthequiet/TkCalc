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

from ast import Global
import tkinter as tk
import tksheet
import logging

from functools import partial

class GlobalVars():
    shortname = "TkCalc"
    ver = "0.1a1" 
    appname = (shortname + " " + ver)
    btnsz = 2
    pad = 2
    calcmem = None
    opmem = None

class TkCalc():
    def mrc(mem=None):
        print("MRC")

    def memmin(mem=None):
        print("M-")
    
    def memplus(mem=None):
        print("M+")
    
    def memce(mem=None):
        print("CE")
        try:
            GlobalVars.calcmem = None
            print("Working memory cleared.")
            GlobalVars.opmem = None
            print("Operator memory cleared.")
        except Exception as e:
            print("Error clearing memory.")
    
    def percent(operator="%"):
        print(operator)
        GlobalVars.opmem = "%"
    
    def sqrt(operator="sqrt"):
        print(operator)
        GlobalVars.opmem = "sqrt"

    def mult(operator="x"):
        print(operator)
        GlobalVars.opmem = "x"

    def div(operator="/"):
        print(operator)
        GlobalVars.opmem = "/"

    def minus(operator="-"):
        print(operator)
        GlobalVars.opmem = "-"

    def equal(operator="="):
        print(operator)
        GlobalVars.opmem = "="
        print(GlobalVars.calcmem)

    def period(operator="."):
        print(operator)
        GlobalVars.opmem = "."

    def plusminus(operator="+/-"):
        print(operator)
        GlobalVars.opmem = "+/-"

    def plus(operator="+"):
        print(operator)
        GlobalVars.opmem = "+"

    def docalc(value):
        print("DoCalc function.")
        try:
            match value:
                case 0:
                    operation = 0
                case 1:
                    operation = 0
                case 2:
                    operation = 0
                case 3:
                    operation = 0
                case 4:
                    operation = 0
                case 5:
                    operation = 0
                case 6:
                    operation = 0
                case 7:
                    operation = 0
                case 8:
                    operation = 0
                case 9:
                    operation = 0
                case "+":
                    operation = 1
                case "-":
                    operation = 1
                case "x":
                    operation = 1
                case "/":
                    operation = 1
                case ".":
                    operation = 5

            if operation == 0:
                if not GlobalVars.calcmem:
                    GlobalVars.calcmem = value
                else:
                    GlobalVars.calcmem = int(str(GlobalVars.calcmem) + str(value))
                    
            if operation == 5:
                if not GlobalVars.calcmem:
                    GlobalVars.calcmem = 0
                    GlobalVars.calcmem = int(str(GlobalVars.calcmem) + str(value))
                else:
                    GlobalVars.calcmem = float(str(GlobalVars.calcmem) + str(value))
        except Exception as e:
            print("DoCalc failed.", e)
        print(GlobalVars.calcmem)

    button0 = partial(docalc, 0)
    button1 = partial(docalc, 1)
    button2 = partial(docalc, 2)
    button3 = partial(docalc, 3)
    button4 = partial(docalc, 4)
    button5 = partial(docalc, 5)
    button6 = partial(docalc, 6)
    button7 = partial(docalc, 7)
    button8 = partial(docalc, 8)
    button9 = partial(docalc, 9)
    

    root = tk.Tk()
    root.title(GlobalVars.appname)
    root.geometry("260x210")
    usrentrylbl = tk.Entry(root, state="readonly", width=27, textvariable=GlobalVars.calcmem, readonlybackground='white')
    usrentrylbl.grid(column=0, row=0, columnspan=5, padx=GlobalVars.pad, pady=GlobalVars.pad)
    mrcbtn = tk.Button(root, text="MRC", width=GlobalVars.btnsz, command=mrc)
    mrcbtn.grid(column=0, row=1, padx=GlobalVars.pad, pady=GlobalVars.pad)
    mminusbtn = tk.Button(root, text="M-", width=GlobalVars.btnsz, command=memmin)
    mminusbtn.grid(column=1, row=1, padx=GlobalVars.pad, pady=GlobalVars.pad)
    mplusbtn = tk.Button(root, text="M+", width=GlobalVars.btnsz, command=memplus)
    mplusbtn.grid(column=2, row=1, padx=GlobalVars.pad, pady=GlobalVars.pad)
    mrcbtn = tk.Button(root, text="CE", width=GlobalVars.btnsz, command=memce)
    mrcbtn.grid(column=3, row=1, padx=GlobalVars.pad, pady=GlobalVars.pad)

    btn7 = tk.Button(root, text="7", width=GlobalVars.btnsz, command=button7)
    btn7.grid(column=0, row=2, padx=GlobalVars.pad, pady=GlobalVars.pad)
    btn8 = tk.Button(root, text="8", width=GlobalVars.btnsz, command=button8)
    btn8.grid(column=1, row=2, padx=GlobalVars.pad, pady=GlobalVars.pad)
    btn9 = tk.Button(root, text="9", width=GlobalVars.btnsz, command=button9)
    btn9.grid(column=2, row=2, padx=GlobalVars.pad, pady=GlobalVars.pad)
    percbtn = tk.Button(root, text="%", width=GlobalVars.btnsz, command=percent)
    percbtn.grid(column=3, row=2, padx=GlobalVars.pad, pady=GlobalVars.pad)
    sqrtbtn = tk.Button(root, text="SqRt", width=GlobalVars.btnsz, command=sqrt)
    sqrtbtn.grid(column=4, row=2, padx=GlobalVars.pad, pady=GlobalVars.pad)

    btn4 = tk.Button(root, text="4", width=GlobalVars.btnsz, command=button4)
    btn4.grid(column=0, row=3, padx=GlobalVars.pad, pady=GlobalVars.pad)
    btn5 = tk.Button(root, text="5", width=GlobalVars.btnsz, command=button5)
    btn5.grid(column=1, row=3, padx=GlobalVars.pad, pady=GlobalVars.pad)
    btn6 = tk.Button(root, text="6", width=GlobalVars.btnsz, command=button6)
    btn6.grid(column=2, row=3, padx=GlobalVars.pad, pady=GlobalVars.pad)
    multbtn = tk.Button(root, text="X", width=GlobalVars.btnsz, command=mult)
    multbtn.grid(column=3, row=3, padx=GlobalVars.pad, pady=GlobalVars.pad)
    divbtn = tk.Button(root, text="/", width=GlobalVars.btnsz, command=div)
    divbtn.grid(column=4, row=3, padx=GlobalVars.pad, pady=GlobalVars.pad)

    btn1 = tk.Button(root, text="1", width=GlobalVars.btnsz, command=button1)
    btn1.grid(column=0, row=4, padx=GlobalVars.pad, pady=GlobalVars.pad)
    btn2 = tk.Button(root, text="2", width=GlobalVars.btnsz, command=button2)
    btn2.grid(column=1, row=4, padx=GlobalVars.pad, pady=GlobalVars.pad)
    btn3 = tk.Button(root, text="3", width=GlobalVars.btnsz, command=button3)
    btn3.grid(column=2, row=4, padx=GlobalVars.pad, pady=GlobalVars.pad)
    minbtn = tk.Button(root, text="-", width=GlobalVars.btnsz, command=minus)
    minbtn.grid(column=3, row=4, padx=GlobalVars.pad, pady=GlobalVars.pad)
    eqbtn = tk.Button(root, text="=", width=GlobalVars.btnsz, command=equal, height=3)
    eqbtn.grid(column=4, row=4, padx=GlobalVars.pad, pady=GlobalVars.pad, rowspan=2)

    btn0 = tk.Button(root, text="0", width=GlobalVars.btnsz, command=button0)
    btn0.grid(column=0, row=5, padx=GlobalVars.pad, pady=GlobalVars.pad)
    perbtn = tk.Button(root, text=".", width=GlobalVars.btnsz, command=period)
    perbtn.grid(column=1, row=5, padx=GlobalVars.pad, pady=GlobalVars.pad)
    plusminbtn = tk.Button(root, text="+/-", width=GlobalVars.btnsz, command=plusminus)
    plusminbtn.grid(column=2, row=5, padx=GlobalVars.pad, pady=GlobalVars.pad)
    plusbtn = tk.Button(root, text="+", width=GlobalVars.btnsz, command=plus)
    plusbtn.grid(column=3, row=5, padx=GlobalVars.pad, pady=GlobalVars.pad)
    root.mainloop()


app=TkCalc()


