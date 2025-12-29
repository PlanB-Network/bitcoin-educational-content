---
name: Lightning Smoke Machine
description: Pokreni dim mašinu putem Lightning uplate preko ESP32.
---

![cover-lightning-smoke-machine](assets/cover.webp)



## Uvod



Pretvara klasičnu dim mašinu u uređaj koji se plaća u Bitcoin putem Lightning Network. Svaka uplata automatski pokreće mlaz dima!





- Nivo: Srednji
- Procenjeno vreme: 2-3 sata
- Slučajevi upotrebe: Bitcoin događaji, umetnički performansi, Lightning demonstracije, automatizovani scenski efekti



## Preduslovi



### Znanje





 - Osnovna elektronika (ožičenje, releji)
 - Zavarivanje (ili korišćenje Dupont konektora)
 - Konfiguracija mreže (WiFi, WebSocket)



### Nalozi potrebni





- BTCPay Server: Funkcionalna instanca (samohostovana ili hostovana)
- Blink Wallet : Account + access API



### Pristup





- Administratorski pristup BTCPay Serveru
- WiFi veza za ESP32



## Potrebni materijali



### Hardver - Elektronske komponente





- 1 Mikrokontroler - ESP32-WROOM-32


*ESP32-WROOM-32 je kompaktan, niskobudžetni WiFi/Bluetooth mikrokontroler za povezivanje elektronskih uređaja na Internet i njihovo daljinsko upravljanje*



![ESP32](assets/fr/1.webp)





- 1 Relej modul - 5V sa optokaplerom


*Relej je kao prekidač koji ESP32 može da upravlja kako bi uključio ili isključio mašinu za dim*



![relay](assets/fr/2.webp)





- ~10 Dupont kablova - Muški/Muški i Muški/Ženski



![dupont-cables](assets/fr/3.webp)





- 1 Napajanje za ESP32 - 5V USB ili Li-Po baterija



![battery](assets/fr/4.webp)





- 1 mikro-USB kabl - veza između ESP32 i napajanja



![micro-usb-cables](assets/fr/5.webp)





- 1 mašina za maglu 220V sa daljinskim upravljačem na baterije 12V



![remote-and-smoke-machine](assets/fr/6.webp)





- 1 boca tečnosti kompatibilne sa vašom dim mašinom



### Hardver - Alati





- Lemilica + kalaj (ako se lemí)
- Šrafciger
- Multimetar (preporučeno)



### Softver





- Firmware BitcoinSwitch : **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- WebSerial-kompatibilan veb pregledač (Chrome/Edge/Brave)
- BTCPay Server konfigurisan. Za više informacija o kreiranju instance BTCPay Server-a, posetite ovaj tutorijal: https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc



## Arhitektura sistema



![architecture-lightning-smoke-machine](assets/fr/7.webp)



---


**⚠️** **UPOZORENJE O BEZBEDNOSTI - PROČITAJTE PRE NEGO ŠTO NASTAVITE** **⚠️**



Ovaj projekat uključuje mašinu za maglu povezanu na **220V mrežno napajanje**. Nepravilno rukovanje može dovesti do **smrtonosnog strujnog udara** ili **požara**.



**Neprikosnovena pravila:**



1. **UVEK isključite dim mašinu iz struje** pre nego što otvorite daljinski upravljač ili dirate ožičenje


2. **Uklonite bateriju iz daljinskog upravljača** pre nego što počnete sa rukovanjem (rizik od kratkog spoja i oštećenja komponenti)


3. **Proverite da su sve vaše veze izolovane** pre nego što ponovo povežete bilo šta


4. **Nikada ne povezujte 220V** dok se kutija daljinskog upravljača ne zatvori i osigura



Ako ti nije prijatno da se nosiš sa ovakvom situacijom, povedi nekoga ko jeste.



---

## DEO 1: Sklapanje hardvera



### Korak 1: Priprema daljinskog upravljača



Cilj: Povežite relej sa ON/OFF dugmetom na daljinskom upravljaču


1. Otvori daljinski upravljač




    - Identifikujte dugme UKLJUČENO/ISKLJUČENO
    - Odvijte kućište da biste otvorili daljinski upravljač.


2. Pronađite veze




 - Pronađite + i - terminale od
 - Testirajte kontinuitet pomoću multimetra (opciono)



![smoke-machine-remote](assets/fr/8.webp)



3. Ožičenje dugmeta (lemljenje ili konektori)




    - Zalemi crni kabl na - terminal dugmeta
    - Zalemi crveni kabl na zajednički + terminal



![smoke-machine-remote](assets/fr/9.webp)



### Korak 2: Povezivanje sa relejnim modulom



**Podsetnik: Terminologija releja



| **Terminal**         | **Description**           | **Fonction**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (Normally Open)   | Circuit ouvert par défaut | Se ferme quand le relais est activé |
| NC (Normally Closed) | Circuit fermé par défaut  | S'ouvre quand le relais est activé  |
| COM (Common)         | Terminal central          | Bascule entre NO et NC              |

**Ožičenje od daljinskog upravljača do relejnog modula:**




- Crna žica od ON/OFF dugmeta **→** NO (Normalno Otvoren)
- Crvena žica (zajednička) **→** COM (Zajednička)



**Logika:**


Kada ESP32 aktivira relej, povezuje COM i NO, što je potpuno isto kao pritiskanje dugmeta na daljinskom upravljaču.


Kada ESP32 isključi relej, COM i NO se razdvajaju, što je ekvivalentno otpuštanju dugmeta.



![remote-relay](assets/fr/10.webp)



### Korak 3: Povezivanje ESP32 sa relejnim modulom



**Dijagram ožičenja:**



| **ESP32** | **→** | **Module relais** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (Input)        |

**Verifikacija:**




- VCC i GND dobro povezani (polaritet)
- GPIO 21 koristi se za kontrolni signal
- Nema vidljivog kratkog spoja



![relay-esp32](assets/fr/11.webp)



**Kontrolna tačka Hardver**


Pre nego što pređete na softver, proverite :




- Ispravno povezan daljinski upravljač
- Relej modul povezan sa ESP32
- Nema golih žica koje dodiruju druge komponente
- 220V uvek isključen



![relay-esp32](assets/fr/12.webp)





---


## DEO 2: Konfiguracija softvera



Koristićemo *Blink* kao primer, ali *BTCPay Server* takođe nudi *Strike, Breez i Boltz* ako više volite drugu opciju.



### Korak 1: Dodaci, Instalacija *BitcoinSwitch* + *Blink



1 - Idite na svoju instancu *BTCPay Server* sa administratorskim nalogom



2 - Kreirajte svoj prvi blind



3 - Na levoj strani *BTCPay Server*-a, skroluj do dna i idi na *"Manage Plugins "*



![btcpay-plugins](assets/fr/13.webp)



4 - Instaliraćemo dodatke *BitcoinSwitch* kao i *Blink*



![btcpay-plugins](assets/fr/14.webp)



5 - Skrolujte niz listu dodataka i kliknite na *"Instaliraj "* : *BitcoinSwitch i Blink* (ili dostupni wallet po vašem izboru)



![btcpay-plugins](assets/fr/15.webp)



6 - Kada je instalacija završena, restartujte *BTCPay Server* i sačekajte 1 minut da se instanca ponovo pokrene.



![btcpay-plugins](assets/fr/16.webp)



7 - Kada se vratite na *"Manage plugins"*, proverite da su oba dodatka instalirana



![btcpay-plugins](assets/fr/17.webp)



### Korak 2: Backend : *BTCPay Server + Blink* konfiguracija



**1 - Kreiraj wallet *Blink***




- Posetite https://www.blink.sv
- Kreirajte svoj nalog. Molimo vas da pogledate tutorijal :



[https://planb.academy/en/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd](https://planb.academy/en/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)



**2 - Generiši API ključ *Blink***




- Pristupite API interfejsu: **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** i prijavite se sa istim nalogom koji ste koristili za kreiranje vašeg wallet *Blink*



![blink-api](assets/fr/18.webp)





   - Jednom kada se povežete, idite na karticu *API Keys*



![blink-api](assets/fr/19.webp)





   - Kliknite na *" + "* u gornjem desnom uglu da pristupite konfiguraciji vašeg API ključa.



![blink-api](assets/fr/20.webp)





   - Dajte svom API ključu ime i ostavite podrazumevana podešavanja. Zatim, u trećem koraku, zabeležite svoj API ključ - videćete ga samo jednom: `blink_mZ5KxxxxxxxxxxxxxNbmX`



![blink-api](assets/fr/21.webp)





   - Jednom kada je kreiran, trebao bi se pojaviti na vašoj listi aktivnih API ključeva.



![blink-api](assets/fr/22.webp)



**3 - Poveži *Blink* sa *BTCPay Serverom***




- Otvorite svoj *BTCPay Server*
- Navigiraj do : *Wallet* **→** *Lightning*



![btcpay-server](assets/fr/23.webp)





- Kliknite na *Koristi prilagođeni čvor*
- Nalepite sledeći niz za povezivanje:



```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```



**⚠️** **Važno** :




- Ne menjajte prvi deo: `type=blink;server=https://api.blink.sv/graphql`;
- Zameni samo :
    - api-key= *by your API Blink* key
    - wallet-id= *by your wallet Blink* ID
- Zatim kliknite na *Testiraj vezu*, zatim *Sačuvaj*



![btcpay-server](assets/fr/24.webp)





 - Proverite da je veza uspostavljena (zeleni status)



![btcpay-server](assets/fr/25.webp)



**4 - Kreirajte prodajno mesto (PoS)**




- U BTCPay Serveru, idite na karticu *Plugins* i kliknite na *Point of sale*



![btcpay-server](assets/fr/26.webp)





- Dajte svom PoS-u ime i kliknite na *Create*



![btcpay-server](assets/fr/27.webp)





- PoS konfiguracija :
    - Izaberite stil prodajnog mesta = *Prikaz za štampu*
    - Valuta = *SATS*
    - Kliknite na *SAVE*



![btcpay-server](assets/fr/28.webp)





- Konfiguracija proizvoda :
    - Izbriši sve podrazumevane proizvode
    - Zatim kliknite na *add item*



![btcpay-server](assets/fr/29.webp)



![btcpay-server](assets/fr/30.webp)





- Konfiguriši proizvod:
    - Naslov : *smoke-machine*
    - Cena : *10 sats*
    - Bitcoin GPIO prekidač : 21
    - Bitcoin trajanje preklopa (u milisekundama) : 5000
    - Kliknite na *Close* i zatim *Save* da sačuvate novi proizvod



![btcpay-server](assets/fr/31.webp)



### Korak 3: Firmware: Flashovanje ESP32



**1 - Idi na flash sajt




- Idi na : [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)



![bitcoinswitch-lnbits](assets/fr/32.webp)



**2 - Flash the BitcoinSwitch firmware**




- Povežite ESP32 sa računarom pomoću USB/Micro-USB kabla
- Zatim kliknite na *Connect to Device*
- Otvara se prozor, izaberite USB port na vašem ESP32, zatim kliknite na *Connect*



![bitcoinswitch-lnbits](assets/fr/33.webp)





- Jednom kada je vaš ESP32 povezan, prebacićemo BitcoinSwitch firmware. U odeljku *T-Display*, kliknite na *Upload Firmware* za najnoviju dostupnu verziju (trenutno: *bitcoinSwitch T-Display v1.0.1*)



![bitcoinswitch-lnbits](assets/fr/34.webp)





- Sačekajte da se učitavanje završi, proces je kompletan kada logovi pokažu *"Leaving... "*


![bitcoinswitch-lnbits](assets/fr/35.webp)





- Isključite ESP32



**3 - Proveri instalaciju BitcoinSwitch firmvera




- Ponovo učitaj stranicu: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Ponovo povežite ESP32 sa računarom pomoću USB/Micro-USB kabla.
- Zatim kliknite na *Connect to device
- Odaberite USB port na vašem ESP32, zatim kliknite na *Connect* kao što je opisano iznad.
- Kada se povežete, pritisnite dugme **RESET** na ESP32
- Proveri u zapisima da poslednje linije pokazuju :



```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```



(Ovo je normalno, to znači da još uvek nema konfiguracije, ali da je firmware instaliran)



![bitcoinswitch-lnbits](assets/fr/36.webp)



**4 - Generiši WebSocket LNURL** URL



Očekivani konačni format :



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



Koraci generacije :




- Otvorite svoju instance BTCPay Server-a, zatim idite na PoS koji smo kasnije kreirali.
- Zatim kliknite na "View" da otvorite svoj PoS u pregledaču



![btcpay-server-https](assets/fr/37.webp)





- Kopiraj URL stranice, na primer :



![btcpay-server-https](assets/fr/38.webp)



Hajde da analiziramo ovaj URL:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```





- `XXXXv` → domen vašeg BTCPay Server instance
- `46XXXXXXXXXXXXXXXXXXXXwFB` → vaš jedinstveni PoS identifikator
- `/pos` → označava prodajno mesto



Transformiši to:




- Zameni `https://` sa `wss://`
- Dodaj `/bitcoinswitch` na kraj



Rezultat:



```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```



Sačuvaj ovaj URL za buduću konfiguraciju, jer će omogućiti tvom ESP32 da komunicira u realnom vremenu sa BTCPay Serverom. WebSocket protokol (`wss://`) uspostavlja stalnu vezu između njih: čim je Lightning uplata potvrđena na tvom PoS-u, BTCPay odmah šalje informaciju ESP32, koji zatim može aktivirati tvoju dim mašinu.



**5 - Konfigurisanje WiFi i WebSocket




- Vratite se na stranicu: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/) sa vašim ESP32 povezanim
- Idite na *Configure Device* → *Wifi Settings*



