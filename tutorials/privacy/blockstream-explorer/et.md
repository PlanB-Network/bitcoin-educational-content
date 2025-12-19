---
name: Blockstream Explorer
description: Uurige Bitcoin ja Liquid Network põhikihti
---

![cover](assets/cover.webp)



Blockstream Explorer on projekt, mis hõlbustab tehingute ja Bitcoin protokolli globaalse seisundi uurimist, samuti [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) Liquid, mille on välja töötanud Blockstream ettevõte.



Adam Backi asutatud ettevõtte Blockstream poolt 2014. aastal algatatud [blockstream.info](https://blockstream.info) ekspluater eesmärk on pakkuda Bitcoin jaoks tugevat infrastruktuuri, mis tagab koostalitlusvõime ja tehingute jälgimise kihtide (on-chain ja Liquid) vahel, suurendades samal ajal kasutajate turvalisust ja privaatsust.



Selles õpetuses vaatleme, mis eristab seda, selle teenuseid ja seda, kuidas see pakub sujuvat järelevalvet Bitcoin on-chain ja Liquid kihtide tegevuse ja oleku üle.



## Alustamine Blockstream exploreriga



### Navigeeri põhikanalil



Kui lähete Blockstream.info ekspluater, "**Dashboard**", Bitcoin protokolli peamine kett on vaikimisi valitud. Sellest kasutajaliidesest saate ülevaate :





- Peamise keti suurus: Hiljuti kaevandatud plokid.



![blocks](assets/fr/01.webp)



Selles jaotises on teave hiljuti kaevandatud plokkide kohta, ajatempel, igas plokis sisalduvate tehingute arv, suurus kilobaitides (kB) ja iga ploki mõõtmine kaaluühikutes (**WU** = *Weight Units*). Viimane mõõtmine on huvitav, sest see võimaldab hinnata ploki optimeerimist, arvestades, et iga põhiketi plokk on piiratud `4,000,000 WU` ehk `4,000 kWU`-ga.





- Hiljutised tehingud.



![transactions](assets/fr/02.webp)



Tehingu sektsioonis on teave tehingu unikaalse identifikaatori, kaasatud bitcoini väärtuse, suuruse kohta virtuaalsetes baitides (vB) - mis kujutab endast kõigi andmete (sisend ja väljund) summat - ja sellega seotud tasumäärade kohta. Näiteks tehingu suurus on "153 vB", mille puhul on tasu "2 sat/vB" ja mis maksab "306 satoshit".



### Vedeliku uurimine



Menüüst "**Blocks**" saate jälgida kogu peamise ahela ajalugu kuni viimase kaevandatud plokini.



![blocs](assets/fr/03.webp)



Klõpsates konkreetsel plokil, saate rohkem üksikasju selles sisalduvate andmete ja tehingute kohta. Näiteks ploki 919330 puhul: näete ploki hashi. Samuti saate navigeerida eelmise ploki juurde, sest iga kaevandatud plokk (välja arvatud Genesis) on seotud eelmise plokiga, säilitades selle eelkäija hashi.



![metadata](assets/fr/04.webp)



Vajutades nupule **"Details "**, saate selle ploki kohta lisateavet, näiteks selle staatuse, mis kinnitab, et see on lisatud säilitatud ja paljundatud põhiahelasse. Teil on ka raskusaste, millega seda plokki kaevandatakse: see raskusaste esindab mining krüptograafilise probleemi lahendamiseks vajalikku arvutusvõimsust ja seda kohandatakse iga 2016 ploki (umbes 2 nädala) järel.



![details](assets/fr/05.webp)



Selle üksikasjade osa all on kõik selles plokis sisalduvad tehingud.



Kõige esimest tehingut plokis nimetatakse **transaktsiooniks coinbase**. Seda kasutatakse kaevandaja mining tasu (kõik plokis sisalduvate tehingute ja plokkide toetusega seotud tasud) eraldamiseks. Selle tehinguga loodud bitcoine saab kulutada alles siis, kui on kaevandatud veel 100 järjestikust plokki. Teisisõnu, et neid kasutada, peab kaevandaja ootama ploki **919430** tootmist. Seda nimetatakse [*"küpsusperioodiks "*](https://planb.academy/fr/resources/glossary/maturity-period).



Coinbase on eriline tehing: see on ainus, millel puudub tegelik sisend, kuna see ei kuluta ühtegi bitcoin'i eelmisest tehingust.




![coinbase](assets/fr/06.webp)



Kõik muud tehingud on jagatud kahte ossa: sisendid ja väljundid.



Selleks, et bitcoin'e saaks kasutada uues tehingus sisendina, peab tehingu algataja tõendama oma valdust, andes allkirja, mis vastab konkreetsele skriptile. Iga bitcoin (UTXO) sisaldab skripti, mis nõuab üldiselt konkreetset allkirja, mida saab anda ainult omaniku privaatvõti. Need skriptid on ***scriptSig*** (ASMis), mis on kirjutatud Bitcoin skriptis ja võivad olla erinevat tüüpi. Selles näites näeme, et kasutatud UTXOd olid P2SH tüüpi P2WPKH tüüpi väljundile (*Pay-to-Witness-Public-Key-Hash*).



Te saate jälgida konkreetse UTXO ajalugu, kasutades heuristikat. Kutsume teid üles avastama erinevaid Bitcoin heuristikuid ja viise, kuidas tugevdada oma tehingute konfidentsiaalsust Bitcoin :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Võtame näiteks selle tehingu väljamineva kulu. Tehingu identifikaatorile klõpsates suunatakse meid ümber tehingu üksikasjade lehe jaotisse **Tehingud**.



![transaction](assets/fr/08.webp)



Sellelt lehelt saate teada, millisesse plokki tehing kuulus. Sõltuvalt kasutatud aadressi tüübist võib tehing optimeerida oma andmeid (*virtuaalsed baitid*) ja seega maksta vähem tehingutasusid. See tehing näiteks säästis 53% tasusid, kasutades algupärast SegWit Bech32 aadressiformaati, mis algab sõnaga `bc1q`.



![trx_details](assets/fr/09.webp)



## Liquid kiht



Liquid Network on [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) ja avatud lähtekoodiga 2. taseme lahendus Bitcoin protokollile. Eelkõige võimaldab see kiiremaid ja konfidentsiaalsemaid bitcoin-tehinguid.



Klõpsake Blockstream.info eksplortersüsteemis nupule **"Liquid"**, et minna üle Liquid võrku.



![liquid](assets/fr/10.webp)



Klõpsates ühel tehingul, mida me tahame jälgida, näeme, et bitcoini tükisummad on asendatud sõnadega "**Confidential**". Selles võrgus võivad tehingud olla konfidentsiaalsed, nii et me ei näe iga UTXO summasid, ei tehingu sisse- ega väljapoole.



![liquid_trx](assets/fr/11.webp)



Siiski märgime, et Bitcoin protokolli põhikihis esinevad põhimõtted ja mehhanismid on samad: bitcoini lukustusskriptid ja UTXO jälgitavus.



![liquid_details](assets/fr/12.webp)



Liquid Network pakub ka mittedepositoorseid digitaalseid varasid, mida organisatsioonid saavad kasutada. Menüüst **"Varad "** leiate nimekirja registreeritud varadest, nende kogusummast ja domeenist, millega nad on seotud.



![assets](assets/fr/13.webp)



Iga vara puhul saate jälgida emissiooni- ja põletustehingute ajalugu (kustutades kogu ringluses oleva summa).



![assets_trxs](assets/fr/14.webp)




## Rohkem võimalusi



Blockstream.info ekspluater sisaldab ka visualiseeringuid ja tehingute jälgimist Testnet, Bitcoin, on-chain ja Liquid Network kohta.



![testnet](assets/fr/15.webp)



Kui kasutate Testnet võrku, siis ei kasuta te päris bitcoin'e, kuid teil on olemas kõik eespool kirjeldatud funktsioonid.



![liquid_testnet](assets/fr/16.webp)



Selles võrgus on erinev ahelapikkus, millega saab ühendada ja katsetada Bitcoin ja Liquid mehhanismide tööd.





- API jaotis on mõeldud kõigile, kes soovivad integreerida teatud Exploreri funktsioone oma rakendusse. Selle API kaudu saab küsitleda erinevate kihtide (on-chain ja Liquid) põhiahelat, jälgida tehinguid ja teada saada näiteks tehingute keskmisi tasusid mingis plokis.



![api](assets/fr/17.webp)



Nüüd olete valmis kasutama Blockstream Exploreri täielikku potentsiaali plokiahelate päringute tegemiseks on-chain ja Liquid kihtidel. Loodame, et leidsite selle õpetuse informatiivseks ja soovitame meie õpetust teise Bitcoin exploreri kohta:



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f