---
name: Lightning Network Daemon (Linux)
description: Inasakinisha na kuendesha Lightning Network Daemon kwenye Linux
---

![cover-lightning-network-daemon](assets/cover.webp)



Lightning Network ni Layer ya pili ya Bitcoin, inayoiwezesha kuchukua vipimo vya umeme, shukrani haswa kwa kasi na gharama ya chini ya miamala inayotoa.



Katika somo hili, tutasakinisha utekelezaji wa Lightning Network Daemon kwenye mashine yetu ya Linux (Usambazaji wa Ubuntu 24.04).



## Lightning Network Daemon ni nini?



Lightning Network Daemon ni utekelezaji kamili wa Go wa Lightning Network. Iliundwa na Maabara ya Umeme na hukuruhusu kuendesha mfano kamili wa nodi ya Umeme kwenye mashine yako.


Kwa maneno mengine, na utekelezaji huu, unaweza:





- Wasiliana na Lightning Network**: Unaweza kutumia mistari ya amri kuunda jalada la Radi, kudhibiti njia na njia za malipo, na mengine mengi, moja kwa moja kutoka kwa terminal ya mashine yako.
- Kuunganisha nodi ya mbali ya Bitcoin au mfano wako mwenyewe wa Bitcoin Core**: LND hukuruhusu kuunganisha mfano wa Bitcoin na uitumie kama mandhari yako ya nyuma. Ili kutumia utekelezaji huu, huhitaji kuendesha mfano wa Bitcoin Core kwenye mashine yako.




https://planb.network/fr/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

## Kwa nini uwe na nodi yako ya Umeme?


Umeme ni wekeleo la Bitcoin ambalo huboresha mchakato wa uhamishaji na kupunguza gharama za muamala.



Kwa kuzungusha nodi yako ya Umeme, unapata mamlaka na uhuru. Unadhibiti pesa zako, kwa hivyo kumbuka:



"Sio funguo zako, si bitcoins zako."



Kwa maana hii, kuendesha nodi ya Umeme huongeza usalama na uadilifu wa data yako kwa njia zifuatazo:





- Udhibiti kamili**: Dhibiti njia zako za malipo, uwe benki yako mwenyewe na uwe mmiliki wa mali yako.
- Usiri**: Fanya shughuli bila kutegemea washirika wengine kulinda faragha yako.
- Kujifunza na kujitegemea**: Shukrani kwa amri za `lncli`, unaweza kuelewa vyema michakato ya msingi ya Umeme kwa kujituma kutoka kwa terminal yako.
- Ugatuaji**: Shiriki kikamilifu katika kuimarisha na kugatua Bitcoin / Lightning Network.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


Una chaguzi mbili za kuendesha mfano wa utekelezaji wa LND kwenye mashine yetu. Tunaweza kusanidi mazingira kwenye mashine yetu wenyewe ili kuendeshwa ndani ya nchi, au kusakinisha LND kutoka kwa chombo cha Docker. Hapa, tutazingatia chaguo la kwanza, na kuona jinsi ya kuendelea na Docker katika mafunzo ya baadaye.


## Sakinisha LND kutoka kwa msimbo wa chanzo



### Masharti


Jinsi LND inavyoandikwa katika Go, unahitaji kuhakikisha kuwa una mazingira ya GoLang na vitegemezi vinavyohitajika kwenye mashine yako ya Linux.





- Mahitaji ya maunzi:**


Kwa matumizi laini, bila mshono, mashine yako itahitaji kuwa na uwezo unaohitajika ili kuendesha nodi yako ya Umeme ya LND.



Utahitaji:


1. **RAM ya GB 8** kwa ugiligili bora zaidi,


2. **Kichakataji chenye msingi nyingi (quad-core au zaidi)** ili kudhibiti vitendo vya nodi yako kwa ufanisi,


3. **Angalau nafasi ya diski ya GB 5** kwa modi ya nodi iliyokatwa na 1TB kuendesha Bitcoin Core (si lazima utumie nodi ya mbali)





- Sakinisha vitegemezi muhimu:**


Amri iliyo hapa chini itakuruhusu kusakinisha kwenye mashine yako zana unazohitaji kuendesha LND. Miongoni mwa mambo mengine, utahitaji kusakinisha `Git`, zana ya kutolea matoleo, na `make`, ambayo inaweza kutekeleza na kujenga utekelezaji wa LND kutoka kwa msimbo wa chanzo.



```bash
sudo apt install -y build-essential git make
```



![installation-dependances](assets/fr/01.webp)





- Sakinisha GoLang kwenye mashine yako ya Linux**



Kuanzia tarehe ya mafunzo haya, LND inahitaji toleo la 1.23.6 la Go*** kwa ajili ya kusakinisha.



Ikiwa tayari ulikuwa na toleo la awali lililosakinishwa, liondoe kwa usakinishaji mpya wa Go.


```bash
# Suppression d'une ancienne version de Go
sudo rm -rf /usr/local/go

# Installation de la version 1.23.6 de Go
wget https://golang.org/dl/go1.23.6.linux-amd64.tar.gz

# Decompression du package

sudo tar -C /usr/local -xzf go1.23.6.linux-amd64.tar.gz

```



![go-install](assets/fr/02.webp)





- Nenda ** usanidi wa mazingira


Katika faili yako ya `~/.bashrc`, anzisha vigeu vifuatavyo vya mazingira ili kuongeza Nenda kwenye mfumo wako wa Linux.



```bash
# Configuration de l'environnement Go
export GOROOT=/usr/local/go
export GOPATH=~/gocode
export PATH=$PATH:$GOROOT/bin

# Appliquer les modifications

source ~/.bashrc
```





- Kuangalia usakinishaji** (kwa Kifaransa)


```bash
go version
```



![go-version](assets/fr/03.webp)


### Funga hazina ya LND GitHub



Tumia git kupata nakala ya msimbo wa chanzo wa LND kwenye mashine yako


```bash
git clone https://github.com/lightningnetwork/lnd.git
```


![clone-lnd](assets/fr/04.webp)


### Jenga na usakinishe



Zana ya `kutengeneza`, iliyosakinishwa hapo awali, itakuwezesha kuunda kinachoweza kutekelezeka kutoka kwa msimbo wa chanzo wa LND na kuendelea na usakinishaji wako.



```bash
# Acceder au repertoire clonné
cd lnd

# construire LND
make
```



Sakinisha LND kwenye mashine yako



```bash
# installer LND
make install
```



![make-lnd](assets/fr/06.webp)




- Inaangalia usakinishaji wako** (kwa Kifaransa)



Ili kuhakikisha kuwa kila kitu kilikwenda sawa, kuendesha amri hii kunapaswa kukupa toleo la LND ambalo unaendesha kwa sasa.



```bash
# Version de LND
lnd --version

# Version  de LNCLI
lncli --version
```


![lnd-version](assets/fr/05.webp)




- Matengenezo na uboreshaji



```bash
cd lnd
git pull
make clean && make && make install
```


⚠️ **MUHIMU**: Huenda masasisho ya LND yakahitaji matoleo ya hivi majuzi zaidi ya Go, kwa hivyo hakikisha kwamba umesasisha mfumo wako ili kuepuka matatizo ya utegemezi wakati wa kusakinisha.


### Inasanidi Lightning Network Daemon



Usanidi wa nodi ya Umeme ya LND ni sawa na ile ya Bitcoin, na inafanywa katika faili ya usanidi iliyo na vigezo vyote vya nodi yako. Ili kufanya hivyo, kwenye mzizi wa mashine yako unaweza kuunda folda iliyofichwa `.LND` kisha uunde faili yako ya usanidi `LND.conf` kwenye folda hii.



```bash
# Création du ficher
mkdir -p ~/.lnd

cd ~/.lnd

# Fichier de configuration
touch lnd.conf
```





Katika faili ya usanidi, unaweza kusanidi nodi yako ya LND.



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



## Kuelewa usanidi wako



Ni muhimu kwako kuelewa usanidi wa chini unaohitaji kwa usakinishaji sahihi na kamili wa nodi yako ya LND.



Kulingana na maudhui ya faili `~/.LND/LND.conf`, haya hapa ni maelezo ya sehemu:





- noseedbackup**: Hukuruhusu kuchagua kama unataka LND kutekeleza hifadhi rudufu za kiotomatiki za kwingineko zako.  Kuweka kipengee hiki kuwa `0` hukuruhusu kuhifadhi mwenyewe maelezo ya urejeshaji katika eneo salama lililochaguliwa kibinafsi.





- debuglevel**: Hukuruhusu kufafanua kiwango cha maelezo ya hitilafu na kumbukumbu katika tukio la hitilafu kutokea wakati wa kitendo.





- Bitcoin.active**: Inaagiza LND kufanya kazi kama nodi ya Bitcoin na kuingiliana na mtandao wa Bitcoin.





- Bitcoin.Mainnet**: Inabainisha LND ili kuunganisha kwenye mtandao mkuu wa Bitcoin (Mainnet), unaweza kuweka thamani `bitcoind.signet` na `bitcoind.regtest` mtawalia kwa Saini ya Bitcoin na Bitcoin Regtest mitandao.





- Bitcoin.nodi**: Inabainisha aina ya nodi ya Bitcoin ambayo LND inapaswa kuunganishwa nayo.





- Bitcoin.rpcuser** na **Bitcoin.rpcpassword** : Wakilisha.


kwa mtiririko huo logins (mtumiaji, nenosiri) kuunganishwa na nodi yako ya Bitcoin





- bitcoind.zmqpubrawblock** na **bitcoind.zmqpubrawtx**: kwa mtiririko huo hufafanua ncha za ZeroMQ ili kupokea arifa kuhusu vizuizi vipya na miamala kwenye mtandao wa Bitcoin.




## Inakagua usakinishaji wako na LND



Labda utataka kuhakikisha kuwa mchakato umefaulu, na kwamba unasawazisha na Lightning Network ili kusasisha maelezo ya nodi yako.



Kuanza utekelezaji wa LND na kupata habari kuhusu nodi yako, chapa tu amri:


```bash
lnd getinfo
```


![lnd-getinfo](assets/fr/07.webp)


## Kufanya vitendo kwenye LND



Mara usakinishaji wako umekamilishwa na kukaguliwa, unaweza kuanza kuitumia.


Hapa kuna amri muhimu ili uanze.



### Unda kwingineko


Jalada lako la Umeme ni hatua ya kwanza katika hatua yoyote ya kudhibiti pesa zako.



⚠️ **MUHIMU**: Zingatia kwa makini kishazi chako cha maneno 24 **seed**. Utaihitaji ili kurejesha pesa zako kukitokea matatizo.



Pia hifadhi nenosiri lako la Wallet ili uweze kulifungua kwa amri ya `lncli unlock` unapoanzisha upya nodi yako ya LND.



```bash
lncli create
```


![créer-portefeuille](assets/fr/08.webp)


### Angalia salio lako



Angalia akaunti zako moja kwa moja kutoka kwa terminal yako:



```bash
lncli walletbalance
```


![solde](assets/fr/09.webp)


### Taarifa kuhusu nodi yako



Tumia amri iliyo hapa chini ili kujua ni njia zipi zinazotumika kwenye nodi yako.



```bash
lncli listchannels
```



Unaweza pia kupata orodha ya nodi ambazo umeunganishwa.



```bash
lncli listpeers
```



### Usimamizi wa kituo



Chaneli ya Umeme hukuruhusu kuwa na ** muunganisho wa moja kwa moja, wa jozi-kwa-jozi na nodi nyingine kwenye Lightning Network**. Katika chaneli hii, unaweza kwa uhuru Exchange Satoshis hadi uwezo wa kituo.



### Unganisha kwenye nodi



Kuunganisha kwa nodi zingine za Umeme ni hatua ya kimsingi ikiwa unataka kushiriki kikamilifu na kufaidika na nguvu za Umeme.



Ili kuunganisha kwa rika (Nodi ya umeme), utahitaji taarifa tatu:




- Kitufe cha umma cha nodi**: Hiki ni kitambulisho cha kipekee cha nodi katika mtandao wa Bitcoin;
- IP** : IP ya mashine ambayo node imewekwa;
- PORT** : Bandari hufunguliwa kwenye mashine inayoruhusu mawasiliano na nodi hii.



