---
name: Seed Signer

description: Teie Seed signer'i seadistamine
---

![kaas](assets/cover.webp)

## Materjal:

1. Raspberry Pi Zero (versioon 1.3)

Raspberry Pi Zero

Täielikult õhulõhega lahenduse jaoks veenduge, et kasutate versiooni 1.3 ilma WiFi või Bluetoothi võimekuseta, kuid töötada võib iga Raspberry Pi 2/3/4 või Zero mudel.

Märkus: Raspberry Pi'd ei tule tavaliselt koos joodetud pistikutega; pistikud tuleb kas joota või kasutada midagi, mida nimetatakse "GPIO Hammer" (GPIO Haamer).
GPIO Haamer

Kui teie jootmine pole päris hea või te lihtsalt ei oma veel jootekolbi, siis võite kasutada "GPIO Haamerit" kui alternatiivi jootmisele.

2. Chapeau LCD WaveShare 1,3 tolli ekraaniga 240 × 240 pikslit

WaveShare LCD Müts

Waveshare 1.3″ 240×240 pxl LCD

Märkus: Valige Waveshare ekraan hoolikalt; veenduge, et ostate mudeli, mille resolutsioon on 240×240 pikslit.
rohkem infot

3. Pi Zero'ga ühilduv kaameramoodul

Raspberry Pi Kaamera

Aokin / AuviPal 5MP 1080p OV5647 sensoriga videokaamera moodul; teised brändid OV5647 sensorimooduliga peaksid samuti töötama, kuid ei pruugi olla ühilduvad Orange Pill korpusega.

Märkus: Teil on vaja kaameraribakaablit, mis on spetsiaalselt ühilduv Raspberry Pi Zeroga.

4. MicroSD kaart vähemalt 4 GB mahutavusega

ulatuslikud ressursid: https://seedsigner.com/explainers/

## Tarkvara:

Tarkvara paigaldamine

1. Laadige alla viimane “seedsigner_x_x_x.img.zip” fail
   viimane väljalase

2. Pakkige lahti “seedsigner_x_x_x.img.zip” fail

3. Kasutage Balena Etcherit või sarnast tööriista, et kirjutada lahtipakitud .img pildifail microsd kaardile
   BALENA ETCHER

4. Paigaldage microsd kaart SeedSignerisse.
   SeedSigner GPG Avalik Võti
   seedsigner_pubkey.gpg

## Videoõpetus

_juhend võetud Southerbitcoiner'ilt, looja Cole_

### Videote kogumik, mis katab SeedSignerit: avatud lähtekoodiga, DIY Riistvara Rahakott/Allkirjastamise seade

![pilt](assets/1.webp)

SeedSigner on Bitcoin Allkirjastamise Seade, mille saate nullist ehitada. Tundub keeruline, kuid see 4-osaline seeria peaks teid aitama :) Soovitan vaadata osa 1 ja 2, seejärel otsustada, kas soovite kasutada lauaarvutit (vaadake osa 3) või mobiilseadet (vaadake osa 4).

Kõik, mida peate teadma, on allpool. Muud kasulikud lingid hõlmavad SeedSigneri veebisaiti, nende Githubi, nende Keybase'i, viimast väljalaset ja riistvara nõudeid.

### Osa 1: Kuidas ehitada SeedSignerit:

Selles videos näitan teile, kuidas alla laadida ja kontrollida SeedSigneri tarkvara, milliseid osi on vaja ja kuidas oma SeedSignerit kokku panna.

![video](https://youtu.be/mGmNKYOXtxY)

### Osa 2: Testige oma SeedSignerit
Enne kui hakkasin oma SeedSignerit kasutama, tegin mõned testid, et veenduda, et see ei tee midagi pahatahtlikku. Mõtlesin, et jagan ka seda sammu. Siin on, kuidas kontrollida, et teie SeedSigner ekspordib õige rahakoti (xpub), kuidas kontrollida SeedSigneri täringuveeretuste matemaatikat ja kuidas kontrollida SeedSigneri bip-85 lapse seemneid.
![video](https://youtu.be/34W1IyTyXZE)

### Osa 3: Kuidas kasutada SeedSignerit Sparrow Walletiga (lauaarvuti)

SeedSigner suudab genereerida seemneid ja allkirjastada bitcoin tehinguid. Kuid iseseisvalt ei ole see võimeline tehinguid looma. Peate kasutama rahakoti "koordinaatorit" koos oma SeedSigneriga. Siin on, kuidas kasutada Sparrow Walletit koos oma SeedSigneriga:

![video](https://youtu.be/IQb8dh-VTOg)

Osa 4: Kuidas kasutada SeedSignerit Blue Walletiga (mobiil)

SeedSigner suudab genereerida seemneid ja allkirjastada bitcoin tehinguid. Kuid iseseisvalt ei ole see võimeline tehinguid looma. Peate kasutama rahakoti "koordinaatorit" koos oma SeedSigneriga. Siin on, kuidas kasutada Blue Walletit koos oma SeedSigneriga:

![video](https://youtu.be/x0Ee35Ct0r4)

Need on kõik SeedSigneri juhendid praeguseks! Andke mulle teada, kui arvate, et midagi on puudu. Need on minu nimekirjas potentsiaalsete videote jaoks:

> SeedSigneri üldine ülevaade. Kas see on hea valik allkirjastamisseadmeks? Plussid/miinused?

> Kuidas kasutada Bip-85 SeedSigneriga
> Kuidas olla onu Jim SeedSigneriga

Leidsite need kasulikud? Kaaluge annetuse saatmist, et aidata rahastada tulevasi videoid:
https://www.southernbitcoiner.com/donate/