Informi :




- WiFi SSID: ime vaše WiFi mreže
- WiFi Password: your WiFi password



![bitcoinswitch-lnbits](assets/fr/39.webp)





- U odeljku *LNbits Device URL* nalepite WebSocket URL kreiran u prethodnom koraku.
- Kliknite na *Upload config*



![bitcoinswitch-lnbits](assets/fr/40.webp)





- Sačekajte da se otpremanje završi; dnevnici bi trebalo da prikažu parametre koje ste upravo uneli (SSID, lozinka i WebSocket URL)



![bitcoinswitch-lnbits](assets/fr/41.webp)





- Sačekajte dok ESP32 uspostavi WebSocket vezu. Trebalo bi da vidite:



```
WiFi connection established!

[WebSocket] Connected to url: ...
```



![bitcoinswitch-lnbits](assets/fr/42.webp)





- Sada možete isključiti ESP32



---
## Checkpoint Software



Pre nego što konačni test, proveri :





- Blink povezan sa BTCPay
- PoS kreiran sa najmanje 1 stavkom
- ESP32 flešovan sa BitcoinSwitch
- WiFi konfigurisano na ESP32
- WebSocket URL tačan
- ESP32 dnevnici bez grešaka



---

## Testiranje i otklanjanje grešaka



### Završni test kompletiran



1. Priključite mašinu za dim (220V) i uključite je.


2. Napajanje ESP32 (baterija ili USB)


3. Otvorite svoj BTCPay PoS u pregledaču


4. Skeniraj stavku "smoke-machine"


5. Platite sa wallet Lightning (Blink ili drugi wallet)


6. Posmatraj:




 - Klikovi releja (čujni zvuk i LED svetlo releja se pali)
 - Mašina za dim je aktivirana
 - Dim se dim!



### Problemi pravičnosti i rešenja



| **Problème**                        | **Cause probable**              | **Solution**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 ne se connecte pas            | Driver USB manquant             | Installer [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| Relais ne clique pas                | Mauvais câblage GPIO            | Vérifier GPIO 21 → IN                                                                        |
| Smoke machine ne réagit pas         | Télécommande mal câblée         | Vérifier NO/NC/COM                                                                           |
| WebSocket timeout                   | URL incorrecte                  | Vérifier wss:// et /bitcoinswitch                                                            |
| WiFi ne se connecte pas             | SSID/Password erroné            | Re-flasher la config WiFi                                                                    |
| Paiement reçu mais rien ne se passe | ESP32 non connecté au WebSocket | Vérifier les logs RESET                                                                      |

## Resursi



### Korisni linkovi





- BitcoinSwitch Firmware: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- BTCPay Server Dokumentacija : [https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- ESP32 Pinout : [https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)



### Zajednica i podrška





- BTCPay Server** : [chat.btcpayserver.org](https://chat.btcpayserver.org/) - Zvanični Mattermost
- BTCPay Server Telegram** : [t.me/btcpayserver](https://t.me/btcpayserver)
- LNbits** : [t.me/lnbits](https://t.me/lnbits) - Zvanična Telegram, aktivna zajednica
- BitcoinSwitch (firmware greške)**: [github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)



### Izvorni kod





- Izvorni kod za BitcoinSwitch firmware: [https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)



---

**⚡** Stack sats, napravi dim, zabavi se, ostani skroman! **⚡**