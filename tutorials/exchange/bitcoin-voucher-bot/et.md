---
name: BitcoinVoucherBot
description: Telegram bot, et osta Bitcoin konfidentsiaalselt
---
![image](assets/cover.webp)

_Selle õpetuse on kirjutanud_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)

# Sissejuhatus

BitcoinVoucherBot on vahend, mille abil saab Exchange-s Bitcoine osta eurode eest.

### KYC Light

Eurode muutmine Bitcoin jaoks on esimene ja kõige põhilisem samm selle teema uurimise alustamiseks, kuid ilmselt on see ka kõige raskem ja keerulisem. Võimalusi võib olla palju: Bitcoin pakkumine tsentraliseeritud vahetuste, Bitcoin-teemaliste kohtumiste, sõprade, tuttavate ja muu kaudu. Me liitume Bitcoineri kogukonnaga ja **soovitame tingimata tsentraliseeritud Exchanges** kasutamist, et tagada rohkem tähelepanu oma privaatsusele.

Kuigi see valik võib olla vähem mugav, on oluline mõista, et börsid rakendavad "tunne oma klienti" (KYC) määrust, määrates seega igale neilt ostetud Satoshi-le nii identiteedi kui ka füüsilise asukoha. "Mugavusel" on mõned silmatorkavad kõrvalmõjud.

### Kuidas seda teha?

