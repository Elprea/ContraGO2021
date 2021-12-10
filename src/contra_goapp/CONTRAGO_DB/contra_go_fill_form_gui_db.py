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
    conn = sqlite3.connect("ContraG0_Contract_History.db")

    cursor = conn.cursor()


    cursor.execute("""
                   CREATE TABlE IF NOT EXISTS ContraG0ContractHistory ( 
                       username text, 
                       password text
                       )""")

    conn.commit()

    conn.close()




 
def contractHistoryInsert(clientName, clientPhoneNumber, clientAddress, clientCity, clientZipcode, clientState, contractorName): 
    
    """contractHistoryInsert(clientName, clientPhoneNumber, 
                            clientAddress, clientCity, clientZipcode, 
                            clientState, contractorName)
    
    Inserts new tuple to database for new registered user

    Args:
      clientName: A string value 
      clientAddress: A string value 


    """
   
    conn = sqlite3.connect('ContraG0_Contract_History.db')
    
    cursor = conn.cursor()
    
    cursor.execute("""
                   CREATE TABlE IF NOT EXISTS ContraG0ContractHistory ( 
                       username text, 
                       password text
                       )""")

    cursor.execute("INSERT INTO ContraG0ContractHistory VALUES (:clientName, :clientPhoneNumber, :clientAddress, :clientCity, :clientZipcode, :clientState, :contractorName)",
                   {
                       'clientName': clientName.get(),
                       'clientPhoneNumber': clientPhoneNumber.get(),
                       'clientAddress': clientName.get(),
                       'clientCity': clientPhoneNumber.get(),
                       'clientZipcode': clientName.get(),
                       'clientState': clientPhoneNumber.get(),
                       'contractorName': clientName.get()

               }
          
            )

    cursor.execute(""" SELECT * FROM ContraG0ContractHistory """)

    data = cursor.fetchall ()

    # print the rows
    for row in data :
        print(row[1])
        print(row[0])
        conn.commit() 

    conn.close()

