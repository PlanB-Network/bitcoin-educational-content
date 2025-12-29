---
name: Lightning Smoke Machine
description: Utløs en røykmaskin med en Lightning-betaling via ESP32.
---

![cover-lightning-smoke-machine](assets/cover.webp)



## Innledning



Forvandler en klassisk røykmaskin til en enhet som kan betales i Bitcoin via Lightning Network. Hver betaling utløser automatisk en røykstråle!





- Nivå: Mellomnivå
- Beregnet tid: 2-3 timer
- Bruksområder: Bitcoin-arrangementer, kunstneriske forestillinger, lyndemonstrasjoner, automatiserte sceneeffekter



## Forutsetninger



### Kunnskap





 - Grunnleggende elektronikk (kabling, releer)
 - Sveising (eller bruk av Dupont-kontakter)
 - Nettverkskonfigurasjon (WiFi, WebSocket)



### Regnskap kreves





- BTCPay-server: Funksjonell instans (selvhostet eller hostet)
- Blink Wallet : Konto + tilgang API



### Tilgang





- Administratortilgang til BTCPay Server
- WiFi-tilkobling for ESP32



## Nødvendige materialer



### Maskinvare - Elektroniske komponenter





- 1 mikrokontroller - ESP32-WROOM-32


*ESP32-WROOM-32 er en kompakt og rimelig WiFi-/Bluetooth-mikrokontroller for tilkobling av elektroniske enheter til Internett og fjernstyring av dem*



![ESP32](assets/fr/1.webp)





- 1 Relémodul - 5V med optokobler


*Et relé er som en bryter som ESP32 kan betjene for å slå røykmaskinen på eller av*



![relay](assets/fr/2.webp)





- ~10 Dupont-kabler - hann/hann og hann/hunn



![dupont-cables](assets/fr/3.webp)





- 1 Strømforsyning for ESP32 - 5 V USB eller Li-Po-batteri



![battery](assets/fr/4.webp)





- 1 mikro-USB-kabel - tilkobling mellom ESP32 og strømforsyningen



![micro-usb-cables](assets/fr/5.webp)





- 1 220V tåkemaskin med 12V batterifjernkontroll



![remote-and-smoke-machine](assets/fr/6.webp)





- 1 flaske væske som er kompatibel med røykmaskinen din



### Maskinvare - Verktøy





- Loddebolt + tinn (hvis lodding)
- Skrutrekker
- Multimeter (anbefales)



### Programvare





- Fastvare BitcoinSwitch : **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- WebSerial-kompatibel nettleser (Chrome/Edge/Brave)
- BTCPay Server konfigurert. For mer informasjon om hvordan du oppretter en BTCPay Server-forekomst, besøk denne veiledningen: https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc



## Systemarkitektur



![architecture-lightning-smoke-machine](assets/fr/7.webp)



---


**⚠️** **SIKKERHETSADVARSEL - LES FØR DU FORTSETTER** **⚠️**



Dette prosjektet omfatter en tåkemaskin som er koblet til et **220 V strømnett**. Feil bruk kan føre til **dødelig elektrisk støt** eller **brann**.



**Ikke-forhandlingsbare regler



1. **Koble ALLTID røykmaskinen fra strømnettet** før du åpner fjernkontrollen eller tukler med kablingen


2. **Ta ut batteriet fra fjernkontrollen** før håndtering (fare for kortslutning og skade på komponenter)


3. **Sjekk at alle tilkoblinger er isolert** før du kobler til noe igjen


4. **Koble aldri til 220V** igjen før fjernkontrollboksen er lukket og sikret



Hvis du ikke er komfortabel med denne typen håndtering, bør du ta med deg noen som er det.



---

## DEL 1: Montering av maskinvare



### Trinn 1: Klargjøring av fjernkontrollen



Formål: Koble reléet til ON/OFF-knappen på fjernkontrollen


1. Åpne fjernkontrollen




    - Identifiser ON/OFF-knappen
    - Skru av kabinettet for å åpne fjernkontrollen


2. Finn forbindelser




 - Finn + og - terminalene på
 - Test kontinuiteten med et multimeter (valgfritt)



![smoke-machine-remote](assets/fr/8.webp)



