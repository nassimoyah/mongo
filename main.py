import pymongo 
from dotenv import load_dotenv ,find_dotenv
import os 
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())     ## BRING ENV FILE WITHOUT PASSING THE PATH ...shortcut MONGOFB_PWD    env file to store environment variables. This file contains key-value pairs in the format KEY=VALUE , with each variable on a new line. We can use libraries like python-dotenv to load the variables from the file into our Python script automatically.
password = os.environ.get("MONGOFB_PWD")


connection_string = f"mongodb+srv://nassim:{password}@nodetuts.i6qazqe.mongodb.net/?retryWrites=true&w=majority&appName=nodetuts" #to interface with mongodb 

client = MongoClient(connection_string)

dbs = client.list_database_names()   # listing db names , local , admin test 

testdb = client.test            # accessing  our db
 
collections = testdb.list_collection_names()     # listing the colllection in our db 

print(collections)                                  # printing the collections 

def insert_test_doc():                                  
    collection = testdb.test1                   # accessing to our collection 
    test_document = {
        "name": "nass",
        "type" : "test"
    }
    insertedid = collection.insert_one(test_document).inserted_id
    print(insertedid)

#insert_test_doc() 
    
production = client.production      #accessing database that does not currently exist mongo will creat it 
persons_collection = production.pr_collection # accessing collection that does not exist it will be created 
 
docs= []

def creat_documents():
    first_name = ["tim","jaso"]
    last_name = ["arduino","nafo"]
    ages = [21,40]

    for i,j in zip(first_name,last_name,ages):
        doc = {"first_name": first_name ,"last_name": last_name ,"age" : age}
        docs.append(doc)
    persons_collection.insert_many(docs)    

creat_documents()     


