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
#from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask import request
import requests
from MongoConnection import MongoConnection

client = MongoClient('mongodb+srv://isaicv18:kb0GMCojP5kW8SIX@cluster0-iroqa.azure.mongodb.net/test?retryWrites=true&w=majority')
db = client.test
r = requests.get("https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/8a6eceb2-821b-4961-a29d-758f3087732d/resource/9e807dc6-061e-4fcc-9586-d9403274246b/download/daily-shelter-occupancy-2017-json.json")
collection = db['shelter']
data=r.json()



# create the flask object
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/FormSubmit", methods=['POST'])
def receive_form_data():
    # print(request.mimetype)
    # print(request.json)

    shltername = request.form.get('SHELTER_NAME')
    capacity = request.form.get('CAPACITY')
    programname = request.form.get('PROGRAM_NAME')
    organizationname = request.form.get('ORGANIZATION_NAME')
    sector = request.form.get('SECTOR')
    facilityname = request.form.get('FACILITY_NAME')
    occupancy = request.form.get('OCCUPANCY') 
    occupancydate = request.form.get('OCCUPANCY_DATE')
    shelterprovince = request.form.get('SHELTER_PROVINCE')
    sheltercity = request.form.get('SHELTER_CITY')
    shelteraddress = request.form.get('SHELTER_ADDRESS')
    shelterpostalcode = request.form.get('SHELTER_POSTAL_CODE')

    #programnames = [{"PROGRAM_NAME1":programname},{"PROGRAM_NAME2":programname2}]
 
    row={"SHELTER_NAME":shltername, "CAPACITY":capacity, "PROGRAM_NAME":programname, "ORGANIZATION_NAME":organizationname,
    "SECTOR":sector, "FACILITY_NAME":facilityname, "OCCUPANCY":occupancy, "OCCUPANCY_DATE":occupancydate,
    "SHELTER_PROVINCE":shelterprovince, "SHELTER_CITY":sheltercity, "SHELTER_ADDRESS":shelteraddress, "SHELTER_POSTAL_CODE":shelterpostalcode}    
   # print("*************************************888")
    #print(shltername)
    #print(row)
    db.shelter.insert_one(row)
    return render_template("home.html")

@app.route("/getAllData", methods=['GET'])
#def getAllData():
    
    #return MongoConnection().get_all_record()

@app.route("/view_data")
def view_data():
    return render_template("view_data.html")    
    

if __name__ == "__main__":
    app.run(debug=True)
    