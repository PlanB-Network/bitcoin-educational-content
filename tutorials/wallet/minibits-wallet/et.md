---
name: Minibits Wallet
description: Juhend Minibits Wallet jaoks
---

![cover](assets/cover.webp)


Selles õpetuses tutvustan teile Minibits Wallet seadistamist ecash'i kasutamiseks. Võimas privaatsusele keskendunud maksetehnoloogia, mis töötab koos Bitcoinga. Minibits on ecash ja Lightning Wallet, mis võimaldab koheseid, odavaid ja privaatseid väärtuste ülekandeid, mistõttu on see ideaalne igapäevatehinguteks, kus privaatsus on oluline.


Enne minibittidesse süvenemist selgitage, mis on ja mis ei ole e-raha. Paljud inimesed ajavad ecashi segamini Bitcoin või Blockchain tehnoloogiaga, kuid need on põhimõtteliselt erinevad kontseptsioonid.


Ecash ei ole Bitcoin. See ei asenda teie isehakanud Bitcoin Wallet, vaid pigem täiendab seda. Ecash EI ole Blockchain ja EI ela üheski avalikus Ledger-s. Huvitav on see, et ecash EI ole uus tehnoloogia - see on tegelikult enne ülemaailmset veebi, mille kontseptsioonid töötati välja 1980ndatel ja 1990ndatel aastatel.


Mis on e-raha: uskumatult privaatne (tehingud ei jäta jälgitavat ajalugu), peer-to-peer (otsesed ülekanded ilma vahendajateta) ja toimib digitaalse instrumendina (kui see on teie käes, siis te kontrollite seda). Peamine eelis on see, et e-kassat VÕIB kasutada võrguühenduseta - nii saatja kui ka saaja võib tehingute ajal internetist lahti ühendada. E-raha VÕIB vermida üks osapool või usaldusväärsete üksuste liit ning see ON täiuslik täiendav tehnoloogia Bitcoin-le, mis võimaldab teha väikseid ja sagedasi tehinguid, samal ajal kui Bitcoin toimib arveldus-Layer-na.


Pange tähele, et see Minibitsi seadistus kujutab endast `custodial solution`, mis tähendab, et usaldate oma raha haldamist Mint'i operaatorile. Sellega kaasnevad konkreetsed riskid, millest peate enne jätkamist aru saama.


Projektis kuvatakse see oluline lahtiütlemine:


- Seda Wallet tuleks kasutada ainult teaduslikel eesmärkidel.
- Wallet on beetaversioon, mille funktsionaalsus on puudulik ning milles on nii teadaolevaid kui ka tundmatuid vigu.
- Ärge kasutage seda suurte summade puhul.
- Wallet-s hoitavat e-kassat annab välja rahapada
- usaldate rahapaja tagatisraha Bitcoin, kuni kannate oma varud üle teisele Bitcoin välgule Wallet.
- Cashu protokoll, mida Wallet rakendab, ei ole veel põhjalikult läbi vaadatud ega testitud.


Käsitlege Minibit'e nagu igapäevast Wallet, mitte kui säästukontot, ja ärge kunagi hoidke seal märkimisväärset väärtust.


## 1️⃣ Wallet seadistamine


