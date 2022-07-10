#asendaja

fail = str(input("Sisestage failinimi: "))
failiavaja = open(fail)

faililugeja = failiavaja.read()

faililugeja = faililugeja.replace("8", "ö")
faililugeja = faililugeja.replace("2", "ä")
faililugeja = faililugeja.replace("6", "õ")
faililugeja = faililugeja.replace("y", "ü")

print(faililugeja)