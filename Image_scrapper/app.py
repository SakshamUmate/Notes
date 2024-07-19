import os
import logging
from flask import Flask,jsonify,render_template,request
from flask_cors import CORS,cross_origin
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs 
import requests
import pymongo

logging.basicConfig(filename='Image_scrapper.log',level=logging.DEBUG,format='%(asctime)s %(name)s %(levelname)s %(message)s')

app=Flask(__name__)

@app.route("/",methods=["GET"])

def home_page():
    return render_template("index.html")


@app.route("/review",methods=["POST","GET"])

def results():
    if request.method=="POST":
        try:
            query= request.form["content"].replace(" ","")

            save_dir ="Image"
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            
                            # fake user agent to avoid getting blocked by Google
            header={"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"}
            
            responce=requests.get(f"https://www.google.com/search?q={query}&tbm=isch&ved=2ahUKEwigmPiI0siDAxWK-TgGHTkCDKUQ2-cCegQIABAA&oq=ais&gs_lcp=CgNpbWcQARgAMggIABCABBCxAzIFCAAQgAQyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzILCAAQgAQQsQMQgwEyBQgAEIAEMgUIABCABDoOCAAQgAQQigUQsQMQgwFQhgVY-RtgwitoAHAAeASAAZUBiAHnDJIBBDAuMTOYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABAMABAQ&sclient=img&ei=GzeZZeCeGYrz4-EPuYSwqAo&bih=756&biw=767")

            # parse the HTML using BeautifulSoup
            soap=bs(responce.content,"html.parser")
            images_tags=soap.findAll("img")
            print(len(images_tags))
            del images_tags[0]
            img_data_in_mongo=[]
            for i in images_tags:
                images_url=i["src"]
                image_data=requests.get(images_url).content
                mydict={"Image_url":images_url,"Image_data":image_data}
                img_data_in_mongo.append(mydict)
                with open(os.path.join(save_dir,f"{query}_{images_tags.index(i)}.jpg"),"wb") as f:
                    f.write(image_data)
        
            client=pymongo.MongoClient("mongodb+srv://saksham:qk70nd97a@cluster1.vucvhcs.mongodb.net/?retryWrites=true&w=majority")
            db=client["datascience"]
            collection=db["Image_Scrapper"]
            collection.insert_many(img_data_in_mongo)
            
            return " <h1>\U0001F600\U0001F44D Image laoded Successfully! \U0001F601 \U0001F44D<h1>"     
        
        except Exception as e :
            logging.error(e)
            return 'Something went wrong \U0001F647'
        
    else:
        return render_template("index.html")    


if __name__=="__main__":
    app.run(host="0.0.0.0",port=8000)
#Host:It allows the server to be reachable from outside the local machine.
#Port: (default:5000)Ports are used to differentiate between different services on the same machine. 