Unaweza kupata nodi za kuunganisha kwenye [amboss](https://amboss.space/), mfumo unaoorodhesha maelezo kwenye nodi za Umeme.



```bash
# Se connecter à un noeud
lncli connect <ID_PUBKEY>@<IP>:<PORT>

# Un exemple  : Connexion au noeud de Wallet of Satoshi
lncli connect 035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226@170.75.163.209:9735
```




Hakikisha kuwa umeunganisha kwa **nodi zinazotegemeka** ili kuhifadhi uadilifu wa mfumo wako mwenyewe. Hapa kuna baadhi ya mapendekezo ya kuchagua miunganisho sahihi.





- Mseto wa kijiografia**: Unganisha kwa nodi katika maeneo tofauti.





- Sifa**: Chagua nodi zilizo na upatikanaji mzuri.





- Uwezo**: Chagua mafundo yenye ukwasi mzuri.





- Gharama**: Angalia gharama za uelekezaji.


### Fungua kituo cha malipo


Ili kufungua kituo cha malipo, hakikisha **umeunganishwa** kwenye nodi ya programu zingine, kisha ubainishe **uwezo** (kiasi cha satoshi) ungependa kuzuia katika kituo hiki.



```bash
lncli openchannel --node_key=<ID_PUBKEY> --local_amt=<AMOUNT_SATOSHIS>
```


### Unda umeme wa Invoice



Umeme Invoice inawakilisha mfuatano wa herufi zinazoonyesha nia yako ya kupokea satoshi katika Umeme Wallet yako.


Kuunda ankara za umeme kwa kutumia nodi yako hukuruhusu kulinda data yako (ya kijiografia na ya kibinafsi) na hukupa uhuru wa 100% juu ya usimamizi wa pesa zako.



```bash
# Générer une facture de 1000 sats

lncli addinvoice --amt=1000 --memo="Facture de 1000 sats"
```



### Kulipa Umeme Invoice



```bash
lncli payinvoice <FACTURE>
```


### Funga kituo



Kuna njia mbili za kufunga chaneli inayotumika kwenye nodi yako ya sasa.





- Kufungwa kwa vyama vya ushirika**: Hii inaashiria nia ya nodi yako kujiondoa kwenye kituo cha malipo, na kuhakikisha kwamba kazi zinazoendelea zimekamilika na kwamba data inachelezwa ili kuepuka upotevu wa pesa.


```
lncli closechannel <ID_CANAL>
```




- Kufunga kwa lazima**: ⚠️ Ili kuepukwa ikiwezekana, kitendo hiki kitakatiza michakato inayoendelea katika kituo chako cha malipo na huongeza hatari ya kupoteza pesa.


```
lncli closechannel --force <ID_CANAL>
```


## Mbinu bora na usalama kwa nodi yako ya LND.


Usalama ni muhimu unapotumia nodi ya Bitcoin/ Radi. Hapa kuna vidokezo vichache vya kuimarisha usalama wa usakinishaji wako:





- Weka neno lako la `seed` katika eneo salama, nje ya mtandao.





- Weka nakala za mara kwa mara za faili ya `~/.LND/channel.backup`: Faili hii huhifadhi hali za kituo chako kila wakati kituo kipya kinapofunguliwa (au kituo cha zamani kinapofungwa) kwenye nodi yako.


⚠️ Hukuruhusu kurejesha vituo na kurejesha pesa zilizozuiwa katika njia za malipo iwapo data itapotea au kufeli kwa nodi.



Unaweza kurejesha pesa zako kwa amri iliyo hapa chini kwa kubainisha njia mbadala ya faili hii:


```
lncli restorechanbackup <CHEMIN_DU_FICHIER>
```




- Hakikisha kuwa umehifadhi maneno na nenosiri la urejeshaji la Lightning Wallet.
- Sasisha mfumo wako.



## Utatuzi wa sasa


### Matatizo ya mara kwa mara




- Hitilafu ya muunganisho wa bitcoind** : Angalia maelezo yako ya kuingia kwenye RPC
- Usawazishaji umezuiwa** : Angalia muunganisho wako wa Mtandao
- Hitilafu ya ruhusa**: Angalia haki za folda `~/.LND`




Kwa hivyo umefika mwisho wa somo hili. Iwapo ungependa kupata maelezo zaidi kuhusu Umeme, tunatoa kozi hii ya utangulizi ili kukupa ufahamu bora wa dhana na mbinu za Lightning Network.




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb