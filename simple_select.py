import mysql.connector
import datetime

cnx = mysql.connector.connect(user='add', database='test')

cursor = cnx.cursor()

query = ("SELECT first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s and %s")

hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(2019, 12, 31)

cursor.execute(query, (hire_start, hire_end))

for (first_name, last_name, hire_date) in cursor:
    print(type(first_name), type(hire_date))
    print("{}, {} was hired on {:%d %b %Y}".format(last_name, first_name, hire_end))

cursor.close()
cnx.close()