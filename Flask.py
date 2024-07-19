# REST is implimented here useing https protocol


from flask import Flask
from flask import request
a=Flask(__name__)

@a.route("/")    #It is APP routeing means binding a-->#It is  type of decorator funtion 
def merafun():
    return "<h1>Hello_Sir &#128512; <h1>"

@a.route("/<number>")
def fun(number):
    number=int(number)
    return f"\U0001F601 Your Entered Numbers Squre is:{number**2}  \U0001F609"

@a.route("/GET")   #in get request --> ?a='value' is writen in url
def func():
    data=request.args.get('a')   
    return "Your Get request is :{}".format(data)


if __name__=="__main__":
    a.run(host="0.0.0.0")





