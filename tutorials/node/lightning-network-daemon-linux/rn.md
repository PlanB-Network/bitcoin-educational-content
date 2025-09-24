---
name: Lightning Network Daemon (Linux)
description: Gushiramwo no gukoresha Lightning Network Daemon kuri Linux
---

![cover-lightning-network-daemon](assets/cover.webp)



Lightning Network ni Layer ya kabiri ya Bitcoin, bikaba biyishoboza gufata ingano z’umuravyo, cane cane kubera umuvuduko n’igiciro gito c’ibikorwa itanga.



Muri iyi nyigisho, tuzoshiraho ugushirwa mu ngiro kwa Lightning Network Daemon ku mashine yacu ya Linux (Ubuntu 24.04).



## Lightning Network Daemon ni iki?



Lightning Network Daemon ni ugushirwa mu ngiro kwuzuye kwa Lightning Network. Yaremwe na Lightning Labs kandi ishobora kugufasha gukoresha urugero rwuzuye rw'umurongo w'umuravyo ku mashine yawe.


Mu yandi majambo, n'iyi nzira, urashobora :





- Gukorana na Lightning Network**: Ushobora gukoresha imirongo y’amabwirizwa kugira ngo ureme ama wallets ya Lightning, ucunge inzira zo kwishura n’inzira, n’ibindi vyinshi, ukoresheje imashini yawe.
- Guhuza urudodo rwa Bitcoin ruri kure canke urugero rwawe rwa Bitcoin core**: LND igufasha guhuza urugero rwa Bitcoin maze ukarukoresha nk'inyuma yawe. Kugira ngo ukoreshe iyi nzira, ntukeneye gukoresha instance ya Bitcoin core ku mashini yawe.




https://planb.network/fr/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

## Ni kuki ufise urudodo rwawe rw’Umuravyo?


Lightning ni igikoresho co gupfuka Bitcoin gituma uburyo bwo gutanga amakuru bugenda neza kandi kigabanura amafaranga y’ugucuruza.



Mu guhindukiza urudodo rwawe rw’Umuco, uronka ubusegaba n’ukwigenga. Ni wewe ugenzura amahera yawe, rero uzirikane:



"Si imfunguruzo zawe, si amafaranga yawe."



Muri ubwo buryo, gukoresha urudodo rwa Lightning birongereza umutekano n’ubutungane bw’amakuru yawe mu buryo bukurikira:





- Total control**: Ucunge inzira zawe zo kwishura, ube banki yawe kandi ube umukuru w’itunga ryawe.
- Ibanga**: Gukora ataco wizigiye abandi bantu kugira ngo bakingire ubuzima bwite bwawe.
- Kwiga no kwigenga**: Ushimira amabwirizwa ya `lncli`, urashobora gutahura neza imigenderanire ya Lightning mu kwikoresha uri ku nzira yawe.
- Kwegereza ubutegetsi**: Gugira uruhara runini mu gukomeza no kwegereza ubutegetsi Bitcoin / Lightning Network.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


Ufise uburyo bubiri bwo gukoresha instance y'ugushirwa mu ngiro kwa LND ku mashini yacu. Turashobora gushinga ibidukikije ku mashini yacu bwite kugira ngo bikore mu karere, canke dushiremwo LND tuvuye mu gikoresho ca Docker. Aha, tuzokwibanda ku mahitamwo ya mbere, maze turabe ingene twobandanya na Docker mu nyigisho izoza.


## Shiraho LND kuva kuri kode y'inkomoko



### Ibisabwa


Nk’uko LND yanditswe muri Go, ukeneye kumenya neza ko ufise ibidukikije vya GoLang n’ibintu bikenewe bishingiye ku mashini yawe ya Linux.





- Ibisabwa mu bikoresho:**


Kugira ngo ukore neza kandi utagira umurongo, imashini yawe izokenera kugira ubushobozi bukwiye bwo gukoresha urudodo rwawe rwa LND Lightning.



Uzokenera :


1. **8 GB RAM** kugira ngo ukore neza,


2. **Igikoresho gikoresha ivyuma vyinshi (quad-core canke birenze)** kugira ngo ushobore gucunga neza ibikorwa vy'umurongo wawe,


3. **Nibura 5GB y'umwanya kuri disk** ku buryo bwa node ya pruned na 1TB kugira ngo ukoreshe Bitcoin core (ntibishoboka iyo ukoresheje node iri kure)





- Shiraho ibiva ku ngirakamaro:


Itegeko riri musi rizogufasha gushiramwo ku mashine yawe ibikoresho ukeneye kugira ngo ukoreshe LND. Mu bindi, uzokenera gushiramwo `Git`, igikoresho co guhindura, na `make`, bishobora gukora no kwubaka ugushirwa mu ngiro kwa LND bivuye kuri kode y'inkomoko.



```bash
sudo apt install -y build-essential git make
```



![installation-dependances](assets/fr/01.webp)





- Shiraho GoLang ku mashine yawe ya Linux**



Kuva kw'igenekerezo ry'iyi nyigisho, LND isaba verisiyo 1.23.6 ya **Go** kugira ngo ishiremwo.



Niba wari ufise verisiyo ya kera yari yarashizwemwo, ikureho kugira ngo ushiremwo Go nshasha.


```bash
# Suppression d'une ancienne version de Go
sudo rm -rf /usr/local/go

# Installation de la version 1.23.6 de Go
wget https://golang.org/dl/go1.23.6.linux-amd64.tar.gz

# Decompression du package

sudo tar -C /usr/local -xzf go1.23.6.linux-amd64.tar.gz

```



![go-install](assets/fr/02.webp)





- Genda** imiterere y'ibidukikije


Mu dosiye yawe `~/.bashrc`, tangura ibi bihinduka vy'ibidukikije bikurikira kugira ngo wongere Genda kuri sisitemu yawe ya Linux.



```bash
# Configuration de l'environnement Go
export GOROOT=/usr/local/go
export GOPATH=~/gocode
export PATH=$PATH:$GOROOT/bin

# Appliquer les modifications

source ~/.bashrc
```





- Gusuzuma **ugushiraho** (mu gifaransa)


```bash
go version
```



![go-version](assets/fr/03.webp)


### Gukora ububiko bwa LND GitHub



Koresha git kugira uronke kopi ya kode y'inkomoko ya LND mu karere ku mashine yawe


```bash
git clone https://github.com/lightningnetwork/lnd.git
```


![clone-lnd](assets/fr/04.webp)


### Kubaka no gushiramwo



Igikoresho ca `make`, cari carashizweho mbere, kizogufasha kwubaka igikoresho gishobora gukorwa uhereye kuri kode y'inkomoko ya LND maze ukomeze gushiramwo.



```bash
# Acceder au repertoire clonné
cd lnd

# construire LND
make
```



Shiraho LND ku mashine yawe



```bash
# installer LND
make install
```



![make-lnd](assets/fr/06.webp)




- Gusuzuma uko washizeho** (mu gifaransa)



Kugira ngo umenye neza ko vyose vyagenze neza, gukoresha iri tegeko bikwiye kuguha verisiyo ya LND uriko urakoresha ubu.



```bash
# Version de LND
lnd --version

# Version  de LNCLI
lncli --version
```


![lnd-version](assets/fr/05.webp)




- Gucungera no kuvugurura



```bash
cd lnd
git pull
make clean && make && make install
```


⚠️ **IGIHARURWA**: Ivyagezwe vya LND bishobora gusaba amaverisiyo mashasha ya Go, rero urabe ko uhindura sisitemu yawe kugira ngo wirinde ingorane z’ugushingira intahe mu gihe co gushiramwo.


### Gutunganya Lightning Network Daemon



Itunganywa ry’uruzitiro rwa Lightning LND risa n’irya Bitcoin, kandi rikorwa muri dosiye y’itunganywa irimwo ibipimo vyose vy’uruzitiro rwawe. Kugira ngo ubikore, ku muzi w'imashini yawe ushobora gukora dosiye yihishije `.LND` hanyuma ugakora dosiye yawe y'imiterere `LND.conf` muri iyo dosiye.



```bash
# Création du ficher
mkdir -p ~/.lnd

cd ~/.lnd

# Fichier de configuration
touch lnd.conf
```





Mu dosiye y'imiterere, ushobora gushinga urudodo rwawe rwa LND.



```
noseedbackup=0
debuglevel=debug

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=bitcoind

[Bitcoind]
bitcoind.rpcuser=<UTILISATEUR_BITCOIN>
bitcoind.rpcpassword=<MOT_DE_PASSE_BITCOIN>
bitcoind.zmqpubrawblock=tcp://127.0.0.1:28332
bitcoind.zmqpubrawtx=tcp://127.0.0.1:28333

```



## Gutahura imiterere yawe



Ni ngombwa ko utahura uburyo bukeyi ukeneye kugira ngo ushobore gushiramwo neza kandi mu buryo bushitse urudodo rwawe rwa LND.



Hashingiwe ku birimwo muri dosiye `~/.LND/LND.conf`, ng'ibi ibisobanuro vy'ibibanza:





