---
name: Qubes
description: Poměrně bezpečný operační systém.
---

![cover](assets/cover.webp)



Qubes OS je svobodný operační systém s otevřeným zdrojovým kódem určený pro uživatele, kteří kladou bezpečnost na první místo svých priorit. Jeho zvláštnost je založena na jednoduché, ale radikální myšlence: místo toho, aby se na počítač pohlíželo jako na celek, rozděluje jeho používání na nezávislé oddíly nazývané **_qubes_**.



Každý qube funguje jako **izolované virtuální prostředí** se specifickou úrovní důvěryhodnosti a funkcí. Takže i když je aplikace kompromitována, útok zůstane omezen na její qube, aniž by ovlivnil zbytek systému.



> Pokud vám záleží na bezpečnosti, je Qubes OS nejlepším operačním systémem současnosti. - **Edward Snowden**.

Instalace systému Qubes OS však vyžaduje více příprav než instalace běžného operačního systému. Vyžaduje ověření určitých hardwarových předpokladů, pochopení základů virtualizace a přijetí odlišné zkušenosti, kdy se na každý každodenní úkol myslí odděleně. Jakmile je však systém Qubes OS nasazen, nabízí robustní rámec, který nově definuje způsob každodenní interakce s počítačem. V tomto návodu vám vysvětlíme, jak systém Qubes OS funguje a jak jej snadno nainstalovat do vašeho systému.



## Jak systém Qubes OS funguje?



Systém Qubes OS je založen na principu kompartmentalizace. Namísto použití jediného systému se spoléhá na hypervizor **Xen** a vytváří izolované virtuální stroje, tzv. qubes. Každý qube je vyhrazen pro určitý úkol nebo úroveň důvěryhodnosti (práce, osobní prohlížení, bankovnictví atd.). Toto oddělení zajišťuje, že se případné kompromitace v jednom qube nemohou rozšířit do ostatních a fungují jako několik nezávislých počítačů v rámci jednoho stroje.



Uživatel Interface je spravován centrální zabezpečenou doménou s názvem **dom0**. Tato doména je zcela izolována od internetu a je srdcem systému. Přestože okna a nabídky jsou zobrazovány doménou dom0, skutečné spouštění aplikací probíhá v jejich příslušných qubech.



## Různé typy qubes



Kolem dom0 se točí různé typy qubes, z nichž každý má velmi specifickou úlohu.





- **AppVM** slouží ke spouštění každodenních aplikací: uživatel tak může oddělit své pracovní e-maily od prohlížení webu nebo bankovních činností, přičemž každé prostředí zůstává zcela nezávislé na ostatních.





- Tyto moduly AppVM jsou samy založeny na modulech **TemplateVM**, které slouží jako centralizované šablony pro instalaci a aktualizaci softwaru, čímž odpadá nutnost spravovat každý modul qube zvlášť.



Qubes OS také integruje virtuální stroje specializované na **systémové služby**.





- Systém **NetVM** přímo spravuje **síťová zařízení** a zajišťuje připojení k internetu. Často jsou spojeny s **FirewallVM**, které zasahují do **filtrace provozu** a omezují působení dalších qubů.





- Podobnou roli hrají ServiceVM například při správě zařízení USB, a to vždy se stejnou logikou: izolovat nejrizikovější součásti, aby se zmenšil povrch útoku.



A konečně, pro příležitostné nebo rizikové úlohy nabízí Qubes OS **DisposableVM**. Tyto efemérní quby se vytvářejí za běhu pro **otevření podezřelého dokumentu** nebo **návštěvu pochybné stránky** a po zavření zcela zmizí, čímž se vymažou všechny stopy a zabrání se jakémukoli trvalému útoku.



### Mechanismus zabezpečeného kopírování (qrexec)



Výměny mezi qubes jsou založeny na **qrexec**, komunikačním systému mezi virtuálními počítači navrženém pro zabezpečení. Namísto volné komunikace qubů zavádí qrexec **specifické zásady**: soubor kopírovaný z jednoho AppVM do druhého nebo text přenášený přes schránku vždy prochází kanálem sledovaným a ověřovaným systémem. Tímto způsobem je kontrolován i prostý akt kopírování a vkládání, aby se zabránilo šíření malwaru.



### Správa disků



Systém Qubes OS používá důmyslný systém správy úložišť. Moduly TemplateVM obsahují společný softwarový základ, zatímco moduly AppVM přidávají pouze svá osobní data a specifické soubory. Tím se snižuje využití místa na disku a usnadňují se globální aktualizace. DisposableVMs naproti tomu používají dočasné svazky, které po uzavření zcela zmizí. Tento model zaručuje nejen vyšší bezpečnost, ale také efektivní správu zdrojů.



## Proč si vybrat operační systém Qubes?



Výhody systému Qubes OS spočívají především v jeho jedinečném bezpečnostním modelu. Jádrem tohoto přístupu je kompartmentalizace, která chrání uživatele tím, že jednotlivé úlohy izoluje v samostatných virtuálních strojích. V praxi to znamená, že infikovaný e-mail nebo škodlivá webová stránka může ohrozit pouze jeden qube, přičemž zbytek systému a vaše osobní údaje jsou plně chráněny. Tato architektura výrazně omezuje komplexní útoky, které by se v běžném systému mohly volně šířit.



Qubes OS také nabízí naprostou transparentnost a kontrolu nad digitálním prostředím. Přesně víte, který software má přístup k jakému zdroji, ať už se jedná o síť, zařízení USB nebo jiné citlivé komponenty. Systém ve výchozím nastavení integruje pokročilé funkce zabezpečení, jako je úplné šifrování disku, a usnadňuje používání anonymizačních služeb, jako je operační systém Whonix.



https://planb.network/tutorials/computer-security/operating-system/whonix-06f9172c-2962-412e-9487-b665d8ca9f59

Systém Qubes OS se nesnaží vytvořit neproniknutelný systém, ale zaměřuje se na odolnost: v případě kompromitace zapouzdřuje škody a snižuje tak riziko pro zbytek systému. Díky tomuto pragmatickému přístupu je systém Qubes OS preferovanou volbou pro uživatele s vysokými nároky na zabezpečení nebo pro ty, kteří si chtějí zachovat maximální kontrolu nad svým digitálním životem.



## Instalace operačního systému Qubes



Před instalací operačního systému Qubes je nutné se ujistit, že váš hardware splňuje minimální požadavky, protože systém se spoléhá na virtualizaci, aby izoloval qubes. Hlavní komponenty, které je třeba zkontrolovat, jsou :




- **Procesor**: 64bitový procesor kompatibilní s hardwarovou virtualizací (Intel VT-x nebo AMD-V).
- Paměť RAM: je vyžadováno minimálně 8 GB, ale doporučujeme 16 GB nebo více, abyste mohli spustit několik qubů současně.
- Úložný prostor**: minimálně 36 GB, ideálně 128 GB na disku SSD pro optimální výkon.



