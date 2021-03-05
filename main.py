from pymongo import MongoClient
from postgres import insert

client = MongoClient(port=27017)

with client:

    db = client.huwebshop

    sessions = db.sessions.find({}, {'buid': 1, 'segment': 1})

    for i in sessions:
        try:
            try:
                if i['buid']:
                    insert(i['buid'], i['segment'])
            except KeyError:
                insert(i['buid'], i['segment'])
        except:
            print('error')