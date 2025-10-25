---
name: Nunchuk
description: Wallet mobiil sobib kõigile
---
![cover](assets/cover.webp)



## Võimas Wallet


Nunchuk saabus 2020. aasta lõpus selge filosoofiaga: muuta mitme allkirjaga mängimine standardiks. Seepärast on see loodud väga täiustatud funktsioonide täitmiseks, kusjuures väärtuslik valik oli ehitada konstruktsioon otse Bitcoin Core'ile, mis on Bitcoin ökosüsteemi võrdlustarkvara.



Pärast enam kui 4 aastat kestnud arendus- ja kasutamisperioodi on see nüüdseks valmis, et seda saaks katsetada mastaabis. Kui olete algaja ja Nunchukiga mitte kursis, aitab see juhend teil teha esimesi samme ja avastada seda tarkvara, mille edasijõudnud funktsioonidega saate tutvuda, kui olete esimesest löögist üle saanud. Õpetus ise on mõeldud edasijõudnutele, kellel on vajalikud oskused kõigi sammude järgimiseks, kuid see võib olla inspiratsiooniks kõigile, kes soovivad teada saada, kuidas oskusi suurendada. Alustame mobiiliversioonist ja see väljatoomine on vajalik, sest Nunchukil on tarkvara, mis töötab ka arvutites.



## Lae alla


