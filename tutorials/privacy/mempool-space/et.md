---
name: Mempool
description: Tutvuge kogu Bitcoin ökosüsteemiga.
---

![cover](assets/cover.webp)



Bitcoin protokoll on pseudonüümne, detsentraliseeritud võrk, mis on avatud konsultatsioonidele. Liikmetel (sõlmedel), st arvutitel, millel on Bitcoin tarkvara instants, on piiramatu juurdepääs kõigile Bitcoin-s avaldatud andmetele. Bitcoin algusaastatel ei olnud protokoll siiski nii laialdaselt kättesaadav kui praegu.


Bitcoin algusaegadel oli vaja käivitada Bitcoin sõlme, et pääseda ligi asjakohastele vahenditele (bitcoin-cli), et küsitleda võrku käsurealt.



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Seetõttu on käivitatud projekte Bitcoin kogukonna laiendamiseks, et muuta see kättesaadavamaks kõigile, kellel ei ole sõlme ja/või kellel puuduvad vajalikud tehnilised oskused.



Selles õpetuses vaatleme **Mempool.space** projekti, selle funktsioone ja selle mõju Bitcoin ökosüsteemile.



## Mis on Mempool.space?



**Mempool.space** on avatud lähtekoodiga explorer, mis pakub kasulikku teavet tehingute, tehingutasude, plokkide ja kaevurite kohta erinevates Bitcoin protokolli võrkudes. See 2020. aastal käivitatud teenus parandab oluliselt kasutajakogemust esindusliku graafika, sujuvate animatsioonide ja lihtsate kasutajaliideste abil.



Projekti mõistmiseks on Mempool (mälupool) virtuaalne ruum, kuhu salvestatakse kõik Bitcoin võrgus kinnitust ootavad tehingud. Mempool on nagu "ooteruum", kus Bitcoin tehingud ootavad kinnitamist. Igal võrgu arvutil (sõlmel) on oma ooteruum, mis selgitab, miks kõik tehingud ei ole kõigile korraga nähtavad.



Platvormi peamine mõju Bitcoin ökosüsteemis seisneb selles, et see võimaldab teil pääseda ligi enamiku Bitcoin-s olevate sõlmede mälupiirkondades olevale mitmekesisele teabele, ilma et teil oleks vaja käivitada üks neist. Mempool.space on hoidla Bitcoin protokollivõrkude vaatamiseks ja otsimiseks.



Üha laialdasem kasutamine ökosüsteemis ja asjaolu, et Mempool.space on avatud lähtekoodiga, on võimaldanud seda integreerida üha enamasse personaalsesse majutussüsteemi. Nüüd on teil võimalik omada Mempool.space'i oma instantsi otse oma isiklikus sõlmes. Vaadake allpool meie õpetust Mempool.space'i konfigureerimise kohta oma Umbrel-sõlmes.



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Mempool.space'i põhitõed



