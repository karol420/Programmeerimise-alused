from datetime import datetime

kuupäev_kellaeg = datetime.today()


fail = open("pank.txt", "r")

valik = ("Tehing, väljavõte või lõpetamine?: ")

while valik != "lõpp":
    
    valik  = input("Tehing, väljavõte või lõpetamine?: ")
    
    if valik == "tehing":
        summa = int(input("Sisesta summa: "))
        fail = open("pank.txt", "a")
        fail.write("\n" + "Tehingu aeg: " + str(kuupäev_kellaeg) + ", summa: " + str(summa))
        fail.close()
    
    elif valik == "väljavõte":
        fail = open("pank.txt", "r")
        loetud = fail.read()
        print(loetud)