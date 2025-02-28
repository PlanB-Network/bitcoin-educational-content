---
name: COLDCARD Q
description: COLDCARDi seadistamine ja kasutamine Q
---
![cover](assets/cover.webp)

Riistvaraline rahakott on elektrooniline seade, mis on mõeldud Bitcoini rahakoti privaatvõtmete haldamiseks ja kaitsmiseks. Erinevalt tarkvaralistest rahakottidest (või kuumadest rahakottidest), mis on paigaldatud üldkasutatavatesse masinatesse, mis on sageli ühendatud internetti, võimaldavad riistvaralised rahakotid füüsiliselt isoleerida privaatseid võtmeid, vähendades piraatluse ja varguse ohtu.

Riistvara rahakoti peamine eesmärk on vähendada seadme funktsionaalsust nii palju kui võimalik, et vähendada selle ründepinda. Väiksem ründepind tähendab ka vähem potentsiaalseid ründevektoreid, st vähem nõrku kohti süsteemis, mida ründajad saaksid bitcoinidele juurdepääsu saamiseks ära kasutada.

Soovitatav on kasutada riistvaralist rahakotti oma bitcoinide kaitsmiseks, eriti kui teil on suur kogus, kas absoluutväärtuses või osakaaluna kogu teie varadest.

Riistvara rahakotte kasutatakse koos arvutis või nutitelefonis oleva rahakoti haldustarkvaraga. Viimane haldab tehingute loomist, kuid nende tehingute kehtivaks muutmiseks vajalik krüptograafiline allkiri tehakse ainult riistvara rahakotis. See tähendab, et privaatvõtmed ei ole kunagi avatud potentsiaalselt haavatavale keskkonnale.

Riistvaralised rahakotid pakuvad kasutajale kahekordset kaitset: ühest küljest kindlustavad nad teie bitcoinid kaugrünnakute eest, hoides privaatvõtmeid võrguühenduseta, ning teisest küljest pakuvad nad üldiselt suuremat füüsilist vastupidavust võtmete väljavõtmise katsetele. Just nende kahe turvakriteeriumi alusel saame hinnata ja klassifitseerida turul olevaid erinevaid mudeleid.

Selles õpetuses tutvustan teile ühte sellist lahendust: **COLDCARD Q**.

---
Kuna COLDCARD Q pakub hulgaliselt funktsioone, teen ettepaneku jagada selle kasutamine 2 õppematerjaliks. Selles esimeses õpetuses vaatleme seadme algkonfiguratsiooni ja põhifunktsioone. Seejärel vaatleme teises õpetuses, kuidas kasutada kõiki COLDCARDi täiustatud võimalusi.

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0
---
## COLDCARD Q tutvustamine

COLDCARD Q on ainult Bitcoini riistvara rahakott, mille on välja töötanud Kanada ettevõte Coinkite, mis on tuntud oma eelmiste MK-mudelite poolest. Q on nende seni kõige arenenum toode, mis on positsioneeritud kui ülim Bitcoini riistvaraline rahakott.

COLDCARD Q on varustatud kõigi optimaalseks kasutajakogemuseks vajalike funktsioonidega:


- Suur LCD-ekraan lihtsustab navigeerimist ja kasutamist;
- Täielik QWERTY-klaviatuur;
- Integreeritud kaamera QR-koodide skaneerimiseks;
- Kaks microSD-kaardi pesa ;
- Täielikult isoleeritud toitevõimalus kolme AAA patarei (ei kuulu komplekti) või USB-C kaabli kaudu;
- Kaks turvalist elementi kahelt erinevalt tootjalt lisaturvalisuse tagamiseks;
- Võime suhelda NFC kaudu.

