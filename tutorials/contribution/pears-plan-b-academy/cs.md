---
name: Mapa ₿ Academy - Pears App
description: Jak nainstalovat a používat aplikaci Plan ₿ Academy v systému Pears?
---

![cover](assets/cover.webp)



Jak pravděpodobně víte, Plan ₿ Academy je největší vzdělávací databáze věnovaná Bitcoin, která sdružuje kurzy, výukové programy a tisíce zdrojů publikovaných pod otevřenou licencí. Původně byla Plan ₿ Academy jen webová stránka. Co by se však stalo, kdybyste k ní již nemohli normálně přistupovat, například v případě cenzury?



V tomto tutoriálu se naučíme, jak provozovat platformu **Plan ₿ Academy** skutečně neomezeným způsobem díky **Pears**, technologii peer-to-peer (P2P) vyvinuté společností **Holepunch** a podporované společností **Tether**.



Pears je software, který nám umožní provozovat platformu Plan ₿ Academy bez závislosti na centralizovaných webových stránkách. V tomto návodu nainstalujeme Pears do počítače, abychom mohli přistupovat k Akademii Plan ₿ prostřednictvím Pears.



Cíl společnosti Pears je jednoduchý: umožnit distribuci a používání webových aplikací bez závislosti na jakékoli centralizované infrastruktuře (žádné servery, žádní hostitelé, žádní zprostředkovatelé). Jinými slovy, i když poskytovatel cloudu ukončí činnost nebo země zablokuje doménu, aplikace žije dál mezi rovnocennými uživateli sítě. Právě tento přístup umožňuje naší vzdělávací platformě Plan ₿ Academy zůstat dostupnou kdekoli na světě, bez jediného bodu selhání.



---

**TL;DR :**





- Instalace hrušek ;





- Spuštěním následujícího příkazu spustíte aplikaci Plan ₿ Academy:



```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```



---

## 1. Instalace hrušek



### 1.1 Co je to hruška?



Pears je běhové prostředí, vývojový nástroj a platforma pro nasazení peer-to-peer aplikací. Tento open-source nástroj umožňuje vytvářet, sdílet a spouštět software bez serveru nebo infrastruktury, přímo mezi uživateli. Konkrétně to znamená, že namísto hostování aplikace na centrálním serveru se každý uživatel stává síťovým uzlem, který sdílí část aplikace a data s ostatními peery. Celý systém tvoří distribuovanou síť, přičemž jednotlivé instance spolupracují na udržení dostupnosti služby.



![Image](assets/fr/01.webp)



Tento přístup je založen na sadě modulárních softwarových bloků vyvinutých společností Holepunch:




- Hypercore**: distribuovaný protokol, který zaručuje konzistenci a zabezpečení dat bez centrální databáze.
- Hyperbee**: indexer nad jádrem Hypercore pro efektivní organizaci a procházení dat.
- Hyperdrive**: distribuovaný souborový systém používaný k ukládání a synchronizaci souborů aplikací mezi rovnocennými uživateli.
- Hyperswarm** a **HyperDHT**: síťové vrstvy, které umožňují zjišťování a propojení mezi rovnocennými uživateli po celém světě bez centrálního serveru.
- Secretstream**: šifrovací protokol E2E pro zabezpečení výměn mezi dvěma rovnocennými uživateli.



Kombinací těchto komponent umožňuje Pears vytvářet autonomní, šifrované a distribuované aplikace, kde se každý uživatel aktivně účastní sítě. Tato decentralizovaná architektura eliminuje náklady na infrastrukturu, rizika cenzury a SPOF (*Single Point of Failure*).



Pears vyvíjí společnost Holepunch, kterou založili Mathias Buus a Paolo Ardoino (generální ředitel Tetheru a technický ředitel Bitfinexu) a jejímž cílem je rozšířit logiku peer-to-peer za hranice Bitcoin. Jejich ambicí je vybudovat "Peer-to-Peer internet", kde může každá aplikace běžet bez autorizace, bez serverů a bez prostředníků. Holepunch již stojí za aplikací **Keet**, která je plně P2P aplikací pro videokonference a zasílání zpráv.



https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*Tento návod na instalaci systému Pears je rozdělen do několika částí v závislosti na operačním systému. Přejděte přímo do části odpovídající vašemu prostředí a postupujte podle příslušných pokynů :*




- Linux (Debian)** → Část **1.2.**
- Windows** → Část **1.3.**
- macOS** → Část **1.4.**




### 1.2 - Jak nainstaluji Pears na Linux (Debian)?



Instalace Pears v systému Debian je poměrně jednoduchá, ale vyžaduje několik předpokladů, které podrobně vysvětlíme v této části.



#### 1.2.1. Aktualizace systému



V první řadě je důležité zajistit, aby byl váš systém aktuální.



```bash
sudo apt update && sudo apt upgrade -y
```



![Image](assets/fr/02.webp)



#### 1.2.2 Instalace závislostí



Pears se spoléhá na řadu systémových knihoven, včetně `libatomic1`, kterou používá běhové prostředí Bare JavaScript. Nainstalujte ji následujícím příkazem:



