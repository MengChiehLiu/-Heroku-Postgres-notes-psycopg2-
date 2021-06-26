import os
import psycopg2

DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a nccuacct-angels').read()[:-1]

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

username = '原本的名字'
postgres_update_query = f"""UPDATE account SET username = '新的名字' WHERE username = %s"""

cursor.execute(postgres_update_query, (username,))
conn.commit()

count = cursor.rowcount

print(count, "Record updated successfully into alpaca_training")

