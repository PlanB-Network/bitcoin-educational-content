---
name: Coinjoin - Sparrow Wallet
description: Kuidas teostada coinjoin'i Sparrow Wallet'is?
---
![cover](assets/cover.webp)

***HOIATUS:** Pärast Samourai Wallet'i asutajate arreteerimist ja nende serverite konfiskeerimist 24. aprillil ei toimi Whirlpool tööriist enam, isegi mitte nende kasutajate jaoks, kes omavad oma Dojo't või kasutavad Sparrow Wallet'i. Siiski on võimalik, et see tööriist võidakse järgnevate nädalate jooksul taastada või käivitada erineval viisil. Lisaks jääb selle artikli teoreetiline osa asjakohaseks üldiste coinjoinide (mitte ainult Whirlpool) põhimõtete ja eesmärkide mõistmiseks, samuti Whirlpooli mudeli efektiivsuse mõistmiseks.*

_Jälgime selle juhtumi arenguid ning seotud tööriistade arenguid tähelepanelikult. Võite kindlad olla, et uuendame seda õpetust, kui saabub uut teavet._

_Seda õpetust pakutakse ainult hariduslikel ja informatiivsetel eesmärkidel. Me ei toeta ega julgusta nende tööriistade kasutamist kuritegelikel eesmärkidel. Iga kasutaja vastutab oma jurisdiktsiooni seadustega kooskõlas olemise eest._

---

Selles õpetuses saate teada, mis on coinjoin ja kuidas seda teostada kasutades Sparrow Wallet tarkvara ja Whirlpooli rakendust.

## Mis on coinjoin Bitcoinil?
**Coinjoin on tehnik, mis katkestab bitcoinide jälgitavuse blockchainis**. See põhineb koostööl põhineval tehingul, millel on spetsiifiline sama nimega struktuur: coinjoin tehing.

Coinjoinid suurendavad Bitcoin'i kasutajate privaatsust, muutes ketianalüüsi väliste vaatlejate jaoks keerulisemaks. Nende struktuur võimaldab ühendada mitme kasutaja mündid üheks tehinguks, hägustades seeläbi radu ja muutes sisend- ja väljundiaadresside vaheliste seoste kindlaksmääramise keeruliseks.

Coinjoini põhimõte põhineb koostööl: mitu kasutajat, kes soovivad oma bitcoine segada, panevad samasugused summad sama tehingu sisenditena. Need summad jaotatakse seejärel väljunditena võrdse väärtusega iga kasutaja vahel. Tehingu lõppedes muutub võimatuks seostada kindlat väljundit teadaoleva kasutajaga sisendis. Sisendite ja väljundite vahel puudub otsene seos, mis katkestab seose kasutajate ja nende UTXO vahel, samuti iga mündi ajaloo.
![coinjoin](assets/notext/1.webp)

Näide coinjoin tehingust (mitte minult): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

Selleks, et teostada coinjoin, tagades samal ajal, et iga kasutaja kontrollib oma vahendeid kogu aeg, algab protsess tehingu koostamisega koordinaatori poolt, kes seejärel edastab selle igale osalejale. Iga kasutaja allkirjastab tehingu pärast selle sobivuse kontrollimist. Kõik kogutud allkirjad integreeritakse lõpuks tehingusse. Kui kasutaja või koordinaator üritab vahendeid kõrvale juhtida, muutes coinjoin tehingu väljundeid, muutuvad allkirjad kehtetuks, mis viib tehingu tagasilükkamiseni sõlmede poolt.

Coinjoini on mitmeid rakendusi, nagu Whirlpool, JoinMarket või Wabisabi, mille eesmärk on hallata osalejate koordineerimist ja suurendada coinjoin tehingute efektiivsust.
Selles õpetuses keskendume **Whirlpool** implementatsioonile, mida pean kõige tõhusamaks lahenduseks Bitcoinil coinjoinide sooritamiseks. Kuigi see on saadaval mitmetes rahakottides, uurib see õpetus eksklusiivselt selle kasutamist Sparrow Wallet Desktop tarkvaraga.

## Miks teha CoinJoine Bitcoinil?

Üks esialgsetest probleemidest mis tahes peer-to-peer maksesüsteemiga on topeltkulutamine: kuidas vältida pahatahtlike isikute poolt samade rahaliste ühikute mitmekordset kulutamist ilma keskse autoriteedi poole pöördumata?

Satoshi Nakamoto pakkus sellele dilemmale lahenduse Bitcoin protokolli kaudu, mis on peer-to-peer elektrooniline maksesüsteem, mis toimib sõltumatult igasugusest kesksest autoriteedist. Oma valges raamatus rõhutab ta, et topeltkulutamise puudumise kinnitamise ainus viis on tagada kõigi tehingute nähtavus maksesüsteemis.

Selleks, et iga osaleja oleks tehingutest teadlik, peavad need olema avalikult avaldatud. Seega toetub Bitcoin läbipaistvale ja hajutatud infrastruktuurile, mis võimaldab igal sõlmeoperaatoril kontrollida kogu elektrooniliste allkirjade ahelate ja iga mündi ajalugu alates selle loomisest kaevandaja poolt.

Bitcoin'i plokiahela läbipaistev ja hajutatud olemus tähendab, et iga võrgu kasutaja saab jälgida ja analüüsida kõigi teiste osalejate tehinguid. Seetõttu on tehingutasandil anonüümsus võimatu. Siiski säilitatakse anonüümsus individuaalse identifitseerimise tasandil. Erinevalt traditsioonilisest pangasüsteemist, kus iga konto on seotud isikliku identiteediga, on Bitcoinil vahendid seotud krüptograafiliste võtmepaaridega, pakkudes seeläbi kasutajatele pseudonüümsust krüptograafiliste identifikaatorite taga.

