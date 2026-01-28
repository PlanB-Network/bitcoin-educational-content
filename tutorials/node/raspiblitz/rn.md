---
name: RaspiBlitz
description: Inyobora yo gushinga RaspiBlitz yawe
---

![image](assets/cover.webp)


RaspiBlitz ni umuco w’umuravyo (LND na/canke umuco w’ishimikiro) ukorana n’umuco w’umuravyo Bitcoin-Fullnode kuri RaspberryPi (1TB SSD) n’ikigaragaza ciza kugira ngo ushobore gutegura & gukurikirana vyoroshe.


RaspiBlitz ahanini igenewe kwiga ingene wokoresha node yawe bwite yegerejwe i muhira - kuko: Si Node yawe, Si Amategeko yawe. Vumbura & guteza imbere ibidukikije bigenda birakura vya Lightning Network mu kuba igice cavyo cuzuye. Uyubake nk’igice c’amahugurwa canke nk’umugambi wo mu mpera z’umusi wewe nyene.


![video](https://youtu.be/DTHlSPMz3ns)


RASPIBLITZ - Uko wokoresha umuravyo na Bitcoin Full node n'ikiganiro ca BTC


## Inyigisho yo gutegura Raspiblitz ya Parman


Raspiblitz ni uburyo bwiza cane bwo gukoresha Bitcoin Node n’ibindi bikoresho bijana. Ndasaba iki n’uruzitiro rwa My Node ku bakoresha benshi (Ugire uruzitiro rubiri rwo gukoresha mu buryo bwiza.) Inyungu imwe ikomeye ni uko uruzitiro rwa Raspiblitz ari “Iporogarama y’Isoko Yuguruye y’Ubuntu”, itandukanye na MyNode canke Umbrel. [Kubera iki ivyo bihambaye? Vlad Costa asigura.] Ushobora kandi gukoresha RaspbiBlitz ukoresheje ubuhinga bwa WiFi aho gukoresha ubuhinga bwa ethernet – ng’aha umurongozi](https://armantheparman.com/wifi-itagira umutwe/) ku bw’ivyo. (Nta buryo mbonye bwo kubikora nkoresheje MyNode).


Ushobora kugura node iteguye ifise mini screen ifatanye, canke ushobora kuyiyubaka wewe nyene (ntukeneye screen).


Urupapuro rwo kuri github ni rwiza cane, ariko birashoboka ko rufise ido n’ido ryinshi ku muntu afise ubumenyi buringaniye. Amabwirizwa yanje azoba ari make cane kandi twizigiye ko azoba yoroshe ko muyakurikiza.


Mu vy’ukuri, iyo nzira isa cane n’iyo gushinga [MyNode node](https://armantheparman.com/mynode-Bitcoin-node-easy-setup-guide-raspberry-pi/) n’iyi Raspberry Pi 4. Igitabu ca Raspiblitz ntikigusaba ko udashobora kugura igikoresho co kugenzura, ariko ntaco wogikeneye. Nta n’iyindi klavye canke imbeba ukeneye. Gusa n’ushike ku rutonde rw’ivyo bikoresho biciye kuri mudasobwa iri kuri iyo nzira nyene, hanyuma ukoreshe itegeko rya ssh ukoresheje terminal. Ivyo birashoboka kuri Linux/Mac (vyoroshe) kandi bikaba bikomeye cane kuri Windows.


### Intambwe ya 1: Gura ivyo bikoresho.


Ukeneye neza neza ibikoresho nk'ivyo ukeneye kugira ngo ukoreshe node ya MyNode. Ushobora kugerageza kimwe canke ikindi, itandukaniro ryonyene ni amakuru ari kuri micro SD card.



- Pi 4, ububiko bwa 4Gb canke 8Gb (4Gb ni vyinshi)
- Inguvu za Raspberry Pi zizwi (Birahambaye cane! Nturonke ivy’urugero, vy’ukuri)
- Ikibazo c’aba Pi. (Igikoresho ca FLIRC ni ciza cane. Igikoresho cose ni igikoresho co gukura ubushuhe kandi ntukeneye umuyaga, ushobora gutera urusaku)
- 32 Gb microSD ikarata (urakeneye imwe, ariko nkeyi zirafasha. )
- Igikoresho co gusoma ikarita y’ububiko (mudasobwa nyinshi ntizizogira aho zishobora gushiramwo ikarita ya microSD).
- Inyuma SSD 1Tb Hard umuduga.
- Umugozi wa ethernet (wo gufatanya na router yo muhira yawe).


Ntukeneye ikigenzura (canke klavye canke imbeba)


Iciyumviro: Iyi ni umuduga wa Hard utari wo: Iyi ni umuduga wa Hard wo hanze ushobora gutwara. Si SSD. SSD ni ikintu gihambaye cane. Ni co gituma ari gito (Igiciro mu AUD)


![image](assets/1.webp)


Ubu ni bwo bwoko bwiza bwo kuronka:


![image](assets/2.webp)


Ibi biranyaruka, ariko birazimvye bidakenewe:


![image](assets/3.webp)


### Intambwe ya 2: Gukuraho ishusho ya Raspiblitz


Ja kuri [urubuga rwa github rwa Raspiblitz](https://github.com/rootzoll/raspiblitz), maze urondere “ishusho yo gukuraho” urubuga:


![image](assets/4.webp)


Sha-256 Hash y’iyo dosiye yavanwe iraboneka ku rubuga. Bizohinduka uko bigenda birahindurwa. Ntimutahura ico ivyo bivuga, murakwiye, ni co gituma nanditse [uburongozi mushobora gusoma hano.](https://armantheparman.com/gpg/)


![image](assets/5.webp)


### Intambwe ya 3: Suzuma ishusho


Imbere yo gukomeza, nimba utazi inzira yawe yo gukikuza dosiye ku murongo w’amabwirizwa, biroroshe kwiga, kandi ukwiye kubimenya.


Aha ni [videwo y’ingirakamaro kuri Linux, ariko ikoreshwa kuri Mac](urutonde rw’ibintu) na yo nyene.


Ku madirisha, ng’iyi [inyigisho yoroshe](v=MBBWVgE0ewk&t=1s).


_UPDATE: pgp/gpg kugenzura ubu biraboneka. Uzokenera urufunguzo rwa bose rwa Openoms. [Aha](http://parman.org/ushobora gukuraho/openoms.txt) ni (ushobora gukenera uburyo bwo kwihisha kugira ngo urubuga rukore – http, atari https)_


Mac/Linux


Rindira ko dosiye iheza gukurwako (birahambaye!), hanyuma ufise terminal yuguruye, ugende aho wakuye dosiye, hanyuma wandike iri tegeko:

```bash
shasum -a 256 xxxxxxxxxxxxxx
```


aho `xxxxxxxxxxxxxx` ari izina rya dosiye uherutse gukuraho. Niba utari mu bubiko aho iyo dosiye iri, utegerezwa kwandika inzira yuzuye.


Iyo orodinateri irazirikana amasegonda 20 canke arenga. Suzuma ko hashfile y’isohoka ihuye n’iyo yakuwe ku rubuga mu ntambwe ibanza. Nimba ari kimwe, urashobora gukomeza.

Amadirisha


Gufungura urutonde rw'itegeko maze ugende aho dosiye yavanywe, hanyuma wandike iri tegeko:


```bash
certUtil -hashfile xxxxxxxxxxxxxxx SHA256
```


aho `xxxxxxxxxxxxxx` ari izina rya dosiye uherutse gukuraho. Niba utari mu muyobozi aho iyo dosiye iri, utegerezwa kwandika inzira yuzuye.


Iyo orodinateri irazirikana amasegonda 20 canke arenga. Suzuma ko hashfile y’isohoka ihuye n’iyo yakuwe ku rubuga mu ntambwe ibanza. Nimba ari kimwe, urashobora gukomeza.


### Intambwe ya 4: Flash ikarita SD


Ushobora gukoresha igikoresho ca Balena kugira ngo ubikore. [Uyikure hano](ku rubuga rwa interineti).


Etcher ni umuntu yisigura gukoresha. Injira ikarita yawe ya micro SD hanyuma ushireko porogarama ya Raspiblitz (dosiye .img) kuri iyo karita.


![image](assets/6.webp)


![image](assets/7.webp)


![image](assets/8.webp)


![image](assets/9.webp)


Iyo bimaze gukorwa, iyo drive ntiba igishobora gusomwa. Ushobora kuronka ikosa riva kuri sisitemu ikoresha, kandi umuduga ukwiye kuzimangana kuri desktop. Kura iyo karata.


### Intambwe ya 5: Shiraho Pi maze winjize ikarita SD


Ibice (ikibazo ntivyerekanwa):


![image](assets/10.webp)


![image](assets/11.webp)


Huza umugozi wa ethernet, n’umugozi wa USB wa Hard (nta nguvu iracariho). Irinde gufatanya n’ibikoresho vya USB vy’ibara ry’ubururu biri hagati. Ni USB 3. Koresha port ya USB 2, naho nyene iyo drive yoba ishobora gukoresha USB 3 (ishobora kwizigirwa cane).


![image](assets/12.webp)


Ikarata ya micro SD ija hano:


![image](assets/13.webp)


Ubwanyuma, huza ubushobozi:


![image](assets/14.webp)


### Intambwe ya 6: Rondera IP Address ya Pi


Ntiwigera ukenera igikoresho co kugenzura gifise Raspiblitz. Ariko rero, urakeneye iyindi mudasobwa iri ku rubuga rwo muhira. Nimba Pi yawe idahuye na ethernet, kandi ushaka kwizigira WiFi, kuronka IP bisaba ubuhinga bumwe bumwe bwo gukoresha mudasobwa. Ntashobora kugufasha, mbabarira. Ukeneye uruja n’uruza rwa ethernet. (Ikibazo kiva ku gukenera gushika ku moniteur n’ivyo gukoresha kugira ngo ushobore gufatanya WiFi no kwinjiza ijambo banga.)


Suzuma router yawe, kugira ubone urutonde rw'ama IP yose y'ibikoresho vyose bihuye.


Nanditse 192.168.0.1 muri Mucukumbuzi (amabwirizwa yaje na router yanje), ndinjira, maze ndashobora kubona igikoresho canje gifise IP 192.168.0.191. Iyumvire ko izo IP addresses zitaboneka ku mugaragaro kuri internet (zibanza guca kuri router), ni ibimenyetso gusa vy’ibikoresho biri ku rubuga rwawe rwo muhira.


Kuronka IP ni ikintu gihambaye cane.


**Iciyumviro:** ushobora gukoresha terminal iri ku mashini ya Mac canke Linux kugira uronke IP Address y’ibikoresho vyose bifatanye na Ethernet ku rubuga rwo muhira ukoresheje itegeko “arp -a”. Ivyo usohora si vyiza nk’ivyo router izokwerekana, ariko amakuru yose ukeneye arahari. Niba bitagaragara neza ko ari Pi, gerageza n’amakosa.


### Intambwe ya 7: SSH muri Pi


Ibuka gushiramwo SD card muri Pi imbere yo kuyifungura. Rindira iminota mikeyi, hanyuma ku yindi Linux/Mac, ufungure terminal.


Ku Mac/Linux, mu bwoko bw'iherezo:


```bash
ssh admin@You_Pi's_IP_address
```


Ku Windows, uzokenera gushiramwo [putty](http://putty.org/) kugira ngo ssh muri Pi. Andika itegeko rimwe n’iryo hejuru.


Igihe ca mbere ukora ibi, canke igihe cose uhinduye OS ya Pi mu guhindura ikarita SD, ushobora canke ntushobora kuronka iri kosa...


![image](assets/15.webp)


Uburyo bwo kubikosora ni ukuja aho dosiye “known_hosts” iri (irakubwira mu butumwa bw’ikosa), hanyuma ukayifuta. Itegeko ni "rm izwi_abashitsi"


Hanyuma, usubiremwo itegeko rya ssh kugira winjire. Ivyo bizoshika...


![image](assets/16.webp)


Andika ego (ijambo ryuzuye) kugira ngo ukomeze.


Nivyaba vyiza, uzosabwa ijambobanga. Ivyo si ivya mudasobwa yawe, ahubwo ni ivya raspiblitz. Ijambobanga rusangi ni “raspiblitz”, kandi uzorihindura mu nyuma. Idirisha ry’i terminal rizohinduka ubururu kandi uzoba ufise amahitamwo nk’aya kera ya DOS. Kugendagenda ukoresheje imfunguruzo z'umwampi canke imbeba.


![image](assets/17.webp)


Kurikiza ivyo usabwa, ushireho amajambo y’ibanga yawe, hanyuma izomenya umuduga wawe wa Hard maze iguhe uburenganzira bwo kuyihindura iyo bikenewe.


Hanyuma uzobazwa nimba ushaka gukopa amakuru ya Blockchain mu yindi nzira canke ukayasubiramwo. Kuyikopa ni inzira yo kwiga kandi amabwirizwa ni meza cane, kandi ni vyiza kuguma ufise....


![image](assets/18.webp)


Uburyo bworoshe ariko bugenda buhoro ni ugukuraho uruhererekane rwose kuva mu ntango...


![image](assets/19.webp)


Ivyanditswe vyinshi bizoca ibibatsi ku mugaragaro w'ibarabara. Ushobora kuyifata nk’uko ari uburyo bwo gukuraho Blockchain, ariko bisa n’uko, kuri jewe, itanga urufunguzo rw’ibanga rwo guhanahana amakuru.


Hanyuma amahitamwo y’umuravyo araboneka.


![image](assets/20.webp)


Kora ijambobanga rishasha ryo gufunga urumuri rwawe Wallet, hanyuma Wallet nshasha izoremwa kandi uzohabwa amajambo 24 yo kwandika...


![image](assets/21.webp)


Niwitwararike ko uvyandika kandi ukabigumya neza. Numvise umuntu umwe ataco akora kuko atari afise umugambi wo gukoresha imiravyo, ariko haciye umwaka aca afata ingingo yo kuyikoresha, aca afungura imirongo. Maze abona ko amajambo yiwe ataco yari afise, kandi ndibuka ko bitashoboka ko yongera gukura ayo majambo muri ico gikoresho, yategerezwa gufunga imihora yiwe yose agasubira gutangura. Yaracitse intege, ariko abandi boshobora kutagira amahirwe nk’ayo.


Ivyo biheze, iminota mikeyi y’ivyanditswe iramanuka mw’idirisha ry’ibarabara. None…


![image](assets/22.webp)


Uzosohoka mu gihe ca ssh. Subira winjire, ubu n’ijambobanga ryawe rishasha, ijambobanga A. Uzokwinjira uzosabwa ijambobanga C kugira ngo ufungure umuravyo wawe Wallet.


None rero turindiriye. Turabonana mu ndwi 2. Ushobora gufunga terminal, ntaco ikora kuri Pi, ni idirisha ry’itumanaho gusa.


![image](assets/23.webp)


Nimba kubera imvo iyo ari yo yose, ushaka gufunga Pi imbere y’uko Blockchain iheza gukuraho, ivyo ni vyiza igihe cose ubikoze neza. Blockchain izobandanya gukura aho yahagaze umaze gusubira gufatanya.


Kanda CTRL+c kugira ngo usohoke mu gicapo c'ubururu. Uzoba uriko uraronka urubuga rwa Linux rwa Pi. Aha ushobora kwandika “menu” ifungura igicapo gikurikira, hanyuma uvuye ng’aho ushobora kuzimya Pi.


![image](assets/24.webp)


IMPERUKA y'uburongozi


Rero kuva ubu node yawe si yiteguye kugenda. Niba ugifasha kurondera ubundi buryo, raba github kugira ngo ubone inyigisho nyinshi n'ubuyobozi https://github.com/raspiblitz/raspiblitz#inyandiko-ziranga