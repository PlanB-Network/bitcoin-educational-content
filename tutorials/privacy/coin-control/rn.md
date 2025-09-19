---
name: Coin Control
description: Tangira na Coin Control, igikoresho nyamukuru co kurinda ubuzima bwite bwawe kuri Bitcoin.
---
![cover](assets/cover.webp)


*Iyi nyigisho yavanwe muri [icigwa cakozwe na Officine Bitcoin](https.



## Imenyekanisha



Ubukomezi bw’amasezerano ya Bitcoin burashimangirwa n’ivyiyumviro nyamukuru vyoroshe. Muri ivyo, uguseruka ni kwo guhambaye: amafaranga yose akoreshwa na Bitcoin ni aya bose kandi ashobora kugenzurwa n’umuntu wese bitagoranye. Naho ico kintu ari ibuye ry’imfuruka ry’iyo porotokole, kuko kizibira ubuhendanyi kandi kigatuma amahera ari ay’ukuri, kirashobora kandi gutera ingorane ku bijanye n’ibanga. **Woba warigeze wibaza nimba mwene ukwo guserukira abantu mu mucyo bishobora gutuma ubuzima bwite bwawe buhungabana?**



Ukwiye. Naho kwirundanira Satoshi non-kyc vyoroshe, ubuzima bwite bwawe burari mu kaga cane ku rwego rwo gukoresha.



### Ivyo bishika iyo ukoresheje UTXO.



Gukoresha Bitcoin si uguha agaciro uwundi muntu gusa.



Mu gufungura imwe mu ma UTXO yawe, mu vy’ukuri utegerezwa gushitsa ibisabwa kugira ngo amasezerano akore mu mucyo, kuko ufise inshingano yo kwemeza ko ari wewe ufise ayo mahera. Uca rero wigira uwujejwe :




- gushikiriza urufunguzo rwawe rwa bose;
- gutanga umukono w’ibarabara.



Igihe co gukoresha rero ni co gihambaye cane: **gukoresha Bitcoin ni igikorwa co gukora umuntu abizi kandi afise ububasha bwo kubigenzura uko bishoboka kwose**.



## Coin Gucungera



Mu masezerano ya Bitcoin, ibintu nka _konti_ canke _ibice vy'amahera_ ntibiriho. Iciyumviro ca UTXO kirasigurwa neza cane mu nyigisho ikurikira, iyo ndabashimira cane:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Na Bitcoin ivyo urundanya hanyuma ukabikoresha ni ibice bito canke binini vy'ikonti bipimwa muri Satoshi, bigereranywa n'`ibiva mu bikorwa bitakoreshejwe`, **UTXO**, navyo vyitwa `ibiceri`. Iyo ukoresheje UTXOs kugira ngo ureme transaction, zirasenyuka burundu maze izindi UTXO zikaremwa mu kibanza cazo.



Software Wallets zitegurwa kugira ngo zihitemwo ubwazo, zikoresheje ibiceri vyatoranijwe "mu buryo butari bwo", zikoresheje ubuhinga bumwe bumwe butangwa n'itegeko. Ico nyene izo algorithmes zishitsako, ni ugupfuka amahera akenewe kugira ngo umuntu akoreshe.



Bashobora kuvanga hamwe UTXOs z'imyaka itandukanye, canke bagakunda gukoresha ivyuma bishasha canke "vya kera," bivanye n'ubuhinga bwatowe n'ababiteguye. Ivyiza kuruta ibindi vyose vya Software Wallets, navyo bitegura gusiga uwubikoresha afise amahitamwo ahambaye.



Igitabo ca `Coin Control`, ico ushobora no gusanga citwa `Coin Selection`, ni ikintu kiri muri Software Wallets zimwe zimwe zigufasha **guhitamwo n'amaboko UTXOs zo gukoresha igihe wubaka ibikorwa vyawe**.



Twibaze ko dufise Wallet ifise UTXO 3 zifise 21.000, 42.000 na 63.000 Satoshi, uko zikurikirana.



![img](assets/en/01.webp)



Niba ubwirizwa gukoresha 24.000 Sats maze ukareka algorithm igahitamwo, Software Wallet nziza yoshobora guhitamwo gufatanya UTXO 1 + UTXO 2 kugira ngo wishyure amafaranga 24k Sats na Miner, ugatuma habaho igisigaye gisubira mu ntango y’imbere ya GW-1.



![img](assets/en/02.webp)



Inyuma y’ugucuruza, ivyabaye bishasha muri Wallet, biharura UTXO gusa, birashobora gusobanurwamwo mu ncamake gutya.



![img](assets/en/03.webp)



Ariko rero, iyo ufise porogarama ibereye be n’ukumenya kwawe, wari gushobora guhitamwo uburyo butandukanye, mu buryo bumwebumwe bubereye kuruta. Nk’akarorero, mu guhitamwo UTXO2 gusa (kuva ku 42.000 Sats).



![img](assets/en/04.webp)



N’iherezo ry’ibintu muri Wallet yawe, ku rugero rwa UTXO, ivyo bisa n’ibitandukanye n’imbere.



![img](assets/en/05.webp)



## Ni kuki Coin igenzura n’amaboko?



![img](assets/en/06.webp)



Mu ngero zibiri ziri hejuru, umubare ni umwe `108.280 Sats`. Tumaze gukoresha 24.000 Sats, ata guhitamwo n’amaboko twoba dufise 2 UTXO muri Wallet; na Coin ubugenzuzi bw’amaboko dufise 3 yose hamwe.



Ikibazo twokwibaza ni iki: **kubera iki ivyo vyose bikora?** Hari, canke bishobora kuba, imvo nyinshi zatumye tutakoresha `UTXO1` **kandi zose ziri mu mutima w’igituma—igihe dukoresha—gukoresha ubuhinga bwo kugenzura Coin n’amaboko ari kimwe mu bintu vyiza vyo gukurikiza**.



Guhitamwo UTXOs bituma ukunda imice imwimwe kuruta iyindi. Ihitamwo rivana vy’ukuri n’imigambi ushaka gushikako.



### Ubuzima bwite



Kimwe mu vyiza nyamukuru, iyo bije ku bijanye no kugenzura Coin n’amaboko, ni **ubuzima bwite bwinshi ku muntu akoresha**. Reka twame dufata akarorero kacu: amafaranga 24.000 Satoshi _ata guhitamwo Coin n’amaboko_. Kubera ko Blockchain ya Bitcoin ari inyandiko ya bose, uwuyibona wo hanze arashobora kumenyesha, ata gitutu c’amakenga, ko ivyinjijwe `UTXO1 ya 21.000 Sats` na `UTXO2 ya 42.000 Sats`, hamwe n’ibindi, bivuye kuri `3UT,802. **vyose bitatu ni ivy'ukoresha umwe**.



Mu guhitamwo n’amaboko `UTXO2`, ku rundi ruhande, `UTXO1` iguma yibikiwe rwose, yicaye mu gice ca UTXO irindiriye gukoreshwa ku gihe kibereye.



`UTXO1` yoshobora kuva ku nzira ya KYC, nk’amahera yaronswe muri Exchange ku bicuruzwa n’ibikorwa, mu gihe izindi UTXO zitabigira. Kuvanga UTXO-kyc n’izindi zifise ibanga cane bitera ingorane umugwi w’amahera atari aya kyc.



**Amahera ya KYC yosubira ku bijanye n’akaranga k’uwuyitanga. Iyo iba Wallet yawe, woba woshima ko umuntu wo hanze ashobora gukurikirana akaranga kawe ata gukeka gutyo?**



Gerageza rero kwiyumvira ko ama Wallets ashira mu ngiro uguhitamwo n’amaboko kw’ama UTXO, nk’akarorero, yemera **ugutandukanya UTXO imwe canke nyinshi**, igikorwa co gukoreshwa iyo ibintu nk’ivyo bishitse.



Naho nemera neza ko amahera ya KYC akwiye kubikwa muri Wallet itandukanye n’iya Bitcoin yaguzwe ata kyc, nimba ari ukwo biri kuri wewe ugutandukanya amaderesi yawe amwe amwe ni imfashanyo nyamukuru, iyo woshobora kuvyungukirako mu kwiga guhitamwo n’amaboko ivyo ukoresha.



### Kuzigama ku mahera



Guhitamwo UTXO ibereye kugira ngo ukoreshe amafaranga, **bituma amafaranga akoreshwa neza**. Na none duhereye ku karorero kacu ka mbere, Software Wallet yatoye ama UTXO abiri kugira ngo yishure amahera azokoreshwa. UTXO zibiri zisobanura imikono ibiri izokwerekanwa ku rubuga. Bica bikurikira ko igikorwa gifise "uburemere" buhambaye mu bijanye n'ama vBytes.



Ukoresheje ubugenzuzi bw'amaboko bwa Coin, ku rundi ruhande, urashobora guhitamwo kimwe gusa gihagije kugira ngo ushobore gupfuka amahera, ukazigama amahera mu kugabanya "uburemere" bw'ugucuruza.



Mu bihe amafaranga ari menshi, ariko ukaba ugoberwa no gukoresha Bitcoin On-Chain (nk’akarorero, gufungura umurongo wa Lightning Network), niho ubugenzuzi bwa Coin buhinduka ikintu ciza co gutera intege mu vy’ubutunzi wohindukirako.



### Gukoranya ibisigarira



Iyo utanga amahera kandi ugakoresha Bitcoin On-Chain, ubushobozi bwo kwakira ihinduka hafi y’igihe cose burahinduka ikintu kidakeka. Igisigaye cose ubwaco ni ugutakaza ubuzima bwite buke, kuko gihishurira urubuga (na cane cane uwuronka amahera) Address yawe ishobora gufatanywa n’inyungu yawe y’inkomoko.



Uravye uko ama aderesi meza cane Wallet HDs generate yihariye y'amasigarira, urashobora kuyamenya bitagoranye maze "ukatandukanya" amasigarira yose y'ibikorwa bitandukanye vyakozwe; iyo zishitse ku rugero runaka ushobora kuzitoranya n’amaboko ukazifatanya, canke ukazihindura ukazikoresha Lightning Network (uburyo nkunda) ukazikora kugira ngo usubire kuronka ubuzima bwite bwatakaye mu gukoresha amahera.



### Amafaranga avuye mu ndege ya Cold Wallet



Cold Wallet ni igikoresho umuntu ashobora gukoresha mu kuronka umutekano mwiza, kugira ngo abike amahera yose yoba afise kugira ngo ayagumye ku ruhande igihe kirekire. Ariko rero, ibintu bitari bitezwe birashobora gushika, ni co gituma bikenewe ko umuntu aronka ukuboko ku vyo azigamye no gutanga amahera amwamwe atari yiteze.



Sinzi bangahe bashobora gusangira uburyo bwanje, ariko impanuro yanje ni **kutigera ukora amafaranga ataco ukoresheje Cold Wallet, kugira ngo wirinde kwakira ihinduka hagati y’amaderesi y’ivyo nyene**. Iga guhitamwo n’amaboko ama UTXO akenewe kugira ngo ushobore kwishura amahera, uyashire mu Wallet Hot maze utegure ibikorwa vyawe uhereye kuri iyo ya nyuma. Ihinduka ryose rero, urashobora kurirungika kuri Cold Wallet Address (niba amahera ahagije), ukarikoresha mu bindi bikoresho, canke ukaritandukanya nk’uko twamaze kubibona.



## Inyishu ngirakamaro


Inyuma y`intango y`ubuhinga bw`impamvu`, reka turabe ingene twoshira mu ngiro uburyo bwo kugenzura Coin n`amaboko hakoreshejwe porogarama zitandukanye, kuri mudasobwa no kuri telefone ngendanwa. Tuzokwama dukoresha iyo Wallet BIP39 nyene, yinjijwe muri buri gikoresho catowe, kugira ngo tubereke ututandukaniro dutoduto turi hagati yavyo.



## Wallet Ibiro



### Sparrow



Niba ukoresha Sparrow, fungura Wallet yawe uhitemwo _UTXOs_ mu bimenyetso biri ibubamfu. Uzobona urutonde rw'ama UTXO yose ajanye na Wallet yawe.



Fyonda gusa n'imbeba kuri imwe muri zo hanyuma uhitemwo _Ohereza Ivyatoranijwe_. Sparrow kandi ikwereka umubare wose ushobora gukoresha inyuma y’uguhitamwo, iruhande nyene y’itegeko. Mu buryo bw’ikigereranyo Sparrow ikwereka UTXO yatowe mu kuyigaragaza mu bururu.



![img](assets/en/07.webp)



Ushobora kandi guhitamwo ibirenze kimwe. Ifashe n'urufunguzo _CTRL_ guhitamwo UTXO zitari hafi muri list.



![img](assets/en/08.webp)



Uhejeje guhitamwo UTXO n’amaboko, urashobora gutangura kwubaka igikorwa, Sparrow izokwereka neza, mu buryo bw’ibishushanyo, ingene igizwe.



![img](assets/en/09.webp)



#### Gutandukanya UTXO



Gutandukanya amafaranga bisigura "kuyafunga" muri Wallet kugira ngo ntakoreshwe nk'inyungu mu gucuruza. Sparrow iremera iyo mikorere, ihora iboneka mu _UTXOs_ menu: ushira imbeba hejuru ya UTXO kugira ngo "ifungwe" hanyuma ukande kuri buto y'imbeba y'iburyo. Mu bimenyetso vy'iyi nzira hazoboneka _Freeze UTXO_. Uko niko uzoshobora gutandukanya Ibiceri n’ibipapuro vya Sparrow.



![img](assets/en/29.webp)



### Umuyagankuba



Niba biro vyawe vya Wallet ari Electrum, ukwiye kumenya ko ushobora guhitamwo UTXOs n'amaboko haba mu _Addresses_ canke mu _Coins_. Muri izo menus zompi, uguhitamwo bikorwa mu kwerekeza imbeba kuri UTXO wipfuza hanyuma ugahitamwo _Add to Coin control_ umaze gukanda iburyo.



![img](assets/en/10.webp)



Mbere n'iyi porogaramu urashobora guhitamwo UTXO zirenga imwe, ufasha n'urufunguzo _CTRL_ kuri klavye yawe nimba zitari hafi y'izindi.



![img](assets/en/11.webp)



Mu buryo bw’igishushanyo Electrum izokwereka uguhitamwo mu kugaragaza UTXOs zatowe muri Green, mu gihe umurongo uboneka hasi, ugaragazwa mw’ibara rimwe, ugaragaza uburinganire buriho inyuma y’ugucungera Coin.



![img](assets/en/12.webp)



Umaze guhitamwo igisohoka, canke ibisohoka, ushobora kwubaka igikorwa cawe nk'uko usanzwe ubikora ukoresheje _Send_ menu.



#### Gutandukanya UTXO



Electrum itanga iyo nzira mu kuja muri _Coins_ menu, aho uzoja guhitamwo UTXO imwe imwe hanyuma uhitemwo _Freeze_ ukoresheje gukanda iburyo. Ushobora "gufunga" Address n'aho ata mahera ari muri _Addresses_ menu, canke "Coin" kugira ngo ntuyikoreshe.



![img](assets/en/28.webp)



### Nunchuki



Nunchuk iraguha uburenganzira bwo guhitamwo n’amaboko UTXOs mu rutonde nyamukuru iyo imaze gufungurwa. Tangaza Nunchuk hanyuma ukande _Reba ibiceri_.



![img](assets/en/13.webp)



Ivyo bica bifungura idirisha ririmwo ama UTXO yose ari muri Wallet yawe, aho ushobora guhitamwo imwe canke nyinshi mu gukoresha ikimenyetso co gusuzuma kiri iruhande y’amahera yose. Uhejeje guhitamwo, komeza _Rema igikorwa_.



![img](assets/en/14.webp)



Inyuma y’ivyo ushobora kwinjira aho uja Address ugashinga amahera n’amahera.



![img](assets/en/15.webp)



#### Gutandukanya UTXO



Kugira ngo bibe vyuzuye, Nunchuk na yo iremera mu biranga, gutandukanya UTXO imwe (canke nyinshi) kandi ibigira mu buryo bubiri butandukanye. Hika ku _Reba ibiceri_ maze uhitemwo n'amaboko mu rutonde rw'ibiceri. Hanyuma ukande kuri _More_ menu iri musi iburyo: urutonde rw'amahitamwo ruzoboneka, aho ushobora guhitamwo _Lock coins_.



![img](assets/en/39.webp)



![img](assets/en/40.webp)



Ushobora kandi gukanda mu kibanza cabikiwe UTXO, kugira ngo ushikire idirisha rya _Coin details_. Aha itegeko ryo gufunga/gufungura UTXO iriko iravugwa riboneka mu mfuruka yo hejuru iburyo.



![img](assets/en/41.webp)



### Porogaramu yo guhagarika uruja n'uruza



Blockstream App desktop, mbere yitwa Green, iragufasha guhitamwo Coin iyo umaze gutangura kwubaka igikorwa. Rero, fungura Wallet yawe ukande kuri _Send_.



![img](assets/en/16.webp)



Nimushire aho uja Address mu kibanza kibereye hanyuma uhitemwo _Guhitamwo Coin n'amaboko_.



![img](assets/en/17.webp)



Ivyo bigufungura idirisha aho ushobora guhitamwo igiceri kimwe canke vyinshi vya UTXO. Mu karorero kari aha hepfo, twahisemwo ibiceri bibiri. Inyuma y'ivyo, wemeze ihitamwo ryawe ukanda kuri _Wemeze Ihitamwo rya Coin_.



![img](assets/en/18.webp)



Tegura umubare n’amahera hanyuma ugende nk’uko bisanzwe n’ugucuruza kwawe.



![img](assets/en/19.webp)



⚠️ N.B. Mu _Ibiceri_ vya Green hariho _Lock_/_Unlock_ ibintu vyerekana ubushobozi bwo gutandukanya UTXO. Ico kintu gikoreshwa gusa mu vyo bita Multisig; kandi ikora gusa mu guhitamwo UTXO y'umubare muto cane, hafi y'urugero rwa `Dust`.



## Wallet igendagenda



Ivyuma bishobora kandi gutorwa bivuye kuri telefone ngendanwa, ivyo bikaba bituma UTXOs zitorwa n’amaboko. Reka turabe Blue Wallet nk’akarorero ka mbere.



### Ubururu Wallet



Nimba uri umukoresha w’iyi Wallet, uyifungure maze ukande kugira ngo winjire mu bipimo vy’ubugenzuzi bijanye na imwe mu ma Wallet yawe. Kugira ngo ushikire igitabu c'ubugenzuzi ca Coin utegerezwa kwinjira mu gice co gukoresha, hanyuma ukande _Send_.



![img](assets/en/21.webp)



Ku gicapo gikurikira, nuhitemwo amamenyu yerekanwa n’utudodo dutatu turi hejuru iburyo. Idirisha rimanuka rifunguka rifise urutonde rw’amabwirizwa. Hitamwo ica nyuma: _Igenzura ry'Ibiceri_.



![img](assets/en/22.webp)



Muri iki gihe Blue Wallet yerekana UTXO zawe zose. Uretse amahera, aratandukanywa mu buryo bw’ibishushanyo n’amabara atandukanye.



![img](assets/en/27.webp)



Hitamwo UTXO kugira uhitemwo hanyuma uhitemwo _Koresha Igiceri_.



![img](assets/en/23.webp)



Ubururu Wallet bugusubiza mw'idirisha rya _Send_ kugira ngo ukomeze kwubaka igikorwa. Tunganya umubare n'amahera, hanyuma uhitemwo _Ibikurikira_.



![img](assets/en/24.webp)



Muri iki gihe urashobora guheza igikorwa co gucuruza, nk’uko usanzwe ubigira.



#### Gutandukanya igitabu ca UTXO



Blue Wallet nayo iragufasha gutandukanya UTXOs, bikaba bituma zidashobora gukoreshwa mu gukoresha amahera atari igikorwa kibi ku Wallet iva ku gikoresho gikoreshwa n’amaboko. Ushobora gushika ku bugenzuzi bwa Coin ukoresheje uburyo bwasobanuwe, umaze guhitamwo UTXO, uhitemwo _Freeze_ aho guhitamwo _Use Coin_.



![img](assets/en/26.webp)



### Nunchuki



Verisiyo y’itelefone ngendanwa ya Nunchuk na yo nyene itanga ubushobozi ku muntu ayikoresha bwo gukora ubugenzuzi bwa Coin. Niwakoresha iyi app ukoresheje telefone ngendanwa, uyifungure maze ugende kuri _Wallet_ menu. Aho uhitemwo _Reba ibiceri_.



![img](assets/en/30.webp)



Mu idirisha aho urutonde rwa UTXOs ruboneka, kanda _Hitamwo_.



![img](assets/en/38.webp)



Igikorwa co guhitamwo kiboneka iruhande ya UTXO yose. Nk’uko biri muri verisiyo y’ibiro, guhitamwo n’amaboko kuri telefone ngendanwa ya Nunchuk bikorwa mu kugenzura akarongo gatoyi kari iruhande y’amahera. Ico gicapo kirerekana umubare w’ama UTXO yatowe n’umubare wose uhari. Niwaheza, fyonda ku kimenyetso ₿ kiri mu mfuruka yo hasi ibubamfu, ari ryo tegeko ryo gutangura kwubaka igikorwa.



![img](assets/en/31.webp)



Ubu ushobora kurangiza igikorwa, uhisemwo umubare maze ukanda _Continue_.



![img](assets/en/32.webp)



Bandanya nk’uko wama ubigira, ushireko aho uja Address, insobanuro, kandi uhindure amahera.



#### Gutandukanya UTXO



Ushobora kandi gutandukanya UTXOs n’i Nunchuk igendagenda. Injira mw’idirisha ry’urutonde rw’ibiceri vy’amahera maze uhitemwo umwampi uri iruhande ya UTXO ushaka gutandukanya.



![img](assets/en/42.webp)



Uzobona umwanya wabitswe ku _Ibisobanuro vy'Igiceri_, aho ushobora guhitamwo _Gufunga iki giceri_.



![img](assets/en/43.webp)



### Bitcoin Umurinzi



Bitcoin Keeper ni Wallet ya nyuma tuzobona muri iyi nkuru. Turabona imikorere yayo ikoreshwa ku kugenzura Coin n’ikimenyetso kimwe ca Wallet, naho nyene mwene ukwo gukoresha atari yo ntumbero y’iyi porogarama nyene. Uhejeje gushinga Keeper kuri telefone yawe, uyifungure maze ufungure Wallet irimwo amahera amwamwe. Hagati y'ibarabara ry'ingenzi kanda _Reba Ibiceri Vyose_.



![img](assets/en/34.webp)



Keeper yerekana icegeranyo c’ama UTXO. Kugira ngo ushikire igicapo c'uguhitamwo kanda _Hitamwo Kugira ngo Wohereze_.



![img](assets/en/35.webp)



Ushobora guhitamwo ibiceri mu kuvyikurako mu gufyonda ku itegeko rikwiye. Niwaheza, ukande _Ohereza_.



![img](assets/en/36.webp)



Bitcoin Keeper ikujana mu _Send_ menu, aho ushobora kwubaka ibikorwa n'ama UTXO yatowe.



![img](assets/en/37.webp)



## Hardware Wallet



Imwe mu mpapuro za porogaramu ziboneka muri iyi nkuru ishobora kuba isaha gusa Interface kuri imwe mu mpapuro zawe z’ibikoresho. Bisigura ko ubugenzuzi bwa Coin ku gikoresho co gusinya ata murongo bukorwa n’intambwe zabonetse gushika ubu.



### Impanuro rusangi



Coin control ni uburyo bwiza cane bwo guhitamwo ivyo ukoresha mu gucuruza. Guhitamwo n’amaboko birarushiriza kuba vyiza iyo, igihe ugura/wakira amahera yawe, wanditse neza aho Satoshis yawe ikomoka. Niba wipfuza kwiga neza ubu buhinga, ndagusavye inyigisho ikurikira:



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Twaravuze mbere ivyerekeye `ugutandukanya ibisigarira`. Niba ushaka gufunga amasigarira kugira ngo azoyakoreshe mu nyuma maze usubire kuronka ubuzima bwite (swap kuri Layer 2), utegerezwa kwitwararika `kuyashirako ikimenyetso` igihe cose ubonye imwe. Mu bikoresho vya Software Wallets vyabonetse gushika ubu, ni Electrum yonyene itanga amabara y’ibisigazwa vya UTXO kugira ngo biboneke mu gihe umuntu abibonye. Abandi, nka Sparrow, bakwereka uruhererekane mu nzira y’inkomoko y’umuntu ku giti ciwe UTXO (`m/84’/0’/0’/1/11`).



Kugira ngo ukoreshe neza ubwo buryo, wibuke kwama wongerako insobanuro ku mpinduka ubona: uwo woherereje amahera yawe (amahera yo kwishura, inyigisho canke ibindi), arazi Address ijana n’iryo hinduka kandi arazi ko ari iyawe, kuko iva ku bikorwa mwagiranye!