import mysql.connector
import os

def getMysqlData(name):
    myconnection = os.getenv['cnx']
    cursor = myconnection.cursor()
    if name:
        query = "select * from Employee where First_Name like '%{}%'".format(name)

    else:
        query = "select * from Employee"
    cursor.execute(query)
    results = cursor.fetchall()
    list1 = []
    for items in results:
        finaldict = {'First_Name': items[1], 'Last_Name': items[2], 'Age': items[3]}
        list1.append(finaldict)

    return list1