Seega on Bitcoinil konfidentsiaalsus kompromiteeritud, kui välised vaatlejad suudavad seostada kindlad UTXOd tuvastatud kasutajatega. Kui see seos on loodud, muutub nende tehingute jälgimine ja nende bitcoinide ajaloo analüüsimine võimalikuks. Coinjoin on just nimelt tehnika, mis on välja töötatud UTXOde jälgitavuse katkestamiseks, pakkudes seeläbi Bitcoin kasutajatele teatud konfidentsiaalsuse kihti tehingutasandil.

## Kuidas Whirlpool töötab?

Whirlpool eristub teistest coinjoin meetoditest, kasutades "_ZeroLink_" tehinguid, mis tagavad, et sisendite ja väljundite vahel ei ole tehniliselt võimalik mingit seost luua. See täiuslik segamine saavutatakse struktuuriga, kus iga osaleja panustab sisendisse identse summa (v.a kaevandamistasud), genereerides seeläbi täiesti võrdsetes summade väljundid.

See piirav lähenemine sisenditele annab Whirlpool coinjoin tehingutele unikaalse omaduse: täieliku deterministlike seoste puudumise sisendite ja väljundite vahel. Teisisõnu, igal väljundil on võrdne tõenäosus olla omistatud ükskõik millisele osalejale, võrreldes kõigi teiste tehingu väljunditega.
Algselt oli iga Whirlpool coinjoini osalejate arv piiratud 5-ga, 2 uue tulijaga ja 3 segajaga (selgitame neid mõisteid edasi). Siiski, 2023. aastal täheldatud on-chain tehingutasude tõusu tõttu pidid Samourai meeskonnad oma mudelit ümber mõtlema, et parandada privaatsust samal ajal kulusid vähendades. Seega, arvestades tasude turuolukorda ja osalejate arvu, saab koordinaator nüüd korraldada coinjoine, mis hõlmavad 6, 7 või 8 osalejat. Neid täiustatud seansse nimetatakse "_Surge Cycles_". On oluline märkida, et sõltumata seadistusest on Whirlpool coinjoinides alati ainult 2 uut tulijat.

Seega iseloomustavad Whirlpooli tehinguid identne arv sisendeid ja väljundeid, mis võivad olla:
- 5 sisendit ja 5 väljundit;
![coinjoin](assets/notext/2.webp)
- 6 sisendit ja 6 väljundit;
![coinjoin](assets/notext/3.webp)
- 7 sisendit ja 7 väljundit;
![coinjoin](assets/notext/4.webp)
- 8 sisendit ja 8 väljundit. ![coinjoin](assets/notext/5.webp)
Mudel, mida Whirlpool pakub, põhineb seega väikestel coinjoin tehingutel. Erinevalt Wasabi'st ja JoinMarketist, kus anonüümsete osalejate hulga vastupidavus sõltub osalejate mahust ühes tsüklis, panustab Whirlpool mitme väikese suurusega tsükli aheldamisele.

Sel mudelil tasub kasutaja tasusid ainult oma esialgsel sisenemisel basseini, võimaldades neil osaleda paljudes remixides ilma lisatasudeta. Uued sisenejad kannavad remixijate kaevandamise tasusid.

Iga täiendava coinjoin'iga, milles münt osaleb koos oma minevikus kohatud eakaaslastega, kasvavad anonüümsete osalejate hulgad eksponentsiaalselt. Eesmärk on seega ära kasutada neid tasuta remixe, mis iga kordumisega aitavad tugevdada iga segatud mündiga seotud anonüümsete osalejate tihedust.

Whirlpool on loodud arvestades kahte olulist nõuet:
- Rakendamise ligipääsetavus mobiilseadmetes, arvestades, et Samourai Wallet on peamiselt nutitelefoni rakendus;
- Remiximistsüklite kiirus, et edendada anonüümsete osalejate hulga märkimisväärset suurenemist.

Need imperatiivid juhtisid Samourai Walleti arendajate valikuid Whirlpooli kujundamisel, sundides neid piirama osalejate arvu tsükli kohta. Liiga vähesed osalejad oleksid ohustanud coinjoin'i efektiivsust, drastiliselt vähendades iga tsükliga genereeritud anonüümsete osalejate hulka, samas kui liiga paljud osalejad oleksid tekitanud haldusprobleeme mobiilirakendustes ja takistanud tsüklite voolu.

**Lõppkokkuvõttes pole Whirlpoolis iga coinjoin'i kohta vaja suurt osalejate arvu, kuna anonüümsete osalejate hulgad luuakse mitme coinjoin-tsükli kuhjumise kaudu.**
[-> Uuri lähemalt Whirlpooli anonüümsete osalejate kohta.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)
### Coinjoin basseinid ja tasud
Selleks, et mitu tsüklit tõhusalt suurendaksid segatud müntide anonüümsete osalejate hulka, tuleb kehtestada teatud raamistik, et piirata kasutatavate UTXO-de koguseid. Whirlpool määratleb selleks erinevad basseinid.

Bassein esindab kasutajate gruppi, kes soovivad koos segada, ja kes nõustuvad UTXO-de kasutamise summa osas, et optimeerida coinjoin protsessi. Iga bassein määrab UTXO jaoks fikseeritud summa, millest kasutaja peab osalemiseks kinni pidama. Seega, et teostada coinjoine Whirlpoolis, peate valima basseini. Praegu saadaolevad basseinid on järgmised:
- 0,5 bitcoini;
- 0,05 bitcoini;
- 0,01 bitcoini;
- 0,001 bitcoini (= 100 000 satsi).

