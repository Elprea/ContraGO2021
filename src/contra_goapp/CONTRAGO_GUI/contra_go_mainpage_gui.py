""" ContraGO Main Page GUI Program

This program will run tkinter GUI program that will allow the user to navigate
through the application to either create a new contract or view previous contracts 
tied to the users account



"""
from tkinter import Tk, Canvas, Button, Entry
from PIL import ImageTk, Image
from contra_goapp.CONTRAGO_GUI.contra_go_fill_form_gui import ContraGO_Estimate_Module

from contra_goapp.CONTRAGO_DB.contra_go_fill_form_gui_db import getContractHistory

import contra_goapp.CONTRAGO_DB.contra_go_log_in_db

import os
# Favicon On Tkinter Window 
contrago_favicon = os.path.join(
    os.path.dirname(__file__), "assets", "contrago.ico"
)
helmetImage = os.path.join(
    os.path.dirname(__file__), "assets", "helmets.png"
)

def backBttnMainpage(): 
    """backBttnMainpage()
    
     Returns user back to mainpage gui
    
     Args:
         N/A

    Returns:
        N/A

    Raises:
        N/A
    """
    userSettings.destroy() 
    contrago_mainpage()
    
def openUserSettings():
    """openUserSettings()
    
        Makes a function call to userSettings() and updateUserSettings(). Also 
        closes current window (mainpage)

         Args:
             N/A

        Returns:
            N/A

        Raises:
            N/A
        """
    contra_goapp.CONTRAGO_DB.contra_go_log_in_db.userSettings()
    window.destroy()
    updateUserSettings()


def makeUserSettingsChanges(columnName, updateChange, username):
    """makeUserSettingsChanges(columnName, updateChange, username)
    
        Makes a function call to updateUserInfo(columnName,updateChange, username)
        located in contra_go_log_in_db file in database 

         Args:
             columnName: String name of cetain database column
             updateChange: String of change being made to specified column
             username: String of username to specify which account changes are being made in 

        Returns:
            N/A

        Raises:
            N/A
        """
    contra_goapp.CONTRAGO_DB.contra_go_log_in_db.updateUserInfo(columnName,updateChange, username)
    
def userLogOut(): 
    """userLogOut()
    
        Logs out user out of account and makes current user blank

         Args:
             N/A

        Returns:
            N/A

        Raises:
            N/A
        """
    file = open("user.txt","r+")
    
    file.truncate(0)
    
    file.close()
    
    window.destroy()
    contra_goapp.CONTRAGO_GUI.contra_go_log_in_GUI.contrago_log_in()
    
    

def openFillForm(): 
    
    """openFillForm()

    Opens new fill form gui and destroy 
    previous process 

    Args:
      N/A


    """
    window.destroy()
    ContraGO_Estimate_Module()
    