Minu arvates on COLDCARD Q-l ainult kaks puudust. Esiteks on see oma paljude funktsioonide tõttu üsna mahukas, olles peaaegu 13 cm pikk ja 8 cm lai, mis on peaaegu väikese nutitelefoni suurune. Samuti on see akupesa tõttu üsna paks. Kui otsite väiksemat ja mobiilsemat riistvara rahakotti, võiks palju kompaktsem MK4 olla parem valik. Teine puudus on ilmselt seadme hind, mille hind on ametlikul kodulehel **239,99$**, st 72$ rohkem kui MK4, mis paneb Q otsesesse konkurentsi kõrgema hinnaklassi riistvaraliste rahakottidega, nagu Ledger Flex või Foundationi Passport.

![CCQ](assets/fr/001.webp)

Tarkvara osas on COLDCARD Q sama hästi varustatud kui Coinkite'i teised seadmed, millel on palju täiustatud funktsioone:


- Dice Roll genereerida oma taastamise lause ;
- PIN-kood ;
- Tagasiarvestus lõpliku PIN-lukustumiseni ;
- BIP39 salasõna ;
- Lõplik lukustus PIN ;
- Ühenduse tagasiarvestus ;
- SeedXOR;
- BIP85...

Lühidalt öeldes pakub COLDCARD Q paremat kasutajakogemust kui MK4 ja võib olla ideaalne keskastme ja edasijõudnute jaoks, kes soovivad suuremat kasutusmugavust.

