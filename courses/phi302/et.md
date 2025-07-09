---
name: Bitcoin arendusfilosoofia
goal: Arendada sügav filosoofiline arusaam Bitcoin disainiprintsiipidest.
objectives: 

  - Analüüsida Bitcoin põhilisi kaitsvaid kompromisse ja arhitektuurilisi otsuseid
  - Õppige, kuidas hinnata Bitcoin protokolli kavandatud muudatusi ja uuendusi
  - Sünteesida üle kümne aasta kestnud Bitcoin arengu ajalugu ja kogukonna arutelusid
  - Kriitilise mõtlemise raamistike rakendamine uute piiritletud piiride hindamisel


---

# Sügav sukeldumine Bitcoin arendamise filosoofiasse



Bitcoin arendusfilosoofia on kursus Bitcoin arendajatele, kes juba mõistete ja protsesside, näiteks Proof-of-Work, plokkide ehitamise ja tehingu elutsükli põhitõdesid mõistavad ning kes soovivad tõsta oma taset, omandades sügavama arusaama Bitcoin disaini kompromissidest ja filosoofiast.

See peaks aitama uutel arendajatel omandada üle kümne aasta kestnud Bitcoin arendamise ja avaliku arutelu kõige olulisemad õppetunnid, pakkudes neile samas kasulikku konteksti uute ideede (nii heade kui ka halbade!) hindamiseks.


### Mida oodata?


Nagu eespool öeldud, on see praktiline juhend Bitcoin arendajatele. Bitcoin on siiski lai ja keeruline teema ning me ei saa siinkohal kõiki selle aspekte käsitleda. Selle kursusega loodame arutada vajalikke funktsioone, et alustada arendustegevust, aga ka võimaldada teil seda iseseisvalt edasi uurida.


Bitcoin-ga on seotud palju inimesi; kuna mõnel neist on vastandlikud arvamused, võite siit leida ressursse, mis väljendavad vastuolulisi ideid. Siiski püüame alati jääda faktide valdkonda, kus arvamused ei ole olulised.


### Kes selle kirjutas?


See kursus on kohandatud samanimelise raamatu põhjal, mille peamine autor on Kalle Rosenbaum ja kaasautor Linnéa Rosenbaum.

