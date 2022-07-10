from easygui import *

print("Tere, mis on teie küsimus?: ")
küsimus = enterbox("Teie küsimus?: ")

if "ilm" in küsimus:
    msgbox("Õues on täna ilus ilm. ")
elif "nimi" in küsimus:
    msgbox("Minu nimi on ...")
elif "vanus" in küsimus:
    msgbox("Olen 420 aastat vana. ")
else:
    msgbox("Kahjuks ei oska vastata.")