# we can use the any url in @app.route 


from flask import Flask,request 
import mysql.connector 
from flask_cors import CORS 

app=Flask(__name__)
CORS(app)

@app.route('/Xerox-reg',methods=['POST'])

def reg():
    name=request.json['name']
    loc=request.json['loc']
    rno=request.json['rno']

    con=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='group'
    )
    mycursor=con.cursor()
    query="INSERT INTO `student` VALUES ('{}','{}','{}')".format(name,loc,rno)

    mycursor.execute(query)
    con.commit()
    return str(mycursor.rowcount)+ 'inserted'

if __name__=='__main__':
    app.run()


