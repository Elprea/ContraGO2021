""" ContraGO Form Fill Out Program 

This program will run tkinter GUI program that will allow the user to 
fill out entry fields of the GUI and click on submit button to create a 
new .docx file that will outputed for the contractor to use

  Typical usage example:

  
"""
from __future__ import print_function

from tkinter import Tk, Canvas, Entry, Text, Button

from mailmerge import MailMerge

template = "C:\\Users\\danie\\OneDrive\\Desktop\\ContractGODOCX\\ContraGO_ContractEstimate.docx"

document = MailMerge(template)


def ContraGO_Estimate_Module(): 
    
    def submitForm():
        
        """submitForm()
    
        Args:
          N/A
    
        Output:
          .docx editable file 
        """
        
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
            DemolitionCost=entry_4.get(),
            MaterialCost=entry_2.get(),
            LaborCost=entry_5.get(),
            GutterCost=entry_3.get(),
            EstimateTotal='40000')
    
    
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
    