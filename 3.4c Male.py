#male

taisarv = int(input("Sisestage täisarv: "))
ruudud = taisarv

i = 0

while taisarv > 0:
    if i == 0:
        i = i + 1
        taisarv = taisarv - 1
    else:
        i *= 2
        taisarv = taisarv - 1

print("Nisuteri " + str(ruudud) + ". ruudu eest: " + str(i))