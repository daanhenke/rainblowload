import pymongo
import hashlib

import base95

client = pymongo.MongoClient("localhost")
database = client["rainbow"]
tables = database["tables"]

mines = tables.find()

list = []
amountToPush = 857374

if mines.count() == 0:
    current = 0
else:
    last = mines.sort("id", -1).limit(1)
    for value in last:
        current = value["id"] + 1

print("STARTED WORKING FROM " + str(current))

while True:
    plaintext = base95.encode(current)
    mine = {
        "id": current,
        "plaintext": plaintext,
        "sha1": hashlib.sha1(plaintext).hexdigest() #,
        #"sha256": hashlib.sha256(plaintext).hexdigest(),
        #"sha512": hashlib.sha512(plaintext).hexdigest()
    }

    list.append(mine)

    if len(list) >= amountToPush:
        print("Pushed " + base95.encode(current - amountToPush + 1) + " til " + plaintext)
        tables.insert(list)
        list = []

    current += 1
