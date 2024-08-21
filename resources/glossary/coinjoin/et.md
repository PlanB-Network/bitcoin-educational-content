---
term: COINJOIN
---

Coinjoin on tehnika, mida kasutatakse bitcoini tehingute jälgitavuse katkestamiseks. See põhineb koostööl põhineval tehingul, millel on sama nimega spetsiifiline struktuur: coinjoin tehing. Coinjoin tehingud aitavad parandada Bitcoin'i kasutajate privaatsuskaitset, muutes väliste vaatlejate jaoks tehingute analüüsimise raskemaks. See struktuur võimaldab segada mitmeid münte ühes tehingus, muutes sisend- ja väljundiaadresside vaheliste seoste kindlakstegemise keeruliseks.

Coinjoin'i üldine toimimine on järgmine: erinevad kasutajad, kes soovivad segada, panevad tehingu sisendina teatud summa. Need sisendid tulevad välja erinevate väljunditena samast summast. Tehingu lõppedes on võimatu kindlaks teha, milline väljund kuulub millisele kasutajale. Tehniliselt pole coinjoin tehingu sisendite ja väljundite vahel mingit seost. Iga kasutaja ja iga UTXO vaheline link on katkenud, samamoodi nagu iga mündi ajalugu.

![](../../dictionnaire/assets/4.png)

Selleks, et võimaldada coinjoin'i ilma, et ükski kasutaja kaotaks oma vahendite üle kontrolli ühelgi hetkel, konstrueerib tehingu esmalt koordinaator ja seejärel edastatakse see igale kasutajale. Igaüks neist allkirjastab tehingu oma poolelt pärast kontrollimist, kas see sobib neile, ja seejärel lisatakse kõik allkirjad tehingule. Kui kasutaja või koordinaator üritab teiste vahendeid varastada, muutes coinjoin tehingu väljundeid, siis allkirjad on kehtetud ja tehing lükatakse sõlmede poolt tagasi. Kui osalejate väljundi salvestamine toimub Chaumi pimedate allkirjade abil, et vältida seost sisendiga, nimetatakse seda "Chaumian coinjoin".

See mehhanism suurendab tehingute konfidentsiaalsust ilma, et oleks vaja muuta Bitcoin protokolli. Coinjoin'i spetsiifilised rakendused, nagu Whirlpool, JoinMarket või Wabisabi, pakuvad lahendusi osalejate koordineerimisprotsessi hõlbustamiseks ja coinjoin tehingu efektiivsuse suurendamiseks. Siin on näide coinjoin tehingust:

```text
323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2
```

On raske kindlalt öelda, kes tutvustas esimesena coinjoin ideed Bitcoin'is ja kes tuli välja ideega kasutada selles kontekstis David Chaumi pimedaid allkirju. Sageli arvatakse, et Gregory Maxwell oli esimene, kes seda [sõnumis BitcoinTalk'is 2013. aastal](https://bitcointalk.org/index.php?topic=279249.0) arutas:
Kasutades Chaumi pimedaid allkirju: Kasutajad ühenduvad ja esitavad sisendid (ja vahetus aadressid) ning krüptograafiliselt pimendatud versiooni aadressist, kuhu nad soovivad oma privaatmündid saata; server allkirjastab tokenid ja tagastab need. Kasutajad ühenduvad anonüümselt uuesti, paljastavad oma väljundi aadressid ja saadavad need tagasi serverile. Server näeb, et kõik väljundid on selle poolt allkirjastatud ja seega, et kõik väljundid pärinevad kehtivatelt osalejatelt. Hiljem ühenduvad inimesed uuesti ja allkirjastavad.
Maxwell, G. (2013, August 22). *CoinJoin: Bitcoin privaatsus reaalses maailmas*. BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0
Siiski on varasemaid mainimisi, nii Chaumi allkirjade kohta segamise kontekstis kui ka coinjoinide kohta. [Juunis 2011 esitleb Duncan Townsend BitcoinTalkis](https://bitcointalk.org/index.php?topic=12751.0) mikserit, mis kasutab Chaumi allkirju viisil, mis on üsna sarnane kaasaegsete Chaumian coinjoinidega. Samas teemas on [sõnum hashcoinilt vastuseks Duncan Townsendile](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793), et parandada tema mikserit. See sõnum esitab midagi, mis sarnaneb kõige rohkem coinjoinidega. Samuti on mainitud sarnast süsteemi [sõnumis Alex Mizrahilt 2012. aastal](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), kui ta nõustas Tenebrixi loojaid. Terminit "coinjoin" ei leiutanud Greg Maxwell, vaid see tuli Peter Toddi ideest.
> ► *Terminil "coinjoin" ei ole prantsusekeelset tõlget. Mõned bitcoinide kasutajad kasutavad ka termineid "mix", "mixing" või "mixage", et viidata coinjoin tehingule. Segamine on pigem protsess, mida kasutatakse coinjoini südames. Samuti on oluline mitte segi ajada segamist coinjoinide kaudu segamisega keskse tegutseja kaudu, kes võtab protsessi ajal bitcoine enda valdusse. See ei ole seotud coinjoiniga, kus kasutaja ei kaota oma bitcoinide üle kontrolli protsessi ajal.*