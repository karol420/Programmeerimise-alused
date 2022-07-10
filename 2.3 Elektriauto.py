#elektriauto
vahemaa = int(input("Sisesta, mitu kilomeetrit aku järgi veel sõita saab: "))


from random import *
juhuslik = randint(0, 1)

if juhuslik == 0:

    if vahemaa < 120:
        print("Võiksime laadida enne sõitma hakkamist.")
            
    elif vahemaa == 186:
        print("Jõuame kenasti Tartusse.")

    elif vahemaa > 186:
        print("Jõuame kenasti Tartusse.")
    
    elif vahemaa == 120:
        print("Mäo ristis võiks peatuse teha ja pisut laadida.")

    elif vahemaa < 186 or vahemaa > 120:
        print("Mäo ristis võiks peatuse teha ja pisut laadida.")