---
name: Ride The Lightning (RTL)
description: Koresha Gutwara Umuravyo (RTL) kugira ngo ucungere urudodo rwawe rw'Umuravyo
---
![cover](assets/cover.webp)


## 1. Intangamarara



**Gutwara Umuravyo (RTL)** ni urubuga rwuzuye rwa Interface rwo gucunga urudodo rwa Lightning Network. Iyi porogaramu y'urubuga yikoresha itanga Lightning **"cockpit"** ishobora gushikwako ukoresheje umucukumbuzi wawe. RTL ikorana n’ibikorwa vyose bikomeye vy’umuravyo (LND, Core Lightning/CLN na Eclair) kandi iguha ububasha bwose ku nzira yawe n’imirongo yawe. Inkomoko yuguruye (uruhusha rwa MIT) kandi ku buntu, RTL yinjijwe mu buryo busanzwe mu mirongo myinshi y’ibisubizo vy’urufunguzo (RaspiBlitz, MyNode, Umbrel, n’ibindi).



**Ata Interface y'igishushanyo, amanode ya Lightning ashobora gucungirwa gusa biciye ku mategeko ya CLI akoreshwa neza. RTL yorosha ivyo bikorwa n'ubuhinga bwa Interface. Akira ibikorwa nyamukuru:**





- Raba imirongo yawe n'uruzitiro - Igipande c'ibarabara kigaragaza uburinganire bwa On-Chain, amahera y'umuravyo (yo mu karere/kure), ikibanza c'uguhuza, izina ry'uruzitiro n'ibindi. Ushobora kubona urutonde rw’imirongo yawe, ubushobozi, ugukwiragira kwo mu karere/kure n’aho uri. RTL itanga ama dashboards ashingiye ku vyo umuntu akora kugira ngo asesengure ibikorwa akoresheje imfuruka zitandukanye.





- Uburongozi bw'imirongo y'umuravyo** - Gufungura/funga imirongo n'ugukanda bike. RTL ishobora kugufasha kwifatanya n’umugenzi wawe no gufungura umurongo ata tegeko. Ushobora guhindura amafaranga y’urugendo, kuraba igiharuro c’uburinganire, canke gutangura gusubiramwo uburinganire bw’uruziga kugira ngo wongere uburinganire bw’amahera hagati y’imirongo.





- Gukurikirana no kwishura** - RTL icungera ibikorwa vya Lightning: kohereza amahera biciye ku mafagitire, amafagitire ya generate yo kwakira, gukurikirana ibikorwa (amahera, inzira) n’amateka arambuye. Interface nayo isesangura inzira kugira ngo ibone amahera ariko araca muri node yawe.





- Wallet On-Chain uburongozi n'ububiko** - Urupapuro rwa On-Chain rugufasha gukoresha amaderesi ya generate no kohereza amafaranga. RTL ituma vyoroha kubika imirongo mu gutuma hanze dosiye ya SCB ya LND, n’uguhindura kwihuta ku guhindura imirongo yose.



Muri make, RTL ni **dashboard ikomeye ya Lightning Network**, itanga Interface y’inyigisho yo gutwara node yawe ku musi ku musi. Iyi nyigisho izoguyobora mu kuyishiramwo no kuyikoresha mu gucunga imirongo yawe n’amahera yawe.



## 2. Ibikorwa vy'ubuhinga vya RTL