3. Knappekabling (lodding eller kontakter)




    - Lodd en svart kabel til - terminalen på knappen
    - Lodd en rød kabel til den felles + terminalen



![smoke-machine-remote](assets/fr/9.webp)



### Trinn 2: Koble til relémodulen



**Påminnelse: Reléterminologi



| **Terminal**         | **Description**           | **Fonction**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (Normally Open)   | Circuit ouvert par défaut | Se ferme quand le relais est activé |
| NC (Normally Closed) | Circuit fermé par défaut  | S'ouvre quand le relais est activé  |
| COM (Common)         | Terminal central          | Bascule entre NO et NC              |

**Kablingen fra fjernkontrollen til relémodulen:**




- Svart ledning fra PÅ/AV-knappen **→** NO (normalt åpen)
- Rød ledning (felles) **→** COM (felles)



**Logikk:**


Når ESP32 aktiverer reléet, kobler den sammen COM og NO, noe som er nøyaktig det samme som å trykke på fjernkontrollknappen.


Når ESP32 kobler ut reléet, skilles COM og NO, noe som tilsvarer å slippe knappen.



![remote-relay](assets/fr/10.webp)



### Trinn 3: Koble ESP32 til relémodulen



**Koblingsskjema:**



| **ESP32** | **→** | **Module relais** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (Input)        |

**Verifikasjon:**




- VCC og GND godt tilkoblet (polaritet)
- GPIO 21 brukes til styresignal
- Ingen synlig kortslutning



![relay-esp32](assets/fr/11.webp)



**Checkpoint Hardware**


Før du bytter til programvaren, må du sjekke :




- Korrekt kablet fjernkontroll
- Relémodul koblet til ESP32
- Ingen blanke ledninger som berører andre komponenter
- 220V alltid frakoblet



![relay-esp32](assets/fr/12.webp)





---


## DEL 2: Konfigurasjon av programvare



Vi bruker *Blink* som et eksempel, men *BTCPay Server* tilbyr også *Strike, Breez og Boltz* hvis du foretrekker et annet alternativ.



### Trinn 1: Plugins, installasjon *BitcoinSwitch * + * Blink



1 - Gå til *BTCPay Server*-forekomsten din med en administratorkonto



2 - Lag din første persienne



3 - På venstre side av *BTCPay Server*, bla til bunnen og gå til *"Manage Plugins"*



![btcpay-plugins](assets/fr/13.webp)



4 - Vi kommer til å installere * BitcoinSwitch * plugins samt * Blink *



![btcpay-plugins](assets/fr/14.webp)



5 - Bla nedover listen over plugins og klikk på *"Installer"* : *BitcoinSwitch og Blink* (eller den tilgjengelige wallet etter eget valg)



![btcpay-plugins](assets/fr/15.webp)



6 - Når installasjonen er fullført, starter du *BTCPay Server* på nytt og venter 1 minutt på at instansen skal starte på nytt



![btcpay-plugins](assets/fr/16.webp)



7 - Når du går tilbake til *"Administrer plugins"*, sjekk at begge plugins er installert



![btcpay-plugins](assets/fr/17.webp)



### Trinn 2: Backend: *BTCPay Server + Blink* konfigurasjon



**1 - Opprett en wallet *Blink***




- Besøk https://www.blink.sv
- Opprett kontoen din. Vennligst se veiledningen :



