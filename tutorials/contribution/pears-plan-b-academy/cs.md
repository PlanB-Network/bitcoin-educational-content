---
name: Plán ₿ Akademie - Aplikace Pears
description: Jak nainstalovat a používat aplikaci Plan ₿ Academy v aplikaci Pears?
---

![cover](assets/cover.webp)


Pravděpodobně již víte, že Plan ₿ Academy je největší vzdělávací databáze věnovaná Bitcoin, která sdružuje kurzy, výukové programy a tisíce zdrojů s otevřeným zdrojovým kódem. Původně byla Plan ₿ Academy webová stránka. Co by se však stalo, kdybyste k ní již nemohli normálně přistupovat, například v případě cenzury?


V tomto tutoriálu se naučíme, jak provozovat platformu **Plan ₿ Academy** způsobem skutečně odolným vůči cenzuře pomocí **Pears**, technologie peer-to-peer (P2P) vyvinuté společností **Holepunch** a podporované společností **Tether**.


Pears je software, který nám umožňuje provozovat platformu Plan ₿ Academy bez závislosti na centralizovaných webových stránkách. V tomto návodu nainstalujeme Pears do počítače, abychom mohli přistupovat k Akademii Plan ₿ prostřednictvím Pears.


Cíl systému Pears je jednoduchý: umožnit distribuci a používání webových aplikací bez závislosti na centralizované infrastruktuře (žádné servery, žádní hostitelé, žádní zprostředkovatelé). Jinými slovy, i když poskytovatel cloudu ukončí činnost nebo země zablokuje doménu, aplikace bude nadále žít mezi rovnocennými uživateli sítě. Tento přístup umožňuje, aby naše vzdělávací platforma Plan ₿ Academy zůstala dostupná po celém světě bez jediného bodu selhání.


---

**TL;DR:**



- Instalace hrušek;



- Spuštěním následujícího příkazu spustíte aplikaci Plan ₿ Academy:


```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


---

## 1. Co je to hruška?


Pears je současně běhové prostředí, vývojový nástroj a platforma pro nasazení peer-to-peer aplikací. Tento open-source nástroj umožňuje vytvářet, sdílet a spouštět software bez serverů a infrastruktury, přímo mezi uživateli. V praxi to znamená, že namísto hostování aplikace na centrálním serveru se každý uživatel stává uzlem sítě: sdílí část aplikace a data s ostatními peery. Celý systém tvoří distribuovanou síť, kde jednotlivé instance spolupracují na udržení dostupnosti služby.


![Image](assets/fr/01.webp)


Tento přístup je založen na sadě modulárních softwarových komponent vyvinutých společností Holepunch:



- Hypercore**: distribuovaný protokol, který zajišťuje konzistenci a zabezpečení dat bez centrální databáze.
- Hyperbee**: index vytvořený nad Hypercore, který umožňuje efektivní uspořádání dat a dotazování.
- Hyperdrive**: distribuovaný souborový systém používaný k ukládání a synchronizaci souborů aplikací mezi rovnocennými uživateli.
- Hyperswarm** a **HyperDHT**: síťové vrstvy, které umožňují vyhledávání partnerů a připojení po celém světě bez centrálního serveru.
- Secretstream**: šifrovací protokol typu end-to-end, který zabezpečuje komunikaci mezi rovnocennými uživateli.


Kombinací těchto komponent umožňuje Pears vytvářet autonomní, šifrované a distribuované aplikace, kde se každý uživatel aktivně účastní sítě. Tato decentralizovaná architektura eliminuje náklady na infrastrukturu, rizika cenzury a SPOF (*Single Points of Failure*).


Pears vyvíjí společnost Holepunch, kterou založili Mathias Buus a Paolo Ardoino (generální ředitel Tetheru a technický ředitel Bitfinexu) a jejímž cílem je rozšířit logiku peer-to-peer za hranice Bitcoin. Jejich ambicí je vybudovat "*Internet peerů*", kde může každá aplikace fungovat bez povolení, bez serverů a bez prostředníků. Holepunch již stojí za aplikací **Keet**, která je plně P2P aplikací pro videokonference a zasílání zpráv.


https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*Tento návod na instalaci systému Pears je rozdělen do několika částí v závislosti na operačním systému. Přejděte přímo na tu, která odpovídá vašemu prostředí, a postupujte podle příslušných pokynů:*



- Linux (Debian)** → Sekce **2**
- Okna** → Oddíl **3**
- macOS** → Oddíl **4**


## 2. Jak nainstalovat Pears v Linuxu (Debian)?


Instalace Pears v Debianu je poměrně jednoduchá, ale vyžaduje několik předpokladů, které podrobně popíšeme v této části.


### 2.1. Aktualizace systému


Dříve než cokoli jiného je důležité se ujistit, že je váš systém aktualizovaný.


```bash
sudo apt update && sudo apt upgrade -y
```


![Image](assets/fr/02.webp)


### 2.2. Instalace závislostí


Pears se spoléhá na některé systémové knihovny, včetně `libatomic1`, kterou používá běhové jádro Bare JavaScript. Nainstalujte ji následujícím příkazem:


```bash
sudo apt install -y libatomic1 curl git
```


![Image](assets/fr/03.webp)


### 2.3. Instalace Node.js a npm přes NVM


Pears je distribuován prostřednictvím *npm*, správce balíčků *Node.js*. Přestože běh aplikace Pears není přímo závislý na *Node.js*, je pro instalaci vyžadován. Doporučený způsob instalace *Node.js* v Linuxu je prostřednictvím *NVM* (*Node Version Manager*), který umožňuje spravovat více verzí Node vedle sebe.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


![Image](assets/fr/04.webp)


Poté znovu načtěte terminál a aktivujte *NVM*:


```bash
source ~/.bashrc
```


![Image](assets/fr/05.webp)


Zkontrolujte, zda je *NVM* správně nainstalován:


```bash
nvm --version
```


![Image](assets/fr/06.webp)


Dále nainstalujte stabilní verzi *Node.js* (například aktuální verzi LTS):


```bash
nvm install --lts
```


![Image](assets/fr/07.webp)


Ověřte, zda jsou správně nainstalovány *Node.js* a *npm*:


```bash
node -v
npm -v
```


![Image](assets/fr/08.webp)


### 2.4. Instalace Pears pomocí npm


Jakmile je k dispozici *npm*, můžete globálně nainstalovat Pears CLI do svého systému. To vám umožní spouštět příkaz `pear` z libovolného adresáře.


```bash
npm install -g pear
```


![Image](assets/fr/09.webp)


### 2.5. Inicializace hrušek


Po instalaci stačí v terminálu spustit následující příkaz:


```bash
pear
```


Při prvním spuštění se Pears připojí k peer-to-peer síti a stáhne potřebné komponenty. Tento proces není závislý na žádném centrálním serveru - soubory se stahují přímo od ostatních peerů.


![Image](assets/fr/10.webp)


Po dokončení stahování spusťte příkaz znovu a potvrďte, že vše funguje:


```bash
pear
```


![Image](assets/fr/11.webp)


Pokud je vše správně nainstalováno, zobrazí se nabídka nápovědy programu Pears se seznamem dostupných příkazů.


### 2.6. Testování hrušek s keetem


Chcete-li ověřit, zda je systém Pears plně funkční, můžete spustit stávající aplikaci P2P dostupnou v síti, například Keet, software s otevřeným zdrojovým kódem pro zasílání zpráv a videokonference vyvinutý společností Holepunch.


```bash
pear run pear://keet
```


Tento příkaz načte aplikaci Keet přímo ze sítě Pears bez použití centrálního serveru. Pokud se Keet spustí správně, znamená to, že instalace Pears je plně funkční.


![Image](assets/fr/12.webp)


Váš systém Linux je nyní připraven ke spouštění a hostování peer-to-peer aplikací pomocí Pears.


## 3. Jak nainstalovat hrušky do systému Windows


Instalace systému Pears v systému Windows je stejně jednoduchá jako v systému Linux, ale vyžaduje několik specifických nástrojů.


*Pokud používáte Linux a máte již nainstalovaný Pears, můžete přejít přímo na **Krok 5**.*


### 3.1. Otevřete prostředí PowerShell jako správce


Nejprve spusťte prostředí PowerShell s právy správce:



- Klikněte na nabídku Start;
- Zadejte "PowerShell";
- Klikněte pravým tlačítkem myši na položku "*Windows PowerShell*";
- Vyberte možnost "*Spustit jako správce*".


![Image](assets/fr/15.webp)


### 3.2. Stáhnout NVS


Pears se instaluje pomocí *npm*, správce balíčků *Node.js*. V systému Windows se podle doporučení Holepunch používá metoda *NVS* (*Node Version Switcher*), která je v tomto systému stabilnější než *NVM*.


V prostředí PowerShell spusťte následující příkaz a nainstalujte nejnovější verzi *NVS*:


```PowerShell
winget install jasongin.nvs
```


![Image](assets/fr/16.webp)


### 3.3. Instalace Node.js


Po instalaci restartujte prostředí PowerShell a zadejte následující příkaz:


```powershell
nvs
```


Měl by se zobrazit seznam dostupných verzí *Node.js*. Stisknutím klávesy `a` na klávesnici vyberte první z nich.


![Image](assets/fr/17.webp)


*Node.js* je nyní nainstalován.


![Image](assets/fr/18.webp)


### 3.4. Ověřování instalací


Zkontrolujte, zda jsou přístupné *Node.js* a *npm*:


```powershell
node -v
npm -v
```


Oba příkazy by měly vrátit číslo verze.


![Image](assets/fr/19.webp)


### 3.5. Instalace Pears pomocí npm


Jakmile máte k dispozici *Node.js* a *npm*, nainstalujte do systému globálně **Pears CLI**:


```powershell
npm install -g pear
```


Tím nainstalujete binární soubor `pear` do globálního adresáře *npm*.


![Image](assets/fr/20.webp)


### 3.6. Ověření a inicializace hrušek


Po dokončení instalace spusťte:


```powershell
pear
```


Při prvním spuštění Pears automaticky stáhne potřebné komponenty ze sítě peer-to-peer. Tento proces může trvat několik okamžiků.


![Image](assets/fr/21.webp)


Pokud vše proběhlo v pořádku, měla by se zobrazit nabídka nápovědy Pears CLI se seznamem dostupných dílčích příkazů (run, seed, info...).


### 3.7. Testování hrušek s keetem


Chcete-li ověřit, zda je systém Pears plně funkční, můžete spustit stávající aplikaci P2P dostupnou v síti, například Keet - open-source software pro zasílání zpráv a videokonference vyvinutý společností Holepunch.


```bash
pear run pear://keet
```


Tento příkaz načte aplikaci Keet přímo ze sítě Pears bez použití centrálního serveru. Pokud se Keet úspěšně spustí, znamená to, že instalace Pears je plně funkční.


![Image](assets/fr/22.webp)


Váš systém Windows je nyní připraven ke spouštění a hostování peer-to-peer aplikací pomocí Pears.


## 4. Jak nainstalovat hrušky do systému macOS


Instalace Pears v systému macOS je podobná jako v Linuxu, ale vyžaduje několik úprav specifických pro prostředí Apple. Pojďme si tyto kroky společně projít.


*Pokud používáte systém Linux nebo Windows a máte již nainstalovaný systém Pears, můžete přejít přímo ke kroku 5**.*


### 4.1. Zkontrolujte systémové předpoklady


Před instalací se ujistěte, že jsou v systému nainstalovány nástroje *Xcode Command Line Tools*. Tento balíček poskytuje potřebné nástroje pro sestavení *Node.js* a jeho závislostí.


Za tímto účelem otevřete terminál pomocí klávesové zkratky `Cmd + mezerník`, zadejte `Terminál` a stiskněte `Enter`. Poté v terminálu spusťte následující příkaz pro instalaci:


```bash
xcode-select --install
```


Pokud jsou nástroje v systému již nainstalovány, systém macOS vás na to upozorní.


### 4.2. Instalace NVM


Pears je distribuován prostřednictvím *npm*, správce balíčků *Node.js*. Přestože funkce aplikace Pears není přímo závislá na *Node.js*, je pro instalaci vyžadována. Doporučeným způsobem instalace *Node.js* v systému MacOS je *NVM* (*Node Version Manager*), který umožňuje spravovat více verzí Node současně.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


Poté znovu načtěte terminál a aktivujte *NVM*:


```bash
source ~/.zshrc
```


Pokud místo *zsh* používáte *bash*, spusťte:


```bash
source ~/.bashrc
```


Dále zkontrolujte, zda je *NVM* správně nainstalován:


```bash
nvm --version
```


Terminál by měl zobrazit nainstalovanou verzi *NVM*.


### 4.3. Instalace Node.js a npm


Dále nainstalujte stabilní verzi *Node.js* (například aktuální verzi LTS):


```bash
nvm install --lts
```


Po dokončení instalace ověřte nainstalované verze:


```bash
node -v
npm -v
```


Oba příkazy by měly vrátit číslo verze.


### 4.4. Instalace Pears pomocí npm


Jakmile je k dispozici *npm*, můžete globálně nainstalovat Pears CLI do svého systému. To vám umožní spouštět příkaz `pear` z libovolného adresáře.


```bash
npm install -g pear
```


### 4.5. Inicializace hrušek


Po instalaci stačí v terminálu spustit následující příkaz:


```bash
pear
```


Při prvním spuštění se Pears připojí k peer-to-peer síti a stáhne potřebné komponenty. Tento proces nevyžaduje žádný centrální server - soubory jsou stahovány přímo od ostatních peerů.


Po dokončení stahování znovu spusťte příkaz a ověřte, zda vše funguje:


```bash
pear
```


Pokud je vše správně nainstalováno, zobrazí se nabídka nápovědy Pears se seznamem dostupných příkazů.


### 4.6. Testování hrušek s keetem


Chcete-li ověřit, zda je systém Pears plně funkční, můžete spustit aplikaci P2P, která je již v síti k dispozici, například Keet, open-source software pro zasílání zpráv a videokonference od společnosti Holepunch.


```bash
pear run pear://keet
```


Tento příkaz načte aplikaci Keet přímo ze sítě Pears bez použití centrálního serveru. Pokud se Keet úspěšně spustí, znamená to, že instalace Pears je plně funkční.


Váš systém macOS je nyní připraven ke spouštění a hostování peer-to-peer aplikací pomocí Pears.


## 5. Jak používat Akademii Plan ₿ na hruškách


Po instalaci a spuštění aplikace Pears můžete přímo spustit platformu **Plan ₿ Academy** prostřednictvím sítě P2P. Stačí v terminálu spustit následující příkaz (stejný příkaz funguje v systémech Linux, Windows a MacOS):


```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


