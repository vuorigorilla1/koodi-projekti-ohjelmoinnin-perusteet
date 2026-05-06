import random  #tarvitaan antamaan luku arvausta varten 1-100
import json    #tarvitaan tulosten tallentamiseen tulostaulukkoon
import os      #tarvitaan tarkastamaan jsonin olemassaolo

#tämä funktio lataa tulokset tiedostosta
def lataa_tulokset():
    if os.path.exists("pisteet.json"):  #jos tiedosto on olemassa palautetaan tulokset listana
        with open("pisteet.json", "r") as f:
            return json.load(f) 
    return []  #jos tiedostoa ei ole, palautetaan tyhjä lista
#tämä funktio tallentaa uuden tuloksen tiedostoon
def tallenna_tulos(arvaukset):
    nimi = input("Syötä nimesi tuloslistalle: ") or "Anonyymi"  #kysytään pelaajan nimi
    tulokset = lataa_tulokset()  #ladataan vanhat tulokset
    tulokset.append({"nimi": nimi, "arvaukset": arvaukset})  #lisätään uusi tulos
    tulokset.sort(key=lambda x: x["arvaukset"])  #järjestetään tulokset paremmuusjärjestykseen
    tulokset = tulokset[:10]  #tulostaulukossa on vain top 10 pelaajat
    with open("pisteet.json", "w") as f:
        json.dump(tulokset, f)  #tallennetaan tiedostoon
#tämä funktio näyttää tulostaulukon
def tulostaulukko():
    tulokset = lataa_tulokset()
    print("\n----- TULOSTAULUKKO -----")
    if not tulokset:
        print("    Ei vielä tuloksia!")
    else:
        for i, tulos in enumerate(tulokset, 1):  #käydään tulokset läpi
            print(f"  {i}. {tulos['nimi']} - {tulos['arvaukset']} arvausta")
    print("-------------------------\n")

#peli

while True:  #pyörittää peliä, kunnes pelaaja lopettaa
    tulostaulukko()  #näyttää tulokset
    vastaus = random.randint(1, 100)  #arvotaan satunnainen luku 1-100
    arvaukset = 0  #nollataan arvauksien määrä
    voitto = False  #pelaaja ei ole vielä voittanut
    print("Arvaa luku väliltä 1-100. Sinulla on 7 yritystä.\n")
    while arvaukset < 7:  #looppi pyörii kunnes arvaukset loppuu
        print("---------------------")
        print(f"Arvauksia jäljellä: {7 - arvaukset}")
        print("---------------------")
        print()
        try:
            arvaus = int(input("Anna luku: "))  #pyydetään pelaajan arvaus
        except ValueError:
            print("-------------------")
            print("Anna pelkkä numero!")  #jos syöte ei ole numero
            print("-------------------")
            print()
            continue  #palataan loopin alkuun ilman arvausta
        if arvaus < 1 or arvaus > 100:
            print()
            print("-------------------------------")
            print("Luku täytyy olla väliltä 1-100!")  #tarkistetaan onko luku välillä 1-100
            print("-------------------------------")
            print()
        elif arvaus == vastaus:
            arvaukset += 1
            print("---------------")
            print("Oikein, voitit!")
            print("---------------")
            print()
            voitto = True  #merkitään onko pelajaa voittanut
            tallenna_tulos(arvaukset)  #tallennetaan pelin tulos
            break  #lopettaa loopin, kun peli on voitettu
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
    if not voitto:  #jos pelaaja ei ole voitannut tapahtuu näin
        print("------------------------------")
        print(f"Hävisit! Oikea vastaus oli {vastaus}.")
        print("------------------------------")
    #kysytään haluaako pelata uudelleen
    uudelleen = input("Haluatko pelata uudelleen? (kyllä / ei): ")
    if uudelleen == "ei":
        print("Lopetetaan...")
        tulostaulukko()  #näytetään lopuksi tulostaulukko
        break  #lopetetaan ohjelma
