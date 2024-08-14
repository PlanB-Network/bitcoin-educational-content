---
name: Teoreetiline sissejuhatus Lightning Network'i
goal: Avastada Lightning Network'i tehnilisest perspektiivist
objectives:
  - Mõista võrgu kanalite toimimist.
  - Tutvuda terminitega nagu HTLC, LNURL ja UTXO.
  - Omandada teadmised LNN-i likviidsuse ja tasude haldamisest.
  - Tunnustada Lightning Network'i kui võrku.
  - Mõista Lightning Network'i teoreetilisi kasutusvõimalusi.
---

# Teekond Bitcoin'i teise kihti

See kursus on teoreetiline õppetund Lightning Network'i tehnilisest toimimisest.

Tere tulemast põnevasse Lightning Network'i maailma, mis on Bitcoin'i teine kiht ja mis on nii keerukas kui ka täis potentsiaali. Me oleme valmis sukelduma selle tehnoloogia tehnilistesse sügavustesse, keskendudes mitte konkreetsetele õpetustele või kasutusstsenaariumitele. Selle kursuse maksimaalseks kasutamiseks on hädavajalik hea arusaam Bitcoin'ist. See on kogemus, mis nõuab tõsist ja keskendunud lähenemist. Võite kaaluda ka LN 202 kursuse paralleelset läbimist, mis pakub sellele uurimisele praktilisemat aspekti. Valmistuge teekonnaks, mis võib muuta teie arusaama Bitcoin'i ökosüsteemist.

Nautige avastamist!

+++

# Alustalad
<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>

## Lightning Network'i mõistmine
<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>

Lightning Network on teise kihi makseinfrastruktuur, mis on ehitatud Bitcoin'i võrgu peale ja võimaldab kiireid ning madala maksumusega tehinguid. Lightning Network'i toimimise täielikuks mõistmiseks on oluline mõista, mis on maksekanalid ja kuidas need toimivad.

Lightning maksekanal on omamoodi "privaatne rada" kahe kasutaja vahel, mis võimaldab kiireid ja korduvaid Bitcoin'i tehinguid. Kui kanal avatakse, määratakse sellele fikseeritud maht, mis on ette määratud kasutajate poolt. See maht esindab maksimaalset summat Bitcoin'is, mida kanalis igal hetkel edastada saab.

Maksekanalid on kahepoolse suunaga, mis tähendab, et neil on kaks "poolt". Näiteks, kui Alice ja Bob avavad maksekanali, saab Alice saata Bitcoin'e Bobile ja Bob saata Bitcoin'e Alice'ile. Tehingud kanali sees ei muuda kanali kogumahtu, kuid need muudavad selle mahtu jaotust Alice'i ja Bob'i vahel.

![selgitus](assets/chapitre1/0.webp)

Et tehing oleks Lightning maksekanalis võimalik, peab raha saatval kasutajal olema piisavalt Bitcoin'e oma kanali poolel. Kui Alice soovib saata 1 Bitcoin'i Bobile läbi nende kanali, peab tal olema vähemalt 1 Bitcoin oma kanali poolel.
Piirangud ja maksekanalite toimimine Lightning'is.
Kuigi Lightning maksekanali maht on fikseeritud, ei piira see koguarvu tehinguid ega Bitcoin'i kogumahtu, mida kanali kaudu edastada saab. Näiteks, kui Alice'il ja Bob'il on kanal mahuga 1 Bitcoin, saavad nad teha sadu 0.01 Bitcoin'i tehinguid või tuhandeid 0.001 Bitcoin'i tehinguid, seni kuni kanali kogumaht ei ületa ühelgi hetkel.

Hoolimata nendest piirangutest on Lightning maksekanalid tõhus viis kiirete ja odavate Bitcoin'i tehingute sooritamiseks. Need võimaldavad kasutajatel saata ja vastu võtta Bitcoin'e ilma, et peaksid maksma kõrgeid tehingutasusid või ootama pikki kinnitamisperioode Bitcoin'i võrgus.
Kokkuvõttes pakuvad Lightningi maksekanalid võimsat lahendust neile, kes soovivad teostada kiireid ja soodsaid Bitcoin'i tehinguid. Siiski on oluline mõista nende toimimist ja piiranguid, et neist täielikult kasu saada.
![explication](assets/chapitre1/1.webp)

Näide:

- Alicel on 100,000 SAT
- Bobil on 30,000 SAT

See on kanali praegune seisund. Tehingu ajal otsustab Alice saata Bobile 40,000 SAT. Ta saab seda teha, kuna 40,000 < 100,000.

Seega on kanali uus seisund:

- Alice 60,000 SAT
- Bob 70,000 SAT

```
Kanali algseisund:
Alice (100,000 SAT) ============== Bob (30,000 SAT)

Pärast Alice'i ülekannet Bobile 40,000 SAT:
Alice (60,000 SAT) ============== Bob (70,000 SAT)

```
![explication](assets/chapitre1/2.webp)

Nüüd soovib Bob saata Alicele 80,000 SAT. Kuna tal ei ole piisavalt likviidsust, ei saa ta seda teha. Kanali maksimaalne maht on 130,000 SAT, võimaliku kulutusega kuni 60,000 SAT Alicel ja 70,000 SAT Bobil.

![explication](assets/chapitre1/3.webp)

## Bitcoin, aadressid, UTXO ja tehingud
<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>

Teises peatükis võtame aega, et uurida, kuidas Bitcoin'i tehingud tegelikult toimivad, mis on väga kasulik Lightningi mõistmiseks. Samuti arutame lühidalt mitme allkirjaga aadresside kontseptsiooni, mis on oluline järgmise peatüki mõistmiseks Lightningi võrgus kanalite avamisel.

