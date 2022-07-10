istekoht = str(input('Kas soovite istekohta ise valida ("ise") või loosida ("loos")? '))

from random import *

if istekoht == "ise":
    kuskohas = str(input('Kas soovite istuda akna ääres ("aken") või mitte ("muu")? '))
    if kuskohas == "aken":
        print("Valisite ise. Aknakoht.")
    elif kuskohas == "muu":
        print("Valisite ise. Vahekäigukoht.")


elif istekoht == "loos":
    koht = randint(1, 3)
    if koht == 1:
        print("Istekoht loositi. Aknakoht.")
    else:
        print("Istekoht loositi. Vahekäigukoht.")