---
name: Lightning Smoke Machine
description: Utlös en rökmaskin med en Lightning-betalning via ESP32.
---

![cover-lightning-smoke-machine](assets/cover.webp)



## Inledning



Förvandlar en klassisk rökmaskin till en enhet som betalas i Bitcoin via Lightning Network. Varje betalning utlöser automatiskt en rökstråle!





- Nivå: Medelsvår
- Beräknad tid: 2-3 timmar
- Användningsfall: Bitcoin-evenemang, konstnärliga framträdanden, blixtdemonstrationer, automatiserade sceneffekter



## Förkunskapskrav



### Kunskap





 - Grundläggande elektronik (kablage, reläer)
 - Svetsning (eller användning av Dupont-anslutningar)
 - Nätverkskonfiguration (WiFi, WebSocket)



### Konton krävs





- BTCPay-server: Funktionell instans (självhostad eller hostad)
- Blink Wallet : Konto + åtkomst API



### Tillgång





- Admin-åtkomst till BTCPay Server
- WiFi-anslutning för ESP32



## Material som krävs



### Hårdvara - Elektroniska komponenter





- 1 Mikrokontroller - ESP32-WROOM-32


*ESP32-WROOM-32 är en kompakt och prisvärd WiFi-/Bluetooth-mikrokontroller för anslutning av elektroniska enheter till internet och fjärrstyrning av dem*



![ESP32](assets/fr/1.webp)





- 1 Relämodul - 5V med optokopplare


*Ett relä är som en strömbrytare som ESP32 kan styra för att sätta på eller stänga av rökmaskinen*



![relay](assets/fr/2.webp)





- ~10 Dupont-kablar - hane/hane och hane/hane



![dupont-cables](assets/fr/3.webp)





- 1 Strömförsörjning för ESP32 - 5V USB eller Li-Po-batteri



![battery](assets/fr/4.webp)





- 1 mikro-USB-kabel - anslutning mellan ESP32 och strömförsörjningen



![micro-usb-cables](assets/fr/5.webp)





- 1 220V dimmaskin med fjärrkontroll för 12V-batteri



![remote-and-smoke-machine](assets/fr/6.webp)





- 1 flaska vätska som är kompatibel med din rökmaskin



### Hårdvara - Verktyg





- Lödkolv + tenn (vid lödning)
- Skruvmejsel
- Multimeter (rekommenderas)



### Programvara





- Firmware BitcoinSwitch : **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- WebSerial-kompatibel webbläsare (Chrome/Edge/Brave)
- BTCPay Server konfigurerad. För mer information om hur du skapar en BTCPay Server-instans, besök denna handledning: https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc



## Systemarkitektur



![architecture-lightning-smoke-machine](assets/fr/7.webp)



---


**⚠️** **SÄKERHETSINFORMATION - LÄS INNAN DU FORTSÄTTER** **⚠️**



Detta projekt omfattar en dimmaskin som är ansluten till en **220V nätspänning**. Felaktig användning kan leda till **dödlig elstöt** eller **brand**.



**Icke förhandlingsbara regler:**



1. **koppla ALLTID bort rökmaskinen från elnätet** innan du öppnar fjärrkontrollen eller manipulerar kablarna


2. **Ta ut batteriet ur fjärrkontrollen** före hantering (risk för kortslutning och skador på komponenter)


3. **Kontrollera att alla anslutningar är isolerade** innan du ansluter något igen


4. **Återanslut aldrig 220V** förrän fjärrkontrollen har stängts och säkrats



Om du inte är bekväm med den här typen av hantering, ta med dig någon som är det.



---

## DEL 1: Montering av hårdvara



### Steg 1: Förbereda fjärrkontrollen



Målsättning: Anslut reläet till ON/OFF-knappen på fjärrkontrollen


1. Öppna fjärrkontrollen




    - Identifiera ON/OFF-knappen
    - Skruva loss höljet för att öppna fjärrkontrollen


2. Lokalisera anslutningar




 - Leta reda på + och - polerna på
 - Testa kontinuiteten med en multimeter (tillval)



![smoke-machine-remote](assets/fr/8.webp)



