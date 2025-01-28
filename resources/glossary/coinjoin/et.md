---
term: COINJOIN

---
Coinjoin on meetod, mida kasutatakse bitcoinide jälgitavuse rikkumiseks. See tugineb ühisele tehingule, millel on eriline samanimeline struktuur: coinjoin-tehing. Coinjoin-tehingud aitavad parandada Bitcoini kasutajate privaatsuse kaitset, kuna välise vaatleja jaoks on tehingute analüüsimine raskendatud. See struktuur võimaldab segada mitu münti ühes tehingus, mistõttu on raske kindlaks teha seoseid sisend- ja väljundaadresside vahel.

Coinjoin'i üldine toiming on järgmine: erinevad kasutajad, kes soovivad segada, annavad tehingu sisendiks mingi summa. Need sisendid tulevad välja sama summa erinevate väljunditena. Tehingu lõpus ei ole võimalik kindlaks teha, milline väljund kuulub millisele kasutajale. Tehniliselt puudub seos coinjoin-tehingu sisendite ja väljundite vahel. Seos iga kasutaja ja iga UTXO vahel on katkenud, samamoodi nagu iga mündi ajalugu.

![](../../dictionnaire/assets/4.webp)

Selleks, et võimaldada coinjoin'i, ilma et ükski kasutaja kaotaks igal ajal kontrolli oma raha üle, koostab tehingu esmalt koordinaator ja edastab selle seejärel igale kasutajale. Seejärel allkirjastab igaüks omalt poolt tehingu pärast seda, kui ta on kontrollinud, et see talle sobib, ning seejärel lisatakse kõik allkirjad tehingule. Kui kasutaja või koordinaator üritab teiste rahalisi vahendeid varastada, muutes coinjoin-tehingu väljundeid, siis on allkirjad kehtetud ja sõlmed lükkavad tehingu tagasi. Kui osalejate väljundite salvestamine toimub Chaumi pimedate allkirjade abil, et vältida seost sisendiga, nimetatakse seda "Chaumi coinjoiniks".

See mehhanism suurendab tehingute konfidentsiaalsust, ilma et see nõuaks muudatusi Bitcoini protokollis. Konkreetsed coinjoini rakendused, nagu Whirlpool, JoinMarket või Wabisabi, pakuvad lahendusi, mis hõlbustavad osalejate vahelist koordineerimisprotsessi ja suurendavad coinjoini tehingu tõhusust. Siin on näide coinjoin-tehingu kohta:

```text
323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2
```

Raske on kindlalt kindlaks teha, kes esimesena tutvustas Bitcoinis coinjoini ideed ja kellel oli idee kasutada David Chaumi pimedat allkirja selles kontekstis. Sageli arvatakse, et Gregory Maxwell arutas seda esimesena [2013. aastal BitcoinTalkis avaldatud sõnumis](https://bitcointalk.org/index.php?topic=279249.0):

Chaumi pimedate allkirjade kasutamine: Kasutajad ühenduvad ja esitavad sisendid (ja muudavad aadressi) ning krüptograafiliselt pimendatud versiooni aadressist, kuhu nad soovivad saata oma eramünte; server allkirjastab märgid ja tagastab need. Kasutajad ühenduvad uuesti anonüümselt, paljastavad oma väljundaadressid ja saadavad need serverile tagasi. Server näeb, et kõik väljundid on tema poolt allkirjastatud ja et järelikult pärinevad kõik väljundid kehtivatelt osalejatelt. Hiljem ühenduvad inimesed uuesti ja allkirjastavad.

Maxwell, G. (2013, 22. august). *CoinJoin: Bitcoini privaatsus reaalses maailmas*. BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0

Siiski on olemas varasemad viited nii Chaumi allkirjade kohta segunemise kontekstis kui ka kaasühenduste kohta. [2011. aasta juunis tutvustab Duncan Townsend BitcoinTalkis](https://bitcointalk.org/index.php?topic=12751.0) segajat, mis kasutab Chaumi allkirju üsna sarnaselt tänapäevaste Chaumi coinjoinidega. Samas teemas on [hashcoini sõnum vastuseks Duncan Townsendile](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) tema mikseri täiustamiseks. Selles sõnumis on esitatud see, mis kõige rohkem sarnaneb coinjoinidele. Sarnast süsteemi on mainitud ka [Alex Mizrahi sõnumis 2012. aastal](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), kui ta nõustas Tenebrixi loojaid. Termin "coinjoin" ise ei ole Greg Maxwelli leiutatud, vaid see tuleneb Peter Toddi ideest.

> ► *Terminil "coinjoin" puudub prantsuskeelne tõlge. Mõned bitcoin'id kasutavad coinjoin-tehingu kohta ka mõisteid "mix", "mixing" või "mixage". Segamine on pigem protsess, mida kasutatakse coinjoini keskmes. Samuti on oluline mitte segi ajada segamist coinjoini kaudu segamist keskse toimija kaudu, kes võtab protsessi käigus bitcoinid enda valdusesse. Sellel ei ole midagi pistmist coinjoiniga, mille puhul kasutaja ei kaota protsessi käigus kontrolli oma bitcoinide üle.*