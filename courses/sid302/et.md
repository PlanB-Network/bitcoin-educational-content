---
name: Liquid Bootcamp Essentials
goal: Saate põhjaliku ülevaate Liquid Network ja Elements projektist ning saate teada, kuidas rakendada täiustatud lahendusi konfidentsiaalsete tehingute, sümboolika ja detsentraliseeritud võrguarhitektuuri valdkonnas.
objectives: 

  - Mõista Liquid arhitektuuri põhialuseid ja selle seost Bitcoin-ga.
  - Õppige Liquid sõlmede konfigureerimist ja käitamist Elements tarkvara abil.
  - Uurida konfidentsiaalsete tehingute ja varade emiteerimise kasutamist Liquid Network-s.
  - Mõista Liquid ärilisi ja tehnilisi aspekte kapitaliturgude rakenduste jaoks.

---

# Liquid võrgustiku tutvustamine


Alustage õppereisi, mille eesmärk on anda põhjalik ülevaade Liquid Network ja Elements projektist. See alglaager ühendab teooria ja praktika, et õpetada teile tehnilisi, arhitektuurilisi ja ärilisi põhialuseid, mis on vajalikud Liquid võimaluste rakendamiseks ja kasutamiseks. Alates konfidentsiaalsetest tehingutest kuni ökosüsteemi kujundamiseni on see kursus ideaalne neile, kes soovivad laiendada oma teadmisi Bitcoin ökosüsteemi täiustatud vahenditest.


Kursusel käsitletakse tööstuse ekspertide ettekannetega selliseid teemasid nagu Liquid arhitektuur, märgistusrakendused, Elements tehnilised kontseptsioonid ja uuenduslikud kasutusviisid, nagu Breez SDK. Kursus on mõeldud nii, et see oleks kättesaadav algajatele ja edasijõudnutele, kuid pakub väärtust ka kogenud arendajatele, kes soovivad omandada Liquid kui platvormi oma projektide optimeerimiseks.

+++

# Sissejuhatus


<partId>9f8a83d5-27e0-4e6d-af12-6cd6eb667291</partId>


## Kursuse ülevaade


<chapterId>3192ee7d-255b-4c4f-ba18-e08c5ab98577</chapterId>


Tere tulemast Liquid Bootcamp'ile, mis on põhjalik koolitus, mille eesmärk on anda teile teadmised ja oskused Liquid Network ja Elements projekti tõhusaks kasutamiseks. Sellel kursusel tutvustatakse põhjalikult Liquid eriomadusi, sealhulgas Confidential Transactions, varade väljastamist ja selle föderatiivset võrguarhitektuuri, ning tutvustatakse Elements, Liquid aluseks oleva tarkvara, põhikontseptsioone.


Kogu alglaagri jooksul uurite Liquid Network praktilisi rakendusi, alates sõlmede loomisest ja käitamisest kuni Bitcoin kapitaliturgude ja tokeniseerimise kasutamise mõistmiseni. Tööstuse ekspertide ettekannetega saate ülevaate ka sellistest edasijõudnud teemadest nagu HTLC-d, Breez SDK ja Blockstream AMP projekt.


Algselt viidi see algselt läbi isikliku üritusena, järgides struktureeritud ajakava (nagu on näidatud pildil), mis oli mõeldud live-sessioonideks. Selle kursuse kohandamise jaoks on sisu siiski ümber korraldatud, et see sobiks paremini veebivormingusse ja hõlbustaks õpilaste arusaamist. Uus järjekord tagab loogilise ülemineku aluskontseptsioonidest edasijõudnute ja tehniliste teemade juurde, mis maksimeerib õppimiskogemust.


See reis on üles ehitatud nii, et see sobiks erineva tasemega osalejatele, pakkudes teoreetiliste teadmiste ja praktiliste kogemuste segu. Selle laagri lõpuks on teil kindel arusaam Liquid arhitektuurist, selle integreerimisest Bitcoin-ga ning sellest, kuidas kasutada selle uuenduslikke funktsioone finantslahenduste loomiseks ja optimeerimiseks.


Sukeldu Liquid külgahela maailma ja vabasta selle täielik potentsiaal kohe!

# Põhitõed


<partId>6dd86449-c0f7-4e51-9252-5f135cf019df</partId>


## Liquid arhitektuur


<chapterId>4bca9c70-d54d-4e9a-b2db-17c3a6fa655b</chapterId>


:::video id=ff6899d2-b47f-4c3d-983d-3bd66d2be59d:::

### Liquid Network arhitektuur ja konsensuse mudel


Liquid Network on Elements koodibaasil põhinev föderatiivne külgahel, mis on loodud Bitcoin võimaluste laiendamiseks, tuginedes samas selle põhiturvalisusele. Erinevalt Bitcoin-st Proof-of-Work töötab Liquid föderaalse konsensuse mudelil. Võrku hooldab ülemaailmselt hajutatud liikmete rühm, sealhulgas börsid, kauplemiskeskused ja infrastruktuuri pakkujad. Selle liikmeskonna hulgast valitakse viisteist "funktsionääri", kes tegutsevad plokkide allkirjastajatena.


Need funktsionäärid toodavad plokke deterministlikult, kusjuures iga minut genereeritakse uus plokk. Selline täpne ajastus on vastuolus Bitcoin tõenäosusliku kümne-minutilise intervalliga. Selleks, et plokk oleks kehtiv, peab see olema allkirjastatud vähemalt 11 funktsionäärilt 15st (kaks kolmandikku pluss üks künnis). See mehhanism annab Liquid-le "kahe ploki lõplikkuse", mis tähendab, et kui tehing on saanud kaks kinnitust (umbes kaks minutit), on matemaatiliselt võimatu ahelat ümber korraldada. Selline kiirus ja kindlus on kriitilise tähtsusega arbitraaži, automatiseeritud kauplemise ja kiire börsidevahelise arvelduse jaoks.


Föderatsioon on dünaamiline. Dünaamilise föderatsiooni (Dynafed) protokolli abil saab võrk vahetada funktsionääre või uuendada parameetreid, ilma et oleks vaja kõva fork. See võimaldab süsteemil areneda ja vahetada riistvara või liikmeid sujuvalt, säilitades samas pideva toimimise.


### Confidential Transactions ja varade haldamine


Liquid eripära on Confidential Transactions (CT) ja mitme vara originaalne tugi. Bitcoin põhiahelas on kõik tehingu üksikasjad - saatja, saaja ja summa - avalikud. Liquid-s kasutatakse krüptograafilisi kohustusi, et varjata vara liik ja summa avalikust pearaamatust, võimaldades samal ajal võrgustikul kontrollida, et tehing on kehtiv (st et inflatsiooni ei ole toimunud). Konkreetseid väärtusi saavad näha ainult need osalejad, kellel on pimendavad võtmed, pakkudes suurt positsiooni liigutavate asutuste jaoks olulist ärilist privaatsust.


Liquid käsitleb kõiki varasid kui plokiahela "põliselanikke". See hõlmab Liquid Bitcoin (LBTC), stabiilseid münte nagu USDT ja turvatähti. Vara väljastamine ei nõua keerulisi nutilepinguid; see on protokolli põhifunktsioon.


#### Reguleeritud varad ja AMP

Vastavust nõudvate varade, näiteks väärtpaberitoodete puhul kasutab Liquid Blockstream Asset Management Platform (AMP). Sellega võetakse kasutusele lubadega kiht, kus tehingud nõuavad teist allkirja autoriseerimisserverilt. See võimaldab emitentidel jõustada reegleid - näiteks Whitelisting või KYC nõuded - granulaarsel tasandil, ühendades plokiahela tõhususe traditsioonilise finantseerimise regulatiivse kontrolliga.


### Kahepoolne peg ja turvainfrastruktuur


Ühendus Liquid ja Bitcoin vahel säilib kahesuunalise viigi kaudu. Sisselülitamiseks saadab kasutaja Bitcoin mainchain loodud aadressile. Need vahendid on lukustatud 102 kinnituse ajaks (ligikaudu 17 tundi), et kõrvaldada ümberkorraldusriskid. Pärast kinnitamist vermitakse samaväärne summa LBTC-d Liquid külgahelas.


"Peg-out" protsess võimaldab kasutajatel vahetada LBTC-d Bitcoin vastu. Selleks on vaja LBTC põletamist ja föderatsiooni krüptograafilist luba. Varguse vältimiseks kontrollitakse peg-out'i rangelt föderatsiooni liikmete valduses olevate Peg-out Authorization Keys (PAK) abil. Lisaks saab vahendeid vahetada koheselt kolmandate osapoolte, näiteks SideSwapi teenusepakkujate kaudu, mis võimaldab kiirema likviidsuse saavutamiseks vältida arveldusviivitust.


#### Riistvaralised turvamoodulid (HSM)

Turvalisust tagatakse rangelt riistvara abil. Funktsionäärid ei hoia privaatseid võtmeid tavalistes serverites, vaid kasutavad riistvaralisi turvamooduleid (HSM). Need seadmed on host-serveri loogikast eraldatud ja programmeeritud rangete reeglitega. Näiteks keeldub HSM ploki allkirjastamisest, kui selle kõrgus ei ole suurem kui eelmise ploki kõrgus, vältides seega ajaloo ümberkirjutamist. Selline "vastase" turvamudel eeldab, et vastuvõttev server võib olla ohustatud, tagades, et võtmed jäävad turvaliseks isegi siis, kui füüsilist asukohta rikutakse.


## Elements põhialused


<chapterId>1e9cfbed-108e-4067-afb9-4cf950cb43d3</chapterId>


:::video id=5652dcb2-4303-484c-8be5-d98063b39c1c:::

### Elements: Liquid alus


Elements on avatud lähtekoodiga plokiahela platvorm, mis on tuletatud Bitcoin Core koodibaasist. See laiendab Bitcoin funktsionaalsust, võimaldades kõrvalahelatest sõltumatuid plokiahelaid, mis võivad varasid Bitcoin-sse ja Bitcoin-st üle kanda. Kui Bitcoin Core toetab Bitcoin võrku, siis Elements on Liquid Network ja muude kohandatud kõrvalahelate tarkvaramootor.


Seos on lihtne: Liquid on Elements külgahela konkreetne "eksemplar", mis on konfigureeritud tootmiskasutuseks koos föderaalse konsensusmudeliga. Bitcoin-ga tuttavatele arendajatele on Elements intuitiivne, kuna see säilitab sama RPC (Remote Procedure Call) liidese ja käsurea struktuuri (`elements-cli`, `elements-d`, `elements-qt`). Peamine erinevus seisneb konfiguratsioonis: `chain=liquidv1` ühendab sõlme peamise Liquid võrguga, samas kui `chain=elementsregtest` loob kohaliku regressioonitestimise keskkonna, kus arendajad saavad generate plokke koheselt ja ilma väliste sõltuvusteta testida.


