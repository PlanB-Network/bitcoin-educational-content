---
name: Satoshi Wallet
description: Lihtsaim hooldusvahendi Wallet alustamiseks
---
![cover](assets/cover.webp)

_Selle õpetuse on kirjutanud_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)


## Satoshi Wallet allalaadimine, seadistamine ja kasutamine


Wallet Satoshi on Lightning Network Wallet, eestkostetav ja väga lihtne kasutada.

Kursuse [BTC105 - Finding Now](https://planb.network/it/courses/trovarsi-ora-d1370810-63f6-4aba-b822-e3a66bf225a5) puhul kasutatakse seda Redeem Lightning Network vautšeriteks.


**Mäleta alati**: _ei oma võtmeid, mitte oma münte_


Hoiukassad ei võimalda kasutajatele täielikku kontrolli oma raha üle. Neid ei soovitata tavaliselt, välja arvatud algajatele. WoSi tuleks kasutada üleminekuperioodi Wallet või taskuraha hoidmiseks, mitte pikaajalise fondi kogumiseks.


---

Wallet of Satoshi (WoS) on hooldustoode, kuid sellel on teatav maine. Me võime mõistlikult pöörduda näiteks WoS-i taolise vahendi poole, et suurendada oma võimet saada likviidsust. Me delegeerime WoSile ajutiselt "räpase töö", milleks on kanalite likviidsuse haldamine meie eest. Kui teatud summa on saavutatud, tühjendame WoSi On-Chain meie mittehooldusvalitsuse Wallet jaoks.


**WARNING⚠️: Enne jätkamist on soovitatav lugeda juhendmaterjal tervikuna läbi**


### Satoshi Wallet allalaadimine


Mine Play Store'i ja lae alla WoS


![image](assets/it/01.webp)


**Märkus:** WoS on allalaaditav ainult ametlikest kauplustest. Kui seadme operatsioonisüsteem on programmeeritud, siis enne WoS-i avamist toimub operatsioonisüsteemi enda poolt kontroll. Pärast verifitseerimisfaasi valige _Open_.


![image](assets/it/02.webp)


Satoshi Wallet avaneb järgmise ekraaniga ja tuleb klõpsata nuppu _Start_


![image](assets/it/03.webp)


### WoS-i konto registreerimine


Sel hetkel on Wallet juba töökorras, kuid suurema turvalisuse tagamiseks jätkame sisselogimise seadistamist: seda on vaja vahendite taastamiseks seadme rikke või kaotsimineku korral. Seetõttu valige vasakus ülaosas olev menüü.


![image](assets/it/04.webp)


Avaneb kogu menüüaken, milles tuleb vastavalt maitsele määrata ainult valuuta (Wallet Satoshi vaikimisi esitab USA dollarit kui võrdlusvaluutat) ja teemavärvi (heledat/tumedat). Teisi käske ei kasuta.


Kuna WoS on hooldusvahend, ei saa me Wallet varundada Mnemonic fraasiga, kuid me saame lubada WoSil taastada meie raha, kui mobiilse seadme kaotamise või mittekasutamise korral, klõpsates _Login/Register_

Ilmub aken, kus palutakse sisestada e-posti aadress Address. See võib olla **Proton mail** (soovitatav), kuid see peab olema toimiv, sest see võimaldab meil mobiiltelefoni kadumise/varguse või kahjustumise korral Wallet raha tagasi saada.


![image](assets/it/08.webp)


Wallet Satoshi on saatnud sõnumi näidatud e-postkasti.


![image](assets/it/09.webp)


Postkastist leiame kaks sõna, mida peame sisestama, kirjutades need ümber, rakenduse poolt etteantud ruumi.


- ärge aktiveerige tõlkijat: sõnad on ja peavad jääma inglise keelde**
- kirjutage kaks sõna ümber, pöörates tähelepanu suurtele/väikestele tähtedele**


![image](assets/it/10.webp)


Pärast kahe sõna ümberkirjutamist klõpsake nuppu _OK_.


![image](assets/it/11.webp)


Tulemuseks peaks olema ülesse ilmuv pilt, millel on kontrollimise sümbol.


![image](assets/it/12.webp)


kui seadete sektsioonis kuvatakse nüüd punasel _Login/Register_ ribal kasutaja e-posti aadress Address.


![image](assets/it/13.webp)


### Maksete vastuvõtmine


WoS-i vastuvõtmiseks klõpsake nuppu _Võta_ ja ekraanile ilmub rida käske.


![image](assets/it/14.webp)


Võite saada


- gW-30-Address kaudu **a**
- gW-32 kaudu, seadistades Invoice **b**
- on chain (WoS toetab Bitcoin võrku, kuid tasuliste allveelaevade vahetustega) **c**
- skaneerides LNurl-p **d** QR-koodi


![image](assets/it/15.webp)


### Invoice loomine


Klõpsake nuppu _Vastuvõtmine_ ja valige Lightning Network sümboliga käsk.


![image](assets/it/16.webp)


Ilmub Invoice loomise menüü, kus me vajutame _Add Amount_, et kirjutada täpne summa ja lisada kirjeldus, antud näites "Minu esimene Invoice".


![image](assets/it/17.webp)


Klaviatuuri abil määrame summa.


![image](assets/it/18.webp)


et siis saada tasu Invoice. Saadud makse näeb välja selline:


![image](assets/it/19.webp)


### Kogumine POS-ist


Wallet Satoshi-l on vaikimisi funktsioon, mis muudab selle eriti sobivaks kaupmeestele: POS. Vaatame, kuidas seda aktiveerida.


Valige põhiekraanil paremal üleval olev menüü.


![image](assets/it/20.webp)


Seejärel valige _Müügipunkt_.


![image](assets/it/21.webp)


WoSi viimases versioonis valige kindlasti _Keypad_.


![image](assets/it/22.webp)

ja seejärel sisestage summa klaviatuurile, järgnevas näites võrdne 10 senti / 118 Sats. Lisage kogumise kirjeldus, antud juhul "minu teine koos POS-iga". Suur nupp Green süttib ja sellele tuleb vajutada

![image](assets/it/23.webp)


gW-43 Invoice ja näidata seda näiteks kliendile.


![image](assets/it/24.webp)


See makse on samuti kogutud!


![image](assets/it/25.webp)


### Maksete saatmine


Lihtsus on WoSi põhiekraani tugevus. Invoice maksmiseks klõpsake nuppu _Send_


![image](assets/it/26.webp)


Esimesel kasutamisel küsib WoS luba kaamerale juurdepääsuks


![image](assets/it/27.webp)


Sellest hetkest alates aktiveerub kaamera


![image](assets/it/28.webp)


Raamides Invoice, näeme, et on taotletud 210 Sats makset. Loetakse ka kirjeldus, kui taotleja on selle esitanud. Sellel ekraanil on kokkuvõte ja ka kinnituse taotlus: WoS "küsib makse saatmiseks luba", mis antakse, kui klõpsata nupule Green _Send_


![image](assets/it/29.webp)


Kui makse jõuab sihtkohta, teavitab WoS selle ekraaniga


![image](assets/it/30.webp)


Vajutades põhiekraanil lingile _History_ (kohe saldo all), ilmub tehingute nimekiri


![image](assets/it/31.webp)


#### WoS-i konto taastamine


Nüüd vaatame, kuidas WoSi uude seadmesse paigaldada; see on kasulik ka juhul, kui mobiiltelefon, millele Wallet oli varem paigaldatud, on varastatud, kaotatud või ei saa seda kasutada. Pärast uuesti paigaldamist tuleb äsja selgitatud konto registreerimise protseduur uuesti läbi viia, ühe variandiga: varem määratud e-posti aadressiga sisselogimise nõude lõpus ilmub WoS sellisena:


![image](assets/it/33.webp)


Sõnum hoiatab, et on saadetud e-kiri konto taasaktiveerimise protseduuriga. Te peate avama oma e-postkasti.


**TÄHELEPANU**: avage e-kiri arvutist või igal juhul muust seadmest kui see, millega kavatsete WoS-kontot taastada. Postkastis leiame sõnumi, mis näitab meile QR-koodi, mida tuleb raamida


![image](assets/it/34.webp)


Kui QR-kood on raamitud, ilmub WoSi pealehele taastatud konto koos saldo ja ajalooga.