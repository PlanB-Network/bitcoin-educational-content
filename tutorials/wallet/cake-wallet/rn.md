---
name: Cake Wallet
description: Inyigisho ku gato Wallet n'ukwishyura mu gacerere
---

![cover](assets/cover.webp)


Iyi nkuru iratohoza [**Cake Wallet**](https://cakewallet.com/): wallet y’amahera menshi ifunguye, idashobora kubikwa, yibanda ku buzima bwite, iboneka kuri Android, iOS, macOS, Linux, na Windows. Tuzokwinjira mu biranga ubuzima bwite bwayo bwihariye bwa Bitcoin, tugende mu kohereza/kwakira Bitcoin biciye ku **Silent Payments** (umurongo w’ubuzima bwite wa on-chain wateye imbere) kandi tuzogira ivyiyumviro ku gushirwa mu ngiro kwa PayJoin v2 ku bikorwa bitajanye n’igihe.


## 🎉 Ibirango vy'ingenzi



- [**Ivyishyurwa bicereje (BIP-352)**](https://bips.dev/352/) gutera imbere [amakode y’ukwishyura] ya kera (https://ivyishyurwa bicereje.xyz/docs/kugereranya-ivyifuzo/bip47/) navyo vyitwa "PayN us Iyo uwurungitse akoresheje aderesi yawe yo kwishura mu gacerere, wallet yabo ironka aderesi yihariye y’igihe kimwe ikoresheje imfunguruzo zitandukanye zizohurizwa hamwe zibe aderesi yihariye y’igihe kimwe ya Taproot. Ivyo bitabo vyerekana amafaranga adafitaniye isano, bikabuza guhuza amafaranga yinjira. Ukwishura mu gacerere bitanga inyungu zitandukanye, harimwo:
    - Aderesi zishobora gusubirwamwo: Ntibikenewe ko ukoresha generate aderesi nshasha ku bijanye n’ugucuruza kwose, bikaba bituma umuntu ashobora gukoresha neza kandi akagira ubuzima bwiwe bwite
    - Zero igiciro co kwongerekana: Ukwishura mu gacerere ntikwongera ubunini canke igiciro c’ibikorwa.
    - Ugutahura: Abarorerezi bo hanze ntibashobora guhuza amafaranga n’aderesi y’Ukwishura mu gacerere.
    - Nta gukorana kw’uwurungitse n’uwuronka bisabwa: Amafaranga ashobora gukorwa ata guhanahana amakuru hagati y’ababigiranye.
    - Aderesi zidasanzwe ku kwishura kwose: Gukuraho ingorane zo gusubira gukoresha aderesi mu mpanuka.
    - Nta server ikenewe: Ukwishura mu gacerere birashobora gukorwa ata server yihariye ikenewe.
- PayJoin v2** igabanya isesengura ry’igishushanyo c’ibikorwa mu gufatanya ivyo abarungika n’abakira binjira mu bikorwa bimwe. Cake Wallet ishira mu ngiro amaterambere abiri ahambaye:
    - Ibikorwa vy’ubudandaji bitajanye n’igihe**: Uwurungika n’uwuronka ntibagikeneye kuba kuri Internet icarimwe kugira ngo barangize ibikorwa vy’ubudandaji vy’ibanga.
    - Ivy’Imenyekanisha ata Server**: Nta n’umwe mu bagize uruhande akeneye gukoresha server ya Payjoin, bikuraho intambamyi nini y’ubuhinga.
- Coin Control** ishoboza guhitamwo UTXO n'amaboko mu gihe c'ibikorwa. Ivyo bibuza guhuza amaderesi mu mpanuka igihe ukoresha ama UTXO menshi afise inkomoko itandukanye.
- TOR** infashanyo, yemerera abakoresha gutuma uruja n'uruza rw'urubuga rwabo biciye ku rubuga rwa Tor
- RBF** (Subiriza-N’Amafaranga) iragufasha guhindura amafaranga umaze kohereza amafaranga.


## 1️⃣ Gutegura Wallet yawe


Cake Wallet itanga uburyo bwinshi bwo gufasha ku rubuga. Ushobora guhitamwo hagati ya Android, iOS/macOS, Linux na Windows.  Kugira ngo utangure, genda kuri https://docs.cakewallet.com/tangura/ maze uhitemwo ubuhinga bwawe bwo gukoresha.


![image](assets/en/01.webp)


Inyuma yo gushiramwo, shiraho `PIN` (imibare 4 canke 6). Uzoca ubona:


1. `Rema Wallet nshasha` (ku bakoresha bashasha)

2. `Subizaho Wallet` (ku bikoresho vya kera)


![image](assets/en/02.webp)


Ku rubuga rukurikira urashobora guhitamwo mu mafaranga menshi y’ivy’ubuhinga bwa none. Hitamwo `Bitcoin` hanyuma ukande kuri `Ibikurikira` hanyuma ushiremwo `izina rya Wallet` kugira ngo umenye wallet. Mu gufyonda kuri `Ivyagezwe vy'imbere` urutonde rw' `Ivyagezwe vy'ubuzima bwite` biraboneka. Kora aya mahinduka:



- Fiat API:** hitamwo `Tor gusa` (inzira z'ibiciro bisabwa biciye muri Tor)
- Guhindura:** guhitamwo `Tor gusa` (bihindura amazina)


BIP-39 Ubwoko bwa seed buvugwa ku buryo busanzwe, n'uburyo bwo guhindura ubwoko bwa Electrum seed. Inzira z’Ivyakomoka ni izi zikurikira:



- Electrum: "m/0"
- BIP-39: `m/84'/0'/0`


Niba ushaka kwongerako ikindi gice c'umutekano, ushobora gushinga `passphrase`.  Intumbero ihambaye y’indege passphrase ni ugutanga uburinzi bwongereweko ku bitero vy’umubiri. Naho uwugutera yoronka ijambo seed, ntashobora gushika kuri wallet yawe ata passphrase ibereye. Mu yandi majambo, ijambo seed ryonyene rigereranya wallet imwe, mu gihe ijambo seed ryongeweko passphrase rirema wallet itandukanye rwose ata sano rifise n’iry’umwimerere. Ivyo bishobora kandi gutuma `amasakoshi y'ibanga` akinzwe na passphrase, kandi bikaguha ubushobozi bwo guhakana. Mu gihe c'uguhatira, woshobora guhishura ijambo seed mu gihe uzigama ivy'ubutunzi vyinshi mu wallet irindwa na passphrase.


Niba usanzwe ukoresha urudodo rwawe, hindura `Ongera Urudodo Rushasha` maze ushireho `Urudodo rwawe Address` kugira ngo wemeze ibikorwa n'ibibujijwe mu bikorwa remezo vyawe bwite. Uhejeje, kanda kuri `Bandanya` na `Ibikurikira` kugira ngo ureme wallet yawe.


![image](assets/en/03.webp)


Ku mugaragaro ukurikira, ubona ivyipfuzo:


```
On the next page you will see a series of words. This is your unique and private seed and it is the ONLY way to recover your wallet in case of lass or malfunction. It is YOUR responsibility to write it down and store it in a safe place outside of the Cake Wallet app.
```


![image](assets/en/04.webp)


Kugira ngo umenye uburyo bwiza bwo kubika amajambo yawe y'ubwenge, usabwe kuraba iyi nyigisho:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Kanda kuri `Ndatahura. Mwereke seed` yanje maze ubike aya majambo ahantu hatagira umutekano! Hanyuma ukande kuri `Suzuma seed` hanyuma umaze kugenzura `Fungurira Wallet`.


## 2️⃣ Amagenamiterere


Imbere y'uko twisuka cane, reka turabe `Igishushanyo c'Ingoro` na `Ivyagezwe`.


Ku rubuga rw'imbere dushobora kubona ibintu bitandukanye vyerekanywe:



- `Ibikubiyemo vya Hamburger` bitujana ku `miterere`
- Uburinganire buboneka
- Ikarata yo kwishura mu gacerere kugira ngo utangure gucapura amafaranga yoherejwe kuri aderesi yawe yo kwishura mu gacerere
- Ikarata ya Payjoin kugira ngo `Shoboshe` Payjoin nk'ubuzima bwite-kuzigama no kuzigama amafaranga
- hasi hariho Inzira ngufi zija kuri `Wallet Incamake`, `Kwakira`, `Guhindura` hagati ya Bitcoin n'ayandi mafaranga, `Kohereza` na `Gugura`


![image](assets/en/11.webp)


Gukanda kuri `Hamburger menu` icon bifungura urutonde rw'imiterere. Reka dusuzume amahitamwo.


![image](assets/en/05.webp)


### A - Guhuza & guhuza 🔗


Aha, turashobora gusubira gufatanya wallet, gucunga amanode, no gufatanya node yacu bwite (ni vyiza). `Gucapura mu kwishyura mu gacerere` bituma dushobora guhindura ugucapura mu kugaragaza `Gucapura kuva ku burebure bw'ibarabara` canke `Gucapura kuva kw'itariki`.


![image](assets/en/06.webp)


Nk'ikiranga `Alpha` hariho kandi uburyo bwo `Gushoboza Tor yubatswemwo` kugira ngo urongore uruja n'uruza biciye ku rubuga rwa Tor.


### B - Ukwishyura mu gacerere 🔈


Turashobora guhindura ku ikarita y’Ukwishura ata co uvuze iri ku rubuga rw’Ingoro kugira ngo tugaragaze ico kintu. Gushoboza `Guhora ukora scanning` bituma wallet iguma ikurikirana blockchain ku bijanye n’Ivyishurwa vy’Icereje biza. Turashobora gusobanura ivyerekeye gupima kugira ngo duhindure uburyo bwo gupima ku vyo dukeneye nk’uko vyavuzwe haruguru.


![image](assets/en/07.webp)


### C - Umutekano n'ububiko 🗝️


Kugira ngo tuzigame wallet yacu, turashobora gukora backup mu gukurikiza ivyo dusaba muri app. Ivyo bizotuma tugira kopi nziza y’imfunguruzo zacu z’ibanga, bitume dushobora kuronka wallet yacu iyo yazimiye canke yibwe. Ikindi, turashobora kubona ijambo ryacu rya seed n’imfunguruzo z’ibanga, guhindura PIN yacu, gushoboza kwemeza ivy’ukuri, Gushirako Umukono / Gusuzuma no gushinga 2FA kugira ngo turonke uburinzi bwongereweko.


![image](assets/en/08.webp)


**Iciyumviro**: Kuva muri Nzero 2025, kwemeza ko umuntu afise urutoke ku bikoresho vya Android birakenewe kugira ngo bikore n’imiburiburi ubuhinga bwo gupima urutoke bwo mu rwego rwa 2, ku bindi bisobanuro raba [hano](https://source.android.com/docs/security/features/biometric/measure#biometric-). Ariko rero, ico kintu gishobora guhinduka muri kazoza.


### D - Amagenamiterere y'ubuzima bwite 🔒


Turashobora kandi kwongereza umutekano wa wallet yacu mu gukoresha Tor kugira ngo dushiremwo amakuru y’uruja n’uruza rwacu rwa interineti no kurinda ubuzima bwite bwacu igihe turonka amakuru yo hanze. Ikindi, turashobora kubuza amafoto gufata amakuru kugira ngo amakuru yacu ya wallet agume ari ibanga, gutuma amaderesi yikora ashobora guhingura ayandi mashasha ku bijanye n’ugucuruza kwose, no guhagarika ibikorwa vyo kugura/kugurisha kugira ngo ntihagire amaderesi atarekuriwe. Ikindi turashobora `Gushoboza PayJoin`, ari co kindi kintu c'ubuzima bwite tuzosubiramwo mu nyuma.


![image](assets/en/09.webp)


### E - Ibindi vyategekanijwe 🔧


Ibindi bikoresho bituma dushobora gucunga amafaranga y’imbere no gushinga urugero rw’amafaranga y’imbere y’ibindi ku bikorwa vyacu. Ivyo bituma dushobora kugenzura amahera y’ugucuruza ajanye n’Ivyishyurwa vyacu vy’Iceceka, twisunze uko urubuga rukoreshwa muri iki gihe.


![image](assets/en/10.webp)


## 3️⃣ Kwakira ₿itcoin ukoresheje kwishura mu gacerere


Hariho uburyo bwinshi n'ubwoko bw'amaderesi bwo kwakira Bitcoin. `Segwit (P2WPKH)` *(gutangura na bc1q....)* ni uburyo bwo guhitamwo.  Reka duhitemwo `Ivyishyurwa bicereje` muri aka karorero.


Kugira ngo uronke Ukwishyura mu gacerere, banza ukande ku kimenyetso ca `Kwakira` muri Cake Wallet. Inyuma y’aho, wandike amahera witeze kuronka. Kugira ngo ugaragaze ubwoko bwa aderesi, nusubire gukora kuri `Kwakira` hejuru y'ibarabara, hanyuma uhitemwo `Ukwishyura mu gacerere` mu mahitamwo.


Ku rubuga nyamukuru, hazoboneka kode yawe ya QR n’aderesi yawe yo kwishura mu gacerere. Nk’uko vyari bitezwe, aderesi ni ndende cane:


`sp1qq0ryu780uwragyk06prxn29830a9csnl3wvr4as6fwh73rzn28zzcqmc6ve36vadllfztaa403ty9et0rlzup7kt55qh486gxzrde6y27c8s6.


![image](assets/en/12.webp)


Ubu rero, koresha wallet ihuye na BIP-352 (nk’iyitwa Blue Wallet) kugira ngo ukoreshe iyo kode ya QR maze wohereze amahera. Uzobona ko wallet ikura aderesi yihariye y’aho ija ku aderesi yawe y’agacerere.


![image](assets/en/13.webp)


## 4️⃣ Kwohereza ₿itcoin ukoresheje kwishura mu gacerere


Kubera ko Blue Wallet ishobora gusa`Kohereza` Amahera y'Iceceka, tuzokoresha uwundi BIP 352 ahuye wallet nk'uwuzokwakira. Ivyo bihuye n’ivyo umuntu akora mu gihe c’ugucuruza Bitcoin.



- Kanda kuri `Kohereza` ku gicapo c'imbere
- canke gushiramwo aderesi yacu `sp1qq...` ishobora gusubirwamwo canke gucapura kode ya QR mu buryo butaziguye muri porogarama.
- Hitamwo amahera ushaka gukoresha mu mahera ufise
- Kanda kuri `Kohereza` hasi ku mugaragaro kugira ngo wemeze ugucuruza


Tumaze kwinjiza aderesi `sp1qq...`, wallet ica ibona ubwo nyene aderesi `bc1p...` Taproot (P2TR) ihuye n’iyo mu nyuma, izokoreshwa mu kwishura mu gacerere.


Turashobora kwandika inyandiko yo mu mutima ku bijanye n’ugucuruza kwose, guhindura amafaranga canke guhitamwo UTXO zimwe zimwe ku bijanye n’ugucuruza dukoresheje ubuhinga bwa `Coin Control`.


![image](assets/en/14.webp)


`Swipe` iburyo kugira ngo wemeze ibikorwa.


Uhejeje kohereza iyo nkuru, uzobazwa nimba woshima kwongerako uwo muntu mu gitabu cawe c’amaderesi.


![image](assets/en/15.webp)


## 5️⃣ PayJoin


Reka dusuzume ico PayJoin ari co [ku vyerekeye](inyandiko.


_Payjoin v2 ni uburyo bwo kuzigama ubuzima bwite no kuzigama amafaranga muri Bitcoin butuma uwurungitse n’uwuronka amafaranga bakorana kugira ngo bashireho amafaranga amwe. Iryo soko rifise inyishu zivuye kuri *uwurungitse* n'uwuronka, bica ku buhinga bwo gucungera Bitcoin busanzwe kandi bikaba bituma habaho ugupima neza no kuzigama amafaranga mu bihe bimwebimwe._


Kugira ngo umenye vyinshi ku vyerekeye PayJoin urashobora kandi gusura inyigisho ikurikira.


https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

Kugira ngo ukoreshe PayJoin, abo bompi basaba wallet ihuye na PayJoin, kandi uwuyironka akeneye kugira n’imiburiburi igiceri kimwe canke umusaruro muri wallet yiwe. Kugira utangure, ukurikize izi ntambwe:


1. Kanda kuri `Menu ya Hamburger` hanyuma ukande kuri buto ya `Ibanga`

2. Guhindura `Koresha Payjoin` Amahitamwo

3. Kanda kuri `Receive` ku rubuga rw’imbere uzobona PayJoin QR Code n’ubuto bwo gukopa (iyo uhisemwo Segwit)


![image](assets/en/16.webp)


## 6️⃣ Ibindi biranga


Hariho n’ibindi bikoresho vyinshi nk’amafaranga menshi `Swaps`, `Buy and Sell` amahitamwo n’amahuza atandukanye y’abaguzi na porogarama zihariye za Cake nka `Cake Pay`, zigufasha kugura amakarita yishuwe mbere canke amakarita y’ingabirano.


![image](assets/en/17.webp)


## 🎯 Insozero


Iyi ni isuzuma ryacu rya Cake Wallet, itanga ubuzima bwite bwa Bitcoin bushimishijwe n’ibintu nk’Ukwishura mu gacerere (BIP-352) na Payjoin v2.


Silent Payments zisubirira aderesi zikoreshwa rimwe gusa n’amaderesi ashobora gukoreshwa kandi kugira ngo zibuze on-chain guhuza amafaranga yinjira. Naho ibibazo vyo gukorana n’ibindi bitabu vya kera vyarateye imbere cane, hariho ibisabwa bimwebimwe vyo gukoresha ubuhinga bwa none kugira ngo umuntu ashobore gucapura no kumenya ivyishyurwa bicereje bisabwa, ivyo bikaba bisaba ubutunzi bwinshi n’uburebure bw’uruja n’uruza.


Payjoin v2 ihungabanya isesengura ry’uruhererekane mu gufatanya ivyinjijwe vy’uwohereza n’uwukira mu bikorwa bimwe ata mahera y’inyongera canke uguhuza ibikorwa hagati. Ivyo bica bica mu nzira isanzwe y’ubuhinga bwo gushiramwo ibintu, ariko ni akamaro kanini kuko bisigura ko udashobora kwiyumvira ko ibintu vyose vyinjizwa ari ivy’uwabirungitse.


Ku bakoresha bashira imbere ukutamenyekana mu vy’amahera, Cake Wallet ni uburyo bushoboka. Ishiramwo amategeko y’ubuzima bwite ataco akora mu bikorwa vyayo nyamukuru, bikaba bituma umuntu ashobora kuyaronka ataco akora mu buryo bw’ubuhinga. Uko ugucungera ama blockchains ya bose kugenda kwongerekana, ibikoresho nk’ibi birafasha kubungabunga ubuzima bwite bw’ibikorwa aho bihambaye cane. Gushirwa mu ngiro kwagutse kw’izo ngingo mfatirwako mu gihugu ca wallet vyoba ari iterambere ryiza.


## 📚 Ibikoresho


https://agakate.com


https://inyandiko.agakate.com/


https://github.com/ubuhinga-bw'agakate/igikapu_c'agakate


https://urubuga.agakate.com/


[https://ukwishyura mu gacerere.xyz/](https://ukwishyura mu gacerere.xyz/)


[Ikiganiro/352/](Ikiganiro/352/)


https://kwifatanya.org/