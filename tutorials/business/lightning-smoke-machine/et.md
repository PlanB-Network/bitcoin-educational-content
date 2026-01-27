---
name: Lightning Smoke Machine
description: Käivitage suitsuaparaat välkmaksega ESP32 kaudu.
---

![cover-lightning-smoke-machine](assets/cover.webp)



## Sissejuhatus



Muudab klassikalise suitsuaparaadi Lightning Network kaudu Bitcoin tasuliseks seadmeks. Iga makse käivitab automaatselt suitsujoa!





- Tase: Keskmise taseme
- Hinnanguline aeg: 2-3 tundi
- Kasutusjuhtumid: Bitcoin üritused, kunstilised etendused, välkdemod, automatiseeritud lavaefektid



## Eeltingimused



### Teadmised





 - Põhiline elektroonika (juhtmestik, releed)
 - Keevitamine (või Dupont-liitmike kasutamine)
 - Võrgukonfiguratsioon (WiFi, WebSocket)



### Vajalikud kontod





- BTCPay server: Funktsionaalne instants (ise hostitud või hostitud)
- Blink Wallet : konto + juurdepääs API



### Juurdepääs





- Administraatori juurdepääs BTCPay serverile
- WiFi ühendus ESP32 jaoks



## Vajalikud materjalid



### Riistvara - Elektroonilised komponendid





- 1 mikrokontroller - ESP32-WROOM-32


*ESP32-WROOM-32 on kompaktne ja odav WiFi/Bluetooth mikrokontroller elektrooniliste seadmete ühendamiseks internetti ja nende kaugjuhtimiseks*



![ESP32](assets/fr/1.webp)





- 1 releemoodul - 5V koos optoühendusega


*Relee on nagu lüliti, mida ESP32 saab kasutada suitsumasina sisse või välja lülitamiseks*



![relay](assets/fr/2.webp)





- ~10 Dupont kaablit - mees/mees ja mees/naine



![dupont-cables](assets/fr/3.webp)





- 1 toiteallikas ESP32 jaoks - 5V USB või Li-Po aku



![battery](assets/fr/4.webp)





- 1 micro-USB kaabel - ühendus ESP32 ja toiteallika vahel



![micro-usb-cables](assets/fr/5.webp)





- 1 220V udumasin koos 12 V akupuldiga kaugjuhtimispuldiga



![remote-and-smoke-machine](assets/fr/6.webp)





- 1 pudel teie suitsutusmasinaga ühilduvat vedelikku



### Riistvara - Tööriistad





- Jootekolb + tina (jootmise korral)
- Kruvikeeraja
- Multimeeter (soovitatav)



### Tarkvara





- Firmware BitcoinSwitch : **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- WebSerial-ühilduv veebibrauser (Chrome/Edge/Brave)
- BTCPay server konfigureeritud. Lisateavet BTCPay Serveri instantsi loomise kohta leiate siit: https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc



## Süsteemi arhitektuur



![architecture-lightning-smoke-machine](assets/fr/7.webp)



---


**⚠️** **OHUTUSHOIATUS - LOE ENNE JÄTKAMIST** **⚠️**



See projekt hõlmab **220V vooluvõrku** ühendatud udumasinat. Ebaõige käitamine võib põhjustada **surmaga lõppeva elektrilöögi** või **tulekahju**.



**Mitte-läbirääkimiste reeglid:**



1. **KASUTA ühendage suitsuaparaat alati vooluvõrgust lahti** enne kaugjuhtimispuldi avamist või juhtmestikuga manipuleerimist


2. **Eemaldage enne käsitsemist patarei puldist** (lühise ja komponentide kahjustamise oht)


3. **Kontrollige, et kõik teie ühendused on isoleeritud**, enne kui ühendate midagi uuesti


4. **Mitte kunagi ühendage 220V** uuesti, enne kui kaugjuhtimispult on suletud ja kinnitatud



Kui te ei tunne end sellise käitlemise juures mugavalt, võtke kaasa keegi, kes seda oskab.



---

## OSA 1: Riistvara kokkupanek



### Samm 1: Puldi ettevalmistamine



Eesmärk: Ühendage relee kaugjuhtimispuldi ON/OFF nupu külge


1. Avatud kaugjuhtimispult




    - ON/OFF nupu tuvastamine
    - Puldi avamiseks keerake korpus lahti


2. Leia ühendused




 - Leidke + ja - klemmid seadme
 - Testige pidevust multimeetriga (valikuline)



