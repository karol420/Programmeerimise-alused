from datetime import datetime
kuupäev_kellaeg = datetime.today()
failinimi = str(input("Sisestage logifaili nimi: "))
failiavaja = open(failinimi)
valik = str(input("Kas tahate logisse kirjutada (kirjuta) või lugeda (loe)?: "))

if valik == "loe":
    loetud = failiavaja.read()
    print("Kuupäev ja kellaaeg: " + str(kuupäev_kellaeg) + "\n" + loetud)

else:
    sissekanne = input("Sisesta sissekande tekst: ")
    failiavaja = open(failinimi, "a")
    failiavaja.write(str(kuupäev_kellaeg) + "\n" + sissekanne)
    failiavaja.close()

