---
name: Lightning Network Daemon (Linux)
description: Lightning Network Daemon installimine ja käivitamine Linuxis
---

![cover-lightning-network-daemon](assets/cover.webp)



Lightning Network on Bitcoin teine Layer, mis võimaldab tal omandada välkmõõtmed, eelkõige tänu kiirusele ja madalatele tehingutele, mida ta pakub.



Selles õpetuses paigaldame Lightning Network Daemon rakenduse oma Linuxi masinale (Ubuntu 24.04 distributsioon).



## Mis on Lightning Network Daemon?



Lightning Network Daemon on Lightning Network täielik Go rakendamine. Selle lõi Lightning Labs ja see võimaldab teil käivitada oma masinas Lightning-sõlme täielikku instantsi.


Teisisõnu, selle rakendusega saate :





- Suhelda Lightning Network**: Saate kasutada käsureid Lightning portfellide loomiseks, maksekanalite ja marsruutide haldamiseks ja paljuks muuks otse oma masina terminalist.
- Kaugse Bitcoin sõlme või oma Bitcoin Core'i instantsi** ühendamine: LND võimaldab teil linkida Bitcoin instantsi ja kasutada seda oma backendina. Selle rakenduse kasutamiseks ei ole vaja oma masinas käivitada Bitcoin Core'i instantsi.




https://planb.network/fr/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

## Miks peaks olema oma Lightning-sõlm?


Lightning on Bitcoin pealekandmine, mis optimeerib ülekandeprotsessi ja vähendab tehingukulusid.



Kui pöörate oma välgumihkluse sõlme, saavutate suveräänsuse ja autonoomia. Sa oled oma rahaliste vahendite üle kontrolli all, seega pea meeles:



"Mitte teie võtmed, mitte teie bitcoinid."



Selles mõttes suurendab Lightning-sõlme kasutamine teie andmete turvalisust ja terviklikkust järgmistel viisidel:





- Täielik kontroll**: Haldage oma maksekanaleid, muutuge oma pangaks ja olge oma varade peremees.
- Konfidentsiaalsus**: Tehke tehinguid, ilma et usaldaksite oma privaatsust kolmandate isikute suhtes.
- Õppimine ja iseseisvus**: Tänu käskudele `lncli` saate paremini mõista Lightningi aluseks olevaid protsesse, rakendades neid ise oma terminalist.
- Detsentraliseerimine**: Võtta aktiivselt osa Bitcoin / Lightning Network tugevdamisest ja detsentraliseerimisest.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


Teil on kaks võimalust LND rakendamise instantsi käivitamiseks meie masinas. Me võime kas luua keskkonna oma masinas lokaalselt käivitamiseks või paigaldada LND Dockeri konteinerist. Siinkohal keskendume esimesele võimalusele ja vaatame, kuidas Dockeriga edasi minna, hilisemas õpetuses.


## LND paigaldamine lähtekoodist



### Eeltingimused


Kuna LND on kirjutatud Go keeles, peate veenduma, et teie Linuxi masinas on olemas GoLangi keskkond ja vajalikud sõltuvused.





- Riistvaranõuded:**


Sujuva ja tõrgeteta kasutuskogemuse tagamiseks peab teie masinal olema vajalik võimsus LND Lightning-sõlme käivitamiseks.



Sa pead :


1. **8 GB RAM** optimaalse sujuvuse tagamiseks,


2. **mitme tuumaga protsessor (neljatuumaline või rohkem)**, et tõhusalt hallata oma sõlme tegevusi,


3. ** Vähemalt 5 GB kettaruumi** kärbitud sõlme režiimi jaoks ja 1 TB Bitcoin Core'i käivitamiseks (vabatahtlik, kui kasutatakse kaugseade)





- Paigaldage kasulikud sõltuvused:**


Allpool toodud käsk võimaldab teil paigaldada oma masinasse LND käivitamiseks vajalikud tööriistad. Muuhulgas on vaja paigaldada `Git`, mis on versioonimisvahend, ja `make`, mis suudab LND implementatsiooni lähtekoodist käivitada ja ehitada.



```bash
sudo apt install -y build-essential git make
```



![installation-dependances](assets/fr/01.webp)





- Paigaldage GoLang oma Linuxi masinasse**



Selle õpetuse valmimise ajal vajab LND paigaldamiseks Go*** versiooni 1.23.6.



Kui teil oli eelmine versioon juba paigaldatud, eemaldage see uue Go installimiseks.


```bash
# Suppression d'une ancienne version de Go
sudo rm -rf /usr/local/go

# Installation de la version 1.23.6 de Go
wget https://golang.org/dl/go1.23.6.linux-amd64.tar.gz

# Decompression du package

sudo tar -C /usr/local -xzf go1.23.6.linux-amd64.tar.gz

```



![go-install](assets/fr/02.webp)





- Go** keskkonna konfiguratsioon


Initsialiseerige oma failis `~/.bashrc` järgmised keskkonnamuutujad, et lisada Go oma Linuxi süsteemi.



```bash
# Configuration de l'environnement Go
export GOROOT=/usr/local/go
export GOPATH=~/gocode
export PATH=$PATH:$GOROOT/bin

# Appliquer les modifications

source ~/.bashrc
```





- Paigalduse kontrollimine** (prantsuse keeles)


```bash
go version
```



![go-version](assets/fr/03.webp)


### LND GitHubi repositooriumi kloonimine



Kasutage git'i, et saada LND lähtekoodi koopia lokaalselt oma masinasse


```bash
git clone https://github.com/lightningnetwork/lnd.git
```


![clone-lnd](assets/fr/04.webp)


### Ehita ja paigalda



Eelnevalt paigaldatud tööriist `make` võimaldab teil LND lähtekoodist koostada käivitatava faili ja jätkata installimist.



```bash
# Acceder au repertoire clonné
cd lnd

# construire LND
make
```



Paigaldage LND oma masinasse



```bash
# installer LND
make install
```



![make-lnd](assets/fr/06.webp)




- Paigalduse kontrollimine** (prantsuse keeles)



Selleks, et veenduda, et kõik on sujuvalt läinud, peaks selle käsu käivitamine andma teile LND versiooni, mida te praegu kasutate.



```bash
# Version de LND
lnd --version

# Version  de LNCLI
lncli --version
```


![lnd-version](assets/fr/05.webp)




- Hooldus ja uuendused



```bash
cd lnd
git pull
make clean && make && make install
```


⚠️ **OLULINE**: LND uuendused võivad nõuda Go uuemaid versioone, seega uuendage kindlasti oma süsteemi, et vältida sõltuvusprobleeme installimise ajal.


### Lightning Network Daemon seadistamine



Lightning LND-sõlme konfigureerimine on sarnane Bitcoin-sõlme konfigureerimisega ning see toimub konfiguratsioonifailis, mis sisaldab kõiki teie sõlme parameetreid. Selleks saate luua oma masina juurest peidetud kausta `.LND` ja seejärel luua selles kaustas oma konfiguratsioonifaili `LND.conf`.



```bash
# Création du ficher
mkdir -p ~/.lnd

cd ~/.lnd

# Fichier de configuration
touch lnd.conf
```





Konfiguratsioonifailis saate seadistada oma LND sõlme.



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



## Oma konfiguratsiooni mõistmine



On oluline, et te mõistaksite, millist miinimumkonfiguratsiooni on vaja LND sõlme korrektseks ja täielikuks paigaldamiseks.



Faili `~/.LND/LND.conf` sisu põhjal on siinkohal esitatud väljade üksikasjad:





- ninaedbackup**: Võimaldab valida, kas soovite, et LND teeks portfellidest automaatseid varukoopiaid.  Selle omaduse seadmine `0` võimaldab teil käsitsi salvestada taastamisandmeid isiklikult valitud turvalisse kohta.





- debuglevel**: Võimaldab määrata vigade ja logide detailsuse taseme, kui toimingu käigus ilmnevad vead.





- Bitcoin.active**: Käsib LND-l tegutseda Bitcoin sõlmpunktina ja suhelda Bitcoin võrguga.





- Bitcoin.Mainnet**: Määratleb LND ühendamiseks Bitcoin põhivõrguga (Mainnet), Bitcoin Signet ja Bitcoin Regtest võrkudele saab määrata vastavalt väärtused `bitcoind.signet` ja `bitcoind.regtest`





- Bitcoin.node**: Määrab Bitcoin sõlme tüübi, millega LND peaks ühenduma.





- Bitcoin.rpcuser** ja **Bitcoin.rpcpassword** : Esindada.


vastavalt sisselogimine (kasutaja, parool), et luua ühendus oma Bitcoin sõlme jaoks





- bitcoind.zmqpubrawblock** ja **bitcoind.zmqpubrawtx**: defineerivad vastavalt ZeroMQ lõpp-punkte, et saada teateid uute plokkide ja tehingute kohta Bitcoin võrgus.




## Paigalduse kontrollimine LND abil



Tõenäoliselt soovite veenduda, et protsess on olnud edukas ja et te sünkroonite Lightning Network-ga, et hoida oma sõlme andmed ajakohasena.



LND rakendamise käivitamiseks ja oma sõlme kohta teabe saamiseks kirjutage lihtsalt käsk :


```bash
lnd getinfo
```


![lnd-getinfo](assets/fr/07.webp)


## Tegevuste teostamine LND-l



Kui paigaldus on lõpetatud ja kontrollitud, võite seda kasutama hakata.


Siin on olulised käsud, et alustada.



### Loo portfoolio


Teie välkportfell on esimene samm mis tahes meetmete võtmisel, et hallata oma rahalisi vahendeid.



⚠️ **OLULINE**: Pange hoolikalt tähele oma 24-sõnalist **seed fraasi**. Seda vajate probleemide korral oma vahendite tagasisaamiseks.



Salvestage ka oma Wallet parool, et saaksite selle avada käsuga `lncli unlock`, kui te LND sõlme uuesti käivitate.



```bash
lncli create
```


![créer-portefeuille](assets/fr/08.webp)


### Kontrollige oma saldot



Vaadake oma kontosid otse oma terminalist:



