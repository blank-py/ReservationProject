# File Name: config.py
# Original Author: Jesse Malinen/blank-py
# Description: config for database etc

class Config:
    DEBUG = False
    
    client = pymongo.MongoClient("mongodb+srv://<SUPERUSER>:<VITTUSAATANS>@cluster0.tng3e.mongodb.net/<ReservationApp>?retryWrites=true&w=majority")
    db = client.test

