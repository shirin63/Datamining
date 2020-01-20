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

# create the flask object
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/FormSubmit", methods=['POST'])
def receive_form_data():
    print(request.form.get('SHELTER_NAME'))
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")    
    

if __name__ == "__main__":
    app.run(debug=True)
    