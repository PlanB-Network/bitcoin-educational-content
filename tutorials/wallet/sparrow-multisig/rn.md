---
name: Sparrow Wallet - Multisig
description: Kora Wallet y'imikono myinshi kuri Sparrow
---
![cover](assets/cover.webp)


Wallet y'imikono myinshi (akenshi yitwa "*Multisig*") ni uburyo Bitcoin Wallet yubatswe busaba imikono myinshi y'ubuhinga bwo kupfutsa amakuru, ivuye ku mfunguruzo zitandukanye, kugira ngo ikoreshwa ry'amahera ryemezwe. Bitandukanye na Wallet isanzwe ("*singlesig*"), aho urufunguzo rw'ibanga rumwe rukwiye kugira ngo UTXO ifungurwe, Multisig ishingiye ku kigereranyo ca **m-of-n**: mu mfunguruzo _n_ zifatanye na Wallet, _m_ zitegerezwa kwifatanya ku mukono ku gikorwa cose co gucuruza.


Ubu buryo butuma ubugenzuzi bwa Wallet bushobora gusangirwa hagati y'abantu canke ibikoresho vyinshi. Nk'akarorero, mu miterere ya 2-of-3, hakorwa amatsinda atatu yigenga y'imfunguruzo, ariko abiri gusa ni yo akenewe kugira ngo amahera afungurwe. Uwo mugambi uragabanya cane ingorane zijanye no gucumbagira canke gutakaza urufunguzo: umusuma afise ububasha ku rufunguzo rumwe gusa ntashobora gukubura Wallet, kandi uwukoresha atakaje urumwe aracashobora kuronka amahera yiwe akoresheje ibiri bisigaye.


![Image](assets/fr/01.webp)


Ariko rero, uwo mutekano mwinshi uzana n'ingorane nyinshi. Gushiraho Wallet ya Multisig bisaba kubungabunga amajambo menshi ya Mnemonic (rimwe ku kintu cose co gusinya) hamwe n'imfunguruzo za bose zagutse ("*xpub*"). Nkako, nimba ukoresha Wallet ya Multisig 2-of-3, kugira ngo uyisubizeho utegerezwa kugira amajambo yose atatu ya Mnemonic, canke n'imiburiburi abiri kuri atatu. Ariko nimba ufise abiri gusa kuri atatu, ukeneye kandi kuronka *xpubs* zose zitatu, kuko utazifise bizoba bidashoboka gusubizaho imfunguruzo za bose zikenewe kugira ngo uronke ama bitcoins zikingira.


Mu ncamake, kugira ngo usubizeho Wallet ya Multisig, utegerezwa :


- Canke kuronka amajambo yose ya Mnemonic afatanye n'ikintu cose co gusinya;
- Canke kugira umubare mutoyi w'amajambo ya Mnemonic usabwa n'urugero kugira ngo ushobore gusinya, kandi ukaronka xpubs z'ibintu vyose kugira ngo usubizeho imfunguruzo za bose zikenewe.


![Image](assets/fr/02.webp)


Uku kucungera ivyabitswe vya Wallet ya Multisig birorohejwe n'*Output Script Descriptors*, ihuriza hamwe amakuru yose ya bose akenewe kugira ngo uronke amahera. Ariko rero, iyo mikorere ntiraboneka muri porogaramu zose zicungera ama wallets.


Multisig ibereye canecane aba bitcoiners barondera umutekano wongerejwe canke ugucungera amahera hamwe: amasosiyete, amashirahamwe, imiryango, canke abakoresha ku giti cabo bafise ingero nini y'ama bitcoins. Irashobora gukoreshwa mu kurema imigambi y'uburongozi butari mu maboko y'umuntu umwe, nk'akarorero, mu kugabura ububasha bwo gusinya hagati y'abayobozi canke abagize itsinda benshi.


Muri iyi nyigisho, tuzokwiga ingene turema kandi tukoresha Wallet isanzwe y'imikono myinshi hakoreshejwe **Sparrow Wallet**. Nimba wipfuza kurema Wallet y'imikono myinshi yatunganijwe ukwayo ifise Timelocks, ndagusaba gukoresha Liana:


https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Ivyo bikenewe


Muri iyi nyigisho, ngiye kukwereka ingene ukora Multisig ukoresheje [porogaramu ya Sparrow Wallet icungera ama wallets](https://sparrowwallet.com/download/). Nimba utarashira iyo porogaramu ku gikoresho cawe, uyishireho ubu. Nimba ukeneye ubufasha, dufise kandi inyigisho irambuye ku bijanye no gutunganya Sparrow Wallet :


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Kugira ngo utunganye Wallet y'imikono myinshi, uzokenera hardware wallets zitandukanye. Nk'akarorero, kuri Multisig 2-of-3, ushobora gukoresha :


- Trezor Model One;
- Ledger Flex;
- Passport Core.


![Image](assets/fr/03.webp)


Ni vyiza gukoresha ubwoko butandukanye bwa Hardware Wallet mu miterere ya Multisig yawe. Ivyo bituma nimba icitegererezo kimwe cagize ingorane nkomeye, ntikizogira ico gikoze ku mutekano wose wa Multisig yawe. Ikindi kandi, biratuma uronka ivyiza vyihariye vya buri gikoresho. Nk'akarorero, mu miterere yanje :



- Trezor Model One ni y'inkomoko yuguruye rwose, ivyo bikaba bituma umuntu ashobora kugenzura ukuntu seed yakozwe. Ariko rero, kubera ko idafise Secure Element, iguma ishobora guterwa n'ibitero vy'umubiri;



- Ledger Flex, ku rundi ruhande, ifise firmware yigenga idashobora kugenzurwa, ariko irimwo Secure Element itanga ukwikingira kw'umubiri kwiza cane;



- Passport Core ihuriza hamwe firmware y'inkomoko yuguruye yose, Secure Element, no guhanahana amakuru biciye kuri QR code ata muhuza (air-gapped). Ni umusinya wa gatatu yigenga ashobora kugenzura amaderesi no gushira umukono kuri PSBTs ata huza ry'amakuru rya USB.


Imbere y'uko utunganya Wallet yawe ya Multisig, urabe neza ko Hardware Wallet imwimwe yatunganijwe neza (ukwibonera n'ukubika ijambo rya Mnemonic, ukushinga kode ya PIN). Ku mabwirizwa arambuye, urashobora kuraba inyigisho zacu ku Hardware Wallet imwimwe, nk'akarorero :


https://planb.academy/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Nk'uko tuzobibona imbere muri iyi nyigisho, birashoboka kandi gushira mu miterere ya Multisig yawe ikintu kidafatanye na Hardware Wallet, ariko imfunguruzo zaco z'ibanga zibitswe kuri PC yawe. Ubu buryo, nta gukeka, ntibufise umutekano nk'ubwo bwo gukoresha gusa hardware wallets, ariko bushobora kugira akamaro mu bihe bimwebimwe. Nk'akarorero, kuri Multisig 2-of-3, ushobora guhitamwo hardware wallets zibiri na Software Wallet imwe.

> ⚠️ **Itangazo ry'umutekano kuri Coldcard MK3:** ntukore seed nshasha kuri MK3 ikoresha firmware iri imbere ya 4.2.0. Seed zakozwe kuri firmware ya kera zitegerezwa gusubirirwa kandi amahera akimurwa. Ni co gituma iyi nyigisho ikoresha Passport Core nk'umusinya w'ishimikiro ata muhuza (air-gapped).


## Kurema Wallet ya Multisig


Fungura Sparrow Wallet, kanda ku rubuga rwa "*File*", hanyuma uhitemwo "*New Wallet*".


![Image](assets/fr/04.webp)


Ha izina Wallet yawe y'imikono myinshi, hanyuma ukande kuri "*Create Wallet*" kugira ngo wemeze.


