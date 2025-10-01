---
name: Esimese Bitcoin sõlme seadistamine
goal: Bitcoin sõlme mõistmine, paigaldamine, konfigureerimine ja kasutamine
objectives: 


  - Mõista Bitcoin sõlme rolli ja eesmärki.
  - Määrake kindlaks erinevad olemasolevad riist- ja tarkvaralahendused.
  - Paigaldage ja konfigureerige Full node (Bitcoin core).
  - Kasutage Interface vihmavarju ja lisage kasulikke rakendusi.
  - Ühendage isiklik Wallet oma sõlme.
  - Tutvuge täiustatud seadistuste ja parimate turvatavadega.


---
# Hakka suveräänseks bitcoineriks



Ilmselt olete tuttav ütlusega "Not your keys, not your coins", mis julgustab oma bitcoinide isehoidmist. Oma võtmete hoidmine on tõepoolest oluline esimene samm, kuid sellest ei piisa. Tõelise rahalise suveräänsuse saavutamiseks tuleb teil paigaldada ja kasutada ka oma Bitcoin sõlme. See kursus on mõeldud selleks, et juhendada teid selle põhilise sammu kaudu teie Bitcoin teekonnal!



BTC 202 on kättesaadav kursus, mille eesmärk on õpetada teile, kuidas oma Bitcoin sõlme keerata, isegi kui te ei ole tehniline ekspert. Alustame sellega, et defineerime, mis on Bitcoin sõlme, milleks see on mõeldud ja miks on hädavajalik seda ise keerata. Seejärel juhatan teid samm-sammult läbi riistvara valimise, vajaliku tarkvara paigaldamise, Wallet ühendamise ja esimeste võimalike optimeerimiste tegemise, et seda edasi viia.



Bitcoin-sõlme kasutamine ei ole ainult ekspertide jaoks võimalus, vaid hädavajalik. See on vastupidavusvahend, mida iga kasutaja peab mõistma ja rakendama. See kursus on teie lähtepunkt suveräänseks bitcoineriks saamise teel!




+++




# Sissejuhatus


<partId>fc46ccd7-5d6d-40c3-9e9f-fbbb323c760a</partId>




## Kursuse ülevaade


<chapterId>916b1f86-38a4-4ede-bdb7-83841d5a7abe</chapterId>



Tere tulemast BTC 202, kus õpid, kuidas Bitcoin sõlme lihtsalt ja iseseisvalt paigaldada, konfigureerida ja kasutada. Kuid see pole veel kõik: te saate ka rohkem teada sõlmede kohast ja funktsioonist Bitcoin süsteemis. Kursusel vahelduvad teoreetilised selgitused ja juhendatud praktilised harjutused.



### 1. osa - Sissejuhatus



Selles kursuse esimeses osas selgitame põhimõisteid ja seejärel liigume täpsemate määratluste juurde. Mis on sõlm? Millised on erinevused sõlme, Wallet ja Miner vahel? Seejärel saate teada Bitcoin core ja protokolli rakendused. Eesmärk on rääkida ühes keeles, vältida segadust ja luua kindel teoreetiline alus.



### 2. osa - Suveniirseks bitcoineriks saamine



Selles teises osas selgitan kõigepealt, miks on oluline käivitada oma Bitcoin sõlme. Seejärel uurime erinevaid olemasolevaid sõlmede tüüpe (täielik, pruned, SPV...), nende toimimist ja tehnilist mõju.



Seejärel anname teile ülevaate Bitcoin-sõlme käitamiseks saadaval olevast tarkvarast, sealhulgas selle eelistest ja puudustest. Lõpetuseks anname mõned väga praktilised soovitused teie vajadustele ja eelarvele sobiva riistvara valimiseks.



Seetõttu illustreerib see lõik suveräänse bitcoineri teed: mõista, miks on vaja käivitada sõlme, valida sõlme tüüp, selle valiku põhjal valida tarkvara ja sõltuvalt valitud tarkvarast määrata sobiv riistvara.



### 3. osa - Bitcoin sõlme lihtne paigaldamine



Kui see ettevalmistus on lõpetatud, on aeg asuda praktikasse, kus 3. osa on pühendatud Umbrelile: kodusele pilve-OS-le, mis lihtsustab isehostimist ning Bitcoin ja Lightning-sõlme paigaldamist.



Pärast Umbreli lühitutvustust anname üksikasjaliku õpetuse, mis juhatab teid läbi paigaldamise ja konfigureerimise protsessi teie enda DIY-masinal. Selle osa eesmärk on selge: saada oma esimene täielikult toimiv ja sünkroniseeritud Bitcoin sõlme.



### 4. osa - Wallet ühendamine sõlmpunktiga



Nüüd, kui olete Bitcoin sõlme seadistanud, on aeg seda kasutada! Selles jaotises saate teada, kuidas ühendada oma Wallet haldustarkvara (nagu Sparrow wallet) oma Address indekseerijaga (Electrs või Fulcrum) või otse Bitcoin core-ga, nii et te ei sõltu enam avalikest serveritest.



Samuti uurime indekseerijate rolli ja erinevaid meetodeid, kuidas oma sõlme ühendada (LAN, Tor, Tailscale jne). Lõpuks vaatame viimases peatükis üle kõige kasulikumad rakendused, mis on Umbrelis igapäevase bitcoineri jaoks saadaval.



### 5. osa - Täiustatud mõisted ja parimad tavad



Selles BTC 202 viimases osas on eesmärk süvendada oma teadmisi. Kõigepealt vaatleme parimaid tavasid, mida oma uue Bitcoin sõlme puhul kasutusele võtta ja kuidas seda pikaajaliselt hooldada.



Seejärel võtame aega, et vaadata üle mõned varem kursusel käsitletud teooriad, sealhulgas IBD protsessi ja peer discovery üksikasjalikult mõista, uurida sõlme anatoomiat ja lõpuks õppida, kuidas kasutada "Bitcoin.conf" faili oma seadete peenhäälestamiseks.



### 6. osa - Lõpposa



Nagu kõigi Plan ₿ Network kursuste puhul, leiate lõpuosast lõpueksami, millega testite oma teadmisi Bitcoin sõlmede kohta.



Kas olete valmis oma esimese Bitcoin sõlme sisse lülitama? Võtke suund suveräänsusele!



## Mis on Bitcoin sõlme?


<chapterId>0a9fd4e0-94ab-405e-924c-023397393027</chapterId>



Nagu selle looja Satoshi Nakamoto kirjeldas, kujutab Bitcoin endast vastastikust elektroonilist sularahasüsteemi. See lihtne lause, mis on valge raamatu pealkiri, sisaldab palju vihjeid Bitcoin olemuse kohta:




- Kõigepealt kirjeldab Satoshi Bitcoin kui "süsteemi", teisisõnu riist- ja tarkvarakomponentide ühtset kogumit, mis suhtlevad omavahel, et pakkuda konkreetset teenust või täita konkreetset funktsiooni;
- Seejärel selgitab ta, et see süsteem võimaldab kasutada elektroonilist sularaha, s.t immateriaalse valuuta vormi;
- Lõpuks juhib ta tähelepanu sellele, et see süsteem ei sõltu ühestki kesksest üksusest: see on "peer-to-peer", mis tähendab, et süsteemi haldavad kasutajad ise.



Kuna Bitcoin on süsteem, tuleb seda tingimata käivitada arvutites. Ja kuna tegemist on võrdõiguslikkusega, on kasutajad ise need, kes võtavad vastutuse nende masinate käitamise eest. Me nimetame "Bitcoin-sõlmeks" just seda arvutit, millel töötab Bitcoin protokolli (nagu Bitcoin core, kuid selle juurde tuleme hiljem tagasi) rakendav tarkvara. See võimaldab Bitcoin-l toimida ilma keskse asutuseta: valideerimine toimub hajutatult, tuhandete kasutajate tuhandete sõltumatute masinate poolt.



![Image](assets/fr/047.webp)



Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. https://Bitcoin.org/Bitcoin.pdf



Just need kasutajad tagavad Bitcoin turvalisuse. Nagu Eric Voskuil oma raamatus *Cryptoeconomics* selgitab, ei sõltu Bitcoin turvalisus ei Blockchain-st, hashinguvõimest, valideerimisest, detsentraliseerimisest, krüptograafiast, avatud lähtekoodist ega mänguteooriast. Bitcoin turvalisus sõltub eelkõige isikutest, kes on valmis end isikliku riski suhtes ohtu seadma. Detsentraliseerimine võimaldab seda riski jaotada suure hulga üksikisikute vahel ja ainult nende võime vastu seista tagab süsteemi töökindluse.



Seda põhimõtet on lihtne mõista: kui Bitcoin sõltuks ühestainsast sõlmpunktist, mis kuulub ühele isikule, piisaks selle isiku vangistamisest, et sulgeda võrk, sest ta üksi võtaks enda kanda kõik riskid. Kui võrgus on kümneid tuhandeid sõlmi, mis on üle kogu maailma laiali, on risk hajutatud: Bitcoin sulgemiseks tuleks neutraliseerida kõik need operaatorid.



![Image](assets/fr/048.webp)



Seega võime eristada ja nimetada mitmeid mõisteid, et selgitada asju selle kursuse edasiseks ajaks:




- Bitcoin valuuta: selles süsteemis tehtavate tehingute jaoks kasutatav arvestusühik;
- Bitcoin võrk: kõigi ühendatud sõlmede kogum;
- Bitcoin sõlmed: masinad, mis kasutavad Bitcoin rakendust;
- Bitcoin rakendused: tarkvara, mis tõlgib protokolli käivitatavateks käskudeks;
- Bitcoin protokoll: süsteemi toimimist reguleerivate eeskirjade kogum;
- Süsteem Bitcoin: kõigi nende Elements sidus kombinatsioon.



### Bitcoin sõlme roll



Bitcoin sõlmed moodustavad koos nn Bitcoin võrgu. Need võimaldavad kogu süsteemi iseseisvat toimimist ilma keskasutuse või serverite hierarhia kasutamiseta.



Bitcoin oli algusest peale kavandatud nii, et iga kasutaja saaks kasutada isiklikku sõlme. See kehtib ka tänase Bitcoin core tarkvara puhul, mis ühendab Wallet ja sõlme rollid. Kuid tänapäeval on see funktsioon sageli lahutatud: paljud tänapäevased Bitcoin rahakotid on lihtsalt rahakotid, mis ühenduvad väliste sõlmedega (mis kuuluvad samale isikule või mitte).



### Hoidke Blockchain



Sõlme esimene ülesanne on säilitada Blockchain kohalik koopia. Double-spending vältimiseks Bitcoin-l ilma keskasutust kaasamata peab iga kasutaja kontrollima, et süsteemis ei oleks ühtegi tehingut. Ainus võimalus selles kindel olla on teada kõiki Bitcoins tehtud tehinguid. Sel põhjusel on kõik tehingud ajatempliga varustatud ja rühmitatud plokkidesse ning iga sõlme salvestab kogu Blockchain.



> Ainus viis kinnitada tehingu puudumist on olla teadlik kõigist tehingutest.

Nakamoto, S. (2008). *Bitcoin: Peer-to-Peer elektroonilise sularaha süsteem*. https://Bitcoin.org/Bitcoin.pdf



Blockchain on seega arenev register: iga kord, kui Miner avaldab uue ploki, kontrollib sõlm selle kehtivust enne selle lisamist oma ahela kohalikku koopiasse. Tänase seisuga (juuli 2025) ületab Blockchain kogu suurus 675 GB ja see suurus kasvab jätkuvalt, sest keskmiselt iga 10 minuti tagant lisatakse uus plokk.



![Image](assets/fr/049.webp)



Samuti säilitab sõlmpunkt kohalikku registrit kõigi igal ajahetkel olemasolevate UTXOde kohta, mida nimetatakse **UTXO komplektiks**. See andmebaas sisaldab kõiki kasutamata Bitcoin fragmente. Seda teemat käsitleme üksikasjalikult uuesti kursuse viimases osas.



### Tehingute kontrollimine ja levitamine



Teiseks sõlme rolliks on tagada tehingute kontrollimine ja levitamine. Kui uus tehing jõuab sõlme (kas Wallet tarkvara või mõne teise sõlme kaudu), kontrollib see, kas see vastab reeglistikule (konsensusreeglid ja releereeglid). Näiteks:




- kulutatud bitcoinid peavad olema olemas tema UTXO komplektis (kulutamata väljundite andmebaas);
- allkiri peab olema kehtiv ja kõik kulutuste tingimused peavad olema täidetud (kehtiv skript);
- väljundite kogusumma ei tohi ületada sisendite kogusummat, mis tähendab, et kulud ei saa olla negatiivsed.



![Image](assets/fr/050.webp)



Pärast kinnitamist salvestatakse tehing sõlme Mempool-sse, mis on kinnitamata tehingute jaoks reserveeritud ajutine mäluruum, ja seejärel edastatakse see teistele võrgupartneritele, kellega see on ühendatud. See jaotus- ja valideerimismehhanism jätkub sõlmedest sõlme vahel. Sel viisil levib tehing üle kogu Bitcoin võrgu ja iga sõlme salvestab selle Mempool-s, kuni Miner lisab selle kehtivasse plokki, mis seejärel tegutseb selle esimese kinnituse alusel.



### Kontrollida ja jaotada plokid



Kolmas sõlme roll on kaevandatud plokkide haldamine. Kui Miner avastab uue ploki koos kehtiva Proof of Work-ga, edastatakse see võrgus. Sõlmed võtavad selle vastu, kontrollivad, et see vastab kõigile protokollireeglitele, ja seejärel integreerivad selle oma Blockchain kohalikku koopiasse, kui see on kehtiv. Nagu tehingute puhul, edastatakse äsja valideeritud plokid seejärel kõigile sõlmega ühendatud võrdsetele osapooltele. See protsess jätkub seni, kuni kõik Bitcoin võrgu sõlmed on uuest plokist teadlikud.



![Image](assets/fr/051.webp)



## Mis vahe on vibul ja Wallet-l?


<chapterId>de5af634-a628-4b90-b869-468c208e178b</chapterId>



Bitcoin kasutamisel on oluline eristada kahte erinevat tüüpi tarkvara: sõlme ja Wallet.



Nagu eespool mainitud, on Bitcoin-sõlm tarkvara, mis osaleb aktiivselt võrdõigusvõrgus. See täidab kolme peamist ülesannet:




- gW-77 varukoopia,
- tehingu valideerimine ja edastamine,
- plokkide valideerimine ja relee.



Bitcoin Wallet seevastu on tarkvara, mis on mõeldud teie privaatvõtmete salvestamiseks ja haldamiseks. Need võtmed võimaldavad teil oma bitcoine kulutada, rahuldades lukustusskripte (tavaliselt allkirja kaudu). Wallet võib luua ühenduse sõlme (kas kohaliku või kaugseirega), et konsulteerida Blockchain olekuga ja edastada tema poolt tehtud tehinguid, kuid ta ei ole sellisena võrgus osaleja.



Mõnel juhul on need kaks funktsiooni ühe ja sama tarkvara sees, nagu näiteks Bitcoin core puhul, mis on nii Full node kui ka Wallet. Paljud populaarsed Wallet programmid (Sparrow, BlueWallet jne) nõuavad aga ühendust välise sõlme (kas teie enda või kolmanda osapoolega), et edastada tehinguid ja määrata Wallet saldo.



![Image](assets/fr/052.webp)



## Mis vahe on sõlme ja Miner vahel?


<chapterId>d2992614-7ab7-4bf9-81b1-f548cda67257</chapterId>



Sõlme ja Miner mõisted aetakse sageli segamini. Ometi täidavad need kaks Elements süsteemis täiesti erinevaid funktsioone.



Kui Satoshi Nakamoto 2009. aastal Bitcoin käivitas, eeldati algselt, et iga kasutaja osaleb võrgustikus tervikuna. Seega ühendas algne Bitcoin tarkvara mitu funktsiooni korraga: see toimis Wallet, sõlmpunktina ja ka Miner, mis oli võimeline uusi plokke genereerima. Tollal oli Mining raskusaste väga madal. Kõik, mida tuli teha, oli käivitada Bitcoin tarkvara oma arvutis, et leida plokke ja saada tasu eest bitcoine.



Bitcoin järkjärgulise populariseerimisega ja kaevurite arvu suurenemisega on Mining konkurentsimaastik siiski radikaalselt muutunud. Tänapäeval on Mining muutunud äärmiselt konkurentsivõimeliseks tegevuseks, kus domineerivad spetsialiseeritud infrastruktuuriga varustatud tööstuslikud ettevõtjad. Uue ploki kaevandamiseks vajalik võimsus on nüüd nii suur, et üksikkasutajal on praktiliselt võimatu seda saavutada ainult tavalise arvuti abil. Seetõttu kasutatakse Mining kaevandamisel nüüd peamiselt spetsiaalseid masinaid, mida nimetatakse ASIC-deks (*rakendusspetsiifilised integraallülitused*). Need kiibid on optimeeritud ainult Bitcoin puhul Mining jaoks kasutatud algoritmi SHA-256 kahekordseks käivitamiseks.



![Image](assets/fr/053.webp)



Selle arengu käigus on Bitcoin sõlme ja Miner roll muutunud selgelt eristuvaks. Nagu eespool näidatud, on Bitcoin sõlme roll puhtalt informatiivne ja valideerimisega seotud. Miner roll on teistsugune:




- See valib Mempools olevad tehingud.
- See loob kandidaatbloki, mis integreerib need tehingud.
- Ta otsib katse ja eksituse teel kehtivat Proof of Work.
- Kui ta leiab kehtiva tõendi, edastab ta ploki oma sõlme kaudu teistele sõlmedele.



Miner vajab võrguga suhtlemiseks Bitcoin sõlme.



Mõnikord eristatakse ka Miner rolli kopterist. Hakkur on masin, mille ülesanne on Hash malliplokid, mis on tarnitud basseiniserveri poolt, otsides häkke, mis vastavad aktsiate jaoks määratletud raskusastme eesmärgile, mitte aga Bitcoin-le. Ülejäänud Mining protsessi, mis hõlmab tegelikku plokkide konstrueerimist, tehingu valimist või Bitcoin enda raskusastme järgi Bitcoin otsimist, samuti jaotamist, teostavad otse basseinid.



![Image](assets/fr/054.webp)



Lõpuks on Miner ja sõlme vahel oluline erinevus majandusliku stiimuli osas. Bitcoin sõlme käitamine ei anna otsest rahalist kasu. Seevastu Mining-s osalemine toob kasu (toetused ja tehingutasud) iga leitud ploki eest.



Teises osas uurime üksikasjalikumalt Bitcoin-sõlme paigaldamise ja kasutamise praktilisi ja isiklikke eeliseid, mis ei ole ainult rahalised.



## Bitcoin core ja protokollide rakendamine


<chapterId>72381876-9317-4faa-8d41-2b252a945b8a</chapterId>



Bitcoin protokoll ei ole tarkvara: see on võrgu kasutajate vahel jagatud vaikivate reeglite kogum. See määratleb tehingu kehtivuse tingimused, raha loomise mehhanismid, plokkide vormingu, Proof-of-Work tingimused ja paljud muud spetsifikatsioonid. Selle protokolliga suhtlemiseks peavad kasutajad käivitama tarkvara, mis rakendab neid reegleid: seda nimetatakse Bitcoin **rakenduseks**.



Rakendus on seega sõlmede tarkvara: programm, mis suudab suhelda teiste Bitcoin võrgu masinatega, laadida alla, kontrollida, salvestada ja levitada plokke ja tehinguid ning jõustada kohalikul tasandil konsensuse ja relee reegleid. Iga implementatsioon on protokolli konkreetne tõlgendus, mis on kirjutatud konkreetses programmeerimiskeeles ning millel on oma arhitektuur, jõudlus ja ergonoomika. Igal rakendusel on ka oma arendusorganisatsioon, millel on oma vastutuse jaotus.



Nende rakenduste hulgas domineerib üks neist kaugelt: **Bitcoin core**.



![Image](assets/fr/055.webp)



### Ajalooline rakendamine, millest on saanud võrdlusalus



Bitcoin core on Bitcoin protokolli võrdlustarkvara. See on tuletatud Satoshi Nakamoto 2008-2009 kirjutatud algsest koodist ja on selle otsene jätk. Algselt oli see tuntud kui "*Bitcoin*", seejärel "*Bitcoin QT*" (tänu graafilise Interface lisamisele Qt raamatukogu kaudu), kuid 2014. aastal nimetati see ümber "*Bitcoin core*", et selgelt eristada tarkvara võrgustikust. Alates versioonist 0.5 levitatakse seda kahe komponendiga: `Bitcoin-qt` (graafiline Interface) ja `bitcoind` (käsurea Interface).



Teoreetiliselt ei esinda Bitcoin core protokolli Bitcoin; pigem on see vaid üks rakendamine paljude seas. Seda eristab aga selle massiline kasutuselevõtt, vanus, koodi tugevus ja arendusprotsessi rangus. Sellest tulenevalt on Bitcoin core poolt kohaldatavad reeglid praktikas de facto Bitcoin protokolli reeglid: kasutajad, arendajad, kaevandajad ja ökosüsteemi teenused viitavad peaaegu eranditult sellele protokollile.



### Rakenduste praegune jaotus



