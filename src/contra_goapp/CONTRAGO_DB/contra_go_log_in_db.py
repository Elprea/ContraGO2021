""" ContraGO Log In Database Program

This program will perform user validation for entered credentials, includes 
username and password. This program performs registration of the user to 
register to an account. 



"""

import sqlite3

from tkinter import ttk, messagebox

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
    

def updateUserInfo(columnName,updateChange, username):

    """updateUserInfo(columnName, updateChange, username)
    
        Makes a query to ContraGO_UInformation database to update 
        specified column (columnName), with specified data (updateChange), and
        gets the current user logged in

         Args:
             columnName: String name of cetain database column
             updateChange: String of change being made to specified column
             username: String of username to specify which account changes are being made in 

        Returns:
            N/A

        Raises:
            N/A
        """

    conn = sqlite3.connect("ContraGOUser.db")

    cursor = conn.cursor()
    
    if columnName == "username": 
      
        file = open("user.txt", "r")    
        fileread = file.read() 
        fileread = fileread.replace(username, updateChange) 
        
        file = open("user.txt", "w")  
            
        file.write(fileread)
        
        file.close()

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
    
    value =  "UPDATE ContraGO_UInformation SET " + columnName + " = " + "\"" + updateChange + "\"" +" WHERE username=" + "\"" + username + "\""
    cursor.execute(value)
    root.destroy()
    messagebox.showinfo("ContraGO - Information Update Module ","Information Updated!")
    conn.commit()
    conn.close()
    userSettings()


def userSettings():
    """userSettings()
   
    Display a treeView from all tuples in ContraGO_UInformation with only
    data from the current user

    Args:
      N/A


    """
    global root
    # Creates root tkinter object
    root = tk.Tk()
   
    root.title("ContraGO - User Infomation (User Settings")  
   
    tree = ttk.Treeview(root, column=("c1", "c2", "c3","c4", "c5", "c6","c7","c8", "c9", "c10"), show='headings')
   
    conn = sqlite3.connect("ContraGOUser.db")

    cursor = conn.cursor()
   
    connect()
   
    file1 = open("user.txt", "r")
   
    cursor.execute("SELECT * FROM ContraGO_UInformation WHERE username=" + "\"" + str(file1.readline().strip()) + "\"")
   
    file1.close()
   
    rows = cursor.fetchall()  

    for row in rows:
        tree.insert("", tk.END, values=row)        
   
    conn.commit()
   
    conn.close()
   
    # Create Treeview fields and columns (Table Dimensions)
    tree.column("#1", anchor=tk.CENTER)

    tree.heading("#1", text="Username")

    tree.column("#2", anchor=tk.CENTER)

    tree.heading("#2", text="Password")

    tree.column("#3", anchor=tk.CENTER)

    tree.heading("#3", text="First Name")

    tree.column("#4", anchor=tk.CENTER)

    tree.heading("#4", text="Last Name")

    tree.column("#5", anchor=tk.CENTER)

    tree.heading("#5", text="Address")

    tree.column("#6", anchor=tk.CENTER)

    tree.heading("#6", text="City")

    tree.column("#7", anchor=tk.CENTER)

    tree.heading("#7", text="State")
   
    tree.column("#8", anchor=tk.CENTER)

    tree.heading("#8", text="Zipcode")
   
    tree.column("#9", anchor=tk.CENTER)

    tree.heading("#9", text="Phone Number")
   
    tree.column("#10", anchor=tk.CENTER)

    tree.heading("#10", text="Email Address")
   
    tree.pack()
