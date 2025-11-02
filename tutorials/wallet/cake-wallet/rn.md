---
name: Gato Wallet.
description: Inyigisho ku gato Wallet n'ukwishyura mu gacerere
---

![cover](assets/cover.webp)


Iyi nkuru iratohoza [**Cake Wallet**](https://cakewallet.com/): Wallet y’amahera menshi ifunguye, idashobora kubikwa, yibanda ku buzima bwite iboneka kuri Android, iOS, macOS, Linux, na Windows. Tuzokwinjira mu biranga ubuzima bwite bwayo bwihariye bwa Bitcoin, tugende mu kohereza/kwakira Bitcoin biciye ku **Silent Payments** (umurongo w’ubuzima bwite wa On-Chain wateye imbere) kandi tuzogira ivyiyumviro ku gushirwa mu ngiro kwa PayJoin v2 ku bikorwa bitajanye n’igihe.


## 🎉 Ibirango vy'ingenzi



- [**Ivyishyurwa vy'agacerere (BIP-352)**](https://BIPs.dev/352/) gutera imbere [amakode y'ukwishyura] ya kera (https://ivyishyurwa vy'agacerere.xyz/docs/kugereranya-ivyifuzo-vy'ubuzima/bip47/) na vyo nyene vyitwa "N. Iyo uwurungitse akoresheje Address yawe y'ukwishura mu gacerere, Wallet yabo ironka Address yihariye y'igihe kimwe ikoresheje imfunguruzo zitandukanye zizohurizwa hamwe zibe Taproot Address y'igihe kimwe yihariye. Ivyanditswe vya Blockchain vyerekana amafaranga adafitaniye isano, bikabuza guhuza amafaranga yinjira. Ukwishura mu gacerere bitanga inyungu zitandukanye, harimwo:
    - Aderesi zishobora gusubirwamwo: Ntibikenewe ko ukoresha generate Address nshasha ku bijanye n’ugucuruza kwose, ivyo bikaba bituma umuntu ashobora gukoresha neza kandi akagira ubuzima bwiwe bwite
    - Zero igiciro co kwongerekana: Ukwishura mu gacerere ntikwongera ubunini canke igiciro c’ibikorwa.
    - Ugutahura: Abarorerezi bo hanze ntibashobora guhuza amafaranga n'Inyishu y'Iceceka Address.
    - Nta gukorana kw’uwurungitse n’uwuronka bisabwa: Amafaranga ashobora gukorwa ata guhanahana amakuru hagati y’ababigiranye.
    - Aderesi zidasanzwe z’ukwishurwa kwose: Gukuraho ingorane zo gusubira gukoresha Address mu mpanuka.
    - Nta server ikenewe: Ukwishura mu gacerere birashobora gukorwa ata server yihariye ikenewe.
- PayJoin v2** igabanya isesengura ry’igishushanyo c’ibikorwa mu gufatanya ivyo abarungika n’abakira binjira mu bikorwa bimwe. Cake Wallet ishira mu ngiro amaterambere abiri ahambaye:
    - Ibikorwa vy’ubudandaji bitajanye n’igihe**: Uwurungika n’uwuronka ntibagikeneye kuba kuri Internet icarimwe kugira ngo barangize ibikorwa vy’ubudandaji vy’ibanga.
    - Ivy’uguhanahana amakuru ata server**: Nta n’umwe mu bagize uruhande akeneye gukoresha server ya PayJoin, ivyo bikaba bikuraho intambamyi nini y’ubuhinga.
- Coin Control** ishoboza guhitamwo UTXO n'amaboko mu gihe c'ibikorwa. Ivyo bibuza guhuza amaderesi mu mpanuka igihe ukoresha ama UTXO menshi afise inkomoko itandukanye.
- TOR** infashanyo, yemerera abakoresha gutuma uruja n'uruza rw'urubuga rwabo biciye ku rubuga rwa Tor
- RBF** (Gusubirira-N’Amafaranga) iragufasha guhindura amafaranga umaze kohereza amafaranga.


## 1️⃣ Gutegura Wallet yawe


Cake Wallet itanga uburyo bwinshi bwo gufasha ku rubuga. Ushobora guhitamwo hagati ya Android, iOS/macOS, Linux na Windows.  Kugira ngo utangure, genda kuri https://docs.cakewallet.com/tangura/ maze uhitemwo ubuhinga bwawe bwo gukoresha.


![image](assets/en/01.webp)


Inyuma yo gushiramwo, shiraho `PIN` (imibare 4 canke 6). Uzoca ubona:


1. `Rema Wallet nshasha` (ku bakoresha bashasha)

2. `Subizaho Wallet` (ku bikoresho vya kera)


![image](assets/en/02.webp)


Ku rubuga rukurikira urashobora guhitamwo mu mafaranga menshi y’ivy’ubuhinga bwa none. Hitamwo `Bitcoin` hanyuma ukande kuri `Ibikurikira` hanyuma ushiremwo `izina rya Wallet` kugira ngo umenye Wallet. Mu gufyonda kuri `Ivyagezwe vy'imbere` urutonde rw' `Ivyagezwe vy'ubuzima bwite` biraboneka. Kora aya mahinduka:



- Fiat API:** hitamwo `Tor gusa` (inzira z'ibiciro bisabwa biciye muri Tor)
- Guhindura:** guhitamwo `Tor gusa` (bituma uruja n'uruza rwa Exchange rutamenyekana)


BIP-39 Ubwoko bwa seed buvugwa ku buryo busanzwe, n'uburyo bwo guhindura ubwoko bwa Electrum seed. Inzira z’Ivyakomoka ni izi zikurikira:



- Electrum: "m/0"
- BIP-39: `m/84'/0'/0`


Niba ushaka kwongerako umutekano Layer, ushobora gushinga `passphrase`.  Intumbero ihambaye y’indege passphrase ni ugutanga uburinzi bwongereweko ku bitero vy’umubiri. Naho uwugutera yoronka ijambo seed, ntashobora gushika kuri Wallet yawe ata passphrase ibereye. Mu yandi majambo, ijambo seed ryonyene rigereranya Wallet imwe, mu gihe ijambo seed ryongereweko passphrase rirema Wallet itandukanye rwose ata sano rifise n’iry’umwimerere. Ivyo bishobora kandi gutuma `amasakoshi y'ibanga` akinzwe na passphrase, kandi bikaguha ubushobozi bwo guhakana. Mu gihe c'uguhatira, woshobora guhishura ijambo seed mu gihe uzigama ivy'ubutunzi vyinshi mu Wallet irindwa na Wallet.


Niba usanzwe ukoresha urudodo rwawe, hindura `Ongera urudodo rushasha` maze ushireho `Urudodo rwawe Address` kugira ngo wemeze ibikorwa n'ibibujijwe mu bikorwa remezo vyawe bwite. Uhejeje, kanda kuri `Bandanya` na `Ibikurikira` kugira ngo ureme Wallet yawe.


![image](assets/en/03.webp)


Ku mugaragaro ukurikira, ubona ivyipfuzo:


```
On the next page you will see a series of words. This is your unique and private seed and it is the ONLY way to recover your wallet in case of lass or malfunction. It is YOUR responsibility to write it down and store it in a safe place outside of the Cake Wallet app.
```


![image](assets/en/04.webp)


Kugira ngo umenye uburyo bwiza bwo kubika ijambo ryawe rya Mnemonic, usabwe kuraba iyi nyigisho:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Kanda kuri `Ndatahura. Mwereke seed` yanje maze ubike aya majambo ahantu hatagira umutekano! Hanyuma ukande kuri `Suzuma seed` hanyuma umaze kugenzura `Fungurira Wallet`.


## 2️⃣ Amagenamiterere


Imbere y'uko twisuka cane, reka turabe `Igishushanyo c'Ingoro` na `Ivyagezwe`.


Ku rubuga rw'imbere dushobora kubona ibintu bitandukanye vyerekanywe:



- `Ibikubiyemo vya Hamburger` bitujana ku `miterere`
- Uburinganire buboneka
- Ikarata yo kwishura mu gacerere kugira ngo utangure gucapura amafaranga yoherejwe kuri Address yawe yo kwishura mu gacerere
- Ikarata ya PayJoin kugira ngo `Shoboshe` PayJoin nk'ikintu co kuzigama ubuzima bwite no kuzigama amafaranga
- hasi hariho Inzira ngufi zija kuri `Wallet Incamake`, `Kwakira`, `Guhindura` hagati ya Bitcoin n'ayandi mafaranga, `Kohereza` na `Gugura`


![image](assets/en/11.webp)


Gukanda kuri `Hamburger menu` icon bifungura urutonde rw'imiterere. Reka dusuzume amahitamwo.


![image](assets/en/05.webp)


### A - Guhuza & guhuza 🔗


Aha, turashobora gusubira gufatanya Wallet, gucunga amanode, no gufatanya node yacu bwite (ni vyiza). `Gucapura mu kwishura mu gacerere` bituma dushobora guhindura ugucapura mu kugaragaza `Gucapura kuva ku burebure bwa BLOCK` canke `Gucapura kuva kw'itariki`.


![image](assets/en/06.webp)


Nk'ikiranga `Alpha` hariho kandi uburyo bwo `Gushoboza Tor yubatswemwo` kugira ngo urongore uruja n'uruza biciye ku rubuga rwa Tor.


### B - Ukwishyura mu gacerere 🔈


Turashobora guhindura ku ikarita y’Ukwishura ata co uvuze iri ku rubuga rw’Ingoro kugira ngo tugaragaze ico kintu. Gushoboza `Guhora ukora scanning` bituma Wallet iguma ikurikirana Blockchain ku bijanye n'Ivyishurwa vy'Iceceka biza. Turashobora gusobanura ivyerekeye gupima kugira ngo duhindure uburyo bwo gupima ku vyo dukeneye nk’uko vyavuzwe haruguru.


![image](assets/en/07.webp)


### C - Umutekano n'ububiko 🗝️


Kugira ngo dukingire Wallet yacu, turashobora gukora backup mu gukurikiza ivyo dusaba muri app. Ivyo bizotuma tugira kopi nziza y’imfunguruzo zacu z’ibanga, bitume dushobora kuronka Wallet yacu iyo yazimiye canke yibwe. Ikindi, turashobora kuraba amajambo yacu ya seed n’imfunguruzo z’ibanga, guhindura PIN yacu, gushoboza kwemeza ko ari ukuri, Gushirako Umukono / Gusuzuma no gushinga 2FA kugira ngo turonke Layer y’uburinzi y’inyongera.


![image](assets/en/08.webp)


**Iciyumviro**: Kuva muri Nzero 2025, kwemeza ko umuntu afise ibimenyetso vy’urutoke ku bikoresho vya Android birakenewe kugira ngo bikore n’imiburiburi ubuhinga bwo gupima ubuzima bwo mu rwego rwa 2, ku bindi bisobanuro raba [hano](https://source.android.com/docs/security/features/biometric/measure#biometric-). Ariko rero, ico kintu gishobora guhinduka muri kazoza.


### D - Amagenamiterere y'ubuzima bwite 🔒


Turashobora kandi kwongereza umutekano wa Wallet yacu mu gukoresha Tor kugira ngo dushiremwo amakuru y’uruja n’uruza rwacu rwa interineti no kurinda ubuzima bwite bwacu igihe turonka amakuru yo hanze. Ikindi, turashobora kubuza amafoto gufata amakuru kugira ngo amakuru yacu ya Wallet agume ari ibanga, gutuma amaderesi yikora ashobora guhingura ayandi mashasha ku bijanye n’ugucuruza kwose, no guhagarika ibikorwa vyo kugura/kugurisha kugira ngo twirinde gucuruza ata wemerewe. Ikindi turashobora `Gushoboza PayJoin`, ari co kindi kintu c'ubuzima bwite tuzosubiramwo mu nyuma.


![image](assets/en/09.webp)


### E - Ibindi vyategekanijwe 🔧


Ibindi bikoresho bituma dushobora gucunga amafaranga y’imbere no gushinga urugero rw’amafaranga y’imbere y’ibindi ku bikorwa vyacu. Ivyo bituma dushobora kugenzura amahera y’ugucuruza ajanye n’Ivyishyurwa vyacu vy’Iceceka, twisunze uko urubuga rukoreshwa muri iki gihe.


![image](assets/en/10.webp)


## 3️⃣ Kwakira ₿itcoin ukoresheje kwishura mu gacerere


Hariho uburyo bwinshi n'ubwoko bwa Address bwo kwakira Bitcoin. `SegWit (P2WPKH)` *(gutangura na bc1q....)* ni uburyo bwo guhitamwo.  Reka duhitemwo `Ivyishyurwa bicereje` muri aka karorero.


Kugira ngo uronke Ukwishyura mu gacerere, banza ukande ku kimenyetso ca `Kwakira` muri Cake Wallet. Inyuma y’aho, wandike amahera witeze kuronka. Kugira ngo ugaragaze ubwoko bwa Address, nusubire gukora kuri `Kwakira` hejuru y'ibarabara, hanyuma uhitemwo `Ivyishyurwa bicereje` mu mahitamwo.


Ku rubuga nyamukuru, hazoboneka kode yawe ya QR ya Silent Payment ushobora gusubira gukoresha be na Address. Nk’uko vyari bitezwe, Address ni ndende cane:


`sp1qq0ryu780uwragyk06prxn29830a9csnl3wvr4as6fwh73rzn28zzcqmc6ve36vadllfztaa403ty9et0rlzup7kt55qh486gxzrde6y27c8s6.


![image](assets/en/12.webp)


Ubu rero, koresha Wallet ihuye na BIP-352 (nk’iyitwa Blue Wallet) kugira ngo ukoreshe iyo kode ya QR maze wohereze amahera. Uzobona ko Wallet ikomoka ku nzira yihariye Address ivuye kuri Address yawe icereje.


![image](assets/en/13.webp)


## 4️⃣ Kwohereza ₿itcoin ukoresheje kwishura mu gacerere


Kubera ko Blue Wallet ishobora gusa`Kohereza` Amahera y'Iceceka, tuzokoresha uwundi BIP 352 Wallet ihuye nk'uwuzokwakira. Ivyo bihuye n’ivyo mu gihe umuntu akoresha Bitcoin mu buryo busanzwe.



- Kanda kuri `Kohereza` ku gicapo c'imbere
- canke gushiramwo `sp1qq...` Address yacu ishobora gusubirwamwo canke gucapura kode ya QR mu buryo butaziguye muri porogarama.
- Hitamwo amahera ushaka gukoresha mu mahera ufise
- Kanda kuri `Kohereza` hasi ku mugaragaro kugira ngo wemeze ugucuruza


Tumaze kwinjira muri `sp1qq...` Address, Wallet ica ibona ubwo nyene `bc1p...` Taproot Address (P2TR) ihuye n’iyo mu nyuma, izokoreshwa mu kwishura mu gacerere.


Turashobora kwandika inyandiko yo mu mutima ku bijanye n’ugucuruza kwose, guhindura amafaranga canke guhitamwo UTXO zimwe zimwe ku bijanye n’ugucuruza dukoresheje ubuhinga bwa `Coin Control`.


![image](assets/en/14.webp)


`Swipe` iburyo kugira ngo wemeze ibikorwa.


Uhejeje kohereza iyo nkuru, uzobazwa nimba woshima kwongerako iyo nkuru mu gitabu cawe ca Address.


![image](assets/en/15.webp)


## 6️⃣ PayJoin


Reka dusuzume ico PayJoin ari co [ku] (inyandiko.


_Payjoin v2 ni uburyo bwo kuzigama ubuzima bwite no kuzigama amafaranga muri Bitcoin butuma uwurungitse n’uwuronka amafaranga bakorana kugira ngo bashireho amafaranga amwe. Iryo soko rifise inyishu zivuye kuri *uwurungitse* n'uwuronka, bica ku buhinga bwo gucungera Bitcoin busanzwe kandi bikaba bituma habaho ugupima neza no kuzigama amafaranga mu bihe bimwebimwe._


Kugira ngo umenye vyinshi ku vyerekeye PayJoin urashobora kandi gusura inyigisho ikurikira.


https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

Kugira ngo ukoreshe PayJoin, abo bompi basaba Wallet ihuye na PayJoin, kandi uwuyironka akeneye kugira n’imiburiburi Coin imwe canke umusaruro muri Wallet yiwe. Kugira utangure, ukurikize izi ntambwe:


1. Kanda kuri `Menu ya Hamburger` hanyuma ukande kuri buto ya `Ibanga`

2. Hindura `Koresha PayJoin` Amahitamwo

3. Kanda kuri `Receive` ku rubuga rw’Imbere uzobona PayJoin QR Code n’ubuto bwo gukopa (iyo uhisemwo SegWit)


![image](assets/en/16.webp)


## 7️⃣ Ibindi biranga


Hariho n’ibindi bikoresho vyinshi nk’amafaranga menshi `Swaps`, `Buy and Sell` amahitamwo n’amahuza atandukanye y’abaguzi na porogarama zihariye za Cake nka `Cake Pay`, zigufasha kugura amakarita yishuwe mbere canke amakarita y’ingabirano.


![image](assets/en/17.webp)


## 🎯 Insozero


Iyi ni isuzuma ryacu rya Cake Wallet, itanga ubuzima bwite bwa Bitcoin kubera ibiranga nk'Ukwishura mu gacerere (BIP-352) na PayJoin v2.


Silent Payments zisubirira aderesi zikoreshwa rimwe gusa n’amaderesi ashobora gukoreshwa kandi kugira ngo zibuze On-Chain guhuza amafaranga yinjira. Naho ibibazo vyo gukorana n’ibindi bitabu vya kera vyarateye imbere cane, hariho ibisabwa bimwebimwe vyo gukoresha ubuhinga bwa none kugira ngo umuntu ashobore gucapura no kumenya ivyishyurwa bicereje bisabwa, ivyo bikaba bisaba ubutunzi bwinshi n’uburebure bw’uruja n’uruza.


PayJoin v2 ihungabanya isesengura ry’uruzitiro mu gufatanya ivyinjijwe vy’uwohereza n’uwukira mu bikorwa bimwe bimwe ata mahera y’inyongera canke uguhuza ibikorwa hagati. Ivyo bica bimenagura input rusangi-Ownership heuristic, ariko ni akamaro kanini kuko bisigura ko udashobora kwiyumvira ko inputs zose ari iz’uwazirungitse.


Ku bakoresha bashira imbere ukutamenyekana mu vy’amahera, Cake Wallet ni uburyo bushoboka. Ishiramwo amategeko y’ubuzima bwite ataco akora mu bikorwa vyayo nyamukuru, bikaba bituma umuntu ashobora kuyaronka ataco akora mu buryo bw’ubuhinga. Uko ugucungera ama blockchains ya bose kugenda kwongerekana, ibikoresho nk’ibi birafasha kubungabunga ubuzima bwite bw’ibikorwa aho bihambaye cane. Gushirwa mu ngiro kwagutse kw’izo ngingo mfatirwako mu gihugu ca Wallet vyoba ari iterambere ryiza.


## 📚 Ibikoresho


https://agakate.com


https://inyandiko.agakate.com/


https://github.com/ubuhinga-bw'agakate/igikapu_c'agakate


https://urubuga.agakate.com/


[https://ukwishyura mu gacerere.xyz/](https://ukwishyura mu gacerere.xyz/)


[Ikibanza ca BIPs.Iterambere/352/](Ikibanza ca BIPs.Iterambere/352/)


Urubuga rwa PayJoin.ur/