
# 1.insert the data into mysql

import mysql.connector

con=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='group'
)
mycursor=con.cursor()
query="INSERT INTO `student`(`name`, `loc`, `rno`) VALUES ('Raveena','mumbai',25)"

mycursor.execute(query)
con.commit()
print(mycursor.rowcount,'inserted')