![Schéma de l'architecture RTL : interface responsive compatible avec tous les appareils, frontend Angular, serveur Node (port 3000), connecté aux API REST de LND](assets/fr/01.webp)



Imbere yo gushika ku bintu bitobito, ni vyiza gutahura muri make **ingene RTL ikorana n’urudodo rwawe rwa Lightning** ku rugero rw’ubuhinga.



**Ubwubatsi rusangi:** RTL ni urubuga rwubatswe na Node.js (inyuma) na Angular (imbere). Mu majambo nyayo, RTL ikora nk'umurongo mutoyi w'urubuga rwo mu karere (ku port 3000 ku buryo busanzwe) uvugana n'ugushirwa mu ngiro kwawe kwa Lightning biciye ku APIs zayo. Bivanye n'ubwoko bwa :





- Na **LND**, RTL ikoresha REST API ya LND (icuma 8080) kugira ngo ikore amabwirizwa y'umuravyo. Iryo huriro rikingiwe na TLS kandi risaba dosiye ya LND **admin macaroon** kugira ngo ryemezwe.





- Na **Umuravyo w'Ishingiro (CLN)**, RTL ikoresha API ya REST itangwa na *c-umuravyo-REST*, canke **urune rwo gushikako** biciye ku `commando` plugin. Inyishu nka Umbrel zihita zitunganya izo Elements.





- Na **Eclair**, RTL ihuza na Eclair REST API ikoresheje ijambobanga ry'ukwemeza ryatunganijwe.



**Itunganywa n'umutekano:** RTL itunganijwe biciye muri dosiye ya JSON (`RTL-Config.json`) aho usobanura icuma c'urubuga, ijambobanga ry'ukwinjira, n'amakuru y'ihuriro ku nzira yawe. Urubuga rwa Interface rurindwa n'ijambobanga ry'injira/ijambobanga (`ijambobanga` ry'imbere rizohindurwa) kandi rishigikira 2FA. Ku mburabuzi, RTL ikora nk'i HTTP yo mu karere (`http://localhost:3000`), ariko ku bijanye no gushika kure, wama ukoresha ihuriro ry'umutekano (HTTPS biciye ku nzira y'inyuma, Tor, canke VPN).



Muri make, RTL ni igice c'inyongera gifatanya n'uruzitiro rwawe biciye ku APIs zitekanye, bisaba ibimenyetso vy'ukwinjira bikwiye, kandi itanga umutekano wayo bwite Layer. Iyi nyubakwa y'ibice mbere iragufasha gucunga **ibice vyinshi vy'umuravyo bifise urugero rumwe rwa RTL**.



## 3. Gushiramwo RTL



Nk’uko RTL ikwiragizwa nk’ubuhinga bufunguye, hari uburyo bwinshi bwo kuyishira kuri sisitemu yawe. Muri iki gice, tuzovuga uburyo bubiri nyamukuru: gushiramwo n’amaboko no gushiramwo biciye ku Umbrel.



### Uburyo bw'amaboko



Gushiramwo n'amaboko ni vyiza nimba ukunda kuguma ugenzura neza, canke nimba uriko urashiramwo RTL mu mitunganyirize y'ibintu. Intambwe zikurikira ni iz'umurongo wa LND ukoresha Linux (nk'akarorero Raspberry Pi canke VPS ikoresha Ubuntu/Debian), ariko ni nk'ivyo kuri CLN/Eclair.



**Ibisabwa:** urabe ko ufise **urudodo rwa Bitcoin rukoranye** n'urudodo rwa Lightning rukora (LND, CLN canke Eclair) ku mashini. RTL nta n’urudodo rwa Lightning irimwo, ifatanya n’urudodo ruriho. Ukeneye kandi **Node.js** ishizwemwo (verisiyo 14+ irasabwa). Ushobora kugenzura na `node -v` canke ugashiramwo Node ku rubuga rwemewe (https://nodejs.org/ru/gukuraho/) canke umucungerezi wawe w'amapaki.



Intambwe nyamukuru zo gushiramwo ni :



**Gukuraho kode ya RTL**: Kora ububiko bwa RTL GitHub buzwi mu bubiko uhisemwo. Nk'akarorero:



```bash
git clone https://github.com/Ride-The-Lightning/RTL.git
cd RTL
```



**Shiraho ibishingiyeko**: RTL ni porogaramu ya Node.js, rero ukeneye gushiramwo ibice vyayo bisabwa. Mu dosiye ya RTL, genda :



```bash
npm install --omit=dev --legacy-peer-deps
```



Iri tegeko rishiramwo amapaki ya NPM akenewe (kwirengagiza ivy'iterambere). Ihitamwo `--legacy-peer-deps` ni ryiza kugira ngo wirinde amakimbirane ashobora kubaho.



**RTL-Config**: Igihe ibishingiyeko bimaze gushirwaho, tegura dosiye y'imiterere. Kopa/hindura izina rya dosiye `Icitegererezo-RTL-Imiterere.json` mu muzi w'umugambi ku `RTL-Imiterere.json`. Uwugurure muri :





- Ijambobanga rya UI**: uhitemwo ijambobanga ry'umutekano maze urishire muri `multiPass` (aho gushiramwo `"ijambobanga"`).
- Icibutso**: mburabuzi `3000`. Ushobora kuyihindura nimba iyo port imaze gufatwa ku mashine yawe.
- Urudodo**: mu gice ca `urudodo[0]`, hindura amaparametere y'urudodo rwawe:
     - `lnNode`: izina ridondora urudodo rwawe (nk'akarorero `"Inzu y'urudodo LND"`).
     - lnIshirwa mu ngiro: `"LND"` (canke `"CLN"`/`"ECL"` nk'uko bikwiye).
     - Munsi ya `kwemeza`:
       - macaroonPath`: sobanura inzira yuzuye ija muri dosiye irimwo umuyobozi w'amakaroni ya LND.
       - `Inzira y'Imiterere`: inzira ija kuri dosiye y'imiterere y'uruzitiro (`LND.conf` ya LND).
     - Munsi ya `imiterere`:
       - `Ihindura rya fiat`: shiraho `ukuri` niba ushaka guhindura amafaranga y'amafaranga.
       - `Imirongo itamenyeshejwe`: shiraho `ukuri` kugira ngo ubone imirongo itamenyeshejwe.
       - Ibara ry'insanganyamatsiko` na `Uburyo bw'insanganyamatsiko`: guhindura Interface.
       - umurongoBackupPath`: inzira y'umurongo wa LND.
       - `lnServerUrl`: URL y'uruzitiro rwawe rw'umuravyo (nk'akarorero `https://127.0.0.1:8080`).



**Tangira umukozi wa RTL**: Mu bubiko bwa RTL, genda :



```bash
node rtl
```



Porogaramu iratangura kandi ishobora gushikirizwa kuri `http://umushitsi w'aho hantu:3000`.



**(Ihitamwo) Gukoresha RTL nk'igikorwa**: Kugira ngo utangure ubwavyo, rema systemd :



Kugira ngo ubikore:




- Ugurure terminal ku mashine yawe.
- Rema dosiye nshasha y'umurimo n'itegeko rikurikira (subiriza `nano` n'umuhinduzi ukunda):


```bash
sudo nano /etc/systemd/system/RTL.service
```




- Kopa kandi ushire ibirimwo aha hepfo muri iyi dosiye:



```ini
[Unit]
Description=Ride The Lightning web UI
Wants=lnd.service
After=lnd.service

[Service]
ExecStart=/usr/bin/node /chemin/vers/RTL/rtl
User=<votre_user>
Restart=always
TimeoutSec=120
RestartSec=30

[Install]
WantedBy=multi-user.target
```





- Subiriza `/inzira/to/RTL/rtl` n'inzira nyayo ija kuri dosiye `rtl` ku mashini yawe, na `<your_user>` n'izina ryawe ry'ukoresha rya Linux.
- Bika kandi ufunge dosiye.
- Subiramwo imiterere ya sisitemu:


```bash
sudo systemctl daemon-reload
```




- Gukoresha no gutangura serivisi ya RTL:


```bash
sudo systemctl enable RTL
sudo systemctl start RTL
```



RTL ubu izotangura ubwayo igihe cose imashini isubiye gukora. Ushobora kumenya uko bimeze ukoresheje :


```bash
sudo systemctl status RTL
```



### Gushiramwo biciye ku Mutaka



Niwakoresha [Umutaka](https://getumbrel.com), gushiramwo RTL biroroshe cane:





- Ushobora gushika ku mutaka Interface (kenshi uciye kuri `http://umutaka.aho hantu`)
- Genda kuri **Iduka ry'amaporogarama**
- Rondera "Gera ku Muravyo"



**Iciyumviro gihambaye: hariho porogaramu zibiri zitandukanye za RTL muri Umbrel App Store:**




- Gutwara Umuravyo** (ku LND): kugira ngo ukoreshe n'urudodo rw'Umuravyo rwa Umbrel (LND).
- Ride The Lightning (Umuco w'Ishingiro)**: ukoreshe gusa iyo washizeho porogarama ya *Core Lightning* kuri Umbrel kandi wipfuza gucunga iyi node ukoresheje RTL.



*Verisiyo yose ya RTL irategurwa mbere kugira ngo ivugane n’ugushirwa mu ngiro guhuye (LND canke Core Lightning). Niba utarahindura node yawe ya Lightning, uhitemwo gusa verisiyo ya kera ya LND*



![Fiche de l'application Ride The Lightning dans Umbrel : présentation de l'app avec captures d'écran et bouton violet "Install" en haut à droite](assets/fr/02.webp)





- Fyonda kuri **Shiraho**



![Fenêtre d'affichage du mot de passe par défaut après installation de RTL dans Umbrel, avec bouton "Open Ride The Lightning"](assets/fr/03.webp)



**Igihambaye:** Inyuma yo gushiramwo, RTL yerekana igicapo gifise ijambobanga ry'imbere. **Kopa ubike iri jambobanga** - uzorikenera kugira winjire muri Interface RTL. Iri jambobanga rizogaragara igihe cose RTL itanguye gushika ushitse ku nzira ya "Ntuzosubire kuyigaragaza".



Umutaka uhita witaho :




- Gukuraho no gutunganya RTL
- Gutunganya ukwinjira ku nzira y'umuravyo
- Gucungera ivyavuguruwe
- Gukingira uburenganzira bwo gushika kuri Interface



Iyo umaze gushiramwo, iyo porogaramu iraboneka muri *Apps* yawe kuri Umbrel. Fyonda kuri **Gutwara Umuravyo** kugira ngo uyitangure.



![Écran de connexion RTL via Umbrel : champ de mot de passe avec logo du cheval en haut à gauche, bouton "Login"](assets/fr/04.webp)



Ku rubuga rwo kwinjira, shiramwo ijambobanga wakopiye mbere. Iyo umaze kwinjira, Interface web RTL izoshobora gushikwako ataco uhinduye uhereye ku rubuga rwa Umbrel, ata yindi ntunganyo ikenewe!



## 4. Gutanguza no gukoresha Interface RTL .



None ko RTL iriko irakora, reka twihweze urubuga rwayo rwa Interface n’ibintu nyamukuru biyigize. Tuzoca mu bice bitandukanye vy’ivyo usaba kugira ngo tubahe inyishu yuzuye.



### Igipande nyamukuru c'ubugenzuzi



![Tableau de bord RTL : solde Lightning, solde on-chain, capacité de liquidité entrante/sortante et création de facture](assets/fr/05.webp)



Ukimara kwinjira, uca ushika ku **dashboard nyamukuru**, iguha icegeranyo c'uruzitiro rwawe rwa Lightning. Iyi paji ishira hamwe amakuru y'ingenzi:




- Uburinganire bwawe bwose bw'umuravyo
- On-Chain irahari
- Ugusenyuka kw'amahera yawe (yinjira/isohoka)
- Ukwihuta kohereza no kwakira Satss biciye ku nzira yawe y'umuravyo



### Uburongozi bw'amafaranga On-Chain



![Onglet "On-chain" actif dans RTL : solde Bitcoin (en sats, BTC, USD), et liste des transactions avec type d'adresse Taproot](assets/fr/06.webp)



**On-Chain** tab ishobora kugufasha gucunga ama bitcoins yawe ataco uhinduye ku ruhererekane nyamukuru:




- Iyerekanwa ry'uburinganire mu bice bitandukanye (Sats, BTC, USD)
- Urutonde rw'ibikorwa
- Uruvyaro rwa Address Taproot (P2TR), P2SH (NP2WKH) canke Bech32 (P2WKH)
- UTXO ubuyobozi, kwakira no kohereza bitcoins



### Umuravyo: igaragaza ido n'ido ry'ibice



Interface RTL ifise urutonde rwo ku ruhande rwerekeye Lightning Network, rukoranya ibikorwa vyose bihambaye vyo gucunga urudodo rwawe. Aha niho hari ido n'ido ry'ivyo bimenyetso, mu rutonde rw'ivyo bishushanyo:



#### 1. Abo mu runganwe/Imirongo



![Vue de gestion des canaux Lightning (onglet "Peers/Channels" ouvert)](assets/fr/07.webp)



Iyi nkuru iraguha uburenganzira bwo :




- Raba urutonde rw'abo mu runganwe rwawe bahuye n'imirongo ya Lightning yuguruye canke irindiriye.
- Yongerako umugenzi mushasha (huza n'iyindi nzira y'umuravyo).
- Gufungura, gufunga canke gucunga imihora iriho.
- Raba ido n’ido ry’umurongo wose: ubushobozi, amafaranga yo mu karere/yo kure, ikibanza, amateka y’ubudandaji, amanota y’amafaranga, n’ibindi.



#### 2. Ibicuruzwa



![Historique des transactions Lightning (onglet "Transactions" > "Payments")](assets/fr/08.webp)



Muri iyi nkuru, ushobora :




- Wohereze amahera y’umuravyo (biciye kuri Invoice).
- generate no gucunga amafagitire kugira ngo uronke amahera.
- Raba amateka yose y’amahera yoherejwe n’ayakiriwe, n’ibindi (umubare, itariki, ikibanza, amahera, umubare w’amahera yasimbutse, n’ibindi).



#### 3. Inzira



Iyi menyu yerekana :




- Ivyishyurwa birungikwa n'uruzitiro rwawe ku bandi bakoresha Lightning Network.
- Imibare y'inzira: umubare w'ibikorwa vyashikirijwe, amafaranga yaronkejwe, amakosa yahuye.
- Amateka yoherezwa hanze kugira ngo asesengurwe neza.



#### 4. Gusubiramwo



Iyi nkuru itanga :




- Raporo zitomoye ku bikorwa vy’uruzitiro rwawe rw’Umuravyo.
- Ivyandiko n'imbonerahamwe ku mihora, ukwishyura, amafaranga, ubushobozi, n'ibindi.
- Ibikoresho vyo gutahura neza ingene node yawe ikora.



#### 5. Gushaka igishushanyo



Iyi nkuru iraguha uburenganzira bwo :




- Gutohoza ubuhinga bwa Lightning Network.
- Rondera uturongo canke imirongo yihariye.
- Kuronka amakuru yerekeye uguhuza n’ubushobozi bwose bw’urubuga.



#### 6. Sinya/Suzuma



Iyi menyu itanga :




- Ubushobozi bwo gusinya ubutumwa ukoresheje urufunguzo rwa node yawe (ikimenyamenya ca Ownership).
- Igenzura ry'umukono kugira ngo wemeze ubutumwa buva ku zindi nzira.



#### 7. Gusubiza inyuma



Iyi menyu ntoya ni iyo gusubiza inyuma:




- Dosiye y'ububiko bw'umurongo wo hanze (SCB ya LND).
- Gusubizaho imiterere canke imirongo nimba bikenewe.
- Impanuro zo gukingira ama backups yawe.



#### 8. Urudodo/Urusobe



![Vue d'ensemble du nœud Lightning (onglet "Node/Network")](assets/fr/09.webp)



Muri iyi submenu uzosanga :




- Incamake yuzuye y'imimerere y'umurongo wawe w'umuravyo: izina ry'ibanga, verisiyo, ibara, imimerere y'uguhuza.
- Imibare ku mihora (ikora, irindiriye, yugaye), ubushobozi bwose, guhuza.
- Amakuru yerekeye Lightning Network y'isi yose n'aho node yawe iri muri yo.



### Ibikorwa: Guhindura Boltz



![Interface de gestion des swaps avec Boltz (onglet "Services" > "Boltz")](assets/fr/10.webp)



Boltz ni igikorwa c’ubuzima bwite, kitagira ububiko bwa Exchange gihindura amafaranga y’ibice hagati ya Lightning Network na Blockchain Bitcoin (On-Chain). Itanga ubwoko bubiri bw’ibikorwa: Guhindura amazi yo munsi y’amazi (**Guhindura hanze**) n’uguhindura amazi yo munsi y’amazi (**Guhindura amazi**).



#### Guhindura (Guhindura Ubwato bwo mu Mazi)



Swap Out ihindura Satss iri kuri Lightning Network ikayigira amafaranga y’ibiceri On-Chain. Ubu buryo burakenewe iyo node ipfuye ubushobozi bwo kwinjira, canke iyo ushaka gusubiza amahera kuri On-Chain Address. Ivyo bigenda gutya:




- Uwukoresha ahitamwo umubare wo guhindura
- Igikoresho cohereza amahera y'umuravyo kuri Boltz
- Mu Exchange, Boltz ahagarika amahera angana n’ayo mu biceri vya On-Chain
- Iyo iyo nzira yemejwe, uwuyikoresha arashobora gusaba ayo mahera mu guhishura ibanga ryakoreshejwe mu guhindura amahera .



Iyi nzira ntabwo ari iyo kubika, Boltz ntiyigera afata amahera y’uwukoresha.


![Double capture des étapes de configuration d'un swap-out](assets/fr/11.webp)



#### Guhindura mu (Guhindura mu bwato bwo munsi y'amazi)



Ku rundi ruhande, Swap In iremeza ko amahera ya On-Chain asubira kwinjizwa muri Lightning Network. Ivyo ni ngirakamaro cane cane mu kugarura ubushobozi bwo gusohora ku mihora yawe. Uburyo bwo kubikora ni ubu:




- Uwukoresha yohereza ama bitcoins kuri Address yihariye yakozwe na Boltz .
- Aya mahera ashobora kurekurwa na Boltz gusa iyo yishuye Lightning Invoice ivugwa n’urudodo rw’uwukoresha .
- Iyo Invoice imaze kwishurwa, ayo mahera araboneka ku muhora wa Lightning, ivyo bikaba bituma iyo node igira ubushobozi bwo gutanga umusaruro .



![Configuration d'un swap-in](assets/fr/12.webp)



Ubu buryo bubiri buratuma amafaranga y’umurongo wa Lightning ashobora gucungirwa neza, mu gihe uwukoresha aguma afise ubusegaba ku mahera yiwe.



### Gutunganya no guhindura uko ushaka



![Écran de configuration du nœud (onglet "Node Config")](assets/fr/13.webp)



**Node Config** tab iragufasha guhindura ubumenyi bwawe:




- Gukoresha imirongo itamenyeshejwe
- Guhindura uko ugurisha kwerekana
- Block explorer imiterere
- Guhindura Interface



### Inyandiko n'imfashanyo



![Section d'aide de RTL (onglet "Help")](assets/fr/14.webp)



Ubwa nyuma, igice ca **Imfashanyo** kiratanga inyandiko zitomoye ku :




- Imiterere y'intango
- Uburongozi bw'urunganwe n'umurongo
- Ukwishura n'ugucuruza
- Gusubiza inyuma no kugarura
- Raporo n'imibare
- Imikono n'igenzura
- Urudodo n'imirongo y'ikoreshwa



Iyi Interface iragufasha gucunga neza urudodo rwawe rwa Lightning, kuva ku bikorwa vy'ishimikiro gushika ku bikorwa vy'imbere, vyose mu Interface yoroshe kandi itunganijwe neza.



## 5. Ikoreshwa riteye imbere n'umutekano



Muri iki gice, ng'ibi ivyo ukwiye kumenya kugira ngo ugende kure na RTL kandi ukingire node yawe ya Lightning:



### Gukurikirana no gutorera umuti ingorane



Kugira ngo ukurikirane urudodo rwawe, ushobora kwohereza hanze amakuru ya RTL (ibitabo, CSV) maze ukayabona mu bikoresho nka Grafana. Iyo habaye ingorane (ukwishura kwabujijwe, umurongo udakora), raba ibitabo vya LND/CLN maze ukoreshe amabwirizwa yo gupima (`imirongo y'urutonde lncli`, `imirongo irindiriye lncli`, n'ibindi). RTL kandi itanga ibitabo vya Interface vyo kugenzura ibintu bishika mu nzira.



### Ukwinjira kure gutekanye



Ntukigere ugaragaza RTL ataco uhinduye kuri Internet. Guhitamwo :




- VPN** (nk'akarorero Tailscale) ku kwinjira mu bwiherero, mu buryo bupfutse
- Tor** kugira ngo umuntu ashobore gushika ku mutekano, ata mazina
- Guhindura umugenzuzi **HTTPS** (Nginx/Caddy) gusa iyo uzi uko wobitunganya



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Ivyiza vyo kwirinda





- Rinda uburenganzira bwawe**: ntukigere usangira admin.macaroon canke ijambobanga ryawe rya RTL. Guhagarika uruhusha ku madosiye y'agaciro.
- Ivyiyumviro bihoraho**: sohereza hanze dosiye y'ivy'imirongo (SCB) inyuma y'uguhindura kwose maze uyibike hanze y'uruzitiro.
- Ivyashizwe ku rubuga**: ushire RTL, node yawe na Umbrel ku gihe n'ivyo gukosora umutekano bishasha.
- Ibanga**: gukingira amakuru n’amafoto imbere y’uko ubisangiza abandi. Ntukigere usangira amahera yawe canke urutonde rw’urunganwe rwawe ku mugaragaro.
- Ukwinjira kumwe**: RTL si ugukoresha benshi. Ntusangire uburenganzira bw'ubuyobozi. Kugira ngo ushobore gusoma gusa, koresha amakaroni yihariye nimba bikenewe.



Mu gukurikiza izo ngingo ngenderwako, uragabanya cane ingorane kandi ugakomeza kugenzura urudodo rwawe rw’Umuravyo.



## 7. Insozero



**Ride The Lightning** ni igikoresho gihambaye co gucunga neza urudodo rwa Bitcoin/Lightning, waba uri uwutangura canke uwuteye imbere. Itanga Interface igaragara yo kugenzura imihora yawe, ukwishyura n'ubuzima bw'ibihimba, mu gihe urushiriza gutahura Lightning Network.



RTL iratandukanye n’izindi kubera ko ishobora gushirwa mu ngiro vyinshi, ibikorwa vyayo biteye imbere (gusubiramwo, guhinduranya, gutanga raporo) n’uburyo bwo kwigisha. Ku bikenewe vyoroshe, Interface Umbrel canke Wallet mobile bizoba bihagije, ariko RTL irafise insiguro nziza cane ku bijanye n’ugucungera neza amanode.



Kugira ngo umenye vyinshi :




- Urubuga rwemewe rwa RTL: https://www.amakuru y'umuravyo/
- GitHub RTL: gutwara-umuravyo/RTL
- Reddit r/umuravyo**: [r/umuravyo](https://www.reddit.com/r/umuravyo) - Ibiganiro vy'ubuhinga, amatangazo y'umugambi, inyishu n'ibikoresho vy'inyigisho
- Ihuriro ry'abanyagihugu ry'Umutaka**: [abanyagihugu.
- Lightning Network Abahinguzi**: [github.com/umuravyo](https://github.com/umuravyo) - Ububiko buzwi bwa GitHub bwo gukurikirana iterambere no gutanga kode y'inkomoko
- - Ibibazo n'inyishu vy'ubuhinga n'abahinguzi n'abakoresha bateye imbere



Muri make, RTL iraguha ububasha bwose ku nzira yawe y'umuravyo, mu gihe ca none, gifise ubushobozi bwose Interface.



**Isoko :** Urubuga rwemewe rwa RTL; RTL Igihugu; Iduka ry’Iporogarama ry’Umutaka; Umuryango w’Umutaka; Gahunda B Ivyuma vy’urubuga.



Kugira ngo urushirize gutahura ingene Lightning Network ikora, ndagusavye kandi gufata iri shure ry’ubuntu:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb