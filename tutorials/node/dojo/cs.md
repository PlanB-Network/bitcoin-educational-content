---
name: Dojo
description: Uzel Bitcoin s otevřeným zdrojovým kódem pro soukromí a autonomii
---

![cover](assets/cover.webp)



*Tento návod vychází z [oficiální dokumentace Ashigaru](https://ashigaru.rs/docs/), kterou jsem převzal a rozšířil. Přepsal jsem všechny části, abych zlepšil jejich přehlednost, přidal další podrobná vysvětlení a také ilustrace pro začátečníky, abych usnadnil pochopení instalace a používání.*



---

Dojo je open-source program určený k tomu, aby fungoval jako backendový server pro některé peněženky Bitcoin orientované na soukromí, založený na uzlu Bitcoin core. Historicky byl vyvinut pro spolupráci s mobilním Wallet Samourai, který nabízel pokročilé funkce ochrany soukromí, jako jsou Whirlpool (CoinJoin), Ricochet, Stonewall, PayNym... Samourai Wallet byl nyní po zatčení jeho vývojářů uzavřen, ale jeho komunitní nástupce, **Ashigaru Wallet**, převzal jeho úlohu a nadále se spoléhá na Dojo, aby nabídl kompletní zážitek pro uživatele, kteří si chtějí udržet kontrolu nad svými daty při používání Bitcoin.



![Image](assets/fr/01.webp)



V praxi funguje Dojo jako brána mezi vaším Wallet a sítí Bitcoin. Bez systému Dojo by se odlehčený mobilní systém Wallet musel dotazovat serverů třetích stran, aby získal stav vašich UTXO a vaši historii nebo aby mohl vysílat vaše transakce. To znamená závislost a únik citlivých údajů na server třetí strany (použité adresy, částky, frekvence plateb atd.). V systému Dojo si tento server hostujete sami, přímo připojený k vašemu vlastnímu uzlu Bitcoin. Všechny vaše požadavky na portfolio tak procházejí infrastrukturou, kterou máte pod kontrolou, bez prostředníků, což posiluje vaši důvěrnost a suverenitu.



## Požadavky na zřízení Dojo



Nastavení serveru Dojo nevyžaduje mimořádně výkonný stroj. Každý, kdo má základní počítač, stabilní připojení k internetu a schopnost nechat jej nepřetržitě zapnutý (24 hodin denně, 7 dní v týdnu), může zřídit funkční Dojo.



### Vyberte si typ stroje



Můžete použít :




- notebook;
- stolní počítač;
- mini PC (např. Intel NUC, Lenovo Thincentre Tiny...).



Každá možnost má své výhody a nevýhody:




- Cena: repasovaný mini PC nebo stolní počítač je často levnější než nový notebook.
- Plocha: Mini-PC zabírá méně místa.
- Napájení Supply: notebook má výhodu baterie, což znamená, že se v případě výpadku proudu nevypne, na rozdíl od mini PC.
- Možnost upgradu: barbony obecně umožňují přidat paměť nebo snadno vyměnit disk Hard.



Pro více informací o výběru vybavení doporučuji absolvovat tento kurz:



https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

### Doporučené vybavení



Není třeba kupovat nový stroj. Repasovaný počítač s níže uvedenými specifikacemi poskytne mnohem lepší výkon než jednodesková elektronika (například Raspberry Pi).



**Minimální specifikace:**




- Architektura X86-64 (64bitový procesor).
- dvoujádrový procesor s frekvencí 2 GHz nebo vyšší.
- minimálně 8 GB RAM.
- 2 TB nebo více NVMe SSD (pro uložení Blockchain Bitcoin a potřebných indexů).



**Doporučený operační systém: **




- Distribuce založená na Debianu, například Ubuntu 24.04 LTS.



**Doporučené vybavení:**




- HP EliteDesk / EliteBook
- Dell OptiPlex
- Lenovo ThinkCentre / ThinkPad
- Intel NUC
- atd.



Server Dojo je možné provozovat i na jiných hardwarových konfiguracích. Pro dosažení nejlepšího výkonu a omezení problémů však doporučujeme dodržovat výše uvedená doporučení.



V tomto návodu budu používat starý počítač ThinkCentre Tiny s dvoujádrovým procesorem Intel Pentium Dual-Core G4400T, 8 GB RAM a 2 TB SSD.



## 1 - Instalace Ubuntu



*Pokud chcete nainstalovat aplikaci Dojo do již nakonfigurovaného zařízení, můžete tento krok přeskočit a přejít přímo ke kroku 2.*



Po přípravě vybraného hardwaru je čas na instalaci operačního systému. Můžete použít prakticky jakoukoli distribuci Debianu, ale doporučuji zvolit LTS verzi Ubuntu, protože se pro naše účely dokonale hodí. Zde je uveden postup, který je třeba dodržet:



### 1.1. vytvořte bootovací klíč USB



Z již funkčního počítače (vašeho obvyklého počítače) stáhněte obraz ISO Ubuntu LTS [z oficiálních stránek](https://ubuntu.com/download/desktop) (`24.04` v době psaní tohoto článku, ale pokud je k dispozici jiný, vezměte nejnovější).



![Image](assets/fr/02.webp)



Vložte do tohoto počítače klíč USB o velikosti alespoň 8 GB a poté vytvořte bootovací klíč pomocí softwaru, jako je [Balena Etcher](https://etcher.balena.io/). Vyberte právě stažený obraz ISO Ubuntu, jako cílové zařízení vyberte klíč USB a poté spusťte proces vytváření (buďte trpěliví, může to trvat několik minut).



![Image](assets/fr/03.webp)



Vložte bootovací USB klíč do vypnutého počítače (toho, na kterém chcete spustit program Dojo). Spusťte počítač a ihned stiskněte **F12** nebo **F10** na klávesnici (v závislosti na modelu), abyste se dostali do spouštěcí nabídky. Poté zvolte klíč USB jako prioritní zařízení v pořadí spouštění počítače.



![Image](assets/fr/04.webp)



### 1.2. nainstalujte operační systém



Zobrazí se domovská obrazovka Ubuntu. Vyberte možnost "Vyzkoušet nebo nainstalovat Ubuntu*".



![Image](assets/fr/05.webp)



Poté postupujte podle klasického postupu instalace Ubuntu:




- Zvolte jazyk.
- Vyberte typ klávesnice.
- Pokud jste připojeni kabelem RJ45, není třeba konfigurovat Wi-Fi.
- Klikněte na "*Install Ubuntu*" a zaškrtněte možnost instalace softwaru třetích stran (ovladače Wi-Fi, multimediální kodeky atd.).
- Když se průvodce zeptá na typ instalace, vyberte možnost "*Vymazat disk a nainstalovat Ubuntu*". **Upozornění**: Tato operace zcela vymaže obsah disku. Pečlivě zkontrolujte, zda zvolený disk odpovídá disku NVMe SSD určenému pro Dojo.
- Vytvořte jednoduché uživatelské jméno (např. "*loic*").
- Přiřaďte počítači název (např. "*dojo-node*").
- Nastavte si silné heslo a udržujte ho v bezpečí.
- Pro posílení zabezpečení povolte možnost "*Při přihlášení si vyžádat heslo*".
- Uveďte své časové pásmo a klikněte na "*Install*".
- Počkejte na dokončení instalace. Po dokončení se systém automaticky restartuje.
- Při restartování počítače vyjměte instalační klíč USB.



Další podrobnosti o procesu instalace Ubuntu naleznete v našem specializovaném tutoriálu :



https://planb.network/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

### 1.3. aktualizace systému



Po prvním spuštění systému otevřete terminál pomocí kombinace kláves ***Ctrl + Alt + T*** a spusťte následující příkazy pro aktualizaci systému:



```bash
sudo apt update
sudo apt upgrade -y
```



![Image](assets/fr/06.webp)



## 2. Instalace přístavby



Aby program Dojo fungoval správně, musí být v systému přítomny určité softwarové cihly. Ty slouží ke správě softwarových úložišť, komunikaci, dekompresi archivů a spouštění aplikace Dojo uvnitř kontejnerů Docker. Všechny tyto operace se provádějí v terminálu.



### 2.1. Příprava



Následující příkaz vás vrátí do osobní složky. To je dobrý postup před spuštěním série instalací.



```bash
cd ~/
```



Před instalací jakéhokoli softwaru se ujistěte, že databáze softwaru dostupného v počítači je aktuální. Vyhnete se tak instalaci zastaralých verzí.



```bash
sudo apt-get update
```



![Image](assets/fr/07.webp)



### 2.2. instalace nástrojů



Do systému je třeba přidat několik nástrojů:




- `apt-transport-https`: umožňuje stahovat pakety bezpečně přes HTTPS
- `ca-certificates`: spravuje certifikáty potřebné pro šifrovaná připojení
- `curl`: načítání souborů z internetu
- `gnupg-agent`: pro správu klíčů GPG
- software-properties-common`: poskytuje nástroje pro manipulaci s repozitáři APT
- `unzip`: rozbalí soubory ve formátu ZIP



```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common unzip
```



Během instalace vás systém může požádat o potvrzení. Stiskněte klávesu "*y*" a poté stiskněte "*Enter*".



![Image](assets/fr/08.webp)



### 2.3. nainstalujte Torsocks



Torsocks umožňuje provádět určité příkazy prostřednictvím sítě Tor, což zvyšuje důvěrnost komunikace.



```bash
sudo apt install torsocks
```



![Image](assets/fr/09.webp)



### 2.4. nainstalujte Docker a Docker Compose



Služba Dojo běží v kontejnerech Docker. To znamená, že každá služba je izolována v nezávislém prostředí, což zjednodušuje údržbu a bezpečnost. K tomu je třeba nainstalovat Docker a nástroj Docker Compose, který umožňuje spravovat několik kontejnerů najednou.



#### Přidání podpisového klíče nástroje Docker



Docker poskytuje svůj vlastní digitální podpisový klíč. Jeho přidáním se ověřuje pravost stažených balíčků.



```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```



![Image](assets/fr/10.webp)



#### Přidán oficiální repozitář Docker



Dále je třeba systému sdělit, kde má najít oficiální balíčky Docker. Tento příkaz přidá do konfigurace správce balíčků nový repozitář.



```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "*$VERSION_CODENAME*") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```



![Image](assets/fr/11.webp)



#### Instalace nástrojů Docker a Docker Compose



Nyní lze nainstalovat hlavní součásti nástroje Docker.



```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```



![Image](assets/fr/12.webp)



#### Autorizace uživatele



Ve výchozím nastavení mohou aplikaci Docker spouštět pouze příkazy spuštěné s právy správce. Pro větší pohodlí doporučuji přidat aktuálního uživatele do skupiny "*docker*". To vám umožní používat Docker, aniž byste museli pokaždé zadávat `sudo`.



```bash
sudo usermod -aG docker $USER
```



![Image](assets/fr/13.webp)



## 3. Vytvoření jednoho uživatele (volitelné)



Pokud chcete zvýšit bezpečnost svého systému, doporučuji vytvořit samostatného uživatele výhradně pro spouštění programu Dojo. Tímto oddělením omezíte rizika: pokud se v systému Dojo vyskytne bezpečnostní problém, neohrozí přímo váš hlavní účet.



### 3.1. vytvoření uživatelského účtu



Následující příkaz vytvoří nového uživatele s názvem "*dojo*". Tento uživatel bude mít domovský adresář `/home/dojo` a přístup k terminálu bash. Bude také přidán do skupiny sudo, aby bylo možné provádět administrátorské příkazy.



```bash
sudo useradd -s /bin/bash -d /home/dojo -m -G sudo dojo
```



### 3.2. Nastavení hesla



Je důležité přiřadit tomuto účtu silné heslo. V ideálním případě byste měli použít správce hesel, jako je například Bitwarden, abyste mohli vytvořit dlouhou kombinaci Hard.



```bash
sudo passwd dojo
```



Systém vás následně vyzve k zadání zvoleného hesla a poté jej podruhé potvrdí.



https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

### 3.3. Oprávnění uživatele k používání nástroje Docker



Aby mohl uživatel "*dojo*" spouštět kontejnery potřebné ke spuštění nástroje Dojo, musí být přidán do skupiny Docker. Tím se vyhnete nutnosti zadávat před každý příkaz `sudo`.



```bash
sudo usermod -aG docker dojo
```



### 3.4. Restart systému



Aby se změny ve skupině projevily, je třeba počítač restartovat.



```bash
sudo reboot
```



### 3.5. Přihlášení s novým uživatelem



Po restartu systému se přihlaste pomocí přihlašovacího jména ***dojo*** a hesla, které jste definovali dříve. Všechny další kroky je nutné provádět z tohoto vyhrazeného účtu.



## 4. Stáhněte si a zkontrolujte Dojo



Před instalací aplikace Dojo je nutné se ujistit, že soubory pocházejí od oficiálního vývojáře a že nebyly upraveny. Tento krok se opírá o použití protokolu PGP a hashů k ověření pravosti a integrity souborů.



### 4.1. import klíče PGP vývojáře



Stáhněte si veřejný klíč vývojáře přes Tor a importujte jej do místního klíčenky. Tento klíč bude použit k ověření podpisů přidružených k souborům Dojo.



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/14.webp)



### 4.2. stáhněte si nejnovější verzi aplikace Dojo



Získání komprimovaného archivu obsahujícího zdrojový kód aplikace Dojo. V tomto příkladu je nejnovější verze `1.27.0`: upravte příkaz podle [nejnovější verze zde v oficiálním úložišti GitHub](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases).



```bash
torsocks wget -O samourai-dojo-1.27.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.27.0.zip
```



![Image](assets/fr/15.webp)



### 4.3. Stažení otisků prstů a podpisu



Vývojáři zveřejní soubor se seznamem digitálních otisků archivů a také soubor podepsaný jejich klíčem PGP. Stáhněte si je a porovnejte své soubory lokálně.



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt.sig
```



![Image](assets/fr/16.webp)



### 4.4. Kontrola podpisu PGP



Zkontrolujte, zda byl soubor otisků prstů podepsán importovaným klíčem.



```bash
gpg --verify samourai-dojo-1.27.0-fingerprints.txt.sig
```



Správný výsledek zobrazí platný podpis s klíčem `E53AD419B242822F19E23C6D3033D463D6E544F6` a přidruženým Address `dojocoder@pm.me`. Může se zobrazit varování, že klíč není certifikovaný: můžete jej ignorovat.



Pokud je naopak podpis neplatný, okamžitě zastavte proces instalace a začněte znovu od začátku.



![Image](assets/fr/17.webp)



### 4.5. Kontrola integrity archivu



Vypočítejte otisk SHA256 staženého souboru a poté otevřete soubor s otiskem a porovnejte obě hodnoty.



```bash
sha256sum samourai-dojo-1.27.0.zip
cat samourai-dojo-1.27.0-fingerprints.txt
```



Pokud jsou oba otisky totožné, můžete si být jisti, že archiv nebyl změněn. Pokud se liší, nepokračujte dále a soubory odstraňte.



![Image](assets/fr/18.webp)



### 4.6. Výpis a uspořádání souborů



Po úspěšném ověření můžete archiv rozbalit a připravit si složku určenou pro instalaci programu Dojo.



```bash
unzip samourai-dojo-1.27.0.zip -d .
mkdir ~/dojo-app
mv ~/samourai-dojo-1.27.0/* ~/dojo-app/
```



![Image](assets/fr/19.webp)



### 4.7. Vyčištění nepotřebných souborů



Odstraňte dočasné soubory a archivy, které již nepotřebujete, aby bylo prostředí čisté.



```bash
rm -r samourai-dojo-1.27.0 && rm samourai-dojo-1.27.0.zip && rm samourai-dojo-1.27.0-fingerprints.txt && rm samourai-dojo-1.27.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/20.webp)



## 5. Konfigurace Dojo



Dojo je backendový server, který sdružuje několik služeb pro interakci s vaším portfoliem a správu uzlu Bitcoin. Jeho konfigurace může být složitá, ale projekt nabízí zjednodušenou metodu, která automaticky instaluje a konfiguruje následující komponenty:




- Dojo (hlavní rozhraní API)
- Bitcoin core (kompletní uzel Bitcoin)
- BTC-RPC Explorer (web Block explorer)
- Fulcrum Indexer (rychlé indexování bloků a transakcí)
- Server Fulcrum Electrum dostupný v síti Tor
- Server Fulcrum Electrum dostupný v místní síti
- Administrativní pověření



### 5.1. pověření pro správu



Pro zabezpečení přístupu k různým službám je třeba zadat několik jedinečných identifikátorů generate:




- `BITCOIND_RPC_USER`
- `BITCOIND_RPC_PASSWORD`
- `MYSQL_ROOT_PASSWORD`
- mYSQL_USER
- `MYSQL_PASSWORD`
- nODE_API_KEY`
- `NODE_ADMIN_KEY`
- `NODE_JWT_SECRET`



Tyto identifikátory **musí být jedinečné** (to je velmi důležité: nesmíte používat stejné heslo pro několik služeb), složené výhradně z čísel, velkých a malých písmen (alfanumerické) a dlouhé přibližně 40 znaků, aby byla zaručena vysoká úroveň zabezpečení. Opět důrazně doporučuji používat správce hesel.



### 5.2. Přístup ke konfiguračním souborům



Konfigurační soubory aplikace Dojo jsou umístěny ve složce `conf/`. Přesuňte se do tohoto adresáře:



```bash
cd ~/dojo-app/docker/my-dojo/conf/
```



![Image](assets/fr/21.webp)



### 5.3. Konfigurace Bitcoin core



Otevřete konfigurační soubor Bitcoin core pomocí textového editoru nano:



```bash
nano docker-bitcoind.conf.tpl
```



![Image](assets/fr/22.webp)



V tomto souboru zadejte vygenerované identifikátory:



```
BITCOIND_RPC_USER=your-ID-here
BITCOIND_RPC_PASSWORD=your-password-here
```



⚠️ ***Nahraďte `všechny vaše ID-here` a `všechna vaše hesla-here` vlastními přihlašovacími údaji (se silným heslem).***



Pro zvýšení výkonu můžete také upravit velikost mezipaměti, kterou používá Bitcoin core (pokud máte k dispozici hodně paměti RAM, můžete jí použít i více):



```
BITCOIND_DB_CACHE=2048
```



Uložení změn a zavření editoru :




- stiskněte `Ctrl + X
- typ `y`
- pak stiskněte "*Enter*"



### 5.4. Konfigurace MySQL



Poté otevřete konfiguraci databáze MySQL:



```bash
nano docker-mysql.conf.tpl
```



Zadejte prosím své přihlašovací údaje:



```
MYSQL_ROOT_PASSWORD=your-password-here
MYSQL_USER=your-ID-here
MYSQL_PASSWORD=your-password-here
```



⚠️ ***Nahraďte `všechna vaše ID` a `všechna vaše hesla` vlastními přihlašovacími údaji (se silnými, jedinečnými hesly).***



Stejným způsobem uložte (`Ctrl + X`, `y`, "*Enter*").



![Image](assets/fr/23.webp)



### 5.5. Konfigurace indexeru Fulcrum



Otevřete následující soubor:



```bash
nano docker-indexer.conf.tpl
```



Přidání parametrů pro aktivaci nástroje Fulcrum a jeho správnou integraci do nástroje Dojo :



```
INDEXER_INSTALL=on
INDEXER_TYPE=fulcrum
INDEXER_BATCH_SUPPORT=active
INDEXER_EXTERNAL=on
```



![Image](assets/fr/24.webp)



Dále existují 2 možnosti v závislosti na vaší konfiguraci. Pokud je program Dojo nainstalován na počítači odděleném od vašeho běžného počítače (na vyhrazeném počítači, serveru...), zadejte jeho IP adresu Address v místní síti, například :



```
INDEXER_EXTERNAL_IP=192.168.1.157
```



![Image](assets/fr/25.webp)



Chcete-li zjistit místní adresu IP Address svého počítače, otevřete jiný terminál a zadejte následující příkaz:



```bash
hostname -I
```



Druhá možnost: pokud je Dojo spuštěno přímo na vašem běžném osobním počítači, ponechte výchozí hodnotu, která je již uvedena v konfiguračním souboru :



```
INDEXER_EXTERNAL_IP=127.0.0.1
```



Uložte a ukončete editor (`Ctrl + X`, `y`, "*Enter*").



### 5.6. Konfigurace služby uzlu



Nakonec otevřete konfiguraci hlavní služby Dojo:



```bash
nano docker-node.conf.tpl
```



Zadejte prosím své přihlašovací údaje:



```
NODE_API_KEY=your-password-here
NODE_ADMIN_KEY=your-password-here
NODE_JWT_SECRET=your-password-here
```



⚠️ ***Nahraďte `vaše-heslo-tu` vlastními přihlašovacími údaji (se silnými, jedinečnými hesly).***



![Image](assets/fr/26.webp)



Poté aktivujte místní indexer:



```
NODE_ACTIVE_INDEXER=local_indexer
```



Uložte a ukončete editor (`Ctrl + X`, `y`, "*Enter*").



### 5.7. Správa přihlášení



Po dokončení konfigurace není nutné ukládat všechny vygenerované identifikátory. Jediný, který je bezpodmínečně nutné uložit, je :



```
NODE_ADMIN_KEY
```



Toto přihlášení vám umožní přihlásit se později do nástroje pro údržbu Dojo. Všechna ostatní přihlášení lze odstranit ze správce hesel nebo z ručně psaných poznámek. Zůstanou přístupná z konfiguračních souborů aplikace Dojo, pokud byste je v budoucnu potřebovali získat zpět.



## 6. Instalace zařízení Dojo



V této fázi se na vašem počítači nainstaluje a spustí program Dojo. Operace spustí několik služeb (Bitcoin core, indexer Fulcrum, backend Dojo atd.) a zahájí úplnou synchronizaci Blockchain Bitcoin. To může trvat několik dní v závislosti na vašem hardwaru a internetovém připojení.



### 6.1. Zkontrolujte, zda Docker funguje správně



Před zahájením instalace se ujistěte, že je Docker funkční. Spusťte následující příkaz:



```bash
docker run hello-world
```



Tento příkaz stáhne a spustí malý testovací kontejner. Pokud vše funguje správně, měla by se zobrazit zpráva podobná :



```
Hello from Docker!
This message shows that your installation appears to be working correctly...
```



![Image](assets/fr/27.webp)



Pokud se tato zpráva nezobrazí, začněte restartováním počítače pomocí příkazu :



```bash
sudo reboot
```



Poté se znovu přihlaste ke svému účtu **dojo** a znovu spusťte testovací příkaz. Pokud chyba přetrvává, nebyl Docker nainstalován správně. V takovém případě se vraťte ke kroku `2.4.` o instalaci nástroje Docker a pečlivě zkontrolujte jednotlivé příkazy.



### 6.2. Přejděte do instalačního adresáře Dojo



Skripty potřebné k instalaci jsou umístěny ve složce `my-dojo`. Přesuňte se do tohoto adresáře:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/28.webp)



Pomocí příkazu `ls` zkontrolujte, zda je soubor `dojo.sh` přítomen. To je hlavní skript, který automatizuje instalaci aplikace Dojo a spouštění všech jejích služeb.



![Image](assets/fr/29.webp)



### 6.3. Spusťte instalaci



Instalaci zahájíte spuštěním příkazu :



```bash
./dojo.sh install
```



Instalaci potvrďte stisknutím tlačítka `y` a poté "*Enter*".



![Image](assets/fr/30.webp)



Tento skript bude :




- stáhnout a spustit potřebné kontejnery Docker,
- inicializovat Bitcoin core a zahájit synchronizaci Blockchain,
- spustit indexer Fulcrum a sledovat transakce a adresy,
- aktivovat backend Dojo a jeho rozhraní API.



Uvidíte neustálý proud protokolů s barevnými odkazy jako `bitcoind`, `soroban`, `nodejs` nebo `fulcrum`. Toto rolování znamená, že systém Dojo je spuštěn a začíná vykonávat různé služby.



![Image](assets/fr/31.webp)



### 6.4. Ukončení zobrazení protokolu



Protokoly se v terminálu zobrazují v reálném čase. Chcete-li se vrátit do příkazového řádku, když je program Dojo spuštěn na pozadí, zadejte příkaz :



```
Ctrl + C
```



Nemějte obavy: zastavení zobrazování protokolu neznamená zastavení služeb. Docker pokračuje v běhu služby Dojo na pozadí (pokud chcete, aby IBD pokračoval, nemusíte samozřejmě počítač zastavovat).



### 6.5. Porozumění *Initial Block Download* (IBD)



Při spuštění musí Bitcoin core stáhnout a ověřit celý Blockchain od roku 2009. Tento krok se nazývá ***Initial Block Download* (IBD)**. Je nezbytný, protože umožňuje uzlu Dojo nezávisle ověřit každý blok a transakci Bitcoin.



Doba trvání této synchronizace závisí na několika faktorech:




- výkon procesoru a množství dostupné paměti RAM,
- rychlost disku,
- počet a kvalitu vrstevníků, ke kterým se váš uzel připojuje,
- rychlost vašeho internetového připojení.



V praxi tato operace obvykle trvá **2 až 7 dní**. Během této doby můžete nechat stroj nepřetržitě v provozu. Čím déle je počítač zapnutý, tím rychleji bude synchronizace dokončena. Doporučuji pravidelně kontrolovat stav synchronizace nahlížením do protokolů Bitcoin core nebo pomocí nástroje pro údržbu Dojo po jeho instalaci (viz následující část).



Chcete-li prohloubit své znalosti o IBD a obecněji o fungování a úloze uzlu Bitcoin, doporučuji vám podívat se na tento kurz:



https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426


## 7. Sledování synchronizace



Při první instalaci programu Dojo je třeba počkat na úplné dokončení dvou hlavních operací: kompletní stažení Blockchain Bitcoin (*IBD*) a indexování tohoto Blockchain společností Fulcrum. V závislosti na vašem připojení a výkonu počítače to může trvat několik dní. Během této doby můžete sledovat průběh procesu, abyste se ujistili, že vše probíhá hladce.



Stav synchronizace lze sledovat dvěma způsoby:




- použití nástroje Dojo Maintenance Tool (DMT), který je jednoduchý, ale poskytuje jen málo podrobností během IBD;
- přímé nahlížení do protokolů Dojo na vašem počítači, což je technicky náročnější, ale mnohem přesnější.



### 7.1. Kontrola prostřednictvím nástroje Dojo Maintenance Tool (DMT)



Nástroj Dojo Maintenance Tool je zabezpečený webový nástroj Interface, který umožňuje sledovat stav zařízení a provádět určité operace. Je to nejjednodušší a nejdostupnější způsob, jak sledovat průběh IBD. Během počáteční fáze synchronizace mohou být zobrazované informace omezené. DMT například nezobrazuje podrobný průběh indexace Fulcrum. Na druhou stranu, jakmile je synchronizace dokončena, DMT přehledně zobrazí :




- všechna světla na Green;
- poslední ověřený blok pro každou službu (Node, Indexer, Dojo DB).



Pro přístup k němu musíte znát adresu URL svého DMT a připojit se k němu [prostřednictvím prohlížeče Tor](https://www.torproject.org/download/). Za tímto účelem otevřete terminál a přejděte do adresáře `/my-dojo`:



```bash
cd ~/dojo-app/docker/my-dojo
```



Poté spusťte následující příkaz:



```bash
./dojo.sh onion
```



![Image](assets/fr/32.webp)



Poté budete mít přístup ke všem informacím o připojeních k vašemu zařízení Dojo přes Tor. Nás zde zajímá následující adresa URL:



```
Dojo API and Maintenance Tool =
```



Chcete-li získat přístup k DMT z libovolného počítače v libovolné síti (i vzdáleně), otevřete prohlížeč Tor Browser a zadejte tuto adresu URL následovanou slovy `/admin`. Pokud je například vaše adresa URL `wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion`, musíte ji zadat do panelu [Tor Browser](https://www.torproject.org/download/):



```
wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion/admin
```



⚠️ **Prosíme, zachovejte důvěrnost tohoto dokumentu Address



Poté budete přesměrováni na ověřovací stránku. DMT se přihlásí pomocí hesla `NODE_ADMIN_KEY`, které jste vygenerovali dříve.



![Image](assets/fr/33.webp)



Po přihlášení máte přístup k nástroji *Dojo Maintenance Tool*! Během IBD můžete v nabídce "*Full node*" zobrazit informace o "*Nejnovějším bloku*", které vás informují o aktuálním stavu vašeho uzlu Bitcoin.



![Image](assets/fr/34.webp)



Nezapomeňte si tuto stránku Address přidat do záložek v prohlížeči Tor Browser, abyste ji mohli později snadno vyhledat.



Po úplné synchronizaci programu Dojo byste měli na všech ukazatelích na domovské stránce DMT vidět zaškrtnutí Green ✅.



### 7.2. Ověření prostřednictvím protokolů Dojo



Druhým způsobem, jak sledovat průběh IBD, je nahlédnout přímo do protokolů počítače. Tento přístup nabízí mnohem přesnější sledování v reálném čase. Můžete vidět, jak Bitcoin core postupuje při stahování bloků a jak je Fulcrum indexuje.



Připojte se k počítači, který je hostitelem vašeho programu Dojo, a otevřete terminál. Všechny příkazy by se měly spouštět z adresáře `my-dojo`. Umístěte se do tohoto adresáře:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/35.webp)



#### Protokoly Bitcoin core



Zobrazte protokoly Bitcoin core a sledujte průběh IBD:



```bash
./dojo.sh logs bitcoind
```



Na začátku se zobrazí fáze před synchronizací hlaviček bloků:



```
bitcoind | Pre-synchronizing blockheader, height : NNNNNN
```



Jakmile tato hodnota dosáhne 100 %, zahájí Bitcoin core kompletní stahování Blockchain. Uvidíte průběh IBD. Chcete-li zjistit aktuální výšku bloku, podívejte se na hodnotu označenou `height=`. Můžete také sledovat klíč `progress=`, který udává procentuální průběh IBD.



![Image](assets/fr/36.webp)



Chcete-li zavřít protokoly a vrátit se do příkazového řádku, použijte jako vždy kombinaci kláves `Ctrl + C`.



#### Deníky Fulcrum



Jakmile modul Bitcoin core dokončí předsynchronizaci záhlaví, začne společnost Fulcrum indexovat modul Blockchain za chodu. Prohlédněte si jeho protokoly pomocí :



```bash
./dojo.sh logs fulcrum
```



Poté se zobrazí výška posledního indexovaného bloku, která je uvedena za slovem `height:`, a také procento postupu indexování.



![Image](assets/fr/37.webp)



### 7.3. Poškození databáze Fulcrum



Fulcrum je mimořádně výkonný indexer, ale jeho instalace může být složitá, v neposlední řadě i kvůli jemné správě databáze. V případě výpadku proudu nebo náhlého vypnutí stroje během počáteční synchronizace může dojít k poškození databáze indexeru. O tom se můžete přesvědčit například v případě následujících záznamů:



```bash
fulcrum | The database has been corrupted etc...
```



**Poznámka:** Tento typ chyby by měl být opraven v nadcházející verzi softwaru Fulcrum 2.0.



Pokud se vám to stane, nebude to mít žádný dopad na bitcoind (váš uzel Bitcoin): jeho IBD bude pokračovat nezávisle na Fulcrum. Nebudete však moci používat Fulcrum, dokud nesmažete jeho poškozená data a znovu nespustíte jeho synchronizaci od začátku. Funguje to následovně:



Stop Dojo:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Odstraňte pouze kontejner a svazek Fulcrum:



```bash
docker rm -f fulcrum || true
docker volume ls | grep -i fulcrum
docker volume rm my-dojo_data-fulcrum
```



Obvykle je název `my-dojo_data-fulcrum`, pokud to není váš případ, upravte název vrácený předchozím příkazem.



Pak znovu spusťte Dojo a obnovte Fulcrum od nuly:



```bash
./dojo.sh upgrade
```



Poté můžete zkontrolovat, zda Fulcrum pracuje správně, a to pomocí protokolů:



```bash
docker logs -f fulcrum
```




## 8. Použití nástroje Dojo Maintenance Tool



Jakmile je váš uzel Bitcoin synchronizován s osnovní hlavou s většinou Proof of Work a Blockchain je 100% indexován společností Fulcrum, můžete začít používat svůj Dojo.



Aplikace Dojo nabízí širokou škálu funkcí, které jsou pravidelně vylepšovány s každou novou verzí. Podle mého názoru jsou 2 nejdůležitější :




- možnost připojit Ashigaru Wallet a používat vlastní uzel pro konzultaci dat Blockchain a vysílání transakcí,
- a Block explorer, který vám umožní přístup k informacím o Blockchain Bitcoin, aniž byste svá data vystavili externí instanci, kterou nemáte pod kontrolou.



Zjistěte, jak je používat.


### 8.1. Připojte Ashigaru k vašemu Dojo



Připojení Ashigaru Wallet k vašemu zařízení Dojo je velmi jednoduché: po zapnutí DMT otevřete nabídku "*Párování*". Zobrazí se QR kód, který můžete naskenovat přímo pomocí aplikace Ashigaru.



![Image](assets/fr/38.webp)



Při prvním spuštění aplikace Ashigaru po vytvoření nebo obnovení Wallet budete přesměrováni na stránku "*Konfigurace serveru Dojo*". Stiskněte tlačítko "*Scan QR*" a poté naskenujte QR kód zobrazený na vašem DMT.



![Image](assets/fr/39.webp)



Poté klikněte na tlačítko "*Pokračovat*".



![Image](assets/fr/40.webp)



Nyní jste připojeni ke svému Dojo.



![Image](assets/fr/41.webp)



### 8.2. Používání Block explorer



Aplikace Dojo automaticky nainstaluje uzel Block explorer, [BTC-RPC Explorer](https://github.com/janoside/btc-RPC-explorer), který čerpá data přímo z vašeho vlastního uzlu Bitcoin. Průzkumník vám umožňuje přístup k nezpracovaným informacím z Blockchain a vašeho Mempool prostřednictvím snadno pochopitelného webu Interface. Můžete tak například snadno zkontrolovat stav probíhající transakce, zobrazit zůstatek na Address nebo prozkoumat složení bloku.



Chcete-li k němu přistupovat, jednoduše si v prohlížeči stáhněte Tor Address. Za tímto účelem spusťte stejný příkaz, který jste použili k získání Address vašeho DMT:



```bash
./dojo.sh onion
```



![Image](assets/fr/42.webp)



Ke všem informacím o připojení k službě Dojo budete mít přístup prostřednictvím sítě Tor. Nás zde zajímá následující adresa URL:



```
Block Explorer =
```



Pokud jste již připojeni k DMT, najdete tento modul Address také v nabídce "*Párování*" uvnitř JSON připojení:



![Image](assets/fr/43.webp)



Chcete-li přistupovat k prohlížeči z libovolného počítače v libovolné síti (i vzdáleně), otevřete [Tor Browser](https://www.torproject.org/download/) a zadejte právě získanou adresu URL.



⚠️ **Prosíme, zachovejte důvěrnost tohoto Address



Pak budete mít přístup k vlastnímu zařízení Block explorer.



![Image](assets/fr/44.webp)



*Obrázek: https://ashigaru.rs/.*



Chcete-li sledovat transakci, jednoduše zadejte její číslo txid do vyhledávacího řádku vpravo nahoře.



![Image](assets/fr/45.webp)



*Obrázek: https://ashigaru.rs/.*



Chcete-li zkontrolovat pohyby spojené s modelem Address, postupujte stejným způsobem, když do vyhledávacího řádku zadáte Address.



![Image](assets/fr/46.webp)



*Obrázek: https://ashigaru.rs/.*



Do vyhledávacího řádku můžete zadat také číslo Hash nebo výšku bloku a zobrazit podrobnosti.



![Image](assets/fr/47.webp)



*Obrázek: https://ashigaru.rs/.*



## 9. Údržba dódžó



### 9.1 Zastavte své Dojo



Nikdy náhle nepřerušujte napájení systému Dojo, protože by mohlo dojít k poškození některých databází, zejména indexeru Fulcrum. Pokud jej musíte vypnout, vždy proveďte čisté vypnutí programu Dojo a po dokončení všech procedur vypněte i počítač:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



### 9.2 Aktualizujte své Dojo



Aplikace Dojo se pravidelně vyvíjí a jsou vydávány nové verze, které opravují chyby, zlepšují stabilitu a přidávají funkce. Proto je důležité [pravidelně kontrolovat aktualizace](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) a aktualizovat své Dojo. Tento proces je podobný počáteční instalaci, ale vyžaduje nahrazení některých souborů nejnovější dostupnou verzí při zachování vaší konfigurace. Zde jsou uvedeny podrobné kroky, které je třeba dodržet pro čistou a bezpečnou aktualizaci:



Chcete-li zjistit aktuální verzi svého programu Dojo, spusťte příkaz :



```bash
./dojo.sh version
```



Ačkoli je tento krok nepovinný, doporučuji začít aktualizací operačního systému. Snížíte tím riziko nekompatibility a zajistíte, že závislosti používané systémem Dojo budou aktuální:



```bash
sudo apt-get update
sudo apt-get upgrade
```



Přejděte do adresáře Dojo a zastavte aktuální služby:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Poté restartujte systém, abyste získali čistý štít:



```bash
sudo reboot
```



Aplikace Dojo se dodává s digitálně podepsanými soubory. Tyto podpisy PGP zaručují, že soubory pocházejí od vývojáře a nebyly nijak upraveny. Je důležité je kontrolovat při každé aktualizaci aplikace Dojo, stejně jako při její první instalaci. Začněte stažením veřejného klíče vývojáře přes Tor a poté jej importujte :



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



Vraťte se do osobního adresáře:



```bash
cd ~/
```



Stáhněte si nejnovější verzi nástroje Dojo ze serveru GitHub prostřednictvím služby Tor. V tomto příkladu je to verze `1.28.0` (která v době psaní tohoto článku ještě neexistovala: to je jen příklad). Nezapomeňte nahradit soubor a odkaz [verzí, kterou chcete nainstalovat](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases):



```bash
torsocks wget -O samourai-dojo-1.28.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.28.0.zip
```



Stáhněte také soubor obsahující otisky prstů a podpis PGP (opět nezapomeňte v příkazu upravit verzi):



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt.sig
```



Zkontrolujte, zda byl stažený soubor otisku prstu podepsán klíčem vývojáře:



```bash
gpg --verify samourai-dojo-1.28.0-fingerprints.txt.sig
```



Správný výsledek by se měl zobrazit :



```
gpg: Signature made [date + time]
gpg: using EDDSA key E53AD419B242822F19E23C6D3033D463D6E544F6
gpg: Good signature from "dojocoder@pm.me" <dojocoder@pm.me> [unknown]
```



Může se objevit upozornění, že klíč není certifikovaný, ale to není důležité. Pokud je naopak podpis neplatný nebo odpovídá jinému klíči, nepokračujte dále a začněte znovu a zkontrolujte odkazy.



Poté vypočítejte otisk SHA256 archivu a porovnejte jej s oficiálním souborem otisků:



```bash
sha256sum samourai-dojo-1.28.0.zip
cat samourai-dojo-1.28.0-fingerprints.txt
```



Pokud se oba otisky dokonale shodují, je archiv pravý a neporušený. Pokud se liší, soubory okamžitě odstraňte a nepokračujte v práci.



Rozbalte archiv v domovském adresáři:



```bash
unzip samourai-dojo-1.28.0.zip -d .
```



Poté zkopírujte obsah do adresáře Dojo a přepište starý adresář :



```bash
cp -a samourai-dojo-1.28.0/. dojo-app/
```



Tato operace zachová konfigurační soubory umístěné v adresáři `~/dojo-app/docker/my-dojo/conf`, ale nahradí všechny ostatní soubory aktualizovanými verzemi.



Chcete-li udržet prostředí čisté, odstraňte nepotřebné soubory :



```bash
rm -r samourai-dojo-1.28.0 && rm samourai-dojo-1.28.0.zip && rm samourai-dojo-1.28.0-fingerprints.txt && rm samourai-dojo-1.28.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



Vraťte se do adresáře skriptů Dojo a spusťte příkaz update:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh upgrade -y
```



Tento příkaz dá nástroji Docker pokyn k obnovení obrazů s novými soubory a poté automaticky restartuje všechny služby. Na konci procesu zkontrolujte protokoly a ujistěte se, že Bitcoin core, Fulcrum a Dojo fungují správně:



```bash
./dojo.sh logs bitcoind
./dojo.sh logs fulcrum
```



Pokud se služby spustí bez chyby a v protokolech se zobrazí zpracovávané bloky, je vaše Dojo nyní aktuální a funkční.