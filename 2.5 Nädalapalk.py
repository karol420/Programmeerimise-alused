#praktikum

töötunnid = int(input("Sisestage töötundide arv nädalas: "))
tunnitasu = int(input("Sisestage tavaline tunnitasu: "))

if töötunnid <= 40:
    palk = töötunnid * tunnitasu
    print(palk)
    
elif töötunnid > 40:
    palk = (töötunnid * tunnitasu)
    lisapalk = ((töötunnid - 40) * tunnitasu * 0.5)
    print (int(palk + lisapalk))