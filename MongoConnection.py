import pymongo
import json
import requests
from Shelter import Shelter


class MongoConnection():

    def __init__(self):
        self.DB = self.create_connection()

    def create_connection(self):
        client = pymongo.MongoClient("mongodb+srv://m220student:m220password@cluster0-ktqos.mongodb.net/test?retryWrites=true&w=majority")
        db = client.ShelterDB
        return db

    def fetch_data(self):
        read = requests.get("https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/8a6eceb2-821b-4961-a29d-758f3087732d/resource/9e807dc6-061e-4fcc-9586-d9403274246b/download/daily-shelter-occupancy-2017-json.json")
        # read = requests.get("https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/8a6eceb2-821b-4961-a29d-758f3087732d/resource/50a46bfd-937f-400f-aa8f-be1c0abac19f/download/daily-shelter-occupancy-2018-json.json")
        # read = requests.get("https://secure.toronto.ca/c3api_data/v2/DataAccess.svc/ssha/extractssha?$format=application/json;odata.metadata=none&unwrap=true&$top=100000&$select=OCCUPANCY_DATE,ORGANIZATION_NAME,SHELTER_NAME,SHELTER_ADDRESS,SHELTER_CITY,SHELTER_PROVINCE,SHELTER_POSTAL_CODE,FACILITY_NAME,PROGRAM_NAME,SECTOR,OCCUPANCY,CAPACITY&$orderby=OCCUPANCY_DATE,ORGANIZATION_NAME,SHELTER_NAME,FACILITY_NAME,PROGRAM_NAME")
        # print(read.json())
        records_of_data  = read.json()
        # record_list =[]
        # for record in records_of_data:
        #     single_record = Shelter(record['SHELTER_NAME'],record['CAPACITY'],record['PROGRAM_NAME'],record['ORGANIZATION_NAME'],record['SECTOR'],record['FACILITY_NAME'],record['OCCUPANCY'],record['OCCUPANCY_DATE'],record['SHELTER_PROVINCE'],record['SHELTER_CITY'],record['SHELTER_ADDRESS'],record['SHELTER_POSTAL_CODE'])
        #     record_list.append(single_record)

        # obj1 = record_list[0]
        # print(obj1)
        # print(obj1.SHELTER_NAME)
        # print(obj1.CAPACITY)
        collection_mytb = self.DB.Shelter
        result = collection_mytb.insert_many(records_of_data)

    def get_all_record(self):
        records = self.DB.Shelter.find({},{'_id':0})
        list_records = list(records)
        return json.dumps(list_records)
    
    def insert_new_record(self,single_data):
        collection_mytb = self.DB.Shelter
        result =  collection_mytb.insert(single_data)
        return result



#MongoConnection().get_all_record()

# new_record = {}
# new_record['SHELTER_NAME'] = ''
# new_record['CAPACITY'] =''

# MongoConnection().insert_new_record(new_record)
# MongoConnection().fetch_data()