![Image](assets/fr/13.webp)


Po dokončení načítání se v prostředí Pears otevře aplikace Plan ₿ Academy, která je připravena k použití stejně jako původní webové stránky, ale bez závislosti na centrálním serveru.


![Image](assets/fr/14.webp)


## 6. Jak plánovat výsev ₿ Akademie o hruškách


V síti Pears znamená *seed* aplikaci přerozdělit ji ostatním partnerům z vlastního počítače. V praxi se při seed Plan ₿ Academy váš počítač stává zdrojem dat, který umožňuje ostatním uživatelům stahovat aplikaci bez závislosti na centrálním serveru.


Tento mechanismus posiluje odolnost a cenzuru naší aplikace v síti Pears. Čím více peerů seed aplikaci poskytuje, tím je dostupnější a decentralizovanější, a to i v případě, že některé původní uzly vypadnou z provozu.


Chcete-li pomoci s distribucí akademie Plan ₿, stačí spustit následující příkaz:


```bash
pear seed pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


Dokud bude tento příkaz aktivní, bude se zařízení podílet na distribuci souborů aplikace. Pokud terminál zavřete, proces sdílení se zastaví.


Chcete-li pokračovat ve vysílání i po restartu, můžete spustit příkaz na pozadí nebo vytvořit systémovou službu - například službu systemd v systému Linux, LaunchAgent v systému MacOS nebo naplánovanou úlohu v systému Windows. Tyto metody zajistí, že aplikace Plan ₿ Academy bude automaticky pokračovat v seeding při spuštění systému.


Děkujeme, že jste přispěli k decentralizovanému šíření Akademie Plán ₿ na hruškách a pomohli tak učinit vzdělávání Bitcoin skutečně odolným vůči cenzuře!