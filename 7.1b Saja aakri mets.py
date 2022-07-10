def juurdekasv(pindala, kasv):
    kasv_kokku = pindala * 0.4047 * kasv
    return round(kasv_kokku, 2)

failinimi = input("Sisestage failinimi: ")
fail = open(failinimi)

pindalad = []

for rida in fail:
    pindalad.append(float(rida.strip()))

fail.close()

kasv = float(input("Sisestage aastane juurdekasv hektari kohta tihumeetrites: "))
piir = float(input("Sisestage piir, mitmest aakrist suuremad metsatükid arvesse võtta: " ))

kokku = 0
for el in pindalad:
    if el > piir:
        print("Metsatüki aastane juurdekasv on: " + str(juurdekasv(el, kasv)))
        kokku += 1
    else:
        print("Metsatükki ei võeta arvesse.")

print("Arvutati " + str(kokku) + " metsatüki juurdekasv.")