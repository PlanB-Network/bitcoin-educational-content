---
name: Igitangaza DIY
description: Ubuyobozi bwo gutegura Spectre DIY
---

![cover](assets/cover.webp)


## Igitangaza-DIY


> Abanyacypherpunk bandika kode. Turazi ko umuntu ategerezwa kwandika porogarama kugira ngo arwanire ubuzima bwite, kandi ko tutashobora kuronka ubuzima bwite kiretse twese tuburonse, turaza kuvyandika.

*Ikete rya Cypherpunk - Eric Hughes - 9 Ntwarante 1993*


Iciyumviro c’uwo mugambi ni ugukora igikoresho citwa hardware wallet kivuye mu bihimba bitari ku ruhande.

Naho dufise urubaho rwo kwagura rushira vyose mu buryo bwiza kandi rukagufasha kwirinda gutera ivyatsi, tuzobandanya gushigikira no kubungabunga uguhuza n’ibihimba bisanzwe.


![image](assets/fr/01.webp)


Turashaka kandi ko umugambi uguma uhinduka ku buryo ushobora gukora ku bindi bice vyose ata mpinduka nyinshi. Kumbure ushaka gukora hardware wallet ku nyubakwa itandukanye (RISC-V?), ufise modem y’amajwi nk’umuhora wo guhanahana amakuru - ushobora kubikora. Bishobora kuba vyoroshe kwongerako canke guhindura imikorere ya Spectre kandi tukagerageza gukuraho ibice vy’ubwenge uko dushoboye kwose.


QR codes ni uburyo busanzwe Spectre ikoresha kugira ngo ivugane n’uwayikiriye. QR codes ni nziza cane kandi zituma uwuzikoresha ashobora kugenzura ugutanga amakuru - QR code yose irafise ubushobozi buke cane kandi uguhanahana amakuru bibera mu buryo bumwe. Kandi irafise airgapped - ntukeneye gufatanya wallet na mudasobwa igihe cose.


Ku bijanye n’ububiko bw’amabanga dushigikira uburyo bw’ububiko bw’amabanga (wallet yibagirwa amabanga yose iyo izimye), uburyo bw’ububiko bw’amabanga (ububiko bw’amabanga mu flash y’umugenzuzi w’ikoreshwa) n’ugushiramwo secure element biriko biraza vuba.


Ico twibandako cane ni ugushiraho amasinya menshi n’ibindi bikoresho, ariko wallet irashobora kandi gukora nk’umusinya umwe. Turagerageza kubigira bihuye na Bitcoin Core aho dushobora - PSBT ku bikorwa bitagira umukono, wallet ibisobanuro ku kwinjiza/gusohora ama wallets multisig. Kugira ngo tuvugane na Bitcoin Core mu buryo bworoshe turiko turakora kandi kuri [app ya Specter Desktop] - umukozi mutoyi w’ibara ry’agahama avugana n’urudodo rwawe rwa Bitcoin Core.


