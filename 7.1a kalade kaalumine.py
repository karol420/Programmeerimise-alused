def kala_kaal(pikkus, indeks):
    return round(pikkus ** 3 * indeks / 100)
failinimi = input("Sisesta failinimi: ")
alammõõt = int(input("Sisesta püügi alammõõt: "))
tüsedusindeks = float(input("Sisesta Fultoni tüsedusindeks: "))

fail = open(failinimi, encoding = "UTF-8")

kaalud = []

for rida in fail:
    rida = int(rida)
    if rida < alammõõt:
        print("kala lasti vette tagasi.")
    else:
        kaal = kala_kaal(rida, tüsedusindeks)
        print("Püütad kala on kääluga ", kaal, " grammi.")
        kaalud.append(kaal)
fail.close()

raskeim = round(max(kaalud) / 1000, 3)
print(raskeim)