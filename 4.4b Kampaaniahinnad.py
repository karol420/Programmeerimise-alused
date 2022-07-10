alghinnad = input("Sisesta alghinnad: ")
hiljem = alghinnad.split(",")
hinnakordaja = [0.8, 0.3, 0.2, 0.5, 0.95]

i = 0
number = 1

for el in hiljem:
    arv = int(hiljem[i])
    kampaaniahind = float(arv) * hinnakordaja[i]
    print(str(number) + ". toote alghind: " + str(arv) + ", kampaaniahind: " + str(kampaaniahind))
    i += 1
    number += 1