from math import *

def invest(kaardimaksesumma):
    mikroinvesteeringusumma = round(ceil(kaardimaksesumma) - kaardimaksesumma, 2)
    return mikroinvesteeringusumma

failinimi = input("Sisestage failinimi: ")
fail = open(failinimi, "r")

kaardimaksesumma = []

for rida in fail:
    kaardimaksesumma.append(float(rida.strip()))

summa = 0

for el in kaardimaksesumma:
    
    if (invest(el)) > 0:
        print(invest(el))
        summa += invest(el)
    
    else:
        print("investeeringut ei tehta.")

print("Investeeringute kogusumma: " + str(summa))

