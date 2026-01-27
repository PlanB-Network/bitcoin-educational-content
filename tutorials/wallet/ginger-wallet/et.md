---
name: Ginger Wallet
description: Avatud lähtekoodiga, isehaldatav Bitcoin wallet tarkvara, fork Wasabi Wallet-st, integreerides Coinjoins'i
---
![cover](assets/cover.webp)



Ginger Wallet on avatud lähtekoodiga, mittekaitstav Bitcoin portfell, mis keskendub konfidentsiaalsusele ja privaatsusele. See sai alguse fork-na Wasabi Wallet-st (pärast versiooni 2.0.7.2 - MIT litsents).



Ginger Wallet säilitab Wasabi tehnilise ülesehituse, lisades samas mõned eripärad. [Ginger Wallet dokumentatsiooni](https://docs.gingerwallet.io/why-ginger/difference.html#gingerwallet) kohaselt rõhutab Wasabi **autonoomiat ja kontrolli**, samas kui Ginger keskendub **kasutusele, turvalisusele ja lihtsustatud kasutuskogemusele**, muutes selle kättesaadavaks neile, kes on tehniliste aspektidega vähem kursis.



Ginger Wallet on wallet tarkvara ainult arvutitele (mobiilirakendus puudub).



## Mis on Coinjoin?



**coinjoin** on spetsiaalne Bitcoin tehingustruktuur, mis ühendab mitu osalejat ühte ühistehingusse. See mehhanism segab erinevate kasutajate kirjed ühiseks tehinguks, mis teeb raha jälgimise äärmiselt keeruliseks - kui mitte sageli võimatuks, kui seda õigesti teha -. Selle tulemusel on välise vaatleja jaoks peaaegu võimatu kindlalt tuvastada kaasatud bitcoinide päritolu ja sihtkohta, erinevalt tavapärastest Bitcoin tehingutest.



Teie kui kasutaja jaoks aitab coinjoin säilitada teie konfidentsiaalsust. Näiteks kui saate 10 000 sats annetuse Bitcoin aadressile, saab saatja neid vahendeid jälgida ja mõnel juhul järeldada, et teil on suurem kogus bitcoine, või jälgida teie tegevust. Kui teete pärast seda 10 000 sats annetust coinjoini, katkestate jälgitavuse: saatja ei saa sellest maksest enam teie kohta mingit teavet tuletada.



Chaumian coinjoin pakub kõrgetasemelist turvalisust, kuna raha jääb alati kasutaja ainukontrolli alla. Isegi koordineerivate serverite operaatorid ei saa mingil juhul osalejate bitcoin'e ümber suunata. Ei kasutajad ega koordinaatorid ei pea üksteist usaldama: kumbki säilitab kontrolli oma isiklike võtmete üle ja on ainuüksi volitatud tehingute kinnitamiseks. Ükski kolmas isik ei saa seega teie bitcoin'eid coinjoin'i ajal omastada ega luua otsest seost teie sisendite ja väljundite vahel.



Et rohkem teada saada coinjoinist, vaata Plan ₿ Akadeemia BTC 204 kursust :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Paigaldage Ginger Wallet



Ginger Wallet paigaldamiseks külastage veebisaiti [Ginger Wallet](https://gingerwallet.io).



Vajutage **Download**, et laadida alla õige versioon oma arvutile (Windows / MacOs / Linux).



![screen](assets/fr/03.webp)



Teine võimalus on minna projekti [GitHub](https://github.com/GingerPrivacy/GingerWallet/releases) alla laadida.



![screen](assets/fr/04.webp)



Seejärel käivitage paigaldusprogramm.



![screen](assets/fr/05.webp)




## Parameetrite seaded



### Esialgsed konfiguratsioonid



Avage Ginger Wallet, valige oma eelistatud keel.



![screen](assets/fr/06.webp)



Ginger tuletab teile kohe alguses meelde, millised kulud kaasnevad coinjoin-protsessiga.



![screen](assets/fr/07.webp)



Seejärel vajutage **Start**, seejärel **Uue**, et luua uus portfell.



![screen](assets/fr/08.webp)



Seejärel salvestage ja kinnitage oma seedphrase.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![screen](assets/fr/09.webp)



![screen](assets/fr/10.webp)



Ginger Wallet annab teile lisaturvalisuse tagamiseks võimaluse lisada passphrase.



![screen](assets/fr/11.webp)



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Kui see passphrase on lisatud, küsitakse seda iga kord, kui püüate oma portfellile ligi pääseda.



![screen](assets/fr/12.webp)



Ginger aktiveerib portfelli loomisel automaatselt vaikimisi **Coinjoin**. Teid teavitatakse sellest ja seejärel saate seadistust kohandada vastavalt oma vajadustele.



![screen](assets/fr/13.webp)




### Üldised seaded



Kui olete loonud oma esimese portfoolio, jõuate Ginger Wallet kasutajaliidesesse.



![screen](assets/fr/14.webp)



Aktiveerige **Discreet mode**, kui soovite oma rahakoti saldot varjata.



![screen](assets/fr/15.webp)



Ginger Wallet-s saate luua mitu portfelli. Lihtsalt klõpsake **Lisata portfoolio**.



![screen](assets/fr/16.webp)



Ginger toetab riistvaraportfellide kasutamist standardse Bitcoin Core-liidese kaudu, kuigi otsene integratsioon riistvaraportfellist või riistvaraportfellile ei ole veel võimalik.



Ühilduvate riistvaraportfellide hulka kuuluvad (kuid mitte ainult) :




- Blockstream Jade
- Coldcard MK4
- Coldcard Q
- Ledger Nano S Plus
- Ledger Nano X
- Trezor mudel T
- Trezor Safe 3
- jne.



Nüüd klõpsake **Settings**.



![screen](assets/fr/17.webp)



Need seaded on rakenduse üldised seaded ja seal tehtud seadistused kehtivad kõigile portfellidele.



Seadistustes** on vahekaardid :





- Üldine**



![screen](assets/fr/18.webp)





- Välimus



Sellel vahekaardil saate muu hulgas muuta keelt, valuutat ja tasu kuvamise ühikut (BTC/Satoshi).



![screen](assets/fr/19.webp)





- Bitcoin**



Sellel vahekaardil saate lubada Bitcoin Knots käivitada rakenduse käivitamisel, valida oma võrgu (Main/RegTest) ja oma laadimismäära pakkuja (Mempool Space/Blockstream info/Full Node) jne.



![screen](assets/fr/20.webp)





- Ohutusfunktsioonid**



Vahekaardil Turvalisus saate lubada kahefaktorilist autentimist, aktiveerida või deaktiveerida Tori ja isegi keelata selle, kui Gingeri rakendus on suletud.



![screen](assets/fr/21.webp)



**NB** :




- Kahefaktorilise autentimise puhul veenduge, et teie autentimisrakendus toetab SHA256-protokolli ja 8-kohalisi koode. Ginger Wallet nõuab turvalisuse suurendamiseks 8-kohalist 2FA-koodi. Selle pikema formaadi tõttu on koodi palju raskem ära arvata või kompromiteerida, pakkudes suuremat kaitset volitamata juurdepääsu eest.
- Vaikimisi läbib kogu Gingeri võrguliiklus Tori, mis välistab vajaduse käsitsi konfigureerida. Kui Tor on teie süsteemis juba aktiivne, annab Ginger sellele automaatselt prioriteedi.



Kui te aga Tor'i seadetes deaktiveerite, jääb teie privaatsus üldjuhul alles, välja arvatud kahes olukorras:




- coinjoini ajal võib koordinaator teie sisendid ja väljundid siduda teie IP-aadressiga;
- tehingu edastamisel võib pahatahtlik sõlmpunkt, millega te ühendute, seostada teie tehingu teie IP-ga.



Ärge unustage iga kord vajutada **Done** (all paremas nurgas), et salvestada oma seaded. Mõne seadistuse jõustumiseks tuleb Ginger Wallet uuesti käivitada.



Lisaks võimaldab portfellide ülaosas olev otsinguriba otsida ja kasutada mis tahes parameetrit jne...



![screen](assets/fr/22.webp)




### Portfelli konfiguratsioon



Rakenduses saab luua mitu portfelli, nii et iga portfelli saab konfigureerida vastavalt oma vajadustele. Selleks klõpsake portfelli nime ees oleval **kolm punkti** ja seejärel **Portfelli seaded**.



![screen](assets/fr/23.webp)



Nagu näete, saate lisaks wallet parameetrile näha ka oma UTXOsid (teile kuuluvate märgiste nimekiri), statistikat ja wallet teavet (näiteks laiendatud avalik võti).



Kui klõpsate portfelli parameetritele, siis pöördute tagasi meie portfellikonfiguratsiooni juurde ja avanevad järgmised vahekaardid:




- Üldine** (kus saab portfelli nime muuta) ;



![screen](assets/fr/24.webp)





- Coinjoin** (kus saab kohandada selle wallet jaoks coinjoin'i seadeid) ;



![screen](assets/fr/25.webp)





- Tööriistad** (kus saate kontrollida oma seedphrase, sünkroonida oma portfelli uuesti või kustutada selle).



![screen](assets/fr/26.webp)




## Bitcoinide vastuvõtmine



![video](https://youtu.be/cqv35wBDWMQ)



Et saada bitcoins oma wallet kohta Ginger Wallet:




- vajutage **Vastuvõtmine** ;



![screen](assets/fr/27.webp)





- Sisestage selle allika nimi, millega soovite aadressi seostada. See on märgistus maksete jälgimiseks. Sellel ei ole on-chain mõju; see on lihtsalt teie rakenduses lokaalselt salvestatud jälgitavuse teave;



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

![screen](assets/fr/28.webp)





- klõpsake väikesel noolega vasakul **Loo**, et valida oma aadressiformaat (**SegWit** /**Taproot**) , seejärel klõpsake **Loo**, et generate aadressi ja QR-koodi luua.



![screen](assets/fr/29.webp)



Seda aadressi või QR-koodi kasutab teie saatja bitcoinide saatmiseks.



![screen](assets/fr/30.webp)




## Bitcoinide saatmine




![video](https://youtu.be/2nf5aAimfhg)



Selleks :




- Vajutage nuppu **Saatmine**;
- sisestage saaja aadress, saadetav summa ja silt;
- kontrollige tehingu ülevaadet ja kinnitage saatmine.



![screen](assets/fr/31.webp)




## Kuluta bitcoine



Bitcoin on lihtne osta ja müüa koos Ginger Wallet-ga. Vaid mõne sammuga saate oma bitcoinid kulutada.



### Osta bitcoine



![video](https://youtu.be/lEqTBzm5MEA)



Ginger Wallet kasutajad saavad osta bitcoine.





- Vajutage nuppu **Ostan**. See nupp jääb nähtavaks ka siis, kui wallet on tühi.



![screen](assets/fr/32.webp)





- Enne bitcoini ostu sooritamist valige oma riik või isegi oma riik (mõnes piirkonnas, näiteks Kanadas). Tegelikult, kui klõpsate esimest korda funktsioonil **Ostmine**, peate ka oma piirkonna määrama.



![screen](assets/fr/33.webp)



Ostuprotsessi jätkamiseks vajutage **Jätka**.





- Seejärel sisestage selleks ettenähtud väljale bitcoinide summa, mida soovite osta. Samuti saate valida tehingu valuuta.



![screen](assets/fr/34.webp)



Igal valuutal on minimaalne ja maksimaalne ostulimiit. Näiteks USA dollarites on maksimaalne piirmäär 30 000 dollarit.



Kui olete juba ostu sooritanud, saate vaadata oma tehinguajalugu, klõpsates nupul **Eelmised tellimused**. Kuvatakse nimekiri varasematest tehingutest ja nende staatusest.





- Valige teile sobiv pakkumine.



Siinkohal näete nimekirja kõigist olemasolevatest pakkumistest. Iga pakkumise puhul on teil :




 - tarnija nimi (1) ;
 - eelnevalt sisestatud summale vastav bitcoinide arv, makseviis ja ostutasu (2) ;
 - nuppu **Accept** (3).



![screen](assets/fr/35.webp)



Pakkumises märgitud tasud ei kujuta endast lisakulu. Need on juba lisatud pakkumise kogusummasse.



Ekraani paremas ülemises nurgas, kus on märgitud **Kõik**, saate pakkumisi filtreerida makseviisi järgi. Teie valitud makseviis on vaikimisi määratud, kuid seda saab igal ajal muuta.



![screen](assets/fr/36.webp)



Kui leiate sobiva pakkumise, klõpsake ostu sooritamiseks nupule **Accept**. Seejärel suunatakse teid müüja lehele, kus saate tehingu lõpule viia.



### Bitcoinide müük



Ginger Wallet kasutajad saavad müüa Bitcoin. Nupp **Müüa** on nähtav ainult siis, kui portfellis on vahendeid.





- Klõpsake **Müüa**.



![screen](assets/fr/37.webp)





- Nagu ka **Ostmise** puhul, peate müümise funktsiooni esmakordsel kasutamisel enne bitcoin-müügiga jätkamist valima oma riigi.





- Järgmisena peate sisestama Bitcoins summa, mida soovite müüa. Võite sisestada selle summa BTC-s või fiat-valuutas, näiteks USA dollaris (USD).





- Kui olete seda teinud, näete saadaval olevate pakkumiste nimekirja. Valige teile sobiv müügipakkumine ja jätkamiseks klõpsake **Accept**.





- Nüüd peate tehingu lõpule viima:
 - Kui olete pakkumise heaks kiitnud, suunatakse teid ümber tarnija lehele;
 - Järgige tarnija lehel olevaid juhiseid ;
 - Mingil hetkel saadetakse sulle saaja aadress ja täpne summa, mille saadad;
 - Seejärel naaske Ginger Wallet juurde, et protsessi jätkata;
 - Kui olete tagasi Ginger Wallet-s, ilmub dialoogiboks, mis võimaldab teil jätkata, vajutades **Send**.



See avab ekraani **Saatmine**, kus on eelnevalt täidetud saaja aadress ja summa. Võite kasutada ka avakuval olevat nuppu **Saatmine**. Kuigi saate tehingu saata ka käsitsi, soovitame optimaalse protsessi tagamiseks täita selle dialoogiboksi kaudu.



## Ginger Wallet-l coinjoin'i tegemine



![Vidéo](https://youtu.be/AJe67RDfB1A)



Kaitske oma bitcoinide konfidentsiaalsust **Coinjoiniga**, mis on integreeritud otse Ginger Wallet-sse. wallet kasutab **WabiSabi**, Chaumian coinjoin-protokolli, mis on loodud lihtsamaks ja tõhusamaks coinjoinimiseks.



Sina ise valid, milline coinjoin strateegia (automaatne või manuaalne) sulle kõige paremini sobib.



Ginger Coinjoin on kasutusvalmis kohe, kui olete selle alla laadinud (täiendavaid samme ei ole vaja teha). Ginger Coinjoin töötab automaatselt taustal, et kaitsta teie privaatsust iga tehingu puhul. Praktikas ilmub Coinjoin-mängija alati, kui teil on anonüümseks muudetav saldo.



Mis puutub manuaalsesse coinjoin'i käivitamisse, siis see on ühe klõpsuga tehtav toiming. Alustage vooru ja oodake, kuni coinjoin-tehing luuakse ja kinnitatakse. Kasutajaliideses näete anonüümsuse skoori.



Mitmeid segusid võib teha, kuni saavutatakse soovitud anonüümsuse tase. Te võite ka teatud osad segust välja jätta.



Vaikimisi kasutab Ginger oma koordinaatorit koos kõigi eelkonfigureeritud parameetrite ja garanteeritud tasudega. Rohkem kui 0,03 BTC väärtusega müntide liitmisel tuleb lisaks mining tasule maksta 0,3% koordinaatoritasu. 0,03 BTC või väiksema väärtusega sisseminekud, samuti remixid, on koordinaatoritasudest vabastatud, isegi pärast ühte tehingut. Seega võimaldab Coinjoini vahenditega tehtud makse nii saatjal kui ka saajal oma münte remixida ilma koordinaatoritasudeta.



Ginger eelistab väiksematele ja kiirematele voorudele rohkemate osalejatega ühisvõistlusi. Suuremad coinjoins pakuvad suuremat anonüümsust, väiksemaid kulusid ja suuremat tõhusust plokkide ruumi kasutamisel.




## Ohutus ja parimad tavad



Soov detsentraliseerida ja eraelu puutumatuse säilitamine nõuab mitme parima tava vastuvõtmist:




- Hoidke oma seedphrase alati turvalises kohas, mis ei ole võrgus;
- Kui kaotate oma arvuti või kahtlustate volitamata juurdepääsu, looge kohe uus wallet. Viige oma vahendid sellesse uude portfelli ja kustutage vana portfell;
- Kasutage iga vastuvõtu jaoks erinevat aadressi, et vältida aadresside korduvat kasutamist;
- Laadige oma portfoolio rakendused alati alla ainult ametlikust GitHubi kontost või ametlikust veebisaidist.



Nüüd olete tuttav Ginger Wallet rakenduse kasutamisega bitcoinide saatmiseks, vastuvõtmiseks ja kulutamiseks.



Kui leidsid selle õpetuse kasulikuks, palun jäta mulle allpool roheline pöial. Palun jagage seda artiklit julgelt oma sotsiaalmeedia platvormide kaudu. Tänan teid väga!



Samuti soovitan teil tutvuda selle õpetusega, kuidas kasutada Liana arvutirakendust bitcoinide saatmiseks ja vastuvõtmiseks ning automatiseeritud kinnisvaraplaani rakendamiseks.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04