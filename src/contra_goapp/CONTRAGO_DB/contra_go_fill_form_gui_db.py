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




 
def contractHistoryInsert(clientName, clientPhoneNumber, clientAddress, clientCity, clientZipcode, clientState, contractorName): 
    
    """ContraGOContractHistory(clientName, clientPhoneNumber, 
                            clientAddress, clientCity, clientZipcode, 
                            clientState, contractorName)
    
    Inserts new tuple to database for new registered user

    Args:
      clientName: A string value 
      clientAddress: A string value 


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
                       contractorName text
                       )""")

    cursor.execute("INSERT INTO ContraGOContractHistory VALUES (:clientName, :clientPhoneNumber, :clientAddress, :clientCity, :clientZipcode, :clientState, :contractorName)",
                   {
                       'clientName': clientName,
                       'clientPhoneNumber': clientPhoneNumber,
                       'clientAddress': clientAddress,
                       'clientCity': clientCity,
                       'clientZipcode': clientZipcode,
                       'clientState': clientState,
                       'contractorName': contractorName

               }
          
            )

    cursor.execute(""" SELECT * FROM ContraGOContractHistory """)

    data = cursor.fetchall ()

    # print the rows
    for row in data :
        print(row[1])
        print(row[0])
        conn.commit() 

    conn.close()

