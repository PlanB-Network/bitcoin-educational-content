---
name: Lightning Smoke Machine
description: Gutera imashini y'umwotsi n'ukwishyura kw'umuravyo biciye kuri ESP32.
---

![cover-lightning-smoke-machine](assets/cover.webp)



## Imenyekanisha



Ihindura imashini y'umwotsi ya kera mu gikoresho cishurwa muri Bitcoin biciye ku Lightning Network. Igihe cose umuntu yishuye, aca ahita atera umwotsi!





- Urugero: Hagati
- Igihe gitegekanijwe: amasaha 2-3
- Ikoreshwa ry'ibintu: Ibikorwa vya Bitcoin, ibikorwa vy'ubuhinga, ivyerekanwa vy'umuravyo, ingaruka z'ibarabara zikora



## Ibisabwa



### Ubumenyi





 - Ivy'ishimikiro vy'ubuhinga bwa none (amawaya, amarelay)
 - Gusudira (canke gukoresha ibifatanya Dupont)
 - Itunganywa ry'urubuga (WiFi, WebSocket)



### Konti zikenewe





- Serveri ya BTCPay: Inkuru ikora (yikira canke yakira)
- Blink Wallet : Konti + uburenganzira bwo gukoresha API.



### Kwinjira





- Ukwinjira kw'umuyobozi kuri Serveri ya BTCPay
- Ihuriro rya WiFi kuri ESP32



## Ibikoresho bisabwa



### Ibikoresho - Ibice vy'ubuhinga bwa none





- 1 Igikoresho co kugenzura - ESP32-ICUMBA-32


*ESP32-WROOM-32 ni igikoresho gikomeye kandi kidahenda cane gikoresha WiFi/Bluetooth co gufatanya ibikoresho vy'ubuhinga bwa none na Internet no kubigenzura uri kure*



![ESP32](assets/fr/1.webp)





- 1 Igikoresho co gutanga amakuru - 5V n'igikoresho co gufatanya amaso


*Relay ni nk'umuyagankuba ESP32 ishobora gukoresha kugira ngo imashini y'umwotsi ifungure canke izime*



![relay](assets/fr/2.webp)





- ~10 Intsinga za Dupont - Umugabo/Umugabo n'Umugabo/Umugore



![dupont-cables](assets/fr/3.webp)





- 1 Inguvu za ESP32 - 5V USB canke Li-Po bateri



![battery](assets/fr/4.webp)





- 1 umugozi wa micro-USB - guhuza hagati ya ESP32 n'umuyagankuba



![micro-usb-cables](assets/fr/5.webp)





- 1 Imashini y'igihu 220V ifise ubugenzuzi bwa kure bwa bateri 12V



![remote-and-smoke-machine](assets/fr/6.webp)





- Icupa 1 ry'amazi rihuye n'imashini yawe y'umwotsi



### Ibikoresho - Ibikoresho





- Icuma co gusodera + itini (niba ari ugusodera)
- Igikoresho co gukubita
- Multimètre (ni vyiza)



### Porogaramu





- Porogaramu y'ubuhinga bwa none : **[ihindura ry'amahera.lnbits.com/]
- Umucukumbuzi w'urubuga uhuye n'uruhererekane (Chrome/Edge/Brave)
- Serveri ya BTCPay yatunganijwe. Kugira ngo umenye vyinshi ku bijanye no kurema urugero rwa Server ya BTCPay, sura iyi nyigisho:



## Ubwubatsi bwa sisitemu



![architecture-lightning-smoke-machine](assets/fr/7.webp)



---


**⚠️** **IMBURIZO Y'UMUTEKANO - SOMA IMBERE YO GUKOMEZA** **⚠️**



Uwo mugambi ushimikiye ku mashine y’igihu ifatanye n’umuriro w’amashanyarazi **220V**. Gukoresha nabi bishobora gutuma umuntu **afatwa n’umuyagankuba** canke **umuriro**.



**Amategeko adashobora gusubirwamwo:**



1. **IGIHE cose ushire imashini y’umwotsi ku nzira y’amashanyarazi** imbere yo gufungura televiziyo canke guhindura amashanyarazi


2. **Kura bateri kuri remote** imbere yo kuyikoresha (ingorane yo guca mu nzira igufi no kwonona ibihimba)


3. **Suzuma ko ama connexions yawe yose ari ukwayo** imbere yo gusubira guhuza ikintu cose


4. **Ntukigere usubira gufatanya 220V** gushika akazu k'ivyuma bikoreshwa kure kapfungiwe kandi gakingiwe



Nimba udashobora gufata neza ubwo buryo, gendana n’umuntu ari we.



---

## IGICE CA 1: Ikoraniro ry'ibikoresho



### Intambwe ya 1: Gutegura ivyuma bikoreshwa kure



Intumbero: Huza iyo relay n'ubuto ON/OFF buri ku gikoresho co gukoresha kure


1. Gufungura ubugenzuzi bwa kure




    - Menya buto ON/OFF
    - Kugurura igikapu kugira ngo ufungure ubugenzuzi bwa kure


2. Tora amahuzu




 - Tora aho + na - biherereye
 - Igerageza ry'ububandanya n'igipimo (ntibikenewe)



![smoke-machine-remote](assets/fr/8.webp)



3. Amawaya y'ubuto (amasolde canke amahuza)




    - Gushiramwo umugozi w'umwirabura ku mpera y'ubuto
    - Gutera umugozi utukura ku nzira rusangi +



![smoke-machine-remote](assets/fr/9.webp)



### Intambwe ya 2: Guhuza n'umurongo w'ivyuma



**Icibutso: Amajambo yo gutanga



| **Terminal**         | **Description**           | **Fonction**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (Normally Open)   | Circuit ouvert par défaut | Se ferme quand le relais est activé |
| NC (Normally Closed) | Circuit fermé par défaut  | S'ouvre quand le relais est activé  |
| COM (Common)         | Terminal central          | Bascule entre NO et NC              |

**Ugushiramwo amawaya kuva ku gikoresho co kure gushika ku gikoresho co gutanga amakuru:**




- Intsinga yirabura iva kuri buto ON/OFF **→** OYA (Mu bisanzwe ifungura)
- Intsinga itukura (isanzwe) **→** COM (Isanzwe)



**Ivyiyumviro:**


Iyo ESP32 ikoresheje relay, ifatanya COM na NO, ivyo bikaba bimeze neza neza no gukanda buto ya remote control.


Iyo ESP32 ikata relay, COM na NO biratandukana, ivyo bikaba bingana no kurekura buto.



![remote-relay](assets/fr/10.webp)



### Intambwe ya 3: Gufatanya ESP32 n'umurongo w'ivyuma



**Igishushanyo c'amashanyarazi:**



| **ESP32** | **→** | **Module relais** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (Input)        |

**Igenzura:**




- VCC na GND bihuye neza (uburinganire)
- GPIO 21 ikoreshwa mu kugenzura ikimenyetso
- Nta nzira ngufi iboneka



![relay-esp32](assets/fr/11.webp)



**Ibikoresho vyo gusuzumiramwo**


Imbere yo guhindukira kuri porogaramu, suzuma :




- Igikoresho co kugenzura kure gifise amawaya akwiye
- Igikoresho co guhanahana amakuru gihuye na ESP32
- Nta nsinga zikora ku bindi bihimba
- 220V yama ivuyeho



![relay-esp32](assets/fr/12.webp)





---


## IGICE CA 2: Gutunganya porogaramu



Tuzokoresha *Blink* nk'akarorero, ariko *BTCPay Server* nayo itanga *Strike, Breez na Boltz* nimba ushaka ubundi buryo.



### Intambwe ya 1: Ivyuma, Gushiramwo *Ihindura ryaBitcoin* + *Blink



1 - Genda kuri *BTCPay Server* yawe ufise konti y'umuyobozi



2 - Rema impumyi yawe ya mbere



3 - Ku ruhande rw'ibubamfu rwa *BTCPay Server*, genda hasi uje kuri *"Gucungera Plugins "*



![btcpay-plugins](assets/fr/13.webp)



4 - Tugiye gushiramwo ibikoresho vya *BitcoinSwitch* hamwe n'ivya *Blink*



![btcpay-plugins](assets/fr/14.webp)



5 - Manuka ku rutonde rw'ibikoresho maze ukande kuri *"Shiraho "* : *BitcoinSwitch na Blink* (canke wallet iriho uhisemwo)



![btcpay-plugins](assets/fr/15.webp)



6 - Iyo installation irangiye, subiramwo *BTCPay Server* hanyuma urindire umunota 1 kugira ngo instance isubire gutangura



![btcpay-plugins](assets/fr/16.webp)



7 - Iyo usubiye kuri *"Gucungera ibikoresho "*, suzuma ko ibikoresho vyose vyashizwemwo



![btcpay-plugins](assets/fr/17.webp)



### Intambwe ya 2: Inyuma : * Serveri ya BTCPay + Blink* gutunganya



**1 - Rema Igikoresho-15 *Igikoresho-16***




- Sura urubuga rwa https://www.
- Rema konti yawe. Urasabwa kuraba inyigisho :



[Umugambi.ishure/ru/inyigisho/wallet/telefone ngendanwa/uguca ibibatsi-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd] (Umugambi.ishure/ru/inyigisho/wallet/telefone ngendanwa/uguca ibibatsi-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)



**2 - Gutanga urufunguzo rwa API *Blink***




- Ushobora gushika ku rubuga rwa API: **[https://blink.sv/ru/api)** maze winjire muri iyo konti nyene wakoresheje mu gukora wallet yawe *Blink*



![blink-api](assets/fr/18.webp)





   - Iyo umaze gufatanya, genda kuri *API Keys* tab



![blink-api](assets/fr/19.webp)





   - Fyonda kuri *" + "* mu mfuruka yo hejuru iburyo kugira ngo ugere ku miterere y'urufunguzo rwawe rwa API



![blink-api](assets/fr/20.webp)





   - Ha izina Urufunguzo rwawe rwa API maze usige ivyashizweho. Hanyuma, mu ntambwe ya gatatu, ushire ahabona urufunguzo rwawe rwa API - uzorubona rimwe gusa: `blink_mZ5KxxxxxxxxxxxxxNbmX`



![blink-api](assets/fr/21.webp)





   - Iyo imaze kuremwa, ikwiye kuboneka mu rutonde rwawe rw'Ifunguro rwa API rukora.



![blink-api](assets/fr/22.webp)



**3 - Huza *Blink* na *Seriveri ya BTCPay***




- Gufungura *Serveri yawe ya BTCPay*
- Kugendagenda kuri : *Wallet* **→** *Imiravyo*



![btcpay-server](assets/fr/23.webp)





- Fyonda kuri *Koresha urudodo rwihariye*
- Nimanike urudodo rw'ihuriro rukurikira:



```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```



**⚠️** **Igihambaye** :




- Ntuhindure igice ca mbere: `ubwoko=umuco;umukozi=https://api.umuco.sv/graphql`;
- Gusubirira gusa :
    - api-urufunguzo= *n'urufunguzo rwawe rwa API Blink*
    - Indangamuntu yawe ya wallet-31*
- Hanyuma ukande kuri *Igerageza ry'ihuriro*, hanyuma *Bike*



![btcpay-server](assets/fr/24.webp)





 - Suzuma ko ihuriro ryashizweho (ibara ry'icatsi kibisi)



![btcpay-server](assets/fr/25.webp)



**4 - Gukora ahantu ho kugurisha (PoS)**




- Muri Server ya BTCPay, genda kuri *Plugins* ukande kuri *Ikibanza co kugurisha*



![btcpay-server](assets/fr/26.webp)





- Ha PoS yawe izina hanyuma ukande kuri *Create*



![btcpay-server](assets/fr/27.webp)





- Itunganywa rya PoS :
    - Hitamwo uburyo bwo kugurisha = *Iyerekanwa ry'icapa*
    - Amafaranga = *SATS*
    - Fyonda kuri *BIKA*



![btcpay-server](assets/fr/28.webp)





- Itunganywa ry'igicuruzwa :
    - Gukuraho ibicuruzwa vyose mburabuzi
    - Hanyuma ukande kuri *wongerako ikintu*



![btcpay-server](assets/fr/29.webp)



![btcpay-server](assets/fr/30.webp)





- Gutunganya igicuruzwa:
    - Umutwe : *imashini y'umwotsi*
    - Igiciro : *10 sats*
    - Bitcoin GPIO ihindura : 21
    - Igihe co guhindura Bitcoin (mu milisegonda) : 5000
    - Fyonda kuri *Funga* hanyuma *Bika* kugira ubike igicuruzwa gishasha



![btcpay-server](assets/fr/31.webp)



### Intambwe ya 3: Porogaramu: Guca ESP32



**1 - Genda ku rubuga rwa flash




- Genda kuri : [https://ihindura ry'amafaranga.com/](ibara ry'amafaranga.com/)



![bitcoinswitch-lnbits](assets/fr/32.webp)



**2 - Flash porogaramu nkuru ya Bitcoin**




- Huza ESP32 na mudasobwa yawe ukoresheje umugozi wawe wa USB/Micro-USB
- Hanyuma ukande kuri *Huza n'Igikoresho*
- Idirisha rizofunguka, uhitemwo port ya USB iri kuri ESP32 yawe, hanyuma ukande kuri *Connect*



![bitcoinswitch-lnbits](assets/fr/33.webp)





- ESP32 yawe imaze gufatanya, tuzoca ducapura porogarama ya BitcoinSwitch. Mu gice ca *T-Igaragaza*, fyonda ku *Shirako Porogaramu Nkuru* kugira ngo ubone verisiyo nshasha iriho (ubu: *Igaragaza T-bitcoinSwitch v1.0.1*)



![bitcoinswitch-lnbits](assets/fr/34.webp)





- Rindira gushirwako, igikorwa kiraheza igihe ibitabo vyerekana *"Kuva... "*


![bitcoinswitch-lnbits](assets/fr/35.webp)





- Kuraho ESP32



**3 - Suzuma uko porogaramu ya Bitcoin yashizweho




- Subiramwo urupapuro: [https://ihindura ry'amafaranga.com/](ibara ry'amafaranga.
- Subira gufatanya ESP32 na mudasobwa yawe ukoresheje umugozi wawe wa USB/Micro-USB
- Hanyuma ukande kuri *Huza n'igikoresho
- Hitamwo port ya USB kuri ESP32 yawe, hanyuma ukande kuri *Connect* nk'uko vyavuzwe haruguru
- Igihe umaze gufatanya, kanda buto ya **RESET** iri kuri ESP32
- Suzuma mu nyandiko imirongo ya nyuma yerekana :



```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```



(Ivyo ni ibisanzwe, bisigura ko ata config iracariho, ariko ko firmware yashizwemwo)



![bitcoinswitch-lnbits](assets/fr/36.webp)



**4 - Guhingura urubuga LNURL** URL



Uburyo bwa nyuma bwitezwe :



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



Intambwe z'uruvyaro :




- Ugurure instance ya Server yawe ya BTCPay, hanyuma ugende kuri PoS twaremye mu nyuma.
- Hanyuma ukande kuri "View" kugira ngo ufungure PoS yawe mu mucukumbuzi



![btcpay-server-https](assets/fr/37.webp)





- Kopa URL ya paji, nk'akarorero :



![btcpay-server-https](assets/fr/38.webp)



Reka dufungure iyi URL:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```





- `XXXXv` → urwego rwa Serveri yawe ya BTCPay
- → ikimenyetso cawe kidasanzwe ca PoS
- `/pos` → yerekana ahantu ho kugurisha



Bihindure:




- Gusubiriza `https://` na `wss://`
- Yongerako `/ bitcoins` ku mpera



Umwimbu:



```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```



Gumana iyi URL kugira ngo uyikoreshe mu gihe kizoza, kuko izotuma ESP32 yawe ishobora kuvugana na BTCPay Server mu gihe nyaco. Iryo tegeko rya WebSocket (`wss://`) rishingaho ubucuti buhoraho hagati y’ivyo bibiri: igihe nyene ukwishyura kwa Lightning kwemejwe kuri PoS yawe, BTCPay ica yohereza ayo makuru kuri ESP32, iyo na yo ikaba ishobora gutuma imashini yawe y’umwotsi ikora.



**5 - Gutunganya WiFi na WebSocket




- Subira kuri paji: [https://ibice.
- Genda kuri *Gutunganya igikoresho* → *Ivyagezwe vya Wifi*



Kumenyesha :




- WiFi SSID: izina ry'urubuga rwawe rwa WiFi
- Ijambobanga rya WiFi: ijambobanga rya WiFi yawe



![bitcoinswitch-lnbits](assets/fr/39.webp)





- Mu gice ca *URL y'igikoresho ca LNbits*, shiramwo URL ya WebSocket yaremwe mu ntambwe iheze
- Fyonda kuri *Shirako config*



![bitcoinswitch-lnbits](assets/fr/40.webp)





- Rindira ko ivyo gushiramwo biheza; Inyandiko zikwiye kugaragaza amaparametere uherutse kwinjiza (SSID, ijambobanga na WebSocket URL)



![bitcoinswitch-lnbits](assets/fr/41.webp)





- Rindira igihe ESP32 ishiraho ihuriro rya WebSocket. Ushobora kubona :



```
WiFi connection established!

[WebSocket] Connected to url: ...
```



![bitcoinswitch-lnbits](assets/fr/42.webp)





- Ubu ushobora guca ESP32



---
## Porogaramu y'igenzura



Imbere y'ikigeragezo ca nyuma, suzuma :





- Blink ihuye na BTCPay
- PoS yaremwe n'ikintu 1
- ESP32 yaca ibibatsi n'umuhinduzi wa Bitcoin
- WiFi yatunganijwe kuri ESP32
- URL y'urubuga iragororotse
- Ibitabo vya ESP32 bitagira amakosa



---

## Kugerageza no gukosora



### Uzuze ikibazo canyuma



1. Shira umuriro mu mashine y’umwotsi (220V) hanyuma uyifungure


2. Gutanga ubushobozi kuri ESP32 (bateri canke USB)


3. Fungurira BTCPay PoS yawe mu mucukumbuzi wawe


4. Scan "umwotsi-imashini" ikintu


5. Wishura n’umuravyo wallet (Blink canke uwundi wallet)


6. Iyumvire:




 - Relay gukanda (ijwi ryumvikana n'umuco w'i LED)
 - Imashini y'umwotsi irakora
 - Umwotsi waravutse!



### Ingorane n'umuti w'ubutungane



| **Problème**                        | **Cause probable**              | **Solution**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 ne se connecte pas            | Driver USB manquant             | Installer [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| Relais ne clique pas                | Mauvais câblage GPIO            | Vérifier GPIO 21 → IN                                                                        |
| Smoke machine ne réagit pas         | Télécommande mal câblée         | Vérifier NO/NC/COM                                                                           |
| WebSocket timeout                   | URL incorrecte                  | Vérifier wss:// et /bitcoinswitch                                                            |
| WiFi ne se connecte pas             | SSID/Password erroné            | Re-flasher la config WiFi                                                                    |
| Paiement reçu mais rien ne se passe | ESP32 non connecté au WebSocket | Vérifier les logs RESET                                                                      |

## Ubutunzi



### Amahuza ngirakamaro





- BitcoinSwitch Porogaramu nkuru: [ihindura ry'ibice.
- Inyandiko za Serveri ya BTCPay : [inyandiko.serveri.org/](inyandiko.serveri.org/)
- Blink API : [ubutumwa bw'imbere.sv/] (ubutumwa bw'iterambere.
- ESP32 Pinout : [ivyigwa vy'ubuhinga.com/esp32-ivyigwa-vy'ubuhinga-gpios/]



### Umuryango & Infashanyo





- Serveri ya BTCPay** : [ubutumwa.btcpayserver.org/) - Ikintu gihambaye kuruta ibindi vyose
- Serveri ya BTCPay Telegram** : [t.me/serveri ya btcpay](https://t.me/serveri ya btcpay)
- LNbits** : [ibice] - Telegram yemewe, umuryango ukora
- BitcoinSwitch (ibibazo vya porogaramu)**: [ibibazo] (ibibazo)



### Kode y'inkomoko





- Kode y'inkomoko ya porogaramu nkuru ya BitcoinSwitch:



---

**⚡** Stack sats, ukore umwotsi, winovore, ugume wicishije bugufi! **⚡**