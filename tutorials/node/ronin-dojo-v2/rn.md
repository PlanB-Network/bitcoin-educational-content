---
name: RoninDojo v2
description: Gushiramwo urudodo rwawe rwa RoninDojo v2 Bitcoin kuri Raspberry Pi
---
![cover RoninDojo v2](assets/cover.webp)


**IMBURIZO:** Inyuma y'aho abashinze Samourai Wallet bafashwe, ama server yabo bagafatwa kw'igenekerezo rya 24 Ndamukiza, hari ibintu bimwe bimwe vyo muri RoninDojo, nka Whirlpool, bitagikora. Ariko birashoboka ko ivyo bikoresho vyosubira gukoreshwa canke bikagaruka gukoreshwa mu buryo butandukanye mu ndwi ziza. Ikindi, kubera ko kode ya RoninDojo yari yashizwe kuri GitLab ya Samourai, na yo nyene yafashwe, ubu ntibishoboka ko umuntu ayikura kure. Amashirahamwe ya RoninDojo birashoboka ko ariko arakora ku bijanye no gusubira gusohora iyo kode.*


_Turiko turakurikirana cane iterambere ry’uru rubanza hamwe n’iterambere ryerekeye ibikoresho bijana. Nimwizere ko tuzosubiramwo iyi nyigisho uko amakuru mashasha azoboneka._


_Iyi nyigisho itangwa ku ntumbero y'inyigisho n'amakuru gusa. Ntidushigikira canke ngo turemeshe gukoresha ivyo bikoresho mu ntumbero z’ubugizi bwa nabi. Ni inshingano y'ukoresha wese kwubahiriza amategeko ari mu bubasha bwiwe._


---

> Koresha Bitcoin n’ubuzima bwite.

Mu nyigisho iheruka, twari twamaze gusigura uburyo bwo gushiramwo no gukoresha RoninDojo v1. Ariko rero, mu mwaka uheze, amashirahamwe ya RoninDojo yaratanguje verisiyo ya 2 y’ugushirwa mu ngiro kwayo, ivyo bikaba vyatumye habaho ihinduka rikomeye mu bijanye n’ubwubatsi bwa porogarama. Nkako, baravuye mu gutanga Linux Manjaro bafata Debian. Ku bw’ivyo, ntibasubira gutanga ishusho yatunganijwe imbere y’igihe kugira ngo ishire ubwayo kuri Raspberry Pi. Ariko haracariho uburyo bwo gukomeza gushiramwo n’amaboko. Ivyo nivyo nakoresheje ku node yanje bwite, kandi kuva ico gihe, RoninDojo v2 yariko irakora neza cane kuri Raspberry Pi 4 yanje.

https://planb.network/tutorials/node/bitcoin/ronin-dojo-31d96647-029b-43e8-9fb5-95ec5dde72b0

## Ibirimwo:


- RoninDojo ni iki?
- Ni ibihe bikoresho wohitamwo kugira ngo ushiremwo RoninDojo v2?
- Ni gute wokoranya Raspberry Pi 4?
- Ni gute woshira RoninDojo v2 kuri Pi 4?
- Ni gute wokoresha urudodo rwawe rwa RoninDojo v2?


## RoninDojo ni iki?

Dojo mu ntango ni ugushirwa mu ngiro kw’inzira yuzuye ya Bitcoin, ishingiye kuri Bitcoin core, kandi yateguwe n’imigwi ya Samourai Wallet. Uwo muti ushobora gushirwa ku bikoresho vyose. Udakunze ibindi bikoresho vy'ishimikiro, Dojo yarahinduwe neza cane kugira ngo ikoreshe n'ibidukikije vy'ibikorwa vya Android vya Samourai Wallet. Naho RoninDojo, ni igikoresho gikoreshwa mu gufasha gushiramwo no gucunga Dojo, hamwe n’ibindi bikoresho bitandukanye vy’inyongera. Muri make, RoninDojo iratunganya ugushirwa mu ngiro kw’ishimikiro kwa Dojo mu gushiramwo ibikoresho vyinshi vy’inyongera, mu gihe yorohereza ugushiraho n’ugucungera kwayo.


