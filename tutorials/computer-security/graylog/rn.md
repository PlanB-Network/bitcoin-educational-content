---
name: Graylog
description: Gushira hamwe no gusuzuma inyandiko zawe mu buryo bworoshe
---
![cover](assets/cover.webp)



___



*Iyi nyigisho ishingiye ku bintu vy’umwimerere vya Florian BURNEL vyasohowe kuri [IT-Connect](https://www.it-connect.fr/). Uruhusha [CC KURI-NC 4.0](ku rubuga rwacu/uruhusha/ku-NC/4.0/). Birashoboka ko hari ivyo bahinduye mu canditswe c’intango.*



___



## Gukoresha Graylog kuri Debian 12



### I. Ugushikiriza



Graylog ni umuti w'inkomoko yuguruye "log sink" wagenewe gushiramwo, kubika no gusuzuma ibitabo biva ku mashini yawe n'ibikoresho vy'urubuga mu gihe nyaco. Muri iyi nyigisho, tuzomenya ingene twoshiramwo verisiyo ya Graylog ku buntu ku mashini ya Debian 12!



Mu nzira y’amakuru, **server** yose, yaba ikoresha **Linux** canke **Windows**, na **igikoresho cose c’urubuga** (switch, router, firewall, n’ibindi...) **bitanga amakuru yaco**, abitswe aho hantu. Kubera ibitabo bibitswe ahantu ku mashini yose, ugusesangura ibintu n’uguhuza biragoye cane... Aho niho **Graylog** yinjira.Izokora nk’**log sink**, bisobanura ko **imashini zawe zose zizoyirungikira ibitabo vyazo** (biciye muri syslog, nk’akarorero). Graylog izoca **ibika kandi ikoreshe urutonde rw'ivyo bitabo**, mu gihe izoguha uburenganzira bwo gukora ubushakashatsi kw'isi yose no guhingura imburi.



Graylog ni igikoresho co gusesangura no kugenzura gituma vyoroha kumenya inyifato iteye amakenga n’ingorane zitandukanye (ugushikama, ubushobozi, n’ibindi).




![Image](assets/fr/034.webp)



**Iciyumviro: verisiyo y'ubuntu, Graylog Open, si SIEM nk'uko Wazuh ari, cane cane kuko idafise ibikorwa vy'ukuri vyo kumenya abaje mu nzu.**



### II. Ibisabwa



**Ikirundo ca Graylog** gishingiye ku **bice vyinshi** tuzokenera gushiramwo no gutunganya. Aha, tuzoshira ibice vyose kuri server imwe, ariko birashoboka gukora amatsinda ashingiye ku nzira nyinshi maze tugatanga inshingano kuri server nyinshi. Kubera intumbero z'iyi nyigisho, tuzoba turiko turashiramwo **Graylog 6.1**, verisiyo nshasha gushika ubu.





- MongoDB 7**, ni verisiyo y'ubu igenewe Graylog (ubuke 5.0.7, ubunini 7.x)
- Gushaka gufungura**, inkomoko yuguruye Fork y'ubushakashatsi bukomeye bwakozwe na Amazon (ubuke 1.1.x, ubunini 2.15.x)
- GufunguraJDK 17**



**Serveri ya Graylog** iriko irakora kuri **Debian 12**, ariko gushiramwo birashoboka ku bindi bikoresho, harimwo na Docker. Iyi mashini y’ubuhinga bwa none ifise **8 GB RAM** na **256 GB disk space**, kugira ngo ibe n’ibikoresho bihagije vy’ibice vyose (ahandi ho ivyo bishobora kugira ingaruka zikomeye ku bikorwa). Ariko rero, ivyo ndabitanga nk'indongozi y'agahomerabunwa, kuko **ubunini bw'ubwubatsi bwa Graylog buvana n'ingero y'amakuru azokoreshwa**. Graylog ishobora gukora 30 MB canke 300 MB z’amakuru ku musi, hamwe n’amakuru 300 GB ku musi... Ni **umuti ushobora guhindurwa** ushobora gukora **terabytes z’amakuru** (raba [iki page](ubu/gutegura_ugushirwaho kwawe/gutegura_ugushirwaho_kwawe.html?tocpath=Gutegura%20Ugushirwaho kwawe%7C_____0)).



![Image](assets/fr/032.webp)



Inkomoko: Graylog



Imbere yo gutangura gutunganya, shira IP Address idahinduka ku mashini ya Graylog maze ushiremwo ivyagezwe bishasha. Raba neza ko ushizeho isaha y'imashini yo mu karere kandi usobanure umukozi wa NTP wo guhuza itariki n'isaha. Ehe itegeko ryo kwiruka:



```
sudo timedatectl set-timezone Europe/Paris
```



**Iciyumviro:** Gushiramwo OpenSearch ni ubusabe iyo ukoresheje **Igiharuro c'amakuru ya Graylog** aho.



### III Intambwe ku yindi gushiramwo Graylog



Reka dutangure mu guhindura ububiko bw’amapaki no gushiramwo ibikoresho dukeneye ku vyo tuzoza.



```
sudo apt-get update
sudo apt-get install curl lsb-release ca-certificates gnupg2 pwgen
```



![Image](assets/fr/030.webp)



#### A. Gushiramwo MongoDB



Ivyo bimaze gushika, tuzotangura gushiramwo MongoDB. Gukuraho urufunguzo rwa GPG rujanye n'ububiko bwa MongoDB:



```
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```



Hanyuma wongere ububiko bwa MongoDB 6 ku mashini ya Debian 12:



```
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```



Ibikurikira, tuzosubiramwo ububiko bw'amapaki maze tugerageze gushiramwo MongoDB:



```
sudo apt-get update
sudo apt-get install -y mongodb-org
```



MongoDB ntishobora gushirwaho kubera ko hariho ivyifashe: **libssl1.1**. Tuzobwirizwa gushiramwo iyi package n'amaboko imbere y'uko tubandanya, kuko Debian 12 ntayo ifise mu bubiko bwayo.



```
Les paquets suivants contiennent des dépendances non satisfaites :
mongodb-org-mongos: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
mongodb-org-server: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
E: Impossible de corriger les problèmes, des paquets défectueux sont en mode « garder en l'état ».
```



Tugiye gukuraho umurongo wa DEB witwa "**libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb**" (verisiyo nshasha) n'itegeko rya **wget**, hanyuma tuwushiremwo n'itegeko rya **dpkg**. Ivyo bituma haba amabwirizwa abiri akurikira:



```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
```



![Image](assets/fr/028.webp)



Gusubira gutangura gushiramwo MongoDB:



```
sudo apt-get install -y mongodb-org
```



Hanyuma wongere utangure serivisi ya MongoDB maze uyishoboze gutangura ubwayo igihe umukozi wa Debian atanguye.



```
sudo systemctl daemon-reload
sudo systemctl enable mongod.service
sudo systemctl restart mongod.service
sudo systemctl --type=service --state=active | grep mongod
```



MongoDB imaze gushirwamwo, turashobora kuja ku gushiramwo igice gikurikira.



#### B. Gushiramwo ubushakashatsi bufunguye



Reka tugende ku gushiramwo OpenSearch kuri server. Itegeko rikurikira ryongera urufunguzo rw'umukono ku mapaki ya OpenSearch:



```
curl -o- https://artifacts.opensearch.org/publickeys/opensearch.pgp | sudo gpg --dearmor --batch --yes -o /usr/share/keyrings/opensearch-keyring
```



Hanyuma wongereko ububiko bwa OpenSearch kugira ngo dushobore gukuraho iyo package na **apt** inyuma:



```
echo "deb [signed-by=/usr/share/keyrings/opensearch-keyring] https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable main" | sudo tee /etc/apt/sources.list.d/opensearch-2.x.list
```



Kuvugurura ububiko bwawe:



```
sudo apt-get update
```



Hanyuma **shiramwo OpenSearch**, witwararike **gusobanura ijambobanga ry'imbere ry'intangamarara yawe ya Admin**. Aha, ijambobanga ni "**IT-Connect2024!**", ariko usubirizeho ijambobanga rikomeye. **Irinde amajambo y'ibanga agoyagoya** nka "**P@ssword123**" kandi ukoreshe nibura inyuguti **8** zifise nibura inyuguti imwe y'ubwoko bumwe bumwe (inyuguti nto, nini, umubare n'inyuguti idasanzwe), ahandi ho hazoba ikosa mu mpera y'ugushiraho. **Ivyo ni ivyangombwa kuva mu Bushakashatsi Bufunguye 2.12.**



```
sudo env OPENSEARCH_INITIAL_ADMIN_PASSWORD=IT-Connect2024! apt-get install opensearch
```



Urasabwe kwihangana mu gihe co gushiramwo...



Niwaheza, fata umwanya wo gukora ivy’ugutunganya bikeyi. Gufungura dosiye y'imiterere mu buryo bwa YAML:



```
sudo nano /etc/opensearch/opensearch.yml
```



Igihe dosiye yuguruye, shiraho amahitamwo akurikira:



```
cluster.name: graylog
node.name: ${HOSTNAME}
path.data: /var/lib/opensearch
path.logs: /var/log/opensearch
discovery.type: single-node
network.host: 127.0.0.1
action.auto_create_index: false
plugins.security.disabled: true
```



Iyi nzira ya OpenSearch yagenewe gushinga urudodo rumwe. Aha hariho insobanuro z'ibipimo bitandukanye dukoresha:





- cluster.name: graylog: iyi parametere yita izina ry'itsinda ry'Ishakisha ry'Ubushakashatsi n'izina "**igitabo c'imvi**".
- node.name: **${HOSTNAME}**: izina ry'urudodo rishirwaho kugira ngo rihure n'iry'imashini ya Linux yo mu karere. Naho twoba dufise urudodo rumwe gusa, birahambaye ko turuha izina ryiza.
- inzira.amakuru: /var/lib/gufungura ubushakashatsi: iyi nzira igaragaza aho OpenSearch ibika amakuru yayo ku mashini yo mu karere, muri iki gihe muri "**/var/lib/gufungura ubushakashatsi**".
- inzira.ibitabo: /var/ibitabo/ugufungura ubushakashatsi: iyi nzira isobanura aho amadosiye y'inyandiko y'ubushakashatsi abikwa, hano muri "**/var/ibitabo/ugufungura ubushakashatsi**".
- discovery.type: urudodo rumwe: iyi parametere itunganiriza OpenSearch gukorana n'urudodo rumwe, ni co gituma uguhitamwo "**urudodo rumwe**".
- network.host: 127.0.0.1: iyi ntunganyo ituma OpenSearch yumviriza gusa ku nzira yayo ya Interface, ivyo bikaba bihagije kuko iri kuri server imwe na Graylog.
- action.auto_create_index: false**: mu guhagarika urutonde rwikora, OpenSearch ntizokwikora urutonde iyo inyandiko yoherejwe ata rutonde ruriho.
- plugins.security.disabled: true**: iyi nzira izibira umutekano wa OpenSearch, bisobanura ko ata kwemeza, gucunga uburenganzira canke gukingira amakuru. Iyi nzira izigama umwanya iyo ushiraho Graylog, ariko ikwiye kwirindwa mu gukora (raba [iyi paji](https://opensearch.org/docs/1.0/umutekano-plugin/index/)).



Hariho amahitamwo asanzwe ariho, rero ukeneye gusa gukuraho "#" kugira ngo uyakoreshe, hanyuma ugaragaze agaciro kawe. Niba udashobora kuronka uburyo, ushobora kubumenyesha ataco uhinduye ku mpera y'idosiye.



![Image](assets/fr/023.webp)



Bika kandi ufunge iyi dosiye.



#### C. Gutunganya Java (JVM)



Ukeneye guhindura Java Virtual Machine ikoreshwa na OpenSearch kugira ngo ushobore gutunganya umubare w’ububiko iyi serivisi ishobora gukoresha. Guhindura dosiye y'imiterere ikurikira:



```
sudo nano /etc/opensearch/jvm.options
```



Hamwe n’imiterere ishizweho hano, **OpenSearch izotangura n’ububiko bwa 4 GB kandi ishobora gukura gushika kuri 4 GB**, rero nta guhinduka kw’ububiko kuzoba mu gihe c’ibikorwa. Aha, ivy’ugutunganya bifata mu muzirikanyi ko imashini y’ivy’impwemu ifise **8 GB RAM** yose hamwe. Ivyo bipimo vyose bitegerezwa kuba bifise agaciro kamwe. Ivyo bisigura gusubirira imirongo:



```
-Xms1g
-Xmx1g
```



N’iyi mirongo:



```
-Xms4g
-Xmx4g
```



Aha niho hari ishusho y'ihinduka rizokorwa:



![Image](assets/fr/022.webp)



Funga iyi dosiye umaze kuyibika.



Ikindi, turakeneye kugenzura imiterere y'umurongo "**max_map_count**" mu ntumbero ya Linux. Isobanura umupaka w'ibibanza vy'ukwibuka vyashizwe ku ikarita ku nzira, kugira ngo bishobore gushitsa ivya nkenerwa vy'ikoreshwa ryacu. **OpenSearch**, nka **Elasticsearch**, irasaba gushiramwo aka gaciro kuri "262144" kugira ngo wirinde amakosa yo gucunga ububiko.



Mu ngingo ngenderwako, ku mashini ya Debian 12 iherutse gushirwaho, agaciro karasanzwe ari ukuri. Ariko reka tuvyisuzume. Gukoresha iri tegeko:



```
cat /proc/sys/vm/max_map_count
```



Niwabona agaciro katari "**262144**", koresha itegeko rikurikira, ahandi ho ntaco bimaze.



```
sudo sysctl -w vm.max_map_count=262144
```



Ubwa nyuma, fungura OpenSearch gutangura ubwayo maze utangure serivisi ijana.



```
sudo systemctl daemon-reload
sudo systemctl enable opensearch
sudo systemctl restart opensearch
```



Niwerekana uko system yawe imeze, ushobora kubona igikorwa ca Java gifise 4 GB RAM.



```
top
```



![Image](assets/fr/029.webp)



Intambwe ikurikira: ugushiraho Graylog yari imaze igihe kirekire irindiriwe!



#### D. Gushiramwo Graylog



Kugira ngo **ushiremwo Graylog 6.1** muri verisiyo yayo nshasha, koresha aya mabwirizwa 4 akurikira kugira ngo **ushiremwo Graylog Server**:



```
wget https://packages.graylog2.org/repo/packages/graylog-6.1-repository_latest.deb
sudo dpkg -i graylog-6.1-repository_latest.deb
sudo apt-get update
sudo apt-get install graylog-server
```



Ivyo nivyashika, turakeneye guhindura bimwe mu mitunganyirize ya Graylog imbere y’uko tugerageza kuyitanguza.



Reka dutangure dutunganye aya mahitamwo abiri:





- password_secret**: iyi parameter ikoreshwa mu gusobanura urufunguzo rukoreshwa na Graylog kugira ngo ikingire ububiko bw'amajambo banga y'abakoresha (mu mpwemu y'urufunguzo rw'umunyu). Urufunguzo rutegerezwa kuba **rwihariye** kandi **rudasanzwe**.
- root_password_sha2**: iyi parametere ihuye n'ijambobanga ry'umuyobozi mburabuzi muri Graylog. Ibikwa nk'igitabu ca Hash SHA-256.



Tuzotangura dukoresheje urufunguzo rw'inyuguti 96 ku **ijambobanga_ibanga**:



```
pwgen -N 1 -s 96
wVSGYwOmwBIDmtQvGzSuBevWoXe0MWpNWCzhorBfvMMhia2zIjHguTbfl4uXZJdHOA0EEb1sOXJTZKINhIIBm3V57vwfQV59
```



Kopa agaciro kagarutse, hanyuma ufungure dosiye y'imiterere ya Graylog:



```
sudo nano /etc/graylog/server/server.conf
```



Nimushire urufunguzo muri **ijambobanga_ibanga**, nk'ibi:



![Image](assets/fr/027.webp)



Bika kandi ufunge dosiye.



Igikurikira, ukeneye gushinga ijambobanga rya konti "**admin**" yashizweho ku buryo busanzwe. Mu dosiye y’imiterere, Hash y’ijambobanga itegerezwa kubikwa, bisobanura ko itegerezwa kubarwa. Akarorero kari musi gatanga Hash y'ijambobanga "**LogsWells@**": hindura agaciro k'ijambobanga ryawe.



```
echo -n "PuitsDeLogs@" | shasum -a 256
6b297230efaa2905c9a746fb33a628f4d7aba4fa9d5c1b3daa6846c68e602d71
```



Kopa agaciro karonswe nk'igisohoka (ata n'akarongo kari ku mpera y'umurongo).



Gufungura dosiye y'imiterere ya Graylog kandi:



```
sudo nano /etc/graylog/server/server.conf
```



Nimushire agaciro mu **umuzi_ijambobanga_sha2** nk'uku:



![Image](assets/fr/026.webp)



Mu gihe uri muri dosiye y'imiterere, shiraho "**http_bind_aderesi**". Sobanura "**0.0.0.0:9000**" kugira ngo urubuga rwa Graylog rwa Interface rushobore gushikirwa ku cambu **9000**, biciye ku rubuga rwose rwa IP Address.



![Image](assets/fr/024.webp)



Hanyuma ushireho "**ishakisha_abashitsi**" ku `http://127.0.0.1:9200` kugira ngo umenyeshe urugero rwacu rw'Ishakisha ry'Igihugu. Ivyo ni ngombwa, kuko tutariko turakoresha **Igiharuro c'amakuru ya Graylog**. Kandi ata mahitamwo, ntibizoshoboka kuja kure...



![Image](assets/fr/025.webp)



Bika kandi ufunge dosiye.



Iri tegeko rituma Graylog ikora kugira ngo itangure ubwayo ku nkuru ikurikira, maze igaca itanguza umukozi wa Graylog.



```
sudo systemctl enable --now graylog-server
```



Ivyo bimaze gushika, gerageza kwifatanya na Graylog ukoresheje umucukumbuzi. Injira IP ya server Address (canke izina) n'icuma 9000.



**Ku makuru yawe:**



Nta gihe kirekire gishize, idirisha ry’ukwemeza risa n’iri musi ryabonetse igihe winjiye ubwa mbere muri Graylog. Wabwirizwa kwinjiza "**admin**" n'ijambobanga ryawe. Kandi rero woba utangaye cane ubonye ko iyo connexion itakora.



![Image](assets/fr/031.webp)



Vyari ngombwa ko umuntu asubira ku murongo w’amabwirizwa kuri server ya Graylog maze akabona ivyanditswe. Twoshobora rero kubona ko **ku bijanye n'uguhuza kwa mbere**, bikenewe **gukoresha ijambobanga ry'igihe gito**, rigaragazwa mu bitabo.



```
tail -f /var/log/graylog-server/server.log
```



![Image](assets/fr/021.webp)



Wabwirizwa rero gusubira kugerageza gukorana n'ukoresha "**admin**" n'ijambobanga ry'igihe gito, kandi ivyo vyaguhaye uburenganzira bwo kwinjira!



**Ivyo ntibikiriho. Ico ubwirizwa gukora n'ukwinjira ukoresheje konti yawe y'ubuyobozi n'ijambobanga ryatunganijwe ku murongo w'amabwirizwa.**



![Image](assets/fr/033.webp)



**Murakaze muri Interface ya Graylog!**



![Image](assets/fr/019.webp)



#### E. Graylog: rema konti nshasha y'umuyobozi



Aho gukoresha konti y’umuyobozi yashizweho na Graylog, urashobora kwiremera konti yawe bwite y’umuyobozi. Fyonda kuri "**System**", hanyuma kuri "**Abakoresha n'Imirwi**" kugira ukande kuri buto ya "**Rema umukoresha**". Hanyuma wuzuze urupapuro maze ushire uruhara rw’umuyobozi kuri konti yawe.



![Image](assets/fr/020.webp)



Konti y’umuntu ku giti ciwe ishobora kubamwo amakuru y’inyongera, nk’izina ry’imbere n’iry’umuryango be n’imeli Address, bitandukanye n’ikonti y’umuyobozi w’akavukire. Ikindi, ivyo bituma umuntu wese ashobora gukurikirana neza iyo akorana na konti yitwa.



## Wohereze inyandiko kuri Graylog na rsyslog



### I. Ugushikiriza



Muri iki gice ca kabiri, tuzomenya ingene twotunganya imashini ya Linux kugira ngo yohereze amakuru yayo kuri server ya Graylog. Kugira ivyo tubishikeko, tuzoshiramwo no gutunganya Rsyslog kuri sisitemu.



### II. Gutunganya Graylog kugira ngo yakire inyandiko za Linux



Tuzotangura dutunganije Graylog. Hari intambwe zitatu zo guheza:





- Guhingura **Input** kugira ngo ureme ahantu ho kwinjira hashobora gutuma imashini za Linux **yohereza amakuru ya Syslog biciye kuri UDP**.
- Guhingura **Index** nshasha yo kubika no **index ibitabo vyose vya Linux**.
- Guhingura **Umugezi** wo **gutwara** ibitabo vyakiriwe na Graylog ku rutonde rwa Linux rushasha.



#### A. Rema Injiza ya Syslog



Injira muri Graylog Interface, ukande kuri "**Sisitemu**" mu rutonde hanyuma ukande kuri "**Ivyinjira**". Mu rutonde ruza, hitamwo "**Syslog UDP**" hanyuma ukande kuri buto yanditsweko "**Tanguza inyungu nshasha**". Birashoboka kandi gukora TCP Syslog Input, ariko ivyo bisaba gukoresha icemeza TLS: ikintu co kwongerako ku mutekano, ariko ntibivugwa muri iyi ngingo.



![Image](assets/fr/001.webp)



Umupfumu azoboneka ku rubuga. Tangana n'uguha iyi Njiza izina, nk'akarorero "**Graylog_UDP_Rsyslog_Linux**" hanyuma uhitemwo icuma. Ku mburabuzi, icuma ni "**514**", ariko ushobora kugihindura. Aha, icuma "**12514**" kiratowe.



![Image](assets/fr/016.webp)



Ushobora kandi gusuzuma "**Bika ubutumwa bwose**" kugira ngo ubike ubutumwa bwose bw'inyandiko muri Graylog. Fyonda kuri "**Tanguza Injiza**".



![Image](assets/fr/017.webp)



Injiza nshasha yararemwe kandi ubu irakora. Graylog ubu irashobora kwakira amakuru ya Syslog ku port 12514/UDP, ariko ntituraheza gutunganya porogarama.



![Image](assets/fr/018.webp)


**Iciyumviro:** Input imwe ishobora gukoreshwa mu kubika amakuru y'amamashini menshi ya Linux.



#### B. Rema urutonde rwa Linux rushasha



Turakeneye gukora Index muri Graylog kugira ngo tubike amakuru ava mu mashini za Linux. **index** muri Graylog ni ububiko burimwo amakuru yakiriwe, ni ukuvuga ubutumwa bwakiriwe. Graylog ikoresha OpenSearch nk’ububiko bwayo, kandi ubutumwa burashirwa mu rutonde kugira ngo bushobore gushakisha vyihuta kandi bikora neza.



Kuva kuri Graylog, kanda kuri "**Sisitemu**" muri menyu, hanyuma kuri "**Index**". Kuri paji nshasha izoboneka, kanda kuri "**Rema urutonde**".



![Image](assets/fr/005.webp)



Izina ry'urutonde, nk'akarorero "**Index ya Linux**", wongereko insobanuro n'intango, imbere yo kwemeza. Aha, tuzobika **ibitabo vyose vya Linux muri uru rutonde**. Birashoboka kandi gukora index zidasanzwe zo kubika gusa inyandiko zimwe zimwe (inyandiko [SSH] gusa (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/ "SSH"), inyandiko z'ibikorwa vy'urubuga, n'ibindi).



![Image](assets/fr/006.webp)



Ubu rero turakeneye gukora umugezi mushasha wo gutuma ubutumwa buja muri uru rutonde.



#### C. Rema umugezi



Kugira ngo ureme umugezi mushasha, kanda kuri "**Umugezi**" mu rutonde rwa Graylog. Hanyuma ukande kuri buto ya "**Rema umugezi**" iri iburyo. Mu idirisha rizoboneka, ushire izina ry'uruzi, nk'akarorero "**Uruzi rwa Linux**" hanyuma uhitemwo urutonde "**Index ya Linux**" ku mwanya witwa "**Index Set**". Wemeze ihitamwo ryawe.



**Iciyumviro: ubutumwa bujanye n'uru ruzi na bwo buzoshirwa muri "Uruzi rwa mbere", kiretse usuzumye uburyo bwa "Kuraho ibihuye muri 'Uruzi rwa mbere'".**



![Image](assets/fr/002.webp)



Hanyuma, mu mitunganyirize ya steam yawe, ukande kuri buto ya "**Ongera itegeko ry'uruzi**" kugira ngo wongereko itegeko rishasha ry'inzira y'ubutumwa. Niba udashobora kubona iri dirisha, kanda kuri "**Imigende**" muri menu, hanyuma ku murongo uhuye n'umugezi wawe, kanda kuri "**Ibindi**" hanyuma "**Gucungera Amategeko**".



Hitamwo ubwoko bwa "**injiza ihuye**" hanyuma uhitemwo **injiza ya Rsyslog muri UDP** yaremwe mbere. Wemeze n'ubuto "**Rema Itegeko**". Ubutumwa bwose buja ku Input yacu nshasha ubu buzorungikwa kuri Index ya Linux.



![Image](assets/fr/003.webp)



Umugezi wawe mushasha ukwiye kuboneka muri list kandi ukwiye kuba uri mu rwego rwa "**Running**". Ubutumwa bugaragaza "**0 msg/s**", kuko ubu nta nkuru turiko turarungika ku nzira ya Rsyslog UDP. Kugira ngo ubone amakuru y’uruzi, ushobora gufyonda kw’izina ryawo.



![Image](assets/fr/004.webp)



**Ibintu vyose birateguwe ku ruhande rwa Graylog**. Intambwe ikurikira ni ugutunganya imashini ya Linux.



### III. Gushiramwo no gutunganya Rsyslog kuri Linux



Injira mu mashini ya Linux, haba mu karere canke kure, maze ukoreshe konti y’ukoresha ifise uruhusha rwo gushira hejuru uburenganzira bwayo (biciye kuri sudo). Ahandi ho, koresha konti ya "umuzi" ataco ukora.



#### A. Gushiramwo umuzigo wa Rsyslog



Tangana n'ugusubiramwo ububiko bwa porogaramu no gushiramwo porogaramu yitwa "**rsyslog**".



```
sudo apt-get update
sudo apt-get install rsyslog
```



Hanyuma usuzume uko igikorwa kimeze. Akenshi, irasanzwe iriko iragenda.



```
sudo systemctl status rsyslog
```



#### B. Gutunganya Rsyslog



Rsyslog ifise dosiye nyamukuru y'imiterere iri hano:



```
/etc/rsyslog.conf
```



Ikindi, ububiko "**/etc/rsyslog.d/**" burakoreshwa mu kubika amadosiye y'inyongera y'imiterere ya Rsyslog. Mu dosiye nyamukuru y'imiterere, hariho amabwirizwa yo gushiramwo amadosiye yose "**.conf**" ari muri ubu bubiko. Ivyo bituma bishoboka kugira amadosiye y’inyongera yo gutunganya Rsyslog ata guhindura dosiye nyamukuru.



Muri ubu bubiko, utegerezwa gukoresha imibare kugira ngo usobanure urutonde rwo gushiramwo, kuko amadosiye ashirwa mu buryo bw'inyuguti. Kwongera intango y'umubare bigufasha gucunga ivy'imbere hagati y'amadosiye menshi y'imiterere. Aha, dufise dosiye imwe gusa y’inyongera, rero nta kibazo.



Muri ubu bubiko, tuzokora dosiye yitwa "**10-graylog.conf**":



```
sudo nano /etc/rsyslog.d/10-graylog.conf
```



Muri iyi dosiye, shiramwo uyu murongo:



```
*.* @192.168.10.220:12514;RSYSLOG_SyslogProtocol23Format
```



Ehe ingene wosobanura uyu murongo:





- `*.*`: bisigura kohereza inyandiko zose za Syslog zivuye ku mashini ya Linux zija kuri Graylog.
- `@`: yerekana ko gutwara ibintu bikorerwa muri UDP. Utegerezwa gutanga "**@@**" kugira ngo uhindure kuri TCP.
- `192.168.10.220:12514`: yerekana Address ya server ya Graylog, n'icuma aho amakuru yoherezwa (bihuye n'Ivyinjira).
- `RSYSLOG_Syslog23Imiterere`: ihuye n'imiterere y'ubutumwa buzorungikwa kuri Graylog.



Niwaheza, ubike dosiye hanyuma wongere utangure Rsyslog.



```
sudo systemctl restart rsyslog.service
```



Hakurikijwe iki gikorwa, ubutumwa bwa mbere bukwiye gushika kuri server yawe ya Graylog!



### IV. Kugaragaza inyandiko za Linux muri Graylog



Kuva kuri Graylog, ushobora gukanda kuri "**Streams**" ugahitamwo umugezi wawe mushasha kugira ngo ubone ubutumwa bujanye. Canke ukande kuri "**Search**" uhitemwo Steam yawe maze utangure gushaka.



Aha niho hari ibintu nyamukuru biri muri Interface:



**1** - Hitamwo igihe uzogaragaza ubutumwa. Ku mburabuzi, ubutumwa bwo mu minota 5 iheze buragaragazwa.



**2** - Hitamwo umugezi (s) uzokwerekanwa.



**3** - Gushoboza gusubiramwo urutonde rw'ubutumwa (buri masegonda 5, nk'akarorero). Ahandi ho, ni static kandi uzobwirizwa kuyisubiramwo n’amaboko.



**4** - Fyonda ku nzira y'ugukura kugira ngo utangure ubushakashatsi umaze guhindura igihe, uruzi canke akayunguruzo.



**5** - Umurongo w'inyandiko kugira ngo ugaragaze amayunguruzo y'ubushakashatsi bwawe. Aha, ndasobanura "**source:srv\-docker**" kugira ngo yerekane gusa ibitabo vy'imashini nshasha n'ubu nshizeko Rsyslog.



Ivyanditswe birungikwa n'imashini ya Linux:



![Image](assets/fr/015.webp)



### V. Kumenya ukunanirwa kw'ihuriro rya SSH



Inkomezi za Graylog ziri mu bushobozi bwayo bwo gushiramwo ibitabo no gutuma ubushakashatsi bukorwa hakurikijwe ingingo zitandukanye: imashini y’inkomoko, Timestamp, ibirimwo ubutumwa, n’ibindi... Twoshobora kuba turiko turarondera kumenya amahuzu ya SSH yananiwe.



Uvuye ku mashini iri kure (server ya Graylog, nk’akarorero), gerageza kwifatanya na server yawe ya Linux uherutse gutunganya Rsyslog. Nk'akarorero:



```
ssh [email protected]
```



Hanyuma winjize n'ibigirankana **izina ry'ukoresha** n'ijambobanga** bitari vyo, kugira ngo **amakosa yo guhuza generate**. Mu dosiye "**/var/log/auth.log**", ibi bizotuma ubutumwa bwa generate busa n'ubu bukurikira:



```
Failed password for invalid user it-connect from 192.168.10.199 port 50352 ssh2
```



Ushobora kuronka ubu butumwa kuri Graylog.



Kuri Graylog, koresha akayunguruzo k'ubushakashatsi kugira ngo ugaragaze ubutumwa buhuye gusa:



```
message:Failed password AND application_name:sshd
```



Niba ufise ama server menshi kandi wipfuza gusuzuma inyandiko za server yihariye, vuga izina ryayo mu kwongerako:



```
message:Failed password AND application_name:sshd AND source:srv\-docker
```



Aha niho hari incamake y'igisubizo ku mashini aho nakoze amakosa menshi yo guhuza, mu bihe bitandukanye vy'umusi:



![Image](assets/fr/009.webp)



Igerageza ryo guhuza ridashobotse rikorwa n'imashini ifise IP Address "**192.168.10.199**". Niba ushaka kumenya vyinshi ku bikorwa vy'uyu mushitsi, ushobora **kurondera iyi IP Address**. Graylog izosohora ibitabo vyose aho iyi IP Address ivugwa, ku bashitsi bose (ivyo kohereza ibitabo vyatunganijwe).



Muri iki gihe, akayunguruzo kazokoreshwa gashobora kuba:



```
message:"192.168.10.199"
```



Turaronka ibisubizo vy'inyongera (ntibitangaje, kuko tutayungurura ku gikorwa ca SSH):



![Image](assets/fr/008.webp)



### VI. Iciyumviro



Ukurikije iyi nyigisho, ushobora gutunganya imashini ya Linux kugira ngo yohereza amakuru yayo kuri server ya Graylog. Uko niko, uzoshobora gushiramwo amakuru y'abashitsi bawe ba Linux mu gitabo cawe c'amakuru!



Kugira ngo ugende mbere n’imbere, niwiyumvire gukora ama dashboards n’imburi kugira ngo uronke itangazo iyo hari ikintu kidasanzwe kibonetse.



![Image](assets/fr/007.webp)