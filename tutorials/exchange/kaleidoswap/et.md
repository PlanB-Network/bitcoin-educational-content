---
name: KaleidoSwap
description: Täiustatud juhend RGB varadega kauplemiseks Lightning Network-s koos KaleidoSwapiga
---

![cover](assets/cover.webp)


KaleidoSwap on keerukas avatud lähtekoodiga töölauarakendus, mis katab RGB protokolli ja Lightning Network vahelise lõhe. See on terviklik liides RGB Lightning Node'i haldamiseks, RGB Lightning Service Providers (LSP) suhtlemiseks LSPS1 spetsifikatsiooni kaudu ja RGB varade aatomiliste vahetuste teostamiseks.


Kuna KaleidoSwap ei ole haldusalane lahendus, annab see kasutajatele võimaluse säilitada täielik kontroll oma võtmete ja andmete üle. Kasutades RGB kliendipoolset valideerimisparadigmat, võimaldab see Bitcoin peal privaatseid ja skaleeritavaid arukaid lepinguid. See õpetus sukeldub KaleidoSwapi täiustatud funktsioonidesse, juhatades teid läbi "Värvilise" UTXO juhtimise keerukuse, konkreetsete varade kanali likviidsuse ja võtja-tegija kauplemismudeli, tagades, et saate seda võimsat detsentraliseeritud vahetusprotokolli täielikult ära kasutada.


## Paigaldamine


KaleidoSwap pakub eelkoostatud binaarsüsteeme peamiste operatsioonisüsteemide jaoks, kuid edasijõudnud kasutajatele tagab lähtekoodist ehitamine, et te kasutate uusimat koodi oma spetsiifiliste konfiguratsioonidega.


### Binääride allalaadimine


Saate oma operatsioonisüsteemi uusima versiooni alla laadida [ametlikust veebisaidist](https://kaleidoswap.com/) või [GitHubi versioonide lehelt](https://github.com/kaleidoswap/desktop-app/releases).


### Paigaldusmeetodid


1.  **Windows**: Laadige alla `.exe` paigaldusprogramm ja käivitage see.

2.  **macOS**: Laadige alla `.dmg` fail, avage see ja lohistage KaleidoSwap oma rakenduste kausta.

3.  **Linux**: Laadige alla `.AppImage` või `.deb` fail ja installige/käivitage see.



## Sõlme seadistamise valikud


Kui käivitate KaleidoSwapi esimest korda, kuvatakse teile **ühendusekraan**. See on esimene samm teie keskkonna konfigureerimisel.


![Node Selection Screen](assets/en/01.webp)


Peate valima, kuidas ühendada RGB Lightning Network-ga. See valik mõjutab teie kontrolli ja privaatsuse taset.


### Võimalus 1: kohalik sõlmpunkt (soovitatav isehalduse puhul)


**Täieliku kontrolli ja privaatsuse tagamiseks** käivitage sõlme otse oma masinas, vt allpool toodud eeliseid:


- Iseseisev hooldus**: Sul on võtmed käes. Ükski kolmas osapool ei saa teie raha külmutada ega teie tehinguid tsenseerida.
- Privaatsus**: Teie andmed jäävad teie seadmesse.
- Sõltumatus**: Ei sõltu välistest teenusepakkujatest.


Kui valite **Lokaalne sõlme**, viiakse teid seadistusekraanile, kus saate luua uue wallet või taastada olemasoleva.


![Local Node Setup Screen](assets/en/02.webp)


### Võimalus 2: Kaugsõlm


Ühendage kauge RGB Lightning Node (isehostitud VPS-i või hostitud teenusepakkuja).


- Eelised**: Ei kasuta kohalikke ressursse, 24/7 kättesaadavus.
- Kompromiss**: Nõuab vastuvõtja usaldamist või kaugserveri haldamist.


![Remote Node Setup Screen](assets/en/03.webp)


**KaleidoSwap on loodud selleks, et võimaldada isehaldamist.** Soovitame tungivalt käivitada oma sõlme - kas lokaalselt (variant 1) või ise hostides kaugseade -, et kasutada täielikult ära Bitcoin ja RGB tsensuurikindlaid omadusi.


## Wallet loomine


KaleidoSwap haldab nii Bitcoin kui ka RGB varasid. wallet loomise protsess initsialiseerib võtmesalvestuse, mis kindlustab teie on-chain vahendid ja teie Lightning-kanali olekud.


Siin on üksikasjalik protsess:

1. Avage KaleidoSwap ja valige **Lokaalne sõlm**.

2. Klõpsake nupule **Loo uus Wallet**.

3. **Konto seadistamine**: Sisestage **Konto nimi** ja valige **Võrk** (nt Bitcoin Mainnet, Testnet, Signet).

4. **Kasutatud konfiguratsioon** (valikuline): Kui olete võimekas kasutaja, saate seadistada kohandatud RPC lõpp-punktid, indekseerija URL-aadressid või proksi seaded jaotises "Täiustatud seaded".

5. Klõpsake **Jätka**.

6. **Parool**: Määrake tugev parool, et krüpteerida oma wallet faili kohapeal.

7. **Rekvivalentne fraas**: Kirjutage oma seed fraas üles ja säilitage see turvaliselt.


    - Kriitiline**: See lause on vajalik teie on-chain vahendite ja sõlme identiteedi taastamiseks.
    - Hoiatus**: **Välkekanali olekuid ei saa täielikult taastada ainult seed abil**. Kanalite lukustatud vahendite taastamiseks tuleb säilitada ka staatilisi kanali varukoopiaid (SCB).


![Wallet Creation Screen](assets/en/04.webp)



## Armatuurlaua ülevaade


Kui teie wallet on loodud, suunatakse teid peamisele **Kassafoorumile**.


![KaleidoSwap Dashboard](assets/en/05.webp)


märkus: ülaltoodud ekraanipildil on näha wallet, mis on juba rahastatud ja millel on aktiivsed kanalid. Värske wallet näitab nullsaldot ja aktiivseid kanaleid ei ole, kuni te seda rahastate._


## Teie Wallet rahastamine


RGB varadega tegutsemiseks peate rahastama oma wallet. KaleidoSwap toetab nii Bitcoin kui ka RGB varade hoiustamist on-chain tehingute või Lightning Network kaudu.


### Bitcoin hoiustamine


1. Klõpsake kiiretoimingute menüüs **Panustamine**.

2. Valige varade nimekirjast **BTC**.


![Select BTC Asset](assets/en/06.webp)


3. Valige oma sissemakse meetod: **On-chain** või **Lightning**.


![BTC Deposit Options](assets/en/07.webp)



- On-chain**: Skaneerige QR-koodi või kopeerige aadress, et saata Bitcoin teisest wallet-st.
- Välk**: Looge arve soovitud summa kohta.


![BTC On-chain Deposit](assets/en/08.webp)


### RGB varade ja värviliste UTXOde deponeerimine


RGB varade (nagu USDT) saamiseks on vaja konkreetseid UTXOsid, mida saab "värvida" (määrata varale).


1. Klõpsake **Hoiustamine** ja valige RGB vara (nt USDT). **Tähtis**: Kui see on **esimeseks korraks**, kui teie sõlmpunkt saab seda konkreetset vara, **jätke väli Asset ID tühjaks**. Tundmatu vara ID sisestamine põhjustab sõlme veateate, kuna see ei tunne seda veel ära.

2. Valige **Kettaga** või **Välk**.


![USDT Deposit Options](assets/en/09.webp)


#### Kettasisesed vastuvõturežiimid: Blinded


RGB varade on-chain vastuvõtmisel on teil kaks privaatsusrežiimi:



- Pimeda vastuvõtu (soovitatav privaatsuse tagamiseks)**: Sa annad saatjale "blinded" UTXO. Palute saatjal saata varad olemasolevale UTXO-le, mis on teie omanduses, kuid te varjate tegeliku UTXO identifikaatori. See pakub paremat privaatsust.
- Tunnistaja võtab vastu**: Te annate standardse Bitcoin aadressi. Palute saatjal luua teile *uue* UTXO, saates varad sellele aadressile. See võimaldab RGB varasid lisada otse uuele UTXO-le, mis on loodud tehinguga.


#### Välkdeposiit


Lightning deposiitide puhul piisab generate arve esitamisest. RGB vara suunatakse teile avatud kanalite kaudu.


![USDT Lightning Invoice](assets/en/10.webp)



## Kanalite avamine RGB varadega


RGB varade suunamiseks üle Lightning Network on vaja piisava likviidsuse ja varade jaotusega kanalit. Kõige lihtsam viis alustada on **Ostada kanal** LSP-lt (Lightning Service Provider).


### Kanali ostmine Kaleido LSP-lt


1. Mine vahekaardile **Kanalid**. Näete valikuid "Ava kanal" (käsitsi) või "Osta kanal" (LSP).

2. Klõpsake **Ostan kanalit**.


![Channels Dashboard](assets/en/11.webp)


3. **Ühendage LSPga**: Rakendus ühendab end vaikimisi Kaleido LSP-ga. See teenusepakkuja pakub sissetulevat likviidsust ja toetab RGB varade marsruutimist.


![Connect to LSP](assets/en/12.webp)


4. **Konfigureeri kanal**:


    - Maht**: Valige kanali Bitcoin koguvõimsus.
    - RGB eraldamine**: Valige RGB vara (nt USDT), mida soovite saada või saata. LSP tagab, et kanal on konfigureeritud selle vara toetamiseks.


![Configure Channel](assets/en/13.webp)



    - RGB jaotamine**: Valige RGB vara (nt USDT), mida soovite saada või saata. LSP tagab, et kanal on konfigureeritud selle vara toetamiseks.


![RGB Allocation](assets/en/14.webp)


5.  **Maksmine**: Tasu: Te peate maksma LSP-le tasu kanali avamise ja likviidsuse tagamise eest. Võite maksta, kasutades **Lightning** või **On-chain** Bitcoin. Makse võib teha teie sisemise KaleidoSwap wallet või välise wallet kaudu.


![Complete Payment](assets/en/15.webp)


6. Kui makse on kinnitatud, algatab LSP kanali avamise tehingu. Te näete ekraani **Tellimus lõpetatud**.


![Order Completed](assets/en/16.webp)


7. Pärast kinnitust plokiahelas on teie kanal aktiivne ja valmis RGB ülekanneteks.



## Kauplemine: Taker-Maker mudel


KaleidoSwapi kauplemismootor töötab **Taker-Maker-mudelil**. Saate vahetada varasid käsitsi koos partneriga või kasutada turutegijat (LSP).


### Vahetamine turutegijaga (LSP)


See on kõige tavalisem kauplemisviis. Te tegutsete **Taker**, täites korraldusi LSP (**Maker**) poolt pakutava likviidsuse vastu.


1. Mine vahekaardile **Trade** ja vali **Market Maker**.

2. **Kirjutage summa**: Sisestage Bitcoin summa, mida soovite saata (või vara, mida soovite saada). Kasutajaliides näitab hinnangulist vahetuskurssi ja tasusid.


![Market Maker Swap](assets/en/17.webp)


3. **Kinnitage vahetus**: Vaadake üle üksikasjad, sealhulgas vahetuskurss ja täpne summa, mille saate. Klõpsake **Kinnitage vahetus**.


![Confirm Swap](assets/en/18.webp)


4. **Töötlus**: Vahetus toimub Lightning Network-l aatomiliselt. Te näete olekukuva, mis näitab, et vahetus on pooleli.


![Swap Pending](assets/en/19.webp)


5. **Success**: Kui HTLC-d on arveldatud, on vahetus lõpule viidud ja varad on teie kanalis.


![Swap Success](assets/en/20.webp)



## Arendaja API


KaleidoSwapi peal ehitavate arendajate jaoks pakub rakendus API, mis toetab:



- RGB LSPS1**: Automatiseeritud likviidsusteenuste jaoks.
- Vahetus API**: Programmeeritud kauplemiseks ja turutegemiseks.
- WebSocket**: Reaalajas turuandmete tellimiseks.


Täielikud lõpp-punktid ja spetsifikatsioonid on esitatud [API dokumentatsioonis](https://docs.kaleidoswap.com/api/introduction).


## Kokkuvõte


KaleidoSwap võimaldab teil kasutada RGB varade privaatsust ja skaleeritavust Lightning Network-l. Mõistes Colored UTXO-d ja kanalite varade jaotamist, saate seda võimsat detsentraliseeritud vahetusprotokolli täielikult ära kasutada.