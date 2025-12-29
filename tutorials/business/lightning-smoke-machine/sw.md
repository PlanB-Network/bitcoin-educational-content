---
name: Lightning Smoke Machine
description: Anzisha mashine ya moshi kwa malipo ya Lightning kupitia ESP32.
---

![cover-lightning-smoke-machine](assets/cover.webp)



## Utangulizi



Hubadilisha mashine ya moshi ya kawaida kuwa kifaa kinacholipwa katika Bitcoin kupitia Lightning Network. Kila malipo husababisha moshi mwingi kiotomatiki!





- Kiwango: Kati
- Muda uliokadiriwa: saa 2-3
- Matumizi: Matukio ya Bitcoin, maonyesho ya kisanii, maonyesho ya umeme, athari za kiotomatiki za jukwaa



## Masharti ya awali



### Maarifa





 - Vifaa vya umeme vya msingi (waya, relays)
 - Kulehemu (au matumizi ya viunganishi vya Dupont)
 - Usanidi wa mtandao (WiFi, WebSocket)



### Akaunti zinahitajika





- Seva ya BTCPay: Mfano wa utendaji kazi (inayojipangisha au inayopangishwa)
- Blink Wallet: Akaunti + ufikiaji API



### Ufikiaji





- Ufikiaji wa msimamizi kwa Seva ya BTCPay
- Muunganisho wa WiFi kwa ESP32



## Vifaa vinavyohitajika



### Vifaa - Vipengele vya kielektroniki





- Kidhibiti Kidogo 1 - ESP32-WROOM-32


*ESP32-WROOM-32 ni kidhibiti kidogo cha WiFi/Bluetooth cha bei nafuu cha kuunganisha vifaa vya kielektroniki kwenye Intaneti na kuvidhibiti kwa mbali*



![ESP32](assets/fr/1.webp)





- Moduli 1 ya Relay - 5V yenye optocoupler


*Relay ni kama swichi ambayo ESP32 inaweza kuendesha ili kuwasha au kuzima mashine ya moshi*



![relay](assets/fr/2.webp)





- ~Kebo 10 za Dupont - Mwanaume/Mwanaume na Mwanaume/Mwanamke



![dupont-cables](assets/fr/3.webp)





- Ugavi 1 wa umeme kwa betri ya ESP32 - USB ya 5V au Li-Po



![battery](assets/fr/4.webp)





- Kebo 1 ndogo ya USB - muunganisho kati ya ESP32 na usambazaji wa umeme



![micro-usb-cables](assets/fr/5.webp)





- Mashine 1 ya ukungu ya 220V yenye kidhibiti cha mbali cha betri ya 12V



![remote-and-smoke-machine](assets/fr/6.webp)





- Chupa 1 ya kioevu kinachoendana na mashine yako ya moshi



### Vifaa - Zana





- Chuma cha kusugulia + bati (ikiwa ni cha kusugulia)
- Kiendeshi bisibisi
- Kipima-sauti (inapendekezwa)



### Programu





- Programu dhibiti ya BitcoinSwitch: **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- Kivinjari cha wavuti kinachooana na WebSerial (Chrome/Edge/Brave)
- Seva ya BTCPay imesanidiwa. Kwa maelezo zaidi kuhusu kuunda mfano wa Seva ya BTCPay, tembelea mafunzo haya: https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc



## Usanifu wa mfumo



![architecture-lightning-smoke-machine](assets/fr/7.webp)



---


**⚠️** **ONYO LA USALAMA - SOMA KABLA YA KUENDELEA*** **⚠️**



Mradi huu unahusisha mashine ya ukungu iliyounganishwa na usambazaji wa umeme wa **220V**. Uendeshaji usiofaa unaweza kusababisha **kupigwa na umeme** au **moto**.



**Sheria zisizoweza kujadiliwa:**



1. **Kila wakati tenganisha mashine ya moshi kutoka kwa mtandao mkuu** kabla ya kufungua kidhibiti cha mbali au kuharibu nyaya


