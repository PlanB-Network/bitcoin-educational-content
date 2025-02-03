---
name: RGB protokoll, teooriast praktikasse
goal: Omandada RGB mõistmiseks ja kasutamiseks vajalikud oskused
objectives: 

  - Mõista RGB-protokolli põhimõisteid
  - Kliendipoolse valideerimise ja Bitcoini kohustuste põhimõtete tundmaõppimine
  - Õppige, kuidas RGB lepinguid luua, hallata ja üle kanda
  - Kuidas kasutada RGB-ühilduvat Lightning-sõlme

---
# RGB-protokolli avastamine

Sukeldu RGB maailma, protokolli, mis on loodud digitaalsete õiguste rakendamiseks ja jõustamiseks lepingute ja varade kujul, mis põhinevad Bitcoini plokiahela konsensusreeglitel ja toimingutel. See põhjalik koolituskursus juhatab teid läbi RGB tehniliste ja praktiliste aluste, alates "kliendipoolse valideerimise" ja "ühekordsete pitserite" mõistetest kuni täiustatud arukate lepingute rakendamiseni.

Struktureeritud, samm-sammulise programmi abil avastate kliendipoolse valideerimise mehhanismid, Bitcoini deterministlikud kohustused ja kasutajate vahelised suhtlemismustrid. Õppige, kuidas luua, hallata ja edastada RGB-märke Bitcoinis või Lightning Networkis.

Olenemata sellest, kas olete arendaja, Bitcoini entusiast või lihtsalt uudishimulik, et selle tehnoloogia kohta rohkem teada saada, annab see koolituskursus teile vahendid ja teadmised, mida vajate RGB omandamiseks ja innovaatiliste lahenduste loomiseks Bitcoini abil.

Kursus põhineb Fulgur'Ventures'i korraldatud elusseminaril, mida õpetavad kolm tuntud õpetajat ja RGB eksperti.

+++
# Sissejuhatus

<partId>c6f7a70f-d894-595f-8c0a-b54759778839</partId>

## Kursuse esitlus

<chapterId>cf2f087b-6c6b-5037-8f98-94fc9f1d7f46</chapterId>

Tere kõigile ja tere tulemast sellele koolituskursusele, mis on pühendatud RGB-le, kliendipoolselt valideeritud aruka lepingu süsteemile, mis töötab Bitcoini ja Lightning Networki peal. Selle kursuse ülesehitus on loodud selleks, et võimaldada selle keerulise teema põhjalikku uurimist. Kursus on korraldatud järgmiselt:

**1. jagu: teooria

Esimene osa on pühendatud teoreetilistele mõistetele, mis on vajalikud kliendipoolse valideerimise ja RGB põhimõtete mõistmiseks. Nagu te selle kursuse käigus avastate, tutvustab RGB hulgaliselt tehnilisi mõisteid, mida Bitcoinis tavaliselt ei nähta. Selles jaotises leiate ka sõnastiku, mis sisaldab kõigi RGB-protokollile omaste terminite määratlusi.

** 2. jagu: Praktika

Teises osas keskendutakse 1. osas vaadeldud teoreetiliste kontseptsioonide rakendamisele. Õpime, kuidas luua ja manipuleerida RGB-lepinguid. Samuti näeme, kuidas nende vahenditega programmeerida. Need kaks esimest osa esitab Maxim Orlovsky.

**Jagu 3: Rakendused

Viimase osa juhivad teised kõnelejad, kes tutvustavad konkreetseid RGB-põhiseid rakendusi, et tuua esile reaalseid kasutusjuhtumeid.

