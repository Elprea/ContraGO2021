""" ContraGO Form Fill Out Database Program

This program will provide the database for the fill form GUI program 
that allows user to create and view contracts tied to their account. 

  Typical usage example:

  
"""

import sqlite3

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
                       contractorName text
                       )""")

    conn.commit()

    conn.close()




 
def contractHistoryInsert(clientName, clientPhoneNumber, clientAddress, clientCity, clientZipcode, clientState, contractorName, contractName): 
    
    """ContraGOContractHistory(clientName, clientPhoneNumber, 
                            clientAddress, clientCity, clientZipcode, 
                            clientState, contractorName, contractName)
    
    Inserts new tuple to database for a new contract and client information 

    Args:
      clientName: A string value 
      clientAddress: A string value 
      clientCity: A string value
      clientZipcode: A string value
      clientState: A string value 
      contractorName: A string value
      contractName: A string value


    """
   
    conn = sqlite3.connect('ContraGO_Contract_History.db')
    
    
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
                       contractName text
                       )""")

    cursor.execute("INSERT INTO ContraGOContractHistory VALUES (:clientName, :clientPhoneNumber, :clientAddress, :clientCity, :clientZipcode, :clientState, :contractorName, :contractName)",
                   {
                       'clientName': clientName,
                       'clientPhoneNumber': clientPhoneNumber,
                       'clientAddress': clientAddress,
                       'clientCity': clientCity,
                       'clientZipcode': clientZipcode,
                       'clientState': clientState,
                       'contractorName': contractorName,
                       'contractName': contractName 

               }
          
            )
    
    conn.close()

