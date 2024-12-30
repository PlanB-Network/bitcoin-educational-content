---
name: Teoreetiline sissejuhatus Lightning Network'i
goal: Avasta Lightning Network tehnilisest perspektiivist
objectives:
  - Mõista võrgu kanalite toimimist.
  - Tutvuda terminitega HTLC, LNURL ja UTXO.
  - Omandada teadmised likviidsuse haldamisest ja LNN tasudest.
  - Tunnustada Lightning Network'i kui võrku.
  - Mõista Lightning Network'i teoreetilisi kasutusviise.
---

# Teekond Bitcoin'i teise kihti

Sukeldu Lightning Network'i südamesse, mis on oluline süsteem Bitcoin'i tehingute tuleviku jaoks. LNP201 on teoreetiline kursus Lightning'i tehnilisest toimimisest. See paljastab selle teise kihi võrgu alused ja mehhanismid, mis on loodud Bitcoin'i maksete kiireks, ökonoomseks ja skaleeritavaks muutmiseks.

Tänu oma maksekanalite võrgustikule võimaldab Lightning kiireid ja turvalisi tehinguid ilma iga vahetust Bitcoin'i plokiahelas salvestamata. Peatükkide jooksul saate teada, kuidas kanalite avamine, haldamine ja sulgemine toimib, kuidas makseid turvaliselt vahendajate sõlmede kaudu suunatakse, minimeerides usalduse vajadust, ja kuidas hallata likviidsust. Avastate, mis on kohustuslikud tehingud, HTLC-d, tühistamisvõtmed, karistusmehhanismid, sibulmarsruutimine ja arved.

Olenemata sellest, kas olete Bitcoin'i algaja või kogenum kasutaja, pakub see kursus väärtuslikku teavet Lightning Network'i mõistmiseks ja kasutamiseks. Kuigi me käsitleme esimestes osades mõningaid Bitcoin'i toimimise aluseid, on oluline valdada Satoshi leiutise põhitõdesid enne LNP201-sse sukeldumist.

Nautige avastamist!

+++

# Alused

<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>

## Lightning Network'i mõistmine

<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>

