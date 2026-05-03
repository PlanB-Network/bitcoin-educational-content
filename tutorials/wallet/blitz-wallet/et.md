---
name: Blitz Wallet
description: Kõige lihtsam Bitcoin'i rahakott.
---

![cover](assets/cover.webp)

Kasutajakogemus on Bitcoin'i rahakoti valimisel üks otsustavaid tegureid. Selles õpetuses tutvustame teile Blitz Wallet'it -- rahakotti, mis seab lihtsuse oma lähenemise keskmesse: tänu **Spark** protokolli integreerimisele pakub Blitz teile üht kõige lihtsamat ja terviklikumat Bitcoin'i rahakotti turul, kiirete maksetega ja ilma tehnilise haldamiseta.

## Mis on Blitz Wallet?

Blitz Wallet on **self-custodial** ja **open source** Bitcoin'i rahakott, mis panustab teie suveräänsusele ning sujuvale ja intuitiivsele kasutajakogemusele.

[Blitz Wallet](https://blitz-wallet.com/) on mobiilirakendus, mis on saadaval Androidis (Play Store) ja iOS-is (App Store).

Erinevalt traditsioonilistest Lightning'i rahakottidest, mis nõuavad maksekanalite ja sissetuleva likviidsuse haldamist, toetub Blitz Wallet **Spark protokollile**, et need tehnilised keerukused kõrvaldada. Tulemus: kohesed maksed alates esimesest saadud satoshist, ilma igasuguse eelneva seadistamiseta. Blitzi eesmärk on muuta bitcoin'iga maksmine sama lihtsaks kui tavalise makserakendusega, ilma kunagi teie vahendite self-custody't ohtu seadmata.

Blitz Wallet toetab samuti **loetavaid aadresse** formaadis `kasutaja@domeen.com` (LNURL kaudu), mis võimaldab saata bitcoine sama lihtsalt kui e-kirja, ilma et peaksite iga tehingu jaoks pikki invoice'id või QR code'e käsitlema.

## Spark protokolli mõistmine

Enne praktilise osa juurde asumist on kasulik mõista tehnoloogiat, mis paneb Blitz Wallet'i kapoti all tööle: **Spark protokoll**.

### Mis on Spark?

Spark on open source ülemkihi protokoll, mis on ehitatud Bitcoin'ile ja mille on välja töötanud Lightsparki meeskond. See võimaldab teha koheseid ja madalate kuludega tehinguid, säilitades samal ajal teie bitcoinide self-custody.

Erinevalt Lightning Network'ist, mis põhineb kahe osapoole vahelistel **maksekanalitel**, kasutab Spark tehnoloogiat nimega **statechain** (olekuahel). Põhimõte on järgmine: selle asemel, et iga tehingu käigus bitcoine plokiahelas liigutada, kannab Spark **kulutamisõiguse** ühelt kasutajalt teisele üle ilma on-chain liikumiseta.

### Kuidas see toimib?

Sparki intuitiivseks mõistmiseks kujutage ette, et bitcoini kulutamine Sparkis nõuab kaheosalise pusle täitmist:
- Üht tükki hoiab kasutaja (näiteks Alice).
- Teist tükki hoiab operaatorite rühm nimega **Spark Entity (SE)**.

Ainult kahe sobiva tüki kombinatsioon võimaldab bitcoine kulutada.

Kui Alice soovib oma bitcoine Bobile saata, juhtub järgmine: Bobi ja SE vahel luuakse ühiselt uus pusle. Pusle säilitab sama kuju, kuid seda moodustavad tükid muutuvad. Nüüd on Bobi tükk see, mis sobib SE omaga. Alice'i vana tükk muutub kasutuskõlbmatuks, sest SE on oma vastava tüki hävitanud. Bitcoinide omandiõigus on kätt vahetanud, **ilma ühegi tehinguta plokiahelas**.

Bob saab seejärel sama protsessi korrata, et need bitcoinid Carolile saata, ja nii edasi. Iga ülekanne toimib pusletükkide asendamise teel, mitte on-chain rahavoona.

### Miks see on turvaline?

Tekib õigustatud küsimus: mis juhtub, kui SE tegelikult oma vana tükki ei hävita?

Spark Entity ei ole üksik üksus: see on sõltumatute operaatorite rühm. SE tükki ei hoia kunagi üks operaator. Pusle asendamine nõuab mitme operaatori koostööd. Piisab, kui **ainult üks operaator on aus** ülekande ajal, et takistada vana pusle taasaktiveerimist. Ükski üksik operaator ei saa salaja säilitada vana aktiivset puslet ega seda hiljem taasluua.

Lisaks sisaldab Spark ühepoolse väljumise mehhanismi: saate alati oma bitcoinid on-chain tagasi saada ilma SE koostööta. See varumehanism on Sparki arhitektuuri lahutamatu osa ja tagab, et te ei sõltu kunagi võrgust oma vahenditele ligi pääsemiseks.

### Spark vs Lightning Network

Spark ja Lightning ei ole omavahel konkurendid: nad on **teineteist täiendavad**. Blitz Wallet integreerib mõlemad, mis võimaldab teil mõlema eelistest kasu saada.

|                               | **Spark**                    | **Lightning Network** |
| ----------------------------- | ---------------------------- | --------------------- |
| **Tehnoloogia**               | Statechains (olekuahelad)    | Maksekanalid          |
| **Kanalite haldamine**        | Pole vajalik                 | Vajalik               |
| **Sissetulev likviidsus**     | Pole vajalik                 | Vajalik               |
| **Kohesed tehingud**          | Jah                          | Jah                   |
| **Self-custody**              | Jah                          | Jah                   |
| **Lightning'i ühilduvus**     | Jah (atomic swaps kaudu)     | Natiivne              |

Lightning Network jääb suurepäraseks protokolliks koheste maksete jaoks, kuid see seab tehnilisi piiranguid (kanalite haldamine, sissetulev likviidsus, sõlm peab olema võrgus...), mis võivad algajaid pidurdada. Spark kõrvaldab need piirangud, jäädes samal ajal Lightning'iga ühilduvaks.

## Paigaldamine ja seadistamine

Selles õpetuses lähtume Blitz Wallet'i Androidi versioonist, kuid kõik allpool kirjeldatud protsessid kehtivad samuti iOS-i puhul.

![installation](assets/fr/01.webp)

Kuna Blitz Wallet on self-custody rahakott, on teil valik **luua uus rahakott** või **importida taastefraas** (12 või 24 sõna) olemasolevast rahakotist.

Siin alustame uue rahakoti loomisega. Altpoolt leiate meie soovitused taastefraasi varundamise kohta:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗ **OLULINE**: Need 12 või 24 taastesõna on **ainus ligipääsuvõti teie bitcoinidele**. Blitz on self-custodial rahakott: ei Blitzil ega Sparkil pole ligipääsu teie taastefraasile ega vahenditele. Kui kaotate need sõnad, kaotate jäädavalt ligipääsu oma bitcoinidele. Ärge jagage neid kellegagi: igaüks, kes neid omab, saab teie bitcoine kulutada.

Seejärel looge **PIN kood** oma rahakotile ligipääsu turvamiseks.

![setup-wallet](assets/fr/02.webp)

## Alustamine Blitziga

Tehingute tegemine Blitziga on intuitiivsem kui enamiku teiste Bitcoin'i rahakottide puhul. Liides on minimalistlik ja keskendub kolmele põhitegevusele: saatmine, skannimine ja vastuvõtmine.

### Bitcoinide vastuvõtmine

Bitcoinide vastuvõtmiseks oma Blitzi rahakotis klõpsake ikoonil **"Nool alla"** (↓), sisestage satoshides summa, mida soovite vastu võtta, lisage valikuline kirjeldus, seejärel genereerib rahakott arve (invoice), mille saate saatjaga jagada.

⚠️ **MÄRKUS**: Satoshi (ehk "sat") on bitcoini väikseim ühik: **1 bitcoin = 100 000 000 satoshit**.

Blitz Wallet'i üks eripärasid on see, et ta toetab mitmeid Bitcoin'i ökosüsteemi võrke ja protokolle:

- **Lightning Network**: Üks Bitcoin'i ülemkihtidest, mis võimaldab teha mikromakseid koheselt väga madalate tasudega. Ideaalne igapäevaste väikeste summade jaoks.

- **Bitcoin (on-chain)**: Bitcoin'i protokolli peamine plokiahel, mis sobib suuremate summade tehinguteks, kus maksimaalne turvalisus ja lõplikkus on esmatähtsad.

- **Liquid Network**: Blockstreami välja töötatud Bitcoin'i sidechain (paralleelahel), mis võimaldab kiireid ja konfidentsiaalseid tehinguid kasutades Liquid Bitcoin'i (L-BTC).

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Vaikimisi genereerib Blitz Lightning'i arve, kuid saate valida võrgu, milles soovite oma satoshisid vastu võtta, klõpsates nupul **"Choose format"** (Vali formaat).

![receive-sats](assets/fr/03.webp)

### Kontaktide loomine

Blitz Wallet lihtsustab korduvat bitcoinide saatmist tänu oma kontaktisüsteemile.

Menüüs **Contacts** saate registreerida Blitzi kasutajanimesid või Lightning aadresse (LNURL), kellega sageli suhtlete.

Nii saate satoshisid nendele aadressidele saata mõne klõpsuga, ilma et peaksite iga kord QR code'i skannima või aadressi käsitsi sisestama.

### Bitcoinide saatmine

Lisaks klassikalistele bitcoinide saatmise meetoditele (QR code'i skannimine, aadressi käsitsi sisestamine) pakub Blitz mitmeid praktilisi valikuid:

- **Pildilt** (*From Image*): Importige QR code oma fotogaleriist.
- **Lõikelaualt** (*From Clipboard*): Kleepige varem kopeeritud aadress või arve.
- **Käsitsi sisestamine** (*Manual Input*): Sisestage otse Bitcoin'i aadress, Lightning'i arve või loetav aadress (näiteks `kasutaja@walletofsatoshi.com`).
- **Kontaktidest**: Valige eelnevalt registreeritud saaja, et saata mõne klõpsuga.

Menüüs **Wallet** klõpsake nupul **"Nool üles"** (↑), valige saatmisviis, sisestage saadetav summa, lisage kirjeldus ja kinnitage tehing.

Minimaalne saatmissumma on praegu **1 000 satoshit**.

![send-bitcoin](assets/fr/05.webp)

## Blitzi pood

Lisaks bitcoinide ülekandmisele integreerib Blitz Wallet poe, kus saate oma bitcoine kulutada digitaalsete teenuste ostmiseks otse rakendusest.

Peamenüüst klõpsake vahekaardil **Store**, et poele ligi pääseda. Seal leiate samuti ligipääsu platvormile **Bitrefill**, mis võimaldab osta kinkekaarte tuhandete kaupmeeste juurest üle kogu maailma otse bitcoin'iga.

- **Tehisintellekt**: Pääsete ligi uusimatele generatiivse tehisintellekti mudelitele (Claude 3.5 Sonnet, GPT-4o, GPT-4o-mini, Gemini Flash 1.5) ja makske oma krediidid otse satoshides. Saadaval on mitu paketti vastavalt teie vajadustele (Casual, Pro, Power).

![ia-credits](assets/fr/06.webp)

- **Anonüümsed SMS-id**: Saatke ja võtke vastu SMS-e üle kogu maailma ilma oma isiklikku telefoninumbrit avaldamata. Teenuse eest tasutakse satoshides iga saadetud sõnumi eest.

![sms-credit](assets/fr/07.webp)

- **VPN WireGuard**: Kaitske oma veebiprivaatsust, tellides VPN WireGuard'i paketi (nädalane, kuine või kvartaalne), mida saab maksta bitcoin'iga otse Blitzi poest. Piisab, kui laadite oma seadmesse WireGuard'i klientrakenduse, et seda kasutada.

![wireguard](assets/fr/08.webp)

https://planb.academy/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

## Blitz Wallet kulisside taga: süvitsi minemine

Blitz Wallet'i kasutamise lihtsuse taga peitub läbimõeldud tehniline arhitektuur, mis ühendab Bitcoin'i ökosüsteemi mitmeid kihte.

### Teie saldo jaotus

Blitz Wallet haldab teie saldot läbipaistvalt, jaotades teie vahendid erinevate protokollide vahel vastavalt vajadustele. Kui teie saldo on alla 500 000 satoshi, kasutab Blitz **Liquid Network'i** ja aatomvahetusi (*atomic swaps*), et pakkuda teile sujuvat kogemust ja võimaldada tehinguid Lightning Network'is isegi väikeste summadega.

See lähenemine tagab lihtsa kasutuselevõtu uutele kasutajatele, ilma et neil oleks vaja mõista aluseks olevaid mehhanisme. Saate oma saldo jaotust erinevate kihtide vahel vaadata menüüs **Seaded > Balance Info**.

![balance](assets/fr/09.webp)

### Lightning'i režiim (valikuline)

Vaikimisi kasutab Blitz Wallet Liquid Network'i ja Spark protokolli, et pakkuda teile sujuvat kogemust ilma tehnilise seadistamiseta. Siiski annab Blitz teile võimaluse aktiveerida **Lightning'i režiim**, mis avab automaatselt maksekanali, kui jõuate saldoni **500 000 satoshit** (0,005 BTC).

Lightning'i režiimi aktiveerimiseks minge **Seadetesse**, seejärel jaotises **Tehnilised seaded** klõpsake valikul **Node Info**.

![enable-lightning](assets/fr/10.webp)

Tänu Spark protokollile on see aktiveerimine **valikuline**: Spark võimaldab juba teha Lightning'iga ühilduvaid makseid ilma kanali avamise või sissetuleva likviidsuse haldamiseta. Natiivne Lightning'i režiim jääb kasulikuks edasijõudnud kasutajatele, kes soovivad omada oma Lightning'i sõlme, mis on integreeritud rakendusse.

### Müügikoht (PoS)

Blitz Wallet integreerib **müügikoha** funktsionaalsuse, mis võimaldab kaupmeestel vastu võtta bitcoin'i makseid otse rakendusest.

Menüüs **Seaded > Point-of-sale** saate seadistada:

- Teie poe unikaalse identifikaatori
- Kohaliku fiat-valuuta, milles hindu kuvada
- Juhised teie töötajatele
- Jootraha valik teie klientidele

Teie kliendid peavad lihtsalt skannima genereeritud QR code'i, et teha oma bitcoin'i makse koheselt.

![pos](assets/fr/11.webp)

https://planb.academy/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

Selle õpetuse kirjutamisel kasutatud allikad:
- [Breez](https://breez.technology/) Technology blogi: [*Spark Explained Like You're Five*](https://blog.breez.technology/spark-explained-like-youre-five-8d554aad18d0).