Vastavalt [Luke Dashjr](https://luke.dashjr.org/programs/Bitcoin/files/charts/software.html) (tuntud arendaja ökosüsteemis) poolt augustis 2025 kogutud andmetele on rakenduste jaotus võrgu avalike sõlmede vahel järgmine:




- Bitcoin core**: 87.3% sõlmedest
- Bitcoin Knots**: 12.5
- Muud kumulatiivsed rakendused**: 0.2% (btcsuite, Bcoin, BTCD...)



![Image](assets/fr/056.webp)



Teisisõnu, umbes 9 avalikku sõlme 10-st kasutab Bitcoin core. Ülejäänud võrk tugineb marginaalsematele klientidele (kuigi Knoti osakaal on viimastel kuudel järsult tõusnud, eriti seoses aruteludega OP_RETURN suuruse piirangu üle). Neid alternatiivseid rakendusi hooldab sageli üks inimene või väike meeskond.



**Märkus:** Need arvud on siiski hinnangulised, kuna need põhinevad peamiselt *kuulates sõlmedel*, st sõlmedel, mis võtavad vastu sissetulevaid ühendusi (avatud pordiga 8333). Mitte-kuulavaid sõlmi* on palju keerulisem arvutada, sest nendega ei ole võimalik otse ühendust luua: tuleb oodata, et algatus tuleb neilt, väljamineva ühenduse näol. Luke Dashjr'i sait väidab, et püüab ka neid *non-listening nodes* loendada, kuid täiesti täpseid andmeid nende kohta on endiselt võimatu saada ja nende statistika uuendamine jääb paratamatult tegelikkusele maha.



### Bitcoin core sisemine toimimine



Bitcoin core on kirjutatud C++ keeles. Samuti on tegemist avatud lähtekoodiga projektiga, mida hooldab arendajate kogukond, kes töötavad vabatahtlikult või saavad palka erinevatelt üksustelt (sageli ökosüsteemi ettevõtetelt, kellel on huvi Core'i arendamise vastu). [Kood asub GitHubis](https://github.com/Bitcoin/Bitcoin) ja arendus järgib ranget:




- Kaastöötajad** esitavad ettepanekuid _väljaandmistaotluste_ (PR) vormis. Põhimõtteliselt võib igaüks teha muudatusettepaneku, kuid see peab olema testitud, dokumenteeritud ja läbima vastastikuse eksperdihinnangu.
- **Hooldajatel** on õigus kiita ja ühendada PR-id. Nemad on need, kes tagavad projekti sidususe ja stabiilsuse. Juulis 2025 on neid viis: Hennadii Stepanov, Michael Ford, Andrew Chow, Gloria Zhao ja Ryan Ofsky.
- Alates 2023. aasta veebruarist ei ole olnud **peaminevat hooldajat**. Seda rolli täitis algselt Satoshi Nakamoto Bitcoin käivitamisel, seejärel Gavin Andresen pärast Nakamoto lahkumist 2011. aasta alguses ja lõpuks Wladimir J. Van Der Laan aastatel 2014-2023.



![Image](assets/fr/057.webp)



Bitcoin core arendamisel järgitakse meritokraatlikku loogikat: uusi kaasajaid julgustatakse koodi läbi vaatama ja testima, enne kui nad ise muudatusi välja pakuvad. Otsused põhinevad tehnilisel konsensusel ja suuremad muudatused (eriti konsensuslikes valdkondades) nõuavad eelnevaid arutelusid avalikes kanalites, näiteks postiloendis või PR-klubides.



### Muud Bitcoin rakendused



Kuigi vastuvõtmise osas on see marginaalne, on ka teisi kliente olemas. Peamine neist on Luke Dashjr'i poolt välja töötatud Bitcoin Knots, mis on Fork Bitcoin core-st, mis sisaldab täiendavaid võimalusi ja konservatiivsemat lähenemist arendusele. Nende hulka kuuluvad rangemad piirangud tehinguformaatidele.



![Image](assets/fr/058.webp)



Võime ka mainida:




- Libbitcoin**: Amir Taaki poolt välja töötatud ja Eric Voskuili poolt hooldatud modulaarne C++ raamatukogu;
- Bcoin**: JavaScripti rakendus, mida enam aktiivselt ei hooldata;
- BTCD/btcsuit**e: rakendamine Go keeles.



Need projektid aitavad kaasa ökosüsteemi mitmekesisusele, kuid nende kasutuselevõtt on endiselt väga piiratud, mistõttu on Bitcoin core-l raske iseseisvalt areneda.



### Core arendajate jõud



Võiksite arvata, et Bitcoin core arendajatel on otsene kontroll Bitcoin üle, kuid see ei ole nii. Nad ei saa protokolli muutmist peale suruda. Nende roll on teha ettepanekuid koodi kohta. Iga kasutaja peab oma sõlme kaudu otsustama, kas ta kasutab seda koodi või mitte.



See tähendab, et kui Bitcoin core muudatus ei vasta konsensusele, võivad sõlmed seda ignoreerida, jättes Bitcoin core uuendamata või lihtsalt muutes rakendamist. Seevastu kui kasutajate soovitud funktsioon on Core arendusprotsessis blokeeritud, on alati võimalik minna üle teisele rakendusele või Fork projektile.



Nagu me arutame hiljem selles kursuses, on sõlmed, vastavalt nende majanduslikule kaalule (st kaupmehed), need, kes annavad protokolli versioonile (ja seega ka vastavale valuutale) kasulikkuse, võttes vastu selle reegleid järgivaid ühikuid. Seega on Bitcoin tegelik valitsemisvõime nende kaupmeeste, mitte arendajate käes.




# Hakka suveräänseks bitcoineriks


<partId>df64cad2-e92d-4949-9cca-14394aad0bc6</partId>




## Miks oma sõlme keerata?


<chapterId>39c0cd19-67f9-4c64-bfb3-dbd6eec0bf42</chapterId>



On levinud arvamus, et Bitcoin-sõlme käitamine on puhtalt altruistlik tegu, ilma isikliku kasu saamiseta, üksnes võrgu detsentraliseerimise teenistuses. Mõni peab seda bitcoin'i kasutajate üheks kohustuseks toetada süsteemi ja näidata oma tänu Bitcoin-le.



Tõepoolest, nagu me eelmistes peatükkides märkisime, ei ole sõlme ketramisest otsest rahalist kasu. Seetõttu võiks arvata, et see ei ole isiklik huvi. Ometi toob oma sõlme pidamine palju individuaalset kasu. Et teid selles veenda, esitan selles peatükis kõik põhjused, nii tehnilised kui ka strateegilised, miks te peaksite oma Bitcoin sõlme paigaldama ja kasutama.



### Tehingute konfidentsiaalsem levitamine



Kui Wallet tarkvara ühendub välise sõlmpunktiga, edastab see oma tehingud teie kontrolli alt väljas olevale infrastruktuurile. See tekitab ilmselge jälgimisriski: välissõlme operaator võib analüüsida teie tehingute üksikasju, sealhulgas summasid ja sagedusi, ning teatavate metaandmete (nt IP-aadressid, ajad ja asukohad) ristkontrollimisega potentsiaalselt seostada neid teie identiteediga.



Nagu eelmises peatükis märgitud, ei suhtle rahakotid Bitcoin võrguga maagiliselt; nad peavad sõlmpunktiga ühendust võtma, et konsulteerida saldoga või edastada tehinguid. Kui te ei ole kunagi oma sõlme sisse seadnud, tähendab see, et teie Wallet sõltub kolmanda osapoole (tavaliselt tarkvara taga oleva ettevõtte) infrastruktuurist. See kolmas isik, eriti kui tegemist on ettevõttega, võib neid andmeid jälgida, kasutada või isegi avaldada: kas ärilistel põhjustel, juriidiliste piirangute tõttu või piraatluse tulemusena.



![Image](assets/fr/059.webp)



Kasutades oma sõlme, saadate oma tehingud otse võrku, vältides vahendajaid. Eeldusel, et te kindlustate oma sõlme korralikult (mida arutame hiljem) või järgite teatavaid standardeid, ei avaldata mingit teavet: ei teie IP Address ega teie tehingute üksikasjad ei liigu läbi üksuse, mida te ei kontrolli. See on teie konfidentsiaalsuse säilitamise põhieeldus Bitcoin.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Tsenseerimata tehingud



Samadel eespool nimetatud põhjustel on Wallet tarkvara, mis põhineb kolmanda osapoole sõlmpunktil, haavatav tsensuuriohu suhtes: kaugsõlme operaator võib erinevatel põhjustel keelduda teatud tehingute edastamisest. Ta võib neid pidada kahtlaseks või oma poliitikaga vastuolus olevaks. Tehing võidakse ka blokeerida, kui see ei vasta sõlme edastamise eeskirjadele. Lõpuks võib operaator konkreetselt teie IP Address sihtmärgiks võtta, et blokeerida teie tehingute edastamine.



Seevastu, kasutades oma sõlme, tagate oma tehingute leviku võrdõigusvõrgus. See tähendab, et teil säilib täielik kontroll oma tehingute levitamise üle, kuna te ei sõltu vahendajast. Kui tehing vastab teiega ühendatud sõlmede konsensuse ja edastamise reeglitele, edastatakse see võrgus ja seejärel, kui see sisaldab piisavalt tasusid, integreeritakse see Miner abil plokki. Oma sõlme olemasolu tagab neutraalse, lubadusteta kinnituse teie tehingutele.



### Sõltumatu andmete kontrollimine



Ilma isikliku sõlmpunktita jääte sõltuvaks kolmandast isikust, kes annab teile juurdepääsu teabele, näiteks teie Address saldole, tehingu kinnituse staatusele ja blokeeringu kehtivusele. See eeldab kaudset usaldust välise sõlme täpsuse ja terviklikkuse suhtes.



![Image](assets/fr/060.webp)



Full node kasutamine tähendab, et saate ise kontrollida kõiki protokollireegleid iga tehingu ja iga ploki puhul. Selle tulemusena ei ole teie Wallet poolt kuvatud saldo mitte kaugserverist saadud andmed, vaid tulemus, mis on arvutatud kohapeal Blockchain täieliku koopia põhjal, mis on plokkide kaupa valideeritud. Selline lähenemine annab bitcoin'ile täieliku tähenduse:



> Ärge usaldage, kontrollige.

### Süsteemi turvalisuse parem jaotamine



Iga võrguga ühinev sõlm tugevdab Bitcoin redundantsust ja vastupidavust. See hõlbustab teabe levitamist ja võimaldab uutel eakaaslastel üksteisega ühendust võtta. Ilma sõlmedeta oleks süsteem lihtsalt kasutuskõlbmatu.



Nagu me nägime, ei põhine Bitcoin turvalisus detsentraliseerimisel, Mining või krüptograafial: nagu iga süsteemi puhul, tugineb see üksikisikutele. Täpsemalt öeldes sõltub see sõlmede operaatorite võimest vastu seista sundimisele.



Selliseid detsentraliseeritud süsteeme nagu Bitcoin eristab riski jagunemine kõigi nende toimimises osalevate isikute vahel. Oma Bitcoin-sõlme käitamine tähendab, et võtate osa sellest riskist, tagades oma instantsi turvalisuse; sellega kergendate ka teiste sõlmede operaatorite riskikoormust.



Seega ei ole tegemist otsese isikliku kasuga: sõlme käitamine paneb teid osaliselt vastutama võrgu turvalisuse eest. Ennekõike on see kollektiivne kasu, sest teie osalemine aitab riski hajutada. Te omakorda suurendate enda võimet Bitcoin usaldusväärselt kasutada.



### Süvendada oma arusaamist süsteemist



Full node paigaldamine ei ole triviaalne toiming. See hõlmab tarkvara paigaldamist, põhitegevuse mõistmist, sünkroniseerimise jälgimist, probleemide korral logide uurimist ja isegi terminali kasutamist. See viib teid tingimata süvendatult protokolli mõistmiseni. See on kaudne, kuid mitte ebaoluline eelis.



Nende teadmiste omandamine tugevdab teie usaldust tööriista vastu ja võib vähendada vigade või pettuste ohtu. Oma sõlme keeramine on samuti üks õppimise vorm.



### Valides, milliseid eeskirju kohaldada



Oluline aspekt, mida sageli valesti mõistetakse, on see, et sõlme käitamine võimaldab teil valida, milliseid reegleid te kohalikult rakendate. Reegleid on kahte peamist tüüpi:





- Konsensusreeglid**:



Need on Bitcoin protokolli põhireeglid, mis tagavad süsteemi terviklikkuse ja kehtestavad kriteeriumid tehingute ja plokkide valideerimiseks. Mis tahes tehingut, mis ei vasta nendele konsensuseeskirjadele, ei saa kunagi lisada kehtivasse plokki. Näiteks jäetakse süstemaatiliselt välja tehing, mille ühel kirjel on kehtetu allkiri.



Nende reeglite muutmine on samaväärne protokolli ja seega ka valuuta muutmisega (Hard Fork). Kuid isegi kui neid muuta ei üritata, annab ainuüksi olemasolevate reeglite range kohaldamine teatava võimu: kui plokk rikub reegleid, lükkab sõlmpunkt selle kohe tagasi.





- Releereeglid**:



Need on igale Bitcoin sõlmpunktile omased reeglid, mis lisatakse konsensusreeglitele, et määratleda Mempools aktsepteeritud ja kolleegidele edastatud kinnitamata tehingute struktuur. Iga sõlmpunkt konfigureerib ja kohaldab neid reegleid lokaalselt, mis selgitab, miks need võivad olla eri sõlmedes erinevad. Neid kohaldatakse ainult kinnitamata tehingute suhtes: sõlme poolt "mittestandardseks" peetav tehing võetakse vastu ainult siis, kui see on juba kehtivas plokis. Nende reeglite muutmine ei välista sõlme Bitcoin süsteemist.



Näiteks tehing, mille puhul ei ole tasusid, on konsensuseeskirjade kohaselt täiesti kehtiv, kuid see lükatakse vaikimisi tagasi vastavalt Bitcoin core releepoliitikale, sest parameeter `minRelayTxFee` on määratud `0.00001` (BTC/kB). Siiski on võimalik oma sõlmes seda piirmäära alandada, et edastada madalama tasuga tehinguid, või vastupidi, suurendada piirmäära näiteks 2 Sats/vB-ni, et vältida madala tasuga tehingute edastamist.



Oma sõlme keerutamine tähendab kinnitamist: "Ma kinnitan seda, mida ma valin kinnitada, vastavalt reeglitele, mille ma ise olen vastu võtnud "*. Seega muutute süsteemi juhtimises osalejaks, kes suudab tagasi lükata evolutsiooni, mis tundub teile vastuvõetamatu, või heaks kiita uuenduse vastavalt oma kriteeriumidele.



Nii et me võime kiiresti proovida mõista, kui palju võimu teil on tänu teie sõlmpunktile reeglite üle. Ja selle võimu ulatus sõltub reegli tüübist.



#### Relee-eeskirjade puhul



Mis puutub relee-eeskirjadesse, siis oluline on lihtsalt sõlme omamine, sõltumata selle majandustegevusest. Küsimus on selles, kas olete nõus teatud tüüpi tehingute edastamisega või mitte.



Kui te näiteks usute, et tehinguid, mille tasud on alla 1 sat/vB, tuleks Bitcoin-s aktsepteerida, saate oma sõlme seda reeglit kohandada nii, et see edastab need tehingud, hõlbustades seega nende levikut võrgus, kuni Miner lisab need lõpuks kehtivasse plokki. Sisuliselt on seega tegemist võimuga tehingute levitamise üle: igal sõlmel on otsustusõigus, sest nõusolek mingi tehingu tüübi edastamiseks on samaväärne selle heakskiitmise edendamisega Bitcoin võrgus. Selle tulemusena on teil mitme sõlme käitamisel suurem mõju releepoliitikale, kuna igal sõlmel on oma ühendused ja mõjualad võrgus.



Ühe või mitme sõlme puhul, mis on konfigureeritud konkreetsete edastamisreeglitega, on tõepoolest vaja kindlaks määrata, milline osa võrgust võtab vastu teatavat liiki tehingu edastamise. Sõnumite levitamine võrdõiguslikus graafis, nagu Bitcoin tehingute puhul, järgib perkolatsiooniteooria loogikat. Kujutlege iga sõlme kui saiti, mis võib olla aktiivne (`p` = ta edastab) või mitteaktiivne (`1-p`). Niipea, kui osakaal `p` ületab kriitilise lävendi (`p_c`), tekib hiiglaslik komponent: tehing suudab võrgu läbida ja tal on kõik võimalused jõuda Miner-ni. Bitcoin-taolises võrgus, kus iga sõlmpunkt säilitab keskmiselt 8 väljaminevat ühendust, on `p_c` künniseks tavaliselt vaid mõni protsent, isegi madalam, kui mõnel sõlmpunktil on väga palju ühendusi.



![Image](assets/fr/061.webp)



Niikaua kui "p" jääb alla "p_c", piirdub tehing isoleeritud taskutega ja ei jõua Miner-ni. Niipea kui see lävi ületatakse, levib see peaaegu koheselt kogu võrku.



Lõppkokkuvõttes otsustavad alati kaevandajad, kas tehing lisatakse plokki või mitte. Siiski sekkuvad sõlmed ülespoole, mõjutades tehingute jaotust: nad määravad, kas kaevurid saavad teada konkreetsest tehingust või mitte. Kui tehingut ei edastata kaevuritele, on neil ilmselgelt võimatu seda plokki lisada.



Mõne täiendava sõlme lisamine mõjutab seega ainult marginaalselt, kui võrk on juba teatud tüüpi tehingu jaoks perkolatsioonifaasis, kuid see võib osutuda otsustavaks, kui perkolatsioonikünnis läheneb. Mitme sõlme omamine või mõjutamine, eriti kui need on hästi ühendatud, võib suurendada või vähendada "p" väärtust ja seega kaudselt suunata releereegleid, mis määravad, milliseid tehinguid kaevandajad näevad ja lõpuks aktsepteerivad.



#### Konsensusreeglite puhul



Mis puutub teie sõlme mõjusse konsensuseeskirjadele, siis on määravaks eelkõige selle majanduslik kaal. See on oluline mõiste: iga valuuta väärtus on otseselt seotud selle võimega hõlbustada Exchange. Tõepoolest, kui objekti ei aktsepteeri keegi Exchange-s kaupade või teenuste eest, ei ole tal teoreetiliselt mingit rahalist kasu. Näiteks kui ükski kaupmees ei aktsepteeri kivikesi maksevahendina, siis ei ole neil kasu rahana. Loomulikult jääb kasulikkus individuaalsel skaalal subjektiivseks mõisteks, kuid mida rohkem kaupmehi Exchange mingi objekti maksevahendina aktsepteerib, seda tõenäolisemalt on sellel objektil selle territooriumil elavate inimeste jaoks rahaline kasulikkus.



Võtame näiteks küla, kus paljud kaupmehed võtavad kaupade eest vastu kulda Exchange-s: tõenäoliselt on kuld külaelanike jaoks rahaliselt kasulik. See näitab, et raha kasulikkus sõltub otseselt kaupmeeste otsusest seda vastu võtta või tagasi lükata.



See kontseptsioon on oluline Bitcoin süsteemis toimuva võimudünaamika mõistmiseks. Satoshi teeb selle selgeks: Bitcoin on elektrooniline rahasüsteem; teisisõnu, see pakub teenust, mis pakub üht liiki valuutat, Bitcoin (või BTC). Kui protokollireegleid muudetakse viisil, mis ei ole tagasiulatuvalt ühilduv (Hard Fork), tähendab see uue süsteemi ja seega uue valuuta loomist. Selle Fork edu või läbikukkumine sõltub siis selle majanduse suurusest, mis omakorda sõltub seda uut vääringuvormi aktsepteerivate kaupmeeste arvust.



![Image](assets/fr/062.webp)



Võtame näite: oletame, et Bitcoin kannatab Hard Fork. Sellisel juhul oleks 2 erinevat valuutavormi: BTC-1 (algne, muutmata versioon) ja BTC-2 (uus valuuta, mille konsensusreeglid on erinevad). Kui kõik kaupmehed, kes aktsepteerisid BTC-1, jätkavad seda, kuid keelduvad BTC-2-st, siis on viimasel teoreetiliselt väga piiratud rahaline kasu. Kasutajana ei oleks mul huvi BTC-2 hoida ja kasutada, teades, et ükski kaupmees ei taha seda Exchange kaupade või teenuste eest. Seevastu kui 50% kaupmeestest otsustab aktsepteerida ainult BTC-2 ja ülejäänud 50% võtab ainult BTC-1, siis on BTC-1 kasulikkus teoreetiliselt vähenenud poole võrra. Kasutan terminit "teoreetiliselt", sest kasulikkus jääb individuaalsel tasandil subjektiivseks ja sõltub paljudest teguritest (nagu territoorium ja tarbimisharjumused), mida on raske iga juhtumi puhul eraldi mõista.



Bitcoin puhul hõlmab "kaupmehe" roll, mida mõistetakse kui mis tahes üksust, millel on teatav majanduslik kaal, loomulikult ettevõtteid (füüsilised kauplused, veebimüügileheküljed, teenusepakkujad jne), kuid ka Exchange platvormid, kuna nad aktsepteerivad Bitcoin Exchange-s teiste valuutade eest, ja kaevandajad, kuna nad võtavad Bitcoin tasu kaudu vastu Exchange-s tehingu plokki lisamise teenuse eest.



Mis puutub konsensusreeglitesse, siis võimaldab teie sõlmpunkt teil suunata oma majandustegevust ühe või teise valuuta suunas. Näiteks kui teil on kodus 10 täis sõlme, kuid puudub märkimisväärne majandustegevus, on teie mõju Fork ajal peaaegu olematu. Seevastu üks ainus sõlmpunkt, mida kasutatakse 200 kaupluse keti haldamiseks, mis võtab vastu Bitcoin, annab märkimisväärse majandusliku kaalu.



Seega ei ole oluline mitte sõlmede arv, vaid nende poolt toetatava majandustegevuse tähtsus. Veelgi enam, kui teie majandustegevus sõltub sõlmest, mida te ei kontrolli, otsustab selle omanik, millist valuutat te kasutate, kuni olete selle sõlmega seotud. Seepärast on oma sõlme juhtimine ja kasutamine süsteemi juhtimise kontekstis eriti oluline:



> Mitte sinu sõlme, mitte sinu reegleid.


## Bitcoin sõlmede eri tüübid


<chapterId>be8f0baa-41f2-4b54-b011-092f4ccc93aa</chapterId>



Bitcoin-sõlm on seega masin, mis töötab Bitcoin protokolli rakendusega. Selle ühise sõlmede määratluse taga on mitu võimalikku konfiguratsiooni, mis kõik ei paku samasugust autonoomiat, ressursikulu ja kasulikkust võrgu jaoks. Selles peatükis püüame neid erinevusi mõista, et aidata teil valida sõlmearhitektuuri, mis sobib teie kasutusalale ja riistvaralistele piirangutele.



### Täielik sõlm



Full node on lihtsalt Bitcoin sõlme, mis laeb alla kogu Blockchain Genesis plokist, valideerib iga ploki iseseisvalt ja salvestab kogu selle Blockchain ajaloo lokaalselt. See on Bitcoin sõlme "tavaline" vorm, nagu Satoshi Nakamoto seda ette kujutas.



![Image](assets/fr/063.webp)



Full node ei pea kedagi usaldama, sest ta valideerib ja teab kogu süsteemis olevat teavet. See on sõlme tüüp, mis annab teile kõige rohkem garantiisid: te teate, ilma et peaksite toetuma kolmandale isikule, kas makse on kehtiv, kas plokk on kehtiv, kas reorganiseerimine on õiguspärane ja nii edasi.



Praktikas nõuab Full node mittetriviaalseid ressursse, sealhulgas mitusada gigabaiti plokkfailide jaoks, protsessorit, mis suudab skriptid valideerida, RAM-i Mempool ja vahemälu jaoks ning stabiilset ribalaiust. Esimene sünkroniseerimine (*IBD*) loeb ja kontrollib kogu ajalugu: see on intensiivne, kuid toimub ainult üks kord. Full node osaleb aktiivselt võrgus, edastades plokke ja tehinguid ning võib vastu võtta sissetulevaid ühendusi, et aidata teisi eakaaslasi.



Sõltuvalt teie vajadustest võite lisada oma Full node-le indekseerija. Bitcoin core pakub valikulise funktsioonina tehingu indekseerimist (vaikimisi välja lülitatud), mis võib olla kasulik teatud eesmärkidel. See ei sisalda aga Address indekseerijat, mis on sageli üksikkasutajate jaoks kõige nõutavam funktsioon. Selle parandamiseks saate oma sõlme paigaldada spetsiaalset tarkvara, näiteks Electrs või Fulcrum, et kiirendada Address saldode kontrollimiseks tehtavaid päringuid seotud UTXOdest. Indekseerija rolli juurde tuleme üksikasjalikumalt tagasi eraldi peatükis.



### pruned sõlme



pruned sõlme valideerib kõik Full node, alates Genesis plokist kuni ahela pähe, kus on kõige rohkem tööd, kuid **säilitab ainult plokifailide kõige uuema osa**. Kui vanad plokid on kontrollitud, kustutab ta need järk-järgult, et jääda alla seadistatava ruumipiirangu. See konfiguratsioon on ideaalne, kui teil on kettaruumi piirangud: te säilitate sõltumatuse plokkide valideerimisest, salvestamata kogu Blockchain ajalooarhiivi. See valik on eriti kasulik, kui soovite Bitcoin core lihtsalt oma personaalarvutisse paigaldada, ilma et kasutaksite selleks spetsiaalset masinat.



![Image](assets/fr/064.webp)



Selle võimaluse tehnilised tagajärjed on üsna lihtsad: pruned sõlme on täiesti võimeline edastama teie tehinguid, osalema relees, kontrollima plokke ja tehinguid ning jälgima ahelat. Teisest küljest ei saa see olla ajalooliste andmete allikaks, mis ületab oma piirid teiste rakenduste jaoks (nt täielikud uurijad, indekseerijad, rahakotid). Funktsioonid, mis nõuavad arhiivi (või globaalset indeksit), ei ole seega kättesaadavad.



Praktiliselt saab pruned sõlme kasutada Wallet juhtimistarkvara, näiteks Sparrow wallet, ühendamiseks. Siiski ei saa te oma Wallet-l skaneerida tehinguid, mis on enne kärpimise piirangut. Näiteks kui teil on registreeritud tehing plokis 901 458, kuid teie sõlmpunkt säilitab ainult plokke alates 905 402 (sest vanimad on olnud pruned), ei saa te seda tehingut skaneerida. Teisalt, kui te juba skaneerisite seda, kui teie sõlmes oli veel see plokkide kõrgus, siis teie Wallet haldustarkvara salvestab selle teabe ja kuvab vastavate UTXOde saldot õigesti.



Lühidalt öeldes töötab Wallet jälgimine pruned-sõlmes tõrgeteta, kui te loote uue Wallet, kui teie tarkvara on juba selle sõlme külge ühendatud. Teisest küljest võib tekkida raskusi, kui taastate vana Wallet, sest varasemad tehingud, mida sõlme enam ei säilitata, ei ole ilmselgelt enam leitavad.



### Kerge sõlm / SPV



SPV-sõlm (*Simplified Payment Verification*) ehk lihtsustatud maksesõlm säilitab ainult plokkide päiseid, mitte tehingu üksikasju, ja tugineb teistele täissõlmedele, et saada tõendeid, et tehing on plokis (Merkle-tõendid puude kaudu), mille päis on tal olemas. Lihtsustatud makse tõendamise kontseptsioon ei ole uus, selle pakkus välja Satoshi Nakamoto ise valge raamatu 8. osas.



![Image](assets/fr/066.webp)



Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. https://Bitcoin.org/Bitcoin.pdf



Seda tüüpi sõlmed on salvestusruumi ja protsessorikasutuse poolest ilmselgelt palju kergemad kui Full node või isegi pruned sõlmed. Seetõttu sobib SPV-sõlm hästi väiksemate seadmete ja katkendlike ühenduste jaoks. Tegelikult on see sageli integreeritud otse Wallet-sõlme, eriti mobiilse tarkvara, nagu näiteks Blockstream App.



Kompromissiks on usaldus ja konfidentsiaalsus: SPV-klient ei kontrolli ise skripte ega valideerimispõhimõtteid; ta eeldab, et kõige rohkem tööd teinud ahel on kehtiv, ja sõltub vastuste saamiseks ühest või mitmest täissõlmest. Seda tüüpi sõlme kasutamine on seega parem variant kui ühendus kolmanda osapoole sõlmega; see on siiski vähem kasulik kui Full node või isegi pruned sõlme kasutamine.



![Image](assets/fr/065.webp)



### Milline sõlmpunkt millise vajaduse jaoks?





- Mobiilne / algaja kasutaja



Algajale kasutajale, kellel on vaid Wallet mobiilirakendusega, on SPV-sõlme kasutamine kindlasti parim viis alustada. Paigaldamine on kiire, nõuab vähe ressursse ning kogemus on lihtne ja sujuv. See tähendab, et saate teatud teavet ise kontrollida ja seega vähem sõltuda kolmandate osapoolte sõlmedest, olles samal ajal tehingute edastamisel sõltumatum.





- PC / vahekasutaja



Keskmise kasutaja, kellel on arvuti, võib paigaldada pruned sõlme, et saada kasu peaaegu kõigist Full node eelistest, ilma oma masinat igapäevaselt üle koormamata: täielik valideerimine, mõõdukas kettakasutus ja lihtne hooldus. See on ideaalne lahendus, et ühendada oma töölaua rahakotid ja jääda oma tehingute jaotamisel sõltumatuks, investeerimata spetsiaalsesse masinasse või koormamata oma kettaruumi üle.





- Suveräänne Bitcoiner / arenenud



Full node jääb parimaks lahenduseks, kui soovite Bitcoin kasutamisel olla täiesti sõltumatu ja mitte piirata end hiljem edasijõudnud kasutusaladega, nagu indekseerija, Lightning-sõlm või isegi Block explorer. Just seda me kavatseme sellel kursusel uurida!



## Ülevaade tarkvaralahendustest


<chapterId>0d48b89a-e8b5-441e-a707-537a035fc15e</chapterId>



Tarkvara poolel on Bitcoin sõlme käivitamiseks 2 peamist võimalust:




- paigaldada otse protokolli rakendus, näiteks Bitcoin core (soovitatav) või Bitcoin Knots,
- või kasutada valmis distributsiooni (sageli nimetatakse seda "sõlme-komplektis"), mis integreerib Bitcoin rakendamise samamoodi, kuid sisaldab ka Interface haldussüsteemi, rakenduste kauplust ja valmis tööriistu (Lightning, brauserid, indeksiserverid, isegi Bitcoin välised isehostitavad rakendused...).



Mõlemad lähenemisviisid viivad sama eesmärgini: omada oma sõlme, kuid nad erinevad Interface paigaldamise ja kasutamise, hoolduse, laiendatavuse ja maksumuse poolest. Seda uurime selles peatükis.



### Toores Bitcoin sõlme rakendused



Toore implementatsiooni paigaldamine tähendab, et kasutatakse otse Bitcoin protokolli implementatsiooni tarkvara (näiteks Core), ilma lisatarkvara Layer kasutamata. Te ise haldate konfiguratsiooni, uuendusi ja seotud teenuseid (indekseerimine, API, Lightning, varukoopiad jne) vastavalt oma vajadustele.



See on kõige suveräänsem ja paindlikum lähenemisviis: te teate täpselt, mis töötab, kus andmed asuvad ja kuidas kõik toimib. Teisest küljest muutub see keerulisemaks, niipea kui soovite minna Bitcoin sõlme lihtsast toimimisest kaugemale. Kui teie eesmärk on lihtsalt sõlm, on keerukus võrreldav node-in-a-box'i omaga või isegi vähem, sest tegemist on lihtsalt tarkvara paigaldamisega.



#### Bitcoin core (ülimalt suurklient)



[Bitcoin core on võrgu ülimalt suurklient](https://bitcoincore.org/). See laeb alla, valideerib ja hooldab Blockchain, pakub RPC/REST APIsid ja võib integreerida Wallet. Kui te eelistate standardseid vahendeid ja tunnete end mugavalt, kui lisate ise teenuseid (näiteks Electrumi server, explorer ja LND), siis on parem kasutada Core'i sellisena, nagu ta on.



**Eelised:** Maksimaalne stabiilsus, prognoositav käitumine, toores kogemus, lihtne paigaldada ja konfigureerida.



**Häired:** Te peate käsitsi ehitama ülejäänud virna, et luua täielik rakenduskeskkond, mitte ainult Bitcoin sõlme.



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

#### Bitcoin Knots (peamine alternatiivne klient)



[Bitcoin Knots on Bitcoin core Fork](https://bitcoinknots.org/), mida hooldab Luke Dashjr. See on peamine alternatiivne klient Core'ile Bitcoin protokolli rakendamiseks. Täielikult ühildub ülejäänud võrguga (see ei ole mingil juhul Hard Fork nagu Bitcoin Cash), kuid pakub siiski lisafunktsioone, sealhulgas releepoliitika võimalusi, mis Core'is puuduvad või mida rakendatakse vaikimisi rangemalt, et piirata seda, mida mõned peavad rämpspostiks.



On 2 võimalikku põhjust, miks valida Knotid Core'i asemel:




- Tehnikad**: Erinevad võimalused Core'ist, eelkõige relee haldamise osas, määrates, milliseid tehinguid teie sõlme poolt aktsepteeritakse ja edastatakse.
- Poliitika**: Mõned inimesed eelistavad kasutada alternatiivseid kliente, nagu Knots, mittetehnilistel põhjustel, eelkõige selleks, et toetada alternatiivi Core'ile ja seega vähendada selle monopoli. Kui Core peaks kunagi ohtu sattuma, oleks kasulik mitte ainult omada kindlaid, hästi hooldatud alternatiivseid kliente, vaid ka teada, kuidas neid tõhusalt kasutada. Teised kasutavad Knots'i protestiks, sest nad on kaotanud usalduse Core'i arendajate vastu või ei kiida heaks enamikku kliendi juhtimist.


https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Isiklikult soovitan valida Core, peamiselt selleks, et saada kiiremini kasu turvaparandustest. Tõepoolest, mõned Knotsis avastatud haavatavused parandatakse hilinemisega. Üldisemalt on Core'i arendusprotsess kindlalt struktureeritud ja seda toetab suur hulk toetajaid, samas kui Knots'i hooldab üks inimene ja selle kogukond on palju väiksem. Teisest küljest kipuvad releereeglid tänapäeval oma kasulikkust kaotama, eriti kui neid rakendab vaid väike osa võrgustikust (nagu perkolatsiooniteooria).



### Node-in-a-box jaotused



_node-in-a-box_ ühendab Bitcoin core (või Knots) eelkonfigureeritud operatsioonisüsteemi, Interface Webi ja isehostivate teenuste (Lightning, explorers, Electrumi server, Mempool, BTCPay Server, Nextcloud jne) rakenduste poe. Ühe klõpsuga saate neid erinevaid mooduleid paigaldada, uuendada ja omavahel ühendada.



See on palju lihtsam lahendus arvukate lisarakenduste käivitamiseks ja igapäevaseks haldamiseks. Miinuseks on see, et probleemi ilmnemisel (nt Docker image'i konflikt, vigane värskendus, vigane andmebaas) võib veaotsing muutuda väga keeruliseks, kuna sõltute distributsiooni enda integratsioonist. Veelgi enam, kogukonna või ametlik tugi on sageli keeruline.



Niisiis, node-in-a-boxi on äärmiselt lihtne kasutada seni, kuni kõik töötab korralikult, kuid vea korral peate olema valmis tegema pikki otsinguid, ootama abi ja määrima oma käed.



Enamik neist lahendustest on saadaval kahes formaadis:




- Eelnevalt kokku pandud masin: täielik arvuti, millele on juba installeeritud operatsioonisüsteem. Need tasulised masinad tuleb lihtsalt ühendada vooluvõrku ja internetti, et nad oleksid töökorras. Kui teie eelarve seda võimaldab, on selle variandi eeliseks see, et seda on väga lihtne seadistada, sageli pakutakse eelisjärjekorras tuge ja see aitab kaasa arengu rahastamisele, sest nende ettevõtete ärimudel põhineb üldiselt riistvara müügil.
- DIY: paigalda distributsioon OS oma masinale (vana PC, NUC, Raspberry Pi, koduserver...). See on kõige ökonoomsem lahendus, kuna saate vana masina taaskasutada või valida riistvara, mis vastab täpselt teie vajadustele ja eelarvele. Samuti on see kõige paindlikum variant ja kõige rahuldavam konfigureerida. Just seda lähenemist uurime kursuse praktilises osas.



Siin on ülevaade peamistest saadaolevatest node-in-a-box lahendustest (aastal 2025):



### Umbrel (UmbrelOS & Umbrel Home)



[Tänapäeval on Umbrel juhtiv node-in-a-box lahenduste tootja (https://umbrel.com/). Selle edu on suuresti tingitud selle lihtsast paigaldamisest (kui see käivitati lihtsal Raspberry Pi'l), selle elegantsest ja intuitiivsest Interface-st ning rakenduste ökosüsteemist, mis on kiiresti kasvanud ja nüüdseks väga ulatuslik.



![Image](assets/fr/067.webp)



Umbrel käivitati 2020. aastal lihtsa Bitcoin sõlmpunktina koos mõne abirakendusega, kuid sellest on järk-järgult kujunenud täisfunktsionaalne kaasaegne kodupilv.



Ma ei hakka siinkohal täpsemalt rääkima selle toimimisest ja selle eripärast, sest me uurime neid põhjalikumalt järgmise osa esimeses peatükis. Selle BTC 202 kursuse jaoks olen tõepoolest otsustanud kasutada UmbrelOSi, mis on minu arvates parim praegune node-in-a-box lahendus algajatele ja edasijõudnutele.



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

### Start9 (StartOS)



[Start9 pakub StartOS (https://start9.com/), süsteemi, mis on mõeldud "suveräänseks arvutikasutuseks": eesmärk on, et igaüks saaks omada ja hallata oma privaatserverit, mida täiendab isehostetavate rakenduste turg. Saate osta Start9 serveri (Server One hinnaga 619 dollarit, Server Pure hinnaga 899 dollarit) või koostada omaenda DIY-režiimil oma masina.



Bitcoin poolel võimaldab StartOS paigaldada Full node, Lightning-sõlme, BTCPay-serveri, Electrs ja palju muid teenuseid. Start9 atraktiivsus ulatub aga sellest kaugemale: see pakub võimalust avastada, konfigureerida ja eksponeerida erinevaid tarkvarasid (failipilv, sõnumivahetus, seire) ühtselt ja täieliku kontrolliga. Projekt on seega suunatud kasutajatele, kes soovivad töökindlat isehostinguplatvormi, mitte lihtsalt Bitcoin sõlme. See on tõenäoliselt kõige täielikum ökosüsteem pärast Umbrelit.



![Image](assets/fr/068.webp)



Peamine erinevus Umbreliga on Interface. Umbrel tugineb väga lihvitud kasutajaliidesele, samas kui Start9 pakub jämedamat, funktsionaalsemat Interface. Start9 rakenduste ökosüsteem on vähem rikkalik kui Umbrelil, kuid see kompenseerib seda mitme tehnilise eelisega: juurdepääs täiustatud rakendussätetele on lihtsustatud, samas kui Umbrel muutub kiiresti piiravaks, kui soovitud võimalust Interface ei paku. Start9 paistab silma ka varunduste haldamisel: peale Umbreli tõhusa lahenduse LND jaoks puudub ühtne mehhanism, erinevalt Start9-st. Veelgi enam, see pakub kättesaadavamaid seiretööriistu ja krüpteeritud kaugühendust (`https`), samas kui Umbrelile on kohalik juurdepääs `http` kaudu.



Ühesõnaga, kui teil on vaja lihtsalt olulisi rakendusi Bitcoin jaoks, ilma erilise huvita Umbreli väga rikkaliku ökosüsteemi vastu, ja Interface kasutaja ei ole prioriteet, siis on Start9 parem valik. Vastasel juhul on Umbrel parem valik.



https://planb.network/tutorials/node/bitcoin/start9-8c8b6827-8423-4929-bcba-89057670ed6a

### MyNode



[MyNode on ainult Bitcoin ja Lightning'ile keskendunud distributsioon](https://mynodebtc.com/), mis pakub veebi Interface, rakenduste turuplatsi ja ühe klõpsuga uuendusi. Saate kas osta kasutusvalmis riistvara (*Mudel Kaks* saadaval hinnaga 549 dollarit) või paigaldada MyNode'i tasuta oma masinale. Projekt pakub ka tarkvara *Premium* versiooni ($94), mis sisaldab prioriteetset tuge ja täiustatud funktsioone.



![Image](assets/fr/069.webp)



Praktikas koondab MyNode kõik Full node käitamiseks vajalikud põhielemendid ning Bitcoin kasutajate jaoks olulised rakendused. Seetõttu on see sobiv lahendus, kui te ei vaja Bitcoin ökosüsteemi väliseid rakendusi, nagu näiteks Start9 ja Umbreli süsteemides leiduvad isehostitavad rakendused.



https://planb.network/tutorials/node/bitcoin/mynode-a481fef3-2fd3-4df3-91c0-112cffa094eb

### RaspiBlitz



[RaspiBlitz on 100% avatud lähtekoodiga projekt](https://docs.raspiblitz.org/) (MIT litsents) Bitcoin sõlme ja Lightning sõlme paigaldamiseks Raspberry Pi'le. Lihtsalt laadige pilt alla, käivitage see ja järgige nõustaja juhiseid, et saada oma Raspberry Pi-le töötav node-in-a-box. Eelnevalt kokkupandud komplektid on saadaval ka kolmandatelt osapooltelt, tavaliselt vahemikus 300-400 dollarit, sõltuvalt riistvarast. RaspiBlitz pakub ka mitmeid täiendavaid, lihtsalt paigaldatavaid rakendusi.



![Image](assets/fr/070.webp)



Kui teil on Raspberry Pi, on see suurepärane võimalus, sest terviklikumad süsteemid nagu Umbrel muutuvad üha raskemaks seda tüüpi mini-PC jaoks.



https://planb.network/tutorials/node/bitcoin/raspiblitz-d8cdba2e-a682-46cf-9fdc-d8602fbeac02

### RoninDojo



[RoninDojo on privaatsusele keskendunud node-in-a-box](https://wiki.ronindojo.io/en/home), mis automatiseerib Samurai Dojo ja Whirlpool kasutuselevõttu, kasutades spetsiaalset Interface ja spetsiaalselt Samurai ökosüsteemi jaoks loodud pistikprogramme.



Põhimõte on lihtne: kui kasutate Ashigaru Wallet (Samurai Wallet järeltulija Fork, pärast selle arendajate arreteerimist) või kui soovite kasutada täiustatud privaatsustööriistu, on RoninDojo teie jaoks.



![Image](assets/fr/071.webp)



Varem pakuti projekti raames eelkonfigureeritud masinat nimega Tanto, kuid see on praegu kättesaamatu. See võib hiljem tagasi tulla. Vahepeal on võimalik RoninDojo hõlpsasti paigaldada Rock5B+ või Rockpro64 või isegi kaudselt Raspberry Pi peale.



https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

### Nodl



Teine [node-in-a-box lahendus on Nodl](https://www.nodl.eu/). Nagu eelmiste projektide puhul, võite kas osta eelkonfigureeritud riistvara (sõltuvalt mudelist 599-799 eurot) või paigaldada selle ise DIY-režiimis.



Tarkvara poolel integreerib Nodl Bitcoin core, LND, BTCPay Server, Electrs, Dojo, Whirlpool, Lightning Terminal, RTL, samuti BTC RPC Explorer, kõik koos integreeritud uuenduste ahelaga ja avatud lähtekoodiga MIT litsentsi alusel.



![Image](assets/fr/072.webp)



Olles uurinud erinevaid tarkvaralahendusi, on nüüd aeg valida masin, mis hakkab teie sõlme võõrustama!




## Ülevaade riistvaralahendustest


<chapterId>245d6add-9cda-46b9-9343-31dcdd70456e</chapterId>



Nüüd, kui me oleme uurinud kõiki tarkvaralisi võimalusi, keskendume teie sõlme jaoks vajalikule riistvarale. Ma annan teile konkreetseid nõuandeid komponentide valimiseks koos eri eelarvele kohandatud konfiguratsioonidega. Loomulikult on see minu isiklik arvamus ja tagasiside: lisaks siin esitatule on kindlasti ka teisi asjakohaseid alternatiive. Lisaks ei hakka ma uuesti käsitlema node-in-a-box projektide poolt pakutavaid eelkoostatud masinaid, mida me juba eelmises peatükis käsitlesime. Keskendume siinkohal üksnes DIY-lahendustele.



### Kas teil on tõesti vaja spetsiaalset masinat?



Viimaste aastate jooksul on bitcoin'i kasutajad üha enam teadvustanud levinud väärarusaama, eriti seoses node-in-a-box'i populariseerimisega 2020ndate alguses: Bitcoin sõlme peab tingimata jooksma ainult selleks otstarbeks mõeldud masinas. Kuid see ei ole tõsi. Bitcoin sõlme käivitamiseks ei ole tingimata vaja spetsiaalset arvutit: Bitcoin core on täiesti võimeline töötama teie igapäevases arvutis. Kui teil on piisavalt kettaruumi Blockchain jaoks või kui te lubate kärpimist, võite kinnitada ahela, ühendada oma Wallet ja isegi sulgeda programmi, kui olete selle kasutamise lõpetanud. Selle lähenemisviisi eelis on märkimisväärne: null alginvesteering ja minimaalne keerukus.



![Image](assets/fr/074.webp)



See tähendab, et spetsiaalse masina kasutamine on sageli mugavam. See võib töötada pidevalt (24/7), olla kogu aeg eemalt kättesaadav, ei monopoliseeri teie peamise masina ressursse ja eelkõige isoleerib kasutusalad (hea turvapraktika: kui teie isiklik arvutis tekib probleem, jätkab teie sõlme toimimist ja vastupidi). Seega ei ole küsimus mitte "Kas ma pean pühendama masina?", vaid pigem "Kas ma vajan sõlme, mis on pidevalt võrgus, millele on juurdepääs teistest seadmetest ja mis on võimeline arenema?" (Lightning, indekseerijad, lisarakendused...). Kui vastus on jaatav, teeb eraldi masina valimine asjad palju lihtsamaks.



### 3 omandamismeetodit: ringlussevõtt, kasutatud ja uus



#### Vana arvuti taaskasutamine



See on kõige ökonoomsem lahendus. Enamikul meist on kodus või sõprade ja pereliikmete juures Dust kogunev vana arvuti: see on ideaalne võimalus selle taas kasutusele võtta! Selle kohandamiseks Bitcoin sõlmpunktina kasutamiseks lisage lihtsalt 2TB SSD ja sõltuvalt teie vajadustest asendage või lisage RAM-ribasid, et suurendada RAM-i. Täielikult toimiva masina eest tuleb maksta 100-200 eurot.



Enne mis tahes riistvara ostmist kontrollige olemasolevate kettasahtlite arvu, ühenduse tüüpi (M.2 või SATA), RAM-i formaati (SODIMM või DIMM) ja selle põlvkonda (DDR4 jne). Samuti peaksite kasutama võimalust masinat, eriti ventilaatorit, puhastada, et tagada optimaalne jõudlus.



Olge siiski ettevaatlik, kui kasutate sülearvutit: aku võib aja jooksul muutuda probleemiks (sellest lähemalt edaspidi).



#### Taastatud või kasutatud



Turg on täis renoveeritud äriotstarbelisi miniarvuteid, nagu *Lenovo ThinkCentre Tiny*, *HP EliteDesk Mini* või *Dell OptiPlex Micro*. Need masinad on soliidsed, kompaktsed, vaiksed ja energiatõhusad. Nende hind on tunduvalt madalam kui uute masinate hind ning 6.-10. põlvkonna i5/i7 protsessoritega ja 8-16 GB RAM-iga varustatud mudeleid on lihtne leida väga atraktiivse hinnaga, mis jääb sõltuvalt konfiguratsioonist tavaliselt 70-200 euro vahele. Minu arvates on see tõenäoliselt parim valik, kui otsite oma Bitcoin sõlme jaoks spetsiaalset masinat.



![Image](assets/fr/075.webp)



Samuti on võimalik leida mõne aasta vanuseid kasutatud arvutid ja sülearvutid, mis on huvitavate konfiguratsioonide ja suurepärase hinna ja kvaliteedi suhtega.



**Märkus:** Ettevõtete masinad, nagu näiteks *ThinkCentre Tiny*, on sageli varustatud ainult *DisplayPort* (DP) pordiga ekraani jaoks, ilma HDMI-väljundita. Seega ärge unustage kaasa võtta adapterit või DP-HDMI-kaablit, kui teil on seda vaja.



#### Uute toodete ostmine



Kui teie eelarve võimaldab, võite valida ka uue masina. See on hea valik, kui soovite uuemat ja hea jõudlusega riistvara, eriti kui kavatsete kasutada Umbreli või Start9-i koos täiendavate rakendustega väljaspool Bitcoin ökosüsteemi isehostimiseks.



### Millist tüüpi masinat ma peaksin valima?



#### Mini-PC "NUC" / barebone arvutid



Minu arvates on miniarvutid parim kompromiss Bitcoin sõlme majutamiseks kodus. Nad on ruumikindlad, mahuvad hõlpsasti riiulile, tarbivad minimaalselt energiat ja võimaldavad lihtsaid riistvaramuudatusi, näiteks RAM-i lisamist või SSD-ketta vahetamist.



Mina isiklikult eelistan *Lenovo ThinkCentre Tiny*, mis on väga levinud kasutatud turul (firmaparkidest); need on eriti töökindlad ja neid on lihtne muuta. Loomulikult on ka teistelt tootjatelt palju vasteid: *Dell OptiPlex Micro*, *HP ProDesk / EliteDesk Mini / Micro*, *Intel NUC*, *Gigabyte BRIX*, *MSI Cubi*...



![Image](assets/fr/001.webp)



**Kõrgpunktid:** väike jalajälg, mõõdukas energiatarbimine, madal müra, skaleeritavus (sõltuvalt mudelist) ja usaldusväärsus.



**Puudused:** veidi kallim kui Raspberry Pi-tüüpi SBC, puudub sisseehitatud ekraan (kaugjuurdepääs või välise monitori kaudu), puudub aku (ootamatu väljalülitamine voolukatkestuse korral).



#### Spetsiaalne sülearvuti



See on suurepärane odav alternatiiv mini-PC-le: tänapäeval on võimalik leida kasutatud või isegi uusi sülearvuteid soodsate hindadega, mis on varustatud korralike protsessoritega, arvukate sadamatega ning integreeritud ekraani ja klaviatuuriga (väga praktiline esmaseks paigaldamiseks). Ennekõike toimib aku kui loomulik UPS: voolukatkestuse korral ei lülitu sõlmpunkt järsku välja ja võib isegi mitu tundi töös püsida.



![Image](assets/fr/076.webp)



**Kõrgpunktid:** All-in-one lahendus, aku toimib UPS-ina (ei ole elektrikatkestusi), lihtsustatud paigaldus tänu integreeritud ekraanile ja klaviatuurile, integreeritud Wi-Fi kaart ning suur valik kasutatud ja uute turgude vahel (mis tähendab sageli, et saate pidada hinnaläbirääkimisi).



**Puudused:** veidi suurem energiatarbimine kui paljas Mini-PC, aku järkjärguline kulumine 24/7 töötamisel koos mahu vähenemisega, harva esinev, kuid reaalne oht, et aku paisub või vananedes läheb termiliselt tühjaks. Peamiselt just see aspekt paneb mind pidama mini-PC-d paremaks variandiks kui sülearvutit: aku järkjärguline kulumine ja sellega seotud riskid.



Kui valite selle lahenduse, soovitan hoida aku seisundit tähelepanelikult silmas, et vältida ohtu. Jälgige liigset kuumust, ebatavalisi lõhnu, ebastabiilsust või deformeerunud kesta. Häire korral lülitage arvuti viivitamatult välja ja tõmmake see välja ning seejärel kõrvaldage aku spetsiaalses taaskasutuskeskuses.



**Nipp:** Kui BIOS/UEFI või tootja tööriist võimaldab seda, seadke aku kestvuse pikendamiseks koormuspiirang (nt 60% või 80%).



#### Vaarika Pi ja teised SBC-d: vale idee



2020. aastate alguses, koos node-in-a-box tarkvara levikuga, tekkis ka Raspberry Pi hullumeelsus kui vahend Bitcoin sõlme käivitamiseks. Idee tundus ahvatlev: odav, kompaktne ja kättesaadav.



![Image](assets/fr/073.webp)



Praktikas, kui teie eesmärk on ainult Bitcoin sõlme käivitamine ilma lisarakendusteta, võib piisata Raspberry Pi-st. Kuid niipea, kui soovite kasutada Umbreli, Start9 või rikkalikumat ökosüsteemi (Block explorer, Address indekser, Lightning-sõlm, isehostitavad rakendused...), jõuab masin kiiresti oma piiridesse.



Raspberry Pi'l on mitmeid puudusi:




- liiga õhukesed protsessorid, mille ARM-arhitektuur on mõnikord teatud tarkvaraga ühildumatu või nõuab rohkem käitlemist;
- Joodetud RAM, mida on võimatu uuendada, piiratud konfiguratsioonidega (sageli maksimaalselt 8 GB);
- kaabliga ühendatud SSD-de välised kastid, sagedased veaallikad, mis nõuavad stabiilse SSD jaoks spetsiaalse kaardi ostmist;
- kalduvus kiiresti kuumeneda ja raskused õige jahutuse tagamisel;
- vajadus osta täiendavat riistvara (korpus, ventilaator, SSD-kaart jne);
- väga piiratud ühenduvus.



Ajalooliselt oli SBC-de, nagu Raspberry Pi, suur eelis nende hind: mõne tosina euro eest sai spetsiaalse masina. Tänapäeval on hinnad aga järsult tõusnud ja kui lisada kõik oluline lisahardvara, läheneb hind juba esimeste kasutatud või renoveeritud x86 mini-PC-de maksumusele, mis minu arvates pakuvad palju rohkem eeliseid. Sel põhjusel ei soovita ma SBC-d valida.



### Komponentide valimine



#### Kettasalvestus: SSD kohustuslik, vähemalt 2 TB



Tehniliselt on võimalik käivitada Bitcoin sõlme kõvakettal. Probleem on selles, et kõik aeglustub märkimisväärselt, eriti IBD, mis muutub äärmiselt pikaks, kuna Bitcoin core kasutab ketast intensiivselt vahemäluna (eriti UTXO komplekti puhul). Seepärast soovitan ma tungivalt mitte kasutada HDD-d: see tekitab tõelise kitsaskoha, piirab tõsiselt edasist arengut (nt Lightning-sõlme puhul) ja võib isegi põhjustada sünkroniseerimishäireid Blockchain peaga. Veelgi enam, mehaanilise ketta pidev koormus suurendab enneaegse kulumise ohtu.



SSD-kettad muudavad kasutajakogemust radikaalselt: kõik muutub kiiremaks ja sujuvamaks ning palju usaldusväärsemaks. SSD kasutamine on seega teie sõlme jaoks (peaaegu) kohustuslik ja te ei kahetse seda, eriti kuna suure mahutavusega mudelid on nüüd suhteliselt taskukohased.



![Image](assets/fr/077.webp)



Mahtuvuse osas on 2 TB järk-järgult kujunemas uueks mõistlikuks miinimumiks. Suvel 2025 läheneb Blockchain juba 700 GB-le ja kui lisada Umbrel, Address indekseerija ja mõned rakendused, saab 1 TB SSD kiiresti täis. 2 TB-ga on teil lähiaastateks (laias laastus 5-15 aastat) mugav varu. Võite valida ka 4 TB, kui plaanite Umbrelil kasutada palju rakendusi, salvestada suuri faile isehostes või kui soovite oma kettaruumi vajadust suures ulatuses ette näha.



![Image](assets/fr/078.webp)



Mis puutub formaati, siis see sõltub teie masina olemasolevatest sadamatest; kui võimalik, soovitan siiski kasutada NVMe M.2 SSD-d.



#### Mälu (RAM): 8 kuni 16 GB



Ainult Bitcoin core puhul (ilma Umbreli katteta) on arendajate soovituste kohaselt vaja vähemalt 256 MB RAM-i, kui seaded on reguleeritud madalaimale tasemele, 512 MB vaikimisi seadetega ja 1 GB tavakasutuse korral.



Teisest küljest, kui kasutate node-in-a-box süsteemi nagu Umbrel või Start9, on RAM-i nõuded oluliselt suuremad. Umbreli arendajad soovitavad vähemalt 4 GB RAM-i. Sellest võib piisata ainult Core'i käivitamiseks, kuid peagi on teil piirangud. Seetõttu soovitavad nad 8 GB, mida ka mina pean miinimumiks Bitcoin (Core, LND, indekseerija ja mõned rakendused) ümber oleva põhikonfiguratsiooni jaoks. Minu kogemuse kohaselt on 8 GB koos Umbreliga ja mõne lisateenusega siiski veidi kitsas. Selleks, et tõesti mugavalt hakkama saada ja veidi varu oleks, soovitaksin 16 GB RAM-i.



#### Protsessor (CPU)



Umbrel-sõlme puhul on minimaalne nõue kaksituumaline 64-bitine protsessor Intelilt või AMD-lt. Kui soovite lisaks Bitcoin core-le kasutada ka mõnda rakendust, on neljatuumaline (või suurem) protsessor sujuvuse seisukohalt väga oluline. Näiteks 6.-10. põlvkonna i5/i7 protsessorid on kasutatud turul suurepärased valikud.



### Konkreetsete konfiguratsioonide näited



Järgnevalt pakun välja kolm konkreetset konfiguratsiooni, mis on kohandatud erinevatele eelarvetele ja vajadustele, koos täpsete mudelitega, mis neid toetavad. Need valikud on esitatud näidetena, et illustreerida käesolevas peatükis esitatud teavet; te ei ole kohustatud valima täpselt neid mudeleid. Kuna ma pean Mini-PC-d pikemas perspektiivis parimaks valikuks, toetun kolme pakutud konfiguratsiooni puhul sellele vormile.



*Allpool esitatud hinnad on vaid soovituslikud ja võivad erineda vastavalt piirkonnale, müüjale ja ajavahemikule*



Kõigepealt on vaja SSD-ketta, mis on piisavalt suur, et mahutada Blockchain, jättes samas ruumi manööverdamiseks. SSD-kettadel on piiratud eluiga nii kirjutamistsüklite kui ka kirjutatud andmete kogumahu poolest. Bitcoin sõlme kirjutamisel paneb Bitcoin aga kettale märkimisväärse koormuse. Seepärast ei soovita ma algtaseme mudeleid, vaid soovitan hoopis NVMe SSD-d, mis pakub oluliselt paremat jõudlust.



Selle kursuse tarbeks valisin näiteks järgmise mudeli: *Samsung 990 EVO Plus NVMe M.2 SSD 2Tb*, mis on Amazonis saadaval umbes 120 euroga. Võite valida ka teisi tuntud kaubamärke, näiteks Crucial, Western Digital või Kingston.



![Image](assets/fr/046.webp)



#### Madala eelarvega konfiguratsioon



Kui teie eelarve on väga piiratud (alla 200 euro), siis soovitan teil ilmselt mitte investeerida spetsiaalsesse masinasse, vaid paigaldada Bitcoin core otse oma igapäevasesse arvutisse (pruned režiimis, kui teil pole piisavalt kettaruumi).



Muidu soovitan algtaseme eelarve puhul *HP EliteDesk 800 G2 Mini*. Leidsin Amazonist 96 euro eest renoveeritud mudeli, mis on varustatud 6. põlvkonna Intel Core i5 protsessori ja 8 GB RAM-iga. See on eriti huvitav variant algajatele: sellest protsessorist ja sellisest mälukogusest piisab enam kui küll, et käivitada Core'i Umbrelil, aga ka mitut rakendust samaaegselt, näiteks Electrs indekseerija, Lightning node ja Mempool instants, tingimusel, et te ei eralda Core'ile liiga palju vahemälu. Veelgi enam, seda tüüpi mini-PC võimaldab vajaduse korral hõlpsasti suurendada RAM-i näiteks 16 GB-ni (arvestage, et ühe või kahe kvaliteetse mälupulga eest tuleb maksta umbes 30-40 eurot lisatasu).



![Image](assets/fr/045.webp)



Seejärel lisage SSD lihtsalt eelarvesse. Alustades Samsungi 2TB-st 120 euroga, saame tervikliku ja funktsionaalse masina kogumaksumuseks 216 eurot.



#### Keskmise eelarvega konfiguratsioon



Kui teil on keskmiselt 300 euro suurune eelarve masina jaoks, mis hakkab teie sõlme majutama, siis soovitan näiteks *Lenovo ThinkCentre Tiny*, mis on varustatud suure jõudlusega protsessori ja piisava mälumäluga. Leidsin Amazonist 180 euro eest renoveeritud mudeli, millel on 6. põlvkonna Intel Core i7 protsessor ja 16 GB RAM-i. Koos 2TB SSD-ga, mille hind on 120 eurot, on kogumaksumus 300 eurot.



![Image](assets/fr/044.webp)



Selle masina puhul on teil mugav konfiguratsioon: kiire IBD ja võimalus käivitada oma Umbrelil või Start9-il arvukalt rakendusi ilma raskusteta. Just seda konfiguratsiooni kasutan ma selle BTC 202 kursuse jaoks.



#### High-end konfiguratsioon



Suurema eelarve korral muutuvad võimalused oluliselt laiemaks. Võite valida DIY-konfiguratsiooni või isegi valida eelnevalt kokkupandud masina, mida pakub otse node-in-a-box projekt.



Näiteks *ASUS NUC 14 Pro* on Amazonist saadaval uuena hinnaga 540 eurot. Selle hinna eest saad Intel Core Ultra 5 protsessori (uus ja eriti suure jõudlusega), millega kaasneb 16 GB DDR5 RAM-i. Sellise konfiguratsiooniga saad IBD rekordajaga valmis ja paigaldad raskusteta nõudlikke rakendusi.



See on äärmiselt mugav konfiguratsioon, isegi üle jõu käiv, kui algne eesmärk on lihtsalt Bitcoin sõlme käivitamine. Teisest küljest, kui soovite täielikult ära kasutada kõiki Umbreli ja Start9-i isehostitavaid rakendusi, on see võimsusaste just teie jaoks õige.



![Image](assets/fr/043.webp)



Sõltuvalt teie kasutusotstarbest saate valida kas 2TB SSD, nagu teistes konfiguratsioonides, või otse 4TB SSD, mille hind on 260 eurot, kui soovite salvestada ka isiklikke faile ja laiendada oma isehostingukasutust. 2TB SSD puhul on konfiguratsiooni kogumaksumus 660 eurot, 4TB SSD puhul aga 800 eurot.



### Veel mõned näpunäited





- Kui soovid osta kasutatud seadmeid ja maksta bitcoin'idega, siis tule kohale sinu lähedal toimuvale kokkusaamisele! Teiste osalejatega vesteldes leiate kindlasti sobiva varustuse hea hinnaga, aidates samal ajal hoida Bitcoin ümbritsevat ringmajandust elus. Samuti on see võimalus saada kasu kogukonna usaldusväärsetest nõuannetest.





- Internetiühenduse jaoks on loomulikult vaja RJ45 Ethernet-kaablit, vähemalt süsteemi paigaldamiseks.





- Mõned keskkonnad, näiteks Umbrel, võimaldavad teil kasutada Wi-Fi, kuid jõudlus on üldiselt kehvem (eriti kui soovite oma Lightning-sõlme kasutada eemalt, sest see võib mõjutada). Kui valite Wi-Fi, veenduge, et teie masinal on sisseehitatud kaart või lisage ühilduv dongle.





- Kasutage alati tootja originaalvõimsust Supply oma masina jaoks. See on väga oluline, et vältida teie seadme kahjustamist ja tulekahju tekkimise ohtu.





- Kui teie masinal ei ole sisseehitatud akut, on hea mõte investeerida inverterisse, et vältida ootamatuid väljalülitusi.





- Sõltuvalt teie seadmete väärtusest ja geograafilisest asukohast võib olla asjakohane ka piksekaitse süsteem, kas otse jaotuskilbis või kasutatavas vooluvõrgus.





- Lõpetuseks, ärge unustage optimeerida oma masina jahutust: puhastage seda regulaarselt ja paigaldage see jahedasse, hästi ventileeritavasse ja rahulikku kohta, et vältida ülekuumenemist, mis võib põhjustada drosseldamist (protsessori kiiruse vabatahtlik piiramine).



# Bitcoin sõlme lihtne paigaldamine


<partId>ca6cf2a5-0bcc-41d9-b556-0d38865bf98f</partId>




## Umbrel: palju rohkem kui Bitcoin sõlme


<chapterId>dd4c04f1-924a-43e1-94f3-ea9fbc83dd43</chapterId>



Umbrel on isiklik serveri operatsioonisüsteem, mis on loodud selleks, et teha isehostimine kättesaadavaks: paigaldate Umbreli, avate brauseri `umbrel.local` ja haldate kõike lihtsa kaugjuhtimissüsteemi Interface kaudu.



Projekt populariseeris esmalt ühe klikiga Bitcoin ja Lightning-sõlme idee, seejärel laienes see tõeliseks "kodupilveks": failide ja fotode salvestamine, multimeedia voogedastus, võrguvahendid, koduautomaatika, kohalik tehisintellekt ja sajad rakendused, mis on paigaldatavad integreeritud App Store'ist.



Umbrelis töötab iga rakendus Dockeri konteineris (isolatsioon, aatomi uuendused, sõltumatu start/stopp). Interface tsentraliseerib juurdepääsu kõigile neile rakendustele, pakkudes ühekordset sisselogimist (koos valikulise 2FA-ga), operatsioonisüsteemi ja rakenduste uuendamist ühe klõpsuga, masina reaalajas jälgimist (protsessor, RAM, temperatuur, salvestusruum), rakenduste vaheliste õiguste haldamist ja ülevaadet nende tarbimisest.



Umbreli eesmärk on seega anda teile tagasi kontroll ja konfidentsiaalsus teie andmete üle, ilma et peaksite toetuma pilveteenustele, lisaks lihtsalt Bitcoin sõlme käitamisele.



### Umbrel Home vs umbrelOS



Umbrel pakub kahte erinevat lähenemist:





- [**Umbrel Home**] (https://umbrel.com/umbrel-home): see on kasutusvalmis miniserver, mis on spetsiaalselt loodud ja optimeeritud umbrelOSi jaoks. Kompaktne, vaikne, Ethernet-ühendusega, varustatud NVMe SSD-ga (kuni 4 TB valikuliselt), 16 GB RAM-i ja neljatuumalise protsessoriga. Tellige see, ühendage see ja minge `umbrel.local`. Töötav Umbrel on teil mõne minutiga käivitatud ja töökorras. See on plug-and-play-variant.



![Image](assets/fr/081.webp)





- [**umbrelOS**](https://umbrel.com/umbrelos): see on operatsioonisüsteem, mille saate ise oma riistvarale (mini-PC, NUC, torn, spetsiaalne sülearvuti...) paigaldada. Teil on sama Interface ja sama App Store nagu Umbrel Home'il.



![Image](assets/fr/080.webp)



Mõlemal juhul on kasutajakogemus tarkvara poolel identne: brauseripõhine haldamine, ühe klikiga uuendused, rakenduste paigaldamine soovi korral... DIY-lahendus on sageli odavam kui Umbrel Home'i ostmine (sõltuvalt kasutatavast masinast). Siiski ei soovitaks ma tingimata alati valida DIY-varianti, sest **Umbrel Home'i ostmine aitab otseselt kaasa projekti arendamise rahastamisele**, kuna selle ärimudel põhineb riistvara müügil. Ja ausalt öeldes on hind 389 eurot 2TB salvestusruumi eest väga mõistlik, arvestades pakutava masina kvaliteeti.



![Image](assets/fr/079.webp)



Järgmises peatükis uurime, kuidas paigaldada umbrelOS DIY oma masinale. Kuid te võite seda BTC 202 kursust samamoodi jälgida, kui olete otsustanud Umbrel Home'i kasuks.



### Kasutusjuhtum: Bitcoin sõlme ja kodupilve vahel



Umbrel võib jääda väga minimalistlikuks ja keskenduda ainult Bitcoin-le või areneda tõeliseks multifunktsionaalseks isiklikuks serveriks, sõltuvalt teie vajadustest. Siin on Umbreli peamised kasutusalad:





- Lihtne Bitcoin-sõlm**: see on põhiline kasutusviis, millele Umbrel on algusest peale toetunud. Võite käivitada Bitcoin core (või Knots), ühendada oma rahakotid otse oma sõlme, paljastada Electrumi serveri, võõrustada oma Mempool Block explorer, et vaadata Blockchain ja hinnata tasusid... Need on need kasutusalad, millele me selles kursuses keskendume.



![Image](assets/fr/082.webp)





- Lightning Network**: LND või Core Lightning, mis on kaks Lightning Network rakendust, võimaldab teil ka oma Lightning-sõlme hallata. Tänu paljudele olemasolevatele rakendustele saate avada kanaleid, hallata oma likviidsust, teha makseid, automatiseerida tasakaalustamist, pakkuda teenuseid, ühendada kaugkasutatava Wallet või kasutada Interface täiustatud haldust. Seda konkreetset kasutusjuhtumit käsitleme meie järgmisel LNP 202 kursusel.



![Image](assets/fr/083.webp)





- Üldine self-hosting**: Nextcloud, Immich, Jellyfin/Plex, DNS-ülesed reklaamblokeerijad (Pi-hole/AdGuard), VPN-id (WireGuard, Tailscale), koduautomaatika (Home Assistant), varukoopiad, märkmete haldamine, kontoritööriistad, kohalik AI (Ollama + Open WebUI)... Umbrel võib muutuda teie isiklikuks serveriks, mis võimaldab teil taastada kontrolli oma andmete üle. Te ise hostite teenuseid, mida kasutate iga päev, kasutades lihvitud kasutajakogemust, mis sarnaneb väga palju välistele lahendustele, säilitades samas täieliku kontrolli oma andmete ja privaatsuse üle.



Rakendusi konteineritesse paigutades saate Umbreli kujundada nii, nagu soovite: alustage lihtsa Bitcoin sõlme ja mõne selle ökosüsteemiga seotud rakendusega, seejärel paigaldage oma Bitcoin sõlme kõrvale Lightning-sõlm ja rikastage oma instantsi järk-järgult vajalike isehostetavate rakendustega.



### Ühendus ja vastastikune abi



Üks Umbreli peamisi eeliseid konkurentide ees on selle suur ja väga aktiivne kasutajaskond. Nendega saab ühendust peamiselt [nende Discordi](https://discord.gg/efNtFzqtdx) ja [nende veebifoorumi](https://community.umbrel.com/) kaudu. Siit leiate mitte ainult praktilisi nõuandeid, vaid eelkõige lahendusi probleemide lahendamiseks või vigade parandamiseks. See on suurepärane koht alustamiseks, edasiliikumiseks ja lõpuks ka teiste kasutajate aitamiseks, et te ei jääks oma Coin-ga üksi.



![Image](assets/fr/084.webp)



### UmbrelOS litsents



Umbreli kood on avalikult kättesaadav (seda saab vaadata, Fork ja muuta), kuid see ei ole tõelise avatud lähtekoodiga litsentsi all. Tegelikult levitatakse umbrelOSi [*PolyForm Noncommercial 1.0*] litsentsi (https://polyformproject.org/licenses/noncommercial/1.0.0/) alusel, kuigi mõned sellega seotud arendusvahendid on saadaval MIT-litsentsi alusel.



Praktiliselt võite umbrelOSiga teha peaaegu kõike, mida soovite, kui see on isiklikuks, mitteäriliseks kasutamiseks: modifitseerimine, levitamine mittetulunduslikel eesmärkidel, tuletiste loomine enda või mittetulundusühingute jaoks, tingimusel, et järgite õiguslikke teateid.



Siiski on keelatud müüa Umbrel'i või selle teisendeid (näiteks eelnevalt kokkupandud masinat, millele on eelnevalt paigaldatud UmbrelOS), pakkuda Umbrel'iga seotud teenuseid kaubanduslikult või integreerida selle koodi toote sisse kasumi saamiseks.



Tehniliselt ei piira see litsents Umbreli paigaldamist, auditeerimist ega kohandamist isiklikuks kasutamiseks. Juriidiliselt kaitseb see projekti loata edasimüügi või kommertshostingu eest, eriti pilvepakkujate poolt. Umbrel ei ole seega avatud lähtekoodiga, kuigi selle kood jääb avalikult kättesaadavaks.



Siiski säilitab iga poes olev rakendus oma litsentsi, mis on sageli avatud lähtekoodiga.




## Full node paigaldamine koos vihmavarjuga


<chapterId>61bc09c7-787d-4649-b142-457ec018b0f4</chapterId>



Nüüd, kui meil on olemas kogu vajalik teave, on aeg süveneda üksikasjadesse. Selles õpetuses näitame teile, kuidas paigaldada täielik Bitcoin sõlme, kasutades UmbrelOS-i.



### Vajalikud materjalid



Siinkohal kasutame UmbrelOS x86 kujutist (täpsemalt x86_64 versiooni). Seda juhendit saate järgida ükskõik millisel masinal, kui see ei ole varustatud ARM-arhitektuuriga protsessoriga (mitte Apple Silicon, Raspberry Pi jne). See tähendab, et mis tahes arvuti, millel on 64-bitine Intel või AMD protsessor, on piisav, kui see vastab miinimumnõuetele, sõltuvalt sellest, kuidas te kavatsete oma Umbrelit kasutada (soovitatav on vähemalt kahetuumaline protsessor).



Kui olete valinud Raspberry Pi 5 (mida ma ei soovita, nagu eelmises punktis mainitud), on paigaldus veidi erinev. Seejärel saate jälgida seda spetsiaalset õpetust ja pöörduda tagasi minu kursusele, kui olete kord Interface veebis `http://umbrel.local`:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Nagu eelmises punktis mainitud, valisin selle õpetuse läbiviimiseks väikese renoveeritud arvuti, mille leidsin hea hinnaga: *Lenovo ThinkCentre M900 Tiny*, mis on varustatud Intel Core i7 protsessori ja 16 GB RAM-iga. See on väga mugav konfiguratsioon Umbreli käivitamiseks, eriti Bitcoin sõlme jaoks. Siiski valisin selle konfiguratsiooni, sest tahan hiljem paigaldada Lightning-sõlme ja muid nõudlikumaid rakendusi. Samuti lisasin oma ThinkCentre'ile 2 TB SSD, et säilitada täielik Blockchain ja ikkagi mugav varu. Selle konfiguratsiooni puhul on kogumaksumus 270 eurot koos kõigi kuludega.



![Image](assets/fr/001.webp)



Mulle meeldib eriti Lenovo ThinkCentre Tiny seeria, sest need on kompaktsed, vaiksed ja väga vastupidavad masinad. Need arvutid on ettevõtete seas väga populaarsed ja seetõttu leidub neid rohkesti kasutatud turul, kus võib leida huvitavaid konfiguratsioone vahemikus 70-200 eurot.



Kui te, nagu mina, olete valinud arvutit ilma monitorita, **peate monitori ja klaviatuuri** ühendama ainult paigaldamise ajaks. Pärast seda saate sellele kaugjuurdepääsu teisest arvutist samas võrgus (või muude meetodite abil, mida käsitleme hilisemates peatükkides). Samuti vajate RJ45 Ethernet-kaablit, et ühendada masin kohaliku võrguga, ja vähemalt 4 GB suurust USB-mälupulka, et salvestada paigalduskujutis.



Kokkuvõtteks on siinkohal esitatud nõuded varustusele:




- Arvuti x86_64 protsessoriga (vähemalt kahe-, soovitatav neljatuumaline);
- RAM-mälu (vähemalt 4 GB, pikemaajalise kasutamise korral soovitatakse 8 GB või rohkem);
- SSD (soovitatav + 2 TB);
- USB-mäluseade (+ 4 GB) UmbrelOS-i kujutise paigaldamiseks;
- Monitor ja klaviatuur (kasulik ainult esmaseks paigaldamiseks, kui arvuti ei ole sellega varustatud);
- RJ45 Ethernet-kaabel.



### 1. samm - arvuti paigaldamine



Sõltuvalt valitud riistvarast on esimene samm arvuti erinevate komponentide kokkupanek. Näiteks minu puhul oli esialgse SSD mahutavus ainult 256 GB, seega kasutan seda uuesti ja asendan selle 2 TB SSD-ga. Kui soovite ka RAM-moodulid välja vahetada, siis on nüüd õige aeg seda teha.



### 2. samm: Valmistage ette käivitatav USB-klahv



Enne UmbrelOSi paigaldamist oma masinasse peate looma käivitatava USB-ketta, mis sisaldab operatsioonisüsteemi. Kõik 2. sammu sammud tuleb teha teie isiklikus arvutis (mitte otse arvutis, mis on mõeldud teie sõlmpunktiks).





- Alustage UmbrelOSi uusima versiooni allalaadimisega USB-formaadis:



Mine [Umbreli ametlikule veebilehele, et laadida alla ISO image](https://download.umbrel.com/release/latest/umbrelos-amd64-usb-installer.iso) USB-mälu installimiseks USB-mälu abil. Veenduge, et valite x86_64 arhitektuuriga ühilduva versiooni (fail nimega `umbrelos-amd64-usb-installer.iso`). Allalaadimine võib võtta aega, kuna kujutis on üsna suur.



![Image](assets/fr/002.webp)





- Paigaldage Balena Etcher:



Käivitatava USB-pulga loomiseks kasutate lihtsat, platvormideülest tööriista nimega [Balena Etcher](https://www.balena.io/etcher/). Laadige see alla ja installige see oma arvutisse.



![Image](assets/fr/003.webp)





- Sisestage vähemalt 4 GB suurune tühi USB-mäluseade:



Ühendage USB-mälu oma arvutisse (sellesse, millele olete just alla laadinud UmbrelOSi ja Balena Etcheri kujutise). **Hoiatus: kõik võtmel olevad andmed kustutatakse**. Veenduge, et see ei sisalda ühtegi olulist faili.





- Kirjutage ISO-kujutis USB-pulgale Balena Etcheriga:



Käivitage Balena Etcher ja valige äsja alla laaditud ISO-faili `umbrelos-amd64-usb-installer.iso`, klõpsates nupul "*Flash from file*". Seejärel valige sihtseadmeks USB-mälu ja klõpsake kirjutamise alustamiseks nuppu "*Flash!*".



![Image](assets/fr/004.webp)



Kui operatsioon on lõpule viidud, on teil UmbrelOS-i sisaldav käivitatav USB-mälu, mis on valmis Umbreli käivitamiseks ja installimiseks teie masinasse.



![Image](assets/fr/005.webp)



### 3. samm: arvuti käivitamine USB-mäluseadmelt



Nüüd, kui teie UmbrelOS-i sisaldav käivitatav USB-pulk on valmis, saate süsteemi paigaldamise alustamiseks arvutit selle kaudu käivitada. Ühendage USB-mälupulk oma põhikompuutrist lahti ja sisestage see seadmesse, kuhu soovite Umbreli ja Bitcoin sõlme paigaldada.



Nagu selle peatüki alguses selgitatud, vajate installimiseks ekraaniseadet ja sisendseadet. Ühendage kuvar HDMI (või muu pordi kaudu, sõltuvalt teie arvutist) ja ühendage klaviatuur USB kaudu masinaga. Neid seadmeid on vaja ainult paigaldamiseks; pärast seda ei ole neid vaja, sest Umbrelile pääseb teisest arvutist kaugjuhtimise teel ligi. Ühendage need kaks seadet oma arvutiga.



**Nipp:** Kui teil ei ole kodus äärega ekraani, võite kasutada oma telerit. Selle HDMI (või muu) sisendiga saab seda kasutada ajutiselt ekraanina, kuni paigaldate operatsioonisüsteemi.



Umbrel vajab ilmselt internetiühendust. Ühendage RJ45 Ethernet-kaabel oma seadme ja ruuteri vahel.



![Image](assets/fr/006.webp)



Lülitage oma masin sisse. Enamikul juhtudel peaks see automaatselt tuvastama USB-mäluseadme ja käivitama selle pealt. Seejärel ilmub UmbrelOS Interface paigaldusekraan.



Kui seade käivitub teise süsteemi või kuvab veateate, tähendab see tõenäoliselt, et seade ei käivitu automaatselt USB-mäluseadmelt. Sellisel juhul taaskäivitage seade ja sisenege BIOS/UEFI seadistustesse (tavaliselt pääseb arvutitootjast sõltuvalt vajutades `DEL`, `F2`, `F12` või `ESC`). Seejärel muutke alglaadimisjärjekorda, et anda prioriteet USB-klahvile. Seejärel taaskäivitage seade, et käivitada UmbrelOS.



### Samm 4: Installige UmbrelOS oma arvutisse



Kui seade on USB-pulgalt käivitunud, tervitab teid Interface UmbrelOSi paigaldus. See samm hõlmab süsteemi paigaldamist otse teie masina Hard sisemisele kettale.



Ilmuvas ekraanis on loetletud kõik arvuti poolt tuvastatud sisemised mäluseadmed. Iga ketta juures on number, nimi ja salvestusmaht. Otsige üles ketas, millele soovite Umbreli paigaldada. **Hoiatus: kõik sellel kettal olevad failid kustutatakse lõplikult.**



![Image](assets/fr/007.webp)



Kui olete tuvastanud õige ketta (tavaliselt suurima mahutavusega, et mahutada Blockchain), märkige sellele määratud number. Näiteks, kui valitud ketas ilmub numbri `2` all, sisestage lihtsalt `2` ja vajutage klaviatuuril klahvi `Enter`.



![Image](assets/fr/008.webp)



Programm vormindab valitud ketta, installib UmbrelOSi ja konfigureerib süsteemi automaatselt. See võib võtta paar minutit. Laske protsessil katkematult kulgeda.



![Image](assets/fr/009.webp)



Kui paigaldus on lõpetatud, palutakse teil seade välja lülitada. Arvuti väljalülitamiseks vajutage suvalist klahvi.



![Image](assets/fr/010.webp)



Nüüd saate eemaldada USB-klahvi, klaviatuuri ja ekraani, mida teie Umbrel enam ei vaja. Teie sõlmpunktist jääb alles vaid toiteallikas Supply ja RJ45 Ethernet-kaabel.



![Image](assets/fr/011.webp)



Enne seadme taaskäivitamist kontrollige kahte järgmist punkti:





- USB-mäluseade on lahti ühendatud**: kui see jääb ühendatuks, võib süsteem taaskäivituda siseketta asemel selle abil;
- Ethernet-kaabel on ühendatud**: seade peab töötamiseks olema ühendatud ruuteriga.



Vajutage toitenuppu. Süsteem käivitub automaatselt sisekettalt, kuhu UmbrelOS paigaldati. Esimene käivitamine võib võtta umbes **5 minutit**. Selle aja jooksul initsialiseerib Umbrel oma teenused ja Interface.



Avage teisest arvutist (teie igapäevasest arvutist), mis on ühendatud **sellesse kohalikku võrku**, veebilehitseja (Firefox, Chrome...) ja minge aadressile:



```
http://umbrel.local
```



Seda Address kasutatakse Umbrel Interface graafilise kasutaja Interface kaugjuurdepääsuks ja konfigureerimise alustamiseks.



Kui Address `http://umbrel.local` ei tööta teie brauseris pärast vähemalt 5-minutilist ootamist, proovige lihtsalt:



```
http://umbrel
```



Kui see ikka veel ei toimi, sisestage oma Umbreli kohalik IP Address otse brauserisse. Näiteks (asendage `42` teie Umbreli majutava masina numbriga kohalikus võrgus):



```
http://192.168.1.42
```



Umbreli IP Address tuvastamiseks on mitu meetodit, alates kõige lihtsamast kuni kõige arenenumani:





- Avage oma marsruuteri administratsioon Interface ja leidke Umbreli seadme IP Address kohalikus võrgus.





- Kasutage võrgu skaneerimise tarkvara, näiteks Angry IP Scanner, et tuvastada ühendatud seadmeid ja leida teie Umbreli IP Address.



![Image](assets/fr/012.webp)



https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d



- Viimase abinõuna ühendage monitor ja klaviatuur uuesti seadme külge, logige sisse (vaikimisi kasutajanimi: `umbrel`, parool: `umbrel`) ja sisestage järgmine käsk:



```
hostname -I
```



Nüüd olete valmis Umbreli kasutamiseks!



### Samm 5: Umbreliga alustamine



Umbreli konfigureerimise alustamiseks klõpsake nupule "*Start*".



![Image](assets/fr/013.webp)



#### Konto loomine



Valige pseudonüüm või sisestage oma nimi, seejärel määrake tugev parool. Olge ettevaatlik: see parool on ainus takistus, mis kaitseb juurdepääsu teie Umbrelile teie võrgustikust (ja seega potentsiaalselt ka teie bitcoinidele, kui te kasutate Lightning-sõlme Umbrelil). See kaitseb ka kaugjuurdepääsu Tor'i või VPN-i kaudu, kui need teenused on lubatud.



Valige tugev parool ja tagage, et teil on vähemalt üks varukoopia (soovitatav on kasutada paroolihaldurit).



https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Kui olete sisestanud oma parooli, klõpsake nupule "*Loo*".



![Image](assets/fr/014.webp)



Teie Umbreli konfiguratsioon on nüüd valmis.



![Image](assets/fr/015.webp)



#### Interface avastamine



Umbreli Interface on üsna intuitiivne:





- Avalehel saate vaadata oma paigaldatud rakendusi ja vidinaid.



![Image](assets/fr/016.webp)





- "*App Store*" võimaldab paigaldada uusi rakendusi,



![Image](assets/fr/017.webp)





- Menüü "*Failid*" koondab kõik teie Umbrelil salvestatud dokumendid.



![Image](assets/fr/018.webp)





- Menüü "*Settings*" võimaldab teil muuta oma vihmavarju seadeid ja pääseda ligi selle teabele, sealhulgas:
    - Uuendage, taaskäivitage või peatage masin;
    - Vaadake vaba salvestusruumi, RAM-i kasutamist ja protsessori temperatuuri;
    - Vahetage taustapilti;
    - Halda kaugjuurdepääsu Tor'i, aktiveeri Wi-Fi või 2FA kaudu.



![Image](assets/fr/019.webp)



#### Turvalisuse ja ühenduse seaded



Kõigepealt soovitan tungivalt lubada kahefaktorilist autentimist (2FA). See lisab teie paroolile täiendava Layer turvalisuse. See on peaaegu hädavajalik, kui kavatsete kasutada oma Umbrel'i isiklike failide salvestamiseks, Lightning-sõlme käivitamiseks või muude tundlike tegevuste teostamiseks.



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Selleks klõpsake seadetes vastaval kastil.



![Image](assets/fr/020.webp)



Seejärel skaneerige kuvatavat QR-koodi oma autentimisrakendusega. Seejärel sisestage 6-kohaline dünaamiline kood oma Umbrelil olevale väljale.



Nüüdsest alates nõuab iga uus ühendus teie Umbreliga nii parooli kui ka kahefaktorilise autentimise (2FA) rakenduse poolt genereeritud 6-kohalist koodi.



![Image](assets/fr/021.webp)



Mis puudutab kaugjuurdepääsu Tor'i kaudu, siis kui te seda ei vaja, siis soovitan jätta see valik välja lülitatud, et piirata teie Umbreli rünnakupinda. Vaikimisi on teie sõlme võimalik kasutada ainult masinast, mis on ühendatud samasse kohalikku võrku. Tor'i kaudu juurdepääsu lubamine võimaldab teil siiski oma Umbrelit ka liikvel olles hallata.



Kui te lubate selle funktsiooni, on teoreetiliselt võimalik, et mis tahes masin maailmas võib üritada ühendust teie sõlme, tingimusel, et ta teab Tor Address. Teie parool ja 2FA kaitsevad teid siiski.



Kui aktiveerite selle võimaluse, veenduge, et teil on kahefaktoriline autentimine (2FA) sisse lülitatud, tugev parool ja et te ei avalda kunagi oma Tor-ühendust Address.



Sisestage lihtsalt see Tor Address oma Tor-brauserisse, et pääseda Umbreli Interface-le ligi mis tahes võrgustikust.



![Image](assets/fr/026.webp)



Lõpuks saate sellel seadete lehel aktiveerida ka Wi-Fi-ühenduse. Kui teie Umbrel'i majutaval masinal on Wi-Fi võrgukaart või Wi-Fi dongle, võimaldab see teil pääseda internetti ilma RJ45 kaablit kasutamata. Sõltuvalt teie konfiguratsioonist võib see lahendus siiski ühendust aeglustada, mis võib mõjutada esialgset sünkroniseerimist (IBD) ja sõlme edasist kasutamist (nt Lightning-tehingute puhul). Mina isiklikult ei soovita seda võimalust, sest sõlme ei ole mõeldud mobiilseks kasutamiseks: sellele on alati juurdepääs eemalt, seega võiksite selle sama hästi jätta ühendatuks.



### 6. samm: Bitcoin sõlme paigaldamine Umbrelile



Nüüd, kui UmbrelOS on teie masinale õigesti paigaldatud ja konfigureeritud, võite jätkata Bitcoin sõlme paigaldamist. Miski poleks lihtsam: minge App Store'i, avage kategooria "*Bitcoin*", seejärel valige rakendus "*Bitcoin Node*" (tegelikult on see Bitcoin core).



![Image](assets/fr/022.webp)



Seejärel klõpsake nupule "*Install*".



![Image](assets/fr/023.webp)



Kui paigaldus on lõpetatud, käivitab teie Bitcoin-sõlm oma IBD (*Initial Block Download*): see laeb alla ja valideerib kõik tehingud ja plokid alates Bitcoin loomisest 2009. aastal.



![Image](assets/fr/024.webp)



See etapp on eriti aeganõudev, sest selle kestus sõltub mitmest tegurist, sealhulgas sõlme vahemälu jaoks eraldatud RAM-i mahust, ketta kiirusest, internetiühenduse kiirusest ja protsessori võimsusest. Seetõttu on kestuste vahemik sõltuvalt konfiguratsioonist väga lai. Suure jõudlusega arvutiga (NVMe SSD, +32 GB RAM, võimas protsessor ja hea internetiühendus) saab IBD valmis umbes kümne tunniga. Teisalt võib vana protsessor, vähene RAM või, mis veelgi hullem, mehaaniline Hard ketas (mida tungivalt ei soovitata) pikendada seda toimingut mitme nädalani.



Tavalise konfiguratsiooniga arvutiga (korralik protsessor, 8-16 GB RAM ja SSD) võimaldab see umbes 2-7 päeva.



Et IBD-d pisut kiirendada, saate parameetri `dbcache` abil suurendada sõlme vahemälu (mida kasutatakse peamiselt UTXO komplekti jaoks, mida me hiljem uuesti vaatame) jaoks eraldatud RAM-i. Umbrelil tehakse see muudatus teie sõlme parameetrites, vahekaardil "*Optimization*".



![Image](assets/fr/025.webp)



Vaikimisi on Bitcoin core parameetri `dbcache` väärtus 450 MiB ehk umbes 472 MB. Selle väärtuse suurendamisega saab IBD-d veidi kiirendada. Siiski ei soovitaks ma seda parameetrit tingimata liiga kõrgeks ajada: isegi selle seadmine 4 GiB-le muudab sünkroniseerimise ainult umbes 10% kiiremaks ja võib põhjustada IBD ajal katkestuse korral aja kaotuse.



Olge ettevaatlik, et mitte eraldada teie masinale liiga suurt väärtust. Kui UmbrelOSi jaoks olemasolev RAM-ruum saab otsa, võib teie sõlme töö järsku peatuda, katkestades IBD ja nõudes selle käsitsi taaskäivitamist, mis toob kaasa märkimisväärse ajakaotuse.



Kui soovite rohkem teada saada parameetri `dbcache` mõjust algsele sünkroniseerimisele, siis soovitan seda Jameson Loppi analüüsi: [*Effects of DBcache Size on Bitcoin Node Sync Speed*](https://blog.lopp.net/effects-dbcache-size-Bitcoin-node-sync-speed/)



Kui teie sõlme IBD on lõpule viidud (100% sünkroniseerimine), on teil nüüd täielikult töökorras Bitcoin sõlme. Palju õnne, te olete nüüd Bitcoin võrgu lahutamatu osa!



![Image](assets/fr/027.webp)



Järgmises osas uurime teie uue sõlme praktilist kasutamist: kuidas ühendada Wallet sellega ja milliseid rakendusi peaksite paigaldama, et saada suveräänseks Bitcoineriks.





# Wallet ühendamine sõlmpunktiga


<partId>418d0afd-3a61-4b5a-9db4-203c0335fd29</partId>



## Indekseerijad: roll, toimimine ja lahendused


<chapterId>4f93c07a-f0cb-435f-8b68-162f316d7039</chapterId>



Kui te olete juba enne selle kursuse läbimist Bitcoin sõlmedega tutvunud, olete võib-olla kokku puutunud terminiga "indekseerija". Need on sellised tööriistad nagu Electrs või Fulcrum, mida saab lisada Bitcoin core sõlme. Kuid mis on nende roll täpselt? Kuidas nad praktikas töötavad? Ja kas te peaksite oma uude Bitcoin-sõlme ühe installima? Seda uurime selles peatükis.



### Mis on indekseerija?



Üldiselt on indekseerija programm, mis skaneerib toorandmete kogumi, võtab välja asjakohased võtmed (näiteks sõnad, identifikaatorid ja aadressid) ning koostab abifaili, mida nimetatakse "indeksiks", kus iga võti viitab andmete täpsele asukohale korpuses. See eeltöötlusetapp kasutab protsessoriga seotud aega ja nõuab veidi kettaruumi, kuid see välistab vajaduse töödelda kogu korpust iga kord, kui andmebaasi küsitakse; lihtsalt indeksi küsitlemine annab peaaegu kohese vastuse.



Tavainimese jaoks on see sama põhimõte nagu raamatu register: kui otsite konkreetset teavet, siis kogu raamatu uuesti lugemise asemel vaadake indeksit, et leida otse lehekülg, kus otsitav teave on kirjas.



Bitcoin-sõlmes, nagu Bitcoin core, salvestatakse Blockchain andmed töötlemata, kronoloogilisel kujul. Iga plokk sisaldab tehinguid, mis omakorda sisaldavad sisendeid ja väljundeid, ilma Address, identifikaatori või Wallet järgi liigitamata. Selline lineaarne korraldus on optimeeritud plokkide valideerimiseks, kuid ei sobi sihipäraseks otsinguks. Näiteks kui soovite leida kõik konkreetse Address-ga seotud tehingud indekseerimata sõlmes, peate käsitsi läbi vaatama kogu Blockchain, plokkide ja tehingute kaupa. Just siinkohal tuleb appi Bitcoin-sõlme indekseerija.



![Image](assets/fr/085.webp)



Indekseerija on spetsiaalne tarkvaraprogramm, mis analüüsib seda toorandmete massi (Blockchain, Mempool, UTXO kogum) ja eraldab võtmed, näiteks tehingu identifikaatorid, aadressid ja plokkide kõrgused. Nendest võtmetest koostab ta oma indeksi, seostades iga võtme teabe täpse asukohaga sõlme salvestusruumis.



![Image](assets/fr/086.webp)



Indekseerimine võimaldab teil otsida teavet oma sõlme kohta kiiresti, täpselt ja tõhusalt. Näiteks kui ühendate oma sõlme Wallet nagu Sparrow, saab see peaaegu kohe kuvada Address tasakaalu. Konkreetselt öeldes küsib see indekseerija päringuga nagu: "_Millised UTXOd on seotud selle skriptiga-Hash?_" Indekseerija vastab peaaegu kohe, ilma et ta peaks kogu Blockchain uuesti läbi lugema, sest need andmed on juba tema andmebaasis loetletud.



### Kas Bitcoin core-l on indekseerija?



Ilma lisatarkvara vajaduseta ei paku Bitcoin core rangelt võttes täielikku Address indekseerijat, mis oleks võrreldav selliste tarkvarade nagu Electrs või Fulcrum puhul. Sellegipoolest sisaldab see mitmeid sisemisi indekseerimismehhanisme, samuti valikulisi võimalusi päringuvõimaluste laiendamiseks. Olukorra täielikuks mõistmiseks peame tegema kõrvalepõike projekti ajalukku.



Kuni Bitcoin core versioonini 0.8.0 põhines tehingu valideerimine globaalsel tehinguindeksil, mida tuntakse kui "txindex". See indeks viitas kõigile Blockchain tehingutele ja nende väljunditele. Kui sõlm sai uue tehingu, vaatas ta seda indeksit, et kontrollida, kas tarbitud väljundid (sisendites) on tegelikult olemas ja kas need ei ole juba kulutatud. seetõttu oli `txindex` tollal tehingu valideerimiseks hädavajalik.



Sellisel lähenemisviisil olid siiski omad piirangud: see oli aeglane, kulukas salvestamise osas ja teabe osas üleliigne. Selle probleemi lahendamiseks võeti versioonis 0.8.0 kasutusele valideerimismudeli uuendamine, mida nimetatakse ***Ultraprune***. Selle asemel, et salvestada kõike tehinguindeksite kujul, säilitab Bitcoin core lihtsat andmebaasi, mis on pühendatud ainult UTXOdele ja mida nimetatakse `chainstate` (igapäevakeeles nimetatakse seda "UTXO set"), ning uuendab selle nimekirja, kui väljundeid tarbitakse ja luuakse.



See meetod on palju kiirem ja salvestab ainult registri praeguse seisu, muutes `txindex` indekseerija mittevajalikuks. Kuid selle asemel, et kustutada `txindex` kood, on arendajad otsustanud jätta selle funktsionaalsuse lihtsa parameetri taha (`txindex=1`). Lubades selle valiku oma sõlmes, saate te küsida mis tahes tehingut selle `txid`-st.



Vastupidiselt levinud arvamusele ei paku Bitcoin core Address-põhist indekseerimist nagu Electrs või Fulcrum. Sellel valikul on mitu põhjust:





- Bitcoin core roll ei ole muutuda täielikuks Block explorer-ks ega pakkuda igale kasutusalale kohandatud API-d. Address-põhise indeksi integreerimine tähendaks Commitment pikaajalist hooldust, mis ületab tarkvara esialgse ulatuse.





- Enamikku kasutusjuhtumitest saab juba katta muul viisil. Näiteks Address tasakaalu hindamiseks võib kasutada käsku `scantxoutset`, mis küsib otse UTXO kogumit, ilma et oleks vaja täielikku indeksit.





- Igal tarkvaraprogrammil on konkreetsed nõuded indekseeritavate andmete vormingu või tüübi suhtes (Address, Hash skript, patenteeritud silt jne). On paindlikum ja loogilisem lasta neil programmidel luua oma kohandatud indeksid, kui fikseerida Bitcoin core üldlahendust.



Bitcoin core omab küll valikulist tehinguindikaatorit (`txindex`), mis on tema ajaloolise toimimise jäänuk, kuid see ei paku Address indeksit ega otsest Interface komplekssete otsingute jaoks. Seetõttu võib mõnel juhul olla kasulik lisada väline indekseerija.



### Kas peaksite oma sõlme lisama Address indekseerija?



Address indekseerija, näiteks Electrs või Fulcrum, lisamine ei ole kohustuslik; see sõltub teie konkreetsetest vajadustest.



Kui soovite lihtsalt ühendada Wallet, näiteks Sparrow, oma sõlme, et vaadata saldosid ja edastada tehinguid, on see täiesti võimalik otse Bitcoin core Interface RPC kaudu, kas lokaalselt või eemalt Tori kaudu.



Teisest küljest, et kasutada keerukamat tarkvara, näiteks käivitada Mempool.Locally, paigaldamine Address indekseri muutub hädavajalikuks ruumi Block explorer.



Indekseerija nõuab teatud aja sünkroniseerimist (vähem kui IBD) ja võtab täiendavalt kettaruumi. Kui teie SSD-kettal on pärast Blockchain allalaadimist veel piisavalt vaba ruumi, saate hõlpsasti lisada indekseerija.



### Milline indekseerija valida?



Seda tüüpi Address indeksi koostamiseks ja kättesaadavaks tegemiseks kasutatakse tavaliselt kahte tarkvara: **Electrs** ja **Fulcrum**. Need tööriistad indekseerivad Blockchain vastavalt skript-Hash (aadressid) ja pakuvad seejärel välja standardiseeritud Interface (Electrumi protokoll), millega ühenduvad arvukad rahakotid, näiteks Electrum Wallet, Sparrow või Phoenix.



![Image](assets/fr/087.webp)



Lihtsalt öeldes on Electrs üsna kompaktne: see indekseerib Blockchain kiiremini ja võtab vähem kettaruumi, kuid täidab päringuid veidi halvemini kui Fulcrum. Seevastu Fulcrum tarbib rohkem kettaruumi ja indekseerimine võtab kauem aega, kuid pakub paremat jõudlust päringute tegemisel.



Individuaalseks kasutamiseks soovitan Electrs'i: see tarbib vähem ruumi, on hästi hooldatud ja kuigi see on teatud taotluste puhul veidi aeglasem kui Fulcrum, on see siiski igapäevaseks kasutamiseks enam kui piisav. Kui teil on aega ja kettaruumi, võite proovida ka Fulcrumi, mis töötab oluliselt paremini, eriti rahakottide puhul, kus on arvukalt kontrollitavaid aadresse.



Konkreetselt öeldes vajab Electrs 2025. aasta augustis ligikaudu 56 GB salvestusruumi, Fulcrumi puhul on see näitaja ligikaudu 178 GB. Seega sõltub teie indekseerija valik ka teie mälumahust:




- Kui teie kettaruum on väga piiratud, peate leppima Bitcoin core-ga ilma välise Address indekseerijata.
- Kui soovite kasutada indekseerijat, kuid olete siiski piiratud mahuga, valige Electrs.
- Kui teil on piisavalt kettaruumi, võib Fulcrum olla just see, mida te otsite.



Selle BTC 202 kursuse ülejäänud osas kasutan ma Electrs, kuid te võite hõlpsasti jälgida Fulcrumi kasutamist: paigaldusprotseduur on identne, nagu ka Interface ühendus Wallet-ga, kuna mõlemad avaldavad Electrumi serverit.



### Kuidas paigaldada Umbrelile indekseerija?



Electrs (või Fulcrum) installimiseks teie Umbrelile on protseduur lihtne: minge App Store'i, otsige vastav rakendus (asub vahekaardil Bitcoin) ja seejärel vajutage nupule "*Install*".



![Image](assets/fr/028.webp)



Kui paigaldus on lõpule viidud, jätkab Electrs sünkroniseerimise (indekseerimise) faasi, mis võib võtta mitu tundi.



![Image](assets/fr/029.webp)



Kui sünkroonimine on lõpule viidud, saate ühendada oma Wallet tarkvara oma Electrumi serveriga, mida majutatakse Umbrelis.



## Kuidas ühendada Wallet ja Bitcoin sõlme?


<chapterId>35519b1a-f681-4a69-a652-9fbe510cd17f</chapterId>



Nüüd, kui teil on täielik Bitcoin sõlmpunkt, on aeg see kasutusele võtta! Järgmises peatükis uurime oma Umbreli instantsi muid võimalikke kasutusvõimalusi. Alustame siiski põhitõdedest: ühendage oma Wallet tarkvara, et kasutada oma Blockchain teavet ja jaotada tehinguid oma sõlme kaudu.



Nagu eespool mainitud, on kaks peamist ühendusliidest:




- Otsene ühendus Bitcoin core-ga RPC kaudu;
- Või ühendage Electrumi serveriga (Electrs või Fulcrum).



Selles õpetuses keskendume oma sõlme ühendamisele Tori kaudu, kuna see on algajatele lihtne ja turvaline lahendus. Soovitan tungivalt vältida oma sõlme RPC pordi avalikustamist, sest valesti konfigureerimine kujutab endast märkimisväärset ohtu teie andmete turvalisusele ja konfidentsiaalsusele. Tor'i kaudu toimuva side peamine puudus on selle aeglus. Järgmises peatükis uurime kiiret ja turvalist alternatiivi Torile teie sõlme kaugjuurdepääsuks: VPN.



Kasutame selles peatükis näitena Sparrow, kuid protseduur on sama kõigi teiste Wallet haldustarkvarade puhul, mis aktsepteerivad ühendusi Electrumi serveritega. Leidke lihtsalt vastav seade oma rakenduse parameetritest (tavaliselt "*Server*", "*Network*", "*Node*"...).



Avage Sparrows vahekaart "*Fail*" ja minge menüüsse "Settings".



![Image](assets/fr/030.webp)



Seejärel klõpsake "*Server*", et pääseda juurde ühenduse parameetritele.



![Image](assets/fr/031.webp)



Seejärel avastate kolm võimalust oma tarkvara sidumiseks Bitcoin-sõlmega:




- Avalik server* (kollane): vaikimisi, kui teil ei ole Bitcoin sõlme, ühendab see valik teid avaliku sõlme, mida te ei oma (tavaliselt ettevõtte). See valik ei ole siinkohal oluline, kuna teil on Umbrelil oma sõlme.
- Bitcoin core* (Green): see valik vastab ühendusele Interface RPC kaudu, st otse Bitcoin core-ga.
- Private Electrum* (sinine): see valik võimaldab teil luua ühenduse oma indekseerija Interface Electrumi serveri (Electrs või Fulcrum) kaudu.



### Ühendus Bitcoin core RPC



Kui teie Umbrel-sõlme ei ole indekseerija, peate valima selle valiku. Sparrow puhul klõpsake "*Bitcoin core*".



![Image](assets/fr/032.webp)



Seejärel peate sisestama mitu teavet, et luua ühendus oma sõlme. Kõik need andmed on kättesaadavad Umbreli rakendusest "*Bitcoin Node*", klõpsates Interface paremas ülemises nurgas asuvat nuppu "*Connect*".



![Image](assets/fr/033.webp)



Vahekaardil "*RPC üksikasjad*" kuvatakse kogu vajalik teave ühendamiseks. Valige ühendus Tor Address kaudu (failis `.onion`).



![Image](assets/fr/034.webp)



Sisestage need andmed Sparrow wallet vastavatesse väljadesse ja vajutage seejärel nupule "*Testiühendus*".



![Image](assets/fr/035.webp)



Kui ühendus on edukas, ilmub Green märkeruut ja kinnitussõnum.



![Image](assets/fr/036.webp)



Interface Sparrow wallet paremal allosas olev märkeruut on nüüd Green (mis näitab otsest ühendust Bitcoin core-ga).



**Märkus:** Et ühendus õnnestuks, peab teie sõlm olema 100% sünkroonitud. Kui see ei ole nii, oodake IBD lõpuni.



### Ühendage Electrsiga



Kui teie võrgusõlmes on indekseerija, on parem ühendada sellega, kui kasutada otse Bitcoin core, sest teie päringuid töödeldakse kiiremini.



Mine Sparrows vahekaardile "*Privaatne Electrum*".



![Image](assets/fr/037.webp)



Seejärel peate sisestama mitu teavet, et luua ühendus oma indekseerijaga. Need andmed leiate Umbreli rakendusest "*Electrs*" (või vajaduse korral "*Fulcrum*").



Valige vahekaart "*Tor*", et saada `.onion` ühendus Address. Kui soovite ühendada mobiiltelefoni Wallet tarkvara, saate ka otse QR-koodi skaneerida.



![Image](assets/fr/038.webp)



Sisestage lihtsalt oma Electrumi serveri Tor Address väljale "*URL*" ja vajutage seejärel nupule "*Test Connection*".



![Image](assets/fr/039.webp)



Kui ühendus on edukas, kuvatakse kontrollmärk ja kinnitussõnum.



![Image](assets/fr/040.webp)



Interface Sparrow wallet paremas alumises nurgas olev märkeruut muutub siniseks (värv, mis tähistab ühendust Electrumi serveriga).



**Märkus:** Selleks, et ühendus toimiks, peab teie indekseerija olema 100% sünkroonitud. Kui see ei ole nii, oodake, kuni indekseerimisprotsess on lõpetatud.



Nüüd teate, kuidas ühendada Wallet oma Bitcoin sõlme! Järgmises peatükis tutvustan teile mitmeid Umbrelil kättesaadavaid lisarakendusi, mis mulle eriti meeldivad ja mis võimaldavad teil oma sõlme kaudu Bitcoin igapäevast kasutamist tõhustada.




## Ülevaade olemasolevatest rakendustest


<chapterId>2a5ccfbe-0b17-44c9-863c-b7e8cb4b4594</chapterId>



Umbrel pakub ulatuslikku rakenduste poodi. Nagu näete, on seal palju Bitcoin-ga seotud vahendeid, kuid ka väga erinevaid rakendusi väga erinevates valdkondades: teenuste ja failide isehostimise lahendused, tootlikkusrakendused, üldisemad finantsvahendid, meediahaldus, võrgu turvalisus ja haldamine, arendus, tehisintellekt, sotsiaalvõrgustikud ja isegi koduautomaatika.



Sellel BTC 202 kursusel keskendume ainult Bitcoin-ga seotud rakendustele. Siiski võite vabalt uurida ülejäänud kataloogi vahendeid, mis võivad teile kasulikud olla.



Loomulikult oleks võimatu loetleda siin kõiki Bitcoin rakendusi. Selles peatükis tahaksin teile tutvustada olulisi vahendeid, mis hõlbustavad ja rikastavad teie igapäevast Bitcoin kasutamist.



### Mempool.space



Kui Bitcoin igapäevases kasutuses on üks tööriist, mis on tõeliselt asendamatu, siis on see Block explorer. Kas see on kättesaadav internetis või kohapeal paigaldatud, see muudab Blockchain toorandmed struktureeritud, selgeks ja kergesti loetavaks vorminguks. Samuti on selles otsingumootor, mis võimaldab kasutajatel kiiresti leida konkreetne plokk, tehing või Address.



Konkreetsemalt öeldes võimaldab explorer teil hinnata teie tehingu blokki lisamiseks vajalikke tasusid, seejärel jälgida selle arengut: teada saada, kas see on tõenäoliselt lähitulevikus lisatud, sõltuvalt tasude turust, ja lõpuks kinnitada, et see on tõepoolest blokki lisatud. Samuti pakub see võimalust analüüsida oma varasemaid tehinguid ja tutvuda nende ajalooga. Lühidalt öeldes on see bitcoineri Šveitsi armee nuga.



Nagu eelnevalt mainitud, võib explorer olla veebipõhine veebisait või käivitada seda lokaalselt teie masinas. Veebipõhiste teenuste peamine puudus on see, et need võivad ohustada teie privaatsust. Ilma VPN-i või Torita võib explorerit haldav server teie IP Address siduda teie vaadeldavate tehingutega, mis võib pakkuda ideaalset sisenemispunkti ahelanalüüsiks.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Veelgi enam, teie Interneti-teenuse pakkuja (ISP) võib teada, et te vaatate konkreetset tehingut Block explorer saidi kaudu. See tõstatab ka usaldusküsimuse: te peate usaldama, et võrguteenus annab teile oma tehingute kohta täpset teavet, ilma et saaksite selle tõesust ise kontrollida.



Seepärast on alati kõige parem kasutada oma kohalikku Block explorer. Sel viisil ei leki teie otsingutegevusega seotud andmed välja, sest kõiki päringuid töödeldakse otse teie poolt kontrollitavas masinas, ilma et need läbiksid Internetti. Veelgi enam, lokaalne otsija tugineb teie enda Bitcoin sõlme andmetele, mille olete ise valideerinud vastavalt oma reeglitele ja mida võite usaldada.



Umbrel pakub mitmeid plokkide uurijaid:




- Mempool.Space
- Bitfeed
- BTC RPC Explorer



Mulle meeldib eriti Mempool.Space, mille ma olen oma sõlme paigaldanud. Pange tähele: enamiku plokkide uurijate kasutamiseks Umbrelil on vaja Address indekseerijat. Seega on vaja Bitcoin Node (või Bitcoin Knots) rakendust, mis on 100% sünkroniseeritud Blockchain, samuti indekseerija nagu Electrs või Fulcrum, mis on samuti 100% sünkroniseeritud.



Kui rakendus on paigaldatud, avage see lihtsalt, et pääseda ligi oma ekspluateerijale.



![Image](assets/fr/041.webp)



Kui soovite rohkem teada saada Mempool.Space exploreri kasutamisest, siis soovitan seda põhjalikku õpetust:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

### Välgussõlm



Nüüd, kui teil on oma Bitcoin-sõlm, saate luua ka oma Lightning-sõlme off-chain tehingute tegemiseks, ilma et peaksite toetuma kolmanda osapoole infrastruktuurile.



Umbrel pakub mitmeid rakendusi, mis aitavad teil oma Lightning-sõlme käivitada. Saate valida juba kahe peamise rakenduse vahel:




- LND, rakenduse *Lightning Node* kaudu;
- Core Lightning.



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Seejärel saate oma sõlme hallata Interface peaprogrammist või veelgi suurema funktsionaalsuse ja täiustatud võimaluste saamiseks installida *Ride The Lightning* või *ThunderHub*. Need tööriistad annavad teile oma sõlme jaoks palju põhjalikuma veebipõhise Interface haldussüsteemi.



https://planb.network/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.network/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

![Image](assets/fr/088.webp)



Lõpuks soovitan *Lightning Network+* rakendust, mis võimaldab teil leida eakaaslasi, kellega avada kanaleid, võimaldades nii väljaminevaid kui ka sissetulevaid sularahatehinguid.



![Image](assets/fr/089.webp)



Tänu Umbrelile on isikliku Lightning-sõlme haldamine oluliselt lihtsustatud, kuid see on siiski suhteliselt keeruline. Seetõttu käsitleme seda teemat lähemalt tulevases kursuses, mis on täielikult sellele kasutusalale pühendatud.



### Tailscale



Teine rakendus, mis mulle Umbrelil eriti meeldib, on Tailscale. See on VPN-rakendus, mille eesmärk on lihtsustada turvaliste võrkude loomist mitme seadme vahel, kus iganes nad ka ei asuks. Erinevalt traditsioonilistest VPN-dest, mis tuginevad tsentraliseeritud serveritele, kasutab Tailscale WireGuard-protokolli, et luua otsast lõpuni krüpteeritud ühendusi teie erinevate masinate vahel. See tähendab, et saate toimiva VPN-i kasutusele võtta vaid mõne minutiga, ilma et oleks vaja keerulisi võrgukonfiguratsioone.



Umbreli puhul ühendab Tailscale'i paigaldus teie Bitcoin-sõlme teie enda virtuaalse privaatvõrguga. Pärast konfigureerimist saab teie sõlme privaatne Tailscale'i IP Address, millele on juurdepääs ainult teistest samasse Tailscale'i võrku ühendatud seadmetest (näiteks arvutid, nutitelefonid ja tahvelarvutid). See ühendus on otsast lõpuni krüpteeritud ja ei liigu läbi kaitsmata avaliku võrgu, mis suurendab oluliselt turvalisust võrreldes krüpteerimata ühendusega.



![Image](assets/fr/090.webp)



Konkreetselt öeldes pakub Tailscale teie Umbreli kasutamisel mitmeid eeliseid:





- Saate hallata Interface Umbrel'i või pääseda ligi oma sõlme seotud rakendustele (näiteks Mempool, Ride The Lightning, ThunderHub...) kõikjalt, nagu oleksite samas kohalikus võrgus, ilma et peaksite avama pordid internetis ja ilma, et peaksite läbima Tor'i, mis on väga aeglane;





- Saate luua ühenduse oma Electrumi serveriga (Electrs või Fulcrum) või otse Bitcoin core-ga VPN-i kaudu, vältides Tor'i. See tagab turvalise ühenduse, mis on võrreldav Tori kasutamisega, kuid palju suurema kiiruse ja väiksema latentsusega. Lühidalt öeldes säilitate Tori privaatsuse ja turvalisuse eelised, kuid naudite samal ajal Clearneti ühenduse kiirust. On-Chain Wallet puhul võib see kasu tunduda marginaalne, kuid kui te plaanite hiljem luua oma Lightning-sõlme, on erinevus märkimisväärne. Tõepoolest, maksete tegemine oma sõlme kaudu liikvel Toril on paljude vajalike vahetuste tõttu äärmiselt aeglane, samas kui Tailscale'iga töötab see suurepäraselt.





- Ei ole vaja konfigureerida NAT-reegleid, avada porte ega luua tavalist VPN-serverit. Kui rakendus on paigaldatud Umbrelile ja teie seadmetele, luuakse võrk automaatselt.



Tailscale on Umbrel on seega väga huvitav lahendus, kui soovite oma võrgusõlme kasutada ükskõik kus maailmas turvaliselt, suure jõudlusega ja lihtsalt konfigureeritavalt, ilma privaatsust või turvalisust ohverdamata.



Tailscale'i paigaldamiseks ja konfigureerimiseks Umbrelil vt selle õpetuse 4. jagu: "*Tailscale'i kasutamine Umbrelil*":



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Nostr



Nostr, mis on akronüüm väljendist "*Notes and Other Stuff Transmitted by Relays*", on avatud, detsentraliseeritud protokoll, mis on loodud selleks, et võimaldada sõnumite avaldamist ja vahetamist Internetis ilma tsentraliseeritud platvormist sõltumata. Igal kasutajal on paar krüptograafilist võtit: avalik võti (`npub`), mis on identifikaatoriks, ja privaatvõti (`nsec`), mida kasutatakse sõnumite allkirjastamiseks ja nende autentsuse tagamiseks.



Sõnumid edastatakse sõltumatute releede võrgu kaudu. Selline hajutatud ülesehitus muudab Nostri tsensuurikindlaks: ükski server ei kontrolli juurdepääsu või levitamist ning kasutaja võib ühendada nii palju releesid, kui ta soovib.



See protokoll on Bitcoin kogukonnas väga populaarne, sest sarnaselt Bitcoin-le käsitleb Nostr digitaalse suveräänsuse ja andmekontrolli küsimusi. Selle looja Fiatjaf on arendaja, kes on ökosüsteemis juba tunnustatud oma arvuka panuse eest.



Oma vihmavarju abil saate optimeerida Nostri kasutamist. Installeerides rakenduse ***Nostr Relay***, saate oma privaatse relee otse oma masina peal hoida, tagades, et kõik teie postitused ja suhtlus Nostris salvestatakse lokaalselt ja need ei saa kaduda avalike releede kustutamise tõttu.



Nostr kliendid ***noStrudel*** või ***Snort*** on saadaval ka Umbrelil. Tänu nendele rakendustele saate avaldada, lugeda, otsida profiile ja suhelda Nostri ökosüsteemiga otse Interface veebist oma Umbrelil.



Lõpuks on Umbrelil olemas ***Nostr Wallet Connect*** rakendus, mis võimaldab Nostris kasutada Lightning-makseid. Konkreetselt öeldes saate oma tulevase Lightning-sõlme siduda oma Nostri klientidega, et saata mikromakseid, mida nimetatakse "*zaps*", et tasustada sisu või suhelda rahaliselt, ilma et oleks vaja minna läbi kolmanda osapoole teenuse. Need maksed saadetakse otse teie isiklikust sõlmest teie kanalite kaudu.



Et teada saada, kuidas kõiki neid rakendusi kasutada, soovitan teil vaadata seda täielikku õpetust:



https://planb.network/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

### BTCPay server



BTCPay Server on tasuta, avatud lähtekoodiga makseprotsessor, mis võimaldab teil vastu võtta makseid Bitcoin ja Lightning Network kaudu ilma vahendajateta, säilitades samal ajal rahaliste vahendite isehoidmise.



BTCPay Serveri arhitektuur põhineb Bitcoin sõlmel ja Lightningi puhul ühilduval rakendusel (LND, Core Lightning...), mis teeb sellest ühe ainsa täielikult mittekasutatava PoS-lahenduse. See on ka kõige põhjalikum tarkvara jälgimiseks ja raamatupidamiseks.



![Image](assets/fr/091.webp)



Kui teil on ettevõte ja soovite võtta Bitcoin makseid vastu otse oma Umbrel-sõlme kaudu, on BTCPay Server rakendus teie jaoks ideaalne. Kui soovite selle teema kohta rohkem teada saada, soovitan teil tutvuda järgmiste allikatega:





- BIZ 101 kursus Bitcoin kasutamise kohta teie ettevõttes:



https://planb.network/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a



- POS 305 kursus BTCPay Serveri kasutamise kohta:



https://planb.network/courses/6fc12131-e464-4515-9d3f-9255365d5fa1



- BTCPay serveri õpetus:



https://planb.network/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


# Täiustatud mõisted ja parimad tavad


<partId>fc77a62a-8d9f-4144-9080-3057b04db2c6</partId>



## Umbrel-sõlme hooldamine


<chapterId>06d77d09-bf24-4555-b2ba-c08bbda477c7</chapterId>



Selle viimase osa alustuseks ja enne edasiliikumist edasijõudnuteooria juurde, tahaksin selles lühikeses peatükis uurida parimaid tavasid ja konkreetseid tegevusi, mida saate teha, kui teie Umbrel-sõlm on paigaldatud, sünkroonitud ja õigesti konfigureeritud. Kuidas te seda igapäevaselt hooldate?



### Seadmete tervena hoidmine



Usaldusväärne sõlmpunkt algab stabiilsest riistvarast. Veenduge, et sõlme sisaldav masin on korralikult ventileeritud, Dust-vaba ja paigaldatud kuiva keskkonda, eemal igasugustest soojus- ja niiskusallikatest. Vältige selle kokkusurumist kitsasse ruumi ja valige hästi ventileeritud koht.



Raspberry Pi ja mini-PC-de puhul ummistab Dust lõpuks jahutusradiaatorid, tõstes temperatuuri ja põhjustades throttling'i (ressursikasutuse vabatahtlik piiramine), mis omakorda toob kaasa sõlme tõhususe languse. Seepärast soovitan õhuvõtu ja ventilaatori perioodilist puhastamist, ideaalis iga paari kuu tagant.



Veenduge, et kasutate kvaliteetset Supply, sest ebastabiilne pinge võib põhjustada süsteemi kahjustumist ja isegi tulekahjuohtu. Ideaalis peaksite kasutama originaaltoite Supply, mille on tarninud teie masina tootja. Hoiduge ka toiteallikate Joule'i efektist tingitud ülekuumenemise eest: järgige alati maksimaalset lubatud võimsust ja ärge kunagi ühendage mitut toiteallikat kaskaadina.



Samuti soovitan investeerida UPSi. See kaitseb teie sõlme ootamatute väljalülituste eest, võimaldab Umbrelil katkestuse korral puhtalt sulgeda ja tagab töö jätkumise mikrokatkestuste või lühiajaliste rikete ajal.



Salvestusruumi poolel jälgige arengut: kui ketas läheneb küllastumisele, kaaluge ruumi vabastamist (kasutamata rakenduste deinstalleerimine, indekseerimisseadete kohandamine) või üleminekut suuremale SSD-kettale. Täieliku Bitcoin-sõlme puuduseks on see, et selle salvestusruumi nõuded suurenevad pidevalt, sest iga 10 minuti järel luuakse uus plokk ja vanu plokke ei saa kustutada (välja arvatud juhul, kui tegemist on pruned-sõlmega). Seetõttu soovitan teil riistvara ostmisel planeerida piisavalt suurt mahutavust (vähemalt 2 TB).



### Ajakohastamine



Sõlmede uuendused on olulised kolmel peamisel põhjusel: esiteks turvalisus (haavatavuse parandused, võrgu karastamine ja DoS-kaitse), teiseks ühilduvus (releepoliitika muudatused, vormingu muudatused ja protokolli uuendused) ning kolmandaks töökindlus ja jõudlus (veaparandused, ressursikulu ja muud parandused). Seega kontrollige regulaarselt, et UmbrelOS ja teie rakendused oleksid ajakohased:





- Süsteemi uuendamine: Avage seadete menüü, seejärel klõpsake parameetri "*UmbrelOS*" kõrval nuppu "*Check for Update*".



![Image](assets/fr/042.webp)





- Rakenduste uuendamiseks: Mine App Store'i. Kui mõni teie rakendustest vajab uuendamist, ilmub Interface paremasse ülemisse nurka punase mulliga nupp. Lihtsalt klõpsake sellel, seejärel värskendage iga rakendust.



Tehke seda toimingut regulaarselt, et hoida oma operatsioonisüsteemi ja rakendusi ajakohasena.



### Varukoopiaid



Kui kasutate oma Bitcoin sõlme ainult tehingute valideerimiseks ja levitamiseks, kuid teie rahakotte hallatakse väljaspool Umbrelit (nt Hardware Wallet ja Sparrow wallet abil), ei ole midagi, mida otse Umbrelisse varundada. Sellisel juhul jääb oluliseks varunduseks teie välise Wallet taastamislause ja Descriptor ning see kehtib olenemata sellest, kas kasutate oma sõlme või mitte. Seega ei muutu teie eelmisest konfiguratsioonist midagi.



Teisest küljest, sõltuvalt Umbrelil kasutatavatest lisarakendustest, võib olla vaja teha täiendavaid varukoopiaid. See kehtib eelkõige juhul, kui kasutate Umbrelil Lightning-sõlme. Sellisel juhul on hädavajalik teha varukoopia seed-st, mis on tarnitud teie Lightning-sõlme paigaldamisel. Lisaks seed-le on vaja ajakohastatud ***Static Channel Backup (SCB)***, et saaksite probleemide korral taastada oma Lightning-sõlme. SCB võimaldab teil taastada oma vahendid kanalite sunniviisilise sulgemise teel. Kui kas seed või SCB puudub, on Lightning-sõlme taastamine võimatu.



Umbrel pakub ka võimalust automaatselt ja dünaamiliselt varundada seda SCB-d oma serverites Tori kaudu, et tagada alati ajakohase faili kättesaadavus. Sellisel juhul on sõlme taastamiseks vaja ainult seed.



Neid aspekte käsitleme üksikasjalikult järgmisel LNP202 kursusel.



### Igapäevane tööohutus



Kasutage Interface Umbrel'i jaoks pikka, unikaalset ja juhuslikku salasõna ning ärge unustage kahefaktorilise autentimise (2FA) aktiveerimist. Rakenduste puhul, mis pakuvad nii parooli- kui ka 2FA-kaitset, aktiveerige alati mõlemad ja muutke vaikimisi paroole.



Ärge kunagi avage armatuurlauda Internetti ilma turvalise värava kasutamiseta (näiteks VPN, Tor või ainult kohalik juurdepääs). Piirake paigaldatavate rakenduste arvu ja kustutage regulaarselt need, mida te enam ei vaja, et vähendada ründepinda.



Et süvendada oma teadmisi arvutiturbe kohta üldiselt, soovitan teil kindlasti tutvuda selle teise tasuta kursusega:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Diagnoos ja eneseabi



Kui teie Umbrelil esineb viga, siis esmalt generate diagnostikapakett UmbrelOSi või asjaomase rakenduse tõrkeotsingu sektsiooni kaudu, seejärel käivitage rakendus puhtalt uuesti. Vajaduse korral proovige ka süsteemi täielikku taaskäivitamist.



Kui probleem püsib, soovitan teil [liituda Umbreli kasutajaskonnaga nende Discordis](https://discord.gg/efNtFzqtdx). Alustage otsinguga, et teha kindlaks, kas keegi on juba samade raskustega kokku puutunud ja leidnud lahenduse. Kui ei ole, võite saata sõnumi kanalis `general-support`. Võite kasutada ka [Umbreli foorumit](https://community.umbrel.com/).



Need alad võimaldavad teil mitte ainult jälgida turvakuulutusi ja uuendusi, vaid ka esitada küsimusi ja lõppkokkuvõttes aidata teisi kasutajaid. Sageli avastatakse parimad tavad just nende vahetuste käigus.



Nende lihtsate harjumuste abil jääb teie Umbrel-sõlm stabiilseks, turvaliseks ja kasulikuks nii teie kui ka Bitcoin võrgu jaoks.




## IBD ja vastastikuse avastamise protsessi mõistmine


<chapterId>175ac9d1-ea23-45d9-9918-d3e7352435cd</chapterId>



Teie Bitcoin-sõlm käivitub ilma eelnevate teadmisteta tehinguajaloo kohta. Esialgu on see lihtsalt arvuti, kus töötab tarkvara (Bitcoin core või sarnane). Et saada täielikult sünkroniseeritud ja toimivaks Bitcoin sõlmpunktiks, peab ta lokaalselt rekonstrueerima Ledger seisu, kontrollides kõiki plokke, mis on avaldatud alates Genesis plokist (plokk 0, mille Satoshi Nakamoto avaldas 3. jaanuaril 2009). Seda sammu nimetatakse **IBD (_Initial Block Download_)**.



IBD koosneb iga ploki ja tehingu eraldi allalaadimisest ja kontrollimisest, kohaldades konsensuseeskirju, et luua oma versioon Blockchain-st. Eesmärgiks ei ole mitte lihtsalt kontrollida kontrollimata andmete koopiat, vaid jõuda täiesti sõltumatult samale järeldusele kui võrgu aus enamus.



![Image](assets/fr/092.webp)



### IBD verstapostid



Sünkroniseerimine algab sammuga _**headers-first**_. Teie sõlmpunkt küsib plokkide pealkirjade jada mitmelt vastaspoolelt ja kontrollib igaühele neist Proof of Work, raskuse kohandamist, süntaksit, samuti Timestamp ja versiooni numbri reegleid. Lühidalt öeldes tagab ta, et iga saadud päis vastab konsensuseeskirjadele.



![Image](assets/fr/093.webp)



Tuletame meelde, et Bitcoin plokk koosneb 80 baidi pikkusest päisest ja tehingute loetelust. Ploki sõrmejälg saadakse, kui sellele päisele, mis sisaldab 6 välja, kohaldatakse kahekordset SHA-256 Hash:




- versioon
- Hash eelmisest plokist
- Merkle Root tehingute kohta
- Timestamp (suurem kui 11 eelneva ploki mediaan)
- raskusaste
- Nonce



![Image](assets/fr/094.webp)



Tehingud kantakse Merkle Tree-le. See on struktuur, mis võtab kokku suure andmekogumi (antud juhul kõik tehingud plokis), koondades nende hashid järk-järgult kaks korda kuni ühe "juureni", tõestades seega, et element kuulub kogumisse (ja tuvastades mis tahes muudatused). Sel viisil muudab iga tehingu muutmine ka Merkle Tree juurt ja seega ka ploki päise sõrmejälge. SegWit on kasutusele võtnud eraldi täiendava Commitment küpsiste (allkirjade) jaoks, mis paigutatakse mündipanka.



![Image](assets/fr/095.webp)



See samm _**headers-first**_ võimaldab sõlmpunktil tuvastada haru, millel on kõige rohkem tööd (sõltumata selle plokkide arvust), mis on haru, mille peal Bitcoin sõlmed sünkroniseerivad. Kui see haru on tuvastatud, laeb sõlmpunkt paralleelselt mitmest ühendusest plokkide sisu alla, seejärel valideerib iga tehingu: formaat, skriptide kehtivus (v.a `assumevalid=1`), summad ja topeltkulutuste puudumine. Iga eduka kontrolli puhul uuendatakse `chainstate/` andmebaasis `chainstate/` kulutamata müntide hetkeseisu (UTXO komplekt): kulutatud väljaminekud eemaldatakse, samas kui uued kehtivad väljaminekud lisatakse.



Mempool seevastu tuleb mängu ainult siis, kui lähenetakse ahela tipule: seni, kuni sõlme jääb hiljaks, ei ole tal ühtegi pooleliolevat tehingut, mida salvestada.



Kui IBD on lõpule viidud, läheb sõlmpunkt oma tavapärasesse faasi: ta valideerib uued plokid, kui need avaldatakse, säilitab oma Mempool koos pooleliolevate tehingutega vastavalt oma relee-eeskirjadele, edastab tehinguid ja plokke ning haldab kõiki ahela reorganiseerimisi.



### AssumeValid



Bitcoin core sisaldab mehhanismi, mille eesmärk on vähendada aega, mis kulub enne sõlme täielikku toimimist, säilitades samal ajal autonoomse kontrollimise põhimõtte olemuse: AssumeValid.



Parameeter `assumevalid` põhineb varasemal võrdlusplokil, mille Hash on integreeritud igasse tarkvaraversiooni. IBD ajal, kui teie sõlm leiab, et see plokk on tõepoolest kõige rohkem tööd teinud harus, võib ta ignoreerida skripti kontrollimist kõigi sellele punktile eelnevate tehingute puhul.



Kõik muud reeglid (plokkide struktuur, Proof of Work, suuruspiirangud, tehingusummad, UTXOd jne) jäävad täielikult kontrollituks. Ainult sellele võrdlusplokile eelnevate skriptide arvutamist ei võeta arvesse. IBD puhul on jõudluse kasv märkimisväärne, kuna allkirjade kontrollimine moodustab suure osa protsessori koormusest. Pärast seda võrdlusblokki pöördub kontrollimine tagasi tavapärasesse olekusse.



Saate sundida kõikide skriptide täielikku valideerimist, lülitades selle mehhanismi välja, mis tähendab palju pikemat IBD-d, kasutades parameetrit `assumevalid=0` failis `Bitcoin.conf`.



### OletameUTXO



`assumeutxo` on veel üks olemasolev parameeter, kuid erinevalt `assumevalid`ist ei ole see vaikimisi aktiveeritud. See mehhanism võimaldab tarkvaral laadida hetkeseisu UTXO komplektist koos selle metaandmetega ja pidada seda ajutiselt võrdlusseisundiks pärast seda, kui on kontrollitud, et päised tõepoolest viivad Blockchain-ni, millel on kõige rohkem tööd.



Seega muutub sõlmpunkt kiiresti töövõimeliseks tavapärasteks kasutusteks (RPC, rahakottide ühendamine jne), käivitades samal ajal taustal omaenda UTXO komplekti täieliku, kontrollitud rekonstrueerimise. Kui see etapp on lõpule viidud, asendatakse esialgne hetkefoto lokaalselt rekonstrueeritud olekuga. Selline lähenemisviis eraldab kiire sõlme pakkumise täielikust verifitseerimisest, ilma viimast kahjustamata.



### Vastastikune avastamine: Kuidas teie sõlmpunkt leiab Bitcoin võrgu?



Kui sõlmpunkt käivitub esimest korda, ei tunne ta veel ühtegi võrdset partnerit. Siiski peab ta leidma teised Bitcoin sõlmed Internetis, et taotleda päiseid, seejärel blokeerida, et täita oma IBD. Nende ühenduste algatamiseks järgib Bitcoin core prioritiseeritud loogikat.



![Image](assets/fr/096.webp)



Kui sõlme taaskäivitatakse pärast seda, kui seda on juba kasutatud, üritab Core kõigepealt uuesti ühendust luua enne väljalülitamist registreeritud väljuvate partneritega, mille andmed on salvestatud failis `anchors.dat`. Seejärel konsulteerib ta oma IP Address raamatut **`peers.dat`**, milles on salvestatud varem kohatud partnerite nimekiri, et nendega uuesti ühendust luua. See on lihtsalt kohalik fail, mida Core ajakohastab ja säilitab. Teisalt on äsja käivitatud uue sõlme puhul need kaks faili tühjad, sest ta ei ole veel kunagi suhelnud teiste Bitcoin sõlmedega.



Sellisel juhul küsib tarkvara _**DNS-seemneid**_. Need on [tunnustatud ökosüsteemi arendajate poolt hallatavad serverid](https://github.com/Bitcoin/Bitcoin/blob/master/src/kernel/chainparams.cpp), mis annavad tagasi eeldatavate aktiivsete sõlmede IP-aadresside loetelu. Need aadressid võimaldavad uuel sõlmpunktil luua oma esimesed ühendused ja taotleda IBDst vajalikke andmeid. Siin on praeguseks (august 2025) aktiivsete *DNS-seemnete* nimekiri:




- Pieter Wuille: `seed.Bitcoin.sipa.be.`
- Matt Corallo: `dnsseed.bluematt.me.`
- Luke Dashjr: `dnsseed.Bitcoin.dashjr-list-of-P2P-nodes.us.`
- Jonas Schnelli: `seed.Bitcoin.jonasschnelli.ch.`
- Peter Todd: "seed.btc.petertodd.net"
- Sjors Provoost: `seed.Bitcoin.sprovoost.nl.`
- Stephan Oeste: oeste: `dnsseed.emzy.de.`
- Jason Maurice: `seed.Bitcoin.wiz.biz.`
- Ava Chow: gW-568.Mainnet.achownodes.xyz.xyz.`seed.Mainnet.achownodes.xyz.`



Enamikul juhtudel piisab *DNS-seemnete* sammust, et luua esimesed ühendused teiste sõlmedega. Kui need serverid ei vasta erandkorras 60 sekundi jooksul, läheb sõlmpunkt üle teisele meetodile: gW-569 koodis on sisseehitatud ja korrapäraselt ajakohastatakse [üle 1000 aadressi sisaldav staatiline nimekiri](https://github.com/Bitcoin/Bitcoin/blob/master/src/chainparamsseeds.h) _seed node_. Kui esimesed kaks IP-aadresside saamise meetodit ebaõnnestuvad, loob see viimane lahendus esialgse ühenduse, millest sõlme saab seejärel taotleda uusi IP-aadresse.



![Image](assets/fr/097.webp)



Viimase abinõuna saate käsitsi Supply IP-aadressid faili `peers.dat` kaudu sundida teatud ühendusi.



Pärast käivitamist mitmekesistab Address sisemine haldur allikaid (eraldi autonoomsed võrgud, clearnet ja Tor, samuti erinevad geograafilised piirkonnad), et vähendada topoloogilise isolatsiooni ohtu. Sõlm loob need väljaminevad ühendused (ühendused, mille ta ise valib ja mis on seetõttu turvalisemad).



Kui teie võrgusõlm kuulab avatud porti (vaikimisi 8333), võtab see vastu sissetulevaid ühendusi. Need tugevdavad võrgu üldist vastupidavust, pakkudes uutele sõlmedele kontaktpunkti, ilma et see tooks teie enda IBD-le erilist kasu. Kui teie sõlm töötab Toril, jääb loogika samaks, kuid kasutatavad aadressid on `.onion` teenused.




## Teie Bitcoin sõlme anatoomia


<chapterId>b420bd9d-7e2a-4984-bc70-2b732a94c8ce</chapterId>



Kui teie sõlme on lõpetanud esialgse sünkroniseerimise, salvestab ta mitu täiendavat andmekogumit lokaalselt, mis võimaldab tal kontrollida plokke ja tehinguid, teenindada võrgukaaslasi ja taaskäivitada kiiresti, säilitades samal ajal oma oleku. sõlme jaoks on olulised 3 peamist telliskivi:




- gW-402 **plokid**, mis on salvestatud kettale,
- **UTXO kogum**, mida hoitakse võtmeväärtusandmebaasis,
- ja **Mempool** salvestatakse RAM-i ja perioodiliselt seeriaviisiliselt.



Lisaks sellele täiendavad pilti mitmed lisafailid (eakaaslased, tasuhinnangud, välistamisnimekirjad, rahakotid jne). Avastame kõigi nende failide rolli.



### Kus asuvad sõlme andmed tegelikult?



Vaikimisi salvestab Bitcoin core oma andmed konkreetsesse töökataloogi. GNU/Linuxi all on see tavaliselt `~/.Bitcoin/`, Windowsi all `%APPDATA%\Bitcoin/` ja macOSi all `~/Library/Application Support/Bitcoin/`. Kui te kasutate pakendatud lahendust (nt sõlmedistribuudis), võib see kataloog olla paigaldatud mujale, kuid selle struktuur jääb samaks. Allpool kirjeldatud olulised alamkaustad ja failid asuvad endiselt siin.



![Image](assets/fr/098.webp)



### Plokid



Blockchain on seega plokkide kogum. Full node salvestab need plokid järjestikuste lamefailidena ja säilitab kiireks otsimiseks paralleelset indeksit. Vajaduse korral (reorganiseerimine, Wallet uuesti skaneerimine, vastastikune teenus) loetakse need andmed uuesti sellisena, nagu nad on.



**Märkus:** Reorganiseerumine ehk resünkroniseerumine on nähtus, mille puhul Blockchain struktuur muutub konkureerivate plokkide olemasolu tõttu samal kõrgusel. See juhtub siis, kui osa Blockchain-st asendatakse teise ahelaga, millel on suurem kogunenud töö. Need resünkroniseerimised on Bitcoin toimimise loomulik osa, kus erinevad kaevandajad võivad leida uusi plokke peaaegu samaaegselt, jagades seega Bitcoin võrgu kaheks. Sellistel juhtudel võib võrk ajutiselt jaguneda konkureerivateks ahelateks. Lõpuks, kui üks neist ahelatest kogub rohkem tööd, loobuvad teised ahelad sõlmedest ja nende plokid muutuvad "vananenud plokkideks" või "orvuks jäänud plokkideks" Seda protsessi, mille käigus üks ahel asendatakse teise ahelaga, nimetatakse resünkroniseerimiseks.



#### Blk*.dat-failid (toorplokkide andmed)



Vastuvõetud ja valideeritud plokid kirjutatakse järjestikku konteineritesse nimega `blkNNNNN.dat`, mis on salvestatud kausta `blocks/`. Iga faili täidetakse järjest, kuni see saavutab maksimaalse suuruse 128 MiB, misjärel Core avab järgmise faili. Sees on iga plokk serialiseeritud võrguformaadis, millele eelneb maagiline identifikaator ja pikkus. Selline korraldus võimaldab kiiret kirjutamist kettale ja hõlbustab plokkide teenindust, et sünkroonida eakaaslasi.



![Image](assets/fr/099.webp)



pruned režiimis säilitab sõlmpunkt ainult nende failide hiljutise akna, et piirata plaadijälge. Ta kustutab vanimad `blk*.dat` konteinerid kohe, kui konfigureeritud ruumi sihtmärk on saavutatud, säilitades samal ajal piisava ajaloo, et püsida kooskõlas kõige tuntuma ahelaga. Indeks ja UTXO komplekt jäävad normaalseks, võimaldades järgmiste tehingute ja plokkide valideerimist.



#### Rev*.dat failid (tühistamisandmed)



Selleks, et reorganiseerimise ajal saaks ajas tagasi minna, salvestab Core paralleelselt iga `blk` failiga ka `revNNNNNN.dat` faili `blocks/`. See fail sisaldab teavet, mis on vajalik ploki mõju tühistamiseks UTXO komplektile: iga ploki poolt tarbitud väljundi kohta salvestatakse vastava UTXO eelmine seisund (kogus, skript, kõrgus...). Bloki katkestamise korral saab sõlme kiiresti taastada eelmise seisundi, ilma et oleks vaja kogu ahelat uuesti skaneerida.



![Image](assets/fr/100.webp)



#### Plokkide indeks (plokid/indeks)



Bloki otsimine otse lamefailidest oleks liiga aeganõudev. Core säilitab seetõttu LevelDB andmebaasi "blocks/index/", mis loetleb iga teadaoleva ploki kohta metaandmed, nagu Hash, kõrgus, valideerimise staatus, "blk" fail ja nihke, kus plokk asub. Kui mõni võrdväärne osapool taotleb plokki või kui sisekomponendil on vaja juurdepääsu konkreetsele plokile, pakub see indeks kiiret juurdepääsu. Ilma selle indeksita oleks vaja liiga palju operatsioone.



![Image](assets/fr/101.webp)



#### Vabatahtlikud indeksid (indexes/)



Mõned indeksid on valikulised ja vaikimisi välja lülitatud, kuna need suurendavad kettaruumi mahtu:




- `indexes/txindex/`, mida me juba mainisime, pakub tehingu → asukoha kaardistamise tabelit, mis võimaldab leida mis tahes kinnitatud tehingu ilma seda sisaldavat plokki teadmata. See on kasulik Wallet `getrawtransaction` tüüpi RPC päringute puhul, kuid on üsna kallis.
- indexes/blockfilter/`, mis võib sisaldada kompaktseid blokifiltreid (BIP157/158) õhukeste klientide jaoks. Need struktuurid kiirendavad kliendipoolset kontrollimist indekseerimissõlme täiendava salvestusruumi arvelt.



### UTXO komplekt (ahelapartii)



Mudel UTXO (*Tehingu väljund*) on Bitcoin raamatupidamislik esitus: iga kasutamata väljund on olemasolev "Coin", mida saab kasutada tulevase tehingu sisendina.



![Image](assets/fr/102.webp)



Kõigi nende osade kogum on antud hetkel T, mis moodustab UTXO komplekti: suur nimekiri kõigist praegu saadaolevatest osadest. See on see olek, mida sõlmpunkt konsulteerib, et otsustada, kas tehing kulutab seaduslikke ühikuid, mida ei ole juba kasutatud eelmises tehingus (Double-spending vältimiseks).



![Image](assets/fr/103.webp)



UTXO komplekt on salvestatud kausta `chainstate/` kompaktse LevelDB andmebaasina. Iga osa seostab tehingu Hash võtme ja väljundindeksist tuletatud võtme väärtusega, mis sisaldab: summat, `scriptPubKey` lukustust, loomise ploki kõrgust ja coinbase'i näitajat.



![Image](assets/fr/104.webp)



Sõlm säilitab LevelDB kohal olevat mälu vahemälu, et absorbeerida sagedasi lugemis- ja kirjutamisoperatsioone. Selle vahemälu suuruse muutmiseks saab kasutada parameetrit `dbcache`: mida suurem see on, seda rohkem mälu kasutab IBD ja praegune valideerimine, kuid selle arvelt tarbitakse rohkem RAM-mälu. Kui Miner leiab uue ploki, kustutab sõlme UTXO hulgast plokis sisalduvate tehingute poolt kulutatud (või tarbitud) väljundid ja lisab uued loodud väljundid.



Teoreetiliselt võiksime tehingu valideerida, skaneerides uuesti plokkide ajalugu, et kontrollida, et väljundit ei ole kunagi kulutatud. Praktikas oleks see aga liiga aeganõudev, sest iga uue tehingu puhul tuleks skaneerida kogu Blockchain. UTXO komplekt annab seega minimaalse ülevaate, mis on vajalik Double-spending puudumise kohalikuks ja mõistliku ajaga tõestamiseks.



Pange tähele, et UTXO komplekt on sageli Bitcoin detsentraliseeritusega seotud murede keskmes, kuna selle suurus kasvab loomulikult kiiresti. See on osaliselt tingitud Bitcoin kasvavast hinnast, mis soodustab osade killustumist, ja osaliselt süsteemi kasvavast kasutuselevõtust: mida rohkem on kasutajaid, seda suurem on nõudlus UTXOde järele.



![Image](assets/fr/105.webp)



UTXO komplekti kasv tuleneb ka Bitcoin lihtsate maksetehingute struktuurist. Tõepoolest, makse sooritamisel tarbitakse sisendina üks UTXO ja luuakse väljundina 2 uut UTXOd (üks makse ja teine Exchange jaoks). Lõpuks pakub ahelanalüüsi heuristika, mida nimetatakse CIOH (*Common Input Ownership Heuristic*), täiendavat stiimulit Coin konsolideerimise vältimiseks.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Kuna osa sellest tuleb hoida RAMis, et kontrollida tehinguid mõistliku aja jooksul, võib UTXO komplekt muuta Full node töö järk-järgult liiga kulukaks. Selle probleemi lahendamiseks on juba olemas mõned ettepanekud, eelkõige [Utreexo](https://planb.network/resources/glossary/utreexo).



### Mempool



Mempool on vastuvõetud, kuid veel kinnitamata kehtivate tehingute kohalik kogum. Meeldetuletuseks: "kinnitatud tehing" on tehing, mis on lisatud kehtivasse plokki. Iga sõlmpunkt säilitab oma Mempool, mis võib erineda teiste võrgusõlmede omast sõltuvalt:




- gW-614-le parameetri `maxmempool` kaudu eraldatud suurus: suurema Mempool-ga sõlme saab mahutada rohkem tehinguid kui väiksema Mempool-ga sõlme (välja arvatud juhul, kui viimane muutub tühjaks);
- gW-433 reeglid: need on sõlme releereeglite alamhulk ja määratlevad omadused, millele kinnitamata tehing peab vastama, et seda Mempool-s aktsepteeritaks;
- tehingu perkolatsioon: erinevate tegurite tõttu võib teatav tehing olla jaotatud võrgu ühte ossa, kuid ei ole veel jõudnud teise ossa.



Oluline on märkida, et sõlme mempoolil ei ole konsensuse väärtust. Bitcoin töötab suurepäraselt isegi siis, kui igal sõlmel on erinev Mempool. Lõppkokkuvõttes on autoriteetsed plokid alati need, mis on lisatud Blockchain. Näiteks isegi kui sõlmpunkt lükkab esialgu tagasi konkreetse tehingu oma Mempool-s (konsensusreeglite kohaselt kehtiv), on ta kohustatud selle vastu võtma, kui see lisatakse lõpuks kehtiva Proof of Work-ga plokki. Kui ta seda ei tee ja lükkab selle ploki tagasi, kuigi see vastab konsensusreeglitele, vallandab ta Hard Fork, st uue, eraldi Bitcoin loomise, milles ta oleks üksi.



#### Mälupoliitika ja mälu haldamine



Kui tehing saabub, rakendab Core rea kontrolle konsensusreeglite (süntaks, kehtivad skriptid, topeltkulutuste puudumine jne) ja Mempool reeglite suhtes, mis on kohalik poliitika (RBF, minimaalsed tasuläved, andmete piirnormid OP_RETURN-s jne). Kui tehing vastab nendele reeglitele, salvestatakse see mällu.



Mempool suurus on piiratud parameetriga `maxmempool` failis `Bitcoin.conf` (sellest lähemalt järgmises peatükis). Vaikimisi on piirang 300 MB. Kui see on täis, tõstab sõlme dünaamiliselt oma minimaalse tasu piirmäära ja heidab kõigepealt välja kõige vähem kasumlikud tehingud (st ta jätab alles tehingud, mis tuleks kõigepealt kaevandada). Liiga vanad tehingud võivad samuti pärast seadistatud viivitust aeguda.



#### Mempool püsivus kettal



Taaskäivitamise kiirendamiseks seeriaviisib Core perioodiliselt Mempool oleku faili `Mempool.dat`, kui sõlmpunkt on välja lülitatud. Lisaks tegelikule Mempool-le, mis jääb mällu, salvestab Core selle `Mempool.dat` faili ka kettale. Kui sõlme järgmine kord käivitatakse, laadib ta selle hetkefoto uuesti ja kustutab kõik, mis ei ole enam kehtiv praeguse Blockchain jaoks.



### Abifailid ja andmebaasid



Mitmed teised failid samal tasemel nagu `blocks/`, `chainstate/` ja `indexes/` osalevad nõuetekohases toimimises:




- `peers.dat` säilitab IP Address potentsiaalsete eakaaslaste raamatut, mida toidab esialgne DNS-otsing, võrguvahetus ja käsitsi lisamine. Kui sõlmpunkt käivitub, saab ta väljuvate ühenduste loomiseks kasutada seda faili.
- Kui sõlm on välja lülitatud, salvestab `anchors.dat` väljuvate partnerite aadressid, nii et saate järgmisel käivitamisel nendega kiiresti uuesti ühendust võtta.
- `banlist.json` sisaldab lokaalseid keelde, mille on otsustanud operaator või sõlm (korduv kehtetu käitumine), et takistada sõlme uuesti ühendumist või ühenduste vastuvõtmist nendelt konkreetsetelt eakaaslastelt.
- "fee_estimates.dat" salvestab vaadeldud kinnituste ajalise horisondi statistikat, mida tasude kalkulaator kasutab, et teha ettepanekuid tasumäärade kohta, mis on kooskõlas tehingu loomisel valitud viivitus-eesmärkidega.
- gW-446.conf` sisaldab teie sõlme konfiguratsiooniparameetreid. Siin saate reguleerida relee reegleid. Sellest räägin teile lähemalt järgmises peatükis.
- `settings.json` sisaldab täiendavaid parameetreid failile `Bitcoin.conf`.
- `debug.log` on diagnostiline tekstilogi, mida saab kasutada vea korral sõlme tegevuse mõistmiseks.
- gW-448.pid` salvestab protsessi identifikaatori töö ajal, mis võimaldab teistel rakendustel või skriptidel bitcoind (*Bitcoin daemon*) hõlpsasti tuvastada ja vajaduse korral sellega suhelda. See luuakse sõlme käivitamisel ja kustutatakse sulgemisel.
- `ip_asn.map` on IP → ASN kaardistamise tabel (iseseisev süsteem), mida kasutatakse bucketing ja peer diversification (valik `-asmap`).
- `onion_v3_private_key` salvestab Tor v3 teenuse privaatvõtme, kui valik `-listenonion` on lubatud, et hoida onion Address stabiilset taaskäivituste vahel.
- `i2p_private_key` salvestab I2P privaatvõtme, kui kasutatakse `-i2psam=`, et luua väljaminevad ja võimalusel sissetulevad ühendused I2P kaudu.
- "cookie" sisaldab ephemeraalset RPC autentimise token (luuakse käivitamisel, kustutatakse sulgemisel), kui kasutatakse küpsiste autentimist. Seda saab kasutada näiteks Wallet tarkvara ühendamiseks.
- `.lock` on andmekataloogi lukk, mis takistab mitme instantsi samaaegset kirjutamist samasse andmekataloogi.
- `guisettings.ini.bak` on GUI seadete (*Bitcoin Qt*) automaatne salvestamine, kui kasutatakse valikut `-resetguisettings`.



Nagu me nägime selle BTC 202 kursuse esimestes osades, on Bitcoin core nii Bitcoin sõlme tarkvara kui ka Wallet. Siiski ei ole see tingimata lahendus, mida ma soovitaksin oma rahakottide haldamiseks, kuna selle Interface jääb põhiliseks ja selle funktsioonid on piiratud võrreldes kaasaegse tarkvaraga, nagu Sparrow või Liana. Core sisaldab ka faile oma rahakottide haldamiseks:





- `wallets/` on vaikimisi kataloog, kus asub üks või mitu;
- `wallets/<nimi>/Wallet.dat` on Wallet SQLite andmebaas (võtmed, kirjeldused, tehingu metaandmed jne);
- wallets/<name>/Wallet.dat-journal` on SQLite'i tagasivõtulogi.



Kokkuvõttes on Bitcoin core faili struktuur järgmine:



```
~/.bitcoin/
├── bitcoin.conf
├── blocks/
│   ├── blk00000.dat
│   ├── blk00001.dat
│   ├── rev00000.dat
│   ├── rev00001.dat
│   └── index/
├── chainstate/
├── indexes/
│   ├── txindex/
│   ├── blockfilter/
│   │   └── basic/
│   │       ├── db/
│   │       └── fltrNNNNN.dat
│   └── coinstats/
│       └── db/
├── wallets/
│   └── <wallet_name>/
│       ├── wallet.dat
│       └── wallet.dat-journal
├── peers.dat
├── anchors.dat
├── banlist.json
├── mempool.dat
├── fee_estimates.dat
├── bitcoind.pid
├── debug.log
├── ip_asn.map
├── onion_v3_private_key
├── i2p_private_key
├── settings.json
├── guisettings.ini.bak
├── .cookie
└── .lock
```



### Uue ploki valideerimise tee



Uue ploki kättesaamisel kontrollib teie sõlme Proof of Work ja üldisemalt konsensuseeskirjade järgimist. Kui kõik on korras, rakendab ta muudatused tehingupõhiselt oma UTXO kogumisse: ta kontrollib, et iga sissekanne kulutab olemasolevaid UTXOsid kehtiva skriptiga, kustutab need UTXOd ja lisab uued väljumised. Kui kõik on kehtiv, kinnitatakse muudatused `chainstate/`i.



Paralleelselt kirjutatakse tühistamisandmed faili `rev*.dat` ja metaandmed indeksisse `blocks/index/`. Seejärel serialiseeritakse plokk õigesse `blk*.dat` faili. Ümberkorralduse korral loeb sõlme `rev*.dat` tagurpidi, et puhtalt lahti ühendada mahajäetud plokid, taastada UTXO komplekt ja seejärel ühendada uue parima ahela plokid.





## Bitcoin.conf mõistmine


<chapterId>c54a629a-ddb1-41cb-9a88-21dfd9be50ca</chapterId>



Fail "Bitcoin.conf" on Bitcoin core peamine Interface konfiguratsioonifail. See võimaldab teil kohandada oma sõlme käitumist ja parameetreid, ilma et peaksite selle lähtekoodi uuesti kompileerima või käsurea muudatusi tegema. Konkreetselt öeldes on see tavaline tekstifail, mis on struktureeritud võtmeväärtuspaaridena, mis tähendab, et faili iga rida viitab konkreetsele parameetrile (võtmele) ja sellega seotud väärtusele, mida saab selle parameetri kohandamiseks muuta.



Võrgu, tehinguvahetuse, jõudluse, indekseerimise, logimise ja RPC juurdepääsu parameetrid saab määratleda failis "Bitcoin.conf". See konfiguratsioonifail ei muuda siiski kunagi protokolli konsensusreegleid: see määrab ainult sõlme kohalikku poliitikat (relee reeglid), viisi, kuidas ta ühendab, indekseerib ja eksponeerib teenuseid.



### Asukoht ja prioriteet



Vaikimisi asub fail "Bitcoin.conf" Bitcoin core andmekaustas. See on see kuulus kataloog, mida me eelmises peatükis mainisime. Bitcoin core ei loo seda faili siiski automaatselt, välja arvatud teatud keskkondades, näiteks Umbrel. Kui seda ei ole veel olemas, peate te generate selle ise looma, luues lihtsalt faili nimega `Bitcoin.conf` ja avades selle seejärel tekstiredaktoris, et teha oma muudatused.



Parameetrid, mis on määratletud failis `Bitcoin.conf`, saab tühistada 2 kihi poolt:




- `settings.json` (kirjutatud dünaamiliselt Interface graafika või mõne RPC poolt),
- ja käsurea kaudu muudetud valikud.



Pange tähele, et iga muudatus failis `Bitcoin.conf` vajab jõustumiseks sõlme taaskäivitamist.



### Formaat ja struktuur



SW-664.conf'i vorming on seega väga lihtne: üks rida iga valiku kohta, kujul `option=value`. Ebavajalikud tühikud ja tühjad read jäetakse tähelepanuta ning koodikommentaarid algavad numbriga `#`.



Peaaegu kõiki boolseid valikuid saab keelata eesliitega "no". Näiteks `listen=0` ja `nolisten=1` on sõltuvalt versioonist samaväärsed.



Konfigureerimise segmenteerimiseks võrkude kaupa saate kasutada sektsioone: (testnet3), `[testnet4]`, `[bookmark]`, `[regtest]`. Alternatiivselt võite lisada valiku nimele eesliite `regtest.maxmempool=100`.



### Mida Bitcoin.conf saab ja mida ei saa teha



Nagu eespool selgitatud, ei ole konsensusreeglid ilmselt konfigureeritavad failis "Bitcoin.conf", kuna see võib tekitada Hard Fork. Seevastu paljud muud aspektid on konfigureeritavad. On 3 kasulikku klassi, mida tuleb meeles pidada:




- Puhtalt kohalikud parameetrid. Need mõjutavad ainult teie sõlme: vahemälu suurus (`dbcache`), pruned režiim (`prune`), valikulised indeksid... Need mõjutavad teie masina jõudlust, kuid mitte võrku.
- Relee ja Mempool poliitika. Need otsustavad, mida teie sõlmpunkt aktsepteerib, säilitab ja edastab enne kinnitamist: minimaalne tasu lävi (`minrelaytxfee`), Mempool suurus ja säilitamise aeg (`maxmempool`, `mempoolexpiry`), tehingu asendamine (RBF)... Need reeglid ei ole konsensuse osa, nii et kahel erineval sõlmel võivad olla erinevad reeglid ja need on siiski täielikult ühilduvad. Teisest küljest mõjutavad need parameetrid Bitcoin võrku (nagu on selgitatud esimeses osas, eelkõige perkolatsiooniteooria abil).
- Võrguühendus. Need valikud määravad, kuidas teie võrgusõlm leiab eakaaslasi, kuulab, läbib NAT-i, kasutab Tor'i või proxy'd või piirab oma ribalaiust. Need kujundavad teie topoloogiat, kuid ei muuda tehingute edastamist.



Selle eraldatuse mõistmine on väga oluline: kui tehing ei vasta konsensuse reeglitele, lükkab teie sõlmpunkt selle igal juhul tagasi. Kuid rangem kohalik poliitika võib keelduda konsensuse mõttes kehtiva tehingu edastamisest.



### Võrk ja topoloogia



Kõigepealt on oluline selgelt eristada 2 tüüpi ühendusi, mida Bitcoin sõlmpunkt võib omada:




- Väljaminevad ühendused, mis on algatatud meie sõlme poolt teisele sõlmpunktile;



![Image](assets/fr/106.webp)





- Sissetulevad ühendused, mis on algatatud teise sõlme poolt meie juurde.



![Image](assets/fr/107.webp)



Need kaks ühendustüüpi on täiesti võimelised vahetama samu andmeid mõlemas suunas; küsimus ei ole voolu suuna piiramises, vaid ainult ühenduse algatajal esinevas erinevuses. Meie sõlme seisukohalt peetakse väljaminevaid ühendusi üldiselt turvalisemaks, sest me algatame need ja valime täpselt, millise sõlmega ühendust luua, mistõttu on ebatõenäoline, et ühendus on pahatahtlik. Vaikimisi säilitab Bitcoin core 10 väljaminevat ühendust (8 "*full-relay*" + 2 "*block-relay-only*").



Full node lisab võrgule lisaväärtust, võttes vastu sissetulevaid ühendusi. Parameeter `listen=1` lubab kuulata kõnealuse võrgu vaikimisi port 8333, mis võimaldab neid sissetulevaid ühendusi vastu võtta clearnetis. Selleks, et see toimiks, peab see port olema avatud ka teie marsruuteris. Kui see ei ole, jätkab teie sõlme töö ainult väljaminevate ühendustega, mis ei mõjuta teie isiklikku Bitcoin kasutamist. Valik, kas lubada sissetulevaid ühendusi, on teie otsustada; "parimat valikut" ei ole olemas



Kui te eelistate oma ruuteril mitte avada porti, kuid võtate siiski vastu sissetulevaid ühendusi, võite aktiveerida parameetri `listenonion=1`. Sellega saavutatakse sama tulemus, kuid ainult läbi Tor-võrgu, mitte clearneti.



Võrgustiku tasandil on meil ka:




- `addnode`: lisab lisaks tavapärasele avastamisele (võib määrata mitu korda) ka sõbraliku partneri, kellega ühendust võtta.
- connect`: piirab rangelt ühendusi Address-ga (võib määrata mitu korda). Core ei ühendu ühegi teise sõlme juurde.
- `seednode`: kasutatakse ainult book-Address täitmisel, kui sõlme ühendatakse, siis katkestatakse ühendus.
- `maxconnections`: määrab sissetulevate + väljaminevate ühenduste üldise ülemmäära. Vaikimisi on selle parameetri väärtuseks 125, mis tähendab, et teie sõlmpunkt ei võta kunagi vastu rohkem kui 125 ühendust.
- maxuploadtarget`: piirab üleslaadimisi, et piirata ribalaiust libiseva 24-tunnise akna jooksul. See ülempiir ei ohusta oluliste hiljutiste Elements levikut.
- `onlynet`: piirab väljaminevaid ühendusi ainult valitud võrkudega (`ipv4`, `ipv6`, `onion`, `i2p`, `cjdns`). Näiteks kui soovite, et teie sõlme ühendataks Bitcoin võrguga ainult Tori kaudu, saate lubada parameetrit `onlynet=onion` ja keelata sissetulevad ühendused (või lubada ühendusi ainult ka Tori kaudu).
- `dnsseed`: lubab või keelab _DNS-seemnete_ taotlemise, kui teie kohalik Address-pool on väike (vaikimisi: `1`, kui `-connect` või `-maxconnections=0`).
- `forcednsseed`: sunnib _DNS-seemneid_ taotlema käivitamisel, isegi kui teil on aadressid juba olemas (vaikimisi: `0`).
- `Fixedseeds`: (kõvakooditud Address nimekiri), kui _DNS-seemned_ ei õnnestu või on keelatud (vaikimisi: `1`).
- `dns`: Lubab DNS resolutsioonid üldiselt (nt `-addnode`/`-seednode`/`-connect` jaoks).



Vaikimisi suhtleb teie sõlme üle clearneti, Tori ja I2P. See tähendab, et partnerid, kellega ta clearnetis ühendust võtab, näevad teie avalikku IP-aadressi Address ja teie ISP suudab tõenäoliselt tuvastada, et te kasutate Bitcoin sõlme (kuigi P2P Transport V2 muudab ISP-l pealtkuulamise keerulisemaks). See ei ole tingimata probleem, kuid kui soovite vältida selle teabe lekkimist, võite ühendada oma sõlme ainult Tor-võrgu kaudu.



Et olla täielikult Tor-võimeline, peate sundima Bitcoin core kasutama ainult seda võrku ja looma varjatud teenuse sissetulevate ühenduste jaoks (kui soovite neid lubada). Bitcoin.conf'ile tuleb lisada see konfiguratsioon:




- `onlynet=onion`,
- `proxy=127.0.0.1:9050`,
- `listenonion=1`,
- `torcontrol=127.0.0.1:9051`,
- `proxyrandomize=1`,
- `listen=1`,
- bind=127.0.0.0.1`,
- `upnp=0`,
- `natpmp=0`.



Kõik teie P2P ühendused lähevad läbi Tori. Teie sõlme saadab sissetulevate ühenduste jaoks Address `.onion`, seega ei ole vaja avada ühtegi porti ruuteril. Teie ISP näeb ainult Tor-liiklust ja teie võrgupartnerid ei tea teie tegelikku avalikku IP-d Address.



Et vältida DNS-eraldamist, võite lisada oma konfiguratsiooni `dnsseed=0` ja `dns=0`. Seejärel tuleb teil käsitsi anda `.onion` võrdsuspunktid `seednode=` või `addnode=` kaudu, sest muidu on uute sõlmede leidmine keeruline.



Kui olete algaja, soovitan teil ilmselt esialgu kõik need võrguseadistused rahule jätta. Sageli piisab vaikimisi konfiguratsioonist.



### Mempool ja releepoliitika



#### Põhiparameetrid



Siin on põhiparameetrid, mida saate muuta oma "Bitcoin.conf"-is seoses Mempool haldamisega ja kinnitamata tehingute edastamisega:





- `maxmempool=<n>`: Piirab kohaliku Mempool maksimaalse suuruse `<n>` megabaidini (vaikimisi: `300`). Kui limiit on saavutatud, tõstab teie sõlme dünaamiliselt oma tegelikku tasulävendit ja seab prioriteediks kõige vähem kasumlikud tehingud (tasumäärade, mitte absoluutväärtuse alusel), et jääda alla limiidi. Selle seadistuse võite jätta vaikimisi. Selle suurendamine võib olla kasulik, kui olete Mining üksi või kui soovite saada täpsemat ülevaadet Mempool ülekoormusest ja parandada tasu hindamist. Seevastu selle vähendamine säästab RAM-i ja vähemal määral ka muid süsteemiressursse.





- `mempoolexpiry=<n>`: Kinnitamata tehingute maksimaalne säilitusaeg Mempool-s (tundides, vaikimisi: `336`). Pärast seda aega eemaldatakse tehingud, isegi kui ruumi on veel saadaval.





- `persistmempool=1`: Salvestab hetkeseisu Mempool-st seisundi ajal ja laadib selle taaskäivitamisel uuesti (vaikimisi: `1`). See kiirendab taastumist pärast taaskäivitamist, vältides vajadust õppida olek uuesti võrgu kaudu.





- `maxorphantx=<n>`: Maksimaalne säilitatavate orbtehingute arv (sõltuvad sisendid UTXOdest, mida UTXO komplektis veel ei ole nähtud, vaikimisi: `100`). Selle künnise ületamisel kustutatakse vanimad tehingud, et vältida vahemälu kontrollimatut kasvu.





- blocksonly=1`: Keelab eakaaslastelt saadud kinnitamata tehingute vastuvõtmise ja uuesti edastamise (kui ei ole antud erilisi õigusi). Sõlm laeb nüüd ainult plokke üles ja reklaamib neid. Lokaalselt loodud tehinguid saab endiselt edastada (et kasutada oma sõlme koos Wallet tarkvaraga). See vähendab oluliselt ribalaiuse ja RAM-i nõudeid, kuigi selle hinnaga väheneb relee kasulikkus ja Mempool täielik tundmatus.





- `minrelaytxfee=<n>`: Minimaalne tasu määr (BTC/kvB), millest madalamal ei aktsepteerita tehinguid sõlme Mempool-s ja mida ei edastata eakaaslastele (vaikimisi: `0.00001` = 1 sat/vB). Mida suurem on see väärtus, seda agressiivsemalt filtreerib teie sõlmpunkt madala maksumusega tehinguid.





- `mempoolfullrbf=1`: RBF tehingute vastuvõtmine isegi ilma selgesõnalise RBF signalisatsioonita asendatud tehingus. Selle "*full-RBF*" poliitikaga võib kõrgemat tasu pakkuv tehing asendada teise Mempool tehingu, kui muud asendustingimused on täidetud.



Tuletame meelde, et RBF on tehingumehhanism, mis võimaldab saatjal asendada tehing kõrgema tasuga tehinguga, et kiirendada kinnitamist. Kui liiga madala tasuga tehing jääb blokeerituks, saab saatja kasutada *Replace-by-fee*, et suurendada tasu ja seada oma asendustehing mempools ja kaevurite juures prioriteediks.



#### Täiustatud ja spetsiifilised seaded



Siin on Mempool ja releepoliitika täiustatud seaded. Kui te olete algaja, ei peaks te neid seadeid muutma:





- datacarrier=1`: Lubab edastada ja (kui Mining sõlme kaudu) kaasata tehinguid, mis ei sisalda finantsandmeid OP_RETURN väljundi kaudu (vaikimisi: `1`). Selle parameetri deaktiveerimine vähendab veidi mittefinantsandmete rämpsposti kasutamispinda, kuid vähendab ühilduvust teatavate kasutusviiside puhul. Kõigil juhtudel tuleb aktsepteerida kaevandatud `OP_RETURN`.





- `datacarrierize=<n>`: Maksimaalne suurus (baitides) `OP_RETURN`, mida sõlmpunkt edastab (vaikimisi: `83`). Selle väärtuse alandamine piirab `OP_RETURN` kaudu edastatavat kasuliku koormuse hulka. Pange tähele, et see piirang eemaldatakse vaikimisi Bitcoin core tulevases versioonis.





- `bytespersigop=<n>`: Parameeter, mis konverteerib allkirja tehingud samaväärseteks baitideks releelimiidi hindamiseks (vaikimisi: `20`). See mõjutab `sigops`-rikaste tehingute aktsepteerimist vastavalt kohalikele reeglitele.





- `permitbaremultisig=1`: Lubab *barhe-Multisig* P2MS-tehingute edastamist (vaikimisi: `1`). See on vanim skripti mall mitme allkirja tingimuste loomiseks UTXO-l (leiutas 2011. aastal Gavin Andresen).





- `whitelistrelay=1`: Automaatselt annab releeloa valges nimekirjas olevatele sissetulevatele eakaaslastele (vaikimisi: `1`). Nende peeride tehinguid aktsepteerib relee isegi siis, kui teie sõlmpunkt ei ole üldises releerežiimis.





- `whitelistforcerelay=1`: Annab "*forcerelay*"-õiguse vaikimisi õigustega (vaikimisi: `0`) valges nimekirjas olevatele eakaaslastele. Seejärel edastab sõlme nende tehinguid isegi siis, kui nad on juba Mempool-s olemas, vältides seega koondamisvastaseid mehhanisme.





- `whitebind=<[permissions@]addr>` / `whitelist=<[permissions@]CIDR>`: Seob Interface või Address vahemiku ja määrab vastavatele eakaaslastele peensusteni täpsed õigused: `relay`, `forcerelay`, `Mempool` (Mempool sisupäring), `noban`, `download`, `addr`, `bloomfilter`. See võib olla kasulik privilegeeritud kohtlemise võimaldamiseks usaldusväärsetele partneritele (nagu väravad, LANid ja siseteenused).





- peerbloomfilters=1`: (vaikimisi: `0`): Võimaldab Bloom-filtrite (BIP37) toetuse, et pakkuda filtreeritud plokke/tehinguid õhukestele klientidele (vaikimisi: `0`). Hoiatus: see suurendab teie ressursside koormust.





- peerblockfilters=1`: (vaikimisi: `0`).





- `blockreconstructionextratxn=<n>`: Täiendav tehingute arv, mis jäetakse mällu kompaktsete plokkide taastamiseks (vaikimisi: `100`). Parandab rekonstruktsioonide edukust kompaktsete sünkroniseerimiste ajal väikese mälu arvelt.



Meeldetuletuseks, et kõik need relee-eeskirjad ei mõjuta kehtivas plokis sisalduvate tehingute kehtivust. Nende eesmärk on kohandada teie panust releesse, kaitsta teie ressursse ja muuta teie sõlme prognoositavaks piiratud keskkondades, kuid mitte kunagi ei võimalda teil keelduda konsensusreeglitest kinni pidavatest plokkidest.



### Rahakotid



Samuti saate kohandada oma rahakottide haldamise viisi failis `Bitcoin.conf`. Kui te ei kasuta Wallet otse Core'is, vaid pigem välist haldustarkvara, näiteks Sparrow või Liana, siis on need parameetrid väheolulised:





- addresstype=<legacy|P2SH-SegWit|bech32|bech32m>`: Määratleb Wallet-ga genereeritud aadresside vastuvõtu formaadi.





- `changetype=<legacy|P2SH-SegWit|bech32|bech32m>`: Force Exchange Address formaat (ülejäänud sisend ühe makse kohta).





- `Wallet=<path>`: Laadib käivitamisel olemasoleva Wallet (võib korrata mitme rahakoti laadimiseks).





- `walletdir=<dir>`: Rahakotte sisaldav kataloog (vaikimisi: `<datadir>/wallets`, kui see on olemas, muidu `<datadir>`). See võib olla kasulik, kui soovite salvestada rahakotte spetsiaalses või krüpteeritud mahus.





- `walletbroadcast=1`: (vaikimisi: `1`). Määra `0`, kui soovid hallata edastamist mõne teise kanali kaudu.





- `walletrbf=1`: Lubab RBF opt-in, et anda RBF signaal kõikidele tehingutele (vaikimisi: `1`). Võimaldab blokeeritud tehingu korral hiljem tasusid suurendada.





- `txconfirmtarget=<n>`: Tehingu kinnitamise sihtmärk (plokkide arvuna, vaikimisi: `6`). Wallet seab automaatselt tasu, et tehing kinnitatakse selle arvu plokkide jooksul.





- `paytxfee=<amt>`: Wallet tehingute suhtes kohaldatav fikseeritud tasu määr (BTC/kvB). Vältida üldiselt: kasutage kohanduvat hindamist `txconfirmtarget` kaudu.





- fallbackfee=<amt>`: Tagasipöördumismäär (BTC/kvB), mida kasutatakse juhul, kui hindaja andmed saavad otsa (vaikimisi: `0.00`). Selle seadmine 0-ks keelab tagasilanguse täielikult.





- `mintxfee=<amt>`: Wallet minimaalne künnis (BTC/kvB) tehingute loomiseks (vaikimisi: `0.00001`). Wallet keeldub tehingu loomisest alla selle künnise.





- `maxtxfee=<amt>`: Wallet tehingu kogutasude absoluutne ülempiir (vaikimisi: `0.10` BTC). Kaitseb ebaharilikult kõrgete tasude eest, mis hävitaksid tarbetult bitcoine.





- `avoidpartialspends=1`: Valib UTXO-d Address klastrite kaupa, et vältida osalisi kulutusi.





- `spendzeroconfchange=1`: UTXO Exchange kinnitamata UTXO Exchange võib kasutada uuesti uue tehingu kirjetena (vaikimisi: `1`).





- `consolidatefeerate=<amt>`: Maksimaalne määr (BTC/kvB), mille ületamisel Wallet väldib rohkem sisendite lisamist kui konsolideerimiseks vajalik. See võimaldab odavat konsolideerimist madalate hindadega ja vähendab kulusid, kui kulud on suured.





- `maxapsfee=<n>`: Täiendavate tasude eelarve (BTC, absoluutväärtus), mida Wallet on nõus maksma, et aktiveerida valik "*Vältida osalisi kulutusi*".





- `discardfee=<amt>`: Määr (BTC/kvB), mis näitab teie tolerantsust Exchange ära visata, lisades selle tasule. Väljundid, mis selle määra juures läheksid maksma rohkem kui kolmandiku nende väärtusest, visatakse ära.





- `keypool=<n>`: Eelnevalt genereeritud Address kogumi suurus (vaikimisi: `1000`). Liiga väikesed väärtused suurendavad mittetäieliku taastamise ohtu.





- `disablewallet=1`: Käivitab Bitcoin core ilma Wallet allsüsteemita ja keelab sellega seotud RPC-d. Vähendab ründepinda ja jalajälge, kui sõlme kasutatakse ainult valideerimiseks/vabastamiseks.



### Säilitamine, indekseerimine ja jõudlus



Konfiguratsioonifail võimaldab teil ka seadme parameetreid reguleerida. See võib olla eriti oluline, kui teil on piiratud ressursid või, vastupidi, suur hulk vaba võimsust:





- `datadir=<dir>`: Määrab Bitcoin core peamise andmekataloogi.





- `blocksdir=<dir>`: Lahutab plokkide failide (`blocks/blk*.dat` ja `blocks/rev*.dat`) asukoha `datadir`st. See võib olla kasulik näiteks plokkide arhiivi paigutamisel teisele andmekandjale, säilitades samal ajal staatuse baasi (`chainstate/`) kiiremal andmekandjal.





- `dbcache=<n>`: Eraldab `<n>` MiB andmebaasi vahemälu (*LevelDB*), mida kasutavad plokkindeks ja `chainstate` (vaikimisi: `450`). Mida suurem on väärtus, seda kiirem on IBD ja praegune valideerimine, kuid selle arvelt tarbitakse rohkem RAM-mälu.





- `prune=<n>`: Võimaldab plokkfailide kärpimise ja seab kettaruumi eesmärgi MiB-s (vaikimisi: `0` = keelatud; `1` = käsitsi kärpimine RPC kaudu; `>=550` = automaatne kärpimine alla eesmärgi). Ei ühildu `txindex=1`ga. Sõlm jääb täielikult valideerivaks sõlmpunktiks, kuid ei saa enam pakkuda vana ajalugu. See valik on eriti kasulik, kui teie kettaruum on piiratud, näiteks kui te paigaldate sõlme oma koduarvutisse.





- txindex=1`: Ehitab ja säilitab kinnitatud tehingute globaalset indeksit. Oluline teatavate päringute jaoks (`getrawtransaction`, mitte-Wallet) ja uurimiseks, kuid suurendab oluliselt kettamahte. Ei ühildu pruned režiimiga.





- `assumevalid=<hex>`: Märgib plokki, mis loetakse kehtivaks, võimaldades skripti kontrollimise vahele jätta selle esivanemate puhul (seadke `0`, et kontrollida kõike). Lisateavet vt eelmisest peatükist.





- `reindex=1`: Rekonstrueerib plokkide indeksid ja oleku (`chainstate`) kettal olevatest `blk*.dat` failidest. Taastab ka valikulised aktiivsed indeksid. See on aeganõudev operatsioon, mida saab kasutada vigastatud andmebaasi parandamiseks või raskete indeksite puhtaks aktiveerimiseks/deaktiveerimiseks.





- `reindex-chainstate=1`: Taastab ainult `chainstate` praeguse plokiindeksi. Eelistatud, kui plokkfailid on terved.





- `blockfilterindex=<tüüp>`: Säilitab kompaktsete plokkfiltrite (nt `basic`) indekseid, mida kasutavad õhukesed kliendid (BIP157/158) ja mõned RPC-d. Vaikimisi välja lülitatud (`0`). Kulutab täiendavalt kettaruumi ja indekseerimisaega.





- `coinstatsindex=1`: Hoiab UTXO komplekti statistika indeksit, mida käitab kõne `gettxoutsetinfo`. Kasulik auditite ja meetrikate jaoks, välistades vajaduse kulukate ümberarvutuste tegemiseks. Vaikimisi välja lülitatud.





- `loadblock=<file>`: Impordib plokid käivitamisel välisest `blk*.dat` failist. Kasutatakse ajaloo eellaadimiseks offline allikast (kohalik koopia, väline meedia), et kiirendada initsialiseerimist.





- `par=<n>`: Määrab skripti kontrollimise niitide arvu (vahemikus `-10` kuni `15`, `0` = auto, `<0` = jätab selle arvu südamikke vabaks). Võimaldab reguleerida protsessori paralleelsust valideerimise ajal. Automaatrežiim on enamikul juhtudel sobiv.





- `debuglogfile=<file>`: Määratleb `debug.log` logi asukoha.





- `shrinkdebugfile=1`: (vaikimisi: `1`, kui `-debug` ei ole aktiivne).





- `settings=<file>`: Dünaamiliste seadete faili `settings.json` tee.



### RPC juurdepääs ja tööohutus



Lõpuks võimaldab fail `Bitcoin.conf` konfigureerida ka teie sõlme juurdepääsuparameetrid. Olge nende seadistustega ettevaatlik, eriti kui te alles alustate: vältige nende muutmist ilma mõju põhjaliku mõistmiseta, sest see võib tekitada haavatavusi.





- `server=1`: Aktiveerib JSON-RPC serveri. Oluline, kui kasutate `bitcoind`d `bitcoin-cli` või kolmanda osapoole rakenduse kaudu. Lülita välja (`0`) puhtalt valideeriva sõlme puhul, mis ei avalda ühtegi API-d või kasutab juba Electrumi serverit.





- `rpcbind=<addr>[:port]`: RPC server kuulab Address/port. Vaikimisi toimub kuulamine ainult lokaalselt (`127.0.0.0.1` ja `::1`). Seda parameetrit ignoreeritakse, kui `rpcallowip` ei ole samuti määratletud. Kasutage seda Interface selgesõnaliselt piiramiseks.





- `rpcport=<port>`: RPC port (vaikimisi: `8332` Mainnet, `18332` Testnet, `38332` bookmark, `18443` regtest).





- `rpcallowip=<ip|cidr>`: Lubab RPC kliente antud IP-lt või alamvõrgust (võib korrata). Kasutage koos `rpcbind`iga, et avada API ainult usaldusväärsele segmendile (LAN/VPN).





- `rpcauth=<USERNAME>:<SALT>$<Hash>`: Soovitatav RPC autentimismeetod (hashed password). Võimaldab mitu sisestust ja väldib saladuse salvestamist selge tekstina.





- `rpccookiefile=<path>`: Autentimisküpsise tee (vaikimisi: `.cookie` fail kataloogis `datadir/`). Seda kasutatakse sama kasutaja lokaalseks juurdepääsuks ilma püsivate paroolide haldamiseta. Näiteks saate seda kasutada Liana Wallet ühendamiseks oma Bitcoin core-ga samas masinas.





- `rpccuser=<user>` / `rpcpassword=<pw>`: Klassikaline RPC autentimine lihtkirjas parooliga. Vältige selle kasutamist `rpcauth` või küpsise kasuks.





- `rpcthreads=<n>`: Niitide arv RPC kõnede teenindamiseks (vaikimisi: `4`). Suurendage seda, kui teil on suured kõnepiigid monitooringu/välise tööriista poolel.





- `rpcwhitelist=<USERNAME>:<rpc1>,<rpc2>,...`: Lubatud API-de valgeloend. Vähendab ründepinda, piirates ligipääsetavaid meetodeid.





- `rpcwhitelistdefault=1|0`: Kui see on lubatud ja kasutatakse valget nimekirja, siis keeldutakse nimekirjadesse kandmata kõnedest. See võib ka sundida vaikimisi tühja komplekti (kõned ei ole lubatud), kui midagi ei ole selgesõnaliselt loetletud.





- `rest=1`: Lubage avalik REST API (vaikimisi välja lülitatud). Avaldada ainult usaldusväärses võrgus (sama ettevaatlikkus nagu JSON-RPC puhul).





- `conf=<file>`: Määratleb ainult käsureal ainult lugemiseks mõeldud konfiguratsioonifaili. Kasulik täitmisprofiili külmutamiseks (muutumatu) ops'i poolel.





- `includeconf=<file>`: Laeb täiendava konfiguratsioonifaili (tee suhteline `datadir/`). Võimaldab rollide eraldamist: ühine baas + tundlik kohalik ülekoormus.





- `daemon=1` / `daemonwait=1`: Käivitab `bitcoind` taustal ja ootab koos `daemonwait`iga enne üleandmist initsialiseerimise lõppu. See hõlbustab integreerimist supervisoritega (systemd, runit).





- `pid=<file>`: PID-faili asukoht.





- `sandbox=<log-ja-abort|abort>`: Võimaldab eksperimentaalse syscalls sandboxing: ainult oodatud syscalls on lubatud.





- `startupnotify=<cmd>` / `shutdownnotify=<cmd>`: Käivitab käsu käivitamisel või väljalülitamisel.





- `alertnotify=<cmd>`: Käivitab teate saamisel käsu.





- `blocknotify=<cmd>`: Täidab käsu iga uue ploki puhul.





- `debug=<kategooria>|1` / `debugexclude=<kategooria>`: Lubab/keelab üksikasjalikud logikategooriad (nt `net`, `Mempool`, `RPC`, `valideerimine`...).





- `logips=1`: Logib IP-aadressid.





- `logsourcelocations=1` / `logthreadnames=1` / `logtimestamps=1`: Lisab logidele vastavalt allikate asukohad, niitide nimed ja täpsed ajatemplid.





- `printtoconsole=1`: Saadab jälgede/veadekirjeldused konsooli (*stdout*).





- `help-debug=1`: Kuvab debugimisvõimaluse abi ja lõpetab töö.





- `uacomment=<cmt>`: Lisab kommentaari User-Agent P2P.



Oleme nüüdseks lõpetanud enamiku konfiguratsiooniparameetrite loetlemise. See "Bitcoin.conf" fail moodustab seega teie sõlme tegeliku armatuurlaua: selles määratakse kindlaks võrgu konfiguratsioon, Mempool haldamine, ketta- ja mälukasutus, indekseerimine ja üldine haldamine. Kui soovite selle faili kohta rohkem teada saada ja luua oma vajadustele kohandatud faili, siis soovitan kasutada [Jameson Loppi generaatorit](https://jlopp.github.io/Bitcoin-core-config-generator/).



Oleme jõudnud lõpule selle BTC 202 kursusega, mis on võimaldanud teil mitte ainult mõista sõlmede toimimise ja nende süsteemi koostoimimise põhitõdesid, vaid ka luua oma sõlmed. Nüüd oled sa suveräänne Bitcoiner, kellel on oma enda hallatav Wallet, mis edastab oma tehinguid oma sõlme kaudu. Palju õnne!



Nüüd saate liikuda edasi kursuse lõpuosasse, kus saate hinnata BTC 202, seejärel saate diplomi, et kontrollida, kas olete omandanud kõik käsitletud mõisted.



Nüüd on teil mitu võimalust. Järgmine loogiline samm on luua oma Lightning-sõlm, mis võimaldab teil off-chain tehingute puhul olla täiesti sõltumatu. See on tulevase kursuse teema, mis avaldatakse 2025. aasta sügisel Plan ₿ Network kohta.



Vahepeal kutsun teid üles avastama BTC 204 koolitust, mis võimaldab teil mõista ja omandada privaatsuse kaitse põhimõtteid Bitcoin kasutamisel:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


# Viimane osa


<partId>679169f5-b990-47e1-9a00-45098ba8096b</partId>





## Arvamused ja hinnangud


<chapterId>c18f672d-1074-427e-9505-eecd7ae43e71</chapterId>




<isCourseReview>true</isCourseReview>


## Lõpueksam


<chapterId>a4c97701-996c-4cc5-81fa-37d2dc4ee856</chapterId>




<isCourseExam>true</isCourseExam>


## Kokkuvõte


<chapterId>28c5cf1f-7b9c-4b68-8b8f-eee109629764</chapterId>




<isCourseConclusion>true</isCourseConclusion>