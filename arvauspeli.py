import random
arvaukset = 0
max = 100
min = 1
vastaus = random.randint(min, max)
print(vastaus)
while arvaukset < 5:
  arvaus = int(input("Anna luku väliltä 1-100: "))
  if arvaus == vastaus:
    print("----")
    print("Oikein, voitit pelin")
    print("----")
    break
  if arvaus < vastaus:
    print("----")
    print("Liian pieni luku")
    print("----")
    arvaukset += 1
  elif arvaus > vastaus:
    print("----")
    print("Liian suuri luku")
    print("----")
    arvaukset += 1
if arvaukset == 6:
  print("Liian monta arvausta")
  
  