COLDCARD Q on müügil [Coinkite'i ametlikul veebisaidil](https://store.coinkite.com/store/coldcard). Seda saab osta ka jaemüüjalt.

## Õpetuse ettevalmistamine

Kui olete oma COLDCARDi kätte saanud, tuleb kõigepealt kontrollida pakendit, et veenduda, et seda ei ole avatud. Kui pakend on kahjustatud, võib see viidata sellele, et riistvara rahakott on kahjustatud ja ei pruugi olla ehtne.

![CCQ](assets/fr/002.webp)

Kui avate karbi, peaksite leidma järgmised esemed:


- COLDCARD Q suletud kotis;
- Kaart oma mnemoonilise fraasi salvestamiseks.

![CCQ](assets/fr/003.webp)

Veenduge, et kott ei ole lahti suletatud või kahjustatud. Samuti kontrollige, et kotil olev number vastaks koti sees oleval paberil olevale numbrile. Hoidke see number edaspidiseks alles.

![CCQ](assets/fr/004.webp)

Kui eelistate COLDCARDi toiteallikana kasutada ilma arvutiga ühendamata (õhuvahe), sisestage kolm AAA-patareid seadme tagaküljele. Teise võimalusena võite ühendada selle arvutiga USB-C kaabli kaudu.

![CCQ](assets/fr/005.webp)

Selle õpetuse jaoks on teil vaja ka Sparrow Wallet'i, et hallata oma Bitcoini rahakotti arvutis. Laadige [Sparrow Wallet] (https://sparrowwallet.com/download/) alla ametlikust veebisaidist. Soovitan tungivalt kontrollida nii selle autentsust (GnuPG abil) kui ka terviklikkust (hashi kaudu) enne paigaldamise jätkamist. Kui te ei tea, kuidas seda teha, järgige seda õpetust:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
## PIN-koodi valik

Nüüd saate oma COLDCARDi sisse lülitada, vajutades vasakus ülanurgas asuvat nuppu.

![CCQ](assets/fr/006.webp)

Vajutage nuppu "*ENTER*", et nõustuda kasutustingimustega.

![CCQ](assets/fr/007.webp)

Seejärel kuvatakse COLDCARD Q ekraani ülaosas number. Veenduge, et see number vastab numbrile, mis on pitseeritud kotil ja koti sees oleval plasttükil. Sellega tagatakse, et teie pakendit ei ole avatud ajavahemikus, mis jääb Coinkite'i pakkimise ja teie avamise vahele. Jätkamiseks vajutage "*ENTER*".

![CCQ](assets/fr/008.webp)

Liikuge menüüsse "*Valige PIN-kood*" ja kinnitage see nupuga "*ENTER*".

![CCQ](assets/fr/009.webp)

Seda PIN-koodi kasutatakse teie COLDCARDi avamiseks. Seega on see kaitse volitamata füüsilise juurdepääsu eest. See PIN-kood ei ole seotud teie rahakoti krüptograafiliste võtmete tuletamisega. Seega, isegi ilma juurdepääsuta sellele PIN-koodile, võimaldab teie mälulause omamine taastada juurdepääsu oma bitcoinidele.

COLDCARDi PIN-koodid jagunevad kaheks osaks: ees- ja järelliide, millest kumbki võib sisaldada 2-6 numbrit, kokku 4-12 numbrit. COLDCARDi avamisel peate kõigepealt sisestama eesliite, misjärel näitab seade teile 2 sõna. Seejärel sisestage järelliide. Need kaks sõna antakse teile selle konfigureerimisetapi käigus ja need tuleks hoolikalt salvestada, sest neid vajate iga kord, kui COLDCARDi lukustust vabastate. Kui lukustuse avamise ajal kuvatavad kaks sõna langevad kokku nendega, mille salvestasite konfigureerimise ajal, kinnitab see, et teie seadet ei ole pärast selle viimast kasutamist ohustatud.

Klõpsake uuesti "*Valige PIN-kood*"

![CCQ](assets/fr/010.webp)

Kinnitage, et olete hoiatusi lugenud.

![CCQ](assets/fr/011.webp)

Nüüd valite oma PIN-koodi. Soovitame pikka, juhuslikku PIN-koodi. Hoidke seda koodi kindlasti teises kohas kui teie COLDCARDi hoidmise kohta. Selle koodi salvestamiseks võite kasutada oma pakis kaasasolevat kaarti.

Sisestage valitud eesliide ja vajutage PIN-koodi esimese osa kinnitamiseks nuppu "*ENTER*".

![CCQ](assets/fr/012.webp)

Seejärel kuvatakse teie ekraanil kaks andmepüügivastast sõna. Salvestage need hoolikalt edaspidiseks kasutamiseks. Nende ülesmärkimiseks võite kasutada oma paketiga kaasasolevat kaarti.

![CCQ](assets/fr/013.webp)

Seejärel sisestage PIN-koodi teine osa ja vajutage "*ENTER*".

![CCQ](assets/fr/014.webp)

Kinnitage oma PIN-kood, sisestades selle teist korda, kontrollides, et kaks andmepüügivastast sõna vastaksid varem salvestatud sõnadele.

![CCQ](assets/fr/015.webp)

Nüüdsest alates kontrollige iga kord, kui avate oma COLDCARDi, et kaks andmepüügivastast sõna, mis ilmuvad ekraanile pärast PIN-koodi eesliite sisestamist, oleksid kehtivad.

## Firmware uuendamine

Kui kasutate seadet esimest korda, on oluline kontrollida ja uuendada püsivara. Selleks minge menüüsse "*Advanced/Tööriistad*".

![CCQ](assets/fr/016.webp)

**Tähtis:** Kui te kavatsete oma püsivara uuendada ja see ei ole teie esimene kord COLDCARDi kasutada (st teil on juba COLDCARDil loodud rahakott), veenduge, et teil on olemas teie mälulause ja et see on toimiv (samuti valikuline paroolifraas, kui see on kohaldatav). See on oluline, et vältida oma bitcoinide kaotamist, kui seadme uuendamise ajal tekib probleem.

Valige "*Upgrade Firmware*".

![CCQ](assets/fr/017.webp)

Valige "*Näita versiooni*".

![CCQ](assets/fr/018.webp)

Saate kontrollida oma COLDCARDi praegust püsivara versiooni. Näiteks minu puhul on versioon "*1.2.3Q*".

![CCQ](assets/fr/019.webp)

Kontrollige [COLDCARDi ametlikul veebisaidil](https://coldcard.com/downloads), kas uuem versioon on saadaval. Uue püsivara allalaadimiseks klõpsake "*Download*".

![CCQ](assets/fr/020.webp)

Siinkohal soovitame tungivalt kontrollida allalaaditud püsivara terviklikkust ja autentsust. Selleks laadige alla [dokument, mis sisaldab kõigi versioonide hash'eid, mille on allkirjastanud arendajad](https://raw.githubusercontent.com/Coldcard/firmware/master/releases/signatures.txt), kontrollige allkirja [arendaja avaliku võtmega](https://keybase.io/dochex) ja veenduge, et allkirjastatud dokumendis märgitud hash vastab veebilehelt alla laaditud püsivara hash'ile. Kui kõik on õige, võite jätkata uuendamist.

Kui te ei ole selle kontrollimise protsessiga tuttav, soovitan teil jälgida seda õpetust:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Võtke microSD-kaart ja kandke sellele püsivara fail (dokument faili `.dfu`). Sisestage microSD-kaart ühte COLDCARDi porti.

![CCQ](assets/fr/021.webp)

Seejärel valige püsivara uuendamise menüüst "*MicroSD-kandjal*".

![CCQ](assets/fr/022.webp)

Valige püsivara vastav fail.

![CCQ](assets/fr/023.webp)

Kinnitage oma valik, vajutades nuppu "*ENTER*".

![CCQ](assets/fr/024.webp)

Palun oodake, kuni püsivara uuendatakse.

![CCQ](assets/fr/025.webp)

Kui värskendus on lõpule viidud, sisestage PIN-kood, et seade avada.

![CCQ](assets/fr/026.webp)

Teie püsivara on nüüd ajakohane.

## COLDCARD Q parameetrid

Soovi korral saate uurida oma COLDCARDi seadeid, avades menüü "*Settings*".

![CCQ](assets/fr/027.webp)

Sellest menüüst leiate mitmesuguseid kohandamisvõimalusi, näiteks ekraani heleduse määramine või vaikimisi mõõtühiku valimine.

![CCQ](assets/fr/028.webp)

Järgmises õpetuses vaatame teisi täiustatud seadeid:

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0
## Bitcoini rahakoti loomine

Nüüd on aeg luua uus Bitcoini rahakott! Selleks peate looma mälulause. Coldcardis on selle fraasi genereerimiseks kolm meetodit:


- Kasutage ainult sisemist juhusliku numbri generaatorit (TRNG);
- Kasutage entroopia lisamiseks TRNG ja täringu veeretamise kombinatsiooni;
- Kasutage ainult täringuviskeid.

**Algaja ja edasijõudnud kasutajatele soovitame kasutada ainult COLDCARDi sisemist juhusliku numbri generaatorit**

Ma ei soovita ainult täringutega mängimist, sest kehv täitmine võib viia ebapiisava entroopiaga lauseni, mis seab ohtu teie rahakoti turvalisuse.

Parim variant on aga kindlasti teine, mis ühendab TRNG kasutamise välise entroopiaallikaga. See meetod tagab minimaalse entroopia, mis on samaväärne ainult TRNG-ga, ning lisab täiendava turvalisuse taseme sisemise generaatori võimaliku rikke korral (vabatahtlikult või mitte). Valides selle võimaluse, mis ühendab TRNG ja täringu viskamise, saate kasu suuremast kontrollist lause genereerimise üle, ilma et suureneksid riskid teiepoolse halva täitmise korral.

Klõpsake nupule "*Uued seemnesõnad*".

![CCQ](assets/fr/029.webp)

Saate valida oma karistuse pikkuse. Soovitan valida 12-sõnalise lause, sest seda on vähem keeruline hallata ja see ei paku vähem portfoolio turvalisust kui 24-sõnaline lause.

![CCQ](assets/fr/030.webp)

Seejärel kuvab COLDCARD teie TRNG-ga genereeritud taastamislauset. Kui soovite lisada täiendavat välist entroopiat, vajutage klahvi "*4*".

![CCQ](assets/fr/031.webp)

See viib teid lehele, kus saate lisada entroopiat täringutega. Tehke nii palju viskamisi kui võimalik (soovitatav on vähemalt 50, kuid vähem ei ole suur probleem, sest te juba saate kasu TRNG entroopiast) ja registreerige tulemused klahvidega "*1*" kuni "*6*". Kui olete lõpetanud, vajutage kinnitamiseks "*ENTER*".

![CCQ](assets/fr/032.webp)

Kuvatakse uus mnemooniline lause, mis põhineb teie poolt äsja esitatud entroopial ja TRNG-l põhineval entroopial.

**Hoiatus: See mnemoonik annab täieliku, piiramatu juurdepääsu kõigile teie bitcoinidele**. Igaüks, kes seda fraasi valdab, võib teie raha varastada, isegi ilma füüsilise juurdepääsuta teie COLDCARDile. 12-sõnaline fraas taastab juurdepääsu teie bitcoinidele, kui teie COLDCARD kaob, varastatakse või puruneb. Seetõttu on väga oluline seda hoolikalt talletada ja turvalises kohas hoida.

Te võite selle kirjutada COLDCARDiga kaasas olevale kartongile või täiendava turvalisuse tagamiseks soovitan selle graveerida roostevabast terasest kandjale, et kaitsta seda tulekahju, üleujutuse või kokkuvarisemise eest. Igal juhul ärge salvestage seda kunagi digitaalsele andmekandjale, sest muidu võite oma bitcoinid kaotada.

Kirjutage ekraanil esitatud sõnad enda valitud füüsilisele kandjale. Sõltuvalt teie turvastrateegiast võite kaaluda, kas teha mitu täielikku füüsilist koopiat lausest (kuid ennekõike ärge jagage seda laiali). Oluline on hoida sõnad nummerdatud ja järjestikku.

Loomulikult **ei tohi te neid sõnu** kunagi internetis jagada, erinevalt sellest õpetusest. Seda näidisportfelli kasutatakse ainult Testnetis ja see kustutatakse õpetuse lõpus.

Pärast sõnade üleskirjutamist vajutage "*ENTER*".

![CCQ](assets/fr/033.webp)

Et veenduda, et olete oma lause õigesti salvestanud, palub süsteem teil teatud sõnu kinnitada. Valige igale sõnale vastav number klahvistikul.

![CCQ](assets/fr/034.webp)

Teie rahakott on nüüd loodud! Ekraani paremas ülemises nurgas näete oma peamise privaatvõtme sõrmejälge. Vajutage "*ENTER*".

![CCQ](assets/fr/035.webp)

Nüüd pääsete oma COLDCARDi peamenüüsse.

![CCQ](assets/fr/036.webp)

## Uue portfelli loomine Sparrow's

Sparrow Wallet'i tarkvara ja teie COLDCARDi vahelise suhtluse loomiseks on mitu võimalust. Kõige lihtsam on kasutada USB-C-kaablit. Kuid vaikimisi on teie COLDCARDi kaabli- ja NFC-side välja lülitatud. Nende taasaktiveerimiseks navigeerige jaotisele "*Settings*", seejärel "*Hardware On/Off*" ja aktiveerige soovitud suhtlusvalik.

![CCQ](assets/fr/037.webp)

Kui eelistate oma COLDCARDi arvutist täiesti eraldatuna hoida, võite valida kaudse "õhulõhega" suhtluse, kasutades QR-koode või microSD-kaarti. Seda meetodit kasutame käesolevas õpetuses.

Minge rubriiki "*Advanced/Tööriistad*".

![CCQ](assets/fr/038.webp)

Valige "*Ekspordi rahakott*".

![CCQ](assets/fr/039.webp)

Seejärel valige "*Sparrow Wallet*".

![CCQ](assets/fr/040.webp)

Vajutage "*ENTER*", et luua konfiguratsioonifail.

![CCQ](assets/fr/041.webp)

Seejärel valige, kuidas see fail Sparrow'le saata. Selles näites olen sisestanud microSD mälupessa "*A*", seega valin nupu "*1*". Te võite kuvada teabe ka QR-koodina oma COLDCARDi ekraanil, vajutades nuppu "*QR*" ja skaneerides seda QR-koodi oma arvuti veebikaameraga.

![CCQ](assets/fr/042.webp)

Käivitage Sparrow Wallet ja hüpake sissejuhatavad leheküljed, et jõuda põhiekraanile. Veenduge, et olete õigesti ühendatud sõlmpunktiga, kontrollides ekraani paremas allosas asuvat lülitit.

![CCQ](assets/fr/043.webp)

On tungivalt soovitatav kasutada oma Bitcoini sõlme. Selle õpetuse jaoks kasutan ma avalikku sõlme (kollane), kuna olen testvõrgus, kuid tootmise jaoks on kõige parem kasutada Bitcoin Core'i lokaalselt (roheline) või Electrumi serverit kauges sõlmes (sinine).

Avage menüü "*Fail*" ja valige "*Uus rahakott*".

![CCQ](assets/fr/044.webp)

Anna oma rahakotile nimi ja klõpsa "*Loo rahakott*".

![CCQ](assets/fr/045.webp)

Valige rippmenüüst "*Skripti tüüp*" skripti tüüp, mis kindlustab teie bitcoinid.

![CCQ](assets/fr/046.webp)

Klõpsake nupule "*Airapped Hardware Wallet*".

![CCQ](assets/fr/047.webp)

Klõpsake vahekaardil "*Coldcard*" nupule "*Scan...*", kui kavatsete skaneerida oma COLDCARDil kuvatavat QR-koodi, või "*Import File...*", et importida fail microSD-lt (see on `.json` fail).

![CCQ](assets/fr/048.webp)

Pärast importimist kontrollige, et Sparrow's kuvatav "*Mastersõrmejälg*" vastab teie COLDCARDil kuvatavale sõrmejäljele. Kinnitage loomine, klõpsates nupule "*Kanna*".

![CCQ](assets/fr/049.webp)

Seadistage tugev parool, et tagada juurdepääs oma Sparrow rahakotile. See parool kaitseb teie avalikke võtmeid, aadresse, silte ja tehingulugu volitamata juurdepääsu eest.

See parool on hea mõte salvestada, et te seda ei unustaks (nt paroolihalduris).

![CCQ](assets/fr/050.webp)

Teie rahakott on nüüd Sparrow Walletis seadistatud.

![CCQ](assets/fr/051.webp)

Enne esimeste bitcoinide saamist oma rahakotti, ** soovitan teil tungivalt teha tühja taastamistesti**. Kirjutage üles mõned võrdlusandmed, näiteks oma xpub, ja seejärel lähtestage oma COLDCARD Q, kui rahakott on veel tühi. Seejärel proovige oma rahakoti taastamist COLDCARDile, kasutades oma paberkandjal varukoopiaid. Kontrollige, kas pärast taastamist loodud xpub vastab sellele, mille te algselt üles kirjutasite. Kui see vastab, võite olla kindel, et teie paberkandjal varukoopiad on usaldusväärsed.

Kui soovite rohkem teada saada, kuidas teha taastamistesti, soovitan teil tutvuda selle teise õpetusega:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
## Bitcoinide vastuvõtmine

Oma esimeste bitcoinide saamiseks alustage COLDCARDi sisselülitamisest ja avamisest.

![CCQ](assets/fr/052.webp)

Klõpsake Sparrow Walletis vahekaardil "*Võta*".

![CCQ](assets/fr/053.webp)

Enne Sparrow Walleti pakutud aadressi kasutamist kontrollige seda oma COLDCARDi ekraanil. See võimaldab teil kinnitada, et Sparrow's kuvatav aadress ei ole võltsitud ja et riistvara rahakotis on tõepoolest isiklik võti, mida on vaja selle aadressiga tagatud bitcoinide hilisemaks kulutamiseks. See aitab teil vältida mitut liiki rünnakuid.

Selle kontrollimiseks klõpsake COLDCARDi menüüs "*Adressiotsing*".

![CCQ](assets/fr/054.webp)

Valige käsikirja tüüp, mida te kasutate Sparrow's. Minu puhul on see Segwit P2WPKH. Ma klõpsan sellel.

![CCQ](assets/fr/055.webp)

Seejärel näete oma erinevaid tuletatud aadresse järjekorras.

![CCQ](assets/fr/056.webp)

Kontrollige Sparrow'ga, et aadress vastab. Minu puhul on aadress koos tuletamise teega `m/84'/1'/0'/0/0` tõepoolest `tb1qwfwwvzssep4wyjg3vsgezmwa037ehvd4fhmjvr` nii Sparrow's kui ka COLDCARDis.

![CCQ](assets/fr/057.webp)

Teine võimalus selle aadressi omandiõiguse kontrollimiseks on skannida selle QR-kood otse Sparrow'sse oma COLDCARDilt. Valige oma COLDCARDi avakuval "*Scan Any QR Code*". Võite kasutada ka klaviatuuri klahvi "*QR*".

![CCQ](assets/fr/058.webp)

Skaneerige Sparrow Wallet'is kuvatava aadressi QR-koodi.

![CCQ](assets/fr/059.webp)

Veenduge, et teie COLDCARDil näidatud aadress vastab Sparrow's näidatud aadressile. Seejärel vajutage nuppu "*1*".

![CCQ](assets/fr/060.webp)

Seega on aadress edukalt kinnitatud.

![CCQ](assets/fr/061.webp)

Nüüd saate lisada "*Label*", et kirjeldada bitcoinide allikat, mida selle aadressiga kaitstakse. See on hea tava, mis võimaldab teil paremini hallata oma UTXOsid.

![CCQ](assets/fr/062.webp)

Lisateabe saamiseks märgistamise kohta soovitan ka seda teist õpetust:

https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52
Seejärel saate seda aadressi kasutada bitcoinide saamiseks.

![CCQ](assets/fr/063.webp)

## Bitcoinide saatmine

Nüüd, kui olete saanud oma esimesed satsid oma COLDCARDiga kaitstud rahakotti, võite neid ka kulutada!

Nagu alati, alustage COLDCARD Q sisselülitamisest ja avamisest, seejärel avage Sparrow Wallet ja minge uue tehingu ettevalmistamiseks vahekaardile "*Saatmine*".

![CCQ](assets/fr/064.webp)

Kui soovite "mündikontrolli", st valida konkreetselt, milliseid UTXOsid tehingus tarbida, minge vahekaardile "*UTXOd*". Valige UTXOd, mida soovite kulutada, ja klõpsake seejärel nupule "*Send Selected*". Teid suunatakse tagasi samale ekraanile vahekaardile "*Send*", kuid teie UTXO-d on juba valitud tehingu jaoks.

![CCQ](assets/fr/065.webp)

Sisestage sihtkoha aadress. Võite sisestada ka mitu aadressi, klõpsates nupule "*+ Lisa*".

![CCQ](assets/fr/066.webp)

Kirjutage "*Silt*", et meeles pidada selle kulu eesmärki.

![CCQ](assets/fr/067.webp)

Valige sellele aadressile saadetav summa.

![CCQ](assets/fr/068.webp)

Kohandage oma tehingu tasumäär vastavalt praegusele turule.

![CCQ](assets/fr/069.webp)

Veenduge, et kõik tehingu parameetrid on õiged, seejärel klõpsake "*Loo tehing*".

![CCQ](assets/fr/070.webp)

Kui olete kõigega rahul, klõpsake nuppu "*Tehingu allkirjastamiseks lõpuleviimine*".

![CCQ](assets/fr/071.webp)

Kui olete oma tehingu Sparrow's üles ehitanud, on aeg see COLDCARDiga allkirjastada. PSBT (allkirjastamata tehingu) edastamiseks seadmesse on teil mitu võimalust. Kui traadiga andmeedastus on lubatud, saate saata tehingu otse USB-C-ühenduse kaudu, nagu te seda teeksite mis tahes muu riistvaralise rahakoti puhul. Sel juhul tuleb teil Sparrow's klõpsata all paremas nurgas asuvat nuppu "*Sign*". Minu näites on see nupp blokeeritud, sest COLDCARD ei ole kaabliga ühendatud.

![CCQ](assets/fr/072.webp)

Kui eelistate säilitada "õhulähedase" ühenduse ilma otsese kontaktita riistvara rahakoti ja arvuti vahel, on teil 2 võimalust. Esimene ja keerulisem võimalus on kasutada microSD-kaarti. Sisestage microSD-kaart arvutisse, salvestage tehing Sparrow nupu "*Save Transaction*" abil, seejärel kandke see kaart oma COLDCARDi porti.

![CCQ](assets/fr/073.webp)

Seejärel avage menüü "*Valmis allkirjastama*".

![CCQ](assets/fr/074.webp)

Vaadake üle oma COLDCARDi tehingu andmed, sealhulgas vastuvõtja aadress, saadetud summa ja tehingutasu.

![CCQ](assets/fr/075.webp)

Kui kõik on õige, vajutage tehingu allkirjastamiseks nuppu "*ENTER*".

![CCQ](assets/fr/076.webp)

Seejärel asetage microSD mälukaart tagasi arvutisse ja klõpsake Sparrow's "*Load Transaction*", et laadida allkirjastatud tehing microSD mälukaardilt. Seejärel saate teha lõpliku kontrolli enne selle üleslaadimist Bitcoini võrku.

![CCQ](assets/fr/077.webp)

Teine meetod oma COLDCARDiga allkirjastamiseks Air-Gapis, mis on palju lihtsam kui microSD-meetod, on PSBT skannimine otse seadme kaamera abil. Valige Sparrow's "*Show QR*".

![CCQ](assets/fr/078.webp)

Valige COLDCARDil "*Scan Any QR Code*". Võite kasutada ka klaviatuuri klahvi "*QR*".

![CCQ](assets/fr/079.webp)

Kasutage COLDCARDi kaamerat, et skaneerida Sparrow'l kuvatavat QR-koodi.

![CCQ](assets/fr/080.webp)

Tehingu üksikasjad ilmuvad uuesti kontrollimiseks. Vajutage "*ENTER*", et allkirjastada, kui kõik on teid rahuldanud.

![CCQ](assets/fr/081.webp)

Seejärel kuvab teie COLDCARD allkirjastatud tehingu QR-koodina. Kasutage selle QR-koodi skaneerimiseks oma arvuti veebikaamerat, valides Sparrow's "*Scan QR*".

![CCQ](assets/fr/082.webp)

Teie allkirjastatud tehing on nüüd Sparrow's nähtav. Kontrollige veelkord, et kõik oleks korrektne, seejärel klõpsake "*Tehingu edastamine*", et seda Bitcoini võrgus edastada.

![CCQ](assets/fr/083.webp)

Saate jälgida oma tehinguid Sparrow Walleti vahekaardil "*Tehingud*".

![CCQ](assets/fr/084.webp)

Palju õnne, te olete nüüd kursis COLDCARD Q ja Sparrow Walleti põhikasutusega!

Kui leidsid selle õpetuse kasulikuks, oleksin väga tänulik, kui jätaksid alla rohelise pöidla. Palun jagage seda õpetust julgelt oma sotsiaalvõrgustikes. Tänan teid väga!

Samuti soovitan vaadata seda teist õpetust, kus me arutame COLDCARD Q täiustatud võimalusi:

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0