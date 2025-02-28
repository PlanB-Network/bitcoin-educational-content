---
name: Satochip
description: Satochipi nutikaardi seadistamine ja kasutamine
---
![kaas](assets/cover.webp)

Riistvarakott on elektrooniline seade, mis on pühendatud Bitcoini rahakoti privaatvõtmete haldamisele ja turvamisele. Erinevalt tarkvaralistest rahakottidest (või kuumadest rahakottidest), mis on paigaldatud üldotstarbelistele masinatele, mis on tihti ühendatud internetiga, võimaldavad riistvarakotid privaatvõtmete füüsilist isoleerimist, vähendades häkkimise ja varguse riske.

Riistvarakoti peamine eesmärk on vähendada seadme funktsionaalsusi, et vähendada selle rünnakupinda. Väiksem rünnakupind tähendab ka vähem potentsiaalseid rünnakute vektoreid, st vähem süsteemi nõrkusi, mida ründajad võiksid ära kasutada bitcoini juurdepääsuks.

On soovitatav kasutada riistvarakotti oma bitcoinide turvamiseks, eriti kui omate olulisi summasid, kas absoluutväärtuses või kui osa teie koguvarast.

Riistvarakotte kasutatakse koos rahakoti haldamise tarkvaraga arvutis või nutitelefonis. See tarkvara haldab tehingute loomist, kuid krüptograafiline allkiri, mis on vajalik nende tehingute valideerimiseks, tehakse ainult riistvarakotis. See tähendab, et privaatvõtmed ei ole kunagi avatud potentsiaalselt haavatavale keskkonnale.

Riistvarakotid pakuvad kasutajale kahekordset kaitset: ühelt poolt kaitsevad nad teie bitcoine kaugrünnakute eest, hoides privaatvõtmeid võrguühenduseta, ja teiselt poolt pakuvad nad üldiselt paremat füüsilist vastupanu võtmete kättesaamise katsetele. Ja just nendel 2 turvakriteeriumil saab hinnata ja järjestada turul saadaolevaid erinevaid mudeleid.

Selles õpetuses pakun avastada ühte neist lahendustest: Satochipi.

## Satochipi tutvustus

Satochip on riistvarakott kaardi kujul, millel on *EAL6+* sertifitseeritud kiip, mis on väga kõrge turvastandard (*NXP JCOP*). Selle toodab Belgia ettevõte.

![SATOCHIP](assets/notext/01.webp)

See nutikaart müüakse hinnaga 25 €, mis on väga soodne võrreldes teiste turul olevate riistvarakottidega. Kiip on turvaelement, mis tagab väga hea vastupanu füüsilistele rünnakutele. Lisaks on selle kood avatud lähtekoodiga (*AGPLv3*).
Siiski, oma formaadi tõttu ei paku Satochip nii palju võimalusi kui teised riistvarad. Ilmselgelt ei ole sellel akut, kaamerat ega mikro-SD kaardilugejat, kuna see on kaart. Minu arvates on selle suurim puudus riistvarakotil ekraani puudumine, mis muudab selle teatud tüüpi kaugrünnakute suhtes haavatavamaks. Tõepoolest, see sunnib kasutajat pimesi allkirjastama ja usaldama seda, mida nad näevad oma arvutiekraanil.

Hoolimata oma piirangutest, jääb Satochip huvitavaks oma soodsa hinna tõttu. See rahakott võib eriti olla kasulik kulutuste rahakoti turvalisuse tõstmiseks lisaks säästurahakotile, mida kaitseb ekraaniga varustatud riistvarakott. Samuti on see hea lahendus neile, kes hoiavad väikeseid bitcoini summasid ja ei soovi investeerida sadu eurosid keerukamasse seadmesse. Lisaks võivad Satochipide kasutamine multisig konfiguratsioonides või potentsiaalselt tulevikus ajalukuga rahakottide süsteemides pakkuda huvitavaid eeliseid.

Satochipi ettevõte pakub ka 2 muud toodet. On olemas Satodime, mis on kandekaart, mis on mõeldud bitcoinide offline salvestamiseks, kuid ei võimalda tehinguid. See on omamoodi paberist rahakott, mis on palju turvalisem, mida saab kasutada näiteks kingituse tegemiseks. Lõpuks on olemas Seedkeeper, mis on mnemoonilise fraasi haldur. Seda saab kasutada meie seemne turvaliseks salvestamiseks ilma, et see oleks otse paberile märgitud.

