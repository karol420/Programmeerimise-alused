def pronksikarva_summa(fail):
    fail = open(failin, encoding="UTF-8")
    rahad = []
    for rida in fail:
        rida = int(rida)
        if (rida) <= 5:
            rahad += [(rida)]
    summa = sum(rahad)
    fail.close()
    return summa

failin = input("Sisestage faili nimi: ")
print(pronksikarva_summa(failin))