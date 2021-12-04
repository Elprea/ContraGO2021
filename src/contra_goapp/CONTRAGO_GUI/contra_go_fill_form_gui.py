""" ContraGO Form Fill Out Program 

This program will run tkinter GUI program that will allow the user to 
fill out entry fields of the GUI and click on submit button to create a 
new .docx file that will outputed for the contractor to use

  Typical usage example:

  
"""
from __future__ import print_function

from tkinter import Tk, Canvas, Entry, Text, Button

from mailmerge import MailMerge

import os
cwd=os.getcwd()
template = "\\assets\\ContraGO_ContractEstimate.docx"
path=cwd+template
document = MailMerge(path)


def ContraGO_Estimate_Module(): 
    
    def submitForm():
        
        """submitForm()
    
        Args:
          N/A
    
        Output:
          .docx editable file 
        """
        
        final_estimate = str(int(entry_2.get()) + int(entry_3.get()) + int(entry_4.get())  + int(entry_5.get()))
        
        document.merge(
            
            #Contractor Information 
            ContractorName='Daniel Ordonez',
            ContractorPhoneNumber='(408)-630-5230',
            ContractorAddress='1330 N Nascom Ave',
            CurrentDate='11/28/21',
            
            
            #Client Information
            ClientAddress=entry_7.get(),
            ClientName=entry_1.get(),
            ClientPhoneNumber=entry_11.get(),
            City=entry_8.get(),
            ClientState=entry_10.get(),
            ZipCode=entry_9.get(),
            
            
            #Job Information 
            JobDescription=entry_6.get(),
            MaterialCost=entry_2.get(),
            GutterCost=entry_3.get(),
            DemolitionCost=entry_4.get(),
            LaborCost=entry_5.get(),
            EstimateTotal=final_estimate)
    
    
        document.write('Roofing_ESTIMATE.docx')
    
    
    
    
    # Initilizing new tkinter root object 
    # Creating window of 1440x1024 dimensions 
    window = Tk()
    
    window.geometry("1440x1024")
    
    window.configure(bg = "#FFFFFF")
    
    
    # GUI Canvas & Placement
    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 1024,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    
    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1440.0,
        1024.0,
        fill="#AEC0FF",
        outline="")
    
    canvas.create_rectangle(
        0.0,
        0.0,
        1440.0,
        74.0,
        fill="#6A79FD",
        outline="")
    
    canvas.create_rectangle(
        21.0,
        138.0,
        529.0,
        1005.0,
        fill="#6A79FD",
        outline="")
    
    canvas.create_rectangle(
        21.0,
        84.0,
        395.0,
        129.0,
        fill="#6A79FD",
        outline="")
    
    canvas.create_rectangle(
        598.0,
        84.0,
        972.0,
        129.0,
        fill="#6A79FD",
        outline="")
    
    canvas.create_rectangle(
        598.0,
        138.0,
        1420.0,
        1005.0,
        fill="#6A79FD",
        outline="")
    
    
    
    # Entry_1 Label And Entry Field
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_1.place(
        x=80.0,
        y=205.0,
        width=356.0,
        height=34.0
    )
    
    canvas.create_text(
        64.0,
        161.0,
        anchor="nw",
        text="Client Name",
        fill="#000000",
        font=("AplikaziaMFW Bold", 24 * -1)
    )
    
    
    
    # Entry_2 Label And Entry Field
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_2.place(
        x=622.0,
        y=645.0,
        width=181.0,
        height=37.0
    )
    
    canvas.create_text(
        622.0,
        595.0,
        anchor="nw",
        text="Material Cost",
        fill="#000000",
        font=("AplikaziaMFW Bold", 24 * -1)
    )
    
    
    
    
    # Entry_3 Label And Entry Field
    entry_3 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_3.place(
        x=622.0,
        y=766.0,
        width=181.0,
        height=37.0
    )
    
    canvas.create_text(
        622.0,
        716.0,
        anchor="nw",
        text="Gutter Cost",
        fill="#000000",
        font=("AplikaziaMFW Bold", 24 * -1)
    )
    
    
    
    # Entry_4 Label And Entry Field
    entry_4 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_4.place(
        x=857.0,
        y=645.0,
        width=181.0,
        height=37.0
    )
    
    canvas.create_text(
        857.0,
        595.0,
        anchor="nw",
        text="Demolition Cost",
        fill="#000000",
        font=("AplikaziaMFW Bold", 24 * -1)
    )
    
    
    
    
    # Entry_5 Label And Entry Field
    entry_5 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_5.place(
        x=1093.0,
        y=645.0,
        width=181.0,
        height=37.0
    )
    
    canvas.create_text(
        1093.0,
        595.0,
        anchor="nw",
        text="Labor Cost",
        fill="#000000",
        font=("AplikaziaMFW Bold", 24 * -1)
    )
    
    
    
    # Entry_6 Label And Entry Field
    entry_6 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_6.place(
        x=622.0,
        y=205.0,
        width=773.0,
        height=373.0
    )
    
    canvas.create_text(
        622.0,
        160.0,
        anchor="nw",
        text="Job Description",
        fill="#000000",
        font=("AplikaziaMFW Bold", 24 * -1)
    )
    
    
    
    # GUI Canvas & Placement
    canvas.create_text(
        34.0,
        93.0,
        anchor="nw",
        text="Client & Contractor Details",
        fill="#000000",
        font=("AplikaziaMFW Bold", 24 * -1)
    )
    
    canvas.create_text(
        607.0,
        93.0,
        anchor="nw",
        text="Contractor Measurements",
        fill="#000000",
        font=("AplikaziaMFW Bold", 24 * -1)
    )
    
    
    
    # Entry_7 Label And Entry Field
    entry_7 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_7.place(
        x=75.0,
        y=309.0,
        width=361.0,
        height=39.0
    )
    
    canvas.create_text(
        59.0,
        259.0,
        anchor="nw",
        text="Client Address",
        fill="#000000",
        font=("AplikaziaMFW Bold", 24 * -1)
    )
    
    
    
    # Entry_8 Label And Entry Field
    entry_8 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_8.place(
        x=75.0,
        y=428.0,
        width=361.0,
        height=39.0
    )
    
    canvas.create_text(
        59.0,
        378.0,
        anchor="nw",
        text="Client City",
        fill="#000000",
        font=("AplikaziaMFW Bold", 24 * -1)
    )
    
    
    
    # Entry_9 Label And Entry Field
    entry_9 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_9.place(
        x=75.0,
        y=554.0,
        width=361.0,
        height=39.0
    )
    
    canvas.create_text(
        59.0,
        504.0,
        anchor="nw",
        text="Client Zipcode",
        fill="#000000",
        font=("AplikaziaMFW Bold", 24 * -1)
    )
    
    
    
    # Entry_10 Label And Entry Field
    entry_10 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_10.place(
        x=75.0,
        y=663.0,
        width=361.0,
        height=39.0
    )
    
    canvas.create_text(
        59.0,
        613.0,
        anchor="nw",
        text="Client State",
        fill="#000000",
        font=("AplikaziaMFW Bold", 24 * -1)
    )
    
    
    
    # Entry_11 Label And Entry Field
    entry_11 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_11.place(
        x=73.0,
        y=772.0,
        width=361.0,
        height=39.0
    )
    
    canvas.create_text(
        57.0,
        722.0,
        anchor="nw",
        text="Client Phone Number",
        fill="#000000",
        font=("AplikaziaMFW Bold", 24 * -1)
    )
    
    canvas.create_text(
        21.0,
        10.0,
        anchor="nw",
        text="Contract Making ",
        fill="#000000",
        font=("AplikaziaMFW Bold", 50 * -1)
    )
    
    
    
    # Submit Button 
    button_1 = Button(
        text="Submit",
        borderwidth=0,
        highlightthickness=0,
        command=submitForm,
        relief="flat"
    )
    button_1.place(
        x=622.0,
        y=881.0,
        width=237.0,
        height=63.0
    )
    
    canvas.create_text(
        625.0,
        206.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("AplikaziaMFW Bold", 36 * -1)
    )
    
    
    window.resizable(False, False)
    window.mainloop()


if __name__ == "__main__":
    ContraGO_Estimate_Module()