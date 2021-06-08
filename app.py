from flask import Flask,jsonify,request
app=Flask(__name__)


#Creating an array of each tasks
@app.route("/")
def hello_world():
    return "Hello World"


if (__name__=='__name__'):
    app.run(debug=True)
