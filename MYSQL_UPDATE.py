# update the query on sql 

import mysql.connector

con=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='group'
)
mycursor=con.cursor()
query="UPDATE `student` SET `loc`='Akluj',`rno`=500 WHERE `name`='AQWTREPO'"
#UPDATE `student` SET `name`='[value-1]',`loc`='[value-2]',`rno`='[value-3]' WHERE 1
mycursor.execute(query)
con.commit()
print(mycursor.rowcount,'updated')
