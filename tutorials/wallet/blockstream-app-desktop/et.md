---
name: Blockstream App - Desktop
description: Kuidas kasutada Hardware Wallet koos Blockstream Appiga arvutis?
---
![cover](assets/cover.webp)



## 1. Sissejuhatus



### 1.1 Õpetuse eesmärk





- See õpetus selgitab, kuidas kasutada **Blockstream App** arvutis Bitcoin **onchain** Wallet-i haldamiseks koos **Hardware Wallet**-ga, võimaldades turvalisi tehinguid, mis on salvestatud põhilises Blockchain Bitcoin-s.
- See hõlmab paigaldamist, esialgset konfigureerimist, Hardware Wallet ühendamist ning onchain bitcoinide vastuvõtmist ja saatmist.
- Märkus: Muud lisades olevad õpetused käsitlevad Liquid, Watch-Only ja mobiilirakendust.



### 1.2 Sihtrühm





- **Algajad**: Kasutajad, kes soovivad hallata oma bitcoine turvalise töölauaprogrammi ja Hardware Wallet abil.
- **Vahepealsed kasutajad**: Inimesed, kes soovivad aru saada, kuidas kasutada Hardware Wallet onchain-tehingute ja privaatsusvõimaluste, nagu Tor või SPV, jaoks.



### 1.3. Riistvaraliste rahakottide tausta





- **Hardware Wallet**, **Cold Wallet**: Füüsiline seade, mis salvestab privaatseid võtmeid võrguühenduseta, pakkudes kõrgetasemelist kaitset küberrünnakute vastu, erinevalt **Hot rahakotidest** (ühendatud seadmetes olevad tarkvarakotid).
- **Soovitatav kasutusviis**:
    - Ideaalne suurte summade või pikaajaliste säästude kindlustamiseks.
    - Sobib turvalisusele keskendunud kasutajatele, kes soovivad kaitsta oma raha ühendatud seadmetega seotud riskide eest.
- **Piirangud**: Nõuab tarkvara, näiteks Blockstream App, et vaadata saldosid, generate-aadresse ja edastada Hardware Wallet allkirjastatud tehinguid.



## 2. Blockstream rakenduse tutvustamine





- **Blockstream App** on mobiil- (iOS, Android) ja lauaarvutirakendus Bitcoin rahakottide ja varade haldamiseks Liquid Network-l. Blockstream omandas selle 2016. aastal, selle nimi oli *GreenAddress*, nimetati ümber *Blockstream Green* (2019) ja nüüd on selle nimi *Blockstream app* (2025).
- **Peamised omadused**:
- **Onchain** tehingud Blockchain Bitcoin.
    - Tehingud **Liquid** võrgus (Sidechain kiireks ja konfidentsiaalseks teabevahetuseks).
- Ainult **vaatlusportfellid** fondide jälgimiseks ilma juurdepääsuta võtmetele.
    - Privaatsusvõimalused: ühendus **Tori** kaudu, ühendus **isikliku sõlme** kaudu Electrumi kaudu või **SPV** verifitseerimine, et vähendada sõltuvust kolmandate osapoolte sõlmedest.
    - Funktsioonid **Replace-by-fee (RBF)** kinnitamata tehingute kiirendamiseks.
- **Ühilduvus**: **Blockstream Jade**.
- **Interface**: Intuitiivne algajatele, täiustatud võimalustega ekspertidele.
- **Märkus**: Käesolev juhend keskendub Hardware Wallet lauaversiooniga seotud ahelatele. Muud lisadena esitatud juhendid hõlmavad kasutamist mobiilirakenduses, onchaini, Liquid ja Watch-Only funktsioonide puhul.



## 3. Blockstream App Desktop'i paigaldamine ja seadistamine



### 3.1. allalaadimine





- Mine [ametlikule veebisaidile](https://blockstream.com/app/) ja klõpsa "_Download Now_". Laadige alla oma operatsioonisüsteemile (Windows, macOS, Linux) vastav versioon.
- **Märkus**: Kindlasti lae alla ametlikust allikast, et vältida võltsitud tarkvara.



### 3.2. esialgne konfiguratsioon





- **Avakuva**: Esmakordsel avamisel kuvab rakendus ekraani ilma konfigureeritud Wallet-ta. Loodud või imporditud portfellid ilmuvad siia hiljem.



![image](assets/fr/02.webp)





- **Kohandage seadeid**: Klõpsake all vasakul asuval seadete ikoonil, reguleerige allpool olevaid valikuid ja jätkamiseks väljuda Interface-st.



![image](assets/fr/03.webp)



#### 3.2.1. Üldised parameetrid





- Klõpsake menüüs Seadistused nupule "**Üldine**".
- **Funktsioon**: Vajaduse korral muuta tarkvara keelt ja aktiveerida eksperimentaalseid funktsioone.



![image](assets/fr/04.webp)



#### 3.2.2. Ühendus Tori kaudu





- Klõpsake menüüs Settings (Seaded) nupule "**Network**".
- **Funktsioon**: Marsruudi võrguliiklus **Tor** kaudu, mis on anonüümne võrk, mis krüpteerib teie ühendused.
- **Miks?**: Ideaalne, kui te ei usalda oma võrku (näiteks avalik Wi-Fi).
- **Puudus**: Võib aeglustada rakendust krüpteerimise tõttu.
- **Soovitus**: Aktiveerige Tor, kui konfidentsiaalsus on prioriteet, kuid testige ühenduse kiirust.



![image](assets/fr/05.webp)



#### 3.2.3. Isikliku sõlme ühendamine





- Klõpsake menüüs Settings (Seaded) valikut "**Custom servers and validation**" (kohandatud serverid ja valideerimine).
- **Funktsioon**: Ühendab rakenduse teie enda **täieliku Bitcoin sõlme** kaudu **Electrumi serveri**.
- **Miks?**: Annab täieliku kontrolli Blockchain andmete üle, kõrvaldades sõltuvuse Blockstream serveritest.
- **Eeltingimus**: Konfigureeritud Bitcoin sõlme.
- **Soovitus**: Edasijõudnud kasutajad, kes soovivad maksimaalset suveräänsust.



![image](assets/fr/06.webp)



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

#### 3.2.4. SPV kontrollimine





- Klõpsake menüüs Settings (Seaded) valikut "**Custom servers and validation**" (kohandatud serverid ja valideerimine).
- **Funktsioon**: Kasutab **Ühendatud maksekontrolli (SPV)**, mis laeb alla plokkide päised ja kontrollib teie tehinguid kaasamise tõendi (Merkle) abil, salvestamata kogu Blockchain.
- **Miks?**: Vähendab sõltuvust Blockstream'i vaikimisi sõlmedest, jäädes samal ajal seadmete jaoks kergekaaluliseks.
- **Puudus**: Vähem turvaline kui Full node, kuna see tugineb mõne teabe saamiseks kolmandate osapoolte sõlmedele.
- **Soovitus**: Aktiveerige SPV, kui te ei saa kasutada isiklikku sõlme, kuid eelistate optimaalse turvalisuse tagamiseks Full node.



![image](assets/fr/07.webp)



## 4. Hardware Wallet ühendamine Blockstream rakendusega



### 4.1. Esialgsed kaalutlused



#### 4.1.1. Ledger kasutajatele





- Blockstream Green toetab Ledger seadmetes (Nano S, Nano X) ainult rakendust **Bitcoin Legacy**.
- Enne seadme ühendamist **Ledger Live'is** järgitavad sammud :


1. Mine **"Seaded "** → **"Eksperimentaalsed funktsioonid "** ja aktiveeri **arendajarežiim**.


2. Mine **"Minu Ledger"** → **"Rakenduste kataloog "**, seejärel paigalda rakendus **Bitcoin Legacy**


3. Enne Blockstream Green käivitamist avage Ledger-l rakendus **Bitcoin Legacy**, et luua ühendus.




- **Märkus**: Veenduge, et teie Ledger on PIN-koodiga lahti lukustatud ja et Bitcoin Legacy rakendus on ühendamisel aktiivne.



#### 4.1.2 Hardware Wallet initsialiseerimine





- Kui teie Hardware Wallet (Ledger, Trezor või Blockstream Jade) ei ole kunagi kasutatud (kas koos Blockstream Green või muu tarkvaraga, näiteks Ledger Live), peate selle esmalt initsialiseerima. See samm hõlmab, turvalises keskkonnas, ilma kaamerate või vaatlejateta:


1. **seed lause genereerimine / Mnemonic lause** (12, 18 või 24 sõna): Kirjutage see hoolikalt paberile.


2. **seed fraasi kontrollimine**: Testige Wallet importi märgitud sõnadest, nt laiendatud avaliku võtme kontrollimise teel. Viiakse läbi enne vahendite saatmist Wallet-le ja seed fraasi püsivat kindlustamist.


3. **Securing the seed fraas**: Hoidke fraas füüsilisel andmekandjal (paber või metall) ja turvalises kohas. Ärge säilitage seda kunagi digitaalselt (mitte ekraanipilte, pilve või e-posti teel).




- **Oluline**: seed fraas on teie ainus vahend raha tagasisaamiseks, kui seade on kadunud või talitlushäireid esineb. Igaüks, kellel on juurdepääs, võib teie bitcoinid varastada.
- **Ressursid** seed lause varundamiseks ja kontrollimiseks :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

#### 4.1.3. Konfiguratsioon selle õpetuse jaoks :





- Eeldame, et Hardware Wallet on juba initsialiseeritud seed fraasiga ja lukustava PIN-koodiga.
- Eeldame, et Hardware Wallet ei ole kunagi ühendatud Blockstream Appiga, mis nõuab uue konto loomist. Kui Hardware Wallet on juba Blockstream Appiga kasutatud, ilmub konto automaatselt rakenduse avamisel.



### 4.2. Ühenduse käivitamine





- Avakuval klõpsake "**Setup a New Wallet**", seejärel kinnitage tingimused ja klõpsake "**Get Started**" :



![image](assets/fr/08.webp)





- Valige valik "**On Hardware Wallet**":



![image](assets/fr/09.webp)





- Kui kasutate **Blockstream Jade**, klõpsake vastaval nupul. Vastasel juhul valige "**Connect a different Hardware Device**" :



![image](assets/fr/10.webp)





- Ühendage oma Hardware Wallet USB kaudu arvutiga ja valige see Blockstream App'is:



![image](assets/fr/22.webp)





- Palun oodake, kuni Blockstream App impordib teie portfelli andmed:



![image](assets/fr/23.webp)



### 4.3. Loo konto





- Kui teie Hardware Wallet on juba kasutanud Blockstream Appi, ilmub teie konto pärast importimist automaatselt Interface-sse. Vastasel juhul looge konto, klõpsates "**Loo konto**" :



![image](assets/fr/24.webp)





- Valige "**Standard**", et konfigureerida klassikaline Bitcoin portfell:



![image](assets/fr/25.webp)





- Kui teie konto on loodud, saate juurdepääsu oma peamisele Interface portfellile:



![image](assets/fr/26.webp)





## 5. Onchain Wallet kasutamine koos Hardware Wallet-ga



### 5.1. Võtke bitcoinid vastu





- Klõpsake portfelli põhiekraanil nupule "**Võta vastu**" :



![image](assets/fr/27.webp)





- Rakendus kuvab **tühja vastuvõtu Address**. Uue Address kasutamine iga vastuvõtu jaoks parandab teie konfidentsiaalsust. Address kopeerimiseks klõpsake "**Kopeeri Address**" või laske saatjal skaneerida kuvatavat QR-koodi:



![image](assets/fr/12.webp)



**Võimalused** :




- (1) Klõpsake nooltega generate uue Address seotud portfelliga.
- (2) Konkreetse summa taotlemiseks klõpsake nupule "**Lisaks valikuid**" ja seejärel nupule "**Summa taotlemine**". QR uuendatakse ja Address asendatakse Bitcoin makse URIga, näiteks: `Bitcoin:bc1q...?amount=0.00001`



![image](assets/fr/13.webp)





- (3) Eelmise Address taaskasutamiseks klõpsake "**More options**" ja seejärel "**List of addresses**" :



![image](assets/fr/14.webp)





- **Kontrollimine**: Kontrollige hoolikalt jagatud Address, et vältida vigu või rünnakuid (nt pahavara, mis muudab lõikelaua).
- Kui tehing on võrgus edastatud, ilmub see teie Wallet-sse. Oodake 1 kuni 6 kinnitust, et lugeda tehing muutumatuks.



![image](assets/fr/28.webp)



### 5.2. bitcoinide saatmine





- Klõpsake portfelli põhiekraanil nupule "**Saatmine**".



![image](assets/fr/29.webp)





- Sisestage andmed:
    - (1) Kontrollige, et valitud vara on **Bitcoin** (onchain).
    - (2) Sisestage saaja **Address**, kleepides selle sisse või skaneerides veebikaameraga QR-koodi.
    - (3) Märkige **summa**, mis tuleb saata (BTC-des, satoshides või muudes ühikutes).




![image](assets/fr/16.webp)





- Valige **tehingutasud** (vabatahtlik) :
 - Valige pakutud valikute (kiire, keskmine, aeglane) hulgast vastavalt kiireloomulisusele, koos hinnangulise kinnituse andmise ajaga.
 - Kohandatud tasude jaoks reguleerige käsitsi satoshide arvu vbyte'i kohta. Need kuvatakse avakuval. Vt ka [Mempool.space](https://Mempool.space/).



![image](assets/fr/17.webp)





- **UTXOde käsitsi valimine** (valikuline): Klõpsake "**Manuaalne Coin valik**", et valida konkreetsed UTXOd, mida tehingus kasutada.



![image](assets/fr/18.webp)





- **Esialgne kontroll**: Kontrollige Address, summat ja tasusid kokkuvõtte ekraanil, seejärel klõpsake "**Kinnitage tehing**". Tegelikkuses ei anta tehingut võrku enne, kui olete selle allkirjastanud oma Hardware Wallet-ga, millel üksi on salajased võtmed, mis on seotud aadressidega, millelt UTXOd (satoshid) debiteeritakse.



![image](assets/fr/19.webp)





- **Lõplik kontroll ja allkiri**: Veenduge, et kõik tehingu parameetrid on õiged **teie Hardware Wallet** ekraanil, seejärel allkirjastage tehing selle abil. Address viga võib põhjustada vahendite pöördumatut kadumist.





- **Saade**: Pärast allkirjastamist edastab Blockstream App tehingu automaatselt Bitcoin võrgus.



![image](assets/fr/20.webp)





- **Järelmeetmed**:
 - Tehing kuvatakse Wallet avakuval "ootel" kuni kinnitamiseni.
 - Kui tehingut ei ole veel kinnitatud, saab kinnituse kiirendamiseks kasutada funktsiooni **Replace-by-fee (RBF)**, suurendades tasu (vt lisa).



![image](assets/fr/21.webp)



## Lisad



### A1. Muud Blockstream õpetused





- Liquid Network kasutamine :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Importida ja jälgida portfelli "Watch-Only" :



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb



- Blockstream rakenduse kasutamine mobiiltelefonides (Hot Wallet) :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

### A2. Replace-by-fee (RBF) selgitus





- **Määratlus**: Replace-by-fee (RBF) on Bitcoin võrgu funktsioon, mis võimaldab saatjal kiirendada **ahela** tehingu kinnitamist, suurendades tasu.
- **Piirid**:
    - RBF ei ole saadaval Liquid või Lightning tehingute jaoks.
    - Esialgne tehing tuleb märkida RBF-ga ühilduvaks, mida Blockstream App teeb automaatselt.
- Lisateavet leiate [meie sõnastikust](https://planb.network/resources/glossary/RBF-replacebyfee).



### A3. Parimad tavad





- **Kindlustage oma taastumisfraas** :
    - Salvestage oma Hardware Wallet Mnemonic lause füüsilisel andmekandjal (paber, metall) turvalises kohas.
    - Ärge kunagi salvestage seda digitaalselt (pilv, e-post, ekraanipilt).
    - Tutorial : Mnemonic lause salvestamine :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Kaitske oma privaatsust**:





    - generate uus Address iga vastuvõtu jaoks.
    - Jälgimise piiramiseks aktiveerige **Tor** või **SPV**.
    - Ühendage oma Bitcoin sõlme Electrumi kaudu, et saavutada maksimaalne suveräänsus.
- **Kontrollige alati tarneaadresse**:





    - Enne allkirjastamist kontrollige Address ekraanil Hardware Wallet.
    - Kasutage käsitsi tehtud vigade vältimiseks kopeerimist ja kleepimist või QR-koodi.
- **Optimeerida kulusid**:





    - Kohandada tasusid vastavalt kiireloomulisusele ja võrgu ülekoormusele (vt [Mempool.space](https://Mempool.space/)).
    - Kasutage Liquid või Lightning kiireks ja odavaks tehinguks, mis ei nõua ahelasisest turvalisust.
- **Tarkvara uuendamine**:





    - Hoidke oma Blockstream App ja Hardware Wallet püsivara viimaste funktsioonide ja turvaparandustega ajakohasena.



### A4. Täiendavad ressursid





- **Ametlikud lingid**:
    - [Ametlik veebileht](https://blockstream.com/)
    - [Blockstream Appi tugi](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): dokumentatsioon ja vestlus
    - [GitHub](https://github.com/Blockstream/green_qt)





- **Plokkide uurijad**:
    - Onchain : [Mempool.space](https://Mempool.space/)
    - Liquid : [Blockstream Info](https://blockstream.info/Liquid)
    - Välk : [1ML (Lightning Network)](https://1ml.com/)





- **Teie taastumislause kindlustamine:**



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Liquid Network** :



[Sõnastik](https://planb.network/fr/resources/glossary/Liquid-network)



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727



- **Lightning Network**:



[Sõnastik](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb