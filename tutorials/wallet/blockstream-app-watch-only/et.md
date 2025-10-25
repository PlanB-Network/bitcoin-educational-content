---
name: Blockstream App - Watch-Only
description: Kuidas konfigureerida Watch-only wallet Blockstream Appis?
---

![cover](assets/cover.webp)


## 1. Sissejuhatus


### 1.1 Õpetuse eesmärk





- See õpetus selgitab, kuidas seadistada ja kasutada **Blockstream App** mobiilirakenduse **Watch-Only** funktsiooni, et jälgida Bitcoin Wallet ilma juurdepääsuta selle privaatvõtmetele.
- See hõlmab paigaldamist, esialgset konfigureerimist, laiendatud avaliku võtme importimist ning selle kasutamist saldode ja generate vastuvõtuaadresside jälgimiseks.
- Märkus: Teised õpetused, mis on esitatud lisas, käsitlevad Onchaini, Liquid ja töölauaversiooni.



### 1.2. Sihtrühm





- **Algajad**: Kasutajad, kes soovivad jälgida Bitcoin portfelli (sageli seotud Hardware Wallet-ga) intuitiivse mobiilirakenduse kaudu.
- **Vahepealsed kasutajad**: Inimesed, kes soovivad hallata ainult lugemiseks mõeldud portfelle, kasutades samal ajal privaatsusvõimalusi, nagu Tor või SPV.
- **Hardware Wallet omanikud**: generate omanikud: oma saldode ja generate aadresside kontrollimiseks ilma seadet ühendamata.
- **Ettevõtted ja kauplused**:
 - Jälgige oma tehinguid raamatupidamise eesmärgil ilma oma isiklikke võtmeid paljastamata.
 - Kontrollida online-maksesüsteemides saadud tehinguid ilma nende isiklikke võtmeid sisestamata.
 - Võimaldage töötajatele generate uute vastuvõtuaadresside kasutamine, ilma et neil oleks juurdepääs isiklikele võtmetele.
- **Organisatsioonid ja ühisrahastamine**: Näidata saldot läbipaistvalt annetajatele, võimaldamata juurdepääsu rahalistele vahenditele.



### 1.3. Tutvustame Watch-Only



**Watch-Only** Wallet võimaldab teil jälgida Bitcoin Wallet tehinguid ja saldot, ilma et teil oleks juurdepääs privaatvõtmetele. Erinevalt tavalisest Wallet-st salvestab see ainult avalikke andmeid, näiteks **laiendatud avalikku võtit** (millest tekkis **xpub**, seejärel "zpub", "ypub" jne), mis võimaldab saada vastuvõtuaadresse ja jälgida tehinguajalugu Blockchain Bitcoin-l. See võimaldab saada vastuvõtuaadresse ja jälgida tehinguajalugu Blockchain Bitcoin-l. Privaatvõtmete puudumine muudab võimatuks raha väljamaksmise rakendusest, mis tagab suurema turvalisuse.



![image](assets/fr/10.webp)



**Miks kasutada Watch-only wallet?**





- **Turvalisus**: Ideaalselt sobib **Hardware Walletga** turvatud portfelli jälgimiseks, ilma et ühendatud seadme isiklikud võtmed paljastuksid.
- **Mugavus**: Võimaldab kontrollida saldot ja generate uusi vastuvõtja-aadresse ilma Hardware Wallet ühendamata.
- **Konfidentsiaalsus**: Ühildub selliste valikutega nagu **Tor** või **SPV**, et piirata sõltuvust kolmandate osapoolte serveritest.
- **Kasutusjuhud**: Raha liikumise jälgimine, aadresside genereerimine maksete vastuvõtmiseks või tehingute kontrollimine ilma isiklikke võtmeid riskimata.



![image](assets/fr/01.webp)



### 1.4. Laiendatud avalikud võtmed



**laiendatud avalik võti** (xpub, ypub, zpub jne.) on Bitcoin Wallet-st tuletatud andmestik, mis genereerib kõik avalikud lapsvõtmed ja nendega seotud vastuvõtuaadressid, andmata juurdepääsu privaatvõtmetele.





- Kuidas see toimib: Laiendatud avalik võti genereeritakse seed fraasist deterministliku protsessi abil (BIP-32). See loob hierarhilise puu avalikest lastvõtmetest, millest igaühe saab teisendada Address vastuvõtuks. Kasutades sama tuletamise teed (nt `m/44'/0'/0'/0'`) kui jälgitud Wallet, genereerib Watch-only wallet samad aadressid, mis võimaldab jälgida vahendeid ja luua uusi vastuvõtuaadresse.



![image](assets/fr/11.webp)





- Laiendatud avaliku võtme tüübid
- **xpub**: Kasutatakse Legacy portfellide (aadressid algavad "1", BIP-44) ja Taproot portfellide (aadressid algavad "bc1p", BIP-86) puhul.
- **ypub**: Mõeldud ühilduvatele SegWit rahakottidele (aadressid, mis algavad "3", BIP-49).
- **zpub**: Seotud SegWit portfellidega (aadressid, mis algavad sõnaga "bc1q", BIP-84).
- **Muud (tpub, upub, vpub jne)**: Kasutatakse alternatiivsete võrkude (nt Testnet) või konkreetsete standardite puhul. Näiteks tpub on Testnet võrgu jaoks.





- **Eristus**: Valik xpub, ypub või zpub vahel sõltub Address tüübist (pärand, SegWit, Taproot või nested SegWit) ja Wallet poolt kasutatavast BIP-standardist. Kontrollige, millist formaati nõuab teie allikaportfell, et tagada ühilduvus Blockstream Appiga.





- **Turvalisus ja konfidentsiaalsus**: Laiendatud avalik võti ei ole turvalisuse seisukohalt tundlik, kuna see ei võimalda raha kulutada (puudub juurdepääs isiklikele võtmetele). Konfidentsiaalsuse seisukohast on see aga tundlik, sest see paljastab kõik avalikud aadressid ja nendega seotud tehinguloo.



**Soovitus**: Kaitske oma laiendatud avalikku võtit kui tundlikku teavet.



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 1.5. Hot Wallet meeldetuletus





- **Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: kõik nimetused nutitelefoni, arvutisse või mis tahes internetti ühendatud seadmesse paigaldatud rakendusele, mis võimaldab hallata ja kaitsta Bitcoin Wallet privaatvõtmeid.
- Erinevalt **hardvaralistest rahakottidest**, mida tuntakse ka **Cold rahakottidena**, mis isoleerivad võtmed võrguühenduseta, töötavad tarkvaralised rahakotid ühendatud keskkonnas, mis muudab need küberrünnakute suhtes haavatavamaks.





- **Soovitatav kasutusviis**:
    - Sobib ideaalselt mõõduka koguse Bitcoin haldamiseks, eriti igapäevaste tehingute puhul.
    - Sobib algajatele või piiratud varadega kasutajatele, kellele Hardware Wallet võib tunduda üleliigne.





- **Piirangud**: Vähem turvaline suurte rahaliste vahendite või pikaajaliste säästude säilitamiseks. Sellisel juhul valige Hardware Wallet.




## 2. Blockstream rakenduse tutvustamine





- **Blockstream App** on mobiilirakendus (iOS, Android) ja töölauarakendus Bitcoin portfellide ja varade haldamiseks Liquid Network-l. Omandati [Blockstream](https://blockstream.com/) poolt 2016. aastal ja kandis varem nime *Green Address* ja seejärel *Blockstream Green*.
- **Peamised omadused**:
- **Onchain** tehingud Blockchain Bitcoin.
    - Tehingud **Liquid** võrgus (Sidechain kiireks, konfidentsiaalseks teabevahetuseks).
- Ainult **vaatlusportfellid** fondide jälgimiseks ilma juurdepääsuta võtmetele.
    - Privaatsusvõimalused: ühendus **Tori** kaudu, ühendus **isikliku sõlme** kaudu Electrumi kaudu või **SPV** verifitseerimine, et vähendada sõltuvust kolmandate osapoolte sõlmedest.
    - Funktsioonid **Replace-by-fee (RBF)** kinnitamata tehingute kiirendamiseks.
- **Ühilduvus**: **Blockstream Jade**.
- **Interface**: Intuitiivne algajatele, edasijõudnute valikuvõimalused ekspertidele.
- **Märkus**: Käesolev juhend keskendub ahelate kasutamisele. Teised lisades olevad õpetused käsitlevad Onchaini, Watch-Only ja töölauaversiooni.




## 3. Blockstream rakenduse paigaldamine ja seadistamine



### 3.1. allalaadimine





- **Androidi jaoks**:
    - Lae [Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) Google Play Store'ist alla.
    - Alternatiiv: [Blockstream'i ametlikul GitHubil](https://github.com/Blockstream/green_android) saadaval oleva APK-faili kaudu.
- **IOS-i jaoks**:
    - Lae [Blockstream App](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) App Store'ist alla.
- **Märkus**: Kindlasti lae alla ametlikest allikatest, et vältida võltsitud rakendusi.



### 3.2. esialgne konfiguratsioon





- **Avakuva**: Esmakordsel avamisel kuvab rakendus ekraani ilma konfigureeritud Wallet-ta. Loodud või imporditud portfellid ilmuvad siia hiljem.



![image](assets/fr/02.webp)





- **Kohandage seadeid**: Klõpsake nupule "Rakenduse seaded", kohandage allpool olevaid valikuid, klõpsake nupule "Salvesta", taaskäivitage rakendus ja looge oma portfell.



![image](assets/fr/03.webp)



#### 3.2.1. Täiustatud privaatsus (ainult Android)





- **Funktsioon**: Lülitab ekraanipildid välja, peidab rakenduste eelvaateid ülesannete halduris ja lukustab juurdepääsu, kui telefon on lukustatud.
- **Miks?**: Kaitseb teie andmeid volitamata füüsilise juurdepääsu või ekraani hõivava pahavara eest.



#### 3.2.2. Ühendus Tori kaudu





- **Funktsioon**: Marsruudi võrguliiklus **Tor** kaudu, mis on anonüümne võrk, mis krüpteerib teie ühendused.
- **Miks?**: Ideaalne, kui te ei usalda oma võrku (näiteks avalik Wi-Fi).
- **Puudus**: Võib aeglustada rakendust krüpteerimise tõttu.
- **Soovitus**: Aktiveerige Tor, kui konfidentsiaalsus on prioriteet, kuid testige ühenduse kiirust.



#### 3.2.3. Isikliku sõlme ühendamine





- **Funktsioon**: Ühendab rakenduse oma **täieliku Bitcoin sõlme** kaudu **Electrumi serveri** kaudu.
- **Miks?**: Annab täieliku kontrolli Blockchain andmete üle, kõrvaldades sõltuvuse Blockstream serveritest.
- **Eeltingimus**: Konfigureeritud Bitcoin sõlme.
- **Soovitus**: Edasijõudnud kasutajad, kes soovivad maksimaalset suveräänsust.



#### 3.2.4. SPV kontrollimine





- **Funktsioon**: Kasutab **Ühendatud makse kontrollimine (SPV)**, et kontrollida otse teatavaid Blockchain andmeid ilma kogu ahelat alla laadimata.
- **Miks?**: Vähendab sõltuvust Blockstream'i vaikimisi sõlmedest, jäädes samal ajal mobiilsete seadmete jaoks kergekaaluliseks.
- **Puudus**: Vähem turvaline kui Full node, kuna see tugineb teatud teabe saamiseks kolmandatele sõlmpunktidele.
- **Soovitus**: Aktiveerige SPV, kui te ei saa kasutada isiklikku sõlme, kuid eelistate optimaalse turvalisuse tagamiseks Full node.





## 4. Bitcoin "Watch-only" portfelli loomine



### 4.1. Laiendatud avaliku võtme taastamine



Watch-only wallet seadistamiseks peate kõigepealt hankima jälgitava Wallet laiendatud avaliku võtme (xpub, ypub, zpub jne). See teave on tavaliselt kättesaadav teie tarkvara või Hardware Wallet seadete või "Wallet teave" jaotises.





- Näide Blockstream Appiga: Mine Wallet avakuval "Settings", seejärel "Wallet Details" ja kopeeri zpub :



![image](assets/fr/09.webp)





- Alternatiiv 1: generate QR-kood, mis sisaldab laiendatud avalikku võtit, mida skaneeritakse järgmises etapis.
- Alternatiiv 2: Kasutage output descriptor, kui teie Wallet pakub seda.



### 4.2. importida ainult Wallet Watch-only





- **Ettevaatust**: Seadke oma portfell üles privaatses keskkonnas, ilma kaamerate või vaatlejateta.
- Avakuval klõpsake "Uue portfelli loomine" ja seejärel "Alusta" :



![image](assets/fr/04.webp)





- Ilmub järgmine ekraan:



![image](assets/fr/06.webp)






- (1) **"Setup Mobile Wallet"** : Looge uus Hot Wallet. Vt lisa "Blockstream App - Onchain" juhendmaterjal "Blockstream App - Onchain".
- (2) **"Taastamine varukoopiast "**: Olemasoleva portfelli importimine, kasutades Mnemonic fraasi (12 või 24 sõna). Ettevaatust: Ärge importige fraasi Cold Wallet-st, sest see paljastub ühendatud seadmes, mis muudab selle turvalisuse kehtetuks.
- (3) **"Ainult vaatamine "**: valik, mis meid selles õpetuses huvitab.





- Seejärel valige "**Ühene allkiri**" ja võrk "**Bitcoin**":



![image](assets/fr/12.webp)





- Sisestage laiendatud avalik võti (xpub, ypub, zpub jne), skannige vastav QR-kood või sisestage output descriptor. Isegi kui rakendus määrab "xpub", on lubatud ka võtmed ypub, zpub jne. Seejärel klõpsake nuppu "Connect":



![image](assets/fr/13.webp)




### 4.3. Wallet Watch-only kasutamine



Pärast importimist kuvab Watch-only wallet laiendatud avalikust võtmest tuletatud aadresside kogusaldot ja tehinguajalugu. Nähtavad on ainult ahelasisesed tehingud (Liquid tehinguid ei võeta arvesse). Liquid Wallet jälgimiseks korrake importi, valides eelmises etapis "Liquid".





- **Saldo ja ajalugu**: avakuval saate vaadata kogu saldot ja tehingute ajalugu:



![image](assets/fr/14.webp)





- generate a vastuvõttev **Address**: Klõpsake "Transact", seejärel "Receive", et luua uus onchain Address. Jagage seda QR-koodi kaudu või kopeerige, et saada raha:



![image](assets/fr/15.webp)





- **Saada raha**: Klõpsake **"Tehing"**, seejärel **"Saada"**. Saate sisestada:
 - Vastuvõtja Address.
 - Tehingu summa.
 - Tehingutasud.



Kuna aga Watch-only wallet ei hoia privaatvõtmeid, ei saa te raha otse saata. Tehingu allkirjastamiseks ühendage oma Hardware Wallet või Exchange PSBT-d, skaneerides QR-koode (näiteks Coldcard Q-l saadaval olev võimalus).



![image](assets/fr/16.webp)





- **Märkus**: Vigade vältimiseks kontrollige alati vastuvõtvat Address ja tehingu üksikasju. Vale Address-le saadetud raha ei ole võimalik tagasi saada.




## Lisad



### A1. Muud Blockstream Appi õpetused





- Onchaini võrgu kasutamine :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143



- Liquid Network kasutamine :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Lauaversioon :



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Laiendatud avalikud võtmed





- Sõnastik :
 - [Laiendatud avalikud võtmed](https://planb.network/fr/resources/glossary/extended-key)
 - [xpub](https://planb.network/fr/resources/glossary/xpub)
 - [ypub](https://planb.network/fr/resources/glossary/ypub)
 - [zpub](https://planb.network/fr/resources/glossary/zpub)
- Kursus :
 - [Les clés publiques étendues](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f)




### A3. Parimad tavad



**Blockstream App** turvaliseks ja tõhusaks kasutamiseks järgige järgmisi soovitusi. Need aitavad teil kaitsta oma raha, optimeerida tehinguid ja säilitada konfidentsiaalsust **Bitcoin (onchain)**, **Liquid** ja **Lightning** võrkudes.





- **Kindlustage oma taastumisfraas** :
 - Tutorial: Mnemonic lause salvestamine



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Kasutage turvalist autentimist:
 - Aktiveerige **tugev PIN-kood** või **biomeetriline autentimine** (sõrmejälg või näotuvastus), et kaitsta juurdepääsu rakendusele.
 - Ärge kunagi jagage oma PIN-koodi või biomeetrilisi andmeid.





- **Kaitske oma privaatsust**:
 - generate uus Address iga onchain- või Liquid-vastuvõtu jaoks, et piirata jälgimist Blockchain-l.
 - Aktiveerige funktsioonid "Täiustatud privaatsus", "Tor" ja "SPV".
 - Maksimaalse konfidentsiaalsuse tagamiseks ühendage oma Wallet oma Bitcoin sõlme Electrumi serveri kaudu, selle asemel, et kasutada avalikku sõlme





- Valige oma vajadustele kõige paremini sobiv **võrk**:
- **Onchain**: Eelistatud pikaajalise hoidmise või suure väärtusega tehingute puhul (tasud on summa suhtes tähtsusetud).
- **Liquid**: Kasutage kiireks ja odavaks ülekandmiseks koos täiustatud konfidentsiaalsusega.
- **Välk**: Valige väikeste summade puhul kiire ja soodne ülekanne.





- **Kontrollige alati tarneaadresse**:
 - Enne raha saatmist kontrollige hoolikalt Address. Vale Address-le saadetud raha on igaveseks kadunud. Kasutage kopeerimist/liitmist või QR-koodi skaneerimist, ärge kunagi kopeerige/muutke Address käsitsi.





- **Optimeerida kulusid**:
 - Valige ahelas toimuvate tehingute puhul sobivad tasud (aeglane, keskmine, kiire) vastavalt kiireloomulisusele ja võrgu ülekoormusele.
 - Kasutage Liquid või Lightning väikestes kogustes.





- Hoidke taotlus ajakohasena




### A4. Täiendavad ressursid





- **Ametlikud Blockstream lingid:**
- [Ametlik veebileht](https://blockstream.com/)
- [mobiilirakenduse tugi](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): dokumentatsioon ja vestlus
- [GitHub](https://github.com/Blockstream/green_android)





- Plokkide uurijad:
 - Onchain: **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Välk: **[1ML (Lightning Network)](https://1ml.com/)**





- **Õppe- ja juhendmaterjalid:** **[Plan ₿ Network](https://planb.network/)** :
  - Teie taastumislause kindlustamine



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Liquid Network** :
- [Sõnastik](https://planb.network/fr/resources/glossary/liquid-network)




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- **Lightning Network**:
- [Sõnastik](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb