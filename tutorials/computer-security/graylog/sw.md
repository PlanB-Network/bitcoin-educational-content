---
name: Graylog
description: Weka kati na uchanganue kumbukumbu zako kwa urahisi
---
![cover](assets/cover.webp)



___



*Mafunzo haya yanatokana na maudhui asili ya Florian BURNEL yaliyochapishwa kwenye [IT-Connect](https://www.it-connect.fr/). Leseni [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Huenda mabadiliko yamefanywa kwa maandishi asilia.*



___



## Inapeleka Graylog kwenye Debian 12



### I. Uwasilishaji



Graylog ni suluhisho la chanzo huria la "sink ya kumbukumbu" iliyoundwa ili kuweka kati, kuhifadhi na kuchambua kumbukumbu kutoka kwa mashine na vifaa vyako vya mtandao kwa wakati halisi. Katika somo hili, tutajifunza jinsi ya kusakinisha toleo lisilolipishwa la Graylog kwenye mashine ya Debian 12!



Ndani ya mfumo wa taarifa, kila **seva**, iwe inaendesha **Linux** au **Windows**, na kila **kifaa cha mtandao** (badili, kipanga njia, ngome, n.k...) **huzalisha kumbukumbu zake**, zilizohifadhiwa ndani. Na magogo yaliyohifadhiwa ndani ya kila mashine, uchanganuzi wa tukio na uunganisho ni mgumu sana... Hapa ndipo **Graylog** inapoingia. Itafanya kama **sinki la kumbukumbu**, ikimaanisha kuwa **mashine zako zote zitaituma kumbukumbu zake** (kupitia syslog, kwa mfano). Kisha Greylog ** itahifadhi na kuashiria kumbukumbu hizi **, huku ikikuruhusu kufanya utafutaji wa kimataifa na kuunda arifa.



Graylog ni chombo cha uchambuzi na ufuatiliaji ambacho hurahisisha kutambua tabia ya tuhuma na matatizo mbalimbali (utulivu, utendaji, nk).




![Image](assets/fr/034.webp)



**Kumbuka: toleo lisilolipishwa, **Graylog Open**, si SIEM kama Wazuh ilivyo, hasa kwa vile haina vitendaji halisi vya kugundua uvamizi.



### II. Masharti



**Stack Graylog** inatokana na **vijenzi kadhaa** ambavyo tutahitaji kusakinisha na kusanidi. Hapa, tutasakinisha vipengele vyote kwenye seva moja, lakini inawezekana kuunda makundi kulingana na nodi kadhaa na kusambaza majukumu kwenye seva kadhaa. Kwa madhumuni ya mafunzo haya, tutakuwa tunasakinisha **Graylog 6.1**, toleo la hivi punde zaidi hadi sasa.





- MongoDB 7**, toleo la sasa linalopendekezwa kwa Graylog (kiwango cha chini 5.0.7, cha juu zaidi 7.x)
- OpenSearch**, chanzo huria cha Fork cha Elasticsearch kilichoundwa na Amazon (kiwango cha chini 1.1.x, cha juu zaidi 2.15.x)
- OpenJDK 17**



**Seva ya Greylog** inafanya kazi kwenye **Debian 12**, lakini usakinishaji unawezekana kwenye usambazaji mwingine, pamoja na kupitia Docker. Mashine ya kawaida ina vifaa vya ** 8 GB RAM ** na ** nafasi ya diski 256 GB **, ili kuwa na rasilimali za kutosha kwa vipengele vyote (vinginevyo hii inaweza kuwa na athari kubwa juu ya utendaji). Walakini, ninatoa hii kama mwongozo mbaya, kwani ** ukubwa wa usanifu wa Graylog unategemea kiwango cha habari cha kuchakatwa **. Graylog inaweza kuchakata MB 30 au MB 300 za data kwa siku, pamoja na GB 300 za data kwa siku... Ni **suluhisho la hatari** lenye uwezo wa kushughulikia **terabaiti za kumbukumbu** (ona [hii ukurasa](https://go2docs.graylog.org/current/planning_your_deployment/planning_your_deployment.html?tocpath=Plan%20Your%20Deployment%7C___0)).



![Image](assets/fr/032.webp)



Chanzo: Graylog



Kabla ya kuanza usanidi, toa IP tuli Address kwa mashine ya Graylog na usakinishe masasisho ya hivi karibuni. Hakikisha umeweka saa za eneo la mashine ya karibu na ubainishe seva ya NTP kwa ulandanishi wa tarehe na saa. Hapa kuna amri ya kukimbia:



```
sudo timedatectl set-timezone Europe/Paris
```



**Kumbuka: **Usakinishaji wa OpenSearch ni wa hiari** ikiwa unatumia **Njia ya Data ya Graylog** badala yake.



### III Ufungaji wa hatua kwa hatua wa Graylog



Wacha tuanze kwa kusasisha kashe ya kifurushi na kusakinisha zana tunazohitaji kwa kile kitakachokuja.



```
sudo apt-get update
sudo apt-get install curl lsb-release ca-certificates gnupg2 pwgen
```



![Image](assets/fr/030.webp)



#### A. Inasakinisha MongoDB



Mara tu hiyo ikikamilika, tutaanza kusakinisha MongoDB. Pakua kitufe cha GPG kinacholingana na hazina ya MongoDB:



```
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```



Kisha ongeza hazina ya MongoDB 6 kwenye mashine ya Debian 12:



```
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```



Ifuatayo, tutasasisha kashe ya kifurushi na kujaribu kusakinisha MongoDB:



```
sudo apt-get update
sudo apt-get install -y mongodb-org
```



MongoDB haiwezi kusakinishwa kwa sababu utegemezi haupo: **libssl1.1**. Itabidi tusakinishe kifurushi hiki kwa mikono kabla ya kuendelea, kwa sababu Debian 12 hakina katika hazina zake.



```
Les paquets suivants contiennent des dépendances non satisfaites :
mongodb-org-mongos: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
mongodb-org-server: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
E: Impossible de corriger les problèmes, des paquets défectueux sont en mode « garder en l'état ».
```



Tutapakua kifurushi cha DEB kiitwacho "**libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb**" (toleo la hivi punde) kwa amri ya **wget**, kisha isakinishe kwa **dpkg** amri. Hii hutoa amri mbili zifuatazo:



```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
```



![Image](assets/fr/028.webp)



Anzisha tena usakinishaji wa MongoDB:



```
sudo apt-get install -y mongodb-org
```



Kisha anza upya huduma ya MongoDB na uiwezeshe kuanza kiotomatiki seva ya Debian inapozinduliwa.



```
sudo systemctl daemon-reload
sudo systemctl enable mongod.service
sudo systemctl restart mongod.service
sudo systemctl --type=service --state=active | grep mongod
```



Na MongoDB imewekwa, tunaweza kuendelea na kusakinisha sehemu inayofuata.



#### B. Kusakinisha OpenSearch



Wacha tuendelee kusakinisha OpenSearch kwenye seva. Amri ifuatayo inaongeza ufunguo wa saini kwa vifurushi vya OpenSearch:



```
curl -o- https://artifacts.opensearch.org/publickeys/opensearch.pgp | sudo gpg --dearmor --batch --yes -o /usr/share/keyrings/opensearch-keyring
```



Kisha ongeza hazina ya OpenSearch ili tuweze kupakua kifurushi na **apt** baadaye:



```
echo "deb [signed-by=/usr/share/keyrings/opensearch-keyring] https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable main" | sudo tee /etc/apt/sources.list.d/opensearch-2.x.list
```



Sasisha akiba ya kifurushi chako:



```
sudo apt-get update
```



Kisha **sakinisha OpenSearch**, ukitunza **kufafanua nenosiri chaguo-msingi la akaunti ya Msimamizi** ya mfano wako. Hapa, nenosiri ni "**IT-Connect2024!**", lakini badala ya thamani hii kwa nenosiri kali. **Epuka manenosiri hafifu** kama vile "**P@ssword123**" na utumie angalau vibambo **8** vyenye angalau herufi moja ya kila aina (herufi ndogo, kubwa, nambari na herufi maalum), vinginevyo kutakuwa na hitilafu mwishoni mwa usakinishaji. **Hili ni sharti tangu OpenSearch 2.12.**



```
sudo env OPENSEARCH_INITIAL_ADMIN_PASSWORD=IT-Connect2024! apt-get install opensearch
```



Tafadhali kuwa na subira wakati wa ufungaji...



Ukimaliza, chukua muda kutekeleza usanidi wa chini zaidi. Fungua faili ya usanidi katika umbizo la YAML:



```
sudo nano /etc/opensearch/opensearch.yml
```



Wakati faili imefunguliwa, weka chaguzi zifuatazo:



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



Usanidi huu wa OpenSearch umeundwa ili kusanidi nodi moja. Hapa kuna baadhi ya maelezo ya vigezo tofauti tunavyotumia:





- cluster.name: graylog**: kigezo hiki kinataja nguzo ya OpenSearch yenye jina "**graylog**".
- node.name: ${HOSTNAME}**: jina la nodi limewekwa kwa nguvu ili lilingane na mashine ya ndani ya Linux. Hata kama tuna nodi moja tu, ni muhimu kuipa jina kwa usahihi.
- path.data: /var/lib/opensearch**: njia hii inabainisha ambapo OpenSearch huhifadhi data yake kwenye mashine ya ndani, katika hali hii katika "**/var/lib/opensearch**".
- path.logs: /var/log/opensearch**: njia hii inafafanua ambapo faili za kumbukumbu za OpenSearch zimehifadhiwa, hapa katika "**/var/log/opensearch**".
- discovery.type: single-nodi**: parameta hii inasanidi OpenSearch kufanya kazi na nodi moja, hivyo basi chaguo la "**single-nodi**" chaguo.
- network.host: 127.0.0.1**: usanidi huu unahakikisha kwamba OpenSearch inasikiza tu kwenye kitanzi chake cha ndani cha Interface, ambacho kinatosha kwa vile kiko kwenye seva sawa na Graylog.
- action.auto_create_index: false**: kwa kuzima uundaji wa faharasa otomatiki, OpenSearch haitaunda faharasa kiotomatiki hati inapotumwa bila faharasa iliyopo.
- plugins.security.disabled: kweli**: chaguo hili huzima programu-jalizi ya usalama ya OpenSearch, kumaanisha kuwa hakutakuwa na uthibitishaji, udhibiti wa ufikiaji au usimbaji fiche wa mawasiliano. Mpangilio huu huokoa muda wakati wa kusanidi Graylog, lakini unapaswa kuepukwa katika toleo la umma (angalia [ukurasa huu](https://opensearch.org/docs/1.0/security-plugin/index/)).



Chaguzi zingine tayari zipo, kwa hivyo unahitaji tu kuondoa "#" ili kuziamilisha, kisha uonyeshe thamani yako. Ikiwa huwezi kupata chaguo, unaweza kulitangaza moja kwa moja mwishoni mwa faili.



![Image](assets/fr/023.webp)



Hifadhi na ufunge faili hii.



#### C. Sanidi Java (JVM)



Unahitaji kusanidi Mashine ya Mtandaoni ya Java inayotumiwa na OpenSearch ili kurekebisha kiasi cha kumbukumbu ambacho huduma hii inaweza kutumia. Hariri faili ifuatayo ya usanidi:



```
sudo nano /etc/opensearch/jvm.options
```



Usanidi ukiwa umetumwa hapa, **OpenSearch itaanza na GB 4 ya kumbukumbu iliyotengwa na inaweza kukua hadi GB 4**, kwa hivyo hakutakuwa na tofauti ya kumbukumbu wakati wa operesheni. Hapa, usanidi unazingatia ukweli kwamba mashine ya kawaida ina jumla ya ** 8 GB RAM **. Vigezo vyote viwili lazima viwe na thamani sawa. Hii inamaanisha kuchukua nafasi ya mistari:



```
-Xms1g
-Xmx1g
```



Na mistari hii:



```
-Xms4g
-Xmx4g
```



Hapa kuna picha ya marekebisho ya kufanywa:



![Image](assets/fr/022.webp)



Funga faili hii baada ya kuihifadhi.



Kwa kuongeza, tunahitaji kuangalia usanidi wa kigezo cha "**max_map_count**" kwenye kinu cha Linux. Inafafanua kikomo cha maeneo ya kumbukumbu yaliyopangwa kwa kila mchakato, ili kukidhi mahitaji ya programu yetu. **OpenSearch**, kama vile Elasticsearch**, inapendekeza kuweka thamani hii kuwa "262144" ili kuepuka makosa ya usimamizi wa kumbukumbu.



Kimsingi, kwenye mashine mpya ya Debian 12 iliyosanikishwa, thamani tayari ni sahihi. Lakini hebu tuangalie. Tekeleza amri hii:



```
cat /proc/sys/vm/max_map_count
```



Ikiwa unapata thamani nyingine isipokuwa "**262144**", endesha amri ifuatayo, vinginevyo sio lazima.



```
sudo sysctl -w vm.max_map_count=262144
```



Hatimaye, wezesha OpenSearch autostart na kuzindua huduma husika.



```
sudo systemctl daemon-reload
sudo systemctl enable opensearch
sudo systemctl restart opensearch
```



Ukionyesha hali ya mfumo wako, unapaswa kuona mchakato wa Java na RAM ya GB 4.



```
top
```



![Image](assets/fr/029.webp)



Hatua inayofuata: usakinishaji uliosubiriwa kwa muda mrefu wa Graylog!



#### D. Kufunga Graylog



Ili **kusakinisha Graylog 6.1** katika toleo lake jipya zaidi, endesha amri 4 zifuatazo ili **kupakua na kusakinisha Seva ya Greylog**:



```
wget https://packages.graylog2.org/repo/packages/graylog-6.1-repository_latest.deb
sudo dpkg -i graylog-6.1-repository_latest.deb
sudo apt-get update
sudo apt-get install graylog-server
```



Hii inapofanywa, tunahitaji kufanya mabadiliko fulani kwenye usanidi wa Graylog kabla ya kujaribu kuizindua.



Wacha tuanze kwa kusanidi chaguzi hizi mbili:





- password_secret**: parameta hii inatumika kufafanua ufunguo unaotumiwa na Graylog ili kupata hifadhi ya nywila za mtumiaji (kwa roho ya ufunguo wa salting). Ufunguo huu lazima uwe **kipekee** na **nasibu**.
- root_password_sha2**: parameter hii inafanana na nenosiri la msimamizi wa default katika Graylog. Imehifadhiwa kama Hash SHA-256.



Tutaanza kwa kutengeneza ufunguo wa herufi 96 kwa kigezo cha **password_secret**:



```
pwgen -N 1 -s 96
wVSGYwOmwBIDmtQvGzSuBevWoXe0MWpNWCzhorBfvMMhia2zIjHguTbfl4uXZJdHOA0EEb1sOXJTZKINhIIBm3V57vwfQV59
```



Nakili thamani iliyorejeshwa, kisha ufungue faili ya usanidi ya Graylog:



```
sudo nano /etc/graylog/server/server.conf
```



Bandika kitufe kwenye parameta ya **password_secret**, kama hii:



![Image](assets/fr/027.webp)



Hifadhi na funga faili.



Ifuatayo, unahitaji kuweka nenosiri kwa akaunti ya "**admin**" iliyoundwa na chaguo-msingi. Katika faili ya usanidi, Hash ya nenosiri lazima ihifadhiwe, ambayo ina maana ni lazima ihesabiwe. Mfano ulio hapa chini unatoa Hash ya nenosiri "**LogsWells@**": rekebisha thamani kwa nenosiri lako.



```
echo -n "PuitsDeLogs@" | shasum -a 256
6b297230efaa2905c9a746fb33a628f4d7aba4fa9d5c1b3daa6846c68e602d71
```



Nakili thamani iliyopatikana kama pato (bila hyphen mwishoni mwa mstari).



Fungua tena faili ya usanidi wa Greylog:



```
sudo nano /etc/graylog/server/server.conf
```



Bandika thamani kwenye **root_password_sha2** chaguo kama hii:



![Image](assets/fr/026.webp)



Ukiwa kwenye faili ya usanidi, weka chaguo la "**http_bind_address**". Bainisha "**0.0.0.0:9000**" ili wavuti ya Interface ya Graylog iweze kufikiwa kwenye bandari **9000**, kupitia seva yoyote ya IP Address.



![Image](assets/fr/024.webp)



Kisha weka chaguo la "**elasticsearch_hosts**" kuwa `http://127.0.0.1:9200` ili kutangaza mfano wetu wa OpenSearch. Hii ni muhimu, kwani hatutumii **Njia ya Data ya Graylog**. Na bila chaguo hili, haitawezekana kwenda mbali zaidi ...



![Image](assets/fr/025.webp)



Hifadhi na funga faili.



Amri hii inawasha Greylog ili ianze kiotomatiki kwenye buti inayofuata, na mara moja inazindua seva ya Graylog.



```
sudo systemctl enable --now graylog-server
```



Mara hii imefanywa, jaribu kuunganisha kwa Graylog kutoka kwa kivinjari. Ingiza IP ya seva Address (au jina) na mlango 9000.



**Kwa taarifa yako:**



Sio muda mrefu uliopita, dirisha la uthibitishaji sawa na lililo hapa chini lilionekana wakati ulipoingia kwa mara ya kwanza kwenye Graylog. Ilibidi uingize kuingia kwako "**admin**" na nenosiri lako. Na kisha utashangaa bila kupendeza kupata kwamba muunganisho haukufanya kazi.



![Image](assets/fr/031.webp)



Ilikuwa ni lazima kurudi kwenye mstari wa amri kwenye seva ya Graylog na kushauriana na magogo. Kisha tunaweza kuona kwamba **kwa muunganisho wa kwanza**, ni muhimu **kutumia nenosiri la muda**, lililobainishwa kwenye kumbukumbu.



```
tail -f /var/log/graylog-server/server.log
```



![Image](assets/fr/021.webp)



Kisha ulilazimika kujaribu tena muunganisho na mtumiaji "**admin**" na nenosiri la muda, na hii ilikuruhusu kuingia!



**Hii sivyo ilivyo tena. Unachohitajika kufanya ni kuingia na akaunti yako ya msimamizi na nenosiri lililowekwa kwenye mstari wa amri



![Image](assets/fr/033.webp)



**Karibu kwenye Interface ya Graylog!



![Image](assets/fr/019.webp)



#### E. Graylog: fungua akaunti mpya ya msimamizi



Badala ya kutumia akaunti ya msimamizi iliyoundwa asili na Graylog, unaweza kuunda akaunti yako ya kibinafsi ya msimamizi. Bofya kwenye menyu ya "**Mfumo**", kisha kwenye "**Watumiaji na Timu**" ili kubofya kitufe cha "**Unda mtumiaji**". Kisha jaza fomu na ukabidhi jukumu la msimamizi kwa akaunti yako.



![Image](assets/fr/020.webp)



Akaunti iliyobinafsishwa inaweza kuwa na maelezo ya ziada, kama vile jina la kwanza na la mwisho na barua pepe ya Address, tofauti na akaunti asili ya msimamizi. Zaidi ya hayo, hii inahakikisha ufuatiliaji bora zaidi wakati kila mtu anafanya kazi na akaunti iliyotajwa.



## Tuma kumbukumbu kwa Graylog na rsyslog



### I. Uwasilishaji



Katika sehemu hii ya pili, tutajifunza jinsi ya kusanidi mashine ya Linux kutuma kumbukumbu zake kwa seva ya Graylog. Ili kufanya hivyo, tutasakinisha na kusanidi Rsyslog kwenye mfumo.



### II. Inasanidi Graylog ili kupokea kumbukumbu za Linux



Tutaanza kwa kusanidi Graylog. Kuna hatua tatu za kukamilisha:





- Kuundwa kwa **Ingizo** ili kuunda mahali pa kuingilia kuruhusu mashine za Linux **kutuma kumbukumbu za Syslog kupitia UDP**.
- Kuundwa kwa **Fahasi** mpya ya kuhifadhi na **kuorodhesha kumbukumbu zote za Linux**.
- Uundaji wa **Tiririsha** ili **kuelekeza** kumbukumbu zilizopokelewa na Graylog hadi Fahirisi mpya ya Linux.



#### A. Unda Ingizo la Syslog



Ingia kwenye Graylog Interface, bofya "**Mfumo**" kwenye menyu na kisha kwenye "**Ingizo**". Katika orodha kunjuzi, chagua "**Syslog UDP**" kisha ubofye kitufe kilichoandikwa "**Zindua ingizo jipya**". Inawezekana pia kuunda Uingizaji wa Syslog wa TCP, lakini hii inahitaji matumizi ya cheti cha TLS: nyongeza kwa usalama, lakini haijaangaziwa katika nakala hii.



![Image](assets/fr/001.webp)



Mchawi utaonekana kwenye skrini. Anza kwa kutoa Ingizo hili jina, kwa mfano "**Graylog_UDP_Rsyslog_Linux**" na uchague mlango. Kwa chaguo-msingi, bandari ni "**514**", lakini unaweza kuibadilisha. Hapa, bandari "**12514 **" imechaguliwa.



![Image](assets/fr/016.webp)



Unaweza pia kuangalia chaguo la "**Hifadhi ujumbe kamili**" ili kuhifadhi ujumbe kamili wa kumbukumbu katika Graylog. Bonyeza "**Anzisha Ingizo **".



![Image](assets/fr/017.webp)



Ingizo jipya limeundwa na sasa linatumika. Graylog sasa inaweza kupokea kumbukumbu za Syslog kwenye bandari 12514/UDP, lakini bado hatujamaliza kusanidi programu.



![Image](assets/fr/018.webp)


**Kumbuka: Ingizo moja linaweza kutumika kuhifadhi kumbukumbu kutoka kwa mashine kadhaa za Linux.



#### B. Unda Fahirisi mpya ya Linux



Tunahitaji kuunda Index katika Graylog ili kuhifadhi kumbukumbu kutoka kwa mashine za Linux. **faharasa** katika Graylog ni muundo wa hifadhi ambao una kumbukumbu zilizopokelewa, yaani, ujumbe uliopokelewa. Graylog hutumia OpenSearch kama injini yake ya kuhifadhi, na ujumbe huwekwa katika faharasa ili kuwezesha utafutaji wa haraka na bora.



Kutoka kwa Graylog, bofya "**Mfumo**" kwenye menyu, kisha kwenye "** Fahirisi**". Kwenye ukurasa mpya unaoonekana, bofya "**Unda seti ya faharasa**".



![Image](assets/fr/005.webp)



Taja faharasa hii, kwa mfano "**Linux Index**", ongeza maelezo na kiambishi awali, kabla ya kuthibitisha. Hapa, tutaweza **kuhifadhi kumbukumbu zote za Linux katika faharasa hii**. Pia inawezekana kuunda faharasa maalum ili kuhifadhi kumbukumbu fulani pekee (logi za [SSH] pekee (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/ "SSH"), kumbukumbu za huduma za wavuti, n.k.).



![Image](assets/fr/006.webp)



Sasa tunahitaji kuunda mtiririko mpya ili kuelekeza ujumbe kwa faharasa hii.



#### C. Unda Mtiririko



Ili kuunda mtiririko mpya, bofya "**Mitiririko**" katika menyu kuu ya Graylog. Kisha bofya kitufe cha "**Unda mtiririko**" upande wa kulia. Katika dirisha linaloonekana, taja mkondo, kwa mfano "**Linux Tiririsha**" na uchague faharasa "**Linux Index**" kwa uga unaoitwa "**Index Set**". Thibitisha chaguo lako.



**Kumbuka: barua pepe zinazolingana na mtiririko huu pia zitajumuishwa katika "**Mtiririko Chaguomsingi **", isipokuwa ukiangalia chaguo la "**Ondoa mechi kutoka kwa 'Mtiririko Chaguomsingi'**".



![Image](assets/fr/002.webp)



Kisha, katika mipangilio yako ya mvuke, bofya kitufe cha "**Ongeza kanuni ya mtiririko**" ili kuongeza sheria mpya ya kuelekeza ujumbe. Ikiwa huwezi kupata dirisha hili, bofya "**Mipasho**" kwenye menyu, kisha kwenye mstari unaoendana na mkondo wako, bofya "**Zaidi**" kisha "**Dhibiti Kanuni**".



Chagua aina ya "**lingana*" na uchague ingizo lililoundwa awali **Rsyslog katika UDP**. Thibitisha kwa kitufe cha "** Unda Sheria **". Barua pepe zote kwa Ingizo letu jipya sasa zitatumwa kwa Fahirisi ya Linux.



![Image](assets/fr/003.webp)



Mipasho yako mpya inapaswa kuonekana kwenye orodha na inapaswa kuwa katika hali ya "**Inayoendesha**". Bandwidth ya ujumbe inaonyesha "**0 msg/s**", kwani kwa sasa hatutumi kumbukumbu zozote kwa ingizo la Rsyslog UDP. Ili kutazama kumbukumbu za mtiririko, bonyeza tu kwenye jina lake.



![Image](assets/fr/004.webp)



**Kila kitu kiko tayari kwa upande wa Graylog**. Hatua inayofuata ni kusanidi mashine ya Linux.



### III. Kufunga na kusanidi Rsyslog kwenye Linux



Ingia kwenye mashine ya Linux, iwe ya ndani au ya mbali, na utumie akaunti ya mtumiaji iliyo na ruhusa kuinua marupurupu yake (kupitia sudo). Vinginevyo, tumia akaunti ya "mizizi" moja kwa moja.



#### A. Kusakinisha kifurushi cha Rsyslog



Anza kwa kusasisha kashe ya kifurushi na kusakinisha kifurushi kinachoitwa "**rsyslog**".



```
sudo apt-get update
sudo apt-get install rsyslog
```



Kisha angalia hali ya huduma. Katika hali nyingi, tayari inaendesha.



```
sudo systemctl status rsyslog
```



#### B. Inasanidi Rsyslog



Rsyslog ina faili kuu ya usanidi iliyoko hapa:



```
/etc/rsyslog.conf
```



Kwa kuongeza, saraka ya "**/etc/rsyslog.d/**" inatumiwa kuhifadhi faili za usanidi za ziada za Rsyslog. Katika faili kuu ya usanidi, kuna maagizo ya Jumuisha ya kuleta faili zote za "**.conf**" zilizo katika saraka hii. Hii inafanya uwezekano wa kuwa na faili za ziada za kusanidi Rsyslog bila kurekebisha faili kuu.



Katika saraka hii, lazima utumie nambari ili kufafanua utaratibu wa upakiaji, kwa sababu faili zinapakiwa kwa utaratibu wa alfabeti. Kuongeza kiambishi awali cha nambari hukuruhusu kudhibiti kipaumbele kati ya faili kadhaa za usanidi. Hapa, tuna faili moja tu ya ziada, kwa hivyo sio shida.



Katika saraka hii, tutaunda faili inayoitwa "**10-graylog.conf**":



```
sudo nano /etc/rsyslog.d/10-graylog.conf
```



Katika faili hii, ingiza mstari huu:



```
*.* @192.168.10.220:12514;RSYSLOG_SyslogProtocol23Format
```



Hapa kuna jinsi ya kutafsiri mstari huu:





- `*.*`: inamaanisha kutuma kumbukumbu zote za Syslog kutoka kwa mashine ya Linux hadi Graylog.
- `@`: inaonyesha kuwa usafiri unafanywa katika UDP. Lazima ubainishe "**@@**" ili kubadilisha hadi TCP.
- `192.168.10.220:12514`: inaonyesha Address ya seva ya Graylog, na mlango ambao kumbukumbu hutumwa (inayolingana na Ingizo).
- `RSYSLOG_SyslogProtocol23Format`: inalingana na umbizo la ujumbe utakaotumwa kwa Graylog.



Ukimaliza, hifadhi faili na uanze upya Rsyslog.



```
sudo systemctl restart rsyslog.service
```



Kufuatia kitendo hiki, ujumbe wa kwanza unapaswa kufika kwenye seva yako ya Graylog!



### IV. Inaonyesha kumbukumbu za Linux kwenye Graylog



Kutoka kwa Graylog, unaweza kubofya "**Mitiririko**" na uchague mtiririko wako mpya ili kutazama ujumbe unaohusiana. Vinginevyo, bofya "**Tafuta**" na uchague Steam yako na uanzishe utafutaji.



Hapa kuna baadhi ya vipengele muhimu vya Interface:



**1** - Chagua kipindi cha kuonyesha ujumbe. Kwa chaguo-msingi, ujumbe kutoka kwa dakika 5 zilizopita huonyeshwa.



**2** - Chagua mtiririko wa kuonyeshwa.



**3** - Washa uonyeshaji upya otomatiki wa orodha ya ujumbe (kila sekunde 5, kwa mfano). Vinginevyo, ni tuli na itabidi uirejeshe upya wewe mwenyewe.



**4** - Bofya kwenye kioo cha kukuza ili kuzindua utafutaji baada ya kurekebisha kipindi, mtiririko au kichujio.



**5** - Upau wa ingizo ili kubainisha vichujio vyako vya utafutaji. Hapa, ninabainisha "**source:srv\-docker**" ili kuonyesha kumbukumbu tu za mashine mpya ambayo nimeanzisha Rsyslog.



Kumbukumbu hutumwa na mashine ya Linux:



![Image](assets/fr/015.webp)



### V. Kutambua hitilafu ya muunganisho wa SSH



Nguvu ya Graylog iko katika uwezo wake wa kuorodhesha kumbukumbu na kuwezesha utafutaji ufanyike kulingana na vigezo mbalimbali: mashine ya chanzo, Timestamp, maudhui ya ujumbe, n.k... Tunaweza kutafuta kutambua miunganisho ya SSH iliyoshindwa.



Kutoka kwa mashine ya mbali (seva ya Graylog, kwa mfano), jaribu kuunganisha kwenye seva yako ya Linux ambayo umesanidi Rsyslog. Kwa mfano:



```
ssh [email protected]
```



Kisha kwa makusudi ingiza jina lisilo sahihi **jina la mtumiaji** na **nenosiri**, ili **makosa ya kuunganisha ya generate**. Katika faili ya "**/var/log/auth.log**", hii itaweka ujumbe wa kumbukumbu wa generate sawa na ufuatao:



```
Failed password for invalid user it-connect from 192.168.10.199 port 50352 ssh2
```



Unapaswa kupata ujumbe huu kwenye Graylog.



Kwenye Graylog, tumia kichujio kifuatacho cha utafutaji ili kuonyesha ujumbe unaolingana pekee:



```
message:Failed password AND application_name:sshd
```



Ikiwa una seva kadhaa na ungependa kuchambua kumbukumbu za seva maalum, taja jina lake kwa kuongeza:



```
message:Failed password AND application_name:sshd AND source:srv\-docker
```



Hapa kuna muhtasari wa matokeo kwenye mashine ambapo nilitoa makosa kadhaa ya unganisho, kwa nyakati tofauti za siku:



![Image](assets/fr/009.webp)



Majaribio ya uunganisho yasiyofanikiwa yanafanywa kutoka kwa mashine na IP Address "** 192.168.10.199 **". Iwapo ungependa kujua zaidi kuhusu shughuli za seva pangishi hii, unaweza **kutafuta IP hii Address**. Graylog itatoa kumbukumbu zote ambapo IP hii Address imerejelewa, kwa wapangishi wote (ambao utumaji wa kumbukumbu umesanidiwa).



Katika kesi hii, chujio cha kutumika kinaweza kuwa:



```
message:"192.168.10.199"
```



Tunapata matokeo ya ziada (haishangazi, kwani hatuchuji kwenye programu ya SSH):



![Image](assets/fr/008.webp)



### VI. Hitimisho



Kwa kufuata mafunzo haya, unapaswa kuwa na uwezo wa kusanidi mashine ya Linux kutuma kumbukumbu zake kwa seva ya Graylog. Kwa njia hii, utaweza kuweka kumbukumbu za wapangishi wako wa Linux kwenye sinki yako ya logi!



Ili kwenda mbali zaidi, zingatia kuunda dashibodi na arifa ili kupokea arifa wakati hitilafu inapogunduliwa.



![Image](assets/fr/007.webp)