Ronin kandi itanga [umuti w'urudodo mu gasandugu, witwa "*Tanto*"](https://ronindojo.io/ru/ibikoresho), igikoresho gifise RoninDojo kimaze gushirwa kuri sisitemu yakoranijwe n'umugwi wabo. Tanto ni uburyo bwo kwishura, bushobora gushimisha abakunda kwirinda ingorane z’ubuhinga. Ariko kuko source code ya RoninDojo yuguruye, birashoboka kandi ko uyishira ku bikoresho vyawe bwite. Iyi nzira, ishobora gutuma umuntu agira ubutunzi bwinshi, naho biri ukwo, isaba ko habaho ibindi bikoresho, ivyo tuzobivuga muri iyi nyigisho.

RoninDojo ni Dojo, rero iremesha gushiramwo Whirlpool CLI mu buryo bworoshe mu nzira yawe ya Bitcoin kugira ngo ushireho ubumenyi bwiza cane bwa CoinJoin. Na Whirlpool CLI, birashoboka ko ukomeza gukora remix y’ama bitcoins yawe, amasaha 24 ku musi, imisi 7 ku ndwi, ataco usaba ko mudasobwa yawe bwite iguma ifunguye.


Uretse Whirlpool CLI, RoninDojo irimwo ibikoresho bitandukanye vyo kwongereza ubushobozi bwa Dojo yawe. Muri ivyo, igiharuro ca Boltzmann gisesangura urugero rw’ubuzima bwite bw’amahera ukoresha, server ya Electrum iremeza ko ama wallet yawe ya Bitcoin ashobora gufatanya n’uruzitiro rwawe, kandi server ya Mempool iragufasha kubona ivyo ukoresha mu karere, ata makuru asohoka.


Ugereranije n’ibindi bisubizo vy’ibihimba nka Umbrel, RoninDojo yibanze cane ku bisubizo vya On-Chain n’ibikoresho vy’ubuzima bwite. Udakunze Umbrel, RoninDojo ntishigikira gushinga urudodo rwa Lightning canke gushiramwo ibindi bikorwa vy'umuserukira rusangi. Naho RoninDojo itanga ibikoresho bikeyi bishobora gukoreshwa mu buryo bwinshi kuruta Umbrel, irafise ibikorwa vyose vy’ingenzi vyo gucunga igikorwa cawe ca On-Chain.


Niba udakeneye ibikorwa rusangi canke ivyo bijanye na Lightning Network nk’uko bitangwa na Umbrel, kandi uriko urarondera urudodo rworoshe, rudahinduka rufise ibikoresho vy’ingenzi nka Whirlpool canke Mempool, RoninDojo yoshobora kuba umuti mwiza. Naho Umbrel ikunda kuba umukozi mutoyi akora ibikorwa vyinshi vyerekeye Lightning Network n’ubushobozi bwo gukora vyinshi, RoninDojo, bihuye n’ubuhinga bwa Samourai Wallet, yibanda ku bikoresho vy’ishimikiro vy’ubuzima bwite bw’abakoresha.


None ko twamaze gutanga urutonde rwa RoninDojo, reka turabe hamwe ingene twoshiraho iyo node.


## Ni ibihe bikoresho wohitamwo kugira ngo ushiremwo RoninDojo v2?

RoninDojo itanga ishusho yo gushiramwo porogarama yayo ku [RockPro64](https://ronindojo.io/ru/gukuraho). Ariko rero, inyigisho yacu yibanze ku buryo bwo gushiramwo n’amaboko kuri Raspberry Pi 4. Naho Raspberry Pi 5 iherutse gusohoka, kandi iyi nyigisho ikwiye kuba ihuye n’iyi modele nshasha, jewe ubwanje sinari bwaronke akaryo ko kuyigerageza, kandi nta n’inyishu nabonye ivuye mu kibano. Nkimara kuronka Pi 5 n’ibice bihuye, nzosubiramwo iyi nyigisho kugira ngo mumenye. Hagati aho, ndabahimiriza gushira imbere Pi 4, kuko ikora neza cane ku nzira yanje.

Ku ruhande rwanje, nkoresha RoninDojo kuri Raspberry Pi ifise 8 GB ya RAM. Naho bamwe mu bagize umuryango bashoboye kuyikora ku bikoresho bifise 4 GB gusa ya RAM, jewe ubwanje sinarigeze ngerageza iyo configuration. Kubera ko hariho itandukaniro ritoyi ry’igiciro, bisa n’ibibereye guhitamwo verisiyo ya 8 GB RAM. Ivyo bishobora kandi kuba ngirakamaro nimba utegura gusubira gukoresha Raspberry Pi yawe mu bindi bikoresho muri kazoza.

Ni vyiza kumenya ko amashirahamwe ya RoninDojo yatangaje ibibazo kenshi bijanye n’ico kibazo be n’ivyo SSD ikoresha. Nanje ubwanje narahuye n’ivyo bibazo. **Ni co gituma, birakenewe cane ko wirinda ibikoresho bifise umugozi wa USB wa SSD ya node yawe.** Ahubwo, uhitemwo ikarita yo kwagura ububiko yagenewe Raspberry Pi yawe:


![storage expansion card RPI4](assets/notext/1.webp)


Kugira ngo ubike Bitcoin Blockchain, uzokenera SSD ihuye n’ikarata yo kwagura ububiko wahisemwo. Ubu (Ruhuhuma 2024), turi mu gihe c’ihinduka. Bitegekanijwe ko, mu mezi make, amadisike ya 1 TB atazoba agihagije kugira ngo ashobore gushiramwo ubunini bugenda burakura bwa Blockchain, cane cane uzirikanye ibikorwa bitandukanye utegura gushiramwo mu node yawe. Bamwe rero barasaba ko umuntu yoshiramwo SSD y’ama 2 TB kugira ngo agire amahoro yo mu mutima mu gihe kirekire. Ariko rero, kubera ko ibiciro vya SSD bigenda biragabanuka umwaka ku wundi, abandi barasaba ko bokwisunga disiki y’ama TB 1, iyo disiki ikaba ikwiye kuba ihagije mu mwaka umwe canke ibiri, bavuga ko igihe izoba yacitse igihe, igiciro c’ibikoresho vy’ama 2 TB kumbure kizoba caragabanutse. Ihitamwo rero rivana n’ivyo wewe ubwawe ukunda. Niba utegura kuguma ufise RoninDojo yawe igihe kirekire kandi wipfuza kwirinda gukoresha ubuhinga bwose mu myaka iri imbere, uguhitamwo SSD ya 2 TB bisa n’uko ari vyo vy’ubwenge kuruta ibindi vyose, kuko biguha urugero rwiza rwo muri kazoza.


Ikindi, uzokenera utugingo ngengabuzima dutoduto dutandukanye:


- Igikapu gifise umuyaga wo gushiramwo Raspberry Pi yawe n’ikarata yawe yo kwagura ububiko. Ivyuma birimwo ikarita yo kwagura SSD n’igisandugu gihuye biraboneka kuri Internet;
- Intsinga y’amashanyarazi y’i Raspberry Pi yawe;
- Ikarata ya micro SD ifise nibura 16 GB (naho 8 GB yoshobora guhagije mu buryo bw’ubuhinga, itandukaniro ry’igiciro hagati y’ikarata 8 na 16 GB akenshi ntiryahambaye);
- Umugozi wa Ethernet RJ45 wo gukorana n’urubuga.


![node material](assets/notext/2.webp)


## Ni gute wokoranya Raspberry Pi 4?

Iterambere ry’urudodo rwawe rizohinduka bivanye n’ibikoresho wahisemwo, cane cane ubwoko bw’ikibazo. Ariko rero, urutonde rusangi rw’intambwe zo gukurikiza ruguma muri rusangi nk’urwo nyene mw’ikoraniro.

Tangana ushire SSD yawe ku ikarita yo kwagura ububiko, witwararike gufata neza izo nkoko zibiri zifunga inyuma.


![assembly1](assets/notext/3.webp)


Hanyuma ushire Raspberry Pi yawe ku ikarita yo kwagura.


![assembly2](assets/notext/4.webp)


Kandi, ushire umuyaga ku Raspberry Pi.


![assembly3](assets/notext/5.webp)


Huza ibihimba bitandukanye, witwararike gukoresha amapine akwiriye, ushingiye ku gitabu c’ikibazo cawe. Abahinguzi b’ibikoresho akenshi baratanga inyigisho zo kuri videwo kugira ngo bagufashe mu gukoranya. Ku bijanye nanje, mfise ikarata yo kwagura y’inyongera ifise ubuto bwo gufungura/gufunga. Ivyo si ngombwa kugira ngo umuntu akore urudodo rwa Bitcoin. Ahanini ndayikoresha kugira ngo mfise ubuto bw’umuriro.


Niba, nkanje, ufise ikarita yo kwagura ifise ubuto bwo gufungura/gufunga, ntukibagire gushiramwo agace gatoyi k'ugusimbuka "Auto Power On". Ivyo bizotuma node yawe itangura ubwo nyene iyo ifunguwe. Ico gikoresho ni ngirakamaro cane cane iyo umuyagankuba uzimye, kuko kituma node yawe isubira gukora ubwayo, ataco ukoresheje n’amaboko.


![assembly4](assets/notext/6.webp)


Imbere yo kwinjiza ibikoresho vyose mu gitereko, birahambaye ko usuzuma neza ko Raspberry Pi yawe, ikarita yo kwagura ububiko, n’umuyaga bikora neza mu kubifungura.


![assembly5](assets/notext/7.webp)


Ubwa nyuma, shiramwo Raspberry Pi yawe mu kigega cayo. Menya, intambwe izokurikira izosaba kwongerako ikarita ya micro SD mu port ibereye kuri Raspberry Pi. Nimba igisandugu cawe gifise urufunguruzo rugufasha kwinjiza ikarata SD ataco ukeneye kuyifungura (nk’uko biri ku rwanje rwerekanwa ku ifoto), urashobora gukomeza gufunga igisandugu ubu. Ariko rero, nimba ikibazo cawe kidashobora gushika ku nzira ya micro SD, uzokenera kurindira gushika uteguye ikarita ya micro SD kugira ngo uyishiremwo imbere y’uko uheza gukoranya.


![assembly6](assets/notext/8.webp)


## Ni gute woshira RoninDojo v2 kuri Pi 4?


### Intambwe ya 1: Tegura micro SD ishobora gutangura

Uhejeje gukoranya ibikoresho vyawe, intambwe ikurikira ni ugushiramwo RoninDojo. Ku bw’ivyo, tuzotegura ikarita micro SD ishobora gufunguka ivuye kuri mudasobwa yawe, mu kuyiturirako ishusho ya disk ibereye.

Uzokenera gukoresha porogarama ya _**Raspberry Pi Imager**_, yateguwe kugira ngo ushobore gukura, gutunganya no kwandika ubuhinga bwo gukoresha ku ikarita ya micro SD kugira ngo ukoreshe na Raspberry Pi. Tangira ushire iyi porogaramu kuri mudasobwa yawe bwite:


- Ku bwa Ubuntu/Debian:
- Ku Windows: https://ivyo gukuraho.
- Ku bwa Mac: https://ugukuraho.raspberrypi.org/ishusho/ishusho_ya nyuma.dmg


Iyo porogarama imaze gushirwamwo, uyifungure, hanyuma ushire ikarata yawe ya micro SD muri mudasobwa yawe bwite. Kuva ku gishushanyo ca Raspberry Pi Interface, hitamwo `HINDURA OS`:


![choose OS](assets/notext/9.webp)


Ibikurikira, genda kuri `Raspberry Pi OS (ibindi)`:


![choose OS others](assets/notext/10.webp)


Hitamwo uburyo bwo gukoresha bwitwa `Raspberry Pi OS (Iragi, 64-bit) Lite`, bufise `0.3 GB` mu bunini:


![choose OS Legacy Lite](assets/notext/11.webp)


Uhejeje guhitamwo uburyo bwo gukoresha, uzosubira ku rutonde nyamukuru rwa Raspberry Pi Imager. Fyonda kuri `HINDURA UBUBIKO`:


![choose storage](assets/notext/12.webp)


Hitamwo ikarita yawe ya micro SD:


![choose micro sd](assets/notext/13.webp)


Uhejeje guhitamwo uburyo bwo gukoresha n'ikarita ya micro SD, kanda kuri `IBIKURIKIRA`:


![choose next](assets/notext/14.webp)


Idirisha rishasha rizoboneka. Hitamwo `GUHINDURA IVYO GUHINDURA`:


![edit settings](assets/notext/15.webp)


Muri iri dirisha, genda kuri `GENERAL` tab maze ukore ibi bikurikira (bihambaye cane kugira ngo bikore):


- Gushoboza amahitamwo maze ushireho `RoninDojo` nk'izina ry'umushitsi;
- Gushoboza `Shiraho izina ry'ukoresha n'ijambobanga`, winjize `pi` nk'izina ry'ukoresha, uhitemwo ijambobanga, hanyuma wandike aya makuru, nk'uko azokenerwa mu nyuma. Ivyo vyemezo ni ivy’akanya gato kandi bizokurwaho inyuma;
- Guhagarika `Gutegura Wi-Fi`;
- Gukoresha `Set locale settings` maze uhitemwo isaha yawe hamwe n'ubwoko bwa klavye bujanye na mudasobwa yawe;


![general settings](assets/notext/16.webp)


Mu rwego rw'IBIKORESHO, kanda ku gasandugu ka `Gushoboza SSH` hanyuma uhitemwo `Koresha ijambobanga ryo kwemeza`:


![services settings](assets/notext/17.webp)


Kandi, urabe ko mu `AMAHITAMWO`, telemetry idakora:


![options settings](assets/notext/18.webp)


Fyonda kuri `BIKA`:


![settings save](assets/notext/19.webp)

Wemeze ukanda kuri `EGO` kugira utangure gukora ikarita ya micro SD:

![settings yes](assets/notext/20.webp)


Ubutumwa buzokumenyesha ko amakuru yose ari kuri micro SD card azokurwaho. Wemeze ukanda kuri `EGO` kugira utangure igikorwa:


![overwrite micro SD](assets/notext/21.webp)


Rindira gushika iyo porogaramu irangije gutegura ikarita yawe ya micro SD:


![writing micro SD](assets/notext/22.webp)


Iyo ubutumwa bwerekana ko igikorwa carangiye bubonetse, urashobora gukuraho ikarata micro SD kuri mudasobwa yawe:


![writing micro SD completed](assets/notext/23.webp)


### Intambwe ya 2: Uzuza Ikoraniro ry'Imirongo

Ubu ushobora kwinjiza ikarita ya micro SD mu port ibereye ya Raspberry Pi yawe.


![micro SD](assets/notext/24.webp)


Hanyuma ushire Raspberry Pi yawe kuri router yawe ukoresheje umugozi wa Ethernet. Ubwa nyuma, fungura node yawe mu gufatanya umugozi w’amashanyarazi no gukanda buto y’amashanyarazi (niba setup yawe irimwo imwe).


### Intambwe ya 3: Gushinga uruja n'uruza rwa SSH n'uruzitiro

Ubwa mbere, ni ngombwa kurondera IP Address y’urudodo rwawe. Ufise uburenganzira bwo gukoresha igikoresho nka _[Igikoresho co gupima IP](https://www.ip-scanner.com/)_ canke _[Igikoresho co gupima IP giteye imbere](https://angryip.org/)_, canke ugasuzuma ubuyobozi Interface bwa router yawe. IP Address ikwiye kuba iri mu rupapuro `192.168.1.??`. **Ku mategeko yose akurikira, subiriza `[IP]` IP nyayo Address y'uruzitiro rwawe**, (ukuraho ibifunga).


Gutanguza igisagara.


Kugira ngo ukureho urufunguzo rushoboka rusanzwe rufitaniye isano na IP Address y'uruzitiro rwawe, shira mu ngiro itegeko:

`ssh-urufunguzo -R [IP]`.


Ikosa rikurikira iri tegeko si rikomeye; bisigura gusa ko urufunguzo rutari mu rutonde rwawe rw'abashitsi bazwi (ivyo bikaba bishoboka cane). Nk'akarorero, iyo IP y'urudodo rwawe ari `192.168.1.40`, itegeko rihinduka: `ssh-keygen -R 192.168.1.40`.


Ibikurikira, shiraho ubufatanye bwa SSH n'urudodo rwawe mu gushitsa itegeko:

`ssh pi@[IP]`.

Ubutumwa buzoboneka ku bijanye n'ukuri kw'umushitsi: `Ukuri kw'umushitsi '[IP]' ntigushobora gushingwa.` Ivyo vyerekana ko ukuri kw'igikoresho uriko uragerageza kwifatanya naco kudashobora kugenzurwa kubera ukubura urufunguzo rwa bose ruzwi. Igihe uhuye biciye kuri SSH ku mushitsi mushasha ku ncuro ya mbere, ubu butumwa buzokwama buboneka. Utegerezwa kwishura `egome` kugira ngo wongere urufunguzo rwayo rwa bose ku bubiko bwawe, ivyo bizobuza ubu butumwa bwo kugabisha kugaragara mu gihe c'amahuza ya SSH azoza kuri iyi node. Rero, wandike `egome` hanyuma ukande `enter` kugira ngo wemeze.

Uzoca usabwa kwinjiza ijambobanga ryawe, iryo mbere ryashizweho nk'iry'igihe gito mu ntambwe ya 1. Wemeze na `enter`. Uzoheza uhuzwe n'uruzitiro rwawe biciye kuri SSH.


Mu ncamake, ng’aya amabwirizwa yo gushitsa:


- `ssh-urufunguzo -R [IP]`
- 'ssh pi@[IP]`
- 'ego'
- Injira ijambobanga ry’igihe gito maze ushire mu ngiro.


### Intambwe ya 4: Gusubiramwo no kwitegura

Ubu uhuye n'uruzitiro rwawe biciye ku kiganiro ca SSH. Ku nzira yawe, itegeko rigomba kuba: `pi@RoninDojo:~ $`. Kugira ngo utangure, hindura urutonde rw'amapaki ariho maze ushiremwo amavugurura y'amapaki asanzweho n'iri tegeko rikurikira:

`sudo apt ivugurura && sudo apt ivugurura -y`


Ivyo bishasha bimaze kurangira, genda ushiremwo *Git* na *Dialog* ukoresheje itegeko:

`sudo apt gushiramwo ikiganiro ca git -y`


Ibikurikira, ushireho ishami ry'ububiko bwa _RoninOS_ Git ukoresheje:

`sudo git clone --umukuru w'ishami


Gukoresha inyandiko `guhindura-ishusho.sh` n'itegeko:

`cd / guhitamwo / RoninOS / && sudo ./ guhindura-ishusho.sh`


**Ni vyiza kureka inyandiko ikagenda ataco ihagarika kandi ukarindira wihanganye ko igikorwa cayo kirangira**, ivyo bikaba bifata nk’iminota 10. Iyo ubutumwa `Gutegura burarangiye` bubonetse, ushobora kuja ku ntambwe ikurikira.


### Intambwe ya 5: Gutanguza RoninOS

Gutanguza RoninOS n'itegeko:

`uburyo bwa sudo butangura gushinga-gutegura`


Erekana imirongo ya dosiye y'inyandiko n'itegeko:

`umurizo -f /inzu/ronindojo/.ibitabo/gutegura.ibitabo`


Kuri iyi ntambwe, **ni ngombwa kureka RoninOS igatangura no kuyirindira** kugira ngo iheze gukora. Ivyo bifata nk’iminota 40. Igihe `Ivyiyumviro vyose vya RoninDojo birangiye!` bibonetse, ushobora gukomeza ku ntambwe ya 6.


### Intambwe ya 6: Gushika kuri RoninUI no guhindura ivyemezo

Uhejeje gushiramwo, kugira ngo wihuze n’uruzitiro rwawe biciye ku mucukumbuzi, urabe neza ko mudasobwa yawe bwite ihuye n’uruzitiro rwo mu karere rumwe n’uruzitiro rwawe. Niba ukoresha VPN ku mashine yawe, uyizimye mu gihe gito. Kugira ngo ushikire node Interface mu mucukumbuzi wawe, winjize mu murongo wa URL:


- IP Address y'uruzitiro rwawe, nk'akarorero, `192.168.1.??`;
- Canke, wandike `ronindojo.aho hantu`.


Ushitse kuri paji y'intango ya RoninUI, uzosabwa gutangura gutegura. Kugira ngo ubikore, fyonda ku buto `Reka dutangure`.


![lets start](assets/notext/25.webp)


Kuri iyi ntambwe, RoninUI iraguha ijambobanga ryawe `umuzi`. Ni ngombwa ko tuyizigama neza. Ushobora guhitamwo ububiko bw’umubiri, ku mpapuro, canke ukabubika mu [mucungerezi w’ijambobanga]


![root password](assets/notext/26.webp)


Amaze kubika ijambobanga `umuzi`, shira akazu `Nashizeho amakuru y'umukoresha w'umuzi` hanyuma ukande kuri `Bandanya` kugira ngo ukomeze.


![confirm root password](assets/notext/27.webp)


Intambwe ikurikira ni uguhingura ijambobanga ry’ukoresha, rizokoreshwa mu gushika ku rubuga rwa RoninUI Interface no mu gushinga ibiganiro vya SSH n’uruzitiro rwawe. Hitamwo ijambobanga rikomeye maze urabe ko uribika neza. Uzokenera kwinjiza iri jambobanga incuro zibiri imbere yo gukanda kuri `Finish` kugira ngo wemeze. Naho izina ry'ukoresha, birakenewe ko ugumana ihitamwo ry'imbere, `ronindojo`. Niwafata ingingo yo kuyihindura, wibuke guhindura amabwirizwa ari mu ntambwe zikurikira bivanye n’ivyo.


![user credentials](assets/notext/28.webp)


Ivyo bikorwa bimaze kurangira, rindira ko urudodo rwawe rutangura. Uzoca winjira ku rubuga rwa RoninUI Interface. Ugeze hafi y’iherezo ry’ico gikorwa, hasigaye intambwe nkeyi gusa!

![Ronin UI](assets/notext/29.webp)


### Intambwe ya 7: Kuraho ivyemezo vy'igihe gito

Gufungura terminal nshasha kuri mudasobwa yawe bwite maze ushireho ubufatanye bwa SSH n'uruzitiro rwawe ukoresheje itegeko rikurikira:

`SSH umuduga@[IP]`


Niba, nk'akarorero, IP Address y'uruzitiro rwawe ari `192.168.1.40`, itegeko rikwiye rizoba:

`SSH RONIDOJO@192.168.1.40`


Niwaba warahinduye izina ryawe ry'ukoresha mu ntambwe iheze, usubiriza izina ry'ukoresha ry'imbere (`ronindojo`) n'irindi, urabe ko ukoresha iri zina rishasha mw'itegeko. Nk'akarorero, niwahitamwo `planb` nk'izina ry'ukoresha kandi IP Address ni `192.168.1.40`, itegeko ryo kwinjira rizoba:

'Umugambi wa SSH@192.168.1.40`

Uzosabwa kwinjiza ijambobanga ry’ukoresha. Injira hanyuma ukande `enter` kugira ngo wemeze. Uzoca ubona igitabu ca RoninCLI Interface. Koresha imfunguruzo z'umwampi kuri klavye yawe kugira ngo ugende ku mahitamwo ya `Exit RoninDojo` hanyuma ukande `enter` kugira ngo uyihitemwo.

![RoninCLI](assets/notext/30.webp)


Kuri iyi nkuru, uri ku nzira y'uruzitiro rwawe, ufise itegeko risa n'iri: `ronindojo@RoninDojo:~ $`. Kugira ngo ukureho umukoresha w'igihe gito yaremwe mu gihe co gutunganya ikarita ya micro SD, shiramwo itegeko rikurikira hanyuma ukande `enter`:

`sudo umuzimiza --kuraho-inzu pi`


Uzosabwa kwemeza ijambobanga ryawe. Injira maze uyishire mu ngiro ukanda `enter`. Rindira ko igikorwa kirangira, hanyuma ukoreshe itegeko rya `exit` kugira ngo uve mu kibanza.


Urakoze cane! Node yawe ya RoninDojo v2 ubu iratunganijwe kandi yiteguye gukoreshwa. Izotangura IBD yayo (*Gukuraho Igitabo ca Mbere*), ikomeze gukuraho no kugenzura Bitcoin Blockchain mu gitabu ca Genesis. Iyo ntambwe isaba kugarura amafaranga yose ya Bitcoin yakozwe kuva ku wa 3 Nzero 2009, kandi ifata umwanya. Blockchain imaze gukurwako, indexer izoca ibandanya gufata urutonde rw’amakuru. Igihe IBD imara gishobora guhinduka cane. Igikoresho cawe ca RoninDojo kizokora neza iyo iyo nzira irangiriye.


**Nimba uriko urimuka uva ku node ya kera ya RoninDojo v1** ukaja kuri iyi verisiyo nshasha ufise iyi nyigisho mu gihe ugumye SSD imwe, node yawe ikwiye kwibonera ubwayo no gusubira gukoresha amakuru ariho kuri disk, bikagukingira ivy’ugusubira gukora IBD. Muri ivyo, uzokenera gusa kurindira ko urudodo rwawe rusubira gukorana n'amabuye aheruka.


### Intambwe ya 8: "veth gukosora".

Niwahura n'ikibazo na RoninDojo v2 yawe kuri Raspberry Pi, aho inyuma yo gushiramwo ata ngorane, urudodo rwawe ruca rudashobora gushikirwa biciye kuri SSH ariko rugakira inyuma yo gusubira gutangura, rero urakeneye gukurikira iyi ntambwe 8. Ico kibazo gisanzwe gishobora gukosorwa mu buryo bworoshe n'umuti wateguwe n'abanyagihugu: "_". Ukwo gukosora gutoyi kuratorera umuti ubudasiba ivyo bihimba vy’umubiri bica bukwi na bukwi. Ehe ingene wobishira mu ngiro.


Gufungura terminal nshasha kuri mudasobwa yawe bwite maze ushireho ubufatanye bwa SSH n'urudodo rwawe ukoresheje itegeko rikurikira:

`SSH umuduga@[IP]`


Niba, nk'akarorero, IP y'urudodo rwawe Address ari `192.168.1.40`, itegeko rikwiye ryoba:

`SSH RONIDOJO@192.168.1.40`


Uzosabwa kwinjiza ijambobanga ry'ukoresha. Injira hanyuma ukande `enter` kugira ngo wemeze. Uzoca ubona igitabu ca RoninCLI Interface. Koresha imyampi ya klavye yawe kugira ngo ugende ku `Sohoka RoninDojo` hanyuma ukande `enter` kugira ngo uyihitemwo.


Kuri iyi nkuru, uri ku nzira y'uruzitiro rwawe, ufise itegeko risa n'iri: `ronindojo@RoninDojo:~ $`. Kugira ngo ukoreshe **veth** gukosora, wandike itegeko rikurikira hanyuma ukande `injire`:

`sudo nano / n'ibindi / dhcpcd. conf'


Subira wemeze ijambobanga ryawe hanyuma ukande `enter`.


Uzoshika kuri dosiye `dhcpcd.conf`. Ukeneye gukopa umwandiko ukurikira, ukamenya neza ko ushiramwo akamenyetso k'inyenyeri, hanyuma ukawongerako hasi muri dosiye:

`kwanka imirongo veth*`


Kugira ngo ubikore, genda hasi muri dosiye ukoresheje umwampi uri hasi kuri klavye yawe, hanyuma ukoreshe gukanda iburyo kw’imbeba yawe kugira ngo ushire umwandiko ku murongo wigenga.


Uhejeje kwongerako umwandiko, kanda `ctrl X` kugira ngo utangure gusohoka, ukurikize `ctrl Y` kugira ngo wemeze ko wabitse ivyo wahinduye, hanyuma ukande `enter` kugira ngo uheze maze usubire ku nzira y'itegeko. Kugira ngo umenye neza ko ihinduka ryakoreshejwe neza, subira gufungura dosiye `dhcpcd.conf` ukoresheje itegeko rikwiye.


Kugira ngo urangize gukoresha ivyo gukosora, subiramwo urudodo rwawe ukoresheje:

`sudo yongera gufungura ubu`


Muri iki gihe, urashobora gufunga terminal yawe. Reka umwanya ukenewe kugira ngo RoninDojo yawe isubire gutangura, hanyuma ushobora gusubira kwifatanya biciye ku gishushanyo ca Interface c'umucukumbuzi wawe. Iyi nzira ikwiye gukosora ikibazo cahuye.


## Ni gute wokoresha urudodo rwawe rwa RoninDojo v2?


### Guhuza porogaramu yawe ya Wallet na Electrs

Ikoreshwa rya mbere ry’uruzitiro rwawe rwashizweho kandi rwahujwe rizoba ari ugutangaza amafaranga yawe ku rubuga rwa Bitcoin. Kumbure uzoshaka gufatanya ama wallets yawe atandukanye n’urudodo rwawe kugira ngo ushobore gutangaza amafaranga yawe mu ibanga. Ivyo ushobora kubigira biciye ku Serveri ya Electrum Rust (electrs). Iyi porogaramu akenshi ibanza gushirwa ku nzira yawe ya RoninDojo. Niba atarivyo, ushobora kuyishiramwo n'amaboko biciye kuri RoninCLI Interface muri `Ibikoresho > Gucungera Ibikoresho > Gushiramwo Serveri ya Electrum`.


Kugira uronke Tor Address ya Serveri yawe ya Electrum, uhereye ku rubuga rwa RoninUI Interface, genda kuri:

`Gufatanya > Serveri ya Electrum > Gufatanya ubu`

![Pairing](assets/notext/31.webp)

![Electrs](assets/notext/32.webp)

Uzoca ukenera kwinjiza `Izina ry'Umushitsi` Address rirangizwa na `.onion` muri porogaramu yawe ya Wallet, iherekejwe n'icuma `50001`. ![izina ry'umushitsi](itunga/inyandiko/33.urubuga)

Nk’akarorero, kuri Sparrow wallet, genda gusa kuri tab:

`Dosiye > Ivyo ukunda > Serveri > Electrum yihariye`


![Sparrow](assets/notext/34.webp)


### Guhuza porogaramu yawe ya Wallet na Samourai Dojo

Nk’ubundi buryo bwo gukoresha Electrs, Dojo iraguha uburenganzira bwo gufatanya Software Wallet yawe ihuye n’ivyo ukora ku nzira yawe ya RoninDojo. Ivyuma nka Samourai Wallet na Sentinel biratanga iyo nzira.


Kugira ngo ushireho iyo nzira, uzokenera gusa gucapura kode ya QR ya Dojo yawe. Kugira ngo ushikire iyi kode ya QR uciye kuri RoninUI, genda kuri:

`Gufatanya > Dojo ya Samourai > Gufatanya ubu`

![Samourai Dojo](assets/notext/35.webp)

Kugira ngo uhuze Samourai Wallet yawe na Dojo yawe, ushobora gusa gucapura iyi kode ya QR mu gihe uriko urashiramwo porogarama:


![Samourai Wallet connection](assets/notext/36.webp)


Niba wari usanzwe ufise Samourai Wallet imbere yo gushinga Ronin Dojo yawe, birakenewe ko ukora backup ya Wallet yawe, ukayikuramwo hanyuma ugasubira gushiramwo porogarama ya Samourai Wallet, imbere yo gusubizaho Wallet yawe. Uhejeje gutanguza porogarama yasubiwemwo, uzoba ufise uburenganzira bwo kwifatanya na Dojo nshasha. **Urabe maso, iyi nzira itwara ingorane zo gutakaza amafaranga yawe iyo udakoze neza!** Raba neza ko ufise ububiko bwa Samourai Wallet yawe mu madosiye yawe kandi usuzume ko passphrase yawe ikora biciye ku `Ivyagezwe > Gutorera umuti ingorane > passphrase`. Ni ngombwa kandi kugira ububiko bushobora gusomwa bw'amajambo yawe yo gukira n'igitabu cawe ca passphrase. Kugira ngo ushobore gukora neza muri iki gikorwa, birakenewe ko ukurikiza iyi nyigisho ido n’ido: [https://wiki.ronindojo.io/ru/gutegura/v2_0_0-gusubiramwo/gusubira gufatanya]


### Ukoresheje Mempool yawe bwite.ikibanza Block explorer

Block explorer ihindura amakuru atagiramwo ivyatsi ava muri Bitcoin Blockchain akayagira mu buryo butunganijwe kandi bushobora gusomwa bitagoranye. Hakoreshejwe ibikoresho nka *Mempool.space*, birashoboka gusuzuma amafaranga, kurondera amaderesi yihariye, canke mbere no kuraba ibiciro vy’amahera y’urubuga mu gihe nyaco.


Ariko rero, gukoresha abashakashatsi bo kuri Internet biratera ingorane ubuzima bwite bwawe kandi bikaba birimwo no kwizigira amakuru atangwa n’abandi. Nkako, ukoresheje izo nsiguro utaciye mu nzira yawe bwite, woshobora gutangaza amakuru yerekeye ivyo ukoresha ata co wiyumviriye kandi utegerezwa kwizigira ukuri kw’amakuru yashikirijwe na nyen’urubuga.

Kugira ngo ugabanye ivyo bibazo, birakenewe ko ukoresha instance yawe bwite ya *Mempool.space* biciye ku rubuga rwa Tor, rushizwe ku nzira yawe. Uwo muti uratuma ubuzima bwite bwawe n’ubwigenge bw’amakuru yawe buzigama.

Kugira ngo ubikore, tangura ushiremwo *Mempool Igishushanyo c'Ikirere* kivuye kuri RoninUI. Ku rubuga Interface, genda kuri `Dashboard` maze ukande kuri `Gucungera` munsi ya `Ikibanza ca Mempool`:

`Urubaho > Mempool Umwanya > Gucungera`

![Manage mempool](assets/notext/37.webp)

Hanyuma ukande kuri buto ya `Shiraho igishushanyo ca Mempool`:

![install mempool](assets/notext/38.webp)

Wemeze ijambobanga ryawe:

![password mempool](assets/notext/39.webp)

Rindira ko gushiramwo birangiye, hanyuma wongere ukande kuri buto ya `Gucungera`:

![Mempool Manage](assets/notext/40.webp)

Uzoronka `.onion` link kugira ngo ushikire instance yawe bwite ya *Mempool.space* biciye ku rubuga rwa Tor.

![Mempool link](assets/notext/41.webp)

Ndaguhanura ngo ubike iyi link mu vyo ukunda ku mucukumbuzi wa Tor canke ukayishira kuri app ya Tor Browser kuri telefone yawe kugira ngo ushobore kuyironka mu buryo bworoshe kandi ata nkomanzi uri aho hose. Niba utaragira umucukumbuzi wa Tor, ushobora kuwukura hano: [https://www.torproject.org/gukura/](https://www.torproject.org/gukura/)

![Mempool Tor](assets/notext/42.webp)


### Gukoresha Whirlpool kugira ngo uvange amafaranga yawe

Igikoresho cawe ca RoninDojo kandi gishiramwo _WhirlpoolCLI_, umurongo w'amabwirizwa Interface ushoboza kwikoresha kw'amafaranga y'amafaranga, na _WhirlpoolGUI_, Interface y'ibishushanyo yagenewe gukorana na _WhirlpoolCLI_.


Gukora CoinJoin biciye kuri Whirlpool bisaba ko porogarama ikoreshwa iba ikora kugira ngo ikore ama remix. Ivyo bishobora kuba bibuza abashaka gushika ku rwego rwo hejuru rw’ama anonsets. Nkako, igikoresho cakira porogarama ishiramwo Whirlpool kigomba kuguma gikora. Ivyo bisigura ko kugira ngo umuntu agire uruhara mu bikorwa vy’ugusubiramwo amasaha 24 ku musi, mudasobwa yawe canke telefone yawe y’amaboko bitegerezwa kuguma bifunguye Samourai canke Sparrow biguma bifunguye. Umuti w'iyi ngorane ni ugukoresha _WhirlpoolCLI_ ku mashini yama ifunguye, nk'uruzitiro rwa Bitcoin, bigatuma amafaranga yawe ashobora gusubira gukora ataco ahagarika, kandi ataco ukeneye kuguma ufunguye ikindi gikoresho.


Inyigisho ido n’ido iriko irategurwa kugira ngo ikuyobore intambwe ku yindi mu nzira yo gukorana na Samourai Wallet na RoninDojo v2, kuva kuri A gushika kuri Z.


Kugira ngo utahure neza CoinJoin n’ingene ikoreshwa kuri Bitcoin, ndagutumiye kandi ngo urabe iyi yindi ngingo: Gutahura no gukoresha CoinJoin kuri Bitcoin, aho ndadondora neza ivyo ukeneye kumenya vyose ku bijanye n’ubu buhinga.


https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2

### Gukoresha igikoresho ca Whirlpool (WST)


Inyuma yo gukora coinjoins na Whirlpool, ni vyiza gusuzuma neza urugero rw'ubuzima bwite rwashitsweko ku UTXOs zawe zivanzwe. Kugira ngo ubikore, ushobora gukoresha igikoresho ca Python *Whirlpool Stat Tool*. Ico gikoresho kigufasha gupima ibiharuro vy’imbere n’ivy’inyuma vy’ama UTXO yawe, mu gihe usesangura igipimo c’ukwiragira kwavyo mu kidengeri.


Kugira ngo urushirize gutahura uburyo bwo kubara izo nkuru zitaboneka, ndagusavye gusoma ingingo: REMIX - Whirlpool, idondora neza ingene izo nkuru zikora.


https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa



Kugira ngo ushikire igikoresho ca WST, genda kuri RoninCLI. Kugira ngo ubikore, fungura terminal kuri mudasobwa yawe bwite maze ushireho ubucuti bwa SSH n’uruzitiro rwawe ukoresheje iri tegeko rikurikira:

`SSH umuduga@[IP]`


Niba, nk'akarorero, IP y'uruzitiro rwawe Address ari `192.168.1.40`, itegeko rikwiye ryoba:

`SSH RONIDOJO@192.168.1.40`


Niba warahinduye izina ryawe ry'ukoresha mu ntambwe ya 6, usubiriza izina ry'ukoresha ry'imbere (`ronindojo`) n'irindi, urabe ko ukoresha iri zina rishasha mw'itegeko. Nk'akarorero, iyo uhisemwo `planb` nk'izina ryawe ry'ukoresha kandi IP Address ni `192.168.1.40`, itegeko ryo kwinjira ryoba:

'Umugambi wa SSH@192.168.1.40`


Uzosabwa kwinjiza ijambobanga ry’ukoresha. Injira hanyuma ukande `enter` kugira ngo wemeze. Uzoca ubona igitabu ca RoninCLI Interface. Koresha imfunguruzo z'umwampi kuri klavye yawe kugira ngo ugende ku rutonde rwa `Samourai Toolkit` hanyuma ukande `injire` kugira ngo uyihitemwo:


![Samourai Toolkit](assets/notext/43.webp)


Hanyuma uhitemwo `Igikoresho ca Whirlpool`:


![WST](assets/notext/44.webp)


Iyo utanguje WST, igikoresho kizobandanya n’ugushirwaho kwaco. Rindira mu gihe c’iyi ntambwe. Amabwirizwa y’ikoreshwa azogendagenda. Igihe gushiramwo, kanda urufunguzo urwo ari rwo rwose kugira ngo ushikire terminal ya WST:


![WST commands](assets/notext/45.webp)


Itegeko rikurikira rizogaragara:

`wst#/igerageza>`


Niba wipfuza gusohoka muri iyi Interface ugasubira mu rutonde rwa RoninCLI, winjize gusa:

'reka`


Mbere, ni ngombwa gutunganya proxy kugira ngo ikoreshe Tor, kugira ngo ubone ubuzima bwite igihe ukura amakuru muri OXT. Injira itegeko:

`amasogisi5 127.0.0.1:9050`


Hanyuma, genda ukureho amakuru y'ikigega arimwo amafaranga yawe:

`gukuraho 0001`

Subiriza `0001` kode y'idini y'ikidengeri ushaka. Amakode y'idini ni aya kuri WST:


- Ibice 0.5: `05`
- Ibice 0.05: `005`
- Ibice 0.01: `001`
- Ibice 0.001: `0001`


Inyuma yo gukuraho, shiramwo amakuru mu gusubirira `0001` na kode y'ikidengeri cawe muri iri tegeko: `shiramwo 0001`


![WST loading](assets/notext/46.webp)


Rindira ko ivyo bikoresho biheza, ivyo bishobora gutwara iminota mikeyi. Amakuru amaze gushirwako, kugira ngo umenye amanota y'ibiharuro vya Coin yawe, shira mu ngiro itegeko `amanota` akurikiwe na txid yawe (ata n'ibiharuro):

`amanota [txid]`


![WST score](assets/notext/47.webp)


WST izoca yerekana amanota y’inyuma (_Ibipimo vy’inyuma_), ikurikiwe n’amanota y’imbere (_Ibipimo vy’imbere_). Uretse amanota y’ibihembo, WST izokwerekana kandi igipimo c’ugukwiragira kw’ibikorwa vyawe mu kidengeri, bishingiye ku bihembo vyavyo.


**Ni vyiza kumenya ko amanota y’imbere y’igihe ya Coin yawe akwiye kubarwa ashingiye ku txid y’umuvumba wawe wa mbere, atari ku muvumba wawe wa nyuma. Ku rundi ruhande, igiharuro c’inyuma c’umuntu UTXO giharurwa kiva ku txid y’ingendo ya nyuma.**


### Gukoresha umubare wa Boltzmann

Igiharuro ca Boltzmann ni igikoresho co gusuzuma ibikorwa vya Bitcoin, gitanga ubushobozi bwo gupima urugero rw’uburemere bwaco mu bindi bipimo biteye imbere. Aya makuru aratanga isuzuma ry’ingero ry’ubuzima bwite bw’ugucuruza kandi afasha kumenya amakosa yoshobora kubaho. Ico gikoresho caramaze kwinjira mu nzira yawe ya RoninDojo, bikaba vyoroshe kuronka no gukoresha.


Imbere yo gutanga ido n’ido ry’ingene umuntu akoresha igiharuro ca Boltzmann, birahambaye ko atahura insobanuro y’ivyo bimenyetso, uburyo bwo kubiharura be n’akamaro kavyo. Naho bishobora gukoreshwa ku bijanye n’ugucuruza kwose kwa Bitcoin, ivyo bimenyetso ni ngirakamaro canecane mu gusuzuma uburyo ugucuruza kwa CoinJoin gukorwa.


**Ikimenyetso ca mbere** porogaramu iharura ni umubare wose w'imigwi ishoboka, yerekanwa munsi ya `nb combinations` mu gikoresho. Hashingiwe ku gaciro k’ama UTXO ari muri ivyo, iki kigereranyo kigereranya umubare w’uburyo ivyinjizwa bishobora gufatanywa n’ibisohoka. Mu yandi majambo, igena umubare w'insobanuro zishoboka igikorwa gishobora generate. Nk’akarorero, CoinJoin itunganijwe hakurikijwe ikigereranyo ca Whirlpool 5x5 yerekana `1496` imigwi ishoboka:

![combinations](assets/notext/50.webp)

Inguzanyo: KYCP


**Ikigereranyo ca kabiri** giharurwa ni entropie y'isoko, yerekanwa na `Entropie`. Iyo igikorwa gifise umubare munini w’imigwi ishoboka, kenshi birabereye cane kwerekeza ku entropie yaco. Ivyo bisobanurwa nk'umubare w'ibiharuro bibiri vy'imigwi ishoboka. Akira formule ikoreshwa:


- $E$: entropie y’ugucuruza;
- $C$: umubare w'imigwi ishoboka y'ugucuruza.

$$E = \igitabo_2(C)$$


Mu mibare, logarithme ya binaire (logarithme ya base 2) ihuye n’igikorwa co guhinduranya co kuduza 2 ku bushobozi. Mu yandi majambo, logarithme binaire ya $x$ ni igiharuro 2 kigomba kuduzwako kugira ngo umuntu aronke $x$. Ico kimenyetso rero kigaragazwa mu bice. Reka dufate akarorero ko kubara entropie y’igikorwa ca CoinJoin gitunganijwe hakurikijwe uburyo bwa Whirlpool 5x5, nk’uko twabibonye mbere, butanga umubare w’imigwi ishoboka ya `1496`:

$$ C = 1496 $$

$$ E = \igitabo_2(1496) $$

$$ E \hafi 10.5469 \umwandiko{ibice}$$


Gutyo, iyo nzira ya CoinJoin yerekana entropie y’ibice 10,5469, ivyo bikaba bibonwa ko bishimishije cane. Uko ako gaciro karushiriza kuba kanini, ni ko n’insobanuro zitandukanye iyo nzira yemera, gutyo bigatuma igira urugero rw’ubuzima bwite.


Reka dufate akarorero k'inyongera n'ugucuruza gusanzwe, gufise injiza imwe n'ibisohoka bibiri: 1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce] 00.umwanya/ru/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce)

Mu bijanye n'iyi nzira, insobanuro yonyene ishoboka ni: `(inp 0) > (Isohoka 0 ; Isohoka 1)`. Ku bw'ivyo, entropie yayo ishingwa kuri `0`:

$$ C = 1 $$

$$ E = \igitabo_2(1) $$

$$ E \hafi 0 \umwandiko{ ibice}$$

**Ikimenyetso ca gatatu** gitangwa n'Ibarabara rya Boltzmann citwa `Ubushobozi bwa Wallet`. Ico kigereranyo gisuzuma ubushobozi bw’ugucuruza mu kugereranya n’ugucuruza kwiza gushobora kwiyumvirwa mu ntunganyo isa. Ivyo bituma tuganira ku ciyumviro c’uburemere burengeye ubundi bwose, buhuye n’uburemere burengeye ubundi bwose umubumbe w’ubudandaji wihariye ushobora gushikako mu vyiyumviro. Gutyo, ku mibumbe ya Whirlpool 5x5 CoinJoin, uburemere burengeye ubundi bwose bushirwa kuri `10.5469`. Ubushobozi bw’ugucuruza buraheza buharurwa mu guhangana n’iyo entropi nkuru n’intropi nyayo y’ugucuruza kwasuzumwe. Iryo formule rikoreshwa ni iri:


- $ER$: entropie nyayo y’ugucuruza, igaragazwa mu bice;
- $EM$: entropie ishoboka cane ku miterere y'ibikorwa, na yo nyene mu bice;
- $Ef$: ubushobozi bw'ugucuruza, mu bice.

$$Ef = ER - EM$$ $$Ef = 10,5469 - 10,5469$$

$$Ef = 0 \umwandiko{ibice}$$


Iki kigereranyo naco kigaragazwa nk'ijanisha, formule yaco rero ni:


- $CR$: umubare w'imigwi nyayo ishoboka;
- $CM$: umubare munini w'imigwi ishoboka ifise imiterere imwe;
- $Ef$: ubushobozi bugaragazwa nk'ijanisha.

$$Ef = \umuce{CR}{CM}$$

$$Ef = \igice{1496}{1496}$$

$$Ef = 100\%$$


Ubushobozi bwa `100%` rero bwerekana ko iyo nzira yo gucuruza ishobora gutuma igira ubushobozi bwo gukingira ubuzima bwite bishingiye ku miterere yayo.


**Ikimenyetso ca kane**, uburemere bw’uburemere bw’ibintu, canke `Uburemere bw’uburemere bw’ibintu`, gitanga iciyumviro ku bijanye n’uburemere bw’ibintu bishingiye ku kintu cose cinjira canke gisohoka mu bijanye n’ugucuruza. Ico kigereranyo kigaragaza ko ari ngirakamaro mu gusuzuma no kugereranya ubushobozi bw’ibikorwa vy’ubudandaji vy’ubunini butandukanye. Kugira ngo uyiharure, ushobora gusa kugabanya entropie yose y’isoko n’umubare wose w’ibintu vyinjizwa n’ibisohoka birimwo. Dufashe akarorero k’indege y’umuyagankuba 5x5:


- $ED$: uburemere bw’uburemere bw’ibintu bugaragazwa mu bice;
- $E$: entropie y’ugucuruza igaragazwa mu bice;
- $T$: umubare wose w'ibintu vyinjizwa n'ibisohoka mu gucuruza.

$$T = 5 + 5 = 10$$

$$ED = \umuce{E}{T}$$

$$ED = \igice{10.5469}{10}$$

$$ED = 1.054 \umwandiko {ibice}$$

**Ikiganiro ca gatanu** gitangwa n’Ibarabara rya Boltzmann ni imbonerahamwe y’uguhuza ibishoboka hagati y’ivyo winjiza n’ivyo usohoka. Iyi mbonerahamwe yerekana, biciye ku `Boltzmann score`, ubushobozi bw'uko inyungu yihariye ihuye n'isohoka ry'umuntu. Dufashe akarorero ka Whirlpool CoinJoin, imbonerahamwe y’ibishoboka yogaragaza amahirwe y’uguhuza hagati y’ivyo umuntu yinjiza n’ivyo asohora, igatanga ingero y’ingero y’ukudasobanuka canke ukuntu amashirahamwe ashobora gutegekanirwa mu bijanye n’ugucuruza:


| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
|---------|----------|----------|----------|----------|----------|
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |


Aha, biragaragara ko ikintu cose cinjijwe gifise amahirwe angana yo gufatanya n’igisohoka cose, ivyo bikaba bikomeza ukutumvikana n’ubuzima bwite bw’ugucuruza. Ariko rero, ku bijanye n’ugucuruza kworoshe gufise ikintu kimwe co kwinjira n’ivyo gusohora bibiri, ibintu biratandukanye:


| %       | Output 0 | Output 1 |
|---------|----------|----------|
| Input 0 | 100%     | 100%     |

Aha, turabona ko ubushobozi bw’uko igisohoka cose kiva ku nkuru 0 ari 100%. Ivyiza bike rero bihindura ubuzima bwite bwinshi, mu gutuma amasano ataziguye hagati y’ivyo yinjiza n’ivyo asohoka agenda neza.


**Ikiganiro ca gatandatu** gitanzwe ni umubare w’amahuza y’ivy’ubuhinga, yuzuzwa n’igipimo c’ayo mahuza. Ico kigereranyo kirerekana ingene amasano ari menshi hagati y’ibintu vyinjizwa n’ibisohoka mu bikorwa vy’ubudandaji vyasuzumwe ataco bivuze, afise ubushobozi bwo kubaho 100%. Ico kigereranyo, na co nyene, kiratanga iciyumviro ku buremere bw’ayo mahuza y’ivy’ubuhinga mu mahuza yose y’ugucuruza.


Nk’akarorero, igikorwa co gucuruza CoinJoin c’ubwoko bwa Whirlpool nta mahuza y’ivy’ubuhinga kigaragaza, rero kigaragaza ikimenyetso n’igipimo ca 0%. Ku rundi ruhande, mu bikorwa vyacu vya kabiri twasuzumye (bifise inyungu imwe n’inyungu zibiri), ikigereranyo gishirwa kuri 2 maze igiharuro kigashika ku 100%. Gutyo, ikimenyetso c’ubusa kigaragaza ubuzima bwite bwiza cane kubera ukutagira amasano ataziguye kandi atagira aho ahengamiye hagati y’ibintu vyinjizwa n’ibisohoka.


**Ushobora gute gushika ku giharuro ca Boltzmann kuri RoninDojo?**

Kugira ngo ushikire igikoresho ca *Ibarabara rya Boltzmann*, genda kuri RoninCLI. Kugira ngo ubikore, fungura terminal kuri mudasobwa yawe bwite maze ushireho ubufatanye bwa SSH n'uruzitiro rwawe ukoresheje iri tegeko rikurikira: `SSH ronindojo@[IP]`


Niba, nk'akarorero, IP y'uruzitiro rwawe Address ari `192.168.1.40`, itegeko rikwiye ryoba:

`SSH RONIDOJO@192.168.1.40`


Niba wahinduye izina ryawe ry'ukoresha mu ntambwe ya 6, usubiriza izina ry'ukoresha ry'imbere (`ronindojo`) n'irindi, urabe ko ukoresha iri zina rishasha mw'itegeko. Nk'akarorero, iyo uhisemwo `planb` nk'izina ryawe ry'ukoresha kandi IP Address ni `192.168.1.40`, itegeko ryo kwinjira ryoba:

'Umugambi wa SSH@192.168.1.40`


Uzosabwa kwinjiza ijambobanga ry’ukoresha. Injira hanyuma ukande `enter` kugira ngo wemeze. Uzoca ubona igitabu ca RoninCLI Interface. Koresha imyampi iri kuri klavye yawe kugira ngo ugende kuri `Samourai Toolkit` maze ukande `enter` kugira ngo uyihitemwo:


![Samourai Toolkit](assets/notext/43.webp)


Hanyuma uhitemwo `Ibarabara rya Boltzmann`:


![boltzmann](assets/notext/49.webp)


Uzoshika kuri paji y'intango ya porogaramu:


![boltzmann home](assets/notext/51.webp)


Injira txid y'ibikorwa wipfuza kwiga hanyuma ukande urufunguzo `injira`:


![boltzmann txid](assets/notext/52.webp)


Ico giharuro gica kiguha ibimenyetso vyose twavuganye mbere:


![boltzmann result](assets/notext/53.webp)


### Ibindi biranga RoninDojo yawe v2.

Igikoresho cawe ca RoninDojo gishiramwo ibindi bintu bitandukanye. Cane cane, urafise ubushobozi bwo gucapura amakuru yihariye kugira ngo uyashire mu muzirikanyi. Nk’akarorero, rimwe na rimwe Samourai Wallet yawe, ifatanye na RoninDojo, yoshobora kutagaragaza ama bitcoins ufise vy’ukuri. Iyo umubare werekana 0 mu gihe uzi neza ko ufise bitcoins muri iyi Wallet, imvo zitari nke zirashobora gusigura ivyo bintu, nk’ikosa mu nzira z’ugukura. Ariko kimwe mu bishobora gutuma node yawe idakurikirana neza ama aderesi yawe. Kugira ngo utore umuti w'iki kibazo, ushobora kumenya neza ko urudodo rwawe rukurikira `xpub` yawe ukoresheje igikoresho ca _xpub_. Kugira ngo ushikire iki gikoresho biciye kuri RoninUI, kurikiza inzira:

`Gucungera > Igikoresho ca XPUB`


Injira muri `xpub` iriko irateza ingorane hanyuma ukande kuri buto ya `Suzuma` kugira ngo ugenzure aya makuru:

![xpub tool](assets/notext/54.webp)

Raba neza ko amafaranga yose agurishwa ari ku rutonde rwiza. Ni ngombwa kandi kugenzura ko ubwoko bw'inkomoko bukoreshwa buhuye n'ubwa Wallet yawe. Niba atari uko biri, fyonda ku `Retype`, hanyuma uhitemwo muri `BIP44`, `BIP49`, canke `BIP84` bivanye n'ivyo ukeneye.

Uretse iki gikoresho, `Maintenance` tab ya RoninUI yuzuye ibindi bikoresho vy'ingirakamaro:


- Igikoresho co Gucuruza*: Kiremesha gusuzuma ido n’ido ry’ugucuruza;
- Address Tool*: Iremeza kwemeza ugukurikirana kwa Address yatanzwe na Dojo yawe;
- Rescan Blocks*: Ihatira node yawe gukora scanner nshasha y'urutonde rw'amabuye.


Igipande ca `Push Tx` ni ikindi kintu gishimishije ca RoninUI, gishobora gutangaza amakuru yashizweko umukono ku rubuga rwa Bitcoin. Ivyo bicuruzwa bitegerezwa kwinjira mu buryo bw’inyuguti cumi n’itandatu.


Ku bijanye n'izindi nzira ziboneka ku rubuga rwawe rwa RoninUI:


- `Apps`: Ikira porogaramu ya Whirlpool, kandi nta gukeka ko izokoreshwa mu gushiramwo porogaramu nshasha muri kazoza;
- `Inyandiko`: Itanga igihe nyaco co gushika ku nyandiko z'ivyabaye za porogaramu yawe;
- `Amakuru ya Sisitemu`: Itanga amakuru rusangi yerekeye urudodo rwawe, nk'ubushuhe bwa CPU, ikoreshwa ry'umwanya wo kubika, canke amakuru ya RAM. Uzosanga kandi `Reboot` na `Shut down` amahitamwo yo gusubira gutangura canke kuzima urudodo rwawe;
- `Ivyagezwe`: Biguha uburenganzira bwo guhindura ijambobanga ryawe.


Aho ni ho ufise! Murakoze gukurikira iyi nyigisho gushika kw’iherezo. Niba waravyishimiye, ndaguhimiriza ngo ubisangire ku mbuga ngurukanabumenyi. Ikindi, niwaba ufise akaryo, niwiyumvire gushigikira abakora izo porogarama z’ubuntu kandi zifunguye ziboneka mu kibano cacu n’intererano: [https://donate.ronindojo.io/](https://donate.ronindojo.io/). Kugira ngo umenye cane RoninDojo kandi ubone ibindi bikoresho, ndagusavye cane kuraba amahuzu y’ibikoresho vyo hanze vyavuzwe aha hepfo.


**Ibikoresho vyo hanze:**


- [urutonde rw'ibintu] (urutonde rw'ibintu)
- [Urupapuro rw'Imana](urupapuro rw'Ivyabona vya Yehova)
- [Ikiganiro c'Igihugu c'Igihugu c'Igihugu c'Igihugu c'Igihugu c'Igihugu c'Igihugu c'Igihugu c'Igihugu.
- [Ubumenyeshamakuru/@laurentmt/kumenyesha-boltzmann-85930984a159](ubumenyeshamakuru/@laurentmt/kumenyekanisha-boltzmann-85930984a159)
- [wiki.ronindojo.io/ru/gutegura/V2_0_0-guhindura-umukaraba](ubutumwa bushasha/gutegura/V2_0_0-guhindura-umukaraba)
