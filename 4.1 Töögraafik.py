#töögraafik

fail = open("töögraafik.txt", encoding="UTF-8")
rida = fail.readlines()
töötajad = []

with open("töögraafik.txt") as fail:
    for rida in fail:
        rida = rida.strip()
        töötajad.append(rida)

päev = int(input("Sisestage, mis kuupäeva töötajat soovite: "))
tööt = töötajad[päev-1]
print(str(päev) + ". kuupäeval töötab " + str(tööt))