## Kuidas osta Satochipi?
Satochip on müügil [ametlikul veebilehel](https://satochip.io/product/satochip/). Füüsilisest poest ostmiseks leiate [sertifitseeritud edasimüüjate nimekirja](https://satochip.io/resellers/) Satochipi veebilehelt.
Satochipiga oma rahakoti haldustarkvaraga suhtlemiseks on kaks võimalust: NFC kommunikatsiooni kaudu või nutikaardilugeja abil. NFC valiku puhul veenduge, et teie seade ühildub selle tehnoloogiaga või hankige väline NFC lugeja. Satochip töötab standardse sagedusega 13,56 MHz. Vastasel juhul võite osta ka nutikaardilugeja. Ühe leiate Satochipi veebilehelt või mujalt.

![SATOCHIP](assets/notext/02.webp)

## Kuidas seadistada Satochipi Sparrow'ga?

Kui olete oma Satochipi kätte saanud, on esimene samm pakendi kontrollimine, et veenduda, et seda ei ole avatud. Satochipi pakend peaks sisaldama pitserkleebist. Kui see kleebis puudub või on kahjustatud, võib see viidata, et nutikaart on kompromiteeritud ja ei pruugi olla autentne.
![SATOCHIP](assets/notext/03.webp)
Leiate Satochipi seest.

![SATOCHIP](assets/notext/04.webp)

Rahakoti haldamiseks soovitan selles õpetuses kasutada Sparrow'd. Kui teil tarkvara veel ei ole, [külastage ametlikku veebilehte selle allalaadimiseks](https://sparrowwallet.com/download/). Vaadake ka meie õpetust Sparrow Wallet'i kohta (varsti saadaval).

![SATOCHIP](assets/notext/05.webp)

Sisestage oma Satochip nutikaardilugejasse või asetage see NFC lugejale ja ühendage lugeja arvutiga, millel Sparrow on avatud.

![SATOCHIP](assets/notext/06.webp)

Avage Sparrow Wallet ja veenduge, et olete korrektselt ühendatud Bitcoin'i noodiga. Selleks kontrollige alumises paremas nurgas olevat märget: see peaks olema kollane, kui olete ühendatud avaliku noodiga, roheline Bitcoin Core'iga ühenduse puhul või sinine Electrum'i puhul.

![SATOCHIP](assets/notext/07.webp)

Sparrow Wallet'is klõpsake vahekaardil "*File*".

![SATOCHIP](assets/notext/08.webp)

Seejärel menüül "*New Wallet*".

![SATOCHIP](assets/notext/09.webp)

Valige oma rahakotile nimi ja seejärel klõpsake nupul "*Create Wallet*".

![SATOCHIP](assets/notext/10.webp)

Klõpsake nupul "*Connected Hardware Wallet*".

![SATOCHIP](assets/notext/11.webp)

Klõpsake nupul "*Scan...*".

![SATOCHIP](assets/notext/12.webp)

Teie Satochip peaks ilmuma. Klõpsake nupul "*Import Keystore*".

![SATOCHIP](assets/notext/13.webp)

Järgmisena peate seadistama PIN-koodi, et oma Satochipi avada. Valige tugev parool, 4 kuni 16 tähemärgi vahel. Tehke sellest paroolist varukoopia.

Olge teadlikud, et see parool ei ole parafraas. See tähendab, et isegi ilma selle paroolita võimaldab teie mnemooniline fraas vajadusel teie rahakoti tarkvarasse uuesti importida. Parooli kasutatakse ainult juurdepääsu turvamiseks Satochipile endale. See on võrdväärne teiste riistvaraliste rahakottide leitava PIN-koodiga.

Kui parool on sisestatud, klõpsake uuesti nupul "*Import Keystore*".

![SATOCHIP](assets/notext/14.webp)

Märkige parool uuesti üles, seejärel klõpsake nupul "*Initialize*".
![SATOCHIP](assets/notext/15.webp)
Seejärel jõuate aknani, kus saate genereerida oma mnemoonilise fraasi. Klõpsake nupul "*Generate New*".

![SATOCHIP](assets/notext/16.webp)
Tehke oma taastefraasist üks või mitu füüsilist koopiat, kirjutades selle paberile või metallkandjale. Olge teadlikud, et see fraas annab täieliku juurdepääsu teie bitcoinidele ilma lisakaitseta. Seega, kui keegi selle avastab, võiksid nad teie bitcoine koheselt varastada, isegi ilma juurdepääsuta teie Satochipile või selle PIN-koodile. Seetõttu on oluline need varukoopiad turvata. Lisaks võimaldab see fraas teil taastada juurdepääsu oma bitcoinidele juhul, kui kaotate Satochipi, see saab kahjustada või unustate oma PIN-koodi.
![SATOCHIP](assets/notext/17.webp)

Teie Bitcoin rahakott on edukalt loodud.

![SATOCHIP](assets/notext/18.webp)

Klõpsake uuesti nupul "*Import Keystore*".

![SATOCHIP](assets/notext/19.webp)

Teie rahakott on nüüd loodud. Teie privaatvõtmed on nüüd salvestatud teie Satochipi nutikaardile. Klõpsake nupul "*Apply*", et jätkata.

![SATOCHIP](assets/notext/20.webp)

Soovitatav on seadistada lisaparool, et kaitsta Sparrow Walletis hallatavat avalikku teavet, lisaks teie Satochipi PIN-koodile. See parool tagab juurdepääsu turvalisuse Sparrow Walletile, aidates kaitsta teie avalikke võtmeid, aadresse ja tehingute ajalugu volitamata juurdepääsu eest.

![SATOCHIP](assets/notext/21.webp)

Sisestage oma parool mõlemasse välja, seejärel klõpsake nupul "*Set Password*".

![SATOCHIP](assets/notext/22.webp)

Ja ongi kõik, teie Satochip on nüüd Sparrow Walletis seadistatud.

![SATOCHIP](assets/notext/23.webp)

Nüüd, kui teie rahakott on loodud, võite oma Satochipi lahti ühendada. Hoidke seda turvalises kohas!

## Kuidas vastu võtta bitcoine Satochipiga?

Oma rahakotis olles klõpsake vahekaardil "*Receive*".

![SATOCHIP](assets/notext/24.webp)

Sparrow Wallet genereerib teie rahakotile aadressi. Tavaliselt soovitatakse teiste riistvaraliste rahakottide puhul klõpsata nupul "*Display Address*", et aadressi otse seadme ekraanil kontrollida. Kahjuks pole see võimalus Satochipiga saadaval, kuid veenduge, et kasutate seda oma teiste rahakottide jaoks.

![SATOCHIP](assets/notext/25.webp)

Võite lisada "*Label*"i, et kirjeldada bitcoine, mis selle aadressiga turvatakse. See on hea tava, mis aitab teil paremini hallata oma UTXO-sid.

![SATOCHIP](assets/notext/26.webp)

Lisateabe saamiseks sildistamise kohta soovitan samuti tutvuda selle teise õpetusega:

https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Seejärel võite kasutada seda aadressi bitcoinide vastuvõtmiseks.

![SATOCHIP](assets/notext/27.webp)
## Kuidas saata bitcoine Satochipiga?
Nüüd, kui olete oma esimesed satoshid oma turvalisse rahakotti Satochipiga vastu võtnud, saate neid ka kulutada! Ühendage oma Satochip arvutiga, käivitage Sparrow Wallet ja seejärel minge vahekaardile "*Send*", et koostada uus tehing.

![SATOCHIP](assets/notext/28.webp)
Kui soovite teostada müntide kontrolli, see tähendab, valida spetsiifiliselt, milliseid UTXO-sid tehingus kasutada, minge vahekaardile "*UTXOs*". Valige UTXO-d, mida soovite kulutada, seejärel klõpsake nupul "*Saada Valitud*". Teid suunatakse sama ekraani juurde, mis on vahekaardil "*Saada*", kuid teie valitud UTXO-d on juba tehingu jaoks valitud.
![SATOCHIP](assets/notext/29.webp)

Sisestage sihtkoha aadress. Saate sisestada ka mitu aadressi, klõpsates nupul "*+ Lisa*".

![SATOCHIP](assets/notext/30.webp)

Märkige "*Silt*", et meeles pidada selle kulutuse eesmärki.

![SATOCHIP](assets/notext/31.webp)

Valige sellele aadressile saadetav summa.

![SATOCHIP](assets/notext/32.webp)

Kohandage oma tehingu tasumäära vastavalt praegusele turule.

![SATOCHIP](assets/notext/33.webp)

Veenduge, et kõik teie tehingu parameetrid on õiged, seejärel klõpsake nupul "*Loo Tehing*".

![SATOCHIP](assets/notext/34.webp)

Kui kõik on teie rahuloluks, klõpsake nupul "*Finaliseeri Tehing Allkirjastamiseks*".

![SATOCHIP](assets/notext/35.webp)

Klõpsake nupul "*Allkirjasta*".

![SATOCHIP](assets/notext/36.webp)

Klõpsake uuesti nupul "*Allkirjasta*" oma Satochipi kõrval.

![SATOCHIP](assets/notext/37.webp)

Sisestage oma Satochipi PIN-kood, seejärel klõpsake uuesti nupul "*Allkirjasta*", et oma tehing allkirjastada.

![SATOCHIP](assets/notext/38.webp)

Teie tehing on nüüd allkirjastatud. Klõpsake nupul "*Edasta Tehing*", et see Bitcoin'i võrku edastada.

![SATOCHIP](assets/notext/39.webp)

Seda saate leida Sparrow Wallet'i vahekaardilt "*Tehingud*".

![SATOCHIP](assets/notext/40.webp)

Palju õnne, nüüd olete teadlik, kuidas kasutada Satochipi! Kui leidsite selle õpetuse kasuliku, hindaksin ma allpool pöidla üles. Julgelt jagage seda artiklit oma sotsiaalvõrgustikes. Suur tänu!