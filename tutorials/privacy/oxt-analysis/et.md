---
name: OXT - Chain Analysis
description: Omanda Bitcoinil põhineva ahelanalüüsi algtõed
---
![kaas](assets/cover.webp)

***HOIATUS:** Pärast Samourai Wallet'i asutajate vahistamist ja nende serverite konfiskeerimist 24. aprillil on **veebisait OXT.me hetkel kättesaamatu**. Siiski on võimalik, et see tööriist võidakse järgnevate nädalate jooksul taaskäivitada. Vahepeal saate sellest õpetusest kasu, et mõista Bitcoinil põhineva ahelanalüüsi aluseid. Siin esitatud kõik heuristikad ja mustrid on endiselt rakendatavad Bitcoin tehingutele. Kuigi need tööriistad ei ole nii optimeeritud kui OXT, võite teoreetiliste kontseptsioonide praktikasse rakendamiseks ajutiselt kasutada [Mempool.space](https://mempool.space/) või [Bitcoin Explorer](https://bitcoinexplorer.org/).*

_Me jälgime selle juhtumi arenguid ning seotud tööriistade arenguid tähelepanelikult. Olge kindlad, et me uuendame seda õpetust, kui uus informatsioon saab kättesaadavaks._

_Seda õpetust pakutakse ainult hariduslikel ja informatiivsetel eesmärkidel. Me ei toeta ega julgusta nende tööriistade kasutamist kuritegelikel eesmärkidel. Iga kasutaja vastutab oma jurisdiktsiooni seadustega kooskõlas olemise eest._

---

Selles artiklis õpid tundma olulisi teoreetilisi aluseid, mis on vajalikud Bitcoinil põhineva põhilise ahelanalüüsi alustamiseks ja veelgi olulisem, mõistmaks, kuidas sind jälgivad osapooled toimivad. Kuigi see artikkel ei ole praktiline õpetus OXT tööriista kohta (teema, mida käsitleme tulevases õpetuses), koondab see endas kasutamiseks vajalikku olulist teadmistepagasit. Iga esitatud mudeli, mõõdiku ja indikaatori kohta on antud link näidistehingule OXT-s, mis võimaldab sul paremini mõista selle kasutust ja harjutada lugemise kõrvalt.

## Sissejuhatus
Üks raha funktsioonidest on lahendada kahekordse soovide kokkulangemise probleem. Barteril põhinevas süsteemis nõuab vahetuse lõpuleviimine mitte ainult isiku leidmist, kes pakub minu vajadust rahuldavat kaupa, vaid ka neile vastukaaluks samaväärset väärtust omava kauba pakkumist, mis rahuldab nende enda vajadust. Selle tasakaalu leidmine osutub keerukaks. Seetõttu pöördume raha poole, mis võimaldab meil väärtust liigutada nii ruumis kui ka ajas.

Selleks, et raha saaks seda probleemi lahendada, on oluline, et kauba või teenuse pakkuv pool oleks veendunud oma võimes seda summat hiljem kulutada. Seega, iga ratsionaalne isik, kes on valmis vastu võtma rahatüki, olgu see digitaalne või füüsiline, veendub, et see vastab kahele põhilisele kriteeriumile:
- Münt peab olema terve ja autentne;
- ja seda ei tohi topeltkulutada.

Kui kasutame füüsilist raha, on esimene omadus kõige keerulisem tõestada. Ajaloo erinevatel perioodidel on metallraha terviklikkust sageli mõjutanud praktikad nagu kärpimine või puurimine. Näiteks Vana-Roomas oli kodanikel tavaline kuldraha servadest natuke kallismetalli kraapida, hoides neid siiski tulevaste tehingute jaoks. See on märkimisväärne põhjus, miks hiljem hakati müntide servadele sooni lööma. Autentsus on samuti keeruline omadus füüsilisel rahal kontrollida. Tänapäeval on võltsimisvastased tehnikad üha keerukamad, sundides kaupmehi investeerima kallitesse kontrollisüsteemidesse.

Teisest küljest, nende olemuse tõttu, ei ole topeltkulutamine füüsiliste valuutade puhul probleem. Kui annan sulle 10-eurose, lahkub see pöördumatult minu valdusest, et siseneda sinu omasse, välistades seeläbi mis tahes võimaluse rahaliste ühikute mitmekordseks kulutamiseks.
Digitaalvaluuta puhul on väljakutse erinev. Mündi autentsuse ja terviklikkuse tagamine on sageli lihtsam, kuid topeltkulutamise puudumise tagamine on keerulisem. Iga digitaalne hüve on sisuliselt informatsioon. Erinevalt füüsilistest kaupadest ei jagune informatsioon vahetuste käigus, vaid paljuneb. Näiteks, kui ma saadan sulle dokumendi e-posti teel, siis see duplitseeritakse. Sinu poolel ei saa sa kindlalt kontrollida, kas ma olen originaaldokumendi kustutanud.

Digitaalse hüve duplikatsiooni vältimise ainus viis on olla teadlik kõigist süsteemis toimuvatest vahetustest. Sel viisil saab teada, kes mida omab, ja uuendada kõigi kasutajate kontosid tehtud tehingute põhjal. Seda tehakse näiteks kirjaliku raha puhul. Kui maksad kaupmehele 10 eurot krediitkaardiga, märgib pank selle vahetuse üles ja uuendab pearaamatut.

Bitcoinis toimub topeltkulutamise vältimine samal viisil. Püütakse kinnitada tehingu puudumist, mis on juba küsimuses olevad mündid ära kulutanud. Kui neid pole kunagi kasutatud, siis võime olla kindlad, et topeltkulutamist ei toimu. See on kuulus Satoshi Nakamoto fraas Valges Raamatus: "*Ainsaks viisiks tehingu puudumise kinnitamiseks on olla teadlik kõigist tehingutest.*"

Erinevalt pangandusmudelist ei soovi me Bitcoinis usaldada keskset üksust. Seetõttu peavad kõik kasutajad saama kinnitada topeltkulutamise puudumist, ilma et peaksid kolmandale osapoolele toetuma. Seega peavad kõik olema teadlikud kõigist Bitcoin tehingutest.

Just see informatsiooni avalik levitamine komplitseerib privaatsuse kaitset Bitcoinis. Traditsioonilises pangandussüsteemis on teoorias ainult finantsasutus teadlik tehtud tehingutest. Kuid Bitcoinis on kõik kasutajad teadlikud kõigist tehingutest, läbi oma vastavate sõlmede.

