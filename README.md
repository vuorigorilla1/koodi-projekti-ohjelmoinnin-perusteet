# Arvauspeli
Ryhmän jäsenet: Elias Nieminen, Jesse Mitronen & Jere Paussu

## Pelin käynnistys:
Peli löytyy [Arvauspeli.py](arvauspeli.py) tiedostosta. Pelin saa käyntiin ajamalla ohjelman esimerkiksi Visual Studio Codessa.

## Työmäärän jakautuminen
Ryhmämme suunnitteli, ideoi ja kehitti sovellusta yhdessä. Koska Elias oli ryhmämme osaavin koodari, hän toteutti suurimman osan vaativammasta koodauksesta. Eliaksen tehdessä suurimman osan koodauksesta yritimme jakaa muut projektin tehtävät tasaisemmin ryhmän jäsenten kesken työtaakan tasapainottamiseksi. Jere kirjoitti README.md tiedoston ja teki vuokaavion. Jesse puolestaan teki videotallenteen, jossa hän esitteli sovelluksen ja koodin toimintaa.

## Sisällysluottelo:

- [Tietoa sovelluksesta](#tietoa-sovelluksesta)
- [Kuvankaappaukset](#Kuvankaappaukset)
- [Teknologiat](#Teknologiat)
- [Suunnittelu / Vuokaavio](#Suunnittelu)
- [Tila](#Tila)
- [Lähteet ja tekijät](#lähteet-ja-tekijät)
- [Lisenssi](#lisenssi)

## Tietoa sovelluksesta
Arvauspeli on sovellus, jossa pelaajalla on seitsemän yritystä arvata luku väliltä 1-100. Kun pelaaja yrittää arvata luvun, sovellus kertoo menikö arvaus oikein vai onko luku pienempi tai suurempi kuin käyttäjän antama luku. 

Kun peli päättyy joko pelaajan voittoon tai häviöön, pelaajalle annetaan mahdollisuus pelata uudelleen. Arvauspeli pitää myös kirjaa kymmenestä parhaasta tuloksesta tekemällä itse JSON-tiedoston pisteiden tallentamiseen. Jos tiedosto on jo olemassa, sovellus vain päivittää sitä. Sovellus näyttää tämän "highscore" listan aina pelin alussa.

Lisäksi sovellus on ohjelmoitu tunnistamaan virheelliset syötteet: jos pelaaja antaa arvauksen yhteydessä muun syötteen kuin luvun väliltä 1-100, sovellus tunnistaa ja ilmoittaa siitä. Myös silloin, kun pelaajalta kysytään haluaaka hän pelata uudelleen, sovellus tunnistaa jos vastaus ei ole "kyllä" tai "ei".

## Kuvankaappaukset
Tähän vähintään yks kuvankaappaus sovelluksesta.

## Teknologiat
Projektissa käytettiin pythonia.

## Suunnittelu
Meidän ryhmä lähestyi tehtävää ensin keskustelemalla siitä, millainen sovellus olisi sopivan haastava mutta silti toteutettavissa. Halusimme tehdä jotain missä on selkeä logiikka ja käyttäisi silmukoita. Päädyimme arvauspeliin, koska se sisältää paljon kurssilla oppimaamme, eikä ole liian monimutkainen. 

Suunnitellimme ensin sovelluksen toiminnan vaihe vaiheelta: ohjelma arpoo luvun, käyttäjä arvaa, ja ohjelma antaa palautteen siitä, onko arvaus liian suuri tai pieni. Sovellus kehittyi moneen kertaan, kun huomasimme sovelluksessa virheitä ja parannusideioita. Esimerkiksi top 10 listan lisääminen, pelaajan virheellisten syötteiden huomaaminen ja pelin uudelleen pelaaminen pysäyttämättä ohjelmaa.

Tämän jälkeen teimme vuokaavion, jotta sovelluksen toiminta olisi helpompi hahmottaa, minkä jälkeen aloitimme yhdessä koodin toteutuksen. Vuokaaviota päivitettiin myös moneen kertaan sovelluksen kehittyessä.

![Vuokaavio](Arvauspeli.png)

## Tila
Arvauspeli on vielä työn alla. 'Versio 4' julkaistaan pian.

## Lähteet ja tekijät
Tekijät: Elias Nieminen, Jesse Mitronen & Jere Paussu
Käytimme W3Schools nettisivua, että saimme "random modulen" toimimaan.

## Lisenssi
MIT-lisenssi © [tekijä](mit-license.org)
