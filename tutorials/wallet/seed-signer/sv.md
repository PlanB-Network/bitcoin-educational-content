---
name: seed undertecknare

description: Uppsättning av din seed-signatur
---

![cover](assets/cover.webp)


## Material:


**Raspberry Pi Zero (version 1.3)**


För en helt lufttät lösning, se till att använda version 1.3 utan WiFi- eller Bluetooth-kapacitet, men alla Raspberry Pi 2/3/4 eller Zero-modeller fungerar.


Obs: Raspberry Pi som dessa levereras vanligtvis inte med anslutna stift; stiften måste antingen lödas fast eller så kan något som kallas "GPIO Hammer" användas.

GPIO-hammare


Om du inte är så bra på att löda, eller om du helt enkelt inte har någon lödkolv än, kan du använda "GPIO Hammer" som ett alternativ till lödning.


**Hatt LCD WaveShare 1,3 tum med skärm 240 × 240 pixlar**


WaveShare LCD Hat 1,3″ 240×240 pxl LCD


**Välj Waveshare-skärmen noggrant; se till att köpa den modell som har en upplösning på 240×240 pixlar.


**Kameramodul kompatibel med Pi Zero**


Raspberry Pi Camera Aokin/AuviPal 5MP 1080p med OV5647 Sensor Video Camera Module; andra märken med OV5647 sensormodul bör också fungera, men kanske inte är kompatibla med Orange Pill-kapslingen.


**Du måste ha en bandkabel för kameran som är särskilt kompatibel med Raspberry Pi Zero.


**MicroSD-kort med minst 4 GB kapacitet**


omfattande resurser: https://seedsigner.com/explainers/


## Programvara:


Installation av programvara


1. Ladda ner den senaste filen "seedsigner_x_x_x.img.zip"

senaste utgåvan

2. Packa upp filen "seedsigner_x_x_x.img.zip"

3. Använd Balena Etcher eller ett liknande verktyg för att skriva den uppackade .img-bildfilen till ett microsd-kort

BALENA ETCHER

4. Installera microsd-kortet i SeedSigner.

SeedSigner GPG-offentlig nyckel

seedsigner_pubkey.gpg


## Instruktionsvideo


_guide hämtad från Southerbitcoiner, skapad av Cole_


### En samling videoguider som täcker SeedSigner: en Hardware Wallet/signeringsenhet med öppen källkod som du gör själv


![image](assets/1.webp)


SeedSigner är en Bitcoin-signeringsenhet som du kan bygga från grunden. Låter svårt, men den här 4-delade serien borde hjälpa dig :) Jag föreslår att du tittar på del 1 och 2 och sedan bestämmer om du vill använda skrivbordet (titta på del 3) eller en mobil enhet (titta på del 4).


Allt du behöver veta kommer att finnas nedan. Andra användbara länkar inkluderar SeedSigners webbplats, deras Github, deras Keybase, den senaste versionen och hårdvarukrav.


### Del 1: Hur man bygger en SeedSigner:


I den här videon visar jag hur du laddar ner och verifierar SeedSigner-programvaran, vilka delar som behövs och hur du monterar din SeedSigner.


![video](https://youtu.be/mGmNKYOXtxY)


### Del 2: Testa din SeedSigner


Innan jag använde min SeedSigner gjorde jag några tester för att säkerställa att den inte gjorde något skadligt. Jag tänkte att jag skulle dela detta steg också. Här är hur man verifierar att din SeedSigner exporterar rätt Wallet (xpub), hur man verifierar SeedSigners tärningsrullar matematik och hur man verifierar SeedSigners bip-85 barnfrön.


![video](https://youtu.be/34W1IyTyXZE)


### Del 3: Så här använder du SeedSigner med Sparrow Wallet (skrivbord)


SeedSigner kan generera frön och signera Bitcoin-transaktioner. Men i sig själv kan den inte bygga transaktioner. Du måste använda en Wallet "koordinator" med din SeedSigner. Så här använder du Sparrow Wallet med din SeedSigner:


![video](https://youtu.be/IQb8dh-VTOg)


Del 4: Så här använder du SeedSigner med Blue Wallet (mobil)


SeedSigner kan generera frön och signera Bitcoin-transaktioner. Men i sig själv kan den inte skapa transaktioner. Du måste använda en Wallet "koordinator" med din SeedSigner. Så här använder du Blue Wallet med din SeedSigner:


![video](https://youtu.be/x0Ee35Ct0r4)


Det här är alla SeedSigner-guider, för nu! Låt mig veta om du tror att jag saknar något. Dessa är på min lista för potentiella videor:



- SeedSigner övergripande granskning. Är det ett bra val för en signeringsenhet? Fördelar / nackdelar?
- Så här använder du Bip-85 med SeedSigner
- Hur man blir farbror Jim med SeedSigner


Hittade du dessa värdefulla? Överväg att skicka ett tips för att hjälpa till att finansiera framtida videor:

https://www.southernbitcoiner.com/donate/