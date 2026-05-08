import random #tarvitaan antamaan satunnainen luku
import json #tarvitaan tulosten tallentamiseen tulostaulukkoon json teidostossa
import os #tarvitaan tarkastamaan jsonin olemassaolo 

#------------------------------------------------
#ensin tarvittavat funktiot tulostaulukkoa varten
#------------------------------------------------

#tämä funktio lataa tulokset tiedostosta
def lataa_tulokset():
    if os.path.exists("pisteet.json"): #jos tiedosto on olemassa palautetaan tulokset listana
        with open("pisteet.json", "r") as f:
            return json.load(f) 
    return [] #jos tiedostoa ei ole, palautetaan tyhjä lista

#tällä funktiolla järjestetään tulostaulukko paremmuusjärjestykseen
def arvausjarjestys(tulos):
    return tulos["arvaukset"]

#tämä funktio tallentaa uuden tuloksen tiedostoon
def tallenna_tulos(arvaukset):
    nimi = input("Syötä nimesi tuloslistalle: ") #kysytään pelaajan nimi
    if nimi == "":
        nimi = "Nimetön" #jos pelaaja ei syötä nimeä annetaan nimen arvoksi nimetön
    tulokset = lataa_tulokset() #ladataan vanhat tulokset
    tulokset.append({"nimi": nimi, "arvaukset": arvaukset}) #lisätään uusi tulos
    tulokset.sort(key=arvausjarjestys) #järjestetään tulokset paremmuusjärjestykseen arvausjarjestys funktion avulla
    tulokset = tulokset[:10] #tulostaulukossa on vain top 10 pelaajat
    with open("pisteet.json", "w") as f:
        json.dump(tulokset, f) #tallennetaan tiedostoon
        
#tämä funktio näyttää tulostaulukon
def tulostaulukko():
    tulokset = lataa_tulokset()
    print()
    print("----- TULOSTAULUKKO -----")
    if not tulokset:
        print("    Ei vielä tuloksia!")
    else:
        for i, tulos in enumerate(tulokset, 1): #käydään tulokset läpi
            print(f"  {i}. {tulos['nimi']} - {tulos['arvaukset']} arvausta")
    print("-------------------------")
    print()

#----------------------------
#tästä alkaa itse pelin koodi
#----------------------------

while True: #pyörittää peliä kunnes pelaaja lopettaa
    tulostaulukko() #näyttää tulokset tulostaulukko funktiolla
    vastaus = random.randint(1, 100) #arvotaan satunnainen luku 1-100
    arvaukset = 0 #nollataan arvauksien määrä
    voitto = False #pelaaja ei ole vielä voittanut
    print()
    print("Arvaa luku väliltä 1-100. Sinulla on 7 yritystä.")
    print()
    while arvaukset < 7: #looppi pyörii kunnes arvaukset loppuu
        print("---------------------")
        print(f"Arvauksia jäljellä: {7 - arvaukset}")
        print("---------------------")
        print()
        try: #koitetaan saada käyttäjältä kokonaisluku
            arvaus = int(input("Anna luku: ")) #pyydetään pelaajan arvaus
        except ValueError: #jos käyttäjä syöttää jonkin muun kuin kokonaisluvun niin käy näin:
            print("-------------------")
            print("Anna pelkkä numero!")
            print("-------------------")
            print()
            continue #palataan loopin alkuun ilman viemättä arvausta
        if arvaus < 1 or arvaus > 100:
            print()
            print("-------------------------------")
            print("Luku täytyy olla väliltä 1-100!") #tarkistetaan onko luku välillä 1-100
            print("-------------------------------")
            print()
        elif arvaus == vastaus:
            arvaukset += 1
            print("---------------")
            print("Oikein, voitit!")
            print("---------------")
            print()
            voitto = True #merkitään onko pelajaa voittanut
            tallenna_tulos(arvaukset) #tallennetaan pelin tulos
            break #lopettaa loopin, kun peli on voitettu
        elif arvaus < vastaus:
            print()
            print("------------")
            print("Liian pieni!")
            print("------------")
            print()
            arvaukset += 1
        else:
            print()
            print("------------")
            print("Liian suuri!")
            print("------------")
            print()
            arvaukset += 1
    if not voitto: #jos pelaaja ei ole voitannut tapahtuu näin
        print("------------------------------")
        print(f"Hävisit! Oikea vastaus oli {vastaus}.")
        print("------------------------------")
    #kysytään haluaako pelata uudelleen
    while True:
        print()
        uudelleen = input("Haluatko pelata uudelleen? (kyllä / ei): ")
        print()
        if uudelleen == "kyllä":
            break #vastaat kyllä: peli alkaa alusta rikkomalla tämän loopin ja jatkamalla takaisin ensimmäisen loopin alkuun
        elif uudelleen == "ei":
            print()
            print("Lopetetaan...")
            print()
            tulostaulukko() #näytetään lopuksi tulostaulukko
            break #vastaat ei: peli loppuu kahdella break komenolla tällä rivillä ja koodin viimeisellä rivillä
        else: #jos vastaat jotain muuta kuin kyllä tai ei niin palaat takaisin tämän while loopin alkuun 
            print()
            print("Vastaa 'kyllä' tai 'ei'.")
            print()
    if uudelleen == "ei":
        break #lopetetaan pelin päälooppi