#### Varade väljastamine

Elements silmapaistev omadus on emakeelne varade väljastamine. Erinevalt Ethereumist, kus märgid on keerulised arukad lepingud, on Elements varad esimese klassi kodanikud, mis luuakse lihtsa RPC käsu (issueasset) abil.


- Unikaalsed identifikaatorid:** Iga vara saab unikaalse 64-kohalise kuuekohalise ID.
- Reissuance Tokens:** Emitendid võivad valikuliselt luua reissuance tokenid, mis annavad omanikule õiguse hiljem rohkem varasid vermida (kasulik stabiilseid münte või väärtpaberitähiseid).
- Vararegister:** Kuna heksatunnused ei ole inimesele loetavad, siis Blockstream Asset Registry kaardistab need tunnused nimedeks ja tikriteks (nt "USDT"), sarnaselt varade DNS-ile.


### Privaatsus Confidential Transactions kaudu


Elements tegeleb ühe avaliku plokiahela peamise piiranguga, milleks on ärilise privaatsuse puudumine. Bitcoin-s on iga tehingu summa maailmale nähtav. Elements võtab kasutusele **Confidential Transactions (CT)**, mis krüptograafiliselt pimestab summa ja vara liigi, võimaldades siiski võrgul kontrollida tehingu kehtivust.


See saavutatakse **Pederseni kohustuste** ja **Range Proofs** abil.


- Pederseni kulukohustused** asendavad nähtava summa krüptograafilise kulukohustusega. Homomorfse krüpteerimise tõttu saavad valideerijad kontrollida, et *Input Commitments = Output Commitments + Fees*, ilma et nad näeksid tegelikke väärtusi.
- Vahemiku tõestused** takistavad kasutajat raha õhust välja tekitamast (nt negatiivseid numbreid kasutades), tõestades matemaatiliselt, et varjatud väärtus on positiivne täisarv kehtivas vahemikus.


Välise vaatleja jaoks näitab konfidentsiaalne tehing kehtivaid sisendeid ja väljundeid, kuid varjab *mida* saadetakse ja *kuidas*. Ainult saatja ja vastuvõtja (kellel on pimendavad võtmed) saavad näha selge tekstiga andmeid.


### Arendus ja RPC töökorraldus


Elements-sõlmega suhtlemine toimub peamiselt selle JSON-RPC-liidese kaudu. See võimaldab Pythonis, JavaScriptis või Go's kirjutatud rakendustel plokiahelaga suhelda.



- Seadistamine:** Arendaja alustab tavaliselt režiimis "regtest". See võimaldab koheselt genereerida plokke (`generateblock`), et kinnitada tehinguid kohe, vältides reaalvõrgu 1-minutilist plokkide aega.
- Käsklused:** Saadaval on standardsed Bitcoin käsud, nagu `getblockchaininfo`, ning Elements-spetsiifilised käsud, nagu `dumpblindingkey` (CT-de auditeerimiseks) või `pegin` (BTC liigutamiseks sidechaini).
- Pseudonimed:** Mitme sõlme haldamiseks (nt "saatja" ja "vastuvõtja" testimiseks) kasutavad arendajad sageli shell-pseudonimesid nagu `e1-cli` ja `e2-cli`, mis viitavad erinevatele andmehoidlatele, simuleerides ühe masina peer-to-peer-võrku.


See arhitektuur võimaldab arendajatel luua keerukaid finantsrakendusi - näiteks väärtpaberiplatvorme või eramaksete väravaid - kasutades Bitcoin ökosüsteemi töökindlaid ja tuttavaid tööriistu.


## Bitcoin kihtide ühendamine


<chapterId>3ff2df4a-8995-4d5e-9b8a-cd114880e666</chapterId>


:::video id=31368c02-b979-44d7-b217-ceed96c7ca5c:::

### Cross-Layer infrastruktuur ja HTLCd


Bitcoin ökosüsteem on kujunenud mitmekihiliseks arhitektuuriks, kus Mainchain pakub arveldusi, Lightning pakub kiirust ja Liquid võimaldab täiustatud varafunktsioone. Väärtuse liikumine nende kihtide vahel ilma tsentraliseeritud vahendajateta nõuab usaldusteta krüptograafilist primitiivi: Hash Time Locked Contract (HTLC).


HTLC loob tingimusliku maksekanali, mis ühendab sõltumatuid süsteeme aatomiliselt. See toimib kahe peamise piirangu kaudu: **hash lock** ja **time lock**.


- Hash Lock:** Raha saab kulutada kohe, kui vastuvõtja paljastab salajase "eelpildi", mis vastab konkreetsele krüptograafilisele hashile.
- Ajalukk:** Kui vastuvõtja ei avalda saladust määratud aja jooksul (ploki kõrgus), saab algne saatja raha tagasi nõuda.


Selline kahesuunaline struktuur tagab ohutuse. Ristkihilise vahetuse korral kasutatakse mõlemas võrgus sama hash-lukku. Kui vastuvõtja avaldab saladuse, et nõuda raha ühel kihil (nt Liquid), muutub see saladus nähtavaks saatjale, kes saab seda kasutada vastastikuseks raha nõudmiseks teisel kihil (nt Lightning). See krüptograafiline side tagab, et vahetus toimub kas mõlema poole jaoks edukalt või ebaõnnestub, kõrvaldades riski, et üks pool kaotab raha, samal ajal kui teine saab seda juurde.


### Taproot ja MuSig2 uuendamine


Varasemad HTLC-d (SegWit v0) toimisid hästi, kuid kannatasid privaatsuse ja tõhususe puuduste all. Nad nõudsid kogu skriptiloogika on-chain avaldamist, mistõttu vahetustehingud olid plokiahela analüütikutele kergesti tuvastatavad ja nende andmete suuruse tõttu kallimad. Taproot (SegWit v1) ja MuSig2-protokolli kasutuselevõtt on selle arhitektuuri revolutsiooniliselt muutnud.


Taproot võimaldab **Key Aggregation** MuSig2 kaudu. Selle asemel, et paljastada keerulist skripti mitme avaliku võtmega, võimaldab MuSig2 vahetuses osalejatel ühendada oma võtmed üheks koondatud avalikuks võtmeks.


- Koostööpõhine "võtmevahetus":** Kui mõlemad osapooled nõustuvad vahetusega ("õnnelik tee"), allkirjastavad nad tehingu ühiselt. Võrgustiku jaoks näeb see välja samasugune nagu tavaline, ühe allkirjaga makse. See tarbib minimaalselt plokiruumi ja ei avalda mingit teavet vahetustingimuste kohta.
- Vastase "skripti tee":** Kui üks osapool ei reageeri või on pahatahtlik, siis alles siis paljastatakse aluseks olev skript (mis sisaldab hash/aja lukustusi). See on korraldatud Merkle-puuna, mis võimaldab ausal osapoolel avalikustada ainult konkreetset haru, mis on vajalik raha tagasisaamiseks, hoides ülejäänud lepinguloogika varjatud.


### Praktiline rakendamine: Liquid-Välgivahetused


Praktikas võimaldavad need protokollid sujuvat vahetust Bitcoin kihtide vahel. Tüüpiline Liquid-lt välklambi vahetamine algab sellega, et klient taotleb teenusepakkujalt vahetust. Klient esitab Lightning-arve ja teenusepakkuja lukustab Liquid Bitcoin (L-BTC) samaväärse Taproot-võimelise HTLC aadressi.


Aatomisus saavutatakse makse arveldamisel. L-BTC nõudmiseks peab teenusepakkuja omama eelpilti. Ta saab selle eelkinnituse ainult siis, kui ta maksab edukalt kliendi Lightning-arve. Hetkel, mil Lightning-makse on lõpule viidud, paljastatakse eelkujutis, mis võimaldab teenusepakkujal avada Liquid vahendid.


#### Wallet Abstraheerimine ja UTXO haldamine

Lõppkasutajate jaoks on see keerukus täiesti abstraktselt. Kaasaegsed rahakotid, nagu Aqua, tegelevad võtme genereerimise, arve loomise ja allkirjastamise protsessidega taustal. Kasutaja lihtsalt "maksab" Lightning-arve, kasutades oma Liquid saldot. Kulisside taga haldab teenus UTXO konsolideerimist, pühkides perioodiliselt väikesed, nõudmata või tagastamata väljundid, et säilitada wallet tõhusus ja minimeerida tasu mõju suure liiklusega perioodidel.


## Liquid Network ülevaade


<chapterId>1968db03-2364-46c0-9670-9e9844289ca1</chapterId>


:::video id=0bac0a62-90f2-41da-ac7c-330c0604bc61:::

### Liquid Network Arhitektuur ja konsensus


Liquid Network töötab ühendatud külgahelana, mis põhineb **Elements** koodibaasil. Kui Elements - fork Bitcoin Core - pakub tarkvaralist alust, siis Liquid on tootmisvõrgu rakendamine. Erinevalt Bitcoin Proof-of-Work-st, mis tugineb konkureerivale mining-le, kasutab Liquid **Federated Consensus** mudelit.


Võrgustikku hooldavad viisteist ülemaailmselt jaotatud "funktsionääri" Need üksused haldavad spetsiaalseid servereid, mis täidavad kahte olulist rolli:

1.  **Blokkide tootmine:** Funktsionäärid loovad plokke kordamööda deterministliku ringrežiimi järgi, genereerides uue ploki täpselt iga minut.

2.  **Bloki allkirjastamine:** Selleks, et plokk oleks kehtiv, peab see olema allkirjastatud vähemalt 11 funktsionääri poolt 15-st.


See 11-15 künnis tagab, et võrk suudab taluda kuni nelja sõlme rikkeid ilma peatumata. Selle kompromissi peamine eelis on **deterministlik lõplikkus**. Kui Bitcoin tegeleb tõenäosustega, siis Liquid saavutab lahenduskindluse kahe ploki (umbes kahe minuti) järel. Kui ploki peal on üks kinnitus, ei saa ahelat ümber korraldada, mis muudab selle väga tõhusaks arbitraažiks ja kiireks arveldamiseks.


### Confidential Transactions ja kohalikud varad


Liquid iseloomulikuks tunnuseks on **Confidential Transactions (CT)** vaikimisi kasutamine. Bitcoin mainchain puhul on saatja, vastuvõtja ja summa avalikud. Liquid parandab seda, varjates krüptograafiliselt summa ja vara liigi, jättes samal ajal saatja ja vastuvõtja aadressid kontrollimiseks nähtavaks.


Selleks, et tagada, et kasutaja ei saa raha printida (nt negatiivseid summasid saates), kasutab Liquid **Pedersen Commitments** ja **Range Proofs**. Need krüptograafilised primitiivid võimaldavad võrgul kontrollida, et *Sisendid = Väljundid + Tasud* ja et kõik väärtused on positiivsed täisarvud, ilma et konkreetseid numbreid avalikule pearaamatule avaldataks. Dekrüpteeritud andmeid saavad vaadata ainult need osalejad, kellel on pimendavad võtmed.


#### Varade väljastamine

Liquid käsitleb kõiki varasid "emakeelena" Olenemata sellest, kas tegemist on Liquid Bitcoin (L-BTC), stabiilse mündi nagu USDT või väärtpaberiga token, on neil kõigil sama arhitektuur. Vara emiteerimiseks ei ole vaja ühtegi arukat lepingut - ainult lihtne RPC kõne.


- Reguleerimata varad:** Võib anda välja ilma loata igaüks.
- Reguleeritud varad:** Kasutades Blockstream Asset Management Platformi (AMP), saavad emitendid jõustada vastavusreegleid (nagu KYC/AML), nõudes enne vara liigutamist teist allkirja autoriseerimisserverilt.


### Kahepoolne pulk ja dünaamiline föderatsioon


Bitcoin ja Liquid vaheline sild on **Kaksikühendus**. See võimaldab kasutajatel viia BTC-d külgahelasse (Peg-in) ja tagasi mainchain-sse (Peg-out).


**Pig-in protsess:**

See on loata. Kasutaja saadab BTC föderatsiooni kontrollitavale aadressile. Bitcoin plokiahela ümberkorralduste eest kaitsmiseks peavad need vahendid ootama **102 kinnitust** (umbes 17 tundi), enne kui samaväärne L-BTC prahitakse sidechainis.


**Peg-out protsess:**

Bitcoin juurde tagasipöördumiseks põletatakse L-BTC. Bitcoin varude varguse vältimiseks ei toimu väljaviimine siiski täielikult automaatselt. Selleks on vaja luba liikmelt, kellel on **Peg-Out Authorization Key (PAK)**. Bitcoin vahendid ise on turvatud 11-15 mitme allkirjaga wallet-ga, mille võtmeid hoitakse riistvara turvamoodulites (HSM), mis on funktsionääride põhiserveritest õhku ühendatud.


**Dünaamiline föderatsioon (Dynafed):**

Pikaealisuse tagamiseks kasutab Liquid Dynafed protokolli, mis võimaldab võrgul vahetada funktsionääre või uuendada parameetreid, ilma et fork oleks kõva. Kui funktsionäär tuleb välja vahetada, edastab võrk üleminekutehingu. Pärast kahenädalast kattumisperioodi võtab uus konfiguratsioon üle, mis võimaldab föderatsioonil sujuvalt areneda, säilitades samal ajal pideva tööaja.


## Ökosüsteem ja kapitaliturud


<chapterId>5f4c0e50-b435-4b6c-b8b7-c55cc1a35431</chapterId>


:::video id=07e0b82f-2d60-4eb3-9b5d-2ccb7ad06e8a:::

### Liquid Network: Äristrateegia ja ökosüsteem


Liquid on midagi enamat kui tehniline kõrvalahel; see on äritegevusele keskendunud infrastruktuurikiht, mis on loodud kapitaliturgude keeruliste nõuete täitmiseks, mida Bitcoin mainchain ei suuda tõhusalt toetada. Kui Lightning Network on optimeeritud suure sagedusega ja väikese väärtusega maksete jaoks, siis Liquid on suunatud suure väärtusega ülekannetele, varade emiteerimisele ja börsidevahelistele arveldustele.


Ökosüsteemi juhib **Liquid Federation**, mis on ~73 ettevõtte, sealhulgas börside, kauplemiskohtade ja infrastruktuuri pakkujate konsortsium. See koostöömudel peegeldab traditsioonilisi finantskliirimiskeskusi, kuid toimib suurema läbipaistvuse ja oluliselt lühendatud arveldusajaga (2 minutit võrreldes T+2 päevaga).


### Reaalmaailma varade (RWA) tokeniseerimine (Tokenization of Real-World Assets)


Liquid põhiline äritegevus on "Tokeniseerimine" - reaalse väärtuse (aktsiad, võlakirjad, mining lepingud) kujutamine digitaalsete märkidena plokiahelas. See pakub kolm peamist eelist:

1.  **24/7 globaalsed turud:** Pangaaegade ja geograafiliste piirangute kaotamine.

2.  **Kasutustõhusus:** Ühise, muutumatu pearaamatu abil kõrvaldatakse kooskõlastamisvead.

3.  **Atomic Settlement:** Vähendab vastaspoole riski, tagades, et tarne toimub samaaegselt maksega.


#### Reguleeritud varad ja AMP

Enamik institutsionaalseid varasid ei saa õiguslike nõuete tõttu loata kaubelda. **Asset Management Platform (AMP)** on tehniline standard, millega neid eeskirju jõustatakse.


- Valge nimekiri:** Emitendid võivad piirata hoidmist ja kauplemist KYC-töölehtedega kontrollitud aadressidega.
- Multisig kontroll:** Nõuetele vastavuse tagamise meetmeid (näiteks varastatud vahendite külmutamine või kaotatud žetoonide uuesti väljastamine) hallatakse mitme allkirjaga volituse abil, mis tagab, et ükski töötaja ei saa tegutseda ühepoolselt.


See infrastruktuur on täna kasutusel. Platvormid, nagu **Stalker**, pakuvad Euroopas läbivalt tokeniseerimisteenuseid, samas kui **Sideswap** tegutseb detsentraliseeritud börsina ja mittekaitstavana wallet, võimaldades varadega, nagu **Blockstream Mining Note (BMN)** ja tokeniseeritud MicroStrategy aktsiatega (CMSTR), peer-to-peer kauplemist.


### Reaalse maailma edu: Mayfelli juhtumiuuring


Liquid kasulikkust tõestab kõige veenvamalt **Mayfell** Mehhikos. Turul, kus traditsiooniline rahastamine tugineb pabervekslitele, mis on vastuvõtlikud kadumisele, pettusele ja aeglasele töötlemisele, viis Mayfell kogu infrastruktuuri üle Liquid-le.



- Mastaabid:** Üle 25 000 väljastatud võlakirja, mille väärtus on **1,5 miljardit dollarit+**.
- Privaatsus:** Kasutades Liquid Confidential Transactions, on laenusummad nähtavad ainult laenuandjale ja laenuvõtjale, säilitades ärilise privaatsuse, võimaldades samas audiitoritel kontrollida pearaamatu terviklikkust.
- Mõju:** Ühendades pangavälised laenuandjad globaalsete kapitaliturgudega plokiahela kaudu, vähendas Mayfell kulusid ja laiendas Mehhiko VKEde juurdepääsu krediidile, näidates, et Liquid väärtuspakkumine ulatub kaugemale spekulatiivsest kauplemisest.


### Strateegiline positsioneerimine võrreldes teiste kettidega


Liquid konkureerib tokeniseerimisplatvormide (Ethereum, Solana jne) tihedas konkurentsis, kuid tal on selged strateegilised eelised:


- Regulatiivne selgus:** Liquid kasutab Bitcoin (L-BTC) oma emakeelena. See ei ole eelnevalt kaevandatud token või ICO, vältides "registreerimata väärtpaberi" riske, mis vaevavad teisi L1 plokiahelaid.
- Stabiilsus:** Erinevalt Ethereumi kontomudelist, kus ebaõnnestunud tehingud põletavad endiselt gaasitasusid, on Liquidi UTXO mudel deterministlik ja usaldusväärne kriitiliste finantsandmete jaoks.
- Privaatsus:** Enamiku finantsasutuste jaoks on vaikimisi konfidentsiaalsus nõue, mida Liquid pakub algselt, kuid mida avalike kettide on raske rakendada ilma keeruliste lisanditeta.


Arendajatele pakub see ökosüsteem selge võimaluse: luua vahendid (armatuurlauad, rahakotid, vastavusintegratsioonid), mis ühendavad traditsioonilise rahanduse ja Bitcoin turvalise arvelduskihi.


## Blockstream AMP


<chapterId>4f21a0a7-0dc0-44cf-8a3a-d9e2f8a3f05f</chapterId>


:::video id=f00822b4-dc1a-46ff-adfc-ff7c97a0024d:::

### Blockstream AMP: Lubatud varade kontroll Liquid-l


Blockstream AMP (Asset Management Platform) toimib Liquid Network kriitilise infrastruktuurikihina, mis on mõeldud spetsiaalselt reguleeritud digitaalsete väärtpaberite ja stabiilse mündi emitentide jaoks. Kuigi Liquid pakub lubadeta baaskihti koos emakeelse vara emiteerimisega, vajavad reguleeritud üksused sageli ranget järelevalvet ja vastavusfunktsioone. AMP täidab selle lünga, kehtestades konkreetsete varade üle lubadega kontrollkihi, ohverdamata Liquid Confidential Transactions privaatsuse eeliseid.


Platvormi põhiline väärtuspakkumine tugineb kahele peamisele võimalusele: terviklik emitendi nähtavus ja tehingu autoriseerimine. Erinevalt standardsetest Liquid varadest, mille summad ja liigid on blinded kõigile peale osalejate, võimaldavad AMP varad emitendil säilitada täielikult unblinded auditijälge. Selline läbipaistvus on oluline regulatiivse aruandluse ja siseauditite jaoks. Lisaks sellele tagab AMP range autoriseerimismudeli kaasallkirjastamise mehhanismi kaudu. Iga AMP varade ülekanne nõuab AMP-serveri allkirja. See võimaldab emitentidel jõustada keerulisi reegleid off-chain - näiteks kontode külmutamine, akrediteeritud investorite valges nimekirjas hoidmine või ülekandepiirangute kehtestamine -, tegutsedes sisuliselt tsentraliseeritud väravavalvurina detsentraliseeritud võrgus.


#### Operatiivsed kompromissid

Selline arhitektuur toob kaasa spetsiifilised kompromissid. Süsteem sõltub AMP-serveri kättesaadavusest; kui server tegutseb kaasallkirjastajana ja läheb offline, peatub varade likviidsus. Lisaks, kuigi kasutajate vaheline privaatsus säilib, peavad investorid leppima sellega, et emitent on nende varade suhtes täielikult nähtav. See mudel on ideaalne nõuetele vastavate väärtpaberimärkide jaoks, kuid ei sobi tsensuurikindlate krüptovaluutade jaoks.


### Arhitektuuri areng ja integratsiooniteed


AMP ökosüsteem on praegu üleminekul oma esimesest versioonist paindlikumale, koostalitlusvõimelisele "versioon 2" arhitektuurile. Varasem süsteem nõudis emitentidelt täielikult sünkroniseeritud Elements sõlmede haldamist ja sundis arendajaid tuginema suuresti monoliitsele Green SDK-le. Kuigi see oli funktsionaalne, tekitas see kõrgeid tehnilisi takistusi sisenemiseks ja piiras wallet valikuid.


Järgmise põlvkonna arhitektuur lihtsustab neid nõudeid põhimõtteliselt, viies keerukuse üle serverile. Selles uues mudelis tegeleb AMP-server tehingu koostamise, UTXO valiku ja tasude arvutamisega. Ta esitab emitendile osaliselt allkirjastatud Elements tehingu (PSET), mis nõuab lihtsalt allkirja. Selline "nutikas server, rumal wallet" lähenemisviis välistab emitentide vajaduse käivitada täielikud sõlmed ning võimaldab kasutada riistvaralisi rahakotte ja standardseid mitme allkirja seadistusi riigikassa haldamiseks.


Arendajate jaoks tähendab see areng liikumist ära patenteeritud SDKdest standardsete kirjelduste ja PSET töövoogude suunas. Rahakotid saavad nüüd autoriseerimisõiguste kehtestamiseks registreerida AMP-serveris mitme allkirjaga deskriptoreid. See ühtlustab AMP arenduse laiemate Bitcoin wallet standarditega, muutes integratsiooni kättesaadavaks igale rakendusele, mis suudab käsitleda PSBT/PSET-vorminguid. Täna arendajaid julgustatakse kasutama selliseid vahendeid nagu Liquid Wallet Kit (LWK), mis toetab neid moodsaid, kirjelduspõhiseid arhitektuure, tagades, et nende rakendused on uute AMP-standardite jaoks tulevikukindlad.


### Liquid Wallet ökosüsteem ja konfidentsiaalsus


Rakenduste loomine Liquid peal nõuab navigeerimist keerulisemas korpuses kui tavaline Bitcoin arendus, kuna see on seotud selliste funktsioonidega nagu natiivsed varad ja Confidential Transactions. Ökosüsteemi toetab mitmekihiline arhitektuur: madala taseme raamatukogud nagu `secp256k1-zkp` tegelevad krüptograafiliste primitiividega, samal ajal kui kõrgema taseme tööriistakomplektid haldavad wallet loogikat.


Varem pakkus Green arenduskomplekt (GDK) terviklikku, kuid jäika lahendust. Kaasaegne alternatiiv on Liquid Wallet Kit (LWK), mis pakub modulaarset lähenemist. LWK eraldab probleemid eraldi kastidesse, mis käsitlevad kirjeldusi, allkirjastamist ja riistvaralist suhtlust sõltumatult, andes arendajatele paindlikkuse, et luua kohandatud lahendusi ilma monoliitse raamatukogu koormuseta.


#### Confidential Transactions käitlemine

Kõige suurem väljakutse selles ökosüsteemis on pimeda elutsükli haldamine. Liquid-s krüpteeritakse tehingu väljundid Elliptic Curve Diffie-Hellmani (ECDH) võtmevahetuse abil. Saatja kasutab vastuvõtja blindingi avalikku võtit, et krüpteerida varade summad ja tüübid, luues vahemiktõendi, mis kontrollib tehingu kehtivust ilma väärtusi paljastamata.


Selleks, et wallet toimiks, peab ta selle protsessi edukalt ümber pöörama. Kui wallet tuvastab sissetuleva tehingu, püüab ta oma privaatse blokeerimisvõtme abil väljundit avada. Kui jagatud saladus langeb kokku, saab wallet väärtuse dekrüpteerida ja lisada selle kasutaja saldole. See protsess on arvutusmahukas ja nõuab täpseid pimendustegureid, et tagada tehingute matemaatiline tasakaal, mis on keerukas, kuid mille arendaja jaoks on selliste vahendite nagu LWK eesmärk abstraktselt ära võtta.


# Tehniline


<partId>53629f58-b9e0-4a10-8ab2-d51b047414f8</partId>

<chapterId>f1fdf2b0-4b6a-4ba7-812c-7586dcb36713</chapterId>


## Breez SDK - sõlmedeta


<chapterId>fb77442c-3d1e-427e-b2f5-16668ce4c643</chapterId>


:::video id=1a6289b5-fdae-4320-b5b1-41925150108c:::

### Breez Liquid SDK tutvustus


Breez Liquid SDK on avatud lähtekoodiga tööriistakomplekt, mis on loodud Liquid Network ja laiema Bitcoin ökosüsteemi vahelise lõhe ületamiseks. Selle peamine ülesanne on abstraheerida Lightning Network sõlmede haldamise ja aatomivahetuste keerukust, võimaldades arendajatel luua hõõrdumisvabasid finantsrakendusi.


Põhiloogika on ehitatud "mobiilne kõigepealt" filosoofia alusel ja kirjutatud Rust keeles, et tagada jõudlus ja turvalisus, kuid see kasutab UniFFI (Unified Foreign Function Interface), et pakkuda Kotlini, Swifti, Pythoni, C#, Dart ja Flutteri emakeelseid sidumisi. See tagab, et arendajad saavad Bitcoin funktsionaalsust integreerida oma eelistatud keskkonda ilma madala taseme krüptograafiliste operatsioonide haldamiseta.


**Toetavad tehingutüübid:**

SDK tegutseb Liquid "kodubaasiga" See paistab silma kolme konkreetse operatsiooni puhul:

1.  **Liquid-Liquid:** Otsene on-chain ülekanne.

2.  **Liquid-to-Lightning:** Lightning-arvete maksmine Liquid vahenditega.

3.  **Liquid-lt Bitcoin-le:** Vahetus otse Bitcoin mainchain-le.


*Märkus: SDK ei toeta otseseid Lightning-Lightning või Bitcoin-Bitcoin tehinguid. See on rangelt Liquid-keskne vahend.*


### Maksearhitektuurid: Submarine Swap'id


Liquid, Lightning ja Bitcoin koostalitlusvõime saavutamiseks ilma tsentraliseeritud hooldajateta kasutab Breez **Submarine Swaps**. Need on aatomioperatsioonid, mille puhul tehing kas viiakse edukalt lõpule mõlemas võrgus või ebaõnnestub mõlemas, tagades, et raha ei kao kunagi transiidi käigus.


#### Lightning Send (allveelaevade vahetus)

Kui kasutaja maksab Lightning-arve, edastab SDK Liquid Network-l "lukustustehingu". See paneb raha tegelikult hoiule. Vahetuse pakkuja (Boltz) tuvastab selle, maksab Lightning-arve ja kasutab seejärel makse-eelpilti (krüptograafilist kviitungit), et nõuda lukustatud Liquid vahendeid.


#### Lightning Receive (tagasipööratud allveelaevavahetus)

Välgu vastuvõtmine on vastupidine protsess. Kasutaja koostab arve ja vahetustehingute pakkuja lukustab vahendid Lightning Network-l. SDK jälgib seda protsessi WebSocketi kaudu. Kui lukustus on kinnitatud, viib SDK automaatselt läbi nõudmistehingu, et kanda samaväärsed vahendid kasutaja Liquid wallet.


#### Kettadevaheline Bitcoin

Liquid-lt Bitcoin-le edastamiseks kasutab arhitektuur "dual-swap" mehhanismi. Lukustustehingud toimuvad mõlemas ahelas samaaegselt. Saatja nõuab raha Bitcoin-lt, samas kui saaja nõuab raha Liquid-lt. See võimaldab usaldusteta sildamist ilma federated peg-ist väljaminekute või tsentraliseeritud vahetustehingute kasutamiseta.


### Arendaja Interface ja automatiseeritud juhtimine


Breez SDK lihtsustab arendajate tööd, koondades keerulised finantsvood standardiseeritud kolmeastmelisse protsessi: **Connect, Prepare ja Execute**.


1.  **Connect:** Initsialiseerib wallet, sünkroonib plokiahelaga, kasutades Liquid Wallet Kit (LWK), ja loob WebSocket-ühendused reaalajas jälgimiseks.

2.  **Prepare:** Enne vahendite sidumist arvutab ja tagastab see samm kõik seotud võrgutasud ja vahetuskulud, võimaldades kasutajaliidesel esitada kasutajale selge kogusumma.

3.  **Täitmine:** Selles etapis koostatakse tehing, edastatakse see ja algatatakse vahetus.


#### Automatiseeritud ohutusmehhanismid

Üks SDK kõige kriitilisemaid funktsioone on **automaatne tagasimaksete haldamine**. Võrgurikke või koostööst keeldumise korral võivad vahendid teoreetiliselt takerduda ajaliselt lukustatud lepingusse. SDK abstraheerib taastamisloogika täielikult. See jälgib iga vahetustehingu seisu; kui vahetus ebaõnnestub või aegub, koostab ja edastab SDK automaatselt tagasimaksetehingu, et tagastada raha kasutaja wallet-le.


Lisaks sellele tegeleb SDK **Metaandmete lahendamisega**. See ühendab off-chain vahetuse andmed (mida pakub Boltz vahetuse tegija) on-chain tehinguajalooga. See tagab, et kasutaja tehingulugu on inimloetav, näidates arve üksikasju ja maksekonteksti, mitte ainult toorseid heksadekaalseid tehinguhääli.


# Lõplik osa


<partId>7ec65e6b-6e63-41b6-92ea-6a13bc77c3ff</partId>


## Arvamused ja hinnangud


<chapterId>e5f6348c-e207-40ae-8fef-6a068a6bf741</chapterId>


<isCourseReview>true</isCourseReview>

## Lõpueksam


<chapterId>b13c4aa8-ced6-11f0-8515-afd3f381a001</chapterId>

<isCourseExam>true</isCourseExam>

## Kokkuvõte


<chapterId>e30a5587-d74b-4360-87fb-bbf3de1b0ba8</chapterId>

<isCourseConclusion>true</isCourseConclusion>