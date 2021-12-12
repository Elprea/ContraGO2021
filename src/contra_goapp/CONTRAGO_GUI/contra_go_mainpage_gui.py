""" ContraGO Main Page GUI Program

This program will run tkinter GUI program that will allow the user to navigate
throught the application to either create a new contract or view previous contracts 
tied to the users account

  Typical usage example:


"""
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

import sqlite3

from contra_goapp.CONTRAGO_GUI.contra_go_fill_form_gui import ContraGO_Estimate_Module

from contra_goapp.CONTRAGO_DB.contra_go_fill_form_gui_db import getContractHistory


def openFillForm(): 
    
    """openFillForm()

    Opens new fill form gui and destroy 
    previous process 

    Args:
      N/A


    """
    window.destroy()
    ContraGO_Estimate_Module()
    


def contrago_mainpage(): 
    
    """contrago_mainpage()

    Executes the mainpage gui module for 
    user view contract history and contract making module 

    Args:
      N/A


    """
    global window 
    
    
    window = Tk()
    
    
    """ 
    Tkinter Window Dimensions 
    """ 
    window.title("ContraGO Mainpage")
    window.geometry("1200x780")
    window.configure(bg = "#FFFFFF")
    
    
    """ 
    Tkinter Canvas Create
    """ 
    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 780,
        width = 1200,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    
    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        450.0,
        0.0,
        1200.0,
        780.0,
        fill="#F9ECD3",
        outline="")
    
    
    
    
    """ 
    Tkinter GUI Buttons
    Buttons: 
        About
        View History 
        Log Out 
        Create Contract
    """ 
    
    
    viewHistoryBttn = Button(
        text="View History",
        font=('ArialNarrow 30 bold'),
        bg="#BD8000",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: getContractHistory(),
        relief="flat"
    )
    
    viewHistoryBttn.place(
        x=546.0,
        y=401.0,
        width=557.0,
        height=156.1621551513672
    )
    
    
    createContractBttn = Button(
        text="Create Contract",
        font=('ArialNarrow 30 bold'),
        bg="#BD8000",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: openFillForm(),
        relief="flat"
    )
    createContractBttn.place(
        x=546.0,
        y=221.0,
        width=557.0,
        height=156.1621551513672
    )
    
    
    logOutBttn = Button(
        text="Log Out",
        font=('ArialNarrow 10 bold'),
        bg="#BD8000",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    logOutBttn.place(
        x=10.0,
        y=732.0,
        width=118.0,
        height=38.0
    )
    
    
    aboutBttn = Button(
        text="About",
        font=('ArialNarrow 20 bold'),
        bg="#BD8000",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    aboutBttn.place(
        x=85.0,
        y=496.0,
        width=200.0,
        height=53.0
    )
    
    
    """ 
    Tkinter GUI Title 
    """ 
    canvas.create_text(
        3.0,
        315.0,
        anchor="nw",
        text="\n ContraGO",
        fill="#000000",
        font=("DancingScript Bold", 72 * -1)
    )
    
    canvas.create_text(
        0.0,
        250.0,
        anchor="nw",
        text="  Welcome\n       to",
        fill="#000000",
        font=("DancingScript Bold", 72 * -1)
    )
    window.resizable(False, False)
    window.mainloop()
    
    
if __name__ == "__main__":
    contrago_mainpage()