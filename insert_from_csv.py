from collections import namedtuple
import csv
import datetime
import mysql.connector

file_name='python_mysql_test_data.csv'

EmployeeRecord = namedtuple('EmployeeRecord', 'first_name, last_name, hire_date, gender, birth_date')

add_employee = ("INSERT INTO employees "
                "(first_name, last_name, hire_date, gender, birth_date) "
                "VALUES (%s, %s, %s, %s, %s)")

def convertDate(date_):
    month, day, year = date_.split("/")
    return datetime.date(int(year), int(month), int(day))

cnx = mysql.connector.connect(user='add', database='test')
cursor = cnx.cursor()

for rec in map(EmployeeRecord._make, csv.reader(open(file_name, "r"))):
    converted_rec = (rec.first_name, rec.last_name, convertDate(rec.hire_date),
                     rec.gender, convertDate(rec.birth_date))
    cursor.execute(add_employee, converted_rec)

cnx.commit()
cursor.close()
cnx.close()