Selle levitamise piirangu tõttu erineb Bitcoini privaatsusmudel pangandussüsteemi omast. Viimases seostatakse tehingud kasutaja identiteediga, kuid informatsiooni vool on katkestatud usaldusväärse kolmanda osapoole ja avalikkuse vahel. Teisisõnu, sinu pankur teab, et ostad iga hommik kohalikust pagaripoest baguette, kuid sinu naaber ei ole kõigist nendest tehingutest teadlik. Bitcoinis, kuna informatsiooni voolu tehingute ja avaliku domeeni vahel ei saa katkestada, toetub privaatsusmudel kasutaja identiteedi eraldamisele tehingutest endist.
![analüüs](assets/en/1.webp)
*Diagramm, mis on inspireeritud Satoshi Nakamoto omast Valges Raamatus: Bitcoin: A Peer-to-Peer Electronic Cash System, jaotis 10 "Privaatsus".*
Kuna Bitcoin tehingud tehakse avalikuks, muutub võimalikuks luua nende vahel seoseid, et järeldada informatsiooni osapoolte kohta. See tegevus isegi kujutab endast iseenesest eriala, mida tavaliselt nimetatakse "ahela analüüsiks". Selles artiklis kutsun teid uurima ahela analüüsi aluseid, et mõista, kuidas teie bitcoine jälgitakse.