Raamatu tellis ja rahastas [Chaincode Labs] (https://learning.chaincode.com/), arenduskeskus, mis korraldab haridusprogramme arendajatele, kes soovivad õppida Bitcoin arendamist.


+++



# Sissejuhatus

<partId>58c48e9b-e285-4dc6-8952-6cc5140b1313</partId>


## Kursuse ülevaade

<chapterId>28b7256b-9cb0-463e-a82d-d732be86c98c</chapterId>


Tere tulemast sellele kursusele PHI 301 Bitcoin arengufilosoofia kohta.


Bitcoin on midagi enamat kui lihtsalt krüptoraha, see kehastab filosoofilist nägemust detsentraliseerimisest, privaatsusest, usaldamatusest ja vastupidavusest. See kursus on mõeldud spetsiaalselt arendajatele, kes on juba tuttavad Bitcoin tehniliste alustega ja kes soovivad nüüd süvendada oma arusaamist Bitcoin disaini ja juhtimise aluseks olevatest põhimõtetest.


Selle kursuse käigus saate selgust olulistest väärtustest ja strateegiatest, mis on Bitcoin arengut juhtinud üle kümne aasta. Neid teemasid põhjalikult uurides arendate kriitilist perspektiivi, mida on vaja, et hinnata ja julgelt kaasa rääkida tulevastes arengutes.


### Bitcoin kesksed väärtused


Mis teeb Bitcoin ainulaadseks? See osa paljastab Bitcoin kujunduse keskmes olevad põhiväärtused. Te uurite **detsentraliseerimist**, mis on nurgakivi, mis tagab, et ükski üksus ei kontrolli võrku; **trustlessness**, mis on võti kolmandate isikute sõltuvuse kaotamiseks; **privaatsus**, mis on oluline nii üksikisiku vabaduse kui ka süsteemi terviklikkuse jaoks; ja **piiramatu Supply**, mis on kodeeritud nappuse garantii, mis kujundab Bitcoin majanduslikku identiteeti. Nende mõistete valdamine võimaldab teil täielikult mõista Bitcoin tugevusi ja haavatavusi.


### Bitcoin Juhtimine


Bitcoin keerulisel juhtimismaastikul navigeerimine nõuab enamat kui tehnilisi teadmisi, see nõuab Bitcoin ainulaadse lähenemisviisi mõistmist konsensusele ja otsuste tegemisele. Selles jaotises tutvute kriitiliste protsesside, näiteks protokollide uuendamise mehhanismide ja filosoofiate, vastandliku mõtlemise vajalikkuse, avatud lähtekoodiga koostöö tugevuse, mõõtmete laiendamisega seotud pidevate probleemide ja nüansirikaste strateegiate kohta, mida on vaja, kui asjad paratamatult valesti lähevad. Nende teadmistega varustatuna olete valmis mitte ainult osalema, vaid ka Bitcoin tulevikku tõhusalt ja vastutustundlikult kujundama.


Kas olete valmis astuma järgmise sammu oma Bitcoin teekonnal? Alustame!


***N.B.**: Kui kursuse käigus tekib mõni Bitcoin-ga seotud tundmatu termin, vaadake [sõnastik](https://planb.network/resources/glossary), et leida definitsioonid.*




# Bitcoin Keskmised väärtused

<partId>2d6c683b-54c8-5465-b2ca-4e96a6828834</partId>


## Detsentraliseerimine

<chapterId>9397c84b-0038-5d0e-88d5-11767ce8182d</chapterId>




Selles analüüsitakse, mis on detsentraliseerimine ja miks see on Bitcoin toimimiseks hädavajalik. Me eristame

kaevurite detsentraliseerimine ja täisnoodide detsentraliseerimine ning arutame, mida nad toovad kaasa tsensuurivastasuse, mis on üks Bitcoin kõige kesksemaid omadusi.


Seejärel liigub arutelu neutraalsuse ehk kasutajate, kaevurite ja arendajate suhtes lubadusteta suhtumise mõistmisele, mis on iga detsentraliseeritud süsteemi vajalik omadus. Lõpuks käsitleme, kuidas Hard-sugust detsentraliseeritud süsteemi võib olla raske mõista, ning esitame mõned mentaalsed mudelid, mis võivad aidata teil seda mõista.


Süsteemi, kus puudub keskne kontrollpunkt, nimetatakse *detsentraliseeritud* süsteemiks. Bitcoin on loodud selleks, et vältida keskse kontrollpunkti olemasolu, täpsemalt *tsensuurikeskuse* olemasolu.


Detsentraliseerimine on vahend *tsensuurivastase võitluse* saavutamiseks.


Bitcoin-s on kaks peamist detsentraliseerimise aspekti: Miner detsentraliseerimine ja Full node detsentraliseerimine.


Miner detsentraliseerimine viitab asjaolule, et tehingu töötlemist ei tee ega koordineeri ükski keskne üksus. Full node detsentraliseerimine viitab asjaolule, et plokkide, st kaevurite poolt väljastatud andmete valideerimine toimub võrgu servas, lõppkokkuvõttes selle kasutajate, mitte mõne usaldusväärse asutuse poolt.


![](assets/decentralization-banner.webp)


### Miner detsentraliseerimine



Enne Bitcoin oli tehtud katseid luua digitaalseid valuutasid, kuid enamik neist ebaõnnestus juhtimise detsentraliseerimise ja tsensuurivastase võitluse puudumise tõttu.


Miner detsentraliseerimine Bitcoin-s tähendab, et *tehingute tellimist* ei vii läbi ükski üksus või üksuste fikseeritud kogum. Seda teostavad kollektiivselt kõik osalejad, kes soovivad selles osaleda; see kaevurite kollektiiv on dünaamiline kasutajate kogum. Igaüks võib soovi korral liituda või lahkuda. See omadus muudab Bitcoin tsensuurikindlaks.


Kui Bitcoin oleks tsentraliseeritud, oleks see haavatav nende suhtes, kes soovivad seda tsenseerida, näiteks valitsused. Seda tabaks sama saatus nagu varasemaid katseid luua digitaalset raha. [artikli] (https://www.blockstream.com/sidechains.pdf) pealkirjaga "Enabling Blockchain Innovations with Pegged Sidechains" sissejuhatuses selgitavad autorid, kuidas digitaalraha varajased versioonid ei olnud vastandlikuks keskkonnaks varustatud (vt ka peatükki "Vastandlik mõtlemine" järgmises osas).


David Chaum tutvustas 1983. aastal digitaalset sularaha kui uurimisteemat, mille puhul kasutatakse keskserverit, mida usaldatakse Double-spending vältimiseks. Selleks et vähendada üksikisikute privaatsusriski, mis tuleneb sellest kesksest usaldusväärsest osapoolest, ja tagada asendatavus, võttis Chaum kasutusele pime allkirja, mida ta kasutas krüptograafilise vahendina, et vältida keskserveri allkirjade (mis esindavad münte) ühendamist, võimaldades samas keskserveril vältida topeltkulutusi.

Nõue keskse serveri järele sai digitaalse sularaha Achilleuse kannaks[Gri99]. Kuigi on võimalik levitada seda ühte veapunkti, asendades keskserveri allkirja mitme allakirjutaja lävendallkirjaga, on kontrollitavuse seisukohalt oluline, et allakirjutajad oleksid erinevad ja tuvastatavad. See jätab süsteemi ikkagi haavatavaks, kuna iga allakirjutaja võib ükshaaval ebaõnnestuda või teda võidakse panna ebaõnnestuma.


Selgus, et tsentraalse serveri kasutamine tehingute tellimiseks ei ole elujõuline variant, sest tsensuuri oht on suur. Isegi kui asendada keskserver föderatsiooniga, mis koosneb kindlaksmääratud n serverist, millest vähemalt m peab tellimuse heaks kiitma, tekiksid ikkagi raskused. Probleem muutuks tõepoolest selliseks, kus kasutajad peavad kokku leppima selles n serveri kogumis ja ka selles, kuidas asendada pahatahtlikud serverid headega, ilma et nad peaksid tuginema keskasutusele.


Mõelgem, mis võiks juhtuda, kui Bitcoin oleks tsenseeritav. Tsensor võiks survestada kasutajaid, et nad end identifitseeriksid, teataksid, kust nende raha pärineb või mida nad sellega ostavad, enne kui lubavad oma tehinguid Blockchain-sse sisestada.


Samuti võimaldaks tsensuurivastuse puudumine tsensoril sundida kasutajaid võtma vastu uusi süsteemireegleid. Näiteks võiksid nad kehtestada muudatuse, mis võimaldaks neil paisutada raha Supply, rikastudes seeläbi ise. Sellisel juhul oleks blokeeringuid kontrollival kasutajal kolm võimalust uute reeglitega toimetulemiseks:



- Võtta vastu: Võtta muudatused vastu ja võtta need oma Full node-sse üle.
- Lükake tagasi: Keelduda muudatuste vastuvõtmisest; see jätab kasutajale süsteemi, mis ei töötle enam tehinguid, kuna kasutaja Full node loeb tsensori blokid nüüd kehtetuks.
- Liikumine: määrake uus keskne kontrollpunkt; kõik kasutajad peavad välja mõtlema, kuidas kooskõlastada ja seejärel leppida kokku uues keskmises kontrollpunktis.


Kui see õnnestub, tulevad samad probleemid tõenäoliselt mingil hetkel tulevikus uuesti esile, arvestades, et süsteem jäi sama tsenseeritavaks kui varem.


Ükski neist võimalustest ei ole kasutajale kasulik.


Tsensuurikindlus detsentraliseerimise kaudu on see, mis eristab Bitcoin teistest rahasüsteemidest, kuid *Double-spending probleemi* tõttu ei ole seda lihtne saavutada. See on probleem, mis seisneb selles, et keegi ei saa sama münti kaks korda kulutada, probleem, mida paljud inimesed arvasid, et detsentraliseeritult on võimatu lahendada. Satoshi Nakamoto kirjutab oma [Bitcoin whitepaperis](https://planb.network/Bitcoin.pdf) sellest, kuidas lahendada Double-spending probleem:


> Käesolevas dokumendis pakume välja lahenduse Double-spending probleemile, kasutades võrdõiguslikust jaotatud Timestamp serveriga generate tehingute kronoloogilise järjestuse arvutuslikku tõestamist.


Siinkohal kasutab ta omapäraselt kõlavat väljendit "peer-to-peer jaotatud Timestamp server". Võtmesõnaks on siin *hajutatud*, mis selles kontekstis tähendab, et puudub keskne kontrollpunkt. Seejärel selgitab Nakamoto, kuidas Proof-of-Work on lahendus.

Siiski ei selgita keegi seda paremini kui

[Gregory Maxwell on Reddit](https://www.reddit.com/r/Bitcoin/comments/ddddfl/question_on_the_vulnerability_of_bitcoin/f2g9e7b/), kus ta vastab kellelegi, kes teeb ettepaneku piirata kaevurite Hash võimsust, et vältida võimalikke 51% rünnakuid:


> Detsentraliseeritud süsteem nagu Bitcoin kasutab avalikke valimisi. Kuid detsentraliseeritud süsteemis ei saa lihtsalt "rahva" hääletust korraldada, sest selleks oleks vaja tsentraliseeritud osapoolt, kes volitaks inimesi hääletama. Selle asemel kasutab Bitcoin arvutusvõimsuse hääletust, sest arvutusvõimsust on võimalik kontrollida ilma ühegi tsentraliseeritud
kolmas osapool.


Postituses selgitatakse, kuidas detsentraliseeritud Bitcoin võrk saab Proof-of-Work abil jõuda kokkuleppele tehingu tellimise osas.


Seejärel lõpetab ta, öeldes, et 51% rünnak ei ole eriti murettekitav, võrreldes sellega, et inimesed ei hooli või ei mõista Bitcoin detsentraliseerimisomadusi:


> Bitcoin puhul on palju suurem oht, et seda kasutav avalikkus ei mõista, ei hooli ja ei kaitse neid detsentraliseerimise omadusi, mis teevad selle tsentraliseeritud alternatiivide suhtes väärtuslikuks.

Järeldus on oluline. Kui inimesed ei kaitse Bitcoin detsentraliseeritust, mis on selle tsensuurivastasuse asendaja, võib Bitcoin langeda tsentraliseerivate jõudude ohvriks, kuni see on nii tsentraliseeritud, et tsensuur muutub asjaks. Siis on enamik, kui mitte kogu selle väärtuspakkumine kadunud. See toob meid järgmise jaotise juurde Full node detsentraliseerimise kohta.


### Full node detsentraliseerimine



Ülaltoodud lõigetes rääkisime peamiselt Miner detsentraliseerimisest ja sellest, kuidas kaevandajate tsentraliseerimine võib võimaldada tsensuuri. Kuid on ka teine detsentraliseerimise aspekt, nimelt *Full node detsentraliseerimine*.


Full node detsentraliseerimise tähtsus on seotud usaldamatusega. Oletame, et kasutaja lõpetab oma Full node käitamise näiteks liiga kõrge tegevuskulu tõttu. Sellisel juhul peab ta Bitcoin võrguga suhtlema mõnel muul viisil, kasutades võib-olla veebikassasid või kergekaalu rahakotte, mis eeldab teatud usaldust nende teenuste pakkujate vastu.


Kasutaja läheb võrgu konsensusreeglite otsesest jõustamisest üle usaldusele, et keegi teine seda teeb. Oletame, et enamik kasutajaid delegeerib konsensuse jõustamise usaldusväärsele üksusele. Sellisel juhul võib võrk kiiresti tsentraliseeruda ja võrgu reegleid võivad muuta konspiratiivsed pahatahtlikud osalejad.


In [a

Bitcoin Magazine'i artiklis] (https://bitcoinmagazine.com/technical/decentralist-perspective-Bitcoin-might-need-small-blocks-1442090446) intervjueerib Aaron van Wirdum Bitcoin arendajaid nende seisukohtadest detsentraliseerimise ja Bitcoin maksimaalse plokimahu suurendamisega seotud riskide kohta. See arutelu oli Hot teema 2014-2017 ajastul, kui paljud inimesed vaidlesid plokimahu piirangu suurendamise üle, et võimaldada suuremat tehingu läbilaskevõimet.


Võimas argument plokisuuruse suurendamise vastu on see, et see suurendab verifitseerimiskulusid. Kui verifitseerimiskulud tõusevad, sunnib see mõningaid kasutajaid oma täisnoodide käivitamisest loobuma. See omakorda viib selleni, et rohkem inimesi ei saa süsteemi kasutada Trustless viisil.


Artiklis tsiteeritakse Pieter Wuille'i, kes selgitab Full node tsentraliseerimise riske:


> Kui paljud ettevõtted kasutavad Full node, tähendab see, et neid kõiki tuleb veenda rakendama teistsuguseid reegleid. Teisisõnu: plokkide valideerimise detsentraliseerimine on see, mis annab konsensusreeglitele nende kaalu.
> Kuid kui Full node arv langeks väga madalale, näiteks seetõttu, et kõik kasutavad samu veebikassasid, vahetusi ja SPV- või mobiilikassasid, võib regulatsioon muutuda reaalsuseks. Ja kui ametiasutused saavad reguleerida konsensusreegleid, tähendab see, et nad võivad muuta kõike, mis teeb Bitcoin Bitcoin. Isegi 21 miljoni Bitcoin piiri.

Siin on see. Bitcoin kasutajad peaksid käivitama oma täielikud sõlmed, et takistada reguleerivaid asutusi ja suuri korporatsioone muutmast konsensuse reegleid.


### Neutraalsus



Bitcoin on neutraalne või lubadeta, nagu inimestele meeldib seda nimetada. See tähendab, et Bitcoin ei hooli sellest, kes te olete või milleks te seda kasutate.


Bitcoin on neutraalne, mis on hea ja ainus viis, kuidas see võib toimida. Kui seda kontrolliks mingi organisatsioon, oleks see lihtsalt veel üks virtuaalne objektitüüp ja mul oleks selle vastu null huvi


Niikaua kui sa mängid reeglite järgi, võid seda kasutada nii, nagu sulle meeldib, ilma kelleltki luba küsimata. See hõlmab ka *Mining*, *transiitide* kasutamist ja *protokollide ja teenuste* ehitamist Bitcoin peal:



- Kui *Mining* oleks lubadega protsess, oleks meil vaja keskasutust, kes valiks välja, kellel on lubatud kaevandada. See tooks tõenäoliselt kaasa selle, et kaevandajad peaksid allkirjastama juriidilised lepingud, milles nad nõustuksid

tsenseerida tehinguid vastavalt keskvõimu kapriisidele, mis kaotab Mining eesmärgi.



- Kui Bitcoins *tehinguid sooritavad* inimesed peaksid esitama isikuandmeid, deklareerima, milleks nad tehinguid teevad, või muul viisil tõestama, et nad on tehingu tegemise väärilised, oleks meil vaja ka keskset asutust, mis kinnitaks kasutajaid või tehinguid. See tooks jällegi kaasa tsensuuri ja tõrjutuse.



- Kui arendajad peaksid küsima luba *protokollide* loomiseks Bitcoin peal, siis arendataks ainult neid protokolle, mida keskne arendajaid lubav komisjon lubab. See välistaks valitsuse sekkumise tõttu paratamatult kõik privaatsust säilitavad protokollid ja kõik katsed detsentraliseerimise parandamiseks.


Kõikidel tasanditel püütakse kehtestada piiranguid selle kohta, kes saab Bitcoin milleks kasutada, mis kahjustab Bitcoin nii palju, et see ei vasta enam oma väärtuspakkumisele.


Pieter Wuille https://Bitcoin.stackexchange.com/a/92055/69518 [vastab küsimusele Stack Exchange kohta], kuidas Blockchain on seotud tavaliste andmebaasidega. Ta selgitab, kuidas lubadusteta kasutamine on võimalik Proof-of-Work kasutamise kaudu koos majanduslike stiimulitega.


Ta lõpetab:


> Kasutades Trustless konsensus algoritmid nagu PoW ei lisa midagi, mida ükski teine konstruktsioon ei anna teile (permissionless osalemine, mis tähendab, et ei ole määratud osalejate rühma, mis võib tsenseerida oma muudatusi), Kasutades Trustless konsensus algoritmid nagu PoW ei lisa midagi, kuid tuleb kõrge hinnaga, ja selle majanduslikud eeldused teevad selle üsna palju ainult kasulikud süsteemid, mis määratlevad oma krüptovaluuta.
> Ilmselt on maailmas ainult üks või paar tegelikult kasutatud sellist.

Ta selgitab, et selleks, et saavutada lubadusteta süsteem, vajab see tõenäoliselt omaenda valuutat, mis "piirdub tegelikult ainult krüptovaluutadega". Seda seetõttu, et lubadeta osalemine ehk Mining nõuab süsteemi enda sisse ehitatud majanduslikke stiimuleid.


### Detsentraliseerimise süvenemine



Bitcoin veenev aspekt on see, kui Hard on mõistetav, et keegi ei kontrolli seda. Bitcoin-s ei ole komiteesid ega juhte. Gregory Maxwell, jällegi [Bitcoin subredditis](https://www.reddit.com/r/Bitcoin/comments/s82t2n/comment/htdte7w/?utm_source=share&utm_medium=web2x&context=3), võrdleb seda intrigeerivalt inglise keelega:


> Paljudel inimestel on Hard aeg mõista autonoomseid süsteeme, nende elus on palju asju nagu inglise keel - kuid inimesed võtavad neid lihtsalt enesestmõistetavana ja ei mõtle neist isegi kui süsteemidest. Nad on kinni tsentraliseeritud mõtteviisis, kus kõigel, mida nad peavad "asjaks", on autoriteet, mis seda kontrollib.
>

> Bitcoin ei keskendu millelegi. Erinevad inimesed, kes on Bitcoin kasutusele võtnud, otsustasid omal vabal tahtel seda propageerida, ja see, kuidas nad seda teevad, on nende enda asi. Autoriteedile fikseeritud inimesed võivad näha neid tegevusi ja arvata, et need on mingi Bitcoin autoriteedi operatsioon, kuid sellist autoriteeti ei ole olemas.


See, kuidas Bitcoin detsentraliseerimise kaudu toimib, sarnaneb erakordse kollektiivse intelligentsusega, mida võib leida paljude liikide seas looduses. Arvutiteadlane Radhika Nagpal räägib [Ted talk](https://www.ted.com/talks/radhika_nagpal_what_intelligent_machines_can_learn_from_a_school_of_fish) kalakoolide kollektiivsest käitumisest ja sellest, kuidas teadlased püüavad seda robotite abil jäljendada.


> Teiseks, ja mis minu arvates on ikka veel kõige tähelepanuväärsem, on see, et me teame, et selle kalakooli üle ei ole juhte, kes juhiksid seda kalakooli. Selle asemel tekib see uskumatu kollektiivne meelekäitumine puhtalt ühe ja teise kala omavahelisest suhtlemisest.
> Kuidagi on olemas need naaberkalade vahelised vastastikmõjud või suhtlusreeglid, mis muudavad selle kõik toimivaks.

Ta juhib tähelepanu sellele, et paljud süsteemid, nii looduslikud kui ka kunstlikud, võivad ja toimivad ka ilma juhtideta ning on võimsad ja vastupidavad. Iga üksikisik suhtleb ainult oma vahetu ümbrusega, kuid koos moodustavad nad midagi tohutut.


![](assets/fishschool.webp)

*Kalakoolidel ei ole juhte*


Ükskõik, mida te Bitcoin-st arvate, selle detsentraliseeritud olemus muudab selle kontrollimise keeruliseks. Bitcoin on olemas ja te ei saa selle vastu midagi ette võtta. Seda tuleb uurida, mitte arutada.


### Järeldus detsentraliseerimise kohta


Me eristame Full node detsentraliseerimist ja Mining detsentraliseerimist. Mining detsentraliseerimine on vahend tsensuskindluse saavutamiseks, samas kui Full node detsentraliseerimine on see, mis hoiab võrgu Hard konsensusreeglid muutumatuna ilma kasutajate laialdase toetuseta.


Bitcoin detsentraliseeritud olemus võimaldab neutraalsust arendajate, kasutajate ja kaevurite suhtes. Igaüks võib vabalt osaleda ilma luba küsimata.


Detsentraliseeritud süsteemides võib olla Hard, kuid on olemas mõned mentaalsed mudelid, mis võivad aidata, näiteks inglise keel või kalakoolid.


## Usaldamatus

<chapterId>0506ba61-16a3-543c-95fa-3f3e2dd64121</chapterId>



![](assets/trustlessness-banner.webp)


Selles peatükis analüüsitakse usaldamatuse mõistet, mida see tähendab arvutiteaduse seisukohast ja miks Bitcoin peab olema Trustless, et säilitada oma väärtuspakkumine.

Seejärel räägime sellest, mida tähendab Bitcoin kasutamine Trustless viisil ja milliseid garantiisid Full node saab ja ei saa anda.

Viimases jaotises vaatleme Bitcoin ja tegelike tarkvarade või kasutajate vahelist tegelikku suhtlust ning vajadust teha kompromisse mugavuse ja usaldamatuse vahel, et üldse midagi teha.


Inimesed ütlevad sageli selliseid asju nagu "Bitcoin on suurepärane, sest see on Trustless".


Mida nad Trustless all silmas peavad? Pieter Wuille selgitab seda laialdaselt kasutatavat terminit [Stack Exchange](https://Bitcoin.stackexchange.com/a/45674/69518):


> Usaldus, millest me "Trustless" puhul räägime, on abstraktne tehniline termin. Jaotatud süsteemi nimetatakse Trustless-ks, kui see ei nõua korrektseks toimimiseks ühtegi usaldusväärset osapoolt.

Lühidalt öeldes viitab sõna *Trustless* Bitcoin protokolli omadusele, mille kohaselt võib see loogiliselt toimida ilma "usaldusväärsete osapoolteta". See erineb usaldusest, mida te paratamatult peate rakendatavale tarkvarale või riistvarale avaldama. Seda viimatinimetatud usalduse aspekti käsitletakse käesolevas peatükis lähemalt.


Tsentraliseeritud süsteemides toetume kesksete osalejate mainele, et tagada, et nad hoolitsevad turvalisuse eest või võtavad probleemide korral tagasi, ning õigussüsteemile, et sanktsioneerida rikkumisi. Need usaldusnõuded on pseudonüümsetes detsentraliseeritud süsteemides problemaatilised - puudub võimalus pöörduda, seega ei saa tegelikult mingit usaldust olla. Satoshi Nakamoto kirjeldab seda probleemi [valge raamatu Bitcoin] (https://Bitcoin.org/Bitcoin.pdf) sissejuhatuses:


> Interneti-kaubandus tugineb peaaegu eranditult finantsasutustele, kes on usaldusväärsed kolmandad osapooled elektrooniliste maksete töötlemisel.
> Kuigi süsteem töötab enamiku tehingute puhul piisavalt hästi, on sellel siiski puudusi, mis on omane usaldusel põhinevale mudelile.  Täielikult pöördumatuid tehinguid ei ole tegelikult võimalik teha, sest finantsasutused ei saa vältida vaidluste vahendamist. Vahendusmenetluse kulud suurendavad tehingukulusid, piirates minimaalset praktilist tehingu suurust ja kaotades võimaluse väikesteks juhutehinguteks, ning laiemad kulud seisnevad selles, et mittepöörduvate teenuste eest ei ole võimalik teha mittepöörduvaid makseid.
> Tagasipööramise võimalusega levib vajadus usalduse järele. Kaupmehed peavad olema oma klientide suhtes ettevaatlikud, nõudes neilt rohkem teavet, kui nad muidu vajaksid.  Teatud protsent pettusi aktsepteeritakse kui vältimatuid. Neid kulusid ja makse ebakindlust saab vältida isiklikult, kui kasutada füüsilist raha, kuid puudub mehhanism, et teha makseid sidekanali kaudu ilma usaldusväärse osapooleta

Tundub, et meil ei saa olla detsentraliseeritud süsteemi, mis põhineb usaldusel, ja seetõttu on Bitcoin puhul usaldamatus oluline.


Bitcoin kasutamiseks Trustless viisil peate käivitama täielikult valideeriva Bitcoin sõlme. Ainult siis saate kontrollida, et teistelt saadud plokid järgivad konsensuseeskirju; näiteks, et mündi väljastamise ajakavast peetakse kinni ja et Blockchain-l ei toimu topeltkulutusi. Kui te ei käita Full node-i, annate Bitcoin-i plokkide kontrollimise kellegi teise ülesandeks ja usaldate, et nad teile tõtt räägivad, mis tähendab, et te ei kasuta Bitcoin-i usaldusväärselt.


David Harding on kirjutanud [artikli Bitcoin.org veebilehel](https://Bitcoin.org/en/Bitcoin-core/features/validation), milles ta selgitab, kuidas Full node kasutamine - või Bitcoin usalduseta kasutamine - tegelikult aitab teid:


> Bitcoin valuuta toimib ainult siis, kui inimesed võtavad bitcoin'e Exchange-s vastu muude väärtuslike asjade eest. See tähendab, et inimesed, kes bitcoine vastu võtavad, annavad sellele väärtuse ja otsustavad, kuidas Bitcoin peaks töötama.
>

> Kui te aktsepteerite bitcoin'e, on teil õigus jõustada Bitcoin reegleid, näiteks takistada mis tahes isiku bitcoin'ide konfiskeerimist ilma juurdepääsuta selle isiku privaatvõtmetele.
>

> Kahjuks tellivad paljud kasutajad oma jõustamisvõime sisse. See jätab Bitcoin detsentraliseerimise nõrgestatud olekusse, kus käputäis kaevandajaid võib käputäie pankade ja tasuta teenustega kokku leppida, et muuta Bitcoin reegleid kõigi nende kasutajate jaoks, kes oma võimu välja delegeerisid.
>

> Erinevalt teistest rahakottidest jõustab Bitcoin Core reegleid - kui kaevurid ja pangad muudavad reegleid oma mitte-verifitseerivate kasutajate jaoks, ei saa need kasutajad maksta täieliku valideerimisega Bitcoin Core'i kasutajatele nagu sina.


Ta ütleb, et Full node käivitamine aitab teil kontrollida Blockchain kõiki aspekte, ilma et usaldaksite kedagi teist, et tagada, et teistelt saadud mündid on ehtsad. See on suurepärane, kuid on üks oluline asi, mille puhul Full node ei saa teid aidata: see ei saa takistada topeltkulutusi ahela ümberkirjutamise kaudu:


> Pange tähele, et kuigi kõik programmid - sealhulgas Bitcoin Core - on haavatavad ahela ümberkirjutamise suhtes, pakub Bitcoin kaitsemehhanismi: mida rohkem kinnitusi on teie tehingutel, seda turvalisemad olete. Paremat detsentraliseeritud kaitset ei ole teadaolevalt olemas.

Ükskõik kui arenenud on teie tarkvara, peate siiski usaldama, et teie münte sisaldavaid plokke ei kirjutata ümber. Kuid nagu Harding märkis, võite oodata mitu kinnitust, mille järel peate ahela ümberkirjutamise tõenäosust piisavalt väikeseks, et see oleks vastuvõetav.


Bitcoin kasutamise stiimulid Trustless viisil on kooskõlas süsteemi Full node detsentraliseerimise vajadusega. Mida rohkem inimesi kasutab oma täissõlmi, seda rohkem on Full node detsentraliseeritud ja seega seda tugevam on Bitcoin protokolli pahatahtlike muudatuste vastu. Kuid kahjuks, nagu on selgitatud Full node detsentraliseerimise osas, valivad kasutajad sageli usaldusväärseid teenuseid, mis on paratamatu kompromiss usaldamatuse ja mugavuse vahel.


Bitcoin usaldamatus on süsteemi seisukohast absoluutselt hädavajalik. 2018. aastal rääkis Matt Corallo, [rääkis usaldamatusest](https://btctranscripts.com/baltic-honeybadger/2018/trustlessness-scalability-and-directions-in-security-models/) Balti Honeybadgeri konverentsil Riias.


![video](https://youtu.be/66ZoGUAnY9s?t=4019)


Selle jutu sisuks on see, et Trustless süsteemi ei saa ehitada usaldusväärse süsteemi peale, kuid Trustless süsteemi peale saab ehitada usaldusväärseid süsteeme - näiteks Wallet hooldussüsteemi.



![width=50%](assets/trust.webp)


Trustless baas Layer võimaldab erinevaid kompromisse kõrgematel tasanditel


See turvamudel võimaldab süsteemi projekteerijal valida kompromissid

mis on nende jaoks mõistlikud, ilma et neid kompromisse teistele peale sunniks.


### Ärge usaldage, kontrollige



Bitcoin töötab usaldusväärselt, kuid te peate siiski mingil määral usaldama oma tarkvara ja riistvara. Seda seetõttu, et teie tarkvara või riistvara ei pruugi olla programmeeritud tegema seda, mis on karbil kirjas. Näiteks:



- Protsessor võib olla pahatahtlikult loodud selleks, et tuvastada salajase võtme krüptograafilisi operatsioone ja lekitada salajase võtme andmeid.
- Operatsioonisüsteemi juhuslik numbrigeneraator ei pruugi olla nii juhuslik, kui ta väidab.
- Bitcoin Core võib olla hiilinud sisse koodi, mis saadab teie isiklikud võtmed mõnele kurjategijale.


Nii et lisaks Full node kasutamisele peate veenduma ka selles, et te kasutate seda, mida kavatsete. Redditi kasutaja brianddk [kirjutas artikli](https://www.reddit.com/r/Bitcoin/comments/smj1ep/bitcoin_v220_and_guix_stronger_defense_against/) erinevate usaldustasandite kohta, mille vahel saab tarkvara kontrollimisel valida. Peatükis "Trusting the builders" räägib ta reprodutseeritavatest buildidest:


> Reprodutseeritavad koopiad on viis tarkvara projekteerimiseks nii, et paljud kogukonna arendajad saavad igaüks tarkvara ehitada ja tagada, et lõplik installeerija on identne teiste arendajate toodanguga. Sellise väga avaliku, paljundatava projekti puhul nagu Bitcoin ei pea ühtegi arendajat täielikult usaldama. Paljud arendajad saavad kõik teha buildi ja kinnitada, et nad on tootnud sama faili, mille algne koostaja on digitaalselt allkirjastanud.

Artiklis on määratletud 5 usalduse taset: usaldus saidi, koostajate, kompilaatori, tuuma ja riistvara vastu.


Et süvendada reprodutseeritavate buildide teemat, tegi Carl Dong [ettekande Guixi kohta](https://btctranscripts.com/breaking-Bitcoin/2019/Bitcoin-build-system/), milles selgitas, miks usaldus operatsioonisüsteemi, raamatukogude ja kompilaatorite vastu võib olla problemaatiline ja kuidas seda parandada süsteemiga nimega Guix, mida Bitcoin Core täna kasutab.


> Mida saame siis teha seoses sellega, et meie tööriistakett võib sisaldada hulga usaldusväärseid binaarsüsteeme, mis võivad olla reprodutseeritavalt pahatahtlikud? Me peame olema rohkem kui reprodutseeritavad. Me peame olema käivitatavad. Meil ei saa olla nii palju binaartööriistu, mida me peame alla laadima ja usaldama teiste organisatsioonide poolt kontrollitud välistest serveritest.
>

> Me peaksime teadma, kuidas need tööriistad on ehitatud ja kuidas täpselt saame neid uuesti ehitada, eelistatavalt palju väiksema hulga usaldusväärsete binaarkoodide põhjal. Me peame minimeerima oma usaldusväärsete binaarsüsteemide kogumit nii palju kui võimalik ja meil peab olema kergesti kontrollitav tee nendest tööriistakettidest selleni, mida me kasutame, kuidas Bitcoin ehitada. See võimaldab meil maksimeerida kontrollimist ja minimeerida usaldust.

Seejärel selgitab ta, kuidas Guix võimaldab meil usaldada ainult minimaalset binaarset 357 baiti, mida saab kontrollida ja täielikult mõista, kui te teate, kuidas juhiseid tõlgendada. See on üsna tähelepanuväärne: kontrollitakse, et 357 baidi pikkune binaarsüsteem teeb seda, mida ta peaks tegema, seejärel kasutatakse seda täieliku build-süsteemi ehitamiseks lähtekoodist ja tulemuseks on Bitcoin Core'i binaarsüsteem, mis peaks olema täpne koopia kellegi teise build'ist.


On üks mantra, mida paljud bitcoin'i kasutajad järgivad ja mis võtab hästi kokku suure osa ülaltoodust:


> Ärge usaldage, kontrollige.

See viitab fraasile "[trust, but verify](https://en.wikipedia.org/wiki/Trust,_but_verify)", mida USA endine president Ronald Reagan kasutas tuumadesarmeerimise kontekstis. [Bitcoiners](https://twitter.com/Truthcoin/status/1491415722123153408?s=20&t=ZyROxZxlBppdRpuuzsiF5w) vahetas selle ümber, et rõhutada usalduse tagasilükkamist ja Full node käivitamise tähtsust.


Kasutajad peavad ise otsustama, mil määral nad soovivad kontrollida kasutatavat tarkvara ja saadud Blockchain andmeid. Nagu nii paljude muude asjade puhul Bitcoin puhul, on mugavuse ja usaldamatuse vahel kompromiss. Peaaegu alati on mugavam kasutada eestkostetavat Wallet võrreldes Bitcoin Core'i käivitamisega oma riistvaral. Kuid kuna Bitcoin tarkvara on küpsemas ja kasutajaliidesed paranevad, peaks see aja jooksul toetama paremini kasutajaid, kes on valmis töötama usaldamatuse suunas. Samuti peaksid kasutajad aja jooksul, kui nad omandavad rohkem teadmisi, olema võimelised järk-järgult usaldust kaotama.


Mõned kasutajad mõtlevad vastandlikult ja kontrollivad enamikku nende kasutatava tarkvara aspekte. Selle tulemusena vähendavad nad usalduse vajadust miinimumini, sest nad peavad usaldama ainult oma arvuti riistvara ja operatsioonisüsteemi. Seejuures aitavad nad ka neid, kes ei kontrolli oma riistvara nii põhjalikult, tõstes avalikult häält, et hoiatada võimalike probleemide eest. Üks hea näide sellest on [2018. aastal toimunud sündmus](https://bitcoincore.org/en/2018/09/20/notice/), kui keegi avastas vea, mis võimaldas kaevandajatel kulutada väljundit kaks korda sama tehingu käigus:


> CVE-2018-17144, mille parandus avaldati 18. septembril Bitcoin Core versioonides 0.16.3 ja 0.17.0rc4, sisaldab nii teenusetõkestuse komponenti kui ka kriitilist inflatsioonihaavatavust. Algselt teatati sellest mitmetele Bitcoin Core'i ja teisi krüptovaluutasid toetavate projektide, sealhulgas ABC ja Unlimitedi arendajatele 17. septembril ainult teenusetõrjevigana, kuid me tuvastasime kiiresti, et probleem on ka inflatsioonihaavatavus, mille algpõhjus ja parandus on sama.

Siin teatas anonüümne isik probleemist, mis osutus palju hullemaks, kui reporter aru sai. See toob esile asjaolu, et inimesed, kes kontrollivad koodi, teatavad sageli turvavigadest, selle asemel et neid ära kasutada. See on kasulik neile, kes ei suuda kõike ise kontrollida.


Kasutajad ei tohiks siiski usaldada, et teised neid turvata, vaid peaksid pigem ise kontrollima, millal ja mida iganes nad saavad; nii jääb inimene võimalikult suveräänseks ja Bitcoin õitseb. Mida rohkem silmi on tarkvaral, seda väiksem on tõenäosus, et pahatahtlik kood ja turvaaugud lipsavad läbi.


### Järeldus usaldamatuse kohta



Bitcoin protokoll on Trustless, sest see võimaldab kasutajatel suhelda sellega ilma kolmandat osapoolt usaldamata. Praktikas ei suuda enamik inimesi siiski kontrollida kogu tarkvara ja riistvara virna, millel nad Bitcoin kasutavad. Kvalifitseeritud inimesed, kes kontrollivad tarkvara või riistvara, suudavad hoiatada teisi, vähemkvalifitseeritud inimesi, kui nad leiavad pahatahtlikku koodi või vigu.


Ilma usaldamatuseta ei saa meil olla detsentraliseerimist, sest usaldus eeldab paratamatult mingit keskse võimu olemasolu. Trustless süsteemi peale saab ehitada usaldusväärse süsteemi, kuid Trustless süsteemi ei saa ehitada usaldusväärse süsteemi peale.


## Privaatsus

<chapterId>1b960afe-0008-589b-b2f4-007d60d264c6</chapterId>



![](assets/privacy-banner.webp)


See peatükk käsitleb seda, kuidas hoida oma isiklikku finantsteavet enda jaoks. Selles selgitatakse, mida tähendab privaatsus Bitcoin kontekstis, miks see on oluline ja mida tähendab, et Bitcoin on pseudonüümne. Samuti vaadeldakse, kuidas privaatsed andmed võivad lekkida, nii On-Chain kui ka off-chain.


Seejärel räägitakse sellest, et bitcoinid peaksid olema asendatavad, st vahetatavad mis tahes teiste bitcoinide vastu, ning sellest, kuidas asendatavus ja privaatsus käivad käsikäes. Lõpuks tutvustatakse peatükis mõningaid meetmeid, mida saate võtta, et parandada oma ja teiste privaatsust.


Bitcoin võib kirjeldada kui pseudonüümset süsteemi, kus kasutajatel on mitu pseudonüümi avalike võtmete kujul. Esmapilgul tundub see olevat päris hea viis kasutajate tuvastamise eest kaitsmiseks, kuid tegelikult on väga lihtne tahtmatult lekitada privaatset finantsteavet.


### Mida tähendab privaatsus?



Privaatsus võib erinevates kontekstides tähendada erinevaid asju. Bitcoin puhul tähendab see üldiselt seda, et kasutajad ei pea oma finantsteavet teistele avaldama, välja arvatud juhul, kui nad seda vabatahtlikult teevad.


On palju viise, kuidas te võite oma privaatseid andmeid teistele lekitada, kas teadlikult või teadmatult. Andmed võivad lekkida kas avalikust Blockchain või muude vahendite kaudu, näiteks kui pahatahtlikud isikud teie internetisuhtlust pealtkuulavad.


### Miks on privaatsus oluline?


Võib tunduda ilmselge, miks privaatsus on Bitcoin puhul oluline, kuid on mõned aspektid, millele ei pruugi kohe mõelda. [Bitcoin Talk foorumis] (https://bitcointalk.org/index.php?topic=334316.msg3588908#msg3588908) tutvustab Gregory Maxwell meile palju häid põhjusi, miks tema arvates on privaatsus oluline. Nende hulgas on vaba turg, turvalisus ja inimväärikus:


> Finantsprivaatsus on vaba turu tõhusa toimimise oluline kriteerium: kui te juhite ettevõtet, ei saa te tõhusalt hindu määrata, kui teie tarnijad ja kliendid näevad kõiki teie tehinguid teie tahte vastaselt.
> Te ei saa tõhusalt konkureerida, kui teie konkurendid jälgivad teie müüki.  Individuaalselt on teie informatsiooniline mõjuvõim kaotatud teie isiklikes suhetes, kui teil ei ole privaatsust oma kontode üle: kui te maksate oma üürileandjale Bitcoin-s ilma piisava privaatsuseta, näeb teie üürileandja, millal te olete saanud palgatõusu, ja võib teid rohkem üüri nõuda.
>

> Rahaline privaatsus on isikliku turvalisuse seisukohalt oluline: kui vargad näevad teie kulutusi, sissetulekut ja varasid, saavad nad seda teavet kasutada teie sihtimiseks ja ärakasutamiseks. Ilma privaatsuseta on pahatahtlikel osapooltel rohkem võimalusi teie identiteedi varastamiseks, teie suurte ostude äravõtmiseks või teiega tehtavaid tehinguid sooritavate ettevõtete kehastamiseks teie suunas... nad saavad täpselt teada, kui palju nad teid petta tahavad.
>

> Rahaline privaatsus on inimväärikuse seisukohalt oluline: keegi ei taha, et nohiklik barista kohvikus või uudishimulikud naabrid kommenteeriksid tema sissetulekuid või kulutamisharjumusi. Keegi ei taha, et nende lapsehullud ämmad küsiksid, miks nad rasestumisvastaseid vahendeid (või seksimänguasju) ostavad. Teie tööandjal ei ole vaja teada, millisele kirikule te annetate. Ainult täiesti valgustatud diskrimineerimisvabas maailmas, kus kellelgi ei ole põhjendamatut võimu kellegi teise üle, saaksime säilitada oma väärikuse ja teha oma seaduslikke tehinguid vabalt ilma enesetsensuurita, kui meil ei ole privaatsust.

Maxwell puudutab ka asendatavust, mida käsitletakse hiljem selles peatükis, ning seda, kuidas eraelu puutumatus ja õiguskaitse ei ole omavahel vastuolus.


### Pseudonüümsus


Eespool mainisime, et Bitcoin on pseudonüümne ja et pseudonüümid on avalikud võtmed. Meedias kuuleb sageli, et Bitcoin on anonüümne, mis ei vasta tõele. Anonüümsuse ja pseudonüümsuse vahel on erinevus.


Andrew Poelstra [selgitab Bitcoin Stack Exchange postituses](https://Bitcoin.stackexchange.com/a/29473/69518), kuidas anonüümsus tehingutes välja näeks:


> Täielik anonüümsus selles mõttes, et raha kulutamisel ei ole mingit jälge sellest, kust see on pärit või kuhu see läheb, on teoreetiliselt võimalik, kasutades krüptograafilist tehnikat, milleks on null-teadmiste tõestamine.

Erinevus näib olevat selles, et pseudonüümse raha puhul on võimalik jälgida makseid pseudonüümide vahel, samas kui anonüümse raha puhul ei ole seda võimalik. Kuna Bitcoin maksed on pseudonüümide vahel jälgitavad, ei ole tegemist anonüümse süsteemiga.


Oleme ka öelnud, et pseudonimed on avalikud võtmed, kuid tegelikult on tegemist avalike võtmete põhjal tuletatud aadressidega. Miks me kasutame pseudonüümidena aadresse ja mitte midagi muud, näiteks mingeid kirjeldavaid nimesid, nagu "watchme1984"? Seda on [hästi](https://Bitcoin.stackexchange.com/a/25175/69518) selgitanud kasutaja Tim S., samuti Bitcoin Stack Exchange:


> Selleks, et Bitcoin idee toimiks, peavad teil olema mündid, mida saab kulutada ainult konkreetse isikliku võtme omanik. See tähendab, et mis iganes sa saadad, peab olema mingil viisil seotud avaliku võtmega.
>

> Kui kasutate suvalisi pseudonüüme (nt kasutajanimesid), tähendab see, et peate seejärel kuidagi siduma pseudonüümi avaliku võtmega, et võimaldada avaliku/privaatvõtme krüptograafiat. See kaotaks võimaluse luua turvaliselt aadressid/pseudonüümid offline (nt enne, kui keegi saaks saata raha kasutajanimele "tdumidu", peaksite Blockchain-s teatama, et "tdumidu" kuulub avalikule võtmele "a1c...", ja lisama tasu, et teistel oleks põhjust seda teatada), vähendaks anonüümsust (julgustades teid pseudonüüme uuesti kasutama) ja paisutaks tarbetult Blockchain suurust. Samuti tekitaks see vale turvatunde, et sa saadad sellele, kellele sa arvad end olevat (kui ma võtan nime "Linus Torvalds" enne teda, siis on see minu nimi ja inimesed võivad saata raha, arvates, et nad maksavad Linuxi loojale, mitte mulle).

Aadresside ehk avalike võtmete kasutamisega saavutame olulisi eesmärke, näiteks kaotame vajaduse pseudonüümi eelnevaks registreerimiseks, vähendame pseudonüümi korduvkasutamise stiimuleid, väldime Blockchain paisumist ja muudame teiste inimeste kehastamise raskemaks.


### Blockchain privaatsus



Blockchain privaatsus viitab teabele, mida te Blockchain kaudu tehingutega avalikustate. See kehtib kõigi tehingute kohta, nii nende kohta, mida te saadate kui ka nende kohta, mida te saate.


Satoshi Nakamoto mõtiskleb On-Chain privaatsuse üle oma [Bitcoin whitepaper](https://Bitcoin.org/Bitcoin.pdf) punktis 7:


> Täiendava tulemüürina tuleks iga tehingu puhul kasutada uut võtmepaari, et vältida nende seostamist ühise omanikuga. Mõningane seostamine on siiski vältimatu mitme sisendiga tehingute puhul, mis ilmselgelt näitavad, et nende sisendid kuuluvad samale omanikule. Risk on, et kui võtme omanik paljastub, võib linkimine paljastada teised tehingud, mis kuulusid samale omanikule.

Artiklis võetakse kokku Blockchain privaatsuse peamised probleemid, nimelt Address korduvkasutamine ja Address klasterdamine. Esimene on iseenesestmõistetav, viimane viitab võimalusele otsustada teatud kindlusega, et erinevate aadresside kogum kuulub samale kasutajale.


![](assets/address-reuse-clustering.webp)


Blockchain tüüpilised privaatsuse lekked


Chris Belcher [kirjutas väga üksikasjalikult](https://en.Bitcoin.it/Privacy#Blockchain_attacks_on_privacy) erinevatest eraelu puutumatuse leketest, mis võivad juhtuda Bitcoin Blockchain puhul. Soovitame lugeda vähemalt esimesed alapeatükid "Blockchain rünnakud privaatsusele"


Tulemuseks on see, et Bitcoin privaatsus ei ole täiuslik. See nõuab märkimisväärset tööd, et teha eraviisilisi tehinguid. Enamik inimesi ei ole valmis privaatsuse nimel nii kaugele minema. Tundub, et privaatsuse ja kasutatavuse vahel on selge kompromiss.


Teine oluline eraelu puutumatuse aspekt on see, et meetmed, mida võtate oma eraelu puutumatuse kaitsmiseks, mõjutavad ka teisi kasutajaid. Kui te olete oma privaatsusega hooletu, võivad ka teised inimesed kogeda eraelu puutumatuse vähenemist. Gregory Maxwell selgitab seda väga selgelt samas Bitcoin Talki arutelus [mille me eespool linkisime] (https://bitcointalk.org/index.php?topic=334316.msg3589252#msg3589252) ja lõpetab selle ühe näitega:


> See toimib tegelikult ka praktikas... Üks kena whitehat häkker IRC-is mängis brainwalleti kräkkimisega ja tabas fraasi, kus oli ~250 BTC sees.  Me suutsime omaniku tuvastada ainuüksi Address järgi, sest neile oli maksnud Bitcoin teenus, mis taaskasutas aadresse ja ta suutis neid veenda andma kasutajate kontaktandmeid. Ta sai kasutaja tegelikult telefoni teel kätte, nad olid šokeeritud ja segaduses, kuid tänulikud, et ei ole oma mündi eest väljas.  Õnnelik lõpp. (See ei ole kaugeltki ainus näide ... kuid see on üks lõbusamaid).

Antud juhul läks kõik hästi tänu heategevuslikult mõtlevale häkkerile, kuid järgmine kord ei tasu sellega arvestada.


### Mitte-Blockchain privaatsus


Kuigi Blockchain osutub kurikuulsaks eraelu puutumatuse lekete allikaks, on palju muid lekkeid, mis ei kasuta Blockchain, mõned neist on salakavalamad kui teised. Need ulatuvad võtmelogijatest võrguliikluse analüüsini. Mõne sellise meetodi kohta lugege uuesti [Chris Belcheri teosest] (https://en.Bitcoin.it/Privacy#Non-blockchain_attacks_on_privacy), eriti lõigust "Non-Blockchain rünnakud privaatsusele".


Belcher mainib paljude rünnakute hulgas võimalust, et keegi, näiteks teie Interneti-ühendus, nuhkib teie Interneti-ühenduse üle, näiteks teie Interneti-teenuse pakkuja:


> Kui vastane näeb, et teie sõlmpunktist tuleb välja tehing või plokk, mida varem ei ole sisestatud, siis saab ta peaaegu kindlalt teada, et tehingu tegid teie või ploki kaevandasite teie. Kuna tegemist on internetiühendustega, suudab vastane seostada IP Address ja avastatud Bitcoin teavet.

Kõige ilmsemad eraelu puutumatuse lekked on aga vahetused. Seaduste tõttu, mida tavaliselt nimetatakse KYC (Know Your Customer) ja AML (Anti-Money Laundering) seadusteks, mis kehtivad jurisdiktsioonides, kus nad tegutsevad, peavad börsid ja nendega seotud ettevõtted sageli koguma oma kasutajate kohta isikuandmeid, luues suuri andmebaase selle kohta, millised kasutajad milliseid bitcoine omavad. Need andmebaasid on suurepärased mesipuud kurjade valitsuste ja kurjategijate jaoks, kes otsivad pidevalt uusi ohvreid. Selliste andmete jaoks on olemas tegelikud turud, kus häkkerid

müüa andmeid enim pakkuvale pakkujale.


Asja teeb veelgi hullemaks see, et neid andmebaase haldavatel ettevõtetel on sageli vähe kogemusi finantsandmete kaitsmisega, tegelikult on paljud neist noored alustavad ettevõtted ja me teame kindlalt, et mitmed lekked on juba toimunud. Mõned näited on järgmised

[Indias asuv MobiQwik](https://bitcoinmagazine.com/business/probably-the-largest-kyc-data-leak-in-history-demonstrates-the-importance-of-Bitcoin-privacy) ja [HubSpot](https://bitcoinmagazine.com/business/hubspot-security-breach-leaks-Bitcoin-users-data).


Jällegi, andmete kaitsmine nii paljude rünnakute eest on Hard ja tõenäoliselt ei suuda te seda täielikult teha. Peate valima mugavuse ja privaatsuse vahel kompromissi, mis teile kõige paremini sobib.


### Süütamisvõime


Vahetatavus tähendab valuutade kontekstis seda, et üks münt on vahetatav mis tahes teise sama valuuta mündi vastu. See on naljakas

sõna puudutasime lühidalt varem selles peatükis.


Artiklis, mida seal käsitleti, Gregory Maxwell [märkis](https://bitcointalk.org/index.php?topic=334316.msg3588908#msg3588908):


> Rahaline privaatsus on Bitcoin puhul asendatavuse oluline element: kui te suudate ühe mündi teistest oluliselt eristada, siis on nende asendatavus nõrk. Kui meie vahetatavus on praktikas liiga nõrk, siis ei saa me olla detsentraliseeritud: kui keegi oluline teatab nimekirja varastatud müntidest, millest ta ei võta vastu tuletatud münte, siis peate hoolikalt kontrollima münte, mida te aktsepteerite, selle nimekirjaga võrreldes ja tagastama need, mis ei vasta nõuetele.  Igaüks jääb kinni erinevate asutuste väljastatud mustade nimekirjade kontrollimisega, sest selles maailmas ei tahaks me kõik halbu münte kätte saada. See lisab hõõrdumist ja tehingukulusid ning muudab Bitcoin rahana vähem väärtuslikuks.

Siinkohal räägib ta ohust, mis tuleneb asendatavuse puudumisest. Oletame, et teil on UTXO. Selle UTXO ajalugu saab tavaliselt jälgida mitu hopsu tagasi, laiutades hulgaliselt eelnevaid väljundeid. Kui mõni neist väljunditest oli seotud ebaseadusliku, soovimatu või kahtlase tegevusega, siis võivad mõned teie mündi potentsiaalsed vastuvõtjad selle tagasi lükata. Kui arvate, et teie makse saajad kontrollivad teie münte mõne tsentraliseeritud valge või musta nimekirja teenuse alusel, võiksite kindluse mõttes hakata ka teie saadud münte kontrollima. Tulemuseks on see, et halb asendatavus toetab veelgi halvemat asendatavust.


Adam Back ja Matt Corallo [pidasid 2016. aastal Milanos toimunud Scaling Bitcoin konverentsil ettekande asendatavusest] (https://btctranscripts.com/scalingbitcoin/milan-2016/fungibility-overview/). Nad mõtlesid samadel põhimõtetel:


> Bitcoin toimimiseks on vaja asendatavust. Kui sa saad münte ja ei saa neid kulutada, siis hakkad kahtlema, kas sa saad neid kulutada. Kui on kahtlusi saadud müntide suhtes, siis lähevad inimesed taintiteenistuste juurde ja kontrollivad, kas "kas need mündid on õnnistatud" ja siis keelduvad inimesed kauplemast. See muudab Bitcoin detsentraliseeritud lubadeta süsteemist tsentraliseeritud lubadega süsteemiks, kus sul on "IOU" musta nimekirja pakkujatelt.

Tundub, et privaatsus ja asendatavus käivad käsikäes. Kui privaatsus on nõrk, nõrgeneb fungiilsus, sest näiteks soovimatute inimeste mündid võivad sattuda musta nimekirja. Samamoodi nõrgeneb privaatsus, kui vahetatavus on nõrk: kui on olemas must nimekiri, peate te küsima musta nimekirja pakkujatelt, milliseid münte vastu võtta, ning see võib avaldada teie IP Address, e-posti Address ja muud tundlikku teavet. Need kaks omadust on omavahel nii tihedalt seotud, et kummastki neist eraldi rääkida on Hard.


### Privaatsusmeetmed



On välja töötatud mitu tehnikat, mis aitavad inimestel kaitsta end eraelu puutumatuse lekete eest. Kõige ilmsemad neist on, nagu Nakamoto varem märkis, unikaalsete

aadressid iga tehingu puhul, kuid on olemas ka mitmeid teisi. Me ei hakka teid õpetama, kuidas saada privaatsusninjaks. Kuid Bitcoin Q+A on [kiire kokkuvõte privaatsust suurendavatest tehnoloogiatest](https://bitcoiner.guide/privacytips/), mis on mõnevõrra järjestatud selle järgi, kuidas Hard neid rakendada. Kui te seda loete, märkate, et Bitcoin privaatsus on sageli seotud asjadega väljaspool Bitcoin. Näiteks ei tohiks te oma bitcoinidega hooplema hakata ja te peaksite kasutama Tor'i ja VPN-i.


Postituses on loetletud ka mõned meetmed, mis on otseselt seotud Bitcoin-ga:


- Full node: Kui te ei kasuta oma Full node, siis lekib palju teavet teie Wallet kohta internetis asuvatele serveritele. Full node kasutamine on suurepärane esimene samm.
- Lightning Network: Bitcoin peal on olemas mitu protokolli, näiteks Lightning Network ja Blockstream'i Liquid Sidechain.
- CoinJoin: võimalus mitme inimese tehingute ühendamiseks üheks, mis raskendab ahelanalüüsi tegemist.


Breaking Bitcoin konverentsil toimunud [ettekandes](https://btctranscripts.com/breaking-Bitcoin/2019/breaking-Bitcoin-privacy/) andis Chris Belcher huvitava praktilise näite, kuidas privaatsust on parandatud:


> Nad olid Bitcoin kasiino. Online-hasartmängud ei ole USAs lubatud. Kõigi Coinbase'i klientide, kes hoiustasid otse Bustabitile, kontod suleti, sest Coinbase jälgis seda. Bustabit tegi paar asja. Nad tegid midagi, mida nimetatakse muutuste vältimiseks, kus sa lähed läbi- ja vaatad, kas saad konstrueerida tehingu, millel ei ole muutuste väljundit. See säästab Miner tasusid ja takistab ka analüüsi.
>

> Samuti importisid nad oma tihedalt kasutatud korduvkasutatavad hoiuseaadressid joinmarketisse. Sel hetkel ei saanud coinbase.com kliendid kunagi keeldu. Tundub, et Coinbase'i järelevalveteenus ei suutnud pärast seda analüüsi teha, nii et neid algoritme on võimalik rikkuda.

Ta mainis seda näidet teiste hulgas ka Bitcoin wiki [Privacy page](https://en.Bitcoin.it/Privacy) leheküljel.


Pange tähele, kuidas paremat privaatsust on võimalik saavutada, kui ehitada süsteemid Bitcoin peale, nagu see on Lightning Network puhul:


![image](assets/privacy.webp)


Bitcoin peal olevad kihid võivad lisada privaatsust


Eelmises lõputöös märkisime, et usalduse vajadus võib ainult suureneda, kui kihte peale panna, kuid see ei tundu kehtivat privaatsuse kohta, mida saab meelevaldselt parandada või halvendada kihtide peal. Miks see nii on? Iga Layer, mis on Bitcoin peal, nagu on selgitatud tulevases peatükis "Kihiline skaleerimine", peab aeg-ajalt kasutama On-Chain tehinguid, sest muidu ei oleks see "Bitcoin peal". Privaatsust suurendavad kihid püüavad üldjuhul kasutada põhilist Layer nii vähe kui võimalik, et minimeerida avalikustatud teabe hulka.


Ülaltoodud on mõnevõrra tehnilised viisid teie privaatsuse parandamiseks. Kuid on ka teisi võimalusi. Selle peatüki alguses ütlesime, et Bitcoin on pseudonüümne süsteem. See tähendab, et Bitcoin kasutajaid ei teata nende tegelike nimede ega muude isikuandmete, vaid nende avalike võtmete järgi. Avalik võti on kasutaja pseudonüüm ja kasutajal võib olla mitu pseudonüümi. Ideaalis on teie isiklik identiteet lahutatud teie Bitcoin pseudonüümidest. Kahjuks väheneb see lahtisidumine käesolevas peatükis kirjeldatud privaatsusprobleemide tõttu tavaliselt aja jooksul.


Isikuandmete avalikustamise riski vähendamiseks ei tohi neid üldse välja anda ega anda neid tsentraliseeritud teenustele, mis loovad suuri andmebaase, mis võivad lekkida. Bitcoin Q+A artiklis [selgitab KYC] (https://bitcoiner.guide/nokyconly/) ja sellest tulenevaid ohte. Samuti pakutakse välja mõned sammud, mida saate teha oma olukorra parandamiseks:


> Õnneks on olemas mõned võimalused Bitcoin ostmiseks ilma KYC-i allikateta. Need on kõik P2P (peer to peer) vahetused, kus te kauplete otse teise üksikisikuga, mitte tsentraliseeritud kolmanda osapoolega. Kahjuks müüvad mõned ka muid münte kui Bitcoin, seega soovitame teil olla ettevaatlik.

Artiklis soovitatakse vältida KYC/AMLi nõudvate börside kasutamist ja selle asemel kaubelda privaatselt või kasutada detsentraliseeritud börse nagu [bisq](https://bisq.network/).


https://planb.network/en/tutorials/exchange/peer-to-peer/bisq-fe244bfa-dcc4-4522-8ec7-92223373ed04

Vastumeetmete kohta põhjalikumat teavet leiate eelnevalt mainitud [privaatsust käsitlevast wikiartiklist](https://en.Bitcoin.it/wiki/Privacy#Methods_for_improving_privacy_.28non-Blockchain.29), alustades punktist "Meetodid privaatsuse parandamiseks (mitte-Blockchain)".


### Järeldus privaatsuse kohta



Privaatsus on väga oluline, kuid Hard saavutada. Privaatsust ei ole olemas.


Selleks, et saada Bitcoin-s korralik privaatsus, peate võtma aktiivseid meetmeid, millest mõned on kulukad ja aeganõudvad.


## Lõplik Supply

<chapterId>af125ba2-ef98-5905-8895-41a538fe5ea5</chapterId>



![](assets/finitesupply-banner.webp)


Selles peatükis vaadeldakse Bitcoin Supply piiri 21 miljonit BTC, või kui palju see tegelikult on? Räägime sellest, kuidas seda piirmäära jõustatakse ja mida saab teha, et kontrollida, kas sellest kinni peetakse. Lisaks heidame pilgu kristallkuuli ja arutame dünaamikat, mis tuleb mängu, kui Block reward läheb subsiidiumipõhiselt tasupõhiseks üle.


Bitcoin fundamentaalseks omaduseks peetakse tuntud piiratud Supply 21 miljonit BTC. Kuid kas see on tõesti kivisse raiutud?


Alustame sellest, mida ütlevad praegused konsensusreeglid Supply Bitcoin kohta ja kui palju sellest tegelikult kasutada saab. Pieter Wuille kirjutas selle kohta [Stack Exchange](https://Bitcoin.stackexchange.com/a/38998/69518), kus ta arvutas, kui palju bitmünte jääb, kui kõik mündid on kaevandatud:


> Kui te summeerite kõik need numbrid kokku, saate 20999999.9769 BTC.

Kuid mitmetel põhjustel - näiteks varajased probleemid coinbase'i tehingutega, kaevurid, kes tahtmatult nõuavad vähem kui lubatud, ja privaatvõtmete kadumine - ei jõua see ülempiir kunagi kohale. Wuille järeldab:


> See jätab meile 20999817.31308491 BTC (võttes arvesse kõike kuni plokki 528333)

Erinevad rahakotid on aga kadunud või varastatud, tehinguid on saadetud valele Address-le, inimesed on unustanud, et neil on Bitcoin. Kokku võib see olla miljoneid. Inimesed on püüdnud kokku lugeda teadaolevaid kaotusi [siin](https://bitcointalk.org/index.php?topic=7253.0).


See jätab meile: ??? BTC.


Seega võime olla kindlad, et Bitcoin Supply on maksimaalselt 20999817.31308491 BTC. Igasugune kadunud või tõendamata põletatud müntide arv teeb selle numbri väiksemaks, kuid me ei tea, kui palju. Huvitav on see, et see ei ole tegelikult oluline, või veel parem, et see on Bitcoin omanike jaoks positiivses mõttes oluline,

[nagu selgitas](https://bitcointalk.org/index.php?topic=198.msg1647#msg1647) Satoshi Nakamoto:


> Kaotatud mündid muudavad ainult kõigi teiste müntide väärtuse veidi suuremaks.  Mõelge sellele kui annetusele kõigile.

Piiratud Supply kahaneb ja see peaks vähemalt teoreetiliselt põhjustama hinnalanguse.


Ringluses olevate müntide täpsest arvust tähtsam on viis, kuidas Supply piirangut ilma keskvõimuorganita jõustatakse. Alias chytrik paneb selle hästi kirja [Stack Exchange](https://Bitcoin.stackexchange.com/a/106830/69518):


> Nii et vastus on, et te ei pea usaldama kedagi, et ta ei suurendaks Supply. Sa pead lihtsalt käivitama mingi koodi, mis kontrollib, et nad ei ole seda teinud.

Isegi kui mõned täielikud sõlmed pöörduvad pimedale poole ja otsustavad vastu võtta suurema väärtusega coinbase'i tehinguid sisaldavaid plokke, siis kõik ülejäänud täielikud sõlmed lihtsalt jätavad need tähelepanuta ja jätkavad oma tegevust tavapäraselt. Mõned täielikud sõlmed võivad tahtlikult või tahtmatult käivitada kurja tarkvara, kuid kollektiiv kindlustab Blockchain kindlalt. Kokkuvõttes võite valida, kas usaldada süsteemi, ilma et peaksite kedagi usaldama.


### Blokeeritud subsiidium ja tehingutasud



Block reward koosneb plokksubsiidiumist ja tehingutasudest. Block reward peab katma Bitcoin turvakulud. Me võime kindlalt öelda, et tänastes tingimustes, mis on seotud plokksubsiidiumi, tehingutasude, Bitcoin hinna, Mempool suuruse, Hash võimsuse, detsentraliseerituse määra jne, on stiimulid igale mängijale reeglite järgimiseks piisavalt suured, et säilitada turvaline rahasüsteem.


Mis juhtub, kui blokeeritud toetus läheneb nullile? Et asi oleks lihtne, oletame, et see on tegelikult võrdne nulliga. Sel hetkel kaetakse süsteemi turvakulud ainult tehingutasude kaudu. Mida toob meile tulevik, kui see juhtub, ei saa me teada. Ebakindlustegureid on palju ja me jääme spekuleerima. Näiteks Paul Sztorci panus antud teemasse [tema Truthcoini blogis](https://www.truthcoin.info/blog/security-budget/) on enamasti spekulatsioonid, kuid tal on vähemalt üks kindel punkt (pange tähele, et M2, millele Sztorc viitab, on fiatraha Supply mõõtühik):


> Kuigi need kaks on segatud ühte ja samasse "julgeolekueelarvesse", on blokeeritud toetus ja txn-tasud täiesti ja täiesti erinevad. Nad on teineteisest sama erinevad, nagu "VISA kogukasum 2017. aastal" on "M2 kogukasvust 2017. aastal".

Täna on omanikud need, kes maksavad turvalisuse eest (raha inflatsiooni kaudu). Homme on kulutajate kord seda koormat kuidagi kanda, nagu allpool näidatud.


![image](assets/finitesupply.webp)


Aja möödudes nihkub julgestuskulude kandmine valdajatelt kulutajatele


Kui tehingutasud on Mining peamine motivatsioon, muutuvad stiimulid. Eelkõige, kui Mempool Miner ei sisalda piisavalt tehingutasusid, võib selle Miner jaoks muutuda kasumlikumaks Bitcoin ajaloo ümberkirjutamine, selle asemel et seda pikendada. Bitcoin Optechil on konkreetne [seda käitumist käsitlev lõik](https://bitcoinops.org/en/topics/fee-sniping/), mida nimetatakse *fee sniping'iks*, mille on kirjutanud David Harding:


> Tasude kärpimine on probleem, mis võib tekkida, kui Bitcoin toetus jätkab vähenemist ja tehingutasud hakkavad domineerima Bitcoin plokkide preemiates. Kui tehingutasud on kõik, mis loeb, siis Miner, kellel on `x` protsenti Hash määrast, on `x` protsenti tõenäosus Mining järgmises plokis, seega on nende Mempool ausalt Mining oodatav väärtus `x` protsenti [parimast feerate tehingute kogumist](https://bitcoinops.org/en/newsletters/2021/06/02/#candidate-set-based-csb-block-template-construction).
>

> Teise võimalusena võib Miner ebaausalt üritada uuesti kaevandada eelmist plokki pluss täiesti uut plokki, et laiendada ahelat. Sellist käitumist nimetatakse tasuliseks snipinguks ja ebaausa Miner tõenäosus, et see õnnestub, kui kõik teised Miner on ausad, on `(x/(1-x))^2`. Ehkki tasu snipingil on üldiselt väiksem tõenäosus õnnestumiseks kui ausal Mining-l, võib ebaausa Mining proovimine olla kasumlikum valik, kui eelmises plokis tehtud tehingud maksavad oluliselt kõrgemat tasu kui praegu Mempool-s olevad tehingud - väike võimalus suure summa puhul võib olla rohkem väärt kui suur võimalus väikese summa puhul.

Meie tulevikulootuste üle viskab märja teki asjaolu, et kui kaevurid hakkavad tegema tasulist snaipimist, siis stimuleerib see teisi tegema sama, jättes veelgi vähem ausaid kaevureid. See võib Bitcoin üldist turvalisust tõsiselt kahjustada. Harding loetleb veel mõned vastumeetmed, mida saab võtta, näiteks tehingu ajalukkudele tuginedes piirata, kus Blockchainis võib tehing ilmuda.


Seega, arvestades, et konsensus lõpliku Supply suhtes püsib, jõuab plokksubsiidium - tänu [BIP42](https://github.com/Bitcoin/bips/blob/master/bip-0042.mediawiki), mis parandas väga pikaajalise inflatsioonivea - nullile umbes aastal 2140. Kas tehingutasudest piisab seejärel võrgu kindlustamiseks?


Seda on võimatu öelda, kuid me teame mõningaid asju:


- Bitcoin seisukohast on sajand *pikk* aeg. Kui see on ikka veel olemas, siis on see tõenäoliselt tohutult arenenud.
- Kui ülekaalukas majanduslik enamus peab vajalikuks muuta reegleid ja kehtestada näiteks igavene iga-aastane 0,1% või 1%-line rahaline inflatsioon, ei ole Supply Bitcoin enam piiratud.
- Kui plokkide toetus on null ja Mempool on tühi või peaaegu tühi, võib asi muutuda tasude kärpimise tõttu ebakindlaks.


Kuna üleminek ainult tasu eest makstavale Block reward-le on nii kaugel tulevikus, oleks ehk mõistlik mitte teha ennatlikke järeldusi ja püüda võimalikke probleeme lahendada, kuni me veel saame. Näiteks Peter Todd arvab, et on olemas tegelik oht, et Bitcoin turvalisuse eelarve ei ole tulevikus piisav, ja sellest tulenevalt pooldab ta Bitcoin väikest igikestvat inflatsiooni. Samas arvab ta ka, et praegu ei ole hea mõte sellist küsimust arutada, nagu [ta ütles What Bitcoin Did podcastis](https://www.whatbitcoindid.com/podcast/peter-todd-on-the-essence-of-Bitcoin):


> Kuid see on risk, mis jääb 10, 20 aasta kaugusele. See on väga pikk aeg. Ja kes kurat teab siis, millised on riskid?

Võib-olla võiksime mõelda Bitcoin-st kui millestki orgaanilisest. Kujutage ette väikest, aeglaselt kasvavat tammetaime. Kujutage ette ka seda, et te pole kunagi elus näinud täisväärtuslikku puud. Kas siis ei oleks mõistlik piirata oma kontrolliprobleeme, selle asemel et seada ette kõik reeglid, kuidas see taim peaks arenema ja kasvama?


### Järeldus lõpliku Supply kohta



Kas Bitcoin Supply kasvab üle 21 miljoni, ei oska me täna öelda, ja see pole ilmselt nii hullu. Julgeolekueelarve piisava taseme tagamine on ülioluline, kuid mitte hädavajalik. Arutleme selle üle 10-50 aasta pärast, kui teame rohkem. Kui see on ikka veel asjakohane.


# Bitcoin Gouvernance

<partId>411bf53f-af4b-50f1-b71b-e40fe3ff64b7</partId>


## Uuendamine

<chapterId>3ffa84d1-adfa-5fbc-9b13-384ea783fcdd</chapterId>



![](assets/upgrading-banner.webp)


Bitcoin turvaline ajakohastamine võib olla äärmiselt keeruline. Mõne muudatuse sisseviimiseks kulub mitu aastat. Selles peatükis tutvume Bitcoin uuendamisega seotud üldise sõnavaraga ning uurime mõningaid näiteid selle protokolli ajaloolistest uuendustest ja nendest saadud arusaamadest. Lõpuks räägime ahelate jagunemisest ning nendega seotud riskidest ja kuludest.


Selleks, et häälestada end sellele peatükile, peaksite lugema [David Hardingi teose harmoonia ja ebakõla kohta](https://bitcointalk.org/dec/p1.html):


> Bitcoin eksperdid räägivad sageli konsensusest, mille tähendus on abstraktne ja Hard täpselt määratletav. Kuid sõna konsensus arenes välja ladinakeelsest sõnast concentus, "koos laulmine harmoonias", nii et räägime mitte Bitcoin konsensusest, vaid Bitcoin harmooniast.
>

> Harmoonia on see, mis muudab Bitcoin töötavaks. Tuhanded täielikud sõlmed töötavad igaüks iseseisvalt, et kontrollida saadud tehingute kehtivust, tekitades harmoonilise kokkuleppe Bitcoin Ledger seisundi kohta, ilma et ükski sõlmeoperaator peaks kedagi teist usaldama. See sarnaneb kooriga, kus iga liige laulab sama laulu samal ajal, et toota midagi palju ilusamat, kui üks neist üksi suudaks.
>

> Bitcoin harmoonia tulemuseks on süsteem, kus bitcoinid on turvalised mitte ainult pisivarguste eest (tingimusel, et te hoiate oma võtmeid turvaliselt), vaid ka lõputu inflatsiooni, massilise või sihipärase konfiskeerimise või lihtsalt bürokraatliku mülga eest, mis on senine finantssüsteem.

Selles peatükis käsitletakse, kuidas Bitcoin saab ajakohastada ilma ebakõla tekitamata. Kooskõla säilitamine, st konsensuse säilitamine, on tõepoolest üks suurimaid väljakutseid Bitcoin arendamisel. Uuendamismehhanismides on palju nüansse, mida saab kõige paremini mõista, kui uurida tegelikke juhtumeid varasematest uuendustest. Seetõttu pööratakse peatükis palju tähelepanu ajaloolistele näidetele ja alustatakse mõningate kasulike sõnastike kasutuselevõtuga.


### Sõnavara



Vikipeedia kohaselt viitab [forward compatibility] (https://en.wikipedia.org/wiki/Forward_compatibility) tingimusele, mille puhul vana tarkvara suudab töödelda uuemate tarkvarade poolt loodud andmeid, ignoreerides neid osi, millest ta ei saa aru:


Standard toetab edasiühilduvust, kui varasematele versioonidele vastav toode suudab "graatsiliselt" töödelda standardi hilisematele versioonidele mõeldud sisendit, ignoreerides uusi osi, millest ta ei saa aru.


Vastupidi, [tagasiühilduvus] (https://en.wikipedia.org/wiki/Backward_compatibility) tähendab, et vana tarkvara andmed on kasutatavad uuemates tarkvarades. Muudatus on täielikult ühilduv, kui see on nii edasi- kui ka tagasiühilduv.


Bitcoin konsensusreeglitesse tehtud muudatust nimetatakse *Soft Fork*, kui see on täielikult ühilduv. See on kõige tavalisem viis Bitcoin uuendamiseks mitmel põhjusel, mida me käesolevas peatükis veel arutame. Kui Bitcoin konsensusreeglite muudatus on tagasiühilduv, kuid mitte edasiühilduv, nimetatakse seda *Hard Fork*.


Tehnilise ülevaate Soft ja Hard hargnemiste kohta leiate [Grokking Bitcoin 11. peatükist](https://rosenbaum.se/book/grokking-Bitcoin-11.html). Selles selgitatakse neid mõisteid ja süvenetakse ka uuendamismehhanismidesse. Soovitatav, kuigi mitte tingimata vajalik, on enne lugemise jätkamist sellega tutvuda.


### Ajaloolised uuendused



Bitcoin ei ole täna sama, mis oli Genesis ploki loomise ajal. Aastate jooksul on tehtud mitmeid uuendusi. Eric Lombrozo [rääkis 2018. aastal konverentsil "Breaking Bitcoin"] (https://btctranscripts.com/breaking-Bitcoin/2017/changing-consensus-rules-without-breaking-Bitcoin/) Bitcoin erinevatest uuendamismehhanismidest, tuues välja, kui palju need on aja jooksul arenenud. Ta isegi selgitas, kuidas Satoshi Nakamoto kunagi Bitcoin Hard Fork kaudu uuendas:


> Tegelikult oli Hard-Fork Bitcoin, mida Satoshi tegi, et me ei teeks seda kunagi nii - see on päris halb viis seda teha. Kui te vaatate git commit kirjeldust siin [[757f076](https://github.com/Bitcoin/Bitcoin/commit/757f0769d8360ea043f469f3a35f6ec204740446)], ütleb ta midagi reverted makefile.unix wx-config versiooni 0.3.6 kohta. Õige. See on kõik, mis seal kirjas on. Selles ei ole mingit märki, et see on üldse murranguline muudatus. Ta põhimõtteliselt peitis selle sinna sisse. Ta postitas ka [bitcointalki](https://bitcointalk.org/index.php?topic=626.msg6451#msg6451) ja ütles, et palun uuenda võimalikult kiiresti 0.3.6-le. Me parandasime rakendusviga, mille puhul on võimalik, et võltsitud tehinguid võidakse kuvada aktsepteerituna. Ärge võtke Bitcoin makseid vastu, kuni te ei ole uuendanud versiooni 0.3.6. Kui te ei saa kohe uuendada, siis oleks parim, kui te oma Bitcoin sõlme enne seda sulgeksite. Ja siis peale selle, ma ei tea, miks ta otsustas ka seda teha, otsustas ta lisada mõned optimeerimised samas koodis. Fikseerib vea ja lisab mõned optimeerimised.

Ta juhib tähelepanu sellele, et kas tahtlikult või mitte, see Hard Fork lõi võimalused tulevaste Soft hargnemiste jaoks, nimelt skriptioperaatorite (opkoodide) OP_NOP1-OP_NOP10 jaoks. Me uurime seda koodimuudatust lähemalt dokumendis cve-2010-5141. Neid opkoode on seni kasutatud kahes Soft hargnemisel:


- [BIP65](https://github.com/Bitcoin/bips/blob/master/bip-0065.mediawiki) (OP_CHECKLOCKTIMEVERIFY)
- [BIP113](https://github.com/Bitcoin/bips/blob/master/bip-0112.mediawiki) (OP_SEQUENCEVERIFY).


Lombrozo annab ka ülevaate sellest, kuidas uuendamismehhanismid on aastate jooksul kuni 2017. aastani arenenud. Sellest ajast alates on kasutusele võetud ainult üks teine suurem uuendamine, Taproot. Pikk ja mõnevõrra kaootiline protsess, mis viis selle aktiveerimiseni, on aidanud meil saada täiendavaid teadmisi Bitcoin uuendamismehhanismide kohta.


#### SegWit uuendamine



Kui kõik SegWit-le eelnenud uuendused olid olnud enam-vähem valutult, siis see oli teistsugune. Kui SegWit aktiveerimiskood avaldati 2016. aasta oktoobris, tundus, et Bitcoin kasutajate seas oli selle jaoks ülekaalukas toetus, kuid mingil põhjusel ei andnud kaevurid selle uuenduse toetusest märku, mis pidurdas aktiveerimist ilma lahendust nägemata.


Aaron van Wirdum kirjeldab seda käänulist teed oma Bitcoin Magazine'i artiklis [The Long Road To SegWit] (https://bitcoinmagazine.com/technical/the-long-road-to-SegWit-how-bitcoins-biggest-protocol-upgrade-became-reality). Ta selgitab kõigepealt, mis on SegWit ja kuidas see haakub plokimõõtude aruteluga. Seejärel kirjeldab van Wirdum sündmuste käiku, mis viisid selle lõpliku aktiveerimiseni. Selle protsessi keskmes oli uuendamismehhanism nimega *kasutaja aktiveeritud Soft Fork* ehk lühendatult UASF, mille pakkus välja kasutaja Shaolinfry:


> Shaolinfry pakkus välja alternatiivi: kasutaja aktiveeritud Soft Fork (UASF). Hash võimsuse aktiveerimise asemel oleks kasutaja aktiveeritud Soft Fork puhul ""lipupäeva aktiveerimine", kus sõlmede jõustamine algab eelnevalt kindlaks määratud ajal tulevikus" Niikaua kui selline UASF jõustatakse majandusliku enamuse poolt, peaks see sundima enamikku kaevandajatest järgima (või aktiveerima) Soft Fork.

Muuhulgas tsiteerib ta Shaolinfry e-kirja Bitcoin-dev postiloendis. Sel korral väitis Shaolinfry [Miner aktiveeritud Soft hargnemiste vastu](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-February/013643.html), loetledes mitmeid nendega seotud probleeme:


> Esiteks, see eeldab, et Hash võimsus kinnitatakse pärast aktiveerimist.  BIP66 Soft Fork oli juhtum, kus 95% Hashrate andis valmisolekut märku, kuid tegelikkuses umbes pool ei valideerinud tegelikult uuendatud reegleid ja kaevandas kogemata kehtetu ploki peale.
>

> Teiseks on Miner signalisatsioonil loomulik veto, mis võimaldab väikesel protsendil Hashrate-st panna veto sõlme aktiveerimisele, mis võimaldab kõigil uuendada. Praeguseks on Soft hargnemised kasutanud ära suhteliselt tsentraliseeritud Mining maastikku, kus on suhteliselt vähe Mining pooli, mis ehitavad kehtivaid plokke; kui me liigume rohkem Hashrate detsentraliseerimise suunas, kannatame tõenäoliselt üha enam "uuendamise inertsuse" all, mis paneb veto enamiku uuenduste vastu.

Shaolinfry juhtis tähelepanu ka Miner signaalimise ühele levinud vääritõlgendusele: inimesed arvasid üldiselt, et see on vahend, mille abil kaevurid saavad otsustada protokolli uuendamise üle, mitte tegevus, mis aitab uuendusi koordineerida. Selle vääritimõistmise tõttu võisid kaevandajad tunda ka kohustust kuulutada avalikult oma seisukohti teatud Soft Fork kohta, nagu annaks see ettepanekule kaalu.


Lennundusohutusameti ettepanek on lühidalt öeldes "lipupäev", mil sõlmpunktid hakkavad jõustama konkreetseid uusi eeskirju. Nii ei pea kaevurid tegema kollektiivseid jõupingutusi, et uuendamist koordineerida, vaid *võivad* käivitada aktiveerimise varem kui lipupäeval, kui piisavalt palju plokke annab märku toetusest:


> Minu soovitus on saada mõlemast maailmast parim. Kuna kasutaja aktiveeritud Soft Fork vajab enne aktiveerimist suhteliselt pikka aega, saame kombineerida BIP9-ga, et anda võimalus kiiremaks Hash võimsuse koordineeritud aktiveerimiseks või aktiveerimiseks lipupäevaks, olenevalt sellest, kumb on varem.
> Mõlemal juhul saame kasutada BIP9 hoiatussüsteeme. Muudatus on suhteliselt lihtne, lisades aktiveerimise ajalise parameetri, mis muudab BIP9 oleku LOCKED_IN-iks enne BIP9 kasutuselevõtu aegumistähtaja lõppu.

See idee äratas suurt huvi, kuid ei paistnud saavutavat peaaegu ühehäälset toetust, mis tekitas muret võimaliku ahela lõhenemise pärast. Aaron van Wirdumi artikkel selgitab, kuidas see lõpuks tänu James Hilliardi koostatud [BIP91](https://github.com/Bitcoin/bips/blob/master/bip-0091.mediawiki) lahendati:


> Hilliard pakkus välja veidi keerulise, kuid nutika lahenduse, mis muudaks kõik ühilduvaks: Bitcoin Core arendusmeeskonna pakutud eraldatud tunnistajate aktiveerimine, BIP148 UASF ja New Yorgi lepingu aktiveerimismehhanism. Tema BIP91 võiks hoida Bitcoin tervena - vähemalt kogu SegWit aktiveerimise ajal.

Sellega kaasnesid mõned keerulisemad tegurid (nt nn New Yorgi kokkulepe), mida kõnealune piiripunkt pidi arvesse võtma. Soovitame teil lugeda Van Wirdumi artiklit täies mahus, et tutvuda selle loo paljude huvitavate üksikasjadega.


#### SegWit-järgne arutelu


Pärast SegWit kasutuselevõttu tekkis arutelu kasutuselevõtu mehhanismide üle. Nagu märkis Eric Lombrozo [oma ettekandes konverentsil Breaking Bitcoin](https://btctranscripts.com/breaking-Bitcoin/2017/changing-consensus-rules-without-breaking-Bitcoin/) ja Shaolinfry, ei ole Miner aktiveeritud Soft Fork ideaalne uuendamismehhanism:


> Mingil hetkel tahame tõenäoliselt lisada Bitcoin protokollile rohkem funktsioone. See on suur filosoofiline küsimus, mida me endale esitame. Kas me teeme järgmiseks UASF-i? Kuidas oleks hübriidne lähenemine? Miner, mis on iseenesest aktiveeritud, on välistatud. bip9 me ei kavatse enam kasutada.

2020. aasta jaanuaris saatis Matt Corallo [e-kirja](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2020-January/017547.html) Bitcoin-dev postiloendisse, mis käivitas arutelu Soft Fork tulevaste kasutuselevõtumehhanismide üle. Ta loetles viis eesmärki, mida ta pidas uuenduse puhul oluliseks. David Harding [võtab need Bitcoin Optechi uudiskirjas](https://bitcoinops.org/en/newsletters/2020/01/15/#discussion-of-Soft-Fork-activation-mechanisms) kokku järgmiselt:


> Võimalus katkestada, kui on tõsiseid vastuväiteid kavandatud konsensusreeglite muudatuste kohta . Piisava aja eraldamine pärast uuendatud tarkvara vabastamist, et tagada, et enamik majandussõlmi on nende reeglite jõustamiseks ajakohastatud . Ootus, et võrgu Hash määr on enne ja pärast muudatust ning ka ülemineku ajal ligikaudu sama . Võimalikult suures ulatuses vältida uute reeglite kohaselt kehtetute plokkide loomist, mis võib põhjustada valekinnitusi uuendamata sõlmedes ja SPV-klientides . Kindlustus, et kurjategijad või partisanid ei saa katkestusmehhanisme kuritarvitada, et hoida tagasi laialdaselt soovitud uuendust, mille puhul ei ole teadaolevaid probleeme

Corallo pakub välja Miner aktiveeritud Soft Fork ja kasutaja aktiveeritud Soft Fork kombinatsiooni:


> Seega, kui midagi veidi konkreetsemat, arvan, et aktiveerimismeetod, mis loob õige pretsedendi ja võtab asjakohaselt arvesse eespool nimetatud eesmärke, oleks järgmine:
>

> 1) standardne BIP 9 kasutuselevõtt üheaastase ajahorisondiga
aktiveerimine 95% Miner valmisolekuga, +

> 2) juhul, kui ühe aasta jooksul ei toimu aktiveerimist, siis kuue kuu jooksul
vaikne periood, mille jooksul saab kogukond analüüsida ja arutada

aktiveerimise puudumise põhjused ja +

> 3) juhul, kui see on mõistlik, võimaldaks lihtne käsurea/Bitcoin.conf parameeter, mida toetati alates algsest kasutuselevõtu versioonist, kasutajatel valida BIP 8 kasutuselevõtu 24-kuulise ajahorisondiga lipu päeva aktiveerimiseks (samuti uus Bitcoin Core versioon, mis lubab lipu universaalselt).
>

> See annab väga pika ajahorisondi standardsemaks aktiveerimiseks, tagades samal ajal, et punktis 5 sätestatud eesmärgid on täidetud, isegi kui nendel juhtudel tuleb ajahorisont oluliselt pikendada, et saavutada punktis 3 sätestatud eesmärgid. Bitcoin väljatöötamine ei ole võistlus. Kui me peame, siis 42 kuu ootamine tagab, et me ei loo negatiivset pretsedenti, mida me Bitcoin kasvades kahetsema hakkame.

#### Taproot uuendamine - Kiirproovimine



Kui Taproot oli 2020. aasta oktoobris kasutuselevõtuks valmis, mis tähendab, et kõik tehnilised üksikasjad selle konsensusreeglite kohta olid rakendatud ja saavutasid laialdase heakskiidu kogukonnas, hakkasid arutelud selle tegeliku kasutuselevõtu üle hoogustuma. Need arutelud olid seni olnud üsna tagasihoidlikud.


Paljud ettepanekud aktiveerimismehhanismide kohta hakkasid ringi hõljuma ja David Harding

[kokkuvõte neist Bitcoin Wikis](https://en.Bitcoin.it/wiki/Taproot_activation_proposals). Oma artiklis selgitas ta mõningaid BIP8 omadusi, mille paindlikumaks muutmiseks tehti sel ajal mõned hiljutised muudatused.


> Käesoleva dokumendi koostamise ajal on [BIP8] (https://github.com/Bitcoin/bips/blob/master/bip-0008.mediawiki) koostatud 2017. aastal saadud õppetundide põhjal. Üks märkimisväärne muudatus pärast BIP 9+148 on see, et sunniviisiline aktiveerimine põhineb nüüd ploki kõrgusel, mitte möödunud aja mediaanil; teine märkimisväärne muudatus on see, et sunniviisiline aktiveerimine on boolean-parameeter, mis valitakse Soft Fork aktiveerimisparameetrite seadmisel kas esmaseks kasutuselevõtuks või hilisemas kasutuselevõtus ajakohastamiseks.

BIP8 ilma sunniviisilise aktiveerimiseta on väga sarnane [BIP9](https://github.com/Bitcoin/bips/blob/master/bip-0009.mediawiki) versiooni bittidega koos ajaülevaate ja viivitusega, kusjuures ainus oluline erinevus on BIP8 kasutamine plokkide kõrguste puhul võrreldes BIP9 kasutamisega mediaanajalise mineviku puhul. See seade võimaldab katse ebaõnnestuda (kuid seda saab hiljem uuesti proovida).


Sundaktiveerimisega BIP8 lõpeb kohustusliku signalisatsiooniperioodiga, kus kõik selle eeskirjade kohaselt toodetud plokid peavad andma Soft Fork valmisolekust märku viisil, mis käivitab aktiveerimise sama Soft Fork varasemas kasutuselevõtus mittekohustusliku aktiveerimisega. Teisisõnu, kui sõlme versioon x avaldatakse ilma sunniviisilise aktiveerimiseta ja hiljem avaldatakse versioon y, mis sunnib kaevandajaid edukalt alustama valmisoleku signaliseerimist sama ajavahemiku jooksul, hakkavad mõlemad versioonid samal ajal jõustama uusi konsensusreegleid.


Selline paindlikkus läbivaadatud BIP8 ettepanekus võimaldab väljendada mõningaid muid ideid, mis näeksid välja, kuidas need BIP8 abil välja näeksid. See annab ühise teguri, mida saab kasutada paljude erinevate ettepanekute kategoriseerimiseks.


Sellest hetkest alates muutusid arutelud väga tuliseks, eriti selle üle, kas "lockinontimeout" peaks olema "true" (nagu kasutaja aktiveeritud Soft Fork, millele Harding viitab kui "BIP8 koos sunniviisilise aktiveerimisega") või "false" (nagu Miner aktiveeritud Soft Fork, millele Harding viitab kui "BIP8 ilma sunniviisilise aktiveerimiseta").


Loetletud ettepanekute hulgas oli üks neist pealkirjaga "Vaatame, mis juhtub". Millegipärast ei saanud see ettepanek enne seitsme kuu möödumist suurt kõlapinda.


Nende seitsme kuu jooksul jätkus arutelu ja tundus, et ei suudetud jõuda laiapõhjalise konsensuseni selles osas, millist kasutuselevõtumehhanismi kasutada. Oli peamiselt kaks leeri: üks eelistas `lockinontimeout=true` (UASF-i rahvas) ja teine eelistas `lockinontimeout=false` ("proovi ja kui see ei õnnestu, siis mõtle uuesti" rahvas). Kuna ühelegi neist variantidest ei olnud ülekaalukat toetust, kulges arutelu ringiratast, ilma et oleks olnud võimalik edasi liikuda. Mõned neist aruteludest toimusid IRCis, kanalil nimega ##Taproot-activation, kuid [5. märtsil 2021](https://gnusha.org/Taproot-activation/2021-03-05.log) muutus midagi:


```
06:42 < harding> roconnor: is somebody proposing BIP8(3m, false)?  I mentioned that the other day but I didn't see any responses.
[...]
06:43 < willcl_ark_> Amusingly, I was just thinking to myself that, vs this, the SegWit activation was actually pretty straightforward: simply a LOT=false and if it fails a UASF.
06:43 < maybehuman> it's funny, "let's see what happens" (i.e. false, 3m) was a poular choice right at the beginning of this channel iirc
06:44 < roconnor> harding: I think I am.  I don't know how much that is worth.  Mostly I think it would be a widely acceptable configuration based on my understanding of everyone's concerns.
06:44 < willcl_ark_> maybehuman: becuase everybody actually wants this, even miners reckoned they could upgrade in about two weeks (or at least f2pool said that)
06:44 < roconnor> harding: BIP8(3m,false) with an extended lockin-period.
06:45 < harding> roconnor: oh, good.  It's been my favorite option since I first summarized the options on the wiki like seven months ago.
06:45 <@michaelfolkson> UASF wouldn't release (true,3m) but yeah Core could release (false, 3m)
06:45 < willcl_ark_> harding: It certainly seems like a good approach to me. _if_ that fails, then you can try an understand why, without wasting too much time
```


"Vaatame, mis juhtub" lähenemine näis lõpuks inimeste mõtetes klappivat. Hiljem nimetati seda protsessi selle lühikese märgistusperioodi tõttu "Speedy Trial" (kiirmenetlus). David Harding selgitab seda ideed laiemale üldsusele ühes

[e-kiri Bitcoin-dev postiloendis](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2021-March/018583.html):

> Selle ettepaneku varasem versioon dokumenteeriti üle 200 päeva tagasi ja Taproot aluseks olev kood liideti Bitcoin Core'ile üle 140 päeva tagasi.Kui me oleksime alustanud Speedy Trial'i ajal, kui Taproot liideti (mis on veidi ebareaalne), oleksime Taproot valmimisest vähem kui kaks kuud eemal või oleksime üle kuu aja tagasi liikunud järgmise aktiveerimiskatse juurde.
>

> Selle asemel oleme pikalt arutanud ja ei tundu olevat lähemal sellele, mida ma pean üldiselt vastuvõetavaks lahenduseks, kui siis, kui meililistis hakati üle aasta tagasi arutama SegWit-järgseid aktiveerimisskeeme Ma arvan, et Speedy Trial on viis generate kiireks arenguks, mis kas lõpetab arutelu (esialgu, kui aktiveerimine on edukas) või annab meile tegelikke andmeid, millele tugineda tulevaste Taproot aktiveerimisettepanekute tegemisel.

Seda kasutuselevõtumehhanismi täiustati kahe kuu jooksul ja seejärel avaldati [Bitcoin Core versioon 0.21.1](https://github.com/Bitcoin/Bitcoin/blob/master/doc/release-notes/release-notes-0.21.1.md#Taproot-Soft-Fork). Kaevurid hakkasid selle uuenduse jaoks kiiresti märku andma, viies kasutuselevõtu oleku `LOCKED_IN` ja pärast ajapikendust aktiveeriti Taproot reeglid 2021. aasta novembri keskel plokis [709632](https://Mempool.space/block/0000000000000000000687bca986194dc2c1f949318629b44bb54ec0a94d8244).


#### Tulevased kasutuselevõtumehhanismid


Arvestades hiljutiste Soft, SegWit ja Taproot harude probleeme, ei ole selge, kuidas järgmine uuendus kasutusele võetakse. Speedy Trial'i kasutati Taproot kasutuselevõtmiseks, kuid seda kasutati selleks, et ületada lõhe UASF-i ja MASF-i rahvahulkade vahel, mitte sellepärast, et see on kujunenud parimaks teadaolevaks kasutuselevõtumehhanismiks.


### Riskid


Mis tahes Fork aktiveerimise ajal, olgu see Hard või Soft, Miner aktiveeritud või kasutaja aktiveeritud, on oht, et ahel lõheneb pikaks ajaks. Rohkem kui paar plokki kestev lõhenemine võib põhjustada tõsist kahju Bitcoin ümbritsevale tundele ja ka selle hinnale. Kuid eelkõige tekitaks see suurt segadust selle üle, mis on Bitcoin. Kas Bitcoin on see kett või see kett?


Kasutaja aktiveeritud Soft Fork puhul on oht, et uued reeglid aktiveeritakse isegi siis, kui enamik Hash võimsusest neid ei toeta. Selle stsenaariumi tulemuseks oleks pikaajaline ahela lõhenemine, mis kestaks seni, kuni enamik Hash võimust võtab uued reeglid kasutusele. Eriti Hard võiks olla stiimuliks kaevuritele, et nad läheksid uuele ahelale üle, kui nad olid juba kaevandanud plokke pärast jagunemist vanas ahelas, sest haru vahetamisega loobuksid nad oma plokipreemiast. Siiski väärib märkimist üks tähelepanuväärne episood: 2013. aasta märtsis toimus pikaajaline jagunemine, mis toimus tahtmatu Hard Fork tõttu ja vastupidiselt sellele stiimulile võtsid kaks suurt Mining pooli vastu otsuse loobuda oma haru jagunemisest, et taastada konsensus.


Teisest küljest tuleneb Miner aktiveeritud Soft Fork risk sellest, et kaevurid võivad tegeleda valesignaliseerimisega, mis tähendab, et tegelik Hash võimsuse osa, mis toetab muutust, võib olla väiksem, kui see paistab. Kui tegelik toetus ei moodusta enamust Hash võimsusest, näeme tõenäoliselt eelmises lõigus kirjeldatud ahelate jagunemist sarnaselt. See või vähemalt sarnane probleem on tegelikkuses juhtunud, kui BIP66 kasutusele võeti, kuid see lahenes umbes 6 ploki jooksul.


#### Jagamise kulud



Jimmy Song [rääkis Hard kahvlitega seotud kuludest](https://btctranscripts.com/breaking-Bitcoin/2017/socialized-costs-of-Hard-forks/) Bitcoin murdmisel Pariisis, kuid suur osa sellest, mida ta ütles, kehtib ka Soft Fork ebaõnnestumise tõttu tekkinud kettilõhe kohta. Ta rääkis *negatiivsetest välismõjudest* ja määratles neid kui hinda, mida keegi teine peab maksma teie enda tegevuse eest:


> Klassikaline näide negatiivse välismõju kohta on tehas. Võib-olla toodavad nad - võib-olla on see naftatöötlemistehas ja nad toodavad kaupa, mis on majandusele kasulik, kuid nad toodavad ka midagi, mis on negatiivne välismõju, näiteks saastet. See ei ole lihtsalt midagi, mille eest kõik peavad maksma, mida tuleb puhastada või mille all kannatavad. Aga see on ka 2. ja 3. järgu mõju, nagu suurem liiklus, mis läheb tehase poole, kuna sinna peab minema rohkem töölisi. Sa võid ka- sa võid ohustada mõningaid metsloomi seal ümbruses. See ei tähenda, et kõik peavad maksma negatiivsete välismõjude eest, vaid see võib olla konkreetsed inimesed, näiteks inimesed, kes varem kasutasid seda teed või loomad, kes olid selle tehase lähedal, ja ka nemad maksavad selle tehase kulude eest.

Bitcoin kontekstis toob ta näite negatiivsetest välismõjudest, kasutades Bitcoin Cash (bcash), mis on Hard Fork Bitcoin, mis loodi vahetult enne kõnealust konverentsi 2017. aastal. Ta liigitab Hard Fork negatiivsed välismõjud ühekordseteks kuludeks ja püsivateks kuludeks.


Paljude ühekordsete kulude näidete hulgas mainib ta vahetuste puhul tekkivaid kulusid:


> Nii et meil on hulk vahetusi ja neil oli palju ühekordseid kulusid, mida nad pidid maksma. Esimene asi, mis juhtus, oli see, et nende vahetuste puhul tuli hoiused ja väljamaksed peatada üheks või kaheks päevaks, sest nad ei teadnud, mis juhtub. Paljud neist börsidest pidid kasutama Cold ladusid, sest nende kasutajad nõudsid bcash'i. See on osa nende fidicuiary kohustusest, nad peavad seda tegema. Samuti tuleb uut tarkvara auditeerida. See on midagi, mida me pidime itbitis tegema. Me tahame kulutada bcash- kuidas me seda teeme? Me peame alla laadima elektronraha? Kas see on pahavara? Me peame minema ja seda auditeerima. Meil oli umbes 10 päeva aega, et aru saada, kas see on okei või mitte. Ja siis tuleb otsustada, kas me lubame lihtsalt ühekordset väljamakset või võtame selle uue mündi nimekirja? Exchange lis ta uue mündi, see ei ole lihtne- seal on kõikvõimalikud uued protseduurid Cold säilitamiseks, allkirjastamiseks, hoiustamiseks, väljavõtmiseks. Või siis võiks olla lihtsalt see ühekordne sündmus, kus te annate neile nende bcash mingil hetkel ja siis te ei mõtle enam kunagi selle peale. Aga ka sellega on omad probleemid. Ja lõpuks, ja ükskõik, kuidas te seda ka ei teeks, väljavõtete või loetellu panete - te vajate uut infrastruktuuri, et selle token-ga kuidagi töötada, isegi kui see on ühekordne väljavõtmine. Teil on vaja mingit viisi, kuidas anda neid märke oma kasutajatele. Jällegi, lühikese etteteatamisega. Õige? Pole aega seda teha, tuleb teha kiiresti.

Ta loetleb ka kaupmeeste, makseprotsessorite, rahakottide, kaevurite ja kasutajate ühekordsed kulud, samuti mõned püsivad kulud, näiteks privaatsuse kaotamine ja suurem risk reorgide tekkeks.


Tõepoolest, kui toimub jagunemine ja kõige üldisemate reeglitega kett muutub tugevamaks kui rangemate reeglitega kett, toimub reorganiseerimine. Sellel on tõsine mõju kõikidele tehingutele, mis tehakse väljajäetud harus. Nendel põhjustel on tõesti oluline püüda alati vältida ahelate jagunemist.


### Järeldus uuendamise kohta


Bitcoin kasvab ja areneb aja jooksul. Aastate jooksul on kasutatud erinevaid uuendamismehhanisme ja õppimiskõver on järsk. Pidevalt leiutatakse üha keerukamaid ja jõulisemaid meetodeid, sest me saame üha rohkem teada, kuidas võrk reageerib.


Bitcoin harmoonias hoidmiseks on Soft hargnemiskohad osutunud sobivaks lahenduseks, kuid suur küsimus ei ole ikka veel täielikult vastatud: kuidas me Soft hargnemiskohti ohutult kasutusele võtame, ilma et see tekitaks ebakõla?


## Vastandlik mõtlemine

<chapterId>d4982f3d-4694-51cc-99be-28f54b03a2a2</chapterId>


![](assets/adversarialthinking-banner.webp)


Selles peatükis käsitletakse *vastanduslikku mõtlemist*, mõtteviisi, mis keskendub sellele, mis võib valesti minna ja kuidas vastased võivad tegutseda. Alustame Bitcoin turvalisuse eelduste ja turvamudeli arutamisega, misjärel selgitame, kuidas tavakasutajad saavad oma enesevalitsust ja Bitcoin Full node detsentraliseerimist parandada, mõeldes vastandlikult. Seejärel vaatleme mõningaid tegelikke ohte Bitcoin-le ja ka vastase mõttemaailma. Lõpuks räägime *vastupanemise aksoomist*, mis võib aidata teil mõista, miks inimesed üldse Bitcoin kallal töötavad.


Erinevate süsteemide turvalisuse üle arutledes on oluline mõista, millised on turvalisuse eeldused. Bitcoin tüüpiliseks turbeülesandeks on "diskreetse logaritmi probleem on Hard lahendatav", mis lihtsustatult öeldes tähendab, et on praktiliselt võimatu leida konkreetsele avalikule võtmele vastavat privaatvõtit. Teine üsna tugev turvaeeldus on see, et enamik võrgu hashpowerist on aus, mis tähendab, et nad mängivad reeglite järgi. Kui need eeldused osutuvad valeks, siis on Bitcoin hädas.


2015. aastal pidas Andrew Poelstra [ettekande](https://btctranscripts.com/scalingbitcoin/hong-kong-2015/security-assumptions/) Hongkongis toimunud konverentsil Scaling Bitcoin, mille käigus ta analüüsis Bitcoin turvalisuse eeldusi. Ta alustab sellest, et paljud süsteemid jätavad vastased mingil määral tähelepanuta; näiteks on tõesti Hard kaitsta hoonet igasuguste vastaste vastu. Selle asemel aktsepteeritakse üldiselt võimalust, et keegi võib hoone maha põletada, ja mingil määral ennetatakse seda ja muid vastase käitumist õiguskaitse jne. abil.


Vt greg maxwelli analoogia hoone kohta:


![](https://youtu.be/Gs9lJTRZCDc?t=2799)


Kuid internetis on asjad teisiti:


> Internetis meil seda aga ei ole. Meil on pseudonüümne ja anonüümne käitumine, igaüks võib igaühega ühendust võtta ja süsteemile haiget teha. Kui on võimalik süsteemile vasturääkivalt haiget teha, siis nad teevad seda. Me ei saa eeldada, et nad on nähtavad ja et nad tabatakse.

Selle tulemusena tuleb kõik Bitcoin teadaolevad nõrkused kuidagi kõrvaldada, vastasel juhul kasutatakse neid ära. Bitcoin on ju maailma suurim meepott.


Poelstra mainib veel, et Bitcoin on uut tüüpi süsteem; see on udusem kui näiteks allkirjastamisprotokoll, millel on väga selged turvaprognoosid.


Tarkvarainsener Jameson Lopp [süveneb sellesse] oma isiklikus blogis (https://blog.lopp.net/bitcoins-security-model-a-deep-dive/):


> Tegelikkuses ehitati ja ehitatakse Bitcoin protokolli ilma ametlikult määratletud spetsifikatsiooni või turvamudelita. Parim, mida me saame teha, on uurida stiimuleid ja osalejate käitumist süsteemis, et seda paremini mõista ja püüda kirjeldada.

Seega on meil süsteem, mis näib praktikas toimivat, kuid mille turvalisust me ei saa ametlikult tõestada. Tõestamine ei ole tõenäoliselt võimalik, kuna

süsteemi enda keerukus.


### Mitte ainult Bitcoin ekspertidele



Vastupidise mõtlemise tähtsus laieneb mingil määral ka Bitcoin igapäevastele kasutajatele, mitte ainult Bitcoin hardcorearendajatele ja ekspertidele. Ragnar Lifthasir mainib [tweetstormis](https://bitcoinwords.github.io/tweetstorm-on-adversarial-thinking), kuidas lihtsustatud narratiivid Bitcoin ümber - näiteks "lihtsalt HODL" - võivad Bitcoin enda jaoks olla alandavad, ja lõpetab sõnadega, et


> Bitcoin ja meie endi tugevdamiseks peame mõtlema nagu tarkvara insenerid, kes aitavad Bitcoin-le kaasa. Nad teevad vastastikust eksperdihinnangut, otsides halastamatult vigu. Nende tehnikaüritustel räägivad nad igast võimalusest, kuidas ettepanek võib ebaõnnestuda. Nad mõtlevad vastandlikult. Nad on konservatiivsed

Ta nimetab neid lihtsustatud narratiive monomaaniaid. Selle määratluse kaudu ütleb ta, et keskendudes ühele asjale - näiteks "lihtsalt HODL" - riskite jätta tähelepanuta vaieldamatult tähtsamad asjad, nagu näiteks oma Bitcoin turvalisuse hoidmine või Bitcoin parimal võimalikul viisil kasutamine Trustless viisil.


### Ohud



Bitcoin-s on palju teadaolevaid nõrkusi ja paljusid neist kasutatakse aktiivselt ära. Sellest ülevaate saamiseks vaadake Bitcoin wiki lehekülge [Weaknesses page](https://en.Bitcoin.it/wiki/Weaknesses). Seal on mainitud mitmesuguseid probleeme, näiteks

Wallet vargused ja teenusetõrjerünnakud:


> Kui ründaja üritab täita võrku enda kontrolli all olevate klientidega, siis on väga tõenäoline, et ühendute ainult ründaja sõlmedega. Kuigi Bitcoin ei kasuta kunagi sõlmede loendust millegi jaoks, võib sõlme täielik isoleerimine ausast võrgust olla kasulik teiste rünnakute teostamisel.

Seda tüüpi rünnakut nimetatakse *Sybil-rünnakuks* ja see toimub alati, kui üks üksus kontrollib võrgus mitut sõlme ja kasutab neid selleks, et esineda mitme üksusena.


Nagu tsitaadis ka mainitakse, ei ole Sybil-rünnak Bitcoin võrgus tõhus, sest hääletamine ei toimu sõlmede või muude arvuliste üksuste kaudu, vaid pigem arvutusvõimsuse kaudu. Sellele vaatamata jätab selline lame struktuur süsteemi vastuvõtlikuks teistele rünnakutele. Bitcoin wiki leheküljel kirjeldatakse ka teisi võimalikke rünnakuid, näiteks teabe varjamist (mida sageli nimetatakse *eklipsi rünnakuks*), ja seda, kuidas Bitcoin Core rakendab mõningaid heuristilisi vastumeetmeid selliste rünnakute vastu.


Ülaltoodud on näited reaalsetest ohtudest, mille eest tuleb hoolitseda.


### Lihtne sabotaaživäli


![](assets/sabotage-manual.webp)


Väljavõte lihtsast sabotaažikäsiraamatust


Vastase mõtteviisi paremaks mõistmiseks võib olla kasulik saada aimu sellest, kuidas nad tegutsevad. USA valitsuse asutus nimega Office of Strategic Services, mis tegutses II maailmasõja ajal ja mille üks eesmärke oli spionaaž, sabotaaž ja propaganda levitamine, koostas oma töötajatele [käsiraamatu](https://www.gutenberg.org/ebooks/26184) selle kohta, kuidas vastast õigesti saboteerida. Selle pealkiri oli "Simple Sabotage Field Manual" ja see sisaldas konkreetseid näpunäiteid vaenlase infiltreerimiseks, et muuta nende elu Hard. Nipid ulatuvad laopõletamisest kuni harjutuste kulumise põhjustamiseni, et vähendada vaenlase

tõhusus.


Näiteks on olemas lõik selle kohta, kuidas infiltraator võib organisatsioone häirida. Ei ole Hard näha, kuidas sellist taktikat saaks kasutada Bitcoin arendusprotsessi vastu, milles igaüks võib osaleda. Pühendunud ründaja võib pidevalt takistada edasiminekut ebaoluliste küsimuste lõputute probleemidega, tinkida täpsete sõnastuste üle ja püüda korrata arutelusid, mida on juba põhjalikult käsitletud. Ründaja võib palgata ka trolliarmee, et mitmekordistada oma tõhusust; võime seda nimetada sotsiaalseks Sybil-rünnakuks. Kasutades sotsiaalset Sybil-rünnakut, saavad nad jätta mulje, et kavandatava muudatuse vastu on rohkem vastupanu, kui tegelikult on.


See toob esile, kuidas sihikindel riik suudab ja teeb kõik endast oleneva, et hävitada vaenlane, sealhulgas lõhkuda teda seestpoolt. Kuna Bitcoin on rahavorm, mis konkureerib väljakujunenud fiat-valuutadega, on tõenäoline, et riigid peavad Bitcoin vaenlaseks.


### Vastupidavuse aksionoom


Eric Voskuil [kirjutab oma krüptoökonoomika wiki leheküljel](https://github.com/libbitcoin/libbitcoin-system/wiki/Axiom-of-Resistance) sellest, mida ta nimetab "vastupanu aksioomiks":


> Teisisõnu, eeldatakse, et süsteemil on võimalik riigikontrollile vastu seista. Seda ei aktsepteerita faktina, vaid seda peetakse mõistlikuks eelduseks, mis tuleneb sarnaste süsteemide käitumise empiirilisest uurimisest, mille alusel süsteemi aluseks võtta.
>

> See, kes ei aktsepteeri vastupanu aksioomi, mõtleb hoopis teistsuguse süsteemi peale kui Bitcoin. Kui eeldada, et süsteem ei ole võimalik, et ta peab vastu riigikontrollile, ei ole Bitcoin kontekstis järeldustel mõtet - nii nagu sfäärilise geomeetria järeldused on vastuolus eukleidilise geomeetriaga. Kuidas saab Bitcoin olla ilma aksioomita loata või tsensuurikindel? Vastuolu viib selleni, et tehakse ilmseid vigu, kui püütakse seda vastuolu ratsionaliseerida.


Ta ütleb sisuliselt, et ainult siis, kui eeldatakse, et on võimalik luua süsteem, mida riigid ei saa kontrollida, on mõttekas seda proovida.


See tähendab, et Bitcoin kallal töötamiseks peaksite leppima vastupanu aksioomiga, vastasel juhul peaksite oma aega kulutama teistele projektidele. Selle aksioomi tunnistamine aitab teil keskenduda oma arendusetegevuses tegelikele probleemidele: riigi tasandi vastaste ümber kodeerimine. Teisisõnu, mõelge vastandlikult.


### Järeldus vastandliku mõtlemise kohta



Detsentraliseeritud süsteemis ei saa olla vastutust väljaspool süsteemi ennast, seega peab Bitcoin ennetama pahatahtlikku käitumist rangemalt kui traditsioonilised süsteemid. Vastupidi mõtlemine on sellises süsteemis hädavajalik.


Bitcoin kaitsmiseks peate tundma selle vaenlasi ja nende stiimuleid. Enamik ohtudest näib olevat rahvusriigid, kellel on maksustamise ja rahaprintimise kaudu tohutu majanduslik võim. Tõenäoliselt ei loobu nad oma rahaprintimise privileegidest nii kergesti.


## Avatud lähtekood

<chapterId>427a160c-f893-5b2c-afba-7b24e71ba899</chapterId>



![](assets/opensource-banner.webp)


Bitcoin on ehitatud avatud lähtekoodiga tarkvara kasutades. Selles peatükis analüüsime, mida see tähendab, kuidas tarkvara hooldamine toimib ja kuidas avatud lähtekoodiga tarkvara Bitcoin võimaldab loata arendamist. Sukeldume *valikukrüptograafiasse*, mis käsitleb raamatukogude valikut ja kasutamist krüptograafilistes süsteemides. Peatükk sisaldab jaotist Bitcoin läbivaatamisprotsessi kohta, millele järgneb veel üks peatükk Bitcoin arendajate rahastamise viisidest. Viimases peatükis räägitakse sellest, kuidas Bitcoin avatud lähtekoodiga kultuur võib väljastpoolt vaadates tunduda tõesti kummaline ja miks see tajutav kummalisus on tegelikult hea tervise märk.


Enamik Bitcoin tarkvarasid, eriti Bitcoin Core, on avatud lähtekoodiga. See tähendab, et tarkvara lähtekood on tehtud üldsusele kättesaadavaks uurimiseks, parandamiseks, muutmiseks ja levitamiseks. Avatud lähtekoodi määratlus aadressil [](https://opensource.org/osd) sisaldab muu hulgas järgmisi olulisi punkte:


> Vaba ümberjaotamine: Litsents ei piira ühegi osapoole õigust müüa või kinkida tarkvara mitme eri allika programme sisaldava tarkvarakogumiku komponendina. Litsents ei nõua sellise müügi eest litsentsitasu või muud tasu.
>

> Allikakood: Programm peab sisaldama lähtekoodi ja seda peab olema võimalik levitada nii lähtekoodis kui ka kompileeritud kujul. Kui toodet ei levitata mingil kujul koos lähtekoodiga, peab olema hästi avalikustatud võimalus saada lähtekoodi mitte rohkem kui mõistliku reprodutseerimiskulu eest, eelistatavalt tasuta allalaadimine Interneti kaudu. Lähtekood peab olema eelistatud kujul, milles programmeerija muudaks programmi. Teadlikult varjatud lähtekood ei ole lubatud. Vahepealsed vormid, näiteks preprotsessori või translaatori väljund, ei ole lubatud.
>

> Tuletatud teosed: Litsents peab lubama muudatusi ja tuletatud teoseid ning neid peab lubama levitada samadel tingimustel kui algse tarkvara litsentsi alusel.

Bitcoin Core järgib seda määratlust, kuna seda levitatakse [MIT License](https://github.com/Bitcoin/Bitcoin/blob/master/COPYING) alusel:


```
The MIT License (MIT)

Copyright (c) 2009-2022 The Bitcoin Core developers
Copyright (c) 2009-2022 Bitcoin Developers

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
```


Nagu peatükis "Ära usalda, vaid kontrolli" märgitud, on oluline, et kasutajad saaksid kontrollida, et nende kasutatav Bitcoin tarkvara "töötab nii, nagu seda reklaamitakse". Selleks peab neil olema piiramatu juurdepääs selle tarkvara lähtekoodile, mida nad kontrollida soovivad.


Järgnevates osades käsitleme Bitcoin-s veel mõningaid huvitavaid avatud lähtekoodiga tarkvara aspekte.


### Tarkvara hooldus



Bitcoin Core'i lähtekoodi hoitakse Git-repositooriumis, mis asub [GitHub](https://github.com/Bitcoin/Bitcoin). Igaüks saab kloonida just seda repositooriumi ilma luba küsimata ja seejärel seda kohapeal kontrollida, ehitada või muuta. See tähendab, et selle repositooriumi koopiaid on üle kogu maailma laiali tuhandeid. Need kõik on ühe ja sama repositooriumi koopiad, nii et mis teeb selle konkreetse GitHubi Bitcoin Core repositooriumi nii eriliseks? Tehniliselt ei ole see üldse eriline, kuid sotsiaalselt on sellest saanud Bitcoin arendamise keskpunkt.


Bitcoin ja turvalisuse ekspert Jameson Lopp selgitab seda väga hästi [blogipostituses](https://blog.lopp.net/who-controls-Bitcoin-core-/) pealkirjaga "Who Controls Bitcoin Core?":


> Bitcoin Core on pigem Bitcoin protokolli arendamise keskpunkt kui juhtimis- ja kontrollpunkt. Kui see lakkaks mingil põhjusel eksisteerimast, tekiks uus fookuspunkt - tehniline kommunikatsiooniplatvorm, millel see põhineb (praegu GitHubi repositoorium), on pigem mugavuse kui määratluse/projekti terviklikkuse küsimus. Tegelikult oleme juba näinud, et Bitcoin arenduse fookuspunkt muudab platvormi ja isegi nime!

Ta selgitab, kuidas Bitcoin Core'i tarkvara on hooldatud ja kaitstud pahatahtlike koodimuudatuste eest. Selle täieliku artikli üldised järeldused on kokkuvõtlikult esitatud selle lõpus:


> Keegi ei kontrolli Bitcoin.
>

> Keegi ei kontrolli Bitcoin arendamise fookust.

Bitcoin Core'i arendaja Eric Lombrozo räägib arendusprotsessist lähemalt oma [Mediumi postituses](https://medium.com/@elombrozo/the-Bitcoin-core-merge-process-74687a09d81d) pealkirjaga "The Bitcoin Core Merge Process":


> Igaüks saab Fork koodibaasi repositooriumi ja teha suvalisi muudatusi oma repositooriumis. Nad võivad ehitada kliendi oma repositooriumist ja käivitada selle asemel, kui nad soovivad. Samuti võivad nad teha binaarkomplekte, mida teised inimesed saavad käivitada.
>

> Kui keegi soovib oma repositooriumis tehtud muudatust ühendada Bitcoin Core'i, võib ta esitada pull request. Kui taotlus on esitatud, saab igaüks vaadata muudatusi ja neid kommenteerida, olenemata sellest, kas tal on juurdepääs Bitcoin Core'ile või mitte.

Tuleb märkida, et tõmbetaotlused võivad võtta väga kaua aega, enne kui hooldajad neid repositooriumi ühendavad, ja see on tavaliselt tingitud läbivaatamise puudumisest, mis on sageli tingitud *retsensentide* puudumisest.


Lombrozo räägib ka konsensuse muutmise protsessist, kuid see jääb veidi väljapoole selle peatüki ulatust. Vt eelnevat peatükki "Uuendamine", kus on rohkem teavet Bitcoin protokolli uuendamise kohta.


### Lubadeta arendus



Oleme kehtestanud, et igaüks võib Bitcoin Core'ile koodi kirjutada ilma luba küsimata, kuid ei pruugi seda Git-i peamise repositooriumi lisada. See mõjutab kõiki muudatusi, alates graafilise kasutaja Interface värviskeemide muutmisest kuni võrdõiguslikkuse sõnumite vormistamise viisini ja isegi konsensusreegliteni, st reeglite kogumini, mis määratlevad kehtiva Blockchain.


Tõenäoliselt on sama oluline, et kasutajad võivad Bitcoin peal vabalt arendada süsteeme, ilma et nad peaksid selleks luba küsima. Me oleme näinud lugematul hulgal edukaid tarkvaraprojekte, mis on ehitatud Bitcoin peal, näiteks:



- Lightning Network: Maksevõrk, mis võimaldab väga väikeste summade kiiret maksmist. See nõuab väga vähe On-Chain Bitcoin tehinguid. On olemas mitmesuguseid koostalitlusvõimelisi rakendusi, näiteks [Core Lightning] (https://github.com/ElementsProject/lightning), [LND] (https://github.com/lightningnetwork/LND), [Eclair] (https://github.com/ACINQ/eclair) ja [Lightning Dev Kit] (https://github.com/lightningdevkit).
- CoinJoin: Mitu osapoolt teevad koostööd, et ühendada oma maksed üheks tehinguks, et Address klastrite moodustamine oleks raskem. On olemas erinevaid rakendusi.
- Külgahelad: See süsteem võib lukustada mündi Bitcoin Blockchain-s, et avada see mõnes teises Blockchain-s. See võimaldab bitimünte viia mõnele teisele Blockchain-le, nimelt Sidechain-le, et kasutada selle Sidechain funktsioone. Näiteks [Blockstream'i Elements](https://github.com/ElementsProject/Elements).
- OpenTimestamps: See võimaldab teil [Timestamp dokumenti](https://opentimestamps.org/) Bitcoin Blockchain privaatselt kasutada. Seejärel saate selle Timestamp abil tõestada, et dokument peab olema eksisteerinud enne teatavat aega.


Ilma loata arenguta ei oleks paljud neist projektidest olnud võimalikud. Nagu neutraalsust käsitlevas peatükis öeldud, kui arendajad peaksid Bitcoin peal protokollide loomiseks luba küsima, arendataks ainult neid protokolle, mida keskne arendajaid lubav komitee lubab.


On tavaline, et sellised süsteemid nagu eespool loetletud on ise avatud lähtekoodiga tarkvarana litsentseeritud, mis omakorda võimaldab inimestel anda oma panuse, taaskasutada või vaadata nende koodi läbi ilma luba küsimata. Avatud lähtekoodist on saanud Bitcoin tarkvaralitsentside kuldstandard.


### Pseudonüümne areng



See, et Bitcoin tarkvara arendamiseks ei pea luba küsima, toob kaasa huvitava ja olulise võimaluse: te võite kirjutada ja avaldada koodi Bitcoin Core'is või mõnes muus avatud lähtekoodiga projektis, ilma et teie identiteeti avalikustataks.


Paljud arendajad valivad selle võimaluse, tegutsedes pseudonüümi all ja püüdes seda oma tegelikust identiteedist lahus hoida. Põhjused, miks nad seda teevad, võivad arendajatel erineda. Üks pseudonüümne kasutaja on ZmnSCPxj. Muude projektide hulgas aitab ta kaasa Bitcoin Core'ile ja Core Lightning'ile, mis on üks mitmest Lightning Network rakendusest. [Ta kirjutab](https://zmnscpxj.github.io/about.html) oma veebilehel:


> Ma olen ZmnSCPxj, juhuslikult genereeritud Interneti inimene. Minu pronoomenid on ta/see/see.
>

> Ma mõistan, et inimesed soovivad instinktiivselt teada minu identiteeti. Kuid ma arvan, et minu identiteet on suuresti ebaoluline, ja ma eelistan, et mind hinnatakse minu töö järgi.
>

> Kui te mõtlete, kas annetada või mitte, ja mõtlete, milline on minu elukallidus või sissetulek, siis palun mõistke, et õigesti rääkides peaksite mulle annetama lähtuvalt kasulikkusest, mida te leiate mu
artiklid ja minu töö Bitcoin ja Lightning Network kohta.


Tema puhul tuleb pseudonüümi kasutamise põhjuseid hinnata tema teenete põhjal, mitte selle põhjal, kes on või kes on pseudonüümi taga olev isik või isikud. Huvitaval kombel avaldas ta [artiklis CoinDeskis](https://www.coindesk.com/markets/2020/06/29/many-Bitcoin-developers-are-choosing-to-use-pseudonyms-for-good-reason/), et pseudonüüm loodi hoopis teisel põhjusel.


> Minu esialgne põhjus [pseudonüümi kasutamiseks] oli lihtsalt see, et ma olin mures [massiivse vea tegemise pärast]; seega oli ZmnSCPxj algselt mõeldud ühekordselt kasutatavaks pseudonüümiks, millest saaks sellisel juhul loobuda. Siiski tundub, et see on kogunud enamasti positiivset mainet, nii et ma olen selle säilitanud

Pseudonüümi kasutamine võimaldab teil tõepoolest vabamalt rääkida, ilma et seaksite oma isikliku maine ohtu, kui peaksite ütlema midagi rumalat või tegema mõne suure vea. Nagu selgus, sai tema pseudonüüm väga mainekaks ja 2019. aastal [sai ta isegi arendustoetuse](https://twitter.com/spiralbtc/status/1204815615678177280), mis on iseenesest tunnistus Bitcoin loata olemusest.


Vaieldamatult on Bitcoin kõige tuntum pseudonüüm Satoshi Nakamoto. On ebaselge, miks ta valis pseudonüümi, kuid tagantjärele vaadates oli see tõenäoliselt hea otsus mitmel põhjusel:


- Kuna paljud inimesed spekuleerivad, et Nakamoto omab palju Bitcoin, on tema rahalise ja isikliku turvalisuse huvides hädavajalik, et tema identiteet jääks teadmata.
- Kuna tema identiteet on teadmata, ei ole võimalik kedagi vastutusele võtta, mis annab erinevatele valitsusasutustele Hard aega.
- Puudub autoriteetne isik, kelle poole võiks üles vaadata, mis muudab Bitcoin meritokraatlikumaks ja vastupidavamaks väljapressimise vastu.


Pange tähele, et need punktid ei kehti mitte ainult Satoshi Nakamoto kohta, vaid igaühe kohta, kes töötab Bitcoin-s või omab märkimisväärseid koguseid seda valuutat, erineval määral.


### Valikukrüptograafia


Avatud lähtekoodiga arendajad kasutavad sageli teiste inimeste väljatöötatud avatud lähtekoodiga raamatukogusid. See on iga terve ökosüsteemi loomulik ja suurepärane osa. Kuid Bitcoin tarkvara tegeleb reaalse rahaga ja seda silmas pidades peavad arendajad olema eriti ettevaatlikud, kui nad valivad, millistest kolmandate osapoolte raamatukogudest nad peaksid sõltuma.


Filosoofilises [kõnes krüptograafiast](https://btctranscripts.com/greg-maxwell/2015-04-29-gmaxwell-Bitcoin-selection-cryptography/) soovib Gregory Maxwell uuesti defineerida mõistet "krüptograafia", mis on tema arvates liiga kitsas. Ta selgitab, et põhimõtteliselt *teave tahab olla vaba*, ja teeb oma krüptograafia definitsiooni sellest lähtuvalt:


> Krüptograafia on kunst ja teadus, mida me kasutame selleks, et võidelda teabe põhiolemuse vastu, painutada seda meie poliitilise ja moraalse tahte järgi ning suunata seda inimlikele eesmärkidele vastu igasuguse juhuse ja selle vastu suunatud jõupingutuste vastu.

Seejärel tutvustab ta terminit *valikukrüptograafia*, mida nimetatakse krüptograafiliste vahendite valimise kunstiks, ja selgitab, miks see on krüptograafia oluline osa. See keerleb selle ümber, kuidas valida krüptograafilisi raamatukogusid, vahendeid ja tavasid, või nagu ta ütleb "krüptosüsteemide valimise krüptosüsteem".


Konkreetsete näidete abil näitab ta, kuidas valikukrüptograafia võib kergesti kohutavalt valesti minna, ning pakub välja ka nimekirja küsimustest, mida võiksite endale selle harjutamisel esitada. Allpool on esitatud selle loetelu destilleeritud versioon:


- Kas tarkvara on mõeldud teie jaoks?
- Kas krüptograafilisi kaalutlusi võetakse tõsiselt?
- Milline on läbivaatamisprotsess? Kas on olemas?
- Millised on autorite kogemused?
- Kas tarkvara on dokumenteeritud?
- Kas tarkvara on kaasaskantav?
- Kas tarkvara on testitud?
- Kas tarkvara võtab kasutusele parimad tavad?


Kuigi see ei ole lõplik juhend edu saavutamiseks, võib nende punktide läbimine valikukrüptograafia tegemisel olla väga kasulik.


Maxwelli poolt eespool nimetatud probleemide tõttu püüab Bitcoin Core tõesti Hard [minimeerida oma kokkupuudet kolmandate osapoolte raamatukogudega](https://github.com/Bitcoin/Bitcoin/blob/master/doc/dependencies.md). Loomulikult ei saa kõiki väliseid sõltuvusi likvideerida, sest muidu peaks kõike ise kirjutama, alates fontide renderdamisest kuni süsteemikutsete rakendamiseni.


### Ülevaade



See osa kannab nime "Review", mitte "Code review", sest Bitcoin turvalisus tugineb suuresti mitmetasandilisele läbivaatamisele, mitte ainult lähtekoodile. Peale selle nõuavad erinevad ideed läbivaatamist erinevatel tasanditel: konsensusreeglite muutmine nõuaks põhjalikumat läbivaatamist mitmel tasandil võrreldes värviskeemi muutmise või trükivigade parandamisega.


Teel lõpliku vastuvõtmiseni läbib idee tavaliselt mitu arutelu- ja läbivaatamisetappi. Mõned neist etappidest on loetletud allpool:



- Idee on postitatud Bitcoin-dev postiloendis
- Idee on vormistatud Bitcoin parendusettepanekuks (BIP)
- BIP on rakendatud tõmbetaotluses (PR) Bitcoin Core'ile
- Arutatakse kasutuselevõtumehhanisme
- Mõned konkureerivad kasutuselevõtumehhanismid on rakendatud Bitcoin Core'ile esitatud tõmbetaotlustes
- Pull-päringud liidetakse master-harusse
- Kasutajad otsustavad, kas nad kasutavad tarkvara või mitte


Igas nimetatud etapis vaatavad erinevate seisukohtade ja taustaga inimesed läbi olemasoleva teabe, olgu see siis lähtekood, piiritletud lähteülesanne või lihtsalt vabalt kirjeldatud idee. Tavaliselt ei toimu need faasid rangelt ülalt-alla, tõepoolest võib mitu faasi toimuda samaaegselt ja mõnikord liigutakse nende vahel edasi-tagasi. Erinevate etappide ajal võivad tagasisidet anda ka erinevad inimesed.


Üks kõige viljakamaid koodi ülevaatajaid Bitcoin Core'is on Jon Atack. Ta kirjutas [blogipostituse](https://jonatack.github.io/articles/how-to-review-pull-requests-in-Bitcoin-core) selle kohta, kuidas vaadata läbi tõmbepäringuid Bitcoin Core'is. Ta rõhutab, et hea koodi ülevaataja keskendub sellele, kuidas kõige paremini väärtust lisada.


> Uustulnukana on eesmärk püüda sõbralikult ja tagasihoidlikult lisaväärtust luua, õppides samal ajal võimalikult palju.
>

> Hea lähenemine on teha see mitte sinust, vaid pigem "Kuidas saan ma kõige paremini teenida?"

Ta rõhutab asjaolu, et läbivaatamine on Bitcoin Core'i puhul tõeliselt piirav tegur. Paljud head ideed jäävad seisma, kus ei toimu läbivaatamist, ootele. Märkab, et läbivaatamine ei ole mitte ainult kasulik Bitcoin-le, vaid ka suurepärane võimalus õppida tarkvara kohta, andes samal ajal sellele väärtust. Atacki rusikareegel on vaadata läbi 5-15 PR-i, enne kui teete ise PR-i. Jällegi, teie tähelepanu peaks olema suunatud sellele, kuidas kõige paremini kogukonda teenida, mitte sellele, kuidas teie enda koodi ühendada. Lisaks sellele rõhutab ta, kui oluline on teha ülevaatamist õigel tasemel: kas see on aeg nippe ja kirjavigade jaoks või vajab arendaja rohkem kontseptuaalselt orienteeritud ülevaatamist? Jon Attack lisab:


> Kasulik esimene küsimus läbivaatamise alguses võib olla: "Mida on siin praegu kõige rohkem vaja?" Sellele küsimusele vastamine nõuab kogemusi ja kogunenud konteksti, kuid see on kasulik küsimus, et otsustada, kuidas saaksite kõige vähem aja jooksul kõige rohkem väärtust lisada.

Postituse teine pool koosneb mõnest kasulikust praktilisest tehnilisest juhendist selle kohta, kuidas tegelikult läbivaatamist teha, ning sisaldab linke olulisele dokumentatsioonile, mille abil saab edasi lugeda.


Bitcoin Core arendaja ja koodi ülevaataja Gloria Zhao on kirjutanud [artikli](https://github.com/glozow/Bitcoin-notes/blob/master/review-checklist.md), mis sisaldab küsimusi, mida ta tavaliselt ülevaatamise ajal endale esitab. Samuti märgib ta, mida ta peab heaks ülevaatuseks:


> Ma isiklikult arvan, et hea arvustus on selline, kus ma olen esitanud endale palju teravaid küsimusi PR-i kohta ja olnud vastustega rahul
neile. [...] Loomulikult alustan ma kontseptuaalsetest küsimustest, seejärel lähenemisviisiga seotud küsimustest ja seejärel rakendamisega seotud küsimustest. Üldiselt arvan ma isiklikult, et on mõttetu jätta C++ süntaksiga seotud kommentaare PR-i eelnõule, ja oleks ebaviisakas pöörduda tagasi "kas see on mõistlik" pärast seda, kui autor on käsitlenud 20+ minu koodi korraldamise ettepanekut.


Tema mõte, et hea ülevaade peaks keskenduma sellele, mida on konkreetsel ajahetkel kõige rohkem vaja, ühtib hästi Jon Atacki nõuannetega. Ta

pakub välja loetelu küsimustest, mida võite esitada endale läbivaatamisprotsessi eri tasanditel, kuid rõhutab, et see loetelu ei ole mingil juhul ammendav ega otsene retsept. Loetelu on illustreeritud GitHubi tegelike näidetega.


### Rahastamine



Paljud inimesed töötavad Bitcoin avatud lähtekoodiga, kas Bitcoin Core'i või muude projektide jaoks. Paljud teevad seda vabal ajal, saamata mingit hüvitist, kuid mõned arendajad saavad selle eest ka tasu.


Ettevõtted, üksikisikud ja organisatsioonid, kes on huvitatud Bitcoin jätkuvast edust, võivad annetada raha arendajatele kas otse või organisatsioonide kaudu, kes omakorda jagavad raha üksikutele arendajatele. On ka mitmeid Bitcoin-le keskendunud ettevõtteid, mis palkavad kvalifitseeritud arendajaid, et nad saaksid Bitcoin-ga täistööajaga töötada.


### Kultuurišokk



Inimestele jääb mõnikord mulje, et Bitcoin arendajate seas on palju sisevõitlusi ja lõputuid tuliseid arutelusid ning et nad on võimetud otsuseid tegema.


Näiteks Taproot kasutuselevõtumehhanismi üle arutati pikka aega, mille jooksul moodustusid kaks "laagrit". Üks tahtis "ebaõnnestuda" uuenduse puhul, kui kaevurid ei olnud pärast teatud hetke ülekaalukalt uute reeglite poolt hääletanud, samas kui teine tahtis reegleid pärast seda hetke igatahes jõustada. Michael Folkson võtab kahe leeri argumendid kokku [email](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2021-February/018380.html) postiloendis Bitcoin-dev.


Arutelu kestis näiliselt igavesti ja see oli tõesti Hard, et näha, et selles küsimuses kujuneb üksmeel lähiajal. See tekitas inimestes pettumust ja selle tulemusena süvenes kuumus. Gregory Maxwell (kasutajana nullc) muretses [Redditis](https://www.reddit.com/r/Bitcoin/comments/hrlpnc/technical_taproot_why_activate/fyqbn8s/?utm_source=share&utm_medium=web2x&context=3), et pikad arutelud muudavad uuenduse vähem turvaliseks:


> Praegusel hetkel ei lisa täiendav ootamine rohkem ülevaatamist ja kindlustunnet. Selle asemel vähendab täiendav viivitus inertsust ja suurendab potentsiaalselt mõnevõrra riski, kuna inimesed hakkavad unustama üksikasju, lükkavad edasi tööd järgnevate kasutusviiside (nagu Wallet tugi) ja ei investeeri nii palju täiendavat läbivaatamist, kui nad investeeriksid, kui nad oleksid kindlad aktiveerimise ajakava suhtes.

Lõpuks sai see vaidlus lahendatud tänu David Hardingi ja Russel O'Connori uuele ettepanekule nimega Speedy Trial, mis tähendas kaevurite jaoks suhteliselt lühemat signalisatsiooniperioodi, et lukustada Taproot aktiveerimine või ebaõnnestuda kiiresti. Kui nad aktiveeriksid selle ajaakna jooksul, siis Taproot võetaks kasutusele umbes 6 kuud hiljem.


Keegi, kes ei ole harjunud Bitcoin arendusprotsessiga, arvab ilmselt, et need tulised arutelud näevad kohutavalt halvad ja isegi mürgised välja. Mõne inimese silmis on vähemalt kaks tegurit, mis panevad need halvasti välja nägema:



- Võrreldes suletud lähtekoodiga ettevõtetega toimuvad kõik arutelud avalikult, toimetamata. Selline tarkvarafirma nagu Google ei laseks oma töötajatel kunagi avalikult arutleda kavandatud funktsioonide üle, vaid avaldaks kõige rohkem avalduse ettevõtte seisukoha kohta selles küsimuses. See muudab ettevõtted Bitcoin-ga võrreldes harmoonilisemaks.
- Kuna Bitcoin on lubadeta, võib igaüks oma arvamust avaldada. See erineb põhimõtteliselt suletud lähtekoodiga ettevõttest, kus on käputäis inimesi, kellel on oma arvamus, tavaliselt mõttekaaslased. Bitcoin-s väljendatud arvamuste rohkus on lihtsalt hämmastav võrreldes näiteks PayPaliga.


Enamik Bitcoin arendajaid väidavad, et selline avatus loob hea ja tervisliku keskkonna ning et see on isegi vajalik parima tulemuse saavutamiseks.


Nagu peatükis Threat vihjati, võib teine ülaltoodud punkt olla väga kasulik, kuid sellega kaasneb ka negatiivne külg. Ründaja võib kasutada viivitustaktikat, nagu on kirjeldatud [Simple Sabotage Field Manual] (https://www.gutenberg.org/ebooks/26184), et moonutada otsustus- ja arendusprotsessi.


Veel üks asi, mida tasub mainida, on see, et kuna Bitcoin on raha ja Bitcoin Core kindlustab mõõtmatuid rahasummasid, ei võeta turvalisust selles kontekstis kergekäeliselt. Seepärast on kogenud Bitcoin Core

arendajad võivad tunduda väga Hard-peaga, mis suhtumine on tavaliselt õigustatud. Tõepoolest, funktsioon, mille taga on nõrk põhjendus, ei ole vastuvõetav. Sama juhtuks, kui see rikuks

reprodutseeritavad buildid, lisati uusi sõltuvusi või kui kood ei järginud Bitcoin [parimaid tavasid](https://github.com/Bitcoin/Bitcoin/blob/master/doc/developer-notes.md).


See võib uusi (ja vanu) arendajaid frustreerida. Kuid nagu avatud lähtekoodiga tarkvaras tavaks, võite alati Fork repositooriumi, ühendada mis iganes soovite oma Fork, ning ehitada ja käivitada oma binaarsüsteemi.


### Kokkuvõte avatud lähtekoodist


Bitcoin Core ja enamik muudest Bitcoin tarkvaradest on avatud lähtekoodiga, mis tähendab, et igaüks võib tarkvara levitada, muuta ja kasutada nii, nagu talle meeldib. Bitcoin Core'i repositoorium GitHubis on praegu Bitcoin arendamise keskpunkt, kuid see staatus võib muutuda, kui inimesed hakkavad selle hooldajatele või veebisaidile endale umbusaldama.


Avatud lähtekood võimaldab Bitcoin-s ja selle peal lubadeta arendamist. Kas te kirjutate koodi, vaatate koodi või protokollid üle; avatud lähtekood võimaldab teil seda teha, pseudonoomselt või mitte.


Bitcoin ümber toimuv arendusprotsess on radikaalselt avatud, mis võib muuta Bitcoin mürgiseks ja ebatõhusaks, kuid just see hoiab Bitcoin vastupidavana pahatahtlike osalejate vastu.


## Skaala

<chapterId>bb3f3924-202c-5cdd-b2e9-e0c1cab0e48e</chapterId>



![](assets/scaling-banner.webp)



Selles peatükis uurime, kuidas Bitcoin skaleerub ja kuidas mitte. Alustame sellest, kuidas inimesed on minevikus skaalumise kohta arutanud. Seejärel selgitab suurem osa sellest peatükist erinevaid lähenemisi Bitcoin skaleerimisele, täpsemalt vertikaalset, horisontaalset, sisemist ja kihilist skaleerimist. Igale kirjeldusele järgnevad kaalutlused selle kohta, kas see lähenemisviis häirib Bitcoin väärtuspakkumist.


Bitcoin ruumis omistavad erinevad inimesed sõnale "skaala" erinevaid määratlusi. Mõned mõistavad seda kui Blockchain tehinguvõimsuse suurendamist, teised usuvad, et see tähendab Blockchain tõhusamat kasutamist, ja kolmandad näevad seda kui süsteemide arendamist Bitcoin peal.


Bitcoin kontekstis ja käesoleva raamatu eesmärkidel defineerime skaleerimist kui * Bitcoin kasutusvõimsuse suurendamist ilma tsensuurikindluse vähenemiseta*. See määratlus hõlmab mitmeid

näiteks mitmesugused muudatused:


- Tehingu sisendite kasutamine vähemate baitidega
- Allkirjade kontrollimise tulemuslikkuse parandamine
- Võrdlusvõrgustiku kasutamine väiksema ribalaiusega
- Tehingute pakkimine
- Kihiline arhitektuur


Peagi sukeldume erinevatesse lähenemistesse skaleerimisele, kuid alustame lühikese ülevaatega Bitcoin ajaloost skaleerimise kontekstis.


### Skaalamise ajalugu



Skaalamine on olnud arutelude keskmes alates Genesis Bitcoin-st. Kõige esimene lause [kõige esimeses e-kirjas](https://www.metzdowd.com/pipermail/cryptography/2008-November/014814.html) vastuseks Satoshi teadustöödele Bitcoin kohta krüptograafia meililistis oli tõepoolest skaalumise kohta:


> Satoshi Nakamoto kirjutas:
>

> "Olen töötanud uue elektroonilise sularahasüsteemi kallal, mis on täielikult vastastikune, ilma usaldusväärse kolmanda osapooleta.  Töö on kättesaadav aadressil http://www.Bitcoin.org/Bitcoin.pdf"
>

> Me vajame sellist süsteemi väga-väga palju, kuid nii nagu ma teie ettepanekust aru saan, ei tundu see olevat vajaliku suurusega.

Vestlus iseenesest ei pruugi olla väga huvitav ega täpne, kuid see näitab, et mastaapsus on olnud algusest peale probleemiks.


Diskussioonid skaalumise üle saavutasid oma kõrgpunkti umbes aastatel 2015-2017, kui ringlesid mitmed erinevad ideed selle kohta, kas ja kuidas suurendada maksimaalset plokimahu piirangut. See oli üsna ebahuvitav arutelu ühe parameetri muutmise üle lähtekoodis, muudatus, mis ei lahendanud põhimõtteliselt midagi, kuid lükkas skaalumise probleemi veelgi kaugemale tulevikku, tekitades tehnilist võlga.


2015. aastal toimus Montrealis konverents [Scaling Bitcoin] (https://scalingbitcoin.org/), mille järelkonverents toimus kuus kuud hiljem Hongkongis ja seejärel mitmes teises kohas üle maailma. Keskenduti just sellele, kuidas Address skaleerida. Paljud Bitcoin arendajad ja teised entusiastid kogunesid nendele konverentsidele, et arutada erinevaid skaleerimisküsimusi ja -ettepanekuid. Enamik neist aruteludest ei keerelnud mitte plokkide suuruse suurendamise, vaid pikemaajaliste lahenduste ümber.


Pärast Hongkongi konverentsi 2015. aasta detsembris võttis Gregory Maxwell [oma seisukoha](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-December/011865.html) kokku paljude arutlusel olnud küsimuste kohta, alustades mõnest üldisest skaalamisfilosoofiast:


> Olemasoleva tehnoloogia puhul on olemas põhimõttelised kompromissid mastaabi ja detsentraliseerimise vahel. Kui süsteem on liiga kulukas, on inimesed sunnitud usaldama kolmandaid osapooli, selle asemel et iseseisvalt süsteemi reegleid jõustada. Kui Bitcoin Blockchain ressursikasutus võrreldes olemasoleva tehnoloogiaga on liiga suur, kaotab Bitcoin oma konkurentsieelised võrreldes vanade süsteemidega, sest valideerimine muutub liiga kulukaks (hinnates paljud kasutajad välja), mis sunnib usaldust tagasi süsteemi.  Kui võimsus on liiga väike ja meie tehingumeetodid liiga ebatõhusad, on juurdepääs ahelale vaidluste lahendamiseks liiga kulukas, mis jällegi surub usalduse tagasi süsteemi.

Ta räägib kompromissist läbilaskevõime ja detsentraliseerimise vahel. Kui lubate suuremaid plokke, siis tõrjutate mõned inimesed võrgust välja, sest neil ei ole enam ressursse plokkide valideerimiseks. Aga teisest küljest, kui juurdepääs plokiruumile muutub kallimaks, saavad vähem inimesi endale lubada selle kasutamist vaidluste lahendamise mehhanismina. Mõlemal juhul surutakse kasutajad usaldusväärsete teenuste poole.


Ta jätkab, tehes kokkuvõtte konverentsil esitatud paljudest skaalamise lähenemisviisidest. Nende hulgas on arvutuslikult tõhusamad allkirja kontrollimised, *segregeeritud tunnistaja*, sealhulgas plokisuuruse piirangu muutmine, ruumiliselt tõhusam plokkide levitamise mehhanism ja protokollide ehitamine kihtide kaupa Bitcoin peal. Paljud neist

vahepeal on rakendatud erinevaid lähenemisviise.


### Skaalalähedased lähenemisviisid



Nagu eespool vihjati, ei pea Bitcoin skaleerimine tingimata tähendama plokimahu või muude piirangute suurendamist. Käime nüüd läbi mõned üldised lähenemised skaleerimisele, millest mõned ei kannata eelmises punktis mainitud läbilaskevõime-detsentraliseerimise kompromissi.


#### Vertikaalne skaleerimine



Vertikaalne skaleerimine on protsess, mille käigus suurendatakse andmeid töötlevate masinate arvutusressursse. Bitcoin kontekstis oleksid need viimased täissõlmed, nimelt masinad, mis valideerivad Blockchain kasutajate nimel.


Bitcoin puhul on kõige sagedamini arutatud vertikaalse skaleerimise meetodiks plokimahu piirangu suurendamine. See nõuaks, et mõned täissõlmed peaksid oma riistvara ajakohastama, et pidada sammu kasvavate arvutusnõuetega. Miinuseks on see, et see toimub tsentraliseerimise arvelt.


Lisaks negatiivsetele mõjudele Full node detsentraliseerimisele võib vertikaalne skaleerimine mõjutada Bitcoin Mining detsentraliseerimist ja turvalisust ka vähem ilmselgetel viisidel. Vaatame, kuidas kaevandajad "peaksid" tegutsema. Oletame, et Miner kaevandab ploki kõrgusel 7 ja avaldab selle ploki Bitcoin võrgus. Selle ploki laialdase aktsepteerimise saavutamine võtab aega, mis tuleneb peamiselt kahest tegurist:


- Bloki edastamine võrdsete osapoolte vahel võtab aega ribalaiuse piirangute tõttu.
- Ploki valideerimine võtab aega.


Kuigi plokk 7 levib võrgus, on paljud kaevurid ikka veel Mining ploki 6 peal, sest nad ei ole veel saanud ja valideerinud plokki 7. Kui mõni neist kaevuritest leiab selle aja jooksul uue ploki kõrgusel 7, on sellel kõrgusel kaks konkureerivat plokki. Kõrgusel 7 (või mõnel muul kõrgusel) võib olla ainult üks plokk, mis tähendab, et üks kahest kandidaadist peab muutuma aegunuks.


Lühidalt öeldes, aegunud plokid tekivad, sest iga ploki levik võtab aega ja mida kauem levik kestab, seda suurem on aegunud plokkide tõenäosus.


Oletame, et plokimahu piirang tühistatakse ja et keskmine plokimaht suureneb oluliselt. Siis leviksid plokid üle võrgu aeglasemalt, kuna ribalaius on piiratud ja kontrollimiseks kulub aega. Levitamisaja suurenemine suurendab ka aegunud plokkide tekkimise tõenäosust.


Kaevuritele ei meeldi, kui nende plokid on kinni pandud, sest nad kaotavad oma Block reward, seega teevad nad kõik endast oleneva, et seda vältida

stsenaarium. Meetmed, mida nad võivad võtta, hõlmavad järgmist:



- Saabuva ploki valideerimise edasilükkamine, tuntud ka kui *valideerimata Mining*. Kaevandajad võivad lihtsalt kontrollida ploki päise Proof-of-Work ja kaevandada selle pealt, samal ajal kui nad laadivad vahepeal alla kogu ploki ja valideerivad selle.
- Suurema ribalaiuse ja ühenduvuse Mining pool-ga ühendamine.


Validatsioonita Mining õõnestab Full node detsentraliseerimist veelgi, kuna Miner kasutab vähemalt ajutiselt sissetulevate plokkide usaldamist. Samuti kahjustab see mingil määral turvalisust, sest osa võrgu arvutusvõimsusest ehitab potentsiaalselt kehtetu Blockchain peale, selle asemel et ehitada tugevaima ja kehtiva ahela peale.


Teine punkt avaldab Miner detsentraliseerimisele negatiivset mõju, sest tavaliselt on parima võrguühenduse ja ribalaiusega basseinid ka kõige suuremad, mistõttu kaevandajad koonduvad mõne suure basseini poole.


#### Horisontaalne skaleerimine



Horisontaalne skaleerimine viitab tehnikatele, mis jagavad töökoormuse mitme masina vahel. Kuigi see on levinud skaleerimismeetod populaarsete veebisaitide ja andmebaaside puhul, ei ole seda Bitcoin puhul lihtne teha.


Paljud inimesed nimetavad seda Bitcoin skaleerimismeetodit *shardinguks*. Põhimõtteliselt seisneb see selles, et iga Full node laseb kontrollida ainult osa Blockchain-st. Peter Todd on sharding'i kontseptsioonile palju mõelnud. Ta kirjutas [blogipostituse](https://petertodd.org/2015/why-scaling-Bitcoin-with-sharding-is-very-Hard), kus ta selgitab shardingi üldiselt ja tutvustab ka oma ideed nimega *treechains*. Artikkel on raske lugemine, kuid Todd toob välja mõned punktid, mis on üsna seeditavad:


> Sharded-süsteemides ei toimi "Full node kaitse", vähemalt otseselt. Kogu mõte on selles, et kõik andmed ei ole kõigil olemas, seega tuleb otsustada, mis juhtub, kui neid ei ole saadaval.

Seejärel tutvustab ta erinevaid ideid, kuidas lahendada jagamist ehk horisontaalset skaleerimist. Postituse lõpus lõpetab ta:


> Siin on aga suur probleem: püha !@#$ on ülaltoodud kompleks võrreldes Bitcoin-ga! Isegi "kiddy" versioon shardingist - minu linearisatsiooniskeem, mitte zk-SNARKS - on ilmselt ühe või kahe suurusjärgu võrra keerulisem kui Bitcoin protokolli kasutamine praegu on, kuid praegu tundub, et suur % selle valdkonna ettevõtetest on käed üles visanud ja kasutavad selle asemel tsentraliseeritud API-teenuste pakkujaid. Eespool kirjeldatu tegelik rakendamine ja selle lõppkasutajate kätte saamine ei ole lihtne.
>

> Teisest küljest ei ole detsentraliseerimine odav: PayPali kasutamine on ühe või kahe suurusjärgu võrra lihtsam kui Bitcoin protokoll.

Tema järeldus on, et jagamine *võiks* olla tehniliselt võimalik, kuid see tuleks tohutu keerukuse hinnaga. Arvestades, et paljud kasutajad peavad Bitcoin juba praegu liiga keeruliseks ja eelistavad selle asemel kasutada tsentraliseeritud teenuseid, siis on Hard veenda neid kasutama midagi veelgi keerulisemat.


#### Sisemine skaalumine



Kuigi horisontaalne ja vertikaalne skaleerimine on tsentraliseeritud süsteemides, nagu andmebaasid ja veebiserverid, ajalooliselt hästi toiminud, ei tundu need tsentraliseeriva mõju tõttu sobivat detsentraliseeritud võrku nagu Bitcoin.


Lähenemisviis, mida hinnatakse liiga vähe, on see, mida võime nimetada *sisese skaleerimisega*, mis tähendab "tee vähemaga rohkem". See viitab paljude arendajate pidevale tööle, mille eesmärk on optimeerida juba olemasolevaid algoritme, et me saaksime süsteemi olemasolevate piiride piires teha rohkem.


Sisemõõtkava abil saavutatud edusammud on pehmelt öeldes muljetavaldavad. Et anda teile üldine ettekujutus aastate jooksul toimunud parandustest, on Jameson Lopp [teinud Blockchain sünkroniseerimise võrdlusteste](https://blog.lopp.net/Bitcoin-core-performance-evolution/), milles ta võrdleb mitmeid erinevaid Bitcoin Core'i versioone alates versioonist 0.8.


![](assets/Bitcoin-Core-Sync-Performance-1.webp)


Bitcoin Core'i erinevate versioonide esialgne plokkide allalaadimise jõudlus. Y-teljel on sünkroniseeritud ploki kõrgus ja X-teljel aeg, mis kulus sünkroniseerimiseks sellele kõrgusele


Erinevad read tähistavad Bitcoin Core'i erinevaid versioone. Kõige vasakpoolsem rida on viimane, st versioon 0.22, mis ilmus septembris 2021 ja mille täielikuks sünkroniseerimiseks kulus 396 minutit. Kõige parempoolsem on versioon 0.8 novembrist 2013, mis võttis 3452 minutit. Kogu see - umbes 10-kordne - paranemine on tingitud sissepoole skaleerimisest.


Parandused võib liigitada kas ruumi (RAM, kettas, ribalaius jne) või arvutusvõimsuse säästmiseks. Mõlemad kategooriad aitavad kaasa eespool esitatud diagrammi parandustele.


Hea näide arvutusliku täiustamise kohta on [libsecp256k1](https://github.com/Bitcoin-core/secp256k1) raamatukogu, mis muu hulgas rakendab digitaalallkirjade tegemiseks ja kontrollimiseks vajalikke krüptograafilisi algtõdesid. Pieter Wuille on üks selle raamatukogu toetajatest ja ta kirjutas [Twitteri teema](https://twitter.com/pwuille/status/1450471673321381896), kus ta tutvustab erinevate pull-päringute abil saavutatud jõudluse paranemist.


![](assets/libsecp256k1speedups.webp)


Allkirjade kontrollimise tulemuslikkus aja jooksul, ajajoonele on märgitud olulised tõmbepäringud


Graafik näitab suundumust kahe erineva 64-bitise protsessoritüübi, nimelt ARM ja x86 puhul. Erinevus jõudluses tuleneb x86-arhitektuuri rohkematest spetsialiseeritud käskudest võrreldes ARM-arhitektuuriga, millel on vähem ja rohkem üldisi käske. Üldine suundumus on aga mõlema arhitektuuri puhul sama. Pange tähele, et Y-telg on logaritmiline, mis muudab paranemise vähem muljetavaldavaks, kui see tegelikult on.


On ka mitmeid häid näiteid ruumi kokkuhoiu paranduste kohta, mis aitasid kaasa jõudluse suurendamisele. Ühes

[Medium blogipostitus](https://murchandamus.medium.com/2-of-3-Multisig-inputs-using-Pay-to-Taproot-d5faf2312ba3) Taproot panuse kohta ruumi säästmisse, kasutaja Murch võrdleb, kui palju plokkide ruumi 2-of-3 künnise allkiri vajaks, kasutades Taproot erinevatel viisidel, samuti seda üldse mitte kasutades.


![](assets/murch-taproot.webp)


Ruumi kokkuhoid erinevate kulutustüüpide, Taproot ja vanade versioonide puhul.


2-ast-3 Multisig, mis kasutab originaalset SegWit, vajaks kokku 104,5+43 vB = 147,5 vB, samas kui Taproot kõige ruumisäästlikum kasutamine nõuaks standardkasutuse korral ainult 57,5+43 vB = 100,5 vB. Halvemal juhul ja harvaesinevatel juhtudel, näiteks kui standardallkirjastaja ei ole mingil põhjusel kättesaadav, kasutaks Taproot 107,5+43 vB = 150,5 vB. Te ei pea kõigist üksikasjadest aru saama, kuid see peaks andma teile ettekujutuse sellest, kuidas arendajad mõtlevad ruumi kokkuhoiust - iga väike bait loeb.


Lisaks Bitcoin tarkvara sisemisele skaleerimisele on ka mõned viisid, kuidas kasutajad saavad sisemisele skaleerimisele kaasa aidata. Nad saavad teha oma tehinguid arukamalt, et säästa tehingutasusid, vähendades samal ajal oma jalajälge Full node nõuetele. Kahte tavaliselt kasutatavat meetodit sellise eesmärgi saavutamiseks nimetatakse tehingute pakkimiseks ja väljundi konsolideerimiseks.


Tehingute pakkimise idee on ühendada mitu makset üheks tehinguks, selle asemel, et teha üks tehing iga makse kohta. See võib säästa palju tasusid ja samal ajal vähendada plokkide ruumi koormust.


![](assets/tx-batching.webp)


Tehingute ühendamine ühendab mitu makset üheks tehinguks, et säästa tasusid.


Väljundite konsolideerimine tähendab, et kasutatakse ära perioodid, mil plokipinna nõudlus on väike, et ühendada mitu väljundit üheks väljundiks. See võib vähendada teie tasukulusid hiljem, kui teil on vaja teha makseid, kui nõudlus plokkruumi järele on suur.


![](assets/utxo-consolidation.webp)


Väljundi konsolideerimine: Sulatage oma mündid üheks suureks mündiks, kui tasud on madalad, et hiljem tasusid säästa.


Ei pruugi olla ilmne, kuidas toodangu konsolideerimine aitab kaasa sisemaisele skaalumisele. Lõppude lõpuks suureneb Blockchain andmete kogumaht selle meetodi puhul isegi veidi. Sellegipoolest kahaneb UTXO kogum, st andmebaas, milles peetakse arvestust selle üle, kellele millised mündid kuuluvad, sest te kulutate rohkem UTXOsid kui te loote. See leevendab täisnoodide koormust oma UTXO kogude säilitamisel.


Kahjuks aga võivad need kaks *UTXO haldamise* meetodit kahjustada teie enda või teie makse saajate privaatsust. Parteerimise puhul teab iga makse saaja, et kõik parteeritud väljundid on teistelt makse saajatelt (välja arvatud võimalik, et muutus). UTXO konsolideerimise korral paljastate, et teie konsolideeritud väljundid kuuluvad samale Wallet-le. Seega peate võib-olla tegema kompromissi kulutõhususe ja privaatsuse vahel.


#### Kihiline skaleerimine



Kõige mõjusam lähenemine skaleerimisele on tõenäoliselt kihiline lähenemine. Üldine idee kihistamise taga on see, et protokoll saab arveldada kasutajate vahelisi makseid ilma Blockchain-le tehinguid lisamata.


Mitmekihiline protokoll algab kahe või enama inimese kokkuleppimisega, mis pannakse Blockchain-le, nagu on näidatud allpool oleval joonisel.


![](assets/scaling-layer.webp)

Tüüpiline Layer 2 protokoll Bitcoin, Layer 1 peal.


See, kuidas see alustamistehing luuakse, on protokollides erinev, kuid ühine on see, et osalejad loovad allkirjastamata alustamistehingu ja mitu eelallkirjastatud karistustehingut, mis kulutavad alustamistehingu väljundit erinevalt. Seejärel allkirjastatakse alustamistehing täielikult ja avaldatakse Blockchain-le ning karistustehingud võivad olla täielikult allkirjastatud ja avaldatud, et karistada vääralt käituvat osapoolt. See motiveerib osalejaid oma lubadustest kinni pidama, nii et protokoll saaks töötada Trustless viisil.


Kui käivitamistehing on Blockchain-s, saab protokoll teha seda, mida ta peaks tegema. Näiteks võib see teha osalejate vahelisi ülikiireid makseid, rakendada mõningaid privaatsust suurendavaid tehnikaid või teha täiustatud skriptimist, mida Bitcoin Blockchain ei toeta.


Me ei hakka üksikasjalikult kirjeldama, kuidas konkreetsed protokollid töötavad, kuid nagu eelmisest joonisest näha, kasutatakse Blockchain protokolli elutsükli jooksul harva. Kogu mahlakas tegevus toimub *off-chain*. Me nägime, kuidas see võib olla privaatsuse võit, kui seda õigesti teha, kuid see võib olla ka eelis skaleeritavuse jaoks.


Gregory Maxwell selgitab [Redditi postituses](https://www.reddit.com/r/Bitcoin/comments/438hx0/a_trip_to_the_moon_requires_a_rocket_with/) pealkirjaga "Reis Kuule nõuab mitmeastmelist raketti või muidu sööb raketi võrrand sinu lõunasöögi... pakkimine kõik klounautode stiilis trebuchetisse ja lootmine edule on õige out.", miks kihistumine on meie parim võimalus Bitcoin skaalale jõudmiseks suurusjärkude võrra.


Ta alustab, rõhutades, et Visa või Mastercard on ekslik, kui neid peetakse Bitcoin peamisteks konkurentideks, ja rõhutab, et maksimaalse plokimahu suurendamine on halb lähenemine nimetatud konkurentsile. Seejärel räägib ta sellest, kuidas kihtide kasutamisega tõelist vahet teha:


> Kas see tähendab, et Bitcoin ei saa olla suur võitja kui maksetehnoloogia? Ei. Kuid selleks, et saavutada selline võimsus, mida on vaja maailma maksevajaduste rahuldamiseks, peame töötama arukamalt.
>

> Bitcoin oli algusest peale kavandatud nii, et see sisaldaks kihte turvaliselt oma nutika lepingute sõlmimise võime kaudu (Mis, arvate, et see oli sinna pandud ainult selleks, et inimesed saaksid mõttetutest "DAO-dest" filosofeerida?). Tegelikult kasutame Bitcoin süsteemi kui väga kättesaadavat ja täiesti usaldusväärset robotkohtunikku ning ajame enamiku oma asju väljaspool kohtusaali - kuid teeme tehinguid nii, et kui midagi läheb valesti, on meil olemas kõik tõendid ja sõlmitud kokkulepped, nii et võime olla kindlad, et robotkohtu teeb asja õigeks. (Geek sidebar: kui see tundub võimatu, minge ja lugege seda vana postitust tehingu läbilõikamisest)
>

> See on võimalik just Bitcoin põhiomaduste tõttu. Tsenseeritav või pöörduv baassüsteem ei ole väga sobiv, et selle peale ehitada võimsat ülemist Layer tehingutöötlust... ja kui alusvara ei ole terve, siis on vähe mõtet sellega üldse tehinguid teha.

Analoogia kohtunikuga on üsna näitlik, kuidas kihistumine toimib: see kohtunik peab olema korrumpeerumatu ega tohi kunagi oma meelt muuta, sest muidu ei toimi Bitcoin baasist Layer kõrgemal olevad kihid usaldusväärselt.


Ta jätkab tsentraliseeritud teenuste kohta. Tavaliselt ei ole probleemiks, kui usaldada keskserverile triviaalse koguse Bitcoin, et asjad saaksid tehtud: see on samuti kihiline skaleerimine.


Paljud aastad on möödunud sellest, kui Maxwell kirjutas ülaltoodud teose, ja tema sõnad on ikka veel õiged. Lightning Network edu tõestab, et kihistamine on tõepoolest üks võimalus Bitcoin kasulikkuse suurendamiseks.



### Järeldus skaalamise kohta



Me oleme arutanud erinevaid viise, mille abil võib soovida Bitcoin skaleerida, suurendada Bitcoin kasutusvõimsust. Skaleerimine on Bitcoin puhul olnud probleemiks juba selle algusaegadest alates.


Täna teame, et Bitcoin ei ole hästi skaleeritav vertikaalselt ("osta suuremat riistvara") ega horisontaalselt ("kontrolli ainult osa andmeid"), vaid pigem sissepoole ("tee vähemaga rohkem") ja kihiti ("ehita protokollid Bitcoin peale").


## Kui sitt tabab ventilaatorit

<chapterId>fe39c13c-310f-51fd-84ff-6b92dd01c9e7</chapterId>



![](assets/shtf-banner.webp)

Bitcoin on ehitatud inimeste poolt. Inimesed kirjutavad tarkvara ja inimesed käivitavad seda tarkvara. Kui avastatakse turvaauk või tõsine viga - kas nende kahe vahel on tõesti vahet? - avastavad seda alati inimesed, lihast ja verest. Selles peatükis mõeldakse, mida inimesed teevad, peaksid ja ei peaks tegema, kui sitt tabab ventilaatorit. Esimeses peatükis selgitatakse mõistet *vastutustundlik avalikustamine*, mis viitab sellele, kuidas keegi, kes avastab haavatavuse, saab tegutseda vastutustundlikult, et aidata vähendada sellest tulenevat kahju. Peatüki ülejäänud osa viib teid ekskursioonile mõnede aastate jooksul avastatud kõige tõsisemate haavatavuste kaudu ja selle kaudu, kuidas arendajad, kaevandajad ja kasutajad nendega toime tulid. Bitcoin varases lapsepõlves ei olnud asjad nii ranged kui tänapäeval.


### Vastutustundlik avalikustamine



Kujutage ette, et avastate Bitcoin Core'is vea, mis võimaldab kellelgi Bitcoin Core'i sõlme eemalt välja lülitada, kasutades selleks spetsiaalselt koostatud võrguteateid. Kujutage ette, et te ei ole pahatahtlik ja soovite, et see probleem jääks kasutamata. Mida teete? Kui te vaikite sellest, avastab probleemi tõenäoliselt keegi teine ja te ei saa olla kindel, et see inimene ei ole pahatahtlik.


Kui avastatakse turvaprobleem, peaks selle avastanud isik kasutama _vastutustundlikku avalikustamist_, mis on Bitcoin arendajate seas sageli kasutatav termin. See termin on [Vikipeedia](https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure):


> Riistvara ja tarkvara arendajad vajavad sageli aega ja ressursse oma vigade parandamiseks. Sageli on eetilised häkkerid need, kes leiavad need
haavatavused. Häkkerid ja arvutiturvalisuse teadlased on seisukohal, et nende sotsiaalne kohustus on teavitada avalikkust haavatavustest. Probleemide varjamine võib tekitada vale turvatunde. Selle vältimiseks kooskõlastavad ja lepivad asjaomased osapooled kokku mõistliku aja haavatavuse kõrvaldamiseks. Sõltuvalt haavatavuse võimalikust mõjust, erakorralise paranduse või lahenduse väljatöötamiseks ja rakendamiseks kuluvast eeldatavast ajast ning muudest teguritest võib see ajavahemik varieeruda mõnest päevast kuni mitme kuuni.


See tähendab, et kui leiate turvaprobleemi, peaksite sellest teatama süsteemi eest vastutavale meeskonnale. Kuid mida see tähendab Bitcoin kontekstis? Keegi ei kontrolli Bitcoin, kuid praegu on olemas Bitcoin arenduse keskpunkt, nimelt [Bitcoin Core Githubi repositoorium](https://github.com/Bitcoin/Bitcoin). Kõnealuse repositooriumi hooldajad vastutavad seal oleva koodi eest, kuid nad ei vastuta süsteemi kui terviku eest - keegi ei vastuta. Sellegipoolest on üldine parim tava saata e-kiri aadressile security@bitcoincore.org.


2017. aasta [e-posti teemas](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/015002.html) pealkirjaga "Vastutustundlik vigade avalikustamine" üritas Anthony Towns kokku võtta, mida ta pidas praeguseks parimaks tavaks. Ta oli kogunud sisendit mitmest allikast ja erinevatelt inimestelt, et anda oma seisukohale sel teemal teavet.




- Haavatavustest tuleks teatada turvalisuse kaudu aadressil bitcoincore.org
- Kriitilise probleemiga (mida saab kohe ära kasutada või mida juba kasutatakse ära, põhjustades suurt kahju) tegeletakse:
  - avaldatud plaaster ASAP
  - laiaulatuslik teavitamine uuendamise vajadusest (või mõjutatud süsteemide väljalülitamine)
  - tegeliku probleemi minimaalne avalikustamine, et lükata rünnakuid edasi
- Mittekriitilise haavatavusega (kuna seda on raske või kallis ära kasutada) tegeletakse järgmiselt:
  - tavapärase arengu käigus tehtud parandused ja ülevaatused
  - paranduse või lahenduse tagasiportimine master'ist praegusesse avaldatud versiooni
- Arendajad püüavad tagada, et paranduse avaldamine ei paljastaks haavatavuse olemust, andes pakutud paranduse kogenud arendajatele, keda ei ole teavitatud haavatavusest, teatades neile, et see parandab haavatavuse, ja paludes neil tuvastada haavatavus.
- Arendajad võivad soovitada teistele Bitcoin rakendustele haavatavuse paranduste vastuvõtmist enne paranduse avaldamist ja laialdast kasutuselevõttu, kui nad saavad seda teha ilma haavatavust avalikustamata; näiteks kui parandusel on märkimisväärne kasu jõudlusele, mis õigustab selle lisamist.
- Enne haavatavuse avalikuks muutumist soovitavad arendajad üldiselt sõbralikele Altcoin arendajatele, et nad peaksid parandustega järele jõudma. Kuid seda alles pärast seda, kui parandused on Bitcoin võrgus laialdaselt kasutusel.
- Üldiselt ei teavita Altcoin arendajaid, kes on käitunud vaenulikult (nt kasutavad haavatavusi teiste ründamiseks või rikuvad embargot).
- Bitcoin arendajad ei avalikusta haavatavuse üksikasju enne, kui >80% Bitcoin sõlmedest on parandused kasutusele võtnud. Haavatavuse avastajatel soovitatakse ja palutakse järgida sama poliitikat. [1] [6]


See nimekiri näitab, kui ettevaatlik tuleb olla Bitcoin paranduste avaldamisel, sest parandused ise võivad haavatavuse ära anda. Neljas punkt on eriti huvitav, sest seal selgitatakse, kuidas testida, kas parandus on piisavalt hästi varjatud. Tõepoolest, kui mõned tõesti kogenud arendajad ei suuda haavatavust märgata isegi teadmisega, et parandus parandab seda, siis tõenäoliselt on teistel tõesti Hard seda avastada.


Teema, mis viis selle e-kirjani, käsitles seda, kas, millal ja kuidas avalikustada haavatavusi altcoinidele ja teistele Bitcoin rakendustele. Siin ei ole selget vastust. "Heade poiste aitamine" tundub olevat mõistlik, kuid kes otsustab, kes need on ja kuhu tõmmatakse piir? Bryan Bishop [väitis](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/014983.html), et altcoinide ja isegi scamcoinide kaitsmine turvaaukude vastu on moraalne kohustus:


> Ei piisa Bitcoin ja selle kasutajate kaitsmisest aktiivsete ohtude eest, on üldisem vastutus kaitsta igasuguseid kasutajaid ja erinevat tarkvara igasuguste ohtude eest, ükskõik millises vormis, isegi kui inimesed kasutavad rumalat ja ebaturvalist tarkvara, mida te isiklikult ei halda ega toeta ega propageeri. Haavatavuse teadasaamine on delikaatne asi ja te võite saada teadasaamist, millel on tõsisemad otsesed või kaudsed tagajärjed kui algselt kirjeldatud.

Eespool toodud Towni e-kirjale eelnes ka Gregory Maxwelli [postitus](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/014977.html), milles ta väitis, et turvaaukud võivad olla tõsisemad, kui nad paistavad:


> Ma olen mitu korda näinud Hard kasutada küsimus osutub triviaalseks, kui leiate õige trikk, või väike dos küsimus omakorda meie palju tõsisemaks.
>

> Lihtsaid jõudlusvigu, mis on oskuslikult rakendatud, saab potentsiaalselt kasutada võrgu tükeldamiseks - Miner A ja Exchange B lähevad ühte partitsiooni, kõik teised teise... ja kahekordistatakse.
>

> Ja nii edasi.  Seega, kuigi ma olen täiesti nõus, et erinevaid asju tuleks ja võib käsitleda erinevalt, ei ole see alati nii selge. On mõistlik käsitleda asju tõsisemalt, kui sa tead, et nad on.

Seega, isegi kui haavatavus tundub Hard kasutatavana, võib olla parem eeldada, et see on kergesti kasutatav ja te lihtsalt ei ole veel aru saanud, kuidas seda teha.


Ta mainib ka seda, kuidas "on mõnevõrra vale nimetada seda teemat millekski avalikustamiseks, see teema ei puuduta avalikustamist. Avalikustamine on see, kui sa ütled müüjale.  See niit räägib avaldamisest ja sellel on hoopis teised tagajärjed. Avaldamine on see, kui sa oled kindel, et sa oled rääkinud potentsiaalsetele ründajatele". See viimane tähelepanek avalikustamise ja avaldamise eristamise kohta on oluline. Lihtne osa on vastutustundlik avalikustamine; Hard osa on mõistlik avaldamine.


### Bitcoin traumaatiline lapsepõlv



Bitcoin alustas ühe mehe (vähemalt sellele viitab selle looja pseudonüüm) projektina ja Bitcoin oli esialgu vähe või üldse mitte väärtuslik. Seetõttu ei tegeletud haavatavuste ja vigade parandamisega nii rangelt kui tänapäeval.


Bitcoin wikis on [nimekiri ühistest haavatavustest ja riskipunktidest](https://en.Bitcoin.it/wiki/Common_Vulnerabilities_and_Exposures) (CVE), mida Bitcoin on läbinud. See osa kujutab endast väikest ülevaadet mõnest Bitcoin algusaastate turvaprobleemist ja intsidentidest. Me ei käsitle neid kõiki, kuid valisime välja mõned, mis meie arvates on eriti huvitavad.


#### 2010-07-28: Kuluta kellegi münte (CVE-2010-5141)



28. juulil 2010 avastas pseudonüümne isik nimega ArtForz vea versioonis 0.3.4, mis võimaldas kellelgi võtta münte kelleltki teiselt. ArtForz teatas sellest *vastutavalt* Satoshi Nakamotole ja teisele Bitcoin arendajale nimega Gavin Andresen.


Probleem oli selles, et skriptioperaator `OP_RETURN` lihtsalt lõpetaks programmi täitmise, nii et kui scriptPubKey oli `<pubkey> OP_CHECKSIG` ja scriptSig oli `OP_1 OP_RETURN`, siis scriptPubKey-s olev programmiosa ei käivituks kunagi. Ainus asi, mis juhtuks, oleks `1`, mis pannakse virna ja seejärel `OP_RETURN` põhjustaks programmi väljumise. Mis tahes mittenullväärtus virna peal pärast programmi täitmist tähendab, et kulutamise tingimus on täidetud. Kuna virna ülemine element `1` ei ole null, siis on kulutamine korras.


See oli koodi "OP_RETURN" käsitlemiseks:


```
case OP_RETURN:
{
pc = pend;
}
break;
```

`pc = pend;` mõju oli see, et ülejäänud programm jäeti vahele, mis tähendab, et mis tahes lukustusskripti scriptPubKey's ignoreeriti. Parandus seisnes `OP_RETURN` tähenduse muutmises nii, et see kohe ebaõnnestus.


```
case OP_RETURN:
{
return false;
}
break;
```


Satoshi tegi selle muudatuse lokaalselt ja ehitas sellest versiooniga 0.3.5 käivitatava binaarsüsteemi. Seejärel postitas ta Bitcointalki foorumisse `\\*** ALERT \*** Upgrade to 0.3.5 ASAP`, kutsudes kasutajaid üles installima seda tema binaarversiooni, esitamata selle lähtekoodi:


> Palun uuenda 0.3.5-le niipea kui võimalik!  Me parandasime rakendusviga, mille tõttu oli võimalik, et võltsitud tehinguid võis vastu võtta.  Ärge võtke Bitcoin tehinguid maksetena vastu, kuni te ei ole uuendanud versiooni 0.3.5!

Esialgset sõnumit on hiljem muudetud ja see ei ole enam täies mahus kättesaadav. Ülaltoodud katkend on [tsiteerides vastust](https://bitcointalk.org/index.php?topic=626.msg6458#msg6458). Mõned kasutajad proovisid Satoshi binaari, kuid puutusid sellega kokku probleemidega. Varsti pärast seda kirjutas [Satoshi](https://bitcointalk.org/index.php?topic=626.msg6469#msg6469):


> Ei ole veel olnud aega SVN-i uuendada.  Oodake 0.3.6, ma ehitan seda praegu.  Sa võid vahepeal oma sõlme sulgeda.

Ja 35 minutit hiljem [kirjutas ta](https://bitcointalk.org/index.php?topic=626.msg6480#msg6480):


> SVN on uuendatud versiooniga 0.3.6.
>

> Laadin praegu Sourceforge'ile üles Windowsi versiooni 0.3.6, seejärel ehitan linuxi ümber.

Sel hetkel tundus ta ka, et ta uuendas algset postitust, et mainida 0.3.6 asemel 0.3.5:


> Palun uuenda 0.3.6-le niipea kui võimalik!  Me parandasime rakendusviga, mille tõttu oli võimalik, et võltsitud tehinguid võis näidata aktsepteerituna.  Ärge aktsepteerige Bitcoin tehinguid maksetena, kuni te ei ole uuendanud versiooni 0.3.6!
>

> Kui te ei saa kohe uuendada versiooni 0.3.6, siis on kõige parem Bitcoin sõlme enne seda sulgeda.
>

> Samuti 0.3.6, kiirem hashing:
> - midstate vahemälu optimeerimine tänu tcatmile
> - Crypto++ ASM SHA-256 tänu BlackEye'ile
> Kokku genereerimise kiirendus 2,4 korda kiirem.
>

> Allalaadimine:
>

> http://sourceforge.net/projects/Bitcoin/files/Bitcoin/Bitcoin-0.3.6/
>

> Windowsi ja Linuxi kasutajad: kui teil on 0.3.5, peate siiski uuendama versiooni 0.3.6.

Pange tähele erinevust probleemi iseloomustuses võrreldes esimese sõnumiga: "võidakse kuvada aktsepteerituna" vs "võidakse aktsepteerida". Võib-olla alandas Satoshi oma teatises vea tõsidust, et mitte tõmmata tegelikule probleemile liiga palju tähelepanu. Igatahes, inimesed uuendasid versiooni 0.3.6 ja see töötas ootuspäraselt. See konkreetne probleem lahendati, hämmastaval kombel ilma Bitcoin kaotusteta.


Satoshi sõnumis kirjeldati ka mõningaid Mining jõudluse optimeerimist. On ebaselge, miks see lisati kriitilise turvaparanduse hulka, võimalik, et eesmärk oli tegeliku probleemi varjamine. Siiski tundub tõenäolisem, et ta lihtsalt avaldas selle, mis oli Subversioni repositooriumi arendusharu peas, millele oli lisatud turvaparandus.


Sel ajal ei olnud kaugeltki nii palju kasutajaid kui praegu ja Bitcoin väärtus oli nullilähedane. Kui see viga reageerimine mängitaks tänapäeval, peetaks seda mitmel põhjusel täielikuks jama-show'ks:



- Satoshi tegi ainult binaarset versiooni 0.3.5, mis sisaldab parandust. Ühtegi parandust ega koodi ei esitatud, võib-olla probleemi varjamiseks.
- 0.3.5 [isegi ei töötanud](https://bitcointalk.org/index.php?topic=626.msg6455#msg6455).
- Parandus 0.3.6 oli tegelikult Hard Fork.


Teine vaieldav asi on see, kas on hea või halb, et kasutajatel paluti oma sõlmed sulgeda. Tänapäeval ei oleks see võimalik, kuid sel ajal jälgisid paljud kasutajad aktiivselt foorumeid uuenduste saamiseks ja olid tavaliselt asjadega kursis. Arvestades, et seda oli võimalik teha, oleks see võinud olla mõistlik.


#### 2010-08-15 Kombineeritud väljundi ülevool (CVE-2010-5139)



2010. aasta augusti keskel teatas Bitcointalki foorumi kasutaja jgarzik ehk Jeff Garzik,

[avastas, et](https://bitcointalk.org/index.php?topic=822.msg9474#msg9474) teatud tehingul ploki kõrgusel 74638 oli kaks ebatavaliselt suure väärtusega väljundit:


```
"out" : [
{
"value" : 92233720368.54277039,
"scriptPubKey" : "OP_DUP OP_HASH160 0xB7A73EB128D7EA3D388DB12418302A1CBAD5E890 OP_EQUALVERIFY OP_CHECKSIG"
},
{
"value" : 92233720368.54277039,
"scriptPubKey" : "OP_DUP OP_HASH160 0x151275508C66F89DEC2C5F43B6F9CBE0B5C4722C OP_EQUALVERIFY OP_CHECKSIG"
}
]
```


> "Väärtus välja" selles plokis #74638 on üsna kummaline:
>

> 92233720368.54277039 BTC?  Kas see on UINT64_MAX, ma ei tea?

Arvatavasti oli viga, mis põhjustas kahe int64 (mitte uint64, nagu Garzik eeldas) väljundi summa ülevoolu negatiivsesse väärtusesse -0.00997538 BTC. Sõltumata sisendite summast, oleks väljundite "summa" väiksem, mistõttu see tehing oleks tolleaegse koodi järgi OK.


Antud juhul oli viga avalikustatud ja avaldatud tegeliku vigastuse kaudu. Selle õnnetu tulemus oli see, et oli loodud umbes 2x92 miljardit Bitcoin, mis lahjendas tugevalt sel ajal eksisteerinud umbes 3,7 miljoni mündi suurust raha Supply.


Ühes sellega seotud teemas postitas [Satoshi](https://bitcointalk.org/index.php?topic=823.msg9531#msg9531), et ta oleks tänulik, kui inimesed lõpetaksid Mining (või *genereerimise*, nagu nad seda siis nimetasid):


> See aitaks, kui inimesed lõpetaksid genereerimise.  Tõenäoliselt tuleb meil praeguse haru ümber teha uus haru, ja mida vähem te generate, seda kiiremini saab see toimuda.
>

> Esimene parandus on SVN rev 132.  See ei ole veel üles laaditud.  Ma surun esmalt mõned muud misc muudatused välja, siis laadin selle plaastri üles.

Tema plaan oli teha Soft Fork, et muuta sellised tehingud nagu siin käsitletud tehingud kehtetuks, muutes seega selliseid tehinguid sisaldanud plokid (eriti plokk 74638) kehtetuks. Vähem kui tund aega hiljem tegi ta [paranduse Subversioni repositooriumi versioonis 132](https://sourceforge.net/p/Bitcoin/code/132/) ja [postitas foorumisse](https://bitcointalk.org/index.php?topic=823.msg9548#msg9548) kirjeldades, mida tema arvates peaksid kasutajad tegema:


> Parandus on üles laaditud SVN rev 132!
>

> Praeguseks soovituslikud sammud:
> 1) Sulgemine.
> 2) Laadige alla knightmb'i blk failid.  (asendage oma blk0001.dat ja blkindex.dat failid)
> 3) Uuendamine.
> 4) See peaks algama vähem kui 74000 plokiga. Laske tal ülejäänud uuesti alla laadida.
>

> Kui te ei soovi kasutada knightmb-i faile, võite lihtsalt kustutada oma blk*.dat-failid, kuid see koormab võrku väga palju, kui kõik laevad korraga alla kogu plokkide indeksit.
>

> Ma ehitan varsti väljaanded.

Ta soovis, et inimesed laadiksid alla ühe konkreetse kasutaja, nimelt knightmb, blkXXXX.dat ja blkindex.dat failid, mis olid avaldatud tema Blockchain plaadil. Põhjus, miks Blockchain andmeid niimoodi alla laaditi, erinevalt nullist sünkroniseerimisest, oli vähendada võrgu ribalaiuse kitsaskohti.


Selle puhul oli üks suur hoiatus: andmed, mida kasutajad laadisid alla knightmbist [ei kontrollinud Bitcoin tarkvara](https://Bitcoin.stackexchange.com/a/113682/69518) käivitamisel. Fail blkindex.dat sisaldas UTXO komplekti ja tarkvara aktsepteeris kõiki selles olevaid andmeid, nagu oleks ta neid juba kontrollinud. knightmb oleks võinud andmeid manipuleerida, et anda endale või kellelegi teisele bitcoine.


Jällegi tundus, et inimesed olid sellega nõus ning invaliidiploki ja selle järeltulijate ümberpööramine oli edukas. Kaevandajad hakkasid töötama bloki [74637](https://Mempool.space/block/0000000000606865e679308edf079991764d88e8122ca9250aef5386962b6e84) uue järeltulija kallal ja vastavalt bloki Timestamp-le ilmus järeltulija kell 23:53 UTC, umbes 6 tundi pärast probleemi avastamist. Järgmisel päeval, 16. augustil kell 08:10 oli uus kett umbes plokis 74689 vanast ketist möödunud, mistõttu kõik mitte-uuendatud sõlmed reorganiseerusid, et järgida uut ketti. See on Bitcoin ajaloo kõige sügavam reorg - 52 plokki -.


Võrreldes OP_RETURN probleemiga on seda probleemi käsitletud mõnevõrra puhtamalt:


- Ei ole ainult binaarset plaastri väljaannet
- Väljaantud tarkvara töötas nagu ette nähtud
- Nr Hard Fork


Kasutajatel paluti ka selle probleemi ajal Mining peatada. Me võime arutada, kas see on hea mõte või mitte, kuid kujutage ette, et te olete Miner ja olete veendunud, et kõik plokid, mis asuvad halva ploki peal, hävitatakse lõpuks sügavas reorgis: miks te raiskate ressursse Mining hukule määratud plokkidele?


Sa võid ka arvata, et on natuke kahtlane teha nii, nagu Nakamoto soovitas, ja laadida Blockchain, sealhulgas UTXO komplekti, juhusliku tüübi Hard kettalt alla. Kui nii, siis on teil õigus: see on kahtlane. Aga arvestades asjaolusid, oli see hädaolukorra lahendamine mõistlik.


Selle juhtumi ja eelmise OP_RETURN juhtumi vahel on oluline erinevus: seda probleemi kasutati ära looduses ja seega oli parandamine lihtsam. OP_RETURN puhul pidid nad paranduse varjama ja tegema avalikke avaldusi, mis ei paljastanud otseselt, milles probleem seisnes.


#### 2013-03-11 DB-lukustuse probleem 0.7.2 - 0.8.0 (CVE-2013-3220)



Väga huvitav ja hariduslikult väärtuslik küsimus kerkis esile 2013. aasta märtsis. Ilmnes, et Blockchain oli pärast plokki 225429 lõhenenud (kuigi alljärgnevas tsitaadis on kasutatud sõna "Fork"). Selle juhtumi üksikasjad olid [teatatud BIP50](https://github.com/Bitcoin/bips/blob/master/bip-0050.mediawiki). Kokkuvõttes öeldakse:


> Plokk, mille tehingute koguarv oli suurem kui varem nähtud, kaevandati ja edastati. Bitcoin 0.8 sõlmed said sellega hakkama, kuid mõned enne 0.8 Bitcoin sõlmed lükkasid selle tagasi, põhjustades Blockchain ootamatu Fork. Pre-0.8-ühilduvas ahelas (edaspidi 0.8-ahelas) oli sel hetkel umbes 60% Mining Hash võimsusest, tagades, et jagunemine ei laheneks automaatselt (nagu oleks juhtunud, kui pre-0.8-ahela oleks ületanud 0.8-ahela kogutööd, sundides 0.8-sõlmi ümber korraldama pre-0.8-ahelasse).
>

> Selleks, et taastada kanooniline kett võimalikult kiiresti, BTCGuild ja Slush alandasid oma Bitcoin 0,8 sõlmede arvu 0,7-le, nii et nende basseinid lükkaksid ka suurema ploki tagasi. See asetas enamuse hashpoweri ahelasse ilma suurema plokita, mistõttu 0.8 sõlmede ümberkorraldus lõpuks 0.8-eelsesse ahelasse.

Mining basseinide BTCGuild ja Slush kiire tegutsemine oli selles hädaolukorras hädavajalik. Nad suutsid suurema osa Hash võimust üle viia jagunemise 0,8-eelsele harule ja seega aidata taastada konsensust. See andis arendajatele aega jätkusuutliku lahenduse leidmiseks.


Väga huvitav on ka see, et versioon 0.7.2 ei ühildunud iseendaga, nagu see oli ka eelmiste versioonide puhul. Seda on selgitatud [BIP50] (https://github.com/Bitcoin/bips/blob/master/bip-0050.mediawiki#root-cause) jaotises "Põhjus":


> Ebapiisavalt kõrge BDB-luku konfiguratsiooniga oli kaudselt muutunud võrgu konsensusreegliks, mis määras ploki kehtivuse (kuigi
ebajärjekindel ja ebaturvaline reegel, kuna lukustuskasutus võib erineda sõlmede lõikes).


Lühidalt öeldes seisneb probleem selles, et andmebaasilukkude arv, mida Bitcoin Core tarkvara vajab ploki kontrollimiseks, ei ole deterministlik. Üks sõlm võib vajada X lukku, samas kui teine sõlm võib vajada X+1 lukku. Samuti on sõlmedel piirang, kui palju lukke Bitcoin võib võtta. Kui vajaminevate lukkude arv ületab piiri, loetakse plokk kehtetuks. Seega, kui X+1 ületab piiri, kuid mitte X, siis jagavad kaks sõlme Blockchain ja ei ole ühel meelel, milline haru on kehtiv.


Valitud lahendus, lisaks kahe reservi poolt konsensuse taastamiseks võetud viivitamatutele meetmetele, seisnes selles, et



- piirata plokke nii suuruse kui ka vajalike lukustuste osas versioonil 0.8.1
- parandada vanu versioone (0.7.2 ja mõned vanemad versioonid) samade uute reeglitega ja suurendada globaalset lukustuspiirangut.


Välja arvatud teises punktis nimetatud suurenenud üldine lukustuspiirang, rakendati neid eeskirju ajutiselt eelnevalt kindlaks määratud ajaks. Plaan oli need piirangud kaotada, kui enamik sõlmpunkte on uuendatud.


See Soft Fork vähendas oluliselt konsensuse ebaõnnestumise ohtu ja mõned kuud hiljem, 15. mail, deaktiveeriti ajutised reeglid ühiselt kogu võrgus. Pange tähele, et see deaktiveerimine oli tegelikult Hard Fork, kuid see ei olnud vaieldav. Lisaks sellele avaldati see koos eelneva Soft Fork-ga, nii et inimesed, kes kasutasid Soft-fooritud tarkvara, olid teadlikud, et sellele järgneb Hard Fork. Seetõttu jäi valdav enamus sõlmi konsensuse juurde, kui Hard Fork aktiveeriti. Kahjuks läksid aga mõned sõlmed, mis ei uuendanud, selle käigus kaduma.


Võib küsida, kas see oleks tänapäeval võimalik. Mining maastik on tänapäeval keerulisem ja sõltuvalt Hash võimsusest mõlemal pool jagunemist võib olla Hard piisavalt kiire sellise plaastri nagu BIP50 välja töötamine. Tõenäoliselt oleks Hard veenda "vale" haru kaevureid oma plokipreemiast lahti laskma.


#### BIP66



BIP66 on huvitav, sest selles rõhutatakse:



- hea valik krüptograafia
- vastutustundlik avalikustamine
- kasutuselevõtt ilma haavatavust paljastamata
- Mining kontrollitud plokkide peal


BIP66 oli ettepanek karmistada allkirjade kodeerimise eeskirju Bitcoin Scriptis. Motivatsioon](https://github.com/Bitcoin/bips/blob/master/bip-0066.mediawiki#motivation) oli, et oleks võimalik analüüsida allkirju muu tarkvara või raamatukogudega kui OpenSSL ja isegi OpenSSLi hiljutiste versioonidega. OpenSSL on üldotstarbelise krüptograafia raamatukogu, mida Bitcoin Core sel ajal kasutas.


Piirangutähis aktiveeriti 4. juulil 2015. Kuigi eespool öeldu vastab tõele, parandab BIP66 ka palju tõsisemat probleemi, mida ei ole BIPis mainitud.


##### Haavatavus



Selle küsimuse täielik avalikustamine avaldati 28. juulil 2015 Pieter Wuille'i poolt välja antud

[e-kiri Bitcoin-dev postiloendis](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-July/009697.html):


> Tere kõigile,
>

> Soovin avalikustada haavatavuse, mille avastasin 2014. aasta septembris ja mis muutus kasutamatuks, kui BIP66 95% künnis saavutati selle kuu alguses.
>

> Lühikirjeldus:
>

> Spetsiaalselt koostatud tehing oleks võinud Blockchain sõlmede vahel hargneda:
>

> - kasutades OpenSSL-i 32-bitistes süsteemides ja 64-bitistes Windows süsteemides
> - openSSL-i kasutamine muudes kui Windowsi 64-bitistes süsteemides (Linux, OSX, ...)
> - mõnede mitte-OpenSSL-i koodibaaside kasutamine allkirjade analüüsimiseks

E-kirjas on täpsemalt kirjeldatud, kuidas probleem avastati ja mis selle täpsemalt põhjustas. Lõpuks esitab ta sündmuste ajaskaala ja me kordame siinkohal mõned kõige olulisemad sündmused. Mõnda neist on, nagu joonisel eespool näidatud, juba kirjeldatud.


![](assets/bip66-timeline-1.webp)


BIP66-i ümbritsevate sündmuste ajakava. Mustas kirjas olevad punktid on selgitatud eespool.


##### Enne avastamist



Ilma, et keegi oleks sellest probleemist teadlik olnud, oleks seda saanud lahendada nüüdseks laialivalgunud BIP62, mis oli ettepanek vähendada tehingu vormistamise võimalusi. BIP62 kavandatavate muudatuste hulgas oli allkirjade kodeerimise konsensusreeglite karmistamine ehk "range DER-kodeerimine". Pieter Wuille pakkus 2014. aasta juulis välja mõned parandused BIPi, mis oleksid probleemi lahendanud:


> 2014-Jul-18: Selleks, et Bitcoin allkirjade kodeerimise eeskirjad ei sõltuks OpenSSLi spetsiifilisest parserist, muutsin BIP62 ettepanekut nii, et selle range DER-allkirjade nõue kehtiks ka 1. versiooni tehingute suhtes. Sel ajal ei kaevandatud enam mitte-DER-allkirju plokkidesse, seega eeldati, et sellel ei ole mingit mõju. Vt https://github.com/Bitcoin/bips/pull/90 ja http://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2014-July/006299.html. Sel ajal ei olnud teada, kuid kui see oleks kasutusele võetud, oleks see lahendanud haavatavuse.

Kuna see piiritähis oli väga laiaulatuslik ja hõlmas oluliselt rohkem kui ainult "ranget DER-kodeerimist", muutus see pidevalt ja ei jõudnud kunagi kasutuselevõtu lähedale. Hiljem võeti see piiritähis tagasi, sest segregitud tunnistaja (BIP141) lahendas tehingu muutlikkuse teistsugusel ja täielikumal viisil.


##### Pärast avastamist



OpenSSL andis välja uued versioonid oma tarkvarast koos parandustega, mis, kui neid oleks algusest peale Bitcoin-s kasutatud, oleks probleemi lahendanud. Kuid OpenSSLi mis tahes uue versiooni kasutamine ainult Bitcoin Core'i uues versioonis muudaks asja hullemaks. Gregory Maxwell selgitab seda teises [e-posti teemas](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-January/007097.html) 2015. aasta jaanuaris:


> Kuigi enamiku rakenduste puhul on üldiselt vastuvõetav, et mõned allkirjad lükatakse innukalt tagasi, on Bitcoin konsensussüsteem, kus kõik osalejad peavad üldiselt nõustuma sisendandmete täpse kehtivuse või kehtetuse osas.  Mõnes mõttes on järjepidevus tähtsam kui "korrektsus".
> [...]
> Eespool nimetatud parandused parandavad siiski ainult ühe sümptomi üldisest probleemist: konsensuse normatiivse käitumise toetumine tarkvarale, mis ei ole konsensuse kasutamiseks mõeldud või levitatud (eelkõige OpenSSL).  Seetõttu teen ettepaneku, et Soft-Fork oleks peagi suunatud Soft-Fork, et tagada range DERi vastavus, kasutades BIP62 alamhulka.

Ta juhib tähelepanu sellele, et selliste koodide kasutamine, mis ei ole mõeldud konsensussüsteemides kasutamiseks, kujutab endast tõsist ohtu, ja teeb ettepaneku, et Bitcoin rakendab ranget DER-kodeerimist. See on väga selge näide hea valikukrüptograafia tähtsusest.


Need sündmused võivad jätta mulje, et Gregory Maxwell teadis haavatavusest, mille Pieter Wuille hiljem avaldas, kuid tahtis aidata sisse viia paranduse, mis oli varjatud ettevaatusabinõuna, tõmbamata tegelikule probleemile liiga palju tähelepanu. See võib olla nii, kuid see on puhtalt spekulatsioon.


Seejärel loodi Maxwelli ettepanekul BIP66 kui BIP62 alamhulk, mis määratles ainult ranget DER-kodeerimist. See BIP võeti ilmselt laialdaselt vastu ja võeti juulis kasutusele, kuigi kaks Blockchain jagunemist toimusid irooniliselt *valitsuseta Mining* tõttu. Neid jagunemisi käsitletakse järgmises osas.


![](assets/bip66-timeline-2.webp)


Peamine järeldus sellest on, et piiripunktid peaksid olema enam-vähem *atomaarsed*, mis tähendab, et nad peaksid olema piisavalt täielikud, et pakkuda midagi kasulikku või lahendada konkreetne probleem, kuid piisavalt väikesed, et võimaldada kasutajate laialdast toetust. Mida rohkem asju te BIPi sisse panete, seda väiksem on tõenäosus, et see võetakse vastu.


##### Valideerimisvaba Mining tõttu tekkinud lõhenemine



Kahjuks ei lõppenud BIP66 lugu sellega. Kui BIP66 aktiveeriti, osutus see üsna räpaseks, sest mõned kaevurid ei kontrollinud plokke, mida nad üritasid laiendada. Seda nimetatakse valideerimiseta Mining ehk SPV-Mining (nagu Simplified Payment Verification). Bitcoin sõlmedele saadeti hoiatussõnum koos lingiga [probleemi kirjeldavale veebilehele](https://Bitcoin.org/en/alert/2015-07-04-spv-Mining):


> 4. juuli 2015. aasta varahommikul saavutati 950/1000 (95%) künnis. Varsti pärast seda kaevandas väike Miner (osa uuendamata 5%) kehtetu ploki - see oli ootuspärane juhtum. Kahjuks selgus, et umbes pool võrgu Hash määrast oli Mining ilma täielikult valideerimata plokid (nn SPV Mining) ja ehitas selle kehtetu ploki peale uusi plokke.

Hoiatuslehel anti inimestele korraldus oodata 30 täiendavat kinnitust, kui nad kasutasid Bitcoin Core'i vanemaid versioone.


Eespool mainitud jagunemine toimus 2015-07-04 kell 02:10 UTC pärast ploki kõrgust [363730](https://Mempool.space/block/000000000000000006a320d752b46b532ec0f3f815c5dae467aff5715a6e579e). See probleem sai lahendatud kell 03:50 samal päeval, pärast seda, kui 6 kehtetut plokki oli kaevandatud. Kahjuks juhtus sama probleem järgmisel päeval, st 2015-07-05 kell 21:50 uuesti, kuid seekord kestis kehtetu haru ainult 3 plokki.


![](assets/bip66-timeline-3.webp)

Sündmused, mis viisid BIP66-ni, selle kasutuselevõttu ja selle tagajärgi, on väga hea näide sellest, kui ettevaatlikud peavad Bitcoin arendajad olema. Mõned peamised järeldused BIP66-st:



- Tasakaal avatuse ja haavatavuse mitteavaldamise vahel on väga delikaatne.
- Avaldamata haavatavuste paranduste kasutuselevõtt on keeruline mäng.
- Konsensuse säilitamine on Hard.
- Tarkvara, mis ei ole mõeldud konsensussüsteemidele, on üldiselt riskantne.
- Piirangud peaksid olema mõnevõrra atomaarsed.


### Kokkuvõte Kui sitt tabab ventilaatorit



Bitcoin-l on vead. Inimesi, kes avastavad vigu, julgustatakse neid Bitcoin arendajatele vastutustundlikult avaldama, et nad saaksid vea parandada ilma seda avalikult avaldamata. Ideaaljuhul võib vea parandamise maskeerida tulemuslikkuse parandamise või muu suitsukattega.


Oleme vaadelnud mõningaid tõsisemaid probleeme, mis on aastate jooksul esile kerkinud, ja seda, kuidas neid käsitleti. Mõned avastati avalikult ekspluateerimise kaudu, teised aga avalikustati vastutustundlikult ja neid sai parandada enne, kui pahatahtlikel osalejatel oli võimalus neid ära kasutada.


## Arutelu küsimused

<chapterId>91462ca7-f09c-55da-a5b9-3e211de31da5</chapterId>


Need aruteluküsimused ei ole lihtsalt kokkuvõte "Bitcoin arengufilosoofia" sisust, need on mõeldud selleks, et julgustada teid edasi uurima, nii et minge kindlasti välja ja uurige.


Saate testida oma arusaamise sügavust, kirjutades [mini-essee](https://www.youtube.com/watch?v=N4YjXJVzoZY) 100-300 sõnaga, valides teema sellest küsimuste kogumist. Kui soovite oma töö kohta tagasisidet, võite saata selle aadressile mini-essay@planb.network, me vaatame selle hea meelega üle.


#### Detsentraliseerimine



- Detsentraliseerimine on Hard. Miks me kõik see vaeva näeme, et see toimiks? Kas me võiksime valida hübriidse lähenemisviisi, kus mõned osad on tsentraliseeritud ja teised mitte?
- Kas detsentraliseerimine toob kaasa topeltkulude probleemi või nõuab topeltkulude probleem detsentraliseerimist? Kuidas Satoshi lahendas topeltkulude probleemi?
- Millistes aspektides on Bitcoin ikka veel kõige rohkem tsensuuri suhtes altid ja miks on tsensuur nii halb asi? Kas on mingeid argumente tsensuuri kasuks?
- On märgitud, et Bitcoin on loata. Kas on ka teisi makseviise, mida võiksite pidada loata?



#### Usaldamatus




- Usaldamatus on sageli spekter, mitte binaarne. Millised Bitcoin aspektid on pigem Trustless ja millised on tavaliselt seotud kõrgema usalduse tasemega? Kas neid saab leevendada?
- Te soovite käivitada Full node, et oleks võimalik kõik tehingud täielikult valideerida. Te laadite Bitcoin Core alla aadressilt https://Bitcoin.org/en/download. Kuhu te usaldasite ja kus te täielikult Trustless?
- Kas Trustless süsteemi saab ehitada usaldusväärse süsteemi peale?



#### Privaatsus




- Millised on mõned olulised eelised, mida kasutaja saab, kui ta säilitab Bitcoin-ga suhtlemisel hea privaatsuse? Millised on mõned altruistlikud eelised võrgu jaoks?
- Kuidas mõjutab aadresside taaskasutamine teie privaatsust?
- Bitcoin kasutab UTXO mudelit, samas kui mõned alternatiivsed krüptovaluutad kasutavad kontomudelit. Millised on selle valiku tagajärjed eraelu puutumatusele?



#### Lõplik Supply




- Milline on seos Bitcoin lõpliku Supply ja selle mündi väljaandmise vahel Coinbase Transaction kaudu? Milline on müntide emiteerimise ja turvalisuse eelarve vaheline seos ja kuidas need on vastuolus?
- Milliseid parameetreid võis Satoshi muuta Bitcoin Supply mütsi muutmiseks? Mis muutuks, kui ta oleks otsustanud Supply ülempiiri 1 miljonile? Kuidas oleks 1 triljon?
- Miks pooldavad mõned inimesed Bitcoin Supply suurendamist? Kas te arvate, et see juhtub?


#### Uuendamine



- Mis on Speedy Trial ja miks oli vaja aktiveerida Taproot?
- Miks me vajame nii suurt protsentuaalset kaevurite uuendamist softforkis? Miks ei ole künnis lihtsalt 51%?



#### Vastandlik mõtlemine




- Mis on sybil-rünnak ja mis teeb detsentraliseeritud võrgu selle suhtes nii vastuvõtlikuks?
- Miks on oluline, et kõik Bitcoin võrgustiku osalised - ja mitte ainult arendajad - mõtleksid vastandlikult?



#### Avatud lähtekood




- Ainult vähestel hooldajatel on vajalikud GitHubi õigused koodi ühendamiseks [Bitcoin Core](https://github.com/Bitcoin/Bitcoin) repositooriumi. Kas see ei ole vastuolus lubadeta võrguga?
- Kas avatud lähtekoodiga arendusprotsess on vastuvõtlik sybil-rünnakule? Kui jah, siis kuidas te selle vastu võitleksite?
- Millised on kolmandate osapoolte avatud lähtekoodiga raamatukogudele tuginemise eelised ja puudused ning milline on Bitcoin Core'i lähenemisviis?
- Millisel viisil on meil vaja ülevaatamist lisaks koodi ülevaatamisele? Kuidas määrata, kui palju ülevaatamist on piisav?
- Kuidas me tagame, et Bitcoin kallal töötab alati piisavalt asjatundlikke inimesi? Mis juhtub, kui neid ei ole, ja kuidas me hindame nende ausust ja kavatsusi?



#### Skaala




- Väidetakse, et jagamine pakub skaleerimisega seotud eeliseid keerukuse arvelt. Miks me peaksime või ei peaks vastu võtma tehnoloogilisi täiustusi, sest neid on raske mõista, isegi kui need tunduvad tehnoloogiliselt mõistlikud?
- Millised on mõned näited Bitcoin-s kasutusele võetud sisemiste skaalamismeetodite kohta?
- Miks on vertikaalne skaleerimine detsentraliseeritud süsteemis palju keerulisem? Kuidas on lood horisontaalse skaleerimisega?
- Tundub, et me ei ole kaugeltki jõudnud üksmeelele selles, kuidas me saaksime kogu maailma Bitcoin pardale võtta. Kas Satoshi ei oleks pidanud vähemalt välja mõtlema, kuidas sinna jõuda, enne Mining esimest plokki 2009. aastal?
- Kuidas liigitaksite (vertikaalne, horisontaalne, sissepoole või mitte skaalumistehnika) iga järgmist: sharding, plokimahu suurendamine, SegWit, SPV-sõlmed, tsentraliseeritud vahetused, Lightning Network, plokkide intervalli vähendamine, Taproot, sidechains



# Lõplik osa


<partId>4b6ff4ef-b9ea-4c48-b05f-62d41a38fbbb</partId>


## Arvamused ja hinnangud


<chapterId>d334a837-df46-4989-9cad-8d8779147dbe</chapterId>


<isCourseReview>true</isCourseReview>

## Kokkuvõte


<chapterId>b77ed55c-b13a-430b-a212-37aab527b9e7</chapterId>


<isCourseConclusion>true</isCourseConclusion>