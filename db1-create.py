import os
import psycopg2

DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a nccuacct-angels').read()[:-1]
#DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()
SQL_order = '''CREATE TABLE permanent_comments(
   id serial PRIMARY KEY,
   user_id VARCHAR (50) NOT NULL,
   comment VARCHAR NOT NULL
);'''
cursor.execute(SQL_order)
conn.commit()
cursor.close()
conn.close()