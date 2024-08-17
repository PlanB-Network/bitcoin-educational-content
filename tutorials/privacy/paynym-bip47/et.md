---
name: BIP47 - PayNym

description: Kuidas PayNymid töötavad
---
***HOIATUS:** Pärast Samourai Wallet'i asutajate arreteerimist ja nende serverite konfiskeerimist 24. aprillil ei saa rakendust enam kasutada kasutajad, kellel pole oma Dojot. BIP47 on endiselt kasutatav Sparrow Wallet'is kõikide kasutajate jaoks ja **Samourai Wallet'is ainult kasutajatele, kellel on Dojo**.*

_Jälgime selle juhtumi arenguid ning seotud tööriistade arenguid tähelepanelikult. Võite kindlad olla, et uuendame seda õpetust, kui saadaval on uut teavet._

_Seda õpetust pakutakse ainult hariduslikel ja informatiivsetel eesmärkidel. Me ei toeta ega julgusta nende tööriistade kasutamist kuritegelikel eesmärkidel. Iga kasutaja vastutab oma jurisdiktsiooni seadustega kooskõlas olemise eest._

---

> "Ta on liiga suur," ütlesid kõik, ja kalkun, kes oli sündinud kannustega ja arvas, et ta on keiser, paisus nagu laev kõikide purjedega üles ja marssis otse tema juurde suures raevus, tema silmad punased nagu tuli. Vaene väike pardipoeg ei teadnud, kas seista paigal või põgeneda, ja oli väga õnnetu, sest kõik õue pardid põlgasid teda.

![BIP47, inetu pardipoja illustratsioon](assets/1.webp)

Üks olulisemaid probleeme Bitcoin'i protokollis on aadresside taaskasutamine. Võrgu läbipaistvus ja jaotatus muudavad selle praktika kasutaja privaatsuse jaoks ohtlikuks. Probleemide vältimiseks on soovitatav iga uue sissetuleva makse jaoks kasutada uut tühja vastuvõtu aadressi, mis mõnel juhul võib olla keeruline saavutada.

See kompromiss on sama vana kui Valge Raamat. Satoshi hoiatas meid juba oma 2008. aasta lõpus avaldatud töös selle riski eest:

> "Lisakaitsemeetmena tuleks iga tehingu jaoks kasutada uut võtmepaari, et neid ei saaks siduda ühise omanikuga."

On palju lahendusi, mis võimaldavad vastu võtta mitmeid makseid ilma aadressi taaskasutamiseta. Igal neist on oma kompromissid ja puudused. Kõigi nende lahenduste seas on [BIP47](https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki), ettepanek, mille töötas välja Justus Ranvier ja avaldas 2015. aastal, mis võimaldab genereerida korduvkasutatavaid maksekoodid. Selle eesmärk on võimaldada teha mitu tehingut samale isikule ilma aadressi taaskasutamiseta.

