from pymongo import MongoClient
import psycopg2

client = MongoClient(port=27017)


def getConnection():  #
    conn = psycopg2.connect(
        host="localhost",
        database="huwebshop",
        user="postgres",
        password="Theredslime123")
    return conn


def insert(ids, bu_id, segment, pre_rec, viewed, conn):
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO profiles (id, bu_id, segment, previously_recommended, viewed_before) VALUES(%s, %s, %s, %s, %s)
            """, (ids, bu_id, segment, pre_rec, viewed))
        conn.commit()
    print("INSERTED ", ids, bu_id, segment, pre_rec, viewed)

with client:

    db = client.huwebshop

    profiles = db.profiles.find()
    profiles_recommendations = db.profiles.find({}, {'recommendations': 1, 'previously_recommended': 1, 'buids': 1})

    for profile in profiles_recommendations:
        try:
            if profile['buids']:
                ids = (str(profile['_id']))
                if profile['recommendations']:
                    for rec_type, value in profile['recommendations'].items():
                        if rec_type == 'segment':
                            segment = value
                        if rec_type == 'viewed_before':
                            viewed = value
                else:
                    segment = 'NULL'
                    viewed = 'NULL'
                bu_id = profile['buids']
                if profile['previously_recommended']:
                    pre_rec = profile['previously_recommended']
                else:
                    pre_rec = []

                insert(ids, bu_id, segment, pre_rec, viewed, getConnection())

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)