- Privaatvõti > Avalik võti > Aadress: Tehingu ajal saadab Alice raha Bobile. Viimane annab aadressi, mille ta sai oma avaliku võtme kaudu. Alice, kes ise sai raha aadressil oma avaliku võtme kaudu, kasutab nüüd oma privaatvõtit tehingu allkirjastamiseks ja seeläbi bitcoinide aadressilt vabastamiseks.
- Bitcoin'i tehingus peavad kõik bitcoinid liikuma. Nimetatud UTXO (Unspend Transaction Output), bitcoinide killud lahkuvad kõik ainult selleks, et hiljem omaniku juurde tagasi pöörduda.
  Alicel on 0.002 BTC, Bobil on 0 BTC. Alice otsustab saata Bobile 0.0015 BTC. Ta allkirjastab 0.002 BTC suuruse tehingu, kus 0.0015 läheb Bobile ja 0.0005 naaseb tema rahakotti.

![explication](assets/chapitre2/0.webp)

Siin, ühest UTXOst (Alicel on aadressil 0.0002 BTC), oleme loonud 2 UTXOt (Bobil on 0.0015 ja Alicel on uus UTXO (sõltumatu eelmisest) 0.0005 BTC).

```
Alice (0.002 BTC)
  |
  V
Bitcoin'i tehing (0.002 BTC)
  |
  |----> Bob (0.0015 BTC)
  |
  V
Alice (uus UTXO: 0.0005 BTC)
```
Lightning Network'is kasutatakse mitme allkirjaga tehinguid. Seega on vahendite vabastamiseks vajalikud 2 allkirja, st kaks privaatvõtit raha liigutamiseks. See võib olla Alice ja Bob, kes peavad koos nõustuma raha vabastamisega (UTXO). LN-is on need spetsiifiliselt 2/2 tehingud, nii et mõlemad allkirjad on absoluutselt vajalikud, erinevalt 2/3 või 3/5 mitme allkirjaga tehingutest, kus on vajalik ainult võtmete täieliku arvu kombinatsioon.
![selgitus](assets/chapitre2/1.webp)

# Kanalite avamine ja sulgemine
<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>

## Kanali avamine
<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>

Nüüd vaatame lähemalt, kuidas kanalit avatakse ja kuidas see toimub Bitcoin'i tehingu kaudu.

Lightning Network'il on erinevad suhtlustasandid:

- P2P suhtlus (Lightning Network protokoll)
- Maksekanal (Lightning Network protokoll)
- Bitcoin tehing (Bitcoin protokoll)

![selgitus](assets/chapitre3/0.webp)

Kanali avamiseks suhtlevad kaks osapoolt suhtluskanali kaudu:

- Alice: "Tere, ma tahan kanalit avada!"
- Bob: "Olgu, siin on minu avalik aadress."

![selgitus](assets/chapitre3/1.webp)

Alicel on nüüd 2 avalikku aadressi, et luua 2/2 mitme allkirjaga aadress. Ta saab nüüd teha bitcoin'i tehingu, et saata sinna raha.

Oletame, et Alicel on 0.002 BTC UTXO ja ta tahab avada kanali Bobiga 0.0013 BTC ulatuses. Ta loob tehingu kahe UTXO väljundiga:

- 0.0013 UTXO 2/2 mitme allkirjaga aadressile
- 0.0007 UTXO ühele oma vahetusaadressidest (UTXOde tagastus).

See tehing ei ole veel avalik, sest kui see selles etapis on, usaldab ta Bobi, et see suudab mitme allkirjaga aadressilt raha vabastada.

Aga kuidas edasi minna?

Alice loob teise tehingu, mida nimetatakse "väljavõtte tehinguks", enne mitme allkirjaga aadressile fondide sissemakse avaldamist.

![selgitus](assets/chapitre3/2.webp)

Väljavõtte tehing kulutab vahendid mitme allkirjaga aadressilt ühele tema enda aadressile (see tehakse enne kõige avaldamist).
Kui mõlemad tehingud on loodud, teatab Alice Bobile, et see on tehtud, ja küsib temalt allkirja oma avaliku võtmega, selgitades, et nii saab ta oma vahendid tagasi, kui midagi peaks valesti minema. Bob nõustub, kuna ta ei ole ebaaus.

Alice saab nüüd vahendid üksi tagasi, kuna tal on juba Bobi allkiri. Ta avaldab tehingud. Kanal on nüüd avatud 0.0013 BTC (130,000 SAT) Alici poolel.

![selgitus](assets/chapitre3/3.webp)

## Lightning Tehing & Kohustuse Tehing
<chapterId>7d3fd135-129d-5c5a-b306-d5f2f1e63340</chapterId>

![kaas](assets/chapitre4/1.webp)
Nüüd analüüsime, mis tegelikult toimub kulisside taga, kui Lightning Network'is kanali ühelt poolt teisele vahendeid üle kantakse, kasutades kohustusliku tehingu (commitment transaction) mõistet. Ahelasisene väljamakse/sulgemistehing esindab kanali seisundit, tagades, kes omab vahendeid pärast iga ülekannet. Seega pärast Lightning Network'i ülekannet toimub selle tehingu/lepingu uuendus, mida ei teostata kahe osapoole, Alice'i ja Bobi vahel, kes loovad sulgemise korral sama tehingu praeguse kanali seisundiga:
- Alice avab kanali Bobiga, omades oma poolel 130 000 SAT-i. Mõlemad nõustuvad sulgemise korral väljamaksetehinguga, mis näeb ette, et 130 000 SAT läheb Alice'ile ja Bob nõustub, sest see on õiglane.

![cover](assets/chapitre4/2.webp)

- Alice saadab Bobile 30 000 SAT-i. Nüüd on olemas uus väljamaksetehing, mis näitab, et sulgemise korral saab Alice 100 000 SAT-i ja Bob 30 000 SAT-i. Mõlemad nõustuvad, sest see on õiglane.

![cover](assets/chapitre4/3.webp)

- Alice saadab Bobile 10 000 SAT-i ja luuakse uus väljamaksetehing, mis näitab, et Alice saab sulgemise korral 90 000 SAT-i ja Bob 40 000 SAT-i. Mõlemad nõustuvad, sest see on õiglane.