3. Kabeldragning för knappar (lödning eller kontakter)




    - Löd en svart kabel till knappens -terminal
    - Löd en röd kabel till den gemensamma + terminalen



![smoke-machine-remote](assets/fr/9.webp)



### Steg 2: Anslutning till relämodulen



**Påminnelse: Terminologi för reläer



| **Terminal**         | **Description**           | **Fonction**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (Normally Open)   | Circuit ouvert par défaut | Se ferme quand le relais est activé |
| NC (Normally Closed) | Circuit fermé par défaut  | S'ouvre quand le relais est activé  |
| COM (Common)         | Terminal central          | Bascule entre NO et NC              |

**Kabeldragning från fjärrkontroll till relämodul:**




- Svart ledning från ON/OFF-knappen **→** NO (normalt öppen)
- Röd tråd (gemensam) **→** COM (gemensam)



**Logik:**


När ESP32 aktiverar reläet kopplar den ihop COM och NO, vilket är exakt samma sak som att trycka på fjärrkontrollens knapp.


När ESP32 slår av reläet separeras COM och NO, vilket motsvarar att släppa knappen.



![remote-relay](assets/fr/10.webp)



### Steg 3: Ansluta ESP32 till relämodulen



**Kopplingsschema:**



| **ESP32** | **→** | **Module relais** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (Input)        |

**Verifiering:**




- VCC och GND väl anslutna (polaritet)
- GPIO 21 används för styrsignal
- Ingen synlig kortslutning



![relay-esp32](assets/fr/11.webp)



**Checkpoint hårdvara**


Innan du byter till programvaran, kontrollera :




- Korrekt ansluten fjärrkontroll
- Relämodul ansluten till ESP32
- Inga nakna kablar som vidrör andra komponenter
- 220V alltid bortkopplad



![relay-esp32](assets/fr/12.webp)





---


## DEL 2: Konfiguration av programvara



Vi använder *Blink* som ett exempel, men *BTCPay Server* erbjuder också *Strike, Breez och Boltz* om du föredrar ett annat alternativ.



### Steg 1: Plugins, installation *BitcoinSwitch* + *Blink



1 - Gå till din *BTCPay Server*-instans med ett administratörskonto



2 - Skapa din första persienn



3 - På vänster sida av *BTCPay Server*, bläddra till botten och gå till *"Manage Plugins"*



![btcpay-plugins](assets/fr/13.webp)



4 - Vi kommer att installera * BitcoinSwitch * plugins samt * Blink *



![btcpay-plugins](assets/fr/14.webp)



5 - Bläddra ner i listan över plugins och klicka på *"Installera"* : *BitcoinSwitch och Blink* (eller den tillgängliga wallet som du väljer)



![btcpay-plugins](assets/fr/15.webp)



6 - När installationen är klar startar du om *BTCPay Server* och väntar 1 minut på att instansen ska starta om



![btcpay-plugins](assets/fr/16.webp)



7 - När du återvänder till *"Hantera plugins"*, kontrollera att båda plugins har installerats



![btcpay-plugins](assets/fr/17.webp)



### Steg 2: Backend: *BTCPay Server + Blink* konfiguration



**1 - Skapa en wallet *Blink***




- Besök https://www.blink.sv
- Skapa ditt konto. Vänligen se handledningen :



[https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)



**2 - Generera en API-nyckel *Blink***




- Gå till gränssnittet för API: **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** och logga in med samma konto som du använde för att skapa din wallet *Blink*



![blink-api](assets/fr/18.webp)





   - När du är ansluten går du till fliken *API Keys*



![blink-api](assets/fr/19.webp)





   - Klicka på *" + "* i det övre högra hörnet för att komma åt konfigurationen av din API-nyckel



![blink-api](assets/fr/20.webp)





   - Ge din API Key ett namn och lämna standardinställningarna. I det tredje steget noterar du sedan din API-nyckel - du ser den bara en gång: `blink_mZ5KxxxxxxxxxxxxxNbmX`



![blink-api](assets/fr/21.webp)





   - När den har skapats bör den visas i din aktiva API Key-lista.



![blink-api](assets/fr/22.webp)



**3 - Anslut *Blink* till *BTCPay Server***




