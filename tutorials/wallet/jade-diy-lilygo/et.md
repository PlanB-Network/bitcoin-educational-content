---
name: Jade DIY
description: Muutke 15-dollariline arendusplaat täielikult toimivaks Bitcoin riistvaraks wallet
---

![cover](assets/cover.webp)


## Bitcoin Hardware Wallet - Algaja ehitamine


**Auditoorium:** Uudishimulikud ehitajad, kellel on vähe või üldse mitte mingisuguseid kogemusi.


**Kestvus:** 2 tundi (paindlik)


**Tulemused:** Lõpptulemuseks on õpilased:



- Tunnistage omatehtud riistvaraliste rahakottide turvamudelit võrreldes kommertsseadmetega.
- Mikrokontrolleril põhineva allkirjastamise seadme kokkupanek.
- Flashige avatud lähtekoodiga püsivara ja kontrollige koostamise kontrollsummat.
- Allkirjastada ja edastada mainnet tehing, kasutades oma uut seadet.


---

## Abstraktne


See 2-tunnine töötuba õpetab algajatele, kuidas ehitada toimiv Bitcoin riistvara wallet, vilgutades avatud lähtekoodiga Jade'i püsivara 15-dollarilisele LilyGO T-Display plaadile. Õpilased muudavad üldise arendusriistvara 150 dollarit maksvate kommertslike rahakottidega võrreldavaks allkirjastamise seadmeks, õppides turvalisuse põhialuseid pigem praktilise kogemuse kui pelgalt teooria kaudu.


### Filosoofia


Oma allkirjastamisseadme ehitamine ei tähenda ainult raha kokkuhoidu - see tähendab, et peate mõistma oma Bitcoin kaitsvat tehnoloogiat. See töötuba hõlmab "turvalisust mõistmise kaudu", mitte musta kasti usaldust. Komponentide hankimise, avatud lähtekoodiga püsivara väljalülitamise ja entroopia ise genereerimise abil vähendavad õpilased tarneahela riske, õppides samal ajal kriitiliselt hindama turvanõudeid. Eesmärgiks on teadlik iseseisvus: õpilased peaksid mõistma nii oma omatehtud seadme võimsust kui ka piiranguid võrreldes karastatud kommertsalternatiividega.


---

## Kontseptsiooni algatus (15 min)


### Mis on isehooldus ja miks on see oluline?


Bitcoin loodi selleks, et kaotada vajadus usaldusväärsete kolmandate osapoolte, näiteks pankade ja ettevõtete järele meie rahasüsteemis. Usalduse asemel kasutab bitcoin matemaatikat, füüsikat ja krüptograafiat, et võimaldada igaühel omada ja kontrollida oma raha, ilma et ta vajaks kellegi luba.


See toimib nii, et bitcoin eksisteerib globaalses digitaalses pearaamatus, mida nimetatakse plokiahelaks ehk bitcoin timechain, mis on avalik ja läbipaistev pearaamat, mida juhivad arvutid, mitte tsentraliseeritud pearaamat nagu pangakonto.


Oluline on mõista, et selleks, et Bitcoini ühest kohast teise liigutada, peate selle tehingu allkirjastama niinimetatud privaatvõtmega. Mõelge sellele kui truubi avamisele parooliga ja bitcoinide teisaldamisele kellegi teise truubi. Bitcoin annab sulle õiguse hoida selle võlvkambri võtmeid ise, selle asemel, et usaldada, et pank liigutab sinu raha sinu eest.


Suure võimuga kaasneb suur vastutus, kui kaotate oma võtmed ja teie vahendid on igaveseks kadunud. Niimoodi võite mõelda, et truubi võtmed on nagu raha ise. Kuigi võtmed ei ole sama asi, mis bitcoin, on need mehhanism, mille abil teie raha liigub, ja seetõttu on nende kaitsmine äärmiselt oluline. Seepärast ütleme "mitte teie võtmed, mitte teie mündid".


