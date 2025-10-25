---
name: Coin Control
description: Tutvuge Coin Controliga, võtmetööriistaga oma privaatsuse kaitsmiseks Bitcoinis
---
![cover](assets/cover.webp)


*See õpetus on imporditud [Officine Bitcoini õppetunnist](https://officinebitcoin.it/lezioni/coinco/).*



## Sissejuhatus



Bitcoini protokolli tugevuse tagavad lihtsad põhimõisted. Nende seas paistab silma läbipaistvus: kõik Bitcoini tehingud on avalikud ja igaühe poolt hõlpsasti kontrollitavad. Kuigi see omadus on protokolli nurgakivi, kuna see hoiab ära pettused ja tagab vahendite autentsuse, võib see kujutada endast ka väljakutset konfidentsiaalsusele. **Oled sa mõelnud, kas selline läbipaistvus võib kahjustada sinu privaatsust?**



Sa peaksid. Kuigi Satoshi non-kyc kogumine on üsna lihtne, on teie privaatsus kõige rohkem ohus just kulutuste tegemise etapis.



### Mis juhtub, kui te kulutate UTXO



Bitcoin kulutamine ei ole lihtsalt väärtuse ülekandmine kellelegi teisele.



Tarbides ühte oma UTXOdest, peate te tegelikult täitma protokolli läbipaistvuse jaoks kehtestatud tingimusi, sest teil on kohustus tõestada, et need vahendid kuuluvad teile. Seega panete te end vastutavaks :




- avalikustage oma avalik võti;
- toota digitaalallkirja.



Seetõttu on kulutuste tegemise aeg kõige kriitilisem: ** Bitcoin kulutamine on tegu, mida tuleb teha teadlikult ja võimalikult palju kontrolli all**.



## Coin kontroll



Bitcoin protokollis ei ole selliseid elemente nagu _konto_ või _rahaühikud_ olemas. UTXO kontseptsiooni selgitatakse suurepäraselt järgmises kursuses, mida ma väga soovitan:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Bitcoin abil kogunevad ja hiljem kulutatakse väikesed või suured arvestusühikud, mida mõõdetakse Satoshi, mida esindavad `kulutamata tehingu väljundid`, **UTXO**, mida nimetatakse ka `müntideks`. Kui kasutate UTXOsid tehingu loomiseks, hävitatakse need täielikult ja nende asemele luuakse teised UTXOd.



Tarkvara rahakotid on välja töötatud selleks, et teha see valik automaatselt, kasutades "juhuslikult" valitud münte, võttes kasutusele teatud protokolli poolt ette nähtud algoritmid. Ainus kriteerium, millele need algoritmid vastavad, on kulutamiseks vajaliku summa katmine.



Need võivad segada kokku eri vanuses UTXOsid või eelistada kõige uuemaid või "vanemaid" kulutusi, sõltuvalt arendajate valitud algoritmist. Parimad tarkvara rahakotid, kavatsevad ka jätta kasutajale olulise valiku.



Käsiraamat `Coin Control`, millele võib viidata ka kui `Coin Selection`, on mõnede tarkvarakomplektide funktsioon, mis võimaldab teil **manuaalselt valida UTXO-d, mida te oma tehingu koostamisel kulutate**.



Oletame, et meil on Wallet, millel on 3 UTXO-d vastavalt 21 000, 42 000 ja 63 000 Satoshi.



![img](assets/en/01.webp)



Kui peate kulutama 24 000 Sats ja laskma algoritmil teha automaatse valiku, võib hea Software Wallet valida UTXO 1 + UTXO 2, et maksta 24k Sats ja Miner tasud, tekitades jäägi, mis läheb tagasi Address sisemisele Wallet algavale GW-le.



![img](assets/en/02.webp)



Pärast tehingut võib Wallet uue olukorra, mis hõlmab ainult UTXOd, kokku võtta järgmiselt.



![img](assets/en/03.webp)



Õige tarkvara ja teie teadlikkuse korral oleksite aga võinud teha teistsuguse, mõnes mõttes õigema valiku. Näiteks valides ainult UTXO2 (alates 42 000 Sats).



![img](assets/en/04.webp)



Teie Wallet lõppolukorras, UTXO tasemel, mis näeb välja teistsugune kui varem.



![img](assets/en/05.webp)



## Miks käsitsi coin control?



![img](assets/en/06.webp)



Kahe eespool toodud näite puhul on saldo tegelikult sama `108,280 Sats`. Pärast 24 000 Sats kulutamist oleks meil ilma manuaalse valikuta 2 UTXO Wallet; Coin manuaalse kontrolliga on meil kokku 3 UTXO.



Küsimus, mille me võiksime endalt küsida, on järgmine: **miks seda kõike teha?** On olemas või võiks olla mitu põhjust, miks me ei kasutanud `UTXO1` **ja need kõik on aluseks sellele, miks kulutamise faasis on üheks heaks tavaks manuaalse coin control'i aktiveerimine**.



UTXOde valimine võimaldab teil eelistada mõningaid aspekte teistele. Valik sõltub tegelikult eesmärkidest, mida soovite saavutada.



### Privaatsus



Üks peamisi eeliseid, kui tegemist on käsitsi Coin kontrolliga, on **suurim privaatsus kulutaja jaoks**. Võtame alati meie näite: 24 000 Satoshi kulutused _manuaalse Coin valiku_ puudumisel. Kuna Blockchain Bitcoin on avalik, võib väline vaatleja ilma igasuguse kahtluseta väita, et sisendid `UTXO1 21,000 Sats` ja `UTXO2 42,000 Sats`, samuti ülejäänud, `UTXO5 38,280 Sats`st **kuuluvad kõik kolm samale kasutajale**.



Käsitsi valides seevastu `UTXO2`, jääb `UTXO1` täielikult reserveerituks, istudes UTXO komplektis ja oodates, et seda saaks kasutada sobivamal ajal.



"UTXO1" võib pärineda KYC allikast, näiteks Exchange-s kaupade ja teenuste eest saadud maksest, samas kui teised UTXO-d ei ole. UTXO-kyc-i segamine teiste konfidentsiaalsemate vahenditega ohustab mittekyc-i vahendite anonüümsuse kogumit.



**KYC vahendid viiksid paratamatult makse tegija identiteedi tuvastamiseni. Kui see oleks sinu rahakott, kas sooviksid, et väline vaatleja saaks sinu identiteedi nii absoluutse kindlusega kindlaks teha?**



Proovige siis arvestada, et rahakotid, mis rakendavad UTXOde käsitsi valimist, võimaldavad näiteks **ühendada ühte või mitut UTXOd**, funktsiooni, mida saab kasutada selliste olukordade tekkimisel.



Kuigi ma olen veendunud, et KYC-i vahendeid tuleks hoida eraldi Wallet-s kui Bitcoin, mis on ostetud ilma kyc-ta, on teie puhul mõne aadressi eraldamine oluline abi, mida võiksite kasutada, õppides käsitsi valima oma kulutuste sisendeid.



### Tasude kokkuhoid



Õige UTXO valimine kulutuste tegemiseks **võimaldab tasu optimeerimist**. Jällegi alustades meie esialgsest näitest, valis Software Wallet kaks UTXOd, et katta tehtavaid kulutusi. Kaks UTXOd tähendavad kahte allkirja, mida tuleb näidata võrgule. Sellest järeldub, et tehingul on suurem "kaal" vBaitide osas.



Kasutades Coin manuaalset kontrolli, saate te seevastu valida ainult ühe, mis on piisav summa katmiseks, säästes tehingu "kaalu" vähendamisega tasusid.



Ajal, mil tasud on kõrged, kuid te olete sunnitud kulutama Bitcoin On-Chain (nt Lightning Network kanali avamiseks), siis on Coin kontroll osutub õigeks majanduslikuks stiimuliks, mille poole pöörduda.



### Jäänuste koondamine



Kui teete makse ja kasutate Bitcoin On-Chain, muutub võimalus saada raha peaaegu alati kindlaks. Iga jääk on iseenesest väike eraelu puutumatuse kaotus, sest see paljastab võrgule (ja eriti makse saajale) teie Address, mida saab seostada teie allikasissetulekuga.



Arvestades, et parim Wallet HDs generate eriaadressid jäägid, saate kergesti tunda neid ja "eraldada" kõik jäägid erinevate tehingute tehtud; kui nad on jõudnud teatud summa, saate valida neid käsitsi ja konsolideerida neid, või vahetada Lightning Network (minu eelistatud meetod) ja töödelda neid, et taastada privaatsust kaotatud kulutusi.



### Cold Wallet kulud



Cold Wallet on vahend, millega saab mõistlikult saavutada hea turvalisuse taseme, et hoida mis tahes summat raha pikaks ajaks kõrvale. Siiski võib juhtuda ettenägematuid sündmusi, mistõttu tekib vajadus saada käsile säästud ja katta mõned ootamatud kulud.



Ma ei tea, kui paljud võivad jagada minu lähenemist, kuid minu soovitus on **ei kunagi teha kulutusi otse Cold Wallet, et vältida muutuste saamist sama aadresside vahel**. Õppige käsitsi valima kulutuse katmiseks vajalikud UTXOd, kandke need üle Wallet Hot ja valmistage oma tehing ette viimasest. Iga vahetus, siis võite saata selle tagasi Cold Wallet Address (kui summa on piisav), kasutada seda teiste kulude jaoks või ikkagi eraldada, nagu me just nägime.



## Praktiline esitlus


Pärast tehnilist sissejuhatust "miks", vaatame, kuidas Coin käsitsijuhtimist erinevate tarkvarade, laua- ja mobiilseadmete abil praktikas rakendada. Kasutame alati sama Wallet BIP39, mis on imporditud igasse valitud tööriistasse, et näidata teile nende vahelisi väikseid erinevusi.



## Wallet Desktop



### Sparrow



Kui kasutate Sparrow, avage oma Wallet ja valige vasakpoolsest menüüst _UTXOs_. Näete loetelu kõigist teie Wallet-ga seotud UTXOdest.



Lihtsalt klõpsake hiirega ühel neist ja valige seejärel _Saatke valitud_. Sparrow näitab teile ka pärast valiku tegemist käsu kõrval, kui palju raha on võimalik kulutada. Graafiliselt näitab Sparrow teile valitud UTXO, tõstes selle sinise värviga esile.



![img](assets/en/07.webp)



Võite valida ka rohkem kui ühe. Aita ennast _CTRL_ klahviga, et valida nimekirjas mitte-niisuguseid UTXOsid.



![img](assets/en/08.webp)



Pärast UTXO käsitsi valimist saate alustada tehingu koostamist ja Sparrow näitab teile hästi graafiliselt, kuidas see koosneb.



![img](assets/en/09.webp)



#### UTXO eraldamine



Rahaliste vahendite eraldamine tähendab nende "lukustamist" Wallet-s, nii et neid ei saa kasutada tehingu sisendina. Sparrow võimaldab seda funktsiooni, mis on alati kättesaadav menüüst _UTXOs_: asetage hiir "lukustatava" UTXO kohale ja vajutage hiire paremat nuppu. Selle protseduuri funktsioonide hulgas ilmub _Freeze UTXO_. Nii saate te Sparrow rahakotiga münte eraldada.



![img](assets/en/29.webp)



### Electrum



Kui teie Wallet töölaual on Electrum, siis peaksite teadma, et saate UTXOsid käsitsi valida kas menüüst _Adressid_ või menüüst _Mündid_. Mõlemas menüüs toimub valik, kui osutate hiirega soovitud UTXO-le ja valite pärast paremklõpsu valikut _Add to Coin control_.



![img](assets/en/10.webp)



Isegi selle tarkvara abil saate valida rohkem kui ühe UTXO, aidates oma klaviatuuril klahviga _CTRL_, kui need ei ole üksteise kõrval.



![img](assets/en/11.webp)



Graafiliselt näitab Electrum teile valikut, tõstes valitud UTXO-d Green-s esile, samal ajal kui allosas ilmub sama värviga esile tõstetud riba, mis näitab olemasolevat tasakaalu pärast Coin kontrolli.



![img](assets/en/12.webp)



Kui olete valinud väljundi või väljundid, saate oma tehingu koostada, nagu tavaliselt teete menüüst _Send_.



#### UTXO eraldamine



Electrum pakub seda funktsiooni, kui lähete menüüsse _Coins_, kus valite konkreetse UTXO ja seejärel valite paremklikiga _Freeze_. Address saate "külmutada" ka ilma rahata menüüst _Adressid_ või "Coin", et seda mitte kulutada.



![img](assets/en/28.webp)



### Nunchuk



Nunchuk võimaldab teil käsitsi valida UTXO-d peamenüüst, kui see on avatud. Käivitage Nunchuk ja klõpsake _View coins_.



![img](assets/en/13.webp)



See avab akna, mis sisaldab kõiki teie Wallets olevaid UTXOsid, kus saate valida ühe või mitu, aktiveerides iga summa kõrval oleva märkeruudu. Pärast valiku tegemist jätkake _Create transaction_.



![img](assets/en/14.webp)



Seejärel saate sisestada sihtkoha Address ning määrata summa ja tasud.



![img](assets/en/15.webp)



#### UTXO eraldamine



Täielikkuse huvides võimaldab Nunchuk oma funktsioonide hulgas ka ühe (või mitme) UTXO eraldamist ning teeb seda kahel erineval viisil. Jõuate menüüsse _View coins_ ja valige käsitsi müntide nimekirjast. Seejärel klõpsake paremal allosas olevasse menüüsse _More_: ilmub valikute nimekiri, millest saate valida _Lock coins_.



![img](assets/en/39.webp)



![img](assets/en/40.webp)



Samuti võite klõpsata UTXO jaoks reserveeritud alal, et pääseda aknasse _Coin details_. Siin ilmub paremas ülanurgas käsk kõnealuse UTXO lukustamiseks/avastamiseks.



![img](assets/en/41.webp)



### Blockstream App



Blockstream App desktop, varem tuntud kui Green, võimaldab teil teha Coin valiku, kui olete juba alustanud tehingu ehitamist. Seepärast avage oma Wallet ja klõpsake _Send_.



![img](assets/en/16.webp)



Sisestage sihtkoha Address vastavasse lahtrisse ja valige seejärel _Manuaalne Coin valik_.



![img](assets/en/17.webp)



See avab akna, kus saate valida ühe või mitu UTXO münti. Allpool toodud näites oleme valinud kaks münti. Pärast seda kinnitage oma valik, klõpsates nupule _Confirm Coin Selection_.



![img](assets/en/18.webp)



Määrake summa ja tasud ning jätkake seejärel tehingut tavapäraselt.



![img](assets/en/19.webp)



⚠️ NB. Green menüüs _Coins_ on kirjed _Lock_/_Unlock_, mis annavad aimu UTXO eraldamise võimalusest. See funktsioon on aktiveeritud ainult nn Multisig kontodel; samuti aktiveeritakse see ainult väga väikese summa UTXO valimisel, mis on lähedal `Dust` künnisele.



## Wallet mobiilne



Rahakotte saab valida ka mobiiltelefonist, mis võimaldab UTXO-d käsitsi valida. Vaatame esimese näitena Blue Wallet.



### Sinine Wallet



Kui olete selle Wallet kasutaja, avage see ja klõpsake, et siseneda ühe teie rahakotiga seotud kontroll-ekraanidele. Coin kontrollijuhendile pääsemiseks peate sisenema kulutamisfaasi, seejärel klõpsake _Send_.



![img](assets/en/21.webp)



Järgmisel ekraanil valige menüüd, mis on tähistatud kolme punktiga paremas ülanurgas. Avaneb rippmenüüaken, milles on rida käske. Valige viimane: _Coin Control_.



![img](assets/en/22.webp)



Sel hetkel näitab Blue Wallet kõiki teie UTXOsid. Lisaks summadele eristatakse neid graafiliselt erinevate värvidega.



![img](assets/en/27.webp)



Valige UTXO, mille järel valige _Use Coin_.



![img](assets/en/23.webp)



Sinine Wallet viib teid tagasi aknasse _Send_, et jätkata tehingu koostamist. Kohandage summa ja tasud, mille järel valite _Next_.



![img](assets/en/24.webp)



Siinkohal võite tehingu lõpetada, nagu te tavaliselt teete.



#### UTXO eraldamine



Blue Wallet võimaldab ka eraldada UTXO-d, muutes need kulutuste tegemiseks kättesaamatuks, mis ei ole Wallet jaoks mobiilseadme jaoks halb funktsioon. Coin kontrollile pääseb just selgitatud protseduuriga ja pärast UTXO valimist valib _Freeze_ asemel _Use Coin_.



![img](assets/en/26.webp)



### Nunchuk



Nunchuki mobiilne versioon pakub kasutajale ka võimalust teha Coin juhtimist. Kui kasutate seda rakendust mobiilist, avage see ja minge menüüsse _Wallet_. Sealt valige _View coins_.



![img](assets/en/30.webp)



Aknas, kus ilmub UTXOde loend, klõpsake nuppu _Select_.



![img](assets/en/38.webp)



Iga UTXO kõrval kuvatakse valikufunktsioon. Nagu lauaarvutiversioonis, toimub käsitsi valimine Nunchuk mobile'is, märgistades summa kõrval asuva väikese ruudu. Ekraanil kuvatakse valitud UTXOde arv ja olemasolev kogusumma. Kui olete lõpetanud, klõpsake vasakus alumises nurgas oleval sümbolil ₿, mis on käsk tehingu koostamise alustamiseks.



![img](assets/en/31.webp)



Nüüd saate tehingu lõpule viia, valides summa ja klõpsates nuppu _Continue_.



![img](assets/en/32.webp)



Jätkake nagu alati, lisades sihtkoha Address, kirjelduse ja kohandades tasu seadeid.



#### UTXO eraldamine



Võite eraldada UTXOsid ka mobiilse Nunchuki abil. Avage spetsiaalne müntide loendiaken ja valige nool selle UTXO kõrval, mida soovite eraldada.



![img](assets/en/42.webp)



Te näete ruumi, mis on reserveeritud _Mündi andmed_ jaoks, kus saate valida _Lock this coin_ (lukusta see münt).



![img](assets/en/43.webp)



### Bitcoin Keeper



Bitcoin Keeper on viimane Wallet, mida me selles juhendis näeme. Näeme selle funktsionaalsust Coin kontrollimisel Wallet ühe signeeringuga, kuigi selline kasutamine ei ole selle konkreetse rakenduse eesmärk. Pärast Keeperi seadistamist telefonis käivitage see ja avage Wallet, mis sisaldab mõningaid vahendeid. Klõpsake põhiekraani keskel nupule _View All Coins_ (Vaata kõiki münte).



![img](assets/en/34.webp)



Keeper näitab ülevaadet UTXOdest. Valikuekraanile pääsemiseks klõpsake nuppu _Select To Send_.



![img](assets/en/35.webp)



Võite valida münte, märgistades need ära, klõpsates vastaval käsul. Kui olete lõpetanud, klõpsake nuppu _Send_.



![img](assets/en/36.webp)



Bitcoin Keeper viib teid otse menüüsse _Send_, kus saate koostada tehingu valitud UTXOdega.



![img](assets/en/37.webp)



## Hardware Wallet



Iga käesolevas juhendis vaadeldav tarkvarakomplekt võib olla ainult Interface ühe teie riistvarakomplekti jaoks. See tähendab, et Coin kontroll võrguühenduseta allkirjastamise seadme jaoks toimub seni nähtud sammudega.



### Üldised soovitused



Coin kontroll on väga tõhus tava oma tehingusisendite valimiseks. Käsitsi valimine on veelgi tõhusam, kui olete oma vahendite ostmisel/saamisel hästi märgistanud oma Satoshis allikad. Kui soovite seda tehnikat hästi õppida, siis soovitan järgmist õpetust:



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Me oleme varem rääkinud "säilmete segregatsioonist". Kui te soovite lukustada jäänused hilisemaks töötlemiseks ja taastada privaatsust (vahetus Layer 2), peate hoolitsema selle eest, et `märgistada` neid iga kord, kui te saate ühe jäänuse. Seni nähtud tarkvarakomplektidest ainult Electrum värvib UTXO jäägid graafiliselt, et need oleksid silmaga nähtavad. Teised, näiteks Sparrow, näitavad teile ahelat üksiku UTXO tuletamise teel (`m/84'/0'/0'/0'/1/11`).



Selle tehnika tõhusaks rakendamiseks ärge unustage alati lisada saadud muutusele kirjeldus: isik, kellele te oma raha (makse, juhendaja või muu) saatsite, teab muutusega seotud Address ja teab, et see kuulub teile, sest see pärineb teie ühisest tehingust!