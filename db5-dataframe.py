import os
import psycopg2
import pandas as pd

DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a nccuacct-angels').read()[:-1]

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
sql = "select * from account;"
dat = pd.read_sql_query(sql, conn)
conn = None

print(dat)
#print("U55cce311c3805b9fa42f53867bd5d88d" in dat["user_id"].tolist())