---
name: Kook Wallet
description: Tutorial Cake Wallet ja vaiksete maksete kohta
---

![cover](assets/cover.webp)


Selles juhendis uuritakse [**Cake Wallet**](https://cakewallet.com/): avatud lähtekoodiga, mittekaitstav, privaatsusele keskenduv mitme valuutaga wallet, mis on saadaval Androidile, iOSile, macOSile, Linuxile ja Windowsile. Sukeldume selle Bitcoin-spetsiifilistesse privaatsusfunktsioonidesse, käime läbi Bitcoin saatmise/vastuvõtmise **Silent Payments** (täiustatud on-chain privaatsusprotokoll) kaudu ja vaatame PayJoin v2 rakendamist asünkroonsete tehingute jaoks.


## 🎉 Peamised omadused



- [**Silent Payments (BIP-352)**](https://bips.dev/352/), millega parandatakse eelmist [BIP 47 maksekoode](https://silentpayments.xyz/docs/comparing-proposals/bip47/), mida nimetatakse ka "PayNyms", korduvkasutatavate varjatud aadressidega. Kui saatja kasutab teie Silent Payment'i aadressi, tuletab tema wallet eri võtmete abil unikaalse ühekordse aadressi, mis kombineeritakse unikaalseks ühekordseks Taproot aadressiks. Blockchaini kirjed näitavad omavahel mitteseotud tehinguid, takistades sissetulevate maksete seostamist. Silent Payments pakub mitmeid eeliseid, sealhulgas:
    - Korduvkasutatavad aadressid: Iga tehingu jaoks ei ole vaja generate uut aadressi, mis tagab parema kasutajakogemuse ja suurema privaatsuse
    - Kulude kasv on null: Vaikimisi maksed ei suurenda tehingute mahtu ega kulusid.
    - Tõhustatud anonüümsus: Välised vaatlejad ei saa siduda tehinguid Silent Paymenti aadressiga.
    - Ei nõuta saatja-vastuvõtja suhtlemist: Tehinguid saab teha ilma osapoolte vahelise suhtluseta.
    - Unikaalne aadress iga makse jaoks: Välja arvatud juhusliku aadressi korduvkasutamise oht.
    - Server ei ole vajalik: Vaikne makseid saab teha ilma spetsiaalse serverita.
- PayJoin v2** leevendab tehingugraafi analüüsi, ühendades saatjate ja vastuvõtjate sisendid üheks tehinguks. Kook Wallet rakendab kaks olulist edasiminekut:
    - Asünkroonsed tehingud**: Saatja ja vastuvõtja ei pea enam olema samaaegselt võrgus, et viia lõpule privaatne tehing.
    - Serverita side**: Kumbki pool ei pea käivitama Payjoin-serverit, mis kõrvaldab olulise tehnilise takistuse.
- Coin Control** võimaldab käsitsi UTXO valimist tehingute ajal. See hoiab ära aadresside juhusliku sidumise, kui kulutatakse mitu erineva päritoluga UTXOd.
- TOR** tugi, mis võimaldab kasutajatel suunata oma võrguliiklust läbi Tor-võrgu
- RBF** (Replace-By.Fee) võimaldab teil kohandada tasu pärast tehingu saatmist.


## 1️⃣ Wallet seadistamine


Cake Wallet pakub laiaulatuslikku platvormitoetust. Saate valida Androidi, iOS / macOS, Linuxi ja Windowsi vahel.  Alustamiseks külastage veebilehte https://docs.cakewallet.com/get-started/ ja valige oma operatsioonisüsteem.


![image](assets/en/01.webp)


Pärast paigaldamist määrake `PIN` (4- või 6-kohaline). Seejärel näete:


1. "Uue Wallet loomine" (uutele kasutajatele)

2. `Restore Wallet` (olemasolevate rahakottide puhul)


![image](assets/en/02.webp)


Järgmisel ekraanil saate valida paljude krüptovaluutade hulgast. Valige `Bitcoin` ja koputage `Järgmine` ning andke `Wallet nimi`, et tuvastada wallet. Koputades `Advanced Settings` ilmub rida `Privaatsusseadistusi`. Tehke need muudatused:



- Fiat API:** valige `Tor Only` (suunab hinnapäringud läbi Tori)
- Swap:** vali `Tor Only` (anonüümseks muudab andmevahetusliikluse)


Vaikimisi genereeritakse BIP-39 seed tüüpi, kusjuures on võimalus muuta Electrum seed tüüpi. Tuletamise teed on järgmised:



- Electrum: `m/0'`
- BIP-39: `m/84'/0'/0`


Kui soovite lisada täiendava turvakihi, võite luua `passphrase`.  passphrase peamine eesmärk on pakkuda täiendavat kaitset füüsiliste rünnakute vastu. Isegi kui ründaja leiab seed fraasi, ei pääse ta ilma õige passphrase-ga teie wallet-le ligi. Teisisõnu, seed fraas üksi kujutab endast ühte wallet, samas kui seed fraas koos passphrase-ga loob täiesti erineva wallet, millel puudub seos originaaliga. See funktsioon võimaldab ka "salajasi rahakotte", mis on kaitstud passphrase-ga, ja annab teile usutava eitamise võimaluse. Sundolukorras võite avaldada seed fraasi, hoides samal ajal suuremaid varasid turvaliselt passphrase-ga kaitstud wallet-s.


Kui teil on juba oma sõlme, lülitage "Lisa uus kohandatud sõlme" ja esitage oma "sõlme Address", et valideerida tehinguid ja plokke oma infrastruktuuris. Kui olete lõpetanud, koputage `Continue` ja `Next`, et luua oma wallet.


![image](assets/en/03.webp)


Järgmisel ekraanil kuvatakse lahtiütlemine:


```
On the next page you will see a series of words. This is your unique and private seed and it is the ONLY way to recover your wallet in case of lass or malfunction. It is YOUR responsibility to write it down and store it in a safe place outside of the Cake Wallet app.
```


![image](assets/en/04.webp)


Mnemofraasi salvestamise parimate tavade õppimiseks vaadake seda õpetust:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Puudutage valikut "Ma saan aru. Näita mulle oma seed` ja salvesta need sõnad turvalisse kohta! Seejärel koputage valikut "Kinnita seed" ja pärast kinnitamist "Ava Wallet".


## 2️⃣ Seadistused


Enne kui me sügavamale sukeldume, heidame pilgu "Avakuvale" ja "Seadistustele".


Avakuval näeme erinevaid kuvatud elemente:



- menüü `Hamburger` toob meid `seadete` juurde
- Vaba saldo
- Silent Payments Card, et alustada oma Silent Payment aadressile saadetud tehingute skaneerimist
- Payjoin kaart, et `Enable` Payjoin kui privaatsust säilitav ja tasu säästev funktsioon
- allosas on otseteed "Wallet ülevaade", "vastuvõtmine", "vahetamine" Bitcoin ja teiste valuutade vahel, "saatmine" ja "ostmine"


![image](assets/en/11.webp)


Koputades ikooni `Hamburgermenüü` avaneb seadete menüü. Vaatame valikud üle.


![image](assets/en/05.webp)


### A - ühendus ja sünkroonimine 🔗


Siin saame uuesti ühendada wallet, hallata sõlmi ja ühendada oma sõlme (soovitatav). `Silent Payments Scanning` võimaldab meil kohandada skaneerimist, määrates kas `Scan from block height` või `Scan from date`.


![image](assets/en/06.webp)


Alfa-funktsioonina on olemas ka võimalus lülitada sisseehitatud Tor, et suunata liiklus läbi Tor-võrgu.


### B - Vaiksete maksete seaded 🔈


Selle funktsiooni kuvamiseks saame lülitada sisse vaiksete maksete kaardi avakuval. Kui lülitate sisse funktsiooni "Always scanning", võimaldab wallet pidevalt jälgida plokiahelat sissetulevate vaikivate maksete suhtes. Me saame määrata skaneerimisparameetrid, et kohandada skaneerimisprotsessi vastavalt meie vajadustele, nagu eespool kirjeldatud.


![image](assets/en/07.webp)


### C - Turvalisus ja varundamine 🗝️


Meie wallet kindlustamiseks saame luua varukoopia, järgides rakendusesiseseid juhiseid. See tagab, et meil on turvaline koopia meie isiklikest võtmetest, mis võimaldab meil taastada wallet, kui see on kadunud või varastatud. Lisaks saame vaadata oma seed fraasi ja isiklikke võtmeid, muuta oma PIN-koodi, lubada biomeetrilist autentimist, allkirjastada / kinnitada ja seadistada 2FA lisakaitseks.


![image](assets/en/08.webp)


**Märkus**: Alates septembrist 2025 peab sõrmejälje biomeetriline autentimine Android-seadmetes toimima vähemalt 2. klassi biomeetrilise rakendusega, täpsemalt vt [siin](https://source.android.com/docs/security/features/biometric/measure#biometric-classes). See nõue võib siiski tulevikus muutuda.


### D - Privaatsusseaded 🔒


Samuti saame suurendada oma wallet turvalisust, kasutades Tor'i, et krüpteerida oma internetiühendus ja kaitsta oma privaatsust, kui pääseme ligi välistele allikatele. Lisaks saame vältida ekraanipilte, et hoida meie wallet andmed konfidentsiaalsetena, lubada automaatselt genereeritud aadresside loomist iga tehingu jaoks ja keelata ostu/müügitehingud, et vältida volitamata tehinguid. Lisaks saame `Enable PayJoin`, mis on veel üks privaatsusfunktsioon, mida vaatame hiljem läbi.


![image](assets/en/09.webp)


### E - Muud seaded 🔧


Muud seaded võimaldavad meil hallata tasu prioriteeti ja määrata tehingutele vaikimisi tasu taseme. See võimaldab meil kontrollida meie vaikivate maksetega seotud tehingutasusid, võttes arvesse võrgu praegust kasutust.


![image](assets/en/10.webp)


## 3️⃣ Saamine ₿itcoin kasutades Silent Payments


Bitcoin vastuvõtmiseks on saadaval mitu võimalust ja aadressitüüpi. *Segwit (P2WPKH)* (alates bc1q....)* on vaikimisi valik.  Valime selles näites `Silent Payments`.


Vaikiva makse vastuvõtmiseks puudutage esmalt Cake Wallet-s ikooni "Vastuvõtmine". Seejärel sisestage summa, mida ootate saada. Aadressi tüübi määramiseks koputage uuesti ekraani ülaosas `Receive` ja seejärel valige valikute hulgast `Silent Payments`.


Peakuval kuvatakse teie korduvkasutatav Silent Payment QR-kood ja aadress. Nagu oodata, on aadress üsna pikk:


`sp1qq0ryu780uwragyk06prxn29830a9csnl3wvr4as6fwh73rzn28zzcqmc6ve36vadllfztaa403ty9et0rlzup7kt55qh486gxzrde6y27c8s6x5p` .


![image](assets/en/12.webp)


Nüüd kasutage BIP-352 ühilduvat wallet (näiteks Blue Wallet), et skannida seda QR-koodi ja saata makse. Näete, et wallet tuletab teie vaikiva aadressi põhjal unikaalse sihtkoha aadressi.


![image](assets/en/13.webp)


## 4️⃣ Saatmine ₿itcoin kasutades Silent Payments


Kuna Blue Wallet saab ainult "saata" vaikimisi makseid, kasutame vastuvõtva osapoolena teist BIP 352 ühilduvat wallet. See protsess on identne tavalise Bitcoin tehinguga.



- Puudutage avakuval valikut "Saada"
- kas kleepides meie korduvkasutatava `sp1qq...` aadressi või skaneerides QR-koodi otse rakenduses.
- Valige, kui palju soovite oma olemasolevast saldost kulutada
- Tehingu kinnitamiseks puudutage ekraani allosas nuppu "Saada"


Kui oleme sisestanud `sp1qq...` aadressi, tuletab wallet automaatselt taustal vastava `bc1p...` Taproot aadressi (P2TR), mida kasutatakse vaikiva makse tegemiseks.


Meil on võimalus kirjutada iga tehingu kohta sisemine märkus, kohandada tasu seadeid või valida tehingu jaoks teatud UTXO-d, kasutades funktsiooni `Coin Control`.


![image](assets/en/14.webp)


tehingu kinnitamiseks pühkige paremale.


Kui olete tehingu saatnud, küsitakse, kas soovite selle kontakti oma aadressiraamatusse lisada.


![image](assets/en/15.webp)


## 5️⃣ PayJoin


Vaatame üle, mis on PayJoin [umbes] (https://docs.cakewallet.com/cryptos/bitcoin/#payjoin):


_Payjoin v2 on Bitcoin privaatsust säilitav ja tasu säästev funktsioon, mis võimaldab tehingu saatjal ja saajal teha koostööd, et luua üks tehing. Sellisel tehingul on sisendid nii saatjalt kui ka saajalt, mis murrab Bitcoin vastu suunatud kõige levinumad jälgimismeetodid ning võimaldab mõnes olukorras ka paremat skaalumist ja tasude kokkuhoidu _


PayJoin kohta saate rohkem teada ka järgmisest juhendmaterjalist.


https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

PayJoin kasutamiseks on mõlemal poolel vaja PayJoin-ga ühilduvat wallet ja vastuvõtjal peab olema vähemalt üks münt või väljund oma wallet-s. Alustamiseks järgige järgmisi samme:


1. Koputage menüüs "Hamburgeri menüü" ja seejärel nuppu "Privaatsus"

2. Lülita ümber valik "Kasuta Payjoin"

3.  Koputage Avakuval nuppu "Vastuvõtmine" ja teile kuvatakse PayJoin QR-kood ja kopeerimisnupp (kui on valitud Segwit)


![image](assets/en/16.webp)


## 6️⃣ Muud omadused


On mitmeid muid funktsioone, nagu mitme valuuta vahetamine, ostu- ja müügivõimalused erinevate müüjate ühendustega ja Cake-spetsiifilised programmid nagu "Cake Pay", mis võimaldab teil osta ettemakstud kaarte või kinkekaarte.


![image](assets/en/17.webp)


## 🎯 Kokkuvõte


See on meie ülevaade Cake Wallet kohta, mis pakub praktilist Bitcoin privaatsust tänu sellistele funktsioonidele nagu Silent Payments (BIP-352) ja Payjoin v2.


Silent Payments asendab ühekordsed aadressid korduvkasutatavate varjatud aadressidega, et vältida on-chain seoseid sissetulevate tehingute vahel. Kuigi eelmiste versioonide sünkroonimisprobleemid on märkimisväärselt paranenud, on Silent Payments'i skaneerimiseks ja tuvastamiseks vajalikud arvutuslikud nõuded suurenenud, mis nõuavad rohkem ressursse ja ribalaiust.


Payjoin v2 katkestab ahela analüüsi, ühendades saatja ja vastuvõtja sisendid ühtseteks tehinguteks ilma lisatasudeta või keskse koordineerimiseta. See rikub ühise sisendi omandiõiguse heuristikat, mis on oluline eelis, kuna see tähendab, et te ei saa eeldada, et kõik sisendid kuuluvad saatjale.


Kasutajate jaoks, kellele on oluline rahaline anonüümsus, on Cake Wallet elujõuline valik. See sisaldab privaatsusprotokolle otse oma põhifunktsiooni, muutes need kättesaadavaks ilma tehnilise keerukuseta. Kuna järelevalve avalike plokiahelate üle suureneb, aitavad sellised vahendid nagu see aidata säilitada tehingu privaatsust seal, kus see on kõige olulisem. Nende standardite laiem rakendamine wallet maastikul oleks tervitatav areng.


## 📚 Ressursid


https://cakewallet.com


https://docs.cakewallet.com/


https://github.com/cake-tech/cake_wallet


https://blog.cakewallet.com/


[https://silentpayments.xyz/](https://silentpayments.xyz/)


[ttps://bips.dev/352/](https://bips.dev/352/)


https://payjoin.org/