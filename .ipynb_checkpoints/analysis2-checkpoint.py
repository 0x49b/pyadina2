import sqlite3
import json
import matplotlib.pyplot as plt
import pandas as pd

conn = sqlite3.connect('pyadina-24-08-23.db')
cursor = conn.execute("select distinct date from orders")
dat = cursor.fetchall()
print(dat)

de_eint_x = []
de_eint = 0
de_scharf_x = []
de_scharf = 0
de_vegi_x = []
de_vegi = 0
y = []

for d in dat:
    sql = "SELECT * FROM orders where date='{d}'".format(d=d[0])
    cursor = conn.execute(sql)
    rows = cursor.fetchall()
    print(rows)

    for row in rows:
        jsn = json.loads(row[5])
        de_eint = de_eint + jsn['0']
        de_scharf = de_scharf + jsn['1']
        de_vegi = de_vegi + jsn['2']

        de_eint_x.append(de_eint)
        de_scharf_x.append(de_scharf)
        de_vegi_x.append(de_vegi)
        y.append(row[6])

    print(de_eint_x)
    print(de_scharf_x)
    print(de_vegi_x)
    print(y)

df = pd.DataFrame({
    'period':y,
    'de_eint': de_eint_x,
    'de_scharf': de_scharf_x,
    'de_vegi': de_vegi_x
})

# plot individual lines
plt.plot(df['de_eint'], label='De Eint')
plt.plot(df['de_scharf'], label='De Scharf')
plt.plot(df['de_vegi'], label='De Vegi')

plt.legend()
plt.title('Summarized Piadina Sales per Type', fontsize=16)

# display plot
plt.show()




