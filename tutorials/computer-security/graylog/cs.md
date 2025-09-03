---
name: Graylog
description: Centralizace a snadná analýza protokolů
---
![cover](assets/cover.webp)



___



*Tento návod vychází z původního obsahu Floriana BURNELA zveřejněného na stránkách [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). V původním textu mohly být provedeny změny.*



___



## Nasazení Graylogu v Debianu 12



### I. Prezentace



Graylog je open source řešení "log sink" určené k centralizaci, ukládání a analýze protokolů z vašich počítačů a síťových zařízení v reálném čase. V tomto návodu se naučíme nainstalovat bezplatnou verzi Graylogu na počítač s Debianem 12!



V rámci informačního systému každý **server**, ať už s operačním systémem **Linux** nebo **Windows**, a každé **síťové zařízení** (přepínač, směrovač, brána firewall atd.) **generuje své vlastní protokoly**, které se ukládají lokálně. S protokoly uloženými lokálně na každém počítači je analýza a korelace událostí velmi obtížná... Zde přichází na řadu **Graylog**. Bude fungovat jako **odběrné místo pro protokoly**, což znamená, že **všechny vaše stroje mu budou posílat své protokoly** (například prostřednictvím syslogu). Graylog pak bude tyto protokoly **ukládat a indexovat** a zároveň vám umožní provádět globální vyhledávání a vytvářet upozornění.



Graylog je nástroj pro analýzu a monitorování, který usnadňuje identifikaci podezřelého chování a různých problémů (stabilita, výkon atd.).




![Image](assets/fr/034.webp)



**Poznámka: bezplatná verze **Graylog Open** není SIEM jako Wazuh, zejména proto, že postrádá skutečné funkce detekce narušení.



### II. Předpoklady



**Stack Graylog** je založen na **několika komponentách**, které budeme muset nainstalovat a nakonfigurovat. Zde nainstalujeme všechny komponenty na jeden server, ale je možné vytvořit clustery založené na několika uzlech a rozdělit role na více serverů. Pro účely tohoto návodu budeme instalovat **Graylog 6.1**, tedy dosud nejnovější verzi.





- MongoDB 7**, aktuální doporučená verze pro Graylog (minimálně 5.0.7, maximálně 7.x)
- OpenSearch**, open source Fork aplikace Elasticsearch vytvořené společností Amazon (minimálně 1.1.x, maximálně 2.15.x)
- OpenJDK 17**