2. **Toa betri kutoka kwa rimoti** kabla ya kuishughulikia (hatari ya mzunguko mfupi na uharibifu wa vipengele)


3. **Hakikisha kwamba miunganisho yako yote imetenganishwa** kabla ya kuunganisha tena chochote


4. **Usiwahi kuunganisha tena 220V** hadi kisanduku cha kudhibiti mbali kifungwe na kuwekwa salama



Kama hujisikii vizuri na aina hii ya kushughulikia, chukua mtu ambaye anajihisi vizuri.



---

## SEHEMU YA 1: Uunganishaji wa vifaa



### Hatua ya 1: Kuandaa kidhibiti cha mbali



Lengo: Unganisha relay kwenye kitufe cha ON/OFF kwenye rimoti


1. Fungua kidhibiti cha mbali




    - Kitufe cha kutambua WASHA/ZIMA
    - Fungua kisanduku ili kufungua kidhibiti cha mbali


2. Tafuta miunganisho




 - Tafuta vituo vya + na - vya
 - Jaribu mwendelezo kwa kutumia multimeter (hiari)



![smoke-machine-remote](assets/fr/8.webp)



3. Kuunganisha vifungo (kiunganishi au viunganishi)




    - Sulida kebo nyeusi kwenye sehemu ya mwisho ya kitufe
    - Sulisha kebo nyekundu kwenye kituo cha kawaida +



![smoke-machine-remote](assets/fr/9.webp)



### Hatua ya 2: Kuunganisha kwenye moduli ya relay



**Kikumbusho: Istilahi za Relay



| **Terminal**         | **Description**           | **Fonction**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (Normally Open)   | Circuit ouvert par défaut | Se ferme quand le relais est activé |
| NC (Normally Closed) | Circuit fermé par défaut  | S'ouvre quand le relais est activé  |
| COM (Common)         | Terminal central          | Bascule entre NO et NC              |

**Kuunganisha waya kutoka kwa kidhibiti cha mbali hadi moduli ya kupokezana:**




- Waya mweusi kutoka kitufe cha WASHA/ZIMA **→** HAPANA (Kwa kawaida Hufunguliwa)
- Waya nyekundu (kawaida) **→** COM (Kawaida)



**Mantiki:**


ESP32 inapowasha relay, inaunganisha COM na NO, ambayo ni sawa kabisa na kubonyeza kitufe cha kudhibiti mbali.


ESP32 inapokata relay, COM na NO hutengana, ambayo ni sawa na kutoa kitufe.



![remote-relay](assets/fr/10.webp)



### Hatua ya 3: Kuunganisha ESP32 kwenye moduli ya relay



**Mchoro wa waya:**



| **ESP32** | **→** | **Module relais** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (Input)        |

**Uthibitishaji:**




- VCC na GND zimeunganishwa vizuri (polariti)
- GPIO 21 inayotumika kwa ishara ya udhibiti
- Hakuna mzunguko mfupi unaoonekana



![relay-esp32](assets/fr/11.webp)



**Vifaa vya Kituo cha Kuangalia**


Kabla ya kubadili hadi kwenye programu, angalia:




- Kidhibiti cha mbali kilichounganishwa kwa waya kwa usahihi
- Moduli ya reli imeunganishwa na ESP32
- Hakuna waya tupu zinazogusa vipengele vingine
- 220V hutenganishwa kila wakati



![relay-esp32](assets/fr/12.webp)





---


## SEHEMU YA 2: Usanidi wa programu



Tutatumia *Blink* kama mfano, lakini *BTCPay Server* pia inatoa *Strike, Breez na Boltz* ikiwa unapendelea chaguo jingine.



### Hatua ya 1: Programu-jalizi, Usakinishaji *BitcoinSwitch* + *Blink



1 - Nenda kwenye mfano wako wa *BTCPay Server* ukitumia akaunti ya msimamizi



2 - Unda kipofu chako cha kwanza



3 - Upande wa kushoto wa *BTCPay Server*, sogeza hadi chini na uende kwenye *"Dhibiti Programu-jalizi"*



![btcpay-plugins](assets/fr/13.webp)



4 - Tutasakinisha programu-jalizi za *BitcoinSwitch* pamoja na *Blink*



![btcpay-plugins](assets/fr/14.webp)



5 - Sogeza chini orodha ya programu-jalizi na ubofye *"Sakinisha"* : *BitcoinSwitch na Blink* (au wallet inayopatikana ya chaguo lako)



![btcpay-plugins](assets/fr/15.webp)



6 - Mara tu usakinishaji utakapokamilika, anzisha upya *BTCPay Server* na subiri dakika 1 kwa mfano kuanza upya



![btcpay-plugins](assets/fr/16.webp)



7 - Utakaporudi kwenye *"Dhibiti programu-jalizi"*, hakikisha kwamba programu-jalizi zote mbili zimesakinishwa



![btcpay-plugins](assets/fr/17.webp)



### Hatua ya 2: Sehemu ya nyuma: *BTCPay Server + Blink* usanidi



**1 - Unda wallet *Blink***




- Tembelea https://www.blink.sv
- Fungua akaunti yako. Tafadhali rejelea mafunzo:



[https://planb.academy/en/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd](https://planb.academy/en/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)



**2 - Tengeneza kitufe cha API *Blink***




- Fikia kiolesura cha API: **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** na uingie kwa kutumia akaunti ile ile uliyotumia kuunda wallet *Blink* yako.



![blink-api](assets/fr/18.webp)





   - Ukishaunganisha, nenda kwenye kichupo cha *Funguo za API*



![blink-api](assets/fr/19.webp)





   - Bonyeza *" + "* kwenye kona ya juu kulia ili kufikia usanidi wako wa API Key



![blink-api](assets/fr/20.webp)





   - Mpe jina Funguo lako la API na uache mipangilio chaguo-msingi. Kisha, katika hatua ya tatu, andika Funguo lako la API - utaiona mara moja tu: `blink_mZ5KxxxxxxxxxxxxxxxNbmX`



![blink-api](assets/fr/21.webp)





   - Mara tu ikishaundwa, inapaswa kuonekana kwenye orodha yako ya Ufunguo wa API inayotumika.



![blink-api](assets/fr/22.webp)



**3 - Unganisha *Blink* kwenye *Seva ya BTCPay***




- Fungua *Seva yako ya BTCPay*
- Nenda kwenye: *Wallet* **→** *Umeme*



![btcpay-server](assets/fr/23.webp)





- Bonyeza *Tumia nodi maalum*
- Bandika kamba ifuatayo ya muunganisho:



```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```



**⚠️** **Muhimu** :




- Usirekebishe sehemu ya kwanza: `type=blink;server=https://api.blink.sv/graphql`;
- Badilisha tu:
    - api-key= *kwa ufunguo wako wa API Blink*
    - wallet-id= *kwa kitambulisho chako cha wallet Blink*
- Kisha bofya *Jaribu muunganisho*, kisha *Hifadhi*



![btcpay-server](assets/fr/24.webp)





 - Hakikisha muunganisho umeanzishwa (hali ya kijani)



![btcpay-server](assets/fr/25.webp)



**4 - Unda Sehemu ya Uuzaji (PoS)**




- Katika Seva ya BTCPay, nenda kwenye kichupo cha *Programu-jalizi* na ubofye *Pointi ya mauzo*



![btcpay-server](assets/fr/26.webp)





- Mpe PoS yako jina na ubofye *Unda*



![btcpay-server](assets/fr/27.webp)





- Usanidi wa PoS:
    - Chagua mtindo wa sehemu ya mauzo = *Chapisha onyesho*
    - Sarafu = *SATS*
    - Bonyeza *HIFADHI*



![btcpay-server](assets/fr/28.webp)





- Usanidi wa bidhaa:
    - Futa bidhaa zote chaguomsingi
    - Kisha bonyeza *ongeza kipengee*



![btcpay-server](assets/fr/29.webp)



![btcpay-server](assets/fr/30.webp)





- Sanidi bidhaa:
    - Kichwa: *mashine ya kuvuta sigara*
    - Bei: *10 sats*
    - Swichi ya Bitcoin GPIO: 21
    - Muda wa swichi ya Bitcoin (katika milisekunde): 5000
    - Bonyeza *Funga* kisha *Hifadhi* ili kuhifadhi bidhaa mpya



![btcpay-server](assets/fr/31.webp)



### Hatua ya 3: Programu dhibiti: Kuwasha ESP32



**1 - Nenda kwenye tovuti ya flash




- Nenda kwa: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)