Liitudes oma bitcoinidega basseiniga, jagatakse need, et genereerida UTXO-d, mis on täiesti homogeensed basseini teiste osalejate omadega. Igal basseinil on maksimaalne piir; seega summade puhul, mis ületavad seda piiri, peate kas tegema kaks eraldi sisenemist samasse basseini või liikuma teise basseini, mille summa on suurem:

| Bassein (bitcoin) | Maksimaalne summa sisenemise kohta (bitcoin) |
|-------------------|----------------------------------------------|
| 0,5               | 35                                           |
| 0,05              | 3,5                                          |
| 0,01              | 0,7                                          |
| 0,001             | 0,025                                        |
Nagu varem mainitud, peetakse UTXO-d basseini kuuluvaks, kui see on valmis integreerimiseks coinjoin'i. Siiski ei tähenda see, et kasutaja kaotab selle valduse. **Läbi mitmesuguste segamistsüklite säilitate täieliku kontrolli oma võtmete ja seega ka oma bitcoinide üle.** See on see, mis eristab coinjoin tehnikat teistest tsentraliseeritud segamistehnikatest.
Coinjoin basseini sisenemiseks tuleb maksta teenustasud ning kaevandamistasud. Teenustasud on iga basseini jaoks fikseeritud ja on mõeldud Whirlpooli arendamise ja hooldusega tegelevate meeskondade kompenseerimiseks. Sparrow Wallet'i kasutajate jaoks edastatakse need tasud Samourai meeskondade poolt Sparrow arendajatele.

Whirlpooli kasutamise teenustasud tuleb maksta ühekordselt basseini sisenedes. Kui see samm on lõpetatud, on teil võimalus osaleda piiramatus arvus uuestisegamistes ilma lisatasudeta. Siin on praegused fikseeritud tasud iga basseini jaoks:

| Bassein (bitcoin) | Sisenemistasu (bitcoin) |
|-------------------|-------------------------|
| 0.5               | 0.0175                  |
| 0.05              | 0.00175                 |
| 0.01              | 0.0005 (50,000 sats)    |
| 0.001             | 0.00005 (5,000 sats)    |


Need tasud toimivad sisuliselt kui sissepääsupilet valitud basseini, olenemata summast, mille panete coinjoin'i. Seega, kas liitute 0.01 basseiniga täpselt 0.01 BTC-ga või sisestate 0.5 BTC, jäävad tasud absoluutväärtuses samaks.

Enne coinjoinidega jätkamist on kasutajal seega valik kahe strateegia vahel:
- Eelistada väiksemat basseini, et minimeerida teenustasusid, teades, et vastu saadakse mitu väikest UTXO-d;
- Või eelistada suuremat basseini, nõustudes maksma kõrgemaid tasusid, et lõpuks saada vähem, kuid suurema väärtusega UTXO-sid.

Üldiselt soovitatakse vältida mitme segatud UTXO ühendamist pärast coinjoin tsükleid, kuna see võib ohustada saavutatud konfidentsiaalsust, eriti Common-Input-Ownership Heuristic (CIOH) tõttu. Seetõttu võib olla mõistlik valida suurem bassein, isegi kui see tähendab rohkema maksmist, et vältida liiga paljude väikese väärtusega UTXO-de väljundit. Kasutaja peab kaaluma neid kompromisse, et valida eelistatud bassein.

Lisaks teenustasudele tuleb arvestada ka igale Bitcoin tehingule omaseid kaevandamistasusid. Whirlpooli kasutajana peate maksma kaevandamistasud ettevalmistustehingu (`Tx0`) jaoks, samuti esimese coinjoini eest. Kõik järgnevad uuestisegamised on tasuta, tänu Whirlpooli mudelile, mis toetub uute osalejate maksetele.

Tõepoolest, igas Whirlpooli coinjoinis on kahe sisendi puhul tegemist uute osalejatega. Ülejäänud sisendid pärinevad uuestisegajatelt. Selle tulemusena kaetakse kõigi tehingus osalejate kaevandamistasud nende kahe uue osaleja poolt, kes seejärel saavad samuti kasu tasuta uuestisegamistest:
![coinjoin](assets/en/6.webp)
Tänu sellele tasusüsteemile eristub Whirlpool tõeliselt teistest coinjoin teenustest, kuna UTXO-de anonüümsuskomplektid ei ole proportsionaalsed kasutaja poolt makstud hinnaga. Seega on võimalik saavutada märkimisväärselt kõrge anonüümsuse tase, makstes ainult basseini sisenemistasu ja kahe tehingu (Tx0 ja esialgne segamine) kaevandamistasud.
On oluline märkida, et kasutaja peab katma kaevandamistasud, et tõmmata oma UTXOd pärast mitme coinjoin'i lõpetamist basseinist välja, välja arvatud juhul, kui nad on valinud `mix to` valiku, mida me allpool olevas õpetuses arutame.
### Whirlpooli kasutatavad HD rahakoti kontod
Whirlpooli kaudu coinjoin'i sooritamiseks peab rahakott genereerima mitu erinevat kontot. Konto, HD (Hierarhiliselt Deterministliku) rahakoti kontekstis, kujutab endast jaotust, mis on täielikult isoleeritud teistest, see eraldatus toimub rahakoti hierarhia kolmandal sügavustasemel, st `xpub` tasemel.
Teoreetiliselt võib HD rahakott tuletada kuni `2^(32/2)` erinevat kontot. Algkonto, mida vaikimisi kasutatakse kõikides Bitcoin'i rahakottides, vastab indeksile `0'`.

Whirlpoolile kohandatud rahakottide, nagu Samourai või Sparrow, puhul kasutatakse coinjoin protsessi vajaduste rahuldamiseks 4 kontot:
- **Deposiidi** konto, mida tuvastab indeks `0'`;
- **Halb pank** (või doxxic change) konto, mida tuvastab indeks `2 147 483 644'`;
- **Premix** konto, mida tuvastab indeks `2 147 483 645'`;
- **Postmix** konto, mida tuvastab indeks `2 147 483 646'`.

Iga nendest kontodest täidab coinjoinis kindlat funktsiooni.

Kõik need kontod on seotud ühe seemnega, mis võimaldab kasutajal taastada juurdepääsu kõigile oma bitcoinidele, kasutades oma taastefraasi ja vajadusel oma paroolifraasi. Siiski on vajalik tarkvarale taastamistoimingu ajal erinevate kasutatud kontoindeksite täpsustamine.

Vaadelgem nüüd Whirlpooli coinjoini erinevaid etappe nendes kontodes.

### Coinjoinide erinevad etapid Whirlpoolis
**Etap 1: Tx0**
Iga Whirlpooli coinjoini lähtepunkt on **deposiidi** konto. See konto on see, mida automaatselt kasutate, kui loote uue Bitcoin'i rahakoti. Sellele kontole tuleb kanda bitcoinid, mida soovite segada.

`Tx0` esindab Whirlpooli segamisprotsessi esimest etappi. Selle eesmärk on ette valmistada ja võrdsustada UTXOd coinjoini jaoks, jagades need valitud basseini summale vastavateks ühikuteks, et tagada segamise homogeensus. Võrdsustatud UTXOd saadetakse seejärel **premix** kontole. Mis puutub erinevusse, mis ei saa basseini siseneda, siis see eraldatakse spetsiifilisele kontole: **halb pank** (või "doxxic change").

See algne tehing `Tx0` teenib ka segamiskoordinaatori teenustasude tasumist. Erinevalt järgnevatest etappidest ei ole see tehing koostööaldis; kasutaja peab seega kandma kõik kaevandamistasud:
![coinjoin](assets/en/7.webp)
Selles `Tx0` tehingu näites jagatakse meie **deposiidi** kontolt pärit sisend `372,000 sats` mitmeks väljaminevaks UTXOks, mis jaotuvad järgmiselt:
- Summa `5,000 sats` on mõeldud koordinaatorile teenustasude eest, vastates basseini sisenevale `100,000 sats`-ile;
- Kolm UTXOd on ette valmistatud segamiseks, suunatud meie **premix** kontole ja registreeritud koordinaatoriga. Need UTXOd on võrdsustatud `108,000 sats` igaüks, et katta nende tulevaste algsete segude kaevandamistasud;
- Ülejääk, mis ei saa basseini siseneda, kuna see on liiga väike, peetakse toksiliseks muutuseks. See saadetakse oma spetsiifilisse kontosse. Siin on see muutus `40,000 sats`;
- Lõpuks on `3,000 sats`, mis ei moodusta väljundit, vaid on kaevandamistasud, mis on vajalikud `Tx0` kinnitamiseks.

Näiteks siin on reaalne Tx0 Whirlpool (mis ei pärine minult): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

**2. samm: Toksilise Muutuse**
Ülejääk, mis ei suutnud basseini integreeruda, siin võrdne `40,000 sats`-iga, suunatakse **halva panga** kontole, mida nimetatakse ka "toksiliseks muutuseks", et tagada range eraldatus teistest UTXO-dest rahakotis.

See UTXO on kasutaja privaatsuse jaoks ohtlik, kuna see on alati seotud oma minevikuga ja seega võimalikult ka oma omaniku identiteediga, lisaks on see märgitud kuuluvaks kasutajale, kes on teostanud coinjoin'i.

Kui see UTXO ühendatakse segatud väljunditega, kaotavad viimased kõik privaatsuse, mis saavutati coinjoin-tsüklite jooksul, eriti CIOH (*Common-Input-Ownership-Heuristic*) tõttu. Kui see ühendatakse teiste toksiliste muutustega, riskib kasutaja privaatsuse kaotamisega, kuna see seob erinevad coinjoin-tsüklite sissekanded. Seega tuleb sellega ettevaatlikult ümber käia. Kuidas seda toksilist UTXO-d hallata, kirjeldatakse artikli viimases osas ja tulevased õpetused sukelduvad nendesse meetoditesse PlanB võrgustikus sügavamalt.

**3. samm: Esialgne Segamine**
Pärast `Tx0` lõpetamist saadetakse võrdsustatud UTXO-d meie rahakoti **premix** kontole, valmis olema tutvustatud nende esimesse coinjoin-tsüklisse, mida nimetatakse ka "esialgseks segamiseks". Kui, nagu meie näites, `Tx0` genereerib mitu segamiseks mõeldud UTXO-d, integreeritakse igaüks neist eraldi esialgsesse coinjoin'i.
Nende esialgsete segamiste lõppedes on **premix** konto tühi, samal ajal kui meie mündid, olles maksnud kaevandamistasud selle esimese coinjoin'i eest, on täpselt kohandatud valitud basseini määratud summaga. Meie näites on meie esialgsed UTXO-d `108 000 sats`-ist vähendatud täpselt `100 000 sats`-ini.
![coinjoin](assets/en/8.webp)
**4. samm: Ümbersegamised**
Pärast esialgset segamist kantakse UTXO-d **postmix** kontole. See konto kogub juba segatud UTXO-sid ja neid, mis ootavad ümbersegamist. Kui Whirlpooli klient on aktiivne, on **postmix** kontol asuvad UTXO-d automaatselt saadaval ümbersegamiseks ja valitakse juhuslikult osalema nendes uutes tsüklites.

Meenutuseks, ümbersegamised on seejärel 100% tasuta: lisateenustasusid ega kaevandamistasusid ei nõuta. UTXO-de hoidmine **postmix** kontol säilitab nende väärtuse muutumatuna ja samal ajal parandab nende anonüümsete komplektide taset. Seetõttu on oluline lasta neil müntidel osaleda mitmes coinjoin-tsüklis. See ei maksa teile midagi ja suurendab nende anonüümsuse taset.
Kui otsustate segatud UTXOsid kulutada, saate seda otse teha sellest **postmix** kontost. On soovitatav hoida segatud UTXOsid selles kontos, et saada kasu tasuta ümbersegamistest ja vältida nende lahkumist Whirlpooli ringlusest, mis võiks vähendada nende privaatsust.
Nagu me järgnevas õpetuses näeme, on olemas ka `mix to` valik, mis pakub võimalust saata automaatselt teie segatud mündid teise rahakotti, näiteks külma rahakotti, pärast määratletud arvu coinjoine.

Pärast teooria arutamist sukeldugem praktikasse õpetusega, kuidas kasutada Whirlpooli Sparrow Wallet lauaarvuti tarkvara kaudu!

## Õpetus: Coinjoin Whirlpool Sparrow Wallet'is
Whirlpooli kasutamiseks on mitmeid võimalusi. Esimene, mida teile tutvustada tahan, on Sparrow Wallet valik, avatud lähtekoodiga Bitcoin'i rahakoti haldustarkvara PC-le.
Sparrow kasutamise eeliseks on see, et alustamine on üsna lihtne, seadistamine kiire ja vajalik on ainult arvuti ja internetiühendus. Siiski on märkimisväärne puudus: coinjoinid toimuvad ainult siis, kui Sparrow on käivitatud ja ühendatud. See tähendab, et kui soovite oma bitcoine segada ja ümber segada 24/7, peate oma arvuti pidevalt sisse lülitatuna hoidma.

