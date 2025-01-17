---
name: COLDCARD Q - edasijõudnud
description: COLDCARD Q täiustatud võimaluste kasutamine
---
![cover](assets/cover.webp)

Eelmises õppematerjalis käsitlesime COLDCARD Q algkonfiguratsiooni ja selle põhifunktsioone algajatele. Kui olete oma COLDCARD Q alles kätte saanud ja pole seda veel seadistada, soovitan enne siin jätkamist alustada sellest õpetusest:

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3
See uus õpetus on pühendatud COLDCARD Q täiustatud võimalustele, mis on mõeldud edasijõudnutele ja paranoilistele kasutajatele. Tegelikult eristuvad COLDCARDid teistest riistvaralistest rahakottidest paljude täiustatud turvaelementide poolest. Loomulikult ei pea te kõiki neid võimalusi kasutama. Valige lihtsalt need, mis sobivad teie turvastrateegiaga.

**Hoiatus**, mõnede nende täiustatud valikute ebaõige kasutamine võib põhjustada teie bitcoinide kaotuse või riistvaralise rahakoti hävimise. Seetõttu soovitan tungivalt lugeda hoolikalt iga valiku kohta antud nõuandeid ja selgitusi.

Enne alustamist veenduge, et teil on juurdepääs 12- või 24-sõnalise mnemofraasi füüsilisele varukoopiale, ja kontrollige selle kehtivust järgmise menüü kaudu: `Advanced/Tööriistad > Danger Zone > Seed Functions > View Seed Words` (Edasijõudnud/Tööriistad > Ohutsoon > Seed Functions > View Seed Words).

![CCQ](assets/fr/01.webp)

## BIP39 paroolifraas

Kui te ei tea, mis on BIP39 parool, või kui teile ei ole täiesti selge, kuidas see töötab, siis soovitan tungivalt eelnevalt tutvuda selle õpetusega, mis katab teoreetilised alused, mis on vajalikud parooli kasutamisega seotud riskide mõistmiseks:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Pidage meeles, et kui olete oma rahakotis seadistanud salasõna, ei piisa ainult teie mnemoonikast, et taastada juurdepääs oma bitcoinidele. Teil on vaja nii mnemoonikat kui ka paroolifraasi. Veelgi enam, peate sisestama paroolfraasi iga kord, kui avate oma COLDCARDi Q. See suurendab turvalisust, sest ilma paroolfraasita on füüsiline juurdepääs COLDCARDile ja PIN-koodi teadmine ebapiisav.

COLDCARDi puhul on teil kaks võimalust oma salasõna haldamiseks:

1. **Klassikaline sisestamine:** Sisestate salasõna käsitsi iga kord, kui kasutate oma riistvaralist rahakotti, nagu teete seda ka teiste riistvaraliste rahakottide puhul. COLDCARD Q lihtsustab seda ülesannet täieliku klaviatuuri abil.

2. **Võidate valida, kas soovite oma salasõna krüpteerida ja salvestada selle microSD-kaardile. Sellisel juhul peate microSD-kaardi iga kord COLDCARD Q-sse sisestama, kui seda kasutate. Pange tähele, et see microSD-kaart töötab ainult teie COLDCARD Q-s ja ei ole varukoopia. Seetõttu on väga oluline, et te hoiaksite oma salasõna koopiat ka füüsilisel andmekandjal, näiteks paberil või metallist.

BIP39 salasõna määramiseks avage menüü "*Passphrase*".

![CCQ](assets/fr/02.webp)

Sisestage oma salasõna klaviatuuri abil. Valige kindlasti tugev parool (pikk ja juhuslik) ja tehke füüsiline varukoopia.

![CCQ](assets/fr/03.webp)

Kui olete määranud oma salasõna, näitab COLDCARD Q teile selle salasõnaga seotud uue rahakoti põhivõtme sõrmejälge. Salvestage see sõrmejälg kindlasti. Kui sisestate tulevikus seadme kasutamisel uuesti oma paroolfraasi, saate kontrollida, kas kuvatav sõrmejälg vastab teie poolt salvestatud sõrmejäljele. See kontroll tagab, et te ei ole oma paroolfraasi sisestamisel viga teinud.

![CCQ](assets/fr/04.webp)

Nüüd saate vajutada "*ENTER*", et rakendada seda paroolifraasi oma mnemofraasile ja aktiveerida uus rahakott. Kui eelistate selle tunnusfraasi salvestada microSD-kaardile, sisestage kaart vastavasse pessa ja vajutage "*1*".

![CCQ](assets/fr/05.webp)

Teie salasõna on nüüd rakendatud. Võtmejälg ilmub avakuvale ja ekraani ülaossa.

![CCQ](assets/fr/06.webp)

Iga kord, kui avate COLDCARD Q lukustuse, peate sisenema menüüsse "*Passphrase*" ja sisestama oma salasõna samamoodi nagu eespool, et rakendada seda seadmesse salvestatud mnemooniale ja pääseda ligi õigele Bitcoini rahakotile.

![CCQ](assets/fr/07.webp)

Kui olete salvestanud salasõna microSD-kaardile, sisestage see iga kord, kui kasutate seda, COLDCARDi ja avage menüü "*Passphrase*". COLDCARD laeb salasõna otse microSD-kaardilt, nii et te ei pea seda käsitsi sisestama. Vajutage nupule "*Restore Saved*".

![CCQ](assets/fr/08.webp)

Kontrollige, et sisestatud salasõna pikkus ja esimene täht oleksid õiged.

![CCQ](assets/fr/09.webp)

Kinnitage, et kuvatav sõrmejälg vastab teie rahakoti sõrmejäljele, ja klõpsake nuppu "*Restore*".

![CCQ](assets/fr/10.webp)

Pidage meeles, et paroolifraasi kasutamine tähendab, et peate importima oma rahakoti haldustarkvarasse (näiteks Sparrow Wallet) uue võtmekomplekti, mis on tuletatud teie mnemoonilise fraasi ja paroolifraasi kombinatsioonist. Selleks järgige selle teise õpetuse sammu "*Uue rahakoti konfigureerimine Sparrow's*" :

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3
## Lukustusvõimaluste avamine

COLDCARDid saavad kasu ka paljudest seadme avamise võimalustest. Uurime nende täiustatud võimaluste kohta lähemalt.

### Trikk PIN-koodid

Trikk-PIN-kood on seadme algse konfigureerimise ajal määratud PIN-koodist erinev teisene PIN-kood. Seda koodi kasutatakse konkreetsete eelkonfigureeritud toimingute käivitamiseks kohe, kui see sisestatakse COLDCARDi sisselülitamisel. Saate konfigureerida mitu Trick PIN-koodi, millest igaüks on seotud erineva toiminguga. Need funktsioonid võimaldavad teil kohandada COLDCARDi oma isikliku turvastrateegiaga. Need on eriti kasulikud füüsilise sunduse korral, näiteks röövimise ajal (mida Bitcoini kogukonnas nimetatakse tavaliselt "*5 dollari võtmega rünnakuks*").

Trikk-PINi aktiveerimiseks ja selle seostamiseks tegevusega avage menüü "Seaded > Sisselogimise seaded > Trikk-PINid".

![CCQ](assets/fr/11.webp)

Valige "*Uue triki lisamine*".

![CCQ](assets/fr/12.webp)

Seadistage PIN-kood, mis on seotud toiminguga, ja ärge unustage seda salvestada.

![CCQ](assets/fr/13.webp)

Seejärel valige toiming, mis toimuks automaatselt iga kord, kui sisestate selle Trikk-PINi. Siin on nimekiri PIN-koodi jaoks saadaval olevatest toimingutest:


- "*Mütsike ise*: See tegevus hävitab mõlemad COLDCARD Q kiibid, kui Trick PIN sisestatakse, muutes seadme täiesti kasutuskõlbmatuks. Seejärel on seda võimatu edasi müüa, taaskasutada või isegi Coinkite'ile tagastada. Seade muutub pöördumatult igaveseks. Seda funktsiooni saab kasutada röövimise korral, et veenda ründaja, et ta ei pääse kunagi ligi teie bitcoinidele. **Pöörake tähelepanu**: ilma füüsilise varukoopiata oma mnemofraasist ja mis tahes paroolfraasist on teie bitcoinid jäädavalt kadunud.

![CCQ](assets/fr/14.webp)


