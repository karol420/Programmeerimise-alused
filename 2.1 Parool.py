parool = str(input("Sisestage parool: "))
pikkus = len(parool)

if pikkus < 8:
    print("Parool ei sobi.")
elif pikkus > 8:
    print("Parool sobib.")
elif pikkus == 8:
    print("Parool sobib.")