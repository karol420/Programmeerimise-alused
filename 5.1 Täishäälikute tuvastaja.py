#täishäälikud
def täishäälikud(sõna):
    kokku = 0
    täishäälikute_järjend = set("aeiouõäöü")
    for täht in sõna:
        if täht in täishäälikute_järjend:
            kokku += 1
    return(kokku)

sona = input("Sisesta sõna: ")




print("Sõnas " + (sona) + " on kokku " + str(täishäälikud(sona)) + " täishäälikut.")
