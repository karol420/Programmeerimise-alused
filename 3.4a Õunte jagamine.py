#kolmaspraks

from random import *

pöialpoisid = int(input("Mitu pöialpoissi tahab õunu? "))

pöialpoisid >= 0 and pöialpoisid <= 7

i = 0
kokku = 0

while i < pöialpoisid:
    juhuslik = randint(1, 2)
    print(juhuslik)
    kokku += juhuslik
    i += 1

summa = 14 - kokku

print("Lumivalgekesele jäi " + str(summa) + " õuna.")
