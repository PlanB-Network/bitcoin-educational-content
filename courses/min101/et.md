---
name: Sissejuhatus Bitcoin mining
goal: Bitcoin mining ja proof-of-work mõistmine algusest peale
objectives: 


  - Mõista proof-of-work ja selle rolli Bitcoin-s.
  - Analüüsige raskuste reguleerimise mehhanismi.
  - Teadke, mida mining-ga seotud tehnilised terminid tegelikult tähendavad.
  - Kirjeldage Bitcoin ploki ja selle komponentide ehitamise etappe.
  - Tuvastage mining tööstuse peamised arengud.


---

# Avastage Bitcoin mining põhialused



proof of work mõistmine tähendab Bitcoin toimimise mõistmist. Ilma selle leiutiseta ja selle geniaalse kasutamiseta ei oleks Bitcoin lihtsalt olemas olnud. See kursus annab teile kogu mining teooria, mida vajate oma bitcoini teekonnal.



MIN 101 on suunatud eelkõige algajatele, sest selles selgitatakse kõik mõisted täpselt algusest peale. Kui teil on aga juba keskastme teadmised, võimaldab see kursus teil oma arusaamist kinnistada, parandada mõningaid ligikaudseid intuitsioone ja uurida üksikasju, mis peamistest selgitustest sageli puudu jäävad.



Selle kursuse lõpuks suudate te selgitada, kuidas proof-of-work töötab lihtsalt ja täpselt. MIN 101 on ka ideaalne sissejuhatus kõigisse teistesse Bitcoin mining-le pühendatud edasijõudnute kursustesse Plan ₿ Academy kohta, olgu need siis teoreetilised või praktilised.



+++


# Sissejuhatus


<partId>041ff0fa-53c3-4d55-9888-d7840de283e9</partId>



## Kursuse ülevaade


<chapterId>a82d49dc-d68a-4e3f-985e-bcef6643677e</chapterId>



Tere tulemast MIN 101 kursusele, kus te avastate mining ja Proof-of-Work teoreetilised põhimõisted Bitcoin süsteemis. See kursus on esimene samm teie bitcoineri teekonnal, et mõista, kuidas mining töötab. Kui olete selle läbinud, saate edasi liikuda edasijõudnute teooria kursuste juurde või saada praktilise tööga hakkama ja hakata ise bitcoini kaevandajaks!



Sellel MIN 101 kursusel ei hakka me Bitcoin põhimõisteid uuesti läbi käima, sest me läheme otse asja tuuma juurde: mining. Kui te ei ole kunagi kuulnud Bitcoin-st või kui selle põhialused on teile veel veidi ebaselged, siis soovitan tungivalt alustada meie sissejuhatavast BTC 101 kursusest. Kui olete need põhitõed omandanud, saate julgelt tegeleda MIN 101-ga:



https://planb.academy/courses/2b7dc507-81e3-4b70-88e6-41ed44239966


### 1. osa - Sissejuhatus



Alustame seda kursust vabatahtliku esimese peatükiga, milles pakun väga lihtsustatud selgitust mining kohta, et anda teile selge vaimne pilt enne tehniliste mehhanismide käsitlemist.



Eesmärk ei ole anda teile kõiki tehnilisi üksikasju (need tulevad hiljem kursuse käigus), vaid anda teile suunav teema. Kui see raamistik on paigas, sobitub iga edasijõudnud kontseptsioon, mida hiljem tutvustatakse, loomulikult sellesse struktuuri.



### 2. osa - Kuidas proof of work töötab



Pärast sissejuhatust on 2. osa koolitusprogrammi tehniline alus. Selle eesmärk on selgitada samm-sammult, kuidas Bitcoin toodab kehtivaid plokke. Alustame ploki struktuuri avastamisega, enne kui läheme proof-of-work mehhanismi juurde: sihtmärgi, nonce'i ja hash-funktsiooni roll. Lõpuks näeme, kuidas Bitcoin suudab tänu raskuse reguleerimise mehhanismile säilitada stabiilse plokitootmise kiiruse, vaatamata muutustele hash-võimsuses. Selle osa lõpus on teil täielik arusaam Bitcoin proof-of-worki põhiprintsiipidest.



### 3. osa - Bitcoin mining stiimulite süsteem



Kolmandas osas vaatleme, miks kaevandajaid julgustatakse ausalt osalema mining-s. Me kirjeldame üksikasjalikult plokkide tasu põhimõtet, selle koostist ja arvutusmeetodit, selle arengut ajas läbi poolituste ning coinbase'i tehingu erilist rolli.



### 4. osa - Bitcoin mining tööstus



Neljandas osas viiakse mining tagasi oma tegevusreaalsusesse. Selles jälgitakse mining masinate arengut Bitcoin algusest kuni kaasaegse ASIC-ni, et mõista praeguseid riistvaralisi piiranguid. Samuti vaatleme mining poolide põhitõdesid, et mõista, kuidas kaevurid suudavad vähendada oma sissetulekute varieeruvust.



### 5. osa - Lõpposa



Kursuse lõpuosas saate oma teadmisi mining kohta proovile panna diplomi andmisega.



Selle MIN 101 kursuse eesmärk on seega võimaldada teil lahkuda selge, struktureeritud ja püsiva arusaamaga Bitcoin mining kohta nii tehniliselt kui ka majanduslikult.



Kas olete valmis avastama Bitcoin mining? Alustame!




## Bitcoin mining lihtsaks tehtud


<chapterId>278577a6-98bb-4659-86c7-f6c4f6d5fa3e</chapterId>



Enne kui liigume Bitcoin [mining](https://planb.academy/resources/glossary/mining) üksikasjaliku ja tehnilisema selgituse juurde, tahaksin anda teile ülevaate põhimõttest, mis on teadlikult lihtne ja skemaatiline. Kui teil on juba mõningad põhiteadmised olemas, saate pärast viktoriiniküsimustele vastamist järgmises peatükis otse asja tuumani minna. See peatükk on mõeldud eelkõige algajatele, et anda teile õrnalt alustuseks.



Kujutage Bitcoin ette kui suurt avalikku märkmikku, mida kõik jagavad ja kuhu me paneme kirja, kes kellele bitcoine saatis. Seda märkmikku nimetatakse [plokiahelaks](https://planb.academy/resources/glossary/blockchain). See ei saa olla ainult ühe inimese käes, sest muidu peaks seda usaldama. Selle asemel töötab Bitcoin kollektiivselt: tuhanded arvutid kontrollivad ja haldavad sama versiooni sellest märkmikust.



![Image](assets/fr/049.webp)



Bitcoins loote makse tegemisel [tehingu](https://planb.academy/resources/glossary/transaction-tx). Seda tehingut ei lisata koheselt märkmikusse. See saadetakse kõigepealt võrku, seejärel oodatakse, kuni see integreeritakse järgmisesse tehingupaketti. Seda paketti nimetatakse [plokiks](https://planb.academy/resources/glossary/block).



![Image](assets/fr/050.webp)



Blokk on lihtsalt tehingute kogum, mis on rühmitatud kokku. Kui plokk on valmis, ei piisa selle avaldamisest. Peate tõestama võrgule, et plokk on väärt, et seda koondisse lisada. Siinkohal tuleb mängu mining.



Mining on töö, mille käigus valideeritakse plokk energiat tarbides. [Kaevandajateks](https://planb.academy/resources/glossary/miner) kutsutud tegutsejad kasutavad spetsiaalseid arvuteid. Need masinad tarbivad elektrienergiat, et teha väga palju katseid, kuni nad leiavad tõendi, mille võrk aktsepteerib. Kui kaevandaja leiab selle tõendi, loetakse tema plokk kehtivaks.



Kui plokk on valideeritud, edastatakse see võrku. Teised [sõlmed](https://planb.academy/resources/glossary/node) kontrollivad kiiresti, kas see vastab reeglitele, ja lisavad selle seejärel eelmiste plokkide jadasse. Seepärast nimetatakse seda "plokiahelaks": iga uus plokk tuleb järjestikku teiste järel ja see ahel kasvab vähehaaval.



![Image](assets/fr/051.webp)



Kokkuvõttes luuakse kõigepealt tehingud. Seejärel rühmitatakse need plokkidesse. Seejärel valideerib kaevandaja selle ploki, tarbides selleks elektrit. Lõpuks lisatakse see plokk plokiahelasse ja selles sisalduvad tehingud [kinnitatakse](https://planb.academy/resources/glossary/confirmation).



Kui kaevurid tarbivad elektrit, siis mitte sellepärast, et nad on vabatahtlikud. Nad teevad seda sellepärast, et nad saavad selle eest [tasu](https://planb.academy/resources/glossary/transaction-fees). Kui kaevur valideerib ploki, saab ta kahte liiki tulu. Ühest küljest saab ta äsja loodud bitcoine. Teisest küljest kogub ta kasutajate poolt plokis sisalduvate tehingute eest makstud tasu. Teisisõnu, kaevandaja saab hüvitist nii programmeeritud raha väljaandmise kui ka turu poolt määratud tehingutasude kaudu.



Selles etapis antakse teile teadlikult väga lihtne vaade mining-le. Selles ei selgitata veel, kuidas plokk on üksikasjalikult üles ehitatud või kuidas täpselt töötab tõestus, mida kaevurid otsivad, või kuidas Bitcoin hoiab ühtlast tempot, või kuidas tasu täpselt arvutatakse või kuidas seda nõutakse. See on okei, see on kõik, mida me selle MIN 101 kursuse lõpuosas näeme!



Selle peatüki eesmärk oli lihtsalt anda teile selge vaimne struktuur: tehingud → plokid → mining → plokiahelad → tasu. Hoidke seda ideede ahelat meeles. Ülejäänud kursuse jooksul lisatakse igas peatükis ühe neist elementidest tehnilise detaili kiht, kuni saate aru mitte ainult sellest, mis toimub, vaid ka sellest, kuidas ja miks see toimib usaldusväärselt, mastaapselt, ilma ülemuseta ja ilma usaldust vajamata.



# Kuidas proof of work töötab


<partId>e917e8e3-37f2-46fb-91b2-6a5ce6f0f5c3</partId>



## Bitcoin tehingutee


<chapterId>3b7a3502-4814-4554-8de1-86ac961a2958</chapterId>



Selleks, et mõista, mida Bitcoin mining endast kujutab, peame kõigepealt jälgima tüüpilise Bitcoin tehingu kulgu. See näitab teile täpselt, kus plokk mängu tuleb ja miks see on süsteemi keskmes. Seda tahaksin teile selles esimeses peatükis selgitada.



Bitcoins on tehing andmestruktuur, mis annab bitcoinide omandiõiguse ühelt kasutajalt teisele üle. Konkreetselt öeldes tarbib see "väljundeid" varasematest tehingutest (nn [UTXO](https://planb.academy/resources/glossary/utxo)), viidates neile kui "sisenditele", ja loob seejärel uued "väljundid", mis määravad, kellele need bitcoinid nüüd kuuluvad ja millistel tingimustel saab neid hiljem kulutada.



![Image](assets/fr/001.webp)



Bitcoin oluline punkt on kulutuste lubamine. Bitcoin ei ole kontol, nagu teie raha pangas võib olla, vaid on lukustatud kulutamistingimustega. Kui [wallet](https://planb.academy/resources/glossary/wallet) soovib kasutada UTXO [sisendina](https://planb.academy/resources/glossary/input), peab ta esitama krüptograafilise tõendi, et tal on õigus seda avada. See tõend on sageli [digitaalallkirja](https://planb.academy/resources/glossary/digital-signature) generated kujul, mis on saadud [privaatvõttest](https://planb.academy/resources/glossary/private-key). Seepärast nõuavad bitcoin'id oma privaatvõtmete kindlustamist: just need on need, mis vabastavad juurdepääsu teie bitcoinidele ja võimaldavad teil järelikult neid kulutada.



![Image](assets/fr/002.webp)



Bitcoin digitaalallkirjal on kaks olulist rolli:




- Kulutuste lubamine: see tõestab, et kasutaja omab UTXO kulutuste tingimuse kohaselt eeldatavat privaatvõtit;
- Terviklikkuse kaitse: seob autoriseerimise tehingu täpsete üksikasjadega (saajad, summad, tasud jne). Kui keegi muudab tehingut tagantjärele, ei ole allkiri enam kehtiv.



Kui kasutaja Bitcoin wallet on tehingu korrektselt koostanud ja allkirjastanud, tuleb see Bitcoin võrgus edastada.



### Bitcoin sõlme roll levitamisel



Bitcoin on [võrdõiguslik võrk](https://planb.academy/resources/glossary/peertopeer-p2p): puudub keskne server, mis võtab vastu ja töötleb kõiki tehinguid. Seda rolli täidavad sõlmed ühiselt. Bitcoin-sõlm on tarkvara (nt [Bitcoin Core](https://planb.academy/resources/glossary/bitcoin-core)), mis on ühendatud teiste Bitcoin-võrgu sõlmedega ja mille peamine ülesanne on tehingute ja plokkide kontrollimine, salvestamine ja edastamine.



Kui saadate tehingu wallet-st, edastab wallet selle sõlme (teie enda või teenuse sõlme). See sõlmpunkt kontrollib kõigepealt, kas tehing vastab erinevatele reeglitele, näiteks:




- allkirjad on kehtivad;
- sisendid viitavad olemasolevatele UTXO-dele (st olemasolevatele bitcoinidele);
- need UTXO ei ole juba mujal kulutatud;
- [väljundite](https://planb.academy/resources/glossary/output) hulk on väiksem või võrdne sisendite hulgaga (bitcoin'id ei teki tühjalt kohalt);
- jne.



Kui tehing läbib kõik need kontrollid, edastab sõlmpunkt selle teistele võrgusõlmedele, millega ta on ühendatud. Need omakorda kontrollivad seda ja edastavad selle edasi jne. Mõne sekundiga on tehing levitatud ja sellest saab teada kogu Bitcoin võrk või vähemalt suur osa sellest.



![Image](assets/fr/003.webp)



### Mempool: tehingu ooteruum



Tehingu edastamise ja selle kinnitamise vahel peab see ootama. Seda ooteala nimetatakse **[mempool](https://planb.academy/resources/glossary/mempool)** (lühend sõnadest `memory` ja `pool`). Mempool on seega ajutine salvestusruum kehtivate, kuid veel kinnitamata tehingute jaoks.



Oluline punkt: ei ole olemas sellist asja nagu üks mempool, vaid ainult mempool. Iga sõlmpunkt haldab oma mempool'i, millel on oma kohalikud piirangud. See tähendab, et igal ajahetkel võib kahe sõlme mempoolisisu veidi erineda (sõltuvalt sellest, mida nad on saanud, mida nad on tagasi lükanud või mida nad on kustutanud).



![Image](assets/fr/004.webp)



Selles etapis teab võrk tehingust, on seda kontrollinud ja hoiab seda mälus kuni selle kinnitamiseni. Kuid selle tehingu kinnitamine saabub alles siis, kui kaevandaja lisab selle plokki ja võrk aktsepteerib selle ploki.



### Blockchain: avalik ajamärgistusregister



Kuna bitcoin on immateriaalne valuuta, peab see lahendama ühe probleemi: vältida [topeltkulutusi](https://planb.academy/resources/glossary/double-spending-attack) ilma keskse asutuseta. Kui kaks tehingut üritavad kulutada sama UTXO, peab kõigil olema võimalik läheneda ühele, ühtsele olekule. Satoshi Nakamoto võtab selle probleemi kokku selle kuulsa lausega:



> Ainus viis kinnitada tehingu puudumist on olla teadlik kõigist tehingutest.

Teisisõnu, selleks, et teada, et bitcoin ei ole juba kulutatud, on vaja ühiseid andmeid varasemate kulutuste kohta.



See ongi plokiahela roll: avalik register, mis sisaldab tehingute ajalugu. Kuid selle asemel, et kirjutada iga tehingu toimumise ajal, rühmitab Bitcoin need plokkidesse. Iga plokk toimib ajaloo leheks ja süsteem toimib seega nagu ajatemplite server: see järjestab tehinguid aja jooksul kontrollitaval viisil.



Seda registrit ei saa ümber kirjutada tänu lihtsale põhimõttele: iga plokk sisaldab eelmise ploki krüptograafilist sõrmejälge ([hash](https://planb.academy/resources/glossary/hash-function)). Seega on plokid omavahel seotud: kui muuta eelmist plokki, muutub selle hash, mis katkestab seose järgmise plokiga, mis katkestab seose ülejärgmise plokiga jne. Just selline sõltuvuste ahel annab "*blockchainile*" oma nime.



![Image](assets/fr/005.webp)



Kui me oleme neid Bitcoin põhiprintsiipe mõistnud, saame kirjeldada kaevuri eesmärki konkreetsemalt: ehitada uus plokk, mis laiendab olemasolevat ahelat, kirjutades sinna pooleliolevad tehingud, ja seejärel püüda see kehtivaks muuta (see on kuulus "[proof of work](https://planb.academy/resources/glossary/proof-of-work)", mida me uurime hilisemas peatükis). Kuid kõigepealt avastame koos järgmises peatükis, kuidas kandidaatblokki konstrueeritakse.



## Bitcoin ploki ehitamine


<chapterId>2b5cd04b-d400-4865-b0a0-e70fa7e67c17</chapterId>



Nüüd olete aru saanud, kuidas Bitcoin tehing toimib ja milline on plokiahela roll. Kuid enne, kui vaatame lähemalt, kuidas proof-of-work töötab, on veel üks oluline samm, mille kaevandaja peab tegema: [kandidaatbloki](https://planb.academy/resources/glossary/candidate-block) konstrueerimine. Uurime üheskoos, mis on kandidaatblokk ja kuidas kaevandaja selle konstrueerib, enne kui alustame kehtiva tõendi otsimist.



### Kandidaatide plokk



Miner peavad oma plokid ise ehitama, enne kui nad üritavad neid kaevandada. Iga kaevandaja omakorda konstrueerib oma mempoolis olevate tehingute põhjal nn kandidaatbloki. Kandidaatbloki ehitamine koosneb seega järgmisest:




- valida, milliseid tehinguid lisada;
- korraldada need tehingud viisil, mis on kooskõlas Bitcoin eeskirjadega;
- toota ploki metaandmed, mis on salvestatud selle [päisesse](https://planb.academy/resources/glossary/block-header).



Tehingute valik järgib lihtsat majanduslikku loogikat: plokil on Bitcoin protokolliga piiratud maht, seega püüab kaevandaja maksimeerida seda, mida ta selle ruumi eest teenib. Ta valib esmajärjekorras tehingud, mis pakuvad kõrgeimat tasu võrreldes nende poolt plokis hõivatud ruumiga (seda nimetatakse "tasumääraks", mida väljendatakse sats/vB-s). Tasude üksikasjadega tegeletakse hiljem; tuletage lihtsalt meelde ruumi tõhususe järgi sorteerimise ideed.



Bitcoin plokk koosneb seega kahest peamisest osast:




- tehingute loetelu;
- ploki päis, mis on teatud mõttes ploki isikutunnistus.



![Image](assets/fr/006.webp)



Pealkiri on oluline, kuna seda kasutatakse proof-of-work alusena: Bitcoin puhul ei kaevandata otseselt tervet plokki, vaid ainult ploki päist, mis võtab kokku teabe, mis on vajalik ploki sidumiseks ahelaga ja selle sisu kinnitamiseks. Selleks, et päises oleksid esindatud kõik tehingud, kasutab Bitcoin krüptograafilist vahendit: [Merkle'i puu](https://planb.academy/resources/glossary/merkle-tree).



### Merkle'i puu: suure hulga tehingute kokkuvõte



Kõigi tehingute loetlemine päises oleks võimatu: üks plokk võib sisaldada tuhandeid tehinguid, samas kui päise suurus on fikseeritud (80 baiti). Seepärast on lahendus arvutada unikaalne hash, mis sõltub kõigist plokis olevatest tehingutest: see on [Merkle'i juur](https://planb.academy/resources/glossary/merkle-root).



Põhimõte on järgmine:




- arvutatakse iga tehingu krüptograafiline sõrmejälg (hash);
- need hashid on paaritatud, liidetud ja seejärel uuesti hashitud, et moodustada uus hashide kiht;
- seda protsessi korratakse, kuni saadakse üks lõplik hash: Merkle'i juur.



![Image](assets/fr/007.webp)



Seega, kui üks tehing muutub, isegi ühe bitiga, on tulemuseks selle sõrmejälje muutmine, mis levib Merkle'i juurtele. See juur sisaldub ploki päises. Seega tähendab varasema tehingu muutmine, et muudetakse ploki päistekirje, milles see sisaldub, ja seega ka ploki jalajälg, ning seejärel seos järgnevate plokkidega.



Alates [SegWit](https://planb.academy/resources/glossary/segwit) oleme eraldanud allkirjad teistest. Nii et tegelikult on igas plokis 2 Merkle'i puud, mis on pesitsetud. See eraldamine mõjutab seda, kuidas me loeme ploki suurust ja teatavaid krüptograafilisi kohustusi, kuid põhiidee jääb samaks: päis peab kompaktselt kinnitama kogu ploki sisu.



### Ploki päis



Ploki päise pikkus on 80 baiti ja see sisaldab täpselt 6 välja. proof of work otsimisel (vt järgmine peatükk) hakitakse need kuus elementi hashed-meetodil:





- Versioon (`version`): See näitab, millistele reeglitele või uuendussignaalidele plokk järgib. See on mehhanism protokolli ühilduvuse ja evolutsiooni säilitamiseks.




- Eelmise ploki hash (`previousblockhash`): See on eelmise ploki päise hash. See on see, mis seob plokke omavahel. Ilma selle väljata oleks meil iseseisvad plokid. Lisades eelmise ploki päise hashi, saame ahela, kus iga uus plokk tugineb eelmisele.





- Merkle'i juur (`merkleroot`): See on kõigi plokis olevate tehingute sõrmejälg (Merkle'i puu kaudu). See seob päise sisuga: kui kaevandaja muudab tehingute valikut või järjekorda, muutub juur.





- [Ajatempel](https://planb.academy/resources/glossary/timestamp): See on kaevandaja valitud ajatempel (Unixi aeg) (kehtivuspiirangutega), mis peab näitama, millal plokk kaevandati. See ei pea olema sekundilise täpsusega, kuid peab vastama teatavatele tingimustele, et see jääks võrgu jaoks vastuvõetavaks.





- Kodeeritud raskusaste (`nbits`): See väli kodeerib praeguse [raskusastme eesmärgi](https://planb.academy/resources/glossary/difficulty-target). Me läheme täpsemalt raskusi käsitlevas peatükis, kuid pidage meeles, et see parameeter on osa päisest.





- [Nonce](https://planb.academy/resources/glossary/nonce) (mitte üks kord): See on väärtus, mida kaevandaja võib vabalt muuta. See toimib proof-of-work ajal reguleeritava muutujana. Ma selgitan selle rolli üksikasjalikumalt järgmises peatükis, kuid on oluline mõista, et nonce on osa ploki päisest ja on mõeldud selleks, et võimaldada järjestikuseid katseid.



Et seda oleks lihtsam visualiseerida, on siin näide ploki päise kohta heksadekaalformaadis (80 baiti):



```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```



Siin on jaotus valdkondade kaupa:



```text
version: 00e0ff3f
previousblockhash: 5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
merkleroot: 206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
time: bcb13a64
nbits: b2e00517
nonce: 43f09a40
```



See kaevandaja poolt konstrueeritud plokkide päis on nende töö aluseks. Kehtiva proof-of-work otsimisel ei ole see mitte kogu tehingute nimekiri, mida otse loopis hashitakse, vaid pigem see 80baidine plokk, mis sisaldab kõike, mis on vajalik ploki sidumiseks minevikuga ja selle sisu kinnitamiseks, sisaldades samas ka mining mehhanismi jaoks vajalikke parameetreid, mida me uurime järgmises peatükis.



## Hash, sihtmärk ja nonce


<chapterId>d054323b-16bd-4556-bac5-4878654e59a3</chapterId>



Eelmistes peatükkides jälgisite Bitcoin tehingu teekonda: see luuakse ja allkirjastatakse wallet poolt, edastatakse sõlmede poolt, salvestatakse mempools, seejärel kinnitatakse, kui kaevandaja lisab selle võrgu poolt aktsepteeritud plokki. Kuid me ei ole veel näinud, kuidas kaevandaja saab oma ploki plokiahelasse lisada. Milline on protsess mining taga?



mining protsessi mõistmine on üsna lihtne. See taandub kolmele mõistele, mis käivad käsikäes: hash-funktsioon, sihtväärtus ja muutuja, mida kaevandaja saab muuta. Vaatame, kuidas see kõik toimib.



### Hash-funktsioon



Hash-funktsioon on vahend, mis võtab sisendiks sõnumi ja toodab fikseeritud suurusega väljundi, mida nimetatakse "*fingerprint*" või "*hash*".



![Image](assets/fr/010.webp)



Hash-funktsioon on arvutisüsteemides huvitav, sest sellel on teatud omadused:





- Kui te muudate sisendi ühtki bitti, muutub tulemuseks olev väljundi hash täielikult ja ettearvamatult;



![Image](assets/fr/011.webp)





- Väljundist ei ole võimalik minna sisendisse: funktsioon on pöördumatu;



![Image](assets/fr/012.webp)





- On võimatu leida kahte erinevat sõnumit, mis annavad täpselt sama hashi.



![Image](assets/fr/013.webp)



Bitcoin-s mining jaoks kasutatav hash-funktsioon on "[SHA256](https://planb.academy/resources/glossary/sha256)", mida rakendatakse kaks korda järjest. Seda tuntakse kui kahekordset SHA256 või SHA256d. See kahekordne hashimine annab ploki sõrmejälje.



```text
hash = SHA256(SHA256(message))
```



Meie puhul vastab "sõnum" tegelikult ploki päisele, mida nägite eelmises peatükis. Meeldetuletuseks, et päis on väike struktuur, mis võtab kokku kõik plokis oleva.



![Image](assets/fr/014.webp)



### Töö tõestamine: sihtmäärast väiksema hash'i leidmine



Proof-of-Work kirjeldatakse sageli kui keerulise probleemi lahendust. Tegelikult ei ole see mitte niivõrd probleem, kuivõrd katse-eksituse otsing: kaevandaja peab leidma päise versiooni, mille hash (pärast "SHA256d" hash-funktsiooni läbimist) vastab lihtsale tingimusele: see peab olema väiksem kui teatav sihtväärtus.



See tingimus on sõnastatud järgmiselt:




- ploki päise hash arvutatakse hash-funktsiooni abil;
- tõlgendame seda hashi numbrina;
- selleks, et plokk oleks kehtiv, peab see number olema väiksem või võrdne väärtusega "*raskuse eesmärk*".



Teisisõnu, plokk on kehtiv, kui:



```text
SHA256d(block_header) <= target
```



![Image](assets/fr/015.webp)



Sihtmärk on 256-bitine number. Kuna ka `SHA256d` poolt toodetud hash on 256-bitine, saab neid võrrelda kahe arvuna. Mida madalam on sihtmärk, seda raskem on tingimus, sest alla selle künnise on vähem võimalikke tulemusi. Seevastu mida kõrgem on sihtarv, seda lihtsam on tingimust täita ja seda lihtsam on plokki kaevandada. Seda, kuidas see eesmärk määratakse, vaatleme lähemalt hilisemates peatükkides.



Selles süsteemis on huvitav hash-funktsioon. Pidage meeles, et väljundit on lihtne arvutada sisendi põhjal, kuid võimatu on leida sisendit, teades ainult funktsiooni väljundit. mining puhul ei paluta kaevandajatel leida täpset hashi, vaid pigem leida sihtväärtusest madalam hash. Ainus viis selle saavutamiseks on teha väga palju katseid, kuni nende kandidaadiploki konkreetse päise hashimise tulemuseks on sellest eesmärgist väiksem hash.



Kui eesmärk on piisavalt madal, muutub see protsess kulukaks. Kaevandaja arvutab oma kandidaadiploki päise hashi, kontrollib tulemust ja kui tingimus ei ole täidetud, muudab päise ja kordab arvutust. Seda tsüklit korratakse seni, kuni leitakse kehtiv päis. Kui päise hash vastab lõpuks tingimusele, on proof of work loodud, plokk loetakse kehtivaks ja seda saab Bitcoin võrgus edastada, et sõlmed saaksid seda oma plokiahelasse lisada. Võitnud kaevandaja saab seejärel sellega seotud tasu (selle koosseisu kirjeldame üksikasjalikult hiljem), samal ajal kui kõik kaevandajad asuvad kohe otsima uut, kehtivat päistekoodi järgmise ploki jaoks.



Selle mehhanismi peamine eelis seisneb selle asümmeetrias. proof of work tootmine on kaevurite jaoks kulukas, sest see nõuab suurt arvu hash-arvutusi. Teisalt on verifitseerijate, st võrgusõlmede jaoks verifitseerimine äärmiselt lihtne: nad peavad vaid arvutama kaevandaja esitatud ploki päise ja kontrollima, et saadud hash on tõepoolest madalam kui eesmärk. Tõendi leidmine nõuab seega palju tööd ja ressursse, samas kui selle kehtivuse kontrollimine on kiire ja odav. Just see omadus määrab tõhusa proof-of-work süsteemi.



### Nonce



Praktiline küsimus jääb: kui kaevandaja poolt konstrueeritud kandidaatbloki päis ei anna kehtivat hashi, siis kuidas saab kaevandaja uuesti proovida? Ta peab muutma midagi päises, et saada teistsugune hash. Just see ongi nonce'i roll.



Pidage meeles hash-funktsiooni esimest omadust: piisab, kui muuta sisendist ühtki bitti, et saada täiesti erinev ja ettearvamatu väljundhash. Iga hash-arvutus on seega võrreldav juhusliku loosimisega.



![Image](assets/fr/016.webp)



Et uuesti õnne proovida, ei pea kaevandaja muutma kogu oma kandidaadiploki päistikku: ta peab muutma vaid pisikest osa sellest, sest isegi üks erinev bitt annab täiesti uue hashi, mis võib olla kehtiv, kui see on väiksem kui sihtmärk.



Just sellepärast sisaldab ploki päis nonce'i. Nonce on 32-bitine väärtus, mida kasutatakse üks kord ja mis seejärel asendatakse. Praktiliselt võib kaevandaja ühe ja sama kandidaatploki puhul testida umbes 4,29 miljardit võimalikku väärtust (alates "0" kuni "2^32 - 1"). Iga nonce'i variatsioon muudab ploki päise ja sellest tulenevalt muudab täielikult hash-funktsiooni "SHA256d" rakendamise järel saadud hash-funktsiooni.



mining protsess on väga lihtne:




- kaevandaja koostab kandidaatbloki (tehingud + päis);
- seejärel arvutab "SHA256d(päise)-i" hashi;
- kui tulemus on suurem kui eesmärk, muudab see nonce;
- algab uuesti;
- jne.



![Image](assets/fr/017.webp)



Tegelikult ei ole nonce ainus väli, mida saab muuta. Iga muudatus ploki tehingute raames toob kaasa Merkle'i puu juure muutmise ja seega ka selle ploki päise muutmise. Tänapäevase arvutusvõimsuse juures on 4,29 miljardi võimaliku nonce'i väärtuse läbimine võimalik suhteliselt kiiresti. Seepärast on olemas veel üks väli, mida üldiselt nimetatakse "*[extra-nonce](https://planb.academy/resources/glossary/extra-nonce)*", mis mitmekordistab veelgi päise muutmise võimalusi. Me tuleme selle mehhanismi juurde üksikasjalikumalt tagasi hilisemas peatükis.



### Mis on proof of work mõte?



Me nimetame seda "tõestuseks", sest tulemus on koheselt kontrollitav: kui plokk on toodetud, saab iga sõlmpunkt sekundi murdosa jooksul kontrollida, et selle päise krüptograafiline hash on tõepoolest alla nõutava eesmärgi. Me nimetame seda "tööks", sest selle hashi saavutamiseks on vaja arvukalt katseid ja seetõttu on see arvutuste ja energia seisukohast väga kulukas.



Bitcoin [valges raamatus](https://planb.academy/resources/glossary/white-paper) Satoshi Nakamoto toob proof-of-work süsteemi kasutamise kaks eelist Bitcoin-süsteemis:





- Seal majandusajalugu:**



Kui arvutuskoormus on kulutatud, on plokk lukustatud: selle muutmine nõuaks selle ploki proof of work uuesti sooritamist. Ja kuna plokid on omavahel aheldatud, tähendaks vana ploki muutmine ka kõigi järgnevate plokkide ümberarvutamist ning seejärel ausa ahela käimasoleva töö järelejõudmist ja ületamist.



Teisisõnu, proof-of-work on ajamärgistussüsteemi selgroog, mis muudab mineviku võltsimise plokkide kogunemisel üha kulukamaks. Uue ploki kaevandamisel kohaldatakse proof of work pakutavat turvalisust samaaegselt ja ühtlaselt kõigile olemasolevatele UTXO-dele. Iga lisanduva plokiga kogub iga UTXO seega Proof-of-Work-lt täiendavat tagatist.





- Määratleda enamuse reegel ([konsensus](https://planb.academy/resources/glossary/consensus)) ja neutraliseerida Sybil:**



Proof-of-Work võimaldab ka Bitcoin-l jõuda konsensusele, ilma et ta tugineks "üks ID = üks hääl" hääletusreeglile, mida on lihtne võltsida identiteetide (IP-d, sõlmed, võtmed...) massilise loomise tõttu.



Bitcoin puhul ei ole "*Majoriteet*" mitte suurim osalejate arv, vaid **ahela, mis kogub kõige rohkem tööd**. Nagu Satoshi ütleb, on see põhimõte "üks protsessor = üks hääl", st hääl, mida kaalutakse kehtivate plokkide tootmiseks kulutatud tegeliku arvutusvõimsuse järgi. Seega ei anna tuhandete sõlmede kasutuselevõtt iseenesest mingit eelist Bitcoin ees. Ilma täiendava arvutusvõimsuseta ei kogune rohkem tõendeid ja [Sybil-rünnak](https://planb.academy/resources/glossary/sybil-attack) muutub kasutuks, samas kui otsustusreegel jääb objektiivseks ja ei nõua osalejate tuvastamist.



![Image](assets/fr/018.webp)



[Nakamoto, S. (2008). *Bitcoin: Peer-to-Peer elektroonilise sularaha süsteem.*](https://bitcoin.org/bitcoin.pdf)



Alaealiste kasulikkuse ja volitustega seotud põhimõtted on väga keeruline teema, mida ma siinkohal põhjalikumalt ei käsitle. Kuid me tuleme selle teema juurde põhjalikult tagasi tulevastel MIN 201 koolitustel.



Hetkel võib kokku võtta, kuidas mining töötab järgmiselt: kaevurid koostavad kandidaadiploki koos mempoolides pooleliolevate tehingutega, seejärel otsivad selle päise hash'i (SHA256d kaudu), mis on väiksem või võrdne sihtmääraga. Nad saavutavad selle, katsetades katsete ja eksimuste abil mitte-otsuseid.



Järgmises peatükis teeme lühikese ajaloolise kõrvalepõike proof-of-work põhimõttesse, et mõista selle tausta, ja seejärel vaatame, kuidas süsteem määrab kindlaks raskuse eesmärgi.



## proof of work ajalugu


<chapterId>919d9f3e-8b3b-41d9-b45a-54df4f3c31a3</chapterId>



Proof-of-work ei ole Bitcoin jaoks leiutatud. [Satoshi Nakamoto](https://planb.academy/resources/glossary/nakamoto-satoshi) võttis üles ja ühendas mitu varasemat ideed, mida oli juba erinevates kontekstides uuritud.



### Hashcash



1990ndate lõpus muutus rämpsposti probleem oluliseks. Kui e-kirja saatmine ei maksa peaaegu midagi, võib spämmija saata miljoneid. Kui aga iga sõnum nõuab väikest arvutuslikku pingutust, jääb ühe seadusliku sõnumi saatmine tavakasutajale lihtsaks, samas kui miljonite sõnumite saatmine muutub väga kalliks.



See on [Hashcash'i](https://planb.academy/resources/glossary/hashcash) eesmärk, mille Adam Back pakkus välja 1997. aastal ja mida peetakse proof-of-work põhimõtte leiutamiseks. Hashcash'i põhimõte on väga sarnane mining-le: toota hash, mis vastab tingimusele (teatud arv nulle hashi alguses). Tõend on siis sõnumiga kaasas ja vastuvõtja saab seda väga kiiresti kontrollida. Kui saabub e-kiri, mis ei sisalda seda tõendit, võib seda kohe pidada rämpspostiks ja seega filtreerida. Rämpsposti saatjad on siis sunnitud kulutama märkimisväärse hulga energiat miljonite sõnumite saatmiseks, mis vähendab oluliselt (või isegi muudab täielikult olematuks) seda tüüpi tegevuse kasumlikkust, olgu see siis turunduslik või pettuslik.



Tänapäeval ei kasutata Hashcash'i e-kirjade saatmiseks. Rämpsposti filtreerimine põhineb nüüd suures osas tsentraliseeritud süsteemidel. Hashcashi eelis praeguste lahenduste ees seisneb selles, et see ei nõua tsentraliseeritud filtreerimist: igaüks saab parameetreid kohandada vastavalt oma kriteeriumidele. Samuti ei nõua see tuvastamist, sest hash-otsingut saab teha anonüümselt. Ennekõike ei tugine see mainesüsteemile, mis kipub kehtestama subjektiivseid filtreerimisviise.



Hashcash ei tegelenud raha loomisega. Selle eesmärk oli kehtestada marginaalsed kulud kergesti automatiseeritavale digitaalsele tegevusele.



![Image](assets/fr/008.webp)



### Bit Gold



1990ndate lõpus ja 2000ndate alguses uuris Nick Szabo proof of work alusel digitaalse nappuse ideed. Tema kontseptuaalne projekt nimega Bit Gold näeb ette väärtuseühikute loomist, lahendades kulukat proof of work ja seejärel registreerides need tõendid registris, et luua omandiõiguse vorm.



Bit Gold ei andnud tulemuseks Bitcoin-sarnast kasutuselevõetud süsteemi, kuid see sisaldab mitmeid olulisi arusaamu: idee, et arvutamine võib tekitada nappust, ja idee, et aja jooksul tembeldatakse elemente, et luua ajalugu, mida on raske ümber kirjutada.



### RPOW



2004. aastal tegi Hal Finney ettepaneku RPOW (*Reusable Proofs of Work*). Idee oli toota tööde tõendid, mida saaks seejärel vahetada, mitte lihtsalt tarbida. RPOW eesmärk oli luua proof of work alusel digitaalsed token, mille puhul oleks olemas süsteem nende token kontrollimiseks ja edastamiseks ilma neid dubleerimata. RPOW ei lahendanud jällegi rahuldavalt täielikult detsentraliseeritud registri probleemi, nagu seda tegi hiljem Bitcoin, kuid see jääb üheks Bitcoin suureks eelkäijaks.



![Image](assets/fr/009.webp)



Hashcash, Bit Gold ja RPOW kasutavad proof-of-work, et kehtestada kulu ja luua puuduse vorm. Bitcoin kasutab seda mehhanismi, kuid annab sellele keskse ja kollektiivse rolli: proof-of-work ei kasutata mitte ainult millegi loomiseks, vaid seda kasutatakse ka selleks, et otsustada, kellel on õigus kirjutada registri järgmine lehekülg (järgmine plokk), ning selleks, et muuta selle registri võltsimine kulukaks.



## Raskuse eesmärgi kohandamine


<chapterId>528bcaa8-351e-4eae-887a-426a78a223e3</chapterId>



Eelmistes peatükkides nägite proof-of-work põhitõdesid: kaevandajad hashivad oma kandidaatbloki päise "SHA256d" ja plokk loetakse kehtivaks ainult siis, kui saadud hash on numbriliselt väiksem või võrdne sihtväärtusega, mida nimetatakse sihtväärtuseks. Seejärel jääb küsimus: kust see sihtväärtus pärineb ja kuidas süsteem tagab, et see jääb aja jooksul järjepidevaks?



Bitcoin eesmärk on leida keskmiselt üks plokk iga 10 minuti tagant. Ilmselgelt ei ole see tempo sekundi täpsusega garanteeritud. Tegelikkuses leitakse mõned plokid mõne sekundi pärast eelmist, teised aga rohkem kui tunni aja pärast. Oluline on siinkohal keskmine väärtus piisavalt pika aja jooksul.



![Image](assets/fr/019.webp)



Selline varieeruvus tuleneb mining tõenäosuslikust olemusest: iga hash on sõltumatu katse, mille puhul (eeldusel, et eesmärk ei muutu) on tõenäosus, et tulemus jääb alla eesmärgi, konstantne. Seetõttu võib seda võrrelda pideva loosimisega loteriiga: mida rohkem hashes'eid teevad kaevandajad sekundis, seda lühem on oodatav viivitus enne kehtiva ploki ilmumist, kuid see ei kõrvalda kunagi juhuslikkust ühest loosimisest teise.



### Miks peaks blokide vahel olema 10 minutit?



Kuigi selle kohta puuduvad tõendid, valis Satoshi Nakamoto kindlasti 10 minutit kui praktilise kompromissi tõhususe ja turvalisuse vahel. Lühem intervall annaks sagedamini kinnitusi, kuid põhjustaks rohkem ajutisi võrgu lõhkumisi. Selle punkti mõistmiseks peame pöörduma tagasi ploki leviku viiside juurde.



Kui kaevur leiab kehtiva ploki, jagab ta selle kohe oma kolleegidele. Selle saanud sõlmed kontrollivad selle kehtivust (tehingud, proof of work, konsensusreeglid jne) ja edastavad seda omakorda edasi. See levitamine võtab teatud aja, mida piiravad interneti latentsus, ribalaius ja iga sõlme võime plokki kontrollida.



![Image](assets/fr/020.webp)



Kui selle difusiooniviivituse ajal avastab teine kaevandaja samuti kehtiva ploki samal kõrgusel, võib võrk ajutiselt jaguneda: üks osa sõlmedest ja kaevandajatest toetub plokile A, teine osa aga plokile B. See on võrgu ajutine jagunemine.



![Image](assets/fr/021.webp)



Need lahkarvamused ei ole katastroofilised. Nakamoto konsensus ennustab, et pikas perspektiivis jääb ainult üks haru valituks: see, mis kogub kõige rohkem tööd. Tõepoolest, niipea kui näiteks ploki A peale kaevandatakse uus plokk, sünkroniseerib kogu võrk selle haru suhtes uuesti ja loobub plokist B, mis muutub seejärel "*[tühjaks plokiks](https://planb.academy/resources/glossary/stale-block)*", mida mõnikord ekslikult nimetatakse argikeeles "*orblaseks plokiks*".



![Image](assets/fr/022.webp)



Teisest küljest on neil hind: mõne minuti jooksul töötab murdosa kaevuritest oksal, mis jäetakse maha. See töö on siis üldise turvalisuse seisukohast raisku läinud, sest see ei ole aidanud kaasa lõpliku ahela loomisele. Mida kiirem on iga ploki vaheline ajavahemik, seda suurem on selliste jagunemiste tõenäosus, sest paljundusaeg moodustab suurema osa iga ploki vahelisest ajast.



10-minutiline intervall võimaldab üldjuhul piisavalt aega, et võitnud plokk saaks laialt levida, enne kui leitakse samal kõrgusel asuv konkureeriv plokk. See on kompromiss, mis piirab jagunemisi, vähendab arvutusvõimsuse raiskamist ja aitab võrgul püsida sünkroonis globaalsel skaalal.



### hashrate mõistmine



*"[Hashrate](https://planb.academy/resources/glossary/hashrate)*" viitab sekundis toodetud hash-arvutuste hulgale, olenemata sellest, kas seda teeb üks kaevur, kaevurite rühm või kõik kaevurid Bitcoin-s. Seda väljendatakse ühikutes "H/s" (hashid sekundis), mille kordajad on näiteks "TH/s" (terahashid sekundis) või "EH/s" (eksahashid sekundis). See näitab, mitu katset kaevandajad saavad teha igas sekundis, et saada sihtarvust madalam hash.



Kui sihtmärk jääb fikseeritud, siis:




- igal katsel on kindel tõenäosus õnnestumiseks;
- rohkemate katsete tegemine sekundis suurendab tõenäosust, et võitnud katse ilmub kiiresti


Teisisõnu, kui homne Bitcoin võrk kahekordistab oma arvutusvõimsust, ühendades kaks korda rohkem mining masinaid, siis ilma parandusmehhanismita leitakse plokid keskmiselt kaks korda kiiremini. Seepärast tuleb eesmärki kohandada, et kompenseerida hashrate erinevusi.



### Raskuse eesmärgi kohandamine



Bitcoin lahendab selle probleemi perioodilise sihtmärgi kohandamise mehhanismiga, mis kohandab mining [raskust](https://planb.academy/resources/glossary/difficulty-adjustment). Põhimõte on järgmine: iga 2016. ploki järel (umbes iga 2 nädala järel) arvutab iga sõlmpunkt raskuse eesmärgi uuesti, jälgides, kui palju aega tegelikult kulus nende 2016. plokkide tootmiseks.



Selle mehhanismi eesmärk on vähendada ühe ploki keskmist tootmistähtaega umbes 10 minutini, samas kui võrgu üldine hashrate muutub pidevalt, sest masinaid ühendatakse maha või vastupidi, uusi masinaid lisatakse.



![Image](assets/fr/023.webp)



Arvutus põhineb möödunud ajavahemiku jooksul täheldatud ajal:




- kui viimased 2016. aasta plokid leiti liiga kiiresti, tähendab see, et hashrate suurenes selle perioodi jooksul; Bitcoin muudab seejärel tingimuse raskemaks, vähendades järgmise perioodi eesmärki;
- kui 2016. aasta plokid leiti liiga aeglaselt, tähendab see, et hashrate on vähenenud; Bitcoin leevendab seda tingimust, suurendades eesmärki.



Valem on järgmine:



```txt
Tn = To * (Ta / Tt)
```



Koos:




- `tn`: uus sihtmärk
- "to": vana sihtmärk
- "Ta": viimase 2016 ploki kulunud reaalaeg
- "Tt": siht aeg (sekundites)



Eesmärgiks on kaks nädalat, st "Tt = 1 209 600" sekundit:



```txt
Tn = To * (Ta / 1 209 600)
```



Selleks, et mõista, kuidas kohandada Bitcoin mining raskust, on siin näide fiktiivsete väärtustega:



```txt
Tn = To * (Ta / 1 209 600)
Tn = 18 045 755 102 * (1 000 000 / 1 209 600)
Tn = 14 918 779 020
```


Koos:



- `**To = 18,045,755,102**`: Vana sihtväärtus, st kontrollväärtus enne korrigeerimist.
- `**ta = 1,000,000 sekundit**`: Viimase 2016 ploki tegelik tootmisaeg. Kuna see aeg on väiksem kui eesmärk, on võrk kaevandanud liiga kiiresti.
- **1,209,600 sekundit**: Eesmärk, mis vastab 10 minutile ühe ploki kohta 2016. aasta plokkide puhul, mida kasutatakse võrdlusena korrigeerimisel.
- "**tn = 14,918,779,020**": Uus eesmärk, mis on arvutatud pärast raskuste korrigeerimist.



Siin on uus eesmärk madalam kui vana, mis tähendab, et mining muutub raskemaks, et aeglustada plokkide tootmist järgmisel perioodil.


*Selles näites esitatud sihtväärtused on lihtsustatud ja õpetamise eesmärgil skaleeritud; Bitcoin-s kasutatav tegelik sihtväärtus on 256-bitine täisarv, mis on täiesti teistsuguse suurusjärgu *



Selle arvutuse teeb iga sõlmpunkt lokaalselt, tuginedes plokkidesse sisestatud ajatemplitele. Kuna kõik sõlmed kohaldavad samu reegleid, jõuavad nad samale tulemusele ja uuest eesmärgist saab ühine viide järgmistele 2016. aasta plokkidele.



Selle kohandamise kohta tuleb märkida üks oluline detail: **See on piiratud**. Bitcoin piirab raskusastme muutumist perioodi kohta, et vältida liiga järske muutusi, mis võivad seda blokeerida. Tegelikult piiratakse arvesse võetavat tegelikku aega nii, et see jääks vahemikku, mis vastab 4-kordsele tegurile (minimaalselt veerand vanast eesmärgist, maksimaalselt neli korda vanast eesmärgist). See takistab äärmuslikku ümberhindamist, kui ajatemplid on väga ebatüüpilised või manipuleeritud.



### Eesmärgi esindatus



Bloki päises ei ole sihtmärk esitatud täies 256-bitises vormis, kuna see võtaks liiga palju ruumi. Selle asemel kodeerib 32-bitine väli "nBits" eesmärgi kompaktses formaadis, mis on võrreldav baas 256 teadusliku notatsiooniga: eksponent (1 bait) ja koefitsient (3 baiti). Seejärel rekonstrueeritakse täielik sihtmärk nendest kahest väärtusest. Me ei hakka siinkohal üksikasjadesse laskuma, sest see teema on suhteliselt keeruline ja ei anna mining mõistmisele midagi juurde. Pidage lihtsalt meeles, et sihtmärk ei ole salvestatud ploki päises toorelt, vaid kompaktsel kujul.



Selle I osa viimase peatükiga oleme teinud ringkäigu, kuidas proof-of-work töötab Bitcoin-s: kaevandaja koostab kandidaatbloki, valides oma mempoolist tehinguid, arvutab kandidaatbloki päise, hashib seda, võrdleb saadud hashi perioodi sihiga, seejärel alustab uuesti, muutes nonce'i, kuni saadakse kehtiv hash. Lõpuks arvutab võrk iga 2016 ploki järel uue eesmärgi uuesti, et säilitada hashrate pidevatest muutustest hoolimata keskmine aeg umbes 10 minutit ploki kohta.




# Bitcoin mining stimuleeriv süsteem


<partId>27fb10c1-d53b-4dc2-90fa-3cb0309b74c1</partId>



## Block reward


<chapterId>b316fb89-9c18-417e-917b-ab98f1722646</chapterId>



Nagu te võite ette kujutada, ei ole Bitcoin mining altruistlik tegevus. Miner-l on reaalsed kulud: elektrienergia nende mining arvutite käitamiseks, eriseadmete ostmine, hoolduse palgakulu, mõnikord ruumid ja jahutussüsteemid. Selleks, et Bitcoin süsteem toimiks, peavad kaevurite erahuvid olema kooskõlas võrgu kollektiivsete huvidega. Just see on mining tasu roll. See julgustab kaevandajaid investeerima proof of work-sse, lisama kehtivaid tehinguid ja austama protokolli reegleid, mitte püüdma seda rikkuda.



See loogika põhineb mänguteoorial: protokoll muudab aususe ratsionaalseks. Kaevur teenib raha, kui ta toodab kehtiva ploki, mille sõlmed on heaks kiitnud. Kui ta aga üritab petta, lükkavad sõlmed tema ploki tagasi ja ta ei saa midagi. Kuna ploki tootmine on kulukas, tähendab tagasilükatud plokk otsest kaotust. Konkurentsikeskkonnas, kus tuhanded mängijad otsivad samaaegselt kehtivat plokki, on seega kõige kasumlikum strateegia enamasti reeglite range järgimine ja oma tulu ausalt maksimeerimine.



Selle saavutamiseks näeb Bitcoin protokoll ette, et kaevandaja, kes leiab kehtiva ploki, võidab õiguse lisada sellesse konkreetne tehing, mis annab kaevandajale teatud summa BTC. Seda nimetatakse **[blokipreemiaks](https://planb.academy/resources/glossary/block-reward)**. Selles esimeses peatükis on eesmärk mõista, millest see koosneb ja kuidas see määratakse. Hiljem näeme, kuidas raha loomise osa aja jooksul areneb (koos poolitustega) ja kuidas seda tegelikult tehniliselt kogutakse (coinbase'i tehingu kaudu).



### Millest koosneb plokkide preemia?



Eelmistes peatükkides nägime, kuidas kaevurite õnnestub leida kehtiv plokk. Kui kaevandaja on leidnud päise, mille hash on väiksem kui sihtmärk, loetakse tema plokikandidaat kehtivaks. Seejärel võib ta seda levitada kogu Bitcoin-võrku. Plokk lisatakse ülejäänud plokiahelale, kinnitades selles sisalduvad tehingud.



Just see sündmus (ploki tegelik lisamine plokiahelasse) käivitab võitnud kaevandajale tasu andmise. See tasu koosneb kahest erinevast elemendist, mis liidetakse kokku:




- [blokeeritud toetus](https://planb.academy/resources/glossary/block-subsidy)**;
- tehingutasud**.



![Image](assets/fr/024.webp)



Vaatame, millele need kaks tasu osa vastavad.



### Blokeeritud subsiidium



Plokksubsiidium vastab tasu rahalise loomise osale. Kui kaevandaja toodab kehtiva ploki, lubab protokoll tal luua teatud arvu uusi bitcoine ja eraldada need endale tasu eest. Need bitcoinid luuakse ex nihilo. Neid ei olnud varem olemas.



Kuid äsja loodud bitcoinide kogus ei ole sugugi suvaline. See on rangelt määratletud Bitcoin protokolli reeglitega ja on kõigil kaevandajatel ühesugune. Vaatleme seda mehhanismi lähemalt järgmises peatükis, sest toetus ei ole lõpmatult fikseeritud väärtus: seda jagatakse perioodiliselt täpse ajakava järgi. Praegu pidage lihtsalt meeles, et:




- blokeeritud toetus on üks kahest blokeeritud preemia komponendist;
- see on piiratud ja määratud protokolli, mitte kaevandaja poolt (kuigi kaevandaja võib tehniliselt taotleda vähem kui maksimaalne summa);
- see loob bitcoinid õhust välja.



Sellel toetusel on Bitcoin protokollis kaks peamist rolli. Esimene neist on julgustada mängijaid mining-s osalema. Bitcoin algusaastatel (ja mõnikord ka praegu) olid tehingutasud väga madalad. Seetõttu on toetus taganud piisava hüvitise, et meelitada kaevandajaid ja säilitada süsteemi turvalisuse tase.



Teine roll on seotud valuuta jaotamisega. Iga uus valuuta seisab silmitsi küsimusega, kuidas jaotada rahaühikuid õiglaselt elanikkonna vahel. Blocksubsiidium annab sellele probleemile vastuse. Luues bitcoin'e mining kaudu, võimaldab see nende esialgset jaotamist avatud ja neutraalsel viisil: igaüks võib neid saada, kui ta osaleb mining-s, ilma et selleks oleks vaja eelnevat luba või identifitseerimist.



Teisest küljest, kuna need bitcoinid on loodud tühjalt kohalt, ei ole nende väärtus aluseta. Suurendades ringluses oleva raha hulka, lahjendab toetus mehaaniliselt olemasolevate bitcoinide väärtust. Seega toob see kaasa rahainflatsiooni ühe vormi. Järgmises peatükis näeme aga, et see subsiidium on määratud järk-järgult kaduma ja inflatsioon lõpuks lakkab.



![Image](assets/fr/025.webp)



### Tehingutasud



Teine komponent plokkide tasu on seotud süsteemi kasutamisega: kui kasutaja teeb tehingu, soovib ta, et see kinnitatakse. Blokimaht on aga piiratud ja plokid ilmuvad keskmiselt ainult iga 10 minuti tagant. Plokiruum on seega napp ressurss. Kui nõudlus ületab pakkumise, tõuseb hind: see on tehingutasu turg. Iga kaevandaja, kes suudab toota kehtiva ploki, saab õiguse koguda enda arvele kõik tehingutasud, mis on seotud kõigi tema plokki lisatud tehingutega.



Võite mõelda sellest kui oksjonisüsteemist: iga tehing pakub välja tasusumma ja kaevurid seavad ruumipiirangute tingimustes esikohale need, mis maksimeerivad nende tulu. See mehhanism ühtlustab loomulikult huvisid:




- kiirustades maksavad kasutajad rohkem, et nad kiiresti kaasataks;
- kaevandajaid julgustatakse lisama tehinguid, mis maksavad kõrgeimat tasu plokiruumi eest.
- võrk väldib rämpsposti, sest tehingu avaldamine on kulukas.



#### Kuidas arvutatakse tehingutasusid?



Vastupidiselt levinud arvamusele ei ole Bitcoin tehingu väljundiks tasud. Tegelikult kulutab tehing sisendeid ja loob väljundeid. Sisendid kujutavad endast kasutatud bitcoinide allikat, samas kui väljundid kujutavad endast maksete sihtkohta. Tehingutasud on lihtsalt **sisendite ja väljundite kogusumma vahe**.



Teisisõnu, kasutaja bitcoinide sisendid, mis kuuluvad talle, loovad väljundid saajatele, kuid ei taastoota kogu sisendite poolt tarbitud summat. Nende kahe erinevus kujutab endast tehingutasusid, mida kaevandaja saab koguda.



Võtame ühe näite. Tehing tarbib kaks sisendit, millest üks on "100 000 sats" ja teine "150 000 sats", ja loob kolm väljundit "35 000 sats", "42 000 sats" ja "170 000 sats".



![Image](assets/fr/027.webp)



Seega on sisendite summa 250 000 sats ja väljundite summa 247 000 sats. See tähendab, et 3 000 sats" on tarbitud sisenditena, ilma et neid oleks uuesti loodud väljunditena: see summa vastab käesoleva tehinguga kavandatavatele tasudele.



![Image](assets/fr/028.webp)



Kui kaevandaja lisab selle tehingu kehtivasse plokki, on tal õigus saada tagasi need 3000 sats, lisaks kõigi teiste plokis sisalduvate tehingute tasudele. Siiski ei ole otsest seost tasu maksva tehingu ja kaevandaja poolt tegelikult kogutud sats vahel. Tehniliselt hävitatakse 3000 sats`i tasud ja vastutasuks saab kaevandaja õiguse sama summa enda jaoks uuesti luua.



#### Tasude suhe



Plokk ei ole piiratud tehingute arvuga, vaid selle kogumahutavusega (tänapäeval praktikas ploki kaaluga). Mõned tehingud võtavad rohkem ruumi kui teised: paljude sisendite ja väljunditega tehing on suurem kui lihtne tehing ühe sisendi ja kahe väljundiga. Kasutatavad skriptid mõjutavad samuti suurust.



![Image](assets/fr/026.webp)



Seetõttu võivad kaks tehingut maksta absoluutarvudes sama suurt tasu, kuid ei pruugi olla kaevandaja seisukohast majanduslikult samaväärsed. Kui üks neist on kaks korda suurem, maksab see kaks korda rohkem ruumi plokis. Ruumi on vähe, seega püüab kaevandaja maksimeerida oma tulu ruumiühiku kohta.



Seetõttu väljendame praktikas tehingu konkurentsivõimet tasu suhtarvuga, mis on tavaliselt sats/vB ([satoshi](https://planb.academy/resources/glossary/satoshi-sat) virtuaalse baidi kohta). Selle suhtarvu arvutamine on lihtne:



```text
fee rate = fee / weight (in vB)
```



Näiteks, kui meil on tehing, mis kaalub 141 vB ja mille tasud on 1,974 sats, siis on selle tasumäär 14 sats/vB.



```text
1 974 / 141 ≈ 14 sats/vB
```



See suhe seletab kaevurite tehtud majanduslikke valikuid: fikseeritud võimsuse juures maksimeerib kõrgete tehingute kaasamine ploki kogutasu ja seega ka kaevuri hüvitist. See seletab ka seda, miks odavad tehingud jäävad pikaks ajaks mempoolsesse järjekorda: nad konkureerivad teiste tehingutega, mis maksavad rohkem ruumiühiku eest.



### Võrgu kaitse rämpsposti eest



Tasud täidavad ka operatiivset turvalisuse eesmärki: need suurendavad tehingute korrutamise kulusid. Kui tehingu avaldamine oleks tasuta, oleks lihtne võrku üle ujutada kasutute tehingutega ja küllastada mempool, suurendades sõlmede koormust.



Praktikas rakendavad sõlmed kohalikke releepoliitikaid (mempoolreeglid) ja määravad sageli minimaalse tasu künnise, millest allapoole nad tehingut ei edasta (vaikimisi "0,1 sat/vB" Bitcoin Core'is "minRelayTxFee" kaudu). Tehing võib olla konsensusreeglite ranges mõttes kehtiv, kuid enamik sõlmi ei edasta seda, kui selle tasud on liiga madalad. Selle tulemusel ei liigu see ringlusse, ei jõua kaevandajateni ja selle kinnitamise tõenäosus on väga väike.



Siinkohal on teil plokkide tasu põhiolemus: see vastab võitnud kaevandajale makstavale hüvitisele ja koosneb kahest erinevast elemendist. Ühest küljest protokollireeglitega määratletud plokktoetus, mis loob ex nihilo uusi bitcoine. Ja teiselt poolt kaevandatud plokis sisalduvate tehingute tasud.



Järgmises peatükis keskendume üksikasjalikumalt blokksubsiidiumile, et mõista täpselt, kuidas seda arvutatakse ja kuidas see aja jooksul vastavalt Bitcoin protokolli reeglitele muutub.



## Halving


<chapterId>7cdca211-7300-48f8-a1e4-53e5c2678cd8</chapterId>



Eelmises peatükis nägime, et kaevandajad, kes toodavad kehtiva ploki, saavad tasu, mis koosneb plokis sisalduvate tehingute tasudest ja plokkide toetusest. Me ei ole aga veel selgitanud, kuidas selle toetuse suurus määratakse. Mehhanism, mis seda väärtust määrab ja arendab, on tuntud kui ***[halving](https://planb.academy/resources/glossary/halving)***.



### Mis on poolitamine?



Halving on Bitcoin-protokolli sisse programmeeritud sündmus, mis vähendab plokkide toetust poole võrra, st maksimaalset uute bitcoinide kogust, mida võitnud kaevandajal on lubatud iga plokiga luua. See ei mõjuta tehingutasusid: tasud eksisteerivad sõltumatult ja need määratakse jätkuvalt kasutajate aktiivsuse ja plokipinna pärast peetava konkurentsi alusel.



Kui Bitcoin käivitati 2009. aastal, määrati plokisubsiidiumiks 50 BTC iga kaevandatud ploki kohta. Sellest ajast alates on seda toetust mitu korda poole võrra vähendatud.



![Image](assets/fr/029.webp)



Halving ei käivitu mitte kuupäeva, vaid ploki kõrguse järgi. See käivitatakse **kord iga 210 000 ploki** järel. Kuna Bitcoin eesmärk on keskmiselt 10 minutit ploki kohta, vastab 210 000 plokki ligikaudu neljale aastale.



```cpp
CAmount GetBlockSubsidy(int nHeight, const Consensus::Params& consensusParams)
{
int halvings = nHeight / consensusParams.nSubsidyHalvingInterval;
// Force block reward to zero when right shift is undefined.
if (halvings >= 64)
return 0;

CAmount nSubsidy = 50 * COIN;
// Subsidy is cut in half every 210,000 blocks which will occur approximately every 4 years.
nSubsidy >>= halvings;
return nSubsidy;
}
```



Seega, kui me märkime `n` juba toimunud poolitamiste arvu, saab BTC plokisubsiidiumi arvutada järgmiselt:



```text
subsidy(n) = 50 / 2^n
```



### Varasemad poolitamised



Siin on kokkuvõtlik tabel juba toimunud poolitamistest koos nende plokkide kõrguse, kuupäeva ja pärast sündmust kohaldatava uue plokkide toetusega:



| Event               |   Height  | Date                        | Subsidy    |
| ------------------- | --------: | --------------------------- | ---------: |
| Halving 1           |   210 000 | 28 novembre 2012            |     25 BTC |
| Halving 2           |   420 000 | 9 july 2016                 |   12,5 BTC |
| Halving 3           |   630 000 | 11 may 2020                 |   6,25 BTC |
| Halving 4           |   840 000 | 20 april 2024               |  3,125 BTC |
| Halving 5 (upcoming) | 1 050 000 | Spring   2028 (estimation) | 1,5625 BTC |

### Millal ja kuidas toetus lõpeb?



Halving kordub seni, kuni toetust saab väljendada süsteemi minimaalses ühikus: satoshi.



```text
1 BTC = 100 000 000 sats
```



Kui toetus väheneb poole võrra, jõuame lõpuks nii väikeste bitcoinide murdosadeni, et need jäävad alla 1 satoshi. Sel hetkel ei ole enam võimalik luua pool satoshi ühikut. Raha loomine plokksubsiidiumi kaudu lõpeb ja kaevandajatele makstakse hüvitist ainult tehingutasude alusel. Sellest hetkest alates on kõik bitcoinid ringluses ja uusi ühikuid ei ole enam võimalik toota.



Plokkide toetuste lõplik lõpetamine toimub plokkide tasandil 6,930,000, st 33. ja viimasel poolitamisel. See sündmus leiab eeldatavasti aset umbes aastal 2140, kuigi täpset kuupäeva ei ole võimalik määrata, sest see sõltub sellest, kui kiiresti plokke praegusest hetkest kuni selle ajani tegelikult leitakse.



Kuna plokksubsiidium järgib geomeetrilist jada, mille suhe on 1/2 igal poolitamisel, siis oli rahaloome Bitcoin algusaegadel äärmiselt suur ja väheneb seejärel väga kiiresti. Seitsmendaks poolitamiseks on juba üle 99% bitcoinidest ringlusse lastud. Eeldatavasti ületatakse 99% künnis 2032. ja 2036. aasta vahel. See tähendab, et siis kulub üle 100 aasta, et kaevandada viimane 1% bitcoinidest. Kui Bitcoin käivitamisel oli raha inflatsioon väga kõrge, et võimaldada valuuta laialdast levitamist, siis nüüd on see väga madal ja langeb jätkuvalt, kuni see jõuab tõelise kõva valuuta tasemele, mille ringluses olev pakkumine ei saa enam suureneda.



![Image](assets/fr/030.webp)



### Miks ei ole kunagi 21 miljonit BTC?



Bitcoin maksimaalne rahaline varu on sageli esitatud kui 21 miljonit BTC. See on hea ligikaudne hinnang, et mõista selle rahapoliitikat, kuid rangelt tehnilisest vaatenurgast vaadatuna ei jõua kogu pakkumine tegelikult kunagi täpselt 21 000 000 bitcoinini.



Peamine põhjus on mehaaniline. Läbi järjestikuste poolitamiste langeb plokksubsiidium lõpuks alla miinimumväärtuse 1 sati, mis lõpeb enne täpse teoreetilise kogusumma saavutamist. Selle minimaalse granulaarsuse ja ümardamisreeglite tulemusena on subsiidiumiga loodud bitcoinide koguarv veidi alla 21 miljoni.



Lisaks võivad sellele lisanduda ka marginaalsed protokolliga seotud kõrvalekalded. Näiteks võivad mõned kaevandajad harvadel juhtudel jätta oma toetuse täielikult taotlemata, mis vähendab lõplikult tegelikult väljastatud bitcoinide kogust. Samuti võib mainida 3. jaanuaril 2009 Satoshi toodetud [genesis-blokki](https://planb.academy/resources/glossary/genesis-block), mille loodud bitcoinid ei ole osa [UTXO set](https://planb.academy/resources/glossary/utxo-set)-st, samuti teatud ajaloolisi sündmusi, mis on seotud vigadega, näiteks topelt coinbase'i tehingu identifikaatoritega.



Lõpuks tuleb arvesse võtta ka kõik bitcoinid, mis on hävitatud või blokeeritud:




- lahendamatutesse skriptidesse lukustatud bitcoinid;
- need, mis on tahtlikult hävitatud "OP_RETURN" skriptidega;
- või isiklike võtmete kadumine rakenduse tasandil.



Teoreetiliselt on Bitcoin varud seega piiratud 21 miljoniga. Tegelikkuses ei ole aga tegelikult kunagi 21 miljonit bitcoin'i ringluses.



## Coinbase'i tehing


<chapterId>69476700-3616-4aab-b006-367aba059de9</chapterId>



Eelmistes peatükkides esitasime kaks olulist punkti. Esiteks, kaevandaja, kes suudab toota ja levitada kehtiva ploki, saab tasu. Teisest küljest nägime, et see tasu koosneb kahest erinevast elemendist:




- plokksubsiidium (ex nihilo loodud bitcoinid, mille maksimaalne summa on määratud protokolliga ja mida vähendatakse järk-järgult poolituste kaudu);
- kõik tehingutasud, mida on maksnud kasutajad, kelle tehingud on plokki lisatud.



Üks küsimus jääb siiski: millise mehhanismi abil kogub kaevur selle tasu Bitcoin-s? Just see on konkreetse tehingu roll, mida nimetatakse "coinbase'iks".



### Kuidas coinbase'i tehing toimib



Nagu me nägime kursuse esimeses osas, sisaldab iga Bitcoin plokk nimekirja pooleliolevatest tehingutest, mida ta kinnitab. Kõige esimene neist on alati [coinbase'i tehing](https://planb.academy/resources/glossary/coinbase-transaction). See on see, mis võimaldab võitnud kaevandajal oma tasu saada.



![Image](assets/fr/031.webp)



Esmapilgul näeb see välja nagu klassikaline Bitcoin tehing: sellel on [TXID](https://planb.academy/resources/glossary/txid-transaction-identifier), väljundid ja see sisaldub ploki Merkle-puus. Siiski erineb see ühes olulises osas: see ei kuluta ühtegi olemasolevat UTXO.



Klassikalise Bitcoin tehingu puhul viitavad "sisendid" eelmistele kulutamata väljunditele (UTXO), mis annavad sisendväärtuse. Väljundid jaotavad seejärel selle väärtuse ümber uutele UTXO-dele, millel on uued kulutamistingimused. Teisisõnu, bitcoinide saatmiseks peate neid juba omama. Coinbase'i tehing seevastu ei tarbi sisendina bitcoine: see loob väljundina bitcoine otse nullist.



Just see mehhanism võimaldab uute bitcoinide ringlusse laskmist plokisubsiidiumi kaudu ja krediteerib kaevandajat plokis sisalduvate tehingutega seotud tasudega. Coinbase'i tehing ei saa viidata reaalselt olemasolevale UTXO-le (tegelikult viitab ta fiktiivsele UTXO-le), sest tema roll on just nimelt luua osa väärtusest (subsiidium) ja saada tagasi teine osa (tasud), ilma et ta saaks neid eelnevast tehingust. Et kogu süsteem jääks järjepidevaks, peab tasudele vastav osa olema täpselt võrdne nende bitcoinide summaga, mis tarbitakse sisenditena, kuid mida ei looda uuesti väljunditena teistes ploki tehingutes.



![Image](assets/fr/032.webp)



See tehing ei ole vabatahtlik. Blokk, mis ei sisalda coinbase'i tehingut, on kehtetu ja võrgusõlmed lükkavad selle süstemaatiliselt tagasi.



⚠️ Pange tähele: termin "*coinbase*" ei ole seotud samanimelise vahetusplatvormiga. Bitcoins viitab "*coinbase*" ajalooliselt tehingule, mis loob plokkide tasu. Ettevõte on selle termini lihtsalt oma nimeks võtnud.



Coinbase'i tehing täidab tegelikult korraga mitut rolli:




- Esimene on see, mida me just kirjeldasime: see määrab kaevandajale tasu, mida tal on õigus saada kehtiva ploki loomise eest.
- Selle teine, tehnilisem roll on kinnitada krüptograafiline kohustus plokis sisalduvate SegWit tehingute tunnistajatele (allkirjadele).
- Kolmas roll, mis seekord ei ole otseselt seotud protokolliga, kuid on seotud mining kaasaegse industrialiseerimisega, on see, et mündipõhja kasutatakse nüüd sageli suvaliste tehniliste andmete ankurdamiseks. Need andmed on üldiselt seotud mining poolide toimimise ja nende sisemise korraldusega.



Et aidata teil mõista neid erinevaid kasutusviise, vaatleme nüüd lähemalt coinbase'i tehingu struktuuri.



### Coinbase'i tehingu põhistruktuur



Coinbase'i tehing peab sisaldama täpselt ühte sisendit. Lihtsuse huvides ütleme mõnikord, et sellel ei ole sisendit, sest see sisend ei kuluta tegelikku UTXO. Tegelikkuses on olemas sisend, millel on viidatud allikas, kuid see osutab teadlikult olematule UTXO-le.



Nagu me juba nägime, peab iga Bitcoin tehing tarbima UTXOs sisendina, et luua kehtivaid väljundeid. Bitcoin tehingu puhul toimub see tarbimine olemasoleva UTXO sisendina viitamise kujul. Viitamine toimub lihtsalt eelmise tehingu (mille käigus UTXO loodi) identifikaatori ja selle indeksi märkimisega selle tehingu väljundite hulgas. Konkreetselt on UTXO määratletud hashi (eelmine TXID) ja indeksiga.



Kuid coinbase'i tehingu puhul peab sisend selle asemel, et viidata reaalsele olemasolevale UTXO-le, tingimata osutama sellele konkreetsele võltsitud UTXO-le, mille TXID on täis nulle, mis ei vasta ühelegi reaalsele TXID-le:



```text
0000000000000000000000000000000000000000000000000000000000000000
```


Sellele järgneb vahetult valeindeks:


```text
0xffffffff
```


![Image](assets/fr/033.webp)



Bitcoin põhiprotokollis, nagu on kirjeldatud Satoshi Nakamoto-s, on see vale sisend ainuke piirang, mis on kehtestatud mündipõhisele tehingule.



Nagu iga UTXO, millele viidatakse tehingu sisendis, on ka see seotud väljaga "scriptSig". Tavapärase tehingu puhul sisaldab see `scriptSig` väli elemente, mis on vajalikud `scriptPubKey` täitmiseks ja seega kulutatud UTXO vabastamiseks. Kuid kuna coinbase'i puhul on viidatud UTXO tahtlikult fiktiivne, on "scriptSig"-väli täiesti vaba. Miner võib seega sisestada ükskõik milliseid andmeid. Vaatame hiljem, kuidas seda vabadust kasutatakse.


Lisaks sellele valesisendile on üks või mitu täiesti tavalist väljundit, mis võimaldavad kaevandajal koguda bitcoin'id tasu eest ühel oma Bitcoin-aadressil. Need väljundid on UTXO, mis on lukustatud `scriptPubKey`ga (nt skript, mis osutab kaevandaja või basseini poolt kontrollitavale aadressile). Ainus eripära seisneb siin nende väärtuse arvutamise reeglis: coinbase'i väljundite kogusumma ei tohi kunagi ületada maksimaalset lubatud toetust, millele lisanduvad plokitasud.



Ajalooliselt siis, coinbase tehing on kokkuvõttes see lihtne skeem: võltsitud sisend viitab olematu UTXO, ja üks või mitu väljundid mõeldud jaotada plokk tasu võitnud kaevur. Tänapäeval ei ole coinbase aga enam piiratud selle jaotamise rolliga. Selle eriline positsioon plokis ja selle struktuuri suur paindlikkus on toonud kaasa uusi kasutusvõimalusi nii protokollis endas kui ka mining basseinide haldamise mehhanismides.



### Muud coinbase'i kasutusviisid



Aja jooksul on coinbase'i tehingust saanud eriti mugav sisestuspunkt, kuhu saab integreerida mitmesugust mining jaoks kasulikku teavet ja plokistruktuuri enda jaoks. Vaatame neid, et paremini mõista üldist coinbase'i organisatsiooni.



#### BIP-34



[BIP-34](https://planb.academy/resources/glossary/bip0034) on 2013. aasta märtsis kasutusele võetud fork soft, alustades plokist 227,930, millega võeti kasutusele Bitcoin plokkide 2. versioon. See uus versioon nõuab, et iga plokk sisaldaks coinbase'i tehingu `scriptSig`-sõnas loodava ploki kõrgust.



Ühest küljest selgitab see areng, kuidas võrk nõustub arendama plokkide struktuuri ja konsensuse reegleid. Teiseks tagab see iga ploki ja coinbase'i tehingu ainulaadsuse.



Seega ei ole coinbase'i `scriptSig` täiesti tasuta. Alates BIP-34 aktiveerimisest on see lihtsalt piiratud, et alustada selle ploki kõrgusega, milles see coinbase'i tehing sisaldub.



![Image](assets/fr/035.webp)



#### Ekstra-nonce



Nagu me nägime selle kursuse esimestes peatükkides, on kaevandajal 32-bitine nonce-väli ploki päises, mida ta muudab katse ja eksituse teel, et leida sihtmäärast väiksem või sellega võrdne hash. See 32-bitine ala võimaldab juba väga paljude kombinatsioonide uurimist, kuid kui mining raskusaste on kõrge, võib see vahemik suhteliselt lühikese ajaga täielikult ammenduda ja seega ei pruugi see anda ühtegi kombinatsiooni, mis annaks kehtiva hashi. Kui kõik võimalikud `nonce` väärtused on katsetatud edutult, peab kaevandaja seejärel muutma teist elementi, et muuta ploki pealkirja ja alustada uut katsete seeriat.



Kuna coinbase'i tehing pakub oma sisendi `scriptSig` kaudu vaba välja, on nonce'i ruumi laiendamiseks kasutatav lahendus selle `scriptSig` osa kasutamine. Seda nimetatakse üldiselt extra-nonce'iks. Extra-nonce'i muutmisega muudab kaevandaja coinbase'i `scriptSig`, st tehingu identifikaatorit, seejärel ploki Merkle'i juurt ja lõpuks ploki enda päise. Sel viisil saavad nad uurimiseks uue hashide otsinguruumi, ilma et nad peaksid muutma oma plokikandidaadi teisi komponente.



![Image](assets/fr/036.webp)



#### Basseinide ja kaevurite tuvastamine



Tänapäeval on väga suur osa maailma hashrate-st organiseeritud mining-baasides. Need struktuurid ühendavad üksikuid kaevandajaid, et ühendada oma tööd ja vähendada sissetulekute varieeruvust.



Operatiivsetel põhjustel kasutavad mining basseinid ka coinbase'i sisendi `scriptSig` vaba välja, et sisestada sinna mitmesugust teavet. Need varieeruvad basseiniti ja võrguprotokollide kaupa, kuid üldiselt sisaldavad igale kaevandajale määratud unikaalset identifikaatorit (sageli mitmest alajaotusest koosnev lisatähis), et vältida töö dubleerimist basseinis. Tavaliselt lisatakse ka koondtunnus, mida kasutatakse leitud plokkide avalikuks omistamiseks, mining statistika ja muudel jälgimise eesmärkidel.



![Image](assets/fr/037.webp)



#### SegWit kohustus



Alates SegWit pehme fork lubamisest 2017. aastal on tunnistajate andmed (st üldiselt allkirjad) eraldatud tehingu põhiandmetest, eelkõige [Bitcoin tehingute võltsitavuse probleemi](https://planb.academy/resources/glossary/malleability-transaction) parandamiseks. See eraldamine toob seega kaasa uue elemendi, mis tuleb blokis kinnitada.



Selleks grupeeritakse tunnistajad teise spetsiaalsesse Merkle'i puusse, mille juur on seejärel "OP_RETURN" väljundi kaudu coinbase'i tehingule kinnitatud.



![Image](assets/fr/038.webp)



Ma ei hakka seda mehhanismi siinkohal üksikasjalikumalt käsitlema, kuna see väljub käesoleva artikli raamidest, kuid pidage meeles, et alates SegWit kasutuselevõtust on coinbase'i tehing vahendiks, mis ankurdab plokki sõrmejälje, mis võtab kokku kõik SegWit tunnistajad. Tunnistajad paigutatakse iseseisvasse Merkle-puusse, selle puu juur kirjutatakse coinbase'i tehingu väljundisse ja see coinbase'i tehing ise lisatakse koos kõigi teiste tehingutega, mille juur ilmub ploki päises, peamisesse Merkle-puusse. Nii on tunnistajad, mis on salvestatud põhitehingu andmetest eraldi, ikkagi kinnitatud ploki päisesse.



![Image](assets/fr/039.webp)



#### Meelevaldsed sõnumid



Kuna `scriptSig` võimaldab vabalt sisestada suvalist teavet, mille kaevandaja ise valib, on mõned kasutanud võimalust lisada pigem isiklikke kui tehnilisi sõnumeid. Kõige kuulsam juhtum on muidugi Satoshi Nakamoto oma nüüdseks ikooniliseks saanud sõnumiga:



> The Times 03/Jan/2009 Kantsler on pankade teise päästepaketi äärel

See sõnum, mis on olemas Genesis plokis (Bitcoin kõige esimene plokk), on tegelikult kodeeritud heksadekaalarvudes coinbase'i tehingu "scriptSig":



```text
5468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73
```


![Image](assets/fr/034.webp)



### Lõpptähtaeg


Kui plokk on kaevandatud ja levitatud, ilmub coinbase'i tehing plokiahelas nagu iga teine tehing. See loob võitnud kaevandajale UTXO, mis võimaldab tal oma tasu kätte saada. Need UTXO ei ole siiski kohe kulutatavad: nende suhtes kehtib [tähtaeg](https://planb.academy/resources/glossary/maturity-period). See tähtaeg on määratud 100 plokki pärast mündipanga sisaldavat plokki. Konkreetselt öeldes peab coinbase'i tehingu kogusumma olema 101 kinnitust, et võitnud kaevandaja saaks selle väljundeid kulutada.


![Image](assets/fr/040.webp)


Selle eeskirja eesmärk on piirata ahelreorganiseerimise mõju majandusele. Nagu eelmistes peatükkides nägime, võib juhtuda, et samal kõrgusel leiavad erinevad kaevurid peaaegu samaaegselt kaks erinevat kehtivat plokki. Lühikeseks hetkeks võib võrk jaguneda: mõned sõlmed saavad esimesena ploki A, samas kui teised näevad esimesena plokki B. Seejärel kogub üks kahest harust järgnevate plokkide käigus rohkem tööd ja saab võrdlusharuks. Teine haru jäetakse kõrvale ja selle plokid muutuvad aegunuks. Selles sisalduvad tehingud võivad seejärel teoreetiliselt naasta mempoolidesse, mis ootavad kinnitust.



Tegelikkuses juhtub seda harva, sest tasuturu tulemusel ilmnevad sageli peaaegu samad tehingud kahes konkureerivas plokis samal kõrgusel. See on üks põhjusi, miks Bitcoin tehingut peetakse tavaliselt muutumatuks pärast kuut kinnitust: rohkem kui kuue ploki ümberkujundamine on nii ebatõenäoline, et seda võib mõistlikult pidada võimatuks.



![Image](assets/fr/041.webp)



Probleem nende ümberkorraldustega on coinbase'i tehingu puhul selles, et see ei ole tavaline tehing. See toob ringlusse täiesti uued bitcoinid. Kui plokkide tasu saaks kohe ära kulutada, võib tekkida problemaatiline kaskaadiolukord:




- kaevandaja kulutab bitcoine coinbase'ist,
- need bitcoinid ringlevad majanduses,
- siis loobuti algsest plokist lõpuks ümberkorraldamise käigus.



Ringluses olevad bitcoinid ei oleks siis kunagi olnud lõplikus ahelas olemas ja rida tehinguid, mis olid kehtivad väljaandmise ajal, muutuksid tagantjärele kehtetuks.



Lõpptähtaeg on piisavalt pikk, et muuta see stsenaarium ebarealistlikuks. 101 ploki ümberkorraldamist peetakse praktikas võimatuks (isegi kui selle tõenäosus jääb lõpmatult väikeseks). Me ei tea täpselt, miks Satoshi valis küpsusaja nii suure väärtuse, kuid tõenäoliselt valiti see nii, et mehhanism jääks toimivaks ka suuremate võrguhäirete korral.



See reegel takistab vastloodud plokkide preemiaraha ringluse alustamist enne, kui plokk, mis generated on kindlalt maetud suure hulga kogunenud töö alla.



---

Nüüd oleme jõudnud selgituse lõpuni, kuidas Bitcoin mining töötab. Nüüd peaks teil olema selge ülevaade põhilistest mehhanismidest.



Kursuse viimases osas pöördume tagasi konkreetsemate aspektide juurde, et näidata teile, kuidas Bitcoin mining realiseerub reaalses maailmas: selle industrialiseerimine, kasutatavad masinad, mängijate rühmitamine jne. Eesmärk on anda teile üldine ülevaade Bitcoin mining-st nii teoreetilisest ja protokollilisest vaatenurgast, mida me just nägime, kui ka selle praktilisest ja operatiivsest küljest.



# Tööstus Bitcoin mining


<partId>906a6e18-4718-4a1f-85f5-18854cebdf7c</partId>



## mining masinate areng


<chapterId>2d2f9055-75fd-4630-b493-a577d708a39f</chapterId>



Bitcoin algusaegadel ei olnud mining tööstuslik tegevus. See oli osa Bitcoin tarkvarast, mis käivitati personaalarvutis, sageli uudishimust, mõnikord võrgu toetamiseks ja teisalt bitcoinide hankimiseks, millel siis praktiliselt puudus turuväärtus.



Aastate jooksul on see tegevus muutunud: masinad on muutunud, raskused on plahvatuslikult kasvanud ja mining on muutunud omaette tööstusharuks. Vaatleme Bitcoin mining tegevusaspekte.



### Alustamine: mining koos protsessoriga



2009. aastal ja algusaastatel kasutati mining puhul peamiselt tavalise arvuti protsessorit. Bitcoin oli tollal vaid lihtne tarkvara, mis teenis wallet, sõlme ja kaevandaja ülesandeid. mining protsessis osalemiseks ja paljudel juhtudel ka plokkide leidmiseks piisas lihtsalt Satoshi Nakamoto tarkvara käivitamisest oma personaalarvutis.



Protsessor saab teha kõike, kuid see ei ole millegi jaoks optimeeritud. See täidab väga üldisi käske, millel on keeruline loogika. Sellise ülesande jaoks nagu plokkide päiste korduv hashimine ei ole see ideaalne vahend, kuid võrgu käivitamisel on raskusaste nii madal, et plokkide leidmiseks on see enam kui piisav.



See periood on oluline, sest see tuletab meile meelde üht olulist punkti: proof of work ei sõltu konkreetsest seadmekategooriast. Tähtis on võime arvutada hash'e kiiremini kui teised, antud hinnaga. Niipea kui tehniline eelis ilmneb, muutub see automaatselt majanduslikuks eeliseks. Kuid absoluutarvudes on ka täna võimalik püüda leida Bitcoin plokke tavalise protsessori abil. Sellist lähenemist kasutab näiteks projekt NerdMiner. Tõenäosus ploki leidmiseks on praktiliselt null, kuid tõenäosus on siiski lõpmatult väike.



https://planb.academy/tutorials/mining/hardware/nerdminer-c9826fd9-c2b4-4d1e-8c78-809122de1654

### Üleminek GPUdele



Peagi mõistsid kaevurid, et kitsaskohaks ei olnud mitte võimsus, vaid võime sooritada paralleelselt suur hulk sarnaseid operatsioone. See oli just see, mida graafikaprotsessorid (GPU) teha oskasid. Algselt oli GPU loodud selleks, et teha samu operatsioone suurel hulgal andmetega. Selline arhitektuur sobis suurepäraselt sellise ülesande jaoks nagu korduv hashing: mõne väga mitmekülgse tuuma asemel on teil sadu, siis tuhandeid ühikuid, mis on võimelised samu käske samaaegselt täitma.



Võrreldava energiatarbimise korral suudab GPU toota palju rohkem hashes'e sekundis kui CPU. Samal ajal oli bitcoini kurss dollari suhtes, selle väärtus tõusis ja tekkisid vahetusplatvormid. Sellest ajast alates hakkas mining olemus muutuma. See ei olnud enam ainult osalemine, vaid raha teenimine. Tekkisid spetsiaalsed konfiguratsioonid: mitme graafikakaardi ümber ehitatud masinad, mõnikord ilma ekraanita, minimaalse süsteemi ja spetsiaalse tarkvaraga, mille ainus eesmärk oli kaevandamine.



Just sel hetkel hakkasid mining raskused plahvatuslikult kasvama. Ajavahemikul 2010. aasta keskpaigast kuni 2011. aasta keskpaigani kasvas see isegi 1000 korda. Mehhaaniliselt algab spetsialiseerumine, nagu industrialiseerimise varajased vormid, ja tavakasutajatel - kes rahulduvad Bitcoin tarkvara käivitamisega oma personaalarvutis - on nüüd väga väike võimalus leida kehtivat plokki.



![Image](assets/fr/044.webp)



*Allikas: [CoinWarz.com](https://www.coinwarz.com/mining/bitcoin/hashrate-chart)*



GPU ajastu ja kaasaegse [ASIC](https://planb.academy/resources/glossary/asic) ajastu vahel oli vahepealne etapp: FPGAde kasutamine. FPGA on ümberprogrammeeritav komponent: seda saab konfigureerida nii, et see rakendab otseselt konkreetse arvutuse, antud juhul SHA256d, loogikahela. Idee oli liikuda veelgi kaugemale üldotstarbelisest riistvarast (CPU/GPU), et suurendada energiatõhusust. Kuid peagi rakendatakse virtuaalselt FPGAs tehtud parandusi füüsiliselt kiipidele endile: see on ASIC saabumine.



### ASIC saabumine



mining riistvara spetsialiseerumise viimane etapp oli ASIC (*rakendusspetsiifilised integraallülitused*). ASIC on kiip, mis on mõeldud ühe ülesande täitmiseks. Bitcoin mining puhul on see ülesanne just `SHA256d` täitmine maksimaalse kiirusega ja optimaalse energiatõhususega. Erinevalt GPU-st ei kasutata ASIC-d mängude, 3D-rendereerimise või tehisintellekti käivitamiseks. See on hashinguks, ja see on kõik.



![Image](assets/fr/045.webp)



*ASIC S21 XP, mille on tootnud Bitmain*



Sellisel spetsialiseerumisel on kaks peamist tagajärge:




- Esimene neist on hüpe jõudluses ja tõhususes. Võrreldava põlvkonna seadmete puhul toodab ASIC palju rohkem hashes'e sekundis kui GPU, tarbides samal ajal vähem energiat. Mining koos GPUga muutus kiiresti konkurentsivõimetuks: kuigi see töötas tehniliselt, ületasid elektrikulud enamikus kontekstides kaugelt oodatavat tulu;
- Teine on mudeli muutus: investeeringud on peamiselt suunatud tööstuslikule riistvarale. Mining tähendab nüüd selleks ettenähtud masinate ostmist, nende pidevat toitmist, jahutamist, hooldamist ja nende vananemist. Sest ASIC ei ole majanduslikult igavene: kui turule tuleb uus, tõhusam põlvkond, muutuvad vanad masinad üha vähem kasumlikuks, isegi kui nad jäävad toimima.



Sellest hetkest alates ei räägi me enam lihtsalt hobist. Me räägime sektorist, kus konkurentsivõime sõltub võrrandist:




- elektrienergia maksumus;
- seadmete maksumus ja amortisatsioon;
- võime jahtuda ja tegutseda suures ulatuses;
- masina kättesaadavus ja töökindlus;
- side kiirus;
- jne.



### Mining talud



Üks isoleeritud masin võib kaevandada, kuid koondades sadu, seejärel tuhandeid ASIC-sid ühte kohta, jagame püsikulusid, optimeerime logistikat ja liigume lähemale spetsialiseeritud andmekeskuse mudelile.



[mining-farm](https://planb.academy/resources/glossary/mining-farm) on kõige lihtsamal kujul hoone (või konteinerite kogum), mis on täidetud ASIC-ga, mis töötab 24/7. Väljakutse on nüüd stabiilsete töötingimuste säilitamine:




- tarnida suuri koguseid odavat ja stabiilset elektrienergiat;
- juhtida soojust, et vältida drosseldamist, sest energiatihedus on märkimisväärne;
- filtreerida tolmu, kontrollida niiskust, puhastada;
- masina jõudluse reaalajas jälgimine (temperatuurid, riistvaravigad, hashrate langused jne).



![Image](assets/fr/043.webp)



*Üks seitsmest hoonest, mis on pühendatud Bitcoin mining-le Riot Platforms'i Rockdale'i rajatises, Texase osariigis Austini lähedal. See on spetsiaalselt pühendatud immersioonile mining*



Mining on nüüd juhtinud tööstuslikud ettevõtjad, kellest mõned on börsil noteeritud ja kes ehitavad ja käitavad väga suuri põllumajandusettevõtteid. Nende hulka kuuluvad MARA Holdings (Nasdaq: `MARA`) ja Riot Platforms (Nasdaq: `RIOT`).



![Image](assets/fr/042.webp)



Isegi ilma kasumlikkuse mudelite üksikasjadesse laskumata on oluline mõista, miks mining on võtnud sellise kuju. Proof-of-work on konkurentsimehhanism: tõenäosus leida plokk ja seega teenida raha on proportsionaalne kasutatava hashrate osakaaluga. Selle tulemusel on pidev surve suurendada arvutusvõimsust, vähendada kulusid arvutusühiku kohta ja piirata kahjusid. Selle tulemusena muutuvad loomulikult atraktiivsemaks keskkonnad, mis pakuvad odavamat elektrit, jahutamiseks soodsat kliimat või rikkalikku energiainfrastruktuuri.



Mining Bitcoin on seega muutunud algusaegadel kõigile kättesaadavast tegevusest tegevuseks, kus domineerivad eriseadmed ja professionaalsed operatsioonid. See ei muuda protokolli reegleid. Teoreetiliselt võib igaüks kaevandada mis tahes masinaga. Kuid praktikas on ASIC raskusaste ja tõhusus muutnud kodumaise mining enamikus kontekstides suuresti konkurentsivõimetuks.



Loomulikult on veel olukordi, kus kodu mining võib huvi pakkuda, näiteks kui saate kasu väga odavast elektrist või kui kasutate oma kaevuri generated soojust talvel kodu kütmiseks. Kuid igal juhul peate ikkagi ostma ASIC kiibiga varustatud masina. Veelgi enam, kuna teie mining võimsus jääb Bitcoin võrgu suhtes äärmiselt väikeseks, peate leidma viisi, kuidas vähendada oma sissetuleku varieeruvust: just see on mining poolide roll, mida me arutame järgmises peatükis.



Kui soovite uurida koduseid mining lahendusi koos soojuse taaskasutamisega, on meil õpetused erinevate tööriistade kohta, nii valmis kui ka DIY:



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

https://planb.academy/tutorials/mining/hardware/attakai-0d177e6b-e167-4b25-8e38-4ec74213d1fb

## mining rühmadesse rühmitamine


<chapterId>c871bece-eebe-4ef4-9789-d47251f16c8b</chapterId>



Mining Bitcoin on seotud pidevate ja vältimatute kuludega, mille hulgas on eelkõige masina energiatarbimine. Need kulud tekivad sõltumata mis tahes tulemustest, kuigi mining tulud on oma olemuselt haruldased ja juhuslikud. Ploki leidmine sõltub ainult kaevandaja osakaalust hashrate, mis muudab tulu seda ettearvamatumaks, mida väiksem on see osakaal. Just see praktiline probleem viis kiiresti [mining-poolide](https://planb.academy/resources/glossary/pool-mining) laialdase kasutamiseni. Selles MIN 101 kursuse viimases peatükis tutvustan Bitcoin mining poolide põhimõtteid ja toimimist.



### Mis on mining bassein?



mining-pool on organisatsioon (sageli veebipõhine teenus), mis koondab paljude sõltumatute kaevurite arvutusvõimsust, et suurendada nende grupi plokkide leidmise sagedust. Kui bassein leiab ploki, jaotatakse ploki tasu osalejate vahel ümber vastavalt basseinisisestele reeglitele (mida käsitletakse MIN 201 kursusel, kuna need on MIN 101 jaoks liiga keerulised).



mining-poolis osalejaid nimetatakse siis sageli "[hasheriteks](https://planb.academy/resources/glossary/hasher)", mitte "kaevandajateks", kuna nad ei tee enam kogu mining tööd, vaid lihtsalt hashivad neile poolilt edastatud andmeid.



Olge ettevaatlik, et mitte segi ajada mining pooli mining farmiga. Need on kaks erinevat mõistet. Nagu me eelmises peatükis nägime, on farmis füüsiline asukoht, kus üks üksus haldab mitmeid mining masinaid. Pool seevastu on eelkõige virtuaalne rühmitus: tuhanded, sageli geograafiliselt hajutatud masinad töötavad ühise koordineerimise all. Farm võib siiski osaleda ja sageli osalebki talus.



![Image](assets/fr/048.webp)



### Sissetulekute erinevuse vähendamine



Miks siis liituda basseiniga? Lihtsalt sellepärast, et mining tegevuse tulemus on tõenäosuslik: iga hash-katse puhul on väga väike tõenäosus, et see vastab raskusastme eesmärgile ja annab seega kehtiva ploki.



Väga pika aja jooksul peaks teie keskmine sissetulek olema proportsionaalne teie osaga hashrate üldisest sissetulekust. See põhimõte tuleneb otseselt tõenäosuse seadustest: iga hash-arvutus kujutab endast sõltumatut juhuslikku loosimist ja suurte arvude seaduse kohaselt läheneb teie poolt avastatud plokkide sagedus matemaatiliselt teie osakaalule võrgu hashrate kogusummast. Lühikeses ja keskpikas perspektiivis võib teie tegelik tulu siiski olla äärmiselt ebaregulaarne. Seda erinevust teoreetilise keskmise ja juhusliku tegelikkuse vahel nimetame matemaatikas **varieeruvuseks**.



Siin on lihtne näide põhimõtte illustreerimiseks:




- Bitcoin võrk toodab keskmiselt 144 plokki päevas (umbes üks plokk iga 10 minuti järel);
- Kui teil on "0,0001 %" kogu hashrate-st, on teie eeldatav väärtus "144 × 0,000001" ehk "0,000144" plokki päevas;
- Teisisõnu, te peaksite leidma ploki keskmiselt iga `1 / 0,000144` päeva järel, st iga 6944 päeva järel ehk umbes 19 aasta järel.



Kuid see väärtus vastab ainult matemaatilisele ootusele: avastamisaegade jaotus järgib juhuslikku seadust, nii et praktikas on täiesti võimalik, et isegi väga pika aja jooksul ei avastata kunagi ühtegi plokki. Võite olla ebaõnne ja väga pikka aega mitte midagi leida, makstes samal ajal jooksvaid kulusid (elekter, hooldus, seadmete amortisatsioon...).



mining-pool muudab selle probleemi olemust: hashrate-de kombineerimisel leiab pool sagedamini plokke. Iga osaleja nõustub siis saama ainult osa igast leitud plokist, kuid palju sagedamini. See on üleminek väga volatiilsest, laialt hajutatud sissetulekust korrapärasemaks sissetulekuks, mis on seotud preemiate jagamise ja teenustasude maksmisega.



### Miks varieeruvus väheneb, kui te rühmitate koos?



Mida suurem on teie arvutusvõimsus, seda suurem on leitud plokkide eeldatav sagedus. Veelgi olulisem on see, et mida sagedamini toimuvad sündmused, seda lähemal on täheldatud tulemused statistilisele keskmisele antud ajavahemiku jooksul.



Üksinda tegutsedes võib väikekaevandaja olla aastaid ilma ühegi plokita, siis saab ta ühel päeval suure väljamakse ja siis mitte midagi. Poole puhul kehtib sama tõenäosuslik reaalsus, kuid see on kollektiivsel skaalal silutud: pool leiab plokke sagedamini ja ümberjaotamine muudab need sündmused korrapärasemateks väljamakseteks iga osaleja jaoks. **mining-pool müüb seega mining aktiivsuse prognoositavust**.



### Ajaloolised vaatamisväärsused



Nagu nägime eelmises peatükis, võis mining algul teha üksi tavalise arvutiga, sest raskusaste oli väga madal. Kuid kui globaalne hashrate plahvatuslikult kasvas (GPU, seejärel ASIC), muutus mining soolosõit enamiku osalejate jaoks väga aeganõudvaks hasartmänguks.



Esimesed basseinid loodi just sellele uuele reaalsusele reageerides. Braiins Pool (endine Slush Pool / Bitcoin.cz) on esimene Bitcoin mining bassein: see kaevandas oma esimese ploki 16. detsembril 2010. aastal. Selle esimese mining pooli edu oli kiire, sest vaid mõne päevaga hõivas ta peaaegu 3,5% ülemaailmsest hashrate-st.



![Image](assets/fr/047.webp)



Tehnilisest küljest struktureeriti basseinid seejärel spetsiaalsete kommunikatsiooniprotokollide ümber basseini ja kaevurite vahel (nt [Stratum](https://planb.academy/resources/glossary/stratum), seejärel Stratum V2), et tõhusalt korraldada hajutatud tööd. Neid kontseptsioone vaatleme lähemalt meie MIN 201 koolituskursusel.



### Kaasaegne olukord



Kirjutamise ajal (2026. aasta alguses) on globaalne Bitcoin hashrate suurusjärgus zetta-hash sekundis (= 1 000 EH/s = 1 000 000 000 000 000 000 000 000 hashes sekundis) ja peaaegu kõik leitud plokid pärinevad mining basseinidest.



Järgnevalt on esitatud peamiste mining koondumiste ja nende vastavate hashrate osakaalude senine järjestus. See järjestus võib tõenäoliselt muutuda selleks ajaks, kui te seda kursust loete. Värskete andmete saamiseks külastage [mempool.space](https://mempool.space/graphs/mining/pools).



![Image](assets/fr/046.webp)



| Ranking    | Pool           | Blocks found  | Hashrate share   |
| ---------: | -------------- | ------------: | ---------------: |
|          1 | Foundry USA    |          1297 |           29.57% |
|          2 | AntPool        |           755 |           17.21% |
|          3 | ViaBTC         |           514 |           11.72% |
|          4 | F2Pool         |           467 |           10.65% |
|          5 | SpiderPool     |           349 |            7.96% |
|          6 | MARA Pool      |           229 |            5.22% |
|          7 | SECPOOL        |           197 |            4.49% |
|          8 | Luxor          |           128 |            2.92% |
|          9 | Binance Pool   |           105 |            2.39% |
|         10 | OCEAN          |            78 |            1.78% |
|         11 | SBI Crypto     |            70 |            1.60% |
|         12 | Braiins Pool   |            54 |            1.23% |
|         13 | WhitePool      |            33 |            0.75% |
|         14 | Mining Squared |            26 |            0.59% |
|         15 | BTC.com        |            16 |            0.36% |
|         16 | Poolin         |            14 |            0.32% |
|         17 | ULTIMUSPOOL    |            14 |            0.32% |
|         18 | GDPool         |            12 |            0.27% |
|         19 | Innopolis Tech |            11 |            0.25% |
|         20 | NiceHash       |             8 |            0.18% |
|         21 | RedRock Pool   |             8 |            0.18% |
|         22 | Unknown        |             2 |            0.05% |
|         23 | Public Pool    |             1 |            0.02% |

*Allikas [mempool.space](https://mempool.space/graphs/mining/pools), ühe kuu andmed, 16. detsember 2025 kuni 16. jaanuar 2025.*



Edasijõudnute kursusel läheme lähemalt sisse basseinide sisemisse toimimisse (aktsiad, võrguprotokollid, makseviisid...), sest just siin tulevad mängu detailid, mis määravad nii kaevandaja kasumlikkuse kui ka võimalikud tagajärjed Bitcoin-le.



---

Oleme nüüd jõudnud MIN 101 lõpuni. Täname teid, et olete seda lõpuni jälginud. Kui soovite hinnata kursuse jooksul omandatud oskusi, ootab teid järgmises osas ees lõpueksam.



Äsja omandatud põhiteadmistega saate nüüd mining kohta Plan ₿ Academy edasijõudnute kursusi, kas siis teoreetilisi, nagu see, või praktilisemaid kursusi, et ka teie saaksite hakata osalema Bitcoin mining!



# Viimane osa


<partId>eced8ca1-971d-4a22-9254-dbf8bce15d1b</partId>



## Arvamused ja hinnangud


<chapterId>dc005a96-f4b4-42be-ab72-d4624c110716</chapterId>


<isCourseReview>true</isCourseReview>

## Lõpueksam


<chapterId>959f06cf-fd66-4f29-b7ee-665bfedfea0d</chapterId>


<isCourseExam>true</isCourseExam>

## Kokkuvõte


<chapterId>f16a4e42-c16e-466b-ad16-f42b5360f510</chapterId>


<isCourseConclusion>true</isCourseConclusion>