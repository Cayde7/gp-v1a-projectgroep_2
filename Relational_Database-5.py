import psycopg2


def getConnection():  # https://www.postgresqltutorial.com/postgresql-python/connect/
    conn = psycopg2.connect(
        host="localhost",
        database="huwebshop",
        user="postgres",
        password="Theredslime123")
    return conn


def executeSQL(sqlString):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        conn = getConnection()
        cur = conn.cursor()
        cur.execute(sqlString)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database edition done')


# Creeert de tabellen voor de database

products = """
CREATE TABLE products
(
    id character varying(25) NOT NULL,
    brand character varying(50),
    category character varying(50),
    sub_category character varying(50),
    sub_sub_category character varying(50),
    sub_sub_sub_category character varying(50),
    price integer NOT NULL,
    gender character varying(20),
    fast_mover boolean,
    herhaalaankopen boolean,
    name character varying(150),
    discount character varying(25),
    doelgroep character varying(25),
    PRIMARY KEY (id)
);"""

sessions = """
CREATE TABLE sessions
(
    bu_id character varying(500)[] NOT NULL,
    segment character varying(50),
    PRIMARY KEY (bu_id)
);"""

profiles = """
CREATE TABLE profiles
(
    id character varying(80) NOT NULL,
    bu_id character varying(500)[] NOT NULL,
    segment character varying(80),
    previously_recommended character varying(500)[],
    viewed_before character varying(500)[],
    PRIMARY KEY (id)
);"""

orders = """
CREATE TABLE orders
(
    sessions_bu_id character varying(500)[] NOT NULL,
    products_id character varying (25) NOT NULL
);
"""

foreign_key1 = """ALTER TABLE profiles
    ADD FOREIGN KEY (bu_id)
    REFERENCES public.sessions (bu_id)
    NOT VALID;"""

foreign_key2 = """ALTER TABLE orders
    ADD FOREIGN KEY (sessions_bu_id)
    REFERENCES public.sessions (bu_id)
    NOT VALID;"""

foreign_key3 = """ALTER TABLE orders
    ADD FOREIGN KEY (products_id)
    REFERENCES public.products (id)
    NOT VALID;"""

executeSQL("""DROP TABLE products CASCADE """)
executeSQL("""DROP TABLE orders CASCADE""")
executeSQL("""DROP TABLE profiles CASCADE""")
executeSQL("""DROP TABLE sessions CASCADE""")
executeSQL(profiles)
executeSQL(products)
executeSQL(sessions)
executeSQL(orders)
executeSQL(foreign_key1)
executeSQL(foreign_key2)
executeSQL(foreign_key3)