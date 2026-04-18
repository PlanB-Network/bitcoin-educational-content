---
name: Silentium
description: Urubuga rutera imbere wallet rufise ubufasha bwo kwishura mu gacerere (BIP-352)
---

![cover](assets/cover.webp)



Gusubira gukoresha amaderesi ya Bitcoin ni kimwe mu bintu bitera ubwoba cane ibanga ry’abakoresha. Iyo uwuronka asangira aderesi imwe kugira ngo aronke amahera menshi, uwubibona wese arashobora gukurikirana amafaranga yose ajanye n’ivyo maze agasubira kwubaka amateka yabo y’ivy’ubutunzi. Ico kibazo kiratera cane cane abahingura ibintu, amashirahamwe y’ubugiraneza canke abaharanira uburenganzira bw’abantu bipfuza kwerekana ku mugaragaro aderesi y’intererano ataco bahinduye ku buzima bwite bwabo.



Silentium yishura kuri iki kibazo n’umuti mwiza ushobora gushikira uhereye ku mucukumbuzi wawe. Iyi porogaramu y’urubuga rwuguruye (PWA), yatangujwe muri Rusama 2024 na Louis Singer, ishira mu ngiro Silent Payments (BIP-352): aderesi idahinduka ishobora gusubirwamwo aho ukwishyura kwose guhera kuri aderesi itandukanye ya blockchain, ata n’umwe abanza gukorana canke ngo aboneke hagati y’ibikorwa.



**Imbuzi ihambaye**: Silentium ni umugambi w'igerageza ukora nk' *ikimenyamenya c'iciyumviro* ku ndege za Silent Payments zidakomeye cane zitwa wallets. Ntibikwiye gukoreshwa nk’igitabu ca wallet co ku musi canke co kubika amahera menshi. Ababiteguye bavuga neza:



> Koresha ku rwego rwawe bwite.

Zirikana ko iyi wallet ishobora gukoreshwa nk’uruzitiro canke regtest.



## Silentium ni iki?



### Filozofiya n'intumbero



Silentium ikora nk’iyerekanwa ry’ubuhinga ryo gushitsa Silent Payments mu mucukumbuzi wallet yoroshe. Naho kandi ishigikira amaderesi asanzwe ya Bitcoin, ikintu gishimikiyeko ni Silent Payments kugira ngo abakoresha bashobore kugerageza ubu buhinga bwo gucungera ubuzima bwite mu buryo bugororotse.



### None Ivyishyurwa vy’Icereje bikora gute?



Ivyishyurwa bicereje (BIP-352) bikoresha urufunguzo rwa Diffie-Hellman Exchange (ECDH). Uwuronka atanga aderesi idahinduka (`sp1...` kuri mainnet, `tsp1...` kuri testnet) igizwe n'imfunguruzo zibiri za bose: urufunguzo rwo gupima kugira ngo umenye amahera yishuwe, n'urufunguzo rwo gukoresha kugira ngo uzikoreshe.



Uwurungitse afatanya urufunguzo rwiwe rw'ibanga n'urufunguzo rw'uwuronka kugira ngo abare ibanga ry'abantu bose rituma habaho "uguhindura" kw'ibanga. Ivyo bihinduka, vyongewe ku rufunguzo rwo gukoresha, bituma habaho aderesi yihariye ya Taproot ku bijanye n’ugucuruza kwose. Uwuronka ayo mahera asubiramwo iyo mibare akoresheje urufunguruzo rwiwe rw’ibanga kugira ngo amenye kandi akoreshe ayo mahera ata n’umwe abanje gukorana na yo.



Ivyiza: ibanga ryongerekanye ku wurungika n’uwuronka, nta serveri y’uwundi muntu isabwa, amafaranga adatandukanywa n’amahera asanzwe yishurwa kuri Taproot. Intambamyi nyamukuru: gupima cane blockchain kugira ngo umenye amahera yishuwe.



Kugira ngo umenye vyinshi ku bijanye n’ingene Silent Payments ikora, raba igice ca nyuma c’inyigisho ya BTC,204 ku Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Imbuga zishigikiwe



Silentium ni Porogarama y’urubuga itera imbere (PWA) ishobora gukoreshwa n’umucukumbuzi uwo ari wo wose wo muri iki gihe (uwukoresha telefone canke kuri mudasobwa). Uyikoreshe kuri `app.silentium.dev`, uyishiremwo nk'iporogarama y'akavukire biciye ku mucukumbuzi wawe, canke uyishire ahantu. Gushiramwo bikorwa biciye ku mucukumbuzi, ataco uciye mu maduka yemewe.



## Gukoresha porogaramu y'urubuga



### Ukwinjira no gushiramwo



[Genda kuri `https://app.silentium.dev/` uvuye mu mucukumbuzi wawe](https://app.silentium.dev/). Porogarama ica ifunguka ubwo nyene maze igaragaza igicapo c’inzu.



Kugira ngo uyishiremwo nk'iporogarama y'akavukire kuri iOS, kanda buto yo gusangira (akarongo n'umwampi uja hejuru) hanyuma uhitemwo "Ku mugaragaro w'intango". Kuri Android, umucukumbuzi akenshi atanga itangazo ry'"Ongera ku rubuga rw'intango" ataco rihinduye. Iyo imaze gushirwako, Silentium iraboneka n’ikimenyetso cayo cihariye kandi ikora nk’iporogarama y’akavukire, ariko isaba ko umuntu akoresha interineti kugira ngo akoreshe amafaranga.



![Installation de Silentium comme PWA sur iOS](assets/fr/01.webp)



### Guhingura ububiko



Ku gutangura kwa mbere, hitamwo "Rema Wallet" kugira ngo ushireho wallet nshasha, canke "Subizaho Wallet" kugira ngo usubizeho kuva ku majambo yo gusubizaho ariho.



Hitamwo "Rema Wallet". Ico gikoresho kiratanga amajambo y’amajambo 12 utegerezwa kwandika neza. Iri jambo ni ryo ryonyene ryo gusubiza amahera yawe. Mbere no kuri testnet, ushiremwo ingendo nziza zo gusubiza inyuma. Kanda "Bandanya" umaze kubika ijambo ryawe.



Iyo porogarama ica igusaba gushinga ijambobanga kugira ngo ushobore gukoresha wallet. Hitamwo ijambobanga rikomeye maze uryemeze.



![Création d'un nouveau wallet avec phrase de récupération](assets/fr/02.webp)



Iyo iryo jambo rimaze kwemezwa kandi ijambobanga rikaba ryashizweho, uzojanwa ku rubuga nyamukuru.



### Interface nyamukuru n'imirongo ngenderwako



Igikoresho nyamukuru kigaragaza uburinganire bwawe mu satoshis (mu ntango 0 sats), harimwo amabuto atatu hasi:




- Guhuza**: guhuza wallet na blockchain
- Kwakira**: kwakira amahera
- Wohereze**: kugira ngo wohereze ama bitcoins



Ushobora gushika ku mirongo ngenderwako biciye ku kimenyetso kiri hejuru iburyo (imirongo itatu iringaniye). Ububiko bw'imiterere buratanga amahitamwo menshi:





- Ivyerekeye**: amakuru y'ugusaba
- Gusubiza inyuma**: gusubiza inyuma amajambo yo gusubizaho
- Umugenzuzi**: hitamwo blockchain umugenzuzi (Mempool ku mburabuzi) na Silentiumd server
- Urubuga**: uguhitamwo urusobe (mainnet/urusobe rw'ikigeragezo)
- Ijambobanga**: guhindura ijambobanga
- Gusubiramwo**: gusubiramwo wallet
- Gusubiramwo**: gusubiramwo vyose
- Insiguro**: guhindura insiguro



![Interface principale et paramètres avec Explorer](assets/fr/03.webp)



Igice ca **Umugenzuzi** kirahambaye cane: kigufasha guhitamwo umugenzuzi wa blockchain ukoresha (Mempool ku buryo busanzwe) kandi kigaragaza kandi URL ya server ya Silentiumd (`https://bitcoin.silentium.dev/v1` kuri mainnet). Niba wakira server yawe bwite ya Silentiumd canke wipfuza gukoresha testnet, aha niho utunganya ivyo bipimo.



### Kwakira amafranga



Kuva ku rubuga nyamukuru, kanda kuri buto ya "Kwakira". Kubera ko ari vyo, Silentium yerekana aderesi y’Ukwishura mu gacerere iri kumwe na kode yayo ya QR. Aderesi itangura na `sp1...` kuri mainnet canke `tsp1...` kuri testnet.



Ushobora guhindura hagati y'Ukwishura mu gacerere n'amaderesi ya kera ya Bitcoin ukoresheje buto ya "Gihindurira kuri aderesi ya kera" / "Gihindurira kuri aderesi y'agacerere" iri musi y'ibarabara.



![Réception de fonds avec Silent Payment et adresse classique](assets/fr/04.webp)




Igihe amafaranga amaze gutangazwa, ndagusavye urindire iminota mikeyi. Ku bijanye n’Ivyishyurwa Bicereje, Silentium ica ihita isuzuma blockchain kugira ngo ibone amafaranga yawe. Ibikorwa vy'ubudandaji bigaragara bifise ikibanza "Ntivyemejwe" imbere y'uko vyemezwa buhoro buhoro.



### Wohereze amahera



Kuva ku rubuga nyamukuru, kanda kuri buto ya "Ohereza". Igikoresho co kohereza kizokubaza :



1. **Address**: ushireko aderesi y’Ukwishura mu gacerere (`sp1...` canke `tsp1...`) canke aderesi ya kera ya Bitcoin. Ushobora gukoresha ikimenyetso ca QR kugira ngo uscane aderesi.


2. **Igiciro**: shiramwo igiciro mu satoshis uzorungikwa. Igipande c’imibare kiragaragazwa kugira ngo umuntu yinjire bitagoranye. Igitigiri cawe kiboneka kigaragara hejuru kugira ngo ushobore kugikoresha.



![Envoi de fonds depuis Silentium](assets/fr/05.webp)



Umaze kwandika aderesi n'amahera, ukande "Bandanya" kugira ngo ukomeze. Iryo koraniro rizogusaba guhitamwo urugero rw’amahera wipfuza imbere y’uko wemeza ko ugurisha.



## wallet kwiyakira



### Kubera iki kwikira?



Silentium's local hosting itanga ubusegaba bwose, kugenzura kode, ibidukikije vy'iterambere n'ukwihangana mu gihe urubuga rwemewe rudakora neza.



### Ibisabwa



Node.js (uburyo 14+), npm canke urudodo, Git, n'ahantu hafi 500 MB kuri disiki.



### Gushiraho aho hantu



Kora ububiko maze ushiremwo :



```bash
git clone https://github.com/louisinger/silentium.git
cd silentium
yarn install
```



### Gutanguza no gukoresha



Tangira porogaramu mu buryo bwo gutegura:



```bash
yarn start
```



Genda kuri `http://umushitsi wo mu karere:3000` mu mucukumbuzi wawe. Kugira ngo ubone verisiyo nziza cane :



```bash
yarn build
```



Dosiye zakozwe muri `build/` zishobora gukoreshwa na nginx, Apache canke umukozi w'urubuga uwo ari wo wose. Ku mburabuzi, Silentium ihuza n'umukozi wa bose. Guhindura iyi nzira mu mirongo ngenderwako kugira ngo ukoreshe testnet canke server yawe bwite.



## Serveri ya Silentiumd



### Uruhara n'imikorere



Silentium ikoresha **Silentiumd** server y'urutonde kugira ngo ishobore kumenya neza amahera. Gucapura amafaranga yose ya Taproot vyoba ari ikintu kigoye cane ku mucukumbuzi canke kuri telefone ngendanwa.



Silentiumd ibanza kubara amakuru yo hagati (tweaks) ku bijanye n’ugucuruza kwose kwa Taproot. wallet yawe irakuraho izo tweaks (bytes nkeyi ku giciro) maze igakora ibara rya nyuma mu karere, igenzura uwufise iyo nyishu. Server ntiyigera amenya imfunguruzo zawe canke ngo ishobore kumenya amafaranga yawe, bitandukanye n’ama server asanzwe ya Electrum.



Ivyuma biyungurura bikomeye vyitwa BIP158 biratuma wallet yawe imenya amabarabara yo gucapura ataco itangaza ku maderesi yawe, gutyo bikaguma bizigama ibanga ryawe.



### Server ya bose



Igikoresho ca bose `bitcoin.silentium.dev` (mainnet), giterwa inkunga na Vulpem Ventures, gitanga ubumenyi bworoshe kandi buca bushika. Naho ibanga rizigama, iyo nzira ivuga ko umuntu yizigira ibikorwa remezo vy’uwundi muntu.



### Ukwakira umukozi wawe bwite wa Silentiumd



Kugira ngo ubone ubusegaba bwose, n’ushire umukozi wawe bwite wa Silentiumd. Ibisabwa: Bitcoin Igikoresho nyamukuru kitagira amabara gifise `txindex=1` na `blockfilterindex=1`, Go 1.21+, umwanya wa 10-20 GB kuri disiki, ubuhinga bwo gutwara sisitemu.



**Gushiramwo:**



```bash
git clone https://github.com/louisinger/silentiumd.git
cd silentiumd
make build
./build/silentium-[OS]-[ARCH]
```



Gutunganya biciye ku bihinduka vy'ibidukikije (raba `config.md` y'ububiko ku bisobanuro). Serveri itanga urutonde rwa blockchain maze igaragaza API ishobora kubazwa na wallet yawe.



Nta mirongo y’ibisubizo vy’amapaki ya Umbrel canke Start9 iriho ubu, igabanura ukuronka ku bakoresha batari abahinga.



## Inyungu n'aho bigarukira



### Ibintu bihambaye





- Ugushikira cane**: ukoreshe mu mucukumbuzi uwo ariwo wose, nta gushiramwo vyinshi bisabwa
- Ivyuma vyinshi**: bikora kuri telefone ngendanwa (Android/iOS) no kuri mudasobwa kubera ubuhinga bwa PWA
- Kwiyakira vyoroshe**: gushiramwo mu karere birashoboka hakoreshejwe amabwirizwa make
- Inkomoko yuguruye**: kode ishobora gusuzumwa kuri GitHub
- Ivyerekeye ubuzima bwite**: nta gukurikirana, nta gusesangura, imibare y'ubuhinga bwo mu karere
- Ubwubatsi butandukanye**: gutandukanya neza hagati ya wallet (umukiriya) na server y'urutonde
- Ata konti**: nta kwiyandikisha canke amakuru y'ibanga bisabwa



### Intambamyi zo kwiyumvira





- Umugambi w'igerageza**: ikimenyamenya c'iciyumviro gusa, ntikigenewe gukoreshwa canke gukorwa buri musi
- Nta n'ivyemezo**: ingorane z'ibikoko, ubugoyagoye, gutakaza amahera bishoboka
- Infashanyo igabanutse**: inyandiko nke z'abakoresha, umuryango muto, nta nfashanyo yemewe
- Ugushingira kuri server**: bisaba server ya Silentiumd ikora (ya bose canke yiyakira)
- Gupima cane**: Gutahura kwishura mu gacerere bifata ubwaguke bw'umurongo
- Ibikorwa bigabanutse**: nta kugenzura igiceri, nta Muravyo, nta multi-signatures



## Ibikorwa vyiza



### seed umutekano



No kuri testnet, fata neza ijambo ryawe ryo gukira. Uvyandike kandi ubishire ahantu heza. Gumana wallets zitandukanye za testnet na mainnet: ntukigere ukoresha seed y’igerageza kuri wallet igenewe amahera nyayo.



### Kugenzura kode y'inkomoko



Kimwe mu vyiza vyo kwiyakira ni ubushobozi bwo kugenzura source code imbere yo kuyikoresha. Niba uriko urategura gukoresha Silentium n’amahera nyayo, fata umwanya wo kugenzura kode canke uronke umuhinga mu bijanye n’ubuhinga wizigirwa ngo abikore. Gereranya kandi hash ya kode yashizwe kuri `app.silentium.dev` n'iyo mu bubiko bwa GitHub kugira ngo umenye neza ko ari iy'ukuri.



### Gusubiza inyuma no gusubizaho



Gusubiza amafaranga y’Ivyishyurwa vy’Icereje bisaba wallet ihuye n’umurongo wa BIP-352. wallet isanzwe ntishobora gucapura blockchain kugira ngo ibone UTXO yawe y’Ivyishurwa vy’Iceceka. Gumana Silentium canke urabe ko ufise uburenganzira bwo gukoresha iyindi wallet ihuye (nka Cake Wallet canke ibindi bizoshirwa mu ngiro muri kazoza) kugira ngo usubize amahera yawe nimba bikenewe.



## Iciyumviro



Silentium itanga ikibanza co kugerageza gishoboka co gutahura Silent Payments ata n’umwe afise uguhuzagurika mu vy’ubuhinga. Nk’ikimenyamenya c’iciyumviro, yerekana ingene ubu buhinga bwo gucungera ubuzima bwite bushobora kwinjizwa mu mucukumbuzi wallet mu gihe buzigama uburenganzira bwo kwizigama. Igerageza kuri testnet kugira ngo ubone iyo nzira nziza cane ku bijanye n’ubuzima bwite bwa on-chain.



## Ubutunzi



### Inyandiko zemewe




- Silentium Ububiko bwa GitHub (wallet):
- Silentiumd ububiko bwa GitHub (umukozi):
- Urubuga rwo gukoresha: https://porogaramu.guceceka.dev/
- Urubuga rw'abanyamuryango b'Ivyishyurwa vy'Iceceka: https://ivyishyurwa vy'Iceceka.xyz
- Ibisobanuro BIP-352:



### Ingingo n'ibikoresho




- Itangazo ry’ubutegetsi (Twitter): 1790824126472667227
- NoBS Bitcoin: https://www
- Bitcoin Optech - Ukwishura mu gacerere:



### Ibikoresho vya Testnet




- Testnet: https://igerageza-uruzitiro.com/
- Mempool umugenzuzi w'urubuga rwo kugerageza: https://mempool.ikibanza/urubuga rwo kugerageza