[https://planb.academy/en/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd](https://planb.academy/en/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)



**2 - Generer en API-nøkkel *Blink***




- Gå til API-grensesnittet: **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** og logg inn med den samme kontoen som du brukte til å opprette wallet *Blink*



![blink-api](assets/fr/18.webp)





   - Når du er tilkoblet, går du til fanen *API Keys*



![blink-api](assets/fr/19.webp)





   - Klikk på *" + "* øverst i høyre hjørne for å få tilgang til konfigurasjonen av API-nøkkelen



![blink-api](assets/fr/20.webp)





   - Gi API-nøkkelen et navn, og la standardinnstillingene stå. I det tredje trinnet noterer du API-nøkkelen din - du vil bare se den én gang: `blink_mZ5KxxxxxxxxxxxxxxxxxNbmX`



![blink-api](assets/fr/21.webp)





   - Når den er opprettet, skal den vises i listen over aktive API-nøkler.



![blink-api](assets/fr/22.webp)



**3 - Koble *Blink* til *BTCPay Server***




- Åpne din *BTCPay-server*
- Naviger til : *Wallet* **→** *Lightning*



![btcpay-server](assets/fr/23.webp)





- Klikk på *Bruk en egendefinert node*
- Lim inn følgende tilkoblingsstreng:



```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```



**⚠️** **Viktig** :




- Ikke endre den første delen: `type=blink;server=https://api.blink.sv/graphql`;
- Erstatt kun :
    - api-key= *etter din API Blink*-nøkkel
    - wallet-id= *etter din wallet Blink* ID
- Klikk deretter på *Test tilkobling*, og deretter på *Lagre*



![btcpay-server](assets/fr/24.webp)





 - Kontroller at forbindelsen er opprettet (grønn status)



![btcpay-server](assets/fr/25.webp)



**4 - Opprett et salgssted (PoS)**




- I BTCPay Server går du til fanen *Plugins* og klikker på *Point of sale*



![btcpay-server](assets/fr/26.webp)





- Gi PoS-en din et navn, og klikk på *Opprett*



![btcpay-server](assets/fr/27.webp)





- PoS-konfigurasjon :
    - Velg en salgsstedstil = *Print display*
    - Valuta = *SATS*
    - Klikk på *SETT*



![btcpay-server](assets/fr/28.webp)





- Produktkonfigurasjon :
    - Slett alle standardprodukter
    - Klikk deretter på *legg til element*



![btcpay-server](assets/fr/29.webp)



![btcpay-server](assets/fr/30.webp)





- Konfigurer produktet:
    - Tittel : *røykmaskin*
    - Pris : *10 sats*
    - Bitcoin GPIO-bryter: 21
    - Bitcoin-bryterens varighet (i millisekunder) : 5000
    - Klikk på *Lukk* og deretter på *Lagre* for å lagre det nye produktet



![btcpay-server](assets/fr/31.webp)



### Trinn 3: Fastvare: Flashing av ESP32



**1 - Gå til flash-nettstedet




- Gå til : [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)



![bitcoinswitch-lnbits](assets/fr/32.webp)



**2 - Flash BitcoinSwitch-fastvaren**




- Koble ESP32 til datamaskinen med USB/Micro-USB-kabelen
- Klikk deretter på *Koble til enhet*
- Et vindu åpnes, velg USB-porten på ESP32, og klikk deretter på *Connect*



![bitcoinswitch-lnbits](assets/fr/33.webp)





- Når ESP32 er tilkoblet, flasher vi fastvaren til BitcoinSwitch. I delen *T-Display* klikker du på *Last opp fastvare* for den nyeste tilgjengelige versjonen (for øyeblikket: *bitcoinSwitch T-Display v1.0.1*)



![bitcoinswitch-lnbits](assets/fr/34.webp)





- Vent på opplastingen, prosessen er fullført når loggene viser *"Leaving... "*


![bitcoinswitch-lnbits](assets/fr/35.webp)





- Koble fra ESP32



**3 - Kontroller installasjonen av BitcoinSwitch-fastvare




- Last inn siden på nytt: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Koble ESP32 til datamaskinen igjen med USB/Micro-USB-kabelen
- Klikk deretter på *Koble til enhet
- Velg USB-porten på ESP32, og klikk deretter på *Connect* som beskrevet ovenfor
- Når du er tilkoblet, trykker du på **RESET**-knappen på ESP32
- Sjekk i loggene at de siste linjene viser :



```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```



(Dette er normalt, det betyr at det ikke er noen konfigurasjon ennå, men at fastvaren er installert)



![bitcoinswitch-lnbits](assets/fr/36.webp)



**4 - Generer WebSocket LNURL** URL



Forventet endelig format :



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



Genereringstrinn :




- ÅpneBTCPay Server-forekomsten din, og gå deretter til PoS-en vi opprettet senere.
- Klikk deretter på "Vis" for å åpne PoS i nettleseren



![btcpay-server-https](assets/fr/37.webp)





- Kopier URL-adressen til siden, for eksempel :



![btcpay-server-https](assets/fr/38.webp)



La oss pakke ut denne URL-en:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```





- `XXXXv` → domenet til BTCPay Server-forekomsten din
- `46XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXwFB` → din unike PoS-identifikator
- `/pos` → angir et utsalgssted



Forvandle den:




- Erstatt `https://` med `wss://`
- Legg til `/bitcoinswitch` på slutten



Resultat:



```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```



Ta vare på denne URL-en for fremtidig konfigurasjon, ettersom den vil gjøre det mulig for ESP32 å kommunisere i sanntid med BTCPay Server. WebSocket-protokollen (`wss://`) etablerer en permanent forbindelse mellom de to: Så snart en Lightning-betaling er bekreftet på PoS-en din, sender BTCPay øyeblikkelig informasjonen til ESP32, som deretter kan utløse røykmaskinen din.



**5 - Konfigurere WiFi og WebSocket




- Gå tilbake til siden: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/) med ESP32 tilkoblet
- Gå til *Konfigurer enhet* → *Wifi-innstillinger*



