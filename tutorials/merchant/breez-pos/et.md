---
nimi: Breez müügipunkt

kirjeldus: Juhend, kuidas hakata Breez POS-i kasutades bitcoine vastu võtma
---

![kaas](assets/cover.webp)

_See tekst pärineb Breez'i dokumentatsiooni veebilehelt: https://doc.breez.technology/How-to-Get-Started-with-Breez-POS.html_

## Mis on Breez POS?

**Breez** on täisteenindusega, mittehoidmisõiguslik Lightning rakendus. Vaatame, mida see tähendab:

- **Lightning** on bitcoin'i maksevõrk, mis vähendab tehinguaegu minutitest millisekunditeni ja tehingutasusid mitmest dollarist mõne sendini või vähem. Lightning muudab bitcoin'i digitaalsest kullast digitaalseks valuutaks, säilitades samal ajal kõik eelised, mis teevad bitcoin'i suurepäraseks.
- **Mittehoidmisõiguslik** tähendab, et Breez ei võta kasutajate raha oma valdusse. Paljud Lightning rakendused võtavad oma kasutajate raha valdusse. Nad on sisuliselt bitcoin'i pangad. Mittehoidmisõigusliku rakendusena nagu Breez, on kõik kasutajad omaenda pangad.
- **Täisteenindus** tähendab, et Breez hoolitseb peaaegu kõigi tehniliste toimingute eest automaatselt ja taustal. Asjad nagu kanali loomine, sissetuleva likviidsuse ja marsruutimine jäävad varjatuks. (Kuid Breez on ka avatud lähtekoodiga, nii et need, kes on huvitatud tehnoloogia auditeerimisest, on teretulnud seda tegema!)

