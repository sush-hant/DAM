import mysql.connector
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password',
)

#prepare cursor object
cursorObject = dataBase.cursor()

cursorObject.execute("Use demoJoin")
cursorObject.execute("select * from Location_LU")
print("Database")