```bash
lncli walletbalance
```


![solde](assets/fr/09.webp)


### Teave teie sõlme kohta



Kasutage allolevat käsku, et teada saada, millised kanalid on teie võrgusõlmes aktiivsed.



```bash
lncli listchannels
```



Saate ka nimekirja sõlmedest, millega olete ühendatud.



```bash
lncli listpeers
```



### Kanalite haldamine



Lightning-kanal võimaldab teil luua **direktse, paarikaupa ühenduse teise Lightning Network-sõlme**. Selles kanalis saate vabalt kasutada Exchange Satoshis kuni kanali mahutavuseni.



### Ühenda sõlme



Teiste Lightning-sõlmedega ühendamine on oluline tegevus, kui soovite aktiivselt osaleda ja Lightningu võimsusest kasu saada.



Selleks, et luua ühendus partneriga (Lightning-sõlmega), on vaja kolme teavet:




- Sõlme avalik võti**: See on sõlme unikaalne identifikaator Bitcoin võrgus;
- IP** : Selle masina IP-aadress, millele sõlme on paigaldatud;
- PORT** :  Masina avatud port, mis võimaldab selle sõlme suhtlemist.



Saate leida sõlmed, millega ühendada [amboss](https://amboss.space/), platvormi, mis loetleb teavet Lightning-sõlmede kohta.



```bash
# Se connecter à un noeud
lncli connect <ID_PUBKEY>@<IP>:<PORT>

# Un exemple  : Connexion au noeud de Wallet of Satoshi
lncli connect 035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226@170.75.163.209:9735
```




Veenduge, et ühendute **lugevate sõlmedega**, et säilitada oma süsteemi terviklikkus. Siin on mõned soovitused õigete ühenduste valimiseks.





- Geograafiline mitmekesistamine**: Ühendage eri piirkondade sõlmedega.





- Maine**: Valige hea kättesaadavusega sõlmed.





- Maht**: Valige hea likviidsusega sõlmed.





- Tasud**: Kontrollige marsruutimistasusid.


### Avage maksekanal


Maksekanali avamiseks veenduge, et olete **ühendatud** vastassõlmega, seejärel määrake **mahutavus** (satelliitide kogus), mida soovite selles kanalis blokeerida.



```bash
lncli openchannel --node_key=<ID_PUBKEY> --local_amt=<AMOUNT_SATOSHIS>
```


### Loo välk Invoice



Lightning Invoice kujutab endast tähemärkide jada, mis väljendab teie soovi saada satoshis oma Lightning Wallet.


Lightning-arvete loomine oma sõlme abil võimaldab teil kaitsta oma andmeid (geograafilisi ja isiklikke) ning annab teile 100% autonoomia oma vahendite haldamise üle.



```bash
# Générer une facture de 1000 sats

lncli addinvoice --amt=1000 --memo="Facture de 1000 sats"
```



### Maksmine Lightning Invoice



```bash
lncli payinvoice <FACTURE>
```


### Sulge kanal



Praeguse sõlme aktiivse kanali sulgemiseks on kaks võimalust.





- Ühistegevuse lõpetamine**: See annab märku teie sõlme soovist maksekanalist välja astuda, tagades, et käimasolevad ülesanded on lõpetatud ja andmed on varundatud, et vältida vahendite kadumist.


```
lncli closechannel <ID_CANAL>
```




- Sulgemine**: see tegevus katkestab teie maksekanalis käimasolevad protsessid ja suurendab rahaliste vahendite kaotamise riski.


```
lncli closechannel --force <ID_CANAL>
```


## LND sõlme parimad tavad ja ohutus.


Bitcoin/ Lightning-sõlme kasutamisel on ohutus esmatähtis. Siin on mõned punktid, mis tugevdavad teie paigalduse ohutust:





- Hoidke oma "seed fraasi" turvalises, võrguvälises kohas.





- Tee regulaarselt varukoopiaid failist `~/.LND/channel.backup`: See fail salvestab teie kanalite olekuid iga kord, kui teie sõlmes avatakse uus kanal (või suletakse vana kanal).


⚠️ Võimaldab taastada kanaleid ja taastada maksekanalites blokeeritud vahendeid andmete kadumise või sõlme rikke korral



Saate oma vahendid taastada alljärgneva käsuga, määrates selle faili varukoopiatee:


```
lncli restorechanbackup <CHEMIN_DU_FICHIER>
```




- Veenduge, et olete salvestanud oma Lightning Wallet taastamissõnad ja parooli.
- Hoidke oma süsteem ajakohasena.



## Praegune tõrkeotsing


### Sagedased probleemid




- bitcoind ühendusviga** : Kontrollige oma RPC sisselogimise andmeid
- Sünkroniseerimine blokeeritud** : Kontrollige oma internetiühendust
- Lubade viga**: Kontrollige kausta `~/.LND` õigusi




Nii et olete jõudnud selle õpetuse lõpuni. Kui soovite Lightningist rohkem teada saada, siis pakume seda sissejuhatavat kursust, et anda teile parem arusaam Lightning Network kontseptsioonidest ja praktikatest.




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb