from flask import Flask,render_template ,request , jsonify

#it is a flask aplication instance
app=Flask(__name__)



#this is for routing the home_page
@app.route("/",methods=["GET","POST"])      
def home_page():
    return render_template("index.html")


@app.route("/math",methods=["POST"])
def calculate():
    if (request.method=="POST"):
        ops=(request.form["operation"])
        n1=int(request.form["num1"])
        n2=int(request.form["num2"])
        
        if ops=="add":
            result= f"Your answer is \U0001F609 :{n1+n2}"  
        if ops=="subtract":
            result= f"Your answer of subtraction is \U0001F609:{n1-n2}"        
        if ops=="multiply":
            result= f"Your answer of multiply is \U0001F609:{n1*n2}"
        if ops=="divide":
            result= f"Your answer of divide is \U0001F609:{n1/n2}"
        if ops=="Squre":
            result= f"Your answer of Squre is \U0001F609:{n1**n2}"
        # elif n1== None or n2==None:
        #     result="Please enter a valid number \U0001F601"
        return render_template("results.html",result=result)


@app.route("/POSTMAN",methods=["POST"])
def calculates():
    if (request.method=="POST"):
        # data extraction by json request
        ops=(request.json["operation"])
        n1=int(request.json["num1"])
        n2=int(request.json["num2"])
        
        if ops=="add":
            result= f"Your answer is \U0001F609 :{n1+n2}"  
        if ops=="subtract":
            result= f"Your answer of subtraction is \U0001F609:{n1-n2}"        
        if ops=="multiply":
            result= f"Your answer of multiply is \U0001F609:{n1*n2}"
        if ops=="divide":
            result= f"Your answer of divide is \U0001F609:{n1/n2}"
        if ops=="x^n":
            result= f"Your answer of n1^n2 is \U0001F609:{n1**n2}"
        return jsonify(result)


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
#The host="0.0.0.0" parameter makes the application accessible from any network interface