def updateUserSettings(): 
    """updateUserSettings()

    Executes the userSetting module of the mainpage 
    which allows user to change their information (Address, City,..)
    
    Args:
      N/A


    """
    
    global userSettings 
    
    file1 = open("user.txt","r+")
    
    conName = str(file1.readline().strip())
    
    file1.close()
    
    userSettings = Tk()
    
    userSettings.geometry("500x500")
    userSettings.configure(bg = "#FFFFFF")
    userSettings.title("ContraGO - Information Update Module")
    userSettings.iconbitmap(contrago_favicon)
    
    """ 
    Tkinter Canvas Create
    """ 
    canvas = Canvas(
        userSettings,
        bg = "#FFFFFF",
        height = 500,
        width = 500,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    
    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        37.0,
        500.0,
        500.0,
        fill="#F8F4E8",
        outline="")
    
    """ 
    Tkinter GUI Buttons
    Buttons: 
        updateChange
        backBttn
    """ 
    updateChange = Button(
        font=('ArialNarrow 10 bold'),
        bg="#C8CDFF",
        text="Update",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: makeUserSettingsChanges(str(enterColumn.get().strip()), str(enterItem.get().strip()), str(conName.strip())),
        relief="flat"
    )
    updateChange.place(
        x=170.0,
        y=380.0,
        width=130.0,
        height=50.0
    )
    
    backBttn = Button(
        font=('ArialNarrow 10 bold'),
        bg="#C8CDFF",
        text="Back",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: backBttnMainpage(),
        relief="flat"
    )
    backBttn.place(
        x=10,
        y=5,
        width=74.6417236328125,
        height=34.33673095703125
    )
   
    """ 
    Tkinter GUI Entry Fields 
    Entry Fields: 
        
    """
    enterColumn = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    enterColumn.place(
        x=212.0,
        y=190.0,
        width=197.0,
        height=32.0
    )
    
    
    enterItem = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    enterItem.place(
        x=224.0,
        y=285.0,
        width=197.0,
        height=32.0
    )
    
    canvas.create_rectangle(
        0.0,
        2.0,
        500.0,
        41.0,
        fill="#E8DBBF",
        outline="")
    
   
    """ 
    Tkinter GUI Title 
    """ 
    canvas.create_text(
        95.0,
        10.0,
        anchor="nw",
        text="Update User Settings",
        fill="#585858",
        font=("CrimsonText Regular", 24 * -1)
    )
    
    canvas.create_text(
        27.0,
        197.0,
        anchor="nw",
        text="Enter Item Name:",
        fill="#000000",
        font=("CourierPrime Regular", 18 * -1)
    )
    
    canvas.create_text(
        24.0,
        292.0,
        anchor="nw",
        text="Enter Item Change:",
        fill="#000000",
        font=("CourierPrime Regular", 18 * -1)
    )
    
    canvas.create_text(
        27.0,
        74.0,
        anchor="nw",
        text="Please use the following naming scheme to select what you want changed in\n Enter Item Name Entry Field Below:",
        fill="#000000",
        font=("CourierPrime Regular", 12 * -1)
    )
    
    canvas.create_text(
        27.0,
        100.0,
        anchor="nw",
        text="\n\nusername, password, userFirstName, userLastName, userAddress, userCity,\nuserState, userZipcode, userPhoneNumber, userEmailAddress",
        fill="#000000",
        font=("CourierPrime Regular", 12 * -1)
    )
    userSettings.resizable(False, False)
    userSettings.mainloop()

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
    window.iconbitmap(contrago_favicon)
    
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
    
       
    """ 
    Tkinter Canvas Background Image 
    """ 

    pic = Image.open(helmetImage)
    resized = pic.resize((1400, 800), Image.ANTIALIAS)
    bg = ImageTk.PhotoImage(resized)
    canvas.create_image(0, 400, image=bg)
    
    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        451,
        2,
        1197,
        777,
        fill="#F9ECD3",
        outline="#e8a854", width=5)
    
    
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
        font=('Coda 30 bold'),
        bg="#BD8000",
        borderwidth=20,
        fg='white',
        activebackground="#BD8000",
        command=lambda: getContractHistory(),
        relief="raised"
    )
    
    viewHistoryBttn.place(
        x=546.0,
        y=401.0,
        width=557.0,
        height=156
    )
    
    
    createContractBttn = Button(
        text="Create Contract",
        font=('Coda 30 bold'),
        bg="#BD8000",
        fg='white',
        borderwidth=20,
        activebackground="#BD8000",
        command=lambda: openFillForm(),
        relief="raised"
    )
    createContractBttn.place(
        x=546.0,
        y=221.0,
        width=557.0,
        height=156
    )
    
    aboutBttn = Button(
        text="ABOUT",
        font=('Coda 11 bold'),
        bg="#ffe8b3",
        borderwidth=4,
        command=lambda: print("button_4 clicked"),
        relief="ridge"
    )
    aboutBttn.place(
        x=160,
        y=460,
        width=130,
        height=35
    )
    
    logOutBttn = Button(
        text="LOG OUT",
        font=('Coda 11 bold'),
        bg="#ffe8b3",
        borderwidth=4,
        command=lambda: userLogOut(),
        relief="ridge"
    )
    logOutBttn.place(
        x=160,
        y=540,
        width=130,
        height=35
    )
    
    userSettingBttn = Button(
       text="UPDATE ACCOUNT",
       font=('Coda 8 bold'),
       bg="#ffe8b3",
       borderwidth=4,
       command=lambda: openUserSettings(),
       relief="ridge"
       )
    userSettingBttn.place(
       x=160,
       y=500,
       width=130,
       height=35
       )
    
    
    """ 
    Tkinter GUI Title 
    """ 
    canvas.create_text(
        92,
        247.0,
        anchor="nw",
        text="Welcome",
        fill="#474545",
        font=("Crimson Text", 66 * -1)
    )
    canvas.create_text(
        96,
        250,
        anchor="nw",
        text="Welcome",
        fill="white",
        font=("Crimson Text", 64 * -1)
    )
    
    canvas.create_text(
        202,
        302,
        anchor="nw",
        text="to",
        fill="#474545",
        font=("Crimson Text", 47 * -1)
    )
    canvas.create_text(
        205,
        305,
        anchor="nw",
        text="to",
        fill="white",
        font=("Crimson Text", 45 * -1)
    )

    canvas.create_text(
            55,
            315,
            anchor="nw",
            text="ContraGO",
            fill="white",
            font=("Dancing Script Bold", 90 * -1)
        )
    canvas.create_text(
            52,
            312,
            anchor="nw",
            text="ContraGO",
            fill="black",
            font=("Dancing Script Bold", 90 * -1)
        )
    canvas.create_text(
            50,
            310,
            anchor="nw",
            text="ContraGO",
            fill="purple",
            font=("Dancing Script Bold", 90 * -1)
        )
    window.resizable(False, False)
    window.mainloop()
    
    
if __name__ == "__main__":
    contrago_mainpage()