![Lightning Network'i mõistmine](https://youtu.be/PszWk046x-I)

Tere tulemast LNP201 kursusele, mille eesmärk on selgitada Lightning Network'i tehnilist toimimist.

Lightning Network on maksekanalite võrk, mis on ehitatud Bitcoin'i protokolli peale, eesmärgiga võimaldada kiireid ja madala tasuga tehinguid. See võimaldab luua maksekanaleid osalejate vahel, mille sees saab tehinguid teha peaaegu koheselt ja minimaalsete tasudega, ilma et iga tehingut oleks vaja eraldi plokiahelas salvestada. Seega püüab Lightning Network parandada Bitcoin'i skaleeritavust ja muuta selle kasutatavaks madala väärtusega maksete jaoks.

Enne "võrgu" aspekti uurimist on oluline mõista Lightning'il maksekanali kontseptsiooni, kuidas see toimib ja selle eripärasid. See on selle esimese peatüki teema.

### Maksekanali kontseptsioon

Maksekanal võimaldab kahel osapoolel, siin **Alice** ja **Bob**, vahetada vahendeid Lightning Network'i kaudu. Igal protagonistil on sõlm, mida sümboliseerib ring, ja nende vaheline kanal on esindatud joonlõiguga.

![LNP201](assets/en/01.webp)

Meie näites on Alicel oma kanali poolel 100 000 satoshi ja Bobil 30 000, kokku 130 000 satoshi, mis moodustab **kanali mahutavuse**.

**Aga mis on satoshi?**

**Satoshi** (või "sat") on Bitcoin'i arvestusühik. Euro sendi sarnaselt on satoshi lihtsalt Bitcoin'i murdosa. Üks satoshi võrdub **0.00000001 Bitcoiniga**, ehk ühe sajandikmiljondikuga Bitcoin'ist. Satoshi kasutamine muutub üha praktilisemaks, kui Bitcoin'i väärtus tõuseb.

### Vahendite jaotus kanalis

Tagasi maksekanali juurde. Peamine kontseptsioon siin on "**kanali pool**". Igal osalejal on oma kanali poolel teatud summa vahendeid: Alicel 100 000 satoshi ja Bobil 30 000. Nagu oleme näinud, esindab nende vahendite summa kanali koguvõimsust, mis määratakse kanali avamisel.

![LNP201](assets/en/02.webp)

Võtame näiteks Lightning tehingu. Kui Alice soovib saata 40 000 satoshit Bobile, on see võimalik, kuna tal on piisavalt vahendeid (100 000 satoshit). Pärast seda tehingut omab Alice oma poolel 60 000 satoshit ja Bob 70 000.

![LNP201](assets/en/03.webp)

**Kanali võimsus**, 130 000 satoshit, jääb muutumatuks. Muutub vahendite jaotus. See süsteem ei luba saata rohkem vahendeid, kui omatakse. Näiteks, kui Bob sooviks saata tagasi 80 000 satoshit Alicele, ei saaks ta seda teha, kuna tal on ainult 70 000.

Teine viis vahendite jaotuse ettekujutamiseks on mõelda **liugurile**, mis näitab, kus vahendid kanalis asuvad. Alguses, kui Alicel on 100 000 satoshit ja Bobil 30 000, on liugur loogiliselt Alice'i poolel. Pärast 40 000 satoshi tehingut liigub liugur veidi Bobi poole, kellel on nüüd 70 000 satoshit.

![LNP201](assets/en/04.webp)

See esitusviis võib olla kasulik kanalis olevate vahendite tasakaalu ettekujutamiseks.

### Maksekanali Põhireeglid

Esimene meeldejääv punkt on see, et **kanali võimsus** on fikseeritud. See on natuke nagu toru diameeter: see määrab maksimaalse summa vahendeid, mida saab korraga kanali kaudu saata.
Võtame näiteks: kui Alicel on oma poolel 130 000 satoshit, saab ta maksimaalselt saata Bobile ühe tehinguga 130 000 satoshit. Siiski, Bob saab seejärel saata neid vahendeid tagasi Alicele, kas osaliselt või täielikult.

Oluline on mõista, et kanali fikseeritud võimsus piirab ühe tehingu maksimaalset summat, kuid mitte võimalike tehingute koguarvu ega kanalis vahetatud vahendite üldmahtu.

**Mida peaksite sellest peatükist kaasa võtma?**

- Kanali võimsus on fikseeritud ja määrab maksimaalse summa, mis saab ühe tehinguga saata.
- Kanalis olevad vahendid jaotuvad kahe osaleja vahel ning igaüks saab teisele saata ainult need vahendid, mis neil oma poolel on.
- Lightning Network võimaldab seega vahendite kiiret ja tõhusat vahetamist, austades samal ajal kanalite võimsusest tulenevaid piiranguid.

See on selle esimese peatüki lõpp, kus oleme pannud aluse Lightning Networkile. Järgnevates peatükkides näeme, kuidas avada kanalit ja süveneme siin arutatud kontseptsioonidesse.

## Bitcoin, Aadressid, UTXO ja Tehingud

<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>

![bitcoin, aadressid, utxo ja tehingud](https://youtu.be/cadCJ2V7zTg)
See peatükk on veidi eriline, kuna see ei ole otseselt pühendatud Lightning'ule, vaid Bitcoinile. Tõepoolest, Lightning Network on kiht Bitcoin'i peal. Seetõttu on oluline mõista teatud Bitcoin'i põhimõisteid, et korralikult mõista Lightning'i toimimist järgnevates peatükkides. Selles peatükis vaatame üle Bitcoin'i vastuvõtu aadresside, UTXO-de ning Bitcoin'i tehingute toimimise alused.

### Bitcoin'i Aadressid, Privaatvõtmed ja Avalikud Võtmed

Bitcoin'i aadress on tähemärkide jada, mis on tuletatud **avalikust võtmest**, mis omakorda on arvutatud **privaatvõtmest**. Nagu te kindlasti teate, kasutatakse seda bitcoinide lukustamiseks, mis on võrdne nende vastuvõtmisega meie rahakotti.

Privaatvõti on salajane element, mida **ei tohiks kunagi jagada**, samas kui avalik võti ja aadressi võib jagada ilma turvariskita (nende avalikustamine kujutab endast ainult teie privaatsuse riski). Siin on üldine esitus, mida me kogu selle koolituse vältel kasutame:

- **Privaatvõtmed** kujutatakse **vertikaalselt**.
- **Avalikud võtmed** kujutatakse **horisontaalselt**.
- Nende värv näitab, kes neid omab (Alice oranžis ja Bob mustas...).

### Bitcoin'i Tehingud: Fondide Saatmine ja Skriptid

Bitcoin'il hõlmab tehing fondide saatmist ühelt aadressilt teisele. Võtame näiteks Alice'i, kes saadab 0.002 Bitcoin'i Bobile. Alice kasutab oma aadressiga seotud privaatvõtit tehingu **allkirjastamiseks**, tõestades sellega, et ta on tõepoolest võimeline neid vahendeid kulutama. Kuid mis täpselt selle tehingu taga toimub? Bitcoin'i aadressil olevad fondid on lukustatud **skriptiga**, omamoodi mini-programmiga, mis seab fondide kulutamiseks teatud tingimused.

Kõige levinum skript nõuab aadressiga seotud privaatvõtmega allkirjastamist. Kui Alice allkirjastab tehingu oma privaatvõtmega, **avab ta skripti**, mis blokeerib vahendid, ja need saab seejärel üle kanda. Fondide ülekandmine hõlmab nende fondidele uue skripti lisamist, milles on sätestatud, et nende kulutamiseks on seekord vajalik **Bob'i** privaatvõtme allkiri.

![LNP201](assets/en/05.webp)

### UTXO-d: Kulutamata Tehinguväljundid

Bitcoin'il vahetame tegelikult mitte otseselt bitcoine, vaid **UTXO-sid** (_Unspent Transaction Outputs_), tähendab "kulutamata tehinguväljundeid".

UTXO on bitcoin'i tükk, mis võib olla mis tahes väärtuses, näiteks **2,000 bitcoin'i**, **8 bitcoin'i** või isegi **8,000 sats'i**. Iga UTXO on lukustatud skriptiga ja selle kulutamiseks tuleb rahuldada skripti tingimused, sageli allkiri antud vastuvõtu aadressiga seotud privaatvõtmega.

UTXO-sid ei saa jagada. Iga kord, kui neid kasutatakse bitcoini summa kulutamiseks, mida nad esindavad, tuleb seda teha tervikuna. See on natuke nagu pangatäht: kui sul on 10-eurone ja sa võlgned pagarile 5 eurot, ei saa sa lihtsalt pangatähte pooleks lõigata. Sa pead talle andma 10-eurose ja tema annab sulle 5 eurot tagasi. Bitcoin'i UTXO-de puhul on põhimõte täpselt sama! Näiteks, kui Alice avab oma privaatvõtmega skripti, avab ta terve UTXO. Kui ta soovib saata Bobile ainult osa selle UTXO poolt esindatud fondidest, saab ta selle "tükeldada" mitmeks väiksemaks. Ta saadab siis 0.0015 BTC Bobile ja ülejäänud, 0.0005 BTC, **muudatusaadressile**.

Siin on näide tehingust 2 väljundiga:

- UTXO 0.0015 BTC Bobi jaoks, lukustatud skriptiga, mis nõuab Bobi privaatvõtme allkirja.
- UTXO 0.0005 BTC Alice'i jaoks, lukustatud skriptiga, mis nõuab tema enda allkirja.

![LNP201](assets/en/06.webp)

### Mitme allkirjaga aadressid

Lisaks lihtsatele aadressidele, mis on genereeritud ühest avalikust võtmest, on võimalik luua **mitme allkirjaga aadresse** mitmest avalikust võtmest. Eriti huvitav Lightning Networki jaoks on **2/2 mitme allkirjaga aadress**, mis on genereeritud kahest avalikust võtmest:

![LNP201](assets/en/07.webp)

Selle 2/2 mitme allkirjaga aadressiga lukustatud vahendite kulutamiseks on vajalik allkirjastada kahe privaatvõtmega, mis on seotud avalike võtmetega.

![LNP201](assets/en/08.webp)

See aadressitüüp on täpselt Bitcoin'i plokiahela esitus Lightning Networki maksekanalitest.

**Mida peaksite sellest peatükist kaasa võtma?**

- **Bitcoin'i aadress** on tuletatud avalikust võtmest, mis omakorda on tuletatud privaatvõtmest.
- Bitcoinis olevad vahendid on lukustatud **skriptidega**, ja nende vahendite kulutamiseks tuleb skripti nõuded täita, mis üldjuhul hõlmab vastava privaatvõtme allkirja esitamist.
- **UTXO-d** on skriptidega lukustatud bitcoini tükid, ja iga Bitcoin'i tehing koosneb UTXO avamisest ja seejärel ühe või mitme uue loomisest vastutasuks.
- **2/2 mitme allkirjaga aadressid** nõuavad vahendite kulutamiseks kahe privaatvõtme allkirja. Neid konkreetseid aadresse kasutatakse Lightningis maksekanalite loomise kontekstis.

See peatükk Bitcoinist on võimaldanud meil üle vaadata mõned olulised mõisted järgnevaks. Järgmises peatükis avastame spetsiifiliselt, kuidas toimib kanalite avamine Lightning Networkis.

# Kanalite Avamine ja Sulgemine

<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>

## Kanali Avamine

<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>

![ava kanal](https://youtu.be/B2caBC0Rxko)

Sel peatükis vaatame täpsemalt, kuidas avada maksekanalit Lightning Networkis ja mõistame selle operatsiooni seost aluseks oleva Bitcoin süsteemiga.

### Lightning Kanalid

Nagu me esimeses peatükis nägime, võib **maksekanalit** Lightningis võrrelda "toruga" vahendite vahetamiseks kahe osaleja vahel (**Alice** ja **Bob** meie näidetes). Selle kanali maht vastab mõlema poole saadaolevate vahendite summale. Meie näites on Alicel **100 000 satoshi** ja Bobil **30 000 satoshi**, andes **kogumahuks 130 000 satoshi**.

![LNP201](assets/en/09.webp)

### Informatsiooni Vahetuse Tasemed

On oluline selgelt eristada erinevaid vahetuse tasemeid Lightning Networkis:

- **Eakaaslastevaheline suhtlus (Lightning protokoll)**: Need on sõnumid, mida Lightningi sõlmed omavahel suhtlemiseks saadavad. Me kujutame neid sõnumeid meie diagrammides katkendlike mustade joontega.
- **Maksekanalid (Lightning protokoll)**: Need on teed vahendite vahetamiseks Lightningis, mida me kujutame tahkete mustade joontega.
- **Bitcoin'i tehingud (Bitcoin protokoll)**: Need on onchain tehingud, mida me kujutame oranžide joontega.

![LNP201](assets/en/10.webp)
On oluline märkida, et Lightningi sõlm suudab suhelda P2P protokolli kaudu ilma kanalit avamata, kuid vahendite vahetamiseks on kanal vajalik.

### Sammud Lightningi kanali avamiseks

1. **Sõnumivahetus**: Alice soovib Bobiga kanali avada. Ta saadab talle sõnumi, mis sisaldab summat, mida ta soovib kanalisse deponeerida (130 000 satsi) ja oma avaliku võtme. Bob vastab, jagades oma avalikku võtit.

![LNP201](assets/en/11.webp)

2. **Mitme allkirjaga aadressi loomine**: Nende kahe avaliku võtmega loob Alice **2/2 mitme allkirjaga aadressi**, mis tähendab, et hiljem sellel aadressil deponeeritud vahendid nõuavad kulutamiseks mõlema (Alice'i ja Bobi) allkirja.

![LNP201](assets/en/12.webp)

3. **Deposiidi tehing**: Alice valmistab ette Bitcoin'i tehingu, et deponeerida vahendid sellele mitme allkirjaga aadressile. Näiteks võib ta otsustada saata **130 000 satoshi** sellele mitme allkirjaga aadressile. See tehing on **koostatud, kuid veel mitte avaldatud** plokiahelas.

![LNP201](assets/en/13.webp)

4. **Väljavõtte tehing**: Enne deposiidi tehingu avaldamist koostab Alice väljavõtte tehingu, et ta saaks oma vahendid tagasi saada, kui Bobiga tekib probleem. Tõepoolest, kui Alice avaldab deposiidi tehingu, lukustatakse tema satsid 2/2 mitme allkirjaga aadressile, mis nõuab avamiseks nii tema kui ka Bobi allkirja. Alice kaitseb end selle kaotuse riski eest, koostades väljavõtte tehingu, mis võimaldab tal oma vahendid tagasi saada.

![LNP201](assets/en/14.webp)

5. **Bob'i allkiri**: Alice saadab deposiidi tehingu Bobile tõendina ja palub tal allkirjastada väljavõtte tehingu. Kui Bobi allkiri on väljavõtte tehingul saadud, on Alice kindel, et ta saab oma vahendid igal ajal tagasi, kuna nüüd on vaja ainult tema enda allkirja, et mitme allkirjaga lukust avada.

![LNP201](assets/en/15.webp)

6. **Deposiidi tehingu avaldamine**: Kui Bobi allkiri on saadud, saab Alice deposiidi tehingu Bitcoin'i plokiahelas avaldada, avades sellega ametlikult Lightningi kanali kahe kasutaja vahel.

![LNP201](assets/en/16.webp)

### Millal peetakse kanalit avatuks?

Kanalit peetakse avatuks, kui deposiidi tehing on lisatud Bitcoin'i plokki ja see on saavutanud teatud sügavuse kinnitustes (järgnevate plokkide arv).

**Mida peaksite sellest peatükist meeles pidama?**

- Kanali avamine algab **sõnumite vahetusega** kahe poole vahel (summade ja avalike võtmete vahetus).
- Kanal luuakse, luues **2/2 mitme allkirjaga aadressi** ja deponeerides sinna vahendid Bitcoin'i tehingu kaudu.
- Kanali avav isik tagab, et ta saab **oma vahendid tagasi** läbi teise poole poolt allkirjastatud väljavõtte tehingu enne deposiidi tehingu avaldamist.

Järgmises peatükis uurime Lightningi tehingu tehnilist toimimist kanalis.

## Pühendumise Tehing

<chapterId>7d3fd135-129d-5c5a-b306-d5f2f1e63340</chapterId>

![Lightningi tehing & pühendumise tehing](https://youtu.be/aPqI34tpypM)

Sel peatükis avastame tehnilist toimimist tehingu puhul kanalis Lightningi võrgus, see tähendab, kui vahendid liiguvad ühelt kanali poolelt teisele.

### Meeldetuletus kanali elutsüklist

Nagu varem nähtud, algab Lightning kanal **avamisega** läbi Bitcoin'i tehingu. Kanalit saab **sulgeda** igal ajal, samuti läbi Bitcoin'i tehingu. Nende kahe hetke vahel saab kanalis toimuda peaaegu lõputu arv tehinguid, ilma et peaks minema läbi Bitcoin'i plokiahela. Vaatame, mis toimub kanalis tehingu ajal.

![LNP201](assets/en/17.webp)

### Kanali algseisund

Kanali avamise hetkel deposiit Alice **130 000 satoshi** kanali multisignatuuri aadressile. Seega, algseisundis on kõik vahendid Alice'i poolel. Enne kanali avamist lasi Alice Bobil allkirjastada ka **väljavõtte tehingu**, mis võimaldaks tal oma vahendid tagasi saada, kui ta sooviks kanali sulgeda.

![LNP201](assets/en/18.webp)

### Avaldamata Tehingud: Kohustuslikud Tehingud

Kui Alice teeb kanalis tehingu, et saata vahendeid Bobile, luuakse uus Bitcoin'i tehing, et kajastada seda muutust vahendite jaotuses. Seda tehingut, mida nimetatakse **kohustuslikuks tehinguks**, ei avaldata plokiahelas, kuid see esindab kanali uut seisundit pärast Lightning tehingut.

Võtame näiteks, kus Alice saadab 30 000 satoshi Bobile:

- **Alguses**: Alice'il on 130 000 satoshi.
- **Pärast tehingut**: Alice'il on 100 000 satoshi ja Bobil 30 000 satoshi.
  Selle ülekande valideerimiseks loovad Alice ja Bob uue **avaldamata Bitcoin'i tehingu**, mis saadaks **100 000 satoshi Alice'ile** ja **30 000 satoshi Bobile** multisignatuuri aadressilt. Mõlemad pooled konstrueerivad selle tehingu iseseisvalt, kuid sama andmetega (summad ja aadressid). Kui konstruktsioon on valmis, allkirjastab igaüks tehingu ja vahetab teisega oma allkirja. See võimaldab kummalgi poolel tehingu igal ajal avaldada, kui see on vajalik, et taastada oma osa kanalist peamisel Bitcoin'i plokiahelal.
  ![LNP201](assets/en/19.webp)

### Ülekandeprotsess: Arve

Kui Bob soovib vahendeid vastu võtta, saadab ta Alice'ile **_arve_** 30 000 satoshi eest. Alice seejärel jätkab selle arve tasumist, alustades ülekannet kanalis. Nagu oleme näinud, toetub see protsess uue **kohustusliku tehingu** loomisele ja allkirjastamisele.

Iga kohustuslik tehing esindab kanalis vahendite uut jaotust pärast ülekannet. Selles näites, pärast tehingut, on Bobil 30 000 satoshi ja Alice'il 100 000 satoshi. Kui üks kahest osalejast otsustaks selle kohustusliku tehingu plokiahelale avaldada, tulemuseks oleks kanali sulgemine ja vahendid jaotataks vastavalt sellele viimasele jaotusele.

![LNP201](assets/en/20.webp)

### Uus Seisund Pärast Teist Tehingut

Võtame teise näite: pärast esimest tehingut, kus Alice saatis 30 000 satoshi Bobile, otsustab Bob saata **10 000 satoshi tagasi Alice'ile**. See loob kanali uue seisundi. Uus **kohustuslik tehing** esindab seda uuendatud jaotust:

- **Alice**l on nüüd **110 000 satoshi**.
- **Bob**il on **20 000 satoshi**.

![LNP201](assets/en/21.webp)

Jällegi, seda tehingut ei avaldata plokiahelas, kuid seda saab igal ajal teha, juhul kui kanal suletakse.

Kokkuvõttes, kui vahendid liiguvad Lightning kanalis:

- Alice ja Bob loovad uue **kohustusliku tehingu**, mis kajastab vahendite uut jaotust. - See Bitcoin'i tehing on mõlema poole poolt **allkirjastatud**, kuid **ei avaldata** Bitcoin'i plokiahelas niikaua, kui kanal püsib avatuna.
- Kohustuslikud tehingud tagavad, et iga osaleja saab igal ajal oma vahendid Bitcoin'i plokiahelas taastada, avaldades viimase allkirjastatud tehingu.

Siiski on selles süsteemis potentsiaalne viga, mida käsitleme järgmises peatükis. Näeme, kuidas iga osaleja saab end kaitsta teise poole petmiskatse eest.

## Tühistamisvõti

<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>
![transactions part 2](https://youtu.be/RRvoVTLRJ84)
Sel peatükis süveneme sellele, kuidas tehingud Lightning Network'is toimivad, arutades mehhanisme, mis on paigas petmise vastu kaitsmiseks, tagades, et mõlemad pooled järgivad kanalis reegleid.

### Meeldetuletus: Kohustuslikud Tehingud

Nagu varem nägime, toetuvad Lightning'i tehingud avaldamata **kohustuslikele tehingutele**. Need tehingud kajastavad kanalis olevate vahendite praegust jaotust. Kui tehakse uus Lightning'i tehing, luuakse ja allkirjastatakse mõlema poole poolt uus kohustuslik tehing, et kajastada kanali uut seisundit.

Võtame lihtsa näite:

- **Algseisund**: Alicel on **100,000 satoshi**, Bobil **30,000 satoshi**.
- Pärast tehingut, kus Alice saadab **40,000 satoshi** Bobile, jaotatakse vahendid uue kohustusliku tehingu järgi järgmiselt:
  - Alice: **60,000 satoshi**
  - Bob: **70,000 satoshi**

![LNP201](assets/en/22.webp)

Igal ajal võivad mõlemad pooled avaldada **viimase allkirjastatud kohustusliku tehingu**, et sulgeda kanal ja taastada oma vahendid.

### Viga: Petmine, Avaldades Vana Tehingu

Potentsiaalne probleem tekib, kui üks osapooltest otsustab **petta**, avaldades vana kohustusliku tehingu. Näiteks võiks Alice avaldada vanema kohustusliku tehingu, kus tal oli **100,000 satoshi**, kuigi tegelikkuses on tal nüüd ainult **60,000**. See võimaldaks tal varastada **40,000 satoshi** Bobilt.

![LNP201](assets/en/23.webp)

Veelgi hullem, Alice võiks avaldada kõige esimese väljavõtmistehingu, selle enne kanali avamist, kus tal oli **130,000 satoshi**, ja seeläbi varastada kogu kanali vahendid.

![LNP201](assets/en/24.webp)

### Lahendus: Tühistamisvõti ja Ajalukk

Selle liiki petmise vältimiseks Alice'i poolt, lisatakse Lightning Network'is kohustuslikele tehingutele **turvamehhanismid**:

1. **Ajalukk**: Iga kohustuslik tehing sisaldab Alice'i vahenditele ajalukku. Ajalukk on nutilepingu primitiiv, mis seab aja tingimuse, mis peab olema täidetud, et tehingut saaks lisada plokki. See tähendab, et Alice ei saa oma vahendeid taastada enne, kui on möödunud teatud arv plokke, kui ta avaldab ühe kohustuslikest tehingutest. See ajalukk hakkab kehtima alates kohustusliku tehingu kinnitamisest. Selle kestus on üldiselt proportsionaalne kanali suurusega, kuid seda saab ka käsitsi seadistada.
2. **Tühistamisvõti**: Alice'i vahendeid saab samuti kohe kulutada Bob, kui tal on **tühistamisvõti**. See võti koosneb saladusest, mida hoiab Alice, ja saladusest, mida hoiab Bob. Pange tähele, et see saladus on iga kohustusliku tehingu jaoks erinev.
   Tänu nende kahe ühendatud mehhanismi kasutamisele on Bobil aega tuvastada Alice'i petmiskatse ja teda karistada, taastades oma väljundi revokatsioonivõtmega, mis Bobi jaoks tähendab kanali kõikide vahendite tagasisaamist. Meie uus kohustuslik tehing näeb nüüd välja selline:
   ![LNP201](assets/en/25.webp)

Vaadelgem selle mehhanismi toimimist üksikasjalikumalt.

### Tehingu Uuendamise Protsess

Kui Alice ja Bob uuendavad kanali olekut uue Lightning tehinguga, vahetavad nad ette oma vastavad **saladused** eelmise kohustusliku tehingu jaoks (see, mis muutub vananenuks ja võiks lubada ühel neist petta). See tähendab, et kanali uues olekus:

- Alice'il ja Bobil on uus kohustuslik tehing, mis kujutab pärast Lightning tehingut fondide praegust jaotust.
- Mõlemal on teise osapoole saladus eelmise tehingu jaoks, mis võimaldab neil kasutada revokatsioonivõtit ainult siis, kui üks neist üritab petta, avaldades tehingu vanas olekus Bitcoin'i sõlmede mempoolides. Tõepoolest, teise poole karistamiseks on vajalik mõlema saladuste ja teise osapoole kohustusliku tehingu omamine, mis sisaldab allkirjastatud sisendit. Ilma selle tehinguta on revokatsioonivõti üksi kasutu. Ainus viis selle tehingu saamiseks on selle taastamine mempoolidest (ootavates tehingutes) või kinnitatud tehingutest plokiahelas ajaluku ajal, mis tõestab, et teine pool üritab petta, olgu see tahtlikult või mitte.

Võtame näite, et mõista seda protsessi hästi:

1. **Algolek**: Alice'il on **100,000 satoshi**, Bobil **30,000 satoshi**.

![LNP201](assets/en/26.webp)

2. Bob soovib saada Alice'ilt läbi nende Lightning kanali 40,000 satoshi. Selleks:
   - Ta saadab talle arve koos oma saladusega revokatsioonivõtme jaoks oma eelmise kohustusliku tehingu jaoks.
   - Vastuseks annab Alice oma allkirja Bobi uue kohustusliku tehingu jaoks, samuti oma saladuse revokatsioonivõtme jaoks oma eelmise tehingu jaoks.
   - Lõpuks saadab Bob oma allkirja Alice'i uue kohustusliku tehingu jaoks.
   - Need vahetused võimaldavad Alicel saata **40,000 satoshi** Bobile Lightning'i kaudu läbi nende kanali, ja uued kohustuslikud tehingud peegeldavad nüüd seda uut fondide jaotust.

![LNP201](assets/en/27.webp)

3. Kui Alice üritab avaldada vana kohustusliku tehingu, kus tal oli endiselt **100,000 satoshi**, saab Bob, olles saanud revokatsioonivõtme, kohe kasutada seda võtit fondide taastamiseks, samal ajal kui Alice on ajaluku tõttu blokeeritud.

![LNP201](assets/en/28.webp)

Isegi kui sel juhul pole Bobil majanduslikku huvi petta proovida, kui ta seda siiski teeb, saab Alice samuti sümmeetrilisest kaitsest kasu, pakkudes talle samu tagatisi.

**Mida peaksite sellest peatükist kaasa võtma?**

Lightning Network'i **kohustuslikud tehingud** sisaldavad turvamehhanisme, mis vähendavad nii petmise riski kui ka selleks motiveerivaid stiimuleid. Enne uue kohustusliku tehingu allkirjastamist vahetavad Alice ja Bob oma vastavad **saladused** eelmiste kohustuslike tehingute jaoks. Kui Alice üritab avaldada vana kohustusliku tehingu, saab Bob kasutada **revokatsioonivõtit** kõikide fondide taastamiseks enne Alice'i (kuna ta on ajaluku tõttu blokeeritud), mis karistab teda petmiskatse eest.

See turvasüsteem tagab, et osalejad järgivad Lightning Network'i reegleid, ja nad ei saa kasu vanade kohustuslike tehingute avaldamisest.
Selles koolituse etapis te nüüd teate, kuidas Lightning kanalid avatakse ja kuidas tehingud nendes kanalites toimivad. Järgmises peatükis avastame erinevaid viise kanali sulgemiseks ja oma bitcoinide taastamiseks põhiketis.

## Kanali Sulgemine

<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>

![kanali sulgemine](https://youtu.be/FVmQvNpVW8Y)

Sel peatükis arutame **kanali sulgemist** Lightning võrgus, mida tehakse läbi Bitcoin tehingu, just nagu kanali avamine. Pärast seda, kui oleme näinud, kuidas tehingud kanalis toimivad, on nüüd aeg vaadata, kuidas sulgeda kanal ja taastada vahendid Bitcoin'i plokiahelas.

### Meeldetuletus kanali elutsüklist

**Kanali elutsükkel** algab selle **avamisega**, läbi Bitcoin tehingu, seejärel tehakse selles Lightning tehinguid, ja lõpuks, kui osapooled soovivad oma vahendeid taastada, **sulgetakse** kanal läbi teise Bitcoin tehingu. Vahepealsed tehingud Lightning'is esindavad avaldamata **kohustuste tehinguid**.

![LNP201](assets/en/29.webp)

### Kolm tüüpi kanali sulgemist

On kolm peamist viisi selle kanali sulgemiseks, mida võib nimetada **heaks, jõuliseks ja petturlikuks** (inspireeritud Andreas Antonopoulos'ist raamatus _Mastering the Lightning Network_):

1. **Hea**: **koostööaline sulgemine**, kus Alice ja Bob nõustuvad kanali sulgema.
2. **Halb**: **jõuline sulgemine**, kus üks osapooltest otsustab kanali ausalt sulgeda, kuid ilma teise nõusolekuta.
3. **Kole**: **petturlik sulgemine**, kus üks osapooltest üritab varastada vahendeid, avaldades vana kohustuste tehingu (ükskõik millise, välja arvatud viimase, mis kajastab tegelikku ja õiglast vahendite jaotust).

Võtame näite:

- Alicel on **100 000 satoshi** ja Bobil **30 000 satoshi**.
- See jaotus kajastub **2 kohustuste tehingus** (üks kasutaja kohta), mis ei ole avaldatud, kuid võiksid olla kanali sulgemise korral.

![LNP201](assets/en/30.webp)

### Hea: koostööaline sulgemine

**Koostööalises sulgemises** nõustuvad Alice ja Bob kanali sulgema. Siin on, kuidas see toimub:

1. Alice saadab Bobile sõnumi Lightning kommunikatsiooniprotokolli kaudu, ettepanekuga kanal sulgeda.
2. Bob nõustub ja mõlemad pooled ei tee kanalis rohkem tehinguid.

![LNP201](assets/en/31.webp)

3. Alice ja Bob läbirääkimisi peavad koos **sulgemistehingu** tasude üle. Need tasud arvutatakse üldiselt välja Bitcoin'i tasuturu alusel sulgemise ajal. On oluline märkida, et **alati on see isik, kes kanali avas** (meie näites Alice), kes maksab sulgemistasud.
4. Nad koostavad uue **sulgemistehingu**. See tehing sarnaneb kohustuste tehinguga, kuid ilma ajalukkude või tühistamismehhanismideta, kuna mõlemad pooled teevad koostööd ja petmise ohtu ei ole. Seega on see koostööaline sulgemistehing erinev kohustuste tehingutest.
   Näiteks, kui Alice omab **100,000 satoshit** ja Bob **30,000 satoshit**, siis lõpetav tehing saadab **100,000 satoshit** Alice'i aadressile ja **30,000 satoshit** Bob'i aadressile, ilma ajalukustuseta. Kui mõlemad pooled on tehingu allkirjastanud, avaldab Alice selle. Kui tehing on Bitcoin'i plokiahelas kinnitatud, on Lightning kanal ametlikult suletud.
   ![LNP201](assets/en/32.webp)

**Kooperatiivne sulgemine** on eelistatud sulgemismeetod, kuna see on kiire (ajalukustuseta) ja tehingutasud on kohandatud vastavalt praegustele Bitcoin'i turutingimustele. See väldib liiga väheste tasude maksmist, mis võiks tehingu mempuulis kinni jääda, või tarbetult liiga suurte tasude maksmist, mis toob osalejatele tarbetu rahalise kaotuse.

### Halb: sunnitud sulgemine

Kui Alice'i sõlm saadab Bob'ile sõnumi, paludes kooperatiivset sulgemist, kuid ta ei vasta (näiteks internetiühenduse katkemise või tehnilise probleemi tõttu), võib Alice jätkata **sunnitud sulgemisega**, avaldades **viimase allkirjastatud kohustuse tehingu**.
Sellisel juhul avaldab Alice lihtsalt viimase kohustuse tehingu, mis kajastab kanali seisundit viimase Lightning tehingu toimumise ajal õige fondide jaotusega.

![LNP201](assets/en/33.webp)

See tehing sisaldab **ajalukustust** Alice'i fondidele, muutes sulgemise aeglasemaks.

![LNP201](assets/en/34.webp)

Samuti võivad kohustuse tehingu tasud sulgemise hetkel olla sobimatud, kuna need määrati tehingu loomisel, mõnikord mitu kuud varem. Üldiselt ülehindavad Lightning kliendid tasusid, et vältida tulevikuprobleeme, kuid see võib viia liigsete tasudeni või vastupidi liiga madalateni.

Kokkuvõttes on **sunnitud sulgemine** viimane võimalus, kui teine pool enam ei vasta. See on aeglasem ja vähem majanduslik kui kooperatiivne sulgemine. Seetõttu tuleks seda võimalikult palju vältida.

### Pettus: petmine

Lõpuks toimub sulgemine **petmisega**, kui üks osapooltest üritab avaldada vana kohustuse tehingu, kus nad omavad rohkem vahendeid kui nad peaksid. Näiteks võib Alice avaldada vana tehingu, kus ta omas **120,000 satoshit**, samas kui tegelikult omab ta nüüd ainult **100,000**.

![LNP201](assets/en/35.webp)

Bob, et vältida petmist, jälgib Bitcoin'i plokiahelat ja selle mempuuli, et tagada, et Alice ei avaldaks vana tehingut. Kui Bob tuvastab petmise katse, saab ta kasutada **tühistamisvõtit**, et taastada Alice'i vahendid ja karistada teda, võttes kogu kanali fondid. Kuna Alice on oma väljundi ajalukustusega blokeeritud, on Bob'il aega seda kulutada ilma oma poolel ajalukustuseta, et taastada kogu summa aadressil, mida ta omab.

![LNP201](assets/en/36.webp)

Ilmselgelt võib petmine potentsiaalselt õnnestuda, kui Bob ei tegutse Alice'i väljundi ajalukustusele seatud ajapiirangus. Sellisel juhul avatakse Alice'i väljund, võimaldades tal seda tarbida, et luua uus väljund aadressile, mida ta kontrollib.

**Mida peaksite sellest peatükist kaasa võtma?**

On kolm viisi kanali sulgemiseks:

1. **Kooperatiivne Sulgemine**: Kiire ja vähem kulukas, kus mõlemad pooled nõustuvad kanali sulgema ja avaldavad kohandatud sulgemistehingu.
2. **Sunnitud Sulgemine**: Vähem soovitav, kuna see põhineb kohustuse tehingu avaldamisel, potentsiaalselt sobimatute tasudega ja ajalukustusega, mis aeglustab sulgemist.
3. **Petmine**: Kui üks osapooltest üritab varastada vahendeid, avaldades vana tehingu, saab teine kasutada tühistamisvõtit, et seda petmist karistada.
   Järgnevates peatükkides uurime Lightning Networki laiemast perspektiivist, keskendudes sellele, kuidas võrk toimib.

# Likviidsusvõrk

<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>

## Lightning Network

<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>

![lightning network](https://youtu.be/RAZAa3v41DM)

Sel peatükis uurime, kuidas makseid Lightning Networkis saab saajani jõuda isegi siis, kui nad ei ole otse ühendatud maksekanaliga. Lightning on tõepoolest **maksekanalite võrk**, mis võimaldab vahendeid saata kaugemale sõlmele läbi teiste osalejate kanalite. Avastame, kuidas makseid võrgus suunatakse, kuidas likviidsus kanalite vahel liigub ja kuidas tehingutasusid arvutatakse.

### Maksekanalite Võrk

Lightning Networkis vastab tehing vahendite ülekandele kahe sõlme vahel. Nagu eelmistes peatükkides nägime, on Lightning tehingute sooritamiseks vajalik avada kellegagi kanal. See kanal võimaldab peaaegu lõpmatut hulka off-chain tehinguid enne selle sulgemist, et taastada on-chain saldo. Siiski on sellel meetodil puudus, kuna vahendite vastuvõtmiseks või saatmiseks on vaja otsest kanalit teise isikuga, mis tähendab iga kanali jaoks avamis- ja sulgemistehingut. Kui plaanin selle inimesega teha suure hulga makseid, muutub kanali avamine ja sulgemine kuluefektiivseks. Vastupidiselt, kui mul on vaja sooritada vaid mõned Lightning tehingud, ei ole otsekanali avamine kasulik, kuna see maksaks mulle 2 on-chain tehingut piiratud hulga off-chain tehingute jaoks. Selline olukord võib tekkida näiteks siis, kui soovitakse maksta Lightningiga kaupmehe juures, ilma et plaanitaks sinna tagasi pöörduda.

Selle probleemi lahendamiseks võimaldab Lightning Network suunata makse läbi mitme kanali ja vahendajasõlmede, võimaldades nii tehingut ilma otsekanalita teise isikuga.

Näiteks kujutage ette, et:

- **Alice** (oranžis) omab kanalit **Suzie**ga (hallis), kus Alice'i poolel on **100,000 satoshi** ja Suzie poolel **30,000 satoshi**.
- **Suzie** omab kanalit **Bobiga**, kus Suzie poolel on **250,000 satoshi** ja Bobil pole satoshisid.

![LNP201](assets/en/37.webp)

Kui Alice soovib saata vahendeid Bobile ilma temaga otsekanalit avamata, peab ta minema läbi Suzie, ja iga kanal peab kohandama likviidsust mõlemal poolel. **Saadetud satoshid jäävad oma vastavatesse kanalitesse**; need ei "ületa" tegelikult kanaleid, vaid ülekanne toimub iga kanali sisese likviidsuse kohandamise kaudu.

Oletame, et Alice soovib saata **50,000 satoshi** Bobile:

1. **Alice** saadab 50,000 satoshi **Suzie**le nende ühises kanalis.
2. **Suzie** kordab seda ülekannet, saates 50,000 satoshi **Bobile** nende kanalis.

![LNP201](assets/en/38.webp)
Seega suunatakse makse Bobile läbi likviidsuse liikumise igas kanalis. Operatsiooni lõppedes on Alicel 50 000 satsi. Ta on tõepoolest üle kandnud 50 000 satsi, kuna algselt oli tal 100 000. Bobil omakorda on nüüd 50 000 satsi rohkem. Suzie jaoks (vahepealne sõlm) on see operatsioon neutraalne: algselt oli tal oma kanalis Alicega 30 000 satsi ja oma kanalis Bobiga 250 000 satsi, kokku 280 000 satsi. Pärast operatsiooni omab ta oma kanalis Alicega 80 000 satsi ja oma kanalis Bobiga 200 000 satsi, mis on sama summa kui alguses.
See ülekanne on seega piiratud **saadaoleva likviidsusega** ülekande suunas.

### Marsruudi ja Likviidsuse Piirangute Arvutamine

Võtame teoreetilise näite teisest võrgust, kus on:

- **130 000 satoshit** Alice'i poolel (oranzis) tema kanalis **Suziega** (hallis).
- **90 000 satoshit** **Suzie** poolel ja **200 000 satoshit** **Caroli** poolel (roosas).
- **150 000 satoshit** **Caroli** poolel ja **100 000 satoshit** **Bobi** poolel.

![LNP201](assets/en/39.webp)

Maksimaalne summa, mida Alice saab Bobile selles konfiguratsioonis saata, on **90 000 satoshit**, kuna teda piirab väikseim saadaolev likviidsus kanalis **Suzielt Carolile**. Vastupidises suunas (Bobilt Aliceni) ei ole makse võimalik, kuna **Suzie** poolel kanalis **Alice'iga** ei ole satoshi'e. Seega ei ole selles suunas kasutatavat **marsruuti**.
Alice saadab **40 000 satoshit** Bobile läbi kanalite:

1. Alice kannab 40 000 satoshit oma kanalisse Suziega.
2. Suzie kannab 40 000 satoshit Carolile nende ühises kanalis.
3. Carol lõpuks kannab 40 000 satoshit Bobile.

![LNP201](assets/en/40.webp)

**Saadetud satoshid** jäävad iga kanali sisse, nii et Caroli poolt Bobile saadetud satoshid ei ole samad, mis Alice saatis Suziele. Ülekanne toimub ainult likviidsuse reguleerimisega iga kanali sees. Lisaks jääb kanalite kogumahutavus muutumatuks.

![LNP201](assets/en/41.webp)

Nagu eelmises näites, pärast tehingut on allikasõlmel (Alice) 40 000 satoshit vähem. Vahepealsed sõlmed (Suzie ja Carol) säilitavad sama kogusumma, muutes operatsiooni nende jaoks neutraalseks. Lõpuks saab sihtsõlm (Bob) juurde 40 000 satoshit.

Vahepealsete sõlmede roll on seega Välguvõrgu (Lightning Network) toimimises väga oluline. Nad hõlbustavad ülekandeid, pakkudes maksete jaoks mitmeid radu. Nende sõlmede likviidsuse pakkumise ja maksete suunamises osalemise julgustamiseks makstakse neile **suunamistasusid**.

### Suunamistasud

Vahepealsed sõlmed rakendavad tasusid, et lubada makseid läbida nende kanalitest. Need tasud on määratud **iga sõlme poolt iga kanali kohta**. Tasud koosnevad kahest elemendist:

1. "**Baastasu**": fikseeritud summa kanali kohta, sageli vaikimisi **1 sat**, kuid kohandatav.
2. "**Muutuv tasu**": protsent ülekantavast summast, arvutatud **miljondike osades (ppm)**. Vaikimisi on see **1 ppm** (1 sat iga miljoni ülekantud satoshi kohta), kuid seda saab ka kohandada.
   Tasud erinevad ka ülekande suuna järgi. Näiteks Alice'ilt Suzie'le ülekande puhul kehtivad Alice'i tasud. Vastupidiselt, Suzie'lt Alice'ile ülekande puhul kasutatakse Suzie tasusid.

Näiteks Alice'i ja Suzie vahelise kanali puhul võime omada:

- **Alice**: baastasu 1 sat ja 1 ppm muutuva tasu jaoks.
- **Suzie**: baastasu 0.5 sat ja 10 ppm muutuva tasu jaoks.

![LNP201](assets/en/42.webp)

Et paremini mõista, kuidas tasud töötavad, uurigem sama Lightning Networki nagu varem, kuid nüüd järgmiste marsruutimistasudega:

- Kanal **Alice - Suzie**: baastasu 1 satoshi ja 1 ppm Alice'i jaoks.
- Kanal **Suzie - Carol**: baastasu 0 satoshi ja 200 ppm Suzie jaoks.
- **Carol - Bob** Kanal: baastasu 1 satoshi ja 1 ppm Suzie 2 jaoks.
  ![LNP201](assets/en/43.webp)

Sama makse puhul **40,000 satoshis** Bob'ile peab Alice saatma veidi rohkem, kuna iga vahendaja sõlm võtab oma tasud:

- **Carol** võtab kanalil Bob'iga maha 1.04 satoshit:
  $$ f*{\text{Carol-Bob}} = \text{baastasu} + \left(\frac{\text{ppm} \times \text{summa}}{10^6}\right) $$
  $$ f*{\text{Carol-Bob}} = 1 + \frac{1 \times 40000}{10^6} = 1 + 0.04 = 1.04 \text{ sats} $$

- **Suzie** võtab kanalil Carol'iga maha 8 satoshit tasudes:
  $$ f*{\text{Suzie-Carol}} = \text{baastasu} + \left(\frac{\text{ppm} \times \text{summa}}{10^6}\right) $$
  $$ f*{\text{Suzie-Carol}} = 0 + \frac{200 \times 40001.04}{10^6} = 0 + 8.0002 \approx 8 \text{ sats} $$

Seega on selle makse kogutasud sellel teel **9.04 satoshit**. Seega peab Alice saatma **40,009.04 satoshit**, et Bob saaks täpselt **40,000 satoshit**.

![LNP201](assets/en/44.webp)

Seega on likviidsus uuendatud:

![LNP201](assets/en/45.webp)

### Onion marsruutimine

Makse saatmiseks saatjalt saajale kasutab Lightning Network meetodit, mida nimetatakse "**onion marsruutimiseks**". Erinevalt klassikalise andmete marsruutimisest, kus iga ruuter otsustab andmete suuna nende sihtkoha põhjal, töötab onion marsruutimine erinevalt:

- **Saatja sõlm arvutab kogu marsruudi**: Alice näiteks määrab, et tema makse peab minema läbi Suzie ja Carol'i enne Bob'ini jõudmist.
- **Iga vahendaja sõlm teab ainult oma vahetut naabrit**: Suzie teab ainult, et ta sai raha Alicelt ja et ta peab selle edasi kandma Carolile. Siiski ei tea Suzie, kas Alice on algne sõlm või vahendaja sõlm, samuti ei tea ta, kas Carol on saaja sõlm või lihtsalt järjekordne vahendaja sõlm. See põhimõte kehtib ka Caroli ja kõigi teiste teel olevate sõlmede kohta. Seega säilitab sibulmarsruutimine (onion routing) tehingute konfidentsiaalsuse, maskeerides saatja ja lõpliku saaja identiteeti. Selleks, et edastav sõlm saaks sibulmarsruutimises arvutada täieliku marsruudi saajani, peab ta säilitama **võrgugraafiku**, et teada oma topoloogiat ja määrata võimalikud marsruudid.
  **Mida peaksite sellest peatükist kaasa võtma?**

1. Lightningil saab makseid suunata sõlmede vahel, mis on ühendatud kaudselt vahendajakanalite kaudu. Iga selline vahendajasõlm hõlbustab likviidsuse ülekannet.
2. Vahendajasõlmed saavad oma teenuse eest komisjonitasu, mis koosneb fikseeritud ja muutuvatest tasudest.
3. Sibulmarsruutimine võimaldab edastaval sõlmel arvutada täieliku marsruudi ilma, et vahendajasõlmed teaksid allika või lõppsihtkoha kohta.

Sel peatükis uurisime maksete suunamist Lightningi võrgus. Kuid tekib küsimus: mis takistab vahendajasõlmi vastu võtmast saabuvat makset ilma seda järgmisesse sihtkohta edastamata, eesmärgiga tehing katkestada? Just see on HTLC-de roll, mida me järgmises peatükis uurime.

## HTLC – Hashed Time Locked Contract

<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>

![HTLC](https://youtu.be/-JC4mkq7H48)

Sel peatükis avastame, kuidas Lightning võimaldab makseid suunata läbi vahendajasõlmede ilma, et peaks neid usaldama, tänu **HTLC**-le (_Hashed Time-Locked Contracts_). Need nutilepingud tagavad, et iga vahendajasõlm saab oma kanalist rahad kätte ainult siis, kui ta edastab makse lõppsaajale, vastasel juhul makset ei valideerita.

Maksete suunamisel tekib seega vajadus usaldada vahendajasõlmi ja ka vahendajasõlmede vahelist usaldust. Selle illustreerimiseks vaatame uuesti meie lihtsustatud Lightningi võrgu näidet 3 sõlme ja 2 kanaliga:

- Alicel on kanal Suziega.
- Suziel on kanal Bobiga.

Alice soovib saata 40 000 satsi Bobile, kuid tal pole temaga otsest kanalit ja ta ei soovi seda avada. Ta otsib marsruuti ja otsustab minna läbi Suzie sõlme.

![LNP201](assets/en/46.webp)

Kui Alice saadab naiivselt 40 000 satoshit Suziele, lootes, et Suzie kannab selle summa Bobile üle, võib Suzie raha endale jätta ja mitte midagi Bobile edastada.

![LNP201](assets/en/47.webp)
Selle olukorra vältimiseks kasutame Lightningis HTLC-sid (Hashed Time-Locked Contracts), mis muudavad makse vahendajasõlmele tingimuslikuks, tähendades, et Suzie peab täitma teatud tingimused, et pääseda ligi Alice'i rahadele ja need Bobile edasi kanda.

### Kuidas HTLC-d Töötavad

HTLC on eriline leping, mis põhineb kahe põhimõttel:

- **Juurdepääsutingimus**: Saaja peab avaldama saladuse, et avada neile ette nähtud makse.
- **Aegumine**: Kui makset ei viida lõpule määratletud perioodi jooksul, tühistatakse see ja vahendid tagastatakse saatjale.

Siin on, kuidas see protsess meie näites Alice'i, Suzie ja Bobiga töötab:

![LNP201](assets/en/48.webp)
**Saladuse loomine**: Bob genereerib juhusliku saladuse, mida tähistatakse _s_-na (eelkujutis), ja arvutab selle räsi, mida tähistatakse _r_-na, kasutades räsimisfunktsiooni, mida tähistatakse _h_-na. Meil on:

$$
r = h(s)
$$

Räsimisfunktsiooni kasutamine muudab võimatuks leida _s_ ainult _h(s)_ põhjal, kuid kui _s_ on antud, on lihtne kontrollida, et see vastab _h(s)_-le.

![LNP201](assets/en/49.webp)

**Maksepäringu saatmine**: Bob saadab Alicele **arve**, paludes makset. See arve sisaldab muuhulgas räsi _r_.

![LNP201](assets/en/50.webp)

**Tingimusliku makse saatmine**: Alice saadab Suziele HTLC 40 000 satoshi ulatuses. Tingimus, mille alusel Suzie need vahendid saab, on see, et ta peab Alicele andma saladuse _s'_, mis rahuldab järgmist võrrandit:

$$
h(s') = r
$$

![LNP201](assets/en/51.webp)

**HTLC ülekandmine lõppsaajale**: Suzie, et saada Alicelt 40 000 satoshit, peab edastama sarnase HTLC 40 000 satoshi ulatuses Bobile, kellel on sama tingimus, nimelt et ta peab andma Suziele saladuse _s'_, mis rahuldab võrrandit:

$$
h(s') = r
$$

![LNP201](assets/en/52.webp)

**Kinnitamine saladuse _s_ abil**: Bob annab _s_-i Suziele, et saada lubatud 40 000 satoshit HTLC-st. Selle saladusega saab Suzie seejärel avada Alice'i HTLC ja saada Alicelt 40 000 satoshit. Makse on seejärel õigesti suunatud Bobile.

![LNP201](assets/en/53.webp)
See protsess takistab Suziel hoidmast Alice'i vahendeid ilma ülekannet Bobile lõpule viimata, kuna ta peab saatma makse Bobile, et saada saladus _s_ ja seeläbi avada Alice'i HTLC. Operatsioon jääb samaks isegi siis, kui marsruut hõlmab mitut vahendajat: see on lihtsalt küsimus Suzie sammude kordamisest iga vahendaja jaoks. Iga sõlm on kaitstud HTLC-de tingimustega, sest viimase HTLC avamine saaja poolt käivitab automaatselt kõigi teiste HTLC-de kaskaadse avamise.

### HTLC-de aegumine ja haldamine probleemide korral

Kui makseprotsessi ajal üks vahendajatest või saaja sõlm ei vasta, eriti interneti- või elektrikatkestuse korral, siis makset ei saa lõpule viia, kuna vajalikku saladust HTLC-de avamiseks ei edastata. Võttes meie näite Alicest, Suziest ja Bobist, tekib see probleem näiteks siis, kui Bob ei anna saladust _s_ Suziele. Sel juhul blokeeritakse kõik marsruudi ülesvoolu HTLC-d ja samuti nende poolt tagatud vahendid.

![LNP201](assets/en/54.webp)

Selle vältimiseks on Lightningi HTLC-del aegumistähtaeg, mis võimaldab HTLC eemaldada, kui seda ei ole teatud aja jooksul lõpule viidud. Aegumine järgib kindlat järjekorda, kuna see algab esmalt HTLC-ga, mis on saajale kõige lähemal, ja liigub seejärel järk-järgult ülespoole tehingu väljastajani. Meie näites, kui Bob ei anna kunagi saladust _s_ Suziele, põhjustaks see esmalt Suzie HTLC aegumise Bobi suunas.

![LNP201](assets/en/55.webp)

Seejärel Alice'i HTLC Suzie suunas.
![LNP201](assets/en/56.webp)
Kui aegumise järjekord oleks vastupidine, võiks Alice oma makse tagasi saada enne, kui Suzie suudaks end potentsiaalse pettuse eest kaitsta. Tõepoolest, kui Bob tuleb tagasi, et nõuda oma HTLC-d, samal ajal kui Alice on juba oma oma eemaldanud, oleks Suzie ebasoodsas olukorras. See kaskaadne HTLC-de aegumise järjekord tagab seega, et ükski vahendajast sõlm ei kannataks ebaõiglasi kaotusi.

### HTLC-de esitus kohustuslike tehingute puhul

Kohustuslikud tehingud esitavad HTLC-sid sellisel viisil, et tingimused, mida need Lightning'ile seavad, saab üle kanda Bitcoinile, juhul kui kanal suletakse sunniviisiliselt HTLC eluea jooksul. Meenutuseks, kohustuslikud tehingud esindavad kahe kasutaja vahelise kanali praegust seisundit ja võimaldavad ühepoolset sunniviisilist sulgemist probleemide korral. Iga kanali uue seisundi korral luuakse 2 kohustuslikku tehingut: üks mõlemale poolele. Vaatame meie näidet Alice'i, Suzie ja Bobiga, kuid uurime lähemalt, mis toimub kanalitasandil Alice'i ja Suzie vahel, kui HTLC luuakse.
![LNP201](assets/en/57.webp)

Enne 40 000 satsi makse algust Alice'i ja Bobi vahel, on Alice'il oma kanalis Suzie'ga 100 000 satsi, samal ajal kui Suzie'l on 30 000. Nende kohustuslikud tehingud on järgmised:

![LNP201](assets/en/58.webp)

Alice on just saanud Bobi arve, mis sisaldab märkimisväärselt _r_, salajase väärtuse räsi. Seega saab ta luua Suzie'ga 40 000 satoshi suuruse HTLC. See HTLC on esitatud viimastes kohustuslikes tehingutes väljundina nimega "**_HTLC Out_**" Alice'i poolel, kuna vahendid on väljaminevad, ja "**_HTLC In_**" Suzie poolel, kuna vahendid on sissetulevad.

![LNP201](assets/en/59.webp)

Need HTLC-ga seotud väljundid jagavad täpselt samu tingimusi, nimelt:

- Kui Suzie suudab pakkuda salajast _s_, saab ta selle väljundi kohe avada ja üle kanda aadressile, mida ta kontrollib.
- Kui Suzie ei oma salajast _s_, ei saa ta seda väljundit avada, ja Alice saab selle pärast ajaluku avada, et saata see aadressile, mida ta kontrollib. Ajalukk annab seega Suzie'le aega reageerida, kui ta saab _s_.

Need tingimused kehtivad ainult juhul, kui kanal suletakse (st kohustuslik tehing avaldatakse ahelas), samal ajal kui HTLC on endiselt aktiivne Lightning'is, tähendades, et Alice'i ja Bobi vaheline makse ei ole veel lõpule viidud ja HTLC-d ei ole veel aegunud. Tänu nendele tingimustele saab Suzie taastada talle võlgu olevad 40 000 satoshit HTLC-st, pakkudes _s_. Vastasel juhul taastab Alice vahendid pärast ajaluku aegumist, sest kui Suzie ei tea _s_, tähendab see, et ta ei ole üle kandnud 40 000 satoshit Bobile, ja seetõttu ei ole Alice'i vahendid talle võlgu.

Lisaks, kui kanal suletakse, samal ajal kui mitu HTLC-d on ootel, luuakse nii palju lisaväljundeid, kui on käimasolevaid HTLC-sid.
Kui kanalit ei suleta, siis pärast Lightningi makse aegumist või õnnestumist luuakse uued kohustuslikud tehingud, et kajastada kanali uut, nüüd stabiilset seisundit, st ilma ühegi ootel HTLC-ta. Seega saab HTLC-dega seotud väljundid kohustuslikest tehingutest eemaldada.
![LNP201](assets/en/60.webp)
Lõpuks, kui koostööl põhinev kanali sulgemine toimub samal ajal, kui HTLC on aktiivne, lõpetavad Alice ja Suzie uute maksete vastuvõtmise ja ootavad käimasolevate HTLC-de lahendamist või aegumist. See võimaldab neil avaldada kergema sulgemistehingu, ilma HTLC-dega seotud väljunditeta, vähendades seeläbi tasusid ja vältides võimaliku ajaluku ootamist.
**Mida peaksite sellest peatükist kaasa võtma?**

HTLC-d võimaldavad Lightning maksete suunamist mitme sõlme kaudu, ilma et peaks neid usaldama. Siin on peamised punktid, mida meeles pidada:

1. HTLC-d tagavad maksete turvalisuse saladuse (eelkujutis) ja aegumisaja kaudu.
2. HTLC-de lahendamine või aegumine järgib kindlat järjekorda: siis sihtpunktist allika suunas, et kaitsta iga sõlme.
3. Niikaua kui HTLC ei ole lahendatud ega aegunud, hoitakse seda väljundina kõige uuemates kohustuste tehingutes.

Järgmises peatükis avastame, kuidas sõlm, mis väljastab Lightning tehingu, leiab ja valib marsruudid oma makse kohaletoimetamiseks saaja sõlmele.

## Oma Tee Leidmine

<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>

![oma tee leidmine](https://youtu.be/wnUGJjOxd9Q)

Eelmistes peatükkides nägime, kuidas kasutada teiste sõlmede kanaleid maksete suunamiseks ja sõlmele jõudmiseks, ilma et oleksime sellega otse kanali kaudu ühendatud. Samuti arutasime, kuidas tagada ülekande turvalisus, ilma et peaksime vahepealseid sõlmi usaldama. Selles peatükis keskendume parima võimaliku marsruudi leidmisele sihtsõlme jõudmiseks.

### Marsruutimise Probleem Lightningis

Nagu oleme näinud, peab Lightningis makset saatva sõlme arvutama täieliku marsruudi saajani, kuna kasutame sibulmarsruutimise süsteemi. Vahepealsed sõlmed ei tea ei lähtepunkti ega lõppsihtkohta. Nad teavad ainult, kust makse tuleb ja millisele sõlmele nad peavad selle järgmisena edastama. See tähendab, et saatva sõlme peab säilitama dünaamilise kohaliku topoloogia võrgust, olemasolevate Lightning sõlmede ja nende vaheliste kanalitega, arvestades avamisi, sulgemisi ja olekuuuendusi.

![LNP201](assets/en/61.webp)
Isegi selle Lightning Networki topoloogiaga on marsruutimiseks olulist infot, mis jääb saatva sõlme jaoks kättesaamatuks, mis on kanalites igal hetkel täpne likviidsuse jaotus. Tõepoolest, iga kanal näitab ainult oma **koguvõimsust**, kuid fondide sisemine jaotus on teada ainult kahele osalevale sõlmele. See tekitab tõhusa marsruutimise väljakutseid, kuna makse õnnestumine sõltub märkimisväärselt sellest, kas selle summa on väiksem kui valitud marsruudil olev madalaim likviidsus. Siiski, likviidsused ei ole saatva sõlme jaoks kõik nähtavad.
![LNP201](assets/en/62.webp)

### Võrgukaardi Uuendamine

Selleks, et hoida oma võrgukaarti ajakohasena, vahetavad sõlmed regulaarselt sõnumeid algoritmi kaudu, mida nimetatakse "**_gossip_**" (kuulujutt). See on hajutatud algoritm, mida kasutatakse informatsiooni epideemiliseks levitamiseks kõigile võrgu sõlmedele, mis võimaldab kanalite globaalse oleku vahetamist ja sünkroniseerimist mõne suhtlusetsükli jooksul. Iga sõlm levitab teavet ühele või mitmele juhuslikult või mitte juhuslikult valitud naabrile, need omakorda levitavad teavet teistele naabritele ja nii edasi, kuni saavutatakse globaalselt sünkroniseeritud olek.

Kahe peamise Lightning sõlmede vahel vahetatava sõnumi on järgmised:

- "**Channel Announcements**": sõnumid, mis teatavad uue kanali avamisest.
- "**Kanali Uuendused**": uuenduste sõnumid kanali seisundi kohta, eriti tasude arengu kohta (kuid mitte likviidsuse jaotuse kohta).
  Lightning sõlmed jälgivad samuti Bitcoin'i plokiahelat, et tuvastada kanali sulgemise tehinguid. Sulgemise järel eemaldatakse kanal kaardilt, kuna seda ei saa enam maksete suunamiseks kasutada.

### Makse Suunamine

Võtame näiteks väikese Lightning Network'i, kus on 7 sõlme: Alice, Bob, 1, 2, 3, 4 ja 5. Kujutame ette, et Alice soovib saata makse Bobile, kuid peab läbima vahendajate sõlmed.

![LNP201](assets/en/63.webp)

Siin on tegelik rahade jaotus nendes kanalites:

- **Kanal Alice'i ja 1 vahel**: 250,000 satsi Alice'i poolel, 80,000 1 poolel (kogumaht 330,000 satsi).
- **Kanal 1 ja 2 vahel**: 300,000 satsi 1 poolel, 200,000 2 poolel (kogumaht 500,000 satsi).
- **Kanal 2 ja 3 vahel**: 50,000 satsi 2 poolel, 60,000 3 poolel (kogumaht 110,000 satsi).
- **Kanal 2 ja 5 vahel**: 90,000 satsi 2 poolel, 160,000 5 poolel (kogumaht 250,000 satsi).
- **Kanal 2 ja 4 vahel**: 180,000 satsi 2 poolel, 110,000 4 poolel (kogumaht 290,000 satsi).
- **Kanal 4 ja 5 vahel**: 200,000 satsi 4 poolel, 10,000 5 poolel (kogumaht 210,000 satsi).
- **Kanal 3 ja Bobi vahel**: 50,000 satsi 3 poolel, 250,000 Bobi poolel (kogumaht 300,000 satsi).
- **Kanal 5 ja Bobi vahel**: 260,000 satsi 5 poolel, 100,000 Bobi poolel (kogumaht 360,000 satsi).

![LNP201](assets/en/64.webp)

Makse tegemiseks 100,000 satsi ulatuses Alice'ilt Bobile on suunamisvõimalused piiratud iga kanali saadaoleva likviidsusega. Alice'i jaoks optimaalne marsruut, lähtudes teadaolevatest likviidsuse jaotustest, võiks olla jada `Alice → 1 → 2 → 4 → 5 → Bob`:

![LNP201](assets/en/65.webp)

Kuid kuna Alice ei tea iga kanali täpset rahade jaotust, peab ta optimaalse marsruudi tõenäosuslikult hindama, võttes arvesse järgmisi kriteeriume:

- **Edu tõenäosus**: kanal, mille kogumaht on suurem, on tõenäolisemalt piisavalt likviidne. Näiteks kanalil sõlme 2 ja sõlme 3 vahel on kogumaht 110,000 satsi, seega on ebatõenäoline leida 100,000 satsi või rohkem sõlme 2 poolel, kuigi see jääb võimalikuks.
- **Tehingutasud**: parima marsruudi valimisel arvestab saatja sõlm ka iga vahesõlme rakendatud tasusid ja püüab minimeerida kogu suunamiskulu.
- **HTLC-de aegumine**: et vältida maksete blokeerimist, on HTLC-de aegumisaeg samuti arvesse võetav parameeter.
- **Vahepealsete sõlmede arv**: lõpuks, laiemalt vaadates, püüab saatja sõlm leida marsruudi võimalikult väheste sõlmedega, et vähendada rikke riski ja piirata Lightning tehingutasusid.
  Neid kriteeriume analüüsides saab saatja sõlm testida kõige tõenäolisemaid marsruute ja üritada neid optimeerida. Meie näites võiks Alice parimad marsruudid järjestada järgmiselt:

1. `Alice → 1 → 2 → 5 → Bob`, kuna see on lühim marsruut suurima mahutavusega.
2. `Alice → 1 → 2 → 4 → 5 → Bob`, kuna see marsruut pakub head mahutavust, kuigi on pikem kui esimene.
3. `Alice → 1 → 2 → 3 → Bob`, kuna see marsruut hõlmab kanalit `2 → 3`, mille mahutavus on väga piiratud, kuid jääb siiski potentsiaalselt kasutatavaks.

### Makse Täitmine

Alice otsustab testida oma esimest marsruuti (`Alice → 1 → 2 → 5 → Bob`). Seega saadab ta HTLC 100 000 satsi sõlmele 1. See sõlm kontrollib, kas tal on piisavalt likviidsust sõlmega 2, ja jätkab ülekannet. Sõlm 2 saab HTLC sõlmelt 1, kuid mõistab, et tal pole oma kanalis sõlmega 5 piisavalt likviidsust, et suunata 100 000 satsi makset. Seejärel saadab ta veateate tagasi sõlmele 1, kes edastab selle Alice'ile. See marsruut on ebaõnnestunud.

![LNP201](assets/en/66.webp)

Seejärel üritab Alice suunata oma makse kasutades oma teist marsruuti (`Alice → 1 → 2 → 4 → 5 → Bob`). Ta saadab HTLC 100 000 satsi sõlmele 1, kes edastab selle sõlmele 2, seejärel sõlmele 4, sõlmele 5 ja lõpuks Bobile. Seekord on likviidsus piisav ja marsruut toimib. Iga sõlm avab oma HTLC kaskaadselt, kasutades Bobi poolt antud eelkujutist (saladus _s_), mis võimaldab Alice'i makse Bobile edukalt lõpule viia.

![LNP201](assets/en/67.webp)

Marsruudi otsing toimub järgmiselt: saatja sõlm alustab parimate võimalike marsruutide tuvastamisega, seejärel üritab makseid järjestikku, kuni leitakse toimiv marsruut.

On oluline märkida, et Bob võib Alice'ile **arvel** esitatud teabega hõlbustada marsruudi leidmist. Näiteks võib ta näidata lähedal asuvaid kanaleid piisava likviidsusega või paljastada privaatkanalite olemasolu. Need vihjed võimaldavad Alice'il vältida vähe edukate marsruutide kasutamist ja esmalt proovida Bobi soovitatud teid.

**Mida peaksite sellest peatükist kaasa võtma?**

1. Sõlmed hoiavad võrgu topoloogia kaarti läbi teadaannete ja jälgides kanalite sulgemist Bitcoin'i plokiahelas.
2. Makse optimaalse marsruudi otsing on tõenäosuslik ja sõltub paljudest kriteeriumitest.
3. Bob võib **arvel** anda vihjeid, mis juhivad Alice'i marsruudi valikut ja hoiavad teda ebatõenäoliste marsruutide katsetamisest.

Järgmises peatükis uurime spetsiifiliselt arvete toimimist, lisaks mõningaid teisi Lightning Network'is kasutatavaid tööriistu.

# Lightning Network'i Tööriistad

<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>

## Arve, LNURL ja Keysend

<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>
![arve, LNURL, Keysend](https://youtu.be/CHnXJuZTarU)
Selles peatükis vaatame lähemalt Lightning **arvete** tööpõhimõtet, see tähendab maksepäringuid, mida saaja sõlm saadab saatja sõlmele. Eesmärk on mõista, kuidas Lightningis makseid teha ja vastu võtta. Arutleme ka kahe klassikalisele arvetele alternatiivi üle: LNURL ja Keysend.
![LNP201](assets/en/68.webp)

### Lightning Arvete Struktuur

Nagu HTLC-de peatükis selgitatud, algab iga makse **arve** genereerimisega saaja poolt. See arve edastatakse seejärel maksjale (QR-koodi või kopeerimise ja kleepimise teel), et makse algatada. Arve koosneb kahest peamisest osast:

1. **Inimloetav Osa**: see jaotis sisaldab selgelt nähtavat metaandmeid, et parandada kasutajakogemust.
2. **Andmeosa**: see jaotis sisaldab masinate poolt makse töötlemiseks mõeldud teavet.

Tüüpilise arve struktuur algab identifikaatoriga `ln` "Lightning" jaoks, millele järgneb `bc` Bitcoinile, seejärel arve summa. Eraldaja `1` eristab inimloetavat osa andmeosast.

Võtame näiteks järgmise arve:

```invoice
lnbc100u1p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

Saame selle juba jagada kaheks osaks. Esiteks, inimloetav osa:

```invoice
lnbc100u
```

Seejärel andmeosa:

```invoice

p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

Kaks osa on eraldatud `1`-ga. See eraldaja valiti erimärgi asemel, et võimaldada terve arve lihtsat kopeerimist topeltklõpsuga.
Esimeses osas näeme, et:

- `ln` näitab, et tegemist on Lightning tehinguga.
- `bc` näitab, et Lightning võrk asub Bitcoin'i plokiahelas (mitte testvõrgus ega Litecoin'il).
- `100u` näitab arve summat, väljendatuna **mikrosatoshi'des** (`u` tähendab "mikro"), mis siin võrdub 10,000 satsiga.

Maksesumma määramiseks väljendatakse seda bitcoini alaühikutes. Siin on kasutatud ühikud:

- **Millibitcoin (tähisega `m`):** Esindab üht tuhandikku bitcoinist.

  $$
  1 \, \text{mBTC} = 10^{-3} \, \text{BTC} = 10^5 \, \text{satoshi}
  $$

- **Mikrobitcoin (tähisega `u`):** Mõnikord nimetatud ka "bit", esindab üht miljonikku bitcoinist.

  $$
  1 \, \mu\text{BTC} = 10^{-6} \, \text{BTC} = 100 \, \text{satoshi}
  $$

- **Nanobitcoin (tähisega `n`):** Esindab üht miljardikku bitcoinist.

  $$
  1 \, \text{nBTC} = 10^{-9} \, \text{BTC} = 0.1 \, \text{satoshi}
  $$

- **Pikobitcoin (tähisega `p`):** Esindab üht triljonikku bitcoinist.
  $$
  1 \, \text{pBTC} = 10^{-12} \, \text{BTC} = 0.0001 \, \text{satoshi}
  $$

### Arve Sisu

Arve sisu hõlmab mitmeid makse töötlemiseks vajalikke teabeosi:

- **Ajatempel:** Arve loomise hetk, väljendatuna Unixi ajatemplina (sekundite arv, mis on möödunud alates 1. jaanuarist 1970).
- **Saladuse räsistamine**: Nagu nägime HTLC-de jaotises, peab vastuvõttev sõlm andma saatva sõlmele eelkujutise räsi. Seda kasutatakse HTLC-des tehingu turvamiseks. Me nimetasime seda "_r_"-iks.
- **Maksesaladus**: Teine saladus genereeritakse saaja poolt, kuid seekord edastatakse see saatva sõlmele. Seda kasutatakse sibulmarsruutimises, et vältida vahepealsetel sõlmedel arvamast, kas järgmine sõlm on lõppsaaja või mitte. See säilitab seega teatud konfidentsiaalsuse saaja suhtes viimase vahepealse sõlme ees marsruudil.
- **Saaja Avalik Võti**: Näitab maksjale makstava isiku identifikaatorit.
- **Aegumise Kestus**: Maksimaalne aeg arve tasumiseks (vaikimisi 1 tund).
- **Marsruudi Viited**: Saaja poolt antud lisateave, mis aitab saatjal optimeerida makseteed.
- **Allkiri**: Tagab arve terviklikkuse, autentides kogu teabe.

Arved kodeeritakse seejärel **bech32** formaadis, sama formaat nagu Bitcoin SegWit aadressidel (formaadiga alustades `bc1`).

### LNURL Väljamakse

Traditsioonilises tehingus, nagu poeost, genereeritakse arve kogusumma tasumiseks. Kui arve esitatakse (QR-koodi või tähemärkide jada kujul), saab klient selle skaneerida ja tehingu lõpule viia. Makse järgib seejärel traditsioonilist protsessi, mida me eelmises jaotises uurisime. Siiski võib see protsess mõnikord olla kasutajakogemuse jaoks väga tülikas, kuna see nõuab saajalt saatjale arve kaudu teabe saatmist.

Teatud olukordades, nagu bitcoiinide väljavõtmine veebiteenusest, on traditsiooniline protsess liiga tülikas. Sellistel juhtudel lihtsustab **LNURL** väljavõtmise lahendus seda protsessi, kuvades QR-koodi, mille saaja rahakott skaneerib automaatselt arve loomiseks. Teenus seejärel maksab arve ja kasutaja näeb lihtsalt koheselt toimuvat väljavõtmist.

![LNP201](assets/en/69.webp)

LNURL on suhtlusprotokoll, mis määratleb funktsioonide kogumi, mille eesmärk on lihtsustada suhtlust Lightning sõlmede ja klientide, samuti kolmandate osapoolte rakenduste vahel. Nagu me just nägime, on LNURL väljavõtmine seega vaid üks näide teiste funktsioonide hulgas.
See protokoll põhineb HTTP-l ja võimaldab luua linke erinevateks toiminguteks, nagu makse- või väljavõtmistaotlus, või muud funktsioonid, mis parandavad kasutajakogemust. Iga LNURL on bech32 kodeeritud URL lnurl eesliitega, mis, kui skaneeritud, käivitab Lightning rahakotis automaatsete toimingute seeria.
Näiteks LNURL-väljavõtte (LUD-03) funktsioon võimaldab teenusest raha välja võtta QR-koodi skaneerides, ilma et oleks vaja käsitsi genereerida arvet. Samamoodi võimaldab LNURL-auth (LUD-04) sisse logida veebiteenustesse kasutades oma Lightning rahakoti privaatvõtit parooli asemel.

### Lightning Makse Saatmine Ilma Arveta: Keysend

Teine huvitav juhtum on vahendite ülekandmine ilma eelnevalt saadud arveta, mida tuntakse kui "**Keysend**". See protokoll võimaldab saata vahendeid lisades eelkujutise krüpteeritud makseandmetesse, mis on kättesaadavad ainult saajale. See eelkujutis võimaldab saajal avada HTLC, seega saades vahendid kätte ilma eelnevalt arvet genereerinud olemata.

Lihtsustatult, selles protokollis on saatja see, kes genereerib HTLC-des kasutatava saladuse, mitte saaja. Praktiliselt võimaldab see saatjal teha makse ilma eelnevalt saajaga suhelnud olemata.

![LNP201](assets/en/70.webp)

**Mida peaksite sellest peatükist kaasa võtma?**

1. **Lightning Arve** on maksetaotlus, mis koosneb inimloetavast osast ja masinaandmete osast.
2. Arve kodeeritakse **bech32** formaadis, `1` eraldajaga kopeerimise hõlbustamiseks ja andmeosaga, mis sisaldab kogu makse töötlemiseks vajalikku teavet.
3. Lightningil on olemas ka teisi makseprotsesse, eriti **LNURL-Withdraw** väljavõtmiste hõlbustamiseks ja **Keysend** otseülekanneteks ilma arveta.

Järgmises peatükis vaatleme, kuidas sõlmeoperaator saab hallata oma kanalites likviidsust, et mitte kunagi olla blokeeritud ja alati suuta saata ning vastu võtta makseid Lightning võrgus.

## Oma Likviidsuse Haldamine

<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>

![oma likviidsuse haldamine](https://youtu.be/YuPrbhEJXbg)

Sel peatükis uurime strateegiaid likviidsuse efektiivseks haldamiseks Lightning võrgus. Likviidsuse haldamine varieerub sõltuvalt kasutaja tüübist ja kontekstist. Vaatleme peamisi põhimõtteid ja olemasolevaid tehnikaid, et paremini mõista, kuidas seda haldust optimeerida.

### Likviidsuse Vajadused

Lightning'il on kolm peamist kasutajaprofiili, millest igaühel on spetsiifilised likviidsusvajadused:

1. **Maksja**: See on isik, kes teeb makseid. Neil on vaja väljaminevat likviidsust, et suuta üle kanda vahendeid teistele kasutajatele. Näiteks võib see olla tarbija.
2. **Müüja (või Saaja)**: See on isik, kes saab makseid. Neil on vaja sissetulevat likviidsust, et suuta vastu võtta makseid oma sõlme. Näiteks võib see olla ettevõte või veebipood.
3. **Ruuter**: Vahepealne sõlm, mis on sageli spetsialiseerunud maksete suunamisele, peab optimeerima oma likviidsust igas kanalis, et suunata võimalikult palju makseid ja teenida tasusid.

Need profiilid ei ole muidugi fikseeritud; kasutaja võib sõltuvalt tehingutest vahetada maksja ja saaja rolli. Näiteks võib Bob saada oma palga Lightning'is oma tööandjalt, mis asetab ta "müüja" positsioonile, vajades sissetulevat likviidsust. Järgnevalt, kui ta soovib oma palka kasutada toidu ostmiseks, muutub ta "maksjaks" ja peab seejärel omama väljaminevat likviidsust.

Paremaks mõistmiseks võtame näite lihtsast võrgust, mis koosneb kolmest sõlmest: ostja (Alice), ruuter (Suzie) ja müüja (Bob).

![LNP201](assets/en/71.webp)

Kujutage ette, et ostja soovib saata 30 000 satsi müüjale ja et makse läheb läbi ruuteri sõlme. Igal osapoolel peab siis olema minimaalne likviidsuse summa makse suunas:

- Maksjal peab olema vähemalt 30 000 satoshit oma kanali poolel ruuteriga.
- Müüjal peab olema kanal, kus 30 000 satoshit on vastaspoolel, et suuta neid vastu võtta.
- Ruuteril peab olema 30 000 satoshit maksja poolel oma kanalis ja samuti 30 000 satoshit oma poolel kanalis müüjaga, et suuta makset suunata.

![LNP201](assets/en/72.webp)

### Likviidsuse Haldamise Strateegiad

Maksjad peavad tagama piisava likviidsuse oma kanalite poolel, et tagada väljaminev likviidsus. See osutub suhteliselt lihtsaks, kuna piisab uute Lightning kanalite avamisest, et omada seda likviidsust. Tõepoolest, multisigis lukustatud algfondid on Lightning kanalis alguses täielikult maksja poolel. Maksevõime on seega tagatud, kuni kanalid avatakse piisavate vahenditega. Kui väljaminev likviidsus on ammendatud, piisab uute kanalite avamisest.
Teisest küljest on müüja ülesanne keerulisem. Selleks, et suuta makseid vastu võtta, peavad neil olema likviidsus oma kanalite vastaspoolel. Seega ei piisa ainult kanali avamisest: nad peavad samuti tegema makse selles kanalis, et liigutada likviidsus teisele poolele enne, kui nad saavad ise makseid vastu võtta. Teatud Lightning kasutajaprofiilide jaoks, nagu kaupmehed, on selge ebaproportsionaalsus selle vahel, mida nende sõlm saadab ja mida see vastu võtab, kuna ettevõtte eesmärk on peamiselt koguda rohkem kui kulutada, et genereerida kasumit. Õnneks on neil kasutajatel, kellel on spetsiifilised sissetuleva likviidsuse vajadused, olemas mitu lahendust:

- **Kanalite meelitamine**: Kaupmees saab eelise tänu oma sõlmele oodatavate sissetulevate maksete mahule. Arvestades seda, võivad nad püüda meelitada suunamissõlmi, kes otsivad tulu tehingutasudest ja kes võivad avada kanaleid nende poole, lootes suunata nende makseid ja koguda seotud tasusid.
- **Likviidsuse liikumine**: Müüja võib samuti avada kanali ja kanda osa vahenditest vastaspoolele, tehes fiktiivseid makseid teisele sõlmele, mis tagastab raha muul viisil. Järgmises osas näeme, kuidas seda toimingut teostada.
- **Kolmnurkne avamine**: Platvormid on olemas sõlmedele, kes soovivad kanaleid koostöös avada, võimaldades igaühel saada kohe sissetulevat ja väljaminevat likviidsust. Näiteks [LightningNetwork+](https://lightningnetwork.plus/) pakub seda teenust. Kui Alice, Bob ja Suzie soovivad avada kanali 100 000 satiga, võivad nad sellel platvormil kokku leppida, et Alice avab kanali Bobi suunas, Bob Suzie suunas ja Suzie Alice'i suunas. Sel viisil on igal neist 100 000 sati väljaminevat likviidsust ja 100 000 sati sissetulevat likviidsust, olles samal ajal lukustanud ainult 100 000 sati.

![LNP201](assets/en/73.webp)

- **Kanalite ostmine**: Teenused Lightning kanalite rentimiseks on samuti olemas, et saada sissetulevat likviidsust, nagu [Bitrefill Thor](https://www.bitrefill.com/thor-lightning-network-channels/) või [Lightning Labs Pool](https://lightning.engineering/pool/). Näiteks Alice võib osta kanali ühe miljoni satoshiga oma sõlme suunas, et saada makseid vastu võtta.

![LNP201](assets/en/74.webp)

Lõpuks, marsruuterite jaoks, kelle eesmärk on maksimeerida töödeldud maksete arvu ja kogutud tasusid, peavad nad:

- Avama hästi rahastatud kanalid strateegiliste sõlmedega.
- Regulaarselt kohandama vahendite jaotust kanalites vastavalt võrgu vajadustele.

### Loop Out teenus

[Loop Out](https://lightning.engineering/loop/) teenus, mida pakub Lightning Labs, võimaldab liigutada likviidsust kanali vastaspoolele, taastades samal ajal vahendid Bitcoin'i plokiahelas. Näiteks Alice saadab 1 miljon satoshit Lightningu kaudu loop sõlmele, mis seejärel tagastab need vahendid talle on-chain bitcoinides. See tasakaalustab tema kanali 1 miljoni satoshiga mõlemal poolel, optimeerides tema võimet makseid vastu võtta.

![LNP201](assets/en/75.webp)

Seega võimaldab see teenus sissetulevat likviidsust, taastades samal ajal oma bitcoinid on-chain, mis aitab piirata sularaha immobiliseerimist, mis on vajalik Lightningu maksete vastuvõtmiseks.

**Mida peaksite sellest peatükist kaasa võtma?**

- Maksete saatmiseks Lightningus peab teil olema piisavalt likviidsust oma kanalites teie poolel. Selle saatmisvõime suurendamiseks avage lihtsalt uusi kanaleid.
- Maksete vastuvõtmiseks on vaja likviidsust vastaspoolel teie kanalites. Selle vastuvõtuvõime suurendamine on keerulisem, kuna see nõuab teistelt kanalite avamist teie suunas või (fiktiivsete või reaalsete) maksete tegemist likviidsuse teisele poolele liigutamiseks.
- Likviidsuse säilitamine soovitud kohas võib olla veelgi keerulisem sõltuvalt kanalite kasutamisest. Seetõttu on olemas tööriistad ja teenused, mis aitavad kanaleid soovitud viisil tasakaalustada.

Järgmises peatükis pakun üle vaadata selle koolituse kõige olulisemad kontseptsioonid.

# Minge kaugemale

<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>

## Koolituse järeldus

<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>

![järeldus](https://youtu.be/MaWpD0rbkVo)
Selles viimases peatükis, mis tähistab LNP201 koolituse lõppu, teen ettepaneku vaadata üle olulised kontseptsioonid, mida oleme koos käsitletud.
Selle koolituse eesmärk oli anda teile põhjalik ja tehniline arusaam Lightning Networkist. Avastasime, kuidas Lightning Network toetub Bitcoin'i plokiahelale, et teostada off-chain tehinguid, säilitades samal ajal Bitcoin'i põhilised omadused, eriti vajaduse puudumise usaldada teisi sõlmi.

### Maksekanalid

Esimestes peatükkides uurisime, kuidas kaks osapoolt, avades maksekanali, saavad teostada tehinguid väljaspool Bitcoin'i plokiahelat. Siin on käsitletud sammud:

1. **Kanali Avamine**: Kanali loomine toimub läbi Bitcoin'i tehingu, mis lukustab vahendid 2/2 multisignatuuriga aadressile. See sissemakse esindab Lightning kanalit plokiahelas.

![LNP201](assets/en/76.webp) 2. **Tehingud Kanalis**: Selles kanalis on seejärel võimalik teostada arvukalt tehinguid ilma, et peaks neid plokiahelas avaldama. Iga Lightning tehing loob kanali uue seisundi, mida kajastab kohustuse tehing.
![LNP201](assets/en/77.webp)

3. **Turvamine ja Sulgemine**: Osalejad kinnitavad kanali uut seisundit, vahetades tühistamisvõtmeid, et turvata vahendeid ja vältida pettust. Mõlemad pooled saavad kanali koostööd tehes sulgeda, tehes uue tehingu Bitcoin'i plokiahelas, või viimase abinõuna läbi sunnitud sulgemise. See viimane võimalus, kuigi vähem efektiivne, kuna see on pikem ja mõnikord halvasti hinnatud tasude osas, võimaldab siiski vahendite taastamist. Pettuse korral saab ohver petturit karistada, taastades kõik kanali vahendid plokiahelas.

![LNP201](assets/en/78.webp)

### Kanalite Võrgustik

Isolatsioonis kanalite uurimise järel laiendasime oma analüüsi kanalite võrgustikule:

- **Suunamine**: Kui kaks osapoolt ei ole otseselt ühendatud kanaliga, võimaldab võrgustik suunata makseid läbi vahendajate sõlmede. Maksed liiguvad siis ühest sõlmest teise.

![LNP201](assets/en/79.webp)

- **HTLCd**: Vahendajate sõlmede kaudu liikuvad maksed on turvatud "_Hash Time-Locked Contracts_" (HTLC) abil, mis võimaldavad vahendeid lukustada kuni makse on lõpuni teostatud.

![LNP201](assets/en/80.webp)

- **Onion Routing**: Makse konfidentsiaalsuse tagamiseks maskeerib onion routing lõppsihtkoha vahendajate sõlmede eest. Saatja sõlm peab seega arvutama kogu marsruudi, kuid kanalite likviidsuse täieliku teabe puudumisel toimub makse suunamine järjestikuste katsete kaudu.

![LNP201](assets/en/81.webp)

### Likviidsuse Haldamine

Oleme näinud, et likviidsuse haldamine on Lightningis väljakutse, et tagada maksete sujuv liikumine. Maksete saatmine on suhteliselt lihtne: see nõuab lihtsalt kanali avamist. Kuid maksete vastuvõtmine nõuab likviidsuse olemasolu oma kanalite vastasküljel. Siin on arutatud mõningaid strateegiaid:

- **Kanalite Meelitamine**: Teisi sõlmi kanaleid enda poole avama julgustades saab kasutaja sissetulevat likviidsust.

- **Likviidsuse Liigutamine**: Maksete saatmisega teistesse kanalitesse liigub likviidsus vastasküljele.

![LNP201](assets/en/82.webp)

- **Teenuste Nagu Loop ja Pool Kasutamine**: Need teenused võimaldavad tasakaalustada või osta kanaleid likviidsusega vastasküljel.
  ![LNP201](assets/en/83.webp)
- **Koostöölised Avamised**: On ka platvorme saadaval, et ühenduda kolmnurksete avamiste sooritamiseks ja sissetuleva likviidsuse saamiseks.

![LNP201](assets/en/84.webp)

# Kokkuvõte

<partId>b8715c1c-7ae2-49b7-94c7-35bf85346ad3</partId>

## Hinda seda kursust

<chapterId>38814c99-eb7b-5772-af49-4386ee2ce9b0</chapterId>
<isCourseReview>true</isCourseReview>

## Lõpueksam

<chapterId>7ed33400-aef7-5f3e-bfb1-7867e445d708</chapterId>
<isCourseExam>true</isCourseExam>

## Kokkuvõte

<chapterId>afc0d72b-4fbc-5893-90b2-e27fb519ad02</chapterId>
Palju õnne! 🎉

Olete läbinud LNP 201 koolituse - Sissejuhatus Lightning Network'i!

Võite enda üle uhke olla, sest see pole lihtne teema.

Vähesed inimesed sukelduvad nii sügavale Bitcoini küülikuauku.

Suur tänu **Fanis Michalakisele** selle suurepärase tasuta kursuse eest Lightning Network'i tehnilise toimimise kohta.

Jälgige teda [Twitteris](https://x.com/FanisMichalakis), [tema blogis](https://fanismichalakis.fr/) või tema töö kaudu [LN Markets'is](https://lnmarkets.com/).

Nüüd, kui valdate Lightning Network'i, kutsun teid uurima meie teisi tasuta kursusi Plan ₿ Network'is, et süveneda Satoshi Nakamoto leiutise teistesse aspektidesse:

#### Mõistke, kuidas Bitcoin'i rahakott töötab

https://planb.network/courses/cyp201

#### Avastage Bitcoin'i päritolu ajalugu

https://planb.network/courses/his201

#### Seadistage BTC makseserver

https://planb.network/courses/btc305

#### Omandage Bitcoin'i privaatsuse põhimõtted

https://planb.network/courses/btc204

#### Avastage kaevandamise põhitõed

https://planb.network/courses/min201

#### Õppige looma oma Bitcoin'i kogukonda

https://planb.network/courses/btc302

