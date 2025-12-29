---
name: Pärimiskava Bitcoin
description: Kuidas kanda bitcoine oma lähedastele üle
---

![cover](assets/cover.webp)



Bitcoinide edastamine kujutab endast suurt tehnilist väljakutset, mida paljud omanikud eiravad. Erinevalt traditsioonilistest pangavahenditest, kus finantsasutus saab raha õigustatud omanikele üle kanda, toimib Bitcoin ilma vahendajateta. Teie lähedased ei saa kunagi ilma vajalike tehniliste andmeteta juurdepääsu teie rahalistele vahenditele, sõltumata nende õiguslikust seaduslikkusest.



See juhendmaterjal juhendab teid tehnilise pärimisplaani koostamisel. Saate teada, kuidas on-chain automaatse edastamise mehhanismid toimivad, kuidas dokumenteerida oma konfiguratsioone ja kuidas valida õigeid lahendusi, et tagada Bitcoin pärandi kättesaadavus oma lähedastele.



## Miks tehniline pärandkava on hädavajalik



Bitcoin põhineb põhilisel krüptograafilisel põhimõttel: kes iganes omab isiklikke võtmeid, see kontrollib ka raha. See suveräänsus muutub suureks haavatavuseks, kui omanik kaob ilma vajalikku teavet edastamata.



Bitcoin pärimisplaan peab vastama kahele näiliselt vastuolulisele eesmärgile: võimaldada teie lähedastele juurdepääsu teie rahalistele vahenditele, kui aeg on käes, ja samas takistada kellelgi teisel nende varade enneaegset kasutamist. See tundlik tasakaal tugineb Bitcoin algupärastele programmeerimisvõimalustele.



Tehniline keerukus lisab täiendava raskusastme. Teie pärijad peavad manipuleerima selliseid mõisteid nagu taastamislaused, portfelli kirjeldused või tuletamisrajad. Ilma piisava ettevalmistuseta võib isegi heade kavatsustega pärija teha pöördumatuid vigu.



## Kuidas on-chain pärimine toimib



Bitcoin kasutab oma skriptimiskeelt kulutustingimuste kodeerimiseks otse tehingutes. on-chain pärand kasutab seda programmeeritavust, et luua alternatiivseid taastumisviise, mis aktiveeruvad automaatselt.



### Timelocks



Ajamärgid on Bitcoin pärimise põhiline mehhanism. Need võimaldavad rahalisi vahendeid lukustada, kuni mingi ajaline tingimus on täidetud.



**CLTV (CheckLockTimeVerify)**: See absoluutne ajalukk kontrollib, et enne kulutuste lubamist on saavutatud kindel aeg (kuupäev või ploki kõrgus). Näiteks "neid vahendeid võib kulutada alles pärast blokki 900000" või "pärast 1. jaanuari 2026". CLTV eelis on see, et see võimaldab pikki viivitusi (mitu aastat), kuid kuupäev on fikseeritud ja kehtib samamoodi kõigi portfelli UTXOde suhtes. Selleks, et säilitada kontroll oma vahendite üle, peate perioodiliselt looma uue portfelli pikendatud aegumiskuupäevaga ja kandma oma vahendid sinna üle.



**CSV (CheckSequenceVerify)**: See suhteline ajalukk kontrollib, et UTXO loomisest on möödunud teatud arv plokke. Näiteks "neid vahendeid võib kulutada ainult 52560 plokki (~1 aasta) pärast nende saamist". CSV eelis on see, et igal UTXO-l on oma sõltumatu loendur. Iga kord, kui te sooritate tehingu, nullivad äsja loodud UTXOd omaenda ajalimiidi. Tehniline piirang 65535 plokki (~15 kuud maksimaalselt) piirab siiski võimalikke ajavahemikke. Selline lähenemine on igapäevaseks kasutamiseks loomulikum, kuna teie tavapärane tegevus lükkab tähtaegu automaatselt edasi.



### Mitmesugused kulutused



Pärandportfell ühendab igas aadressis mitu kulutamisviisi:





- Peamine tee** : Omanik võib oma põhivõtmega igal ajal kulutada oma raha, ilma ajaliste piiranguteta.
- Taastamisviis(id)**: Üks või mitu alternatiivset võtit võivad kulutada raha alles pärast kindlaksmääratud aja möödumist.



Iga omaniku poolt sooritatud tehing "värskendab" UTXO, luues uusi väljundeid koos lähtestatud ajamärkidega. See mehhanism tagab, et nii kaua, kui omanik on aktiivne, ei aktiveeru taastumisrajad kunagi.



### Miniskript ja Taproot



**Miniscript** on Andrew Poelstra, Pieter Wuille ja Sanket Kanjalkari poolt välja töötatud struktureeritud keel, mis muudab keeruliste Bitcoin skriptide kirjutamise ja analüüsimise lihtsaks. See võimaldab koostada loetavaid ja kontrollitavaid kulutustingimusi, mis on olulised mitut võtit ja ajamäärangut hõlmavate päringukonfiguratsioonide puhul.



**Taproot** (aktiveeritud novembris 2021) parandab oluliselt on-chain pärandit. Tänu selle puustruktuurile (MAST) ilmneb plokiahelas ainult kasutatud kulutustingimus. Kui omanik kulutab oma vahendid normaalselt, jäävad pärimistingimused nähtamatuks. See konfidentsiaalsus vähendab ka tehingukulusid keerukate teekondade puhul.



## Deskriptorite kriitiline tähtsus



Varasemate portfellide puhul ei piisa taastamislausest (seed), et taastada juurdepääs rahalistele vahenditele. Kriitiliseks elemendiks saab **deskriptor**.



Deskriptor on string, mis kirjeldab ammendavalt portfelli struktuuri: asjaomased avalikud võtmed, kulutustingimused, tuletamise teed ja konfigureeritud ajamäärad. Siin on lihtsustatud näide:



```
wsh(or_d(pk([fingerprint/path]xpub...),and_v(v:pkh([fingerprint/path]xpub...),older(52560))))
```



See kirjeldus ütleb: "kas peavõti võib kulutada kohe või taastamisvõti võib kulutada pärast 52560 plokki".



Võtame selle näite lahti:




- `wsh()` : Witness Script Hash, näitab aadressi tüüpi (P2WSH)
- or_d()`: "või" tingimus vaikimisi haruga
- pk([fingerprint/path]xpub...)`: Avalik peavõti koos selle sõrmejälje ja tuletamise teega
- and_v()`: "ja" tingimus, mis ühendab taastamisvõtme ja ajaluku
- `vanem(52560)`: 52560 ploki suhteline ajaline lukk



**Kirjelduseta, isegi kõigi taastamislausetega, ei saa teie pärijad portfelli taastada.** Standardportfelli saab taastada ainult seed-st, sest see järgib standardiseeritud tuletamisviise (BIP44, BIP84). Pärandportfell seevastu kasutab kohandatud skripte, mida ei saa ära arvata. Deskriptori varukoopia (või teie tarkvara poolt eksporditud konfiguratsioonifail) peab olema koos taastamislausetega teie pärimisplaanis.



## Pärimisplaani dokumentaalsed komponendid



Lisaks tehnilistele mehhanismidele tugineb tõhus pärandkava kolmele dokumentatsiooni sambale.



### Pärimiskiri



See isiklik kiri on teie plaani sisenemispunkt. See on kirjutatud teie pärijatele ja selles selgitatakse konteksti ja ettevaatusabinõusid.



Teie kiri peab sisaldama selgesõnalisi ohutuseeskirju:




- Ärge kiirustage, võtke aega õppimiseks enne rahaliste vahendite liikumist
- Ärge kunagi edastage täielikku taastumisfraasi ühele inimesele
- Ärge kunagi sisestage taastamise fraasi kontrollimata tarkvaraprogrammi või arvutisse
- Ettevaatust pettuste ja soovimatut abi pakkuvate inimeste suhtes
- Enne otsuse tegemist küsige nõu vähemalt kahelt inimeselt, keda te usaldate



See kiri sisaldab ka teie notari kontaktandmeid ja testamendi asukoha. See ei tohiks kunagi sisaldada taastumisfraase ega paroole.



### Usaldusväärsete kontaktide kataloog



Ükski pärija ei peaks Bitcoini taastamisega üksi silmitsi seisma. Selles kataloogis on loetletud inimesed, kes saavad pakkuda tehnilist või juriidilist abi.



Dokumenteerige iga kontaktisiku kohta: täielik nimi, suhe teiega, roll plaanis, usalduse tase, Bitcoin oskused ja täielikud kontaktandmed. Põhireegel: teie pärijad peaksid alati konsulteerima vähemalt kahe erineva inimesega enne mis tahes olulise otsuse tegemist.



### Bitcoin varade inventuur



Selles jaotises on kaardistatud kõik teie bitcoinid koos nende taastamiseks vajaliku tehnilise teabega.



Iga portfelli puhul dokumenteerige :




- Portfelli tüüp**: riistvara, tarkvara, konfiguratsioon (ühe signeeringuga, mitme signeeringuga, pärand)
- Seadme asukoht**: wallet riistvara füüsiline asukoht
- Descriptor/konfiguratsioonifaili asukoht**: kriitiline edasijõudnute portfellide puhul
- Taastamislause asukoht**: kirjeldusest eraldi
- Juurdepääsukoodid**: kus PIN-koodid ja paroolid on salvestatud
- Konfigureeritud viivitused**: kui taastumisradad aktiveeruvad



## Saadaval on tehnilised lahendused



Mitmed tarkvarapaketid rakendavad on-chain pärimismehhanisme. Igaühel neist on oma tehnilised omadused.



### Liana



Liana on töölaua tarkvara (Linux, macOS, Windows), mis kasutab Miniscript'i, et luua portfooliosid ajastatud taastumisradadega. Projekti arendab Wizardsardine, mille kaasasutajaks on Antoine Poinsot (Bitcoin Core'i toetaja).



**Tehniline arhitektuur**: Liana loob vaikimisi P2WSH portfellid (SegWit native), Taproot tugi on saadaval sõltuvalt wallet riistvara ühilduvusest. Arhitektuur põhineb põhirajal ja ühel või mitmel taastamisrajal. Genereeritud kirjeldus kodeerib kõik tingimused ja see tuleb salvestada.



**Kasutatakse ajalukke**: Liana kasutab suhtelisi ajamärke (CSV), mis on piiratud 65535 plokiga (~15 kuud). Kontrolli säilitamiseks tuleb enne ajatõkke kehtivusaja lõppemist teha uuendustehing.



**Hardvara wallet integreerimine**: BitBox02, Blockstream Jade, Coldcard, Ledger, Specter DIY ja muud seadmed ühilduvad tehingute allkirjastamiseks.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

### Bitcoin Keeper



Bitcoin Keeper on mobiilirakendus (iOS, Android), mis kombineerib multisig ja ajalukud oma "täiustatud võlvid" kaudu. Mobiilne lähenemine koos integreeritud juhistega teeb selle kättesaadavaks ka vähem tehnilistele kasutajatele.



**Tehniline arhitektuur**: Täiustatud võlvrid kasutavad Miniscripti, et luua multisig-konfiguratsioone, kus lisaklahvid aktiveeruvad pärast kindlaksmääratud viivitusi. Inheritance Key lisab olemasolevale kvoorumile, samal ajal kui Emergency Key võib multisigist täielikult mööda minna.



**Kasutatakse ajalukke**: Bitcoin Keeper kasutab absoluutseid ajamõõtjaid (CLTV), mis võimaldab üle 15 kuu pikkust tarneaega. Aktiveerimiskuupäev määratakse wallet loomisel ja seda kohaldatakse kõigi UTXOde suhtes. Rakendus sisaldab "revaulting" funktsiooni, mis juhib automaatselt uuendamist: kasutaja lihtsalt järgib juhendatud samme, ilma et ta peaks käsitsi uut wallet looma.



**Lisafunktsioonid**: Kanaari rahakotid võtmete kompromisside tuvastamiseks ja värskendavad meeldetuletusi.



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

### Heritage



Heritage on töölauarakendus, mis kasutab Taproot skripte, et kodeerida pärimistingimusi. Taproot kasutamine pakub suuremat konfidentsiaalsust, kuna kasutamata teed jäävad plokiahelas nähtamatuks.



**Tehniline arhitektuur**: Iga pärandi aadress sisaldab peamist ja alternatiivseid radu iga pärandi jaoks, millel on järkjärguline ajakava. Hierarhiline struktuur võimaldab määratleda isikliku varukoopia 6 kuuga ja perepärijate 12-15 kuuga.



**Kasutamisviisid**: (tasuta) või hallatav teenus, mis lisab meeldetuletusi ja teateid pärijatele (0,05% aastas).



https://planb.academy/tutorials/wallet/desktop/heritage-0549701f-2619-4037-ad05-44982be73ef4

## Pärija taastumisprotsess



Taastumisprotsessi mõistmine aitab koostada tõhusa plaani. Järgnevalt on esitatud tehnilised sammud, mida pärija peab järgima.



### Taastamisnõuded



Pärija vajab :


1. **Algse portfelli kirjeldus- või konfiguratsioonifail** (JSON- või tekstivormingus, sõltuvalt tarkvarast)


2. **Selle taastumisfraas** (mis on seotud selle pärimisvõtmega, tavaliselt 12 või 24 sõna)


3. **Sobiv tarkvara** (Liana, Bitcoin Keeper, Heritage või Sparrow/Specter standarddeskriptorite jaoks)


4. **ühendus Bitcoin**-sõlmega, et kontrollida ajaluku staatust ja edastada tehing



### Taastumise sammud



1. **Installige tarkvara** turvalisse seadmesse ja konfigureerige ühendus Bitcoin võrguga (isiklik sõlmpunkt või Electrum server)


2. **Impordi kirjeldaja** portfelli struktuuri rekonstrueerimiseks. Tarkvara generate automaatselt kõik kasutatud aadressid


3. **Pärimisvõtme taastamine** taastamislausest. Tarkvara kontrollib, et see võti vastab ühele kirjelduses lubatud võtmetele


4. **Sünkroniseeri portfell**, et avastada kõik UTXOd ja nende kulutustingimused


5. **Kontrollige ajaluku aegumist**: tarkvara näitab iga UTXO puhul, kas taastumisraja on aktiivne


6. **Loo taastamistehing** aadressile, mida kontrollib ainult pärija (ideaalis uus üksik wallet)


7. **Tehingu allkirjastamine ja edastamine** Bitcoin võrgus



Kui ajapiirang ei ole veel lõppenud, peab pärija ootama. Tarkvara kuvab kuupäeva või ploki, millest alates on võimalik taastamine. Selle ooteaja jooksul jäävad rahalised vahendid turvaliselt plokiahelasse.



### Punktid, mida tuleb jälgida pärija puhul



Pärandaja peab pöörama erilist tähelepanu :




- Kontrollida allalaaditud tarkvara autentsust** (kontrollsummad, allkirjad)
- Ärge kunagi jagage oma taastumisfraasi** kellegagi, kes pakub abi
- Konsulteerige vähemalt kahe inimesega, keda te usaldate**, enne kui teete taastamise
- Viia vahendid üle lihtsasse portfelli**, mida ta pärast taastumist täielikult kontrollib



## Parimad tavad



### Teabe eraldamine



Ärge kunagi hoidke kogu teavet ühes kohas. Deskriptor tuleb eraldada taastamislausetest, mis omakorda eraldatakse PIN-koodidest. Selline jaotamine raskendab ründajale juurdepääsu, jäädes samas teie seaduslikele pärijatele taastatavaks.



### Taastamiskatsed



Enne suuremate summade hoiustamist testige kogu taastamisprotsessi väikese summaga. Kontrollige, et saate portfelli taastada kirjelduse ja taastamislausete abil tühjal seadmel. Dokumenteerige sammud oma pärijate jaoks.



### Timelocki hooldus



Plaanige oma ajamärkide uuendamine aegsasti enne nende kehtivuse lõppemist. 12-kuulise ajatõkke puhul tehke tehing iga 9-10 kuu tagant. Tarkvara pakub tavaliselt meeldetuletusi või automaatseid uuendamisfunktsioone.



### Plaani ajakohastamine



Teie Bitcoin konfiguratsioon areneb. Iga oluline muudatus (uus portfell, tähtaegade muutmine, pärandi lisamine) peab kajastuma teie dokumentatsioonis. Kehtestage iga-aastane läbivaatamisrutiin.



## Lähenemisviisi valimine



Valik erinevate lahenduste vahel sõltub teie tehnilisest profiilist ja konkreetsetest vajadustest.



**Liana** sobib töölaua kasutajatele, kes eelistavad avatud lähtekoodiga tarkvara, mida saab täielikult kontrollida oma sõlme kaudu. Konfigureerimine jääb tänu juhendatud kasutajaliidesele kättesaadavaks. Suhtelised ajavõtud (CSV) lihtsustavad hooldust, kuna teie tavapärane tegevus lükkab tähtaegu automaatselt edasi. Piirang: maksimaalne viivitus ca 15 kuud (65535 plokki).



**Bitcoin Keeper** on suunatud mobiilsetele kasutajatele, kes otsivad intuitiivset kasutajaliidest koos integreeritud kaasnevate dokumentidega. Rakendus pakub kahte tüüpi erivõti: pärimisvõti (mis lisab kvoorumi) ja hädaolukorra võti (mis möödub sellest täielikult). Absoluutsed ajavõtmed (CLTV) võimaldavad üle 15 kuu pikkust üleminekuaega, kusjuures integreeritud taastamisfunktsioon lihtsustab uuendamist. Diamond Hands plaan avab täiustatud pärandifunktsioonid.



**Pärimine** on suunatud tehnilistele kasutajatele, kes hindavad Taproot konfidentsiaalsust ja hierarhilist pärimist järkjärgulise viivitusega. Taproot puustruktuur varjab pärimistingimusi tavaliste tehingute ajal, paljastades ainult taastamise ajal kasutatava tingimuse.



Kõiki kolme lahendust ühendab üks asi: nad nõuavad perioodilist värskendamist, et vältida taastumisradade enneaegset aktiveerimist. See piirang on nii hind kui ka garantii on-chain usaldamatule pärandile. Planeerige regulaarsed meeldetuletused ja tehke see hooldus Bitcoin haldamise rutiini osaks.



## Kokkuvõte



Tehniline Bitcoin pärandkava ühendab krüptograafilised mehhanismid (ajalukud, Miniscript, Taproot) ja range dokumentatsiooni. Täiustatud rahakotid võimaldavad teil edastada oma bitcoinid automaatselt pärast tegevusetuse perioodi, ilma kolmanda osapoole sekkumiseta.



Kriitilised elemendid, mida pärandada oma pärijatele, on: kirjeldus või konfiguratsioonifail, nende taastamise fraas, üksikasjalikud taastamisjuhised ja pädevate inimeste kontaktandmed, kes saavad neid aidata.



Alustage oma profiilile sobiva tehnilise lahenduse valimisest, testige seda väikese koguse abil, seejärel dokumenteerige kogu asi struktureeritud plaanis. Esialgne keerukus tagab, et teie Bitcoin vara antakse edasi täie usaldusega.



## Ressursid



### Pärimisplaani mall





- [Bitcoin pärimisplaani mall (PDF)](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/seed-management-tools/assets/Bitcoin-Inheritance-Plan-Template.pdf) - Plan ₿ Network dokumentatsiooni mall



### Tehnilised viited





- [BIP-65 : OP_CHECKLOCKTIMEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki) - Absoluutsete ajamõõturite spetsifikatsioon (CLTV)
- [BIP-112 : OP_CHECKSEQUENCEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki) - Suhteliste ajatelgede spetsifikatsioon (CSV)
- [Miniscript Reference](https://bitcoin.sipa.be/miniscript/) - Pieter Wuille'i koostatud ametlik Miniscript dokumentatsioon



### Ametlikud lahenduse veebisaidid





- [Liana Wallet](https://wizardsardine.com/liana/) - Wizardsardine
- [Bitcoin Keeper](https://bitcoinkeeper.app/) - Bithyve
- [Heritage Wallet](https://btc-heritage.com/) - Crypto7