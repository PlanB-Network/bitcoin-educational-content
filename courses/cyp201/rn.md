---
name: Ibikorwa vy'imbere mu bikoresho vya Bitcoin
goal: Nimwinjire mu ngingo ngenderwako z’ubuhinga bwa none ziha ubushobozi amasakoshi ya Bitcoin.
objectives: 

  - Sigura ivyiyumviro vy'inyigisho bikenewe kugira ngo umuntu atahure ubuhinga bwo gukora amakuru bukoreshwa muri Bitcoin.
  - Gutahura neza inyubako y'ubuhinga n'ubuhinga bwa Wallet.
  - Kumenya ingene womenya no kugabanya ingorane zijanye n’ugucungera Wallet.
  - Gutahura ingingo ngenderwako z’ibikorwa vya Hash, imfunguruzo z’ubuhinga bwa none, n’imikono y’ubuhinga bwa none.

---

# Urugendo rwo mu mutima w'amasakoshi ya Bitcoin


Tora amabanga y’amasakoshi ya Bitcoin y’ubuhinga n’ubukuru n’inyigisho yacu ya CYP201! Waba uri umukoresha asanzwe canke uwukunda cane ushaka gukomeza ubumenyi bwawe, iri shure ritanga inyigisho yuzuye mu mikorere y’ivyo bikoresho twese dukoresha ku musi ku musi.


Menya uburyo Hash ikora, imikono ya digitale (ECDSA na Schnorr), amajambo ya Mnemonic, imfunguruzo z’ubuhinga bwa none, n’uguhingura amaderesi y’ukwakira, vyose mu gihe uriko urarondera ingamba ziteye imbere zo gucungera umutekano.


Iryo huriro ntirizoguha gusa ubumenyi bwo gutahura imiterere ya Bitcoin Wallet ariko kandi rizogutegurira kwisuka cane mw’isi iryoshe cane y’ubuhinga bwo gukingira amakuru.


CYP201 ifise inyigisho zitomoye, ibishushanyo birenga 60 vy’insobanuro, n’ingero zitomoye, izogufasha gutahura kuva kuri A gushika kuri Z ingene Wallet yawe ikora, kugira ngo ushobore kugendagenda mw’isanzure ry’ikirere rya Bitcoin wizigiye. Fata ububasha ku ma UTXO yawe uno musi mu gutahura ingene ama wallet ya HD akora!


+++

# Imenyekanisha


<partId>32960669-d13a-592f-a053-37f70b997cbf</partId>


## Intangamarara y'Ivyigwa


<chapterId>fb4e8857-ea35-5a8a-ae8a-5300234e0104</chapterId>


Murakaze mu nyigisho ya CYP201, aho tuzokwihweza mu buryo bwimbitse ingene ama wallets ya HD Bitcoin akora. Iryo shure ryagenewe umuntu wese yipfuza gutahura ivy’ishimikiro vy’ubuhinga bwo gukoresha Bitcoin, yaba abayikoresha mu buryo busanzwe, abakunda ivy’umuco, canke abahinga bo muri kazoza.


Intumbero y’iyi nyigisho ni ukuguha imfunguruzo zo kumenya neza ibikoresho ukoresha ku musi ku musi. Ama wallets ya HD Bitcoin, ari yo ari mu mutima w’ubumenyi bwawe bwo gukoresha, ashingiye ku vyiyumviro rimwe na rimwe bikomeye, ivyo tuzogerageza gutuma bishoboka. Twese hamwe, tuzobikuramwo amabanga!


Imbere yo kwisuka mu ndondoro y’ubwubatsi n’imikorere y’amasakoshi ya Bitcoin, tuzotangura n’ibice bikeyi ku bijanye n’ibintu vya kera vy’ubuhinga bwa cryptography kugira ngo tumenye ibizokurikira.

Tuzotangura n’ibikorwa vy’ubuhinga bwa Hash, ivy’ishimikiro ku bikoresho vyose bibiri vy’amahera no ku bijanye n’umurongo wa Bitcoin ubwawo. Uzobona ibiranga cane, ibikorwa vyihariye bikoreshwa muri Bitcoin, kandi mu kigabane c'ubuhinga, uzomenya mu buryo burambuye ibijanye n'imikorere y'umwamikazi w'ibikorwa vya Hash: SHA256.


![CYP201](assets/fr/010.webp)


Igikurikira, tuzovuga ku mikorere y’ubuhinga bwa digitale signature ukoresha buri musi kugira ngo ukingire ama UTXO yawe. Bitcoin ikoresha bibiri: ECDSA n’umurongo wa Schnorr. Uzomenya ibiharuro vy’intango bishingiye kuri izo nzira n’ingene zituma haba umutekano w’ibikorwa.


![CYP201](assets/fr/021.webp)


Tumaze gutahura neza izo Elements z’ubuhinga bwo gukingira amakuru, tuzoheza tuje ku mutima w’amahugurwa: amasakoshi y’ibintu vy’agaciro n’ivy’ubukuru! Ica mbere, hariho igice kigenewe amajambo Mnemonic, ayo majambo akurikirana y’amajambo 12 canke 24 atuma ushobora kurema no gusubizaho amasakoshi yawe. Uzobona ingene ayo majambo akomoka ku nzira y’ubuhinga n’ingene yorosha gukoresha Bitcoin.


![CYP201](assets/fr/040.webp)


Iryo huriro rizobandanya n’ukwiga BIP39 passphrase, seed (ntituvyivangane n’ijambo Mnemonic), chain code nyamukuru, n’urufunguzo nyamukuru. Turaza kubona mu buryo burambuye ivyo Elements ari vyo, uruhara rwavyo, n’ingene biharurwa.


![CYP201](assets/fr/045.webp)


Ubwa nyuma, kuva ku rufunguzo rwa mbere, tuzobona ingene urufunguzo rw’ibanga rubiri ruva mu buryo bugenwa n’ubukuru gushika ku maderesi y’ukwakira.


![CYP201](assets/fr/056.webp)


Iryo shure rizotuma ushobora gukoresha porogarama yawe ya Wallet wizigiye, mu gihe uzokwongerera ubuhinga bwo kumenya no kugabanya ingorane. Nimwitegure kuba umuhinga nyakuri mu vy’amasakoshi ya Bitcoin!


Iyi mbonerahamwe iguha ubusobanuro bw’amagambo y’icongereza akunda gukoreshwa, kugira ngo bigufashe gusobanukirwa neza amashusho n’inyandiko z’ubuhanga zikoreshwa mu masomo ya CYP 201.

| Icongereza      | Ibisobanuro / Ibisobanuro                                                                           |
| --------------- | -------------------------------------------------------------------------------------------------- |
| *pubkey hash*   | Hash y'urufunguzo rw'umuryango (ikoreshwa mugukora aderesi ya Bitcoin).                            |
| *public key*    | Urufunguzo rw'umuryango (rukoreshwa mugwakira amafaranga, rukomoka k'urufunguzo rw'ibanga).         |
| *signature*     | Umukono wa dijitale (ikimenyetso cya cryptographie cyerekana ko ubutumwa buva ku nyir' urufunguzo rw'ibanga). |
| *scriptPubKey*  | Script yo gufunga (igena uburyo bwo gukoresha output).                                              |
| *scriptSig*     | Script yo gufungura (itanga amakuru yo kuzura *scriptPubKey*).                                      |
| *Stack*         | Stack (uburyo bw'imiterere y'amakuru bukoreshwa na *Bitcoin Script*).                               |
| *input*         | Icyinjizo cya transaction (icyerekezo ku output yahise ikoreshwa nk'isoko).                        |
| *output*        | Icyasohotse cya transaction (igena uwakiriye n' amafaranga).                                        |
| *transaction*   | Transaction ya Bitcoin (itsinda ry'ibyinjijwe n'ibyashyizwe hanze bigaragaza kohereza amafaranga).  |
| *XOR*           | Operateri ya logic "OR idasanzwe", ikoreshwa mu buryo bumwe bwa cryptographie.                     |
| *HMAC*          | Kode yo kugenzura ubutumwa ishingiye kuri hash n'urufunguzo rw'ibanga.                              |
| *ECDSA*         | Algorithmu y'umukono wa dijitale ushingiye ku mirongo y'ibiziga by'ellipse.                         |
| *hash*          | Hash (ikimenyetso cyihariye kandi gihoraho cy'amakuru).                                             |
| *SigHash*       | Ubwoko bwa hash bw'umukono (bugena ibice bya transaction bisinywa).                                 |
| *HD Wallet*     | Wallet idashobora guhinduka igendera ku byiciro (ikora imfunguzo nyinshi uhereye ku mbuto imwe).    |
| *Random Number* | Umubare w'ibanze (ukoreshwa mugukora imfunguzo z'ibanga zizewe).                                    |
| *State*         | Leta (agaciro kari hagati mu buryo bwa cryptographie).                                              |
| *Entropy*       | Entropie (igipimo cy'ubusanzwe, gikoreshwa mugukora imbuto za wallet).                             |
| *Mnemonic*      | Mnemonique (urukurikirane rw'amagambo yorohereza kubika no kugarura imbuto).                        |
| *Wordlist*      | Urutonde rw'amagambo (itsinda ryagenwe rikoreshwa mugukora mnemonique za BIP39).                    |
| *Seed*          | Imbuto (agaciro k'ibanze gashobora gukuramo imfunguzo zose za HD Wallet).                           |
| *Address*       | Aderesi ya Bitcoin (ikimenyetso cyoroshye gusoma cyo kwakira amafaranga, gituruka ku rufunguzo rw'umuryango). |
| *Leaf*          | Ishami (iherezo ry'igiti cya derivation).                                                           |

# Imikorere ya Hash


<partId>3713fee1-2ec2-512e-9e97-b6da9e4d2f17</partId>


## Intangamarara y'Ibikorwa vya Hash


<chapterId>dba011f5-1805-5a48-ac2b-4bd637c93703</chapterId>


Ubwoko bwa mbere bw’ubuhinga bwo gukora amakuru bukoreshwa muri Bitcoin bushimikiye ku bikorwa vya Hash. Bifise uruhara runini ku nzego zitandukanye z’amasezerano, ariko kandi no mu bipapuro vya Bitcoin. Reka tubone hamwe ico igikorwa ca Hash ari co n'ico gikoreshwa muri Bitcoin.


### Insobanuro n'ingingo ngenderwako y'ugukora Hashing


Hashing ni uburyo buhindura amakuru y’uburebure butari bwo mu yandi makuru y’uburebure butahinduka biciye ku gikorwa c’ubuhinga bwa cryptographic Hash. Mu yandi majambo, igikorwa ca Hash gifata inyinjizo y'ingene iyo ari yo yose ikayihindura mu rutoke rw'ingene rudahinduka, rwitwa "Hash".

Hash ishobora kandi rimwe na rimwe kwitwa "digest", "ihinduka", "ihinduka", canke "ihinduka".


Nk’akarorero, igikorwa ca SHA256 Hash kiratanga Hash y’uburebure butahinduka bw’ibice 256. Gutyo, nitwakoresha inyinjizo "_PlanB_", ubutumwa bw'uburebure butari bwo, Hash izovyarwa izoba ari urutoke rw'ibice 256 rukurikira:


```text
24f1b93b68026bfc24f5c8265f287b4c940fb1664b0d75053589d7a4f821b688
```


![CYP201](assets/fr/001.webp)


### Ibiranga ibikorwa vya Hash


Ivyo bikorwa vy’ubuhinga bwa Hash bifise ibiranga vyinshi bihambaye bituma biba ngirakamaro canecane mu bijanye na Bitcoin n’izindi nzira za mudasobwa:



- Ugusubira inyuma (canke ukurwanya imbere y'ishusho)
- Uguhangana n'ibintu (ingaruka z'urubura)
- Uguhangana n'ugutombora
- Uguhangana n'ishusho ya kabiri


#### 1. Ugusubira inyuma (uguhangana n’ishusho y’imbere):


Irreversibility bisigura ko vyoroshe kubara Hash bivuye ku makuru yinjijwe, ariko kubara inverse, ni ukuvuga kuronka inyungu bivuye kuri Hash, ntaco bimaze. Ivyo bituma ibikorwa vya Hash biba vyiza cane mu guhingura ibimenyetso vy’intoke vy’ubuhinga bwa none ataco bihinduye ku makuru y’intango. Ico kiranga akenshi citwa igikorwa c’inzira imwe.


Mu karorero katanzwe, kuronka Hash `24f1b9...` mu kumenya inyungu "_PlanB_" biroroshe kandi vyihuta. Ariko rero, kuronka ubutumwa "_PlanB_" mu kumenya gusa `24f1b9...` ntibishoboka.


![CYP201](assets/fr/002.webp)


Rero, ntibishoboka ko umuntu aronka ishusho y’imbere $m$ ku Hash $h$ ku buryo $h = \umwandiko{Hash}(m)$, aho $\umwandiko{Hash}$ ari igikorwa ca Hash c’ubuhinga bwo gukingira.


#### 2. Uguhangana n'ibintu bitari vyo (ingaruka z'urubura)


Ikintu ca kabiri kiranga ni ukudashobora guhindurwa, kizwi kandi kw’izina rya **avalanche effect**. Ivyo bigaragara mu gikorwa ca Hash iyo ihinduka ritoyi mu butumwa bw'injiza rituma habaho ihinduka rikomeye mu butumwa bw'isohoka Hash.


Nitwasubira ku karorero kacu n'inyungu "_PlanB_" n'igikorwa ca SHA256, twabonye ko Hash yavutse ari iyi:


```text
24f1b93b68026bfc24f5c8265f287b4c940fb1664b0d75053589d7a4f821b688
```


Nitwahindura gato cane ku vyo twinjiza dukoresheje "_Planb_" kuri iyi ncuro, rero guhindura gusa kuva ku nyuguti nini "B" gushika ku nyuguti nto "b" bihindura burundu igisohoka ca SHA256 Hash:


```text
bb038b4503ac5d90e1205788b00f8f314583c5e22f72bec84b8735ba5a36df3f
```


![CYP201](assets/fr/003.webp)


Ivyo bituma mbere n'uguhindura gutoyi kw'ubutumwa bw'intango bica bimenyekana, kuko bidahindura gusa igice gitoyi ca Hash, ariko bihindura Hash yose. Ivyo birashobora gushimisha mu bikorwa bitandukanye kugira ngo umuntu asuzume ubutungane bw’ubutumwa, porogarama canke mbere n’ibikorwa vya Bitcoin.


#### 3. Uguhangana n'ugutombora


Ikintu ca gatatu kiranga ni ukudashobora guhura n’ibintu. Igikor ca Hash kirashobora guhangana n’ugutomboka iyo bidashoboka mu buryo bw’ubuhinga bwo guharura kuronka ubutumwa 2 butandukanye butanga umusaruro umwe wa Hash uva ku gikorwa. Mu buryo busanzwe, biragoye kuronka ubutumwa bubiri butandukanye $m_1$ na $m_2$ ku buryo:


$$
\text{HASH}(m_1) = \text{HASH}(m_2)
$$


![CYP201](assets/fr/004.webp)


Mu vy’ukuri, ni ikintu kidashobora gukurwaho mu mibare ko hariho ugutombora ku bikorwa vya Hash, kuko ubunini bw’ibintu vyinjizwa bushobora kuba bunini kuruta ubunini bw’ibintu bisohoka. Ivyo bizwi nk’ingingo ngenderwako y’ibitabo vya Dirichlet: iyo ibintu $n$ bigabanywe mu bitabo $m$, bifise $m < n$, rero n’imiburiburi igitabo kimwe kizobamwo ibintu bibiri canke birenze. Ku gikorwa ca Hash, iyi ngingo irakora kubera ko umubare w'ubutumwa bushoboka ari (hafi) ubutagira iherezo, mu gihe umubare w'ama hashes ashoboka ufise iherezo ($2^{256}$ mu gihe ca SHA256).


Gutyo, iki kiranga ntibisigura ko ata gutombora ku bikorwa vya Hash, ahubwo ko igikorwa ciza ca Hash gituma ubushobozi bwo kuronka ugutombora buba buke. Ico kiranga, nk’akarorero, ntikigisuzumwa ku nzira za SHA-0 na SHA-1, zabanjirije SHA-2, zabonetse ko zihuye. Ivyo bikorwa rero ubu birahanurirwa kandi kenshi bifatwa nk’ibitagira akamaro.

Ku gikorwa ca Hash c'ibice $n$, ubushobozi bwo guhangana n'ugutombora ni ubw'urutonde rwa $2^{\frac{n}{2}}$, bihuye n'igitero c'umunsi w'amavuko. Nk’akarorero, kuri SHA256 ($n = 256$), uburemere bwo kuronka ugutombora ni ubw’urutonde rw’ibigeragezo vya $2^{128}$. Mu majambo y'ibikorwa, ivyo bisigura ko iyo umuntu aciye $2^{128}$ ubutumwa butandukanye biciye mu gikorwa, umuntu ashobora gusanga ihuriro.


#### 4. Uguhangana n’Ishusho ya Kabiri


Uguhangana n’ishusho ya kabiri ni ikindi kintu gihambaye kiranga ibikorwa vya Hash. Ivuga ko hatanzwe ubutumwa $m_1$ na Hash $h$ yayo, bidashoboka mu buryo bw’ubuhinga bwo guharura kuronka ubundi butumwa $m_2 \neq m_1$ nk’uko:


$$
\text{HASH}(m_1) = \text{HASH}(m_2)
$$


Rero, ukurwanya ishusho ya kabiri y’imbere birasa n’ukurwanya ugutombora, kiretse aha, igitero kiragoye cane kuko uwutera adashobora guhitamwo $m_1$ mu mwidegemvyo.


![CYP201](assets/fr/005.webp)


### Ikoreshwa rya Hash Ibikorwa muri Bitcoin


Igikoresho ca Hash gikoreshwa cane muri Bitcoin ni **SHA256** ("_Igikoresho ca Hash gikoreshwa cane 256"_). Yahinguwe mu ntango z’imyaka ya 2000 na NSA, ikaba yashizwe ku rugero rwa NIST, itanga umuyagankuba w’ibice 256 Hash.


Iyi nzira ikoreshwa mu mice myinshi ya Bitcoin. Ku rugero rwa porotokole, iragira uruhara mu buryo bwa Proof-of-Work, aho ikoreshwa mu gukora hashing kabiri kugira ngo irondere uguhura kw’igice hagati y’umutwe w’ibarabara ry’umukandida, ryaremwe na Miner, n’intumbero y’ingorane. Iyo iyo mpanuka y'igice ibonetse, igice c'abashaka gutora kiragira akamaro kandi gishobora kwongerwa kuri Blockchain.


SHA256 ikoreshwa kandi mu kwubaka Merkle Tree, ari yo cane cane accumulateur ikoreshwa mu kwandika amafaranga mu bice. Iyi mibumbe iraboneka kandi mu nzira ya Utreexo, ishobora kugabanya ubunini bwa UTXO Set. Ikindi, n’ugushiraho Taproot mu 2021, SHA256 irakoreshwa muri MAST (_Merkelised Alternative Script Tree_), ishobora guhishura gusa ivyangombwa vy’ugukoresha amahera bikoreshwa mu vy’ukuri mu nyandiko, ata guhishura izindi nzira zishoboka. Ikoreshwa kandi mu kubara ibimenyetso vy’ibikorwa, mu gutanga amapakete ku rubuga rwa P2P, mu mikono y’ubuhinga bwa none... Ubwa nyuma, kandi ivyo birahambaye cane muri aya mahugurwa, SHA256 ikoreshwa ku rugero rw’ikoreshwa ry’ubwubatsi bw’amasakoshi ya Bitcoin no gukura amaderesi.


Akenshi, iyo uhuye n'ikoreshwa rya SHA256 muri Bitcoin, mu vy'ukuri izoba ari Hash SHA256 ibiri, ivugwa ko "**HASH256**", ikaba gusa igizwe n'ugukoresha SHA256 incuro zibiri zikurikirana:


$$
\text{HASH256}(m) = \text{SHA256}(\text{SHA256}(m))
$$


Uwo mugenzo wo gukoresha double hashing wongeramwo Layer y’umutekano ku bitero bimwebimwe bishobora gushika, naho SHA256 imwe uno musi ifatwa nk’iyitekanye mu buryo bw’ubuhinga bw’ibanga.


Iyindi nzira yo gukora hashing iboneka mu rurimi rwa Script kandi ikoreshwa mu gukura amaderesi y’ukwakira ni nzira ya RIPEMD160. Iyi nzira itanga Hash y’ibice 160 (ni co gituma ari ngufi kuruta SHA256). Muri rusangi ifatanijwe na SHA256 kugira ngo ikore igikorwa ca HASH160:


$$
\text{HASH160}(m) = \text{RIPEMD160}(\text{SHA256}(m))
$$


Iryo huriro rikoreshwa ku generate hashes ngufi, cane cane mu kurema aderesi zimwe zimwe za Bitcoin ziserukira hashes z'imfunguruzo canke hashes z'inyandiko, hamwe no gutanga ibimenyetso vy'intoke z'imfunguruzo.


Ubwa nyuma, ku rugero rw’ikoreshwa gusa, rimwe na rimwe igikorwa ca SHA512 na co nyene kirakoreshwa, kikaba gifise uruhara mu buryo butaziguye mu gukuraho urufunguzo rw’amasakoshi. Iyi nshingano isa cane na SHA256 mu mikorere yayo; vyose biri mu muryango umwe wa SHA2, ariko SHA512 itanga, nk'uko izina ryayo rivyerekana, Hash y'ibice 512, ugereranyije n'ibice 256 vya SHA256. Tuzodondora ido n’ido ingene rikoreshwa mu bigabane bikurikira.


Ubu urazi ivy’ishimikiro vy’ingenzi ku bijanye n’ibikorwa vy’ugukora hashing ku bikurikira. Mu gice gikurikira, ndasaba kumenya mu buryo burambuye ingene igikorwa kiri mu mutima wa Bitcoin: SHA256 gikora. Tuzoyicapura kugira ngo dutahure ingene ishika ku biranga twadondoye ngaha. Iki gice gikurikira ni kirekire cane kandi gifise ubuhinga, ariko si ngombwa ko umuntu akurikirana inyigisho zisigaye. Rero, nimba ufise ingorane zo kubitahura, ntuhagarike umutima maze ugende ushitse ku kigabane gikurikira, kizoba kigufasha cane.


## Ibikorwa vy'imbere vya SHA256


<chapterId>905eb320-f15b-5fb6-8d2d-5bb447337deb</chapterId>


Twarabonye mbere ko ibikorwa vy'ugukora hashing bifise ibiranga bihambaye bituma bikoreshwa muri Bitcoin. Reka ubu dusuzume uburyo bwo mu mutima bw'izo nshingano ziziha izo nzira, kandi kugira ngo tubikore, ndasaba gucapura igikorwa ca SHA256.


Ibikorwa vya SHA256 na SHA512 biri mu muryango umwe wa SHA2. Uburyo bwavyo bushingiye ku nyubakwa yihariye yitwa **inyubako ya Merkle-Damgård**. RIPEMD160 nayo ikoresha ubwo bwoko nyene bw’ubwubatsi.


Nk’ukwibutsa, dufise ubutumwa bw’ubunini butari bwo nk’injiza muri SHA256, kandi tuzobuca mu gikorwa kugira ngo turonke Hash y’ibice 256 nk’isohoka.


### Imbere y'ugutunganya ivyinjijwe


Kugira ngo dutangure, turakeneye gutegura ubutumwa bwacu bw’injiza $m$ kugira ngo bugire uburebure busanzwe ari bwo bwinshi bw’ibice 512. Iyi ntambwe ni ngirakamaro kugira ngo algorithme ikore neza mu nyuma.

Kugira ngo ivyo tubishikeko, dutangura n’intambwe y’ibice vy’ivyuma. Turabanza kwongerako igice gitandukanya `1` ku butumwa, hanyuma hakurikirwa umubare w'ibice `0`. Umubare w'ibice `0` vyongeweko ubarwa kugira ngo uburebure bwose bw'ubutumwa inyuma y'ivyo vyongeweko bube buhuye na 448 modulo 512. Gutyo, uburebure $L$ bw'ubutumwa bufise ibice vy'ugushiramwo bungana na:


$$
L \equiv 448 \mod 512
$$


$\text{mod}$, ku modulo, ni igikorwa c'imibare, hagati y'imibare ibiri yose, kigarura igice gisigaye c'ugucapura kwa Euclide kw'uwa mbere n'uwa kabiri. Nk’akarorero: $16 \mod 5 = 1$. Ni igikorwa gikoreshwa cane mu gukora amakuru y’ibanga.


Aha, intambwe yo gupfuka iratuma, umaze kwongerako ibice 64 mu ntambwe ikurikira, uburebure bwose bw’ubutumwa buringanijwe buzoba ari incuro nyinshi y’ibice 512. Niba ubutumwa bwa mbere bufise uburebure bw'ibice $M$, umubare ($N$) w'ibice `0` vyo kwongerwako ni uko:


$$
N = (448 - (M + 1) \mod 512) \mod 512
$$


Nk’akarorero, nimba ubutumwa bwa mbere ari 950 bits, igiharuro coba ari iki:


$$
\begin{align*}
M & = 950 \\
M + 1 & = 951 \\
(M + 1) \mod 512 & = 951 \mod 512 \\
& = 951 - 512 \cdot \left\lfloor \frac{951}{512} \right\rfloor \\
& = 951 - 512 \cdot 1 \\
& = 951 - 512 \\
& = 439 \\
\\
448 - (M + 1) \mod 512 & = 448 - 439 \\
& = 9 \\
\\
N & = (448 - (M + 1) \mod 512) \mod 512 \\
N & = 9 \mod 512 \\
& = 9
\end{align*}
$$


Gutyo, twoba dufise 9 `0`s zongeye ku gitandukanya `1`. Ivyiyumviro vyacu vyo kwongerako inyuma y'ubutumwa bwacu $M$ vyoba rero:


```text
1000 0000 00
```


Tumaze kwongerako ibice vy’ugupfuka ku butumwa bwacu $M$, twongerako kandi ibice 64 vy’uburebure bw’intango bw’ubutumwa $M$, bugaragazwa mu buryo bw’ibice bibiri. Ivyo bituma igikorwa ca Hash gishobora gutahura urutonde rw’ibice be n’uburebure bw’ubutumwa.


Nitwasubira ku karorero kacu n'ubutumwa bwa mbere bw'ibice 950, duhindura umubare w'icumi `950` mu bice bibiri, bikaduha `1110 1101 10`. Turaheza uwo mubare dukoresheje zero ku ntango kugira ngo tugire umubare wose w’ibice 64. Mu karorero kacu, ivyo bitanga:


```text
0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0011 1011 0110
```


Iyi ngano y'ugupfuka yongerwa hakurikijwe ugupfuka kw'ibice. Ubutumwa rero inyuma y’ugutegura imbere y’igihe kwacu bugizwe n’ibice bitatu:



- Ubutumwa bw'intango $M$;
- A bit `1` ikurikiwe n'ibice vyinshi `0` kugira ngo haboneke ibice vy'inyuma;
- Igishushanyo c'ibice 64 c'uburebure bwa $M$ kugira ngo ukore igipfukisho n'ubunini.


![CYP201](assets/fr/006.webp)


### Itanguriro ry'ibihinduka


SHA256 ikoresha ibihinduka umunani vy'intango, bigaragazwa na $A$ gushika kuri $H$, kimwe cose gifise ibice 32. Ivyo bihinduka bitanguzwa n’ibidahinduka vyihariye, ari vyo bice vy’imice y’imizi y’imibare umunani ya mbere. Tuzokoresha izo nkuru mu nyuma mu gihe c'urugendo rwo gukora hashing:



- $A = 0x6a09e667$
- $B = 0bb67ae85$
- $C = 0x3c6ef372$
- $D = 0xa54ff53a$
- $E = 0x510e527f$
- $F = 0x9b05688c$
- $G = 0x1f83d9ab$
- $H = 0x5kuba0cd19$


SHA256 kandi ikoresha izindi nkuru 64 zidahinduka, zigaragazwa na $K_0$ gushika kuri $K_{63}$, arivyo bice vy'imice y'imizi y'imibare 64 ya mbere:


$$
K[0 \ldots 63] = \begin{pmatrix}
0x428a2f98, & 0x71374491, & 0xb5c0fbcf, & 0xe9b5dba5, \\
0x3956c25b, & 0x59f111f1, & 0x923f82a4, & 0xab1c5ed5, \\
0xd807aa98, & 0x12835b01, & 0x243185be, & 0x550c7dc3, \\
0x72be5d74, & 0x80deb1fe, & 0x9bdc06a7, & 0xc19bf174, \\
0xe49b69c1, & 0xefbe4786, & 0x0fc19dc6, & 0x240ca1cc, \\
0x2de92c6f, & 0x4a7484aa, & 0x5cb0a9dc, & 0x76f988da, \\
0x983e5152, & 0xa831c66d, & 0xb00327c8, & 0xbf597fc7, \\
0xc6e00bf3, & 0xd5a79147, & 0x06ca6351, & 0x14292967, \\
0x27b70a85, & 0x2e1b2138, & 0x4d2c6dfc, & 0x53380d13, \\
0x650a7354, & 0x766a0abb, & 0x81c2c92e, & 0x92722c85, \\
0xa2bfe8a1, & 0xa81a664b, & 0xc24b8b70, & 0xc76c51a3, \\
0xd192e819, & 0xd6990624, & 0xf40e3585, & 0x106aa070, \\
0x19a4c116, & 0x1e376c08, & 0x2748774c, & 0x34b0bcb5, \\
0x391c0cb3, & 0x4ed8aa4a, & 0x5b9cca4f, & 0x682e6ff3, \\
0x748f82ee, & 0x78a5636f, & 0x84c87814, & 0x8cc70208, \\
0x90befffa, & 0xa4506ceb, & 0xbef9a3f7, & 0xc67178f2
\end{pmatrix}
$$


### Ugucapura kw'injiza


Ubu ko dufise input ingana, ubu tuzoja ku rwego nyamukuru rwo gutunganya SHA256 algorithm: igikorwa co gufatanya. Iyi ntambwe irahambaye cane, kuko ari yo mbere na mbere iha igikorwa ca Hash ubushobozi bwaco bwo gukingira amakuru twarize mu kigabane ca mbere.


Mbere, dutangura mu kugabanya ubutumwa bwacu bungana (inyishu y’intambwe z’imbere y’ugutegura) mu bice vyinshi $P$ vy’ibice 512 kuri kimwe cose. Nimba ubutumwa bwacu bungana bufise ubunini bwose hamwe bw’ibice $n \incuro 512$, tuzogira rero ibice $n$, kimwe cose kikaba gifise ibice 512. Igipande cose c’ibice 512 kizotunganirizwa kimwekimwe cose n’igikorwa co gufatanya, kikaba gifise ibice 64 vy’ibikorwa bikurikirana. Reka twite aya mabuye $P_1$, $P_2$, $P_3$...


### Ibikorwa bihuje n'ubwenge


Imbere yo gutohoza mu buryo burambuye igikorwa co gufatanya, birahambaye gutahura ibikorwa vy’ishimikiro vy’ubwenge bikoreshwa muri co. Ivyo bikorwa, bishingiye kuri aligebra ya Boolean, bikora ku rugero rw'ibice. Ibikorwa vy'ishimikiro bikoreshwa ni:



- **Inyuguti (AND)**: yerekanwa $\land$, ihuye n'inyuguti "AND" yumvikana.
- **Igiharuro (CANKE)**: kigaragazwa $\lor$, gihuye n'"CANKE" gihuye n'ubwenge.
- **Ukwihakana (NTA)**: bigaragazwa $\lnot$, bihuye n'ivyo "NTA" bihuye n'ubwenge.


Duhereye kuri ivyo bikorwa vy'ishimikiro, turashobora gusobanura ibikorwa bikomeye cane, nka "Exclusive OR" (XOR) yerekanwa na $\oplus$, ikoreshwa cane mu gukora amakuru y'ibanga.

Igikorwa kimwekimwe cose gishobora guserurwa n'imbonerahamwe y'ukuri, yerekana igisubizo ku migwi yose ishoboka y'agaciro k'inyungu y'ibice bibiri (ibikorwa bibiri $p$ na $q$).

Ku bwa XOR ($\ukwongerekana$):


| $p$ | $q$ | $p \oplus q$ |
| --- | --- | ------------ |
| 0   | 0   | 0            |
| 0   | 1   | 1            |
| 1   | 0   | 1            |
| 1   | 1   | 0            |

Kubera KANDI ($\ubutaka$):


| $p$ | $q$ | $p \land q$ |
| --- | --- | ----------- |
| 0   | 0   | 0           |
| 0   | 1   | 0           |
| 1   | 0   | 0           |
| 1   | 1   | 1           |

Kubera ATA ($\lsi p$):


| $p$ | $\lnot p$ |
| --- | --------- |
| 0   | 1         |
| 1   | 0         |

Reka dufate akarorero kugira ngo dutahure uko XOR ikora ku rugero rw’ibice. Niba dufise imibare ibiri ku bice 6:



- $a = 101100$
- $b = 001000$


None:


$$

a \oplus b = 101100 \oplus 001000 = 100100


$$


Mu gukoresha XOR gato ku gato:


| Bit Position | $a$ | $b$ | $a \oplus b$ |
| ------------ | --- | --- | ------------ |
| 1            | 1   | 0   | 1            |
| 2            | 0   | 0   | 0            |
| 3            | 1   | 1   | 0            |
| 4            | 1   | 0   | 1            |
| 5            | 0   | 0   | 0            |
| 6            | 0   | 0   | 0            |

Ico bivamwo rero ni $100100$.


Uretse ibikorwa vy’ubwenge, igikorwa co gufatanya gikoresha ibikorwa vyo guhindura ibice, ivyo bizogira uruhara runini mu gukwiragiza ibice mu nzira y’ubuhinga.


Ica mbere, hariho igikorwa co guhindura iburyo gihuje n’ubwenge, kigaragazwa na $ShR_n(x)$, gihindura ibice vyose vya $x$ iburyo n’ibibanza vya $n$, kikazuza ibice bitagira ikintu biri ibubamfu n’ibiharuro.


Nk'akarorero, ku $x = 101100001$ (ku bice 9) na $n = 4$:


$$

ShR_4(101100001) = 000010110


$$


Mu buryo bw'igishushanyo, igikorwa co guhindura iburyo coshobora kubonwa gutya:


![CYP201](assets/fr/007.webp)


Iyindi nzira ikoreshwa muri SHA256 ku gukoresha ibice ni uguhinduranya uruziga rw'iburyo, bigaragazwa na $RotR_n(x)$, bihindura ibice vya $x$ iburyo n'ibibanza vya $n$, bigasubira kwinjiza ibice vyahinduwe mu ntango y'urudodo.

Nk'akarorero, ku $x = 101100001$ (ibice birenga 9) na $n = 4$:


$$

RotR_4(101100001) = 000110110


$$


Mu buryo bw'igishushanyo, igikorwa co guhindura uruziga rw'iburyo coshobora kubonwa gutya:


![CYP201](assets/fr/008.webp)


### Ibikorwa vyo gufatanya


None ko twatahuye ibikorwa vy’ishimikiro, reka dusuzume mu buryo burambuye igikorwa co gufatanya SHA256.


Mu ntambwe ibanza, twagabuye ivyo twinjiza mu bice vyinshi vy’ibice 512 $P$. Ku buri 512-bit $P$, dufise:



- Amajambo y'ubutumwa **$W_i$**: ku $i$ kuva kuri 0 gushika kuri 63.
- Ibihoraho **$K_i$**: ku $i$ kuva kuri 0 gushika kuri 63, vyasobanuwe mu ntambwe ibanza.
- Ibihinduka vy'intara **A, B, C, D, E, F, G, H**: vyatangujwe n'agaciro kavuye mu ntambwe imbere.


Amajambo 16 ya mbere, $W_0$ gushika kuri $W_{15}$, akurwa mu buryo butaziguye mu gice c'ibice 512 $P$. Ijambo ryose $W_i$ rigizwe n'ibice 32 bikurikirana biva ku gice. Rero, nk’akarorero, dufata igice cacu ca mbere c’inyungu $P_1$, maze tugakomeza kugigabanya mu bice bitobito vy’ibice 32 twita amajambo.


Amajambo 48 akurikira ($W_{16}$ gushika kuri $W_{63}$) akomoka hakoreshejwe iyi formile:


$$
W_i = W_{i-16} + \sigma_0(W_{i-15}) + W_{i-7} + \sigma_1(W_{i-2}) \mod 2^{32}
$$


Hamwe:



- $ \ sigma_0 (x) = RotR_7 (x) \ yongerako ShR_3 (x) $
- $ \ sigma_1 (x) = RotR_{17}(x) \oplus ShR_{10}(x)$


Muri iki gihe, $x$ ingana na $W_{i-15}$ ku $\sigma_0(x)$ na $W_{i-2}$ ku $\sigma_1(x)$.


Tumaze kumenya amajambo yose $W_i$ y’igice cacu c’ibice 512, turashobora kuja ku gikorwa co gufatanya, kikaba ari ugukora ibice 64.


![CYP201](assets/fr/009.webp)

Ku nzira yose $i$ kuva kuri 0 gushika kuri 63, dufise ubwoko butatu butandukanye bw’ibintu vyinjizwa. Ica mbere, $W_i$ twahejeje kumenya, igice kimwe kigizwe n’igice c’ubutumwa bwacu $P_n$. Igikurikira, 64 bihoraho $K_i$. Ubwa nyuma, dukoresha ibihinduka vy’intara $A$, $B$, $C$, $D$, $E$, $F$, $G$, na $H$, bizotera imbere mu gihe cose c’ugukora hashing kandi bihindurwe n’igikorwa cose co gukoranya. Ariko rero, ku gice ca mbere $P_1$, dukoresha ibiharuro vy’intango vyatanzwe mbere.


Turaheza tugakora ibikorwa bikurikira ku vyo twinjiza:



- Umurimo $\Sigma_0$:


$$
\Sigma_0(A) = RotR_2(A) \oplus RotR_{13}(A) \oplus RotR_{22}(A)
$$



- Umukozi $\Sigma_1$:


$$
\Sigma_1(E) = RotR_6(E) \oplus RotR_{11}(E) \oplus RotR_{25}(E)
$$



- Umukozi $Ch$ ("_Hitamwo_")**:**


$$
Ch(E, F, G) = (E \land F) \oplus (\lnot E \land G)
$$



- Umukozi $Maj$ ("_Ivyinshi_"):


$$
Maj(A, B, C) = (A \land B) \oplus (A \land C) \oplus (B \land C)
$$


Turaheza tukabara ibihinduka 2 vy'igihe gito:



- $igihe1$:


$$
temp1 = H + \Sigma_1(E) + Ch(E, F, G) + K_i + W_i \mod 2^{32}
$$



- $igihe2$:


$$
temp2 = \Sigma_0(A) + Maj(A, B, C) \mod 2^{32}
$$


Ibikurikira, duhindura ibihinduka vya leta nk'uko bikurikira:


$$
\begin{cases}
H = G \\
G = F \\
F = E \\
E = D + temp1 \mod 2^{32} \\
D = C \\
C = B \\
B = A \\
A = temp1 + temp2 \mod 2^{32}
\end{cases}
$$


Igishushanyo gikurikira kigereranya uruziga rw'igikorwa co gufatanya SHA256 nk'uko twabidondoye:


![CYP201](assets/fr/010.webp)



- Imyambi yerekana ingene amakuru agenda;
- Ivyo bisandugu bigereranya ibikorwa vyakozwe;
- Ivyo $+$ bikikujwe bigereranya umubare w'inyongezo $2^{32}$.


Turashobora kubona ko iyo nzira isohora ibihinduka bishasha vy’intara $A$, $B$, $C$, $D$, $E$, $F$, $G$, na $H$. Ivyo bihinduka bishasha bizokora nk’inyungu y’urugendo rukurikira, ivyo na vyo bikazotuma habaho ibihinduka bishasha $A$, $B$, $C$, $D$, $E$, $F$, $G$, na $H$, bizokoreshwa mu rugendo rukurikira. Ivyo bica bibandanya gushika mu gice ca 64.

Inyuma y'ibice 64, turasubiramwo agaciro k'intango k'ibihinduka vya leta mu kubishira ku gaciro ka nyuma ku mpera y'igice ca 64:


$$
\begin{cases}
A = A_{\text{initial}} + A \mod 2^{32} \\
B = B_{\text{initial}} + B \mod 2^{32} \\
C = C_{\text{initial}} + C \mod 2^{32} \\
D = D_{\text{initial}} + D \mod 2^{32} \\
E = E_{\text{initial}} + E \mod 2^{32} \\
F = F_{\text{initial}} + F \mod 2^{32} \\
G = G_{\text{initial}} + G \mod 2^{32} \\
H = H_{\text{initial}} + H \mod 2^{32}
\end{cases}
$$


Ivyo bipimo bishasha vya $A$, $B$, $C$, $D$, $E$, $F$, $G$, na $H$ bizokora nk'ibipimo vy'intango vy'igice gikurikira, $P_2$. Kuri iyi block $P_2$, dusubiramwo iyo nzira nyene yo gufatanya n’ibice 64, hanyuma tugasubiramwo ibihinduka vy’iyi block $P_3$, n’ibindi gushika ku block ya nyuma y’inyungu yacu ingana.


Tumaze gukora ibice vyose vy’ubutumwa, duca dufatanya agaciro ka nyuma k’ibihinduka $A$, $B$, $C$, $D$, $E$, $F$, $G$, na $H$ kugira ngo dukore Hash ya nyuma y’ibice 256 y’igikorwa cacu co gukora hashing:


$$

\text{Hash} = A \Vert B \Vert C \Vert D \Vert E \Vert F \Vert G \Vert H


$$


Buri mpinduka ni umubare wose w'ibice 32, rero gufatanya kwabo kwama gutanga igisubizo c'ibice 256, ata kuraba ubunini bw'ubutumwa bwacu bwinjiza mu gikorwa co gukora hashing.


### Gushingira intahe imiterere y'ibanga


Ariko none, ni gute iyo nzira idashobora gusubirwamwo, idashobora gutombora, kandi idashobora guhindurwa?


Ku bijanye n’ukudashobora guhindurwa, biroroshe cane gutahura. Hariho imibare myinshi ikorwa mu buryo bw’uruzitiro, ivana n’ivyo winjiza be n’ivyo bihoraho, ku buryo guhindura gatoyi ubutumwa bwa mbere bihindura burundu inzira yafashwe, gutyo bigahindura burundu igisohoka Hash. Ivyo ni vyo vyitwa ingaruka y’urubura. Ivyo bimenyetso bimwe bimwe bishikirizwa n’uguvanga ivy’imbere n’ivy’intango ku gice kimwekimwe cose.

Igikurikira, iyo turiko turaganira ku gikorwa c'ubuhinga bwa Hash, ijambo "irreversibility" ntirikoreshwa muri rusangi. Ahubwo, tuvuga ivyerekeye "preimage resistance," ivyo bikaba bisobanura ko ku $y$ iyo ari yo yose, bigoye kuronka $x$ ku buryo $h(x) = y$. Ukwo guhangana n’ishusho y’imbere y’igihe biremezwa n’ugusobanuka kw’imibare n’ukudakorana kw’umurongo gukomeye kw’ibikorwa bikorwa mu gikorwa co gufatanya, be n’ugutakaza amakuru amwamwe mu gihe c’ivyo bikorwa. Nk'akarorero, ku gisubizo c'inyongezo modulo, hariho ibikorwa vyinshi bishoboka:


$$

3+2 \mod 10 = 5 \\
7+8 \mod 10 = 5 \\
5+10 \mod 10 = 5


$$


Muri aka karorero, umuntu azi gusa modulo ikoreshwa (10) n’igisubizo (5), ntashobora kumenya ata gukeka ko ari ibihe bikoreshwa mu kwongerako. Bivugwa ko hariho ibintu vyinshi bihuye modulo 10.


Ku bijanye n’igikorwa ca XOR, natwe turahura n’ingorane imwe. Ibuka imbonerahamwe y'ukuri y'iki gikorwa: igisohoka cose c'ibice 1 gishobora kumenyekana n'imiterere ibiri itandukanye y'inyungu ifise ubushobozi bumwe bwo kuba agaciro kabereye. Rero, umuntu ntashobora kumenya ata gukeka ibikorwa vya XOR mu kumenya gusa igisubizo caco. Iyo twongereye ubunini bw’ibikorwa vya XOR, umubare w’ibintu bishoboka vyinjizwa bizi gusa igisubizo uragwira cane. Ikindi, XOR ikoreshwa kenshi iruhande y'ibindi bikorwa vyo ku rugero rw'ibice, nk'igikorwa ca $\text{RotR}$, ivyongera mbere n'insobanuro zishoboka ku gisubizo.


Igikorwa co gufatanya naco gikoresha igikorwa ca $\text{ShR}$. Iryo koraniro rikuraho igice c’amakuru y’ishimikiro, ayo makuru rero ntashobora kuyaronka mu nyuma. Na none, nta buryo bw’aligebra bwo guhindura iyo nzira. Ivyo bikorwa vyose vy’inzira imwe n’ivy’ugutakaza amakuru bikoreshwa kenshi cane mu bikorwa vy’ugufatanya. Umubare w’ibintu bishoboka vyinjizwa ku gisohoka kimwe rero ni hafi y’aho ata n’iherezo ugira, kandi igihe cose umuntu agerageje guharura mu buryo butari bwo, vyotuma habaho ingano zifise umubare munini cane w’ibintu bitazwi, ivyo bikaba vyokwongerekana cane ku ntambwe yose.


Ubwa nyuma, ku bijanye n’akaranga k’uguhangana n’ugutombora, hariho ibintu vyinshi biza mu kibanza. Gutegura ubutumwa bw’intango imbere y’igihe birafise uruhara runini. Hatariho iyo nzira y'imbere, vyoshobora kworoha kuronka amatombora ku gikorwa. Naho, mu vyiyumviro, hariho ugutombora (bivuye ku ngingo ngenderwako y’inuma), imiterere y’igikorwa ca Hash, ifatanijwe n’ibintu twavuze haruguru, bituma ubushobozi bwo kuronka ugutombora buba buke cane.

Kugira ngo igikorwa ca Hash kibe gishobora guhangana n’ugutomboka, ni ngombwa ko:



- Ico kivamwo ntigishobora kumenyekana: Ugushobora kumenyekana kwose kurashobora gukoreshwa kugira ngo umuntu aronke amatombora vyihuta kuruta iyo umuntu akoresheje igitero c’inkomezi z’agahomerabunwa. Igikorwa kigaragaza ko igice cose c'isohoka kivana mu buryo butagira akamaro ku vyo winjiza. Mu yandi majambo, igikorwa gitegekanijwe ku buryo igice cose c'igisubizo ca nyuma gifise ubushobozi bwigenga bwo kuba 0 canke 1, naho ubwo bwigenga butari ubw'ukuri mu bikorwa.
- Ugukwiragizwa kw’ama hashes ni pseudo-random: Ivyo bituma ama hashes akwiragizwa mu buryo bumwe.
- Ubwinshi bwa Hash ni bwinshi cane: uko umwanya ushoboka wo gushiramwo ibisubizo uba munini, ni ko bigorana kuronka aho ihuriye.


Abahinga mu vy’ubuhinga bwa cryptography barahingura ivyo bikorwa mu gusuzuma ibitero vyiza kuruta ibindi vyose kugira ngo bashobore kuronka aho bihuriye, hanyuma bagahindura ibipimo kugira ngo ivyo bitero ntibibe vyiza.


### Ubwubatsi bwa Merkle-Damgård


Igishushanyo ca SHA256 gishingiye ku nyubakwa ya Merkle-Damgård, ishobora guhindura igikorwa co gufatanya mu gikorwa ca Hash gishobora gukora ubutumwa bw’uburebure butari bwo. Ivyo nyene ni vyo twabonye muri iki kigabane.


Ariko rero, ibikorwa bimwe bimwe vya kera vya Hash nka SHA1 canke MD5, bikoresha iyo nyubakwa yihariye, birashobora guterwa n’ibitero vy’ukwagura uburebure. Ubu ni ubuhinga butuma umuterabwoba azi Hash y’ubutumwa $M$ n’uburebure bwa $M$ (atazi ubutumwa ubwabwo) ashobora kubara Hash y’ubutumwa $M’$ bwakozwe mu gufatanya $M$ n’ibindi birimwo.


SHA256, naho ikoresha ubwoko bumwe bw'ubwubatsi, mu vyiyumviro irashobora guhangana n'ubwo bwoko bw'igitero, bitandukanye na SHA1 na MD5. Ivyo vyoshobora gusigura akabanga k’ugucapura kabiri kwashizwe mu ngiro muri Bitcoin yose na Satoshi Nakamoto. Kugira ngo umuntu yirinde ubwo bwoko bw’igitero, Satoshi yoba yarahisemwo gukoresha SHA256 ibiri:


$$

\text{HASH256}(m) = \text{SHA256}(\text{SHA256}(m))


$$


Ivyo bituma haba umutekano mwinshi ku bitero bishobora kuba bifitaniye isano n’ubwubatsi bwa Merkle-Damgård, ariko ntivyongera umutekano w’uburyo bwo gukora hashing mu bijanye no guhangana n’ugutombora. Ikindi kandi, naho SHA256 yoba yarashikiwe n’ubwo bwoko bw’igitero, ntiyari kugira ingaruka zikomeye, kuko ibikorwa vyose vya Hash muri Bitcoin birimwo amakuru ya bose. Ariko rero, igitero co kwagura uburebure coshobora kuba ngirakamaro gusa ku muntu atera iyo amakuru ya hashed ari ay’ibanga kandi uwukoresha yakoresheje igikorwa ca Hash nk’uburyo bwo kwemeza ayo makuru, nk’uko bigenda kuri MAC. Gutyo, ugushirwa mu ngiro kw’ugukora hashing kabiri biracari ikinyegezwa mu guhingura Bitcoin.

Ubu ko twabonye mu buryo burambuye ingene ibikorwa vya Hash bikora, cane cane SHA256, ikoreshwa cane muri Bitcoin, tuzokwibanda cane ku mirongo y’ugukuraho amakuru y’ibanga ikoreshwa ku rugero rw’ibikorwa, cane cane mu gukuraho imfunguruzo za Wallet yawe.


## Ubuhinga bukoreshwa mu gukuraho


<chapterId>cc668121-7789-5e99-bf5e-1ba085f4f5f2</chapterId>


Mu Bitcoin ku rugero rw’ibikorwa, uretse ibikorwa vya Hash, ubuhinga bwo gukuraho amakuru bukoreshwa kugira ngo generate ikingire amakuru ava ku vyo yinjije mu ntango. Naho izo algorithme zishingiye ku bikorwa vya Hash, zikora intumbero zitandukanye, cane cane mu bijanye no kwemeza ko umuntu ari uwuriho no gutanga urufunguzo. Izo algorithme zigumya bimwe mu biranga ibikorwa vya Hash, nk’ukudashobora gusubira inyuma, ukudashobora guhindurwa, n’ukudashobora gutombora.


Mu bikoresho vya Bitcoin, ahanini hakoreshwa ubuhinga 2 bwo gukura:



- **HMAC (_Kode y'ukwemeza ubutumwa bushingiye kuri Hash_)**
- **PBKDF2** (_Ijambobanga-rishingiye ku rufunguzo rwo gukuraho umurimo 2_)


Tuzosuzuma hamwe ingene umwe wese muri bo akora n’uruhara afise.


### HMAC-SHA512


HMAC ni ubuhinga bwo guharura kode y’ukwemeza ishingiye ku guhuza igikorwa ca Hash n’urufunguzo rw’ibanga. Bitcoin ikoresha HMAC-SHA512, uburyo butandukanye bwa HMAC bukoresha igikorwa ca SHA512 Hash. Twaramaze kubona mu gice ca mbere ko SHA512 iri mu muryango umwe w’ibikorwa vya Hash na SHA256, ariko itanga umusaruro w’ibice 512.


Aha niho umugambi wayo rusangi w'ibikorwa $m$ ari ubutumwa bw'injiza na $K$ urufunguzo rw'ibanga:


![CYP201](assets/fr/011.webp)


Reka twige mu buryo burambuye ibiba muri aka gasandugu k’umwirabura ka HMAC-SHA512. HMAC-SHA512 ikorana na:



- $m$: ubutumwa bufise ubunini butari bwo bwatowe n'ukoresha (injiza ya mbere);
- $K$: urufunguzo rw'ibanga rw'ububisha rwatowe n'ukoresha (injiza ya kabiri);
- $K'$: urufunguzo $K$ rwahinduwe ku rugero $B$ rw'ibice vy'ibikorwa vya Hash (ibice 1024 vya SHA512, canke ibice 128);
- $ \ umwandiko{SHA512}$: igikorwa ca SHA512 Hash;
- $\oplus$: igikorwa ca XOR (kidasanzwe canke);
- $\Vert$: umukozi w'uguhuza, guhuza imirongo y'ibice kuva ku mpera kugeza ku mpera;
- $\umwandiko{opad}$: ihoraho igizwe na byte $0x5c$ isubirwamwo incuro 128
- $\text{ipad}$: ikintu kidahinduka gikozwe na byte $0x36$ isubirwamwo incuro 128.


Imbere yo kubara HMAC, birakenewe ko urufunguzo n’ibidahinduka bingana hakurikijwe ubunini bw’ibarabara $B$. Nk'akarorero, iyo urufunguzo $K$ ari rugufi kuruta 128 bytes, rushirwako zero kugira ngo rushike ku bunini $B$. Iyo $K$ ari ndende kuruta 128 bytes, irafatwa hakoreshejwe SHA512, hanyuma zeros zigashirwako gushika ishitse kuri 128 bytes. Muri ubwo buryo, urufunguzo rungana rwitwa $K'$ ruraboneka. Agaciro ka $\inyandiko{opad}$ na $\inyandiko{ipad}$ kaboneka mu gusubiramwo byte yabo y'ishimikiro ($0x5c$ ku $\inyandiko{opad}$, $0x36$ ku $\inyandiko{ipad}$) gushika ubunini $B$ bushitse. Gutyo, n'amabayiti $B = 128$, dufise:


$$

\text{opad} = \underbrace{0x5c5c\ldots5c}\_{128 \  \text{bytes}}


$$


Igihe ivy’ugutegura imbere y’igihe bimaze gukorwa, ubuhinga bwa HMAC-SHA512 burasobanurwa n’iyi nsiguro ikurikira:


$$

\text{HMAC-SHA512}(K,m) = \text{SHA512} \left( (K' \oplus \text{opad}) \parallel \text{SHA512} \left( (K' \oplus \text{ipad}) \parallel m \right) \right)


$$


Iyi nkuru igabanywamwo intambwe zikurikira:



- XOR urufunguzo rwahinduwe $K'$ n'$\umwandiko{ipad}$ kugira ngo ubone $\umwandiko{iKpad}$;
- XOR urufunguzo rwahinduwe $K'$ n' $\umwandiko{opad}$ kugira ngo ubone $\umwandiko{oKpad}$;
- Gufatanya $\umwandiko{iKpad}$ n'ubutumwa $m$.
- Hash iki gisubizo na SHA512 kugira ngo uronke Hash $H_1$ yo hagati.
- Gufatanya $\umwandiko{oKpad}$ na $H_1$.
- Hash iki gisubizo na SHA512 kugira ngo ubone igisubizo ca nyuma $H_2$.


Izo ntambwe zishobora gusobanurwamwo mu ncamake nk’uko bikurikira:


![CYP201](assets/fr/012.webp)


HMAC ikoreshwa muri Bitcoin cane cane mu gukura urufunguzo mu bikoresho vya HD (Hierarchical Deterministic) (tuzobivuga mu buryo burambuye mu bice biza) kandi nk'igice ca PBKDF2.


### PBKDF2


PBKDF2 (_Igikorwa co gukuraho urufunguzo rushingiye ku majambobanga 2_) ni ubuhinga bwo gukuraho urufunguzo bwagenewe kwongereza umutekano w'amajambobanga. Iryo koraniro rikoresha igikorwa c’ubuhendanyi (aha HMAC-SHA512) ku jambobanga n’umunyu w’ibanga, hanyuma rigasubiramwo iyo nzira incuro zinaka kugira ngo rivemwo urufunguzo rw’isohoka.


Mu Bitcoin, PBKDF2 ikoreshwa mu generate seed ya HD Wallet ivuye mu mvugo ya Mnemonic n’iyi passphrase (ariko ivyo tuzobivuga mu buryo burambuye mu bice bizoza).


Inzira ya PBKDF2 ni iyi, n’:



- $m$: ijambo ry'umukoresha Mnemonic;
- $s$: passphrase y'ubusa kugira ngo wongere umutekano (ubusa iyo ata passphrase);
- $n$: umubare w'ibisubirwamwo vy'igikorwa, mu gihe cacu, ni 2048.


Igikor ca PBKDF2 gisobanurwa mu buryo busubiramwo. Isubiramwo ryose rifata igisubizo c’iry’imbere, rikayica muri HMAC-SHA512, rikafatanya ibisubizo bikurikirana kugira ngo rivemwo urufunguzo rwa nyuma:


$$

\text{PBKDF2}(m, s) = \text{HMAC-SHA512}^{2048}(m, s)


$$


Mu buryo bw’igishushanyo, PBKDF2 ishobora guserurwa gutya:


![CYP201](assets/fr/013.webp)


Muri iki gice, twasuzumye ibikorwa vya HMAC-SHA512 na PBKDF2, bikoresha ibikorwa vy’ugukora hashing kugira ngo bimenye neza ubutungane n’umutekano w’ibikomoka ku bintu nyamukuru biri mu masezerano ya Bitcoin. Mu gice gikurikira, turaza kuraba imikono y’ubuhinga bwa none, ubundi buryo bwo gukora amakuru bukoreshwa cane muri Bitcoin.


# Imikono ya digitale


<partId>76b58a00-0c18-54b9-870d-6b7e34029db8</partId>


## Imikono ya digitale n'imirongo y'imirongo


<chapterId>c9dd9672-6da1-57f8-9871-8b28994d4c1a</chapterId>


Uburyo bwa kabiri bwo gukora amakuru y’ibanga bukoreshwa muri Bitcoin bujanye n’ubuhinga bwo gushiramwo amasinya y’inyandiko. Reka turabe ivyo ivyo birimwo n’ingene bikora.


### Bitcoins, UTXOs, n'Ivyangombwa vyo Gukoresha


Ijambo "_wallet_" muri Bitcoin rishobora gutera urujijo cane ku batangura. Nkako, ico bita Bitcoin Wallet ni porogarama idafata ata guca ku ruhande amafaranga yawe y’ibiceri, bitandukanye n’ivyo Wallet y’umubiri ishobora gufata amafaranga canke amafaranga. Bitcoins ni ibice vy’ikonti gusa. Iyi konti igereranywa na **UTXO** (_Ibiva mu bikorwa bitakoreshejwe_), ari vyo biva mu bikorwa bitakoreshejwe. Iyo ivyo bisohoka bitakoreshejwe, bisigura ko ari ivy’ukoresha. UTXOs ni, mu buryo bumwe, ibice vy’ama bitcoins, vy’ubunini buhinduka, vy’umuntu akoresha.


Iryo tegeko rya Bitcoin rirakwiragizwa kandi rikora ata butegetsi bukuru. Ntibimeze rero nk’ibitabo vya kera vyo mu mabanki, aho amayero ari ayawe afatanijwe gusa n’akaranga kawe bwite. Muri Bitcoin, ama UTXO yawe ni ayawe kuko arindwa n’ivyo gukoresha amahera bivugwa mu rurimi rw’Inyandiko. Kugira ngo vyorohe, hari ubwoko bubiri bw’inyandiko: inyandiko yo gufunga (_scriptPubKey_), irinda UTXO, n’inyandiko yo gufungura (_scriptSig_), ishobora gufungura UTXO gutyo igakoresha ibice vya Bitcoin iserukira.

Ibikorwa vya mbere vya Bitcoin n’inyandiko za P2PK birimwo gukoresha urufunguzo rwa bose kugira ngo ufunge amahera, ugaragaza mu _scriptPubKey_ ko umuntu yipfuza gukoresha iyi UTXO ategerezwa gutanga umukono ubereye n’urufunguzo rw’ibanga rujanye n’urwo rufunguzo rwa bose. Kugira ngo ufungure iyi UTXO, birakenewe rero ko utanga umukono ubereye muri _scriptSig_. Nk’uko amazina yabo abivuga, urufunguzo rwa bose rurazwi na bose kuko ruca kuri Blockchain, mu gihe urufunguzo rw’ibanga ruzwi gusa n’uwufise ayo mahera mu buryo bubereye.

Ivyo ni vyo bikoresho vy’ishimikiro vya Bitcoin, ariko uko igihe cagenda kirarenga, ivyo bikorwa vyararushirije kuba bikomeye. Ubwa mbere, Satoshi nayo yashizeho inyandiko za P2PKH, zikoresha Address yakira muri _scriptPubKey_, iserukira Hash y'urufunguzo rwa bose. Hanyuma, iyo nzira yararushirije kugorana igihe haza SegWit hanyuma Taproot. Ariko rero, ingingo ngenderwako rusangi iguma ari imwe mu ntango: urufunguzo rwa bose canke igiserukira urwo rufunguzo ni co gikoreshwa mu gufunga UTXO, kandi urufunguzo rw’ibanga ruhuye n’urwo rurakenewe kugira ngo umuntu afungure gutyo akoreshe.


Uwukoresha yipfuza gukora igikorwa co gucuruza Bitcoin ategerezwa rero gukora umukono wa digitale akoresheje urufunguzo rwiwe rw’ibanga ku gicuruzwa. Iryo sinya rishobora kugenzurwa n’abandi bari muri iyo nzira. Iyo ari ngirakamaro, ivyo bisigura ko uwukoresha atanguye gukora ari we vy’ukuri afise urufunguzo rw’ibanga, rero ni we afise ama bitcoins bipfuza gukoresha. Abandi bakoresha barashobora rero kwemera no gukwiragiza iyo nzira.


Ivyo bituma uwukoresha amafaranga yitwa bitcoins yugarijwe n’urufunguzo rwa bose ategerezwa kurondera uburyo bwo kubika neza ico kimufasha gufungura amahera yiwe: urufunguzo rw’ibanga. Bitcoin Wallet ni igikoresho nyaco kizotuma ushobora kubika imfunguruzo zawe zose mu buryo bworoshe ata bandi bantu bashobora kuzironka. Ni co gituma imeze nk’urufunguzo kuruta Wallet.


Ihuriro ry’imibare hagati y’urufunguzo rwa bose n’urufunguzo rw’ibanga, hamwe n’ubushobozi bwo gukora umukono kugira ngo umuntu yerekane ko afise urufunguzo rw’ibanga ataco ahishuriye, bishoboka biciye ku buhinga bwo gusinya mu buryo bwa digitale. Mu masezerano ya Bitcoin, hakoreshwa ubuhinga bubiri bwo gusinya: **ECDSA** (_Ubuhinga bwo gusinya bwa digitale_) na **Igishushanyo co gusinya ca Schnorr**. ECDSA ni porotokole y’umukono wa digitale ikoreshwa muri Bitcoin kuva mu ntango zayo. Schnorr ni yo iherutse gusohoka muri Bitcoin, nk’uko yashizweho mu kwezi kwa 11 2021 n’ivugurura rya Taproot.

Izo algorithme zibiri zirasa cane mu buryo zikora. Ivyo vyose bishingiye ku buhinga bwo gukingira amabara y’uruzitiro. Itandukaniro rikomeye hagati y’izo porotokole zibiri riri mu mibumbe y’umukono be n’ibintu bimwebimwe vy’imibare vyihariye. Tuzokwiga rero ingene izo nzira zikora, dutangurire ku rwa kera cane: ECDSA.


### Ugupfuka kw'ibara ry'umuhondo


Elliptic Curve Cryptography (ECC) ni urutonde rw’ubuhinga bukoresha umurongo w’uruzitiro kubera imiterere yayo itandukanye y’imibare n’ubuhinga bw’ubuhinga bw’ubuhinga bw’ubuhinga bw’ubuhinga. Umutekano w’izo nzira ushingiye ku ngorane z’ingorane y’ubuhinga bwa logarithme butandukanye ku nzira zigoramye. Ivyiyumviro vy'uruzitiro bikoreshwa cane cane mu guhindura urufunguzo, mu gushiramwo amakuru ataringaniye, canke mu guhingura imikono y'ubuhinga bwa none.


Ikintu gihambaye kiranga izo nzira ni uko zihuye n’umurongo wa x. Gutyo, umurongo wose udahagaze uca umurongo w’umurongo ku ntumbero zibiri zitandukanye uzokwama uca umurongo w’umurongo ku ntumbero ya gatatu. Ikindi kandi, tangente iyo ari yo yose y’umurongo w’umurongo ku ntumbero itari imwe izoca n’umurongo w’umurongo ku yindi ntumbero. Ivyo bizogira akamaro mu gusobanura ibikorwa ku nzira.


Aha niho hagaragazwa umurongo w'uruzitiro hejuru y'imibare nyayo:


![CYP201](assets/fr/014.webp)


Buri mugongo w'uruzitiro usobanurwa n'ingero y'uburyo:


$$

y^2 = x^3 + ax + b


$$


### igice256k1


Kugira ngo umuntu akoreshe ECDSA canke Schnorr, ategerezwa guhitamwo ibipimo vy’umurongo w’uruzitiro, ni ukuvuga agaciro ka $a$ na $b$ mu nsiguro y’uruzitiro. Hariho ingingo mfatirwako zitandukanye z’ibigobe vy’imirongo y’imirongo bivugwa ko zitekanye mu buryo bw’ibanga. Igizwi cane ni _secp256r1_ curve, gisobanurwa kandi gishimikijwe na NIST (_Ikigo c’Igihugu c’Imirongo ngenderwako n’Ikoranabuhanga_).


Naho vyari ukwo, Satoshi Nakamoto, uwahinguye Bitcoin, yahisemwo kudakoresha iyo nzira y’umurongo. Impamvu y’iryo hitamwo ntiramenyekana, ariko bamwe bemera ko yahisemwo kurondera ubundi buryo kuko amaparametere y’iyi nzira yoshobora kubamwo urugi rw’inyuma. Ahubwo, umurongo wa Bitcoin ukoresha umurongo w'umurongo **_secp256k1_**. Iyi nzira isobanurwa n'ibipimo $a = 0$ na $b = 7$. Ingano yayo rero ni:


$$

y^2 = x^3 + 7


$$


Igishushanyo caco kigaragaza hejuru y'imibare nyayo kimeze gutya:


![CYP201](assets/fr/015.webp)


Ariko rero, mu vy’ubuhinga bwo gupfuka amakuru, dukorana n’imibare ifise iherezo. Mu buryo butomoye, dukora ku kibanza gifise impera $\mathbb{F}_p$, ari co kibanza c'imibare yose modulo umubare w'intango $p$.

**Insobanuro**: Umubare w'intango ni umubare w'inzira kamere uruta canke ungana na 2 ufise gusa ibice bibiri bitandukanye vy'umubare w'inzira nziza: 1 na wo nyene. Nk'akarorero, umubare 7 ni umubare w'intango kuko ushobora kugabanywa na 1 na 7 gusa. Ku rundi ruhande, umubare 8 si umubare w'intango kuko ushobora kugabanywa na 1, 2, 4, na 8.

Muri Bitcoin, umubare w’intango $p$ ukoreshwa mu gusobanura umurima ufise impera ni munini cane. Itoranywa mu buryo bw’uko urutonde rw’umurima (ni ukuvuga, umubare wa Elements muri $\mathbb{F}_p$) ari munini bihagije kugira ngo umutekano w’ibanga ubeho.


Umubare w'intango $p$ ukoreshwa ni:


```text
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
```


Mu kwandika kw'icumi, ibi bihuye na:


$$

p = 2^{256} - 2^{32} - 977


$$


Rero, ingano y’umurongo wacu w’uruzitiro ni:


$$

y^2 \equiv x^3 + 7 \mod p


$$


Kubera ko iyo nzira isobanurwa hejuru y’umurima w’iherezo $\mathbb{F}_p$, ntikigisa n’inzira ikomeza ahubwo isa n’umugwi w’intonde zitandukanye. Nk’akarorero, ng’uko uko umurongo ukoreshwa muri Bitcoin usa ku $p = 17$ nto cane:


![CYP201](assets/fr/016.webp)


Muri aka karorero, nashizeho n’ibigirankana umurima ufise impera ku $p = 17$ kubera imvo z’inyigisho, ariko umuntu ategerezwa kwiyumvira ko uwo ukoreshwa muri Bitcoin ari munini cane, hafi $2^{256}$.


Dukoresha umurima ufise impera w’imibare yose modulo $p$ kugira ngo twiyemeze ko ibikorwa ku nzira y’umurongo ari ukuri. Nkako, imirongo y’imirongo y’imirongo y’imirongo iri hejuru y’ibarabara ry’imibare nyayo irashobora gushikirwa n’ukudatahura neza kubera amakosa yo gukikuza mu gihe c’imibare y’imibare. Iyo hakozwe ibikorwa vyinshi ku nzira y’umurongo, ayo makosa ararundanywa maze igisubizo ca nyuma gishobora kuba kitari co canke kigoye gusubiramwo. Gukoresha gusa imibare yose y’ukuri bituma imibare igira ukuri gutunganye, gutyo rero igisubizo kikaba gishobora gusubirwamwo.


Imibare y'imirongo y'uruzitiro ku bibanza bifise impera isa n'iyo ku bibanza vy'imibare nyayo, n'uguhindura ko ibikorwa vyose bikorwa modulo $p$. Kugira ngo tworohereze insobanuro, tuzobandanya mu bigabane bikurikira kwerekana ivyiyumviro dukoresheje umurongo usobanuwe ku mibare nyayo, mu gihe tuzirikana ko, mu bikorwa, umurongo usobanurwa ku kibanza gifise impera.


Niba wipfuza kumenya vyinshi ku bijanye n’imishinge y’imibare y’ubuhinga bwa none bwo gukingira amakuru, ndagusavye kandi kuraba iyi yindi nyigisho iri kuri Plan ₿ Network:


https://planb.network/courses/d2fd9fc0-d9ed-4a87-9fa3-0fdbb3937e28

## Guharura urufunguzo rwa bose kuva ku rufunguzo rw'ibanga


<chapterId>fcb2bd58-5dda-5ecf-bb8f-ad1a0561ab4a</chapterId>

Nk’uko twabibonye mbere, ubuhinga bwo gusinya mu buryo bwa digitale muri Bitcoin bushingiye ku mfunguruzo zibiri z’ibanga n’iz’abantu bose zifitaniye isano n’imibare. Reka dusuzume hamwe ico iyo nzira y’imibare ari co n’ingene ivyara.


### Urufunguzo rw'ibanga


Urufunguzo rw’ibanga ni umubare gusa w’imburakimazi canke w’imburakimazi. Ku bijanye na Bitcoin, uwo mubare ufise ubunini bw’ibice 256. Umubare w'ibishoboka vy'urufunguzo rw'ibanga rwa Bitcoin rero ni $2^{256}$.


**Iciyumviro**: "Umubare w'ibinyoma" ni umubare ufise imiterere iri hafi y'umubare w'ibinyoma vy'ukuri ariko ukaba uterwa n'ubuhinga bwo gupima.


Ariko mu bikorwa, hariho gusa $n$ uturongo dutandukanye ku nzira yacu y’uruzitiro secp256k1, aho $n$ ari urutonde rw’inzira y’umuyagankuba $G$ y’uruzitiro. Tuzobona mu nyuma ico uwo mubare uhuye, ariko wibuke gusa ko urufunguzo rw’ibanga rufise akamaro ari umubare wose uri hagati ya $1$ na $n-1$, tuzi ko $n$ ari umubare uri hafi ariko uri munsi gatoyi ya $2^{256}$. Rero, hariho imibare imwe imwe y'ibice 256 idafise akamaro ko kuba urufunguzo rw'ibanga muri Bitcoin, cane cane, imibare yose iri hagati ya $n$ na $2^{256}$. Iyo ivyara vy'umubare w'imburakimazi (urufunguzo rw'ibanga) bitanga agaciro $k$ ku buryo $k \geq n$, bifatwa nk'ibidafise akamaro, kandi agaciro gashasha k'imburakimazi gategerezwa gushirwaho.


Umubare w'ibishoboka vy'urufunguzo rw'ibanga rwa Bitcoin rero ni nk'$n$, ari wo mubare uri hafi y'$1.158 \incuro 10^{77}$. Uwo mubare ni munini cane ku buryo iyo uhisemwo urufunguzo rw’ibanga mu buryo bw’impfagusa, mu mibare hafi bidashoboka ko ushika ku rufunguzo rw’ibanga rw’uwundi muntu akoresha. Kugira ngo ubone iciyumviro c’urugero, igitigiri c’imfunguruzo z’ibanga zishoboka ziri muri Bitcoin ni urutonde rw’ubunini rwo hafi y’urw’amaatome agereranywa ari mw’isanzure ry’ikirere rishobora kwihwezwa.


Nk’uko tuzobibona mu bice bizoza, uno musi, imfunguruzo nyinshi z’ibanga zikoreshwa muri Bitcoin ntizivugwa mu buryo bw’impfagusa ahubwo ni ingaruka y’ugukomoka kw’ibintu biva ku nsiguro ya Mnemonic, ubwayo ikaba ari pseudo-random (iryo ni ryo jambo rizwi cane ry’amajambo 12 canke 24). Aya makuru ntaco ahindura ku gukoresha ubuhinga bwo gusinya nka ECDSA, ariko afasha gusubira kwibanda ku gukwiragiza kwacu muri Bitcoin.


Ku bindi bisobanuro, urufunguzo rw'ibanga ruzogaragazwa n'urudome ruto $k$.


### Urufunguzo rwa bose


Urufunguzo rwa bose ni akarongo kari ku nzira y'uruzitiro, rwerekanwa n'urudome runini $K$, kandi ruharurwa ku rufunguzo rw'ibanga $k$. Iyi nkuru $K$ igereranywa n’ibiharuro bibiri $(x, y)$ ku nzira y’uruzitiro, igiharuro cose kikaba ari umubare wose modulo $p$, umubare w’intango usobanura umwanya w’iherezo $\mathbb{F}_p$.

Mu bikorwa, urufunguzo rwa bose rudafise ubushobozi bwo gukora rugereranywa n’ibice 520 (canke 65 bytes), bihuye n’imibare ibiri y’ibice 256 ($x$ na $y$) ishizwe ku mpera ku mpera, itangurizwa n’intango y’ibice 8 $0x04$.


Ariko kandi, birashoboka guserukira urufunguzo rwa bose mu buryo bupfutse hakoreshejwe gusa ama byte 33 (ibice 264) mu kugumiza gusa abscissa $x$ y’akarongo kacu ku nzira y’umurongo n’ama byte yerekana uburinganire bwa $y$. Ivyo ni vyo bizwi nk’urufunguzo rwa bose rwacitse. Ivyo nzobivuga cane mu bice vya nyuma vy’iri huriro. Ariko ico ukwiye kwibuka ni uko urufunguzo rwa bose $K$ ari akarongo kadondorwa na $x$ na $y$.


Kugira ngo tubare akarongo $K$ gahuye n’urufunguzo rwacu rwa bose, dukoresha igikorwa co gukubita kw’ibiharuro ku bipimo vy’imirongo, bisobanurwa nk’ugusubiramwo ($k$ incuro) kw’akarongo k’umuyagankuba $G$:


$$

K = k \cdot G


$$


hehe:



- $k$ ni urufunguzo rw'ibanga (umubare wose w'imburakimazi uri hagati ya $1$ na $n-1$);
- $G$ ni umurongo w’umuyagankuba w’umurongo w’uruzitiro ukoreshwa n’abaje bose mu rubuga rwa Bitcoin;
- $\cdot$ igereranya ugukubita kw'ibiharuro ku nzira y'uruzitiro, bikaba bingana no kwongerako akarongo $G$ kuri yo nyene incuro $k$.


Kuba iyo nkuru $G$ ihurikiye ku mfunguruzo zose za bose muri Bitcoin bituma twizigira ko urwo rufunguzo rw’ibanga rumwe $k$ ruzokwama ruduha urufunguzo rwa bose rumwe $K$:


![CYP201](assets/fr/017.webp)


Ikintu nyamukuru kiranga iyo nzira ni uko ari igikorwa c’inzira imwe. Biroroshe kubara urufunguzo rwa bose $K$ uzi urufunguzo rw’ibanga $k$ n’inzira y’umuyagankuba $G$, ariko mu vy’ukuri ntibishoboka kubara urufunguzo rw’ibanga $k$ uzi urufunguzo rwa bose $K$ n’inzira y’umuyagankuba $G$ gusa. Kuronka $k$ muri $K$ na $G$ bingana no gutorera umuti ingorane ya logarithme itandukanye ku mirongo y’imirongo, ingorane igoye mu mibare ata algorithme nziza izwi. Mbere n’ibiharuro bikomeye cane vyo muri iki gihe ntibishobora gutorera umuti ico kibazo mu kiringo gikwiriye.


![CYP201](assets/fr/018.webp)


### Kwongerako n'ugukubita kabiri uturongo ku mirongo y'imirongo


Iciyumviro co kwongerako ku bigobe vy’uruzitiro gisobanurwa mu buryo bw’ubuhinga. Iyo dufise uturongo tubiri $P$ na $Q$ ku nzira y’umurongo, igikorwa $P + Q$ giharurwa mu guca umurongo uca muri $P$ na $Q$. Uyu murongo uzoca ku nzira y'umurongo ku ntumbero ya gatatu $R'$. Turaheza dufate ishusho y’indorerwamo y’iyi nkuru ku bijanye n’umurongo wa x kugira ngo turonke inkuru $R$, ari yo ngaruka y’ukwongerako:


$$

P + Q = R


$$


Mu buryo bw’ikigereranyo, ivyo bishobora guserurwa gutya:


![CYP201](assets/fr/019.webp)


Ku bijanye n’ugukubita kabiri kw’akarongo, ni ukuvuga igikorwa $P + P$, duca ducapura tangente ku nzira y’umurongo ku karongo $P$. Iryo tangente rica ku nzira y'umurongo ku kindi kibanza $S'$. Turaheza dufate ishusho y’indorerwamo y’iyi nkuru ku bijanye n’umurongo wa x kugira ngo turonke inkuru $S$, ari yo ngaruka y’ugukubita kabiri:


$$

2P = S


$$


Mu gishushanyo, ibi vyerekanwa nk'ibi:


![CYP201](assets/fr/020.webp)


Dukoresheje izo bikorwa vyo kwongerako no gukubita kabiri, turashobora gukora ugukubita kw’akarongo n’umubare wose $k$, ugaragazwa na $kP$, dukoresheje ugukubita kabiri n’ugukubita kabiri.


Nk’akarorero, dufate ko twahisemwo urufunguzo rw’ibanga $k = 4$. Kugira ngo tubaze urufunguzo rwa bose rufitaniye isano, dukora:


$$

K = k \cdot G = 4G


$$


Mu buryo bw'ikigereranyo, ivyo bihuye no gukora urutonde rw'ivyo kwongerako n'ivyo gukubita kabiri:



- Harura $2G$ mu gukubita kabiri $G$.
- Harura $4G$ mu gukubita kabiri $2G$.


![CYP201](assets/fr/021.webp)


Niba twipfuza nk’akarorero kubara akarongo $3G$, dutegerezwa kubanza kubara akarongo $2G$ mu gukubita kabiri akarongo $G$, hanyuma tukongerako $G$ na $2G$. Kugira ngo wongereko $G$ na $2G$, ushobora gusa guca umurongo uhuza izo nkuru zibiri, ugatora inkuru yihariye $-3G$ ku mahuriro hagati y’uwo murongo n’umurongo w’uruzitiro, hanyuma umenye $3G$ nk’ikinyuranyo ca $-3G$.


Tuzogira:


$$

G + G = 2G


$$


$$

2G + G = 3G


$$


Mu buryo bw’ikigereranyo, ivyo vyogereranywa gutya:


![CYP201](assets/fr/022.webp)


### Umurimo w'inzira imwe


Kubera ivyo bikorwa, turashobora gutahura igituma vyoroshe gukura urufunguzo rwa bose mu rufunguzo rw’ibanga, ariko ivyo bihushanye n’ivyo ntibishoboka.


Reka dusubire ku karorero kacu koroshe. N'urufunguzo rw'ibanga $k = 4$. Kugira ubaze urufunguzo rwa bose rufitaniye isano, dukora:


$$
K = k \cdot G = 4G
$$


Twarashoboye rero kubara mu buryo bworoshe urufunguzo rwa bose $K$ mu kumenya $k$ na $G$.


None, iyo umuntu azi urufunguzo rwa bose $K$ gusa, ahura n’ingorane y’ubuhinga bwa logarithme butandukanye: kuronka $k$ ku buryo $K = k \cdot G$. Ico kibazo kibonwa ko kigoye kubera ko ata nzira nziza yo kugitorera umuti ku bigobe vy’imirongo y’imirongo. Ivyo bituma haba umutekano w’ubuhinga bwa ECDSA na Schnorr.


Ego cane, muri aka karorero koroshe gafise $k = 4$, vyoshoboka ko umuntu aronka $k$ biciye mu kugerageza no gukosa, kuko umubare w’ibishoboka ari muto. Ariko mu bikorwa, $k$ ni umubare wose w’ibice 256, bikaba bituma umubare w’ibishoboka uba munini cane mu vy’inyenyeri (nk’amadolari 1.158 \incuro 10^{77}$). Ntibishoboka rero kuronka $k$ ku nguvu z’agahomerabunwa.


## Gusinya n'urufunguzo rw'ibanga


<chapterId>bb07826f-826e-5905-b307-3d82001fb778</chapterId>


Ubu ko uzi gukura urufunguzo rwa bose mu rufunguzo rw’ibanga, urashobora kuronka bitcoins ukoresheje uru rufunguzo rubiri nk’itegeko ryo gukoresha. Ariko none twozikoresha gute? Kugira ngo ukoreshe ama bitcoins, uzokenera gufungura _scriptPubKey_ ifashe kuri UTXO yawe kugira ngo werekane ko ari wewe vy’ukuri nyirayo. Kugira ngo ubikore, utegerezwa gutanga umukono $s$ uhuye n'urufunguzo rwa bose $K$ ruri muri _scriptPubKey_ ukoresheje urufunguzo rw'ibanga $k$ rwakoreshejwe mu ntango mu kubara $K$. Umukono wa digitale rero ni ikimenyamenya kidashobora guhakanwa c’uko ufise urufunguzo rw’ibanga rujanye n’urufunguzo rwa bose uvuga.


### Imirongo y'umugongo


Kugira ngo umuntu akore umukono w’ibarabara, abaje mu nama bose bategerezwa kubanza kwemeranya ku mirongo y’umurongo w’uruzitiro rwakoreshejwe. Ku bijanye na Bitcoin, ibipimo vya **secp256k1** ni ibi bikurikira:


Umurima ufise impera $\imibarebb{Z}_p$ usobanuwe na:


$$
p = 2^{256} - 2^{32} - 977
$$


```text
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
```


$p$ ni umubare munini cane w'intango uri munsi gato ya $2^{256}$.


Igicapo c'umurongo $y^2 = x^3 + ax + b$ hejuru ya $\imibarebb{Z}_p$ gisobanurwa na:


$$
a = 0, \quad b = 7
$$


Igikoresho c'umuyagankuba canke inkomoko $G$:


```text
G = 0x0279BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
```


Uwo mubare ni uburyo bupfutse butanga gusa abscisse y'akarongo $G$. Intangamarara `02` mu ntango igena mu mibare ibiri ifise iyo abscisse $x$ izokoreshwa nk'inzira y'ugutanga.

Urutonde $n$ rwa $G$ (umubare w'ibiharuro biriho) n'umufasha $h$:


```text
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
```


$n$ ni umubare munini cane uri munsi gato ya $p$.


$$
h=1
$$


$h$ ni cofactor canke umubare w'imigwi mitomito. Sinzosobanura neza ico ivyo bigereranya hano, kuko biragoye cane, kandi ku bijanye na Bitcoin, ntidukwiye kubizirikana kuko bingana n’amadolari 1.


Aya makuru yose ni aya bose kandi arazwi n’abaje muri iyo nama bose. Kubera bo, abakoresha barashobora gukora umukono wa digitale no kuwugenzura.


### Umukono na ECDSA


Ubuhinga bwa ECDSA buratuma uwukoresha ashobora gushirako umukono ku butumwa akoresheje urufunguzo rwiwe rw’ibanga, mu buryo umuntu wese azi urufunguzo rwa bose ruhuye n’urwo rufunguzo ashobora kugenzura ko uwo mukono ari ukuri, ata rufunguzo rw’ibanga rwigera rumenyekana. Mu bijanye na Bitcoin, ubutumwa buzoshirwako umukono buvana n'_sighash_ yatowe n'uwukoresha. Uwo _sighash_ niwo azomenya ibice vy’ugucuruza bipfutswe n’umukono. Ivyo nzobivuga cane mu kigabane gikurikira.


Akira intambwe zo gushiramwo umukono wa generate wa ECDSA:


Ubwa mbere, turaharura Hash ($e$) y’ubutumwa bukeneye gushirwako umukono. Ubutumwa $m$ rero buca mu gikorwa c'ubuhinga bwa Hash, muri rusangi SHA256 canke SHA256 kabiri mu gihe ca Bitcoin:


$$
e = \text{HASH}(m)
$$


Inyuma y’aho, turaharura Nonce. Mu vy’ubuhinga bwo gupfuka amakuru, Nonce ni umubare gusa uvugwa mu buryo butari bwo canke butari bwo bukoreshwa rimwe gusa. Ni ukuvuga ko igihe cose umukono mushasha wa digitale ukozwe n’urufunguzo rubiri, bizoba bihambaye cane gukoresha Nonce itandukanye, ahandi ho, bizotuma umutekano w’urufunguzo rw’ibanga uhungabana. Birahagije rero kumenya umubare wose w’imburakimazi kandi udasanzwe $r$ ku buryo $1 \leq r \leq n-1$, aho $n$ ari urutonde rw’intangamarara $G$ y’umurongo w’uruzitiro.


Hanyuma, tuzoharura akarongo $R$ ku nzira y’umurongo w’uruzitiro n’amabara $(x_R, y_R)$ ku buryo:


$$
R = r \cdot G
$$


Turakura agaciro k’igice c’inyuma c’akarongo $R$ ($x_R$). Uwo mubare ugereranya igice ca mbere c'umukono. Kandi mu nyuma, turaharura igice ca kabiri c’umukono $s$ muri ubu buryo:


$$
s = r^{-1} \left( e + k \cdot x_R \right) \mod n
$$


hehe:



- $r^{-1}$ ni umubare w'ibiharuro $r$ w'ibiharuro $n$, ni ukuvuga umubare wose ku buryo $r \cdot r^{-1} \equiv 1 \mod n$;
- $k$ ni urufunguzo rw'ibanga rw'ukoresha;
- $e$ ni Hash y'ubutumwa;
- $n$ ni urutonde rw’inzira y’umuyagankuba $G$ y’umurongo w’uruzitiro.


Umukono rero ni gusa uguhuza $x_R$ na $s$:


$$
\text{SIG} = x_R \Vert s
$$


### Gusuzuma umukono wa ECDSA


Kugira ngo ugenzure umukono $(x_R, s)$, umuntu wese azi urufunguzo rwa bose $K$ n'imirongo y'umurongo w'uruzitiro ashobora gukomeza muri ubu buryo:


Mbere, suzuma ko $x_R$ na $s$ biri hagati y'igihe $[1, n-1]$. Ivyo bituma umukono wubaha inzitizi z’imibare z’umugwi w’ibiharuro vy’ibiharuro. Iyo bitabaye gutyo, uwugenzura aca yanka iyo sinya ko ata co imaze.


Hanyuma, ubaze Hash y’ubutumwa:


$$
e = \text{HASH}(m)
$$


Harura igisubizo c'imirongo ya $s$ modulo $n$:


$$
s^{-1} \mod n
$$


Harura agaciro kabiri $u_1$ na $u_2$ muri ubu buryo:


$$
\begin{align*}
u_1 &= e \cdot s^{-1} \mod n \\
u_2 &= x_R \cdot s^{-1} \mod n
\end{align*}
$$


Kandi mu nyuma, uharure akarongo $V$ ku nzira y’umurongo w’uruzitiro ku buryo:


$$
V = u_1 \cdot G + u_2 \cdot K
$$


Umukono ugira akamaro gusa iyo $x_V \equiv x_R \mod n$, aho $x_V$ ari $x$ ihuza ry'akarongo $V$. Nkako, umuntu afatanije $u_1 \cdot G$ na $u_2 \cdot K$, aronka akarongo $V$, iyo umukono ufise akamaro, kagomba guhura n’akarongo $R$ kakoreshwa mu gihe c’umukono (modulo $n$).


### Umukono n'amasezerano ya Schnorr


Igishushanyo c’umukono wa Schnorr ni ubundi buryo bwo gusubirira ECDSA butanga inyungu nyinshi. Birashoboka ko ikoreshwa muri Bitcoin kuva mu 2021 n’ugushiraho Taproot, n’ibigereranyo vy’inyandiko za P2TR. Cokimwe na ECDSA, umugambi wa Schnorr uremerera gusinya ubutumwa hakoreshejwe urufunguzo rw’ibanga, mu buryo uwo musinya ushobora kugenzurwa n’umuntu wese azi urufunguzo rwa bose ruhuye.

Ku bijanye na Schnorr, umurongo umwe nyawo na ECDSA ukoreshwa n’ibipimo bimwe. Ariko rero, imfunguruzo za bose ziserukirwa mu buryo butandukanye gatoyi ugereranije na ECDSA. Nkako, zigaragazwa gusa n’urugero rwa $x$ rw’akarongo kari ku nzira y’uruzitiro. Udakunze ECDSA, aho imfunguruzo za bose zikozwe zigereranywa n’amabayiti 33 (n’ibara ry’intango ryerekana uburinganire bwa $y$), Schnorr akoresha imfunguruzo za bose zifise amabayiti 32, zihuye gusa n’ihuriro rya $x$ ry’akarongo $K$, kandi bifatwa ko $y$ ari mbere ku buryo busanzwe. Ukwo guserukira kworoshe kugabanya ubunini bw’imikono kandi kworohereza ugutunganya bimwebimwe mu mirongo y’ugusuzuma.

Urufunguzo rwa bose rero ni $x$ rwo guhuza n'akarongo $K$:


$$
\text{pk} = K_x
$$


Intambwe ya mbere kugira ngo generate umukono ni Hash ubutumwa. Ariko bitandukanye na ECDSA, bikorwa n’ibindi bipimo kandi igikorwa ca Hash gikoreshwa kugira ngo ntihagire ugutombora mu bihe bitandukanye. Igikorwa kirimwo ikimenyetso ca Hash gisaba gusa kwongerako ikimenyetso kidasanzwe ku vyinjizwa vy'igikorwa ca Hash iruhande y'amakuru y'ubutumwa.


![CYP201](assets/fr/023.webp)


Uretse ubutumwa, $x$ coordinate y'urufunguzo rwa bose $K_x$, hamwe n'akarongo $R = r \cdot G$, biharuwe bivuye kuri Nonce $r$ (ari vyo ubwavyo ari umubare wose wihariye ku musinya wose, biharuwe mu buryo butegekanijwe bivuye ku rufunguzo rw'ibanga n'ubutumwa bufitaniye isano n'ubugoyagoye bwo kwirinda GW3). igikorwa cashizweko ikimenyetso. Nka kurya kw'urufunguzo rwa bose, gusa $x$ coordinate y'akarongo ka Nonce $R_x$ ni yo igumaho kugira ngo idondore akarongo.


Inyishu y'iyi hashing yashizweho $e$ yitwa "ingorane":


$$
e = \text{HASH}(\text{``BIP0340/challenge''}, R_x \Vert K_x \Vert m) \mod n
$$


Aha, $\umwandiko{Hash}$ ni igikorwa ca SHA256 Hash, na $\umwandiko{``BIP0340/ingorane''}$ ni ikimenyetso kidasanzwe c'ugucapura.


Ubwa nyuma, umurongo $s$ ubarwa uhereye ku rufunguzo rw’ibanga $k$, Nonce $r$, n’ingorane $e$ nk’uko bikurikira:


$$
s = (r + e \cdot k) \mod n
$$


Umukono rero ni gusa umugwi $R_x$ na $s$.


$$
\text{SIG} = R_x \Vert s
$$


### Gusuzuma umukono wa Schnorr


Igenzura ry’umukono wa Schnorr ryoroshe kuruta iry’umukono wa ECDSA. Aha niho hari intambwe zo kugenzura umukono $(R_x, s)$ n'urufunguzo rwa bose $K_x$ n'ubutumwa $m$.

Mbere, turasuzuma ko $K_x$ ari umubare wose ubereye uri munsi ya $p$. Niba ari uko bimeze, turagarura akarongo kahuye ku nzira $K_y$ ari umubare. Turakura kandi $R_x$ na $s$ mu gucapura umukono $\text{SIG}$. Hanyuma, tugasuzuma ko $R_x < p$ na $s < n$ (urutonde rw’umurongo).

Igikurikira, turaharura ingorane $e$ mu buryo bumwe n’ubw’uwatanze umukono:


$$
e = \text{HASH}(\text{``BIP0340/challenge''}, R_x \Vert K_x \Vert m) \mod n
$$


Hanyuma, tubaze ikigereranyo ku nzira y'umurongo muri ubu buryo:


$$
R' = s \cdot G - e \cdot K
$$


Ubwa nyuma, turasuzuma ko $R'_x = R_x$. Niba izo x zibiri zihuye, rero umukono $(R_x, s)$ urakora vy'ukuri n'urufunguzo rwa bose $K_x$.


### Ni kuki ivyo bikora?


Uwushizeko umukono yaharuye $s = r + e \cdot k \mod n$, rero $R' = s \cdot G - e \cdot K$ ikwiye kuba ingana n'akarongo k'intango $R$, kuko:


$$
s \cdot G = (r + e \cdot k) \cdot G = r \cdot G + e \cdot k \cdot G
$$


Kubera ko $K = k \cakarongo G$, dufise $e \cakarongo k \cakarongo G = e \cakarongo K$. Gutyo:


$$
R' = r \cdot G = R
$$


Ni co gituma dufise:


$$
R'_x = R_x
$$


### Ivyiza vy'imikono ya Schnorr


Igishushanyo c’umukono wa Schnorr kiratanga inyungu nyinshi kuri Bitcoin ku bijanye n’ubuhinga bwa mbere bwa ECDSA. Ica mbere, Schnorr aremera ko imfunguruzo n’imikono bihurizwa hamwe. Ivyo bisigura ko imfunguruzo nyinshi za bose zishobora guhurizwa hamwe zikaba urufunguzo rumwe.


![CYP201](assets/fr/024.webp)


Kandi ni ko nyene, imikono myinshi irashobora gukoranirizwa hamwe ikaba umukono umwe ufise akamaro. Gutyo, mu gihe c’ugucuruza kw’imikono myinshi, umugwi w’abaje mu nama urashobora gusinya n’umukono umwe n’urufunguzo rwa bose ruhurikiye hamwe. Ivyo bigabanya cane igiciro co kubika n’uguharura ku rubuga, kuko urudodo rumwe rumwe rukeneye gusa kugenzura umukono umwe.


![CYP201](assets/fr/025.webp)


Ikindi kandi, gukoranya amasinya biratuma umuntu agira ubuzima bwite. Ku bwa Schnorr, biraca bidashoboka gutandukanya igikorwa c’imikono myinshi n’igikorwa c’umukono umwe gisanzwe. Ukwo guhuza gutuma gusuzuma uruzitiro bigorana cane, kuko bigabanya ubushobozi bwo kumenya ibimenyetso vy’intoke vya Wallet.


Ubwa nyuma, Schnorr aratanga kandi ubushobozi bwo kugenzura ibice. Mu kugenzura imikono myinshi icarimwe, ama node arashobora kuronka ubushobozi, cane cane ku ma blocs arimwo amafaranga menshi. Ukwo gutuma ibintu bigenda neza bigabanya umwanya n’ubutunzi bikenewe kugira ngo umuntu yemeze igice.

Kandi, imikono ya Schnorr ntishobora guhinduka, itandukanye n’imikono ikoreshwa na ECDSA. Ivyo bisigura ko uwutera adashobora guhindura umukono ubereye kugira ngo akore uwundi mukono ubereye ku butumwa bumwe n’urufunguzo rwa bose rumwe. Ubwo bugoyagoye bwariho mbere muri Bitcoin kandi bwabujije cane cane gushirwa mu ngiro kwa Lightning Network. Yatowe umuti kuri ECDSA n’iyi SegWit softfork mu 2017, ivyo bikaba birimwo kwimurira imikono mu rutonde rw’amakuru rutandukanye n’ibikorwa vy’ubudandaji kugira ngo ntibibe bishobora guhinduka.


### Ni kuki Satoshi yahisemwo ECDSA?


Nk'uko twabibonye, ​​Satoshi mu ntango yahisemwo gushiramwo ECDSA ku mikono ya digitale muri Bitcoin. Yamara, twabonye kandi ko Schnorr aruta ECDSA mu bintu vyinshi, kandi iyo porotokole yashizweho na Claus-Peter Schnorr mu 1989, imyaka 20 imbere y’uko Bitcoin ivumburwa.


Erega, ntituzi vy’ukuri igituma Satoshi itayihisemwo, ariko iciyumviro gishobora kuba ari uko iyo porotokole yari munsi y’uburenganzira gushika mu 2008. Naho Bitcoin yaremwe haciye umwaka, muri Mukakaro 2009, nta n’itegeko ry’ubuhinga ry’imikono ya Schnorr ryari ririho ico gihe. Kumbure Satoshi yabonye ko ari vyiza gukoresha ECDSA, yari isanzwe ikoreshwa cane kandi igeragezwa muri porogarama zifunguye kandi zifise uburyo bwinshi bwo gushirwa mu ngiro (cane cane ububiko bwa OpenSSL bwakoreshejwe gushika mu 2015 muri Bitcoin core, hanyuma bugasubirizwa na libsecp250.k10 muri). Canke kumbure gusa ntiyari azi ko iyo patent izohera mu 2008. Uko biri kwose, iciyumviro gishoboka cane kimeze nk’igifitaniye isano n’iyo patent be n’uko ECDSA yari ifise amateka yemejwe kandi ko yari yoroshe gushirwa mu ngiro.


## Amabendera ya sighash


<chapterId>231c41a2-aff2-4655-9048-47b6d2d83d64</chapterId>


Nk’uko twabibonye mu bice vyabanje, imikono ya digitale akenshi ikoreshwa mu gufungura inyandiko y’inyungu. Mu nzira yo gusinya, birakenewe ko amakuru yashizweko umukono ashirwa mu biharuro, yerekanwa mu ngero zacu n’ubutumwa $m$. Aya makuru, iyo amaze gushirwako umukono, ntashobora guhindurwa ataco ahinduye kugira ngo umukono ube utagira akamaro. Nkako, haba kuri ECDSA canke kuri Schnorr, uwugenzura umukono ategerezwa gushiramwo mu biharuro vyabo ubutumwa bumwe $m$. Iyo itandukanye n'ubutumwa $m$ bwakoreshejwe mu ntango n'uwashizeko umukono, igisubizo kizoba kitari co kandi umukono uzobonwa ko udafise akamaro. Bica bivugwa ko umukono upfuka amakuru amwamwe kandi ukayakingira, mu buryo bumwe, kugira ngo ntahindurwe ata wemerewe.


### Ibendera ry’umutima ni iki?


Mu bijanye na Bitcoin, twabonye ko ubutumwa $m$ buhuye n’ugucuruza. Ariko rero, mu vy’ukuri, biragoye cane. Nkako, kubera amabendera ya sighash, birashoboka guhitamwo amakuru yihariye mu bijanye n’ugucuruza azopfukwa canke atazopfukwa n’umukono.

"Ibendera rya sighash" ni rero umurongo wongerewe ku nkuru yose, ushobora kumenya ibice vy'isoko bipfutse n'umukono ujana. Ivyo bice ni ivyo kwinjira n’ivyo gusohoka. Ihitamwo ry’ibendera rya sighash rero rigena ivyo kwinjira n’ivyo gusohora vy’ugucuruza bishingwa n’umukono kandi bishobora guhindurwa ataco bihinduye. Ubwo buryo butuma abasinye bashobora gukora amakuru y’ibikorwa vy’ubudandaji hakurikijwe imigambi y’uwushizeko umukono.


Biragaragara ko iyo iyo nzira yemejwe kuri Blockchain, iba idahinduka, ata kuraba amabendera ya sighash akoreshwa. Ubushobozi bwo guhindura biciye ku mabendera ya sighash buragarukira ku kiringo kiri hagati y’ugushirako umukono n’ugushingira intahe.


Muri rusangi, porogarama ya Wallet ntiguha uburenganzira bwo guhindura n’amaboko ibendera ry’ivyo winjiza igihe wubaka igikorwa. Ku mburabuzi, `SIGHASH_VYOSE` vyashizweho. Ku bwanje, nzi gusa Sparrow wallet yemera iyo mpinduka kuva ku mukoresha Interface.


### Ni amabendera ayahe ariho muri Bitcoin?


Muri Bitcoin, hariho mbere na mbere amabendera 3 y’ishimikiro:



- `SIGHASH_ALL` (`0x01`): Umukono ukoreshwa ku vyinjizwa vyose n'ibisohoka vyose vy'ugucuruza. Ivyo rero bica bipfukwa vyose n’umukono kandi ntibishobora guhindurwa. `SIGHASH_ALL` ni sighash ikoreshwa cane mu bikorwa vya misi yose iyo umuntu ashaka gusa gukora ibikorwa ataco bishobora guhindurwa.


![CYP201](assets/fr/026.webp)


Mu bishushanyo vyose vyo muri iki kigabane, ibara ry’umuhondo rigereranya Elements yuzuye umukono, mu gihe ibara ryirabura ryerekana ivyo bitapfutse.



- `SIGHASH_NONE` (`0x02`): Umukono upfuka ivyinjijwe vyose ariko nta na kimwe mu bisohoka, gutyo bikaba vyemerera guhindura ibisohoka inyuma y'umukono. Mu majambo nyayo, ivyo bisa n’ugucapura ata co bimaze. Uwushizeko umukono afungura UTXOs mu vyinjizwa ariko asiga umurima w’ibisohoka ushobora guhindurwa vyose. Umuntu wese azi iyo nzira arashobora rero kwongerako umusaruro yihitiyemwo, nk’akarorero mu kugaragaza Address yakira kugira ngo akoranirize hamwe amahera akoreshwa n’ivyo bikoresho, hanyuma akamenyesha iyo nzira kugira ngo asubire kuronka ama bitcoins. Umukono wa nyen’ibintu vyinjijwe ntuzoba uwutagira akamaro, kuko upfuka ibintu vyinjijwe gusa.


![CYP201](assets/fr/027.webp)



- `SIGHASH_SINGLE` (`0x03`): Umukono upfutse ivyinjijwe vyose hamwe n'isohoka rimwe, rihuye n'urutonde rw'ivyinjijwe vyashizweko umukono. Nk'akarorero, iyo umukono ufunguye _scriptPubKey_ y'injiza #0, rero ipfuka n'isohoka #0. Iryo sinyatire kandi ririnda ibindi vyose vyinjijwe, bitagishobora guhindurwa. Ariko rero, umuntu wese arashobora kwongerako ikindi gisohoka ataco ahinduye ku mukono, igihe gusa igisohoka #0, ari co conyene gipfutse na co, kitahinduwe.


![CYP201](assets/fr/028.webp)


Uretse ayo mabendera atatu, hariho n'igihinduzi `SIGHASH_ANYONPAY` (`0x80`). Iyi mpinduka ishobora gufatanywa n'ibendera ry'ishimikiro kugira ngo ureme amabendera atatu mashasha:



- `GUSUBIZA_VYOSE | SIGHASH_ANYONECANPAY` (`0x81`): Umukono upfuka inyinjizo imwe mu gihe ushiramwo ibisohoka vyose vy'ugucuruza. Iryo bendera ry’i sighash ry’ihuriro rituma, nk’akarorero, habaho ugucuruza kw’amahera y’abantu benshi. Uwutegura umusaruro ategura umusaruro akoresheje Address yabo n’amahera yitezwe, maze umushoramari wese agashobora kwongerako ivyo akoresha kugira ngo ashobore gufasha uwo musaruro. Amahera ahagije amaze kwegeranywa mu bikoresho vy’injiza kugira ngo bihaze umusaruro, iyo nzira y’ugucuruza irashobora gutangazwa.


![CYP201](assets/fr/029.webp)



- `SIGHASH_NTA | SIGHASH_ANYONECANPAY` (`0x82`): Umukono upfuka ikintu kimwe co kwinjiza, ataco wiyemeje ku gisohoka;


![CYP201](assets/fr/030.webp)



- `SIGHASH_UMURI UMUNTU | SIGHASH_ANYONECANPAY` (`0x83`): Umukono upfuka inyinjizo imwe hamwe n'isohoka rifise urutonde rumwe n'urwo rwinjijwe. Nk'akarorero, iyo umukono ufunguye _scriptPubKey_ y'injiza #3, izopfuka n'isohoka #3. Ibindi bice vy’ugucuruza biguma bishobora guhindurwa, haba mu bijanye n’ibindi bikoresho vyinjizwa canke ibindi bisohoka.


![CYP201](assets/fr/031.webp)


### Imigambi yo kwongerako amabendera mashasha ya Sighash


Ubu (2024), amabendera ya sighash gusa yerekanwa mu gice ca mbere ni yo akoreshwa muri Bitcoin. Ariko rero, hari imigambi iriko iriyumvira kwongerako amabendera mashasha y’ibara ry’agahama. Nk'akarorero, BIP118, yashikirijwe na Christian Decker na Anthony Towns, izana amabendera abiri mashasha y'ibara ry'agahama: `Igisubizo_IKIBAZO COSE` na `Igisubizo_IKIBAZO COSE` (_Igisohoka cose = "Igisubizo cose c'imbere"_).


Ivyo bimenyetso bibiri vy’ibara ry’agahama vyotanga uburyo bwo kwongerako muri Bitcoin: guhingura imikono idapfuka ikintu na kimwe kidasanzwe c’ugucuruza.


![CYP201](assets/fr/032.webp)


Ico ciyumviro catangujwe na Joseph Poon na Thaddeus Dryja mu gitabu cera c’umuravyo. Imbere y'uko ihindurwa izina, iri bendera ry'ibara ry'agahama ryari ryitwa `SIGHASH_NOINPUT`.

Iyo iri bendera rya sighash ryinjijwe muri Bitcoin, rizotuma hakoreshwa amasezerano, ariko kandi ni ikintu gikenewe kugira ngo Eltoo ishirwe mu ngiro, itegeko rusangi ry’ibice vya kabiri risobanura ingene umuntu yocungera hamwe Ownership ya UTXO. Eltoo yari yagenewe canecane gutorera umuti ingorane zijanye n’uburyo bwo guhanahana amakuru ku bijanye n’ingene imirongo ya Lightning imeze, ni ukuvuga hagati yo gufungura n’ugufunga.


Kugira ngo urushirize kumenya neza Lightning Network, inyuma y’inyigisho ya CYP201, ndagusavye cane inyigisho ya LNP201 ya Fanis Michalakis, ivuga ku ciyumviro mu buryo burambuye:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Mu gice gikurikira, ndasaba kumenya ingene ijambo Mnemonic riri ku ntango ya Bitcoin Wallet yawe rikora.


# Invugo Mnemonic


<partId>4070af16-c8a2-58b5-9871-a22c86c07458</partId>


## Ugutera imbere kw'amasakoshi ya Bitcoin


<chapterId>9d9acd5d-a0e5-5dfd-b544-f043fae8840f</chapterId>


Ubu ko twasuzumye ingene ibikorwa vya Hash n’imikono ya digitale bikora, turashobora kwiga ingene amasakoshi ya Bitcoin akora. Intumbero izoba iyo gusobanura ingene Wallet iri muri Bitcoin yubatswe, ingene ibora, n’ico amakuru atandukanye ayigize akoreshwa. Ukwo gutahura uburyo Wallet ikora bizokuronsa uburenganzira bwo gukoresha neza Bitcoin mu bijanye n’umutekano n’ubuzima bwite.


Imbere yo kwisuka mu vy'ubuhinga, ni ngombwa gusobanura neza ico "Bitcoin Wallet" bisobanura no gutahura akamaro kayo.


### Igikoresho ca Bitcoin Wallet ni iki?


Udakunze ama wallets ya kera, atuma ubika amafaranga y’umubiri n’ibiceri, Bitcoin Wallet nti "irimwo" bitcoins ubwayo. Nkako, bitcoins ntizibaho mu buryo bw’umubiri canke bw’ubuhinga bwa none bushobora kubikwa, ariko zigereranywa n’ibice vya konti vyerekanywe muri sisitemu ya Bitcoin mu buryo bwa **UTXOs** (_Ibisohoka mu bikorwa bitakoreshejwe_).


UTXOs rero zigereranya ibice vy’ama bitcoins, vy’ubunini butandukanye, bishobora gukoreshwa igihe _scriptPubKey_ yabo yuzuye. Kugira ngo ukoreshe amafaranga yiwe, umukoresha ategerezwa gutanga _scriptSig_ ifungura _scriptPubKey_ ifatanye na UTXO yiwe. Iki kimenyamenya gikorwa muri rusangi biciye ku mukono wa digitale, uva ku rufunguzo rw'ibanga rujanye n'urufunguzo rwa bose ruri muri _scriptPubKey_. Gutyo, ikintu gihambaye cane uwukoresha ategerezwa gukingira ni urufunguzo rw’ibanga.

Uruhara rwa Bitcoin Wallet ni ugucungera neza izo mfunguruzo z’ibanga. Mu vy’ukuri, uruhara rwayo rusa cane n’urw’urufunguzo kuruta Wallet mu buryo bwa kera.


### Amasakoshi ya JBOK


Ivyuma vya mbere vyakoreshejwe muri Bitcoin vyari ivyuma vya JBOK (_Just a Bunch Of Keys_), vyari bihuriye hamwe imfunguruzo z’ibanga zavutse ku giti cabo kandi ata sano riri hagati yazo. Izo nkweto zakoreshwa mu buryo bworoshe aho urufunguzo rwose rw'ibanga rwashobora gufungura Bitcoin yihariye yakira Address.


![CYP201](assets/fr/033.webp)


Iyo umuntu yipfuza gukoresha imfunguruzo nyinshi z’ibanga, vyari ngombwa ko akora ama backup menshi kugira ngo ashobore kuronka amahera mu gihe hoba ingorane ku gikoresho cakira Wallet. Niba ukoresha urufunguzo rumwe rw’ibanga, iyo nzira ya Wallet yoshobora guhagije, kubera ko gucungera urufunguzo rumwe gusa bihagije. Ariko rero, ivyo biratera ingorane: muri Bitcoin, birahanurirwa cane ko umuntu adakoresha urufunguzo rw’ibanga rumwe. Nkako, urufunguruzo rw’ibanga rujanye n’urufunguzo rwihariye rwa Address, kandi amaderesi y’ukwakira Bitcoin mu bisanzwe agenewe gukoreshwa rimwe gusa. Igihe cose uronse amahera, ukwiye kugira generate Address nshasha y’ubusa.


Ivyo biva ku citegererezo c’ubuzima bwite ca Bitcoin. Mu gusubira gukoresha iyo Address nyene, bituma abarorerezi bo hanze bashobora gukurikirana ibikorwa vya Bitcoin. Ni co gituma gusubira gukoresha Address yakira bitera intege cane. Ariko rero, kugira ngo tugire amaderesi menshi kandi dutandukanye ku mugaragaro amafaranga dukoresha, birakenewe ko ducungera imfunguruzo nyinshi z’ibanga. Ku bijanye n’amasakoshi ya JBOK, ivyo bisigura guhingura ama backup menshi nk’uko hariho amafunguro mashasha, igikorwa gishobora guca gikomeye kandi kigoye kubungabunga abakoresha.


Kugira ngo umenye vyinshi ku bijanye n’akarorero k’ubuzima bwite bwa Bitcoin no kumenya uburyo bwo kurinda ubuzima bwite bwawe, ndagusavye kandi gukurikira inyigisho yanje ya BTC204 ku bijanye na Plan ₿ Network:


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Amasakoshi ya HD


Ku Address imipaka y’amasakoshi ya JBOK, haciye hakoreshwa ubuhinga bushasha bwa Wallet. Mu mwaka w’2012, Pieter Wuille yasavye ko hoba ugutera imbere hakoreshejwe BIP32, izana amasakoshi y’amahera y’ubuhinga bwa none (HD). Ingingo ya HD Wallet ni ugukura imfunguruzo zose z’ibanga zivuye ku nzira imwe y’amakuru, yitwa seed, mu buryo bugenwa n’ubukuru. Iyi seed ivyara mu buryo butari bwo igihe Wallet iremwe kandi ikaba igize ububiko bwihariye bushobora gutuma habaho ugusubiramwo imfunguruzo zose z’ibanga za Wallet. Gutyo, uwukoresha arashobora generate umubare munini cane w'imfunguruzo z'ibanga kugira ngo yirinde Address gusubira gukoresha no kuzigama ubuzima bwiwe bwite, mu gihe akeneye gusa gukora backup imwe ya Wallet yiwe biciye kuri seed.


![CYP201](assets/fr/034.webp)


Mu bikoresho vya HD, ugukuraho urufunguzo bikorwa hakurikijwe uburyo bw’ubukuru butuma urufunguzo rutunganirizwa mu bice bitobito vy’ugukuraho, igice cose kikaba gishobora gucagurwa, kugira ngo bishobore gucunga neza amafaranga no gukorana hagati ya porogarama zitandukanye za Wallet. Muri iki gihe, iyo ngingo ngenderwako yemerwa n’abantu benshi cane bakoresha Bitcoin. Kubera iyo mvo, tuzovyihweza mu buryo burambuye mu bigabane bikurikira.


### Itegeko rya BIP39: Invugo ya Mnemonic


Uretse BIP32, BIP39 irahuza uburyo bwa seed nk’ijambo Mnemonic, kugira ngo bishobore gusubiza inyuma no gusomwa n’abakoresha. Invugo Mnemonic, yitwa kandi invugo yo gusubizaho canke invugo y'amajambo 24, ni urutonde rw'amajambo yakuwe ku rutonde rwategekanijwe imbere y'igihe rushiramwo neza seed ya Wallet.


Iryo jambo Mnemonic ryorosha cane gucungera amakuru ku muntu akoresha. Mu gihe igikoresho cakira Wallet coba caratakaye, cononekaye canke cibwa, kumenya gusa iri jambo rya Mnemonic biratuma umuntu ashobora kwiruhutsa Wallet no kugaruka kuronka amahera yose yari afise.


Mu bice bizoza, tuzokwihweza ingene ama wallet ya HD akora imbere mu mutima, harimwo uburyo bwo gukuraho amakuru n’imiterere itandukanye ishoboka y’ubukuru. Ivyo bizotuma utahura neza imishinge y’ubuhinga bwo gukingira amahera muri Bitcoin ishingiyeko. Kandi kugira ngo dutangure, mu kigabane gikurikira, ndasaba ko tubona uruhara rw'uburemere bw'ibintu ku ntango ya Wallet yawe.


## Entropi n'imibare y'imburakimazi


<chapterId>b43c715d-affb-56d8-a697-ad5bc2fffd63</chapterId>

Ivyuma vya HD vy'ubu vyishingikiriza ku makuru amwe y'intango yitwa "entropy" kugira ngo bimenyekane generate umugwi wose w'imfunguruzo za Wallet. Iyi entropie ni umubare w'ibinyoma ugena umutekano wa Wallet.


### Insobanuro ya Entropi


Entropie, mu bijanye n’ubuhinga bwo gukingira amakuru n’amakuru, ni ingero y’ingero y’ukudakeka canke ukudashobora kumenya imbere y’igihe bifitaniye isano n’inkomoko y’amakuru canke inzira y’imburakimazi. Irafise uruhara runini mu gucungera ubuhinga bwo gukora amakuru y’ibanga, cane cane mu guhingura imfunguruzo n’imibare y’imburakimazi. Entropie nini ituma imfunguruzo zivutse zidashobora kumenyekana bihagije kandi zishobora guhangana n’ibitero vy’inguvu z’agahomerabunwa, aho uwutera agerageza imigwi yose ishoboka kugira ngo atekereze urufunguzo.


Mu bijanye na Bitcoin, entropi ikoreshwa kuri generate seed. Igihe umuntu arema HD Wallet, inyubako y’ijambo Mnemonic ikorwa bivuye ku mubare w’imburakimazi, ubwawo ukaba uva ku isoko y’uburemere bw’ibintu. Iryo jambo rero rikoreshwa kuri generate imfunguruzo nyinshi z’ibanga, mu buryo bugenwa n’ubukuru, kugira ngo haboneke ivyangombwa vyo gukoresha amahera ku UTXOs.


### Uburyo bwo gutuma habaho Entropi


Entropie y’intango ikoreshwa kuri HD Wallet muri rusangi ni ibice 128 canke ibice 256, aho:



- 128 bits z'entropie zihuye n'ijambo Mnemonic ry'amajambo **12**;
- 256 bits z'entropie zihuye n'ijambo Mnemonic ry'amajambo **24**.


Akenshi, uwo mubare w'imburakimazi uhita uterwa na porogarama ya Wallet ikoresheje PRNG (_Umubare w'imburakimazi w'ikinyoma_). PRNGs ni urutonde rw’imirongo ikoreshwa mu generate urutonde rw’imibare ivuye mu ntango, ifise ibiranga vyegera ivy’umubare w’imburakimazi, ataco ari kimwe mu vy’ukuri. PRNG nziza itegerezwa kuba ifise ibintu nk’uguhuza ivy’isohoka, ukudashobora kumenya imbere y’igihe, no kunanira ibitero vy’imbere y’igihe. Mu buryo butandukanye n’ibikoresho vy’ukuri vy’imibare y’imburakimazi (TRNGs), PRNGs ni ivy’ukuri kandi birashobora gusubirwamwo.


![CYP201](assets/fr/035.webp)


Iyindi nzira ni ugukoresha amaboko generate entropie, ivyo bikaba bitanga ubugenzuzi bwiza ariko kandi bikaba bifise ingorane nyinshi. Ndaguhanura cane ko utogira entropie ya HD Wallet yawe wewe nyene.


Mu kigabane gikurikira, turaza kubona ingene tuva ku mubare w’imburakimazi tuja ku nsiguro ya Mnemonic y’amajambo 12 canke 24.


## Ijambo Mnemonic


<chapterId>8f9340c1-e6dc-5557-a2f2-26c9669987d5</chapterId>

Invugo ya Mnemonic, yitwa kandi "invugo ya seed", "invugo yo gusubirana", "invugo y'ibanga", canke "invugo y'amajambo 24", ni urutonde rusanzwe rugizwe n'amajambo 12 canke 24, rukomoka ku ntungamubiri. Ikoreshwa mu gutora imfunguruzo zose za HD Wallet. Ivyo bisigura ko kuva muri iri jambo, bishoboka ko umuntu ashobora gufata generate no gusubira kurema imfunguruzo zose z’ibanga n’iza bose za Bitcoin Wallet, maze akaronka amahera akinzwe na yo. Intumbero y’ijambo Mnemonic ni ugutanga uburyo bwo gusubiza inyuma no gusubiza amafaranga y’ama bitcoins afise umutekano kandi yoroshe gukoresha. Yatangujwe mu mwaka w’2013 n’ingingo ngenderwako ya BIP39.


Reka tuvumbure hamwe ingene twova muri entropie tuja mu nsiguro ya Mnemonic.


### Igitigiri c'igenzura


Kugira ngo umuntu ahindure entropi mu mvugo ya Mnemonic, ategerezwa kubanza kwongerako umubare w'igenzura (canke "umubare w'igenzura") ku mpera y'entropi. Iyi checksum ni urutonde rugufi rw'ibice bigaragaza ubutungane bw'amakuru mu kugenzura ko ata mpinduka y'impanuka yashizweho.


Kugira ngo umuntu abaze umubare w’ibintu bigenzurwa, igikorwa ca SHA256 Hash gikoreshwa ku ntungamubiri (rimwe gusa; iki ni kimwe mu bihe bidasanzwe muri Bitcoin aho hakoreshwa SHA256 Hash imwe aho gukoresha Hash ibiri). Ivyo bituma habaho Hash y'ibice 256. Igitigiri c’ibintu bigenzurwa gifise ibice vya mbere vy’iyi Hash, kandi uburebure bwayo buvana n’ubw’iyi entropie, hakurikijwe iyi formile:


$$
\text{CS} = \frac{\text{ENT}}{32}
$$


aho $\text{ENT}$ igereranya uburebure bw'intropi mu bice, na $\text{CS}$ uburebure bw'umubare w'igenzura mu bice.


Nk’akarorero, ku entropie y’ibice 256, ibice 8 vya mbere vya Hash birafatwa kugira ngo bibe umubare w’igenzura:


$$
\text{CS} = \frac{256}{32} = 8 \text{ bits}
$$


Igihe umubare w'igenzura umaze kubarwa, urafatanywa n'ibara ry'umubiri kugira ngo ubone urutonde rw'ibice rwagutse rwanditsweko $\text{ENT} \Vert \text{CS}$ ("gufatanya" bisobanura gushiramwo iherezo-ku-iherezo).


![CYP201](assets/fr/036.webp)


### Uguhuza hagati ya Entropy n'Ijambo Mnemonic


Igitigiri c’amajambo ari mu nteruro ya Mnemonic kivana n’ubunini bw’entropie y’intango, nk’uko vyerekanwa mu mbonerahamwe ikurikira n’:



- $\text{ENT}$: ubunini mu bice vy'uburemere;
- $\text{CS}$: ubunini mu bice vy'umubare w'igenzura;
- $w$: umubare w'amajambo ari mu nteruro ya nyuma ya Mnemonic.


$$
\begin{array}{|c|c|c|c|}
\hline
\text{ENT} & \text{CS} & \text{ENT} \Vert \text{CS} & w \\
\hline
128 & 4 & 132 & 12 \\
160 & 5 & 165 & 15 \\
192 & 6 & 198 & 18 \\
224 & 7 & 231 & 21 \\
256 & 8 & 264 & 24 \\
\hline
\end{array}
$$


Nk'akarorero, ku ntungamubiri y'ibice 256, igisubizo $\text{ENT} \Vert \text{CS}$ ni ibice 264 kandi kigatanga ijambo Mnemonic ry'amajambo 24.


### Guhindura urutonde rw'ibice bibiri mu mvugo ya Mnemonic


Urutonde rw'ibice $\umwandiko{ENT} \Vert \umwandiko{CS}$ rero rugabanywamwo ibice vy'ibice 11. Igice kimwekimwe cose c’ibice 11, iyo kimaze guhindurwamwo igice c’icumi, gihuye n’umubare uri hagati ya 0 na 2047, uwo na wo ukaba ugaragaza aho ijambo riri [mu rutonde rw’amajambo 2048 rwashizwe ku rugero rwa 1000). BIP39](https://github.com/Umugambi-w'Ivyigwa/Bitcoin-ibirimwo-ivy'inyigisho/blob/dev/ibikoresho/bet/urutonde rw'amajambo rwa bip39/itunga/URUTONDE RW'AMAJAMBO rwa BIP39.pdf).


![CYP201](assets/fr/037.webp)


Nk’akarorero, ku entropie y’ibice 128, umubare w’igenzura ni ibice 4, rero urutonde rwose rupima ibice 132. Igabanywemwo ibice 12 vy'ibice 11 (ibice vy'umutuku vyerekana umubare w'igenzura):


![CYP201](assets/fr/038.webp)


Igice kimwekimwe cose gica gihindurwa umubare w’icumi ugereranya ijambo riri kuri urwo rutonde. Nk'akarorero, igice ca kabiri `01011010001` kingana mu cumi na `721`. Mu kwongerako 1 kugira ngo bihure n'urutonde rw'urutonde (rutangura kuri 1 atari 0), ivyo bitanga ijambo rank `722`, ari ryo "_focus_" muri urutonde.


![CYP201](assets/fr/039.webp)


Ukwo kwandikirana kurasubirwamwo kuri buri gice 12, kugira ngo umuntu aronke invugo y’amajambo 12.


![CYP201](assets/fr/040.webp)


### Ibiranga urutonde rw'amajambo rwa BIP39


Ikintu kidasanzwe ku rutonde rw’amajambo rwa BIP39 ni uko ata jambo risangiye inyuguti zine za mbere zimwe mu buryo bumwe n’irindi jambo. Ivyo bisigura ko kwandika inyuguti zine za mbere gusa z’ijambo rimwe rimwe bihagije kugira ngo umuntu azigame iryo jambo Mnemonic. Ivyo birashobora gushimisha mu kuzigama umwanya, canecane ku bipfuza kubicapura ku gifadika c’icuma.


Uru rutonde rw’amajambo 2048 ruri mu ndimi nyinshi. Izo si ubuhinduzi bworoshe, ahubwo ni amajambo atandukanye y’ururimi rumwe rumwe. Ariko rero, biraremeshwa cane ko umuntu afata ingingo yo mu congereza, kuko muri rusangi iyo mu zindi ndimi idashigikirwa na porogarama ya Wallet.


### Ni uburebure ubuhe wohitamwo ku nsiguro yawe ya Mnemonic?


Kugira ngo umuntu amenye uburebure bwiza bw’ijambo ryawe Mnemonic, ategerezwa kurimbura umutekano nyawo ritanga. Invugo y’amajambo 12 itanga umutekano w’ibice 128, mu gihe invugo y’amajambo 24 itanga ibice 256 vy’umutekano.


Ariko rero, iyo ntandukaniro mu mutekano wo ku rugero rw’amajambo ntituma umutekano wose wa Bitcoin Wallet utera imbere, kuko imfunguruzo z’ibanga zikomoka kuri iri jambo zironka inyungu gusa ku bice 128 vy’umutekano. Nkako, nk’uko twabibonye mbere, imfunguruzo z’ibanga za Bitcoin zikomoka ku mibare y’imburakimazi (canke zikomoka ku nzira y’imburakimazi) ziri hagati ya $1$ na $n-1$, aho $n$ igereranya urutonde rw’intangamarara $G$ y’umurongo wa secp256k1, umubare uri munsi gatoyi ya $2}$6.{25). Umuntu rero yoshobora kwiyumvira ko izo mfunguruzo z’ibanga zitanga umutekano w’ibice 256. Ariko rero, umutekano wabo uri mu ngorane yo kuronka urufunguzo rw’ibanga ruva ku rufunguzo rwa bose rujanye n’urwo rufunguzo, ingorane ishingwa n’ingorane y’imibare y’ibara ry’umubiri ry’ibara ry’umubiri (_ECDLP_). Kugeza ubu, ubuhinga buzwi cane bwo gutorera umuti ico kibazo ni ubuhinga bwa Pollard bwa rho, bugabanura igitigiri c’ibikorwa bikenewe kugira ngo umuntu amene urufunguzo ku muzi w’ubunini bwarwo.


Ku mfunguruzo z'ibice 256, nk'izo zikoreshwa muri Bitcoin, ubuhinga bwa Pollard rho rero buragabanya uburemere bw'ibikorwa ku $2^{128}$:


$$

O(\sqrt{2^{256}}) = O(2^{128})


$$


Ku bw’ivyo, bifatwa ko urufunguzo rw’ibanga rukoreshwa muri Bitcoin rutanga ibice 128 vy’umutekano.


Ivyo bituma guhitamwo ijambo ry’amajambo 24 bidatanga uburinzi bwongereweko kuri Wallet, kuko ibice 256 vy’umutekano ku majambo ata co bimaze nimba imfunguruzo zikomokako zitanga gusa ibice 128 vy’umutekano. Kugira ngo tubone ingero y’iyo ngingo ngenderwako, ni nk’aho woba ufise inzu ifise inzugi zibiri: urugi rwa kera rw’ibiti n’urugi rukomeye. Iyo umuntu yivye, urwo rugi rwari rukomeye nta co rwobaye rumaze, kubera ko uwo muntu yinjiye yoca muri urwo rugi rw’ibiti. Ivyo ni ibintu bisa n’ivyo ngaha.


Ijambo ry’amajambo 12, na ryo nyene ritanga umutekano w’ibice 128, rero ubu rirahagije kugira ngo ukingire amafaranga yawe y’ibice vy’ubusuma ubusuma bwose. Igihe cose ubuhinga bwo gusinya ku murongo butahindutse kugira ngo bukoreshe imfunguruzo nini canke ngo bwizigire ingorane y’imibare itari ECDLP, ijambo ry’amajambo 24 riguma ari ridakenewe. Ikindi kandi, ijambo rirerire ryongera ingorane zo gutakaza mu gihe co gukora backup: backup ari ngufi incuro zibiri yama yoroshe gucungera.


Kugira ngo ugende kure kandi wige neza ingene wokoresha amaboko generate ijambo ry’ikigeragezo Mnemonic, ndaguhanura ngo uvumbure iyi nyigisho:


https://planb.network/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

Imbere yo kubandanya n’ugukura kwa Wallet muri iri jambo Mnemonic, nzobamenyesha, mu kigabane gikurikira, BIP39 passphrase, kuko ifise uruhara mu nzira yo gukura, kandi iri ku rugero rumwe n’ijambo Mnemonic.


## passphrase


<chapterId>6a51b397-f3b5-5084-b151-cef94bc9b93f</chapterId>


Nk’uko twabibonye, ​​ama wallet ya HD akomoka ku majambo Mnemonic asanzwe agizwe n’amajambo 12 canke 24. Iri jambo rirahambaye cane kuko rituma umuntu ashobora kugarura imfunguruzo zose za Wallet mu gihe igikoresho caco c’umubiri (nk’akarorero Hardware Wallet) coba caratakaye. Ariko rero, ni ikintu kimwe co kunanirwa, kuko iyo gishizwe mu kaga, uwugitera yoshobora kwiba ama bitcoins yose. Aho niho BIP39 passphrase iza.


### None igikoresho citwa BIP39 passphrase ni iki?


passphrase ni ijambobanga ry’ubuhinga, ushobora guhitamwo mu mwidegemvyo, ryongerwa ku majambo Mnemonic mu nzira y’ugukuraho urufunguzo kugira ngo wongere umutekano wa Wallet.


Urabe maso, passphrase ntikwiye kuvyivangako na PIN code ya Hardware Wallet yawe canke ijambo banga ry’ugufungura uburenganzira bwo gukoresha Wallet yawe kuri mudasobwa yawe. Udakunze izo Elements zose, passphrase irafise uruhara mu gukuraho imfunguruzo za Wallet yawe. **Ivyo bisigura ko atavyo, ntuzokwigera ushobora gusubirana ama bitcoins yawe.**


passphrase ikorana n’ijambo Mnemonic, ihindura seed aho imfunguruzo zikomoka. Gutyo, naho umuntu yoronka amajambo yawe y’amajambo 12 canke 24, ata passphrase, ntashobora kuronka amahera yawe. Gukoresha passphrase mu vy’ukuri bituma haba Wallet nshasha ifise imfunguruzo zitandukanye. Guhindura (mbere gatoyi) passphrase bizoba generate itandukanye Wallet.


![CYP201](assets/fr/041.webp)


### Ni kuki ukwiye gukoresha igitabu passphrase?


passphrase ni ubusa kandi ishobora kuba ihuriro ryose ry'inyuguti zitowe n'uwukoresha. Gukoresha passphrase rero biratanga ivyiza vyinshi. Mbere na mbere, bigabanya ingorane zose zijanye n’ugusenyuka kw’ijambo Mnemonic mu gusaba ikintu ca kabiri kugira ngo umuntu ashobore kuronka ayo mahera (ubusuma, gushika mu nzu yawe, n’ibindi).


Igikurikira, gishobora gukoreshwa mu buryo bubereye kugira ngo ukore umutego Wallet, kugira ngo uhangane n'ingorane zo kwiba amahera yawe nk'igitero c'urufunguzo rwa "_$5 wrench_". Muri iki gihe, iciyumviro ni ukugira Wallet ata passphrase irimwo gusa amafaranga makeyi, ahagije kugira ngo umuntu ashobora gutera, mu gihe afise Wallet yihishije. Iyi ya nyuma ikoresha iryo jambo nyene Mnemonic ariko ikaba icungiwe n'iyindi passphrase.

Ubwa nyuma, gukoresha passphrase biraryoshe iyo umuntu yipfuza kugenzura uburyo bwo gukora seed ya HD Wallet.


### Ni gute wohitamwo passphrase nziza?


Kugira ngo passphrase ikore neza, itegerezwa kuba ndende bihagije kandi ikaba idasanzwe. Nk’uko biri ku jambobanga rikomeye, ndabahimiriza guhitamwo passphrase ndende kandi idasanzwe uko bishoboka kwose, ifise inyuguti zitandukanye, imibare n’ibimenyetso kugira ngo igitero cose c’inkomezi z’agahomerabunwa ntigishoboka.


Ni ngombwa kandi gukiza neza iyi passphrase, mu buryo bumwe n’ubw’ijambo Mnemonic. **Kuyitakaza bisigura gutakaza uburenganzira bwo kuronka ama bitcoins yawe**. Ndahanura cane ko umuntu atavyibuka mu mutwe gusa, kuko ivyo bishobora kwongera ingorane zo gutakaza ata co bimaze. Iciyumviro ciza ni ukuvyandika ku gikoresho c’umubiri (impapuro canke icuma) gitandukanye n’ijambo Mnemonic. Ivyo bimenyetso bitegerezwa kubikwa ahantu hatandukanye n’aho ijambo ryawe rya Mnemonic ribitswe kugira ngo vyose ntibishobora guhungabanywa icarimwe.


![CYP201](assets/fr/042.webp)


Mu gice gikurikira, tuzobona ingene izo Elements zibiri ziri ku musozo wa Wallet yawe — ijambo Mnemonic na passphrase — zikoreshwa mu gukuraho amafunguro abiri akoreshwa muri _scriptPubKey_ afunga UTXOs zawe.


# Guhingura amasakoshi ya Bitcoin


<partId>9c25e767-7eae-50b8-8c5f-679d8fc83bab</partId>


## Guhingura seed n'urufunguzo rwa mbere


<chapterId>63093760-2010-5691-8d0e-9a04732ae557</chapterId>


Igihe ijambo Mnemonic n’ijambo passphrase ry’uguhitamwo bimaze gusohoka, igikorwa co gukuraho Bitcoin HD Wallet gishobora gutangura. Iryo jambo Mnemonic ribanza guhindurwa rikagira seed ari ryo shingiro ry'imfunguruzo zose za Wallet.


![CYP201](assets/fr/043.webp)


### seed ya HD Wallet


Itegeko rya BIP39 risobanura seed nk'urutonde rw'ibice 512, rukora nk'intango y'ugukuraho imfunguruzo zose za HD Wallet. seed ikomoka ku mvugo ya Mnemonic n'ishobora gukoreshwa passphrase hakoreshejwe ubuhinga bwa **PBKDF2** (_Ijambobanga ry'urufunguzo rwo gukuraho urufunguzo 2_) twamaze kuvuga mu kigabane ca 3.3. Muri iyi nzira y'ugukura, tuzokoresha ibi bikurikira:



- $m$ : ijambo Mnemonic;
- $p$ : passphrase idasanzwe yatowe n'ukoresha kugira ngo yongere umutekano wa seed. Iyo ata passphrase iriho, iki kibanza kiguma ari ubusa;
- $\umwandiko{PBKDF2}$ : igikorwa c'ugukura n'ibisubirwamwo $\umwandiko{HMAC-SHA512}$ na $2048$;
- $s$: 512-ibice Wallet seed.

Utitaye ku burebure bw’amajambo ya Mnemonic yatowe (ibice 132 canke ibice 264), igikorwa ca PBKDF2 kizokwama gitanga igisohoka c’ibice 512, kandi seed rero izokwama ari iyo ngano.


### seed Igishushanyo c'Ivyakozwe na PBKDF2.


Iyi nkuru ikurikira yerekana aho ijambo seed ryakomotse ku mvugo Mnemonic n’ijambo passphrase:


$$
s = \text{PBKDF2}_{\text{HMAC-SHA512}}(m, p, 2048)
$$


![CYP201](assets/fr/044.webp)


Agaciro ka seed rero karagira ico gakoze ku gaciro k’ijambo Mnemonic n’aka passphrase. Mu guhindura passphrase, umuntu aronka seed itandukanye. Ariko rero, n’ijambo rimwe Mnemonic na passphrase, seed imwe ni yo yama ivyara, kuko PBKDF2 ari igikorwa co gushinga intahe. Ivyo bituma izo mfunguruzo zibiri zishobora gusubirwamwo biciye mu nzira zacu zo gucungera.


**Iciyumviro:** Mu rurimi rusangi, ijambo "seed" akenshi ryerekeza, mu gukoresha nabi ururimi, ijambo Mnemonic. Nkako, iyo ata passphrase iriho, imwe ni ugushiramwo gusa amakuru y’iyindi. Ariko nk'uko twabibonye, ​​mu vy'ukuri vy'ubuhinga bw'amasakoshi, seed n'ijambo Mnemonic ni vy'ukuri Elements zibiri zitandukanye.


Ubu ko dufise seed yacu, turashobora kubandanya n'ugukuraho Bitcoin Wallet yacu.


### Urufunguzo rw'Umukuru n'Umukuru chain code


Igihe seed imaze kuronka, intambwe ikurikira mu kuronka HD Wallet ni uguharura urufunguzo rw'ibanga rwa mbere na chain code, ruzogereranya uburebure 0 bwa Wallet yacu.


Kugira ngo uronke urufunguzo rw'ibanga rwa mbere n'urufunguzo rwa chain code, igikorwa ca HMAC-SHA512 gikoreshwa kuri seed, hakoreshejwe urufunguzo rudahinduka "_Bitcoin Seed_" rusa n'urw'abakoresha bose ba Bitcoin. Ivyo bihoraho bitorwa kugira ngo bimenyekane ko ibivako vy'ingenzi ari vyo vyihariye kuri Bitcoin. Akira Elements:



- $\umwandiko{HMAC-SHA512}$: igikorwa c'ugukura;
- $s$: igikoresho c’ibice 512 Wallet seed;
- $\text{"Bitcoin seed"}$: igiharuro c'ivyaduka rusangi ku bikoresho vyose vya Bitcoin.


$$

\text{output} = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)


$$


Igisohoka c’iyi nzira rero ni 512 bits. Hanyuma igabanywamwo ibice 2:



- Ibice 256 vy'ibubamfu bikora **urufunguzo rw'ibanga rwa mbere**;
- Ivyiyumviro 256 vy'iburyo ni vyo bikora **umukuru chain code**.


Mu mibare, izo nkuru zibiri zishobora kwandikwa gutya $k_M$ ari urufunguzo rw'ibanga rwa mbere na $C_M$ ari chain code:


$$
k_M = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)_{[:256]}
$$


$$
C_M = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)_{[256:]}
$$


![CYP201](assets/fr/045.webp)


### Uruhara rw'Urufunguzo rw'Umukuru na chain code


Urufunguzo rw’ibanga rw’umukuru rufatwa nk’urufunguzo rw’umuvyeyi, aho urufunguzo rw’ibanga rwose ruvuye — abana, abuzukuru, abuzukuruza, n’ibindi — ruzova. Igereranya urugero rwa zero mu rwego rw’uburongozi bw’inkomoko.


Ku rundi ruhande, umukuru chain code, ashiramwo isoko y’inyongera y’uburemere bw’ibintu mu nzira y’ugukuraho ivy’ingenzi ku bana, kugira ngo arwanye ibitero bimwebimwe bishobora gushika. Ikindi kandi, muri HD Wallet, urufunguzo rumwe rumwe rufise chain code yihariye ifatanye na rwo, na rwo nyene rukoreshwa mu gukura urufunguzo rw’abana muri urwo rufunguzo rubiri, ariko ivyo tuzobivugako mu buryo burambuye mu bice bizoza.


Imbere yo kubandanya n’ugukura kwa HD Wallet n’iyindi Elements, nipfuza, mu kigabane gikurikira, kubamenyesha imfunguruzo zagutse, zikunda gutera urujijo n’urufunguzo nyamukuru. Turabona ingene vyubatswe n’uruhara bifise muri Bitcoin Wallet.


## Imfunguruzo zagutse

<chapterId>8dcffce1-31bd-5e0b-965b-735f5f9e4602</chapterId>


Urufunguzo rwagutse ni ugufatanya urufunguzo (rwaba urw'ibanga canke rwa bose) n'urufunguzo rujanye n'urwo chain code. Iyi chain code ni nkenerwa mu gukuraho imfunguruzo z’abana kuko, atayo, ntibishoboka gukuraho imfunguruzo z’abana mu rufunguzo rw’umuvyeyi, ariko iyo nzira tuzoyibona neza mu kigabane gikurikira. Izo mfunguruzo zagutse rero zituma umuntu ashobora gukoranya amakuru yose akenewe kugira ngo abone imfunguruzo z'abana, gutyo bikongera gucunga konti muri HD Wallet.


![CYP201](assets/fr/046.webp)


Urufunguzo rwagutse rugizwe n’ibice bibiri:


- Igikoresho co gukoresha, kirimwo urufunguzo rw’ibanga canke rwa bose hamwe n’urufunguzo rwa chain code rujana;
- Ivyo bimenyetso, ni amakuru atandukanye yo kworohereza ugukorana hagati ya porogarama no gutuma uwuyikoresha arushiriza gutahura.


### Uko imfunguruzo zagutse zikora

Iyo urufunguzo rwagutse rurimwo urufunguzo rw'ibanga, rwitwa urufunguzo rw'ibanga rwagutse. Imenyekana n'intango yayo irimwo ikimenyetso `prv`. Uretse urufunguzo rw'ibanga, urufunguzo rw'ibanga rwagutse rurimwo kandi chain code ijana. Hamwe n'ubwo bwoko bw'urufunguzo rwagutse, birashoboka gukura ubwoko bwose bw'urufunguzo rw'ibanga rw'abana. Rero, mu kwongerako no gutera kabiri uturongo ku bigobe vy’uruzitiro, biratuma kandi hashobora gukurwamwo imfunguruzo za bose z’abana.


Iyo urufunguzo rwagutse rudafise urufunguzo rw'ibanga, ahubwo rufise urufunguzo rwa bose, rwitwa urufunguzo rwa bose rwagutse. Imenyekana n'intango yayo irimwo ikimenyetso `pub`. Biragaragara ko uretse urufunguzo, harimwo n’igitabu chain code gifitaniye isano na co. Udakunze urufunguzo rw'ibanga rwagutse, urufunguzo rwa bose rwagutse rwemerera gukuraho urufunguzo rwa bose rw'abana "rusanzwe" gusa (bisobanura ko rudashobora gukuramwo urufunguzo rw'abana "rukomeye"). Tuzobona mu kigabane gikurikira ico ivyo bimenyetso "bisanzwe" n'"ibikomeye" bisobanura.


Uko biri kwose, urufunguzo rwa bose rwagutse ntirwemera gukuraho urufunguzo rw'ibanga rw'abana. Rero, naho umuntu yoba afise uburenganzira bwo gukoresha `xpub`, ntazoshobora gukoresha amahera ajanye na yo, kuko atazoshobora gukoresha imfunguruzo z’ibanga zihuye. Bashobora gusa gukura imfunguruzo za bose z'abana kugira ngo bamenye ibikorwa bijanye.


Ku bikurikira, tuzokwemera ubu buhinga bukurikira:


- $K_{\umwandiko{PAR}}$: urufunguzo rwa bose rw'umuvyeyi;
- $k_{\umwandiko{PAR}}$: urufunguzo rw'ibanga rw'umuvyeyi;
- $C_{\umwandiko{PAR}}$: umuvyeyi chain code;
- $C_{\umwandiko{CHD}}$: umwana chain code;
- $K_{\umwandiko{CHD}}^n$: urufunguzo rusangi rw'umwana;
- $k_{\umwandiko{CHD}}^n$: urufunguzo rw'ibanga rw'umwana rusanzwe;
- $K_{\umwandiko{CHD}}^h$: urufunguzo rwa bose rw'umwana rukomeye;
- $k_{\umwandiko{CHD}}^h$: urufunguzo rw'ibanga rw'umwana rukomeye.


![CYP201](assets/fr/047.webp)


### Ukwubaka urufunguzo rwagutse


Urufunguzo rwagutse rwubatswe gutya:


- **Verisiyo**: Kode ya verisiyo yo kumenya kamere y'urufunguzo (`xprv`, `xpub`, `yprv`, `ypub`...). Turabona mu mpera y'iki gice ivyo inyuguti `x`, `y`, na `z` zihuye.
- **Uburebure**: Urugero rw'ubukuru muri HD Wallet rujanye n'urufunguzo nyamukuru (0 ku rufunguzo nyamukuru).
- **Urutoke rw'umuvyeyi**: Bytes 4 za mbere za HASH160 Hash z'urufunguzo rwa bose rw'umuvyeyi rukoreshwa mu gukura urufunguzo ruri mu muzigo w'inyungu.
- **Index Number**: Ikimenyetso c'umwana mu mfunguruzo z'abavukanyi, ni ukuvuga mu mfunguruzo zose ziri ku rugero rumwe rw'inkomoko zifise imfunguruzo z'umuvyeyi zimwe.
- **chain code**: Kode yihariye y'amabayiti 32 yo gukuraho imfunguruzo z'abana.
- **Urufunguzo**: Urufunguzo rw'ibanga (rutangurirwa na byte 1 ku bunini) canke urufunguzo rwa bose.
- **Checksum**: Checksum iharuwe n'igikorwa ca HASH256 (sha256 ibiri) na yo nyene irashirwako, ivyo bikaba bituma umuntu ashobora kugenzura ubutungane bw'urufunguzo rwagutse mu gihe rwoherezwa canke rwo kubika.


Uburyo bwose bw'urufunguzo rwagutse rero ni 78 bytes ata n'umubare w'igenzura, na 82 bytes n'umubare w'igenzura. Hanyuma igahindurwa muri Base58 kugira ngo ivemwo igishushanyo gishobora gusomwa bitagoranye n’abakoresha. Uburyo bwa Base58 ni bumwe n'ubwo bwakoreshwa ku *Legacy* amaderesi yakira (imbere ya *SegWit*).


| Element           | Description                                                                                                        | Size      |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ | --------- |
| Version           | Indicates whether the key is public (`xpub`, `ypub`) or private (`xprv`, `zprv`), as well as the version of the extended key | 4 bytes   |
| Depth             | Level in the hierarchy relative to the master key                                                                  | 1 byte    |
| Parent Fingerprint| The first 4 bytes of HASH160 of the parent public key                                                              | 4 bytes   |
| Index Number      | Position of the key in the order of children                                                                       | 4 bytes   |
| Chain Code        | Used to derive child keys                                                                                          | 32 bytes  |
| Key               | The private key (with a 1-byte prefix) or the public key                                                          | 33 bytes  |
| Checksum          | Checksum to verify integrity                                                                                       | 4 bytes   |

Iyo byte imwe yongewe ku rufunguzo rw'ibanga gusa, ni kubera ko urufunguzo rwa bose rwashizwemwo rurerure kurusha urufunguzo rw'ibanga kuri byte imwe. Iyi byte y'inyongera, yongewe mu ntango y'urufunguzo rw'ibanga nk'`0x00`, iringaniza ubunini bwavyo, igatuma umuzigo w'urufunguzo rwagutse uba ufise uburebure bumwe, yaba urufunguzo rwa bose canke rw'ibanga.


### Imbere y'urufunguzo rwagutse

Nk’uko twabibonye, ​​imfunguruzo zagutse zirimwo intango yerekana uko urufunguzo rwagutse ruri be n’ingene ruteye. Igiharuro `pub` kigaragaza ko kivuga urufunguzo rwa bose rwagutse, kandi igiharuro `prv` kigaragaza urufunguzo rw'ibanga rwagutse. Urudome rw’inyongera ruri mu ntango y’urufunguzo rwagutse rurafasha kwerekana nimba urugero rukurikira ari Iragi, SegWit v0, SegWit v1, n’ibindi.

Aha niho hari incamake y’intangamarara zikoreshwa n’insobanuro zazo:


| Base 58 Prefix  | Base 16 Prefix  | Network | Purpose             | Associated Scripts  | Derivation            | Key Type     |
| --------------- | --------------- | ------- | ------------------- | ------------------- | --------------------- | ------------ |
| `xpub`          | `0488b21e`      | Mainnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/0'`, `m/86'/0'` | public       |
| `xprv`          | `0488ade4`      | Mainnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/0'`, `m/86'/0'` | private      |
| `tpub`          | `043587cf`      | Testnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/1'`, `m/86'/1'` | public       |
| `tprv`          | `04358394`      | Testnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/1'`, `m/86'/1'` | private      |
| `ypub`          | `049d7cb2`      | Mainnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/0'`             | public       |
| `yprv`          | `049d7878`      | Mainnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/0'`             | private      |
| `upub`          | `049d7cb2`      | Testnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/1'`             | public       |
| `uprv`          | `044a4e28`      | Testnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/1'`             | private      |
| `zpub`          | `04b24746`      | Mainnet | SegWit V0           | P2WPKH              | `m/84'/0'`             | public       |
| `zprv`          | `04b2430c`      | Mainnet | SegWit V0           | P2WPKH              | `m/84'/0'`             | private      |
| `vpub`          | `045f1cf6`      | Testnet | SegWit V0           | P2WPKH              | `m/84'/1'`             | public       |
| `vprv`          | `045f18bc`      | Testnet | SegWit V0           | P2WPKH              | `m/84'/1'`             | private      |


### Ivyerekeye urufunguzo rwagutse rwa Elements


Kugira ngo dutahure neza imiterere y’imbere y’urufunguzo rwagutse, reka dufate rumwe nk’akarorero maze turusenyure. Akira urufunguzo rwagutse:



- Mu ntango58:


```text
xpub6CTNzMUkzpurBWaT4HQoYzLP4uBbGJuWY358Rj7rauiw4rMHCyq3Rfy9w4kyJXJzeFfyrKLUar2rUCukSiDQFa7roTwzjiAhyQAdPLEjqHT
```



- Mu gice cumi na gatandatu:


```text
0488B21E036D5601AD80000000C605DF9FBD77FD6965BD02B77831EC5C78646AD3ACA14DC3984186F72633A89303772CCB99F4EF346078D167065404EED8A58787DED31BFA479244824DF50658051F067C3A
```


Uru rufunguzo rwagutse ruca mu bice vyinshi bitandukanye Elements:


**Umuhinduzi**: `0488B21E`


Bytes 4 za mbere ni verisiyo. Aha, bihuye n'urufunguzo rwa bose rwagutse kuri Mainnet rufise intumbero yo gukuraho *Legacy* canke *SegWit v1*.


2.**Uburebure**: `03`


Iyi nzira yerekana urugero rw'uburongozi bw'urufunguzo muri HD Wallet. Muri iki gihe, uburebure bwa `03` bisigura ko urufunguzo ari ingero zitatu z'ugukomoka munsi y'urufunguzo nyamukuru.


3.**Ikimenyetso c'urutoke rw'umuvyeyi**: `6D5601AD`


Ivyo ni bytes 4 vya mbere vya HASH160 Hash vy'urufunguzo rwa bose rwakoreshejwe mu gukuraho iyi `xpub`.


4.**Umubare w'urutonde**: `80000000`


Ico kigereranyo kirerekana ikibanza urufunguruzo rufise mu bana b’umuvyeyi warwo. Intangamarara `0x80` yerekana ko urufunguzo rukomoka mu buryo bukomeye, kandi ko ibindi vyuzuye zero, vyerekana ko urwo rufunguzo ari rwo rwa mbere mu bavukanyi barwo bashobora kuba.


**chain code**: `C605DF9FBD77FD6965BD02B77831EC5C78646AD3ACA14DC3984186F72633A893`


**Urufunguzo rwa bose**: `03772CCB99F4EF346078D167065404EED8A58787DED31BFA


7.**Igitigiri co kugenzura**: `1F067C3A`


Igitigiri c’igenzura gihuye n’ibice 4 vya mbere vya Hash (SHA256 bibiri) vy’ibindi vyose.


Muri iki gice, twabonye ko hari ubwoko bubiri butandukanye bw’imfunguruzo z’abana. Twaramenye kandi ko gukuraho izo mfunguruzo z'abana bisaba urufunguzo (rwaba urw'ibanga canke rwa bose) n'urufunguzo rwayo chain code. Mu kigabane gikurikira, tuzosuzuma mu buryo burambuye kamere y’ubwo bwoko butandukanye bw’imfunguruzo n’ingene twozikura ku rufunguzo rwazo rw’umuvyeyi na chain code.



## Inkomoko y'abana urufunguzo babiri

<chapterId>61c0807c-845b-5076-ad06-7f395b36adfd</chapterId>


Ivy’ugukura kw’imfunguruzo z’abana zibiri mu bikoresho vya Bitcoin HD bishingiye ku ntunganyo y’ubukuru ishobora gutuma habaho umubare munini w’imfunguruzo, mu gihe zitunganya izo mfunguruzo zibiri mu migwi itandukanye biciye ku mashami. Buri mwana w’umuvyeyi ashobora gukoreshwa ataco akora muri *scriptPubKey* kugira ngo ufunge bitcoins, canke nk’intango ku generate izindi mfunguruzo z’abana, n’ibindi, kugira ngo ureme igiti c’imfunguruzo.


Ivyo bikomoka vyose bitangura n’urufunguzo rw’umukuru n’urufunguzo rw’umukuru chain code, ari bo bavyeyi ba mbere ku rugero rw’uburebure 0. Ni, mu buryo bumwe, Adamu na Eva b’imfunguruzo za Wallet yawe, ba sekuruza rusangi b’urufunguzo rwose rukomoka.


![CYP201](assets/fr/048.webp)


Reka turabe ingene iyo nzira y’ugukomoka ku bintu bigaragara ikora.


### Ubwoko butandukanye bw'ibikomoka ku mwana


Nk’uko twabivuze muri make mu kigabane c’imbere, imfunguruzo z’abana zigabanywemwo ubwoko bubiri nyamukuru.


- **Imfunguruzo z'abana zisanzwe** ($k_{\umwandiko{CHD}}^n, K_{\umwandiko{CHD}}^n$): Izo zikomoka ku rufunguzo rwa bose rwagutse ($K_{\umwandiko{PAR}}$), canke urufunguzo rw'ibanga rwagutse ($k_{\umwandiko{PAR}}$), mu kubanza gukura urufunguzo rwa bose rwagutse.
- Imfunguruzo z'abana zikomeye ($k_{\text{CHD}}^h, K_{\text{CHD}}^h$): Izo rufunguzo zishobora gukomoka gusa ku rufunguzo rw'ibanga rwagutse ($k_{\text{PAR}}$) kandi rero ntiziboneka ku bavyitegereza bafise urufunguzo rwa bose rwagutse gusa.


Buri rufunguzo rw'umwana rumenyekana n'ibice 32 **index** (yitwa $i$ mu biharuro vyacu). Index z'imfunguruzo zisanzwe ziva kuri $0$ gushika kuri $2^{31}-1$, mu gihe izo z'imfunguruzo zikomeye ziva kuri $2^{31}$ gushika kuri $2^{32}-1$. Ivyo biharuro bikoreshwa mu gutandukanya abavukanyi babiri b’urufunguzo mu gihe c’ugukura. Nkako, urufunguzo rw’umuvyeyi rwose rutegerezwa kuba rushoboye gukuraho urufunguzo rw’abana rwinshi. Iyo dukoresha iyo mibare nyene mu buryo butunganye dufatiye ku mfunguruzo z’umuvyeyi, imfunguruzo zose z’abavukanyi zironswa zoba zisa, ivyo bikaba bitari vyiza. Ico kigereranyo rero kirazana igihinduka gihindura ibara ry’inkomoko, kigatuma umuvukanyi wese ashobora gutandukanywa. Uretse gukoresha mu buryo bwihariye mu masezerano amwamwe n'ingingo mfatirwako z'ugukura, muri rusangi dutangura dukura urufunguzo rwa mbere rw'umwana rufise urutonde `0`, urwa kabiri rufise urutonde `1`, n'ibindi.


### Uburyo bwo gukuraho na HMAC-SHA512


Igikomoka c’urufunguzo rw’umwana rumwe rumwe gishingiye ku gikorwa ca HMAC-SHA512, ico twavuganye mu Gice ca 2 ku bikorwa vya Hash. Bifata ibintu bibiri: umuvyeyi chain code $C_{\text{PAR}}$, n'ugufatanya urufunguzo rw'umuvyeyi (rwaba urufunguzo rwa bose $K_{\text{PAR}}$ canke urufunguzo rw'ibanga $k_{\text{PAR}}$, bivanye n'ubwoko bw'urufunguzo rw'umwana rufise urutonde rukenewe) Igisohoka ca HMAC-SHA512 ni urutonde rw’ibice 512, bigabanywemwo ibice bibiri:


- Bytes 32 za mbere (canke $h_1$) zikoreshwa mu kubara abana babiri bashasha.
- Bytes 32 za nyuma (canke $h_2$) zikora nk'iyi chain code $C_{\text{CHD}}$ nshasha y'abana babiri.


Mu biharuro vyacu vyose, nzokwerekana $\text{Hash}$ igisohoka c'igikorwa ca HMAC-SHA512.


![CYP201](assets/fr/049.webp)


#### Kuva ku rufunguzo rw'ibanga rw'umwana ruva ku rufunguzo rw'ibanga rw'umuvyeyi


Kugira ngo ubone urufunguzo rw'ibanga rw'umwana $k_{\text{CHD}}$ ruvuye ku rufunguzo rw'ibanga rw'umuvyeyi $k_{\text{PAR}}$, ibintu bibiri birashoboka bivanye n'uko urufunguzo rukomeye canke rusanzwe rukenewe.


Ku **urufunguzo rw'umwana rusanzwe** ($i < 2^{31}$), ibara rya $\umwandiko{Hash}$ ni uku:


$$
\text{hash} = \text{HMAC-SHA512}(C_{\text{PAR}},  k_{\text{PAR}} \cdot G \Vert i)
$$


Muri iki giharuro, turabona ko igikorwa cacu ca HMAC gifata ibintu bibiri: ica mbere, umuvyeyi chain code, hanyuma n’ugufatanya urutonde n’urufunguzo rwa bose rujanye n’urufunguzo rw’ibanga rw’umuvyeyi. Urufunguzo rwa bose rw'umuvyeyi rukoreshwa hano kuko turiko turarondera gukura urufunguzo rw'umwana rusanzwe, atari urufunguzo rukomeye.

Ubu dufise $\text{Hash}$ y'amabayiti 64 tuzoyigabanyamwo ibice 2 vy'amabayiti 32 kuri kimwe cose, $h_1$ na $h_2$:



$$

\text{hash} = h_1 \Vert h_2

$$



$$
h_1 = \text{hash}_{[:32]} \quad, \quad h_2 = \text{hash}_{[32:]}
$$


Urufunguzo rw'ibanga rw'umwana $k_{\text{CHD}}^n$ rero ruharurwa gutya:


$$
k_{\text{CHD}}^n = \text{parse256}(h_1) + k_{\text{PAR}} \mod n
$$


Muri iki giharuro, igikorwa $\text{parse256}(h_1)$ gishingiye ku gusobanura ama bytes 32 ya mbere ya $\text{Hash}$ nk'umubare wose w'ibice 256. Uwo mubare rero wongerwa ku rufunguzo rw’ibanga rw’umuvyeyi, vyose bifatwa modulo $n$ kugira ngo bigume mu rutonde rw’umurongo w’uruzitiro, nk’uko twabibonye mu gice ca 3 ku mikono ya digitale. Gutyo, kugira ngo umuntu abone urufunguzo rw’ibanga rw’umwana rusanzwe, naho urufunguzo rwa bose rw’umuvyeyi rukoreshwa nk’ishimikiro ryo kubara mu vyinjizwa vy’igikorwa ca HMAC-SHA512, vyama bikenewe ko umuntu agira urufunguzo rw’ibanga rw’umuvyeyi kugira ngo arangize kubara.


Kuri uru rufunguzo rw’ibanga rw’umwana, birashoboka gukura urufunguzo rwa bose ruhuye n’urwo rufunguzo hakoreshejwe ECDSA canke Schnorr. Muri ubwo buryo, turonka imfunguruzo zibiri zitunganye.


Hanyuma, igice ca kabiri ca $\text{Hash}$ gisobanurwamwo gusa ko ari chain code y'urufunguzo rw'abana twahejeje gukura:


$$
C_{\text{CHD}} = h_2
$$


Aha niho hari igishushanyo c'ivyo vyose biva:


![CYP201](assets/fr/050.webp)


Ku **urufunguzo rw'umwana rukomeye** ($i \geq 2^{31}$), ibara rya $\umwandiko{Hash}$ ni uku:



$$
\text{hash} = \text{HMAC-SHA512}(C_{\text{PAR}}, 0x00 \Vert k_{\text{PAR}} \Vert i)
$$


Muri iki giharuro, turabona ko igikorwa cacu ca HMAC gifata ibintu bibiri: ica mbere, umuvyeyi chain code, hanyuma n’ugufatanya urutonde n’urufunguzo rw’ibanga rw’umuvyeyi. Urufunguzo rw'ibanga rw'umuvyeyi rukoreshwa hano kuko turiko turarondera gukura urufunguzo rw'umwana rukomeye. Ikindi, byte ingana na `0x00` yongerwa ku ntango y'urufunguzo. Iyi nzira ingana n'uburebure bwayo kugira ngo bujane n'ubw'urufunguzo rwa bose rwacitse.

Rero, ubu dufise $\text{Hash}$ y'amabayiti 64 tuzogabanyamwo ibice 2 vy'amabayiti 32 kuri kimwe cose, $h_1$ na $h_2$:

$$

\text{hash} = h_1 \Vert h_2

$$



$$
h_1 = \text{hash}[:32] \quad, \quad h_2 = \text{hash}[32:]
$$


Urufunguzo rw'ibanga rw'umwana $k_{\text{CHD}}^h$ rero ruharurwa gutya:


$$
k_{\text{CHD}}^h = \text{parse256}(h_1) + k_{\text{PAR}} \mod n
$$


Igikurikira, dusobanura gusa igice ca kabiri ca $\text{Hash}$ nk'aho ari chain code y'imfunguruzo z'abana zibiri twahejeje gukura:


$$
C_{\text{CHD}} = h_2
$$


Aha niho hari igishushanyo c'ivyo vyose biva:


![CYP201](assets/fr/051.webp)


Turashobora kubona ko ugukura gusanzwe n’ugukura gukomeye bikora mu buryo bumwe, n’iri tandukaniro: ugukura gusanzwe gukoresha urufunguzo rwa bose rw’umuvyeyi nk’inyungu ku gikorwa ca HMAC, mu gihe ugukura gukomeye gukoresha urufunguzo rw’ibanga rw’umuvyeyi.


#### Gukura urufunguzo rwa bose rw'umwana kuva ku rufunguzo rwa bose rw'umuvyeyi


Niba tuzi gusa urufunguzo rwa bose rw'umuvyeyi $K_{\text{PAR}}$ n'urufunguzo rwa bose rwagutse chain code $C_{\text{PAR}}$, ni ukuvuga urufunguzo rwa bose rwagutse, birashoboka gukura urufunguzo rwa bose rw'abana $K_{\text{CHD}}^n$, ariko gusa ku rufunguzo rusanzwe (rudakomeye) Iryo hame ryemerera cane cane gukurikirana ingendo za konti muri Bitcoin Wallet kuva kuri `xpub` (*kuraba gusa*).


Kugira ngo dukore iyo mibare, tuzoharura $\text{Hash}$ n'urutonde $i < 2^{31}$ (ugukomoka gusanzwe):


$$
\text{hash} = \text{HMAC-SHA512}(C_{\text{PAR}}, K_{\text{PAR}} \Vert i)
$$


Muri iki giharuro, turabona ko igikorwa cacu ca HMAC gifata ibintu bibiri: ubwa mbere umuvyeyi chain code, hanyuma ugufatanya urutonde n’urufunguzo rwa bose rw’umuvyeyi.


Rero, ubu dufise $\text{Hash}$ y'amabayiti 64 tuzogabanyamwo ibice 2 vy'amabayiti 32 kuri kimwe cose, $h_1$ na $h_2$:



$$

\text{hash} = h_1 \Vert h_2

$$



$$

h_1 = \text{hash}[:32] \quad, \quad h_2 = \text{hash}[32:]

$$


Urufunguzo rwa bose rw'umwana $K_{\text{CHD}}^n$ rero ruharurwa gutya:


$$
K_{\text{CHD}}^n = \text{parse256}(h_1) \cdot G + K_{\text{PAR}}
$$


Niba $\text{parse256}(h_1) \geq n$ (urutonde rw'umurongo w'uruzitiro) canke iyo $K_{\text{CHD}}^n$ ari akarongo ku butagira urugero, ivy'ugukomoka ntibifise akamaro, kandi uwundi murongo utegerezwa gutorwa.


Muri iki giharuro, igikorwa $\text{parse256}(h_1)$ gisaba gusobanura ama byte 32 ya mbere ya $\text{Hash}$ nk'umubare wose w'ibice 256. Uwo mubare ukoreshwa mu kubara akarongo ku nzira y’umurongo w’uruzitiro biciye mu kwongerako no gutera kabiri kuva ku karongo k’umuyagankuba $G$. Iyi ngingo rero yongerwa ku rufunguzo rwa bose rw'umuvyeyi kugira ngo uronke urufunguzo rwa bose rw'umwana rusanzwe. Gutyo, kugira ngo umuntu abone urufunguzo rwa bose rw’umwana rusanzwe, urufunguzo rwa bose rw’umuvyeyi n’umuvyeyi chain code ni vyo vyonyene bikenewe; urufunguzo rw'ibanga rw'umuvyeyi ntirwigera ruza muri iyo nzira, bitandukanye n'uguharura urufunguzo rw'ibanga rw'umwana twabonye mbere.


Igikurikira, umwana chain code ni gusa:


$$
C_{\text{CHD}} = h_2
$$


Aha niho hari igishushanyo c'ivyo vyose biva:


![CYP201](assets/fr/052.webp)


### Amakete hagati y'imfunguruzo za bose n'iz'ibanga z'abana


Ikibazo gishobora kuvyuka ni ingene urufunguzo rwa bose rw’umwana rusanzwe ruva ku rufunguzo rwa bose rw’umuvyeyi rushobora guhura n’urufunguzo rw’ibanga rw’umwana rusanzwe rukomoka ku rufunguzo rw’ibanga rw’umuvyeyi ruhuye. Iryo huriro ryemezwa neza na neza n’imiterere y’ibigobe vy’imirongo y’imirongo. Nkako, kugira ngo umuntu abone urufunguzo rwa bose rw’umwana rusanzwe, HMAC-SHA512 ikoreshwa mu buryo bumwe, ariko igisohoka caco gikoreshwa mu buryo butandukanye:


- Urufunguzo rw'ibanga rw'umwana rusanzwe: $k_{\umwandiko{CHD}}^n = \umwandiko{gusesangura256}(h_1) + k_{\umwandiko{PAR}} \mod n$
- Urufunguzo rusangi rw'umwana rusanzwe: $K_{\umwandiko{CHD}}^n = \umwandiko{gusesangura256}(h_1) \cdot G + K_{\umwandiko{PAR}}$


Kubera ibikorwa vyo kwongerako no gutera kabiri ku nzira y’uruzitiro, ubwo buryo bwompi buratanga ibisubizo bihuye: urufunguzo rwa bose ruva ku rufunguzo rw’ibanga rw’umwana rusa n’urufunguzo rwa bose rw’umwana ruva ku rufunguzo rwa bose rw’umuvyeyi.


### Incamake y'ubwoko bw'inkomoko


Mu ncamake, ng’ubu ubwoko butandukanye bushoboka bw’ibikomoka ku majambo:


$$
\begin{array}{|c|c|c|c|}
\hline
\rightarrow & \text{PAR} & \text{CHD} & \text{n/h} \\
\hline
k_{\text{PAR}} \rightarrow k_{\text{CHD}} & k_{\text{PAR}} & \{ k_{\text{CHD}}^n, k_{\text{CHD}}^h \} & \{ n, h \} \\
k_{\text{PAR}} \rightarrow K_{\text{CHD}} & k_{\text{PAR}} & \{ K_{\text{CHD}}^n, K_{\text{CHD}}^h \} & \{ n, h \} \\
K_{\text{PAR}} \rightarrow k_{\text{CHD}} & K_{\text{PAR}} & \times & \times \\
K_{\text{PAR}} \rightarrow K_{\text{CHD}} & K_{\text{PAR}} & K_{\text{CHD}}^n & n \\
\hline
\end{array}
$$


Kugeza ubu mwarize gukora Elements y'ishimikiro ya HD Wallet: ijambo Mnemonic, seed, hanyuma urufunguzo nyamukuru na chain code nyamukuru. Mwabonye kandi ingene mwokura abana babiri b’urufunguzo muri iki kigabane. Mu kigabane gikurikira, tuzoca irya n’ino ingene ivyo bikomoka bitunganijwe mu bipapuro vya Bitcoin n’imiterere yo gukurikiza kugira ngo turonke neza amaderesi y’ukwakira hamwe n’amafunguro abiri akoreshwa muri *scriptPubKey* na *scriptSig*.


## Wallet Imiterere n'Inzira z'Ivyakozwe

<chapterId>34e1bbda-67de-5493-b268-1fded8d67689</chapterId>


Uburyo bw’ubukuru bw’amasakoshi ya HD muri Bitcoin buratuma habaho ugutunganya amasakoshi y’ingenzi mu buryo butandukanye. Iciyumviro ni ugukura, mu rufunguzo rw’ibanga rw’umukuru n’umukuru chain code, ingero nyinshi z’uburebure. Urugero rwose rwongereweko rujanye n'ugukura kw'urufunguzo rw'umwana rubiri ruva ku rufunguzo rw'umuvyeyi.


Mu gihe c’igihe, BIPs zitandukanye zashizeho ingingo mfatirwako z’izo nzira z’ugukura, zigamije guhuza ikoreshwa ryazo muri porogarama zitandukanye. Rero, muri iki gice, tuzobona insobanuro y’urugero rwose rw’ugukomoka mu ma wallet ya HD, hakurikijwe izo ngingo mfatirwako.


### Uburebure bw'aho HD Wallet ikomoka


Inzira z’ugukura zitunganijwe mu bice vy’uburebure, kuva ku burebure 0, bugereranya urufunguzo rwa mbere n’urufunguzo rwa chain code, gushika ku bice vy’inzego ntoya zo gukura amaderesi akoreshwa mu gufunga UTXO. BIPs (*Ivyiyumviro vyo gutegura neza Bitcoin*) isobanura ingingo ngenderwako za Layer imwe imwe, ivyo bikaba bifasha guhuza ibikorwa mu bikoresho bitandukanye vyo gucunga Wallet.


Inzira y'ugukura rero, yerekeza ku rutonde rw'ibiharuro bikoreshwa mu gukura imfunguruzo z'abana ku rufunguzo rw'umukuru.


**Uburebure 0: Urufunguzo rwa mbere (BIP32)**


Ubu burebure buhuye n'urufunguzo rw'ibanga rwa Wallet n'urufunguzo rwa chain code. Igereranywa n’inyandiko $m/$.


**Uburebure bwa 1: Intumbero (BIP43)**


Intumbero ni yo igena imiterere yumvikana y’ivyo bikomokako. Nk’akarorero, indege ya P2WPKH Address izogira $/84’/$ ku burebure bwa 1 (nk’uko BIP84 ibivuga), mu gihe indege ya P2TR Address izogira $/86’/$ (nk’uko BIP86 ibivuga). Iyi Layer iratuma habaho uguhuza hagati y’amasakoshi mu kwerekana imibare y’urutonde ihuye n’imibare ya BIP.


Mu yandi majambo, iyo umaze kuronka urufunguzo rwa mbere n’urufunguzo rwa mbere chain code, ivyo bikora nk’urufunguzo rw’umuvyeyi kugira ngo ubone urufunguzo rw’umwana. Index ikoreshwa muri iyi nkuru ishobora kuba, nk'akarorero, $/84'/$ nimba Wallet igenewe gukoresha inyandiko z'ubwoko bwa SegWit v0. Ivyo bibiri vy’urufunguzo rero biri ku burebure bwa 1. Uruhara rwavyo si ugufunga bitcoins, ahubwo ni ugukora gusa nk’inzira mu rwego rw’uburongozi bw’ibikomoka.


**Uburebure bwa 2: Ubwoko bw'amafaranga (BIP44)**


Kuva ku rufunguzo rubiri ku burebure 1, hakorwa ugukura gushasha kugira ngo umuntu aronke urufunguzo rubiri ku burebure 2. Ubwo burebure buratuma umuntu ashobora gutandukanya amakonti ya Bitcoin n’ayandi mafaranga y’ibanga ari muri Wallet imwe.


Ifaranga ryose rifise urutonde rwihariye kugira ngo rihure n'amafaranga menshi. Nk'akarorero, kuri Bitcoin, urutonde ni $/0'/$ (canke `0x80000000` mu kwandika kw'ibice cumi na bitandatu). Index z'amafaranga zitorwa mu rugero kuva kuri $2^{31}$ gushika kuri $2^{32}-1$ kugira ngo habeho ugukomoka gukomeye.


Kugira ngo ndabahe izindi ngero, ng’izi urutonde rw’amafaranga amwe amwe:


- $1'$ (`0x80000001`) ku biceri vya Testnet;
- $2'$ (`0x80000002`) ku giciro c'amahera;
- $60'$ (`0x8000003c`) ku Ethereum...


**Uburebure bwa 3: Konti (BIP32)**


Wallet yose ishobora guca mu makonti menshi, ikaba iharurwa kuva kuri $2^{31}$, kandi igaserurwa ku burebure bwa 3 na $/0'/$ ku konti ya mbere, $/1'/$ ku ya kabiri, n'ibindi. Muri rusangi, iyo yerekeza ku rufunguzo rwagutse `xpub`, yerekeza ku mfunguruzo ziri muri ubu burebure bw'inkomoko.


Ukwo gutandukanya mu nkuru zitandukanye ni uguhitamwo. Igamije kworohereza imitunganirize ya Wallet ku bakoresha. Mu vy’ukuri, kenshi na kenshi hakoreshwa inkuru imwe gusa, akenshi ikaba ari yo ya mbere. Ariko rero, mu bihe bimwebimwe, iyo umuntu yipfuza gutandukanya neza amabara y’ingenzi abiri akoreshwa mu buryo butandukanye, ivyo birashobora kuba ngirakamaro. Nk’akarorero, birashoboka gukora konti y’umuntu ku giti ciwe n’iyindi y’umwuga ivuye muri seed imwe, n’imigwi itandukanye rwose y’imfunguruzo ivuye muri ubwo burebure bw’ugukomoka.


**Uburebure bwa 4: Urudodo (BIP32)**


Inkuru yose isobanuwe mu burebure bwa 3 rero itunganijwe mu minyororo ibiri:


- Uruhererekane rw'inyuma: Muri urwo ruhererekane, ivyo bizwi nk'amaderesi "ya bose" ni vyo bivako. Izo aderesi zakira zigamije gufunga ama UTXO ava mu bikorwa vyo hanze (ni ukuvuga ava mu gukoresha ama UTXO atari ayawe). Mu kuvuga mu buryo bworoshe, uwo munyororo wo hanze ukoreshwa igihe cose umuntu yipfuza kwakira ama bitcoins. Iyo ukanda kuri "*receive*" muri porogaramu yawe ya Wallet, yama ari Address iva mu ruzitiro rw'inyuma baguhaye. Uyu murongo ugereranywa n'imfunguruzo zibiri zikomoka ku rutonde $/0/$.
- **Uruhererekane rw'imbere (uguhindura)**: Uruhererekane rwagenewe kwakira amaderesi afunga ama bitcoins ava mu gukoresha ama UTXO ari ayawe, mu yandi majambo, guhindura amaderesi. Imenyekana n'urutonde $/1/$.


**Uburebure bwa 5: Urutonde rwa Address (BIP32)**


Ubwa nyuma, uburebure bwa 5 bugereranya intambwe ya nyuma yo gukura muri Wallet. Naho mu buryo bw’ubuhinga bishoboka ko umuntu abandanya ibihe bidahera, ingingo mfatirwako ziriho ubu zihagarara aha. Kuri ubu burebure bwa nyuma, imfunguruzo zibiri zizokoreshwa mu vy’ukuri mu gufunga no gufungura UTXOs zirava. Index yose iremesha gutandukanya hagati y’urufunguzo rw’abavukanyi babiri: rero, uwa mbere azoronka Address azokoresha index $/0/$, uwa kabiri index $/1/$, n’ibindi.


![CYP201](assets/fr/053.webp)


### Inyandiko y'inzira z'inkomoko


Inzira y'inkomoko yandikwa mu gutandukanya urugero rwose n'agacamuzingi ($/$). Buri nzira rero yerekana inkomoko y'urufunguzo rw'umuvyeyi ($k_{\umwandiko{PAR}}$, $K_{\umwandiko{PAR}}$, $C_{\umwandiko{PAR}}$) ku rufunguzo rw'umwana ($k_{\umwandiko{CHD}}$, $C_{\}$}{HDC). Umubare wanditswe ku burebure bumwebumwe uhuye n’urutonde rwakoreshejwe kugira ngo urwo rufunguzo ruve ku bavyeyi barwo. Igiharuro ($'$) rimwe na rimwe gishirwa iburyo bw'urutonde kigaragaza inkomoko ikomeye ($k_{\igisomwa{CHD}}^h$, $K_{\igisomwa{CHD}}^h$). Rimwe na rimwe, iyo apostrophe isubirizwa n’ikimenyetso $h$. Iyo ata kimenyetso c’inyuma canke $h$, rero ni inkomoko isanzwe ($k_{\igisomwa{CHD}}^n$, $K_{\igisomwa{CHD}}^n$).

Nk'uko twabibonye mu bice vyabanje, urutonde rw'urufunguzo rukomeye rutangura kuri $2^{31}$, canke `0x80000000` mu bice cumi na bitandatu. Rero, iyo urutonde rukurikiwe n'agace k'inyuma mu nzira y'inkomoko, $2^{31}$ itegerezwa kwongerwa ku mubare werekanwa kugira ngo ubone agaciro nyako gakoreshwa mu gikorwa ca HMAC-SHA512. Nk'akarorero, iyo inzira y'inkomoko igaragaza $/44'/$, urutonde nyarwo ruzoba:

$$

i = 44 + 2^{31} = 2\,147\,483\,692

$$


Mu nkuru cumi n'itandatu, ibi ni `0x8000002C`.


None ko twatahuye ingingo ngenderwako nyamukuru z’inzira z’ugukomoka, reka dufate akarorero! Aha niho inzira y'ugukura kwa Bitcoin yakira Address:



$$

m / 84' / 0' / 1' / 0 / 7

$$


Muri aka karorero:


- $84'$ yerekana urugero rwa P2WPKH (SegWit v0);
- $0'$ yerekana amafaranga y'i Bitcoin kuri Mainnet;
- $1'$ ihuye n'inkuru ya kabiri iri muri Wallet;
- $0$ yerekana ko Address iri ku ruzitiro rw’inyuma;
- $7$ yerekana Address y’inyuma ya 8 y’iyi konti.


### Incamake y'imiterere y'inkomoko


| Depth | Description        | Standard Example                  |
| ----- | ------------------ | --------------------------------- |
| 0     | Master Key         | $m/$                              |
| 1     | Purpose            | $/86'/$ (P2TR)                    |
| 2     | Currency           | $/0'/$ (Bitcoin)                  |
| 3     | Account            | $/0'/$ (First account)            |
| 4     | Chain              | $/0/$ (external) or $/1/$ (change)|
| 5     | Address Index      | $/0/$ (first address)             |

Mu gice gikurikira, tuzobona ico "*ibisobanuro vy'inyandiko z'isohoka*" ari vyo, ubuhinga bushasha bwashizweho muri Bitcoin core bworosha gusubiza inyuma Bitcoin Wallet.


## Igisohoka c'inyandiko isobanura

<chapterId>e4f1c2d3-9b8a-4d3e-8f2a-7b6c5d4e3f2a</chapterId>

Kenshi ubwirwa ko ijambo Mnemonic ryonyene rihagije kugira ngo ushobore kuronka Wallet. Mu vy’ukuri, ibintu birarushiriza kugorana gatoyi. Mu kigabane ca mbere, twaravye ingene HD Wallet ikomoka, kandi ushobora kuba warabonye ko iyo nzira igoye cane. Inzira z'ugukura zibwira porogaramu iyo ikwiye gukurikira kugira ngo ikure imfunguruzo z'ukoresha. Ariko rero, iyo umuntu ariko aragarura Bitcoin Wallet, iyo atazi izo nzira, ijambo Mnemonic ryonyene ntirihagije. Bituma umuntu aronka urufunguzo rwa mbere n’urufunguzo rwa mbere chain code, ariko rero birakenewe kumenya index zikoreshwa kugira ngo umuntu ashike ku rufunguzo rw’abana.


Mu vy’impwemu, vyoba ngombwa ko tuzigama gusa ijambo Mnemonic ryo muri Wallet yacu ariko kandi n’inzira zija ku nkuru dukoresha. Mu bikorwa, kenshi birashoboka ko umuntu asubira kuronka imfunguruzo z’abana ata makuru ayo, igihe gusa ingingo mfatirwako zakurikijwe. Mu kugerageza urugero rumwe rumwe rumwe rumwe, muri rusangi birashoboka ko umuntu asubira kuronka ama bitcoins. Ariko rero, ivyo ntivyemewe kandi biragoye cane cane ku batangura. Kandi, n’uguhinduka kw’ubwoko bw’inyandiko be n’uguseruka kw’imiterere igoye cane, ayo makuru yoshobora kugora gusobanura, gutyo ayo makuru agahinduka amakuru y’ibanga kandi bikaba bigoye kuyagarura hakoreshejwe inguvu z’agahomerabunwa. Ni co gituma ubuhinga bushasha buherutse gushirwaho kandi butangura kwinjizwa muri porogarama yawe ukunda ya Wallet: *ibisobanuro vy’inyandiko z’isohoka*.


### "Descriptor" ni iki?


"*Ibisobanuro vy'inyandiko y'isohoka*", canke gusa "*ibisobanuro*", ni imvugo zitunganijwe zidondora neza inyandiko y'isohoka (*scriptPubKey*) kandi zitanga amakuru yose akenewe kugira ngo hakurikizwe ibikorwa bijanye n'inyandiko kanaka. Bifasha mu gucunga imfunguruzo mu bikoresho vya HD mu gutanga insobanuro ihuye kandi yuzuye y’imiterere ya Wallet n’ubwoko bw’amaderesi akoreshwa.


Inyungu nyamukuru y’ibisobanuro biri mu bushobozi bwavyo bwo gushiramwo amakuru yose ahambaye kugira ngo umuntu asubizeho Wallet mu murongo umwe (ukwongerako ijambo ry’ugusubizaho). Mu kubika Descriptor n’amajambo ajanye na Mnemonic, birashoboka kugarura imfunguruzo z’ibanga mu kumenya neza ikibanza zazo mu rwego rw’ubukuru. Ku bikoresho vya Multisig, ivyo mu ntango vyari bikomeye cane, Descriptor irimwo `xpub` y’ikintu cose, gutyo bikaba bishoboka ko umuntu yosubira gukora amaderesi iyo habaye ingorane.


### Ubwubatsi bw'indege Descriptor


Descriptor igizwe n’ama Elements menshi:


- Imikorere y'inyandiko nka `pk` (*Ishura-ku-rufunguzo-rwa-Pub*), `pkh` (*Ishura-ku-rufunguzo-rwa-Pub-Hash*), `wpkh` (*Ishura-ku-Icabona-Urufunguzo-rwa-Pub-Hash*), `sh` (*Pay-to-Script-Hash`sh*), `w (*Inyandiko-Yishyura-Icabona-Hash*), `tr` (*Pay-to-Taproot*), `yinshi` (*Imikono myinshi*), na `imikono myinshi yatoranijwe` (*Imikono myinshi ifise imfunguruzo zatoranijwe*);
- Inzira z'inkomoko, nk'akarorero, `[d34db33f/44h/0h/0h]` yerekana inzira ya konti ikomoka n'urutoke rw'urufunguzo rw'umukuru;
- Imfunguruzo mu buryo butandukanye nk'imfunguruzo za bose z'icumi na zitandatu canke imfunguruzo za bose zagutse (`xpub`);
- Igitigiri c'ibintu bigenzurwa, kibanzirizwa n'ikimenyetso ca Hash, kugira ngo umuntu asuzume ubutungane bwa Descriptor.


Nk’akarorero, igikoresho ca Descriptor c’igikoresho co mu bwoko bwa P2WPKH (SegWit v0) coshobora gusa n’iki:


```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7nr4
```


Muri iyi Descriptor, igikorwa c'inkomoko `wpkh` kigaragaza ubwoko bw'inyandiko *Pay-to-Witness-Public-Key-Hash*. Ikurikirwa n’inzira y’inkomoko irimwo:


- `cdeab12f`: urutoke rw'urufunguzo rw'umukuru;
- `84h`: bisobanura gukoresha intumbero ya BIP84, igenewe amaderesi ya SegWit v0;
- `0h`: vyerekana ko ari amafaranga y’i BTC kuri Mainnet;
- `0h`: yerekeza ku nomero ya konti ikoreshwa muri Wallet.


Descriptor kandi irimwo urufunguzo rwa bose rwagutse rukoreshwa muri iyi Wallet:


```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```


Igiharuro `/<0;1>/*` kigaragaza ko Descriptor ishobora gutanga aderesi za generate zivuye ku ruhererekane rw'inyuma (`0`) no ku ruhererekane rw'imbere (`1`). Ikimenyetso c'ibara ry'agahama (`*`) kiri ku mpera y'inzira bisigura ko, mu buryo bukurikiranye, imfunguruzo zose z'abana zitakomeye (“*zitakomeye*”) zishobora gukurwa muri iki kibanza, zaba ari aderesi zo hanze canke zo mu mutima. Iyi nsiguro ntisobanura ata guca ku ruhande iciyumviro ca *gap limit*, kikaba ari igice c’uburyo bwihariye bwa Wallet bwo kumenya Address, ariko aha gikoreshwa gusa mu kwerekana ko ibiva vyose bishoboka kuri iki kibanza vyiyumviriwe.


Ubwa nyuma, `#jy0l7nr4` igereranya umubare w'igenzura kugira ngo ugenzure ubutungane bwa Descriptor.


Ubu urazi vyose ku bijanye n’ingene ama wallet ya HD akora muri Bitcoin be n’ingene umuntu ashobora gukura ama key abiri. Ariko mu bice vya nyuma, twagarukiye ku guhingura imfunguruzo z’ibanga n’iza bose, tutavuze ku bijanye n’ubwubatsi bw’amaderesi yo kwakira. Ivyo nyene ni vyo tuzovuga mu kigabane gikurikira!


## Ukwakira aderesi

<chapterId>ca80a89d-f8da-4e09-8c35-43179b65bced</chapterId>


Aderesi zo kwakira ni ibice vy'amakuru bishizwe muri *scriptPubKey* kugira ngo ufunge UTXOs ziherutse kuremwa. Mu mvugo yoroshe, Address ikoreshwa mu kwakira amafaranga y’ibiceri. Reka dusuzume ingene zikora mu bijanye n’ivyo twize mu bigabane vyabanje.


### Uruhara rw'amaderesi ya Bitcoin mu nyandiko


Nk’uko vyasiguwe imbere, uruhara rw’ugucuruza ni ugukura Ownership y’ibice vy’amahera (bitcoins) kuva ku vyo yinjiza gushika ku vyo gusohoka. Ivyo birimwo gukoresha UTXO nk’ibintu vyinjizwa mu gihe habaho uguhingura UTXO nshasha nk’ibintu bisohoka. Izo UTXO zikingirwa n’inyandiko, zisobanura ivyangombwa bikenewe kugira ngo amafaranga afungurwe.


Iyo uwukoresha aronse amafaranga y’ibiceri, uwurungitse akora UTXO akayifunga n’urufunguzo rwa *scriptPubKey*. Iyi nyandiko irimwo amategeko yo gufungura UTXO, mu bisanzwe yerekana imikono n’imfunguruzo za bose zikenewe. Kugira ngo ukoreshe iyi UTXO mu bikorwa bishasha, uwuyikoresha ategerezwa gutanga amakuru asavye biciye ku *scriptSig*. Ishirwa mu ngiro rya *scriptSig* rifatanijwe na *scriptPubKey* ritegerezwa kugarura "ukuri" canke `1`. Iyo iyo nzira ishitse, UTXO irashobora gukoreshwa mu guhingura UTXO nshasha, yo ubwayo igakingirwa n' *scriptPubKey* nshasha, n'ibindi.


![CYP201](assets/fr/054.webp)


Ni muri *scriptPubKey* nyene amaderesi y'abakira aboneka. Ariko rero, ukuntu bikoreshwa biratandukanye bivanye n’ingingo mfatirwako y’inyandiko yemejwe. Aha niho hari urutonde rw'incamake rw'amakuru ari muri *scriptPubKey* hakurikijwe urugero rwakoreshejwe, hamwe n'amakuru yitezwe muri *scriptSig* kugira ngo ufungure *scriptPubKey*.


| Standard           | *scriptPubKey*                                              | *scriptSig*                     | *redeem script*     | *witness*                                |
| ------------------ | ----------------------------------------------------------- | ------------------------------- | ------------------- | ---------------------------------------- |
| P2PK               | `<pubkey> OP_CHECKSIG`                                      | `<signature>`                   |                     |                                          |
| P2PKH              | `OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG` | `<signature> <public key>`      |                     |                                          |
| P2SH               | `OP_HASH160 <scriptHash> OP_EQUAL`                          | `<data pushes> <redeem script>` | Arbitrary data     |                                          |
| P2WPKH             | `0 <pubKeyHash>`                                            |                                 |                     | `<signature> <public key>`               |
| P2WSH              | `0 <witnessScriptHash>`                                     |                                 |                     | `<data pushes> <witness script>`         |
| P2SH-P2WPKH        | `OP_HASH160 <redeemScriptHash> OP_EQUAL`                    | `<redeem script>`               | `0 <pubKeyHash>`    | `<signature> <public key>`               |
| P2SH-P2WSH         | `OP_HASH160 <redeemScriptHash> OP_EQUAL`                    | `<redeem script>`               | `0 <scriptHash>`    | `<data pushes> <witness script>`         |
| P2TR (key path)    | `1 <public key>`                                            |                                 |                     | `<signature>`                            |
| P2TR (script path) | `1 <public key>`                                            |                                 |                     | `<data pushes> <script> <control block>` |

*Isoko: Ishirahamwe ry'isubiramwo ry'ubucuti n'abantu Bitcoin core, igenekerezo rya 7 Nyakanga 2021 - Gloria Zhao*


Ama opcode akoreshwa mu nyandiko agenewe gukoresha amakuru, kandi, iyo bikenewe, kuyagereranya canke kuyagerageza. Reka dufate akarorero k’inyandiko ya P2PKH, ariyo ikurikira:


```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
```


Nk'uko tuzobibona muri iki gice, `<pubKeyHash>` mu vy'ukuri igereranya umuzigo w'umuzigo wa Address ukoreshwa mu gufunga UTXO. Kugira ngo ufungure uru *scriptPubKey*, birakenewe ko utanga *scriptSig* irimwo:


```text
<signature> <public key>
```


Mu rurimi rw'inyandiko, ikirundo ni *LIFO* ("*Inyuma In, Imbere Gusohoka*") imiterere y'amakuru ikoreshwa mu kubika mu gihe gito Elements mu gihe c'ugushirwa mu ngiro kw'inyandiko. Buri gikorwa c'inyandiko gikoresha iki kirundo, aho Elements ishobora kwongerwako (*push*) canke igakurwaho (*pop*). Ivyanditswe bikoresha ikirundo mu gusuzuma imvugo, kubika ibihinduka vy'igihe gito, no gucunga ivyangombwa.


Ishirwa mu ngiro ry'inyandiko n'ubu nyene ntanga nk'akarorero rikurikira iyi nzira:



- Turafise *inyandikoSig*, *inyandikoPubKey*, n'ikirundo:


![CYP201](assets/fr/055.webp)



- *scriptSig* isunikwa ku kirundo:


![CYP201](assets/fr/056.webp)



- `OP_DUP` isubiramwo urufunguzo rwa bose rwatanzwe muri *scriptSig* ku kirundo:


![CYP201](assets/fr/057.webp)



- `OP_HASH160` igarura Hash y'urufunguzo rwa bose rwari rwasubiwemwo:


![CYP201](assets/fr/058.webp)



- `OP_PUSHBYTES_20 <UrufunguzoHash>` isunika Bitcoin Address iri mu *Urufunguzo rw'Inyandiko* ku kirundo:


![CYP201](assets/fr/059.webp)



- `OP_EQUALVERIFY` igenzura ko urufunguzo rwa bose rujanye n'urwakira Address:


![CYP201](assets/fr/060.webp)


`OP_CHECKSIG` isuzuma umukono uri muri *scriptSig* ikoresheje urufunguzo rwa bose. Iyi opcode ikora canecane ugusuzuma umukono nk’uko twabivuze mu gice ca 3 c’iri huriro:



![CYP201](assets/fr/061.webp)



- Niba `1` iguma ku kirundo, rero inyandiko irakora:


![CYP201](assets/fr/062.webp)


Rero, mu ncamake, iyi nyandiko iremesha kugenzura, bifashijwe n’umukono wa digitale, ko uwukoresha avuga ko ari Ownership y’iyi UTXO kandi yipfuza kuyikoresha vy’ukuri afise urufunguzo rw’ibanga rujanye n’ukwakira Address yakoreshejwe mu gihe co kurema iyi GW-51.


### Ubwoko butandukanye bw'amaderesi ya Bitcoin


Mu gihe Bitcoin yariko iratera imbere, hariho uburyo bwinshi bwo kwandika busanzwe bwongereweko. Umwe wese muri bo akoresha ubwoko butandukanye bwo kwakira Address. Aha niho hari incamake y'ibigereranyo vy'inyandiko nyamukuru biriho gushika ubu:


**P2PK (*Ishura-ku-rufunguzo rwa Pub*)**:


Iyi nzira y’inyandiko yashizweho mu nsiguro ya mbere ya Bitcoin na Satoshi Nakamoto. Inyandiko ya P2PK ifunga bitcoins ataco ihinduye ikoresheje urufunguzo rwa bose rudasanzwe (gutyo, nta kwakira Address ikoreshwa n’iki kigereranyo). Igishushanyo caco ni coroshe: kirimwo urufunguzo rwa bose kandi gisaba umukono w’ibarabara uhuye kugira ngo umuntu ashobore gufungura ayo mahera. Iyi nyandiko iri mu rugero rwa "*Iragi*".


**P2PKH (*Ishura-ku-rufunguzo-gw-526*)**:


Cokimwe na P2PK, inyandiko ya P2PKH yashizweho igihe Bitcoin yatangura. Udakunze uwuyibanjirije, ifunga ama bitcoins ikoresheje Hash y’urufunguzo rwa bose, aho gukoresha ata guca ku ruhande urufunguzo rwa bose rudasanzwe. *scriptSig* itegerezwa rero gutanga urufunguzo rwa bose rujanye n’urwakira Address, hamwe n’umukono ubereye. Amaderesi ahuye n'iki kigereranyo atangura na `1` kandi ashizwe muri *base58check*. Iyi nyandiko na yo nyene iri mu rugero rwa "*Legacy*".


**P2SH (*Pay-to-Script-Hash*)**:


Yashizweho mu 2012 na BIP16, ikigereranyo ca P2SH kiremesha gukoresha Hash y'inyandiko idasanzwe muri *scriptPubKey*. Iyi script hashed, yitwa "*redeemscript*", irimwo ivyangombwa vyo gufungura amafaranga. Kugira ngo ukoreshe UTXO yugarijwe na P2SH, birakenewe ko utanga *scriptSig* irimwo *redeemscript* y’umwimerere hamwe n’amakuru akenewe kugira ngo yemezwe. Iyi modele ikoreshwa cane cane ku bimenyetso vya kera. Amaderesi ajanye na P2SH atangura na `3` kandi ashirwa muri *base58check*. Iyi nyandiko na yo nyene iri mu rugero rwa "*Legacy*".


**P2WPKH (*Ishura-Icabona-Urufunguzo-537*)**:


Iyi nyandiko isa na P2PKH, kuko nayo ifunga bitcoins ikoresheje Hash y’urufunguzo rwa bose. Ariko rero, bitandukanye na P2PKH, *scriptSig* yimurirwa mu gice gitandukanye citwa "*Icabona*". Ivyo rimwe na rimwe vyitwa "*scriptWitness*" kugira ngo vyerekane umugwi ugizwe n'umukono n'urufunguzo rwa bose. Igiharuro cose ca SegWit gifise *Icabona c'inyandiko* caco, kandi ihuriro ry' *Ivyabona vy'inyandiko* rigize *Icabona* c'umurima w'ugucuruza. Ukwo kwimura amakuru y’imikono ni ubuhinga bushasha bwashizweho n’ivugurura rya SegWit, rigamije cane cane gukingira ubugoyagoye bw’ibikorwa bitewe n’imikono ya ECDSA.

Amaderesi ya P2WPKH akoresha *bech32* kandi yama atangura na `bc1q`. Ubwo bwoko bw'inyandiko buhuye n'ibisohoka vya verisiyo 0 SegWit.


**P2WSH (*Inyishu-ku-Icabona-Inyandiko-Hash*)**:


Ico kigereranyo ca P2WSH na co nyene carashizweho n’ivugurura rya SegWit muri Myandagaro 2017. Kimwe n’ico kigereranyo ca P2SH, gifunga bitcoins hakoreshejwe Hash y’inyandiko. Itandukaniro rikomeye riri mu kuntu imikono n’inyandiko bishirwa mu gucuruza. Kugira ngo ukoreshe ama bitcoins yugarijwe n’ubwo bwoko bw’inyandiko, uwuyaronka ategerezwa gutanga inyandiko y’umwimerere, yitwa *witnessScript* (ingana na *redeemscript* muri P2SH), hamwe n’amakuru akenewe kugira ngo yemeze iyo *witnessScript*. Ubwo buryo buratuma hashirwa mu ngiro ibintu bikomeye cane vyo gukoresha amahera, nk’ivyo gukoresha amahera menshi.


Aderesi za P2WSH zikoresha *bech32* kandi zihora zitangura na `bc1q`. Iyi nyandiko na yo ihuye n’ibisohoka vya verisiyo 0 SegWit.


**P2TR (*Pay-to-Taproot*)**:


Ico kigereranyo ca P2TR carashizweho n’ugushirwa mu ngiro kwa Taproot mu kwezi kwa 11/2021. Gishingiye ku nzira ya Schnorr yo gukoranya urufunguzo rw’ubuhinga bwa none, hamwe n’itegeko rya Merkle Tree ry’inyandiko zindi, ryitwa MAST (*Igiti c’inyandiko zindi zikoreshwa mu buryo bwa Merkelized*). Mu buryo butandukanye n’ubundi bwoko bw’inyandiko, aho ivyangombwa vyo gukoresha amahera bigaragazwa ku mugaragaro (yaba igihe umuntu yakira canke igihe akoresha amahera), P2TR iremeza guhisha inyandiko zigoye inyuma y’urufunguzo rumwe rusa n’urw’abantu bose.


Mu buryo bw’ubuhinga, inyandiko ya P2TR ifunga ama bitcoins ku rufunguzo rwa bose rwihariye rwa Schnorr, rwerekanwa na $Q$. Uru rufunguzo $Q$ mu vy'ukuri ni umugwi w'urufunguzo rwa bose $P$ n'urufunguzo rwa bose $M$, rwa nyuma rukabarwa ruvuye kuri Merkle Root y'urutonde rwa *scriptPubKey*. Bitcoins zifungiwe n’ubwo bwoko bw’inyandiko zishobora gukoreshwa mu buryo bubiri:


- Mu gutangaza umukono w'urufunguzo rwa bose $P$ (*inzira y'urufunguzo*).
- Mu guhazwa n’imwe mu nyandiko ziri muri Merkle Tree (*inzira y’inyandiko*).


P2TR rero itanga uburyo bwinshi bwo guhindura, kuko ishobora gufunga bitcoins haba n’urufunguzo rwihariye rwa bose, n’inyandiko nyinshi zo guhitamwo, canke vyose icarimwe. Ivyiza vy’iyi nzira ya Merkle Tree ni uko inyandiko y’ugukoresha amahera ikoreshwa gusa ari yo ihishurirwa mu gihe c’ugucuruza, ariko izindi nyandiko zose zishobora gukoreshwa ziguma ari ibanga.


![CYP201](assets/fr/063.webp)


P2TR ihuye n'ibisohoka vya verisiyo 1 ya SegWit, bisobanura ko imikono y'ibisohoka vya P2TR ibikwa mu gice ca *Icabona* c'ibikorwa, atari mu *scriptSig*. Amaderesi ya P2TR akoresha ubuhinga bwa *bech32m* kandi atangura na `bc1p`, ariko ni ay’umwihariko kuko adakoresha igikorwa ca Hash mu kwubaka. Nkako, zigereranya urufunguzo rwa bose $Q$ rufise uburyo bworoshe n'amakuru y'imbere. Ni rero, ikigereranyo c’inyandiko kiri hafi ya P2PK.


None ko twamaze gupfuka inyigisho, reka tugende ku bikorwa! Mu gice gikurikira, ndasaba gukuramwo SegWit v0 Address na SegWit v1 Address mu mfunguruzo zibiri.


## Address Inkomoko

<chapterId>3ebdc750-4135-4881-b07e-08965941b93e</chapterId>


Reka twihweze hamwe ingene generate Address yakira ivuye ku mfunguruzo zibiri ziri, nk'akarorero, ku burebure bwa 5 bwa HD Wallet. Iyi Address ishobora rero gukoreshwa muri porogaramu ya Wallet kugira ngo ikingire UTXO.


Kubera ko uburyo bwo gukora Address buvana n'akarorero k'inyandiko, reka twibande ku bintu bibiri vyihariye: gukora SegWit v0 Address muri P2WPKH na SegWit v1 Address muri P2TR. Ubwo bwoko bubiri bw’amaderesi burakoreshwa cane cane muri iki gihe.


### Gufatanya urufunguzo rwa bose


Tumaze gukora intambwe zose zo gukura kuva ku rufunguzo rwa mbere gushika ku burebure bwa 5 dukoresheje urutonde rukwiye, turonka urufunguzo rubiri ($k$, $K$) rufise $K = k \cdot G$. Naho bishoboka gukoresha uru rufunguzo rwa bose nk’uko biri ugufunga amafaranga n’ingingo ya P2PK, iyo si yo ntumbero yacu hano. Ahubwo, dufise intumbero yo kurema Address muri P2WPKH mu ntango, hanyuma mu P2TR ku rundi rugero.


Intambwe ya mbere ni ugufatanya urufunguzo rwa bose $K$. Kugira ngo dutahure neza iyo nzira, reka tubanze twibuke ibintu bimwebimwe vy’ishimikiro vyavuzwe mu gice ca 3.

Urufunguzo rwa bose muri Bitcoin ni akarongo $K$ kari ku nzira y'umurongo w'umurongo. Igereranywa mu buryo $(x, y)$, aho $x$ na $y$ ari amakoordinate y’akarongo. Mu buryo bwayo butashizwemwo, uru rufunguzo rwa bose rupima ibice 520: ibice 8 ku ntango (agaciro k’intango ka `0x04`), ibice 256 ku nzira ya $x$, n’ibice 256 ku nzira ya $y$.

Ariko rero, imirongo y’uruzitiro irafise akamaro k’uburinganire ku bijanye n’umurongo wa x: ku nzira ya $x$ yatanzwe, hariho gusa agaciro kabiri gashoboka k’ $y$: $y$ na $-y$. Izo nkuru zibiri ziri ku mpande zompi z’umurongo wa x. Mu yandi majambo, nitwamenya $x$, birahagije gusobanura nimba $y$ ari umubare canke umubare kugira ngo tumenye akarongo nyako kari ku nzira.


![CYP201](assets/fr/064.webp)


Kugira ngo ushire urufunguzo rwa bose, $x$ gusa ni yo ikoreshwa, ifata ibice 256, kandi hakongerwako intango kugira ngo ugaragaze uburinganire bwa $y$. Ubu buryo bugabanya ubunini bw'urufunguzo rwa bose ku bice 264 aho ku bice 520 vy'intango.Intango `0x02` yerekana ko $y$ ari umubare, intango `0x03` yerekana ko $y$ ari umubare.


Reka dufate akarorero kugira ngo dutahure neza, n'urufunguzo rwa bose rudasanzwe mu guserukira ataco bimaze:


```text
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```


Nitwabora urufunguzo, turagira:


   - Intangamarara: `04`;
   - $x$: `678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6`;
   - $y$: `49f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f`


Ikimenyetso ca nyuma c'icumi na gatandatu ca $y$ ni `f`. Mu rwego rwa 10, `f = 15`, bihuye n'umubare udasanzwe. Rero, $y$ ni ikintu kidasanzwe, kandi intango izoba `0x03` kugira ngo yerekane ivyo.


Urufunguzo rwa bose rwacitse:


```text
K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6
```

Iyi nzira ikoreshwa ku bigereranyo vyose vy'inyandiko bishingiye kuri ECDSA, ni ukuvuga vyose kiretse P2TR ikoresha Schnorr. Ku bijanye na Schnorr, nk’uko vyasiguwe mu gice ca 3, tugumya gusa agaciro ka $x$, tutashizeko intango y’intango kugira ngo twereke uburinganire bwa $y$, bitandukanye na ECDSA. Ivyo bishoboka kubera ko uburinganire bwihariye butorwa mu buryo butari bwo ku mfunguruzo zose. Ivyo bituma habaho ukugabanya gatoyi umwanya wo kubika imfunguruzo za bose.

### Ivyakomoka kuri SegWit v0 (bech32) Address


None ko twaronse urufunguzo rwacu rwa bose rwacitse, turashobora gukuramwo SegWit v0 yakira Address muri rwo.


Intambwe ya mbere ni ugukoresha igikorwa ca HASH160 Hash ku rufunguzo rwa bose rwacitse. HASH160 ni igihimba c'ibikorwa bibiri bikurikirana vya Hash: SHA256, ikurikiwe na RIPEMD160:



$$

\text{HASH160}(K) = \text{RIPEMD160}(\text{SHA256}(K))

$$


Mbere, duca urufunguzo muri SHA256:


```text
SHA256(K) = C489EBD66E4103B3C4B5EAFF462B92F5847CA2DCE0825F4997C7CF57DF35BF3A
```


Hanyuma tugaca mu gisubizo biciye muri RIPEMD160:


```text
RIPEMD160(SHA256(K)) = 9F81322CC88622CA4CCB2A52A21E2888727AA535
```


Twararonse Hash y'ibice 160 y'urufunguzo rwa bose, ari rwo rugize ico bita umuzigo w'amahera wa Address. Uwo muzigo ugereranya igice nyamukuru kandi gihambaye kuruta ibindi vyose ca Address. Ikoreshwa kandi muri *scriptPubKey* kugira ngo ufunge ama UTXO.


Ariko rero, kugira ngo uwo muzigo w’inyungu ushobore gukoreshwa n’abantu bitagoranye, harashirwako amakuru y’ivy’ubuhinga. Intambwe ikurikira ni ugushiramwo iyi Hash mu migwi y’ibice 5 mu bice cumi. Iryo hinduka ry'icumi rizoba ngirakamaro mu guhindura *bech32*, rikoreshwa n'amaderesi y'inyuma ya SegWit. Ico gikoresho c’ibice 160 Hash rero kigabanywamwo imigwi 32 y’ibice 5:



$$

\begin{array}{|c|c|}
\hline
\text{5 bits} & \text{Decimal} \\
\hline
10011 & 19 \\
11110 & 30 \\
00000 & 0 \\
10011 & 19 \\
00100 & 4 \\
01011 & 11 \\
00110 & 6 \\
01000 & 8 \\
10000 & 16 \\
11000 & 24 \\
10001 & 17 \\
01100 & 12 \\
10100 & 20 \\
10011 & 19 \\
00110 & 6 \\
01011 & 11 \\
00101 & 5 \\
01001 & 9 \\
01001 & 9 \\
01010 & 10 \\
00100 & 4 \\
00111 & 7 \\
10001 & 17 \\
01000 & 8 \\
10001 & 17 \\
00001 & 1 \\
11001 & 25 \\
00111 & 7 \\
10101 & 21 \\
00101 & 5 \\
00101 & 5 \\
10101 & 21 \\
\hline
\end{array}

$$

Rero, dufise:


```text
HASH = 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21
```


Igihe Hash ishizwe mu mirwi y'ibice 5, umubare w'igenzura wongerwa kuri Address. Iryo banga ry’igenzura rikoreshwa mu kugenzura ko umuzigo w’ivyo bikoresho vya Address utahinduwe mu gihe co kubika canke gutanga. Nk'akarorero, iremeza porogarama ya Wallet kugira ngo umenye neza ko utakoze ikosa ryo kwandika igihe winjiza Address. Ata n’iyi nkuru, woshobora kohereza bitcoins ku Address idakwiriye, bikavamwo ugutakaza amahera ubudasiba, kuko udafise urufunguzo rwa bose canke rw’ibanga rujanye n’ivyo. Rero, iyo checksum ni uburinzi ku makosa y’abantu.


Ku ma aderesi ya kera ya Bitcoin *Legacy*, igiharuro c’isuzuma cari giharuwe gusa kuva mu ntango ya Address Hash n’igikorwa ca HASH256. Kubera ko SegWit n’uburyo bwa *bech32* vyashizweho, ubu hakoreshwa amakode ya BCH (*Bose, Ray-Chaudhuri, na Hocquenghem*). Izo kode zikosora amakosa zikoreshwa mu kumenya no gukosora amakosa ari mu rutonde rw’amakuru. Barabona neza ko amakuru arungikwa ashika aho aja ataco akoze, mbere n’aho yoba hariho utuhinduko dutoduto. Amakode ya BCH akoreshwa mu bintu vyinshi, nk’amakode ya SSD, DVD be n’amakode ya QR. Nk’akarorero, kubera izo kode za BCH, kode ya QR ipfutse igice irashobora gusomwa no gusobanurwamwo.


Mu bijanye na Bitcoin, amakode ya BCH atanga ugusenyera ku mugozi umwe hagati y’ubunini n’ubushobozi bwo kumenya amakosa ugereranyije n’ibikorwa vyoroshe vya Hash bikoreshwa ku maderesi *Legacy*. Ariko rero, muri Bitcoin, amakode ya BCH akoreshwa gusa mu kumenya amakosa, ntakoreshwa mu gukosora. Gutyo, porogarama ya Wallet izokwerekana ko Address yakira nabi ariko ntizokwikosora ubwo nyene. Ivyo bigabanywa ni ibigirankana: kwemera gukosora ubwavyo vyogabanya ubushobozi bwo kumenya amakosa.


Kugira ngo tubare umubare w’ibintu bigenzurwa dukoresheje amakode ya BCH, turakeneye gutegura Elements nyinshi.


- Igiharuro c'ubuzima (*Igice gisomwa n'umuntu*): Ku bijanye na Bitcoin Mainnet, igiharuro c'ubuzima ni `bc`;


HRP itegerezwa kwaguka mu gutandukanya ikimenyetso cose mu bice bibiri:


- Gufata inyuguti za HRP muri ASCII:
 - 'b`: '01100010'
 - 'c': '01100011'
- Gukuraho ibice 3 bihambaye cane n'ibice 5 bihambaye cane:
  - 3 ibice bihambaye cane: `011` (3 mu cumi)
  - 3 ibice bihambaye cane: `011` (3 mu cumi)
  - 5 ibice bifise akamaro gatoyi: `00010` (2 mu cumi)
  - 5 ibice bifise akamaro gatoyi: `00011` (3 mu cumi)


Hamwe n'itandukaniro `0` hagati y'inyuguti zibiri, HRP rero ni:


```text
03 03 00 02 03
```



- **Verisiyo y'icabona**: Ku verisiyo ya SegWit 0, ni `00`;



- **Igikoresho**: Agaciro k'icumi k'urufunguzo rwa bose Hash;



- **Igiharuro c'isuzuma**: Twongerako zero 6 `[0, 0, 0, 0, 0, 0]` ku mpera y'urutonde.


Amakuru yose ahurijwe hamwe kugira ngo yinjizwe muri porogarama yo kubara umubare w’igenzura ni aya:


```text
HRP = 03 03 00 02 03
SEGWIT v0 = 00
HASH = 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21
CHECKSUM = 00 00 00 00 00 00

INPUT = 03 03 00 02 03 00 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21 00 00 00 00 00 00
```


Ibara ry’umubare w’ibintu bigenzurwa ni ikintu gikomeye cane. Birimwo imibare y'umurima w'iherezo ry'ibiharuro vyinshi. Ntituzodondora neza iyo mibare hano kandi tuzoca tuja ku ciyumviro. Mu karorero kacu, umubare w'igenzura uboneka mu cumi ni:


```text
10 16 11 04 13 18
```


Ubu turashobora kwubaka Address yakira mu gufatanya mu buryo bukurikira Elements ikurikira:


- **Verisiyo ya SegWit**: `00`
- **Ivyo bikoresho**: Urufunguzo rwa bose Hash
- **Igitigiri c'igenzura**: Agaciro kabonetse mu ntambwe imbere (`10 16 11 04 13 18`)


Ivyo biduha mu cumi:


```text
00 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21 10 16 11 04 13 18
```


Hanyuma, agaciro k'icumi kose kagomba gushushanirizwa n'ikimenyetso *bech32* hakoreshejwe imbonerahamwe y'uguhindura ikurikira:



$$

\begin{array}{|c|c|c|c|c|c|c|c|c|}
\hline
& 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 \\
\hline
+0 & q & p & z & r & y & 9 & x & 8 \\
\hline
+8 & g & f & 2 & t & v & d & w & 0 \\
\hline
+16 & s & 3 & j & n & 5 & 4 & k & h \\
\hline
+24 & c & e & 6 & m & u & a & 7 & l \\
\hline
\end{array}

$$


Kugira ngo uhindure agaciro mu nyuguti _bech32_ ukoresheje iyi mbonerahamwe, ushobora gusa kurondera agaciro kari mu nkingi ya mbere n'umurongo wa mbere, iyo wongerewe hamwe, utanga igisubizo wipfuza. Hanyuma, ushiremwo ikimenyetso gihuye. Nk’akarorero, umubare w’icumi `19` uzohindurwa urudome `n`, kuko $19 = 16 + 3$.


Mu gukora ikarita y’agaciro kacu kose, turonka Address ikurikira:


```
qn7qnytxgsc3v5nxt9ff2y83g3pe84ff42stydj
```


Igisigaye ni uko wongerako HRP `bc`, yerekana ko ari Address ku Bitcoin Mainnet, hamwe n’igitandukanya `1`, kugira ngo uronke Address yuzuye yakira:


```
bc1qn7qnytxgsc3v5nxt9ff2y83g3pe84ff42stydj
```


Ikintu kidasanzwe c’iyi nyuguti _bech32_ ni uko irimwo inyuguti zose z’inyuguti n’imibare kiretse `1`, `b`, `i`, na `o` kugira ngo ntihagire uwuvyura urujijo mu kubona hagati y’inyuguti zisa n’izo, cane cane mu gihe ziriko zirasomwa canke zisomwa n’abantu.


Mu ncamake, ng’iyi inzira y’ugukura:


![CYP201](assets/fr/065.webp)


Uko ni ko umuntu ashobora gukura P2WPKH (SegWit v0) yakira Address mu mfunguruzo zibiri. Reka noneho tuje ku ma aderesi ya P2TR (SegWit v1 / Taproot) maze tubone ingene zivyara.


### Ivyakomoka kuri SegWit v1 (imirongo32) Address


Ku ma aderesi ya Taproot, uburyo bwo guhingura buratandukanye gatoyi. Ivyo reka tubirabe hamwe!


Kuva ku ntambwe y’ugufatanya urufunguzo rwa bose, itandukaniro rya mbere riboneka ugereranyije na ECDSA: urufunguzo rwa bose rwakoreshejwe kuri Schnorr muri Bitcoin rugereranywa gusa n’urufunguzo rwazo rwitwa abscissa ($x$). Nta n’intango rero iriho, kandi urufunguzo rwo gufatanya rupima neza na neza ibice 256.

Nk’uko twabibonye mu kigabane c’imbere, inyandiko ya P2TR ifunga ama bitcoins ku rufunguzo rwa bose rwihariye rwa Schnorr, rwerekanwa na $Q$. Uru rufunguzo $Q$ ni umugwi w'imfunguruzo zibiri za bose: $P$, urufunguzo rwa bose rw'imbere, na $M$, urufunguzo rwa bose ruva kuri Merkle Root y'urutonde rwa _scriptPubKey_. Ivyo bice vy’amahera vyugarijwe n’ubwo bwoko bw’inyandiko bishobora gukoreshwa mu buryo bubiri:



- Mu gutangaza umukono w'urufunguzo rwa bose $P$ (_inzira y'urufunguzo_);
- Mu guhazwa n'imwe mu nyandiko ziri muri Merkle Tree (_inzira y'inyandiko_).


Mu vy'ukuri, izo mfunguruzo zibiri ntizikoranye vy'ukuri. Urufunguzo $P$ ahubwo ruhindurwa n'urufunguzo $M$. Mu buhinga bw'ibanga, "guhindura" urufunguzo rwa bose bisigura guhindura urufunguzo hakoreshejwe agaciro k'inyongera kitwa "guhindura." Iyi nzira ituma urufunguzo rwahinduwe ruguma rujanye n'urufunguzo rw'ibanga rw'umwimerere n'ivyo guhindura. Mu buryo bw'ubuhinga, tweak ni agaciro ka scalar $t$ kongerwa ku rufunguzo rwa mbere rwa bose. Niba $P$ ari urufunguzo rwa bose rw'umwimerere, urufunguzo rwahinduwe ruhinduka:



$$

P' = P + t \cdot G

$$


Aho $G$ ari umugenzuzi w’umurongo w’uruzitiro ukoreshwa. Iyi nzira itanga urufunguzo rushasha rwa bose ruva ku rufunguzo rw’intango, mu gihe ruguma rufise imiterere y’ubuhinga bwo gukingira amakuru yemerera gukoreshwa.


Niba udakeneye kwongerako izindi nyandiko (gukoresha gusa biciye mu nzira y'urufunguzo_), ushobora generate Taproot Address ishinzwe gusa ku rufunguzo rwa bose ruri mu burebure bwa 5 bwa Wallet yawe. Muri ivyo, birakenewe gukora inyandiko idashobora gukoreshwa ku _inzira y'inyandiko_, kugira ngo ushobore gushitsa ibisabwa n'imiterere. Ivyo bihinduka $t$ bica biharurwa hakoreshejwe igikorwa ca Hash, **`TapTweak`**, ku rufunguzo rwa bose rw'imbere $P$:



$$

t = \text{H}_{\text{TapTweak}}(P)

$$


hehe:



- $\umwandiko{H}_{\umwandiko{KandaTweak}}$ **ni SHA256 Hash umukozi ushizweko ikimenyetso** `KandaTweak`. Niba utazi neza ico igikorwa ca Hash gifise ikimenyetso ari co, ndagutumiye ngo urabe igice ca 3.3;
- $P$ ni urufunguzo rwa bose rw'imbere, ruserukirwa mu buryo bwarwo bufise 256-bit, rukoresha gusa $x$ coordinate.


Urufunguzo rwa bose rwa Taproot $Q$ rero ruharurwa mu kwongerako tweak $t$, igwijwe n'umuhinguzi w'umurongo w'uruzitiro $G$, ku rufunguzo rwa bose rw'imbere $P$:



$$

Q = P + t \cdot G

$$


Igihe urufunguzo rwa bose rwa Taproot $Q$ rubonetse, turashobora generate Address ihuye n'iyo. Mu buryo butandukanye n’ibindi bikoresho, amaderesi ya Taproot ntashirwa kuri Hash y’urufunguzo rwa bose. Rero, urufunguzo $Q$ rwinjizwa ataco ruhinduye muri Address, mu buryo butagiramwo ivyiza.


Kugira ngo dutangure, dukuraho $x$ coordinate y’akarongo $Q$ kugira ngo turonke urufunguzo rwa bose rwacitse. Kuri iyo nzira, umubare w’isuzuma ubarwa hakoreshejwe amakode ya BCH, nk’uko biri ku maderesi ya SegWit v0. Ariko rero, porogarama ikoreshwa ku maderesi ya Taproot iratandukanye gatoyi. Nkako, inyuma y'ugushiraho uburyo _bech32_ na SegWit, havumbuwe ikibazo: iyo ikimenyetso ca nyuma ca Address ari `p`, kwinjiza canke gukuraho `q`s imbere gato y'iyi `p` ntibituma umubare w'igenzura utagira akamaro. Naho iki gikoko kitagira ingaruka kuri SegWit v0 (kubera ubunini), coshobora gutera ingorane muri kazoza. Iyi bug rero yarakosowe ku ma aderesi ya Taproot, kandi uburyo bushasha bwakosowe bwitwa "_bech32m_".


Taproot Address ivugwa mu gushiramwo $x$ y'ibara rya $Q$ mu buryo bwa _bech32m_, n'iyi Elements ikurikira:



- **HRP (_Igice Gisomwa n'Umuntu_)**: `bc`, kugira ngo yerekane urusobe nyamukuru rwa Bitcoin;
- **Verisiyo**: `1` kugira ngo yerekane Taproot / SegWit v1;
- **Igitigiri c'igenzura**.


Address ya nyuma rero izogira uburyo:


```
bc1p[Qx][checksum]
```


Ku rundi ruhande, niwaba wipfuza kwongerako izindi nyandiko uretse gukoresha urufunguzo rwa bose rw’imbere (_inzira y’inyandiko_), ibara rya Address yakira rizoba ritandukanye gatoyi. Uzokenera gushiramwo Hash y’inyandiko zindi mu kubara tweak. Muri Taproot, inyandiko yose, iri ku mpera ya Merkle Tree, yitwa "ibabi".


Igihe inyandiko zitandukanye zishobora kwandikwa, utegerezwa kuzica ku giti cabo biciye ku gikorwa ca Hash `TapLeaf`, kiherekejwe n'amakuru amwe amwe:



$$

\text{h}_{\text{leaf}} = \text{H}_{\text{TapLeaf}} (v \Vert sz \Vert S)

$$


Hamwe:



- $v$: umubare w'inyandiko (`0xC0` ku Taproot);
- $sz$: ubunini bw'inyandiko ikodeshejwe mu buryo bwa _CompactSize_;
- $S$: inyandiko.


Ivyanditswe bitandukanye ($\text{h}_{\text{leaf}}$) bibanza gutorwa mu buryo bw'inkoranyabumenyi. Hanyuma, zica zifatanywa zibiri zibiri zigaca mu gikorwa ca Hash `TapBranch`. Ivyo bisubirwamwo kugira ngo wubake, intambwe ku yindi, Merkle Tree:

$$

\text{h}_{\text{branch}} = \text{H}_{\text{TapBranch}}(\text{h}_{\text{leaf1}} \Vert \text{h}_{\text{leaf2}})

$$


Turaheza tukabandanya mu gufatanya ibisubizo bibiri bibiri, tukabirenga ku ntambwe yose biciye ku gikorwa ca Hash `TapBranch`, gushika turonse umuzi wa Merkle Tree:


![CYP201](assets/fr/066.webp)


Igihe Merkle Root $h_{\text{umuzi}}$ imaze kubarwa, turashobora kubara tweak. Ku bw'ivyo, dufatanya urufunguzo rwa bose rw'imbere rwa Wallet $P$ n'umuzi $h_{\text{umuzi}}$, hanyuma tukabica vyose mu gikorwa ca Hash `TapTweak`:



$$

t = \text{H}_{\text{TapTweak}}(P \Vert h_{\text{root}})

$$


Ubwa nyuma, nk’uko vyari biri imbere, urufunguzo rwa bose rwa Taproot $Q$ ruronswa mu kwongerako urufunguzo rwa bose rw’imbere $P$ ku gicuruzwa c’ihinduka $t$ n’inzira y’umuyagankuba $G$:



$$

Q = P + t \cdot G

$$

Hanyuma, uruvyaro rwa Address rukurikira iyo nzira nyene, rukoresheje urufunguzo rwa bose rudasanzwe $Q$ nk’umuzigo w’inyungu, ruherekejwe n’ibindi bimenyetso vy’inyongera.


Kandi ng’aho ni ho ufise! Twarashitse ku mpera y’iri shure rya CYP201. Niba mwabonye ko iri shure rifasha, noshima cane iyo mufata umwanya mutoyi mukariha igiharuro ciza mu kigabane c’isuzuma gikurikira. Ntutinye kandi kubisangiza abo ukunda canke ku mbuga zawe zo gusangirirako amakuru. Ubwa nyuma, nimba wipfuza kuronka impapuro z’umutsindo z’iyi nyigisho, urashobora gukora ikizame ca nyuma ubwo nyene inyuma y’igice c’isuzuma.

# Igice ca nyuma

<partId>58111408-b734-54db-9ea7-0d5b67f99f99</partId>


## Amasuzuma n'Ibipimo

<chapterId>0cd71541-a7fd-53db-b66a-8611b6a28b04</chapterId>

<isCourseReview>true</isCourseReview>

## Ikibazo canyuma

<chapterId>a53ea27d-0f84-56cd-b37c-a66210a4b31d</chapterId>

<isCourseExam>true</isCourseExam>

## Iciyumviro

<chapterId>d291428b-3cfa-5394-930e-4b514be82d5a</chapterId>

<isCourseConclusion>true</isCourseConclusion>