- Öppna din *BTCPay Server*
- Navigera till : *Wallet* **→** *Blixt*



![btcpay-server](assets/fr/23.webp)





- Klicka på *Använd en anpassad nod*
- Klistra in följande anslutningssträng:



```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```



**⚠️** **Viktigt** :




- Modifiera inte den första delen: `type=blink;server=https://api.blink.sv/graphql`;
- Byt endast ut :
    - api-nyckel= *med din API Blink* nyckel
    - wallet-id= *med ditt wallet Blink* ID
- Klicka sedan på *Testa anslutningen* och sedan på *Spara*



![btcpay-server](assets/fr/24.webp)





 - Kontrollera att anslutningen är upprättad (grön status)



![btcpay-server](assets/fr/25.webp)



**4 - Skapa ett försäljningsställe (PoS)




- I BTCPay Server går du till fliken * Plugins* och klickar på *Point of sale*



![btcpay-server](assets/fr/26.webp)





- Ge din PoS ett namn och klicka på *Create*



![btcpay-server](assets/fr/27.webp)





- PoS-konfiguration :
    - Välj ett försäljningsställe = *Print display*
    - Valuta = *SATS*
    - Klicka på *SAVE*



![btcpay-server](assets/fr/28.webp)





- Produktkonfiguration :
    - Ta bort alla standardprodukter
    - Klicka sedan på *lägg till artikel*



![btcpay-server](assets/fr/29.webp)



![btcpay-server](assets/fr/30.webp)





- Konfigurera produkten:
    - Titel : *rökmaskin*
    - Pris : *10 sats*
    - Bitcoin GPIO-omkopplare : 21
    - Bitcoin växlingens varaktighet (i millisekunder) : 5000
    - Klicka på *Close* och sedan på *Save* för att spara den nya produkten



![btcpay-server](assets/fr/31.webp)



### Steg 3: Firmware: Flasha ESP32



**1 - Gå till flash-webbplatsen




- Gå till : [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)



![bitcoinswitch-lnbits](assets/fr/32.webp)



**2 - Flash firmware för BitcoinSwitch**




- Anslut ESP32 till datorn med en USB/Micro-USB-kabel
- Klicka sedan på * Anslut till enhet*
- Ett fönster öppnas, välj USB-porten på din ESP32 och klicka sedan på *Connect*



![bitcoinswitch-lnbits](assets/fr/33.webp)





- När din ESP32 är ansluten ska vi flasha BitcoinSwitch firmware. I avsnittet *T-Display* klickar du på *Upload Firmware* för den senaste tillgängliga versionen (för närvarande: *bitcoinSwitch T-Display v1.0.1*)



![bitcoinswitch-lnbits](assets/fr/34.webp)





- Vänta på uppladdningen, processen är klar när loggarna visar *"Leaving... "*


![bitcoinswitch-lnbits](assets/fr/35.webp)





- Koppla ur ESP32



**3 - Kontrollera installation av firmware för BitcoinSwitch




- Ladda om sidan: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Anslut ESP32 till datorn igen med USB/Micro-USB-kabeln
- Klicka sedan på * Anslut till enhet
- Välj USB-porten på din ESP32 och klicka sedan på *Connect* enligt beskrivningen ovan
- När du har anslutit trycker du på **RESET**-knappen på ESP32
- Kontrollera i loggarna att de sista raderna visar :



```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```



(Detta är normalt, det betyder att det inte finns någon konfiguration ännu, men att den fasta programvaran har installerats)



![bitcoinswitch-lnbits](assets/fr/36.webp)



**4 - Generera WebSocket LNURL** URL



Förväntat slutligt format :



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



Generationssteg :




- Öppna dinBTCPay Server-instans och gå sedan till PoS som vi skapade senare.
- Klicka sedan på "Visa" för att öppna din PoS i webbläsaren



![btcpay-server-https](assets/fr/37.webp)





- Kopiera webbadressen till sidan, till exempel :



![btcpay-server-https](assets/fr/38.webp)



