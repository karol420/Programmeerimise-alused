#palindroomid

sõnad = []

sona = ("Sisesta sõna: ")

while sona != "lõpp":
    sona = input("Sisesta sõna: ")
    sõnad.append(sona)

for sona in sõnad:
    if sona == sona[::-1]:
        print((sona.capitalize()) + " on palindroom.")
    
    elif sona == "lõpp":
        break
    
    else:
        print((sona.capitalize()) + " ei ole palindroom. ")