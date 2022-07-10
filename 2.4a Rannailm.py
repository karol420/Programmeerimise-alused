temp = int(input("Sisestage välistemperatuur: "))
päike = str(input("Kas päike paistab? "))
lipp = str(input("Kas rannas lehvib roheline lipp? "))

if temp >= 20 and päike == "jah" or lipp == "jah":
    print("Võid minna randa!")

elif temp < 20 and päike == "ei" or lipp == "ei":
    print("Täna ei tasu randa minna.")
        