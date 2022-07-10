nimi = input("Sisestage failinimi koos laiendiga: ")
fail = open(nimi)

laulud = []

tekst = "Muusikapalade valik: "

print(tekst)

järjekord = 1

for rida in fail:
    laulud.append(rida)
    print(str(järjekord) + ". " + rida)
    järjekord = järjekord + 1

fail.close()
        
mitmeslaul = int(input("Vali muusikapala number: "))
valitudlaul = laulud[mitmeslaul-1]
print("Mängitav muusikapala on " + (valitudlaul))