import mysql.connector

def getMysqlData(name):
    myconnection = mysql.connector.connect(
        host='mytestingmysqlserver.mysql.database.azure.com',
        user='chohan47@mytestingmysqlserver',
        password='Chohan443',
        database='test'
    )
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
