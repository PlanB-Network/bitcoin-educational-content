---
name: Lightning Network Daemon (Linux)
description: Instalace a spuštění Lightning Network Daemon v systému Linux
---

![cover-lightning-network-daemon](assets/cover.webp)



Lightning Network je druhým Layer Bitcoin, což mu umožňuje nabývat bleskových rozměrů, zejména díky rychlosti a nízké ceně transakcí, které nabízí.



V tomto návodu nainstalujeme implementaci Lightning Network Daemon na náš počítač se systémem Linux (distribuce Ubuntu 24.04).



## Co je Lightning Network Daemon?



Lightning Network Daemon je kompletní implementací Lightning Network v jazyce Go. Vytvořila ji společnost Lightning Labs a umožňuje spustit na vašem počítači plnou instanci uzlu Lightning.


Jinými slovy, díky této implementaci můžete :





- Interakce s Lightning Network**: Pomocí příkazových řádků můžete vytvářet portfolia Lightning, spravovat platební kanály a trasy a mnoho dalšího přímo z terminálu počítače.
- Propojení vzdáleného uzlu Bitcoin nebo vlastní instance jádra Bitcoin**: LND umožňuje propojit instanci Bitcoin a používat ji jako backend. Pro použití této implementace nemusíte mít na svém počítači spuštěnou instanci jádra Bitcoin.




https://planb.network/fr/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

## Proč mít vlastní uzel Lightning?


Lightning je překryvný systém Bitcoin, který optimalizuje proces převodu a snižuje transakční náklady.



Rotací uzlu Lightning získáte suverenitu a nezávislost. Své prostředky máte pod kontrolou, takže mějte na paměti:



"Ne vaše klíče, ne vaše bitcoiny."



V tomto smyslu zvyšuje provoz uzlu Lightning bezpečnost a integritu vašich dat následujícími způsoby:





- Úplná kontrola**: Spravujte své vlastní platební kanály, staňte se svou vlastní bankou a buďte pánem svého majetku.
- Důvěrnost**: Transakce probíhají bez spoléhání se na třetí strany, které chrání vaše soukromí.
- Učení a samostatnost**: Díky příkazům `lncli` můžete lépe porozumět základním procesům systému Lightning, a to tak, že se sami přihlásíte z terminálu.
- Decentralizace**: Bitcoin / Lightning Network: aktivně se podílejte na posilování a decentralizaci Bitcoin / Lightning Network.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


Pro spuštění instance implementace LND na našem počítači máte dvě možnosti. Buď můžeme prostředí nastavit na vlastním počítači, aby běželo lokálně, nebo můžeme LND nainstalovat z kontejneru Docker. Zde se zaměříme na první možnost a v některém z dalších tutoriálů se podíváme, jak postupovat s Dockerem.


## Instalace LND ze zdrojového kódu



### Předpoklady


Protože je LND napsán v jazyce Go, musíte se ujistit, že máte na počítači s Linuxem prostředí GoLang a potřebné závislosti.





- Hardwarové požadavky:**


Pro hladký a bezproblémový provoz musí mít váš počítač potřebnou kapacitu pro provoz uzlu LND Lightning.



Budete potřebovat :


1. **8 GB RAM** pro optimální plynulost,


2. **Vícejádrový procesor (čtyřjádrový nebo více)** pro efektivní správu činností uzlu,


3. **Nejméně 5 GB místa na disku** pro režim ořezaného uzlu a 1 TB pro spuštění jádra Bitcoin (volitelné, pokud používáte vzdálený uzel)





- Instalace užitečných závislostí:**


Níže uvedený příkaz vám umožní nainstalovat do počítače nástroje potřebné ke spuštění LND. Mimo jiné budete potřebovat nainstalovat `Git`, nástroj pro správu verzí, a `make`, který dokáže spustit a sestavit implementaci LND ze zdrojového kódu.



```bash
sudo apt install -y build-essential git make
```



![installation-dependances](assets/fr/01.webp)





- Instalace GoLangu do počítače se systémem Linux**



K datu vydání tohoto návodu vyžaduje LND k instalaci verzi 1.23.6 aplikace Go***.



Pokud jste již měli nainstalovanou předchozí verzi, pro novou instalaci Go ji odstraňte.


```bash
# Suppression d'une ancienne version de Go
sudo rm -rf /usr/local/go

# Installation de la version 1.23.6 de Go
wget https://golang.org/dl/go1.23.6.linux-amd64.tar.gz

# Decompression du package

sudo tar -C /usr/local -xzf go1.23.6.linux-amd64.tar.gz

```



![go-install](assets/fr/02.webp)





- Konfigurace prostředí Go**


V souboru `~/.bashrc` inicializujte následující proměnné prostředí, abyste do systému Linux přidali příkaz Go.



```bash
# Configuration de l'environnement Go
export GOROOT=/usr/local/go
export GOPATH=~/gocode
export PATH=$PATH:$GOROOT/bin

# Appliquer les modifications

source ~/.bashrc
```





