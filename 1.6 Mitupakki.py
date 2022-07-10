laius = int(input("Mitu küpsist on tordi laius? "))
pikkus = int(input("Aga pikkus? "))
korrused = int(input("Mitmekorruselist torti soovid? "))
ükspakk = int(input("Mitu küpsist on ühes pakis?"))

print("Vaja läheb " + str(laius * pikkus * korrused) + " küpsist.")

mitupakki = laius * pikkus * korrused / ükspakk

import math

print (math.ceil (mitupakki))