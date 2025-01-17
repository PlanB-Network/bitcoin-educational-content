---
name: RoninDojo v2
description: Instalace vašeho Bitcoinového uzlu RoninDojo v2 na Raspberry Pi
---
![obal RoninDojo v2](assets/cover.webp)

***VAROVÁNÍ:** Po zatčení zakladatelů peněženky Samourai a zabavení jejich serverů dne 24. dubna jsou některé funkce RoninDojo, jako je Whirlpool, již nefunkční. Je však možné, že tyto nástroje budou v nadcházejících týdnech obnoveny nebo znovu spuštěny jiným způsobem. Navíc, protože kód RoninDojo byl hostován na GitLabu Samourai, který byl také zabaven, v současné době není možné kód vzdáleně stáhnout. Týmy RoninDojo pravděpodobně pracují na znovu publikování kódu.*

_Pozorně sledujeme vývoj této kauzy i vývoj s ní spojených nástrojů. Ujistěte se, že tento návod aktualizujeme, jakmile budou k dispozici nové informace._

_Tento návod je poskytován pouze pro vzdělávací a informační účely. Nepodporujeme ani nevyzýváme k používání těchto nástrojů pro kriminální účely. Je zodpovědností každého uživatele dodržovat zákony ve své jurisdikci._

---

> "*Používejte Bitcoin soukromě.*"

V předchozím návodu jsme již vysvětlili postup instalace a používání RoninDojo v1. Během posledního roku však týmy RoninDojo spustily verzi 2 své implementace, což představovalo významný obrat v architektuře softwaru. Skutečně se odvrátili od distribuce Linux Manjaro ve prospěch Debianu. V důsledku toho již nenabízejí předkonfigurovaný obraz pro automatickou instalaci na Raspberry Pi. Existuje však stále metoda, jak pokračovat v ruční instalaci. Toho jsem využil pro svůj vlastní uzel a od té doby RoninDojo v2 na mém Raspberry Pi 4 funguje báječně. Proto nabízím nový návod, jak ručně nainstalovat RoninDojo v2 na Raspberry Pi.

https://planb.network/tutorials/node/bitcoin/ronin-dojo-31d96647-029b-43e8-9fb5-95ec5dde72b0



## Obsah:
- Co je RoninDojo?
- Jaký hardware vybrat pro instalaci RoninDojo v2?
- Jak sestavit Raspberry Pi 4?
- Jak nainstalovat RoninDojo v2 na Raspberry Pi 4?
- Jak používat váš uzel RoninDojo v2?

## Co je RoninDojo?
Dojo je původně plná implementace Bitcoinového uzlu, založená na Bitcoin Core, a vyvinutá týmy peněženky Samourai. Toto řešení lze nainstalovat na jakékoli zařízení. Na rozdíl od jiných implementací Core bylo Dojo specificky optimalizováno pro integraci s prostředím Android aplikace Samourai Wallet. Co se týče RoninDojo, jedná se o nástroj navržený k usnadnění instalace a správy Dojo, stejně jako různých dalších doplňkových nástrojů. Stručně řečeno, RoninDojo obohacuje základní implementaci Dojo integrací množství dalších nástrojů, zatímco zjednodušuje jeho instalaci a správu.

