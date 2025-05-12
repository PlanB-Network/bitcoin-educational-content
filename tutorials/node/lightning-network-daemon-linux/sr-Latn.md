---
name: Lightning Network Daemon (Linux)
description: Instaliranje i pokretanje Lightning Network Daemon na Linuxu
---

![cover-lightning-network-daemon](assets/cover.webp)



Lightning Network je drugi Layer od Bitcoin, omogućavajući mu da preuzme dimenzije munje, zahvaljujući posebno brzini i niskoj ceni transakcija koje nudi.



U ovom vodiču, instaliraćemo Lightning Network Daemon implementaciju na naš Linux računar (Ubuntu 24.04 distribucija).



## Šta je Lightning Network Daemon?



Lightning Network Daemon je kompletna Go implementacija Lightning Network. Kreirala ga je Lightning Labs i omogućava vam da pokrenete punu instancu Lightning čvora na vašem računaru.


Drugim rečima, sa ovom implementacijom, možete :





- Interaktujte sa Lightning Network**: Možete koristiti komandne linije za kreiranje Lightning portfolija, upravljanje kanalima plaćanja i rutama, i još mnogo toga, direktno iz vašeg terminala na mašini.
- Povezivanje udaljenog Bitcoin čvora ili vaše sopstvene Bitcoin Core instance**: LND vam omogućava da povežete Bitcoin instancu i koristite je kao vaš backend. Da biste koristili ovu implementaciju, nije potrebno da pokrećete Bitcoin Core instancu na vašem računaru.




https://planb.network/fr/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

## Zašto imati svoj Lightning čvor?


Lightning je Bitcoin sloj koji optimizuje proces prenosa i smanjuje troškove transakcija.



Rotiranjem vašeg Lightning čvora, stičete suverenitet i autonomiju. Vi kontrolišete svoja sredstva, zato imajte na umu:



"Nisu tvoji ključevi, nisu tvoji bitkoini."



U tom smislu, pokretanje Lightning čvora povećava sigurnost i integritet vaših podataka na sledeće načine:





- Totalna kontrola**: Upravljajte sopstvenim kanalima plaćanja, postanite sopstvena banka i budite gospodar svojih sredstava.
- Poverljivost**: Obavljajte transakcije bez oslanjanja na treće strane za zaštitu vaše privatnosti.
- Učenje i autonomija**: Zahvaljujući `lncli` komandama, možete bolje razumeti osnovne procese Lightning-a primenjujući se iz vašeg terminala.
- Decentralizacija**: Igrajte aktivnu ulogu u jačanju i decentralizaciji Bitcoin / Lightning Network.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


Imate dve opcije za pokretanje instance LND implementacije na našoj mašini. Možemo ili postaviti okruženje na našoj mašini za lokalno pokretanje, ili instalirati LND iz Docker kontejnera. Ovde ćemo se koncentrisati na prvu opciju, a kako nastaviti sa Docker-om ćemo videti u kasnijem tutorijalu.


## Instaliraj LND iz izvornog koda



### Preduslovi


Kako je LND napisan u Go-u, potrebno je da imate GoLang okruženje i neophodne zavisnosti na vašoj Linux mašini.





- Hardverski zahtevi:**


Za glatko, besprekorno iskustvo, vaša mašina će morati imati neophodan kapacitet za pokretanje vašeg LND Lightning čvora.



Trebaće vam :


1. **8 GB RAM** za optimalnu fluidnost,


2. **Višejezgarni procesor (četvorojezgarni ili više)** za efikasno upravljanje radnjama vašeg čvora,


3. **Najmanje 5GB prostora na disku** za pruned node režim i 1TB za pokretanje Bitcoin Core (opciono ako se koristi udaljeni čvor)





- Instalirajte korisne zavisnosti:**


Komanda ispod će vam omogućiti da instalirate na vašem računaru alate potrebne za pokretanje LND. Između ostalog, potrebno je instalirati `Git`, alat za verzionisanje, i `make`, koji može izvršiti i izgraditi LND implementaciju iz izvornog koda.



```bash
sudo apt install -y build-essential git make
```



![installation-dependances](assets/fr/01.webp)





- Instalirajte GoLang na vaš Linux računar**



Od datuma ovog vodiča, LND zahteva verziju 1.23.6 Go*** za instalaciju.



Ako ste već imali instaliranu prethodnu verziju, uklonite je za novu instalaciju Go-a.


```bash
# Suppression d'une ancienne version de Go
sudo rm -rf /usr/local/go

# Installation de la version 1.23.6 de Go
wget https://golang.org/dl/go1.23.6.linux-amd64.tar.gz

# Decompression du package

sudo tar -C /usr/local -xzf go1.23.6.linux-amd64.tar.gz

```



![go-install](assets/fr/02.webp)





- Konfiguracija okruženja za Go**


U vašem `~/.bashrc` fajlu, inicijalizujte sledeće promenljive okruženja kako biste dodali Go na vaš Linux sistem.



```bash
# Configuration de l'environnement Go
export GOROOT=/usr/local/go
export GOPATH=~/gocode
export PATH=$PATH:$GOROOT/bin

# Appliquer les modifications

source ~/.bashrc
```





