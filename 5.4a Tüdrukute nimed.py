def nimeotsing(nimedejärjend, esitäht, minpikkus):
    sobilik = []
    for osa in nimedejärjend:
        if osa[0] == esitäht.upper() and len(osa) >= minpikkus:
            sobilik.append(osa)
    return sobilik

failinimi = input("Sisestage failinimi: ")
fail = open(failinimi, encoding= "UTF-8")
nimedejärjend = []

for rida in fail:
    nimedejärjend.append(rida.strip())

esitäht = input("Sisestage nime algustäht: ")
minpikkus = int(input("Sisestage nime miniimaalne pikkus: "))
print("Sobivad ained on: " + str(nimeotsing(nimedejärjend, esitäht, minpikkus)))