![cover](assets/chapitre4/4.webp)


```
Kanali algseisund:
Alice (130,000 SAT) =============== Bob (0 SAT)

Pärast esimest ülekannet:
Alice (100,000 SAT) =============== Bob (30,000 SAT)

Pärast teist ülekannet:
Alice (90,000 SAT) =============== Bob (40,000 SAT)

```

Raha ei liigu tegelikult, kuid lõplik saldo uuendatakse allkirjastatud, kuid avaldamata ahelasisese tehinguga. Seega on väljamaksetehing kohustuslik tehing. Satoshi ülekanded on teine, hilisem kohustuslik tehing, mis uuendab saldot.

## Kohustuslikud Tehingud
<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>

Kui kohustuslikud tehingud määravad kanali seisundi likviidsusega ajahetkel X, kas me saame petta, avaldades vana seisundi? Vastus on jah, sest meil on juba mõlema osaleja eelallkiri avaldamata tehingus.

![instruction](assets/Chapitre5/0.webp)

Selle probleemi lahendamiseks lisame keerukust:

- Ajalukk = vahendid on lukustatud kuni plokini N
- Tühistamisvõti = Alice'i saladus ja Bobi saladus

Need kaks elementi lisatakse kohustuslikule tehingule. Selle tulemusena peab Alice ootama ajaluku lõppu ja igaüks, kes omab tühistamisvõtit, saab vahendeid liigutada ilma ajaluku lõppu ootamata. Kui Alice üritab petta, kasutab Bob tühistamisvõtit, et varastada ja karistada Alice'i.

![instruction](assets/Chapitre5/1.webp)
Nüüd (ja tegelikkuses) ei ole kohustuse tehing Alice'i ja Bobi jaoks sama, need on sümmeetrilised, kuid igaühel erinevate piirangutega, nad annavad teineteisele oma saladuse, et luua eelmise kohustuse tehingu tühistamisvõti. Seega loomisel loob Alice kanali Bobiga, 130 000 SAT tema poolel, tal on Ajalukk, mis takistab tal kohe oma raha tagasi saamast, ta peab natuke ootama. Tühistamisvõti võib raha vabastada, kuid ainult Alicel on see (Alice'i kohustuse tehing). Kui toimub ülekanne, annab Alice oma vana saladuse Bobile ja seega saab viimane kanali eelmisesse olekusse tühjendada, juhul kui Alice üritab petta (Alice on seega karistatud).
![juhis](assets/Chapitre5/2.webp)

Sarnaselt annab Bob oma saladuse Alice'ile. Nii et kui ta üritab petta, saab Alice teda karistada. Operatsiooni korratakse iga uue kohustuse tehingu jaoks. Otsustatakse uus saladus ja uus tühistamisvõti. Seega iga uue tehingu jaoks tuleb eelmine kohustuse tehing hävitada, andes tühistamise saladuse. Nii kui Alice või Bob üritavad petta, saab teine enne tegutseda (tänu Ajalukule) ja seega vältida petmist. Tehingu #3 ajal antakse seega tehingu #2 saladus, et võimaldada Alice'il ja Bobil end kaitsta Alice'i või Bobi vastu.

![juhis](assets/Chapitre5/3.webp)

Isik, kes loob tehingu Ajalukuga (see, kes raha saadab), saab tühistamisvõtit kasutada alles pärast Ajalukku. Siiski, isik, kes raha saab, saab seda kasutada enne Ajalukku, juhul kui ühelt kanali poolelt teisele Lightning Network'is toimub pettus. Eelkõige kirjeldame mehhanisme, mis võimaldavad meil kaitsta võimaliku pettuse eest kanalis oma partneri poolt.

## Kanali Sulgemine
<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>

Me oleme huvitatud kanali sulgemisest läbi Bitcoin'i tehingu, mis võib võtta erinevaid vorme olenevalt juhtumist. On 3 tüüpi kanali sulgemist:

- Hea: koostööalane sulgemine
- Jõhker: sunnitud sulgemine (mittekoostööalane)
- Pettur: sulgemine petturi poolt

![juhis](assets/chapitre6/1.webp)
![juhis](assets/chapitre6/0.webp)


### Hea

Mõlemad osapooled suhtlevad ja nõustuvad kanali sulgema. Nad peatavad kõik tehingud ja valideerivad kanali lõpliku oleku. Nad lepivad kokku võrgutasudes (kanali avanud isik maksab sulgemistasud). Nad loovad nüüd sulgemistehingu. On olemas sulgemistehing, mis erineb kohustuse tehingutest, kuna selles ei ole Ajalukku ega tühistamisvõtit. Tehing avaldatakse ja Alice ning Bob saavad oma vastavad saldod. See sulgemise tüüp on kiire (kuna Ajalukku puudub) ja üldiselt odav.

![juhis](assets/chapitre6/3.webp)


### Jõhker

Alice soovib kanali sulgeda, kuid Bob ei vasta, kuna ta on võrguühenduseta (interneti või elektrikatkestus). Alice avaldab siis kõige uuema kohustuse tehingu (viimase). Tehing avaldatakse ja Ajalukk aktiveeritakse. Siis otsustati tasud, kui see tehing loodi X aega tagasi! MemPool on võrk, mis on sellest ajast alates muutunud, nii et protokoll lähtub tasudest, mis on 5 korda kõrgemad kui praegused, kui tehing loodi. Loomise tasu 10 SAT, nii et tehingut peetakse 50 SAT-ks. Sunnitud sulgemise ajal on võrk:
- 1 SAT = ülemakstud 50\*- 100 SAT = alamakstud 2\*

See muudab sunnitud sulgemise pikemaks (Timelock) ja eriti riskantsemaks seoses tasude ja võimaliku kaevurite poolt valideerimisega.

![juhend](assets/chapitre6/4.webp)