![bitcoinswitch-lnbits](assets/fr/32.webp)



**2 - Flash programu dhibiti ya BitcoinSwitch**




- Unganisha ESP32 kwenye kompyuta yako kwa kutumia kebo yako ya USB/Micro-USB
- Kisha bonyeza *Unganisha kwenye Kifaa*
- Dirisha litafunguka, chagua mlango wa USB kwenye ESP32 yako, kisha bofya *Unganisha*



![bitcoinswitch-lnbits](assets/fr/33.webp)





- Mara tu ESP32 yako ikiwa imeunganishwa, tutabadilisha programu dhibiti ya BitcoinSwitch. Katika sehemu ya *T-Display*, bofya *Pakia Programu dhibiti* kwa toleo jipya zaidi linalopatikana (kwa sasa: *bitcoinSwitch T-Display v1.0.1*)



![bitcoinswitch-lnbits](assets/fr/34.webp)





- Subiri upakiaji, mchakato unakamilika kumbukumbu zinapoonekana *"Inaondoka... "*


![bitcoinswitch-lnbits](assets/fr/35.webp)





- Ondoa ESP32



**3 - Angalia usakinishaji wa programu dhibiti ya BitcoinSwitch




- Pakia upya ukurasa: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Unganisha tena ESP32 kwenye kompyuta yako kwa kutumia kebo yako ya USB/Micro-USB
- Kisha bonyeza *Unganisha kwenye kifaa
- Chagua mlango wa USB kwenye ESP32 yako, kisha bofya *Unganisha* kama ilivyoelezwa hapo juu.
- Mara tu ikiwa imeunganishwa, bonyeza kitufe cha **RESET** kwenye ESP32
- Angalia kumbukumbu ambazo mistari ya mwisho inaonyesha:



```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```



(Hili ni jambo la kawaida, inamaanisha kwamba hakuna usanidi bado, lakini kwamba programu dhibiti imewekwa)



![bitcoinswitch-lnbits](assets/fr/36.webp)



**4 - Tengeneza URL ya WebSocket LNURL**



Muundo wa mwisho unaotarajiwa:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



Hatua za kizazi:




- Fungua mfano wa Seva yako ya BTCPay, kisha nenda kwenye PoS tuliyounda baadaye.
- Kisha bofya "Tazama" ili kufungua PoS yako kwenye kivinjari



![btcpay-server-https](assets/fr/37.webp)





- Nakili URL ya ukurasa, kwa mfano:



![btcpay-server-https](assets/fr/38.webp)



Hebu tufungue URL hii:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```





- `XXXXv` → kikoa cha mfano wa Seva yako ya BTCPay
- `46XXXXXXXXXXXXXXXXXXwFB` → kitambulisho chako cha kipekee cha PoS
- `/pos` → inaonyesha Sehemu ya Mauzo



Ibadilishe:




- Badilisha `https://` na `wss://`
- Ongeza `/bitcoinswitch` mwishoni



Matokeo:



```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```



Weka URL hii kwa ajili ya usanidi wa siku zijazo, kwani itawezesha ESP32 yako kuwasiliana kwa wakati halisi na Seva ya BTCPay. Itifaki ya WebSocket (`wss://`) huanzisha muunganisho wa kudumu kati ya hizo mbili: mara tu malipo ya Lightning yanapothibitishwa kwenye PoS yako, BTCPay hutuma taarifa hiyo mara moja kwa ESP32, ambayo inaweza kusababisha mashine yako ya kuvuta sigara.