Enamik ahela analüüsiga tegelevaid ettevõtteid tegutseb mustades kastides ja ei avalikusta oma metoodikaid. Seetõttu on selle praktika kohta raske teavet saada. Selle artikli kirjutamisel toetusin peamiselt mõnele saadaolevale avatud ressursile:
- Suurem osa minu artiklist on väljavõte neljast artiklist nimega: [Understanding Bitcoin Privacy with OXT](https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923), mille tootis Samourai Wallet 2021. aastal;
- Kasutasin ka erinevaid [OXT Research](https://medium.com/oxt-research) aruandeid, samuti nende tasuta ahela analüüsi tööriista;
- Üldisemalt pärineb minu teadmised erinevatest säutsudest ja sisust, mida on jaganud [@LaurentMT](https://twitter.com/LaurentMT) ja [@ErgoBTC](https://twitter.com/ErgoBTC);- Samuti inspireeris mind [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji), kus osalesin koos [@louneskmt](https://twitter.com/louneskmt), [@TheoPantamis](https://twitter.com/TheoPantamis), [@Sosthene___](https://twitter.com/Sosthene___), ja [@LaurentMT](https://twitter.com/LaurentMT).

Sooviksin tänada nende autorite, arendajate ja tootjate eest. Ilma nende erineva sisu ja tarkvarata ei oleks see artikkel olemas. Tänan ka ülevaatajaid, kes seda teksti hoolikalt parandasid ja jagasid oma ekspertnõuandeid:
- [Gilles Cadignan](https://twitter.com/gillesCadignan);
- [Ludovic Lars](https://twitter.com/lugaxker) ([https://viresinnumeris.fr/](https://viresinnumeris.fr/)).

*Teie teadmiseks, olen artikli lõppu lisanud tehnilise minisõnastiku, et defineerida teatud termineid. Kui näete sõna, mida te ei mõista ja sellel on tärn, siis selle definitsioon on lehekülje lõpus.*

## Mis on ahela analüüs?
Ahela analüüs hõlmab kõiki meetodeid Bitcoin'i voo jälgimiseks plokiahelas. Üldiselt tugineb ahela analüüs eelnevate tehingute proovide omaduste jälgimisele. Seejärel hõlmab see nende samade omaduste tuvastamist tehingus, mida soovitakse analüüsida, ja tõenäoliste tõlgenduste järeldamist. See probleemilahendusmeetod, mis põhineb praktilisel lähenemisel piisavalt hea lahenduse leidmiseks, on see, mida nimetatakse heuristikaks.

Lihtsustatult öeldes tehakse ahela analüüs kahe peamise sammuna:
1. Tuntud omaduste tuvastamine;
2. Hüpoteeside tuletamine.

Üks ahela analüüsi eesmärkidest on grupeerida erinevad tegevused Bitcoin'is, et määrata kindlaks kasutaja ainulaadsus, kes neid teostas. Seejärel on võimalik proovida seostada see tegevuste kogum reaalse identiteediga.

Mäletage minu sissejuhatust. Selgitasin, miks Bitcoin'i privaatsusmudel algselt tugines kasutaja identiteedi eraldamisele nende tehingutest. Seega võiks arvata, et ahela analüüs on tarbetu, kuna isegi kui õnnestub grupeerida ahelategevusi, ei saa neid seostada reaalse identiteediga. Teoreetiliselt on see väide täpne. Krüptograafilisi võtmepaare kasutatakse UTXO-de tingimuste kehtestamiseks. Olemuselt ei avalda need võtmepaarid mingit teavet oma hoidjate identiteedi kohta. Seega, isegi kui õnnestub grupeerida tegevusi, mis on seotud erinevate võtmepaaridega, ei ütle see meile midagi nende tegevuste taga oleva üksuse kohta.
Siiski on praktiline reaalsus palju keerulisem. On mitmeid käitumisi, mis seovad reaalse identiteedi ahelas toimuva tegevusega. Analüüsis nimetatakse seda sisenemispunktiks ja neid on palju. Kõige tavalisem, muidugi, on KYC (Know Your Customer). Kui võtate oma bitcoine reguleeritud platvormilt välja ühele oma isiklikule vastuvõtu aadressile, siis mõned inimesed suudavad teie identiteedi selle aadressiga seostada. Laiemalt võttes võib sisenemispunkt olla igasugune suhtlus teie reaalse elu ja Bitcoin tehingu vahel. Näiteks, kui avaldate oma vastuvõtu aadressi oma sotsiaalvõrgustikes, võib see olla analüüsi jaoks sisenemispunkt. Kui teete oma pagarile makse bitcoinides, võivad nad seostada teie näo (mis on osa teie identiteedist) Bitcoin aadressiga. Need sisenemispunktid on Bitcoini kasutamisel peaaegu vältimatud. Kuigi võib püüda nende ulatust piirata, jäävad need siiski olemasolevaks. Seetõttu on oluline ühendada meetodid, mille eesmärk on teie privaatsuse säilitamine. Kuigi teie reaalse identiteedi ja tehingute vahelise aktsepteeritava eraldatuse säilitamine on kiiduväärt lähenemine, jääb see siiski ebapiisavaks. Tõepoolest, kui kõik teie ahelas toimuvad tegevused saab kokku grupeerida, siis isegi väikseim sisenemispunkt võib kompromiteerida selle ühe privaatsuse kihi, mille olite loonud.

Seetõttu on vajalik tegeleda ka ahela analüüsiga meie Bitcoini kasutamisel. Tehes seda, saame minimeerida oma tegevuste koondumist ja piirata sisenemispunkti mõju meie privaatsusele. Täpsemalt, ahela analüüsi vastu võitlemiseks, mis parem viis kui tutvuda ahela analüüsis kasutatavate meetoditega? Kui soovite teada, kuidas oma privaatsust Bitcoinis parandada, peate mõistma neid meetodeid. See võimaldab teil paremini mõista tehnikaid nagu [Coinjoin](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef) või [Payjoin](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f) ning vähendada vigu, mida võite teha.

Sellega saame tõmmata analoogia krüptograafia ja krüptoanalüüsi vahel. Hea krüptograaf on eelkõige hea krüptoanalüütik. Uue krüpteerimisalgoritmi väljamõtlemiseks peab teadma, milliste rünnakutega see silmitsi seisab, ja uurima ka, miks eelmised algoritmid murdusid. Sama põhimõte kehtib Bitcoini privaatsuse kohta. Ahela analüüsi meetodite mõistmine on võti selle vastu kaitsmiseks. Seetõttu pakun teile seda artiklit.

On oluline mõista, et ahela analüüs ei ole täppisteadus. See tugineb heuristikale, mis on tuletatud varasematest vaatlustest või loogilistest tõlgendustest. Need reeglid võimaldavad üsna usaldusväärseid tulemusi, kuid mitte kunagi absoluutse täpsusega. Teisisõnu, ahela analüüs hõlmab alati tõenäosusdimensiooni järeldustes. Me võime hinnata rohkem või vähem kindlalt, et kaks aadressi kuuluvad samale üksusele, kuid täielik kindlus jääb alati kättesaamatuks.

Ahela analüüsi kogu eesmärk seisneb just erinevate heuristikate koondamises, et minimeerida vea riski. See on omamoodi tõendite kuhjamine, mis võimaldab meil reaalsusele lähemale jõuda.

Need kuulsad heuristikad saab grupeerida erinevatesse kategooriatesse, mida me koos üksikasjalikult käsitleme:
- Tehingumustrid (või tehingumudelid);
- Tehingu sisemised heuristikad;
- Tehingu välised heuristikad.

On märkimisväärne, et esimesed kaks Bitcoinile omast heuristikat formuleeris Satoshi Nakamoto ise. Ta arutleb neid Valge Raamatu osas 10. Nagu hiljem näeme, on huvitav täheldada, et need kaks heuristikat hoiavad ahela analüüsis tänapäevalgi pretsedenti. Need on:
- ühise sisendi omandi heuristika (CIOH);
- ja aadressi taaskasutus.
Uurime koos täheldatavaid omadusi ja tõlgendusi, mida saab teha analüüsi läbiviimiseks.
## Tehingumustrid (või tehingumudelid)
Tehingumuster on lihtsalt tüüpiline tehingumudel, mida võib leida plokiahelast, mille tõlgendamine on tõenäoliselt teada. Mustrite uurimisel keskendume ühele tehingule, mida analüüsime kõrgel tasemel. Teisisõnu, me vaatame ainult sisendite ja väljundite arvu, jättes tähelepanuta selle spetsiifilisemad detailid või keskkonna. Täheldatud mudelist lähtuvalt suudame tõlgendada tehingu olemust. Seejärel otsime omadusi selle struktuuri kohta ja teeme tõlgenduse.

### Lihtne saatmine (või lihtne makse)
Seda mudelit iseloomustab ühe või mitme UTXO tarbimine sisendina ja kahe UTXO tootmine väljundina.

![analüüs](assets/en/2.webp)

Selle mudeli tõlgendus on, et meil on tegemist saatmise või maksetehinguga. Kasutaja on tarbinud oma UTXOsid sisendina, et rahuldada väljundis makse UTXO ja vahetus UTXO (vahetus, mis tuleb tagasi samale kasutajale). Seega teame, et täheldatud kasutaja tõenäoliselt ei oma enam ühte kahest UTXOst väljundis (makse oma), kuid on endiselt teise UTXO (vahetuse oma) omanik.

Sel hetkel on meil võimatu täpsustada, milline väljund esindab millist UTXOt, kuna see ei ole selle mudeli eesmärk. Saame seda teha toetudes heuristikale, mida uurime järgmises osas. Praeguses etapis on meie eesmärk piiratud ainult küsimuse all oleva tehingu olemuse tuvastamisega, mis on sel juhul lihtne saatmine.

Näiteks siin on Bitcoin tehing, mis järgib lihtsa saatmise mustrit:
### Pühkimine ("sweep" inglise keeles)
Seda mudelit iseloomustab ühe UTXO tarbimine sisendina ja ühe UTXO tootmine väljundina.

![analüüs](assets/en/3.webp)

Selle mudeli tõlgendus on, et meil on tegemist eneseülekandega. Kasutaja on kandnud oma bitcoine endale, teisele aadressile, mida ta omab. Kuna tehingus ei ole vahetust, on väga ebatõenäoline, et tegemist on maksega. Siis teame, et täheldatud kasutaja tõenäoliselt ikka omab seda UTXOt.

Näiteks siin on Bitcoin tehing, mis järgib pühkimise mustrit:
[35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d](https://mempool.space/tx/35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d)

Siiski võib see tüüpi muster samuti paljastada eneseülekande krüptoraha vahetuskontole (krüptoraha vahetusplatvorm). Selleks, et teada saada, kas tegemist on pühkimisega isehoidla rahakotti või väljavõtmisega platvormile, tuleb uurida tuntud aadresse ja tehingu konteksti.

### Konsolideerimine
Seda mudelit iseloomustab mitme UTXO tarbimine sisendina ja ühe UTXO tootmine väljundina.

![analüüs](assets/en/4.webp)
Selle mudeli tõlgendus on, et oleme konsolideerimise juures. See on Bitcoin'i kasutajate seas levinud praktika, mille eesmärk on ühendada mitu UTXO-d eelnevalt võimaliku tehingutasude tõusu ootuses. Seda toimingut tehes ajal, mil tasud on madalad, on võimalik tulevikus tasudelt säästa.
Võime järeldada, et selle tehingu taga olev kasutaja oli tõenäoliselt kõigi sisendis olevate UTXO-de omanik ja on endiselt väljundi UTXO omanik. Seega on see kindlasti iseenesele tehtud ülekanne.

Nagu ka pühkimisel, võib see tüüpiline muster samuti paljastada iseenesele tehtud ülekande börsikontole. Tuntud aadresside ja tehingu konteksti uurimine võimaldab meil teada saada, kas tegemist on konsolideerimisega isehoide rahakotti või väljavõtmisega platvormile.

Näiteks siin on Bitcoin'i tehing, mis järgib konsolideerimise mustrit:
[77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94](https://mempool.space/tx/77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94)
### Partii Kulutamise Mudel
Seda mudelit iseloomustab väheste UTXO-de kasutamine sisendina (tihti ainult üks) ja paljude UTXO-de tootmine väljundina.

![analüüs](assets/en/5.webp)

Selle mudeli tõlgendus on, et oleme partii kulutamise juures. See on tava, mis tõenäoliselt paljastab olulist majandustegevust, näiteks vahetust. Partii kulutamine võimaldab neil üksustel säästa tasudelt, ühendades oma kulutused üheks tehinguks.

Võime järeldada, et UTXO sisend pärineb olulise majandustegevusega ettevõttelt ja UTXO väljundid hajuvad. Mõned kuuluvad ettevõtte klientidele. Teised võivad minna partnerettevõtetele. Lõpuks jõuab kindlasti muutus tagasi väljaandva ettevõtte kätte.

Näiteks siin on Bitcoin'i tehing, mis järgib partii kulutamise mustrit:
[8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43](https://mempool.space/tx/8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43)

### Protokollispetsiifilised Tehingud
Tehingumustrite seas saame samuti tuvastada mudeleid, mis paljastavad konkreetse protokolli kasutamise. Näiteks Whirlpool coinjoins'il on kergesti tuvastatav struktuur, mis võimaldab neid eristada teistest klassikalistest tehingutest.

![analüüs](assets/en/6.webp)

Selle mustri analüüs viitab sellele, et tõenäoliselt oleme koostöö tehingu juures. On ka võimalik täheldada coinjoin'i. Kui see viimane hüpotees osutub täpseks, siis väljundite arv võiks anda meile ligikaudse hinnangu osalejate arvule.

Näiteks siin on Bitcoin'i tehing, mis järgib koostöö tehingu tüüpi coinjoin mustrit:
[00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea](https://mempool.space/tx/00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea)
On palju teisi protokolle, millel on oma spetsiifilised struktuurid. Seega võime eristada näiteks Wabisabi tüüpi tehinguid või Templite tehinguid.
## Sisemiste Tehingute Heuristikud
Sisemine heuristika on tehingu enda sees tuvastatud spetsiifiline omadus, ilma et oleks vaja uurida selle keskkonda, mis võimaldab meil teha järeldusi. Erinevalt mustritest, mis keskenduvad tehingu üldisele struktuurile, põhinevad sisemised heuristikad väljavõetavate andmete kogumil. See hõlmab:
- Erinevate UTXO-de summad nii sissetulevate kui väljaminevate puhul;
- Kõik, mis on seotud skriptidega: vastuvõtvad aadressid, versioonid, lukustusajad...

Üldiselt võimaldab see tüüpi heuristika meil tuvastada muutuse konkreetses tehingus. Tehes seda, saame seejärel jätkata üksuse jälitamist mitme erineva tehingu kaudu.

Tuletan veel kord meelde, et need heuristikad ei ole absoluutselt täpsed. Üksikuna võetuna võimaldavad need meil tuvastada usutavaid stsenaariume. Mitme heuristika kuhjumine aitab vähendada ebakindlust, ilma et see kunagi täielikult kõrvaldataks.

### Sisemised Sarnasused
See heuristika hõlmab sama tehingu sisendite ja väljundite sarnasuste uurimist. Kui sama omadus on täheldatud sisendites ja ainult ühes tehingu väljundis, siis on tõenäoline, et see väljund kujutab endast muutust.

Kõige ilmsem omadus on sama vastuvõtu aadressi taaskasutamine samas tehingus.

![analüüs](assets/en/7.webp)

See heuristika jätab vähe ruumi kahtlustele. Kui nende privaatvõtit ei ole kompromiteeritud, siis sama vastuvõtu aadress paljastab paratamatult ühe kasutaja tegevuse. Järgnev tõlgendus on, et tehingu muutus on väljund, millel on sama aadress kui sisendil. See võimaldab meil jätkata isiku jälitamist sellest muutusest.

Näiteks siin on tehing, kus seda heuristikat tõenäoliselt saab rakendada:
[54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0](https://mempool.space/tx/54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0)

Need sarnasused sisendite ja väljundite vahel ei piirdu ainult aadressi taaskasutamisega. Iga sarnasus skriptide kasutamises võib võimaldada heuristika rakendamist. Näiteks mõnikord võib täheldada sama versioonimist sisendi ja tehingu ühe väljundi vahel.

![analüüs](assets/en/8.webp)
Selles diagrammis näeme, et sisend number 0 avab P2WPKH skripti (SegWit V0, mis algab "bc1q"). Väljund number 0 kasutab sama tüüpi skripti. Siiski, väljund number 1 kasutab P2TR skripti (SegWit V1, mis algab "bc1p"). Selle omaduse tõlgendus on, et tõenäoliselt kuulub sama versioonimisega aadress kui sisendil olev muutuse aadress. Seega kuuluks see endiselt samale kasutajale.
Siin on tehing, kus seda heuristikat tõenäoliselt saab rakendada:
[db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578](https://mempool.space/tx/db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578)
Selles tehingus näeme, et sisendi number 0 ja väljundi number 1 kasutavad P2WPKH skripte (SegWit V0), samal ajal kui väljundi number 0 kasutab erinevat skripti tüüpi, P2PKH (Legacy).
### Ümmarguste Summade Maksed
Teine sisemine heuristika, mis võib aidata meil tuvastada vahetusraha, on ümmarguste summade kasutamine. Üldiselt, kui tegemist on lihtsa maksemustriga (1 sisend ja 2 väljundit), kui üks väljunditest kulutab ümmarguse summa, siis see esindab makset.

![analüüs](assets/en/9.webp)

Elimineerimisprotsessi teel, kui üks väljunditest esindab makset, siis teine esindab vahetusraha. Seega võime tõlgendada, et on tõenäoline, et sisendi kasutaja omab endiselt väljundit, mis on tuvastatud kui vahetusraha.

Tuleb märkida, et seda heuristikat ei saa alati rakendada, kuna enamik makseid tehakse endiselt fiat-valuuta ühikutes. Tõepoolest, kui kaupmees Prantsusmaal aktsepteerib bitcoine, üldiselt ei näita nad stabiilseid hindu satsides. Nad eelistaksid hinda eurodes konverteerida bitcoini makstavaks summaks. Seega ei tohiks tehingu väljundis olla ümmargust numbrit. Siiski võiks analüütik proovida teha seda konversiooni arvestades vahetuskurssi, mis kehtis tehingu võrgus levitamise ajal.

Kui ühel päeval muutub bitcoin meie vahetuste eelistatud arvestusühikuks, võib see heuristika muutuda analüüsiks veelgi kasulikumaks.

Näiteks siin on tehing, kus seda heuristikat tõenäoliselt saab rakendada:
### Suur Kulutus

Kui lihtsa maksemudeli kahe tehingu väljundi vahel märgatakse piisavalt suurt vahet, võib hinnata, et suurem väljund on tõenäoliselt vahetusraha.

![analüüs](assets/en/10.webp)

See suurima väljundi heuristika on tõenäoliselt kõige ebatäpsem kõigist. Kui see tuvastatakse iseseisvalt, on see üsna nõrk. Siiski võib seda omadust kombineerida teiste heuristikatega, et vähendada meie tõlgenduse ebakindlust.

Näiteks, kui me uurime tehingut, mis sisaldab väljundit ümmarguse summaga ja teist väljundit suurema summaga, ümmarguste maksete heuristika ja suurima väljundi heuristika ühine rakendamine võimaldab meil vähendada meie ebakindluse taset.

Näiteks siin on tehing, kus seda heuristikat tõenäoliselt saab rakendada:
[b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf](https://mempool.space/tx/b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf)

## Tehingu Välised Heuristikad
Väliste heuristikate uurimine on sarnasuste, mustrite ja teatud elementide omaduste analüüs, mis ei ole tehingule omane. Teisisõnu, kui varem piirdusime tehingu sisemiste elementidega kasutades sisemisi heuristikaid, siis nüüd laiendame oma analüüsivälja tehingu keskkonnale tänu välistele heuristikatele.

### Aadressi Korduvkasutus
See on üks tuntumaid heuristikaid Bitcoinide seas. Aadressi korduvkasutus võimaldab luua seose erinevate tehingute ja erinevate UTXOde vahel. See on täheldatav, kui Bitcoinide vastuvõtu aadressi kasutatakse mitu korda.

Aadressi korduvkasutuse tõlgendus on, et kõik sellel aadressil lukustatud UTXOd kuuluvad (või on kuulunud) samale entiteedile. See heuristika jätab vähe ruumi ebakindlusele. Kui see on tuvastatud, on järgneva tõlgenduse vastavus reaalsusele suure tõenäosusega.
Nagu sissejuhatuses selgitatud, avastas selle heuristika Satoshi Nakamoto ise. Valges raamatus mainib ta spetsiifiliselt lahendust, et vältida kasutajaid seda tootmast, mis on lihtsalt iga uue tehingu jaoks värske aadressi kasutamine: "*Lisakaitsemeetmena võiks iga tehingu jaoks kasutada uut võtmepaari, et hoida neid seostamata ühise omanikuga.*"
Näiteks siin on aadress, mida kasutatakse mitme tehingu puhul:
[bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0](https://mempool.space/address/bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0)

### Skriptide ja Rahakoti Jälgede Sarnasus
Aadresside korduvkasutusest kaugemale minnes on palju muid heuristikaid, mis võivad seostada tegevusi sama rahakoti või aadresside kogumiga.

Esiteks võib analüütik kasutada skriptide kasutamise sarnasusi. Näiteks teatud vähemusgruppi kuuluvaid skripte nagu multisig on lihtsam märgata kui SegWit V0 skripte. Mida suuremas grupis me peidame, seda raskem on meid märgata. See on märkimisväärne põhjus, miks Coinjoin Whirlpool protokollis kasutavad kõik osalejad täpselt sama tüüpi skripti.

Laiemalt võib analüütik keskenduda ka rahakoti iseloomulikele jälgedele. Need on konkreetse kasutusega seotud protsessid, mida võidakse püüda tuvastada, et neid kasutada jälgimisheuristikana. Teisisõnu, kui täheldatakse sama sisemise omaduse kuhjumist tehingutes, mis on omistatud jälgitavale üksusele, võib püüda tuvastada neid samu omadusi teistel tehingutel.

Näiteks võib tuvastada, et jälgitav kasutaja saadab süstemaatiliselt oma vahetusraha P2TR* aadressidele (bc1p…). Kui see protsess kordub, võib seda kasutada meie analüüsi jätkamise heuristikana. Teisi jälgi võib samuti kasutada, nagu UTXO-de järjekord, vahetusraha paigutus väljundites, RBF (Replace-by-Fee) märkimine või isegi versiooninumber ja lukustusaeg.
Nagu [@LaurentMT](https://twitter.com/LaurentMT) täpsustab [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) saates (prantsuskeelne podcast), kasvab rahakoti jälgede kasulikkus ahela analüüsis aja jooksul märkimisväärselt. Tõepoolest, skriptitüüpide kasvav arv ja nende uute omaduste järkjärguline kasutuselevõtt rahakottide tarkvaras rõhutavad erinevusi. Juhtub isegi, et saab täpselt tuvastada jälgitava üksuse poolt kasutatava tarkvara. Seetõttu on oluline mõista, et rahakoti jälje uurimine on eriti asjakohane hiljutiste tehingute puhul, rohkem kui nende puhul, mis algatati 2010. aastate alguses.
Kokkuvõtteks võib öelda, et jäljeks võib olla mis tahes konkreetne praktika, mida rahakott automaatselt või kasutaja käsitsi teostab, mida saab leida teistelt tehingutelt, et aidata meie analüüsis.

### CIOH
CIOH, "Common Input Ownership Heuristic" ehk "sisendite ühise omandi heuristika" või "kaas-kulutamise heuristika", on heuristika, mis väidab, et kui tehingul on mitu sisendit, siis tõenäoliselt pärinevad need kõik ühelt üksuselt. Seega on nende omand ühine.
CIOH rakendamiseks tuleb esmalt jälgida tehingut, millel on mitu sisendit. See võib olla nii kaks sisendit kui ka kolmkümmend sisendit. Kui see omadus on tuvastatud, kontrollitakse, kas tehing ei sobitu teadaolevasse mustrisse. Näiteks, kui on 5 sisendit umbes sama summaga ja 5 väljundit täpselt sama summaga, teame, et see on Coinjoin Whirlpooli struktuur. Seega ei saa CIOH-d rakendada.
Kuid, kui tehing ei sobitu ühtegi teadaolevasse koostöötehingu mustrisse, siis võib tõlgendada, et kõik sisendid tulevad tõenäoliselt samalt isikult. See võib olla väga kasulik juba teadaoleva klasteri laiendamiseks või jälgimise jätkamiseks.

![analüüs](assets/en/11.webp)

CIOH avastas Satoshi Nakamoto. Ta arutab seda Valge Raamatu osas 10: "*[...] link on paratamatu mitme sisendiga tehingute puhul, mis tingimata paljastavad, et nende sisendid kuulusid samale omanikule. Risk on selles, et kui võtme omanik paljastatakse, võivad lingid paljastada ka teised tehingud, mis kuulusid samale omanikule.*"
Eriti huvitav on märkida, et Satoshi Nakamoto oli juba enne Bitcoini ametlikku käivitamist tuvastanud kaks peamist privaatsusega seotud haavatavust kasutajate jaoks, nimelt CIOH ja aadresside taaskasutus. Selline ettenägelikkus on märkimisväärne, kuna need kaks heuristikat on tänaseni kõige kasulikumad ahela analüüsis.

### Off-chain andmed
Ilmselgelt ei piirdu ahela analüüs ainult on-chain andmetega. Analüüsi täpsustamiseks võib kasutada ka varasemast analüüsist või internetist kättesaadavaid andmeid.

Näiteks, kui täheldatakse, et jälgitavad tehingud edastatakse süstemaatiliselt samast Bitcoin'i noodist ja selle IP-aadress on tuvastatav, võib olla võimalik tuvastada teisi tehinguid samalt isikult.

Analüütikul on võimalus toetuda ka varem avalikustatud analüüsidele või oma varasematele analüüsidele. Võib-olla leiab väljundi, mis viitab juba tuvastatud aadresside klastri. Mõnikord on võimalik toetuda ka väljunditele, mis viitavad vahetusele, kuna nende platvormide aadressid on üldiselt teada.

Samuti on võimalik teha analüüs eliminatsiooni teel. Näiteks, kui tehingu kahe väljundi analüüsimisel on üks neist seotud teadaoleva, kuid jälgitavast isikust erineva aadresside klastri, siis võib tõlgendada, et teine väljund tõenäoliselt esindab vahetusraha.

Ahela analüüs hõlmab ka OSINT-i (Open Source Intelligence) osa, mis on internetiotsingutega veidi üldisem. Seetõttu soovitatakse vältida vastuvõtu aadresside otsest postitamist sotsiaalmeediasse või veebisaidile, olgu see siis pseudonüümi all või mitte.

### Ajalised mudelid
Võib-olla ei tule see kohe meelde, kuid teatud inimkäitumised on ahelas äratuntavad. Kõige kasulikum uurimisel on teie unemuster! Jah, kui te magate, siis tõenäoliselt ei edasta te Bitcoini tehinguid. Kuna te üldiselt magate umbes samadel tundidel, on on-chain analüüsis tavaline kasutada ajalisi analüüse. See hõlmab lihtsalt antud isiku tehingute Bitcoini võrku edastamise aegade salvestamist. Nende ajaliste mustrite analüüsimine võimaldab meil järeldada mitmeid teavetükke.
Eelkõige võib ajaline analüüs mõnikord tuvastada jälgitava isiku olemuse. Kui täheldatakse, et tehinguid edastatakse järjepidevalt 24 tundi ööpäevas, võib see viidata tugevale majandustegevusele. Nende tehingute taga olev isik on tõenäoliselt ettevõte, potentsiaalselt rahvusvaheline ja võib-olla sisemiselt automatiseeritud protseduuridega.
Näiteks märkasin ma seda mustrit mõni nädal tagasi, analüüsides tehingut, milles oli ekslikult eraldatud 19 bitcoini tasudeks. Lihtne ajaline analüüs võimaldas mul hüpoteesida, et tegemist oli automatiseeritud teenusega ja seega tõenäoliselt suure üksusega, nagu näiteks vahetusplatvorm: https://twitter.com/Loic_Pandul/status/1701127409712452072
Tõepoolest, mõni päev hiljem avastati, et vahendid kuulusid PayPalile, Paxose vahetuse kaudu.

Vastupidi, kui näeme, et ajaline muster on pigem jaotunud 16 konkreetse tunni vältel, siis võib hinnata, et tegemist on individuaalse kasutajaga või võib-olla kohaliku ettevõttega, sõltuvalt vahetatud mahtudest.

Vaadeldava üksuse olemusest kaugemale minnes võib ajaline muster anda meile ka kasutaja ligikaudse asukoha. Seega võime korreleerida teisi tehinguid ja kasutada nende ajatempli kui lisaeuristika, mida saab lisada meie analüüsi.

Näiteks aadressil, mida ma varem mainisin ja mida on mitu korda kasutatud, võib täheldada, et tehingud, olgu need siis sissetulevad või väljaminevad, on koondunud 13-tunnise intervalli jooksul.
![analüüs](assets/notext/12.webp)
*Krediit: OXT*

See intervall vastab tõenäoliselt Euroopale, Aafrikale või Lähis-Idale. Seega võib tõlgendada, et nende tehingute taga olev kasutaja elab seal.

Teistsuguses registris on samuti sellist tüüpi ajaline analüüs võimaldanud hüpoteesida, et Satoshi Nakamoto ei tegutsenud Jaapanist, vaid tegelikult Ameerika Ühendriikidest: [https://medium.com/@insearchofsatoshi/the-time-zones-of-satoshi-nakamoto-aa40f035178f](https://medium.com/@insearchofsatoshi/the-time-zones-of-satoshi-nakamoto-aa40f035178f)

### Mahtude Analüüs
Teine väline euristika, mida saab kasutada, on kauplemismahtude analüüs. Põhinedes igale üksusele omistatud tehingute summadele, saab seda teavet kasutada lisaeuristikana ülejäänud analüüsis.
See euristika on ilmselgelt üsna nõrk, kuid see võib aidata vähendada ebakindlust, kui seda lisada teiste euristikate juurde.

## Kuidas end kaitsta ahela analüüsi eest?
Bitcoini kasutajana on teil õigus kaitsta oma privaatsust. See tuleneb teie loomulikest õigustest omada ja enda üle otsustada, mis on omane igale üksikisikule, sõltumata mistahes seadusandlikust piirangust.

See loomulik õigus kaitsta oma privaatsust on samuti muudetud nõudeõiguseks, mis on sätestatud Inimõiguste Ülddeklaratsiooni artiklis 12, öeldes, et "*Kedagi ei tohi meelevaldselt segada tema privaatsuses, perekonnas, kodus või kirjavahetuses, ega rünnata tema au ja mainet. Igaühel on õigus seaduse kaitsele sellise sekkumise või rünnakute vastu.*".

Siiski, ettevõtete, mis on spetsialiseerunud ahela analüüsile, põhitegevus seisneb just teie privaatsfääri tungimises, seeläbi kompromiteerides teie kirjavahetuse konfidentsiaalsust. Kuigi võiks loota, et eelpool mainitud nõudeõiguse kohaselt kaitseksid riigid meie privaatsust jõuliselt, mitte ainult ei jäta nad seda tegemata, vaid nad ka rahastavad oluliselt nende analüüsifirmade tegevust. Samuti oleks asjatu loota toetust sektoriliitude poolt, mis tunduvad olevat valmis tegema kõik järeleandmised seadusandja ees.

Faktiliselt ei eksisteeri see nõudeõigus privaatsusele Bitcoinis. Seega on teie, kasutaja, ülesanne kinnitada oma loomulik õigus ja kaitsta oma kirjavahetuse konfidentsiaalsust. See hõlmab erinevate tehnikate ja kasutuspraktikate omaksvõtmist, mis võimaldavad teil vältida või petta ahela analüüsiks kasutatavaid euristikaid.

### Vältimaks langemist euristikasse
Esiteks, enne radikaalsemate meetodite kaalumist, on soovitatav piirata meie kokkupuudet ahelaanalüüsi kasutatavate heuristikatega nii palju kui võimalik. Nagu varem mainitud, on kaks kõige võimsamat heuristikat aadresside taaskasutamine ja COINJOIN.
Põhiprintsiip oma privaatsuse tagamiseks Bitcoinis seisneb iga saabuva tehingu jaoks uue, puhta aadressi kasutamises oma rahakotis. Aadresside taaskasutamine on tõepoolest peamine oht konfidentsiaalsusele Bitcoinis.
Üksikule kasutajale on iga saabuva makse jaoks uue aadressi genereerimine väga lihtne. Kaasaegsed rahakotid teevad seda automaatselt kohe, kui klõpsate "Vasta". Seega, kui teie tehingute privaatsus on teile vähemalt natuke oluline, siis värske aadresside kasutamine on absoluutne miinimum. Kui vajate internetis staatilist kontaktipunkti, siis aadressi panemise asemel võite kasutada lahendusi [nagu PayNym, mis rakendab BIP47](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093).
Järgmisena, kui soovite võidelda ahelaanalüüsi vastu, vältige UTXO-de ühendamist tehingu sisendis. Minimaalselt, kui peate tõesti ühendama, eelistage UTXO-sid, millel on sama allikas. See soovitus tähendab teie UTXO-de hea haldamise vajadust. Oma bitcoinide ostmisel eelistage suurte summadega ülekandeid, et maksimeerida maksete arvu, mida saate teha ilma ühendamata. Soovitan teil ka oma tarkvaras UTXO-sid märgistada, et tuvastada nende päritolu ja vältida erinevatest allikatest ühendamist.

Laiemalt, kõigi teiste heuristikate puhul, peate neid tundma, et proovida neisse mitte sattuda:
- Ärge kasutage vähemusstsenaariume. Eelistage SegWit V0 või võimalusel SegWit V1;
- Ärge tehke makseid ümmargustes summas. Näiteks, kui peate saatma sõbrale 100k satsi, saatke neile 114,486 satsi. Nad ostavad teile vastutasuks joogi;
- Proovige mitte alati omada vahetusraha, mis on palju suurem kui makse väljund;
- Ärge postitage oma vastuvõtu aadresse sotsiaalmeedias;
- Kasutage oma tehingute edastamiseks oma sõlme Tori all;
- Proovige mitte alati edastada oma Bitcoin tehinguid samal ajal...

### Privaatsustööriistade kasutamine
Samuti võite pöörduda meetodite poole, mis muudavad teie Bitcoini kasutamise ebaselgeks, et vältida või petta ahelaanalüüsi.

Kõige populaarsem tehnika on kindlasti Coinjoin, koostööaline tehingustruktuur, mis mobiliseerib mitu sama summa UTXO-d. Siin on eesmärk katkestada deterministlikud seosed, takistades seeläbi analüüse minevikust olevikku ja olevikust minevikku. Coinjoin võimaldab usutavat eitamist, peites teie mündid suure hulga eristamatute müntide seas. Kui soovite Coinjoini kohta rohkem teada saada, nii tehniliselt kui ka praktiliselt, soovitan teil lugeda neid teisi artikleid ja õpetusi:
- [COINJOIN - SAMOURAI WALLET](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef);
- [COINJOIN - SPARROW WALLET](https://planb.network/tutorials/privacy/on-chain/coinjoin-sparrow-wallet-84def86d-faf5-4589-807a-83be60720c8b);
- [WHIRLPOOL STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375).
![analüüs](assets/en/13.webp)

CoinJoin on suurepärane vahend müntide usutava eitamise loomiseks, kuid see ei ole optimeeritud kõigi kasutajate privaatsusvajaduste jaoks. Eelkõige ei ole CoinJoin kavandatud maksevahendiks. See on väga jäik vahetatavate summade osas, et täiustada usutava eitamise tootmist. Kuna tehingu väljundite summat ei saa vabalt valida, ei saa CoinJoini kasutada bitcoinides maksete tegemiseks.
Näiteks kujutage ette, et tahan oma baguette'i eest maksta bitcoinides, optimeerides samal ajal oma privaatsust. Arvestades võimatust valida CoinJoin'i tulemusena saadava UTXO summat, leian end olukorrast, kus ei suuda oma kulutuse summat pagari määratud hinnaga kohandada. Seetõttu osutub CoinJoin maksetehingute jaoks ebapiisavaks.

Teisi vahendeid on välja mõeldud, et rahuldada privaatsusvajadusi rohkem spetsiifilistes kasutusjuhtumites. Näiteks on meil [PayJoin](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f), omamoodi mini-CoinJoin, mis hõlmab ainult kahte osalejat ja põhineb struktuuril, mis võimaldab makset.

PayJoin'i ainulaadsus seisneb selles, et see suudab toota tehingu, mis näeb välja tavaline, kuigi tegelikult on see mini-CoinJoin kahe kasutaja vahel. Selles struktuuris osaleb tehingu saaja sisendites koos tegeliku saatjaga. Seega sisestab saaja tehingusse endale makse, mis hõlbustab tegelikku makset.

Näiteks, kui ostate oma pagarilt baguette'i 6,000 satsi eest UTXO-st, mis on 10,000 satsi, ja soovite teha PayJoin'i, lisab teie pagar sisendina oma algsele tehingule kuuluva 15,000 satsi suuruse UTXO, mille nad täielikult väljundina tagasi saavad, et petta heuristikat:

![analüüs](assets/en/14.webp)

Tehingutasusid eiratakse, et lihtsustada skeemi mõistmist.

PayJoin'i eesmärgid on kaks. Esiteks, see püüab petta välist vaatlejat, luues läbi COH petukauba. Tõepoolest, kui analüütik vaatleb seda tehingut, arvavad nad, et nad saavad rakendada COH-d ja seega eeldada erinevate sisendite ühist omandit. Tegelikkuses on see eeldus vale, kuna üks sisend kuulub saatjale, samal ajal kui teine on saaja omandis. Seega rikub PayJoin ahela analüüsi, viies analüütiku valele teele.
PayJoin'i teine eesmärk on petta analüütikut tegeliku tehingu summa osas, tänu selle väljundite spetsiifilisele struktuurile. Seega kuulub PayJoin steganograafia valdkonda. See võimaldab tegeliku tehingu summa peita petliku tehingu sisse.

Tõepoolest, kui me vaatame uuesti meie näidet PayJoin'i kasutamisest baguette'i ostmiseks, võib väline vaatleja arvata, et tegemist on 4,000 satsi või 21,000 satsi maksega. Tegelikkuses on baguette'i eest makse 6,000 satsi: 21,000 - 15,000 = 6,000. Tegelik makseväärtus on seega peidetud võltsmakse sisse, mis toimib ahela analüüsi petukaubana.

PayJoin'i ja CoinJoin'i kõrval on palju muid Bitcoin'i tehingustruktuure, mis kas blokeerivad ahela analüüsi või petavad seda. Nende hulgas võiksin mainida [Stonewall](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4) ja [StonewallX2](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b) tehinguid, mis võimaldavad kas teha paindliku mini CoinJoin'i või jäljendada paindlikku mini CoinJoin'i. On ka [Ricochet](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589) tehinguid, mis simuleerivad bitcoinide omandiõiguse muutust, tehes mitmeid võltsülekandeid iseendale.

Kõik need vahendid on saadaval Samourai Wallet'is mobiilis ja Sparrow Wallet'is PC-l. Kui soovite rohkem teada saada nende spetsiifiliste tehingustruktuuride kohta, soovitan teil avastada minu õpetused:
- [PAYJOIN](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f);
- [PAYJOIN - SAMOURAI RAHAKOTT](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab);
- [PAYJOIN - SPARROW RAHAKOTT](https://planb.network/tutorials/privacy/on-chain/payjoin-sparrow-wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62);
- [STONEWALL](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4);
- [STONEWALL X2](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b);
- [RICOCHET](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589).

## Järeldus
Ahela analüüs on praktika, mis hõlmab bitcoini tehingute ahelas jälgimist. Selleks otsivad analüütikud mustreid ja omadusi, et teha rohkem või vähem tõenäolisi hüpoteese ja tõlgendusi.

Nende heuristikate täpsus varieerub: mõned pakuvad suuremat kindlust kui teised, kuid ükski ei saa väita, et on eksimatu. Siiski, mitme kattuva heuristika kogunemine võib vähendada seda kaasasündinud kahtlust, kuigi on võimatu seda täielikult kõrvaldada.
Neid meetodeid saab liigitada kolme eristuvasse põhikategooriasse:
- Mustrid, keskendudes iga tehingu üldisele struktuurile;
- Sisemised heuristikad, mis võimaldavad tehingu kõiki üksikasju põhjalikult uurida, ilma et see laieneks selle kontekstile;
- Välised heuristikad, mis hõlmavad tehingu analüüsi selle keskkonnas, samuti mis tahes välist andmeid, mis võivad pakkuda ülevaadet.

Bitcoini kasutajana on oluline valdada ahela analüüsi põhiprintsiipe, et seda tõhusalt vastu seista ja seeläbi kaitsta oma privaatsust.

## Tehniline mini-sõnastik:
**P2PKH:** lühend väljendist Pay to Public Key Hash. See on standardne skriptimudel, mida kasutatakse UTXO kulutamistingimuste kehtestamiseks. See võimaldab lukustada bitcoine avaliku võtme heshi peale, see tähendab, vastuvõtu aadressile. See skript on seotud Legacy standardiga ja tutvustati Bitcoin'i esimestes versioonides Satoshi Nakamoto poolt. Erinevalt P2PK-st, kus avalik võti on skriptis selgelt kaasatud, kasutab P2PKH avaliku võtme krüptograafilist jälge koos mõningate metaandmetega, mida nimetatakse ka "vastuvõtu aadressiks". See skript sisaldab avaliku võtme SHA256 hashi RIPEMD160 hashi ja nõuab, et fondidele juurdepääsuks peab saaja esitama selle hashiga vastavuses oleva avaliku võtme, samuti kehtiva digitaalse allkirja, mis on genereeritud seotud privaatvõtmest. P2PKH aadresse kodeeritakse Base58Check formaadis, mis annab neile vastupanuvõime trükivigadele tänu kontrollsumma kasutamisele. Need aadressid algavad alati numbriga 1.
**P2TR:** lühend väljendist Pay to Taproot ("maksa juurtipule"). See on standardne skriptimudel, mida kasutatakse kulutamistingimuste seadmiseks UTXO-le. P2TR tutvustati Taprooti rakendamisega novembris 2021. See kasutab Schnorri protokolli krüptograafiliste võtmete agregatsiooniks, samuti Merkle puude jaoks alternatiivsete skriptide jaoks, mida tuntakse kui MAST (Merkelized Alternative Script Tree). Erinevalt traditsioonilistest tehingutest, kus kulutamistingimused on avalikult nähtavad (mõnikord vastuvõtmisel, mõnikord kulutamisel), võimaldab P2TR keerukate skriptide peitmist ühe näilise avaliku võtme taha. Tehniliselt lukustab P2TR skript bitcoine unikaalse Schnorri avaliku võtme, mida tähistatakse kui K, peale. Siiski, see K võti on tegelikult avaliku võtme P ja avaliku võtme M agregaat, viimane arvutatakse ScriptPubKeys nimekirja Merkle juurest. Võtmete agregatsioon toimub kasutades Schnorri allkirjastamise protokolli. P2TR skriptiga lukustatud bitcoine saab kulutada kahel eristuval viisil: kas avaldades allkirja avaliku võtme P jaoks või rahuldades ühte skriptidest Merkle puus. Esimest võimalust nimetatakse "võtmeehiks" ja teist "skriptiteeks". Seega võimaldab P2TR kasutajatel saata bitcoine kas avalikule võtmele või mitmele nende valitud skriptile. Selle skripti veel üks eelis on see, et kuigi P2TR väljundi kulutamiseks on mitu võimalust, tuleb kulutamisel avalikustada ainult kasutatud viis, võimaldades kasutamata alternatiividel jääda privaatseks. Näiteks tänu Schnorri võtmete agregatsioonile võib avalik võti P ise olla agregaatvõti, mis potentsiaalselt esindab multisigi. P2TR on versioon 1 SegWit väljund, mis tähendab, et P2TR sisendite allkirjad salvestatakse tehingu tunnistajasse, mitte ScriptSig-sse. P2TR aadressid kasutavad Bech32m kodeeringut ja algavad bc1p-ga.

**P2WPKH:** lühend väljendist Pay to Witness Public Key Hash. See on standardne skriptimudel, mida kasutatakse kulutamistingimuste seadmiseks UTXO-le. P2WPKH tutvustati SegWiti rakendamisega augustis 2017. See skript on sarnane P2PKH-ga (Pay to Public Key Hash), kuna see samuti lukustab bitcoine avaliku võtme räsi põhjal, st vastuvõtu aadressil. Erinevus seisneb selles, kuidas allkirjad ja skriptid on tehingusse kaasatud. P2WPKH puhul liigutatakse allkirjaskripti teave (ScriptSig) traditsioonilisest tehingustruktuurist eraldi sektsiooni nimega Witness. See liigutus on SegWiti (Segregated Witness) uuenduse omadus. Sellel tehnikal on eelis tehinguandmete suuruse vähendamisel põhikehas, säilitades samal ajal vajaliku skriptiteabe valideerimiseks eraldi sektsioonis. Seetõttu on P2WPKH tehingud üldiselt vähem kulukad tasude osas võrreldes Legacy tehingutega. P2WPKH aadressid on kirjutatud kasutades Bech32 kodeeringut, mis aitab kaasa lühemale ja vähem eksimustele altuvale kirjutamisele tänu BCH kontrollsummale. Need aadressid algavad alati bc1q-ga, muutes need kergesti eristatavaks Legacy vastuvõtu aadressidest. P2WPKH on versioon 0 SegWit väljund.
**UTXO:** Lühend väljendist Kasutamata Tehingu Väljund. UTXO on tehingu väljund, mida ei ole veel kulutatud ega kasutatud uue tehingu sisendina. UTXO-d esindavad bitcoini kasutaja omandis olevat ja hetkel kulutamiseks saadaolevat bitcoini osa. Iga UTXO on seotud kindla väljundskriptiga, mis määratleb bitcoini kulutamiseks vajalikud tingimused. Bitcoinis tarbivad tehingud neid UTXO-sid sisenditena ja loovad uusi UTXO-sid väljunditena. UTXO mudel on Bitcoinile fundamentaalne, kuna see võimaldab lihtsalt kontrollida, et tehingud ei ürita kulutada olematuid või juba kulutatud bitcoine. Sisuliselt on UTXO tükk Bitcoinist.