### Pettur

Alice üritab petta, avaldades vana kohustuse tehingu. Kuid Bob jälgib MemPooli ja otsib tehinguid, mis üritavad avaldada vanu. Kui ta leiab mõne, kasutab ta tühistamisvõtit, et Alice karistada ja võtta kogu SAT kanalist.

![juhend](assets/chapitre6/5.webp)

Kokkuvõttes on kanali sulgemine Lightning Networkis oluline samm, mis võib võtta erinevaid vorme. Koostöölises sulgemises suhtlevad mõlemad pooled ja lepivad kokku kanali lõplikus seisundis. See on kiireim ja odavaim variant. Teisest küljest toimub sunnitud sulgemine, kui üks pooltest ei reageeri. See on kallim ja pikem olukord ettearvamatute tehingutasude ja Timelocki aktiveerimise tõttu. Lõpuks, kui osaleja üritab petta, avaldades vana kohustuse tehingu, saab pettur karistada, kaotades kõik SAT kanalist. Seega on oluline mõista neid mehhanisme Lightning Networki tõhusaks ja õiglaseks kasutamiseks.

# Likviidsusvõrk
<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>

## Lightning Network
<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>


Selles seitsmendas peatükis uurime, kuidas Lightning toimib kanalite võrgustikuna ja kuidas makseid suunatakse nende lähtekohast sihtkohta.

![kaas](assets/Chapitre7/0.webp)
![kaas](assets/Chapitre7/1.webp)

Lightning on maksekanalite võrgustik. Tuhandeid eakaaslasi oma likviidsuskanalitega on omavahel ühendatud ja seega kasutavad nad ise tehingute tegemiseks ühendamata eakaaslaste vahel. Nende kanalite likviidsust ei saa üle kanda teistele likviidsuskanalitele.