![smoke-machine-remote](assets/fr/8.webp)



3. Nuppude juhtmestik (jootmine või pistikud)




    - Joodetage must kaabel nupu - klemmile
    - Joodetakse punane kaabel ühisele + klemmile



![smoke-machine-remote](assets/fr/9.webp)



### Samm 2: Ühendamine releemooduliga



**Mälestus: Releeterminoloogia




| **Klemm**         | **Kirjeldus**           | **Funktsioon**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (Tavaliselt avatud)   | Ahel on vaikimisi avatud | Sulgub, kui rele aktiveeritakse |
| NC (Tavaliselt suletud) | Ahel on vaikimisi suletud  | Avaneb, kui rele aktiveeritakse  |
| COM (Ühine)         | Keskne klemm          | Lülitub NO ja NC vahel              |

**Puldi juhtmestik releemoodulile:**




- Must juhe nupust ON/OFF **→** NO (normaalselt avatud)
- Punane juhe (ühine) **→** COM (ühine)



**Loogika:**


Kui ESP32 aktiveerib relee, ühendab ta COM ja NO, mis on täpselt sama, mis kaugjuhtimispuldi nupu vajutamine.


Kui ESP32 katkestab relee, eralduvad COM ja NO, mis on samaväärne nupu vabastamisega.



![remote-relay](assets/fr/10.webp)



### Samm 3: ESP32 ühendamine releemooduliga



**Juhtmestiku skeem:**




| **ESP32** | **→** | **Relee moodul** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (Sisend)        |

**Kontroll:**




- VCC ja GND hästi ühendatud (polaarsus)
- GPIO 21, mida kasutatakse juhtimissignaaliks
- Nähtav lühis puudub



![relay-esp32](assets/fr/11.webp)



**Checkpoint Hardware**


Enne tarkvarale üleminekut kontrollige :




- Õigesti ühendatud kaugjuhtimispult
- ESP32-ga ühendatud releemoodul
- Paljad juhtmed ei puutu kokku teiste komponentidega
- 220V alati lahti ühendatud



![relay-esp32](assets/fr/12.webp)





---


## OSA 2: Tarkvara konfigureerimine



Kasutame näitena *Blink*, kuid *BTCPay Server* pakub ka *Strike, Breez ja Boltz*, kui eelistate muud võimalust.



### Samm 1: Plugins, paigaldus *BitcoinSwitch* + *Blink



1 - Mine oma *BTCPay Server* instantsile administraatori kontoga



2 - Loo oma esimene pime



3 - *BTCPay Serveri* vasakul poolel kerige allapoole ja minge *"Manage Plugins "*



![btcpay-plugins](assets/fr/13.webp)



4 - Me paigaldame nii *BitcoinSwitch* pluginad kui ka *Blink*



![btcpay-plugins](assets/fr/14.webp)



5 - kerige pluginate loendis alla ja klõpsake *"Install "* : *BitcoinSwitch ja Blink* (või teie valitud wallet)



![btcpay-plugins](assets/fr/15.webp)



6 - Kui paigaldus on lõpetatud, taaskäivitage *BTCPay Server* ja oodake 1 minut, kuni instants taaskäivitub



![btcpay-plugins](assets/fr/16.webp)



7 - Kui naasete *"Manage plugins "*, kontrollige, et mõlemad pluginad on paigaldatud



![btcpay-plugins](assets/fr/17.webp)



### 2. samm: Backend : *BTCPay Server + Blink* konfiguratsioon



**1 - Loo wallet *Blink***




- Külasta https://www.blink.sv
- Looge oma konto. Palun vaadake juhendmaterjali :



[https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)



**2 - API võtme genereerimine *Blink***




- Juurdepääs API liidesele: **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** ja logige sisse sama kontoga, mida kasutasite wallet loomisel *Blink*



![blink-api](assets/fr/18.webp)





   - Kui olete ühendatud, minge vahekaardile *API võtmed*



![blink-api](assets/fr/19.webp)





   - Klõpsake *" + "* üleval paremas nurgas, et pääseda oma API võtme konfiguratsioonile



![blink-api](assets/fr/20.webp)





   - Andke oma API võtmele nimi ja jätke vaikimisi seaded. Seejärel märkige kolmandas etapis oma API võti - seda näete ainult üks kord: `blink_mZ5KxxxxxxxxxxxxxxxxxxxxxNbmX`