**Breez POS** on lühend meie müügipunkti režiimist. Teisisõnu, Breez toimib nagu digitaalne kassaseade ettevõtetele ja kaupmeestele, kes soovivad vastu võtta Lightning makseid (lisaks selle "standard" režiimile, mis on nagu digitaalse versioon nahast rahakotist bitcoin'i jaoks, ja järgmise põlvkonna podcasti mängija). Vaatame nüüd, kuidas seadistada Breez'i oma ettevõtte Lightning kassaseadmeks.

## Kuidas alustada Breez'iga?

1. Esimene samm on rakenduse allalaadimine. See on saadaval Androidile ja iOS'ile (installige TestFlight ja klõpsake seadmest lingil).
2. Breez saab end automaatselt varundada Google Drive'i, iCloud'i või mis tahes WebDav serverisse.
   > Pange tähele, et iga seade käitab oma Lightning sõlme. Võite käitada POS režiimi nii paljudel seadmetel kui soovite, kuid saldod jäävad eraldi.
3. Rakenduse avamisel klõpsake üleval vasakul asuval ikoonil, et leida Müügipunkti režiim.

## POS seadistamine

1. Klõpsake sellel ikoonil üleval vasakul ja seejärel Müügipunkt > POS Seaded.

### Juhi Parool

POS Seadetes on teil võimalus luua juhi parool. Juhi parool muudab Breez rakendusest väljaminevate maksete tegemise ilma loata võimatuks. Müügipersonal saab seadmest ainult makseid vastu võtta. Pange tähele, et kui kasutate seda võimalust, võiksite ka takistada juurdepääsu Breez'i varundusele, seega on soovitatav kasutada välist WebDav kontot (nt Nextcloud) selle kasutusjuhu jaoks.

### Toote Nimekiri

Toote nimekiri on müügiks olevate esemete kataloog ja nende hinnad. Tooteid saab nimekirja lisada kahel viisil:

- Üksikute esemete sisestamiseks klõpsake peamises POS vaates üleval Items, seejärel paremal all "+" märgil. Siin saate sisestada ühe tüüpi eseme nime, hinna (näidatud teie valitud valuuta ekvivalendis) ja SKU (unikaalne sisemine identifikaator selle tüüpi eseme jaoks; see on valikuline).
- Mitme eseme korraga sisestamiseks klõpsake vasakus ülanurgas kalkulaatori ikoonil, seejärel "Point of Sale" > "Preferences" > "POS Settings" ja seejärel klõpsake paremal asuvatel kolmel punktil "Items List" kõrval ja seejärel "Import from CSV". See võimaldab teil importida ettevalmistatud CSV-faili, mis sisaldab teie esemete nimesid, hindu ja SKU-sid.
### Fiat Display

Breez saadab ja võtab vastu ainult bitcoine ning enamiku Lightning'i tehingute puhul, mis kipuvad olema väiksemate summade jaoks, kuvatakse summat tavaliselt Satoshi'des, tuntud ka kui satsid (1 BTC = 100,000,000 satsi). Siiski leiavad paljud kaupmehed, et on praktiline näha (ja öelda klientidele) ostu väärtust kohalikus fiat-valuutas.

Peamises POS-vaates on praegu kuvatav valuuta nähtav paremal küljel (vaikimisi on SAT). Seal on ka teiste kuvatavate valuutade rippmenüü. Valuutade lisamiseks või eemaldamiseks sellest rippmenüüst klõpsake "Point of Sale" > "Preferences" > "Fiat Currencies". Seejärel märkige lihtsalt rippmenüüs soovitud valuutad ja eemaldage märge nende eest, mida soovite jätta välja.

Kuvatavad väärtused pärinevad yadiost, austatud vahetuskursi andmete allikast, ja neid uuendatakse peaaegu reaalajas. Kuid pidage meeles: olenemata hetkel kuvatavast valuutaväärtusest, on makse ise bitcoinides.

### Tellimuse Vormistamine

Tellimuse koostamiseks lisage esemeid esemete loendist või sisestage lihtsalt summa klaviatuuril. Seejärel klõpsake peamises POS-vaates ülaosas nupul "Charge". Seejärel näete QR-koodi, mida klient saab skannida oma Lightning-rakendusega, mida saate otse teisest rakendusest oma seadmes jagada või mida saate vajadusel kopeerida ja kleepida.

Selle koodi skannimisel või jagatud/kleebitud arve klõpsamisel näeb klient oma Lightning-rakenduses arvet ja tal on võimalus see kohe maksta ja tehing lõpetada.

Kui näete kaupmehe seadmes Breez-rakenduses animatsiooni "Payment approved!", saate klõpsata printeri ikoonil, et genereerida kliendile kviitung. Kviitungiprinteri kasutamiseks Androidis proovige kasutada seda draiverit. Pange tähele, et saate printida ka varasemaid tehinguid läbi "Transactions" ekraani.

### Müügiaruanne

Oma müügi igapäevase/nädalase/kuise aruande vaatamiseks (raamatupidamise eesmärkidel või muul põhjusel) klõpsake ikoonil vasakus ülanurgas ja seejärel klõpsake "Transactions". Klõpsake aruande kuvamiseks aruande ikoonil ja valitud kuupäevavahemiku muutmiseks kalendri ikoonil.

### Tehingute Eksportimine

Breezis saadud maksete loendi vaatamiseks klõpsake ikoonil vasakus ülanurgas ja seejärel klõpsake "Transactions". Klõpsake paremal üleval asuvatel kolmel punktil ja seejärel "Export", et eksportida saabunud maksete loend CSV-vormingus. Loendi piiramiseks teatud ajavahemikuga klõpsake kalendri ikoonil, et määrata kuupäevavahemik.

### Kviitungite Printimine

Müügikviitungi printimiseks klõpsake maksekinnituse dialoogis paremal üleval printimise ikoonil. Või klõpsake ikoonil vasakus ülanurgas ja seejärel klõpsake "Transactions". Leidke printimiseks müük, avage see ja klõpsake paremal üleval printimise ikoonil.

> Märkus: kasutage selle draiveri abil printimiseks kaasaskantavat 58mm/80mm Bluetooth/USB termoprinterit.

## Tahan rohkem teada saada

- Lisateabe saamiseks Lightning'i ja Breezi kohta vaadake meie [blogi](https://breez.technology/blog).
- Rohkemate tehniliste näpunäidete saamiseks, kuidas rakendusest maksimumi võtta ja tavalisi toiminguid sooritada, vaadake meie [dokumentatsiooni](https://breez.technology/documentation).
- Kui jääte hätta ega leia vastust ühestki meie abimaterjalist, leiate meid [Telegramist](https://t.me/breez_labs) või saatke meile [e-kiri](mailto:support@breez.technology).
- Kui soovite näha mõningaid demonstratsioonivideosid Breez POS režiimi kasutamisest, mida on teinud meie fännid ja kasutajad, [siin](https://www.youtube.com/watch?v=xxxx) on üks suurepärane lühike video ja [siin](https://www.youtube.com/watch?v=xxxx) on pikem, üksikasjalikum video.