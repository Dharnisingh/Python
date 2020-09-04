# Python program to connect 
# to mysql databse 
  
  
import mysql.connector 
  
  
# Connecting from the server 
conn = mysql.connector.connect(user = 'root',
                               password = 'password',
                               host = 'localhost', 
                              database = 'my_db') 
  
print(conn) 

#Creating table
Cursor = conn.cursor()

Cursor.execute("CREATE DATABASE College")
print("College Data base is created")
# Disconnecting from the server 
conn.close() 