### Sparrow Wallet'i paigaldamine
Alustuseks vajate ilmselgelt Sparrow Wallet tarkvara. Saate selle otse alla laadida [ametlikult veebilehelt](https://sparrowwallet.com/download/) või [nende GitHubist](https://github.com/sparrowwallet/sparrow/releases).

Enne tarkvara paigaldamist on oluline kontrollida allalaaditud täitmisfaili allkirja ja terviklikkust. Kui soovite Sparrow tarkvara paigaldusprotsessi ja kontrollimise kohta rohkem üksikasju, soovitan teil lugeda seda teist õpetust: *[The Sparrow Wallet Guides](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607)*.

### Tarkvararahakoti loomine
Pärast tarkvara paigaldamist peate jätkama Bitcoin'i rahakoti loomisega. On oluline märkida, et coinjoinide kasutamiseks on hädavajalik kasutada tarkvararahakotti (nn "kuum rahakott"). Seega **ei ole võimalik teostada coinjoine rahakotiga, mis on turvatud riistvaralise rahakotiga**.

Kuigi see ei ole kohustuslik, kui plaanite segada märkimisväärseid summasid, on tungivalt soovitatav valida selle rahakoti jaoks tugev BIP39 paroolilause.

Uue rahakoti loomiseks avage Sparrow, seejärel klõpsake vahekaardil `File` ja `New Wallet`.

![sparrow](assets/notext/9.webp)

Valige sellele rahakotile nimi, näiteks: "Coinjoin Wallet". Klõpsake nupul `Create Wallet`.

![sparrow](assets/notext/10.webp)

Jätke vaikeseaded, seejärel klõpsake nupul `New or Imported Software Wallet`.

![sparrow](assets/notext/11.webp)

Kui jõuate rahakoti loomise aknasse, soovitan valida 12-sõnalise jada, kuna see on täiesti piisav. Valige `Generate New`, et genereerida uus taastefraas, ja klõpsake `Use Passphrase`, kui soovite lisada BIP39 paroolilause. On oluline teha oma taasteinfo füüsiline varukoopia, kas paberil või metalltoel, et tagada oma bitcoinide turvalisus.

![sparrow](assets/notext/12.webp)
Enne `Confirm Backup...` nupule klõpsamist veenduge oma taastefraasi varukoopia kehtivuses. Sparrow palub teil seejärel oma fraasi uuesti sisestada, et kontrollida, kas olete sellest teada võtnud. Kui see samm on lõpetatud, jätkake klõpsates `Create Keystore`.
![sparrow](assets/notext/13.webp)
Jätke soovitatud tuletustee vaikimisi seadistuseks ja vajutage `Import Keystore`. Minu näites erineb tuletustee veidi, kuna kasutan seda õpetust tehes Testneti. Teie jaoks peaks ilmuma järgmine tuletustee:
```plaintext
m/84'/0'/0'
```

![sparrow](assets/notext/14.webp)

Pärast seda kuvab Sparrow teie uue rahakoti tuletusandmed. Kui olete seadistanud paroolilause, on väga soovitatav märkida üles teie `Master fingerprint`. Kuigi see peamine võtmejäljend ei ole tundlik andme, on see hiljem kasulik, et kontrollida, kas pääsete tõesti õigele rahakotile ligi ja kinnitada paroolilause sisestamisel vigade puudumist.

Vajutage nupule `Apply`.

![sparrow](assets/notext/15.webp)

Sparrow kutsub teid looma oma rahakotile parooli. Seda parooli on vaja, et pääseda sellele ligi Sparrow Wallet tarkvara kaudu. Valige tugev parool, tehke sellest varukoopia ja seejärel vajutage `Set Password`.

![sparrow](assets/notext/16.webp)

### Bitcoini vastuvõtmine
Pärast oma rahakoti loomist on teil alguses üks konto, indeksiga `0'`. See on **deposiidi** konto, millest me eelmistes osades rääkisime. See on konto, millele peate saatma bitcoine segamiseks.

Selleks valige akna vasakul küljel `Receive` vaheleht. Sparrow genereerib automaatselt uue tühja aadressi bitcoinide vastuvõtmiseks.

![sparrow](assets/notext/17.webp)

Saate sellele aadressile märgistuse lisada ja seejärel saata sinna segamiseks bitcoine.

![sparrow](assets/notext/18.webp)

### Tx0 tegemine
Kui teie tehing on kinnitatud, saate seejärel minna `UTXOs` vahelehele.

![sparrow](assets/notext/19.webp)

Seejärel valige UTXO(d), mida soovite esitada coinjoin tsüklitele. Mitme UTXO samaaegseks valimiseks hoidke all `Ctrl` klahvi, klõpsates oma valitud UTXO-del.

![sparrow](assets/notext/20.webp)

Seejärel klõpsake akna allosas nuppu `Mix Selected`. Kui seda nuppu teie liideses ei kuvata, on see sellepärast, et kasutate riistvaralise rahakotiga turvatud rahakotti. Coinjoinide tegemiseks Sparrow'ga peate kasutama tarkvararahakotti.
![sparrow](assets/notext/21.webp)
Avaneb aken, mis selgitab, kuidas Whirlpool töötab. See on lihtsustus sellest, mida selgitasin eelmistes osades. Jätkamiseks klõpsake `Next`.

![sparrow](assets/notext/22.webp)

Järgmisel lehel saate sisestada "SCODE", kui teil on selline. SCODE on sooduskood, mis pakub allahindlust basseini teenustasudelt. Samourai Wallet pakub selliseid koode oma kasutajatele eriürituste ajal. Soovitan teil [jälgida Samourai Walletit](https://twitter.com/SamouraiWallet) sotsiaalmeedias, et mitte jääda ilma tulevastest SCODESidest.
Samal lehel peate seadistama ka tasumäära `Tx0` ja oma esialgse segamise jaoks. See valik mõjutab teie ettevalmistava tehingu ja esimese coinjoin'i kinnitamise kiirust. Pidage meeles, et olete vastutav `Tx0` ja esialgse segamise kaevandamistasude eest, kuid järgnevate ümbersegamiste eest tasusid maksma ei pea. Reguleerige `Premix Priority` liugurit vastavalt oma eelistustele, seejärel klõpsake `Next`.
![sparrow](assets/notext/23.webp)

Uues aknas on teil võimalus valida rippmenüüst bassein, milles soovite osaleda. Minu juhul, olles algselt valinud UTXO suurusega `456 214 sats`, on minu ainus võimalik valik bassein `100 000 sats`. See liides teavitab teid ka makstavatest teenustasudest ning UTXO-de arvust, mis basseini integreeritakse. Kui tingimused tunduvad teile rahuldavad, jätkake klõpsates `Preview Premix`.

![sparrow](assets/notext/24.webp)

Pärast seda sammu palub Sparrow sisestada teie rahakoti parooli, mille määrasite tarkvaral rahakoti loomisel. Parooli sisestamisel pääsete ligi oma `Tx0` eelvaatele. Akna vasakul küljel näete, et Sparrow on genereerinud erinevad kontod Whirlpooli kasutamiseks (`Deposit`, `Premix`, `Postmix` ja `Badbank`). Teil on ka võimalus vaadata oma `Tx0` struktuuri, mis sisaldab erinevaid väljundeid:
- Teenustasud;
- Võrdsustatud UTXO-d, mis on mõeldud basseini sisenemiseks;
- Toksiline vahetus (Doxxic Change).

![sparrow](assets/notext/25.webp)

Kui tehing on teie meelest sobiv, klõpsake `Broadcast Transaction`, et edastada teie `Tx0`. Vastasel juhul on teil võimalus `Tx0` parameetreid kohandada, valides `Clear`, et kustutada sisestatud andmed ja alustada loomisprotsessi algusest.

### Coinjoinide sooritamine
Kui Tx0 on edastatud, leiate oma UTXO-d segamiseks valmis `Premix` kontolt.
![sparrow](assets/notext/26.webp)

Kui `Tx0` on kinnitatud, registreeritakse teie UTXO-d koordinaatoriga ja esialgsed segamised algavad automaatselt järjest.

![sparrow](assets/notext/27.webp)

`Postmix` kontot kontrollides märkate esialgsetest segamistest saadud UTXO-sid. Need mündid jäävad valmis järgnevateks ümbersegamisteks, mis ei too kaasa lisatasusid.

![sparrow](assets/notext/28.webp)

`Mixes` veerus on võimalik näha iga teie mündi poolt sooritatud coinjoinide arvu. Nagu järgmistes jaotistes näeme, ei ole tegelikult oluline mitte niivõrd ümbersegamiste arv iseenesest, vaid pigem nendega seotud anonüümsuskomplektid, kuigi need kaks näitajat on osaliselt seotud.

![sparrow](assets/notext/29.webp)

Coinjoinide ajutiseks peatamiseks klõpsake lihtsalt `Stop Mixing`. Teil on võimalus operatsioone igal ajal jätkata, valides `Start Mixing`.

![sparrow](assets/notext/30.webp)
Selleks, et tagada teie UTXO-de pidev kättesaadavus segamiseks, on vajalik hoida Sparrow tarkvara aktiivsena. Tarkvara sulgemine või arvuti väljalülitamine peatab coinjoinid. Probleemi vältimiseks on võimalik keelata une funktsioonid läbi operatsioonisüsteemi seadete. Lisaks pakub Sparrow võimalust vältida arvuti automaatset unerežiimi minekut, mida saate leida `Tools` vahelehelt pealkirjaga `Prevent Computer Sleep`.
![sparrow](assets/notext/31.webp)

### Coinjoinide lõpetamine
Oma segatud bitcoinide kulutamiseks on teil mitu võimalust. Kõige otsesem meetod on pääseda ligi `Postmix` kontole ja valida `Send` vaheleht.

![sparrow](assets/notext/32.webp)

Selles jaotises on teil võimalus sisestada sihtkoha aadress, saadetava summa ja tehingutasud, samamoodi nagu iga teise Sparrow Walletiga tehtud tehingu puhul. Soovi korral võite kasutada ka täiustatud privaatsusfunktsioone nagu Stonewall, klõpsates `Privacy` nupul.

![sparrow](assets/notext/33.webp)

[-> Uuri lähemalt Stonewall tehingute kohta.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)

Kui soovite oma kulutatavate müntide valikut täpsemalt teha, minge `UTXOs` vahelehele. Valige spetsiifiliselt tarbida soovitud UTXOd ja seejärel vajutage `Send Selected` nuppu tehingu alustamiseks.

![sparrow](assets/notext/34.webp)
Lõpuks võimaldab Sparrow'is saadaolev `Mix to...` valik automaatselt eemaldada valitud UTXO coinjoin tsüklitest, lisatasusid maksmata. See funktsioon võimaldab määrata remixide arvu, pärast mida UTXO ei reintegreerita teie `Postmix` kontole, vaid kantakse otse teise rahakotti. Seda valikut kasutatakse sageli segatud bitcoinide automaatseks saatmiseks külma rahakotti.
Selle valiku kasutamiseks alustage avades saaja rahakoti koos oma coinjoin rahakotiga Sparrow tarkvaras.

![sparrow](assets/notext/35.webp)

Seejärel minge `UTXOs` vahelehele ja valige huvipakkuvad mündid, seejärel klõpsake akna allosas asuval `Mix to...` nupul.

![sparrow](assets/notext/36.webp)

Aken avaneb, alustage sihtkoha rahakoti valimisega rippmenüüst.

![sparrow](assets/notext/37.webp)

Valige coinjoini läviväärtus, millest alates tehakse väljamakse automaatselt. Ma ei saa teile täpset remixide arvu anda, kuna see varieerub vastavalt teie isiklikule olukorrale ja privaatsuseesmärkidele, kuid vältige liiga madala läviväärtuse valimist. Soovitan konsulteerida selle teise artikliga, et rohkem teada saada remiximise protsessist: [REMIX - WHIRLPOOL](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa).

Võite jätta `Index range` valiku vaikimisi väärtusele `Full`. See funktsioon võimaldab segamist samaaegselt erinevatest klientidest, kuid see pole meie eesmärk selles õpetuses. `Mix to...` valiku lõplikuks aktiveerimiseks vajutage `Restart Whirlpool`.

![sparrow](assets/notext/38.webp)

Siiski olge `Mix to` valiku kasutamisel ettevaatlik, kuna segatud müntide eemaldamine teie `Postmix` kontolt võib oluliselt suurendada teie privaatsuse ohustamise riski. Selle potentsiaali põhjused on üksikasjalikult kirjeldatud järgmistes jaotistes.

## Kuidas teada meie coinjoin tsüklite kvaliteeti?
Selleks, et coinjoin oleks tõeliselt efektiivne, on oluline, et see esitaks hea homogeensuse sisendite ja väljundite summade vahel. See ühtlus suurendab võimalike tõlgenduste arvu välise vaatleja silmis, suurendades seeläbi tehingu ümber olevat ebakindlust. Coinjoini poolt tekitatud ebakindluse kvantifitseerimiseks võib kasutada tehingu entroopia arvutamist. Nende näitajate põhjalikumaks uurimiseks viitan teile õpetusele: [BOLTZMANNI KALKULAATOR](https://planb.network/en/tutorials/privacy/boltzmann-entropy). Whirlpooli mudelit tunnustatakse kui seda, mis toob coinjoinides kõige rohkem homogeensust. Järgnevalt hinnatakse mitme coinjoini tsükli tulemuslikkust grupi suuruse põhjal, millesse münt on peidetud. Nende gruppide suurus määratleb nn anonsetid. Anonsete on kahte tüüpi: esimene hindab privaatsuse kasvu tagasiulatuva analüüsi vastu (olevikust minevikku) ja teine, etteulatuva analüüsi vastu (minevikust olevikku). Nende kahe näitaja detailseks selgituseks kutsun teid üles konsulteerima õpetusega: [WHIRLPOOLI STATISTIKATÖÖRIISTAD - ANONSETID](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375).

## Kuidas hallata postmixi?
Pärast coinjoini tsüklite sooritamist on parim strateegia hoida oma UTXOsid **postmix** kontol, oodates nende tulevast kasutamist. On isegi soovitatav lasta neil lõputult remixida, kuni peate neid kulutama.

Mõned kasutajad võivad kaaluda oma segatud bitcoinide ülekandmist riistvaralise rahakoti poolt kaitstud rahakotti. See on võimalik, kuid on oluline järgida täpselt Samourai Walleti soovitusi, et mitte ohustada omandatud konfidentsiaalsust.

UTXOde ühendamine on kõige sagedamini tehtav viga. On vajalik vältida segatud UTXOde ühendamist segamata UTXOdega samas tehingus, et vältida CIOH (*Common-Input-Ownership-Heuristic*) tekkimist. See nõuab teie UTXOde hoolikat haldamist oma rahakotis, eriti märgistamise osas. Peale coinjoini on UTXOde ühendamine üldiselt halb tava, mis tihti viib privaatsuse kaotuseni, kui seda korralikult ei hallata.

On oluline olla ettevaatlik ka segatud UTXOde omavahel konsolideerimisel. Mõõdukad konsolideerimised on mõeldavad, kui teie segatud UTXOdel on olulised anonsetid, kuid see vähendab paratamatult teie müntide konfidentsiaalsust. Veenduge, et konsolideerimised ei oleks liiga suured ega toimuks pärast ebapiisavat arvu remixe, kuna see seab ohtu dedutseeritavad seosed teie UTXOde vahel enne ja pärast coinjoini tsükleid. Kui kahtlete nende manipulatsioonide osas, on parim praktika mitte konsolideerida postmix UTXOsid ja üle kanda need ükshaaval oma riistvaralisse rahakotti, genereerides iga kord uue tühja aadressi. Jällegi, pidage meeles korralikult märgistada iga vastuvõetud UTXO.
Samuti ei soovitata üle kanda oma postmix UTXOsid rahakotti, mis kasutab ebatavalisi skripte. Näiteks, kui sisestate Whirlpooli multisig rahakotist, mis kasutab `P2WSH` skripte, on väike tõenäosus, et teid segatakse teiste kasutajatega, kellel on algselt sama tüüpi rahakott. Kui võtate oma postmixi välja samasse multisig rahakotti, väheneb teie segatud bitcoinide privaatsuse tase oluliselt. Skriptide kõrval on palju muid rahakoti jälgi, mis võivad teid eksitada.
Nagu iga Bitcoin'i tehingu puhul, on oluline ka mitte taaskasutada vastuvõtvaadressi. Iga uus tehing peaks toimuma uuel, tühjal aadressil.
Lihtsaim ja turvalisem lahendus on lasta oma segatud UTXO-del puhata nende **postmix** kontol, lastes neil uuesti seguneda ja puudutades neid ainult kulutamiseks. Samourai ja Sparrow rahakotid pakuvad lisakaitset kõigi nende ahelanalüüsiga seotud riskide vastu. Need kaitsemeetmed aitavad vältida vigade tegemist.
## Kuidas hallata doxxic muutust?
Järgmisena peate olema ettevaatlik doxxic muutuse haldamisel, muutusega, mis ei saanud siseneda coinjoin basseini. Need toksilised UTXO-d, mis tulenevad Whirlpooli kasutamisest, kujutavad endast teie privaatsusele ohtu, kuna need loovad seose teie ja coinjoini kasutamise vahel. Seetõttu on hädavajalik neid hoolikalt käsitseda ja mitte ühendada neid teiste UTXO-dega, eriti segatud UTXO-dega. Siin on erinevad strateegiad nende kasutamiseks:
- **Sega neid väiksemates basseinides:** Kui teie toksiline UTXO on piisavalt suur, et üksi väiksemasse basseini siseneda, kaaluge selle segamist. See on sageli parim valik. Siiski on oluline mitte ühendada mitut toksilist UTXO-d, et pääseda basseini, kuna see võib siduda teie erinevad sissekanded;
- **Märgi need "mittekulutatavateks":** Teine lähenemine on neid enam mitte kasutada, märkides need nende pühendatud kontol "mittekulutatavateks" ja lihtsalt Hodl. See tagab, et sa ei kuluta neid kogemata. Kui bitcoini väärtus tõuseb, võivad tekkida uued basseinid, mis sobivad paremini teie toksiliste UTXO-dega;
- **Tee annetusi:** Kaaluge annetuste tegemist, isegi tagasihoidlikke, arendajatele, kes töötavad Bitcoiniga ja selle seotud tarkvaraga. Samuti võite annetada organisatsioonidele, kes aktsepteerivad BTC-d. Kui teie toksiliste UTXO-de haldamine tundub liiga keeruline, võite neist lihtsalt vabaneda, tehes annetuse;
- **Osta kinkekaarte:** Platvormid nagu [Bitrefill](https://www.bitrefill.com/) võimaldavad teil vahetada bitcoine kinkekaartide vastu, mida saab kasutada erinevates kauplustes. See võib olla viis vabaneda oma toksilistest UTXO-dest ilma seotud väärtust kaotamata.
- **Konsolideeri need Moneros:** Samourai Wallet pakub nüüd aatomivahetuse teenust BTC ja XMR vahel. See on ideaalne toksiliste UTXO-de haldamiseks, konsolideerides need Moneros, ilma et see ohustaks teie privaatsust CIOH kaudu, enne kui saadate need tagasi Bitcoini. Siiski võib see valik olla kulukas kaevandustasude ja likviidsuspiirangute tõttu makstava preemia tõttu.
- **Saada need Lightning Networki:** Nende UTXO-de ülekandmine Lightning Networki, et kasu saada väiksematest tehingutasudest, on võimalus, mis võib olla huvitav. Siiski võib see meetod sõltuvalt teie Lightningi kasutamisest paljastada teatud teavet ja seetõttu tuleks seda praktiseerida ettevaatlikult.

Nende erinevate tehnikate rakendamise kohta pakutakse varsti üksikasjalikke õpetusi PlanB Networkis.

**Lisaresursid:**
- [Sparrow Wallet Videoõpetus](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607);
- [Samourai Wallet Videoõpetus](https://planb.network/tutorials/wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956);
- [Samourai Wallet Dokumentatsioon - Whirlpool](https://docs.samourai.io/whirlpool/basic-concepts);
- [Twitteri lõim CoinJoinsi kohta](https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [Blogipostitus CoinJoinsi kohta](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin).