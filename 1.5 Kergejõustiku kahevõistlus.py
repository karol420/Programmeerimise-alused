jooksutulemus = float(input("Sisesta 100 meetri jooksu tulemus: "))
kaugushuppetulemus = int(input("Sisesta kaugushüppe tulemus: "))

a = 25.4347
b = 18
c = 1.81

jooks = int(a * (b - jooksutulemus) ** c)


d = 0.14354
e = 220
f = 1.4

kaugushupe = int(d * (kaugushuppetulemus - e) ** f)

print(jooks + kaugushupe)