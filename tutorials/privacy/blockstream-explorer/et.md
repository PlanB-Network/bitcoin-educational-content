---
name: BLOCKSTREAM Explorer
description: Uurige Bitcoin ja Liquid Network peamist Layer
---

![cover](assets/cover.webp)



BLOCKSTREAM Explorer on projekt, mis hõlbustab tehingute ja Bitcoin protokolli Global State ning BLOCKSTREAM ettevõtte poolt välja töötatud [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) Liquid uurimist.



Adam Backi asutatud ettevõtte BLOCKSTREAM poolt 2014. aastal algatatud [BLOCKSTREAM.info](https://BLOCKSTREAM.info) exploreri eesmärk on pakkuda Bitcoin jaoks tugevat infrastruktuuri, mis tagab koostalitlusvõime ja tehingute jälgimise kihtide (On-Chain ja Liquid) vahel, suurendades samal ajal kasutajate turvalisust ja privaatsust.



Selles õppematerjalis tutvustame, mille poolest see erineb, selle teenuseid ja seda, kuidas see pakub sujuvat järelevalvet Bitcoin On-Chain ja Liquid kihtide tegevuse ja oleku üle.



## BLOCKSTREAM kasutamise alustamine



### Navigeeri põhikanalil



Kui lähete BLOCKSTREAM.info ekspluaterisse, on "**Kaardil**" vaikimisi valitud Bitcoin põhiprotokolli kanal. Sellest Interface, teil on ülevaade :





- Peamise keti suurus: Hiljuti kaevandatud plokid.



![blocks](assets/fr/01.webp)



Selles jaotises on esitatud teave hiljuti kaevandatud plokkide, Timestamp, igas BLOCK sisalduvate tehingute arvu, suuruse kilobaitides (kB) ja iga BLOCK mõõtmise kohta kaaluühikutes (**WU** = *Weight Units*). Viimane mõõtmine on huvitav, sest see võimaldab hinnata BLOCK optimeerimist, arvestades, et iga BLOCK põhiahelas on piiratud `4,000,000 WU` ehk `4,000 kWU`.





- Hiljutised tehingud.



![transactions](assets/fr/02.webp)



Tehingu osa annab teavet tehingu unikaalse identifikaatori, asjaomase Bitcoin väärtuse, suuruse virtuaalsetes baitides (vB) - mis kujutab endast kõigi andmete (sisend- ja väljundandmed) summat - ja sellega seotud maksumäära kohta. Näiteks tehing, mille suurus on "153 vB" ja määr "2 sat/vB", maksab "306 satoshit".



### Vedeliku uurimine



Menüüst "**Blocks**" saate jälgida kogu peamise ahela ajalugu kuni viimase kaevandatud BLOCK-ni.



![blocs](assets/fr/03.webp)



Kui klõpsate konkreetsel BLOCK-l, saate lisateavet selles sisalduvate andmete ja tehingute kohta. Näiteks BLOCK 919330 puhul: teil on Hash BLOCK. Samuti saate navigeerida eelmise BLOCK juurde, sest iga kaevandatud BLOCK (välja arvatud Genesis) on seotud eelmise BLOCK-ga, säilitades selle eelkäija Hash.



![metadata](assets/fr/04.webp)



Vajutades nupule **"Details "**, saate selle BLOCK kohta lisateavet, näiteks selle staatuse, mis kinnitab, et see on lisatud säilitatud ja paljundatud põhiahelasse. Teil on ka raskusaste, millega seda BLOCK kaevandatakse: see raskusaste kujutab endast Mining krüptograafilise probleemi lahendamiseks vajalikku arvutusvõimsust ja seda kohandatakse iga 2016 ploki (umbes 2 nädala) järel.



![details](assets/fr/05.webp)



Selle üksikasjade osa all on esitatud kõik selles BLOCK-s sisalduvad tehingud.



Kõige esimene tehing BLOCK-s on nn **transiit coinbase**. Seda kasutatakse Miner Mining tasu (kõik BLOCK ja BLOCK toetuses sisalduvate tehingutega seotud tasud) eraldamiseks. Selle tehinguga loodud bitcoine saab kulutada alles siis, kui on kaevandatud veel 100 järjestikust plokki. Teisisõnu, selleks, et neid kasutada, peab Miner ootama BLOCK **919430** tootmist. Seda nimetatakse [*"küpsusperioodiks "*](https://planb.network/fr/resources/glossary/maturity-period).



Coinbase on eriline tehing: see on ainus, millel puudub tegelik sisend, kuna see ei kuluta ühtegi bitcoin'i eelmisest tehingust.




![coinbase](assets/fr/06.webp)



Kõik muud tehingud on jagatud kahte ossa: sisendid ja väljundid.



Selleks, et bitcoin'e saaks kasutada uue tehingu sisendina, peab tehingu algataja tõestama oma valdust, andes allkirja, mis vastab konkreetsele skriptile. Iga bitcoin (UTXO) sisaldab skripti, mis nõuab üldiselt konkreetset allkirja, mida saab anda ainult omaniku privaatvõti. Need skriptid on ***scriptSig*** (ASMis), mis on kirjutatud Bitcoin Script'is ja võivad olla erinevat tüüpi. Selles näites näeme, et kasutatud UTXOd olid P2SH tüüpi P2WPKH tüüpi väljundile (*Pay-to-Witness-Public-Key-Hash*).



Te saate jälgida konkreetse UTXO ajalugu, kasutades heuristikat. Kutsume teid üles avastama erinevaid Bitcoin heuristikuid ja seda, kuidas tugevdada oma Bitcoin tehingute konfidentsiaalsust:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Võtame näiteks selle tehingu väljamineva kulu. Tehingu identifikaatorile klõpsates suunatakse meid ümber tehingu üksikasjade lehe jaotisse **Tehingud**.



![transaction](assets/fr/08.webp)



Sellelt leheküljelt saate teada, millise BLOCK alla tehing kuulus. Sõltuvalt kasutatud Address tüübist võib tehing optimeerida oma andmeid (*virtuaalsed baitid*) ja seega maksta vähem tehingutasusid. See tehing näiteks säästis 53% tasusid, kasutades algupärast SegWit BECH32 Address formaati, mis algab `bc1q`.



![trx_details](assets/fr/09.webp)



## Liquid kate



Liquid Network on [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) ja 2. taseme avatud lähtekoodiga lahendus Bitcoin protokollile. Eelkõige võimaldab see kiiremaid ja konfidentsiaalsemaid Bitcoin tehinguid.



BLOCKSTREAM.info eksplorters klõpsake nupule **"Liquid"**, et minna üle Liquid Network-le.



![liquid](assets/fr/10.webp)



Klõpsates ühel tehingul, mida soovime jälgida, näeme, et Bitcoin tükkide summad on asendatud sõnadega "**Confidential**". Selles võrgus võivad tehingud olla konfidentsiaalsed, nii et me ei näe iga UTXO summasid, ei tehingu sees ega väljaspool tehingut.



![liquid_trx](assets/fr/11.webp)



Siiski märgime, et Bitcoin protokolli Layer peamistel Bitcoin põhimõtetel ja mehhanismidel on samad: Bitcoin lukustusskriptid ja UTXO jälgitavus.



![liquid_details](assets/fr/12.webp)



Liquid Network pakub ka mittedepositoorseid digitaalseid varasid, mida organisatsioonid saavad kasutada. Menüüst **"Varad "** leiate nimekirja registreeritud varadest, nende kogusummast ja domeenist, millega nad on seotud.



![assets](assets/fr/13.webp)



Iga vara puhul saate jälgida emissiooni- ja põletustehingute ajalugu (kustutades kogu ringluses oleva summa).



![assets_trxs](assets/fr/14.webp)




## Rohkem võimalusi



BLOCKSTREAM.info explorer sisaldab ka Testnet, Bitcoin, On-Chain ja Liquid Network tehingute visualiseerimist ja jälgimist.



![testnet](assets/fr/15.webp)



Testnet võrku minnes ei kasuta sa küll reaalseid bitcoin'e, kuid sul on olemas kõik eespool kirjeldatud funktsioonid.



![liquid_testnet](assets/fr/16.webp)



Selles võrgus on erinev ahelapikkus, millega saab ühendada ja katsetada Bitcoin ja Liquid mehhanismide tööd.





- API sektsioon on mõeldud kõigile, kes soovivad integreerida teatud Exploreri funktsioone oma rakendusse. Selle API kaudu saate küsitleda erinevate kihtide (On-Chain ja Liquid) põhiahelat, jälgida tehinguid ja leida näiteks BLOCK tehingute keskmisi tasusid.



![api](assets/fr/17.webp)



Nüüd olete valmis kasutama BLOCKSTREAM Exploreri kogu potentsiaali, et teha päringuid plokiahelate kohta On-Chain ja Liquid kihil. Loodame, et leidsite selle õpetuse informatiivseks ja soovitame meie õpetust teise Bitcoin Exploreri kohta:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f