Ronin také nabízí [řešení uzlu v krabici, nazvané "*Tanto*"](https://ronindojo.io/en/products), zařízení s již nainstalovaným RoninDojo na systému sestaveném jejich týmem. Tanto je placená možnost, která může být zajímavá pro ty, kteří se chtějí vyhnout technickým komplikacím. Ale protože zdrojový kód RoninDojo je otevřený, je také možné jej nasadit na vlastním hardwaru. Tato alternativa, ekonomičtější, nicméně vyžaduje některé další manipulace, které v tomto návodu pokryjeme.
RoninDojo je Dojo, což umožňuje snadnou integraci Whirlpool CLI do vašeho Bitcoinového uzlu, aby poskytl co nejlepší zážitek z coinjoin. S Whirlpool CLI je možné neustále míchat vaše bitcoiny, 24 hodin denně, 7 dní v týdnu, aniž by bylo nutné, aby váš osobní počítač zůstal zapnutý.
Kromě Whirlpool CLI zahrnuje RoninDojo řadu nástrojů pro rozšíření funkcionalit vašeho Doja. Mezi ně patří kalkulačka Boltzmann, která analyzuje úroveň soukromí vašich transakcí, Electrum server umožňuje připojení vašich Bitcoinových peněženek k vašemu uzlu a Mempool server umožňuje lokální zobrazení vašich transakcí, aniž by docházelo k úniku informací.

Ve srovnání s jinými řešeními uzlů, jako je Umbrel, je RoninDojo jasně zaměřen na on-chain řešení a nástroje pro soukromí. Na rozdíl od Umbrelu RoninDojo nepodporuje nastavení Lightning uzlu ani integraci více všeobecných serverových aplikací. Ačkoli RoninDojo nabízí méně univerzálních nástrojů než Umbrel, má všechny základní funkce pro správu vaší on-chain aktivity.

Pokud nepotřebujete všeobecné funkce nebo ty související s Lightning Network, jak nabízí Umbrel, a hledáte jednoduchý, stabilní uzel se základními nástroji, jako jsou Whirlpool nebo Mempool, RoninDojo by mohlo být ideálním řešením. Zatímco Umbrel směřuje k mini multitaskingovému serveru orientovanému na Lightning Network a univerzálnost, RoninDojo, v souladu s filozofií Samourai Wallet, se zaměřuje na základní nástroje pro soukromí uživatele.

Nyní, když jsme představili RoninDojo, pojďme se společně podívat, jak tento uzel nastavit.

## Jaký hardware vybrat pro instalaci RoninDojo v2?
RoninDojo nabízí obraz pro automatickou instalaci svého softwaru na [RockPro64](https://ronindojo.io/en/download). Nicméně, náš tutoriál se zaměřuje na manuální instalační proceduru na Raspberry Pi 4. Ačkoli byl nedávno spuštěn Raspberry Pi 5 a tento tutoriál by teoreticky měl být kompatibilní s tímto novým modelem, osobně jsem jej ještě neměl šanci otestovat a od komunity jsem nenašel žádnou zpětnou vazbu. Jakmile získám Pi 5 a kompatibilní komponenty, aktualizuji tento tutoriál, abych vás informoval. Mezitím doporučuji dát přednost Pi 4, protože pro můj uzel funguje perfektně.
Z mé strany provozuji RoninDojo na Raspberry Pi vybaveném 8 GB RAM. Ačkoli někteří členové komunity dokázali zprovoznit zařízení pouze s 4 GB RAM, tuto konfiguraci jsem osobně netestoval. Vzhledem k malému cenovému rozdílu se zdá být rozumné zvolit verzi s 8 GB RAM. To by se také mohlo ukázat jako užitečné, pokud plánujete v budoucnu svůj Raspberry Pi využít pro jiné účely.
Je důležité poznamenat, že týmy RoninDojo hlásily časté problémy související s pouzdrem a adaptérem SSD. S těmito problémy jsem se setkal i já. **Proto se důrazně doporučuje vyhnout pouzdrům vybaveným USB kabelem pro SSD vašeho uzlu.** Místo toho preferujte kartu pro rozšíření úložiště speciálně navrženou pro vaše Raspberry Pi:

![storage expansion card RPI4](assets/notext/1.webp)
Pro uložení Bitcoin blockchainu budete potřebovat SSD kompatibilní s rozšiřující kartou pro úložiště, kterou jste si vybrali. Aktuálně (únor 2024) jsme ve fázi přechodu. Očekává se, že za několik měsíců již 1 TB disky nebudou dostatečné pro obsažení rostoucí velikosti blockchainu, zvláště pokud vezmeme v úvahu různé aplikace, které plánujete do vašeho uzlu integrovat. Někteří proto doporučují investovat do 2 TB SSD pro klid na dlouhou dobu. Avšak s ročním poklesem cen SSD, jiní navrhují spokojit se s 1 TB diskem, který by měl stačit na jeden nebo dva roky, s argumentem, že do doby, kdy se stane zastaralým, pravděpodobně klesnou ceny 2 TB modelů. Volba tedy závisí na vašich osobních preferencích. Pokud plánujete udržet váš RoninDojo po významnou dobu a chcete se vyhnout jakékoliv technické manipulaci v nadcházejících letech, volba 2 TB SSD se jeví jako nejrozumnější, jelikož vám nabízí pohodlnou rezervu do budoucna.
Kromě toho budete potřebovat různé malé komponenty:
- Pouzdro vybavené ventilátorem pro umístění vašeho Raspberry Pi a vaší rozšiřující karty pro úložiště. Na internetu jsou dostupné sady obsahující jak rozšiřující kartu SSD, tak kompatibilní pouzdro;
- Napájecí kabel pro vaše Raspberry Pi;
- Micro SD kartu o kapacitě alespoň 16 GB (i když technicky by stačilo 8 GB, cenový rozdíl mezi 8 a 16 GB kartami je často zanedbatelný);
- RJ45 Ethernetový kabel pro síťové připojení.

![node material](assets/notext/2.webp)

## Jak sestavit Raspberry Pi 4?
Sestavení vašeho uzlu se bude lišit v závislosti na vybraném hardware, zejména na typu pouzdra. Obecný nástin kroků, které je třeba následovat, zůstává však obecně podobný.
Začněte instalací vašeho SSD na rozšiřující kartu pro úložiště, přičemž si dejte pozor na zajištění obou uzamykacích šroubů na zadní straně.

![assembly1](assets/notext/3.webp)

Poté připevněte vaše Raspberry Pi k rozšiřující kartě.

![assembly2](assets/notext/4.webp)

Také připevněte ventilátor k Raspberry Pi.

![assembly3](assets/notext/5.webp)

Připojte různé komponenty, přičemž věnujte pozornost správnému použití pinů, odkazujte se na manuál vašeho pouzdra. Výrobci pouzder často nabízejí video tutoriály, které vám pomohou při sestavení. V mém případě mám dodatečnou rozšiřující kartu vybavenou tlačítkem zapnutí/vypnutí. To není pro vytvoření Bitcoin uzlu nezbytné. Hlavně to používám pro mít tlačítko pro zapnutí.

Pokud, jako já, máte rozšiřující kartu vybavenou tlačítkem zapnutí/vypnutí, nezapomeňte nainstalovat malý jumper "Auto Power On". To umožní vašemu uzlu automaticky se spustit, jakmile je napájen. Tato funkce je zvláště užitečná v případě výpadku proudu, jelikož umožňuje vašemu uzlu restartovat samostatně, bez manuálního zásahu z vaší strany.

![assembly4](assets/notext/6.webp)

Před vložením veškerého hardware do pouzdra je důležité zkontrolovat správnou funkčnost vašeho Raspberry Pi, rozšiřující karty pro úložiště a ventilátoru zapnutím.

![assembly5](assets/notext/7.webp)
Nakonec nainstalujte svůj Raspberry Pi do jeho pouzdra. Mějte na paměti, že v pozdějším kroku bude nutné vložit micro SD kartu do příslušného portu na Raspberry Pi. Pokud je vaše pouzdro vybaveno otvorem, který umožňuje vložit SD kartu bez nutnosti otevírání pouzdra (jak je tomu u mého, ilustrovaného na fotografii), můžete pouzdro nyní zavřít. Pokud však vaše pouzdro nemá přímý přístup k portu micro SD, budete muset počkat, až připravíte micro SD kartu, než ji vložíte před dokončením montáže.
![assembly6](assets/notext/8.webp)

## Jak nainstalovat RoninDojo v2 na Raspberry Pi 4?

### Krok 1: Příprava bootovatelné micro SD
Po sestavení vašeho hardware je dalším krokem instalace RoninDojo. K tomu připravíme bootovatelnou micro SD kartu z vašeho počítače vypálením příslušného diskového obrazu na ni.
Budete potřebovat použít software _**Raspberry Pi Imager**_, který je navržen k usnadnění stahování, konfigurace a zápisu operačních systémů na micro SD kartu pro použití s Raspberry Pi. Začněte instalací tohoto softwaru na váš osobní počítač:
- Pro Ubuntu/Debian: https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb
- Pro Windows: https://downloads.raspberrypi.org/imager/imager_latest.exe
- Pro Mac: https://downloads.raspberrypi.org/imager/imager_latest.dmg

Jakmile je software nainstalován, otevřete ho a vložte vaši micro SD kartu do vašeho osobního počítače. Z rozhraní Raspberry Pi Imager vyberte `CHOOSE OS`:

![choose OS](assets/notext/9.webp)

Dále přejděte do menu `Raspberry Pi OS (other)`:

![choose OS others](assets/notext/10.webp)

Vyberte operační systém pojmenovaný `Raspberry Pi OS (Legacy, 64-bit) Lite`, který má velikost `0.3 GB`:

![choose OS Legacy Lite](assets/notext/11.webp)

Po výběru operačního systému budete přesměrováni do hlavního menu Raspberry Pi Imager. Klikněte na `CHOOSE STORAGE`:

![choose storage](assets/notext/12.webp)

Vyberte vaši micro SD kartu:

![choose micro sd](assets/notext/13.webp)

Po výběru operačního systému a micro SD karty klikněte na `NEXT`:

![choose next](assets/notext/14.webp)

Objeví se nové okno. Vyberte `EDIT CONFIGURATION`:

![edit settings](assets/notext/15.webp)

V tomto okně přejděte na kartu `GENERAL` a proveďte následující nastavení (která jsou velmi důležitá pro jeho fungování):
- Povolte možnost a přiřaďte `RoninDojo` jako hostname;
- Povolte `Set username and password`, zadejte `pi` jako uživatelské jméno, vyberte heslo a poznamenejte si tyto informace, protože budou později potřeba. Tyto přihlašovací údaje jsou dočasné a budou později smazány;
- Zakázat `Configure Wi-Fi`;
- Povolte `Set locale settings` a vyberte vaše časové pásmo i typ klávesnice odpovídající vašemu počítači;

![general settings](assets/notext/16.webp)

Na kartě SERVICES zaškrtněte políčko `Enable SSH` a vyberte `Use a password for authentication`:

![services settings](assets/notext/17.webp)

Také se ujistěte, že na kartě `OPTIONS` je telemetrie zakázána:

![options settings](assets/notext/18.webp)

Klikněte na `SAVE`:
![nastavení uložit](assets/notext/19.webp)Potvrďte kliknutím na `YES` pro zahájení vytváření bootovací micro SD karty:
![nastavení ano](assets/notext/20.webp)

Zpráva vás informuje, že všechna data na micro SD kartě budou smazána. Potvrďte kliknutím na `YES` pro zahájení procesu:

![přepsání micro SD](assets/notext/21.webp)

Počkejte, dokud software nedokončí přípravu vaší micro SD karty:

![zápis micro SD](assets/notext/22.webp)

Když se objeví zpráva oznamující konec procesu, můžete micro SD kartu vyjmout z počítače:

![zápis micro SD dokončen](assets/notext/23.webp)

### Krok 2: Dokončení sestavení uzlu
Nyní můžete vložit micro SD kartu do příslušného portu vašeho Raspberry Pi.

![micro SD](assets/notext/24.webp)

Poté připojte vaše Raspberry Pi k routeru pomocí Ethernetového kabelu. Nakonec zapněte váš uzel připojením napájecího kabelu a stisknutím tlačítka napájení (pokud vaše sestava jedno obsahuje).

### Krok 3: Navázání SSH spojení s uzlem
Nejprve je nutné najít IP adresu vašeho uzlu. Můžete použít nástroj jako _[Advanced IP Scanner](https://www.advanced-ip-scanner.com/)_ nebo _[Angry IP Scanner](https://angryip.org/)_, nebo zkontrolovat administrační rozhraní vašeho routeru. IP adresa by měla být ve formátu `192.168.1.??`. **Pro všechny následující příkazy nahraďte `[IP]` skutečnou IP adresou vašeho uzlu**, (odeberte závorky).

Spusťte terminál.

Pro odstranění možného klíče již spojeného s IP adresou vašeho uzlu, proveďte příkaz: 
`ssh-keygen -R [IP]`. 

Chyba po tomto příkazu není vážná; jednoduše to znamená, že klíč neexistuje ve vašem seznamu známých hostitelů (což je celkem pravděpodobné). Například, pokud je IP vašeho uzlu `192.168.1.40`, příkaz se stane: `ssh-keygen -R 192.168.1.40`.

Dále navážte SSH spojení s vaším uzlem provedením příkazu: 
`ssh pi@[IP]`.
Objeví se zpráva týkající se autenticity hostitele: `The authenticity of host '[IP]' can't be established.` To znamená, že autenticita zařízení, ke kterému se snažíte připojit, nemůže být ověřena kvůli nedostatku známého veřejného klíče. Při prvním SSH připojení k novému hostiteli se tato zpráva vždy objeví. Musíte odpovědět `yes` pro přidání jeho veřejného klíče do vašeho lokálního adresáře, což zabrání zobrazení tohoto varovného hlášení při budoucích SSH spojeních s tímto uzlem. Proto napište `yes` a stiskněte `enter` pro potvrzení.
Poté budete vyzváni k zadání vašeho hesla, toho, které bylo dříve nastaveno jako dočasné v kroku 1. Potvrďte stisknutím `enter`. Nyní jste připojeni k vašemu uzlu přes SSH.

Shrnutí, zde jsou příkazy k provedení:
- `ssh-keygen -R [IP]`
- `ssh pi@[IP]`
- `yes`
- Zadejte dočasné heslo a potvrďte.

### Krok 4: Aktualizace a příprava
Nyní jste připojeni k vašemu uzlu přes SSH sezení. Na vašem terminálu by výzva příkazu měla být: `pi@RoninDojo:~ $`. Pro začátek aktualizujte seznam dostupných balíčků a nainstalujte aktualizace pro stávající balíčky s následujícím příkazem:
`sudo apt update && sudo apt upgrade -y`
Jakmile budou aktualizace dokončeny, pokračujte v instalaci *Git* a *Dialog* pomocí příkazu: `sudo apt install git dialog -y`

Dále naklonujte větev `master` Git repozitáře _RoninOS_ spuštěním:
`sudo git clone --branch master https://code.samourai.io/ronindojo/RoninOS.git /opt/RoninOS`

Spusťte skript `customize-image.sh` s příkazem:
`cd /opt/RoninOS/ && sudo ./customize-image.sh`

**Je důležité nechat skript běžet bez přerušení a trpělivě čekat na konec jeho procesu**, což trvá přibližně 10 minut. Když se objeví zpráva `Setup is complete`, můžete přejít k dalšímu kroku.

### Krok 5: Spuštění RoninOS
Spusťte RoninOS příkazem:
`sudo systemctl start ronin-setup`

Zobrazte řádky log souboru příkazem:
`tail -f /home/ronindojo/.logs/setup.logs`

V této fázi **je důležité nechat RoninOS spustit a počkat na jeho dokončení**. To trvá přibližně 40 minut. Když se objeví `All RoninDojo feature installations complete!`, můžete přejít k kroku 6.

### Krok 6: Přístup k RoninUI a změna přihlašovacích údajů
Po dokončení instalace, pro připojení k vašemu uzlu přes prohlížeč, se ujistěte, že váš osobní počítač je připojen k téže lokální síti jako váš uzel. Pokud na vašem stroji používáte VPN, dočasně ji vypněte. Pro přístup k rozhraní uzlu ve vašem prohlížeči zadejte do adresního řádku:
- Přímo IP adresu vašeho uzlu, například `192.168.1.??`;
- Nebo napište `ronindojo.local`.

Po přechodu na domovskou stránku RoninUI budete vyzváni k zahájení nastavení. K tomu klikněte na tlačítko `Let's start`.

![lets start](assets/notext/25.webp)

V této fázi vám RoninUI představí vaše heslo `root`. Je zásadní jej bezpečně uložit. Můžete si vybrat fyzickou zálohu, na papíře, nebo uložení v [správci hesel](https://planb.network/courses/secu101/4/2).

![root password](assets/notext/26.webp)

Po uložení hesla `root` zaškrtněte políčko `I have backed up Root user credentials` a klikněte na `Continue` pro pokračování.

![confirm root password](assets/notext/27.webp)

Dalším krokem je vytvoření uživatelského hesla, které bude použito jak pro přístup k webovému rozhraní RoninUI, tak pro navázání SSH sezení s vaším uzlem. Vyberte silné heslo a ujistěte se, že jej bezpečně uložíte. Toto heslo budete muset zadat dvakrát před kliknutím na `Finish` pro potvrzení. Co se týče uživatelského jména, doporučuje se ponechat výchozí volbu, `ronindojo`. Pokud se rozhodnete jej změnit, nezapomeňte příslušně upravit příkazy v následujících krocích.

![user credentials](assets/notext/28.webp)

Po dokončení těchto akcí počkejte, až se váš uzel inicializuje. Poté získáte přístup k webovému rozhraní RoninUI. Jste téměř na konci procesu, zbývá jen několik malých kroků!
![Ronin UI](assets/notext/29.webp)

### Krok 7: Odstranění dočasných přihlašovacích údajů
Otevřete nový terminál na vašem osobním počítači a navážte SSH spojení s vaším uzlem pomocí následujícího příkazu:
`SSH ronindojo@[IP]`
Pokud například IP adresa vašeho uzlu je `192.168.1.40`, příslušný příkaz bude: `SSH ronindojo@192.168.1.40`

Pokud jste během předchozího kroku změnili své uživatelské jméno, nahraďte výchozí uživatelské jméno (`ronindojo`) jiným, nezapomeňte použít toto nové jméno v příkazu. Například, pokud jste si vybrali `planb` jako uživatelské jméno a IP adresa je `192.168.1.40`, příkaz k zadání bude:
`SSH planb@192.168.1.40`
Budete vyzváni k zadání uživatelského hesla. Zadejte jej a poté stiskněte `enter` pro potvrzení. Poté získáte přístup k rozhraní RoninCLI. Použijte šipky na klávesnici k navigaci k možnosti `Exit RoninDojo` a stiskněte `enter` pro její výběr.
![RoninCLI](assets/notext/30.webp)

V tomto okamžiku jste na terminálu svého uzlu s výzvou příkazu podobnou: `ronindojo@RoninDojo:~ $`. Pro odstranění dočasného uživatele vytvořeného během konfigurace bootovatelné micro SD karty zadejte následující příkaz a stiskněte `enter`:
`sudo deluser --remove-home pi`

Budete vyzváni k potvrzení vašeho uživatelského hesla. Zadejte jej a potvrďte stiskem `enter`. Počkejte, až operace dokončí, poté použijte příkaz `exit` pro opuštění terminálu.

Gratulujeme! Váš RoninDojo v2 uzel je nyní nakonfigurován a připraven k použití. Začne s IBD (*Initial Block Download*), pokračovat ve stahování a ověřování Bitcoin blockchainu od Genesis bloku. Tento krok zahrnuje načítání všech Bitcoin transakcí provedených od 3. ledna 2009 a zabere určitý čas. Jakmile je blockchain plně stažen, indexer pokračuje v kompresi databáze. Doba trvání IBD se může výrazně lišit. Váš RoninDojo uzel bude plně operativní, jakmile tento proces dokončí.

**Pokud migrujete ze starého RoninDojo v1 uzlu** na tuto novou verzi s tímto návodem a zachováváte stejný SSD, váš uzel by měl automaticky detekovat a znovu použít existující data na disku, čímž vám ušetří nutnost provádět IBD znovu. V tomto případě budete muset pouze počkat, až se váš uzel resynchronizuje s nejnovějšími bloky.

### Krok 8: "veth* oprava"
Pokud narazíte na chybu s vaším RoninDojo v2 na Raspberry Pi, kde po bezproblémové instalaci váš uzel náhle není přes SSH dosažitelný, ale po jednoduchém restartu se obnoví, pak musíte postupovat podle tohoto kroku 8. Tuto běžnou chybu lze snadno opravit řešením vyvinutým komunitou: "_veth oprava_". Tato drobná korekce trvale řeší náhlá odpojení. Zde je návod, jak ji aplikovat.

Otevřete nový terminál na vašem osobním počítači a navážte SSH spojení s vaším uzlem pomocí následujícího příkazu:
`SSH ronindojo@[IP]`

Pokud například IP adresa vašeho uzlu je `192.168.1.40`, příslušný příkaz by byl:
`SSH ronindojo@192.168.1.40`

Budete vyzváni k zadání uživatelského hesla. Zadejte jej a stiskněte `enter` pro potvrzení. Poté získáte přístup k rozhraní RoninCLI. Použijte šipky na klávesnici k navigaci k možnosti `Exit RoninDojo` a stiskněte `enter` pro její výběr.
V tomto okamžiku jste v terminálu vašeho uzlu s výzvou příkazu podobnou: `ronindojo@RoninDojo:~ $`. Pro aplikaci opravy veth* napište následující příkaz a stiskněte `enter`: `sudo nano /etc/dhcpcd.conf`

Potvrďte znovu své heslo a stiskněte `enter`.

Dostanete se do souboru `dhcpcd.conf`. Potřebujete zkopírovat následující text, nezapomeňte zahrnout hvězdičku, a přidat jej na konec souboru:
`denyinterfaces veth*`

Pro toto se posuňte na konec souboru pomocí šipky dolů na klávesnici, poté použijte pravé tlačítko myši k vložení textu na samostatný řádek.

Po přidání textu stiskněte `ctrl X` pro zahájení ukončení, následované `ctrl Y` pro potvrzení uložení změn, a stiskněte `enter` pro dokončení a návrat do příkazového řádku. Aby bylo zajištěno, že byla modifikace správně aplikována, znovu otevřete soubor `dhcpcd.conf` pomocí příslušného příkazu.

Pro dokončení aplikace opravy restartujte váš uzel spuštěním:
`sudo reboot now`

V tomto bodě můžete zavřít váš terminál. Počkejte potřebný čas, aby se váš RoninDojo restartoval, po kterém byste se měli být schopni znovu připojit přes grafické rozhraní vašeho prohlížeče. Tento proces by měl opravit zjištěnou chybu.

## Jak používat váš RoninDojo v2 uzel?

### Připojení vaší peněženkové aplikace k Electrs
První použití vašeho čerstvě nainstalovaného a synchronizovaného uzlu bude k odesílání vašich transakcí do Bitcoinové sítě. Pravděpodobně budete chtít připojit vaše různé peněženky k vašemu uzlu, aby bylo možné odesílat vaše transakce důvěrně. To můžete udělat prostřednictvím Electrum Rust Server (electrs). Tato aplikace je obvykle předinstalována na vašem RoninDojo uzlu. Pokud ne, můžete ji ručně nainstalovat přes rozhraní RoninCLI v `Applications > Manage Applications > Install Electrum Server`.

Pro získání Tor adresy vašeho Electrum Serveru, z webového rozhraní RoninUI, jděte na:
`Pairing > Electrum server > Pair now`
![Pairing](assets/notext/31.webp)
![Electrs](assets/notext/32.webp)
Poté budete muset zadat `Hostname` adresu končící na `.onion` ve vaší peněženkové aplikaci, doprovázenou portem `50001`. ![hostname](assets/notext/33.webp)
Například na Sparrow Wallet, jednoduše jděte na záložku:
`File > Preferences > Server > Private Electrum`

![Sparrow](assets/notext/34.webp)

### Připojení vaší peněženkové aplikace k Samourai Dojo
Jako alternativu k použití Electrs, Dojo umožňuje připojit vaši kompatibilní softwarovou peněženku přímo k vašemu RoninDojo uzlu. Peněženky jako Samourai Wallet a Sentinel nabízejí tuto funkcionalitu.

Pro navázání spojení budete muset pouze naskenovat QR kód vašeho Dojo. Pro přístup k tomuto QR kódu přes RoninUI, navigujte na:
`Pairing > Samourai Dojo > Pair now`
![Samourai Dojo](assets/notext/35.webp)
Pro propojení vaší Samourai Wallet s vaším Dojo, jednoduše naskenujte tento QR kód během instalace aplikace:

![Samourai Wallet connection](assets/notext/36.webp)
Pokud jste již před nastavením vašeho Ronin Dojo měli peněženku Samourai Wallet, je nutné zálohovat vaši peněženku, odinstalovat a poté znovu nainstalovat aplikaci Samourai Wallet, než obnovíte vaši peněženku. Po spuštění znovu nainstalované aplikace budete mít možnost připojit se k novému Dojo. **Buďte opatrní, tento proces nese riziko ztráty vašich bitcoinů, pokud nebude proveden správně!** Ujistěte se, že máte zálohu vaší peněženky Samourai ve vašich souborech a ověřte platnost vaší heslové fráze přes `Nastavení > Řešení problémů > Heslová fráze`. Je také důležité mít čitelnou zálohu vaší obnovovací fráze a heslové fráze. Pro větší přesnost této operace se doporučuje následovat tento podrobný tutoriál: [https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai](https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai).
### Používání vlastního prohlížeče bloků Mempool.space
Prohlížeč bloků přetváří surové informace z Bitcoin blockchainu do strukturovaného a snadno čitelného formátu. S nástroji jako *Mempool.space* je možné analyzovat transakce, hledat konkrétní adresy, nebo dokonce konzultovat průměrné sazby poplatků mempoolů sítě v reálném čase.

Nicméně, používání online prohlížečů bloků představuje rizika pro vaše soukromí a zahrnuje důvěru ve data poskytovaná třetími stranami. Skutečně, používáním těchto služeb bez procházení vlastním uzlem byste mohli nechtěně prozradit informace o vašich transakcích a musíte se spolehnout na přesnost informací prezentovaných majitelem webu.
Aby se tyto rizika minimalizovala, doporučuje se používat vlastní instanci *Mempool.space* přes síť Tor, přímo hostovanou na vašem uzlu. Toto řešení zajišťuje ochranu vašeho soukromí a autonomii vašich dat.
Pro provedení tohoto kroku začněte instalací *Mempool Space Visualizer* z RoninUI. Na webovém rozhraní přejděte na záložku `Dashboard` a klikněte na `Spravovat` pod `Mempool Space`:
`Dashboard > Mempool Space > Spravovat`
![Spravovat mempool](assets/notext/37.webp)
Poté klikněte na tlačítko `Instalovat Mempool visualizer`:
![instalovat mempool](assets/notext/38.webp)
Potvrďte heslo uživatele:
![heslo mempool](assets/notext/39.webp)
Počkejte, až se instalace dokončí, a poté znovu klikněte na tlačítko `Spravovat`:
![Spravovat Mempool](assets/notext/40.webp)
Získáte `.onion` odkaz pro přístup k vaší vlastní instanci *Mempool.space* přes síť Tor.
![Odkaz Mempool](assets/notext/41.webp)
Doporučuji si tento odkaz uložit do oblíbených v prohlížeči Tor nebo jej přidat do aplikace Tor Browser na vašem smartphonu pro snadný a bezpečný přístup odkudkoli. Pokud ještě nemáte prohlížeč Tor, můžete si jej stáhnout zde: [https://www.torproject.org/download/](https://www.torproject.org/download/)
![Mempool Tor](assets/notext/42.webp)

### Používání Whirlpoolu k míchání vašich bitcoinů
Váš uzel RoninDojo také integruje _WhirlpoolCLI_, rozhraní příkazové řádky, které umožňuje automatizaci Whirlpool coinjoinů, a _WhirlpoolGUI_, grafické rozhraní navržené pro interakci s _WhirlpoolCLI_.
Provádění coinjoin prostřednictvím Whirlpool vyžaduje, aby aplikace použitá k provedení remixů byla aktivní. Tato podmínka může být omezující pro ty, kteří si přejí dosáhnout vysokých úrovní anonymních setů. Skutečně, zařízení hostující aplikaci integrující Whirlpool musí zůstat neustále zapnuté. To znamená, že pro účast na remixech 24 hodin denně musí váš počítač nebo smartphone zůstat zapnutý s nepřetržitě otevřeným Samourai nebo Sparrow. Řešením této omezení je použití _WhirlpoolCLI_ na stroji, který je vždy zapnutý, například na Bitcoin node, což umožňuje vašim mincím remixovat bez přerušení a bez nutnosti nechat zapnuté další zařízení.
Podrobný tutoriál je připravován, aby vás krok za krokem provedl procesem coinjoin s Samourai Wallet a RoninDojo v2, od A do Z.

Pro hlubší pochopení coinjoin a jeho použití na Bitcoinu, vás také zvu, abyste si přečetli tento další článek: Understanding and using coinjoin on Bitcoin, kde detailně popisuji vše, co potřebujete vědět o této technice.

https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2
### Používání nástroje Whirlpool Stat Tool (WST)

Po provedení coinjoinů s Whirlpool je užitečné přesně zhodnotit dosaženou úroveň soukromí pro vaše smíchané UTXO. K tomu můžete použít Python nástroj *Whirlpool Stat Tool*. Tento nástroj umožňuje měřit jak perspektivní, tak retrospektivní skóre vašich UTXO, zatímco analyzuje jejich míru rozptylu v bazénu.

Pro prohloubení vašeho porozumění výpočetním mechanismům těchto anonymních setů doporučuji přečíst článek: REMIX - WHIRLPOOL, který detailně popisuje fungování těchto indexů.

https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa



Pro přístup k nástroji WST přejděte na RoninCLI. K tomu otevřete terminál na vašem osobním počítači a navážte SSH spojení s vaším node pomocí následujícího příkazu:
`SSH ronindojo@[IP]`

Pokud je například IP adresa vašeho node `192.168.1.40`, odpovídající příkaz by byl:
`SSH ronindojo@192.168.1.40`

Pokud jste během kroku 6 změnili své uživatelské jméno z výchozího jména (`ronindojo`) na jiné, ujistěte se, že použijete toto nové jméno v příkazu. Například, pokud jste si vybrali `planb` jako vaše uživatelské jméno a IP adresa je `192.168.1.40`, příkaz k zadání by byl:
`SSH planb@192.168.1.40`

Budete požádáni o zadání uživatelského hesla. Zadejte jej a stiskněte `enter` pro potvrzení. Poté získáte přístup k rozhraní RoninCLI. Použijte šipky na klávesnici k navigaci do menu `Samourai Toolkit` a stiskněte `enter` pro jeho výběr:

![Samourai Toolkit](assets/notext/43.webp)

Poté vyberte `Whirlpool Stat Tool`:

![WST](assets/notext/44.webp)

Po inicializaci WST nástroj zahájí jeho automatickou instalaci. Počkejte během tohoto kroku. Instrukce k použití se budou procházet. Jakmile je instalace dokončena, stiskněte libovolnou klávesu pro přístup k terminálu WST:

![WST commands](assets/notext/45.webp)

Zobrazí se následující výzva k zadání příkazu:
`wst#/tmp>`

Pokud si přejete opustit toto rozhraní a vrátit se do menu RoninCLI, jednoduše zadejte:
`quit`

Nejprve je nutné nakonfigurovat proxy pro použití Toru, aby bylo zajištěno důvěrnost při extrakci dat z OXT. Zadejte příkaz:
`socks5 127.0.0.1:9050`
Následně pokračujte stažením informací o poolu obsahující vaši transakci:
`download 0001`
Nahraďte `0001` kódem denominace poolu, který vás zajímá. Kódy denominací jsou na WST následující:
- Pool 0.5 bitcoinů: `05`
- Pool 0.05 bitcoinů: `005`
- Pool 0.01 bitcoinů: `001`
- Pool 0.001 bitcoinů: `0001`

Po stažení nahrajte data nahrazením `0001` kódem vašeho poolu v tomto příkazu: `load 0001`

![WST loading](assets/notext/46.webp)

Počkejte, až se načtení dokončí, což může trvat několik minut. Jakmile jsou data načtená, abyste zjistili skóre anonsetu vaší mince, spusťte příkaz `score` následovaný vaším TXID (bez závorek):
`score [TXID]`

![WST score](assets/notext/47.webp)

WST poté zobrazí retrospektivní skóre (_Metriky zpětného pohledu_), následované prospektivním skóre (_Metriky vpřed hledící_). Kromě skóre anonsetu WST také ukáže míru rozptylu vaší transakce v rámci poolu vzhledem k jejímu anonsetu.

**Je důležité si uvědomit, že prospektivní skóre vaší mince by mělo být vypočítáno z TXID vašeho počátečního mixu, a ne z vašeho nejnovějšího mixu. Naopak, retrospektivní skóre UTXO je vypočítáno z TXID posledního cyklu.**

### Použití Boltzmannova kalkulátoru
Boltzmannův kalkulátor je nástroj pro analýzu Bitcoinové transakce, který nabízí možnost měřit její úroveň entropie mezi jinými pokročilými metrikami. Tyto údaje poskytují kvantifikované hodnocení soukromí transakce a pomáhají identifikovat potenciální nedostatky. Tento nástroj je již integrován do vašeho uzlu RoninDojo, což usnadňuje jeho přístup a použití.

Před podrobným popisem postupu použití Boltzmannova kalkulátoru je důležité porozumět významu těchto ukazatelů, jejich výpočetní metodě a jejich užitečnosti. Ačkoli jsou tyto ukazatele použitelné pro jakoukoli Bitcoinovou transakci, jsou obzvláště užitečné pro hodnocení kvality transakce coinjoin.

**První ukazatel**, který software vypočítá, je celkový počet možných kombinací, označený pod `nb combinations` v nástroji. Na základě hodnot zapojených UTXO tento ukazatel kvantifikuje počet způsobů, jakými lze vstupy spojit s výstupy. Jinými slovy, určuje počet věrohodných interpretací, které může transakce generovat. Například coinjoin strukturovaný podle modelu Whirlpool 5x5 představuje `1496` možných kombinací:
![combinations](assets/notext/50.webp)
Kredit: KYCP

**Druhý ukazatel** vypočítaný je entropie transakce, označená `Entropy`. Když má transakce vysoký počet možných kombinací, je často relevantnější odkazovat na její entropii. Definuje se jako binární logaritmus počtu možných kombinací. Zde je použitý vzorec:
- $E$: entropie transakce;
- $C$: počet možných kombinací pro transakci.
$$E = \log_2(C)$$
V matematice binární logaritmus (logaritmus o základu 2) odpovídá inverzní operaci umocňování čísla 2 na určitou mocninu. Jinými slovy, binární logaritmus $x$ je exponent, na který musí být 2 umocněno, aby bylo získáno $x$. Proto je tento ukazatel vyjádřen v bitech. Vezměme si příklad výpočtu entropie pro transakci coinjoin strukturovanou podle modelu Whirlpool 5x5, který, jak bylo dříve zmíněno, nabízí řadu možných kombinací `1496`:$$ C = 1496 $$
$$ E = \log_2(1496) $$
$$ E \approx 10.5469 \text{ bitů}$$

Takže tato transakce coinjoin vykazuje entropii 10.5469 bitů, což je považováno za velmi uspokojivé. Čím vyšší tato hodnota je, tím více různých interpretací transakce připouští, čímž zvyšuje její úroveň soukromí.

Vezměme si další příklad s více konvenční transakcí, která obsahuje jeden vstup a dva výstupy: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://mempool.space/en/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce)
V případě této transakce je jediná možná interpretace: `(inp 0) > (Outp 0 ; Outp 1)`. V důsledku toho je její entropie stanovena na `0`:
$$ C = 1 $$
$$ E = \log_2(1) $$
$$ E \approx 0 \text{ bitů}$$
**Třetí ukazatel** poskytnutý kalkulačkou Boltzmann se nazývá `Efektivita Peněženky`. Tento ukazatel hodnotí efektivitu transakce porovnáním s optimální transakcí, která by byla možná ve stejné situaci. To nás přivádí k diskusi o konceptu maximální entropie, která odpovídá nejvyšší entropii, kterou může konkrétní struktura transakce teoreticky dosáhnout. Takže pro strukturu coinjoin Whirlpool 5x5 je maximální entropie stanovena na `10.5469`. Efektivita transakce je poté vypočítána porovnáním této maximální entropie s aktuální entropií analyzované transakce. Použitý vzorec je následující:
- $ER$: aktuální entropie transakce, vyjádřená v bitech;
- $EM$: maximální možná entropie pro danou strukturu transakce, také v bitech;
- $Ef$: efektivita transakce, v bitech.
$$Ef = ER - EM$$ $$Ef = 10.5469 - 10.5469$$
$$Ef = 0 \text{ bitů}$$

Tento ukazatel je také vyjádřen jako procento, jeho vzorec je poté:
- $CR$: počet aktuálních možných kombinací;
- $CM$: maximální počet možných kombinací se stejnou strukturou;
- $Ef$: efektivita vyjádřená jako procento.
$$Ef = \frac{CR}{CM}$$
$$Ef = \frac{1496}{1496}$$
$$Ef = 100\%$$

Efektivita `100%` tedy naznačuje, že transakce maximalizuje svůj potenciál pro soukromí na základě své struktury.
**Čtvrtý ukazatel**, hustota entropie, neboli `Entropy Density`, nabízí pohled na entropii vzhledem ke každému vstupu nebo výstupu transakce. Tento ukazatel se ukazuje jako užitečný pro hodnocení a porovnávání efektivity transakcí různých velikostí. Pro jeho výpočet jednoduše vydělte celkovou entropii transakce celkovým počtem vstupů a výstupů zapojených do transakce. Vezměme si příklad Whirlpool 5x5 coinjoin:
- $ED$: hustota entropie vyjádřená v bitech;
- $E$: entropie transakce vyjádřená v bitech;
- $T$: celkový počet vstupů a výstupů v transakci.
$$T = 5 + 5 = 10$$
$$ED = \frac{E}{T}$$
$$ED = \frac{10.5469}{10}$$
$$ED = 1.054 \text{ bity}$$
**Pátý údaj** poskytnutý Boltzmannovým kalkulátorem je tabulka pravděpodobností shody mezi vstupy a výstupy. Tato tabulka ukazuje prostřednictvím `Boltzmannova skóre` pravděpodobnost, že konkrétní vstup je spojen s daným výstupem. Vezmeme-li příklad Whirlpool coinjoin, tabulka pravděpodobností by zdůraznila šance na propojení mezi každým vstupem a výstupem, poskytující kvantitativní míru nejednoznačnosti nebo předvídatelnosti asociací v transakci:

| %       | Výstup 0 | Výstup 1 | Výstup 2 | Výstup 3 | Výstup 4 |
|---------|----------|----------|----------|----------|----------|
| Vstup 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Vstup 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Vstup 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Vstup 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Vstup 4 | 34%      | 34%      | 34%      | 34%      | 34%      |

Zde je jasné, že každý vstup má stejnou šanci být spojen s jakýmkoli výstupem, což posiluje nejednoznačnost a důvěrnost transakce. Avšak v případě jednoduché transakce s jedním vstupem a dvěma výstupy je situace jiná:

| %       | Výstup 0 | Výstup 1 |
|---------|----------|----------|
| Vstup 0 | 100%     | 100%     |

Zde vidíme, že pravděpodobnost, že každý výstup pochází z vstupu 0, je 100%. Nižší pravděpodobnost tedy překládá do větší důvěrnosti tím, že rozptyluje přímé vazby mezi vstupy a výstupy.

**Šestý údaj** poskytnutý je počet deterministických spojení doplněný o poměr těchto spojení. Tento ukazatel odhaluje, kolik spojení mezi vstupy a výstupy v analyzované transakci je nesporných, s pravděpodobností 100%. Poměr zase nabízí perspektivu na váhu těchto deterministických spojení v rámci celkových spojení transakce.

Například transakce typu Whirlpool coinjoin představuje žádná deterministická spojení a proto zobrazuje ukazatel a poměr 0%. Na druhou stranu, v naší druhé zkoumané transakci (s jedním vstupem a dvěma výstupy) je ukazatel nastaven na 2 a poměr dosahuje 100%. Tedy nulový ukazatel signalizuje vynikající důvěrnost díky absenci přímých a nesporných spojení mezi vstupy a výstupy.
**Jak přistoupit k Boltzmann Calculator na RoninDojo?** Pro přístup k nástroji *Boltzmann Calculator* přejděte na RoninCLI. K tomu otevřete terminál na vašem osobním počítači a navážete SSH spojení s vaším uzlem pomocí následujícího příkazu: `SSH ronindojo@[IP]`

Pokud je například IP adresa vašeho uzlu `192.168.1.40`, příslušný příkaz by byl:
`SSH ronindojo@192.168.1.40`

Pokud jste během kroku 6 změnili své uživatelské jméno, nahraďte výchozí uživatelské jméno (`ronindojo`) jiným, ujistěte se, že použijete toto nové jméno v příkazu. Například, pokud jste si vybrali `planb` jako vaše uživatelské jméno a IP adresa je `192.168.1.40`, příkaz k zadání by byl:
`SSH planb@192.168.1.40`

Budete vyzváni k zadání uživatelského hesla. Zadejte jej a poté stiskněte `enter` pro potvrzení. Poté získáte přístup k rozhraní RoninCLI. Použijte šipky na klávesnici k navigaci do menu `Samourai Toolkit` a stiskněte `enter` pro jeho výběr:

![Samourai Toolkit](assets/notext/43.webp)

Poté vyberte `Boltzmann Calculator`:

![boltzmann](assets/notext/49.webp)

Dostanete se na domovskou stránku softwaru:

![boltzmann home](assets/notext/51.webp)

Zadejte TXID transakce, kterou chcete studovat, a stiskněte klávesu `enter`:

![boltzmann txid](assets/notext/52.webp)

Kalkulačka poté poskytne všechny ukazatele, o kterých jsme dříve diskutovali:

![boltzmann result](assets/notext/53.webp)

### Další funkce vašeho RoninDojo v2
Váš uzel RoninDojo integruje různé další funkce. Zejména máte možnost skenovat specifické informace, aby byly vzaty v úvahu. Například někdy vaše peněženka Samourai, připojená k RoninDojo, nemusí zobrazovat bitcoiny, které ve skutečnosti vlastníte. Pokud zůstatek ukazuje 0, zatímco jste si jisti, že v této peněžence máte bitcoiny, několik důvodů může vysvětlovat tuto situaci, jako je chyba v cestách derivace. Ale jednou z příčin může být také to, že váš uzel správně nesleduje vaše adresy. Pro vyřešení tohoto problému můžete zajistit, že váš uzel skutečně sleduje váš `xpub` pomocí nástroje _xpub tool_. Pro přístup k tomuto nástroji přes RoninUI postupujte podle cesty:
`Maintenance > XPUB Tool`

Zadejte `xpub`, který způsobuje problém, a klikněte na tlačítko `Check` pro ověření této informace:
![xpub tool](assets/notext/54.webp)
Ujistěte se, že jsou správně uvedeny všechny transakce. Je také důležité ověřit, že typ derivace použitý odpovídá vaší peněžence. Pokud tomu tak není, klikněte na `Retype`, a poté vyberte z `BIP44`, `BIP49`, nebo `BIP84` podle vašich potřeb.
Kromě tohoto nástroje je záložka `Maintenance` v RoninUI plná dalších užitečných funkcí:
- *Transaction Tool*: Umožňuje prozkoumat detaily dané transakce;
- *Address Tool*: Umožňuje potvrdit sledování dané adresy vaším Dojo;
- *Rescan Blocks*: Nutí váš uzel provést nové skenování určitého rozsahu bloků.

Záložka `Push Tx` je další zajímavou funkcí RoninUI, která umožňuje vysílání podepsané transakce na síti Bitcoin. Transakce musí být zadána v hexadecimální formě.
Ohledně dalších záložek dostupných na vašem dashboardu RoninUI:
- `Apps`: Hostuje aplikaci Whirlpool a v budoucnu bude jistě použita pro integraci nových aplikací;
- `Logs`: Nabízí přístup v reálném čase k protokolům událostí vašeho softwaru;
- `System Info`: Poskytuje obecné informace o vašem uzlu, jako je teplota CPU, využití úložného prostoru nebo data RAM. Najdete zde také možnosti `Reboot` a `Shut down` pro restart nebo vypnutí vašeho uzlu;
- `Settings`: Umožňuje změnit heslo uživatele.

To je vše! Děkuji, že jste sledovali tento tutoriál až do konce. Pokud se vám líbil, povzbuzuji vás, abyste ho sdíleli na sociálních médiích. Kromě toho, pokud máte příležitost, zvažte podporu vývojářů, kteří tyto volně dostupné a open-source softwary poskytují naší komunitě prostřednictvím daru: [https://donate.ronindojo.io/](https://donate.ronindojo.io/). Pro prohloubení vašich znalostí o RoninDojo a objevení dalších zdrojů, vřele doporučuji konzultovat odkazy na níže uvedené externí zdroje.

**Externí zdroje:**
- [https://ronindojo.io/index.html](https://ronindojo.io/index.html)
- [https://wiki.ronindojo.io/en/home](https://wiki.ronindojo.io/en/home)
- [https://gist.github.com/LaurentMT/e758767ca4038ac40aaf](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [https://medium.com/@laurentmt/představujeme-boltzmann-85930984a159](https://medium.com/@laurentmt/představujeme-boltzmann-85930984a159)
- [https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry](https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry)