# %%
import mysql.connector

# %%
mydb= mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Pass@123456789")
mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM xyz.datascience")
for i in mycursor.fetchall():
    print(i)

# %%
mydb.close()
# import mysql.connector
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="abc",
#     password="password"
# )
# print(mydb)
# mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)

# %%