Låt oss packa upp den här URL:en:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```





- `XXXXv` → domänen för din BTCPay Server-instans
- `46XXXXXXXXXXXXXXXXXXXXXXwFB` → din unika PoS-identifierare
- `/pos` → anger ett försäljningsställe



Förvandla den:




- Ersätt `https://` med `wss://`
- Lägg till `/bitcoinswitch` i slutet



Resultat:



```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```



Spara den här webbadressen för framtida konfiguration, eftersom den gör det möjligt för din ESP32 att kommunicera i realtid med BTCPay Server. WebSocket-protokollet (`wss://`) upprättar en permanent anslutning mellan de två: så snart en Lightning-betalning bekräftas på din PoS skickar BTCPay omedelbart informationen till ESP32, som sedan kan utlösa din rökmaskin.



**5 - Konfigurera WiFi och WebSocket




- Gå tillbaka till sidan: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/) med din ESP32 ansluten
- Gå till *Konfigurera enhet* → *Wifi-inställningar*



Informera :




- WiFi SSID: namnet på ditt WiFi-nätverk
- WiFi-lösenord: ditt WiFi-lösenord



![bitcoinswitch-lnbits](assets/fr/39.webp)





- I avsnittet *LNbits Device URL* klistrar du in URL:en för WebSocket som skapades i föregående steg
- Klicka på *Ladda upp konfiguration*



![bitcoinswitch-lnbits](assets/fr/40.webp)





- Vänta tills uppladdningen är klar; loggarna bör visa de parametrar som du just angav (SSID, lösenord och WebSocket URL)



![bitcoinswitch-lnbits](assets/fr/41.webp)





- Vänta medan ESP32 upprättar WebSocket-anslutningen. Du bör se :



```
WiFi connection established!

[WebSocket] Connected to url: ...
```



![bitcoinswitch-lnbits](assets/fr/42.webp)





- Du kan nu koppla bort ESP32



---
## Checkpoint programvara



Före det slutliga testet, kontrollera :





- Blink ansluten till BTCPay
- PoS skapad med minst 1 föremål
- ESP32 flashad med BitcoinSwitch
- WiFi konfigurerat på ESP32
- WebSocket URL korrekt
- Felfria ESP32-loggar



---

## Testning och felsökning



### Slutföra slutprov



1. Koppla in rökmaskinen (220V) och slå på den


2. Strömförsörjning till ESP32 (batteri eller USB)


3. Öppna din BTCPay PoS i din webbläsare


4. Skanna objektet "rökmaskin"


5. Betala med en wallet Lightning (Blink eller annan wallet)


6. Observera:




 - Reläet klickar (hörbart ljud och reläets LED-lampa tänds)
 - Rökmaskinen är aktiverad
 - Rökutveckling!



### Rättviseproblem och lösningar



| **Problème**                        | **Cause probable**              | **Solution**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 ne se connecte pas            | Driver USB manquant             | Installer [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| Relais ne clique pas                | Mauvais câblage GPIO            | Vérifier GPIO 21 → IN                                                                        |
| Smoke machine ne réagit pas         | Télécommande mal câblée         | Vérifier NO/NC/COM                                                                           |
| WebSocket timeout                   | URL incorrecte                  | Vérifier wss:// et /bitcoinswitch                                                            |
| WiFi ne se connecte pas             | SSID/Password erroné            | Re-flasher la config WiFi                                                                    |
| Paiement reçu mais rien ne se passe | ESP32 non connecté au WebSocket | Vérifier les logs RESET                                                                      |

## Resurser



### Användbara länkar





- Firmware för BitcoinSwitch: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Dokument för BTCPay-server : [https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- ESP32 Pinout : [https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)



### Gemenskap & stöd





- BTCPay Server** : [chat.btcpayserver.org](https://chat.btcpayserver.org/) - Officiell Mattermost
- BTCPay-server Telegram** : [t.me/btcpayserver](https://t.me/btcpayserver)
- LNbits** : [t.me/lnbits](https://t.me/lnbits) - Officiell Telegram, aktiv gemenskap
- BitcoinSwitch (buggar i firmware)**: [github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)



### Källkod





- BitcoinSwitch firmware källkod: [https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)



---

**⚡** Stapla sats, rök, ha kul, var ödmjuk! **⚡**