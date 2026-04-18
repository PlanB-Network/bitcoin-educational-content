---
name: Bitaxe avatud lähtekoodiga Mining Mastery
goal: Kogu Bitaxe ökosüsteemi omandamine, alates riistvara kokkupanekust kuni täiustatud kohandamise ja jõudluse optimeerimiseni
objectives: 

  - Avatud lähtekoodiga Bitcoin mining riistvara filosoofia mõistmine
  - Bitaxe mining seadmete ehitamine algusest peale
  - mining tarkvara, sealhulgas AxeOS ja Public Pool, konfigureerimine ja optimeerimine
  - Rakendada täiustatud jõudluse optimeerimist, sealhulgas ületaktimist ja võrdlusuuringuid

---

# Teie Bitaxe Mining juhend


Tere tulemast terviklikule Bitaxe'i kursusele, kus saate omandada revolutsioonilise avatud lähtekoodiga Bitcoin mining riistvara, mis demokratiseerib juurdepääsu mining tehnoloogiale. See kursus viib teid detsentraliseeritud mining filosoofiliste aluste mõistmisest kuni täiustatud riistvara kohandamise ja jõudluse optimeerimise tehnikateni.


Bitaxe'i projekt kujutab endast paradigmamuutust Bitcoin mining valdkonnas, murdes ASIC tootjate monopoli, pakkudes täielikult avatud lähtekoodiga projekte, püsivara ja tarkvara. Nende praktiliste peatükkide kaudu saate praktilisi oskusi riistvara kokkupaneku, tarkvara konfigureerimise, trükkplaadi disaini ja jõudluse optimeerimise kohta.


Varasemat mining kogemust ei ole vaja, kuid elektroonika alusteadmised ja GitHubi tundmine tulevad kasuks. Kursus muudab teid uudishimulikust vaatlejast võimekaks Bitaxe'i ehitajaks ja panustajaks.

Märkus: Selle kursuse videod on saadaval ainult inglise keeles.

+++


# Sissejuhatus


<partId>6b3cd9f0-0063-40f0-a7bb-00a48f330d88</partId>


## Kursuse ülevaade


<chapterId>1fac9579-0e1c-48e3-9bc5-e7a2960018c8</chapterId>


Tere tulemast kursusele MIN 306 _**Bitaxe Open Source Mining Mastery**_, mis on põhjalik teekond Bitaxe mining maailma. See kursus on mõeldud neile, kes soovivad mõista, ehitada ja optimeerida oma Bitaxe mining riistvara, uurides samal ajal filosoofilisi ja tehnilisi aluseid, mis teevad selle projekti Bitcoin ökosüsteemis ainulaadseks.


### Bitaxe'i mõistmine


Esimeses osas pannakse alus: te saate teada Bitaxe'i projekti päritolu, selle arengut ning detsentraliseerimise ja läbipaistvuse väärtusi, mis seda määratlevad. Saate teada, mis on Bitaxe tegelikult, kuidas see erineb patenteeritud ASIC-dest ja kust leida kogukonna ressursse oma teadmiste süvendamiseks. See osa annab vajaliku konteksti, et mõista, miks Bitaxe kujutab endast pöördepunkti Bitcoin mining ajaloos.


### Tarkvara ja operatsioonid


Teine osa keskendub tarkvarakeskkonnale, kus tutvustatakse üksikasjalikult *AxeOS*: spetsiaalselt Bitaxe-seadmete jaoks loodud avatud lähtekoodiga operatsioonisüsteemi. Saate teada selle põhifunktsioone ning seda, kuidas seadet konfigureerida ja sellega suhelda, et alustada oma esimest mining operatsiooni.


### Ühendus ja koostöö


Kolmandas osas rõhutatakse projekti koostööaspekti. Te uurite avatud lähtekoodiga filosoofiat, mida rakendatakse nii Bitaxe'i riistvara kui ka tarkvara arendamisel. Praktiliste harjutuste kaudu saate teada, kuidas otse lähtekoodi panustada, ning te avastate ka _Public Pool_, kogukonna platvormi arvutusvõimsuse koondamiseks. Samuti saate teada, kuidas seda paigaldada Umbrel-sõlme kohalikuks ja suveräänseks integreerimiseks.


### Riistvara kokkupanek ja tõrkeotsing


Neljandas jaotises sukeldute riistvara enda sisse. Te saate teada, kuidas tuvastada Bitaxe'i kokkupanekuks vajalikud tööriistad, parandada jootmisprobleeme ja teostada täielikku diagnostikat *AxeOS* ja USB-tööriistade abil. Selles osas rõhutatakse praktilist tegevust ja sügavat arusaamist sellest, kuidas riist- ja tarkvarakomponendid omavahel suhtlevad.


### Täiustatud kohandamine


Viies osa on pühendatud kohandamisele. Saate teada, kuidas muuta PCB-d (trükkplaati), luua tehase faili ja kasutada _Bitaxe Web Flasher_. See osa on mõeldud neile, kes soovivad minna kaugemale lihtsast kokkupanekust ja tõesti kujundada oma seadme kohandatud versioone.


### Tulemuslikkuse optimeerimine


Kuues osa käsitleb täiustatud optimeerimistehnikaid. Saate teada, kuidas oma Bitaxe'i jõudluse hindamiseks võrrelda ja kuidas seda tõhusalt üle taktida. Need oskused aitavad teil oma riistvarast maksimumi välja võtta, austades samas selle füüsilisi piiranguid.


Nagu iga Plan ₿ Academy kursuse puhul, sisaldab viimane osa hindamist, mille eesmärk on kinnistada teie teadmisi.


Sukelduge otse sellesse tehnilisse seiklusesse - Bitcoin mining tulevik on teie kätes!


# Bitaxe'i mõistmine

<partId>ba1cb4ea-6a77-54fd-916c-57285c8c2418</partId>


## Ajalugu

<chapterId>73d928e5-72f0-5c17-a7a6-8b6ece7f9a30</chapterId>

:::video id=67d2529a-b7cb-4804-b02c-e56c12c9e66e:::

