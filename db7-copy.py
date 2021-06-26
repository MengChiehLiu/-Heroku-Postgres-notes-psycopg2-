import os
import psycopg2

DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a nccuacct-angels').read()[:-1]
#DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()
cursor.execute(f"""INSERT INTO permanent_comments  SELECT * FROM temp_comments;""")
conn.commit()
cursor.close()
conn.close()