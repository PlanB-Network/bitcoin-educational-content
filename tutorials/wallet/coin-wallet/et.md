---
name: Coin Wallet
description: Coin Wallet ja viisid eraelu puutumatuse ja turvalisuse suurendamiseks
---

![cover](assets/cover.webp)


See õpetus käsitleb [Coin Wallet](https://coin.space/) - isekaitstavat krüpto wallet mobiilseadmete jaoks ning seda, kuidas suurendada turvalisust ja privaatsust wallet mobiilirakenduste kasutamisel.



## Coin Wallet kohta


**Coin Wallet** on avatud lähtekoodiga wallet, mis on loodud Bitcoin entusiastide meeskonna poolt 2015. aastal. See algas veebirakendusena, millele järgnes 2017. aastal iOSi rakendus ja 2020. aastal Android-rakendus - saadaval Google Play, Samsung Galaxy Store ja Huawei AppGallery.


Peamised eelised:


- Mittekaitstav arhitektuur
- Täielikult [avatud lähtekoodiga](https://github.com/CoinSpace/CoinSpace/blob/master/LICENSE)
- Lihtne ja puhas disain
- Keskendub põhieesmärgile - krüptoraha turvaline säilitamine, ilma ebavajalike funktsioonideta
- Platvormiülene tugi: mobiilne (iOS ja Android), töölauaarvuti, veebi
- RBF (Replace-By-Fee) tugi - kiirendada kinni jäänud tehinguid igal ajal
- Riistvaraline 2FA koos [YubiKey](https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/) / FIDO2 võtmega
- Sisseehitatud Tor-tugi - suunake kogu liiklus läbi Tor-võrgu maksimaalse privaatsuse tagamiseks



## 1️⃣ Coin paigaldamine Wallet

Coin Wallet on saadaval kõigil suurematel platvormidel.



- [iOS App Store](https://apps.apple.com/app/coin-wallet-bitcoin-crypto/id980719434)



- [Android Google Play](https://play.google.com/store/apps/details?id=com.coinspace.app)



- [Android (Galaxy Store)](https://galaxystore.samsung.com/detail/com.coinspace.app)



- [Android (Huawei AppGallery)](https://appgallery.huawei.com/app/C112183767)



- [Android (Uptodown)](https://coin-wallet.en.uptodown.com/android)



- [Android APK](https://coin.space/api/v3/download/android-apk/any)



- [Kõik väljalaske lingid](https://github.com/CoinSpace/CoinSpace/releases)


Saadaval ka töölauale (Windows, Linux, macOS), veebirakendusena ja Tori kaudu.


![image](assets/en/01.webp)


## 2️⃣ Wallet loomine ja PIN-koodi määramine


wallet luuakse, kasutades passphrase - juhuslikku järjestust, mis koosneb 12 sõnast, mis on eraldatud tühikutega ja genereeritud [2048 sõnast koosnevast loendist](https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts).

Coin Wallet toetab 12-, 15-, 18-, 21- või 24-sõnalist parooli, mis on imporditud teistest rahakottidest.


passphrase on inimese poolt loetav eravõti. See tuleb turvaliselt salvestada. passphrase on kõik, mida on vaja wallet-le juurdepääsuks või selle taastamiseks. Kui passphrase kaob, on wallet ja kõik vahendid lõplikult kadunud. passphrase ei tohi kunagi jagada. Coin Wallet ei salvesta võtmeid üheski serveris ega andmebaasis.


**Kas 12-sõnaline passphrase on turvaline?**

2048 võimaliku sõnaga ühe positsiooni kohta on 2048¹² ≈ 10³⁹ kombinatsiooni, mis annab ~128 bitti turvalisust, mis on võrreldav Bitcoin privaatvõtmega. Seda taset peetakse üldiselt piisavaks.


![image](assets/en/02.webp)


Pärast passphrase üleskirjutamist ja kinnitamist palub rakendus määrata **4-kohaline PIN-kood** igapäevaseks juurdepääsuks. Täiendava mugavuse tagamiseks saate PIN-koodi asemel lubada biomeetrilist autentimist (sõrmejälg või näotuvastus).


![image](assets/en/03.webp)



Ei ole kontot, võtme taastamist, passphrase lähtestamist ega tehingu tühistamist. Turvalisuse eest vastutab täielikult kasutaja.


Üksikasjalikud parimad tavad mälulause salvestamiseks:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 3️⃣ Salasõna + PIN-kood. Millal ja kuidas neid kasutatakse


**Millal on passphrase nõutav?**

Ainult nendel harvadel juhtudel:


- wallet seadistamine uues seadmes
- Coin Wallet rakenduse uuesti paigaldamine
- Rakenduse/brauseri andmete kustutamine (kohalik salvestusruum)
- Riistvara võtme eemaldamine kontolt
- Vale PIN-koodi sisestamine kolm korda (rakendus lukustab turvalisuse tagamiseks)


Igapäevases kasutuses piisab wallet lukustuse avamiseks neljakohalisest PIN-koodist.


**Passfraas + PIN: kuidas see toimib**

passphrase on tõeline peamine privaatne võti ja töötab igas seadmes.

Kuna iga kord 12-24 sõna sisestamine oleks ebamugav, kasutab Coin Wallet neljakohalist PIN-koodi kiireks igapäevaseks juurdepääsuks praegusele seadmele.

Lihtne PIN-kood üksi ei ole piisavalt turvaline, et kaitsta otse peavõti, seega ei kasutata seda kunagi krüpteerimiseks. Selle asemel:



- PIN-kood saadetakse serverisse ja vahetatakse pika krüptograafilise token vastu.
- See token dekrüpteerib ainult seadmes salvestatud krüpteeritud üldvõtme.


Kui PIN-kood sisestatakse kolm korda valesti, kustutab server token lõplikult. Kohalikult salvestatud võti muutub kasutuskõlbmatuks ja ainus viis wallet taastamiseks on sisestada originaal passphrase.

Selline konstruktsioon tagab nii mugavuse kui ka tugeva tagavarakaitse.



## 4️⃣ Vastuvõtmine ₿itcoin - Address tüübid ja privaatsus


Coin Wallet toetab kõiki kolme Bitcoin aadressiformaati:



- Native SegWit (Bech32)** - algab tähega **bc1q** - madalaim tasu, soovitatav
- Sisestatud SegWit (P2SH)** - algab numbriga **3**
- Legacy (P2PKH)** - algab numbriga **1**


![image](assets/en/04.webp)


**Miks muutub aadress pärast iga sissemakse tegemist?**

See on tahtlik ja kaitseb eraelu puutumatust. Iga kord, kui münte saadakse, genereerib Coin Wallet automaatselt uue kasutamata aadressi. Kui sama aadressi kasutataks uuesti (näiteks igakuise palga puhul), saaks igaüks hõlpsasti kõik sissetulevad tehingud plokiahela uurija abil kokku lugeda ja teada kogutulu.


Vanad aadressid jäävad igavesti kehtima - te võite neile endiselt vastu võtta -, kuid iga kord uue aadressi kasutamine on soovitatav parim privaatsustava.


**Kuidas saada Bitcoin:**

1. Avage münt

2. Puudutage valikut **Võta vastu**

3. Valige soovitud aadressitüüp (eelistatavalt **bc1q** - `Native SegWit`)

4. Näidake QR-koodi või kopeerige aadress ja saatke see maksjale


**Võimalik - Mecto (isiklike maksete puhul):**

Samal vastuvõtuekraanil on nupp "Mecto".

Kui lülitate selle sisse:


- Teil palutakse sisestada **nickname** (gravatar)
- Teie praegune asukoht + vastuvõtuaadress jagatakse ajutiselt teiste Coin Wallet kasutajatega, kellel on samuti Mecto aktiveeritud
- Nad saavad teid väikesel kaardil avastada ja saata münte ilma trükkimata või skaneerimata


Andmed on nähtavad ainult teistele Mecto kasutajatele ja need kustutatakse automaatselt 1 tunni pärast (või kohe, kui lülitate selle välja).

Mecto on täiesti vabatahtlik - jätke see välja, kui soovite maksimaalset privaatsust.


![image](assets/en/05.webp)


## 5️⃣ Saatmine ₿itcoin


Bitcoin saatmiseks:


1. Avage münt → koputage valikut **Saatmine**

2. Sisestage aadress või skannige QR-kood

3. Sisestage summa (või koputage **Max**)

4. Valige tehingu kiirus:



| Kiirus   | Ligikaudne kinnitusaeg | Tasude tase     |
|---------|---------------------------|---------------|
| **Aeglane**    | ~120 minutit              | Madalaim
| **Vaikimisi** | ~60 minutit               | Keskmise
| **Kiire**    | ~20 minutit               | Kõrgem

5. Kinnitage oma 4-kohaline PIN-kood → tehing on eetrisse saadetud


### Kuidas kiirendada pooleliolevat ₿itcoin-tehingut (RBF)


Kui valisid aeglase tasu ja tehing on kinni:


1. Mine vahekaardile **History**

2. Puudutage ootel olevat tehingut

3. Koputage **Kiirenda** (asendamine tasu eest)

4. Kinnita → tehing edastatakse uuesti kõrgema tasuga


RBF kiirendus on praegu toetatud järgmistel juhtudel:

Bitcoin - Avalanche - Binance Smart Chain - Ethereum - Ethereum Classic - Polygon


Lisateave Replace-by-fee (RBF) kohta: https://bitcoinops.org/en/topics/replace-by-fee/


## 6️⃣ Privaatsete võtmete eksportimine


**Millal on tegelikult vaja privaatvõtit?**

(99 % kasutajatest ei tee seda kunagi - 12-sõnalisest passphrase-st piisab)



| Olukord                                      | Miks teil on vaja privaatset võtit                     |
|------------------------------------------------|--------------------------------------------------|
| Vana paberrahahoidla puhastamine                   | Vahendite teisaldamine praegusesse rahakotti             |
| Riistvara allkirjastajale importimine (nt Coldcard) | Võrguühenduseta allkirjastamiseks                              |
| Hädaolukorras taastamine (kadunud seeme, kuid rakendus on endiselt avatud) | Müntide päästmine enne rakenduse kadumist           |
| Tööriistade kasutamine, mis ei aktsepteeri seemefraase     | Mõned ainult jälgimisvõi allkirjastamise utiliidid             |

### Kuidas eksportida privaatseid võtmeid Coin Wallet abil


1. Avatud **Bitcoin (BTC)**

2. Kerige lehe lõppu - koputage valikut **Eraldi võtmete eksportimine**

3. Rakendus näitab iga aadressi koos saldoga + selle privaatne võti **WIF**-vormingus (algab 5, K või L) ja QR-koodiga.


Ilmuvad ainult mitte-tühjad aadressid.


**Näide WIF-võtme**

`L2v1eK4i9j3k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k`


**Mida teha edasi (soovitatav)**


- Avage Electrum, Sparrow, BlueWallet või mis tahes riistvara wallet
- Impordi/pühkige privaatne võti
- Kõik rahalised vahendid liiguvad koheselt uuele turvalisele aadressile teie praeguse seed all


Ärge kunagi salvestage privaatvõtit digitaalselt lihtkirjana. Pärast pühkimist saab selle turvaliselt kustutada.


Täielik juhend privaatvõtmete ja tuletamisviiside kohta: [Kuidas töötada privaatvõtmetega: Ülim juhend](https://coin.space/how-to-work-with-private-keys-the-ultimate-guide/)



## 7️⃣ Tehnilised üksikasjad - BIP39, BIP32 ja tuletatud teed


Coin Wallet järgib rangelt ametlikke Bitcoin standardeid, mida kasutavad peaaegu kõik tõsised rahakotid.


"BIP39" - kuidas passphrase muutub peamiseks privaatvõtmeks


- Vaikimisi sõnade arv: 12
- Vabatahtlik passphrase/parool: ei ole ("")
- Algne entroopia: 128 bitti (12 sõna) → 256 bitti (24 sõna)
- Avatud lähtekoodiga rakendamine: https://github.com/paulmillr/scure-bip39
- Sõnade nimekiri: 2048 sõnast koosnev standardne ingliskeelne sõnade nimekiri
- Toetab 12-, 15-, 18-, 21- ja 24-sõnaliste fraaside importimist mis tahes teisest BIP39 wallet-st


"BIP32 + BIP44/BIP49/BIP84" - kõigi aadresside deterministlik genereerimine

wallet saab generate ühe peavõti abil miljardeid aadresse rangelt määratletud järjekorras. Seetõttu näitavad samad 12 sõna, mis on sisestatud Electrum, Sparrow, Trezorisse, Ledger, BlueWalletisse jne, täpselt samu aadresse ja saldosid.





**Coin Wallet-is Bitcoini jaoks kasutatavad tuletamise teed**

| Aadressi tüüp              | Standard | Tuletamise tee       | Algab | Kommentaar                              |
|---------------------------|----------|-----------------------|-------------|--------------------------------------|
| Omandolik SegWit (Bech32)    | BIP84    | `m/84'/0'/0'`         | bc1q…       | Kaasaegne vorming, madalaim tasu           |
| Pesastatud SegWit (P2SH)      | BIP49    | `m/49'/0'/0'`         | 3…          | Ühilduvusumbrella vanale teenuste jaoks |
| Pärand (P2PKH)            | BIP44    | `m/44'/0'/0'`         | 1…          | Vanin vorming, kõrgeim tasu          |

Iga tee sees:


- `/0` - väline ahel (aadressid, mida näitate maksete vastuvõtmiseks)
- `/1` - sisemine ahel (wallet enda poolt kasutatavate aadresside muutmine)


Kuna Coin Wallet järgib neid avalikke standardeid ilma muudatusteta, jäävad teie rahalised vahendid tagastatavaks mis tahes muus ühilduvas wallet-s isegi 10-20-30 aasta pärast.


## 8️⃣ Anonüümsuse suurendamine Toriga


**Miks kasutada Tori Coin Wallet**

Tor peidab teie tegeliku IP-aadressi Bitcoin sõlmede, vahetuste ja vaatlejate eest.

Kogu liiklus (saldod, tehingud, vahetused) käib läbi Tori võrgu - ei mingeid otseseid ühendusi, ei mingeid IP-lekkeid.

Seda rakendatakse otse rakenduse lähtekoodis (vt [.env configuration](https://github.com/CoinSpace/CoinSpace/blob/master/web/.env#L31)).


Coin Wallet-l on varjatud .onion-aadress ja alates versioonist 6.6.3 (detsember 2024) on **sisseehitatud Tor-tugi otse mobiilirakenduses**.


### Kuidas aktiveerida Tor Androidis ja iOSis


1. **Installi Orbot** - ametlik Tor Project rakendus (tasuta)


   - Android → [Google Play](https://play.google.com/store/apps/details?id=org.torproject.android) / [F-Droid](https://orbot.app/en/)
   - iPhone / iPad → [App Store](https://apps.apple.com/us/app/orbot/id1609461599)


2. **Avaneb Orbot → koputage nuppu Start**

Valige nimekirjast **Coin Wallet**, et ainult wallet kasutaks Tori (valikuline, kuid soovitatav)

Oodake, kuni kuvatakse **"Ühendatud "** (10-30 sekundit)


3. **Avaneb Coin Wallet → Seaded → Võrk**

Lülitage sisse **Kasutage Tor**


4. **Kontrollige staatust**

Ülemisele ribale ilmub **lilla Tor sibula ikoon** → kogu liiklus suunatakse nüüd läbi Tor'i


![image](assets/en/06.webp)


See ongi kõik - teie mobiil Coin Wallet on täiesti anonüümne.


Naudi privaatset krüptohaldust!


## 📝 Kokkuvõte


[Coin Wallet](https://coin.space/) - üks tõelisi Bitcoin wallet pioneere, millel on 10-aastane arendusajalugu.

See on teadlikult lihtne ja keskendub oma põhiülesandele: teie krüptoraha turvalisele säilitamisele.

Ei ole reklaami, uudisvoogu, tellimusi, sotsiaalseid funktsioone ega segavaid tegureid - lihtsalt puhas, kiire, isetoimiv wallet, mis teeb täpselt seda, mida ta tegema peab.

Coin Wallet seab lihtsuse ja turvalisuse esikohale - on alati olnud ja jääb alati.


## 📖 Ressursid


https://coin.space/


https://support.coin.space/hc/en-us


https://en.bitcoin.it/wiki/Wallet


https://bitcoinops.org/


https://github.com/CoinSpace/CoinSpace/


https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/


https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts


https://github.com/paulmillr/scure-bip39