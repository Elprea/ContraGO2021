""" ContraGO Log In Database Program

This program will perform user validation for entered credentials, includes 
username and password. This program performs registration of the user to 
register to an account. 

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
    conn = sqlite3.connect("ContraGOUser.db")

    cursor = conn.cursor()
    

    cursor.execute(
        """
                   CREATE TABlE IF NOT EXISTS ContraGO_UInformation (
                       username text,
                       password text,
                       userFirstName text, 
                       userLastName text,
                       userAddress text,
                       userCity text,
                       userState text, 
                       userZipcode text, 
                       userPhoneNumber text, 
                       userEmailAddress text  
                       )"""
    )

    conn.commit()

    conn.close()



def validationUser(username, password):

    """validationUser(username, password)

    Validates tuple in database if user credential are valid

    Args:
      username: A string value for username
      password: A string value for password


    """

    conn = sqlite3.connect("ContraGOUser.db")

    cursor = conn.cursor()
    
    cursor.execute(
        """
                   CREATE TABlE IF NOT EXISTS ContraGO_UInformation (
                       username text,
                       password text,
                       userFirstName text, 
                       userLastName text,
                       userAddress text,
                       userCity text,
                       userState text, 
                       userZipcode text, 
                       userPhoneNumber text, 
                       userEmailAddress text
                       )"""
    )

    cursor.execute(
        "SELECT * from ContraGO_UInformation WHERE username= :username AND password = :password",{
            "username": username, 
            "password": password
        },
    )
    
    if cursor.fetchone():
        # Correct credentials 
        return 0
        

    else:
        # Incorrect credentials 
        return 1
    
    conn.commit()
    conn.close()