Informer :




- WiFi SSID: navnet på WiFi-nettverket ditt
- WiFi-passord: ditt WiFi-passord



![bitcoinswitch-lnbits](assets/fr/39.webp)





- Lim inn WebSocket-URL-en som ble opprettet i forrige trinn, i delen *LNbits Device URL*
- Klikk på *Last opp konfigurasjon*



![bitcoinswitch-lnbits](assets/fr/40.webp)





- Vent til opplastingen er fullført; loggene skal vise parameterne du nettopp har angitt (SSID, passord og WebSocket URL)



![bitcoinswitch-lnbits](assets/fr/41.webp)





- Vent mens ESP32 oppretter WebSocket-tilkoblingen. Du bør se :



```
WiFi connection established!

[WebSocket] Connected to url: ...
```



![bitcoinswitch-lnbits](assets/fr/42.webp)





- Du kan nå koble fra ESP32



---
## Checkpoint-programvare



Før den endelige testen, sjekk :





- Blink koblet til BTCPay
- PoS opprettet med minst 1 vare
- ESP32 flashet med BitcoinSwitch
- WiFi konfigurert på ESP32
- WebSocket URL korrekt
- Feilfrie ESP32-logger



---

## Testing og feilsøking



### Fullfør siste test



1. Koble til røykmaskinen (220V) og slå den på


2. Strømtilførsel til ESP32 (batteri eller USB)


3. Åpne BTCPay PoS i nettleseren din


4. Skann "røykmaskin" element


5. Betal med en wallet Lightning (Blink eller annen wallet)


6. Vær oppmerksom:




 - Reléet klikker (hørbar lyd og reléets LED-lampe lyser)
 - Røykmaskinen er aktivert
 - Røyk generert!



### Rettferdighetsproblemer og løsninger



| **Problème**                        | **Cause probable**              | **Solution**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 ne se connecte pas            | Driver USB manquant             | Installer [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| Relais ne clique pas                | Mauvais câblage GPIO            | Vérifier GPIO 21 → IN                                                                        |
| Smoke machine ne réagit pas         | Télécommande mal câblée         | Vérifier NO/NC/COM                                                                           |
| WebSocket timeout                   | URL incorrecte                  | Vérifier wss:// et /bitcoinswitch                                                            |
| WiFi ne se connecte pas             | SSID/Password erroné            | Re-flasher la config WiFi                                                                    |
| Paiement reçu mais rien ne se passe | ESP32 non connecté au WebSocket | Vérifier les logs RESET                                                                      |

## Ressurser



### Nyttige lenker





- BitcoinSwitch Firmware: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- BTCPay Server Docs : [https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- ESP32 Pinout : [https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)



### Fellesskap og støtte





- BTCPay Server** : [chat.btcpayserver.org](https://chat.btcpayserver.org/) - Official Mattermost
- BTCPay Server Telegram** : [t.me/btcpayserver](https://t.me/btcpayserver)
- LNbits** : [t.me/lnbits](https://t.me/lnbits) - Offisiell Telegram, aktivt fellesskap
- BitcoinSwitch (fastvarefeil)**: [github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)



### Kildekode





- BitcoinSwitch fastvare kildekode: [https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)



---

**⚡** Stable sats, lag røyk, ha det gøy, vær ydmyk! **⚡**