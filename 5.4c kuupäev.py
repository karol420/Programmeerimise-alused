def kuu_nimi(järjekorranumber):
    järjekorranumber = int(järjekorranumber)
    kuud = ["jaanuar",
            "veebruar",
            "märts",
            "aprill",
            "mai",
            "juuni",
            "juuli",
            "august",
            "september",
            "oktoober",
            "november",
            "detsember"]
    return kuud[järjekorranumber - 1]

def kuupäev_sõnena(kp):
    kuuosa = kp.split(".")
    return kuuosa[0] + ". " + kuu_nimi(kuuosa[1]) + " " + kuuosa[2] + ". a"

kuupäev = input("Sisestage kuupäev kujul PP.KK.AAAA: ")
print(kuupäev_sõnena(kuupäev))