Alice -> Eden - > Bob`. Satoshi'd ei ole liikunud `Alice -> Bob`, vaid `Alice -> Eden` ja `Eden -> Bob`.

Seega on igal inimesel ja kanalil erinev likviidsus. Maksete tegemiseks peate võrgust leidma marsruudi piisava likviidsusega. Kui piisavalt likviidsust ei ole, siis makse ei toimu.

Kaalu järgmist võrku:

```
Võrgu algseisund:
Alice (130 SAT) ==== (0 SAT) Susie (90 SAT) ==== (200 SAT) Eden (150 SAT) ==== (100 SAT) Bob
```
![kaas](assets/Chapitre7/2.webp)

Kui Alice peab Bobile üle kandma 40 SAT, siis likviidsus jaotatakse ümber kahe osapoole vahelisel marsruudil.

```
Pärast Alice'i 40 SAT ülekannet Bobile:
Alice (90 SAT) ==== (40 SAT) Susie (50 SAT) ==== (240 SAT) Eden (110 SAT) ==== (140 SAT) Bob
```

![kaas](assets/Chapitre7/4.webp)

Siiski algseisundis ei saa Bob saata 40 SAT Alicele, kuna Susiel pole Alicega likviidsust, et saata 40 SAT, seega makse selle marsruudi kaudu ei ole võimalik. Seega on vaja teist marsruuti, kus tehing on võimatu.

Esimeses näites on selge, et Susie ja Eden ei ole kaotanud ega võitnud midagi. Lightning Networki sõlmed küsivad tasu tehingu marsruutimise nõustumise eest!
Erinevad tasud sõltuvad sellest, kus likviidsus asub
Alice - Bob

- Alice'i tasu = Alice -> Bob
- Bobi tasu = Bob -> Alice

![cover](assets/Chapitre7/5.webp)

On kahte tüüpi tasusid:

- fikseeritud tasu sõltumata summast: 1 SAT (vaikimisi, kuid seda saab muuta)
- muutuv tasu (vaikimisi 0.01%)

Tasu näide:

- Alice - Susie; 1/1 (1 fikseeritud tasu ja 1 muutuv tasu)
- Susie - Eden; 0/200
- Eden - Bob; 1/1

Seega:

- Tasu 1: (maksab Alice iseendale) 1 + (40,000\*0.000001)
- Tasu 2: 0 + 40,000 \* 0.0002 = 8 SAT
- Tasu 3: 1 + 40,000\*0.000001 = 0.4 SAT

![cover](assets/Chapitre7/6.webp)

Saatmine:

1. Saadetis 40,009.04 Alice -> Susie; Alice maksab oma kulud, seega seda ei arvestata
2. Susie teeb Edenile teene, saates 40 001.04; ta võtab selle komisjoni 8 SAT
3. Eden teeb teenuse, saates 40,000 Bobile, ta võtab oma 1.04 SAT tasu.

Alice maksis 9.04 SAT tasu ja Bob sai 40,000 SAT.

![cover](assets/Chapitre7/7.webp)

Lightning Network'is on Alice'i sõlm, mis otsustab marsruudi enne makse saatmist. Seega otsitakse parimat marsruuti ja ainult Alice teab marsruuti ja hinda. Makse saadetakse, kuid Susiel pole teavet.

![cover](assets/Chapitre7/9.webp)

Susie või Edeni jaoks: nad ei tea, kes on lõplik saaja ega kes maksab. See on sibulmarsruutimine. Sõlm peab hoidma võrgu plaani, et leida oma marsruut, kuid ükski vahendajatest ei oma teavet.

## HTLC - Hashed Time Locked Contract
<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>

Traditsioonilises marsruutimissüsteemis, kuidas saame tagada, et Eden ei petaks ja austaks oma osa lepingust?

HTLC on makseleping, mida saab avada ainult saladusega. Kui seda ei avalikustata, siis leping aegub. Seega on see tingimuslik makse. Kuidas neid kasutatakse?

![instruction](assets/chapitre8/0.webp)

Kaalu järgmist olukorda:
`Alice (100,000 SAT) ==== (30,000 SAT) Susie (250,000 SAT) ==== (0 SAT) Bob`

- Bob genereerib saladuse S (eelkujutis) ja arvutab räsi r = hash(s)
- Bob saadab Alice'ile arve, milles on "r" kaasatud
- Alice saadab Susiele HTLC 40,000 SAT-ga tingimusel, et avalikustatakse "s'", nii et hash(s') = r
- Susie saadab sarnase HTLC Bobile
- Bob avab Susie HTLC, näidates talle "s"
- Susie avab Alice'i HTLC, näidates talle "S"

Kui Bob on võrguühenduseta ja ei saa kunagi saladust, mis annab talle õiguse raha saada, siis HTLC aegub pärast teatud arvu plokke.
![juhend](assets/chapitre8/1.webp)
HTLC-d aeguvad vastupidises järjekorras: esmalt Susie-Bobi aegumine, seejärel Alice-Susie aegumine. Nii, kui Bob naaseb, ei muutu midagi. Vastasel juhul, kui Alice katkestab samal ajal, kui Bob naaseb, tekib segadus ja inimesed võivad asjata tööd teha.

Niisiis, mis juhtub sulgemise korral? Tegelikult on meie kohustuste tehingud veelgi keerulisemad. Me peame esindama vahebilanssi, kui kanal suletakse.

Seetõttu on kohustuste tehingus HTLC-väljaminek 40 000 satoshi (piirangutega, mida varem nägime) väljundis #3.

![juhend](assets/chapitre8/2.webp)

Alice'il on kohustuste tehingus:

- Väljund #1: 60 000 SAT Alice'ile ajalukustuse ja tühistamisvõtmega (mis jääb tema jaoks alles)
- Väljund #2: 30 000, mis juba kuulub Susiele
- Väljund #3: 40 000 HTLC-s

Alice'i kohustuste tehing on HTLC-väljaminekuga, kuna ta saadab HTLC-sisse Susiele.

![juhend](assets/chapitre8/3.webp)

Seega, kui me avaldame selle kohustuste tehingu, saab Susie HTCL raha kätte "s" pildi abil. Kui tal ei ole eelkujutist, saab Alice raha tagasi, kui HTCL aegub. Mõelge väljunditele (UTXO) kui erinevatele maksetele erinevate tingimustega.
Kui makse on tehtud (aegumine või täitmine), muutub kanali seisund ja tehing HTCL-iga enam ei eksisteeri. Me naaseme tavapärase juurde.
Koostöölise sulgemise korral: me peatame maksed ja seega ootame ülekannete/HTCL täitmist, tehing on kerge, seega vähem kulukas, kuna on maksimaalselt 1 või 2 väljundit.
Sunnitud sulgemise korral: me avaldame kõik käimasolevad HTLC-d, nii et see muutub väga raskeks ja väga kulukaks. Ja see on segadus.

Kokkuvõttes kasutab Lightning Networki marsruutimissüsteem Hash Time-Locked Contracts (HTLC) turvaliste ja kontrollitavate maksete tagamiseks. HTLC-d võimaldavad tingimuslikke makseid, kus raha saab vabastada ainult saladusega, tagades seeläbi, et osalejad täidavad oma kohustusi.
Esitatud näites soovib Alice saata SAT-i Bobile läbi Susie. Bob genereerib saladuse, loob sellest räsi ja edastab selle Alice'ile. Alice ja Susie seadistavad selle räsi põhjal HTLC. Kui Bob avab Susie HTLC, näidates talle saladust, saab Susie seejärel avada Alice'i HTLC.
Juhul, kui Bob ei avalikusta saladust teatud aja jooksul, aegub HTLC. Aegumine toimub vastupidises järjekorras, tagades, et kui Bob tuleb tagasi võrguühendusse, ei ole soovimatuid tagajärgi.

Kanali sulgemisel, kui see on koostööline sulgemine, katkestatakse maksed ja HTLC-d lahendatakse, mis on üldiselt vähem kulukas. Kui sulgemine on sunnitud, avaldatakse kõik käimasolevad HTLC tehingud, mis võivad muutuda väga kulukaks ja segaseks.
Kokkuvõttes lisab HTLC mehhanism Lightning Networkile täiendava turvakihi, tagades, et maksed viiakse õigesti täide ja et kasutajad täidavad oma kohustusi.

## Tee leidmine
<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>

Ainus avalik andmed on kogu kanali maht (Alice + Bob), kuid me ei tea, kus likviidsus asub.
Et saada rohkem teavet, kuulab meie sõlm LN kommunikatsioonikanalit uute kanalite teadaannete ja kanalitasude uuenduste jaoks. Teie sõlm vaatab ka blockchaini kanali sulgemiste jaoks.
Kuna meil ei ole kogu teavet, peame otsima graafi/marsruudi olemasoleva teabega (maksimaalne kanali maht ja mitte kus likviidsus asub).

Kriteeriumid:

- Edu tõenäosus - Tasud
- HTLC aegumisaeg
- Vahepealsete sõlmede arv
- Juhuslikkus

![graafik](assets/chapitre9/1.webp)

Niisiis, kui on 3 võimalikku marsruuti:

- Alice > 1 > 2 > 5 > Bob
- Alice > 1 > 2 > 4 > 5 > Bob
- Alice 1 > 2 > 3 > Bob

Otsime teoreetiliselt parimat marsruuti madalaimate tasude ja kõrgeima eduvõimalusega: maksimaalne likviidsus ja võimalikult vähe hüppeid.

Näiteks, kui 2-3-l on ainult maht 130,000 SAT, on 100,000 saatmine väga ebatõenäoline, seega valikul #3 pole eduvõimalust.

![graafik](assets/chapitre9/2.webp)

Nüüd on algoritm teinud oma 3 valikut ja proovib esimest:

Valik 1:

- Alice saadab HTLC 100,000 SAT 1-le;
- 1 teeb HTLC 100,000 SAT 2-le;
- 2 teeb HTLC 100,000 SAT 5-le, aga 5 ei saa seda teha, seega teatab sellest.

Teave saadetakse tagasi, nii et Alice otsustab proovida teist marsruuti:

- Alice saadab HTLC 100,000 1-le;
- 1 teeb HTLC 100,000 2-le;
- 2 teeb HTLC 100,000 4-le;
- 4 teeb HTLC 100,000 Bobile. Bobil on likviidsus, seega on kõik korras.
- Bob kasutab HTLC eelkujutise (hash) ja seega kasutab saladust, et saada 100,000 SAT
- 5-l on nüüd HTLC saladus, et saada kinni pandud HTLC 4-lt
- 4-l on nüüd HTLC saladus, et saada kinni pandud HTLC 2-lt
- 2-l on nüüd HTLC saladus, et saada kinni pandud HTLC 1-lt
- 1-l on nüüd HTLC saladus, et saada Alice'i kinni pandud HTLC

Alice ei näinud marsruudi 1 ebaõnnestumist, ta lihtsalt ootas ühe sekundi kauem. Makse ebaõnnestumine toimub siis, kui võimalikku marsruuti pole. Marsruudi otsimise hõlbustamiseks võib Bob anda Alice'ile teavet, mis aitab tema arvel:

- Summa
- Tema aadress
- Eelkujutise hash, et Alice saaks luua HTLC
- Viited Bobi kanalitele

Bob teab kanalite 5 ja 3 likviidsust, kuna ta on nendega otseselt ühendatud, ta võib seda Alice'ile näidata. Ta hoiatab Alice'i, et sõlm 3 on kasutu, mis takistab Alice'il potentsiaalselt oma marsruuti tegemast.
Teine element võiksid olla privaatsed kanalid (seega mitte võrgus avaldatud), mida Bobil võib olla. Kui Bobil on privaatne kanal 1-ga, võib ta öelda Alice'ile, et kasutagu seda ja see annaks Alice > 1 > Bob'.

![graafik](assets/chapitre9/3.webp)
Järeldusena võib öelda, et tehingute suunamine Lightning Network'is on keeruline protsess, mis nõuab mitmete tegurite arvesse võtmist. Kuigi kanalite koguvõimsus on avalik, ei ole likviidsuse täpne jaotus otseselt kättesaadav. See sunnib sõlmi hindama kõige tõenäolisemaid edukaid marsruute, võttes arvesse kriteeriume nagu tasud, HTLC aegumistähtaeg, vahesõlmede arv ja juhuslikkuse faktor. Kui mitu marsruuti on võimalik, püüavad sõlmed minimeerida tasusid ja maksimeerida edukuse võimalusi, valides kanalid piisava likviidsuse ja minimaalse hüpete arvuga. Kui tehingu katse ebaõnnestub likviidsuse puudumise tõttu, proovitakse teist marsruuti, kuni tehing õnnestub.
Lisaks, et hõlbustada marsruudi otsingut, võib saaja pakkuda lisateavet, nagu aadress, summa, eelkujutise räsi ja vihjeid oma kanalite kohta. See võib aidata tuvastada piisava likviidsusega kanaleid ja vältida tarbetuid tehingukatseid. Lõppkokkuvõttes on Lightning Network'i marsruutimissüsteem kavandatud tehingute kiiruse, turvalisuse ja efektiivsuse optimeerimiseks, säilitades samal ajal kasutaja privaatsuse.

# Lightning Network'i vahendid
<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>

## Arve, LNURL, Keysend
<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>

![cover](assets/chapitre10/0.webp)

LN arve (või arve) on pikk ja mitte meeldiv lugeda, kuid see võimaldab tihedat esitust makse taotlusest.

Näide:
lnbc1m1pskuawzpp5qeuuva2txazy5g483tuv9pznn9ft8l5e49s5dndj2pqq0ptyn8msdqqcqzpgxqrrsssp5v4s00u579atm0em6eqm9nr7d0vr64z5j2sm5s33x3r9m4lgfdueq9qyyssqxkjzzgx5ef7ez3dks0laxayx4grrw7j22ppgzyhpydtv6hmc39skf9hjxn5yd3kvv7zpjdxd2s7crcnemh2fz26mnr6zu83w0a2fwxcqnvujl3

- lnbc1m = loetav osa
- 1 = eraldus ülejäänust
- Siis ülejäänud
- Bc1 = Bech32 kodeering (base 32), seega kasutatakse 32 tähemärki.
- 10 = 1.2.3.4.5.6.7.8.9.0
- 26 = abcdefghijklmnopqrstuvwxyz
- 32 = ei "b-i-o" ega "1"

### lnbc1m

- ln = Lightning
- Bc = bitcoin (põhivõrk)
- 1 = summa
- M = milli (10^-3 / u = mikro 10^-6 / n = nano 10^-9 / p = piko 10^-12'
  Siin 1m = 1 * 0.0001btc = 100,000 BTC
Palun tasuge 100 000 SAT Lightning võrgus Bitcoin'i põhivõrgus aadressile pskuawzpp5qeuuva2txazy5g483tuv9pznn9ft8l5e49s5dndj2pqq0ptyn8msdqqcqzpgxqrrsssp5v4s00u579atm0em6eqm9nr7d0vr64z5j2sm5s33x3r9m4lgfdueq9qyyssqxkjzzgx5ef7ez3dks0laxayx4grrw7j22ppgzyhpydtv6hmc39skf9hjxn5yd3kvv7zpjdxd2s7crcnemh2fz26mnr6zu83w0a2fwxcqnvujl3
### Ajatempel (millal see loodi)

See sisaldab 0 või rohkem lisandosa:

- Eelkujutise räsi
- Makse saladus (sibulmarsruutimine)
- Suvalised andmed
- Saaja LN avalik võti
- Aegumisaeg (vaikimisi 1 tund)
- Marsruutimisviited
- Kogu arve allkiri

On olemas ka teisi arvetüüpe. LNURL meta-protokoll võimaldab pakkuda otsest satoshi summat, selle asemel, et esitada taotlus. See on väga paindlik ja võimaldab palju parendusi kasutajakogemuse osas.

![kaas](assets/chapitre10/2.webp)

Keysend võimaldab Alicel saata raha Bobile ilma Bobi taotluseta. Alice hangib Bobi ID, loob eelkujutise ilma Bobilt küsimata ja lisab selle oma maksesse. Nii saab Bob üllatusnõude, kus ta saab raha vabastada, sest Alice on juba töö ära teinud.

![kaas](assets/chapitre10/3.webp)

Kokkuvõttes, kuigi Lightning Network'i arve võib esmapilgul tunduda keeruline, kodeerib see tõhusalt maksetaotluse. Arve iga osa sisaldab võtmekohast teavet, sealhulgas makstav summa, saaja, loomise ajatempel ja potentsiaalselt muu teave, nagu eelkujutise räsi, makse saladus, marsruutimisviited ja aegumisaeg. Protokollid nagu LNURL ja Keysend pakuvad olulisi parendusi paindlikkuse ja kasutajakogemuse osas, võimaldades näiteks saata vahendeid ilma teise poole eelneva taotluseta. Need tehnoloogiad muudavad makseprotsessi Lightning võrgus sujuvamaks ja tõhusamaks.

## Likviidsuse haldamine
<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>

![juhis](assets/chapitre11/0.webp)

Anname mõned üldised juhised igikestvale küsimusele likviidsuse haldamisest Lightning'is.

LN-s on 3 tüüpi inimesi:

- Ostjad: neil on väljaminev likviidsus, mis on kõige lihtsam, sest nad peavad lihtsalt kanaleid avama
- Kaupmehed: see on keerulisem, sest nad vajavad sissetulevat likviidsust teistelt sõlmedelt ja teistelt osalistelt. Neil peab olema ühendus inimestega
- Marsruutimissõlmed: nad soovivad olla tasakaalus likviidsusega mõlemal poolel ja omada head ühendust paljude sõlmedega, et neid võimalikult palju kasutataks

Nii et kui vajate sissetulevat likviidsust, saate seda teenustest osta.

![juhis](assets/chapitre11/1.webp)

Alice ostab kanali Susiega 1 miljoni satoshi eest, nii et ta avab kanali otse 1 000 000 SAT-ga sissetuleval poolel. Ta saab siis vastu võtta kuni 1 miljon SAT-i makseid klientidelt, kes on Susiega ühendatud (kes on hästi ühendatud).
Teine lahendus oleks teha makseid; maksate 100 000 mingil X põhjusel, nüüd saate vastu võtta 100 000.
![instruction](assets/chapitre11/2.webp)

### Loop Out lahendus: Atomic swap LN - BTC

Alice 2 miljonit - Susie 0

![instruction](assets/chapitre11/3.webp)

Alice soovib saata likviidsust Susiele, seega teeb ta Loop out'i (eriline sõlm, mis pakub pro teenust LN/BTC tasakaalustamiseks).
Alice saadab 1 miljoni Loopile läbi Susie sõlme, nii et Susiel on likviidsus ja Loop saadab on-chain saldo tagasi Alice'i sõlme.

![instruction](assets/chapitre11/4.webp)

Nii läheb 1 miljon Susiele, Susie saadab 1 miljoni Loopile, Loop saadab 1 miljoni Alice'ile. Alice on seega liigutanud likviidsust Susiele, makstes mõningaid tasusid Loopile teenuse eest.

Kõige keerulisem asi LN-is on likviidsuse säilitamine.

![instruction](assets/chapitre11/5.webp)

Kokkuvõttes on likviidsuse haldamine Lightning Networkis võtmeküsimus, mis sõltub kasutaja tüübist: ostja, kaupmees või marsruutimissõlm. Ostjad, kes vajavad väljaminevat likviidsust, on lihtsaimas olukorras: nad lihtsalt avavad kanalid. Kaupmehed, kes vajavad sissetulevat likviidsust, peavad olema ühendatud teiste sõlmede ja osalistega. Marsruutimissõlmed seevastu püüavad säilitada likviidsuse tasakaalu mõlemal poolel. Likviidsuse haldamiseks on mitmeid lahendusi, nagu kanalite ostmine või vastuvõtu võimekuse suurendamise eest maksmine. "Loop Out" võimalus, mis võimaldab Atomic Swap'i LN ja BTC vahel, pakub huvitavat lahendust likviidsuse tasakaalustamiseks. Hoolimata neist strateegiatest, jääb likviidsuse säilitamine Lightning Networkis keeruliseks väljakutseks.

# Mine edasi
<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>

## Kursuse kokkuvõte
<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>

Meie eesmärk oli selgitada, kuidas Lightning Network töötab ja kuidas see toetub Bitcoinile.

Lightning Network on maksekanalite võrgustik. Oleme näinud, kuidas maksekanal töötab kahe osapoole vahel, kuid oleme samuti laiendanud oma vaadet kogu võrgustikule, maksekanalite võrgustiku mõistele.

![instruction](assets/chapitre12/0.webp)

Kanalid avatakse Bitcoin tehinguga ja need võivad mahutada nii palju tehinguid kui võimalik. Kanali seisundit esindab kohustuslik tehing, mis saadab igale osapoolele selle, mis neil kanali poolel on. Kui kanalis toimub tehing, kohustuvad osapooled uuele seisundile, tühistades vana seisundi ja luues uue kohustusliku tehingu.

![instruction](assets/chapitre12/1.webp)

Paarid kaitsevad end pettuse eest revokatsioonivõtmete ja ajalukuga. Kanali sulgemisel eelistatakse vastastikust nõusolekut. Sunnitud sulgemise korral avaldatakse viimane kohustuslik tehing.

![instruction](assets/chapitre12/3.webp)

Maksed võivad laenata kanaleid teistelt vahesõlmedelt. Tingimuslikud maksed hash time lock'i (HTLC) abil võimaldavad vahendeid lukustada, kuni makse on täielikult lahendatud. Lightning Network kasutab sibulmarsruutimist. Vahesõlmed ei tea maksete lõppsihtkohta. Alice peab arvutama maksetee, kuid tal pole kogu teavet vahesõlmede likviidsuse kohta.

![instruction](assets/chapitre12/4.webp)

Makse saatmisel Lightning Networki kaudu on olemas tõenäosuskomponent.
![juhend](assets/chapitre12/5.webp)
Maksete vastuvõtmiseks tuleb kanalites likviidsust hallata, mida saab teha teistelt kanalite avamist paludes, ise kanaleid avades ning kasutades tööriistu nagu Loop või ostes/rentides kanaleid turgudelt.

## Fanise intervjuu
<chapterId>077cb5f5-1626-5da5-9964-e67b1de503bf</chapterId>

Siin on intervjuu kokkuvõte:

Lightning Network on Bitcoinil põhinev ülikiire makselahendus, mis võimaldab ületada võrgu skaleeritavusega seotud piiranguid. Siiski ei ole Lightningil olevad bitcoini'd nii turvalised kui need Bitcoin'i ahelas, kuna skaleeritavuse üle eelistatakse detsentraliseeritust ja turvalisust.

Liigne ploki suuruse suurendamine ei ole hea lahendus, kuna see ohustab node'e ja andmemahu piiranguid. Selle asemel võimaldab Lightning Network luua maksekanaleid kahe Bitcoin'i kasutaja vahel ilma tehinguid plokiahelas näitamata, säästes ruumi plokkides ja võimaldades Bitcoin'il täna skaleeruda.

Siiski on Lightning Network'i skaleeritavuse ja tsentraliseerituse osas kriitikat, potentsiaalsete probleemidega seoses kanalite sulgemise ja kõrgete tehingutasudega. Nende probleemide lahendamiseks soovitatakse vältida väikeste kanalite avamist, et tulevikus probleeme vältida, ja suurendada tehingutasusid Child Pay for Parent abil.

Lightning Network'i tulevikuks kaalutud lahendused on tehingute grupeerimine ja kanalite loomine gruppides, et vähendada tehingutasusid, samuti ploki suuruse suurendamine pikemas perspektiivis. Siiski on oluline märkida, et Lightning'il olevad bitcoini'd ei ole nii turvalised kui Bitcoin'i ahelas olevad bitcoini'd.

Bitcoin'i ja Lightning'i privaatsus on omavahel seotud, sibulmarsruutimine tagab tehingutele teatud privaatsuse taseme. Siiski on Bitcoin'il kõik vaikimisi läbipaistev, kasutades heuristikat Bitcoinide jälgimiseks aadressilt aadressile Bitcoin'i ahelas.

Bitcoinide ostmine KYC abil võimaldab vahetusel teada väljamaksetehinguid, samas kui ümmargused summad ja vahetus aadressid võimaldavad teada, milline osa tehingust on mõeldud teisele isikule ja milline osa endale.

Privaatsuse parandamiseks võimaldavad ühistegevused ja coinjoinid murda tõenäosusarvutusi, tehes tehinguid, kus mitu inimest teevad koos tehingu. Ahelaanalüüsi ettevõtetel on raskem jälgida, mida te oma bitcoinidega teete.

Lightning'il on tehingust teadlikud ainult kaks inimest ja see on privaatsem kui Bitcoin. Sibulmarsruutimine tähendab, et vahepealne sõlm ei tea makse saatjat ja saajat.

Lightning Network'i kasutamiseks soovitatakse jälgida koolitust teie YouTube'i kanalil või otse avastage Bitcoin'i veebisaidil või kasutada koolitust Umbrellil. Samuti on võimalik Lightning'i makse ajal saata suvalist teksti kasutades selleks ettenähtud välja, mis võib olla kasulik annetuste või sõnumite jaoks.
Siiski on oluline märkida, et tulevikus võidakse Lightning'i marsruutimissõlmi reguleerida, mõned riigid püüavad marsruutimissõlmi reguleerida. Kaupmeestele on vajalik likviidsuse haldamine maksete vastuvõtmiseks Lightning Network'is, praeguste piirangutega, mida saab ületada sobivate lahendustega.

Lõpuks on Bitcoin'i tulevik lubav, võimaliku prognoosiga üks miljon viie aasta jooksul. Tööstuse professionaalsuse tagamiseks ja olemasoleva pangandussüsteemi alternatiivi loomiseks on oluline panustada võrku ja lõpetada usaldamine.

## Tunnustused ja jätkake jäneseurgu uurimist
<chapterId>afc0d72b-4fbc-5893-90b2-e27fb519ad02</chapterId>

Palju õnne! 🎉
Olete lõpetanud LN 201 koolituse - Sissejuhatus Lightning Network'i!
Võite olla uhke, sest see pole lihtne. Teadke, et vähesed inimesed lähevad Bitcoin'i jäneseurgu nii sügavale.
Esiteks, suur tänu Fanis Makalakisele, kes pakkus meile seda suurepärast tasuta kursust, mis keskendub Lightning'i etnilisemale aspektile. Ärge kõhelge jälgimast teda Twitteris, tema blogis või tema töö kaudu LN turul.

Seejärel, kui soovite projekti aidata, ärge kõhelge meid Patreonis toetamast. Teie annetusi kasutatakse uute koolituskursuste sisu tootmiseks ja loomulikult teavitatakse teid esimesena (kaasa arvatud Fanise järgmise kursuse kohta, mis on töös!).

Lightning Network'i seiklus jätkub Umbreli koolituse ja Lightning Network'i sõlme rakendamisega. Teooria on läbi ja on aeg praktikaks LN 202 koolitusega nüüd!

Musid ja näeme varsti!

Rogzy