- "*Puhasta seemne*": See menüü pakub mitmeid toiminguid seemne kustutamiseks, st COLDCARDi lähtestamiseks ilma seda hävitamata. Erinevalt valikust "*Brick Self*" on võimalik seadet uuesti konfigureerida, kasutades oma mälulause varukoopiat. Kuid ilma selle varukoopiana lähevad teie bitcoinid kaduma. Siin on saadaval olevad valikud:
 - "*Wipe & Reboot* : Eemaldab seemne ja taaskäivitab COLDCARDi, ilma et ekraanil kuvataks mingit teavet.
 - "*Silent Wipe*": Tühjendab seemne vaikselt ja avab COLDCARDi juhuslikus võltsitud rahakotis, nagu poleks midagi juhtunud.
 - "*Puhasta -> Rahakott*": Eemaldab seemne diskreetselt ja vabastab COLDCARDi lukustuse eelkonfigureeritud sekundaarses rahakotis, mis on mõeldud peibutisena. See rahakott võib sisaldada väikest osa teie bitcoin-säästudest, et rahuldada ründaja.
 - "*Saage pühkida, stopp*": Kustutab seemne ja kuvab ekraanil teate `Seed on pühitud, Stop`.

![CCQ](assets/fr/15.webp)


- "*Duress rahakott*": Trikk PIN-kood avab BIP85 abil seemnest tuletatud rahakoti. Seda sekundaarset rahakotti saab kasutada söödana, et rahuldada ründaja. COLDCARD käitub nii, nagu oleks tegemist tõelise rahakotiga, kuid ilma peamise PIN-koodita (mis erineb Trick PIN-koodist) ei pääse ründaja kunagi ligi tõelisele rahakotile. Selle strateegia eesmärk on panna inimesed uskuma, et Trikk-PINiga seotud rahakott on ainus olemasolev rahakott.

![CCQ](assets/fr/16.webp)


- "*Login Countdown*": See menüü rühmitab tegevusi, mille puhul on enne nende täitmist loendur. **Hoiatus**, mõned neist võivad hävitada teie seadme või põhjustada bitcoinide kaotuse. Siin on saadaval olevad alltegevused:
 - "*Wipe & Countdown* : Tühjendab seemne COLDCARDi mälust, seejärel alustab ühe tunni pikkust tagasiarvestust. Ilma mälumärki või salasõna salvestamata lähevad bitcoinid kaduma. See valik on mõeldud selleks, et ründaja arvab, et seade vabastatakse loenduse lõppedes, kuid tegelikult lähtestatakse see tehaseseadetele.
 - "*Countdown & Brick*": Käivitab ühe tunni pikkuse loenduri, mille lõppedes COLDCARD hävitab oma kaks turvalist kiipi, muutes selle lõplikult kasutuskõlbmatuks. Ilma varundamata on teie bitcoinid kadunud. See toiming on mõeldud ründaja petmiseks, kes arvab, et ootab avamist, kuigi tegelikult hävitab seade end ise.
 - "*Just Countdown* : Käivitab lihtsa ühe tunni pikkuse loenduri, mille järel COLDCARD taaskäivitub ilma edasise tegevuseta. Seeme ei kustutata ja seade jääb puutumatuks. Olge ettevaatlik, et mitte segi ajada seda tegevust järgnevates punktides käsitletava valikuga "*Login Countdown*", mis lisab peamise PIN-koodi juurde tagasiarvamise, andes samal ajal juurdepääsu tegelikule rahakotile.

![CCQ](assets/fr/17.webp)


- "*Vaate tühi*": See tegevus muudab COLDCARDi tühjaks, jättes mulje, et seemne on kustutatud. Tegelikkuses ei juhtu midagi ja seemne jääb alles. See simuleerib kasutamata või tühistatud COLDCARDi.

![CCQ](assets/fr/18.webp)


- "*Just Reboot* : Trikk-PIN-i kasutamisel COLDCARD lihtsalt taaskäivitub. Muid toiminguid ei tehta.

![CCQ](assets/fr/19.webp)


- "*Delta režiim*": See keerukas tegevus, mis on reserveeritud kogenud kasutajatele, on mõeldud väga keeruliste sundrünnakute tõrjumiseks, olgu need siis riigi või privilegeeritud teavet omava sugulase poolt. Kui delta-režiim on aktiveeritud, annab COLDCARD juurdepääsu tegelikule rahakotile, võimaldades ründajal navigeerida ja kontrollida, et tegemist on õige rahakotiga. Tehingu allkirjad on aga blokeeritud, mis takistab bitcoinide ülekandmist. Lisaks sellele on juurdepääs mnemofraasile blokeeritud ja igasugune katse seda välja otsida toob kaasa selle kustutamise. Usaldusväärsuse suurendamiseks peab Delta-režiimiga kasutatav trikk-PIN olema sama eesliide kui tegelikul PIN-koodil (et kuvada samu andmepüügivastaseid sõnu), kuid järelliide peab olema erinev.

![CCQ](assets/fr/20.webp)

Kui olete tegevuse valinud, kinnitage oma valik.

![CCQ](assets/fr/21.webp)

Seejärel saate vaadata kõiki konfigureeritud Trikk-PIN-koode spetsiaalses menüüs.

![CCQ](assets/fr/22.webp)

Valides olemasoleva Trikk-PINi, saate kontrollida sellega seotud tegevust. Saate selle ka varjata käsuga "*Hide Trick*", muutes selle Trick PINi menüüs nähtamatuks. Saate selle kustutada, klõpsates "*Delete Trick*", või muuta PIN-koodi, säilitades samal ajal sellega seotud tegevuse, kasutades "*Change PIN*".

![CCQ](assets/fr/23.webp)

Menüüs "*Trikk-PIN*" saadaval olev valik "*Lisata, kui valesti*" võimaldab teil konfigureerida konkreetse tegevuse, mis käivitub automaatselt pärast teatud arvu valesid PIN-koodi sisestamise katseid. Lubatud katsete arvu saab seadistamise ajal määrata.

### Scramble võtmed

Valik Scramble Keys võimaldab teil PIN-koodi sisestamisel klahvinuppudel kuvatavaid numbreid segada. See funktsioon kaitseb teie PIN-koodi konfidentsiaalsust isegi siis, kui teid jälgivad inimesed või kaamerad.

Selle valiku aktiveerimiseks avage menüü "Seadistused > Sisselogimise seaded > Klahvide segamine".

![CCQ](assets/fr/24.webp)

Valige valik "*Scramble Keys*".

![CCQ](assets/fr/25.webp)

Nüüdsest alates määratakse COLDCARD Q lukustuse avamisel klahvistikule juhuslikult uued numbrid iga kord, kui te neid kasutate.

![CCQ](assets/fr/26.webp)

### Sisselogimise tagasiarvestus

See valik võimaldab teil kehtestada süstemaatilise tagasiarvestuse iga kord, kui püüate oma COLDCARDi avada. Seda saab integreerida teie turvastrateegiasse, viivitades seadmele juurdepääsu varguse korral või kehtestades viivituse enne tehingu allkirjastamist, näiteks enda kaitsmiseks röövimise korral. Kuid see tagasiarvestus kehtib kõigi teie kasutusalade puhul, sealhulgas ka siis, kui kasutate oma COLDCARDi seaduslikult, mis samuti kohustab teid kannatlikkusele. Olge ettevaatlik, et mitte segi ajada seda võimalust toiminguga "*Just Countdown*", mis aktiveerub ainult konkreetse Trikk-PINi kasutamisel.

Selle valiku seadistamiseks avage menüü "Seaded > Sisselogimise seaded > Sisselogimise aeglustumine".

![CCQ](assets/fr/27.webp)

Valige tagasiarvestuse aeg. Näiteks kui valite 1 tund, peate iga COLDCARD Q avamise katse puhul ootama 1 tunni.

![CCQ](assets/fr/28.webp)

Iga kord, kui avate lukustuse, palutakse teil sisestada PIN-kood.

![CCQ](assets/fr/29.webp)

Seejärel oodake loenduri poolt määratud aega.

![CCQ](assets/fr/30.webp)

Tagasiarvamise lõppedes peate seadmele juurdepääsuks uuesti sisestama PIN-koodi.

![CCQ](assets/fr/31.webp)

### Arvuti sisselogimine

See valik võimaldab teil oma COLDCARDi lukustuse avamisel maskeerida kalkulaatoriks. Selle funktsiooni aktiveerimiseks avage menüü "Seaded > Sisselogimise seaded > Kalkulaatori sisselogimine".

![CCQ](assets/fr/32.webp)

Aktiveerige valik, valides selle.

![CCQ](assets/fr/33.webp)

