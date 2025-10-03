---
name: Dojo
description: Inkomoko yuguruye Bitcoin y'ubuzima bwite n'ukwigenga
---

![cover](assets/cover.webp)



*Iyi nyigisho ishingiye ku [nyandiko za Ashigaru](https://ashigaru.rs/docs/), nazifashe nkazigura. Nasubiyemwo ibice vyose kugira ngo bimenyekane neza, nongerako n’izindi nsobanuro zitomoye, be n’ibigereranyo vy’abatangura, kugira ngo gushiramwo no gukoresha vyorohe gutahura.*



---

Dojo ni porogarama yuguruye yateguwe gukora nk’umukozi w’inyuma ku bikoresho bimwebimwe vy’ubuzima bwite vy’amasakoshi ya Bitcoin, bishingiye ku nzira ya Bitcoin core. Mu mateka, yateguwe kugira ngo ikore na Samourai Wallet, Wallet igendagenda yatanga ubuhinga buteye imbere bwo gucungera ubuzima bwite nka Whirlpool (CoinJoin), Ricochet, Stonewall, PayNym... kuri Dojo kugira ngo ushireho ubumenyi bushitse ku bakoresha bipfuza kuguma bagenzura amakuru yabo igihe bakoresha Bitcoin.



![Image](assets/fr/01.webp)



Mu majambo ngirakamaro, Dojo ikora nk’irembo hagati ya Wallet yawe n’urubuga rwa Bitcoin. Iyo ata Dojo, Wallet igendagenda yoroshe yobwirizwa kubaza abakozi b’abandi kugira ngo ibone ikibanza c’ama UTXO yawe n’amateka yawe, canke ngo itangaze amafaranga yawe. Ivyo bisigura ko amakuru y’agaciro ashobora gukoreshwa no gusohoka kuri server y’uwundi muntu (amaderesi akoreshwa, amafaranga, incuro umuntu yishura, n’ibindi). Na Dojo, urakira iyi server wewe nyene, uhuye n’uruzitiro rwawe rwa Bitcoin. Muri ubwo buryo, ivyo usaba vyose mu bitabo vyawe bica mu bikorwa remezo ugenzura, ata bahuza, bikomeza ibanga ryawe n’ubusegaba bwawe.



## Ibisabwa kugira ngo umuntu ashobore gushinga Dojo



Gushinga server ya Dojo ntibisaba imashini ikomeye cane. Umuntu wese afise mudasobwa y’urugero rwo kwinjira, afise Internet ihamye kandi afise ubushobozi bwo kuyisiga ikora ubudasiba (24/7) arashobora gushinga Dojo ikora.



### Hitamwo ubwoko bw'imashini yawe



Ushobora gukoresha :




- laptop ;
- mudasobwa yo ku biro ;
- PC ntoyi (nk’akarorero Intel NUC, Lenovo ntoyi...).



Ihitamwo ryose rifise ivyiza n'ibibi vyaryo:




- Igiciro: mini-PC canke desktop yasanuwe kenshi izoba ihendutse kuruta laptop nshasha.
- Ikirenge: Mini-PC ifata umwanya muto.
- Power Supply: laptop ifise akamaro ko kuba ifise bateri, bisigura ko itazozima iyo umuriro wacitse, bitandukanye na mini-PC.
- Ugushobora gusubiramwo: barbones muri rusangi zigufasha kwongerako ububiko canke gusubirira mu buryo bworoshe disiki ya Hard.



Kugira ngo umenye vyinshi ku bijanye no guhitamwo ibikoresho vyawe, ndagusavye gufata iri shure:



https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

### Ibikoresho vyiza



Ntaco bimaze kugura imashini nshasha. Mudasobwa yasanuwe ifise ibimenyetso biri aha hepfo izotanga ubushobozi bwiza cane kuruta ivyuma vy’ubuhinga bwa none bifise urupapuro rumwe (nka Raspberry Pi).



**Ibisobanuro bikeyi:**




- X86-64 ubwubatsi (umurongozi w’ibice 64).
- 2 GHz y’ivyuma bibiri canke vyihuta kuruta.
- 8 GB RAM ni ntoyi.
- 2 TB canke zirenga NVMe SSD (kugira ngo ubike Blockchain ya Bitcoin n’ibiharuro bikenewe).



**Uburyo bwo gukoresha bwiza: **




- Igikoresho gishingiye kuri Debian, nka Ubuntu 24.04 LTS.



**Ibikoresho vyiza:**




- HP EliteDesk / Igitabo c'abanyabwenge
- Dell OptiPlex
- Lenovo IvyiyumviroIkigo / IvyiyumviroPad
- Intel NUC
- n'ibindi.



Birashoboka cane gukoresha server ya Dojo ku bindi bikoresho. Ariko rero, kugira ngo ubone ibikorwa vyiza kandi ugabanye ingorane, turaguhanura gukurikiza izo mpanuro zivuzwe haruguru.



Muri iyi nyigisho, nzoba ndiko nkoresha ThinkCentre Tiny ya kera ifise umurongo wa Intel Pentium G4400T, RAM 8 GB na SSD 2 TB.



## 1 - Gushiramwo Ubuntu



*Niba wipfuza gushiramwo Dojo ku gikoresho gisanzwe gitunganijwe, urashobora gusimbuka iyi ntambwe maze ukaja ku ntambwe ya 2.*



Amaze gutegura ibikoresho vyatowe, ni igihe co gushiramwo ubuhinga bwo gukoresha. Ushobora gukoresha hafi uburyo bwose bwo gutanga Debian, ariko ndagusavye guhitamwo verisiyo ya LTS ya Ubuntu, kuko ihuye neza n'intumbero zacu. Dore intambwe zo gukurikira:



### 1.1. Rema urufunguzo rwa USB rushobora gufungurwa



Ku mudasobwa isanzwe ikora (imashini yawe isanzwe), fungura ishusho ya Ubuntu LTS ISO [ku rubuga rwemewe](https://ubuntu.com/download/desktop) (`24.04` igihe c’ukwandika, ariko ufate iyo nshasha nimba hari iyindi iriho).



![Image](assets/fr/02.webp)



Injira urufunguzo rwa USB rwo nibura 8 GB muri iyi mudasobwa, hanyuma ureme urufunguzo rushobora gutangura ukoresheje porogarama nka [Balena Etcher](https://etcher.balena.io/). Hitamwo ishusho ya Ubuntu ISO uherutse gukuraho, uhitemwo urufunguzo rwa USB nk’igikoresho ushaka, hanyuma utangure igikorwa co kurema (wihangane, bishobora gutwara iminota myinshi).



![Image](assets/fr/03.webp)



Injira urufunguzo rwa USB rushobora gutangura muri mudasobwa izimye (iyo ushaka gukoresha Dojo). Tangira imashini maze uce ukanda **F12** canke **F10** kuri keyboard yawe (bivanye n’ivyo ukoresha) kugira ngo ugere kuri boot menu. Hanyuma uhitemwo urufunguzo rwawe rwa USB nk’igikoresho c’imbere mu rutonde rwo gufungura mudasobwa.



![Image](assets/fr/04.webp)



### 1.2. Gushiramwo uburyo bwo gukoresha



Igishushanyo c'inzu c'Ubuntu kiraboneka. Hitamwo "Gerageza canke Shiraho Ubuntu*".



![Image](assets/fr/05.webp)



Hanyuma ukurikize uburyo bwa kera bwo gushiramwo Ubuntu:




- Hitamwo ururimi.
- Hitamwo ubwoko bwa klavye.
- Niba uhuye n’umugozi wa RJ45, ntaco ukeneye guhindura Wi-Fi.
- Fyonda kuri "*Install Ubuntu*" hanyuma usuzume uburyo bwo gushiramwo porogaramu z'abandi (abashoferi ba Wi-Fi, ama codecs y'ivy'amakuru, n'ibindi).
- Igihe umupfumu asavye ubwoko bw'ugushiramwo, hitamwo "*Gukuraho disiki maze ushiremwo Ubuntu*". **Imburi**: iki gikorwa kizofuta vyose ibirimwo kuri disiki. Suzuma neza ko iyo disiki wahisemwo ihuye na NVMe SSD yagenewe Dojo.
- Rema izina ry'ukoresha ryoroshe (nk'akarorero "*loic*").
- Guha izina imashini (nk'akarorero "*dojo-node*").
- Shiraho ijambobanga rikomeye kandi urizigame.
- Gukoresha "*Saba ijambobanga ryanje kugira ngo winjire*" kugira ngo ukomeze umutekano.
- Erekana isaha yawe, hanyuma ukande kuri "*Install*".
- Rindira ko iyo installation irangira. Iyo bimaze kurangira, iyo sisitemu izosubira gukora ubwayo.
- Kuraho urufunguzo rwo gushiramwo USB igihe usubiye gufungura mudasobwa.



Ku bindi bisobanuro ku buryo bwo gushiramwo Ubuntu, usabwe kuraba inyigisho yacu yihariye :



https://planb.network/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

### 1.3. ivugurura rya sisitemu



Inyuma y’ugufungura kwa mbere, fungura terminal ukoresheje urufunguzo ***Ctrl + Alt + T*** hanyuma ukoreshe aya mabwirizwa akurikira kugira ngo uhindure sisitemu:



```bash
sudo apt update
sudo apt upgrade -y
```



![Image](assets/fr/06.webp)



## 2. Gushiraho inyubakwa zo hanze



Kugira Dojo ikore neza, amatafari amwe amwe ategerezwa kuba ari kuri system yawe. Ivyo bikoreshwa mu gucunga ububiko bwa porogarama, guhanahana amakuru, gukuraho ububiko n’ugukora Dojo imbere mu bikoresho vya Docker. Ivyo bikorwa vyose bikorerwa mu kibanza c’indege.



### 2.1. Gutegura



Itegeko rikurikira rigusubiza muri dosiye yawe bwite. Ivyo ni akamenyero keza imbere yo gukoresha urutonde rw’ibintu vyo gushiramwo.



```bash
cd ~/
```



Imbere yo gushiramwo porogarama iyo ari yo yose, nurabe neza ko urutonde rw’ibintu biri kuri mashini yawe ruri ku gihe. Ivyo bituma udashobora gushiramwo verisiyo zitagikoreshwa.



```bash
sudo apt-get update
```



![Image](assets/fr/07.webp)



### 2.2. Gushiramwo ibikoresho



Ibikoresho vyinshi birakenewe kwongerwa kuri iyo sisitemu:




- `apt-gutwara-https`: bigufasha gukuraho amapakete mu mutekano biciye kuri HTTPS
- `ca-certificates`: icungera ivyemezo bisabwa ku mahuriro yashizwemwo
- `curl`: kugarura amadosiye kuri interineti
- `gnupg-umukozi`: ku buyobozi bw'urufunguzo rwa GPG
- porogaramu-imiterere-isanzwe`: itanga ubufasha bwo gukoresha ububiko bwa APT
- `unzip`: gufungura dosiye mu buryo bwa ZIP



```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common unzip
```



Mu gihe co gushiramwo, iyo sisitemu ishobora kugusaba kwemeza. Kanda urufunguzo "*y*", hanyuma ukande "*Injira*".



![Image](assets/fr/08.webp)



### 2.3. Gushiramwo amasogisi



Torsocks ituma amabwirizwa amwamwe ashobora gushirwa mu ngiro biciye ku rubuga rwa Tor, ivyo bikaba bituma ivy’itumanaho biguma ari ibanga.



```bash
sudo apt install torsocks
```



![Image](assets/fr/09.webp)



### 2.4. gushiramwo Docker na Docker



Dojo ikora imbere mu bikoresho vya Docker. Ivyo bisigura ko igikorwa cose kiri ukwaco mu kibanza cigenga, ivyo bikaba bituma vyoroha gucungera no gucungera umutekano. Kugira ngo ubikore, ukeneye gushiramwo Docker n’igikoresho ca Docker Compose, kigufasha gucunga ibikoresho vyinshi igihe kimwe.



#### Kwongera urufunguzo rwo gusinya rwa Docker



Docker itanga urufunguzo rwayo rw’umukono wa digitale. Kuyishiramwo bigenzura ukuri kw’amapaki yashizwe kuri interineti.



```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```



![Image](assets/fr/10.webp)



#### Ububiko bwemewe bwa Docker bwongeweko



Igikurikira, ukeneye kubwira sisitemu aho yosanga amapaki ya Docker yemewe. Iri tegeko ryongera ububiko bushasha ku miterere y'umucungerezi w'amapaki yawe.



```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "*$VERSION_CODENAME*") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```



![Image](assets/fr/11.webp)



#### Gushiramwo Docker na Docker



Ibice nyamukuru vya Docker ubu birashobora gushirwamwo.



```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```



![Image](assets/fr/12.webp)



#### Uruhusha rw'ukoresha



Ku mburabuzi, amabwirizwa gusa ashirwa mu ngiro n'uburenganzira bw'umuyobozi ashobora gutanguza Docker. Kugira ngo bibe vyiza cane, ndagusavye kwongerako umukoresha wawe w'ubu ku mugwi "*docker*". Ivyo bigufasha gukoresha Docker utabwirizwa kwandika `sudo` igihe cose.



```bash
sudo usermod -aG docker $USER
```



![Image](assets/fr/13.webp)



## 3. Guhingura umukoresha umwe (ntibikenewe)



Niba ushaka gutuma umutekano wa sisitemu yawe utera imbere, ndagusavye ko worema umukoresha atandukanye akoreshwa gusa Dojo. Ukwo gutandukanya kuragabanya ingorane: iyo ingorane y’umutekano ibaye muri Dojo, ntizotuma konti yawe nyamukuru ihungabana.



### 3.1. kurema konti y'ukoresha



Itegeko rikurikira rirema umukoresha mushasha yitwa "*dojo*". Uyu mukoresha azogira ububiko bw'i muhira `/home/dojo` n'uburyo bwo gushika ku nzira ya bash. Bizokwongerwa kandi ku mugwi wa sudo kugira ngo bishobore gushitsa amabwirizwa y'ubuyobozi.



```bash
sudo useradd -s /bin/bash -d /home/dojo -m -G sudo dojo
```



### 3.2. Gushinga ijambobanga



Ni ngombwa gutanga ijambobanga rikomeye kuri iyi konti. Ivyiza, ushobora gukoresha umucungerezi w’ijambobanga nka Bitwarden ku generate ihuriro rirerire, Hard-ku-gukeka.



```bash
sudo passwd dojo
```



Sisitemu izoca igusaba kwinjiza ijambobanga wahisemwo, hanyuma uyimenyeshe ubugira kabiri.



https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

### 3.3. Kwemerera umukoresha gukoresha Docker



Kugira ngo umukoresha "*dojo*" ashobore gutanguza ibikoresho bikenewe kugira ngo Dojo ikore, ategerezwa kwongerwa mu mugwi wa Docker. Ivyo bituma udategerezwa gutangura itegeko ryose `sudo`.



```bash
sudo usermod -aG docker dojo
```



### 3.4. Sisitemu yosubira gutangura



Kugira ngo amahinduka y’imigwi agire ico akora, imashini itegerezwa gusubira gukora.



```bash
sudo reboot
```



### 3.5. Injira n'ukoresha mushasha



Iyo system isubiye gutangura, winjiremwo ukoresheje ***dojo*** login n’ijambobanga wasobanuye mbere. Intambwe zose zikurikira zitegerezwa gukorwa zivuye kuri iyo nkuru yihariye.



## 4. Gukuraho no gusuzuma Dojo .



Imbere yo gushiramwo Dojo, ni ngombwa ko uraba neza ko amadosiye yavuye ku muhinguzi wemewe kandi ko ataco yahinduye. Iyi ntambwe ishingiye ku gukoresha PGP na hashes kugira ngo ugenzure ukuri n’ubutungane bwa dosiye.



### 4.1. kwinjiza urufunguzo rwa PGP rw'umuhinguzi



Gukuraho urufunguzo rwa bose rw'umuhinguzi biciye kuri Tor maze urushire mu rufunguzo rwawe rwo mu karere. Uru rufunguzo ruzokoreshwa mu kugenzura imikono ijana n'amadosiye ya Dojo.



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/14.webp)



### 4.2. gukuraho verisiyo nshasha ya Dojo



Kugarura ububiko bushizwemwo kode y'inkomoko ya Dojo. Muri aka karorero, verisiyo nshasha ni `1.27.0`: hindura itegeko hakurikijwe [verisiyo nshasha hano ku bubiko bwa GitHub](https://github.com/Dojo-Umugambi-Ufunguye-Isoko-Samourai-dojo/ibisohoka).



```bash
torsocks wget -O samourai-dojo-1.27.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.27.0.zip
```



![Image](assets/fr/15.webp)



### 4.3. Gukuraho ibimenyetso vy'intoke n'umukono



Ababikora barasohora dosiye irimwo ibimenyetso vy’intoke vy’ububiko, hamwe n’idosiye yashizweko umukono n’urufunguzo rwabo rwa PGP. Bikureho kugira ngo ugereranye amadosiye yawe mu karere.



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt.sig
```



![Image](assets/fr/16.webp)



### 4.4. Suzuma umukono wa PGP



Suzuma ko dosiye y'urutoke yashizweko umukono n'urufunguzo rwazanywe.



```bash
gpg --verify samourai-dojo-1.27.0-fingerprints.txt.sig
```



Igisubizo kibereye kigaragaza umukono ubereye ufise urufunguzo `E53AD419B242822F19E23C6D3033D463D6E544F6` n'urufunguzo rwa Address `dojocoder@pm.me`. Imburi yoshobora kuboneka ivuga ko urufunguzo rutaremejwe: urashobora kururengagiza.



Ku rundi ruhande, nimba umukono udafise akamaro, uce uhagarika igikorwa co gushiramwo maze wongere utangure kuva mu ntango.



![Image](assets/fr/17.webp)



### 4.5. Suzuma ubutungane bw'ububiko



Harura urutoke rwa SHA256 rwa dosiye yavanwe, hanyuma ufungure dosiye y’urutoke kugira ngo ugereranye izo nkuru zibiri.



```bash
sha256sum samourai-dojo-1.27.0.zip
cat samourai-dojo-1.27.0-fingerprints.txt
```



Nimba izo ntoke zibiri zisa, urashobora kwemera udakeka ko ububiko butahinduwe. Niba zitandukanye, ntugende kure maze usibe amadosiye.



![Image](assets/fr/18.webp)



### 4.6. Gukuraho no gutunganya amadosiye



Igihe igenzura ryarangiye neza, urashobora gufungura ububiko maze ugategura dosiye yihariye gushiramwo Dojo.



```bash
unzip samourai-dojo-1.27.0.zip -d .
mkdir ~/dojo-app
mv ~/samourai-dojo-1.27.0/* ~/dojo-app/
```



![Image](assets/fr/19.webp)



### 4.7. Gusukura amadosiye adakenewe



Gukuraho amadosiye y’igihe gito n’ububiko bw’ibintu bitagikenewe kugira ngo ibidukikije vyawe bibe bisukuye.



```bash
rm -r samourai-dojo-1.27.0 && rm samourai-dojo-1.27.0.zip && rm samourai-dojo-1.27.0-fingerprints.txt && rm samourai-dojo-1.27.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/20.webp)



## 5. Gutunganya Dojo



Dojo ni server y’inyuma ihuriza hamwe ibikorwa vyinshi kugira ngo ukoreshe n’ibikorwa vyawe no gucunga node yawe ya Bitcoin. Ivyo bishobora kuba bigoye, ariko umugambi utanga uburyo bworoshe bushobora gushiramwo no gutunganya ibi bikurikira:




- Dojo (API nyamukuru)
- Bitcoin core (urudodo rwuzuye rwa Bitcoin)
- BTC-RPC Umugenzuzi (urubuga Block explorer)
- Indexer ya Fulcrum (index yihuse y'ibice n'ibikorwa)
- Serveri ya Fulcrum Electrum iboneka ku rubuga rwa Tor
- Serveri ya Fulcrum Electrum iboneka ku rubuga rw'aho hantu
- Ivyemezo vy'ubuyobozi



### 5.1. ivyemezo vy'ubuyobozi



Kugira ngo ushobore gukoresha ibikorwa bitandukanye, ukeneye generate ibimenyetso vyinshi bidasanzwe:




- `UMUKORESHA_RPC_IBIKONI`
- `IJAMBO_BANGA RPC`
- `IJAMBO_BANGA_RY'UMUZI_WANJE`
- myYSQL_UMUKORESHA
- `IJAMBO_BANGA RYANJE`
- nODE_API_URUPFUZO`
- `URUPFUZO_W'UMUGAMBI`
- `UMUGAMBI_JWT_IBANGA`



Ivyo bimenyetso **bitegerezwa kuba bidasanzwe** (ivyo birahambaye cane: ntutegerezwa gukoresha ijambobanga rimwe ku bikorwa vyinshi), bigizwe n’imibare gusa, inyuguti nini n’inyuguti nto (alphanumeric), kandi bikaba bifise uburebure bw’inyuguti 40 kugira ngo ushobore gucungera urugero rwo hejuru. Na none, ndabahimiriza cane gukoresha umucungerezi w’ijambobanga.



### 5.2. Kugera kuri dosiye z'imiterere



Dosiye z'imiterere ya Dojo ziri muri dosiye `conf/`. Kwimukira kuri ubu bubiko:



```bash
cd ~/dojo-app/docker/my-dojo/conf/
```



![Image](assets/fr/21.webp)



### 5.3. Bitcoin core imiterere



Gufungura dosiye y'imiterere ya Bitcoin core n'umuhinduzi w'inyandiko ya nano:



```bash
nano docker-bitcoind.conf.tpl
```



![Image](assets/fr/22.webp)



Muri iyi dosiye, shiramwo ibimenyetso vyavutse:



```
BITCOIND_RPC_USER=your-ID-here
BITCOIND_RPC_PASSWORD=your-password-here
```



⚠️ ***Subiriza `ID-yawe-aha` na `ijambobanga ryawe-aha` n'ama logins yawe bwite (n'ijambobanga rikomeye).***



Ushobora kandi guhindura ubunini bw’ububiko bw’ibintu bukoreshwa na Bitcoin core kugira ngo ukore neza (ushobora mbere gukoresha vyinshi nimba ufise RAM nyinshi):



```
BITCOIND_DB_CACHE=2048
```



Kubika amahinduka yawe no gufunga umuhinduzi :




- kanda `Ctrl + X
- wandike `y`
- hanyuma ukande "*Injira*"



### 5.4. Imiterere ya MySQL



Hanyuma ufungure urutonde rw'amakuru rwa MySQL:



```bash
nano docker-mysql.conf.tpl
```



Urasabwa kwinjiza amakuru yawe yo kwinjira:



```
MYSQL_ROOT_PASSWORD=your-password-here
MYSQL_USER=your-ID-here
MYSQL_PASSWORD=your-password-here
```



⚠️ ***Subiriza `ID-yawe-aha` na `ijambobanga ryawe-aha` n'amajambo yawe bwite yo kwinjira (n'amajambo y'ibanga akomeye kandi yihariye).***



Bika mu buryo bumwe (`Ctrl + X`, `y`, "*Injira*").



![Image](assets/fr/23.webp)



### 5.5. Imiterere y'urutonde rwa Fulcrum



Gufungura dosiye ikurikira:



```bash
nano docker-indexer.conf.tpl
```



Yongerako amaparametere kugira ngo ukoreshe Fulcrum maze uyishiremwo neza muri Dojo :



```
INDEXER_INSTALL=on
INDEXER_TYPE=fulcrum
INDEXER_BATCH_SUPPORT=active
INDEXER_EXTERNAL=on
```



![Image](assets/fr/24.webp)



Igikurikira, hariho uburyo 2, bivanye n’ingene ukora. Niba Dojo ishizwe ku mashini itandukanye na mudasobwa yawe ya misi yose (ku mashini yihariye, server...), shiramwo IP yayo Address mu muhora wawe wo mu karere, nk'akarorero :



```
INDEXER_EXTERNAL_IP=192.168.1.157
```



![Image](assets/fr/25.webp)



Kugira ngo umenye IP Address y’aho hantu y’imashini yawe, fungura iyindi terminal maze winjize itegeko rikurikira:



```bash
hostname -I
```



Ica kabiri: nimba Dojo ikoreshwa kuri mudasobwa yawe ya misi yose, ugumye agaciro mburabuzi kariho muri dosiye y'imiterere :



```
INDEXER_EXTERNAL_IP=127.0.0.1
```



Bika kandi usohoke mu muhinduzi (`Ctrl + X`, `y`, "*Injira*").



### 5.6. Imiterere ya serivisi y'urudodo



Ubwanyuma, fungura imiterere ya serivisi nyamukuru ya Dojo:



```bash
nano docker-node.conf.tpl
```



Urasabwa kwinjiza amakuru yawe yo kwinjira:



```
NODE_API_KEY=your-password-here
NODE_ADMIN_KEY=your-password-here
NODE_JWT_SECRET=your-password-here
```



⚠️ ***Subiriza `ijambobanga ryawe-aha` n'ibimenyetso vyawe bwite (n'amajambobanga akomeye, yihariye).***



![Image](assets/fr/26.webp)



Hanyuma ukoreshe urutonde rw'aho hantu:



```
NODE_ACTIVE_INDEXER=local_indexer
```



Bika kandi usohoke mu muhinduzi (`Ctrl + X`, `y`, "*Injira*").



### 5.7. Ubuyobozi bwo kwinjira



Igihe configuration irangiye, si ngombwa kubika ibimenyetso vyose vyavutse. Ico kimwe gusa kigomba gukizwa ni :



```
NODE_ADMIN_KEY
```



Ukwo kwinjira kuzotuma ushobora kwinjira mu nyuma mu gikoresho co gusanasana Dojo. Ibindi vyose bishobora gukurwa mu mucungerezi w’ijambobanga ryawe canke mu nyandiko zanditswe n’ukuboko. Biguma bishobora gushikwako bivuye mu madosiye y'imiterere ya Dojo iyo ukeneye kubigarura muri kazoza.



## 6. Gushiraho Dojo



Kuri iyi ntambwe, Dojo izoshirwaho kandi itanguzwe ku mashine yawe. Ico gikorwa kizotanguza ibikorwa vyinshi (Bitcoin core, indexer ya Fulcrum, Dojo backend, n'ibindi) kandi gitangure gukorana neza na Blockchain Bitcoin. Ivyo bishobora gutwara imisi myinshi, bivanye n’ivyo ukoresha be n’ivyo ukoresha kuri Internet.



### 6.1. Suzuma ko Docker ikora neza



Imbere yo gutangura gushiramwo, urabe neza ko Docker ikora. Gukoresha itegeko rikurikira:



```bash
docker run hello-world
```



Iri tegeko rikuraho maze rigatanguza agace gatoyi k’ikigeragezo. Niba vyose bikora neza, ushobora kubona ubutumwa busa na :



```
Hello from Docker!
This message shows that your installation appears to be working correctly...
```



![Image](assets/fr/27.webp)



Niba ubu butumwa butagaragara, tangura gusubira gufungura imashini yawe ukoresheje :



```bash
sudo reboot
```



Hanyuma usubire muri konti yawe ya **dojo** wongere ukoreshe itegeko ry’ikigeragezo. Iyo ikosa rigumaho, Docker ntiyashizweho neza. Muri ivyo, subira ku ntambwe `2.4.` ku gushiramwo Docker maze usuzume neza itegeko ryose.



### 6.2. Genda ku bubiko bwo gushiramwo Dojo



Ivyanditswe bisabwa kugira ngo ubishiremwo biri muri dosiye ya `my-dojo`. Kwimukira kuri ubu bubiko:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/28.webp)



Koresha itegeko rya `ls` kugira ngo ugenzure ko dosiye ya `dojo.sh` iriho. Iyi ni yo script nyamukuru ikoresha ubuhinga bwo gushiramwo Dojo no gutangura ibikorwa vyayo vyose.



![Image](assets/fr/29.webp)



### 6.3. Gutangura gushiramwo



Tangira gushiramwo ukoresheje :



```bash
./dojo.sh install
```



Wemeze ko washizeho ukanda `y` hanyuma "*Enter*".



![Image](assets/fr/30.webp)



Iyi nyandiko izo :




- gukuraho no gutanguza ibikoresho vya Docker bikenewe,
- gutangura Bitcoin core maze utangure guhuza Blockchain,
- gutangura urutonde rwa Fulcrum kugira ngo ukurikirane ibikorwa n'amaderesi,
- gukoresha inyuma ya Dojo na APIs zayo.



Uzobona uruzi rudahinduka rw'ibitabo bigendagenda, n'ibimenyetso vy'amabara nka `bitcoind`, `soroban`, `nodejs` canke `fulcrum`. Ivyo bigaragaza ko Dojo iriko irakora kandi itanguye gukora ibikorwa bitandukanye.



![Image](assets/fr/31.webp)



### 6.4. Sohoka mu gitabo c'iyerekanwa



Ivyanditswe bigaragara mu gihe nyaco mu kibanza cawe. Kugira ngo usubire ku nzira y'itegeko mu gihe Dojo iriko irakora inyuma, wandike :



```
Ctrl + C
```



Ntuhagarike umutima: guhagarika iyerekanwa ry'inyandiko ntibihagarika ibikorwa. Docker irabandanya ikoresha Dojo mu nyuma (biragaragara ko udakeneye guhagarika mudasobwa nimba ushaka ko IBD ikomeza).



### 6.5. Gutahura *Igice ca mbere co gukuraho* (IBD)



Mu gutangura, Bitcoin core itegerezwa gukuraho no kugenzura Blockchain yose kuva mu 2009. Iyo ntambwe yitwa ***Gukuraho Ivya mbere* (IBD)**. Ni ngombwa, kuko bishoboza Dojo node yawe kugenzura buri block ya Bitcoin n’ibikorwa vy’ubudandaji vyigenga.



Igihe ivyo bihuza bizomara kivana n’ibintu vyinshi:




- ubushobozi bwa processeur yawe n'ingero ya memory ya RAM iriho,
- umuvuduko wa disiki yawe,
- umubare n'uburyo bw'urunganwe urudodo rwawe ruhuza,
- umuvuduko w’urubuga rwawe rwa Internet.



Mu bikorwa, iyo operation muri rusangi ifata hagati y’imisi **2 n’imisi 7**. Muri ico kiringo, urashobora gusiga imashini yawe iguma ikora. Uko iyo mashini imara igihe kirekire ikora, ni ko n’ivyo gukorana bizoheza vyihuta. Ndaguhanura ko wosuzuma uko uguhuza ibintu bimeze ubudasiba mu kuraba ibitabo vya Bitcoin core, canke mu gukoresha igikoresho co gucungera Dojo kimaze gushirwaho (raba igice gikurikira).



Kugira ngo urushirizeho ubumenyi bwawe ku vyerekeye IBD, muri rusangi, ku bijanye n’ingene urudodo rwawe rwa Bitcoin rukora be n’uruhara rwarwo, ndagusavye urabe iri shure:



https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426


## 7. Gukurikirana ivy'uguhuza



Igihe ushizeho Dojo ku ncuro ya mbere, ukeneye kurindira ko ibikorwa bibiri nyamukuru biheza: gukuraho vyose Blockchain Bitcoin (*IBD*) no gushiramwo index y’iyi Blockchain na Fulcrum. Bivanye n’uko ukoresha ubuhinga bwawe n’ububasha bw’imashini, ivyo bishobora gutwara imisi myinshi. Muri ico gihe, urashobora gukurikirana ingene ivyo bikorwa bigenda kugira ngo umenye neza ko vyose bigenda neza.



Hari uburyo bubiri bwo kugenzura uko ivy'uguhuza bimeze:




- gukoresha Igikoresho co Gucungera Dojo (canke DMT), kikaba coroshe ariko kigatanga amakuru make mu gihe ca IBD;
- guhanahana amakuru ataco akora ku bitabo vya Dojo ku mashini yawe, bikaba ari ivy’ubuhinga ariko bikaba ari ivy’ukuri cane.



### 7.1. Suzuma biciye ku gikoresho co gusanasana Dojo (DMT)



Igikoresho co gucungera Dojo ni igikoresho gitekanye, gishingiye ku rubuga Interface kigufasha kugenzura uko uruganda rwawe rumeze, no gukora ibikorwa bimwebimwe. Ni uburyo bworoshe kandi bushoboka bwo kugenzura ingene IBD itera imbere. Mu gihe c’intango co guhuza, amakuru yerekanwa yoshobora kuba make. Nk’akarorero, DMT ntiyerekana ingene indexing ya Fulcrum itera imbere mu buryo burambuye. Ku rundi ruhande, iyo guhuza birangiye, DMT izokwerekana neza :




- amatara yose ari kuri Green;
- igice ca nyuma cemejwe ku gikorwa cose (Igikoresho, Indexer, Dojo DB).



Kugira ngo uyironke, ukeneye kumenya URL ya DMT yawe maze ukayifatanya [biciye mu mucukumbuzi wa Tor](https://www.torproject.org/download/). Kugira ngo ubikore, fungura urubuga maze uje ku bubiko bwa `/my-dojo`:



```bash
cd ~/dojo-app/docker/my-dojo
```



Hanyuma ukoreshe itegeko rikurikira:



```bash
./dojo.sh onion
```



![Image](assets/fr/32.webp)



Uzoheza ubone amakuru yose yerekeye amahuza na Dojo yawe biciye kuri Tor. Ico dushaka hano ni URL ikurikira:



```
Dojo API and Maintenance Tool =
```



Kugira ngo ushikire DMT ukoresheje imashini iyo ari yo yose iri ku rubuga urwo ari rwo rwose (mbere no kure), fungura Tor Browser maze winjize iyi URL ikurikiwe na `/admin`. Nk'akarorero, nimba URL yawe ari `wo4zobymdl`, uzokenera kwinjira mu mucukumbuzi wa [Tor](https://www.torproject.org/download/) bar:



```
wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion/admin
```



⚠️ **Ndasavye ko iyi Address muyigumye ari ibanga ryose



Uzoca urungikwa kuri paji y'ukwemeza. DMT yinjira ikoresheje ijambobanga `NODE_ADMIN_KEY` washizeho mbere.



![Image](assets/fr/33.webp)



Iyo umaze kwinjira, urashobora gushika ku *Igikoresho co Gucungera Dojo*! Mu gihe ca IBD, ushobora kubona amakuru ya "*Latest Block*" mu rutonde rwa "*Full node*", bigufasha kumenya uko urudodo rwawe rwa Bitcoin ruri.



![Image](assets/fr/34.webp)



Ibuka gushiramwo iyi Address muri Tor Browser kugira ngo uzoyironke mu nyuma.



Dojo yawe imaze gukorana neza, ushobora kubona Green check ✅ ku bimenyetso vyose biri kuri paji y’intango ya DMT.



### 7.2. Igenzura biciye mu bitabo vya Dojo



Uburyo bwa kabiri bwo gukurikirana ingene IBD yawe itera imbere ni ukuraba neza ibitabo vy’imashini yawe. Ubwo buryo buratanga ukugenzura gutomoye cane, mu gihe nyaco. Ushobora kubona ingene Bitcoin core iriko iratera imbere mu gukuraho ama blocs, n’ingene Fulcrum iriko irayashira mu rutonde.



Huza n’imashini yakira Dojo yawe maze ufungure terminal. Amabwirizwa yose akwiye gushirwa mu ngiro avuye mu bubiko bwa `my-dojo`. Ishire muri iyi dosiye:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/35.webp)



#### Ibiti vya Bitcoin core



Raba ibitabo vya Bitcoin core kugira ukurikirane iterambere rya IBD:



```bash
./dojo.sh logs bitcoind
```



Mu ntango, uzobona igice c'imbere y'uguhuza imitwe y'ibice:



```
bitcoind | Pre-synchronizing blockheader, height : NNNNNN
```



Iyo uwo mubare ushitse ku 100%, Bitcoin core izotangura gukuraho Blockchain yose. Uzobona ingene IBD itera imbere. Kugira ngo umenye uburebure bw'ibarabara, raba agaciro werekanwa na `uburebure=`. Ushobora kandi gukurikira urufunguzo `progress=`, rwerekana ijana ry'iterambere rya IBD.



![Image](assets/fr/36.webp)



Nk'uko bisanzwe, kugira ngo ufunge ibitabo maze usubire ku nzira y'itegeko, koresha `Ctrl + C`.



#### Ibiti vya Fulcrum



Bitcoin core imaze kurangiza gukorana n’umutwe, Fulcrum itangura gukora index ya Blockchain uko igenda. Raba ibitabo vyayo na :



```bash
./dojo.sh logs fulcrum
```



Uzoca ubona uburebure bw'ibara rya nyuma ry'urutonde, ryerekanywe inyuma ya `uburebure:`, hamwe n'ijanisha ry'iterambere ry'urutonde.



![Image](assets/fr/37.webp)



### 7.3. Igiturire c'ububiko bw'amakuru



Fulcrum ni indexer ikomeye cane, ariko gushiramwo kwayo birashobora kuba bigoye, atari kubera uburyo buhambaye bwo gucunga amakuru. Iyo umuyagankuba ucitse canke imashini igahagarara bukwi na bukwi mu gihe c’ugukorana kw’intango, urutonde rw’amakuru rw’indexer rushobora kwonona. Ushobora kubona ibi, nk'akarorero, nimba ufise ibi bikurikira:



```bash
fulcrum | The database has been corrupted etc...
```



**Iciyumviro:** Ubwo bwoko bw'ikosa bukwiye gukosorwa n'isohorwa rya Fulcrum 2.0 rizoza.



Ivyo nivyagushikiye, nta ngaruka bigira kuri bitcoind (node ​​yawe ya Bitcoin): IBD yayo izobandanya itera imbere ataco ikora kuri Fulcrum. Ariko rero, ntuzoshobora gukoresha Fulcrum gushika umaze gukuraho amakuru yayo yononekaye, ugasubira gutangura gukorana na yo kuva mu ntango. Ehe ingene bigenda:



Hagarika Dojo:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Gukuraho gusa igikoresho ca Fulcrum n'umubare:



```bash
docker rm -f fulcrum || true
docker volume ls | grep -i fulcrum
docker volume rm my-dojo_data-fulcrum
```



Mu bisanzwe izina ni `my-dojo_data-fulcrum`, nimba ivyo atari vyo kuri wewe, hindura izina ryagaruwe n'itegeko ry'imbere.



Hanyuma wongere utangure Dojo wongere wubake Fulcrum uhereye ku ntango:



```bash
./dojo.sh upgrade
```



Ushobora rero kumenya ko Fulcrum ikora neza mu kuraba ibitabo:



```bash
docker logs -f fulcrum
```




## 8. Gukoresha igikoresho co gusanasana Dojo



Igihe urudodo rwawe rwa Bitcoin ruzoba rwahuye n’umutwe w’uruzitiro rufise Proof of Work nyinshi, kandi Blockchain ikaba 100% indexed na Fulcrum, urashobora gutangura gukoresha Dojo yawe.



Dojo yawe itanga ibintu vyinshi, biguma vyiyongera uko habaho verisiyo nshasha. Mu vyiyumviro vyanje, 2 bihambaye cane ni :




- ubushobozi bwo gufatanya Ashigaru Wallet yawe kugira ngo ukoreshe node yawe bwite kugira ngo ubone amakuru ya Blockchain no gutangaza amafaranga yawe,
- na Block explorer, biguha uburenganzira bwo kuronka amakuru yerekeye Blockchain Bitcoin utashize amakuru yawe ku kintu co hanze udacungera.



Reka turabe ingene twobikoresha.


### 8.1. Huza Ashigaru na Dojo yawe



Gufatanya Ashigaru Wallet yawe na Dojo yawe biroroshe cane: umaze kuri DMT yawe, fungura urutonde rwa "*Pairing*". Haca haboneka kode ya QR, iyo ushobora kuyicapura ukoresheje porogarama ya Ashigaru.



![Image](assets/fr/38.webp)



Mu gikorwa ca Ashigaru, igihe ca mbere uzoba ugifunguye umaze kurema canke gusubizaho Wallet yawe, uzoca urungikwa kuri paji ya "*Configure your Dojo server*". Kanda "*Scan QR*", hanyuma ushireko kode ya QR yerekanwa kuri DMT yawe.



![Image](assets/fr/39.webp)



Hanyuma ukande kuri buto ya "*Bandanya*".



![Image](assets/fr/40.webp)



Ubu rero warahuye na Dojo yawe.



![Image](assets/fr/41.webp)



### 8.2. Gukoresha igitabu Block explorer



Dojo ihita ishiramwo Block explorer, [BTC-RPC Explorer](BTC-RPC-explorer), ikoresha amakuru ava ku nzira yawe bwite ya Bitcoin. Igikoresho co gutohoza kigufasha kuronka amakuru atagiramwo ivyatsi ava kuri Blockchain na Mempool yawe biciye ku rubuga rwa Interface rworoshe gutahura. Ushobora rero, nk’akarorero, kumenya uko igikorwa kiriko kirategerezwa, kuraba umubare w’amahera y’i Address canke gusuzuma igihimba c’ibarabara bitagoranye.



Kugira ngo uyironke, ushobora gukura Tor Address mu mucukumbuzi wawe. Kugira ngo ubikore, ukoreshe itegeko nyene wakoresheje kugira uronke Address ya DMT yawe:



```bash
./dojo.sh onion
```



![Image](assets/fr/42.webp)



Uzoshobora kuronka amakuru yose y'ihuriro ryawe rya Dojo biciye kuri Tor. Ico dushaka hano ni URL ikurikira:



```
Block Explorer =
```



Niba umaze kwifatanya na DMT yawe, ushobora kandi kubona iyi Address mu "*Pairing*", imbere mu guhuza JSON:



![Image](assets/fr/43.webp)



Kugira ngo ushikire umucukumbuzi wawe ukoresheje imashini iyo ari yo yose iri ku rubuga urwo ari rwo rwose (naho woba uri kure), fungura [Umucukumbuzi wa Tor](https://www.torproject.org/download/) hanyuma winjize URL uherutse kuronka.



⚠️ **Ndasavye ko iyi Address muyigumye ari ibanga ryose



Uzoheza ubone Block explorer yawe bwite.



![Image](assets/fr/44.webp)



*Ishusho: https://ashigaru.rs/.*



Kugira ngo ukurikirane ivy’ugucuruza, ushobora gusa kwinjiza txid yavyo mu kabati k’ugushakisha kari hejuru iburyo.



![Image](assets/fr/45.webp)



*Ishusho: https://ashigaru.rs/.*



Kugira ngo usuzume inyigisho zijanye n’igikoresho ca Address, nugende muri ubwo buryo nyene winjiza Address mu kabati k’ugushaka.



![Image](assets/fr/46.webp)



*Ishusho: https://ashigaru.rs/.*



Ushobora kandi kwinjiza Hash canke uburebure bw'ibarabara mu kabati k'ugushaka kugira ngo ugaragaze ido n'ido.



![Image](assets/fr/47.webp)



*Ishusho: https://ashigaru.rs/.*



## 9. Gutunganya Dojo



### 9.1 Hagarika Dojo yawe



Ntukigere ugabanya ubushobozi bwa Dojo yawe, kuko ivyo bishobora kwonona amakuru amwe amwe, cane cane indexer ya Fulcrum. Niba ubwirizwa kuyizimya, wama ukora ugufunga neza kwa Dojo, hanyuma, iyo uburyo bwose burangiye, uzimye n’imashini:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



### 9.2 Vugurura Dojo yawe



Dojo iratera imbere ubudasiba kandi n’ibindi bishasha birasohoka kugira ngo ikosore ibibazo, itere imbere mu gushikama no kwongerako ibintu. Ni ngombwa rero [guhora usuzuma ko hariho ivyahinduwe](https://github.com/Umugambi-w’Isoko-Yuguruye wa Dojo/samourai-dojo/ibisohoka) no guhindura Dojo yawe. Ivyo bikorwa bisa n’ivyo mu ntango, ariko bisaba ko usubiriza amadosiye amwamwe n’iyindi nshasha iriho, mu gihe uguma ufise imiterere yawe. Dore intambwe zitomoye zo gukurikira kugira ngo ubone ivyagezwe bisukuye kandi bitekanye:



Kugira umenye verisiyo ya Dojo yawe, koresha itegeko :



```bash
./dojo.sh version
```



Naho iyo ntambwe ari ubusabe, ndagusavye utangure mu guhindura OS yawe. Ivyo bigabanya ingorane zo kudahuza kandi bikaba bituma ibikoresho bikoreshwa na Dojo biguma ku gihe:



```bash
sudo apt-get update
sudo apt-get upgrade
```



Genda mu bubiko bwa Dojo maze uhagarike ibikorwa biriho ubu:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Hanyuma wongere ufungure sisitemu yawe kugira uronke igitabu gisukuye:



```bash
sudo reboot
```



Dojo izana n’amadosiye yashizweko umukono mu buryo bwa digitale. Izo sinyatire za PGP zituma amadosiye akomoka ku muhinguzi kandi ko atahinduwe mu buryo na bumwe. Ni vyiza ko ubisuzuma igihe cose uhinduye Dojo, nk’uko wabigize igihe wabanza kuyishiramwo. Tangana n'ugukuraho urufunguzo rwa bose rw'umuhinguzi biciye kuri Tor, hanyuma urushiremwo :



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



Subira mu bubiko bwawe bwite:



```bash
cd ~/
```



Gukuraho verisiyo nshasha ya Dojo kuri GitHub biciye kuri Tor. Muri aka karorero, ni verisiyo `1.28.0` (itarabaho mu gihe c'ukwandika: iki ni ugutanga akarorero gusa). Ibuka gusubirira dosiye n'ihuriro [na verisiyo wipfuza gushiramwo](https://github.com/Umugambi-Wuguruye-Isoko-ya-Dojo/samourai-dojo/ibisohoka):



```bash
torsocks wget -O samourai-dojo-1.28.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.28.0.zip
```



Kandi n'ushireko dosiye irimwo ibimenyetso vy'intoke vya PGP n'umukono (na none, wibuke guhindura verisiyo iri mw'itegeko):



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt.sig
```



Suzuma ko dosiye y'ibimenyetso vy'urutoke yashizweko umukono n'urufunguzo rw'umuhinguzi:



```bash
gpg --verify samourai-dojo-1.28.0-fingerprints.txt.sig
```



Igisubizo kibereye gikwiye kwerekana :



```
gpg: Signature made [date + time]
gpg: using EDDSA key E53AD419B242822F19E23C6D3033D463D6E544F6
gpg: Good signature from "dojocoder@pm.me" <dojocoder@pm.me> [unknown]
```



Imburi y’uko urufunguruzo rutaremejwe yoshobora kuboneka, ariko ivyo nta co bimaze. Ku rundi ruhande, nimba umukono udafise akamaro canke uhuye n’urundi rufunguzo, ntugende kure maze wongere utangure, usuzume amahuza.



Hanyuma ubaze urutoke rwa SHA256 rw'ububiko maze urugereranye na dosiye y'urutoke yemewe :



```bash
sha256sum samourai-dojo-1.28.0.zip
cat samourai-dojo-1.28.0-fingerprints.txt
```



Iyo ivyo bimenyetso bibiri vy'intoke bihuye neza, ububiko ni ubw'ukuri kandi butagiramwo ikibazo. Niba zitandukanye, uce uzifuta ubwo nyene kandi ntubandanye.



Gukuraho ububiko mu bubiko bwawe bwo muhira:



```bash
unzip samourai-dojo-1.28.0.zip -d .
```



Hanyuma ukope ibirimwo mu bubiko bwa Dojo, wandikeko ivya kera :



```bash
cp -a samourai-dojo-1.28.0/. dojo-app/
```



Iyi nzira igumya amadosiye yawe y'imiterere ari muri `~/dojo-app/docker/my-dojo/conf`, ariko isubirira ayandi madosiye yose n'amaverisiyo yavuguruwe.



Kugira ngo ibidukikije vyawe bigume bisukuye, siba amadosiye adakenewe :



```bash
rm -r samourai-dojo-1.28.0 && rm samourai-dojo-1.28.0.zip && rm samourai-dojo-1.28.0-fingerprints.txt && rm samourai-dojo-1.28.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



Subira mu bubiko bw'inyandiko za Dojo maze ukoreshe itegeko ryo guhindura:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh upgrade -y
```



Iri tegeko ritegeka Docker gusubira kwubaka amashusho n’amadosiye mashasha, hanyuma igasubira gutangura ibikorwa vyose. Igihe igikorwa kirangiye, suzuma ibitabo kugira ngo umenye neza ko Bitcoin core, Fulcrum na Dojo vyose bikora neza:



```bash
./dojo.sh logs bitcoind
./dojo.sh logs fulcrum
```



Iyo ibikorwa bitanguye ata makosa kandi ibitabo vyerekana amabuye ariko aratunganirizwa, Dojo yawe ubu iri ku gihe kandi irakora.