lista = ['F5.3', 'NF1', 'F3.2', 'NF0.6', 'NF0', 'F2.1', 'NF2']
hossz = []
for karakter in lista:
  if karakter[0] == "F":
    hossz.append(float(karakter[1:]))
  else:
    hossz.append(float(karakter[2:]))
print("2. feladat")
print(f"A verseny távja {sum(hossz)} km volt.")
print()
print("3. feladat")
futott = False
if lista[-1][0:2] == "NF":
  pass
else:
  futott = True
if futott:
  print("Futva ért célba")
else:
  print("Gyalogolva ért célba")
print()
counter = 0
print("4. feladat")
for szam in lista:
  if szam == "NF0":
    counter += 1
    
print(f"A verseny során {counter} alkalommal állt meg.")
print()
print("5. feladat")
tarolo = ""
megszakitas = 0
for karakter in lista:
  if karakter[0] == "F":
    tarolo = karakter[0]
  if karakter[0] == "N" and tarolo == "F":
    tarolo = karakter[0]
    megszakitas += 1

print(f"A futását {megszakitas} alkalommal szakította meg.") 
print()
print("6. feladat")

volt_e = False
tarolo = ""
for karakter in lista:
  if karakter == "NF0" and tarolo[:2] == "NF":
    volt_e = True
  tarolo = karakter


print(volt_e)
