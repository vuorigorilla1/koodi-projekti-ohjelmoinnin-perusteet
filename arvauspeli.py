import random
while True:
    arvaukset = 0
    max = 100
    min = 1
    vastaus = random.randint(min, max)
    print()
    print()
    print()
    print("Tässä pelissä sinun kuuluu arvata luku väliltä 1-100. Sinulla on seitsemän yritystä. Ohjelma kertoo onko luku liian suuri vai liian pieni. Jos saat luvun oikein, voitat pelin.")
    print()
    print()
    print()
    while arvaukset < 7:
        arvaus = input("Anna luku väliltä 1-100: ")
        if arvaus > 100:
            print()
            print("--------------------------------")
            print("Virhe, luku on suurempi kuin 100")
            print("--------------------------------")
            print()
        elif arvaus < 1:
            print()
            print("------------------------------")
            print("Virhe, luku on pienempi kuin 1")
            print("------------------------------")
            print()
        elif arvaus == vastaus:
            print()
            print("--------------------")
            print("Oikein, voitit pelin")
            print("--------------------")
            print()
            break
        elif arvaus < vastaus:
            print()
            print("----------------")
            print("Liian pieni luku")
            print("----------------")
            print()
            arvaukset += 1
        elif arvaus > vastaus:
            print()
            print("----------------")
            print("Liian suuri luku")
            print("----------------")
            print()
            arvaukset += 1
    if arvaukset == 7:
        print()
        print("--------------------")
        print("Liian monta arvausta")
        print("--------------------")
        print()
    uudelleen = input("Haluatko pelata uudelleen? (kyllä / ei) ")
    if uudelleen == "kyllä":
        arvaukset = arvaukset - 7
        continue
    elif uudelleen == "ei":
        break
    else:
        print("Vaustaukset tulee olla 'kyllä' tai 'ei'")
