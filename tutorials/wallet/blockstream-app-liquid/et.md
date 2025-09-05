---
name: Blockstream App - Liquid
description: Kuidas konfigureerida Blockstream App ja kasutada Liquid Network
---
![cover](assets/cover.webp)


## 1. Sissejuhatus


### 1.1 Õpetuse eesmärk





- Selles õpetuses selgitatakse, kuidas kasutada **Blockstream App** mobiilirakendust **Bitcoin Liquid** portfelli haldamiseks, st otse Bitcoin "Liquid" külgahelas salvestatud tehingute haldamiseks.
- See hõlmab paigaldamist, esialgset konfigureerimist, Software Wallet loomist ja operatsioone bitcoinide vastuvõtmiseks ja saatmiseks Liquid-l.
- Märkus: Teised lisades olevad õpetused hõlmavad Onchaini, Watch-Only ja töölauaversiooni.



### 1.2 Sihtrühm





- Algajad**: Kasutajad, kes soovivad hallata oma bitcoine intuitiivse mobiilirakenduse abil, integreerides Liquid Network.
- Vahepealsed kasutajad**: Inimesed, kes soovivad mõista onchaini funktsioone ja privaatsusvõimalusi, nagu Tor või SPV.



### 1.3 Liquid tutvustamine



**Liquid** on **[Blockstream](https://blockstream.com/Liquid/)** poolt välja töötatud Bitcoin **Sidechain**, mille eesmärk on pakkuda kiiremat, rohkem Confidential Transactions ja täiustatud funktsionaalsust, jäädes samas ühendatud peamise Blockchain Bitcoin-ga.



Sidechain on sõltumatu Blockchain, mis töötab paralleelselt Bitcoin-ga, kasutades mehhanismi, mida tuntakse kui **kaksikühendust**. See süsteem lukustab bitcoinid peamise Blockchain külge, et luua **Liquid-Bitcoinid (L-BTC)**, mis on märgid, mis ringlevad Liquid Network-s, säilitades samal ajal algsete bitcoinide väärtuse pariteedi. Raha saab igal ajal Blockchain Bitcoin-le tagasi anda.



![image](assets/fr/17.webp)






- (1) Peg-in**: Bitimündid (BTC) on lukustatud Liquid föderatsiooni poolt Blockchain peavõimele. Vastutasuks väljastatakse Blockchain Liquid Liquid-le samaväärne kogus Liquid-Bitcoine (L-BTC), mis tagab pariteedi kahe ahela vahel, ja saadetakse kasutajale.





- (2) Sõltumatud tehingud** : Tehingud võivad toimuda samaaegselt ja sõltumatult peamisel Blockchain (BTC) ja Sidechain Liquid (L-BTC), sõltuvalt kasutaja vajadustest.





- (3) Peg-out**: Kasutaja saadab Liquid-Bitcoins (L-BTC) tagasi Liquid föderatsioonile. Seejärel vabastab föderatsioon samaväärse koguse bitcoin'e (BTC) peamisel Blockchain-l ja kannab need kasutajale üle.



Liquid tugineb usaldusväärsete osalejate **liidule** (börsid, tunnustatud Bitcoin ettevõtted), kes haldavad plokkide valideerimist ja kahepoolset ankurdamist. Erinevalt Blockchain Bitcoin, mis on detsentraliseeritud ja tugineb kaevandajatele, on Liquid **föderatiivne** võrk, mis tähendab, et selle turvalisus ja juhtimine sõltuvad nendest osalejatest. Kuigi see tähendab kompromissi detsentraliseerimise osas, võimaldab see optimeeritud jõudlust ja täiustatud funktsionaalsust.



![image](assets/fr/18.webp)



##### Miks kasutada Liquid?





- Kiirus**: Liquid tehingud kinnitatakse umbes **1 minutiga**, võrreldes 10 minutiga või enamaga onchaini tehingute puhul, tänu plokkidele, mis luuakse iga minuti tagant valideerijate föderatsiooni poolt.
- Täiustatud konfidentsiaalsus**: Liquid kasutab **Confidential Transactions**, mis varjab ülekantud vara summa ja liigi, muutes tehingud privaatsemaks (kuigi aadressid jäävad nähtavaks).
- Madalad tasud** : Liquid tehingud on üldiselt odavamad, mistõttu on need ideaalsed sagedaste ülekannete või väikeste summade puhul.
- Mitu vara**: Lisaks L-BTC-dele toetab Liquid ka muude digitaalsete varade, näiteks stabiilseid münte või žetoneid, emiteerimist konkreetsetes rakendustes kasutamiseks.
- Kasutusjuhud**: Liquid sobib eriti hästi platvormideüleseks vahetuseks, kiireks maksmiseks või rakenduste jaoks, mis nõuavad arukaid lepinguid, jäädes samal ajal seotud Bitcoin turvalisusega.



** Märkus: See õpetus keskendub Liquid kasutamisele Blockstream Appi kaudu. Liquid Network põhjalikumaks tundmaõppimiseks leiate lisast ressursse.



### 1.4. Hot Wallet meeldetuletus





- Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: kõik nimetused nutitelefoni, arvutisse või mis tahes internetti ühendatud seadmesse paigaldatud rakendusele, mis võimaldab hallata ja kaitsta Bitcoin Wallet privaatvõtmeid.
- Erinevalt **hardvaralistest rahakottidest**, mida tuntakse ka **Cold rahakottidena**, mis isoleerivad võtmed võrguühenduseta, töötavad tarkvaralised rahakotid ühendatud keskkonnas, mis muudab need küberrünnakute suhtes haavatavamaks.





- Soovitatav kasutusviis** :
    - Sobib ideaalselt mõõduka koguse Bitcoin haldamiseks, eriti igapäevaste tehingute puhul.
    - Sobib algajatele või piiratud varadega kasutajatele, kellele Hardware Wallet võib tunduda üleliigne.





- Piirangud**: Vähem turvaline suurte rahaliste vahendite või pikaajaliste säästude säilitamiseks. Sellisel juhul valige Hardware Wallet.




## 2. Blockstream rakenduse tutvustamine





- Blockstream App** on mobiil- (iOS, Android) ja lauaarvutirakendus Bitcoin rahakottide ja varade haldamiseks Liquid Network-s. Omandas [Blockstream] (https://blockstream.com/) 2016. aastal, varem kandis nime *Green Address* ja seejärel *Blockstream Green*.
- Peamised omadused** :
    - Onchain** tehingud Blockchain Bitcoin.
    - Tehingud **Liquid** võrgus (Sidechain kiireks ja konfidentsiaalseks teabevahetuseks).
    - Ainult vaatlusportfellid** fondide jälgimiseks ilma juurdepääsuta võtmetele.
    - Privaatsusvõimalused: ühendus **Tori** kaudu, ühendus **isikliku sõlme** kaudu Electrumi kaudu või **SPV** verifitseerimine, et vähendada sõltuvust kolmandate osapoolte sõlmedest.
    - Funktsioonid **Replace-by-fee (RBF)** kinnitamata tehingute kiirendamiseks.
- Ühilduvus**: **Blockstream Jade**.
- Interface**: Intuitiivne algajatele, täiustatud võimalustega ekspertidele.
- Märkus**: Käesolev juhend keskendub ahelate kasutamisele. Teised lisades olevad õpetused käsitlevad Onchaini, Watch-Only ja töölauaversiooni.




## 3. Blockstream rakenduse paigaldamine ja seadistamine



### 3.1. allalaadimine





- Androidi jaoks** :
    - Lae [Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) Google Play Store'ist alla.
    - Alternatiiv: [Blockstream'i ametlikul GitHubil](https://github.com/Blockstream/green_android) saadaval oleva APK-faili kaudu.
- IOS-i jaoks** :
    - Lae [Blockstream App](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) App Store'ist alla.
- Märkus**: Kindlasti lae alla ametlikest allikatest, et vältida võltsitud rakendusi.



### 3.2. esialgne konfiguratsioon





- Avakuva**: Esmakordsel avamisel kuvab rakendus ekraani ilma konfigureeritud Wallet-ta. Loodud või imporditud portfellid ilmuvad siia hiljem.



![image](assets/fr/02.webp)





- Kohandage seadeid**: Klõpsake nupule "Rakenduse seaded", kohandage allpool olevaid valikuid, klõpsake nupule "Salvesta", taaskäivitage rakendus ja looge oma portfell.



![image](assets/fr/03.webp)



#### 3.2.1. Täiustatud privaatsus (ainult Android)





- Funktsioon**: Lülitab ekraanipildid välja, peidab rakenduste eelvaateid ülesannete halduris ja lukustab juurdepääsu, kui telefon on lukustatud.
- Miks?** : Kaitseb teie andmeid volitamata füüsilise juurdepääsu või ekraani hõivava pahavara eest.



#### 3.2.2. Ühendus Tori kaudu





- Funktsioon**: Marsruudi võrguliiklus **Tor** kaudu, mis on anonüümne võrk, mis krüpteerib teie ühendused.
- Miks?**: Ideaalne, kui te ei usalda oma võrku (näiteks avalik Wi-Fi).
- Puudus**: Võib aeglustada rakendust krüpteerimise tõttu.
- Soovitus**: Aktiveerige Tor, kui konfidentsiaalsus on prioriteet, kuid testige ühenduse kiirust.



#### 3.2.3. Isikliku sõlme ühendamine





- Funktsioon**: Ühendab rakenduse teie enda **täieliku Bitcoin sõlme** kaudu **Electrumi serveri**.
- Miks?**: Annab täieliku kontrolli Blockchain andmete üle, kõrvaldades sõltuvuse Blockstream serveritest.
- Eeltingimus**: Konfigureeritud Bitcoin-sõlm.
- Soovitus**: Edasijõudnud kasutajad, kes soovivad maksimaalset suveräänsust.



#### 3.2.4. SPV kontrollimine





- Funktsioon**: Kasutab **Ühendatud makse kontrollimine (SPV)**, et kontrollida otse teatud Blockchain andmeid ilma kogu ahelat alla laadimata.
- Miks?**: Vähendab sõltuvust Blockstream'i vaikimisi sõlmedest, jäädes samal ajal mobiilsete seadmete jaoks kergekaaluliseks.
- Puudus**: Vähem turvaline kui Full node, kuna see tugineb teatud teabe saamiseks kolmandatest osapooltest sõlmedele.
- Soovitus**: Aktiveerige SPV, kui te ei saa kasutada isiklikku sõlme, kuid eelistate optimaalse turvalisuse tagamiseks Full node.





## 4. Bitcoin onchain portfelli loomine



### 4.1. Alusta loomist





- Ettevaatust**: Seadke oma portfell üles privaatses keskkonnas, ilma kaamerate või vaatlejateta.
- Avakuval klõpsake nuppu "Get Started" :



![image](assets/fr/04.webp)





- Kui soovite hallata **Cold Wallet** (offline Wallet): klõpsake **"Connect Jade "**, et kasutada Hardware Wallet Blockstream Jade või muid ühilduvaid Cold rahakotte.



![image](assets/fr/05.webp)






- Ilmub järgmine ekraan:



![image](assets/fr/06.webp)






- (1) **"Setup Mobile Wallet"** : Looge uus Hot Wallet (Hot Wallet).
- (2) **"Taastamine varukoopiast "**: Olemasoleva portfelli importimine, kasutades Mnemonic fraasi (12 või 24 sõna). Hoiatus: Ärge importige fraasi Cold Wallet-st, sest see paljastub ühendatud seadmes, mis muudab selle turvalisuse kehtetuks.
- (3) **"Ainult valvega "**: Importige olemasolev ainult lugemiseks mõeldud portfell, et vaadata saldot (nt teie Cold Wallet) ilma Mnemonic fraasi avaldamata. Vt "Watch Only" õpetust lisas.



**Selles õpetuses**: Hot Wallet loomiseks klõpsake **"Setup Mobile Wallet"**.


Teie Wallet luuakse automaatselt ja kuvatakse Wallet avaleht, mille nimi on siin "Minu Wallet 5":



![image](assets/fr/07.webp)



**Tähtis**: Blockstream App on lihtsustanud Wallet loomist, mitte kuvades automaatselt 12-sõnalist seed fraasi. *Kuigi portfell luuakse nüüd ühe klõpsuga, on oht, et te kaotate juurdepääsu oma rahalistele vahenditele, kui te ei salvesta seed fraasi*.



### 4.2. Salvesta seed fraas





- Wallet avakuval klõpsake vahekaardil "Turvalisus" ja seejärel menüüs "Varundamine" või "Recovery Phrase":



![image](assets/fr/08.webp)



seed 12-sõnaline lause kuvatakse teile salvestamiseks.





- Kirjutage oma taastumisfraas ülima hoolikusega üles. Kirjutage see paberile või metallile ja hoidke seda kindlas kohas (turvalises, võrguühenduseta kohas). See fraas on teie ainus vahend, mille abil saate oma bitcoinidele ligi, kui seade kaob või rakendus kustutatakse.
- Samuti on oluline märkida, et igaüks, kes seda lauset kasutab, võib kõik teie bitcoinid varastada. Ärge kunagi salvestage seda digitaalselt:
 - Puudub ekraanipilt
 - Pilve, e-posti või sõnumite varukoopiaid ei ole
 - Ei ole kopeerimist/liitmist (oht, et salvestatakse lõikelauale)



**! See punkt on kriitiline**. Lisateavet varundamise kohta :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3. Kontrollida seed lauset



Enne vahendite saatmist selle seed fraasiga seotud Address-le peate testima oma 12 sõna varundust.


Selleks kirjutame viite üles, kustutame Wallet, taastame selle varukoopiaga ja kontrollime, et viide on muutumatu.





- Wallet avakuval klõpsake vahekaardil "Settings", seejärel "Wallet Details" ja kopeerige zPub ([extended public key](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f):



![image](assets/fr/09.webp)



Märkus: zpub Address saab importida oma Blockstream rakendusse "Watch Only" funktsiooni jaoks (vt lisa).





- Kustutage rakendus, seejärel taastage Wallet abil **"Restore from Backup "**, sisestades Mnemonic fraasi, ja kontrollige, et zpub on muutmata. Kui jah, siis on teie varukoopia õige ja te saate Wallet-le raha saata.





- Et rohkem teada saada, kuidas teha taastamistesti, on siin spetsiaalne õpetus :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.4. Rakendusele juurdepääsu tagamine



Lukustage juurdepääs rakendusele tugeva PIN-koodiga:




- Mine Wallet avakuval **"Turvalisus "**, seejärel klõpsa **"PIN "**
- Sisestage ja kinnitage **juhuslik 6-kohaline PIN-kood**.



**Biomeetriline valik**: Saadaval lisamugavuse tagamiseks, kuid vähem turvaline kui tugev PIN-kood (volitamata juurdepääsu oht, nt sõrmejälje või näo skaneerimine une ajal).



**Märkus**: PIN-kood kaitseb seadet, kuid raha tagasisaamiseks saab kasutada ainult seed fraasi.





## 5. Liquid Wallet kasutamine



### 5.1. Saada "L-BTC" bitcoinid



Liquid-Bitcoinide (L-BTC) saamiseks on saadaval mitu võimalust. Võite paluda kellelgi saata teile mõned otse, jagades Liquid vastuvõtva Address, mida on üksikasjalikult kirjeldatud allpool.



Alternatiivselt Exchange oma bitcoins onchain või kaudu Lightning Network L-BTC kasutades [sild nagu Boltz](https://boltz.Exchange/): sisestage oma Liquid saavad Address, teha makse, nagu soovite, ja saada oma L-BTC.





- Klõpsake portfelli avakuval "**Tehing**" ja seejärel **"Saamine "**.



![image](assets/fr/19.webp)





- Vaikimisi kuvab rakendus tühja **kviitungi Address, onchain** (SegWit v0 formaat, mis algab sõnaga `bc1q...`). Klõpsake "Bitcoin", et valida **Liquid Bitcoin** :



![image](assets/fr/20.webp)





- Valikud** :
 - (1) Klõpsake nooltele, et valida teine uus Address, mis on seotud selle seed lausega.
    - (2) Võite valida Address ka juba kasutatud/näidatud aadresside hulgast, klõpsates kolmel punktil üleval paremal ja seejärel "List of Addresses" (aadresside nimekiri)
    - (3) Konkreetse summa taotlemiseks klõpsake paremal üleval olevatel kolmel punktil, valige "Request amount" ja sisestage soovitud summa. QR uuendatakse ja Address asendatakse Bitcoin makse URIga.



![image](assets/fr/21.webp)





- Jagage Address/URI, klõpsates "**Jagamine**", kopeerides teksti või skaneerides QR-koodi.
- Kontrollimine**: Kontrollige Address, mida jagatakse vastuvõtjaga, nii palju kui võimalik, et vältida vigu või rünnakuid (nt pahavara, mis muudab lõikelaua).



### 5.2. bitcoinide saatmine





- Klõpsake portfelli avakuval "**Tehing**" ja seejärel **"Saada "** :



![image](assets/fr/22.webp)





- Sisestage andmed** :
    - (1) Sisestage saaja **Address**, kleepides selle peale või skaneerides QR-koodi.
    - (2) Kontrollige varasid ja kontot, millelt raha saadetakse.
    - (3) Märkige **summa**, mis tuleb saata. Saate valida ühiku: L-BTC, L-satoshis, USD, ...



![image](assets/fr/23.webp)





- Kontrolli** :
    - Kontrollige Address, summat ja tasusid kokkuvõtte ekraanil.
    - Address viga võib kaasa tuua vahendite pöördumatu kaotuse. Ettevaatust pahavara, mis muudab lõikelaua.



![image](assets/fr/24.webp)





- Kinnitus**: Tehingu allkirjastamiseks ja levitamiseks libistage nuppu "Saada".
- Järelmeetmed**: Wallet vahekaardil "Transact" kuvatakse tehing kui "Unconfirmed", seejärel "Confirmed", seejärel "Completed":



![image](assets/fr/25.webp)





- 2 ploki vaheline aeg on Liquid puhul 1 minut, nii et tehing kinnitatakse ja viiakse kiiresti lõpule.




## Lisad



### A1. Muud Blockstream Appi õpetused



Onchaini võrgu kasutamine



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

Wallet importimine ja jälgimine režiimis "Watch Only" (ainult vaatlus)



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Töölaua versioon



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da



### A2. Parimad tavad



**Blockstream App** turvaliseks ja tõhusaks kasutamiseks järgige järgmisi soovitusi. Need aitavad teil kaitsta oma raha, optimeerida tehinguid ja säilitada konfidentsiaalsust **Bitcoin (onchain)**, **Liquid** ja **Lightning** võrkudes.





- Kindlustage oma taastumisfraas** :
 - Tutorial: Mnemonic lause salvestamine



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Kasutage turvalist autentimist** :
 - Aktiveerige **tugev PIN-kood** või **biomeetriline autentimine** (sõrmejälg või näotuvastus), et kaitsta juurdepääsu rakendusele.
 - Ärge kunagi jagage oma PIN-koodi või biomeetrilisi andmeid.





- Kaitske oma privaatsust** :
 - generate uus Address iga vastuvõtuahela jaoks või Liquid, et piirata jälgimist Blockchain-l.
 - Aktiveerige funktsioonid "Täiustatud privaatsus", "Tor" ja "SPV".
 - Maksimaalse konfidentsiaalsuse tagamiseks ühendage oma Wallet oma Bitcoin-sõlme Electrumi serveri kaudu, selle asemel et kasutada avalikku sõlme





- Valige oma vajadustele kõige paremini sobiv võrk** :
 - Onchain**: Eelistatud pikaajalise hoidmise või suure väärtusega tehingute puhul (tasud on summa suhtes tähtsusetud).
 - Liquid**: Kasutage kiireks ja odavaks ülekandeks koos täiustatud konfidentsiaalsusega.
 - Välk**: Valige väikeste summade puhul kiire ja soodne ülekanne.





- Kontrollige alati tarneaadresse** :
 - Enne raha saatmist kontrollige Address hoolikalt. Vale Address-le saadetud raha on igaveseks kadunud. Kasutage kopeerimist/liitmist või QR-koodi skaneerimist, ärge kunagi kopeerige/muutke Address käsitsi.





- Optimeerida kulusid** :
 - Valige ahelas toimuvate tehingute puhul sobivad tasud (aeglane, keskmine, kiire) vastavalt kiireloomulisusele ja võrgu ülekoormusele.
 - Kasutage Liquid või Lightning väikestes kogustes.





- Hoidke taotlus ajakohasena




### A3. Täiendavad ressursid





- Ametlikud lingid:**
 - [Ametlik veebileht](https://blockstream.com/)**
 - [mobiilirakenduse tugi](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)** : dokumentatsioon ja vestlus
 - [GitHub](https://github.com/Blockstream/green_android)**





- Plokkide uurijad :**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Välk: **[1ML (Lightning Network)](https://1ml.com/)**





- Õppe- ja juhendmaterjalid:** **[Plan ₿ Network](https://planb.network/)** :
 - Teie taastumislause kindlustamine



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** :
 - [Sõnastik](https://planb.network/fr/resources/glossary/liquid-network)**




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- Lightning Network** :
 - [Sõnastik](https://planb.network/fr/resources/glossary/lightning-network)**



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
