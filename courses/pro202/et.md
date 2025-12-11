---
name: Bitcoin programmeerimine
goal: Luua täielik Bitcoin raamatukogu nullist ja mõista Bitcoin krüptograafilisi aluseid
objectives: 

 - Rakendada Pythonis lõpliku välja aritmeetikat ja elliptilise kõveraga seotud operatsioone
 - Bitcoin tehingute konstrueerimine ja analüüsimine programmiliselt
 - Testnet aadresside loomine ja tehingute edastamine üle võrgu
 - Bitcoin turvamudeli aluseks olevate matemaatiliste aluste omandamine

---
# Teekond Bitcoin skriptide ja programmide juurde


See intensiivne kahepäevane kursus, mida õpetab Jimmy Song, viib teid sügavale Bitcoin tehnilistesse alustesse, ehitades täieliku Bitcoin raamatukogu algusest peale. Alustades lõplike väljade ja elliptiliste kõverate põhilistest matemaatilistest teadmistest, liigute edasi tehingu analüüsimise, skriptide täitmise ja võrgukommunikatsiooni kaudu. Praktiliste kodeerimisharjutuste abil Jupyter-vihikutes loote oma Testnet Address, konstrueerite käsitsi tehinguid ja edastate neid otse võrku - ja saate samal ajal põhjaliku ülevaate krüptograafilistest põhimõtetest, mis muudavad Bitcoin ja Trustless turvaliseks.


Nautige oma avastust!


+++

# Sissejuhatus

<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>

## Kursuse ülevaade

<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>

Tere tulemast kursusele PRO 202 _**Programming Bitcoin**_, intensiivsele teekonnale, mis viib sind lõplike väljade aritmeetikast kuni päris tehingute loomise ja edastamiseni Bitcoini testvõrgus.

Selles kursuses ehitad samm-sammult Pythonis Bitcoini teegi, omandades samal ajal krüptograafilised, protokolli ja tarkvara alused, mis on vajalikud Bitcoini turvalisuse ja sisemise toimimise täpseks mõistmiseks. PRO 202 lähenemine on täielikult praktiline: iga kontseptsioon rakendatakse kohe Jupyteri märkmikes, tagades, et teooria ja kood tugevdavad üksteist.

### Bitcoini põhilised matemaatilised mõisted

See esimene jaotis loob hädavajaliku matemaatilise aluse. Rakendad lõplike väljade aritmeetikat ja elliptiliste kõverate operatsioone (grupi seadus, liitmine, kahekordistamine, skaala korrutamine...) — ECDSA eeltingimused. Eesmärk on kahekordne: mõista algebraatilist struktuuri, mis muudab krüptograafilised allkirjad võimalikuks, ning luua usaldusväärsed Pythoniga tööriistad nende käsitlemiseks.

Seejärel vormistad ECDSA komponendid: võtmete genereerimine, punktide vormindamine, räsi arvutamine, allkirjade loomine ja kontrollimine. See jaotis seob teooria otse praktikaga, rõhutades rakenduse üksikasju ja aluseks oleva turvamudeli töökindlust.

### Bitcoini tehingu sisemine toimimine

Teises osas analüüsid Bitcoini tehingu struktuuri: UTXO-sid, sisendeid/väljundeid, jadasid, skripte, kodeeringuid ja muud. Kirjutad koodi tehingute koostamiseks, allkirjastamiseks ja kontrollimiseks, saavutades täpse arusaamise sellest, mida räsi kinnitab ja miks.

Seejärel rakendad minimaalset _Script_-täiturit, vaatad läbi peamised opkoodid ja valideerid kulutusteed. Eesmärk on muuta sind võimeliseks auditeerima tehingute käitumist, diagnoosima valideerimisvigu ja hindama kulutuspoliitikate turvalisust.

### Bitcoini võrgu sisemine toimimine

Kolmandas osas paigutad tehingu laiemasse süsteemi: ploki struktuur, päised, raskusaste ja Proof-of-Work mehhanism. Töötad protokollisõnumite, plokipäiste ja Merkle puudega.

Lõpuks uurid võrgu võrgu (peer-to-peer) sõlmedevahelist suhtlust, sõnumi optimeerimist ja SegWiti kasutuselevõttu.

Nagu kõigis Plan ₿ Academy kursustes, sisaldab ka lõpuosa hindamist, mis on loodud sinu arusaama kinnistamiseks. Oled valmis avastama Bitcoini sisemist toimimist ja kirjutama koodi, mis seda käitab? Alustame!

# Olulised matemaatilised mõisted Bitcoin jaoks

<partId>e545b7a7-b596-436e-86e9-d0ddceb72543</partId>


## Bitcoin rakendamise matemaatika

<chapterId>790e5214-836b-40fe-bbd6-f4ccc920b778</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Elliptiline kõver krüptograafia

<chapterId>7d3d842e-ae88-472e-85ff-196d60655815</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin tehingu sisemised toimingud

<partId>774c0e80-d316-414a-bd59-0bbd185d3b58</partId>


## Bitcoin Tehingu analüüs ja ECDSA allkirjad

<chapterId>ae86fc27-2f27-4de9-b17c-351c00690144</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Skript ja tehingu valideerimine

<chapterId>8f0d4381-2b36-4c66-8bee-1100b2dfd8ed</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Tehingu ülesehitus ja Pay-to-Script Hash


<chapterId>1a6ca3fa-a71f-4b7e-9337-7c84a0b3f928</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Bitcoin võrgu sisemised toimingud

<partId>6af9d722-07da-487b-bf08-1b30bc3db3d4</partId>


## Bitcoin plokid ja Proof of Work

<chapterId>28a0f5d3-af1b-4093-be49-e3112e1d48a4</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Võrgukommunikatsioon ja Merkle Trees

<chapterId>dd8e23bc-ddd6-45a6-8d3a-16bc86ba49ac</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Täiustatud sõlmede side ja eraldatud tunnistaja

<chapterId>8d70c283-4609-46a8-ad24-83b04a68529a</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Lõplik osa


<partId>f338e5f4-216e-4b38-bf56-8333e674c04c</partId>


## Arvamused ja hinnangud


<chapterId>e149d14b-e99f-428a-a775-ed50cd0a6e9b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## Kokkuvõte


<chapterId>247bcefb-b158-42a3-82f4-c58bcad4a47a</chapterId>

<isCourseConclusion>true</isCourseConclusion>
