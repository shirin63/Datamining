import os
import json
import requests
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

# create the flask object
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")    
    
client = MongoClient('mongodb+srv://m220student:<password>@cluster0-ktqos.mongodb.net/test?retryWrites=true&w=majority')
db = client.test
r = requests.get("https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/8a6eceb2-821b-4961-a29d-758f3087732d/resource/9e807dc6-061e-4fcc-9586-d9403274246b/download/daily-shelter-occupancy-2017-json.json")
collection = db['shelter']
data=r.json()
if __name__ == "__main__":
    app.run(debug=True)
    