import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="atts"
)

mycursor = mydb.cursor()

sql = "DROP TABLE customers"

mycursor.execute(sql)