Nüüdsest alates kuvatakse iga kord, kui seade sisse lülitatakse, töötav kalkulaator koos põhikäsklustega.

![CCQ](assets/fr/34.webp)

Näiteks saate arvutada SHA256-hashi "*Plan B Network*".

![CCQ](assets/fr/35.webp)

COLDCARDi avamiseks kalkulaatorirežiimist alustage PIN-koodi eesliite sisestamisega, millele järgneb mõttekriips. Näiteks kui teie PIN-kood on `00-00` (see kood on nõrk ja ainult näide, seega valige tugev PIN-kood), sisestage `00-`. Seejärel kuvab COLDCARD teie kaks andmepüügivastast sõna.

![CCQ](assets/fr/36.webp)

Seejärel sisestage oma täielik PIN-kood, mis on eraldatud tühiku või kriipsuga, näiteks: "00 00".

![CCQ](assets/fr/37.webp)

Seejärel väljub COLDCARD kalkulaatorirežiimist ja avab lukustuse normaalselt.

## COLDCARDi puhas hävitamine

Kui te kavatsete oma COLDCARD Q hävitada, näiteks kuna kasutate nüüd teist riistvaralist rahakotti, on oluline, et seade hävitatakse õigesti. See tagab, et kolmandad isikud ei saa teie rahakotiga seotud teavet taastada.

Sõltuvalt teie vajadustest on teabe hävitamise kolm taset. Enne alustamist veenduge, et teie rahakott on imporditud teise riistvara rahakotti, et teil on juurdepääs kõigile oma rahalistele vahenditele ja eelkõige, et teil on olemas teie mälulause ja mis tahes paroolfraas, mis mõlemad on toimivad. Ilma rahakoti varukoopiana toob teie COLDCARDi hävimine kaasa teie bitcoinide kadumise.

Esimene hävitamise tase seisneb ainult seemne kustutamises. See valik kustutab teie mnemofraasi COLDCARDi mälust, jättes samas seadme funktsionaalseks. See on ideaalne, kui soovite COLDCARD Q-d hiljem uuesti kasutada. Seemne mälust kustutamiseks minge menüüsse `Advanced/Tools > Danger Zone > Seed Functions > Destroy Seed` (Edasijõudnud/Tööriistad > Ohutsoon > Seemne funktsioonid > Seemne hävitamine).

![CCQ](assets/fr/38.webp)

Teine hävitamise tase seisneb COLDCARDi kahe turvalise kiibi püsivas väljalülitamises tarkvara abil. See muudab seadme täielikult kasutuskõlbmatuks. Te ei saa seda edasi müüa, uuesti kasutada ega Coinkite'ile tagastada: see hävitatakse jäädavalt. Jätkamiseks järgige eelmises punktis kirjeldatud samme seoses "*Brick Me*" PIN-koodi, seejärel sisestage see PIN-kood tahtlikult COLDCARDi avamisel.

Kolmas tase hõlmab COLDCARD Q turvaliste komponentide füüsilist hävitamist. Nagu varemgi, muudab see seadme pöördumatult kasutuskõlbmatuks. Selleks tehke puuriga auk seadme paremal ülemisel küljel asuvasse kahte kiibile (kui see on tagurpidi pööratud), mis asub "*SHOOT HERE*" kiri lähedal.

**Tähtsaid ettevaatusabinõusid** :


- Elektrilöögi ohu vältimiseks eemaldage enne seadme käsitsemist patareid seadmest ja ühendage see vooluvõrgust lahti.
- Oodake pärast seadme väljalülitamist paar minutit, enne kui alustate puurimist.
- Teie ohutuse tagamiseks kandke isoleeritud kindaid ja kaitseprille.

![CCQ](assets/fr/39.webp)

Kui kiibid on löödud, ärge püüdke COLDCARDi Q uuesti ühendada.

Palju õnne, nüüd olete COLDCARD Q täiustatud võimalustega kursis!

Kui leidsid selle õpetuse kasulikuks, oleksin väga tänulik, kui jätaksid alla rohelise pöidla. Jaga seda õpetust julgelt oma sotsiaalvõrgustikes. Tänan teid väga!

Soovitan ka seda teist õpetust, kus me arutame CCQ otsese konkurendi, Ledger Flexi kasutamist:

https://planb.network/fr/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a