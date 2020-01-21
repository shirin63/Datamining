import os
import json
import dns
import time
import datetime
from datetime import datetime
from flask import Flask, render_template, url_for
#import bson import BSON
#import bson import json_util
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask import request
from MongoConnection import MongoConnection

# create the flask object
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/FormSubmit", methods=['POST'])
def receive_form_data():
    # print(request.mimetype)
    # print(request.json)
    data = request.get_json(force=True)
    result = MongoConnection().insert_new_record(data)
    return result

@app.route("/getAllData", methods=['GET'])
def getAllData():
    return MongoConnection().get_all_record()

@app.route("/view_data")
def view_data():
    return render_template("view_data.html")    
    

if __name__ == "__main__":
    app.run(debug=True)
    