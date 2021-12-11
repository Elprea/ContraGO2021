
from tkinter import Button, Canvas, Entry, PhotoImage, Text, Tk, Toplevel, messagebox

from contra_goapp.CONTRAGO_DB.contra_go_log_in_db import registerUser, validationUser

from contra_goapp.CONTRAGO_GUI.contra_go_mainpage_gui import contrago_mainpage

def contrago_register():
    
    """contrago_register()

    Checks if user credentials are valid 
    to close and open new window for mainpage

    Args:
      N/A


    """
    window1 = Toplevel(window)
    
    window1.title("Contra - GO Register")
    


def valUserClose(username, password): 
    
    """valUserClose(username, password)

    Checks if user credentials are valid 
    to close and open new window for mainpage

    Args:
      username: A string value for username
      password: A string value for password


    """
    if validationUser(username, password) == 1: 
        
        window.destroy()
        contrago_mainpage()
       
        
    else: 
        
        messagebox.showinfo("ContraGo Log In","Incorrect Information")


def contrago_log_in(): 
    
    """contrago_log_in()

    Executes the log in gui module for 
    user log in and register module 

    Args:
      N/A


    """
    global window
    global username 
    global password
    
    
    window = Tk()
    
    
    """ 
    Tkinter Window Dimensions 
    """ 
    window.title("ContraGO - Log In/Register")
    window.geometry("1152x700")
    window.configure(bg="#AEC0FF")
    
    
    
    """ 
    Tkinter Canvas Create
    """ 
    canvas = Canvas(
        window,
        bg="#AEC0FF",
        height=700,
        width=1152,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )
    
    canvas.place(x=0, y=0)
    canvas.create_rectangle(0.0, 0.0, 1109.0, 700.0, fill="#AEC0FF", outline="")
    
    canvas.create_text(
        609.0,
        75.0,
        anchor="nw",
        text="ContraGO",
        fill="#000000",
        font=("AplikaziaMFW Bold", 50 * -1),
    )
    
    canvas.create_text(
        609.0,
        142.0,
        anchor="nw",
        text="Log In",
        fill="#000000",
        font=("AplikaziaMFW Bold", 36 * -1),
    )
    
    
    
    
    """ 
    Tkinter GUI Entry Fields 
    Entry Fields: 
        
    """
    username = Entry(
        bd=0,
        bg="#6A79FD",
        highlightthickness=0
    )
    username.place(
        x=643.0,
        y=328.0,
        width=320.0,
        height=34.0
    )
    
    
    password = Entry(
        bd=0,
        bg="#6A79FD",
        highlightthickness=0
    )
    password.place(
        x=643.0,
        y=430.0,
        width=320.0,
        height=34.0
    )
    
    
    """ 
    Tkinter GUI Title 
    """ 
    canvas.create_text(
        609.0,
        284.0,
        anchor="nw",
        text="Username",
        fill="#000000",
        font=("AplikaziaMFW Bold", 24 * -1),
    )
    
    canvas.create_text(
        609.0,
        383.0,
        anchor="nw",
        text="Password\n",
        fill="#000000",
        font=("AplikaziaMFW Bold", 24 * -1),
    )
    
    
    
    
    """ 
    Tkinter GUI Buttons
    Buttons: 
        login 
        Register 
    """ 
    # Log In Button
    loginBttn = Button(
        text="Submit",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print('daw'),
        relief="flat",
    )
    
    loginBttn.place(
        x=640.079833984375, 
        y=508.1396484375, 
        width=133.920166015625, 
        height=46.8603515625
    )
    
    
    
    # Register Button
    registerBttn = Button(
        text="Register",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: valUserClose(username.get(), password.get()),
        relief="flat",
    )
    
    registerBttn.place(
        x=830.079833984375, 
        y=508.1396484375, 
        width=133.920166015625, 
        height=46.8603515625
    )
    
    
    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    contrago_log_in()