**5 - Kusanidi WiFi na WebSocket




- Rudi kwenye ukurasa: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/) huku ESP32 yako ikiwa imeunganishwa
- Nenda kwenye *Sanidi Kifaa* → *Mipangilio ya Wifi*



Taarifa:




- WiFi SSID: jina la mtandao wako wa WiFi
- Nenosiri la WiFi: nenosiri lako la WiFi



![bitcoinswitch-lnbits](assets/fr/39.webp)





- Katika sehemu ya *LNbits Device URL*, bandika URL ya WebSocket iliyoundwa katika hatua iliyotangulia
- Bonyeza *Usanidi wa kupakia*



![bitcoinswitch-lnbits](assets/fr/40.webp)





- Subiri upakiaji ukamilike; kumbukumbu zinapaswa kuonyesha vigezo ambavyo umeingiza hivi punde (SSID, nenosiri na URL ya WebSocket)



![bitcoinswitch-lnbits](assets/fr/41.webp)





- Subiri wakati ESP32 inaanzisha muunganisho wa WebSocket. Unapaswa kuona:



```
WiFi connection established!

[WebSocket] Connected to url: ...
```



![bitcoinswitch-lnbits](assets/fr/42.webp)





- Sasa unaweza kutenganisha ESP32



---
## Programu ya Kituo cha Ukaguzi



Kabla ya jaribio la mwisho, angalia:





- Blink imeunganishwa kwenye BTCPay
- PoS imeundwa kwa angalau kipengee 1
- ESP32 imewashwa na BitcoinSwitch
- WiFi imesanidiwa kwenye ESP32
- URL ya WebSocket ni sahihi
- Kumbukumbu za ESP32 zisizo na hitilafu



---

## Kujaribu na kurekebisha makosa



### Jaribio kamili la mwisho



1. Chomeka mashine ya moshi (220V) na uiwashe


2. Washa ESP32 (betri au USB)


3. Fungua BTCPay PoS yako kwenye kivinjari chako


4. Changanua kipengee cha "mashine ya kuvuta sigara"


5. Lipa kwa kutumia wallet Lightning (Blink au wallet nyingine)


6. Angalia:




 - Mibofyo ya relay (sauti inayosikika na taa za LED za relay zinawaka)
 - Mashine ya moshi imewashwa
 - Moshi unaozalishwa!



### Matatizo na suluhisho za haki



| **Problème**                        | **Cause probable**              | **Solution**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 ne se connecte pas            | Driver USB manquant             | Installer [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| Relais ne clique pas                | Mauvais câblage GPIO            | Vérifier GPIO 21 → IN                                                                        |
| Smoke machine ne réagit pas         | Télécommande mal câblée         | Vérifier NO/NC/COM                                                                           |
| WebSocket timeout                   | URL incorrecte                  | Vérifier wss:// et /bitcoinswitch                                                            |
| WiFi ne se connecte pas             | SSID/Password erroné            | Re-flasher la config WiFi                                                                    |
| Paiement reçu mais rien ne se passe | ESP32 non connecté au WebSocket | Vérifier les logs RESET                                                                      |

## Rasilimali



### Viungo muhimu





- Programu dhibiti ya BitcoinSwitch: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Hati za Seva ya BTCPay: [https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- Kidokezo cha ESP32: [https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)



### Jumuiya na Usaidizi





- Seva ya BTCPay**: [chat.btcpayserver.org](https://chat.btcpayserver.org/) - Muhimu Rasmi
- Seva ya BTCPay Telegram** : [t.me/btcpayserver](https://t.me/btcpayserver)
- LNbits** : [t.me/lnbits](https://t.me/lnbits) - Jumuiya Rasmi ya Telegram, inayofanya kazi
- BitcoinSwitch (hitilafu za programu dhibiti)**: [github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)



### Msimbo chanzo





- Msimbo chanzo cha programu dhibiti ya BitcoinSwitch: [https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)



---

**⚡** Pakia sats, vuta moshi, furahiya, endelea kuwa mnyenyekevu! **⚡**