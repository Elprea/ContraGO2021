""" ContraGO Form Fill Out Database Program

This program will provide the database for the fill form GUI program 
that allows user to create and view contracts tied to their account. 

  
"""

import sqlite3

from tkinter import ttk

import tkinter as tk


__author__ = "DanO"
__copyright__ = "DanO"
__license__ = "MIT"



def connect():

    """connect()
    
        Args:
          N/A
    
        Output:
          .docx editable file 
        """
    conn = sqlite3.connect("ContraGOContract_History.db")

    cursor = conn.cursor()


    cursor.execute("""
                   CREATE TABlE IF NOT EXISTS ContraGOContractHistory ( 
                       clientName text, 
                       clientPhoneNumber text, 
                       clientAddress text, 
                       clientCity text, 
                       clientZipcode text, 
                       clientState text, 
                       contractorName text, 
                       estimateName text,
                       finalContractName text
                       )""")

    conn.commit()

    conn.close()




 
def contractHistoryInsert(clientName, clientPhoneNumber, clientAddress, clientCity, clientZipcode, clientState, contractorName, estimateName, finalContractName): 
    
    """ContraGOContractHistory(clientName, clientPhoneNumber, 
                            clientAddress, clientCity, clientZipcode, 
                            clientState, contractorName, estimateName, finalContractName)
    
    Inserts new tuple to database for a new contract and client information 

    Args:
      clientName: A string value 
      clientAddress: A string value 
      clientCity: A string value
      clientZipcode: A string value
      clientState: A string value 
      contractorName: A string value
      estimateName: A string value
      finalContractName: A string value


    """
    
    conn = sqlite3.connect('ContraGOContract_History.db')
    
    
    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABlE IF NOT EXISTS ContraGOContractHistory ( 
                       clientName text, 
                       clientPhoneNumber text, 
                       clientAddress text, 
                       clientCity text, 
                       clientZipcode text, 
                       clientState text, 
                       contractorName text,
                       estimateName text,
                       finalContractName text
                       )""")

    cursor.execute("INSERT INTO ContraGOContractHistory VALUES (:clientName, :clientPhoneNumber, :clientAddress, :clientCity, :clientZipcode, :clientState, :contractorName, :estimateName, :finalContractName)",
                   {
                       'clientName': clientName,
                       'clientPhoneNumber': clientPhoneNumber,
                       'clientAddress': clientAddress,
                       'clientCity': clientCity,
                       'clientZipcode': clientZipcode,
                       'clientState': clientState,
                       'contractorName': contractorName,
                       'estimateName': estimateName,
                       'finalContractName': finalContractName

               }
          
            )
    
    
    conn.commit()
    conn.close()
    
    
    
def getContractHistory():
    """getContractHistory()
    
    Retrieves all users tuple tied with their username and displays
    tuple in Treeview module 

    Args:
      N/A


    """
    # Creates root tkinter object
    root = tk.Tk() 
    
    root.title("ContraGO - Contract History")   
    
    tree = ttk.Treeview(root, column=("c1", "c2", "c3","c4", "c5", "c6","c7","c8", "c9", "c10"), show='headings')
    
    conn = sqlite3.connect("ContraGOContract_History.db")

    cursor = conn.cursor()
    
    connect()
    
    file1 = open("user.txt", "r")
    
    cursor.execute("SELECT * FROM ContraGOContractHistory WHERE contractorName=" + "\"" + str(file1.readline()) + "\"")
    
    file1.close()
    
    rows = cursor.fetchall()  

    for row in rows:
        tree.insert("", tk.END, values=row)        
    
    conn.commit() 
    
    conn.close()
    
    # Create Treeview fields and columns (Table Dimensions)
    tree.column("#1", anchor=tk.CENTER)

    tree.heading("#1", text="Client Name")

    tree.column("#2", anchor=tk.CENTER)

    tree.heading("#2", text="Client Phone Number")

    tree.column("#3", anchor=tk.CENTER)

    tree.heading("#3", text="Client Address")

    tree.column("#4", anchor=tk.CENTER)

    tree.heading("#4", text="Client City")

    tree.column("#5", anchor=tk.CENTER)

    tree.heading("#5", text="Client Zipcode")

    tree.column("#6", anchor=tk.CENTER)

    tree.heading("#6", text="Client State")

    tree.column("#7", anchor=tk.CENTER)

    tree.heading("#7", text="Contractor Name")
    
    tree.column("#8", anchor=tk.CENTER)

    tree.heading("#8", text="Estimate File Name")
    
    tree.column("#9", anchor=tk.CENTER)

    tree.heading("#9", text="Final Contract File Name")

    tree.pack()
    

