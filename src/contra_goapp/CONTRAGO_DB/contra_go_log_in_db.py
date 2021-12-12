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
                       password text
                       )"""
    )

    conn.commit()

    conn.close()


def registerUser(username, password):

    """registerUser(username, password)

    Inserts new tuple to database for new registered user

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
                       password text
                       )"""
    )

    cursor.execute(
        "INSERT INTO ContraGO_UInformation VALUES (:username, :password)",
        {"username": username, "password": password},
    )

    cursor.execute(""" SELECT * FROM ContraGO_UInformation """)

    data = cursor.fetchall()

    # print the rows
    for row in data:
        print(row[1])
        print(row[0])
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
                       password text
                       )"""
    )

    cursor.execute(
        "SELECT username from ContraGO_UInformation WHERE username= :username AND Password = :password",
        {"username": username, "password": password},
    )
    
    
    if not cursor.fetchone():
        # Incorrect credentials 
        return 0
        

    else:
        # Correct credentials 
        return 1
    cursor.commit()