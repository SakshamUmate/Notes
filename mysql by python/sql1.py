import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Pass@123456789"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE if NOT exists xyz.datascience (c1 INT NOT NULL AUTO_INCREMENT,c2 VARCHAR(255),c3 INT,c4 INT,PRIMARY KEY (c1))")
mydb.close()