import os
import psycopg2

DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a nccuacct-angels').read()[:-1]

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()
user_id="Uda3c85da6e156dddabf31b0e4d49d510"
cursor.execute("DELETE FROM account WHERE user_id = '%s';" %user_id)
conn.commit()
cursor.close()
conn.close()
'''
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()
sql = "delete from temp_comments;"
cur.execute(sql)
conn.commit()
cur.close()
conn.close()
'''
