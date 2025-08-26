---
name: IP-võrgud teooriast praktikasse
goal: IP-võrkude põhialuste omandamine, et neid paremini konfigureerida ja tõrkeid kõrvaldada.
objectives: 


  - Mõista TCP/IP-protokolli ülesehitust ja toimimist
  - Selgitage IPv4 ja IPv6 erinevusi, eeliseid ja piiranguid
  - Erinevate IP Address tüüpide tuvastamine ja eristamine
  - IP-aadresside seadistamine ja kontrollimine Unix/Linuxi süsteemides
  - Kasutage peamisi diagnostikavahendeid võrguprobleemide analüüsimiseks ja lahendamiseks


---

# Olulised oskused intellektuaalomandi maailmas navigeerimiseks


Sukeldu IP-maailma südamesse ja varusta end teadmistega, et mõista ja tõhusalt hallata oma võrke. Sellel kursusel õpite kõike, mida peate arvutivõrkude kohta teadma, selgel ja praktilisel viisil.


Te saate teada, kuidas võrgud ja IP-aadressid toimivad, kuidas teha vahet IPv4 ja IPv6 vahel, kuidas tuvastada ja kasutada erinevaid Address kategooriaid ning kuidas mõista TCP/IP-protokolli ja selle abil loodud seoseid IP-aadresside, füüsiliste aadresside ja DNS-nimede vahel.


NET 302 on suunatud peamiselt üliõpilastele, Linuxi kasutajatele või lihtsalt uudishimulikele, kes soovivad mõista võrkude põhitõdesid ja tugevdada oma iseseisvust infrastruktuuride haldamisel, tõrkeotsingul ja optimeerimisel.


Liitu meiega ja muuda oma teadmised tõeliseks operatiivseks ekspertiisiks!


___