Bitaxe'i projekt kujutab endast murrangulist muutust Bitcoin [mining](https://planb.academy/resources/glossary/mining) riistvara arendamises, tuues avatud lähtekoodiga põhimõtted tööstusesse, kus domineerivad patenteeritud lahendused. Selles õppesarjas uuritakse Bitaxe'i põhjalikku ajalugu, tehnilisi uuendusi ja kogukonna juhitud arengut, andes ülevaate sellest, kuidas ühe inseneri visioonist sai detsentraliseeritud mining riistvara edukas ökosüsteem. Uurides projekti päritolu, probleeme ja saavutusi, saame väärtusliku ülevaate nii [ASIC](https://planb.academy/resources/glossary/asic) arendamise tehnilistest keerukustest kui ka avatud lähtekoodiga koostöö võimsusest Bitcoin valdkonnas.


### Päritolulugu: Solar Mining visioon: Siiditee avastamisest Solar Mining visioonini


Bitaxe'i asutaja Skot alustas oma teekonda Bitcoin-sse kolledži peol, kus ta sai Bitcoin-st esimest korda teada, kui keegi ostis esemeid Siiditeel. See esialgne kokkupuude Bitcoin-ga, mille hind oli umbes 20 dollarit mündi kohta, tekitas uudishimu, mis hiljem kujunes revolutsiooniliseks mining projektiks. Tema tulevase töö tehniline alus loodi ülikoolis õppimise ajal, kus tal oli juurdepääs ulatuslikele FPGA-vahenditele laboratooriumis. Töötades koos oma juhendajaga, hakkas Skot eksperimenteerima avatud lähtekoodiga FPGA bitivoogudega Bitcoin mining jaoks, esialgu tagasihoidliku eesmärgiga mining piisavalt Bitcoin, et osta oma kontorisse pitsat.


Üleminek akadeemilistelt katsetustelt tõsisele arendustegevusele toimus aastaid hiljem, kui Skot töötas päikeseenergial töötavate väravate kallal andmete kaugkogumiseks Aafrikas. See erialane kogemus päikeseenergiasüsteemidega tekitas arusaama, et Bitcoin mining ASIC-d, mis on põhimõtteliselt madalpinge alalisvoolu seadmed, sobiksid suurepäraselt päikesepaneelidega. Kontseptsioon tundus loomulik ja elegantne. Kuid kui Skot hakkas olemasolevaid lahendusi uurima, avastas ta turul märkimisväärse lünga: erinevalt Bitcoin mining algusaegadest, mil FPGA-disainid olid avalikult kättesaadavad, oli ASICide tulek viinud tööstuse täiesti patenteeritud, suletud lähtekoodiga lahenduste suunas.


Avatud lähtekoodiga mining riistvara puudumine muutus Skoti jaoks pettumuseks, eriti arvestades tema tausta avatud lähtekoodiga tarkvara arendamisel ja tema veendumust, et Bitcoin avatud lähtekoodiga olemus peaks laienema ka mining infrastruktuurile. See filosoofiline lähenemine avatud lähtekoodiga põhimõtetele koos tehnilise väljakutsega, mis tulenes ASIC patenteeritud disainilahenduste tagasitöötlusest, pani aluse sellele, millest sai Bitaxe'i projekt. Esialgne visioon oli ambitsioonikas, kuid samas praktiline: luua päikeseenergial töötav Bitcoin [kaevandaja](https://planb.academy/resources/glossary/miner), mis suudaks töötada iseseisvalt, ilma et vajaks eraldi arvutit kontrollimiseks, mis võimaldaks seda kasutada kaugetes kohtades päikesepaneelide all.


### Tehnilised väljakutsed ja pöördtehnilised läbimurded


Bitaxe'i arendamiseks oli vaja ületada olulisi tehnilisi takistusi, mis keskendusid peamiselt Bitmaini ASIC kiipide dokumentatsiooni täielikule puudumisele. Skoti lähenemine sellele väljakutsele näitas, kui sihikindel ja leidlik on edukas pöördprojekteerimine. Kuna tal puudus juurdepääs ametlikele andmelehtedele või tehnilistele spetsifikatsioonidele, kasutas ta kiipide uurimist mikroskoobi all, tihvtide sammude mõõtmist kalibreerimisvahenditega ja isegi kiipide skaneerimist, et määrata kindlaks nende täpne jalajälg. Selle vaevarikka protsessi tulemuseks oli mitu ebaõnnestunud prototüüpi, kusjuures kaks esimest "päevakaevuri" iteratsiooni ei toiminud korralikult, kuna jalajälje arvutused olid valed.


Läbimurre tuli kolmanda iteratsiooniga 2022. aasta mais, kui Skot lõi edukalt toimiva kahe kiibi disaini, kasutades Antminer S9 seadmetest korjatud BM1387 kiipe. See saavutus tähistas nime Bitaxe sündi, mis oli inspireeritud Bitcoin mining jaoks mõeldud kiirkontseptsiooni kontseptsioonist. Selle disaini edu kinnitas tagasipööratud inseneri lähenemisviisi ja näitas, et sõltumatud arendajad saavad luua toimivat mining riistvara ilma tootja toetuseta. Tehnilised väljakutsed ulatusid aga kiibi liidestamisest kaugemale ja hõlmasid ka keerukat toiteallika projekteerimist, kuna ASIC-id nõudsid suure voolutugevuse juures täpset pingeregulatsiooni, mis sageli töötas vaid 0,6-voldise pingega, võttes samal ajal märkimisväärset voolutugevust.


Firmatarkvara arendamisega kaasnes veel üks keerukuse tase, kuna projekti jaoks oli vaja luua mining tarkvara, mis oleks võimalik käivitada otse ESP32 mikrokontrolleril, mitte tugineda välistele arvutitele, kus töötab tarkvara, näiteks CGMiner. Selline iseseisev lähenemisviis oli oluline Skoti nägemuse jaoks, mille kohaselt on mining üksused iseseisvalt kasutatavad. Riistvara tagasipööramise ja varjatud püsivara arendamise kombinatsioon tekitas ulatusliku tehnilise väljakutse, mis nõudis teadmisi mitmest erialast, alates elektrotehnilisest projekteerimisest ja trükkplaatide disainist kuni varjatud programmeerimise ja võrguprotokollideni.


### Kogukonna moodustamine ja avatud lähtekoodiga koostöö


Bitaxe'i muutumine sooloprojektist õitsvaks kogukondlikuks algatuseks on selle edu üks olulisemaid aspekte. Esialgu said Skoti katsed generate huvi äratada Bitcoin foorumites ja sotsiaalmeedias piiratud vastukaja ja aeg-ajalt skeptilisuse osaliseks. Läbimurre tuli siis, kui kogukonnaliikmed nagu SirVapesAlot tunnistasid avatud lähtekoodiga mining potentsiaali ja asutasid Open Source Miners United (OSMU) Discord-serveri. See platvorm pakkus projekti õitsenguks vajaliku koostöökeskkonna, meelitades ligi erineva taustaga osalejaid, kes jagasid ühist huvi Bitcoin mining tehnoloogia demokratiseerimise vastu.


Kogukonnapõhine arendusmudel osutus märkimisväärselt tõhusaks, kuna sellised võtmetegijad nagu johnny9 ja Ben hakkasid tegelema konkreetsete tehniliste probleemidega. Johnny9 teadmised püsivara arendamises lahendasid kriitilised tarkvara rakendamise probleemid, samas kui Ben arendusoskused lõid intuitiivse AxeOSi armatuurlaua, mis lihtsustas seadme konfigureerimist ja jälgimist. Beni täiendav panus hõlmas tootmisvõimaluste loomist ja avatud lähtekoodiga [mining-pool](https://planb.academy/resources/glossary/pool-mining), mis on optimeeritud Bitaxe-seadmete jaoks. Selline koostööpõhine lähenemisviis näitas, kuidas avatud lähtekoodiga põhimõtete abil saab kiirendada arendustegevust rohkem, kui üksikud osalejad üksi suudaksid saavutada.


OSMU kogukond edendas ka kaasavat keskkonda, kus uustulnukad said õppida ja anda oma panuse sõltumata nende algsetest tehnilistest teadmistest. Beni enda teekond jootmise algajaist suurtööstajaks on hea näide sellest külalislahkest lähenemisviisist oskuste arendamisele. Kogukonna pühendumine haridusele ja vastastikusele toetusele lõi positiivse tsükli, kus kogenud liikmed juhendasid uusi tulijaid, kes seejärel ise muutusid panustajateks. See mudel osutus oluliseks, et projekti laiendada algsest ulatusest kaugemale ja luua jätkusuutlik ökosüsteem jätkuvaks innovatsiooniks ja kasvuks.


### Detsentraliseeritud Mining visioon ja tulevane mõju


Skoti pikaajaline nägemus Bitaxe'i kohta ulatub kaugemale teise mining seadme loomisest: see on Bitcoin mining maastiku põhjalik ümberkujundamine. Ambitsioonikas eesmärk toota üks miljon ühe terahashi kaevandajat tekitaks mining hajutatud võimu eksahashi, mis kujutab endast olulist sammu mining detsentraliseerimise suunas. See visioon käsitleb kriitilisi muresid mining tsentraliseerimise pärast, kus suured basseinid ja tööstuslikud tegevused võivad sattuda valitsuse surve alla või olla reguleeritud. Jagades mining energiat lugematute kodukaevandajate vahel, muutub võrk vastupidavamaks ja viiakse vastavusse Bitcoin detsentraliseeritud põhimõtetega.


Seda visiooni toetav majandusmudel tugineb koduse mining ainulaadsetele omadustele, kus infrastruktuurikulud on sisuliselt null ja kaevurid saavad tegutseda minimaalse järelevalvega. Erinevalt tööstuslikest mining toimingutest, mis nõuavad suuri kapitaliinvesteeringuid rajatistesse, elektriinfrastruktuuri ja jahutussüsteemidesse, saavad kodused kaevandajad lihtsalt ühendada seadmed olemasolevatesse elektripistikutesse ja internetiühendustesse. Selline lähenemisviis võiks teoreetiliselt tuua märkimisväärse [hash-kiiruse](https://planb.academy/resources/glossary/hashrate) võrgus ilma traditsiooniliste sisenemistõketeta, mis iseloomustavad suuremahulisi mining operatsioone.


Projekti edu on juba hakanud mõjutama laiemat Bitcoin mining ökosüsteemi, mis võib inspireerida ka teisi tootjaid kasutama avatud lähtekoodiga arendusmudeleid. Bitaxe'i tootjate poolt näidatud rahaline elujõulisus tõestab, et avatud lähtekoodiga riistvara võib olla äriliselt edukas, säilitades samal ajal läbipaistvuse ja kogukonna kaasatuse. Kuna projekt areneb jätkuvalt uute kiibiintegratsioonide, täiustatud disainilahenduste ja laiendatud tootmispartnerluste abil, on see kontseptsiooni tõestuseks, kuidas Bitcoin mining saab naasta oma detsentraliseeritud juurte juurde, võttes samal ajal kasutusele kaasaegse ASIC tehnoloogia. Lõppeesmärk ulatub kaugemale kui pelgalt hash-kiiruse levitamine ja hõlmab ka hariduslikku mõju, tuues rohkem inimesi otsekontakti Bitcoin mining põhiprotsessiga ja edendades võrgu turvamudeli sügavamat mõistmist.


## Mis on Bitaxe?

<chapterId>6a56af56-35ce-51af-999b-4bc7305e6464</chapterId>

:::video id=12b26c7a-74b1-4ea9-afc0-e3ef90cf5837:::

### Riistvara ülevaade ja võimalused


Bitaxe'i ökosüsteem hõlmab mitmeid riistvara iteratsioone, millest igaühe eesmärk on optimeerida mining kogemuse erinevaid aspekte, säilitades samal ajal avatud lähtekoodiga ligipääsetavuse põhifilosoofia. Need seadmed ei ole mitte ainult funktsionaalne mining riistvara, vaid ka õppevahendid, mis võimaldavad kasutajatel mõista ASIC kiipide, mikrokontrollerite ja Bitcoin mining protsessi keerulist seost. Bitaxe'i disainifilosoofia ja tehnilise rakendamise mõistmine annab väärtusliku ülevaate sellest, kuidas kaasaegne mining riistvara toimib nii komponentide kui ka süsteemi tasandil.



### Bitaxe Max, esimese põlvkonna rakendamine


Bitaxe Max kujutab endast Bitaxe'i kontseptsiooni põhilist rakendamist, kasutades BM1397 ASIC kiipi, mille Bitmain on algselt välja töötanud oma S17 mining seeria jaoks. See kiibi integreerimine näitab, kuidas avatud lähtekoodiga riistvara saab olemasolevat ASIC tehnoloogiat ümber kasutada, et luua kättesaadavaid mining lahendusi. Bitaxe Max pakub hinnanguliselt 300-400 gigahashi sekundis, mis asetab selle pigem hariduslikuks ja eksperimentaalseks mining platvormiks kui kommertsmahus lahenduseks.


BM1397 kiibi integreerimine Bitaxe Maxi nõudis energiajuhtimise, soojusjuhtimise ja kommunikatsiooniprotokollide hoolikat kaalumist. Plaadi konstruktsioon vastab selle ASIC spetsiifilistele nõuetele, pakkudes samal ajal stabiilseks toimimiseks vajalikke toetavaid vooluahelaid. See rakendamine näitab, kuidas avatud lähtekoodiga riistvaraarenduse abil saab kasutada olemasolevat pooljuhttehnoloogiat, et luua uusi rakendusi ja õppimisvõimalusi mining kogukonnas.


### Bitaxe Ultra, täiustatud kiibitehnoloogia


Bitaxe Ultra on Bitaxe platvormi edasiarendus, mis sisaldab Bitmaini S19-seeria täiustatud BM1366 ASIC kiipi. See uuem kiibitehnoloogia toob Bitaxe'i platvormile parema tõhususe ja jõudluse, säilitades samas sama põhimõttelise disainifilosoofia. BM1366 kiibile üleminek näitab platvormi kohanemisvõimet ja kogukonna pühendumust tehnoloogiliste edusammude kaasamisele avatud lähtekoodiga mining lahendustesse.


Üleminek BM1397 kiibilt BM1366 kiibile nõudis muudatusi plaadi toiteallikasüsteemides, soojusjuhtimises ja juhtimisalgoritmides. Need muudatused illustreerivad riistvara arendamise iteratiivset iseloomu ja ühilduvuse säilitamise olulisust jõudluse suurendamise ajal. Bitaxe Ultra rakendamine annab kasutajatele juurdepääsu uuemale ASIC tehnoloogiale, säilitades samal ajal platvormi haridusliku ja eksperimentaalse iseloomu.


### Mikrokontroller ja sidesüsteemid


Iga Bitaxe-seadme keskmes on ESP-mikrokontroller, mis on peamine liides kasutaja ja ASIC kiibi vahel. Sellel mikrokontrolleril töötab Open Source Miners United (OSMU) kogukonna poolt välja töötatud spetsiaalne tarkvara, mis võimaldab ASIC tööparameetrite täpset kontrollimist. Side mikrokontrolleri ja ASIC vahel toimub hoolikalt kavandatud jadaühendusliinide kaudu, mis on nähtavate jälgedena otse trükkplaadile söövitatud.


Mikrokontrolleri roll ulatub kaugemale lihtsast ASIC juhtimisest: see hõlmab ka toitehaldust, temperatuuri jälgimist ja kasutajaliidese funktsioone. Integreeritud ekraani kaudu saavad kasutajad jälgida kriitilisi tööparameetreid, nagu temperatuur, hash-kiirus, IP-aadress ja muu asjakohane mining statistika. See reaalajas tagasisidesüsteem annab väärtusliku ülevaate seadme jõudlusest ja aitab kasutajatel optimeerida mining toimimist, õppides samal ajal tundma riistvara aluseks olevat käitumist.


### Toitehaldus ja ohutusega seotud kaalutlused


Bitaxe'i platvorm töötab range 5-voldise vooluvoolu nõudega, mistõttu on seadme pikaealisuse ja ohutuse seisukohalt kriitilise tähtsusega õige toiteallika valik. Bitaxe'i plaatide toitejuhtimissüsteem sisaldab keerukat vooluahelat, mis on mõeldud ASIC kiibi pingevarustuse reguleerimiseks, jälgides samal ajal energiatarbimist eri töörežiimide puhul. Selline toitehalduse võime võimaldab seadmel töötada tõhusalt erinevate sisemiste sageduste ja pingete vahemikus, tarbides sõltuvalt konfiguratsioonist tavaliselt 5-25 vatti.


Võimsusnõuete mõistmine muutub otsustavaks, kui arvestada, et vale pingekasutus võib seadet jäädavalt kahjustada. Sageduse, pinge, energiatarbimise ja hash-kiiruse vaheline seos näitab ASIC tööpõhimõtteid, mis kehtivad kogu mining riistvara puhul. Kasutajad saavad eksperimenteerida erinevate võimsuse seadistustega, et mõista mining operatsioonidele omaseid tõhususe kompromisse, saades praktilisi kogemusi mõistetega, mida kohaldatakse suuremahuliste mining rakenduste puhul.


### Solo Mining fookus ja võrgustikus osalemine


Bitaxe'i platvorm on spetsiaalselt suunatud mining rakendustele, kus üksikud kaevurid püüavad lahendada Bitcoin [plokke](https://planb.academy/resources/glossary/block) iseseisvalt, mitte osaleda suurtes mining-poolides. Kuigi Bitaxe'i seadmete hash-kiiruse määr muudab eduka plokkide avastamise statistiliselt ebatõenäoliseks, teenib selline lähenemisviis Bitcoin kogukonnas olulisi hariduslikke ja filosoofilisi eesmärke. Solo mining koos Bitaxe'i seadmetega aitab kasutajatel mõista Bitcoin [proof-of-work](https://planb.academy/resources/glossary/proof-of-work) süsteemi fundamentaalset mehaanikat, aidates samal ajal kaasa võrgu detsentraliseerimisele.


Rõhuasetus mining soolole peegeldab OSMU kogukonna pühendumust julgustada individuaalset osalemist Bitcoin turvamudelis. Bitaxe'i platvorm võimaldab kasutajatel iseseisvalt töötava kättesaadava riistvara pakkumisega teostada oma mining operatsioone, ilma et nad peaksid toetuma koondinfrastruktuurile. Selline lähenemisviis soodustab Bitcoin [konsensusmehhanismi](https://planb.academy/resources/glossary/consensus) sügavamat mõistmist, toetades samal ajal võrgu detsentraliseeritud olemust kaevandajate suurema mitmekesisuse kaudu.


### Riistvara areng ja tootmise täiustamine


Bitaxe'i platvorm areneb jätkuvalt kogukonna tagasiside ja tootmise optimeerimise kaudu, kusjuures uuemad versioonid sisaldavad parandusi, mis parandavad valmistatavust ja kasutajakogemust. Versiooniuuendused keskenduvad tavaliselt pigem tootmise tõhususele kui põhimõttelistele tulemuslikkuse muudatustele, tagades, et olemasolevad kasutajad ei puutu kokku vananemise survega. Sellised funktsioonid nagu üleminek micro-USB-ühendustelt USB-C-pistikutele ja täiustatud toiteühendussüsteemid peegeldavad kogukonna tähelepanu praktilise kasutatavuse parandamisele.


Selline evolutsiooniline lähenemine näitab avatud lähtekoodiga riistvara arendamise eeliseid, kus kogukonna panus aitab kaasa järk-järgulistele parandustele, millest saavad kasu kõik kasutajad. Filosoofia "kui see on hashes, siis on see hashes" rõhutab platvormi keskendumist funktsionaalsusele, mitte pidevatele uuendustele, julgustades kasutajaid oma seadmeid hooldama ja kasutama, mitte püüdlema uusimate versioonide poole. Selline lähenemisviis toetab jätkusuutlikke riistvara kasutamise tavasid, säilitades samal ajal Bitaxe'i haridusliku väärtuse.


## Kus ma saan rohkem teada?

<chapterId>706f2fff-fa1c-5d8e-b14c-ece6e42c016f</chapterId>

:::video id=90088397-3a16-485f-bbd2-89cdbb844e4a:::

Bitaxe'i projekt kujutab endast terviklikku avatud lähtekoodiga mining algatust, mis ulatub kaugemale ühest seadmest. Arusaam sellest, kust leida usaldusväärset teavet, tehnilisi ressursse ja kogukonna toetust, on oluline kõigile, kes soovivad selles ökosüsteemis osaleda. Selles peatükis on esitatud täielik juhend oluliste platvormide ja ressursside kohta, mis moodustavad Bitaxe'i ja Open Source Miners United (OSMU) kogukonna aluse.


### Bitaxe.org, keskne keskus


Bitaxe.org veebisait on peamine juurdepääs kogu projektiga seotud teabele ja ressurssidele. See tsentraliseeritud platvorm on teie esimene tugipunkt, kui teil on vaja teada saada Bitaxe'i seadmete kohta või uurida teisi projekte OSMU kogukonnas. Veebisaidi kujunduses on esikohal ligipääsetavus ja organiseerimine, esitades külastajatele hoolikalt kureeritud linke, mis ühendavad erinevaid spetsialiseeritud ressursse kogu ökosüsteemis.


Selle keskse keskuse tähtsust ei saa ülehinnata, sest see kõrvaldab segaduse, mis sageli kaasneb detsentraliseeritud avatud lähtekoodiga projektidega. Selle asemel, et otsida läbi mitme platvormi või tugineda mitteametlikest allikatest pärit potentsiaalselt vananenud teabele, saavad kasutajad usaldada Bitaxe.org-i, et see pakub ajakohaseid ja kontrollitud linke kõigile olulistele allikatele. Selline lähenemine tagab, et nii uustulnukad kui ka kogenud kogukonnaliikmed saavad tõhusalt leida oma projektide jaoks vajalikku teavet.


### Tehnilised ressursid ja arendusmaterjalid


GitHubis asuv riistvara disainifailide repositoorium on üks kõige väärtuslikumaid ressursse kõigile, kes on huvitatud Bitaxe'i seadmete mõistmisest või ehitamisest. See avalik repositoorium sisaldab põhjalikku dokumentatsiooni, mis hõlmab kõiki riistvara projekteerimisprotsessi aspekte, alates esialgsetest kontseptsioonidest kuni lõplike tootmisspetsifikaatideni. Repositoorium sisaldab üksikasjalikke pilte, projekti eesmärke, funktsioonide kirjeldusi ja sisseehitatud komponentide selgitusi, mis pakuvad nii tehnilist sügavust kui ka praktilisi juhiseid.


Neile, kes on huvitatud oma seadmete valmistamisest, sisaldab repositoorium konkreetseid dokumentatsioonifaile, nagu näiteks building.md, mis annab samm-sammult juhiseid kogu tootmisprotsessi kohta. See dokumentatsioon hõlmab trükkplaatide projekteerimiseks vajalikke tarkvaravahendeid, failide tootjatele saatmise korda ning valmistatud trükkplaatide vastuvõtu ja valideerimise samme. Selline üksikasjalikkus tagab, et üksikisikud või väikesed organisatsioonid saavad tootmisprotsessis edukalt navigeerida ilma ulatusliku eelneva kogemuseta riistvara tootmises.


ESP-Miner repositoorium on kogu firmavaraga seotud koodi ja dokumentatsiooni keskne asukoht. See GitHubi repositoorium sisaldab kõiki Bitaxe'i püsivara jaoks kirjutatud koodiridu koos põhjaliku dokumentatsiooniga, mis selgitab süsteeminõudeid, riistvara spetsifikatsioone ja konfiguratsioonivõimalusi. Repositooriumi struktuur on loodud nii kasutajatele, kes eelistavad eelkompileeritud binaarfaile, kui ka arendajatele, kes soovivad püsivara lähtekoodist koostada.


Selle repositooriumi dokumentatsioon sisaldab üksikasjalikke jaotisi riistvaranõuete, eelkonfigureerimise võimaluste ja erinevate seadete soovituslike väärtuste kohta. See teave osutub hindamatuks kasutajatele, kes soovivad oma seadmeid kohandada või lahendada konkreetseid probleeme. Lisaks sisaldab repositoorium teavet uuemate arengute kohta, näiteks Raspberry Pi integreerimise kohta, tagades, et dokumentatsioon jääb projekti käimasoleva arenguga samale tasemele.


### Seadme haldus- ja hooldusvahendid


Bitaxe'i veebiplahvatusprogramm on praktiline lahendus seadme hoolduseks ja uuendamiseks. See veebipõhine tööriist võimaldab kasutajatel oma seadmetesse püsivara flashida ilma spetsiaalse tarkvara või keeruliste käsurea protseduurideta. Flasher toetab mitut seadmevarianti, sealhulgas Bitaxe Ultra erinevate portversioonidega ja vanemaid Bitaxe Maxi mudeleid. Kasutajad saavad valida, kas uuendada olemasolevat püsivara veebiliidese kaudu või teostada USB-ühenduste abil täielikku tehasepuhastust.


See tööriist tegeleb ühe kõige tavalisema probleemiga, millega riistvarahuvilised silmitsi seisavad: seadme püsivara hooldamine ja uuendamine. Kasutajasõbraliku veebiliidese abil kõrvaldab see väljalülitusprogramm paljud tehnilised takistused, mis muidu takistaksid kasutajatel oma seadmeid viimaste püsivara versioonidega ajakohasena hoida. Tööriista disainis on esikohal lihtsus, säilitades samas paindlikkuse, mis on vajalik erinevate seadmekonfiguratsioonide ja uuendamisstsenaariumide jaoks.


### Ühenduse platvormid ja sidekanalid


Discordi server on Bitaxe'i ökosüsteemi reaalajas toimuva kogukonna suhtluse ja toetuse süda. Serveri korraldus peegeldab kogukonnaliikmete erinevaid huve ja vajadusi, kusjuures hoolikalt struktureeritud kanalid hõlbustavad konkreetsete teemade üle peetavaid arutelusid. Uued liikmed puutuvad kokku kontrolliprotsessiga, mis nõuab kogukonna reeglite lugemist ja aktsepteerimist, tagades, et kõik osalejad mõistavad lugupidava ja produktiivse suhtluse ootusi.


Serveri kanali struktuur sisaldab üldisi arutelualasid, mis hõlmavad selliseid teemasid nagu päikeseenergia integreerimine, mining basseinid ja Bitcoin-ga seotud arutelud. Spetsiifilisemad sektsioonid keskenduvad konkreetsetele seadmetele, sealhulgas spetsiaalsed kanalid Bitaxe Ultra, Hex ja Supra variantidele. Firmware-kanal pakub keskendunud ruumi tarkvaraarenduse ja tõrkeotsingu tehniliste arutelude jaoks, samas kui ametlike väljaannete kanal tagab, et kogukonna liikmed saavad õigeaegselt teateid uute arengute kohta.


Samuti on seal olemas tellija ala, mis pakub lisahüvesid kogukonna liikmetele, kes otsustavad projekti rahaliselt toetada. Selline mitmetasandiline lähenemisviis võimaldab kogukonnal pakkuda täiustatud teenuseid, säilitades samal ajal avatud juurdepääsu olulisele teabele ja toetuskanalitele. Abikanal on spetsiaalne ruum tõrkeotsingu ja tehnilise abi jaoks, mis tagab, et kasutajad saavad probleemide korral kiiret tuge.



Open Source Miners Unitedi wiki (osmu.wiki) pakub põhjalikku dokumentatsiooni, mis täiendab Discordis toimuvaid reaalajas toimuvaid arutelusid. Erinevalt chat-põhistest platvormidest pakub wiki struktureeritud, otsitavat dokumentatsiooni, mis hõlmab kõiki Bitaxe'i projekti ja sellega seotud algatusi. Selle ülesehitus peegeldab projekti struktuuri, kus on eri seadmesarjadele pühendatud jaotised ja põhjalikud seadistusjuhendid.


Wiki avatud lähtekoodiga olemus võimaldab kogukonna liikmetel otse dokumentatsiooni panustada. Kasutajad saavad GitHubi integratsiooni kaudu muuta lehekülgi, esitada parandusi ja lisada uut teavet, tagades, et teadmistebaas jääb ajakohaseks ja läbipaistvaks. Selline koostööl põhinev lähenemisviis kasutab kogukonna kollektiivseid teadmisi, säilitades samal ajal kvaliteedikontrolli esitatud muudatuste läbivaatamisprotsessi kaudu.


Wiki sisaldab praktilisi ressursse, näiteks PDF-seadistusjuhendeid, mis annavad samm-sammult juhiseid seadme konfigureerimiseks ja kasutamiseks. Need juhendid on väärtuslikud viited nii uutele kasutajatele kui ka kogenud kogukonna liikmetele, kes vajavad kiiret juurdepääsu konkreetsetele protseduuridele või konfiguratsiooni üksikasjadele.


### Ostu ja müüja teave


Bitaxe legitiimne nimekiri on avatud lähtekoodiga riistvarakogukonna kriitilise tähtsusega vajadus: usaldusväärsete müüjate tuvastamine ja petturlike müüjate vältimine. See kureeritud nimekiri sisaldab kontrollitud edasimüüjaid ja tootjaid, kes vastavad kindlatele legitiimsuse ja kogukonna toetuse kriteeriumidele. Iga loetelu sisaldab otselinki müüja veebisaitidele, piirkondlikku teavet ja ettevõtte kirjeldusi, mis aitavad kasutajatel teha teadlikke ostuotsuseid.


Oluline on see, et nimekirjas on märgitud, kas iga müüja toetab OSMU kogukonda rahaliselt või muul viisil. Selline läbipaistvus aitab kogukonna liikmetel mõista, millised müüjad toetavad aktiivselt projekti arengut ja jätkusuutlikkust. Nimekiri on ka kaitsemeetmeks levinud pettuste, näiteks välja andmata toodete volitamata eeltellimuste vastu, mis on kogukonnas varem probleeme tekitanud.


Rõhuasetus mitteseotud linkidele näitab kogukonna pühendumust pakkuda erapooletuid müüja soovitusi. Kasutajad võivad usaldada, et soovitused põhinevad pigem müüja legitiimsusel ja kogukonna panusel kui rahalistel stiimulitel, mis tagab, et ostuotsused toetavad nii individuaalseid vajadusi kui ka kogukonna jätkusuutlikkust.



# Tarkvara ja operatsioonid

<partId>04b302a9-42ba-5ad4-834c-6979950c2948</partId>


## Mis on AxeOS?

<chapterId>a0cdf10d-e007-58e2-a17b-b588fd393b5e</chapterId>

:::video id=de7bcbf2-f9ac-4057-ad40-29dc223b4798:::

AxeOS on Bitaxe mining seadmetele mõeldud püsivara- ja veebiliides, mis pakub kasutajatele täielikku kontrolli ja jälgimise võimalust intuitiivse brauseripõhise armatuurlaua kaudu. See süsteem muudab ASIC haldamise keerulise ülesande hõlpsasti kasutatavaks, võimaldades kaevuritele jälgida jõudlust, kohandada seadeid ja hallata mitut seadet ühest kasutajaliidesest. AxeOSi mõistmine on oluline, et maksimeerida oma Bitaxe'i seadme potentsiaali ja säilitada optimaalne mining toimimine.


### Armatuurlaua ülevaade ja põhinäitajad


AxeOSi armatuurlaud on teie esmane aken Bitaxe'i seadme jõudlusele, esitades kriitilised mining mõõdikud organiseeritud ja reaalajas vormingus. Kui navigeerite oma Bitaxe'i seadme IP-aadressile, kuvatakse teile kohe neli peamist tulemusnäitajat, mis määratlevad teie mining operatsiooni hetkeseisu. Hash-kiiruse kuva näitab tegelikku arvutuskiirust, mida teie ASIC kiip praegust plokkmalli töötleb, andes vahetut tagasisidet teie seadme põhifunktsionaalsuse kohta.


Hashimiskiiruse kõrval jälgib aktsiate loendur iga kehtivat lahendust, mille teie Bitaxe'i seade mining-poolsesse esitab, suurendades seda iga eduka esitamisega ja olles otsene näitaja teie seadme panuse kohta mining-poolsete jõupingutuste tegemisel. Tõhususe mõõdik annab olulise ülevaate teie seadme energiatarbimisest, arvutades hash-kiiruse ja energiatarbimise suhte, mis aitab teil optimeerida oma tegevuse kasumlikkust. Parima raskusastme näitaja säilitab teie seadme kõrgeima raskusastme osakaalu, säilitades selle saavutuse isegi taaskäivituste ja värskenduste ajal ning nullides selle ainult siis, kui te teostate täieliku tehase väljalülituse.


Armatuurlaua laiendatav menüüsüsteem, mida juhitakse lülitusnupuga, võimaldab juurdepääsu kõikidele AxeOSi funktsioonidele, säilitades samas puhta kasutajaliidese. Üks selle kõige väärtuslikumaid funktsioone on live-hash-kiiruse graafik, mis näitab reaalajas toimimisandmeid, mis muutuvad seda täpsemaks ja informatiivsemaks, mida kauem te oma seanssi säilitate. Toite-, soojuse- ja jõudluse sektsioonid pakuvad teie seadme tööseisundi põhjalikku jälgimist, sealhulgas sisendpinge hoiatusi, mis hoiatavad teid võimalike toiteallikaga seotud probleemide eest, tagades samal ajal jätkuva töö ohutute parameetrite piires.


### Täiustatud seire ja süsteemiteave


AxeOSi seirevõimalused ulatuvad kaugemale põhilisest hash-kiiruse jälgimisest, andes üksikasjaliku ülevaate teie Bitaxe'i seadme toimimise igast aspektist. Toiteosa kuvab arvutuslikku energiatarbimist, mis on saadud integreeritud vooluahelatest, sisendpinge mõõtmisi teie toiteallika ühendusest ja soovitud ASIC pingetasemeid. Pinge languse korral esitab AxeOS kohe hoiatusteated, kuigi need tavaliselt ei mõjuta mining toimimist ja näitavad lihtsalt võimalikke toiteallika optimeerimise võimalusi.


Temperatuuri jälgimine keskendub ASIC kiibi soojusjuhtimisele, kusjuures mõõtmistulemused võetakse seadme strateegilistest kohtadest, et anda täpseid soojusandmeid koos sobivate nihetega kiibitasandi täpsuse tagamiseks. Sageduse ja pinge näidikud pakuvad reaalajas tagasisidet ASIC häälestusparameetrite kohta, kusjuures mõõdetud pinge kujutab endast kõige täpsemat kättesaadavat näitu, mis on võetud otse ASIC kiibi asukohast. Selline täpsus võimaldab jõudlusparameetrite peenhäälestamist, säilitades samal ajal ohutud töötingimused.


Ühenduse oleku sektsioon annab vahetu ülevaate mining basseini konfiguratsioonist, näidates praeguse kihi URL-i, pordi ja kasutaja identifikaatori. Avalike basseinidega ühendatud seadmete puhul genereerib AxeOS mugavad kiirlinkid, mis viivad teid otse teie basseini veebiliidesesse, kus saate juurdepääsu üksikasjalikule statistikale, seadmete nimekirjadele ja varasematele tulemuslikkuse andmetele. See integratsioon lihtsustab seireprotsessi, ühendades seadme- ja basseinitasandi teabe sujuvaks töövooks.


### Parve haldamine ja mitme seadme juhtimine


Swarm-funktsioon kujutab endast AxeOSi lahendust mitme Bitaxe'i seadme haldamise keerukusele kogu võrgus, kõrvaldades vajaduse mäletada ja navigeerida arvukatele IP-aadressidele. See tsentraliseeritud haldussüsteem võimaldab teil lisada seadmeid, sisestades lihtsalt nende IP-aadressid, tuvastab automaatselt aktiivsed Bitaxe'i kaevandajad ja lisab need ühtsele juhtimisplaadile. Pärast seadistamist pakub Swarm terviklikku kontrolli kogu teie mining operatsiooni üle ühest kasutajaliidesest.


Parve kasutajaliidese kaudu saate täita kriitilisi haldusülesandeid mitme seadme puhul samaaegselt või üksikult, sealhulgas muuta basseinide konfiguratsiooni, taaskäivitada seadmeid, kohandada sagedust ja jälgida jõudlust. Selline tsentraliseeritud lähenemisviis vähendab märkimisväärselt suurte mining operatsioonide haldamisega seotud halduskulusid, tagades samal ajal kõigi seadmete järjepideva konfiguratsiooni. Süsteem säilitab individuaalse seadme identiteedi, pakkudes samal ajal kollektiivseid haldusvõimalusi, saavutades optimaalse tasakaalu granulaarse kontrolli ja tegevuse tõhususe vahel.


Swarmi armatuurlaual esitatakse iga hallatava seadme praegune olek, jõudlusnäitajad ja kiire ligipääsuga kontroll, mis võimaldab kiiret reageerimist jõudlusprobleemidele või konfiguratsioonimuudatustele. See funktsioon on eriti väärtuslik kaevurite jaoks, kes kasutavad mitut seadet erinevates asukohtades või kes sageli kohandavad mining parameetreid vastavalt turutingimustele või basseinide tulemuslikkusele.


### Konfiguratsiooni haldamine ja süsteemi seaded


AxeOSi seadete sektsioon pakub põhjalikku kontrolli Bitaxe'i seadme iga seadistatava aspekti üle, alates võrguühendusest kuni mining parameetrite ja riistvara optimeerimiseni. Võrgu konfigureerimine algab Wi-Fi seadistamisega, kus te määrate oma võrgu nime ja parooli, kusjuures AxeOS soovitab usaldusväärse ühenduvuse tagamiseks ühe sõnaga, ilma tühikuteta võrgu nimesid. Süsteem tegeleb kogu traadita võrgu konfigureerimisprotsessiga, võimaldades kaugjuhtimise ja jälgimise võimalusi.


Mining konfigureerimise keskmes on kihi seaded, kus te määrate valitud mining basseini URL-i ilma protokollide eesliite või portide numbriteta, mida käsitletakse eraldi väljadel. Stratum kasutaja väli vastab erinevatele basseinõuetele, toetades nii Bitcoin aadresse soolo mining jaoks kui ka kasutajanimede süsteeme basseini mining jaoks, kusjuures mitme seadme operatsioonide jaoks on võimalik lisada seadme identifikaatorid. Hiljuti lisatud stratum password funktsioon toetab autentimist nõudvaid basseinid, kuigi enamik avalikke basseinid töötavad ilma selle nõudeta.


Riistvara optimeerimine sageduse ja tuumapinge reguleerimise kaudu on AxeOSi kõige võimsam jõudluse häälestamise võimalus. Sõltuvalt seadme versioonist ja brauserist võivad need seaded ilmuda rippmenüüdena koos eelseadistatud konfiguratsioonidega või avatud väljadena, mis võimaldavad kohandatud väärtusi. Vaikimisi seaded 485 MHz sagedus ja 1200 mV tuumapinge tagavad stabiilse töö esialgsete testide jaoks, samas kui edasijõudnud kasutajad saavad neid parameetreid optimeerida maksimaalse jõudluse või tõhususe saavutamiseks vastavalt oma konkreetsetele nõuetele ja töötingimustele.


### Süsteemi hooldus ja täiustatud funktsioonid


AxeOS sisaldab keerukaid süsteemi hooldusvõimalusi, mis on loodud selleks, et hoida teie Bitaxe'i seade töötama tipptasemel, pakkudes samal ajal diagnostilist teavet tõrkeotsingu ja optimeerimise jaoks. Värskendussüsteem lihtsustab püsivara haldamist, kuvades uusima saadaval oleva versiooni otse kasutajaliideses ja pakkudes otselinkide allalaadimist ametlikele püsivara failidele. See integratsioon välistab vajaduse käsitsi GitHubi hoidlates navigeerida või failide allalaadimist hallata, lihtsustades uuendamisprotsessi mõne klikiga.


Uuendusliides aktsepteerib õigesti nimetatud püsivara faile, täpsemalt esp-miner.bin ja www.bin, tagades ühilduvuse ja vältides paigaldusvigu. Kasutajatele, kellel on raskusi standardse uuendamisprotsessiga, pakub AxeOS viiteid põhjalikele tehase flash-protseduuridele, millega saab taastada seadmete algse funktsionaalsuse. See kahekordne lähenemisviis sobib nii tavapäraste uuenduste kui ka taastamisstsenaariumide jaoks.


Logisüsteem annab reaalajas ülevaate seadme toimimisest, kuvades üksikasjalikku teavet ASIC kiibimudelite, süsteemi tööaja, Wi-Fi ühenduvuse oleku, olemasoleva mälu, püsivara versioonide ja plaadi versioonide kohta. Need logid on hindamatu väärtusega arendajatele ja edasijõudnud kasutajatele, kes soovivad mõista seadme käitumist, diagnoosida probleeme või optimeerida jõudlust. Reaalajas logide vaataja esitab reaalajas tööandmeid, sealhulgas [nonce'i](https://planb.academy/resources/glossary/nonce) töötlemist, raskusarvutusi ja mining esitamise parameetreid, pakkudes enneolematut ülevaadet mining protsessist endast.


Süsteemi lisafunktsioonide hulka kuuluvad ekraani orientatsiooni juhtimine seadmetele, mida kasutatakse kohandatud korpustes, ventilaatori polaarsuse ümberpööramine spetsiaalsete jahutuskonfiguratsioonide jaoks ja automaatne ventilaatori juhtimine, mis reguleerib jahutust vastavalt ASIC temperatuurile. Ventilaatori kiiruse käsitsi juhtimine tagab täpse jahutuse juhtimise, kui automaatsed süsteemid ei vasta konkreetsetele nõuetele. Kõik konfiguratsioonimuudatused vajavad jõustumiseks salvestamist ja seadme taaskäivitamist, mis tagab stabiilse töö ja hoiab ära osalised konfiguratsiooniseisundid, mis võivad mõjutada mining jõudlust.



# Ühendus ja koostöö

<partId>eed1ce48-6752-5744-91f7-91e4e20ff6b2</partId>


## Avatud lähtekoodiga panuse ülevaade

<chapterId>715d026e-cebc-536e-a34e-728f5653b999</chapterId>

:::video id=7298ba19-28d2-4a7c-ac0b-44ad0c4770cf:::

### GitHub ja selle roll tarkvaraarenduses


GitHub kujutab endast põhimõttelist muutust selles, kuidas tarkvaraarendusprojekte hallatakse ja jagatakse üleilmses programmeerimiskogukonnas. GitHub on pilvepõhine platvorm, kus tarkvaraarendusprojektid toimuvad jaotatud versioonihaldussüsteemi Git abil, mis võimaldab arendajatel teha projektides sujuvalt koostööd, sõltumata nende füüsilisest asukohast. Platvorm on programmeerijatele nii tehniline vahend kui ka sotsiaalne võrgustik, mis võimaldab neil jälgida muudatusi, ühendada uuendusi, säilitada oma koodi erinevaid versioone ja aidata kaasa avatud lähtekoodiga algatustele, nagu Open Source Miners Unitedi BitX projekt.


GitHubi võimsus seisneb tema võimekuses lihtsustada keerulist ühisarendusprotsessi. Kui mitu arendajat töötab ühe ja sama projekti kallal, pakub GitHub infrastruktuuri, et hallata panust, vaadata muudatusi, käsitleda projekti probleeme ja säilitada põhjalikku dokumentatsiooni. Selline koostööpõhine lähenemine on muutnud GitHubi kaasaegse tarkvaraarenduse töövoogude oluliseks osaks, muutes nii üksikute arendajate kui ka suurte organisatsioonide lähenemisviisi projektijuhtimisele ja koodijagamisele.


### GitHub Interface ja repositooriumi struktuuris navigeerimine


GitHubi kasutajaliidese mõistmine algab iga repositooriumi lehe põhielementide äratundmisest. Ülemine navigatsiooniriba sisaldab mitmeid olulisi jaotisi, sealhulgas Code, Issues, Pull Requests, Discussions, Actions, Projects, Security ja Insights. Iga sektsioon täidab projektijuhtimise ökosüsteemis konkreetset eesmärki, kusjuures sektsioonis Code kuvatakse tegelikud failid ja kaustad, millest projekt koosneb.


Repositooriumi struktuur ise peegeldab projekti hooldajate organisatsioonilist lähenemist. Mõned repositooriumid sisaldavad vaid ühte faili, võib-olla lihtsat shell-skripti, samas kui teised, nagu BitXi riistvaraprojekt, sisaldavad arvukalt faile, mis on organiseeritud kataloogidesse ja alamkataloogidesse. Hoidla nimi on silmapaistvalt nähtav ja see on nii identifikaator kui ka projekti eesmärgi lühikirjeldus. Oluliste interaktiivsete elementide hulka kuuluvad nupp Watch, millega saab teateid repositooriumi uuenduste kohta, nupp Fork, millega saab luua isiklikke koopiaid repositooriumist, ja nupp Star, mis toimib kogukonna toetussüsteemina, mis sarnaneb "pöidlaid üles" funktsiooniga.


Jaotises "Teave" on esitatud oluline teave projekti kohta lühendatud kujul, sealhulgas ühe rea kirjeldus, litsentsimisandmed ja projekti peamised üksikasjad. BitX-projekti puhul määratletakse see jaotises kui "avatud lähtekoodiga ASIC Bitcoin kaevandaja riistvara" ja täpsustatakse GPL 3.0 litsentsi. Litsentside mõistmine on eriti oluline, sest GitHub toimib avatud lähtekoodiga platvormina, kus avalikud hoidlad on kättesaadavad kogu kogukonnale, kuid sisu saab kasutada ja levitada ainult vastavalt iga litsentsi vastavuse eeskirjadele.


### Töö harude ja projekti versioonidega


Filiaalide kontseptsioon on üks GitHubi kõige võimsamaid funktsioone erinevate versioonide ja arenguradade haldamiseks ühe projekti raames. Haru loob sisuliselt peamise koodibaasi koopia või muudetud versiooni, mis võimaldab arendajatel töötada konkreetsete funktsioonide, veaparanduste või eksperimentaalsete muudatuste kallal, ilma et see mõjutaks peamist arendusliini. Põhiharu on tavaliselt projekti vaikimisi ja kõige stabiilsem versioon, samal ajal kui lisaharud sobivad erinevate iteratsioonide, testimisfaaside või täiesti erinevate tootevariantide jaoks.


BitXi riistvaraprojektis on olemas mitu haru, et hallata erinevaid riistvaraversioone ja -konfiguratsioone. Näiteks Ultra v2 haru sisaldab selle riistvara iteratsiooni jaoks spetsiifilisi faile, samas kui Super 401 haru keskendub rakendustele, mis kasutavad S21 ASIC kiipi tõhususe parandamiseks. Iga haru võib olla mitu kommitsiooni enne või pärast põhiharu, mis näitab muudatuste ja arendustegevuse ulatust. Erinevaid harusid uurides märkavad kasutajad täiesti erinevaid failistruktuure, dokumentatsiooni ja isegi visuaalseid esitlusi, mis peegeldavad iga riistvaravariandi unikaalseid nõudeid ja spetsifikatsioone.


Harude süsteem väldib segadust kaastöötajate ja kasutajate vahel, kuna see eristab selgelt erinevad arendusrajad. Selle asemel, et segada eksperimentaalseid funktsioone stabiilsete versioonidega või kombineerida erinevaid riistvaraversioone ühes kohas, tagavad harud puhta eraldatuse, säilitades samal ajal võimaluse edukate muudatuste ühendamiseks tagasi peamisesse arendusliini, kui see on asjakohane. Selline organisatsiooniline lähenemine tagab, et kasutajad saavad hõlpsasti leida konkreetse versiooni, mida nad vajavad, samal ajal kui arendajad saavad töötada paranduste kallal ilma põhiprojekti häirimata.


### Panustamine läbi probleemide


Probleemide sektsioon on peamine suhtluskanal kasutajate ja projekti hooldajate vahel probleemidest teatamiseks, parandusettepanekute tegemiseks ja vigade dokumenteerimiseks. Siiski on oluline mõista, et probleemide sektsioon on mõeldud pigem õigustatud tehniliste probleemide lahendamiseks kui üldiste küsimuste või toetustaotluste esitamiseks. Kui kasutajad kogevad tegelikke tõrkeid, ootamatut käitumist või tuvastavad võimalikke parandusi, aitab hästi dokumenteeritud probleemi loomine kogu kogukonda, kuna see juhib tähelepanu probleemidele, mis võivad mõjutada paljusid kasutajaid.


Tõhus probleemidest teatamine eeldab probleemi üksikasjalikku dokumenteerimist, sealhulgas probleemi tekkimise asjaolusid, probleemi taastamise samme ja kõiki asjakohaseid tehnilisi üksikasju. Projekt BitX demonstreerib seda põhimõtet erinevate suletud probleemide kaudu, mis näitavad lahendamise protsessi alates probleemi esialgsest tuvastamisest kogukonna arutelude kaudu kuni lõpliku lahenduseni. Mõne probleemi tulemuseks on riistvara parandamine, näiteks paigaldusavade lisamine jahutusvõimaluste suurendamiseks, samas kui teised probleemid lahendatakse kasutajate koolitamise või tarkvara uuendamise abil.


Probleemide ja arutelude eristamine on oluline kogukonna organiseeritud suhtluse säilitamiseks. Kui teemad keskenduvad konkreetsetele tehnilistele probleemidele, siis arutelude rubriik pakub foorumilaadset keskkonda küsimuste, ideede ja üldise kogukonna kaasamise jaoks. Ehkki Discordi serverist on saanud BitXi kogukonna peamine suhtluskanal, on GitHubi jaotis "Arutelud" endiselt kättesaadav ametlikumate või otsitavate vestluste jaoks, mis saavad kasu pidevast dokumentatsioonist ja lihtsast viitamisest.


### Pull Requesti mõistmine


Pull-päringud on mehhanism, mille kaudu välised toetajad teevad ettepanekuid projekti repositooriumi muutmiseks. Kui keegi tuvastab paranduse, veaparanduse või uue funktsiooni, mis oleks projektile kasulik, saab ta luua tõmbetaotluse, et esitada oma muudatused läbivaatamiseks ja võimalikuks integreerimiseks põhikoodibaasi. See protsess tagab, et kõik muudatused vaadatakse enne ametliku projekti osaks saamist läbi, säilitades koodi kvaliteedi ja projekti sidususe ning võimaldades samal ajal kogukonna panust.


Tööprotsess algab tavaliselt siis, kui toetaja jagab repositooriumi, loob oma koopia, kus ta saab teha muudatusi, ja seejärel esitab need muudatused algsesse projekti tagasi tõmbetaotluse kaudu. Projekti hooldajad saavad seejärel kavandatud muudatused läbi vaadata, arutada muudatusi kaasajaga ja lõpuks otsustada, kas muudatused liita põhiprojekti. Selline ühine läbivaatamisprotsess aitab säilitada projekti standardeid, julgustades samal ajal kogukonna osalemist ja täiustamist.


Siltide ja versioonide mõistmine lisab projektijuhtimisele ja versioonikontrollile veel ühe tasandi. Sildid toimivad arenduse ajajoonel markeritena, mis tähistavad konkreetseid punkte, mis esindavad konkreetseid versioone või verstaposte. Riistvaraprojektides, nagu BitX, vastavad sildid sageli konkreetsetele mudelinumbritele või riistvara versioonidele, pakkudes kasutajatele, kes otsivad konkreetseid versioone, selgeid võrdluspunkte. Tarkvaraprojektides sagedamini kasutatavad versioonid kujutavad endast lõpetatud funktsioonide ja veaparanduste ametlikku levitamist, millega sageli kaasnevad üksikasjalikud märkused ja allalaaditavad paketid.


GitHubi ökosüsteem loob tervikliku keskkonna avatud lähtekoodiga koostööks, mis ulatub kaugemale lihtsast failide jagamisest. Nende erinevate komponentide ja nende nõuetekohase kasutamise mõistmisega saavad kaasajad tõhusalt osaleda projektides, aidata parandada tarkvara ja riistvara projekte ning saada kasu globaalse arenduskogukonna kollektiivsetest teadmistest ja jõupingutustest. GitHub pakub vahendeid ja struktuuri, mis on vajalikud sisuliseks koostööks avatud lähtekoodiga maailmas, olenemata sellest, kas tegemist on probleemidest teatamise, parendusettepanekute tegemise või koodiga.


## Avatud lähtekoodiga panus Praktiline panus

<chapterId>84d033f5-7182-584f-b1a5-697172bc7a1c</chapterId>

:::video id=7d318fd0-6f0b-422a-9f30-2c470b56951d:::

Tuginedes probleemide loomise ja avatud lähtekoodiga projektide uurimise alusele, keskendutakse selles peatükis otsese panuse andmise praktilistele aspektidele tõmbetaotluste ja repositooriumi haldamise kaudu. fork repositooriumide mõistmine, muudatuste tegemine ja tõmbetaotluste esitamine on oluline oskus iga arendaja jaoks, kes soovib anda olulist panust avatud lähtekoodiga projektidesse, olgu need siis seotud tarkvaraarenduse või riistvara disainiga.


Koodimuudatuste sisseviimise protsess järgib standardiseeritud töövoogu, mis tagab projekti terviklikkuse, võimaldades samal ajal ühist arendamist. See töövoog hõlmab projekti repositooriumi oma koopia loomist, muudatuste tegemist kontrollitud keskkonnas ja seejärel nende muudatuste esitamist tagasi algsesse projekti ametliku läbivaatamisprotsessi kaudu. Kuigi käesolevas peatükis toodud näited keskenduvad peamiselt tarkvarale, kehtivad samad põhimõtted ja protseduurid võrdselt ka riistvaraprojektide puhul, mis hõlmavad trükkplaadi projekte, skeeme ja muud tehnilist dokumentatsiooni.


### Kahvlite ja repositooriumi struktuuri mõistmine


Mis tahes avatud lähtekoodiga projekti panustamine algab fork loomisega, mis on teie isiklik koopia algsest repositooriumist. Kui navigeerite GitHubi repositooriumi ja vajutate nupule "fork", loote oma GitHubi konto all sõltumatu koopia, mis säilitab selge ühenduse algallika allikaga. See forkeeritud repositoorium ilmub teie kontol selge märkega selle päritolu kohta, kuvades repositooriumi pealkirja all teksti nagu "forked from [original-owner]/[repository-name]".


Teie forkeeritud repositoorium toimib originaalist sõltumatult, võimaldades teil teha muudatusi, ilma et see mõjutaks põhiprojekti. Siiski säilitab see GitHubi sünkroonimisfunktsioonide kaudu teadlikkuse algse repositooriumi uuendustest. Kui algne repositoorium saab uuendusi, mis teie fork puudub, kuvab GitHub staatusteavet, näiteks "See haru on X kommitsiooni taga" või "X kommitsiooni ees", andes selget ülevaadet teie fork ja eelrepositooriumi vahelisest suhtest. Saate oma fork algse repositooriumiga igal ajal sünkroonida, klõpsates nuppu "Sync fork", mis tõmbab sisse viimased muudatused eelkasutatavast allikast.


Suhe teie fork ja algse repositooriumi vahel muutub eriti oluliseks siis, kui hakkate muudatusi tegema. Kui te rakendate muudatusi ja kinnitate need oma fork-sse, jälgib GitHub neid erinevusi ja kuvab need algsele repositooriumile eelnevate kommititena. See jälgimissüsteem võimaldab pull request'i protsessi, kus saate esitada oma muudatusi põhiprojekti lisamiseks, säilitades samal ajal selge ajaloo selle kohta, mida on muudetud.


### Arenduskeskkonna seadistamine


Tõhusa arenduskeskkonna loomine nõuab hoolikat tähelepanu nii üldistele arendusvahenditele kui ka projektispetsiifilistele nõuetele. Visual Studio Code on suurepärane integreeritud arenduskeskkond (IDE) enamiku avatud lähtekoodiga projektide jaoks, pakkudes olulisi funktsioone koodi redigeerimiseks, versioonihalduse integreerimiseks ja projektijuhtimiseks. Esimene kriitiline komponent hõlmab Git laienduse installimist ja konfigureerimist, mis võimaldab sujuvat integreerimist GitHubi repositooriumidega otse teie arenduskeskkonnast.


Visual Studio Code'i kaasaegsed versioonid sisaldavad tavaliselt vaikimisi Git-tuge, kuid täieliku funktsionaalsuse võimaldamiseks peate autentima oma GitHubi kontoga. See autentimisprotsess hõlmab GitHubi sisselogimist IDE kaudu, mis võimaldab teil seejärel kloonida repositooriume, teha muudatusi ja lükata uuendusi otse oma arenduskeskkonnast. GitHubi integratsioon ilmub ikoonina vasakul külgribal, pakkudes juurdepääsu repositooriumide kloonimise, harude haldamise ja sünkroniseerimise funktsioonidele, ilma et selleks oleks vaja käsurea toiminguid.


Manussüsteemide või spetsiifiliste riistvaraplatvormidega seotud projektide puhul on vaja lisavahendeid. ESP-IDF laiendus on ESP32 mikrokontrolleritele suunatud projektide jaoks oluline komponent, mis vajab nõuetekohase funktsionaalsuse tagamiseks konkreetsete versioonide ühilduvust. Paigaldusprotsess hõlmab sobiva ESP-IDF-i versiooni valimist, tööriistaradade konfigureerimist ja arenduskonteineri keskkonna seadistamist. Versioon 5.1.3 on praegu paljude ESP32-põhiste projektide jaoks soovitatav konfiguratsioon, kuigi need nõuded võivad muutuda, kui projektid uuendavad oma sõltuvusi ja tööriistakomplekte.


### Muudatuste tegemine ja kommitite haldamine


Kui teie arenduskeskkond on õigesti konfigureeritud, algab sisuline panustamine sellega, et laadite alla või kloonite oma kahveldatud repositooriumi oma kohalikku masinasse. Seda saab teha kas repositooriumi sisu sisaldava ZIP-faili allalaadimisega või kasutades Visual Studio Code'i integreeritud kloonimisfunktsiooni, mis pakub sujuvamat töövoogu pidevaks arenduseks. Kloonimisprotsess loob teie repositooriumi lokaalse koopia, mis jääb sünkroniseerituks teie GitHub fork-ga, võimaldades teil töötada võrguühenduseta, säilitades samal ajal versioonihalduse võimalused.


Kui töötate kohaliku repositooriumiga, saate juurdepääsu kogu projekti struktuurile, sealhulgas lähtekoodifailidele, konfiguratsioonifailidele, dokumentatsioonile ja kõigile riistvara projekteerimisfailidele. Enamik püsivara projekte kasutab põhifunktsioonide jaoks programmeerimiskeeli, näiteks C, ning lisakomponente, mis on kirjutatud TypeScriptis kasutajaliideste jaoks või Java keeles konkreetsete utiliitide jaoks. Projekti struktuuri mõistmine aitab teil tuvastada sobivad failid, mida muuta, ja tagab, et teie muudatused on kooskõlas projekti arhitektuurimustrite ja kodeerimisstandarditega.


Kinnitusprotsess on versioonihalduse põhiline aspekt, mis nõuab hoolikat tähelepanu nii tehnilisele täpsusele kui ka kommunikatsiooni selgusele. Enne muudatuste tegemist peaksite olemasolevast koodist põhjalikult aru saama ja testima kõiki muudatusi oma kohalikus keskkonnas. Avatud lähtekoodi panustamise põhireegel rõhutab, et kunagi ei tohi avaldada testimata koodi, sest see võib tuua sisse vigu või turvaauke, mis mõjutavad kogu projekti kogukonda. Lisaks sellele ei tohi te kunagi avalikesse repositooriumidesse panna tundlikku teavet, nagu paroolid, API-tokendid või isiklikud volitused, sest see teave muutub püsivalt kättesaadavaks kõigile, kellel on juurdepääs repositooriumile.


### Pull Requesti loomine ja haldamine


Teie panuse kulminatsiooniks on pull request, mis on ametlik ettepanek teie muudatuste ühendamiseks projekti algsesse repositooriumi. See protsess algab teie GitHubi fork-s, kus saate vaadata erinevusi teie repositooriumi ja eelneva lähtekoodi vahel. GitHubi kasutajaliides näitab selgelt, kui palju kommenteeringuid on ees või taga, mis annab kohese ülevaate teie pakutud muudatuste ulatusest. Enne tõmbetaotluse loomist peaksite tagama, et teie fork on sünkroonitud viimaste eelkasutatavate muudatustega, et vähendada võimalikke konflikte.


Tõhusa tõmbetaotluse loomine nõuab enamat kui lihtsalt oma koodimuudatuste esitamine. Tõmbetaotluse kirjeldus on teie võimalus edastada projekti hooldajatele ja kogukonnale teie muudatuste eesmärk, ulatus ja mõju. Hästi kirjutatud kirjeldus selgitab, milliseid probleeme teie muudatused lahendavad, kuidas te lahenduse rakendasite ja millised on võimalikud mõjud projekti teistele osadele. See dokumentatsioon muutub eriti oluliseks keeruliste muudatuste puhul, mis ei pruugi olla kohe ilmsed ainult koodi erinevusi uurides.


Läbivaatamise protsess on avatud lähtekoodiga arenduse koostööaspekt, kus projekti hooldajad ja kogenud kaasajad hindavad teie kavandatud muudatusi. Võite taotleda konkreetseid ülevaatajaid, kellel on kogemusi valdkondades, mida teie muudatused puudutavad, tagades, et asjatundlikud kogukonnaliikmed teie tööga tutvuvad. Läbivaatamise protsess võib hõlmata mitmeid kordusi, mille käigus annavad ülevaatajad tagasisidet, nõuavad muudatusi või paluvad täiendavat testimist. Selline ühine täiustamisprotsess aitab säilitada koodi kvaliteeti, pakkudes samal ajal väärtuslikke õppimisvõimalusi kõigi kogemustasemete osalistele.


Mõistmine, et mitte kõik tõmbetaotlused ei saa heakskiitu, aitab seada asjakohased ootused panustamisprotsessile. Projekti hooldajad võivad keelduda projektitaotluste esitamisest erinevatel põhjustel, sealhulgas mittevastavus projekti eesmärkidele, ebapiisav testimine või juba väljatöötamisel olevate alternatiivsete lahenduste olemasolu. Selle asemel, et käsitleda tagasilükkamist kui ebaõnnestumist, tuleks seda käsitleda kui võimalust tagasisidest õppida, täiustada lähenemisviisi ja potentsiaalselt pakkuda alternatiivseid lahendusi, mis vastavad paremini projekti vajadustele. Avatud lähtekoodiga kogukond õitseb sellisest ettepanekute esitamise, läbivaatamise ja täiustamise iteratiivsest protsessist, mis lõppkokkuvõttes viib projekte edasi tänu ühistele jõupingutustele ja jagatud kogemustele.



## Mis on Public-Pool?

<chapterId>b461bf94-4a90-5bb8-ba3f-976d5d57be0d</chapterId>


:::video id=d4652496-1ed4-4415-8048-0b6871b9ed51:::

Public Pool kujutab endast revolutsioonilist lähenemist Bitcoin mining-le, mis lahendab paljud probleemid, mis kaevandajatel on traditsiooniliste mining-ga seotud. Täielikult avatud lähtekoodiga Bitcoin mining soolopoolina muudab Public Pool põhjalikult tasu jaotamise mudelit, millega kaevurid on harjunud. Erinevalt tavapärastest mining-puulidest, kus osalejad jagavad tasu, kui ükskõik milline kaevandaja leiab ploki, töötab Public Pool soolo- mining põhimõttel, kus üksikud kaevandajad säilitavad 100 % oma ploki tasu, kui nad on edukalt ploki kaevandanud.


Public Pool'i kõige veenvam omadus on selle tasuta struktuur. Kui kaevandajad leiavad Public Pool'i abil edukalt ploki, saavad nad kogu ploki tasu koos kõigi sellega seotud [tehingutasudega](https://planb.academy/resources/glossary/transaction-fees), ilma et neist oleks maha arvatud basseerimisega seotud kulud. See on teravaks kontrastiks traditsioonilistele mining-poolidele, mis tavaliselt võtavad tasu vahemikus 1-3% mining-palgast. Nulltasu mudel muudab Public Pooli eriti atraktiivseks kaevurite jaoks, kes soovivad maksimeerida oma võimalikku tulu, säilitades samal ajal täieliku kontrolli oma mining operatsioonide üle.


Public Pooli unikaalse positsiooni mõistmiseks on oluline mõista põhimõttelist erinevust soolo- mining ja ühisrahastuse mining vahel. Tõeline soolo mining tähendab, et kaevandate iseseisvalt ja saate bloki leidmise korral kogu plokihüvitise (praegu 3,125 BTC + tasud), kuid tõenäosus on proportsionaalne teie hash-kiirusega võrreldes kogu võrgustikuga - see tekitab äärmusliku varieeruvuse, mis võib ulatuda kuude või aastate vahele. Traditsioonilised basseinid kombineerivad hash-võimsust, et leida plokke sagedamini, jaotades tasu proportsionaalselt ja pakkudes stabiilset, prognoositavat sissetulekut. Kaevurite jaoks, kes on investeerinud märkimisväärset kapitali riistvarasse ja tegevuskuludesse, on puhas soolo- mining tavaliselt ebapraktiline, olenemata selle filosoofilistest eelistest - varieeruvus muudab elektrikulude katmise ja investeeringute tagasisaamise peaaegu võimatuks. See majanduslik reaalsus tähendab, et enamik kaevandajaid valib praktilistel finantspõhjustel ühendatud mining. Public Pool tegutseb soolo- mining-poolina, mis tähendab, et teil on endiselt silmitsi soolo- mining variatsiooniga (te saate tasu ainult siis, kui te isiklikult leiate ploki), kuid te saate kasu basseini infrastruktuurist ja läbipaistvast, tasuta toimimisest.


### Avatud lähtekoodi eelis ja tehniline rakendamine


Public Pooli pühendumine avatud lähtekoodiga arendusele annab kaevuritele enneolematu läbipaistvuse ja kontrolli oma mining operatsioonide üle. Kogu koodibaas on kättesaadav GitHubis, mis võimaldab kaevandajatel täpselt uurida, kuidas tarkvara töötab, seda vastavalt oma vajadustele muuta ja isegi selle arendamisse panustada. Selline läbipaistvus aitab lahendada mining kogukonna olulist muret seoses traditsiooniliste mining poolide tundmatute konfiguratsioonide ja tavadega.


Tarkvara ülesehitus hõlmab nii mining basseini põhifunktsioone kui ka eraldi kasutajaliidese repositooriumi, mis mõlemad on vabalt allalaadimiseks ja muutmiseks saadaval. Kaevandajad saavad Public Pool'i käivitada erinevates konfiguratsioonides, sealhulgas Dockeri konteinerites, mis muudab selle kohandatavaks erinevate riistvara seadistuste ja tehniliste eelistustega. GitHubi repositooriumides pakutav põhjalik dokumentatsioon pakub üksikasjalikke paigaldusjuhiseid, konfiguratsioonivõimalusi ja muutmisjuhiseid, mis teeb selle kättesaadavaks erineva tehnilise tasemega kaevuritele.


Avaliku basseiniga ühendamine nõuab traditsiooniliste mining seadistustega võrreldes minimaalset konfigureerimist. Kaevandajad peavad lihtsalt konfigureerima oma mining-seadmed [Stratumi](https://planb.academy/resources/glossary/stratum) ühenduse üksikasjadega ja andma kasutajanimeks oma Bitcoin aadressi. Valikuline töötaja nimi võib lisada pärast punkti eraldusjoont korralduslikel eesmärkidel.


### Ühenduse omadused ja jätkusuutlikkuse mudel


Public Pool sisaldab mitmeid uuenduslikke funktsioone, mis tugevdavad Bitcoin mining kogukonda, säilitades samal ajal selle tasuta toimimise. Platvorm kuvab põhjalikku statistikat, sealhulgas ühendatud kaevurite kogu hash-kiirust, mis 2024. aastal oli tavaliselt vahemikus 1-2 PetaHashi sekundis ja 2025. aasta novembris umbes 40 PH/s, ning annab üksikasjalikku teavet ühendatud mining seadmete kohta. Eriti tähelepanuväärne on platvormi rõhuasetus avatud lähtekoodiga mining riistvarale, kusjuures seadmed on tähistatud tähtedega, mis tähistavad täielikult avatud lähtekoodiga projekte, koos linkidega nende vastavatele GitHubi hoidlatele.


Public Pool'i tasuta tegevuse jätkusuutlikkus põhineb loomingulisel partnerprogrammi partnerlusel mining riistvara tarnijatega. Kui kaevurid ostavad partnerfirmadelt seadmeid, kasutades allahindluskoodi "SOLO", toetab viiskümmend protsenti partneri tuludest Public Pooli tegevuskulusid, ülejäänud viiskümmend protsenti jagatakse preemiatena kaevuritele, kes saavutavad iga kuu kõrgeima raskusastme. See mudel loob sümbiootilise suhte, kus kaevurid saavad seadmete ostmisel soodustusi, müüjad saavad kliente ja Public Pool säilitab oma tegevuse ilma otseseid tasusid nõudmata.


### Detsentraliseerimise filosoofia ja parimad tavad


Kuigi Public Pool pakub suurepärast alternatiivi traditsioonilistele mining-poolidele, on oluline mõista selle rolli Bitcoin detsentraliseerimise laiemas kontekstis. Platvorm on hüppelauaks lõppeesmärgi suunas, milleks on individuaalsed kaevandajad, kes haldavad oma mining-pooled. Oma mining basseini haldamine on detsentraliseerimise kõrgeim tase, sest see välistab sõltuvuse kolmandatest osapooltest, olenemata sellest, kui läbipaistev või heatahtlik see kolmas osapool on.


Public Pooli avatud lähtekoodiga olemus muudab selle ideaalseks õppeplatvormiks kaevuritele, kes soovivad enne oma lahenduste rakendamist mõista pooli toiminguid. Paigaldusjuhendite kättesaadavus mitme operatsioonisüsteemi jaoks ja põhjalik dokumentatsioon annavad kaevuritele vajalikud teadmised, et minna Public Pooli kasutamisest üle oma mining infrastruktuuri käitamisele. See hariduslik aspekt on kooskõlas Bitcoin põhiprintsiipidega, milleks on isemajandamine ja detsentraliseerimine, andes üksikutele kaevuritele võimaluse võtta oma mining operatsioonide üle täielik kontroll, aidates samal ajal kaasa Bitcoin võrgu üldisele turvalisusele ja detsentraliseerimisele.


Platvormi kasutajaliides pakub kaevuritele üksikasjalikke jälgimisvõimalusi, sealhulgas töötajate staatust, hash-kiiruse statistikat ja tulemuslikkuse näitajaid. Need funktsioonid aitavad kaevandajatel optimeerida oma tegevust, õppides samal ajal tundma basseinide haldamise põhimõtteid, mida nad saavad hiljem rakendada oma mining basseinide rakendustes.


## Kuidas paigaldada Public-Pool Umbrelile

<chapterId>7f6d0307-7715-5581-89ea-f13cf8754f9a</chapterId>


:::video id=3a4fe0a9-bbf5-458a-8ec1-52c3b83afd87:::

Oma Bitcoin mining basseinide käitamine kodus on tänu kaasaegsele riistvarale ja lihtsustatud tarkvaralahendustele muutunud üha kättesaadavamaks. Selles peatükis uuritakse kodus asuva avaliku basseini praktilist rakendamist, kasutades taskukohast mini-PC riistvara ja lihtsustatud [sõlme](https://planb.academy/resources/glossary/node) haldustarkvara. Selle juhendi lõpuks saate aru riistvaranõuetest, tarkvara seadistamisprotsessist ja põhikonfiguratsioonist, mis on vajalikud oma mining basseinitaristu loomiseks.


### Riistvaranõuded ja seadistamine


Iga koduse mining basseiniseadme alus algab sobiva riistvara valikuga, mis tasakaalustab jõudluse, hinna ja energiatõhususe. Miniarvuti on selle rakenduse jaoks ideaalne lahendus, mis pakub piisavat töötlemisvõimsust, säilitades samal ajal kompaktse ruumi ja mõistliku energiatarbimise. Soovitatav konfiguratsioon sisaldab Intel N100 protsessorit, mis pakub piisavaid arvutusvõimsusi basseinitöödeks, koos vähemalt ühe terabaidi NVMe-mäluga, et mahutada Bitcoin [plokiahela](https://planb.academy/resources/glossary/blockchain) ja sellega seotud andmeid.


Salvestusruumi nõue on eriti kriitiline, kuna mining koondamise korral on vaja säilitada täielikult sünkroniseeritud Bitcoin sõlme. Ühe terabaidi suurune NVMe-ketas tagab kiire lugemis- ja kirjutamisoperatsiooni, mis on oluline plokiahela sünkroniseerimiseks ja jooksva [tehingu](https://planb.academy/resources/glossary/transaction-tx) töötlemiseks. Lisaks sellele toetab piisav RAM-i eraldamine nii aluseks oleva Linuxi operatsioonisüsteemi kui ka basseinitegevusi koordineeriva sõlme haldustarkvara sujuvat toimimist.


### Tarkvaraarhitektuur ja sõlmede haldamine


mining koduse basseini tarkvarapakett tugineb Linuxi baasil, mis tagab Bitcoin tööks vajaliku stabiilsuse ja turvalisuse. Selle baassüsteemi peal loob spetsiaalne sõlmede haldustarkvara, nagu Umbrel, intuitiivse liidese Bitcoin infrastruktuuri haldamiseks. Selline lähenemisviis vähendab suurt osa keerukusest, mis on tavapäraselt seotud Bitcoin sõlmede käitamisega, muutes basseinide käitamise kättesaadavaks ka kasutajatele, kellel puudub ulatuslik tehniline taust.


Umbrel on terviklik sõlme haldusplatvorm, mis tegeleb [Bitcoin Core'i](https://planb.academy/resources/glossary/bitcoin-core) paigaldamise, sünkroniseerimise ja pideva hooldusega veebipõhise liidese kaudu. Platvormi rakenduste poe mudel võimaldab lihtsate point-and-click operatsioonide abil hõlpsasti paigaldada lisateenuseid, sealhulgas mining basseinitarkvara. Selline arhitektuur tagab, et kasutajad saavad keskenduda pigem basseinide käitamisele kui süsteemi haldamisele, säilitades samas täieliku kontrolli oma Bitcoin infrastruktuuri üle.


### Avaliku basseini paigaldamine ja konfigureerimine


Avaliku basseinitarkvara paigaldamine Umbreli platvormi kaudu näitab kaasaegse Bitcoin infrastruktuuri kasutuselevõtu sujuvust. Protsess algab juurdepääsuga Umbreli rakenduste poodi veebiliidese kaudu, kus lihtne otsing "public pool" toob esile saadaval oleva mining basseinitarkvara. Paigaldamine nõuab vaid paari klõpsu: rakenduse valimine, paigalduse kinnitamine ja automaatse häälestusprotsessi lõpuleviimise ootamine.


Paigaldusprotsess konfigureerib automaatselt vajalikud ühendused avaliku basseinitarkvara ja selle aluseks oleva Bitcoin-sõlme vahel. See integratsioon tagab, et bassein saab tehinguid valideerida, plokkide malle konstrueerida ja tööd ühendatud kaevuritele jaotada, ilma et oleks vaja keerulisi võrguparameetreid käsitsi konfigureerida. Pärast paigaldamise lõpetamist muutub basseiniliides kohe kättesaadavaks kohaliku võrgu kaudu, pakkudes reaalajas jälgimis- ja haldusvõimalusi.


### Kaevurite ühendamine ja võrguga seotud kaalutlused


mining riistvara ühendamine teie äsja loodud basseiniga nõuab kaevandaja basseisu seadete konfigureerimist nii, et need osutaksid teie kohalikule infrastruktuurile. See hõlmab vaikimisi basseiniaadressi asendamist teie kohaliku IP-aadressiga ja avaliku basseini paigaldamise käigus määratud asjakohase portinumbriga. Konfiguratsiooni muutmine suunab teie mining riistvara arvutustegevuse väliselt basseinilt teie kodusele infrastruktuurile, võimaldades teil säilitada täieliku kontrolli mining tööde ja võimalike tasude üle.


Võrgukonfiguratsioon mängib basseinide juurdepääsetavuse ja funktsionaalsuse puhul olulist rolli. Kohaliku võrgu seadistamine hõlmab tavaliselt standardset IP-aadressi, kuid kasutajad võivad sõltuvalt ruuteri konfiguratsioonist kokku puutuda DNS-eralduse erinevustega. Mõned marsruuterid pakuvad kohalikke DNS-teenuseid, mis loovad kohalike teenuste jaoks sõbralikud nimed, samas kui teised nõuavad otsest IP-aadressile juurdepääsu. Laiema ligipääsu tagamiseks väljaspool kohalikku võrku võib osutuda vajalikuks portide suunamise konfigureerimine marsruuteril, kuigi see toob kaasa täiendavaid turvakaalutlusi, mis nõuavad sellega seotud riskide ja eeliste hoolikat hindamist.


Koduse mining-pooluse edukas loomine on oluline samm detsentraliseeritud Bitcoin infrastruktuuri suunas, mis pakub nii hariduslikku väärtust kui ka praktilisi mining võimalusi, säilitades samal ajal täieliku kontrolli oma Bitcoin toimingute üle.


# Riistvara kokkupanek ja tõrkeotsing

<partId>f6987088-5ba4-52e2-b2d0-aa122080940c</partId>


## Milliseid vahendeid kasutada?

<chapterId>733935b5-0171-5a22-838c-e192df6f7ccf</chapterId>


:::video id=bddd0e47-7b43-4685-ba2e-bf3a8ff653c9:::

Pindpaigaldatavate seadmete (SMD) jootmise maailmas, eriti Bitaxe-projektidega töötades, muudab õigete tööriistade olemasolu pettumuse ja edu vahel erinevuse. Selles põhjalikus juhendis käsitletakse SMD-jootmisprojektide tõhusaks lahendamiseks vajalikke olulisi seadmeid, alates põhilistest käsitööriistadest kuni spetsiaalsete seadmeteni, mis tõstavad teie jootmisvõimet.


Kui soovite tutvuda skeemide dokumentatsiooniga, vaadake seda [GitHub repo](https://github.com/skot/bitaxe-doc/tree/main).


### Põhilised käsitööriistad ja täppisinstrumendid


Iga SMD-jootmise seadistuse alus algab kvaliteetsetest pintsettidest, mis on teie peamised komponentide paigutamise vahendid. Kõige väärtuslikumaks osutuvad kaks tüüpi pintsetid: tavalised sirge otsaga pintsetid ja pintsetid, mille ots on kergelt painutatud. Sirge otsaga pintsetid sobivad enamiku tüüpilistes Bitaxe-komplektides leiduvate SMD-komponentidega, samas kui painutatud otsaga pintsetid on suurepärased, kui töötate väga väikeste komponentidega, mis nõuavad täpset positsioneerimist. Need tööriistad on sageli kaasas remondikomplektidega, näiteks iFixiti komplektidega, mis on mõeldud telefonide parandamiseks, mistõttu on need enamikule harrastajatele hõlpsasti kättesaadavad.


Pintsettidele lisaks on hea käärid hädavajalikud elektrilindi lõikamiseks, millel on elektroonikaprojektides mitu otstarvet. Elektriline teip on oluline isolatsioon kaablitele ja komponentidele ning kvaliteetse teibi kättesaadavus lihtsustab jootmisprotsessi. Neid põhitarbeid saab hankida riistvarapoodidest või veebimüüjatest, ilma et oleks vaja spetsiaalseid elektroonikatarnijaid.


### Jootepasta kasutamine ja haldamine


Jootepasta pealekandmine on SMD-jootmise üks kõige kriitilisemaid aspekte ning õiged tööriistad muudavad selle protsessi nii täpseks kui ka nauditavaks. Väikesed, mitte teravad süstlad, mis on täidetud jootepastaga, tagavad erakordse kontrolli pasta paigutamise üle. See meetod võimaldab iga ühenduskoha jaoks vajaliku jootepasta koguse täpset pealekandmist ning enamik inimesi omandab praktilise harjutamise käigus kiiresti õige tehnika rõhu ja voolukiiruse kontrollimiseks.


Jootepasta valik ise mõjutab oluliselt jootmise edukust. ChipQuik TS391SNL50 paistab silma kui erakordne jootepasta Bitaxe-projektide ja üldiste SMD-tööde jaoks. See pasta säilitab nõuetekohase konsistentsi ja sulamisomadused, vältides probleeme, mis on seotud odavamate alternatiividega, millel on liiga madalad sulamistemperatuurid. Madala kvaliteediga jootepastad võivad tekitada probleeme, kus varem jootetud ühendused muutuvad kõrvalolevate alade kuumutamisel uuesti vedelaks, mis viib komponentide nihkumise ja kehvade ühendusteni. Kuigi kvaliteetne jootepasta kujutab endast suuremat alginvesteeringut, õigustavad paremad tulemused ja vähenenud pettumused seda kulu.


### Probleemide lahendamise ja puhastamise vahendid


Isegi kogenud jootjad puutuvad kokku probleemidega, mis vajavad parandamist, mistõttu on jootevahendid hädavajalikud igas täielikus tööriistakomplektis. Jootevaba seadeldis, mis on sisuliselt kuumutatud vaakumtööriist, eemaldab liigse jootmise ja parandab komponentide tihvtide vahelised sillatud ühendused. Need tööriistad töötavad kõige tõhusamalt koos jootevahendiga, mis parandab jootevoolu ja aitab jootmisprotsessi tõhusamalt läbi viia.


Voolufluksi on mitmesugusel kujul, sealhulgas tahkete ja vedelate variantidena, ning sellel on mitmeid eesmärke peale jootmisabi. Kui jootepasta hakkab pikema töö käigus oma tõhusust kaotama, taastab täiendava jootevahendi kasutamine nõuetekohased voolavusomadused ja tagab usaldusväärsed ühendused. Väike lusikalaadne tööriist, mida sageli leidub täppisremondikomplektides, hõlbustab täpse jootevahendi pealekandmist konkreetsetele piirkondadele, ilma et ümbritsevad komponendid saastuksid.


Plaadi puhastamine on professionaalse töö viimane samm, mis nõuab isopropanoolalkoholi ja spetsiaalset puhastusharja. Selleks sobib suurepäraselt vana hambahari ning isopropanooli sisaldav pigistuspudel võimaldab puhastuslahuse kontrollitud pealekandmist. See kombinatsioon eemaldab fluksijäägid ja pastajäägid, jättes plaadid puhta ja professionaalse välimusega, mis hõlbustab ka jootekohtade kontrollimist.


### Spetsiaalsed seadmed ja täiustatud tööriistad


Keerukate integraallülituste, eriti ASIC-de puhul muudavad šabloonid jootmisprotsessi tüütust käsitsi paigaldamisest tõhusaks ja täpseks pastakandmiseks. Need täppislõikega šabloonid tagavad ühtlase pastapaksuse ja paigutuse, vähendades oluliselt keeruliste komponentide jaoks kuluvat aega ja parandades samal ajal töökindlust. Investeering kvaliteetsetesse šabloonidesse tasub end ära nii aja kokkuhoiu kui ka paremate tulemuste näol.


Soojusjuhtimine muutub energiakomponentidega töötades ülioluliseks, mistõttu termopasta või termorasv on hädavajalikud tarvikud. Need materjalid tagavad nõuetekohase soojusülekande jahutusaluste ja integraallülituste vahel, ennetades termilisi kahjustusi ja tagades usaldusväärse töö. Kvaliteetsed soojusliidese materjalid on väike investeering, mis kaitseb palju kallimaid komponente.


Iga SMD-jootmisseadme süda on kuumaõhu ümbertöötlusjaam, mis tagab pinna paigaldamiseks vajaliku kontrollitud kuumuse. Kuigi 30-50 dollari suurused odavad jaamad võivad olla piisavalt tõhusad, puudub neil sageli kõrgema klassi seadmete usaldusväärsus ja täpsus. Need algtaseme jaamad töötavad tavaliselt tõhusalt 355 °C juures ja sisaldavad automaatset temperatuuri vähendamist, kui käsitsitükk pannakse tagasi hoidikusse. Siiski võib nende töökindlus olla ebaühtlane, mõned seadmed võivad enneaegselt välja kukkuda. Tõsisemate tööde puhul pakub spetsialiseerunud elektroonikatarnijate kvaliteetsemate seadmete soetamine parema pikaajalise väärtuse tänu paremale töökindlusele ja täpsemale temperatuurikontrollile.


Nende tööriistade kombinatsioon loob täieliku SMD-jootevõimekuse, mis ulatub kaugemale Bitaxe projektidest kuni üldiste elektroonikatöödeni. Iga tööriista rolli mõistmine ja teie oskuste tasemele ja projekti nõuetele vastava kvaliteetse varustuse valimine tagab eduka tulemuse ja meeldiva jootmiskogemuse.



## Fikseerige jooteküsimused

<chapterId>96663744-b4f7-5154-930f-a68ba7954603</chapterId>


:::video id=9286c0dc-acd6-44d9-b34e-59cfb2da9748:::


Bitaxe transceiveri komplekt esitab monteerimisel unikaalseid väljakutseid, mis nõuavad hoolikat tähelepanu komponentide orientatsioonile, jootesildade vältimisele ja nõuetekohasele soojusjuhtimisele. Nende tavaliste probleemide ja nende lahenduste mõistmine on oluline komplekti edukaks ehitamiseks ja kulukate komponentide kahjustuste vältimiseks. Selles peatükis vaadeldakse Bitaxe'i koostamisel kõige sagedamini esinevaid jootmisprobleeme ning esitatakse praktilisi meetodeid nende tuvastamiseks ja lahendamiseks.


### Komponentide orienteerumine ja identifitseerimine


Komponentide õige orienteerimine on üks kriitilisemaid aspekte eduka Bitaxe'i monteerimise juures, eriti MOSFETide Q1 ja Q2 puhul. Nendel komponentidel on iseloomulikud orientatsioonimärgid, mida tuleb paigaldamisel hoolikalt jälgida. Igal MOSFETil on väike punktimärgistus, mis vastab spetsiifilisele padide paigutusele trükkplaadil. Õige orienteerimise võti seisneb nende komponentide füüsilise struktuuri mõistmises, millel on neli tihvti, mis on paigutatud ühe suure padiga ja kolme väiksema padiga, mis ei ole suure padiga seotud.


Q1 ja Q2 paigaldamisel uurige hoolikalt nii komponenti kui ka trükkplaati. Plaadi paigutus näitab selgelt kavandatud orientatsiooni läbi selle pad-konfiguratsiooni, kus neli tihvti on paigutatud vastavalt MOSFETi struktuurile. Enne mis tahes suure komponendi jootmist kontrollige alati orientatsiooni, võrreldes komponendi füüsilisi tähiseid plaadi padide paigutusega. See lihtne kontrollsamm hoiab ära pettumuse, mis kaasneb valesti orienteeritud komponentide lahtijootmise ja uuesti paigaldamisega.


Vale orienteerumise tagajärjed ulatuvad kaugemale lihtsatest funktsionaalsuse probleemidest. Vääralt orienteeritud MOSFETid võivad tekitada vooluahela häireid, mida on raske diagnoosida ja mis võivad nõuda komponentide täielikku väljavahetamist. Aja võtmine orientatsiooni kontrollimiseks enne kuumuse rakendamist tagab vooluahela nõuetekohase toimimise ja hoiab ära tarbetu tõrkeotsingu hiljem kokkupaneku käigus.


### Joodisildade ja üleliigse jootekoguse haldamine


Joodisillad on veel üks tavaline probleem Bitaxe monteerimisel, eriti selliste peenikese sammuga komponentide puhul nagu U10. Need soovimatud ühendused kõrvuti asetsevate tihvtide vahel võivad põhjustada vooluahela häireid ja nõuavad hoolikat eemaldamist. Kõige tõhusam lähenemisviis hõlmab jootevahendi eemaldamist, mis on vaskpunutisega materjal, mis kuumutamisel imab endasse liigse joote. See tehnika nõuab kannatlikkust ja õiget tööriistade valikut, et vältida õrnade komponentide kahjustamist.


Integreeritud vooluahelate jootesildade käsitlemisel kasutage PCB-hoidjat või liigendklambrit, et hoida komponenti töö ajal kindlalt kinni. Kuumutage kahjustatud piirkonda õrnalt ja tõmmake jootekolbist ettevaatlikult üle sillatud ühenduste. Vaskpunutis absorbeerib loomulikult liigse joote, eraldades soovimatud ühendused. See protsess võib nõuda mitu katset, kuid püsivus annab puhtaid, korralikult eraldatud ühendusi.


Ennetamine on endiselt parim lähenemisviis jootesildade haldamiseks. Sobiva hulga jootepasta kasutamine ja kindla käekontrolli säilitamine komponentide paigutamise ajal vähendab oluliselt sildade teket. Kui sillad tekivad, tuleb nendega kohe tegeleda, mitte loota, et need ei mõjuta vooluahela toimimist. Isegi näiliselt väikesed sillad võivad põhjustada märkimisväärseid funktsionaalsusprobleeme, mida on raske diagnoosida, kui plaat on täielikult kokku pandud.


### Kriitilised komponendid ja erilised kaalutlused


Erilist tähelepanu väärib ülesehitusmuundur U9, kuna see mängib olulist rolli 5 volti muundamisel 1,2 volti ASIC kiibi jaoks. See komponent kujutab endast ainulaadset väljakutset oma viie väikese ühenduse ja riketele kaldumise tõttu. Nõuetekohane paigaldamine nõuab täpset jootepasta pealekandmist ja hoolikat soojusjuhtimist. Ebapiisav jootepasta U9 all võib põhjustada halbu ühendusi, mis takistavad nõuetekohast pinge muundamist, samas kui liigne pasta võib tekitada sildasid, mis põhjustavad vooluahela talitlushäireid.


U9 tekitab jootesildade probleemide korral iseloomulikke helisignaale, tekitades kõrgsageduslikku müra, mis erineb ASIC tavalisest tööpõhimõttest. See auditiivne diagnostikameetod võib aidata probleeme tuvastada, kuigi selle tuvastamiseks on vaja head kõrgsageduslikku kuulmist. Kui audiodiagnostika ei ole võimalik, muutub oluliseks visuaalne kontroll. Uurige hoolikalt kõiki ühendusi, otsides sildasid või ebapiisavat jootekatet.


Kui U9 ei väljasta nõutavat 1,2 volti, kuigi tundub korralikult jootetuna, peate tõenäoliseks põhjuseks ebapiisavat jootepastat. Eemaldage komponent, kandke väike kogus täiendavat jootepastat ja paigaldage uuesti. Kui üksikud tihvtid ei ole piisavalt kaetud jootepinnaga, kandke pintsettide abil ettevaatlikult väikestes kogustes jootepastat konkreetsetesse kohtadesse. Soojuspasta voolab kuumutamisel loomulikult komponendi alla, luues kapillaarjuhtimise abil korralikud ühendused.


### Soojuse juhtimine ja komponentide kaitse


Nõuetekohane soojusjuhtimine kaitseb tundlikke komponente termiliste kahjustuste eest, tagades samal ajal usaldusväärsed jootekohad. Sellised komponendid nagu kristallostsillaator Y1 ja U1 on eriti tundlikud pikaajalise kuumuse suhtes ja vajavad hoolikat temperatuurikontrolli. Hoidke jootekolvi temperatuur 350 kraadi juures, kuid vähendage kuumuse kohaldamise aega, et vältida komponentide kahjustamist. Kiire ja tõhusad jootmistehnikad kaitsevad neid tundlikke komponente, saavutades samal ajal usaldusväärsed ühendused.


ASIC kiip nõuab erilisi käitlemistehnikaid oma keerulise tihvtstruktuuri ja mehaanilise pingetundlikkuse tõttu. Kui kasutate jootepasta pealekandmiseks šablooni, veenduge, et kõik pins on ühtlaselt kaetud, et vältida komponentide ebaühtlast istumist. Kui liigne jootepasta põhjustab ASIC ebaühtlase istumise, laske koostel enne paranduste tegemist täielikult jahtuda. Õige istumise saavutamiseks avaldage uuesti soojendamise ajal õrnat survet ainult komponendi märgistatud servadele, mitte kunagi keskmisele matriitspiirkonnale.


Komponent U8 kujutab endast ainulaadset väljakutset oma arvukate tihvtide ja võimalike painduvate juhtmete tõttu. Kui viigud painduvad käsitsemise käigus, kasutage komponendi kinnitamiseks trükkplaadihoidjat või liigendklambrit ja sirutage kahjustatud viigud ettevaatlikult. Töötage aeglaselt ja kannatlikult, et vältida õrnade juhtmete purunemist. Arusaamine, et teatud viigirühmad U8-l on sisemiselt ühendatud, võib lihtsustada tõrkeotsingut, kuna nende konkreetsete viigude vahelised sillad ei mõjuta vooluahela toimimist. Teiste viigude vahelised sillad vajavad aga nõuetekohase funktsioneerimise tagamiseks ettevaatlikku eemaldamist.


## Kuidas oma Bitaxe'ile AxeOS-i abil vigade kõrvaldamine toimub

<chapterId>603f5c0d-4b7c-51e1-9bad-318a8b8e9db7</chapterId>

:::video id=d23d748b-510e-4748-9617-b875da757031:::

Bitaxe mining seadmetega töötades võivad riistvararikked ilmneda erinevatel viisidel, mis ei pruugi olla kohe ilmsed. Mõistmine, kuidas neid probleeme AxeOSi operatsioonisüsteemi abil süstemaatiliselt diagnoosida, võib säästa märkimisväärselt aega ja vältida komponentide asjatut väljavahetamist. Selles peatükis uuritakse diagnostikameetodeid ja tõrkeotsingumeetodeid, mida kogenud tehnikud kasutavad konkreetsete riistvaraprobleemide tuvastamiseks tarkvara analüüsi abil.


### Energiatarbimise näitajate mõistmine


Esimene ja kõige kriitilisem diagnostiline näitaja AxeOSis on energiatarbimise jälgimine. Tavalised Bitaxe'i seadmed, sealhulgas mudelid Bitaxe Ultra ja Bitaxe Supra, tarbivad tavapärase töö ajal tavaliselt 10-17 vatti. See baasmõõtmine on kogu süsteemi esmane tervisenäitaja. Kui energiatarbimine langeb oluliselt alla selle vahemiku, eriti alla 3 vati, annab see märku põhimõttelisest probleemist ASIC kiibiga või seda toetava vooluahelaga.


Madala energiatarbimise stsenaariumid nõuavad kohest tähelepanu, sest need viitavad sellele, et mining kiip on kas täiesti mittetoimiv või töötab väga halvenenud seisundis. Juba ainuüksi see mõõtmine aitab teil kiiresti eristada jõudlusprobleeme ja täielikke riistvararikkeid. AxeOSi võimsusnäit annab reaalajas tagasisidet, mis võimaldab teil jälgida seadme remondikatsete tõhusust.


### ASIC pingemõõtmiste analüüsimine


AxeOSi ASIC pinge mõõtmise funktsioon annab olulist diagnostilist teavet, mis aitab kindlaks teha riistvaraprobleemide täpse olemuse. Pinge näitude uurimisel peate probleemide nõuetekohaseks diagnoosimiseks mõistma mõõdetud pinge ja soovitud pinge vahelist suhet. Süsteem näitab nii ASIC kiibile antavat pinget kui ka pinget, mida kiip vooluhaldussüsteemilt taotleb.


Kui te täheldate ASIC pinge mõõtmist täpselt 1,2 volti koos energiatarbimisega alla 3 vati, siis see konkreetne kombinatsioon näitab kas jootmisprobleemi ASIC kiibiga või ASIC täielikku rikkeid. Selline pingemõõtmine näitab, et vool jõuab küll kiibini, kuid kiip ise ei tööta korralikult. ASIC kiibi füüsilisel kontrollimisel võivad ilmneda praod või muud nähtavad kahjustused, mis seletavad sellist käitumismustrit.


Teistsugune diagnostiline stsenaarium ilmneb, kui näete madalat energiatarbimist koos väga madalate nõutavate pingenäitude, näiteks 100 millivolti või 0,5 volti, näitajatega. See muster näitab, et ASIC kiip ei saa piisavat pingevarustust, mis tavaliselt viitab probleemidele U9 buck-muunduri komponendis. Buck-muundur vastutab täpse pinge reguleerimise eest, mida ASIC kiibid vajavad nõuetekohaseks toimimiseks.


### Logiandmete tõlgendamine ja ASIC side


AxeOS logisüsteem annab väärtusliku ülevaate sellest, kas teie ASIC kiip suhtleb juhtimissüsteemiga. Kui pääsete logidele juurde funktsiooni "show logs" kaudu, kinnitab "ASIC results" kirjete olemasolu, et kiip ei ole mitte ainult ühendatud, vaid ka aktiivselt töödeldav ja tulemusi tagastav. See suhtlus näitab, et ASIC on korralikult jootnud ja säilitab oma ühenduse juhtimisahelaga.


ASIC tulemuste puudumine logides, eriti koos muude sümptomitega, aitab kitsendada probleemi konkreetsete komponentide või ühendusprobleemide suhtes. Selline diagnostiline lähenemine võimaldab eristada kiibid, mis ei reageeri täielikult, ja need, millel võivad olla katkendlikud ühendusprobleemid. Logianalüüs muutub eriti väärtuslikuks keerukate probleemide lahendamisel, kus mitu sümptomit võivad viidata erinevatele algpõhjustele.


### Süstemaatiline veaotsingu lähenemine


Bitaxe'i riistvaraprobleemide diagnoosimisel aitab süstemaatiline lähenemine vältida kriitiliste probleemide tähelepanuta jätmist ja tagab tõhusa remondiprotsessi. Alustage energiatarbimise ja pinge näitude dokumenteerimisest, seejärel korreleerige need mõõtmised logiandmetega, et luua täielik pilt süsteemi käitumisest. Selline metoodiline lähenemine aitab kindlaks teha, kas probleemid tulenevad ASIC kiibist endast, toiteallika süsteemist või komponentidevahelistest kommunikatsiooniradadest.


Juhul kui probleem tundub olevat U9 konverteris, võib olla vajalik füüsiline kontroll ja võimalik ümberlülitamine. U9 komponent on eriti vastuvõtlik jooteprobleemidele, eriti esmakordsel kokkupanekul. Kui kahtlustatakse pinge reguleerimise probleeme, annab multimeetri kasutamine, et kontrollida, kas ASIC viikudel on tegelikult 1,2 volti, lõpliku kinnituse voolu edastamise probleemide kohta. Kui pinge on viikudel olemas, kuid ASIC ikka veel ei tööta ja füüsiline kontroll ei näita kahjustusi, on järgmine loogiline samm ASIC kiibi väljavahetamine. Kui probleemid püsivad ka pärast ASIC asendamist, võib veaotsingu viimase elemendina vajada tähelepanu komponent U2, mis juhib ASIC kiipi.


## Kuidas USB abil siluda?

<chapterId>f3182763-e1ef-5460-8bc0-f2ea53e3a410</chapterId>


:::video id=fe1b4b48-5f8a-4fd7-9417-ca03a36bce9f:::


Bitaxe mining seadmete tõrkeotsingul annab otsene juurdepääs seadme sisemisele logisüsteemile hindamatut teavet, mida veebipõhised liidesed ei suuda pakkuda. Selles peatükis uuritakse, kuidas luua otsene USB-seeriaühendus Bitaxe'i seadmega, kasutades ESP-IDF raamistikku, mis võimaldab reaalajas jälgida süsteemi logisid, käivitamisjärjestusi ja veateateid. Selline vigade kõrvaldamise lähenemisviis on eriti oluline, kui tegemist on seadmetega, mida taaskäivitatakse sageli või mille riistvaras esineb tõrkeid, sest see salvestab kogu diagnostilise teabe, mis võib süsteemi taaskäivitamise ajal kaduma minna.


Veaotsinguprotsess nõuab Visual Studio Code'i koos ESP-IDF laiendiga, kuigi võib kasutada mis tahes ühilduvat IDE-d. See meetod töötab kõigi Bitaxe-variantidega, millel on USB-port, kaasa arvatud Bitaxe Ultra 204 ja teised seeria mudelid. Otsene jadaühendus võimaldab vältida võimalikke veebiliidese piiranguid ja annab filtreerimata juurdepääsu seadme sisemisele olekuteabele.


### Seeriaühenduse seadistamine


Side loomine Bitaxe'i seadmega algab USB-kaabli ühendamisega ja ESP-IDF-terminali avamisega arenduskeskkonnas. Käsk `idf.py monitor` algatab ühendusprotsessi, skaneerides automaatselt olemasolevaid COM-porti, et luua UART-side ESP32 kiibiga teie Bitaxe-seadmes. Tavaliselt läbib süsteem olemasolevaid porte (COM3, COM4, COM16 jne), kuni leiab õige ühenduse.


Kui terminal on ühendatud, kuvatakse kogu käivitamisjärjekord ja käimasolevad kasutusprotokollid. Esialgne ühendamisprotsess võib võtta mitu hetke, kuni süsteem tuvastab õige sidepordi. Kui automaatne pordi tuvastamine ebaõnnestub, võite määrata COM-porti käsitsi IDE pordivalimisliidese kaudu. See otsene sidekanal jääb aktiivseks kogu seadme töö ajal, võimaldades pidevat juurdepääsu süsteemi diagnostikale ja jõudlusnäitajatele.


### Käivitusjärjekorra ja tavapäraste tööprotokollide tõlgendamine


Käivitusjärjekord annab kriitilist teavet teie Bitaxe-seadme riistvara konfiguratsiooni ja initsialiseerimisprotsessi kohta. Tavalised käivitamisprotokollid algavad ESP-IDF-i versiooniteabega, millele järgneb iseloomulik "Welcome to the Bitaxe. Hack the planet" sõnum, mis kinnitab edukat püsivara laadimist. Seejärel kuvatakse ASIC sageduskonfiguratsioon, seadme mudeli identifikatsioon ja plaadi versiooni andmed.


Nõuetekohaselt toimiv seade näitab edukat I2C-initsialiseerimist ja ASIC pinge reguleerimist 1,2 volti. Logides kuvatakse GPIO olekuteave ja Wi-Fi initsialiseerimise jadad, millele järgneb DHCP-serveri konfigureerimine ja IP-aadressi määramine. Üks olulisemaid näitajaid on ASIC kiibi tuvastamise teade, mis peaks ühe kiibiga seadme puhul teatama "detected one ASIC chip" (tuvastatud üks ASIC kiip). See kinnitus kinnitab, et mining riistvara on korralikult ühendatud ja suhtleb ESP32 kontrolleriga.


Operatsioonipäevikutest ilmneb, et seadmes töötab mitu samaaegset ülesannet, sealhulgas kihi API side, põhiülesannete koordineerimine, ASIC ülesannete haldamine ja kihi ülesannete töötlemine. Need erinevad ülesannete tunnused aitavad isoleerida probleeme konkreetsete süsteemikomponentide puhul. Tavapärane töö hõlmab koondühenduste loomist, raskuste korrigeerimise teateid, ülesannete järjekorda seadmist ja järjekorra kustutamist ning nonce'i genereerimise aruandlust. Edukad mining operatsioonid kuvavad ASIC tulemusi koos raskuste arvutustega ja mining esitab kinnitused, kui osakaalud vastavad nõutavale künnisele.


### Riistvara rikete ja veamustrite tuvastamine


Riistvararikked ilmnevad logides konkreetsete veamustrite kaudu, mis näitavad, millised komponendid ei tööta. Kõige tavalisem veamoodus hõlmab I2C-sidevigu Bitaxe'i plaadi konkreetsete integraallülituste puhul. Näiteks DS4432U kommunikatsioonivigade puhul ilmnevad sõnumid "ESP_ERROR_CHECK failed" koos aegumistähistega, mis viitavad pinge reguleerimise probleemidele või jootmisprobleemidele, mis mõjutavad ekraani kommunikatsiooni eest vastutavat U10 komponenti.


Need veateated sisaldavad üksikasjalikku vigade kõrvaldamise teavet, nagu konkreetne lähtekoodifail (main_ds4432u.c), ebaõnnestunud funktsioonikõne ja ülesannet käitlev protsessori tuum. Tagasi jälgitav teave annab täiendava konteksti edasijõudnud veaotsingu jaoks. Sarnaseid veamustreid võib esineda ka EMC2101 temperatuuri ja ventilaatorite kontrollkiibi puhul, mis mõlemad tekitavad eripäraseid logiallkirju, mis aitavad tuvastada rikkeid põhjustavat komponenti.


Füüsilised riistvaraprobleemid esinevad sageli korduvate veatsüklitena, millele järgnevad süsteemi taaskäivitused. Kui teie seade tekitab töö ajal kuuldavat müra, viitab see tavaliselt jootmisprobleemidele, nagu näiteks sildade tekkimine komponentide pinside vahel või ebapiisavad jootekohad. Kuigi need mehaanilised probleemid ei pruugi alati generate konkreetseid logi kirjeid tekitada, tekitavad nad ebastabiilseid töötingimusi, mis väljenduvad sagedaste krahhide ja taaskäivitamise tsüklitena seiretulemustes.


### Täiustatud tõrkeotsingustrateegiad


Seeriajälgimine pakub mitmeid eeliseid veebipõhiste silumisliidestega võrreldes, eriti aeg-ajalt esinevate rikete või sagedaste taaskäivitustega seadmete puhul. Pidev logi salvestamine tagab, et süsteemi taaskäivitamise ajal ei lähe diagnostiline teave kaduma, erinevalt veebiliidestest, mis võivad andmeid kaotada ühenduse katkestamise ajal. Selline põhjalik logimisvõime võimaldab tuvastada rikete mustreid ja seostada konkreetseid veatingimusi riistvara või keskkonnateguritega.


Probleemseid seadmeid analüüsides keskenduge pigem rikete tekkimiseni viinud sündmuste jadale kui üksikutele veateadetele. Edukas ASIC side peaks näitama regulaarset tööde töötlemist, nonce'i genereerimist ja aktsiate esitamise tsüklit. Puuduvad ASIC tulemused logides viitavad ESP32 ja mining kiibi vahelistele kommunikatsioonihäiretele, mille põhjuseks on sageli toiteallikaga seotud probleemid, kahjustatud jäljed või komponentide rikked.


Süstemaatiliseks tõrkeotsinguks dokumenteerige veamustrid ja komponendispetsiifilised vead enne kogukonna toetuse taotlemist. Üksikasjalikud veaprotokollid, sealhulgas konkreetsed kiibitunnused ja veamoodused, võimaldavad kogenud kasutajatel anda sihipäraseid remondijuhiseid, näiteks komponentide asendamise protseduurid või jootmisparandused. Selline metoodiline lähenemine riistvara veaotsingule parandab oluliselt paranduste edukuse määra ja vähendab keerukate probleemide korral veaotsingu aega.


# Täiustatud kohandamine

<partId>8d333102-ecb5-5f05-bfb5-03a27b2d0d70</partId>


## Muuda trükkplaati

<chapterId>ca08d2a4-2b34-575b-aecc-7482a03c190e</chapterId>


:::video id=30fb0010-f560-4e96-a05b-c21dc172746e:::

KiCad on üks võimsamaid avatud lähtekoodiga tööriistu trükkplaatide (PCB) projekteerimiseks ja marsruutimiseks. See professionaalse tasemega tarkvara võimaldab inseneridel ja harrastajatel luua keerulisi elektroonilisi projekte, paigutades komponendid virtuaalsetele plaatidele ja suunates keerulised jäljed, mis neid komponente omavahel ühendavad. KiCad on eriti väärtuslik haridus- ja arendusotstarbel, kuna see on täielikult avatud lähtekoodiga, mis võimaldab kasutajatel muuta, kohandada ja õppida olemasolevatest projektidest ilma litsentsipiiranguteta.


Bitaxe'i projekt on näide avatud lähtekoodiga riistvara arendamise võimsusest, pakkudes täielikku PCB disaini, mida kasutajad saavad uurida, muuta ja kohandada vastavalt oma konkreetsetele vajadustele. Selline ligipääsetavus loob suurepärase õpikeskkonna, kus üliõpilased ja praktikud saavad uurida reaalseid PCB-konstruktsioone, arendades samal ajal oma arusaamist elektroonikasüsteemidest. Võimalus kohandada visuaalseid elemente, näiteks logosid, pakub ligipääsetavat sisenemisvõimalust kasutajatele, keda elektroonilise disaini tehniline keerukus võib hirmutada.


### KiCad keskkonna seadistamine


Enne mis tahes kohandamistööde alustamist on oluline oma arenduskeskkonna nõuetekohane seadistamine. Bitaxe'i repositoorium tuleb alla laadida oma kohalikku masinasse, mis tavaliselt toimub GitHubi ZIP-allalaadimisfunktsiooni abil. See repositoorium sisaldab kõiki vajalikke projektfaile, sealhulgas KiCadi projektfaile, komponentide raamatukogusid ja projekteerimisdokumentatsiooni, mis on edukaks muutmiseks vajalikud.


KiCadi paigaldamine tuleks lõpule viia, kasutades KiCadi veebilehe ametlikku distributsiooni, mis tagab ühilduvuse projektfailidega ja juurdepääsu uusimatele funktsioonidele. Kui nii repositoorium kui ka KiCad on korralikult paigaldatud, tuleb projekti avamiseks navigeerida allalaaditud repositooriumi struktuuris Bitaxe Ultra KiCad'i projektifaili juurde. See projektfail on keskne keskus, mis ühendab kõik seotud projekteerimisfailid, komponentide raamatukogud ja konfiguratsiooni seaded.


Keerulise trükkplaadi disaini esialgne vaade võib tunduda üle jõu käiv, sest arvukad komponendid, jäljed ja kihid loovad tiheda visuaalse maastiku. KiCadi 3D vaatefunktsioon pakub siiski hindamatut abi füüsilise paigutuse ja ruumiliste suhete mõistmiseks disainis. See kolmemõõtmeline vaatenurk muudab abstraktse skeemilise kujutise realistlikuks visualiseerimiseks lõplikust valmistatud tootest, muutes komponentide paigutuse ja üldise disaini esteetika arusaadavamaks.


### Logo kohandamise protsess


Logode kohandamine PCB-disainidel on üks kõige kättesaadavamaid muudatusi KiCadiga alustavatele kasutajatele, mis nõuab minimaalseid tehnilisi teadmisi, pakkudes samas koheseid visuaalseid tulemusi. Protsess algab pildikonverteri tööriistaga, mis muudab standardpildifailid PCB-disaini tarkvaraga ühilduvateks jalajäljeformaatideks. See teisendusprotsess nõuab hoolikat tähelepanu mõõtmisparameetritele, mida tavaliselt mõõdetakse millimeetrites, et tagada lõplikul valmistataval plaadil õige mõõtkava.


Pildikonverteri tööprotsess hõlmab mitmeid kriitilisi etappe, mis määravad kohandatud logode lõpliku välimuse ja paigutuse. Allikapildi valikul tuleks eelistada kontrastseid kujundusi, mis sobivad hästi PCBde valmistamisel kasutatava siiditrükiprotsessi jaoks. Suuruse täpsustamine on otsustava tähtsusega, kuna logod peavad olema piisavalt suured, et need jääksid pärast tootmist loetavaks, kuid ei segaks komponentide paigutamist ega funktsionaalsust. Valik esi- ja tagakihi vahel mõjutab nii nähtavust kui ka tootmisega seotud kaalutlusi.


Jalajälgede raamatukogu haldamine on KiCadi kohandamise põhiline aspekt, mis nõuab kasutajatelt arusaamist sellest, kuidas tarkvara korraldab projekteerimiselemendid ja neile juurdepääsu võimaldab. Kohandatud logode lisamine hõlmab uute jalajälgede raamatukogude loomist või olemasolevate muutmist ning seejärel nende raamatukogude nõuetekohast sidumist projekti struktuuris. See protsess tagab, et kohandatud elemendid jäävad eri projekteerimissessioonidel kättesaadavaks ja neid saab hõlpsasti jagada teiste meeskonnaliikmete või kaastöötajatega.


### Täiustatud disaini uurimine ja mõistmine


Lisaks lihtsale logo kohandamisele pakub KiCad võimsaid tööriistu keeruliste trükkplaadi disainide uurimiseks ja mõistmiseks. Kihtide haldussüsteem võimaldab kasutajatel valikuliselt vaadata disaini erinevaid aspekte, alates komponentide paigutusest ja marsruutimisest kuni tootmisspetsifikaatide ja koosteteabeni. Selline kihiline lähenemine võimaldab konkreetsete disainielementide üksikasjalikku analüüsi ilma mitteseotud komponentide visuaalse segaduseta.


Jälgede marsruutimise analüüs on trükkplaatide uurimise üks kõige harivamaid aspekte, mis näitab, kuidas elektrilised ühendused voolavad komponentide ja allsüsteemide vahel. Üksikute jälgede või seotud signaalide rühmade jälgimisega saavad kasutajad arendada arusaamist vooluahela funktsionaalsusest ja projekteerimisotsustest. Näiteks näitab toitevõrkude uurimine, kuidas pinge reguleerimine ja filtreerimiskomponendid töötavad koos, et tagada puhas ja stabiilne toide tundlikele elektroonikakomponentidele.


Seos skeemikujunduse ja füüsilise paigutuse vahel ilmneb komponentide paigutuse ja marsruutimisotsuste hoolika uurimise kaudu. Mõistmine, miks konkreetsed komponendid on paigutatud konkreetsetesse kohtadesse, kuidas termilised kaalutlused mõjutavad paigutusotsuseid ja kuidas signaalide terviklikkuse nõuded mõjutavad marsruutimisvalikuid, annab väärtusliku ülevaate professionaalsetest PCBde projekteerimistavadest. Need teadmised osutuvad hindamatuks kasutajatele, kes arendavad oma projekte või muudavad olemasolevaid projekte konkreetsete rakenduste jaoks.


KiCad'i põhjalikud projekteerimisreeglite kontrolli- ja verifitseerimisvahendid tagavad, et muudatused säilitavad elektri- ja tootmissobivuse. Need automaatsed süsteemid aitavad vältida tavalisi projekteerimisvigu, õpetades samal ajal kasutajatele tööstusstandardeid ja parimaid tavasid. 3D-visualiseerimise integreerimine elektriliste projekteerimisandmetega loob võimsa õpikeskkonna, kus teoreetilised mõisted muutuvad käegakatsutavaks visuaalse kujutamise ja interaktiivse uurimise kaudu.


## Kuidas luua tehase faili?

<chapterId>e9da631c-e6d1-50c1-bb59-bc8455c29d3e</chapterId>


:::video id=07f980bf-6052-4ed4-bf7b-75e8aba585df:::

ESP-põhiste mining-seadmete jaoks kohandatud püsivara loomine nõuab hoolikat tähelepanu konfiguratsioonile, sõltuvustele ja nõuetekohasele koostamisprotsessile. Selles põhjalikus juhendis vaadatakse läbi nii standardse püsivara binaarsete failide kui ka tehases loodud failide loomise täielik protsess, mis sisaldab eelkonfigureeritud seadistusi, mis muudab kasutuselevõtu tõhusamaks ja vähendab lõppkasutajate seadistamisaega.


Pange tähele, et see peatükk on üsna tehniline ja selle võib lihtsalt läbi sirvida, kui olete selle kohta uudishimulik.


### Arenduskeskkonna seadistamine


ESP-Miner püsivara arendamise alustamiseks peaksite looma sobiva arenduskeskkonna Visual Studio Code'is, ideaalis linuxi distributsioonis. Selle seadistuse nurgakiviks on ESP-IDF laiendus, mis pakub ESP32 arendamiseks vajalikke vahendeid ja raamistiku integreerimist. ESP-IDF laienduse esmakordsel paigaldamisel leiavad kasutajad seadistusjuhendi, mis hõlbustab seadistamisprotsessi.


Kriitiline kaalutlus seadistamisprotsessis hõlmab sobiva ESP-IDF-versiooni valimist. Kuigi varem soovitati versiooni 5.1.3, on praktiline kogemus näidanud, et see versioon võib põhjustada probleeme, mis raskendavad arendusprotsessi. Nüüd soovitatakse kasutada ESP-IDF-i versiooni 5.3 Beta 1, mis on osutunud lahendavaks nende komplikatsioonide kõrvaldamiseks ja tagab Bitaxe'i seadmete nõuetekohase toimimise. Paigaldusprotsessis tuleb valida Express paigaldamise võimalus ja valida olemasolevate valikute hulgast konkreetselt versioon 5.3 Beta 1.


Arenduskeskkonna seadistamine ulatub ESP-IDF-i paigaldamisest kaugemale ja hõlmab ka terminali nõuetekohast konfigureerimist. Visual Studio Code pakub ESP-IDF-i funktsioonidele juurdepääsu mitut meetodit, sealhulgas käsupaleti valikut ESP-IDF-i terminali avamiseks või kasutajaliideses asuva spetsiaalse terminali ikooni kasutamist. See spetsiaalne terminalikeskkond tagab, et kõik ESP-IDF-i käsud toimivad õigesti, ja annab juurdepääsu kogu tööriistakomplektile.


### ESP-Miner seadete konfigureerimine


Konfiguratsioonifail on ESP-Miner kohandamisprotsessi süda, mis sisaldab kõiki olulisi parameetreid, mis määravad, kuidas seade sihtkeskkonnas töötab. See konfiguratsioon hõlmab võrguseadistusi, mining koondühendusi ja riistvaraspetsiifilisi parameetreid, mis tuleb kohandada konkreetse kasutuselevõtu stsenaariumiga.


Võrgukonfiguratsioon on seadistamisprotsessi peamine osa, mis nõuab Wi-Fi-levi volituste, sealhulgas SSID ja parooli määramist. Tootmiskonfiguratsioonid peaksid sisaldama tegelikke võrgukrediteeringuid, mida seade kasutab töökeskkonnas, selle asemel, et kasutada paigutusväärtusi nagu "test". Konfiguratsioon võimaldab ka erinevaid mining-poolseadistusi, toetades nii erapoolikonfiguratsioone konkreetsete IP-aadressidega kui ka avalikke pooli nagu public-pool.io koos vastavate portide seadistustega.


Mining-spetsiifiliste konfiguratsiooniparameetrite hulka kuulub stratum user setting, mis tavaliselt vastab Bitcoin aadressile, kuhu mining preemiad tuleb suunata. Täiendavad riistvaraparameetrid, nagu sageduse seaded, pingekonfiguratsioonid ja ASIC tüübispetsifikatsioonid, peavad olema vastavuses sihtriistvaraplatvormiga. GitHubi repositooriumis on erinevate riistvaravariantide jaoks eelkonfigureeritud näited, näiteks Super-seadmete jaoks mõeldud BM1368 konfiguratsioon ja Ultra-variantide jaoks mõeldud BM1366 seaded. Plaadi versiooni spetsifikatsioonid, näiteks pordiversiooni seadistamine 401-le uuemate riistvaraversioonide puhul, tagavad ühilduvuse sihtseadme spetsiifiliste omadustega.


### Veebi Interface ja põhifirmavara koostamine


Projekt ESP-Miner sisaldab keerukat veebiliidest, mis nõuab eraldi kompileerimist, enne kui saab alustada põhilise püsivara koostamise protsessi. See veebiliides, mida nimetatakse AxeOS firmware'ks, pakub kasutajatele terviklikku haldusliidest mining seadmete jälgimiseks ja juhtimiseks.


Veebiliidese loomise protsess algab HTTP-serveri kataloogi navigeerimisega peamise repositooriumi struktuuris, täpsemalt AxeOS alamkataloogis. See asukoht sisaldab Node.js-põhist veebirakendust, mis nõuab sõltuvuste paigaldamist käsu npm install abil. Ehitussüsteem eeldab, et Node.js on arendussüsteemis korralikult installitud, kuna see on veebiliidese koostamise protsessi põhinõue.


Pärast sõltuvuste paigaldamist koostab käsk npm run build veebiliidese komponendid, luues vajalikud failid, mis lisatakse ESP32 püsivara sisse. See kompileerimisprotsess genereerib optimeeritud veebivarad, mis pakuvad kasutajaliidese funktsionaalsust, säilitades samal ajal tõhusa mälukasutuse piiratud ESP32 platvormil. Selle koostamisetapi edukas lõpuleviimine on oluline enne põhilise püsivara koostamise jätkamist, kuna ESP-Miner püsivara sisaldab neid veebiliidese komponente lahutamatu funktsioonina.


### Tehasefailide loomine sisseehitatud konfiguratsiooniga


Tehasefailide loomine kujutab endast täiustatud kasutuselevõtustrateegiat, mis paigutab konfiguratsioonisätted otse püsivara binaarsüsteemi, kõrvaldades seadme seadistamise ajal manuaalse konfigureerimise vajaduse. See lähenemisviis on eriti väärtuslik suuremahuliste juurutuste puhul või olukordades, kus on oluline mitme seadme järjepidev konfigureerimine.


Tehasefaili loomise protsess algab konfiguratsioonibinaari genereerimisega CSV-konfiguratsioonifailist, kasutades ESP-IDF-i NVS partitsiooni genereerimise tööriista. See tööriist, mis asub ESP-IDF-i komponentide kataloogis nvs-flash/nvs-partition-generator, teisendab inimesele loetava konfiguratsiooni otseseks flash-mälu salvestamiseks sobivasse binaarvormingusse. Skript nvs-partition-gen.py töötleb faili config.csv ja genereerib faili config.binary, mis on suunatud 0x6000 mälu aadressiruumi.


Tehasefailide lõplikuks kokkupanekuks kasutatakse spetsiaalseid ühendamisskripte, mis ühendavad püsivara tuumikprogrammide binaarsed failid konfiguratsiooniandmetega. Hoidla pakub mitmeid ühendamisvõimalusi, sealhulgas standardset ühendamisskripti põhiliste tehasespetsiifiliste failide jaoks ja konfiguratsiooni sisaldavat ühendamisskripti põhjalike tehasespetsiifiliste failide jaoks. Skript merge-bin-with-config.sh loob tehasefailid, mis sisaldavad nii püsivara funktsionaalsust kui ka eelkonfigureeritud seadeid, mille tulemuseks on täielik juurutamispakett. See lähenemisviis võimaldab luua seadmespetsiifilisi tehasefaile, näiteks Bitaxe Ultra seadmetele kohandatud versioone, millel on spetsiifilised plaadi versioonid, säilitades samas paindlikkuse generate üldiste tehasefailide loomiseks ilma sisseehitatud konfiguratsioonita stsenaariumide jaoks, mis nõuavad manuaalset seadistamise paindlikkust.


Valmis tehasfailid annavad juurutamismeeskondadele valmis flash-binaarid, mis sisaldavad kõiki vajalikke püsivara komponente ja konfiguratsiooniseadistusi, lihtsustades seadme kasutuselevõtu protsessi ja tagades ühtsed tööparameetrid kõigis juurutatud mining seadmetes.


## Kuidas kasutada Bitaxe Web Flasherit?

<chapterId>8c3e2d4c-c038-53ec-93cb-cc30a29e4394</chapterId>


:::video id=291757b9-f459-48f6-8766-56387f907859:::

Bitaxe Web Installer kujutab endast lihtsustatud lähenemist Bitaxe'i seadmete püsivara haldamisele, pakkudes kasutajatele veebipõhise kasutajaliidese kaudu mitmeid paigaldusvõimalusi. See terviklik vahend kõrvaldab keerukuse, mis on tavapäraselt seotud püsivara uuendamise ja uue paigaldamisega, muutes seadme haldamise kättesaadavaks kasutajatele sõltumata nende tehnilistest teadmistest. Selle paigaldusprogrammi õige kasutamise mõistmine on äärmiselt oluline, et säilitada seadme optimaalne jõudlus ja vältida tavalisi lõkse, mis võivad muuta seadmed ajutiselt kasutuskõlbmatuks.


### Juurdepääs ja brauseri ühilduvusnõuded


Bitaxe Web Installer on kättesaadav spetsiaalse URL-i [https://bitaxeorg.github.io/bitaxe-web-flasher/](https://bitaxeorg.github.io/bitaxe-web-flasher/) kaudu (videos esitatud URL on nüüdseks aegunud), mis on kõigi püsivara paigaldamistoimingute keskne keskus. Selle veebipõhise tööriista edukas kasutamine eeldab siiski brauseri ühilduvust, kuna paigaldaja tugineb spetsiifilistele veebitehnoloogiatele, mida kõik brauserid ei toeta. Chrome on paigaldusprogrammi jaoks peamine soovitatav brauser, mis tagab täieliku ühilduvuse kõigi funktsioonide ja funktsioonidega. Kuigi teised Chromiumil põhinevad brauserid võivad pakkuda sarnast funktsionaalsust, puuduvad populaarsetel alternatiividel, nagu Brave ja Firefox, vajalik veebiseeria API tugi, mistõttu need ei ühildu paigaldaja põhitoimingutega.


See brauseripiirang tuleneb sellest, et paigaldaja tugineb veebiliidese kaudu Bitaxe'i seadmetega otsesele jadaühendusele. Veebisarja API, mis võimaldab sellist suhtlust, on endiselt suhteliselt uus veebistandard, mis ei ole veel saavutanud universaalset brauserite kasutuselevõttu. Kasutajad, kes üritavad paigaldusprogrammile juurdepääsu mitte toetatud brauserite kaudu, puutuvad kokku ühenduse katkemisega ja ei saa oma seadmetega suhelda, mistõttu on vaja enne paigaldustegevusega jätkamist minna üle ühilduvale brauserile.


### Toitenõuded ja seadme ettevalmistamine


Bitaxe'i seadmetel on sõltuvalt nende konkreetsest mudelist ja versioonist erinevad energiavajadused, mistõttu nõuetekohane energiakasutuse juhtimine on püsivara edukaks paigaldamiseks hädavajalik. Seadmed, mille versioon on 204 või väiksem, võivad töötada ainult USB-toite kaudu, võttes ühendatud arvutist piisavalt voolu, et säilitada töö vilkumisprotsessi ajal. Selline lihtsustatud toitekorraldus muudab need varasemad versioonid püsivara uuendamiseks eriti mugavaks, kuna kasutajad peavad paigaldusprotsessi alustamiseks ühendama vaid ühe USB-kaabli.


Seadmed, mis töötavad versiooniga 205 ja sellest ülespoole, vajavad lisaks USB-ühendusele ka väliseid toiteallikaid, mis kajastab muudatusi energiatarbimises ja vooluahela konstruktsioonis uuemates riistvara versioonides. Need seadmed ei saa piisavat energiat ainult USB kaudu, mistõttu on vaja püsivara paigaldamise ajal ühendada need standardse toiteallikaga. Kui neid uuemaid seadmeid ei varustata piisava toiteallikaga, põhjustab see installeerimise tõrkeid ja võimalikke rikkumisi püsivara uuendamise protsessis.


Füüsiline ühendamisprotsess nõuab spetsiifilist ajastust ja nuppudega manipuleerimist, et tagada nõuetekohane side paigaldaja ja seadme vahel. Kasutajad peavad enne USB-C kaabli ühendamist arvutiga vajutama ja hoidma all Bitaxe seadme käivitamisnuppu. See järjestus paneb seadme alglaadimisrežiimi, mis võimaldab paigaldajal suhelda otse seadme püsivara salvestusruumiga. USB-kaabli ühendamine enne alglaadimisnupu vajutamist toob kaasa seadme normaalse töö, mitte püsivara paigaldamiseks vajaliku alglaadimisrežiimi, mis takistab paigaldaja vajaliku sidekanali loomist.


### Paigaldamisvõimalused ja nende rakendused


Bitaxe Web Installer pakub nelja erinevat paigaldusvõimalust, millest igaüks on mõeldud konkreetsete kasutusjuhtumite ja seadmekonfiguratsioonide jaoks. Bitaxe Superboardi versioon 4.0.1 on kõige uuem püsivara Super-mudeli seadmetele, versioon 4.0.2 on kavas välja anda tulevikus. See valik sisaldab nii tehase- kui ka uuendusvariante, mis võimaldab paindlikku paigaldusviisi vastavalt kasutaja vajadustele ja seadme olekule.


Tehase paigaldamine kujutab endast täielikku püsivara asendamist, mis peegeldab algset tootmisprotsessi, sealhulgas põhjalikke enesetestimise protseduure, mis kontrollivad seadme funktsionaalsust kõigis süsteemides. Kui kasutajad valivad tehase paigalduse, kustutab paigaldaja olemasoleva püsivara ja konfiguratsiooniandmed täielikult, asendades need uue, puhta paigaldusega, mis on identne sellega, mida kasutati tootmise ajal. See protsess hõlmab automaatset enesetestimist, mis kinnitab riistvara nõuetekohast toimimist, nõudes kasutajatelt seadme taaskäivitamist pärast selle lõpetamist, enne kui seadme normaalne töö võib jätkuda. Tehaseinstallatsioon on eriti väärtuslik siis, kui seadmetel esineb püsivaid probleeme või kui kasutajad soovivad oma seadmeid taastada tehase algsete spetsifikatsioonide järgi.


Värskenduspaigaldised pakuvad konservatiivsemat lähenemist, säilitades olemasolevad konfiguratsiooniandmed, uuendades samal ajal ainult põhilisi püsivara komponente. See võimalus on ideaalne kasutajatele, kes on oma seadme seadeid kohandanud ja soovivad säilitada oma isiklikud konfiguratsioonid, saades samal ajal kasu püsivara parandustest ja veaparandustest. Värskendusprotsess on suunatud ainult muutmist vajavatele püsivara komponentidele, jättes kasutajakohased seaded, WiFi-volitused ja Bitcoin-aadressid kogu paigaldusprotsessi jooksul puutumatuks.


### Kriitilised paigaldamisega seotud kaalutlused ja andmekaitse


Tehase- ja uuenduste paigaldamise eristamine mõjutab oluliselt seadme konfiguratsiooni ja kasutajaandmete säilitamist. Tehasepaigaldiste puhul kustutatakse seade täielikult, eemaldades kõik kasutaja poolt konfigureeritud seaded, sealhulgas WiFi kasutajatunnused, Bitcoin aadressid ja kõik seadme isiklikud parameetrid. Pärast tehasepoolset paigaldamist peavad kasutajad uuesti ühenduma seadme vaikimisi WiFi-võrku ja konfigureerima kõik isiklikud seaded uuesti nullist, käsitledes seadet sisuliselt nii, nagu oleks see tootja poolt täiesti uus.


Uuenduste paigaldamine nõuab hoolikat tähelepanu seadme kustutamise valikule, mis esitatakse paigaldusprotsessi ajal. Paigaldusprogramm küsib kasutajatelt küsimust "Kas soovite seadme enne Bitaxe Flasheri paigaldamist kustutada?", millele lisandub hoiatus, et kõik seadmel olevad andmed kaovad. Kasutajad, kes teostavad uuenduste paigaldamist, peavad selle võimaluse tagasi lükkama, klõpsates "Next", mitte kinnitades kustutamistoimingut. Kustutamise valiku vastuvõtmine uuenduse paigaldamise ajal eemaldab seadme konfiguratsioonifaili, mis võib muuta seadme kuni nõuetekohase konfiguratsiooni taastamiseni mittefunktsionaalseks. Kuigi selline olukord ei kahjusta seadet jäädavalt, tekitab see tarbetuid komplikatsioone ja nõuab normaalse töö taastamiseks täiendavaid konfigureerimismeetmeid.


Paigaldusprotsess ise toimub automaatselt, kui kasutajad on teinud oma valikud ja kinnitanud need. Installeerija tegeleb kõigi püsivara ülekande ja kontrollimise tehniliste aspektidega, esitades kogu protsessi vältel edusammude indikaatorid ja olekuteadete uuendused. Selline automaatne lähenemine välistab kasutajate vajaduse mõista keerulisi püsivara paigaldusprotseduure, tagades samas usaldusväärsed ja järjepidevad tulemused erinevate seademudelite ja püsivara versioonide puhul.


## Kuidas luua ja tellida trükkplaati?

<chapterId>566f5e06-9ec9-55c0-84f6-101d6ca4c2ff</chapterId>


:::video id=9a56ad84-d9cf-4f85-ab98-301fb3101228:::

Selles peatükis keskendutakse KiCadi projektidest tootmisfailide genereerimisele ja professionaalsete trükkplaatide tellimisele veebipõhistelt tootjatelt. Kasutades näitena Bitaxe projekti, käime läbi kogu töövoo alates faili genereerimisest kuni tellimuse esitamiseni trükkplaaditootjale.


### PCB tootmisprotsessi mõistmine


Teekond valmis KiCad'i projektist füüsilise trükkplaadi valmistamiseni hõlmab mitmeid kriitilisi samme, mis ületavad lõhe digitaalse disaini ja füüsilise tootmise vahel. Kui töötate keeruliste projektidega nagu Bitaxe, pakub KiCadi trükkplaadiredaktor terviklikku ülevaadet teie disainist, näidates kõiki komponente ja nende omavahelisi ühendusi värviliste jälgede kaudu. Punased ja sinised jooned, mida näete, tähistavad elektrilisi ühendusi erinevate integraallülituste ja komponentide vahel plaadil. KiCadi 3D vaatefunktsioon võimaldab visualiseerida, kuidas lõplik kokkupandud plaat välja näeb, andes väärtusliku ülevaate komponentide paigutusest ja võimalikest mehaanilistest konfliktidest.


Tootmisprotsess nõuab konkreetseid failivorminguid, mida trükkplaaditootjad saavad tõlgendada ja kasutada teie plaatide valmistamiseks. Need failid sisaldavad täpset teavet vaskkihtide, puuraukude, komponentide paigutuse ja muude tootmisspetsifikaatide kohta. Selle töövoo mõistmine on oluline, olenemata sellest, kas töötate Bitaxe'i standardse disainiga või teete muudatusi, näiteks lisate kohandatud logosid, muudate komponentide väärtusi või kohandate plaadi paigutust, et see vastaks konkreetsetele nõuetele.


### Gerberi failide genereerimine tootmiseks


Gerber-failid on tööstusharu standardiks PCB-disaini teabe edastamisel tootjatele. Need failid sisaldavad kõiki vajalikke andmeid trükkplaadi valmistamiseks, sealhulgas vaskkihi mustreid, jootemaskide määratlusi ja puuraukude asukohti. Nende failide generate jaoks KiCadis navigeerige PCB redaktorisse ja pääsete failide menüüst juurde valmistamise väljunditele. Tarkvara konfigureerib automaatselt sobivad seaded standardsete tootmisprotsesside jaoks, sealhulgas õige väljundkataloogi struktuuri, mis on tavaliselt korraldatud kui "tootmisfailid/gerberid"


Genereerimisprotsess loob mitu Gerber-faili, millest igaüks esindab teie trükkplaadi disaini erinevaid aspekte. Need failid töötavad koos, et anda tootjatele täielikud valmistamisjuhised. Pärast genereerimist tuleb need failid pakendada ZIP-arhiivi, kuna see on standardformaat, mida enamik trükkplaaditootjaid ootab. ZIP-fail sisaldab kõiki vajalikke tootmisandmeid ja tagab, et tootja veebisaidile üleslaadimise käigus ei läheks faile kaduma ega rikneks.


Tasub märkida, et paljud avatud lähtekoodiga projektid, sealhulgas Bitaxe, sisaldavad oma repositooriumides sageli eelnevalt loodud tootmisfaile. Kuid arusaamine sellest, kuidas neid faile ise generate teha, on väga oluline, kui teete disainimuudatusi või töötate erinevate plaadiversioonidega. Need teadmised muutuvad eriti väärtuslikuks disainilahenduste kohandamisel või tootmisprobleemide lahendamisel.


### Trükkplaaditootjate valimine ja valikuvõimaluste mõistmine


Trükkplaatide tootmismaastik pakub mitmeid mainekaid võimalusi, kusjuures JLCPCB ja PCBWay on nii harrastajate kui ka professionaalide seas kõige populaarsemad valikud. Mõlemad tootjad pakuvad sarnaseid teenuseid konkurentsivõimelise hinna ja usaldusväärse kvaliteediga, kuigi mõlemal on sõltuvalt teie projekti nõuetest konkreetsed eelised. JLCPCB meelitab sageli esmakordseid kasutajaid soodushindade ja kasutajasõbralike liideste abil, samas kui PCBWay võib pakkuda erinevaid materjalivalikuid või spetsialiseeritud teenuseid.


Kui laadite oma Gerber-failid tootja veebisaidile üles, analüüsib süsteem automaatselt teie projekti ja esitab erinevaid tootmisvõimalusi. Nende platvormide pakutavad vaikimisi seaded sobivad tavaliselt enamiku standardsete disainilahenduste jaoks ja üldiselt on soovitatav neid seadistusi säilitada, kui teil ei ole erinõudeid. Peamised parameetrid on näiteks trükkplaadi paksus, vase kaal, pinnaviimistlus ja miinimumkogused. Enamik tootjaid nõuab viie plaadi miinimumtellimust, mis tegelikult töötab hästi hobikorras projektide puhul, kus varuplaatide omamine või sõpradega jagamine on kasulik.


Värvivalikud on üks vähestest esteetilistest valikutest, mis on tootmisprotsessi käigus saadaval. Kuigi roheline on endiselt traditsiooniline ja kõige kuluefektiivsem valik, pakuvad tootjad tavaliselt alternatiive, sealhulgas sinist, punast, kollast, lillat ja musta. Värvivalik on puhtalt esteetiline ja ei mõjuta teie trükkplaadi elektrilist jõudlust, kuigi mõned värvid võivad mõjutada veidi kulusid või pikemat valmistamisaega.


### Täiustatud tootmisega seotud kaalutlused ja montaaživõimalused


Lisaks põhilisele trükkplaatide valmistamisele pakuvad kaasaegsed tootjad lisateenuseid, mis võivad teie projekti lõpuleviimist märkimisväärselt lihtsustada. Šabloonid on üks kõige väärtuslikumaid lisateenuseid, eriti selliste peene sammuga komponentidega disainilahenduste puhul nagu ASIC kiibid, mida Bitcoin mining projektides leidub. Šabloon on sisuliselt täpselt lõigatud alumiiniumist šabloon, mille avad vastavad täpselt teie trükkplaadi jootekohtade kohtadele. See tööriist võimaldab jootepasta järjepidevat ja täpset pealekandmist, parandades oluliselt koostekvaliteeti ja vähendades jootevigade tõenäosust.


Šabloonide valikus on tavaliselt üksikud šabloonid nii ülemise kui ka alumise mustriga või eraldi šabloonid plaadi mõlemale küljele. Enamiku projektide puhul osutub kombineeritud šabloon mugavamaks ja kuluefektiivsemaks. Šablooni paksus on hoolikalt arvutatud, et ladestada sobiv kogus jootepastat teie konkreetsete komponentide tüüpide ja padide suuruse jaoks. Šablooni kasutamine muudab tüütu ja veaohtliku manuaalse protsessi kiireks ja professionaalseks montaažiks.


Kuigi mõned tootjad pakuvad osalist või täielikku montaažiteenust, nõuavad need võimalused Bitaxe'i-suguste keeruliste projektide puhul hoolikat kaalumist. Selle otsuse tegemisel tuleb arvestada komponentide kättesaadavust, kulude mõju ja isekomplekteerimise hariduslikku väärtust. Paljud Bitcoin mining projektide jaoks vajalikud spetsiaalsed komponendid ei pruugi olla hõlpsasti kättesaadavad tavaliste trükkplaatide koosteteenuste kaudu, mistõttu on komponentide hankimine ja käsitsi kokkupanek praktilisem lähenemisviis. Selle sarja tulevastes episoodides käsitletakse komponentide hankimisstrateegiaid ja koostetehnikaid, mis aitavad teil oma Bitaxe-projekti edukalt lõpule viia, alates paljast trükkplaadist kuni funktsionaalse seadmeni.


Tootmis- ja montaažiprotsess on oluline sild digitaalse disaini ja füüsilise rakendamise vahel. Nende töövoogude mõistmine võimaldab teil oma projekte kontrollida, vähendada kulusid ja saada väärtuslikke praktilisi kogemusi professionaalsete tootmisprotsessidega. Olenemata sellest, kas te ehitate ühe prototüübi või kavandate väikest tootmisjärjekorda, avab nende oskuste valdamine uusi võimalusi oma elektrooniliste disainilahenduste ellu viimiseks.


# Tulemuslikkuse optimeerimine

<partId>87b8790f-b7a9-5286-a7f8-328176ef7cb5</partId>


## Bitaxe võrdlusuuring

<chapterId>7259a4b1-93c1-5956-87d3-baaee58115af</chapterId>


:::video id=2491a783-9750-4ea5-a40c-1d1d611784d5:::

Optimaalse mining jõudluse saavutamine nõuab süstemaatilist lähenemist riistvara konfiguratsioonile, mis tasakaalustab hashrate, tõhusust ja soojusjuhtimist. Bitaxe pakub arvukalt konfiguratsiooniparameetreid, mis võivad jõudlust oluliselt mõjutada, kuid iga seadete kombinatsiooni käsitsi katsetamine oleks ebapraktiline ja aeganõudev. Selles peatükis uuritakse, kuidas kasutada automatiseeritud võrdlusuuringute vahendeid, et teaduslikult optimeerida oma Bitaxe'i jõudlust, säilitades samal ajal ohutud töötingimused.


### Bitaxe'i jõudlusnäitajate ja baaskonfiguratsiooni mõistmine


Enne optimeerimistehnikatesse sukeldumist on oluline mõista põhilisi tulemusnäitajaid, mis määravad teie Bitaxe'i töö tõhususe. Peamised näitajad on hashrate, mida mõõdetakse terahapides sekundis, energiatõhusus, mida väljendatakse džaulides terahapide kohta, ASIC sagedus megahertsides ja tuumapinge voltides. Hästi konfigureeritud Bitaxe võib saavutada umbes 1,1 terahashi, mille kasutegur on umbes 17 džauli terahashi kohta, töötades sagedusel 550 megahertsi ja mõõdetud ASIC pinge on 1,14 volti. Need baasnumbrid annavad võrdluspunkti, et mõista süstemaatilise optimeerimise abil saavutatavaid potentsiaalseid parandusi.


Nende näitajate vaheline suhe on keeruline ja üksteisest sõltuv. Kõrgemad sagedused suurendavad tavaliselt hashrate, kuid suurendavad ka energiatarbimist ja soojuse teket. Samamoodi mõjutavad pinge reguleerimine nii jõudlust kui ka soojusomadusi. Väljakutse seisneb optimaalse tasakaalu leidmises, mis maksimeerib kas hashrate või tõhusust, säilitades samal ajal stabiilse töö ohututes temperatuuripiirides. See optimeerimisprotsess nõuab metoodilist katsetamist mitme parameetri kombinatsiooni puhul, mistõttu on automatiseeritud vahendid optimaalsete tulemuste saavutamiseks hindamatu väärtusega.


### Bitaxe Hashrate Benchmark Tool arhitektuur


Tööriist [Bitaxe Hashrate Benchmark](https://github.com/mrv777/Bitaxe-Hashrate-Benchmark/) on keerukas Pythonil põhinev lahendus, mille algselt töötas välja WhiteCookie ja hiljem täiustas mrv777. See avatud lähtekoodiga tööriist, mida levitatakse GPLv3 litsentsi alusel, automatiseerib mitme konfiguratsioonikombinatsiooni testimise keerulise protsessi, et leida optimaalsed seaded teie konkreetse riistvara jaoks. Tööriista peamine tugevus seisneb tema süstemaatilises lähenemisviisis parameetrite testimisele, kohandades järk-järgult sageduse ja pinge seadeid, jälgides samal ajal pidevalt jõudlusnäitajaid ja termilisi tingimusi.


Võrdlusuuringu läbiviimiseks kulub tavaliselt 30-40 minutit, mille jooksul tööriist testib metoodiliselt erinevaid ASIC sageduse ja pinge seadete kombinatsioone. Tööriist alustab konservatiivsete algseadistustega, alustades tavaliselt 1,15 voltist ja 500 megahertsist, ning seejärel suurendab neid parameetreid järk-järgult, jälgides samal ajal hashrate, temperatuuri ja stabiilsust. Oluline on see, et tööriist seab ohutu töö prioriteediks maksimaalse jõudluse ees, vähendades automaatselt seadistusi, mis põhjustavad liigset soojuse teket või ebastabiilsust. Selline konservatiivne lähenemine tagab, et optimeerimisprotsess ei sea ohtu riistvara pikaealisust ega töökindlust.


### Paigaldamise ja seadistamise nõuded


Bitaxe Hashrate Benchmark'i tööriista rakendamine nõuab teie kohalikus arvutis mitut eeltingimuseks olevat tarkvarakomponenti. Peamised nõuded on Python võrdlusskriptide täitmiseks, Git hoidla haldamiseks ja valikuliselt Visual Studio Code laiendatud arenduskeskkonna võimaluste jaoks. Kuigi tööriista saab kasutada käsurea liidestest, annab integreeritud arenduskeskkonna, näiteks VS Code, kasutamine parema ülevaate võrdlusuuringu protsessist ja tulemuste analüüsist.


Paigaldusprotsess järgib Pythoni standardseid arenduspraktikaid, alustades repositooriumi kloonimisega GitHubist oma kohalikku masinasse. Kui repositoorium on alla laaditud, peate looma virtuaalse keskkonna, et isoleerida tööriista sõltuvused teie süsteemi Pythoni paigaldusest. Selline isoleerimine hoiab ära võimalikud konfliktid teiste Pythoni rakendustega ja tagab järjepideva töö. Pärast virtuaalkeskkonna aktiveerimist paigaldate vajalikud sõltuvused, kasutades kaasasolevat nõuete faili, mis konfigureerib automaatselt kõik vajalikud raamatukogud ja moodulid tööriista nõuetekohaseks toimimiseks.


### Võrdlusuuringute teostamine ja tulemuste tõlgendamine


Võrdlusuuringu käivitamiseks on vaja käivitada üks Python-käsk, mis sisaldab parameetrina teie Bitaxe'i IP-aadressi. Tööriist loob automaatselt ühenduse teie kaevuri veebiliidesega ja alustab süstemaatilist testimisprotsessi. Tööriist annab täitmise ajal üksikasjalikku logiteavet, mis näitab praegust testimise kordust, rakendatud pinge- ja sageduse seadistusi, saadud hashrate, sisendpinget, temperatuuri näitu ja kriitiliste komponentide, näiteks buck-muunduri termilisi andmeid. See reaalajas tagasiside võimaldab teil jälgida võrdlusuuringu edenemist ja mõista, kuidas erinevad seadistused mõjutavad teie kaevuri jõudlust.


Tööriista intelligentne soojusjuhtimine ilmneb, kui temperatuur läheneb 66-kraadisele ohutuspiirile. Selle asemel, et ületada ohutuid tööpiire, vähendab võrdlusalus automaatselt seadistusi, et säilitada termiline stabiilsus. See konservatiivne lähenemisviis tagab, et optimeerimisprotsessis seatakse riistvara pikaajaline töökindlus lühiajalise jõudluse kasvu asemel esikohale. Tööriist genereerib pärast lõpetamist põhjalikud tulemused JSON-vormingus, reastades viis parimat konfiguratsiooni nii maksimaalse hashrate kui ka optimaalse tõhususe osas. Need tulemused annavad selgeid juhiseid, et valida konfiguratsioon, mis vastab kõige paremini teie tegevusprioriteetidele, olenemata sellest, kas keskendutakse maksimaalsele võimsusele või energiatõhususele.


Võrdlustööriist pakub ka kohandamisvõimalusi edasijõudnud kasutajatele, kes soovivad testimise parameetreid muuta. Käsurea argumendid võimaldavad määrata kohandatud algpinged ja sagedused, mis võimaldab konkreetsete kasutusjuhtumite jaoks sihipärasemat optimeerimist. Näiteks kui te juba teate, et teie riistvara töötab hästi kõrgematel sagedustel, võite võrdlusuuringut alustada konservatiivsete vaikimisi seadistuste asemel kõrgendatud seadistustega. Selline paindlikkus muudab tööriista väärtuslikuks nii automaatset optimeerimist otsivatele algajatele kui ka kogenud kaevuritele, kes soovivad täpsustada konkreetseid jõudlusomadusi.


## Bitaxe'i ületaktimine

<chapterId>6b48c0c6-51c3-51a3-b317-850a374ae61e</chapterId>


:::video id=46c7a442-cd72-477c-8c91-b2c489ada1e6:::

Bitaxe-seadme ületaktimine nõuab hoolikat arvestamist nii riistvara piirangute kui ka jahutusnõuetega. Kuigi paljud kasutajad eelistavad oma seadmeid vaiksema töö tagamiseks alataktida, on õige ületaktimise tehnika mõistmine oluline neile, kes soovivad maksimaalset jõudlust ilma riistvara kahjustamata. Protsess hõlmab sageduse suurendamist ja võimalikku pinge seadete kohandamist üle tehase spetsifikatsioonide, mis suurendab soojuse teket ja komponentide koormust.


Eduka ületöötluse aluseks on piisav jahutusinfrastruktuur. Enne sageduse muutmise katsetamist peate tagama, et teie Bitaxe'ile on tagatud nõuetekohane soojuse hajutamise võimekus. Bitaxe Gamma koos kvaliteetse jahutusaluse ja ventilaatoriga tagab ohutu ületaksimise jaoks vajaliku soojusjuhtimise. Väikeste jahutusaluste ja ebapiisavate ventilaatoritega seadmeid ei tohiks üle taktitada, sest kehv jahutusjõudlus põhjustab termilist drosseldamist ja võimalikku riistvara kahjustamist. Soojuse ja komponentide pikaealisuse vahelist seost on oluline mõista - liigne soojus tekitab stressi, mis aja jooksul lagundab elektroonikakomponente, vähendades märkimisväärselt teie seadme kasutusiga.


### Strateegiline jahutusradade paigutus


Kõige kriitilisem komponent, mis vajab täiendavat jahutust, on buck converter, väike must komponent, mis asub Bitaxe'i tagaküljel suure mähise lähedal. See seade muundab sissetuleva 5 V toiteallika ASIC kiibi jaoks sobivaks pingeks, tavaliselt umbes 1,2 V. Buck-muundur, mida sageli nimetatakse TPS-iks, tekitab töö ajal märkimisväärset soojust ja kujutab endast termilist kitsaskohta, mis piirab ületaktimisvõimalusi. Väikese kleepuva jahutusaluse paigaldamine sellele komponendile ei võimalda mitte ainult suuremat ületaktimisruumi, vaid parandab ka üldist tõhusust, vähendades soojuskaotusi.


Täiendav jahutusplaadi paigutus võib olla kasulik ka muudele suure voolutugevusega aladele plaadil. Pinge reguleerimise vooluahelat koormab oluliselt, kuna vool voolab sisendosast läbi mitmesuguste plaadi jälgede alla, et varustada ASIC kiipi. Paljud kogenud ülitaktimootorid paigaldavad Bitaxe'i esiküljele nendesse suure voolutugevusega piirkondadesse jahutusradade täiendavaks parandamiseks jahutusradasid. Kuigi need täiendavad jahutusmeetmed ei ole mõõduka ületöötluse puhul tingimata vajalikud, muutuvad nad oluliseks, kui sagedused on ekstreemselt kõrged.


### Jahutussüsteemi kaalutlused ja piirangud


ESP32 kontroller, mis on plaadil nähtav hõbedase komponendina, ei vaja tavaliselt täiendavat jahutust. See komponent toodab iseseisvalt minimaalselt soojust ja soojeneb ainult ümbritsevate komponentide soojusülekande tõttu. Kui ESP32 lähedale paigaldatakse jahutusradiaatorid, võib see häirida kõrval asuvat Wi-Fi antenni, mis halvendab traadita ühendust ja signaali kvaliteeti. Keskenduge jahutamisel pigem voolureguleerimise komponentidele ja ASIC piirkonnale kui juhtimisahelale.


Kahe ventilaatori konfiguratsioonid pakuvad nii võimalusi kui ka piiranguid. Kuigi teise ventilaatori lisamine õhu puhumiseks üle Bitaxe'i tagakülje võib parandada jahutustõhusust, saab seadme püsivara juhtida ainult ühte ventilaatorit korralikult. Bitaxe'il on kaks ventilaatorite päistikku, kuid ainult üks ventilaatorite kontroller, mis tähendab, et kahe ventilaatori ühendamine ajab püsivara segadusse, kuna see saab vastuolulisi pöörlemissignaale. Selline konfiguratsioon toimib, kuid võib põhjustada ventilaatorite kontrollimisel ettearvamatut käitumist.


### Põhitegevuse hindamine


Enne ületaktimise muutmise katsetamist määrake baasnäitajad, käivitades oma Bitaxe'i mitu tundi algseadistustel. Jälgige ASIC temperatuuri, pingeregulaatori temperatuuri ja ventilaatori kiiruse protsenti veebiliidese kaudu. Optimaalne töötemperatuur peaks hoidma ASIC temperatuuril alla 60 °C ja pingeregulaatori temperatuuril alla 60 °C tavatingimustes. Kui teie seade töötab juba üle 65 °C ASIC puhul või 70-80 °C pingeregulaatori puhul algseadete juures, on enne ületaktimise jätkamist kohustuslik täiendav jahutusriistvara.


Sageduse süstemaatiline suurendamine hõlmab astmelisi samme, kasutades seadete menüüs eelnevalt määratud sageduse valikuid. Alustage, valides järgmise võimaliku sageduse sammu, mis on suurem kui teie praegune seadistus, säilitades samal ajal vaikimisi tuumapinge. See konservatiivne lähenemisviis võimaldab teil enne täiendavate muudatuste tegemist hinnata termilist ja stabiilsuse mõju. Laske seadmel töötada iga uue sageduse seadistuse juures vähemalt 30 minutit kuni üks tund, jälgides kogu hindamisperioodi jooksul temperatuuri suundumusi ja hash-kiiruse stabiilsust.


### Täiustatud kohandatud konfiguratsioon


Juurdepääs kohandatud sageduse ja pinge seadetele eeldab täiustatud ületaktimisliidese lubamist, lisades seadme veebiliidese URL-ile "?OC". See avab käsitsi sisestatavad väljad täpseks sageduse ja pinge kontrollimiseks, millele on lisatud asjakohased hoiatused ettenähtud parameetrite ületamise ohtude kohta. Kohandatud kasutajaliides võimaldab peenhäälestust, mis ulatub kaugemale standardsetest sagedussammudest, võimaldades kogenud kasutajatel optimeerida jõudlust oma konkreetsete jahutuskonfiguratsioonide jaoks.


Kohandatud seadete kasutamisel säilitage konservatiivne sammu suurus 10-15 MHz ühe reguleerimisastme kohta. Selline metoodiline lähenemine hoiab ära järsud soojuspiigid ja võimaldab nõuetekohast stabiilsuse testimist igal sagedustasemel. Mõned edasijõudnud kasutajad saavutavad sagedusi umbes 700 MHz, kui südamiku pinge on reguleeritud 1,175 V-ni või sarnaste väärtustega, kuid need äärmuslikud seadistused nõuavad ulatuslikke jahutusmuudatusi ja hoolikat jälgimist. Pingeregulaator võib töötada temperatuuril kuni 100 °C ilma kohese kahjustuseta, kuid kõrgemad temperatuurid vähendavad tõhusust ja pikaajalist töökindlust. Edukas ületaktimine nõuab kannatlikkust, süstemaatilist testimist ja pidevat jälgimist, et saavutada stabiilne jõudluse paranemine, säilitades samal ajal riistvara terviklikkuse.


# Lõplik osa

<partId>33367393-17a7-58d4-8359-79fffc6221fb</partId>


## Hinnake seda kursust

<chapterId>785f8b92-c8a6-5a65-aa39-e9753a7edf51</chapterId>

<isCourseReview>true</isCourseReview>

## Kokkuvõte

<chapterId>758baee6-2404-56fb-b534-6a39e441ae29</chapterId>

<isCourseConclusion>true</isCourseConclusion>