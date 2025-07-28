---
name: Lynis
description: Provedení bezpečnostního auditu počítače se systémem Linux pomocí aplikace Lynis
---
![cover](assets/cover.webp)



___



*Tento návod vychází z původního obsahu, který Fares CHELLOUG zveřejnil na stránkách [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). V původním textu mohly být provedeny změny.*



___



## I. Prezentace



**V tomto tutoriálu se naučíme provádět bezpečnostní audit na počítači se systémem Linux pomocí programu Lynis! Pro ty z vás, kteří neznáte **Lynis**, je to malý nástroj příkazového řádku, který analyzuje konfiguraci vašeho serveru a vydá doporučení pro **zlepšení zabezpečení vašeho počítače**



Lynis je open source nástroj od společnosti CISOFY, která se specializuje na **auditování a zpevňování systémů**. Pokud chcete pokročit v oblasti hardeningu Linuxu a populárních služeb (SSH, Apache2 atd.), Lynis je vaším spojencem! Lynis vám nejen řekne, co je špatně, ale také vám poskytne doporučení, která vás nasměrují správným směrem (a ušetří vám čas).



**Lynis** funguje s většinou distribucí Linuxu, včetně: **Debian, FreeBSD, HP-UX, NetBSD, NixOS, OpenBSD, Solaris**. Lynis je určen pro uživatele Linuxu / UNIXu, ale je kompatibilní i s **macOS**. Velmi rychle se instaluje, na úrovni balíčků není žádná správa závislostí.



Používá se k různým účelům:





- Bezpečnostní audity
- Testování shody (PCI, HIPAA a SOX)
- Náročnější konfigurace systému
- Detekce zranitelnosti



Nástroj je široce využíván širokou škálou uživatelů, včetně správců systémů, IT auditorů a pentesterů. Pro analýzy je nástroj založen na standardech, jako jsou **CIS Benchmark, NIST, NSA, OpenSCAP**, a na oficiálních doporučeních **Debian, Gentoo, Red Hat**.



Projekt je k dispozici na této adrese Address na **Githubu** :





- [GitHub - Lynis](https://github.com/CISOfy/lynis)
- [Stáhnout Lynis z CISOFY](https://cisofy.com/lynis/#download)



V tomto návodu krok za krokem **použiji VPS s Debianem 12** a zaměřím se na část SSH, protože bych rád zkontroloval jeho konfiguraci a vylepšil ji.



## II. Stažení a instalace



Lynis lze stáhnout a nainstalovat několika způsoby. Vyberte si z níže uvedeného seznamu ten, který vám vyhovuje.



### A. Instalace z repozitářů Debianu



Tento režim instalace umožňuje použít příkaz **lynis** odkudkoli ze systému, na rozdíl od instalace ze zdrojového kódu, kde se musíte nacházet v daném adresáři.



Připojte se k serveru přes SSH a zadejte následující příkazy pro instalaci Lynis :



```
sudo apt-get update
sudo apt-get install lynis -y
```



Tohle dostanete:



![Image](assets/fr/024.webp)



### B. Stáhněte si z oficiálních webových stránek



Můžete si ji také stáhnout z webových stránek Cisofy:



```
sudo wget https://downloads.cisofy.com/lynis/lynis-3.0.9.tar.gz
```



Tohle dostanete:



![Image](assets/fr/032.webp)



Poté archiv rozbalíme pomocí následujícího příkazu:



```
sudo tar -zxf lynis-3.0.9.tar.gz
```



Tohle dostanete:



![Image](assets/fr/020.webp)



Přesuňme se do složky **lynis**:



```
cd lynis
```



Aktualizace můžeme zkontrolovat pomocí následujícího příkazu:



```
./lynis update info
```



Tohle dostanete:



![Image](assets/fr/023.webp)



### C. Stáhnout z GitHubu



Stáhneme si **Lynis** z oficiálního repozitáře GitHub pomocí následujícího příkazu (v počítači musí být přítomen *git*):



```
git clone https://github.com/CISOfy/lynis.git
```



Tohle dostanete:



![Image](assets/fr/060.webp)



## III. Používání systému Lynis



Lynis je na našem počítači přítomen, tak se ho naučme používat!



### A. Hlavní ovládací prvky a možnosti



Chcete-li zobrazit dostupné příkazy, stačí zadat následující příkaz:



```
sudo lynis
# Si vous avez récupéré Lynis depuis les sources, utilisez cette syntaxe :
./lynis
```



Tohle dostanete:



![Image](assets/fr/039.webp)



K dispozici jsou také následující možnosti:



![Image](assets/fr/040.webp)



Chcete-li zobrazit všechny dostupné příkazy, zadejte následující příkaz:



```
sudo lynis show
```



Tohle dostanete:



![Image](assets/fr/022.webp)



Pokud chcete zobrazit všechny možnosti, musíte zadat :



```
sudo lynis show options
```



Tohle dostanete:



![Image](assets/fr/021.webp)



Ve zbytku tohoto článku se dozvíte, jak používat některé možnosti.



### B. Provedení auditu systému



Požádáme společnost **Lynis**, aby provedla audit našeho systému a upozornila na to, co je správně nakonfigurováno a co by se dalo zlepšit. Za tímto účelem zadejte následující příkaz:



```
sudo lynis audit system
# ou
./lynis audit system
```



Pokud nejste při spuštění tohoto příkazu přihlášeni jako root, spustí se nástroj ve výchozím nastavení s právy aktuálně přihlášeného uživatele. Některé testy se v tomto kontextu nespustí:



![Image](assets/fr/052.webp)



Zde jsou uvedeny testy, které se v tomto režimu neprovádějí:



![Image](assets/fr/051.webp)



Po provedení příkazu se spustí analýza. Stačí chvíli počkat.



Na konci auditu se zobrazí toto (vidíme, že **Lynis** správně identifikoval systém **Debian 12** a pro analýzu použije zásuvný modul **Debian**):



![Image](assets/fr/017.webp)



Dále Lynis uvede soubor bodů, které odpovídají všemu, co v našem systému zkontroloval. Ten je uspořádán podle kategorií, jak ještě uvidíme. Za zmínku také stojí, že k zvýraznění doporučení se používá barevný kód:





- Červená** pro nedodržení kritických bodů Elements nebo osvědčených postupů (například chybějící balíček), tj. váš server tento bod nedodržuje
- Žlutá** pro návrhy nebo částečné splnění doporučení (řekněme, že splnění bodu zvýrazněného touto barvou je plus (není prioritní))
- Green** pro body, kde je konfigurace vašeho serveru v souladu s předpisy
- Bílá**, když je neutrální



Zde vidíme, že Lynis doporučuje nainstalovat **fail2ban**:



![Image](assets/fr/057.webp)



V části "**Boot a služby**" vidíme, že by bylo možné zlepšit ochranu služeb prostřednictvím *systemd*. Pozitivní je, že Grub2 je přítomen a nejsou žádné problémy s oprávněními na :



![Image](assets/fr/029.webp)



Dále máte sekce "**Jádro**" a "**Paměť a procesy**":



![Image](assets/fr/037.webp)



Dále následuje část "**Uživatelé, skupiny a ověřování**". Nástroj nás informuje o varování ohledně oprávnění adresáře "**/etc/sudoers.d**". Prozatím nevíme více, ale na konci analýzy se budeme moci podívat, jaké je doporučení.



![Image](assets/fr/049.webp)



Zde najdete informace v sekcích "**Schránky", "Souborové systémy" a "Zařízení USB "**. Mimo jiné vidíme, že existují návrhy přípojných bodů a že zařízení USB jsou v tomto počítači aktuálně povolena.



![Image](assets/fr/048.webp)



Dále sekce: "Zde je uvedeno, že již nepoužívané balíčky mohou být vyčištěny a že neexistuje žádný nástroj, který by spravoval automatické aktualizace.



![Image](assets/fr/058.webp)



Vidíme, že je aktivován firewall (a ano, je zde iptables!). Dále vidíme, že našel nepoužívaná pravidla a že je nainstalován webový server Apache.



![Image](assets/fr/055.webp)



Poté následuje analýza samotného webového serveru, protože služba byla identifikována.



Vidíme, že našel konfigurační soubory **Nginx** a že v části SSL/TLS jsou nakonfigurovány **šifry** s použitím protokolu, který by byl nezabezpečený. Na druhou stranu je podle Lynisu správa protokolů správná.



![Image](assets/fr/038.webp)



Služba SSH je na mém serveru VPS k dispozici. Její konfiguraci analyzuje Lynis. Je třeba říci, že zabezpečení SSH lze snadno zlepšit! K této oblasti se podrobně vrátíme, jakmile získáme doporučení.



![Image](assets/fr/026.webp)



Zde jsou sekce **"Podpora SNMP", "Databáze", "PHP", "Podpora Squid", "Služby LDAP", "Protokolování a soubory "**.



V souvislosti se správou protokolů je důležité jedno doporučení: důrazně doporučujeme, abyste protokoly neukládali pouze lokálně v počítači. Pokud by stroj poškodil útočník, je pravděpodobné, že se pokusí své stopy vymazat... Proto je třeba protokoly externalizovat.



![Image](assets/fr/050.webp)



Zde máme audit zranitelných služeb, správy účtů, naplánovaných úloh a synchronizace NTP.Na banneru a identifikační části je uvedeno, že úroveň je nízká: to je pochopitelné, pokud zobrazíte verzi systému, dává to potenciálnímu útočníkovi indicii. Jedná se o výchozí nastavení.



Bylo by zajímavé aktivovat **auditd**, abyste měli logy pro případ **forenzní** analýzy. Kontroluje se také **NTP**, protože pro efektivní prohledávání logů je výhodné mít systémy včas, což zjednodušuje vyhledávání.



![Image](assets/fr/036.webp)



Lynis se dále věnuje kryptografickému systému Elements, virtualizaci, kontejnerům a bezpečnostním rámcům. Některé části jsou prázdné, protože neodpovídají analyzovanému stroji. Vidíme však, že mám dva prošlé certifikáty SSL a nemám aktivovaný **SELinux**.



![Image](assets/fr/027.webp)



I zde je prostor pro zlepšení: není k dispozici antivirový ani antimalwarový skener a máme návrhy na oprávnění k souborům.



![Image](assets/fr/028.webp)



Dále se Lynis zaměřuje na zpřísnění konfigurace linuxového jádra (včetně pravidel pro zásobník IPv4) a na správu domovských adresářů linuxového počítače.



![Image](assets/fr/035.webp)



Dostali jsme se na konec analýzy... Z tohoto posledního bodu vyplývá, že bychom měli z přítomnosti ClamAV na tomto počítači vše.



![Image](assets/fr/030.webp)



## IV. Doporučení



Po auditu je čas na přečtení a analýzu doporučení. Zde získáme doporučení a vysvětlení ke každému z testů provedených společností Lynis.



Vezměme si například doporučení SSH. ** U každého doporučení najdete doporučený parametr a odkaz, který vysvětlí bezpečnostní bod ** Je na vás, abyste se rozhodli v závislosti na kontextu a způsobu použití.



Podívejme se na několik příkladů doporučení, která přímo odrážejí body zdůrazněné v celém auditu...



### A. Příklady doporučení





- Jak jsme viděli dříve, protokol NTP je důležitý pro časové razítkování protokolů:



![Image](assets/fr/043.webp)





- Společnost Lynis také doporučuje nainstalovat balíček **apt-listbugs**, který umožňuje získat informace o kritických chybách při instalaci balíčků prostřednictvím **apt.**



![Image](assets/fr/041.webp)





- Nástroj navrhuje nainstalovat **needrestart, aby bylo možné** zjistit, které procesy používají starou verzi knihovny a je třeba je restartovat.



![Image](assets/fr/054.webp)





- Tento návrh navrhuje nainstalovat **fail2ban** pro automatické blokování hostitelů, kterým se nepodaří ověřit pravost (zejména hrubou silou).



![Image](assets/fr/044.webp)





- Pro posílení systémových služeb doporučuje spustit modrý příkaz pro každou službu v počítači.



![Image](assets/fr/056.webp)





- Doporučuje nastavit datum vypršení platnosti všech hesel chráněných účtů.



![Image](assets/fr/031.webp)





- Tento návrh navrhuje nastavit minimální a maximální hodnotu stáří hesla. Tím se mimo jiné zajistí, že hesla budou pravidelně měněna.



![Image](assets/fr/042.webp)





- Doporučujeme používat oddělené oddíly, aby se omezil dopad problémů s místem na disku na jednom oddílu.



![Image](assets/fr/047.webp)





- Toto doporučení navrhuje vypnout úložiště USB a rozhraní firewire, aby se zabránilo úniku dat



![Image](assets/fr/033.webp)





- Chcete-li splnit toto doporučení, jednoduše nainstalujte a nakonfigurujte například **unnatended-upgrade**.



![Image](assets/fr/053.webp)



### B. Instalace doporučených balíčků



Pro zlepšení konfigurace systému nainstalujeme do počítače několik balíčků: některé doporučil Lynis, některé doporučuji já osobně.



Pokud věnujete trochu času jejich konfiguraci, získáte dobrý základ pro práci. K tomu vám poslouží stránky IT-Connect, další články na webu a dokumentace k nástrojům.



```
sudo apt-get install debsums apt-listbugs needrestart apt-show-versions fail2ban unattended-upgrades clamav clamav-daemon rkhunter
```



Některé informace o nainstalovaných balíčcích :





- Clamav** je antivirový program.
- unattend-upgrades** vám umožní spravovat aktualizace automaticky a dokonce restartovat počítač nebo automaticky vyčistit staré balíčky, je plně konfigurovatelný.
- rkhunter** je antirootkit, který skenuje souborový systém.
- Fail2ban** bude vycházet z vašich souborů protokolu podle toho, co mu dáte ke čtení, a bude spolupracovat s **iptables**, například aby zakázal IP adresy, které se pokusí "hrubou silou" vynutit váš server v SSH.



### C. Doporučení pro SSH



Podívejme se na doporučení SSH. Jsou uvedeny níže. Nebojte se, hned si vysvětlíme, jak konfiguraci vylepšit.



![Image](assets/fr/034.webp)



Podívejme se blíže na mou aktuální konfiguraci **SSH** v :**/etc/ssh/sshd_config**



![Image](assets/fr/018.webp)



Níže navrženou konfiguraci lze ještě optimalizovat, ale poskytuje dobrý základ. *Všimněte si, že jsem pro větší srozumitelnost* odstranil řadu komentářů.



Budeme :





- Změna portu připojení SSH (zapomeňte na výchozí 22)
- Zvýšení úrovně hovorovosti protokolů z **INFO na VERBOSE**
- Nastavte hodnotu **LoginGraceTime** na **2 minuty**



Pokud do dvou minut nejsou zadány žádné informace o připojení, připojení se přeruší.





- Aktivace **strictModes**



Určuje, zda má sshd před ověřením připojení zkontrolovat režimy a vlastníka souborů uživatele a také domovský adresář uživatele. To je obvykle žádoucí, protože nováčci někdy omylem nechávají svůj adresář nebo soubory plně přístupné všem. Výchozí nastavení je "ano".





- Nastavte hodnotu **MaxAuthtries** na 3



Představuje počet neúspěšných pokusů o ověření před ukončením komunikace.





- Nastavení hodnoty **MaxSessions** na 2



To představuje maximální počet souběžných relací.





- Povolení ověřování pomocí veřejného klíče



```
PubkeyAuthentication yes
```





- Zachovat ověřování heslem :



```
PasswordAuthentication yes
```



Zákaz prázdných hesel a ověřování **Kerberos**, stejně jako **přímé ověřování kořene**



```
PermitEmptyPasswords no
PermitRootLogin no
```



Ujistěte se, že máte "**PermitRootLogin no", pokud se rovná "yes", je to "absolutní zlo "**.





- Zákaz přesměrování připojení TCP



```
AllowTcpForwarding no
```



Určuje, zda jsou povolena přesměrování TCP, přičemž výchozí nastavení je "ano". Upozornění: zakázání přesměrování TCP nezvýší zabezpečení, pokud mají uživatelé přístup k shellu, protože si stále mohou nastavit vlastní nástroje pro přesměrování.





- Zákaz přesměrování X11



```
X11Forwarding no
```



Určuje, zda jsou přesměrování X11 přijímána, přičemž výchozí nastavení je "ne". Upozornění: i když jsou přesměrování X11 zakázána, nezvyšuje to bezpečnost, protože uživatelé si stále mohou nastavit vlastní přesměrovače. Přesměrování X11 je automaticky zakázáno, pokud je vybrána možnost **Použítpřihlášení**.





- Nastavení časového limitu komunikace mezi klientem a sshd



```
ClientAliveInterval  300
```



Definuje časový limit v sekundách, po jehož uplynutí služba sshd odešle zprávu s žádostí o odpověď od klienta, pokud od něj neobdrží žádná data. Ve výchozím nastavení je tato možnost nastavena na "0", což znamená, že tyto zprávy nejsou klientovi zasílány. Tuto možnost podporuje pouze verze 2 protokolu SSH.



```
ClientAliveCountMax 0
```



Podle [dokumentace (*man page*) pro sshd](https://www.delafond.org/traducmanfr/man/man5/sshd_config.5.html) znamená tato volba následující: "Nastavuje počet podržených zpráv (viz výše), které mají být odeslány bez odpovědi od klienta pro **sshd**. Pokud je této prahové hodnoty dosaženo při odesílání podržených zpráv, **sshd** odpojí klienta a ukončí relaci. Je důležité si uvědomit, že tyto zprávy hold se velmi liší od možnosti **KeepAlive** (níže). Zprávy o podržení spojení jsou odesílány přes šifrovaný tunel, a proto je nelze podvrhnout. Zprávy o podržení spojení na úrovni protokolu TCP povolené pomocí funkce **KeepAlive** jsou podvrhnutelné. Mechanismus podržení spojení je zajímavý, pokud klient nebo server potřebuje vědět, zda je spojení nečinné."





- Zabránit vyzrazení informací zakázáním **motd, banner, lastlog**



```
PrintMotd no
```



Určuje, zda má sshd při přihlášení uživatele v interaktivním režimu zobrazit obsah souboru "/etc/motd". V některých systémech může být tento obsah zobrazen také shellem prostřednictvím souboru /etc/profile nebo podobného souboru. Výchozí hodnota je "yes".



```
Banner none
```



Stojí za zmínku, že v některých jurisdikcích může být podmínkou právní ochrany odeslání zprávy před jejím ověřením. Obsah zadaného souboru je předán vzdálenému uživateli před autorizací připojení. Tuto možnost je třeba nakonfigurovat, protože ve výchozím nastavení se žádná zpráva nezobrazí.



V obrázcích to dává :



![Image](assets/fr/019.webp)



### D. Výsledek auditu



Nakonec nezapomeňte zkontrolovat **skóre auditu Lynis**! Vidíme, že **můj Hardening score je 63** a že soubor s hlášením lze zobrazit v "**/var/log/lynis-report.dat**". K dispozici je také soubor "**/var/log/lynis.log**".



**Jinými slovy, čím vyšší skóre, tím lépe! Proto je třeba pracovat na konfiguraci tak, abyste dosáhli co nejvyššího skóre a zároveň umožnili normální fungování počítače a hostovaných služeb (což znamená provádění funkčních testů).



![Image](assets/fr/046.webp)



Podívejme se na výsledky na mém druhém serveru, kde jsem strávil trochu více času přitvrzováním! Je tedy normální, že skóre je vyšší (**76**).



![Image](assets/fr/045.webp)



## V. Lynis automatizované plánování



**Lynis** také nabízí možnost spouštět své kontroly prostřednictvím naplánované úlohy. Ve skutečnosti existuje možnost **"--cronjob "**, která spustí všechny testy Lynis bez nutnosti validace nebo zásahu uživatele. Můžete pak velmi jednoduše vytvořit skript, který spustí **Lynis** a výstup vloží do souboru s časovým razítkem a názvem daného serveru. Zde je soubor tohoto typu, který můžete umístit do složky */etc/cron.daily*:



```
#!/bin/sh
mkdir /var/log/lynis
NOM_AUDITEUR="tache_crontab"
DATE=$(date +%Y%m%d)
HOTE=$(hostname)
LOG_DIR="/var/log/Lynis"
RAPPORT="$LOG_DIR/rapport-${HOTE}.${DATE}"
DATA="$LOG_DIR/rapport-data-${HOTE}.${DATE}.txt"

cd /root/Lynis./Lynis -c --auditor "${NOM_AUDITEUR}" --cronjob > ${RAPPORT}
mv /var/log/lynis-report.dat ${DATA}
```



Proměnná **"AUDITOR_NAME "** je jednoduše proměnná, kterou nastavíme ve volbě **"--auditor "** programu **Lynis** tak, aby se toto jméno zobrazilo v sestavě:



![Image](assets/fr/059.webp)



Vytvoříme také několik kontextových proměnných, které nám pomohou lépe se organizovat, například název hostitele a datum pro pojmenování sestavy a její časové označení a cestu ke složce, do které chceme sestavy umístit.



## VI. Závěr



Lynis je velmi praktický nástroj, který vám pomůže ušetřit čas a být efektivnější, když chcete zjistit více o stavu konfigurace linuxového serveru, zejména z hlediska zabezpečení. Nezapomínejte však, že každou změnu je třeba před použitím v produkčním prostředí otestovat a zohlednit přitom vlastní použití a kontext.



Stejnou konfiguraci pravděpodobně nepoužijete pro VPS vystavený síti, kde potřebujete pouze jedno připojení SSH (protože jste jediná připojující se osoba), na rozdíl od **bastionu** nebo **scheduleru**, které budou potřebovat znásobit **SSH.** připojení



Jakmile získáte konfiguraci, která vám vyhovuje z hlediska zabezpečení, je vhodné použít automatizační nástroj, abyste nemuseli úlohy provádět znovu ručně, protože by to bylo časově náročné a náchylné k chybám. Můžete například použít **: Puppet, Chef, Ansible atd...**



Nezapomeňte před implementací komunikovat se svými týmy: musíte jim vysvětlit, proč tyto změny zavádíte, ne jim jen říct, že je zavádíte. Nakonec bude cílem předat dobré postupy, a to zvýší vaše šance na úspěch.



Nakonec můžete **Lynis** porovnat i s jinými nástroji, kterých je několik. Pokud chcete přejít na centralizovanou správu a zároveň zůstat u otevřeného kódu, doporučuji nástroj [Wazuh] (https://wazuh.com/).



**Tento tutoriál je u konce, bavte se s Lynisem!