See NET 302 kursus on kohandatud kursusest *Võrgu alused: TCP/IP, IPv4 ja IPv6*, mille Philippe Pierre kirjutas prantsuse keeles ja avaldas [IT-Connect](https://www.it-connect.fr/cours/les-bases-du-reseau-tcpip-ipv4-et-ipv6/) lehel, litsentsi Creative Commons Attribution-NonCommercial 4.0 International ([CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)) alusel.



Loïc Moreli originaalversioonis on tehtud olulisi muudatusi: tekst on täielikult ümber kirjutatud, laiendatud ja rikastatud, et pakkuda ajakohastatud ja põhjalikku sisu, säilitades samal ajal Philippe Pierre'i algse teose hariva vaimu. Ka diagrammid on üle vaadatud.


+++


# Sissejuhatus


<partId>a52b996d-1e23-470f-a9df-7ad88790099a</partId>



## Kursuse ülevaade


<chapterId>9f238ecd-c9bb-4886-a205-2beba609fb13</chapterId>


See kursus annab täieliku sissejuhatuse IP-võrkude põhitõdedesse. Kursus on jaotatud nelja põhiosasse, millest igaüks hõlmab arvutivõrgu probleemide mõistmiseks, konfigureerimiseks ja diagnoosimiseks vajalikku aspekti.


### TCP/IP protokoll


Selles esimeses osas paneme aluse, uurides võrkude kontseptsiooni ja TCP/IP-protokolli ajalugu. Uurime selle põhikomponente: IP, TCP ja lühidalt IPv5 QoS-protokolli. Samuti käsitleme teenuse primitiive, et paremini mõista andmete Exchange loogikat.


### IPv4-aadressimine


Seejärel liigume edasi IPv4-aadressimisele pühendatud mooduli juurde. Saate teada, kuidas IPv4-i praktikas kasutatakse, selle erinevaid Address tüüpe (privaatne, avalik, ringhääling jne), DNS-i põhilist rolli, samuti seda, kuidas töötavad Ethernet-aadressid ja ARP-protokoll. Samuti avastate NAT-i (Network Address Translation) ja võrgu konfigureerimise põhitõed.


### IPv6-aadressimine


Kolmandas osas keskendutakse IPv6-aadressimisele, mis on vajalik IPv4 piirangute Address jaoks. Käime läbi selle standardid ja määratlused, Address Assignment kohalikus võrgus, Address blokihalduse ja IPv6 ja DNS-i vahelise suhte.


### Võrgu diagnostikavahendid


Lõpetuseks tutvustame peamisi võrgudiagnostikavahendeid. Need võimaldavad teil analüüsida, kontrollida ja tõrkeid kõrvaldada. See osa on struktureeritud kihtide kaupa: Võrgule juurdepääs, võrk, transport ja ülemine kiht.


Selle kursuse lõpuks on teil põhiteadmised võrguinfrastruktuuri tõhusaks haldamiseks ja võimalike probleemide diagnoosimiseks.


Kas olete valmis sukelduma arvutivõrkude maailma? Läheme!


**MÄRKUS**: Kirjeldused põhinevad GNU/Linux CentOS 7 süsteemil. Siiski on võrgukonfiguratsioonid suures osas samad, kui võrrelda Debiani ja CentOS süsteemi. Seega ei tee me mingit vahet. Kui see on olemas, siis lisame sellele konkreetse logo.


**N.B.**: Kui kursuse käigus satute mõne tundmatu terminiga kokku, vaadake [sõnastikust] (https://planb.network/resources/glossary), et leida mõisted.



# TCP/IP-protokollid


<partId>53fd4b73-cdf1-4865-ba29-1ac8ec3e9e9a</partId>



## Mis on võrgustik?


<chapterId>7370904f-f8f5-4ad4-a63a-5931d94c3b3b</chapterId>



Selles esimeses moodulis tutvume põhjalikult TCP/IP-protokolliga, mis on kaasaegse digitaalse side nurgakivi. Arutame selle päritolu, selle aluspõhimõtteid ja selles kasutatavat adresseerimissüsteemi, mis on oluline ühendatud seadmete vahelise teabevahetuse tagamiseks.


Samuti tutvustame üksikasjalikult peamisi komponente, mis seda mudelit struktureerivad, ja selgitame, kuidas need omavahel koostoimivad, et moodustada toimiv, usaldusväärne ja skaleeritav võrk. Kuid kõigepealt on oluline minna tagasi võrgu mõiste juurde.


Etümoloogiliselt tähendab võrk üksteisega seotud punktide kogumit, mis moodustavad omavahel seotud struktuuri. Telekommunikatsiooni ja arvutite puhul tähendab see määratlus seadmete rühma (arvutid, marsruuterid, kommutaatorid, juurdepääsupunktid jne), mis on võimelised füüsilise või traadita andmekandja kaudu andmeid vahetama. Seega võimaldab võrk pidevat või katkendlikku teabevahetust, sõltuvalt nõuetest, kasutatavatest protokollidest ja kasutatava arhitektuuri iseloomust.


Aja jooksul on välja töötatud mitmeid klassikalisi topoloogiaid, mis vastavad erinevatele vajadustele seoses kulude, jõudluse, vastupidavuse ja hooldusmugavusega. Nende hulka kuuluvad:


- ringvõrk,
- puiduvõrgustik,
- bussivõrk,
- tähtede võrgustik,
- võrgusilma võrk.



### Ringvõrk


Ringtopoloogias on seadmed ühendatud suletud ringina: iga jaam on ühendatud järgmise jaamaga ning viimane ühendub tagasi esimese jaamaga. Sellise ülesehituse puhul toimib iga seade releena, mis edastab andmeid järgmisele lingile. Sõltuvalt võrgu tüübist võib teave liikuda ainult ühes või mõlemas suunas.


Selle korralduse eelis seisneb lihtsas kaabeldamises ja selles, et ei sõltu ühestki keskseadmest. Kogu võrgu toimimine sõltub siiski iga üksiku elemendi töökindlusest: ühe jaama rike võib katkestada kogu sidesüsteemi. Seepärast on sageli kasutusele võetud redundants või ümbersõidumehhanismid.



![Image](assets/fr/001.webp)



### Puude võrgustik


Puude võrk ehk hierarhiline topoloogia on modelleeritud perekonnapuu struktuuri järgi. See koosneb üksteisele järgnevatest tasanditest: tipus asuv juursõlm ühendab mitu madalama taseme sõlme, mis omakorda võivad ühenduda teiste sõlmedega jne.


Selline hierarhiline ülesehitus sobib eriti hästi suurte võrkude puhul, mis vajavad selget vastutuse jaotust ja segmenteeritud juhtimist. Samas muudab see võrgu haavatavaks ka kõrgemate sõlmede rikke suhtes: juur- või peaharu kaotamine võib katkestada terve infrastruktuuri osa.



![Image](assets/fr/002.webp)



### Bussivõrk


Bussitopoloogias kasutavad kõik seadmed sama ülekandevahendit, tavaliselt koaksiaalliini või optilist kiudu. Iga seade on passiivselt ühendatud, mis tähendab, et ta ei muuda aktiivselt signaali ja saab selle ühise kanali kaudu andmeid saata või vastu võtta.


Bussitopoloogia peamine eelis on madalad paigalduskulud tänu lihtsustatud kaabeldamisele.  Vanemates koaksiaalpõhistes rakendustes (Ethernet 10BASE2/10BASE5) võis aga ühe jaama lahtiühendamine või kaotamine häirida või isegi peatada kogu liikluse, kuna elektriline pidevus ja lõpetamise impedants ei oleks enam säilinud. Ühe füüsilise andmekandja olemasolu on samuti kriitiline nõrkus: iga katkestus või rike peatab kogu võrgu side.



![Image](assets/fr/003.webp)



### Tähtede võrgustik


Täht-topoloogia, mida tuntakse ka kui "hub and spoke", on tänapäeval kõige levinum, eriti kodu- ja kontorivõrkudes. Siin on kõik seadmed ühendatud ühe keskseadmega.


Selline paigutus muudab haldamise ja hoolduse lihtsaks: kui üks välisseade läheb rikki, ei mõjuta see ülejäänud võrku. Miinuseks on see, et keskseade on üks veapunkt: kui see läheb katki, lakkab side kõikjal. Hea jõudluse säilitamiseks tuleb hoolikalt kaaluda ka kaabli kvaliteeti ja ühenduste pikkust.



![Image](assets/fr/004.webp)



**Märkus**: on veel võrke, mis on korraldatud lineaarses, bussilaadses topoloogias, kus seadmed on ühendatud üksteise järel. Selle lahenduse, mida on küll odav kasutada, peamine puudus on see, et üks katkestus isoleerib osa hostidest, jagades võrgu sõltumatuteks alamrühmadeks.


### Võrgustik


Võrguvõrk on kavandatud maksimaalse redundantsi saavutamiseks: iga seade on otse ühendatud iga teise seadmega. See tagab teenuse järjepidevuse isegi siis, kui mitu linki või seadet ebaõnnestuvad, sest liiklust saab ümber suunata alternatiivseid teid mööda.


Kompromissiks on see, et loodavate ühenduste arv suureneb kiiresti koos terminalide arvuga. N ühenduspunkti puhul on vaja N × (N-1) / 2 eraldi linki, mis muudab selle topoloogia kasutuselevõtu kalliks ja keeruliseks. Seetõttu kasutatakse seda peamiselt kriitilistes võrkudes, mis nõuavad väga kõrget kättesaadavust, näiteks Interneti teatud osad või tundlikud tööstussüsteemid.



![Image](assets/fr/005.webp)



On olemas ka teisi variante, näiteks grid- või hüperkuubikuvõrgud, mis on mõeldud hajutatud arvutuste või paralleelarvutuse erivajaduste rahuldamiseks.


Ülemaailmselt on Internet mitmesuguseid topoloogiaid kasutavate võrkude massiline ühendus, mida ühendab ühine adresseerimine (IPv4 ja IPv6) ja IETF (*Internet Engineering Task Force*) poolt määratletud standardiseeritud protokollide kogum. Selline mitmekesisus tähendab, et Internet ei järgi ühte topoloogiat: selle struktuur on paindlik, skaleeritav ja sõltumatu loogilisest adresseerimisskeemist, mis muudab selle kasutatavaks.



## TCP/IP päritolu


<chapterId>266b6864-8789-48d7-bc85-001cb9f1651f</chapterId>



TCP-protokolli algupära on **ARPA** (*Advanced Research Projects Agency*, mis 1972. aastal nimetati ümber DARPAks), mis käivitas 1966. aastal projekti **ARPANET**. Esimene ARPANETi segment käivitus 1969. aasta oktoobris, ühendades UCLA ja Stanfordi ülikoolid. Eesmärgiks oli ühendada teaduskeskused pakettkommuteeritud võrgu kaudu, mis suudaks sidet pidada isegi infrastruktuuri osalise rikke korral.


Selle dünaamika raames rahastas ARPA Berkeley ülikooli, et integreerida esimesed TCP/IP-protokollid BSD Unix-süsteemi. See mängis olulist rolli protokolli levitamisel ja standardiseerimisel, kõigepealt akadeemilises maailmas ja hiljem tööstuses.


**Märkus**: sel ajal ei olnud arvutiteadlastel veel Linuxi (mis ilmus alles 1990ndate alguses) ega Andrew Tanenbaumi loodud haridussüsteemi Minixi.  Peamised valikud olid Unix või mõnikord patenteeritud suurarvutid nagu OpenVMS. Tänu oma paindlikkusele ja avatusele oli Unixil oluline roll esimeste võrgukontseptsioonide levitamisel.


Rangelt võttes ei ole TCP/IP mitte üks protokoll, vaid TCP ja IP ümber ehitatud protokollide kogum. See saavutas tuntuse, sest see pakkus standardiseeritud programmeerimis Interface andmevahetuseks masinate vahel samas võrgus. See Interface, mis põhineb "socketideks" nimetatud primitiividel, võimaldas luua usaldusväärseid ja paindlikke ühendusi, integreerides samal ajal olulisi rakendusprotokolle.


ARPANET on seega tänase Interneti ajalooline alus. Internet on tõepoolest pakettkommuteerimise põhimõttel põhinev ülemaailmne võrk, kus teave liigub standardiseeritud protokollide abil, mis tagavad heterogeensete süsteemide ühilduvuse ja koostalitlusvõime. See avatud arhitektuur on võimaldanud arendada ja kasutusele võtta lugematuid teenuseid ja rakendusi, sealhulgas:


- e-kirjad,
- world Wide Web (www),
- failide edastamine ja jagamine...


Nende protokollide juhtimist ja arengut jälgib ***Internet Architecture Board*** (IAB).

See organisatsioon koordineerib tehnilisi suundumusi kahe peamise struktuuri kaudu:


- IRTF** (_Internet Research Task Force_), mis viib läbi pikaajalisi uuringuid protokollide arengu ja täiustamise kohta.
- IETF** (_Internet Engineering Task Force_), mis töötab välja, standardiseerib ja dokumenteerib Internetis kasutatavad tööprotokollid


Võrguressursside (IP Address vahemikud, autonoomsete süsteemide numbrid, juurdomeeninimed jne) jaotamist koordineerib rahvusvaheliselt **IANA/ICANN**. Operatiivne juhtimine tugineb: **RIR** (*Regional Internet Registries*): **RIPE NCC** (Euroopa, Lähis-Ida, Kesk-Aasia), **ARIN**, **APNIC**, **LACNIC** ja **AFRINIC**.


Kõik TCP/IP-protokollide spetsifikatsioonid on salvestatud dokumentides, mida nimetatakse **RFC** (_Request For Comments_), mis on autoriteetsed tehnilised viited. RFC-d ajakohastatakse ja nummerdatakse pidevalt, et kajastada protokollide jätkuvat arengut.


TCP/IP virna kujutatakse sageli neljast funktsionaalsest kihist koosneva virna, mida sageli võrreldakse **ISO** (_International Standards Organization_) poolt välja töötatud seitsme Layer **OSI** (_Open Systems Interconnection_) mudeliga, mis on võrkude kontseptuaalne võrdlusalus.


TCP/IP mudeli neli kihti on järgmised:


- nETWORK ACCESS Layer, mis pakub füüsilise ühenduse ja meediapääsu kontrolliprotokolle;
- iNTERNET Layer, mis tegeleb marsruutimise ja IP-aadressimisega;
- tRANSPORT Layer, mis tagab andmevoogude usaldusväärsuse ja haldamise, kasutades selliseid protokolle nagu TCP või UDP ;
- aPPLICATION Layer, mis koondab kasutaja- ja tarkvaraprotokolle, nagu HTTP, FTP, SMTP ja DNS.



![Image](assets/fr/006.webp)



Tänapäeval on kõige laialdasemalt kasutatav IP-versioon IPv4, kuid selle 32-bitine Address ruum on selgelt piiratud. See tõi kaasa IPv6 loomise, mis kasutab 128-bitist adresseerimist ja pakub praktiliselt piiramatut võimsust: see on oluline ühendatud seadmete plahvatusliku kasvu toetamiseks ja asjade interneti, liikuvuse ja turvalisuse väljakutsetele vastamiseks.


Iga TCP/IP virna Layer pakub konkreetseid teenuseid, võimaldades Address erinevaid võrguvajadusi moodulitena: füüsiline edastamine, loogiline adresseerimine, andmete terviklikkus ja rakendustasandi teenused.


| Device example    | Description                                                                               | 	TCP/IP layer |
| ---------------------- | ----------------------------------------------------------------------------------------- | ----------------------- |
| Web server            | Application services closest to end users                                      | Application             |
| Gateway or proxy    | 	Encodes, encrypts, compresses useful data                                              | Application             |
| Session switch | Establishes sessions between applications                                               | Application             |
| Firewall or L4 router | Establishes, maintains, and terminates sessions between endpoint devices                  | Transport               |
| Router                | Globally addresses interfaces and determines optimal paths through a network | Network                  |
| Switch   | Locally addresses interfaces and forwards traffic via MAC                            | Network Access         |
| Network Interface Card (NIC)     | Signal encoding, cabling, connectors, physical specifications                        | Network Access         |

https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864

## IPv5 QoS protokoll


<chapterId>570ded19-be61-4005-844e-9490570a6455</chapterId>



IP-paketi päis on oluline andmestruktuur, mis on jagatud mitmeks väljaks, millest igaühel on konkreetne roll, et tagada pakettide edastamine ja korrektne töötlemine nende liikumisel läbi võrgu. Need väljad hõlmavad siht-IP Address (mis on vajalik paketi suunamiseks ettenähtud vastuvõtjani), IHL (*Internet Header Length*) väljal märgitud päise pikkust, *Total Length väljal* märgitud paketi kogupikkust, kontrolli- ja kontrollteavet ning muid parameetreid sidevoo ja kvaliteedi juhtimiseks.


Kõige esimene väli päises kannab nime Version. See 4-bitine väärtus määrab, millise IP-protokolli versiooni järgi pakett on. See on oluline, sest see ütleb igale marsruuterile või vahepealsele seadmele, kuidas tõlgendada ja käsitleda kapseldatud andmeid.


**Märkus**: IP-protokollide versioonide haldamise ja määramise eest vastutab **IANA**. 4-bitine väli võimaldab 16 binaarset kombinatsiooni (väärtused 0 kuni 15). Tänaseks on nende jaotus järgmine:



| Version Number | Protocol   | Version Description         | Reference               |
| -------------- | ---------- | --------------------------- | ----------------------- |
| 0–1            | Reserved   | Reserved                    |                         |
| 2–3            | Unassigned | Unassigned                  |                         |
| 4              | IP         | Internet Protocol           | RFC 791                 |
| **5**          | **ST**     | **ST Datagram mode**        | **RFC 1190** / RFC 1819 |
| 6              | IPv6       | Internet Protocol version 6 | RFC 8200                |
| 7              | TP/IX      | The Next Internet           | RFC 1475                |
| 8              | PIP        | The P Internet Protocol     | RFC 1621                |
| 9              | TUBA       | Tuba                        | RFC 1347                |
| 10–14          | Unassigned | Unassigned                  |                         |
| 15             | Reserved   | Reserved                    |                         |

Nende hulgas on IPv5, mis on küll avalikkusele suuresti tundmatu, kuid mis oli olemas ST (_Stream Protocol_) nime all. IPv5 töötati välja 1980ndatel aastatel, et tagada "teenuse kvaliteet" (QoS) teatud andmevoogude jaoks, mis nõudsid pidevat ja stabiilset edastamist, näiteks Voice over IP või multimeediavoogude jaoks. Selle eesmärk oli tagada otsest ribalaiust ja prioriteetsust, mis on sarnane kontseptsiooniga, mida RSVP (_Resource Reservation Protocol_) pakub tänapäeval võrguressursside dünaamiliseks reserveerimiseks kaasaegsetes ruuterites.


IPv5 jäi siiski eksperimentaalseks ja seda rakendati vaid vähestes võrguseadmetes. Selle piiratud kasutuselevõtt koos kiiresti kasvava vajadusega suurema Address ruumi järele sundis Interneti projekteerijaid otse IPv4-lt IPv6-le üle minema. Sellega välditi nii IPv4 Address piiranguid kui ka segaduse või ühildamatuse ohtu IPv5 eksperimentaalsete spetsifikatsioonidega.


Kuigi IPv5 ei leidnud kunagi laialdast kasutamist, mängis see olulist rolli QoSi ja andmevoogude haldamise alase mõtteviisi kujundamisel. Tänapäeval on see pigem ajalooline tähis kui toimiv standard.


**Mälu** - Protokoll on kommunikatsioonireeglite kogum: andmestruktuurid, algoritmid, pakettide vormingud ja konventsioonid, mis võimaldavad erinevatel seadmetel Exchange teavet usaldusväärselt ja arusaadavalt edastada. Teenus on protokolli konkreetne rakendamine konkreetsete programmide (kliendid, serverid) kaudu, mis järgivad neid reegleid ja teevad funktsionaalsuse kasutajatele ja rakendustele kättesaadavaks.


Nüüd saame lähemalt uurida IP-protokolli, mis on kogu võrguside oluline alus, ülesehitust ja toimimist.



## IP-protokoll


<chapterId>758fddbd-b652-4c18-bd1e-d038bd2e4d05</chapterId>



### Mõisted ja üldine teave


IP-protokoll ehk "***Internetprotokoll***" on TCP/IP-mudeli selgroog. See edastab andmepakette ühest hostist teise võrgus, olgu see siis kohalik või üle maailma ulatuv. Sellel on kaks võtmerolli: seadmete loogilise adresseerimise haldamine ja pakettide suunamine sageli heterogeensetes ja omavahel ühendatud võrkudes.


Füüsilisel tasandil tugineb andmeedastus riistvaraliideseile, et luua sõlmede vahel punkt-punkt ühendused. IP-protokoll teeb aga võimalikuks otseteedevahelise side, andes igale paketile vajalikku teavet, et liikuda läbi mitme võimaliku tee sihtkohta.


Kolm võrgukonfiguratsiooni Elements määravad, kuidas pakett oma teele saadetakse:


- IP Address**: identifitseerib üheselt sihtkoha võrgus.
- Subnet mask**: määrab kindlaks, milline osa Address tähistab võrku ja milline osa hostit, võimaldades loogilist jaotust alamvõrkudeks.
- Värav**: näitab vahepealset marsruuterit, mida pakett peaks läbima, et jõuda välisvõrku või kohaliku võrgu teise segmenti.


Internetis ei liigu andmed ühe pideva andmevooluna, vaid neid saadetakse **datagrammidena**: iseseisvad andmeplokid, millest igaüks on kapseldatud kogu edastamiseks vajaliku teabega. See on **pakettide vahetamise** põhimõte, kus teave jagatakse iseseisvateks ühikuteks, mis võivad jõuda samale vastuvõtjale eri teid pidi.


Lisaks kasulikule koormusele (*maksekoormus*) sisaldab iga IP-andmesõnum struktureeritud päistekirje, mis sisaldab selliseid välju nagu siht-Address, lähte-Address, teenuse tüüp, protokolli versiooni number ja muud edastamise haldamiseks vajalikku kontrollteavet.


IP-andmeside teoreetiline maksimaalne suurus on **65 536 oktetti**, mis on määratud päise kogupikkuse väljaga. Praktikas saavutatakse seda suurust harva, kuna pakette edastavad füüsilised võrgud (Ethernet, Wi-Fi, valguskaabel...) kehtestavad tavaliselt rangemad piirid, mida tuntakse kui **MTU** (_Maximum Transmission Unit_). Kui datagramm ületab füüsilise ühenduse MTU, tuleb see jagada väiksemateks pakettideks, mis saadetakse eraldi ja mis saabumisel uuesti kokku pandud.


Selline kohanemisvõime muudab IP-protokolli töökindlaks ja paindlikuks, mis on võimeline töötama mitmesuguste aluseks olevate tehnoloogiate kaudu, säilitades samas universaalse ühilduvuse heterogeensete süsteemide ja võrkude vahel.



### IP-andmesõnumite killustamine


Kui IP-andmeside peab läbima võrku, mille ülekandevõimsus on väiksem kui andmeside ise, tuleb see **pragmenteerida**, et see saaks probleemideta liikuda. Seda füüsilise suuruse piirangut nimetatakse **MTU** (Maximum Transmission Unit): suurim kaadri suurus, mis saab läbida antud võrku ilma jagamata.


Iga võrgutehnoloogia kehtestab oma MTU, mis määratakse kindlaks riistvara ja protokolli omaduste alusel. Üldised väärtused on järgmised:


- ARPANET**: 1000 baiti
- Ethernet**: 1500 baiti
- FDDI**: 4470 baiti


Kui datagramm ületab võrgusegmendi MTU-d, mida ta peab ületama, jagavad marsruutimisseadmed selle väiksemateks **fragmentideks**, mis vastavad piirangule. See juhtub tavaliselt siis, kui liigutakse suure MTU-ga võrgust väiksema läbilaskevõimega võrku. Näiteks võib FDDI-võrgust tulev datagramm olla vaja enne Ethernet-segmendi kaudu saatmist killustada.



![Image](assets/fr/008.webp)



Fragmenteerimisprotsess toimib järgmiselt:


- Marsruuter jaotab datagrammi fragmentideks, mis ei ole suuremad kui sihtvõrgu MTU.
- Iga fragmendi suurus on 8 baidi kordne, kuna IP-protokoll kasutab seda ühikut uuesti kokkupaneku nihke kodeerimiseks.
- Iga fragment saab oma IP-pealkirja, mis sisaldab teavet, mida lõplik vastuvõtja vajab nende õiges järjekorras uuesti kokku panemiseks.


Pärast killustamist liiguvad tükid iseseisvalt läbi võrgu. Nad võivad kasutada erinevaid marsruute, sõltuvalt marsruutimistabelitest, linkide koormusest või katkestustest. Ei ole mingit garantiid, et nad jõuavad kohale samas järjekorras, nagu nad on saadetud.


Saabumisel tegeleb vastuvõtumasin **tagasi kokkupanemisega**. Kasutades päises sisalduvat teavet (jagatud identifikaator, nihke ja fragmenteerimisliigid), paneb ta fragmendid õiges järjekorras tagasi, et taastada esialgne datagramm enne selle edastamist järgmisele Layer-le. Kui isegi üks fragment on kadunud või vigastatud, visatakse tavaliselt kogu datagramm ära, sest ilma iga tükita oleks tulemus ebatäielik või kasutuskõlbmatu.


Kuigi killustamisel ja taasühendamisel on omad puudused: lisatöötlus marsruuterite ja hostide jaoks ning suurem võimalus pakettide kadumiseks, mis võib suurendada uuesti edastamist. Seepärast on sujuvaks ja tõhusaks IP-suhtluseks oluline hoolikas MTU-haldus ja pakettide suuruse optimeerimine.



### Andmete kapseldamine


Selleks, et tagada andmete korrektne suunamine läbi TCP/IP mudeli kihtide, on võtmeroll **kapseldamisel**. Igas etapis, kui sõnum liigub saatja rakendusest vastuvõtja masinasse, lisatakse lisateavet, mida nimetatakse päisteks. Need päised annavad vahepealsetele seadmetele ja tarkvarakihtidele juhised, mida nad vajavad andmete töötlemiseks, edastamiseks ja vajaduse korral uuesti kokku panemiseks.


Kui sõnum saadetakse, läbib see TCP/IP korstna neli kihti. Iga Layer puhul lisatakse olemasolevatele andmetele uus päis: iga päis sisaldab konkreetseid metaandmeid, näiteks loogilisi või füüsilisi aadresse, sideporti, järjestusnumbreid, veakontrolli lipukesi ja mis tahes teavet, mis on vajalik edastamise ja marsruutimise haldamiseks.


Seega järgib edastamine struktureeritud protsessi:


- Application Layer loob esialgse **sõnumi**, mis sisaldab algandmeid.
- Transport Layer kapseldab selle **segmendiks**, lisades lähte- ja sihtportid, järjestusnumbrid ja voojuhtimismehhanismid.
- Internet Layer lisab segmendile IP-pealkirja, et moodustada **datagramm**, milles on määratud lähte- ja siht-IP-aadressid.
- Network Access Layer pakib datagrammi **kaadrisse**, lisades MAC-aadressid ja terviklikkuse kontrollkoodid (CRC).



![Image](assets/fr/009.webp)



Selline kapseldamisprotsess tagab nii andmete terviklikkuse ja jälgitavuse kui ka nende kohandatavuse: ühest võrgust teise liikumisel annavad päised seadmetele vajalikku teavet marsruudi valimiseks, kehtivuse kontrollimiseks või vajaduse korral fragmenteerimiseks.


Saabumisel toimub protsess vastupidi: vastuvõttev masin saab kaadri võrgujuurdepääsu Layer-s, mis loeb ja eemaldab vastava päise. Seejärel edastatakse datagramm Interneti Layer-le, mis loeb IP-pealkirja ja eemaldab selle omakorda, et edastada segment transpordivõrgu Layer-le. Transpordi Layer töötleb transpordi päiseid, kontrollib voo terviklikkust ja lõpuks edastab **sõnumi** sihtrakendusele algses olekus.



![Image](assets/fr/010.webp)



Andmete muundamise iga Layer puhul võib kokku võtta järgmiselt:


- Teade**: infoblokk Application Layer.
- Segment**: andmeühik pärast kapseldamist Transport Layer poolt.
- Datagramm**: vorm, mis võetakse pärast IP-pealkirja lisamist Interneti Layer poolt.
- Kaader**: lõplik plokk, mis on valmis võrguühendus Layer poolt füüsilise andmekandja kaudu edastamiseks.



![Image](assets/fr/011.webp)



See protsess, mis on oluline Interneti-side usaldusväärsuse ja universaalsuse jaoks, tagab, et iga andmestik, ükskõik kui killustatud või keeruline see ka poleks, saab edastada otsast lõpuni, jäädes samas vastuvõtva masina jaoks arusaadavaks ja kasutatavaks.



### IP-aadressimine


Isegi kui pakettkommuteerimine, fragmenteerimine ja kapseldamine on olemas, ei saa võrk ikkagi toimida ilma usaldusväärse aadressisüsteemita. Et tagada, et iga andmepakett jõuab õigesse vastuvõtjasse, kasutab Internet Layer unikaalset identifikaatorit: **IP Address**.

IPv4-s on IP Address kodeeritud **32 bitti** ja kirjutatud nelja punktidega eraldatud kümnendnumbrina tuttavas N1.N2.N3.N4-vormingus (näiteks: 192.168.1.12).


IP Address koosneb kahest osast:


- _netid_**: identifitseerib võrgu, millesse host kuulub
- _hostid_**: identifitseerib konkreetse hosti kõnealuses võrgus

Selline eraldamine võimaldab globaalset Internetti loogiliselt struktureerida paljudeks omavahel ühendatud võrkudeks.


Ajalooliselt tugines IPv4-süsteem klassipõhisele skeemile, mis oli tähistatud A-st E-sse, mis määratles Address vahemiku ja nende kasutusotstarbe. Iga klass määras kindla arvu bite _netid_ ja _hostid_ jaoks, mis mõjutas otseselt võimalike võrkude ja hostide arvu.



| **Class** | **IPv4 Address Range**            | **Usage**                    |
| --------- | --------------------------------- | ---------------------------- |
| A         | 1.x.x.x to 126.x.x.x              | Unicast addresses            |
|           | (127.x.x.x reserved for loopback) | Local loopback               |
| B         | 128.0.x.x to 191.255.x.x          | Unicast addresses            |
| C         | 192.0.0.x to 223.255.255.x        | Unicast addresses            |
| D         | 224.0.0.0 to 239.255.255.255      | IP Multicast                 |
| E         | 240.0.0.0 to 255.255.255.255      | Reserved for experimentation |

Kõiki võimalikke väärtusi ei saa määrata hostidele. Näiteks **klassi C** Address puhul pakub viimane bait 8 bitti (256 väärtust). Kuid kaks neist on reserveeritud:


- 0: identifitseerib võrgu enda
- 255: on **broadcast** Address, mida kasutatakse paketi saatmiseks kõigile võrgus asuvatele hostidele korraga.

Seega jääb 254 kasutatavat aadressi seadmete jaoks.


Saadaolevate aadresside arv on klassiti väga erinev: alates suurtest avalikest võrkudest klassis A, kuni ettevõtete võrkudeni klassis B ja väiksemate kohalike võrkudeni klassis C.



![Image](assets/fr/013.webp)



Mõned Address vahemikud on reserveeritud isiklikuks kasutamiseks ja neid ei suunata kunagi otse Internetti. Neid nimetatakse **privaataadressideks** ja neid kasutatakse organisatsioonide, ettevõtete või kodude sees ning need vajavad Address tõlget, tavaliselt NAT-i (*Network Address Translation*), et jõuda avalikku Internetti. Need on järgmised:


- Klass A**: 10.0.0.0 kuni 10.255.255.255.255
- B-klass**: 172.16.0.0 kuni 172.31.255.255
- Klass C**: 192.168.0.0 kuni 192.168.255.255


Kui seade, millel on privaatne Address, siseneb internetti, asendab NAT-toega ruuter või värav selle kehtiva avaliku Address-ga.


Näide: Kui hostil on Address **192.168.7.5**, saame sellest järeldada:


- 192.168.7.0: võrk Address
- 192.168.7.1: sageli kohalik marsruuter
- 192.168.7.5: vastuvõtja ise


Teine erijuhtum on **127.0.0.1**, mida tuntakse kui "***loopback***".

Linuxi süsteemides on see seotud Interface **lo**. See Address võimaldab masinal Address ise kohalikuks testimiseks või diagnostikaks kasutada, ilma et ta peaks läbima füüsilist Interface. Selleks on reserveeritud kogu vahemik **127.0.0.0/8**.


Address kasutamise optimeerimiseks ja keerukate võrkude projekteerimiseks on **subnetmask** (_netmask_) väga oluline. See binaarmask eraldab _netid_ ja _hostid_ IP Addresss.

Igal klassil on vaikimisi mask:


- 255.0,0,0** A-klassi puhul,
- 255.255.0.0** B-klassi puhul,
- 255.255.255.0** C-klassi puhul.


Hea võrgukujundus järgib põhireeglit: seadmed, mis peavad otseselt suhtlema, peaksid olema samas võrgus või alamvõrgus. Võrgu segmenteerimiseks kasutame alamvõrku, jagades võrgu väiksemateks alamvõrkudeks, kasutades spetsiifilisemat maski.


Alamvõrkude loomise näide:

**Klassi C** võrk: 192.168.1.0/24 vaikimisi maskiga 255.255.255.255.0.

Soovime 4 alamvõrku, millest igaühes on kuni 60 hosti.


**Samm 1**: Vajalike aadresside arv alamvõrgu kohta = 60 + 2 reserveeritud aadressi (võrk + ringhääling) = 62.


**Samm 2**: Leia lähim võimsus 2 ≥ 62. -> 2⁶ = 64.


**Samm 3: Reguleeri mask. Hoidke _netid_ bitid ja reserveerige vajalikud _hostid_ bitid. Saame binaarse maski, mis pärast teisendamist annab **255.255.255.255.192**.


```
11111111 11111111 11111111 11000000
```


**Samm 4**: Arvutage Address vahemikud iga alamvõrgu jaoks, muutes hostile reserveeritud bitid.



| Subnet ID (bits) | Subnet Address   | Subnet Mask     | Address Range                 | Broadcast Address |
| ---------------- | ---------------- | --------------- | ----------------------------- | ----------------- |
| 00               | 192.168.1.0/26   | 255.255.255.192 | 192.168.1.1 – 192.168.1.62    | 192.168.1.63      |
| 01               | 192.168.1.64/26  | 255.255.255.192 | 192.168.1.65 – 192.168.1.126  | 192.168.1.127     |
| 10               | 192.168.1.128/26 | 255.255.255.192 | 192.168.1.129 – 192.168.1.190 | 192.168.1.191     |
| 11               | 192.168.1.192/26 | 255.255.255.192 | 192.168.1.193 – 192.168.1.254 | 192.168.1.255     |


**Samm 5**: See loob neli alamvõrku, millest igaüks toetab kuni 62 masinat, säilitades samal ajal üldise adresseerimisskeemi tõhususe. _hostid_ osa jagatakse _subnetid_ osaks ja hostide osaks.



![Image](assets/fr/016.webp)



See alajaotuse aluspõhimõte on tänapäeva võrgutehnikas endiselt hädavajalik, võimaldades täpset IP-ühendust, paremat liiklusjuhtimist, tugevat segmentide eraldamist ja skaleeritavat võrguhaldust.



### CIDR-aadressimine


1990ndate alguses, kui Internet levis kiiresti ettevõtetes ja organisatsioonides, hakkas traditsiooniline IP-aadresside süsteem, mis põhines klassidel (A, B, C), oma piire näitama.

Selle jäik struktuur tõi kaasa märkimisväärse IP-aadresside raiskamise ning muutis marsruutimistabelid üha suuremaks, keerulisemaks ja raskesti hooldatavaks.

Address nende probleemide lahendamiseks võeti kasutusele paindlikum ja tõhusam meetod: **CIDR** (klassivaba domeenidevaheline marsruutimine). CIDR on järk-järgult muutunud standardiks, asendades suures osas vana klassipõhise süsteemi.


CIDRi põhiidee on võimalus rühmitada mitu kõrvuti asuvat võrku, eriti C-klassi plokke, üheks loogiliseks üksuseks, mida nimetatakse **supernetiks** (_supernet_). Sellise koondamise abil võib üks kirje marsruutimistabelis esindada mitut alamvõrku, vähendades marsruuterite töödeldavate marsruutide arvu ja parandades nende jõudlust.


Kui algselt oli C-klassi võrkudel nende väiksema läbilaskevõime tõttu kõige suurem vajadus koondamise järele, siis seda põhimõtet on rakendatud ka B-klassi ja teoreetiliselt isegi A-klassi võrkudele, kuigi viimased on tänu nende suurele Address levialale vähem mõjutatud.


CIDRi puhul kaob fikseeritud klasside mõiste. Address ruumi käsitletakse pideva vahemikuna, mida saab vastavalt vajadusele jagada või koondada. CIDR-blokid määratletakse alamvõrgumaskide abil, mis ei ole piiratud A-, B- või C-klasside vaikeväärtusega. CIDR-blokk võib esindada kas ühte võrku või ühte ja sama eesliidet jagavate alamvõrkude kokkukuuluvust.


CIDR-blokk kirjutatakse formaadis "Address/prefiks", kus kaldkriipsu järel olev number näitab, mitu bitti moodustab võrguosa. Näiteks /17 tähendab, et esimesed 17 bitti tähistavad võrku, ülejäänud 15 bitti aga hoste.


Näide:

/17 plokk sisaldab 2^(32-17) aadressi, seega 2^15 = 32 768 aadressi kokku. Kui lahutada kaks reserveeritud aadressi (võrgu- ja ringhäälinguaadress), jääb 32 766 kasutatavat hostiaadressi. See võimaldab võrguadministraatoritel oma alamvõrkude suurust täpselt tegelikele vajadustele vastavaks muuta, vältides asjatut raiskamist.


Et CIDRi suuruse määramine oleks lihtsamini arusaadav, on siin tabel tavalistest prefiksitest ja nende vastavatest alamvõrgumaskidest ja kasutatavatest aadressidest:


| CIDR Prefix | Available Host Bits | Subnet Mask     | Usable Host Addresses         |
| ----------- | ------------------- | --------------- | ----------------------------- |
| /8          | 24                  | 255.0.0.0       | 2^24 - 2 = 16,777,214         |
| /12         | 20                  | 255.240.0.0     | 2^20 - 2 = 1,048,574          |
| /16         | 16                  | 255.255.0.0     | 2^16 - 2 = 65,534             |
| /20         | 12                  | 255.255.240.0   | 2^12 - 2 = 4,094              |
| /24         | 8                   | 255.255.255.0   | 2^8 - 2 = 254                 |
| /26         | 6                   | 255.255.255.192 | 2^6 - 2 = 62                  |
| /27         | 5                   | 255.255.255.224 | 2^5 - 2 = 30                  |
| /28         | 4                   | 255.255.255.240 | 2^4 - 2 = 14                  |
| /29         | 3                   | 255.255.255.248 | 2^3 - 2 = 6                   |
| /30         | 2                   | 255.255.255.252 | 2^2 - 2 = 2                   |
| /31         | 1                   | 255.255.255.254 | 2^1 = 2 (point-to-point only) |
| /32         | 0                   | 255.255.255.255 | 1 (host address only)         |


**MÄRKUS**: Ajalooliselt on RFC 950 takistanud alamvõrgu nullmäära kasutamist, peamiselt selleks, et vältida segadust marsruutimisel.  See piirang muutus vananenuks RFC 1878-ga, mis lubab selle kasutamist täielikult. Vana piirang oli peamiselt tingitud vanema riistvara kokkusobimatusest, mis ei suutnud CIDRi korrektselt käsitleda. Kaasaegsetel seadmetel sellist probleemi ei ole.


Näiteks alamvõrk **1.0.0.0.0** koos alammaskiga **255.255.0.0.0**, mis kunagi oli mitmetähenduslik koos A-klassi võrgu identifikaatoriga, on nüüd täiesti kehtiv ja kasutatav.


**TIP**: alamvõrkude vigadeta arvutamiseks ja aadresside kiireks konverteerimiseks CIDR-märgistusse on olemas sellised praktilised vahendid nagu ***ipcalc***. See "võrgukalkulaator" näitab selgelt Address jaotust, olemasolevaid vahemikke ja nendega seotud maske, mis on ideaalne nii administraatoritele kui ka CIDRi õppivatele õpilastele.


```shell
sudo apt install ipcalc
```


https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d

## TCP protokoll


<chapterId>860bf7d5-a502-4d10-a12c-9827f6c2d393</chapterId>



**TCP protokoll** (_Transmission Control Protocol_) mängib keskset rolli TCP/IP mudeli TRANSPORT Layer-s. See toimib sillana rakenduste ja Interneti Layer vahel, tagades usaldusväärse andmeedastuse kahe kaugel asuva masina vahel.

Kui IP-protokoll lihtsalt saadab pakette, tagamata nende kättetoimetamist või järjekorda, siis TCP tagab andmevoo terviklikkuse ja järjepidevuse, edastades selle kadudeta, õiges järjekorras ja ilma duplikaatideta.


TCP peamised ülesanded on järgmised:


- Saadud segmentide ümberjärjestamine;
- Andmevoo jälgimine ummikute vältimiseks;
- Andmeplokkide jagamine või taasühendamine sobivateks ühikuteks (segmentideks);
- Side mõlema otsa vaheliste ühenduste loomise ja lõpetamise haldamine.


TCP on ühendusele orienteeritud protokoll, mis tähendab, et see loob selgesõnalise, pideva suhte kliendi ja serveri vahel. Selleks kasutatakse **järjenumbreid** ja **tunnistusi**: igale saadetud segmendile määratakse unikaalne identifikaator, et vastuvõttev masin saaks kontrollida nii andmete järjekorda kui ka terviklikkust. Seejärel saadab vastuvõtja tagasi kinnitussegmendi, mille **ACK-flipp** on seatud 1, kinnitades vastuvõtmist ja näidates järgmist oodatavat järjekorranumbrit.



![Image](assets/fr/018.webp)



Usaldusväärsuse parandamiseks kasutab TCP taimerit: kui segment on saadetud, algab tagasiarvestus. Kui kinnitust ei saabu aja jooksul, saadab saatja segmendi automaatselt uuesti, eeldades, et see on kadunud teel. See automaatne korduvsaatmismehhanism tasakaalustab IP-võrkudele omaseid kadusid, mis võivad tekkida ülekoormuse, marsruutimisvigade või riistvararikete korral.



![Image](assets/fr/019.webp)



TCP suudab tuvastada ja käsitleda duplikaate. Kui saabub uuesti edastatud segment, kuid ka originaal ilmub, kasutab vastuvõtja järjekorranumbreid duplikaadi tuvastamiseks ja säilitab ainult õige koopia, kõrvaldades igasuguse ebaselguse.


Selleks, et see protsess toimiks, peavad mõlemad masinad mõistma ühiselt oma algseid järjekorranumbreid. See tagatakse range ühendamisprotseduuri järgimisega: ühelt poolt ootab **server** konkreetsel pordil sissetulevat päringut (passiivne režiim); teiselt poolt algatab **klient** aktiivselt ühenduse, saates serverile päringu samal teenindusportil.


**MÄRKUS**: Port on arvutis olevale võrgurakendusele määratud numbriline identifikaator (vahemikus 0-65 535). Seda kasutatakse mitme samal IP Address-l samaaegselt töötava teenuse eristamiseks. Kui klient saadab andmeid, täpsustab ta pordi numbri, et serveri operatsioonisüsteem teaks, milline programm peaks selle vastu võtma (nt 80 HTTP puhul, 443 HTTPS puhul, 25 SMTP puhul). Pordid toimivad nagu spetsiaalsed uksed, mis suunavad liiklust sisse ja välja, takistavad teenuste segiajamist ja võimaldavad peene juurdepääsu kontrolli tulemüüride või filtreerimisreeglite abil.


Järjestuse sünkroniseerimine Exchange põhineb kuulsal **"*kolmesuunalise käepigistuse*"** mehhanismil, mis sarnaneb sellega, kuidas kaks inimest tervitavad teineteist kontakti loomiseks. See initsialiseerimisfaas, mis tagab TCP töökindluse, toimub 3 etapis:

1. **SYN:** Klient saadab esialgse sünkroniseerimissegmendi (**SYN**), mille puhul on seatud vastav lipukene ja esialgne järjekorranumber (nt C);

2. **SYN-ACK:** Vastuvõttev server vastab kinnitussegmendiga (**SYN-ACK**), ta kinnitab kliendi järjenumbri ja annab oma esialgse järjenumbri;

3. **ACK:** Klient saadab lõpliku kinnituse (**ACK**), mis kinnitab serveri järjekorranumbri kättesaamist, millega sünkroniseerimine lõpetatakse. SYN-märk on nüüd välja lülitatud ja ACK-märk jääb seatud, mis näitab, et ühendus on loodud.



![Image](assets/fr/020.webp)



See Exchange protokoll tagab, et mõlemad osapooled kasutavad enne kasuliku koormuse andmete edastamist sama numeratsioonibaasi. Kui see sünkroniseerimine on lõpule viidud, avatakse seanss: segmendid võivad nüüd liikuda mõlemas suunas, mõlemat kinnitatakse vastuvõtmisel, tagades andmevoo maksimaalse usaldusväärsuse.


See ***kolmesuunaline käepigistus*** puudutab ainult ühenduse loomist. Sulgemiseks kasutab TCP *neljasuunalist käepigistust*: FIN → ACK → FIN → ACK, mis garanteerib, et ükski lõik ei kao enne ühenduse täielikku vabastamist.


Kuigi see protsess on kavandatud töökindluse ja usaldusväärsuse tagamiseks, on see tekitanud ka kasutatavaid haavatavusi. Näiteks selliste rünnakute nagu **IP Spoofing** eesmärk on sellest usaldussuhtest mööda minna või seda rikkuda, esitades end volitatud masinana võltsitud järjestusnumbrite abil, luues rikkumise, mis võimaldab andmevoo pealtkuulamist või manipuleerimist.


Järjestuse sünkroniseerimise kaaperdamise ohu piiramiseks ja võrgu koormuse haldamiseks kasutab TCP-protokoll voogude juhtimise tehnikat, mida tuntakse kui "**_Sliding Window_**". See süsteem reguleerib, kui palju andmeid võib saata, ilma et iga segmendi kohta nõutaks kohest kinnitust, vähendades seega võrgu tarbetut ülekoormust, säilitades samal ajal hea töökindluse.


Praktikas määratleb libisev aken järjestusnumbrite vahemiku, mis võib vabalt ringelda saatja ja vastuvõtja vahel, ilma et iga üksikut segmenti kinnitataks. Kui saatev süsteem saab kinnitusi, "libiseb" aken: see libiseb paremale, tehes ruumi uutele saadetavatele segmentidele. Selle akna suurus (mis on kriitilise tähtsusega läbilaskevõime optimeerimiseks, vältides samal ajal ummikuid) on määratud TCP päise väljal "*Window*".


**Näide**: kui algne järjekorranumber on 3 ja aken ulatub järjekorranumbrini 5, saab segmendid numbritega 3 kuni 5 saata ilma üksikuid kinnitusi ootamata.



![Image](assets/fr/021.webp)



Libiseva akna suurus ei ole fikseeritud; see kohandub dünaamiliselt vastavalt võrgu tingimustele ja vastuvõtja töötlemisvõimsusele.  Kui vastuvõtja suudab suurema andmemahuga hakkama saada, annab ta sellest märku aknavälja kaudu, kutsudes saatjat üles oma akent laiendama. Vastupidi, ülekoormuse või küllastumise ohu korral võib vastuvõtja taotleda vähendamist, saatja ootab, kuni aken liigub edasi, et saata täiendavaid segmente.


Protokolliga on ette nähtud sümmeetriline protseduur TCP-ühenduse sulgemiseks, et tagada puhas ja korrapärane sulgemine. Kumbki masin võib algatada sulgemise, saates segmendi, mille **FIN** lipukese on seatud 1, mis annab märku side lõpetamise kavatsusest. Seejärel ootab ta, kuni kõik edastatavad segmendid on vastu võetud, ja ignoreerib edasisi andmeid.


Selle segmendi vastuvõtmisel saadab teine masin kinnituse, mis on samuti märgistatud FIN-märgisega. Seejärel lõpetab ta allesjäänud andmete saatmise, enne kui teatab kohalikule rakendusele, et ühendus on suletud. Selline kahekordne kinnitus tagab nõuetekohase sulgemise ja vähendab andmekaotuse ohtu.


Sellist täpset juhtimist, mis ühendab IP paindliku marsruutimise ja TCP range kontrolli, illustreerib sageli diagramm, kus vastandatakse IP-protokolli kiirust (mis töötab **"parimate jõupingutuste "** alusel, ilma kättetoimetamise garantiita) ja TCP-protokolli usaldusväärsust (mis juhib edastamist kinnituste ja kokkulepitud jadade abil).



![Image](assets/fr/022.webp)



Mõnel juhul ei ole aga absoluutne usaldusväärsus esmatähtis, vaid kiirus ja lihtsus. See kehtib selliste rakenduste puhul nagu otseülekanne või VoIP, mis taluvad mõningaid paketikadu, ilma et see mõjutaks tõsiselt kasutajakogemust. Sellistel juhtudel eelistatakse **UDP** (_User Datagram Protocol_).


UDP töötab TCP-st põhimõtteliselt erineval põhimõttel: see on **ühendusteta**, mis tähendab, et saatja ja vastuvõtja vahel ei ole eelnevat suhet. Kui masin saadab pakette UDP kaudu, edastatakse need ühesuunaliselt; vastuvõtja ei saada kinnitusi ja saatja ei saa kinnitust, et sõnum on kohale jõudnud. UDP päis on tahtlikult minimaalne, sisaldades ainult lähteport, sihtport, segmendi pikkus ja kontrollsumma, ilma sisseehitatud kinnituse või staatuse kontrollimise mehhanismita. Nagu alati, on IP-aadressid kantud aluseks olevasse IP-pealkirja.


Üldine võrdlus on, et TCP on nagu **telefonikõne**, kus luuakse vooluahel, mida jälgitakse ja kontrollitakse kogu vestluse vältel. UDP-protokoll on nagu **postipostitus**, kus saatja pistab kirja postkasti, ilma kohese kättetoimetamistõendita või süstemaatilise tagasiside andmiseta.


Selline TCP ja UDP vastastikune täiendavus võimaldab kaasaegsetel võrkudel kohaneda erinevate vajadustega, valides sõltuvalt rakendusest maksimaalse usaldusväärsuse või kiiruse.



## Teenuse primitiivid


<chapterId>4480afb7-e950-4ccb-88fa-d132f9dc3479</chapterId>



### Kihiline arhitektuur ja Exchange korraldus


Nagu me nägime, on **teenused** seni kirjeldatud protokollide konkreetne rakendamine. Kuigi TCP/IP-mudel erineb **OSI**-mudelist, kasutatakse sama kihilist lähenemisviisi: iga Layer on kavandatud täitma konkreetset funktsiooni ja pakkuma **teenuseid** otse ülevalpool asuvale Layer-le, mille tulemuseks on modulaarne, töökindel ja kergesti hooldatav arhitektuur.


Iga Layer tugineb temast allpool asuva Layer võimalustele ja annab omakorda eespool asuva Layer-le andmete haldamiseks järjepideva Interface. Selles arhitektuuris on igal Layer-l oma **andmestruktuurid**, mis on hoolikalt määratletud, et tagada täiuslik ühilduvus teiste kihtidega. Selline ühilduvus on oluline sujuvaks, usaldusväärseks ja selgeks sidepidamiseks ühelt lõpp-punktilt teisele.


Neid vahetusi reguleerivad kaks põhiaspekti:


- Vertikaalne aspekt**: suhe ühe Layer ja selle kohal või all asuva Layer vahel (Layer N-st Layer N+1-ni ja vastupidi).



![Image](assets/fr/023.webp)




- Horisontaalne aspekt**: kaugrakenduste vaheline suhtlus, st dialoog **kliendi** ja **serveri** vahel, mõlemas suunas.



![Image](assets/fr/024.webp)



Kihiline arhitektuur järgib põhimõtet, et iga Layer töötleb ainult oma reguleerimisalasse kuuluvat teavet: andmestruktuurid, päised ja kontrollimehhanismid on Layer-l erinevad, kuid koos moodustavad nad ühtse süsteemi, mis tagab andmete järk-järgulise suunamise lõppsihtkohta.


**Meeldetuletus**: Kihtide vahel vahetatavate andmeühikute kirjeldamiseks kasutatakse spetsiifilist terminoloogiat:


- sõnum** taotluse Layer kohta,
- segment** transpordi Layer (TCP) jaoks,
- datagramm** Interneti Layer (IP) jaoks,
- raam** võrgujuurdepääsu Layer jaoks.


Alljärgnevas tabelis on kokkuvõte TCP- ja UDP-kontekstide terminitest:


| TCP/IP Layer         | Unit Name (TCP) | Unit Name (UDP) |
|----------------------|------------------|------------------|
| Application Layer    | Stream           | Message          |
| Transport Layer      | Segment          | Packet           |
| Internet Layer       | Datagram         | Datagram         |
| Network Access Layer | Frame            | Frame            |

### Teenuse primitiivid ja andmeühikud


Selle süsteemi keskmes on **teenuse algmoodulid**, mis toimivad suhtlusliidestena. Need algmoodulid toimivad nagu teenindusjaamad, kuulates reserveeritud konkreetseid **porti** ja võimaldades protsessidel luua, säilitada ja lõpetada võrguühendusi kontrollitud viisil. Kuigi protokollid korraldavad andmete vormingut ja edastamist võrgus, on **teenused ja nende primitiivid** need, mis tagavad vertikaalse sideme kihtide vahel.


Ühendades horisontaalse aspekti (hajutatud rakenduste vaheline side) vertikaalse aspektiga (kihtide vaheline sisemine suhtlus), pakub TCP/IP mudel täielikku ja skaleeritavat arhitektuuri. Nende kahe vaatenurga kattumine annab selge ülevaate sellest, kuidas andmeid vahetatakse struktureeritud võrgusuhtluses.



![Image](assets/fr/026.webp)



### Osa kokkuvõte


Selles esimeses suuremas osas uurisime põhilist arhitektuuri, mis reguleerib tänapäeva Interneti-ühendusega võrkude konfiguratsiooni ja toimimist. See arhitektuur põhineb OSI-mudelist inspireeritud **nelja Layer mudelil**, mis on üles ehitatud kaasaegse kommunikatsiooni selgroo, **TCP/IP** protokollide komplekti ümber. Me nägime, et TCP tagab oma ühendusele orienteeritud lähenemisega usaldusväärse ülekande, samas kui UDP, mis on kergem ja kiirem, on eelistatud, kui kiirus on tähtsam kui usaldusväärsus.


Selle mudeli nõuetekohane toimimine sõltub protokollide rakendamisest **teenusepõhimõtete** kaudu. Need tagavad sideme kihtide vahel, võimaldades andmetöötluse kohandamist iga tasandi erinõuetele, alates transpordist kuni rakendusteni, sealhulgas Interneti- ja võrgujuurdepääsuni. Selline modulaarne lähenemisviis muudab süsteemi nii paindlikuks kui ka töökindlaks.


IP-aadressimine on selle infrastruktuuri teine nurgakivi. Iga ühendatud seade on identifitseeritud **üksikliku IP Address** abil, mis on võetud Address ruumi, mis on jaotatud **klassidesse** (A-st E-sse). Mõned neist aadressidest on reserveeritud eriotstarbeliseks kasutamiseks, näiteks kohalik tagasisaatmine või multisaatmine, samas kui teisi, nn privaatseid aadresse, ei edastata Internetis ilma tõlkimiseta (NAT). Selline liigitus võimaldab võrkude loogilist, hierarhilist korraldust.


Samuti uurisime **alavõrkude** kontseptsiooni, mis võimaldab jagada võrgu segmente, et paremini hallata IP-ressursse ja optimeerida andmevooge. Kuigi käsitsi alavõrkude jagamine alamvõrkude maskide abil on endiselt oluline põhimõte, on see tänu **CIDRile** (_Classless Inter-Domain Routing_) suures osas kaasajastatud. See meetod on muutnud Address haldamist, võimaldades IP-piirkondade paindlikumat ja ratsionaalsemat jaotamist, vähendades samal ajal marsruutimistabelite suurust.


Nende mõistete - kihtide, protokollide, teenuste algtunnuste, adresseerimise ja alamvõrkude määramise - omandamisega saate tugeva aluse kaasaegsete võrkude tehnilise toimimise mõistmiseks ja võrguinfrastruktuuri tõhusaks konfigureerimiseks tänapäeva vajaduste rahuldamiseks.


Järgmises jaotises vaatleme lähemalt IPv4-aadressimist.



# IPv4-aadressimine


<partId>83f3c3e5-378c-440f-a095-df210842efde</partId>



## IPv4 kasutamine


<chapterId>79e4dd18-446a-435b-9f25-c88a00f8bec6</chapterId>



Selles jaotises läheme sügavamale ja vaatleme, kuidas **IPv4**-aadressid reaalses võrgus tegelikult rakenduvad. Me analüüsime nende formaati, nende loogikat ja seda, kuidas nad on seotud teiste peamiste Elements-võrkudega, nagu **DNS-nimed**, **MAC-aadressid**, **alavõrgud** ja **tõlketehnikad**.


IP Address on unikaalne numbriline identifikaator, mis on määratud igale **võrgu Interface** seadmes. See võimaldab seda seadet võrgus üles leida ja temaga andmete edastamiseks ühendust võtta. Näiteks ruuteril, serveril, tööjaamal, võrguprinteril või isegi valvekaameral on vähemalt üks IP Address. IP Address teeb võimalikuks **routerdamise**, st pakettide edastamise punktist A punkti B, isegi kui need asuvad füüsiliselt kaugel üksteisest.


IP-aadresse saab määrata peamiselt kahel viisil:


- Staatiline**: Seadmes käsitsi seadistatud.
- Dünaamiline**: DHCP (_Dynamic Host Configuration Protocol_) serveri poolt automaatselt määratud nõudmisel. DHCP lihtsustab võrgu haldamist, kõrvaldades vajaduse käsitsi konfigureerimise järele, võimaldades samal ajal täpset kontrolli reserveerimise ja rendiperioodi kaudu.


**IPv4**-aadressid kirjutatakse **32-bitises** formaadis, mis on jagatud **neljaks baidiks**. Iga bait sisaldab 8 bitti ja kujutab kümnendarvu vahemikus 0 kuni 255. Neli baiti on eraldatud punktidega, et moodustada selge ja loetav tähistus.


näide: Address 172.16.254.1_



![Image](assets/fr/027.webp)



Iga bait on väärtusega (või "kaaluga"): vasakpoolne bitt (kõige tähtsam bitt) on väärtusega 128, järgmine 64, seejärel 32, 16, 8, 4, 2 ja 1 parempoolne bitt (kõige vähemväärtuslikum bitt). Sel viisil teisendatakse binaarkirjutus kümnendsüsteemi lihtsa kaalude liitmise teel.


Järgnev tabel illustreerib seda vastavust:



| Binary Code | Activated Bit Values          | Decimal Value |
|-------------|-------------------------------|---------------|
| 00000000    | 0                             | 0             |
| 00000001    | 1                             | 1             |
| 00000011    | 1 + 2                         | 3             |
| 00000111    | 1 + 2 + 4                     | 7             |
| 00001111    | 1 + 2 + 4 + 8                 | 15            |
| 00011111    | 1 + 2 + 4 + 8 + 16            | 31            |
| 00111111    | 1 + 2 + 4 + 8 + 16 + 32       | 63            |
| 01111111    | 1 + 2 + 4 + 8 + 16 + 32 + 64  | 127           |
| 11111111    | 1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 | 255      |

Binaarsüsteemi teisendamiseks kümnendsüsteemiks tuleb liita nende bittide osakaalud, mis on seatud 1.


| Binary     | Decimal Value |
| ---------- | ------------- |
| `10101100` | 172           |
| `00010000` | 16            |
| `11111110` | 254           |
| `00000001` | 1             |

IP Address tähistab ühte **võrgu Interface**, mitte kogu seadet. Mitmeportaalsel marsruuteril või tulemüüril on mitu liidest, millest igaühel on oma IP Address. Ühel Interface-l võib olla isegi mitu IP-aadressi (näiteks mitme virtuaalse võrgu või teenuse teenindamiseks).


Iga IP-paketi päises on kaks IP-aadressi:


- Allikas Address (**saatja**)
- Sihtkoht Address (**vastuvõtja**)

Marsruuterid loevad neid aadresse, et leida parim tee paketi saatmiseks, kuni see jõuab sihtkohta. Ilma rangete aadressireegliteta ei saaks võrguliiklust õigesti suunata ja võrkude ülemaailmne ühendamine oleks võimatu.


IPv4 Address koosneb kahest osast:


- NetID**: identifitseerib võrgu
- HostID**: identifitseerib seadme kõnealuses võrgus

**Alavõrgumask** määrab, kus lõpeb NetID ja algab HostID, määrates, mitu bitti kuulub kummalegi osale. Mida pikem on NetID, seda suurem on võimalike alamvõrkude arv, kuid vastavalt väheneb hostide arv alamvõrgu kohta.


Algselt olid IPv4-võrgud jagatud viide **klassi**: (A, B, C, D ja E). Iga klass vastab konkreetsele NetID-vahemikule ja määratleb kindla granulaarsuse:


- A-klass: väga suured võrgud suure hulga hostidega
- B-klass: keskmise suurusega võrgud
- C-klass: väikesed võrgud
- Klass D: aadressid, mis on reserveeritud multisaatmiseks (_multicast_)
- Klass E: eksperimentaalsed aadressid, mida ei kasutata tavapärasteks aadressideks



| Class | Leading Bits | First Byte Range | Default Subnet Mask | Purpose                          |
| ----- | ------------ | ---------------- | ------------------- | -------------------------------- |
| A     | 0            | 0 – 127          | 255.0.0.0           | Very large networks              |
| B     | 10           | 128 – 191        | 255.255.0.0         | Medium-sized networks            |
| C     | 110          | 192 – 223        | 255.255.255.0       | Small networks                   |
| D     | 1110         | 224 – 239        | N/A                 | Multicast addresses              |
| E     | 1111         | 240 – 255        | N/A                 | Experimental (not publicly used) |

Eriaadressid:


- Võrk Address**: Identifitseerib võrku ennast (kasutatakse marsruutimistabelites).
- Saade Address**: Saadab andmed korraga kõigile seadmetele allvõrgus (kõik HostID bits on seatud 1).


Järgmised vahemikud on reserveeritud sisekasutuseks:


- 10.0.0.0/8** (A-klassi eraisik)
- 127.0.0.0/8** (kohalik tagasiside või _loopback_)
- 172.16.0.0 kuni 172.31.255.255** (privaatne B-klass)
- 192.168.0.0 kuni 192.168.255.255** (privaatne C-klass)


Aadressid **127.0.0.1** ja üldisemalt kogu 127.0.0.0/8 kasutatakse sisemiseks testimiseks: kõik sinna saadetud päringud ei lahku kunagi masinast. See on kasulik selleks, et kontrollida, kas kohalik võrguteenus töötab ilma laiemat võrku kaasamata.


Address ruumi paremaks kasutamiseks jagavad administraatorid sageli võrgud **alavõrkudeks**, kasutades alammaske või **CIDR** märkimist (_Classless Inter-Domain Routing_). CIDR võimaldab täpsemat haldamist ja aitab vältida aadresside raiskamist. Tänapäeval on CIDR oluline IP-piirkondade peenhäälestamiseks ja marsruutimistabelite suuruse vähendamiseks.


Kaasaegsetes võrkudes on IP-aadressimine tavaliselt ühendatud teiste identifikaatoritega:



- domeeninimi**, mis on registreeritud **DNSis** (_Domain Name System_): See seostab numbrilise IP Address inimsõbraliku nimega.
- MAC Address**: võrgukaardile graveeritud füüsiline identifikaator, mida kasutatakse kohalikuks transpordiks (_Ethernet_). Kui IP-paketti on vaja füüsiliselt edastada, siis ARP-tabel võrdleb IP Address sihtkoha MAC Address-ga.


IPv4 Address puudujäägi kõrvaldamiseks ja Layer turvalisuse lisamiseks kasutavad võrgud sageli Address tõlget (_NAT_). NAT võimaldab paljudel eraseadmetel jagada Internetti pääsemisel ühte avalikku IP Address.


**Märkus**: Veebipõhised ja sisseehitatud operatsioonisüsteemi tööriistad, näiteks [Grenoble CRIC kalkulaator](http://cric.grenoble.cnrs.fr/Administrateurs/Outils/CalculMasque/), muudavad alamvõrgu ja maski arvutused palju lihtsamaks.

Need utiliidid aitavad võrgu jagamist tõhusalt planeerida.


Kokkuvõtteks võib öelda, et Address on endiselt praktiline funktsioon, et saata sama sõnum kõigile segmendiga ühendatud seadmetele: see saavutatakse, kui kõik bitid HostID-osas on 1, nii et kõik hostid on sihtrühmaks.



## Erinevad IPv4 Address tüübid


<chapterId>2adfad24-a90d-45b5-b808-3d2f6598bebf</chapterId>



IPv4-aadressid jagunevad kahte põhikategooriasse: avalikud aadressid, mis on otse kättesaadavad Internetis, ja privaatsed aadressid, mis on mõeldud sisekasutuseks kohalikus võrgus.


Avalik IPv4 Address on ülemaailmselt unikaalne ja marsruutitav kogu Internetis. Selle määravad ametlikud asutused ja see on vajalik avalike teenuste, näiteks veebisaitide, e-posti serverite või pilveinfrastruktuuri jaoks.

Nende aadresside ülemaailmne unikaalsus on oluline, et vältida marsruutimiskonflikte või kokkupõrkeid.


Nende IP-piirkondade jaotamist haldab **IANA** (_Internet Assigned Numbers Authority_), mis tegutseb **ICANNi** (_Internet Corporation for Assigned Names and Numbers_) alluvuses. Konkreetselt öeldes jagab IANA IPv4-ruumi 256 plokki suurusega /8 vastavalt CIDR-märkimisele. Iga plokk esindab veidi üle 16,7 miljoni aadressi (2³² / 2⁸).


IANA on usaldanud need Address üheaadressi plokid **Regionaalsetele internetiregistritele** (RIR). Need RIRid vastutavad aadresside ümberjaotamise eest piirkondlikul tasandil vastavalt juurdepääsu pakkujate, ettevõtete või haldusasutuste tegelikele vajadustele. Unicast Address ruum ulatub plokkidest **1/8 kuni 223/8**, millest osad on kas reserveeritud erikasutuseks (teadusuuringud, dokumenteerimine, testimine) või eraldatud otse võrgule või RIRile ümberjaotamiseks.


Avaliku IP Address omanikuks olemise kontrollimiseks saate vaadata RIRi andmebaasidest, kasutades käsku **whois** või iga registri pakutavaid veebiliideseid. Nende vahendite abil saab Address tagasi jälgida organisatsiooni või teenusepakkujani, kes selle deklareeris.


Seevastu on olemas privaatseid IPv4-aadresse, mis on praktiline vastus avalike aadresside puudusele. Need aadressid, mida ei saa Internetis suunata, on reserveeritud kohalikele keskkondadele: ettevõtete võrkudele, kodustele kohtvõrkudele, andmekeskustele või arvutiklastritele. Need ei ole ülemaailmselt unikaalsed: paljud eravõrgud võivad samu IP-piirkondi segamatult uuesti kasutada, kui nad jäävad isoleerituks või kasutavad internetile juurdepääsuks võrgu Address tõlkeseadmeid.


Selleks, et võimaldada privaatse IP Address-ga seadmele juurdepääsu Internetile, kasutavad võrgud NAT-i (Network Address Translation). NAT töötab, asendades dünaamiliselt privaatse Address avaliku Address-ga, võimaldades kümnetel (või isegi sadadel) seadmetel jagada ühte avalikku IP Address. See meetod optimeerib IPv4 ruumi kasutamist ja lisab ka Layer turvalisust, varjates võrgu sisemise struktuuri.


Teine erikategooria on **määratlemata** aadressid. IPv4 märkus **0.0.0.0.0** või selle IPv6 versioon **::/128** tähendab "puudub konkreetne Address". Selline Address on kehtetu kui võrgu Address sihtkoht, kuid seda võib host kasutada lokaalselt, et märkida "kõik liidesed" või "Address ei ole veel määratud". See on tavaline DHCP dünaamilise Assignment puhul või kõigi serveriliideste kuulamiseks.


IPv6 toetab ka privaatset adresseerimist, kuid standard soovitab üldiselt avalikku adresseerimist, et vältida mitme NAT-kihi korrastamist. Bloki **fec0::/10** **sait-lokaalsed aadressid** (_site-local_) kaotasid järjepidevuse ja turvalisuse huvides kehtivuse **RFC 3879** järgi. Need asendati **Unikaalsete lokaalsete aadressidega** (_ULA_), mis asuvad **fc00::/7** plokis. ULAd võimaldavad luua puhta sisemise marsruutimisega privaatseid IPv6-võrke, kasutades juhuslikult genereeritud 40-bitist identifikaatorit, et tagada kohalik unikaalsus.


IPv4 ammendumine kinnitati ametlikult 2011. aastal. Selle eluea pikendamiseks võttis internetikogukond vastu mitu strateegiat:


- Järkjärguline üleminek **IPv6-le**
- **NAT** laialdane kasutamine
- Rangemad eraldamispõhimõtted, mis nõuavad Address vajaduste täpset põhjendamist ja haldamist
- Kasutamata või vabatahtlikult tagastatud Address plokkide tagasinõudmine äriühingute poolt


Need meetmed näitavad, et IP-aadressimine ei ole mitte ainult tehniline probleem, vaid ka ülemaailmse juhtimise küsimus, mis on Interneti jätkuva laienemise seisukohalt keskse tähtsusega.



## DNS, Address kataloog


<chapterId>511244ec-ba43-44ac-b4c3-b41579a15cff</chapterId>



Olgem ausad, inimesed ei suuda hästi meelde jätta pikki numbrite jadasid, olgu need siis binaarses või kümnendsüsteemis. See probleem muutub veelgi suuremaks IP-aadresside puhul, mis võivad olla keerulised ja üks IP Address võib mõnikord maskeerida mitu aadressi, eriti kui kasutatakse selliseid tehnikaid nagu NAT või virtuaalne hosting.


Asjade lihtsustamiseks kasutab rakendus Layer süsteemi, mis seob IP Address loogilise, inimesele loetava nimega. See on **DNS** (*Domain Name System*), massiivne, hierarhiline, hajutatud kataloog, mis sobitab loetavad domeeninimed IP-aadressidega. Süsteem põhineb protokollidel ja teenustel. Kõige laialdasemalt kasutatav DNS-serveri tarkvara on **BIND** (_Berkeley Internet Name Domain_), avatud lähtekoodiga tarkvarapakett, mis viitab suurele osale Interneti DNS-infrastruktuurist.


DNS-i põhiline idee on lihtne: iga ühendatud teenuse, olgu selleks siis veebisait, postiserver või muu võrguteenus, jaoks on olemas kirje, mis seob domeeninime ühe või mitme IP-aadressiga. See toimib kahes suunas:


- Edasisaatmine: nime tõlkimine IP-ks Address.
- Pöördlahendus: antud IP-aadressiga seotud domeeninime leidmine Address.

See muudab võrguadresseerimise inimestele kasutatavaks, säilitades samal ajal täpsuse, mida marsruuterid vajavad andmete korrektseks liikumiseks.


Domeeninimi on alati hierarhiliselt struktureeritud, kusjuures iga tase on eraldatud punktiga: täisnime nimetatakse **FQDN** (_Fully Qualified Domain Name_). Kõige parempoolsem osa on **TLD** (_Top Level Domain_), näiteks `.com`, `.org` või `.fr`. Kõige vasakpoolsem osa tähistab host'i, st konkreetset masinat või teenust, mis on seotud IP Address-ga.


DNS-süsteem on loodud **tsoonide puuna**. **tsoon** on domeeni nimeruumi osa, mida haldab konkreetne DNS-server. Üks tsoon võib sisaldada mitmeid **alldomeene**, mis võivad omakorda olla delegeeritud teistesse tsoonidesse, mida haldavad erinevad serverid. Administraatorid vastutavad oma tsoonide hooldamise eest: uuenduste, delegeerimise ja üldise haldamise eest.


See struktuur võimaldab mitte ainult osutada põhidomeenile (nt `example.com`), vaid ka täpsustada kirjeid üksikute hostide jaoks (`www`, `mail`, `ftp` jne.). Võrgustiku algusaegadel käsitleti seda kaardistamist staatiliste failide abil (`/etc/hosts` Unixi süsteemides), kuid selline meetod muutus kiiresti ebapraktiliseks kiiresti kasvava, omavahel ühendatud Interneti jaoks.


Oluline on mõista, et **DNS-server** võib teenindada ainult piiratud ulatusega. Näiteks ei pruugi ettevõtte sisemine DNS-server olla internetist otse kättesaadav. Kui see DNS ei ole konfigureeritud päringute edastamiseks või kui tal ei ole usaldusväärset suhet teiste serveritega, siis mõned päringud ebaõnnestuvad: nime ega IP Address ei saa siis väljaspool määratletud tsooni lahendada.


DNS mängib rolli ka e-posti marsruutimises. Näiteks **MX** (_Mail Exchange_) kirje määrab kindlaks e-posti serverid, mis vastutavad antud domeeni e-kirjade vastuvõtmise eest. Need kirjed määravad prioriteedid (kaalutegur) ja tõrkelahendused. DNS-serveri tsoonifail peab sisaldama **SOA** (_Start Of Authority_) kirjet, mis määrab serveri selle tsooni ametlikuks teabeallikaks.


Tänu oma hierarhilisele, hajutatud struktuurile on DNS endiselt Interneti nurgakivi, mis võimaldab kasutajatel pääseda teenustele juurde selgete, meeldejäävate domeeninimede kaudu pikkade tehniliste IP-aadresside asemel.


Järgmises peatükis uurime veel üht põhikontseptsiooni: **Ethernet-aadressid**, mida nimetatakse ka **MAC-aadressideks**, mis tagavad andmete edastamise kohtvõrgu füüsilises Layer-s.



## Ethernet-aadresside ja ARP avastamine


<chapterId>d02109f6-9bf9-4261-a8f9-e1aa4398b949</chapterId>



### Määratlused


Selleks, et andmete marsruutimisprotokoll töötaks usaldusväärselt ja järjepidevalt, on oluline üks põhikomponent. Inimestena saame me masinat hõlpsasti tuvastada selle IP Address või DNSi kaudu leitud nime järgi. Masin peab aga suutma pakettide edastamiseks üheselt ära tunda sihtseadme. Selleks tugineb ta konkreetsele riistvara tunnusele, mida kasutab otseselt tema võrgu Interface: MAC Address (_Media Access Control_).


**Märkus**: Sellel ei ole midagi pistmist "füüsilise Address" mäluarhitektuuriga. Arvutitehnikas viitab füüsiline mälu Address konkreetsele asukohale mälubussis, erinevalt virtuaalsest Address-st, mida haldab operatsioonisüsteem. Seevastu MAC Address on seotud rangelt võrgurakendusega.


MAC Address on seadme tootja poolt püsivalt ja üheselt määratud. MAC Address identifitseerib üheselt võrgukaardi, olenemata sellest, kas tegemist on arvuti, nutitelefoni, printeri või mõne muu ühendatud seadmega. Erinevalt IP Address-st, mis võib dünaamiliselt muutuda (DHCP-serveri või käsitsi konfigureerimise kaudu), jääb MAC Address tavaliselt kogu seadme eluea jooksul samaks, kui seda ei muudeta tahtlikult.


Igal võrgu Interface, nii traadiga kui ka traadita, on oma MAC Address. Seda Address kasutatakse andmeside Layer raames (OSI mudeli Layer 2), et sisestada ja hallata riistvara Address igas vahetatavas võrgukaadris. Seda nimetatakse mõnikord _Etherneti aadressiks_ või _UAA_ (_Universally Administered Address_). Standarditud pikkus on 48 bitti ehk 6 baiti ja see kirjutatakse heksadekaalarvudes, tavaliselt baididena, mis on eraldatud `:` või `-`ga.


Näiteks: "5A:BC:17:A2:AF:15"


Selles struktuuris identifitseerivad esimesed kolm baiti võrgukaardi tootjat: seda nimetatakse **OUI** (*Organisationally Unique Identifier*). Neid IEEE poolt määratud eesliiteid kasutatakse ka muudes riistvara adresseerimisskeemides, nagu Bluetooth ja LLDP, et tagada ülemaailmne unikaalsus.


### MAC Address muutmine (MAC Spoofing)


Teoreetiliselt on MAC Address kavandatud nii, et see jääks fikseerituks, kuid on olemas võimalused selle muutmiseks, eelkõige konkreetsete vajaduste rahuldamiseks või teatavate piirangute vältimiseks. See operatsioon, mida sageli nimetatakse _spoofing MAC_, hõlmab algse riistvaralise Address asendamist teistsuguse väärtusega, mis on määratletud tarkvara tasandil. Mõned operatsioonisüsteemid hõlbustavad seda muutmist, eriti kui tegelik Ethernet Address ei ole draiveri poolt otseselt kasutatav.


Sellise muutuse põhjused on erinevad. See võib olla vajadus, et teatav rakendus vajab korrektseks toimimiseks konkreetset Ethernet Address või et lahendada kahe sama kohtvõrku kasutava seadme vaheliste identsete aadresside konflikt.


MAC Address muutmise põhjuseks võivad olla ka eraelu puutumatuse kaalutlused: kaardile graveeritud unikaalse identifikaatori varjamisega vähendavad kasutajad võimalust, et nende seadet jälgivad võrgud või järelevalveteenistused. Selline praktika ei ole siiski ilma tagajärgedeta. MAC Address muutmine võib häirida teatavaid filtreerivaid seadmeid või nõuda tulemüüride ümberkonfigureerimist, et lubada uut riistvara.


Mõned võrgud, eriti Wi-Fi, kasutavad MAC Address filtreerimist, et lubada ainult heakskiidetud aadressidega seadmeid. Kuigi see lisab põhilise kontrolli taseme, ei ole see iseenesest turvaline. Ründaja võib hõivata võrgus juba lubatud MAC Address ja kloonida selle piirangutest möödahiilimiseks. Seetõttu tuleks MAC-filtreerimist alati kombineerida tugevamate turvameetmetega.


### MAC/IP kirjavahetus


Selleks, et kohalik võrk toimiks tõhusalt, peab füüsiliste aadresside (MAC-aadressid) ja loogiliste aadresside (IP-aadressid) vahel olema selge vastavus. Ilma selle seoseta võib arvuti teada sihtkoha IP Address, kuid ei tea, kuidas füüsiliselt andmeid sinna kohalikus võrgus saata.

Seda kaardistamist teostab automaatselt ARP (_Adress Resolution Protocol_).


Kui kasutaja soovib teada, milline MAC Address vastab konkreetsele IP Address-le, võib ta kasutada abiprogrammi "ARP". See tööriist kontrollib masina kohalikku ARP-tabelit, et näidata teadaolevaid kokkulangevusi IP-aadresside ja MAC-aadresside vahel kohalikus võrgus. Sel viisil on võimalik kiiresti kontrollida tegelikku seost loogilise ja füüsilise kihi vahel.


Praktiline näide: kui soovite kontrollida, milline võrgukaart vastab IP Address `192.168.1.5`, kasutage järgmist käsku:


```bash
arp –a 192.168.1.5
```


Väljund näitab seotud füüsilist Address (MAC), sisendi laadi (staatiline või dünaamiline) ja asjaomast Interface.


```
Interface: 192.168.1.5 --- 0x5
IP Address            MAC Address                Type
192.168.1.5           00:54:BC:17:14:6E          D
```


Oluline on meeles pidada, et MAC Address ja IP Address on kaks täiesti erinevat identifikaatorit, mis siiski täiendavad üksteist. MAC Address graveeritakse tootja poolt igale võrgu Interface-le unikaalselt ja seda kasutatakse seadme füüsiliseks identifitseerimiseks kohalikus võrgus. IP Address on seevastu loogiline Address, mis on määratud kas dünaamiliselt või staatiliselt, võimaldades seadmel liituda IP-võrguga ja Exchange pakettidega väljaspool oma kohalikku võrku.



- Visuaalne näide MAC Address kohta:


![Image](assets/fr/032.webp)




- Visuaalne näide IP Address-st:


![Image](assets/fr/027.webp)



Ettevõtte keskkonnas ei saa need kaks adresseerimistasandit eraldi toimida. Näiteks kui DHCP-server määrab automaatselt IP Address, kasutatakse lähtepunktina seadme MAC Address. Arvuti saadab DHCP eetrisse taotluse, mis sisaldab tema MAC Address, et server saaks määrata õigele seadmele vaba IP Address. Ilma selle riistvara identifitseerimiseta ei teaks DHCP-server, millisele seadmele Address edastada.


ARP-protokoll on seega väga oluline: see loob seose IP-aadresside ja füüsiliste aadresside vahel, võimaldades masinatel tõlkida loogiline sihtkoht tegelikuks füüsiliseks sihtkohaks. Kui arvutil on vaja saata pakett samas võrgus asuvale masinale, vaatab ta kõigepealt ARP-tabelist, et kontrollida, kas vastuvõtja MAC Address on juba teada. Kui ei ole, saadab ta ARP päringu kõigile kohalikus võrgus asuvatele hostidele. Seade, mis tunneb selles taotluses siht-IP Address ära, vastab, määrates oma MAC Address. Seejärel kirjutab saatja selle IP/MAC paari oma ARP vahemällu, et vältida operatsiooni kordamist iga kord, kui taotlus saadetakse.


See ARP-tabel toimib kui minikataloog, mida uuendatakse dünaamiliselt sarnaselt DNS-i poolt IP-aadressidega seostatud domeeninimedega. Ilma ARP-tahvlita ei oleks võimalik kohalik Exchange, sest andmeside Layer peab teadma MAC Address, et Ethernet-raame õigesti kapseldada.


Seevastu RARP-protokoll (_Reverse Address Resolution Protocol_) on mõeldud vastupidiseks olukorraks: võimaldada masinal, mis teab ainult oma MAC Address, leida oma IP Address. See oli tavaline juhtum vanemate tööjaamade puhul, millel ei olnud kohalikku Hard-ketast, mis pidid käivituma üle võrgu ja taotlema IP Address. RARP asendati lõpuks **BOOTP** ja seejärel **DHCP**, mis on paindlikumad ja automatiseeritumad.


Need assotsiatsiooniprotokollid mängivad marsruutimises olulist rolli. Marsruuter on sisuliselt masin, millel on mitu võrguliidest, mis ühendavad erinevaid segmente. Kui marsruuter saab kaadri, töötleb ta seda, et eraldada IP-datagramm ja uurib IP-pealkirja, et määrata sihtkoht. Kui sihtkoht asub otseühendusega võrgus, edastatakse datagramm pärast päise päise uuendamist otse. Kui sihtkoht kuulub teise võrku, kasutab marsruuter oma marsruutimistabelit, et leida parim tee ehk _järgmine hüpe_ sihtkohani.


See jaotab marsruudi lühemateks, paremini hallatavateks lõikudeks. Iga vahepealne marsruuter teab ainult järgmist sammu, mitte tingimata lõppsihtkohta.


**Mäletatavasti:** Otsene kättetoimetamine toimub siis, kui saatja ja vastuvõtja asuvad samas füüsilises võrgus. Muul juhul on kättetoimetamine kaudne ja läbib ühe või mitu marsruuterit.


Marsruutimistabel, mida hallatakse kas käsitsi (staatiline marsruutimine) või dünaamiliselt (dünaamiline marsruutimine), sisaldab teavet, mida on vaja marsruudi valimiseks. Väikestes võrkudes piisab staatilisest konfiguratsioonist. Suuremates infrastruktuurides on dünaamiline marsruutimine oluline, et automaatselt kohandada marsruute, kui topoloogia muutub või mõni link läheb katki.


Marsruutimistabel toimib siht-IP-aadresside ja järgmiste väravate vahelise kaardistustabelina. Tavaliselt salvestatakse selles pigem võrgu identifikaatorid (_network ID_) kui iga üksiku host Address, mis vähendab oluliselt selle suurust.


| Destination Address | Next-Hop Router Address | Interface |
| ------------------- | ----------------------- | --------- |

Nende kirjete abil saab marsruuter kiiresti kindlaks teha, millise Interface kaudu ja millisele sõlmpunktile iga andmeprogramm tuleks saata. Koos ARP-ga sobivate MAC-aadresside lahendamiseks tagab see tõhusa ja usaldusväärse andmeedastuse üle võrgu.


Dünaamilised marsruutimisprotokollid hõlmavad selliseid standardeid nagu RIP (_Routing Information Protocol_), mis põhineb kauguse algoritmil, ja OSPF (_Open Shortest Path First_), mis arvutab lühimaid teid keerulises topoloogias. Need protokollid Exchange uuendavad pidevalt marsruute, et optimeerida marsruute, vähendada ülekandekulusid ja parandada vastupidavust katkestuste või ülekoormuse korral.



## NAT: Address tõlge


<chapterId>4f984d5d-f2e0-4faf-b703-ff315f32cef4</chapterId>



### Määratlus


Network Address Translation_ (NAT) on tehnika, mis on välja töötatud Address olemasolevate IPv4-aadresside järkjärguliseks ammendumiseks. Enne IPv6 laialdast kasutuselevõttu ajutise lahendusena loodud NAT võimaldas ettevõtetel ja üksikisikutel jätkata suure hulga masinate ühendamist, kasutades samal ajal ainult piiratud hulka avalikke IP-aadresse.


**Tähtis meeldetuletus:** üleminek IPv4-lt IPv6-le teoreetiliselt lahendab ammendumise probleemi, laiendades Address ruumi 32 bitilt 128 bitile, pakkudes peaaegu piiramatut arvu aadresse (2^128). Tegelikkuses on üleminek siiski veel mittetäielik ja NAT on ka praegu laialdaselt kasutusel.


NAT-i põhimõte on lihtne, kuid väga tõhus: selle asemel, et määrata igale sisevõrgu seadmele unikaalne avalik IP-aadress Address, kasutatakse kõigi privaatsete seadmete jaoks ühte marsruutimisvõimalusega Address (või väikest aadresside kogumit). NAT-värav, mis on sageli integreeritud marsruuterisse või tulemüüri, tõlgib dünaamiliselt sisemise IP Address koos teabega, mida on vaja liikluse korrektseks suunamiseks välismaailma, ja tagab, et vastused saadetakse tagasi algsele saatjale.


Sellisel lähenemisviisil on vahetu eelis: see varjab täielikult võrgu sisemise arhitektuuri. Välise vaatleja jaoks näivad kõik tööjaamade, serverite või printerite päringud tulevat samast avalikust identiteedist. Eriaadressid, mis on tavaliselt võetud reserveeritud vahemikest (nt 192.168.x.x või 10.x.x.x.x), jäävad internetist nähtamatuks.


Lisaks IPv4 nappuse lahendamisele tugevdab NAT ka turvalisust, luues esimese loogilise barjääri sisevõrgu ja avalike võrkude vahele. Soovimatu sissetulev side on loomulikult blokeeritud, sest ainult võrgu siseselt algatatud ühendused saavad vastuse saamiseks vajaliku tõlke.



![Image](assets/fr/035.webp)



### Tõlketüübid


NATi saab rakendada eri viisidel, et see vastaks konkreetsetele vajadustele. Kaks peamist töörežiimi on staatiline ja dünaamiline tõlge.


**Staatiline tõlge** loob fikseeritud kaardistuse privaatse IP Address ja avaliku IP Address vahel. Iga sisemine masin on püsivalt seotud oma spetsiaalse avaliku Address-ga. Näiteks võib siseseade, mis on konfigureeritud kui 192.168.20.1, olla seotud marsruutitava Address-ga 157.54.130.1. Kui väljaminev pakett lahkub kohalikust võrgust, asendab marsruuter paketi lähte Address avaliku Address-ga ja teeb sissetuleva liikluse puhul vastupidise operatsiooni. See kahesuunaline tõlge on kasutajale läbipaistev.


**Hoiatus:** Kuigi see meetod isoleerib sisevõrgu, ei lahenda see avalike IP-aadresside puudust, sest teil on vaja ikkagi nii palju avalikke aadresse, kui palju on masinaid, mida avalikustada. Staatilist tõlget kasutatakse seetõttu peamiselt siis, kui teatud siseressursid peavad jääma väljastpoolt ligipääsetavaks (veebiserver, postiserver...).


**Dünaamiline tõlge** seevastu kasutab avalike IP-aadresside kogumit. Kui sisemine host alustab ühendust, määrab marsruuter ajutiselt ühe neist avalikest aadressidest host'i privaatsele Address-le seansi ajaks. Ühendus on 1:1, kuid ajutine: kui ühendus lõpeb, muutub avalik Address teise seadme jaoks kättesaadavaks. Dünaamiline NAT vähendab seega vajalike avalike aadresside arvu, kui kõik masinad ei ole samal ajal võrgus, kuid see nõuab siiski vähemalt sama suurt väliste aadresside blokki kui maksimaalne samaaegsete ühenduste arv.


**Port translation** (PAT), tuntud ka kui *NAT overload* või *IP masquerading*, läheb sammu võrra kaugemale: kõik privaatseadmed jagavad ühte avalikku IP Address (või väga väikest arvu). Sessioonide eristamiseks muudab värav mitte ainult lähte Address, vaid ka lähteport. Ta peab tabelit, mis seob iga *(privaatne Address, privaatne port)* paari unikaalse *(avalik Address, avalik port)* paariga. Seda NAT-i vormi kasutatakse peaaegu kõigis koduruuterites, mis võimaldab kümnetel seadmetel (arvutid, nutitelefonid, ühendatud objektid jne) jagada sama avalikku IP Address, säilitades samal ajal sujuvat suhtlust.


NAT pikendab seega IPv4-i eluiga, lisades samal ajal väärtusliku Layer segmenteerimise ja turvalisuse. Kuna IPv6 kasutuselevõtt kasvab ja selle suur Address ruum muutub laialdasemalt kasutatavaks, väheneb tõenäoliselt NAT-i roll, kuigi ühilduvuse ja kontrolli eesmärgil kasutatakse seda mõnes keskkonnas endiselt liikluse segmenteerimiseks ja filtreerimiseks.


### NAT-i rakendamine


Address tõlke nõuetekohase toimimise tagamiseks peab NAT-ruuter või -värav pidama täpset arvestust iga sisevõrgu privaatse Address ja välismaailmaga suhtlemiseks kasutatava avaliku Address vahel loodud kaardistuste kohta. See teave salvestatakse nn NAT-tõlketabelisse, millel on keskne roll võrguliikluse haldamisel.


Iga kirje selles tabelis seob vähemalt ühe paari: saatva masina sisemine IP Address ja väline IP Address, mis on Internetis avatud. Kui eravõrgust saadetakse pakett avalikku sihtkohta, siis NAT-marsruuter võtab kaadri kinni, analüüsib IP- ja TCP/UDP-pealkirju ning asendab seejärel eralähte Address värava avaliku Address-ga. Tagasiteel võtab sama värav kinni sissetuleva paketi, kontrollib vastavustabelit ja sooritab pöördoperatsiooni, et suunata voog ümber algsele sisemisele IP Address-le.


See dünaamilise tõlkimise põhimõte tugineb täpsele tabelihaldusele: iga kirje jääb kehtima seni, kuni on olemas aktiivne liiklus, mis seda õigustab. Pärast konfigureeritavat tegevusetuse perioodi kustutatakse kirje ja seda saab uuesti kasutada uute ühenduste jaoks.


näide lihtsustatud NAT-tõlketabelist:_


| Internal IP   | External IP    | Duration (sec) | Reusable? |
| ------------- | -------------- | -------------- | --------- |
| 10.101.10.20  | 193.48.100.174 | 1,200          | no        |
| 10.100.54.251 | 193.48.101.8   | 3,601          | yes       |
| 10.100.0.89   | 193.48.100.46  | 0              | no        |

Selles näites, kui teise kirje puhul ei ole üle tunni aja (3600 sekundit) ükski pakett läbinud, märgitakse see korduvkasutatavaks. Seevastu kestus null tähistab aktiivset sidet, mille kaardistus on lukustatud.


Kuigi NAT toimib enamiku tavapäraste kasutusviiside puhul (veebilehitsemine, e-post, failide edastamine jne) läbipaistvalt, võib see tekitada lisaprobleeme teatavate võrgurakenduste puhul. Mõned tehnoloogiad tuginevad IP-aadresside või portide selgesõnalisele vahetamisele paketi kasulikus koormuses. Pärast NAT-värava läbimist muutub see teave ebajärjekindlaks.


Tüüpilised näited piirangute kohta on järgmised:


- Peer-to-peer protokollid (P2P), mis nõuavad otseseid ühendusi seadmete vahel, on takistatud NAT-barjääriga, kuna kõik sisemised masinad jagavad sama välise IP Address ja neid ei saa otse kätte ilma spetsiaalse konfiguratsioonita (näiteks *port forwarding* või UPnP);
- IPSec-protokoll, mida kasutatakse võrguside kaitsmiseks, krüpteerib pakettide päised. Kuna NAT peab neid päiseid muutma, et asendada IP-aadressid, muudab krüpteerimine selle võimatuks ilma kohandamismehhanismideta nagu NAT-T (*NAT Traversal*);
- X Window protokoll, mis võimaldab graafiliste rakenduste kaugnäitamist Unix/Linuxis, töötab nii, et X-server saadab aktiivselt TCP-ühendusi klientidele. Seda ühenduste tavapärase suuna ümberpööramist võib blokeerida NAT.


Üldiselt mõjutab see kõiki protokolle, mis sisaldavad paketi kasuliku koormuse sees olevat IP Address, kuna see Address ei vasta pärast tõlkimist enam tegelikule, internetis nähtavale Address-le.


**Tähtis märkus:** Address jaoks pakuvad mõned NAT-ruuterid _Deep Packet Inspection_ (DPI) või _Protocol Helpers_ , mis kontrollivad pakettide sisu, et tuvastada ja dünaamiliselt asendada aadressid või portnumbrid rakendusandmetes. See nõuab protokolliformaadi põhjalikku tundmist ja võib tekitada turvaauke või suurendada ressursikasutust.


**Ohutus:** Kuigi NAT aitab varjata sisevõrku ja kontrollida sissetulevat liiklust, ei asenda see spetsiaalset tulemüüri. Tõlkimine üksi ei ole täielik turvatõke: seda tuleb alati täiendada selgete filtreerimisreeglitega, et blokeerida soovimatu või soovimatu liiklus.


selle praktilise toimimise näitlikustamiseks võib tuua järgmise näite:_



![Image](assets/fr/037.webp)



Selle stsenaariumi puhul saab sisemine tööjaam siseneda sisemisele veebiserverile lihtsalt URL-i "http://192.168.1.20:80" kutsudes. Pordi määramine on siinkohal vabatahtlik, sest `80` on standardne HTTP-port. seevastu kui päring algatatakse väljastpoolt, sisestab kasutaja avaliku Address `http://85.152.44.14:80`. NAT-ruuter võtab päringu vastu, konsulteerib oma kaardistamistabeliga ja tõlgib avaliku Address automaatselt privaatseks, suunates ühenduse ümber `http://192.168.1.20:80`.


Sama põhimõte kehtib ka kõigi teiste serverite kohta, millel on õigus võtta vastu internetiühendusi, näiteks Extraneti server (sinine vooluahel joonisel).


**Praktiline märkus:** Virtualiseeritud keskkondades kasutatakse tavaliselt võrguliideseid nimega _virbrX_ (tähistab _Virtual Bridge X_). Need virtuaalsillad, mida pakub eelkõige libvirt raamatukogu või Xen hüperviisor, ühendavad külalismasinate virtuaalse sisevõrgu füüsilise võrguga, rakendades samal ajal NAT-i. Neid konfigureeritakse tavaliselt skriptide abil failis `/etc/sysconfig/network-scripts/`, nagu on näidatud allpool `virbr0` puhul:


```ini
NAME=""
BOOTPROTO=none
MACADDR=""
TYPE=Bridge
DEVICE=virbr0
NETMASK=255.255.255.0
MTU=""
BROADCAST=192.168.0.255
IPADDR=192.168.0.1
NETWORK=192.168.0.0
ONBOOT=yes
```


Kui virtuaalne sild on paigas, tuleb teil lubada IP marsruutimine ja konfigureerida portitõlge `iptables`iga:


```shell
echo 1 > /proc/sys/net/ipv4/ip_forward
```


```shell
iptables -t nat -A POSTROUTING -o <WAN> -s 192.168.0.0/24 -j MASQUERADE
```


Selle konfiguratsiooni puhul suunatakse väljaminev liiklus ja rakendatakse NAT-tõlget, mis võimaldab virtuaalmasinatel suhelda välismaailmaga, ilma et nende sisemised IP-aadressid oleksid otseselt avatud.


Järgmises peatükis vaatleme üksikasjalikult IP Address konfigureerimist Linuxi all, käsitledes nii lihtsaid kui ka täiustatud meetodeid, mis sobivad erinevatele halduskontekstidele.



https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864


## Kuidas konfigureerida võrku koos `ip`ga?


<chapterId>8ba7e946-d2a0-4841-8d54-e85ba96baa25</chapterId>



### Standardne konfiguratsioon


Pärast võrgu loomise teoreetiliste aluste käsitlemist ja arusaamist, kuidas IP-aadressid, maskid, marsruutimine ja tõlkimine koos toimivad, on aeg liikuda edasi praktilise konfigureerimise juurde. GNU/Linuxis toimub võrgu seadistamine nüüd käsuga **`ip`** (pakett _iproute2_), mis asendab vanema käsu `ifconfig`.


`ip` võimaldab määrata või muuta IP Address, muuta maski, käivitada või peatada Interface või kontrollida selle olekut igal ajal.


**TIPS:** kõigi liideste (aktiivsete või mitteaktiivsete) kuvamiseks: `ip addr show`


Näide: staatilise Address määramine ja Interface aktiveerimine


Lisa Address `192.168.1.2/24` Interface `eth0` juurde:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Aktiveerige Interface:


```shell
ip link set dev eth0 up
```


Deaktiveerige sama Interface:


```shell
ip link set dev eth0 down
```


Näitab konkreetse Interface staatust:


```shell
ip addr show dev eth2
```


**Praktiline näpunäide:** koos `ip`ga ei nõua täiendava Address lisamine Interface-le enam järelliidet `:1`. Lihtsalt lisage veel üks rida `ip addr add ...`:


```shell
ip addr add 172.18.2.39/24 dev eth2
```


### Aktiveerimisskriptid: ifup / ifdown


Utiliidid `ifup` ja `ifdown` loevad staatilisi konfiguratsioonifaile failidest `/etc/sysconfig/network-scripts/` (RHEL, CentOS, Rocky Linux, AlmaLinux...) või `/etc/network/interfaces` (Debian/Ubuntu), et liidesed puhtalt üles või alla viia.


```shell
ifup eth1
ifdown eth2
```


Konfiguratsioonifailid (RHEL-taolised):


- /etc/sysconfig/network**: globaalsed seaded (NETWORKING, HOSTNAME, GATEWAY...).
- ifcfg-**: igale Interface-le omased seaded.


Staatiline näide (ifcfg-eth0):


```ini
DEVICE=eth0
BOOTPROTO=none
ONBOOT=yes
IPADDR=192.168.2.5
NETMASK=255.255.255.0
GATEWAY=192.168.2.1
```


DHCP näide:


```ini
DEVICE=eth0
BOOTPROTO=dhcp
ONBOOT=yes
```


See moodulstruktuur on endiselt kehtiv ja seda saab praegustes süsteemides hõlpsasti automatiseerida.


### Täiustatud konfiguratsioon: sidumine


Professionaalsetes keskkondades on eesmärk tagada teenuse järjepidevus ja/või koondada ribalaiust. *Bonding* (või *teaming* koos _teamd_ga) mehhanismid vastavad nendele vajadustele: mitu füüsilist liidest toimivad ühe loogilise Interface-na, mida sageli nimetatakse `bond0` või `team0`.



![Image](assets/fr/039.webp)



Eeltingimused:


- Laadige moodul `bonding` (või kasutage `teamd`) ;
- Vähemalt kaks füüsilist liideseid peab olema saadaval.


#### Erinevad üldkasutatavad liimimismeetodid:


|Mode|Name|Principle|
|---|---|---|
|0|balance-rr|Round-robin, cyclic distribution of frames|
|1|active-backup|Single active interface with hot failover |
|2|balance-xor|Selection based on XOR of src/dst MAC addresses|
|3|broadcast|Broadcast simultaneously on all interfaces   |
|4|802.3ad (LACP)|Standardized dynamic aggregation; requires compatible switch|
|5|tlb (Transmit Load Balancing)|Balancing based on transmit load|
|6|alb (Adaptive Load Balancing)|Adaptive balancing; also balances receive via ARP|

#### Seadistamine koos `ip link



- Lülitage füüsilised liidesed välja:


```shell
ip link set eth0 down
ip link set eth1 down
```



- Loo liimitud Interface:


```shell
ip link add bond0 type bond mode balance-alb
```



- Konfigureeri valikud pärast loomist


```shell
ip link set bond0 type bond miimon 100
```



- Määrake MAC- ja IP-aadressid:


```shell
ip link set dev bond0 address 00:17:56:BC:02:3A
ip addr add 192.168.2.3/24 dev bond0
ip route add default via 192.168.2.1
```



- Kinnitage orjapoolsed liidesed:


```shell
ip link set eth0 master bond0
ip link set eth1 master bond0
```



- Tooge kõik tagasi üles:


```shell
ip link set bond0 up
ip link set eth0 up
ip link set eth1 up
```


**Vihje:** orja lahutamine ilma sidet katkestamata: `ip link set eth1 nomaster`


#### Püsikonfiguratsioon (RHEL-taoline)


Looge kolm faili failis `/etc/sysconfig/network-scripts`:


_ifcfg-bond0_


```ini
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=none
IPADDR=192.168.2.3
NETMASK=255.255.255.0
BROADCAST=192.168.2.255
GATEWAY=192.168.2.1
BONDING_OPTS="mode=balance-alb miimon=100"
```


_ifcfg-eth0_


```ini
DEVICE=eth0
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```


_ifcfg-eth1_


```ini
DEVICE=eth1
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```


Siis:


```shell
systemctl restart network
```


#### Täiendav IP Address (kaasaegne varjunimi)


IP-ga saate lihtsalt lisada teise Address samale seadmele:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Et see alias pärast taaskäivitust püsivaks muuta, lisage kas teine `IPADDR2=...` / `PREFIX2=...` plokk `ifcfg-eth0`-le või looge uus *NetworkManager* ühendus `nmcli` kaudu.


Tänu `ip` ja sellega seotud käskudele (`ip link`, `ip addr`, `ip route`) on võrgu konfigureerimine järjepidevam, skriptitavam ja selgem. Sidumine on kõrge käideldavusega arhitektuuride võtmekomponent ja mitme aadressi määramine ühele Interface-le on muutunud palju lihtsamaks.


Järgmises peatükis vaatleme IPv6-aadressimise eripärasid ja rakendamist.


# IPv6-aadressimine


<partId>9b1d87f1-2a68-496e-b5dd-76cf74fb8cde</partId>


## IPv6: standardid ja määratlused


<chapterId>d1f16f0a-1104-460d-8d67-f725665f8e3f</chapterId>



Nüüd liigume järgmise põlvkonna IP-aadresside juurde: IPv6-protokoll, mida algselt tunti IPng (_IP Next Generation_) nime all. See protokoll, mis on loodud IPv4 struktuuriliste piirangute ületamiseks, toob kaasa märkimisväärselt laiendatud aadressiarhitektuuri ja arvukad tehnilised optimeerimised.


IPv6 kasutuselevõtu motiivid on erinevad ja Address on interneti arengu jaoks kriitilise tähtsusega. Esiteks on IPv6 roll toetada ühendatud seadmete arvu eksponentsiaalset kasvu (eesmärk, mida IPv4 piiratud Address ruumi puhul ei ole võimalik saavutada). Teiseks on protokolli eesmärk vähendada marsruutimistabelite suurust, muutes teabevahetuse tõhusamaks ja vähendades pikemas perspektiivis marsruuterite töökoormust.


IPv6 eesmärk on ka lihtsustada pakettide käitlemise teatavaid aspekte, parandada andmevooge ja optimeerida võrkudevahelist ülekandekiirust. Turvalisuse seisukohast on *IPsec*-protokolli AH/ESP päised lisatud põhispetsifikatsiooni ja kõik IPv6-sõlmed peavad neid toetama (RFC 6434). Nende kasutamine jääb siiski vabatahtlikuks: administraator peab neid sõltuvalt kontekstist lubama.


Muud eesmärgid hõlmavad teenusetüüpide täpsemat käsitlemist, eelkõige parema kvaliteedi tagamiseks reaalajas kasutatavate rakenduste (VoIP, videokonverentsid jne) puhul. IPv6 on kavandatud ka selleks, et võimaldada paindlikumat liikuvuse haldamist: seade võib vahetada juurdepääsupunkte ilma Address muutmata, mis on nähtav tema kolleegidele.


Lõpuks on IPv6 kavandatud koos eksisteerima koos vanade protokollidega. Kuigi see ei ole IPv4-ga otseselt binaarselt ühilduv, on see täielikult koostalitlusvõimeline kõrgema Layer protokollide, nagu TCP, UDP, ICMPv6 ja DNS, ning marsruutimisprotokollide, nagu OSPF ja BGP, suhtes, kui teatavad kohandused on tehtud. IPv6 kasutab multisaadetiste haldamiseks MLD (*Multicast Listener Discovery*) protokolli, mis on IPv4-keskkonna IGMP funktsionaalne ekvivalent.


### Märkimisreeglid


Üks olulisemaid muudatusi IPv6-s on IP Address enda vorming. Address kroonilise IPv4-aadresside nappuse tõttu on Address pikkust suurendatud 32 bitilt 128 bitile, seega 16 baidile. Teoreetiliselt annab see võimaliku Address ruumi:


$$3.4 \ korda 10^{38}$$$


See tagab praktiliselt piiramatu võimsuse kõikidele praegustele ja tulevastele seadmetele.


IPv6-aadressid kirjutatakse väga erinevalt tuttavast punktkomaalsest märkimisest. IPv6 Address koosneb kaheksast 16-bitisest rühmast, mis on kirjutatud heksadetsimaalselt ja eraldatud koolonitega `:`.


Näiteks:


```
1987:0c02:0000:84c2:0000:0000:cf2a:9077
```


Märkimise lihtsustamiseks võib igas rühmas juhtivad nullid ära jätta. Ülaltoodud näide muutub siis järgmiselt:


```
1987:c02:0:84c2:0:0:cf2a:9077
```


Lisaks sellele võib ühe pideva nullrühmade jada asendada::, mis lühendab Address veelgi:


```
1987:c02:0:84c2::cf2a:9077
```


**Hoiatus:** see reegel on range: ainult üks järjestikuste nullide jada võib asendada `::`ga. Kui Address sisaldab mitut nullikombinatsiooni, siis ainult pikim neist kondenseeritakse. See tagab nii unikaalsuse kui ka loetavuse.


**Täht `:`, mida kasutatakse kuueteistkümnendsete plokkide eraldamiseks, võib tekitada URL-ides ebaselgust, kuna `:` kasutatakse ka teenuse pordi tähistamiseks. Segaduse vältimiseks tuleb IPv6-aadressid URL-is lisada nurksulgudesse `[ ]`.


Näide HTTP-juurdepääsu kohta konkreetsele Address portile `2002:400:2A41:378::34A2:36`:


```
http://[2002:400:2A41:378::34A2:36]:8080
```


IPv4 Address esitamisel IPv6-kontekstis võib kasutada segatud märkimist punktiiriga kümnendmurdes, millele eelneb `::`:


```
::192.168.1.5
```


See ühilduvus aitab lihtsustada üleminekut kahe protokolli vahel, võimaldades IPv4 plokkide lisamist IPv6 Address ruumi.


** Märkus:** Aadresside kirjutamise standardiseerimiseks määratleb RFC 5952 kanoonilise formaadi koos lühendireeglitega, et vältida sama Address mitut esitust. Nende soovituste järgimine aitab vähendada vääritõlgendusi ja tagab järjepidevad võrgukonfiguratsioonid.


### IPv6 Address tüübid


IPv6 erineb oma eelkäijast mitmesuguste Address kategooriate poolest, millest igaüks on mõeldud konkreetsete kasutusviiside jaoks, võimaldades samas paindlikku marsruutimist ja võrguhaldust. Nagu IPv4 puhul, võivad aadressid olla globaalsed, kohalikud, reserveeritud või teatud üleminekumehhanismidele spetsiifilised.


Täpsustamata IPv6 Address on esitatud kujul `::` või täpsemalt `::0.0.0.0.0`. Seda erivormi kasutatakse Address hankimise ajal või vaikeväärtusena, et näidata Address puudumist.



| IPv6 Address Prefix | Description                                 |
| ------------------- | ------------------------------------------- |
|::/8                | Reserved addresses                          |
| 2000::/3            | Unicast addresses, routable on the Internet |
| fc00::/7            | Unique local addresses (1)                  |
| fe80::/10           | Link-local addresses                        |
| ff00::/8            | Multicast addresses                         |

(1): *Eralühenduses eelistatakse eelisliidet `fd00::/8` siseaadresside määramiseks, mis ei ole marsruutimisvõimalusega Internetis.*


#### Reserveeritud aadressid


Teatud IPv6 vahemikud on selgesõnaliselt reserveeritud ja neid ei tohi kasutada globaalsete aadressidena. Neil on konkreetne tehniline otstarve:


- `::/128`**: määratlemata Address, mida ei ole kunagi püsivalt seadmele määratud, kuid mida kasutab konfiguratsiooni ootav masin Address allikana.
- `::1/128`**: _loopback_ Address, mis on otsene vaste `127.0.0.1`-le IPv4-s, mis võimaldab masina Address-le ise.
- `64:ff9b::/96`**: Reserveeritud protokollide tõlkijatele, et võimaldada IPv4/IPv6 ühendamist, nagu on määratletud RFC 6052-s.
- `::ffff:0:0/96`**: ühilduvusplokk IPv4 Address esindamiseks konkreetses IPv6 struktuuris, mida rakendused kasutavad sageli sisemiselt.


Need plokid tagavad koostalitlusvõime ja hõlbustavad üleminekut kahe protokolli versiooni vahel.


#### Ülemaailmsed unicast-aadressid


Ülemaailmsed ühesaadete aadressid moodustavad suurema osa avalikult marsruutitavast IPv6-ruumist, mis moodustab umbes 1/8 Address-ruumist. Alates 1999. aastast on IANA eraldanud need plokid, näiteks eesliide `2001::/16`, CIDR-blokkidena (alates `/23` kuni `/12`) piirkondlikele registritele, mis seejärel jaotavad need edasi teenusepakkujatele ja organisatsioonidele.


Mõnel vahemikul on dokumenteeritud erikasutusviisid:


- `2001:2::/48`**: Reserveeritud jõudluse ja koostalitlusvõime testimiseks (RFC 5180).
- `2001:db8::/32`**: Reserveeritud dokumentatsiooni ja näidete jaoks (RFC 3849).
- `2002::/16`**: Kasutatakse 6to4-mehhanismi jaoks, mis võimaldab IPv6-liiklust IPv4-infrastruktuuri kaudu (kasulik üleminekufaasis kahe protokolli vahel).


**Märkus:** suur osa ülemaailmsetest aadressidest jääb kasutamata, mis on reserviks Interneti tulevase kasvu jaoks.


#### Unikaalsed kohalikud aadressid (ULA)


Unikaalsed kohalikud aadressid (`fc00::/7`) on IPv6 vaste IPv4 privaatsetele aadressidele (RFC1918). Need võimaldavad luua isoleeritud sisevõrke, ilma et tekiksid konfliktid avalike aadressidega. Tegelikkuses on tegelik prefiks `fd00::/8`, kusjuures 8. bitt on seatud 1, et näidata kohalikku kasutamist. Iga ULA-blokk sisaldab 40-bitist pseudosituatsioonilist identifikaatorit, mis minimeerib Address kokkupõrkeid eraldiseisvate privaatvõrkude ühendamisel.


#### Link-lokaalsed aadressid


Link-lokaalseid aadresse (`fe80::/64`) kasutatakse ainult sama Layer 2-segmendi (sama VLAN või switch) piires toimuvaks suhtluseks. Neid ei suunata kunagi kaugemale kohalikust lingist. Iga võrgu Interface genereerib automaatselt link-lokaalse Address, mis on sageli tuletatud tema MAC Address-st, kasutades EUI-64 skeemi.


**Eripärasus**: sama masin võib kasutada sama link-lokaalset Address mitmel liidesel, kuid Interface tuleb mitmetähenduslikkuse vältimiseks suhtlemisel täpsustada Interface.


#### Multisaateaadressid


IPv6s on eetrisse saatmine asendatud multisaatega, mis on tõhusam viis pakettide edastamiseks kindlaksmääratud vastuvõtjate rühmale. Multisaate vahemiku eesliide on `ff00::/8`. Need sisaldavad selliseid aadresse nagu `ff02::1`, mis on suunatud kõigile sõlmedele kohalikul lingil. Kuigi see Address on mugav, ei soovitata seda enam rakenduste jaoks, kuna see võib generate kontrollimatuid saateid saata.


Multisaate kasutamine on levinud _Neighbor Discovery Protocol_ (NDP), mis asendab IPv6-s ARP-i. NDP kasutab konkreetseid multisaateaadresse, näiteks `ff02::1:ff00:0/104`, et automaatselt leida teisi sama lingiga ühendatud hoste.


Kombineerides neid Address tüüpe, pakub IPv6 täielikku valikut, mis vastab globaalse marsruutimise, kohaliku side, IPv4/IPv6 ülemineku ja automaatse seadmekonfiguratsiooni vajadustele, parandades samal ajal edastamise tõhusust.


### Address reguleerimisala


IPv6 Address ulatus määrab kindlaks täpse domeeni, milles see on kehtiv ja ainulaadne. Selle kontseptsiooni mõistmine on IPv6-võrgu pakettide marsruutimise ja loogilise korralduse omandamise võti. IPv6-aadressid jagatakse üldiselt kolme põhikategooriasse, mis põhinevad nende ulatusel ja kasutusalal: unicast, anycast ja multicast.


**Unicast-aadressid** on kõige levinumad ja sisaldavad mitmeid erinevaid alatüüpe.

Nende hulka kuulub _loopback_ (`::1`) Address, mille ulatus on piiratud seda kasutava hostiga ja mida kasutatakse võrgupinu sisemiseks testimiseks ilma liiklust üle füüsilise võrgu saatmata.

Seejärel on olemas ling-lokaalsed aadressid (_link-local_), mille ulatus on piiratud ühe võrgusegmendiga: neid kasutatakse otseseks suhtluseks sama füüsilise või loogilise ühenduse (nt ühe kommutaatori või VLANi) seadmete vahel.

Lõpuks, unikaalsed kohalikud aadressid (_ULA_, mis tähendab _Unique Local Addresses_) on eravõrgu sisemised aadressid. Neid võib suunata mitme erasektori segmendi vahel, kuid need ei ole kunagi nähtavad Internetis.


Kontseptuaalselt esitatakse IPv6-aadressid sageli binaarse struktuurina, mille esimene pool (esimesed 64 bitti) tähistab võrgu eesliidet ja teine pool (samuti 64 bitti) tähistab üheselt seadme Interface selles võrgus. Selline jagunemine lihtsustab Address autokonfigureerimist selliste mehhanismide abil nagu SLAAC (_Stateless Address Autoconfiguration_), mis võimaldavad masinatel automaatselt generate stabiilset Address MAC Address või pseudosituatsioonilise identifikaatori alusel.


| Field     | Prefix | L | Global ID | Subnet | Interface ID |
|-----------|--------|---|-----------|--------|---------------|
| Bits      | 7      | 1 | 40        | 16     | 64            |

IPv6 arhitektuur järgib tänase Interneti hierarhilist globaalse marsruutimise mudelit. Prefiksite jaotamine võimaldab piirkondlikel registritel ja võrguoperaatoritel hallata Address jaotamist detsentraliseeritult, tagades samas ülemaailmse unikaalsuse. Selles raamistikus võib üks ja sama host omada samaaegselt globaalset üheaadressi Address Interneti-suhtluseks ja link-lokaalset Address kohalikuks suhtluseks, nt vahetu naabruskonnaga või marsruuteri avastamissõnumite jaoks.


| Field     | Prefix | Zero | Interface ID |
|-----------|--------|------|--------------|
| Bits      | 10     | 54   | 64           |

**Anycast-aadressid** kujutavad endast vahepealset kontseptsiooni, mis põhineb unicast-mudelil, kuid võib teatud juhtudel käituda nagu multicast. Anycast Address on sisuliselt unicast Address, mis on määratud mitmele eri võrgusõlmedesse jaotatud liidesele. Kui pakett saadetakse anycast Address-le, püüab IPv6-protokoll edastada selle ühele seda Address jagavale hostile, mis on tavaliselt marsruutimistopoloogia poolest kõige lähemal. Selline lähenemisviis optimeerib päringute töötlemise kiirust ja parandab hajutatud teenuste vastupidavust. Klassikaline näide on juur-DNS-serverid, kus anycast-aadressimine suunab päringud automaatselt lähimale kohalolekupunktile.



| Field     | Prefix | Subnet | Interface ID |
|-----------|--------|--------|--------------|
| Bits      | 48     | 16     | 64           |

IPv6s asendavad **multisaateaadressid** ringhäälingumehhanismi, mida peeti liiga kulukaks ja ülemaailmsete võrkude jaoks ebasobivaks. Multisaate Address identifitseerib grupi liideseid, tavaliselt mitme hosti vahel, mis soovivad saada samu pakette samaaegselt.

Iga multisaadetise Address sisaldab spetsiaalset 4-bitist _scope_-välja, mis määratleb ülekande geograafilise või loogilise piiri:


- Ulatus `1` tähendab, et pakett on mõeldud ainult kohalikule seadmele.
- Mõiste "2" piirab paketi kohalikule lingile: kõik seadmed samas füüsilises või virtuaalses segmendis saavad seda vastu võtta.
- Ulatus "5" laiendab ulatust saiti, tavaliselt kogu ettevõtte võrku.
- Ulatus "8" laiendab organisatsiooni ulatust, võimaldades edastamist kõigis sama üksuse alamvõrkudes.
- Ulatus "e" (14 kuueteistkümnendsüsteemis) tähistab globaalset ulatust, mis teeb multisaatmisrühma kättesaadavaks kõikjal Internetis, kui marsruutimisinfrastruktuur seda toetab.


IPv6 multisaate Address struktuur hõlmab järgmist:


- väli _Flag_ (4 bitti) määrab, kas rühm on alaline või ajutine,
- väli _Scope_ (4 bitti) määrab ulatuse,
- identifitseerimisväli (112 bitti), mis identifitseerib multisaadete grupi numbri.


| Field      | Prefix | Flags | Scope | Group ID |
|------------|--------|--------|--------|----------|
| Bits       | 8      | 4      | 4      | 112      |

Tuntud näide IPv6 multisaadetiste toimimisest on _Neighbor Discovery Protocol_ (NDP). Selle asemel, et kasutada ARP-d nagu IPv4-s, kasutab NDP naabrite avastamise päringute edastamiseks multisaateaadresse, näiteks `ff02::1:ff00:0/104`, mis on suunatud ainult asjaomastele hostidele samal lingil.


Address ulatuse nii täpse määratlemise kaudu struktureerib IPv6, kuidas andmevooge saadetakse, võetakse vastu ja suunatakse. Selline granulaarsus muudab protokolli paindlikumaks ja tõhusamaks nii kohaliku kui ka globaalse side haldamisel, vältides samal ajal üldistatud ringhäälinguga kaasnevaid puudusi.


## Address Assignment kohalikus võrgus


<chapterId>4c9c3e52-59bc-499a-af0a-6dd369a9e029</chapterId>


Selles peatükis vaatleme IPv6 kasutuselevõtu üht kõige praktilisemat aspekti: IP-aadresside määramine kohalikus võrgus asuvatele hostidele. IPv6-arhitektuur on kavandatud paindlikuks, võimaldades igale seadmele generate oma Address automaatselt, võimaldades samas vajaduse korral täielikult käsitsi konfigureerimist.


IPv6-lokaalvõrk jagab Address süstemaatiliselt kaheks osaks:


- esimesed 64 bitti tähistavad alamvõrgu eesliidet, mille tavaliselt annab marsruuter või Address asutus;
- ülejäänud 64 bitti kasutab vastuvõtja enda unikaalseks identifitseerimiseks kõnealuses segmendis.

See mudel lihtsustab oluliselt marsruutide koondamist ja Address plokkide haldamist.


Seadmetele aadresside määramiseks kasutatakse kahte peamist lähenemisviisi:


- Käsitsi konfigureerimine, kus administraator määrab iga Interface täpse Address;
- Automaatne konfigureerimine, kus seadmed generate või saavad oma aadressid dünaamiliselt.


Käsitsi konfigureerimise korral määrab administraator igale Interface-le täieliku IPv6 Address. Teatud väärtused jäävad reserveerituks:


- `::/128`: määratlemata Address, ei ole kunagi püsivalt määratud ;
- `::1/128`: loopback Address (_loopback_), IPv4-ekvivalent: `127.0.0.1`.


Erinevalt IPv4-st puudub _broadcast_ mõiste; "kõik nullid" või "kõik üksikud" kombinatsioonid host-osas ei oma erilist tähendust.

Käsitsi konfigureerimine on kontrollitud keskkonnas endiselt kasulik, kuid seda on raske säilitada mastaabis.


Automaatseks konfigureerimiseks on olemas mitu meetodit:


- **NDP** (_Neighbor Discovery Protocol_) protokoll, mis on määratletud RFC4862-s, võimaldab *stateless* automaatset konfigureerimist. Selles režiimis saab host võrgu eesliite kohalikult marsruuterilt ja täiendab Address ise oma MAC Address identifikaatoril põhineva identifikaatoriga. Seda meetodit on lihtne kasutusele võtta ja see ei nõua keskset serverit.
- Rakendused, nagu need, mis on kasutusel Windowsis, võivad generate vastuvõtva osa pseudosituatiivselt parandada privaatsust, vältides MAC Address otsest paljastamist. MAC Address paljastamine IPv6-pakettides võib tekitada probleeme privaatsusega, kuna see võimaldab seadme jälgimist erinevates võrkudes.
- DHCPv6 protokoll: See on määratletud RFC3315-s ja sarnaneb IPv4 puhul kasutatavale DHCP-le, kuid võimaldab rohkem kontrollitud ja tsentraliseeritud konfigureerimist, sealhulgas üürilepingute haldamist, lisavõimalusi (DNS, MTU...) ja andmebaaside registreerimist. DHCPv6 võib toimida üksi või koos staatilise konfigureerimisega, et pakkuda lisaparameetreid ilma IP Address ise määramata.


**Tähtis märkus:** MAC-põhise meetodi puhul teisendatakse MAC Address 64-bitiseks identifikaatoriks, kasutades EUI-64 formaati. See mehhanism lisab algse MAC Address (48-bitise) keskele baitid `FF:FE` ja inverteerib 7. biti, et näidata globaalset unikaalsust. Tulemuseks on stabiilne Interface identifikaator, mida kasutatakse täielikus IPv6 Address-s.


Siin on näide, kuidas muuta MAC Address EUI-64-ks:


![Image](assets/fr/045.webp)



Seadmete jälgimise üle kasvava mure tõttu lubavad kaasaegsed operatsioonisüsteemid (eelkõige Linux, Windows 10+, macOS, Android) nüüd siiski vaikimisi privaatsuse laiendusi. Need kasutavad juhuslikult genereeritud Interface identifikaatoreid, mida perioodiliselt uuendatakse väljaminevate ühenduste puhul, säilitades samal ajal stabiilse identifikaatori siseside jaoks (näiteks DNS või DHCPv6).


Nagu IPv4-i DHCP puhul, võib automaatselt määratud IPv6-aadressidel olla kaks kasutusiga, mille määravad DHCPv6-ruuterid või -serverid:


- Eelistatud eluiga*: pärast seda perioodi jääb Address kehtima, kuid seda ei kasutata enam uute ühenduste algatamiseks;
- Kehtiv eluiga*: kui see aeg lõpeb, eemaldatakse Address täielikult Interface konfiguratsioonist.


See süsteem võimaldab dünaamiliselt hallata võrgumuutusi, näiteks tagada sujuv üleminek ühelt Interneti-teenuse pakkujalt teisele. Uuendades marsruuterite poolt teatatud eesliidet ja kohandades paralleelselt DNS-kirjeid, saab IPv6-le üleminekut teostada ilma teenuse märgatava katkestuseta.


**Tipp:** Address ja DNS-i elutsüklite kombineeritud kasutamine võimaldab rakendada järkjärgulist üleminekustrateegiat, kus uued ühendused liiguvad uude topoloogiasse, samas kui olemasolevad ühendused jätkuvad kuni nende loomuliku lõpuni.


Lühidalt öeldes pakub IPv6 Address Assignment jaoks suurt paindlikkust: käsitsi konfigureerimine, staatiline või staatiline automaatne konfigureerimine, DHCPv6 või juhuslik genereerimine. Igal lähenemisviisil on oma eelised ja piirangud ning seda saab kohandada vastavalt nõutavale kontrollitasemele, võrgu suurusele või privaatsusvajadustele.


## IPv6 Address plokkide määramine


<chapterId>45cce866-1b58-4888-b3fe-15c922180839</chapterId>


### Address levitamine


IPv6 Address jaotusskeem on üles ehitatud nii, et see vastaks kahele eesmärgile: tagada globaalne Address unikaalsus ja võimaldada loogilist hierarhiat, mis soodustab marsruutimistabelite koondamist ja lihtsustamist.

Nagu IPv4 puhul, asub selle hierarhia tipus *Internet Assigned Numbers Authority* (IANA). Ta haldab globaalset Address ruumi ja delegeerib Address plokid viiele piirkondlikule internetiregistrile (_RIR_).


Viis olemasolevat RIRi on järgmised:


- ARIN (Põhja-Ameerika),
- RIPE NCC (Euroopa, Lähis-Ida, Kesk-Aasia),
- APNIC (Aasia ja Vaikse ookeani piirkond),
- AFRINIC (Aafrika),
- LACNIC (Ladina-Ameerika ja Kariibi mere piirkond).


IANA eraldab igale RIRile erineva suurusega IPv6-blokid, mis jäävad tavaliselt vahemikku /23 ja /12. Selline lähenemisviis pakub paindlikkust, tagades samas pikaajalise skaleeritavuse. RIRid omakorda jaotavad need plokid ümber Interneti-teenuse pakkujatele, suurtele ettevõtetele ja avalik-õiguslikele asutustele.


Alates 2006. aastast on iga RIR saanud IANA-lt IPv6 /12 ploki, mis on fikseeritud suurusega, et tagada stabiilne ja piisavalt suur reserv tulevase kasvu jaoks. RIRid jagavad need tavaliselt /23, /26 või /29 plokkideks. ISPd saavad kõige sagedamini /32 plokke, kuigi see suurus võib sõltuvalt ISP suurusest ja geograafilisest piirkonnast varieeruda. Tavaliselt eraldavad nad klientidele /48 plokke. Iga /48 annab 65 536 erinevat /64 alamvõrku (tohutu maht võrreldes IPv4-ga).


**Tähtis märkus:** /32 plokk sisaldab täpselt 65,536 /48 alamplokki. See tähendab, et iga ISP saab teenindada kümneid tuhandeid kliente, ilma et nende eraldis ammenduks. Tänu oma /48-le on siis igal kliendil hiiglaslik ruum, et struktureerida oma sisevõrku nii paljude /64 segmentidega, kui ta soovib.


Tüüpiline jaotamise hierarhia näeb välja järgmiselt:


| IANA | RIR | LIR | Customer | Subnet | Interface |
|------|-----|-----|----------|--------|-----------|
|  3   | 20  |  9  |    16    |   16   |     64    |

Sellise aadresside rohkuse tõttu ei ole NAT (*Network Address Translation*), mis oli kunagi IPv4-s hädavajalik, et tulla toime Address puudusega, enam vajalik. Igal hostil võib olla unikaalne, globaalselt marsruutitav avalik Address, mis lihtsustab otsest ühenduvust ja lihtsustab selliste protokollide nagu IPSec, VoIP või sissetulevate ühenduste kasutamist.


Et kontrollida, millisele organisatsioonile IPv6 Address kuulub, saate kasutada käsku `whois`, et teha päring avalike RIR-andmebaaside kohta. See läbipaistvus võimaldab tuvastada organisatsiooni, kellele eesliide kuulub, mis võib olla kasulik võrgu-, analüüsi- või turvalisuse eesmärgil.


### PA vs PI adresseerimine


Algselt põhines IPv6 jaotamise mudel ainult PA (*Provider Aggregatable*) plokkidel, mis tähendab, et see on seotud ISPga. Selle mudeli puhul saab organisatsioon oma prefiksi oma ISP-lt, mis tähendab, et teenusepakkuja vahetamine nõuab kogu infrastruktuuri ümber nummerdamist.


Kuigi IPv6 automaatse konfigureerimise funktsioonid ja Address kasutusiga muudavad ümbernumereerimise lihtsamaks, on see endiselt ebamugav organisatsioonidele, kellel on kriitiline infrastruktuur või mitu teenusepakkuja ühendust, mis on vajalikud koondamise jaoks.


Alates 2009. aastast on jaotuspõhimõtted võimaldanud PI (*Provider Independent*) plokke. Need plokid (üldjuhul /48 suurusega) eraldatakse otse ettevõttele või asutusele RIRi poolt, sõltumata mis tahes ISPst. See mudel sobib eriti hästi organisatsioonidele, kes praktiseerivad *multihoming'i* (st on ühendatud mitme operaatoriga samaaegselt). Näiteks Euroopas kirjeldab RIPE-512 PI eraldamise poliitikat.


### Subvõrgu maski märkimine


Nagu IPv4 puhul, kasutatakse ka IPv6 puhul CIDRi (*Classless Inter-Domain Routing*). See seisneb selles, et pärast Address märgitakse eesliite moodustavate bittide arv, kasutades selleks märki `/`.


Võtame järgmise näite:


```
2001:db8:1:1a0::/59
```


See tähendab, et esimesed 59 bitti on fikseeritud ja identifitseerivad võrgu. Kõiki ülejäänud bitte (siin 69 bitti) saab kasutada alamvõrkude või hostide identifitseerimiseks.


Seega hõlmab see tähendus aadressid alates `2001:db8:1:1a0:0:0:0:0:0:0` kuni `2001:db8:1:1bf:ffff:ffff:ffff:ffff:ffff`.


See plokk hõlmab seega 8 /64 alamvõrku, millest igaüks suudab majutada suurt arvu seadmeid.


CIDR-märgistus võimaldab täpset Address ruumi planeerimist, alates suuremahulistest võrkudest kuni koduste seadistuste ja virtualiseeritud keskkondadeni, ning soodustab marsruutide koondamist, vähendades marsruuterite koormust ja parandades skaleeritavust.


### IPv6 paketid ja päised


IPv6 pakettide formaat erineb IPv4-st selle poolest, et see on lihtsam ja laiendatavam. IPv6 andmeprogramm algab alati 40 baidi suuruse fikseeritud suurusega päisega, mis sisaldab kogu olulist marsruutimisalast teavet. Selline lihtsustatud lähenemisviis võrreldes IPv4-i muutuva pikkusega päisega (20 kuni 60 baiti) võimaldab marsruuteritel kiiremini ja tõhusamalt pakette töödelda.


IPv6 ei eemalda siiski funktsionaalsust: selle asemel, et integreerida arvukalt valikulisi välju põhipealkirja, võetakse kasutusele laienduste süsteem, mis paigutatakse kohe pärast põhipealkirja. Need valikulised päised võimaldavad lisada teatud funktsioonidele spetsiifilisi andmeid või juhiseid, koormamata tarbetult tavalisi pakette.


Mõned laienduste päised järgivad kindlat struktuuri, samas kui teised võivad sisaldada muutuvat arvu valikuid. Need valikud on kodeeritud kui `{Tüüp, pikkus, väärtus}` kolmikud:


- Väli "Type" (1 bait) näitab valiku olemust;
- "Tüübi" kaks esimest bitti määravad, mida marsruuterid peaksid tegema, kui valik ei ole tuvastatud:
 - Ignoreerige seda valikut ja jätkake ravi,
 - Andmesõnum jäetakse välja,
 - Katkestab ja saadab ICMP-vea allikale.
 - Andmesidepaketi katkestamine ilma teavitamata (multisaate pakettide puhul).
- Väli "Length" (1 bait) määrab välja "Value" suuruse, mis on vahemikus 0 kuni 255 baiti;
- Väli "Väärtus" sisaldab valikuga seotud andmeid.


Siin on ülevaade erinevatest IPv6-s määratletud laienduste päistest.


#### Hop-by-Hop päis


See päis, kui see on olemas, paigutatakse alati kohe pärast põhipealkirja. See sisaldab teavet, mida peab töötlema iga marsruuter paketi teekonnal, erinevalt enamikust teistest päistest, mida tavaliselt töötleb ainult sihtkoht. Tüüpilised kasutusalad hõlmavad globaalsete parameetrite edastamist või konkreetsete töötlemisetappide taotlemist paketi liikumisel läbi võrgu.


![Image](assets/fr/047.webp)


#### Marsruudi päis


Marsruudi päises määratakse nimekiri vaheaadressidest, mida pakett peab läbima. On kaks peamist marsruutimisrežiimi:


- Range marsruutimine: täpne marsruut on ette määratud
- Lahtine marsruutimine: täpsustatud on ainult teatavad kohustuslikud sammud.


Selle juurdumispealkirja neli esimest välja on järgmised:


- Järgmine päis**: määrab järgmise päise tüübi;
- Marsruudi tüüp**: määrab marsruudi meetodi (tavaliselt "0");
- Allesjäänud segmendid**: läbimiseks jäänud segmentide arv ;
- Address[n]**: vahepealsete aadresside loetelu.


Väli "Segmendid jäänud" algab allesjäänud segmentide koguarvuga ja seda vähendatakse iga hüppega ühe võrra.


![Image](assets/fr/048.webp)


#### Fragmenteerimise päis


IPv6-s on ainult lähtekoha hostil lubatud datagrammi fragmenteerida, erinevalt IPv4-st, kus seda võisid teha ka marsruuterid. Kõik IPv6-sõlmed peavad olema võimelised töötlema vähemalt 1280 baidi suuruseid pakette. Kui marsruuter kohtab järgmise lingi MTU-st suuremat paketti, saadab ta *ICMPv6 Packet Too Big* teate tagasi allikale, kes seejärel kohandab oma ülekannete suurust.


Fragmenteerimise päis sisaldab järgmisi välju:


- Identification**: unikaalne datagrammi identifikaator uuesti kokkupanekuks.
- Fragment Offset**: fragmendi asukoht algses datagrammis.
- M flag**: näitab, kas järgneb rohkem fragmente.


![Image](assets/fr/049.webp)


#### Autentimispealkiri (AH)


Selle päise eesmärk on tagada side turvalisus, kontrollides nii saatja autentsust kui ka andmete terviklikkust. Seda kasutatakse tavaliselt koos IPsec-protokolliga. Autentimiskoodi abil saab vastuvõtja kinnitada, et sõnum on tõesti pärit oodatud saatjalt ja et seda ei ole transiidi käigus muudetud.


Pettusliku muutmiskatse korral ei vasta autentimiskood enam ja andmeprogramm võidakse tagasi lükata. See mehhanism kaitseb ka kordusrünnakute eest, tuvastades volitamata dubleerimisi.


![Image](assets/fr/050.webp)


#### Sihtkoha valikute päis


See päis on mõeldud ainult andmegrammi lõppsaajale. Seda võib kasutada rakendusele omaste valikute või metaandmete lisamiseks, ilma et vahepealsed marsruuterid seda arvesse võtaksid.


Algselt ei olnud sellist võimalust protokollis määratletud. See päis võeti siiski kasutusele IPv6 kavandamisel, et võimaldada tulevikus lisada laiendusi ilma paketi üldist struktuuri muutmata. Näiteks null-optsiooni kasutatakse ainult selleks, et täita päis 8 baidi mitmekordselt mälu joondamise eesmärgil.


![Image](assets/fr/051.webp)


IPv6-pakettide disain on üles ehitatud minimaalse baaspealkirja ja modulaarsete laienduspealkirjade selgel eraldamisel. Selline ülesehitus tagab nii standardse töötlemisjõudluse kui ka paindlikkuse, mis on vajalik protokolli arendamiseks ja turvalisuse, keerulise marsruutimise või teenuse kvaliteedi mehhanismide integreerimiseks, säilitades samas ühilduvuse tulevaste infrastruktuuridega.


## IPv6 ja DNS vaheline seos


<chapterId>421eacb8-b80b-4aee-910f-e069ed805f00</chapterId>


Kaasaegsetes võrkudes tõlgib DNS (*Domain Name System*) domeeninimed IP-aadressideks, mida masinad saavad kasutada. IPv6 kasutuselevõtuga pidi DNS kohanduma, et toetada 128-bitiseid aadresse, säilitades samal ajal tagasiulatuva ühilduvuse IPv4-ga. See kooseksisteerimine on eriti oluline kahestapilistes keskkondades, kus mõlemad IP-versioonid töötavad samaaegselt.


### IPv6-spetsiifilised DNS kirjed


Domeeninime seostamiseks IPv6 Address-ga kasutab DNS AAAA (*quad-A*) kirjet, mis on analoogne IPv4-aadresside A-kirjega. AAAA-kirje kaardistab domeeninime selgesõnaliselt IPv6 Address-le.

Näide:


```shell
ipv6.mydmn.org.         IN      AAAA    2001:66c:2a8:22::c100:68b
```


See kirje näitab, et domeen `ipv6.mydmn.org` lahendab IPv6 Address `2001:66c:2a8:22::c100:68b`. Sama domeeninime on võimalik ja maksimaalse ühilduvuse huvides isegi soovitatav seostada mitme IP-aadressiga, kas IPv4 (A-kirje kaudu) või IPv6 (AAAA-kirje kaudu). See võimaldab IPv6-ühilduvatel klientidel eelistada IPv6-i, tagades samal ajal, et ainult IPv4-ühilduvad kliendid jäävad toetatuks.


Lisaks sellele toetab DNS pöördlahendus, mis tähendab, et ta saab otsida antud IP Address-ga seotud domeeninime. IPv6 puhul kasutab see toiming PTR-kirjeid, mis on paigutatud tsooni "ip6.arpa". See tsoon on spetsiaalselt reserveeritud IPv6 pöördlahendusena. IPv4 puhul on see tsoon `in-addr.arpa`.


### Pööratud resolutsioon


IPv6 Address pöördlahendus järgib ranget protsessi:

1) Laiendage Address täisheksakohaliseks märkimiseks (16 baiti, st 32 heksakohalist numbrit).

Näide:


```shell
2001:66c:2a8:22::c100:68b
```


Saab:


```shell
2001:066c:02a8:0022:0000:0000:c100:068b
```


2) Pöörake iga heksadekaalarvu (nibble) järjekord ümber, eraldage need punktidega ja lisage `ip6.arpa`:


```shell
b.8.6.0.0.0.1.c.0.0.0.0.0.0.0.0.2.2.0.0.8.a.2.0.c.6.6.0.1.0.0.2.ip6.arpa  IN PTR  ipv6.mydmn.org
```


See struktuur tagab standardiseeritud, unikaalsed pöördotsingud IPv6 Address ruumis.


**Pöörake tähelepanu**: DNS päringud võivad liikuda kas IPv4 või IPv6 kaudu. Kasutatav transpordiprotokoll ei mõjuta tagastatavate kirjete tüüpi.

Näiteks:


- IPv6 kaudu ühendatud klient võib taotleda IPv4-kirjet.
- IPv4 kaudu ühendatud klient võib taotleda IPv6-kirjet.

DNS-server vastab lihtsalt oma kirjetega, olenemata päringu transpordiprotokollist.


Kui hostinimi on kaardistatud nii IPv4 kui ka IPv6-le, reguleerib valik, millist Address kasutada, RFC 6724, mis määratleb Address valiku algoritmi, mis põhineb sellistel teguritel nagu prefiksi eelistus, ulatus ja juurdepääsetavus. Vaikimisi eelistatakse üldiselt IPv6-i, kui süsteemi või võrgu konfiguratsioon ei ole seda välistanud.


**Tähtis meeldetuletus**: kui IPv6 Address sisestatakse URL-i (*Uniform Resource Locator*), peab see olema ümbritsetud nurksulgudes (`[]`). Sellega välditakse segadust IPv6 Address-sisese kooloni (`:`) ja URL-is hostinime ja pordi eraldava kooloni vahel.


Kehtiv näide:


```shell
http://[2001:db8::1]:8080
```


See tagab, et nii veebilehitsejad kui ka veebiserverid töötlevad URL-aadressi õigesti.


IPv6 integreerimine DNS-süsteemi sõltub seega uutest kirjetüüpidest, rangest pöördlahendusmeetodist ning täpsetest valiku- ja vormindusreeglitest, et tagada marsruutimise ühilduvus ja järjepidevus.


### Osa kokkuvõte


Selles jaotises uurisime IPv6-aadressimise aluspõhimõtteid. Alustasime IPv6 Address struktuuri uurimisega: selle 128-bitine pikkus, heksadekaalnumbriline märkimine ja lihtsustamisreeglid, mida kasutatakse korduvate nullide jadade lühendamiseks. Selline ülesehitus võimaldab IPv6-l ületada IPv4 Address ruumi piirangud, tagades samal ajal skaleeritavuse ja tõhusa hierarhia.


Seejärel vaatlesime IPv6-aadresside eri kategooriaid: unicast, anycast ja multicast, kirjeldades üksikasjalikult nende ulatust, tüüpilist kasutamist ja esindatust Address ruumis.


Seejärel vaatasime läbi IPv6-aadresside määramise meetodid kohalikus võrgus, kas käsitsi konfigureerimise, DHCPv6-protokolli kaudu või staatita automaatse konfigureerimise mehhanismide, näiteks NDP pakutavate mehhanismide abil. Need lähenemisviisid võimaldavad seadmetel automaatselt generate oma Address etteantud prefiksist ja nende MAC Address (EUI-64 kaudu), pakkudes samas paindlikkust eluea haldamise ja privaatsuse osas.


Oleme ka üksikasjalikult kirjeldanud, kuidas Address plokid jaotatakse, alustades IANA-st, kes jaotab need viiele RIR-ile (*registreeritud internetipiirkonnad*) ja seejärel Interneti-teenuste pakkujatele, kes jaotavad need oma klientidele alamvõrkudena (sageli /48, mis võimaldab 65536 /64 alamvõrku). Erinevus _Provider Aggregatable_ (PA) ja _Provider Independent_ (PI) plokkide vahel aitab hallata _multihoming_ või teenusepakkuja vahetamise stsenaariume.


Me nägime, et DNS on kohandunud IPv6-ga koos AAAA-kirje kasutuselevõtuga ja et pöördlahendusmehhanismid tuginevad nüüd tsoonile "ip6.arpa". Oluline on, et DNS jääb sõltumatuks kasutatavast transpordiprotokollist (IPv4 või IPv6), tagades sujuva koostalitlusvõime kahestapilises keskkonnas.


IPv6 ei ole seega mitte ainult IPv4-i täiendus, vaid aadressisüsteemi täielik ümberkujundamine, mis on loodud nii praeguse kui ka tulevaste globaalse Interneti väljakutsete lahendamiseks.


Selle NET 302 kursuse viimases osas liigume praktikasse ja keskendume võrgu diagnostikavahenditele.



# Võrgu diagnostikavahendid


<partId>368a5c6f-ec48-4b28-970f-3a770788ad37</partId>


## Võrgule juurdepääsu Layer tööriistad


<chapterId>1d25a21d-6900-4fbe-a438-e06c8afb9e02</chapterId>


Selles võrgudiagnostika viimase osa esimeses peatükis keskendume TCP/IP-mudeli Layer võrgule juurdepääsu analüüsimiseks mõeldud vahenditele. See Layer vastutab samas füüsilises võrgus olevate seadmete vahelise otsese suhtluse eest, eelkõige MAC-aadresside ja füüsiliste võrguliideste, näiteks Ethernet-kaartide või Wi-Fi liideste kasutamise kaudu.


Eesmärk on anda administraatoritele praktilised vahendid, et kontrollida, testida ja optimeerida seda olulist Layer madalatasemelist ühenduvust. Neid vahendeid saab kasutada liideste nõuetekohase toimimise kontrollimiseks, võrgukaartide konfiguratsiooniprobleemide kõrvaldamiseks või selliste kõrvalekallete nagu kokkupõrked, paketikadu või sidevigade avastamiseks.


### IP/MAC naabruskonna kommunaalteenused


#### `Arp` tööriist


Üks vanimaid diagnostikavahendeid Network Access Layer juures on käsk `arp`. Kuigi üha enam asendub kaasaegsete alternatiividega nagu `ip neigh` (mida me peagi avastame). `Arp` on ikka veel paljudes süsteemides olemas, et vaadata või manipuleerida ARP (*Address Resolution Protocol*) vahemälu. See vahemälu salvestab IP-aadresside ja MAC-aadresside vahelised seosed, mis on masinas kohapeal teada. Teisisõnu võimaldab see kindlaks teha, milline füüsiline (MAC) Address vastab antud IP Address-le kohalikus võrgus.


Praktikas, kui host soovib saata paketi samas alamvõrgus asuvale IP Address-le, peab ta kõigepealt teadma sihtmasina MAC Address. Seda seostamist teostab ARP, mis saadab päringu kohalikus võrgus ja saab vastuse, mis sisaldab vastavat MAC Address. See tulemus salvestatakse seejärel ajutiselt kohalikku tabelisse, mida nimetatakse "ARP vahemäluks", et vältida päringute kordamist iga uue paketi puhul.


Selle vahemälu sisu vaatamiseks ja masinale hetkel teadaolevate kirjete kontrollimiseks kasutage järgmist:


```bash
arp -a
```


See käsk loetleb kõik lokaalselt registreeritud IP/MAC-ühendused kõigis liidesedes. Igal real on esitatud hostinimi (kui see on lahendatav), IP Address, vastav MAC Address ja Interface, kus vastavust on täheldatud.


Kui soovite filtreerida ekraani konkreetse IP Address jaoks, siis lihtsalt määrake see:


```bash
arp -a 192.168.1.5
```


See võimaldab hõlpsasti kontrollida, kas konkreetne IP Address on vahemälus olemas, mis võib aidata diagnoosida kahe samas võrgus asuva hosti vahelisi kommunikatsioonihäireid.


Samamoodi, kui soovite kuvada ainult konkreetse võrgu Interface (näiteks Ethernet-kaardi nimega `eth0`) ARP-kirjeid, võite kasutada järgmist:


```bash
arp -a -i eth0
```


See on eriti kasulik mitme Interface keskkonnas (traadiga, traadita, VPN jne), kus ühel hostil võib olla mitu võrguadapterit.


Käsk `arp` ei ole piiratud ainult lugemisega. Seda saab kasutada ka ARP vahemälu käsitsi muutmiseks, mis on hindamatu funktsioon teatud edasijõudnud tõrkeotsingustsenaariumides või konkreetsete tingimuste simuleerimisel. Näiteks saab käsitsi lisada IP/MAC kaardistamise:


```bash
arp -s 192.168.1.7 00:17:BC:56:4F:25 -i eth2
```


See käsk loob staatilise kande kohalikku ARP-tabelisse, seostades IP Address `192.168.1.7` MAC Address `00:17:BC:56:4F:25` Interface `eth2`ga.Kui Interface ei ole määratud, kasutab süsteem automaatselt esimest sobivat Interface.


Saate ka kustutada kirje ARP vahemälust, kas vea parandamiseks või uuesti leidmiseks:


```bash
arp -d 192.168.1.7
```


Sellega kustutatakse kirje, tagades, et järgmine suhtluskatsetus käivitab uue ARP-päringu.


**MÄRKUS**: Kustutamisvalik võtab vastu ka Interface nime, mis võimaldab teil konkreetse kirje eemaldamist täpsemalt suunata.


Kokkuvõttes pakub tööriist `arp` madalatasemelist diagnostikat, mis on eriti kasulik kohalikes võrkudes, kus ühenduvusprobleeme saab sageli tagasi viia ebaõigele või vananenud Address resolutsioonile. Viimastel süsteemidel, eriti kaasaegsetes Linuxi distributsioonides, asendatakse see tööriist siiski üha enam käsuga `ip neigh`, mis kuulub tööriistakomplekti `iproute2`, mis pakub sarnast funktsionaalsust ühtsemas raamistikus.


#### `Ip neigh` tööriist


Kaasaegsetes süsteemides, eriti uuemates Linuxi distributsioonides, on käsk `ip neigh` IP- ja MAC-aadresside vaheliste seoste kontrollimiseks ja haldamiseks parim vahend. See käsk on osa `iproute2` paketist, mis on järk-järgult asendamas vanemaid vahendeid, nagu `arp`, pakkudes järjepidevamat ja paindlikumat raamistikku diagnostikaks andmesideliidese Layer juures.


Käsk `ip neigh` küsib kohalikku IP naabrite vahemälu, mis vastab IPv4 puhul ARP vahemälule ja IPv6 puhul NDP (_Neighbor Discovery Protocol_) vahemälule. See vahemälu salvestab teadaolevad seosed IP-aadresside (v4 või v6) ja MAC-aadresside vahel koos nende staatusega (kehtiv, ootel, aegunud...).


Põhiline käsk vahemälu kuvamiseks on:


```bash
ip neigh
```


See väljastab kirjete loetelu, mis näitab siht-IP Address, asjaomast võrku Interface, seotud MAC Address (kui see on olemas) ja kirje olekut (nt "Saabuv", "KÕRVALIK", "LÄHELEPANU", "VÄLJA", "VÄLJA"...).


Näidisväljund:


```bash
192.168.1.5 dev eth0 lladdr 00:17:BC:56:4F:25 REACHABLE
```


See rida näitab, et masin teab Interface `eth0` kaudu IP Address `192.168.1.5` ja MAC Address `00:17:BC:56:4F:25` vahelist kehtivat vastavust.


Samuti saate filtreerida kirjeid selliste kriteeriumide alusel nagu IP Address, Interface või riik. Näiteks ainult Address `192.168.1.7` päringu tegemiseks:


```bash
ip neigh show 192.168.1.7
```


Või kuvada kõik kirjed Interface `eth1` kohta:


```bash
ip neigh show dev eth1
```


Lisaks konsulteerimisele saab `ip neigh` kasutada ka vahemälu käsitsi muutmiseks. Näiteks staatilise kirje lisamiseks:


```bash
ip neigh add 192.168.1.7 lladdr 00:17:BC:56:4F:25 dev eth1 nud permanent
```


See seob IP Address `192.168.1.7` püsivalt Interface `eth1` määratud MAC Address-ga. Valik `nud permanent` (naabri kättesaamatuse tuvastamiseks) tagab, et sissekannet ei tühistata automaatselt.


Vastupidiselt, et kustutada vahemälu kirje:


```bash
ip neigh del 192.168.1.7 dev eth1
```


See sunnib süsteemi järgmisel korral, kui ta selle Address-ga suhtleb, kaardistust uuesti lahendama.


**MÄRKUS**: Tööriist "ip neigh" töötab nii IPv4 kui ka IPv6 puhul. IPv4 puhul suhtleb see ARP-ga, IPv6 puhul NDP-ga. See pakub ühtset, järjepidevat lähenemist IP/MAC suhete haldamiseks kõigis protokolliperekondades, muutes `ip neigh` kaasaegseks standardiks naabrite haldamiseks Linuxi süsteemides.


### Pakettide analüüsivahendid


Selleks, et põhjalikult analüüsida arvutivõrgus toimuvat, vajavad administraatorid vahendeid, mis suudavad salvestada masinate vahel vahetatavaid pakette. Kaks utiliiti paistavad silma: `tcpdump` ja `Wireshark`. Need tööriistad on hädavajalikud ebanormaalse käitumise diagnoosimiseks, protokollide vahetamise auditeerimiseks või võrgu turvalisuse uurimiseks kaadrite sisu kontrollimise teel.


#### `ttcpdump`: käsurea analüüs


`tcpdump` on väga võimas käsurea tööriist, mis on loodud võrgu kaudu liikuvate pakettide salvestamiseks ja kuvamiseks Interface. See töötab reaalajas ja tänu oma kergele disainile saab seda kasutada süsteemides, millel puudub graafiline Interface või mille ressursid on piiratud. See tugineb raamatukogule `libpcap`, mis pakub riistvarast sõltumatuid madala taseme salvestusfunktsioone.


Tcpdump'i tavaline kasutusviis on jälgida masina või võrgusegmendi võrguaktiivsust, filtreerides pakette vastavalt kindlatele kriteeriumidele. Tulemused saab suunata faili, mis võimaldab liiklust arhiveerida hilisemaks analüüsiks või esitada uuesti mõnes teises tööriistas, näiteks Wiresharkis.


Üldine käsu süntaks on järgmine:


```bash
tcpdump -w <file.cap> -i <interface> -s <snapshot_length> -n <filters>
```



- `-w` kirjutab pildistatud paketid faili formaadis `libpcap` (laiendiga `.cap` või `.pcap`);
- `-i` määrab võrgu Interface, mida jälgida (nt `eth0`, `wlan0`);
- "s" määrab maksimaalse andmemahu paketi kohta. Kui määrata `0`, jäädvustatakse kõik paketid;
- `-n` keelab DNS-i ja teenuse nimede lahendamise, parandades jõudlust.


Väljendifiltrid käsu lõpus võimaldavad piirata pildistamist liikluse alamhulgaga. Valiku täpsustamiseks saate kombineerida märksõnu `host`, `port`, `src`, `dst` jne.


Näide: HTTP-pakettide (port 80) salvestamine serverisse `192.168.25.24` või serverist `192.168.25.24` ja nende salvestamine faili `fichier.cap`:


```bash
tcpdump -w fichier.cap -i eth0 -s 0 -n port 80 and host 192.168.25.24
```


Saadud faili saab hiljem analüüsida graafilises tööriistas või taasesitada teises süsteemis.


#### Wireshark: täiustatud visuaalne analüüs


Wireshark, varem tuntud kui *Ethereal*, on täielik võrguanalüüsi programm, millel on graafiline Interface. Erinevalt `tcpdump`ist pakub struktureeritud, üksikasjalikku pakettide visualiseerimist, sealhulgas protokollide lahtimõtestamist, voogude graafikuid, liiklusstatistikat ja interaktiivseid filtreid. Samuti tugineb see `libpcap`ile, mis tähendab, et see saab avada ja töödelda `tcpdump`i poolt genereeritud kaadrifaile.


Wireshark on saadaval paljudes operatsioonisüsteemides, sealhulgas Linuxis ja Windowsis. Selle installimiseks on vaja administraatori õigusi, et pääseda ligi salvestusliidestele. Pärast käivitamist saate valida võrgu Interface menüüst *Capture*. Klõpsates *Start* algab reaalajas pakettide salvestamine. Ekraan on jagatud kolmeks paneeliks:


- pildistatud kaadrite nimekiri ;
- protokolliga dekodeeritud üksikasjad,
- töötlemata heksadetsimaalsed andmed.



![Image](assets/fr/052.webp)



Wireshark sobib suurepäraselt stsenaariumides, kus on vaja jälgida keerulist protokolli käitumist, rekonstrueerida rakenduse dialoogid (näiteks HTTP- või DNS-seanss) või uurida teenuse vastamisaega. See toetab ka väga spetsiifilisi kuvamisfiltreid, kasutades oma spetsiaalset süntaksit (mis erineb `tcpdump'i omast), et keskenduda ainult asjakohastele pakettidele.


#### Täiendavad vahendid


Oluline on märkida, et `tcpdump` ja Wireshark ei ole omavahel asendatavad: mõlemal on oma tugevused. `tcpdump` sobib paremini käsurea keskkondadesse, automatiseeritud skriptidesse ja kaugserverisse sekkumiseks, samas kui Wireshark on ideaalne üksikasjalikuks, interaktiivseks ja harivaks liiklusanalüüsiks.


Neid kahte tööriista saab kombineerida: kauges süsteemis saab teha kaamera salvestuse `tcpdump`iga, seejärel edastatakse `.cap` fail analüüsiks Wiresharkiga kohalikus masinas. Seda lähenemisviisi kasutatakse praktikas laialdaselt.


### Interface analüüsivahendid


Võrgujuurdepääsu Layer puhul on sageli vaja füüsilisi võrguliideseid pärida ja konfigureerida, et diagnoosida rikkeid, optimeerida jõudlust või kontrollida ühenduse terviklikkust. Üks võimsamaid Linuxi all kättesaadavaid vahendeid selleks on `ethtool`, käsurea utiliit, mis mitte ainult ei anna üksikasjalikku tehnilist teavet Ethernet Interface kohta, vaid võimaldab ka mõningaid parameetreid reaalajas reguleerida.


#### Vaata Interface spetsifikatsioone


Tööriista `ethtool` põhifunktsioon on selle võime teha päringuid Interface kohta ja kuvada selle praeguseid omadusi. See võimaldab teil kontrollida:


- ühenduse kiirus (nt 100 Mbit/s, 1 Gbit/s või 10 Gbit/s) ;
- läbirääkimiste režiim (pooldupleks või täisdupleks) ;
- kas autonegotatsioon on lubatud;
- pordi tüüp (vask, kiudoptiline jne) ;
- lingi staatus (aktiivne või mitte) ;
- toetus täiustatud funktsioonidele, nagu *Wake-on-LAN*.


See teave on eriti kasulik probleemide diagnoosimiseks, mis on seotud füüsilise ühenduvuse või host'i võrgukaardi ja sellega ühendatud seadmete (kommutaator, marsruuter jne) vaheliste sobimatute läbirääkimissätetega.


Selle teabe saamiseks lihtsalt käivitage:


```bash
ethtool enp0s3
```


See käsk väljastab üksikasjaliku aruande Interface kohta, mis on CentOS- või RHEL-põhistes süsteemides tavaline nimekonventsioon.



![Image](assets/fr/053.webp)



#### Interface parameetrite dünaamiline muutmine


`ethtool` ei piirdu ainult vaatlusega: see võimaldab ka teatud Interface parameetreid seadistada ilma masinat taaskäivitamata. See võimaldab näiteks sundida konkreetset ühenduskiirust või lubada funktsioone vastavalt kohaliku võrgu vajadustele.


Valikut `-s` kasutatakse selliste parameetrite dünaamiliseks konfigureerimiseks nagu:


- lingi kiirus (kiirus), mis on selgelt määratud (nt 1000 1 Gbit/s puhul) ;
- dupleksrežiim (`duplex`), kas `pool` või `täielik`;
- autonegotatsiooni (`autoneg`) lubamine või keelamine ;
- *Wake-on-LAN* (`wol`) lubamine ;
- sadama tüüp.


Näide 1: lubage autonegotatsioon Interface-l:


```bash
ethtool -s enp0s3 autoneg on
```


Näide 2: lubage *Wake-on-LAN* funktsioon (et võimaldada masinal ärgata eemalt maagilise paketi abil):


```bash
ethtool -s enp0s3 wol p
```


Selles näites määrab valik "p", et ärkamine toimub kohe, kui avastatakse *Wake-on-LAN* pakett. Sellist seadistust kasutatakse sageli ettevõtluskeskkondades öiste uuenduste või kaughoolduse tegemiseks.


#### Tööriistade paigaldamine


Oluline on märkida, et `ethtool` ei ole alati vaikimisi paigaldatud. Red Hat/CentOS distributsioonides saab seda paigaldada käsuga:


```bash
yum install -y ethtool
```


Debianis ja Ubuntus on samaväärne käsk:


```bash
sudo apt install ethtool
```


**Hoiatus**: kõigis `ethtool` käskudes tuleb võrgu Interface nimi märkida kohe pärast valikut (nagu `-s`). Mis tahes süntaksiviga parameetrite paigutamisel muudab käsu kehtetuks või ebaefektiivseks.



## Võrgustiku Layer tööriistad


<chapterId>d2c5bf35-4284-4af8-8e8b-049c696a511b</chapterId>


### Liiklusanalüüsi vahendid


Võrgudiagnostikas on käsk "ping" endiselt üks lihtsamaid, kuid samas kõige võimsamaid vahendeid kahe masina vahelise ühenduse testimiseks. See kontrollib, kas kaugem host on antud ajahetkel saavutatav, andes samas teavet ka latentsuse, ühenduse stabiilsuse ja DNS-lahenduse kohta.


Käsk `ping` tugineb ICMP (*Internet Control Message Protocol*) protokollile. Kui kasutaja saadab `ping` taotluse, saadab süsteem ICMP "Echo Request" paketi IP Address või hostinimele. Kui sihtmasin on võrgus ja võrgutee on kehtiv, vastab ta ICMP "Echo Reply" paketiga. Seda lihtsat mehhanismi saab kasutada latentsuse mõõtmiseks ja ühenduvuse või nimede lahendamise probleemide tuvastamiseks.


Näide klassikalise käsu kohta:


```bash
ping 172.17.18.19
```


Tüüpiline vastus:


```bash
mydmn.org (172.17.18.19): 56 data bytes
64 bytes from 172.17.18.19: icmp_seq=0 ttl=56 time=7.7 ms
64 bytes from 172.17.18.19: icmp_seq=1 ttl=56 time=6.0 ms
64 bytes from 172.17.18.19: icmp_seq=2 ttl=56 time=5.5 ms
```


Selles näites on nimeresolutsioon teostatud automaatselt: domeen `mydmn.org` on seotud IP Address `172.17.18.19`ga, mis kinnitab, et DNS-resolutsioon toimib korrektselt. Käsk annab ka tehnilisi üksikasju, näiteks:


- iCMP järjestusnumber (`icmp_seq`), mis on kasulik vastuste järjekorra kontrollimiseks;
- TTL (*Time-To-Live*), mis näitab, mitu hüpet on jäänud enne paketi äraviskamist;
- ümberistumise aeg/viivitus (time), väljendatud millisekundites, mis annab hinnangu lingi latentsuse kohta.


#### ICMP parameetrite üksikasjalikum analüüs


TTL on IP-protokollis kriitiline väli. Iga andmeprogramm initsialiseeritakse saatja poolt TTL-väärtusega (sageli 64, 128 või 255). Iga marsruuderi marsruudil vähendab seda väärtust 1 võrra. Kui TTL jõuab enne sihtkohta jõudmist 0-ni, siis pakett visatakse ära ja saatjale saadetakse ICMP-viga. See mehhanism takistab lõpmatuid marsruutimisahelaid.


Edasikandmisaeg (*tagasisõidu viivitus/aeg*) mõõdab viivitust, mis kulub paketil saatjast lahkumisel, sihtkohta jõudmisel ja tagasipöördumisel. Praktikas peetakse stabiilse ühenduse puhul vastuvõetavaks viivitust alla 200 ms. Ebaharilikult suured viivitused võivad viidata võrgu ülekoormusele, ebatõhusale marsruutimisele või ühenduse kehvale kvaliteedile.


#### Täiustatud `ping` kasutamine


`ping` pakub võimalusi testide täpsustamiseks ja spetsiifilise võrgukäitumise jälgimiseks.


Saate saatmistaotluste saatmiseks kasutada valikut `-b`, et suunata need kõigile alamvõrgus asuvatele hostidele:

```bash
ping -b 192.168.1.255
```


See on kasulik kohalikes võrkudes, et kiiresti tuvastada aktiivseid hoste või testida, kuidas võrk käitleb ringhäälingupäringuid. Paljudes seadistustes blokeerivad marsruuterid ja tulemüürid siiski ringhäälingupingid, et vältida võimendusrünnakuid.


Saate määrata ka kohandatud intervalli päringute vahel valikuga `-i` (vaikimisi: 1 sekund):


```bash
ping -i 0.2 -c 10 192.168.1.7
```


See saadab 10 ICMP päringut 0,2-sekundiliste intervallidega. Selline testimine on kasulik lühikese aja jooksul esinevate latentsuse kõikumiste tuvastamiseks või lingi kergeks koormamiseks, et hinnata selle stabiilsust.


### Marsruutimistabelite analüüsi vahendid


Käsk `ip route`, mis on osa `iproute2` komplektist, on kaasaegsetes Linuxi süsteemides soovitatav ja standardne vahend tuuma IP marsruutimistabeli kontrollimiseks ja haldamiseks. See asendab vananenud käsu `route`, pakkudes selgemat süntaksit, suuremat järjepidevust ja laiendatud toetust kaasaegsetele funktsioonidele (IPv6, mitu tabelit, nimeruumid jne).


#### Marsruutimistabeli kuvamine


Praeguse marsruutimistabeli kuvamine:


```bash
ip route show
```


Selles väljundis on loetletud kõik tuumale teadaolevad marsruudid, st väljaminevate pakettide teekonnad sõltuvalt nende sihtkohast.


Näidisväljund:


```bash
default via 192.168.1.1 dev eth0 proto dhcp metric 100
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
```


Iga rida tähistab marsruuti. Peamised väljad on järgmised:


- default**: vaikimisi marsruut, mida kasutatakse, kui ükski spetsiifilisem marsruut ei vasta.
- via**: sihtkohta jõudmiseks kasutatud värav.
- dev**: kasutatud Interface võrk.
- proto**: kuidas marsruut loodi (käsitsi, DHCP, kernel jne).
- meetrika**: marsruudi maksumus, mida kasutatakse mitme võimaliku marsruudi prioriseerimiseks.
- scope**: marsruudi ulatus (nt "link" otseühendusega marsruudi puhul).
- src**: lähte-IP Address, mida kasutatakse selle Interface väljaminevate pakettide jaoks.


#### Marsruutide lisamine ja kustutamine


Marsruutimistabelit saab muuta ka dünaamiliselt, näiteks lisades või eemaldades staatilisi marsruute.


Staatilise marsruudi lisamine:


```bash
ip route add 192.168.1.0/24 via 192.168.1.1 dev eth0
```


Sellega konfigureeritakse marsruut võrku `192.168.1.0/24` Interface `eth0` värava `192.168.1.1` kaudu.


Eemaldage see marsruut:


```bash
ip route del 192.168.1.0/24
```


See käsk kustutab eelnevalt määratud marsruudi.


#### Kasulikud käsud


Siin on mõned kasulikud variandid analüüsiks või skriptide koostamiseks:


- `ip -4 route`: näitab ainult IPv4 marsruute;
- `ip -6 route`: näitab ainult IPv6 marsruute;
- `ip route list table main`: kuvab peamise marsruutimistabeli (vaikimisi väärtus) ;
- `ip route get <Address>`: näitab, millist Interface ja väravat pakett antud Address-le kasutab.


Näide:


```bash
ip route get 8.8.8.8
```


See näitab täpset marsruuti, mida pakett peab võtma, et jõuda aadressile `8.8.8.8.8`.


### Jälgimisvahendid


Üheks kõige tõhusamaks vahendiks IP-pakettide poolt lähtekoha ja sihtkoha vahel kulgeva marsruudi analüüsimiseks on käsk "traceroute". See näitab samm-sammult pakettide läbitud teed ja tuvastab vahepealsed marsruuterid, mida nad läbivad. Võrguliidese rikke või teenuse katkestuse korral aitab `traceroute` kindlaks teha probleemi täpse asukoha.


Nagu käsu `ping` puhul, saab sihtmärgi määrata kas selle täielikult kvalifitseeritud domeeninime (FQDN) või IP Address abil. Näiteks:


```bash
traceroute mydmn.org
```


#### Tööpõhimõte


`traceroute` tugineb TTL (*Time To Live*) väljale IP-pakettide päises. Nagu varem selgitatud, on see väli loendur, mida iga marsruuderi poolt tee ääres vähendatakse. Kui TTL jõuab nullini, visatakse pakett ära ja marsruuter saadab saatjale ICMP-teate "Time Exceeded". See mehhanism hoiab ära lõputud silmused väärate marsruutide korral.


`traceroute` kasutab seda käitumist ära saatja ja vastuvõtja vaheliste marsruuterite kaardistamiseks:


- Kõigepealt saadab ta rea UDP-pakette (tavaliselt kolm), mille TTL on 1. Esimene marsruuter leiab TTL-i 0, nii et ta heidab paketi kõrvale ja vastab seejärel ICMP-teatega, milles avaldab oma IP Address ja vastamisaja.
- Seejärel saadab ta teise seeria pakette, mille TTL on 2, paljastades teise marsruuteri.
- Protsess kordub, kuni sihtpunktini jõutakse, misjärel host vastab ICMP Port Unreachable sõnumiga, mis näitab, et lõpp-punkt on saavutatud.


Vaikimisi kasutab `traceroute` UDP-pakette, mis saadetakse kasutamata portidele (tavaliselt alates 33434), kuid seda saab seadistada ka ICMP (nagu `ping`) või isegi TCP kasutamiseks, sõltuvalt süsteemidest või käskude variantidest.


Näidisväljund:


```bash
traceroute to www.google.fr (216.58.210.35), 64 hops max, 52 byte packets

1  par81-024.ff.avast.com (62.210.189.205)   25.107 ms  24.235 ms  24.383 ms
2  62-210-189-1.rev.poneytelecom.eu (62.210.189.1)  27.341 ms  27.119 ms  28.184 ms
3  a9k1-45x-s43-1.dc3.poneytelecom.eu (195.154.1.92)  25.910 ms  25.040 ms  25.558 ms
4  72.14.218.182 (72.14.218.182)  36.234 ms  39.907 ms  38.130 ms
5  108.170.244.177 (108.170.244.177)  25.880 ms
108.170.244.240 (108.170.244.240)  25.791 ms
108.170.244.177 (108.170.244.177)  26.449 ms
6  216.239.62.143 (216.239.62.143)  26.491 ms
216.239.43.157 (216.239.43.157)  26.414 ms
216.239.62.139 (216.239.62.139)  26.400 ms
...
9  108.170.246.161 (108.170.246.161)  33.174 ms
108.170.246.129 (108.170.246.129)  34.342 ms
108.170.246.161 (108.170.246.161)  33.707 ms
10  108.170.232.105 (108.170.232.105)  33.845 ms  33.846 ms
108.170.232.103 (108.170.232.103)  34.206 ms
11  lhr25s11-in-f35.1e100.net (216.58.210.35)  34.094 ms  33.353 ms  33.718 ms
```


Iga rida vastab läbitud marsruuterile, kusjuures kuni kolm ajamõõtmist (millisekundites) näitavad selle marsruuteri edasisõidu latentsust. Need väärtused aitavad hinnata iga võrgusegmendi jõudlust.


#### Tulemuste tõlgendamine


Kui marsruuter ei vasta või filtreerib ICMP-sõnumeid, kuvatakse vastusaja asemel tärnid `*`. See võib tähendada:


- iCMP-vastuseid blokeeriv tulemüür,
- seade, mis on konfigureeritud mitte reageerima, või
- ajutine ühendusprobleem teel.


Seega ei tuvasta "traceroute" mitte ainult läbitud marsruuti, vaid toob esile ka ebatavalised viivitused või katkestused.


Mõnes süsteemis võib kasutada samaväärset käsku `tracepath`, mis ei nõua root-õigusi. IPv6 puhul kasutage `traceroute6` või `tracepath6`.


Näide IPv6 jälgimise kohta:


```bash
traceroute6 ipv6.google.com
```


### Tööriistad aktiivsete ühenduste kontrollimiseks


Aktiivsete võrguühenduste diagnoosimiseks ja võrguaktiivsuse jälgimiseks Linuxi süsteemis on käsk `ss` (lühend _socket statistics_) kaasaegne võrdlusvahend. See on osa `iproute2` paketist ja asendab nüüdseks kadunud `netstat`, pakkudes paremat jõudlust ja täpsemaid tulemusi.


`ss` näitab aktiivseid TCP- ja UDP-ühendusi, kuulavaid porte, kohalikke ja kaugaadresse, ühenduse olekut ja nendega seotud protsesse.


#### Üldine kasutamine


Kui käsk `ss` käivitatakse ilma valikuteta, näitab see aktiivseid TCP-ühendusi. Põhiline süntaks:


```bash
ss [options]
```


Mõned ühised võimalused analüüsi täpsustamiseks:


- `-t`: näitab ainult TCP-ühendusi;
- `-u`: näitab ainult UDP-ühendusi;
- `-l`: näitab ainult kuulavaid pesasid;
- `-n`: keelab nimede lahendamise (toor-IP-d ja portnumbrid) ;
- `-p`: kuvab iga sokliga seotud protsessi (PID ja programmi nimi),
- `-a`: näitab kõiki ühendusi, sealhulgas mitteaktiivseid,
- `-s`: kuvab kõrgetasemelist socket statistika.


#### Juhtumiuuringud


Kõigi aktiivsete ühenduste kuvamine, mis kasutavad TCP-porti 80 (HTTP):


```bash
ss -ant | grep ':80'
```


See näitab aktiivseid TCP-ühendusi, mis hõlmavad porti 80. Sellised olekud nagu "LISTEN", "ESTABLISHED", "TIME-WAIT" näitavad iga Exchange hetkeolukorda.


Näidisväljund:

```
ESTAB 0 0 192.168.1.10:54321  93.184.216.34:80
```


Kõigi võrguühenduste ja nendega seotud protsesside kuvamine:


```bash
ss -tulnp
```


Et saada üldist pistikupesa kasutamise kokkuvõtet:

```bash
ss -s
```


Ainult UDP-ühenduste filtreerimiseks:

```bash
ss -unp
```


Need käsud on eriti kasulikud kahtlaste ühenduste, ootamatute kuulatavate portide või konkreetse teenuse tegevuse jälgimiseks.


## Transpordi ja top Layer tööriistad


<chapterId>bce47931-930e-4288-b0fd-666c9a1066b5</chapterId>


### DNS päringu tööriistad


TCP/IP-mudeli ülemistes kihtides, eriti rakenduse Layer puhul, on oluline mõista, kuidas nimede lahendamine toimib. DNS-päringuvahendid võimaldavad kontrollida, kas domeeninimi on õigesti seotud IP Address-ga, ning aitavad diagnoosida ka DNS-serveri probleeme, nagu valesti konfigureerimine, levikuhäired või kättesaamatus. Need tööriistad on hädavajalikud igale võrguadministraatorile või igale kasutajale, kes soovib põhjalikumalt mõista DNS-vahetusi IP-keskkonnas.


#### Käsk `nslookup`


Lihtsaim DNS päringuvahend on `nslookup`. See saadab päringu DNS-serverile ja tagastab domeeninimega seotud IP Address (või vastupidi). Vaikimisi küsib see süsteemi konfigureeritud DNS-serverit, kuid te võite ka otse käsus serveri määrata.


Näide otsese otsingu kohta:

```bash
nslookup mydmn.org
```


Konkreetse DNS-serveri päring:

```bash
nslookup mydmn.org 192.6.23.4
```


Taotlus palub DNS-serveril aadressil `192.6.23.4` lahendada nimi `mydmn.org`. See on eriti kasulik selleks, et kontrollida, kas antud DNS-server tunneb domeeninime ära või et kontrollida, kas server töötab korralikult.


#### Käsk "dig


`dig` (*Domain Information Groper*) on kaasaegsem, täielikum ja paindlikum vahend kui `nslookup`. See toetab keerulisi päringuid ja annab üksikasjalikku teavet lahendamise protsessi, kaasatud serverite hierarhia, tagastatud kirje tüübi (A, AAAA, MX, TXT jne) ja tekkinud vigade kohta.


Põhiline päringu näide:

```bash
dig mydmn.org
```


Konkreetse DNS-serveri päring:

```bash
dig @192.6.23.4 mydmn.org
```


See käsk kontrollib DNS-kirje kättesaadavust antud serveris.

Üks `dig` peamisi eeliseid on see, et see näitab DNS-vastuse üksikasju, mis teeb selle väga kasulikuks konfiguratsioonivigade diagnoosimisel.


#### DNS-lahendajate käsitsi konfigureerimine


Mõnikord on vaja kohalikult kasutatavaid DNS-servereid muuta, näiteks testkeskkondades või sundida kasutama konkreetseid servereid. Seda saab teha, muutes faili `/etc/resolv.conf`, mis määratleb süsteemi DNS resolutsiooni seaded.


Näidiskonfiguratsioon:


```bash
vi /etc/resolv.conf

search mydmn.org
nameserver 192.168.1.10
nameserver 192.168.1.11
```



- Väljal `search` määratakse domeen, mis lisatakse automaatselt lühinimede lahendamisel.
- Kirjed "nimeserver" määravad kasutatavaid DNS-servereid prioriteetsuse järjekorras.


Paljudes kaasaegsetes distributsioonides (eriti nendes, mis kasutavad `systemd-resolved`) on muudatused failis `/etc/resolv.conf` ajutised ja need võidakse taaskäivitamisel või võrgu taasühendamisel üle kirjutada. Püsivamad meetodid on `resolvconf`, `systemd-resolved` või *NetworkManageri* konfiguratsioonide muutmine.


#### Käsk "host


Teine lihtne, kuid tõhus DNS-vahend on `host`. See lahendab domeeninimesid IP-aadressideks (või vastupidi) ja aitab diagnoosida DNS-vigu või valekonfiguratsioone võrgus Interface.


Näited:

```bash
host mydmn.org
```


Pööratud otsing:

```bash
host 192.6.23.4
```


`host` on eriti mugav kiireks kontrollimiseks, eriti kui seda kasutatakse käsurea skriptides.


Korduvaid või intensiivseid päringuid kolmandate osapoolte DNS-serveritele ilma loata võib tõlgendada sissetungikatsetena või pahatahtliku tegevusena. Kui neid käske kasutatakse valesti või nende võrkude vastu, mida te ei kontrolli, võivad need käsud sarnaneda luurele, mis on sageli rünnaku esimene samm. Piirake nende kasutamine alati keskkondadega, mida te haldate või kus teil on selgesõnaline luba.


### Võrgu skaneerimise tööriistad


Kohaliku või laivõrgu jälgimisel või kaitsmisel on oluline tuvastada aktiivsed seadmed ja nende poolt pakutavad teenused. Just seda teeb tööriist `nmap` (*Network Mapper*).


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

#### Tutvustame `nmap`


`nmap` võimaldab ühe või mitme hosti sihipärast skaneerimist, et tuvastada avatud porte, olemasolevaid teenuseid (HTTP, SSH, DNS jne) ja mõnikord isegi kasutatava operatsioonisüsteemi tüüpi. Tänu paljudele võimalustele annab `nmap` täpse ülevaate võrgu kokkupuutepinnast, mis on oluline infrastruktuuri haldamise auditeerimise või karmistamise faasis.


Nii nagu käsku `host`, ei tohi ka käsku `nmap` kunagi kasutada võrkudes või infrastruktuurides, mis ei kuulu teile, või ilma selgesõnalise loata. Autoriseerimata portide skaneerimine võidakse märkida pahatahtlikuks luurekatseks, seda avastavad sageli turvasüsteemid (tulemüürid, IDS/IPS) ja see võib põhjustada isegi õiguslikke tagajärgi.


#### Põhikasutus


Konkreetse vastuvõtja skaneerimiseks ja selle avatud portide vaatamiseks:

```bash
nmap 192.168.0.1
```


See käsk skaneerib 1000 kõige levinumat porti hostil `192.168.0.1` ja kuvab kasutatud teenused ja protokollid. Kui DNS-lahendus on konfigureeritud, saate IP Address asemel kasutada ka hostinime.


#### Täielik võrgu skaneerimine


Üks `nmap`i eeliseid on selle võime skaneerida kogu aadresside vahemikku ühe käsuga. See teeb näiteks lihtsaks kõikide võrgus olevate aktiivsete masinate kiire inventeerimise:


```bash
nmap 192.168.0.0/24
```


Sel juhul küsitakse kõiki hoste vahemikus `192.168.0.0` kuni `192.168.0.255`. Iga IP Address puhul loetletakse tulemused avatud porte, nende staatust (avatud, filtreeritud jne) ja võimaluse korral vastava teenuse nime.



![Image](assets/fr/055.webp)



Administraator saab kasutada `nmap`i mitmete ülesannete täitmiseks:


- Aktiivsete hostide tuvastamine**: tuvastab, millised masinad reageerivad allvõrgus;
- Teenuste inventuur**: tagada juurdepääs ainult vajalikele sadamatele (vähimate privileegide põhimõte);
- Vastavuskontroll**: võrdle avatud porte organisatsiooni turvapoliitikaga;
- Haavatavuste ennetamine**: kriitilistes masinates töötavate ebaturvaliste või aegunud teenuste tuvastamine.


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

### Protsessi küsitlusvahendid


Aktiivsete protsesside ja avatud failide põhjalikuks analüüsiks, eriti võrgukontekstis, kasutavad Linuxi administraatorid sageli käsku `lsof` (*List Open Files*). Vaatamata oma nimele ei ole `lsof` piiratud traditsiooniliste failidega: UNIXi süsteemides loetakse failiks kõike, sealhulgas võrgupesasid, seadmeid ja sidekanaleid.


Seega annab see tööriist süsteemi läbilõike, seostades aktiivsed protsessid, avatud võrgupordid, kasutatud failid ja kaasatud kasutajad.


#### Võrgustiku analüüs `lsof`-iga


Valik "-i" piirab väljundit ainult võrguühendustele (TCP, UDP, IPv4 või IPv6). See võimaldab hõlpsasti näha, millised protsessid suhtlevad võrgu kaudu:


```bash
lsof -i
```


See käsk loetleb kõik jooksvad protsessid, mis kasutavad võrgupesa, näidates kasutatavat porti, protokolli (TCP/UDP), ühenduse olekut, samuti PID-i ja seotud kasutajat.


#### Filtreerimine IP Address või pordi järgi


Saate täpsustada otsinguid, määrates IP Address ja pordi, isoleerides konkreetse võrguvoo. Näiteks SMTP-sessiooni (port 25) kontrollimiseks konkreetse hostiga:


```bash
lsof -n -i @192.168.2.1:25
```


See näitab ainult aktiivseid võrguühendusi hostiga `192.168.2.1` pordil 25, mis on kasulik kahtlase tegevuse või SMTP-voogudega seotud probleemide diagnoosimiseks.


#### Seadme juurdepääsu jälgimine


Veel üks `lsof` tugevus on erifailide, näiteks kettapartitsioonide jälgimine. Näiteks, et kontrollida, millised protsessid on avanud faile `/dev/sda1` peal:


```bash
lsof /dev/sda1
```


See on kasulik, kui eemaldamise katse ebaõnnestub, sest seade on veel kasutusel, või kui uuritakse, millised rakendused pääsevad partitsioonile ligi.


#### Ristanalüüs: protsess ja võrgustik


Valikuid saab kombineerida, et saada täpne ülevaade. Näiteks, et näha kõiki võrgu porte, mis on avatud protsessi PID 1521 poolt:


```bash
lsof -i -a -p 1521
```


Valik `-a` lõikab kriteeriumid (`-i` ja `-p`), piirates väljundi ainult selle protsessi võrguühendustega.


#### Mitme kasutaja jälgimine


`lsof`i saab kasutada ka konkreetsete kasutajate tegevuse analüüsimiseks, loetledes kõik nende poolt avatud failid, valikuliselt filtreerituna PID-i järgi:


```bash
lsof -p 1521 -u 500,phil
```


See näitab faile või võrguühendusi, mida kasutab kasutaja `phil` või UID 500, mis on piiratud protsessiga 1521.


### Jaotise kokkuvõte


Selles viimases osas oleme tutvunud paljude asendamatute vahenditega arvutivõrkude diagnoosimiseks, analüüsimiseks ja haldamiseks. TCP/IP-mudeli kihtide ümber struktureeritud uuring ei selgita mitte ainult seda, kuidas võrgukommunikatsioon toimib, vaid kehtestab ka range metoodika võimalike probleemide tuvastamiseks, isoleerimiseks ja lahendamiseks.


Need tööriistad annavad administraatoritele ühtse tehniliste hoobade komplekti, et jälgida võrgu tervist, analüüsida liiklust, auditeerida ühendusi ja sekkuda kiiresti vigaste seadmete või teenuste puhul.


#### Võrgule juurdepääs Layer


Vahendid, mis pakuvad otsest nähtavust liidestele ja raamidele:


- arp / ip neigh**: kontrollib ja muudab ARP/NDP vahemälu, et kontrollida või parandada IP-MAC-ühendusi;
- tcpdump**: käsurea pakettide salvestamine, filtreeritav ja eksporditav;
- Wireshark**: graafiline pakettide analüüs koos süvaprotokollide dekodeerimisega;
- ethtool**: Etherneti kaardi füüsiliste parameetrite (kiirus, dupleks, WoL jne) päring ja reguleerimine.


#### Võrk Layer


Tööriistad IP-ühenduvuse, marsruutimise ja paketiliikluse hindamiseks:


- ping**: saavutatavuse testimine ja ICMP-viivituse mõõtmine;
- ip route**: kontrollib ja muudab marsruutimistabelit, et kontrollida pakettide teekonda;
- traceroute**: marsruudi marsruudi marsruudi sihtkohani kulgeva marsruudi identifitseerimine hüppeliigiti;
- ss**: üksikasjalik ülevaade TCP/UDP-sokkidest ja nendega seotud protsessidest (netstat'i järeltulija).


#### Transpordi- ja rakenduskihid


Teenuste ja protsesside diagnoosimise vahendid:


- nslookup / dig / host**: DNS päringud nimede lahenduse kinnitamiseks ja kirjete analüüsimiseks;
- nmap**: uurib avatud porte ja avatud teenuseid, et hinnata rünnakupinda;
- lsof**: loetleb protsesside poolt avatud faile ja sokke, seostades süsteemi ja võrgu aktiivsust.


Nende vahendite, millest igaüks on vastavuses TCP/IP-mudeli konkreetse etapiga, omandamine võimaldab metoodilist lähenemist: alustades füüsilisest Layer-st, liikudes marsruutimise kaudu kuni rakendusteenusteni. See teadmisteahel annab administraatoritele võimaluse diagnoosida, kindlustada ja optimeerida oma infrastruktuuri, tagades nii võrgu jõudluse kui ka kättesaadavuse.


# Viimane osa


<partId>09d5393c-63bc-42fc-bf79-c65e380211bd</partId>


## Arvamused ja hinnangud


<chapterId>114c33c0-9831-4d74-affd-f5d37adc53c3</chapterId>


<isCourseReview>true</isCourseReview>

## Lõpueksam


<chapterId>b99e005e-8dd0-4fa4-b302-f940c27a30ac</chapterId>


<isCourseExam>true</isCourseExam>

## Kokkuvõte


<chapterId>3b449814-78f3-41c0-8138-0a04f3682719</chapterId>


<isCourseConclusion>true</isCourseConclusion>