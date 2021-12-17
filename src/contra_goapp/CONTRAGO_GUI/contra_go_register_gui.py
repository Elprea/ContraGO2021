""" ContraGO Register GUI Program

This program will run tkinter GUI program that will allow the user to register 
for a new account. The user will be able to create and view contract history 
when registering an account.


"""
from tkinter import Tk, Canvas, Entry, Button, messagebox, PhotoImage, END

import os

from contra_goapp.CONTRAGO_DB.contra_go_register_db import registerUser

import contra_goapp.CONTRAGO_GUI.contra_go_log_in_GUI


# Favicon For Tkinter Window
contrago_favicon = os.path.join(
    os.path.dirname(__file__), "assets", "contrago.ico"
)
backIcon = os.path.join(
    os.path.dirname(__file__), "assets", "back-icon.png"
)

def validateRegister(username, password, userFirstName, userLastName, userAddress, userCity, userState,  userZipcode, userPhoneNumber, userEmailAddress):
   """validateRegister(username, 
                    password, 
                    userFirstName, 
                    userLastName, 
                    userAddress, 
                    userCity, 
                    userState, 
                    userZipcode, 
                    userPhoneNumber, 
                    userEmailAddress)

    Checks if username exist in the datbase 

    Args:
      username: A string value 
      password: A string value 
      userFirstName: A string value 
      userLastName: A string value  
      userAddress: A string value  
      userCity: A string value 
      userState: A string value 
      userZipcode: A string value  
      userPhoneNumber: A string value  
      userEmailAddress: A string value 


    """
   if registerUser(username.strip(), password.strip(), userFirstName.strip(), userLastName.strip(), userAddress.strip(), userCity.strip(), userState.strip(),  userZipcode.strip(), userPhoneNumber.strip(), userEmailAddress.strip()) == 1:
       
       messagebox.showinfo("ContraGo - Register","Username already exist. Please enter a new username")
       
   else: 
       
       registerUser(username.strip(), password.strip(), userFirstName.strip(), userLastName.strip(), userAddress.strip(), userCity.strip(), userState.strip(),  userZipcode.strip(), userPhoneNumber.strip(), userEmailAddress.strip())
       
       messagebox.showinfo("ContraGo - Register","Successfully Made Account. Please Log In")
       
       window.destroy()
       
       contra_goapp.CONTRAGO_GUI.contra_go_log_in_GUI.contrago_log_in() 
       
    
def backLogIn(): 
        """backLogIn()

        Args:
          N/A

        Output:
          .docx editable file
        """
        window.destroy()
        contra_goapp.CONTRAGO_GUI.contra_go_log_in_GUI.contrago_log_in() 
        
    
