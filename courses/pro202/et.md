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

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Bitcoin rakendamise matemaatika

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Elliptiline kõver krüptograafia

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin tehingu sisemised toimingud

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Tehingu analüüs ja ECDSA allkirjad

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Skript ja tehingu valideerimine

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Tehingu ülesehitus ja Pay-to-Script Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Bitcoin võrgu sisemised toimingud

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bitcoin plokid ja Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Võrgukommunikatsioon ja Merkle Trees

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Täiustatud sõlmede side ja eraldatud tunnistaja

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Lõplik osa


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Arvamused ja hinnangud


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>


## Kokkuvõte


<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>

<isCourseConclusion>true</isCourseConclusion>