Esimene samm on kindlasti otsustada, kust rakendus alla laadida. Mine [ametlikule saidile](https://nunchuk.io/), kust leiad dokumentatsiooni (mitte palju, aga see on algus), funktsioonide tutvustuse ning lehe lõpus kõik allalaadimislingid.



📌 Selle õpetuse jaoks otsustasin näidata teile, kuidas laadida Software Wallet alla Githubi repositooriumist ja kuidas kontrollida versiooni enne selle paigaldamist oma mobiiltelefonile. **Järgnevat protseduuri saab teha ainult arvutist**, seega soovitan teha kõik need sammud töölaualt või sülearvutist ja - pärast kõiki kontrollimisi - kanda `.apk` fail oma mobiiltelefoni.



![image](assets/en/01.webp)



Kui teie oskused ei ole väga arenenud, võite otsustada, et laadige `.apk` ametlikest kauplustest alla ja hüpake otse selle õpetuse konfigureerimisosa juurde. Kui te aga soovite hüpata, jätkake samm-sammult.



Seega klõpsake oma töölauakompuutrist _Visiit meie avatud lähtekoodiga repositooriumi_



Link viib teid Nunchuki Githubi lehele, kust leiate mitmeid reposid. Keskendume _nunchuk-android_-leheküljele



![image](assets/en/02.webp)



Järgmisel ekraanil leiate paremal pool jaotise _Releases_ ja valige _Latest_



![image](assets/en/03.webp)



Laadige alt _Assets_ alla versioon (antud näites 1.67.apk) koos SHA256SUMS-faili ja SHA256SUMS.asc failiga.



![image](assets/en/04.webp)



Arendaja GPG võtme leidmiseks minge tagasi repositooriumi _Releases_ sektsiooni ja otsige 1.9.53 (või varasem), mis sisaldab linki _GPG võtme_ saamiseks ja allalaadimiseks



![image](assets/en/05.webp)



Me jätkame kontrollimist Sparrow wallet poolt pakutava käepärase tööriista abil, millel on selleks spetsiaalne aken ja mis toetab PGP-allkirju ja SHA256-manifeste.



Seejärel käivitage Sparrow ja valige menüüst _Tööriistad_ käsk _Verify Download_.



![image](assets/en/06.webp)



Avanevas aknas leiate väljad, mida "täita": valige paremal olev nupp _Browse_ ja valige iga välja jaoks vastavad failid, mille olete äsja Githubist alla laadinud. Kui olete kõik sammud lõpule viinud, näeb aken välja järgmiselt, Green kontrollmärgiga ja Hash kinnitusega manifesti kohta.



![image](assets/en/07.webp)


**N.B.** ekraanipilt on tehtud Windowsi arvutist, sama praktikat saab kasutada mis tahes operatsioonisüsteemiga arvutis, lihtsalt Sparrow wallet peab olema paigaldatud. Ja kontrollitud!



Leiad Sparrow wallet juhendi, et laadida alla see Software Wallet


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Seejärel saate .apk-faili arvutist telefoni üle kanda



![image](assets/en/08.webp)



ja paigaldada Nunchuk



![image](assets/en/09.webp)



Enne Nunchuki käivitamist telefonis avage Orbot ja pange uustulnukad Tori alla suunatavate rakenduste nimekirja.



![image](assets/en/11.webp)



Nüüd käivitage Nunchuk. Projekti funktsioonide jaoks - mis ei ole selle õpetuse teema - kutsub Nunchuk pärast avamist teid sisse logima e-posti või Google'i profiili kaudu. Kuni te ei kavatse kasutada Nunchuk Inc-i täiustatud plaane, **vältige sisselogimist** ja jätkake, valides valiku _Continue as guest_ (Jätka külalisena).



![image](assets/en/12.webp)



## Seaded


Nunchuk esitleb end _Kodu_ aknaga, kus on lihtne mõista selle tööfilosoofiat ja mida me kohe lähemalt selgitame.



Alumisest osast leiate menüüd ja esimese sammuna valige _Profiil_, et pääseda seadistustesse.



![image](assets/en/10.webp)



Seejärel valige _Ekraaniseaded_, jätkates konto loomise kutse ignoreerimist.



![image](assets/en/14.webp)



Allpool oleval ekraanil saate kontrollida, kas Wallet on võrgus ja kas saate oma serveri ühendada, pöörates suurt tähelepanu juhistele lingil, mida pakutakse, kui klõpsate _teisele juhendile_.



![image](assets/en/15.webp)



Salvestage seaded käsuga _Save network settings_, minge tagasi menüüsse _Profile_ ja valige _Security settings_.



![image](assets/en/16.webp)



Selles menüüs määrate, kuidas kaitsta rakenduse avamist. Soovimatu juurdepääsu vältimiseks saate Nunchuki kaitsta telefoni biomeetrilise tunnusega ja/või lisada turva-PINi.



![image](assets/en/17.webp)



Vaata ka menüüd _About_, mille leiad alati aknast _Profiil_



![image](assets/en/18.webp)



mis võimaldab teil kontrollida rakenduse versiooni või vajadusel võtta ühendust arendajatega.



![image](assets/en/19.webp)



## Key Generation ja Wallet


Nagu Nunchuki filosoofiast on lihtne arvata, on tarkvara mõeldud kasulikuks vahendiks mitme allkirjaga rahakottide haldamiseks. Selle funktsiooni täitmiseks võimaldab Nunchuk luua Wallet, eraldades need digitaalallkirjade korraldamiseks vajalikest võtmetest.



Tegelikult hõlmab Nunchuki ideaalne toimimine rahakottide loomist, mis võivad olla ainult kellad, sõltuvalt võtmetest, mis võivad olla "külmad"



Eelnevatel ekraanidel olete võib-olla märganud, et allosas on menüü nimega _Keys_. Kui olete just Nunchuki alla laadinud, näete nii _Kodu_ kui ka _Keys_ all suurt nuppu, mis kutsub teid üles lisama klahvi, _Add Key_.



![image](assets/en/20.webp)


![image](assets/en/21.webp)



**See on just see, kuidas Nunchuk töötab:** kõigepealt generate/impordite võtmed ja seejärel loote Wallet, konfigureerides seda, et valida, millised võtmed lubavad sellel salvestatud vahendite avamist.



Isegi Wallet singlesigi puhul loote kõigepealt võtme ja alles seejärel Wallet. Ja just seda me nüüd teeme, alustades Wallet singlesigiga, et murda jää ja avastada Nunchuki funktsioone.



Klõpsake nuppu _Add Key_



![image](assets/en/22.webp)



Nunchuk näitab mitmeid toetatud signatuurseadmeid, kuid alustuseks valige _Tarkvara_.



![image](assets/en/23.webp)



Nunchuk generate Mnemonic, mis salvestatakse seadmesse. Seejärel peate kirjutama üles sõnade järjestuse varundamiseks, luues parimad keskkonnatingimused ja veendudes, et teil on aega seda hästi ja vaikselt teha. Tarkvara näitab Mnemonic ainult üks kord, olenemata sellest, kas soovite seda näidata praegu või hiljem, seega valige _Create and backup now_.



![image](assets/en/24.webp)



Nunchuk genereerib 24-sõnalised Mnemonic laused, mis ilmuvad kohe järgmisele ekraanile



![image](assets/en/25.webp)



ja seejärel tegi kiire kontrolli, paludes teil valida 3 valikust õige sõna, mis vastab numbrile Mnemonic järjestuses.


Kui te olete Mnemonic õigesti kirjutanud, muutub nupp _Jätka_ töötavaks. Edasi liikumiseks vajutage seda.



![image](assets/en/26.webp)



Nimetage oma klahv ja vajutage nuppu _Jäta_.



![image](assets/en/27.webp)



Nende sammude lõpus küsitakse, kas soovite oma Mnemonic fraasile lisada [passphrase](https://planb.network/en/resources/glossary/passphrase-bip39). Kui te ei ole piisavalt teadlik passphrase kasutamisest, selle varundamise korraldamisest või selle toimimisest, soovitan valida _Mulle ei ole fraasi vaja_.



![image](assets/en/28.webp)



Võti on lõpuks loodud ja seda näidatakse teile menüüs:




- _Key Spec_ puhul on näidatud põhisõrmejälg
- Teil on seaded, kolm punkti üleval paremal, kus saate kustutada võtme või allkirjastada sõnumi
- Võtme nime kõrval on nupu ikoon, millele klõpsates saate muuta võtme nime, näiteks selleks, et tulevikus oma võtmed korras hoida.
- Viimase käsuna saate kontrollida võtme tervislikku seisundit: vajutades _Run health check_ saate lasta rakendusel kontrollida, kas võti on kahjustatud.



Kui olete valmis, klõpsake _Done_



![image](assets/en/29.webp)



Menüüs _Keys_ näete oma esimest võtit.



![image](assets/en/30.webp)



Kui lähete menüüsse _Kodu_, ilmub valik Wallet loomiseks. Klõpsake nuppu _Create new wallet_.



![image](assets/en/31.webp)



Nunchuk näitab teile mitmeid võimalusi, mis on enamasti seotud ettevõtte pakutavate teenustega, mis ei ole selle õpetuse teema.



Selles juhendis loome _Hot Wallet ja _Custom wallet_, kirjeldades üksikasju.


Alustame _Custom wallet_.



![image](assets/en/32.webp)



Lihtsalt öeldes palub rakendus teil anda sellele uuele Wallet-le nimi ja valida aadresside jaoks skript. Õpetuse jaoks otsustasin jätta vaikimisi seadistuse _Native segwit_. Kui olete lõpetanud, valige _Continue_



![image](assets/en/33.webp)



Wallet konfiguratsioonis palutakse teil määrata, millise võtmega selle Wallet vahendid avatakse. Kui võtmeid on mitu, kuvatakse teile nimekiri, millest valida. Meie oleme hetkel loonud ainult ühe, seega valime selle võtme, et paneme selle peale ristmärgi. Paremas alumises nurgas näete, kuidas Nunchuk palub teil luua oma tulevase Wallet mitu allkirja, suurendades _Vajalike võtmete_ arvu.



![image](assets/en/34.webp)



Kuna me loome singlesig, jätame "1" ja vajutame nuppu "Jätka".



Viimasena ilmub kontrolliekraan, kus saate kontrollida Wallet funktsioone:




- nimi
- `1/1 Multisig` tage, nii nimetab Nunchuk Wallet singlesig'i
- skripti tüüp, "Native SegWit"
- võti `Keys` koos selle sõrmejälje ja tuletamise teega



Kui olete rahul, vajutage _Create wallet_



![image](assets/en/35.webp)



Wallet on loodud ja te saate [.BSMS](https://github.com/Bitcoin/bips/blob/master/bip-0129.mediawiki) faili varukoopiana alla laadida. Peamenüüsse naasmiseks klõpsake vasakus ülanurgas oleval noolega.



![image](assets/en/36.webp)



Olete kohas _Kodu_, kus teile kuvatakse äsja loodud Wallet, mis teatab ühenduse saldost ja olekust. Klõpsates sinisel alal, saate juurdepääsu Wallet põhifunktsioonidele.



![image](assets/en/37.webp)





- Paremas ülanurgas olev objektiivi ikoon võimaldab teil teha tehinguotsingu;
- `View Wallet config` annab ligipääsu konfiguratsioonimenüüle, kus saab muuta Wallet nime ja lubada täiustatud valikuid, üleval paremal (millest ei saa ekraanipilte). Siin saate eksportida Wallet konfiguratsiooni, sildid, asendada klahve, muuta [gap limit] (https://planb.network/en/resources/glossary/gap-limit) ja muud.



## Tehingud Nunchukiga



Auhinnad _saab_



![image](assets/en/38.webp)



Rakendus on programmeeritud näitama Address QR-koodi või kopeerima/jagama scriptPubKey-d, et saada onchaini vahendeid.



![image](assets/en/39.webp)



Meil saabus UTXO selle esimese Address peale,



![image](assets/en/40.webp)



kuid me vajutame ikkagi _Vastuvõtmine_, et saada teine.



![image](assets/en/41.webp)



Eesmärk on, et sa saaksid teada, et Nunchuk teatab sulle selle uue Address aadressi kui _Kasutamata aadressi_, kuid näitab sulle ka, et sul on _Kasutatud aadressid_ ja nende arvu.



### Mündikontrolliga tehingu kulutamine



Kui ka see teine UTXO on saabunud, minge tagasi Wallet põhiekraanile, et kontrollida kahe sissetuleva tehingu staatust ja, mis kõige tähtsam, klõpsake valikul _View coins_ (Mündi vaatamine)



![image](assets/en/42.webp)



kus teile näidatakse üksikuid UTXOsid. Siin saate valida, kas soovite vaadata ühte konkreetset summat, klõpsates summa kõrval oleval väikesel noolega



![image](assets/en/43.webp)



ja kontrollida, millal see saabus, kirjeldus, plokk UTXO, nii et see ei ole kulutatud ja rohkem.



![image](assets/en/44.webp)



Aga kui sa lähed tagasi menüüsse _Mündid_, klõpsates noolt paremas ülanurgas, saad lülitada sisse "Mündikontrolli", et kulutada oma UTXO-d kontrollitumalt.



Järgnevas näites valisin 21 000 Sats-st UTXO ja seejärel klõpsasin vasakus alumises nurgas oleval sümbolil.



![image](assets/en/45.webp)



Nunchuk avab selle UTXO kulutamiseks automaatselt akna _Uue tehing_. Kulutamistehingus peate kõigepealt määrama summa käsitsi või valides _Sendama kõik valitud_, et saata kogu mündikontrolli saldo, ilma jääke tekitamata. Kui summa on määratud, valige _Continue_



![image](assets/en/46.webp)



Nüüd näitab Nunchuk, kuhu tuleb kleepida Address, kuhu need vahendid üle kanda, esitada üksikasjalik kirjeldus ja lõpetada tehing.



![image](assets/en/47.webp)



Valides _Create transaction_, delegeeritakse automaatne tasu ja tehingu haldamine rakendusele. Soovitan valida _Custom transaction_ suurema kontrolli saavutamiseks.



Sellel uuel ekraanil on oluline valida




- _Substraheeri tasu saatmise summast_, et vältida tasu maksmist teise UTXO poolt, mis on Wallet-s, kulutades seda ja tekitades jäägi (mis on välditav privaatsuse kaotamine);
- ja seejärel määrata tasud käsitsi pärast kontrollimist exploreril.



Kui olete kõik need sammud läbi teinud, klõpsake nuppu _Jätka_



![image](assets/en/48.webp)



Järgmisel ekraanil kuvatakse tehingu täielik kokkuvõte. Kui kõik on korras, kinnitage, valides _Confirm and create transaction_.



![image](assets/en/49.webp)



Funktsiooniga _Olemasolevad allkirjad_ teavitab Nunchuk teid sellest, et tehing ootab teie allkirja kulutuste heakskiitmiseks, mille te kinnitate, klõpsates nupul _allkirjastada_.



![image](assets/en/50.webp)



Lõpliku ja allkirjastatud tehingu levitamiseks ilmub allosas käsk _Broadcast_.



![image](assets/en/51.webp)



### Tehingu kulutamine menüüst _Saatmine_



Kui Wallet pealehel näeme, et tehing läheb välja ja ootab kinnitust, siis kasutame menüüd _Send_, et simuleerida päevakulu.



![image](assets/en/52.webp)



Kui klõpsata _Send_, avaneb tegelikult tehingu saatmise ekraan, mis on sama, mis äsja nähtud, kuid ilma mündikontrolli läbimata.



Ka selles teises näites otsustasin valida _Custom transaction_ ja saata kogu summa, kuid oleksin võinud selle ka käsitsi määrata. Kui olete otsustanud, millise summa soovite saata, vajutage _Continue_.



![image](assets/en/53.webp)



Seejärel tehke alati juhtum, kas tasud lahutatakse kõnealusest UTXO-st (antud näites on valik sunnitud, sest neid on ainult üks), kohandage tasud käsitsi vastavalt hetkeolukorrale Mempool-s ja vajutage _Continue_.



![image](assets/en/54.webp)



Kui kokkuvõttev ekraan on rahuldav, valige _Confirm and create transaction_.



![image](assets/en/55.webp)



Allkirjastage tehing koos _Sign_



![image](assets/en/56.webp)



ja levitada seda võrgus.



![image](assets/en/57.webp)



Wallet on selles punktis, kus saldo on null ja ajalugu uuendatakse.



![image](assets/en/58.webp)



## "Hot Wallet" loomine



Viimasena ja et mitte jätta midagi välja Nunchuk mobile'i algstaadiumist, vaatame, kuidas see loob selle, mida rakendus nimetab "Hot Wallet"



Nunchuki menüüs _Home_, kus kuvatakse rahakottide nimekiri, klõpsake paremas ülemises nurgas olevale `+`.



![image](assets/en/59.webp)



Valige valikute hulgast _Kuum rahakott_



![image](assets/en/60.webp)



Nunchuk jagab mõningaid nõuandeid Hot rahakotide käitlemise kohta esitluslehel, kus te valite jätkamiseks _Jätka_.



![image](assets/en/61.webp)



Mõne hetke pärast on Wallet loodud ja ilmub nimekirja pruunika värviga. Selle värviga annab Nunchuk teile märku, et te ei ole veel Wallet varundanud.



![image](assets/en/62.webp)



Klõpsake Wallet nimele, et pääseda ligi selle konfiguratsioonidele, ja te võite märgata üleskutset varundada Mnemonic fraasi kohe.



![image](assets/en/63.webp)



Menetlus on sama, mida oleme varem näinud, nii et me ei hakka seda uuesti üle vaatama. Kui see on tehtud, viib Nunchuk teid vastavale võtmelehele, mida saate redigeerida nagu seda, mille olete loonud _Custom_-protseduuriga.



![image](assets/en/64.webp)



Proovige ka _Tervisekontrolli käivitamine_



![image](assets/en/65.webp)



või vaadata, kuidas kuvada kõiki oma rahakotte rakenduse _Kodu_ kaudu.



![image](assets/en/66.webp)



## Pidada meeles, et jätkata iseseisvalt


Nii nagu loomisel on olemas järjekord, st kõigepealt genereeritakse võtmed ja seejärel Wallet, tuleb ka nende elementide kustutamisel rakendusest säilitada vastupidine järjekord.



Kui teil on vaja ühte võtit kustutada, peaksite kõigepealt olema ettenägelikult kustutanud Wallet ehk rahakotid, mis kasutavad tehinguteks ühte allkirja võtit: esmalt kustutate rahakotid ja alles seejärel võtmed. Kui te seda järjekorda ei järgi, ei ole teil võimalik võtit eemaldada.



Nüüd, kui tead, kuidas Nunchukiga alustada, võid jätkata selle rakenduse uurimist ja selle saladuste avastamist. Selles õpetuses tegime vaid esimesed sammud, kuid on olemas keerukamaid rakendusi ja edasijõudnute vajadusi, mida see Software Wallet võib aidata teil täita.