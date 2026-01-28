---
name: Start9

description: Výukový program o nastavení soukromého serveru Start9

---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=DzikmY4S42Y)


*Zde je videonávod od Southern Bitcoiner, videonávod, který vám ukáže, jak nastavit a používat osobní server Start9 / StartOS a jak spustit bitcoinový uzel.*


## 1️⃣ Úvod


### Co přesně je Start9?


Start9 je společnost založená v roce 2020, která je známá především vývojem [**StartOS**,](https://github.com/Start9Labs/start-os) operačního systému založeného na Linuxu a určeného pro osobní servery. Umožňuje uživatelům snadno samostatně hostovat širokou škálu softwarových služeb - například uzly Bitcoin a Lightning, aplikace pro zasílání zpráv nebo správce hesel, přičemž si zachovávají plnou kontrolu nad svými daty a eliminují závislost na centralizovaných technologických platformách. StartOS nabízí uživatelsky přívětivé rozhraní založené na prohlížeči, kurátorský Marketplace pro instalaci služeb a integrované nástroje pro ochranu soukromí, jako je integrace Tor a šifrování HTTPS v celém systému. Start9 také poskytuje hardwarová zařízení s předinstalovaným operačním systémem, ačkoli software lze nainstalovat na kompatibilní hardware nebo virtuální počítače (VM).


### Jaké možnosti jsou k dispozici?


Start9 nabízí jak předpřipravené, tak DIY možnosti nasazení. Modely [**Server One**](https://store.start9.com/collections/servers/products/server-one) a [**Server Pure** ](https://store.start9.com/collections/servers/products/server-pure) jsou oficiální hardwarová zařízení s výkonnými komponentami: Server One využívá procesor **AMD Ryzen 7 5825U** s konfigurovatelnou pamětí RAM (16-64 GB) a úložištěm (2TB-4TB NVMe SSD), zatímco Server Pure je vybaven procesorem **Intel i7-10710U** a rovněž nabízí konfigurovatelnou paměť RAM a úložiště. Oba zahrnují **životní technickou podporu** při nákupu přímo od společnosti Start9. Uživatelé, kteří dávají přednost flexibilitě, mohou systém StartOS zdarma nainstalovat na širokou škálu stávajícího hardwaru, včetně notebooků, stolních počítačů, mini PC a jednodeskových počítačů, nebo v rámci virtuálních počítačů.


![image](assets/en/01.webp)


### Jaké jsou rozdíly oproti Umbrelu?


StartOS i Umbrel zjednodušují instalaci samoobslužných služeb, ale liší se architekturou a funkcemi. Umbrel funguje jako aplikační vrstva na systémech Debian/Ubuntu nebo virtuálních počítačích, zatímco Start9 je specializovaný operační systém vyžadující přímou instalaci na hardware nebo virtuální počítač. Umbrel má vybroušené rozhraní inspirované systémem MacOS, zatímco Start9 upřednostňuje funkční, minimální design. Umbrel nabízí větší [výběr aplikací](https://apps.umbrel.com/), zatímco [Start9 Marketplace](https://marketplace.start9.com/) to kompenzuje pokročilými technickými možnostmi. Start9 zjednodušuje přístup k pokročilým nastavením prostřednictvím ověřených formulářů uživatelského rozhraní, čímž snižuje potřebu interakce s příkazovým řádkem. Vyniká také ve správě zálohování díky šifrovanému zálohování systému jedním kliknutím, což je funkce, kterou Umbrel nativně postrádá. StartOS poskytuje integrované nástroje pro monitorování a vynucuje šifrování HTTPS pro přístup k místní síti, čímž zvyšuje bezpečnost. Umbrel používá lokálně nešifrovaný protokol HTTP, ačkoli obě platformy podporují zabezpečený vzdálený přístup přes Tor. Umbrel je vhodný pro uživatele, kteří upřednostňují bohatý ekosystém aplikací a vyladěné uživatelské rozhraní. Start9 je silnou volbou pro ty, kteří oceňují zabezpečení, konfigurovatelnost, spolehlivost zálohování a pokročilou správu služeb, aniž by museli mít znalosti příkazového řádku. Chcete-li se dozvědět více o produktu Umbrel a rozdílech oproti produktu Start9, navštivte tento kurz:


https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

## 2️⃣ DIY Předpoklady: Minimální a doporučené specifikace


Pro základní použití s minimem služeb jsou **minimální specifikace** následující: **1 jádro vCPU (2,0GHz+ boost), 4GB RAM, 64GB úložiště** a port Ethernet. Přesto bych doporučil jít výrazně nad tento rámec, zejména pokud provozujete uzel Bitcoin. Osobně jsem začínal s 1 TB a rychle mi došlo místo. Raději se zaměřte na **nejméně 2TB úložiště** spolu s **čtyřjádrovým procesorem (2,5 GHz+)** a **8 GB+ RAM**. Je to obrovský rozdíl ve výkonu a životnosti. Pokud se chcete ponořit do hloubky, zde je aktuální komunitní vlákno o [Hardwaru schopném spustit systém StartOS](https://community.start9.com/t/known-good-hardware-master-list-hardware-capable-of-running-startos/66/229).


## 3️⃣ Stažení a flashování firmwaru


Chcete-li zahájit nastavení, navštivte na samostatném počítači [webovou stránku Start9](https://start9.com/) a přejděte do sekce dokumentace kliknutím na `DOCS`. Odtud přejděte do části `Průvodci flashováním` a vyhledejte příslušnou verzi systému StartOS. K dispozici jsou dvě možnosti:



- StartOS (Raspberry Pi)
- StartOS (X86/ARM)


Tento návod se zabývá volbou `x86/ARM`.


Nejnovější verzi operačního systému si můžete stáhnout ze stránky [Github release page](https://github.com/Start9Labs/start-os/releases/latest). pro uživatele, kteří si chtějí vyzkoušet nové funkce, jsou k dispozici také verze [Pre-release](https://github.com/Start9Labs/start-os/releases). V dolní části stránky, v části `Assets`, si stáhněte `x86_64` nebo `x86_64-nonfree.iso`.  Obraz `x86_64-nonfree.iso` obsahuje nesvobodný (closed-source) software potřebný pro Server One a většinu DIY hardwaru, zejména pro podporu grafiky a síťových zařízení.


Doporučujeme ověřit integritu souboru porovnáním jeho hashe SHA256 s hashem uvedeným na GitHubu. Pro Linux lze použít příkaz `sha256sum startos-0.3.4.2-efc56c0-20230525_x86_64.iso`, ostatní operační systémy jsou popsány v dokumentaci.


Po stažení a ověření bitové kopie systému StartOS je třeba ji nahrát na jednotku USB. pro tento úkol se doporučuje software `BalenaEtcher`. Jedná se o bezplatný nástroj s otevřeným zdrojovým kódem pro zápis obrazů operačních systémů na jednotky USB a karty SD, který je k dispozici pro systémy Windows, macOS a Linux. Stáhněte si příslušnou verzi z oficiálních stránek [Balena Etcher](https://www.balena.io/etcher/) a spusťte instalační program. Připojte cílovou jednotku USB nebo kartu SD, otevřete Balena Etcher a kliknutím na `Flash from file` vyberte stažený obraz operačního systému. Program Etcher automaticky detekuje připojené jednotky; pokud jich je více, vyberte správný cíl. Klikněte na `Flash!` a začněte zapisovat obraz. Po dokončení Etcher automaticky ověří proces zápisu. Po dokončení bezpečně vyjměte jednotku a použijte ji ke spuštění zařízení.


![image](assets/en/19.webp)


## úvodní nastavení 4️⃣


Informace o počátečním nastavení naleznete na stránce Start9 [dokumentace](https://docs.start9.com/0.3.5.x/) v části `Uživatelská příručka` a následně v části `Začínáme - počáteční nastavení`.  V této oficiální příručce by měly být uvedeny nejaktuálnější informace.


Jsou uvedeny dvě možnosti:



- Začněte znovu
- Možnosti obnovy


Při nové instalaci serveru vyberte možnost `Spustit nový`. Nejprve připojte server k napájení a ethernetovému kabelu. Ujistěte se, že počítač použitý pro nastavení je ve stejné místní síti. Vyjměte nově flashovanou jednotku USB z počítače a vložte ji do serveru.


Server můžete ovládat vzdáleně z libovolného počítače ve stejné síti. Otevřete webový prohlížeč a přejděte na adresu `http://start.local`.


**Poznámka**: Pokud se s touto adresou vyskytnou problémy s připojením, je to často způsobeno tím, že domácí sítě nedokáží přeložit doménová jména `.local`. Problém lze vyřešit přímým přístupem k serveru prostřednictvím jeho IP adresy. IP adresu lze zjistit přihlášením do administrátorského rozhraní směrovače (obvykle na adrese `192.168.1.1` nebo podobné adrese) a vyhledáním zařízení v seznamu klientů DHCP nebo v seznamu map sítě. Poté do prohlížeče zadejte celou adresu IP (např. `http://192.168.1.105`). Tím obejdete překlad DNS. Pokud problémy přetrvávají, podívejte se na stránku [Common Issues page](https://docs.start9.com/0.3.5.x/support/common-issues.html#setup-troubleshoot) nebo [reach out to their support.](https://start9.com/contact/)


Měla by se zobrazit obrazovka nastavení systému StartOS. Kliknutím na tlačítko `Start Fresh` zahájíte nastavení nového serveru.


![image](assets/en/03.webp)


Dalším krokem je výběr úložné jednotky, na kterou budou uložena data systému StartOS.


![image](assets/en/04.webp)


Nastavení silného `Hesla` pro server. Zaznamenejte ho podle rady Start9 a klikněte na tlačítko `Dokončit`.


![image](assets/en/05.webp)


Na obrazovce se zobrazí zpráva, že systém StartOS inicializuje a nastavuje server. Dalším krokem je `Stáhnout informace o adrese`, protože adresa `start.local` slouží pouze pro účely nastavení a poté nebude fungovat.


![image](assets/en/06.webp)


Konfigurační soubor obsahuje dvě kritické přístupové adresy: jednu pro `místní síť (LAN)` a druhou pro zabezpečený přístup přes `Tor`. Obě adresy by měly být uloženy v bezpečném správci hesel. Dalším krokem je `Důvěřovat kořenové certifikační autoritě`. Otevřete novou kartu prohlížeče a postupujte podle pokynů pro důvěřování kořenové certifikační autoritě a přihlášení. Certifikát kořenové certifikační autority lze také stáhnout kliknutím na `Stáhnout certifikát` ve staženém souboru.


## 5️⃣ Důvěřujte své kořenové certifikační autoritě


Po stažení certifikátu musí být kořenová certifikační autorita serveru důvěryhodná pro operační systém. Klikněte na tlačítko `Zobrazit pokyny` a vyhledejte pokyny pro konkrétní operační systém.


![image](assets/en/07.webp)


V systému Linux se používají následující příkazy. Nejprve otevřete Terminál a nainstalujte potřebné balíčky:


```shell
sudo apt update

sudo apt install -y ca-certificates p11-kit
```


Přejděte do adresáře, kam byl certifikát stažen, obvykle `~/Downloads` . Pro přidání certifikátu do úložiště důvěryhodnosti operačního systému proveďte tyto příkazy. Přepněte se do adresáře stažených souborů pomocí `cd ~/Downloads`. Vytvořte požadovaný adresář příkazem `sudo mkdir -p /usr/share/ca-certificates/start9`. Zkopírujte soubor s certifikátem a nahraďte `všechno.crt` skutečným názvem souboru pomocí `sudo cp "vaše-jméno.crt" /usr/share/ca-certificates/start9/`. Certifikát trvale zaregistrujte připojením jeho cesty do konfigurace systému pomocí `sudo bash -c "echo 'start9/your-filename.crt' >> /etc/ca-certificates.conf"`. Nakonec obnovte důvěryhodné úložiště pomocí `sudo update-ca-certificates`. Před provedením těchto příkazů je důležité použít skutečný název souboru certifikátu a ověřit všechny cesty. Tímto postupem se vytvoří trvalá důvěryhodnost pro připojení HTTPS serveru Start9.


Úspěšná instalace bude indikována výstupním hlášením `1 added`. Většina aplikací se pak bude moci bezpečně připojit prostřednictvím `https`. Pokud používáte Firefox, je vyžadován další [poslední krok](https://docs.start9.com/0.3.5.x/misc-guides/ca-ff.html#ca-ff). V případě prohlížeče Chrome nebo Brave je zapotřebí jiný [závěrečný krok](https://docs.start9.com/0.3.5.x/misc-guides/ca-chrome.html#ca-chrome), který prohlížeč nakonfiguruje tak, aby respektoval kořenovou certifikační autoritu. Připojení otestujte obnovením stránky. Pokud problém přetrvává, ukončete a znovu otevřete prohlížeč a teprve poté znovu otevřete stránku.


![image](assets/en/08.webp)


## 6️⃣ Začínáme se systémem StartOS


Nyní by mělo být možné přihlásit se pomocí zabezpečeného připojení HTTPS. Zadejte `Heslo` pro přístup k `Uvítací obrazovce`.


![image](assets/en/09.webp)


Tato obrazovka obsahuje užitečné zkratky pro zahájení práce. Levý postranní panel obsahuje hlavní položky navigačního menu.


## 7️⃣ System


Karta Systémy v systému StartOS poskytuje přístup k základním systémovým funkcím pro správu osobního serveru. Nabízí nástroje pro údržbu, zabezpečení, diagnostiku a konfiguraci systému, aniž by bylo nutné mít znalosti příkazového řádku.


Sekce `Zálohy` umožňuje vytvářet úplné zálohy systému včetně služeb, konfigurací a dat, které lze později obnovit. To je nezbytné pro obnovu po havárii nebo pro přechod na nový hardware. Zálohy lze ukládat na externí disky a jsou šifrovány pomocí hlavního hesla.


Sekce `Správa` na kartě Systémy umožňuje ovládat klíčové funkce systému. Uživatelé mohou ručně zkontrolovat a použít aktualizace systému StartOS, čímž si zachovají kontrolu nad procesem aktualizace systému. Je možné načíst vlastní služby nebo služby třetích stran, které nejsou k dispozici na oficiálním trhu. Pokud server není připojen prostřednictvím sítě Ethernet, lze v této části konfigurovat nastavení Wi-Fi. Pokročilí uživatelé mohou povolit přístup SSH pro správu systému na úrovni terminálu.


![image](assets/en/10.webp)


Sekce `Insights` poskytuje sledování výkonu a stavu serveru v reálném čase a zobrazuje využití procesoru, paměti RAM a disku pomocí grafů. Zobrazuje také teplotu systému, což je užitečné u zařízení, jako je Raspberry Pi, která nemají aktivní chlazení. Metriky doby provozu a průměrné zátěže pomáhají posoudit stabilitu systému a pro řešení problémů se službou nebo systémem jsou k dispozici živé protokoly.


Sekce `Podpora` nabízí přístup k integrovaným častým dotazům, oficiální dokumentaci a komunitním kanálům podpory. Z této sekce lze stáhnout protokoly ladění a sdílet je s podporou Start9 pro rychlejší řešení problémů.


![image](assets/en/11.webp)


## 8️⃣ Marketplace


Služba `Marketplace` slouží k vyhledávání, instalaci a správě služeb na osobním serveru. Poskytuje přístup k softwaru, jako je Bitcoin Core, BTCPay Server a electrs. StartOS podporuje více tržišť, včetně oficiálního registru Start9 a komunitních registrů. Ty lze přidat kliknutím na tlačítko `Změnit` a přepnutím na `Komunitní registr`, který poskytuje přístup k širšímu spektru služeb.


![image](assets/en/12.webp)


## 9️⃣ Instalace plného uzlu Bitcoin


Instalace Bitcoin full node v systému StartOS poskytuje plnou suverenitu nad prostředím Bitcoin. Umožňuje ověřování transakcí a zvyšuje soukromí a zabezpečení tím, že odstraňuje závislost na externích službách, které mohou zaznamenávat činnost. Získává se plná kontrola nad transakcemi, což umožňuje jejich vysílání přímo do sítě. Výchozí volbou je `Bitcoin Core`, která se nativně integruje se systémem StartOS a umožňuje propojení s peněženkami, jako jsou Specter, Sparrow nebo Electrum, pro nastavení vlastní úschovy. Prostřednictvím registru komunity je k dispozici také alternativní varianta `Bitcoin Knots`.


Chcete-li nainstalovat jádro Bitcoin, přejděte na tržiště. Ve výchozím registru vyhledejte a nainstalujte službu Bitcoin Core. Po instalaci se zobrazí výzva `Needs Config`, která vyžaduje dokončení nastavení před spuštěním služby. K tomu obvykle dochází po aktualizacích nebo čerstvých instalacích a je požadována kontrola `Nastavení RPC`. Pokračujte ve výchozí konfiguraci a klikněte na tlačítko `Uložit`.


![image](assets/en/13.webp)


Po úplné synchronizaci může váš uzel sloužit jako privátní backend pro peněženky, jako je Sparrow, a poskytovat tak větší soukromí a ověřování transakcí. Pro uživatele, kteří ukládají významné částky, je však zásadní pochopit bezpečnostní kompromisy tohoto přímého připojení. Při přímém připojení wallet k jádru Bitcoin může dojít k odhalení citlivých údajů, protože jádro Bitcoin ukládá veřejné klíče (xpubs) a zůstatky wallet nešifrovaně na hostitelském počítači. Kompromitovaný systém by mohl útočníkovi umožnit zjistit vaše podíly a zaměřit se na vás.


Chcete-li toto riziko zmírnit a dosáhnout robustnějšího modelu zabezpečení, můžete nastavit privátní službu Electrum Server. Tento server funguje jako prostředník, který indexuje blockchain, aniž by ukládal jakékoli informace specifické pro wallet. Připojením wallet k vlastnímu serveru Electrum namísto přímo k jádru Bitcoin zabráníte wallet v přístupu k citlivým datům uzlu.


![image](assets/en/14.webp)


## 🔟 Nastavení elektra


`electrs` (Electrum Rust Server) je rychlý a efektivní indexer, který se připojuje k uzlu Bitcoin Core a umožňuje peněženkám kompatibilním s Electrum dotazovat se na historii transakcí a zůstatky v reálném čase. Spuštěním systému electrs v systému StartOS eliminujete závislost na serverech Electrum třetích stran, což výrazně zvyšuje soukromí a bezpečnost - vaše dotazy na wallet směřují přímo do vašeho samostatně hostovaného uzlu.


Chcete-li ji nastavit, nejprve nainstalujte službu electrs z tržiště StartOS Marketplace. Systém bude před pokračováním vyžadovat úplnou synchronizaci s jádrem Bitcoin. Po instalaci potvrďte nastavení `Needs Config` doporučenými výchozími hodnotami a electrs začne indexovat blockchain, což může trvat až jeden den v závislosti na vašem hardwaru.


![image](assets/en/15.webp)


Po dokončení můžete připojit peněženky jako Sparrow nebo Specter. Úspěšné připojení umožní synchronizaci wallet přímo s vaším uzlem, čímž získáte bezpečný, soukromý a samostatný hosting Bitcoin.


## 1️⃣1️⃣ Connect Sparrow Wallet


Chcete-li připojit `Sparrow Wallet` k uzlu StartOS pomocí implementace electrs, ujistěte se nejprve, že je jádro Bitcoin plně synchronizováno a že je nainstalován a spuštěn electrs. Otevřete Sparrow Wallet na svém zařízení a přejděte do `Soubor` -> `Nastavení` -> `Server`. Poté zvolte `Soukromý Electrum Server`. Do pole URL zadejte `název hostitele` a `port` pro electrs, který najdete v systému StartOS v části `Services` -> `electrs` -> `Vlastnosti` (obvykle končí na `.onion:50001`).


![image](assets/en/16.webp)


Poté povolte Tor zaškrtnutím políčka `Použít proxy server`, nastavte adresu proxy serveru na `127.0.0.1` a port na `9050`. Klikněte na `Test Connection` a chvíli počkejte. Při úspěšném připojení se zobrazí potvrzovací zpráva, například `Connected to electrs`. Po ověření zavřete nastavení a pokračujte ve vytváření nebo obnovení wallet. Toto nastavení zajišťuje, že se váš wallet dotazuje na váš vlastní uzel prostřednictvím electrs, což poskytuje plné soukromí a provoz bez důvěry.


![image](assets/en/17.webp)


## 🎯 Závěr


StartOS od Start9 je uživatelsky přívětivá platforma zaměřená na ochranu soukromí, která je určena pro vlastní hostování základních služeb, jako jsou uzly Bitcoin a Lightning, peněženky a osobní aplikace. Díky přehlednému grafickému rozhraní, automatickému zálohování, monitorování stavu a bezpečnému přístupu na Tor eliminuje potřebu znalosti příkazového řádku, takže je ideální pro netechnické uživatele. Jeho modulární architektura podporuje bezproblémovou integraci s nástroji, jako jsou electrs nebo Sparrow, a poskytuje vám tak plnou kontrolu nad vaší finanční a digitální suverenitou. Díky silnému důrazu na transparentnost, místní kontrolu a rozšiřitelnost umožňuje StartOS uživatelům získat zpět vlastnictví od centralizovaných platforem a provozovat vlastní soukromou, odolnou infrastrukturu.