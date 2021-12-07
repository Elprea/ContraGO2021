""" ContraGO Form Fill Out Datbase Program

This program will run tkinter GUI program that will allow the user to
fill out entry fields of the GUI and click on submit button to create a
new .docx file that will outputed for the contractor to use

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

    cursor.execute(
        """
                   CREATE TABlE IF NOT EXISTS ContraG0ContractHistory (
                       username text,
                       password text
                       )"""
    )

    conn.commit()

    conn.close()


def contractHistoryInsert(
    clientName,
    clientPhoneNumber,
    clientAddress,
    clientCity,
    clientZipcode,
    clientState,
    contractorName,
):

    """registerUser(username, password)

    Inserts new tuple to database for new registered user

    Args:
      username: A string value for username
      password: A string value for password


    """

    conn = sqlite3.connect("ContraG0_Contract_History.db")

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO ContraG0ContractHistory VALUES (:clientName, :clientPhoneNumber, :clientAddress, :clientCity, :clientZipcode, :clientState, :contractorName)",
        {
            "clientName": clientName.get(),
            "clientPhoneNumber": clientPhoneNumber.get(),
            "clientAddress": clientName.get(),
            "clientCity": clientPhoneNumber.get(),
            "clientZipcode": clientName.get(),
            "clientState": clientPhoneNumber.get(),
            "contractorName": clientName.get(),
        },
    )

    cursor.execute(""" SELECT * FROM ContraG0_UInformation """)

    data = cursor.fetchall()

    # print the rows
    for row in data:
        print(row[1])
        print(row[0])
        conn.commit()

    conn.close()