def contrago_register():
    
    def clearFields(): 
        """clearFields()

        Args:
          N/A

        Output:
          N/A
        """
        username.delete(0, END)
        password.delete(0, END)
        userEmailAddress.delete(0, END)
        userPhoneNumber.delete(0, END)
        userZipCode.delete(0, END)
        userState.delete(0, END)
        userCity.delete(0, END)
        userAddress.delete(0, END)
        userFirstName.delete(0, END)
        userLastName.delete(0, END)
        messagebox.showinfo("ContraGo - Register","All Fields Cleared")
    
    global window 
    
    window = Tk()
    
    """ 
    Tkinter Window Dimensions 
    """ 
    window.title("ContraGO - Register")
    window.geometry("748x780")
    window.configure(bg = "#FFFFFF")
    window.iconbitmap(contrago_favicon)
    
    """ 
    Tkinter Canvas Create
    """ 
    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 780,
        width = 748,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    
    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        62.0,
        748.0,
        780.0,
        fill="#F8F4E8",
        outline="")
    
    canvas.create_rectangle(
        0.0,
        0.0,
        1440.0,
        75,
        fill="#d1a862",
        outline="#E8DBBF", width=2)
    
    canvas.create_rectangle(
        73.0,
        166.0,
        684.0,
        711.0,
        fill="#F8F4E8",
        outline="#AD5F00", width=5)
    
    
    
    """ 
    Tkinter GUI Buttons
    Buttons: 
        Register
        Clear
        Back
    """ 
    registerBttn = Button(
        text="Register",
        command=lambda: validateRegister(username.get(), password.get(), userFirstName.get(), userLastName.get(), userAddress.get(), userCity.get(), userState.get(),  userZipCode.get(), userPhoneNumber.get(), userEmailAddress.get()),
        highlightthickness=0,
        font=('Coda 18'),
        borderwidth=4,
        activebackground='#f7edf5',
        highlightcolor="black",
        bg='#f7edf5',
        fg='#210205',
        relief="raised",
    )
    registerBttn.place(
        x=232.0,
        y=644.0,
        width=130.0,
        height=50.0
    )
    
    
    clearBttn = Button(
        text="Clear",
        command=lambda: clearFields(),
        highlightthickness=0,
        font=('Coda 18'),
        borderwidth=4,
        activebackground='#f7edf5',
        highlightcolor="black",
        bg='#f7edf5',
        fg='#210205',
        relief="raised",
    )
    clearBttn.place(
        x=383.0,
        y=644.0,
        width=130.0,
        height=50.0
    )

        
    #Back Button
    backPhoto = PhotoImage(file=backIcon)
    backBttn = Button(
        font=('ArialNarrow 10 bold'),
        image=backPhoto,
        bg="#d1a862",
        activebackground='#d1a862',
        text="Back",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: backLogIn(),
        relief="flat"
    )
    backBttn.place(
        x=25.0,
        y=15.0,
        width=50.0,
        height=50.0
    )
    
    
    
    """ 
    Tkinter GUI Entry Fields 
    Entry Fields: 
        
    """
    username = Entry(
        bd=2,
        bg="#FFFFFF",
        highlightthickness=0
    )
    username.place(
        x=235.0,
        y=457.0,
        width=389.0,
        height=31.0
    )
    
    canvas.create_text(
        140.0,
        460.0,
        anchor="nw",
        text="Username:",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
    
    
    password = Entry(
        bd=2,
        bg="#FFFFFF",
        highlightthickness=0
    )
    password.place(
        x=235.0,
        y=520.0,
        width=389.0,
        height=31.0
    )
    
    canvas.create_text(
        140.0,
        526.0,
        anchor="nw",
        text="Password:",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
    
    
    userEmailAddress = Entry(
        bd=2,
        bg="#FFFFFF",
        highlightthickness=0
    )
    userEmailAddress.place(
        x=235.0,
        y=402.0,
        width=145.0,
        height=31.0
    )
    
    canvas.create_text(
        100.0,
        403.0,
        anchor="nw",
        text="E-mail address: ",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
    
    
    userPhoneNumber = Entry(
        bd=2,
        bg="#FFFFFF",
        highlightthickness=0
    )
    userPhoneNumber.place(
        x=235.0,
        y=348.0,
        width=145.0,
        height=30.0
    )
    
    canvas.create_text(
        100.0,
        352.0,
        anchor="nw",
        text="Phone Number:\n",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
    
    
    
    userZipCode = Entry(
        bd=2,
        bg="#FFFFFF",
        highlightthickness=0
    )
    userZipCode.place(
        x=529.0,
        y=290.0,
        width=95.0,
        height=31.0
    )
    
    canvas.create_text(
        461.0,
        296.0,
        anchor="nw",
        text="Zipcode: ",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
    
    

    userState = Entry(
        bd=2,
        bg="#FFFFFF",
        highlightthickness=0
    )
    userState.place(
        x=329.0,
        y=290.0,
        width=95.0,
        height=31.0
    )
    
    canvas.create_text(
        279.0,
        294.0,
        anchor="nw",
        text="State: ",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
    
    
    userCity = Entry(
        bd=2,
        bg="#FFFFFF",
        highlightthickness=0
    )
    userCity.place(
        x=143.0,
        y=292.0,
        width=95.0,
        height=29.0
    )
    
    canvas.create_text(
        100.0,
        297.0,
        anchor="nw",
        text="City: ",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
    
    
    
    
    
    userAddress = Entry(
        bd=2,
        bg="#FFFFFF",
        highlightthickness=0
    )
    userAddress.place(
        x=181.0,
        y=238.0,
        width=443.0,
        height=29.0
    )
    
    canvas.create_text(
        100.0,
        240.0,
        anchor="nw",
        text="Address: ",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
    
    
    
    
    
    userLastName = Entry(
        bd=2,
        bg="#FFFFFF",
        highlightthickness=0
    )
    userLastName.place(
        x=481.0,
        y=187.0,
        width=143.0,
        height=30.0
    )
    
    canvas.create_text(
        397.0,
        190.0,
        anchor="nw",
        text="Last Name:",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
    
    
    
    
    
    
    userFirstName = Entry(
        bd=2,
        bg="#FFFFFF",
        highlightthickness=0
    )
    userFirstName.place(
        x=193.0,
        y=187.0,
        width=133.0,
        height=26.0
    )
    
    canvas.create_text(
        100.0,
        190.0,
        anchor="nw",
        text="First Name:",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
    
    
    """ 
    Tkinter GUI Title 
    """ 
    canvas.create_text(
        72.0,
        126.0,
        anchor="nw",
        text="User Information",
        fill="#441B00",
        font=('Coda Caption ExtraBold', 25 * -1)
    )
    
    canvas.create_text(
        90.0,
        3.0,
        anchor="nw",
        text="Contract Maker",
        fill="black",
        font=("Crimson Text Bold", 50 * -1)
    )
    canvas.create_text(
        88.0,
        1.0,
        anchor="nw",
        text="Contract Maker",
        fill="white",
        font=("Crimson Text Bold", 50 * -1)
    )
    
    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    contrago_register()