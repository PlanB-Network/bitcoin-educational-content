---
name: Bitcoin programmeerimine
goal: Luua täielik Bitcoin raamatukogu nullist ja mõista Bitcoin krüptograafilisi aluseid
objectives: 

 - Rakendada Pythonis lõpliku välja aritmeetikat ja elliptilise kõveraga seotud operatsioone
 - Bitcoin tehingute konstrueerimine ja analüüsimine programmiliselt
 - Luua testvõrgu aadressid ja edastada tehinguid üle võrgu
 - Bitcoin turvamudeli aluseks olevate matemaatiliste aluste omandamine

---
# Teekond Bitcoin skriptidesse ja programmidesse


See intensiivne kahepäevane kursus, mida õpetab Jimmy Song, viib teid sügavale Bitcoin tehnilistesse alustesse, ehitades täieliku Bitcoin raamatukogu algusest peale. Alustades lõplike väljade ja elliptiliste kõverate põhilistest matemaatilistest teadmistest, liigute edasi tehingu analüüsimise, skriptide täitmise ja võrgukommunikatsiooni kaudu. Praktiliste kodeerimisharjutuste abil Jupyter-vihikutes loote oma testvõrgu aadressi, konstrueerite tehinguid käsitsi ja edastate neid otse võrku - ja saate samal ajal põhjaliku ülevaate krüptograafilistest põhimõtetest, mis muudavad Bitcoin turvaliseks ja usaldusväärseks.


Nautige reisi!


+++

# Sissejuhatus


<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>


## Kursuse ülevaade


<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>


Tere tulemast kursusele PRO 202 _**Programmeerimine Bitcoin**_, mis on intensiivne teekond, mis viib teid lõplike väljade aritmeetikast kuni Bitcoini Testnet-l reaalsete tehingute loomise ja edastamiseni.


Sellel kursusel ehitate järk-järgult Bitcoin raamatukogu Pythonis, omandades samal ajal krüptograafilisi, protokolli- ja tarkvaralisi aluseid, mis on vajalikud Bitcoin turvalisuse ja sisemise toimimise täpseks mõistmiseks. PRO 202 lähenemisviis on põhjalikult praktiline: iga kontseptsiooni rakendatakse kohe Jupyter-vihikutes, tagades, et teooria ja kood tugevdavad teineteist.


### Olulised matemaatilised mõisted Bitcoin jaoks


See esimene osa loob hädavajaliku matemaatilise aluse. Te rakendate lõpliku välja aritmeetikat ja elliptiliste kõverate operatsioone (grupi seadus, liitmine, kahekordistamine, skalaarkordistamine...) - ECDSA eeldused. Eesmärgiks on kaks eesmärki: mõista algebralist struktuuri, mis teeb krüptograafilised allkirjad võimalikuks, ja luua usaldusväärsed Python-tööriistad nende manipuleerimiseks.


Seejärel vormistate ECDSA komponendid: võtme genereerimine, punktide vormindamine, räsimine, allkirja loomine ja kontrollimine. See osa ühendab teooria otseselt praktikaga, rõhutades rakendamise üksikasju ja aluseks oleva turvamudeli töökindlust.


### Bitcoin tehingu sisemine toimimine


Teises osas analüüsite Bitcoin tehingu struktuuri: UTXOd, sisendid/väljundid, järjestused, skriptid, kodeeringud ja muud. Kirjutate koodi tehingute koostamiseks, allkirjastamiseks ja kontrollimiseks, saades täpse arusaama sellest, mida ja miks hashiga pühendatakse.


Järgnevalt rakendate minimaalse _Scripti_ täitja, vaatate üle peamised opkoodid ja valideerite kuluread. Eesmärk on, et te oleksite võimeline auditeerima tehingu käitumist, diagnoosima valideerimisvigasid ja arutlema kulutamispõhimõtete ohutuse üle.


### Bitcoin võrgu sisemine töö


Kolmandas jaotises paigutate tehingud laiemasse süsteemi: plokkide struktuur, päised, raskused ja Proof-of-Work mehhanism. Käsitlete protokolli sõnumeid, plokkide päiseid ja Merkle'i puid.


Lõpuks uurite peer-to-peer-sõlmede vahelist suhtlust, sõnumite optimeerimist ja SegWit kasutuselevõttu.


Nagu iga Plan ₿ Academy kursuse puhul, sisaldab viimane osa hindamist, mille eesmärk on kinnistada teie arusaamist. Olete valmis Bitcoin sisemisi toiminguid avastama ja kirjutama koodi, mis seda käima paneb? Alustame!










# Olulised matemaatilised mõisted Bitcoin jaoks

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Bitcoin rakendamise matemaatika

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>


![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


### Bitcoin Programmeerimise alused: Põhilised matemaatilised struktuurid


See kursus koondab Bitcoin krüptograafiasüsteemide aluseks oleva olulise matemaatika väga praktiliseks töövõtteks. Kontseptsioone selgitatakse, näidetega demonstreeritakse ja seejärel rakendatakse Jupyter Notebookis. Juhtidee on lihtne: krüptograafilist primitiivi saab tõeliselt mõista alles siis, kui see on kodeeritud. Kahepäevase ülesehituse jooksul testivad õpilased generate testvõrgu aadresse, koostavad ja edastavad [tehinguid](https://planb.academy/resources/glossary/transaction-tx) ning lõpuks suhtlevad võrguga ilma plokkide uurijateta. Kõik see eeldab kindlaid teadmisi piiratud väljadest ja elliptilistest kõveratest.


### Lõplikud väljad: Krüptograafia aritmeetiline mootor


Lõplik väli F(p) on aritmeetiline süsteem, mis on defineeritud algarvuga p ja sisaldab elemente 0 kuni p-1. Primaarväljad tagavad, et igal nullist erineval elemendil on pöördväärtus ja et kõik operatsioonid jäävad väljal. Aritmeetikas kasutatakse liitmise, lahutamise ja korrutamise puhul moodulit p. Pythoni `pow(base, exp, mod)` võimaldab tõhusat modulaarset korrutust, mis on oluline suurte eksponentide puhul, mida kasutatakse reaalsetes krüptograafilistes operatsioonides.


#### Multiplikatiivne käitumine

Kui korrutada mis tahes nullist erinevat elementi k kõigi primaarvälja elementidega, saadakse selle välja permutatsioon. See omadus tagab ühetaolisuse ja hoiab ära struktuurilised nõrkused, mistõttu on priimusväljad ideaalsed turvaliseks võtmete genereerimiseks ja [digitaalseks allkirjastamiseks](https://planb.academy/resources/glossary/digital-signature).


#### Jagamine ja Fermat' väike teoreem

Jaotust rakendatakse korrutavate inversioonide abil. Fermat' väike teoreem väidab, et

n^(p-1) ≡ 1 (mod p),

nii et pöördväärtus on n^(p-2). Python toetab seda otse `pow(n, -1, p)` abil. Need operatsioonid esinevad pidevalt [ECDSA](https://planb.academy/resources/glossary/ecdsa) ja Bitcoin aluseks olevates krüptograafilistes rutiinides.


### Elliptilised kõverad: Mitte-lineaarsed struktuurid avaliku võtme turvalisuse tagamiseks


Elliptilised kõverad järgivad võrrandit y² = x³ + ax + b. Bitcoin kasutab secp256k1, mis on defineeritud kui y² = x³ + 7 üle lõpliku välja. Punktid elliptilisel kõveral moodustavad matemaatilise rühma punktide liitmisel. Läbi kahe punkti P ja Q tõmmatud sirge lõikab kõverat kolmandas punktis R; R-i peegeldamine üle x-telje annab P + Q. See süsteem on assotsiatiivne ja sisaldab identiteedielementi: punkti lõpmatuses.


Punkti kahekordistamisel kasutatakse sekantsi asemel tangentsjoont, mille kalle tuleneb kõvera tuletisest. Kuigi need valemid hõlmavad reaalarvude arvutamist, muutuvad need täielikult diskreetseks ja täpseks, kui kõver on defineeritud piiratud väljal - Bitcoin-s kasutatud kontekstis.


### Matemaatikast Bitcoin krüptograafiani


Lõplikud väljad pakuvad deterministlikku, inverteeritavat aritmeetikat; elliptilised kõverad pakuvad mittelineaarset struktuuri, kus k-P arvutamine on lihtne, kuid selle ümberpööramine on arvutuslikult teostamatu. Mõlema kombinatsioon annab aluse Bitcoin avalike/privaatvõtmete, ECDSA allkirjade ja tehinguturbe loomiseks. Nende põhialuste mõistmine valmistab õpilasi ette võtmete, tehingute ja allkirjade otseseks rakendamiseks - ilma abstraktsioonide või väliste vahenditeta.


## Elliptiline kõver krüptograafia

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>


![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


Selles peatükis tutvustatakse piiratud väljadel defineeritud elliptilisi kõveraid ja selgitatakse, miks need moodustavad Bitcoin [krüptograafia](https://planb.academy/resources/glossary/cryptography) matemaatilise selgroo. Kui reaalarvude kohal olevad elliptilised kõverad tunduvad siledad ja pidevad, siis samade võrrandite rakendamine lõpliku välja kohal tekitab diskreetse, hajutatud punktide kogumi. Vaatamata visuaalsele erinevusele käituvad kõik punktide liitmisvalemid, kalded ja algebralised reeglid täpselt samamoodi - ainult aritmeetika muutub modulaararitmikaks. Bitcoin kasutab kõverat y² = x³ + 7 (secp256k1), mis säilitab sümmeetria ja mittelineaarsuse, mis on oluline krüptograafilise turvalisuse jaoks.


### Punktide kontrollimine ja lõpliku välja rakendamine


Punkt asub lõpliku välja elliptilisel kõveral, kui selle koordinaadid rahuldavad kõvera võrrandit modulo p all. Sellise punkti nagu (73,128) F₁₃₇ kontrollimiseks tuleb kontrollida, et y² mod p on võrdne x³ + 7 mod p. Selle rakendamine koodis eeldab klasside loomist lõpliku välja elementide ja kõverapunktide jaoks. Operaatorite ülelaadimine tagab, et kogu aritmeetika - liitmine, korrutamine, korrutamine, korrutamine, korrutamine, jagamine - toimub automaatselt modulo p. Kui need abstraktsioonid on olemas, on edasijõudnud krüptograafilisi operatsioone lihtne kirjutada ja arutleda.


#### Grupi omadused ja punktide liitmine

Elliptilise kõvera punktid moodustavad matemaatilise rühma liitmise korral. See rühm vastab sulgemisele, assotsiatiivsusele, identiteedile (punkt lõpmatuses) ja inversioonile (peegeldus üle x-telje). Geomeetrilised konstruktsioonid kinnitavad neid omadusi, muutes skalaarkordistamise (P korduvalt iseendaga liitmine) hästi defineerituks. Need grupireeglid võimaldavad elliptilise kõvera krüptograafiat ja tagavad järjepideva, prognoositava käitumise korduvate punktoperatsioonide korral.


### Tsüklilised rühmad ja diskreetse logaritmi probleem


Generaatorpunkti G valimine kõveral võimaldab meil generate tsüklilist rühma: G, 2G, 3G, ..., nG = 0. Punktid tunduvad mittelineaarsed ja ettearvamatud, isegi kui neid genereeritakse järjestikku. See ettearvamatus loob aluse diskreetse logaritmi probleemile: P = sG arvutamine on lihtne, kuid s määramine P-st on suurte rühmade puhul arvutuslikult teostamatu. See ühesuunaline funktsioon on see, mis teeb avaliku võtme krüptograafia turvaliseks. Skalarid ([privaatsed võtmed](https://planb.academy/resources/glossary/private-key)) kirjutatakse väiketähtedega, punktid ([avalikud võtmed](https://planb.academy/resources/glossary/public-key)) suurtähtedega.


#### Tõhus skemaatiline korrutamine

Et arvutada sG tõhusalt, kasutavad rakendused topelt- ja lisaalgoritmi: skaneeritakse skalaari binaarne esitus, kahekordistatakse punkt igal sammul ja lisatakse G ainult siis, kui bitt on 1. See vähendab arvutusi O(n) liitmistelt O(log n), võimaldades praktilisi krüptograafilisi operatsioone isegi 256-bitiste skalaaride puhul.


#### Secp256k1 kõver Bitcoin-s


Bitcoin kasutab kõverat secp256k1, mis on defineeritud y² = x³ + 7 üle primaarvälja, kus p = 2²⁵⁶ - 2³² - 977. Generaatori punkt G on fikseeritud koordinaatidega, mis on valitud deterministliku NUMS-menetlusega ("nothing up my sleeve"). Grupi järjestus n on suur priimus, mis on 2²⁵⁶ lähedal, tagades, et iga mittenullpunkt genereerib sama grupi. Suurus 2²⁵⁶ (~10⁷⁷) on astronoomiliselt suur, mis muudab privaatvõtmete füüsiliselt võimatuks. Isegi triljon triljon aastat töötavat triljon superarvutit ei vähendaks oluliselt võtmeruumi.


### Avalikud võtmed, privaatvõtmed ja SEC-serialiseerimine


Privaatne võti on juhuslik skalaar s; avalik võti on P = sG. Kuna diskreetse logiprobleemi lahendamine on teostamatu, saab P jagada ilma s-i avaldamata. Avalikud võtmed tuleb edastamiseks SEC-vormingus seeriaviisiliselt vormistada. Pakkimata SEC-vormingus kasutatakse 65 baiti: prefix 0x04 + x-koordinaat + y-koordinaat. Pakitud vormingus kasutatakse ainult 33 baiti: prefix 0x02 või 0x03 (sõltuvalt y pariteedist) + x-koordinaat. Bitcoin kasutas algselt tihendamata võtmeid, kuid nüüd eelistab tõhususe huvides tihendatud võtmeid.


#### Bitcoin Address Loomine


Bitcoin aadressid on avalike võtmete hashid, mitte toorvõtmed ise. generate aadressi saamiseks tuleb avalik võti SEC-vormingus järjestada, arvutada hash160 ([SHA-256](https://planb.academy/resources/glossary/sha256), seejärel RIPEMD-160), lisada võrgu eesliide (0x00 mainnet puhul, 0x6F testneti puhul), arvutada kontrollsumma, kasutades kahekordset SHA-256, lisada esimesed neli kontrollsumma baiti ja kodeerida tulemus Base58 abil. See kodeerimine eemaldab mitmetähelised märgid ja sisaldab kontrollsummat, et vältida transkriptsioonivigu. Mitmeastmeline torujuhtmemehhanism peidab avaliku võtme kuni kulutamiseni, lisab võrgu identifitseerimise ja tagab inimloetavad, veakindlad aadressid.


# Bitcoin tehingu sisemine toimimine

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Tehingu analüüs ja ECDSA allkirjad

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>


![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


### ECDSA mõistmine: Bitcoini digitaalallkirja alused


Bitcoin tugineb ECDSA-le, mis on elliptilisel kõveral põhinev allkirja skeem, mis pakub tugevat turvalisust palju väiksema võtme suurusega kui RSA. Selle turvalisus tuleneb elliptilise kõvera diskreetse logaritmi probleemist: kui P = eG, on P arvutamine lihtne, kuid e tuletamine P-st on arvutuslikult teostamatu. See asümmeetria võimaldab avaliku võtme krüptograafiat, säilitades samal ajal privaatvõtmete turvalisuse.


#### ECDSA allkirjade DER-kodeerimine


Bitcoin kodeerib ECDSA allkirjad DER-vormingus:


- 0x30 (järjestuse marker)
- pikkuse bait
- 0x02 + pikkus + R baiti
- 0x02 + pikkus + S baiti


See lisab lisakulu, laiendades 64 baidi pikkust allkirja ~71-72 baidini. [Taproot](https://planb.academy/resources/glossary/taproot) kõrvaldab selle ebatõhususe, võttes kasutusele fikseeritud suurusega [Schnorr](https://planb.academy/resources/glossary/schnorr-protocol)-allkirjad.


### Allakirjutamiskohustused ja allkirjastamisprotsess


ECDSA allkirjad tuginevad kohustuste võrrandile: UG + VP = KG. Allakirjutaja valib nullist erinevad väärtused U ja V ning juhusliku [mittekoodi](https://planb.academy/resources/glossary/nonce) K, mis tõestab, et ta tunneb eravõti, ilma et ta seda avalikustaks. Sõnum hashitakse Z-sse, genereeritakse juhuslik K, R on KG x-koordinaat ja S = (Z + RE)/K. Allkiri on paar (R, S). Turvalisus sõltub olulisel määral unikaalse, ettearvamatu K kasutamisest - kui K on korduvkasutatav või lekkinud, on privaatne võti ohus. Kaasaegsed rakendused kasutavad deterministlikku K genereerimist (RFC 6979), et vältida RNG tõrkeid.


#### Allkirja kontrollimine

Arvestades Z, (R, S) ja avalikku võtit P, arvutab verifitseerija U = Z/S ja V = R/S, seejärel kontrollib, kas UG + VP x-koordinaat on võrdne R-ga. See toimib, sest verifitseerimisalgebra rekonstrueerib KG ilma isiklikku võtit vajamata. Allkirjade võltsimine nõuaks diskreetse logi probleemi lahendamist või hash-funktsiooni murdmist.


#### Schnorri allkirjad ja ajalooline kontekst


Schnorr'i allkirjad on matemaatiliselt puhtamad ja toetavad koondamisfunktsioone, kuid need olid Bitcoin käivitamisel patenteeritud. ECDSA pakkus vaba alternatiivi, mis oli küll keerulisem ja suuremate allkirjadega. Kuna patentide kehtivus lõppes, lisati Bitcoinsse Taproot kaudu Schnorr'i allkirjad, mis pakkusid 64 baidi pikkuseid fikseeritud allkirju ja paremat privaatsust. ECDSA on endiselt toetatud, et tagada vanade allkirjade ühilduvus.



### Tehingu struktuur ja sisendid/väljundid


Bitcoin tehing koosneb järgmistest osadest:


- version (4 baiti, little-endian)
- sisestusnimekiri
- väljundnimekiri
- locktime (4 baiti)


Sisendid viitavad eelnevatele [UTXOdele](https://planb.academy/resources/glossary/utxo) nende tehingu hashi ja väljundindeksi järgi ning sisaldavad lukustamisskripti (scriptSig) ja järjekorranumbrit, mida kasutatakse ajalukkude või RBF puhul. Väljundid määravad summa (8 baiti) ja lukustamisskripti (scriptPubKey), määratledes kulutustingimused. Bitcoin aadressid on nende [skriptide](https://planb.academy/resources/glossary/script) esitused.


#### Mudel UTXO

Bitcoin jälgib pigem kasutamata väljundeid kui kontode saldosid. UTXOd peavad olema täielikult kulutatud - osaline kulutamine on võimatu. Selleks, et kulutada 1 BTC 100 BTC UTXO-st, peab tehing sisaldama muutuste väljundit. Vahetuse väljundi unustamine muudab ülejäänud summa kaevandamistasuks.


#### Tehingu serialiseerimine ja analüüs


Tehingud kasutavad kompaktset binaarset formaati. Versioonivälja järel on varint, mis kodeerib sisendite arvu. Sisendite hulka kuuluvad:


- eelmine tx-hash (32 baiti)
- väljundindeks (4 baiti)
- scriptSig (varstr)
- jada (4 baiti)


Väljundite hulka kuuluvad 8 baidi suurune summa ja scriptPubKey (varstr). Locktime kontrollib, millal tehing muutub kehtivaks. Serialiseerimine kasutab enamiku täisarvude puhul little-endian järjestust. Parserid tarbivad baite järjestikku ja delegeerivad spetsialiseeritud klassidele sisendite, väljundite ja skriptide jaoks.


### Tasud, muutused ja plastilisus


Tasud on kaudsed:

tasu = summa(sisendväärtused) - summa(väljundväärtused).

Iga määramata väärtus muutub tasuks, mistõttu on oluline õige muudatuste väljundi konstrueerimine. Enne [SegWit](https://planb.academy/resources/glossary/segwit) lubasid allkirjad muudetavust - S-i muutmine N-S-ks andis uue kehtiva tehingu erineva ID-ga. Bitcoin kehtestab nüüd madala S-i reegli ja SegWit isoleerib allkirjad txid arvutustest, muutes ID-d stabiilseks ja võimaldades teise tasandi protokollid, nagu [Lightning](https://planb.academy/resources/glossary/lightning-network).


## Bitcoin Skript ja tehingu valideerimine

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>


![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


Bitcoin Script on väike, korstnapõhine nutikas lepingukeel, mis määratleb, kuidas münte saab kulutada. Iga väljund kannab scriptPubKey (lukustusskript) ja iga sisend kannab scriptSig (lukustusskript). Koos moodustavad nad programmi, mis peab hindama "true", et kulutamine oleks kehtiv. Script ei ole tahtlikult Turingi-komplektne, et kõik täitmisviisid oleksid etteaimatavad ja hõlpsasti valideeritavad kogu võrgus.


### Skriptioperatsioonid ja täitmise mudel


Skript on andmeelementide ja opkoodide jada. Andmete tõuked (allkirjad, avalikud võtmed, hashid) paigutatakse virna, samas kui opkoodid, mis algavad sõnaga `OP_`, muudavad virna. Pärast täitmist peab virna ülemine element olema nullist erinev, et saavutada edu. Näited: `OP_DUP` dubleerib ülemist elementi, `OP_HASH160` rakendab SHA256, seejärel RIPEMD160, ja `OP_CHECKSIG` kontrollib allkirja tehingu sighash'i ja avaliku võtme suhtes, lükates 1 kui see on kehtiv, 0 kui see on kehtetu. Parsimisreeglid eristavad toorandmeid (pikkuse-eesmärgiga) ja opkoode (otsitakse baitide väärtuse järgi) ning väike virtuaalmasin täidab neid deterministlikult igas [sõlmes](https://planb.academy/resources/glossary/node).


### P2PK ja P2PKH: põhilised maksemustrid


Varaseim muster, Pay-to-Public-Key (P2PK), lukustas mündid otse täie avaliku võtmega: scriptPubKey on `<pubkey> OP_CHECKSIG` ja scriptSig on lihtsalt allkiri. See on lihtne, kuid ruumiliselt ebatõhus ja avaldab avaliku võtme enne müntide kulutamist.


#### P2PKH ja aadressid

Pay-to-Public-Key-Hash (P2PKH) parandab seda, lukustades avaliku võtme 20 baidise hash'ile. ScriptPubKey on `OP_DUP OP_HASH160 <pubkey_hash> OP_EQUALVERIFY OP_CHECKSIG` ja scriptSig annab `<allkiri> <pubkey>`. Täitmine kontrollib, et esitatud avalik võti vastab hashiga kinnitatud väärtusele, ja seejärel kontrollib allkirja. See peidab avaliku võtme kuni kulutamiseni, vähendab suurust ja vastab tuttavale "1..." mainnet aadressiformaadiga.


### Tehingu valideerimine ja allkirja pesemine


Tehingut valideeriv sõlm peab tagama:

1) Iga sisend viitab olemasolevale, kasutamata väljundile.

2) Sisendväärtus kokku ≥ väljundväärtus kokku (vahe on tasu).

3) Iga scriptSig avab korrektselt oma viidatud scriptPubKey.


Allkirja kontrollimine nõuab täpse allkirjastatud sõnumi konstrueerimist, mida nimetatakse sighash'iks. Varasema ECDSA puhul tühjendab valideerimine kõik scriptSig'id, asendab praeguse sisendi scriptSig'i vastava scriptPubKey'ga, lisab 4-baidise hash-tüübi (tavaliselt `SIGHASH_ALL`) ja topelt-šassibab tulemuse. Seda 256-bitist väärtust kasutab `OP_CHECKSIG`. Alternatiivsed hash-tüübid (nt `SINGLE`, `NONE`, koos või ilma `ANYONECANPAY`-ga) muudavad seda, milliseid tehingu osi kinnitatakse, võimaldades niššikasutusjuhtumeid nagu ühisrahastamine või osaliselt määratletud tehingud, kuid praktikas kasutatakse neid harva.


#### Kvadraatiline krüpteerimine ja SegWit

Kuna iga päranditehingu sisend nõuab omaette sighash-arvutusi kõiki sisendeid sisaldava struktuuri üle, võib valideerimisaeg kasvada kvadraatiliselt koos sisendite arvuga. Kunagi põhjustasid suured mitme sisendiga tehingud märkimisväärseid valideerimisviivitusi. SegWit kujundas sighash-arvutuse ümber nii, et ühiseid osi saab vahemällu salvestada ja keerukust vähendada lineaarse ajani, mis parandab skaleeritavust ja raskendab teenusetõkestusrünnakuid.


### Skripti mõistatused ja turvalisuse õppetunnid


Skript võib väljendada palju enamat kui lihtsalt "üks allkiri avab need mündid" Skripti mõistatused demonstreerivad seda, kodeerides suvalisi tingimusi - matemaatilisi probleeme, hash-ettevalmistamise väljakutseid või isegi kokkupõrkepakkumisi -, mille puhul igaüks, kes esitab õiged andmed, saab mündid kulutada. Väljundid, mis tuginevad ainult avalikele andmetele (ilma allkirjadeta), on aga haavatavad kaevandajate front-runningule: kui kehtiv lahendus ilmub [mempoolis](https://planb.academy/resources/glossary/mempool), võib iga [kaevandaja](https://planb.academy/resources/glossary/miner) selle kopeerida ja väljamakse endale ümber suunata.


Praktiline õppetund on see, et reaalsed lepingud sisaldavad peaaegu alati allkirja kontrolli, isegi kui need sisaldavad keerukamat loogikat, nagu multisig, timelokid või hashlockid. Allkirjad seovad lahenduse konkreetse osapoolega, säilitades stiimulid ja takistades teisi väljamakseid varastamast. Script'i korstnamudeli, standardmustrite ja peente lõksude mõistmine on oluline turvaliste Bitcoin nutilepingute kavandamisel ja arutlusel selle üle, kuidas tehinguid võrgus tegelikult valideeritakse.


## Tehingu ülesehitus ja Pay-to-Script Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>


![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


### Hoone Bitcoin tehingud ja P2SH tehingud


Bitcoin tehingukonstruktsioon ühendab teoreetilised protokolliteadmised praktilise rakendamisega. Tehing valib UTXOd kulutamiseks, ehitab väljundid lukustusskriptidega, loob iga sisendi jaoks allkirjad ja serialiseerib kõik täpselt sellises formaadis, nagu sõlmed ootavad. See protsess nõuab arusaamist sighash'i genereerimisest, skriptide käitumisest ning korrektsest tasu ja muudatuste käsitlemisest.


### Põhitehingu ülesehitus


Iga tehingu sisend viitab eelmisele väljundile txid ja indeksi järgi. Väljundid määravad summad satoshis ja lukustusskriptides. Sisendite kogusumma ja väljundite kogusumma vahe on tasu. Sisendi allkirjastamiseks serialiseeritakse tehingu muudetud versioon, arvutatakse selle sighash ja allkirjastatakse see eravõti. Saadud allkiri ja avalik võti moodustavad ScriptSig. Kui iga sisend on allkirjastatud, saab toortehingut võrku edastada.


### Mitme allkirjaga tehingud


Paljas multisig kasutab "OP_CHECKMULTISIG", et nõuda m-of-n allkirju. Varajase off-by-one vea tõttu tarbib OP_CHECKMULTISIG täiendavat virnaelementi, mis nõuab algset `OP_0` ScriptSigis. Paljas multisig on funktsionaalne, kuid ebaefektiivne: kõik avalikud võtmed ilmuvad on-chain, mis muudab scriptPubKeys'i suureks, kalliks ja raskesti aadressidena kodeeritavaks. Need piirangud ajendasid pay-to-script-hash'i kasutuselevõttu.


#### P2SH arhitektuur

P2SH peidab keerulised skriptid 20 baidi HASH160 taha. ScriptPubKey on fikseeritud: `OP_HASH160 <20 baidi hash> OP_EQUAL`. Selle aluseks olev lunastusskript - mis sisaldab multisig, ajamääranguid või muid tingimusi - paljastatakse ja täidetakse ainult kulutuste korral. Saatja näeb ainult hash'i, samas kui vastuvõtja haldab lunastusskripti privaatselt. Selline ülesehitus vähendab on-chain suurust, parandab privaatsust ja võimaldab keerulisi lepinguid ilma saatjaid koormamata.


### P2SH kulutused ja rakendamine


P2SH väljundi kulutamiseks peab ScriptSig sisaldama vajalikke avamisandmeid *pluss* ja lunastusskripti ennast. Valideerimine toimub kahes etapis:

1) HASH160(redeem_script) peab vastama scriptPubKey hashile.

2) Pärast kontrollimist käivitatakse lunastusskript esitatud andmetega.


P2SH sisendi jaoks allkirjade genereerimisel kasutab sighash protsess scriptPubKey asemel lunastusskripti. generate kehtivate allkirjade saamiseks peab iga allkirjastaja omama täielikku redeem-skripti. P2SH aadressid kasutavad mainnet puhul versiooni baiti 0x05 ("3..." aadressid) ja testnetis 0xC4 ("2..." aadressid).


#### Praktilised julgeolekukaalutlused


Lunastusskripti kaotamine tähendab rahaliste vahendite kaotamist: kulutamiseks on vaja nii isiklikke võtmeid kui ka lunastusskripti ennast. Multisig osalejad peavad enne hoiuste vastuvõtmist kontrollima, et nende avalikud võtmed on korrektselt lisatud. P2SH toetab täiustatud konstruktsioone, nagu multisig, timelock ja hashlock, kuid vead skriptiloogikas võivad rahalised vahendid jäädavalt lukustada, seega on testimine testneti kaudu hädavajalik.


P2SH parandab privaatsust, kuna varjab kulutustingimused kuni esimese kulutamiseni, kuid kui lunastusskript ilmub on-chain, muutub see püsivalt nähtavaks. Sellele vaatamata on P2SH tänu väiksemale suurusele, tagasiulatuvale ühilduvusele ja paindlikule lepingutoele oluline verstapost, mis mõjutas hilisemaid uuendusi, näiteks SegWit ja Taproot.


# Bitcoin võrgustiku sisemine toimimine

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bitcoin plokid ja Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>


![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


Bitcoin blokeerib rühmatehingud ja kindlustab need [proof of work](https://planb.academy/resources/glossary/proof-of-work) abil. Iga [plokk](https://planb.academy/resources/glossary/block) sisaldab 80 baidi pikkust [päistekirja](https://planb.academy/resources/glossary/block-header) ja tehingute nimekirja. Hoolimata kehtiva ploki tootmise suurest energiakulust on selle verifitseerimine odav: kõigi ~900k päiste salvestamiseks on vaja ainult ~72 MB, mis võimaldab isegi väikestel seadmetel ahela proof of work tõhusalt verifitseerida.


### Coinbase'i tehingud ja plokkide preemiad


Iga plokk algab täpselt ühe [Coinbase'i tehinguga](https://planb.academy/resources/glossary/coinbase-transaction) - see on ainus viis, kuidas uued bitcoinid ringlusse jõuavad. Sellel on nullitud prev-tx hash ja indeks 0xffffffffff, mis identifitseerib selle üheselt. Toetus algas 50 BTC-st ja väheneb poole võrra iga 210 000 ploki järel (50, 25, 12,5, 6,25, 3,125, ...). Kaevandajad sisaldavad ka tehingutasusid. Kuna 4 baidi suurune nonce on kaasaegsete ASICide jaoks liiga väike, muudavad kaevandajad Coinbase'i tehingu andmeid, et muuta [Merkle'i](https://planb.academy/resources/glossary/merkle-tree) juurt ja luua täiendavat otsinguruumi. [BIP34](https://planb.academy/resources/glossary/bip) nõuab blokikõrguse manustamist Coinbase'i skriptSig, et tagada iga Coinbase'i txid ainulaadsus.


### Ploki päise väljad ja Soft Fork signaalimine


80 baidi pikkune päis sisaldab:


- versioon (4 baiti)
- eelmise ploki hash (32 baiti)
- Merkle'i juur (32 baiti)
- ajatempel (4 baiti)
- bitid (raskusaste, 4 baiti)
- nonce (4 baiti)


Versiooninumbrid arenesid BIP9 kaudu bitivälja signalisatsioonisüsteemiks, mis võimaldab kaevandajatel koordineerida [soft-fork](https://planb.academy/resources/glossary/soft-fork) valmisolekut. Ajatempel on 32-bitine Unixi ajaväärtus ja vajab uuendamist umbes aastal 2106.


#### Bittide väli ja sihtmärgid

Bitide väli kodeerib eesmärgi kompaktsel kujul: eesmärk = koefitsient × 256^(eksponent-3). Kehtivad plokkide hashid peavad olema numbriliselt alla selle eesmärgi. Kuna häkke tõlgendatakse väikese lõpuastmega täisarvudena, siis on kehtivate häkkide puhul sageli kuusnumbrilisel kujul esitatud palju nulle.


### Raskused, valideerimine ja kohandused


[Raskus](https://planb.academy/resources/glossary/difficulty) on määratletud kui madalaim_eesmärk / praegune_eesmärk, mis näitab, kui palju raskem on mining täna võrreldes kõige lihtsama võimaliku raskusastmega. Valideerimiseks on vaja ainult võrrelda pealkirja hash'i sihtmärgiga - see on mining suhtes äärmiselt odav.


Iga 2016 ploki järel kohandab Bitcoin raskusastet, et saavutada ~10-minutiliste plokkide intervallid. Kohandamisel võrreldakse eelmise 2016. aasta plokkide tegelikku aega eeldatava kahe nädalaga. Piirangud piiravad kohandusi neljakordaja piires. Suuremad reaalsed sündmused - näiteks Hiina mining keelustamine - näitasid selle mehhanismi vastupidavust, kui hash-kiirus langes järsult ja raskusastet kohandati selle kompenseerimiseks allapoole.


### Blokeeritud toetus ja kogusumma Supply


Subsiidium kõrgusel h arvutatakse järgmiselt: subsiidium = 5_000_000_000 >> (h // 210_000). See annab poolitusgraafiku, mis konvergeerub ~21 miljoni BTC suuruse kogupakkumise suunas. Geomeetriliste jadade (50 + 25 + 12,5 + ...) × 210 000 summeerimine selgitab ülempiiri. Kaevandajad võivad nõuda vähem kui lubatud toetus, kuid mitte kunagi rohkem, või plokk muutub kehtetuks. Kuna subsiidiumid vähenevad järjestikuste poolitamiste käigus, muutuvad tehingutasud üha olulisemaks komponendiks kaevandajate tulude ja võrgu pikaajalise turvalisuse seisukohalt.


## Võrgukommunikatsioon ja Merkle Trees

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>


![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


### Bitcoin võrguarhitektuur


Bitcoin [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p)-võrk toimib detsentraliseeritud kuulujuttude süsteemina, kus sõlmed edastavad tehinguid ja plokke üksteist usaldamata. Uued sõlmed käivituvad, võttes ühendust tuumarendajate poolt hallatavate kõvakodeeritud DNS-seemnetega. Need DNS-seemned tagastavad aktiivsete eakaaslaste IP-aadressid, mis võimaldab sõlmedel võrgustikku avastada ja seejärel taotleda getaddr kaudu täiendavaid eakaaslasi. Võrgustik ei ole tahtlikult konsensuskriitiline, nii et rakendused võivad erineda, kui [konsensuse](https://planb.academy/resources/glossary/consensus) reeglid jäävad muutumatuks.


### Sõnumi struktuur ja käepigistus


Kõik Bitcoin P2P sõnumid kasutavad fikseeritud ümbrikku: 4-baidine maagiline väärtus (F9BEB4D9 mainnet puhul), 12baidine ASCII käsk, 4-baidine little-endian kasuliku koormuse pikkus, 4-baidine kontrollsumma (esimesed 4 baiti [hash](https://planb.academy/resources/glossary/hash-function)256-st) ja kasuliku koormuse. Tavalised käsud on version, verack, inv, getdata, tx, block, getheaders, headers, headers, ping ja pong.


Kätevahetus algab, kui ühendav sõlm saadab versioonisõnumi. Vastuvõtja vastab verackiga ja oma versiooniga. Kui mõlemad pooled vahetavad need kaks sõnumit, on ühendus aktiivne ja sõlmed võivad alustada inventuuri ja andmete edastamist.


### Merkle-puud ja Merkle-juured


Bitcoin salvestab iga ploki päisesse ühe 32baidise Merkle'i juure, mis on kohustus kõigi ploki tehingute suhtes. Tehingud hashitakse (hash256), paaritakse, ühendatakse ja hashitakse korduvalt, kuni järele jääb üks hash. Kui tasand on paaritu arvuga, dubleeritakse viimane hash. Hashid on sisemiselt big-endian, samas kui serialiseeritud plokkide andmed on little-endian, mis nõuab ümberpööramist enne ja pärast puu konstrueerimist.


#### Merkle Proofs ja SPV

Merkle-tõendid võimaldavad kontrollida, et tehing sisaldub plokis ilma kogu plokki alla laadimata. Tõend koosneb õdedest hashidest piki teed juureni. Kerge SPV-kliendid salvestavad ainult plokkide päised ja nõuavad neid tõendeid [täis sõlmedelt](https://planb.academy/resources/glossary/full-node). Kuna Merkle'i puu kasvab logaritmiliselt, nõuab tuhandete tehingutega plokki kuulumise tõestamine vaid mõnisada baiti.


Taproot laiendab seda kontseptsiooni, sidudes kulutuste tingimused Merklized script tree (MAST), paljastades ainult teostatud haru koos Merkle-tõendiga. See parandab nii tõhusust kui ka privaatsust.


### Võrguoperatsioonid ja plokkide sünkroniseerimine


Sõlmed kasutavad getdata, et taotleda tehinguid või plokke, määrates tüübi ID (1=tx, 2=plokk, 3=filtreeritud plokk, 4=kompaktne plokk) ja 32baidise identifikaatori. Ahelasünkroonimiseks saadavad sõlmed getheaders'i koos algbloki hashiga, saades vastuseks kuni 2000 headerit. Iga tagastatav päis on 80 baiti, millele järgneb nullist tehingulugu.


Saadud plokkide täielik kontrollimine nõuab kahte kontrolli:

1. Plokkide hash peab olema allpool bittide väljal kodeeritud eesmärki.

2. Kõikidest tehingutest arvutatud Merkle'i juur (nõuetekohase endiannuse käsitlemise korral) peab vastama päise juurele.


Ainult siis, kui mõlemad tingimused on täidetud, võtab sõlmpunkt ploki vastu, mis peegeldab Bitcoin põhimõtet "ära usalda, kontrolli".


## Täiustatud sõlmede side ja eraldatud tunnistaja

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>


![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)


See sessioon ühendab P2P täiustatud võrguühendust segregatsioonitunnistajaga, näidates, kuidas kaasaegne Bitcoin tarkvara suhtleb otse sõlmedega, kasutades samal ajal SegWit-teadlikke tehingustruktuure. Arendajad õpivad otsima plokke, otsima asjakohaseid tehinguid ja konstrueerima tehinguid, kasutades ainult töötlemata võrgukommunikatsiooni - plokkide uurijaid ei ole vaja.


### Blokipõhine tehinguotsing ja privaatsus


[Rahakotid](https://planb.academy/resources/glossary/wallet) peavad tuvastama sissetulevad maksed, skaneerides plokke nende scriptPubKey-le vastavate väljundite jaoks. Tervete plokkide otsimine kaitseb privaatsust paremini kui üksikute tehingute pärimine, mis annab tugevaid signaale kasutaja aktiivsuse kohta. Isegi plokkide päringud võivad lekkida teavet väikese mahuga ahelate kohta, mistõttu on kompaktsed plokkide filtrid (BIP158) olulised eraelu puutumatust säilitavate kergklientide jaoks. Filtrid võivad anda valepositiivseid, kuid mitte kunagi valenegatiivseid tulemusi, võimaldades klientidel alla laadida ainult potentsiaalselt asjakohaseid plokke, ilma et nad paljastaksid konkreetseid aadresse.


### Trustless Võrgu koostoime


Tööprotsess "get_block" näitab võrgu nõuetekohast kasutamist: saadetakse getdata, saadetakse plokk, seejärel kontrollitakse sõltumatult selle Merkle'i juurt ja proof of work. Plokk võetakse vastu ainult siis, kui vastuvõetud päise hash langeb kokku taotletud hashiga ja selle arvutatud Merkle'i juur langeb kokku päisega. See kehastab põhimõtet "ära usalda, kontrolli", tagades, et isegi pahatahtlikud partnerid ei saa sõlmi pettusega panna muutnud andmeid vastu võtma.


#### Tehingute väljavõtmine plokkidest

Bloki tehinguid saab skaneerida sobivate scriptPubKeys'ide leidmiseks, kasutades lihtsat iteratsiooni. Tootmise rahakotid teevad seda pidevalt uute plokkide saabumisel, tõestades väljundite omandiõigust rangelt krüptograafilise valideerimise kaudu, mitte kolmandate osapoolte APIdele tuginedes.


### SegWit Eesmärgid ja kavandamine


Eraldatud tunnistaja (SegWit) parandas tehingu võltsitavuse, eemaldades txid arvutustest allkirjaandmed. See võimaldas usaldusväärseid eelallkirjastatud tehinguahelaid ja muutis Lightning Network praktiliseks. SegWit suurendas ka plokkide mahutavust, kasutades "plokkide kaalu": vanad sõlmed näevad endiselt ≤1 MB plokke, samas kui uuendatud sõlmed valideerivad kuni 4 MB koos tunnistajate andmetega. Versioonitud tunnistajaprogrammid (seni v0-v1) loovad struktureeritud uuendustee tulevaste skriptitüüpide jaoks.


#### P2WPKH (emakeelne SegWit)


P2WPKH asendab senise P2PKH struktuuri 22 baidise skriptiga: OP_0 + push20 + hash160(pubkey). Spending paigutab allkirja ja pubkey eraldi tunnistusväljale.


- SegWit-eelsed sõlmed: vt "igaüks võib kulutada", käsitlege seda kehtivana.
- SegWit järgsed sõlmed: tunnevad OP_0 + 20 baidi hash ja valideerivad tunnistajate andmete abil.


Selline eraldamine parandab paindlikkust ja vähendab tasusid. Tunnistaja kasutab varint loendust, millele järgneb allkiri ja avalik võti.


#### P2SH-P2WPKH (tagasiühilduv SegWit)


Selleks, et vanad rahakotid saaksid saata SegWit aadressidele, võib P2WPKH skripte pakendada P2SH-ga.


- scriptPubKey: standard P2SH hash160(redeemScript)
- scriptSig: redeemScript (programm P2WPKH)
- tunnistaja: allkiri + avalik võti


Valideerimiskihid:

1. Pre-BIP16 sõlmed aktsepteerivad redeemScripti kehtivana.

2. Post-BIP16 sõlmed hindavad seda, jättes OP_0 + hashi virna.

3. SegWit-sõlmed teostavad täielikku tunnistajate valideerimist.


#### P2WSH keeruliste skriptide jaoks


P2WSH üldistab SegWit multisigade ja täiustatud skriptide jaoks, kasutades hash160 asemel SHA256(skript). Tüüpiline 2-ast-3 multisig tunnistajate virna:


- tühi element (CHECKMULTISIG-viga)
- sig1
- sig2
- tunnistajaskript (multisig script)


SegWit sõlmed kontrollivad, kas SHA256(witnessScript) vastab scriptPubKey hashile ja seejärel täidavad seda. SHA256 ja 32baidise hashi kasutamine võimaldab eristada P2WSH-d P2WPKH-st ja tugevdab turvalisust.


#### P2SH-P2WSH (maksimaalne ühilduvus)


Kompleksseid SegWit skripte saab ka P2SH-ga ümbritseda:


- scriptSig: redeemScript (OP_0 + 32 baiti suurune hash)
- tunnistaja: allkirjad + tunnistajaSkript


Valideerimine läbib kolm põlvkonda reegleid täpselt nagu P2SH-P2WPKH puhul. See pakett oli oluline varajase Lightning'i kasutuselevõtu jaoks, mis vajas multisegmendi kasutamist ilma muudetavuseta. Kuigi tänapäeval eelistatakse originaalset P2WSH-d, tagab pakendatud vorm ühilduvuse vanemate wallet süsteemide vahel.


### SegWit mõju


SegWit ette nähtud:


- stabiilne tehingu ID
- madalamad tasud tänu soodushinnaga tunnistajate andmetele
- suurem plokkide läbilaskevõime tänu plokkide kaalule
- vanade sõlmede ühilduvus
- puhas uuendustee Taproot ja tulevaste laienduste jaoks


Need vahendid moodustavad koos usaldusvaba võrgustiku suhtlusega kaasaegse Bitcoin arendamise selgroo.



# Lõpposa


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Arvamused ja hinnangud


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Lõpueksam


<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>



<isCourseExam>true</isCourseExam>

## Kokkuvõte



<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>


<isCourseConclusion>true</isCourseConclusion>