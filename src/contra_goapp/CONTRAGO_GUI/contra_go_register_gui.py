

from tkinter import Tk, Canvas, Entry, Text, Button, messagebox

from contra_goapp.CONTRAGO_DB.contra_go_register_db import registerUser


def validateRegister(username, password, userFirstName, userLastName, userAddress, userCity, userState,  userZipcode, userPhoneNumber, userEmailAddress):
    
   if registerUser(username.strip(), password.strip(), userFirstName.strip(), userLastName.strip(), userAddress.strip(), userCity.strip(), userState.strip(),  userZipcode.strip(), userPhoneNumber.strip(), userEmailAddress.strip()) == 1:
       messagebox.showinfo("ContraGo - Register","Username already exist. Please enter a new username")
   else: 
       registerUser(username.strip(), password.strip(), userFirstName.strip(), userLastName.strip(), userAddress.strip(), userCity.strip(), userState.strip(),  userZipcode.strip(), userPhoneNumber.strip(), userEmailAddress.strip())
       messagebox.showinfo("ContraGo - Register","Successfully Made Account. Please Log In")
    
def contrago_register():
    
    window = Tk()
    
    """ 
    Tkinter Window Dimensions 
    """ 
    window.title("ContraGO - Register")
    window.geometry("748x780")
    window.configure(bg = "#FFFFFF")
    
    
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
        748.0,
        62.0,
        fill="#E8DBBF",
        outline="")
    
    canvas.create_rectangle(
        73.0,
        166.0,
        684.0,
        711.0,
        fill="#808080",
        outline="")
    
    
    
    """ 
    Tkinter GUI Buttons
    Buttons: 
        Register
        Clear
        Back
    """ 
    registerBttn = Button(
        font=('ArialNarrow 10 bold'),
        bg="#C8CDFF",
        text="Register",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: validateRegister(username.get(), password.get(), userFirstName.get(), userLastName.get(), userAddress.get(), userCity.get(), userState.get(),  userZipCode.get(), userPhoneNumber.get(), userEmailAddress.get()),
        relief="flat"
    )
    registerBttn.place(
        x=232.0,
        y=644.0,
        width=130.0,
        height=50.0
    )
    
    
    clearBttn = Button(
        font=('ArialNarrow 10 bold'),
        bg="#C8CDFF",
        text="Clear",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    clearBttn.place(
        x=385.0,
        y=644.0,
        width=130.0,
        height=50.0
    )
    
    
    
    backBttn = Button(
        font=('ArialNarrow 10 bold'),
        bg="#C8CDFF",
        text="Back",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    backBttn.place(
        x=14.0,
        y=8.0,
        width=76.0,
        height=46.0
    )
    
    
    
    """ 
    Tkinter GUI Entry Fields 
    Entry Fields: 
        
    """
    username = Entry(
        bd=0,
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
        font=("Coda Regular", 16 * -1)
    )
    
    
    password = Entry(
        bd=0,
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
        font=("Coda Regular", 16 * -1)
    )
    
    
    userEmailAddress = Entry(
        bd=0,
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
        font=("Coda Regular", 16 * -1)
    )
    
    
    userPhoneNumber = Entry(
        bd=0,
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
        font=("Coda Regular", 16 * -1)
    )
    
    
    
    userZipCode = Entry(
        bd=0,
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
        font=("Coda Regular", 16 * -1)
    )
    
    

    userState = Entry(
        bd=0,
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
        font=("Coda Regular", 16 * -1)
    )
    
    
    userCity = Entry(
        bd=0,
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
        font=("Coda Regular", 16 * -1)
    )
    
    
    
    
    
    userAddress = Entry(
        bd=0,
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
        font=("Coda Regular", 16 * -1)
    )
    
    
    
    
    
    userLastName = Entry(
        bd=0,
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
        font=("Coda Regular", 16 * -1)
    )
    
    
    
    
    
    
    userFirstName = Entry(
        bd=0,
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
        font=("Coda Regular", 16 * -1)
    )
    
    """ 
    Tkinter GUI Title 
    """ 
    canvas.create_text(
        67.0,
        126.0,
        anchor="nw",
        text="User Information",
        fill="#441B00",
        font=("AplikaziaMFW Bold", 25 * -1)
    )
    
    
    canvas.create_text(
        105.0,
        4.0,
        anchor="nw",
        text="Register",
        fill="#585858",
        font=("CrimsonText Regular", 50 * -1)
    )
    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    contrago_register()