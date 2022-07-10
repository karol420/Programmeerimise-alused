def mahlapakkide_arv(kogus):
    mahlapakkidearv =((kogus)*(0.4/3))
    return round(mahlapakkidearv)

koogus = float(input("Sisesta õunte kogus kilogrammides: "))

print(mahlapakkide_arv(koogus))