- noseedbackup**: Iguha uburenganzira bwo guhitamwo nimba ushaka ko LND ikora ububiko bw'amasakoshi yawe. Gushinga iki kintu kuri `0` bigufasha kubika amakuru yo gusubiza mu kibanza gitekanye wahisemwo.





- debuglevel**: Iguha uburenganzira bwo gusobanura urugero rw'ido n'ido ry'amakosa n'ibitabo mu gihe amakosa abaye mu gihe c'igikorwa.





- Bitcoin.active**: Itegeka LND gukora nk’uruzitiro rwa Bitcoin no gukorana n’urubuga rwa Bitcoin.





- Bitcoin.Mainnet**: Igaragaza LND kugira ngo ihuze n'urubuga rwa Bitcoin (Mainnet), ushobora gushinga agaciro `bitcoind.signet` na `bitcoind.regtest` hakurikijwe urubuga rwa Bitcoin rwa Bitcoin n'urubuga rwa Bitcoin





- Bitcoin.node**: Igaragaza ubwoko bw'uruzitiro rwa Bitcoin LND ikwiye kwifatanya nazo.





- Bitcoin.rpc** na **Bitcoin.ijambobanga** : Biserukira.


nk'uko bigenda (ukoresha, ijambobanga) kugira ngo wihuze n'uruzitiro rwawe rwa Bitcoin





- bitcoind.zmqpubrawblock** na **bitcoind.zmqpubrawtx**: uko bikurikirana bisobanura iherezo rya ZeroMQ kugira ngo uronke amatangazo yerekeye amabuye mashasha n'ibikorwa ku rubuga rwa Bitcoin.




## Gusuzuma uko washizeho na LND



Kumbure uzoshaka kumenya neza ko iyo nzira yagenze neza, kandi ko uriko urakorana na Lightning Network kugira ngo amakuru yawe y’urudodo agume ari ku gihe.



Kugira ngo utangure gushirwa mu ngiro kwa LND no kuronka amakuru yerekeye urudodo rwawe, wandike gusa itegeko :


```bash
lnd getinfo
```


![lnd-getinfo](assets/fr/07.webp)


## Gukora ibikorwa kuri LND



Iyo installation yawe imaze kurangira kandi ikagenzurwa, urashobora gutangura kuyikoresha.


Akira amabwirizwa y’ingenzi kugira ngo utangure.



### Rema Wallet


Lightning Wallet yawe ni intambwe ya mbere mu gikorwa cose co gucunga amahera yawe.



⚠️ **IGIHARURWA**: Uzirikane neza amajambo yawe 24 **Ijambo seed**. Uzoyikenera kugira ngo ubone amahera yawe iyo habaye ingorane.



Kandi ubike ijambobanga ryawe rya Wallet kugira ngo ushobore kurifungura ukoresheje itegeko rya `lncli unlock` igihe usubiye gutangura node yawe ya LND.



```bash
lncli create
```


![créer-portefeuille](assets/fr/08.webp)


### Suzuma uburinganire bwawe



Raba amakonti yawe ukoresheje terminal yawe:



```bash
lncli walletbalance
```


![solde](assets/fr/09.webp)


### Amakuru yerekeye urudodo rwawe



Koresha itegeko riri musi kugira umenye imirongo ikora kuri node yawe.



```bash
lncli listchannels
```



Ushobora kandi kuronka urutonde rw’ibihimba uhuye navyo.



```bash
lncli listpeers
```



### Ubuyobozi bw'imirongo



Umurongo w'umuravyo uraguha uburenganzira bwo kugira **ubufatanye butaziguye, bubiri ku bubiri n'iyindi nzira iri kuri Lightning Network**. Muri iyi nzira, urashobora kwidegemvya Exchange Satoshis gushika ku bushobozi bw’iyo nzira.



### Huza n'urudodo



Gufatanya n’izindi nzira z’Umuravyo ni igikorwa c’ishimikiro nimba ushaka kugira uruhara n’umwete no kwungukira ku bubasha bwa Lightning.



Kugira ngo wihuze n'umugenzi (Lightning node), uzokenera amakuru atatu:




- Urufunguzo rwa bose rw'urudodo**: Uru ni ikimenyetso kidasanzwe c'urudodo mu rubuga rwa Bitcoin;
- IP**: IP y’imashini iyo node ishizweko;
- PORT**: Icuma kifunguka ku mashini kiremesha guhanahana amakuru n’iyi node.



Ushobora kuronka amanode yo gufatanya kuri [amboss](https://amboss.space/), urubuga rutanga urutonde rw'amakuru ku manode y'umuravyo.



```bash
# Se connecter à un noeud
lncli connect <ID_PUBKEY>@<IP>:<PORT>

# Un exemple  : Connexion au noeud de Wallet of Satoshi
lncli connect 035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226@170.75.163.209:9735
```




Raba neza ko wifatanya na **nodes zizewe** kugira ngo uzigame ubutungane bwa sisitemu yawe bwite. Aha hariho impanuro zimwe zimwe zo guhitamwo amahuzu akwiriye.





- Uguhinduranya ibibanza**: Guhuza n’ibihimba vyo mu turere dutandukanye.





- Izina**: Hitamwo amanode afise uburyo bwiza bwo kuronka.





- Ubushobozi**: Hitamwo amapfundo afise amahera meza.





- Ibiciro**: Suzuma ibiciro vy’inzira.


### Gufungura umurongo wo kwishura


Kugira ngo ufungure umurongo wo kwishura, urabe neza ko **uhuye** n'uruzitiro rw'urunganwe, hanyuma usobanure **ubushobozi** (umubare w'amasatoshi) wipfuza guhagarika muri uwo muhora.



```bash
lncli openchannel --node_key=<ID_PUBKEY> --local_amt=<AMOUNT_SATOSHIS>
```


### Rema umuravyo Invoice



Umuravyo Invoice ugereranya urutonde rw'ibimenyetso vyerekana icipfuzo cawe co kwakira satoshis mu Muravyo Wallet yawe.


Gukora amafagitire ya Lightning ukoresheje node yawe bwite bigufasha kurinda amakuru yawe (ay’aho uba n’ay’umuntu ku giti ciwe) kandi bikaguha ubwigenge 100% ku bijanye n’ugucungera amahera yawe.



```bash
# Générer une facture de 1000 sats

lncli addinvoice --amt=1000 --memo="Facture de 1000 sats"
```



### Kwishura umuravyo Invoice



```bash
lncli payinvoice <FACTURE>
```


### Gufunga umurongo



Hari uburyo bubiri bwo gufunga umurongo ukora kuri node yawe y'ubu.





- Gufunga kw’ubufatanye**: Ivyo bigaragaza icipfuzo c’urudodo rwawe co kuva mu muhora wo kwishura, bikaba ari vyo bituma ibikorwa bigenda biraheza kandi ko amakuru ashigikirwa kugira ngo ntihagire amahera atakaza.


```
lncli closechannel <ID_CANAL>
```




- Gufunga ku nguvu**: ⚠️ Kugira ngo uvyirinde nimba bishoboka, ico gikorwa kirahagarika ibikorwa biriko biraba mu muhora wawe wo kwishura kandi kikongera ingorane zo gutakaza amahera.


```
lncli closechannel --force <ID_CANAL>
```


## Ivyiza n’umutekano ku bijanye n’urudodo rwawe rwa LND.


Umutekano ni wo uhambaye cane iyo ukoresheje urudodo rwa Bitcoin/ Lightning. Aha hariho ingingo nkeyi zo gukomeza umutekano w’ivyo ushizeho:





- Gumana ijambo ryawe `seed` ahantu hatagira umurongo.





- Gukora ububiko bwa dosiye `~/.LND/channel.backup`: Iyi dosiye ibika amakuru y'umurongo wawe igihe cose umurongo mushasha ufunguwe (canke umurongo wa kera ufunze) ku nzira yawe.


⚠️ Igufasha kugarura imihora no gusubiza amahera yabujijwe mu mihora yo kwishura mu gihe amakuru yatakaye canke node idakora neza



Ushobora kugarura amafaranga yawe ukoresheje itegeko riri musi mu kugaragaza inzira y'ububiko bw'iyi dosiye:


```
lncli restorechanbackup <CHEMIN_DU_FICHIER>
```




- Raba neza ko wabitse amajambo yo gusubizaho n'ijambobanga rya Lightning Wallet yawe.
- Gumana ubuhinga bwawe bujanye n’igihe.



## Ubu gutorera umuti ingorane


### Ingorane zikunda gushika




- Ikosa ryo guhuza bitcoind**: Suzuma amakuru yawe yo kwinjira muri RPC
- Guhuza vyabujijwe**: Suzuma uruja n'uruza rwawe rwa interineti
- Ikosa ry'uruhusha**: Suzuma uburenganzira bwa dosiye `~/.LND`




Rero mwashitse ku mpera y’iyi nyigisho. Niba wifuza kumenya vyinshi ku vyerekeye Lightning, turaguha iyi nyigisho y'intango kugira ngo utahure neza ivyiyumviro n'imigenzo iri inyuma ya Lightning Network.




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb