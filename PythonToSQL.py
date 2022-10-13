#GitHub: ayoamrit

#import library to connect python to mySQL
import mysql.connector


#creating a function
def sqlConnection():
    
    try:
        
        #Enter all of your mysql servers detial inside quotation marks.
        mydb = mysql.connector.Connect(
            
        #If you are running your database on the same server as your application your hostname is going to be "localhost"   
        host='HostName',
        user='UserName',
        password='Your_Password',
        database='Database_Name')
        
        #Cursor is used to execute the SQL statements in python.
        myCursor = mydb.cursor()
        
        #Execute compiles SQL statement.
        myCursor.execute("show tables")
        
        #using for loop to display the result of above SQL statement.
        for x in myCursor:
            print(x)
        
        
    #In the case of an error
    except Exception:
        print("An error occurred")
        
        
#calling the function
sqlConnection()