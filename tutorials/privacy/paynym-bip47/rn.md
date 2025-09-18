---
name: BIP47 - PayNym

description: Uko PayNyms ikora
---
***IMBURIZO:** Inyuma y'aho abashinze Samourai Wallet bafashwe, ama server yabo bagafatwa kw'igenekerezo rya 24 Ndamukiza, iyo application ntizosubira gukoreshwa n'abakoresha badafise Dojo yabo. BIP47 iguma ikoreshwa kuri Sparrow wallet ku bakoresha bose na **kuri Samourai Wallet ku bakoresha bafise Dojo gusa**.*


_Turiko turakurikirana cane iterambere ry’uru rubanza hamwe n’iterambere ryerekeye ibikoresho bijana. Nimwizere ko tuzosubiramwo iyi nyigisho uko amakuru mashasha azoboneka._


_Iyi nyigisho itangwa ku ntumbero y'inyigisho n'amakuru gusa. Ntidushigikira canke ngo turemeshe gukoresha ivyo bikoresho mu ntumbero z’ubugizi bwa nabi. Ni inshingano y'ukoresha wese kwubahiriza amategeko ari mu bubasha bwiwe._


---

> Bose baravuga bati: «Ni munini cane», maze iyo nkoko y’inkoko, yari yavutse ifise amababa, yiyumvira ko ari umwami w’abami, iravyimba nk’ubwato bufise amababa yose, maze iragenda igororotse imugana n’ishavu ryinshi, amaso yayo atukura nk’umuriro. Uwo mwana w’intare w’umukene ntiyamenya nimba yohagarara canke yohunga, kandi ntiyanezerewe cane kuko yasuzugurwa n’intare zose zo mu rugo.

![BIP47, the ugly duckling illustration](assets/1.webp)


Kimwe mu bibazo bihambaye cane ku bijanye n’amasezerano ya Bitcoin ni ugusubira gukoresha Address. Uguseruka no gukwiragizwa kw’urubuga bituma iyo ngeso iba akaga ku buzima bwite bw’abakoresha. Kugira ngo umuntu yirinde ingorane zijanye n’ivyo, birakenewe ko umuntu akoresha igitabu gishasha kironka Address ku giciro gishasha cose cinjira ku Wallet, ivyo bikaba bishobora kugora gushikako mu bihe bimwebimwe.


Ukwo gusenyera ku mugozi umwe ni ukwa kera nk’Igitabu Cera. Satoshi yari amaze kutugabisha ku bijanye n’ico kigeragezo mu gitabu ciwe casohowe mu mpera z’umwaka w’2008:


> Nk’uruhome rw’umuriro rw’inyongera, urufunguzo rushasha rukwiye gukoreshwa ku bijanye n’ugucuruza kwose kugira ngo ntiruhuzwe n’uwundi muntu.

Hariho inyishu nyinshi zo kwakira amahera menshi ata Address isubira gukoreshwa. Umwe wese muri bo arafise ivyo ashobora gusenyera ku mugozi umwe be n’ivyo ashobora gusenyuka. Muri ivyo bisubizo vyose, harimwo [BIP47](BIP47](https/github.com/BIPs/blob/master/BIP-0047.mediawiki), igitekerezo categuwe na Justus Ranvier kigasohorwa mu 2015, gishobora gutuma habaho amakode yo kwishura ashobora gusubirwamwo. Intumbero yayo ni ugutuma umuntu ashobora gukoresha amafaranga menshi ataco akoresheje Address.


Mu ntango, ico ciyumviro carasuzuguwe n'abanyagihugu, kandi nticigeze congerwa kuri Bitcoin core. Ariko rero, hariho porogarama zimwezimwe zahisemwo kubishira mu ngiro ku giti cabo. Nk’akarorero, Samourai Wallet yarateguye uburyo bwayo bwo gushirwa mu ngiro bwa BIP47: PayNym. Ubu, iyo nzira y’ugushirwa mu ngiro iraboneka kuri Samourai Wallet ku matelefone ngendanwa, no kuri [Sparrow wallet](https://sparrowwallet.com/) ku ma PC.


Igihe kirenze, Samourai yarateguye ibintu bishasha bijanye na PayNym. Ubu, hariho ibikoresho vyose bishobora gukoreshwa mu gutuma ubuzima bwite bw'abakoresha bugenda neza bishingiye kuri PayNym na BIP47.

Muri iki kiganiro, uzobona ingingo ngenderwako ya BIP47 na PayNym, uburyo ayo masezerano akora, n’ingene akoreshwa mu buryo ngirakamaro biva muri yo. Nzokora Address gusa verisiyo ya mbere ya BIP47, ubu ikoreshwa kuri PayNym, ariko verisiyo 2, 3, na 4 zikora hafi mu buryo bumwe.


**Iciyumviro** ko itandukaniro rikomeye ryonyene riboneka mu gutangaza:


- Verisiyo ya 1 ikoresha Address yoroshe iri kumwe na OP_RETURN kugira ngo imenyekane,
- Verisiyo ya 2 ikoresha inyandiko ya Multisig (ishurwe-Multisig) iri kumwe na OP_RETURN, .
- Kandi verisiyo 3 na 4 zikoresha gusa inyandiko ya Multisig (cfilter-Multisig).


Uburyo bwavuzwe muri iki kiganiro, harimwo n’uburyo bwo gukora amakuru y’ibanga bwigwa, burakoreshwa rero ku mirongo ine yose. Kugeza ubu, ugushirwa mu ngiro kwa PayNym kuri Samourai Wallet na Sparrow bikoresha verisiyo ya mbere ya BIP47.


## Icegeranyo:


1- Ikibazo co gusubira gukoresha Address.


2- Ingingo ngenderwako za BIP47 na PayNym.


3- Ivyigwa: Gukoresha PayNym.



- Kubaka ubucuruzi bwa BIP47 na Samourai Wallet.
- Kubaka ubucuruzi bwa BIP47 na Sparrow wallet.


4- Ibikorwa vya BIP47.



- Kode y’ukwishura ishobora gusubirwamwo.
- Uburyo bwo gupfuka: Urufunguzo rwa Diffie-Hellman Exchange rwashinzwe ku bipimo vy’imirongo (ECDH).
- Ivyo gutangaza ivy’ugucuruza.
- Kubaka igikorwa co gutangaza.
- Kwakira itangazo ry’ugucuruza.
- Ivyo bikorwa vyo kwishura BIP47.
- Kwakira amahera ya BIP47 no gukura urufunguzo rw’ibanga.
- Gusubiza amahera ya BIP47.


5- Ikoreshwa rya PayNym rikomoka.


6- Iciyumviro canje bwite kuri BIP47.


## Ikibazo co gusubira gukoresha Address.


Address yakira ikoreshwa mu kwakira ama bitcoins. Iva ku rufunguzo rwa bose mu kurushiramwo no gukoresha uburyo bumwe bumwe. Gutyo, bituma habaho uburyo bushasha bwo gukoresha amahera ku ndege ya Coin kugira ngo hahindurwe nyen’iyo ndege.


Kugira ngo umenye vyinshi ku bijanye no gutanga Address yakira, ndagusavye gusoma igice ca nyuma c’iki kiganiro: **Bitcoin Wallet - igice kivuye muri** [ebook Bitcoin Démocratisé 2](Igitabu c'Igitabu c'Igihugu c'Igihugu c'Igihugu c'Igihugu c'Igihugu c'Igihugu c'Igihugu c'Igihugu).


Ikindi, kumbure waramaze kwumva ku muntu afise ubumenyi mu vy’ubuhinga bwa bitcoiner ko kwakira amaderesi ari ayo gukoresha rimwe gusa, kandi ko ukwiye generate nshasha ku giciro gishasha cose kija kuri Wallet yawe. Sawa, ariko kuki?


Mu vy’ukuri, gusubira gukoresha Address ntibitera ingorane amahera yawe ata guca ku ruhande. Gukoresha ubuhinga bwo gukingira amakuru ku bigobe vy’uruzitiro bigufasha kwemeza urubuga ko ufise urufunguzo rw’ibanga utahishuriye urwo rufunguzo. Rero, urashobora gufunga ama UTXO menshi atandukanye (Ibisohoka mu bikorwa bitakoreshejwe) kuri Address imwe maze ukayakoresha mu bihe bitandukanye. Iyo utahishuye urufunguzo rw’ibanga rujanye n’iyo Address, nta n’umwe ashobora gushika ku mahera yawe. Ikibazo co gusubira gukoresha Address gifitaniye isano cane n’ubuzima bwite.


Nk’uko vyavuzwe mu ntangamarara, uguseruka no gukwiragiza urubuga rwa Bitcoin bisigura ko uwukoresha wese afise uburenganzira bwo gukoresha node ashobora kwihweza ibikorwa vy’uburyo bwo kwishura. Ivyo bituma bashobora kubona uburinganire butandukanye bw’amaderesi. Satoshi Nakamoto yaciye avuga ko bishoboka ko haba amaderesi mashasha, ku bijanye n'amahera yose yinjira kuri Wallet. Intumbero yoba iyo kugira uruhome rw’umuriro rw’inyongera mu gihe hoba hariho isano hagati y’akaranga k’ukoresha n’imwe mu nzira zabo zibiri z’ingenzi.


Muri iki gihe, kubera ko hariho amashirahamwe y’isesengura ry’uruzitiro be n’uguteza imbere ubuhinga bwa KYC (Know Your Customer), gukoresha amaderesi ataco avuga ntibikiri ikintu co kwongerako, ahubwo ni inshingano ku muntu wese yitwararika mbere n’agatoyi ubuzima bwiwe bwite.


Gukurikirana ubuzima bwite si ihumure canke ivyiyumviro vy’aba Bitcoiners ba Maximalist. Ni parametere yihariye igira ingaruka zitaziguye ku mutekano wawe bwite no ku mutekano w’amahera yawe. Kugira ngo ivyo ubitahure, ng’aka akarorero gatomoye cane:



- Bob agura Bitcoin biciye mu gupima igiciro c’amadolari (DCA), bisobanura ko aronka amahera makeyi ya Bitcoin mu bihe bitandukanye kugira ngo ashobore gupima igiciro ciwe co kwinjira. Bob yohereza mu buryo bubereye amahera yaguzwe kuri Address nyene yakira. Agura 0.01 Bitcoin buri ndwi akayirungika kuri iyo Address nyene. Inyuma y’imyaka ibiri, Bob yarirundanirije Bitcoin yose kuri iyi Address.
- Umutetsi w’imikate ari ku mfuruka yemera amahera ya Bitcoin. Bob anezerewe cane no kuba ashoboye gukoresha Bitcoin, aca aja kugura baguette yiwe mu masatoshi. Kugira ngo yishure, akoresha amahera yapfungiwe n’igitabu ciwe citwa Address. Umutetsi wiwe ubu arazi ko afise Bitcoin. Ivyo bihembo vyinshi vyoshobora gutuma umuntu agira ishari, kandi Bob irashobora guterwa n’abantu muri kazoza.


Address gusubira gukoresha bituma uwubibona ashobora gukora isano ridashobora guhakanwa hagati y'ama UTXO yawe atandukanye rimwe na rimwe hagati y'akaranga kawe na Wallet yawe yose.

Ni co gituma porogarama nyinshi za Bitcoin Wallet zica zitanga Address nshasha iyo ukanda kuri buto ya "Receive". Ku bakoresha ubudasiba, kugira akamenyero ko gukoresha amaderesi mashasha si ikintu gikomeye gitera ingorane. Ariko rero, ku bijanye n’ubudandaji bwo kuri Internet, Exchange canke isekeza ry’ugutanga intererano, iyo nzitizi irashobora guca ihinduka ikintu kidashobora gutorwa.

Hariho inyishu nyinshi z’ayo mashirahamwe. Imwe yose muri zo irafise ivyiza n’ibibi, ariko gushika n’ubu, kandi nk’uko tuzobibona mu nyuma, BIP47 vy’ukuri iratandukanye n’izindi.


Iki kibazo co gusubira gukoresha Address ntabwo ari ikintu co kwirengagiza muri Bitcoin. Nk’uko mushobora kubibona ku gicapo kiri musi cakuwe ku rubuga rwa oxt.me, igitigiri cose c’abakoresha Address basubira gukoresha Bitcoin ubu ni 52%:

Igishushanyo kivuye kuri OXT.me kigaragaza iterambere ry’igipimo cose c’ugusubira gukoresha Address ku rubuga rwa Bitcoin.


![image](assets/2.webp)

_Inguzanyo: OXT_


Ivyinshi muri ivyo bikoresho bisubira gukoreshwa biva ku bihugu bihinduranya, kubera imvo z’ubushobozi n’uburyohe, bisubira gukoresha iyo Address nyene incuro nyinshi. Kugeza ubu, BIP47 yoba ari umuti mwiza wo guhagarika ico kintu hagati y’uguhanahana amakuru. Ivyo vyofasha kugabanya igitigiri cose c’abasubira gukoresha Address ataco bitera amakimbirane menshi kuri izo nzego.


Ico gipimo c’isi yose ku rubuga rwose ni co gihambaye cane muri iki kibazo. Nkako, gusubira gukoresha Address si ingorane gusa ku muntu yifatanya n’uwo mugenzo, ariko no ku muntu wese akorana na bo. Ugutakaza ubuzima bwite kuri Bitcoin bikora nk’umugera, bikakwiragira kuva ku muntu ukoresha gushika ku wundi. Kwiga ingero y’isi yose ku bikorwa vyose vy’urubuga biratuma dutahura urugero rw’ico kintu.


## Ingingo ngenderwako za BIP47 na PayNym.


BIP47 ifise intumbero yo gutanga uburyo bworoshe bwo kwakira amahera menshi ata Address isubira gukoresha. Ivyo ikora bishingiye ku gukoresha kode yo kwishura ishobora gusubirwamwo.


Gutyo, abarungika benshi barashobora kohereza amahera menshi kuri kode imwe yo kwishura ishobora gusubirwamwo y’uwundi muntu, ata wuyironka akeneye gutanga Address nshasha y’ubusa ku bijanye n’ugucuruza gushasha kwose.


Uwukoresha arashobora gusangira n’abandi kode yiwe yo kwishura (ku mbuga ngurukanabumenyi, ku rubuga rwiwe...) ata ngorane yo gutakaza ubuzima bwiwe bwite, bitandukanye n’umuntu asanzwe aronka Address canke urufunguzo rwa bose.

Kugira ngo ukore Exchange, abakoresha bompi bategerezwa kuba bafise Bitcoin Wallet ifise ugushirwa mu ngiro kwa BIP47, nka PayNym kuri Samourai Wallet canke Sparrow wallet. Ihuriro ry’amakode y’ukwishyura y’abo babiri bakoresha rizoshinga umurongo w’ibanga hagati yabo. Kugira ngo uwo muhora ushireho neza, uwuwurungitse ategerezwa gukora igikorwa co gutanga amakuru kuri Bitcoin Blockchain: igikorwa co kumenyesha (ivyo nzobisigura vyinshi mu nyuma).


Ihuriro ry’amakode y’ukwishura y’abakoresha babiri rituma haba amabanga asangiye ko bo ubwabo generate umubare munini w’amaderesi yihariye yakira Bitcoin (2^32 nyayo). Gutyo, mu vy’ukuri, ukwishyura hakoreshejwe BIP47 ntigurungikwa ku kode y’ukwishyura, ahubwo kwoherezwa ku maderesi asanzwe rwose, akomoka ku kode z’ukwishyura z’abafise uruhara.


Kode y'ukwishyura ikora nk'ikimenyetso c'ukuri, kiva kuri Wallet seed. Mu ntumbero y’ugukura kwa HD Wallet, kode y’ukwishura iri ku burebure bwa 3, ku rugero rwa konti ya Wallet.


![image](assets/3.webp)


Intumbero yayo y'ugukomoka ni 47' (0x8000002F) mu bijanye na BIP47. Nk'akarorero, inzira y'ugukomoka kuri kode y'ukwishura yosubira gukoreshwa yoba: ** m/47'/0'/0'/**


Kugira ngo mubone iciyumviro c’ingene kode yo kwishura isa, ng’iyi iyanje: **PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ21UVRKU5


Ishobora kandi gushirwamwo kode ya QR kugira ngo umuntu ashobore guhanahana amakuru:


![image](assets/4.webp)


Naho PayNym Bots, izo robo ubona kuri Twitter, ni amashusho gusa yerekana kode yawe yo kwishura, yaremwe na Samourai Wallet. Bikoreshwa hakoreshejwe ubuhinga bwa Hash, ivyo bikaba bituma hafi biba bimwe bimwe. Ehe ivyanje n'ikimenyetso cavyo: **+ikiyaga8B1**


![image](assets/5.webp)


Izo Bots ntaco zimaze mu vy’ubuhinga nyazo. Ahubwo, zituma habaho imigenderanire hagati y’abakoresha mu guhingura akaranga k’amaso.


Ku mukoresha, inzira yo kwishura BIP47 n’ugushirwa mu ngiro kwa PayNym ni yoroshe cane. Reka twiyumvire ko Alice ishaka kohereza amahera kuri Bob:


1. Bob asangira kode yiwe ya QR canke ataco akora kode yiwe yo kwishura ishobora gusubira gukoreshwa. Ashobora kubishira ku rubuga rwiwe, ku mbuga ziwe zitandukanye z’abantu bose, canke akabirungikira Alice biciye ku bundi buryo bwo guhanahana amakuru.

2. Alice ifungura porogarama yiwe yitwa Samourai canke Sparrow maze igaca isuzuma canke igashiramwo kode y’ukwishyura ya Bob.

3. Alice ahuza PayNym yiwe n'iya Bob ("Kurikira" mu congereza). Ivyo bikorwa bikorwa off-chain kandi biguma ataco bimaze.

4. Alice ahuza PayNym yiwe n'iya Bob ("Huza" mu congereza). Ivyo bikorwa "On-Chain". Alice itegerezwa kwishura amafaranga y’ugucuruza Mining hamwe n’amafaranga adahinduka y’ama Sats 15.000 ku gikorwa co ku kirwa ca Samourai. Amafaranga y’ibikorwa ararekurwa kuri Sparrow. Iyo ntambwe ni co twita igikorwa co kumenyesha.

5. Igihe igikorwa co kumenyesha cemejwe, Alice irashobora gukora igikorwa co kwishura BIP47 kuri Bob. Wallet yiwe izokwihuta generate ubusa bushasha bwakira Address iyo Bob yonyene ifise urufunguzo rw’ibanga.


Gukora igikorwa co kumenyesha, ni ukuvuga gufatanya PayNym yiwe, ni ikintu gikenewe kugira ngo umuntu ashobore kwishura BIP47. Ariko ivyo bimaze gukorwa, uwurungitse arashobora kwishura incuro nyinshi uwuyakira (2^32 nyavyo) ataco akeneye gukora igikorwa gishasha co kumenyesha.


Ushobora kuba warabonye ko hariho ibikorwa bibiri bitandukanye vyo guhuza PayNyms hamwe: "kurikira" na "guhuza". Igikorwa kijanye n'uguhuza ("connecter") gihuye n'igikorwa co kumenyesha BIP47, ari co gikorwa gusa ca Bitcoin gifise amakuru amwamwe arungikwa biciye ku gisohoka ca OP_RETURN. Gutyo, birafasha gushinga ubutumwa bufise amabanga hagati y’abo bakoresha babiri kugira ngo bashobore gutanga amabanga basangira akenewe kugira ngo bashobore gutanga amaderesi mashasha y’ukwakira ata co avuga.


Ku rundi ruhande, igikorwa co guhuza ("kurikira" canke "kwizigira") kiremesha guhuza kuri Soroban, ubuhinga bwo guhanahana amakuru bushingiye kuri Tor, bwateguwe cane cane n'imigwi ya Samourai.


Mu ncamake:



- Guhuza PayNyms zibiri ("kurikira") ni ubuntu rwose. Ifasha gushinga ubutumwa bushingiye ku nzira ya off-chain, cane cane mu gukoresha ibikoresho vya Samourai vyo gukorana n’abandi (Stowaway canke StonewallX2). Iyi nzira ni iyo PayNym kandi ntidondora muri BIP47.
- Guhuza PayNyms zibiri biratwara igiciro. Ivyo birimwo gukora igikorwa co kumenyesha kugira ngo utangure gukorana. Ico kiguzi gifise amahera yose y’ibikorwa, amahera y’ugucuruza Mining, n’amahera 546 Sats yoherezwa ku itangazo ry’uwuronka Address kugira ngo abamenyeshe ko umugende ufunguwe. Iyi nzira ifitaniye isano na BIP47. Iyo amaze kurangiza, uwurungitse arashobora gutanga amahera menshi ya BIP47 ku muntu yaronse.


Kugira ngo uhuze PayNyms zibiri, zitegerezwa kuba zisanzwe zihujwe.


## Ivyigwa: Gukoresha PayNym.


None ko twabonye inyigisho, reka twige hamwe ingendo. Iciyumviro c'inyigisho zikurikira ni uguhuza PayNym yanje kuri Sparrow wallet yanje na PayNym yanje kuri Samourai Wallet yanje. Inyigisho ya mbere ikwereka ingene wokora igikorwa ukoresheje kode yo kwishura ishobora gusubirwamwo kuva kuri Samourai gushika kuri Sparrow, inyigisho ya kabiri idondora uburyo bumwe kuva kuri Sparrow gushika kuri Samourai.


**Iciyumviro:** Nakoze izo nyigisho kuri Testnet. Ivyo si ama bitcoins nyayo.


### Kubaka ubucuruzi bwa BIP47 na Samourai Wallet.


Kugira ngo utangure, biragaragara ko ukeneye igitabu ca Samourai Wallet. Ushobora kuyikura kuri Google Play Store canke ukoresheje dosiye ya APK iri ku rubuga rwemewe rwa Samourai.


Wallet imaze gutangura, nimba utaratangura, usabe PayNym yawe ukanda ku nkuru (+) iri musi iburyo, hanyuma kuri "PayNym".


Intambwe ya mbere yo kwishura BIP47 ni ukuronka kode y’ukwishura ishobora gusubirwamwo ku muntu twakira. Hanyuma, tuzoshobora kwifatanya na bo hanyuma tuzohuza:


![video](assets/6.mp4)


Igihe itangazo ry’ugucuruza ryemejwe, ndashobora kohereza amahera menshi ku muntu yaronse. Igihe cose umuntu azogurisha, azoca akora ubwo nyene akoresheje urupapuro rushasha rwa Address rudafise ikintu, uwo muntu azoronka afise imfunguruzo. Uwuronka ntaco akeneye gukora, vyose biharurwa ku ruhande rwanje.


Ehe ingene wokora ubucuruzi bwa BIP47 kuri Samourai Wallet:


![video](assets/7.mp4)


### Kubaka ubucuruzi bwa BIP47 na Sparrow wallet.


Nka kurya kwa Samourai, biragaragara ko ukeneye kugira porogarama ya Sparrow. Ivyo biraboneka kuri mudasobwa yawe. Ushobora kuyikura ku [urubuga rwemewe] rwabo(https://sparrowwallet.com/).


Raba neza ko ugenzura neza umukono w’uwawukoze be n’ubutungane bwa porogarama waronse imbere y’uko uyishira ku mashine yawe.


Rema Wallet maze usabe PayNym yawe ukanda kuri "Show PayNym" mu rutonde rwa "Igikoresho" ruri hejuru:


![image](assets/8.webp)


Hanyuma, uzokenera guhuza no guhuza PayNym yawe n’iy’uwuguhaye. Kugira ngo ubikore, shiramwo kode yabo yo kwishura ishobora gusubirwamwo mw'idirisha rya "Rondera uwo mubonana", uyikurikire, hanyuma ukore igikorwa co kumenyesha ukanda kuri "Huza uwo mubonana":


![image](assets/9.webp)


Igihe igikorwa co kumenyesha cemejwe, urashobora kohereza amahera kuri kode y’amahera yo gusubira gukoreshwa. Ehe ingene wobikora:


![video](assets/10.mp4)


Ubu ko twashoboye kwiga uruhande rw’ibikorwa rw’ugushirwa mu ngiro kwa PayNym kwa BIP47, reka turabe ingene ubwo buryo bwose bukora n’uburyo bwo gukora amakuru y’ibanga bukoreshwa.


## Ibikorwa vy’imbere vya BIP47.


Kugira ngo twige uburyo BIP47 ikora, birakenewe cane ko umuntu atahura imiterere y’umurongo w’ubuhinga (HD) Wallet, uburyo bwo gukuraho amajambo y’urufunguzo y’abana, hamwe n’ingingo ngenderwako z’ubuhinga bwo gukingira amakuru y’uruzitiro rw’uruzitiro. Igishimishije, urashobora kuronka amakuru yose akenewe kugira ngo utahure iki gice ku rubuga rwanje:



- [Gutahura inzira z'ugukomoka kw'igikoresho ca Bitcoin Wallet](gutahura imiti-y'ivy'ugukomoka kw'ijambo Bitcoin)



- [Igitabo ca Bitcoin Wallet - igice co mu gitabu ca Bitcoin Democratized 2]


### Kode y’ukwishura ishobora gusubirwamwo.


Nk’uko vyasiguwe mu gice ca kabiri c’iki kinyamakuru, kode yo kwishura ishobora gusubirwamwo iri mu burebure bwa gatatu bwa HD Wallet. Ni nk’aho igereranywa na xpub, mu vyo ishirwamwo no mu mibumbe yayo, no mu ruhara rwayo.


Aha niho hari ibice bitandukanye bigize kode yo kwishura y’ama byte 80:



- _Bayiti 0_: Ivyo bivugwa. Niba ukoresha verisiyo ya mbere ya BIP47, iyi byte izongana na 0x01.
- _Bayite 1_: Umurima w'ibice. Ico kibanza kigenewe gutanga ibindi bimenyetso mu gihe co gukoresha mu buryo budasanzwe. Niba ukoresha PayNym gusa, iyi byte izongana na 0x00.
- _Bayite 2_: Uburinganire bwa y. Iyi byte yerekana 0x02 canke 0x03 bivanye n'uburinganire (umubare w'ibiharuro canke w'ibiharuro) w'agaciro ka y-coordinate y'urufunguzo rwacu rwa bose. Ushaka kumenya vyinshi ku bijanye n'iyi ngeso, soma intambwe ya 1 y'igice ca "Address derivation" c'iki kiganiro.
- _Kuva kuri byte 3 gushika kuri byte 34_: Agaciro ka x. Izo bytes zirerekana x-coordinate y'urufunguzo rwacu rwa bose. Ihuriro rya x na y parity riduha urufunguzo rwacu rwa bose rwacitse.
- _Kuva ku bayiti 35 gushika ku bayiti 66_: chain code. Ico kibanza kigenewe chain code ifatanye n’urufunguzo rwa bose twavuze haruguru.
- _Kuva kuri byte 67 gushika kuri byte 79_: Gushiramwo. Ico kibanza kigenewe ibintu bishobora gushika muri kazoza. Ku bijanye na verisiyo ya 1, tuyuzuza gusa zero kugira ngo tugere ku bytes 80, ari vyo bipimo vy’amakuru y’isohoka rya OP_RETURN.


Aha niho hari igishushanyo c’icumi na gatandatu c’itegeko ryanje ryo kwishura rishobora gusubirwamwo, ryashikirijwe mu gice c’imbere, n’amabara ahuye n’ama bytes yashikirijwe haruguru:

Igikurikira, urakeneye kandi kwongerako byte y'intango "P" kugira ngo umenye ningoga ko turiko turakorana na kode yo kwishura. Iyi byte ni 0x47.


**0x47010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c4. 70c390d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a00000000000000000000000000000000000000000000000


Ubwa nyuma, turaharura umubare w’igenzura ry’iyi kode y’ukwishyura dukoresheje HASH256, bisobanura gukora hashing kabiri n’igikorwa ca SHA256. Turakura ama bytes ane ya mbere y’iyi digest tukayafatanya ku mpera (mu rangi y’umutuku).


**0x47010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c470c3. 90d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a000000000000000000000000000080c4**


Kode yo kwishura irateguye, ubu dukeneye gusa kuyihindura ngo ibe Base 58:


**PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ21UVRKU5


Nk'uko ushobora kubibona, iyi nyubakwa isa cane n'imiterere y'urufunguzo rwa bose rwagutse rw'ubwoko "xpub".


Muri iyo nzira kugira ngo turonke kode yacu yo kwishura, twakoresheje urufunguzo rwa bose rwo mu rwego rwo hejuru be n’urufunguzo rwa chain code. Izo Elements zibiri ni ingaruka y’ugukura kw’ibintu bishingiye ku ntumbero n’ivy’ubukuru biva kuri Wallet seed, hakurikijwe inzira y’ugukura ikurikira: m/47’/0’/0’/


Mu majambo nyayo, kugira ngo turonke urufunguzo rwa bose na chain code y’itegeko ry’ukwishura rishobora gusubirwamwo, tuzoharura urufunguzo rw’ibanga rw’umukuru ruvuye kuri seed, hanyuma turonke abana babiri bafise urutonde 47 + 2^31 (ugukura gukomeye). Hanyuma, turonka abandi bana babiri babiri bafise urutonde 2^31 (ugukura gukomeye).


**Iciyumviro:** niba ushaka kwiga vyinshi ku bijanye no gukuraho urufunguzo rw'abana mu rwego rw'uburongozi Bitcoin Wallet, ndagusavye gufata CRYPTO301.


### Uburyo bwo gucapura: Urufunguzo rwa Diffie-Hellman rwitwa Exchange (ECDH).


Uburyo bwo gukora amakuru bukoreshwa mu mutima wa BIP47 ni ECDH (Diffie-Hellman). Iyi porotokole ni uburyo butandukanye bw'urufunguzo rwa kera rwa Diffie-Hellman Exchange.


Diffie-Hellman, mu nsiguro yayo ya mbere, ni amasezerano y’ingenzi yashikirijwe mu 1976 yemerera abantu babiri, umwe wese afise urufunguruzo rwa bose n’urw’ibanga, kumenya ibanga basangiye mu guhana amakuru biciye ku nzira y’itumanaho idatekanye.


![image](assets/11.webp)


Iryo banga ry’abantu bose (urufunguzo rutukura) rirashobora rero gukoreshwa mu bindi bikorwa. Mu bisanzwe, iri banga rishobora gukoreshwa mu gupfuka no gukuraho ubutumwa ku rubuga rudatekanye:


![image](assets/12.webp)


Kugira ngo Diffie-Hellman ashike kuri iyo Exchange, akoresha imibare y’ibice kugira ngo abare ibanga basangiye. Aha niho hari insobanuro yoroshe y’ingene bikora:



- Alice na Bob bemeranya ibara rimwe, muri iki gihe ni umuhondo. Iri bara rizwi na bose. Ni amakuru ya bose.
- Alice ihitamwo ibara ry’ibanga, muri iki gihe, umutuku. Aca avanga ayo mabara abiri, bigatuma haba umuhondo.
- Bob ihitamwo ibara ry’ibanga, muri iki gihe, ubururu bw’agahama. Avanga ayo mabara abiri, bigatuma haba ubururu bw’ikirere.
- Alice na Bob zishobora Exchange amabara zaronse: umuhondo n’ubururu bw’ikirere. Iyi Exchange ishobora gushika ku rubuga rudatekanye kandi ishobora kwihwezwa n’abatera.
- Alice avanga ibara ry’ubururu bw’ikirere yaronse kuri Bob n’ibara ryiwe ry’ibanga (umutuku). Aronka ibara ry’inzobe.
- Bob avanga ibara ry’umuhondo yaronse kuri Alice n’ibara ryiwe ry’ibanga (ubururu bw’umuhondo). Araronka kandi ibara ry’inzobe.


![image](assets/13.webp)


**Ivyiyumviro:** Iciyumviro c’intango: A.J. Han VinckVector Verisiyo: FlugaalImpinduro: Dereckson, Ivy'abantu bose, biciye ku rubuga rwa Wikimedia. Dosiye:Diffie-Hellman_Urufunguzo_Ruguhindura_(fr).svg


Muri ukwo kworohereza, ibara ry’inzobe rigereranya ibanga ry’abasangiye hagati ya Alice na Bob. Birabereye kwiyumvira ko mu vy’ukuri, bidashoboka ko uwutera atandukanya ibara ry’umuhondo n’ubururu bw’ikirere kugira ngo abone amabara y’ibanga ya Alice canke Bob.


None rero, reka twige ingene ikora vy’ukuri. Umuntu aravye neza, Diffie-Hellman yoshobora gusa n’uwugoye gutahura. Mu vy’ukuri, ingingo ngenderwako y’ugukora ni nk’iy’umwana. Imbere yo kubabwira mu buryo burambuye uburyo bwayo, nzobibutsa ningoga ivyiyumviro bibiri vy’imibare tuzokenera (kandi mu buryo butari bwo, birakoreshwa no mu bundi buryo bwinshi bwo gukora amakuru y’ibanga).


1. Umubare w’intango ni umubare kamere ufise ibigabanywa bibiri gusa: 1 na wo nyene. Nk’akarorero, umubare 7 ni umubare w’intango kuko ushobora gusa kugabanywa na 1 na 7 (ubwawo). Ku rundi ruhande, umubare 8 si umubare w’intango kuko ushobora kugabanywa na 1, 2, 4 na 8. Ku bw’ivyo nta migabane ibiri gusa ufise, ahubwo ufise imigabane ine yuzuye kandi nziza.

2. "Modulo" (igaragazwa na "mod" canke "%") ni igikorwa c'imibare gishobora gutuma imibare ibiri yose igarura igice gisigaye c'ugucapura kwa Euclide kw'umubare wa mbere n'umubare wa kabiri. Akarorero, 16 mod 5 ingana na 1.


Urufunguzo rwa Diffie-Hellman Exchange ruri hagati ya Alice na Bob rukora gutya:



- Alice na Bob zigena imibare ibiri rusangi: p na g. p ni umubare w'intango. Uko uwo mubare p uba munini, niko Diffie-Hellman azoba afise umutekano mwinshi. g ni umuzi w’intango wa p. Ivyo biharuro bibiri bishobora gumenyeshwa mu nyandiko rusangi ku rubuga rudatekanye, ni vyo bingana n’ibara ry’umuhondo mu kworohereza haruguru. Alice na Bob bikeneye gusa kugira agaciro kamwe nyene ka p na g.
- Igihe amaparametere amaze gutorwa, Alice na Bob umwe wese agena umubare w’ibanga w’imburakimazi ku giti ciwe. Igitigiri c’imburakimazi caronswe na Alice citwa a (kingana n’ibara ry’umutuku) igitigiri c’imburakimazi caronswe na Bob citwa b (kingana n’ibara ry’umutuku). Ivyo biharuro bibiri bitegerezwa kuguma ari ibanga.
- Aho guhinduranya iyo mibare a na b, buri ruhande ruzoharura A (inyuguti nini) na B (inyuguti nini) ku buryo:


A ingana na g iduzwe ku bubasha bwa modulo p:

**A = g^a % p**


B ingana na g yaduzwe ku bubasha bwa b modulo p:

**B = g^b % p**



- Ivyo biharuro A (bingana n’ibara ry’umuhondo) na B (bingana n’ibara ry’ubururu bw’ikirere) bizohindurwa hagati y’abo babiri. Exchange ishobora gukorwa mu nyandiko rusangi ku rubuga rudatekanye.
- Alice, ubu azi B, azoharura agaciro ka z ku buryo:


z ingana na B iduzwe ku bubasha bwa modulo p:

**z = B^a % p**



- Nk’ukwibutsa, B = g^b % p. Rero:

**z = B^a % p**

**z = (g^b)^a % p**


Dushingiye ku mategeko y’ugutera imbere:

**(x^n)^m = x^nm**


Rero:

**z = g^ba % p**



- Bob, ubu azi A, na we azoharura agaciro ka z nk’uko bikurikira:


z ingana na A yaduzwe ku bubasha bwa b modulo p:

**z = A^b % p**


Rero:

**z = (g^a)^b % p**

**z = g^ab % p**

**z = g^ba % p**


Kubera ugusangira kw’umukoresha wa modulo, Alice na Bob zironka agaciro kamwe nyene ka z. Uwo mubare ugereranya ibanga basangiye, rikaba ringana n’ibara ry’umuhondo ryari mu nsobanuro ya kera. Bashobora gukoresha iryo banga basangiye kugira ngo bashiremwo amakuru hagati yabo ku rubuga rudatekanye.


![Diffie-Hellman Technical Operation Diagram](assets/14.webp)


Umuntu atera afise p, g, A na B ntazoshobora kubara a, b canke z. Gukora iyo nzira vyosaba guhindura igiharuro, ivyo bikaba bidashoboka gukorwa atari mu kugerageza ubushobozi bwose bumwe bumwe kuko turiko turakorana n’umurima ufise impera. Ivyo vyoba bingana no kubara logarithme itandukanye, ari yo nzira y’ugusubiza inyuma mu mugwi w’inzinguzingu w’iherezo.


Rero, igihe cose duhisemwo agaciro kanini bihagije ka a, b, na p, Diffie-Hellman aratekanye. Mu bisanzwe, n'ibipimo vy'ibice 2.048 (umubare ufise imibare 600 mu cumi), kugerageza ubushobozi bwose bwa a na b ntivyoba ari vyiza. Kugeza ubu, n’imibare y’ubunini nk’ubwo, iyo algorithme ifatwa ko itekanye.


Aho ni ho nyene ikintu nyamukuru gitera ingorane y’amasezerano ya Diffie-Hellman kiri. Kugira ngo iyo algorithme ibe itekanye, itegerezwa gukoresha imibare myinshi. Ivyo vyatumye ubu hakunda ubuhinga bwa ECDH, ari bwo buryo butandukanye bwa Diffie-Hellman bukoresha umurongo w’aligebra, cane cane umurongo w’uruzitiro rw’uruzitiro. Ivyo bituma dukorana n’imibare mikeyi cane mu gihe tuguma dufise umutekano ungana, gutyo tukagabanya ibikoresho bisabwa vyo gukoresha ubuhinga bwo guharura no kubika.


Ingingo rusangi y’ubuhinga bwa algorithme iguma ari imwe. Ariko rero, aho gukoresha umubare w’imburakimazi a n’umubare A ubazwe uhereye kuri a dukoresheje ubuhinga bwo gutera imbere, tuzokoresha imfunguruzo zibiri zishingiye ku nzira y’uruzitiro. Aho kwizigira ugusangira kw’umukoresha wa modulo, tuzokoresha itegeko ry’umugwi ku mirongo y’imirongo, cane cane ubufatanye bw’iri tegeko.

Niba utazi ingene imfunguruzo z’ibanga n’iza bose zikora ku nzira y’uruzitiro rw’uruzitiro, nzogusigurira ivy’ishimikiro vy’ubu buryo mu bice bitandatu vya mbere vy’iki kiganiro.


Mu ncamake, urufunguzo rwihariye ni umubare udasanzwe uri hagati ya 1 na n-1 (aho n ari urutonde rw’umurongo), kandi urufunguzo rwa bose ni akarongo kadasanzwe ku murongo kagenwa n’urufunguzo rwihariye biciye mu kwongerako akarongo no gukubita kabiri kuva ku karongo k’umuyagankuba, nk’uko bikurikira:


**K = k·G**


Aho K ari urufunguzo rwa bose, k ari urufunguzo rw’ibanga, G ni urufunguzo rw’umuyagankuba.


Kimwe mu bintu vy’iyi nzira y’urufunguzo ni uko vyoroshe cane kumenya K iyo uzi k na G, ariko ubu ntibishoboka kumenya k iyo uzi K na G. Ni igikorwa c’inzira imwe.


Mu yandi majambo, urashobora kubara urufunguzo rwa bose mu buryo bworoshe iyo uzi urufunguzo rw’ibanga, ariko ntibishoboka kubara urufunguzo rw’ibanga iyo uzi urufunguzo rwa bose. Uwo mutekano wongeye gushingiye ku kudashobora kubara logarithme itandukanye.


Tuzokoresha iyi nzira kugira ngo duhindure ubuhinga bwacu bwa Diffie-Hellman. Gutyo, ingingo ngenderwako y’imikorere ya ECDH ni iyi:



- Alice na Bob bemeranya ku bijanye n’umurongo w’uruzitiro rw’uruzitiro rutekanye mu buryo bw’ubuhinga bwa crypto n’imirongo yarwo. Aya makuru ni aya bose.
- Alice itanga umubare w’imburakimazi ka, uzoba urufunguzo rwiwe rw’ibanga. Urufunguzo rw’ibanga rutegerezwa kuguma ari ibanga. Agena urufunguzo rwiwe rwa bose Ka mu kwongerako no gutera kabiri uturongo ku nzira y’uruzitiro yatowe.


**Ka = ka·G**



- Bob nayo itanga umubare w’imburakimazi kb, uzoba urufunguzo rwiwe rw’ibanga. Araharura urufunguzo rwa bose rujanye n’ivyo Kb.


**Kb = kb·G**



- Alice na Bob Exchange imfunguruzo zabo za bose Ka na Kb ku rubuga rwa bose rudatekanye.
- Alice ibara akarongo (x, y) ku nzira y’umurongo mu gukoresha urufunguzo rwiwe rw’ibanga ka ku rufunguzo rwa bose rwa Bob Kb.


**(x, y) = ka·Kb**



- Bob abara akarongo (x, y) ku nzira y’umurongo akoresheje urufunguzo rwiwe rw’ibanga kb ku rufunguzo rwa bose rwa Alice Ka.


**(x, y) = kb·Ka**



- Alice na Bob zironka akarongo kamwe ku nzira y’uruzitiro rw’uruzitiro. Ibanga ry’abantu bose rizoba x-coordinate y’iyi nkuru.


Baronka ibanga rimwe basangiye kubera ko:


**(x, y) = ka·Kb = ka·kb·G = kb·ka·G = kb·Ka**


Umuntu ashobora gutera yihweza urubuga rwa bose rudatekanye ashobora gusa kuronka imfunguruzo za bose z’umugwi umwumwe wose n’imirongo y’umurongo yatowe. Nk’uko vyasiguwe imbere y’aho, ayo makuru abiri yonyene ntatuma umuntu ashobora kumenya imfunguruzo z’ibanga, ni co gituma uwutera adashobora gushika ku banga.

ECDH ni ubuhinga bwemerera urufunguzo Exchange. Akenshi ikoreshwa iruhande y’ubundi buryo bwo gukora amakuru y’ibanga kugira ngo umuntu asobanure porotokole. Nk'akarorero, ECDH ikoreshwa mu ntumbero ya TLS (Umutekano w'Ivy'Itwara Layer), uburyo bwo gupfuka no kwemeza bukoreshwa mu gutwara abantu kuri interineti Layer. TLS ikoresha ECDHE ku rufunguzo Exchange, urufunguzo rutandukanye rwa ECDH aho urufunguzo rumara igihe gito kugira ngo rutange ubuzima bwite buhoraho. Uretse ECDHE, TLS ikoresha kandi ubuhinga bwo kwemeza nk'uko ECDSA, ubuhinga bwo gupfuka nk'uko AES, n'igikorwa ca Hash nka SHA256.


TLS isobanura "s" muri "https" n'agashushanyo gatoyi k'urufunguzo ubona ku mucukumbuzi wawe wa internet mu mfuruka yo hejuru ibubamfu, ivyo bikaba vyemeza ko ushobora guhanahana amakuru mu buryo bupfutse. Rero, ubu uriko urakoresha ECDH mu gusoma iyi nkuru, kandi birashoboka ko uyikoresha ku musi ku musi utabizi.


### Itangazo ry'ubucuruzi


Nk’uko twabibonye mu gice ca mbere, ECDH ni uburyo butandukanye bwa Diffie-Hellman Exchange bujanye n’ibice bibiri vy’ingenzi bishingiye ku nzira y’uruzitiro. Amahirwe, dufise amapayi menshi y’ingenzi ahuye n’ico kigereranyo mu masakoshi yacu ya Bitcoin!


Iciyumviro ni ugukoresha amabanga abiri y’ingenzi avuye mu bipapuro vy’ubukuru vy’ubukuru Bitcoin vy’impande zompi kugira ngo hashingwe amabanga basangira kandi y’igihe gito hagati yabo. Muri BIP47, ECDHE (Igiharuro c’Igiharuro c’Igiharuro c’Igiharuro c’Igiharuro) ni co gikoreshwa mu kibanza caco.


ECDHE ikoreshwa mu ntango muri BIP47 kugira ngo ihereze kode y’ukwishura y’uwurungitse ku wuyironka. Iyi ni yo nzira izwi cane yo gutangaza. Kugira ngo BIP47 ikoreshwe, abo bompi (uwurungika amahera n’uwuronka amahera) barakeneye kumenya kode y’amahera y’uwundi. Ivyo ni ngombwa kugira ngo umuntu abone imfunguruzo za bose z’igihe gito, rero n’amaderesi y’ukwakira yihariye.


Imbere y’iyi Exchange, uwuyirungitse aba asanzwe azi kode y’ukwishura y’uwuyironka kuko bari gushobora kuyironka off-chain, nk’akarorero, ku rubuga rwabo canke ku mbuga ngurukanabumenyi. Ariko rero, uwuronka iyo nkuru yoshobora kutamenya vy’ukuri kode y’ukwishura y’uwuyirungitse. Bikenewe ko babashikirizwa, ahandi ho ntibazoshobora gukura imfunguruzo zabo z’igihe gito rero ntibazoshobora kumenya aho ama bitcoins yabo ari no gufungura amahera yabo. Ishobora kubarungikira off-chain, hakoreshejwe ubundi buryo bwo guhanahana amakuru, ariko ivyo vyotera ingorane iyo Wallet ivuye kuri seed.

Nkako, nk’uko namaze kubivuga, amaderesi ya BIP47 ntava kuri seed y’uwuyakira (ahandi ho, vyoba vyiza ukoresheje imwe muri xpubs zabo ataco akora), ariko ni ingaruka y’uguharura birimwo kode y’ukwishura y’uwuyakira n’ikode y’ukwishura y’uwuyirungitse. Rero, iyo uwuronka amafaranga atakaje Wallet yiwe akagerageza kuyigarura kuri seed yiwe, azokenera vy’ukuri kugira ama code yose yo kwishura y’abantu bamurungikiye bitcoins biciye kuri BIP47.


Vyoshoboka gukoresha BIP47 ata n’iyi nzira y’imenyekanisha, ariko umukoresha wese yokenera gukora backup y’amakode y’ukwishyura y’urunganwe rwiwe. Ivyo bizoguma bidashobora gutunganirizwa gushika habonetse uburyo bworoshe kandi bukomeye bwo kurema, kubika no guhindura ivyo bimenyetso. Ivyo gutangaza rero ni nk’itegeko mu gihe ibintu vyifashe ubu.


Uretse uruhara rwayo rwo gukingira amakode y’ukwishyura, nk’uko izina ryayo rivyerekana, iyo nzira y’ugucuruza irakora kandi nk’imenyekanisha ku muntu ayironka. Imenyesha umukiriya wabo ko hariho umugende uherutse gufungurwa.


Imbere yo gusigura mu buryo burambuye ingene ubuhinga bwo gutanga amakuru bukora, noshima kuvuga gatoyi ku bijanye n’akarorero k’ubuzima bwite. Nkako, urugero rw’ubuzima bwite rwa BIP47 rurashingira intahe ingingo zimwe zimwe zifatwa igihe umuntu yubaka iyo nzira y’intango.


Iryo tegeko ry’ukwishura ubwaryo ntiritera ingorane ata guca ku ruhande ubuzima bwite. Udakunze uburyo bwa kera bwa Bitcoin, bushobora guca uruja n’uruza rw’amakuru hagati y’akaranga k’ukoresha n’ibikorwa, cane cane mu kugumiza imfunguruzo za bose zitamenyekana, kode yo kwishura ishobora gufatanywa ata guca ku ruhande n’akaranga. Ivyo si ngombwa, ariko iri huriro ntiriteye akaga.


Nkako, kode y’ukwishura ntiva ata guca ku ruhande ku maderesi akoreshwa mu kwakira amahera ya BIP47. Ahubwo, amaderesi aboneka mu gukoresha ECDHE hagati y’imfunguruzo z’abana z’amakode y’ukwishura y’impande zompi.


Ku bw’ivyo, kode yo kwishura yonyene ntitera ingorane zitaziguye ku buzima bwite kubera ko itangazo Address gusa ari ryo riva muri yo. Hari amakuru umuntu ashobora gukuramwo, ariko mu bisanzwe umuntu ntashobora kumenya uwo uriko urakorana na we.


Ni ngombwa rero ko habaho itandukaniro rikomeye hagati y’amakode y’ukwishura y’abakoresha. Muri ivyo, intambwe ya mbere yo gutangaza amakuru y’itegeko ni igihe gihambaye cane ku bijanye n’ubuzima bwite bw’ukwishura, kandi naho biri ukwo, ni ngombwa kugira ngo iyo porotokole ikore neza. Nimba imwe muri kode zo kwishura ishobora gutorwa ku mugaragaro (nk’akarorero, ku rubuga), kode ya kabiri, ni ukuvuga kode y’uwayirungitse, ntikwiye gufatanywa n’iya mbere.


Nk’akarorero, reka twiyumvire ko nshaka gutanga intererano na BIP47 ku muhari w’imyiyerekano y’amahoro muri Canada:



- Iri shirahamwe ryashizeho kode yaryo yo kwishura ataco rihinduye ku rubuga rwaryo canke ku mbuga ngurukanabumenyi.
- Iryo tegeko rero rifitaniye isano n’ukwinyiganza.
- Ndagarura iyi kode yo kwishura.
- Imbere y’uko mbarungikira amafaranga, ntegerezwa kumenya neza ko bazi kode yanje bwite yo kwishura, iyo kode na yo nyene ikaba ijana n’akaranga kanje kuko ndayikoresha mu kwakira amafaranga avuye ku mbuga zanje z’ubudandaji.


None nobarungikira gute? Iyo ndabarungikiye nkoresheje uburyo busanzwe bwo guhanahana amakuru, ayo makuru yoshobora gusohoka, maze nkamenya ko ndi umuntu ashigikiye imigwi y’amahoro.


Ivyo gutangaza nta gukeka ko atari vyo vyonyene bishobora gutuma umuntu atanga mu mpisho kode y’ukwishyura y’uwurungitse, ariko ubu birarangura neza iyo nshingano mu gukoresha ivyicaro vyinshi vy’umutekano.


Mu kigereranyo kiri aha hepfo, imirongo itukura igereranya igihe uruja n’uruza rw’amakuru rutegerezwa gucika, imyampi yirabura na yo igereranya amahuzu adashobora guhakanwa ashobora gukorwa n’umuntu wo hanze yihweza:


![Privacy model diagram for reusable payment code](assets/15.webp)


Mu vy’ukuri, ku bijanye n’akarorero ka kera k’ubuzima bwite ka Bitcoin, kenshi biragoye guca burundu uruja n’uruza rw’amakuru hagati y’ababiri b’urufunguzo n’uwukoresha, cane cane igihe umuntu ariko arakora ibikorwa vyo kure. Nk’akarorero, iyo hari igikorwa co gutanga intererano, uwuzoyironka azosabwa guhishura Address canke urufunguzo rwa bose ku rubuga rwabo canke ku mbuga ngurukanabumenyi. Ikoreshwa ryiza rya BIP47, ni ukuvuga, n’ugucuruza kw’imenyekanisha, ritorera umuti ico kibazo biciye ku ECDHE n’ugushiramwo amakuru Layer tuzokwiga.


Biragaragara ko uburyo bwa kera bwo gucungera ubuzima bwite bwa Bitcoin buca buboneka ku rugero rw’imfunguruzo za bose z’igihe gito zikomoka ku guhuza amakode abiri y’ukwishura. Ivyo bigereranyo bibiri birafatanya. Nshaka gusa gushimika aha ko, bitandukanye n’ikoreshwa rya kera ry’urufunguzo rwa bose kugira ngo umuntu aronke ama bitcoins, kode yo kwishura ishobora gufatanywa n’akaranga kubera ko amakuru "Bob ariko arakorana na Alice" ameneka mu kindi gihe. Kode yo kwishura ikoreshwa ku maderesi yo kwishura ya generate, ariko mu kwihweza gusa Blockchain, ntibishoboka gufatanya igikorwa co kwishura ca BIP47 n’amakode yo kwishura akoreshwa mu kugikora.


### Ubwubatsi bw'itangazo ry'ubucuruzi


None, reka turabe ingene iyo nzira y’imenyekanisha ikora. Reka twiyumvire ko Alice ishaka kohereza amahera kuri Bob ikoresheje BIP47. Mu karorero kanje, Alice akora nk’uwurungika, Bob na we akora nk’uwuronka. Bob amaze gutangaza kode yiwe yo kwishura ku rubuga rwiwe, rero Alice aramaze kumenya kode yo kwishura ya Bob.


1- Alice ibara ibanga basangira na ECDH:



- Ahitamwo urufunguruzo rubiri muri HD Wallet yiwe ruri kw’ishami ritandukanye n’iryo kode yiwe yo kwishura. Zirikana ko iyo nkuru ibiri idakwiye gufatanywa mu buryo bworoshe n’itangazo rya Alice Address canke akaranga ka Alice (raba igice c’imbere).
- Alice ihitamwo urufunguzo rw’ibanga muri abo babiri. Tuzovyita **a** (inyuguti nto).



- Alice igarura urufunguzo rwa bose rujanye n'itangazo rya Bob Address. Urufunguzo ni umwana wa mbere akomoka kuri kode y’ukwishura ya Bob (index 0). Urufunguzo rwa bose tuzorwita "B" (inyuguti nini). Urufunguzo rw'ibanga rujanye n'urwo rufunguzo rwa bose rwitwa "b" (inyuguti nto). "B" igenwa n'ukwongerako uturongo no gutera kabiri ku nzira y'uruzitiro kuva kuri "G" (uturongo tw'umuyagankuba) n'"b" (urufunguzo rw'ibanga).

**B = b·G**



- Alice iharura akarongo k'ibanga "S" (inyuguti nini) ku nzira y'uruzitiro mu kwongerako akarongo no gukubita kabiri, ikoresheje urufunguzo rwiwe rw'ibanga "a" ku rufunguzo rwa bose rwa Bob "B".

**S = a·B**



- Alice ibara ikintu gihuma amaso "f" kizokoreshwa mu gupfuka kode yiwe yo kwishura. Kugira ngo abikore, azokoresha generate umubare w’ibinyoma akoresheje igikorwa ca HMAC-SHA512. Nk’inyungu ya kabiri muri iyo nzira, akoresha agaciro Bob yonyene izoshobora kuronka: (x), ari ryo x-coordinate y’intangamarara y’ibanga yari yaraharuwe mbere. Injiza ya mbere ni (o), ari yo UTXO ikoreshwa nk’injiza muri iyo nzira (outpoint).

**f = HMAC-SHA512(o, x)**


2- Alice ihindura kode yiwe bwite yo kwishura ikayigira base 2 (binaire).


3- Akoresha iki kintu gihuma amaso nk’urufunguzo rwo gukora encryption symétrique ku payload ya kode yiwe yo kwishura. Uburyo bwo gupfuka amakuru bukoreshwa ni XOR gusa. Ivyo bikorwa bisa n'ivyo Vernam cipher, izwi kandi kw'izina rya "one-time pad":



- Alice ibanza gucapura igice ciwe co guhuma amaso mu bice bibiri: bytes 32 za mbere zitwa "f1" na bytes 32 za nyuma zitwa "f2". Rero dufise:

**f = f1 || f2**



- Alice ibara inyandiko y’ibanga (x’) ya x-coordinate y’urufunguzo rwa bose (x) rw’itegeko ryiwe ryo kwishura, kandi ibara itandukanye inyandiko y’ibanga (c’) ya chain code yiwe (c). "f1" na "f2" bikora nk'imfunguruzo zo gupfuka, kandi igikorwa ca XOR kirakoreshwa.

**x' = x XCANKE f1**

**c' = c XCANKE f2**



- Alice isubirira agaciro nyakuri k’urufunguzo rwa bose (x) na chain code (c) muri kode yiwe yo kwishura n’agaciro kashizwemwo (x’) na (c’).


Imbere yo kubandanya n’insobanuro y’ubuhinga y’iyi nzira y’imenyekanisha, reka dufate umwanya wo kuganira ku gikorwa ca XOR. XOR ni umukoresha w'ibice bishingiye kuri aligebra ya Boolean. Hatanzwe ibikorwa bibiri vy'ibice, igarura 1 iyo ibice bihuye bitandukanye, kandi igarura 0 iyo ibice bihuye bingana. Aha niho hari imbonerahamwe y'ukuri ya XOR ishingiye ku gaciro k'ibikorwa D na E:


| D   | E   | D XOR E |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |

Nk'akarorero:


**0110 XCANKE 1110 = 1000**


Canke:


**010011 XCANKE 110110 = 100101**


Na ECDH, gukoresha XOR nk’ububiko Layer birahuye cane. Ica mbere, kubera uwo mukoresha, ugushiramwo amakuru ni uguhuye. Ivyo bituma uwuronka iyo nsiguro ashobora gukuraho kode y’ukwishyura akoresheje urufunguzo rumwe rukoreshwa mu gufungura. Urufunguzo rwo gupfuka no gufungura ruharurwa bivanye n’ibanga ry’abantu bose hakoreshejwe ECDH.


Ubu bugereranyo bushobozwa n'imiterere y'uguhindura n'ugufatanya kw'umukoresha wa XOR:



- Ibindi bikoresho:

-> D ⊕ D = 0

-> D ⊕ 0 = D



- Uguhinduranya:

D ⊕ E = E ⊕ D



- Ishirahamwe:

D ⊕ (E ⊕ Z) = (D ⊕ E) ⊕ Z = D ⊕ E ⊕ Z



- Uburinganire:

Niba: D ⊕ E = L

Hanyuma: D ⊕ L = D ⊕ (D ⊕ E) = D ⊕ D ⊕ E = 0 ⊕ E = E

-> D ⊕ L = E

Igikurikira, ubwo buryo bwo gushiramwo amakuru burasa cane n’uburyo bwo gushiramwo amakuru bwa Vernam (One-Time Pad), uburyo bwonyene bwo gushiramwo amakuru buzwi gushika ubu bufise umutekano udafise ivyangombwa (canke ushitse). Kugira ngo urufunguzo rwa Vernam rugire ico kiranga, urufunguzo rwo gupfuka rutegerezwa kuba rudasanzwe, rukaba rungana n’ubutumwa, kandi rukoreshwe rimwe gusa. Mu buryo bwo gupfuka bukoreshwa hano kuri BIP47, urufunguzo ni rwo rungana n'ubutumwa, ikintu gihuma amaso ni co nyene gifise ubunini bungana n'ugufatanya x-coordinate y'urufunguzo rwa bose n'ikode y'ukwishyura chain code. Uwo mufunguzo wo gupfuka ukoreshwa vy’ukuri rimwe gusa. Ariko rero, uru rufunguzo ntiruva ku nzira y’imburakimazi itunganye kuko ari HMAC. Ahubwo ni ivy’ibinyoma. Rero, si igiharuro ca Vernam, ariko uburyo bwo kubikora burasa n’ubwo.


Reka dusubire ku bijanye n'ubwubatsi bwacu bw'amatangazo:


4- Alice ubu ifise kode yiwe yo kwishura ifise umuzigo w’amahera ushizwemwo amakuru. Azokora kandi atangaze ibikorwa vy'ubudandaji birimwo urufunguzo rwiwe rwa bose "A" nk'inyungu, igisohoka ku itangazo rya Bob Address, n'isohoka rya OP_RETURN rigizwe na kode yiwe yo kwishura n'umuzigo w'inyungu washizwemwo. Iryo soko ni iryo soko ry’imenyekanisha.


OP_RETURN ni Opcode, ariyo nyandiko igaragaza ko igisohoka c'ibikorwa vya Bitcoin kitagira akamaro. Ubu, rikoreshwa mu gutangaza canke amakuru ya Anchor ku Bitcoin Blockchain. Ishobora kubika amakuru ashika ku bytes 80 yanditswe ku ruzitiro rero akaboneka ku bandi bakoresha bose.


Nk’uko twabibonye mu gice ca mbere, Diffie-Hellman amenyereye generate ibanga ry’abakoresha babiri bavugana ku rubuga rudatekanye, rushobora kwihwezwa n’abatera. Mu BIP47, ECDH ikoreshwa mu guhanahana amakuru ku rubuga rwa Bitcoin, urwo mu kameremere kakaba ari urubuga rwo guhanahana amakuru rubonerana rwobonwa n’abatera benshi. Ibanga ry’abantu bose riharuwe biciye ku rufunguzo rwa Diffie-Hellman Exchange ruri ku nzira y’uruzitiro rw’uruzitiro, rero rikoreshwa mu gupfuka amakuru y’ibanga azorungikwa: kode y’ukwishura y’uwurungitse (Alice).


Aha niho hari igishushanyo cakuwe muri BIP47 kigaragaza ivyo twamaze gusobanura:


![Diagram Alice sends her masked payment code to Bob's notification address](assets/16.webp)


Inguzanyo: Amakode yo kwishura ashobora gukoreshwa kandi ku bikoresho vy’amahera vy’ubukuru, Justus Ranvier. 226/227/blob/umukuru/BIP-0047.mediawiki


Nitwahuza iki kigereranyo n’ivyo nadondoye mbere:



- "Urufunguzo rw'Ibanga rwa Wallet" ku ruhande rwa Alice rujanye n'ibi: a.
- "Umwana Pub-Urufunguzo 0" ku ruhande rwa Bob ruhuye na: B.
- "Ibanga ry'Imenyekanisha" rihuye na: f.
- "Kode y'ukwishyura ipfutse" ihuye na kode y'ukwishyura ipfutse, ni ukuvuga, n'umuzigo w'ukwishyura upfutse: x' na c'.
- "Imenyekanisha ry'Ibikorwa" ni ibikorwa birimwo OP_RETURN.


Reka dusubiremwo intambwe twaciyemwo kugira ngo dukore igikorwa co gutangaza:



- Alice igarura kode y'ukwishyura ya Bob n'itangazo Address.
- Alice ihitamwo UTXO iri yiwe muri HD Wallet yiwe n’urufunguzo rubiri ruhuye.
- Araharura akarongo k’ibanga ku nzira y’uruzitiro akoresheje ECDH.
- Akoresha iyo nkuru y’ibanga kugira ngo abare HMAC, ari yo nkuru ihuma amaso.
- Akoresha ico kintu gihuma amaso kugira ngo apfuke umuzigo w’amahera y’ikode yiwe bwite yo kwishura.
- Akoresha igisohoka c'ibikorwa vya OP_RETURN kugira ngo arungike kode y'ukwishyura kuri Bob.


Kugira ngo dutahure neza ingene ikora, cane cane ikoreshwa rya OP_RETURN, reka twige hamwe igikorwa co gutangaza nyaco. Nakoze igikorwa c’ubwo bwoko kuri Testnet, ushobora kugisanga ukanda hano:


244.0e2e4695a3c49272ef631426a9fd2dae6ec3a469e3a39a3db51aa476cd09de2e


txid: **


![BIP47 Notification Transaction](assets/17.webp)


Inguzanyo: https://ububiko.amakuru/


Mu kwihweza iyo nzira, turashobora kubona ko ifise input imwe n’isohoka 4:



- Igisohoka ca mbere ni OP_RETURN irimwo kode yanje yo kwishura ipfutse.
- Igisohoka ca kabiri ca 546 Sats kigaragaza itangazo ry'uwuronka Address.
- Igisohoka ca gatatu c’ama Sats 15.000 kigereranya amahera y’ibikorwa, nk’uko nakoresheje Samourai Wallet mu kwubaka iyo nzira.
- Igisohoka ca kane c’imiliyoni zibiri za Sats kigereranya ihinduka, ni ukuvuga itandukaniro risigaye n’ivyo nshizemwo risubira ku yindi Address yanje.


Igishimishije cane kwiga ni igisohoka 0 hakoreshejwe OP_RETURN. Reka twihweze neza ivyo irimwo:


![OP_RETURN Output of Notification Transaction BIP47](assets/18.webp)


Inguzanyo: https://ububiko.amakuru/


Turabona inyandiko y'icumi na gatandatu y'igisohoka: **6a4c50010002b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164927b0e8. 8f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d80000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000


Muri iyi nyandiko, turashobora gucapura ibice vyinshi:

Mu ma opcode, turashobora kumenya 0x6a yerekeza kuri OP_RETURN na 0x4c yerekeza kuri OP_PUSHDATA1. Byte ikurikira iyi opcode yerekana ubunini bw'umuzigo ukurikira. Igaragaza 0x50, ni ukuvuga ama bytes 80.


Inyuma y’aho haza kode yo kwishura iri kumwe n’umuzigo w’amahera washizwemwo.


Akira kode yanje yo kwishura ikoreshwa muri iyi nzira:


Mu rwego rwa 58: **PM8TJQCyt6ovbozreUCBrfKqmSVmTzJ5vjqse58LnBzKFFZTwny3KfCDdwTqAEYVasn11tTMPc2FJsFygFd3YzsHvwNXLEQTUGZUGM2GM


Mu rwego rwa 16 (HEX): **4701000277507c9c17a89cfca2d3af554745d6c2db0e7f6b2721a3941a50493103cc42kwongerako94881210d6e 752a9abc8a9fa0070e85184993c4f643f1121dd807dd556d1dc00000000000000000000000008604e4db**


Turagereranije kode yanje yo kwishura n’iya OP_RETURN, turabona ko HRP (mu rangi y’umuhondo) n’ibara ry’ibara ry’umuhondo (mu rangi y’umuhondo) bitarungikwa. Ivyo ni ibisanzwe, kuko ayo makuru agenewe abantu.

Inyuma y’aho, turashobora kumenya (muri Green) verisiyo (0x01), umwanya w’ibice (0x00), n’uburinganire bw’urufunguzo rwa bose (0x02). Kandi, ku mpera y’itegeko ry’ukwishyura, ama bytes ataco amaze ari mu mwijima (0x00) atuma padding ishika ku bytes 80 zose hamwe. Ivyo vyose bimenyeshwa mu nyandiko zisanzwe (zitagiramwo amakuru).

Ubwa nyuma, turashobora kubona ko x-coordinate y’urufunguzo rwa bose (mu bururu) na chain code (mu mutuku) vyashizwe mu mfuruka. Ivyo ni vyo bigize umuzigo w’inyungu w’itegeko ry’ukwishura.


### Kwakira itangazo ry’ugucuruza.


None ko Alice yarungikiye Bob iyo transaction y’imenyekanisha, reka turabe ingene ayisobanura.


Nk’ukwibutsa, Bob itegerezwa kuba ishobora gushika ku kode y’ukwishura ya Alice. Ata ayo makuru, nk’uko tuzobibona mu gice gikurikira, ntazoshobora gukuraho ama key pairs yaremwe na Alice, kandi rero, ntazoshobora gushika ku bitcoins ziwe yaronse na BIP47. Ubu, kode y’ukwishyura ya Alice payload irashizwe mu mfuruka. Reka turabe hamwe ingene Bob ibifungura.


1- Bob akurikirana ibikorwa bitanga ibisubizo n'itangazo ryiwe Address.

2- Iyo igikorwa gifise igisohoka ku itangazo ryiwe Address, Bob iragisuzuma kugira ngo ibone nimba kirimwo igisohoka ca OP_RETURN gihuye n’ingingo ya BIP47.

3- Iyo byte ya mbere y’umuzigo wa OP_RETURN ari 0x01, Bob itangura kurondera ibanga rishoboka ryo gusangira na ECDH:



- Bob ihitamwo urufunguzo rwa bose mu vyo kwinjiza mu bikorwa. Ni ukuvuga, urufunguzo rwa bose rwa Alice rwitwa "A" rufise: **A = a·G**
- Bob ahitamwo urufunguzo rw'ibanga "b" rujanye n'itangazo ryiwe bwite Address: **b**
- Bob abara akarongo k'ibanga "S" (ibanga ryasangiwe na ECDH) ku nzira y'umurongo w'uruzitiro mu kwongerako no gutera kabiri uturongo, akoresheje urufunguzo rwiwe rw'ibanga "b" ku rufunguzo rwa bose rwa Alice "A": **S = b·A**
- Bob igena ikintu gihuma amaso "f" kizotuma ashobora gusobanura umuzigo w'ikode y'ukwishyura ya Alice. Mu buryo bumwe Alice yabiharuriye mbere, Bob izoronka "f" mu gukoresha HMAC-SHA512 kuri (x) agaciro ka x-coordinate k'akarongo k'ibanga "S", no kuri (o) UTXO ikoreshwa nk'inyungu muri iki gikorwa co kumenyesha: **f = H**o-,SHA)1.


4- Bob isobanura amakuru ari muri OP_RETURN y’isoko ry’imenyekanisha nk’itegeko ry’ukwishura. Aca asobanura gusa umuzigo w'iyi kode y'ukwishura akoresheje ikintu gihuma "f".



- Bob itandukanya ikintu gihuma "f" mu bice bibiri: bytes 32 za mbere za "f" zizoba "f1" na bytes 32 za nyuma zizoba "f2".
- Bob ifungura agaciro ka x-coordinate (x') k'urufunguzo rwa bose rwa kode y'ukwishyura ya Alice:


**x = x' XCANKE f1**



- Bob ifungura agaciro ka chain code (c') k'itegeko ry'ukwishyura rya Alice:


**c = c' XCANKE f2**


5- Bob igenzura nimba agaciro k’urufunguzo rwa bose rw’ibara ry’ukwishyura rya Alice kari mu mugwi wa secp256k1. Nimba ari ukwo biri, arabisobanura nk’itegeko ry’ukwishura ribereye. Ahandi ho, arirengagiza ivyo agurisha.


Ubu Bob azi kode y’ukwishura kwa Alice, arashobora kumurungikira amahera ashika kuri 2^32 atazosubira gukora igikorwa co kumenyesha nk’iki.


Ni kuki ivyo bikora? Ni gute Bob ashobora kumenya ikintu kimwe gihuma amaso na Alice maze agaca afungura kode yiwe yo kwishura? Reka dusuzume ingene ECDH ikora mu buryo burambuye twisunze ivyo twahejeje kudondora.


Ica mbere, turiko turakorana n’ugushiramwo amakuru mu buryo buhuye. Ivyo bisigura ko urufunguzo rwo gupfuka n’urufunguzo rwo gufungura ari agaciro kamwe. Muri ivyo, urufunguruzo mu gucuruza itangazo ni ikintu gihuma amaso (f = f1 || f2). Alice na Bob zikeneye kuronka agaciro kamwe ka f ataco zirungitse, kuko uwuyitera yoshobora kuyifata maze akayikuramwo amakuru y’ibanga.


Ico kintu gihuma amaso kiboneka mu gukoresha HMAC-SHA512 ku mibare ibiri: x-coordinate y’aho ibanga n’ivyo UTXO ikoresha mu kwinjiza ivy’ugucuruza. Rero, Bob irakeneye kugira ayo makuru abiri kugira ngo ishobore gusobanura umuzigo w’ikode y’ukwishyura ya Alice.


Ku bijanye n’inyungu UTXO, Bob ishobora gusa kuyigarura mu kwihweza ibikorwa vy’imenyekanisha. Ku bijanye n’ibanga, Bob izobwirizwa gukoresha ECDH.


Nk’uko bigaragara mu gice kivuga kuri Diffie-Hellman, mu guhinduranya imfunguruzo zabo za bose no gukoresha mu mpisho imfunguruzo zabo z’ibanga ku rufunguzo rwa bose rw’uwundi, Alice na Bob barashobora kuronka ikintu kidasanzwe kandi c’ibanga ku nzira y’uruzitiro rw’uruzitiro. Itangazo ry'ugucuruza rishingiye kuri ubu buryo:


Urufunguzo rwa Bob: **B = b·G**


Urufunguzo rwa Alice: **A = a·G**


Ku ntumbero y'ibanga S (x,y): **S = a·B = a·b·G = b·a·G = b·A**


![Diagram of generating a shared secret with ECDHE](assets/19.webp)

Ubu Bob azi kode y’ukwishura kwa Alice, azoshobora kumenya amahera yiwe ya BIP47 maze akureho imfunguruzo z’ibanga zibuza ama bitcoins yaronse.

![Bob interprets Alice's notification transaction](assets/20.webp)


Inguzanyo: Amakode yo kwishura ashobora gukoreshwa kandi ku bikoresho vy’amahera vy’ubukuru, Justus Ranvier. Igitabo c'Ivyabona vya Yehova 305/BIPs/blob/umukuru w'Igihugu


Nitwahuza iki kigereranyo n’ivyo nabasobanuriye mbere:



- "Urufunguzo rwa Wallet" ku ruhande rwa Alice rujanye n'ibi: A.
- "Umwana Priv-Key 0" ku ruhande rwa Bob ruhuye na: b.
- "Ibanga ry'Imenyekanisha" rihuye na: f.
- "Ikode y'ukwishura ipfutse" ihuye na kode y'ukwishura ipfutse ya Alice, ni ukuvuga, n'umuzigo w'inyungu upfutse: x' na c'.
- "Imenyekanisha ry'Ibikorwa" ni ibikorwa birimwo OP_RETURN.


Reka mvuge mu ncamake intambwe twahejeje kubona hamwe kugira ngo twakire no gusobanura itangazo ry’ugucuruza:



- Bob igenzura ibiva mu bikorwa vy'ubudandaji ku itangazo ryiwe Address.
- Iyo abonye imwe, aca aronka amakuru ari muri OP_RETURN.
- Bob ihitamwo urufunguzo rwa bose rw'injiza maze ibara ingingo y'ibanga ikoresheje ECDH.
- Akoresha iyo nkuru y’ibanga kugira ngo abare HMAC, ari yo nkuru ihuma amaso.
- Akoresha ico kintu gihuma amaso kugira ngo ashobore gusobanura kode y'ukwishyura ya Alice iri muri OP_RETURN.


### Ivyo bikorwa vyo kwishura BIP47.


Reka ubu twige uburyo bwo kwishura dukoresheje BIP47. Kugira ndabibutse uko ibintu vyifashe ubu:



- Alice arazi kode y’ukwishura ya Bob, iyo yaronse gusa ku rubuga rwiwe.



- Bob irazi kode y’ukwishura ya Alice kubera igikorwa co kumenyesha.



- Alice izotanga amahera ya mbere kuri Bob. Arashobora gukora n’abandi benshi muri ubwo buryo nyene.


Imbere yo kubasigurira iyo nzira, mbona ko ari vyiza kubabwira index turiko turakorako ubu:


Turadondora inzira y'inkomoko ya kode y'ukwishyura nk'uko bikurikira: m/47'/0'/0'/.


Uburebure bukurikira buratanga urutonde nk'uko bikurikira:



- Umwana wa mbere asanzwe (atakomeye) akoreshwa kugira ngo generate itangazo Address twavuganye mu gice ca mbere: m/47'/0'/0'/0/.



- Urufunguzo rw'abana rusanzwe rukoreshwa muri ECDH gushika kuri generate BIP47 amaderesi y'ukwakira amahera, nk'uko tuzobibona muri iki gice: m/47'/0'/0'/ kuva kuri 0 gushika kuri 2.147.483.647/.



- Urufunguzo rw'abana rukomeye ni amakode y'ukwishura y'igihe gito: m/47'/0'/0'/ kuva kuri 0' gushika kuri 2.147.483.647'/.

Igihe cose Alice ashaka kohereza amahera kuri Bob, aronka Address nshasha idasanzwe, yongera gushimira umurongo wa ECDH:


- Alice ihitamwo urufunguzo rwa mbere rw’ibanga ruva kuri kode yiwe bwite yo kwishura ishobora gusubira gukoreshwa: **a**



- Alice ihitamwo urufunguzo rwa mbere rwa bose rudakoreshwa ruva kuri kode y’ukwishura ya Bob. Urufunguzo rwa bose, tuzorwita "B". Ifatanye n'urufunguzo rw'ibanga "b" Bob gusa ruzi.

**B = b·G**



- Alice ibara akarongo k'ibanga "S" ku nzira y'umurongo w'uruzitiro mu kwongerako no gukubita kabiri uturongo, ikoresheje urufunguzo rwiwe rw'ibanga "a" ku rufunguzo rwa bose rwa Bob "B":

**S = a·B**



- Kuva kuri iyo nkuru y'ibanga, Alice izoharura ibanga ry'abantu bose "s" (inyuguti nto). Kugira ngo abikore, ahitamwo x-coordinate y'akarongo k'ibanga "S" kitwa "Sx", maze akarungika ako gaciro mu gikorwa ca SHA256 Hash.

**s = SHA256(Sx)**


Ntimwizere. Kwemeza! Niba ushaka gutahura ingingo ngenderwako z’ishimikiro z’igikorwa ca Hash, uzosanga ivyo ukeneye muri iki kiganiro. Kandi nimba utizigira NIST (uravuga ukuri), kandi ushaka kuba ushobora gutahura mu buryo burambuye ingene SHA256 ikora, ndagusigurira vyose muri iyi nkuru mu gifaransa.



- Alice ikoresha iri banga "s" kugira ngo ibare amahera ya Bitcoin yakira Address. Ubwa mbere, asuzuma ko "s" iri mu rutonde rw'umurongo wa secp256k1. Nimba atari vyo, yongerako urutonde rw’urufunguzo rwa bose rwa Bob kugira ngo aronke irindi banga basangiye.



- Ica kabiri, abara urufunguzo rwa bose "K0" mu kwongerako uturongo "B" na "s·G" ku nzira y'uruzitiro. Mu yandi majambo, Alice yongerako urufunguzo rwa bose ruva kuri kode y'ukwishyura ya Bob "B" n'iyindi ntumbero iharuwe ku nzira y'umurongo w'uruzitiro mu kwongerako no gukubita kabiri uturongo n'ibanga ry'uruzitiro "s" kuva ku ntumbero y'umurongo w'umurongo wa secp256k1 "G". Iyi ngingo nshasha igereranya urufunguzo rwa bose, kandi turwita "K0":

**K0 = B + s·G**



- Hamwe n'uru rufunguzo rwa bose "K0", Alice ishobora gukuraho ubusa bwakira Address mu buryo busanzwe (nk'akarorero, SegWit V0 muri Bech32).


Igihe Alice afise iyi Address "K0" ya Bob, arashobora kwubaka ubucuruzi bwa Bitcoin mu guhitamwo UTXO ari uwiwe ku rindi shami rya HD Wallet yiwe, maze akayikoresha kuri GW-340-345's.


![Alice sends bitcoins with BIP47 to Bob](assets/21.webp)


Inguzanyo: Amakode yo kwishura ashobora gukoreshwa kandi ku bikoresho vy’amahera vy’ubukuru, Justus Ranvier. Igitabo c'Igihugu c'Igihugu c'Igihugu c'Igihugu

Nitwahuza iki kigereranyo n’ivyo nabasobanuriye mbere:



- "Umwana Priv-Key" ku ruhande rwa Alice ruhuye na: a.
- "Umwana Pub-Key 0" ku ruhande rwa Bob ihuye na: B.
- "Ibanga ry'Ukwishura 0" rihuye na: s.
- "Ukwishura Pub-Key 0" bihuye na: K0.


Reka mvuge mu ncamake intambwe twaciyemwo turi kumwe kugira ngo twohereze amahera ya BIP47:



- Alice ihitamwo urufunguzo rw’ibanga rw’umwana rwa mbere rwavuye muri kode yiwe bwite yo kwishura.
- Araharura akarongo k’ibanga ku murongo w’uruzitiro akoresheje ECDH avuye ku rufunguzo rwa mbere rw’umwana rutakoreshejwe ruvuye ku rufunguzo rwa bose rw’umwana ruvuye kuri kode y’ukwishyura ya Bob.
- Akoresha iyi nkuru y'ibanga kugira ngo abare ibanga asangiye na SHA256.
- Akoresha iryo banga asangiye kugira ngo aharure akarongo gashasha k’ibanga ku nzira y’uruzitiro.
- Yongerako iyo ngingo nshasha y’ibanga ku rufunguzo rwa bose rwa Bob.
- Aronka urufunguzo rushasha rwa bose rw’igihe gito Bob gusa rufise urufunguzo rw’ibanga rujana.
- Alice ishobora kohereza amafaranga asanzwe kuri Bob n'ivyo bivako vyakira Address.


Iyo ashaka kwishura ubwa kabiri, azosubiramwo izo ntambwe zivuzwe haruguru, kiretse azohitamwo urufunguzo rwa bose rwa kabiri ruvuye muri kode y’ukwishura ya Bob. Ni ukuvuga urufunguruzo rukurikira rudakoreshwa. Azoheza agire uwugira kabiri Address ari uwa Bob, "K1".


![Alice derives three BIP47 receiving addresses for Bob](assets/22.webp)


Inguzanyo: Amakode yo kwishura ashobora gukoreshwa kandi ku bikoresho vy’amahera vy’ubukuru, Justus Ranvier. Igitabo c'Ivyabona vya Yehova 368


Ashobora kubandanya gutyo akabona amaderesi 2^32 y'ubusa ari aya Bob.


Uvuye hanze, mu kwihweza Bitcoin Blockchain, mu vyiyumviro ntibishoboka gutandukanya amahera ya BIP47 n’amahera asanzwe. Aha ni akarorero k’ugutanga amahera BIP47 kuri Testnet:


94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254


txid: **94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254**


Bisa n’ugucuruza gusanzwe n’inyungu yakoreshejwe, inyungu y’ukwishyura 210.000 Sats, n’ihinduka.


![Bitcoin payment transaction with BIP47](assets/23.webp)


Inguzanyo: https://ububiko.amakuru/


### Kwakira amahera ya BIP47 no gukura urufunguzo rw’ibanga.


Alice aherutse gutanga amahera yiwe ya mbere ku BIP47 Address y'ubusa ya Bob. None rero reka turabe ingene Bob ironka iyo nkunga. Turabona kandi igituma Alice adashobora gushika ku rufunguzo rw’ibanga rwa Address aherutse gukora, n’ingene Bob asubirana urwo rufunguzo kugira ngo akoreshe ama bitcoins aherutse kuronka.


Bob akimara kwakira itangazo ry'ubudandaji rivuye kuri Alice, aca akura urufunguzo rwa bose rwa BIP47 "K0" mbere n'imbere y'uko ayirungikira amahera. Arabona rero amahera yose yo kwishurwa kuri Address ifatanye n’ivyo. Nkako, aca ahita aronka amaderesi menshi azokwihweza (K0, K1, K2, K3...). Ehe ingene akuraho urufunguzo rwa bose "K0":



- Bob ihitamwo urufunguzo rw’ibanga rw’umwana wa mbere ruva kuri kode yiwe yo kwishura. Urufunguzo rwihariye rwitwa "b". Ifatanye n'urufunguzo rwa bose "B" Alice yakoresheje mu ntambwe ya mbere: **b**



- Bob ihitamwo urufunguzo rwa mbere rwa Alice rwavuye muri kode yiwe yo kwishura. Urufunguzo rwitwa "A". Ifatanye n'urufunguzo rw'ibanga "a" Alice yakoresheje mu biharuro vyiwe, kandi Alice wenyene ni we abizi. Bob arashobora gukora iyo nzira kuko azi kode y’ukwishura ya Alice yamurungikiye hamwe n’isoko ry’imenyekanisha.

**A = a·G**



- Bob ibara akarongo k'ibanga "S" mu kwongerako no gukubita kabiri akarongo ku nzira y'umurongo, akoresheje urufunguzo rwiwe rw'ibanga "b" ku rufunguzo rwa bose rwa Alice "A". Aha dukoresha ECDH, ikaba yemeza ko iyi nkuru "S" izoba imwe kuri Bob na Alice.

**S = B·A**



- Nka kurya kwa Alice, Bob itandukanya x-coordinate y'iyi nkuru "S". Twise aka gaciro "Sx". Aca muri ako gaciro biciye mu gikorwa ca SHA256 kugira aronke ibanga ry'abantu bose "s" (inyuguti nto).

**s = SHA256(Sx)**



- Mu buryo bumwe na Alice, Bob ibara akarongo "s·G" ku nzira y'uruzitiro. Hanyuma, yongerako iyo nkuru y'ibanga ku rufunguzo rwiwe rwa bose "B". Araheza aronka akarongo gashasha ku nzira y'uruzitiro asobanura nk'urufunguzo rwa bose "K0":

**K0 = B + s·G**


Igihe Bob afise urufunguzo rwa bose "K0", arashobora gukura urufunguzo rw'ibanga rujana kugira ngo akoreshe amafaranga yiwe. Ni we wenyene ashobora generate uwo mubare.



- Bob yongerako urufunguzo rwiwe rw'ibanga rw'umwana "b" ruvuye muri kode yiwe bwite yo kwishura. Ni we wenyene ashobora kuronka agaciro ka "b". Hanyuma, yongerako "b" ku banga basangiye "s" kugira ngo aronke k0, urufunguzo rw'ibanga rwa K0: **k0 = b + s**



- Kubera itegeko ry'umugwi ry'umurongo w'uruzitiro, Bob ironka neza urufunguzo rw'ibanga rujanye n'urufunguzo rwa bose rukoreshwa na Alice. Rero dufise: **K0 = k0·G**


![Bob generates his BIP47 receiving addresses](assets/24.webp)


Inguzanyo: Amakode yo kwishura ashobora gukoreshwa kandi ku bikoresho vy’amahera vy’ubukuru, Justus Ranvier. Ubutumwa bw'ikinyamakuru 401-0047


Nitwahuza iki kigereranyo n’ivyo nabasobanuriye mbere:



- "Umwana Priv-Key 0" ku ruhande rwa Bob ruhuye na: b.



- "Umwana Pub-Key 0" ku ruhande rwa Alice ihuye na: A.



- "Ibanga ry'Ukwishura 0" rihuye na: s.



- "Ukwishura Pub-Key 0" bihuye na: K0.



- "Ukwishura Priv-Urufunguzo 0" bihuye na: k0.


Reka mvuge mu ncamake intambwe twahejeje kubona hamwe kugira ngo turonke amahera ya BIP47 maze tubaze urufunguzo rw’ibanga ruhuye:



- Bob ihitamwo urufunguzo rw’ibanga rw’umwana rwa mbere ruvuye muri kode yiwe bwite yo kwishura.



- Aharura ibanga ku murongo w'uruzitiro akoresheje ECDH kuva ku rufunguzo rwa mbere rw'umwana rwa Alice rwa chain code.



- Akoresha iyo nkuru y'ibanga kugira ngo abare ibanga asangiye na SHA256.



- Akoresha iryo banga asangiye kugira ngo aharure akarongo gashasha k’ibanga ku nzira y’umurongo w’uruzitiro.



- Yongerako iyo ngingo nshasha y’ibanga ku rufunguzo rwiwe bwite rwa bose.



- Aronka urufunguzo rushasha rwa bose rw’igihe gito, aho Alice azorungikira amahera yiwe ya mbere.



- Bob ibara urufunguzo rw’ibanga rujanye n’urwo rufunguzo rwa bose rw’igihe gito mu kwongerako urufunguzo rw’ibanga rw’umwana wiwe rwavuye muri kode yiwe yo kwishura n’ibanga ry’abantu bose.


Kubera ko Alice idashobora kuronka "b," urufunguzo rw'ibanga rwa Bob, ntashobora kumenya k0, urufunguzo rw'ibanga rujanye n'urufunguzo rwa Bob rwa BIP47 rwakira Address.


Mu buryo bw'igishushanyo, turashobora guserura ibara ry'ibanga ry'abantu bose "S" nk'uko bikurikira:


![Calculation of the shared secret with ECDHE](assets/25.webp)


Igihe ibanga ry'abantu bose ribonetse na ECDH, Alice na Bob baharura urufunguzo rwa bose rwo kwishura BIP47 "K0," na Bob na yo iharura urufunguzo rw'ibanga rujanye n'ivyo "k0":


![Derivation of the BIP47 receiving address from the shared secret](assets/26.webp)


### Gusubiza amahera ya BIP47.


Kubera ko Bob azi kode ya Alice yo gusubira gukoresha, arasanzwe afise amakuru yose akenewe kugira ngo amurungikire amahera. Ntazokenera guhamagara Alice kugira ngo asabe amakuru yose. Azomumenyesha gusa n’ibikorwa vy’imenyekanisha, cane cane kugira ngo ashobore kugarura amaderesi yiwe ya BIP47 akoresheje seed yiwe, hanyuma ashobore no kumurungikira amahera ashika kuri 2^32.

Bob arashobora rero kwishura Alice mu buryo bumwe nyene yamurungikiye amahera. Uruhara rurahindurwa:


![Bob sends a refund to Alice with BIP47](assets/27.webp)


Inguzanyo: Amakode yo kwishura ashobora gukoreshwa kandi ku bikoresho vy’amahera vy’ubukuru, Justus Ranvier. Igitabo c'amakuru gifise amakuru y'ivy'ubuhinga bwa none


Ubu urazi ins n’outs zose z’uwo muti mwiza cane BIP47 iserukira.


## Ikoreshwa rya PayNym ryakomotse.


Ishirwa mu ngiro ry’iyi BIP47 kuri Samourai Wallet ryatumye habaho PayNyms, ibimenyetso biharurwa bivanye n’amakode y’ukwishura y’abakoresha. Muri iki gihe, akamaro kavyo kararengeye kure cane gukoresha BIP47.


Ishirahamwe rya Samourai ririko ritera imbere buhoro buhoro urutonde rw’ibikoresho n’ibikorwa bishingiye kuri PayNym y’uwukoresha. Muri ivyo, biragaragara ko hariho ibikoresho vyose vyo gukoresha amahera bishobora gutuma umuntu ashobora gutuma ubuzima bwiwe bwite bugenda neza mu kwongerako entropie ku gicuruzwa, gutyo bigatuma umuntu ashobora guhakana.


Ikoreshwa rya Soroban, urubuga rw’itumanaho rwihishije rushingiye kuri Tor, na PayNyms ryatumye abakoresha bashobora gukoresha neza cane igihe bubaka amafaranga y’ubufatanye, mu gihe bagumana urugero rwiza rw’umutekano. Gutyo, biroroshe gukora ibikorwa vya Stowaway (PayJoin) na StonewallX2 ata gukora n’amaboko ibikorwa vyinshi vyo guhindura ibikorwa bitagira umukono bisabwa kugira ngo umuntu ashobore gushinga mwene iyo nzira y’ubufatanye.


Mu buryo butandukanye n’ikoreshwa rya BIP47, kuko ivyo bikorwa vy’ubufatanye bitasaba ibikorwa vy’imenyekanisha, birahagije guhuza PayNyms kugira ngo ukoreshe ivyo bikoresho. Nta co bimaze kubihuza.


Niba ushaka kumenya vyinshi ku bijanye n'ibikorwa vy'ubufatanye, no mu buryo bwagutse ku bijanye n'ibikoresho vyose vyo gukoresha amahera vya Samourai Wallet, urashobora gusoma igice ca "Ibikoresho vyo gukoresha amahera" muri iyi ngingo. Uzosangamwo insobanuro y’ubuhinga n’inyigisho ido n’ido y’igikoresho cose.


Uretse ivyo bikorwa vy’ubufatanye, vyabonetse vuba ko ikigo ca Samourai kiriko kirakora ku bijanye n’uburyo bwo kwemeza ko umuntu ari umunyakuri bufitaniye isano na PayNym: Auth47. Ico gikoresho caramaze gushirwa mu ngiro kandi kiremerera, nk’akarorero, kwemeza umuntu akoresheje PayNym ku rubuga rwemera ubu buryo. Mu gihe kizoza, nibwira ko uretse ubu bushobozi bwo kwemeza ku rubuga, Auth47 izoba igice c’umugambi munini ukikuje ibidukikije vya BIP47/PayNym/Samourai. Kumbure iyo porotokole izokoreshwa mu gutuma ubumenyi bw’abakoresha bwa Samourai Wallet bugenda neza cane cane mu gukoresha ibikoresho vyo gukoresha amahera. Bisigaye ngo tubone...


## Iciyumviro canje bwite kuri BIP47.


Biragaragara ko ikibazo nyamukuru ca BIP47 ari ugutanga amakuru. Bituma uwuyikoresha ategerezwa gukoresha amahera y’iyi Mining, ivyo bikaba bishobora kubabaza bamwebamwe. Ariko rero, imvugo ya "spam" kuri Bitcoin Blockchain ntiyemewe na gato. Umuntu wese ariha amahera y’ivyo akora ategerezwa kuba ashoboye kuyandika ku rupapuro rwa Ledger, ataravye intumbero yayo. Kuvuga ukundi ni uguharanira ugucengera.


Birashoboka ko muri kazoza, hazoboneka izindi nzira zitazimvye zo kumenyesha uwuzoronka kode y’ukwishura y’uwuyirungitse, kandi uwuyironka akayibika ata nkomanzi. Ariko ubu, igikorwa co kumenyesha kiguma ari co gisubizo n’ugusenyuka gukeyi kuruta ibindi vyose.


Ico kibazo kiguma ari gito cane iyo turimbuye inyungu zose za BIP47. Mu vyiyumviro vyose biriho vyo gutorera umuti iki kibazo co gusubira gukoresha Address, mbona ko ari co gisubizo ciza kuruta ibindi vyose.


Nk’uko vyasiguwe imbere, igice kinini c’ugusubira gukoresha Address kiva ku guhinduranya. BIP47 ni umuti wonyene ubereye utorera umuti mu vy’ukuri ico kibazo aho gikomoka. Iciyumviro cose kigamije kugabanya igitigiri c’abasubira gukoresha Address gikwiye kwibanda kuri uwo muce kandi kigahuza umuti n’inkomoko nyamukuru y’ingorane.


Ku bijanye n’ugukoreshwa, naho ibikorwa vyayo vy’imbere bikomeye cane, uburyo bwo kwishura BIP47 buragororotse. Amakode yo kwishura ashobora gusubirwamwo rero arashobora kwemerwa bitagoranye, mbere n’abakoresha bashasha.


Ku bijanye n’ubuzima bwite, BIP47 iraryoshe cane. Nk’uko nabisobanuye mu gice kivuga ku bijanye n’ugutanga amakuru, kode y’ukwishura ntiyerekana amakuru yose yerekeye amaderesi y’igihe gito yava. Bica rero bica uruja n’uruza rw’amakuru hagati y’ugucuruza Bitcoin n’ikimenyetso c’uwuronka, bitandukanye n’ikoreshwa rya kera ry’uwuronka Address.


Kandi ikiruta vyose, ugushirwa mu ngiro kwa PayNym kwa BIP47 kurakora! Yabonetse ku ndege ya Samourai Wallet kuva mu 2016, no ku ndege ya Sparrow wallet kuva mu ntango z’uyu mwaka. Si umugambi wa siyansi, ahubwo ni umuti wageragejwe ejo, ukaba ukora neza uno musi.


Ni vyiza ko muri kazoza, izo kode zo kwishura zishobora gusubirwamwo zizokwemerwa n’abakozi b’ibidukikije, zishirwe mu ngiro muri porogarama ya Wallet, kandi zikoreshwe n’aba Bitcoiners.


Umuti wose mwiza vy’ukuri wo gukingira ubuzima bwite bw’abakoresha utegerezwa gushikirizwa, gusunikwa, no kurwanirwa, kugira ngo Bitcoin ntibe ikibanza co gukiniramwo c’aba CA n’igikoresho co gucungera intwaro.

Yariyumviriye ukuntu yari yahamwa, atukwa hose, none rero yumva bose bavuga ngo ni we mwiza kurusha izo nyoni nziza zose! Kandi mbere n’igiti c’umuberoshi caramupfukamira amashami yaco, izuba na ryo rikakwiragiza umuco ushushe kandi w’ubugwaneza nk’uwo! Maze amababa yiwe aravyimba, izosi ryiwe ryiza riragororoka, aca avuga n'umutima wiwe wose ati: "None nari gushobora gute kurota umunezero mwinshi gutyo kandi nari akagazi k'intare kabi gusa."


## Kugira ngo ugende kure:



- Gutahura no gukoresha CoinJoin kuri Bitcoin.



- Gutahura inzira z'ugukomoka kwa Bitcoin Wallet.



- Gushiramwo no gukoresha urudodo rwawe rwa RoninDojo Bitcoin.


### Ivyo hanze n'ivyo gushimira:


Ndashimira LaurentMT na Théo Pantamis ku vyiyumviro vyinshi bansiguriye, ivyo nakoresheje muri iyi nkuru. Nizigiye ko nabishikirije neza.


Turashimira Fanis Michalakis kubera yakosoye iki canditswe n’impanuro ziwe z’abahinga.



- https://uburongozi/uburongozi/izina ry'amahera/
- Igitabo c'amakuru gifise amakuru y'ivy'ubuhinga bwa none
- %C3%89guhindura_cl%C3%A9s_Diffie-Hellman
- %C3%89guhindura_ivyo_cl%C3%A9s_Diffie-Hellman_bas%C3%A9_sur_les_courbes_elliptiques
- https://umutekano.stack.com/ibibazo/46802/ni-itandukaniro-ri-hagati-ya-dhe-na-ecdh#:~:text=I %20itandukaniro%20hagati ya%20DHE%20na%20ECDH%20mu%20ibiharuro bibiri%20 vy'amasasu%20,ubwoko%20bw'20umurongo%20w'aligebra).
- https://umurongo w'itegeko
- 24.pdf
- 317339928_Icigwa_ku_masezerano_yo_guhana_imfunguruzo