- Kontrola instalace** (ve francouzštině)


```bash
go version
```



![go-version](assets/fr/03.webp)


### Klonování repozitáře LND GitHub



Pomocí služby git získáte kopii zdrojového kódu LND lokálně ve svém počítači


```bash
git clone https://github.com/lightningnetwork/lnd.git
```


![clone-lnd](assets/fr/04.webp)


### Sestavení a instalace



Dříve nainstalovaný nástroj `make` vám umožní sestavit spustitelný soubor ze zdrojového kódu LND a pokračovat v instalaci.



```bash
# Acceder au repertoire clonné
cd lnd

# construire LND
make
```



Nainstalujte si do počítače program LND



```bash
# installer LND
make install
```



![make-lnd](assets/fr/06.webp)




- Kontrola instalace** (ve francouzštině)



Chcete-li se ujistit, že vše proběhlo bez problémů, spusťte tento příkaz a zjistěte, jakou verzi systému LND právě používáte.



```bash
# Version de LND
lnd --version

# Version  de LNCLI
lncli --version
```


![lnd-version](assets/fr/05.webp)




- Údržba a modernizace



```bash
cd lnd
git pull
make clean && make && make install
```


⚠️ **DŮLEŽITÉ**: Aktualizace LND mohou vyžadovat novější verze Go, proto nezapomeňte aktualizovat svůj systém, abyste se vyhnuli problémům se závislostmi během instalace.


### Konfigurace Lightning Network Daemon



Konfigurace uzlu Lightning LND je podobná konfiguraci uzlu Bitcoin a provádí se v konfiguračním souboru, který obsahuje všechny parametry uzlu. Za tímto účelem můžete v kořenovém adresáři svého počítače vytvořit skrytou složku `.LND` a v ní pak vytvořit konfigurační soubor `LND.conf`.



```bash
# Création du ficher
mkdir -p ~/.lnd

cd ~/.lnd

# Fichier de configuration
touch lnd.conf
```





V konfiguračním souboru můžete nastavit uzel LND.



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



## Pochopení konfigurace



Je důležité, abyste věděli, jakou minimální konfiguraci potřebujete pro správnou a úplnou instalaci uzlu LND.



Na základě obsahu souboru `~/.LND/LND.conf` jsou zde uvedeny podrobnosti o polích:





- noseedbackup**: Umožňuje zvolit, zda chcete, aby společnost LND prováděla automatické zálohování vašich portfolií.  Nastavení této vlastnosti na `0` vám umožní ručně ukládat informace o obnově do osobně zvoleného zabezpečeného umístění.





- debuglevel**: Umožňuje definovat úroveň podrobnosti chyb a protokolů v případě chyb, které se vyskytnou během akce.





- Bitcoin.active**: LND je instruován, aby pracoval jako uzel Bitcoin a komunikoval se sítí Bitcoin.





- Bitcoin.Mainnet**: Pro sítě Bitcoin Signet a Bitcoin Regtest lze nastavit hodnoty `bitcoind.signet` a `bitcoind.regtest`





- Bitcoin.node**: Určuje typ uzlu Bitcoin, ke kterému se má LND připojit.





- Bitcoin.rpcuser** a **Bitcoin.rpcpassword** : Zastupují.


resp. přihlašovací údaje (uživatel, heslo) pro připojení k uzlu Bitcoin





- bitcoind.zmqpubrawblock** a **bitcoind.zmqpubrawtx**: definují koncové body ZeroMQ pro příjem oznámení o nových blocích a transakcích v síti Bitcoin.




## Kontrola instalace pomocí LND



Pravděpodobně se budete chtít ujistit, že proces proběhl úspěšně a že se synchronizujete se serverem Lightning Network, aby byly informace o uzlu aktuální.



Chcete-li spustit implementaci LND a získat informace o uzlu, zadejte příkaz :


```bash
lnd getinfo
```


![lnd-getinfo](assets/fr/07.webp)


## Provádění akcí na LND



Po dokončení a kontrole instalace ji můžete začít používat.


Zde jsou základní příkazy, které vám pomohou začít.



### Vytvoření portfolia


Vaše portfolio Lightning je prvním krokem při jakékoli akci na správu vašich finančních prostředků.



⚠️ **DŮLEŽITÉ**: Pozorně si zapište svou 24slovnou větu **seed**. Budete ji potřebovat k tomu, abyste mohli v případě problémů získat zpět své finanční prostředky.



Uložte si také heslo k uzlu Wallet, abyste jej mohli odemknout příkazem `lncli unlock` při restartování uzlu LND.



```bash
lncli create
```


![créer-portefeuille](assets/fr/08.webp)


### Zkontrolujte si zůstatek



Nahlížejte do svých účtů přímo z terminálu:



```bash
lncli walletbalance
```


![solde](assets/fr/09.webp)


### Informace o vašem uzlu



Pomocí níže uvedeného příkazu zjistíte, které kanály jsou ve vašem uzlu aktivní.



```bash
lncli listchannels
```



Můžete také získat seznam uzlů, ke kterým jste připojeni.



```bash
lncli listpeers
```



### Správa kanálů



Kanál Lightning umožňuje **přímé párové spojení s jiným uzlem Lightning Network**. V tomto kanálu můžete volně používat Exchange Satoshis až do výše kapacity kanálu.



### Připojení k uzlu



Pokud se chcete aktivně zapojit a využívat sílu služby Lightning, je připojení k ostatním uzlům Lightning zásadní činností.



Chcete-li se připojit k uzlu Lightning, budete potřebovat tři informace:




- Veřejný klíč uzlu**: Jedná se o jedinečný identifikátor uzlu v síti Bitcoin;
- IP** : IP adresa počítače, na kterém je uzel nainstalován;
- PORT** :  Port otevřený na počítači, který umožňuje komunikaci s tímto uzlem.



Uzly, ke kterým se můžete připojit, najdete na platformě [amboss](https://amboss.space/), kde jsou uvedeny informace o uzlech Lightning.



```bash
# Se connecter à un noeud
lncli connect <ID_PUBKEY>@<IP>:<PORT>

# Un exemple  : Connexion au noeud de Wallet of Satoshi
lncli connect 035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226@170.75.163.209:9735
```




Ujistěte se, že se připojujete k **spolehlivým uzlům**, abyste zachovali integritu vlastního systému. Zde je několik doporučení pro výběr správných připojení.





- Geografická diverzifikace**: Připojení k uzlům v různých regionech.





- Pověst**: Vybírejte uzly s dobrou dostupností.





- Kapacita**: Vybírejte uzly s dobrou likviditou.





- Poplatky**: Poplatky za směrování šeků.


### Otevření platebního kanálu


Chcete-li otevřít platební kanál, ujistěte se, že jste **připojeni** k uzlu peer, a poté definujte **kapacitu** (množství satošů), kterou chcete v tomto kanálu blokovat.



```bash
lncli openchannel --node_key=<ID_PUBKEY> --local_amt=<AMOUNT_SATOSHIS>
```


### Vytvoření blesku Invoice



Blesk Invoice představuje řetězec znaků vyjadřující vaše přání obdržet satoši v blesku Wallet.


Vytváření faktur Lightning s vlastním uzlem umožňuje chránit vaše údaje (geografické i osobní) a dává vám 100% autonomii nad správou vašich prostředků.



```bash
# Générer une facture de 1000 sats

lncli addinvoice --amt=1000 --memo="Facture de 1000 sats"
```



### Platba za blesk Invoice



```bash
lncli payinvoice <FACTURE>
```


### Zavření kanálu



Aktivní kanál v aktuálním uzlu lze uzavřít dvěma způsoby.





- Uzavření spolupráce**: To signalizuje přání uzlu odstoupit od platebního kanálu, čímž se zajistí dokončení probíhajících úkolů a zálohování dat, aby se zabránilo ztrátě finančních prostředků.


```
lncli closechannel <ID_CANAL>
```




- Nucené uzavření**: tato akce přeruší probíhající procesy v platebním kanálu a zvyšuje riziko ztráty finančních prostředků.


```
lncli closechannel --force <ID_CANAL>
```


## Osvědčené postupy a bezpečnost pro uzel LND.


Při používání uzlu Bitcoin/ Lightning je nejdůležitější bezpečnost. Zde je několik bodů, které posílí bezpečnost vaší instalace:





- Frázi `seed` uchovávejte na bezpečném místě mimo síť.





- Pravidelně zálohujte soubor `~/.LND/channel.backup`: Tento soubor ukládá stavy kanálů pokaždé, když je na vašem uzlu otevřen nový kanál (nebo uzavřen starý kanál).


⚠️ Umožňuje obnovit kanály a získat zpět prostředky zablokované v platebních kanálech v případě ztráty dat nebo selhání uzlu



Prostředky můžete obnovit pomocí níže uvedeného příkazu, ve kterém zadáte cestu k záloze tohoto souboru:


```
lncli restorechanbackup <CHEMIN_DU_FICHIER>
```




- Ujistěte se, že jste uložili slova a heslo pro obnovení aplikace Lightning Wallet.
- Udržujte svůj systém aktualizovaný.



## Řešení aktuálních problémů


### Časté problémy




- Chyba připojení bitcoind** : Zkontrolujte přihlašovací údaje k RPC
- Synchronizace zablokována** : Zkontrolujte připojení k internetu
- Chyba oprávnění**: Zkontrolujte práva složky `~/.LND`




Dostali jste se na konec tohoto návodu. Pokud se chcete dozvědět více o systému Lightning, nabízíme vám tento úvodní kurz, který vám umožní lépe porozumět koncepcím a postupům, které se skrývají za systémem Lightning Network.




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb