
from cmath import inf
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("jsonFile.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

import datetime


db.collection("Fruit").add({"name": "banana", "color": "yellow"})



db.collection("Collection Name")
  #.add({"document1(aka an attribute)": "key value pair aka data",
 #"document2": "data"}
def main():
    information_list = []
    item = input("What is the item? ")
    information_list.append(item)
    experation_date = input("When is the expiration date? ")
    information_list.append(experation_date)
    addFoodInfo("Food", information_list)

def addFoodInfo(CollectionName, informationList):
    item = informationList[0]
    expiration = informationList[1]
    db.collection(CollectionName).add({"item": item, "expirationDate": expiration})

def test_datetime_stuff():
    now = datetime.datetime.now()
    print(now)
    print(type(now))

test_datetime_stuff()




# get rid of brackets when you use a lost
number = [1, 2, 3, 4, 5, 6, 7]
print(str(numbers)[1:-1])