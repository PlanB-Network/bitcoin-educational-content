---
name: Lightning Smoke Machine
description: Käynnistä savukone salamamaksulla ESP32:n kautta.
---

![cover-lightning-smoke-machine](assets/cover.webp)



## Johdanto



Muuttaa klassisen savukoneen Lightning Network:n kautta Bitcoin:ssa maksettavaksi laitteeksi. Jokainen maksu laukaisee automaattisesti savusuihkun!





- Taso: Keskitaso
- Arvioitu aika: 2-3 tuntia
- Käyttötapaukset: Bitcoin-tapahtumat, taiteelliset esitykset, salamademot, automatisoidut lavatehosteet



## Edellytykset



### Tieto





 - Peruselektroniikka (johdotukset, releet)
 - Hitsaus (tai Dupont-liittimien käyttö)
 - Verkkokonfigurointi (WiFi, WebSocket)



### Tarvittavat tilit





- BTCPay-palvelin: (itse isännöity tai isännöity)
- Blink Wallet : Tili + pääsy API



### Pääsy





- Pääkäyttäjän pääsy BTCPay-palvelimelle
- WiFi yhteys ESP32:lle



## Tarvittavat materiaalit



### Laitteisto - Elektroniset komponentit





- 1 mikrokontrolleri - ESP32-WROOM-32


*ESP32-WROOM-32 on kompakti ja edullinen WiFi/Bluetooth-mikrokontrolleri elektronisten laitteiden liittämiseen Internetiin ja niiden etähallintaan*



![ESP32](assets/fr/1.webp)





- 1 Relemoduuli - 5V optoerottimella varustettuna


*Rele on kuin kytkin, jota ESP32 voi käyttää kytkemään savukoneen päälle tai pois päältä*



![relay](assets/fr/2.webp)





- ~10 Dupont-kaapelia - uros/uros ja uros/naaras



![dupont-cables](assets/fr/3.webp)





- 1 Virtalähde ESP32:lle - 5V USB tai Li-Po akku



![battery](assets/fr/4.webp)





- 1 mikro-USB-kaapeli - ESP32:n ja virtalähteen välinen yhteys



![micro-usb-cables](assets/fr/5.webp)





- 1 220V sumukone 12V paristokaukosäätimellä varustettuna



![remote-and-smoke-machine](assets/fr/6.webp)





- 1 pullo savukoneen kanssa yhteensopivaa nestettä



### Laitteisto - Työkalut





- Juotosrauta + tina (jos juottaminen)
- Ruuvimeisseli
- Yleismittari (suositellaan)



### Ohjelmisto





- Firmware BitcoinSwitch : **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- WebSerial-yhteensopiva verkkoselain (Chrome/Edge/Brave)
- BTCPay-palvelin määritetty. Lisätietoja BTCPay Server -palvelimen luomisesta saat tästä ohjeesta: https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc



## Järjestelmän arkkitehtuuri



![architecture-lightning-smoke-machine](assets/fr/7.webp)



---


**⚠️** **TURVALLISUUSVAROITUS - LUE ENNEN JATKAMISTA** **⚠️**



Tässä hankkeessa on kyse sumulaitteesta, joka on kytketty **220 V:n verkkovirtaan**. Vääränlainen käyttö voi johtaa **kuolemaan johtavaan sähköiskuun** tai **paloon**.



**Säännöt, joista ei voida neuvotella:**



1. **KATKAISE AINA savukone sähköverkosta** ennen kaukosäätimen avaamista tai johdotuksen peukalointia


2. **Poista paristo kaukosäätimestä** ennen sen käsittelyä (oikosulun ja komponenttien vaurioitumisen vaara)


3. **Tarkista, että kaikki yhteydet on eristetty** ennen kuin kytket mitään uudelleen


4. **Älä koskaan kytke 220V** uudelleen, ennen kuin kaukosäätimen laatikko on suljettu ja kiinnitetty



Jos tällainen käsittely ei ole sinulle tuttua, ota mukaan joku, joka osaa.



---

## OSA 1: Laitteiston kokoonpano



### Vaihe 1: Kaukosäätimen valmistelu



Tavoite: Kytke rele kaukosäätimen ON/OFF-painikkeeseen


1. Avaa kaukosäädin




    - Tunnista ON/OFF-painike
    - Avaa kaukosäädin ruuvaamalla kotelo auki


2. Paikanna yhteydet




 - Paikanna + ja - liitännät laitteen
 - Testaa jatkuvuus yleismittarilla (valinnainen)



![smoke-machine-remote](assets/fr/8.webp)



3. Painikkeen johdotus (juotos tai liittimet)




    - Juota musta kaapeli painikkeen --liittimeen
    - Juota punainen kaapeli yhteiseen +-liittimeen



![smoke-machine-remote](assets/fr/9.webp)



### Vaihe 2: Kytkentä relemoduuliin



**Muistutus: Releterminologia



| **Terminal**         | **Description**           | **Fonction**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (Normally Open)   | Circuit ouvert par défaut | Se ferme quand le relais est activé |
| NC (Normally Closed) | Circuit fermé par défaut  | S'ouvre quand le relais est activé  |
| COM (Common)         | Terminal central          | Bascule entre NO et NC              |

**Johdotus kaukosäätimestä relemoduuliin:**




- Musta johto ON/OFF-painikkeesta **→** NO (normaalisti avoin)
- Punainen johto (yhteinen) **→** COM (yhteinen)



**Logiikka:**


Kun ESP32 aktivoi releen, se yhdistää COM- ja NO-liitännät, mikä on täsmälleen sama kuin kaukosäätimen painikkeen painaminen.


Kun ESP32 katkaisee releen, COM ja NO eroavat toisistaan, mikä vastaa painikkeen vapauttamista.



![remote-relay](assets/fr/10.webp)



### Vaihe 3: ESP32:n liittäminen relemoduuliin



**Johtokaavio:**



| **ESP32** | **→** | **Module relais** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (Input)        |

**Varmennus:**




- VCC ja GND hyvin kytketty (napaisuus)
- GPIO 21 käytetään ohjaussignaaliin
- Ei näkyvää oikosulkua



![relay-esp32](assets/fr/11.webp)



**Checkpoint Hardware**


Tarkista ennen ohjelmistoon siirtymistä :




- Oikein kytketty kaukosäädin
- ESP32:een liitetty relemoduuli
- Paljaat johdot eivät kosketa muita komponentteja
- 220V aina kytketty pois päältä



![relay-esp32](assets/fr/12.webp)





---


## OSA 2: Ohjelmiston konfigurointi



Käytämme esimerkkinä *Blink*:aa, mutta *BTCPay Server* tarjoaa myös *Strike, Breez ja Boltz*, jos haluat toisen vaihtoehdon.



### Vaihe 1: Liitännäiset, asennus *BitcoinSwitch* + *Blink



1 - Siirry *BTCPay Server*-palvelimesi instanssiin hallintatililläsi



2 - Luo ensimmäinen kaihdin



3 - Selaa *BTCPay Serverin* vasemmalla puolella alaspäin ja siirry kohtaan *"Manage Plugins "*



![btcpay-plugins](assets/fr/13.webp)



4 - Asennamme *BitcoinSwitch*-lisäosat sekä *Blink*



![btcpay-plugins](assets/fr/14.webp)



5 - Selaa liitännäisluetteloa alaspäin ja napsauta *"Asenna "* : *BitcoinSwitch ja Blink* (tai valitsemasi käytettävissä oleva wallet)



![btcpay-plugins](assets/fr/15.webp)



6 - Kun asennus on valmis, käynnistä *BTCPay Server* uudelleen ja odota 1 minuutti, kunnes instanssi käynnistyy uudelleen



![btcpay-plugins](assets/fr/16.webp)



7 - Kun palaat kohtaan *"Manage plugins "*, tarkista, että molemmat liitännäiset on asennettu



![btcpay-plugins](assets/fr/17.webp)



### Vaihe 2: Backend : *BTCPay-palvelin + Blink*-konfiguraatio



**1 - Luo wallet * Blink***




- Käy osoitteessa https://www.blink.sv
- Luo tili. Tutustu ohjeeseen :



[https://planb.academy/en/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd](https://planb.academy/en/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)



**2 - Luo API-avain *Blink***




- Siirry API-liitäntään: **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** ja kirjaudu sisään samalla tilillä, jota käytit wallet:n luomiseen *Blink*



![blink-api](assets/fr/18.webp)





   - Kun yhteys on muodostettu, siirry *API Keys*-välilehdelle



![blink-api](assets/fr/19.webp)





   - Klikkaa *" + "* oikeassa yläkulmassa päästäksesi API-avaimen konfiguraatioon



![blink-api](assets/fr/20.webp)





   - Anna API-avaimelle nimi ja jätä oletusasetukset. Kirjoita sitten kolmannessa vaiheessa muistiin API-avaimesi - näet sen vain kerran: `blink_mZ5KxxxxxxxxxxxxxxxxxxxxxxxNbmX`



![blink-api](assets/fr/21.webp)





   - Kun se on luotu, sen pitäisi näkyä aktiivisessa API Key -luettelossa.



![blink-api](assets/fr/22.webp)



**3 - Yhdistä *Blink* *BTCPay-palvelimeen***




- Avaa *BTCPay Server*
- Siirry osoitteeseen : *Wallet* **→** *Lightning*



![btcpay-server](assets/fr/23.webp)





- Napsauta *Käytä mukautettua solmua*
- Liitä seuraava yhteysmerkkijono:



```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```



**⚠️** **Tärkeää** :




- Älä muuta ensimmäistä osaa: `type=blink;server=https://api.blink.sv/graphql`;
- Vaihda vain :
    - api-key= *avain API Blink* avaimella
    - wallet-id= *tunnuksesi wallet Blink* ID:n mukaan
- Napsauta sitten *Testaa yhteys* ja sitten *Tallenna*



![btcpay-server](assets/fr/24.webp)





 - Tarkista, että yhteys on muodostettu (vihreä tila)



![btcpay-server](assets/fr/25.webp)



**4 - Luo myyntipiste (PoS)**




- Mene BTCPay Serverissä *Plugins*-välilehdelle ja napsauta *Myyntipiste*



![btcpay-server](assets/fr/26.webp)





- Anna PoS:lle nimi ja napsauta *Luo*



![btcpay-server](assets/fr/27.webp)





- PoS-konfiguraatio :
    - Valitse myyntipisteen tyyli = *Tulostusnäyttö*
    - Valuutta = *SATS*
    - Klikkaa *SAVE*



![btcpay-server](assets/fr/28.webp)





- Tuotteen kokoonpano :
    - Poista kaikki oletustuotteet
    - Napsauta sitten *add item*



![btcpay-server](assets/fr/29.webp)



![btcpay-server](assets/fr/30.webp)





- Määritä tuote:
    - Nimike : *savukone*
    - Hinta : *10 sats*
    - Bitcoin GPIO-kytkin : 21
    - Bitcoin kytkennän kesto (millisekunteina) : 5000
    - Tallenna uusi tuote napsauttamalla *Sulje* ja sitten *Tallenna*



![btcpay-server](assets/fr/31.webp)



### Vaihe 3: Firmware: ESP32:n flashaaminen



**1 - Siirry flash-sivustolle




- Siirry osoitteeseen : [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)



![bitcoinswitch-lnbits](assets/fr/32.webp)



**2 - Flash BitcoinSwitch-firmware**




- Liitä ESP32 tietokoneeseen USB/Micro-USB-kaapelilla
- Napsauta sitten *Yhdistä laitteeseen*
- Avautuu ikkuna, valitse ESP32:n USB-portti ja napsauta *Connect*



![bitcoinswitch-lnbits](assets/fr/33.webp)





- Kun ESP32 on kytketty, flashataan BitcoinSwitchin laiteohjelma. Napsauta *T-Display*-osiossa *Upload Firmware* uusinta saatavilla olevaa versiota varten (tällä hetkellä: *bitcoinSwitch T-Display v1.0.1*)



![bitcoinswitch-lnbits](assets/fr/34.webp)





- Odota latausta, prosessi on valmis, kun lokit näyttävät *"Leaving...". "*


![bitcoinswitch-lnbits](assets/fr/35.webp)





- Irrota ESP32:n pistoke



**3 - Tarkista BitcoinSwitchin laiteohjelmiston asennus




- Lataa sivu uudelleen: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Kytke ESP32 uudelleen tietokoneeseen USB/Micro-USB-kaapelilla
- Napsauta sitten *Connect to device
- Valitse ESP32:n USB-portti ja napsauta sitten *Connect*, kuten edellä on kuvattu
- Kun yhteys on muodostettu, paina ESP32:n **RESET**-painiketta
- Tarkista lokitiedoista, että viimeiset rivit osoittavat :



```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```



(Tämä on normaalia, se tarkoittaa, että konfiguraatiota ei ole vielä määritetty, mutta laiteohjelma on asennettu.)



![bitcoinswitch-lnbits](assets/fr/36.webp)



**4 - WebSocket LNURL** URL-osoitteen luominen



Odotettu lopullinen muoto :



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



Sukupolven vaiheet :




- AvaaBTCPay-palvelimen instanssi ja siirry sitten myöhemmin luotuun PoS-palvelimeen.
- Klikkaa sitten "Näytä" avataksesi PoS:n selaimessa



![btcpay-server-https](assets/fr/37.webp)





- Kopioi sivun URL-osoite, esimerkiksi :



![btcpay-server-https](assets/fr/38.webp)



Puretaanpa tämä URL-osoite:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```





- `XXXXv` → BTCPay-palvelininstanssisi verkkotunnus
- `46XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXwFB` → PoS-tunnuksesi yksilöllinen tunniste
- `/pos` → osoittaa myyntipisteen



Muunna se:




- Korvaa `https://` sanalla `wss://`
- Lisää `/bitcoinswitch` loppuun



Tulos:



```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```



Säilytä tämä URL-osoite tulevaa konfigurointia varten, sillä sen avulla ESP32 voi kommunikoida reaaliaikaisesti BTCPay-palvelimen kanssa. WebSocket-protokolla (`wss://`) luo pysyvän yhteyden näiden kahden välille: heti kun Lightning-maksu on vahvistettu PoS-palvelimellasi, BTCPay lähettää tiedot välittömästi ESP32:een, joka voi sitten käynnistää savukoneesi.



**5 - WiFin ja WebSocketin määrittäminen




- Palaa sivulle: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/), kun ESP32 on kytketty
- Siirry kohtaan *Konfiguroi laite* → *Wlan-asetukset*



Ilmoita :




- WiFi SSID: WiFi-verkkosi nimi
- WiFi-salasana: WiFi-salasanasi



![bitcoinswitch-lnbits](assets/fr/39.webp)





- Liitä edellisessä vaiheessa luotu WebSocket URL-osoite *LNbits Device URL* -osioon
- Napsauta *Upload config*



![bitcoinswitch-lnbits](assets/fr/40.webp)





- Odota, että lataus on valmis; lokitiedostoissa pitäisi näkyä juuri syöttämäsi parametrit (SSID, salasana ja WebSocket URL)



![bitcoinswitch-lnbits](assets/fr/41.webp)





- Odota, kun ESP32 muodostaa WebSocket-yhteyden. Sinun pitäisi nähdä :



```
WiFi connection established!

[WebSocket] Connected to url: ...
```



![bitcoinswitch-lnbits](assets/fr/42.webp)





- Voit nyt irrottaa ESP32:n



---
## Checkpoint-ohjelmisto



Tarkista ennen lopputestiä :





- Blink yhdistetty BTCPayhin
- PoS luotu vähintään yhdellä esineellä
- ESP32 välähti BitcoinSwitchillä
- WiFi konfiguroitu ESP32:een
- WebSocket URL oikein
- Virheettömät ESP32-lokit



---

## Testaus ja virheenkorjaus



### Täydellinen lopputesti



1. Kytke savukone (220V) ja käynnistä se


2. Syötä ESP32:een virta (paristo tai USB)


3. Avaa BTCPay PoS selaimessasi osoitteessa


4. Skannaa "smoke-machine" kohde


5. Maksa wallet Lightningilla (Blink tai muu wallet)


6. Tarkkaile:




 - Rele naksahtaa (ääni kuuluu ja releen LED-valo syttyy)
 - Savukone aktivoidaan
 - Savua syntyy!



### Oikeudenmukaisuuteen liittyvät ongelmat ja ratkaisut



| **Problème**                        | **Cause probable**              | **Solution**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 ne se connecte pas            | Driver USB manquant             | Installer [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| Relais ne clique pas                | Mauvais câblage GPIO            | Vérifier GPIO 21 → IN                                                                        |
| Smoke machine ne réagit pas         | Télécommande mal câblée         | Vérifier NO/NC/COM                                                                           |
| WebSocket timeout                   | URL incorrecte                  | Vérifier wss:// et /bitcoinswitch                                                            |
| WiFi ne se connecte pas             | SSID/Password erroné            | Re-flasher la config WiFi                                                                    |
| Paiement reçu mais rien ne se passe | ESP32 non connecté au WebSocket | Vérifier les logs RESET                                                                      |

## Resurssit



### Hyödyllisiä linkkejä





- BitcoinSwitch Firmware: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- BTCPay-palvelimen asiakirjat : [https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- ESP32 Pinout : [https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)



### Yhteisö ja tuki





- BTCPay-palvelin** : [chat.btcpayserver.org](https://chat.btcpayserver.org/) - Official Mattermost
- BTCPay-palvelin Telegram** : [t.me/btcpayserver](https://t.me/btcpayserver)
- LNbits** : [t.me/lnbits](https://t.me/lnbits) - Virallinen Telegram, aktiivinen yhteisö
- BitcoinSwitch (laiteohjelmistovirheet)**: [github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)



### Lähdekoodi





- BitcoinSwitchin laiteohjelmiston lähdekoodi: [https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)



---

**⚡** Pinoa sats, tee savua, pidä hauskaa, pysy nöyränä! **⚡**