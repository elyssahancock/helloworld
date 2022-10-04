
# Assignment requirements.
"""Your software must demonstrate 
the ability to insert, modify, delete,
 and retrieve (or query) data."""

# Basic Imports.
from select import select
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

def main():

    # Set up.
    db_json_file =  "take 3/food-inventory-6cbfd-firebase-adminsdk-zjecw-9714286f35.json"
    cred = credentials.Certificate(db_json_file)
    firebase_admin.initialize_app(cred)

    db = firestore.client()


    
    collection_name = "Pantry" 
    
    # Timestamps:
    """
    Stored as: 
    DatetimeWithNanoseconds(2022, 9, 29, 22, 36, 6, 661000, tzinfo=datetime.timezone.utc)
    DatetimeWithNanoseconds(year, month, day, militaryHour + 6, minutes, seconds, nanoseconds )
    """
    # Trial of Expiration date
    # db.collection(collection_name).add({"expiration": datetime.datetime(2022, 10, 7)})

    """# Get all documents in a collection
    docs = db.collection(collection_name).get()
    for doc in docs:
        print(doc.to_dict()) """

    selection = getInput()
    while selection != 0:    
        print(selection)

        if selection == 1:
            addItem(collection_name, db)
        if selection == 2:
            deleteItem(collection_name, db)
        if selection == 4:
            displayItems(collection_name, db)
        
        selection = getInput()
        

""" # Querying
    print("Query")
    # only adding documents that meet the where clause to the list
    docs = db.collection(collection_name).where("name", "==", "Bob").get()
        # Looping through the list of documents in the collection
    for doc in docs:
        print(doc.to_dict())
        """

# ✅
def getInput():
    # Menu.
    
    print("Menu:")
    print("(0) Quit")
    print("(1) Add Item")
    print("(2) Delete Item")
    print("(3) Edit Item")
    print("(4) Display all items")
    selection = int(input("-- "))
    return selection

# ✅
def addItem(collection_name, db):

    # Get item.
    item_name = input("Item: ")
    
    # Get expiration.
    print("Expiration date")
    date = input("Date: MM/DD/YYYY  ")
    date_items = date.split("/")
    month = int(date_items[0])
    day = int(date_items[1])
    year = int(date_items[2])

    expiration = datetime.datetime(year, month, day)
    db.collection(collection_name).document(item_name).add({"item": item_name, "expirationDate": expiration})

# ✅ - until ordering is done
def displayItems(collection_name, db):

    
    docs = db.collection(collection_name).get()
    print("\n\n\nYour items are:")
    for doc in docs:
        dictionary = doc.to_dict()
        print(f"  * {dictionary['item']}")
        expiration_date = dictionary["expirationDate"]
        print(f"  - - {expiration_date}")
        #   print(convertTimestamp(expiration_date))
    print("\n\n")


# 🅿️
def convertTimestamp(expiration_date):
    """0022-09-30 00:00:00+00:00 is passed in"""

    date2_0 = datetime.fromtimestamp(expiration_date)
    """
    ExpDate_string = str(expiration_date)
    year = int(ExpDate_string[0:5])
    month = ExpDate_string[6:8]
    if month[0] == "0":
        month = month[1]
    month = int(month)
    day = ExpDate_string[9:11]
    converted_string = (f" ")
    """
    print(date2_0)


# 🅿️
def deleteItem(collection_name, db):
    item_name = input("Item to be deleted: ")
    docs = db.collection(collection_name).where("item", "==", item_name).get()
    for doc in docs:
        #db.collection(collection_name).document(doc).delete()
        print(doc)
### Cloud Messaging -> notifacations to operating system 

# ❌
def orderByDateTime():
    None
main()