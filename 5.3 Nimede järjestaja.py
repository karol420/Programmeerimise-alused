def järjestaja(a, b = False):
    nimedjärjend = sorted(a.split(", "))
    if b == True:
        nimedjärjend = list(reversed(nimedjärjend))
    for i in nimedjärjend:
        print(str(nimedjärjend.index(i) + 1) + ". " + str(i))
    return(nimedjärjend)
    

nimed = input("Sisestage nimed: ")
järjekord = input("Kas soovid nimesid ka tagurpidises tähestiku järjekorras? ")

if järjekord == "jah":
    järjestaja(nimed, True)

else:
    järjestaja(nimed)