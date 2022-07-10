from datetime import *
today = (datetime.now().day)
õpilased = []

failiinput = (input("Sisestage failinimi: "))
fail = open(failiinput)

with open(failiinput) as fail:
    for rida in fail:
        rida = rida.strip()
        õpilased.append(rida)

õpilane = õpilased[today-1]
print("Vastama tuleb " + (õpilane))