Mõiste self-custody võib kõlada segadusttekitavana, kuid see tähendab vaid seda, et sa hoiad oma isiklikke võtmeid ja kontrollid oma bitcoini. Kui te ei hoia seda võtit, siis usaldate, et keegi teine hoiab seda teie eest. Kui teie bitcoin on ETFis või börsil (Mt. Gox, FTX, Coinbase, Binance jne), siis te ei oma bitcoini, vaid te omate nõudeõigust bitcoinile. Sellega kaasnevad igasugused riskid, nagu näiteks see, et börsid häkitakse ja teie bitcoin kaotatakse või et ettevõtted laenavad teie raha välja ja annavad teile ainult murdosa reservi. Lisaks oleks usaldusväärsetel kolmandatel isikutel täielik kontroll teie raha üle ja nad võiksid piirata või külmutada väljavõtteid.


![image](assets/fr/01.webp)


Iseseisva hoolduse puhul eemaldate võrdusest usalduse. Keegi ei saa teie raha külmutada ega tehingut keelata, te saate saata raha üle piiri, kellele iganes ja igal ajal ning te ei vaja pangakontot, isikut tõendavat dokumenti ega kellegi heakskiitu. Keegi ei saa teid peatada, tsenseerida ega varastada, avades bitcoini kui vabadusraha täieliku võimsuse. Seepärast ütleme, et bitcoiniga saate olla iseenda pank.


Bitcoin loodi usalduse ja rahaga manipuleerimise probleemi lahendamiseks, meie praegusest süsteemist väljumiseks, kuid väljumine toimib ainult siis, kui võtate võtmed. Seepärast ongi enesehooldus nii oluline.


### Mis on Wallet?


Mõiste wallet on veidi ekslik ja võib seetõttu segadust tekitada. Jah, on tõsi, et bitcoin wallet, nagu ka füüsiline wallet, salvestab väärtust. Kuid peamine erinevus seisneb selles, et bitcoini rahakotid ei säilita tegelikult ühtegi bitcoini.


Bitcoin eksisteerib ainult avaliku plokiahela pearaamatu kirjetena ehk küberruumi metafoorsetes võlvides. Pidage meeles, et bitcoinide liigutamiseks peate kasutama oma võtmeid, et avada võlv ja liigutada münte kuhugi mujale, privaatvõtmed on see, mida kasutatakse bitcoinide kulutamiseks. Kui teete tehingu oma wallet-ga, kasutate te tegelikult vaid oma võtmeid, et tehingut allkirjastada. Nii tõendate, et raha kuulub teile ja teil on õigus neid münte kulutada.


Bitcoin rahakotid hoiavad tegelikult lihtsalt teie isiklikke võtmeid, seega oleks täpsem nimetada neid võtmehoidjateks.


### Hot vs Cold rahakotid


Hot wallet on teie telefonis või arvutis olev tarkvararakendus. See on ühendatud internetti, seega on seda lihtsam kasutada ja kiirem tehingute allkirjastamine, kuid see tähendab ka, et see on rohkem avatud häkkeritele, pahavara ja andmepüügile. Seda nimetatakse "kuumaks", sest see on ühendatud internetti, on ühendatud ja sisse lülitatud. Näiteks võib tuua telefoni wallet või brauseri wallet.


Teisest küljest on külm wallet ehk riistvaraline wallet seade, mis loob ja salvestab teie võtme võrguühenduseta. See kaotab võimaluse, et keegi saaks teie raha häkkida, ja on pikaajaliste säästude jaoks palju turvalisem, kuid see on seade, mida on vaja iga tehingu allkirjastamiseks ja mis võib olla vähem mugav.


### Hardware Wallet ohumudel


Riistvaralised rahakotid on olemas selleks, et lahendada põhiprobleem: kuidas allkirjastada Bitcoin tehinguid, ilma et teie privaatvõtmed oleksid avatud internetiühendusega arvutile, mida pahavara või kaugründajad võivad ohustada? Põhiline ohumudel eeldab, et teie igapäevane sülearvuti või telefon on potentsiaalselt vaenulik. Riistvaraline wallet loob isoleeritud keskkonna, kus privaatvõtmed ei lahku kunagi seadmest ja tehingu allkirjastamine toimub secure element või mikrokontrolleris, mis edastab vastuvõtvale arvutile tagasi ainult allkirja, mitte võtit ennast. Isegi kui teie arvuti on täielikult ohustatud, ei saa ründaja teie Bitcoin varastada ilma füüsilise juurdepääsuta seadmele ja teie PIN-koodile.


Riistvaralised rahakotid toovad aga kaasa oma ohud. Te peate usaldama, et tootja ei ole sisse viinud tagauksi, et tarneahelat ei ole võltsitud ja et juhuslike numbrite genereerimine on tõeliselt juhuslik. Füüsilised ründajad võivad kõrvalkanalrünnakute või kiibiga manipuleerimise kaudu võtmeid välja võtta ning keegi, kellel on ajutine juurdepääs, võib teie seadet muuta. Oma riistvara wallet ehitamine aitab teil neid kompromisse mõista - teete otsuseid turvaliste elementide ja üldotstarbeliste mikrokontrollerite vahel, kuidas kontrollida tehinguid ekraanil ja kuidas kaitsta nii kaug- kui ka füüsiliste ohtude eest. Eesmärgiks ei ole täiuslik turvalisus, vaid arusaamine, milliste ohtude eest te kaitsete ja millised jäävad alles.


### Põhimõisted



- Entroopia ja seed laused:** Teie wallet on ainult nii turvaline kui juhuslikkus, mis selle sünnitab. Me segame seadme juhusliku numbrigeneraatori inimsõbralike trikkidega, nagu täringuvisked, teisendame selle entroopia 12- või 24-sõnaliseks [BIP39 fraasiks](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) ja lahkume ruumist kirjaliku või metallist varundusega, mida te usaldate.
- Seemne fraasi hügieen:** Käsitle seed nagu oma säästude peavõti. Ärge kunagi kirjutage sõnu telefoni või arvutisse - keyloggerid, ekraanipildid ja pilve varukoopiad võivad seda igaveseks lekitada. Hoidke fraasi offline, hoidke seda kusagil, kuhu ainult teil on juurdepääs, ja harjutage selle valjusti tagasi lugemist enne lahkumist.
- Turvaline element + mikrokontroller:** Mõelge secure element-st kui truumist ja mikrokontrollerist kui ajust. secure element valvab privaatseid võtmeid võltsimiskindlalt, samas kui mikrokontroller tegeleb ekraani, nuppude ja firmavara loogikaga. Pange tähele, et riistvaralistel rahakottidel, mida me täna ehitame, ei ole secure element. See ei tähenda, et see on ebaturvaline, vaid lihtsalt, et sellel on üks kaitsetase vähem.
- Firmware usaldamine:** Firmware on wallet nähtamatu operatsioonisüsteem. Laadige alati alla märgistatud versioonidest, kontrollige avaldatud hashi ja mõistke, et reprodutseeritavad buildid võimaldavad mitmel inimesel sama koodi kompileerida ja jõuda täpselt sama binaarkoodini. Kui kontrollsumma ei vasta, siis ei allkirjasta.


---

## Mida me ehitame?