![blink-api](assets/fr/21.webp)





   - Kui see on loodud, peaks see ilmuma teie aktiivse API võtme loendisse.



![blink-api](assets/fr/22.webp)



**3 - ühendage *Blink* *BTCPay serveriga***




- Avage oma *BTCPay Server*
- Navigeeri aadressile : *Wallet* **→** *Lightning*



![btcpay-server](assets/fr/23.webp)





- Klõpsake *Kasutage kohandatud sõlme*
- Sisestage järgmine ühendusstring:



```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```



**⚠️** **Tähtis** :




- Ärge muutke esimest osa: `type=blink;server=https://api.blink.sv/graphql`;
- Asendage ainult :
    - api-key= * teie API Blink* võti
    - wallet-id= * teie wallet Blink* ID järgi
- Seejärel klõpsake *Testiühendus*, seejärel *Salvesta*



![btcpay-server](assets/fr/24.webp)





 - Kontrollida, et ühendus on loodud (roheline olek)



![btcpay-server](assets/fr/25.webp)



**4 - Müügikoha loomine (PoS)**




- Mine BTCPay Serveris vahekaardile *Plugins* ja klõpsa *Müügipunkt*



![btcpay-server](assets/fr/26.webp)





- Andke oma PoSile nimi ja klõpsake *Loo*



![btcpay-server](assets/fr/27.webp)





- PoS-konfiguratsioon :
    - Valige müügipunkti stiil = *Trükinäidik*
    - Valuuta = *SATS*
    - Klõpsake *SAVE*



![btcpay-server](assets/fr/28.webp)





- Toote konfiguratsioon :
    - Kustuta kõik vaikimisi tooted
    - Seejärel klõpsa *lisa kirje*



![btcpay-server](assets/fr/29.webp)



![btcpay-server](assets/fr/30.webp)





- Konfigureerige toode:
    - Pealkiri : *smoke-machine*
    - Hind : *10 sats*
    - Bitcoin GPIO lüliti : 21
    - Bitcoin lüliti kestus (millisekundites) : 5000
    - Uue toote salvestamiseks klõpsake *Sulge* ja seejärel *Salvesta*



![btcpay-server](assets/fr/31.webp)



### 3. samm: püsivara: ESP32 flashimine



**1 - Mine flash-saidile




- Mine : [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)



![bitcoinswitch-lnbits](assets/fr/32.webp)



**2 - Flash BitcoinSwitch firmware**




- Ühendage ESP32 arvutiga USB/Mikro-USB kaabli abil
- Seejärel klõpsake *Seadmega ühendamine*
- Avaneb aken, valige oma ESP32 USB-port, seejärel klõpsake *Connect*



![bitcoinswitch-lnbits](assets/fr/33.webp)





- Kui teie ESP32 on ühendatud, flashime BitcoinSwitchi püsivara. Klõpsake jaotises *T-Display* värskema saadaval oleva versiooni *Upload Firmware* (praegu: *bitcoinSwitch T-Display v1.0.1*)



![bitcoinswitch-lnbits](assets/fr/34.webp)





- Oodake üleslaadimist, protsess on lõpetatud, kui logid näitavad *"Leaving... "*


![bitcoinswitch-lnbits](assets/fr/35.webp)





- Ühendage ESP32 lahti



**3 - Kontrollige BitcoinSwitchi püsivara paigaldamist




- Laadige leht uuesti: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Ühendage ESP32 uuesti arvutiga USB/Mikro-USB-kaabli abil
- Seejärel klõpsake *Seadmega ühendamine
- Valige oma ESP32 USB-port, seejärel klõpsake *Connect*, nagu eespool kirjeldatud
- Pärast ühendamist vajutage ESP32-l nuppu **RESET**
- Kontrollige logides, et viimased read näitavad :



```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```



(See on normaalne, see tähendab, et konfiguratsiooni veel ei ole, kuid püsivara on paigaldatud)



![bitcoinswitch-lnbits](assets/fr/36.webp)



**4 - WebSocket LNURL** URL-i genereerimine



Eeldatav lõplik vorming :



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



Genereerimise sammud :




- Avage omaBTCPay serveri instants, seejärel minge hiljem loodud PoS-i.
- Seejärel klõpsake "View", et avada oma PoS brauseris



![btcpay-server-https](assets/fr/37.webp)





- Kopeeri lehekülje URL, näiteks :



![btcpay-server-https](assets/fr/38.webp)



Võtame selle URL-i lahti:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```





- `XXXXv` → teie BTCPay serveri instantsi domeen
- "46XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXwFB" → teie PoSi kordumatu tunnus
- `/pos` → tähistab müügikohta



Muutke see ümber:




- Asendage "https://" sõnadega "wss://"
- Lisa `/bitcoinswitch` lõppu



Tulemus:



```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```



Hoidke see URL edaspidiseks seadistamiseks alles, sest see võimaldab teie ESP32-l suhelda reaalajas BTCPay serveriga. WebSocket-protokoll (`wss://`) loob nende kahe vahel püsiva ühenduse: niipea, kui Lightning-makse kinnitatakse teie PoSis, saadab BTCPay selle teabe koheselt ESP32-le, mis saab seejärel käivitada teie suitsumasinat.



**5 - WiFi ja WebSocket seadistamine




- Tagasi leheküljele: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/), kui ESP32 on ühendatud
- Mine *Seadme konfigureerimine* → *Wifi seaded*



Teavita :




- WiFi SSID: teie WiFi-võrgu nimi
- WiFi parool: teie WiFi parool



![bitcoinswitch-lnbits](assets/fr/39.webp)





- Sisestage *LNbits seadme URL* sektsiooni eelmises etapis loodud WebSocket URL
- Klõpsake *Upload config*



![bitcoinswitch-lnbits](assets/fr/40.webp)





- Oodake üleslaadimise lõppu; logid peaksid näitama äsja sisestatud parameetreid (SSID, parool ja WebSocket URL)



![bitcoinswitch-lnbits](assets/fr/41.webp)





- Oodake, kuni ESP32 loob WebSocket-ühenduse. Te peaksite nägema :



```
WiFi connection established!

[WebSocket] Connected to url: ...
```



![bitcoinswitch-lnbits](assets/fr/42.webp)





- Nüüd saate ESP32 lahti ühendada



---
## Checkpoint tarkvara



Enne lõppkatset kontrollige :





- Blink ühendatud BTCPayga
- Vähemalt 1 esemega loodud PoS
- ESP32 vilksatas koos BitcoinSwitchiga
- WiFi konfigureeritud ESP32-s
- WebSocket URL õige
- Vigadeta ESP32 logid



---

## Testimine ja vigade kõrvaldamine



### Täielik lõppkatsetus



1. Ühendage suitsuaparaat (220 V) ja lülitage see sisse


2. ESP32 toide (aku või USB)


3. Avage oma BTCPay PoS brauseris


4. Skaneeri objekt "suitsumasin"


5. Maksab wallet välguga (Blink või muu wallet)


6. Jälgige:




 - Relee klõpsab (helisev heli ja relee LED süttib)
 - Suitsumasin on aktiveeritud
 - Tekkinud suitsu!



### Õigluse probleemid ja lahendused




| **Probleem**                        | **Tõenäoline põhjus**              | **Lahendus**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 ei ühenda            | Puudub USB-draiver             | Installige [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| Rele ei kliki                | Vale GPIO-kaablitamine            | Kontrollige GPIO 21 → IN                                                                        |
| Suitsumachine ei reageeri         | Kaugjuhtimise vale kaablitamine         | Kontrollige NO/NC/COM                                                                           |
| WebSocket ajalõpp                   | Vale URL                  | Kontrollige wss:// ja /bitcoinswitch                                                            |
| WiFi ei ühenda             | SSID/Parool vale            | Kirjutage WiFi-seadistus uuesti                                                                    |
| Makse saadud, kuid midagi ei juhtu | ESP32 pole WebSocketiga ühendatud | Kontrollige RESET-logisid                                                                      |

## Ressursid



### Kasulikud lingid





- BitcoinSwitch Firmware: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- BTCPay serveri dokumendid : [https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- ESP32 pinout : [https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)



### Kogukond ja toetus





- BTCPay server** : [chat.btcpayserver.org](https://chat.btcpayserver.org/) - Official Mattermost
- BTCPay server Telegram** : [t.me/btcpayserver](https://t.me/btcpayserver)
- LNbits** : [t.me/lnbits](https://t.me/lnbits) - Ametlik Telegram, aktiivne kogukond
- BitcoinSwitch (püsivara vead)**: [github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)



### Allikakood





- BitcoinSwitchi püsivara lähtekood: [https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)



---

**⚡** Stack sats, tee suitsu, lõbutsege, jääge tagasihoidlikuks! **⚡**