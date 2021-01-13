import mysql.connector
mydb=mysql.connector.connect(host="localhost" , user="root", passwd="root")

print(mydb)

if (mydb):
    print("Sucess")
else:
    Print("Fail")
mycursor=mydb.cursor()
mycursor.execute("show databases")
for x in mycursor:
  print(x)