Ivyinshi muri firmware vyanditswe muri MicroPython bituma code yoroha gusuzuma no guhindura. Dukoresha ububiko bw’ibitabu buva kuri Bitcoin Core ku bijanye n’imibare y’imirongo y’uruzitiro n’ububiko bw’ibitabu [LittlevGL] (https://lvgl.io/) ku bijanye n’ubuhinga bwa GUI.


## Ukwiyamiriza


Uwo mugambi warakuze cane, ku buryo urugero rw’umutekano wa Spectre-DIY ubu rugereranywa n’ibikoresho vy’ubudandaji biri kw’isoko. Twarashizeho bootloader itekanye igenzura ivyagezwe vya firmware, kugira ngo ushobore kwizigira ko firmware yashizweko umukono gusa ari yo ishobora gushirwa ku gikoresho inyuma yo gutegura ubwa mbere. Ariko rero, bitandukanye n’ibikoresho vy’ubudandaji vyo gusinya, bootloader itegerezwa gushirwako n’uwuyikoresha kandi ntishirwa mu ruganda rw’uwugurisha ibikoresho. Gutyo, nushire umutima cane mu gihe co gushiramwo porogarama y’intango kandi urabe neza ko wasuzumye imikono ya PGP kandi ushireko porogarama y’ivyuma ukoresheje mudasobwa itekanye.


Iyo hari ikintu kitagenda neza fungura ikibazo hano canke ubaze ikibazo muri [umugwi wacu wa Telegram](https://t.me/+VEinVSYkW5TUl5Ai).


## Urutonde rw'ibigurishwa vya Spectre-DIY


Aha turadondora ivyo wogura, kandi mu gukoranya igice gikurikira turasigura ingene wobishira hamwe n’ibimenyetso bikeyi ku bijanye n’urubaho - ama power jumpers, ama ports ya USB n’ibindi.


### Urubaho rw'ubuvumbuzi


Igice nyamukuru c'igikoresho ni urubaho rw'abahinguzi:



- Igikoresho co gutegura STM32F469I-DISCO (ni ukuvuga kuva kuri [Imbeba](Ibisobanuro vy'Ibicuruzwa/STMicroElectronics/STM32F469I-DISCO?qs=kWQV1gtkNndotCjy2DKZ4w==) canke [Ikifunguzo c'Igikoresho] (Igikoresho-c'Igikoresho/Igikoresho c'Ivy'Ikoranabuhanga/STM32F469I-DISCO/497-15990-ND/5428811))
- Umugozi muto**USB
- Umugozi wa MicroUSB usanzwe wo kuvugana kuri USB


Ni ubusabe ariko ni vyiza:


- [Igikoresho co gupima kode ya QR ya Waveshare] (httm) gifise imitwe miremire y'ibipimo nk'ivyo [ivyo] (ivyo] canke [ivyo](ivyo] kugira ngo bihuze igikoresho co gupima n’urubaho (imitwe 4 y’amapin irakenewe).


Ubu turiko turakora ku rubaho rwo kwagura rurimwo ahantu ho gushiramwo ikarita y’ubwenge, igikoresho co gupima kode ya QR, bateri n’igikapu co gucapura 3d, ariko nta gice nyamukuru kirimwo — urubaho rwo kuvumbura ukeneye gusaba ukwaco. Ubwo buryo igitero c’uruhererekane rw’ibikoresho n’ubu ntikiri ikibazo kuko ibihimba bihambaye vy’umutekano bigurishwa mu maduka y’ubuhinga bwa none.


Ushobora gutangura gukoresha Spectre naho ata bindi bihimba vy’inyongera, ariko uzoshobora kuvugana na yo kuri USB canke ku nzira y’ikarata SD yubatswemwo. Gukoresha Spectre kuri USB bisigura ko idafise airgapped rero utakaza umutungo w’umutekano uhambaye.


### Igikoresho co gupima QR


Ku scanner ya QR code ufise uburyo bwinshi bwo kubikora.


**Ihitamwo rya 1. Ni vyiza.** Igikoresho ciza cane co gupima kiva kuri Waveshare (40$)


- uzokenera kurondera uburyo bwo kugitera neza, kumbure ukoreshe ubwoko bumwe bw’ingabo ya Arduino Prototype n’urudodo rw’inkoko.


Nta gutera ivyatsi bisabwa, ariko iyo ufise ubuhinga bwo gutera ivyatsi urashobora gutuma wallet igenda neza ;)


**Ihitamwo rya 2.** Scanner nziza cane ya Mikroe ariko irazimvye cane (150$):


[Fyonda kuri kode y'uruzitiro] (kanda kuri kode y'uruzitiro) + [Igikoresho co guhindura]


**Ihitamwo rya 3.** Iyindi scanner ya QR yose


Ushobora gusanga ama scanners atari make mu Bushinwa. Uburyo bwabo kenshi si bwinshi gutyo, ariko urashobora gufata akaryo. Kumbure mbere na ESPcamera yokora ako kazi. Ukeneye gusa gufatanya ubushobozi, UART (pins D0 na D1), no gutera kuri D5.


**Ihitamwo rya 4.** Nta scanner.


Hanyuma ushobora gukoresha Spectre gusa ufise ikarita ya USB / SD.


Keretse wubatse igice cawe co guhanahana amakuru gikoresha ikindi kintu aho gukoresha ama code ya QR - audiomodem, bluetooth canke ikindi cose. Igihe nyene bishobora gutera no kohereza amakuru kuri serial ushobora gukora ivyo ushaka vyose.


### Ibice vy'amahitamwo


Iyo wongeyeko aka powerbank gatoyi canke bateri & chargeur/booster y’amashanyarazi, wallet yawe iraheza igaca yikorera ;)



## Ikoraniro rya Spectre-DIY



![video](https://youtu.be/1H7FqG_FmCw)


### Guhuza igikoresho co gupima kode ya Waveshare


Porogarama ya wallet izogutunganya iyo scanner ku gihe uyikoresha ubwa mbere, rero nta gutunganya mbere n’amaboko bisabwa.


Ehe ingene ufatanya scanner n'urubaho:


![image](assets/fr/02.webp)


Kugira ngo bigufashe ushobora kugura ingabo ya Arduino Protype no kuyishirako vyose (i.e. [iyi] (i.e. [iyi])


### Uburongozi bw'inguvu


Ku ruhande rwo hejuru rw’urubaho hariho igisimbuka gisobanura aho ruzotwara ububasha. Ushobora guhindura aho umusimbuzi ari ugahitamwo inkomoko y’ububasha kugira ngo ibe imwe mu nzira za USB canke pin ya VIN maze ugafatanya bateri y’inyuma ng’aho (ikwiye kuba 5V).


### Uruzitiro rwa DIY


Raba [ibiziga](https://github.com/iterambere ry'ubuhinga/igiti/umukuru/inyandiko/ibiziga) dosiye.


### Nimube abarema!


Koranya Spectre-DIY yawe maze utwoherereze amafoto (ukore ubusabe bwo gukurura canke utwandikire).


Raba [Igishushanyo] (https://github.com/cryptoadvance/specter-diy/blob/master/inyandiko/amafoto/inzu y'ibishushanyo/README.md) n'Ibishushanyo vyakoranijwe n'abanyagihugu!




## Gushiramwo kode yashizwe hamwe


Na bootloader itekanye, gushiramwo mbere y’ivyo bikoresho biratandukanye gatoyi. Guhindura ibintu biroroshe kandi ntibisaba gufatanya hardware wallet na mudasobwa.


![video](https://youtu.be/eF4cgK_L6T4)


### Gukayangana porogaramu y'intango


**Iciyumviro** Niba udashaka gukoresha ama binaries avuye mu bisohotse, reba [inyandiko z'ivyuma] (https://github.com/cryptoadvance/spectre-bootloader/blob/master/doc/selfsigned.md) zisigura ingene wozikoranya no kuzitunganya kugira ngo ukoreshe stead y'imfunguruzo zacu za bose mu.



- Niba uriko urasubiramwo uhereye ku verisiyo ziri munsi ya `1.4.0` canke uriko urashiramwo porogaramu nkuru ku ncuro ya mbere, koresha `porogaramu_y'intango_<verisiyo>.bin` kuva kuri [ibisohotse](https://github.com/cryptoadvance/specter-diy/ibisohotse) kuri paji.
 - Genzura umukono wa dosiye `sha256.signed.txt` ku [urufunguzo rwa PGP rwa Stepan]
 - Genzura hash ya `intango_ya porogaramu_<verisiyo>.bin` ku hash ibitswe muri `sha256.signed.txt`
- Niba uriko urasubiramwo uhereye ku gikoresho co gufungura ubusa canke ubona ubutumwa bw'ikosa ry'igikoresho co gufungura ko porogarama idakora, raba igice gikurikira - Igikoresho ca Spectre gifise umukono.
- Raba neza ko umusimbuzi w'ububasha bw'urubaho rwawe rwo kuvumbura ari ku kibanza ca STLK
- Huza urubaho rwo kuvumbura na mudasobwa yawe biciye ku nzira ya **miniUSB** iri hejuru y’urubaho.
    - Igipande gikwiye kugaragara nk'idisiki ishobora gukurwaho yitwa `DIS_F469NI`.
- Kopa dosiye `intango_ya mbere_<verisiyo>.bin` mu muzi wa dosiye `DIS_F469NI`.
- Iyo board irangije gucapura firmware board izosubira kwisubirako maze isubire gutangura ku bootloader. Bootloader izosuzuma porogarama y’imbere maze ifungure muri porogarama nyamukuru. Niwabona ubutumwa bw'ikosa ko ata firmware ibonetse - kurikiza amabwirizwa yo guhindura maze ushireko firmware biciye ku ikarita ya SD.
- Ubu ushobora guhindura igikoresho co gusimbuka aho ushaka maze ugatanga amashanyarazi ku rubaho ukoresheje powerbank canke kuri bateri.


Gucapura porogaramu ya mbere biciye mu gukopa-gushiramwo dosiye `.bin` rimwe na rimwe birananirwa - kenshi kubera umugozi, canke iyo uhuje igikoresho biciye ku nzira ya USB. Muri ivyo ushobora kugerageza incuro nkeyi (mu bisanzwe bikora mu kugerageza 2-3).


Iyo inaniwe igihe cose ushobora gukoresha igikoresho c’inkomoko yuguruye. Uyishiremwo maze wandike mu nzira yawe: `st-flash wandike <inzira/ku/intango_y'umuyagankuba.bin> 0x8000000`. Akenshi ikora cane kuruta iyo kwizigirwa.


### Kuvugurura porogaramu



- Gukuraho `ivugurura_<version>.bin` mu [bisohotse](https://github.com/iterambere ry'ibanga/ibisohotse-diy/ibisohotse).
- Kopa iyi binaire ku muzi w'ikarata SD (ifise ubuhinga bwa FAT, 32 GB max)
 - Raba neza ko dosiye imwe gusa `specter_upgrade***.bin` iri mu bubiko bw'umuzi
- Injiza ikarita SD mu kibanza ca SD c'urubaho rwo kuvumbura maze ushire ubushobozi ku rubaho
- Bootloader izoguca flash firmware kandi izokumenyesha iyo irangiye.
- Gusubira gufungura urubaho - uzobona interface ya Spectre-DIY ubu, izogusaba guhitamwo kode yawe ya PIN


Igihe cose igisohoka gishasha kizosohoka, ushire `specter_upgrade_<version>.bin` mu bisohotse, ugishire ku ikarita SD maze ushire hejuru igikoresho nk’uko vyari mu ntambwe iheze. Bootloader izokora vyose kugira ngo firmware yashizweko umukono gusa ishobora gushirwa ku rubaho.


### Uko womenya verisiyo ya porogaramu


Genda kuri `Ivyagezwe vy'igikoresho` - bizokwerekana inomero ya verisiyo iri munsi y'umutwe w'igicapo.


## Koresha Igitangaza-DIY wallet



![video](https://youtu.be/Oysg-hhBusc)



![video](https://youtu.be/XfMr7B_uUIk)



![video](https://youtu.be/BzBlh_knIww)



## Umutekano wa Spectre-DIY


### Ibikoresho


Iyerekanwa rigenzurwa n'ikoreshwa rya MCU.


Ugushiramwo ibintu bitekanye ntibirashika - muri iki gihe amabanga na yo arabikwa kuri MCU nyamukuru. Ariko ushobora gukoresha wallet utabitse ibanga - ukeneye kwinjiza ijambo ryawe ryo gukira igihe cose. Ni kuki wokwibuka passphrase ndende nimba ushobora kwibuka mnemonic yose?


Igikoresho gikoresha umuco wo hanze kugira ngo kibike amadosiye amwamwe (QSPI), ariko amadosiye yose y’abakoresha ashirwako umukono na wallet kandi agasuzumwa iyo ashizwemwo.


Ivyo gukora scanning ya QR biri ku gikoresho gitandukanye ku buryo amashusho yose akora hanze ya MCU ihambaye cane. Muri iki gihe USB na SD card biracari bicungiwe na MCU nyamukuru, rero ntukoreshe SD card na USB nimba ushaka kugabanya uburebure bw’igitero.


### Uburinzi bwa PIN (ukwemeza umukoresha)


Mu gihe c’ugutangura kwa mbere ibanga ridasanzwe riravuka kuri MCU nyamukuru. Iryo banga rituma ushobora kugenzura ko igikoresho kitasubirijwe n’ikindi kibi - iyo winjije kode ya PIN ubona urutonde rw’amajambo azoguma ari uko nyene igihe iryo banga ririho.


Kode yawe ya PIN hamwe n’iryo banga ridasanzwe bikoreshwa mu generate urufunguzo rwo gukuraho urufunguzo rwawe rwa Bitcoin (niba uzibitse). Rero iyo uwo muterabwoba ashobora guca ku ruhande rwa PIN, decryption izoguma inanirwa.


Iyo warafunze firmware (TODO: add instructions link here) izofunga neza ibanga na ryo nyene, rero iyo uwugutera flash firmware itandukanye ku board ibanga rirazimangana kandi uzoshobora kurimenya iyo utanguye kwinjiza PIN code - urutonde rw’amajambo ruzoba rutandukanye.


### Uruvyaro rw'ijambo ryo gukira


Ivyo ni bimwe mu bice bihambaye cane vya wallet - ku generate urufunguzo ata nkomanzi. Kugira ngo ivyo tubikore neza dukoresha inkomoko nyinshi z’uburemere bw’ibintu:



- TRNG y’umugenzuzi w’ibintu bitobito. Ivy’umutungo, vyemewe kandi birashoboka ko ari vyiza ariko ntituvyizigira
- Igikoresho gikorako. Igihe cose ukoze ku gicapo dupima aho uri n’igihe ico gikorwa cabaye (mu bimenyetso vya microcontroller ku 180MHz).
- Mikoro yubatswemwo - ntabwo irashika. Ico gipande gifise amamikro abiri, rero hardware wallet irashobora kukwumviriza no kuguvanga muri ayo makuru mu kidengeri c’uburemere.


Ivyo vyose bica bihurizwa hamwe bikahindurwa ijambo ryawe ryo gukira. Entropie ivamwo yama ari nziza kuruta iyo ari yo yose mu masoko y’umuntu ku giti ciwe.


### Urugero rwo hejuru rw'ubwenge - amasakoshi


Spectre ikora nk’ububiko bw’urufunguzo. Ifise imfunguruzo z’ibanga za HD zishobora gushirwa mu bipapuro vy’amahera. Ama wallet asobanurwa n’abayadondora. Turashigikiye miniscript na yo nyene.


wallet yose ni iy’urubuga runaka. Ivyo bisigura ko iyo wazanye wallet kuri `testnet` ntizoboneka kuri `mainnet` canke `regtest` - ukeneye guhindukira kuri uru rubuga maze ukazana wallet ukwayo.


### Igenzura ry'ibikorwa


Amategeko akurikira arakora ku bikorwa wallet izoshirako umukono:



- iyo habonetse ibintu bivanze biva mu bikoresho bitandukanye, uwubikoresha aragabishwa ([igitero](https://blog.trezor.io/ibisobanuro-vy’ikibazo-co-guhindura-aderesi-n’ingene-bigabanywa-6370ad73ed2a))
- guhindura ibisohoka vyerekana izina rya wallet boherezwa kuri
- kugira ngo ukoreshe multisig canke miniscript ubanza kwinjiza wallet mu kwongerako igisobanuro ca wallet (ku QR, USB canke SD card)


## Abadondora barashigikira


Ivyo vyose bisanzwe bidondora Bitcoin birakora. Uretse ivyo dufise n’ibindi bikeyi:


### Amashami menshi mu bidondora


Kugira ngo tuzigame umwanya mu ma code ya QR twemera kwongerako ibisobanuro bifise amashami menshi mu gihe kimwe. Niba ushaka gukoresha `wpkh(xpub/0/*)` mu kwakira aderesi na `wpkh(xpub/1/*)` mu guhindura aderesi ushobora kubifatanya mu ndondoro imwe: `wpkh(xpub/{0,1}/*)` - wallet izofata `urutonde rwa mbere rw'igice ca` ica kabiri nk’amaderesi y’ihinduka.


Ushobora kandi gusobanura amashami arenga abiri, kandi urutonde rw'amashami rushobora kuba rutandukanye ku ba cosigners batandukanye, rero iyi ndondoro iratangaje cane ariko irafise akamaro:


```
wsh(sortedmulti(2,xpubA/{22,33,44}/*,xpubB/34/*/{1,8,6},pubkey3))
```


Aha ku kwakira aderesi inomero 17 wallet izokoresha inyandiko ivuye kuri `wsh(yatoranijwe (2,xpubA/22/17,xpubB/34/17/1,urufunguzo3))`.


Igisabwa conyene ni uko umubare w’index mu migwi yose uba umwe (3 mu gihe kiri hejuru).


### Ivyakozwe mburabuzi


Niba igisobanuro kirimwo imfunguruzo za bose ariko zidafise ibikomoka ku nyuguti, igikomoka `/{0,1}/*` kizokwongerwa ku mfunguruzo zose zagutse mu gisobanuro. Niba n'imiburiburi imwe muri xpubs ifise inkomoko y'ikimenyetso c'ibara ry'agahama, igisobanuro ntikizohindurwa.


Insobanuro `wpkh(xpub)` izohindurwa `wpkh(xpub/{0,1}/*)`.


### Inyandiko


Spectre ishigikira miniscript, ariko ntishigikira gukoranya politike-ku-miniscript (kuko izimvye cane). Turakora ivyigwa bimwe bimwe ku nyandiko nto, rero inyandiko `B` gusa ni zo zemerewe ku rugero rwo hejuru kandi imvo zose ziri mu nyandiko nto zitegerezwa kuba zifise imiterere hakurikijwe [spec](http://bitcoin.sipa.be/miniscript/).


Ushobora gukoresha [bitcoin.sipa.be](http://bitcoin.sipa.be/miniscript/) ku generate insobanuro iva ku ngingo ngenderwako hanyuma ukayizana muri wallet.


Nk'akarorero, politike "Ndashobora gukoresha ubu, canke mu misi 100 umugore wanje ashobora gukoresha" ishobora guhindurwa ikaja muri wallet nk'uko:


Amategeko: `canke(9@pk(xpubA),na(ya kera(14400),pk(B))` (urufunguzo rwanje rurashoboka incuro 9)


Inyandiko ntoya: `canke_d(pk(xpubA),na_v(v:pkh(xpubB),ya kera(14400)))`


Descriptor: 'wsh(canke_d(pk(xpubA),na_v(v:pkh(xpubB),shaje(14400))))`


Nk'uko hano ata n'imwe dufise y'inyuguti zikomoka ku `/{0,1}/*` zizokwongerwa ku xpubs.



---

Uruhusha rwa MIT


Uburenganzira bw'umuhinguzi (c) 2019 imbere y'igihe


---