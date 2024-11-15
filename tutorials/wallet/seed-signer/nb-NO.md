---
name: Seed Signer

description: Oppsett av din Seed signer
---

![cover](assets/cover.webp)

## Materiell:

1. Raspberry Pi Zero (versjon 1.3)

Raspberry Pi Zero

For en fullstendig luftgappet løsning, sørg for å bruke versjon 1.3 uten WiFi eller Bluetooth-kapasitet, men enhver Raspberry Pi 2/3/4 eller Zero-modell vil fungere.

Merk: Raspberry Pi kommer vanligvis ikke med pins festet; pinnene må enten loddes på, eller noe som kalles en "GPIO Hammer" kan brukes.
GPIO Hammer

Hvis loddeferdighetene dine ikke er helt på topp, eller du bare ikke eier en loddebolt ennå, kan du bruke "GPIO Hammer" som et alternativ til lodding.

2. Chapeau LCD WaveShare 1,3 tommer med skjerm 240 × 240 piksler

WaveShare LCD Hat

Waveshare 1.3″ 240×240 pxl LCD

Merk: Velg Waveshare-skjermen nøye; sørg for å kjøpe modellen som har en oppløsning på 240×240 piksler.
mer info

3. Modul de caméra kompatibel med Pi Zero

Raspberry Pi Camera

Aokin / AuviPal 5MP 1080p med OV5647 Sensor Video Camera Module; andre merker med OV5647-sensormodulen skal også fungere, men er kanskje ikke kompatible med Orange Pill-kabinettet.

Merk: Du må ha et kamerabåndkabel spesifikt kompatibelt med Raspberry Pi Zero.

4. MicroSD-kort med minst 4 GB kapasitet

omfattende ressurser: https://seedsigner.com/explainers/

## Programvare:

Programvareinstallasjon

1. Last ned den nyeste “seedsigner_x_x_x.img.zip”-filen
   siste utgivelse

2. Pakk ut “seedsigner_x_x_x.img.zip”-filen

3. Bruk Balena Etcher eller et lignende verktøy for å skrive den utpakkede .img-bildefilen til et microsd-kort
   BALENA ETCHER

4. Installer microsd-kortet i SeedSigner.
   SeedSigner GPG Public Key
   seedsigner_pubkey.gpg

## Videoveiledning

_guide hentet fra Southerbitcoiner, laget av Cole_

### En samling av videoveiledninger som dekker SeedSigner: en åpen kildekode, DIY Hardware Wallet/Signing-enhet

![image](assets/1.webp)

SeedSigner er en Bitcoin Signing Device du kan bygge fra bunnen av. Høres vanskelig ut, men denne 4-delers serien bør hjelpe deg :) Jeg foreslår at du ser del 1 og 2, og deretter bestemmer om du vil bruke desktop (se del 3) eller en mobil enhet (se del 4).

Alt du trenger å vite vil være nedenfor. Andre nyttige lenker inkluderer SeedSigners nettsted, deres Github, deres Keybase, den siste utgivelsen, og maskinvarekrav.

### Del 1: Hvordan bygge en SeedSigner:

I denne videoen viser jeg deg hvordan du laster ned og verifiserer SeedSigner-programvaren, hvilke deler som trengs, og hvordan du monterer din SeedSigner.

![video](https://youtu.be/mGmNKYOXtxY)

### Del 2: Testing av din SeedSigner
Før jeg brukte min SeedSigner, gjorde jeg noen tester for å forsikre meg om at den ikke gjorde noe ondsinnet. Jeg tenkte jeg skulle dele dette steget også. Her er hvordan du verifiserer at din SeedSigner eksporterer den korrekte lommeboken (xpub), hvordan verifisere SeedSigners terningkastmatematikk, og hvordan verifisere SeedSigners bip-85 barneseeds.
![video](https://youtu.be/34W1IyTyXZE)

### Del 3: Hvordan bruke SeedSigner med Sparrow Wallet (desktop)

SeedSigner er i stand til å generere seeds og signere bitcoin-transaksjoner. Men alene er den ikke i stand til å bygge transaksjoner. Du trenger å bruke en lommebok "koordinator" med din SeedSigner. Slik bruker du Sparrow Wallet med din SeedSigner:

![video](https://youtu.be/IQb8dh-VTOg)

Del 4: Hvordan bruke SeedSigner med Blue Wallet (mobil)

SeedSigner er i stand til å generere seeds og signere bitcoin-transaksjoner. Men alene er den ikke i stand til å skape transaksjoner. Du trenger å bruke en lommebok "koordinator" med din SeedSigner. Slik bruker du Blue Wallet med din SeedSigner:

![video](https://youtu.be/x0Ee35Ct0r4)

Det var alle SeedSigner-guidene, for nå! Gi meg beskjed hvis du tror jeg mangler noe. Dette er på listen min over potensielle videoer:

> En helhetlig anmeldelse av SeedSigner. Er det et godt valg for en signeringsenhet? Fordeler/ulemper?

> Hvordan bruke Bip-85 med SeedSigner
> Hvordan være onkel Jim med SeedSigner

Fant du disse verdifulle? Vurder å sende et tips for å hjelpe med finansiering av fremtidige videoer:
https://www.southernbitcoiner.com/donate/