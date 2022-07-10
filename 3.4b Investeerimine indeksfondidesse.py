#investeerimine

invsumma = float(input("Sisestage summa, mida soovid investeerida: "))
aastad = int(input("Sisestage aastates, kaua soovid investeerida: "))
tootlus = float(input("Sisestage oodatav iga-aastane tootlus: "))

for i in range(aastad):
    invsumma = invsumma + ((invsumma * tootlus)/100)

print("{:.2f}".format(round(invsumma, 2)))
    