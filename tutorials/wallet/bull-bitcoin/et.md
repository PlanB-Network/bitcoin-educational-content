---
name: Bull Bitcoin Wallet
description: Uurige, kuidas kasutada Wallet Bull Bitcoin
---

![cover](assets/cover.webp)



Selles juhendis tutvustatakse teile Bull Bitcoin Mobile'i paigaldamist, konfigureerimist ja kasutamist. Saate teada, kuidas võtta vastu ja saata raha kolmes võrgus: onchain, Liquid ja Lightning ning kuidas Bitcoin-i ühest võrgustikust teise üle kanda. Lisades on esitatud ressursid ja kontaktid, taustateave ja tehniliste mõistete lühiselgitused.



## Sissejuhatus



**Bull Bitcoin Mobile**, mille on välja töötanud **[Bull Bitcoin](https://www.bullbitcoin.com/)** ([loo konto](https://app.bullbitcoin.com/registration/orangepeel)), on **iseseisev** Bitcoin Wallet, mis tähendab, et teil on täielik kontroll oma isiklike võtmete ja seega ka raha üle, ilma et te sõltuksite kolmandast isikust. Avatud lähtekoodiga ja Cypherpunk-filosoofial põhinev Wallet ühendab endas lihtsuse, konfidentsiaalsuse ja täiustatud funktsioonid, nagu võrkudevahelised vahetused ja PayJoin tugi. See võimaldab teil hallata oma bitcoine kolmes võrgus: **Bitcoin onchain**, **Liquid** ja **Lightning**, millest igaüks on kohandatud konkreetsetele kasutusviisidele.



### Arengu kontekst



Wallet vastab suurele väljakutsele: Bitcoin võrgutasud ei sobi väikeste maksete tegemiseks või väikeste isehostetavate Lightning-kanalite avamiseks. Wallet Bull Bitcoin Mobile pakub isekasutatavat lahendust, tuginedes samal ajal 3 peamisele Bitcoin võrgule:





- **Bitcoin võrk (onchain)**: Ideaalne UTXOde ja suure väärtusega tehingute keskmise ja pikaajalise säilitamise jaoks, kus tasud on proportsionaalselt tähtsusetud.
- **Liquid Network**: Mõeldud kiireks (~2 minutit), konfidentsiaalsemaks (varjatud summad) ja odavaks tehinguks, mis sobib ideaalselt väikeste summade kogumiseks või privaatsuse kaitsmiseks.
- **Lightning** võrk: Optimeeritud koheseks ja odavaks maksmiseks, mis sobib väikese ja keskmise väärtusega igapäevatehinguteks.



Näiteks Bull Bitcoin Mobile'iga saate koguda väikeseid summasid **Liquid** või **Lightning** portfellis ja kui olete saavutanud märkimisväärse summa, saate :





- Ülekandmine onchain-võrku turvaliseks keskmise või pikaajaliseks säilitamiseks, millel on parem konfidentsiaalsus koos Liquid ja/või Lightningiga ülespoole ning onchain-tasud ühe tehingu eest



### Pidev areng



Wallet areneb pidevalt, seega ärge imestage, kui leiate lahknevusi selle õpetuse ja teie ajakohase rakenduse vahel.




- Näiteks alates 19.07.2025 on **"Osta / Müü / Maksa "** nupud nähtavad, kuid rakenduses hallatud, kuna need valikud, mis on saadaval Exchange [bullbitcoin.com](https://app.bullbitcoin.com/registration/orangepeel), integreeritakse peagi ühtseks kogemuseks. Nende kasutamine jääb täiesti vabatahtlikuks. Paljud muud arendused on käimas või plaanis: mitme Wallet haldamine, passphrase, ühilduvus riistvaraliste rahakottidega...
- [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49), saate tutvuda praeguste teemade ja tulevaste arengutega. Kuna projekt on 100% avatud lähtekoodiga ja "avalikult ehitatud", saate meile saata ka oma ettepanekuid ja kõiki vigu, millega te kokku puutute.




## 1. Eeltingimused



Enne **Bull Bitcoin Mobile** kasutamise alustamist veenduge, et teil on olemas järgmised esemed:





- **Ühilduv nutitelefon**: **iOS** (iPhone või iPad) või **Android** seade
- Interneti-ühendus
- **Turvaline varunduskandja**: Kirjutage oma **tagasivõtmislause** (12 sõna) paberile või metallile ja hoidke seda turvalises kohas.
- **Põhiteadmised**: Bitcoin mõistete (aadressid, tehingud, tasud) minimaalne mõistmine on kasulik, kuigi see õpetus selgitab iga sammu algajatele.



## 2. Paigaldamine





- Lae taotlus alla:
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&pcampaignid=web_share) **Lae alla Android-seadmetele mõeldud rakenduste poest**
- [GitHub](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) **Laadige APK Android-seadmetele otse alla**
- [iOS](https://testflight.apple.com/join/FJbE4JPN) **Lae alla TestFlight'i kaudu Apple'i seadmetele**
 - Kontrollida arendaja nime (Bull Bitcoin), et vältida petturlikke taotlusi.
 - Veenduge, et allalaaditud versioon vastab GitHubis märgitud viimasele stabiilsele versioonile.
 - Bull Bitcoin Mobile on **avatud lähtekoodiga**. Koodi vaatamiseks: [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49)





- Installige rakendus




## 3. Esialgne konfiguratsioon



### 3.1 Käivitage rakendus :



Taotluses kasutatakse mõlema portfelli jaoks unikaalset 12-sõnalist taastamislauset:




- **turvaline Bitcoin Wallet**: Tehinguteks Bitcoin võrgus (onchain)
- **Kohesed maksed Wallet**: Liquid ja Lightning võrkudes tehtavate koheselt tehtavate tehingute jaoks



Avamisel palutakse teil importida olemasolev taastamislause või luua uus Wallet :



![image](assets/fr/02.webp)



### 3.2 Recovery fraas :



Kui soovite olemasolevat Wallet uuesti kasutada, klõpsake "**Recover Wallet**" ja täitke 12 sõna oma taastamislauset.



Vastasel juhul klõpsake nuppu "**Loo uus Wallet**" :




- Kirjutage oma taastumisfraas ülima hoolikusega üles. Kirjutage see paberile või metallile ja hoidke seda turvalises kohas (seif, offline-koht). See fraas on teie ainus vahend, mille abil saate oma bitcoinidele ligi, kui seade kaob või rakendus kustutatakse.
- Samuti on oluline märkida, et igaüks, kes seda lauset kasutab, võib kõik teie bitcoinid varastada. Ärge kunagi salvestage seda digitaalselt:
 - Puudub ekraanipilt
 - Pilve, e-posti või sõnumite varukoopiaid ei ole
 - Ei ole kopeerimist/liitmist (oht, et salvestatakse lõikelauale)



**! See punkt on kriitiline**. Täiendava abi saamiseks :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 3.3 Juurdepääsu tagamine :





- Mine seadistustesse ja klõpsa seejärel **PIN-kood**.
- Seadistage kindel **PIN-kood**, et kaitsta juurdepääsu rakendusele.
- See samm on vabatahtlik, kuid tungivalt soovitatav, et keegi, kellel on juurdepääs teie telefonile, ei saaks juurdepääsu teie Wallet-le.



![image](assets/fr/03.webp)



### 3.4 Ühendus isikliku sõlmpunktiga (valikuline):



Wallet BullBitcoin ühendub vaikimisi Electrumi serveritega: esimene, mida haldab Bull Bitcoin ja teine Blockstream'i server, mis mõlemad ei pea logisid, vähendades jälgimise riski.



Suurema konfidentsiaalsuse tagamiseks saate rakenduse ühendada oma Bitcoin sõlme Electrumi serveri kaudu (juhised on saadaval [BullBitcoini GitHubis](https://github.com/orgs/SatoshiPortal/projects/49) ).




## 4. Raha saamine



Raha vastuvõtmine **Bull Bitcoin Mobile** abil on lihtne ja kohandatud teie vajadustele, olenemata sellest, kas kasutate :




  - **Bitcoin (onchain)** võrk pikaajalise säilitamise eesmärgil,
  - **Liquid** võrk kiireks, rohkem Confidential Transactions,
  - **Lightning** võrk, mis võimaldab koheseid, väikese väärtusega makseid.



Rakendus genereerib automaatselt Lightning-vastuvõtu või Invoice-aadressid, sõltuvalt valitud võrgust. Järgnevalt on kirjeldatud, kuidas iga võrgu puhul toimida.



### 4.1. onchain (Bitcoin võrk)



Avakuval saate :




- või valige **Secure Bitcoin Wallet** ja seejärel klõpsake "**Vaata "** :



![image](assets/fr/04.webp)





- või klõpsake "**Vastuvõtmine "** ja seejärel valige **Bitcoin** võrk:



![image](assets/fr/05.webp)



#### 4.1.1. Ainult Address kopeerimine või skaneerimine" valik on välja lülitatud (vaikimisi)



![image](assets/fr/06.webp)





- See annab juurdepääsu valikulistele täiustatud parameetritele. Saate määrata :
 - **summa** BTC, Sats või fiat.
 - **Isiklik märkus**, mis lisatakse URI / QR-koodi koopiale.
 - **PayJoin** aktiveerimine (vt 3. liide), mis parandab konfidentsiaalsust, ühendades saatja ja vastuvõtja kirjed.





- Näide automaatselt genereeritud URI-st:



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=2.1e-7&message=Exemple+de+note&pj=HTTPS%3A%2F%2FPAYJO.IN%2FUJA9LJ6L4CMHY%23RK1QT3YSGFC6PMKRUXND2DSGQMLESTUNH29AY0305XAQ678742CVT5ES+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1RRH8C6Q
```





- **Kasutamine**: Kopeeri URI, et seda saatjaga jagada, või lase tal QR-koodi skaneerida.



#### 4.1.2. Ainult Address kopeerimine või skaneerimine" valik on lubatud



![image](assets/fr/07.webp)





- Kui valik **"Ainult Address kopeerimine või skaneerimine "** on lubatud, genereerib rakendus lihtsa Bitcoin Address SegWit (bech32) formaadis.





- Näide:



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```



Isegi kui te sisestate summa või märkuse, ei lisata neid QR-koodi ega Address koopiasse





- **Kasutamine**: Kopeeri Address, et seda saatjaga jagada, või lase tal QR-koodi skaneerida.



#### 4.1.3. Uue Address genereerimine





- Miks kasutada iga tehingu jaoks uut Address? See **kaitseks teie privaatsust**, kuna see takistab mitme makse sidumist sama Address-ga ja piirab jälgimise võimalusi Blockchain-ga.
- Vaikimisi genereerib Bull Bitcoin automaatselt kasutamata **Address**.
 - Uue Address loomist saate sundida, kui klõpsate ekraani allosas oleval nupul **"Uus Address"**.
 - Kõik teie aadressid on seotud teie seed fraasiga: olenemata sellest, kui paljusid aadresse te kasutate, kuvatakse teie portfellis üksainus saldo, mis võib saadetiste saatmisel automaatselt vahendeid konsolideerida.





- Vihje: Kasutage alati uut **Address**, mida pakub Bull Bitcoin, välja arvatud juhul, kui teil on konkreetne vajadus (nt avalik Address annetuste vastuvõtmiseks).



### 4.2. Liquid



Avakuval saate :




- või valige **Pikamaksed Wallet**, seejärel klõpsake **"Saamine "** ja seejärel **"Liquid"** :



![image](assets/fr/08.webp)





- või klõpsake "**Vastuvõtmine "** ja seejärel valige **Liquid** võrk:



![image](assets/fr/09.webp)



Kui olete ekraanil **"Receive "**, kopeerige Liquid Address:





- Summa või märkus puudub. Näide:



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```





- Või määrates **summa** (BTC, Sats või fiat) ja/või **isikliku märkuse**, mis lisatakse URI / QR-koodi koopiasse. Näide:



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



**Kasutus**: Kopeeri Address/URI, et seda saatjaga jagada, või lase tal QR-koodi skaneerida.



### 4.3. Välk



Avakuval saate :




- või valige **Pikamaksed Wallet** ja seejärel klõpsake "**Võta vastu "** :



![image](assets/fr/10.webp)





- või klõpsake "**Vastuvõtmine "** ja seejärel valige **Valguse** võrk:



![image](assets/fr/11.webp)



#### 4.3.1. Toimimine, piirangud ja eelised





- **Mehhanism**: Wallet: Bull Bitcoin Wallet on Wallet, mis võimaldab makseid teha ja vastu võtta välklambi kaudu. Lightning'i kaudu saadud raha salvestatakse **Liquid** võrgus (Wallet Instant Payments'is) tänu automaatsele vahetusele **Boltz** kaudu. See annab teile võimaluse suhelda Lightninguga, ilma et peaksite likviidsuskanaleid haldama, jäädes samal ajal isehoidjaks.





- **Piirangud:**
- **Minimaalne summa** on 100 satoshi (seisuga 19.07.2025), kui te generate Invoice.
- Te maksate kulud, mis arvatakse saatja poolt saadetud summast maha, erinevalt Wallet Lightning native'iga vastuvõtmisest, kus ainult saatja maksab ülekandekulud lisaks saadetud summale. Seisuga 19/07/2025, 47 Sats arvatakse saadetud summast maha.





- **Eelised**:
- **Iseseisvalt hooldatav**: Teie rahalised vahendid jäävad teie kontrolli alla, neid hoitakse Liquid Network-s.
- **Ei mingeid kõrgeid tasusid**: Liquid ladustamine väldib kulukaid hoiuseid, et avada oma Lightning-kanal või lisada likviidsust. Neid toiminguid saab teha hiljem, kui Liquid-s kogunenud summa õigustab tasusid.





- **Vihje:** Kui saatjal on Wallet Bull Bitcoin, kasutage vahetustasu vältimiseks otse Liquid Network



#### 4.3.2. generate Invoice





- Sisestage **summa** (BTC, Sats või fiat)





- Lisage **isiklik märkus**, mis integreeritakse Invoice-sse. Kui saatja maksab Invoice, lisab teie Wallet selle samuti tehingu üksikasjadesse.





- **Invoice kehtivusaeg:** Välk Invoice kehtib **12 tundi**. Selle aja möödudes kaotab see kehtivuse ja selle eest ei saa enam maksta. Tuleb genereerida uus Invoice.





- **Kasutamine**: Invoice, et seda saatjaga jagada, või laske tal QR-koodi skaneerida.




## 5. Raha saatmine



### 5.1. Põhimõte



Kas kodulehelt või rahakotidest :



![image](assets/fr/12.webp)



et pääseda saatmise ekraanile:



![image](assets/fr/13.webp)



**Bull Bitcoin Mobile** muudab raha saatmise lihtsaks, tuvastades automaatselt võrgu (Bitcoin, Liquid või Lightning) sisestatud Address või Invoice (kopeeritud või QR-koodi abil skaneeritud) alusel.



### 5.2. ahelasisene edastamine (Bitcoin võrk)



#### 5.2.1. Saada ekraan



**Action**: Sisestage või skannige Bitcoin onchain Address





- Kui summa ei ole määratletud, näiteks :



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```





- Seejärel saate saatmise ekraanil valida :
 - Summa BTC, sat või fiat. Minimaalne summa: 546 satoshis 22/07/2025.
 - Valikuline märkus tehingu identifitseerimiseks. Nähtav ainult teile, tehingu üksikasjades.



![image](assets/fr/14.webp)





- Kui summa on juba määratletud, näiteks :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Seejärel suunatakse teid otse allpool olevale kinnitusekraanile.



#### 5.2.2 Kinnitusekraan



Võtke aega, et kontrollida kõiki parameetreid, eriti summat, sihtkoha Address ja tasusid.


Seejärel saate parameetreid reguleerida:



![image](assets/fr/15.webp)




- **Tasud**: Saate valida :
- Kas teie tehingu täitmise kiirus ja sellega seotud tasud on hinnangulised
- Kas tasud, absoluutsete tasude (kogukulud satoshi) või suhteliste tasude (tasud baidi kohta) režiimis, ja teie tehingu kiirus on hinnanguline





- **Täiustatud seaded**:





- **Replace-by-fee (RBF)**: See funktsioon on vaikimisi aktiveeritud ja kiirendab tehingut, makstes suuremat tasu (üksikasjad vt 4. liites).





- **UTXO** käsitsi valimine: Kui teie raha on salvestatud mitmel erineval Wallet-aadressil, saate valida aadressid, kust raha saata. Miks peaksite seda tegema? Seoses Bitcoin üha laialdasema kasutamisega tõusevad ülekandetasud. Väikeste summade saatmine mitmest aadressist on kallim kui saatmine ühest Address-st, kuid kui teete seda praegu, väldite seda hiljem, kui tasud on veelgi kõrgemad. Seda nimetatakse **konsolideerimiseks UTXO**.



![image](assets/fr/16.webp)





- Saatmine koos **PayJoin**: Kui funktsioon on aktiveeritud saaja poolt, kes andis URI, nt :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Seejärel konfigureerib Bull Bitcoin Mobile saatmise, kombineerides teie UTXO-d vastuvõtja UTXO-dega, mis parandab konfidentsiaalsust (vt 3. liites üksikasjad).



### 5.3. Saada Liquid-le



#### 5.3.1 Saada ekraan



**Liquid** võrk võimaldab kiireid tehinguid (~2 minutit tänu ühele plokile minutis), konfidentsiaalsemaid (maskeeritud summad) kui onchain-võrgus ja väga madalate tasudega. Raha võetakse välja **Instant Payments Wallet**-st.



**Action**: Sisestage või skannige Liquid Address





- Kui summa ei ole määratletud, näiteks :



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```



Seejärel saate saatmise ekraanil valida :




- Summa BTC, sat või fiat. Ei ole miinimum, 1 Satoshi võimalik;
- Valikuline märkus tehingu identifitseerimiseks. Nähtav ainult teile, tehingu üksikasjades.



![image](assets/fr/17.webp)





- Kui summa on juba määratletud, näiteks :



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



Seejärel suunatakse teid otse allpool olevale kinnitusekraanile.



#### 5.3.2 Kinnitusekraan



Võtke aega, et kontrollida kõiki parameetreid, eriti kogust ja sihtkohta Address.



![image](assets/fr/18.webp)





- **Tasud**: Proportsionaalselt tehingu keerukusega, üldiselt 0,1 sat/vB alusel, st 20-40 satoshit lihtsa tehingu puhul (33 Sats seisuga 22.07.2025).



### 5.4. Saada välkule



#### 5.4.1 Saada ekraan



**Lightning** võrk võimaldab koheseid ja odavaid makseid väikeste summade eest, mis on ideaalne väikeste igapäevaste tehingute tegemiseks.



**Action**: Sisesta või skaneeri välk Invoice





- Kui skaneerite LN-URL Address, mis võimaldab määrata summa


Näide: "orangepeel@walletofsatoshi.com".


siis saate saata ekraanil valida :




 - Summa BTC, sat või fiat. Minimaalne summa 1000 satoshis 23/07/2025
 - Valikuline märkus tehingu identifitseerimiseks. See saadetakse saajale.



![image](assets/fr/19.webp)





- Kui skaneerite Lightning Invoice, mis sisaldab kindlaksmääratud koguse


Näide:



```
lnbc210n1p58hhk6bullbitcoint4a9jq34dmrmcrursjmw3wjf8elz0nxtdsw9pscqzyssp52jg9dm8vc3xy26er5rc965lxjllhd82je97au7ysvv6lpq7r7shs9q7sqqqqqqqqqqqqqqqqqqqsqqqqqysgqdqqmqz9gxqyjw5qrzjqwryaup9lh50kkranzgcdnn2fgvx390wgj5jd07rwr3vxeje0glclle6wrlm37k39uqqqqlgqqqqqeqqjqnf7w9f2evnzptm2vtdknk7483hsndkl98c4mv2kfe64v5pkq0j6x2dqt9y9wayszv3z33az7c8hkj3yqj9jd7ans7ugq8xv0xefp23gqltph72
```



Seejärel suunatakse teid otse allpool olevale kinnitusekraanile.



Märkus: summa peab olema suurem kui 21 Sats seisuga 23.07.2025



#### 5.4.2 Toimimine, piirangud ja eelised





- **Mehhanism**: Raha võetakse **Instant Payments Wallet** (Liquid) ja konverteeritakse **Liquid → Lightning** vahetuse kaudu **Boltziga**.





- **Piirangud:**
- Minimaalne summa, mis on suurem kui **Wallet Lightning native** (vt eespool)
- **Kulud** pluss Liquid → välguvahetus Boltzi kaudu





- **Eelised**:
- **Iseseisvalt hooldatav**: Teie rahalised vahendid jäävad teie kontrolli alla, neid hoitakse Liquid Network-s ja vajadusel saab neid Lightning'i kaudu üle kanda
- **Ei mingeid kõrgeid tasusid**: Liquid-s hoiustamine on säästnud teid kulukate onchaini hoiuste eest, et avada oma Lightning-kanal või lisada likviidsust. Neid toiminguid saab teha hiljem, kui Liquid-s kogunenud summa õigustab tasusid.





- **Vihje:** Kui vastuvõtjal on Wallet Bull Bitcoin, kasutage otse Liquid Network, et vältida vahetuskulusid



#### 5.3.3 Kinnitusekraan



Võtke aega, et kontrollida kõiki parameetreid, eriti kogust ja sihtkohta Address.



![image](assets/fr/20.webp)




## 6. Vaata ajalugu



**Bull Bitcoin Mobile** võimaldab hõlpsasti jälgida oma tehinguid **Bitcoin (onchain)**, **Liquid** ja **Lightning** võrkudes. Ajalugu saab vaadata kahel viisil ja kuvab üksikasjalikku teavet iga tehinguliigi kohta. Samuti saate oma tehinguid kontrollida, kasutades väliseid plokibrausereid.



### 6.1. Juurdepääsu ajalugu





- **Avakuva kaudu** :
 - Klõpsake **Secure Bitcoin Wallet**, et vaadata **onchain** tehinguid, või **Instant Payments Wallet**, et vaadata **Liquid** ja **Lightning** tehinguid.
 - Ajalugu kuvatakse otse portfelli kogusumma all, filtreerituna vastavalt valitud Wallet tüübile.



![image](assets/fr/21.webp)





- **Spetsiaalse lehekülje** kaudu:
 - Klõpsake avakuval **ajaloo sümbolil** (kella ikoon vms).
- Juurdepääs leheküljele, kus on loetletud kõik tehingud koos filtritega tegevuse tüübi järgi: **(Märkus: Müüa ja osta on arendamisel ja ei ole praegu, 20. juuli 2025, veel saadaval)**.



![image](assets/fr/22.webp)



### 6.2. Tehingu üksikasjad



Iga tehingu kohta kuvatakse konkreetne teave sõltuvalt võrgust ja tegevuse tüübist (saatmine või vastuvõtmine). Siin on andmed, mis on saadaval **transaction onchain** kohta:



![image](assets/fr/23.webp)



### 6.3. Kontrollimine Block explorer kaudu



**Bitcoin onchain**, **Liquid** ja **Lightning** võrkude uurijate nimekiri on esitatud 4. liites.



**Lightning** puhul ei ole tehingud avalikes veebilehitsejates nähtavad. Kontrollige üksikasju (sh vahetustunnust Boltzile) taotluses.




## 7. Seaded



Lehele "Seaded" pääseb otse rakenduse Bull Bitcoin avalehelt ning seda kasutatakse portfelli ja kasutajakogemuse erinevate aspektide konfigureerimiseks ja haldamiseks.



![image](assets/fr/24.webp)





- **Wallet varukoopia**: Kuvab portfelli taastamislauset turvalise varundamise jaoks. Vt taastamislause haldamise ja salvestamise parimaid tavasid portfelli loomise kohta jaotises 3.





- **Wallet üksikasjad**:
- **Pubkey**: Wallet-ga seotud avalik võti, mida kasutatakse Bitcoin vastuvõtuaadresside genereerimiseks.
- **Tuletamise tee**: generate Wallet aadresside tuletamise tee, mida kasutatakse generate Wallet aadresside tuletamiseks privaatvõtmest.





- **Electrum server (Bitcoin sõlme)**: Seadistage ühendus kohandatud Bitcoin sõlme jaoks onchain-tehingute jaoks.





- **PIN-kood**: Aktiveerige ja/või muutke turvakoodi, et kaitsta juurdepääsu rakendusele ja Wallet funktsioonidele.





- **Valuutta**: Valige, kas summad kuvatakse BTC või Sats ja vaikimisi fiat-valuuta (dollar, euro jne).





- **Automaatne vahetus seaded**: Funktsioon _Auto Swap_ võimaldab teil automatiseerida oma BTC ülekandmist **Instant Payments Wallet (Liquid)**-st oma **Bitcoin On-Chain** Wallet-sse, niipea kui summa saavutab künnise, mida te peate piisavalt suureks, et õigustada tehingutasu.





- **Logid**: Vaadeldavad tegevuslogid, mida saab jagada tehnilise toega, et hõlbustada tõrkeotsingut.





- **Telegrammi ligipääs toetuse saamiseks**: Otselink ametlikule Telegrami kanalile kasutajaabi saamiseks.





- **Githubi juurdepääs**: Link [Bull Bitcoin Githubi repositooriumi](https://github.com/SatoshiPortal) juurde, et vaadata avatud lähtekoodiga koodi või teatada probleemidest.




## LIITED



### A1. PayJoin selgitus (P2EP)



![image](assets/fr/25.webp)



**Määratlus** :




- PayJoin ehk **Pay-to-EndPoint (P2EP)** on Bitcoin tehingutehnika, mis suurendab konfidentsiaalsust **onchain** võrgus. See ühendab saatja ja vastuvõtja kirjed ühte tehingusse, mis muudab summad ja aadressid raskemini jälgitavaks.



**Operatsioon:**




- PayJoin tehingu puhul teevad saatja ja vastuvõtja ühilduva PayJoin serveri kaudu koostööd generate ühise tehingu tegemiseks.
- Selle asemel, et ainult saatja esitab kirjeid (UTXO), annab ka vastuvõtja oma panuse ühe oma UTXOga. See ähmastab Blockchain-s nähtavat teavet: tegelikule summale vastava ühe kande asemel on nüüd kaks kannet ja väljundid ei kajasta otseselt vahetatud summat.
- Lõplik tehing sarnaneb tavalise Bitcoin tehinguga (mitme sisendi ja mitme väljundiga), kuid tänu steganograafilisele struktuurile on tegelik saadetud summa ja aadresside vahelised seosed varjatud.



**Kasutamiseks Bull Bitcoin Mobile'is**




- **Vastuvõtmine** (Address Supply): PayJoin on vaikimisi lubatud.
- **Saada**: Wallet tuvastab automaatselt PayJoin URI ja konfigureerib tehingu vastavalt, näiteks:



```
bitcoin:bc1qp2nxbullbticoinzt6tx7x5tlnpzhv37?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F475QR36G3ZCFZ%23...
```




**Eelised**




- **Täiustatud konfidentsiaalsus**: PayJoin tühistab eelduse, et kõik kirjed tehingus kuuluvad ühele üksusele. PayJoin puhul tulevad sisendid nii saatjalt kui ka vastuvõtjalt, mis rikub selle eelduse.
- **Summa maskeerimine**: Tegelik vahetatud summa ei ilmne otse väljundites. See arvutatakse vastuvõtja UTXO sissetuleva ja väljamineva summa vahena, mis muudab analüüsi eksitavaks.



**Piirangud**




- PayJoin nõuab, et saatja ja vastuvõtja kasutaksid ühilduvaid rahakotte, vastasel juhul kasutatakse standardset ahelatehingut.
- Tehing on veidi keerulisem (rohkem sisendeid ja väljundeid), mille tulemuseks on veidi suuremad kulud.
- Ehkki see on kavandatud sarnanema standardsele tehingule, võib arenenud heuristika (nt mitmetähenduslikud väljundid, tuntud PayJoin serverid) anda alust kahtlustada selle kasutamist, kuigi ilma absoluutse kindluseta.



**Lisainfo:**




- [Sõnastik](https://planb.network/fr/resources/glossary/payjoin)
- Chapitre [Les transactions PayJoin](https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c/c1e90b95-f709-4574-837b-2ec26b11286f)




### A2. Replace-by-fee (RBF) selgitus



**Määratlus**: Replace-by-fee (RBF) on Bitcoin võrgu funktsioon, mis võimaldab saatjal kiirendada **onchain** tehingu kinnitamist, nõustudes maksma kõrgemat tasu.



**Piirangud** :




- RBF ei ole saadaval Liquid või Lightning-tehingute puhul.
- Esialgne tehing tuleb selle loomisel märkida RBF-ga ühilduvaks, mida Bull Bitcoin Mobile teeb automaatselt, kui see ei ole keelatud.



**Lisainfo:**




- [Sõnastik](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. Parimad tavad



**Bull Bitcoin Mobile** turvaliseks ja tõhusaks kasutamiseks järgige järgmisi soovitusi. Need aitavad teil kaitsta oma raha, optimeerida tehinguid ja säilitada konfidentsiaalsust **Bitcoin (onchain)**, **Liquid** ja **Lightning** võrkudes.





- **Kindlustage oma taastumisfraas** :
 - Tutorial: [Save your Mnemonic phrase](https://planb.network/fr/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270)
 - Cours [La phrase mnémonique](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8f9340c1-e6dc-5557-a2f2-26c9669987d5)





- Kasutage turvalist autentimist:
 - Aktiveerige **tugev PIN-kood** või **biomeetriline autentimine** (sõrmejälg või näotuvastus), et kaitsta juurdepääsu rakendusele.
 - Ärge kunagi jagage oma PIN-koodi või biomeetrilisi andmeid.





- **Kaitske oma privaatsust**:
 - generate uus Address iga onchain- või Liquid-vastuvõtu jaoks, et piirata jälgimist Blockchain-l.
 - Kasutage PayJoin, kui see on saadaval, et suurendada konfidentsiaalsust seoses saadetava kogusega
 - Maksimaalse konfidentsiaalsuse tagamiseks ühendage oma Wallet oma Bitcoin sõlme Electrumi serveri kaudu, selle asemel et kasutada avalikku sõlme





- Valige oma vajadustele kõige paremini sobiv **võrk**:
- **Onchain**: Eelistatud pikaajalise hoidmise või suure väärtusega tehingute puhul (tasud on summa suhtes tähtsusetud).
- **Liquid**: Kasutage kiireks ja odavaks ülekandmiseks koos täiustatud konfidentsiaalsusega.
- **Välk**: Väikeste summade kiire ja soodne ülekanne. Kui teil on kaks Wallet Bull Bitcoin kasutajat, valige Liquid, et vältida Lightning <> Liquid vahetustasu Boltzi kaudu.





- **Kontrollige alati tarneaadresse**:
 - Enne raha saatmist kontrollige hoolikalt Address. Vale Address-le saadetud raha on igaveseks kadunud. Kasutage kopeerimist/liitmist või QR-koodi skaneerimist, ärge kunagi kopeerige/muutke Address käsitsi.





- **Optimeerida kulusid**:
 - Valige ahelas toimuvate tehingute puhul sobivad tasud (aeglane, keskmine, kiire) vastavalt kiireloomulisusele ja võrgu ülekoormusele.
 - Kasutage Liquid või Lightning väikestes kogustes.
 - Aktiveerige Replace-by-fee (RBF) (vt 4. liide) ahelasaadetiste jaoks, kui eeldate, et peate kinnitamist kiirendama.





- Hoidke taotlus ajakohasena




### A4. Täiendavad ressursid





- **Ametlikud lingid ja toetus:**
- [staff@bitcoinsupport.com](mailto:staff@bitcoinsupport.com), **support@bullbitcoin.com** : tugi e-kiri
- [Bull Bitcoin ametlik veebileht](https://bullbitcoin.com/): **Teave Bull Bitcoin teenuste kohta, konto loomine, juurdepääs rakendusele**
- [GitHub Bull Bitcoin Mobile](https://github.com/SatoshiPortal/bullbitcoin-mobile): **Vaata koodi, arengut ja teekaarti, aita kaasa arendusele...**
- [Konto X - Twitter Bull Bitcoin](https://x.com/BullBitcoin_)
- **Telegram** grupp Wallet mobiilile: grupivestlus koos toetusega, vt lehekülge "Seaded".





- Plokkide uurijad:
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Välk: **[1ML (Lightning Network)](https://1ml.com/)**





- **Õppe- ja juhendmaterjalid:** **[Plan ₿ Network](https://planb.network/)** :
 - Teie taastumislause kindlustamine



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Liquid Network** :
- [Sõnastik](https://planb.network/resources/glossary/liquid-network)




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727





- **Lightning Network**:
- [Sõnastik](https://planb.network/resources/glossary/lightning-network)




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


### A5. Bull Bitcoin



#### Ettevõtte ülevaade



**[Bull Bitcoin](https://www.bullbitcoin.com/fr)**, on vanim Exchange platvorm, mis on pühendatud ainult Bitcoin-le ja mis asutati 2013. aastal Bitcoin saatkonnas Montrealis, Kanadas. Ettevõtte eesotsas Francis Pouliot'ga, kes on tunnustatud pioneer Bitcoin ökosüsteemis, positsioneerib end finantssõltumatuse ja kasutajate autonoomia edendamise võtmeisikuna. Selle missioon on võimaldada üksikisikutel taastada kontroll oma raha üle, kasutades Bitcoin vabaduse ja maksevahendina, lükates samal ajal tagasi fiat-valuutad ja muud krüptovaluutad kui Bitcoin.



![image](assets/fr/26.webp)



[Looge oma konto](https://app.bullbitcoin.com/registration/orangepeel), kus Bitcoin ostude ja müügi puhul on 0,25% allahindlus.



#### Väärtused ja filosoofia



Bull Bitcoin paistab silma Commitment kuni Cypherpunk põhimõtete ja Bitcoin eetika poolest:





- **Eksklusiivne keskendumine Bitcoin-le**: Platvorm on truuks jäänud detsentraliseeritud, tsensuurikindla valuuta visioonile.





- **Mittekaitstav**: Kasutajad säilitavad täieliku kontrolli oma bitcoinide üle, saates raha oma portfelli.





- **Konfidentsiaalsus**: Minimeeritud isikuandmete kogumine, KYC-vabad ostuvõimalused alla 999 USD tehtavate tehingute puhul. Andmed on kaitstud vastavalt eeskirjadele (FINTRAC Kanadas, AMF Prantsusmaal).





- **Läbipaistvus**: Kulud sisalduvad hinnavahedes (ostu- ja müügihinna vahe).





- **Finantssuveräänsus**: Bull Bitcoin edendab sõltumatust traditsioonilistest pangandussüsteemidest ja tsentraliseeritud institutsioonidest.



#### Peamised teenused





- **Fiat hoius**: Kasutajad saavad oma Bull Bitcoin kontole kanda fiat-valuutat (CAD, EUR jne.) pangaülekande või sularaha/ deebetkaardi abil valitud Kanada postkontorites.





- **Bitcoin** ostmine : Kasutajad saavad osta Bitcoin, mis saadetakse otse nende mittehoiustamise portfelli, tagades täieliku kontrolli oma vahendite üle.





- **Planeeritud Bitcoin ostmine**: Bull Bitcoin pakub regulaarsete ajavahemike tagant automatiseeritud korduvat ostuteenust (DCA - Dollar Cost Averaging), mis kasutab teie vaba saldot ja kannab bitcoinid otse kasutaja poolt kontrollitavasse Wallet-sse, vähendades hinnakõikumiste mõju.



Pange tähele, et võimalus nimega "AutoBuy" võimaldab teil konverteerida oma fiatid kohe, kui need puudutavad teie Bull Bitcoin saldot, ja saata oma bitcoinid oma Wallet-sse. Seda võimalust saab kombineerida ka teie pangaga kavandatud korduva pangaülekandega, et teha DCA. See võimalus automatiseerib teie Bitcoin akumulatsiooni, ilma et peaksite rakendust avama.






- Ostke Bitcoin fikseeritud hinnaga **"Limit Order"**: Võimaldab osta Bitcoin kasutaja poolt eelnevalt määratud hinnaga, mis täidetakse automaatselt, kui Bull Bitcoin indeksi hind jõuab seatud piirhinnani või langeb sellest allapoole.





- **Müüa Bitcoin**: Kasutajad saavad müüa oma Bitcoine ja saada raha fiat-valuutas otse oma pangakontole panga või SEPA ülekande kaudu.





- **Kolmandate isikute maksed**: Bull Bitcoin võimaldab kasutajatel saata oma bitcoinidest pangakontodele fiatraha, mis on vastuvõtjale täiesti läbipaistev.





- **Bull Bitcoin Prime**: Bull Bitcoin Prime on lisateenus suurtele ja suurtele klientidele, mis pakub individuaalseid lahendusi ja lisatuge. See hõlmab juurdepääsu vähendatud tasudele, spetsiaalset kliendihaldurit ja kohandatud ettevõtte teenuseid. See teenus on suunatud institutsioonidele, professionaalsetele kauplejatele ja äriklientidele, kes soovivad põhjalikku ekspertiisi ja eeliskohtlemist.





- **Mobiilne Wallet**: Bull Bitcoin pakub avatud lähtekoodiga, isekasutatavat mobiilset Wallet, mis on saadaval Androidil ja iOSil ja toetab onchain-, Liquid- ja Lightning Network-tehinguid.





- **Haridusalane toetus**: Tasuta juhendid ja personaalne juhendamine, mis aitavad kasutajatel luua, kindlustada ja hallata oma Bitcoin portfelli, tugevdades finantsautonoomiat.



#### Vastavus ja ohutus





- **Reguleeriv**: Bull Bitcoin vastab KYC/AML nõuetele.





- **Turvalisus**: Turvaliste portfellide kasutamine ja soovitused võrguühenduseta salvestamiseks. Isikuandmeid hoitakse Bulli Bitcoin infrastruktuuris, mis on 100% isehostitav ja ei sõltu kolmandatest isikutest.