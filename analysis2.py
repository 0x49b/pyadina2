import sqlite3
import json
import matplotlib.pyplot as plt

conn = sqlite3.connect('pyadina-24-08-23.db')
cursor = conn.execute("select distinct date from orders")
dat = cursor.fetchall()
print(dat)

for d in dat:
    sql = "SELECT * FROM orders where date='{d}'".format(d=d[0])
    cursor = conn.execute(sql)
    rows = cursor.fetchall()
    print(rows)