Alguses suhtuti sellesse ettepanekusse osa kogukonna poolt põlgusega ja seda ei lisatud kunagi Bitcoin Core'i. Siiski otsustas mõni tarkvara seda omal käel rakendada. Näiteks arendas Samourai Wallet oma BIP47 rakenduse: PayNym. Täna on see rakendus saadaval Samourai Wallet'is nutitelefonidele, samuti [Sparrow Wallet'is](https://sparrowwallet.com/) arvutitele.

Aja jooksul on Samourai programmeerinud PayNymiga otseselt seotud uusi funktsioone. Nüüd on olemas terve tööriistade ökosüsteem, mis on loodud kasutaja privaatsuse optimeerimiseks PayNymi ja BIP47 põhjal.
Selles artiklis avastate BIP47 ja PayNymi põhimõtte, nende protokollide mehhanismid ja nendest tulenevad praktilised rakendused. Käsitletakse ainult BIP47 esimest versiooni, mida praegu PayNymi jaoks kasutatakse, kuid versioonid 2, 3 ja 4 töötavad praktiliselt samal viisil.
Ainus oluline erinevus leitakse teavitustehingus. Versioon 1 kasutab lihtsat aadressi koos OP_RETURN-iga teavitamiseks, versioon 2 kasutab multisig skripti (bloom-multisig) koos OP_RETURN-iga ja versioonid 3 ja 4 kasutavad lihtsalt multisig skripti (cfilter-multisig). Selles artiklis arutatud mehhanismid, sealhulgas uuritud krüptograafilised meetodid, on seega kohaldatavad kõigi nelja versiooni puhul. Praeguse seisuga kasutavad Samourai Wallet ja Sparrow PayNymi rakendamisel BIP47 esimest versiooni.

## Kokkuvõte:

1- Aadressi taaskasutamise probleem.

2- BIP47 ja PayNymi põhimõtted.

3- Õpetused: PayNymi kasutamine.

- BIP47 tehingu loomine Samourai Wallet'iga.
- BIP47 tehingu loomine Sparrow Wallet'iga.

4- BIP47 toimimine.

- Taaskasutatav maksekood.
- Krüptograafiline meetod: Diffie-Hellmani võtmevahetus, mis on loodud elliptilistel kõveratel (ECDH).
- Teavitustehing.
- Teavitustehingu koostamine.
- Teavitustehingu vastuvõtmine.
- BIP47 maksetehing.
- BIP47 makse vastuvõtmine ja privaatvõtme tuletamine.
- BIP47 makse tagastamine.

5- PayNymi tuletatud kasutusalad.

6- Minu isiklik arvamus BIP47 kohta.

## Aadressi taaskasutamise probleem.

Vastuvõttev aadress on mõeldud bitcoinide vastuvõtmiseks. See genereeritakse avalikust võtmest, rakendades sellele hashimist ja spetsiifilist formaati. Seega võimaldab see luua mündile uue kulutamistingimuse, et muuta selle omanikku.

> Lisateavet vastuvõtva aadressi genereerimise kohta soovitan lugeda selle artikli viimasest osast: Bitcoin Wallet - katkend raamatust [ebook Bitcoin Démocratisé 2](https://www.pandul.fr/post/le-portefeuille-bitcoin-extrait-ebook-bitcoin-d%C3%A9mocratis%C3%A9-2#viewer-epio7).

Lisaks olete tõenäoliselt juba kuulnud teadjalt bitcoinikasutajalt, et vastuvõtvad aadressid on mõeldud ühekordseks kasutamiseks ja et iga uue sissetuleva makse jaoks oma rahakotti peaks genereerima uue aadressi. Okei, aga miks?
Põhimõtteliselt ei ohusta aadressi taaskasutamine otseselt teie vahendeid. Krüptograafia kasutamine elliptilistel kõveratel võimaldab teil võrgule tõestada, et olete privaatvõtme omanik, ilma seda võtit avalikustamata. Seega võite lukustada mitu erinevat UTXO-d (kasutamata tehinguväljundit) samal aadressil ja kulutada neid erinevatel aegadel. Kui te ei avalikusta selle aadressiga seotud privaatvõtit, ei pääse keegi teie vahenditele ligi. Aadressi taaskasutamise probleem on rohkem seotud privaatsusega.

Nagu sissejuhatuses mainitud, tähendab Bitcoin võrgu läbipaistvus ja jaotatus, et igal kasutajal, kellel on juurdepääs sõlmele, on võimalik jälgida maksesüsteemi tehinguid. Selle tulemusena näevad nad erinevate aadresside saldojääke. Satoshi Nakamoto mainis siis uute võtmepaaride ja seega uute aadresside genereerimise võimalust iga uue sissetuleva makse jaoks rahakotti. Eesmärk oleks lisada täiendav tulemüür juhuks, kui kasutaja identiteet seostatakse ühe nende võtmepaariga.

Tänapäeval, kui kettanalüüsi ettevõtted on olemas ja KYC (Know Your Customer) arenguga, ei ole tühjade aadresside kasutamine enam lisatulemüür, vaid kohustus igaühele, kes hoolib isegi natuke oma privaatsusest.

Privaatsuse tagaajamine ei ole mugavus ega maksimalistlike Bitcoinikasutajate fantaasia. See on konkreetne parameeter, mis mõjutab otseselt teie isiklikku turvalisust ja teie vahendite turvalisust. Selle mõistmiseks toon teile väga konkreetse näite:
- Bob ostab Bitcoini läbi Dollar Cost Averaging (DCA) meetodi, mis tähendab, et ta soetab regulaarsete intervallidega väikese koguse Bitcoini, et keskmistada oma sisenemishinda. Bob saadab süsteemselt ostetud vahendid samale vastuvõtu aadressile. Ta ostab 0.01 Bitcoini iga nädal ja saadab selle samale aadressile. Kahe aasta pärast on Bobil sellel aadressil kogunenud terve Bitcoin.
- Nurgapealne pagar aktsepteerib Bitcoin'i makseid. Põnevil võimalusest Bitcoini kulutada, läheb Bob ostma oma baguette'i satoshi'des. Maksmiseks kasutab ta oma aadressil lukustatud vahendeid. Tema pagar saab nüüd teada, et tal on Bitcoin. See oluline summa võib tekitada kadedust ja Bob võib tulevikus riskida füüsilise rünnakuga.

Aadressi korduvkasutus võimaldab vaatlejal teha vaieldamatu seose teie erinevate UTXOde ja mõnikord teie isiku ning kogu teie rahakoti vahel.
Seetõttu genereerib enamik Bitcoin'i rahakottide tarkvara automaatselt uue vastuvõtu aadressi, kui klõpsate nupul "Vasta". Tavalistele kasutajatele ei ole uute aadresside kasutamise harjumuseks saamine suur ebamugavus. Siiski võib see piirang online-äridele, vahetustele või annetuskampaaniatele kiiresti muutuda haldamatuks.
Nendele organisatsioonidele on palju lahendusi. Igal neist on oma eelised ja puudused, kuid tänase seisuga ja nagu hiljem näeme, paistab BIP47 teistest selgelt silma.

See aadressi korduvkasutuse probleem ei ole Bitcoinis sugugi tühine. Nagu allpool oxt.me veebisaidilt võetud graafikust näha, on Bitcoin'i kasutajate üldine aadressi korduvkasutuse määr praegu 52%:
Graafik OXT.me-st, mis näitab Bitcoin'i võrgu üldise aadressi korduvkasutuse määra arengut.

![image](assets/2.webp)

Autor: OXT

Enamik neist korduvkasutustest pärineb vahetustest, mis efektiivsuse ja mugavuse huvides kasutavad sama aadressi mitu korda. Tänase seisuga oleks BIP47 parim lahendus selle nähtuse ohjeldamiseks vahetuste seas. See aitaks vähendada üldist aadressi korduvkasutuse määra, põhjustamata nendele üksustele liiga palju hõõrdumist.

See üle kogu võrgu ulatuv meede on sel juhul eriti asjakohane. Tõepoolest, aadressi korduvkasutus ei ole probleem ainult selle praktikaga tegelevale isikule, vaid ka kõigile, kes nendega tehinguid teevad. Privaatsuse kaotus Bitcoinis toimib nagu viirus, levides kasutajalt kasutajale. Kogu võrgu tehingute globaalse mõõtmise uurimine võimaldab meil mõista selle nähtuse ulatust.

## BIP47 ja PayNym põhimõtted.

BIP47 eesmärk on pakkuda lihtsat viisi mitme makse vastuvõtmiseks ilma aadressi korduvkasutuseta. Selle toimimine põhineb korduvkasutatava maksekoodi kasutamisel.

Seega saavad mitmed saatjad saata mitmeid makseid ühele korduvkasutatavale maksekoodile teisest kasutajast, ilma et saaja peaks iga uue tehingu jaoks pakkuma uut tühja aadressi.

Kasutaja võib oma maksekoodi vabalt jagada (sotsiaalvõrgustikes, oma veebisaidil...) ilma privaatsuse kaotuse riskita, erinevalt tavalisest vastuvõtu aadressist või avalikust võtmest.
Vahetuse läbiviimiseks peavad mõlemal kasutajal olema Bitcoin'i rahakott BIP47 rakendusega, nagu PayNym Samourai Wallet'is või Sparrow Wallet'is. Kahe kasutaja maksekoodide ühendamine loob nende vahel salajase kanali. Selle kanali nõuetekohaseks loomiseks peab saatja tegema tehingu Bitcoin'i plokiahelas: teavitustehingu (selgitan sellest hiljem rohkem).

Kahe kasutaja maksekoodide ühendamine genereerib jagatud saladusi, mis omakorda genereerivad suure hulga unikaalseid Bitcoin'i vastuvõtu aadresse (täpselt 2^32). Seega, tegelikkuses ei saadeta makse BIP47 maksekoodile, vaid täiesti tavalistele aadressidele, mis on tuletatud osapoolte maksekoodidest.
Maksekood toimib virtuaalse identifikaatorina, mis on tuletatud rahakoti seemnest. HD rahakoti tuletusstruktuuris asub maksekood sügavusel 3, rahakonto tasandil.
![image](assets/3.webp)

Selle tuletamise eesmärk on märgitud kui 47' (0x8000002F) viidates BIP47-le. Näiteks korduvkasutatava maksekoodi tuletamise tee oleks:

> m/47'/0'/0'/

Et anda teile ettekujutus, milline maksekood välja näeb, siin on minu oma:

> PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5

Seda saab kodeerida ka QR-koodina, et hõlbustada suhtlust:

![image](assets/4.webp)

Mis puutub PayNym Botsidesse, need robotid, mida näete Twitteris, siis need on lihtsalt teie maksekoodi visuaalsed esitlused, mille on loonud Samourai Wallet. Need genereeritakse kasutades räsifunktsiooni, mis muudab need peaaegu unikaalseks. Siin on minu oma koos selle identifikaatoriga:

> +throbbingpond8B1

![image](assets/5.webp)

Need Botsid ei oma mingit reaalset tehnilist kasutust. Selle asemel hõlbustavad nad kasutajatevahelisi suhtlusi, luues virtuaalse visuaalse identiteedi.

Kasutaja jaoks on BIP47 makse tegemine PayNym rakendusega äärmiselt lihtne. Kujutagem ette, et Alice soovib saata makseid Bobile:

1. Bob jagab oma QR-koodi või otse oma korduvkasutatavat maksekoodi. Ta võib selle paigutada oma veebisaidile, oma erinevatele avalikele sotsiaalvõrgustikele või saata selle Alicele mõne muu suhtlusvahendi kaudu.
2. Alice avab oma Samourai või Sparrow tarkvara ja skannib või kopeerib Bobi maksekoodi.
3. Alice seob oma PayNymi Bobi omaga ("Follow" inglise keeles). See toiming tehakse väljaspool ahelat ja on täiesti tasuta.

4. Alice ühendab oma PayNymi Bobi omaga ("Connect" inglise keeles). See toiming tehakse "on-chain". Alice peab maksma tehingu kaevandamistasud ning fikseeritud tasu 15 000 satsi Samourai teenuse eest. Sparrow's on teenustasud tühistatud. Seda sammu nimetame teavitustehinguks.

5. Kui teavitustehing on kinnitatud, saab Alice luua BIP47 maksetehingu Bobile. Tema rahakott genereerib automaatselt uue tühja vastuvõtu aadressi, mille privaatvõtit omab ainult Bob.

Teavitustehingu sooritamine, st PayNymi ühendamine, on BIP47 maksete tegemiseks kohustuslik eeltingimus. Kuid kui see on tehtud, saab saatja teha mitu makset saajale (täpselt 2^32) ilma, et oleks vaja teha uut teavitustehingut.

Te olete võib-olla märganud, et PayNymide omavahel ühendamiseks on kaks erinevat toimingut: "follow" ja "connect". Ühendamistoiming ("connect") vastab BIP47 teavitustehingule, mis on lihtsalt Bitcoin tehing teatud teabe edastamisega läbi OP_RETURN väljundi. Seega aitab see luua kahe kasutaja vahel krüpteeritud suhtluse, et toota vajalikud ühised saladused uute tühjade vastuvõtu aadresside genereerimiseks.

Teisest küljest võimaldab sidumistoiming ("follow" või "relier") luua lingi Sorobanil, krüpteeritud suhtlusprotokollil, mis põhineb Toril, eriti välja töötatud Samourai meeskondade poolt.

Kokkuvõtteks:
- Kahe PayNymi ("jälgimine") ühendamine on täiesti tasuta. See aitab luua off-chain krüpteeritud suhtlust, eriti Samourai koostööl põhinevate tehinguvahendite (Stowaway või StonewallX2) kasutamiseks. See toiming on spetsiifiline PayNymile ja seda ei kirjeldata BIP47-s.
- Kahe PayNymi ühendamine toob kaasa kulud. See hõlmab teavitustehingu sooritamist ühenduse alustamiseks. Kulu koosneb kõigist teenustasudest, tehingu kaevandamise tasudest ja 546 satsist, mis saadetakse saaja teavitusaadressile, et teavitada neid tunneli avamisest. See toiming on seotud BIP47-ga. Kui see on lõpule viidud, saab saatja teha mitu BIP47 makset saajale.

Kahe PayNymi ühendamiseks peavad need juba olema ühendatud.

## Õpetused: PayNymi kasutamine.

Nüüd, kui oleme teooria üle vaadanud, uurime koos praktikat. Allpool olevate õpetuste idee on ühendada minu PayNym minu Sparrow rahakotis minu PayNymiga minu Samourai rahakotis. Esimene õpetus näitab, kuidas teha tehingut, kasutades Samourai korduvkasutatavat maksekoodi Sparrow'le, ja teine õpetus kirjeldab sama mehhanismi Sparrow'st Samourai'le.

> Ma sooritasin need õpetused Testnetis. Need ei ole päris bitcoiinid.

### BIP47 tehingu loomine Samourai rahakotiga.

Alustuseks vajate ilmselgelt Samourai rahakoti rakendust. Selle saate otse alla laadida Google Play poest või APK-failina, mis on saadaval ametlikul Samourai veebisaidil.

Kui rahakott on algseadistatud, kui te pole seda juba teinud, taotlege oma PayNymi, klõpsates paremas alanurgas plussil (+), seejärel "PayNym".

Esimeseks sammuks BIP47 makse tegemiseks on meie saaja korduvkasutatava maksekoodi hankimine. Seejärel saame nendega ühendust võtta ja seejärel ühendada:

![video](assets/6.mp4)

Kui teavitustehing on kinnitatud, saan ma saajale saata mitu makset. Iga tehing tehakse automaatselt uue tühja aadressiga, mille võtmed on saajal. Saaja ei pea midagi tegema, kõik arvutatakse minu poolt.

Siin on, kuidas teha BIP47 tehingut Samourai rahakotiga:

![video](assets/7.mp4)

### BIP47 tehingu loomine Sparrow rahakotiga.

Nagu Samouraiga, peate ilmselgelt omama Sparrow tarkvara. See on saadaval teie arvutis. Selle saate alla laadida nende [ametlikult veebisaidilt](https://sparrowwallet.com/).

Veenduge, et kontrolliksite arendaja allkirja ja alla laaditud tarkvara terviklikkust enne selle installimist oma masinasse.

Looge rahakott ja taotlege oma PayNymi, klõpsates "Näita PayNymi" "Tööriist" menüüs ülal:

![image](assets/8.webp)

Seejärel peate oma PayNymi ühendama ja siduma oma saaja PayNymiga. Selleks sisestage nende korduvkasutatav maksekood aknasse "Leia kontakt", jälgige neid ja seejärel sooritage teavitustehing, klõpsates "Link Contact":

![image](assets/9.webp)

Kui teavitustehing on kinnitatud, saate saata makseid korduvkasutatavale maksekoodile. Siin on, kuidas seda teha:

![video](assets/10.mp4)

Nüüd, kui oleme suutnud uurida PayNymi rakendamise praktilist aspekti BIP47 puhul, vaatame, kuidas kõik need mehhanismid töötavad ja milliseid krüptograafilisi meetodeid kasutatakse.
BIP47 mehhanismide uurimiseks on oluline mõista hierarhilise deterministliku (HD) rahakoti struktuuri, lastevõtmete paaride tuletamise mehhanisme, samuti elliptilise kõvera krüptograafia põhimõtteid. Õnneks leiate kogu vajaliku teabe selle osa mõistmiseks minu blogist:
- [Bitcoini rahakoti tuletamisteede mõistmine](https://www.pandul.fr/post/comprendre-les-chemins-de-d%C3%A9rivation-d-un-portefeuille-bitcoin)

- [Bitcoini rahakott - katkend e-raamatust Bitcoin Democratized 2](https://www.pandul.fr/post/le-portefeuille-bitcoin-extrait-ebook-bitcoin-d%C3%A9mocratis%C3%A9-2)

### Korduvkasutatav maksekood.

Nagu selgitatud selle dokumendi teises osas, asub korduvkasutatav maksekood HD rahakoti kolmandal tasemel. See on mingil määral võrreldav xpub'iga, nii oma asukoha ja struktuuri kui ka rolli poolest.

Siin on erinevad osad, mis moodustavad 80-baidise maksekoodi:

- Bait 0: Versioon. Kui kasutate BIP47 esimest versiooni, siis see bait võrdub 0x01-ga.

- Bait 1: Bittide väli. See ruum on reserveeritud täiendavate näidustuste andmiseks spetsiifilise kasutuse korral. Kui kasutate lihtsalt PayNym'i, siis see bait võrdub 0x00-ga.

- Bait 2: Y pariteet. See bait näitab 0x02 või 0x03 sõltuvalt meie avaliku võtme y-koordinaadi väärtuse pariteedist (paaris või paaritu number). Selle praktika kohta lisateabe saamiseks lugege palun selle artikli "aadressi tuletamise" osa esimest sammu.

- Baitidest 3 kuni 34: X väärtus. Need baidid näitavad meie avaliku võtme x-koordinaati. X ja y pariteedi ühendamine annab meile meie kokkusurutud avaliku võtme.

- Baitidest 35 kuni 66: Ahela kood. See ruum on reserveeritud eelpool mainitud avaliku võtme ahela koodi jaoks.

- Baitidest 67 kuni 79: Täidis. See ruum on reserveeritud võimalike tulevaste arenduste jaoks. Versiooni 1 puhul täidame selle lihtsalt nullidega, et jõuda 80 baidini, mis on OP_RETURN väljundi andmete suurus.

Siin on minu korduvkasutatava maksekoodi heksadetsimaalne esitus, mis on esitatud eelmises jaotises, värvidega, mis vastavad ülalpool esitatud baitidele:
Järgmisena peate lisama ka eesliite baiti "P", et kiiresti tuvastada, et tegemist on maksekoodiga. See bait on 0x47.

> 0x47010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c470c390d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a00000000000000000000000000

Lõpuks arvutame selle maksekoodi kontrollsumma kasutades HASH256, mis tähendab topelt hasheerimist SHA256 funktsiooniga. Me võtame selle seede esimesed neli baiti ja ühendame need lõppu (roosas).
Maksekood on valmis, nüüd peame selle teisendama Base 58 formaati:

> PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5

Nagu näete, sarnaneb see konstruktsioon laiendatud avaliku võtme struktuurile, mida tüübilt nimetatakse "xpub".

Selle protsessi käigus, et saada meie maksekood, kasutasime kokkusurutud avalikku võtit ja ahelakoodi. Need kaks elementi on deterministliku ja hierarhilise tuletuse tulemus rahakoti seemnest, järgides järgmist tuletusteed: m/47'/0'/0'/
Konkreetsemalt, et saada korduvkasutatava maksekoodi avalik võti ja ahelakood, arvutame meistervõtme seemnest, seejärel tuletame lapsepaari indeksiga 47 + 2^31 (kõvendatud tuletus). Seejärel tuletame veel kaks lapsepaari indeksiga 2^31 (kõvendatud tuletus).

> Kui soovite rohkem teada saada lapsevõtmepaaride tuletamisest hierarhilises deterministlikus Bitcoin'i rahakotis, soovitan võtta CRYPTO301.

### Krüptograafiline meetod: Elliptilise kõvera Diffie-Hellmani võtmevahetus (ECDH).

BIP47 tuumaks kasutatav krüptograafiline meetod on ECDH (Elliptilise-Kõvera Diffie-Hellman). See protokoll on klassikalise Diffie-Hellmani võtmevahetuse variant.

Diffie-Hellman, oma esimeses versioonis, on võtmeleppimise protokoll, mis esitati 1976. aastal ja võimaldab kahel osapoolel, kummalgi oma avaliku ja privaatvõtmepaariga, määrata jagatud saladuse, vahetades teavet ebaturvalise suhtluskanali kaudu.

![image](assets/11.webp)

See jagatud saladus (punane võti) saab seejärel kasutada muudeks ülesanneteks. Tavaliselt saab seda jagatud saladust kasutada suhtluse krüpteerimiseks ja dekrüpteerimiseks ebaturvalisel võrgul:

![image](assets/12.webp)

Selle vahetuse saavutamiseks kasutab Diffie-Hellman modulaararitmeetikat jagatud saladuse arvutamiseks. Siin on lihtsustatud selgitus, kuidas see töötab:

- Alice ja Bob lepivad kokku ühises värvuses, sel juhul kollases. See värv on kõigile teada. See on avalik teave.

- Alice valib salajase värvi, sel juhul punase. Ta segab kaks värvi, mille tulemuseks on oranž.

- Bob valib salajase värvi, sel juhul teal sinise. Ta segab kaks värvi, mille tulemuseks on taevassinine.

- Alice ja Bob saavad vahetada saadud värve: oranži ja taevassinist. See vahetus võib toimuda ebaturvalisel võrgul ja seda võivad jälgida ründajad.

- Alice segab Bobilt saadud taevassinist värvi oma salajase värviga (punane). Ta saab pruuni.

- Bob segab Alicelt saadud oranži värvi oma salajase värviga (teal sinine). Ta saab samuti pruuni.

![image](assets/13.webp)
> z on võrdne A tõstetud b astmesse modulo p:
> z = A^b % p

- Meenutuseks, A = g^a % p. Seega:

  > z = A^b % p
  > z = (g^a)^b % p
  >
  > Astendamise reeglite kohaselt:
  >
  > (x^n)^m = x^nm
  >
  > Seega:
  >
  > z = g^ab % p

Selles lihtsustuses esindab pruun värv saladust, mis on Alice'i ja Bobi vahel jagatud. Tuleb ette kujutada, et tegelikkuses on ründajal võimatu eraldada oranži ja taevassinist värvi, et saada kätte Alice'i või Bobi salajased värvid.

Nüüd vaatleme selle tegelikku toimimist. Esmapilgul võib Diffie-Hellmani võtmevahetus tunduda keeruline mõista. Tegelikkuses on toimimispõhimõte peaaegu lapselikult lihtne. Enne selle mehhanismide detailsemat kirjeldamist tuletan kiiresti meelde kahte matemaatilist kontseptsiooni, mida me vajame (ja mis muuseas on kasutusel ka paljudes teistes krüptograafilistes meetodites).

1. Algarv on loomulik arv, millel on ainult kaks jagajat: 1 ja iseennast. Näiteks number 7 on algarv, sest seda saab jagada ainult 1 ja 7 (iseendaga). Teisest küljest, number 8 ei ole algarv, sest seda saab jagada 1, 2, 4 ja 8-ga. Seega ei ole tal mitte ainult kaks jagajat, vaid neli täis- ja positiivset jagajat.

2. "Modulo" (tähisega "mod" või "%") on matemaatiline tehe, mis võimaldab kahe täisarvu puhul tagastada esimese arvu ja teise arvu Eukleidese jagamise jäägi. Näiteks 16 mod 5 on võrdne 1-ga.

Diffie-Hellmani võtmevahetus Alice'i ja Bobi vahel toimib järgmiselt:

- Alice ja Bob määravad kaks ühist numbrit: p ja g. p on algarv. Mida suurem see number p on, seda turvalisem Diffie-Hellman on. g on p primitiivjuur. Neid kahte numbrit saab edastada lihttekstina turvamata võrgu kaudu, need on võrdsed ülaltoodud lihtsustuses kollase värviga. Alice'il ja Bobil peab olema p ja g väärtuste osas täpselt samad arvud.

- Kui parameetrid on valitud, määravad Alice ja Bob igaüks omaette salajase juhuarvu. Alice'i saadud juhuarvu nimetatakse a-ks (võrdne punase värviga) ja Bobi saadud juhuarvu nimetatakse b-ks (võrdne teal värviga). Need kaks numbrit peavad jääma salajaseks.

- Selle asemel, et vahetada neid numbreid a ja b, arvutab iga osapool A (suurtäht) ja B (suurtäht) nii, et:

> A on võrdne g tõstetud a astmesse modulo p:
> A = g^a % p

> B on võrdne g tõstetud b astmesse modulo p:
> B = g^b % p

- Neid numbreid A (võrdne oranži värviga) ja B (võrdne taevassinise värviga) vahetatakse kahe osapoole vahel. Vahetus saab toimuda lihttekstina turvamata võrgu kaudu.

- Alice, kes nüüd teab B-d, arvutab z väärtuse nii, et:

> z on võrdne B tõstetud a astmesse modulo p:
> z = B^a % p
z on võrdne A astmega b modulo p:
> z = A^b % p

Seega:
> z = (g^a)^b % p
> z = g^ab % p
> z = g^ba % p

Tänu modulo operaatori distributiivsusele leiavad Alice ja Bob täpselt sama väärtuse z jaoks. See number esindab nende jagatud saladust, mis on võrdne eelnevas selgituses mainitud pruuni värviga. Nad saavad seda jagatud saladust kasutada suhtluse krüpteerimiseks nende vahel ebaturvalisel võrgul.

![Diffie-Hellmani tehnilise toimingu diagramm](assets/14.webp)

Ründaja, kes omab p, g, A ja B väärtusi, ei suuda arvutada a, b või z väärtusi. Selle operatsiooni sooritamine nõuaks eksponenteerimise ümberpööramist, mis on võimatu teha muul viisil kui kõiki võimalusi ükshaaval proovides, kuna me töötame lõpliku väljaga. See oleks võrdne diskreetse logaritmi arvutamisega, mis on eksponenteerimise vastand tsüklilises lõplikus grupis.

Seega, kuni me valime piisavalt suured väärtused a, b ja p jaoks, on Diffie-Hellman turvaline. Tavaliselt, parameetritega 2048 bitti (number, millel on kümnendsüsteemis 600 numbrit), oleks kõikide võimaluste testimine a ja b jaoks ebapraktiline. Praeguse seisuga, sellise suurusega numbritega, peetakse algoritmi turvaliseks.

Siin peitubki Diffie-Hellmani protokolli peamine puudus. Turvalisuse tagamiseks peab algoritm kasutama suuri numbreid. Selle tulemusena eelistatakse nüüd ECDH algoritmi, mis on Diffie-Hellmani variant, mis kasutab algebralist kõverat, täpsemalt elliptilist kõverat. See võimaldab meil töötada palju väiksemate numbritega, säilitades samas võrdväärse turvalisuse, vähendades seeläbi vajalikke arvutus- ja salvestusressursse.

Algoritmi üldpõhimõte jääb samaks. Siiski, selle asemel, et kasutada juhuslikku numbrit a ja numbrit A, mis on arvutatud a-st kasutades modulaarset eksponenteerimist, kasutame paari võtmeid, mis on loodud elliptilisel kõveral. Modulo operaatori distributiivsuse asemel kasutame elliptilistel kõveratel grupiseadust, täpsemalt selle seaduse assotsiatiivsust.
Kui teil puuduvad teadmised, kuidas privaatsed ja avalikud võtmed elliptilisel kõveral töötavad, selgitan selle meetodi põhitõdesid selle artikli esimeses kuues osas.

Lühidalt kokkuvõttes, privaatvõti on juhuslik number vahemikus 1 kuni n-1 (kus n on kõvera järk), ja avalik võti on kõveral unikaalne punkt, mis on määratud privaatvõtmest lähtuvalt punkti lisamise ja kahekordistamise teel generaatorpunktist, järgnevalt:

> K = k·G

Kus K on avalik võti, k on privaatvõti ja G on generaatorpunkt.

Üks selle võtmepaari omadustest on, et K on väga lihtne kindlaks määrata, kui te teate k ja G, kuid praegu on võimatu kindlaks määrata k, kui te teate K ja G. See on ühesuunaline funktsioon.

Teisisõnu, avaliku võtme saab hõlpsasti arvutada, kui teate privaatvõtit, kuid on võimatu arvutada privaatvõtit, kui teate avalikku võtit. See turvalisus põhineb taas diskreetse logaritmi arvutamise võimatusele.

Me kasutame seda omadust, et kohandada meie Diffie-Hellmani algoritmi. Seega, ECDH toimimispõhimõte on järgmine:

- Alice ja Bob lepivad kokku krüptograafiliselt turvalises elliptilises kõveras ja selle parameetrites. See teave on avalik.
- Alice genereerib juhusliku numbri ka, mis saab olema tema privaatvõti. See privaatvõti peab jääma saladuseks. Ta määrab oma avaliku võtme Ka, lisades ja kahekordistades punkte valitud elliptilisel kõveral.
> Ka = ka·G

- Bob genereerib samuti juhusliku numbri kb, mis saab olema tema privaatvõti. Ta arvutab vastava avaliku võtme Kb.

> Kb = kb·G

- Alice ja Bob vahetavad oma avalikke võtmeid Ka ja Kb üle ebaturvalise avaliku võrgu.

- Alice arvutab kõvera punkti (x, y), rakendades oma privaatvõtit ka Bobi avalikule võtmele Kb.

> (x, y) = ka·Kb

- Bob arvutab kõvera punkti (x, y), rakendades oma privaatvõtit kb Alice'i avalikule võtmele Ka.

> (x, y) = kb·Ka

- Alice ja Bob saavad elliptilisel kõveral sama punkti. Jagatud saladus saab olema selle punkti x-koordinaat.

Nad saavad sama jagatud saladuse, sest:

> (x, y) = ka·Kb = ka·kb·G = kb·ka·G = kb·Ka

Potentsiaalne ründaja, kes jälgib ebaturvalist avalikku võrku, saab ainult kätte mõlema osapoole avalikud võtmed ja valitud kõvera parameetrid. Nagu varem selgitatud, ei võimalda need kaks teavetükki üksinda privaatvõtmete kindlaksmääramist, seega ei saa ründaja ligi saladusele.
ECDH on algoritm, mis võimaldab võtmevahetust. Seda kasutatakse sageli koos teiste krüptograafiliste meetoditega, et määratleda protokoll. Näiteks kasutatakse ECDH-d TLS-i (Transport Layer Security) tuumas, mis on interneti transpordikihi jaoks mõeldud krüpteerimis- ja autentimisprotokoll. TLS kasutab võtmevahetuseks ECDHE-d, ECDH variatsiooni, kus võtmed on efemeersed, et tagada püsiv konfidentsiaalsus. Lisaks ECDHE-le kasutab TLS ka autentimisalgoritmi nagu ECDSA, krüpteerimisalgoritmi nagu AES ja räsifunktsiooni nagu SHA256.

TLS määratleb "s" "https"-is ja väikese lukusümboli, mida näete oma internetibrauseri ülemises vasakus nurgas, mis tagavad krüpteeritud suhtluse. Seega kasutate ECDH-d praegu selle artikli lugemisel ja tõenäoliselt kasutate seda iga päev, ilma et seda teaksite.

### Teavitustransaktsioon.

Nagu eelmises jaotises avastasime, on ECDH Diffie-Hellmani vahetuse variant, mis hõlmab võtmepaare, mis on loodud elliptilisel kõveral. Õnneks on meil oma Bitcoin'i rahakottides palju võtmepaare, mis vastavad sellele standardile!

Mõte on kasutada mõlema osapoole hierarhilistest deterministlikest Bitcoin'i rahakottidest võtmepaare, et luua nende vahel jagatud ja efemeersed saladused. BIP47-s kasutatakse selle asemel ECDHE-d (Elliptic Curve Diffie-Hellman Ephemeral).

ECDHE-d kasutatakse algselt BIP47-s saatja maksekoodi edastamiseks saajale. See on kuulus teavitustransaktsioon. Selleks, et BIP47-d kasutada, peavad mõlemad osapooled (saatja, kes teeb makseid, ja saaja, kes võtab makseid vastu) olema teadlikud teineteise maksekoodidest. See on vajalik efemeersete avalike võtmete ja seega pühendatud vastuvõtu aadresside tuletamiseks.
Enne seda vahetust teab saatja loogiliselt juba saaja maksekoodi, kuna nad võisid selle saada väljaspool ahelat, näiteks nende veebisaidilt või sotsiaalmeediast. Siiski ei pruugi saaja tingimata teada saatja maksekoodi. See tuleb neile edastada, vastasel juhul ei saa nad tuletada oma ajutisi võtmeid ja seega ei saa nad teada, kus nende bitcoiinid asuvad, ega saa oma vahendeid avada. See võiks neile edastada väljaspool ahelat, kasutades mõnda muud suhtlusviisi, kuid see tekitaks probleemi, kui rahakott taastatakse seemnest. Tõepoolest, nagu ma juba mainisin, ei tuletata BIP47 aadresse saaja seemnest (vastasel juhul oleks parem kasutada otse ühte nende xpubidest), vaid need on arvutuse tulemus, mis hõlmab nii saaja maksekoodi kui ka saatja maksekoodi. Seega, kui saaja kaotab oma rahakoti ja üritab seda oma seemnest taastada, peab tal tingimata olema kõik maksekoodid inimestelt, kes on neile bitcoine saatnud BIP47 kaudu.

BIP47 kasutamine ilma selle teavitustehinguta oleks võimalik, kuid iga kasutaja peaks varundama oma eakaaslaste maksekoodid. See olukord jääb juhitamatuks, kuni leitakse lihtne ja vastupidav viis nende varunduste loomiseks, salvestamiseks ja uuendamiseks. Seega on teavitustehing praeguses olukorras peaaegu kohustuslik.

Lisaks maksekoodide varundamise rollile, nagu selle nimi viitab, toimib see tehing ka teavitamisena saajale. See teavitab nende klienti, et tunnel on just avatud.

Enne teavitustehingu tehnilise toimimise üksikasjalikumat selgitamist tahaksin natuke rääkida privaatsusmudelist. Tõepoolest, BIP47 privaatsusmudel õigustab teatud ettevaatusabinõusid, mida võetakse selle esialgse tehingu koostamisel.

Maksekood ise ei kujuta otseselt privaatsusriski. Erinevalt klassikalisest Bitcoin mudelist, mis võimaldab kasutaja identiteedi ja tehingute vahelise infovoo katkestamist, eriti avalikke võtmeid anonüümsena hoides, võib maksekoodi otseselt seostada identiteediga. See ei ole kohustuslik, kuid see seos ei ole ohtlik.

Tõepoolest, maksekood ei tuleta otseselt aadresse, mida kasutatakse BIP47 maksete vastuvõtmiseks. Selle asemel saadakse aadressid, rakendades ECDHE-d mõlema poole maksekoodide lastevõtmete vahel.

Seega ei kujuta maksekood üksinda otseselt privaatsusriski, kuna ainult teavitusaadress on sellest tuletatud. Sellest võib järeldada teatud teavet, kuid tavaliselt ei saa keegi teada, kellega te tehinguid teete.

Seetõttu on oluline säilitada range eraldatus kasutajate maksekoodide vahel. Selles suhtes on koodi esialgne suhtlusaste kriitiline hetk makse privaatsuse jaoks, ja siiski on see protokolli nõuetekohaseks toimimiseks kohustuslik. Kui ühte maksekoodi saab avalikult hankida (näiteks veebisaidilt), ei tohiks teist koodi, st saatja koodi, seostada esimesega.

Näiteks kujutagem ette, et tahan teha annetuse BIP47 kaudu rahumeelsele protestiliikumisele Kanadas:

- See organisatsioon on oma maksekoodi avaldanud otse oma veebisaidil või sotsiaalmeedia platvormidel.
- Seega on see kood seotud liikumisega.

- Ma hangin selle maksekoodi.

- Enne kui saan neile tehingu saata, pean veenduma, et nad on teadlikud minu isiklikust maksekoodist, mis on samuti seotud minu identiteediga, kuna kasutan seda tehingute vastuvõtmiseks oma sotsiaalvõrgustikest.

Kuidas ma saan selle neile edastada? Kui saadan selle neile kasutades tavapärast suhtlusviisi, võib teave lekkida ja mind võidakse tuvastada inimesena, kes toetab rahumeelseid liikumisi.
Teavitustransaktsioon ei ole kindlasti ainus lahendus saatja maksekoodi salajaseks edastamiseks, kuid praegu täidab see rolli suurepäraselt, rakendades mitmeid turvakihte.
Allpool olevas diagrammis tähistavad punased jooned hetke, mil informatsiooni voo tuleb katkestada, ja mustad nooled tähistavad vaieldamatuid seoseid, mida saab teha välise vaatleja poolt:

![Privaatsusmudeli diagramm korduvkasutatava maksekoodi jaoks](assets/15.webp)

Tegelikkuses on Bitcoin'i klassikalise privaatsusmudeli puhul sageli keeruline täielikult katkestada informatsiooni voo võtmepaari ja kasutaja vahel, eriti kaugtehingute sooritamisel. Näiteks annetuskampaania korral peab saaja oma veebisaidil või sotsiaalmeedia platvormidel avalikustama aadressi või avaliku võtme. BIP47 nõuetekohane kasutamine, st teavitustransaktsioon, lahendab selle probleemi ECDHE ja krüpteerimiskihi abil, mida me uurime.

Ilmselgelt järgitakse Bitcoin'i klassikalist privaatsusmudelit ka kahe maksekoodi ühendamisel tuletatud efemeersete avalike võtmete tasandil. Mõlemad mudelid on omavahel sõltuvad. Ma soovin lihtsalt siin rõhutada, et erinevalt klassikalisest avaliku võtme kasutamisest bitcoinide vastuvõtmiseks, saab maksekoodi seostada identiteediga, kuna teave "Bob teeb tehingu Alicega" katkestatakse teisel hetkel. Maksekoodi kasutatakse makseaadresside genereerimiseks, kuid ainult plokiahela vaatlemisel on võimatu seostada BIP47 maksetehingut kasutatud maksekoodidega.

### Teavitustransaktsiooni konstrueerimine.

Nüüd vaatame, kuidas see teavitustransaktsioon toimib. Kujutame ette, et Alice soovib saata vahendeid Bobile, kasutades BIP47. Minu näites toimib Alice saatjana ja Bob saajana. Bob on oma maksekoodi juba oma veebisaidil avaldanud, seega on Alice juba teadlik Bobi maksekoodist.

1. Alice arvutab jagatud saladuse ECDH abil:

- Ta valib oma HD rahakotist erinevalt harult võtmepaari, mida ei tohiks kergesti seostada Alice'i teavitusaadressi või Alice'i identiteediga (vt eelmine jaotis).
- Alice valib sellest paarist privaatvõtme. Me nimetame seda "a" (väiketäht).

> a

- Alice hangib Bobi teavitusaadressiga seotud avaliku võtme. See võti on Bobi maksekoodist tuletatud esimene laps (indeks 0). Me nimetame seda avalikku võtit "B" (suurtäht). Selle avaliku võtmega seotud privaatvõtit nimetatakse "b" (väiketäht). "B" määratakse elliptilisel kõveral punktide liitmise ja kahekordistamise teel "G" (generaatorpunkt) abil "b" (privaatvõti) kasutades.

> B = b·G

- Alice arvutab elliptilisel kõveral saladuspunkti "S" (suurtäht) punktide liitmise ja kahekordistamise teel, rakendades oma privaatvõtit "a" Bobi avalikule võtmele "B".

> S = a·B

- Alice arvutab pimestamisteguri "f", mida kasutatakse tema maksekoodi krüpteerimiseks. Selleks genereerib ta pseudojuhusliku numbri, kasutades HMAC-SHA512 funktsiooni. Selle funktsiooni teise sisendina kasutab ta väärtust, mille saab taastada ainult Bob: (x), mis on eelnevalt arvutatud saladuspunkti x-koordinaat. Esimene sisend on (o), mis on selle tehingu sisendina tarbitud UTXO (väljundpunkt).

> f = HMAC-SHA512(o, x)

2. Alice teisendab oma isikliku maksekoodi aluseks 2 (binaarne).
3. Ta kasutab seda pimestamistegurit võtmena, et teostada sümmeetrilist krüpteerimist oma maksekoodi andmepaketil. Kasutatav krüpteerimisalgoritm on lihtsalt XOR. Teostatav toiming on sarnane Vernami šifriga, mida tuntakse ka kui "ühekordset paberit":
- Alice jagab esmalt oma pimestamisteguri kaheks osaks: esimesed 32 baiti nimetatakse "f1" ja viimased 32 baiti nimetatakse "f2". Seega meil on:

> f = f1 || f2

- Alice arvutab krüptoteksti (x') maksekoodi avaliku võtme x-koordinaadi (x) jaoks ning eraldi arvutab krüptoteksti (c') oma ahelakoodi (c) jaoks. "f1" ja "f2" toimivad krüpteerimisvõtmetena ning kasutatakse XOR operatsiooni.

> x' = x XOR f1
>
> c' = c XOR f2

- Alice asendab oma maksekoodis avaliku võtme abskissa (x) ja ahelakoodi (c) tegelikud väärtused krüpteeritud väärtustega (x') ja (c').

Enne selle teavitustehingu tehnilise kirjelduse jätkamist, võtame hetke, et arutada XOR operatsiooni üle. XOR on bittide loogiline operaator, mis põhineb Boole'i algebral. Antud kahe biti operandi korral tagastab see 1, kui vastavad bitid on erinevad, ja tagastab 0, kui vastavad bitid on võrdsed. Siin on tõeväärtustabel XOR jaoks, lähtudes operandide D ja E väärtustest:

| D   | E   | D XOR E |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |

Näiteks:

> 0110 XOR 1110 = 1000

Või:

> 010011 XOR 110110 = 100101

ECDH puhul on XOR-i kasutamine krüpteerimiskihina eriti koherentne. Esiteks, tänu sellele operaatorile, on krüpteerimine sümmeetriline. See võimaldab saajal dekrüpteerida maksekoodi sama võtmega, mida kasutati krüpteerimiseks. Krüpteerimis- ja dekrüpteerimisvõti arvutatakse jagatud saladusest, kasutades ECDH-d.

See sümmeetria on võimaldatud XOR operaatori kommutatiivsuse ja assotsiatiivsuse omaduste tõttu:

- Muud omadused:
  -> D ⊕ D = 0
  -> D ⊕ 0 = D

- Kommutatiivsus:
  D ⊕ E = E ⊕ D

- Assotsiatiivsus:
  D ⊕ (E ⊕ Z) = (D ⊕ E) ⊕ Z = D ⊕ E ⊕ Z

- Sümmeetria:
  Kui: D ⊕ E = L
  Siis: D ⊕ L = D ⊕ (D ⊕ E) = D ⊕ D ⊕ E = 0 ⊕ E = E
  -> D ⊕ L = E
Järgnevalt on see krüpteerimismeetod väga sarnane Vernami šifriga (Ühekordne Plokk), mis on ainus tänaseks teadaolev krüpteerimisalgoritm, millel on tingimusteta (või absoluutne) turvalisus. Selleks, et Vernami šifr omaks seda omadust, peab krüpteerimisvõti olema täiesti juhuslik, olema sama suur kui sõnum ja kasutatud vaid üks kord. BIP47-s kasutatavas krüpteerimismeetodis on võti tõepoolest sama suur kui sõnum, pimestamisfaktor on täpselt sama suur kui avaliku võtme x-koordinaadi ja maksekoodi ahela koodi ühendamine. See krüpteerimisvõti kasutatakse tõepoolest ainult üks kord. Siiski ei tuleta seda võtit täiuslikust juhuslikust allikast, kuna see on HMAC. See on pigem pseudojuhuslik. Seetõttu ei ole see Vernami šiffer, kuid meetod on sarnane.
Räägime nüüd meie teavitustransaktsiooni konstrueerimisest:

4. Alicel on praegu tema maksekood krüpteeritud andmetega. Ta koostab ja edastab transaktsiooni, mis hõlmab tema avalikku võtit "A" sisendina, väljundit Bobi teavitusaadressile ja OP_RETURN väljundit, mis koosneb tema maksekoodist krüpteeritud andmetega. See transaktsioon on teavitustransaktsioon.

OP_RETURN on Opcodes, mis on skript, mis märgib Bitcoin'i transaktsiooni väljundi kehtetuks. Täna kasutatakse seda teabe edastamiseks või ankurdamiseks Bitcoin'i plokiahelas. See võib salvestada kuni 80 baiti andmeid, mis on ahelas salvestatud ja seega nähtavad kõigile teistele kasutajatele.

Nagu me eelmises jaotises nägime, kasutatakse Diffie-Hellmani jagatud saladuse genereerimiseks kahe kasutaja vahel, kes suhtlevad ebaturvalises võrgus, mida võivad jälgida ründajad. BIP47-s kasutatakse ECDH-d suhtlemiseks Bitcoin'i võrgus, mis oma olemuselt on läbipaistev suhtlusvõrk, mida jälgib palju ründajaid. Elliptilisel kõveral toimuva Diffie-Hellmani võtmevahetuse kaudu arvutatud jagatud saladust kasutatakse seejärel saladuse krüpteerimiseks: saatja (Alice'i) maksekood.

Siin on diagramm BIP47-st, mis illustreerib just kirjeldatut:

![Diagramm Alice saadab oma maskeeritud maksekoodi Bobi teavitusaadressile](assets/16.webp)

Autoriõigus: Taaskasutatavad Maksekoodid Hierarhilistele Deterministlikele Rahakottidele, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Kui sobitame selle diagrammi sellega, mida ma varem kirjeldasin:

- "Wallet Priv-Key" Alice'i poolel vastab: a.

- "Child Pub-Key 0" Bobi poolel vastab: B.
- "Notification Shared Secret" vastab: f.
- "Masked Payment Code" vastab krüpteeritud maksekoodile, st krüpteeritud andmetega: x' ja c'.

- "Notification Transaction" on transaktsioon, mis sisaldab OP_RETURN-i.

Kokkuvõttes läbisime just sammud, et teostada teavitustransaktsioon:

- Alice hangib Bobi maksekoodi ja teavitusaadressi.

- Alice valib oma HD rahakotis kuuluva UTXO, millel on vastav võtmepaar.

- Ta arvutab elliptilisel kõveral salajase punkti, kasutades ECDH-d.

- Ta kasutab seda salajast punkti HMAC-i arvutamiseks, mis on pimestamisfaktor.

- Ta kasutab seda pimestamisfaktorit oma isikliku maksekoodi andmete krüpteerimiseks.

- Ta kasutab OP_RETURN transaktsiooni väljundit, et edastada maskeeritud maksekood Bobile.

Et paremini mõista selle toimimist, eriti OP_RETURN kasutamist, uurime koos reaalset teavitustransaktsiooni. Sooritasin sellise transaktsiooni Testnetis, mille leiate klõpsates siin:
Vaadeldes seda tehingut, võime juba näha, et sellel on üks sisend ja 4 väljundit:

- Esimene väljund on OP_RETURN, mis sisaldab minu maskeeritud maksekoodi.

- Teine väljund 546 satsi suunab saaja teavitusaadressile.

- Kolmas väljund 15 000 satsi esindab teenustasu, kuna kasutasin selle tehingu koostamiseks Samourai rahakotti.

- Neljas väljund kahe miljoni satsi suuruses esindab ülejääki, st minu sisendist järele jäänud erinevust, mis läheb tagasi teisele aadressile, mis kuulub mulle.

Kõige huvitavam uurida on ilmselgelt väljund 0, kasutades OP_RETURN. Vaatame lähemalt, mida see sisaldab:

Avastame väljundi heksadekimaalse skripti:

> 6a4c50010002b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164927b0e88f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d800000000000000000000000000

Selles skriptis saame eristada mitmeid osi:
Opcodes'ide seas võime ära tunda 0x6a, mis viitab OP_RETURNile ja 0x4c, mis viitab OP_PUSHDATA1-le. Sellele opkoodile järgnev bait näitab järgneva koormuse suurust. See näitab 0x50, mis on 80 baiti.

Järgneb maksekood krüpteeritud koormusega.

Siin on minu maksekood, mida kasutati selles tehingus:

> Baasis 58:
>
> PM8TJQCyt6ovbozreUCBrfKqmSVmTzJ5vjqse58LnBzKFFZTwny3KfCDdwTqAEYVasn11tTMPc2FJsFygFd3YzsHvwNXLEQNADgxeGnMK8Ugmin62TZU
>
> Baasis 16 (HEX):
> 4701000277507c9c17a89cfca2d3af554745d6c2db0e7f6b2721a3941a504933103cc42add94881210d6e752a9abc8a9fa0070e85184993c4f643f1121dd807dd556d1dc000000000000000000000000008604e4db

Kui võrdleme minu maksekoodi OP_RETURNiga, võime näha, et HRP (pruunis) ja kontrollsumma (roosas) ei edastata. See on normaalne, kuna see teave on mõeldud inimestele.
Järgnevalt võime ära tunda (roheliselt) versiooni (0x01), bitivälja (0x00) ja avaliku võtme paarsuse (0x02). Ja maksekoodi lõpus tühjad baidid mustana (0x00), mis võimaldavad täita kuni 80 baiti. Kogu see metaandmed edastatakse lihttekstina (krüpteerimata). Lõpuks võime märgata, et avaliku võtme x-koordinaat (siniselt) ja ahelakood (punane) on krüpteeritud. See moodustab maksekoodi andmeploki.

### Teavitustransaktsiooni vastuvõtmine.

Nüüd, kui Alice on saatnud teavitustransaktsiooni Bobile, vaatame, kuidas ta seda tõlgendab.

Meenutuseks, Bob peab olema võimeline ligi pääsema Alice'i maksekoodile. Ilma selle teabeta, nagu me järgmises jaotises näeme, ei suuda ta tuletada Alice'i loodud võtmepaare ja seega ei saa ta ligi pääseda oma bitcoinidele, mis on saadud BIP47 abil. Praegu on Alice'i maksekoodi andmeplokk krüpteeritud. Vaatame koos, kuidas Bob selle lahti krüpteerib.

1. Bob jälgib tehinguid, mis loovad väljundeid tema teavitusaadressile.

2. Kui tehingul on väljund tema teavitusaadressile, analüüsib Bob seda, et näha, kas see sisaldab OP_RETURN väljundit, mis vastab BIP47 standardile.

3. Kui OP_RETURN andmeploki esimene bait on 0x01, alustab Bob võimaliku jagatud saladuse otsimist ECDH abil:

- Bob valib tehingu sisendis oleva avaliku võtme. See tähendab Alice'i avalikku võtit nimega "A":

> A = a·G

- Bob valib oma isikliku teavitusaadressiga seotud privaatvõtme "b":

> b

- Bob arvutab elliptilisel kõveral saladuspunkti "S" (ECDH jagatud saladus), lisades ja kahekordistades punkte, rakendades oma privaatvõtit "b" Alice'i avalikule võtmele "A":

> S = b·A

- Bob määrab pimestamisteguri "f", mis võimaldab tal lahti krüpteerida Alice'i maksekoodi andmeploki. Samamoodi nagu Alice seda varem arvutas, leiab Bob "f", rakendades HMAC-SHA512 (x) saladuspunkti "S" x-koordinaadi väärtusele ja (o) selles teavitustransaktsioonis sisendina tarbitud UTXO-le:

> f = HMAC-SHA512(o, x)

4. Bob tõlgendab teavitustransaktsiooni OP_RETURN andmeid maksekoodina. Ta lihtsalt dekrüpteerib selle võimaliku maksekoodi andmeploki pimestamisteguri "f" abil.

- Bob jagab pimestamisteguri "f" kaheks osaks: "f" esimesed 32 baiti on "f1" ja viimased 32 baiti on "f2".
- Bob dekrüpteerib Alice'i maksekoodi avaliku võtme krüpteeritud x-koordinaadi väärtuse (x'):

> x = x' XOR f1

- Bob dekrüpteerib Alice'i maksekoodi krüpteeritud ahelakoodi väärtuse (c'):

> c = c' XOR f2

5. Bob kontrollib, kas Alice'i maksekoodi avaliku võtme väärtus kuulub secp256k1 gruppi. Kui see kuulub, tõlgendab ta seda kehtiva maksekoodina. Vastasel juhul ignoreerib ta tehingut.

Nüüd, kui Bob teab Alice'i maksekoodi, saab ta talle saata kuni 2^32 makset, ilma et oleks kunagi vaja teha sellist teavitustransaktsiooni uuesti.

Miks see töötab? Kuidas saab Bob kindlaks määrata sama pimestamisteguri nagu Alice ja dekrüpteerida tema maksekoodi? Vaatleme ECDH protsessi üksikasjalikumalt, põhinedes sellel, mida me just kirjeldasime.
Esmalt tegeleme sümmeetrilise krüpteerimisega. See tähendab, et krüpteerimisvõti ja dekrüpteerimisvõti on sama väärtusega. Sel juhul on teavitustransaktsiooni võti pimestamistegur (f = f1 || f2). Alice'il ja Bob'il on vaja saada sama väärtus f ilma seda otseselt edastamata, kuna ründaja võiks selle pealt kuulata ja salajase informatsiooni dekrüpteerida.
See pimestamistegur saadakse, rakendades HMAC-SHA512 kahele väärtusele: salajase punkti x-koordinaat ja transaktsiooni sisendis tarbitud UTXO. Seega peab Bobil olema need kaks teavet, et dekrüpteerida Alice'i maksekoodi koormat.

Sisend-UTXO puhul saab Bob selle lihtsalt kätte, jälgides teavitustransaktsiooni. Salajase punkti jaoks peab Bob kasutama ECDH-d.

Nagu Diffie-Hellmani jaotises nägime, vahetades omavahel avalikke võtmeid ja salaja rakendades oma privaatvõtmeid teise avalikule võtmele, suudavad Alice ja Bob leida spetsiifilise ja salajase punkti elliptilisel kõveral. Teavitustransaktsioon tugineb sellele mehhanismile:

> Bobi võtmepaar:
>
> B = b·G
>
> Alice'i võtmepaar:
>
> A = a·G
>
> Salajase punkti S (x,y) jaoks:
>
> S = a·B = a·b·G = b·a·G = b·A

![Diagramm jagatud saladuse genereerimisest ECDHE abil](assets/19.webp)
Nüüd, kui Bob teab Alice'i maksekoodi, suudab ta tuvastada tema BIP47 makseid ja tuletada privaatvõtmed, mis blokeerivad saadud bitcoine.
![Bob tõlgendab Alice'i teavitustransaktsiooni](assets/20.webp)

Autor: Reusable Payment Codes for Hierarchical Deterministic Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Kui me võrdleme seda diagrammi sellega, mida ma teile varem kirjeldasin:

- "Wallet Pub-Key" Alice'i poolel vastab: A.

- "Child Priv-Key 0" Bobi poolel vastab: b.

- "Notification Shared Secret" vastab: f.

- "Masked Payment Code" vastab Alice'i maskeeritud maksekoodile, st krüpteeritud koormale: x' ja c'.

- "Notification Transaction" on tehing, mis sisaldab OP_RETURN-i.

Lubage mul kokku võtta sammud, mida me just koos vaatasime, et vastu võtta ja tõlgendada teavitustransaktsiooni:

- Bob jälgib tehinguväljundeid oma teavitusaadressil.

- Kui ta tuvastab ühe, taastab ta OP_RETURN-is sisalduva teabe.

- Bob valib sisendi avaliku võtme ja arvutab salajase punkti, kasutades ECDH-d.

- Ta kasutab seda salajast punkti, et arvutada HMAC, mis on pimestamistegur.

- Ta kasutab seda pimestamistegurit, et dekrüpteerida Alice'i maksekoodi koormat, mis sisaldub OP_RETURN-is.

### BIP47 maksetehing.

Vaadelgem nüüd makseprotsessi BIP47-ga. Meenutamaks teile praegust olukorda:

- Alice teab Bobi maksekoodi, mille ta lihtsalt võttis tema veebisaidilt.

- Bob teab Alice'i maksekoodi tänu teavitustransaktsioonile.

- Alice teeb Bobile esialgse makse. Ta saab teha palju rohkem samal viisil.

Enne selle protsessi selgitamist pean teile meelde tuletama, milliste indeksitega me praegu töötame:

Maksekoodi tuletamise teed kirjeldame järgmiselt: m/47'/0'/0'/.

Järgmine sügavus jaotab indeksid järgmiselt:
- Esimene tavaline (mitte-kõvastunud) lapsepaar kasutatakse teavitusaadressi genereerimiseks, millest me eelmises jaotises rääkisime: m/47'/0'/0'/0/.
- Tavalisi lapse võtmepaare kasutatakse ECDH protokollis BIP47 maksevastuvõtu aadresside genereerimiseks, nagu me selles jaotises näeme: m/47'/0'/0'/ alates 0 kuni 2,147,483,647/.

- Kõvastunud lapse võtmepaarid on ajutised maksekoodid: m/47'/0'/0'/ alates 0' kuni 2,147,483,647'/.
  Iga kord, kui Alice soovib Bobile makset saata, genereerib ta uue unikaalse tühja aadressi, taas tänu ECDH protokollile:
- Alice valib esimese privaatvõtme, mis on tuletatud tema isiklikust korduvkasutatavast maksekoodist:

> a

- Alice valib esimese kasutamata avaliku võtme, mis on tuletatud Bobi maksekoodist. Seda avalikku võtit nimetame "B"-ks. See on seotud privaatvõtmega "b", mida teab ainult Bob.

> B = b·G

- Alice arvutab elliptilisel kõveral salajase punkti "S", lisades ja kahekordistades punkte, rakendades oma privaatvõtit "a" Bobi avalikule võtmele "B":

> S = a·B

- Sellest salajasest punktist arvutab Alice jagatud salajase "s" (väiketähtedega). Selleks valib ta salajase punkti "S" x-koordinaadi, mida nimetatakse "Sx", ja sisestab selle väärtuse SHA256 räsifunktsiooni.

> s = SHA256(Sx)

Ära usalda. Kontrolli! Kui soovid mõista räsifunktsiooni põhiprintsiipe, leiad vajaliku sellest artiklist. Ja kui sa ei usalda NIST-i (õigesti teed), ning soovid üksikasjalikult mõista, kuidas SHA256 töötab, selgitan kõike sellest artiklist prantsuse keeles.

- Alice kasutab seda jagatud salajast "s", et arvutada Bitcoin'i maksevastuvõtu aadress. Esiteks kontrollib ta, kas "s" on secp256k1 kõvera järjekorras. Kui ei, siis suurendab ta Bobi avaliku võtme indeksit, et tuletada teine jagatud salajane.

- Teiseks arvutab ta avaliku võtme "K0", lisades punktid "B" ja "s·G" elliptilisel kõveral. Teisisõnu, Alice lisab avaliku võtme, mis on tuletatud Bobi maksekoodist "B", teise punktiga, mis on arvutatud elliptilisel kõveral, lisades ja kahekordistades punkte jagatud salajase "s" abil secp256k1 kõvera generaatorpunktist "G". See uus punkt esindab avalikku võtit ja me nimetame seda "K0":

> K0 = B + s·G

- Selle avaliku võtmega "K0" saab Alice tuletada tühja vastuvõtu aadressi standardviisil (näiteks SegWit V0 Bech32-s).

Kui Alicel on see vastuvõtu aadress "K0", mis kuulub Bobile, saab ta koostada standardse Bitcoin'i tehingu, valides UTXO, mis kuulub talle teisel harul tema HD rahakotis, ja kulutades selle Bobi "K0" aadressile.

![Alice saadab bitcoine BIP47 abil Bobile](assets/21.webp)

Autor: Korduvkasutatavad Maksekoodid Hierarhilistele Deterministlikele Rahakottidele, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki
Kui me võrdleme seda diagrammi sellega, mida ma teile varem kirjeldasin:

- "Child Priv-Key" Alice'i poolel vastab: a.
- "Child Pub-Key 0" Bobi poolel vastab: B.
- "Payment Secret 0" vastab: s.
- "Makse Avalik Võti 0" vastab: K0.
Lubage mul kokku võtta sammud, mida me just koos läbisime, et saata BIP47 makse:

- Alice valib oma isiklikust maksekoodist esimese tuletatud lapse privaatvõtme.
- Ta arvutab elliptilisel kõveral salajase punkti, kasutades ECDH-d Bobi maksekoodist esimesest kasutamata tuletatud lapse avalikust võtmest.
- Ta kasutab seda salajast punkti, et arvutada jagatud salajane SHA256 abil.
- Ta kasutab seda jagatud salajast, et arvutada elliptilisel kõveral uus salajane punkt.
- Ta lisab selle uue salajase punkti Bobi avalikule võtmele.
- Ta saab uue efemeerse avaliku võtme, millele ainult Bobil on vastav privaatvõti.
- Alice saab saata Bobile tavalise tehingu tuletatud efemeerse vastuvõtu aadressiga.

Kui ta soovib teha teise makse, kordab ta ülaltoodud samme, välja arvatud see, et ta valib Bobi maksekoodist teise tuletatud avaliku võtme. See tähendab järgmist kasutamata võtit. Ta saab siis teise vastuvõtu aadressi, mis kuulub Bobile, "K1".

![Alice tuletatud kolm BIP47 vastuvõtu aadressi Bobile](assets/22.webp)

Autor: Reusable Payment Codes for Hierarchical Deterministic Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Ta võib jätkata samamoodi ja tuletada kuni 2^32 tühja aadressi, mis kuuluvad Bobile.

Välisest perspektiivist, vaadeldes Bitcoin'i plokiahelat, on teoreetiliselt võimatu eristada BIP47 makset tavalisest maksest. Siin on näide BIP47 maksetehingust Testnetis:

https://blockstream.info/testnet/tx/94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254

TXID:

> 94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254

See näeb välja nagu tavaline tehing, millel on kulutatud sisend, makse väljund 210,000 satsi ja vahetus.

![Bitcoin'i maksetehing BIP47-ga](assets/23.webp)

Autor: https://blockstream.info/

### BIP47 makse vastuvõtmine ja privaatvõtme tuletamine.

Alice on just teinud oma esimese makse tühjale BIP47 aadressile, mille omanik on Bob. Vaatame nüüd, kuidas Bob seda makset vastu võtab. Samuti näeme, miks Alice'il ei ole juurdepääsu aadressi genereerinud privaatvõtmele ja kuidas Bob taastab selle võtme, et kulutada just saadud bitcoine.

Niipea kui Bob saab Alicelt teavitustehingu, tuletatakse BIP47 avalik võti "K0" isegi enne, kui ta saadab sellele makse. Seega jälgib ta igasugust makset seotud aadressile. Tegelikult tuletatakse kohe mitu aadressi, mida ta jälgib (K0, K1, K2, K3...). Siin on, kuidas ta tuletatakse seda avalikku võtit "K0":

- Bob valib oma maksekoodist esimese tuletatud lapse privaatvõtme. Seda privaatvõtit nimetatakse "b". See on seotud avaliku võtmega "B", mida Alice kasutas eelmises sammus:

> b

- Bob valib Alice'i maksekoodist esimese tuletatud avaliku võtme. Seda võtit nimetatakse "A". See on seotud privaatvõtmega "a", mida Alice kasutas oma arvutustes ja millest ainult Alice on teadlik. Bob saab seda protsessi teostada, kuna ta teab Alice'i maksekoodi, mis edastati talle teavitustehinguga.

> A = a·G
- Bob arvutab salajase punkti "S", liites ja kahekordistades punkte elliptilisel kõveral, rakendades oma privaatvõtit "b" Alice'i avalikule võtmele "A". Siin kasutame ECDH-d, mis tagab, et see punkt "S" on sama nii Bobi kui ka Alice'i jaoks.
> S = b·A

- Nagu Alice tegi, eraldab Bob selle punkti "S" x-koordinaadi. Oleme selle väärtuse nimetanud "Sx"-ks. Ta läbib selle väärtuse SHA256 funktsiooni, et leida jagatud saladus "s" (väiketähtedega).

> s = SHA256(Sx)

- Samamoodi nagu Alice, arvutab Bob punkti "s·G" elliptilisel kõveral. Seejärel lisab ta selle salajase punkti oma avalikule võtmele "B". Ta saab elliptilisel kõveral uue punkti, mida ta tõlgendab avaliku võtmena "K0":

> K0 = B + s·G

Kui Bobil on see avalik võti "K0", saab ta tuletada seotud privaatvõtme, et kulutada oma bitcoine. Ainult tema saab seda numbrit genereerida.

- Bob lisab oma tuletatud lapse privaatvõtme "b" oma isiklikust maksekoodist. Ainult tema saab saada "b" väärtuse. Seejärel lisab ta "b" jagatud saladusele "s", et saada k0, K0 privaatvõti:

> k0 = b + s
> Tänu elliptilise kõvera grupiseadusele saab Bob täpselt privaatvõtme, mis vastab Alice'i poolt kasutatud avalikule võtmele. Nii meil on:
> K0 = k0·G

![Bob genereerib oma BIP47 vastuvõtu aadressid](assets/24.webp)

Autoriõigus: Taaskasutatavad Maksekoodid Hierarhiliste Deterministlike Rahakottide jaoks, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Kui me võrdleme seda diagrammi sellega, mida ma teile varem kirjeldasin:

- "Child Priv-Key 0" Bobi poolel vastab: b.

- "Child Pub-Key 0" Alice'i poolel vastab: A.

- "Payment Secret 0" vastab: s.

- "Payment Pub-Key 0" vastab: K0.

- "Payment Priv-Key 0" vastab: k0.

Lubage mul kokku võtta sammud, mida me just koos nägime, et vastu võtta BIP47 makse ja arvutada vastav privaatvõti:

- Bob valib esimese tuletatud lapse privaatvõtme oma isiklikust maksekoodist.

- Ta arvutab salajase punkti elliptilisel kõveral, kasutades ECDH-d esimesest tuletatud lapse avalikust võtmest Alice'i ahelakoodist.

- Ta kasutab seda salajast punkti, et arvutada jagatud saladus SHA256-ga.

- Ta kasutab seda jagatud saladust, et arvutada uus salajane punkt elliptilisel kõveral.

- Ta lisab selle uue salajase punkti oma isiklikule avalikule võtmele.

- Ta saab uue efemeerse avaliku võtme, millele Alice saadab oma esimese makse.

- Bob arvutab selle efemeerse avaliku võtme seotud privaatvõtme, lisades oma tuletatud lapse privaatvõtme oma maksekoodist ja jagatud saladuse.

Kuna Alice ei saa saada "b", Bobi privaatvõtit, ei suuda ta kindlaks teha k0, privaatvõtit, mis on seotud Bobi BIP47 vastuvõtu aadressiga.

Skeemiliselt saame esitada jagatud saladuse "S" arvutamise järgmiselt:

![Jagatud saladuse arvutamine ECDHE-ga](assets/25.webp)

Kui jagatud saladus on ECDH abil leitud, arvutavad Alice ja Bob BIP47 makse avaliku võtme "K0" ning Bob arvutab ka seotud privaatvõtme "k0":
![BIP47 vastuvõtu aadressi tuletamine jagatud saladusest](assets/26.webp)
### BIP47 makse tagastamine.

Kuna Bob teab Alice'i korduvkasutatavat maksekoodi, on tal juba kõik vajalik teave, et saata talle tagasimakse. Ta ei pea Alice'ilt lisainformatsiooni küsimiseks temaga ühendust võtma. Ta lihtsalt teavitab teda teavitustransaktsiooniga, eriti selleks, et ta saaks oma BIP47 aadressid oma seemne abil taastada, ja siis saab ta talle saata kuni 2^32 makset.
Bob saab seejärel tagastada Alice'ile makse samal viisil, nagu ta talle makseid saatis. Rollid on vahetunud:

![Bob saadab Alice'ile tagasimakse BIP47 abil](assets/27.webp)

Autor: Korduvkasutatavad Maksekoodid Hierarhiliste Deterministlike Rahakottide jaoks, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Nüüd teate kõiki detaile sellest suurepärasest lahendusest, mida BIP47 esindab.

## PayNymi tuletatud kasutusalad.

Selle BIP47 rakendamine Samourai Wallet'is on toonud kaasa PayNymid, identifikaatorid, mis on arvutatud kasutajate maksekoodidest. Täna ulatub nende kasulikkus kaugemale BIP47 kasutamisest.

Samourai meeskond arendab järk-järgult terve ökosüsteemi tööriistu ja teenuseid, mis põhinevad kasutaja PayNymil. Nende hulgas on ilmselgelt kõik kulutamise tööriistad, mis võimaldavad optimeerida kasutaja privaatsust, lisades tehingule entroopiat ja seeläbi usutavat eitamist.

Sorobani, Toril põhineva krüpteeritud suhtlusvõrgustiku, ja PayNymide ühine kasutamine on oluliselt optimeerinud kasutajakogemust koostööpõhiste tehingute loomisel, säilitades samal ajal hea turvalisuse taseme. Seega on lihtne teostada Stowaway (PayJoin) ja StonewallX2 tehinguid ilma käsitsi paljude allkirjastamata tehingute vahetamist nõudmata, mis on vajalik sellise koostööpõhise tehingu seadistamiseks.

Erinevalt BIP47 kasutamisest, kuna need koostööpõhised tehingud ei nõua teavitustransaktsiooni, piisab PayNymide ühendamisest nende tööriistade kasutamiseks. Pole vaja neid ühendada.

Kui soovite rohkem teada saada koostööpõhistest tehingutest ja laiemalt kõigist Samourai Wallet'i kulutamise tööriistadest, võite lugeda jaotist "Spending Tools" selles artiklis. Leiate tehnilise selgituse ja iga tööriista üksikasjaliku õpetuse.

Lisaks nendele koostööpõhistele tehingutele on hiljuti täheldatud, et Samourai meeskond töötab PayNymiga seotud autentimisprotokolli kallal: Auth47. See tööriist on juba rakendatud ja võimaldab näiteks autentimist PayNymiga veebisaidil, mis aktsepteerib seda meetodit. Tulevikus arvan, et lisaks sellele autentimise võimalusele veebis, saab Auth47 osaks suuremast projektist ümber BIP47/PayNym/Samourai ökosüsteemi. Võib-olla kasutatakse seda protokolli Samourai Wallet'i kasutajakogemuse edasiseks optimeerimiseks, eriti kulutamise tööriistade kasutamisel. Jääb näha...

## Minu isiklik arvamus BIP47 kohta.

Ilmselgelt on BIP47 peamine puudus teavitustransaktsioon. See sunnib kasutajat kulutama tasusid selle kaevandamiseks, mis võib mõne jaoks olla tüütu. Siiski on Bitcoin'i plokiahelas "spämmi" argument täiesti vastuvõetamatu. Igaüks, kes maksab oma tehingu eest tasud, peab saama selle pearaamatusse kanda, olenemata selle eesmärgist. Vastasel juhul pooldatakse tsensuuri.

On võimalik, et tulevikus leitakse teisi vähem kulukaid lahendusi saatja maksekoodi teatamiseks saajale ja saaja turvaliseks hoidmiseks. Kuid praegu on teavitustransaktsioon lahendus, mis nõuab kõige vähem kompromisse.
See puudus jääb tühiseks, kui arvestada kõiki BIP47 eeliseid. Kõigi olemasolevate ettepanekute seas, mis lahendavad aadresside korduvkasutuse probleemi, tundub see mulle parima lahendusena. Nagu varem selgitatud, tuleb enamik aadresside korduvkasutusest vahetusteenustest. BIP47 on ainus mõistlik lahendus, mis tegelikult lahendab selle probleemi selle allikas. Iga ettepanek, mille eesmärk on vähendada aadresside korduvkasutuse arvu, peaks keskenduma sellele aspektile ja kohandama lahendust probleemi peamise allikaga.

Kasutatavuse osas, kuigi selle sisemine töö on üsna keeruline, on BIP47 makseprotseduur lihtne. Seega saavad korduvkasutatavad maksekoodid hõlpsasti omaks võetud isegi algajate kasutajate poolt.

Privaatsuse osas on BIP47 väga huvitav. Nagu ma selgitasin teates tehingu jaotises, ei avalda maksekood mingit teavet tuletatud ajutiste aadresside kohta. Seega katkestab see teabevoogu Bitcoini tehingu ja saaja identifikaatori vahel, erinevalt traditsioonilisest vastuvõtva aadressi kasutamisest.

Ja mis kõige tähtsam, BIP47 PayNym rakendus töötab! See on olnud saadaval Samourai Wallet'is alates 2016. aastast ja Sparrow Wallet'is selle aasta algusest. See ei ole teadusprojekt, vaid lahendus, mis oli eile testitud ja on täna täielikult funktsionaalne.

Loodetavasti võetakse tulevikus need korduvkasutatavad maksekoodid ökosüsteemi osalejate poolt omaks, rakendatakse rahakotitarkvaras ja kasutavad Bitcoinereid.

Iga tõeliselt positiivne lahendus kasutaja privaatsuse jaoks peab olema arutatud, edendatud ja kaitstud, et Bitcoin ei muutuks CA-de mänguväljakuks ja valitsuste järelevalvevahendiks.
Ta mõtles sellele, kuidas teda oli igal pool taga kiusatud ja solvatud, ja nüüd kuulis ta kõiki ütlemas, et ta oli kõige kaunim kõigist neist kaunitest lindudest! Ja isegi pihlakas kummardas oma oksi tema poole, ja päike levitas nii sooja ja heatahtlikku valgust! Siis paisusid tema suled, tema sale kael sirgus, ja ta hüüdis kogu südamest: "Kuidas ma oleksin osanud unistada nii suurest õnnest, kui olin vaid inetu väike pardipoeg."

## Edasi minemiseks:

- Mõistmine ja CoinJoin'i kasutamine Bitcoinis.

- Bitcoin rahakoti tuletamisteede mõistmine.

- Oma RoninDojo Bitcoin sõlme paigaldamine ja kasutamine.

### Välised ressursid ja tänusõnad:

Tänu LaurentMT-le ja Théo Pantamis'ele paljude kontseptsioonide eest, mida nad mulle selgitasid ja mida ma selles artiklis kasutasin. Loodan, et olen neid täpselt edasi andnud.

Tänu Fanis Michalakis'ele selle teksti toimetamise ja tema eksperdinõu eest.

- https://bitcoiner.guide/paynym/
- https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman_bas%C3%A9_sur_les_courbes_elliptiques
- https://security.stackexchange.com/questions/46802/what-is-the-difference-between-dhe-and-ecdh#:~:text=The%20difference%20between%20DHE%20and%20ECDH%20in%20two%20bullet%20points,a%20type%20of%20algebraic%20curve).
- https://commandlinefanatic.com/cgi-bin/showarticle.cgi?article=art060
- https://ee.stanford.edu/~hellman/publications/24.pdf
- https://www.researchgate.net/publication/317339928_A_study_on_diffie-hellman_key_exchange_protocols