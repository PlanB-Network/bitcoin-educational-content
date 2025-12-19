---
name: RoninDojo

description: Gushiramwo no gukoresha urudodo rwawe rwa RoninDojo Bitcoin.
---
***IMBURIZO:** Inyuma y'aho abashinze Samourai Wallet bafashwe, ama server yabo bagafatwa kw'igenekerezo rya 24 Ndamukiza, hari ibintu bimwe bimwe vyo muri RoninDojo, nka Whirlpool, bitagikora. Ariko birashoboka ko ivyo bikoresho vyosubira gukoreshwa canke bikagaruka gukoreshwa mu buryo butandukanye mu ndwi ziza. Ikindi, kubera ko kode ya RoninDojo yari yashizwe kuri GitLab ya Samourai, na yo nyene yafashwe, ubu ntibishoboka ko umuntu ayikura kure. Amashirahamwe ya RoninDojo birashoboka ko ariko arakora ku bijanye no gusubira gusohora iyo kode.*


_Turiko turakurikirana cane iterambere ry’uru rubanza hamwe n’iterambere ryerekeye ibikoresho bijana. Nimwizere ko tuzosubiramwo iyi nyigisho uko amakuru mashasha azoboneka._


_Iyi nyigisho itangwa ku ntumbero y'inyigisho n'amakuru gusa. Ntidushigikira canke ngo turemeshe gukoresha ivyo bikoresho mu ntumbero z’ubugizi bwa nabi. Ni inshingano y'ukoresha wese kwubahiriza amategeko ari mu bubasha bwiwe._


_Iyi nyigisho ni iyo gushiramwo RoninDojo v1. Kugira ngo wungukire ku bintu bishasha vyashizweho n’ibindi bishasha, ndagusavye cane kuraba inyigisho yacu yerekeye gushiramwo RoninDojo v2 kuri Raspberry Pi yawe:_

https://planb.academy/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

---

Kwiruka no gukoresha urudodo rwawe bwite ni ngombwa kugira ngo vy’ukuri ugire uruhara mu murongo wa Bitcoin. Naho gukoresha node ya Bitcoin ata nyungu n’imwe y’amahera bizana ku muntu ayikoresha, biratuma ashobora kuzigama ubuzima bwiwe bwite, akora yigenga, kandi akagira ububasha ku cizigiro afise ku rubuga.


Muri iyi nkuru, turaza kuraba mu buryo burambuye RoninDojo, umuti mwiza wo gukoresha node yawe bwite ya Bitcoin.


### Imbonerahamwe y'ibirimwo:



- RoninDojo ni iki?
- Ni igiki co guhitamwo?
- Ni gute woshiramwo RoninDojo?
- Ni gute twokoresha RoninDojo?
- Iciyumviro


Niba utazi neza ingene urudodo rwa Bitcoin rukora n’uruhara rwarwo, ndagusavye gutangura usoma iyi nkuru: Urudodo rwa Bitcoin - Igice ca 1/2: Ivyiyumviro vy’ubuhinga.


![Samourai](assets/1.webp)


## RoninDojo ni iki?


Dojo ni umurongo wuzuye wa Bitcoin wakozwe n’umugwi wa Samourai Wallet. Ushobora kuyishira ku mashini iyo ari yo yose mu mwidegemvyo.


RoninDojo ni umufasha mu gushiramwo n’igikoresho co gutwara Dojo n’ibindi bikoresho bitandukanye. RoninDojo ifata ugushirwa mu ngiro kwa mbere kwa Dojo yongerako ibindi bikoresho vyinshi, mu gihe kandi ituma gushiramwo no gucunga vyoroha.


Batanga kandi igikoresho "co gutera no gukina", RoninDojo Tanto, RoninDojo ibanza gushirwa ku mashini yakoranijwe n'umugwi wabo. Tanto ni umuti wishurwa, ubereye abadashaka guhumanya ibiganza.


Kode ya RoninDojo ni open-source, rero birashoboka kandi gushiramwo uwo muti ku bikoresho vyawe bwite. Iryo hitamwo rirahenda ariko risaba gukoresha nabi gatoyi, ivyo ni vyo tuzokora muri iki kiganiro.


RoninDojo ni Dojo, rero bituma ushobora gushiramwo Whirlpool CLI mu buryo bworoshe mu nzira yawe ya Bitcoin kugira ngo ubone ubumenyi bwiza cane bwa CoinJoin. Na Whirlpool CLI, ntushobora gusa kureka bitcoins zawe zigakora remix 24/7 utakeneye kuguma ukoresha mudasobwa yawe bwite, ariko kandi urashobora gutuma ubuzima bwite bwawe butera imbere cane.


RoninDojo ihuriza hamwe ibindi bikoresho vyinshi vyishingikiriza kuri Dojo yawe, nk’igiharuro ca Boltzmann, kigena urugero rw’ubuzima bwite bw’ibikorwa, umukozi wa Electrum wo gufatanya ama wallet yawe atandukanye ya Bitcoin n’uruzitiro rwawe, canke umukozi wa Mempool wo kwihweza mu mwiherero ivyo ukora.

Ugereranije n'iyindi nzira y'umuti nka Umbrel, iyo nabashikirije muri iyi nkuru, RoninDojo yibanze cane ku nzira za "on chain" n'ibikoresho bituma ubuzima bwite bw'abakoresha bugenda neza. Rero, RoninDojo ntiyemera gukorana na Lightning Network.

RoninDojo itanga ibikoresho bikeyi ugereranyije na Umbrel, ariko ibintu bikeyi vy’ingenzi ku Bitcoiner biri kuri Ronin birashikamye bitangaje.


Rero nimba udakeneye ibintu vyose vya server ya Umbrel kandi ushaka gusa node yoroshe kandi ihamye ifise ibikoresho bikeyi vy’ingenzi nka Whirlpool canke Mempool, rero RoninDojo birashoboka ko ari umuti mwiza kuri wewe.


Mu vyiyumviro vyanje, iterambere rya Umbrel ryibanda cane kuri Lightning Network n’ibikoresho vyinshi. Ni node ya Bitcoin, ariko intumbero ni ukuyigira mini-server ikora ibikorwa vyinshi. Mu buryo bunyuranye, iterambere rya RoninDojo ryibanda ku bijanye n’imigwi yo muri Samourai Wallet kandi ryibanda ku bikoresho nyamukuru vy’umunya Bitcoin, bikaba vyemeza ubwigenge bushitse n’uburongozi bwiza bw’ubuzima bwite kuri Bitcoin.


Urashobora kubona ko gushinga urudodo rwa RoninDojo bitoroshe gatoyi kuruta urudodo rwa Umbrel.


None ko twashoboye gushushanya ishusho ya RoninDojo, reka turabe ingene twoshiraho iyo node hamwe.


## Ni igiki co guhitamwo?


Kugira uhitemwo imashini yakira kandi ikoresha RoninDojo, urafise uburyo bwinshi.


Nk’uko vyasiguwe imbere y’aho, uburyo bworoshe bwo guhitamwo ni ugusaba Tanto, imashini ishobora gukoreshwa n’umuyagankuba, ikaba yagenewe canecane iyo ntumbero. Kugira ngo usabe ivyawe, genda hano: [ihuriro](https://iduka.ronindojo.io/urutonde rw'ibicuruzwa/ibihimba/).


Kubera ko amashirahamwe ya RoninDojo akora kode y’inkomoko yuguruye, birashoboka kandi gushirwa mu ngiro RoninDojo ku zindi mashini. Ushobora kubona amaverisiyo mashasha y’umuhinga wo gushiramwo kuri iyi paji: [ihuriro](https://ronindojo.io/ru/downloads.html), n’amaverisiyo mashasha ya kode kuri iyi paji: [ihuriro](https://code.samourai.io/ronindojo/RoninDojo).


Ku bwanje, nayishize kuri Raspberry Pi 4 8GB kandi vyose birakora neza cane.


Ariko rero, ndabinginze mumenye ko amashirahamwe ya RoninDojo yerekana ko kenshi haba ingorane ku bijanye n’igisandugu be n’igikoresho co gukoresha SSD. Ntivyiza rero gukoresha igikapu gifise umugozi wa SSD y’imashini yawe. Ahubwo, ni vyiza gukoresha ikarita yo kwagura ububiko yagenewe canecane urupapuro rwawe, nk’iyi: Ikarata yo kwagura ububiko bwa Raspberry Pi 4.


Aha ni akarorero k'ingene woshiraho urudodo rwawe rwa RoninDojo:



- Pi 4 y'umukaraba.
- Igikapu gifise umuyaga.
- Ikarata yo kwagura ububiko ihuye.
- Umugozi w’amashanyarazi.
- Ikarata micro SD y’inganda ifise 16GB canke irenga.
- SSD ya 1TB canke nini kuruta.
- Umugozi wa Ethernet RJ45, wo mu rwego rwa 8 ni wo ushimikwako.


## Ni gute woshiramwo RoninDojo?


### Intambwe ya 1: Tegura ikarita ya micro SD ishobora gufunguka.


Umaze gukoranya imashini yawe, urashobora gutangura gushiramwo RoninDojo. Kugira ngo ubikore, tangura ukoresheje ikarita micro SD ishobora gufungurwa mu kuyiturirako ishusho ya disiki ibereye.


Injira ikarita yawe ya micro SD muri mudasobwa yawe bwite, hanyuma ugende ku rubuga rwemewe rwa RoninDojo kugira ngo ubone ishusho ya disiki ya RoninOS: https://ronindojo.io/ru/downloads.html.


Gukuraho ishusho ya disiki ihuye n’ibikoresho vyawe. Mu gihe canje, narakuyeho ishusho ya "MANJARO-ARM-RONINOS-RPI4-22.03.IMG.XZ":


![Download RoninOS disk image](assets/2.webp)


Ishusho imaze gukurwako, suzuma ubutungane bwayo ukoresheje dosiye .SHA256 ihuye. Nzodondora mu buryo burambuye ingene ivyo bikorwa muri iyi nkuru: Ni gute wogenzura ubutungane bwa porogarama ya Bitcoin kuri Windows?


Amabwirizwa yihariye yo kugenzura ubutungane bwa RoninOS araboneka no kuri iyi paji: https://wiki.ronindojo.io/ru/extras/verify.


Kugira ngo uturire iyo shusho ku ikarita yawe ya micro SD, ushobora gukoresha porogarama nka Balena Etcher, ushobora kuyikura hano: https://www.balena.io/etcher/.


Kugira ngo ubikore, hitamwo ishusho iri muri Etcher hanyuma uyishire ku ikarita ya micro SD:


![Burn disk image with Etcher](assets/3.webp)


Igihe igikorwa kirangiye, urashobora kwinjiza ikarata micro SD ishobora gufunguka muri Raspberry Pi maze ugaca ufungura imashini.


### Intambwe ya 2: Gutegura RoninOS.


RoninOS ni uburyo bwo gukoresha uruzitiro rwawe rwa RoninDojo. Ni verisiyo yahinduwe ya Manjaro, ikoreshwa rya Linux. Uhejeje gutangura imashini yawe no kurindira iminota mikeyi, urashobora gutangura kuyitunganya.


Kugira ngo uyihuze kure, uzokenera kurondera IP Address y’imashini yawe ya RoninDojo. Kugira ngo ubikore, urashobora nk’akarorero kwifatanya n’ibarabara ry’ubuyobozi ry’agasanduku kawe ka interineti, canke ushobora no gukuraho porogarama nka https://angryip.org/ kugira ngo ushiremwo urubuga rwawe rwo mu karere maze uronke IP y’iyo mashini.


Uhejeje kuronka IP, urashobora gufata ububasha ku mashine yawe ukoresheje iyindi mudasobwa ifatanye n’iyo nzira nyene y’aho uba ukoresheje SSH.


Uvuye kuri mudasobwa ikoresha macOS canke Linux, fungura gusa terminal. Uvuye kuri mudasobwa ikoresha Windows, ushobora gukoresha igikoresho kidasanzwe nka Putty canke ukoresheje Windows PowerShell.


Igihe terminal yuguruye, wandike itegeko rikurikira:

```
ssh root@192.168.?.?
```


Gusa usubirize ibimenyetso bibiri vy’ikibazo IP ya RoninDojo wari warabonye mbere.

Impanuro: Mu Shell, kanda iburyo kugira ngo ushireko ikintu.


Inyuma y’aho, uzoshika ku kibanza co gucungera Manjaro. Hitamwo uburyo bwiza bwo gukoresha klavye ukoresheje imyampi kugira ngo uhindure intumbero iri muri list imanuka.


![Manjaro Keyboard Configuration](assets/4.webp)


Hitamwo izina ry'ukoresha n'ijambobanga ry'ikiganiro cawe. Koresha ijambobanga rikomeye maze ukore ububiko butekanye. Ushobora gukoresha ijambobanga ry'intege nke mu gihe co gushiramwo, hanyuma ukarihindura mu buryo bworoshe mu "gukopa-gushiramwo" muri RoninUI. Ivyo bizotuma ukoresha ijambobanga rikomeye cane utamara umwanya munini uriyandika n’amaboko mu gihe co gutegura Manjaro.


![Manjaro Username Configuration](assets/5.webp)


Igikurikira, uzosabwa kandi guhitamwo ijambobanga ry’umuzi. Ku jambobanga ry'umuzi, shiramwo ijambobanga rikomeye ataco rihinduye. Ntuzoshobora kuyihindura uhereye kuri RoninUI. Kandi, wibuke gufata neza iri jambobanga ry’umuzi.


Hanyuma winjize aho uri n’isaha yawe.


![Manjaro Time Zone Configuration](assets/6.webp)


![Manjaro Location Configuration](assets/7.webp)


Igikurikira, uhitemwo izina ry’umushitsi.


![Manjaro Hostname Configuration](assets/8.webp)


Ubwa nyuma, suzuma amakuru y’imiterere ya Manjaro maze wemeze.


![Verification of ManjaroOS Configuration Information](assets/9.webp)


### Intambwe ya 3: Gukuraho RoninDojo.


Ivy’intango vyo gutegura RoninOS bizokorwa. Iyo imaze guheza, nk’uko vyerekanwa ku gicapo kiri hejuru, iyo mashini izosubira gukora. Rindira umwanya muto, hanyuma winjize itegeko rikurikira kugira ngo wongere wihuze n'imashini yawe ya RoninDojo:

```
ssh username@192.168.?.?
```


Gusa usubirize "izina ry'ukoresha" n'izina ry'ukoresha wahisemwo mbere, hanyuma usubirize ibimenyetso vy'ibibazo IP ya RoninDojo yawe.


Hanyuma winjize ijambobanga ryawe.


Mu nzira, bizomera gutya:


![SSH Connection to RoninOS](assets/10.webp)


Ubu rero uhuye n’imashini yawe, ubu ifise RoninOS gusa. Ubu rero ukeneye gushiramwo RoninDojo kuri yo.


Gukuraho verisiyo nshasha ya RoninDojo winjiza itegeko rikurikira:

```
git clone https://code.samourai.io/ronindojo/RoninDojo
```


Ivyo bizoba vyihuta. Mu terminal, uzobona ibi:


![Cloning RoninDojo](assets/11.webp)


Rindira ko ivyo gukuraho birangiye, hanyuma ushiremwo kandi ushikire umukoresha wa RoninDojo Interface ukoresheje itegeko rikurikira:

```
~/RoninDojo/ronin
```


Uzosabwa kwinjiza ijambobanga ryawe:


![Bitcoin Node Password Verification](assets/12.webp)


Iri tegeko rikenewe gusa igihe ca mbere winjiye muri RoninDojo yawe. Inyuma y'aho, kugira ngo ushikire RoninCLI biciye kuri SSH, uzokenera gusa kwinjiza itegeko [SSH izina ry'ukoresha@192.168.?.?] usubiriza "izina ry'ukoresha" izina ryawe ry'ukoresha maze winjize IP Address y'uruzitiro rwawe. Uzosabwa ijambobanga ryawe ry'ukoresha.


Igikurikira, uzobona iyi nkuru nziza cane:


![RoninCLI launch animation](assets/13.webp)


Hanyuma uzoshika ku mukoresha wa RoninDojo CLI Interface.


### Intambwe ya 4: Shiraho RoninDojo.


Kuva ku rutonde nyamukuru, genda kuri rutonde rwa "System" ukoresheje imfunguruzo z'umwampi ziri kuri klavye yawe. Kanda urufunguzo rwo kwinjira kugira ngo wemeze ihitamwo ryawe.


![RoninCLI navigation menu to System](assets/14.webp)


Hanyuma ugende kuri "Gutegura no gushiramwo Sisitemu".


![RoninCLI navigation menu to RoninDojo system installation](assets/15.webp)


Ubwa nyuma, reba "Itegeko rya Sisitemu" na "Gushiramwo RoninDojo" ukoresheje umurongo w'umwanya, hanyuma uhitemwo "Emera" kugira ngo utangure gushiramwo.


![RoninDojo installation confirmation](assets/16.webp)


Reka ugushiraho bigende mu gacerere. Ku bwanje, vyatwaye nk’amasaha 2. Gumana terminal yawe yuguruye mu gihe c’ivyo bikorwa.


Rimwe na rimwe suzuma terminal yawe, kuko uzosabwa gukanda urufunguzo ku ntambwe zimwe zimwe z'ugushiraho, nk'aha nk'akarorero:


![RoninDojo installation in progress](assets/17.webp)


Inyuma y'ugushiraho, uzobona ibikoresho bitandukanye bitangura:


![Node container startup](assets/18.webp)


Hanyuma node yawe izosubira gutangura. Wongere uhuze na RoninCLI ku ntambwe ikurikira.


![Bitcoin node restart](assets/19.webp)


### Intambwe ya 5: Gukuraho uruzitiro rwa Proof-of-Work maze winjire kuri RoninUI.


Igihe gushiramwo, node yawe izotangura gukuraho uruzitiro rwa Bitcoin Proof-of-Work. Ivyo vyitwa Gukuraho Ivya mbere (IBD). Kenshi bifata hagati y’imisi 2 na 14 bivanye n’uko ukoresha internet n’igikoresho ukoresha.


Ushobora gukurikirana ingene uruhererekane rwo gukuraho rugenda ukoresheje urubuga rwa RoninUI Interface.


Kugira ngo uyironke ukoresheje urubuga rwo mu karere, wandike ibi bikurikira mu mucukumbuzi wawe Address:



- Ushobora kwinjira muri IP Address y'imashini yawe (192.168.?.?)
- Canke winjire: ronindojo.aho hantu


Ibuka guhagarika VPN yawe nimba uriko urakoresha.


### Gugoramye bishoboka


Niba udashobora kwifatanya na RoninUI ukoresheje umucukumbuzi wawe, suzuma uko porogarama ikora neza ukoresheje Terminal yawe ihuye n’uruzitiro rwawe biciye kuri SSH. Huza kuri menyu nyamukuru ukurikije intambwe zabanje:



- Ubwoko: Izina ry'ukoresha rya SSH@192.168.?.? gusubirira n’ivyemezo vyawe.



- Injira ijambobanga ryawe.


Igihe umaze ku rutonde nyamukuru, genda kuri: **RoninUI > Gusubira gutangura**


Iyo porogaramu isubiye gutangura neza, ni ingorane y’uguhuza kuva ku mucukumbuzi wawe. Suzuma ko udakoresha VPN kandi urabe ko uhuye n’urubuga rumwe n’urudodo rwawe.


Niba gusubira gutangura bizana ikosa, gerageza guhindura ubuhinga bwo gukoresha hanyuma wongere ushiremwo RoninUI. Kugira ngo uhindure OS: **Sisitemu > Ivugurura rya porogaramu > Vugurura Sisitemu ikoresha**


Igihe ivugurura n'ugusubira gutangura birangiye, subira kwifatanya n'uruzitiro rwawe biciye kuri SSH hanyuma wongere ushiremwo RoninUI: **RoninUI > Subira ushiremwo**


Amaze gusubira gukuraho RoninUI, gerageza kwifatanya na RoninUI biciye ku mucukumbuzi wawe.


**Impanuro:** Niwasohoka muri RoninCLI mu mpanuka ugasanga uri ku nzira ya Manjaro, ushiremwo gusa itegeko "ronin" kugira ngo usubire ku rutonde rwa RoninCLI.


### Kwinjira ku rubuga


Ushobora kandi kwinjira ku rubuga rwa RoninUI Interface ukoresheje urubuga urwo ari rwo rwose ukoresheje Tor. Kugira ngo ubikore, fungura Tor Address ya RoninUI yawe muri RoninCLI: **Ivyemezo > Ronin UI**


Kugarura Tor Address ihera kuri .onion hanyuma winjire muri Ronin UI winjiza iyi Address mu mucukumbuzi wawe wa Tor. Urabe maso ntusohoke amakuru yawe atandukanye, kuko ari amakuru y’agaciro.


![RoninUI web login interface](assets/20.webp)


Uhejeje kwinjira, uzosabwa ijambobanga ryawe. Ni ijambobanga nyene ukoresha kugira winjire biciye kuri SSH.


![RoninUI web interface management panel](assets/21.webp)


Turashobora kubona ingene IBD (Intial Block Download) itera imbere hano. Wihangane, uriko uraronka amafaranga yose yakozwe kuri Bitcoin kuva ku wa 3 Mukakaro 2009.


Amaze gukuraho Blockchain yose, indexer izokoranya urutonde rw’amakuru. Ivyo bifata amasaha nk’12. Ushobora kandi gukurikirana ingene itera imbere munsi ya "Indexer" kuri RoninUI.


Igikoresho cawe ca RoninDojo kizokora neza inyuma y'ibi:


![Indexer synchronized at 100% functional node](assets/22.webp)


Niba ushaka guhindura ijambobanga ry'ukoresha ngo ribe irindi rikomeye, ushobora kubigira ubu ukoresheje "Ivyagezwe". Kuri RoninDojo, nta mutekano w’inyongera Layer, rero ndabagira inama yo guhitamwo ijambobanga rikomeye vy’ukuri no kwitwararika ububiko bwaryo.


## Ni gute twokoresha RoninDojo?


Igihe uruzitiro rumaze gukurwako no gukorana, urashobora gutangura kunezerererwa ibikorwa bitangwa n’uruzitiro rwawe rushasha rwa RoninDojo. Reka turabe ingene twobikoresha.


### Guhuza porogarama ya Wallet n’amashanyarazi.


Ivyiza vya mbere vy’uruzitiro rwawe rushasha rwashizweho kandi rwahujwe bizoba ari ugutangaza amafaranga yawe ku rubuga rwa Bitcoin. Ku bw’ivyo, birashoboka ko uzoshaka gufatanya na yo porogarama yawe itandukanye yo gucunga Wallet.


Ivyo ushobora kubikora ukoresheje umuyagankuba Rust (electrs). Porogaramu isanzwe ibanza gushirwa ku nzira yawe ya RoninDojo. Niba atarivyo, ushobora kuyishiramwo n'amaboko ukoresheje RoninCLI Interface.


Gusa genda kuri: **Ibikoresho > Gucungera Ibikoresho > Shiraho Electrum Server**


Kugira uronke Tor Address ya Serveri yawe ya Electrum, mu rutonde rwa RoninCLI, genda kuri:

**Ivyemezo > Amashanyarazi**


Ubwirizwa gusa kwinjira muri .onion link muri porogaramu yawe ya Wallet. Nk’akarorero, muri Sparrow wallet, genda ku rubuga:

**Dosiye > Ivyo ukunda > Serveri**


Mu bwoko bwa server, hitamwo `Electrum yihariye`, hanyuma winjize Tor Address ya Serveri yawe ya Electrum mu kibanza gihuye. Ubwa nyuma, fyonda ku "Test Connection" kugira ngo ugerageze kandi ubike ubufatanye bwawe.


![Sparrow Wallet connection interface to an electrs](assets/23.webp)


### Guhuza porogarama ya Wallet na Dojo ya Samourai.


Aho gukoresha Electrs, urashobora kandi gukoresha Samourai Dojo kugira ngo uhuze Software Wallet yawe ihuye n’urudodo rwawe rwa RoninDojo. Nk’akarorero, Samourai Wallet iratanga iyo nzira.


Kugira ngo ubikore, ushobora gusa gucapura kode ya QR y’ihuriro rya Dojo yawe. Kugira ngo uyironke ukoresheje RoninUI, fyonda ku rubuga rwa "Dashboard" hanyuma ukande ku buto bwa "Manage" buri mu gasandugu ka Dojo yawe. Uzoheza ubone amakode ya QR y’uguhuza Dojo yawe na BTC-RPC Explorer. Kugira ngo ubigaragaze, kanda kuri "Kwerekana agaciro".


![Retrieving the connection QR code to Dojo](assets/24.webp)


Kugira ngo uhuze Samourai Wallet yawe na Dojo yawe, uzokenera gucapura iyi kode ya QR mu gihe co gushiramwo porogarama:


![Connecting to Dojo from the Samourai Wallet application](assets/25.webp)


### Ukoresheje igikoresho cawe ca Mempool.


Igikoresho gihambaye ku ba Bitcoiners, umugenzuzi aragufasha kugenzura amakuru atandukanye yerekeye uruzitiro rwa Bitcoin. Nk’akarorero, ukoresheje Mempool, urashobora kumenya mu gihe nyaco amahera akoreshwa n’abandi bakoresha kugira ngo uhindure ayawe bihuye n’ivyo. Ushobora kandi kugenzura uko kimwe mu bikorwa vyawe vyemejwe canke ukabona amahera asigaye kuri Address.


Ivyo bikoresho vy’ubushakashatsi birashobora kugutera ingorane z’ubuzima bwite kandi bikagusaba kwizigira urutonde rw’amakuru rw’uwundi muntu. Iyo ukoresheje iki gikoresho co kuri internet utaciye mu nzira yawe bwite:



- Ushobora gusohora amakuru yerekeye Wallet yawe.



- Uzigira umuyobozi w’urubuga rw’uruzitiro rwa Proof-of-Work bakira.


Kugira ngo wirinde ivyo bibazo, urashobora gukoresha instance yawe bwite ya Mempool ku node yawe biciye ku rubuga rwa Tor. Iyo ukoresheje uwo muti, ntuzigama gusa ubuzima bwite bwawe igihe ukoresha iyo serivisi, ariko kandi ntugikeneye kwizigira uwuguha iyo serivisi kuko ubaza urutonde rwawe bwite.


Kugira ngo ubikore, tangura ushiremwo Mempool Igishushanyo c'Ikirere kivuye kuri RoninCLI:


**Ibikoresho > Gucungera Ibikoresho > Shiraho Mempool Igishushanyo c'Ikirere**


Iyo umaze kuyishiramwo, ushiremwo uruja n'uruza rwa Mempool yawe. Tor Address izogufasha kuyironka uri ku rubuga urwo ari rwo rwose. Natwe nyene, turaronka iyi nzira biciye kuri RoninCLI:


**Ivyemezo > Mempool**


![Retrieve Tor Mempool address](assets/26.webp)


Niwinjize gusa Mempool Tor Address yawe mu mucukumbuzi wa Tor kugira ngo uryoherwe n’inkuru yawe bwite ya Mempool, ishingiye ku makuru yawe bwite. Ndabagira inama yo kwongerako iyi Tor Address ku vyo mukunda kugira ngo muyironke ningoga. Ushobora kandi gukora inzira ngufi ku biro vyawe.


![Mempool Space interface](assets/27.webp)


Niba utaragira umucukumbuzi wa Tor, ushobora kuwukura hano: https://www.torproject.org/download/


Ushobora kandi kuyironka ukoresheje telefone yawe ukoresheje Tor Browser maze ukayinjiramwo Address nyene. Uhereye aho hose, urashobora kubona uko uruzitiro rwa Bitcoin rumeze ukoresheje urudodo rwawe bwite.


### Gukoresha Whirlpool CLI.


Igikoresho cawe ca RoninDojo kirimwo kandi WhirlpoolCLI, umurongo w'amabwirizwa wo kure Interface wo gukoresha ubuhinga bwa Whirlpool.


Iyo ukora CoinJoin n’ugushirwa mu ngiro kwa Whirlpool, porogarama uriko urakoresha itegerezwa kuguma yuguruye kugira ngo ukore imivumba n’imivumba. Ivyo bishobora kuba bigoye ku bakoresha bashaka kugira ama sets menshi, kuko igikoresho cakira porogarama gifise Whirlpool kigomba kuguma gikora. Mu majambo y’ibikorwa, ivyo bisigura ko niwaba ushaka gukorana n’aba UTXO bawe mu gukora ama remixes 24/7, uzokenera kuguma ukoresha mudasobwa yawe canke telefone yawe bwite kandi iyo porogarama ifunguye.


Umuti umwe w’iyi ngorane ni ugukoresha WhirlpoolCLI ku mashini igenewe kuguma ikora, nk’uruzitiro rwa Bitcoin. Ivyo bituma UTXO zacu zishobora gusubirwamwo 24/7 ataco zikeneye kuguma zikoresha iyindi mashini atari node yacu ya Bitcoin.

WhirlpoolCLI ikoreshwa na WhirlpoolGUI, igishushanyo Interface co gushirwa kuri mudasobwa y’umuntu ku giti ciwe kugira ngo ushobore gucunga Coinjoins mu buryo bworoshe. Nzobasigurira mu buryo burambuye ingene woshiraho Whirlpool CLI ufise dojo yawe bwite muri iyi nkuru: [ihuriro](https://www.pandul.fr/iposita/ugutahura-n'ugukoresha-CoinJoin-ku-Bitcoin#:~:umwandiko=dans%20cette%20p artie.-,Inyigisho%20%3A%20Ikiyaga%20CLI%20sur%20Ikiyaga%20et%20Ikiyaga%20GUI.,-Si%20vous%20souhaitez).


Kugira ngo umenye vyinshi ku vyerekeye CoinJoin muri rusangi, ndabasigurira vyose muri iyi nkuru: [link](https://www.pandul.fr/post/ukoresha-CoinJoin-ku-Bitcoin).


### Gukoresha igikoresho ca Whirlpool.


Inyuma yo gukora CoinJoins na Whirlpool, ushobora gushaka kumenya urugero nyarwo rw’ubuzima bwite bw’ama UTXO yawe avunganye. Whirlpool Stat Tool iragufasha gukora ivyo mu buryo bworoshe. Ukoresheje iki gikoresho, urashobora kubara amanota y’imbere n’ay’inyuma y’ama UTXO yawe avunganye. Kugira ngo umenye vyinshi ku bijanye no kubara izo Anon Sets n’ingene zikora, ndagusavye gusoma iki gice: [ihuriro](https://www.pandul.fr/iposita/ugutahura-n'ugukoresha-CoinJoin-ku-Bitcoin#:~:umwandiko=perdre% 20ru%20ibanga%C3%A9.-,Anon%20Imigwi.,-Comme%20gusobanura%C3%A9%20pr%C3%A9c%C3%A9Igihano).


Ico gikoresho kirabanza gushirwa kuri RoninDojo yawe. Ubu rero, iboneka gusa kuri RoninCLI. Kugira ngo uyitangure uhereye kuri menyu nyamukuru, genda kuri:

**Igikoresho ca Samourai > Igikoresho ca Whirlpool**


Amabwirizwa y’ugukoresha azoboneka. Uhejeje, kanda urufunguzo urwo ari rwo rwose kugira ngo ushikire imirongo y'amabwirizwa:


![Whirlpool Stats Tool software home](assets/28.webp)


Igikoresho kizokwerekana:

**ivyo#/igihe>**


Kugira ngo usohoke muri iyi Interface usubire muri menu ya RoninCLI, ushiremwo itegeko:

```
quit
```


Kugira ngo dutangure, tuzoshiraho proxy kuri Tor kugira ngo dukure amakuru ya OXT n’ubuzima bwite bwose. Injira itegeko:

```
socks5 127.0.0.1:9050
```


Hanyuma ushire amakuru mu kigega kirimwo amafaranga yawe:

```
download 0001
```


**Iciyumviro:** subiriza `0001` kode y'idini ry'ikidengeri igushimisha.


Amakode y’idini ni aya kuri WST:



- Ivyuma 0.5: 05
- Ibice 0.05: 005
- Ibice 0.01: 001
- Ibice 0.001: 0001


![Downloading data from pool 0001 from OXT](assets/29.webp)


Amakuru amaze gukurwako, uyashiremwo itegeko:

```
load 0001
```


**Iciyumviro:** subiriza `0001` kode y'idini ry'ikidengeri igushimisha.


![Loading data from pool 0001](assets/30.webp)

Reka igikorwa co gushiramwo ibintu kibeho, bishobora gutwara iminota mikeyi. Amaze gushiramwo amakuru, wandike itegeko ry’amanota rikurikiwe na txid yawe (ikimenyetso c’ibikorwa) kugira uronke Anon Sets zayo:

```
score TXID
```


**Iciyumviro:** subiriza `txid` ikimenyetso c'ibikorwa vyawe.


![Printing the prospective and retrospective scores of the given TXID](assets/31.webp)


WST izoca yerekana amanota y’inyuma (Ibipimo vy’inyuma) ikurikiwe n’amanota y’imbere (Ibipimo vy’imbere). Uretse amanota y’ibice vya Anon, WST iraguha kandi igipimo c’ugukwiragira kw’ivyo usohora mu kidengeri bishingiye ku bice vya anon.


Urashobora kubona ko amanota y’ivyizigiro y’ivyo UTXO yawe ibarirwa ashingiye ku txid y’umuvumba wawe wa mbere, atari umuvumba wawe wa nyuma. Ku rundi ruhande, igiharuro c’inyuma c’umugwi wa UTXO giharurwa hakurikijwe txid y’ingendo ya nyuma.


Na none, nimba udatahura ivyo vyiyumviro vya Anon Sets, ndagusavye gusoma iki gice c’ingingo yanje ku CoinJoin aho ndasigura vyose mu buryo burambuye nkoresheje ibishushanyo: [https://www.pandul.fr/post/ugutahura-n'uwukoresha-CoinJoin-ku-Bitcoin#:~:umwandiko=perdre%20en%20ibanga%C3%A9.-,Imigwi%20Itamenyekana.,-Itangazo%20Isobanuro%A%A9%C9%320 (https://www.pandul.fr/post/ugutahura-n'uwukoresha-CoinJoin-ku-Bitcoin#:~:umwandiko=perdre%20en%20ibanga%C3%A9.-,Imigwi%20Itamenyekana.,-Itangazo%20Isobanuro%A%A9%C9%C2)


### Ukoresheje igiharuro ca Boltzmann.


Igiharuro ca Boltzmann ni igikoresho kigufasha kubara mu buryo bworoshe ibipimo bitandukanye vy’iterambere ku giciro ca Bitcoin, harimwo n’urugero rwaco rw’uburemere. Aya makuru yose azotuma ushobora kumenya urugero rw’ubuzima bwite bw’ibintu ugurisha no kumenya amakosa yose yoshobora kubaho. Ico gikoresho carashizweho mbere ku nzira yawe ya RoninDojo.


Kugira ngo uyironke ukoresheje RoninCLI, huza biciye kuri SSH, hanyuma ugende kuri menyu:

**Igikoresho ca Samourai > Ibarabara rya Boltzmann**


Imbere yo gusigura ingene woyikoresha kuri RoninDojo, nzobasigurira ico izo nzira zigereranya, ingene ziharurwa, n’ico zikoreshwa.


Ivyo bimenyetso birashobora gukoreshwa ku bikorwa vyose vy’ubudandaji vya Bitcoin, ariko biraryoshe cane cane mu kwiga uburyo ubudandaji bwa CoinJoin bumeze.


1. Ikimenyetso ca mbere giharurwa n’iyi porogarama ni umubare w’imigwi ishoboka. Bigaragara ku giharuro nk'"imigwi ya nb". Hakurikijwe agaciro k’ama UTXO, iki kigereranyo kigereranya umubare w’amakarata ashoboka kuva ku vyo yinjiza gushika ku vyo gusohoka.


**iciyumviro:** nimba utazi ijambo `UTXO`, ndagusavye gusoma iyi nkuru ngufi:


> Uburyo bwo gucuruza Bitcoin: UTXO, ivyinjizwa, n’ibisohoka.

Mu yandi majambo, iki kigereranyo kigereranya umubare w’insobanuro zishoboka z’ugucuruza kanaka. Nk'akarorero, igishushanyo ca Whirlpool 5x5 CoinJoin kizogira umubare w'imigwi ishoboka ingana na 1496:


![Schema of a Coinjoin transaction on kycp.org](assets/32.webp)


Inguzanyo: KYCP


2. Ikimenyetso ca kabiri giharurwa ni entropie y’igicuruzwa. Kubera ko umubare w’imigwi ishoboka ushobora kuba munini cane ku bijanye n’ugucuruza, umuntu arashobora guhitamwo gukoresha entropi mu kibanza cavyo. Entropie igereranya logarithme ibiri y’umubare w’imigwi ishoboka. Igishushanyo caco ni iki:



- E: entropie y’ugucuruza.
- C: umubare w’imigwi ishoboka y’ugucuruza.


**E = igitabo2(C)**


Mu mibare, logarithme ya kabiri (ishingiro rya 2) ni igikorwa gihinduka c'ububasha bw'igikorwa ca 2. Mu yandi majambo, logarithme binaire ya x ni ububasha umubare 2 utegerezwa kuduzwako kugira ngo ubone agaciro x.


Gutyo:


**E = igitabo2(C)**


**C = 2^E**


Ico kimenyetso kigaragazwa mu bice. Nk’akarorero, ng’aha niho habarwa entropie y’isoko rya Whirlpool 5x5 CoinJoin, n’umubare w’imigwi ishoboka twavuze mbere ungana na 1496:


**C = 1496**


**E = igitabo2(1496)**


**E = ibice 10.5469**


Rero, iyo nzira ya CoinJoin ifise entropie y’ibice 10,5469, ivyo bikaba ari vyiza cane.


Uko ico kigereranyo kiba hejuru, ni ko n’insobanuro zitandukanye z’ivyo bicuruzwa zirushiriza kuba nyinshi, ni ko rero ivyo bicuruzwa biba ibanga.


Reka dufate akandi karorero. Aha niho hari "classic" transaction ifise input imwe n'isohoka ribiri:


![Bitcoin transaction schema on oxt.me](assets/34.webp)


Ivyerekeye: OXT


Iyi nzira ifise insobanuro imwe gusa ishoboka:


**[(inp 0) > (Isohoka 0 ; Isohoka 1)]**


Rero entropie yayo izongana na 0:


**C = 1**,

**E = igitabo2(C)**,

**E = 0**


3. Ikimenyetso ca gatatu kigarurwa n'umubare wa Boltzmann ni ubushobozi bwa Tx bwitwa "Wallet Efficiency". Ico kimenyetso kiremesha gusa kugereranya igikorwa co kwinjiza n'igikorwa ciza kuruta ibindi vyose gishoboka mu ntunganyo imwe.


Ubu tuzozana iciyumviro c’uburemere burengeye ubundi bwose, bugereranya uburemere burengeye ubundi bwose bushobora gushikwako ku bijanye n’imiterere y’ugucuruza. Nk'akarorero, umubumbe wa Whirlpool 5x5 CoinJoin uzogira uburemere burengeye 10.5469. Ikigereranyo c’ubushobozi kigereranya iyo entropi nkuru n’entropi nyayo y’ugucuruza kw’inyungu. Igishushanyo caco ni iki:



- ER: Entropie nyayo igaragazwa mu bice.
- EM: Entropie nini cane ifise imiterere imwe yerekanwa mu bice.
- Ef: Ubushobozi bugaragazwa mu bice.


**Ef = ER - EM**


**Ef = 10,5469 - 10,5469**


**Ef = ibice 0**


Iki kigereranyo naco kigaragazwa nk'ijanisha, rero iyo formule iba:



- CR: Umubare nyawo w’imigwi ishoboka.
- CM: Umubare munini w’imigwi ishoboka ifise imiterere imwe.
- Ef: Ubushobozi bugaragazwa nk’ijanisha.


**Ef = CR/CM**


**Ef = 1496/1496**


**Ef = 100%**


Ubushobozi bwa 100% bisigura ko iyo nzira ifise ubuzima bwite buhambaye kuruta ubundi bwose ugereranije n’imiterere yayo.


4. Ikimenyetso ca kane giharuwe ni uburemere bw’uburemere bw’ibintu. Bituma dushobora gufatanya entropie n’ivyo twinjiza canke ivyo dusohora vyose. Ico kigereranyo gishobora gukoreshwa mu kugereranya ubushobozi hagati y’ibikorwa vy’ubudandaji vy’ubunini butandukanye.


Ibara ryayo ryoroshe cane: tugabanura entropie y’isoko n’umubare w’ibintu vyinjizwa n’ibisohoka biriho. Nk’akarorero, ku ndege ya Whirlpool 5x5 CoinJoin, twoba dufise:


ED: Uburemere bw’entropie bugaragazwa mu bice.

E: Entropie y’ibikorwa yerekanwa mu bice.

T: Umubare wose w’ibintu vyinjizwa n’ibisohoka mu gucuruza.


T = 5 + 5 = 10

ED = E / T

ED = 10,5469 / 10

ED = ibice 1.054


Amakuru ya gatanu atangwa n’umubare wa Boltzmann ni imbonerahamwe y’ibishoboka y’amasano hagati y’ibintu vyinjizwa n’ibisohoka. Iyi mbonerahamwe iraguha gusa ubushobozi (Boltzmann score) bw’uko inyungu yatanzwe ihuye n’isohoka ryatanzwe.


Nitwafata akarorero kacu na Whirlpool CoinJoin, imbonerahamwe y’ibishoboka yoba:


| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
|---------|----------|----------|----------|----------|----------|
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |


Aha turabona ko ikintu cose cinjira gifise amahirwe angana yo guhuzwa n’igisohoka cose.


Ariko rero, nitwafata akarorero k’ugucuruza gufise input imwe n’isohoka bibiri, vyosa n’ibi:


| Input | Output 0 | Output 1 |
| ----- | -------- | -------- |
| 0     | 100%     | 100%     |

Muri aka karorero, turashobora kubona ko ubushobozi bw’isohoka ryose rivuye mu nzira 0 ari 100%.


Uko ivyo bishoboka bigabanutse, ni ko n’urugero rw’ubuzima bwite rugenda rurakura.


6. Amakuru ya gatandatu aharurwa ni umubare w’amahuza y’ivy’ubuhinga. Igitigiri c’amahuza y’ivy’ubuhinga na co nyene kizotangwa. Ico kigereranyo kigaragaza umubare w’amahuza hagati y’ibintu vyinjizwa n’ibisohoka vy’isoko ry’ubudandaji ryatanzwe afise ubushobozi bwa 100%, bisobanura ko ataco bishobora guhakana.


Igipimo kigaragaza umubare w’amahuza y’ivy’ubuhinga mu gucuruza ugereranyije n’umubare wose w’amahuza.


Nk’akarorero, ugucuruza kwa CoinJoin Whirlpool nta sano ry’ugushinga intahe hagati y’ivyo yinjiza n’ivyo isohoka. Ico kigereranyo kizoba zero kandi igipimo naco kizoba 0%.


Ariko rero, ku bijanye n’ugucuruza kwa kabiri kwigishijwe (1 input na 2 outputs), ikimenyetso ni 2 kandi igipimo ni 100%.


Rero, iyo ico kimenyetso ari zero, vyerekana ko umuntu afise ubuzima bwiza.


None ko twarize ibimenyetso, reka turabe ingene twobiharura dukoresheje iyi porogarama. Kuva kuri RoninCLI, genda kuri menyu:

**Igikoresho ca Samourai > Ibarabara rya Boltzmann**


![Boltzmann Calculator software homepage](assets/35.webp)


Iyo porogarama imaze gutangura, ushiremwo transaction ID ushaka kwiga. Ushobora kwinjiza amafaranga menshi icarimwe mu kuyatandukanya n'agacamuzingi, hanyuma ukande enter:


![Enter a TXID to study on Boltzmann Calculator](assets/36.webp)


Ico giharuro kizoca kigarura ibimenyetso vyose twabonye mbere:


![Printing of Boltzmann Calculator data for this TXID](assets/37.webp)


Andika itegeko "Quit" kugira ngo usohoke muri porogaramu maze usubire mu rutonde rwa RoninCLI.


Kugira ngo umenye vyinshi ku bijanye n’igiharuro ca Boltzmann, ndagusavye gusoma izi ngingo:



- 85930984a159



- LaurentMT/e758767ca4038ac40aaf


### Guhuza Bisq.


Bisq ni urubuga rw’urunganwe rwa Exchange rugufasha kugura no kugurisha amafaranga y’ibiceri. Ikoreshwa na porogarama y’ibiro ikoreshwa kuri Tor kandi ishobora kugufasha gukoresha Exchange bitcoins utakeneye gutanga akaranga kawe.

Bisq icungera uguhanahana kw’urunganwe biciye ku buryo bw’imikono myinshi 2/2. Ushobora gukoresha iyi porogaramu n'uruzitiro rwawe bwite rwa RoninDojo kugira ngo ukoreshe neza ubuzima bwite bw'ivyo uhindura kandi wizere amakuru ava kuri Blockchain y'uruzitiro rwawe bwite.


Kugira ngo ubone porogarama ya Bisq, genda ku rubuga rwabo rwemewe: https://bisq.network/


Kugira ngo utangure gukoresha porogarama, ndagusavye gusoma iyi paji: https://bisq.network/gutangura/


Kugira ngo ubone urubuga rwo gufatanya na RoninDojo yawe, uzokenera gufatanya na RoninCLI biciye kuri SSH. Hanyuma ugende kuri menyu:

**Ibikorwa > Gucungera ibikorwa**


Injira ijambobanga ryawe, hanyuma ushire akamenyetso mu gasandugu karimwo urufunguzo rw'umwanya:

**[ ] Gushoboza Bisq Guhuza**


Wemeze ihitamwo ryawe. Reka node yawe ishiremwo, hanyuma utore Tor V3 Address kuva kuri:

**Ivyemezo > bitcoind**


Kopa igitabu ca Address munsi ya "Igitabo ca Bitcoin Igitabo ca daemon".


Ushobora kandi kugarura bitcoind Tor V3 Address yawe muri RoninUI Interface ukanda gusa kuri "Gucungera" mu gasandugu "Bitcoin core" ku "Igikoresho":


![Retrieve TorV3 Bitcoin Daemon address on RoninUI](assets/38.webp)


Kugira ngo uhuze node yawe uvuye kuri Bisq, genda kuri menyu:

**Imiterere > Amakuru y'urubuga**


![Access the node connection interface from the Bisq software](assets/39.webp)


Fyonda ku gipfukisho "Koresha amanode ya Bitcoin core". Hanyuma winjize Bitcoin TorV3 Address yawe mu gasandugu kagenewe, ufise ".igitunguru" ariko ata "http://".


![Box to enter the TorV3 address of your node in the Bisq software](assets/40.webp)


Subiramwo porogaramu ya Bisq. Node yawe ubu irahuye na Bisq yawe.


### Ibindi biranga.


Igikoresho cawe ca RoninDojo na co nyene kirimwo ibindi bintu vy’ishimikiro. Ufise ubushobozi bwo gucapura amakuru yihariye kugira ngo umenye neza ko afatwa mu muzirikanyi.


Nk’akarorero, rimwe na rimwe birashoboka ko Wallet yawe ifatanye na RoninDojo yawe itaronka ama bitcoins ari ayawe. Igitigiri ni 0 naho woba uzi neza ko ufise Bitcoin muri iyi Wallet. Hariho imvo nyinshi zishoboka zo kwiyumvira, harimwo n’ikosa mu nzira z’ugukomoka, kandi muri zo, birashoboka kandi ko urudodo rwawe rutariko rurabona amaderesi yawe.


Kugira ngo ukosore ivyo, ushobora kugenzura ko node yawe iriko irakurikirana xpub yawe ukoresheje "igikoresho ca xpub". Kugira ngo uyironke ukoresheje RoninUI, genda kuri menu:

**Gucungera > Igikoresho ca XPUB**


Injira muri xpub ifise ingorane hanyuma ukande kuri "Suzuma" kugira ngo ugenzure aya makuru.


![XPUB Tool from RoninUI](assets/41.webp)


Niba xpub yawe iriko irakurikiranywa n'uruzitiro, uzobona ibi bigaragara:


![XPUB Tool result showing successful analysis](assets/42.webp)


Suzuma ko amafaranga yose akoreshwa aboneka neza. Kandi, suzuma ko ubwoko bw'ivyo bivugwa buhuye n'ubwo Wallet yawe. Aha turabona ko node isobanura iyi xpub nk’ikomoka kuri BIP44. Niba ubwo bwoko bw'inkomoko butahuye n'ubw'i Wallet yawe, fyonda ku buto "Retype", hanyuma uhitemwo BIP44/BIP49/BIP84 bivanye n'ivyo uhisemwo:


![Change the derivation type of the studied xpub from RoninUI](assets/43.webp)


Niba xpub yawe idakurikiranywe n'uruzitiro rwawe, uzobona iyi skrini ikutumira kuyizana:


![Import an xpub with XPUB Tool on RoninUI](assets/44.webp)


Ushobora kandi gukoresha ibindi bikoresho vyo kwitaho:



- Igikoresho co Gucuruza: Kigufasha kwihweza ido n’ido ry’ugucuruza kinaka.
- Igikoresho ca Address: Kigufasha kugenzura ko Address yihariye iriko irakurikiranywa na Dojo yawe.
- Gusubira gupima amabuye: Ihatira urudodo rwawe gusubira gupima urutonde rw'amabuye yatowe.


Uzosanga kandi igikoresho ca "Push Tx" kuri RoninUI. Iragufasha gutangaza amakuru yashizweko umukono ku rubuga rwa Bitcoin. Bitegerezwa kwinjira mu buryo bw'icumi na gatandatu:


![Tool for broadcasting a signed transaction from RoninUI](assets/45.webp)


## Iciyumviro.


Twarabonye ingene twoshiramwo no gutangura n’iki gikoresho ciza cane ari co RoninDojo. Ni amahitamwo meza cane yo gukoresha node yawe bwite ya Bitcoin. Ni umuti ushikamye ushiramwo kandi ukaguma ushira ku gihe ibikoresho vyose bihambaye vy’umunya Bitcoin.


Nimba gukoresha terminal bitagutera ubwoba kandi nimba udakeneye ibikoresho bijanye na Lightning Network, rero RoninDojo yoshobora kugukwegera.


Niba ushobora, niwiyumvire gutanga intererano ku bategura porogarama bagukorera mu mwidegemvyo: https://donate.ronindojo.io/


Kugira ngo umenye vyinshi ku vyerekeye RoninDojo, ndagusavye kuraba amahuzu ari mu bikoresho vyanje vyo hanze biri aha hepfo.


### Ibindi bisomwa:



- Gutahura no gukoresha CoinJoin kuri Bitcoin.
- Imikorere ya Hash - igice kivuye mu gitabu ca interineti Bitcoin Demokarasi 1.
- Ivyo vyose ukeneye kumenya ku bijanye na Bitcoin passphrase.


### Ibikoresho vyo hanze:



- Urutonde rw'ibintu
- https://wiki.ronindojo.io/ru/inzu
- LaurentMT/e758767ca4038ac40aaf
- 85930984a159
- Urubuga rwa Boltzmann
- https://wiki.ronindojo.io/ru/gutegura/bisq
- urubuga rwa bisq/