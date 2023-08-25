import sqlite3
import json
import matplotlib.pyplot as plt

conn = sqlite3.connect('pyadina-24-08-23.db')
cursor = conn.execute("SELECT json FROM orders where date > '16.08.2023'")
rows = cursor.fetchall()

de_eint = 0
de_scharf = 0
de_vegi = 0
plaettli = 0
PRICE_PER_PIADINA = 12
PLAETTLI_PRICE = 19

for j in rows:
    jsn = json.loads(j[0])
    de_eint = de_eint + jsn['0']
    de_scharf = de_scharf + jsn['1']
    de_vegi = de_vegi + jsn['2']
    if '3' in jsn:
        plaettli = plaettli + jsn['3']

print("de Eint: {cnt}".format(cnt=de_eint))
print("de Scharf: {cnt}".format(cnt=de_scharf))
print("de Vegi: {cnt}".format(cnt=de_vegi))
print("Plättli: {cnt}".format(cnt=plaettli))

total = de_eint + de_scharf + de_vegi
print("Total {cnt}".format(cnt=total))
print("Umsatz: {cnt:.2f} CHF".format(cnt=(total * PRICE_PER_PIADINA + plaettli * PLAETTLI_PRICE)))

x = ['De Eint', 'De Scharf', 'De Vegi', 'Plättli']
y = [de_eint, de_scharf, de_vegi, plaettli]

fig, br = plt.subplots()
br.grid(zorder=0)
br.bar(x, y, color=['lightgreen', 'limegreen', 'mediumseagreen', 'mediumspringgreen'], zorder=3)

text = fig.text(.5,
                .02,
                "De Eint: {de_eint} | De Scharf: {de_scharf} | De Vegi: {de_vegi} | Plättli: {plaettli}\n Total Piadina: {total} - Total Plättli: {total_plaettli}  - Umsatz: {umsatz} CHF"
                .format(de_eint=de_eint,
                        de_scharf=de_scharf,
                        de_vegi=de_vegi,
                        plaettli=plaettli,
                        total=total,
                        total_plaettli=plaettli,
                        umsatz=(total * PRICE_PER_PIADINA + plaettli * PLAETTLI_PRICE)),
                horizontalalignment='center', wrap=True)
fig.tight_layout(rect=(0, .05, 1, 1))
plt.show()