Server **Graylog** je spuštěn v systému **Debian 12**, ale instalace je možná i v jiných distribucích, včetně instalace pomocí nástroje Docker. Virtuální počítač je vybaven **8 GB RAM** a **256 GB místa na disku**, aby měl dostatek prostředků pro všechny komponenty (jinak to může mít značný vliv na výkon). Uvádím to však jako hrubé vodítko, protože **velikost architektury Graylog závisí na množství zpracovávaných informací**. Graylog může zpracovat 30 MB nebo 300 MB dat za den, stejně jako 300 GB dat za den... Jedná se o **škálovatelné řešení** schopné zpracovat **terabajty protokolů** (viz [tato stránka](https://go2docs.graylog.org/current/planning_your_deployment/planning_your_deployment.html?tocpath=Plan%20Your%20Deployment%7C_____0)).



![Image](assets/fr/032.webp)



Zdroj: Graylog



Před zahájením konfigurace přiřaďte počítači Graylog statickou IP adresu Address a nainstalujte nejnovější aktualizace. Nezapomeňte nastavit časové pásmo místního počítače a definovat server NTP pro synchronizaci data a času. Zde je příkaz, který je třeba spustit:



```
sudo timedatectl set-timezone Europe/Paris
```



**Poznámka: Instalace **OpenSearch je nepovinná**, pokud místo toho použijete **Graylog Data Node**.



### III Instalace Graylog krok za krokem



Začněme aktualizací mezipaměti balíčků a instalací nástrojů, které potřebujeme pro to, co přijde.



```
sudo apt-get update
sudo apt-get install curl lsb-release ca-certificates gnupg2 pwgen
```



![Image](assets/fr/030.webp)



#### A. Instalace MongoDB



Jakmile to bude hotové, začneme instalovat MongoDB. Stáhněte si klíč GPG odpovídající úložišti MongoDB:



```
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```



Poté přidejte úložiště MongoDB 6 do počítače s Debianem 12:



```
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```



Dále aktualizujeme mezipaměť balíčků a pokusíme se nainstalovat MongoDB:



```
sudo apt-get update
sudo apt-get install -y mongodb-org
```



MongoDB nelze nainstalovat, protože chybí závislost: **libssl1.1**. Než budeme moci pokračovat, budeme muset tento balíček nainstalovat ručně, protože Debian 12 jej ve svých repozitářích nemá.



```
Les paquets suivants contiennent des dépendances non satisfaites :
mongodb-org-mongos: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
mongodb-org-server: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
E: Impossible de corriger les problèmes, des paquets défectueux sont en mode « garder en l'état ».
```



Pomocí příkazu **wget** stáhneme balíček DEB s názvem "**libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb**" (nejnovější verze) a poté jej nainstalujeme pomocí příkazu **dpkg**. Tím se vytvoří následující dva příkazy:



```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
```



![Image](assets/fr/028.webp)



Restartujte instalaci MongoDB:



```
sudo apt-get install -y mongodb-org
```



Poté restartujte službu MongoDB a povolte její automatické spuštění při spuštění serveru Debian.



```
sudo systemctl daemon-reload
sudo systemctl enable mongod.service
sudo systemctl restart mongod.service
sudo systemctl --type=service --state=active | grep mongod
```



Po instalaci MongoDB můžeme přejít k instalaci další součásti.



#### B. Instalace aplikace OpenSearch



Přejděme k instalaci služby OpenSearch na server. Následující příkaz přidá podpisový klíč pro balíčky OpenSearch:



```
curl -o- https://artifacts.opensearch.org/publickeys/opensearch.pgp | sudo gpg --dearmor --batch --yes -o /usr/share/keyrings/opensearch-keyring
```



Poté přidejte úložiště OpenSearch, abychom mohli balíček stáhnout pomocí **apt**:



```
echo "deb [signed-by=/usr/share/keyrings/opensearch-keyring] https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable main" | sudo tee /etc/apt/sources.list.d/opensearch-2.x.list
```



Aktualizujte mezipaměť balíčků:



```
sudo apt-get update
```



Poté **nainstalujte OpenSearch** a dbejte na to, abyste **nadefinovali výchozí heslo pro účet správce** vaší instance. Zde je heslo "**IT-Connect2024!**", ale nahraďte tuto hodnotu silným heslem. **Vyvarujte se slabých hesel**, jako je "**P@ssword123**", a používejte alespoň **8 znaků** s alespoň jedním znakem od každého typu (malá písmena, velká písmena, číslice a speciální znak), jinak dojde na konci instalace k chybě. **Tato podmínka je nutná od verze OpenSearch 2.12.**



```
sudo env OPENSEARCH_INITIAL_ADMIN_PASSWORD=IT-Connect2024! apt-get install opensearch
```



Během instalace buďte trpěliví...



Po dokončení proveďte minimální konfiguraci. Otevřete konfigurační soubor ve formátu YAML:



```
sudo nano /etc/opensearch/opensearch.yml
```



Po otevření souboru nastavte následující možnosti:



```
cluster.name: graylog
node.name: ${HOSTNAME}
path.data: /var/lib/opensearch
path.logs: /var/log/opensearch
discovery.type: single-node
network.host: 127.0.0.1
action.auto_create_index: false
plugins.security.disabled: true
```



Tato konfigurace služby OpenSearch je určena k nastavení jednoho uzlu. Zde je několik vysvětlení k jednotlivým parametrům, které používáme:





- cluster.name: graylog**: tento parametr pojmenovává cluster OpenSearch s názvem "**graylog**".
- node.name: ${HOSTNAME}**: název uzlu je nastaven dynamicky tak, aby odpovídal názvu místního počítače Linux. I když máme pouze jeden uzel, je důležité jej správně pojmenovat.
- path.data: /var/lib/opensearch**: tato cesta určuje, kam OpenSearch ukládá svá data na lokálním počítači, v tomto případě do "**/var/lib/opensearch**".
- path.logs: /var/log/opensearch**: tato cesta určuje, kde jsou uloženy soubory protokolu OpenSearch, zde v "**/var/log/opensearch**".
- discovery.type: single-node**: tento parametr konfiguruje OpenSearch pro práci s jedním uzlem, proto je zvolena možnost "**single-node**".
- network.host: 127.0.0.1**: tato konfigurace zajišťuje, že OpenSearch naslouchá pouze na své lokální smyčce Interface, což je dostačující, protože je na stejném serveru jako Graylog.
- action.auto_create_index: false**: vypnutím automatického vytváření indexu OpenSearch automaticky nevytvoří index, pokud je dokument odeslán bez existujícího indexu.
- plugins.security.disabled: true**: tato volba deaktivuje bezpečnostní plugin OpenSearch, což znamená, že nebude k dispozici žádné ověřování, správa přístupu ani šifrování komunikace. Toto nastavení šetří čas při nastavování Graylogu, ale v produkčním provozu byste se mu měli vyhnout (viz [tato stránka](https://opensearch.org/docs/1.0/security-plugin/index/)).



Některé možnosti jsou již přítomny, takže stačí odstranit znak "#", abyste je aktivovali, a poté zadat svou hodnotu. Pokud volbu nemůžete najít, můžete ji deklarovat přímo na konci souboru.



![Image](assets/fr/023.webp)



Uložte a zavřete tento soubor.



#### C. Konfigurace Javy (JVM)



Je třeba nakonfigurovat virtuální počítač Java používaný službou OpenSearch, aby bylo možné upravit množství paměti, které může tato služba využívat. Upravte následující konfigurační soubor:



```
sudo nano /etc/opensearch/jvm.options
```



Při zde nasazené konfiguraci **OpenSearch začne s přidělenou pamětí 4 GB a může se zvětšit až na 4 GB**, takže během provozu nedochází k žádným výkyvům paměti. Zde konfigurace zohledňuje skutečnost, že virtuální počítač má celkem **8 GB RAM**. Oba parametry musí mít stejnou hodnotu. To znamená nahradit řádky:



```
-Xms1g
-Xmx1g
```



S těmito řádky:



```
-Xms4g
-Xmx4g
```



Zde je obrázek úpravy, kterou je třeba provést:



![Image](assets/fr/022.webp)



Po uložení tento soubor zavřete.



Dále je třeba zkontrolovat konfiguraci parametru "**max_map_count**" v jádře Linuxu. Ten definuje limit mapovaných paměťových oblastí na jeden proces, aby vyhovoval potřebám naší aplikace. **OpenSearch**, stejně jako Elasticsearch**, doporučuje nastavit tuto hodnotu na "262144", aby se předešlo chybám při správě paměti.



Na čerstvě nainstalovaném počítači s Debianem 12 je tato hodnota v zásadě správná. Ale ověřme si to. Spusťte tento příkaz:



```
cat /proc/sys/vm/max_map_count
```



Pokud získáte jinou hodnotu než "**262144**", spusťte následující příkaz, jinak to není nutné.



```
sudo sysctl -w vm.max_map_count=262144
```



Nakonec povolte automatické spouštění služby OpenSearch a spusťte přidruženou službu.



```
sudo systemctl daemon-reload
sudo systemctl enable opensearch
sudo systemctl restart opensearch
```



Pokud zobrazíte stav systému, měl by se zobrazit proces Java se 4 GB RAM.



```
top
```



![Image](assets/fr/029.webp)



Další krok: dlouho očekávaná instalace Graylogu!



#### D. Instalace Graylogu



Chcete-li **nainstalovat Graylog 6.1** v jeho nejnovější verzi, spusťte následující 4 příkazy pro **stažení a instalaci serveru Graylog**:



```
wget https://packages.graylog2.org/repo/packages/graylog-6.1-repository_latest.deb
sudo dpkg -i graylog-6.1-repository_latest.deb
sudo apt-get update
sudo apt-get install graylog-server
```



Po dokončení této operace musíme provést několik změn v konfiguraci Graylogu, než se jej pokusíme spustit.



Začněme konfigurací těchto dvou možností:





- password_secret**: tento parametr slouží k definici klíče, který Graylog používá k zabezpečení ukládání uživatelských hesel (v duchu solícího klíče). Tento klíč musí být **unikátní** a **náhodný**.
- root_password_sha2**: tento parametr odpovídá výchozímu heslu správce v systému Graylog. Je uloženo ve formátu Hash SHA-256.



Začneme vygenerováním 96znakového klíče pro parametr **heslo_secret**:



```
pwgen -N 1 -s 96
wVSGYwOmwBIDmtQvGzSuBevWoXe0MWpNWCzhorBfvMMhia2zIjHguTbfl4uXZJdHOA0EEb1sOXJTZKINhIIBm3V57vwfQV59
```



Zkopírujte vrácenou hodnotu a otevřete konfigurační soubor Graylog:



```
sudo nano /etc/graylog/server/server.conf
```



Vložte klíč do parametru **password_secret** takto:



![Image](assets/fr/027.webp)



Uložte a zavřete soubor.



Dále je třeba nastavit heslo pro standardně vytvořený účet "**admin**". V konfiguračním souboru musí být uloženo heslo Hash, což znamená, že musí být vypočteno. Níže uvedený příklad uvádí Hash hesla "**LogsWells@**": přizpůsobte hodnotu svému heslu.



```
echo -n "PuitsDeLogs@" | shasum -a 256
6b297230efaa2905c9a746fb33a628f4d7aba4fa9d5c1b3daa6846c68e602d71
```



Zkopírujte získanou hodnotu jako výstup (bez pomlčky na konci řádku).



Znovu otevřete konfigurační soubor Graylog:



```
sudo nano /etc/graylog/server/server.conf
```



Vložte hodnotu do možnosti **root_password_sha2** takto:



![Image](assets/fr/026.webp)



V konfiguračním souboru nastavte možnost "**http_bind_address**". Zadejte "**0.0.0.0:9000**", aby byl web Graylog Interface přístupný na portu **9000** prostřednictvím libovolného serveru IP Address.



![Image](assets/fr/024.webp)



Poté nastavte možnost "**elasticsearch_hosts**" na `http://127.0.0.1:9200`, abyste deklarovali naši místní instanci služby OpenSearch. To je nezbytné, protože nepoužíváme datový uzel **Graylog**. A bez této možnosti nebude možné pokračovat dále...



![Image](assets/fr/025.webp)



Uložte a zavřete soubor.



Tento příkaz aktivuje Graylog tak, aby se při příštím spuštění automaticky spustil, a okamžitě spustí server Graylog.



```
sudo systemctl enable --now graylog-server
```



Po dokončení tohoto úkonu se zkuste připojit ke službě Graylog z prohlížeče. Zadejte IP adresu serveru Address (nebo název) a port 9000.



**Pro vaši informaci:**



Není to tak dávno, co se při prvním přihlášení do Graylogu objevilo ověřovací okno podobné tomu, které je uvedeno níže. Museli jste zadat své přihlašovací jméno "**admin**" a heslo. A pak jste byli nemile překvapeni, že připojení nefunguje.



![Image](assets/fr/031.webp)



Bylo nutné vrátit se k příkazovému řádku na serveru Graylog a nahlédnout do protokolů. Poté jsme mohli zjistit, že **pro první připojení** je nutné **použít dočasné heslo**, uvedené v protokolech.



```
tail -f /var/log/graylog-server/server.log
```



![Image](assets/fr/021.webp)



Poté jste museli zopakovat připojení s uživatelem "**admin**" a dočasným heslem, což vám umožnilo přihlášení!



**To již neplatí. Stačí se přihlásit pomocí účtu správce a hesla nakonfigurovaného v příkazovém řádku



![Image](assets/fr/033.webp)



**Vítejte na Graylogově Interface!



![Image](assets/fr/019.webp)



#### E. Graylog: vytvoření nového účtu správce



Namísto používání účtu správce vytvořeného nativně službou Graylog si můžete vytvořit vlastní osobní účet správce. Klikněte na nabídku "**Systém**", poté na "**Uživatelé a týmy**" a klikněte na tlačítko "**Vytvořit uživatele**". Poté vyplňte formulář a přiřaďte svému účtu roli správce.



![Image](assets/fr/020.webp)



Personalizovaný účet může na rozdíl od nativního účtu správce obsahovat další informace, například jméno a příjmení a e-mail Address. Navíc je tak zajištěna lepší dohledatelnost, když každá osoba pracuje s pojmenovaným účtem.



## Odesílání protokolů do Graylogu pomocí rsyslogu



### I. Prezentace



V této druhé části se naučíme, jak nakonfigurovat počítač se systémem Linux tak, aby odesílal své protokoly na server Graylog. Za tímto účelem nainstalujeme a nakonfigurujeme systém Rsyslog.



### II. Konfigurace Graylogu pro příjem protokolů systému Linux



Začneme konfigurací Graylogu. Je třeba provést tři kroky:





- Vytvoření **vstupu** pro vytvoření vstupního bodu umožňujícího počítačům se systémem Linux **odesílat protokoly Syslog prostřednictvím protokolu UDP**.
- Vytvoření nového **Indexu** pro ukládání a **indexování všech protokolů systému Linux**.
- Vytvoření **Proudu** pro **směrování** protokolů přijatých Graylogem do nového linuxového indexu.



#### A. Vytvoření vstupu pro protokol Syslog



Přihlaste se do systému Graylog Interface, v nabídce klikněte na "**Systém**" a poté na "**Vstupy**". V rozevíracím seznamu vyberte položku "**Syslog UDP**" a poté klikněte na tlačítko označené "**Začítat nový vstup**". Je také možné vytvořit vstup TCP Syslog, ale to vyžaduje použití certifikátu TLS: je to výhoda z hlediska bezpečnosti, ale v tomto článku se jí nebudeme zabývat.



![Image](assets/fr/001.webp)



Na obrazovce se zobrazí průvodce. Začněte zadáním názvu tohoto vstupu, například "**Graylog_UDP_Rsyslog_Linux**", a vyberte port. Ve výchozím nastavení je port "**514**", ale můžete si jej přizpůsobit. Zde je vybrán port "**12514**".



![Image](assets/fr/016.webp)



Můžete také zaškrtnout možnost "**Uložit celou zprávu**", aby se do Graylogu uložila celá zpráva protokolu. Klikněte na "**Spustit vstup**".



![Image](assets/fr/017.webp)



Nový vstup byl vytvořen a je nyní aktivní. Graylog nyní může přijímat protokoly Syslog na portu 12514/UDP, ale ještě jsme nedokončili konfiguraci aplikace.



![Image](assets/fr/018.webp)


**Poznámka: jeden vstup lze použít k ukládání protokolů z několika počítačů se systémem Linux.



#### B. Vytvoření nového indexu Linux



Potřebujeme vytvořit index v systému Graylog, do kterého budeme ukládat protokoly z počítačů se systémem Linux. **Index** v Graylogu je úložná struktura, která obsahuje přijaté protokoly, tj. přijaté zprávy. Graylog používá jako úložný engine OpenSearch a zprávy jsou indexovány, aby bylo možné rychlé a efektivní vyhledávání.



V programu Graylog klikněte v nabídce na "**Systém**" a poté na "**Indices**". Na nově zobrazené stránce klikněte na "**Vytvořit sadu indexů**".



![Image](assets/fr/005.webp)



Před potvrzením tento index pojmenujte, například "**Linux Index**", přidejte popis a předponu. Zde budeme **ukládat všechny protokoly systému Linux do tohoto indexu**. Je také možné vytvořit specifické indexy pro ukládání pouze určitých protokolů (pouze protokoly [SSH] (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/ "SSH"), protokoly webových služeb atd.)



![Image](assets/fr/006.webp)



Nyní je třeba vytvořit nový datový tok pro směrování zpráv do tohoto indexu.



#### C. Vytvoření proudu



Chcete-li vytvořit nový stream, klikněte na "**Streams**" v hlavní nabídce Graylogu. Poté klikněte na tlačítko "**Vytvořit stream**" vpravo. V okně, které se zobrazí, pojmenujte stream, například "**Linux Stream**", a do pole s názvem "**Index Set**" vyberte index "**Linux Index**". Svou volbu potvrďte.



**Poznámka: zprávy odpovídající tomuto proudu budou zahrnuty také do "**Výchozího proudu**", pokud nezaškrtnete možnost "**Odstranit shody z 'Výchozího proudu'**".



![Image](assets/fr/002.webp)



Poté v nastavení služby steam klikněte na tlačítko "**Přidat pravidlo streamu**" a přidejte nové pravidlo směrování zpráv. Pokud toto okno nemůžete najít, klikněte v nabídce na "**Streamy**" a poté na řádku odpovídajícím vašemu streamu klikněte na "**Další**" a poté na "**Správa pravidel**".



Zvolte typ "**match input**" a vyberte dříve vytvořený **Rsyslog input in UDP**. Potvrďte tlačítkem "**Vytvořit pravidlo**". Všechny zprávy na náš nový vstup budou nyní odesílány do indexu pro Linux.



![Image](assets/fr/003.webp)



Váš nový Stream by se měl objevit v seznamu a měl by být ve stavu "**Running**". Šířka pásma zpráv ukazuje "**0 msg/s**", protože v současné době neodesíláme žádné protokoly na vstup Rsyslog UDP. Chcete-li zobrazit protokoly proudu, stačí kliknout na jeho název.



![Image](assets/fr/004.webp)



**Vše je připraveno na straně Graylog**. Dalším krokem je konfigurace linuxového počítače.



### III. Instalace a konfigurace systému Rsyslog v systému Linux



Přihlaste se do počítače se systémem Linux, ať už lokálně, nebo vzdáleně, a použijte uživatelský účet s oprávněním zvýšit jeho oprávnění (pomocí sudo). V opačném případě použijte přímo účet "root".



#### A. Instalace balíčku Rsyslog



Začněte aktualizací mezipaměti balíčků a instalací balíčku s názvem "**rsyslog**".



```
sudo apt-get update
sudo apt-get install rsyslog
```



Poté zkontrolujte stav služby. Ve většině případů je již spuštěna.



```
sudo systemctl status rsyslog
```



#### B. Konfigurace protokolu Rsyslog



Rsyslog má hlavní konfigurační soubor umístěný zde:



```
/etc/rsyslog.conf
```



Kromě toho se adresář "**/etc/rsyslog.d/**" používá k ukládání dalších konfiguračních souborů pro Rsyslog. V hlavním konfiguračním souboru je direktiva Include, která importuje všechny soubory "**.conf**" umístěné v tomto adresáři. Díky tomu je možné mít další soubory pro konfiguraci Rsyslogu, aniž by bylo nutné měnit hlavní soubor.



V tomto adresáři je nutné použít čísla pro určení pořadí načítání, protože soubory se načítají v abecedním pořadí. Přidání číselné předpony umožňuje spravovat prioritu mezi několika konfiguračními soubory. Zde máme pouze jeden další soubor, takže to není problém.



V tomto adresáři vytvoříme soubor s názvem "**10-graylog.conf**":



```
sudo nano /etc/rsyslog.d/10-graylog.conf
```



Do tohoto souboru vložte tento řádek:



```
*.* @192.168.10.220:12514;RSYSLOG_SyslogProtocol23Format
```



Tady je návod, jak si tuto větu vyložit:





- `*.*`: znamená odesílání všech protokolů Syslog z linuxového počítače do Graylogu.
- `@`: označuje, že přenos probíhá v protokolu UDP. Chcete-li přepnout na TCP, musíte zadat "**@@**".
- `192.168.10.220:12514`: označuje Address serveru Graylog a port, na který se odesílají protokoly (odpovídá Vstupu).
- `RSYSLOG_SyslogProtocol23Format`: odpovídá formátu zpráv, které mají být odesílány do Graylogu.



Po dokončení soubor uložte a restartujte systém Rsyslog.



```
sudo systemctl restart rsyslog.service
```



Po této akci by na váš server Graylog měly dorazit první zprávy!



### IV. Zobrazení logů Linuxu v Graylogu



V Graylogu můžete kliknout na "**Streams**" a vybrat nový stream pro zobrazení souvisejících zpráv. Případně klikněte na "**Hledat**", vyberte svůj Steam a spusťte vyhledávání.



Zde jsou některé klíčové vlastnosti modelu Interface:



**1** - Vyberte období, za které se mají zprávy zobrazovat. Ve výchozím nastavení se zobrazují zprávy za posledních 5 minut.



**2** - Vyberte proud(y), které se mají zobrazit.



**3** - Povolte automatické obnovování seznamu zpráv (například každých 5 sekund). V opačném případě bude statický a budete jej muset obnovovat ručně.



**4** - Kliknutím na lupu spustíte vyhledávání po úpravě období, toku nebo filtru.



**5** - Vstupní panel pro zadání vyhledávacích filtrů. Zde zadám "**source:srv\-docker**", aby se zobrazily pouze protokoly nového počítače, na kterém jsem právě nastavil Rsyslog.



Protokoly jsou odesílány počítačem se systémem Linux:



![Image](assets/fr/015.webp)



### V. Identifikace selhání připojení SSH



Síla Graylogu spočívá v jeho schopnosti indexovat protokoly a umožnit vyhledávání podle různých kritérií: zdrojový stroj, Timestamp, obsah zprávy atd... Mohli bychom hledat neúspěšná připojení SSH.



Ze vzdáleného počítače (například ze serveru Graylog) se zkuste připojit k serveru Linux, na kterém jste právě nakonfigurovali Rsyslog. Například:



```
ssh [email protected]
```



Poté záměrně zadejte nesprávné **jméno** a **heslo**, abyste dosáhli **Chyb v připojení generate**. V souboru "**/var/log/auth.log**" se tak objeví hlášení protokolu generate podobné následujícímu:



```
Failed password for invalid user it-connect from 192.168.10.199 port 50352 ssh2
```



Tyto zprávy byste měli najít na Graylogu.



V Graylogu použijte následující vyhledávací filtr pro zobrazení pouze odpovídajících zpráv:



```
message:Failed password AND application_name:sshd
```



Pokud máte několik serverů a chcete analyzovat protokoly konkrétního serveru, zadejte kromě jeho názvu také:



```
message:Failed password AND application_name:sshd AND source:srv\-docker
```



Zde je přehled výsledku na počítači, kde jsem vygeneroval několik chyb připojení v různých denních dobách:



![Image](assets/fr/009.webp)



Neúspěšné pokusy o připojení jsou prováděny z počítače s IP adresou Address "**192.168.10.199**". Chcete-li se o aktivitě tohoto hostitele dozvědět více, můžete **vyhledat tuto IP adresu Address**. Graylog vypíše všechny protokoly, ve kterých je odkazováno na tuto IP adresu Address, na všech hostitelích (pro které je nakonfigurováno odesílání protokolů).



V tomto případě lze použít filtr:



```
message:"192.168.10.199"
```



Získáme další výsledky (což není překvapivé, protože v aplikaci SSH nefiltrujeme):



![Image](assets/fr/008.webp)



### VI. Závěr



Podle tohoto návodu byste měli být schopni nakonfigurovat počítač se systémem Linux tak, aby odesílal své protokoly na server Graylog. Tímto způsobem budete moci centralizovat logy svých linuxových hostitelů v log sink!



Chcete-li jít ještě dál, zvažte vytvoření řídicích panelů a výstrah, abyste mohli dostávat upozornění při zjištění anomálie.



![Image](assets/fr/007.webp)