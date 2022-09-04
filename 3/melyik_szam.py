import random
print("Egy számot kell kitalálnod 1 és az általad megadott felső határéték között.")


bekeres = int(input("Add meg a határértéket! "))
gep_kitalalt_szama = random.randint(1,bekeres)
print(gep_kitalalt_szama)
print()

counter = 0
while True:
  if counter == 0:
    gondolat = int(input("Melyik számra gondoltam? "))
  if counter > 0:
    gondolat = int(input("Melyik számra gondoltam? (kilépés: -1) "))
  if gep_kitalalt_szama != gondolat:
    if gondolat < gep_kitalalt_szama and gondolat != -1:
      counter += 1
      print("Sajnos nem talált")
      print("Nagyobb számra gondoltam!")
      print()
    if gondolat > gep_kitalalt_szama and gondolat != -1:
      counter += 1
      print("Sajnos nem talált")
      print("Kissebb számra gondoltam!")
      print()
  if gondolat == -1:
    print(f"Sajnálom! A kitalálandó szám a  {gep_kitalalt_szama} volt.")
    break
  if gondolat == gep_kitalalt_szama:
    print(f"Eltaláltad {counter} próbálkozásból!")
    break
