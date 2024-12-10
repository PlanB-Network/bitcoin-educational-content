---
name: Coinjoin - Samourai Wallet
description: Kuidas teostada coinjoin'i Samourai Wallet'is?
---
![kaas](assets/cover.webp)

***HOIATUS:** Pärast Samourai Wallet'i asutajate arreteerimist ja nende serverite konfiskeerimist 24. aprillil ei toimi Whirlpool tööriist enam, isegi mitte nende kasutajate jaoks, kes omavad oma Dojo't või kasutavad Sparrow Wallet'it. Siiski on võimalik, et see tööriist võidakse järgnevate nädalate jooksul taaskehtestada või käivitada erineval viisil. Lisaks jääb selle artikli teoreetiline osa asjakohaseks coinjoin'ide põhimõtete ja eesmärkide mõistmiseks üldiselt (mitte ainult Whirlpool), samuti Whirlpooli mudeli tõhususe mõistmiseks.*

_Jälgime selle juhtumi arenguid ning seotud tööriistade arenguid tähelepanelikult. Võite olla kindlad, et uuendame seda õpetust, kui saabub uut teavet._

_Seda õpetust pakutakse ainult hariduslikel ja informatiivsetel eesmärkidel. Me ei toeta ega julgusta nende tööriistade kasutamist kuritegelikel eesmärkidel. Iga kasutaja vastutab oma jurisdiktsiooni seadustega kooskõlas olemise eest._

---

"*bitcoin'i rahakott tänavatele*"

Selles õpetuses saate teada, mis on coinjoin ja kuidas seda teostada kasutades Samourai Wallet tarkvara ja Whirlpooli rakendust.

## Mis on coinjoin Bitcoin'is?
**Coinjoin on tehnik, mis katkestab bitcoinide jälgitavuse blockchain'is**. See põhineb koostööl põhineval tehingul, millel on sama nimega spetsiifiline struktuur: coinjoin tehing.

Coinjoin'id suurendavad Bitcoin'i kasutajate privaatsust, muutes ketianalüüsi väliste vaatlejate jaoks keerulisemaks. Nende struktuur võimaldab ühendada mitme erineva kasutaja mündid üheks tehinguks, seeläbi varjates radu ja muutes sisend- ja väljundiaadresside vaheliste seoste kindlakstegemise keeruliseks.

Coinjoin'i põhimõte põhineb koostööl: mitu kasutajat, kes soovivad oma bitcoine segada, panevad samasugused summad sama tehingu sisenditena. Need summad jaotatakse seejärel võrdse väärtusega väljunditena igale kasutajale. Tehingu lõppedes muutub võimatuks seostada kindlat väljundit teadaoleva sisendiga kasutajaga. Sisendite ja väljundite vahel puudub otsene seos, katkestades seose kasutajate ja nende UTXO vahel, samuti iga mündi ajaloo.
![coinjoin](assets/notext/1.webp)

Näide coinjoin tehingust (mitte minult): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

Selleks, et teostada coinjoin, tagades samal ajal, et iga kasutaja hoiab oma vahendeid alati kontrolli all, algab protsess tehingu koostamisega koordinaatori poolt, kes seejärel edastab selle osalejatele. Iga kasutaja allkirjastab tehingu pärast selle sobivuse kontrollimist. Kõik kogutud allkirjad integreeritakse lõpuks tehingusse. Kui kasutaja või koordinaator üritab coinjoin tehingu väljundeid muutes vahendeid kõrvale juhtida, muutuvad allkirjad kehtetuks, viies tehingu tagasilükkamiseni sõlmede poolt.

Coinjoin'i on mitmeid rakendusi, nagu Whirlpool, JoinMarket või Wabisabi, mille eesmärk on hallata koordineerimist osalejate vahel ja suurendada coinjoin tehingute tõhusust.
Selles õpetuses sukeldume **Whirlpool** implementatsiooni, mida pean kõige efektiivsemaks lahenduseks coinjoinide sooritamiseks Bitcoinil. Kuigi see on saadaval mitmes rahakotis, uurime selles õpetuses eksklusiivselt selle kasutamist Samourai Wallet mobiilirakendusega, ilma Dojota.
## Miks sooritada coinjoine Bitcoinil?
Üks esialgsetest probleemidest mis tahes peer-to-peer maksesüsteemiga on topeltkulutamine: kuidas takistada pahatahtlikel isikutel sama rahaühikut mitu korda kulutamast ilma keskse autoriteedi poole pöördumata?

Satoshi Nakamoto pakkus sellele dilemmale lahenduse Bitcoin protokolli kaudu, mis on peer-to-peer elektrooniline maksesüsteem, mis toimib sõltumatult igasugusest kesksest autoriteedist. Oma valges raamatus rõhutab ta, et ainus viis topeltkulutamise puudumise tõendamiseks on tagada kõigi tehingute nähtavus maksesüsteemis.

Et tagada, et iga osaleja on tehingutest teadlik, peavad need olema avalikult avaldatud. Seega toetub Bitcoin läbipaistvale ja jaotatud infrastruktuurile, mis võimaldab igal sõlmeoperaatoril kontrollida kogu elektrooniliste allkirjade ahelate ja iga mündi ajalugu alates selle loomisest kaevandaja poolt.

Bitcoin'i blockchaini läbipaistev ja jaotatud olemus tähendab, et iga võrgu kasutaja saab jälgida ja analüüsida kõigi teiste osalejate tehinguid. Selle tulemusena on tehingutasandil anonüümsus võimatu. Siiski säilitatakse anonüümsus individuaalse identifitseerimise tasandil. Erinevalt traditsioonilisest pangandussüsteemist, kus iga konto on seotud isikliku identiteediga, on Bitcoinil vahendid seotud krüptograafiliste võtmepaaridega, pakkudes seeläbi kasutajatele pseudonüümsust krüptograafiliste identifikaatorite taga.

Seega on Bitcoinil konfidentsiaalsus kompromiteeritud, kui välised vaatlejad suudavad seostada kindlad UTXOd tuvastatud kasutajatega. Kui see seos on loodud, muutub nende tehingute jälgimine ja nende bitcoinide ajaloo analüüsimine võimalikuks. Coinjoin on just nimelt tehnika, mis on välja töötatud UTXOde jälgitavuse katkestamiseks, pakkudes seeläbi Bitcoin kasutajatele teatud konfidentsiaalsuse kihti tehingutasandil.

## Kuidas Whirlpool töötab?
Whirlpool eristub teistest coinjoin meetoditest, kasutades "_ZeroLink_" tehinguid, mis tagavad, et sisendite ja väljundite vahel ei ole tehniliselt mingit võimalikku seost. See täiuslik segamine saavutatakse struktuuriga, kus iga osaleja panustab sisendisse identse summa (v.a kaevandamistasud), genereerides seeläbi täiesti võrdsetes summadest väljundeid.
See sisenditele seatud piirang annab Whirlpool coinjoin tehingutele ainulaadse omaduse: täielik deterministlike seoste puudumine sisendite ja väljundite vahel. Teisisõnu, igal väljundil on võrdne tõenäosus olla omistatud mis tahes osalejale, võrreldes kõigi teiste tehingu väljunditega.
Algselt oli iga Whirlpool coinjoini osalejate arv piiratud 5-ga, 2 uue tulijaga ja 3 ümbersegajaga (selgitame neid mõisteid edaspidi). Siiski, 2023. aastal täheldatud on-chain tehingutasude tõusu tõttu pidid Samourai meeskonnad oma mudelit ümber mõtlema, et parandada privaatsust samal ajal kulusid vähendades. Seega, arvestades tasude turuolukorda ja osalejate arvu, saab koordinaator nüüd korraldada coinjoine, mis hõlmavad 6, 7 või 8 osalejat. Neid täiustatud seansse nimetatakse "_Surge Cycles_". On oluline märkida, et olenemata konfiguratsioonist, on Whirlpool coinjoinides alati ainult 2 uut tulijat.

Seega iseloomustavad Whirlpool tehinguid identne arv sisendeid ja väljundeid, mis võivad olla:
- 5 sisendit ja 5 väljundit;
![coinjoin](assets/notext/2.webp)
- 6 sisendit ja 6 väljundit;
![coinjoin](assets/notext/3.webp)
- 7 sisendit ja 7 väljundit;
![coinjoin](assets/notext/4.webp)- 8 sisendit ja 8 väljundit.
![coinjoin](assets/notext/5.webp)
Whirlpooli pakutud mudel põhineb seega väikestel coinjoin tehingutel. Erinevalt Wasabi'st ja JoinMarketist, kus anonüümsete osalejate hulga vastupidavus sõltub ühe tsükli osalejate mahust, panustab Whirlpool mitme väikese suurusega tsükli aheldamisele.

Sel mudelil maksab kasutaja tasud ainult oma esialgsel sisenemisel basseini, võimaldades neil osaleda paljudes ümbersegamistes ilma lisatasudeta. Uued sisenejad katavad ümbersegajate kaevandamistasud.

Iga täiendava coinjoin'iga, milles münt osaleb koos oma minevikus kohatud eakaaslastega, kasvavad anonüümsete osalejate hulgad eksponentsiaalselt. Eesmärk on seega ära kasutada neid tasuta ümbersegamisi, mis iga kordumisega aitavad tugevdada iga segatud mündiga seotud anonüümsete osalejate hulga tihedust.

Whirlpool on loodud arvestades kahte olulist nõuet:
- Rakendamise ligipääsetavus mobiilseadmetes, arvestades, et Samourai Wallet on peamiselt nutitelefoni rakendus;
- Ümbersegamistsüklite kiirus, et soodustada anonüümsete osalejate hulga märkimisväärset suurenemist.
Need imperatiivid juhtisid Samourai Walleti arendajaid Whirlpooli kujundamisel, sundides neid piirama osalejate arvu tsükli kohta. Liiga vähesed osalejad oleksid ohustanud coinjoin'i efektiivsust, drastiliselt vähendades iga tsükli jooksul genereeritud anonüümsete osalejate hulka, samas kui liiga paljud osalejad oleksid tekitanud haldusprobleeme mobiilirakendustes ja takistanud tsüklite voolu.
**Lõppkokkuvõttes pole Whirlpoolis iga coinjoin'i kohta vaja suurt osalejate arvu, kuna anonüümsete osalejate hulk saavutatakse mitme coinjoin-tsükli kuhjumise kaudu.**

[-> Uuri lähemalt Whirlpooli anonüümsete osalejate kohta.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

### Basseinid ja coinjoin tasud
Selleks, et need mitmed tsüklid tõhusalt suurendaksid segatud müntide anonüümsete osalejate hulka, tuleb kehtestada teatud raamistik, et piirata kasutatavate UTXO-de summasid. Whirlpool määratleb seega erinevad basseinid.

Bassein esindab kasutajate gruppi, kes soovivad koos segada, leppides kokku UTXO summas, mida kasutada coinjoin protsessi optimeerimiseks. Iga bassein määratleb UTXO jaoks fikseeritud summa, millest kasutaja peab kinni pidama, et osaleda. Seega, et teha coinjoine Whirlpooliga, peate valima basseini. Praegu saadaolevad basseinid on järgmised:
- 0,5 bitcoini;
- 0,05 bitcoini;
- 0,01 bitcoini;
- 0,001 bitcoini (= 100 000 satsi).

Liitudes oma bitcoinidega basseini, jagatakse need, et genereerida UTXO-d, mis on täiesti homogeensed basseini teiste osalejate omadega. Igal basseinil on maksimaalne piir; seega summade puhul, mis ületavad seda piiri, sunnitakse teid kas tegema kaks eraldi sisenemist samasse basseini või suunama end teise basseini, mille summa on suurem:

| Bassein (bitcoin) | Maksimaalne summa ühe sisenemise kohta (bitcoin) |
|-------------------|--------------------------------------------------|
| 0,5               | 35                                               |
| 0,05              | 3,5                                              |
| 0,01              | 0,7                                              |
| 0,001             | 0,025                                            |
Nagu varem mainitud, peetakse UTXO-d basseini kuuluvaks, kui see on valmis integreerimiseks coinjoin'i. Siiski, see ei tähenda, et kasutaja kaotab selle üle omamise. **Erinevate segamistsüklite vältel säilitate täieliku kontrolli oma võtmete ja seega ka oma bitcoinide üle.** See on see, mis eristab coinjoin tehnikat teistest tsentraliseeritud segamistehnikatest.
Coinjoin basseini sisenemiseks tuleb maksta teenustasusid ning kaevandamistasusid. Teenustasud on iga basseini jaoks fikseeritud ning on mõeldud Whirlpooli arenduse ja hoolduse eest vastutavate meeskondade kompenseerimiseks.
Whirlpooli kasutamise teenustasud tuleb maksta ainult üks kord basseini sisenedes. Pärast seda sammu on teil võimalus osaleda piiramatus arvus uuestisegamistes ilma lisatasudeta. Siin on praegused fikseeritud tasud iga basseini kohta:

| Bassein (bitcoin) | Sisenemistasu (bitcoin) |
|-------------------|-------------------------|
| 0.5               | 0.0175                  |
| 0.05              | 0.00175                 |
| 0.01              | 0.0005 (50,000 sats)    |
| 0.001             | 0.00005 (5,000 sats)    |


Need tasud toimivad sisuliselt sisenemispiletina valitud basseini, olenemata summast, mille panete coinjoin'i. Seega, kas liitute 0.01 basseiniga täpselt 0.01 BTC-ga või sisestate selle 0.5 BTC-ga, jäävad tasud absoluutväärtuses samaks.

Enne coinjoin'idega jätkamist on kasutajal seega valik kahe strateegia vahel:
- Eelistada väiksemat basseini, et minimeerida teenustasusid, teades, et vastu saadakse mitu väikest UTXO-d;
- Või eelistada suuremat basseini, nõustudes maksma kõrgemaid tasusid, et lõpuks saada vähem UTXO-sid suurema väärtusega.

Üldiselt soovitatakse vältida mitme segatud UTXO ühendamist pärast coinjoin tsükleid, kuna see võib kompromiteerida saavutatud konfidentsiaalsust, eriti Common-Input-Ownership Heuristic (CIOH) tõttu. Seetõttu võib olla mõistlik valida suurem bassein, isegi kui see tähendab rohkema maksmist, et vältida liiga paljude väikese väärtusega UTXO-de saamist väljundis. Kasutaja peab kaaluma neid kompromisse, et valida eelistatud bassein.

Peale teenustasude tuleb arvestada ka igale Bitcoin tehingule omaseid kaevandamistasusid. Whirlpooli kasutajana peate maksma kaevandamistasud ettevalmistustehingu (`Tx0`) ja esimese coinjoin'i eest. Kõik järgnevad uuestisegamised on tasuta, tänu Whirlpooli mudelile, mis toetub uute osalejate maksetele.

Tõepoolest, igas Whirlpooli coinjoin'is on kaks sisendit uued osalejad. Ülejäänud sisendid pärinevad uuestisegajatelt. Selle tulemusena kaetakse kõigi tehingu osalejate kaevandamistasud nende kahe uue osaleja poolt, kes seejärel saavad ka tasuta uuestisegamistest kasu:
![coinjoin](assets/en/6.webp)
Tänu sellele tasusüsteemile eristub Whirlpool tõeliselt teistest coinjoin teenustest, kuna UTXO-de anonüümsuskomplektid ei ole proportsionaalsed kasutaja poolt makstud hinnaga. Seega on võimalik saavutada märkimisväärselt kõrge anonüümsuse tase, makstes ainult basseini sisenemistasu ja kahe tehingu (Tx0 ja esialgne segamine) kaevandamistasud.
On oluline märkida, et kasutaja peab katma kaevandamistasud, et tõmmata oma UTXOd pärast mitme coinjoin'i lõpetamist basseinist välja, välja arvatud juhul, kui nad on valinud `mix to` valiku, millest me allpool olevas õpetuses räägime.

### Whirlpooli kasutatavad HD rahakoti kontod
Whirlpooli kaudu coinjoin'i sooritamiseks peab rahakott genereerima mitu eraldiseisvat kontot. Konto, HD (*Hierarchical Deterministic*) rahakoti kontekstis, kujutab endast täielikult teistest eraldatud sektsiooni, see eraldatus toimub rahakoti hierarhia kolmandal sügavustasemel, st xpub tasemel.

Teoreetiliselt võib HD rahakott tuletada kuni `2^(32/2)` erinevat kontot. Esialgne konto, mida vaikimisi kasutatakse kõikides Bitcoin rahakottides, vastab indeksile `0'`.

Whirlpoolile kohandatud rahakottide, nagu Samourai või Sparrow, puhul kasutatakse coinjoin protsessi vajaduste rahuldamiseks 4 kontot:
- **Deposiidi** konto, mida tuvastatakse indeksiga `0'`;
- **Halb pank** (või doxxic change) konto, mida tuvastatakse indeksiga `2 147 483 644'`;
- **Premix** konto, mida tuvastatakse indeksiga `2 147 483 645'`;
- **Postmix** konto, mida tuvastatakse indeksiga `2 147 483 646'`.

Iga nendest kontodest täidab coinjoin protsessis kindlat funktsiooni.

Kõik need kontod on seotud ühe seemnega, mis võimaldab kasutajal taastada juurdepääsu kõigile oma bitcoinidele, kasutades nende taastefraasi ja vajadusel nende paroolilauset. Siiski on vajalik tarkvarale selle taastamistoimingu ajal erinevate kasutatud kontoindeksite täpsustamine.

Vaadelgem nüüd Whirlpooli coinjoin'i erinevaid etappe nende kontode piires.

### Coinjoinide erinevad etapid Whirlpoolis
**Etap 1: Tx0**
Iga Whirlpooli coinjoin'i lähtepunkt on **deposiidi** konto. See konto on see, mida automaatselt kasutate, kui loote uue Bitcoin rahakoti. Sellele kontole tuleb kanda bitcoine, mida soovitakse segada.
`Tx0` esindab Whirlpooli segamisprotsessi esimest sammu. Selle eesmärk on ette valmistada ja võrdsustada UTXO coinjoin'i jaoks, jagades need üksusteks, mis vastavad valitud basseini summale, tagamaks segamise homogeensust. Võrdsustatud UTXOd saadetakse seejärel **premix** kontole. Mis puutub erinevusse, mis ei saa basseini siseneda, siis see eraldatakse spetsiifilisele kontole: **halb pank** (või "doxxic change").
See esialgne tehing `Tx0` teenib ka segamiskoordinaatori teenustasude tasumist. Erinevalt järgnevatest sammudest ei ole see tehing koostööaldis; kasutaja peab seega kandma kõik kaevandamistasud:
![coinjoin](assets/en/7.webp)

Selles `Tx0` tehingu näites jagatakse meie **deposiidi** kontolt pärit sisend `372,000 sats` mitmeks väljund UTXOks, mis jaotuvad järgmiselt:
- Summa `5,000 sats` on mõeldud koordinaatorile teenustasudeks, mis vastab basseini siseneva summa `100,000 sats` eest;
- Kolm UTXOd, mis on ette valmistatud segamiseks, suunatakse meie **premix** kontole ja registreeritakse koordinaatoriga. Need UTXOd võrdsustatakse `108,000 sats` igaühele, et katta nende tulevaste esialgsete segude kaevandamistasud;
- Ülejääk, mis on liiga väike, et basseini siseneda, peetakse toksiliseks vahetusrahaks. See suunatakse oma spetsiifilisse kontosse. Siin on see vahetusraha summa `40,000 sats`;
- Lõpuks on `3,000 sats`, mis ei moodusta väljundit, vaid on kaevandamistasud, mis on vajalikud `Tx0` kinnitamiseks.

Näiteks siin on päris Whirlpool Tx0 (mitte minult): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

**2. samm: Toksilised vahetusrahad**
Ülejääk, mida ei saanud basseini integreerida, siin võrdne `40,000 sats`-iga, suunatakse **halva panga** kontole, mida nimetatakse ka "toksiliseks vahetusrahaks", et tagada range eraldatus teistest rahakoti UTXO-dest.

See UTXO on kasutaja privaatsuse jaoks ohtlik, kuna see on endiselt seotud oma minevikuga ja seega võimalikult ka oma omaniku identiteediga, lisaks on see märgitud kasutajale, kes on teinud coinjoin'i.
Kui see UTXO ühendatakse segatud väljunditega, kaotavad need kõik coinjoin-tsüklite jooksul saavutatud konfidentsiaalsuse, eriti Common-Input-Ownership-Heuristic (CIOH) tõttu. Kui see ühendatakse teiste toksiliste vahetusrahadega, riskib kasutaja konfidentsiaalsuse kaotamisega, kuna see seob erinevad coinjoin-tsüklite sisendid. Seetõttu tuleb sellega ettevaatlikult ümber käia. Kuidas seda toksilist UTXO-d hallata, kirjeldatakse artikli viimases osas ja tulevased õpetused käsitlevad neid meetodeid PlanB võrgustikus põhjalikumalt.

**3. samm: Esialgne Segamine**
Pärast `Tx0` lõpetamist saadetakse võrdsustatud UTXO-d meie rahakoti **eelsegamise** kontole, valmis esimesse coinjoin-tsüklisse tutvustamiseks, mida nimetatakse ka "esialgseks segamiseks". Kui, nagu meie näites, `Tx0` genereerib mitu segamiseks mõeldud UTXO-d, integreeritakse igaüks neist eraldi esialgsesse coinjoin'i.

Nende esimeste segamiste lõppedes on **eelsegamise** konto tühi, samal ajal kui meie mündid, olles maksnud kaevandamistasud selle esimese coinjoin'i eest, on täpselt kohandatud valitud basseini määratletud summaga. Meie näites on meie esialgsed UTXO-d `108 000 sats`-ist vähendatud täpselt `100 000 sats`-ini.
![coinjoin](assets/en/8.webp)
**4. samm: Ümbersegamised**
Pärast esialgset segamist kantakse UTXO-d **järelsegamise** kontole. See konto kogub juba segatud UTXO-sid ja neid, mis ootavad ümbersegamist. Kui Whirlpooli klient on aktiivne, on **järelsegamise** konto UTXO-d automaatselt ümbersegamiseks saadaval ja neid valitakse juhuslikult osalema nendes uutes tsüklites.

Meenutuseks, ümbersegamised on seejärel 100% tasuta: ei nõuta täiendavaid teenustasusid ega kaevandamistasusid. UTXO-de hoidmine **järelsegamise** kontol säilitab seega nende väärtuse muutumatuna ja parandab samal ajal nende anonüümsete komplektide taset. Seepärast on oluline lasta neil müntidel osaleda mitmes coinjoin-tsüklis. See ei maksa teile midagi ja suurendab nende anonüümsuse taset.
Kui otsustate segatud UTXOsid kulutada, saate seda teha otse sellest **postmix** kontost. On soovitatav hoida segatud UTXOsid selles kontos, et saada kasu tasuta remixidest ja vältida nende lahkumist Whirlpooli ringlusest, mis võib vähendada nende konfidentsiaalsust.
Nagu me järgnevas õpetuses näeme, on olemas ka `mix to` valik, mis pakub võimalust saata automaatselt teie segatud mündid teise rahakotti, näiteks külma rahakotti, pärast määratud arvu coinjoine.
Pärast teooria läbitöötamist sukeldume praktikasse õpetusega, kuidas kasutada Whirlpooli läbi Samourai Wallet Androidi rakenduse!
## Õpetus: Coinjoin Whirlpool Samourai Walletis
Whirlpooli kasutamiseks on mitmeid võimalusi. Siin tutvustan Samourai Walleti valikut (ilma Dojota), mis on avatud lähtekoodiga Bitcoin'i rahakoti haldamise rakendus Androidil.

Segamine Samourai's ilma Dojota on eelis, kuna see on üsna lihtne kasutada, kiire seadistada ja ei nõua muud seadet peale Androidi telefoni ja internetiühenduse.

Siiski on sellel meetodil kaks märkimisväärset puudust:
- Coinjoinid toimuvad ainult siis, kui Samourai töötab taustal ja on ühendatud. See tähendab, et kui soovite oma bitcoine segada ja remixida 24/7, peate Samourai pidevalt sisse lülitatuna hoidma;
- Kui kasutate Whirlpooli Samourai Walletiga, ilma et ühendaksite oma Dojo, peab teie rakendus ühenduma Samourai meeskondade poolt hooldatava serveriga ja te avaldate neile oma rahakoti `xpub`. Need anonüümsed andmed on vajalikud, et teie rakendus leiaks teie tehingud.

Ideaalne lahendus nende piirangute ületamiseks on oma Dojo käitamine koos Whirlpool CLI instantsiga teie isiklikul Bitcoin'i noodil. Nii väldite igasugust informatsiooni leket ja saavutate täieliku sõltumatuse. Kuigi allpool esitatud õpetus on kasulik teatud eesmärkidel või algajatele, on oma Dojo kasutamine tõeliselt optimaalse coinjoini seansi saavutamiseks soovitatav. Selle seadistuse üksikasjalik juhend on varsti saadaval PlanB Networkis.

### Samourai Walleti paigaldamine
Alustuseks vajate ilmselgelt Samourai Walleti rakendust. Saate selle otse ametlikult veebisaidilt alla laadida APK kaudu, nende GitLabist või Google Play poest.

### Tarkvararahakoti loomine
Pärast tarkvara paigaldamist peate jätkama Bitcoin'i rahakoti loomisega Samourais. Kui teil juba on üks, võite järgmise sammu juurde otse minna.

Rakenduse avamisel vajutage sinist `Start` nuppu. Seejärel palutakse teil valida asukoht telefoni failides, kus teie uue rahakoti krüpteeritud varukoopia salvestatakse.

![samourai](assets/notext/9.webp)
Aktiveerige Tor, klõpsates vastaval lülitil. Selles etapis on teil võimalus valida ka konkreetne Dojo. Kuid selles õpetuses jätkame vaikimisi Dojoga; nii et võite valiku keelata. Kui Tor on ühendatud, vajutage `Loo uus rahakott` nuppu.
![samourai](assets/notext/10.webp)

Samourai Wallet seejärel palub teil seada BIP39 paroolilause. See lisaparool on väga oluline, kuna see toimib otseselt teie privaatvõtmete tuletamisel. Selle paroolilause kaotamine toob kaasa võimetuse pääseda ligi teie bitcoinidele, muutes need pöördumatult kadunuks. Oma Samourai rahakoti taastamiseks on hädavajalik omada nii teie 12-sõnalist taastefraasi kui ka paroolilauset.
Seetõttu on oluline valida tugev paroolilause ja teha üks või mitu füüsilist koopiat, kas paberil või metallil, et tagada oma bitcoinide turvalisus. Pärast nende ülesannete täitmist märkige ruut `Olen teadlik, et kaotuse korral...`, seejärel vajutage `JÄRGMINE` nuppu.
![samourai](assets/notext/11.webp)

Seejärel peate määrama PIN-koodi, mis koosneb 5 kuni 8 numbrist. See kood tagab juurdepääsu turvalisuse teie rahakotile telefonis. Samourai rakenduse avamisel küsitakse seda koodi iga kord. Valige tugev PIN-kood ja veenduge, et teil on varukoopia. Pärast seda võite vajutada `JÄRGMINE` nuppu.

![samourai](assets/notext/12.webp)

Samourai palub teil PIN-koodi uuesti sisestamiseks kinnituseks. Sisestage see, seejärel vajutage `LÕPETA`.

![samourai](assets/notext/13.webp)

Seejärel pääsete juurde oma taastefraasile, mis koosneb 12 sõnast. See fraas võimaldab teil taastada oma rahakoti eelnevalt sisestatud paroolilause abil. On tungivalt soovitatav teha sellest fraasist üks või mitu koopiat füüsilisel kandjal, näiteks paberil või metallil, et tagada oma bitcoinide turvalisus probleemi korral.

Pärast nende varunduste tegemist suunatakse teid teie uue Samourai rahakoti liidesesse.

![samourai](assets/notext/14.webp)

Teile pakutakse võimalust saada oma PayNym Bot. Võite seda soovi korral taotleda, kuigi see ei ole meie õpetuse jaoks hädavajalik.

![samourai](assets/notext/15.webp)
Enne uuele rahakotile bitcoinide vastuvõtmist on tungivalt soovitatav uuesti kontrollida oma rahakoti varunduste (paroolilause ja taastefraasi) kehtivust. Paroolilause kontrollimiseks saate valida oma PayNym Boti ikooni, mis asub ekraani vasakus ülanurgas, seejärel järgige teed:
```plaintext
Seaded > Tõrkeotsing > Paroolilause/varukoopia test
```

Sisestage oma paroolilause kontrollimiseks.

![samourai](assets/notext/16.webp)

Samourai kinnitab, kas see on kehtiv.

![samourai](assets/notext/17.webp)

Taastefraasi varukoopia kontrollimiseks pääsete juurde oma PayNym Boti ikoonile, mis asub ekraani vasakus ülanurgas, ja järgige seda teed:
```plaintext
Seaded > Rahakott > Näita 12-sõnalist taastefraasi
```

Samourai kuvab akna teie taastefraasiga. Veenduge, et see vastab täpselt teie füüsilisele varukoopiale.

Täieliku taastamistesti tegemiseks ja veelgi kaugemale minemiseks märkige üles oma rahakoti tunnistuselement, näiteks üks `xpubs`, seejärel jätkake oma rahakoti kustutamisega (eeldusel, et see on endiselt tühi). Eesmärk on proovida taastada see tühi rahakott kasutades ainult teie füüsilisi varukoopiaid. Kui taastamine õnnestub, näitab see, et teie varukoopiad on kehtivad ja usaldusväärsed.

### Bitcoinide vastuvõtmine
Pärast oma rahakoti loomist alustate ühe kontoga, mida tuvastatakse indeksiga `0'`. See on **deposiidi** konto, millest me eelmistes osades rääkisime. Just sellele kontole peate kandma coinjoins jaoks mõeldud bitcoinid.

Selleks klõpsake ekraani paremas alanurgas asuval sinisel `+` sümbolil.

![samourai](assets/notext/18.webp)

Seejärel klõpsake rohelisel `Vasta võta` nupul.

![samourai](assets/notext/19.webp)

Samourai genereerib automaatselt uue tühja aadressi bitcoinide vastuvõtmiseks.

![samourai](assets/notext/20.webp)
Saate saata bitcoine segamiseks sinna.
![samourai](assets/notext/21.webp)

### Tx0 loomine
Kui tehing on kinnitatud, saame alustada coinjoin protsessiga. Selleks klõpsake ekraani paremas alanurgas sinisel `+` nupul.

![samourai](assets/notext/22.webp)

Seejärel klõpsake sinisel `Whirlpool`.

![samourai](assets/notext/23.webp)

Oodake, kuni Whirlpool käivitub ja Samourai loob vajalikud kontod.

![samourai](assets/notext/24.webp)

Seejärel jõuate Whirlpooli avalehele. Klõpsake `Start`.
![samourai](assets/notext/25.webp)
Valige **deposit** kontolt UTXO, mida soovite saata coinjoin tsüklitesse, seejärel klõpsake `Next`.

![samourai](assets/notext/26.webp)

Järgmises etapis peate valima taseme `Tx0` jaoks ning oma esimese segamise jaoks. See seadistus määrab kiiruse, millega teie `Tx0` ja teie esimene coinjoin (või esimesed coinjoins) kinnitatakse. Pidage meeles, et `Tx0` ja esimese segamise kaevandamistasud on teie kanda, kuid järgnevate ümbersegamiste eest tasusid maksma ei pea. Teil on valikus `Low`, `Normal` või `High` võimalused.

![samourai](assets/notext/27.webp)

Samas aknas on teil võimalus valida bassein, kuhu siseneda. Kuna valisin alguses UTXO suurusega `454,258 sats`, on minu ainus võimalik valik `100,000 sats` bassein. See leht esitab teile ka basseini teenustasud lisaks kaevandamistasudele, mis võimaldab teil teada saada selle coinjoin tsükli kogumaksumust. Kui kõik sobib, valige sobiv bassein ja jätkake, klõpsates sinisel `VERIFY CYCLE DETAILS` nupul.

![samourai](assets/notext/28.webp)

Seejärel näete kõiki oma coinjoin tsükli detaile:
- basseini sisenevate UTXO-de arv;
- erinevad tasud;
- doxxic muutuse summa...

Kontrollige teavet, seejärel klõpsake rohelisel `START CYCLE` nupul.

![samourai](assets/notext/29.webp)

Ilmub aken, mis pakub teile võimalust märkida coinjoin tsüklisse sisenemisest tulenev toksiline muutus "mittekulutatavaks". Valides `YES`, ei ole see UTXO teie rahakotis nähtav ega valitav tulevaste tehingute jaoks. Siiski jääb see juurdepääsetavaks teie rahakoti UTXO-de loendis, kus saate selle staatust käsitsi muuta. Soovitatav on see valik teha, et vältida mis tahes käsitsemisviga, mis võib hiljem teie privaatsust ohustada. Kui valite `NO`, jääb toksiline muutus teie rahakotis kasutamiseks saadavaks. Kui soovite rohkem teada saada selle toksilise muutuse haldamise ja kasutamise kohta, soovitan teil lugeda selle õpetuse viimast osa.

![samourai](assets/notext/30.webp)

Samourai seejärel edastab teie Tx0.

![samourai](assets/notext/31.webp)

### Coinjoinide tegemine
Kui Tx0 on edastatud, leiate selle Whirlpooli menüü `Transactions` vahelehelt.

![samourai](assets/notext/32.webp)
Teie segamiseks valmis UTXOd asuvad vahekaardil `Mixing in progress...`, mis vastab **Premix** kontole.![samourai](assets/notext/33.webp)

Kui `Tx0` on kinnitatud, registreeritakse teie UTXOd automaatselt koordinaatoriga ja esialgsed segamised algavad järjestikku automaatselt.

![samourai](assets/notext/34.webp)

Kontrollides vahekaarti `Remixing`, mis vastab **Postmix** kontole, näete esialgsetest segamistest saadud UTXOsid. Need mündid jäävad valmis järgnevaks ümbersegamiseks, mis ei too kaasa lisatasusid. Soovitan konsulteerida selle teise artikliga, et saada rohkem teavet ümbersegamise protsessi ja coinjoin tsükli efektiivsuse kohta: [REMIX - WHIRLPOOL](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa).

![samourai](assets/notext/35.webp)

UTXO ajutiseks ümbersegamise peatamiseks on võimalik vajutada selle paremal asuvale pausinupule. Selle uuesti ümbersegamiseks sobilikuks muutmiseks klõpsake lihtsalt samal nupul teist korda. On oluline märkida, et ühe kasutaja ja basseini kohta saab korraga teostada ainult ühe coinjoini. Seega, kui teil on 6 UTXOt `100 000 sats` valmis coinjoiniks, saab segada ainult ühte neist. Pärast UTXO segamist valib Samourai Wallet juhuslikult uue UTXO teie saadavusest, et mitmekesistada ja tasakaalustada iga mündi ümbersegamist.

![samourai](assets/notext/36.webp)

Selleks, et tagada teie UTXOde pidev saadavus ümbersegamiseks, on vajalik hoida Samourai rakendus taustal aktiivsena. Peaksite oma telefonis nägema teadet, mis kinnitab, et Whirlpool töötab. Rakenduse sulgemine või telefoni väljalülitamine peatab coinjoinid.

### Coinjoinide lõpetamine
Segatud bitcoinide kulutamiseks minge **Postmix** kontole, mida märgitakse Whirlpooli menüü vahekaartidel kui `Remixing`.

![samourai](assets/notext/37.webp)

Klõpsake alumises paremas nurgas asuval sinisel Whirlpooli logol.

![samourai](assets/notext/38.webp)

Seejärel klõpsake `Spend Mixed UTXOs`.

![samourai](assets/notext/39.webp)

Seejärel saate sisestada saaja aadressi ja saadetava summa, samamoodi nagu iga teise Samourai Walletiga tehtud tehingu puhul. Sinine taust näitab, et vahendid kulutatakse Whirlpooli kontolt, mitte **deposiidi** kontolt.

![samourai](assets/notext/40.webp)

Klõpsates üleval paremal asuvatel kolmel väikesel punktil, on teil võimalus valida kindlad UTXOd.
![samourai](assets/notext/41.webp)
Klõpsates akna üleval paremal asuval valgel ruudul, saate oma kaameraga skaneerida saaja aadressi QR-koodi.

![samourai](assets/notext/42.webp)

Sisestage oma kulutustehingu jaoks vajalik teave, seejärel klõpsake sinisel `VERIFY TRANSACTION` nupul.

![samourai](assets/notext/43.webp)
Järgmises etapis on teil võimalus muuta oma tehingu tasumäära. Samuti saate lubada Stonewall valiku, märkides vastava ruudu. Kui Stonewall valikut ei saa valida, tähendab see, et teie **Postmix** konto ei sisalda piisavalt suurt UTXO-d, et toetada seda konkreetset tehingustruktuuri.
[-> Lugege lisaks Stonewall tehingute kohta.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)

Kui kõik on teie jaoks rahuldav, klõpsake rohelisel `SEND ... BTC` nupul.

![samourai](assets/notext/44.webp)

Seejärel Samourai allkirjastab teie tehingu enne selle võrku saatmist. Peate lihtsalt ootama, kuni see lisatakse plokki miner'i poolt.

![samourai](assets/notext/45.webp)

### SCODE kasutamine
Mõnikord pakuvad Samourai Wallet meeskonnad "SCODE-sid". SCODE on sooduskood, mis pakub allahindlust basseini teenustasudele. Samourai Wallet pakub selliseid koode oma kasutajatele eriliste sündmuste ajal. Soovitan teil [jälgida Samourai Walletit](https://twitter.com/SamouraiWallet) sotsiaalmeedias, et mitte jääda ilma tulevastest SCODE-dest.

SCODE rakendamiseks Samourais, enne uue coinjoin tsükli alustamist, minge Whirlpool menüüsse ja valige kolm väikest punkti ekraani paremas ülanurgas.

![samourai](assets/notext/46.webp)

Klõpsake `SCODE (promo code) Whirlpool`.

![samourai](assets/notext/47.webp)

Sisestage avanenud aknas SCODE, seejärel kinnitage klõpsates `OK`.

![samourai](assets/notext/48.webp)

Whirlpool sulgub automaatselt. Oodake, kuni Samourai on laadimise lõpetanud, seejärel avage Whirlpool menüü uuesti.

![samourai](assets/notext/49.webp)

Veenduge, et teie SCODE on õigesti registreeritud, klõpsates veel kord kolmel väikesel punktil ja valides `SCODE (promo code) Whirlpool`. Kui kõik on korras, olete valmis alustama uut Whirlpool tsüklit teenustasude allahindlusega. On oluline märkida, et need SCODE-d on ajutised: need jäävad kehtima mõneks päevaks enne, kui muutuvad aegunuks.

## Kuidas teada meie coinjoin tsüklite kvaliteeti?
Selleks, et coinjoin oleks tõeliselt efektiivne, on oluline, et see näitaks head ühtsust sisendite ja väljundite summade vahel. See ühtsus suurendab võimalike tõlgenduste arvu välise vaatleja silmis, suurendades seeläbi tehingu ümber olevat ebakindlust. Selle ebakindluse kvantifitseerimiseks, mida coinjoin tekitab, võib kasutada tehingu entroopia arvutamist. Nende näitajate süvauuringuks viitan teid õpetusele: [BOLTZMANNI KALKULAATOR](https://planb.network/en/tutorials/privacy/boltzmann-entropy). Whirlpooli mudelit tunnustatakse kui seda, mis toob coinjoinidele kõige rohkem homogeensust.
Järgnevalt hinnatakse mitme coinjoin tsükli sooritust lähtuvalt rühmade ulatusest, milles münt on peidetud. Nende rühmade suurus määratleb, mida nimetatakse anonüümseteks komplektideks. Anonüümseid komplekte on kahte tüüpi: esimene hindab saavutatud privaatsust tagasiulatuva analüüsi (olevikust minevikku) põhjal ja teine, tulevikku suunatud analüüsi (minevikust olevikku) põhjal. Nende kahe näitaja detailse selgituse saamiseks kutsun teid tutvuma õpetusega: [WHIRLPOOL STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375).

## Kuidas hallata postmixi?
Pärast coinjoin tsüklite sooritamist on parim strateegia hoida oma UTXOsid **postmix** kontol, oodates nende tulevast kasutamist. On isegi soovitatav lasta neil lõputult remixida, kuni on vaja neid kulutada.

Mõned kasutajad võivad kaaluda oma segatud bitcoinide ülekandmist riistvaralise rahakoti poolt kaitstud rahakotti. See on võimalik, kuid on oluline järgida Samourai Wallet'i soovitusi täpselt, et mitte ohustada saavutatud konfidentsiaalsust.

UTXOde ühendamine on kõige sagedamini tehtav viga. On vajalik vältida segatud UTXOde ühendamist segamata UTXOdega samas tehingus, et vältida CIOH (*Common-Input-Ownership-Heuristic*) tekkimist. See nõuab teie UTXOde hoolikat haldamist teie rahakotis, eriti märgistamise osas. Peale coinjoini on UTXOde ühendamine üldiselt halb praktika, mis tihti viib konfidentsiaalsuse kaotamiseni, kui seda korralikult ei hallata.
Samuti peaks olema ettevaatlik segatud UTXOde omavahelise konsolideerimisega. Mõõdukad konsolideerimised on võimalikud, kui teie segatud UTXOdel on olulised anonüümsed komplektid, kuid see vähendab paratamatult teie müntide privaatsust. Veenduge, et konsolideerimised ei oleks liiga suured ega toimuks pärast ebapiisavat arvu remixe, kuna see suurendab ohtu, et teie UTXOde vahel enne ja pärast coinjoin tsükleid luuakse jälitatavad seosed. Kui kahtlete nende toimingute osas, on parim praktika mitte konsolideerida postmix UTXOsid ja üle kanda need ükshaaval oma riistvaralisse rahakotti, genereerides iga kord uue tühja aadressi. Jällegi, pidage meeles iga saadud UTXO korrektselt märgistada.

Samuti ei soovitata üle kanda oma postmix UTXOsid rahakotti, mis kasutab ebatavalisi skripte. Näiteks, kui sisestate Whirlpooli multisig rahakotist, mis kasutab `P2WSH` skripte, on väike tõenäosus, et teid segatakse teiste sama tüüpi rahakoti algsete kasutajatega. Kui väljute oma postmixist samasse multisig rahakotti, väheneb teie segatud bitcoinide privaatsuse tase oluliselt. Peale skriptide on palju muid rahakoti jälgi, mis võivad teid eksitada.

Nagu iga Bitcoin tehingu puhul, on samuti asjakohane mitte taaskasutada vastuvõtvaadressi. Iga uus tehing peab olema vastu võetud uuel tühjal aadressil.

Lihtsaim ja turvalisim lahendus on lasta oma segatud UTXOdel puhata nende **postmix** kontol, lastes neil remixida ja puudutades neid ainult kulutamiseks. Samourai ja Sparrow rahakotid pakuvad lisakaitset kõigi nende ahelaanalüüsiga seotud riskide eest. Need kaitsemeetmed aitavad teil vältida vigu.

## Kuidas hallata doxxic muutust?
Järgmisena peate olema ettevaatlik doxxic muutuse haldamisel, muutusega, mis ei saanud siseneda coinjoin basseini. Need toksilised UTXOd, mis tulenevad Whirlpooli kasutamisest, kujutavad endast ohtu teie privaatsusele, kuna need loovad seose teie ja coinjoini kasutamise vahel. Seetõttu on hädavajalik neid ettevaatlikult käsitseda ja mitte ühendada neid teiste UTXOdega, eriti segatud UTXOdega. Siin on erinevad strateegiad nende kasutamiseks:
- **Sega neid väiksematesse basseinidesse:** Kui sinu toksiline UTXO on piisavalt suur, et üksi väiksemasse basseini siseneda, kaalu selle segamist. See on tihti parim valik. Siiski on oluline mitte ühendada mitut toksilist UTXOd, et pääseda basseini, kuna see võib sinu erinevad sissekanded omavahel seostada.
- **Märgi need "mittekulutatavaks":** Teine lähenemine on nende kasutamise lõpetamine, märkides need nende pühendatud kontol "mittekulutatavaks" ja lihtsalt Hodl. See tagab, et sa ei kuluta neid kogemata. Kui bitcoini väärtus tõuseb, võivad ilmuda uued basseinid, mis sobivad paremini sinu toksiliste UTXOde jaoks;
- **Tee annetusi:** Kaalu annetuste tegemist, isegi tagasihoidlikke, arendajatele, kes töötavad Bitcoin'i ja selle seotud tarkvaraga. Sa võid samuti annetada organisatsioonidele, mis aktsepteerivad BTC-d. Kui sinu toksiliste UTXOde haldamine tundub liiga keeruline, võid neist lihtsalt vabaneda, tehes annetuse;
- **Osta kinkekaarte:** Platvormid nagu [Bitrefill](https://www.bitrefill.com/) võimaldavad sul vahetada bitcoine kinkekaartide vastu, mida saab kasutada erinevates kauplustes. See võib olla viis vabaneda oma toksilistest UTXOdest ilma seotud väärtust kaotamata;
- **Konsolideeri need Moneros:** Samourai Wallet pakub nüüd aatomivahetuse teenust BTC ja XMR vahel. See on ideaalne toksiliste UTXOde haldamiseks, konsolideerides need Moneros, ilma sinu privaatsust KYC kaudu ohustamata, enne kui saadad need tagasi Bitcoini. Siiski võib see valik olla kulukas kaevandamistasude ja likviidsuspiirangute tõttu makstava preemia tõttu;
- **Saada need Lightning Networki:** Nende UTXOde ülekandmine Lightning Networki, et kasu saada vähendatud tehingutasudest, on huvitav valik. Siiski võib see meetod sõltuvalt sinu Lightningi kasutusest teatud teavet avaldada ja seetõttu tuleks seda praktiseerida ettevaatlikult.

Üksikasjalikud õpetused nende erinevate tehnikate rakendamiseks pakutakse varsti PlanB Networkis.

**Lisaresursid:**
- [Samourai Wallet videoõpetus](https://planb.network/tutorials/wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956);
- [Samourai Wallet Dokumentatsioon - Whirlpool](https://docs.samourai.io/whirlpool/basic-concepts);
- [Twitteri lõim coinjoins kohta](https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [Blogipostitus coinjoins kohta](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin).