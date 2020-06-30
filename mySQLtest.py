import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user='lairning',
                                  password='Pocosi12!',
                                  host='173.249.37.119')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

mycursor = cnx.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)