Siin tuleb [BitcoinVoucherBot:](https://t.me/BitcoinVoucherBot) teenus, Telegram bot, mis toimib kanalina meie SEPA ülekannete ja Sats ostude vahel.

### Eeltingimused

BitcoinVoucherBot'i kasutamise alustamiseks ei ole vaja Bot'i töötajatele delikaatseid isikuandmeid avaldada. **Es ei ole vaja autoriseerimist**.

Vaja on vaid juba aktiivset Telegram-kontot ja pangakontot. **Märkus**: Poste Italiane (Itaalia klientide jaoks) avatud konto või üldisemalt laetavale kaardile viitamine ei sobi.

Telegrami vestluses koostame tellimuse, maksame selle eest pangaülekandega ja lõpuks saame boti kaudu ostuobjekti mitte tundva kolmanda osapoole ettevõtte poolt väljastatud vautšeri.

### Boti aktiveerimine ja menüü

Aktiveerimine on lihtne ühekordne toiming. Otsige Telegramist _@BitcoinVoucherBot_ ja niipea, kui jõuate Bot'i vestlusesse, paistab alt suur _Start/Start_ nupp. Operatsioon põhjustab Bot'i reageerimise, mis esitab talle kättesaadavate peamiste käskude menüü. Samuti ilmuvad esimesed tervitussõnumid, mida soovitame hoolikalt lugeda.

**Hoiatus**: on mitmeid pettureid, kes esinevad originaalse VoucherBot'ina. Kui te ei ole kindel, et otsing Telegrami kaudu, palun pääseda BitcoinVoucherBot link [ametlikul kodulehel](https://www.bitcoinvoucherbot.com/)

![image](assets/it/01.webp)

Valikud ilmuvad, kui klõpsate vasakus alumises nurgas olevale nupule _Menu_: võite klõpsata käsule vastaval sõnal või sisestada sõnumikasti kaldkriipsu `/`, millele järgneb sisestatud käsk.

![image](assets/it/02.webp)

Peamised tegevused hõlmavad:


- _/purchase_: on tegelik ostumenetlus. Kui tehing on lõpule viidud, genereerib robot automaatselt QR-koodi, mis on valmis lunastamiseks.
- _/refill_: selle õpetuse kirjutamise ajal saadaval, kuid me ei käsitle seda, sest tehnilistel põhjustel võidakse see võimalus hiljem eemaldada.
- _/swap_: avab swap-protseduuri, mis on saadaval kas mugava Telegram-boti või veebi kaudu.
- _/ap_: akumulatsiooniplaan, mis võimaldab teil luua **Konstantse akumulatsiooniplaani (CAP)**.
- _/lnaddress_: millega meil palutakse siduda oma LN Address, konkreetse protseduuri jaoks, mida näeme hiljem.
- _/credits_: kontrollida, kui palju krediiti on jäänud generate vautšerite jaoks.
- _/myorders_: näitab botiga tehtud tellimusi (**Hoiatus** süsteem jälgib ainult viimased 10 tehtud tellimust, mitte kogu ajalugu).
- _/fees_: käsk võrgutasude kontrollimiseks. Nende hindamiseks on alati kõige parem tugineda Mempool.space'ile.
- _/support_: vajaduse korral avanevad kontaktid, et teatada probleemidest tugimeeskonnale.

# Bitcoin ostumenetlus

## Tellimuse ettevalmistamine

Klõpsake käsurea menüüs _/osta_

![image](assets/it/03.webp)

Ilmub mitmeid võimalusi, kuid me valime _BTC Vouchers_

![image](assets/it/04.webp)

BitcoinVoucherBot võimaldab teil osta Bitcoin onchain, Lightning ja Liquid.

Selles etapis vali _Onchain & Lightning 🔗⚡️_

![image](assets/it/05.webp)

Ekraan muutub kiiresti ja VoucherBot pakub välja ostunimetused. Need algavad minimaalselt 100,00 eurost kuni 900,00 euroni.

Esimese ostu puhul pakutakse ainult 100,00 €, Onchain ja Lightning nimiväärtusi. Konfidentsiaalsuse suurendamiseks soovitame valida _Lightning ⚡️_

![image](assets/it/06.webp)

VoucherBot teavitab meid, et esimene valik on tehtud ja et selle kinnitamiseks tuleb valida _Proceed_

![image](assets/it/07.webp)

Nüüd on vaja valida makseviis. Ülekanne tehakse ülekandega **(aktsepteeritakse ainult SEPA) **. VoucherBot pakub vastuvõtjaks ettevõtet, mis pakub kahte pangakontot, üks Ühendkuningriigis ja teine Šveitsis. Selle õpetuse läbiviimiseks valiti Šveitsi pank

![image](assets/it/08.webp)

Siinkohal palutakse meil sisestada oma IBAN, millest algab ülekanne valitud panka. See teave läheb pusle koostamiseks, mis võimaldab botil, s.t. masinal, panna kokku mõned andmed, et ostuprotsess kulgeks ilma inimese sekkumiseta.

IBAN tuleb kirjutada sõnumiribale, kontrollida ja saata botile.

![image](assets/it/09.webp)

Nüüd ilmub VoucherBotiga vestluses kontrollteade.

Kui kõik on õige, jätkake, klõpsates nuppu _Proceed_.

![image](assets/it/10.webp)

## Maksmine

Pärast mõne hetke möödumist, mis on vajalik andmete töötlemiseks, vastab VoucherBot sõnumiga, mis sisaldab kõiki tellimuse täitmiseks vajalikke andmeid. Sõltuvalt sellest, mida teie pank nõuab, on asjakohane teave:


- "IBAN", mis on oluline hoiuse tegemiseks, samuti saaja Address;
- "valitud summa" eelnevalt läbi cutoff, mis peab olema täidetud, et VoucherBot saaks makse laekumisel tellimuse ära tunda;
- `Makse põhjus`, mis on makse põhjus. **Tuleb kopeerida ja kleepida ilma midagi eemaldamata või lisamata oma ülekande vastavasse lahtrisse. Kõik maksmise põhjuses olevad "." või "-" võib asendada "valge tühikuga "**.
- unikaalne `OrderID`, millele viidata abi taotlemisel.

Seejärel saate jätkata maksmist rakenduse või panga kaudu. Kui pank on makse heaks kiitnud, on oluline meeles pidada, et vajutate VoucherBotiga vestluses _Makse teatamine_. See lihtne toiming annab teile märku, et makse on teel.

![image](assets/it/11.webp)

VoucherBot vastab sõnumiga, mis sisaldab väga olulist hoiatust: **ei kustuta vestlust**, vähemalt kuni vautšeri kättesaamiseni, sest see on ainus vahend tellimuse taastamiseks ja selle jätkamiseks.

![image](assets/it/12.webp)

---
Palun võtke arvesse:


- aktsepteeritakse ainult SEPA ülekandeid;
- ooteajad on seotud üksnes sellega, kuidas pangad (mis ei tööta 24/7/365 nagu Bitcoin) vautšerit töötlevad. Vautšeri saamine võib võtta paar tundi kuni 3 tööpäeva;
- mis tahes vajaduste korral on Bitcoin VoucherBotil suurepärane [tugi](https://t.me/BitcoinVoucherGroup) teenus Telegramis.

---
## Lunastus

Niipea kui makse on edukas, saadab Bitcoin VoucherBot vautšeri otse vestlusesse. Välkvautšer on QR-koodi kujul, mis on trükitud oranžile taustale.

![image](assets/it/31.webp)

Seal on kõik vajalikud andmed, et seda sisse nõuda:


- summa Sats-s, mis vastab ülekandega saadetud summale, välja arvatud teenus- ja võrgutasud;
- vautšeri viite ID;
- kuupäev, millal vautšer tuleb lunastada, vastasel juhul lähevad vahendid kaduma, st 25 päeva pärast väljastamise kuupäeva.

Voucheri saate sisse maksta, kui kujundate QR-koodi ühilduva Wallet Lightning Network skaneerimisfunktsiooniga või LNURL-i kaudu, mis on samuti QR-koodi all näidatud.

Selle õpetuse jaoks kasutasime Wallet Of Satoshi, kasutades skaneerimisfunktsiooni, mis on aktiveeritud klahviga _Send_

![image](assets/it/32.webp)

Kui mobiiltelefoni kaamera on aktiveeritud, raamige QR-koodi vestluses, avades Telegrami arvutist

![image](assets/it/34.webp)

Enne jätkamist, Wallet Of Satoshi alates kontrolli ekraani, mis sisaldab summa, mis täpselt vastab summa väljendatud vautšeri ja, nagu kirjeldus, BitcoinVoucherBot. Vautšeri väljamaksmiseks klõpsake lihtsalt nuppu _Receive_

![image](assets/it/35.webp)

Wallet Satoshi protsessid mõne hetke jooksul

![image](assets/it/36.webp)

ja lõpuks teatatakse kogumisest ja see on kohe kättesaadav Wallet bilansis.

**Wallet Satoshi on eestkostetav rakendus: kohe pärast vautšeri lunastamist on soovitav Sats üle viia Wallet mitte-eestkostetavaks.**

![image](assets/it/37.webp)

### Kuidas lunastada onchain vautšer

Nagu me nägime tellimuse ettevalmistamisel, võimaldab VoucherBot osta Sats otse onchain, valides samanimelise vautšeri.

**Märkus**: Tellimuse ettevalmistamine ja maksmine ei muutu, need on alati samad. Muutub vaid see, kuidas onchain-vutšer lunastatakse.

Pärast tellimuse lõpetamist, makse sooritamist, vajutades _Makse teatamine_ ja oodates pankade tehnilist aega ülekande tegemiseks, vastab VoucherBot, saates vautšeri otse vestlusesse.

See vautšer on samuti QR-koodi kujul, kuid põhivärv on kanariakollane ja - mis kõige tähtsam - kirjelduses on hästi selgitatud, et tegemist on ahelas oleva vautšeriga, mille te lunastate otse oma Wallet ahelas ja väljamaksmise alustamiseks peate klõpsama lingil _Redem on Telegram_. Onchaini vautšer sisaldab ka juba nähtud teavet välklambi kohta:


- summa Sats-s, mis vastab ülekandega saadetud summale, välja arvatud teenus- ja võrgutasud;
- vautšeri kood;
- vautšeri viite ID;
- kuupäev, millal vautšer tuleb lunastada, vastasel juhul lähevad vahendid kaduma, st 25 päeva pärast väljastamise kuupäeva.

![image](assets/it/22.webp)

**Hoiatus ⚠️:** klõpsates nagu selgitatud, avaneb teise bot'i hüpikaken: **Voucher RedeemBot.**

Voucher RedeemBot on vahend, mis on tehtud kättesaadavaks selleks otstarbeks. Olenemata sellest, kas tegemist on esimese kasutamisega või on olemas varasemad tellimused, tuleb iga kord, kui tehakse uus lunastus, alati vajutada _START_.

![image](assets/it/23.webp)

Sel hetkel laeb RedeemBot ahelas oleva vautšeri, mis on hõlpsasti äratuntav vautšeri koodi ja viite ID järgi. Samuti avab see riba sõnumite kirjutamiseks ja botiga vestluse alustamiseks, mis tegelikult kutsub meid üles ütlema talle onchain Address meie Wallet.

**Märkus**: See Address peab olema SegWit tüüpi.

![image](assets/it/24.webp)

Me avame oma Wallet sel hetkel ja generate SegWit Address

![image](assets/it/25.webp)

me kopeerime seda

![image](assets/it/26.webp)

ja kleepige see vestlusesse RedeemBotiga

![image](assets/it/27.webp)

Meil on nüüd kontrolliekraan, et kontrollida, kas vautšeri kood on õige, samuti Address, mille me oleme edastanud RedeemBotile. Kontrollime seda hästi, sest klikkides _Proceed_, käivitub tehing ja seda ei ole võimalik uuesti leida, kui oleme näiteks edastanud vale Address.

![image](assets/it/28.webp)

Tehing on alanud ja seega lõpeb Redeem protseduur onchain vautšeri puhul.

![image](assets/it/29.webp)

samas kui summa on näha meie Wallet ajaloos.

![image](assets/it/30.webp)