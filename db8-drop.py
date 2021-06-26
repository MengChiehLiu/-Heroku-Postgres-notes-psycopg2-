import os
import psycopg2

DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a nccuacct-angels').read()[:-1]

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

drop_table_query = '''DROP TABLE IF EXISTS temp_comments'''

cursor.execute(drop_table_query)
conn.commit()
cursor.close()
conn.close()
print("drop success")