---
See koolituskursus kasvas algselt välja kahenädalasest edasijõudnute arenduslaagrist Viareggios, Toscanas, mille korraldas [Fulgur'Ventures] (https://fulgur.ventures/). Esimene nädal, mis keskendus Rustile ja SDK-dele, on leitav sellest teisest kursusest:

https://planb.network/courses/lnp402
Sellel kursusel keskendume stardilaagri teisele nädalale, mis keskendub RGB-le.

**Nädal 1 - LNP402:**

![RGB-Bitcoin](assets/fr/001.webp)

**2. nädal - praegune koolitus CSV402:**

![RGB-Bitcoin](assets/fr/002.webp)

Suur tänu nende kursuste korraldajatele ja 3 õpetajale, kes osalesid:


- Maxim Orlovski: *Ex Tenebrae sententia sapiens dominabitur astris. Cypher, AI, robootika, transhumanism. RGB, Prime, Radiant ja lnp_bp, mycitadel_io & cyphernet_io* looja;
- Hunter Trujilo: *Rust, Bitcoin, Lightning, RGB* ;
- Federico Tenga: *Tenego Tenego: Ma teen oma panuse, et muuta maailm tsüfferpunki düstoopiaks. Praegu töötan RGB kallal Bitfinexis*.

Selle koolituskursuse kirjaliku versiooni koostamisel kasutati 2 peamist allikat:


- Videod Maxim Orlovsky, Hunter Trujilo ja Frederico Tenga seminarist Lightning Bootcampis ;
- RGB dokumentatsioon, mille koostamist sponsoreeris [Bitfinex](https://www.bitfinex.com/).

# RGB teoreetiliselt

<partId>80e797ee-3f33-599f-ab82-e82eeee08219</partId>

## Sissejuhatus hajutatud arvutuskontseptsioonidesse

<chapterId>f52f8af5-5d7c-588b-b56d-99b97176204b</chapterId>

![video](https://youtu.be/AF2XbifPGXM)

RGB on protokoll, mis on loodud digitaalsete õiguste (lepingute ja varade kujul) kohaldamiseks ja jõustamiseks skaleeritaval ja konfidentsiaalsel viisil, mis põhineb Bitcoini plokiahela konsensusreeglitel ja toimingutel. Käesoleva esimese peatüki eesmärk on tutvustada RGB-protokolliga seotud põhimõisteid ja terminoloogiat, rõhutades eelkõige selle tihedat seost selliste põhiliste hajutatud arvutuskontseptsioonide nagu kliendipoolne valideerimine ja ühekordsed pitsatid.

Selles peatükis uurime **jaotatud konsensussüsteemide** põhialuseid ja vaatame, kuidas RGB sobib sellesse tehnoloogiaperekonda. Samuti tutvustame peamisi põhimõtteid, mis aitavad meil mõista, miks RGB eesmärk on olla laiendatav ja sõltumatu Bitcoini enda konsensusmehhanismist, tuginedes samas vajadusel sellele.

### Sissejuhatus

Jaotatud andmetöötlus, mis on arvutiteaduse eriharu, uurib protokolle, mida kasutatakse teabe levitamiseks ja töötlemiseks sõlmede võrgus. Need sõlmed ja protokollide reeglid moodustavad koos selle, mida nimetatakse hajutatud süsteemiks. Sellist süsteemi iseloomustavate oluliste omaduste hulka kuuluvad :


- **Võimekus kontrollida ja valideerida** teatavaid andmeid sõltumatult iga sõlme poolt;
- Sõlmede võimalus konstrueerida (sõltuvalt protokollist) täielik või osaline vaade teabele. Need vaated on jaotatud süsteemi **seisundid**;
- Toimingute **kronoloogiline järjekord**, et andmed oleksid usaldusväärselt ajatempliga varustatud ja et sündmuste (seisundite järjestuse) osas valitseks üksmeel.

Eelkõige hõlmab mõiste **konsensus** hajutatud süsteemis kahte aspekti:


- Seisundi muutuste kehtivuse** tunnustamine (vastavalt protokolli reeglitele);
- **Kokkulepe nende oleku muutuste järjekorras**, mis muudab võimatuks ümberkirjutamise või tagurpidi valideeritud operatsioonide tagantjärele teostamise (seda tuntakse Bitcoinis ka kui "topeltkulutuste kaitset").

Satoshi Nakamoto võttis Bitcoiniga kasutusele esimese funktsionaalse, lubadusteta jaotatud konsensusmehhanismi, tänu plokiahela andmestruktuuri ja Proof-of-Work (PoW) algoritmi kombineeritud kasutamisele. Selles süsteemis sõltub plokkide ajaloo usaldusväärsus sõlmede (kaevurite) poolt sellele pühendatud arvutusvõimsusest. Bitcoin on seega oluline ja ajalooline näide kõigile avatud hajutatud konsensussüsteemist (*vabaduseta*).

Plokiahela ja hajutatud arvutuste maailmas võime eristada kahte põhilist paradigmat: ***blockchain*** traditsioonilises mõttes ja ***riigi kanalid***, mille parim näide tootmises on Lightning Network. Plokiahelat defineeritakse kui kronoloogiliselt järjestatud sündmuste registrit, mida reprodutseeritakse konsensuse alusel avatud, lubadusteta võrgus. Seevastu olekukanalid on vastastikused kanalid, mis võimaldavad kahel (või enamal) osalejal säilitada ajakohastatud olekut väljaspool ahelat, kasutades plokiahelat ainult nende kanalite avamisel ja sulgemisel.

Bitcoini kontekstis olete kahtlemata tuttav kaevandamise, detsentraliseerimise ja tehingute lõplikkuse põhimõtetega plokiahelas, samuti sellega, kuidas maksekanalid töötavad. RGBga võtame kasutusele uue paradigma nimega **Kliendipoolne valideerimine**, mis erinevalt plokiahela või Lightningist seisneb nutilepingu oleku üleminekute lokaalses (kliendipoolses) salvestamises ja valideerimises. See erineb teistest "DeFi" tehnikatest (_rollups_, _plasma_, _ARK_ jne) ka selle poolest, et kliendipoolne valideerimine tugineb plokiahelale, et vältida topeltkulutusi ja omada ajatemplisüsteemi, hoides samal ajal ahelaväliseid olekuid ja üleminekuid käsitlevat registrit ainult asjaomaste osalejate juures.

![RGB-Bitcoin](assets/fr/003.webp)

Hiljem tutvustame ka üht olulist terminit: mõistet "**stash**", mis viitab kliendipoolsete andmete kogumile, mis on vajalik lepingu seisundi säilitamiseks, kuna neid andmeid ei reprodutseerita globaalselt üle võrgu. Lõpuks vaatleme RGB, kliendipoolset valideerimist kasutava protokolli põhjendusi ja seda, miks see täiendab olemasolevaid lähenemisviise (plokiahela ja olekukanalid).

### Trilemmasid hajutatud andmetöötluses

Et mõista, kuidas kliendipoolne valideerimine ja RGB lahendavad probleeme, mida plokiahelad ja Lightning ei lahenda, avastame 3 peamist "kolmikmängu" hajutatud andmetöötluses:


- Skaleeritavus, detsentraliseerimine, privaatsus** ;
- CAP** teoreem (järjepidevus, kättesaadavus, partitsiooni taluvus) ;
- CIA** trilemma (konfidentsiaalsus, terviklikkus, kättesaadavus).

#### 1. Skaleeritavus, detsentraliseerimine ja konfidentsiaalsus


- Blockchain (Bitcoin)**

Blockchain on väga detsentraliseeritud, kuid mitte väga skaleeritav. Veelgi enam, kuna kõik on ülemaailmses, avalikus registris, on konfidentsiaalsus piiratud. Konfidentsiaalsust saab püüda parandada nullteabe tehnoloogiate abil (konfidentsiaalsed tehingud, mimblewimble-skeemid jne), kuid avalik ahel ei suuda tehingugraafikut varjata.


- Välk/riiklikud kanalid**

Riigi kanalid (nagu Lightning Network) on paremini skaleeritavad ja privaatsemad kui plokiahelad, kuna tehingud toimuvad väljaspool ahelat. Kuid kohustus teatavatest elementidest (rahastamistehingud, võrgu topoloogia) avalikult teada anda ja võrguliikluse jälgimine võib osaliselt ohustada konfidentsiaalsust. Ka detsentraliseerimine kannatab: marsruutimine on sularahamahukas ja suuremad sõlmed võivad muutuda tsentraliseerimispunktideks. Just seda nähtust hakkame Lightningi puhul nägema.


- Kliendipoolne valideerimine (RGB)**

See uus paradigma on veelgi skaleeritavam ja konfidentsiaalsem, sest me ei saa mitte ainult integreerida nullsaladuse tõendamise tehnikat, vaid meil puudub ka tehingute globaalne graaf, sest kogu registrit ei ole kellegi käes. Teisest küljest tähendab see ka teatavat kompromissi detsentraliseerimise osas: nutilepingu emitendil võib olla keskne roll (nagu Ethereumis "lepingu kasutuselevõtja"). Erinevalt plokiahelast salvestate ja valideerite kliendipoolse valideerimise puhul siiski ainult need lepingud, millest olete huvitatud, mis parandab skaleeritavust, kuna ei ole vaja alla laadida ja kontrollida kõiki olemasolevaid olekuid.

![RGB-Bitcoin](assets/fr/004.webp)

#### 2. CAP teoreem (järjepidevus, kättesaadavus, partitsiooni taluvus)

CAP-teoreem rõhutab, et hajutatud süsteemil on võimatu rahuldada samaaegselt järjepidevust (*Konsistentsus*), kättesaadavust (*Kättesaadavus*) ja jaotustaluvust (*Partitsiooni taluvus*).


- Blockchain**

Plokiahelad eelistavad järjepidevust ja kättesaadavust, kuid ei saa hästi hakkama võrgu jagunemisega: kui sa ei näe plokki, ei saa sa tegutseda ja omada sama vaateid kui kogu võrk.


- Välk** (prantsuse keeles)

Riigi kanalite süsteemil on kättesaadavuse ja jagunemise tolerantsus (kuna kaks sõlme võivad jääda üksteisega ühendatuks isegi siis, kui võrk on killustunud), kuid üldine järjepidevus sõltub kanalite avamisest ja sulgemisest plokiahelas.


- Kliendipoolne valideerimine (RGB)**

Selline süsteem nagu RGB pakub järjepidevust (iga osaleja valideerib oma andmed lokaalselt, ilma mitmetähenduslikkuseta) ja partitsioneerimistolerantsust (te säilitate oma andmeid iseseisvalt), kuid ei taga üldist kättesaadavust (igaüks peab veenduma, et tal on asjakohased ajalootükid olemas, ja mõned osalejad võivad midagi mitte avaldada või lõpetada teatud teabe jagamise).

![RGB-Bitcoin](assets/fr/005.webp)

#### 3. CIA trilemma (konfidentsiaalsus, terviklikkus, kättesaadavus)

See kolmikprobleem tuletab meile meelde, et konfidentsiaalsust, terviklikkust ja kättesaadavust ei saa optimeerida üheaegselt. Blockchain, Lightning ja kliendipoolne valideerimine langevad sellesse tasakaalu erinevalt. Mõte on selles, et ükski süsteem ei suuda kõike pakkuda; on vaja kombineerida mitu lähenemisviisi (plokiahela ajatempli, Lightningi sünkroonne lähenemine ja kohalik valideerimine RGBga), et saada sidus pakett, mis pakub häid tagatisi igas mõõtmes.

![RGB-Bitcoin](assets/fr/006.webp)

### Blokiahela roll ja jagamise mõiste

Plokiahel (antud juhul Bitcoin) on eelkõige _aja tembeldamise_ mehhanism ja kaitse topeltkulutuste vastu. Selle asemel, et sisestada aruka lepingu või detsentraliseeritud süsteemi täielikud andmed, lisame lihtsalt **krüptograafilised kohustused** (_commitments_) tehingutele (kliendipoolse valideerimise mõttes, mida me nimetame "olekute üleminekuteks"). Seega :


- Vabastame plokiahelat suurest hulgast andmetest ja loogikast;
- Iga kasutaja salvestab ainult oma lepingu osa jaoks vajaliku ajaloo (oma "*shard*"), mitte ei kopeeri globaalset seisu.

Jagamine on kontseptsioon, mis pärineb hajutatud andmebaasidest (nt MySQL sotsiaalvõrgustike nagu Facebook või Twitter jaoks). Andmemahu ja sünkroniseerimisviivituse probleemi lahendamiseks jagatakse andmebaas _shardideks_ (USA, Euroopa, Aasia jne). Iga segment on lokaalselt järjepidev ja ainult osaliselt sünkroniseeritud teistega.

RGB-tüüpi arukate lepingute puhul jagame need vastavalt lepingutele endile. Iga leping on sõltumatu _shard_. Näiteks kui teil on ainult USDT-märkid, ei pea te salvestama ega valideerima kogu teise märgi, näiteks USDC, ajalugu. Bitcoini puhul ei tee plokiahelas _shardingut_: teil on globaalne kogum UTXOsid. Kliendipoolse valideerimise puhul säilitab iga osaleja ainult lepingu andmed, mida ta omab või kasutab.

Seega võime ökosüsteemi ette kujutada järgmiselt:


- Plokiahel (Bitcoin)** kui alus, mis tagab minimaalse registri täieliku kordamise ja toimib ajatempli kihina;
- Lightning Network** kiirete ja konfidentsiaalsete tehingute jaoks, mis põhinevad endiselt Bitcoini plokiahela turvalisusel ja lõplikul arveldamisel;
- RGB ja kliendipoolne valideerimine**, et lisada keerulisemat aruka lepingu loogikat, ilma et see segaks plokiahelat või kaotaks konfidentsiaalsust.

![RGB-Bitcoin](assets/fr/007.webp)

Need kolm elementi moodustavad kolmnurkse terviku, mitte lineaarse virna "kiht 2", "kiht 3" jne. Lightning võib ühendada otse Bitcoiniga või olla seotud Bitcoini tehingutega, mis sisaldavad RGB-andmeid. Samamoodi võib "BiFi" kasutamine (rahandus Bitcoinis) moodustada koos plokiahelaga, Lightningiga ja RGBga vastavalt konfidentsiaalsuse, skaleeritavuse või lepinguloogika vajadustele.

![RGB-Bitcoin](assets/fr/008.webp)

### Mõiste "olekute üleminekud"

Igas hajutatud süsteemis on valideerimismehhanismi eesmärk olla võimeline **määrama oleku muutuste kehtivust ja ajalist järjekorda**. Eesmärk on kontrollida, et protokollireeglitest on kinni peetud, ja tõestada, et need olekumuutused järgnevad üksteisele kindlas, vaidlustamatus järjekorras.

Et mõista, kuidas see valideerimine **Bitcoini** kontekstis toimib, ja üldisemalt, et mõista kliendipoolse valideerimise taga olevat filosoofiat, vaatame kõigepealt tagasi Bitcoini plokiahela mehhanismidesse, enne kui näeme, kuidas kliendipoolne valideerimine neist erineb ja milliseid optimeerimisi see võimaldab.

![RGB-Bitcoin](assets/fr/009.webp)

Bitcoini plokiahela puhul põhineb tehingu valideerimine lihtsal reeglil:


- Kõik võrgusõlmed laadivad alla iga ploki ja tehingu;
- Nad valideerivad need tehingud, et kontrollida UTXO-komplekti (kõik kulutamata väljundid) õiget arengut;
- Nad salvestavad need andmed (plokkide kujul), nii et ajalugu saab vajaduse korral uuesti esitada.

![RGB-Bitcoin](assets/fr/010.webp)

Sellel mudelil on siiski kaks peamist puudust:


- Skaleeritavus**: kuna iga sõlme peab töötlema, kontrollima ja arhiveerima kõigi tehinguid, on tehingumahule ilmselge piir, mis on seotud eelkõige maksimaalse plokisuurusega (1 MB keskmiselt 10 minuti jooksul Bitcoini puhul, välja arvatud küpsised);
- Privaatsus**: kõik edastatakse ja salvestatakse avalikult (summad, sihtaadressid jne), mis piirab teabevahetuse konfidentsiaalsust.

![RGB-Bitcoin](assets/fr/012.webp)

Praktikas toimib see mudel Bitcoini puhul baaskihina (kiht 1), kuid võib osutuda ebapiisavaks keerulisemate kasutusalade puhul, mis nõuavad samaaegselt suurt tehingu läbilaskevõimet ja teatavat konfidentsiaalsust.

Kliendipoolne valideerimine põhineb vastupidisel ideel: selle asemel, et nõuda kogu võrgustikult kõigi tehingute valideerimist ja salvestamist, valideerib iga osaleja (klient) ainult selle osa ajaloost, mis teda puudutab:


- Kui isik saab vara (või mis tahes muu digitaalse vara), peab ta ainult teadma ja kontrollima operatsioonide ahelat (olekute üleminekuid), mis viivad selle varani, ja tõestama selle seaduslikkust;
- See operatsioonide jada alates ***Genesis*** (algsest väljastamisest) kuni viimase tehinguni moodustab atsüklilise suunatud graafi (DAG) või killustiku, st osa kogu ajaloost.

![RGB-Bitcoin](assets/fr/013.webp)

Samal ajal, et ülejäänud võrk (või täpsemalt, aluseks olev kiht, näiteks Bitcoin) saaks lukustada lõpliku seisundi, ilma et ta näeks nende andmete üksikasju, tugineb kliendipoolne valideerimine ***commitment*** mõistele.

*Kohustus* on krüptograafiline kohustus, tavaliselt _hash_ (näiteks SHA-256), mis lisatakse Bitcoini tehingusse ja mis tõestab, et privaatsed andmed on lisatud, ilma neid andmeid paljastamata.

Tänu nendele _kohustustele_ saame tõestada:


- Teabe olemasolu (kuna see on pandud hash'ile) ;
- Selle teabe eelisjärjekord (kuna see on ankurdatud ja ajatempliga varustatud plokiahelas koos kuupäeva ja plokkide järjekorraga).

Täpne sisu siiski ei avaldata, säilitades seega selle konfidentsiaalsuse.

Konkreetselt on RGB-staatuste ülemineku tööpõhimõte järgmine:


- Te valmistate ette uue oleku ülemineku (nt RGB-märgi üleandmine);
- Te genereerite selle ülemineku kohta krüptograafilise kohustuse ja sisestate selle Bitcoini tehingusse (neid kohustusi nimetatakse RGB-protokollis "*ankriteks*");
- Vastaspool (vastuvõtja) otsib selle varaga seotud kliendipoolset ajalugu ja valideerib otsest järjepidevust, alates aruka lepingu tekkimisest kuni teie poolt edastatava üleminekuni.

![RGB-Bitcoin](assets/fr/014.webp)

Kliendipoolne valideerimine pakub kahte olulist eelist:


- Skaleeritavus:**

Plokiahelas sisalduvad kohustused (*commitments*) on väikesed (suurusjärgus mõnikümmend baiti). See tagab, et plokiruumi ei küllastata, kuna vaja on lisada ainult hash. See võimaldab ka ahelavälise protokolli arengut, kuna iga kasutaja peab salvestama ainult oma ajaloofragmenti (oma _stash_).


- Privaatsus :**

Tehinguid (st nende üksikasjalikku sisu) ei avaldata ahelas. Avaldatakse ainult nende sõrmejäljed (*hash*). Seega jäävad summad, aadressid ja lepinguloogika privaatseks ning vastuvõtja saab kohapeal kontrollida oma osakonna kehtivust, vaadates kõiki eelnevaid ülekandeid. Vastuvõtjal ei ole mingit põhjust neid andmeid avalikustada, välja arvatud vaidluse korral või kui on vaja tõestust.

Sellises süsteemis nagu RGB saab mitme eri lepingute (või erinevate varade) oleku üleminekuid koondada üheks Bitcoini tehinguks ühe _commitment_ kaudu. See mehhanism loob deterministliku, ajamärgistatud seose ahelas toimuva tehingu ja ahelaväliste andmete (kliendipoolsed valideeritud üleminekud) vahel ning võimaldab mitut killustikku üheaegselt salvestada ühes ankurduspunktis, vähendades veelgi ahelas olevaid kulusid ja jalajälge.

Praktikas, kui see Bitcoini tehing on kinnitatud, "lukustab" see aluspõhiste lepingute seisundi jäädavalt, kuna plokiahelasse juba kantud hash'i muutmine muutub võimatuks.

![RGB-Bitcoin](assets/fr/015.webp)

### Varamu kontseptsioon

**Kast** on kliendipoolsete andmete kogum, mida osaleja peab tingimata säilitama, et säilitada RGB nutilepingu terviklikkus ja ajalugu. Erinevalt Lightning-kanalist, kus teatud olekuid saab ühisest teabest lokaalselt rekonstrueerida, ei reprodutseerita RGB-lepingu stash'i mujal: kui te selle kaotate, ei saa keegi seda teile taastada, sest te vastutate oma osa ajaloo eest. Seepärast peate RGB-s kasutusele võtma usaldusväärse varundamismenetlusega süsteemi.

![RGB-Bitcoin](assets/fr/016.webp)

### Ühekordselt kasutatav pitsat: päritolu ja toimimine

Sellise vara nagu valuuta vastuvõtmisel on olulised kaks tagatist:


- Saadud eseme autentsus;
- Saadud eseme ainulaadsus, et vältida topeltkulusid.

Füüsilise vara, näiteks pangatähe puhul piisab füüsilisest olemasolust, et tõestada, et seda ei ole dubleeritud. Kuid digitaalses maailmas, kus vara on puhtalt informatiivne, on see kontrollimine keerulisem, sest teave võib kergesti paljuneda ja dubleerida.

Nagu me nägime varem, võimaldab saatja avalikustatud oleku üleminekute ajalugu tagada RGB-märkide autentsuse. Kuna meil on juurdepääs kõikidele tehingutele alates algsest tehingust, saame kinnitada märgi autentsust. See põhimõte on sarnane Bitcoini põhimõttega, kus müntide ajalugu saab nende kehtivuse kontrollimiseks jälgida tagasi algse coinbase'i tehinguni. Kuid erinevalt Bitcoinist on RGB-s see oleku üleminekute ajalugu privaatne ja seda hoitakse kliendi poolel.

RGB-märkide kahekordse kulutamise vältimiseks kasutame mehhanismi nimega "**Korduvkasutatav pitser**". See süsteem tagab, et iga kord kasutatud žetooni ei saa pettuse teel teist korda uuesti kasutada.

Ühekordsed pitsatid on 2016. aastal Peter Toddi poolt välja pakutud krüptograafilised primitiivid, mis sarnanevad füüsiliste pitserite kontseptsioonile: kui pitser on kord konteinerile asetatud, on seda võimatu avada või muuta ilma pitserit pöördumatult murdmata.

![RGB-Bitcoin](assets/fr/018.webp)

Selline lähenemisviis, mis on üle kantud digitaalsesse maailma, võimaldab tõestada, et sündmuste jada on tõepoolest toimunud ja et seda ei saa enam tagantjärele muuta. Ühekordse kasutusega pitsatid lähevad seega kaugemale lihtsast loogikast `hash + ajatempel`, lisades mõiste pitsat, mida saab sulgeda **kord**.

![RGB-Bitcoin](assets/fr/017.webp)

Selleks, et ühekordselt kasutatavad pitserid toimiksid, on vaja avaldamise tõendamiseks meediumit, mis suudab tõestada avaldamise olemasolu või puudumist ja mida on raske (kui mitte võimatu) võltsida, kui teave on juba levitatud. Seda rolli võib täita **blockchain** (nagu Bitcoin), nagu ka näiteks avaliku levikuga paberkandjal ajaleht. Idee on järgmine:


- Me tahame tõestada, et teatava sõnumi `h(m)` kohta võetud kohustus on publitseeritud publikule ilma sõnumi `m` sisu paljastamata;
- Me tahame tõestada, et ükski teine konkureeriv `h(m')` sõnumikohustus ei ole avaldatud `h(m)` asemel;
- Samuti tahame kontrollida, et sõnum "m" oleks olemas enne teatud kuupäeva.

Plokiahel sobib ideaalselt selle rolli täitmiseks: niipea, kui tehing on lisatud plokki, on kogu võrgustikul sama võltsimata tõend selle olemasolu ja sisu kohta (vähemalt osaliselt, sest _commitment_ võib varjata üksikasjad, tõestades samas sõnumi autentsust).

Ühekordset pitserit võib seega vaadelda kui ametlikku lubadust avaldada (praegu veel tundmatu) sõnum üks kord ja ainult üks kord viisil, mida kõik huvitatud pooled saavad kontrollida.

Erinevalt lihtsatest _commitments_ (hash) või ajatemplitest, mis tõendavad olemasolu kuupäeva, pakub ühekordselt kasutatav pitser lisagarantiid, et **ei saa olla ühtegi alternatiivset kohustust**: te ei saa sama pitserit kaks korda sulgeda ega üritada pitseeritud sõnumit asendada.

Järgnev võrdlus aitab seda põhimõtet mõista:


- Krüptograafiline kohustus (hash)**: Hash-funktsiooni abil saab andmete (numbri) suhtes pühenduda, avaldades selle hash'i. Andmed jäävad salajaseks, kuni te avaldate eelkujutise, kuid te saate tõestada, et te teadsite seda eelnevalt;
- Ajatempel (plokiahela)**: Lisades selle hash'i plokiahelasse, tõestame ka, et me teadsime seda konkreetsel hetkel (plokki lisamise ajal);
- Ühekordselt kasutatav pitsat**: Ühekordsete pitserite puhul läheme sammu võrra kaugemale, muutes kohustuse ainulaadseks. Ühe hashiga saab paralleelselt luua mitu vastandlikku kohustust (arstide probleem, kes teatab perele "*See on poiss*" ja oma isiklikus päevikusse "*See on tüdruk*"). Ühekordne pitsat välistab selle võimaluse, ühendades kohustuse avaldustõendiga, näiteks Bitcoini plokiahelaga, nii et UTXO kulutamine pitseerib kohustuse lõplikult. Pärast kulutamist ei saa sama UTXO-d uuesti kulutada, et asendada kohustust.

| Ühekordsed pitsatid | Ajatemplid | Lihtne kohustus (digest/hash) | Ühekordsed pitsatid | Ühekordsed pitsatid |

| -------------------------------------------------------------------------------- | ------------------------------- | ---------- | ---------------- |

| Kohustuse avaldamine ei avalda sõnumit | Jah | Jah | Jah | Jah | Jah | Jah | Jah | Jah

| Kohustuse kuupäevade tõendamine / sõnumi olemasolu enne teatud kuupäeva | Võimatu | Võimalik | Võimalik | Võimalik | Võimalik | Võimalik

| Tõend, et muud alternatiivset kohustust ei saa olla | Võimatu | Võimalik | Võimalik |

Ühekordsed tihendid töötavad kolmes peamises etapis:

**Seal Definition :**


- Alice määrab eelnevalt kindlaks pitseri avaldamise reeglid (millal, kus ja kuidas sõnum avaldatakse);
- Bob nõustub või tunnistab neid tingimusi.

![RGB-Bitcoin](assets/fr/021.webp)

**Seal Closing :**


- Käitusajal sulgeb Alice pitseri, avaldades tegeliku sõnumi (tavaliselt _commitment_ kujul, nt hash);
- Samuti annab see **tunnistuse** (krüptograafiline tõend), mis tõestab, et pitser on suletud ja tühistamatu.

![RGB-Bitcoin](assets/fr/019.webp)

**Seal Verification :**


- Kui pitser on suletud, ei saa Bob seda enam avada: ta saab ainult kontrollida, kas pitser on suletud;
- Bob kogub pitseri, **tunnistaja** ja sõnumi (või oma kohustuse), et veenduda, et kõik sobib ja et ei ole konkureerivaid pitsereid või erinevaid versioone.

Protsessi võib kokku võtta järgmiselt:

```txt
# Défini par Alice, validé ou accepté par Bob
seal <- Define()
# Fermeture du sceau par Alice avec le message
witness <- Close(seal, message)
# Vérification par Bob
bool <- Verify(seal, witness, message)
```

Kliendipoolne valideerimine läheb aga veel ühe sammu võrra kaugemale: kui pitseri enda määratlus jääb plokiahelast väljapoole, on (teoreetiliselt) võimalik, et keegi vaidlustab kõnealuse pitseri olemasolu või õiguspärasuse. Selle probleemi ületamiseks kasutatakse omavahel seotud ühekordsete pitserite ahelat:


- Iga suletud pitser sisaldab järgmise pitseri määratlust;
- Me registreerime need sulgemised (koos nende _commitments_) plokiahelas (Bitcoini tehingus);
- Seega oleks igasugune katse muuta varasemat pitserit vastuolus Bitcoini sisseehitatud ajalooga.

Just seda RGB-süsteem teebki:


- Avaldatud sõnumid on kliendi poolsete valideeritud andmete _kohustused_;
- Pitsati määratlus on seotud Bitcoini UTXOga ;
- Pitser suletakse, kui see UTXO on kulutatud või kui samale kulukohustusele kantakse uus väljund;
- Tehinguahel, mis kulutab neid UTXOsid, vastab avaldamise tõendile: iga üleminek või oleku muutus RGBs on seega ankurdatud Bitcoinis.

Kokkuvõttes:


- _Pitsatite määratlus_ on UTXO, mida te kavatsete pitsatite tulevase kohustuse;
- Sulgemine toimub siis, kui te kulutate selle UTXO, luues tehingu, mis sisaldab kulukohustust;
- _tunnistus_ on tehing ise, mis tõestab, et te olete selle sisuga pitseri sulgenud;
- Te ei saa tõestada, et pitserit ei ole suletud (te ei saa olla täiesti kindel, et UTXO ei ole juba kulutatud või et seda ei kulutata plokis, mida te veel ei ole näinud), kuid te saate tõestada, et see on tõepoolest suletud.

See unikaalsus on oluline kliendipoolse valideerimise jaoks: kui te valideerite oleku üleminekut, siis kontrollite, et see vastab unikaalsele UTXO-le, mis ei ole eelnevalt kulutatud konkureerivas kulukohustuses. See on see, mis tagab topeltkulutuste puudumise ahelavälistes nutilepingutes.

### Mitmesugused kohustused ja juured

RGB-arukas leping võib vajada samaaegselt mitme ühekordse kasutusega pitseri (mitu UTXOd) kulutamist. Veelgi enam, üks Bitcoini tehing võib viidata mitmele erinevale lepingule, millest igaüks pitseerib oma riigi ülemineku. See nõuab **multi-commitment** mehhanismi, mis tõestab deterministlikult ja üheselt, et ükski kohustus ei eksisteeri dubleerivalt. Siinkohal tuleb RGBs mängu mõiste **anker**: spetsiaalne struktuur, mis ühendab Bitcoini tehingu ja ühe või mitu kliendipoolset kohustust (oleku üleminekut), millest igaüks võib kuuluda eri lepingule. Vaatleme seda mõistet lähemalt järgmises peatükis.

![RGB-Bitcoin](assets/fr/023.webp)

Projekti kaks peamist GitHubi repositooriumi (LNPBP organisatsiooni all) koondavad nende esimeses peatükis uuritud kontseptsioonide põhilisi rakendusi:


- kliendi_poolne_valideerimine** : Sisaldab Rusti primitiive kohalikuks valideerimiseks ;
- ühekordse_kasutuse_plommid**: Rakendab loogikat nende plommide turvaliseks määratlemiseks ja sulgemiseks.

![RGB-Bitcoin](assets/fr/020.webp)

Pange tähele, et need tarkvaraplokid on Bitcoini agnostilised; teoreetiliselt võib neid rakendada ka mis tahes muu avaldamise tõendusmaterjali puhul (teine register, ajakiri jne). Tegelikkuses tugineb RGB Bitcoinile, kuna see on usaldusväärne ja laiapõhjaline konsensus.

![RGB-Bitcoin](assets/fr/021.webp)

### Avalikkuse küsimused

#### Ühekordsete pitserite laiema kasutamise suunas

Peter Todd lõi ka _Open Timestamps_ protokolli ja ühekordselt kasutatava pitseri kontseptsioon on nende ideede loomulikuks laienduseks. Lisaks RGB-le võib ette näha ka muid kasutusjuhtumeid, näiteks _sidechains_ ehitamine ilma _merge mining'ile_ või drivechainiga seotud ettepanekutele nagu BIP300. Põhimõtteliselt võib seda krüptograafilist primitiivi kasutada iga süsteem, mis nõuab ühekordset kohustust. Täna on RGB esimene suuremahuline täiemahuline rakendus.

#### Andmete kättesaadavuse probleemid

Kuna kliendipoolse valideerimise puhul salvestab iga kasutaja oma osa ajaloost, ei ole andmete kättesaadavus globaalselt tagatud. Kui lepingu väljastaja jätab teatud andmed tagasi või tühistab need, ei pruugi te olla kursis pakkumise tegeliku arenguga. Mõnel juhul (näiteks stabiilse mündi puhul) eeldatakse, et emitent säilitab avalikke andmeid, et tõestada ringluses olevat mahtu, kuid tehnilist kohustust selleks ei ole. Seetõttu on võimalik kujundada tahtlikult läbipaistmatuid lepinguid piiramatu pakkumisega, mis tekitab usaldusküsimusi.

#### Jagamine ja lepingu isoleerimine

Iga leping kujutab endast üksikut "killustikku": USDT ja USDC näiteks ei pea oma ajalugu jagama. Aatomivahetused on endiselt võimalikud, kuid see ei hõlma nende registrite ühendamist. Kõik toimub krüptograafiliste kohustuste abil, ilma et iga osaleja saaks kogu ajaloo graafikut avaldada.

### Kokkuvõte

Me nägime, kuidas kliendipoolse valideerimise kontseptsioon sobib kokku plokiahela ja _state channels_, kuidas see reageerib hajutatud arvutusküsimustele ja kuidas see kasutab Bitcoini plokiahelat unikaalselt, et vältida topeltkulutusi ja *time-stamping*. Idee põhineb mõistel **Korduvkasutatav pitsat**, mis võimaldab luua unikaalseid kohustusi, mida ei saa soovi korral uuesti kulutada. Sel viisil laeb iga osaleja üles ainult selle ajaloo, mis on tingimata vajalik, suurendades arukate lepingute skaleeritavust ja konfidentsiaalsust, säilitades samal ajal Bitcoini turvalisuse taustaks.

Järgmise sammuna selgitatakse üksikasjalikumalt, kuidas seda ühekordselt kasutatava pitseri mehhanismi rakendatakse Bitcoinis (UTXOde kaudu), kuidas luuakse ja valideeritakse ankurdusi ning seejärel, kuidas täielikud arukad lepingud on RGB-s üles ehitatud. Eelkõige vaatleme mitmekordsete kohustuste küsimust, tehnilist väljakutset tõestada, et Bitcoini tehing pitseerib samaaegselt mitu oleku üleminekut erinevates lepingutes, ilma et see tooks kaasa haavatavusi või topeltkohustusi.

Enne teise peatüki tehnilistesse üksikasjadesse sukeldumist lugege julgelt uuesti läbi peamised definitsioonid (kliendipoolne valideerimine, ühekordne pitser, ankurdused jne) ja pidage meeles üldist loogikat: me püüame ühitada Bitcoini plokiahela tugevusi (turvalisus, detsentraliseerimine, ajatempeldus) ja ahelaväliseid lahendusi (kiirus, konfidentsiaalsus, skaleeritavus) ning just seda püütakse saavutada RGB ja kliendipoolse valideerimise abil.

## Kohustuste kiht

<chapterId>cc2fe85a-9cc7-5b8c-a00a-c0a867241061</chapterId>

![video](https://youtu.be/FS6PDprWl5Q)

Selles peatükis vaatleme kliendipoolse valideerimise ja ühekordselt kasutatavate pitserite rakendamist Bitcoini plokiahelas. Tutvustame RGB **commitment layer** (1. kiht) peamisi põhimõtteid, keskendudes eelkõige **TxO2** skeemile, mida RGB kasutab pitseri defineerimiseks ja sulgemiseks Bitcoini tehingus. Seejärel arutame kahte olulist punkti, mida ei ole veel üksikasjalikult käsitletud:


- _deterministlikud Bitcoini kohustused_;
- Mitme protokolliga seotud kohustused.

Just nende mõistete kombinatsioon võimaldab meil ühe UTXO ja seega ühe plokiahela peale panna mitu süsteemi või lepingut.

Tuleb meeles pidada, et kirjeldatud krüptograafilisi operatsioone saab absoluutselt kohaldada ka teiste plokiahelate või avaldamismeedia suhtes, kuid Bitcoini omadused (detsentraliseerituse, tsensuurikindluse ja kõigile avatuse osas) muudavad selle ideaalseks aluseks täiustatud programmeeritavuse arendamiseks, nagu seda nõuab **RGB**.

### Kohustusskeemid Bitcoinis ja nende kasutamine RGB poolt

Nagu me nägime kursuse esimeses peatükis, on ühekordse kasutusega pitsatid üldine kontseptsioon: me anname lubaduse lisada kohustus (_commitment_) tehingu konkreetsesse kohta ja see koht toimib nagu pitsat, mille me sulgeme sõnumile. Bitcoini plokiahelas on aga mitu võimalust valida, kuhu see _commitment_ paigutada.

Loogika mõistmiseks tuletame meelde põhiprintsiipi: _korduvkasutatava pitseri_ sulgemiseks kulutame pitseriga kaetud ala, sisestades antud sõnumi kohta _commitment_. Bitcoinis saab seda teha mitmel viisil:


- Kasutage avalikku võtit või aadressi**

Me võime otsustada, et konkreetne avalik võti või aadress on _kasutatav pitsat_. Niipea kui see võti või aadress ilmub tehingus ahelas, tähendab see, et pitser on suletud teatud sõnumiga.


- Kasutage Bitcoin** tehingu väljundit

See tähendab, et _korduvkasutatav pitsat_ on määratletud täpse _väljundpunktina_ (TXID + väljundnumbri paar). Niipea kui see _väljundpunkt_ on kulutatud, suletakse pitser.

RGB kallal töötades leidsime vähemalt 4 erinevat võimalust nende pitserite rakendamiseks Bitcoinis:


- Määrake pitser avaliku võtme kaudu ja sulgege see _väljundis_ ;
- Määrake pitsat _väljundiga_ ja sulgege see _väljundiga_ ;
- Määrake pitser avaliku võtme väärtuse kaudu ja sulgege see _sisendisse_ ;
- Määrake pitsat _väljundpunkti_ kaudu ja sulgege see _sisendpunkti_ kaudu.

| Pitseri määratlus | Pitseri sulgemine | Täiendavad nõuded | Põhirakendus | Võimalikud kaasamisskeemid |

| ------------- | ------------------------- | --------------------- | ----------------------------------------------------------------- | ---------------------------- | ------------------------------ |

| P2(W)PKH | Praegu puudub | Keytweak, taptweak, opret |

| TxO2 | Tehingu väljund | Tehingu väljund | Nõuab Bitcoini deterministlikke kohustusi | RGBv1 (universaalne) | Keytweak, tapret, opret |

| PkI | Avaliku võtme väärtus | Tehingukanne | Ainult Taproot & ei ühildu Legacy rahakottidega | Bitcoin-põhised identiteedid | Sigtweak, witweak |

| TxO1 | Tehingu väljund | Tehingu sisend | Ainult Taproot & ei ühildu Legacy rahakottidega | Hetkel puudub | Sigtweak, witweak |

Me ei hakka iga sellise konfiguratsiooni kohta üksikasjalikult rääkima, sest RGB-s oleme otsustanud kasutada **pitseri määratlusena **väljundit** ja paigutada _sisselülitus_ tehingu väljundisse, mis kulutab seda _väljundit_. Seega võime järgmiseks kasutusele võtta järgmised mõisted:


- "Pitseri määratlus "** : Antud _väljundpunkt_ (identifitseeritud TXID + väljundi nr.) ;
- "Pitseri sulgemine "**: Tehing, mis kulutab selle _väljapunkti_, kus sõnumile lisatakse _commitment_.

See skeem on valitud RGB-arhitektuuriga ühilduvuse tõttu, kuid muud konfiguratsioonid võivad olla kasulikud erinevatel kasutusaladel.

"O2" sõnas "TxO2" tuletab meile meelde, et nii määratlus kui ka sulgemine põhinevad tehingu väljundi kulutamisel (või loomisel).

### TxO2 diagrammi näide

Tuletame meelde, et _kasutatava pitseri_ määratlemine ei nõua tingimata ahelas toimuva tehingu avaldamist. Näiteks piisab sellest, kui Alice'il on juba kasutamata UTXO. Ta võib otsustada: "See _väljapunkt_ (juba olemasolev) on nüüd minu pitsat". Ta märgib seda lokaalselt (_kliendipoolselt_) ja kuni see UTXO on kulutatud, loetakse pitsat avatuks.

![RGB-Bitcoin](assets/fr/024.webp)

Päeval, mil ta tahab sulgeda pitseri (et anda märku mingist sündmusest või kinnitada mingi konkreetne sõnum), kulutab ta selle UTXO uues tehingus (seda tehingut nimetatakse sageli "_näitlustehinguks_" (ei ole seotud _segwit_ga, see on lihtsalt termin, mille me talle anname). See uus tehing sisaldab sõnumi _commitment_.

![RGB-Bitcoin](assets/fr/025.webp)

Pange tähele, et selles näites :


- Mitte keegi peale Bobi (või inimeste, kellele Alice otsustab avaldada täieliku tõendi) ei tea, et selles tehingus on peidetud teatud sõnum;
- Kõik näevad, et _väljapunkt_ on kulutatud, kuid ainult Bobil on tõestus, et sõnum on tegelikult tehingusse ankurdatud.

Selle TxO2-skeemi illustreerimiseks võime kasutada PGP-võtme tühistamise mehhanismina _korduvkasutatavat pitserit_. Selle asemel, et avaldada tühistamissertifikaat serverites, võib Alice öelda: "See Bitcoini väljund, kui see kulutatakse, tähendab, et minu PGP-võti on tühistatud".

Seega on Alice'il konkreetne UTXO, millega on lokaalselt (kliendi poolel) seotud teatav seisund või andmed (mida teab ainult tema).

Alice teatab Bobile, et kui see UTXO on kulutatud, loetakse, et teatav sündmus on toimunud. Väljastpoolt vaadates näeme vaid Bitcoini tehingut, kuid Bob teab, et sellel kulutusel on varjatud tähendus.

![RGB-Bitcoin](assets/fr/026.webp)

Kui Alice veedab selle UTXO, sulgeb ta pitseri sõnumile, mis näitab tema uut võtit või lihtsalt vana võtme tühistamist. Sel viisil näevad kõik, kes jälgivad ahelas, et UTXO on kulutatud, kuid ainult need, kellel on täielik tõend, teavad, et tegemist on just PGP-võtme tühistamisega.

![RGB-Bitcoin](assets/fr/027.webp)

Selleks, et Bob või keegi teine asjaosaline saaks varjatud sõnumit kontrollida, peab Alice andma talle ahelavälise teabe.

![RGB-Bitcoin](assets/fr/028.webp)

Alice peab seega andma Bobile :


- Sõnum ise (näiteks uus PGP-võti) ;
- Krüptograafiline tõend selle kohta, et sõnum oli tehingus osalenud (tuntud kui _extra transaction proof_ või _anchor_).

![RGB-Bitcoin](assets/fr/029.webp)

Kolmandatel isikutel ei ole seda teavet. Nad näevad ainult seda, et UTXO on kulutatud. Seega on konfidentsiaalsus tagatud.

Struktuuri selgitamiseks võtame protsessi kokku kahes tehingus:


- Tehing 1**: See sisaldab _pitsati määratlust_, st _väljundpunkti_, mida kasutatakse pitsatina.

![RGB-Bitcoin](assets/fr/031.webp)


- Tehing 2**: Kulutab selle _väljapunkti_. Sellega suletakse pitser ja samas tehingus sisestatakse sõnumile _commitment_.

![RGB-Bitcoin](assets/fr/033.webp)

Seepärast nimetame teist tehingut "_tunnistustehinguks_".

Et illustreerida seda teise nurga alt, võime kujutada kahte kihti:


- Ülemine kiht (plokiahelat, avalik)**: kõik näevad tehingut ja teavad, et _väljapunkt_ on kulutatud;
- Madalam kiht (kliendipoolne, privaatne)** : ainult Alice (või asjaomane isik) teab, et see kulu vastab sellisele ja sellisele sõnumile, kasutades selleks krüptograafilist tõestust ja sõnumit, mida ta hoiab kohapeal.

![RGB-Bitcoin](assets/fr/034.webp)

Kuid pitseri sulgemisel tekib küsimus, kuhu tuleks sisestada _kohustus_

Eelmises punktis mainisime lühidalt, kuidas kliendipoolset valideerimismudelit saab rakendada RGB ja muude süsteemide puhul. Siinkohal käsitleme **deterministlikke Bitcoini kohustusi** ja seda, kuidas neid tehingusse integreerida. Mõte on mõista, miks me püüame lisada ühe kohustuse _tunnistustehingusse_ ja eelkõige seda, kuidas tagada, et ei saa olla teisi avalikustamata konkureerivaid kohustusi.

### Kulukohustuste asukohad tehingus

Kui te annate kellelegi tõendi, et teatud sõnum on varjatud tehingus, peate olema võimeline tagama, et samas tehingus ei ole teist liiki kohustust (teist, varjatud sõnumit), mida teile ei ole avaldatud. Selleks, et kliendipoolne valideerimine jääks töökindlaks, on vaja **deterministlikku** mehhanismi, millega paigutatakse tehingusse üks _kohustus_, mis sulgeb _ükskordse kasutamise pitseri_.

_tunnistustehing_ kulutab kuulsa UTXO (ehk _pitsatimääruse_) ja see kulu vastab pitsati sulgemisele. Tehniliselt teame, et iga väljundpunkti saab kulutada ainult üks kord. Just see on aluseks Bitcoini vastupidavusele topeltkulutamisele. Kuid kulutamistehingul võib olla mitu _väljundit_, mitu _väljundit_ või see võib olla kompleksselt kokku pandud (coinjoins, Lightning-kanalid jne). Seetõttu tuleb selgelt ja ühetaoliselt määratleda, kuhu selles struktuuris _commitment_ sisestada.

Olenemata meetodist (PkO, TxO2 jne.), saab _kohustust_ sisestada :


- Sisend** kaudu :
    - Sigtweak** (muudab ECDSA allkirja "r" komponenti, sarnaselt "Sign-to-contract" põhimõttele) ;
    - Witweak** (tehingu _segregeeritud tunnistaja_ andmeid muudetakse).
- Väljundis** kaudu :
    - Keytweak** (vastuvõtja avalik võti "tweakitakse" koos sõnumiga) ;
    - Opret** (sõnum paigutatakse mittekasutatavasse väljundisse `OP_RETURN`) ;
    - Tapret** (või _Taptweak_), mis tugineb taproot'ile, et sisestada taproot-võtme skriptiosasse kohustus, muutes seega avalikku võtit deterministlikult.

![RGB-Bitcoin](assets/fr/035.webp)

Siin on iga meetodi üksikasjad:

![RGB-Bitcoin](assets/fr/038.webp)

***Sig tweak (lepingu sõlmimine) :***

Varasem skeem hõlmas allkirja juhusliku osa (ECDSA või Schnorr) kasutamist, et varjata _sidus_: see on tehnika, mida tuntakse kui "**allkirja-lepinguks-saamine**". Juhuslikult genereeritud nonce asendatakse andmeid sisaldava hashiga. Sel viisil paljastab allkiri kaudselt teie pühendumuse, ilma et tehingus oleks lisaruumi. Sellel lähenemisviisil on mitmeid eeliseid:


- Puudub ahelasisene ülekoormus (te kasutate sama kohta, kus põhiline nonce);
- Teoreetiliselt võib see olla üsna diskreetne, kuna nonce on algselt juhuslik andmestik.

Siiski on ilmnenud 2 peamist puudust:


- Multisig enne Taproot: kui teil on mitu allakirjutajat, peate otsustama, milline allkiri kannab _kohustust_. Allkirju võib tellida erinevalt ja kui allakirjutanu keeldub, kaotate kontrolli _commitment_ tulemuse üle;
- MuSig ja jagatud nonce: Schnorr multisig (*MuSig*) puhul on nonce'i genereerimine mitmepoolne algoritm ja nonce'i on praktiliselt võimatu individuaalselt muuta.

Praktikas ei ühildu **sig tweak** ka väga hästi olemasoleva riistvara (riistvara rahakotid) ja formaatidega (Lightning jne). Seega on seda toredat ideed raske ellu viia.

***Key tweak (pay-to-contract) :***

**Välimalt oluline muudatus** võtab kasutusele ajaloolise kontseptsiooni _maksab lepingust_. Võtame avaliku võtme `X` ja muudame seda, lisades väärtuse `H(sõnum)`. Täpsemalt, kui `X = x * G` ja `h = H(sõnum)`, siis on uus võti `X' = X + h * G`. See muudetud võti peidab `sõnumi` kohustust. Esialgse privaatvõtme omanik saab, lisades `h` oma privaatvõtmele `x`, tõestada, et tal on võti väljundi kulutamiseks. Teoreetiliselt on see elegantne, sest :


- _commitment_ sisestatakse ilma lisaväljade lisamiseta;
- Te ei salvesta mingeid täiendavaid ahelas olevaid andmeid.

Praktikas puutume aga kokku järgmiste raskustega:


- Rahakotid ei tunnista enam tavalist avalikku võtit, kuna seda on "muudetud", nii et nad ei saa UTXO-d hõlpsasti teie tavapärase võtmega seostada;
- Riistvaralised rahakotid ei ole mõeldud allkirjastamiseks võtmega, mis ei ole tuletatud nende standardsest tuletusest;
- Te peate kohandama oma skripte, kirjeldusi jne.

RGB kontekstis oli see tee ette nähtud kuni 2021. aastani, kuid see osutus liiga keeruliseks, et seda praeguste standardite ja infrastruktuuriga toimima panna.

***Tunnistus tweak :***

Teine idee, mida teatud protokollid, näiteks _inscriptions Ordinals_, on rakendanud, on andmete paigutamine otse tehingu "tunnistajate" sektsiooni (siit ka väljend "tunnistaja tweak"). Kuid see meetod :


- Teeb kaasamise kohe nähtavaks (te sõna otseses mõttes kleebite toorandmed tunnistajasse);
- Võib alluda tsensuurile (kaevurid või sõlmed võivad keelduda edastamisest, kui see on liiga suur või mõni muu suvaline tunnus);
- Kulutab ruumi plokkides, vastupidiselt RGB eesmärgile diskreetsuse ja kerguse osas.

Lisaks sellele on tunnistaja kavandatud nii, et ta on teatavates kontekstides kärbitav, mis võib muuta usaldusväärsete tõendite olemasolu keerulisemaks.

***Open-return (opret) :***

Väga lihtsa toimega `OP_RETURN` võimaldab salvestada hashi või sõnumi tehingu eriväljale. Kuid see on kohe avastatav: igaüks näeb, et tehingus on _commitment_, ja seda saab tsenseerida või ära visata, samuti lisada lisaväljundi. Kuna see suurendab läbipaistvust ja suurust, peetakse seda kliendipoolse valideerimislahenduse seisukohast vähem rahuldavaks.

```txt
34-byte_Opret_Commitment =
OP_RETURN   OP_PUSHBYTE_32   <mpc::Commitment>
|_________| |______________| |_________________|
1-byte       1-byte         32 bytes
```

### Tapret

Viimane võimalus on kasutada **Taproot** (kasutusele võetud koos BIP341) koos *Tapret* skeemiga. *Tapret* on deterministliku kohustuse keerukam vorm, mis toob kaasa parandusi seoses jalajälje vähenemisega plokiahelas ja lepinguoperatsioonide konfidentsiaalsusega. Põhiidee seisneb selles, et kohustus on peidetud [taproot-tehingu] (https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki) `Script Path Spend` osasse.

![RGB-Bitcoin](assets/fr/036.webp)

Enne kui kirjeldame, kuidas kohustus sisestatakse taproot-tehingu sisse, vaatleme kohustuse **täpse vormi**, mis peab **imperatiivselt** vastama 64baidisele stringile [konstrueeritud](https://github.com/BP-WG/bp-core/blob/master/dbc/src/tapret/mod.rs#L179-L196) järgmiselt:

```txt
64-byte_Tapret_Commitment =
OP_RESERVED ...  ... .. OP_RESERVED   OP_RETURN   OP_PUSHBYTE_33  <mpc::Commitment>  <Nonce>
|___________________________________| |_________| |______________| |_______________|  |______|
OP_RESERVED x 29 times = 29 bytes      1 byte         1 byte          32 bytes        1 byte
|________________________________________________________________| |_________________________|
TAPRET_SCRIPT_COMMITMENT_PREFIX = 31 bytes                    MPC commitment + NONCE = 33 bytes
```


- 29 baiti "OP_RESERVED", millele järgneb "OP_RETURN" ja seejärel "OP_PUSHBYTE_33" moodustavad 31 baidi pikkuse _prefix_ osa;
- Järgneb 32 baidi suurune _commitment_ (tavaliselt Merkle root alates **MPC**), millele lisame 1 baidi **Nonce** (kokku 33 baiti selle teise osa jaoks).

Seega näeb 64 baidi pikkune meetod `Tapret` välja nagu `Opret`, millele me oleme ette pannud 29 baiti `OP_RESERVED` ja lisanud ühe lisabaidi Nonce'ina.

Et säilitada paindlikkus rakendamise, konfidentsiaalsuse ja skaalumise osas, võtab Tapret-skeem arvesse erinevaid kasutusjuhtumeid, sõltuvalt nõuetest:


- Ainulaadne Tapret'i kulukohustuse lisamine taproot-tehingusse ilma eelnevalt olemasoleva Script Path'i struktuurita;
- Tapret-kohustuse integreerimine Taproot-tehingusse, mis on juba varustatud Script Path'iga.

Vaatleme lähemalt mõlemat neist kahest stsenaariumist.

#### Tapret'i lisamine ilma olemasoleva Script Path'ilt

Esimesel juhul alustame taproot väljundvõtmest (*Taproot Output Key*) `Q`, mis sisaldab ainult sisemist avalikku võtit `P` *(Internal Key*), ilma seotud skriptitee (*Script Path*) ilma sellega seotud skriptitee (*Script Path*) :

![RGB-Bitcoin](assets/fr/047.webp)


- "P": _Key Path Spend_ sisemine avalik võti.
- "G": elliptilise kõvera [secp256k1] (https://en.bitcoin.it/wiki/Secp256k1) genereeriv punkt.
- t = tH_TWEAK(P)` on tweak-tegur, mis arvutatakse _tagged hash_ abil (nt `SHA-256(SHA-256(TapTweak) || P)`) vastavalt [BIP86](https://github.com/bitcoin/bips/blob/master/bip-0086.mediawiki#address-derivation). See tõestab, et varjatud skripti ei ole.

**Tapret** kulukohustuse lisamiseks lisage **Skripti tee kulutused** koos **üheselt mõistetava skriptiga** järgmiselt:

![RGB-Bitcoin](assets/fr/048.webp)


- t = tH_TWEAK(P || Script_root)` saab siis uueks tweak-faktoriks, sealhulgas **Script_root**.
- `Script_root = tH_BRANCH(64-byte_Tapret_Commitment)` kujutab selle **skripti** juurt, mis on lihtsalt hash tüüpi `SHA-256(SHA-256(TapBranch) || 64-byte_Tapret_Commitment)`.

Kaasamise ja ainulaadsuse tõestamine taproot-puus taandub siinkohal ühele sisemisele avalikule võtmele `P`.

#### Tapret'i integreerimine olemasolevasse skriptipidi

Teine stsenaarium on seotud keerukama `Q` taproot** väljundiga, mis sisaldab juba mitmeid skripte. Näiteks on meil 3 skriptist koosnev puu:

![RGB-Bitcoin](assets/fr/049.webp)


- tH_LEAF(x)` tähistab lehtskripti normaliseeritud märgistatud hash-funktsiooni.
- a, B, C` tähistavad skripte, mis on juba lisatud taproot-struktuuri.

Tapret'i kohustuse lisamiseks peame lisama *kulutamata skripti* puu esimesele tasemele, nihutades olemasolevad skriptid ühe taseme võrra allapoole. Visuaalselt muutub puu :

![RGB-Bitcoin](assets/fr/050.webp)


- tHABC` tähistab ülemise taseme rühmituse "A, B, C" märgistatud hash'i.
- tHT` kujutab 64baidisele `Tapret` vastava skripti hash'i.

Taproot-reeglite kohaselt tuleb iga haru/leht kombineerida leksikograafilise hash-järjestuse järgi. On kaks võimalikku juhtumit:


- `tHT` > `tHABC`: Tapret'i kohustus liigub puu paremale poole. Ainulaadsuse tõestamiseks on vaja ainult `tHABC` ja `P` ;
- tHT` < `tHABC`**: Tapret'i kohustus paigutatakse vasakule. Et tõestada, et paremal ei ole muud Tapret-kohustust, tuleb `tHAB` ja `tHC` paljastada, et näidata, et puudub mõni muu selline skript.

Visuaalne näide esimese juhtumi kohta (`tHABC < tHT`):

![RGB-Bitcoin](assets/fr/051.webp)

Näide teise juhtumi kohta (tHABC > tHT):

![RGB-Bitcoin](assets/fr/052.webp)

#### Optimeerimine koos nonce'iga

Konfidentsiaalsuse parandamiseks võime "kaevandada" (täpsem termin oleks "bruteforcing") `<Nonce>` (64 baidi pikkuse `Tapret` viimane bait) väärtuse, püüdes saada hash `tHT` nii, et `tHABC < tHT`. Sellisel juhul pannakse kohustus paremale poole, säästes kasutajat sellest, et ta ei peaks avaldama kogu olemasolevate skriptide sisu, et tõestada Tapret'i unikaalsust.

Kokkuvõttes pakub "Tapret" diskreetset ja deterministlikku viisi kohustuse lisamiseks taproot-tehingusse, järgides samal ajal unikaalsuse ja ühemõttelisuse nõuet, mis on RGB kliendipoolse valideerimise ja ühekordse pitsatiloogika jaoks oluline.

#### Kehtivad väljapääsud

RGB-kohustustehingute puhul on kehtiva Bitcoini kohustusskeemi põhinõue järgmine: Tehing (*tunnistustehing*) peab tõendatavalt sisaldama ühte kohustust. See nõue muudab võimatuks alternatiivse ajaloo konstrueerimise kliendipoolsete kinnitatud andmete jaoks sama tehingu raames. See tähendab, et teade, mille ümber _üksikasutuspitsat_ sulgub, on unikaalne.

Selle põhimõtte täitmiseks ja olenemata tehingu väljundite arvust, nõuame, et **üks ja ainult üks väljund** võib sisaldada kohustust (*commitment*). Iga kasutatava skeemi (*Opret* või *Tapret*) puhul on ainsad kehtivad väljundid, mis võivad sisaldada RGB _commitment_, järgmised:


- Esimene väljund "OP_RETURN" (kui see on olemas) skeemi *Opret* jaoks;
- Esimene taproot väljund (kui see on olemas) *Tapret* skeemi jaoks.

Pange tähele, et on täiesti võimalik, et tehing sisaldab ühte "Opret"-kohustust ja ühte "Tapret"-kohustust kahes eraldi väljundis. Tänu Seal Definition'i deterministlikule olemusele vastavad need kaks kohustust siis kahele erinevale kliendipoolselt valideeritud andmestikule.

### Analüüs ja praktilised valikud RGB-süsteemis

Kui me alustasime RGBga, vaatasime kõik need meetodid läbi, et määrata kindlaks, kuhu ja kuidas transaktsiooni _commitment_ deterministlikult paigutada. Me määratlesime mõned kriteeriumid:


- Ühilduvus erinevate stsenaariumidega (nt multisig, Lightning, riistvara rahakotid jne);
- Mõju ahelasisesele ruumile ;
- Rakendamise ja hoolduse keerukus ;
- Konfidentsiaalsus ja vastupanu tsensuurile.

| Jälgimine ja ahelasisene dimensioneerimine | Kliendipoolne dimensioneerimine | Portfelli integreerimine | Riistvara ühilduvus | Lightning ühilduvus | Taproot ühilduvus |

| --------------------------------------------------- | ------------------------ | ------------------ | ----------------------------- | ------------------------ | ----------------------- | --------------------- |

| Keytweak (deterministlik P2C) | 🟢 | 🟡 | 🔴 | 🟠 | 🔴 BOLT, 🔴 Bifrost | 🟠 Taproot, 🟢 MuSig | 🟢 MuSig |

| Sigtweak (deterministlik S2C) | 🟢 | 🟠 | 🔴 | 🔴 BOLT, 🔴 Bifrost | 🟠 Taproot, 🔴 MuSig | 🟠 Sigtweak |

| Opret (OP_RETURN) | 🔴 | 🟢 | 🟢 | 🟠 | 🔴 BOLT, 🟠 Bifrost | - | |

| Tapret algoritm: vasakpoolne ülemine sõlmpunkt | 🟠 | 🔴 | 🟠 | 🟢 | 🔴 BOLT, 🟢 Bifrost | 🟢 Taproot, 🟢 MuSig | 🟢 MuSig |

| Tapret algoritm #4: iga sõlme + tõend | 🟢 | 🟠 | 🟢 | 🔴 BOLT, 🟢 Bifrost | 🟢 Taproot, 🟢 MuSig | 🟢 Taproot |

| Deterministlik kulukohustusskeem | Standard | Kulud ahelas | Kliendipoolse tõendusmaterjali suurus |

| ------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |

| Keytweak (deterministlik P2C) | LNPBP-1, 2 | 0 baiti | 33 baiti (parandamata võti) |

| Sigtweak (deterministlik S2C) | WIP (LNPBP-39) | 0 baiti | 0 baiti | 0 baiti |

| Opret (OP_RETURN) | - | 36 (v)baiti (TxOut täiendav) | 0 baiti |

| Tapret algoritm: vasakpoolne ülemine sõlm | LNPBP-6 | 32 baiti tunnistaja (8 vbaiti) igal n-m multisigil ja kulutab ühe skripti tee kohta | 0 baiti taproot skriptita skriptidel ~270 baiti ühe skripti puhul, ~128 baiti, kui mitu skripti |

| Tapret algoritm #4: iga sõlme + unikaalsuse tõestus | LNPBP-6 | 32 baiti tunnistajas (8 vb) ühe skripti puhul, 0 baiti tunnistajas enamikul muudel juhtudel | 0 baiti taproot skriptita skriptide puhul, 65 baiti kuni Taptree on tosin skripti |

| Kiht | Kettakulu (baidid/vbait) | Kettakulu (baidid/vbait) | Kettakulu (baidid/vbait) | Kettakulu (baidid/vbait) | Kettakulu (baidid/vbait) | Kettakulu (baidid/vbait) | Kliendipoolne kulu (baidid) | Kliendipoolne kulu (baidid) | Kliendipoolne kulu (baidid) | Kliendipoolne kulu (baidid) | Kliendipoolne kulu (baidid) | Kliendipoolne kulu (baidid) |

| ------------------------------ | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ |

| **Tüüp** | **Tapret** | **Tapret #4** | **Keytweak** | **Sigtweak** | **Opret** | **Tapret** | **Tapret #4** | **Keytweak** | **Sigtweak** | **Opret** | **Tapret #4** | **Tapret #4** | **Keytweak** | **Sigtweak** | **Opret** | **Opret** |

| Single-sig | 0 | 0 | 0 | 0 | 0 | 0 | 32 | 0 | 0 | 0 | 32 | 0? | 0 | 0 |

| MuSig (n-n) | 0 | 0 | 0 | 0 | 0 | 32 | 0 | 0 | 0 | 32 | ? > 0 | 0 |

| Multi-sig 2-of-3 | 32/8 | 32/8 või 0 | 0 n/a | 32 | ~270 | 65 | 32 | n/a | 0 | 0 |

| Multi-sig 3-of-5 | 32/8 | 32/8 või 0 | 0 n/a | 32 | ~340 | 65 | 32 | n/a | 0 | 0 |

| Multi-sig 2-of-3 ajavaruga | 32/8 | 0 | 0 n/a | 32 | 64 | 65 | 32 | n/a | 0 | 0 | 0

| Kiht | Kulu ahelas (vb) | Kulu ahelas (vb) | Kulu ahelas (vb) | Kulu kliendi poolel (baidid) | Kulu kliendi poolel (baidid) | Kulu kliendi poolel (baidid) |

| -------------------------------- | ---------------------- | ---------------------- | ---------------------- | ------------------------ | ------------------------ |

| **Tüüp** | **Base** | **Tapret #2** | **Tapret #4** | **Tapret #2** | **Tapret #4** | **Tapret #4** |

| MuSig (n-n) | 16,5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0

| FROST (n-of-m) | ? | 0 | 0 | 0 | 0 |

| Multi_a (n-m) | 1+16n+8m | 8 | 8 | 33 * m | 65 | 65 |

| MuSig haru / Multi_a (n-ist-m) | 1+16n+8n+8xlog(n) | 8 | 0 | 64 | 65 | 65 |

| Aegumistega (n-ist-m) | 1+16n+8n+8xlog(n) | 8 | 0 | 64 | 65 | 65 |

| Meetod | Konfidentsiaalsus ja skaleeritavus | Koostalitlusvõime | Ühilduvus | Kaasaskantavus | Keerukus | Komplekssus |

| ----------------------------------------- | ------------------------------ | ---------------- | ------------- | ----------- | ---------- |

| Keytweak (deterministlik P2C) | 🟢 | 🔴 | 🔴 | 🟡 | 🟡 | 🟡 |

| Sigtweak (deterministlik S2C) | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 | 🟢 | 🔴 |

| Opret (OP_RETURN) | 🔴 | 🟠 | 🔴 | 🟢 | 🟢 | 🟢 |

| Algo Tapret: ülemine vasakpoolne sõlm | 🟠 | 🟢 | 🔴 | 🟠 | 🟠 |

| Algo Tapret #4: Iga sõlme + tõend | 🟢 | 🟢 | 🟠 | 🔴 | 🟢 |

Uuringu käigus selgus, et ükski kohustusskeemidest ei ole täielikult ühilduv praeguse Lightning-standardiga (mis ei kasuta Taproot, _muSig2_ või täiendavat _commitment_-tuge). Praegu tehakse jõupingutusi, et muuta Lightning'i kanali konstruktsiooni (*BiFrost*), et võimaldada RGB-kohustuste lisamist. See on veel üks valdkond, kus me peame üle vaatama tehingu struktuuri, võtmed ja viisi, kuidas kanali uuendused allkirjastatakse.

Analüüs näitas, et muud meetodid (key tweak, sig tweak, witness tweak jne) kujutasid endast tegelikult muid komplikatsioone:


- Kas meil on suur ahelasisene maht;
- Kas on radikaalne kokkusobimatus olemasoleva rahakoti koodiga;
- Kas lahendus ei ole elujõuline mittetöötava multisegi puhul.

RGB puhul paistavad silma eelkõige kaks meetodit: ***Opret*** ja ***Tapret***, mis mõlemad on klassifitseeritud kui "Transaction Output" ja ühilduvad protokollis kasutatava TxO2 režiimiga.

### Mitme protokolliga seotud kohustused - MPC

Selles jaotises vaatleme, kuidas **RGB** käsitleb mitme lepingu (või täpsemalt, nende _transition bundles_) koondamist ühe kohustuse (*commitment*) raames, mis on salvestatud Bitcoini tehingus deterministliku skeemi kaudu (vastavalt `Opret` või `Tapret`). Selle saavutamiseks toimub erinevate lepingute Merkeliseerimise järjekord struktuuris, mida nimetatakse **MPC-puuks** (_Multi Protocol Commitment Tree_). Selles jaotises vaatleme selle MPC Tree ehitust, kuidas saada selle juurt ja kuidas mitu lepingut saavad sama tehingut konfidentsiaalselt ja üheselt mõistetavalt jagada.

Mitme protokolliga seotud kohustused (MPC) on mõeldud kahe vajaduse rahuldamiseks:


- `mpc::Commitment` hashi konstrueerimine: see lisatakse Bitcoini plokiahelasse vastavalt `Opret` või `Tapret` skeemile ja peab kajastama kõiki valideeritavaid olekumuutusi;
- Mitme lepingu samaaegne salvestamine ühes _commitment_is, mis võimaldab mitme vara või RGB-lepingu eraldi uuendusi hallata ühes Bitcoini tehingus.

Konkreetselt öeldes kuulub iga _üleminekupakett_ konkreetsele lepingule. Kogu see teave sisestatakse **MPC-puusse**, mille juur (`mpc::Root`) on seejärel uuesti hashitud, et saada `mpc::Commitment`. See viimane hash pannakse Bitcoini tehingusse (_tunnistustehing_) vastavalt valitud deterministlikule meetodile.

![RGB-Bitcoin](assets/fr/042.webp)

#### MPC root Hash

Tegelik väärtus, mis kirjutatakse ahelas (`Opret` või `Tapret`), kannab nime `mpc::Commitment`. See arvutatakse kujul [BIP-341] (https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki), vastavalt valemile :

```txt
mpc::Commitment = SHA-256(SHA-256(mpc_tag) || SHA-256(mpc_tag) || depth || cofactor || mpc::Root )
```

kus :


- `mpc_tag` on silt: `urn:ubideco:mpc:commitment#2024-01-31`, mis on valitud vastavalt [RGB märgistuse konventsioonidele](https://github.com/RGB-WG/rgb-core/blob/master/doc/Commitments.md);
- `depth` (1 baidiga) näitab *MPC Tree* sügavust;
- cofactor` (16 bitti, Little Endian) on parameeter, mida kasutatakse igale lepingule määratud positsioonide unikaalsuse edendamiseks puu sees;
- `mpc::Root` on *MPC Tree* juur, mis arvutatakse järgmises jaotises kirjeldatud protsessi kohaselt.

![RGB-Bitcoin](assets/fr/044.webp)

#### MPC puu ehitus

Selle MPC-puu loomiseks peame tagama, et iga leping vastab unikaalsele lehe positsioonile. Oletame, et meil on :


- c` lepingud, mis tuleb lisada, indekseerituna `i`ga `i = {0,1,...,C-1}` ;
- Iga lepingu `c_i` jaoks on meil identifikaator `ContractId(i) = c_i`.

Seejärel konstrueerime puu laiusega `w` ja sügavusega `d` nii, et `2^d = w`, kusjuures `w > C`, nii et iga leping saab paigutada eraldi _lehte_. Iga lepingu positsioon `pos(c_i)` puu sees on määratud :

```txt
pos(c_i) = c_i mod (w - cofactor)
```

kus "koefaktor" on täisarv, mis suurendab iga lepingu puhul erinevate positsioonide saamise tõenäosust. Praktikas järgib konstruktsioon iteratiivset protsessi:


- Alustame minimaalsest sügavusest (kokkuleppeliselt `d=3`, et varjata lepingute täpset arvu);
- Proovime erinevaid "koefitsiente" (kuni "w/2" või maksimaalselt 500 jõudluse tagamiseks);
- Kui meil ei õnnestu kõiki lepinguid ilma kokkupõrgeteta paigutada, suurendame `d` ja alustame uuesti.

Eesmärk on vältida liiga kõrgeid puid, hoides samas kokkupõrke riski minimaalsena. Pange tähele, et kokkupõrke nähtus järgib juhusliku jaotuse loogikat, mis on seotud [Anniversary Paradox](https://en.wikipedia.org/wiki/Birthday_problem).

#### Asustatud lehed

Kui lepingute `i = {0,1,...,C-1}` jaoks on saadud `C` erinevat positsiooni `pos(c_i)`, täidetakse iga leht hash-funktsiooniga (*tagged hash*):

```txt
tH_MPC_LEAF(c_i) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x10 || c_i || BundleId(c_i))
```

kus :


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, valitakse alati vastavalt RGB Merkle konventsioonidele;
- `0x10` tähistab _lepingulehte_ ;
- "c_i" on 32baidine lepingu identifikaator (tuletatud Genesis'i hashist);
- bundleId(c_i)` on 32 baidi suurune hash, mis kirjeldab `c_i`ga seotud oleku üleminekute kogumit (mis on koondatud *Transition Bundle'iks*).

#### Asustamata lehed

Ülejäänud lehed, mis ei ole määratud lepingule (st `w - C` lehed), täidetakse "dummy" väärtusega (_entroopia leht_) :

```txt
tH_MPC_LEAF(j) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x11 || entropy || j )
```

kus :


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, valitakse alati vastavalt RGB Merkle konventsioonidele;
- `0x11` tähistab _entroopialehte_ ;
- `entroopia` on juhuslik 64 baidi suurune väärtus, mille valib puu koostamise eest vastutav isik;
- "j" on selle lehe positsioon (32-bitises Little Endian'is) puu sees.

#### MPC-sõlmed

Pärast "w" lehtede (asustatud või mitte) genereerimist jätkame merkeldamist. Kõiki sisemisi sõlmi hakitakse järgmiselt:

```txt
tH_MPC_BRANCH(tH1 || tH2) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || b || d || w || tH1 || tH2)
```

kus :


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, valitakse alati vastavalt RGB Merkle konventsioonidele;
- b` on _hargnemistegur_ (8 bitti). Enamasti on `b=0x02`, sest puu on binaarne ja täielik;
- d` on sõlme sügavus puu sees;
- "w" on puu laius (256-bitises Little Endian binaarsüsteemis);
- tH1` ja `tH2` on laps-sõlmede (või lehtede) hashid, mis on juba arvutatud nagu eespool näidatud.

Sel viisil edasi liikudes saame juure `mpc::Root`. Seejärel saame arvutada `mpc::Commitment` (nagu eespool selgitatud) ja sisestada selle ahelasse.

Selle illustreerimiseks kujutame ette näidet, kus "C=3" (kolm lepingut). Nende positsioonid on eeldatavasti `pos(c_0)=7`, `pos(c_1)=4`, `pos(c_2)=2`. Teised lehed (positsioonid 0, 1, 3, 5, 6) on _entroopialehed_. Alljärgnevas diagrammis on esitatud hashide jada juurtega :


- `BUNDLE_i`, mis tähistab `BundleId(c_i)` ;
- `tH_MPC_LEAF(A)` ja nii edasi, mis kujutavad lehti (mõned lepinguid, teised entroopiat) ;
- Iga haru `tH_MPC_BRANCH(...)` kombineerib oma kahe lapse hashid.

Lõpptulemus on **mpc::Root**, seejärel `mpc::Commitment`.

![RGB-Bitcoin](assets/fr/053.webp)

#### MPC võlli kontroll

Kui tõendaja soovib tagada, et leping `c_i` (ja selle `BundleId`) sisaldub lõplikus `mpc::Commitment`is, saab ta lihtsalt Merkle-tõendi. See tõestus näitab sõlmed, mida on vaja, et jälgida lehed (antud juhul `c_i` _lepinguleht_) tagasi juureni. Kogu *MPC-puud* ei ole vaja avalikustada: see kaitseb teiste lepingute konfidentsiaalsust.

Näites vajab `c_2` verifitseerija ainult vahepealset hashi (`tH_MPC_LEAF(D)`), kahte `tH_MPC_BRANCH(...)`, `pos(c_2)` positsioonitõendit ja `cofactor` väärtust. Seejärel saab ta lokaalselt rekonstrueerida juure, seejärel arvutada uuesti `mpc::Commitment` ja võrrelda seda Bitcoini tehingus (`Opret` või `Tapret` raames) kirja panduga.

![RGB-Bitcoin](assets/fr/054.webp)

See mehhanism tagab, et :


- Seisund "c_2" suhtes on tõepoolest lisatud koondteabeblokki (kliendipoolne);
- Keegi ei saa luua alternatiivset ajalugu sama tehinguga, sest ahelasisene _commitment_ osutab ühele MPC juurele.

#### MPC struktuuri kokkuvõte

Multi Protocol Commitment* (MPC) on põhimõte, mis võimaldab RGB-l koondada mitu lepingut üheks Bitcoini tehinguks, säilitades samal ajal kohustuste unikaalsuse ja konfidentsiaalsuse teiste osalejate suhtes. Tänu puu deterministlikule ehitusele määratakse igale lepingule unikaalne positsioon ja "dummy" lehtede (*Entroopia lehed*) olemasolu varjab osaliselt tehingus osalevate lepingute koguarvu.

Kogu Merkle'i puu ei salvestata kunagi kliendile. Me lihtsalt genereerime iga asjaomase lepingu jaoks _Merkle-puu_, mis edastatakse vastuvõtjale (kes saab seejärel kohustuse kinnitada). Mõnel juhul võib teil olla mitu vara, mis on läbinud sama UTXO. Siis saate ühendada mitu _Merkle-tee_ nn _multiprotokollide kulukohustuste blokki_, et vältida andmete liigset dubleerimist.

Iga _Merkle tõestus_ on seega kerge, eriti kuna puu sügavus ei ületa RGB-s 32. Samuti on olemas mõiste "Merkle'i plokk", mis säilitab rohkem teavet (ristlõige, entroopia jne), mis on kasulik mitme haru ühendamiseks või eraldamiseks.

Seepärast võttis RGB lõpuleviimine nii kaua aega. Meil oli üldine visioon alates 2019. aastast: panna kõik kliendipoolele, ringlusse panna märgid väljaspool ahelat. Aga selliste detailide puhul nagu mitme lepingu jagamine, Merkle'i puu struktuur, kuidas käsitleda kokkupõrkeid ja ühinemistõendeid... kõik see nõudis iteratsioone.

### Ankurdajad: ülemaailmne koost

Pärast meie kohustuste (`Opret` või `Tapret`) ja meie MPC (*Multi Protocol Commitment*) konstrueerimist peame käsitlema RGB-protokolli **Anchor** mõistet. Ankur on kliendipoolne valideeritud struktuur, mis koondab kokku elemendid, mis on vajalikud selle kontrollimiseks, et Bitcoini kohustus sisaldab tegelikult konkreetset lepingulist teavet. Teisisõnu, Anchor võtab kokku kõik andmed, mida on vaja eespool kirjeldatud _kohustuste_ valideerimiseks.

Ankur koosneb kolmest järjestatud väljast:


- `Txid`
- `MPC Proof`
- ekstra tehingu tõendamine - ETP

Kõik need väljad mängivad valideerimisprotsessis oma osa, olgu siis tegemist Bitcoini aluseks oleva tehingu rekonstrueerimisega või varjatud kohustuse olemasolu tõendamisega (eriti "Tapret" puhul).

#### TxId

Väli "TXID" vastab 32baidisele Bitcoini tehingu identifikaatorile, mis sisaldab "Opret"- või "Tapret"-kohustust.

Teoreetiliselt oleks võimalik leida see "Txid", jälgides olekute üleminekute ahelat, mis omakorda viitavad igale tunnistajatehingule, järgides ühekordse kasutusega pitserite loogikat. Kontrollimise hõlbustamiseks ja kiirendamiseks lisatakse see `Txid` siiski lihtsalt ankrusse, mis säästab valideerijat kogu ahelavälise ajaloo läbimise vajadusest.

#### MPC tõend

Teine väli, "MPC tõend", viitab tõendile, et see konkreetne leping (nt "c_i") on lisatud _Multiprotokolli kulukohustusse_. See on kombinatsioon :


- "pos_i", selle lepingu positsioon mitmeaastase partnerluslepingu puus;
- cofactor`, väärtus, mis on määratletud positsioonikolleteerimise lahendamiseks;
- "Merkle Proof", s.t sõlmede ja hashide kogum, mida kasutatakse MPC juure rekonstrueerimiseks ja selle kontrollimiseks, et lepingu identifikaator ja selle "Transition Bundle" on juurele kinnitatud.

Seda mehhanismi kirjeldati eelmises jaotises *MPC Tree* ehitamise kohta, kus iga leping saab unikaalse lehe tänu :

```txt
pos(c_i) = c_i mod (w - cofactor)
```

Seejärel kasutatakse deterministlikku merkeldamisskeemi, et koondada kõik lehed (lepingud + entroopia). Lõpuks võimaldab `MPC tõestus` rekonstrueerida juurt lokaalselt ja võrrelda seda ahelas oleva `mpc::Commitment`iga.

#### Täiendav tehingu tõendamine - ETP

Kolmas väli, **ETP**, sõltub kasutatavast kulukohustuse tüübist. Kui kohustus on tüüpi "Opret", ei ole täiendavat tõendit vaja. Valideerija kontrollib tehingu esimest `OP_RETURN` väljundit ja leiab `mpc::Commitment` otse sealt.

**Kui kohustus on tüüpi "Tapret "**, tuleb esitada täiendav tõend nimega *Extra Transaction Proof - ETP*. See sisaldab :


- Taproot-väljundi sisemine avalik võti (`P`), millesse *commitment* on põimitud;
- Partner sõlmed `Skripti tee kulutamine` (kui Tapret *kommitatsioon* on sisestatud skripti), et tõestada selle skripti täpset asukohta taproot-puus:
 - Kui `Tapret` *commitment* on parempoolses harus, paljastame vasakpoolse sõlme (nt `tHABC`),
 - Kui `Tapret` *sidumine* on vasakul, siis tuleb avalikustada 2 sõlme (nt `tHAB` ja `tHC`), et tõestada, et paremal pool ei ole ühtegi teist *sidumist*.
- `nonce` võib kasutada parima konfiguratsiooni "kaevandamiseks", mis võimaldab *sõltuvuse* paigutada puu paremale poole (tõestuse optimeerimine).

See lisatõend on oluline, sest erinevalt `Opret`ist on `Tapret` kohustus integreeritud taproot-skripti struktuuri, mis nõuab taproot-puu osa paljastamist, et õigesti kinnitada *kohustuse* asukohta.

![RGB-Bitcoin](assets/fr/045.webp)

**Ankurdajad** sisaldavad seega kogu teavet, mis on vajalik Bitcoini kohustuse kinnitamiseks RGB kontekstis. Nad näitavad nii asjaomast tehingut (`Txid`) kui ka lepingu positsioneerimise tõestust (`MPC Proof`), hallates samal ajal täiendavat tõestust (`ETP`) `Tapret` puhul. Sel viisil kaitseb Anchor ahelavälise oleku terviklikkust ja ainulaadsust, tagades, et sama tehingut ei saa ümber tõlgendada teiste lepinguliste andmete jaoks.

### Kokkuvõte

Selles peatükis käsitleme :


- Kuidas rakendada ühekordselt kasutatavate pitserite kontseptsiooni Bitcoinis (eelkõige _outpoint_ kaudu);
- Erinevad meetodid, mille abil saab tehingusse deterministlikult sisestada _commitment_ (Sig tweak, Key tweak, witness tweak, op_return, Taproot/Tapret) ;
- Põhjused, miks RGB keskendub Tapret'i kohustustele ;
- Mitme lepingu haldamine _multi-protokolli kohustuste_ kaudu, mis on oluline, kui te ei soovi paljastada tervet riiki või teisi lepinguid, kui soovite tõestada konkreetset punkti;
- Me oleme näinud ka _Ankurdajate_ rolli, mis koondavad kõik kokku (tehingu TXID, Merkle tree proof ja Taproot proof) ühte paketti.

Tegelikkuses on tehniline rakendamine jagatud mitme spetsiaalse Rusti _crates_ vahel (_client_side_validation_, _commit-verify_, _bp_core_ jne). Põhimõttelised mõisted on olemas:

![RGB-Bitcoin](assets/fr/046.webp)

Järgmises peatükis vaatleme RGB puhtalt ahelavälise komponendi, nimelt lepinguloogikat. Näeme, kuidas RGB lepingud, mis on korraldatud osaliselt replitseeritud _lõputute olekuga masinatena_, saavutavad palju suurema väljendusrikkuse kui Bitcoini skriptid, säilitades samal ajal oma andmete konfidentsiaalsuse.

## Sissejuhatus arukatesse lepingutesse ja nende olekudesse

<chapterId>04a9569f-3563-5382-bf53-0c7069343ba0</chapterId>

![video](https://youtu.be/tmAVdyXGmj4)

Selles ja järgmises peatükis vaatleme RGB-keskkonna raames mõistet **armas leping** ja uurime erinevaid viise, kuidas need lepingud saavad määratleda ja arendada oma *seisundit*. Me näeme, miks RGB arhitektuur, kasutades ühekordsete pitserite järjestatud jada, võimaldab erinevaid ***sõlmimisoperatsioone*** skaleeritaval viisil ja ilma tsentraliseeritud registri kaudu käimata teostada. Samuti vaatleme ***Business Logic*** fundamentaalset rolli lepingu staatuse arengu kujundamisel.

### Arukad lepingud ja digitaalsed omanikuõigused

RGB eesmärk on pakkuda infrastruktuuri arukate lepingute rakendamiseks Bitcoinis. "Aruka lepingu" all mõistame mitme osapoole vahelist kokkulepet, mida rakendatakse automaatselt ja arvutuslikult, ilma et inimene sekkuks klauslite jõustamiseks. Teisisõnu, lepingu seadust jõustab tarkvara, mitte usaldusväärne kolmas isik.

Selline automatiseerimine tõstatab küsimuse detsentraliseerimisest: kuidas saame vabaneda tsentraliseeritud registrist (nt keskne platvorm või andmebaas), et hallata omandiõigust ja lepingute täitmist? Algne idee, mille RGB on üles võtnud, on pöörduda tagasi omandivormi, mida tuntakse kui "esitajainstrumente". Ajalooliselt anti teatavad väärtpaberid (võlakirjad, aktsiad jne) välja esitaja vormis, mis võimaldas igaühel, kes dokumenti füüsiliselt valdas, oma õigusi maksma panna.

![RGB-Bitcoin](assets/fr/055.webp)

RGB kohaldab seda kontseptsiooni digitaalsele maailmale: õigused (ja kohustused) on kapseldatud andmetesse, mida manipuleeritakse ahelaväliselt, ning nende andmete staatuse kinnitavad osalejad ise. See võimaldab a priori palju suuremat konfidentsiaalsust ja sõltumatust kui muudes avalikel registritel põhinevates lähenemisviisides.

### Sissejuhatus nutika lepingu RGB olekusse

Nutikat lepingut RGB-s võib vaadelda kui riigimasinat, mis on määratletud :


- **State**, st lepingu praegust konfiguratsiooni kajastav teabekogum;
- **Ülesandeloogika** (reeglistik), mis kirjeldab, millistel tingimustel ja kelle poolt saab olekut muuta.

![RGB-Bitcoin](assets/fr/056.webp)

Oluline on mõista, et need lepingud ei piirdu pelgalt žetoonide ülekandmisega. Need võivad kehastada väga erinevaid rakendusi: alates traditsioonilistest varadest (märgid, aktsiad, võlakirjad) kuni keerulisemate mehaanikateni (kasutusõigused, äritingimused jne). Erinevalt teistest plokiahelatest, kus lepingukood on kõigile kättesaadav ja täidetav, on RGB lähenemisviisiga lepingule juurdepääs ja teadmised lepingust jaotatud osalejatele ("***lepingu osalejad***"). Rolle on mitu:


- Emitent** või lepingu looja, kes määratleb lepingu tekkepõhimõtted ja selle algsed muutujad;
- Õigustega** (*omand*) või muude täitevõimalustega osapooled ;
- Vaatlejad**, kes võivad näha ainult teatud teavet, kuid ei saa käivitada muudatusi.

Selline rollide eraldamine aitab kaasa tsensuurivastasusele, tagades, et ainult volitatud isikud saavad lepingulise riigiga suhelda. Samuti annab see RGB-le võime horisontaalselt skaleeruda: enamik valideerimisi toimub väljaspool plokiahelat ja Bitcoini on kantud ainult krüptograafilised ankurdused (*sõlmimised*).

### Staatus ja äriloogika RGB-s

Praktilisest vaatenurgast vaadatuna on lepingu **äriühingu loogika** reeglite ja skriptide kujul, mis on määratletud selles, mida RGB nimetab **skeemiks**. Skeem kodeerib :


- Riigi struktuur (millised väljad on avalikud? Millised väljad kuuluvad millistele osapooltele?
- Kehtivustingimused (mida tuleb kontrollida enne riigi ajakohastamise lubamist?) ;
- Volitused (kes võib algatada *riigi ülemineku*? Kes võib ainult jälgida?).

Samal ajal jaguneb **Liikmesriik** sageli kaheks komponendiks:


- **Globaalne olek**: avalik osa, mida võivad kõik jälgida (sõltuvalt konfiguratsioonist);
- Omandis olevad riigid**: eraõiguslikud osad, mis eraldatakse omanikele konkreetselt lepinguloogikas viidatud UTXOde kaudu.

Nagu me näeme järgmistes peatükkides, peab iga staatuse uuendamine (*Liikumisoperatsioon*) dubleerima Bitcoini _commitment_-iga (läbi `Opret` või `Tapret`) ja vastama *Business Logic* skriptidele, et seda saaks pidada kehtivaks.

### Lepingulised tegevused: riigi loomine ja areng

RGB universumis on ***Lepinguoperatsioon*** mis tahes sündmus, mis muudab lepingu **vanast seisundist** **uuesse seisundisse**. Need operatsioonid järgivad järgmist loogikat:


- Võtame teadmiseks lepingu hetkeseisu;
- Me rakendame reeglit või operatsiooni (***State Transition***, ***Genesis***, kui see on kõige esimene olek, või ***State Extension***, kui on olemas avalik *valentsus*, mida uuesti käivitada);
- Me kinnistame muudatuse uue _commitment_ kaudu plokiahelas, sulgedes ühe _üksikasutusplommi_ ja luues teise ;
- Asjaomased õiguste omanikud kinnitavad lokaalselt (*kliendipoolselt*), et üleminek vastab *skeemile* ja et sellega seotud Bitcoini tehing on registreeritud ahelas.

![RGB-Bitcoin](assets/fr/057.webp)

Lõpptulemus on ajakohastatud leping, nüüd teistsuguse riigiga. See üleminek ei nõua, et kogu Bitcoini võrgustik oleks üksikasjadega seotud, sest plokiahelas salvestatakse ainult väike krüptograafiline sõrmejälg (_commitment_). Ühekordsete pitserite jada takistab riigi topeltkulutamist või topeltkasutamist.

### Tegevusahel: alates Genesisest kuni lõppseisundini

Et seda paremini mõista, algab RGB nutikas leping **Genesis**, kõige esimesest olekust. Seejärel järgnevad erinevad lepinguoperatsioonid üksteisele, moodustades operatsioonide DAG (*Directed Acyclic Graph*):


- Iga üleminek tugineb eelmisele olekule (või konvergentsete üleminekute puhul mitmele);
- Krooniline järjekord on tagatud iga ülemineku lisamisega Bitcoini ankurdusesse, mis on ajamärgistatud ja muutumatu tänu konsensusele Proof-of-Work'i abil;
- Kui enam ühtegi toimingut ei toimu, saavutatakse **Terminaalseis**: lepingu viimane ja täielik seisund.

![RGB-Bitcoin](assets/fr/012.webp)

Selline DAG-topoloogia (lihtsa lineaarse ahela asemel) kajastab võimalust, et lepingu eri osad võivad areneda paralleelselt, kui nad ei ole omavahel vastuolus. RGB hoolitseb seejärel vastuolude vältimise eest, kontrollides *kliendipoolselt* iga osalejat.

### Kokkuvõte

RGB nutikate lepingutega võetakse kasutusele digitaalsete esitajainstrumentide mudel, mis on detsentraliseeritud, kuid mille aluseks on Bitcoin, et tagada tehingute ajaline tempelmine ja nende järjekord. Nende lepingute automatiseeritud täitmine põhineb :


- **Lepingu olek*, mis näitab lepingu praegust konfiguratsiooni (õigused, saldod, muutujad jne);
- **Ülesandeloogika** (*Skeem*), mis määratleb, millised üleminekud on lubatud ja kuidas neid tuleb valideerida;
- Lepingulised operatsioonid**, mis ajakohastavad seda seisundit samm-sammult tänu Bitcoini tehingutesse kinnistatud kohustustele.

Järgmises peatükis käsitleme üksikasjalikumalt nende ***seisundite*** ja ***seisundi üleminekute*** konkreetset esitust ahelavälisel tasandil ning nende seost Bitcoini sisseehitatud UTXOde ja ühekordsete pitsatitega. See annab võimaluse näha, kuidas RGB sisemine mehaanika, mis põhineb kliendipoolsel valideerimisel, suudab säilitada arukate lepingute järjepidevust, säilitades samal ajal andmete konfidentsiaalsuse.

## RGB lepingulised toimingud

<chapterId>78c44e88-50c4-5ec4-befe-456c1a9f080b</chapterId>

![video](https://youtu.be/lUTjeuM0oTA)

Selles peatükis vaatleme, kuidas toimivad operatsioonid nutikontraktides ja olekute üleminekud, jällegi RGB-protokollis. Eesmärk on ka mõista, kuidas mitu osalejat teevad koostööd vara omandiõiguse üleandmiseks.

### Riigi üleminekud ja nende mehaanika

Üldine põhimõte on endiselt kliendipoolne valideerimine, kus riigiandmed on omaniku valduses ja vastuvõtja poolt valideeritud. RGB puhul seisneb eripära aga selles, et Bob kui vastuvõtja palub Alice'il lisada lepinguandmetesse teatud teavet, et omada tegelikku kontrolli saadud vara üle, kasutades selleks varjatud viidet ühele oma UTXO-le.

Riigi ülemineku* protsessi (mis on üks põhilistest ***Lepinguoperatsioonidest*** RGB-s) illustreerimiseks võtame samm-sammulise näite varade ülekandmisest Alice'i ja Bobi vahel:

**Esialgne olukord:**

Alice'il on ***stash RGB*** lokaalselt valideeritud andmetega (*kliendipoolne*). See peidik viitab ühele tema UTXO-le Bitcoinis. See tähendab, et neis andmetes sisalduv _pitsatimääratlus_ osutab Alice'ile kuuluvale UTXO-le. Idee on võimaldada tal kanda teatud varaga (nt RGB-märkidega) seotud digitaalsed õigused üle Bobile.

![RGB-Bitcoin](assets/fr/058.webp)

**Bobil on ka UTXOd :**

Bobil seevastu on vähemalt üks oma UTXO, millel puudub otsene seos Alice'i omaga. Juhul, kui Bobil ei ole UTXO-d, on siiski võimalik teha üleandmine talle, kasutades *tunnistustehingut* ise: selle tehingu väljund sisaldab siis kohustust (_commitment_) ja seostab uue lepingu omandiõiguse kaudselt Bobiga.

![RGB-Bitcoin](assets/fr/059.webp)

**Uue vara ehitamine (*Uus riik*) :**

Bob saadab Alice'ile ***arve*** kujul kodeeritud teabe (arve koostamisest räägime lähemalt hilisemates peatükkides), paludes tal luua uus lepingureeglitele vastav riik. See olek sisaldab uut *sõltumatuse määratlust*, mis osutab ühele Bobi UTXO-le. Sel viisil antakse Bobile selles uues olekus määratletud varade, näiteks teatud hulga RGB-märkide omandiõigus.

![RGB-Bitcoin](assets/fr/060.webp)

**Tehingu näidise ettevalmistamine:**

Seejärel loob Alice Bitcoini tehingu, mille käigus ta kulutab eelmises pitseris viidatud UTXO-d (see, mis legitimeeris teda kui omanikku). Selle tehingu väljundisse lisatakse *commitment* (läbi `Opret` või `Tapret`), et kinnitada uus RGB olek. Kohustused `Opret` või `Tapret` tuletatakse *MPC-puust* (nagu eelmistes peatükkides nähtud), mis võib koondada mitu üleminekut erinevatest lepingutest.

**Saadetise* edastamine Bobile:**

Enne tehingu edastamist saadab Alice Bobile ***Consignment***, mis sisaldab kõiki vajalikke *kliendipoolseid* andmeid (tema *varamu*) ja Bobi kasuks uut olekuteavet. Sel hetkel kohaldab Bob RGB konsensusreegleid:


- See kinnitab kõik *Kontsignatsioonis* sisalduvad RGB-andmed, sealhulgas uue oleku, mis annab talle vara omandiõiguse;
- Tuginedes *Konsignatsioonile* lisatud *Ankurdajatele*, kontrollib see tunnistajate tehingute kronoloogiat (alates Genesisest kuni viimase üleminekuni) ja kinnitab vastavad kohustused plokiahelas.

**Ülemineku lõpuleviimine:**

Kui Bob on rahul, võib ta anda oma heakskiidu (näiteks allkirjastades *tellimuse*). Seejärel võib Alice edastada ettevalmistatud näidistehingu. Pärast kinnitamist sulgeb see Alice'ile varem kuulunud pitser ja vormistab Bobi omandiõiguse. Topeltkulutuste vastane turvalisus põhineb siis samal mehhanismil nagu Bitcoinis: UTXO on kulutatud, mis tõestab, et Alice ei saa seda enam uuesti kasutada.

![RGB-Bitcoin](assets/fr/061.webp)

Uus olek viitab nüüd Bobi UTXO-le, andes Bobile varem Alice'ile kuulunud omandiõiguse. Bitcoini väljundist, kus RGB-andmed on ankurdatud, saab tühistamatu tõend omandiõiguse ülemineku kohta.

Näide minimaalsest DAG-st (*Directed Acyclic Graph*), mis koosneb kahest lepingulisest operatsioonist (**Genesis**, seejärel ***State Transition***), võib illustreerida, kuidas RGB riik (*kliendipoolne* kiht, punase värviga) ühendab Bitcoini plokiahelat (*Commitment* kiht, oranži värviga).

![RGB-Bitcoin](assets/fr/062.webp)

See näitab, et Genesis määratleb pitseri (*pitseri määratlus*), seejärel *State Transition* sulgeb selle pitseri, et luua uus pitser teises UTXOs.

Sellega seoses on siinkohal mõned terminoloogilised meeldetuletused:


- Ülesanne*** ühendab :
    - ***Seal Definition*** (mis osutab UTXO-le);
    - Omandis olevad riigid**, st andmed, mis on seotud omandiõigusega (näiteks ülekantud žetoonide kogus).
- **Global State** koondab lepingu üldised omadused, mis on kõigile nähtavad ja tagavad evolutsioonide globaalse järjepidevuse.

Eelmises peatükis kirjeldatud riigi üleminekud** on peamine lepingu toimimise vorm. Nad viitavad ühele või mitmele eelmisele olekule (Genesis'ist või mõnest teisest olekute üleminekust) ja ajakohastavad need uueks olekuks.

![RGB-Bitcoin](assets/fr/063.webp)

See diagramm näitab, kuidas *State Transition Bundle'is* saab ühe näidistehingu käigus sulgeda mitu pitserit, avades samal ajal uusi pitsereid. RGB-protokolli huvitav omadus on tõepoolest selle võime skaleeruda: mitu üleminekut saab koondada üleminekupaketiks, kusjuures iga koondamine on seotud *MPC-puu* konkreetse lehega (unikaalse paketi identifikaatoriga). Tänu *Deterministliku Bitcoin Commitment* (DBC) mehhanismile sisestatakse kogu teade `Tapret` või `Opret` väljundisse, sulgedes samal ajal eelmised pitsatid ja määratledes võimalusel uued. `Anchor* on otsene ühendus plokiahelasse salvestatud kohustuse ja kliendipoolse valideerimisstruktuuri (*kliendipoolne*) vahel.

Järgnevates peatükkides vaatleme kõiki komponente ja protsesse, mis on seotud oleku ülemineku koostamise ja kinnitamisega. Enamik neist elementidest on osa RGB-konsensusest, mis on rakendatud **RGB Core Library's**.

### Üleminekupakett

RGB-s on võimalik koondada erinevaid olekute üleminekuid, mis kuuluvad samasse lepingusse (st jagavad sama **ContractId**, mis on tuletatud Genesis **OpId**). Kõige lihtsamal juhul, nagu ülaltoodud näites Alice'i ja Bobi vahel, sisaldab **Transition Bundle** ainult ühte üleminekut. Kuid mitme maksja operatsioonide (näiteks coinjoins, Lightning-kanali avamine jne) toetamine tähendab, et mitu kasutajat võivad oma olekute üleminekuid kombineerida ühte kimbusesse.

Kui need üleminekud on kogutud, kinnitatakse need (MPC + DBC mehhanismi abil) ühte Bitcoini tehingusse:


- Iga oleku üleminek on räsitud ja rühmitatud üleminekupaketiks ;
- Üleminekupakett on ise räsitud ja sisestatud sellele lepingule vastavasse MPC-puu lehte (BundleId);
- MPC-puu võetakse lõpuks kasutusele "Opret" või "Tapret" abil tunnistustehingus, mis seega sulgeb tarbitud pitsatid ja määrab uued pitsatid.

Tehniliselt võttes saadakse MPC-lehele sisestatud **BundleId** märgistatud hashist, mida rakendatakse kimbu *InputMap* välja range serialiseerimise suhtes:

```txt
BundleId = SHA256( SHA256(bundle_tag) || SHA256(bundle_tag) || InputMap )
```

Kus näiteks `bundle_tag = urn:lnp-bp:rgb:bundle#2024-02-03`.

*InputMap* on andmestruktuur, mis loetleb iga näidistehingu sisendi "i" kohta viite vastava oleku ülemineku *OpId*-le. Näiteks:

```txt
InputMap =
N               input_0    OpId(input_0)    input_1    OpId(input_1)   ...    input_N-1  OpId(input_N-1)
|____________________| |_________||______________| |_________||______________|       |__________||_______________|
16-bit Little Endian   32-bit LE   32-byte hash
|_________________________| |_________________________|  ...  |___________________________|
MapElement1                MapElement2                       MapElementN
```


- "N" on tehingus olevate kirjete koguarv, mis viitavad "OpId"-ile;
- opId(input_j)` on ühe kimbu olevasse oleku ülemineku operatsiooni identifikaator.

Viidates igale sissekandele ainult üks kord ja järjekindlalt, väldime, et sama pitsat kuluks kaks korda kahes samaaegses oleku üleminekus.

### Riigi loomine ja aktiivne seisund

Riigi üleminekut saab seega kasutada vara omandiõiguse üleandmiseks ühelt isikult teisele. Need ei ole siiski ainsad võimalikud toimingud RGB-protokollis. Protokollis on määratletud kolm **lepingutoimingut** :


- Riigi üleminek** ;
- Genesis** ;
- Riiklik laiendus**.

Nendest operatsioonidest kutsutakse **Genesis** ja **State Extension** mõnikord "*State Generation operatsioonideks*", sest need loovad uusi olekuid, ilma et neid kohe sulgeksid. See on väga oluline punkt: **Genesis** ja **State Extension** ei hõlma pitseri sulgemist. Pigem määratlevad nad uue pitseri, mis tuleb seejärel kulutada järgneva **State Transition** abil, et olla tõeliselt kinnitatud plokiahela ajaloos.

![RGB-Bitcoin](assets/fr/064.webp)

Lepingu **aktiivne seisund** on sageli määratletud kui tehingute ajaloost (DAG) tulenevate viimaste seisundite kogum, alustades Genesis ja järgides kõiki ankruteid Bitcoini plokiahelas. Kõiki vanu seisundeid, mis on juba vananenud (st seotud kulutatud UTXOdega), ei loeta enam aktiivseks, kuid need on endiselt olulised ajaloo järjepidevuse kontrollimiseks.

### Genesis

Genesis on iga RGB lepingu lähtepunkt. Selle loob lepingu väljastaja ja selles määratakse algsed parameetrid vastavalt **skeemile**. RGB-märkide puhul võib Genesis määrata näiteks :


- Algselt loodud žetoonide arv ja nende omanikud;
- Võimaliku emissiooni ülemmäär ;
- Mis tahes uuesti väljaandmise eeskirjad ja millised osalejad on abikõlblikud.

Kuna tegemist on lepingu esimese tehinguga, ei viita Genesis ühelegi eelmisele seisundile ega sulge ühtegi pitserit. Selleks, et Genesis ilmuks ajalukku ja oleks kinnitatud, peab see siiski olema **tarbitud** (suletud) esimese oleku üleminekuga (sageli skaneerimise/automaatse kulutamise tehing emitendile endale või esialgne jaotamine kasutajatele).

### Riigi laiendamine

Riigi laiendused** pakuvad nutikate lepingute jaoks originaalset funktsiooni. Need võimaldavad lunastada teatavaid lepingu määratluses ette nähtud digitaalseid õigusi (*Valencies*), ilma et pitserit kohe sulgeda. Enamasti puudutab see :


- Jaotatud sümboolsete märkide emissioonid;
- Varade vahetamise mehhanismid ;
- Tingimuslik taasväljaandmine (mis võib hõlmata muude varade hävitamist jne).

Tehniliselt võttes viitab oleku laiendus *Redeemile* (teatud tüüpi RGB-sisend), mis vastab eelnevalt (näiteks Genesis või mõnes teises oleku üleminekus) määratletud *Valencyle*. See määratleb uue pitseri, mis on kättesaadav isikule või seisundile, kes sellest kasu saab. Selleks, et see pitser jõustuks, peab see olema kulutatud järgneva olekute üleminekuga.

![RGB-Bitcoin](assets/fr/065.webp)

Näiteks: Genesis loob väljaandmise õiguse (*Valency*). Seda saab kasutada volitatud tegutseja, kes seejärel ehitab riigi laienduse :


- See viitab Valentsile (lunastamisele);
- See loob uue *lähetuse* (uued *Owned State* andmed), mis viitab UTXO-le ;
- Selle uue UTXO omaniku poolt väljastatud tulevane riigimuutus kannab tegelikult üle või jaotab äsja väljastatud märgid.

### Lepingulise tegevuse komponendid

Tahaksin nüüd üksikasjalikult vaadata iga **Kontraktsiooni operatsiooni** RGB iga koostisosa. Lepinguoperatsioon on toiming, mis muudab lepingu seisundit ja mida õigustatud vastuvõtja valideerib kliendi poolel deterministlikult. Eelkõige näeme, kuidas lepinguoperatsioon võtab ühelt poolt arvesse lepingu **vanemat seisundit** (*Old State*) ja teiselt poolt **Uue seisundi** (*New State*) määratlust.

```txt
+---------------------------------------------------------------------------------------------------------------------+
|  Contract Operation                                                                                                 |
|                                                                                                                     |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|  | Ffv |     | ContractId | SchemaId |      | TransitionType | ExtensionType |      | Testnet |     | AltLayers1 |  |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Metadata                                      |  | Global State                                               |  |
|  |                                               |  | +----------------------------------+                       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  | |          Structured Data            |       |  | | |  GlobalStateType  | |  Data  | |     ...     ...       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  |                                               |  | +----------------------------------+                       |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|                                                                                                                     +---------> OpId |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|  | Inputs                                        |  | Assignments                                                |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #1                                  | |  | | Assignment #1                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ + ---------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #2                                  | |  | | Assignment #2                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  |       ...           ...          ...          |  |     ...          ...             ...                       |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Redeems                                       |  | Valencies                                                  |  |
|  |                                               |  |                                                            |  |
|  | +------------------------------+              |  |                                                            |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
| OpId +--------------> PrevOpId | | ValencyType | |  ...   ...   |  |  | ValencyType |  | ValencyType |         ...              |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
|  | +------------------------------+              |  |                                                            |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------+
```

Kui me vaatame ülaltoodud diagrammi, näeme, et lepinguoperatsioon sisaldab elemente, mis viitavad **Uusale olekule** ja teisi, mis viitavad uuendatud **Vana olekule**.

**Uue riigi** elemendid on :


- Ülesanded**, milles on määratletud :
 - **Seal Definition**;
 - **Omanikust riik**.
- **Global State**, mida saab muuta või rikastada ;
- Valencies**, mis võib olla määratletud State Transitionis või Genesis.

**Vana riik** on viidatud :


- Sisendid**, mis viitavad *Sisendite* eelnevatele olekute üleminekutele (Genesis ei ole olemas);
- Lunastused**, mis viitavad eelnevalt määratletud väärtustele (ainult riigilaiendustes).

Lisaks sellele sisaldab lepinguline toiming üldisemaid toimingule omaseid välju:


- ffv` (*Kiirendatud versioon*): 2baidine täisarv, mis näitab lepingu versiooni;
- transitionType` või ExtensionType`: 16-bitine täisarv, mis määrab ülemineku või laienduse tüübi vastavalt äriloogikale;
- `ContractId`: 32baideline number, mis viitab lepingu *OpId* Genesis. Sisaldab üleminekuid ja laiendusi, kuid mitte Genesis ;
- schemaId: esineb ainult Genesis, see on 32 baidi suurune hash, mis esindab lepingu struktuuri (*Schema*);
- testnet`: Boolean, mis näitab, kas olete Testneti või Mainneti võrgus. Ainult Genesis;
- altlayers1`: muutuja, mis tähistab alternatiivset kihti (sidechain või muu), mida kasutatakse andmete ankurdamiseks lisaks Bitcoinile. Esineb ainult Genesis ;
- metaandmed": väli, mis võib salvestada ajutist teavet, mis on kasulik kompleksse lepingu valideerimiseks, kuid mida ei tohi salvestada lõpliku staatuse ajalukku.

Lõpuks kondenseeritakse kõik need väljad kohandatud hashing-protsessi abil, et saada unikaalne sõrmejälg, "OpId". See "OpId" integreeritakse seejärel üleminekupaketti, mis võimaldab seda protokolli raames autentida ja valideerida.

Iga *Lepinguoperatsioon* on seega identifitseeritud 32 baidi pikkuse hashiga nimega `OpId`. See hash arvutatakse kõigi operatsiooni moodustavate elementide SHA256-hashiga. Teisisõnu on igal *Sõlmimisoperatsioonil* oma krüptograafiline kohustus, mis sisaldab kõiki andmeid, mis on vajalikud operatsiooni autentsuse ja järjepidevuse kontrollimiseks.

RGB-lepingut identifitseeritakse seejärel `ContractId` abil, mis on tuletatud Genesis `OpId`-st (kuna Genesis-eelset operatsiooni ei ole olemas). Konkreetselt võttes võtame Genesis `OpId`, pöörame baitide järjekorra ümber ja rakendame Base58 kodeeringut. See kodeering muudab `ContractId` lihtsamini käsitletavaks ja äratuntavaks.

### Staatuse uuendamise meetodid ja eeskirjad

**Lepingu olek** kujutab endast teabe kogumit, mida RGB-protokoll peab konkreetse lepingu puhul jälgima. See koosneb järgmistest elementidest:


- Üks globaalne riik**: see on lepingu avalik, globaalne osa, mis on kõigile nähtav;
- Üks või mitu omandatud riiki**: iga omandatud riik on seotud unikaalse pitseriga (ja seega ka UTXO Bitcoinis). Eristatakse :
    - **avalik** omandis olevad riigid,
    - **privaatse** omandiõigusega riigid.

![RGB-Bitcoin](assets/fr/066.webp)

*Global State* sisaldub otse *Contract Operation* ühe plokina. *Omaned States* on määratletud igas *Assignment'is* koos *Seal Definition'iga*.

RGB peamine omadus on viis, kuidas muudetakse globaalset riiki ja omandatud riike. Üldiselt on kahte tüüpi käitumist:


- Muutuv**: kui olekuelement on kirjeldatud muutuvana, siis iga uus operatsioon asendab eelmise oleku uue olekuga. Vanad andmed loetakse siis vananenudeks;
- Akumuleeriv**: kui olekute element on defineeritud akumuleerivana, siis iga uus operatsioon lisab eelmisele olekule uut teavet, ilma seda ülekirjutamata. Tulemuseks on omamoodi akumuleeritud ajalugu.

Kui lepingus ei ole seisundielementi määratletud muutuva või kumulatiivse elemendina, jääb see element järgnevate operatsioonide puhul tühjaks (teisisõnu, selle välja jaoks ei ole uusi versioone). See on lepingu skeem (st kodeeritud äriloogika), mis määrab, kas olek (globaalne või omandatud) on muutuv, kumulatiivne või fikseeritud. Kui Genesis on defineeritud, saab neid omadusi muuta ainult siis, kui leping ise seda lubab, näiteks konkreetse State Extension'i kaudu.

Alljärgnevas tabelis on näidatud, kuidas iga lepinguoperatsiooni tüüp võib manipuleerida (või mitte) globaalset ja omandatud riiki:

| Genesis | Riigi laiendamine | Riigi üleminek | State Transition |

| ---------------------------- | :-----: | :-------------: | :--------------: |

| **Add Global State** | + | | - | + | | | |

| k.a. | - | + | **Ülemaailmse seisundi muutumine** | - | + | | |

| **Omaniku staatuse lisamine** | + | | - | + | | |

| **Omaniku staatuse muutmine** | n/a | Ei | + | | |

| **Lisatakse väärtused** | + | + | + | + | + | + | | | |

**`+`** : tegevus võimalik, kui lepingu skeem seda võimaldab.

**`-`**: toiming peab olema kinnitatud järgneva oleku üleminekuga (oleku laiendamine üksi ei sulge ühekordset pitserit).

Lisaks sellele saab järgmises tabelis eristada iga andmetüübi ajalist ulatust ja ajakohastamisõigusi:

| Metaandmed | Üldine riik | Omaniku riik |

| ------------------------------- | ---------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |

| Määratletud ühele lepinguoperatsioonile | Määratletud ülemaailmselt lepingu jaoks | Määratletud igale pitserile (*Ülesanne*) | Määratletud ühele lepinguoperatsioonile | Määratletud ülemaailmselt lepingu jaoks | Määratletud igale pitserile (*Ülesanne*) | Määratletud igale pitserile (*Ülesanne*) | Määratletud igale lepingule

| Mitte-aktualiseeritav (efemeersed andmed) | Toimijate (emitent jne) poolt väljastatud tehing | Sõltub pitseri õigustatud omanikust (kes saab seda hilisemas tehingus kulutada) |

| Seisund on määratletud enne operatsiooni (eelmise operatsiooni *Seal Definition* poolt) | Seisund on määratud operatsiooni lõpus | Seisund on määratud operatsiooni lõpus | Seisund on määratud enne operatsiooni (eelmise operatsiooni *Seal Definition* poolt) | Seisund on määratud operatsiooni lõpus | Seisund on määratud enne operatsiooni (eelmise operatsiooni *Seal Definition* poolt) | Seisund on määratud enne operatsiooni (eelmise operatsiooni *Seal Definition* poolt)

### Ülemaailmne riik

Globaalset riiki kirjeldatakse sageli kui "keegi ei oma, kõik teavad". See sisaldab üldist teavet lepingu kohta, mis on avalikult nähtav. Näiteks tokeni väljaandmise lepingu puhul sisaldab see potentsiaalselt :


- Ticker (sümboolne sümboolne lühend): `ticker` ;
- Märgi täisnimi: `nimi` ;
- Täpsus (kümnendkohtade arv): `precision` ;
- Esialgne pakkumine (ja/või maksimaalne tokeni limiit): `issuedSupply` ;
- Väljaandmise kuupäev: "loodud" ;
- Õiguslikud andmed või muu avalik teave: "andmed".

Seda globaalset olekut saab paigutada avalikele ressurssidele (veebilehed, IPFS, Nostr, Torrent jne) ja levitada kogukonnale. Samuti ajendab majanduslik stiimul (vajadus hoida ja edastada neid märke jne) loomulikult lepingulisi kasutajaid ise neid andmeid säilitama ja levitama.

### Ülesanded

*Assignment* on põhistruktuur, mille abil saab määratleda :


- Pitser (*Pitseri määratlus*), mis osutab konkreetsele UTXO-le;
- *Omaned State*, st selle pitseriga seotud omadus või andmed.

*Ülesannet* võib vaadelda kui Bitcoini tehingu väljundi analoogi, kuid suurema paindlikkusega. Siin peitubki vara üleandmise loogika: *Assignment* seostab teatud tüüpi vara või õiguse (`AssignmentType`) pitseriga. See, kes omab selle pitseriga seotud UTXO eravõti (või kes saab seda UTXOd kulutada), loetakse selle *omandis oleva riigi* omanikuks.

Üks RGB suuri tugevusi on võimalus soovi korral *Seal Definition* ja *Owned State* väljad paljastada (*reveal*) või varjata (*conceal*). See pakub võimsat kombinatsiooni konfidentsiaalsuse ja selektiivsuse vahel. Näiteks saab tõestada, et üleminek on kehtiv, ilma kõiki andmeid avalikustamata, andes avalikustatud versiooni isikule, kes peab seda valideerima, samas kui kolmandad isikud näevad ainult varjatud versiooni (hash). Praktikas arvutatakse ülemineku `OpId` alati *salajaste* andmete põhjal.

![RGB-Bitcoin](assets/fr/067.webp)

#### Pitsati määratlus

*Seal Definition* on oma ilmnenud kujul nelja põhiväljaga: `txptr`, `vout`, `blinding` ja `method` :


- txptr**: see on viide UTXO-le Bitcoinis :
    - **Genesis'i pitseri** puhul osutab see otse olemasolevale UTXO-le (mis on seotud Genesis'iga);
    - **Graafilise pitseri** puhul saame :
        - Lihtne `txid`, kui see osutab konkreetsele UTXO-le,
        - Või `WitnessTx`, mis tähistab enesereferentsi: pitser osutab tehingule endale. See on eriti kasulik, kui väline UTXO ei ole kättesaadav, näiteks Lightning-kanali avamistehingute puhul või kui vastuvõtjal puudub UTXO.
- vout** : tehingu väljundnumber, mis on märgitud `txptr`. Esineb ainult standardse graafikapitsati puhul (mitte `WitnessTx` puhul);
- blinding**: juhuslik 8 baidi suurune number, et tugevdada konfidentsiaalsust ja vältida UTXO identiteedi räpase jõu abil tehtavaid katseid;
- method** : näitab kasutatud ankurdamismeetodit (`Tapret` või `Opret`).

Pitsatimääratluse *varjatud* vorm on nende 4 välja ühendamise SHA256-hash (märgistatud) koos RGB-le omase märgisega.

![RGB-Bitcoin](assets/fr/068.webp)

#### Omandis olevad riigid

Teine komponent *Assignment* on Owned State. Erinevalt globaalsest riigist võib see eksisteerida nii avalikul kui ka privaatsel kujul:


- Avalik omandis olev riik**: kõik teavad pitseriga seotud andmeid. Näiteks avalik pilt;
- Private Owned State**: andmed on peidetud, neid teab ainult omanik (ja vajadusel ka valideerija). Näiteks käes olevate žetoonide arv.

RGB määratleb neli võimalikku olekutüüpi (*StateTypes*) Owned State'i jaoks:


- Deklaratiivne**: ei sisalda numbrilisi andmeid, vaid ainult deklaratiivset õigust (nt hääleõigus). Varjatud ja avalikustatud vormid on identsed;
- Fungible**: esindab asendatavat kogust (nagu žetoonid). Avaldatud kujul on meil "summa" ja "siduva". Varjatud kujul on meil üks *Pederseni kohustus*, mis peidab summa ja siduva;
- Struktureeritud**: salvestab struktureeritud andmeid (kuni 64 kB). Avatud kujul on see andmeplokk. Varjatud kujul on see selle blobi märgistatud hash:

```txt
SHA-256(SHA-256(tag_data) || SHA-256(tag_data) || blob)
```

Näiteks :

```txt
tag_data = urn:lnp-bp:rgb:state-data#2024-02-12
```


- Attachments**: lingib faili (audio, pilt, binaarne jne) omandatud olekuga, salvestades faili hashi `file_hash`, MIME-tüübi `media type` ja krüptograafilise soola `salt`. Faili ennast hoitakse mujal. Varjatud kujul on see hash, mis on märgistatud kolme eelneva andmeelemendiga:

```txt
SHA-256(SHA-256(tag_attachment) || SHA-256(tag_attachment) || file_hash || media_type || salt)
```

Näiteks :

```txt
tag_attachment = urn:rgb:state-attach#2024-02-12
```

Kokkuvõttes on siin 4 võimalikku riigitüüpi avalikus ja varjatud vormis:

```txt
State                      Concealed form                              Revealed form
+---------------------------------------------------------------------------------------------------------
+--------------------------------------------------------------------------------+
|                                                                                |
Declarative        |                              < void >                                          |
|                                                                                |
+--------------------------------------------------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------+ +----------+       |
Fungible           | | Pedersen Commitement | | <========== |         | Amount | | Blinding |       |
| +----------------------+ |             |         +--------+ +----------+       |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------------------+        |
Structured         | |     Tagged Hash      | | <========== |         |     Data Blob      |        |
| +----------------------+ |             |         +--------------------+        |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             | +-----------+ +------------+ +------+ |
Attachments        | |     Tagged Hash      | | <========== | | File Hash | | Media Type | | Salt | |
| +----------------------+ |             | +-----------+ +------------+ +------+ |
+--------------------------+             +---------------------------------------+
```

| **Etteavaldav** | **Kõnestatav** | **Struktureeritud** | **Attachments** | |

| --------------------- | -------------- | ------------------------------------ | ----------------------------- | ---------------------------- |

| Puudub | 64-bitine märgistatud või märkimata täisarv | Mis tahes range andmetüüp | Mis tahes fail |

| Info type** | None | Signed or unsigned | Strict types | MIME type |

| Pederseni kohustus | Pimestamine koos pimestamisega | Faili pimestatud ID

| Suuruse piirangud** | N/A | 256 baiti | Kuni 64 KB | Kuni ~500 Gb |

### Sisendid

*Lepinguoperatsiooni* sisendid viitavad *Ülesannetele*, mis kulutatakse selles uues operatsioonis. Sisend näitab :


- prevOpId` : eelmise operatsiooni identifikaator (`OpId`), kus *Assignment* asus;
- assignmentType` : *Assignment* tüüp (näiteks `assetOwner` tokeni puhul) ;
- `Index`: eelmise `OpId`-iga seotud nimekirja *Assignment* indeks, mis määratakse pärast peidetud pitserite leksikograafilist sorteerimist.

Sisendid ei ilmu kunagi Genesis, kuna puuduvad eelnevad Assignments. Samuti ei ilmu nad State Extensions'is (sest State Extensions ei sulge pitsatid, vaid määratlevad uued pitsatid ümber Valencies'i alusel).

Kui meil on omandatud "Fungible" tüüpi olekud, kontrollib valideerimisloogika (skeemis toodud AluVM skripti kaudu) summade järjepidevust: sissetulevate märkide (*Sisendid*) summa peab olema võrdne väljaminevate märkide summaga (uues *Assignments*).

### Metaandmed

Väli **Metadata** võib olla kuni 64 KiB ja seda kasutatakse ajutiste andmete lisamiseks, mis on kasulikud valideerimiseks, kuid mida ei integreerita lepingu püsivasse olekusse. Näiteks võib siia salvestada keerukate skriptide vahepealseid arvutusmuutujaid. Seda ruumi ei ole ette nähtud salvestada globaalsesse ajalukku, mistõttu see jääb väljapoole Owned States või Global State reguleerimisala.

### Valentsused

Valencies** on originaalne RGB-protokolli mehhanism. Neid võib leida Genesis, State Transitions või State Extensions. Nad esindavad numbrilisi õigusi, mida saab aktiveerida State Extensioniga (*Redeems* kaudu) ja seejärel lõpule viia järgneva Transitioniga. Iga Valentsi identifitseeritakse `ValencyType` (16 bitti) abil. Selle semantika (reissue-õigus, tokeni vahetamine, põletusõigus jne) on määratletud skeemis.

Konkreetselt võiksime ette kujutada Genesis'i, mis määratleb "õiguse uuesti välja anda" valentsi. Riigi laiendus tarbib seda (*Redeem*), kui teatud tingimused on täidetud, et võtta kasutusele uus kogus märke. Seejärel saab sel viisil loodud pitseri omanikult lähtuv oleku üleminek neid uusi märke üle kanda.

### Lunastab

Lunastused on väärtuse ekvivalents sisenditele Assignmentide jaoks. Need ilmuvad ainult State Extensions'is, kuna seal aktiveeritakse eelnevalt määratletud Valentsi. Redeem koosneb kahest väljast:


- `PrevOpId` : selle operatsiooni `OpId`, mille puhul Valentsi määrati;
- `ValencyType`: Valentsi tüüp, mida soovite aktiveerida (iga `ValencyType` saab kasutada ainult üks kord State Extension'i poolt).

Näide: Lunastus võib vastata CoinSwap'i täitmisele, sõltuvalt sellest, mis on kodeeritud Valentsile.

### RGB staatuse omadused

Nüüd vaatleme mitmeid põhilisi RGB olekuomadusi. Eelkõige vaatleme :


- **Strict Type System**, mis kehtestab andmete täpse ja tüpiseeritud korralduse;
- Oluline on eraldada **valitsemine** ja **omand** ;
- **konsensuslik evolutsioonisüsteem** RGBs, mis hõlmab mõisteid *kiiresti edasi* ja *tagasi*.

Nagu alati, pidage meeles, et kõik, mis on seotud lepingu staatusega, valideeritakse kliendi poolel vastavalt protokollis sätestatud konsensusreeglitele, mille lõplik krüptograafiline viide on ankurdatud Bitcoini tehingutes.

#### Range tüübisüsteem

RGB kasutab *Strict Type System* ja deterministlikku serialiseerimisrežiimi (*Strict Encoding*). See korraldus on loodud selleks, et tagada lepinguandmete määratlemisel, käsitlemisel ja valideerimisel täiuslik reprodutseeritavus ja täpsus.

Paljudes programmeerimiskeskkondades (JSON, YAML...) võib andmestruktuur olla paindlik, isegi liiga lubav. RGB-s seevastu on iga välja struktuur ja tüübid määratletud selgesõnaliste piirangutega. Näiteks :


- Igal muutujal on konkreetne tüüp (näiteks 8-bitine täisarvu `u8` või 16-bitine täisarvu jne);
- Tüüpe võib koostada (sisemine tüüp). See tähendab, et te võite defineerida tüübi, mis põhineb teistel tüüpidel (nt koondtüüp, mis sisaldab `u8`-välja, `bool`-välja jne);
- Kollektsioone saab samuti määrata: nimekirjad (*list*), komplektid (*set*) või sõnastikud (*map*), mille järjestus on deterministlik;
- Iga väli on piiratud (*alumine piir* / *ülesmine piir*). Samuti kehtestame piirangud kogumite elementide arvule (containment);
- Andmed on baitidega joondatud ja serialiseerimine on rangelt määratletud ja üheselt mõistetav.

Tänu sellele rangele kodeerimisprotokollile :


- Väljade järjekord on alati sama, sõltumata kasutatavast rakendusest või programmeerimiskeelest;
- Sama andmekogumi põhjal arvutatud hashid on seega korratavad ja identsed (rangelt deterministlikud *sidemed*);
- Piirid takistavad andmete kontrollimatut kasvu (nt liiga palju välju);
- Selline kodeerimine hõlbustab krüptograafilist kontrollimist, kuna iga osaleja teab täpselt, kuidas andmeid järjestada ja hajutada.

Praktikas kompileeritakse struktuur (*Skeem*) ja sellest tulenev kood (*Liides* ja sellega seotud loogika). Lepingu määratlemiseks (tüübid, väljad, reeglid) ja range binaarvormingu genereerimiseks kasutatakse kirjeldavat keelt. Kompileerimisel on tulemuseks :


- *Mälu paigutus* igale väljale;
- Semantilised identifikaatorid (mis näitavad, kas muutuja nime muutmine mõjutab loogikat, isegi kui mälustruktuur jääb samaks).

Range tüübisüsteem võimaldab ka muudatuste täpset jälgimist: iga struktuurimuudatus (isegi välja nime muutmine) on tuvastatav ja võib põhjustada muutusi üldises jalajäljes.

Lõpuks toodab iga kompileerimine sõrmejälje, krüptograafilise tunnuse, mis tõendab koodi täpset versiooni (andmed, reeglid, valideerimine). Näiteks identifikaator kujul :

```txt
BEiLYE-am9WhTW1-oK8cpvw4-FEMtzMrf-mKocuGZn-qWK6YF#ginger-parking-nirvana
```

See võimaldab hallata konsensuse või rakendamise uuendusi, tagades samal ajal võrgus kasutatavate versioonide üksikasjaliku jälgitavuse.

Selleks, et RGB-lepingu olek ei muutuks kliendi poolel valideerimiseks liiga tülikaks, kehtestatakse konsensusreegliga valideerimisarvutustes osalevate andmete maksimaalseks suuruseks "2^16" baiti (64 Kio). See kehtib iga muutuja või struktuuri kohta: mitte rohkem kui 65536 baiti või samaväärne arv (32768 16-bitist täisarvu jne). See kehtib ka kollektsioonide (loendid, komplektid, kaardid) kohta, mille elemendid ei tohi ületada `2^16` elementi.

See piirang tagab :


- Reguleerib oleku ülemineku ajal manipuleeritavate andmete maksimaalset suurust;
- Ühilduvus virtuaalmasinaga (*AluVM*), mida kasutatakse valideerimisskriptide käivitamiseks.

#### Valideerimise != omandiõiguse paradigma

Üks RGB peamisi uuendusi on kahe mõiste range eraldamine:


- Valideerimine**: kontrollimine, et oleku üleminek vastab lepingu reeglitele (äriloogika, ajalugu jne);
- **omand** (omandiõigus või kontroll): Bitcoini UTXO omamine, mis võimaldab ühekordselt kasutatava pitseri kulutada (või sulgeda) ja seega toimub riigi üleminek.

Valideerimine** toimub RGB tarkvarapaketi tasandil (raamatukogud, *sõlmimisprotokoll* jne). Selle ülesanne on tagada, et lepingu sisemisi reegleid (summad, õigused jne) järgitakse. Vaatlejad või teised osalejad võivad samuti andmete ajalugu valideerida.

Omanik** seevastu tugineb täielikult Bitcoini turvalisusele. UTXO privaatvõtme omamine tähendab, et kontrollitakse võimalust käivitada uus üleminek (ühekordse pitseri sulgemine). Seega, isegi kui keegi saab andmeid näha või valideerida, ei saa ta seisundit muuta, kui ta ei oma asjaomast UTXO-d.

![RGB-Bitcoin](assets/fr/069.webp)

Selline lähenemisviis piirab klassikalisi haavatavusi, mis esinevad keerukamates plokiahelates (kus kogu aruka lepingu kood on avalik ja igaühe poolt muudetav, mis on mõnikord viinud häkkimiseni). RGB-s ei saa ründaja lihtsalt ahelas oleva olekuga suhelda, kuna õigust olekuga tegutseda (*omand*) kaitseb Bitcoini kiht.

Veelgi enam, selline lahtisidumine võimaldab RGB-l loomulikult integreeruda Lightning Networkiga. Lightning-kanaleid saab kasutada RGB varade kaasamiseks ja liigutamiseks, ilma et oleks vaja iga kord ahelas olevaid *sidemeid* kaasata. Seda RGB integreerimist Lightningiga vaatleme lähemalt kursuse hilisemates peatükkides.

#### Konsensuslikud arengud RGB valdkonnas

Lisaks semantilise koodi versioonimisele sisaldab RGB süsteemi lepingu konsensusreeglite arendamiseks või ajakohastamiseks aja jooksul. Evolutsiooni on kaks peamist vormi:


- Kiiresti edasi**
- Push-back** (prantsuse keeles)

Kiiresti toimub, kui varem kehtetu reegel muutub kehtivaks. Näiteks kui leping areneb nii, et see lubab uut tüüpi `AssignmentType` või uut välja :


- Seda ei saa võrrelda klassikalise plokiahela hardforkiga, kuna RGB töötab kliendipoolses valideerimises ja ei mõjuta plokiahela üldist ühilduvust;
- Praktikas näitab seda tüüpi muudatust lepinguoperatsiooni väli "Ffv" (*kiirendatud versioon*);
- Praegused omanikud ei kannata: nende staatus jääb kehtima;
- Uued abisaajad (või uued kasutajad) peavad seevastu uuendama oma tarkvara (rahakoti), et see tunneks uusi eeskirju.

Tagasilükkamine tähendab, et varem kehtinud reegel muutub kehtetuks. Seega on see reeglite "karmistamine", kuid mitte rangelt võttes softfork:


- See võib mõjutada olemasolevaid omanikke (nende varad võivad uues versioonis vananeda või muutuda kehtetuks);
- Me võime arvata, et me loome tegelikult uue protokolli: kes iganes võtab uue reegli vastu, lahkub vanast reeglist;
- Emitent võib otsustada varasid uuesti välja anda selles uues protokollis, sundides kasutajaid säilitama kaks eraldi rahakotti (üks vana protokolli jaoks, teine uue protokolli jaoks), kui nad soovivad hallata mõlemat versiooni.

Selles peatükis, mis käsitleb RGB-lepingu operatsioone, oleme uurinud selle protokolli aluseks olevaid aluspõhimõtteid. Nagu olete märganud, nõuab RGB-protokollile omane keerukus paljude tehniliste terminite kasutamist. Seega annan teile järgmises peatükis sõnastiku, mis võtab kokku kõik selles esimeses teoreetilises osas käsitletud mõisted koos kõigi RGBga seotud tehniliste terminite definitsioonidega. Seejärel vaatleme järgmises osas praktiliselt RGB-lepingute määratlust ja rakendamist.

## RGB sõnastik

<chapterId>545e16a4-3cca-44a3-9fd5-dbc5868abf97</chapterId>

Kui teil on vaja pöörduda tagasi selle lühikese sõnastiku juurde, mis sisaldab RGB-maailmas kasutatavaid olulisi tehnilisi termineid (loetletud tähestikulises järjekorras), on see teile kindlasti kasulik. See peatükk ei ole hädavajalik, kui olete juba aru saanud kõigest, mida me esimeses peatükis käsitlesime.

#### AluVM

Lühend AluVM tähistab "_Algorithmic logic unit Virtual Machine_", mis on registripõhine virtuaalmasin, mis on mõeldud arukate lepingute valideerimiseks ja hajutatud arvutuseks. Seda kasutatakse (kuid mitte ainult) RGB lepingute valideerimiseks. RGB-lepingus sisalduvaid skripte või operatsioone saab seega täita AluVM-keskkonnas.

Täiendav teave: [AluVM ametlik kodulehekülg](https://www.aluvm.org/)

#### Ankur

Ankur kujutab endast kliendipoolsete andmete kogumit, mida kasutatakse unikaalse _commitment_ sisalduse tõendamiseks tehingus. RGB-protokollis koosneb ankur järgmistest elementidest:


- Bitcoini tehingu identifikaator (TXID) **tunnistustehing** ;
- **Multiprotokolliga seotud kohustused (MPC)** ;
- **Deterministlik Bitcoin Commitment (DBC)**;
- **Extra Transaction Proof (ETP)**, kui kasutatakse **Tapret** kulukohustuste mehhanismi (vt selle mudeli kohta käivat jaotist).

Ankur on seega mõeldud selleks, et luua kontrollitav seos konkreetse Bitcoini tehingu ja RGB-protokolliga valideeritud privaatsete andmete vahel. See tagab, et need andmed on tõepoolest plokiahelas, ilma et nende täpne sisu oleks avalikult nähtav.

#### Ülesanne

RGB loogikas on määramine samaväärne tehingu väljundiga, mis muudab, ajakohastab või loob teatud omadusi lepingu olekus. Assignment koosneb kahest elemendist:


- A **Seal Definition** (viide konkreetsele UTXO-le) ;
- **Omaned State** (andmed, mis kirjeldavad selle uue omanikuga seotud riiki).

Seega näitab loovutamine, et osa riigist (näiteks vara) on nüüd eraldatud konkreetsele omanikule, kes on identifitseeritud UTXOga seotud ühekordse pitseri abil.

#### Äriloogika

Äriloogika koondab kõik lepingu reeglid ja sisemised toimingud, mida kirjeldab selle **skeem** (st lepingu enda struktuur). See dikteerib, kuidas ja millistel tingimustel võib lepingu seisund areneda.

#### Kliendipoolne valideerimine

Kliendipoolne valideerimine on protsess, mille käigus iga osapool (klient) kontrollib privaatselt vahetatud andmete kogumit vastavalt protokolli reeglitele. RGB puhul on need vahetatud andmed rühmitatud nn **kontsentratsioonideks**. Erinevalt Bitcoini protokollist, mis nõuab kõigi tehingute avaldamist ahelas, lubab RGB avalikult salvestada ainult _commitments_ (mis on ankurdatud Bitcoinis), samas kui oluline lepinguteave (üleminekud, kinnitused, tõendid) jääb ahelaväliseks, mida jagavad ainult asjaomased kasutajad.

#### Kohustus

Kohustus (krüptograafilises mõttes) on matemaatiline objekt, mida tähistatakse tähisega "C" ja mis saadakse deterministlikult struktureeritud andmete "m" (sõnum) ja juhusliku väärtuse "r" operatsioonist. Kirjutame :

$$
C = \text{commit}(m, r)
$$

See mehhanism koosneb kahest peamisest toimingust:


- Commit**: krüptograafilist funktsiooni rakendatakse sõnumi "m" ja juhusliku arvu "r" suhtes, et saada "C";
- Verify**: me kasutame `C`, `m` sõnumit ja `r` väärtust, et kontrollida, kas see kohustus on õige. Funktsioon tagastab `True` või `False`.

Kohustus peab järgima kahte omadust:


- Sidumine**: peab olema võimatu leida kahte erinevat sõnumit, mis toodavad sama "C" :

$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$

Näiteks :

$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$


- Varjamine**: teadmine `C` ei tohi paljastada `m` sisu.

RGB-protokollis lisatakse Bitcoini tehingusse kohustus, mis tõestab teatud teabe olemasolu teatud ajal, ilma et see teave ise paljastuks.

#### Konsignatsioon

**Konsignatsioon** koondab poolte vahel vahetatavad andmed, mille suhtes kohaldatakse RGB-süsteemi kliendipoolset valideerimist. On olemas kaks peamist saadetise kategooriat:


- Lepingu saadetis**: *väljaandja* (lepingu väljastaja) poolt esitatud teave, mis sisaldab initsialiseerimisandmeid, nagu skeem, genesis, liides ja liidese rakendamine.
- Ülekandmissaadetis**: maksja (*maksja*) poolt esitatud. Sisaldab kogu ajaloo seisundite üleminekutest, mis viivad lõppsaatmiseni (st maksja poolt saadud lõppseisundini).

Neid saadetisi ei registreerita avalikult plokiahelas; neid vahetatakse otse asjaomaste osapoolte vahel nende valitud sidekanali kaudu.

#### Leping

Leping on õiguste kogum, mis täidetakse digitaalselt mitme osalise vahel RGB-protokolli kaudu. Sellel on aktiivne olek ja äriloogika, mis on määratletud skeemi abil, mis määrab kindlaks, millised toimingud on lubatud (ülekanded, laiendused jne). Lepingu olek ja selle kehtivusreeglid on väljendatud skeemis. Igal ajahetkel areneb leping ainult vastavalt sellele, mida see skeem ja valideerimisskriptid (mida käivitatakse näiteks AluVMis) lubavad.

#### Lepinguline tegevus

Lepingu operatsioon on lepingu staatuse ajakohastamine vastavalt skeemi reeglitele. RGB-s on olemas järgmised operatsioonid:


- Riigi üleminek** ;
- Genesis** ;
- Riiklik laiendus**.

Iga operatsioon muudab olekut, lisades või asendades teatud andmeid (globaalne olek, omandatud olek...).

#### Lepinguosaline

Lepingus osaleja on osaleja, kes osaleb lepinguga seotud toimingutes. RGB-s eristatakse :


- Lepingu emitent, kes loob Genesis'i (lepingu päritolu);
- Lepingupooled, s.t. lepingujärgsete õiguste omanikud;
- Avalikud isikud, kes võivad ehitada riiklikke laiendusi, kui leping pakub avalikkusele kättesaadavaid Valencies.

#### Lepingulised õigused

Lepingulised õigused viitavad erinevatele õigustele, mida RGB lepingus osalejad võivad kasutada. Need jagunevad mitmesse kategooriasse:


- Omandiõigused**, mis on seotud konkreetse UTXO omandiõigusega (_Seal Definition_ kaudu);
- Täitjaõigused**, st võime ehitada üks või mitu üleminekut (State Transitions) vastavalt skeemile ;
- Avalikud õigused**, kui skeem lubab teatavaid avalikke kasutusviise, näiteks riigi laienduse loomine Valentsi lunastamise kaudu.

#### Lepingu riik

Lepingu olek vastab lepingu hetkeseisundile. See võib koosneda nii avalikest kui ka privaatsetest andmetest, mis kajastavad lepingu seisundit. RGB eristab :


- **Global State**, mis sisaldab lepingu avalikke omadusi (mis on loodud Genesis'is või lisatud volitatud uuenduste kaudu);
- Omandis olevad riigid**, mis kuuluvad konkreetsetele omanikele, kes on kindlaks määratud nende UTXOde järgi.

#### Deterministlik Bitcoin Commitment - DBC

Deterministlik Bitcoin Commitment (DBC) on reeglite kogum, mida kasutatakse Bitcoini tehingu _commitment_ tõestatavaks ja unikaalseks registreerimiseks. RGB-protokollis on kaks peamist DBC vormi:


- Opret**
- Tapret**

Need mehhanismid määravad täpselt kindlaks, kuidas Bitcoini tehingu väljundis või struktuuris kodeeritakse _commitment_, et tagada selle kohustuse deterministlik jälgitavus ja kontrollitavus.

#### Suunatud atsükliline graaf - DAG

DAG (või *Atsükliline juhitav graaf*) on tsüklivaba graaf, mis võimaldab topoloogilist planeerimist. Plokiahelad, nagu ka RGB lepingute _shardid_, saab esitada DAGide abil.

Täiendav teave: [Directed Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph)

#### Graveerimine

Graveering on vabatahtlik andmerida, mille lepingu järjestikused omanikud võivad sisestada lepingu ajalukku. See funktsioon on olemas näiteks **RGB21** liideses ja võimaldab lisada lepingu ajalukku mälestus- või kirjeldavat teavet.

#### Täiendav tehingu tõendamine - ETP

ETP (*Extra Transaction Proof*) on ankurduse osa, mis sisaldab **Tapret** *commitment* (_taproot_ kontekstis) valideerimiseks vajalikke täiendavaid andmeid. See sisaldab muu hulgas taproot-skripti sisemist avalikku võtit (_internal PubKey_) ja teavet, mis on omane _Script Path Spendile_.

#### Genesis

Genesis viitab skeemiga reguleeritud andmekogumile, mis moodustab RGB-s iga lepingu algse seisundi. Seda võib võrrelda Bitcoini _Genesis Block_ kontseptsiooniga või Coinbase'i tehingu kontseptsiooniga, kuid siinkohal _kliendipoolsel_ ja RGB tokeni tasandil.

#### Ülemaailmne riik

Üldine olek on lepingu olekus sisalduvate avalike omaduste kogum. See on määratletud Genesis ja seda saab sõltuvalt lepingu reeglitest ajakohastada volitatud üleminekutega. Erinevalt Owned States'ist ei kuulu Global State konkreetsele üksusele; see on lähemal lepingu avalikule registrile.

#### Kasutajaliides

Kasutajaliides on juhiste kogum, mida kasutatakse skeemi või lepinguoperatsioonide ja nende olekute raames koostatud binaarsete andmete dekodeerimiseks, et muuta need kasutaja või tema rahakoti jaoks loetavaks. See toimib tõlgenduskihina.

#### Kasutajaliidese rakendamine

Kasutajaliidese rakendamine on deklaratsioonide kogum, mis seob **liidese** ja **skeemi**. See võimaldab liidese enda poolt teostatavat semantilist tõlget, nii et kasutaja või asjaomane tarkvara (rahakotid) saaks lepingu toorandmeid mõista.

#### Arve

Arve on [base58](https://en.wikipedia.org/wiki/Binary-to-text_encoding#Base58) kujul kodeeritud URL, mis sisaldab andmeid, mis on vajalikud **State Transition** (maksja poolt) koostamiseks. Teisisõnu on see arve, mis võimaldab vastaspoolel (*maksjal*) luua vastav üleminek vara üleandmiseks või lepingu oleku uuendamiseks.

#### Lightning Network

Lightning Network on Bitcoini detsentraliseeritud maksekanalite (või _state channels_) võrgustik, mis koosneb 2/2 mitme allkirjaga rahakotist. See võimaldab kiireid ja odavaid _off-chain_ tehinguid, tuginedes samal ajal Bitcoini 1. kihile vahekohtu (või sulgemise) jaoks, kui see on vajalik.

Lisateabe saamiseks selle kohta, kuidas Lightning töötab, soovitan teil läbida selle teise kursuse:

https://planb.network/courses/lnp201
#### Mitme protokolliga seotud kohustused - MPC

Multi Protocol Commitment (MPC) viitab RGB-s kasutatavale Merkle-puu struktuurile, mis hõlmab ühe Bitcoini tehingu raames mitmeid **Transitsioonipakke** erinevatest lepingutest. Idee on koondada mitu kohustust (mis võivad vastata erinevatele lepingutele või erinevatele varadele) ühte ankurduspunkti, et optimeerida plokiruumi hõivatust.

#### Omandis olev riik

Omandis olev riik on lepinguriigi osa, mis on ümbritsetud loovutamisega ja seotud konkreetse valdajaga (UTXO-le osutava ühekordse pitseri kaudu). See esindab näiteks digitaalset vara või konkreetset lepingulist õigust, mis on sellele isikule omistatud.

#### Omanikuks olemine

Omandiõigus viitab võimalusele kontrollida ja kulutada UTXOd, millele viitab pitsatimääratlus. Kui omandatud riik on seotud UTXOga, on selle UTXO omanikul potentsiaalselt õigus seotud riiki üle anda või arendada vastavalt lepingu reeglitele.

#### Osaliselt allkirjastatud Bitcoini tehing - PSBT

PSBT (_Partially Signed Bitcoin Transaction_) on Bitcoini tehing, mis ei ole veel täielikult allkirjastatud. Seda võib jagada mitme üksuse vahel, millest igaüks saab lisada või kontrollida teatud elemente (allkirjad, skriptid...), kuni tehing loetakse valmis olevat ahelasiseseks levitamiseks.

Täiendav teave: [BIP-0174](https://github.com/bitcoin/bips/blob/master/bip-0174.mediawiki)

#### Pederseni kohustus

Pederseni kohustus on krüptograafilise kohustuse tüüp, millel on omadus olla **homomorfne** liitmisoperatsiooni suhtes. See tähendab, et kahe kohustuse summat on võimalik kinnitada ilma üksikuid väärtusi avaldamata.

Formaalselt, kui :

$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$

siis :

$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$

See omadus on kasulik näiteks selleks, et varjata vahetatud žetoonide summasid, kuid samas on võimalik kontrollida summasid.

Täiendav teave: [Pedersen commitment](https://link.springer.com/chapter/10.1007/3-540-46766-1_9)

#### Lunastada

Riigi laiendamise puhul viitab lunastamine varem deklareeritud **Valentsuse** tagasivõitmisele (või ärakasutamisele). Kuna valentsus on avalik õigus, võimaldab lunastamine volitatud osalejal nõuda konkreetset lepingu riigi laiendamist.

#### Skeem

RGB-skeem on deklareeriv kood, mis kirjeldab lepingu toimimist reguleerivate muutujate, reeglite ja äriloogika (*äriloogika*) kogumit. Skeem määratleb olekute struktuuri, lubatud üleminekutüübid ja valideerimistingimused.

#### Pitsati määratlus

Pitsatimääratlus on loovutamise osa, mis seostab _kohustust_ uue omaniku omandis oleva UTXOga. Teisisõnu, see näitab, kus tingimus asub (millises UTXOs), ja kehtestab vara või õiguse omandiõiguse.

#### Shard

Shard esindab haru DAGis RGB-lepingu riigi üleminekute ajaloost. Teisisõnu, see on lepingu üldise ajaloo sidus alamhulk, mis vastab näiteks üleminekute järjestusele, mis on vajalik konkreetse vara kehtivuse tõestamiseks alates _Genesis_.

#### Ühekordselt kasutatav pitser

Ühekordselt kasutatav pitsat on krüptograafiline lubadus, millega lubatakse veel tundmatu sõnum, mis avaldatakse ainult üks kord tulevikus ja mis peab olema teada kõigile konkreetse sihtrühma liikmetele. Eesmärgiks on vältida mitme konkureeriva kohustuse loomist sama pitseri jaoks.

#### Stash

Stash on kliendipoolsete andmete kogum, mille kasutaja salvestab ühe või mitme RGB-lepingu jaoks valideerimise eesmärgil (*Kliendipoolne valideerimine*). See hõlmab üleminekuajalugu, saadetisi, kehtivuse tõendeid jne. Iga valdaja säilitab ainult need osad ajaloost, mida ta vajab (*shards*).

#### Riigi laiendamine

Riigi laiendamine on lepinguline operatsioon, mida kasutatakse riigi uuenduste uuesti käivitamiseks, lunastades eelnevalt deklareeritud **Valitsused**. Selleks, et oleku laiendamine oleks tõhus, tuleb see seejärel sulgeda oleku üleminekuga (mis ajakohastab lepingu lõpliku oleku).

#### Riigi üleminek

Seisundi üleminek on operatsioon, mis muudab RGB-lepingu seisundi uude seisundisse. See võib muuta globaalse oleku ja/või omandatud oleku andmeid. Praktikas kontrollitakse iga üleminekut skeemireeglitega ja ankurdatakse Bitcoini plokiahelas _commitment_ kaudu.

#### Taproot

Viitab Bitcoini Segwit v1 tehinguformaadile, mille kehtestasid [BIP341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki) ja [BIP342](https://github.com/bitcoin/bips/blob/master/bip-0342.mediawiki). Taproot parandab skriptide konfidentsiaalsust ja paindlikkust, muutes eelkõige tehingud kompaktsemaks ja raskemini eristatavaks.

#### Terminal Consignment - kaubasaadetise lõpp-punkt

Terminal Consignment (või _Consignment Endpoint_) on *transfer consignment*, mis sisaldab lepingu lõppseisundit, sealhulgas saaja arve (*payee*) alusel loodud State Transition'i. Seega on see ülekande lõpp-punkt, mis sisaldab vajalikke andmeid, mis tõendavad, et omandiõigus või riik on üle läinud.

#### Üleminekupakett

Üleminekupakett on hulk RGB-riigi üleminekuid (mis kuuluvad samasse lepingusse), mis on kõik seotud sama ***tunnistustehinguga*** Bitcoinis. See võimaldab koondada mitu uuendust või ülekannet ühte ahelasisesesse ankrusse.

#### UTXO

Bitcoini UTXO (*Unspent Transaction Output*) on määratletud tehingu hashi ja väljundindeksiga (*vout*). Mõnikord nimetatakse seda ka _väljundiks_. RGB-protokollis võimaldab viide UTXO-le (**Seal Definition** kaudu) leida **Owned State**, st plokiahelas hoitava vara.

#### Valentsus

Valentsus on avalik õigus, mis ei nõua riiklikku ladustamist kui sellist, kuid mida saab lunastada **riigi laiendamise** kaudu. Seega on see kõigile (või teatavatele mängijatele) avatud võimalus, mis on deklareeritud lepingu loogikas, et teostada hiljem teatav laiendus.

#### Tunnistaja tehing

Tunnistaja tehing on Bitcoini tehing, mis sulgeb ühekordselt kasutatava pitseri sõnumi ümber, mis sisaldab mitmeprotokolli (MPC). See tehing kulutab UTXO või loob selle, et RGB-protokolliga seotud kohustus oleks pitseeritud. See toimib ahelasiseselt tõendina, et seisund on seatud konkreetsel ajahetkel.

# RGB programmeerimine

<partId>148a7436-d079-56d9-be08-aaa4c14c6b3a</partId>

## RGB lepingute rakendamine

<chapterId>8333ea5f-51c7-5dd5-b1d7-47d491e58e51</chapterId>

![video](https://youtu.be/Uo1UoxiImsI)

Selles peatükis vaatleme lähemalt, kuidas RGB-lepingut defineeritakse ja rakendatakse. Me näeme, millised on RGB-lepingu komponendid, milline on nende roll ja kuidas nad on üles ehitatud.

### RGB lepingu komponendid

Siiani oleme juba arutanud **Genesis**, mis kujutab endast lepingu alguspunkti, ja me nägime, kuidas see sobib kokku *Lepingu operatsiooni* loogikaga ja protokolli olekuga. RGB lepingu täielik määratlus ei piirdu siiski ainult Genesisega: see hõlmab kolme täiendavat komponenti, mis koos moodustavad rakendamise tuuma.

Esimest komponenti nimetatakse **Skeemiks**. See on fail, mis kirjeldab lepingu põhistruktuuri ja äriloogikat (*äriloogika*). Selles määratakse kindlaks kasutatavad andmetüübid, valideerimisreeglid, lubatud toimingud (nt algne märgiste väljastamine, ülekanded, eritingimused jne) - lühidalt öeldes üldine raamistik, mis määrab, kuidas leping toimib.

Teine komponent on **liides**. See keskendub sellele, kuidas kasutajad (ja seega ka portfelli tarkvara) selle lepinguga suhtlevad. See kirjeldab semantikat, st erinevate väljade ja tegevuste loetavat esitust. Seega, kui skeem määratleb, kuidas leping tehniliselt toimib, siis kasutajaliides määratleb, kuidas neid funktsioone esitada ja eksponeerida: meetodite nimed, andmete kuvamine jne.

Kolmas komponent on **Liidese rakendamine**, mis täiendab kahte eelmist, olles omamoodi sild skeemi ja liidese vahel. Teisisõnu, see ühendab liidese poolt väljendatud semantika skeemis määratletud reeglitega. See rakendus on see, mis haldab näiteks rahakotti sisestatud parameetri ja protokolliga kehtestatud binaarse struktuuri vahelist konverteerimist või valideerimisreeglite koostamist masinakeeles.

Selline modulaarsus on RGB huvitav omadus, sest see võimaldab erinevatel arendajarühmadel töötada eraldi nende aspektidega (*Skeem*, *Liides*, *Implementatsioon*), kui nad järgivad protokolli konsensusreegleid.

Kokkuvõttes koosneb iga leping :


- Genesis**, mis on lepingu algseisund (ja mida võib võrrelda spetsiaalse tehinguga, mis määratleb vara, õiguse või mis tahes muu parameetrile vastavate andmete esmase omandiõiguse);
- Skeem**, mis kirjeldab lepingu äriloogikat (andmetüübid, valideerimisreeglid jne);
- Liides**, mis pakub semantilist kihti nii rahakottidele kui ka inimkasutajatele, selgitades tehingute lugemist ja täitmist;
- Rakendus** liides, mis katab lõhe äriloogika ja esitusviisi vahel, tagamaks, et lepingu määratlus on kooskõlas kasutajakogemusega.

![RGB-Bitcoin](assets/fr/070.webp)

Oluline on märkida, et selleks, et rahakott saaks hallata RGB vara (olgu see siis asendatav sümboolne märk või mis tahes õigus), peavad kõik need elemendid olema kokku pandud: *Skeem*, *Liides*, *Liidese rakendamine* ja *Genesis*. See edastatakse ***lepingu saadetise*** kaudu, st andmepaketi kaudu, mis sisaldab kõike, mis on vajalik kliendipoolse lepingu valideerimiseks.

Nende mõistete selgitamiseks on siin kokkuvõtlik tabel, milles võrreldakse RGB-lepingu komponente kas objektorienteeritud programmeerimise (OOP) või Ethereumi ökosüsteemis juba tuntud mõistetega:

| RGB lepingu komponent | Tähendus | OOP ekvivalent | Ethereum ekvivalent |

| ---------------------------- | --------------------------------------- | -------------------------------------------------- | ---------------------------------- |

| Klassi konstruktor | Lepingu konstruktor | Lepingu algseisund

| Klass | Lepingu äriloogika

| Lepingu semantika | Liides (Java) / tunnus (Rust) / protokoll (Swift) | ERC standard |

| Application Binary Interface (ABI) | Impl (Rust) / Implements (Java) | Semantika ja loogika kaardistamine

Vasakpoolne veerg näitab RGB-protokollile omaseid elemente. Keskmine veerg näitab iga komponendi konkreetset funktsiooni. Seejärel leiame veerus "OOP-ekvivalent" samaväärse termini objektorienteeritud programmeerimises:


- **Genesis** mängib sarnast rolli nagu *Klassi konstruktor*: siin initsialiseeritakse lepingu olek;
- **Skeem** on klassi kirjeldus, st selle omaduste, meetodite ja aluseks oleva loogika määratlus;
- **Interface** vastab *interfaces* (Java), *traits* (Rust) või *protocols* (Swift): need on funktsioonide, sündmuste, väljade ... avalikud definitsioonid;
- **Liidese rakendamine** vastab *Impl* Rustis või *Implements* Javas, kus me täpsustame, kuidas kood tegelikult täidab liideses väljakuulutatud meetodeid.

Ethereumi kontekstis on Genesis lähemal *lepingu konstruktorile*, Schema lepingu definitsioonile, Interface standardile nagu ERC-20 või ERC-721 ja Interface Implementation ABI-le (*Application Binary Interface*), mis määrab kindlaks lepinguga suhtlemise formaadi.

RGB modulaarsuse eelis seisneb ka selles, et erinevad sidusrühmad võivad kirjutada näiteks oma liidese implementatsiooni, kui nad järgivad *Skeemi* loogikat ja *Liidese* semantikat. Seega võib emitent välja töötada uue, kasutajasõbralikuma esiosa (liidese), ilma lepingu loogikat muutmata, või vastupidi, ta võib laiendada skeemi, et lisada funktsioone, ja pakkuda kohandatud liidese rakendamise uut versiooni, samas kui vanad rakendused jäävad põhifunktsioonide osas kehtima.

Kui me koostame uue lepingu, genereerime Genesis (esimene samm vara väljaandmisel või levitamisel), samuti selle komponendid (skeem, liides, liidese rakendamine). Pärast seda on leping täielikult toimiv ja seda saab levitada rahakottidele ja kasutajatele. See meetod, kus Genesis on kombineeritud nende kolme komponendiga, tagab suure kohandatavuse (igal lepingul võib olla oma loogika), detsentraliseerituse (igaüks saab anda oma panuse konkreetsesse komponendisse) ja turvalisuse (valideerimine jääb rangelt protokolliga määratletud, sõltumata suvalisest ahelasisesest koodist, nagu see on sageli teiste plokiahelate puhul).

Tahaksin nüüd lähemalt uurida igaüht neist komponentidest: **Skeem**, **Liidese** ja **Liidese rakendamine**.

### Skeem

Eelmises punktis nägime, et RGB ökosüsteemis koosneb leping mitmest elemendist: Genesis, mis määrab algse seisundi, ja mitmetest muudest täiendavatest komponentidest. Skeemi eesmärk on kirjeldada deklaratiivselt kogu lepingu äriloogikat, st andmete struktuuri, kasutatavaid tüüpe, lubatud operatsioone ja nende tingimusi. Seetõttu on see väga oluline element lepingu toimimiseks kliendi poolel, sest iga osaleja (näiteks rahakott) peab kontrollima, et talle edastatavad olekute üleminekud vastavad skeemis määratletud loogikale.

Skeemi võib võrrelda "klassiga" objektorienteeritud programmeerimises (OOP). Üldiselt toimib see mudelina, mis määratleb lepingu komponendid, näiteks :


- Erinevad omaniku staatused ja ülesanded ;
- Valentsused, st eriõigused, mida saab käivitada (*tagastada*) teatud toimingute puhul;
- Globaalse oleku väljad, mis kirjeldavad lepingu globaalseid, avalikke ja ühiseid omadusi;
- Genesis struktuur (esimene toiming, mis aktiveerib lepingu) ;
- Riigi üleminekute ja riigi laienduste lubatud vormid ning kuidas need operatsioonid võivad muuta ;
- Iga toiminguga seotud metaandmed, et salvestada ajutist või täiendavat teavet;
- Reeglid, mis määravad kindlaks, kuidas lepingu sisemised andmed võivad areneda (näiteks kas väli on muutuv või kumulatiivne);
- Kehtivaks peetavate toimingute jadad: näiteks üleminekute järjekord, mida tuleb järgida, või loogiliste tingimuste kogum, mis peab olema täidetud.

![RGB-Bitcoin](assets/fr/071.webp)

Kui vara *väljaandja* RGBs avaldab lepingu, esitab ta sellega seotud Genesis ja Schema. Kasutajad või rahakotid, kes soovivad varaga suhelda, hangivad selle skeemi, et mõista lepingu loogikat ja hiljem kontrollida, et üleminekud, milles nad osalevad, on seaduslikud.

Igaüks, kes saab teavet RGB vara kohta (nt sümboolika ülekandmine), peab kõigepealt valideerima selle teabe skeemi alusel. See hõlmab skeemi koostamise kasutamist, et :


- Kontrollida, et omandatud olekud, määrangud ja muud elemendid on õigesti defineeritud ja et nad järgivad kehtestatud tüüpe (nn *strict type system*);
- Kontrollida, et üleminekureeglid (valideerimisskriptid) on täidetud. Neid skripte saab käivitada AluVMi kaudu, mis on kliendi poolel ja vastutab äriloogika järjepidevuse kontrollimise eest (ülekandesumma, eritingimused jne).

Praktikas ei ole skeem käivitatav kood, nagu on näha plokiahelates, mis salvestavad ahelas olevat koodi (EVM Ethereumis). Vastupidi, RGB eraldab äriloogika (deklaratiivne) plokiahelas täidetavast koodist (mis piirdub krüptograafiliste ankurdustega). Seega määrab skeem reeglid, kuid nende reeglite kohaldamine toimub väljaspool plokiahelat, iga osaleja juures, vastavalt kliendipoolse valideerimise põhimõttele.

Skeem tuleb kompileerida, enne kui RGB rakendused saavad seda kasutada. See kompileerimine tekitab binaarfaili (nt `.rgb`) või krüpteeritud binaarfaili (`.rgba`). Kui rahakott impordib selle faili, teab ta :


- Kuidas iga andmetüüp (täisarvud, struktuurid, massiivid...) näeb välja tänu rangele tüübisüsteemile ;
- Kuidas Genesis peaks olema struktureeritud (et mõista vara initsialiseerimist);
- Erinevad operatsioonitüübid (State Transitions, State Extensions) ja kuidas need võivad muuta olekut ;
- Skriptimisreeglid (mis on esitatud skeemis), mida AluVM mootor rakendab operatsioonide kehtivuse kontrollimiseks.

Nagu eelmistes peatükkides selgitatud, annab *strict type system* meile stabiilse, deterministliku kodeerimisformaadi: kõik muutujad, olgu need siis Owned States, Global States või Valencies, on täpselt kirjeldatud (suurus, alumine ja ülemine piir, kui vaja, signitud või märkimata tüüp jne). Samuti on võimalik defineerida sisemisi struktuure, näiteks keeruliste kasutusjuhtumite toetamiseks.

Valikuliselt võib skeem viidata juurskeemile `SchemaId`, mis hõlbustab olemasoleva põhistruktuuri (malli) taaskasutamist. Sel viisil saab lepingut edasi arendada või luua variante (nt uut tüüpi sümboli) juba tõestatud mallist. Selline modulaarsus väldib vajadust luua uuesti terveid lepinguid ja soodustab parimate tavade standardimist.

Teine oluline punkt on see, et oleku arengu loogika (ülekanded, uuendused jne) on kirjeldatud skeemis skriptide, reeglite ja tingimuste kujul. Seega, kui lepingu projekteerija soovib lubada uuesti väljastada või kehtestada põletusmehhanismi (märgiste hävitamine), saab ta skeemi valideerimisosas täpsustada vastavad skriptid AluVMi jaoks.

#### Erinevus programmeeritavatest ahelates olevatest plokiahelatest

Erinevalt sellistest süsteemidest nagu Ethereum, kus aruka lepingu kood (täidetav) on kirjutatud plokiahelasse, salvestab RGB lepingu (selle loogika) ahelaväliselt, kompileeritud deklaratiivse dokumendi kujul. See tähendab, et :


- Bitcoini võrgu igas sõlmes ei ole Turingi täis VM-i. RGB-lepingu reegleid ei täideta plokiahelas, vaid igas kasutajas, kes soovib seisundit valideerida;
- Lepingu andmed ei reosta plokiahelat: Bitcoini tehingutesse on (Tapret'i või Opret'i kaudu) lisatud ainult krüptograafilised tõendid (*kohustused*);
- Skeemi saab uuendada või tagasi lükata (*kiiresti edasi*, *tagasi lükata* jne), ilma et see nõuaks Bitcoini plokiahelas hargnemist. Rahakotid peavad lihtsalt importima uue skeemi ja kohanema konsensuse muudatustega.

#### Kasutamine emitendi ja kasutajate poolt

Kui *emitent* loob vara (näiteks mitteinflatsioonilise asendatava märgi), valmistab ta :


- Skeem, mis kirjeldab heite-, ülekandereegleid jne;
- Skeemile kohandatud Genesis (koos väljastatud märkide koguarvuga, esialgse omaniku identiteediga, mis tahes eriväärtustega kordusväljastamise puhul jne).

Seejärel teeb ta kompileeritud skeemi (faili `.rgb`) kasutajatele kättesaadavaks, nii et igaüks, kes saab selle sümboli ülekande, saab kohapeal kontrollida operatsiooni järjepidevust. Ilma selle skeemita ei saaks kasutaja tõlgendada olekuandmeid ega kontrollida nende vastavust lepingu reeglitele.

Seega, kui uus rahakott soovib mingit vara toetada, peab ta lihtsalt integreerima asjakohase skeemi. See mehhanism võimaldab lisada ühilduvust uutele RGB-vara tüüpidele, ilma rahakoti tarkvarabaasi invasiivselt muutmata: kõik, mis on vaja, on importida Schema binaarset faili ja mõista selle struktuuri.

Skeem määratleb äriloogika RGB-s. Selles on loetletud lepingu arengureeglid, selle andmete struktuur (Owned States, Global State, Valencies) ja sellega seotud valideerimisskriptid (mida AluVM saab käivitada). Tänu sellele deklaratiivsele dokumendile on lepingu määratlus (kompileeritud fail) selgelt eraldatud reeglite tegelikust täitmisest (kliendipoolne). Selline lahtisidumine annab RGB-le suure paindlikkuse, võimaldades mitmesuguseid kasutusjuhtumeid (asendatavad märgid, NFT, keerukamad lepingud), vältides samas programmeeritavatele ahelates olevatele plokiahelatele omaseid keerukusi ja puudusi.

#### Skeemi näide

Vaatame konkreetset näidet RGB-lepingu skeemi kohta. See on väljavõte Rustis failist `nia.rs` (initsiaalid "*Non-Inflatable Assets*"), mis määratleb mudeli asendatavatele žetoonidele, mida ei saa pärast nende esialgset pakkumist uuesti välja anda (mitteinflatsiooniline vara). Seda tüüpi märke võib RGB universumis vaadelda kui Ethereumi ERC20-i ekvivalenti, st asendatavaid märke, mis järgivad teatavaid põhireegleid (nt ülekannete, varude initsialiseerimise jne).

Enne koodiga tutvumist tasub meenutada RGB skeemi üldist struktuuri. Seal on rida deklaratsioone, mis raamivad :


- Võimalik `SchemaId`, mis näitab teise põhiskeemi kasutamist mallina;
- **Globaalriigid** ja **Omanikmesriigid** (koos nende rangete tüüpidega) ;
- Väärtused** (kui neid on);
- **Operatsioonid** (Genesis, State Transitions, State Extensions), mis võivad viidata nendele seisunditele ja valentsidele;
- **Strict Type System**, mida kasutatakse andmete kirjeldamiseks ja valideerimiseks;
- Valideerimisskriptid** (käivitatakse AluVMi kaudu).

![RGB-Bitcoin](assets/fr/072.webp)

Allpool olev kood näitab Rusti skeemi täielikku määratlust. Me kommenteerime seda osade kaupa, järgides allpool olevaid märkusi (1) kuni (9):

```rust
// ===== PART 1: Function Header and SubSchema =====
fn nia_schema() -> SubSchema {
// definitions of libraries and variables
// ===== PART 2: General Properties (ffv, subset_of, type_system) =====
Schema {
ffv: zero!(),
subset_of: None,
type_system: types.type_system(),
// ===== PART 3: Global States =====
global_types: tiny_bmap! {
GS_NOMINAL => GlobalStateSchema::once(types.get("RGBContract.DivisibleAssetSpec")),
GS_DATA => GlobalStateSchema::once(types.get("RGBContract.ContractData")),
GS_TIMESTAMP => GlobalStateSchema::once(types.get("RGBContract.Timestamp")),
GS_ISSUED_SUPPLY => GlobalStateSchema::once(types.get("RGBContract.Amount")),
},
// ===== PART 4: Owned Types =====
owned_types: tiny_bmap! {
OS_ASSET => StateSchema::Fungible(FungibleType::Unsigned64Bit),
},
// ===== PART 5: Valencies =====
valency_types: none!(),
// ===== PART 6: Genesis: Initial Operations =====
genesis: GenesisSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: tiny_bmap! {
GS_NOMINAL => Occurrences::Once,
GS_DATA => Occurrences::Once,
GS_TIMESTAMP => Occurrences::Once,
GS_ISSUED_SUPPLY => Occurrences::Once,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
},
// ===== PART 7: Extensions =====
extensions: none!(),
// ===== PART 8: Transitions: TS_TRANSFER =====
transitions: tiny_bmap! {
TS_TRANSFER => TransitionSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: none!(),
inputs: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
}
},
// ===== PART 9: Script AluVM and Entry Points =====
script: Script::AluVM(AluScript {
libs: confined_bmap! { alu_id => alu_lib },
entry_points: confined_bmap! {
EntryPoint::ValidateGenesis => LibSite::with(FN_GENESIS_OFFSET, alu_id),
EntryPoint::ValidateTransition(TS_TRANSFER) => LibSite::with(FN_TRANSFER_OFFSET, alu_id),
},
}),
}
}
```


- (1) - Funktsiooni päis ja SubSchema**

Funktsioon `nia_schema()` tagastab `SubSchema`, mis näitab, et see skeem võib osaliselt pärituda üldisemast skeemist. RGB ökosüsteemis võimaldab selline paindlikkus taaskasutada teatud standardseid põhiskeemi elemente ja seejärel määratleda konkreetse lepingu jaoks spetsiifilised reeglid. Siinkohal otsustame mitte lubada pärimist, kuna `subset_of` on `None`.


- (2) - Üldised omadused: ffv, subset_of, type_system**

Omadus `ffv` vastab lepingu *kiiresti edastatavale* versioonile. Väärtus `null!()` näitab, et me oleme selle skeemi versioonil 0 või algsel versioonil. Kui te soovite hiljem lisada uusi funktsioone (uut tüüpi operatsioone jne), saate seda versiooni suurendada, et näidata konsensuse muutmist.

`subset_of: None` omadus kinnitab pärimise puudumist. Väli `type_system` viitab range tüübisüsteemile, mis on juba määratletud raamatukogus `types`. See rida näitab, et kõik lepingus kasutatavad andmed kasutavad kõnealuse raamatukogu poolt pakutavat ranget serialiseerimise rakendamist.


- (3) - ülemaailmsed riigid

Plokis `global_types` deklareerime neli elementi. Hiljem kasutame neile viitamiseks võtit, näiteks `GS_NOMINAL` või `GS_ISSUED_SUPPLY`:


- `GS_NOMINAL` viitab tüübile `DivisibleAssetSpec`, mis kirjeldab loodud sümboli erinevaid välju (täisnimi, ticker, täpsus...);
- `GS_DATA` tähistab üldisi andmeid, näiteks vastutuse välistamist, metaandmeid või muud teksti;
- `GS_TIMESTAMP` viitab väljaandmise kuupäevale;
- `GS_ISSUED_SUPPLY` määrab koguvarustuse, st maksimaalse arvu märke, mida saab luua.

Võtmesõna `once(...)` tähendab, et iga selline väli võib esineda ainult üks kord.


- (4) - omandatud tüübid

Kirjas `owned_types` deklareerime `OS_ASSET`, mis kirjeldab asendatavat olekut. Kasutame `StateSchema::Fungible(FungibleType::Unsigned64Bit)`, mis näitab, et varade (žetoonide) kogus on salvestatud 64-bitise täisarvuna. Seega saadab iga tehing teatud koguse selle märgi ühikuid, mis valideeritakse selle rangelt tüpiseeritud numbrilise struktuuri järgi.


- (5) - Valencies**

Me märgime `valentsi_tüübid: none!()`, mis tähendab, et selles skeemis ei ole mingeid valentsusi, teisisõnu mingeid eri- või lisaõigusi (nagu korduvkasutamine, tingimuslik põletamine jne). Kui skeem sisaldaks neid, siis deklareeritaks need selles jaotises.


- (6) - Genesis: esimesed toimingud

Siin sisestame osa, mis deklareerib lepingu toiminguid. Genesis on kirjeldatud :


- Puuduvad "metaandmed" (väli "metaandmed: Ty::<SemId>::UNIT.id(None)`) ;
- Globaalsed riigid, mis peavad olema kohal üks kord (`Once`);
- Assignments'i nimekiri, kus `OS_ASSET` peab olema `OnceOrMore`. See tähendab, et Genesis vajab vähemalt ühte `OS_ASSET` Assignment'i (esialgset omanikku);
- No Valentsus : `valentsused: none!()`.

Nii piiritleme algse tokeni väljastamise definitsiooni: peame deklareerima väljastatud pakkumise (`GS_ISSUED_SUPPLY`), lisaks vähemalt ühe omaniku (Owned State tüüpi `OS_ASSET`).


- (7) - laiendused

Väli `extensions: none!()` näitab, et selles lepingus ei ole ette nähtud ühtegi riigi laiendust. See tähendab, et enne üleminekut ei ole ette nähtud ühtegi operatsiooni digitaalse õiguse (Valentsi) lunastamiseks või oleku laiendamise teostamiseks. Kõik toimub Genesis või State Transitions kaudu.


- (8) - Üleminekud: TS_TRANSFER

Üleminekutes defineerime operatsioonitüübi `TS_TRANSFER`. Me selgitame, et :


- Sellel puuduvad metaandmed;
- See ei muuda globaalset seisundit (mis on juba Genesis määratletud);
- See võtab sisendiks ühe või mitu `OS_ASSETi`. See tähendab, et see peab kulutama olemasolevaid Owned States;
- See loob (`assignments`) vähemalt ühe uue `OS_ASSET` (teisisõnu, vastuvõtja või vastuvõtjad saavad žetoonid) ;
- See ei tekita uut Valentsi.

See modelleerib põhisiirde käitumist, mis tarbib UTXO-l märke, loob seejärel uusi omandatud seisundeid saajate kasuks ja säilitab seega sisendite ja väljundite kogusumma võrdsuse.


- (9) - AluVM skript ja sisenemiskohad** (prantsuse keeles)

Lõpuks deklareerime AluVM skripti (`Script::AluVM(AluScript { ... })`). See skript sisaldab :


- Üks või mitu välist raamatukogu (`libs`), mida kasutatakse valideerimise ajal;
- Sisendpunktid, mis osutavad AluVM koodis olevatele funktsioonide offsettidele, mis vastavad Genesis'i (`ValidateGenesis`) ja iga deklareeritud ülemineku (`ValidateTransition(TS_TRANSFER)`) valideerimisele.

See valideerimiskood vastutab äriloogika rakendamise eest. Näiteks kontrollib see :


- Et `GS_ISSUED_SUPPLY` ei ületataks Genesis'i ajal ;
- Et "sisendite" (kulutatud žetoonide) summa on võrdne "eraldiste" (saadud žetoonide) summaga "TS_TRANSFERi" puhul.

Kui neid reegleid ei järgita, loetakse üleminek kehtetuks.

See näide "*Non Inflatable Fungible Asset*" skeemi kohta annab meile parema ülevaate lihtsa RGB fungible tokeni lepingu struktuurist. Me näeme selgelt andmete kirjelduse (globaalsed ja omandatud olekud), operatsioonide deklareerimise (Genesis, Transitions, Extensions) ja valideerimise rakendamise (AluVM skriptid) vahelist eraldatust. Tänu sellele mudelile käitub märgis nagu klassikaline fungible märgis, kuid jääb kliendi poolel valideerituks ja ei sõltu oma koodi täitmiseks ahelasisesest infrastruktuurist. Bitcoini plokiahelasse on ankurdatud ainult krüptograafilised kohustused.

### Kasutajaliides

Kasutajaliides on kiht, mille eesmärk on muuta leping loetavaks ja manipuleeritavaks nii kasutajate (inimlugemine) kui ka portfellide (tarkvaralugemine) poolt. Seega on liidese roll võrreldav objektorienteeritud programmeerimiskeele (Java, Rust trait jne) liidese rolliga, kuna see avalikustab ja selgitab lepingu funktsionaalset struktuuri, paljastamata tingimata äriloogika sisemisi üksikasju.

Erinevalt skeemist, mis on puhtalt deklaratiivne ja kompileeritud binaarfailiks, mida on raske kasutada sellisena, pakub Interface lugemisvõtmeid, mis on vajalikud :


- Loetlege ja kirjeldage lepinguga hõlmatud globaalseid ja omandiõiguslikke riike;
- Juurdepääs iga välja nimedele ja väärtustele, et neid saaks kuvada (nt tokeni puhul saada teada selle ticker, maksimaalne summa jne);
- Tõlgendada ja konstrueerida lepinguoperatsioone (Genesis, State Transition või State Extension), seostades andmeid arusaadavate nimedega (nt teha ülekanne, määrates selgelt "summa", mitte binaarset identifikaatorit).

![RGB-Bitcoin](assets/fr/073.webp)

Tänu liidesele saate näiteks rahakotis kirjutada koodi, mis väljadega manipuleerimise asemel manipuleerib otse selliseid silte nagu "žetoonide arv", "vara nimi" jne. Nii muutub lepingu haldamine intuitiivsemaks. Sel viisil muutub lepingu haldamine intuitiivsemaks.

#### Üldine tegevus

Sellel meetodil on palju eeliseid:


- Standardimine:**

Sama tüüpi lepingut võib toetada standardne liides, mida jagavad mitu rahakoti rakendust. See hõlbustab ühilduvust ja koodi taaskasutamist.


- Selge eraldatus skeemi ja liidese vahel:**

RGB kujunduses on skeem (äriloogika) ja kasutajaliides (esitus ja manipuleerimine) kaks sõltumatut üksust. Arendajad, kes kirjutavad lepinguloogikat, saavad keskenduda skeemile, muretsemata ergonoomika või andmete esituse pärast, samal ajal kui teine meeskond (või sama meeskond, kuid teisel ajagraafikul) võib arendada kasutajaliidest.


- Paindlik areng:**

Kasutajaliidest saab muuta või täiendada pärast vara väljaandmist, ilma et peaks muutma lepingut ennast. See on oluline erinevus võrreldes mõne ahelas oleva aruka lepingu süsteemiga, kus liides (sageli segatud täitmiskoodiga) on plokiahelas külmutatud.


- Multi-interface võimekus

Sama leping võib olla avatud erinevate liideste kaudu, mis on kohandatud erinevatele vajadustele: lihtne liides lõppkasutajale, teine keerukam liides emitendile, kes peab haldama keerulisi konfiguratsioonitoiminguid. Rahakott saab siis valida, millist liidest importida, sõltuvalt tema kasutusalast.

![RGB-Bitcoin](assets/fr/074.webp)

Praktikas, kui rahakott hangib RGB-lepingu (faili `.rgb` või `.rgba` kaudu), impordib ta ka sellega seotud liidese, mis samuti kompileeritakse. Käivitamise ajal võib rahakott näiteks :


- Sirvida riikide nimekirja ja lugeda nende nimesid, et kuvada kasutajaliideses loetamatu numbrilise identifikaatori asemel Ticker, esialgne summa, emissiooni kuupäev jne;
- Koostada operatsioon (näiteks ülekanne), kasutades selgesõnalisi parameetrite nimesid: selle asemel, et kirjutada `assignments { OS_ASSET => 1 }`, võib ta pakkuda kasutajale vormil välja "Amount" ja tõlkida selle teabe lepingu poolt oodatavateks rangelt trükitud väljadeks.

#### Erinevus Ethereumist ja teistest süsteemidest

Ethereumis on liides (mida kirjeldatakse ABI, *Application Binary Interface*, kaudu) üldiselt tuletatud ahelas salvestatud koodist (nutikas leping). Võib olla kulukas või keeruline muuta liidese konkreetset osa ilma lepingu enda puudutamata. RGB põhineb aga täielikult ahelavälisel loogikal, kusjuures andmed on ankurdatud *commitments* Bitcoinis. Selline ülesehitus võimaldab muuta liidest (või selle rakendamist) ilma lepingu põhilist turvalisust mõjutamata, kuna ärieeskirjade valideerimine jääb skeemi ja viidatud AluVM-i koodi.

#### Kasutajaliidese koostamine

Nagu skeemi puhul, on liides defineeritud lähtekoodis (sageli Rusti keeles) ja kompileeritud faili `.rgb` või `.rgba`. See binaarfail sisaldab kogu teavet, mida rahakott vajab :


- Väljade tuvastamine nime järgi ;
- Seostage iga väli (ja selle väärtus) lepingus määratletud range süsteemitüübiga;
- Teada erinevaid lubatud operatsioone ja nende ehitamist.

Kui liides on imporditud, saab rahakott lepingu korrektselt kuvada ja kasutajale interaktsioone pakkuda.

### LNP/BP assotsiatsiooni poolt standardiseeritud liidesed

RGB ökosüsteemis kasutatakse liideseid selleks, et anda lepingu andmetele ja toimingutele loetav ja manipuleeritav tähendus. Seega täiendab liides skeemi, mis kirjeldab sisemiselt äriloogikat (ranged tüübid, valideerimisskriptid jne). Selles jaotises vaatleme LNP/BP ühingu poolt välja töötatud standardseid liideseid tavapäraste lepingutüüpide (fungible tokenid, NFT jne) jaoks.

Meeldetuletuseks: idee on, et iga liides kirjeldab, kuidas lepingut rahakoti poolel kuvada ja sellega manipuleerida, nimetades selgelt väljad (näiteks `spec`, `ticker`, `issuedSupply`...) ja määratledes võimalikud operatsioonid (näiteks `Transfer`, `Burn`, `Rename`...). Mitmed liidesed on juba kasutusel, kuid tulevikus lisandub neid veelgi.

#### Mõned kasutusvalmis liidesed

**RGB20** on vahetatavate varade liides, mida võib võrrelda Ethereumi ERC20 standardiga. Siiski läheb see sammu võrra kaugemale, pakkudes ulatuslikumat funktsionaalsust:


- Näiteks võimalus nimetada vara ümber (*tickeri* või täisnime muutmine) pärast selle väljastamist või kohandada selle täpsust (*varude jagamine*);
- Samuti võib selles kirjeldada mehhanismid teisese taasväljaandmise (piiratud või piiramatu) ja põletamise ning seejärel asendamise jaoks, et anda emitendile luba hävitada ja seejärel teatud tingimustel taasluua varasid;

Näiteks saab RGB20 liidest ühendada **Non-Inflatable Asset (NIA) skeemiga**, mis kehtestab mitteinflatsioonilise algvarustuse, või vastavalt vajadusele muude, keerukamate skeemidega.

**RGB21** puudutab NFT-tüüpi lepinguid või laiemalt mis tahes ainulaadset digitaalset sisu, näiteks digitaalse meedia (pildid, muusika jne) esitamist. Lisaks ühe vara väljaandmise ja üleandmise kirjeldamisele sisaldab see selliseid funktsioone nagu :


- Integreeritud tugi faili (kuni 16 MB) otseseks lisamiseks lepingusse (kliendipoolseks päringuks);
- Omaniku võimalus sisestada "*graveering*" ajalukku, et tõestada NFT varasemat omamist.

**RGB25** on hübriidstandard, mis ühendab asendatavad ja mittekõrvaldatavad aspektid. See on mõeldud osaliselt asendatavate varade jaoks, näiteks kinnisvara tokeniseerimiseks, kus soovite jagada kinnisvara, säilitades samal ajal lingi ühe juurvaraga (teisisõnu, teil on asendatavad majatükid, mis on seotud mitte-kungifitseeritava majaga). Tehniliselt saab selle liidese siduda **Collectible Fungible Asset* (CFA)** skeemiga, mis võtab arvesse jagamise mõistet, jälgides samal ajal algset vara.

#### Arendamisel olevad liideseid

Muud liidesed on kavandatud spetsiifilisemateks kasutusaladeks, kuid need ei ole veel saadaval:


- RGB22**, mis on pühendatud digitaalsetele identiteetidele, et hallata identifikaatoreid ja ahelas olevaid profiile RGB ökosüsteemis;
- RGB23**, täiustatud ajatemplite jaoks, mis kasutab mõningaid *Opentimestamps* ideid, kuid millel on jälgitavuse funktsioonid;
- RGB24**, mille eesmärk on detsentraliseeritud domeeninimede süsteemi (DNS) sarnane *Ethereum Name Service* ;
- RGB26**, mis on mõeldud DAOde (*Decentralized Autonomous Organization*) haldamiseks keerulisemas vormis (juhtimine, hääletamine jne);
- RGB30**, mis on väga sarnane RGB20-le, kuid mille eripära on detsentraliseeritud algse emiteerimise arvessevõtmine ja riigi laienduste kasutamine. Seda kasutataks varade puhul, mille taasväljaandmist haldavad mitu üksust või mille suhtes kehtivad täpsemad tingimused.

Loomulikult võivad need liidesed sõltuvalt kuupäevast, mil te selle kursusega konsulteerite, juba toimida ja olla kättesaadavad.

#### Näide liidese kohta

See Rusti koodilõik näitab [RGB20](https://github.com/RGB-WG/rgb-std/blob/master/src/interface/rgb20.rs) liidest (asendatav vara). See kood on võetud standardse RGB raamatukogu failist `rgb20.rs`. Vaatame seda, et mõista Interface'i struktuuri ja seda, kuidas see loob silla ühelt poolt äriloogika (defineeritud Schema's) ja teiselt poolt rahakottidele ja kasutajatele avatud funktsionaalsuse vahel.

```rust
// ...
fn rgb20() -> Iface {
let types = StandardTypes::with(rgb20_stl());
Iface {
version: VerNo::V1,
name: tn!("RGB20"),
global_state: tiny_bmap! {
fname!("spec") => GlobalIface::required(types.get("RGBContract.DivisibleAssetSpec")),
fname!("data") => GlobalIface::required(types.get("RGBContract.ContractData")),
fname!("created") => GlobalIface::required(types.get("RGBContract.Timestamp")),
fname!("issuedSupply") => GlobalIface::one_or_many(types.get("RGBContract.Amount")),
fname!("burnedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
fname!("replacedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
},
assignments: tiny_bmap! {
fname!("inflationAllowance") => AssignIface::public(OwnedIface::Amount, Req::NoneOrMore),
fname!("updateRight") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnEpoch") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnRight") => AssignIface::public(OwnedIface::Rights, Req::NoneOrMore),
fname!("assetOwner") => AssignIface::private(OwnedIface::Amount, Req::NoneOrMore),
},
valencies: none!(),
genesis: GenesisIface {
metadata: Some(types.get("RGBContract.IssueMeta")),
global: tiny_bmap! {
fname!("spec") => ArgSpec::required(),
fname!("data") => ArgSpec::required(),
fname!("created") => ArgSpec::required(),
fname!("issuedSupply") => ArgSpec::required(),
},
assignments: tiny_bmap! {
fname!("assetOwner") => ArgSpec::many(),
fname!("inflationAllowance") => ArgSpec::many(),
fname!("updateRight") => ArgSpec::optional(),
fname!("burnEpoch") => ArgSpec::optional(),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_RESERVES
},
},
transitions: tiny_bmap! {
tn!("Transfer") => TransitionIface {
optional: false,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("previous") => ArgSpec::from_non_empty("assetOwner"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_non_empty("assetOwner"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Issue") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.IssueMeta")),
globals: tiny_bmap! {
fname!("issuedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_non_empty("inflationAllowance"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_many("inflationAllowance"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
ISSUE_EXCEEDS_ALLOWANCE,
INSUFFICIENT_RESERVES
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("OpenEpoch") => TransitionIface {
optional: true,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnEpoch"),
},
assignments: tiny_bmap! {
fname!("next") => ArgSpec::from_optional("burnEpoch"),
fname!("burnRight") => ArgSpec::required()
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("burnRight")),
},
tn!("Burn") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("burnedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: None,
},
tn!("Replace") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("replacedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS,
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Rename") => TransitionIface {
optional: true,
metadata: None,
globals: tiny_bmap! {
fname!("new") => ArgSpec::from_required("spec"),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("updateRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("updateRight"),
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("future")),
},
},
extensions: none!(),
error_type: types.get("RGB20.Error"),
default_operation: Some(tn!("Transfer")),
type_system: types.type_system(),
}
}
```

Selles liideses märkame sarnasusi skeemi struktuuriga: leiame globaalse oleku, omandatud olekute, lepinguoperatsioonide (Genesis ja Transitions) ning veakäitluse deklaratsiooni. Kuid liides keskendub nende elementide esitamisele ja manipuleerimisele rahakoti või muu rakenduse jaoks.

Erinevus skeemiga seisneb tüüpide olemuses. Schema kasutab rangeid tüüpe (näiteks `FungibleType::Unsigned64Bit`) ja tehnilisemaid identifikaatoreid. Interface kasutab väljade nimesid, makrosid (`fname!()`, `tn!()`) ja viiteid argumentide klassidele (`ArgSpec`, `OwnedIface::Rights`...). Eesmärk on hõlbustada rahakoti jaoks elementide funktsionaalset mõistmist ja organiseerimist.

Lisaks võib liides lisada põhiskeemile lisafunktsioone (nt õiguse `burnEpoch` haldamine), kui see on kooskõlas lõpliku valideeritud kliendipoolse loogikaga. AluVMi "skripti" osa skeemis tagab krüptograafilise kehtivuse, samas kui liides kirjeldab, kuidas kasutaja (või rahakott) nende seisundite ja üleminekutega suhtleb.

#### Ülemaailmne seisund ja ülesanded

Jaotises `global_state` leiame sellised väljad nagu `spec` (vara kirjeldus), `data`, `created`, `issuedSupply`, `burnedSupply`, `replacedSupply`. Need on väljad, mida rahakott saab lugeda ja esitada. Näiteks:


- `spec` kuvab sümboli konfiguratsiooni;
- `issuedSupply` või `burnedSupply` annavad meile väljastatud või põletatud žetoonide koguarvu jne.

Jaotises "Assignments" määratleme erinevaid rolle või õigusi. Näiteks:


- `Varaomanik` vastab žetoonide valdusele (see on asendatav *Omaned State*) ;
- `burnRight` vastab võimele põletada žetoone ;
- updateRight` vastab õigusele nimetada vara ümber.

Võtmesõna `public` või `private` (nt `AssignIface::public(...)`) näitab, kas need olekud on nähtavad (`public`) või konfidentsiaalsed (`private`). Nagu `Req::NoneOrMore`, `Req::Optional`, need näitavad eeldatavat esinemist.

#### Genesis ja üleminekud

"Genesis" osa kirjeldab, kuidas vara initsialiseeritakse:


- Väljad `spec`, `data`, `created`, `issuedSupply` on kohustuslikud (`ArgSpec::required()`) ;
- Sellised määrangud nagu `assetOwner` võivad esineda mitmes eksemplaris (`ArgSpec::many()`), võimaldades žetoonide jagamist mitmele algsele omanikule;
- Sellised väljad nagu `inflationAllowance` või `burnEpoch` võivad (või ei pruugi) Genesis sisalduda.

Seejärel määratleb liides iga ülemineku (`Transfer`, `Issue`, `Burn`...) jaoks, milliseid välju operatsioon ootab sisendina, milliseid välju operatsioon väljundina toodab ja milliseid vigu võib esineda. Näiteks:

**Transition :**


- Sisendid : `previous` → peab olema `assetOwner` ;
- Ülesanded : "soodustatud isik" → saab uue "varaomaniku";
- Viga: `NON_EQUAL_AMOUNTS` (rahakott suudab seega käsitleda juhtumeid, kus sisendsumma ei vasta väljundsummale).

**Transition `Issue` :**


- Vabatahtlik (`optional: true`), kuna lisaväljaanne ei ole tingimata aktiveeritud;
- Sisendid: s.t. luba lisada rohkem märke ;
- Ülesanded: "soodustatud" (uued saadud žetoonid) ja "tulevik" (allesjäänud "inflatsioonitoetus") ;
- Võimalikud vead: `SUPPLY_MISMATCH`, `ISSUE_EXCEEDS_ALLOWANCE` jne.

**Burn transition :**


- Sisendid : "kasutatud" → a "burnRight" ;
- Globaalid : `burnedSupply` nõutav ;
- Ülesanded: `future` → võimalik jätk `burnRight`, kui me ei ole kõike põletanud ;
- Vead: `SUPPLY_MISMATCH`, `INVALID_PROOF`, `INSUFFICIENT_COVERAGE`.

Iga toiming on seega kirjeldatud rahakoti jaoks loetavalt. See võimaldab kuvada graafilise kasutajaliidese, kus kasutaja saab selgelt näha: "Teil on õigus põletada. Kas soovite põletada teatud summa? Kood teab, et täita väli `burnedSupply` ja kontrollida, et `burnRight` on kehtiv.

Kokkuvõttes on oluline meeles pidada, et liides, olgu see kui tahes täielik, ei määratle iseenesest lepingu sisemist loogikat. Põhitöö teeb ära **Skeem**, mis sisaldab rangeid tüüpe, Genesis'i struktuuri, üleminekuid ja nii edasi. Kasutajaliides lihtsalt eksponeerib need elemendid intuitiivsemal ja nimetatumal viisil, et neid saaks rakenduses kasutada.

Tänu RGB modulaarsusele saab kasutajaliidest täiustada (näiteks lisades ülemineku "Rename", parandades mõne välja kuvamist jne), ilma et peaks kogu lepingut ümber kirjutama. Selle liidese kasutajad saavad neist parandustest kohe kasu, kui nad uuendavad faili `.rgb` või `.rgba`.

Kui olete aga liidesed deklareerinud, peate selle siduma vastava skeemiga. Seda tehakse ***Interface Implementation*** kaudu, mis määrab kindlaks, kuidas kaardistada iga nimeline väli (näiteks `fname!("assetOwner")`) skeemis määratletud rangele ID-le (näiteks `OS_ASSET`). See tagab näiteks, et kui rahakott manipuleerib välja `burnRight`, siis on see olek, mis skeemis kirjeldab võimet põletada žetooni.

### Kasutajaliidese rakendamine

RGB-arhitektuuris nägime, et iga komponenti (skeem, liides jne) saab arendada ja koostada sõltumatult. Siiski on veel üks hädavajalik element, mis ühendab neid erinevaid ehitusplokke omavahel: ***Interface Implementation***. See on see, mis selgesõnaliselt kaardistab skeemis (äriloogika poolel) määratletud identifikaatorid või väljad liideses (esitusviisi ja kasutaja interaktsiooni poolel) deklareeritud nimedega. Nii saab rahakott lepingu laadimisel täpselt aru, milline väli millele vastab ja kuidas liideses nimetatud operatsioon on seotud skeemi loogikaga.

Oluline punkt on see, et liidese rakendamine ei ole tingimata mõeldud kõigi skeemi funktsioonide ega kõigi liidese väljade avalikustamiseks: see võib piirduda teatud alamhulgaga. Praktikas võimaldab see skeemi teatud aspekte piirata või filtreerida. Näiteks võib teil olla skeem, millel on neli operatsioonitüüpi, kuid rakendusliides, mis kaardistab ainult kaks neist antud kontekstis. Vastupidi, kui liides pakub välja täiendavaid lõpp-punkte, võime otsustada neid siin mitte rakendada.

Siin on klassikaline näide liidese rakendamise kohta, kus me seostame *Non-Inflatable Asset* (NIA) skeemi RGB20 liidesega:

```rust
fn nia_rgb20() -> IfaceImpl {
let schema = nia_schema();
let iface = Rgb20::iface();
IfaceImpl {
version: VerNo::V1,
schema_id: schema.schema_id(),
iface_id: iface.iface_id(),
script: none!(),
global_state: tiny_bset! {
NamedField::with(GS_NOMINAL, fname!("spec")),
NamedField::with(GS_DATA, fname!("data")),
NamedField::with(GS_TIMESTAMP, fname!("created")),
NamedField::with(GS_ISSUED_SUPPLY, fname!("issuedSupply")),
},
assignments: tiny_bset! {
NamedField::with(OS_ASSET, fname!("assetOwner")),
},
valencies: none!(),
transitions: tiny_bset! {
NamedType::with(TS_TRANSFER, tn!("Transfer")),
},
extensions: none!(),
}
}
```

Selles rakendusliideses :


- Me viitame selgesõnaliselt skeemile, kasutades `nia_schema()`, ja liidesele, kasutades `Rgb20::iface()`. Kõnesid `schema.schema_id()` ja `iface.iface_id()` kasutatakse liidese rakendamise kinnistamiseks kompileerimise poolel (see seostab nende kahe komponendi krüptograafilised identifikaatorid);
- Skeemielementide ja liidese elementide vahel luuakse vastavus. Näiteks on skeemi väli `GS_NOMINAL` seotud liidese poolel oleva stringiga `"spec"` (`NamedField::with(GS_NOMINAL, fname!("spec"))`). Sama teeme operatsioonide puhul, näiteks `TS_TRANSFER`, mida me seome liideses `"Transfer"`ga... ;
- Me näeme, et puuduvad valentsused (`valencies: none!()`) ja laiendused (`extensions: none!()`), mis peegeldab asjaolu, et see NIA leping ei kasuta neid funktsioone.

Pärast kompileerimist on tulemuseks eraldi `.rgb` või `.rgba` fail, mis tuleb lisaks skeemile ja liidesele importida rahakotti. Seega teab tarkvara, kuidas konkreetselt ühendada see NIA leping (mille loogikat kirjeldab selle skeem) "RGB20" liidesega (mis pakub inimnimesid ja interaktsioonirežiimi asendatavate žetoonide jaoks), rakendades seda liidese rakendust kui väravat nende kahe vahel.

#### Miks eraldi liidese rakendamine?

Eraldamine suurendab paindlikkust. Ühel skeemil võib olla mitu erinevat liidese rakendust, millest igaüks kujutab endast erinevat funktsionaalsuste kogumit. Veelgi enam, liidese rakendamine ise võib areneda või ümber kirjutada, ilma et oleks vaja muuta skeemi või liideseid. See säilitab RGB modulaarsuse põhimõtte: iga komponenti (skeem, liides, liidese rakendamine) saab iseseisvalt versioonida ja uuendada, kui järgitakse protokolliga kehtestatud ühilduvuseeskirju (samad identifikaatorid, tüüpide järjepidevus jne).

Konkreetses kasutuses, kui rahakott laadib lepingu, peab :


- Laadige kompileeritud **skeem** (et teada äriloogika struktuuri) ;
- Laadige kompileeritud **Liides** (nimede ja kasutajapoolsete operatsioonide mõistmiseks) ;
- Laadige kompileeritud **Liidese rakendamine** (et siduda skeemiloogika liidese nimedega, operatsioonide ja väljade kaupa).

Selline modulaarne arhitektuur võimaldab kasutada selliseid stsenaariume nagu :


- Piirata teatud toiminguid teatud kasutajatele: pakkuda osalist rakendusliidest, mis annab juurdepääsu ainult põhilistele ülekannetele, ilma et pakutaks näiteks põletamis- või uuendamisfunktsioone;
- Muudatuste esitamine: kavandage liidese rakendamine, mis nimetab liidese välja ümber või kaardistab selle teisiti, muutmata seejuures lepingu alust;
- Mitme skeemi toetamine: rahakott võib laadida mitu sama liidesetüübi liidese rakendust, et käsitleda erinevaid skeeme (erinevaid sümbolite loogikaid), tingimusel, et nende struktuur on ühilduv.

Järgmises peatükis vaatleme, kuidas lepingu ülekandmine toimib ja kuidas RGB-arveid koostatakse.

## Lepingu üleandmine

<chapterId>f043a307-d420-5752-b0d7-ebfd845802c0</chapterId>

![video](https://youtu.be/sVoKIi-1XbY)

Selles peatükis analüüsime lepingu üleandmise protsessi RGB ökosüsteemis. Selle illustreerimiseks vaatleme Alice'i ja Bobi, meie tavalisi peategelasi, kes soovivad vahetada RGB vara. Näitame ka mõned käsu väljavõtted käsurea tööriistast `rgb`, et näha, kuidas see praktikas töötab.

### RGB lepingu ülekandmise mõistmine

Võtame näite Alice'i ja Bobi vahelise ülekande kohta. Selles näites eeldame, et Bob alles alustab RGB kasutamist, samas kui Alice'il on juba RGB varasid oma rahakotis. Näeme, kuidas Bob loob oma keskkonna, impordib asjakohase lepingu, seejärel taotleb Alice'ilt ülekannet ja lõpuks, kuidas Alice teostab tegeliku tehingu Bitcoini plokiahelas.

#### 1) RGB rahakoti paigaldamine

Kõigepealt peab Bob paigaldama RGB rahakoti, st protokolliga ühilduva tarkvara. See ei sisalda alguses ühtegi lepingut. Bob vajab ka :


- Bitcoini rahakott oma UTXOde haldamiseks;
- Ühendus Bitcoini sõlme (või Electrumi serveriga), et saaksite tuvastada oma UTXO-d ja levitada oma tehinguid võrgus.

Meeldetuletuseks: **Omaned States** viitavad RGB-s Bitcoini UTXOdele. Seetõttu peame alati suutma hallata ja kulutada UTXOsid Bitcoini tehingus, mis sisaldab RGB-andmetele viitavaid krüptograafilisi kohustusi (`Tapret` või `Opret`).

#### 2) Lepinguga seotud teabe hankimine

Seejärel peab Bob välja otsima lepingu andmed, millest ta on huvitatud. Need andmed võivad liikuda mis tahes kanali kaudu: veebisait, e-post, sõnumirakendus... Praktikas on need koondatud ***saadetistesse***, st väikesesse andmepaketti, mis sisaldab :


- **Genesis**, mis määratleb lepingu algse seisundi;
- **Skeem**, mis kirjeldab äriloogikat (ranged tüübid, valideerimisskriptid jne);
- **Liides**, mis määratleb esitluskihi (väljade nimed, juurdepääsetavad operatsioonid);
- **Liidese rakendamine**, mis seob konkreetselt skeemi ja liidese.

![RGB-Bitcoin](assets/fr/075.webp)

Kogumaht on sageli mõne kilobaidi suurune, kuna iga komponent kaalub tavaliselt vähem kui 200 baiti. Seda saadetist võib olla võimalik edastada ka Base58-s, tsensuurikindlate kanalite kaudu (näiteks Nostr või Lightning Network'i kaudu) või QR-koodina.

#### 3) Lepingu import ja valideerimine

Kui Bob on saadetise kätte saanud, sisestab ta selle oma RGB rahakotti. Seejärel :


- Kontrollige, et Genesis ja Schema on kehtivad;
- Laadimisliides ja liidese rakendamine ;
- Uuendage oma kliendipoolset andmekogu.

Bob saab nüüd näha vara oma rahakotis (isegi kui ta seda veel ei oma) ja saab aru, millised väljad on saadaval, millised operatsioonid on võimalikud... Seejärel peab ta võtma ühendust isikuga, kes tegelikult omab ülekantavat vara. Meie näites on see Alice.

Teatud RGB-vara omaniku leidmise protsess on sarnane Bitcoini maksja leidmisega. Selle ühenduse üksikasjad sõltuvad kasutusest (turuplatsid, privaatsed vestluskanalid, arvete esitamine, kaupade ja teenuste müük, palk...).

#### 4) Arve väljastamine

RGB vara ülekandmise algatamiseks peab Bob kõigepealt väljastama arve. Seda arvet kasutatakse selleks, et :


- Ütle Alice'ile, millist tüüpi operatsiooni soovitakse teha (näiteks `Transfer` RGB20 liidesest);
- Andke Alice'ile Bobi *sulge määratlus* (st UTXO, kus ta soovib vara vastu võtta);
- Märkige nõutav toimeaine kogus (nt 100 ühikut).

Bob kasutab käsurea tööriista `rgb`. Oletame, et ta tahab 100 ühikut tokenit, mille `ContractId` on teada, tahab tugineda `Tapret`ile ja määrab selle UTXO (`456e3..dfe1:0`) :

```bash
bob$ rgb invoice RGB20 100 <ContractId> tapret1st:456e3..dfe1:0
```

RGB-arvete struktuuri vaatleme lähemalt selle peatüki lõpus.

#### 5) Arve edastamine

Genereeritud arve (nt URLina: `rgb:2WBcas9.../RGB20/100+utxob:...`) sisaldab kogu teavet, mida Alice vajab ülekande ettevalmistamiseks. Nagu saadetise puhul, saab seda kompaktselt kodeerida (Base58 või muus formaadis) ja saata sõnumirakenduse, e-posti, Nostr...

![RGB-Bitcoin](assets/fr/076.webp)

#### 6) Tehingu ettevalmistamine Alice'i poolel

Alice saab Bobi arve. Tema RGB rahakotis on peidetud varu, mis sisaldab ülekantavat vara. Selleks, et kulutada vara sisaldavat UTXO-d, peab ta kõigepealt looma PSBT (*Partially Signed Bitcoin Transaction*), st mittetäieliku Bitcoin-tehingu, kasutades oma UTXO-d:

```bash
alice$ wallet construct tx.psbt
```

Seda (hetkel allkirjastamata) põhitehingut kasutatakse Bobile tehtava ülekandega seotud krüptograafilise kohustuse kinnitamiseks. Alice'i UTXO kulutatakse seega ära ja väljundis paigutame Bobi jaoks `Tapret` või `Opret` kohustuse.

#### 7) Ülekandesaadetise koostamine

Seejärel koostab Alice käsuga ***terminal consignment*** (mida mõnikord nimetatakse ka "transfer consignment"):

```bash
alice$ rgb transfer tx.psbt <invoice> consignment.rgb
```

See uus fail `consignment.rgb` sisaldab :


- Varade valideerimiseks vajalike riigisiirete täielik ajalugu kuni praeguseni (alates Genesisest);
- Uus riigi üleminek, mis kannab varad Alice'ilt Bobile üle vastavalt Bobi poolt väljastatud arvele;
- Mittetäielik Bitcoini tehing (*tunnistustehing*) (`tx.psbt`), mis kulutab Alice'i ühekordselt kasutatava pitseri, mida on muudetud, et lisada krüptograafiline kohustus Bobile.

Selles etapis ei ole tehing veel Bitcoini võrgus edastatud. Saadetis on suurem kui põhisaadetis, kuna see sisaldab kogu ajalugu (*tõendamisahel*), et tõestada vara legitiimsust.

#### 8) Bob kontrollib ja võtab saadetise vastu

Alice edastab selle **terminaalse saadetise** Bobile. Bob seejärel :


- Kontrollida riigi ülemineku kehtivust (tagada, et ajalugu on järjepidev, et lepingu reegleid järgitakse jne);
- Lisage see oma kohalikku varandusse;
- Võimalik luua saadetisele allkiri (`sig:...`), et tõestada, et see on kontrollitud ja heaks kiidetud (mõnikord nimetatakse seda ka "*maksekviitungiks*").

```bash
bob$ rgb accept consignment.rgb
sig:DbwzvSu4BZU81jEpE9FVZ3xjcyuTKWWy2gmdnaxtACrS
```

![RGB-Bitcoin](assets/fr/077.webp)

#### 9) Võimalus: Bob saadab kinnituse tagasi Alice'ile (*maksekviitung*)

Kui Bob soovib, võib ta selle allkirja Alice'ile tagasi saata. See näitab:


- Et see tunnistab ülemineku kehtivaks;
- Et ta nõustub Bitcoini tehingu edastamisega.

See ei ole kohustuslik, kuid see võib anda Alice'ile kindluse, et hiljem ei teki vaidlusi üleandmise üle.

#### 10) Alice allkirjastab ja avaldab tehingu

Alice saab siis :


- Kontrollib Bobi allkirja (`rgb check <sig>`) ;
- Allkirjastage *tunnistustehing*, mis on ikkagi PSBT (`wallet sign`) ;
- Avalda tunnistaja tehing Bitcoini võrgus (`-publish`).

```bash
alice$ rgb check <sig>
alice$ wallet sign —publish tx.psbt
```

![RGB-Bitcoin](assets/fr/078.webp)

Pärast kinnitamist tähistab see tehing ülekande lõpetamist. Bobist saab vara uus omanik: tal on nüüd omandatud riik, mis osutab tema kontrolli all olevale UTXO-le, mida tõestab kohustuse olemasolu tehingus.

Kokkuvõttes on siin täielik ülekandeprotsess:

![RGB-Bitcoin](assets/fr/079.webp)

### RGB-ülekannete eelised


- Konfidentsiaalsus** :

Ainult Alice'il ja Bobil on juurdepääs kõikidele oleku üleminekuandmetele. Nad vahetavad seda teavet väljaspool plokiahelat, saadetiste kaudu. Bitcoini tehingu krüptograafilised kohustused ei avalda vara liiki ega summat, mis tagab palju suurema konfidentsiaalsuse kui teised ahelasisesed sümboolsed süsteemid.


- Kliendipoolne valideerimine** :

Bob saab kontrollida ülekande järjepidevust, võrreldes *saatekirja* Bitcoini plokiahela *ankritega*. Ta ei vaja kolmanda osapoole kinnitust. Alice ei pea kogu ajalugu plokiahelas avaldama, mis vähendab alusprotokolli koormust ja parandab konfidentsiaalsust.


- Lihtsustatud aatomisus** :

Keerulisi vahetusi (näiteks BTC ja RGB vara vahelised aatomivahetuslepingud) saab teostada ühe tehinguga, vältides vajadust HTLC või PTLC skriptide järele. Kui kokkulepet ei edastata, saab igaüks oma UTXOsid muul viisil uuesti kasutada.

### Ülekande kokkuvõtlik diagramm

Enne arvete üksikasjalikumat vaatamist on siin kokkuvõtlik skeem RGB-ülekande üldisest kulgemisest:


- Bob paigaldab RGB rahakoti ja saab esialgse lepingulise saadetise;
- Bob väljastab arve, kus on märgitud UTXO, kus vara vastu võtta;
- Alice saab arve, koostab PSBT ja genereerib lõppsaadetise;
- Bob võtab selle vastu, kontrollib, lisab andmed oma varakambrisse ja allkirjastab (*maksekviitung*), kui see on vajalik;
- Alice avaldab tehingu Bitcoini võrgus;
- Tehingu kinnitamine muudab ülekande ametlikuks.

![RGB-Bitcoin](assets/fr/080.webp)

Ülekanne illustreerib RGB-protokolli kogu võimsust ja paindlikkust: privaatne vahetus, mis on kliendi poolel valideeritud, minimaalselt ja diskreetselt ankurdatud Bitcoini plokiahelas ning säilitab protokolli parima turvalisuse (puudub topeltkulutamise oht). See teeb RGB-st paljulubava ökosüsteemi väärtuse ülekandmiseks, mis on konfidentsiaalsem ja skaleeritavam kui ahelas programmeeritavad plokiahelad.

### Arved RGB

Selles jaotises selgitame üksikasjalikult, kuidas **arveid** RGB ökosüsteemis kasutatakse ja kuidas need võimaldavad lepinguga tehtavaid toiminguid (eelkõige ülekandeid) teha. Kõigepealt vaatleme kasutatavaid identifikaatoreid, seejärel seda, kuidas need on kodeeritud, ja lõpuks arve struktuuri, mis on väljendatud URL-aadressina (vorming, mis on piisavalt mugav rahakottides kasutamiseks).

#### Tunnused ja kodeerimine

Iga järgmise elemendi jaoks on määratletud kordumatu identifikaator:


- RGB leping;
- Selle skeem (äriloogika) ;
- Selle kasutajaliides ja kasutajaliidese rakendamine ;
- Selle varad (žetoonid, NFT jne),

See ainulaadsus on väga oluline, sest süsteemi iga komponent peab olema eristatav. Näiteks ei tohi lepingut X segi ajada teise lepinguga Y ja kahel erineval liidesel (näiteks RGB20 vs. RGB21) peavad olema erinevad identifikaatorid.

Et need identifikaatorid oleksid nii tõhusad (väike suurus) kui ka loetavad, kasutame :


- Base58 kodeering, mis väldib segadusttekitavate märkide (nt "0" ja täht "O") kasutamist ja tagab suhteliselt lühikeste stringide kasutamise;
- Identifikaatori olemust näitav eesliide, tavaliselt kujul `rgb:` või sarnane URN.

Näiteks `ContractId` võiks olla esindatud näiteks :

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

Eesliide `rgb:` kinnitab, et tegemist on RGB identifikaatoriga, mitte HTTP-linki või muu protokolliga. Tänu sellele prefiksile suudavad rahakotid seda stringi õigesti tõlgendada.

#### Identifikaatori segmenteerimine

RGB-tunnused on sageli üsna pikad, kuna nende aluseks olev (krüptograafiline) turvalisus võib nõuda 256-bitiseid või pikemaid välju. Inimese lugemise ja kontrollimise hõlbustamiseks *lõikame* need stringid mitmeks plokiks, mis on eraldatud sidekriipsuga (`-`). Seega jagame pika katkematu tähemärkide jada asemel selle lühemateks plokkideks. See tava on tavaline krediitkaardi või telefoninumbri puhul ja seda kohaldatakse ka siin kontrollimise lihtsustamiseks. Nii võib näiteks kasutajale või partnerile öelda: "*Palun kontrollige, et kolmas plokk on `9GEgnyMj7`*", selle asemel, et võrrelda kogu asja korraga. Viimast plokki kasutatakse sageli **kontrollsummana**, et oleks olemas vigade või kirjavigade tuvastamise süsteem.

Näiteks võib `ContractId` base58 kodeeritud ja segmenteeritud kujul olla :

```txt
2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

Iga kriips katkestab stringi osadeks. See ei mõjuta koodi semantikat, vaid ainult selle esitusviisi.

#### Arvete URL-i kasutamine

RGB-arve esitatakse URL-na. See tähendab, et seda saab klõpsata või skaneerida (QR-koodina) ja rahakott saab seda otse tõlgendada, et teostada tehing. Selline suhtlemise lihtsus erineb mõnest muust süsteemist, kus tuleb kopeerida ja kleepida erinevaid andmeid tarkvara erinevatesse väljadesse.

Faktuurarve asendatava märgi (nt RGB20 märgi) kohta võib välja näha järgmiselt:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Analüüsime seda URL-i:


- `rgb:`** (eesliide): tähistab linki, mis kasutab RGB-protokolli (analoogne `http:` või `bitcoin:` teistes kontekstides);
- `2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX`**: tähistab selle sümboli `ContractId`, millega soovite manipuleerida;
- `/RGB20/100`**: näitab, et kasutatakse liidest `RGB20` ja et taotletakse 100 ühikut vara. Süntaks on järgmine: `/Interface/amount` ;
- `+utxob:`**: määrab, et lisatakse teave vastuvõtva UTXO kohta (või täpsemalt, ühekordse pitseri määratlus);
- `egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb`**: see on *pimendatud* UTXO (või pitseri määratlus). Teisisõnu, Bob on maskeerinud oma täpse UTXO, nii et saatja (Alice) ei tea, milline on täpne aadress. Ta teab ainult, et on olemas kehtiv pitser, mis viitab Bobi kontrollitavale UTXO-le.

Asjaolu, et kõik mahub ühte URL-i, teeb kasutaja elu lihtsamaks: lihtne klõps või skaneerimine rahakotis ja operatsioon on valmis.

Võib ette kujutada süsteeme, kus lepingu identifikaatori asemel kasutatakse lihtsat märgusõna (nt "USDT"). See tekitaks aga suuri usaldus- ja julgeolekuprobleeme: märgusõna ei ole unikaalne viide (mitu lepingut võib väita, et nende nimi on `USDT`). RGB puhul tahame unikaalset, üheselt mõistetavat krüptograafilist identifikaatorit. Seepärast ongi võetud kasutusele 256-bitine string, mis on kodeeritud baas58-s ja segmenteeritud. Kasutaja teab, et ta manipuleerib täpselt lepingut, mille ID on `2WBcas9-yjz...` ja mitte mõnda teist.

#### Täiendavad URL-parameetrid

URL-ile saab lisada ka lisaparameetrid, nagu HTTP puhul, näiteks :

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb?sig=6kzbKKffP6xftkxn9UP8gWqiC41W16wYKE5CYaVhmEve
```


- `?sig=...`: tähistab näiteks arvega seotud allkirja, mida mõned rahakotid saavad kontrollida;
- Kui rahakott seda allkirja ei halda, ignoreerib ta seda parameetrit lihtsalt.

Võtame NFT juhtumi RGB21-liidese kaudu. Näiteks võiks meil olla :

```txt
rgb:7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK/RGB21/DbwzvSu-4BZU81jEp-E9FVZ3xj-cyuTKWWy-2gmdnaxt-ACrS+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Siin näeme :


- `rgb:`**: URL prefiks ;
- `7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK`**: Lepingu ID (NFT) ;
- rGB21**: liides mittekantavate varade jaoks (NFT) ;
- `DbwzvSu-4BZU81jEp-...`**: selgesõnaline viide NFT unikaalsele osale, näiteks andmeploki (meedia, metaandmed...) hash;
- `+utxob:egXsFnw-...`**: pitseri määratlus.

Idee on sama: edastada unikaalne link, mida rahakott suudab tõlgendada ja mis selgelt identifitseerib ülekantava vara.

#### Muud toimingud URL-i kaudu

RGB-URL-i ei kasutata ainult ülekande taotlemiseks. Nad võivad kodeerida ka keerulisemaid toiminguid, näiteks uute märkide väljastamist (*issuance*). Näiteks:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/issue/100000+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Siit leiame :


- `rgb:` : protokoll ;
- `2WBcas9-...`: Lepingu ID ;
- `/RGB20/issue/100000`: näitab, et soovite kasutada üleminekut "*Issue*", et luua veel 100 000 märgi;
- `+utxob:`: pitseri määratlus.

Näiteks võib rahakotis olla kirjas: "Mul on palutud teostada `RGB20` liidesest `issue` operatsioon, sellise ja sellise lepingu alusel, 100 000 ühiku ulatuses, sellise ja sellise ühekordse kasutusega pitseri kasuks.*"

Nüüd, kui me oleme vaadanud RGB-programmeerimise põhielemente, tutvustan teile järgmises peatükis, kuidas koostada RGB-lepingut.

## Nutikate lepingute koostamine

<chapterId>0e0a645c-0049-588d-8965-b8c536590cc9</chapterId>

![video](https://youtu.be/GRwS-NvWF3I)

Selles peatükis läheneme lepingu kirjutamisele samm-sammult, kasutades käsurea tööriista `rgb`. Eesmärk on näidata, kuidas paigaldada ja manipuleerida CLI-d, koostada **Skeem**, importida **Interface** ja **Interface Implementation**, seejärel väljastada (*väljastada*) vara. Samuti vaatleme aluseks olevat loogikat, sealhulgas kompileerimist ja oleku valideerimist. Selle peatüki lõpuks peaksite olema võimelised seda protsessi reprodutseerima ja looma oma RGB-lepinguid.

Meeldetuletuseks, et RGB sisemine loogika põhineb Rusti raamatukogudel, mida te arendajatena saate oma projektidesse importida, et hallata kliendipoolset valideerimise osa. Lisaks töötab LNP/BP Associationi meeskond teiste keelte jaoks mõeldud sidemete kallal, kuid see ei ole veel lõplikult välja töötatud. Lisaks arendavad teised üksused, nagu Bitfinex, oma integratsioonipakette (nendest räägime kursuse 2 viimases peatükis). Seega on hetkel `rgb` CLI ametlikuks referentsiks, isegi kui see on veel suhteliselt viimistlemata.

### Tööriista rgb paigaldamine ja esitlemine

Peamine käsk on lihtsalt `rgb`. See on loodud nii, et see meenutab `git`i, koos alamkäskude komplektiga lepingute manipuleerimiseks, nende kutsumiseks, varade väljastamiseks ja nii edasi. Bitcoin Wallet ei ole praegu integreeritud, kuid see saab olema peatses versioonis (0.11). See järgmine versioon võimaldab kasutajatel luua ja hallata oma rahakotte (kirjelduste kaudu) otse `rgb`st, sealhulgas PSBT genereerimine, ühilduvus välise riistvara (nt riistvaraline rahakott) allkirjastamiseks ja koostalitlusvõime sellise tarkvaraga nagu Sparrow. See lihtsustab kogu varade väljastamise ja ülekandmise stsenaariumi.

#### Paigaldamine Cargo kaudu

Me paigaldame tööriista Rust koos :

```bash
cargo install rgb-contracts --all-features
```

(Märkus: crate'i nimi on `rgb-contracts` ja installeeritud käsu nimi on `rgb`. Kui crate nimega `rgb` oli juba olemas, võis tekkida kokkupõrge, sellest ka nimi)

Paigaldus koostab suure hulga sõltuvusi (nt käskude parsimine, Electrumi integreerimine, nullteadmiste tõendite haldamine jne).

Kui paigaldus on lõpetatud, saab :

```bash
rgb
```

Käivitades `rgb` (ilma argumentideta), kuvatakse nimekiri olemasolevatest alamkäskudest, näiteks `liidesed`, `skeem`, `import`, `eksport`, `väljastus`, `arve`, `ülekanne` jne. Saate muuta lokaalset salvestuskataloogi (peidik, mis sisaldab kõiki logisid, skeeme ja rakendusi), valida võrgu (testnet, mainnet) või konfigureerida oma Electrumi serverit.

![RGB-Bitcoin](assets/fr/081.webp)

#### Esimene ülevaade kontrollide kohta

Kui käivitate järgmise käsu, näete, et `RGB20` liides on juba vaikimisi integreeritud:

```bash
rgb interfaces
```

Kui see liides ei ole integreeritud, kloonige :

```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```

Koostage see:

```bash
cargo run
```

Seejärel importige valitud kasutajaliides:

```bash
rgb import interfaces/RGB20.rgb
```

![RGB-Bitcoin](assets/fr/082.webp)

Teisalt öeldakse meile, et ühtegi skeemi ei ole veel tarkvarasse imporditud. Samuti ei ole lepingut kätkesse pandud. Selle nägemiseks käivitage käsk :

```bash
rgb schemata
```

Seejärel saate kloonida repositooriumi teatud skeemide saamiseks:

```bash
git clone https://github.com/RGB-WG/rgb-schemata
```

![RGB-Bitcoin](assets/fr/083.webp)

See repositoorium sisaldab oma kataloogis `src/` mitmeid Rust-faile (näiteks `nia.rs`), mis määratlevad skeemid (NIA nagu "*Non Inflatable Asset*", UDA nagu "*Unique Digital Asset*" jne). Kompileerimiseks saab seejärel käivitada :

```bash
cd rgb-schemata
cargo run
```

See genereerib mitu faili `.rgb` ja `.rgba`, mis vastavad kompileeritud skeemidele. Näiteks leiad `NonInflatableAsset.rgb`.

#### Skeemi ja liidese rakendamise importimine

Nüüd saab skeemi importida `rgb`-sse:

```bash
rgb import schemata/NonInflatableAssets.rgb
```

![RGB-Bitcoin](assets/fr/084.webp)

See lisab selle kohalikku varandusse. Kui käivitame järgmise käsu, näeme, et skeem ilmub nüüd:

```bash
rgb schemata
```

### Lepingu loomine (väljastamine)

Uue vara loomiseks on kaks lähenemisviisi:


- Kas me kasutame skripti või koodi Rustis, mis koostab lepingu, täites skeemi väljad (globaalne olek, omandatud olekud jne) ja toodab `.rgb` või `.rgba` faili;
- Või kasutage otse alamkäsklust `issue` koos YAML (või TOML) failiga, mis kirjeldab sümboli omadusi.

Rustis leiate näiteid kaustast `examples`, mis illustreerivad, kuidas ehitada `ContractBuilder`, täita `globaalne olek` (vara nimi, ticker, pakkumine, kuupäev jne), määrata Owned State (millisele UTXO-le see on määratud), seejärel koostada kõik see *lepingu saadetiseks*, mida saab eksportida, valideerida ja importida stash'ile.

Teine võimalus on käsitsi muuta YAML-faili, et kohandada `ticker`, `name`, `supply` jne. Oletame, et faili nimi on `RGB20-demo.yaml`. Saate määrata :


- `spec`: ticker, nimi, täpsus ;
- `terms`: väli juriidiliste teadete jaoks ;
- `issuedSupply` : väljastatud märgise kogus ;
- `assignments`: näitab ühekordselt kasutatavat pitserit (*pitseri määratlus*) ja lukustamata kogust.

Siin on näide YAML-faili loomiseks:

```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```

![RGB-Bitcoin](assets/fr/085.webp)

Seejärel käivitage lihtsalt käsk :

```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```

![RGB-Bitcoin](assets/fr/086.webp)

Minu puhul on unikaalne skeemi identifikaator (mis tuleb sulgeda jutumärkidesse) `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` ja ma ei ole sisestanud ühtegi väljastajat. Nii et minu tellimus on :

```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```

Kui te ei tea skeemi ID-d, käivitage käsk :

```bash
rgb schemata
```

CLI vastab, et uus leping on väljastatud ja lisatud varandusse. Kui me sisestame järgmise käsu, näeme, et nüüd on olemas täiendav leping, mis vastab äsja väljastatud lepingule:

```bash
rgb contracts
```

![RGB-Bitcoin](assets/fr/087.webp)

Seejärel kuvatakse järgmise käsuga globaalsed olekud (nimi, ticker, pakkumine...) ja nimekiri Owned States, st eraldised (näiteks 1 miljon `PBN` tokenit, mis on määratletud UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).

```bash
rgb state '<ContractId>'
```

![RGB-Bitcoin](assets/fr/088.webp)

### Eksport, import ja valideerimine

Et jagada seda lepingut teiste kasutajatega, saab selle eksportida peidikust :

```bash
rgb export '<ContractId>' myContractPBN.rgb
```

![RGB-Bitcoin](assets/fr/089.webp)

Faili `myContractPBN.rgb` saab edasi anda teisele kasutajale, kes saab selle lisada oma varamusse käsuga :

```bash
rgb import myContractPBN.rgb
```

Kui tegemist on lihtsa *lepingulise kaubasaadetisega*, saame importimisel teate "`Importing consignment rgb`" (kaubasaadetise importimine rgb). Kui tegemist on suurema *riigi ülemineku saadetisega*, on käsk teistsugune (`rgb accept`).

Kehtivuse tagamiseks võite kasutada ka kohalikku valideerimisfunktsiooni. Näiteks võite käivitada :

```bash
rgb validate myContract.rgb
```

#### Varamu kasutamine, kontrollimine ja kuvamine

Meeldetuletuseks, et varamu on skeemide, liideste, rakenduste ja lepingute (Genesis + üleminekud) kohalik inventar. Iga kord, kui te käivitate "import", lisate elemendi varamusse. Seda varandust saab üksikasjalikult vaadata käsuga :

```bash
rgb dump
```

![RGB-Bitcoin](assets/fr/090.webp)

See loob kausta kogu varanduse üksikasjadega.

### Ülekanne ja PSBT

Ülekande teostamiseks peate manipuleerima kohalikku Bitcoini rahakotti, et hallata "Tapret" või "Opret" kohustusi.

#### Loo arve

Enamasti toimub lepingus osalejate (nt Alice ja Bob) vaheline suhtlus arve koostamise kaudu. Kui Alice soovib, et Bob täidaks midagi (sümboolika ülekandmine, uuesti väljastamine, tegevus DAOs jne), loob Alice arve, milles kirjeldatakse üksikasjalikult tema juhiseid Bobile. Seega on meil :


- Alice** (arve väljastaja) ;
- Bob** (kes võtab arve vastu ja täidab selle).

Erinevalt teistest ökosüsteemidest ei ole RGB-arve piiratud makse mõistega. Sellesse võib sisse põimida mis tahes lepinguga seotud taotluse: võtme tühistamine, hääletamine, NFT-le graveeringu (*graveeringu*) loomine jne. Vastavat toimingut saab kirjeldada lepingu liideses. Vastavat toimingut saab kirjeldada lepingu liideses.

Järgmine käsk genereerib RGB-arve:

```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```

Koos :


- `$CONTRACT`: Lepingu identifikaator (*ContractId*) ;
- `$INTERFACE`: kasutatav liides (nt `RGB20`) ;
- `$ACTION`: liideses määratud operatsiooni nimi (lihtsa asendatava sümboli ülekande puhul võib see olla "Transfer"). Kui liides juba pakub vaikimisi tegevust, ei ole vaja seda siin uuesti sisestada;
- `$STATE`: üleantavad olekute andmed (näiteks žetoonide hulk, kui üle kantakse asendatav žetoon);
- `$SEAL`: abisaaja (Alice'i) ühekordselt kasutatav pitsat, st selgesõnaline viide UTXO-le. Bob kasutab seda infot tunnistustehingu koostamiseks ja vastav väljund kuulub seejärel Alice'ile (*pimedas UTXO* või krüpteerimata kujul).

Näiteks järgmiste käskudega

```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```

CLI genereerib arve nagu :

```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```

Seda saab edastada Bobile mis tahes kanali kaudu (tekst, QR-kood jne).

#### Ülekande tegemine

Sellest arvest ülekandmiseks :


- Bobil (kes hoiab žetoonid oma peidus) on Bitcoini rahakott. Ta peab ette valmistama Bitcoini tehingu (PSBT kujul, nt `tx.psbt`), mis kulutab UTXO-d, kus asuvad vajalikud RGB-märgid, pluss üks UTXO valuuta jaoks (vahetus) ;
- Bob täidab järgmise käsu:

```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```


- See genereerib faili `consignment.rgb`, mis sisaldab :
 - Ülemineku ajalugu, mis tõestab Alice'ile, et märgid on ehtsad;
 - Uus üleminek, mis kannab märgid üle Alice'i ühekordselt kasutatavale pitserile ;
 - Tunnistaja tehing (allkirjastamata).
- Bob saadab selle faili `consignment.rgb` Alice'ile (e-posti, jagamisserveri või RGB-RPC-protokolli, Stormi jne kaudu);
- Alice saab `consignment.rgb` ja võtab selle oma peidikusse:

```bash
alice$ rgb accept consignment.rgb
```


- CLI kontrollib ülemineku kehtivust ja lisab selle Alice'i varandusse. Kui käsk on kehtetu, ebaõnnestub see koos üksikasjalike veateadetega. Vastasel juhul õnnestub see ja teatab, et näidistehingut ei ole veel Bitcoini võrgus edastatud (Bob ootab Alice'i rohelist tuld);
- Kinnituseks saadab käsk `accept` allkirja (*maksekviitung*), mille Alice saab saata Bobile, et näidata talle, et ta on *saatekirja* kinnitanud;
- Seejärel saab Bob allkirjastada ja avaldada (--- avaldada) oma Bitcoini tehingu:

```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```


- Niipea, kui see tehing on ahelas kinnitatud, loetakse vara omandiõigus Alice'ile üle läinud. Alice'i rahakott, mis jälgib tehingu kaevandamist, näeb, et tema varakambrisse ilmub uus Owned State.

Järgmises peatükis vaatleme lähemalt RGB integreerimist Lightning-võrku.

## RGB Lightning-võrgus

<chapterId>0962980a-8f94-5d0f-9cd0-43d7f884a01d</chapterId>

![video](https://youtu.be/mqCupTlDbA0)

Käesolevas peatükis teen ettepaneku uurida, kuidas RGB-d saab kasutada Lightning Networkis, et integreerida ja liigutada RGB varasid (märgid, NFT-d jne) ahelavälise maksekanali kaudu.

Põhiidee seisneb selles, et RGB oleku üleminekut (*State Transition*) saab siduda Bitcoini tehinguga, mis omakorda võib jääda ahelaväliseks, kuni Lightning-kanal on suletud. Seega, iga kord, kui kanalit uuendatakse, saab uue RGB oleku ülemineku lisada uude siduvasse tehingusse, mis seejärel muudab vana ülemineku kehtetuks. Sel viisil saab Lightning-kanaleid kasutada RGB varade ülekandmiseks ja neid saab suunata samamoodi nagu tavalisi Lightning-makseid.

### Kanalite loomine ja rahastamine

RGB-vara kandva Lightning-kanali loomiseks on vaja kahte elementi:


- Bitcoini rahastamine, et luua kanali 2/2 multisig (kanali põhiline UTXO);
- RGB rahastamine, mis saadab varad samale multisigile.

Bitcoini mõistes peab rahastamistehing olema olemas, et määratleda viide UTXO, isegi kui see sisaldab ainult väikest kogust sati (see on lihtsalt küsimus iga väljundi tulevaste kohustuste tehingute jäämine üle tolmu piiri kõik sama). Näiteks võib Alice otsustada anda 10k satsit ja 500 USDT (väljastatud RGB varana). Rahastamistehingule lisame kohustuse (`Opret` või `Tapret`), mis ankurdab RGB-staatuse ülemineku.

![RGB-Bitcoin](assets/fr/091.webp)

Kui rahastamistehing on ette valmistatud (kuid veel mitte edastatud), luuakse kulukohustustehingud, nii et kumbki pool saab kanali igal ajal ühepoolselt sulgeda. Need tehingud sarnanevad Lightning'i klassikaliste kohustustehingutega, kuid me lisame täiendava väljundi, mis sisaldab RGB-ankrit (OP_RETURN või Taproot), mis on seotud uue oleku üleminekuga.

Seejärel liigub RGB olekuga üleminek varad 2/2 multisig rahastamisest kulukohustustehingu väljunditesse. Selle protsessi eelis on see, et RGB-oleku turvalisus vastab täpselt Lightningi karistusmehhanismile: kui Bob edastab vana kanali oleku, saab Alice teda karistada ja kulutada väljundit, et saada tagasi nii satsid kui ka RGB-märgid. Seega on stiimul veelgi tugevam kui Lightning-kanalis ilma RGB varadeta, sest ründaja võib kaotada mitte ainult satsid, vaid ka kanali RGB varad.

Alice'i poolt allkirjastatud ja Bobile saadetud kohustustehing näeks seega välja järgmiselt:

![RGB-Bitcoin](assets/fr/092.webp)

Ja sellega kaasnev kohustustehing, mille Bob on allkirjastanud ja Alice'ile saatnud, näeb välja selline:

![RGB-Bitcoin](assets/fr/093.webp)

### Kanali uuendamine

Kui kahe kanali osaleja vahel toimub makse (või kui nad soovivad muuta varade jaotust), loovad nad uue paari kohustustehinguid. Sõltuvalt rakendusest võib summa satsides kummalgi väljundil jääda või mitte jääda muutumatuks, sest selle peamine roll on võimaldada kehtivate UTXOde koostamist. Teisest küljest tuleb OP_RETURN (või Taproot) väljundit muuta, et see sisaldaks uut RGB-ankrit, mis esindab uut varade jaotust kanalis.

Näiteks kui Alice kannab kanalis Bobile üle 30 USDT, kajastab uus olek üleminekul Alice'i saldo 400 USDT ja Bobi saldo 100 USDT. Selle ülemineku lisamiseks lisatakse (või muudetakse) OP_RETURN/Taproot-ankrule tehing, et lisada see üleminek. Pange tähele, et RGB seisukohalt jääb ülemineku sisendiks esialgne multisig (kus tegelikult jaotatakse ahelas olevad varad kuni kanali sulgemiseni). Ainult RGB väljundid (jaotused) muutuvad, sõltuvalt ümberjaotamisest, mille üle otsustatakse.

Alice'i allkirjastatud kohustustehing, mida Bob on valmis levitama:

![RGB-Bitcoin](assets/fr/094.webp)

Kohustustehing, mille on allkirjastanud Bob, valmis Alice'i poolt levitamiseks:

![RGB-Bitcoin](assets/fr/095.webp)

### HTLC juhtimine

Tegelikkuses võimaldab Lightning Network makseid suunata mitme kanali kaudu, kasutades HTLC-d (*Hashed Time-Locked Contracts*). Sama kehtib ka RGB puhul: iga kanali kaudu toimuva makse puhul lisatakse tehingu sooritamisele HTLC väljund ja selle HTLC-ga seotud RGB eraldus. Seega, kes iganes kulutab HTLC-väljundi (tänu saladusele või pärast ajaluku lõppemist), saab tagasi nii satsid kui ka sellega seotud RGB-vara. Teisest küljest on ilmselgelt vaja, et teil oleks piisavalt raha teel nii satside kui ka RGB varade osas.

![RGB-Bitcoin](assets/fr/096.webp)

Seetõttu tuleb RGB toimimist Lightning'ile vaadelda paralleelselt Lightning-võrgu enda toimimisega. Kui soovite selles teemas sügavamalt süveneda, siis soovitan kindlasti vaadata seda teist põhjalikku koolituskursust:

https://planb.network/courses/lnp201
### RGB koodikaart

Lõpuks, enne järgmise jaotise juurde minekut, tahaksin anda teile ülevaate RGB-s kasutatavast koodist. Protokoll põhineb Rusti raamatukogudel ja avatud lähtekoodiga spetsifikatsioonidel. Siin on ülevaade peamistest repositooriumidest ja kastidest:

![RGB-Bitcoin](assets/fr/097.webp)

#### Kliendipoolne valideerimine


- Hoiukoht**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- Kastid** : [kliendipoolne_valideerimine](https://crates.io/crates/client_side_validation), [ühekordsed_kasutustõkendid](https://crates.io/crates/single_use_seals)

Ahelavälise valideerimise ja ühekordse kasutusega plommide loogika haldamine.

#### Deterministlikud Bitcoini kohustused (DBC)


- Hoiukoht**: [bp-core](https://github.com/BP-WG/bp-core)
- Kast**: [bp-dbc](https://crates.io/crates/bp-dbc)

Deterministliku ankurdamise haldamine Bitcoini tehingutes (Tapret, OP_RETURN jne).

#### Mitme protokolliga seotud kohustused (MPC)


- Hoiukoht**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- Kast** : [commit_verify](https://crates.io/crates/commit_verify)

Mitmesugused sidumiskombinatsioonid ja integratsioon erinevate protokollidega.

#### Ranged tüübid ja range kodeerimine


- Spetsifikatsioonid**: [veebisait strict-types.org](https://www.strict-types.org/)
- Repositooriumid**: [strict-types](https://github.com/strict-types/strict-types), [strict-encoding](https://github.com/strict-types/strict-encoding)
- Kastid** : [strict_types](https://crates.io/crates/strict_types), [strict_encoding](https://crates.io/crates/strict_encoding)

Kliendipoolseks valideerimiseks kasutatav range tüübisüsteem ja deterministlik serialiseerimine.

#### RGB tuum


- Hoiukoht**: [rgb-core](https://github.com/RGB-WG/rgb-core)
- Kast**: [rgb-core](https://crates.io/crates/rgb-core)

Protokolli tuum, mis hõlmab RGB valideerimise peamist loogikat.

#### RGB standardne raamatukogu ja rahakott


- Hoiukoht**: [rgb-std](https://github.com/RGB-WG/rgb-std)
- Kast** : [rgb-std](https://crates.io/crates/rgb-std)

Standardsed rakendused, varude ja rahakoti haldamine.

#### RGB CLI


- Hoiukoht**: [rgb](https://github.com/RGB-WG/rgb)
- Kastid**: [rgb-cli](https://crates.io/crates/rgb-cli), [rgb-wallet](https://crates.io/crates/rgb-wallet)

`rgb` CLI ja crate wallet, lepingute käsurea manipuleerimiseks.

#### RGB skeem


- Hoiukoht**: [rgb-skeemid](https://github.com/RGB-WG/rgb-schemata/)

Sisaldab näiteid skeemide (NIA, UDA jne) ja nende rakenduste kohta.

#### ALuVM


- Info** : [aluvm.org](https://www.aluvm.org/)
- Repositooriumid**: [aluvm-spec](https://github.com/AluVM/aluvm-spec), [alure](https://github.com/AluVM/alure)
- Kastid**: [aluvm](https://crates.io/crates/aluvm), [aluasm](https://crates.io/crates/aluasm)

Registripõhine virtuaalmasin, mida kasutatakse valideerimisskriptide käivitamiseks.

#### Bitcoini protokoll - BP


- Repositooriumid** : [bp-core](https://github.com/BP-WG/bp-core), [bp-std](https://github.com/BP-WG/bp-std), [bp-wallet](https://github.com/BP-WG/bp-wallet)

Bitcoini protokolli (tehingud, ümbersõidud jne) toetavad lisaseadmed.

#### Ubiquitous Deterministic Computing - UBIDECO


- Hoiukoht**: [UBIDECO](https://github.com/UBIDECO)

Ökosüsteem, mis on seotud avatud lähtekoodiga deterministlike arendustega.

# RGB-le tuginedes

<partId>3b4b0d66-0c1b-505a-b5ca-4b2e57dd73c2</partId>

## DIBA ja Bitmask projekt

<chapterId>dc92a5e8-ed93-5a3f-bcd0-d433932842f4</chapterId>

![video](https://youtu.be/nbUtV8GOR_U)

See kursuse viimane osa põhineb erinevate RGB bootcamp'i esinejate ettekannetel. See sisaldab RGB ja selle ökosüsteemi kohta käivaid iseloomustusi ja mõtisklusi, samuti protokollile tuginevate vahendite ja projektide tutvustusi. Seda esimest peatükki modereerib Hunter Beast ja kahte järgmist Frederico Tenga.

### JavaScriptist Rustini ja Bitcoini ökosüsteemi

Alguses töötas Hunter Beast peamiselt JavaScriptis. Siis avastas ta **Rust**, mille süntaks tundus esialgu ebameeldiv ja frustreeriv. Kuid ta hakkas hindama selle keele võimsust, kontrolli mälu (*heap* ja *stack*) üle ning sellega kaasnevat turvalisust ja jõudlust. Ta rõhutab, et Rust on suurepärane treeneriõpe arvuti tööpõhimõtete süvitsi mõistmiseks.

Hunter Beast räägib oma taustast erinevates projektides *altcoini* ökosüsteemis, nagu Ethereum (Solidity, TypeScript jne) ja hiljem Filecoin. Ta selgitab, et esialgu avaldasid talle mõned protokollid muljet, kuid lõpuks oli ta enamikus neist pettunud, mitte ainult nende tokenoomika tõttu. Ta mõistab hukka kahtlased finantsstiimulid, investoreid lahjendava tokenite inflatsioonilise loomise ja nende projektide potentsiaalselt ekspluateeriva aspekti. Seega võttis ta lõpuks **Bitcoini maksimalistliku** seisukoha, mitte ainult seetõttu, et mõned inimesed avasid talle silmad Bitcoini kindlamate majandusmehhanismide ja selle süsteemi tugevuse suhtes.

### RGB ja kihtide ülesehitamine

Tema sõnul veenis teda lõplikult Bitcoini olulisuses RGB ja kihtide kontseptsiooni avastamine. Ta usub, et teistes plokiahelates olemasolevaid funktsioone saab reprodutseerida kõrgematel kihtidel, mis asuvad Bitcoinist kõrgemal, ilma põhiprotokolli muutmata.

Veebruaris 2022 liitus ta **DIBAga**, et töötada spetsiaalselt RGB ja eelkõige **Bitmask** rahakoti kallal. Sel ajal oli Bitmask veel versioonil 0.01 ja RGB töötas versioonil 0.4, ainult üksikute žetoonide haldamiseks. Ta märgib, et see oli vähem enesekohane kui tänapäeval, kuna loogika oli osaliselt serveripõhine. Sellest ajast alates on arhitektuur arenenud selle mudeli suunas, mida bitcoin'i kasutajad väga hindavad.

### RGB-protokolli alused

**RGB** protokoll on kõige uuem ja arenenum _värviliste müntide_ kontseptsioon, mida uuriti juba aastatel 2012-2013. Toona püüdsid mitmed meeskonnad seostada UTXOdele erinevaid bitcoinide väärtusi, mis viis mitmete hajutatud rakendusteni. See standardiseerimise puudumine ja tollane vähene nõudlus takistasid neil lahendustel püsivalt kanda kinnitada.

Tänapäeval paistab RGB silma oma kontseptuaalse tugevuse ja ühtsete spetsifikatsioonide poolest LNP/BP assotsiatsiooni kaudu. Põhimõte põhineb kliendipoolsel valideerimisel. Bitcoini plokiahelas salvestatakse ainult krüptograafilisi kohustusi (_commitments_, Taproot või OP_RETURN kaudu), samas kui enamiku andmetest (lepingu määratlused, ülekannete ajalugu jne) salvestavad asjaomased kasutajad. Sel viisil jaotatakse salvestuskoormus ja tugevdatakse vahetuste konfidentsiaalsust, ilma et see koormaks plokiahelat. Selline lähenemisviis võimaldab moodulite ja skaleeritava raamistiku raames luua asendatavaid varasid (**RGB20** standard) või unikaalseid varasid (**RGB21** standard).

### Märkide funktsioon (RGB20) ja unikaalsed varad (RGB21)

**RGB20** abil määratleme Bitcoinis asendatava sümboli. Emitent valib _tarne_, _täpsuse_ ja loob _lepingu_, mille raames ta saab seejärel ülekandeid teha. Igale ülekandele viidatakse Bitcoini UTXO-le, mis toimib *Esmakordselt kasutatava pitserina*. See loogika tagab, et kasutaja ei saa sama vara kaks korda kulutada, kuna ainult UTXO kulutamiseks võimeline isik omab tegelikult võtit, et uuendada kliendipoolse lepingu seisu.

**RGB21** on suunatud unikaalsetele varadele (või "NFT"). Varal on pakkumine 1 ja seda saab seostada metaandmetega (pildifail, heli jne), mida kirjeldatakse konkreetse välja kaudu. Erinevalt avalike plokiahelate NFT-dest võivad andmed ja nende MIME-tunnused jääda privaatseks, jagades neid omaniku äranägemise järgi peer-to-peer.

### Bitmask lahendus: RGB rahakott

RGB võimaluste praktiliseks kasutamiseks on projekt **DIBA** loonud rahakoti nimega [Bitmask](https://bitmask.app/). Idee on pakkuda Taprootil põhinevat mittekasutatavat vahendit, mis on kättesaadav veebirakenduse või brauseripikendusena. Bitmask haldab nii RGB20 kui ka RGB21 varasid ning integreerib erinevaid turvamehhanisme:


- Põhikood on kirjutatud Rustis, seejärel kompileeritud WebAssembly'is, et töötada JavaScript-keskkonnas (React);
- Võtmed genereeritakse lokaalselt, seejärel salvestatakse need krüpteeritult lokaalselt ;
- Riigiandmeid (stash) hoitakse mälus, seerialiseeritakse ja krüpteeritakse **Carbonado** raamatukogu abil, mis teostab Blake3 abil pakkimist, veaparandust, krüpteerimist ja voo kontrollimist.

Tänu sellisele arhitektuurile toimuvad kõik varade tehingud kliendi poolel. Väljastpoolt vaadatuna ei ole Bitcoini tehing midagi muud kui klassikaline Taproot-kulutustehing, mille puhul keegi ei kahtlustaks, et sellega kaasneb ka vahetatavate žetoonide või NFTde ülekandmine. On-chaini ülekoormuse puudumine (avalikult salvestatud metaandmed puuduvad) tagab teatava diskreetsuse ja lihtsustab võimalike tsensuurikatsete tõrjumist.

### Turvalisus ja hajutatud arhitektuur

Kuna RGB-protokoll nõuab, et iga osaleja säilitaks oma tehinguajaloo (et tõestada saadud ülekannete kehtivust), tekib küsimus salvestamise kohta. Bitmask pakub välja, et see varamu serialiseeritakse lokaalselt ja saadetakse seejärel mitmesse serverisse või pilve (valikuliselt). Andmed jäävad kasutaja poolt **Carbonado** kaudu krüpteerituks, nii et server ei saa neid lugeda. Osalise rikkumise korral saab veaparanduskihi abil sisu taastada.

CRDT (_konfliktivaba replitseeritud andmetüüp_) kasutamine võimaldab varamu erinevaid versioone ühendada, kui need erinevad üksteisest. Igaüks võib neid andmeid vabalt hostida, kus iganes ta soovib, kuna ükski täielik sõlmpunkt ei kanna kogu varaga seotud teavet. See peegeldab täpselt *Client-side Validation* filosoofiat, kus iga omanik vastutab oma RGB vara kehtivuse tõendite säilitamise eest.

### Laiema ökosüsteemi suunas: turg, koostalitlusvõime ja uued funktsioonid

Bitmaski taga olev ettevõte ei piirdu ainult rahakoti arendamisega. DIBA kavatseb arendada :


- **turg** žetoonide vahetamiseks, eelkõige **RGB21** kujul;
- Ühilduvus teiste rahakottidega (näiteks *Iris Wallet*);
- Ülekannete batching** tehnika, st võimalus lisada mitu järjestikust RGB ülekannet ühte tehingusse.

Samal ajal töötame **WebBTC** või **WebLN** (standardid, mis võimaldavad veebilehtedel paluda rahakotil allkirjastada Bitcoin- või Lightning-tehinguid), samuti võime "telebronnida" Ordinals-kirjeid (kui tahame Ordinals'i diskreetsemasse ja paindlikumasse RGB-vormingusse repatrieerida).

### Kokkuvõte

Kogu protsess näitab, kuidas RGB ökosüsteemi saab kasutusele võtta ja lõppkasutajatele kättesaadavaks teha jõuliste tehniliste lahenduste abil. Üleminek altcoini perspektiivist Bitcoin-kesksemale visioonile koos *Client-side Validation* avastamisega näitab üsna loogilist teed: me mõistame, et on võimalik rakendada erinevaid funktsioone (fungible tokenid, NFT, smart contracts...) ilma plokiahelat kahveldamata, lihtsalt kasutades ära krüptograafilisi kohustusi Taproot-tehingutes või OP_RETURNides.

**Bitmask** rahakott on osa sellest lähenemisviisist: plokiahela poolel näete ainult tavalist Bitcoini tehingut; kasutaja poolel manipuleerite veebiliidesega, kus saate luua, vahetada ja salvestada igasuguseid ahelaväliseid varasid. See mudel eristab selgelt rahalise infrastruktuuri (Bitcoin) väljaandmis- ja ülekandeloogikast (RGB), tagades samal ajal kõrge konfidentsiaalsuse ja parema skaleeritavuse.

## Bitfinexi töö RGBga

<chapterId>d4d80e07-5eac-5b29-a93a-123180e97047</chapterId>

![vidéo](https://youtu.be/5iAhsgCSL3U)

Selles peatükis, mis põhineb Frederico Tenga ettekandel, vaatleme Bitfinexi meeskonna poolt loodud RGB-le pühendatud vahendeid ja projekte, mille eesmärk on edendada selle protokolli ümber rikkaliku ja mitmekesise ökosüsteemi tekkimist. Meeskonna esialgne eesmärk ei ole välja anda konkreetset kaubanduslikku toodet, vaid pigem pakkuda tarkvara ehitusplokke, aidata kaasa RGB-protokollile endale ja pakkuda välja konkreetseid rakendusviiteid, näiteks mobiilne rahakott (*Iris Wallet*) või RGB-ga ühilduv Lightning-sõlm.

### Taust ja eesmärgid

Alates umbes 2022. aastast on Bitfinexi RGB meeskond keskendunud tehnoloogilise korpuse arendamisele, mis võimaldab RGB-d tõhusalt ära kasutada ja testida. On tehtud mitmeid panuseid:


- Osalemine lähtekoodi ja protokollide spetsifikatsioonides, sealhulgas parendusettepanekute kirjutamine, vigade parandamine jne;
- Tööriistad arendajatele, et lihtsustada RGB integreerimist oma rakendustesse;
- Mobiilse rahakoti [Iris] (https://iriswallet.com/) kujundamine, et katsetada ja illustreerida RGB kasutamise parimaid tavasid;
- Kohandatud Lightning-sõlme loomine, mis on võimeline haldama RGB-vara kanalit;
- Teiste meeskondade toetamine RGB-lahenduste loomisel, et soodustada mitmekesisust ja tugevat ökosüsteemi.

Selle lähenemisviisi eesmärk on katta kogu vajaduste ahel: alates madala taseme raamatukogust (*[RGBlib](https://github.com/RGB-Tools/rgb-lib)*), mis võimaldab rahakoti rakendamist, kuni tootmisaspektini (Lightning-sõlm, rahakott Androidile jne).

### RGBlib raamatukogu: RGB-rakenduste arendamise lihtsustamine

RGB rahakottide ja rakenduste loomise demokratiseerimisel on oluline teha kättesaadavaks piisavalt lihtne abstraktsioon, et arendajad ei peaks õppima kõike protokolli sisemise loogika kohta. Just see ongi Rustis kirjutatud **RGBlib** eesmärk.

RGBlib toimib sillana RGB väga paindlike (kuid mõnikord keeruliste) nõuete, mida oleme saanud uurida eelmistes peatükkides, ja rakenduse arendaja konkreetsete vajaduste vahel. Teisisõnu, rahakott (või teenus), mis soovib hallata žetoonide ülekandeid, varade väljastamist, verifitseerimist jne, saab tugineda RGBlibile, teadmata iga krüptograafilist detaili või iga kohandatavat RGB parameetrit.

Raamatupood pakub :


- Võtmevalmiduse funktsioonid varade (vahetatavate või mitte) emiteerimiseks (_emiteerimiseks_);
- Võimalus edastada (saata/vastuvõtta) varasid lihtsate objektidega (aadressid, summad, UTXOd jne) manipuleerides;
- Mehhanism kliendipoolse valideerimise jaoks vajaliku staatusteabe (*saated*) salvestamiseks ja laadimiseks.

RGBlib tugineb seega RGB-le spetsiifilistele keerulistele mõistetele (kliendipoolne valideerimine, Tapret/Opret ankurdused), kuid kapseldab need, nii et lõplik rakendus ei pea kõike ümber programmeerima või tegema riskantseid otsuseid. Veelgi enam, RGBlib on juba seotud mitme keelega (Kotlin ja Python), mis avab ukse kasutusvõimalustele väljaspool lihtsat Rusti universumit.

### Iris Wallet: näide RGB rahakoti kohta Androidis

RGBlib'i tõhususe tõestamiseks on Bitfinexi meeskond välja töötanud **Iris Wallet**, mis on praegu ainult Androidile mõeldud. See on mobiilne rahakott, mis illustreerib tavalisele Bitcoini rahakotile sarnast kasutajakogemust: saate väljastada vara, saata seda, vastu võtta ja vaadata selle ajalugu, jäädes samal ajal isehoidmise mudelile.

Iirisel on mitmeid huvitavaid omadusi:

**Kasutades Electrumi serverit:**

Nagu iga rahakott, peab Iris teadma tehingu kinnitustest plokiahelas. Täieliku sõlme manustamise asemel kasutab Iris vaikimisi Bitfinexi meeskonna poolt hallatavat Electrumi serverit. Kasutajad võivad siiski konfigureerida oma serveri või mõne muu kolmanda osapoole teenuse. Sel viisil saab Bitcoini tehinguid valideerida ja teavet otsida (indekseerida) modulaarselt.

**RGB proxy server:**

Erinevalt Bitcoinist on RGB puhul vaja saatja ja vastuvõtja vahel vahetada ahelaväliseid metaandmeid (*saadetised*). Selle protsessi lihtsustamiseks pakub Iris lahendust, kus suhtlus toimub proxy-serveri kaudu. Vastuvõttev rahakott genereerib *arve*, milles on märgitud, kuhu saatja peaks saatma *kliendipoolsed* andmed. Vaikimisi osutab URL aadress Bitfinexi meeskonna poolt majutatud proxy'le, kuid te saate seda proxy'd muuta (või majutada omaenda proxy'd). Idee on naasta tuttava kasutajakogemuse juurde, kus saaja kuvab QR-koodi ja saatja skaneerib selle koodi tehingu sooritamiseks, ilma keeruliste lisamanipulatsioonideta.

**Jooksev varundamine:**

Rangelt Bitcoini kontekstis piisab üldiselt seemne varundamisest (kuigi tänapäeval soovitame selle asemel varundada seemet ja kirjeldusi). RGB puhul ei piisa sellest: teil on vaja säilitada ka kohalik ajalugu (*konsignatsioonid*), mis tõestab, et te tõesti omate RGB vara. Iga kord, kui saate kviitungi, salvestab seade uued andmed, mis on olulised hilisemate kulutuste tegemiseks. Iris haldab automaatselt krüpteeritud varukoopiat kasutaja Google Drive'is. See ei nõua erilist usaldust Google'i vastu, kuna varukoopia on krüpteeritud, ning tulevikus on kavas kasutada jõulisemaid võimalusi (nt isiklik server), et vältida tsensuuri või kustutamise ohtu kolmanda osapoole operaatori poolt.

**Muud omadused:**


- Loo kraan, et kiiresti katsetada või levitada žetoone eksperimenteerimiseks või reklaamimiseks;
- Sertifitseerimissüsteem (praegu tsentraliseeritud), et eristada seaduslikku sümbolit võltsitud sümbolist, mis kopeerib kuulsat ticker'i. Tulevikus võib see sertifitseerimine muutuda detsentraliseeritumaks (DNSi või muude mehhanismide kaudu).

Kokkuvõttes pakub Iris kasutajakogemust, mis sarnaneb klassikalise Bitcoini rahakoti omale, varjates tänu RGBlibile ja proxy-serveri kasutamisele täiendavat keerukust (varude haldamine, *saadetiste* ajalugu jne).

### Proxy server ja kasutajakogemus

Eespool tutvustatud proxy-server väärib üksikasjalikku kirjeldust, sest see on sujuva kasutajakogemuse võti. Selle asemel, et saatja peaks *saadetised* käsitsi saajale edastama, toimub RGB-tehing taustal :


- Vastuvõtja koostab *arve* (mis sisaldab muu hulgas proxy-aadressi);
- Saatja saadab (HTTP päringu kaudu) üleminekuprojekti (*saatekiri*) proxy'le ;
- Vastuvõtja hangib selle projekti, teostab *kliendipoolse* valideerimise lokaalselt;
- Seejärel avaldab vastuvõtja proxy kaudu oleku ülemineku vastuvõtmise (või võimalusel tagasilükkamise) ;
- Saatja saab vaadata valideerimise staatust ja kui see on aktsepteeritud, edastada Bitcoini tehingu, mis lõpetab ülekande.

Sel viisil käitub rahakott peaaegu nagu tavaline rahakott. Kasutaja ei ole kõigist vaheetappidest teadlik. Tõsi, praegune vahendaja ei ole krüpteeritud ega autenditud (mis jätab muret konfidentsiaalsuse ja terviklikkuse pärast), kuid need parandused on võimalikud hilisemates versioonides. Vahenduskontseptsioon on endiselt väga kasulik, et taastada "ma saadan QR-koodi, sa skaneerid, et maksta" kogemus.

### RGB integratsioon Lightning Network'is

Bitfinexi meeskonna töö teine põhirõhk on Lightning Networki ühildamine RGB varadega. Eesmärgiks on võimaldada Lightning-kanalite kasutamist USDT-s (või mõnes muus tokenis) ning kasutada samu eeliseid, mis bitcoinil Lightningis (peaaegu kohesed tehingud, marsruutimine jne). Konkreetselt tähendab see Lightning-sõlme loomist, mis on modifitseeritud :


- Avage kanal, paigutades mitte ainult satoshis, vaid ka üks või mitu RGB vara rahastamisel UTXO multisig ;
- Loo Lightning'i kohustustehingud (Bitcoini pool) koos vastavate RGB olekute üleminekutega. Iga kord, kui kanalit ajakohastatakse, määrab RGB-üleminek uuesti vara jaotuse Lightning-väljundites;
- Võimaldab ühepoolse sulgemise, kus vara võetakse tagasi ainuõiguslikus UTXOs, vastavalt Lightning Networki eeskirjadele (HTLC, timelock, karistus jne).

See lahendus, mis kannab nime "**RGB Lightning Node**", kasutab LDK (*Lightning Dev Kit*) baasina ja lisab kanalitesse RGB-märkide süstimiseks vajalikud mehhanismid. Lightning-kohustused säilitavad klassikalise struktuuri (punktuaalsed väljundid, timelock...) ja lisaks sellele kinnitavad RGB-staatuse ülemineku (`Opret` või `Tapret` kaudu). Kasutaja jaoks avab see tee Lightning-kanalitele stabiilse mündi või mis tahes muu RGB kaudu emiteeritud vara puhul.

### DEXi potentsiaal ja mõju Bitcoinile

Kui mitut vara hallatakse Lightning'i kaudu, on võimalik ette kujutada **atomaarset vahetust** ühel Lightning'i marsruudil, kasutades sama saladuste ja ajamärkide loogikat. Näiteks kasutaja A hoiab bitcoini ühes Lightning-kanalis ja kasutaja B hoiab USDT RGB-d teises Lightning-kanalis. Nad võivad luua oma kahte kanalit ühendava tee ja vahetada samaaegselt BTC-d USDT vastu, ilma et oleks vaja usaldust. See ei ole midagi muud kui **atomaarne vahetus**, mis toimub mitme hüppe jooksul, mistõttu välised osalejad peaaegu ei märka, et nad teevad kaubandust, mitte lihtsalt marsruutimist. See lähenemisviis pakub :


- Väga väike latentsus, kuna kõik jääb Lightningi puhul ahelaväliseks.
- Suurepärane **privaatsus**: keegi ei tea, et see on kaubandus, mitte tavaline marsruutimine ;
- Vältides frontrunningut, mis on korduv probleem ahelas oleva DEXi puhul;
- Vähendatud kulud (te ei maksa plokkide ruumi, vaid ainult Lightning'i marsruutimistasu).

Seejärel võime ette kujutada ökosüsteemi, kus Lightning-sõlmed pakuvad vahetushindu (pakkudes likviidsust). Iga sõlmpunkt võib soovi korral mängida _turutegija_ rolli, ostes ja müües erinevaid varasid Lightningis. See _Kihi-2_ DEXi väljavaade tugevdab ideed, et detsentraliseeritud varabörside saamiseks ei ole vaja hargneda või kasutada kolmanda osapoole plokiahelaid.

Mõju Bitcoinile võib olla positiivne: Tänu nende *stabiilsete müntide*, tuletisinstrumentide ja muude müntide tekitatud mahtudele oleks Lightning'i infrastruktuur (sõlmed, kanalid ja teenused) paremini ära kasutatud. Kaupmehed, kes on huvitatud USDT-maksetest Lightningis, avastaksid mehaaniliselt BTC-maksed Lightningis (mida haldab sama stack). Lightning Networki infrastruktuuri hooldus ja rahastamine võiks samuti kasu saada nende mitte-BTC-voogude mitmekordistumisest, mis tooks kaudselt kasu Bitcoini kasutajatele.

### Kokkuvõte ja ressursid

Bitfinexi RGB-le pühendunud meeskond näitab oma tööga, kui mitmekesine on see, mida saab protokolli peal teha. Ühelt poolt on RGBlib, raamatukogu, mis hõlbustab rahakottide ja rakenduste kujundamist. Teisest küljest on meil Iris Wallet, mis on praktiline demonstratsioon Androidi korralikust lõppkasutaja kasutajaliidesest. Lõpuks näitab RGB integreerimine Lightningiga, et stabiilsecoini kanalid on võimalikud, ja avab tee võimalikule detsentraliseeritud DEXile Lightningil.

See lähenemisviis on endiselt suures osas eksperimentaalne ja areneb edasi: RGBlib'i raamatukogu täiustatakse pidevalt, Iris Wallet saab regulaarselt täiendusi ja spetsiaalne Lightning-sõlm ei ole veel peavoolu Lightning-klient.

Neile, kes soovivad rohkem teada saada või anda oma panuse, on kättesaadavad mitmed ressursid, sealhulgas :


- [GitHub RGB Tools repositooriumid](https://github.com/RGB-Tools);
- [Iris Wallet'ile pühendatud teabesait](https://iriswallet.com/), et testida rahakotti Androidil.

Järgmises peatükis vaatleme lähemalt, kuidas RGB Lightning-sõlme käivitada.

## RLN - RGB välgussõlm

<chapterId>ecaabe32-20ba-5f8c-8ca1-a3f095792958</chapterId>

![vidéo](https://youtu.be/piQQH4Q2nr0)

Selles viimases peatükis viib teid Frederico Tenga samm-sammult läbi Lightning RGB-sõlme seadistamise Regtest-keskkonnas ja näitab, kuidas luua RGB-märke. Käivitades kaks eraldi sõlme, avastate ka, kuidas avada nende vahel Lightning-kanal ja vahetada RGB-vara.

See video on õpetus, mis sarnaneb eelmises peatükis käsitletule, kuid seekord on keskendunud just Lightningile!

Selle video peamine allikas on Githubi repositoorium [RGB Lightning Node](https://github.com/RGB-Tools/rgb-lightning-node), mis teeb selle konfiguratsiooni käivitamise Regtestis lihtsaks.

### RGB-ühilduva Lightning-sõlme kasutuselevõtt

Protsessi käigus võetakse kasutusele ja rakendatakse praktikas kõik eelmistes peatükkides käsitletud mõisted:


- Idee, et **UTXO** blokeeritud 2/2 multisig kohta Lightning kanal saab mitte ainult bitcoins, vaid ka üheotstarbeline pitsat RGB varade (fungible või mitte) ;
- Igas Lightning engagement tehingus on lisatud väljund (`Tapret` või `Opret`), mis on ette nähtud RGB oleku ülemineku kinnistamiseks;
- Sellega seotud infrastruktuur (bitcoind/indexer/proxy) Bitcoini tehingute valideerimiseks ja *kliendipoolsete* andmete vahetamiseks.

### Sissejuhatus rgb-lightning-node

Projekt **`rgb-lightning-node`** on Rust'i deemon, mis põhineb `rust-lightning` (LDK) kahvlil, mida on muudetud, et võtta arvesse RGB varade olemasolu kanalis. Kui kanal avatakse, saab vara olemasolu määrata ja iga kord, kui kanali olekut uuendatakse, luuakse RGB üleminek, mis kajastab vara jaotust Lightning-väljundites. See võimaldab :


- Avatud Lightning-kanalid USDT-s, näiteks;
- Suunata need märgid läbi võrgu, tingimusel, et marsruutimisradadel on piisavalt likviidsust;
- Kasutage Lightning'i karistus- ja ajalukustusloogikat ilma muudatusteta: lihtsalt kinnistage RGB-üleminek täiendavasse kohustustehingu väljundisse.

Kood on veel alfa-staadiumis: soovitame seda kasutada ainult **regtestis** või **testnetis**.

### Sõlme paigaldamine

Selleks, et kompileerida ja installeerida `rgb-lightning-node` binaarsüsteemi, alustame repositooriumi ja selle alammoodulite kloonimisest, seejärel käivitame :

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RGB-Bitcoin](assets/fr/098.webp)


- Valik `--recurse-submodules` kloonib ka vajalikud alamseadmed (sealhulgas modifitseeritud versiooni `rust-lightning`);
- Valik `--shallow-submodules` piirab kloonimise sügavust, et kiirendada allalaadimist, pakkudes samal ajal juurdepääsu olulistele kommittidele.

Projekti juurest käivitage järgmine käsk, et kompileerida ja paigaldada binaarsüsteem :

```bash
cargo install --locked --debug --path .
```

![RGB-Bitcoin](assets/fr/099.webp)


- `--locked` tagab, et sõltuvuste versioonist peetakse rangelt kinni;
- `--debug` ei ole kohustuslik, kuid võib aidata teil keskenduda (võite kasutada `--release`, kui soovite) ;
- `--path .` ütleb `cargo install`ile, et ta installiks praegusest kataloogist.

Selle käsu lõpus on teie `$CARGO_HOME/bin/` käsureale `$CARGO_HOME/bin/` saadaval käivitatav `rgb-lightning-node`. Veenduge, et see tee on teie `$PATH`-s, et saaksite käsku käivitada mis tahes kataloogist.

### Tulemuslikkuse nõuded

Selleks, et toimida, vajab deemon `rgb-lightning-node` olemasolu ja konfiguratsiooni :


- Sõlm `bitcoind`**

Iga RLNi instants peab suhtlema "bitcoindiga", et edastada ja jälgida oma ahelasisesed tehingud. Daemonile tuleb esitada autentimine (sisselogimine/parool) ja URL (host/port).


- Indekseerija** (Electrum või Esplora)

Deemon peab suutma loetleda ja uurida ahelas toimuvaid tehinguid, eelkõige leida UTXO, millele vara on ankurdatud. Peate määrama oma Electrumi serveri või Esplora URL-i.


- RGB** proxy

Nagu eelmistes peatükkides on näha, on **proxy server** komponent (valikuline, kuid väga soovitatav), mis lihtsustab Lightning-partnerite vahelist *saatekirjade* vahetamist. Jällegi tuleb määrata URL.

ID-d ja URL-d sisestatakse, kui deemon on API kaudu _avatud_. Sellest rohkem hiljem.

### Regtest käivitamine

Lihtsaks kasutamiseks on olemas skript `regtest.sh`, mis käivitab automaatselt Dockeri kaudu hulga teenuseid: `bitcoind`, `electrs` (indexer), `rgb-proxy-server`.

![RGB-Bitcoin](assets/fr/100.webp)

See võimaldab teil käivitada kohaliku, isoleeritud, eelnevalt konfigureeritud keskkonna. See loob ja hävitab konteinerid ja andmekataloogid igal taaskäivitamisel. Alustame käivitades :

```bash
./regtest.sh start
```

See skript on :


- Looge kataloog `docker/`, et salvestada ;
- Käivitage regtestis `bitcoind`, samuti indekseerija `electrs` ja `rgb-proxy-server` ;
- Oodake, kuni kõik on kasutusvalmis.

![RGB-Bitcoin](assets/fr/101.webp)

Järgnevalt käivitame mitu RLN-sõlme. Käivitage eraldi kestades näiteks (3 RLN-sõlme käivitamiseks) :

```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```

![RGB-Bitcoin](assets/fr/102.webp)


- Parameeter `--network regtest` näitab regtest-konfiguratsiooni kasutamist;
- `--daemon-listening-port` näitab, millises REST-portis Lightning-sõlm hakkab API-kõnesid (JSON) kuulama;
- `---ldk-peer-listening-port` määrab, millist Lightning p2p porti kuulata;
- `dataldk0/`, `dataldk1/` on salvestuskataloogide teekonnad (iga sõlmpunkt salvestab oma andmed eraldi).

Saate oma RLN-sõlmede käske käivitada ka brauserist:

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

Selleks, et sõlm saaks avada kanali, peab tal kõigepealt olema bitcoine aadressil, mis on loodud järgmise käsuga (näiteks sõlme nr 1 jaoks):

```bash
curl -X POST http://localhost:3001/address
```

Vastus annab teile aadressi.

![RGB-Bitcoin](assets/fr/103.webp)

"Bitcoind"-reeglites kaevandame mõned bitcoinid. Käivita :

```bash
./regtest.sh mine 101
```

![RGB-Bitcoin](assets/fr/104.webp)

Saatke raha eespool loodud sõlme aadressile:

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RGB-Bitcoin](assets/fr/105.webp)

Seejärel kaevandage plokk tehingu kinnitamiseks:

```bash
./regtest.sh mine 1
```

![RGB-Bitcoin](assets/fr/106.webp)

### Testneti käivitamine (ilma Dockerita)

Kui soovite testida realistlikumat stsenaariumi, võite käivitada 3 RLN-sõlme Testnetis, mitte Regtestis, mis osutavad avalikele teenustele :

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

Vaikimisi, kui konfiguratsiooni ei leita, proovib deemon kasutada :


- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- "bitcoind_rpc_port": "18332"
- indexer_url`: `ssl://electrum.iriswallet.com:50013`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`

Sisselogimisega :


- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`

Neid elemente saab kohandada ka `init`/`unlock` API kaudu.

### RGB-märkide väljastamine

Tokeni väljastamiseks alustame "värvitavate" UTXOde loomisest:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```

![RGB-Bitcoin](assets/fr/107.webp)

Loomulikult saate järjekorda kohandada. Tehingu kinnitamiseks kaevandame :

```bash
./regtest.sh mine 1
```

Nüüd saame luua RGB vara. Käsk sõltub sellest, millist tüüpi vara soovite luua ja millised on selle parameetrid. Siinkohal loome NIA (*Non Inflatable Asset*) tokeni nimega "PBN", mille varu on 1000 ühikut. `precision` võimaldab teil määrata ühikute jagatavuse.

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```

![RGB-Bitcoin](assets/fr/108.webp)

Vastus sisaldab äsja loodud vara ID-d. Ärge unustage seda identifikaatorit. Minu puhul on see :

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RGB-Bitcoin](assets/fr/109.webp)

Seejärel saate selle üle kanda ahelas või eraldada selle Lightning-kanalis. Just seda teeme järgmises jaotises.

### Kanali avamine ja RGB-vara ülekandmine

Kõigepealt peate oma sõlme ühendama Lightning-võrgus oleva partneriga, kasutades käsku `/connectpeer`. Minu näites juhin ma mõlemat sõlme. Nii et ma hangin oma teise Lightning-sõlme avaliku võtme selle käsuga:

```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```

Käsk tagastab minu sõlme nr 2 avaliku võtme:

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RGB-Bitcoin](assets/fr/110.webp)

Järgmisena avame kanali, määrates vastava vara (`PBN`). Käsk `/openchannel` võimaldab määrata kanali suuruse satoshis ja valida, kas lisada RGB-vara. See sõltub sellest, mida soovite luua, kuid minu puhul on käsk :

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```

Lisateavet leiate siit:


- `peer_pubkey_and_opt_addr`: Selle partneri identifikaator, kellega soovime ühendust luua (avalik võti, mille leidsime varem);
- `capacity_sat`: Kanali koguvõimsus satelliidides ;
- `push_msat`: Kogus millisatossides, mis kanali avamisel algselt partnerile edastatakse (siinkohal edastan kohe 10 000 sati, et ta saaks hiljem RGB ülekande teha) ;
- "varade summa": Kanalile pühendatavate RGB varade summa ;
- `asset_id` : kanaliga seotud RGB-vara unikaalne identifikaator;
- "avalik": Näitab, kas kanal peaks olema avalikustatud võrgus marsruutimiseks.

![RGB-Bitcoin](assets/fr/111.webp)

Tehingu kinnitamiseks kaevandatakse 6 plokki:

```bash
./regtest.sh mine 6
```

![RGB-Bitcoin](assets/fr/112.webp)

Lightning-kanal on nüüd avatud ja sisaldab ka 500 "PBN"-märki sõlme nr 1 poolel. Kui sõlm nr 2 soovib saada PBN-märke, peab ta looma arve. Seda saab teha järgmiselt:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```

Koos :


- `amt_msat`: Arve summa millisatoosides (vähemalt 3000 sats) ;
- `expiry_sec` : Arve aegumise aeg sekundites ;
- `asset_id` : arvega seotud RGB vara identifikaator ;
- "varade summa": Selle arvega ülekantava RGB vara summa.

Vastuseks saate RGB-arve (nagu eelmistes peatükkides kirjeldatud):

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RGB-Bitcoin](assets/fr/113.webp)

Nüüd maksame selle arve esimesest sõlmest, kus on vajalik raha "PBN" sümboliga:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```

![RGB-Bitcoin](assets/fr/114.webp)

Makse on tehtud. Seda saab kontrollida käsuga :

```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```

![RGB-Bitcoin](assets/fr/115.webp)

Siin on kirjeldatud, kuidas võtta kasutusele Lightning-sõlm, mida on muudetud RGB-vara kandmiseks. See demonstratsioon põhineb :


- Regtest keskkond (läbi `./regtest.sh`) või testnet ;
- Lightning-sõlm (`rgb-lightning-node`), mis põhineb `bitcoind`il, indekseerijal ja `rgb-proxy-server`il;
- JSON REST APId kanalite avamiseks/sulgemiseks, märgiste väljastamiseks, varade ülekandmiseks Lightning'i kaudu jne.

Tänu sellele protsessile :


- Lightning engagement tehingud sisaldavad täiendavat väljundit (OP_RETURN või Taproot) koos RGB ülemineku ankurdamisega;
- Ülekandeid tehakse täpselt samamoodi nagu traditsioonilisi Lightning-makseid, kuid lisaks on lisatud RGB-märk;
- Mitut RLN-sõlme saab ühendada, et suunata ja katsetada makseid mitme sõlme vahel, tingimusel, et teel on piisavalt likviidsust nii bitcoinide kui ka vara RGB osas.

Projekt on endiselt alfa-staadiumis. Seetõttu on tungivalt soovitatav piirduda testkeskkondadega (regtest, testnet).

LN-RGB ühilduvuse poolt avanevad võimalused on märkimisväärsed: stabiilsed mündid Lightningil, DEX layer-2, asendatavate žetoonide või NFT-de ülekandmine väga väikeste kuludega... Eelmistes peatükkides on kirjeldatud kontseptuaalset arhitektuuri ja valideerimisloogikat. Nüüd on teil praktiline ülevaade sellest, kuidas saada selline sõlme üles ja tööle, teie tulevaste arenduste või testide jaoks.

# Kokkuvõte

<partId>b0baebfc-d146-5938-849a-f835fafb386f</partId>


## Arvamused ja hinnangud

<chapterId>0217e8b0-942a-5fee-bd91-9a866551eff3</chapterId>

<isCourseReview>true</isCourseReview>

## Kokkuvõte

<chapterId>0309536d-c336-56a0-869e-a8395ed8d9ae</chapterId>

<isCourseConclusion>true</isCourseConclusion>