Chcete-li nainstalovat systém Qubes OS, stáhněte si oficiální obraz ISO ze stránky Qubes OS [oficiální stránka](https://www.qubes-os.org/downloads/). Je nezbytné zkontrolovat integritu ISO pomocí dodaných podpisů GPG, abyste se ujistili, že se souborem nebylo manipulováno a že je stažení bezpečné.



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

![0_01](assets/fr/01.webp)



Po ověření ISO je třeba vytvořit zaváděcí instalační médium, obvykle USB disk. Za tímto účelem si stáhněte a nainstalujte software, například **Rufus** pro systém Windows nebo **Etcher** pro systémy Windows, Linux nebo MacOS. Tyto nástroje umožňují zkopírovat ISO na USB disk tak, aby byl spustitelný.



Před zahájením instalace je nutné nakonfigurovat **BIOS nebo UEFI** počítače tak, aby **povolil virtualizaci** a start z USB. V závislosti na modelu počítače může být nutné **zakázat Secure Boot**, protože systém Qubes OS se zapnutou touto volbou nemusí spustit.



![0_02](assets/fr/02.webp)



Po splnění těchto podmínek restartujte počítač a vstupte do systému BIOS/UEFI okamžitým stisknutím tlačítek **Esc**, **Del**, **F9**, **F10**, **F11** nebo **F12** (v závislosti na výrobci). Ve spouštěcí nabídce vyberte jako spouštěcí zařízení klíč USB a spusťte instalaci operačního systému Qubes.



**Startovací obrazovka**


Při spouštění z paměti USB se dostanete přímo do nabídky **GRUB**, kde můžete vybrat akci, která se má provést. Pomocí kláves se šipkami na klávesnici vyberte možnost "Install Qubes OS" a stiskněte klávesu "Enter".



![0_03](assets/fr/03.webp)



**Volba jazyka** :



Po spuštění instalace je třeba nejprve **vybrat jazyk** a **regionální variantu** vhodné pro vaši konfiguraci. Tím zajistíte, že se systém a možnosti instalace zobrazí správně ve vámi preferovaném jazyce.



![0_04](assets/fr/04.webp)



**Konfigurace parametrů** :



V této fázi budete muset před spuštěním instalace v počítači nakonfigurovat řadu Elements.



![0_05](assets/fr/05.webp)



**Rozložení klávesnice** :



Klikněte na možnost **Klávesnice** a poté vyberte **vhodné rozložení** pro váš počítač. Po výběru přejděte k dalšímu kroku kliknutím na tlačítko **Ukončeno**.



**Volba destinace** :



Výběrem možnosti "Cíl instalace" vyberte disk, na který chcete nainstalovat operační systém Qubes. Ve výchozím nastavení proběhne rozdělení disku automaticky, což vám umožní odstranit z disku všechna data a nainstalovat na něj systém. Můžete však zvolit možnost **Přizpůsobené** nebo **Pokročilé přizpůsobení** a provést vlastní rozdělení disku. Poté klikněte na tlačítko "Hotovo". Systém vás požádá o nastavení **hesla**, které slouží jako bezpečnostní kód Layer pro šifrování dat. Nezapomeňte zvolit složité a jedinečné heslo.



![0_06](assets/fr/06.webp)



![0_07](assets/fr/07.webp)



**Vyberte formát data a času** :


Klikněte na možnost Čas a datum a vyberte zeměpisnou zónu. Můžete také zvolit preferovaný formát času: můžete zvolit 24hodinový nebo 12hodinový čas.



![0_08](assets/fr/08.webp)



**Vytvoření uživatelského účtu** :


Kliknutím na **Vytvořit uživatele** vytvoříte svůj **první účet**, který vám umožní přihlásit se do systému Qubes OS.



![0_09](assets/fr/09.webp)



**Aktivace účtu root** :


Můžete také **povolit účet root** nastavením samostatného hesla pro správu.



![0_10](assets/fr/10.webp)



Po provedení těchto nastavení klikněte na tlačítko **Spustit instalaci**, čímž zahájíte proces instalace.



![0_11](assets/fr/11.webp)



Vyčkejte na **konec instalace** a poté kliknutím na **restartovat systém** dokončete instalaci a spusťte operační systém Qubes.



![0_12](assets/fr/12.webp)



**Další konfigurace** :


Po restartu vás operační systém Qubes vyzve k dokončení **výchozích šablon a konfigurace qubes**. Zadejte heslo definované pro šifrování disku.



![0_13](assets/fr/13.webp)



Poté začněte výběrem **ŠablonyVM**, kterou chcete nainstalovat. Mezi běžné možnosti patří **Debian 12 Xfce**, **Fedora 41 Xfce** a **Whonix 17**, přičemž posledně jmenovaný je doporučován pro použití vyžadující **anonymitu a zabezpečení sítě**. Můžete také definovat **výchozí šablonu**, která bude sloužit jako základ pro vytváření nových **AppVM**.



![0_14](assets/fr/14.webp)



V části **Hlavní konfigurace** můžete zvolit automatické vytvoření základních systémových qubů, jako jsou **sys-net**, **sys-firewall** a **výchozí DisposableVM**. Doporučujeme povolit možnost, aby byly **sys-firewall a sys-usb jednorázové**, aby se omezilo vystavení zařízení a sítě v případě kompromitace. Můžete také vytvořit výchozí **AppVM**, například **personal**, **work**, **untrusted** a **vault**, a uspořádat tak své aktivity podle úrovně jejich důvěryhodnosti.



![0_15](assets/fr/15.webp)



Qubes OS také umožňuje vytvořit **qube vyhrazený pro zařízení USB** (sys-usb) a nakonfigurovat **Whonix Gateway a Workstation qubes** pro zabezpečení komunikace prostřednictvím sítě Tor. Pokročilým uživatelům umožňuje část **Pokročilá konfigurace** vytvořit **LVM thin pool** pro efektivní správu diskového prostoru mezi qubes.



Po nastavení všech těchto možností klikněte na tlačítko **Dokončit** a poté na tlačítko **Dokončit konfiguraci**. Počkejte, než systém provede tato nastavení. Poté budete vyzváni k **přihlášení k uživatelskému účtu** a vaše prostředí Qubes OS bude připraveno k použití, zabezpečené a řádně izolované pro různé činnosti.



![0_17](assets/fr/17.webp)



Váš operační systém je nyní nainstalován a připraven k použití.



![0_18](assets/fr/18.webp)



## Vytvoření qube v systému



Vytvoření kostky se řídí nástrojem **Qube Manager**, který je přístupný z nabídky Start. V okně nástroje stačí kliknout na ikonu **Vytvořit qube** a otevře se nové konfigurační okno. Nejprve zadejte název qube, například "perso-web" nebo "work", abyste identifikovali jeho použití.



Dále vyberete jeho **Typ**, obvykle **AppVM** pro běžné úlohy nebo **DisposableVM** pro dočasné použití. Zásadní je zvolit **Šablonu**, na které bude qube založen, například "fedora-39" nebo "debian-12", protože ta poskytne operační systém a software. Dále určíte **NetVM**, což je qube zodpovědný za přístup k internetu, ve výchozím nastavení **sys-firewall**.



Po případném nastavení velikosti úložiště a operační paměti nakonec jednoduchým kliknutím na **OK** spustíte proces vytváření. Po dokončení procesu bude vaše nová kostka viditelná v seznamu a připravená k použití.



Závěrem lze říci, že Qubes OS není obyčejný operační systém, ale špičkové bezpečnostní řešení, které přehodnocuje architekturu osobního počítače. Jeho přístup, založený na rozdělení a izolaci prostřednictvím virtualizace, nabízí bezkonkurenční ochranu před nejsofistikovanějšími hrozbami. Díky segmentaci pracovního prostředí na specializované quby pro jednotlivé úlohy zajišťuje, že se malware nemůže šířit a ohrozit celý systém.



Ať už potřebujete bezpečně surfovat po webu, chránit citlivé informace nebo pracovat s různými úrovněmi důvěryhodnosti, Qubes OS poskytuje odolný a transparentní rámec. Osvojením správných postupů a plným využitím jeho funkcí získáte **digitální pevnost** přizpůsobenou moderním hrozbám. Přečtěte si více o ochraně svých dat a soukromí.



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1