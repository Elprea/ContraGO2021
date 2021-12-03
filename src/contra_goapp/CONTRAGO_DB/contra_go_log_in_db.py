import sqlite3

__author__ = "DanO"
__copyright__ = "DanO"
__license__ = "MIT"



class CGO_LOG_IN_DB: 
    
    
    def connect():

        conn = sqlite3.connect("ContraG0User.db")

        cursor = conn.cursor()


        cursor.execute("""
                       CREATE TABlE IF NOT EXISTS ContraG0_UInformation ( 
                           username text, 
                           password text
                           )""")

        conn.commit()

        conn.close()
    
    
    


    
 
    def registerUser(username, password): 
       
        conn = sqlite3.connect('ContraG0User.db')
        
        cursor = conn.cursor() 

        cursor.execute("INSERT INTO ContraG0_UInformation VALUES (:username, :password)",
                       {
                           'username': username.get(),
                           'password': password.get()
    
                   }
              
                )
        cursor.execute(""" SELECT * FROM ContraG0_UInformation """)
    
        data = cursor.fetchall ()

        # print the rows
        for row in data :
            print(row[1])
            print(row[0])
            conn.commit() 

        conn.close()
    

    def validationUser(username, password): 
    
        conn = sqlite3.connect('ContraG0User.db')

        cursor = conn.cursor() 
      
        cursor.execute("SELECT username from ContraG0_UInformation WHERE username= :username AND Password = :password",
                       {
                           'username': username.get(),
                           'password': password.get()
        
                   }
              
                )
    
        if not cursor.fetchone():  
           print("Login failed")
        else:
            print("Welcome")    