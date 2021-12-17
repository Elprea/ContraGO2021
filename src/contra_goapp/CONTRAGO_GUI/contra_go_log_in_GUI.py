""" ContraGO Log In GUI Program

This program will run tkinter GUI program that will allow the user to log in 
into their existing account and also register to a new account



"""

import os

from tkinter import Button, Canvas, Entry, Tk, messagebox, PhotoImage

from contra_goapp.CONTRAGO_DB.contra_go_log_in_db import validationUser

import contra_goapp.CONTRAGO_GUI.contra_go_mainpage_gui 

import contra_goapp.CONTRAGO_GUI.contra_go_register_gui 


# Favicon On Tkinter Window 
contrago_favicon = os.path.join(
    os.path.dirname(__file__), "assets", "contrago.ico"
)
bgImage = os.path.join(
    os.path.dirname(__file__), "assets", "bg.png"
)

        
def contraReg():
    
    """contrago_register()
    Checks if user credentials are valid 
    to close and open new window for mainpage

    Args:
      N/A


    """
    window.destroy()
    contra_goapp.CONTRAGO_GUI.contra_go_register_gui.contrago_register()
    
    
    
           
def valUserClose(username, password): 
    
    """valUserClose(username, password)

    Checks if user credentials are valid 
    to close and open new window for mainpage

    Args:
      username: A string value for username
      password: A string value for password


    """
    if validationUser(username, password) == 0: 
        
        file=open("user.txt", "w") 
        file.truncate(0)
        file.write(str(username)+"\n")
        file.write(str(password))
        file.close() 
        
        window.destroy()
        contra_goapp.CONTRAGO_GUI.contra_go_mainpage_gui.contrago_mainpage()
        
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
    window.iconbitmap(contrago_favicon)
    
    
    
    """ 
    Tkinter Canvas Create
    """ 
    canvas = Canvas(
        window,
        height=700,
        width=1152,
        bg="gray",
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )
    canvas.place(x=0, y=0)
    
    """
    background
    """
    bg = PhotoImage(file=bgImage)
    canvas.create_image(500, 350, image=bg)
    
    #ContraGo
    canvas.create_text(
        405,
        105,
        text="ContraGO",
        anchor="nw",
        fill="white",
        font=("Dancing Script BOLD", 100 * -1),
    )
    canvas.create_text(
        400,
        100,
        text="ContraGO",
        anchor="nw",
        fill="purple",
        font=("Dancing Script BOLD", 100 * -1),
    )
    
    #Log In
    canvas.create_text(
        550,
        280,
        text="LOG-IN",
        anchor="nw",
        fill="#000000",
        font=("Coda", 22 * -1),
    )
    
        
    """
    Function for Entry fields
    """
    def entry_click(e):
        if username.get() == 'Username':
            username.delete(0, "end")
            username.insert(0, '')
            username.config(show="", fg="black")

    def focusout(e):
        if username.get() == '':
            username.insert(0, 'Username')
            username.config(show="", fg="gray")
       
    def entry_click_pass(e):     
        if password.get() == 'Password':
            password.delete(0, "end")
            password.insert(0, '')
            password.config(show="*", fg="black")
    def focusout_pass(e):
        if password.get() == '':
            password.config(show="", fg="gray")
            password.insert(0, 'Password')
            
    
    """ 
    Tkinter GUI Entry Fields 
    Entry Fields: 
        
    """
    
    username = Entry(
        bd=4,
        fg="gray",
        bg="white",
        highlightthickness=0,
        font=("Coda", 16 * -1),
    )
    username.insert(0, 'Username')
    username.bind('<FocusIn>', entry_click)
    username.bind('<FocusOut>', focusout)
    username.place(
        x=430,
        y=320,
        width=320.0,
        height=34.0
    )
    
    
    password = Entry(
        bd=4,
        fg="gray",
        bg="white",
        highlightthickness=0,
        font=("Coda", 16 * -1),
    )
    password.insert(0, 'Password')
    password.bind('<FocusIn>', entry_click_pass)
    password.bind('<FocusOut>', focusout_pass)
    password.place(
        x=430,
        y=370,
        width=320.0,
        height=34.0
    )
    
    
    """ 
    Tkinter GUI Buttons
    Buttons: 
        login 
        Register 
    """ 
    # Log In Button
    loginBttn = Button(
        text="SUBMIT",
        font=("Coda", 16 * -1),
        bg='#f7edf5',
        fg='#210205',
        command=lambda: valUserClose(username.get().strip(), password.get().strip()),
        relief="raised",
    )
    
    loginBttn.place(
        x=640, 
        y=412, 
        width=110, 
        height=40
    )
    
    def entry_click(e):
        if username.get() == 'Username':
            username.delete(0, "end")
            username.insert(0, '')

    def focusout(e):
        if username.get() == '':
            username.insert(0, 'Username')
            
    # Register Button
    registerBttn = Button(
        text="No account yet? Register here.",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: contraReg(), 
        relief="flat",
        fg="#1f96ff",
        bg="#E5D3E1",
        activebackground="#E5D3E1",
        font=("Coda 10 italic underline"),
    )
    
    registerBttn.place(
        x=415, 
        y=415, 
        width=200, 
        height=15
    )

    
    
    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    contrago_log_in()