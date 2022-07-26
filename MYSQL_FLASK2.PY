# create a regiration by using Json

from flask import Flask,request 

app=Flask(__name__)

@app.route('/Raveena-reg',methods=['POST'])

def reg():

    name=request.json['name']
    loc=request.json['loc']
    rno=request.json['rno']

    return 'my name is {} my loc is {} my rno is {} '.format(name,loc,rno)

if __name__=='__main__':
    app.run()
