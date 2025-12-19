---
name: Ashigaru - Whirlpool Coinjoin
description: Kuidas teha Ashigaru rakenduses coinjoins?
---

![cover](assets/cover.webp)



"*Bitcoin wallet tänavate jaoks*"



Selles õpetuses saate teada, mis on coinjoin ja kuidas seda teha Ashigaru terminali rakendusega ja Whirlpool rakendusega, mis on Samourai Wallet-st pärinev coinjoin-protokoll.



## Kuidas Whirlpool koosliitmikud toimivad



Selles õpetuses ei hakka ma uuesti üle vaatama mündiühendi mõistet, selle kasulikkust või Whirlpool teoreetilist toimimist, kuna neid teemasid on juba üksikasjalikult selgitatud Plan ₿ Academy's BTC 204 koolituskursuse 5. osas. Kui te ei ole veel omandanud Whirlpool toimimist või coinjoini põhimõtet, soovitan teil enne jätkamist tungivalt tutvuda selle 5. osaga :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Siin on siiski mõned kiired faktid ja arvud, mis võivad olla kasulikud.



Whirlpool ühilduvates portfellides kasutatakse 4 eraldi kontot, et täita coinjoin-protsessi vajadusi:




- Konto **Deposiit**, mis on identifitseeritud indeksiga `0'` ;
- **Paha panga** (või *doksilise vahetuse*) konto, mida tähistatakse indeksiga `2,147,483,644'` ;
- **Premix** konto, mida tähistatakse indeksiga "2 147 483 645'`" ;
- **Postmix** konto, mida tähistatakse indeksiga "2 147 483 646".



Ashigarul on novembris 2025 saadaval kaks basseinide nimiväärtust (see nimekiri tõenäoliselt areneb lähikuudel: nii et ärge unustage lugedes väärtusi kontrollida):




- 0.25 BTC`, osalustasu on `0,0125 BTC`;
- 0.025 BTC, osalustasu on 0,00125 BTC.



Iga segamistsükkel võib hõlmata 5 kuni 10 UTXO-d sisend- ja väljundis.



![Image](assets/fr/01.webp)



## Tarkvaranõuded



Whirlpool-ga koosliidete tegemiseks on vaja kolme eraldi programmi:





- Ashigaru Terminal**, mis võimaldab teil hallata oma mündiliite otse arvutist;



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add



- Ashigaru Wallet**, rakendus teie nutitelefonis, mille abil saate oma bitcoin'id *postmix*-s kõikjal kulutada;



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f



- Dojo**, Bitcoin sõlme rakendamine, mis tagab teile suveräänse ühenduse võrguga, sõltumata kolmanda osapoole serverist.



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Installige kõik need tööriistad, järgides nende vastavaid õpetusi, seejärel võite alustada oma esimeste ühisliidete tegemist.



## Bitcoinide vastuvõtmine



Pärast portfelli loomist alustate ühe kontoga, mida tähistab indeks "0". See on `Deposit` konto. Sellele kontole saadate coinjoins'ile mõeldud bitcoine. Saate neid kas Ashigaru rakenduse kaudu (vt spetsiaalse õpetuse 5. osa) või Ashigaru terminali kaudu (samuti üksikasjalikult spetsiaalse õpetuse 5. osas).



Kui teie deposiitkontol on vähemalt väikseimas basseinis osalemiseks vajalik summa (pluss teenustasud ja mining kulude katmiseks vajalik miinimum), olete valmis algatama oma esimesed coinjoins'id.



![Image](assets/fr/02.webp)



## Tee Tx0



Kui raha on teie hoiukontole laekunud ja tehing on kinnitatud, saate alustada coinjoin'i protsessi. Selleks avage Ashigaru terminalis menüü "Rahakotid" ja valige oma wallet. Kui teie wallet on lukustatud, küsib tarkvara teilt parooli ja passphrase.



![Image](assets/fr/03.webp)



Seejärel valige konto "Deposiit".



![Image](assets/fr/04.webp)



Minge menüüsse `UTXOs`.



![Image](assets/fr/05.webp)



Siin näete nimekirja kõigist UTXOdest teie hoiukontol. Valige need, mida soovite saata coinjoini tsüklitesse.



Suurema konfidentsiaalsuse tagamiseks ja *Common Input Ownership Heuristic (CIOH)* vältimiseks on soovitatav kasutada Whirlpool-s ainult ühte UTXO sisendi kohta (selle põhimõtte üksikasjalik selgitus on esitatud dokumendis BTC 204).



Vajutage klaviatuuril klahvi "ENTER", et valida UTXO: selle kõrvale ilmub tärn "*", mis näitab, et see on valitud.



![Image](assets/fr/06.webp)



Seejärel klõpsake nupul `Mix Selected`.



![Image](assets/fr/07.webp)



Kui teil on piisavalt suur UTXO, et osaleda ühes kahest olemasolevast basseinist, saate sihtbasseini valida noolte abil. Sellel lehel näete oma Tx0 üksikasju:




- reservi sisenevate UTXOde arv;
- erinevad kohaldatavad tasud (teenustasud ja mining tasud) ;
- *doksilise muutuse* suurus.



Kontrollige hoolikalt teavet, seejärel klõpsake Tx0 edastamiseks nuppu `Broadcast`.



![Image](assets/fr/08.webp)



Ashigaru kuvab seejärel teie Tx0 TXID, kinnitades, et tehing on võrgus edastatud.



![Image](assets/fr/09.webp)



## Koosliidete tegemine



Kui Tx0 on eetrisse saadetud, naasta oma hoiukonto avalehele, seejärel klõpsa "Kontod" ja vali "Premix" konto.



![Image](assets/fr/10.webp)



Menüüs `UTXOs` näete erinevaid tasandatud osi, mis on valmis sisestama coinjoin tsüklit. Niipea, kui Tx0 on kinnitatud, alustab Ashigaru Terminal automaatselt oma esimest segamistsüklit.



![Image](assets/fr/11.webp)



Kui Tx0 on kinnitatud, luuakse ja edastatakse Ashigaru terminalis automaatselt esimene mündiühendustehing. Minnes `Kontod > Postmix > UTXOs`, saate vaadata oma tasandatud UTXOsid, mis ootavad oma esimese tsükli kinnitust.



![Image](assets/fr/12.webp)



Nüüd võite Ashigaru Terminalit taustal töötama jätta: see jätkab teie lugude automaatset miksimist ja remiximist.



## Ühisliidete viimistlemine



Nüüd saate lasta oma müntidel end automaatselt remixida. Whirlpool mudel tähendab, et remiximise eest ei võeta lisatasusid: ei teenustasusid, ei mining tasusid. Nii et kui te lasete oma müntidel osaleda rohkemates segamistsüklites, võib see teie konfidentsiaalsusele ainult kasuks tulla.



Selle mehhanismi paremaks mõistmiseks ja selle kohta, mitu tsüklit tasub oodata, soovitan lugeda seda artiklit:



https://planb.academy/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

Et vaadata iga teie teose poolt tehtud remixide arvu, avage "Postmix"-konto menüü "UTXOs".



![Image](assets/fr/13.webp)



Segamüntide kulutamiseks minge Ashigaru rakendusse, mis kasutab sama wallet kui teie Ashigaru terminali tarkvara. Avamisel kuvatav wallet vastab teie "deposiitkontole". Postmix-kontole pääsemiseks, mis sisaldab teie segatud UTXOsid, klõpsake üleval paremas nurgas olevale Whirlpool sümbolile.



![Image](assets/fr/14.webp)



Sellel kontol näete kõiki oma münte, mida praegu segatakse. Nende kulutamiseks vajutage ekraani paremas allosas olevale sümbolile "+" ja valige seejärel "Saada".



![Image](assets/fr/15.webp)



Täitke oma tehingu üksikasjad: saaja aadress, saadetav summa ja soovi korral valige konkreetne tehingu struktuur, et suurendada konfidentsiaalsust (vt vastavaid õpetusi).



![Image](assets/fr/16.webp)



Kontrollige hoolikalt tehingu üksikasju, seejärel lohistage saadetise kinnitamiseks ekraani allosas olevat noolt.



![Image](assets/fr/17.webp)



Teie tehing on allkirjastatud ja edastatud Bitcoin võrgus.



![Image](assets/fr/18.webp)



## Kuluta Doxxic Change



Pea meeles: Whirlpool mudel põhineb teie tükkide võrdsustamisel Tx0 juures, enne nende sisenemist basseinidesse. Just see mehhanism rikub UTXOde jälgimise. Minu arvates on see kõige tõhusam coinjoin-mudel, kuid sellel on üks puudus: see tekitab *muutuse*, mis ei lähe läbi coinjoin-protsessi.



See muudatus vastab igale Tx0 jaoks loodud UTXO-le. See on isoleeritud spetsiaalsesse kontosse nimega `Doxxic Change` või `Bad Bank`, sõltuvalt tarkvarast, et vältida selle kasutamist koos oma teiste UTXOdega. See on väga oluline, sest neid UTXOsid ei ole segatud: nende jälgitavuse lingid jäävad puutumatuks ja nad võivad ohustada teie konfidentsiaalsust, luues ühenduse teie ja teie mündiühendustegevuse vahel. Seega käsitsege neid ettevaatlikult ja **ei tohi neid kunagi kasutada koos teiste UTXOdega**, olenemata sellest, kas neid on segatud või mitte. Mürgise UTXO kombineerimine segatud UTXO-ga hävitab kõik privaatsuse eelised, mida te olete saanud coinjoiningust.



Hetkel ei paku Ashigaru otsest ligipääsu sellele `Doxxic Change` kontole (vähemalt mina ei ole seda leidnud). See funktsioon lisatakse ilmselt mõne tulevase uuendusega. Vahepeal on ainus võimalus neid vahendeid kätte saada, kui importida oma seed Sparrow Wallet. Viimane tuvastab tavaliselt automaatselt, et tegemist on wallet-ga, mida kasutatakse koos Whirlpool-ga, ja annab teile juurdepääsu kõigile neljale kontole, sealhulgas `Doxxic Change` kontole. Seejärel saate neid UTXOsid kulutada nagu tavalisi bitcoin'e Sparrow-st.



Siin on mitu võimalikku strateegiat, kuidas hallata oma välisvaluuta UTXOs alates coinjoins ilma privaatsust ohustamata:





- Segamine väiksematesse basseinidesse:** Kui teie mürgine UTXO on piisavalt suur, et liituda väiksema basseiniga, on see üldiselt parim variant. Olge siiski ettevaatlik, et te ei ühendaks selle saavutamiseks kunagi mitut mürgist UTXOd, sest see loob teie erinevate kirjete vahel seose Whirlpool-s.





- Märkige need mittekasutatavaks:** Teine mõistlik lähenemisviis on lihtsalt jätta need eraldi kontole nii, nagu nad on, ja jätta need puutumata. See hoiab ära, et te neid kogemata kulutaksite. Kui bitcoinide väärtus tõuseb, võib avada uusi, nende suurusele kohandatud poole.





- Tehke annetusi:** Te võite muuta need mürgised UTXO-d annetusteks Bitcoin arendajatele, avatud lähtekoodiga projektidele või ühendustele, mis aktsepteerivad BTC-d. See võimaldab teil neid kasulikult kõrvaldada ja samal ajal ökosüsteemi toetada.





- Osta ettemakstud kinkekaarte või Visa-kaarte:** Platvormid nagu [Bitrefill](https://www.bitrefill.com/) võimaldavad teil vahetada oma bitcoinid kinkekaartide või taaslaetavate Visa-kaartide vastu, mida saab kasutada kauplustes. See võib olla lihtne ja diskreetne viis oma mürgiste UTXOde kulutamiseks.





- Vahetage need Monero vastu:** Samourai Wallet pakkus varem BTC/XMR aatomivahetusteenust, mis on nüüdseks kadunud. Kui sarnane teenus on olemas (ma ei tea isiklikult ühtegi), on see suurepärane lahendus nende UTXOde isoleerimiseks, nende konverteerimiseks Monero'ks ja seejärel lõpuks nende saatmiseks tagasi Bitcoin-le. See meetod oli aga kallis ja sõltus olemasolevast likviidsusest.





- Viige need üle Lightning Network-sse:** Nende UTXOde üleviimine Lightning Network-sse, et saada kasu vähendatud tehingutasudest, on potentsiaalselt huvitav võimalus. See meetod võib aga sõltuvalt Lightning'i kasutamisest avaldada teatud teavet ja seetõttu tuleks seda kasutada ettevaatlikult.



## Kuidas ma saan teada, milline on meie coinjoin'i tsüklite kvaliteet?



Selleks, et coinjoin oleks tõeliselt tõhus, peab see olema sisend- ja väljundkoguste vahel väga ühtlane. Selline ühtsus suurendab välise vaatleja jaoks võimalike tõlgenduste arvu, mis omakorda suurendab tehingu ebakindlust. Selle ebakindluse mõõtmiseks kasutame tehingu suhtes kohaldatavat entroopia mõistet. Whirlpool mudelit peetakse selles osas üheks kõige tõhusamaks, kuna see tagab osalejate vahelise suurepärase homogeensuse. Selle põhimõtte põhjalikumaks käsitlemiseks soovitan teil tutvuda BTC 204 koolituskursuse 5. osa viimase peatükiga.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Mitme mündiühendustsükli jõudlust mõõdetakse nende koguste suuruse järgi, millesse mündi on peidetud. Need komplektid määratlevad nn *anonsetid*. Neid on kahte tüüpi: esimene mõõdab konfidentsiaalsust retrospektiivse analüüsi suhtes (olevikust minevikku) ja teine mõõdab vastupanu prospektiivsele analüüsile (minevikust olevikku). Nende kahe näitaja täielikuks selgitamiseks lugege palun järgmist õpetust (või veel kord BTC 204 koolituskursust):



https://planb.academy/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

## Kuidas hallata postmixi?



Pärast mitme coinjoin'i tsükli läbimist on parim strateegia hoida oma UTXO-d "Postmix"-kontol, lastes neil lõputult remixida, kuni teil on neid tõesti vaja kulutada.



Mõned kasutajad eelistavad kanda oma segatud bitcoinid wallet riistvaraga tagatud wallet-le. See võimalus on võimalik, kuid nõuab teatavat rangust, et tagada mündiühendustega omandatud konfidentsiaalsus ei satuks ohtu.



UTXOde ühendamine on kõige sagedamini esinev viga. Oluline on, et kunagi ei kombineeritaks segatud UTXOsid segamata UTXOdega samas tehingus, sest vastasel juhul on oht, et käivitub *Common Input Ownership Heuristic (CIOH)*. See eeldab teie UTXOde ranget haldamist, eelkõige selge ja täpse märgistamise kaudu. Üldiselt on UTXOde ühendamine halb tava, mis toob sageli kaasa konfidentsiaalsuse kaotuse, kui seda halvasti hallatakse.



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Samuti peaksite olema ettevaatlik segatud UTXOde konsolideerimise suhtes. Piiratud konsolideerimist võib kaaluda, kui UTXO-del on märkimisväärne anonset, kuid see vähendab paratamatult teie konfidentsiaalsuse taset. Vältige massilisi või kiirustatud konsolideerimisi, mis tehakse enne piisava arvu taasühendusi, sest need võivad luua järelduslike seoseid teie eel- ja järelühenduste vahel. Kahtluse korral on kõige parem mitte konsolideerida oma postmix UTXOd ja kanda need ükshaaval üle oma wallet riistvarale, genereerides iga kord uue tühja vastuvõtu aadressi. Ärge unustage märgistada iga üle kantud UTXO.



Soovitame tungivalt vältida oma UTXOde postmix portfellidesse liigutamist, kasutades vähemuste skripte. Näiteks kui te osalesite Whirlpool portfellist multi-sig portfellis `P2WSH`, siis on vähe neid, kes jagavad seda tüüpi skripti. Kui saadate oma postmix UTXO-d sellesse samasse skriptitüüpi, vähendate oluliselt oma anonüümsust. Lisaks skripti tüübile võivad muud konkreetsed wallet sõrmejäljed ohustada teie konfidentsiaalsust, seega on parim, mida teete, kui kulutate neid Ashigaru rakendusest.



Lõpetuseks, nagu kõigi Bitcoin tehingute puhul, ärge kunagi kasutage vastuvõtuaadressi uuesti. Iga makse tuleb saata uuele, unikaalsele, tühjale aadressile.



Kõige lihtsam ja turvalisem meetod on lasta oma segatud UTXO-d oma "Postmix" kontol puhata, lasta neil loomulikult remixida ja kulutada neid ainult siis, kui neid on vaja Ashigarust.



Ashigaru ja Sparrow rahakotid sisaldavad täiendavaid kaitsemeetmeid plokiahela analüüsiga seotud kõige tavalisemate vigade vastu, aidates teil säilitada oma tehingute konfidentsiaalsust.