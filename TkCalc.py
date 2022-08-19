"""
*********************************************************************************
|                                                                               |
|                                    TkCalc                                     |
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
from typing_extensions import Self
import tksheet
import logging

from functools import partial
from tkinter import Tk, ttk, Canvas
from PIL import Image, ImageTk

tkclogger = logging.getLogger(__name__) 
tkclogger.setLevel(logging.DEBUG)
tkcloggerfmt = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
tkcloggerstrm = logging.StreamHandler()
tkcloggerstrm.setFormatter(tkcloggerfmt)
tkclogger.addHandler(tkcloggerstrm)
tkclogger.debug("Starting LST...")
root = tk.Tk()

class GlobalVars():
    shortname = "TkCalc"
    ver = "0.1a1" 
    appname = (shortname + " " + ver)
    btnsz = 2
    pad = 2
    calcmem = 0
    opmem = None
    icon = "calculator.png"
    author = "Lothar TheQuiet"
    contact = "lotharthequiet@gmail.com"
    codeassist = "Rilvyk"
    git = "https://github.com/lotharthequiet/TkCalc.git"
    display = tk.StringVar()
    display.set = 0

class TkCalc():
    GlobalVars.display.set = 0
    def mrc(mem=None):
        tkclogger.debug("MRC function.")

    def memmin(mem=None):
        tkclogger.debug("M- function.")
    
    def memplus(mem=None):
        tkclogger.debug("M+ function.")
    
    def memce(mem=None):
        tkclogger.debug("CE function.")
        try:
            GlobalVars.calcmem = 0
            tkclogger.info("Working memory cleared.")
            GlobalVars.opmem = None
            tkclogger.info("Operator memory cleared.")
            GlobalVars.display.set = GlobalVars.calcmem
        except Exception as e:
            tkclogger.error("Error clearing memory.")
    
    def exitapp():
        TkCalc.root.quit()

    def openabout():
            aboutwindow = tk.Toplevel(root)
            aboutwindow.title(GlobalVars.appname)
            ico = Image.open(GlobalVars.icon)
            photo = ImageTk.PhotoImage(ico)
            aboutwindow.wm_iconphoto(False, photo)
            aboutwinttlfrm = tk.LabelFrame(aboutwindow, text = "About")
            aboutwinttlfrm.grid(column = 0, row = 0, padx = 5, pady = 5, sticky="NSEW")
            img = Image.open(GlobalVars.icon)
            img.resize((128, 128))
            image = ImageTk.PhotoImage(img)
            aboutcanvas = Canvas(aboutwinttlfrm, width=128, height=128)
            aboutcanvas.create_image(128, 128, image = image)
            aboutcanvas.grid(column=0, row=0, padx = 5, pady = 5, sticky="W")
            aboutttllbl = tk.Label(aboutwinttlfrm, text=GlobalVars.appname)
            aboutttllbl.grid(column=1, row=0, padx = 5, pady = 5, sticky="SW")
            aboutauthorlbl = tk.Label(aboutwinttlfrm, text ="Written By:")
            aboutauthorlbl.grid(column = 0, row = 1, padx = 5, pady = 5, sticky="W")
            aboutauthor = tk.Label(aboutwinttlfrm, text = GlobalVars.author)
            aboutauthor.grid(column = 1, row = 1, padx = 5, pady = 5, sticky="W")
            aboutcontactlbl = tk.Label(aboutwinttlfrm, text ="Contact:")
            aboutcontactlbl.grid(column = 0, row = 2, padx = 5, pady = 5, sticky="W")
            aboutcontact = tk.Label(aboutwinttlfrm, text = GlobalVars.contact)
            aboutcontact.grid(column = 1, row = 2, padx = 5, pady = 5, sticky="W")
            aboutcodeasstlbl = tk.Label(aboutwinttlfrm, text ="Coding Assistance:")
            aboutcodeasstlbl.grid(column = 0, row = 3, padx = 5, pady = 5, sticky="W")
            aboutcodeasst = tk.Label(aboutwinttlfrm, text = GlobalVars.codeassist)
            aboutcodeasst.grid(column = 1, row = 3, padx = 5, pady = 5, sticky="W")
            aboutgitlbl = tk.Label(aboutwinttlfrm, text ="Git Link:")
            aboutgitlbl.grid(column = 0, row = 4, padx = 5, pady = 5, sticky="W")
            aboutgithubgit = tk.Label(aboutwinttlfrm, text = GlobalVars.git)
            aboutgithubgit.grid(column = 1, row = 4, padx = 5, pady = 5, sticky="W")
            aboutverlbl = tk.Label(aboutwinttlfrm, text = "Version:")
            aboutverlbl.grid(column = 0, row = 5, padx = 5, pady = 5, sticky="W")
            aboutver = tk.Label(aboutwinttlfrm, text = GlobalVars.ver)
            aboutver.grid(column = 1, row = 5, padx = 5, pady = 5, sticky="W")

    def openhelp():
        helpwindow = tk.Toplevel(root)
        helpwindow.title(GlobalVars.appname)
        ico = Image.open(GlobalVars.icon)
        photo = ImageTk.PhotoImage(ico)
        helpwindow.wm_iconphoto(False, photo)
        helpwinttlfrm = tk.LabelFrame(helpwindow, text = "Help")
        helpwinttlfrm.grid(column = 0, row = 0, padx = 5, pady = 5, sticky="NSEW")
        helpauthorlbl = tk.Label(helpwinttlfrm, text ="Written By:")
        helpauthorlbl.grid(column= 0, row = 0, padx = 5, pady = 5, sticky="W")

    def docalc(value):
        tkclogger.debug("DoCalc function.")
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
                    operation = 2
                case "x":
                    operation = 3
                case "/":
                    operation = 4
                case ".":
                    operation = 5
                case "=":
                    operation = 6

            if operation == 0:
                if not GlobalVars.calcmem:
                    GlobalVars.calcmem = value
                    #Self.usrentrylbl['text'] = GlobalVars.calcmem
                    GlobalVars.display.set = GlobalVars.calcmem
                else:
                    GlobalVars.calcmem = int(str(GlobalVars.calcmem) + str(value))
                    #Self.usrentrylbl['text'] = GlobalVars.calcmem
                    GlobalVars.display.set = GlobalVars.calcmem
                    
            if operation == 5:
                tkclogger.debug(GlobalVars.calcmem)
                if GlobalVars.calcmem == None:
                    GlobalVars.calcmem = 0
                    GlobalVars.calcmem = float(str(GlobalVars.calcmem) + str(value))
                else:
                    GlobalVars.calcmem = float(str(GlobalVars.calcmem) + str(value))
        except Exception as e:
            tkclogger.error("DoCalc failed.", e)
        tkclogger.debug(GlobalVars.calcmem)

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
    buttonplus = partial(docalc, "+")
    buttonminus = partial(docalc, "-")
    buttonmult = partial(docalc, "*")
    buttondiv = partial(docalc, "/")
    buttonper = partial(docalc, "%")
    buttonsqrt = partial(docalc, "sqrt")
    buttonplusmin = partial(docalc, "+/-")
    buttoneq = partial(docalc, "=")
    buttonperiod = partial(docalc, ".")

    
    root.title(GlobalVars.appname)
    root.geometry("260x210")
    ico = Image.open(GlobalVars.icon)
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)
    nb = ttk.Notebook(root)
    menubar = tk.Menu(nb)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=exitapp)
    menubar.add_cascade(label="File", menu=filemenu)
    helpmenu = tk.Menu(menubar, tearoff=0)                                     
    helpmenu.add_command(label="Help", command=openhelp)
    helpmenu.add_separator()
    helpmenu.add_command(label="About", command=openabout)
    menubar.add_cascade(label="Help", menu=helpmenu)
    root.config(menu=menubar)
    usrentrylbl = tk.Entry(root, state="readonly", width=27, textvariable=GlobalVars.display, readonlybackground='white')
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
    percbtn = tk.Button(root, text="%", width=GlobalVars.btnsz, command=buttonper)
    percbtn.grid(column=3, row=2, padx=GlobalVars.pad, pady=GlobalVars.pad)
    sqrtbtn = tk.Button(root, text="SqRt", width=GlobalVars.btnsz, command=buttonsqrt)
    sqrtbtn.grid(column=4, row=2, padx=GlobalVars.pad, pady=GlobalVars.pad)

    btn4 = tk.Button(root, text="4", width=GlobalVars.btnsz, command=button4)
    btn4.grid(column=0, row=3, padx=GlobalVars.pad, pady=GlobalVars.pad)
    btn5 = tk.Button(root, text="5", width=GlobalVars.btnsz, command=button5)
    btn5.grid(column=1, row=3, padx=GlobalVars.pad, pady=GlobalVars.pad)
    btn6 = tk.Button(root, text="6", width=GlobalVars.btnsz, command=button6)
    btn6.grid(column=2, row=3, padx=GlobalVars.pad, pady=GlobalVars.pad)
    multbtn = tk.Button(root, text="X", width=GlobalVars.btnsz, command=buttonmult)
    multbtn.grid(column=3, row=3, padx=GlobalVars.pad, pady=GlobalVars.pad)
    divbtn = tk.Button(root, text="/", width=GlobalVars.btnsz, command=buttondiv)
    divbtn.grid(column=4, row=3, padx=GlobalVars.pad, pady=GlobalVars.pad)

    btn1 = tk.Button(root, text="1", width=GlobalVars.btnsz, command=button1)
    btn1.grid(column=0, row=4, padx=GlobalVars.pad, pady=GlobalVars.pad)
    btn2 = tk.Button(root, text="2", width=GlobalVars.btnsz, command=button2)
    btn2.grid(column=1, row=4, padx=GlobalVars.pad, pady=GlobalVars.pad)
    btn3 = tk.Button(root, text="3", width=GlobalVars.btnsz, command=button3)
    btn3.grid(column=2, row=4, padx=GlobalVars.pad, pady=GlobalVars.pad)
    minbtn = tk.Button(root, text="-", width=GlobalVars.btnsz, command=buttonminus)
    minbtn.grid(column=3, row=4, padx=GlobalVars.pad, pady=GlobalVars.pad)
    eqbtn = tk.Button(root, text="=", width=GlobalVars.btnsz, command=buttoneq, height=3)
    eqbtn.grid(column=4, row=4, padx=GlobalVars.pad, pady=GlobalVars.pad, rowspan=2)

    btn0 = tk.Button(root, text="0", width=GlobalVars.btnsz, command=button0)
    btn0.grid(column=0, row=5, padx=GlobalVars.pad, pady=GlobalVars.pad)
    perbtn = tk.Button(root, text=".", width=GlobalVars.btnsz, command=buttonperiod)
    perbtn.grid(column=1, row=5, padx=GlobalVars.pad, pady=GlobalVars.pad)
    plusminbtn = tk.Button(root, text="+/-", width=GlobalVars.btnsz, command=buttonplusmin)
    plusminbtn.grid(column=2, row=5, padx=GlobalVars.pad, pady=GlobalVars.pad)
    plusbtn = tk.Button(root, text="+", width=GlobalVars.btnsz, command=buttonplus)
    plusbtn.grid(column=3, row=5, padx=GlobalVars.pad, pady=GlobalVars.pad)
    root.mainloop()


app=TkCalc()


