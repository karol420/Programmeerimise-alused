import math

inimesed = int(input("Sisestage inimeste arv: "))
kohad = int(input("Sisestage kohtade arv: "))

mitubussi = math.ceil(inimesed/kohad)
viimane = inimesed % kohad

if viimane == 0:
    viimane = kohad
    
print("Busse on vaja: " + str(mitubussi))
print("Viimases bussis inimesi " + str(viimane))