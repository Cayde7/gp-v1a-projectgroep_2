import psycopg2

con = psycopg2.connect(
    host='localhost',
    database='huwebshop',
    user='postgres',
    password='Theredslime123'
)

def insert(buid, segment):
    with con:
        cur = con.cursor();
        cur.execute('insert into sessions (bu_id, segment) values (%s, %s)', (buid, segment))
        con.commit()
        cur.close()
    print(buid, segment)