![Image](assets/fr/05.webp)


Mu rutonde ruza rwa "*Policy Type*", hitamwo "*Multi Signature*".


![Image](assets/fr/06.webp)


Mu mfuruka yo hejuru iburyo, ubu urashobora kwerekana igitigiri cose c'imfunguruzo ziri muri Multisig yawe, hamwe n'igitigiri c'abasinyanira gisabwa kugira ngo ikoreshwa ry'amahera ryemezwe. Mu karorero kanje, ni ikigereranyo ca 2-of-3.


![Image](assets/fr/07.webp)


Munsi y'idirisha, Sparrow Wallet yerekana "*Keystore*" zitatu. Imwimwe igereranya itsinda ry'imfunguruzo. Aha, ndakoresha hardware wallets zitatu, rero "*Keystore*" imwimwe ihuye n'imwe muri zo. Ubu tuzozitunganya.


Ndatangura na Passport Core. Ku rubuga rwa "*Keystore 1*", ndahitamwo "*Airgapped Hardware Wallet*".


![Image](assets/fr/08.webp)


Kuri Passport, fungura konti wipfuza gukoresha, hanyuma uhitemwo "*Connect Wallet*" > "*Sparrow*" > "*Connect as Multisig*". Passport yerekana QR code inyiganyigana irimwo amakuru y'urufunguzo rwayo rwa bose.

Muri Sparrow, hitamwo "*Scan...*" iri iruhande ya "*Passport*" hanyuma ucapure iyo QR code inyiganyigana ukoresheje kamera ya mudasobwa yawe. Gereranya urutoke rw'urufunguzo nyamukuru rwerekanwa na Sparrow n'urwerekanwa na Passport, hanyuma winjize keystore.

Ubu xpub ya Passport yawe yarinjijwe. Subira ukore uburyo bubereye kuri Ledger Flex na Trezor Model One.


Kuri Ledger Flex, ndahitamwo "*Keystore 2*", hanyuma nkanda kuri "*Connected Hardware Wallet*". Urabe neza ko Ledger ifatanye na mudasobwa, ifunguruwe, kandi ko porogaramu ya Bitcoin ifunguwe.


![Image](assets/fr/15.webp)


Hanyuma ukande kuri buto ya "*Scan...*".


![Image](assets/fr/16.webp)


Iruhande y'izina rya hardware wallet yawe, kanda kuri "*Import Keystore*".


![Image](assets/fr/17.webp)


Umusinya wa kabiri ubu yanditswe neza muri Sparrow Wallet.


![Image](assets/fr/18.webp)


Ndasubira nkore uburyo nyene bumwe kuri Trezor One kugira ngo nsozere imiterere ya Multisig.


![Image](assets/fr/19.webp)


Mu miterere yanje ntitwavuze ico kibazo, ariko nimba wipfuza gushira mu Multisig yawe umukono uciye kuri software wallet iri muri Sparrow (hot wallet), gusa ukande kuri buto ya "*New or Imported Software Wallet*".


None ko ibikoresho vyawe vyose vyo gusinya vyinjijwe muri Sparrow Wallet, urashobora gusozera ukurema Multisig ukanda kuri "*Apply*".


![Image](assets/fr/20.webp)


Hitamwo ijambobanga rikomeye kugira ngo ukingire uburyo bwo kwinjira muri Wallet yawe ya Sparrow Wallet. Iri jambobanga rikingira imfunguruzo zawe za bose, amaderesi, ibimenyetso n'amateka y'ibikorwa vyawe kugira ngo ntihagire uwubironka ata burenganzira.


Ntiwibagire kubika iri jambobanga ahantu hafise umutekano, nk'umucungerezi w'amajambobanga, kugira ngo ntuyitakaze.


![Image](assets/fr/21.webp)


## Kubika Wallet ya Multisig


Ubu tuzobika *Output Script Descriptor* ku gikoresho cigenga kandi tuzogumya kopi zayo nyinshi.


*Descriptor* irimwo xpubs zose ziri muri Wallet yawe ya Multisig, hamwe n'inzira z'ugukomoka zakoreshejwe mu kwibonera imfunguruzo. Ibuka ivyo twabonye mu gice ca 1: kugira ngo usubizeho Wallet ya Multisig, utegerezwa kugira **amajambo yose** ya Mnemonic, canke umubare mutoyi gusa usabwa kugira ngo ushike ku rugero rw'umukono. Ariko rero, muri ico gihe ca kabiri, birahambaye kandi kugira **xpubs** z'abasinya babura. *Descriptor* irimwo xpubs zose za Multisig yawe.


Nimba ivyo bitagusobanukiye, wibuke gusa iki: kugira ngo usubizeho Multisig, ukeneye umubare mutoyi w'amajambo ya Mnemonic ku Hardware Wallet imwimwe yakoreshejwe, bivanye n'urugero (kuri jewe: amajambo 2), hamwe na *Descriptor*.


Iyi *Descriptor* ntirimwo imfunguruzo z'ibanga, irimwo gusa iza bose. Ivyo bisigura ko itatanga uburenganzira bwo kuronka amahera. Ntihambaye rero nk'amajambo ya Mnemonic, atanga uburenganzira bwuzuye ku ma bitcoins yawe. Ingorane ijanye na *Descriptor* ni iy'ibanga gusa: mu gihe yacumbagira, uwundi muntu yoshobora kubona ibikorwa vyawe vyose, ariko ntashobora gukoresha amahera yawe.


Ndagusaba cane gukora kopi nyinshi za iyi *Descriptor*, kandi uzigumye hamwe n'igikoresho cose co gusinya kiri kuri Multisig yawe. Nk'akarorero, kuri jewe, ndacapura *Descriptor* ku rupapuro maze ngumya kopi imwe hamwe na Passport, iyindi hamwe na Trezor, n'iyindi hamwe na Ledger. Ndabika kandi iyi *Descriptor* nk'idosiye ya PDF kuri udukoresho dutatu twa USB, akamwe kamwe kabitswe hamwe n'imwe mu hardware wallets. Muri ubwo buryo, ndongereza amahirwe yo kutazotakaza iyi *Descriptor*, kandi ndazi neza ko mfise kopi zibiri (imwe y'umubiri n'iyindi y'ubuhinga bwa none) hamwe n'igikoresho cose.


Wallet yawe ya Multisig imaze kuremwa, Sparrow iraheza ikakuronsa iyi *Descriptor*. Kanda kuri buto ya "*Save PDF...*" kugira ngo uyibike mu buryo bw'inyandiko no mu buryo bwa QR code.


![Image](assets/fr/22.webp)


Hanyuma urashobora gucapura iyi PDF no kuyikoporora ku dukoresho twawe twa USB.


![Image](assets/fr/23.webp)


Passport ikoresha imiterere ya multisig yinjijwe na Sparrow kugira ngo yerekane kandi igenzure amakuru y'imfunguruzo ahambaye mu gihe c'ihuza rya QR n'igikorwa co gusinya. Bika *Descriptor* ukwayo: iguma ihambaye cane kugira ngo usubizeho Wallet nimba umusinya umwe atari ho.


Uretse kubika *Descriptor*, ntiwibagire kwitwararika canecane ukubika amajambo ya Mnemonic y'ibikoresho vyawe vyose vyo gusinya. Nimba uriko uratangura, ndagusaba cane kuraba iyindi nyigisho kugira ngo wige ingene uyabika kandi uyacungera neza:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Imbere y'uko wakira ama bitcoins yawe ya mbere kuri Multisig yawe, **ndagusaba cane gukora ikigeragezo co gusubirana ubusa**. Andika amakuru amwe amwe y'ishimikiro, nka Address ya mbere yo kwakira, hanyuma usubize hasi hardware wallets zawe igihe Wallet ikiri ubusa. Hanyuma, ugerageze gusubizaho Wallet yawe ya Multisig kuri Hardware Wallets ukoresheje impapuro zawe zanditsweko amajambo ya Mnemonic, hanyuma kuri Sparrow ukoresheje *Descriptor*. Suzuma ko Address ya mbere yavuye mu gusubizaho ihuye n'iyo wanditse mu ntango. Nimba ari uko, urashobora kuruhuka wizeye ko impapuro zawe zibitse ari izizigirwa.


Kugira ngo umenye vyinshi ku bijanye n'ingene ukora ikigeragezo co gusubirana, ndagusaba kuraba iyindi nyigisho:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Kwakira ama bitcoins kuri Multisig yawe


Wallet yawe ubu yiteguye kwakira ama bitcoins. Muri Sparrow, kanda ku rubuga rwa "*Receive*".


![Image](assets/fr/30.webp)


Imbere y'uko ukoresha Address yavuye muri Sparrow Wallet, fata umwanya wo kuyigenzura ku gicapo nyene c'ama hardware wallets yawe. Ivyo bizokwemeza ko Address itahinduwe, kandi ko ibikoresho vyawe bifise imfunguruzo z'ibanga zikenewe kugira ngo amahera ajanye na yo akoreshwe. Ivyo birafasha kukwikingira ku bwoko bwinshi bw'ibitero.


Kugira ngo ubikore, kanda kuri "*Display Address*" kugira ngo Address yerekanwe kuri Trezor canke Ledger yawe, iyo ifatanijwe n'umugozi.


![Image](assets/fr/31.webp)


Kuri Passport, hitamwo konti ya multisig maze uhitemwo "*Verify Address*". Capura QR code ya Address yo kwakira yerekanwa na Sparrow. Passport iremeza ku gicapo cayo nimba iyo Address iri muri Wallet ya multisig.


Suzuma ko Address yerekanwa kuri hardware wallet imwimwe ihuye neza n'iyo iri muri Sparrow Wallet. Ni vyiza kubikora imbere gato y'uko usangiza Address uwuriha, kugira ngo umenye neza ko itahinduwe.


Hanyuma urashobora guha "*Label*" iyi Address, kugira ngo yerekane inkomoko y'ama bitcoins yakiriwe. Ni uburyo bwiza bwo gutunganya ukucungera UTXOs zawe.


![Image](assets/fr/34.webp)


Ivyo bimaze kugenzurwa, urashobora gukoresha Address kugira ngo wakire ama bitcoins.


![Image](assets/fr/35.webp)


## Kurungika ama bitcoins ukoresheje Multisig yawe


None ko wakiriye ama Sats yawe ya mbere kuri Wallet yawe ya Multisig, urashobora no kuyakoresha! Muri Sparrow, genda ku rubuga rwa "*Send*" kugira ngo wubake igikorwa gishasha co gucuruza.


![Image](assets/fr/36.webp)


Nimba wipfuza gukoresha *Coin Control*, ni ukuvuga guhitamwo n'ukuboko UTXOs wipfuza gukoresha, genda ku rubuga rwa "*UTXOs*". Hitamwo UTXOs wipfuza gukoresha, hanyuma ukande kuri "*Send Selected*". Uzoshikanwa ubwaco ku rubuga rwa "*Send*", UTXOs zimaze kwuzurizwa.


![Image](assets/fr/37.webp)


Injiza Address y'iyakirwa. Amaderesi menshi arashobora kwongerwako ukanda kuri "*+ Add*".


![Image](assets/fr/38.webp)


Ongerako "*Label*" idondora intumbero y'iri koreshwa ry'amahera, kugira ngo ukurikirana ibikorwa vyawe bitagoranye.


![Image](assets/fr/39.webp)


Injiza amahera azorungikwa kuri Address yatowe.


![Image](assets/fr/40.webp)


Tunganya igipimo c'amafaranga bivanye n'ingene urubuga ruri ubu. Nk'akarorero, raba [Mempool.space](https://Mempool.space/) kugira ngo uhitemwo urugero rw'amafaranga rubereye.


Umaze kugenzura ibipimo vyose vy'igikorwa co gucuruza, kanda kuri "*Create Transaction*".


![Image](assets/fr/41.webp)


Nimba unezerewe na vyose, kanda kuri "*Finalize Transaction for Signing*".


![Image](assets/fr/42.webp)


Munsi y'igicapo, uzobona ko Sparrow iriko irindira imikono 2. Ni ibisanzwe: Wallet ikoreshwa aha ni Multisig 2-of-3.


![Image](assets/fr/43.webp)


Ndatangura kusinya na Passport yanje. Muri Sparrow, kanda kuri "*Show QR*" kugira ngo PSBT (*Partially Signed Bitcoin Transaction*) yerekanwe mu buryo bwa QR codes zinyiganyigana. Kuri Passport, hitamwo konti ya multisig maze uhitemwo "*Sign with QR Code*", hanyuma ucapure QR code yerekanwa na Sparrow.


Ku gicapo ca Hardware Wallet yawe, genzura witonze ibipimo vy'igikorwa co gucuruza: Address y'uwuronka, amahera yoherejwe, n'amafaranga. Igikorwa co gucuruza gimaze kwemezwa, emeza kugira ngo ubandanye ku mukono.


Umaze kwemeza igikorwa co gucuruza, Passport yerekana PSBT yashizweko umukono mu buryo bwa QR codes zinyiganyigana. Muri Sparrow, kanda kuri "*Scan QR*" maze ucapure izo codes ukoresheje kamera yawe. Umukono wa Passport uraheza ukongerwako. Ubu ndakoresha Ledger ku mukono wa kabiri usabwa: ndayifatanya kandi ndayifungura, hanyuma nkanda kuri "*Sign*" muri Sparrow.


![Image](assets/fr/48.webp)


Kanda kuri "*Sign*" iruhande y'izina rya Hardware Wallet yawe.


![Image](assets/fr/49.webp)


Ubwa mbere ukoresheje Ledger yawe kuri iyi Multisig, Sparrow izokusaba kugenzura imfunguruzo za bose zagutse (xpubs) z'abasinyanira. Nk'uko biri kuri Passport, iyi ntambwe irakubuza kusinya mu buhumyi mu nyuma. Kugira ngo wemeze ayo makuru, gereranya xpub yerekanwa ku gicapo ca Ledger n'izo zitangwa n'ayandi hardware wallets yawe.


![Image](assets/fr/50.webp)


Suzuma Address y'uwuronka, amahera yimuwe n'amafaranga y'ugucuruza, hanyuma ushire umukono ku gikorwa co gucuruza.


![Image](assets/fr/51.webp)


Fyonda ku gicapo kugira ngo usinye.


![Image](assets/fr/52.webp)


Sparrow ubu ifise imikono ibiri ikenewe kugira ngo amahera ava muri Wallet ya Multisig afungurwe. Suzuma igikorwa co gucuruza ubugira kwa nyuma, kandi nimba vyose bimeze neza, kanda kuri "*Broadcast Transaction*" kugira ngo ugitangaze ku rubuga.


![Image](assets/fr/53.webp)


Uzosanga ico gikorwa co gucuruza ku rubuga rwa "*Transactions*" rwa Sparrow Wallet.


![Image](assets/fr/54.webp)


Turabipfuriza, ubu urazi ingene ushiraho kandi ukoresha Wallet y'imikono myinshi kuri Sparrow. Nimba iyi nyigisho yakugiriye akamaro, nokwishima cane niwasiga urutoke rw'icatsi hasi. Ntutinye gusangiza iyi nkuru ku mbuga ngendanwa zawe. Urakoze kubisangiza!


Kugira ngo ubandanye imbere, ndagusaba kuraba iyi nyigisho ivuga ku bundi buryo bwo kwongereza umutekano wa Bitcoin Wallet yawe, passphrase BIP39 :


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