```bash
sudo apt install -y libatomic1 curl git
```



![Image](assets/fr/03.webp)



#### 1.2.3 Instalace Node.js a npm prostřednictvím NVM



Pears je distribuován prostřednictvím *npm*, správce balíčků *Node.js*. Ačkoli Pears není přímo závislý na *Node.js*, je pro instalaci nezbytný. Doporučenou metodou pro instalaci *Node.js* v systému Linux je *NVM* (*Node Version Manager*), který umožňuje paralelní správu několika verzí Node.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



![Image](assets/fr/04.webp)



Poté znovu načtěte terminál a aktivujte *NVM* :



```bash
source ~/.bashrc
```



![Image](assets/fr/05.webp)



Zkontrolujte, zda je nainstalován *NVM*:



```bash
nvm --version
```



![Image](assets/fr/06.webp)



Poté nainstalujte stabilní verzi *Node.js* (např. aktuální LTS):



```bash
nvm install --lts
```



![Image](assets/fr/07.webp)



Zkontrolujte instalace *Node.js* a *npm*:



```bash
node -v
npm -v
```



![Image](assets/fr/08.webp)



#### 1.2.4 Instalace Pears pomocí npm



Jakmile je k dispozici *npm*, můžete do svého systému globálně nainstalovat Pears CLI. To vám umožní spouštět příkaz `pear` z libovolného adresáře.



```bash
npm install -g pear
```



![Image](assets/fr/09.webp)



#### 1.2.5. Inicializace hrušek



Po instalaci stačí v terminálu spustit následující příkaz:



```bash
pear
```



Při prvním spuštění se systém Pears připojí k síti peer-to-peer a stáhne potřebné komponenty. Tento proces nevyžaduje žádný centrální server: soubory jsou získávány přímo od ostatních peerů.



![Image](assets/fr/10.webp)



Po dokončení stahování spusťte příkaz znovu a zkontrolujte, zda vše funguje:



```bash
pear
```



![Image](assets/fr/11.webp)



Pokud je vše správně nainstalováno, zobrazí se nápověda programu Pears se seznamem dostupných příkazů.



#### 1.2.6. Testování hrušek pomocí Keet



Chcete-li zkontrolovat, zda je systém Pears plně funkční, můžete spustit aplikaci P2P, která je již v síti k dispozici, například Keet, open-source software pro zasílání zpráv a videokonference společnosti Holepunch.



```bash
pear run pear://keet
```



Tento příkaz načte aplikaci Keet přímo ze sítě Pears, aniž by procházela centrálním serverem. Pokud se Keet spustí správně, je instalace Pears plně funkční.



![Image](assets/fr/12.webp)



Váš systém Linux je nyní připraven ke spouštění a hostování peer-to-peer aplikací pomocí Pears.



### 1.3 - Jak nainstaluji hrušku do systému Windows?



Instalace systému Pears v systému Windows je stejně snadná jako v systému Linux, ale vyžaduje několik speciálních nástrojů.



*Pokud používáte systém Linux a máte již nainstalovanou aplikaci Pears, můžete přejít přímo ke kroku 2



#### 1.3.1. Otevření prostředí PowerShell v režimu správce



Nejprve spusťte prostředí PowerShell s právy správce :




- Klikněte na nabídku Start;
- Typ PowerShell ;
- Klikněte pravým tlačítkem myši na položku "*Windows PowerShell*" ;
- Vyberte možnost "*Spustit jako správce*".



![Image](assets/fr/15.webp)



#### 1.3.2. Stáhnout NVS



Pears se instaluje pomocí *npm*, správce balíčků *Node.js*. V systému Windows se podle doporučení Holepunch používá metoda *NVS* (*Node Version Switcher*), která je v tomto systému stabilnější než *NVM*.



V prostředí PowerShell spusťte následující příkaz a nainstalujte nejnovější verzi *NVS* :



```PowerShell
winget install jasongin.nvs
```



![Image](assets/fr/16.webp)



#### 1.3.3. Instalace Node.js



Po instalaci restartujte prostředí PowerShell a zadejte následující příkaz:



```powershell
nvs
```



Měl by se zobrazit seznam dostupných verzí *Node.js*. Stisknutím klávesy `a` na klávesnici vyberte první z nich.



![Image](assets/fr/17.webp)



*Je nainstalován Node.js*.



![Image](assets/fr/18.webp)



#### 1.3.4. Kontrola instalací



Zkontrolujte, zda jsou přístupné *Node.js* a *npm*:



```powershell
node -v
npm -v
```



Oba příkazy musí vrátit číslo verze.



![Image](assets/fr/19.webp)



#### 1.3.5. Instalace Pears pomocí npm



Jakmile máte k dispozici *Node.js* a *npm*, nainstalujte do systému globálně **Pears CLI**:



```powershell
npm install -g pear
```



Tím nainstalujete binární soubor `pear` do globálního adresáře *npm*.



![Image](assets/fr/20.webp)



#### 1.3.6. Kontrola a inicializace Pears



Po dokončení instalace spusťte :



```powershell
pear
```



Při prvním spuštění Pears automaticky stáhne potřebné komponenty ze sítě peer-to-peer. Tento proces může trvat několik okamžiků.



