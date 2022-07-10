#sissetulekud

fail = open("konto.txt", encoding ="UTF-8")
sissetulek = []

for rida in fail:
    sissetulek = float(rida)
    if sissetulek > 0:
        print(sissetulek)