Nagu eespool mainitud, on [Mempool.space](https://Mempool.space) Bitcoin protokolli uurija, mis võimaldab teil jälgida oma tehinguid ja nende levikut valitud Bitcoin võrgus reaalajas graafilisest Interface-st.



Mempool.space toetab paljusid Bitcoin protokolliga võrke.


Menüüribal leiate järgmised võrgud:




- **Mainnet**: Peamine Bitcoin võrk, kus toimuvad tegelikud Bitcoin tehingud.
- **Signet**: Testvõrk, mis kasutab plokkide valideerimiseks digitaalallkirju, ilma et see nõuaks põhivõrgu poolt nõutavaid ressursse.
- **Testnet 3**: Bitcoin protokolli riskivaba katse- ja arendusvõrk.
- **Testnet 4**: Testnet 3 uus versioon toob suurema stabiilsuse ja uued konsensusreeglid testkeskkonda.



![reseaux](assets/fr/01.webp)



Green avalehel vasakul näete võimalikke tulevasi plokke (tehingute gruppe), mis on valmis valideerimiseks ja integreerimiseks (kaevandamiseks) Bitcoin võrku. Keskmiselt kaevandatakse üks plokk iga kümne minuti tagant: hoidke see teave alles, sest see tuleb hiljem meie arengus kasuks.


Lilla, paremal pool, leiad viimased plokid kaevandatud Bitcoin, kus number viimase ploki kaevandatud esindab praegune kõrgus võrgu.



![blocs](assets/fr/02.webp)



Rubriik **Tehingutasud** on tehingutasude kalkulaator. Mida suuremad on teie tehingule määratud tasud, seda tõenäolisem on, et teie tehing lisatakse järgmisesse kaevandamisvalmis plokki.


Tehingutasu on kulu, mida Miner võtab teilt, et sisestada teie tehing Mining kandidaatblokki. See on määratletud suhtarvuga sat/vB (Satoshi/Virtuaalsed baidid), mis näitab, kui palju satosid te maksate selle ruumi eest, mida teie tehing kandidaadiblokis hõivab.



⚠️ TÄHELEPANU: Mempool küllastumise korral seavad kaevandajad prioriteediks tehingud, mis pakuvad parimat Satoshi/vByte suhet. Mida raskem (suurem) on teie tehing, seda rohkem satoshisid on vaja kiiresti lisada.



![fees-visualizer](assets/fr/03.webp)



**Mempool Goggles** sektsioon võimaldab teil visualiseerida tehingu poolt hõivatud ruumi.



![mempool](assets/fr/04.webp)



Plokki kaevandatakse umbes iga kümne minuti tagant, kuna kaevandajad peavad andma Proof of Work, et lisada oma plokikandidaat kaevandatud plokkide ahelasse. See raskusaste muutub iga **2016 ploki** järel, mis vastab umbes **2 nädalale**. Selle raskusastme arengut saate näha siin.



![difficulty](assets/fr/05.webp)



Uue ploki lisamine põhiahelale annab valideeritud ploki Miner-le õiguse saada tasu, mis koosneb fikseeritud osast (mis poolitatakse iga 210 000 ploki** järel, mis vastab umbes 4 aasta** jooksul poolitamisele) ja tehingutasudest.



![halving](assets/fr/06.webp)



## Juurdepääs oma tehingu üksikasjadele



Mempool.space'i otsinguribale saate sisestada oma Bitcoin Address või transaction ID, et saada rohkem teavet oma ajaloo kohta.



![search](assets/fr/07.webp)



Tehingu üksikasjade lehel leiate üldist teavet oma tehingu kohta:




- **Staatus**: Kinnitatud, kui see on lisatud plokki, kinnitamata, kui see ootab Mempool-s.
- **Tehingutasud**.
- **Eeldatav saabumisaeg (ETA)**: Ligikaudne aeg, mis kulub teie tehingu blokki lisamiseks. See arvutatakse vastavalt suhtarvule, mis moodustab selle tehinguga seotud tasud.



![general-txinfo](assets/fr/08.webp)



Jaotises **Vool** kuvatakse teie tehingukomponentide graafik.



Sisendid (eelmine UTXO), mida kasutatakse teie tehinguks, ja väljundid, mis annavad saajatele õiguse kasutada bitcoin'e igast väljundist, esitades nende kulutamiseks vajaliku allkirja.



![flow](assets/fr/09.webp)



Lisateavet kasutatud aadresside kohta leiate jaotisest **Sisendid ja väljundid**.



![address](assets/fr/10.webp)



Avastage erinevad Bitcoin tehinguskeemid, et suurendada oma konfidentsiaalsust.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Kiirenda oma tehinguid



Bitcoin ökosüsteemis on kaevurite poolt tehingu valideerimise aspekt lahutamatult seotud tehinguga seotud tehingutasudega. Kaevandajad seavad prioriteediks kõrgema tasude suhtega (satoshis/vBytes) tehingud, mis võib mõjutada teie tehingu kehtivust, kui te ei maksa kaevandajate poolt aktsepteeritud mõistlikke tasusid. Teie tehing jääks Mempool-sse ootama plokki, mis aktsepteerib selle tasude suhet.



Õnneks on Bitcoin võrgus olemas kaks meetodit, mis kiirendavad teie tehingu kinnitamist.





- **RBF** - asendamine tasu alusel: Meetod, mis võimaldab teil kulutada samu kirjeid, mis madala tasuga tehing, kuid seekord suurendades tehingutasu, et kiirendada valideerimist. Teie uus tehing valideeritakse kiiremini ja lisatakse blokki, tühistades madala tasuga tehingu.



Seda mehhanismi aktsepteerivate portfellide puhul saate teostada tasu asendamise toimingut. Vt näiteks meie artiklit Blue Wallet portfelli kohta.



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90



- **CPFP** - Child pay for parent: RBF-st inspireeritud lähenemine, kuid vastuvõtja poolel. Kui tehing, milles te olete vastuvõtja, blokeeritakse Mempool-s, on teil võimalus kulutada selle tehingu väljundid (UTXO), hoolimata sellest, et seda ei ole veel kinnitatud, eraldades sellele uuele tehingule rohkem tasusid, nii et keskmised tasud - tehingu, milles te olete vastuvõtja, ja algatatud tehingu - julgustavad kaevandajaid lisama mõlemad tehingud plokki.



⚠️ Esimene tehing peab sisalduma plokis, et võimaldada teise tehingu kinnitamist.



Kui kõik need terminid tunduvad liiga tehnilised, siis soovitan teil [tutvuda meie sõnastikuga](https://planb.network/resources/glossary), mis sisaldab kõigi Bitcoin ja selle ökosüsteemiga seotud tehniliste terminite määratlusi.



Lisaks nendele meetoditele võimaldab Mempool.space tänu oma ühendustele enam kui 80% Bitcoin võrgus olevate kaevuritega ka kiirendada mis tahes oma **kinnitamata** tehinguid, isegi neid, mis ei aktiveeri RBF, makstes tasu Exchange kaevuritele, et nad lisaksid teie odava tehingu järgmisesse kaevandamisvalmis plokki.



Tehingu üksikasjade lehel klõpsake nupule **Kiirenda**, seejärel jätkake oma vastaspoolele kaevuritele maksmist.



![accelerate-section](assets/fr/11.webp)


## Alaealised



Miner viitab isikule, kes haldab kaevandit, st arvutit, mis osaleb Mining protsessis, mis koosneb Proof-of-Work osalemisest. Miner rühmitab oma Mempool pooleliolevad tehingud, et moodustada kandidaatblokki. Seejärel otsib ta selle ploki päise jaoks kehtivat Hash, mis on väiksem või võrdne sihtmärgiga, muutes erinevaid nonce'e. Kui ta leiab kehtiva Hash, edastab ta oma ploki Bitcoin võrku ja tassib sellega seotud rahalise tasu, mis koosneb plokisubsiidiumist (uute bitcoinide loomine ex niilo) ja tehingutasust.



https://planb.network/courses/ce272232-0d97-4482-884a-0f77a2ebc036

❗Minerid on nagu "valideerijad", kes kontrollivad ja grupeerivad tehinguid plokkidesse. Uue ploki lisamiseks Bitcoin võrku peavad nad lahendama keerulise matemaatilise mõistatuse (Proof-of-Work). Esimene Miner, kes mõistatuse lahendab, võidab Bitcoin tasu (plokkide toetus + tasud plokki lisatud tehingute eest).



Selle Proof of Work raskust jälgitakse, mis võimaldab visualiseerida kaevurite jaoks vajaliku arvutusvõimsuse arengut. Leiad allpool olevatest jaotistest :





- Hinnanguline koguhüvitis, mida kaevurite poolt viimase raskusastme kohandamise ajal saadi, ning hinnanguline hinnang järgmise Halving plokkide andmise kohta, mis toimub iga 210 000 ploki (umbes 04 aasta) järel.



![rewards](assets/fr/12.webp)



Seda raskusastet kohandatakse iga 2016 ploki (umbes kaks nädalat) järel. See on pöördvõrdeline keskmise ajaga, mis kaevuritel kulub Miner iga 2016. ploki puhul.


Kui kaevurite keskmine ajakulu on alla 10 minuti, suureneb raskusaste, mis tõestab, et kaevurite jaoks oli Miner plokkide valideerimine lihtsam. Seevastu kui keskmine ajakulu on suurem kui 10 minutit, siis raskusaste väheneb.



![mining-pool](assets/fr/13.webp)





- Kaevurite rühmad: Proof of Work leidmiseks Bitcoin-l, mida me nimetame **pooliks**, teevad kaevurite rühmad koostööd, pidades silmas sellega seotud raskusi. Kui rühm kaevandab ploki, jagatakse saadud tasu vastavalt iga Miner osalise lahenduse otsingu edukuse protsendile, st panus arvutusvõimsuses Proof-of-Work otsimisel, või vastavalt koostöös kokkulepitud tasustamismeetodile.





![mining](assets/fr/14.webp)



## Lightning Network infrastruktuur



Mempool ei anna teavet mitte ainult Bitcoin võrguinfrastruktuuri (põhiketi) kohta. See sisaldab ka visualiseerimis- ja uurimisvahendeid Bitcoin Lightning overlay jaoks.



Jaotises **Lightning** saate vaadata kõiki olemasolevaid Lightning-sõlmede vahelisi ühendusi.



![network-stats](assets/fr/15.webp)



Käesolev Interface annab teavet :





- Lightning Network statistika.



![distribution](assets/fr/16.webp)




⚠️ **OLULINE**: Maksekanali mahutavus määrab maksimaalse summa, mida sõlmpunkt saab Lightning-tehingu käigus teisele sõlmpunktile saata.





- Välgussõlmed jaotatakse vastavalt internetiteenuse pakkujale (hostinguteenus) ja valikuliselt vastavalt maksekanali mahule.



![distribution](assets/fr/17.webp)





- Lightning Network üldise võimsuse ajalugu.


Samuti leiate nende sõlmede pingerea vastavalt nende maksekanalite võimsusele.



![ranking](assets/fr/18.webp)



## Rohkem graafikat



Mempool.space on ideaalne platvorm Bitcoin-protokolliga suhtlemise nautimiseks. Graafikud ei paku mitte ainult visuaalseid andmeid, mis aitavad teil otsustada, millal tehinguid teha, vaid ka täpseid parameetreid, mis võimaldavad teil reaalajas visualiseerida Bitcoin võrgu ja sellega seotud välkkiirte infrastruktuuride tugevust ja tervist.



Jaotises **Graafika** saate vaadata olulisi andmeid Bitcoin võrgu kohta:




- Mempool suuruse areng: See võib näidata, kuidas Mempool suurus kõigub, mis võib viidata võrgu suure või vähese aktiivsuse perioodidele.



![graphs](assets/fr/19.webp)






- Tehingute ja tehingutasude areng valitud võrgus: Saate jälgida tehingute muutusi sekundis, et ennetada ülekoormuse või vähese aktiivsuse perioode ja optimeerida oma tehingutasusid. See graafik annab teile ülevaate võrgu suutlikkusest tehingute mahuga toime tulla.



![graphs](assets/fr/20.webp)



Nüüd, kui olete jõudnud Mempool.space'is oma reisi lõppu, saate ise uurijaks ja saate jälgida oma tehinguid reaalajas. Allpool leiate meie artikli Bitcoin **Public Pool** explorerist.



https://planb.network/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1