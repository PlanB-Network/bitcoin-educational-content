---
name: SeedSigner

description: Instellen van uw seed ondertekenaar
---

![cover](assets/cover.webp)


## Materiaal:


**Raspberry Pi Zero (versie 1.3)**


Voor een volledig air-gapped oplossing, zorg ervoor dat je de versie 1.3 gebruikt zonder WiFi of Bluetooth mogelijkheden, maar elk Raspberry Pi 2/3/4 of Zero model zal werken.


Opmerking: Raspberry Pi's die dat wel doen worden meestal niet geleverd met pinnen; de pinnen moeten erop gesoldeerd worden of er kan een "GPIO Hammer" gebruikt worden.

GPIO-hamer


Als je niet goed kunt solderen, of je hebt nog geen soldeerbout, dan kun je "GPIO Hammer" gebruiken als alternatief voor solderen.


**Hoed LCD WaveShare 1,3 inch met scherm 240 × 240 pixels**


WaveShare LCD Hoed 1,3″ 240×240 pxl LCD


**Noot:** Kies het Waveshare-scherm zorgvuldig; zorg ervoor dat je een model koopt met een resolutie van 240×240 pixels.


**Cameramodule compatibel met Pi Zero**


Raspberry Pi Camera Aokin/AuviPal 5MP 1080p met OV5647 Sensor Videocameramodule; andere merken met de OV5647 sensormodule zouden ook moeten werken, maar zijn mogelijk niet compatibel met de Orange Pill behuizing.


**Noot:** Je hebt een camera lintkabel nodig die specifiek compatibel is met Raspberry Pi Zero.


**MicroSD-kaart met minstens 4 GB capaciteit**


uitgebreide bronnen: https://seedsigner.com/explainers/


## Software:


Software-installatie


1. Download het nieuwste bestand "seedsigner_x_x.img.zip

nieuwe versie

2. Pak het bestand "seedsigner_x_x.img.zip" uit

3. Gebruik de Balena Etcher of een vergelijkbaar programma om het uitgepakte .img image-bestand naar een microsd-kaart te schrijven

BALENA ETCHER

4. Installeer de microsd-kaart in SeedSigner.

SeedSigner GPG openbare sleutel

seedsigner_pubkey.gpg


## Video-handleiding


_gids overgenomen van Southerbitcoiner, gemaakt door Cole_


### Een verzameling videogidsen over SeedSigner: een open source, doe-het-zelf Hardware Wallet/ondertekenapparaat


![image](assets/1.webp)


SeedSigner is een Bitcoin ondertekeningsapparaat dat je vanaf nul kunt opbouwen. Klinkt moeilijk, maar deze 4-delige serie zou je moeten helpen :) Ik stel voor dat je deel 1 en 2 bekijkt, en dan beslist of je een desktop (deel 3) of een mobiel apparaat (deel 4) wilt gebruiken.


Alles wat je moet weten staat hieronder. Andere nuttige links zijn SeedSigner's website, hun Github, hun Keybase, de laatste release en hardware vereisten.


### Deel 1: Hoe bouw je een SeedSigner?


In deze video laat ik je zien hoe je de SeedSigner software download en controleert, welke onderdelen je nodig hebt en hoe je je SeedSigner in elkaar zet.


![video](https://youtu.be/mGmNKYOXtxY)


### Deel 2: Uw SeedSigner testen


Voordat ik mijn SeedSigner gebruikte, deed ik een paar tests om er zeker van te zijn dat het niets kwaadaardigs deed. Ik wilde deze stap ook met jullie delen. Hier lees je hoe je controleert of je SeedSigner de juiste Wallet (xpub) exporteert, hoe je controleert of SeedSigners dobbelstenen rollen rekenen en hoe je controleert of SeedSigners bip-85 child seeds.


![video](https://youtu.be/34W1IyTyXZE)


### Deel 3: Hoe SeedSigner gebruiken met Sparrow wallet (desktop)


SeedSigner kan zaden genereren en Bitcoin transacties aftekenen. Maar op zichzelf is het niet in staat om transacties op te bouwen. Je moet een Wallet "coördinator" gebruiken met je SeedSigner. Zo gebruik je Sparrow wallet met je SeedSigner:


![video](https://youtu.be/IQb8dh-VTOg)


Deel 4: Hoe SeedSigner gebruiken met Blue Wallet (mobiel)


SeedSigner kan zaden aanmaken en Bitcoin transacties aftekenen. Maar op zichzelf is het niet in staat om transacties aan te maken. Je moet een Wallet "coördinator" gebruiken met je SeedSigner. Zo gebruik je Blue Wallet met je SeedSigner:


![video](https://youtu.be/x0Ee35Ct0r4)


Dit zijn voorlopig alle SeedSigner gidsen! Laat het me weten als je denkt dat ik iets mis. Deze staan op mijn lijst voor mogelijke video's:



- SeedSigner algemene evaluatie. Is het een goede keuze als ondertekeningsapparaat? Voordelen/nadelen?
- Hoe Bip-85 gebruiken met SeedSigner
- Hoe oom Jim te zijn met SeedSigner


Vond je deze waardevol? Overweeg een tip te sturen om toekomstige video's te helpen financieren:

https://www.southernbitcoiner.com/donate/