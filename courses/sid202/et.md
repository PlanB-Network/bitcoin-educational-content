---
name: Ehitus elementide ja vedelikuvõrguga
goal: Õppige kasutama ja arendama avatud lähtekoodiga plokiahela platvormi Elements ja selle põhifunktsioone
objectives: 

  - Mõista Elements plokiahela platvormi ja Liquid sidechains põhimõisteid.
  - Õppige seadistama ja käivitama Elements'i sõlmi eraldiseisvate ja külgahela konfiguratsioonide jaoks.
  - Saate praktilisi kogemusi föderaalse plokkide allkirjastamise ja föderaalse 2-suunalise Pegiga.
  - Turvaliste ja tõhusate plokiahela keskkondade loomine ja haldamine reaalsete kasutusjuhtumite jaoks.

---
# Ehita vedelik ja elemendid

Avastage Liquid ja Elements'i täiustatud funktsioone ja võimalusi ning õppige, kuidas neid vahendeid oma arendusprojektide täiustamiseks tõhusalt kasutada. See koolitus annab täieliku teoreetilise ja praktilise aluse, mis võimaldab teil omandada selliseid funktsioone nagu konfidentsiaalsed tehingud, väljastatud varad ja föderaalne plokkallkirjastamine.

Elements-raamistikul põhinev Liquid on loodud selleks, et parandada finants- ja tehniliste lahenduste privaatsust, skaleeritavust ja funktsionaalsust. Sellel kursusel saate praktilisi kogemusi varade väljastamise ja haldamise, föderaalse 2-suunalise Pegi ning selliste tööriistade nagu elementsd ja elements-cli kasutamisega, mis annab teile võimaluse luua uuenduslikke, teie vajadustele kohandatud lahendusi.

See kursus on mõeldud kõikide kogemustasemete arendajatele. Algajad ja edasijõudnud kasutajad leiavad arusaadavaid selgitusi ja praktilisi näiteid, samas kui edasijõudnud kasutajad saavad süveneda Liquid ja Elements'i tehnilistesse üksikasjadesse ja vähemtuntud funktsioonidesse.

Liitu meiega, et tõsta oma oskusi, avada Liquid'i ja Elements'i täielik potentsiaal ning luua mõjusaid vahendeid Liquid'i innovatsiooni tuleviku jaoks.

+++
# Sissejuhatus

<partId>8f34de87-6e9a-4e3b-a326-50fc7c1803b3</partId>

## Kursused Sissejuhatus

<chapterId>a721398e-7040-4edd-be53-b485ea759fa9</chapterId>

![Video](https://youtu.be/gkQfnwYLyI0?si=H6cIPhgZaSAwHaHI)

Elements Academy eesmärk on tutvustada ja selgitada Elements'i, avatud lähtekoodiga platvormi, millele Liquid on ehitatud, põhimõisteid. Kursuse lõpuks peaks teil olema hea arusaam Elements'i peamistest funktsioonidest, näiteks konfidentsiaalsetest tehingutest ja väljastatud varadest, ning Elements Core'i käitamisega seotud protsessidest.

Igas osas on õppetunnid koos selgitava tekstiga ja video, mis lõpeb viktoriiniga. Küsimuste arv on seotud eelneva teema mahuga. 10. jagu võtab kursuse sisu kokku ja lõpeb suurema viktoriiniga.

Kõik küsimused, lisateabe taotlused või päringud viktoriini vastuste kohta võite suunata oma õpetajale James Dorfmanile.

## Elementide ülevaade

<chapterId>7a7f2712-5300-4a6d-b1ed-05eab731bc35</chapterId>

![Video](https://youtu.be/ns-JLGdkNig?si=fmWye_boRSvVF1Bt)

Elements on avatud lähtekoodiga, sidechain-võimeline plokiahela platvorm, mis pakub juurdepääsu kogukonna liikmete poolt välja töötatud võimsatele funktsioonidele, nagu Confidential Transactions ja Issued Assets.

Elements on oma põhiolemuselt protokoll, mis võimaldab konsensuse saavutamist tehinguajaloo ja reeglite ümber, mis reguleerivad jaotatud plokiahela pearaamatusse salvestatud varade ülekandmist ja loomist.

Rohkem taustateavet Elements'i kohta leiate hõlpsasti Elements Project'i veebisaidilt (https://elementsproject.org/), ametlikust Liquid'i blogist (https://blog.liquid.net/) ja arendajaportaalist(https://liquid.net/devs).

### Elements

2015. aastal käivitatud Elements vähendab sisemisi arendus- ja uurimiskulusid ning kasutab kõige uuemat plokiahela tehnoloogiat, avades paljud uued rakendusjuhtumid. Elementsil põhinev plokiahela võib toimida kas iseseisva plokiahelana või olla seotud mõne teise plokiahela külge ja toimida sidechainina. Elements'i käivitamine Sidechain'ina võimaldab varasid eri plokiahelate vahel kontrollitavalt üle kanda.

Bitcoini koodibaasi põhjal ja seda laiendades võimaldab see bitcoind APIga tuttavatel arendajatel kiiresti ja kulutõhusalt luua töötavaid plokiahelaid ja testida proof-of-concept projekte. Bitcoini koodibaasile ehitamine võimaldab Elementsil toimida ka Bitcoini protokolli enda muutuste testkeskkonnana.

Järgnevalt on loetletud mõned Elements'i peamised funktsioonid.

#### Konfidentsiaalsed tehingud

Vaikimisi on kõik aadressid elementides pimendatud, kasutades Konfidentsiaalsed tehingud. Blinding on protsess, mille käigus ülekantava vara summa ja liik on krüptograafiliselt varjatud kõigi eest, välja arvatud osalejate ja nende eest, kellele nad otsustavad blinding võtme avaldada.

#### Väljaantud varad

Issued Assets on Elements võimaldab mitut liiki vara väljastada ja üle kanda võrguosaliste vahel. Väljaantud vara saab kasutada ka konfidentsiaalset tehingut ja seda saab uuesti välja anda või hävitada igaüks, kellel on vastav taasväljaandmise märgis.

#### Föderatsiooniline 2-suunaline tüüner

Elements on üldotstarbeline plokiahelaplatvorm, mida saab ka olemasoleva plokiahelaga (nt Bitcoin) "siduda", et võimaldada varade kahesuunalist ülekandmist ühest ahelast teise. Elements'i rakendamine külgahelana võimaldab ümber teha mõned põhiahelale omased omadused, säilitades samal ajal suure osa põhiahelas kindlustatud varade pakutavast turvalisusest.

#### Allkirjastatud plokid

Elements kasutab tugevat allkirjastajate föderatsiooni, mida nimetatakse plokkide allkirjastajateks, kes allkirjastavad ja loovad plokke usaldusväärselt ja õigeaegselt. See kõrvaldab PoW-kaevandamise protsessi tehinguviivituse, mis on juhusliku poissoni jaotuse tõttu suures plokkide ajavarieeruvuses. Liitplokkide allkirjastamise protsessiga saavutatakse usaldusväärne plokkide loomine, ilma et oleks vaja kolmanda osapoole usaldust või arvutuslikul "algoritmil" põhinevat kaevandamist.

Elements lisab kõik need funktsioonid Bitcoin Core'i koodibaasi peale, laiendades peahela protokolli võimekust ja võimaldades uusi ärilisi kasutusjuhtumeid, kui neid kasutatakse kõrvalahela või iseseisva plokiahela lahendusena.

# Element

<partId>ac68d611-be84-432f-a3a8-620d310e131c</partId>

## Kuidas elemendid töötavad

<chapterId>05d88877-58b0-455b-9ae6-a72d19070525</chapterId>

![Video](https://youtu.be/v0lzmfH81AY?si=V-xDWfmDLKyBcdPs)

Elements pakub tehnilise lahenduse probleemidele, millega plokiahela kasutajad igapäevaselt silmitsi seisavad: tehingute hilinemine, privaatsuse puudumine ja asendatavuse oht.

Elements lahendab need probleemid föderaalse plokkallkirjastamise ja konfidentsiaalsete tehingute kasutamise abil.

Erinevalt Bitcoini võrgustikust ei sõltu plokkide allkirjastamise protsess elementides dünaamilistest liikmesuse mitmepoolsetest allkirjadest (DMMS) ja töötõenditest (PoW). Selle asemel kasutab Elements allakirjutanute tugevat föderatsiooni, mida nimetatakse plokksigneerijateks, kes saavad plokke usaldusväärselt ja õigeaegselt allkirjastada ja luua. See kõrvaldab PoW-töötlemisprotsessi tehinguviivituse, mille juhusliku poissoni jaotuse tõttu on plokkide ajavarieeruvus suur. Liitplokkide allkirjastamise protsessiga saavutatakse usaldusväärne plokkide loomine, ilma et oleks vaja kolmanda osapoole usaldust.

Elements võib toimida teise plokiahela, näiteks Bitcoini, kõrvalahelana või iseseisva plokiahelana, mis ei sõltu teistest võrkudest.

Kui seda kasutatakse kõrvalahelana, sisaldab tugev föderatsioon ka liikmeid, kes võimaldavad varade turvalist ja kontrollitud ülekandmist peamise ahela ja elementide kõrvalahela vahel. Varade kontrollitud ülekandmist nimetatakse föderaalseks 2-suunaliseks Pegiks ja liikmeid, kes täidavad varade ülekandmise rolli, nimetatakse valvuriteks.

Elements-võrgustiku toimimisega seotud protsessid ja võrgustikus osalejate rollid on olulised, et mõista, kuidas Elements töötab.

Olenemata sellest, kas see on rakendatud kõrvalahelana või iseseisva plokiahelana, kasutab Elements plokkide tootmiseks plokkide allkirjastajate tugevaid föderatsioone.

### Tugevad föderatsioonid

Elements kasutab konsensusmudelit, mille esimesena pakkus välja Blockstream, mida nimetatakse tugevaks föderatsiooniks. Tugev föderatsioon ei vaja töö tõestamist (Proof of Work, PoW) ja tugineb selle asemel vastastikku usaldamatute osalejate (nn funktsionääride) kollektiivsetele tegevustele.

Tugeva föderatsiooni raames võib funktsionäär täita järgmisi rolle: Blokeerijad ja valvurid. Blokisignaatoreid on vaja, kui te kasutate elemente kas sidechaini või eraldiseisva plokiahela režiimis, samas kui valvurid on vajalikud ainult sidechaini seadistuses.

Tugeva föderatsiooni liikme tegevused on jagatud kahe erineva rolli vahel, et suurendada turvalisust ja piirata kahju, mida ründaja saab tekitada.

Kombineerituna võimaldab nende osalejate roll Elementsil pakkuda nii kiiret plokkide loomist (kiirem ja lõplik tehingu kinnitamine) kui ka tagatud, ülekantavaid varasid (teise plokiahelaga otseselt seostatavad varad).

Saate lugeda Strong Federations valge paber siin: https://blockstream.com/strong-federations.pdf

### Blokeeri allakirjutajad

Plokiahelat nagu Bitcoini plokiahelat laiendatakse, kui igaüks, kes moodustab osa ploki allkirjastajate dünaamilisest rühmast, laiendab ahelat, tõendades, et töö on kulutatud. Kogumi dünaamiline olemus toob kaasa sellistele süsteemidele omased latentsusprobleemid.

Kasutades fikseeritud allkirjastajate kogumit, asendab föderaalne mudel dünaamilise kogumi teadaoleva kogumi, mitme allkirja skeemiga. Plokiahela laiendamiseks vajalike osalejate arvu vähendamine suurendab süsteemi kiirust ja skaleeritavust, samal ajal kui kõigi osapoolte poolne valideerimine tagab tehinguloo terviklikkuse.

Liitplokkide allkirjastamine koosneb mitmest etapist:


- 1. samm - plokkide allkirjastajad esitavad kõigile teistele osalevatele plokkide allkirjastajatele kandidaadiblokid ringkäigu korras.
- 2. samm - iga ploki allkirjastaja annab oma kavatsusest märku, andes eelnevalt nõusoleku antud plokikandidaadi allkirjastamiseks.
- 3. samm - Kui eelkohustuse antud künnis on täidetud, allkirjastab iga ploki allkirjastaja ploki.
- 4. samm - Kui allkirja künnis (mis võib erineda 3. sammu künnisest) on täidetud, võetakse plokk vastu ja saadetakse võrku. Tugev föderatsioon on saavutanud konsensuse viimase tehingubloki suhtes.
- Samm 5 - Järgmine plokk esitatakse järgmise plokkide allkirjastaja poolt ja protsess kordub.

Kuna Tugeva föderatsiooni plokkide genereerimine ei ole tõenäosuslik ja põhineb kindlal allakirjutajate hulgal, ei toimu kunagi mitme ploki ümberkorraldusi. See võimaldab oluliselt vähendada tehingute kinnitamisega seotud ooteaega. Samuti kaotab see stiimuli kaevandada kasumit (st plokkide tasu) ja asendab selle stiimuliga osaleda produktiivselt võrgus, kus kõigil osalejatel on sama ühine eesmärk: tagada võrgu jätkuv toimimine kõigile kasulikul viisil. See teeb seda ilma üheainsa tõrkepunkti või kõrgema usaldusnõude kehtestamiseta.

### Elements as a Sidechain - Watchmen and the Federated 2-Way Peg

Kõrvalahelana tegutsedes on mõnedel Tugeva Föderatsiooni liikmetel täita täiendav roll, nimelt valvurite roll. Valvurid vastutavad varade ülekandmise eest elementide kõrvalahelasse ja sealt välja, mis on tuntud kui "Peg-In" ja "Peg-Out" protsessid.

Selleks, et külgahela toimiks usaldusväärselt, peab see võimaldama osalejatel kontrollida, et varade pakkumine on kontrollitud ja kontrollitav. Elements sidechain kasutab 2-Way Federated Peg'i, et võimaldada varade kahesuunalist ülekandmist Elements blockchaini sisse ja sealt välja. See vastab tõendatava emiteerimise ja ahelatevaheliste ülekannete nõuetele.

Federated 2-way Peg funktsioon võimaldab vara olla koostalitlusvõimeline teiste plokiahelate ja esindab teise plokiahela algupärast vara. Oma plokiahelat teise plokiahelaga sidudes saate laiendada põhiahelate võimalusi ja ületada mõned selle loomupärased piirangud.

Kõrgetasemeliselt toimuvad ülekanded sidechaini, kui keegi saadab põhiahelas olevad varad aadressile, mida kontrollib mitme allkirjaga Watchmeni rahakott. See külmutab sisuliselt varad peahelas. Watchmen valideerib seejärel tehingu ja vabastab sama summa seotud vara sidechainis. Vabastatud varad saadetakse sidechaini rahakotti, mis suudab tõestada, et on õigus algsetele mainchaini varadele. See protsess liigutab varad tegelikult emaahelast kõrvalahelasse.

Selleks, et kanda varasid tagasi peahelasse, teeb kasutaja spetsiaalse peg-out-tehingu sidechainis. Seda tehingut kontrollivad valvurid, kes seejärel allkirjastavad tehingu kulutused nende poolt kontrollitavast mitme allkirjaga rahakotist peahelas. Enne kui peahela tehing muutub kehtivaks, peab alla kirjutama künnise võrra rohkem osalejaid föderatsioonis. Kui valvurid saadavad vara tagasi peahelasse, hävitavad nad ka vastava summa sidechainis, viies seega vara tegelikult plokiahelate vahel üle.

## Elementide seadistamine ja käivitamine

<chapterId>cc806e5a-81ab-457b-9531-9f863120a019</chapterId>

![Video](https://youtu.be/Frr_OjTEPAM?si=iq5XonJyQk8S5OAu)

Kuna Elements põhineb Bitcoini koodibaasil, on toimiva võrgu komponendid väga sarnased.

Elements node'i tarkvara ise kannab nime `elementsd` ja see töötab kasutaja masinas deemonina. Daemon (või teenus Windowsis) on programm, mis töötab taustateenusena ilma sisselogitud kasutaja otsese kontrollimiseta.

Märkus: Kogu käesolevas dokumendis viidatakse elementsd-le alati kui daemon-versioonile, kuid kõike saab teha ka elements-qt-ga, tingimusel, et serveri valik on lubatud.

Elements'i deemon ühendub teiste võrgusõlmedega, et vahetada tehingu- ja plokkide andmeid, valideerides ja laiendades võrgu plokiahela kohalikku koopiat.

Elements tarkvara koosneb ka kliendiprogrammist `elements-cli`, mis võimaldab saata käsurealt RPC (Remote Procedure Call) käske elementsd-le. Seda saab kasutada näiteks rahakoti saldo pärimiseks, tehingu- või plokiandmete vaatamiseks või tehingu edastamiseks. See seadistus peaks olema tuttav kõigile, kes on kasutanud Bitcoini ekvivalente; bitcoind ja bitcoin-cli.

Kuna Elements-sõlme saab konfigureerida käivitamisel või konfiguratsioonifaili kaudu parameetrite sisestamisega, on võimalik, et ühes ja samas masinas töötab rohkem kui üks instants. See on kasulik testimise ja arenduse eesmärgil, kuna saate luua oma kohaliku võrgu ühes masinas, kusjuures igal Elements-sõlmel on oma koopia plokiahela andmetest, ta saab hallata oma kinnitamata kehtivate tehingute kogumit ja kuulata RPC-päringuid erinevatel sadamatel.

### Elementide koodihoidla ja kogukond

Elements on avatud lähtekoodiga projekt ja selle lähtekood on leitav Elements GitHubi repositooriumist aadressil https://github.com/ElementsProject/elements. See repositoorium sisaldab programmide elementsd ja elements-cli lähtekoode koos toetavate paigaldus- ja ehitustööriistadega, testide komplektiga ja mõningase juhenddokumendiga.

Koodihoidla täienduseks on ka veebileht https://elementsproject.org, mis on kogukonnale suunatud ressurss, mis sisaldab selgitusi selle kohta, mis on Elements, kuidas see töötab, ja põhjalikku õpetusraamatut. Õpetus keskendub Elements'i tundmaõppimisele käsurea näidete abil ja näitab, kuidas ehitada selle peal lihtsaid töölaua- ja veebirakendusi. Veebilehel on loetletud ka Elements'i kogukonna populaarsed arutelufoorumid ja see on ise GitHubis, mis võimaldab kogukonna panustust veebilehe sisusse.

Elements'i käivitamiseks oma masinas peate esmalt kloonima (alla laadima koopia) lähtekoodi, paigaldama kõik sõltuvused, mis koodil on, ja lõpuks ehitama daemoni ja kliendi käivitatavad failid. Seejärel on Elements tarkvara valmis konfigureerimiseks ja käivitamiseks.

## Sõlmede ja võrkude konfigureerimine

<chapterId>df1ec0aa-84ea-4149-af7a-b4523d67e1d9</chapterId>

Elements-sõlme saab käivitamisel üle anda konfiguratsiooni seaded, et muuta selle tööd, andmete valideerimist, ühendamist teiste sõlmedega ja plokiahela andmete initsialiseerimist.

Seaded laaditakse kas määratud failist `elements.conf` või antakse parameetrina üle käsurea kaudu.

Mõningaid asju saab nende parameetrite abil muuta:


- Eraldi plokiahela rakendustes kasutatava vaikimisi vara nimi.
- Loodud esialgse vara number.
- Vara, mida kasutatakse tehingutasude maksmisel võrgus.
- Plokiahela andmefailide salvestuskoht.
- RPC-volitused, mida kasutatakse Bitcoini sõlme ühendamiseks.
- Künnis "n m", mida tuleb täita, ja kehtivad avalikud võtmed, mis võivad plokke allkirjastada.
- Skript, mis vajab rahuldamist, et kanda varasid sidechaini sisse ja sealt välja.
- Kas ühendada Bitcoini sõlme külgahelana või mitte.

Paljud neist moodustavad osa võrgu konsensusreeglitest, seega on oluline, et neid rakendataks käivitamisel kõigis sõlmedes. Mõnda saab muuta pärast ahela initsialiseerimist, kuid mõned tuleb fikseerida pärast nende kasutamist ahela initsialiseerimiseks.

Parameetrite kasutamist käsitletakse hiljem kursuse jooksul, kui need on seotud iga jaotisega.

### Põhilised toimingud käsurea abil

Sellel kursusel näidatakse näiteid, mis kasutavad programmi `elements-cli`, et teha RPC-kõnesid ühele või mitmele elemendisõlmele. Seda tehakse terminalisessioonist ja selleks, et käsud oleksid lühemad, kasutatakse `alias`. Selle konventsiooni järgi, kui näete midagi sellist nagu järgmised käsud:

```bash
e1-dae
e1-cli getnewaddress
```

`e1-dae` ja `e1-cli` on tegelikult tüpograafiline otsetee, mis kasutab terminali `alias` funktsiooni. `e1-dae` ja `e1-cli` tegelikult asendatakse käsu täitmisel ja käivitatav käsk on sarnane:

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir1
$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir1 getnewaddress
```

Eespool näeme üleskutset Elements deemon'i käivitamiseks ja üleskutset elements-cli programmidele, mis asuvad kataloogis `$HOME/elements/src`, ning parameetri `datadir` väärtust. Parameeter `datadir` võimaldab meil öelda deemonile ja kliendiinstantsidele, kus asuvad nende konfiguratsioonifailid ja deemoni puhul, kus hoida oma plokiahela koopiat. Kuna nad jagavad config-faili, saab klient teha RPC-kõnesid daemonile.

Kui käivitame ülaltoodud käsu uuesti, kuid erineva `datadir` väärtusega, saame käivitada rohkem kui ühe Elements'i instantsi, igaühel oma eraldi plokiahela koopia ja konfiguratsiooni seaded. Selle kokkuleppe järgi kasutame kursuses aliase `e2-dae` ja `e2-cli`, et viidata teistsugusele datadir kataloogile kui e1 oma. Nii et ülaltoodud näide meie teise `e2` instantsi jaoks oleks:

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir2
$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir2 getnewaddress
```

See võimaldab meil teostada igasuguseid toiminguid, nagu näiteks varade vahetamine sõlmede vahel, varade väljastamine ja sama võrgu erinevate sõlmede vaheliste konfidentsiaalsete tehingute sokutamise kontrollimine.

# Elementi kasutamine Praktiline kasutusjuhtum

<partId>3f31a30a-957a-4813-b5fe-5dccbb5366f3</partId>

## Konfidentsiaalsed tehingud

<chapterId>263b1c5b-59ed-49e7-b811-95c354f41eae</chapterId>

![Video](https://youtu.be/-by2xBtXQeE?si=7bLo_geGn3qh7MXN)

Selles jaotises saate teada, kuidas kasutada Elementide funktsiooni Konfidentsiaalsed tehingud.

Kõik Elements'i aadressid on vaikimisi pimendatud, kasutades konfidentsiaalset tehingut, mis hoiab ülekantud varade summa ja tüübi nähtavana ainult tehingus osalejatele (ja neile, kellele nad otsustavad pimendamisvõtme avaldada), tagades samas krüptograafiliselt, et münte ei saa kulutada rohkem, kui on saadaval.

### Konfidentsiaalsed aadressid ja konfidentsiaalsed tehingud

Vaikimisi luuakse uus aadress Elementsis käsuga `getnewaddress` konfidentsiaalse aadressina.

Konfidentsiaalsete tehingute demonstreerimiseks laseme e2-l endal raha saata ja seejärel proovime vaadata e1-i tehingut. See demonstreerib tehingute konfidentsiaalset olemust Elementsis.

Iga uus aadress, mille Elements-sõlm genereerib, on vaikimisi konfidentsiaalne. Me saame seda demonstreerida, kui paneme e2 uut aadressi genereerima.

```
e2-cli getnewaddress
```

Pange tähele, et aadress algab numbriga e1. See tähistab seda kui konfidentsiaalset aadressi. Aadressi üksikasjalikum uurimine käsuga getaddressinfo näitab aadressi üksikasju.

```
e2-cli getaddressinfo <address>
```

Näete, et on olemas omadus confidential_key, mis ütleb meile, et tegemist on konfidentsiaalse aadressiga.

Konfidentsiaalne_võti on avalik pimendav võti, mis lisatakse konfidentsiaalsele aadressile. See on põhjus, miks konfidentsiaalne aadress on nii pikk.

Samuti on sellega seotud mittekonfidentsiaalne aadress. Kui soovite kasutada tavalisi, mittekonfidentsiaalseid tehinguid elementides, tuleks varad saata sellele aadressile, mitte sellele, millel on eesliide lq1.

Nüüd saame lasta e2-l saata mõned rahalised vahendid loodud aadressile. See näitab hiljem, et e1 ei saa tehingu üksikasju vaadata, kuna ta ei ole üks tehingu osapooltest.

```
e2-cli sendtoaddress <address>
```

Pange tähele tehingu ID. Kinnitage tehing.

```
e2-cli -generate 101
```

Vaadates tehingut, mille puhul e2 saatis endale raha, e2 enda vaatenurgast.

```
e2-cli gettransaction <txid>
```

Tehingu üksikasju ülespoole kerides näete, et e2 saab vaadata nii saadetud ja saadud summasid kui ka ülekantud vara. Samuti näete amountblinder- ja assetblinder-omadusi, mida kasutatakse üksikasjade pimestamiseks teiste tehingus mitteosalevate sõlmede eest.

Sama tehingu üksikasjade kontrollimiseks e1-st peame kõigepealt saama tehingu töötlemata andmed.

```
e1-cli getrawtransaction <txid>
```

See tagastab töötlemata tehingu üksikasjad. Kui te vaatate vout sektsiooni sees, näete, et seal on kolm instantsi. Esimesed kaks instantsi on saamise ja muutmise summad ning kolmas on tehingutasu. Nendest kolmest summast on tasu ainus, mille väärtust on võimalik näha, kuna tasu ise on elementides alati pimendamata.

### Pimestavad võtmed

Esimesed kaks vout-osa näitavad väärtuse summade "pimendatud vahemikke" ja kulukohustuste andmeid, mis on tõendiks tegeliku tehingu summa ja vara liigi kohta.

Isegi kui me impordiksime e2 privaatvõtme e1-i rahakotti, ei saaks ta ikkagi näha tehtavate tehingute summasid ja varade tüüpi, sest tal ei ole endiselt teadmisi e2-i kasutatavast pimendavast võtmest. Tõestame seda, importides e2 rahakoti kasutatava privaatvõtme e1 rahakotti. Kõigepealt peame eksportima võtme e2-st

```
e2-cli dumpprivkey <address>
```

Seejärel importige see e1-sse.

```
e1-cli importprivkey <privkey>
```

Nüüd saame tõestada, et e1 ei näe ikka veel väärtusi.

```
e1-cli gettransaction <txid>
```

Tõepoolest, see näitab tx-summana 0, kuigi tegelikult oli see 1.

Selleks, et näha tegelikku, joonistamata väärtust, vajame pimendamisvõtit. Selleks ekspordime kõigepealt pimendamisvõtme e2-st.

```
e2-cli dumpblindingkey <address>
```

Seejärel importige see e1-sse.

```
e1-cli importblindingkey <address> <blinding key>
```

Nüüd, kui me saame tehingu andmed e1-st.

```
e1-cli gettransaction <txid>
```

See näitab, et koos imporditud pimendava võtmega saame nüüd vaadata tehingu tegelikku väärtust 1.

Selles jaotises nägime, et pimendava võtme kasutamine peidab tehingu varade summa ja liigi ning et õige pimendava võtme importimisega saame need väärtused paljastada. Praktilises kasutuses võib pimendamisvõtme anda näiteks audiitorile, kui on vaja kontrollida osapoole valduses olevate varade summasid ja liike. Elements'i konfidentsiaalsete tehingute funktsioon võimaldab ka "vahemiktõendamist". Vahemiku tõendamisega saab tõestada, et varade summa jääb teatavasse vahemikku, ilma et oleks vaja tegelikku summat avaldada.

Samuti nägime, et konfidentsiaalsed tehingud on vabatahtlikud, kuid vaikimisi on need uue aadressi loomisel lubatud.

See on kõik selle tunni jaoks; palju õnne viktoriinis ja kohtumiseni järgmises õppetunnis!

## Väljaantud varad

<chapterId>c33c7020-5975-457a-99db-4f8b90d1fa1c</chapterId>

![Video](https://youtu.be/XnY4WZUNSs4?si=dG8I5OoSh_0EBdvL)

Selles jaotises saate teada, kuidas kasutada Elements'i funktsiooni "Väljastatud varad".

Väljastatud varad võimaldavad väljastada ja üle kanda mitut liiki varasid Elements-võrgustiku osalejate vahel. Iga võrgusõlm võib emiteerida oma vara. Emiteeritud varad võivad esindada mis tahes vara, sealhulgas kupongid, kupongid, valuutad, hoiused, võlakirjad, aktsiad jne, vahetatavat omandiõigust. Issued Assets avab ukse usalduseta börside, optsioonide ja muude täiustatud arukate lepingute loomiseks, mis hõlmavad ise emiteeritud varasid.

Väljaantud vara saab samuti kasu konfidentsiaalsetest tehingutest ja neid saab uuesti välja anda igaüks, kes omab sellega seotud sümbolit.

Esimese sammuna vajame ligipääsu kahele elemendisõlmele, mida nimetame e1 ja e2. Nende sõlmede plokiahelad on nullistatud ja vaikimisi vara nende vahel jagatud.

Need kaks sõlme asuvad samas kohalikus võrgus ja on omavahel ühendatud ning seetõttu jagavad samu tehinguid oma tehingumempoolis ja identsed plokiahelad. Kuigi nad töötavad samas masinas, tasub märkida, et nad ei jaga samu tegelikke plokiahelafaile. Iga sõlm haldab oma plokiahela kohalikku koopiat, mis sisaldab sama tehingulugu, sest nad on konsensuses ja järgivad üksteisega samu protokollireegleid.

Alustame sellega, et kontrollime iga sõlme vaadet olemasolevatele varade emissioonidele võrgus.

Selleks kasutatakse käsku listissuances.

```
e1-cli listissuances
e2-cli listissuances
```

Nagu näete, näitavad mõlemad sõlmed sama väljastamise ajalugu. Mõlemad näitavad ühte vara, 21 miljoni Bitcoini esialgset emissiooni, mis loodi ahela initsialiseerimisel. Ülaltoodud käsu käivitamise tulemustes on näha vara hex id ja ka varale määratud silt, milleks on "bitcoin".

Väärib märkimist, et vaikimisi varale antakse ahela initsialiseerimisel alati silt. Kui te väljastate oma varasid, saate neile ise sildid määrata, mida me peagi teeme. Enne kui me saame seda teha, peame väljastama oma vara.

Me laseme e1-l väljastada uue vara. Selleks kasutatakse käsku issueasset.

```
e1-cli issueasset 100 1 false
```

`issueasset` võtab vastu 3 parameetrit.

Uue vara summa, mida emiteerida, me oleme kasutanud 100. Loomiseks vajalike žetoonide kogus (žetoonide abil saab vara koguseid uuesti välja anda), millest me valisime 1. Viimane parameeter ütleb Elementsile, et luua vara emissioon kas pimendatud või mittepimendatud kujul. Me kasutame unblinded, kuna tahame emissioonisummasid e2-st kohe vaadata, seega sisestame false.

Käsu käivitamine tagastab andmed väljaandmise kohta. Nende hulka kuuluvad tehingu id, millest saate võtta koopia hilisemaks kasutamiseks, vara unikaalne heksaväärtus ja vara sümboli unikaalne heksaväärtus.

Looge plokk väljaandmistehingu kinnitamiseks.

```
e1-cli -generate 1
```

Käivitage käsk "listissuances" uuesti e1 suhtes.

```
e1-cli listissuances
```

See näitab meile, et e1 on nüüd teadlik 2 emissioonist, Bitcoini esmasest emissioonist ja meie äsja emiteeritud varast, millest me näeme 100. Pange tähele uue vara kuuekohalist väärtust ja seda, et sellega ei ole seotud vara märgistus, nagu on bitcoini emissiooni puhul.

Kontrollige uuesti e2 teadaolevate emissioonide nimekirja.

```
e2-cli listissuances
```

See näitab meile, et e2 ei ole teadlik e1 tehtud varaemissioonist. Ta näeb ainult bitcoini esialgset emiteerimist, mida ta juba nägi.

Selle põhjuseks on see, et e2 ei tea ja ei jälgi aadressi, kuhu uus vara saadeti, kui e1 selle väljastas.

Tasub märkida, et kuigi e2 ei näe emissiooni ennast, võib e1 siiski saata e2-le osa varast. Uus vara ilmub siis e2 rahakotis vaba saldona, kuigi ta ei ole teadlik algsest emissioonist.

Selleks, et e2 saaks näha tegelikku väljastamist (ja seega väljastatud summat), peame lisama aadressi e2-sse jälgitava aadressina.

Selleks peame välja selgitama aadressi, kuhu vara saadeti. Selleks kasutame varem kopeeritud tehingu id-d ja laseme e1-l välja otsida selle tehingu andmed, et saaksime leida õige aadressi, mille lisada e2 rahakoti jälgimisnimekirja.

```
e1-cli gettransaction <the-issuance-transaction-id>
```

Kui kerite tehinguandmete kuuekohalistest andmetest ülespoole, näete aadressi, mis sai 100 meie uut vara, mis on identifitseeritud selle kuuekohalise väärtuse järgi.

Võtke aadress ja kopeerige see, et saaksime selle e2-sse importida.

Nüüd impordime selle aadressi e2-sse. Selleks kasutame käsku importaddress.

```
e2-cli importaddress <the-issued-to-address>
```

Kui me nüüd kontrollime e2 emissioonide nimekirja.

```
e2-cli listissuances
```

Näete, et meie äsja väljastatud vara on nüüd nimekirjas. E2-sõlm suudab määrata ka emiteeritud vara summa koos sellega seotud märgise summaga, kuna tegemist oli pimendamata emissiooniga. Et võimaldada vara ID ja nime seostamise kasutamist elementides, peatage kõigepealt elemendid.

```
e1-cli stop
```

Seejärel käivitage see uuesti lisaparameetriga, mis kaardistab vara kuuekohalise väärtuse esitatud märgisele. See võimaldab sõlme kuvada meile andmeid vara kohta inimloetaval kujul. Kui soovite, võite selle lisada elements.conf-i lõppu, siis ei pea te seda argumenti daemonile iga kord käivitamisel lisama. Näiteks:

```
assetdir=5186d0bc8ed15e6ef85571bd2d8070573adf0e06fd4507082694526975ce4f35:My new asset (MNA)
```

Kuid me kasutame siinkohal argumentide meetodit.

```
e1-dae -assetdir=<assetid-here>:<name-of-the-new-asset>
```

Küsitakse uuesti sõlme emissioonide nimekirja.

```
e1-cli listissuances
```

See näitab meile, et vara kuuekohalise väärtuse seostamine selle sildiga toimib. Kontrollime uuesti e2-sõlme emissioonide nimekirja.

```
e2-cli listissuances
```

Näete, et e2-sõlm ei pääse sellele sildile ligi, sest sildid on kättesaadavad ainult sellele sõlmpunktile, mis need määras. Tõepoolest, me võime määrata samale varakuuteele e2-s teistsuguse sildi kui e1-s. Esmalt peatame e2 sõlme.

```
e2-cli stop
```

Uuesti alustades on meie uue vara kuuekohale määratud teine silt.

```
e2-dae -assetdir=<assetid-here>:<another-name-for-the-new-asset>
```

Emissioonide noteerimine e2-st.

```
e2-cli listissuances
```

Vara sildid on iga sõlme jaoks lokaalsed, ainult vara kuusnurk on teiste võrgusõlmede jaoks äratuntav.

Sildi seostamine varade kuuekohaga on kasulik selliste toimingute tegemisel nagu tehingud ja rahakoti saldo päringud, kuna see võimaldab lühidalt viidata varale. Näiteks kui me tahaksime saata osa meie uuest varast (summa 10) e1-st e2-sse ilma etiketti kasutamata.

Kõigepealt peame saama aadressi, kuhu vara saata.

```
e2-cli getnewaddress
```

Seejärel kasutage käsku sendtoaddress.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <asset-id-here>
```

Kinnitage tehing, genereerides ploki.

```
generate 1
```

Kontrollida, et vara on saadud e2-le.

```
e2-cli getwalletinfo
```

Näeme, et vara on tõepoolest saadud.

Pange tähele, et e2 kaardistab saadud vara kuusnurga ja kuvab selle oma sildi abil. Lihtsam viis sama asja tegemiseks oleks kasutada saatmisel e1-i vara sildi.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <name-of-the-new-asset>
```

Kulisside taga kaardistab Elements kohalikud sildid heksaväärtusteks, et lihtsustada väljastatud varade kasutamist.

Selles jaotises nägime, kuidas varasid välja anda ja märgistada. Järgmises jaotises vaatleme emiteeritud varade taasemiteerimist ja hävitamist.

## Varade taasväljastamine

<chapterId>78751b21-1dc8-4877-a406-e71bc80a95b0</chapterId>

![Video](https://youtu.be/5em79YHtYk0?si=rhponm6Hw9AB6RJp)

Selles jaotises saate teada, kuidas emiteerida rohkem juba emiteeritud vara ja kuidas hävitada teatud kogus emiteeritud vara.

Vajadus vara uuesti emiteerida (luua rohkem) või hävitada teatud kogus vara on midagi, mis tõenäoliselt tekib, kui vara kujutab endast midagi, millel ei ole kindlat varu. See võib kehtida näiteks varade puhul, mis esindavad kullavarusid, mida hoitakse hoidlas; kui kuldühikud liiguvad hoidlasse sisse ja sealt välja, tuleb hoidla varusid esindavat vara vastavalt kohandada üles- või allapoole.

Vara koguse taasväljaandmine eeldab, et sellega seotud märgis, mis loodi koos varaga, kui see algselt välja anti, on selle omanikuks.

Kui luua rohkem vara, See ei ole oluline, mis sõlme välja antud vara esimese koha, nii kaua, kui sõlme, mis on reissuing summa vara see on valduses, mida tavaliselt nimetatakse vara reissuance token. Vaatleme, kuidas algselt luua reissuance token, kuidas seda kasutada vara koguse taasväljaandmiseks ja ka seda, kuidas reissuance tokenit teistele sõlmedele üle anda, et neil oleks samuti õigus vara taasväljaandmiseks.

Meil on vaja juurdepääsu kahele elementide sõlmpunktile, mida me nimetame e1 ja e2. Nende sõlmede plokiahelad on nullistatud ja vaikimisi vara nende vahel jagatud.

Me laseme e1 emiteerida 100 uut vara ja loome sama vara jaoks 1 kordusväljaande märgi. Näite lihtsustamiseks loome emissiooni pimendamata kujul. Niisiis, jätkame ja emiteerime vara ja sellega seotud taasväljaandmise märgi.

```
e1-cli issueasset 100 1 false
```

Pange tähele vara ja ka (taasväljastamise) märgi ID.

Kuna me hiljem väljastame e2-st rohkem varasid, peame märkima tehingu ID, millega vara väljastati, ja kasutama seda selleks, et importida aadress, kuhu vara saadeti.

Kinnitage tehing.

```
e1-cli -generate 1
```

Nüüd kontrollime tehingu üksikasju käsuga gettransaction:

```
e1-cli gettransaction <txid>
```

Kui kerite tehingu andmete kuuekohalistest andmetest ülespoole, näete, et tehingus e1 sai 1 taasväljaandmise märgise ja 100 seotud vara.

Võtke aadressist koopia, et saaksime selle e2-sse importida.

Ja nüüd aadressi importimine e2 rahakotti.

```
e2-cli importaddress <address>
```

Nüüd näeme, et nii e1 kui ka e2 on teadlikud vara väljaandmisest.

```
e1-cli listissuances
e2-cli listissuances
```

Praegu on e1-l varade summa ja 1 taasväljaandmise märgis, kuid e2-l ei ole.

```
e1-cli getwalletinfo
```

Pange tähele ka seda, et e1 omab varasemast vähem vaikimisi varasid, sest ta maksis väikese summa tehingutasude katteks. Selle summa peab e1 sisse nõudma siis, kui loodud plokk on üle 100 ploki sügavusel laagerdunud.

```
e2-cli getwalletinfo
```

Kuna e1 omab taasväljaandmise märgendit, võib ta seda uuesti välja anda rohkem. Selleks kasutatakse käsku reissueasset. Laseme e1 uuesti välja anda veel 100 vara.

```
e1-cli reissueasset <asset-id> 100
```

Uuesti väljaandmise kontrollimine töötas.

```
e1-cli getwalletinfo
```

Näete, et e1 omab nüüd 200 vara, nagu oodatud.

Kuna e2-l ei ole käes taasväljaandmise märgi summat, saavad nad veateate, kui nad üritavad vara uuesti välja anda.

```
e2-cli reissueasset <asset-id> 100
```

Pange tähele veateadet.

Me saame vaadata uuesti väljastamise üksikasju e1-st, kasutades käsku listissuances.

```
e1-cli listissuances
```

Pange tähele lipukest `is_reissuance`.

Kui me nüüd saadame e2-le summa, mis on ümberväljastamise märgis, saavad nad ise summa vara ümberväljastada. Kõigepealt vajame aadressi, kuhu seda saata. Tasub märkida, et saldode saatmisel ja kuvamisel käsitletakse reissuance tokenit samamoodi nagu mis tahes muud vara elementides ja et seda saab samuti jaotada väiksemateks nimiväärtusteks nagu mis tahes muud vara, seega ei pea me e2-le saatma 1 reissuance tokenit, et ta saaks vara uuesti välja anda. Piisab mis tahes nimiväärtusest. E2 jaoks aadressi genereerimine, et saada taasväljaandmise märgis.

```
e2-cli getnewaddress
```

Seejärel saadetakse osa RIT-i e1-st e2-le.

```
e1-cli sendtoaddress <address-of-e2> 0.1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Kinnitage tehing.

```
e1-cli -generate 1
```

Nüüd näeme, et e2 hoiab 0,1, mis talle saadeti.

```
e2-cli getwalletinfo
```

See tähendab, et e2 saab nüüd uuesti emiteerida rohkem tema rahakotis oleva RITiga seotud vara. Me laseme e2-l uuesti välja anda 500 vara.

```
e2-cli reissueasset <asset-id> 500
```

Kontrollida uuesti väljaandmise tulemust.

```
e2-cli getwalletinfo
```

Näete, et e2 hoiab nüüd uuesti väljastatud summat oma rahakoti saldos ja et RIT ise ei ole vara uuesti väljastamise käigus tarbitud.

Vara koguse hävitamist võib teha igaüks, kellel on vähemalt hävitatav kogus, see ei ole reguleeritud taasväljastamise märgiga.

```
e2-cli destroyamount <asset-id>
e2-cli getwalletinfo
```

Selles jaotises nägime, kuidas vara välja anda ja kuidas kasutada vara väljaandmise käigus valikuliselt loodud taasväljaandmise märgendit. Samuti nägime, kuidas reissuance tokeni ülekandmine on sama lihtne kui mis tahes muu vara ülekandmine ning et reissuance tokeni mis tahes koguse omamine annab omanikule õiguse emiteerida rohkem seotud vara. Seetõttu on väga oluline kontrollida, kellel on teie võrgus juurdepääs reissuance-tokenitele. Me nägime ka, kuidas hävitada varakogus ja et seda protsessi ei kontrollita reissuance-tokenni valdamisega.

# Elementide Föderatsioon

<partId>173a2440-0203-4dcc-8e2b-f8fa2cc8d3ca</partId>

## Plokkide allkirjastamine

<chapterId>c47b217e-db14-4843-a66f-3e5f3a00a808</chapterId>

![Video](https://youtu.be/kxWX91fCnus?si=KItm_Am3_RrBcLBN)

Elements toetab föderaalset allkirjastamismudelit, mis võimaldab teil määrata, kui palju tugevaid föderatsiooni liikmeid peab pakutud plokki allkirjastama, et saada kehtiv plokk.

Varem oleme näiteks lihtsuse huvides loonud plokke käsuga `generate`, mis ei ole pidanud vastama mitme allkirja nõudele, et loodud plokid oleksid võrgustiku poolt kehtivana aktsepteeritud.

Me seadistame oma sõlmed nii, et need nõuavad 2-of-2 multisig ploki loomist. Seda seadistatakse parameetri signblockscript abil, mille saab lisada konfiguratsioonifaili või edastada sõlme käivitamisel. Selleks, et selle parameetriga ahelat initsialiseerida, peame kõigepealt koostama skripti, millest see koosneb.

Teeme seda mõne olemasoleva sõlme abil, salvestame nende väljastatud andmed ja seejärel kustutame ahela, et saaksime selle uuesti käivitada, kasutades meie signblockscript parameetrit. See on vajalik, kuna skript moodustab osa võrgu konsensusreeglitest ja see tuleb määrata ahela initsialiseerimisel. Seda ei saa hiljem juba olemasolevale ahelale lisada.

Meil on vaja juurdepääsu kahele elementide sõlmpunktile, mida me nimetame e1 ja e2. Nende sõlmede plokiahelad on nullistatud ja vaikimisi vara nende vahel jagatud.

Veenduge, et parameeter con_max_block_sig_size on teie elements.conf-failis seatud kõrgele väärtusele, vastasel juhul ei õnnestu plokkide allkirjastamine hiljem selles jaotises. Me oleme selle õpetuse jaoks seadnud con_max_block_sig_size=2000.

Kuna me lähtestame plokiahelat ja pühkime e1 ja e2 seotud rahakotid, peame võtma koopia aadressidest, avalikest võtmetest ja privaatvõtmetest, mida kasutame plokkide allkirjastamise skripti genereerimiseks, et saaksime neid hiljem kasutada.

Kõigepealt on meil vaja, et iga plokksõlm, millest saab plokksõlm, genereeriks uue aadressi, millest tuleb võtta koopia.

```
e1-cli getnewaddress
e2-cli getnewaddress
```

Seejärel peame aadressidest eraldama avalikud võtmed ja märkima need hilisemaks kasutamiseks.

```
e1-cli getaddressinfo <e1-address>
e2-cli getaddressinfo <e2-address>
```

Seejärel eraldage privaatvõtmed, mida me hiljem uuesti impordime, et sõlmed saaksid plokid allkirjastada pärast meie plokiahela ja rahakoti andmete uuesti initsialiseerimist.

```
e1-cli dumpprivkey <e1-address>
e2-cli dumpprivkey <e2-address>
```

Nüüd peame looma lunastusskripti, millel on 2 2-st mitme allkirja nõuded. Selleks kasutame käsku createmultisig ja anname esimeseks parameetriks 2 ning seejärel anname kaks avalikku võtit. Need on need võtmed, mille omandiõigust on vaja hiljem tõestada, kui plokk luuakse.

Kumbki sõlm, kas e1 või e2, võib luua multisignaali.

```
e1-cli createmultisig 2 '["<e1-pubkey>", "<e2-pubkey>"]'
```

See annab meile meie redeemscripti, mille saate kopeerida hilisemaks kasutamiseks.

Nüüd tuleb olemasolevad plokiahelad ja rahakoti andmed kustutada, et saaksime alustada uuesti uue signblockscriptiga kui osaga ahela konsensusreeglitest. Seetõttu oli meil vaja varem võtta koopia mõnest andmestikust, näiteks privaatvõtmetest, mida uues ahelas kasutatakse plokkide allkirjastamiseks. Seda tuleb teha enne jätkamist.

Kui meie olemasolevad rahakoti ja ahela andmed on kustutatud, saame nüüd käivitada oma sõlmed ja lasta neil initsialiseerida uus kett, kasutades parameetrit signblockscript. Anname parameetrile -evbparams=dynafed:0::::, et keelata dynafed-i aktiveerimine, sest me ei vaja seda täiustatud funktsiooni selle näite jaoks.

```
e1-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
e2-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
```

Nüüd peame importima varem salvestatud privaatvõtmed, et meie sõlmed saaksid allkirjastada ja aidata lõpule viia kõik pakutud plokid.

```
e1-cli importprivkey <e1-priv-key>
e2-cli importprivkey <e2-priv-key>
```

Käsu generate kasutamine peaks nüüd viga tegema, kuna see ei vasta meie sõlmede poolt nüüd jõustatavatele plokkide allkirjastamise reeglitele.

```
e1-cli -generate 1
```

Uue ploki pakkumiseks võib kumbki sõlm kutsuda käsku getnewblockhex. See tagastab uue ploki kuuekohalise väärtuse, mis tuleb allkirjastada, enne kui meie võrgu sõlmed seda aktsepteerivad.

```
e1-cli getnewblockhex
```

Pidage meeles, et käsk lihtsalt loob kavandatud ploki, mitte ei genereeri seda.

Selle kinnitamiseks näeme, et praegu ei ole meie plokiahelas ühtegi plokki.

```
e1-cli getblockcount
```

Kui me proovime esitada blokki kuus ilma selle allkirjastamiseta kõigepealt.

```
e1-cli submitblock <block-hex>
```

Me saame teate, et plokitõend on kehtetu. See on tingitud sellest, et 2 osapoolt ei ole seda veel allkirjastanud kahest nõutavast osapoolest.

Nii et paneme e1 kavandatavale plokile alla kirjutama.

```
e1-cli signblock <block-hex>
```

Laske e2-l kuusikule alla kirjutada.

```
e2-cli signblock <block-hex>
```

Pange tähele, et e2 ei allkirjasta väljundit, mis on loodud e1 poolt pakutud ploki allkirjastamisel. Nad mõlemad allkirjastavad pakutud plokki kuus üksteise tulemustest sõltumatult.

Nüüd tuleb meil kombineerida e1 ja e2 plokksignatuurid. Kumbki sõlme saab seda teha, nad vajavad ainult teise sõlme allkirjastatud plokksignatuuri.

```
e1-cli combineblocksigs <block-hex> '["<signed-hex-from-e1>", "<signed-hex-from-e2>"]'
```

Näete, et käsk combineblocksigs väljastab allkirjastatud ploki kuueksajaotuse ning staatuse complete, mis ütleb meile, et ploki kuueksajaotus on valmis esitamiseks.

Nüüd saab kumbki sõlm esitada valmis plokk kuus. Me laseme e1 seda teha.

```
e1-cli submitblock <combined-signed-hex>
```

Kontrollida, et esitamine oli kehtiv.

```
e1-cli getblockcount
e2-cli getblockcount
```

Näete, et nii e1 kui ka e2 on ploki kehtivaks tunnistanud ja lisanud selle oma plokiahela kohalike koopiate tippu.

Protsessi kokkuvõttes. Selles osas on meil:


- Kavandatud plokk.
- Iga sõlmpunkt pidi sellele alla kirjutama.
- Kombineeritud allkirjad.
- Kontrollida, et allkirjad on kehtivad ja vastavad ahela lunastuskünnisele.
- Esitatud plokk.

Iga võrgusõlm valideeris ploki ja lisas selle oma plokiahela kohalikku koopiasse.

### Plokkide paigaldamine

Kuigi protsess tundub esialgu keeruline, on plokkide allkirjastamise järjekord elementides alati sama ja algseadistust tuleb teha ainult üks kord:

1. Esialgne seadistamine (tehakse üks kord)

2. Luuakse mitme allkirjaga aadress nimega `signblockscript`, kasutades föderaalsete blokeeritud allkirjastajate avalikke võtmeid.

3. Selle lunastusskripti kasutatakse uue plokiahela käivitamiseks.

4. Plokkide tootmine (käimas)

5. Ettepanekud genereeritakse ja vahetatakse allkirjastamiseks.

Kui kavandatavale plokile on alla kirjutanud teatav arv allakirjutanuid, ühendatakse see ja esitatakse võrgustikule. Kui see vastab ahela `signblockscript` kriteeriumidele, aktsepteerivad sõlmed selle kehtiva plokina.

## Element kui külgahela

<chapterId>432d7a65-255f-44a3-8b38-78508202cb37</chapterId>

![Video](https://youtu.be/egYzj4N8CB8?si=v7_-IXsjHPE-ARDe)

Elements on avatud lähtekoodiga, üldotstarbeline plokiahela platvorm, mida saab ka olemasoleva plokiahela, näiteks Bitcoini külge liita. Kui Elements on seotud teise plokiahelaga, siis nimetatakse seda "kõrvalahelaks". Sidechainid võimaldavad varade kahesuunalist ülekandmist ühest ahelast teise. Elements'i rakendamine sidechain'ina võimaldab vältida mõningaid peahelale omaseid piiranguid, säilitades samal ajal suure osa peahelas kindlustatud varade turvalisusest.

Kui kõrvalahela on teadlik peahelast ja selle tehinguajaloost, siis peahela ei ole teadlik kõrvalahelast ja selle toimimiseks ei ole seda vaja. See võimaldab kõrvalahelatel uuendusi teha ilma piirangute või viivitusteta, mis on seotud peahela protokolli täiustamise ettepanekutega. Selle asemel, et püüda seda otseselt muuta, võimaldab peaprotokolli laiendamine peahelale endale tagada turvalisuse ja spetsialiseerumise, mis toetab kõrvalahela tõrgeteta toimimist.

Laiendades Bitcoini funktsionaalsust ja kasutades selle aluseks olevat turvalisust, suudab elementidel põhinev kõrvalahela pakkuda uusi funktsioone, mis varem ei olnud peahela kasutajatele kättesaadavad. Üks näide Elements-põhisest kõrvalahelast, mida kasutatakse tootmises, on Liquid Network.

Elements blockchaini initsialiseerimiseks sidechainina peame kasutama föderaalse peg skripti parameetrit. Selle parameetri saab määrata sõlme konfiguratsioonifailis või edastada käivitamisel.

Liitvõrgustiku skript määratleb, millised tugeva liitvõrgustiku liikmed võivad täita liitvõrgustiku sisse- ja väljavõttesüsteemi funktsioone. Neid funktsionääre nimetatakse "valvuriteks", kuna nad jälgivad põhi- ja kõrvalahelat kehtivate peg-in ja peg-out tehingute suhtes ja tegutsevad nende suhtes, kui need on kehtivad.  Kui me ütleme `move into the sidechain`, siis tegelikult tähendab see seda, et vahendid lukustatakse mitme allkirjaga aadressile mainchainis ja vastav summa vara luuakse Elements sidechainis. Kui me ütleme `move out of the sidechain`, siis peame silmas seda, et varad hävitatakse Elements sidechainis ja vastav summa vabastatakse peahelas hoitavatest lukustatud vahenditest. Luba peg-in ja peg-out funktsioonide täitmiseks nõuab, et funktsionäärid tõestaksid föderaalses peg-skriptis kasutatavate avalike võtmete omandiõigust. Seda tehakse vastavate privaatvõtmete abil.

Selleks, et luua föderatiivne peg-skript, tuleb meil seega kõigepealt lasta igal sõlmpunktil luua avalik võti. Samuti peame salvestama seotud privaatvõtmed hilisemaks kasutamiseks, sest peame kustutama kõik olemasolevad ahela andmed ja initsialiseerima uue ahela, kasutades föderatiivset peg-skripti. Seda seetõttu, et federated peg script moodustab osa sidechaini konsensusreeglitest ja seda ei saa hiljem rakendada olemasolevale, mitte-pegitud plokiahelale.

Seega genereerime iga meie sõlme aadressi, salvestame asjakohased andmed hilisemaks kasutamiseks ja genereerime föderaalse peg-skripti, mida kasutame hiljem meie külgahela initsialiseerimiseks.

Kõigepealt peame iga meie võrgusõlme, mis hakkavad meie võrgus valvuritena tegutsema, looma uue aadressi.

```
e1-cli getnewaddress
e2-cli getnewaddress
```

Seejärel valideerime aadressi, et saada avalikud võtmed.

```
e1-cli getaddressinfo <e1-address>
e2-cli getaddressinfo <e2-address>
```

Ja seejärel otsige välja iga aadressiga seotud privaatvõtmed.

```
e1-cli dumpprivkey <e1-address>
e2-cli dumpprivkey <e2-address>
```

Salvesta privaatne ja avalik võti hilisemaks kasutamiseks.

Nüüd peame pühkima olemasoleva plokiahela ja rahakoti andmed, sest me initsialiseerime uue ahela, kasutades föderaalset peg-skripti. Seda saab nüüd teha. Ärge unustage käivitada Bitcoini deemon, mida me vajame peg-in.

Nüüd saame initsialiseerida uue ahela föderaalse peg-skriptiga, mis on loodud varem salvestatud avalike võtmete abil. Numbrid, mida me sisestame ja mis ümbritsevad meie avalikke võtmeid, määravad ja piiravad kasutatavate võtmete arvu ning võtme omandiõigust, mida tuleb tõestada, et meie külgahelasse sisse ja sealt välja pegida.

```
e1-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
e2-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
```

Nüüd impordime eelnevalt salvestatud privaatvõtmed, et meie sõlmed saaksid hiljem allkirjastada ja lõpule viia varade ülekandmise ahelate vahel ning täita föderatiivse peg-skripti nõudeid.

```
e1-cli importprivkey <priv-key-1>
e2-cli importprivkey <priv-key-1>
```

Nüüd tuleb meil mõlemas ahelas mõned plokid küpseks teha. Plokkide küpsemine on peg-protsessi nõue, kuna see kaitseb plokkide reorganiseerimise eest peahelas, mis toob kaasa pegitud varade pakkumise inflatsiooni kõrvalahelas.

Et see osa keskenduks föderatiivsele pegile, genereerime plokke ilma plokkide allkirjastamise mudelita, mida vaatasime eelmises osas, ja pöördume tagasi käsu 'generate' kasutamise juurde, et luua uusi plokke.

```
b-cli generate 101
e1-cli generate 1
```

Me ei pea tingimata praegu elementide jaoks plokke genereerima. Aga genereerime ühe ikkagi. See on hea tava, et vältida võimalikke vastuolusid.

Nüüd on meie kett valmis peg-in. Peg-in'i jaoks peame genereerima erilise aadressi, kasutades käsku getpeginaddress. Peg-in-aadressi genereerimise (getpeginaddress) ja selle nõude (claimpegin) esitamise vahelist aega tuleks hoida võimalikult lühikest aega. peg-in-aadressid ei ole pikaajalise kestvusega ja neid ei tohiks uuesti kasutada.

```
e1-cli getpeginaddress
```

Näete, et käsk loob uue peahela aadressi, samuti uue skripti, mis vajab rahuldamist, et nõuda peg-in vahendeid. Mainchaini aadress on `pay to script hash`-aadress, mida kasutavad Elements-võrgus Watchmeni rolli täitvad funktsionäärid.

Nagu getnewaddress, lisab ka getpeginaddress uue saladuse kutsuva sõlme rahakotti, seega on oluline, et te võtaksite oma sõlme haldamise protsessis arvesse rahakoti faili varundamist.

Nüüd saadame mõned bitcoinid peahelast kõrvalahelasse. Meie mainchaini regressioonitesti rahakotis on juba mõned vahendid.

```
b-cli getwalletinfo
```

Näeme, et rahakotis on 50 bitcoini. Saadame ühe bitcoini peahelast sidechaini. Peame saatma raha mainchaini aadressile, mille meie sõlmpunkt eelnevalt genereeris.

```
b-cli sendtoaddress <e1-pegin-address>
```

Me peame selle tehingu ID-d säilitama, kuna vajame seda hiljem rahastamise tõendamiseks.

Nüüd näeme, et mainchaini rahakoti saldo on vähenenud meie saadetud summa võrra, millele lisandub väike summa, et katta tehingutasud.

```
b-cli getwalletinfo
```

Me peame tehingu uuesti küpsema.

```
b-cli generate 101
```

Selleks, et meie Elements-sõlm saaks peg-in vahendeid nõuda, peame saama "tõendi", et peg-in tehing on tehtud. Krüptograafiline tõestus kasutab rahastamistehingu ID-d, et arvutada merkel-tee ja tõestada, et tehing on kinnitatud plokis.

```
b-cli gettxoutproof '["<tx-id>"]'
```

Meil on vaja ka tehingu toorandmeid.

```
b-cli getrawtransaction <tx-id>
```

Peg-in-tehingu tõendi ja toorandmete abil saab meie elemendisõlm nüüd nõuda peg-in'i, kasutades toortehingut ja tehingu tõendit.

```
e1-cli claimpegin <raw> <proof>
```

Pange tähele, et on olemas vabatahtlik kolmas argument, mille me oleksime võinud esitada claimpeginile. Seda kolmandat parameetrit saab kasutada selleks, et määrata külgahela aadress, kuhu taotletud raha saadetakse. Meie näites ei olnud seda vaja, sest me kutsusime käsku samast sõlmest, millele kuulub aadress, kuhu taotletavad vahendid lähevad.

E1 saldo kontrollimine.

```
e1-cli getwalletinfo
```

Ploki genereerimine nõude kinnitamiseks.

```
e1-cli generate 1
```

E1 saldo kontrollimine.

```
e1-cli getwalletinfo
```

Näeme, et peg-in on edukalt taotletud.

Väljalülitamiseks on protsess sarnane. See tähendab, et luuakse aadress, sellele saadetakse raha ja raha vabastatakse, kui tehing on kehtiv. Me ei käsitle kogu peg-out protsessi, kuna see hõlmab tööd mainchainis, mis väljub selle kursuse raamidest. Elemendi sündmuste sammud on järgmised: Mainchainis genereeritakse aadress.

```
b-cli getnewaddress
```

Rahalised vahendid saadetakse peahela aadressile elemendisõlmest, kasutades käsku sendtomainchain.

```
e1-cli sendtomainchain <new-address> 1
```

Tehingu kinnitamiseks ploki genereerimine.

```
e1-cli generate 1
```

Kontrollida sõlme rahakoti saldot.

```
e1-cli getwalletinfo
```

Ja vaata, et saldo on vähenenud.

Selles jaotises nägime, kuidas:


- Loo föderatsiooniline peg-skript.
- Uue ahela initsialiseerimine, mis kasutab skripti võrgu konsensuse parameetrite reeglina.
- Saada raha põhikettalt kõrvalkettale.
- Nõuete esitamine elementide külgahelas.
- Saage aru, kuidas alustatakse raha tagasisaatmist põhiketti.

### FederatedPegScript

Selleks, et Elements saaks töötada sidechainina, peab selle plokiahela genesis plokk olema loodud koos `fedpegscript`iga. Seda tehakse, andes sõlme käivitamisel parameetri `fedpegscript`. Seejärel moodustab skript osa Elements blockchaini konsensusreeglitest ning võimaldab peg-in ja peg-out taotluste valideerimist ja täitmist.

`fedpegscript` koosneb avalikest võtmetest, mida kontrollivad need, kellel on õigus teha peg-toiminguid. Järgnevalt on näidisvorming 2-of-2 mitme allkirjaga fedpegscript:

```
fedpegscript=5221<public key 1>21<public key 2>52ae
```

Märkus: Väljaspool avalikke võtmeid olevad märgid on eraldusjooned, mis tähistavad avaliku võtme ja "n m" nõudeid. Näiteks 1-of-1 fedpegscript'i mall oleks '5121<pub key 1>51ae'.

### Peg-in

Enne kui Elements sidechain saab peg-in'i vastu võtta, peab sellel olema piisavalt kinnitusi peahelas. See on vajalik selleks, et vältida pegitud vara pakkumise inflatsiooni Elements sidechainis, mida võib põhjustada peaketi ümberkorraldamine.

Bitcoini plokiahela tipu lühikesed ümberkorraldused on eeldatavasti osa konsensusmehhanismi (Proof of Work, PoW) tavapärasest toimimisest. Seetõttu aktsepteerib Elements peg-in'i kehtivaina ainult siis, kui see on Bitcoini plokiahelas piisavalt sügav. Selle eesmärk on vältida, et Elements ei aktsepteeriks sama peg-in'i rohkem kui üks kord.

### Peg-Out

Peg-out toimub siis, kui Elements'i sõlmpunkt kutsub käsku `sendtomainchain`, mis võtab sisendiks põhiahela aadressi (peg-out sihtkoht) ja ka "withdrawn`tõmmatava vara summa. See loob peg-out-tehingu kõrvalahelas. Kui valvuritena tegutsevad funktsionäärid avastavad, et peg-out-tehing on kinnitatud sidechainis, hoolitsevad nad selle eest, et vara tegelikult vabastatakse mainchainis peg-out sihtkohta, nagu me õppisime kursuse varasemates osades.

## Elements kui iseseisev Blockchain

<chapterId>50dff39b-2702-47d7-9c15-0b54b845e99f</chapterId>

![Video](https://youtu.be/u-3rV7DGtD0?si=G1__H0Uelf4sTUDM)

Siiani oleme vaadelnud, kuidas Elements'i külgahelana käivitada. Siiski võib see toimida ka iseseisva plokiahela lahendusena, millel on oma vaikimisi emakeelne vara. Sellise seadistuse puhul säilitab Elements blockchain endiselt kõik sidechaini rakendamise funktsioonid, näiteks konfidentsiaalsed tehingud ja emiteeritud varad, kuid ei vaja peg-in või peg-out'i, et lisada või eemaldada ringlusse vaikimisi varade koguseid.

Selles jaotises me:

Esialgse uue Elements blockchaini initsialiseerimine vaikimisi varaga nimega `newasset`.

Määrake 1 000 000 "uut vara", mis tuleb luua koos 2 taasväljaandmise märgiga.

Nõuavad kõik igaüks saab kulutada "newasset" münte.

Nõuavad kõik "newasset"-i jaoks mõeldud igaüks-võib-kasutada-taaskasutusmärgid.

Saatke vara ja selle taasväljastamise märgis teise sõlme rahakotti.

Taasväljastada rohkem "newasset" mõlemast sõlmpunktist.

Elements-võrgu initsialiseerimiseks, et see saaks toimida iseseisva plokiahelana, tuleb iga sõlme käivitada mõnede põhiparameetritega. Nende abil öeldakse sõlmpunktile, et ta ei püüaks valideerida peg-in'eid mõnest teisest plokiahelast, võrgu vaikimisi vara nime ning vaikimisi vara ja sellega seotud taasväljaandmise märgi kogust, mis tuleb luua.

Alustame nüüd uut ahelat, kasutades neid parameetreid meie kahes ühendatud Elements-sõlmes. Anname vaikimisi varale nimeks `newasset` ja emiteerime ühe miljoni ja kaks `newasset` reissueance tokenit.

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
e2-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

Pange tähele, et siin kasutatud summad on väikseimad nimiväärtused, mida võrk saab vastu võtta, nii et kakssada miljonit taasväljaandmistähte vastab tegelikult kahele tervele märgile. Sama kehtib ka esialgsete tasuta müntide nimiväärtuse kohta.

Kontrollige meie sõlme praeguseid rahakoti saldosid.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Näeme, et initsialiseerimine toimis õigesti.

Kuna varade esialgne väljaandmine on loodud "igaüks võib kulutada", laseme e1-l neid kõiki nõuda, et me saaksime e2 juurdepääsu neile eemaldada.

```
e1-cli getnewaddress
e1-cli sendtoaddress <e1-address> 1000000 "" "" true
```

Pange tähele, et meil ei ole vaja määrata "newasset" kui saadetavat vara, kuna see on juba vaikimisi vara ja seega ka vaikimisi vara, mida kasutatakse võrgutasude maksmiseks.

Elementsis saate saata mitu varaliiki samale aadressile, seega saame uuesti kasutada aadressi, mille me just genereerisime vaikimisi vara vastuvõtmiseks, ja kasutada seda sihtaadressina taasväljaandmise märgiste jaoks.

```
e1-cli sendtoaddress <e1-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Kinnitage tehingud.

```
e1-cli generate 101
```

Kontrollime, et e1 on nüüd vara ja selle taasväljastamise märgise ainus omanik.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Mida me näeme, et see on tõepoolest nii.

Nüüd saadame osa "newasset'ist" e2-le, kelle saldo on praegu null.

```
e2-cli getnewaddress
e1-cli sendtoaddress <e2-address> 500 "" "" false
```

Pange tähele, et me ei pidanud täpsustama saadetava vara tüüpi, kuna `newasset` on loodud võrgu vaikimisi varana

Saadame ka mõned "newasset"-i jaoks mõeldud taasväljaandmise märgid e2-le.

```
e1-cli sendtoaddress <e2-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Kinnitage tehingud.

```
e1-cli generate 101
```

Saame kontrollida, et rahakotid on vastavalt uuendatud.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Nüüd anname uuesti välja mõned vaikimisi varad e1-st. Pange tähele, et võime seda teha on lubatud algusparameetriga initialreissuancetokens. Mis, kui see jäetakse välja või seatakse nulliks, toob kaasa vaikimisi vara, mida ei saa hiljem uuesti välja anda.

```
e1-cli reissueasset newasset 100
```

Meil oli võimalik kasutada sildi `newasset`, selle asemel, et anda kuuekohaline id väärtus, sest Elements kett tähistab alati oma vaikimisi vara.

Kontrollida, et vaikimisi vara taasväljastamine toimis:

```
e1-cli generate 101
e1-cli getwalletinfo
```

Nüüd tõestame, et kuna e2 omab mõningaid `newasset` taasväljaandmise märke, saab ta ka vaikimisi vara uuesti välja anda.

```
e2-cli reissueasset newasset 100
```

Kontrollimine, et e2 poolt vaikimisi vara uuesti väljaandmine toimis.

```
e2-cli generate 101
e2-cli getwalletinfo
```

Selles jaotises oleme seadistanud Elements'i iseseisva plokiahelana ja kontrollinud, et põhifunktsioonid toimivad nii, nagu me eeldame.

Me kasutasime käivitamisparameetreid:

Initsialiseerida uus Elements blockchain vaikimisi varaga nimega 'newasset'.

Määrake vaikimisi vara kogus, mis luuakse ahela initsialiseerimisel.

Loo mõned vaikimisi vara taasväljaandmise märgid ja anna mõlemast sõlmest uuesti välja rohkem vaikimisi vara.

Meie iseseisvas plokiahela Elements võrgus toimivad kõik muud tehingud samamoodi nagu kursuse põhiosades käsitletud näited, kuid vaikimisi ja tasulise varana kasutatakse "newasset" asemel "bitcoin".

### Sõlme käivitamise ja ahela initsialiseerimise parameetrid

Selleks, et öelda Elements-sõlmele, et see toimiks iseseisva plokiahelana, tuleb koos kasutada paari parameetrit. Vaatame nüüd igaüht neist ja saame teada, mida nad teevad.

#### `validatepegin=0`

Kuna eraldiseisev plokiahela ei pea kinnitama ühtegi peg-in või peg-out tehingut, peame need kontrollid välja lülitama. Selle seadistuse puhul ei ole vaja käivitada Bitcoini klienditarkvara ega salvestada Bitcoini plokiahela koopiat, kuna Elements'i võrk töötab iseseisvalt.

#### `defaultpeggedassetname`

See võimaldab määrata blokiahela initsialiseerimisel loodud vaikimisi vara nime.

#### "esialgsed tasuta mündid

Loodava vaikimisi vara number (Bitcoini Satoshi-ühikus).

#### "algne väljastamise märgid"

Number (Bitcoini Satoshi-ühiku ekvivalendina), mis on vaikimisi vara loomiseks mõeldud taasväljaandmise märgid. Ilma selleta oleks võimatu luua rohkem vaikimisi vara. Kui te ei soovi, et oleks võimalik luua rohkem vaikimisi vara, võib selle väärtuse määrata nulliks või jätta ära.

Kasutades neid parameetreid, näeks ühine sõlme käivitamine välja umbes nii:

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

### Põhilised toimingud

Parameetriga `defaultpeggedassetname` antakse vaikimisi varale silt. Ilma selle seadistuseta on vaikimisi vara nimi automaatselt `bitcoin`. Eelmistes lõikudes, kui me saatsime teisele sõlmpunktile varasid, mida me ise välja andsime, pidime määrama kas vara kuuendiku või lokaalselt rakendatud vara sildi, et öelda Elementsile, millist vara me saadame. Kuna `defaultpeggedassetname` kehtib kõigis sõlmedes, ei pea me seda saatmisel nimetama, kuigi selle nimi ei ole `bitcoin`. Iga funktsioon, mis varem oleks vaikimisi saatnud `bitcoin`, saadab nüüd mis iganes te valisite vaikimisi vara märgistuseks.

Nii et 10 uue vaikimisi vara saatmine aadressile on nii lihtne kui:

```
e1-cli sendtoaddress <destination address> 10 "" "" true
```

Kui olete sõlme jaoks andnud ka väärtuse `initialreissuancetokens`, mis on suurem kui null, siis saate ka rohkem vaikimisi vara uuesti välja anda, mis ei ole võimalik, kui käivitate Elements'i külgahelana.

Selleks peab iga sõlmpunkt, mis omab vaikimisi varaga seotud sümboolset summat, lihtsalt andma käsu kujul:

```
e1-cli reissueasset <default asset name> <amount>
```

Kasutades ülaltoodud parameetreid, saate kasutada Elements'i iseseisva plokiahelana, millel on oma vaikimisi vara, mis on lahti ühendatud Bitcoinist ja teistest plokiahelatest.

## Kokkuvõte

<chapterId>7e2c916d-8114-424c-97f5-cbff9d73b8e3</chapterId>

![Video](https://youtu.be/CTMdamTZBBM?si=16LBcXvN4pBfC7lr)

Sellel kursusel oleme õppinud, et Elements on avatud lähtekoodiga võrguprotokoll, mida saab rakendada teise plokiahela kõrvalahelana või iseseisva plokiahela lahendusena.

Me nägime, et Elements'i lähtekood ja veebisait (https://github.com/ElementsProject/elements) asuvad GitHubis ning et on olemas kogukonna arutelufoorumid, näiteks Build On L2(https://community.liquid.net/c/developers/) või Liquid Developers Telegram (https://t.me/liquid_devel), mida saab kasutada, et saada rohkem teavet rakenduste kasutuselevõtu ja arendamise kohta Elements'is ja Liquid'is. Käsitleti selliseid põhifunktsioone nagu Confidential Transactions ja Issued Assets ning seda, kuidas tugevad föderatsiooni liikmed võimaldavad föderatiivset plokkide allkirjastamist ja 2-Way Peg-mehhanismi.

Järgmine samm on esitada endale väljakutse kumulatiivse viktoriini abil, mis hõlmab kõiki eelnevaid osi, ja seejärel alustada oma Elements reisi... palju õnne!

# Kokkuvõte

<partId>d5dbd616-e291-42bc-aae3-6c44599dbd06</partId>

## Arvamused ja hinnangud

<chapterId>beae23bd-2fd1-49fe-8f38-ed169acde51d</chapterId>

<isCourseReview>true</isCourseReview>

## Kokkuvõte

<chapterId>15f62056-c69c-467e-9565-af48d439a1f5</chapterId>

Palju õnne selle kursuse lõpetamise puhul!

Oleme väga rõõmsad, et olete oma õppimise teekonnal edukalt selle verstapostini jõudnud. Tänu oma pühendumusele ja pühendumusele olete omandanud väärtuslikke teadmisi ja oskusi, mis aitavad teil oma ametialases arengus hästi edasi liikuda.