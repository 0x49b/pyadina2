import sqlite3
import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

conn = sqlite3.connect('pyadina-20-08-23.db')
cursor = conn.execute("SELECT json FROM orders where date > '16.08.2023'")
rows = cursor.fetchall()

de_eint = 0
de_scharf = 0
de_vegi = 0
PRICE_PER_PIADINA = 12

for j in rows:
    jsn = json.loads(j[0])
    de_eint = de_eint + jsn['0']
    de_scharf = de_scharf + jsn['1']
    de_vegi = de_vegi + jsn['2']

print("de Eint: {cnt}".format(cnt=de_eint))
print("de Scharf: {cnt}".format(cnt=de_scharf))
print("de Vegi: {cnt}".format(cnt=de_vegi))
total = de_eint + de_scharf + de_vegi
print("Total {cnt}".format(cnt=total))
print("Umsatz: {cnt:.2f} CHF".format(cnt=(total * PRICE_PER_PIADINA)))

x = ['De Eint', 'De Scharf', 'De Vegi']
y = [de_eint, de_scharf, de_vegi]

fig, br = plt.subplots()
br.grid(zorder=0)
br.bar(x, y, color=['lightgreen', 'limegreen', 'mediumseagreen'], zorder=3)

text = fig.text(.5,
                .02,
                "De Eint: {de_eint} | De Scharf: {de_scharf} | De Vegi: {de_vegi} \n Total: {total}  - Umsatz: {umsatz} CHF"
                .format(de_eint=de_eint,
                        de_scharf=de_scharf,
                        de_vegi=de_vegi,
                        total=total,
                        umsatz=total * PRICE_PER_PIADINA),
                horizontalalignment='center', wrap=True)
fig.tight_layout(rect=(0, .05, 1, 1))
plt.show()
