---
name: Lightning Smoke Machine
description: Activeer een rookmachine met een Lightning-betaling via ESP32.
---

![cover-lightning-smoke-machine](assets/cover.webp)



## Inleiding



Verandert een klassieke rookmachine in een apparaat dat via Lightning Network in Bitcoin betaald kan worden. Elke betaling veroorzaakt automatisch een rookstraal!





- Niveau: Gemiddeld
- Geschatte tijd: 2-3 uur
- Gebruikscases: Bitcoin-evenementen, artistieke optredens, Lightning-demo's, geautomatiseerde podiumeffecten



## Vereisten



### Kennis





 - Basiselektronica (bedrading, relais)
 - Lassen (of gebruik van Dupont connectoren)
 - Netwerkconfiguratie (WiFi, WebSocket)



### Vereiste rekeningen





- BTCPay-server: Functionele instantie (zelf gehost of gehost)
- Blink Wallet : Account + toegang API



### Toegang





- Admin toegang tot BTCPay server
- WiFi-verbinding voor ESP32



## Benodigde materialen



### Hardware - Elektronische onderdelen





- 1 Microcontroller - ESP32-WROOM-32


*De ESP32-WROOM-32 is een compacte, voordelige WiFi/Bluetooth microcontroller voor het verbinden van elektronische apparaten met internet en het op afstand bedienen ervan*



![ESP32](assets/fr/1.webp)





- 1 Relaismodule - 5V met optocoupler


*Een relais is als een schakelaar die de ESP32 kan bedienen om de rookmachine aan of uit te zetten*



![relay](assets/fr/2.webp)





- ~10 Dupont kabels - Mannelijk/Mannelijk en Mannelijk/Vrouwelijk



![dupont-cables](assets/fr/3.webp)





- 1 Voeding voor ESP32 - 5V USB of Li-Po batterij



![battery](assets/fr/4.webp)





- 1 micro-USB-kabel - verbinding tussen ESP32 en voeding



![micro-usb-cables](assets/fr/5.webp)





- 1 220V rookmachine met 12V batterij afstandsbediening



![remote-and-smoke-machine](assets/fr/6.webp)





- 1 fles vloeistof die compatibel is met je rookmachine



### Hardware - Gereedschap





- Soldeerbout + tin (indien solderen)
- Schroevendraaier
- Multimeter (aanbevolen)



### Software





- Firmware BitcoinSwitch : **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- WebSerial-compatibele webbrowser (Chrome/Edge/Brave)
- BTCPay Server geconfigureerd. Voor meer informatie over het creëren van een BTCPay Server instance, bezoek deze tutorial: https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc



## Systeemarchitectuur



![architecture-lightning-smoke-machine](assets/fr/7.webp)



---


**⚠️** **VEILIGHEIDSWAARSCHUWING - LEZEN VOORDAT U VERDER GAAT** **⚠️**



Bij dit project wordt een rookmachine aangesloten op een **220V lichtnet**. Verkeerd gebruik kan leiden tot **dodelijke elektrocutie** of **brand**.



**Niet-onderhandelbare regels:**



1. **Koppel de rookmachine ALTIJD los van het lichtnet** voordat u de afstandsbediening opent of aan de bedrading knoeit


2. **Verwijder de batterij uit de afstandsbediening** voor gebruik (risico op kortsluiting en beschadiging van onderdelen)


3. **Controleer of al je verbindingen geïsoleerd zijn** voordat je iets opnieuw aansluit


4. **Sluit de 220V** nooit opnieuw aan voordat de afstandsbedieningskast gesloten en beveiligd is



Als je je niet op je gemak voelt bij dit soort handelingen, neem dan iemand mee die dat wel kan.



---

## DEEL 1: Hardware-assemblage



### Stap 1: De afstandsbediening voorbereiden



Doel: Sluit het relais aan op de AAN/UIT-knop van de afstandsbediening


1. Afstandsbediening openen




    - AAN/UIT-knop identificeren
    - Schroef de behuizing los om de afstandsbediening te openen


2. Aansluitingen zoeken




 - Zoek de + en - aansluitingen van de
 - Test de continuïteit met een multimeter (optioneel)



![smoke-machine-remote](assets/fr/8.webp)



3. Bedrading van knoppen (soldeer of connectoren)




    - Soldeer een zwarte kabel aan de -aansluiting van de knop
    - Soldeer een rode kabel aan de gemeenschappelijke + aansluiting



![smoke-machine-remote](assets/fr/9.webp)



### Stap 2: Aansluiten op de relaismodule



**Herinnering: Relais terminologie




| **Terminal**         | **Beschrijving**           | **Functie**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (Normaal geopend)   | Schakeling standaard geopend | Sluit wanneer het relais wordt geactiveerd |
| NC (Normaal gesloten) | Schakeling standaard gesloten  | Opent wanneer het relais wordt geactiveerd  |
| COM (Gemeenschappelijk)         | Centrale terminal          | Schakelt tussen NO en NC              |

**Bedrading van afstandsbediening naar relaismodule:**




- Zwarte draad van AAN/UIT-knop **→** NO (Normally Open)
- Rode draad (common) **→** COM (Common)



**Logica:**


Wanneer de ESP32 het relais activeert, verbindt hij COM en NO, wat precies hetzelfde is als wanneer je op de knop van de afstandsbediening drukt.


Wanneer de ESP32 het relais uitschakelt, worden COM en NO gescheiden, wat gelijk staat aan het loslaten van de knop.



![remote-relay](assets/fr/10.webp)



### Stap 3: De ESP32 aansluiten op de relaismodule



**Bedradingsschema:**




| **ESP32** | **→** | **Relaismodule** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (Ingang)        |

**Verificatie:**




- VCC en GND goed aangesloten (polariteit)
- GPIO 21 gebruikt voor besturingssignaal
- Geen zichtbare kortsluiting



![relay-esp32](assets/fr/11.webp)



**Checkpoint Hardware**


Controleer voordat u overschakelt naar de software :




- Correct bedrade afstandsbediening
- Relaismodule aangesloten op ESP32
- Geen blote draden die andere componenten aanraken
- 220V altijd uitgeschakeld



![relay-esp32](assets/fr/12.webp)





---


## DEEL 2: Softwareconfiguratie



We gebruiken *Blink* als voorbeeld, maar *BTCPay Server* biedt ook *Strike, Breez en Boltz* als je een andere optie verkiest.



### Stap 1: Plugins, installatie *BitcoinSwitch* + *Blink



1 - Ga naar uw *BTCPay Server* instantie met een admin account



2 - Maak je eerste jaloezie



3 - Scroll aan de linkerkant van *BTCPay Server* naar beneden en ga naar *"Plugins beheren"*



![btcpay-plugins](assets/fr/13.webp)



4 - We gaan de *BitcoinSwitch* plugins en *Blink* installeren



![btcpay-plugins](assets/fr/14.webp)



5 - Scroll naar beneden in de lijst met plugins en klik op *"Installeren"* : *BitcoinSwitch en Blink* (of de beschikbare wallet van jouw keuze)



![btcpay-plugins](assets/fr/15.webp)



6 - Zodra de installatie voltooid is, herstart u *BTCPay Server* en wacht u 1 minuut totdat de instantie opnieuw is opgestart



![btcpay-plugins](assets/fr/16.webp)



7 - Als je terugkeert naar *"Plugins beheren"*, controleer dan of beide plugins geïnstalleerd zijn



![btcpay-plugins](assets/fr/17.webp)



### Stap 2: Backend : *BTCPay Server + Blink* configuratie



**1 - Maak een wallet *Blink***




- Bezoek https://www.blink.sv
- Maak uw account aan. Raadpleeg de handleiding :



[https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)



**2 - Genereer een API sleutel *Blink***




- Ga naar de API interface: **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** en log in met hetzelfde account dat u gebruikte om uw wallet *Blink* te maken



![blink-api](assets/fr/18.webp)





   - Ga, eenmaal aangesloten, naar het tabblad *API toetsen*



![blink-api](assets/fr/19.webp)





   - Klik op *" + "* in de rechterbovenhoek om toegang te krijgen tot uw API Key-configuratie



![blink-api](assets/fr/20.webp)





   - Geef je API Key een naam en laat de standaardinstellingen staan. Noteer vervolgens in de derde stap uw API Key - u ziet hem maar één keer: `blink_mZ5KxxxxxxxxxxxxxNbmX`



![blink-api](assets/fr/21.webp)





   - Eenmaal aangemaakt, zou het moeten verschijnen in je actieve API Sleutelslijst.



![blink-api](assets/fr/22.webp)



**3 - Verbind *Blink* met *BTCPay Server***




- Open uw *BTCPay Server*
- Navigeer naar : *Wallet* **→** *bliksem*



![btcpay-server](assets/fr/23.webp)





- Klik op *Een aangepast knooppunt gebruiken*
- Plak de volgende verbindingsstring:



```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```



**⚠️** **Belangrijk** :




- Wijzig het eerste deel niet: `type=blink;server=https://api.blink.sv/graphql`;
- Alleen vervangen :
    - api-key= *door jouw API Blink* sleutel
    - wallet-id= *door je wallet Blink* ID
- Klik dan op *Test verbinding* en vervolgens op *Opslaan*



![btcpay-server](assets/fr/24.webp)





 - Controleer of de verbinding tot stand is gebracht (groene status)



![btcpay-server](assets/fr/25.webp)



**4 - Een verkooppunt maken (PoS)**




- Ga in BTCPay Server naar de tab *Plugins* en klik op *Verkooppunt*



![btcpay-server](assets/fr/26.webp)





- Geef uw PoS een naam en klik op *Creëer*



![btcpay-server](assets/fr/27.webp)





- PoS-configuratie :
    - Kies een verkooppuntstijl = *Print weergave*
    - Valuta = *SATS*
    - Klik op *Opslaan*



![btcpay-server](assets/fr/28.webp)





- Productconfiguratie :
    - Alle standaardproducten verwijderen
    - Klik dan op *item toevoegen*



![btcpay-server](assets/fr/29.webp)



![btcpay-server](assets/fr/30.webp)





- Configureer het product:
    - Titel : *rookmachine*
    - Prijs : *10 sats*
    - Bitcoin GPIO-schakelaar : 21
    - Bitcoin schakelduur (in milliseconden) : 5000
    - Klik op *Sluiten* en dan op *Opslaan* om het nieuwe product op te slaan



![btcpay-server](assets/fr/31.webp)



### Stap 3: Firmware: De ESP32 flashen



**1 - Ga naar de flashwebsite




- Ga naar : [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)



![bitcoinswitch-lnbits](assets/fr/32.webp)



**2 - Flash de BitcoinSwitch-firmware**




- Sluit de ESP32 aan op je computer met je USB/Micro-USB-kabel
- Klik vervolgens op *Verbind met apparaat*
- Er wordt een venster geopend, selecteer de USB-poort op je ESP32 en klik vervolgens op *Connect*



![bitcoinswitch-lnbits](assets/fr/33.webp)





- Zodra je ESP32 is aangesloten, flashen we de BitcoinSwitch-firmware. Klik in de sectie *T-Display* op *Upload Firmware* voor de laatste beschikbare versie (momenteel: *bitcoinSwitch T-Display v1.0.1*)



![bitcoinswitch-lnbits](assets/fr/34.webp)





- Wacht op het uploaden, het proces is voltooid als de logs *"Leaving... "*


![bitcoinswitch-lnbits](assets/fr/35.webp)





- Koppel de ESP32 los



**3 - Controleer de installatie van de BitcoinSwitch-firmware




- Pagina herladen: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Sluit de ESP32 opnieuw aan op je computer met je USB/Micro-USB-kabel
- Klik vervolgens op *Verbind met apparaat
- Selecteer de USB-poort op je ESP32 en klik vervolgens op *Connect* zoals hierboven beschreven
- Druk op de knop **RESET** op de ESP32 zodra deze is aangesloten
- Controleer in de logboeken of de laatste regels :



```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```



(Dit is normaal, het betekent dat er nog geen configuratie is, maar dat de firmware is geïnstalleerd)



![bitcoinswitch-lnbits](assets/fr/36.webp)



**4 - WebSocket LNURL** URL genereren



Verwacht eindformaat :



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



Generatiestappen :




- Open jeBTCPay Server instance en ga naar de PoS die we later hebben aangemaakt.
- Klik vervolgens op "Weergeven" om uw PvE in de browser te openen



![btcpay-server-https](assets/fr/37.webp)





- Kopieer de URL van de pagina, bijvoorbeeld :



![btcpay-server-https](assets/fr/38.webp)



Laten we deze URL eens uitpakken:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```





- `XXXXv` → het domein van uw BTCPay Server instantie
- `46XXXXXXXXXXXXXXXXXXwFB` → uw unieke PoS-identificatiecode
- `/pos` → geeft een verkooppunt aan



Transformeer het:




- Vervang `https://` door `wss://`
- Voeg `/bitcoinswitch` toe aan het einde



Resultaat:



```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```



Bewaar deze URL voor toekomstige configuratie, want het zal uw ESP32 in staat stellen om in real time te communiceren met de BTCPay Server. Het WebSocket-protocol (`wss://`) brengt een permanente verbinding tot stand tussen de twee: zodra een Lightning-betaling is bevestigd op uw PoS, stuurt BTCPay onmiddellijk de informatie naar de ESP32, die vervolgens uw rookmachine kan activeren.



**5 - WiFi en WebSocket configureren




- Keer terug naar de pagina: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/) met je ESP32 aangesloten
- Ga naar *Gebruik apparaat configureren* → *Wifi instellingen*



Inform :




- WiFi SSID: de naam van je WiFi-netwerk
- WiFi-wachtwoord: je WiFi-wachtwoord



![bitcoinswitch-lnbits](assets/fr/39.webp)





- Plak in het gedeelte *LNbits Apparaat URL* de WebSocket URL die in de vorige stap is gemaakt
- Klik op *Upload configuratie*



![bitcoinswitch-lnbits](assets/fr/40.webp)





- Wacht tot de upload is voltooid; de logs moeten de parameters weergeven die u zojuist hebt ingevoerd (SSID, wachtwoord en WebSocket URL)



![bitcoinswitch-lnbits](assets/fr/41.webp)





- Wacht terwijl ESP32 de WebSocket-verbinding tot stand brengt. Je zou moeten zien :



```
WiFi connection established!

[WebSocket] Connected to url: ...
```



![bitcoinswitch-lnbits](assets/fr/42.webp)





- U kunt nu de ESP32 loskoppelen



---
## Checkpoint software



Controleer voor de eindtest :





- Blink verbonden met BTCPay
- PoS gemaakt met minstens 1 item
- ESP32 geflasht met BitcoinSwitch
- WiFi geconfigureerd op ESP32
- WebSocket URL correct
- Foutloze ESP32-logboeken



---

## Testen en debuggen



### Eindtest afronden



1. Steek de stekker van de rookmachine in het stopcontact (220V) en zet hem aan


2. Voed de ESP32 (batterij of USB)


3. Open uw BTCPay PoS in uw browser


4. Item "rookmachine" scannen


5. Betalen met een wallet Lightning (Blink of andere wallet)


6. Let op:




 - Relais klikt (hoorbaar geluid en relais-LED brandt)
 - De rookmachine is geactiveerd
 - Rookontwikkeling!



### Eerlijkheidsproblemen en oplossingen




| **Probleem**                        | **Waarschijnlijke oorzaak**              | **Oplossing**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 maakt geen verbinding            | USB-stuurprogramma ontbreekt             | Installeer [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| Relais klikt niet                | Verkeerde GPIO-bedrading            | Controleer GPIO 21 → IN                                                                        |
| Rookmachine reageert niet         | Afstandsbediening verkeerd aangesloten         | Controleer NO/NC/COM                                                                           |
| WebSocket-timeout                   | Onjuiste URL                  | Controleer wss:// en /bitcoinswitch                                                            |
| WiFi maakt geen verbinding             | SSID/Wachtwoord onjuist            | WiFi-configuratie opnieuw flashen                                                                    |
| Betaling ontvangen maar niets gebeurt | ESP32 niet verbonden met WebSocket | Controleer RESET-logboeken                                                                      |

## Bronnen



### Nuttige links





- BitcoinSwitch Firmware: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- BTCPay Server Docs : [https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- ESP32 Pinout : [https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)



### Gemeenschap & ondersteuning





- BTCPay Server** : [chat.btcpayserver.org](https://chat.btcpayserver.org/) - Officiële Mattermost
- BTCPay Server Telegram** : [t.me/btcpayserver](https://t.me/btcpayserver)
- LNbits** : [t.me/lnbits](https://t.me/lnbits) - Officiële Telegram, actieve gemeenschap
- BitcoinSwitch (firmware bugs)**: [github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)



### Broncode





- BitcoinSwitch firmware broncode: [https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)



---

**⚡** Stapel sats, maak rook, heb plezier, blijf nederig! **⚡**