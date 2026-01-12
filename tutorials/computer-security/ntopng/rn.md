---
name: Ntopng
description: Gukurikirana urubuga rwawe ukoresheje ntopng
---
![cover](assets/cover.webp)



___



*Iyi nyigisho ishingiye ku bintu vy’umwimerere vya Florian Duchemin vyasohowe kuri [IT-Connect](https://www.it-connect.fr/). Uruhusha [CC KURI-NC 4.0](ku rubuga rwacu/uruhusha/ku-NC/4.0/). Birashoboka ko hari ivyo bahinduye mu canditswe c’intango.*



___



## I. Ugushikiriza



**Yaba ari ugusuzuma ingene urubuga rugenda, kugira ngo ubone ishusho itomoye y’ingene ikoreshwa canke kugira ngo ubone imibare y’ibikorwa, kugenzura ingene urubuga rugenda ni igice gihambaye c’urubuga rw’ishirahamwe**. Bifasha kwitega amahinduka mu bikorwa remezo kandi bifasha kumenya ko abakoresha bakoresha neza (bizwi kandi nka QoE ku *Uburyo bw’Ubumenyi*, bitandukanye na QoS).



Kugira ngo ivyo bishoboke, hari ubuhinga bwinshi n’amaporogarama/amasezerano menshi. Nk’akarorero, Netflow, yateguwe na Cisco, irashobora gukoreshwa mu kugarura imibare y’uruja n’uruza rwa IP iva kuri Interface, ariko ikoreshwa ryayo rigarukira ku bikoresho bihuye.



Ni co gituma muri iyi nyigisho ngiye kubamenyesha **Ntop** no kukwereka ingene woyikoresha mu bikorwa remezo vyawe kugira ngo ukomeze gukurikirana uko ukoresha urubuga rwawe.



Ntop ni porogaramu yuguruye ishobora gushirwa ku mashine yose ya Linux. Ni ubuntu kandi ushobora gukusanya amakuru akurikira:





- Ikoreshwa ry'ubwaguke bw'umurongo
- Abaguzi bakuru
- Ibibanza vy'ingenzi
- Amasezerano yakoreshejwe
- Ibikoresho vyakoreshejwe
- Ivyambu vyakoreshejwe
- N'ibindi.



Ubu ryahinduwe izina **Ntopng (Ivyaruka Bishasha)**, ritanga ibikorwa vyinshi vy’ishimikiro ku buntu. Verisiyo y’ubudandaji iraboneka kandi, ishobora gutuma imburi zitunganijwe zirungikwa hanze muri porogarama y’ubwoko bwa SIEM, canke uruja n’uruza rucungururwa n’amategeko asobanuwe ataco akoresheje.



## II. Ibisabwa



Gushiramwo sonde ya Ntop biratandukanye bivanye n’ibikoresho n’ibidukikije. Rero sinzobaha intambwe ku yindi uburongozi hano, ariko nzobabwira uburyo butandukanye bushoboka.



### A. Uburyo bwo mu bwato



Niba ufise pfSense, OPNSense canke Endian umuriro uriko urakora, canke mbere n’ikibanza co gukoreramwo ca Linux gifise NFTables, inkuru nziza! Ushobora gushiramwo Ntopng directement ugatangura kugenzura interfaces zawe.



Ivyiza vy’ubu buhinga ni uko budasaba ibindi bikoresho vy’inyongera. Ku rundi ruhande, birongereza ikoreshwa ry’ibikoresho, rero urabe ko ufise ibikoresho bihagije canke VM y’ubunini buhagije (minimum 2 cores na 2BG RAM).



### B. Uburyo bwa TAP / SPAN



A **tap** ni **igikoresho c’urubuga gisubiramwo uruja n’uruza ruca muri rwo kikarurungika ku kindi gikoresho.** Inyungu y’iki gikoresho ni uko kitasaba guhindura ibikorwa remezo biriho, kandi gishobora gushirwa aho hose kugira ngo kigenzure ibice vy’urubuga vyihariye, canke hagati y’umurongo w’uruja n’uruza n’uruja n’uruza rwa Internet/from kugira ngo gisuzume.



Intambamyi nini y’ubwo bwoko bw’ibikoresho ni igiciro cavyo. Mu mihora ya Gigabit y’ubu, tap passive ntishobora gufata neza uruja n’uruza rw’imihora, rero ukeneye igikoresho gikora kigura nk’amayero 200 (minimum).



Uburyo bwa **SPAN**, buzwi kandi nka **port mirroring**, bukoreshwa n'umuhinduzi kugira ngo urungike uruja n'uruza kuva ku cambu kimwe gushika ku kindi. Ubu ni bwo buryo nkunda cane, kuko bworoshe gushinga kandi, nk’ugutera, bugufasha gukurikirana igice c’urubuga canke urubuga rwose uko ushaka. Ariko rero, hariho ingorane zibiri: iyo switch itegerezwa gushiramwo iyo nzira, kandi gukoresha iyo switch birashobora kwongera umuzigo w’ivyo bikoresho ku switch.



### C. Uburyo bwa router



Birashoboka cane gutera router munsi ya Linux ukayishirako ntopng. Intambamyi imwe gusa y'ubu buryo ni uko buzohindura urubuga rwawe, haba adresse yarwo yo mu mutima, canke adresse iri hagati ya router yawe "y'ukuri" n'iyo uriko wongerako.



Iciyumviro: ku basomyi b'ingingo [Rema umurongo wa Wifi ukoresheje Raspberry Pi na RaspAP](https://www.it-connect.fr/) birashoboka cane gushiramwo ntopcurate statistics kuri Rpi yawe kugira ngo ubone!



### D. Uburyo bw'ikiraro



Iyindi nzira iryoshe ni ugukoresha **imashini ya Linux mu buryo bw’ikiraro.** Ishizwe hagati y’ibikoresho bibiri, ivyo bituma uruja n’uruza rwose rufatwa ataco ruhinduye mu gutunganya ibikorwa remezo canke ibikoresho vyavyo. Nk’uko imashini ya kera ishobora gukora ako kazi, igiciro c’ubwo buryo na co nyene kirashobora gukwegera. Zirikana ko kugira ngo igikoresho kibe ciza, gikwiye kuba gifise amakarita atatu y’urubuga, abiri ari mu buryo bw’ikiraro, rimwe ryo gushika kuri Interface na SSH. Birashoboka gukoresha amakarita abiri gusa, ariko rero ubuyobozi bw'igikoresho nabwo buzofatwa...



Rero ni **iyi mode ya nyuma ngiye gukoresha**. Kubera imvo ngirakamaro, nzoba ndiko nkoresha imashini ziboneka mu kwerekana, ariko uburyo buraguma ari bumwe ku mashini zigaragara.



## III. Gutegura itohoza n'ikiraro ca Interface



Ku bijanye n'itohoza, ntora imashini **Debian 11** mu gushiramwo bike.



Intambwe ya mbere, yama ari imwe, guhindura:



```
apt-get update && apt-get upgrade
```



Hanyuma ushiremwo **bridge-utils**, izotuma dushobora gukora ikiraro cacu:



```
apt-get install bridge-utils
```



Iyo umaze gushiramwo, ikintu ca mbere co kwitwararika ni izina ry’ubu ry’amakarata yacu y’urubuga. Munsi ya Debian, iri zina rishobora gufata uburyo bwinshi, kandi tuzorikenera mu gutunganya.



Itegeko ryoroshe **ip add** rizogarura igisohoka n'aya makuru:



![Image](assets/fr/016.webp)



Aha, mbona imirongo 3:





- Lo**: iyi ni yo nzira y’inyuma Interface; ni Interface y'ukuri "izunguruka" hejuru y'ibikoresho. Mu bisanzwe, iyo Interface, Address yayo ni 127.0.0.1 (naho Address iyo ari yo yose iri muri 127.0.0.0/8 izokora, kuko iyo nzira igenewe iyo ntumbero) ikoreshwa mu gukorana n’ibikoresho ubwavyo. Niba warashizeho urubuga ku kibanza cawe co gukoreramwo (ukoresheje WAMPP, nk'akarorero), birashoboka ko warakoresheje "*localhost*" Address igihe kimwe canke ikindi kugira ngo ugaragaze urubuga rwakiriwe ku mashine yawe bwite. Iri zina ry'umushitsi rifitaniye isano na Address 127.0.0.1 rero n'ivy'inyuma vya Interface.
- ens33**: iyi ni Interface yanje ya mbere, yaronse Address hano ivuye kuri DHCP yanje
- ens36**: Interface yanje ya kabiri.



None ko mfise amakuru yose, ndashobora guhindura dosiye */etc/network/interfaces* kugira ngo nkore ikiraro canje. Ehe uko bisa ubu (bishobora guhinduka):



```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug ens33
iface ens33 inet dhcp
# This is an autoconfigured IPv6 interface
iface ens33 inet6 auto
```



Igice ca mbere kijanye n'ivyo Interface yanje y'inyuma, iyo ntazoba ndiko ndakorako, ikurikirwa na Interface ens33. Ivyo bihinduwe birimwo kwongerako Interface yanje ya kabiri (ens36) no gutunganya ikiraro n’izo nzira zibiri:



```
# The primary network interface
auto ens33
iface ens33 inet manual

#The secondary network interface
auto ens36
iface ens36 inet manual
```



Akira insobanuro zimwe zimwe z’ayo mahinduka ya mbere:





- auto **Interface**: izokwihuta "gutangura" Interface ku gutangura kwa sisitemu
- iface *Interface* inet **igitabo**: gukoresha Interface ata IP Address. Nk'ijambo ry'ingenzi "static" gusobanura IP idahinduka Address canke "dhcp" gukoresha aderesi zihinduka



Ivyo bihindurwa birabandanya:



```
# Bridge interface
auto br0
iface br0 inet static
address 192.168.1.23
netmask 255.255.255.0
gateway 192.168.1.1
bridge_ports ens33 ens36
bridge_stp off
```



Aha na ho nyene, insobanuro nkeyi:





- iface br0 inet idahinduka**: aha nasobanuye ikiraro canje ca Interface (*br0*) n'ikiraro kidahinduka Address.
- Address, igipfukisho c'urubuga, irembo**: amakuru yerekeye aderesi y'urubaho
- bridge_ports**: ibigaragara bizoshirwa mu kiraro
- bridge_stp**: Igiti c'Igiti gikoreshwa igihe gihuza ama switch kugira ngo umenye amahuza atari ngombwa no kwirinda inzira. Kubera ko ikiraro gishobora kwinjizwa hagati y’inzira zibiri z’uruja n’uruza, gishobora kuba isoko y’uruzitiro, ni co gituma bishoboka ko iyo porotokole ishoboka. Sinkeneye hano, rero ndiko ndayizibira.



Bika ivyo wahinduye hanyuma wongere utangure urubuga:



```
systemctl restart networking
```



Kugira ngo usuzume amahinduka, ugaragaza igisubizo c'itegeko ryo **ip** add kandi:



![Image](assets/fr/021.webp)


Ushobora kubona neza **Interface yanje nshasha "*br0*" n'IP Address nayihaye.** Ushobora kandi kubona ko interfaces zanje zibiri z'umubiri ari "UP", ariko nta IP Address zifise.



## IV. Gushiramwo NtopNG



None ko sonde yacu ishobora guhonya uruja n’uruza hagati ya network yanje na router, igisigaye ni ugushiramwo ntopng. Kugira ngo ubikore, banza uhindure dosiye */etc/apt/sources.list* wongereko **contrib** ku mpera y'umurongo wose utangura na **deb** canke **deb-src**.



Ku mburabuzi, inkomoko z'amapaki zirimwo gusa amapaki yubahiriza DFSG (*Ingingo ngenderwako za Porogarama z'Ubuntu za Debian*), zigaragazwa n'ijambo ry'ingenzi **rikuru**. Ushobora kandi kwongerako aya masoko:





- contrib**: amapaki arimwo porogaramu yubahiriza DFSG, ariko ikoresha ibishingiyeko bitari mu ishami **rikuru**
- ntabwo ari ubuntu**: irimwo amapaki adakurikiza DFSG



Akarorero k'umurongo muri /n'ibindi/apt/amasoko.urutonde:



```
deb http://deb.debian.org/debian/ bullseye main
```



Rero nzokwongerako gusa ijambo **contrib** ku mirongo nk'iyi.



Intambwe zisigaye ziri ku rubuga rwa [NtopNG](https://packages.ntop.org/apt/) aho, kuri Debian 11, ukeneye kwongerako inkomoko za Ntop kugira ngo uzozishiremwo mu gihe kizoza. Ukwo kwongerako kwikora hakoreshejwe a:



```
wget https://packages.ntop.org/apt/bullseye/all/apt-ntop.deb
apt install ./apt-ntop.deb
```



Hanyuma haza igice nyaco co gushiramwo:



```
apt-get clean all
apt-get update
apt-get install ntopng
```



Itegeko rya mbere rifuta ububiko bw'umucungerezi w'amapaki ya apt. Ubwa kabiri buzohindura urutonde rw’amapaki ubwa gatatu buzoshiramwo NtopNG.



Inyuma yo gushiramwo, **porogaramu ya NtopNG iraboneka ku port 3000 y'imashini ya Debian**. Rero kuri jewe ni `http://192.168.1.23:3000`



![Image](assets/fr/022.webp)



Paje y'intango ya NtopNG



Ijambobanga ry’injira n’iry’ibanga ry’imbere ryerekanywe, rero ico ubwirizwa gukora n’ukuvyinjiramwo!



## V. Gukoresha NtopNG



Iyo winjiye ubwa mbere, ikintu ca mbere uzosabwa gukora ni uguhindura ijambobanga ry’umuyobozi n’ururimi. Ikibabaje ni uko igifaransa si kimwe muri vyo.



Uca ushika ku rubaho:



![Image](assets/fr/023.webp)



Urubaho rwa NtopNG



Ntumenyerere uwu! Niwabona akazu k'umuhondo kari hejuru y'ibarabara, uzobona iryo rungane rigira riti: "*Uruhusha rurahera muri 04:57*". Ku mburabuzi, gushiramwo bitangura kugerageza verisiyo yuzuye ya NtopNG, ariko mu gihe (cane) gito. Igihe iki "guharura" kigeze, verisiyo *y'umuryango* irakora maze urupapuro rw'ibarabara rurahinduka:



![Image](assets/fr/024.webp)



Igikoresho gishasha c'umuryango wa NtopNG



Ico mbere wokora ni **kugenzura ko Interface ibereye iriko iratega yompi**. Mu mfuruka yo hejuru ibubamfu, urutonde rw’ibikoresho biboneka rushobora kugufasha guhitamwo Interface dushaka hano: br0.



![Image](assets/fr/025.webp)



Interface guhitamwo



Idirisha rishasha ryerekana "Top Flaw Talkers", ni ukuvuga ibikoresho bivugana cane. Aha mfise gusa ibibanza bibiri bigaragara:



![Image](assets/fr/026.webp)



**Ivyakira vy'inkomoko biboneka ibubamfu, aho bishika iburyo ** Ivyo bigufasha kubona mu ciyumviro ikoreshwa ry'uburebure bwose bw'umurongo n'ivyakira vyose, no kubona muri rusangi uruja n'uruza rw'urubuga. Ivyo si bibi, ariko turashobora kuja kure...



Iyo nfyondeye kuri "*Hosts*", nk'akarorero, nca mbona igicapo kigaragaza ubushobozi bwo kohereza n'ukwakira umushitsi wese ari ku rubuga rwanje. Aha nk’akarorero, ndashobora kubona ko 192.168.1.37 yonyene ari yo ifata 80% vy’uruja n’uruza rwanje:



![Image](assets/fr/027.webp)



Iyo nfyonda kuri IP Address y'umushitsi ariko arabazwa, nca nsubira kuri paji y'incamake:



![Image](assets/fr/028.webp)



Nshobora kubona nk’akarorero ko ari imashini ya VMWare (mu kwemera EGO ya MAC Address yanje), ko yitwa DESKTOP-GHEBGV1 (rero nta gukeka ko ari umushitsi wa Windows) KANDI mfise **imibare ku mapakete yakiriwe n’ayoherejwe, hamwe n’ingero y’amakuru**.



Uzobona kandi urutonde rushasha ruri hejuru y'iyi ncamake. Ndagusavye ukande kuri "**Apps**" kugira ubone igituma abantu benshi baza:



![Image](assets/fr/017.webp)


Ha, bisa n’uko twaronse inyishu! Ku gicapo kiri ibubamfu, **turabona ko 76,6% vy’uruja n’uruza rwayo biva kuri ... Windows Update**, rero uyu mushitsi ariko arakuraho ivyagezwe!



NtopNG ikoresha ubuhinga bwitwa DPI ku *Deep Packet Inspection*, buyishoboza gushiramwo mu migwi uruja n’uruza rw’urubuga rwose no gusobanura igikorwa (canke umuryango w’ibikorwa) kiri inyuma yaco.



Kugira ngo nshire ahabona, ndatanguza amasanamu ya YouTube ku mushitsi wanje:



![Image](assets/fr/018.webp)



**Ivyo binyabiziga vyaciye bimenyekana ubwo nyene bica bishirwa mu migwi!**



Iciyumviro: kubera imvo zigaragara, ubwo bwoko bwa porogarama burashobora gutuma haba ibibazo vy’ubuzima bwite, rero urabe maso mu kuyikoresha mu buryo bubereye. Iyumvire kandi ko bishoboka **gutuma ibisubizo bitamenyekana**, uburyo bushobora kuboneka muri **Imiterere > Ivyo ukunda > Ibindi** kandi vyitwa "**Mask Host IP Address**".



## VI. Ibimenyetso n'imburi



NtopNG nayo irashobora gutanga imburi z’umutekano ku mafunguro amwe amwe. Ivyo ushobora kubisanga muri **Alerts**, ku bendera y'ibubamfu. Aha nk’akarorero, mfise imburi 2851 zose hamwe, zigabanywemwo uburemere butandukanye: Itangazo, Imburi n’Ikosa.



![Image](assets/fr/019.webp)



Reka turabe ivyibutsa vy’ugunegura cane, mfise 17 muri vyo!



Ufyondeye kuri uwo mubare urabona ido n’ido ry’ivyo bimenyetso. Nta kintu giteye ubwoba kiri hano, ni ikintu ciza c’ikinyoma, gukuraho ibintu bishasha bishirwa mu rwego rw’uguhindura dosiye zibiri mu mugezi wa HTTP, ivyo bishobora vy’ukuri gusobanura igitero.



![Image](assets/fr/020.webp)



Ariko rero, nk’uko ndiko ndakoresha verisiyo y’ubuntu, sinshobora gukuraho amadomaine canke abashitsi ari bo batera imburi, rero uzobwirizwa kuguma uzibona kugira ngo ntubuze ikintu giteye amaganya cane. NtopNG izotanga imburi za generate iyo:





- Dosiye zibiri zikurwa kuri HTTP
- Ugukekwako uruja n'uruza rwa DNS
- Gukoresha icuma kidasanzwe
- Gutahura urushinge rwa SQL
- Inyandiko zijanye n'urubuga (XSS)
- N'ibindi.



## VII. Iciyumviro



Muri iyi nyigisho, twabonye **ingene twoshiraho probe na NtopNG** bidushoboza **gusuzuma uruja n’uruza rw’urubuga rwacu** kugira ngo tubone ikoreshwa rya protocole n’aho umushitsi wese aba, ariko kandi tubone uruja n’uruza ruteye amakenga.



Ikibabaje, sinshobora gutangaza ibiranga vyose n’ibishoboka vyose muri iyi nkuru, ariko ntutinye gutohoza!



Uwo muti ushobora gushirwa mu ngiro ubudasiba mu bikorwa remezo vy’ikigo. NtopNG ishobora kandi kwohereza ibisubizo mu rutonde rw’amakuru rwa InfluxDB, bikagufasha kwikorera ibiharuro vyawe n’igikoresho c’uwundi muntu nka Graphana.