Alustamiseks külastage [Minibitsi veebisaiti](https://www.minibits.cash/), kust leiate allalaadimisvõimalused kõikidele peamistele platvormidele. iOS-i kasutajad saavad alla laadida [App Store'ist](https://testflight.apple.com/join/defJQgTD), samas kui ELi iOS-i kasutajatel on lisavõimalus installida [Freedom Store'ist](https://freedomstore.io/). Androidi kasutajad saavad rakenduse [Google Play Store](https://play.google.com/store/apps/details?id=com.minibits_wallet) või laadida APK-faili otse [GitHub Releases](https://github.com/minibits-cash/minibits_wallet/releases) lehelt.


Minibiti installimisel kuvatakse sissejuhatavad ekraanid, mis selgitavad põhimõisteid - kui olete tehnoloogiaga juba tuttav, võite need läbi lugeda või vahele jätta. Kui olete need esialgsed sammud läbinud, palutakse teil valida järgmiste valikute vahel:


- `Võta see, vii mind Wallet juurde` uutele kasutajatele või
- `Recover lost Wallet`, kui taastate varukoopiast.


![image](assets/en/01.webp)

Pärast algseadistamise lõpetamist jõuate avakuvale, kus on mitu olulist Elements, mida tuleb tähele panna. ① Ülemises nurgas olev profiili ikoon viib teid oma profiililehele, kus saate juurdepääsu oma Minibits Wallet Address ja valida "partii vastuvõtu" valikud. ② Ekraani keskel näete minte, mida saate kasutada, kusjuures vaikimisi on valitud Minibits minti. ③ Allpool olev tegevusrida pakub valikuid ecash- või välkmaksete saatmiseks, QR-koodi skaneerimiseks ja maksete vastuvõtmiseks. ④ Lõpuks sisaldab alumine navigatsiooniriba otseteed avakuvale, tehingute ajaloole, kontaktidele ja seadetele.


![image](assets/en/02.webp)


## 2️⃣ Manage mints


Vaikimisi on Minibitsi mündi kasutamine rakenduse käivitamisel lubatud. Üks ecashi tugevusi on aga võimalus kasutada mitut mündi, et suurendada detsentraliseeritust ja turvalisust. Teise mündi lisamiseks navigeerige menüüsse `Settings`, seejärel valige `Manage mints` ja lõpuks puudutage valikut `Add mint`.


[Bitcoinmints.com](Bitcoinmints.com) pakub põhjalikku nimekirja saadaval olevatest mündid koos kasutajate hinnangutega, et aidata teil valida usaldusväärseid võimalusi. Mitme mündi kasutamine vähendab teie riski. Kui ühel rahapajas esineb probleeme, jäävad teie vahendid teistel rahapajadel kättesaadavaks.


![image](assets/en/04.webp)


## 3️⃣ Varukoopia loomine


Varundamine on vaieldamatult kõige kriitilisem samm kogu seadistamisprotsessis. Varundamise valikutele pääsemiseks navigeerige menüüsse `Settings`-> `Backup` Siit leiate kaks olulist valikut: `Settings`-> `Backup`, `Backup` ja `Backup`:

1. "Sinu seed fraas", mis sisaldab "12 sõna", mis võimaldab sul seadme kadumise korral taastada oma e-kassasaldo. See seed fraas on teie põhivõti kogu ecash'ile kõigis lisatud rahapaikades. Kirjutage see füüsilisele kandjale (paber või metall) ja hoidke seda turvaliselt mitmes kohas. Ärge kunagi säilitage oma seed fraasi digitaalselt, kus seda võidakse ohustada. Vaadake seda [õpetust](https://planb.network/en/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270), et tutvuda Wallet kaitsmise parimate tavadega.

2. `Wallet backup`, mis sisaldab pikka varundustrenni.


**Hoiatus**: Kui kasutate seda varukoopiat Wallet taastamiseks, vajate endiselt seed fraasi.


![image](assets/en/05.webp)


## 4️⃣ Loo minibitid Wallet Address


Järgmisena navigeerige altpoolt "Kontaktid" ja kohandage oma spetsiaalset "Minibits Wallet Address", koputades "Muuda" -> "Muuda Wallet Address". Sisestage oma eelistatud Address ja kontrollige saadavust.


![image](assets/en/07.webp)


Pärast Address seadistamist palutakse teil teha väike "annetus" projekti toetuseks. Kuigi see on vabatahtlik, soovitan seda tungivalt kaaluda, kui kavatsete teenust regulaarselt kasutada. Sellised avatud lähtekoodiga projektid nagu Minibits toetuvad arenduse ja hoolduse jätkamiseks kogukonna toetusele. Isegi väike panus aitab tagada projekti pikaajalisuse.


![image](assets/en/08.webp)


## 5️⃣ Nostr Setup


Kui soovite anda vihjeid inimestele, keda te Nostris jälgite, saate "lisada oma npubi võtme", valides "Kontaktid" ja seejärel "Avalik". See ühendab teie Minibits Wallet sotsiaalvõrgustikuga Nostr, võimaldades sujuvat jootraha andmist.


Teil on ka võimalus "kasutada oma profiili", minnes menüüsse "Seaded" ja seejärel "Privaatsus", et importida oma Nostr Address ja võti. Kuid pidage meeles, et see peatab teie Wallet suhtlemise minibits.cash Nostr ja LNURL Address serveritega, mis lülitab välja Address välkfunktsioonid zapi ja maksete vastuvõtmiseks.


![image](assets/en/09.webp)


## 6️⃣ Rahaliste vahendite saamine


Raha saamiseks peate algselt oma Wallet välk Invoice abil täiendama. See protsess on lihtne: koputage valikut `Topup` , sisestage soovitud summa, lisage soovi korral `Memo` ja seejärel koputage valikut `Loo Invoice`. Seejärel peate selle Invoice eest maksma, kasutades teist Lightning Wallet, see muudab Bitcoin Lightning-maksed teie Minibits Wallet-s ecash-märkideks.


![image](assets/en/10.webp)


## 7️⃣ Saada raha


Nüüd, kui olete oma Wallet rahastanud, saate raha saata kahel erineval viisil.


### Saada e-kassi


Esimene võimalus on saata e-kassat otse. Puudutage valikut "Saada", seejärel valige "Saada e-kassat", sisestage summa ja puudutage valikut "Loo token." See annab generate QR-koodi, mida saate jagada saajaga või lasta tal otse oma seadmega skaneerida. Saaja näeb, et märgid ilmuvad tema Wallet sahtlisse peaaegu kohe, ilma Blockchain tasude või kinnituse hilinemiseta.


![image](assets/en/11.webp)


### Maksa välguga


Teine võimalus on maksta Lightning'i kaudu. Puudutage valikut "Saada", seejärel valige "Maksmine Lightningiga". Saate valida oma Nostr `kontaktide` hulgast (kui olete ühendanud oma npubi) või sisestada/liita Lightning Address, Invoice või LNURL maksekoodi, kasutades `Paste` või `scan` valikut. Pärast saaja kinnitamist palutakse teil sisestada summa, mida soovite maksta, lisada soovi korral memo ja seejärel puudutage valikut "Kinnita", millele järgneb "Maksa nüüd", et viia Lightning-tehing lõpule.


![image](assets/en/12.webp)


## 8️⃣ NWC-ühenduse loomine


Minibitsi teine võimas funktsioon on võimalus luua "Nostr Wallet Connect (NWC)-ühendusi", mis võimaldavad teistel rakendustel taotleda makseid teie Wallet-lt ilma teie isiklikke võtmeid avaldamata.


Selle seadistamiseks valige "Seadistused", seejärel "Nostr Wallet Connect" ja koputage valikut "Lisa ühendus". Nimetage oma ühendus millegi kirjeldava nimega, et tuvastada nii rakendust kui ka seotud kasutajakontot. Määrake mõistlik maksimaalne päevane limiit, et kontrollida, kui palju selle ühenduse kaudu saab kulutada, ja seejärel puudutage seadistamise lõpetamiseks valikut "Salvesta".


See funktsioon on eriti kasulik selliste teenuste puhul nagu Nostr Clients, kus soovite lubada automaatset jootraha andmist ilma iga tehingu käsitsi kinnitamiseta.


![image](assets/en/12.webp)


## 🎯 Kokkuvõte


Minibits pakub ligipääsetavat võimalust siseneda e-raha maailma, pakkudes privaatsusele keskenduvaid makseid, mis täiendavad teie Bitcoin varusid. Ärge unustage, et te säilitaksite alati nõuetekohaseid varukoopiaid, kaaluge mitme mündi kasutamist, et tagada koondamine, ja hoidke selles hoiulahenduses ainult sobivaid summasid.


Lisaressursse leiate Minibitsi GitHubi repositooriumist, ametlikust veebisaidist ja nende Telegram-kanalist, kus kogukond arutab aktiivselt arenguid ja probleemide lahendamist


- [Github](https://github.com/minibits-cash/minibits_wallet)
- [Veebileht](https://www.minibits.cash/)
- [Telegram](https://t.me/MinibitsWallet)


E-raha ökosüsteem on alles arenemas, kuid sellised vahendid nagu Minibits teevad selle võimsa privaatsustehnoloogia tavakasutajatele üha kättesaadavamaks.