Me võtame üldise riistvara, LilyGo T-Display, ja vilgutame sellele Jade SDK püsivara. [Jade Plus](https://blockstream.com/jade/jade-plus/) on avatud lähtekoodiga wallet, mis tavaliselt maksab 150 dollarit:


![image](assets/fr/02.webp)


Täna, me vilgub nende püsivara peale $15 riistvara asemel.


### Mida osta


![image](assets/fr/03.webp)



- LilyGO T-Display (16MB koos kestaga, mudel K164)** - [Telli otse LilyGOst](https://lilygo.cc/products/t-display?srsltid=AfmBOornob5U3FzZifuSwBBOdeXKcdPDqkYEnAVYKBLdzl0BPyNglGBR) umbes 15 dollariga. See ESP32-plaat pakub ekraani, nuppe ja USB-liidest, mis peegeldavad Blockstream'i Jade Plus'i. Pardal ESP32 sisaldab ka Wi-Fi ja Bluetooth raadiosid; me tarnime firmware, mis hoiab neid välja lülitatud, kuid nad kujundavad teie ohumudelit, sest pahatahtlik kood võib neid tagasi sisse lülitada.
- USB-C kaabel** - võtke kaasa andmesideühendusega kaabel, et saaksite firmware'i flashida ja tahvlit otse sülearvutist varustada (sobib täiesti hästi klassis kasutamiseks).


### Miks ehitada oma Hardware Wallet?



- Säästate ligikaudu 135 dollarit võrreldes kaubandusliku seadme ostmisega.
- Ehitage mugavust püsivara vilkumise, turvaliste elementide ja wallet hügieeniga.
- Looge täiendavaid allkirjastamisseadmeid, et levitada säästu mitme rahakoti vahel.
- Vähendage tarneahela riske, hankides ja monteerides kõik komponendid ise.
- Pidage meeles Loppi mantrat: suveräänsus ja mugavus on alati vastuolus.


## Füüsiline seadistus


### Valmistage oma juhtum ette


Sul on kaks võimalust oma LilyGO T-Display tahvli paigutamiseks: 3D-prinditud korpus või ametlik LilyGO korpus. Trükitud korpuse saab leida ja printida [see mudel](https://www.printables.com/model/119144-lilygo-ttgo-t-display-enclosure). See pakub teie seadmele kerget ja kohandatavat kestat.


![image](assets/fr/04.webp)


Teise võimalusena saate kasutada ametlikku LilyGO korpust, mis pakub veidi teistsugust sobivust ja viimistlust, pakkudes tugevamat kaitset ja lihvitud välimust.


![image](assets/fr/05.webp)


Pange tähele, et trükitud ja ametlikud korpused erinevad veidi disaini ja kooste poolest. Ükskõik millise variandi te valite, veenduge, et tahvel on korralikult paigutatud korpuse sisse, et vältida lahtiseid ühendusi või kahjustusi.


### Kontrollida juhatust


Enne jätkamist kontrollige hoolikalt oma LilyGO T-Displei tahvlit nähtavate defektide või prahi suhtes. Kontrollige, et ekraan, nupud ja USB-C port oleksid puhtad ja ilma tolmu või jooteplekideta. Käsitsege plaati ettevaatlikult ja järgige elektrostaatilise laengu (ESD) ohutust, maandades end või kasutades ESD-rihma, et vältida tundlike komponentide kahjustamist.


### Ühendage oma sülearvutiga


Ühendage LilyGO tahvel sülearvutiga andmesidevõimelise USB-C kaabli abil. See ühendus annab voolu ja võimaldab teil püsivara väljalülitada.


Käivitamisel kuvatakse järgmine ekraan:


![image](assets/fr/06.webp)



Kui LilyGO on sisse lülitatud, kuvatakse värvikatsekraan, mis läbib ühevärvilisi värve. See kinnitab, et ekraan ja tahvel toimivad enne püsivara väljalülitamist õigesti.


Kui värvitest on lõppenud, lülitub ekraan vaikimisi olekusse, mis näitab, et tahvel on valmis järgmisteks sammudeks ehitamisprotsessis.


![image](assets/fr/07.webp)


## Lihtne tee või Hard tee


Riistvara wallet püsivara väljalülitamiseks on kaks peamist lähenemisviisi: lihtne ja raske viis. Lihtne viis kasutab eelkonfigureeritud tööriistu või veebipõhiseid flashereid, mis laadivad püsivara seadmesse automaatselt ja minimaalse sisendiga. See meetod sobib ideaalselt algajatele, kes soovivad kiiret võitu või eelistavad vältida vigade kõrvaldamise ja käsurea interaktsiooni keerukust. See lihtsustab protsessi ja viib teid kiiremini tööle, muutes selle kättesaadavaks neile, kes on uued manussüsteemide arenduse või riistvara rahakotiga.


Raske viis seevastu hõlmab püsivara väljalülitamist käsitsi, kasutades käsurea tööriistu. See lähenemisviis nõuab püsivara allkirjade ja kontrollsummade kontrollimist, et tagada autentsus ja terviklikkus, mis annab teile sügavama arusaama väljalülitamise protsessist ja sellest, kuidas püsivara riistvaraga suhtleb. Kuigi see nõuab rohkem vaeva ja terminali käskudega tutvumist, pakub see suuremat kontrolli, läbipaistvust ja usaldust seadme turvalisuse suhtes.


Mõlemal meetodil on omad kompromissid: lihtne viis ohverdab teatava usalduse ja arusaamise kiiruse ja mugavuse eest, samas kui raske viis nõuab rohkem aega ja tehnilisi oskusi, kuid tasub teid paindlikkuse ja tugevama arusaamisega aluseks olevast tehnoloogiast. Juhendajad peaksid julgustama õpilasi valima teed, mis vastab kõige paremini nende mugavustasemele ja uudishimule, edendades nii usaldust kui ka uurimist.


## Lihtne viis


Lihtsaim viis ESP32 flashimiseks



- Mine ametlikule Blockstream Githubile: [https://github.com/Blockstream/jadediyflasher](https://github.com/Blockstream/jadediyflasher)


![image](assets/fr/08.webp)



- Saate lähtekoodifaili alla laadida ja veebilehte lokaalselt käivitada, kuid GitHubis on see juba olemas aadressil [https://blockstream.github.io/jadediyflasher/](https://blockstream.github.io/jadediyflasher/). GitHub edastab HTML-i, CSS-i, JavaScripti jne. otse teie brauserisse, nii et saate seadet ilma arendajatööriistade paigaldamiseta flashida.


![image](assets/fr/09.webp)



- Avage rippmenüü (vaikimisi on tõenäoliselt `M5Stack Core2`) ja valige oma arendusplaat - selle klassi jaoks valige `LILYGO T-Display`.


![image](assets/fr/10.webp)



- Kui klõpsate välklambi, siis ilmub see. Selleks, et teada saada, milline seade on LILYGO, ühendage lilygo lahti ja ühendage see tagasi. Com port, et lilygo ilmub ja kaob. Klõpsake COM-porti, millesse Jade on ühendatud


![image](assets/fr/11.webp)



- See on see, et progress bar peaks ilmuma ja kui see on lõpetanud oma valmis seadistada seda


## Jade Wallet seadistamine


Kui püsivara on edukalt väljalülitatud, on teie LilyGO T-Display nüüd täielikult toimiv Jade riistvara wallet. Selles jaotises tutvustatakse teile esialgset seadistamisprotsessi, alates seed fraasi genereerimisest kuni seadme ühendamiseni wallet tarkvaraga, nagu Sparrow või Blockstream Green mobiilirakendusega.


### Esialgne käivitamine ja seadme seadistamine



- Kui LilyGO on endiselt USB-C kaudu sülearvutiga ühendatud, peaks Jade'i püsivara automaatselt käivituma. Näete, et ekraanile ilmub Jade'i logo.



- Sisestage seadistusrežiim:** Seade esitab teile algmenüü. Kasutage navigeerimiseks kahte füüsilist nuppu:
 - Vasakpoolne nupp:** Liikumine üles/tagasi
 - Parem nupp:** Liikumine alla/ettepoole
 - Mõlemad nupud samaaegselt:** Valige/kinnitage



- Valige "Setup":** Navigeerige valiku "Setup" juurde ja vajutage kinnitamiseks mõlemat nuppu. Seade juhatab teid läbi esialgse seadistamisprotsessi.


### Teie Wallet loomine



- Valige "Begin Setup":** Seade palub teil alustada wallet loomise protsessi. Kinnitage oma valik.



- Valige "Create New Wallet":** Teile kuvatakse kaks võimalust:
 - Loo uus Wallet:** Loob uue seed fraasi (valige see töökoja jaoks)
 - Wallet taastamine:** Olemasoleva wallet taastamine seed fraasist (edasijõudnutele)



- Valige "Create New Wallet" ja kinnitage.



- Entroopia genereerimine:** Seade kasutab krüptograafilise entroopia loomiseks oma juhusliku numbri generaatorit. See protsess võtab aega paar sekundit, kuna seade kogub juhuslikkust mitmest allikast.


### Oma seemnefraasi salvestamine



- Kirjutage oma seed fraas:** Seade kuvab nüüd 12-sõnalist BIP39 seed fraasi, üks sõna korraga. See on kogu protsessi kõige kriitilisem samm.


**Tähtsad turvameetmed:**


- Kirjutage iga sõna selgelt paberile (kasutage võimaluse korral kaasasolevaid seed lausekaarte)
- Kontrollige iga sõna kirjutamise ajal kaks korda
- Ärge kunagi pildistage seed fraasi oma telefoniga
- Ärge kunagi kirjutage sõnu mis tahes arvutisse või telefoni
- Hoidke oma seed fraas privaatne - ärge jagage oma ekraani ega näidake seda teistele



- seed fraasi kontrollimine:** Pärast kõigi 12 sõna üleskirjutamist palub seade teil kinnitada mitu sõna fraasist, et veenduda, et olete need õigesti salvestanud. Kasutage nuppe, et valida iga üleskutse jaoks õige sõna.


**Profi nõuanne:** Enne edasiliikumist harjutage oma seed lause valjusti (vaikselt, et teised ei kuuleks) ette lugemist. See aitab tabada võimalikke käekirjavigu või ebaselgusi.


### Ühendusmeetod



- Valige ühenduse tüüp:** Jade'i püsivara toetab kahte ühendusmeetodit:
 - USB:** Juhtmega ühendus USB-C kaabli kaudu (soovitatav selle töökoja jaoks)
 - Bluetooth:** Juhtmevaba ühendus mobiilseadmetega



- Valige esialgu **USB**, kuna see on kõige lihtsam valik töölaua wallet tarkvara jaoks ja ei tekita traadita rünnaku vektoreid.



- Seadme nimetamine:** Jade kuvab unikaalset identifikaatorit, näiteks "Connect Jade A7D924". See identifikaator aitab teil eristada mitut riistvaralist rahakotti, kui te lõpuks ehitate rohkem kui ühe. Soovi korral märkige see identifikaator üles.


### Ühendamine Wallet tarkvaraga


Teil on nüüd kaks peamist võimalust oma äsja loodud riistvaraga wallet liidestumiseks: Blockstream Green mobiilirakendus (kasutamiseks teel olles) või Sparrow Wallet (kasutamiseks lauaarvutis, millel on rohkem täiustatud funktsioone). Selles töötoas keskendume Sparrow Wallet-le, kuna see pakub paremat ülevaadet Bitcoin tehingute tehnilistest üksikasjadest.


#### Võimalus 1: Blockstream Green mobiilirakendus (Kiirstart)


Kui soovite oma seadet kiiresti testida mobiilseadmega:



- Lae alla rakendus **Blockstream Green** App Store'ist (iOS) või Google Play'st (Android)
- Avage rakendus ja valige "Connect Hardware Wallet"
- Valige toetatavate seadmete nimekirjast "Jade"
- Ühendage oma Jade telefoniga USB-C USB-C kaabli abil (või USB-C Lightning adapteriga iPhone 15+ puhul)
- Järgige ekraanil kuvatavaid juhiseid, et luua oma esimene wallet


**Märkus Liquid kohta:** Blockstream Green rakendus toetab nii Bitcoin kui ka Liquid (Bitcoin külgahela). Kui kasutate Liquid funktsioone, võidakse teil paluda "eksportida master blinding key" - see võimaldab rakendusel näha tehingusummasid Liquid võrgus, mis muidu on konfidentsiaalsed. Selle töötoa puhul võite Liquid funktsioonid vahele jätta ja keskenduda tavalistele Bitcoin tehingutele.


#### Valik 2: Sparrow Wallet (soovitatav töökojale)


Sparrow Wallet on võimas töölauarakendus, mis annab teile üksikasjaliku kontrolli oma Bitcoin tehingute üle ja ühendub sujuvalt teie Jade'i riistvaraga wallet.


**Installatsioon:**



- Lae Sparrow Wallet alla ametlikust veebisaidist: [sparrowwallet.com](https://sparrowwallet.com)
- Kontrollida allalaadimise allkirja (üksikasjad on esitatud Sparrow dokumentatsioonis)
- Installige ja käivitage rakendus


**Jade ühendamine Sparrow-ga:**



- Mine Sparrow-s **Faili → Uus Wallet**
- Andke oma wallet-le nimi (nt "My Jade Wallet")
- Klõpsake nuppu **Kinnitatud Hardware Wallet**
- Sparrow peaks automaatselt tuvastama teie ühendatud Jade'i seadme
- Nõudmise korral kinnitage ühendus Jade ekraanil, vajutades mõlemat nuppu
- Valige soovitud skripti tüüp:
 - Native Segwit (P2WPKH):** Soovitatav algajatele - madalaimad tasud, suurim ühilduvus kaasaegsete rahakottidega
 - Nested Segwit (P2SH-P2WPKH):** Ühilduvuse tagamiseks vanemate teenustega
 - Taproot (P2TR):** Kõige arenenum, pakub parimat privaatsust ja madalaimaid tasusid, kuid nõuab tipptasemel wallet tuge
- Klõpsake **Import Keystore**, et ühendus lõpule viia


** Sparrow serveriühenduse seadistamine:**


Enne kui saate näha oma saldot või edastada tehinguid, peab Sparrow võtma ühendust Bitcoin sõlme, et saada plokiahela andmeid. Teil on mitu võimalust, millest igaühel on erinevad kompromissid mugavuse, privaatsuse ja usalduse vahel:



- Avalik Electrum Server (kõige lihtsam, kõige vähem privaatne):** Ühendub avaliku serveriga, mida haldab kolmas osapool. Kiiresti häälestatav, kuid server näeb teie wallet aadresse ja võib need teie IP-aadressiga siduda. Hea testimiseks testneti kaudu.
 - Mine Sparrow-s **Tööriistad → Eelistused → Server**
 - Valige **Public Server** ja valige server nimekirjast
 - Klõpsake **Testiühendus**, et kontrollida



- Bitcoin Core või Knots Node (kõige isiklikum, kõige rohkem tööd):** Käivitage oma täielik Bitcoin sõlme. See on privaatsuse ja kontrollimise kuldstandard, kuna te valideerite iga tehingu ise ja ei usalda kellegi teise serverit. See nõuab aga kogu plokiahela (~600 GB) allalaadimist ja oma sõlme sünkroonimist.
 - Bitcoin Core või Knots paigaldamine ja sünkroniseerimine
 - Mine Sparrow-s **Tööriistad → Eelistused → Server**
 - Valige **Bitcoin Core või Knots** ja sisestage oma sõlme ühendusandmed



- Privaatne Electrum Server (hea tasakaal):** Hosta oma Electrum serverit (nagu Fulcrum või Electrs), mis on ühendatud Bitcoin Core või Knotsi sõlme. Pakub täielikku privaatsust, ilma et oleks vaja käivitada Sparrow samas masinas kui teie sõlme.
 - Seadistage Electrum server, mis osutab teie Bitcoin Core või Knots sõlme
 - Mine Sparrow-s **Tööriistad → Eelistused → Server**
 - Valige **Privaatne Electrum** ja sisestage oma serveri URL-aadress


Selle töökoja jaoks on **avaliku Electrum Server** kasutamine täiesti piisav testvõrgustiku tehingute tegemiseks. Tootmiskeskkonnas, kus on reaalsed rahalised vahendid, peaksite kaaluma oma sõlme käitamist või usaldatud privaatsuse tagamiseks usaldusliku privaatserveri kasutamist.


#### Valik 3: Blockstream Green Desktop App (Kiirstart)


Blockstream Green on tarkvara JadeDIY seadistamise lõpetamiseks ja see peab olema koos töölauaversiooniga



- Hangi ametlik Blockstream rakendus - see on link nende veebisaidilt. Kui olete seal, klõpsake [Download now](https://blockstream.com/app/).


![image](assets/fr/12.webp)



- Sõltuvalt sellest, kuhu teie allalaadimised lähevad, on fail tõenäoliselt teie kaustas Downloads. Kontrollige seda ja topeltklõpsake käivitatavale failile, et tarkvara paigaldada.


![image](assets/fr/13.webp)



- Paigaldaja käivitamiseks peate võib-olla andma administraatori õigused. Pärast seda avaneb aken, mis peaks välja nägema järgmise pildi sarnane - klõpsake **Järgmine**.


![image](assets/fr/14.webp)



- Valige, kuhu soovite paigaldatud rakendust paigutada (asukoht koos teie teiste programmidega või kusagil, kus seda on lihtne leida), seejärel klõpsake **Järgmine**.


![image](assets/fr/15.webp)



- Installeerija küsib otsetee nime. Sisestage üks või jätke vaikimisi valik, seejärel klõpsake nuppu **Järgmine**.


![image](assets/fr/16.webp)



- Kui soovite töölaua otsetee, märkige ruut, vastasel juhul klõpsake **Järgmine**.


![image](assets/fr/17.webp)



- Lõpuks klõpsake **Install** ja oodake paar minutit, kuni paigaldus on lõpule viidud.


![image](assets/fr/18.webp)



- Edasiminekuriba peaks täituma lõpuni.


![image](assets/fr/19.webp)



- Kui see lõpeb, ilmub uus lehekülg - klõpsake **Finish**.


![image](assets/fr/20.webp)



- Leidke oma äsja paigaldatud Blockstream rakendus (näide on näidatud Windows 11 Start menüüs).


![image](assets/fr/21.webp)



- Kui leiate selle, klõpsake käivitamiseks - peaks ilmuma käivituskuva.


### Seadistuse kontrollimine


Kui see on ühendatud Sparrow (või mõne teise wallet rakendusega):



- Kontrollige oma aadresse:** Sparrow kuvab teie seed fraasist tuletatud vastuvõtuaadressid. Saate aadressi kontrollida oma Jade-seadmes, kui lähete Sparrow-s vahekaardile "Receive" ja klõpsate "Display Address" - aadress peaks ilmuma nii teie arvuti ekraanile kui ka Jade'i ekraanile.



- Looge vastuvõtuaadress:** Klõpsake Sparrows vahekaardil **Vastuvõtmine** ja kopeerige oma esimene Bitcoin vastuvõtuaadress.



- Valmis tehinguteks:** Teie riistvara wallet on nüüd täielikult konfigureeritud ja valmis Bitcoin tehingute vastuvõtmiseks ja allkirjastamiseks. Jätkake järgmise jaotisega, et harjutada testnet-tehingu allkirjastamist.



---

### Kiire seadistamise kontrollnimekiri



- Jade firmware käivitub edukalt
- Uus wallet, mis on loodud 12-sõnalise seed fraasiga
- Selgelt üles kirjutatud ja kontrollitud seemnefraas
- USB-ühenduse režiim valitud
- Wallet tarkvara (Sparrow) on paigaldatud ja ühendatud
- Konfigureeritud serveriühendus (avalik Electrum mainnet jaoks)
- Esimene vastuvõtuaadress luuakse ja kontrollitakse seadmes



---

**MIT litsents**


**Copyright (c) 2025 The Bitcoin Network NYC**


Käesolevaga antakse tasuta luba igale isikule, kes omandab käesoleva tarkvara ja sellega seotud dokumentatsioonifailide (edaspidi "tarkvara") koopia, tegeleda tarkvaraga piiranguteta, sealhulgas, kuid mitte ainult, õigus kasutada, kopeerida, muuta, ühendada, avaldada, levitada, all-litsentsida ja/või müüa tarkvara koopiaid, ning lubada isikutel, kellele tarkvara on antud, seda teha järgmistel tingimustel:


Ülaltoodud autoriõiguse teatis ja käesolev loateade peavad sisalduma kõigis tarkvara koopiates või olulistes osades.


TARKVARA ANTAKSE "NAGU ON", ILMA IGASUGUSE GARANTIITA, EI SELGESÕNALISE EGA KAUDSE, SEALHULGAS, KUID MITTE AINULT, GARANTIID KAUBELDAVUSE, SOBIVUSE JA MITTEKAITSTAVUSE KOHTA. AUTORID VÕI AUTORIÕIGUSTE OMANIKUD EI VASTUTA MINGIL JUHUL ÜHEGI NÕUDE, KAHJU VÕI MUU VASTUTUSE EEST, OLGU SEE SIIS LEPINGULINE, DELIKTILINE VÕI MUU, MIS TULENEB TARKVARAST VÕI SELLE KASUTAMISEST VÕI SELLEGA SEOTUD TEGEVUSEST.


---