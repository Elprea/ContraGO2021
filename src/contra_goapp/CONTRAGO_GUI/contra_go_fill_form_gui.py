""" ContraGO Form Fill Out Program

This program will run tkinter GUI program that will allow the user to
fill out entry fields of the GUI and click on submit button to create a
new .docx file that will outputed for the contractor to use

  Typical usage example:


"""
from __future__ import print_function

import os


from tkinter import Button, Canvas, Entry, Text, Tk, END

from mailmerge import MailMerge

from contra_goapp.CONTRAGO_DB.contra_go_fill_form_gui_db import contractHistoryInsert


template = os.path.join(
    os.path.dirname(__file__), "assets", "ContraGO_ContractEstimate.docx"
)


document = MailMerge(template)


def ContraGO_Estimate_Module():
    
    
    
    def submitForm():

        """submitForm()

        Args:
          N/A

        Output:
          .docx editable file
        """

        final_estimate = str(int(matCost.get()) + int(demoCost.get()) + int(laborCost.get()))

        document.merge(
            # Contractor Information
            ContractorName="Daniel Ordonez",
            ContractorPhoneNumber="(408)-630-5230",
            ContractorAddress="1330 N Nascom Ave",
            CurrentDate="11/28/21",
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
            EstimateTotal=str(final_estimate),
        )
        
        document.write(str(clientAdd.get() + clientName.get()) + "ESTIMATE.docx")
        
        
        contractHistoryInsert(clientName.get(), 
                             clientPhoneN.get(), 
                             clientAdd.get(), 
                             clientCity.get(), 
                             clientZip.get(),
                             clientState.get(), 
                             "Bob", 
                             str(clientAdd.get() + clientName.get()) + "ESTIMATE.docx")
        
        
        

    
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
    
        

    global window
    window = Tk()
    

    """ 
    Tkinter Window Dimensions 
    """ 
    window.title("Contra GO - Contract Maker")
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
        fill="#808080",
        outline="")
    
    canvas.create_rectangle(
        36.0,
        197.0,
        452.0,
        715.0,
        fill="#808080",
        outline="")
    


    
    """ 
    Tkinter GUI Entry Fields 
    Entry Fields: 
        
    """
    #endDate Entry & Label
    endDate = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    endDate.place(
        x=604.0,
        y=683.0,
        width=144.0,
        height=28.0
    )
    
    canvas.create_text(
        519.0,
        686.0,
        anchor="nw",
        text="End Date:\n",
        fill="#000000",
        font=("Coda Regular", 16 * -1)
    )
    
    
    #startDate Entry & Label
    startDate = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    startDate.place(
        x=604.0,
        y=634.0,
        width=144.0,
        height=28.0
    )
    
    canvas.create_text(
        512.0,
        641.0,
        anchor="nw",
        text="Start Date:\n",
        fill="#000000",
        font=("Coda Regular", 16 * -1)
    )
    
    
    
    
    #demoCost Entry & Label
    demoCost = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    demoCost.place(
        x=750.0,
        y=559.0,
        width=144.0,
        height=28.0
    )
    
    canvas.create_text(
        761.0,
        536.0,
        anchor="nw",
        text="Demolition Cost:",
        fill="#000000",
        font=("Coda Regular", 16 * -1)
    )
    
       
    
    #laborCost Entry & Label
    laborCost = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    laborCost.place(
        x=927.0,
        y=559.0,
        width=144.0,
        height=28.0
    )
    
    canvas.create_text(
        957.0,
        536.0,
        anchor="nw",
        text="Labor Cost:",
        fill="#000000",
        font=("Coda Regular", 16 * -1)
    )
    
    
    
    #matCost Entry & Label
    matCost = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    matCost.place(
        x=573.0,
        y=559.0,
        width=144.0,
        height=28.0
    )
    
    canvas.create_text(
        595.0,
        536.0,
        anchor="nw",
        text="Material Cost:",
        fill="#000000",
        font=("Coda Regular", 16 * -1)
    )
    
    
    
    #jobDes Entry & Label
    jobDes = Text(
        bd=0,
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
        font=("Coda Regular", 16 * -1)
    )
    
       
    
    #jobType Entry & Label
    jobType = Entry(
        bd=0,
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
        font=("Coda Regular", 16 * -1)
    )
    
    
    
    

    #clientPhoneN Entry & Label
    clientPhoneN = Entry(
        bd=0,
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
        font=("Coda Regular", 16 * -1)
    )
    
    
    
    #clientState Entry & Label
    clientState = Entry(
        bd=0,
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
        font=("Coda Regular", 16 * -1)
    )
    
    
    #clientZip Entry & Label
    clientZip = Entry(
        bd=0,
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
        font=("Coda Regular", 16 * -1)
    )
    
    
    #clientCity Entry & Label
    clientCity = Entry(
        bd=0,
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
        font=("Coda Regular", 16 * -1)
    )
    
    
    #clientAdd Entry & Label
    clientAdd = Entry(
        bd=0,
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
        font=("Coda Regular", 16 * -1)
    )
    
    
    #clientName Entry & Label
    clientName = Entry(
        bd=0,
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
        font=("Coda Regular", 16 * -1)
    )
    
    
    
    
    
    """ 
    Tkinter GUI Buttons
    Buttons: 
        Generate 
        Clear
        Back 
    """ 
    
    
    clearBttn = Button(
        font=('ArialNarrow 10 bold'),
        bg="#C8CDFF",
        text="Clear",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: clearFields(),
        relief="flat"
    )
    clearBttn.place(
        x=981.0,
        y=648.0,
        width=130.0,
        height=50.0
    )
    
    
    
    #Generate Button
    genBttn = Button(
        font=('ArialNarrow 10 bold'),
        bg="#C8CDFF",
        text="Generate",
        borderwidth=1,
        highlightthickness=2,
        highlightcolor="black",
        command=lambda: submitForm(),
        relief="flat"
    )
    genBttn.place(
        x=824.0,
        y=648.0,
        width=130.0,
        height=50.0
    )
    
    
    
    #Back Button
    backBttn = Button(
        font=('ArialNarrow 10 bold'),
        bg="#C8CDFF",
        text="Back",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print('hello'),
        relief="flat"
    )
    backBttn.place(
        x=14.0,
        y=8.0,
        width=62.0,
        height=46.0
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
        font=("CodaCaption ExtraBold", 25 * -1)
    )
    
    canvas.create_rectangle(
        0.0,
        0.0,
        1440.0,
        62.0,
        fill="#E8DBBF",
        outline="")
    
    canvas.create_text(
        90.0,
        3.0,
        anchor="nw",
        text="Contract Maker",
        fill="#000000",
        font=("ArialNarrow 10 bold", 50 * -1)
    )
    
    canvas.create_text(
        628.0,
        100.0,
        anchor="nw",
        text="Contractor Measurements",
        fill="#441B00",
        font=("CodaCaption ExtraBold", 25 * -1)
    )
    

    
    window.resizable(False, False)
    window.mainloop()


if __name__ == "__main__":
    ContraGO_Estimate_Module()
