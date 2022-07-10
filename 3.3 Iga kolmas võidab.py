arv = int(input("Sisestage limonaadipudelite arv: "))

from random import *

i = 0
limonaade = 0

while i < arv:
    
    juhuslik = randint(1, 3)
    
    if juhuslik == 3:
        print("Osteti limonaad, millega võideti uus limonaad!")
        limonaade += 1
    
    else:
        print("Osteti limonaad.")
        
    i += 1
    
sum = 0
sum += limonaade