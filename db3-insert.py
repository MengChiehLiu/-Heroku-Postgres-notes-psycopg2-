import os
import psycopg2

DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a nccuacct-angels').read()[:-1]
#DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

record = ("UID", f"""your comment""")
table_columns = '(user_id, comment)'
postgres_insert_query = f"""INSERT INTO temp_comments {table_columns} VALUES (%s, %s);"""
cursor.execute(postgres_insert_query, record)
conn.commit()
cursor.close()
conn.close()