- Provera instalacije** (na francuskom)


```bash
go version
```



![go-version](assets/fr/03.webp)


### Kloniraj LND GitHub repozitorijum



Koristi git da dobiješ kopiju LND izvornog koda lokalno na svojoj mašini.


```bash
git clone https://github.com/lightningnetwork/lnd.git
```


![clone-lnd](assets/fr/04.webp)


### Izgradi i instaliraj



Alat `make`, prethodno instaliran, omogućiće vam da napravite izvršni fajl iz LND izvornog koda i nastavite sa instalacijom.



```bash
# Acceder au repertoire clonné
cd lnd

# construire LND
make
```



Instalirajte LND na vašu mašinu



```bash
# installer LND
make install
```



![make-lnd](assets/fr/06.webp)




- Provera vaše instalacije** (na francuskom)



Da biste bili sigurni da je sve prošlo glatko, pokretanje ove komande trebalo bi da vam da verziju LND koju trenutno koristite.



```bash
# Version de LND
lnd --version

# Version  de LNCLI
lncli --version
```


![lnd-version](assets/fr/05.webp)




- Održavanje i nadogradnje



```bash
cd lnd
git pull
make clean && make && make install
```


⚠️ **VAŽNO**: Ažuriranja LND mogu zahtevati novije verzije Go-a, zato obavezno ažurirajte svoj sistem kako biste izbegli probleme sa zavisnostima tokom instalacije.


### Konfigurisanje Lightning Network Daemon



Konfiguracija čvora Lightning LND je slična onoj kod Bitcoin, i vrši se u konfiguracionoj datoteci koja sadrži sve parametre vašeg čvora. Da biste to uradili, na root-u vaše mašine možete kreirati skriveni folder `.LND` i zatim kreirati vašu konfiguracionu datoteku `LND.conf` u ovom folderu.



```bash
# Création du ficher
mkdir -p ~/.lnd

cd ~/.lnd

# Fichier de configuration
touch lnd.conf
```





U konfiguracionoj datoteci, možete postaviti svoj LND čvor.



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



## Razumevanje vaše konfiguracije



Važno je da razumete minimalnu konfiguraciju koju trebate za ispravnu i potpunu instalaciju vašeg LND čvora.



Na osnovu sadržaja datoteke `~/.LND/LND.conf`, ovde su detalji polja:





- noseedbackup**: Omogućava vam da izaberete da li želite da LND automatski pravi rezervne kopije vaših portfolija. Postavljanje ove osobine na `0` omogućava vam da ručno sačuvate informacije za vraćanje na lično izabranoj sigurnoj lokaciji.





- debuglevel**: Omogućava vam da definišete nivo detalja grešaka i logova u slučaju da dođe do grešaka tokom izvođenja akcije.





- Bitcoin.active**: Instruira LND da radi kao čvor Bitcoin i da interaguje sa mrežom Bitcoin.





- Bitcoin.Mainnet**: Specificira LND da se poveže na glavnu mrežu Bitcoin (Mainnet), možete postaviti vrednosti `bitcoind.signet` i `bitcoind.regtest` za Bitcoin Signet i Bitcoin Regtest mreže respektivno.





- Bitcoin.node**: Specifikuje tip Bitcoin čvora na koji bi LND trebalo da se poveže.





- Bitcoin.rpcuser** i **Bitcoin.rpcpassword** : Predstavljaju.


odnosno prijave (korisnik, lozinka) za povezivanje na vaš Bitcoin čvor





- bitcoind.zmqpubrawblock** i **bitcoind.zmqpubrawtx**: respektivno definišu ZeroMQ krajnje tačke za primanje obaveštenja o novim blokovima i transakcijama na Bitcoin mreži.




## Provera vaše instalacije sa LND



Verovatno ćete želeti da se uverite da je proces bio uspešan i da se sinhronizujete sa Lightning Network kako biste održali informacije o čvoru ažurnim.



Da biste započeli implementaciju LND i dobili informacije o vašem čvoru, jednostavno upišite komandu :


```bash
lnd getinfo
```


![lnd-getinfo](assets/fr/07.webp)


## Izvođenje radnji na LND



Kada je vaša instalacija završena i proverena, možete početi da je koristite.


Evo osnovnih komandi da biste započeli.



### Kreiraj portfolio


Vaš Lightning portfolio je prvi korak u bilo kojoj akciji za upravljanje vašim sredstvima.



⚠️ **VAŽNO**: Pažljivo zabeležite vašu 24-rečnu **seed frazu**. Biće vam potrebna za povratak sredstava u slučaju problema.



Takođe sačuvaj svoju Wallet lozinku kako bi mogao da je otključaš sa `lncli unlock` komandom kada ponovo pokreneš svoj LND čvor.



```bash
lncli create
```


![créer-portefeuille](assets/fr/08.webp)


### Proveri svoj saldo



Konsultujte svoje račune direktno sa svog terminala:



```bash
lncli walletbalance
```


![solde](assets/fr/09.webp)


### Informacije o vašem čvoru



Koristite naredbu ispod da biste saznali koji kanali su aktivni na vašem čvoru.



```bash
lncli listchannels
```



Takođe možete dobiti listu čvorova na koje ste povezani.



```bash
lncli listpeers
```



### Upravljanje kanalima



Kanal za Lightning omogućava vam da imate **direktnu, par-po-par vezu sa drugim čvorom na Lightning Network**. U ovom kanalu možete slobodno Exchange Satošija do kapaciteta kanala.



### Poveži se na čvor



Povezivanje sa drugim Lightning čvorovima je osnovna akcija ako želite aktivno učestvovati i imati koristi od snage Lightning-a.



Da biste se povezali sa peer-om (Lightning čvorom), biće vam potrebna tri podatka:




- Javni ključ čvora**: Ovo je jedinstveni identifikator čvora u Bitcoin mreži;
- IP** : IP mašine na kojoj je čvor instaliran;
- PORT** :  Port otvoren na mašini koji omogućava komunikaciju sa ovim čvorom.



Možete pronaći čvorove za povezivanje na [amboss](https://amboss.space/), platformi koja navodi informacije o Lightning čvorovima.



```bash
# Se connecter à un noeud
lncli connect <ID_PUBKEY>@<IP>:<PORT>

# Un exemple  : Connexion au noeud de Wallet of Satoshi
lncli connect 035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226@170.75.163.209:9735
```




Pobrinite se da se povežete na **pouzdane čvorove** kako biste očuvali integritet sopstvenog sistema. Evo nekoliko preporuka za odabir pravih veza.





- Geografska diverzifikacija**: Povežite se sa čvorovima u različitim regionima.





- Reputacija**: Izaberite čvorove sa dobrom dostupnošću.





- Kapacitet**: Izaberite čvorove sa dobrom likvidnošću.





- Optužbe**: Proverite troškove usmeravanja.


### Otvori kanal plaćanja


Da biste otvorili kanal plaćanja, uverite se da ste **povezani** sa čvorom partnera, zatim definišite **kapacitet** (količinu satoshija) koju želite da blokirate u ovom kanalu.



```bash
lncli openchannel --node_key=<ID_PUBKEY> --local_amt=<AMOUNT_SATOSHIS>
```


### Kreiraj Lightning Invoice



Lightning Invoice predstavlja niz karaktera koji izražavaju vašu želju da primite satoshije u vaš Lightning Wallet.


Kreiranje Lightning faktura sa sopstvenim čvorom omogućava vam da zaštitite svoje podatke (geografske i lične) i daje vam 100% autonomiju nad upravljanjem vašim sredstvima.



```bash
# Générer une facture de 1000 sats

lncli addinvoice --amt=1000 --memo="Facture de 1000 sats"
```



### Plaćanje Lightning Invoice



```bash
lncli payinvoice <FACTURE>
```


### Zatvori kanal



Postoje dva načina da zatvorite aktivni kanal na vašem trenutnom čvoru.





- Kooperativno zatvaranje**: Ovo signalizira želju vašeg čvora da se povuče iz platnog kanala, osiguravajući da su tekući zadaci završeni i da su podaci sačuvani kako bi se izbegao gubitak sredstava.


```
lncli closechannel <ID_CANAL>
```




- Prisilno zatvaranje**: ⚠️ Treba ga izbegavati ako je moguće, ova akcija prekida tekuće procese u vašem kanalu plaćanja i povećava rizik od gubitka sredstava.


```
lncli closechannel --force <ID_CANAL>
```


## Najbolje prakse i bezbednost za vaš LND čvor.


Bezbednost je najvažnija kada koristite Bitcoin/ Lightning čvor. Evo nekoliko tačaka za jačanje bezbednosti vaše instalacije:





- Čuvajte svoju `seed frazu` na sigurnom, vanmrežnom mestu.





- Pravovremeno pravite rezervne kopije datoteke `~/.LND/channel.backup`: Ova datoteka čuva stanja vaših kanala svaki put kada se novi kanal otvori (ili stari kanal zatvori) na vašem čvoru.


⚠️ Omogućava vam da obnovite kanale i povratite sredstva blokirana u kanalima plaćanja u slučaju gubitka podataka ili kvara čvora



Možete vratiti svoja sredstva pomoću komande ispod tako što ćete navesti putanju do rezervne kopije ove datoteke:


```
lncli restorechanbackup <CHEMIN_DU_FICHIER>
```




- Uverite se da ste sačuvali reči za obnavljanje i lozinku za Lightning Wallet.
- Ažurirajte svoj sistem redovno.



## Trenutno rešavanje problema


### Česti problemi




- bitcoind greška povezivanja** : Proverite vaše RPC podatke za prijavu
- Sinhronizacija blokirana** : Proverite vašu internet konekciju
- Greška dozvole**: Proverite prava foldera `~/.LND`




Dakle, došli ste do kraja ovog vodiča. Ako želite da saznate više o Lightning-u, nudimo ovaj uvodni kurs kako bismo vam pružili bolje razumevanje koncepata i praksi iza Lightning Network.




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb