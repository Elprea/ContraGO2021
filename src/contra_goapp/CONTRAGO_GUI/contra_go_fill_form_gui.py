""" ContraGO Form Fill Out Program

This program will run tkinter GUI program that will allow the user to
fill out entry fields of the GUI and click on submit button to create a
new .docx file that will outputed for the contractor to use



"""
from __future__ import print_function

import os
import sqlite3

from tkinter import Button, Canvas, Entry, Text, Tk, END, messagebox, PhotoImage

from datetime import date 

from mailmerge import MailMerge

from contra_goapp.CONTRAGO_DB.contra_go_fill_form_gui_db import contractHistoryInsert

import contra_goapp.CONTRAGO_GUI.contra_go_mainpage_gui 


# Favicon On Tkinter Window 
contrago_favicon = os.path.join(
    os.path.dirname(__file__), "assets", "contrago.ico"
)

#Estimate Template
estimate_template = os.path.join(
    os.path.dirname(__file__), "assets", "ContraGO_ContractEstimate.docx"
)


# Final Contract Template
finalContract_template = os.path.join(
    os.path.dirname(__file__), "assets", "ContraGO_FinalContract.docx"
)

backIcon = os.path.join(
    os.path.dirname(__file__), "assets", "back-icon.png"
)

estimate_document = MailMerge(estimate_template)

final_document = MailMerge(finalContract_template)



def getContractorName(): 
    """getContractorName()

         Args:
             N/A

        Returns:
            A string of current user logged in Name

        Raises:
            N/A
        """
    global conName
    
    file1 = open("user.txt", "r")

    conName = file1.readline().strip()
    
    file1.close()
    
    conn = sqlite3.connect("ContraGOUser.db")

    cursor = conn.cursor()
    
    cursor.execute("SELECT userFirstName from ContraGO_UInformation WHERE username=" + "\"" + conName + "\"")
    
    result = cursor.fetchone()
    first_name = str(result[0])
    
    cursor.execute("SELECT userLastName from ContraGO_UInformation WHERE username=" + "\"" + conName + "\"")
   
    result = cursor.fetchone()
    last_name = str(result[0])
    
    conn.commit() 
    
    full_name = str(first_name) + " " + str(last_name)
    
    return full_name


def getContractorPhoneNumber(): 
    """getContractorPhoneNumber()

         Args:
             N/A

        Returns:
            A string of current user logged in phone number

        Raises:
            N/A
        """
    file1 = open("user.txt", "r")

    conName = file1.readline().strip()
    
    file1.close()
    
    conn = sqlite3.connect("ContraGOUser.db")

    cursor = conn.cursor()
    
    cursor.execute("SELECT userPhoneNumber from ContraGO_UInformation WHERE username=" + "\"" + conName + "\"")
    
    result = cursor.fetchone()
    
    phoneNumber = str(result[0])
    
    contractorPhoneNumber = str(phoneNumber) 
    
    return contractorPhoneNumber


def getContractorAddress(): 
    """getContractorAddress()

         Args:
             N/A

        Returns:
            A string of concantanted address of user

        Raises:
            N/A
        """
    file1 = open("user.txt", "r")

    conName = file1.readline().strip()
    
    file1.close()
    
    conn = sqlite3.connect("ContraGOUser.db")

    cursor = conn.cursor()
    
    cursor.execute("SELECT userAddress from ContraGO_UInformation WHERE username=" + "\"" + conName + "\"")
    
    result = cursor.fetchone()
    
    address = str(result[0])
    
    cursor.execute("SELECT userCity from ContraGO_UInformation WHERE username=" + "\"" + conName + "\"")
    
    result = cursor.fetchone()
    
    city = str(result[0])
    
    cursor.execute("SELECT userState from ContraGO_UInformation WHERE username=" + "\"" + conName + "\"")
    
    result = cursor.fetchone()
    
    state = str(result[0])
    
    cursor.execute("SELECT userZipcode from ContraGO_UInformation WHERE username=" + "\"" + conName + "\"")
    
    result = cursor.fetchone()
    
    zipcode = str(result[0])
    
    full_address = str(address) + ", " + str(city) + ", " + str(state) + ", " + str(zipcode) 
    
    return full_address
    


def ContraGO_Estimate_Module():
    
    def backMainpage(): 
        """backMainpage()

        Args:
          N/A

        Output:
          .docx editable file
        """
        window.destroy()
        contra_goapp.CONTRAGO_GUI.contra_go_mainpage_gui.contrago_mainpage()
        
    
    def submitForm():

        """submitForm()

        Args:
          N/A

        Output:
          .docx editable file
        """
        
        currentDate = date.today()
        
        final_estimate = int(matCost.get()) + int(demoCost.get()) + int(laborCost.get())
        
        file1 = open("user.txt", "r")
        # Estimate Contract Mailmerge Input
        estimate_document.merge(
            # Contractor Information
            contractorName=str(getContractorName()),
            contractorPhoneNumber=str(getContractorPhoneNumber()),
            contractorAddress=str(getContractorAddress()),
            CurrentDate=currentDate.strftime("%m/%d/%y"),
            # Client Information
            ClientAddress=clientAdd.get(),
            ClientName=clientName.get(),
            ClientPhoneNumber=clientPhoneN.get(),
            City=clientCity.get(),
            ClientState=clientState.get(),
            ZipCode=clientZip.get(),
            # Job Information
            JobDescription=jobDes.get("1.0", END),
            MaterialCost=matCost.get(),
            DemolitionCost=demoCost.get(),
            LaborCost=laborCost.get(),
            JobType=jobType.get(),
            EstimateTotal=str(final_estimate),
        )
        
        full_address = str(clientAdd.get() + ", " + clientCity.get() + ", " + clientState.get() + ", " + clientZip.get())
        
        estimate_document.write(str(full_address + "_" + clientName.get()) + "_EstimateContract.docx")
        
        # Final Contract Mailmerge Input
        final_document.merge(
            # Contractor Information
            ContractorName=getContractorName(),
            ContractorAddress=getContractorAddress(),
            ContractorWarranty=warranty.get(),
            # Client Information
            EmployerAddress=full_address,
            EmployerName=clientName.get(),
            # Job Information
            StartDate=startDate.get(),
            JobDescription=jobDes.get("1.0", END),
            PaymentTypes=paymentType.get(),
            TotalJobPrice=str(final_estimate)
        )
        
        final_document.write(str(full_address + "_" + clientName.get()) + "_FinalContract.docx")
        
        
        contractHistoryInsert(clientName.get(), 
                             clientPhoneN.get(), 
                             clientAdd.get(), 
                             clientCity.get(), 
                             clientZip.get(),
                             clientState.get(), 
                             str(file1.readline()), 
                             str(full_address + clientName.get() + "_EstimateContract.docx"),
                             str(full_address + clientName.get() + "_FinalContract.docx"))
        file1.close()
        messagebox.showinfo("ContraGo - Contract Maker","Successfully Generated Your Contract, Returning to Mainpage")
        window.destroy()
        contra_goapp.CONTRAGO_GUI.contra_go_mainpage_gui.contrago_mainpage()
    
    def clearFields(): 
        """clearFields()

        Args:
          N/A

        Output:
          N/A
        """
        clientAdd.delete(0, END)
        clientName.delete(0, END)
        clientPhoneN.delete(0, END)
        clientCity.delete(0, END)
        clientState.delete(0, END)
        clientZip.delete(0, END)
        matCost.delete(0, END)
        demoCost.delete(0, END)
        laborCost.delete(0, END)
        startDate.delete(0, END)
        endDate.delete(0, END)
        jobType.delete(0, END)
        jobDes.delete("1.0", "end")
        paymentType.delete(0, END) 
        warranty.delete(0, END)
        messagebox.showinfo("ContraGo - Contract Maker","All Fields Have Been Cleared")
        

    global window
    window = Tk()
    

    """ 
    Tkinter Window Dimensions 
    """ 
    window.title("Contra GO - Contract Maker")
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
    
    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        67.0,
        1200.0,
        781.0,
        fill="#F8F4E8",
        outline="")
    
    canvas.create_rectangle(
        475.0,
        139.0,
        1168.0,
        758.0,
        fill="#F8F4E8",
        outline="#AD5F00", width=5)
    
    canvas.create_rectangle(
        36.0,
        197.0,
        452.0,
        715.0,
        fill="#F8F4E8",
        outline="#AD5F00", width=5)

    
    """ 
    Tkinter GUI Entry Fields 
    Entry Fields: 
        
    """
    #endDate Entry & Label
    endDate = Entry(
        bd=2,
        bg="#FFFFFF",
        highlightthickness=0
    )
    endDate.place(
        x=603,
        y=668,
        width=150,
        height=30
    )
    
    canvas.create_text(
        520,
        671,
        anchor="nw",
        text="End Date:\n",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
    
    
    #startDate Entry & Label
    startDate = Entry(
        bd=2,
        bg="#FFFFFF",
        highlightthickness=0
    )
    startDate.place(
        x=603.0,
        y=619.0,
        width=150,
        height=30
    )
    
    canvas.create_text(
        520.0,
        621.0,
        anchor="nw",
        text="Start Date:\n",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
    
    
    
    
    #demoCost Entry & Label
    demoCost = Entry(
        bd=2,
        bg="#FFFFFF",
    )
    demoCost.place(
        x=819,
        y=559.0,
        width=150,
        height=30
    )
    
    canvas.create_text(
        834,
        532,
        anchor="nw",
        text="Demolition Cost:",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
    
       
    
    #laborCost Entry & Label
    laborCost = Entry(
        bd=2,
        bg="#FFFFFF",
    )
    laborCost.place(
        x=986,
        y=559.0,
        width=150,
        height=30
    )
    
    canvas.create_text(
        1020.0,
        532.0,
        anchor="nw",
        text="Labor Cost:",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
    
    #Payment Type Entry & Label
    paymentType = Entry(
        bd=2,
        bg="#FFFFFF",
        highlightthickness=0
    )
    paymentType.place(
        x=986,
        y=619,
        width=150,
        height=30
    )
    
    canvas.create_text(
        865.0,
        621.0,
        anchor="nw",
        text="Payment Type:",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
    
    
    
    #matCost Entry & Label
    matCost = Entry(
        bd=2,
        bg="#FFFFFF",
        highlightthickness=0
    )
    matCost.place(
        x=652,
        y=559.0,
        width=150,
        height=30
    )
    
    canvas.create_text(
        677,
        532,
        anchor="nw",
        text="Material Cost:",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
     
    #Warranty Entry & Label
    warranty = Entry(
        bd=2,
        bg="#FFFFFF",
        highlightthickness=0
    )
    warranty.place(
        x=520,
        y=559.0,
        width=91,
        height=30
    )
    
    canvas.create_text(
        531,
        532.0,
        anchor="nw",
        text="Warranty:",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
    
    
    #jobDes Entry & Label
    jobDes = Text(
        bd=2,
        bg="#FFFFFF",
        highlightthickness=0
    )
    jobDes.place(
        x=502.0,
        y=244.0,
        width=643.0,
        height=261.0
    )
    
    canvas.create_text(
        497.0,
        218.0,
        anchor="nw",
        text="Job Description:",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
    
       
    
    #jobType Entry & Label
    jobType = Entry(
        bd=2,
        bg="#FFFFFF",
        highlightthickness=0
    )
    jobType.place(
        x=579.0,
        y=156.0,
        width=337.0,
        height=34.0
    )
    
    canvas.create_text(
        499.0,
        162.0,
        anchor="nw",
        text="Job Type:",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
    
    
    
    

    #clientPhoneN Entry & Label
    clientPhoneN = Entry(
        width =11,
        bd=2,
        bg="#FFFFFF",
        highlightthickness=0
    )
    clientPhoneN.place(
        x=66.0,
        y=644.0,
        width=356.0,
        height=30.0
    )
    
    canvas.create_text(
        63.0,
        622.0,
        anchor="nw",
        text="Client Phone Number:",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
    
    
    
    #clientState Entry & Label
    clientState = Entry(
        bd=2,
        bg="#FFFFFF",
        highlightthickness=0
    )
    clientState.place(
        x=66.0,
        y=563.0,
        width=356.0,
        height=31.0
    )
    
    canvas.create_text(
        63.0,
        539.0,
        anchor="nw",
        text="Client State:",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
    
    
    #clientZip Entry & Label
    clientZip = Entry(
        bd=2,
        bg="#FFFFFF",
        highlightthickness=0
    )
    clientZip.place(
        x=66.0,
        y=482.0,
        width=356.0,
        height=29.0
    )
    
    canvas.create_text(
        63.0,
        457.0,
        anchor="nw",
        text="Client Zipcode:",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
    
    
    #clientCity Entry & Label
    clientCity = Entry(
        bd=2,
        bg="#FFFFFF",
        highlightthickness=0
    )
    clientCity.place(
        x=66.0,
        y=400.0,
        width=356.0,
        height=29.0
    )
    
    canvas.create_text(
        63.0,
        376.0,
        anchor="nw",
        text="Client City:",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
    
    
    #clientAdd Entry & Label
    clientAdd = Entry(
        bd=2,
        bg="#FFFFFF",
        highlightthickness=0
    )
    clientAdd.place(
        x=66.0,
        y=318.0,
        width=356.0,
        height=30.0
    )
    
    canvas.create_text(
        63.0,
        296.0,
        anchor="nw",
        text="Client Address:",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
    
    
    #clientName Entry & Label
    clientName = Entry(
        bd=2,
        bg="#FFFFFF",
        highlightthickness=0
    )
    clientName.place(
        x=66.0,
        y=242.0,
        width=356.0,
        height=26.0
    )
    
    canvas.create_text(
        63.0,
        217.0,
        anchor="nw",
        text="Client Name:",
        fill="#000000",
        font=("Coda", 16 * -1)
    )
    
    
    """ 
    Tkinter GUI Buttons
    Buttons: 
        Generate 
        Clear
        Back 
    """ 
    clearBttn = Button(
        text="Clear",
        highlightthickness=0,
        command=lambda: clearFields(),
        font=('Coda 18'),
        borderwidth=4,
        activebackground='#f7edf5',
        highlightcolor="black",
        bg='#f7edf5',
        fg='#210205',
        relief="raised",
    )
    clearBttn.place(
        x=865.0,
        y=686.0,
        width=130.0,
        height=50.0
    )
    
    #Generate Button
    genBttn = Button(
        font=('Coda 18'),
        text="Generate",
        borderwidth=4,
        activebackground='#f7edf5',
        highlightthickness=0,
        highlightcolor="black",
        command=lambda: submitForm(),
        bg='#f7edf5',
        fg='#210205',
        relief="raised",
    )
    genBttn.place(
        x=1006.0,
        y=685.0,
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
        command=lambda: backMainpage(),
        relief="flat"
    )
    backBttn.place(
        x=25.0,
        y=15.0,
        width=50.0,
        height=50.0
    )

    """
    Tkinter GUI Title 
    """ 
    canvas.create_text(
        46.0,
        158.0,
        anchor="nw",
        text="Client & Contractor Details",
        fill="#441B00",
        font=('Coda Caption ExtraBold', 25 * -1)
    )
    
    canvas.create_rectangle(
        0.0,
        0.0,
        1440.0,
        75,
        fill="#d1a862",
        outline="#E8DBBF", width=2)
    
    canvas.create_text(
        90,
        3,
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
    
    canvas.create_text(
        628.0,
        100.0,
        anchor="nw",
        text="Contractor Measurements",
        fill="#441B00",
        font=("Coda Caption ExtraBold", 25 * -1)
    )

    

    
    window.resizable(False, False)
    window.mainloop()


if __name__ == "__main__":
    ContraGO_Estimate_Module()
