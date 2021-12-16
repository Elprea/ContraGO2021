""" ContraGO Register Database Program

This program will provide the database to the register gui in order to allow
new user to register and create new accounts which will be added to the database 
of users. 

  
"""
import sqlite3


def registerUser(username, password, userFirstName, userLastName, userAddress, userCity, userState, userZipcode, userPhoneNumber, userEmailAddress):

    """registerUser(username, 
                    password, 
                    userFirstName, 
                    userLastName, 
                    userAddress, 
                    userCity, 
                    userState, 
                    userZipcode, 
                    userPhoneNumber, 
                    userEmailAddress)

    Inserts new tuple to database for new registered user

    Args:
      username: A string value 
      password: A string value 
      userFirstName: A string value 
      userLastName: A string value  
      userAddress: A string value  
      userCity: A string value 
      userState: A string value 
      userZipcode: A string value  
      userPhoneNumber: A string value  
      userEmailAddress: A string value 


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
                       )""")

    cursor.execute(
        "SELECT username from ContraGO_UInformation WHERE username= :username ",
        {
            "username": username
            
            },
    )
    
    
    if not cursor.fetchone():
        
        cursor.execute("INSERT INTO ContraGO_UInformation VALUES (:username, :password, :userFirstName, :userLastName, :userAddress, :userCity, :userState, :userZipcode, :userPhoneNumber, :userEmailAddress)",
                {
                "username": username, 
                "password": password,
                "userFirstName": userFirstName,
                "userLastName": userLastName,
                "userAddress": userAddress,
                "userCity": userCity,
                "userState": userState, 
                "userZipcode":userZipcode,
                "userPhoneNumber": userPhoneNumber,
                "userEmailAddress": userEmailAddress
                
                }
        )
        
        
    else:
        
        return 1
    
    conn.commit() 
    conn.close()
    