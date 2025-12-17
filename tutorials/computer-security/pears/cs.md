---
name: Pears
description: Jak mohu instalovat a používat aplikace v systému Pears?
---

![cover](assets/cover.webp)



V tomto kurzu se naučíme spouštět aplikace na **Pears**, technologii peer-to-peer (P2P) vyvinuté společností **Holepunch** a podporované společností **Tether**. Cíl je jednoduchý: umožnit distribuci a používání webových aplikací bez závislosti na jakékoli centralizované infrastruktuře (žádné servery, žádní hostitelé, žádní prostředníci). Jinými slovy, i když poskytovatel cloudu ukončí činnost nebo země zablokuje doménu, aplikace žije dál mezi rovnocennými uživateli sítě.



## 1. Co je to hruška?



Pears je běhové prostředí, vývojový nástroj a platforma pro nasazení peer-to-peer aplikací. Tento open-source nástroj umožňuje vytvářet, sdílet a spouštět software bez serveru nebo infrastruktury, přímo mezi uživateli. Konkrétně to znamená, že namísto hostování aplikace na centrálním serveru se každý uživatel stává síťovým uzlem, který sdílí část aplikace a data s ostatními peery. Celý systém tvoří distribuovanou síť, přičemž jednotlivé instance spolupracují na udržení dostupnosti služby.



![Image](assets/fr/01.webp)



Tento přístup je založen na sadě modulárních softwarových bloků vyvinutých společností Holepunch:




- Hypercore**: distribuovaný protokol, který zaručuje konzistenci a zabezpečení dat bez centrální databáze.
- Hyperbee**: indexer nad jádrem Hypercore pro efektivní organizaci a procházení dat.
- Hyperdrive**: distribuovaný souborový systém používaný k ukládání a synchronizaci souborů aplikací mezi rovnocennými uživateli.
- Hyperswarm** a **HyperDHT**: síťové vrstvy, které umožňují zjišťování a propojení mezi rovnocennými uživateli po celém světě bez centrálního serveru.
- Secretstream**: šifrovací protokol E2E pro zabezpečení výměn mezi dvěma rovnocennými uživateli.



Kombinací těchto komponent umožňuje Pears vytvářet autonomní, šifrované a distribuované aplikace, kde se každý uživatel aktivně účastní sítě. Tato decentralizovaná architektura eliminuje náklady na infrastrukturu, rizika cenzury a SPOF (*Single Point of Failure*).



## 2. Vznik a filozofie projektu



Pears vyvíjí společnost Holepunch, kterou založili Mathias Buus a Paolo Ardoino (generální ředitel Tetheru a technický ředitel Bitfinexu) a jejímž cílem je rozšířit logiku peer-to-peer za hranice Bitcoin. Jejich ambicí je vybudovat "Peer-to-Peer internet", kde může každá aplikace běžet bez autorizace, bez serverů a bez prostředníků. Holepunch již stojí za aplikací **Keet**, která je plně P2P videokonferenční aplikací a aplikací pro zasílání zpráv.



*Tento návod na instalaci systému Pears je rozdělen do několika částí v závislosti na operačním systému. Přejděte přímo do části odpovídající vašemu prostředí a postupujte podle příslušných pokynů :*




- Linux (Debian)** → Část **3**
- Okna** → Část **4**
- macOS** → Část **5**



## 3. Jak nainstalovat hrušky v Linuxu (Debian)



Instalace Pears v systému Debian je poměrně jednoduchá, ale vyžaduje několik předpokladů, které podrobně popíšeme v této části.



### 3.1. aktualizace systému



V první řadě je důležité zajistit, aby byl váš systém aktuální.



```bash
sudo apt update && sudo apt upgrade -y
```



![Image](assets/fr/02.webp)



### 3.2. nainstalujte závislosti



Pears se spoléhá na některé systémové knihovny, zejména `libatomic1`, které používá běhové prostředí Bare JavaScript. Nainstalujte ji následujícím příkazem:



```bash
sudo apt install -y libatomic1 curl git
```



![Image](assets/fr/03.webp)



### 3.3. nainstalujte Node.js a npm přes NVM



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



### 3.4 Instalace Pears pomocí npm



Jakmile je k dispozici *npm*, můžete do svého systému globálně nainstalovat Pears CLI. To vám umožní spouštět příkaz `pear` z libovolného adresáře.



```bash
npm install -g pear
```



![Image](assets/fr/09.webp)



### 3.5. Inicializace hrušek



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



### 3.6. Testování hrušek s Keetem



Chcete-li zkontrolovat, zda je systém Pears plně funkční, můžete spustit aplikaci P2P, která je již v síti k dispozici, například Keet, open-source software pro zasílání zpráv a videokonference společnosti Holepunch.



```bash
pear run pear://keet
```



Tento příkaz načte aplikaci Keet přímo ze sítě Pears, aniž by procházela centrálním serverem. Pokud se Keet spustí správně, je instalace Pears plně funkční.



![Image](assets/fr/12.webp)



Váš systém Linux je nyní připraven ke spouštění a hostování peer-to-peer aplikací pomocí Pears.



## 4. Jak nainstalovat hrušky do systému Windows



Instalace systému Pears v systému Windows je stejně snadná jako v systému Linux, ale vyžaduje několik speciálních nástrojů.



*Pokud používáte systém Linux, můžete přeskočit na krok 6.*



### 4.1. otevřete prostředí PowerShell v režimu správce



Nejprve spusťte prostředí PowerShell s právy správce :




- Klikněte na nabídku Start;
- Typ PowerShell ;
- Klikněte pravým tlačítkem myši na položku "*Windows PowerShell*" ;
- Vyberte možnost "*Spustit jako správce*".



![Image](assets/fr/15.webp)



### 4.2. stáhněte si NVS



Pears se instaluje pomocí *npm*, správce balíčků *Node.js*. V systému Windows se podle doporučení Holepunch používá metoda *NVS* (*Node Version Switcher*), která je v tomto systému stabilnější než *NVM*.



V prostředí PowerShell spusťte následující příkaz a nainstalujte nejnovější verzi *NVS* :



```PowerShell
winget install jasongin.nvs
```



![Image](assets/fr/16.webp)



### 4.3. nainstalujte Node.js



Po instalaci restartujte prostředí PowerShell a zadejte následující příkaz:



```powershell
nvs
```



Měl by se zobrazit seznam dostupných verzí *Node.js*. Stisknutím klávesy `a` na klávesnici vyberte první z nich.



![Image](assets/fr/17.webp)



*Je nainstalován Node.js*.



![Image](assets/fr/18.webp)



### 4.4. Kontrola instalací



Zkontrolujte, zda jsou přístupné *Node.js* a *npm*:



```powershell
node -v
npm -v
```



Oba příkazy musí vrátit číslo verze.



![Image](assets/fr/19.webp)



### 4.5. Instalace Pears pomocí npm



Jakmile máte k dispozici *Node.js* a *npm*, nainstalujte do systému globálně **Pears CLI**:



```powershell
npm install -g pear
```



Tím nainstalujete binární soubor `pear` do globálního adresáře *npm*.



![Image](assets/fr/20.webp)



### 4.6. Zkontrolujte a inicializujte hrušky



Po dokončení instalace spusťte :



```powershell
pear
```



Při prvním spuštění Pears automaticky stáhne potřebné komponenty ze sítě peer-to-peer. Tento proces může trvat několik okamžiků.



![Image](assets/fr/21.webp)



Pokud vše proběhlo v pořádku, měla by se zobrazit obrazovka nápovědy CLI Pears se seznamem dostupných dílčích příkazů (run, seed, info...).



### 4.7. Testování hrušek s Keetem



Chcete-li zkontrolovat, zda je systém Pears plně funkční, můžete spustit aplikaci P2P, která je již v síti k dispozici, například Keet, open-source software pro zasílání zpráv a videokonference společnosti Holepunch.



```bash
pear run pear://keet
```



Tento příkaz načte aplikaci Keet přímo ze sítě Pears, aniž by procházela centrálním serverem. Pokud se Keet spustí správně, je instalace Pears plně funkční.



![Image](assets/fr/22.webp)



Váš systém Windows je nyní připraven ke spouštění a hostování peer-to-peer aplikací pomocí Pears.



## 5. Jak nainstaluji hrušky do systému macOS?



Instalace aplikace Pears v systému macOS je podobná instalaci v systému Linux, ale vyžaduje několik úprav specifických pro prostředí Apple. Pojďme tyto kroky společně objevit.



*Pokud používáte systém Linux nebo Windows a máte již nainstalovaný systém Pears, můžete přejít přímo ke kroku 6**.*



### 5.1. Zkontrolujte systémové požadavky



Před instalací se ujistěte, že jsou v systému přítomny nástroje *Xcode Command Line Tools*. Tento balíček poskytuje potřebné kompilační nástroje pro _Node.js_ a jeho závislosti.



Za tímto účelem otevřete terminál pomocí klávesové zkratky `Cmd + mezerník`, poté zadejte `Terminál` a stiskněte klávesu `Enter`. V terminálu pak můžete zadat tento příkaz a spustit instalaci:



```bash
xcode-select --install
```



Pokud jsou nástroje v systému již nainstalovány, systém macOS vás o tom bude informovat.



### 5.2. nainstalujte NVM



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



### 5.3. nainstalujte Node.js a npm



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



### 5.4 Instalace Pears pomocí npm



Jakmile je k dispozici *npm*, můžete do svého systému globálně nainstalovat Pears CLI. To vám umožní spouštět příkaz `pear` z libovolného adresáře.



```bash
npm install -g pear
```



### 5.5. Inicializace hrušek



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



### 5.6. Testování hrušek s Keetem



Chcete-li zkontrolovat, zda je systém Pears plně funkční, můžete spustit aplikaci P2P, která je již v síti k dispozici, například Keet, open-source software pro zasílání zpráv a videokonference společnosti Holepunch.



```bash
pear run pear://keet
```



Tento příkaz načte aplikaci Keet přímo ze sítě Pears, aniž by procházela centrálním serverem. Pokud se Keet spustí správně, je instalace Pears plně funkční.



Váš systém macOS je nyní připraven ke spouštění a hostování peer-to-peer aplikací pomocí Pears.



## 6. Jak se aplikace používá v systému Pears?



Po spuštění aplikace Pears můžete vybranou aplikaci spustit přímo pomocí následujícího příkazu:



```bash
pear run pear://[KEY]
```



Jednoduše nahraďte `[KEY]` klíčem aplikace, který chcete použít.



![Image](assets/fr/13.webp)



Chcete-li se dozvědět, jak spustit naši platformu Plan ₿ Academy na platformě Pears, podívejte se na tento komplexní návod :



https://planb.academy/tutorials/contribution/others/pears-plan-b-academy-77f0ae28-28fc-4465-a9f1-1c6654711770

A pokud chcete zjistit, jak používat aplikaci pro zasílání zpráv Keet, kterou jste právě spustili v systému Pears, podívejte se na tento návod :



https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b