![Image](assets/fr/21.webp)



Pokud vše proběhlo v pořádku, měla by se zobrazit obrazovka nápovědy CLI Pears se seznamem dostupných dílčích příkazů (run, seed, info...).



#### 1.3.7. Testování hrušek pomocí Keet



Chcete-li zkontrolovat, zda je systém Pears plně funkční, můžete spustit aplikaci P2P, která je již v síti k dispozici, například Keet, open-source software pro zasílání zpráv a videokonference společnosti Holepunch.



```bash
pear run pear://keet
```



Tento příkaz načte aplikaci Keet přímo ze sítě Pears, aniž by procházela centrálním serverem. Pokud se Keet spustí správně, je instalace Pears plně funkční.



![Image](assets/fr/22.webp)



Váš systém Windows je nyní připraven ke spouštění a hostování peer-to-peer aplikací pomocí Pears.



### 1.4. Jak nainstalovat hrušky do systému macOS?



Instalace aplikace Pears v systému macOS je podobná instalaci v systému Linux, ale vyžaduje několik úprav specifických pro prostředí Apple. Pojďme tyto kroky společně objevit.



*Pokud používáte systém Linux nebo Windows a máte již nainstalovanou aplikaci Pears, můžete přejít přímo ke kroku 2



#### 1.4.1. Zkontrolujte systémové požadavky



Před instalací se ujistěte, že jsou v systému přítomny nástroje *Xcode Command Line Tools*. Tento balíček poskytuje potřebné kompilační nástroje pro _Node.js_ a jeho závislosti.



Za tímto účelem otevřete terminál pomocí klávesové zkratky `Cmd + mezerník`, poté zadejte `Terminál` a stiskněte klávesu `Enter`. V terminálu pak můžete zadat tento příkaz a spustit instalaci:



```bash
xcode-select --install
```



Pokud jsou nástroje v systému již nainstalovány, systém macOS vás o tom bude informovat.



#### 1.4.2. Instalace NVM



Pears je distribuován prostřednictvím *npm*, správce balíčků *Node.js*. Ačkoli Pears není přímo závislý na *Node.js*, je pro instalaci nezbytný. Doporučenou metodou pro instalaci *Node.js* v systému macOS je *NVM* (*Node Version Manager*), který umožňuje spravovat několik verzí Node paralelně.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



Poté znovu načtěte terminál a aktivujte *NVM* :



```bash
source ~/.zshrc
```



Používáte-li *bash* místo *zsh*, spusťte :



```bash
source ~/.bashrc
```



Poté zkontrolujte, zda je nainstalován *NVM*:



```bash
nvm --version
```



Terminál by měl vrátit verzi *NVM* nainstalovanou ve vašem systému.



#### 1.4.3 Instalace Node.js a npm



Poté nainstalujte stabilní verzi *Node.js* (např. aktuální LTS):



```bash
nvm install --lts
```



Po dokončení instalace zkontrolujte nainstalované verze:



```bash
node -v
npm -v
```



Oba příkazy musí vrátit číslo verze.



#### 1.4.4 Instalace Pears pomocí npm



Jakmile je k dispozici *npm*, můžete do svého systému globálně nainstalovat Pears CLI. To vám umožní spouštět příkaz `pear` z libovolného adresáře.



```bash
npm install -g pear
```



#### 1.4.5. Inicializace hrušek



Po instalaci stačí v terminálu spustit následující příkaz:



```bash
pear
```



Při prvním spuštění se systém Pears připojí k síti peer-to-peer a stáhne potřebné komponenty. Tento proces nevyžaduje žádný centrální server: soubory jsou získávány přímo od ostatních peerů.



Po dokončení stahování spusťte příkaz znovu a zkontrolujte, zda vše funguje:



```bash
pear
```



Pokud je vše správně nainstalováno, zobrazí se nápověda programu Pears se seznamem dostupných příkazů.



#### 1.4.6. Testování hrušek pomocí Keet



Chcete-li zkontrolovat, zda je systém Pears plně funkční, můžete spustit aplikaci P2P, která je již v síti k dispozici, například Keet, open-source software pro zasílání zpráv a videokonference společnosti Holepunch.



```bash
pear run pear://keet
```



Tento příkaz načte aplikaci Keet přímo ze sítě Pears, aniž by procházela centrálním serverem. Pokud se Keet spustí správně, je instalace Pears plně funkční.



Váš systém macOS je nyní připraven ke spouštění a hostování peer-to-peer aplikací pomocí Pears.



## 2. Jak používat Akademii Plan ₿ na hruškách?



Po instalaci a spuštění aplikace Pears můžete přímo spustit platformu **Plan ₿ Academy** prostřednictvím sítě P2P. Stačí v terminálu spustit následující příkaz (jedná se o stejný příkaz pro Linux, Windows i macOS):



```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```



![Image](assets/fr/13.webp)



Po nahrání se v prostředí Pears otevře aplikace Plan ₿ Academy, která je připravena k použití stejně jako původní webové stránky, ale bez závislosti na centrálním serveru.



![Image](assets/fr/14.webp)