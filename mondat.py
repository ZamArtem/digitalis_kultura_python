print("1. feladat")

mondat = input("Add meg a mondatot! ")
szamlalo = 0
for betu in mondat:
  if betu.isalpha():
    szamlalo = szamlalo + 1


print("")
print("2. feladat")
print(f"A mondatban előforduló betűk száma: {szamlalo}.")

print("")
print("3. feladat")
print(f"A szavak száma: {len(mondat.split())}")

print("")
print("4. feladat")

maganhangzok = ["a","á","o","ó","u","ú","e","é","i","í","ö","ő","ü","ű"]
szamlalo = 0
for betu in mondat:
  if betu.lower() in maganhangzok:
    szamlalo += 1

print(f"A mondatban előforduló magánhangzók száma: {szamlalo}.")

print("")
print("5. feladat")
leghosszabb = 0
szavak = mondat.split()

for szo in szavak:
  if len(szo) > leghosszabb:
    leghosszabb = len(szo)

print(f"A leghosszabb szó a(z) leghosszabb {leghosszabb} betűből áll.")
print("6.feladat")
bekeres = input("Add meg a keresett szót! ")

for szo in szavak:
  if bekeres == szo:
    print("A keresett szó előfordul a mondatban.")
    break
  else:
    print("A keresett szó nem fordul elő a mondatban.")
    break

