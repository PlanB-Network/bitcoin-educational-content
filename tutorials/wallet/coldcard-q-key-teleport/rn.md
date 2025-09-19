---
name: COLDCARD Q - Key Teleport
description: Key Teleport ni iki kandi noyikoresha gute?
---

![cover](assets/cover.webp)




![video](https://www.youtube.com/watch?v=Bg0r0DQVcDg)




![video](https://www.youtube.com/watch?v=BRpBiK-F8VU)



Ni igiki **Key Teleport** gitangwa na Coinkite n’igikoresho cayo c’agaciro ColdCardQ?



**Key Teleport** ishobora kugufasha gutanga amakuru y'ibanga hagati ya ColdCardQs 2. Umurongo wo gutanga amakuru ntukeneye mbere gushirwako amakuru, kandi urashobora kuba uwa bose.



Ibi bishobora gukoreshwa mu kwimurira:





- gW-0 amajambo** (umukuru wa seed wa ColdCard Q canke amabanga abitswe mu [seed Vault] ya ColdCardQ.
- amajambo y’ibanga n’amajambo y’ibanga**: ivyo bishobora kuba ibanga iryo ari ryo ryose canke ububiko bwose [Ivyanditswe n’amajambo y’ibanga] (https://coldcard.com/docs/secure_notes/) kuri ColdCardQ yawe.
- ububiko bwa **ColdCardQ** yawe yose: ColdCardQ yakira ubu bubiko ntitegerezwa kuba ifise Umukuru wa seed kugira ngo ivyo bikore.
- gW-3 (*Ibikorwa vya Bitcoin vyasinywe igice*) nk’igice c’**umugambi w’imikono myinshi**.



Ivyo bisaba ko uba waravuguruye [porogarama y’igikoresho cawe kugira ngo ibe verisiyo v1.3.2Q] canke irengeye.



## Nokoresha gute Teleport y’urufunguzo?



### 1- Kurungika ubwoko bwose bw'amakuru



Aha, turaza kuraba ukwimurirwa kw’amajambo ya seed, amajambo, amajambo y’ibanga, canke ukwimurirwa kwose kw’ububiko bwa ColdCardQ. Ikibazo c’ugutanga amafaranga PSBT ku bikorwa vy’amasinyatire menshi kizokwihwezwa mu nyuma.



#### Tegura igikoresho co kwakira amabanga .



Mu **"Ivyiza / Ibikoresho**" kuri ColdCardQ yawe, hitamwo **"Urufunguzo Teleport (tangura) "**.


Ku mugaragaro ukurikira, ijambobanga ry'imirongo 8 rirashikirizwa, hano "20420219". Uzokenera kumenyesha uwugurungikiye iri jambobanga. Koresha sms, nk’akarorero, kugira ngo wohereze iri jambobanga, canke ubutumwa ukunda butekanye, canke mbere n’uguhamagara n’ijwi.



Hanyuma ukande kuri buto ya **"Enter**" iri kuri ColdCardQ yawe kugira ngo ugende ku ntambwe ikurikira.




![CCQ-key-teleport](assets/fr/01.webp)




Ku rubuga haca hasohoka kode ya QR. Na none, uzokenera kumenyesha iyi kode ya QR "uwurungitse" ColdCardQ. Uburyo bworoshe bwo kubigira ni uguhamagara kuri videwo.



**NTUKOREZE IYI QR CODE BICIYE KU MURONGO UMWO WO GUKORESHA GUKORESHA IJAMBO RY'IBANGA RY'IMIBARE 8 Y'IMBERE**.



![CCQ-key-teleport](assets/fr/02.webp)



*Ku bashaka, reka tugerageze gutahura uburyo bushingiyeko butuma amabanga ashobora guhererezwa ku nzira zidatekanye*



*Ico turiko turakora hano mu vy'ukuri ni ugutanguza gutanga amabanga biciye mu buryo bwa Diffie-Hellman, buvugwa mu nyigisho ya BTC204 nashize aha hepfo*



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

*Ubu dufise:*




- yashizeho urufunguzo rw'igihe gito (rwa bose/rwihariye hakurikijwe Ka na ka na Ka=G.ka, G ari yo nzira y'umuyagankuba wa ECDH), n'ijambobanga ry'imirongo 8.
- yakoresheje iri jambobanga kugira ngo apfuke urufunguzo rwa bose (Ka) biciye kuri AES-256-CTR, hanyuma arungika iryo jambobanga biciye ku muhora w'itumanaho A ku "rohereza" ColdCardQ.
- amaherezo, twarungikiye uwo yarungitse iyo paketi yashizwemwo amakuru biciye ku kode ya QR iri hejuru, dukoresheje umurongo wa kabiri wo guhanahana amakuru B utandukanye n’uwa mbere.



#### Tegura igikoresho kizorungika amabanga .



Uvuye ku gikoresho co kohereza, fyonda ku buto **"QR "** kugira ngo ubone kode ya QR yoherejwe n'ico gikoresho kiguha, hanyuma winjize ijambobanga ry'imirongo 8 ryamenyeshejwe mu ntambwe ibanza biciye ku nzira itandukanye. Ubu turiteguriye gutangura kohereza amakuru tuvuye ku gikoresho "co kohereza".



**Ntushiremwo nabi ijambobanga ry'imirongo 8, kuko nta butumwa bw'ikosa buzogaragara kandi igikorwa kizobandanya. Ariko rero, uguhererekanya amakuru kwa nyuma kuzonanirwa kandi uzobwirizwa gusubira gutangura**.



![CCQ-key-teleport](assets/fr/03.webp)



*Ku bashaka kumenya cane muri mwebwe, reka twongere turabe ivyo turiko turakora mu bijanye n'ubuhinga bwo gukora amakuru y'ibanga n'ugutanga amakuru y'ibanga:*




- twashizemwo amakuru yashizwe mu nzira mu gucapura kode ya QR iri ku gikoresho cakira.
- hanyuma tukabifungura dukoresheje ijambobanga ry’imirongo 8 twarungikiwe biciye ku nzira ya kabiri.
- rero turi mu minwe y’urufunguzo rwa bose (Ka) rwavutse n’uwakira mu ntango.
- Turaheza duca generate urufunguzo rushasha rw’igihe gito (Kb/kb, rufise Kb=G.kb) ku gikoresho co kohereza, ivyo dukoresha mu gukoresha ECDH kuri Ka. Turakora rero igikorwa kb.Ka=Ks , aho Ks yitwa **"Urufunguzo rw'Ikiganiro"**.




Ubu usabwa guhitamwo uburyo bw’amabanga azorungikwa hagati ya ColdCardQs 2 (amakete y’ibanga, ijambobanga, ububiko bwose, imbuto ziri mu nzu yawe y’ububiko, umukuru w’igikoresho ca seed).



![CCQ-key-teleport](assets/fr/04.webp)



Aha ibanga ryacu rizoba ubutumwa bugufi mu guhitamwo **"Ubutumwa bwihuta "**. Andika ubutumwa bwawe (ku bwacu "Ibitare vy'urubuga rwa PlanB") hanyuma ukande **"ENTER "**.


Ico gikoresho gica gitanga ijambobanga rishasha ryitwa **"Ijambobanga rya Teleport"** , mu karorero "NE XG BT SK".



![CCQ-key-teleport](assets/fr/05.webp)



Kanda **"ENTER "** uzobona kode nshasha ya QR. Nimugire scanner n’igikoresho kivyakira. Kandi ku nzira itandukanye yo guhanahana amakuru, urungike **"Ijambobanga rya Teleport "** ku wuyakira.



![CCQ-key-teleport](assets/fr/06.webp)



*Aha na ho, ku bashaka kumenya, muri iyi ntambwe:*




- tumaze guhitamwo amabanga azorungikwa, duca generate ijambobanga rishasha ry'imburakimazi ryitwa **"Teleport Password"**.
- turaheza tugashiramwo amabanga biciye kuri AES-256-CTR dukoresheje **"Urufunguzo rw'Ikiganiro"**, "Ks", rwavutse mu ntambwe ibanza.
- dushira imbere ipaki isanzwe yashizwemwo **"Urufunguzo rw'Ikiganiro "** n'urufunguzo rwacu rwa bose rwa Kb, hanyuma twongerako iyindi Layer y'ibanga rya AES-256-CTR n'**"Ijambobanga rya Teleport"**. Ivyo vyose bica bishirwa mu kode ya QR .




#### Gusozera gutanga amabanga ku gikoresho cakira



Kanda buto ya **"QR "** kugira ngo ubone kode ya QR yerekanwa n'igikoresho co kohereza biciye ku muhora wa visio. Uzosabwa kwinjiza **"Ijambobanga ryawe ry'Itelefone"** kuri twebwe "NE XG BT SK".



![CCQ-key-teleport](assets/fr/07.webp)





Amakuru aca afungurwa maze agaca asobanurwa n’ico gikoresho kiyakira. Ubutumwa bwakiriwe ni "Ibitare vy'urubuga rwa PlanB". Ivyo nivyo vyose.



![CCQ-key-teleport](assets/fr/08.webp)



*Ni igiki mu vy'ukuri cabaye muri iyi ntambwe ya nyuma :*?




- twakuye amakuru yarungitswe n'uwayarungitse dukoresheje **"Ijambobanga rya Teleport"**.
- rero dufise urufunguzo rwa bose Kb n'ubutumwa bwacu bw'ibanga bushizwemwo **"Urufunguzo rw'Ikiganiro "**, "Ks". Ariko ivyo twobikora gute ko nk’abakira, tutazi Ks, yaremwe n’uwarungitse?
- Turakeneye gukoresha urufunguzo rwacu rw'ibanga "ka" kuva ku ntambwe ya mbere **"Tegura igikoresho kizokwakira amakuru"** ku rufunguzo rwa bose Kb.
- Nkako, mu kubara **ka.Kb = ka.kb.G=kb.ka.G=kb.Ka=Ks**, turonka **Ks**. Ivyo amaherezo bikoreshwa mu gusobanura ubutumwa bw’ibanga.



### 2- Kwimurira PSBT muri Multisig (iteye imbere)



Ivyo bivuga ko Wallet Multisig yawe yamaze kuremwa kandi ko igikoresho cawe ca ColdCardQ camaze gutegurwa kugira ngo gishobore gukora ibikorwa vy’imikono myinshi. Niba atari uko biri, insobanuro ziraboneka [hano](https://coldcard.com/docs/Multisig/) ku rubuga rwa Coinkite.



Iciyumviro cihuta c’ico Wallet (Multisig) ifise imikono myinshi ari co.



Kenshi, kugira ngo ukoreshe amahera yawe ya Wallet, urufunguzo rumwe gusa rw’ibanga rukenewe kugira ngo ufungure UTXO zijanye n’amaderesi yawe.


Ku bijanye na Wallet Multisig, imfunguruzo z’ibanga zishika 15 rero zishobora gukenerwa imikono 15 kugira ngo ayo mahera akoreshwe. Ivyo bizwi nka "M out of N" portfolio, N iri hagati ya 1 na 15 na M umubare w'imikono isabwa kugira ngo ayo mahera ashobore gukoreshwa. Nk'akarorero, Wallet Multisig 3 kuri 5 izosaba nibura imikono 3 kuri 5 ishoboka.



Ingorane rero ni uguhuza hagati y'abasinye kugira ngo basinye "PSBT" ku "Partially Signed Bitcoin Transaction" mu gihe c'inyuma. Muri ivyo, "**Key Teleport**" ishobora gukoreshwa mu gutanga PSBT hagati y'abasinye mu buryo bworoshe kandi bw'ibanga. Uguhamagara kuri videwo kworoshe hagati y’abasinye kumwe ni kwo kuzokora.



Ehe ingene bikorwa kuri Multisig 3 kuri 4.



**Uwushizeko umukono 1:**



Uwushize umukono 1 azana umukono kuri PSBT. Ubwa nyuma, akanda kuri **"T "** kugira ngo akoreshe **"Key Teleport "** kugira ngo arungike PSBT ku muntu yasinye 2.



![CCQ-key-teleport](assets/fr/09.webp)




Amaze guhitamwo uwusinye 2 mu gufyonda kuri **"ENTER "**, haca hatangwa "IJAMBO RY'IBANGA RYA TELEPORT" (aha JJ YC AB 6A), ritegerezwa gushikirizwa uwusinye 2 biciye ku yindi nzira yo guhanahana amakuru. Nk’akarorero, SMS canke guhamagara mw’ijwi, ariko **si** guhamagara kuri videwo.



Kanda **"ENTER "** kandi haboneke kode ya QR iserukira PSBT yashizweko umukono na 1 hanyuma ikaba yashizweko "IJAMBO BANGA RYA TELEPORT".



![CCQ-key-teleport](assets/fr/10.webp)



**Uwushize umukono 2:**



Uwushizeko umukono 2 aca asuzuma kode ya QR yamushikirijwe n'uwushizeko umukono 1. Hanyuma yinjiza "TELEPORT PASSWORD" yoherezwa ku muhora w'itumanaho wa kabiri kugira ngo ashobore gukuraho amakuru yoherejwe.



Uwusinye 2 ashira umukono ku giciro hanyuma akanda kuri **"T "** kugira ngo arungike PSBT ku washize umukono 3 biciye ku "Key Teleport".


Biragaragara ko hari amasinyatire 2 amaze gushirwako. Ico kibuze ni ic’umusinya 3 kugira ngo iyo transaction ibe ibereye. Hitamwo umusinya 3 ukanda kuri **"ENTER "**.



![CCQ-key-teleport](assets/fr/11.webp)



Kandi haca hakorwa "IJAMBO BANGA RYA TELEPORT" rishasha, hanyuma hakurikirwa kandi kode ya QR ishiramwo PSBT yashizweko umukono na 1 na 2 hanyuma igashirwako n'iryo "JAMBO BANGA RYA TELEPORT" rishasha (GW YQ K3 LL).



![CCQ-key-teleport](assets/fr/12.webp)



**Uwushizeko umukono 3:**



Subiramwo iyo ntambwe nyene nk’iyo twavuze haruguru.


Uwushizeko umukono 3 aca afata kode ya QR yamushikirijwe n'uwushizeko umukono 2. Hanyuma yinjira muri "TELEPORT PASSWORD" yoherezwa n'umurongo wa kabiri w'itumanaho.



Uwushizeko umukono 3 ni we asinya iyo nzira kandi kuri iyi nshuro, kubera ko 3 kuri 4 zashizweko umukono, iyo nzira yerekanwa ko yarangije, kandi ko yiteguriye gukwiragizwa biciye ku bimenyeshamakuru bitandukanye (SD Card, NFC, QR n’ibindi).



![CCQ-key-teleport](assets/fr/13.webp)



Niba ubuhinga bwa ColdCardQ yawe bwa "Push Tx" bukora, ushobora gusa gushiramwo ColdCardQ yawe inyuma y'igikoresho cose gikoresha Internet gikoresha NFC (telefone ngendanwa/tablette) kugira ngo umenyeshe ivy'ugucuruza ku rubuga rwa Bitcoin.



![CCQ-key-teleport](assets/fr/14.webp)



*Ku bijanye n'uguhindura PSBT kuva ku muntu umwe yashize umukono ku wundi, "Key Teleport" ikoreshwa gusa biciye ku "Teleport Password" ku ntambwe yose, ikaba ipfuka PSBT uko iva ku muntu umwe yashize umukono ikaja ku wundi. Kubera ko amakuru yoherejwe adashobora gukoreshwa mu kwiba amahera, nta Diffie-Hellman akenewe nk'uko bigenda iyo wohereje amabanga y'ibanga cane (seed, ijambobanga n'ibindi...)*.



![CCQ-key-teleport](assets/fr/15.webp)



*Isoko: [Urubuga rwemewe rwa ColdCard]*