---
name: Budování pomocí prvků a kapalné sítě
goal: Naučte se používat a vyvíjet s open-source blockchainovou platformou Elements a jejími klíčovými funkcemi
objectives: 

  - Porozumět základním konceptům blockchainové platformy Elements a vedlejších řetězců Liquid.
  - Naučte se nastavovat a spouštět uzly Elements pro samostatné konfigurace a konfigurace sidechain.
  - Získejte praktické zkušenosti s federativním blokovým podepisováním a federativním dvoucestným kolíkem.
  - Nastavte a spravujte bezpečné a efektivní prostředí blockchainu pro reálné případy použití.

---
# Stavět na kapalinách a prvcích

Objevte pokročilé funkce a možnosti nástrojů Liquid a Elements a naučte se, jak tyto nástroje efektivně využívat k vylepšení svých vývojových projektů. Toto školení poskytuje kompletní teoretický a praktický základ, který vám umožní zvládnout funkce, jako jsou důvěrné transakce, vydaná aktiva a federativní podepisování bloků.

Liquid, založený na frameworku Elements, je navržen tak, aby zlepšil soukromí, škálovatelnost a funkčnost finančních a technických řešení. V tomto kurzu získáte praktické zkušenosti s vydáváním a správou aktiv, federovaným dvoucestným kolíkem a používáním nástrojů, jako jsou elementsd a elements-cli, což vám umožní vytvářet inovativní řešení na míru vašim potřebám.

Tento kurz je přizpůsoben vývojářům všech úrovní zkušeností. Začátečníci a středně pokročilí uživatelé zde najdou přístupná vysvětlení a praktické příklady, zatímco pokročilí uživatelé se mohou ponořit do technických detailů a méně známých funkcí aplikací Liquid a Elements.

Připojte se k nám, abyste zvýšili své dovednosti, uvolnili plný potenciál systémů Liquid a Elements a vytvořili působivé nástroje pro budoucnost inovací Liquid.

+++
# Úvod

<partId>8f34de87-6e9a-4e3b-a326-50fc7c1803b3</partId>

## Úvod do kurzů

<chapterId>a721398e-7040-4edd-be53-b485ea759fa9</chapterId>

![Video](https://youtu.be/gkQfnwYLyI0?si=H6cIPhgZaSAwHaHI)

Účelem Elements Academy je představit a vysvětlit klíčové koncepty platformy Elements, na které je Liquid postaven. Na konci kurzu byste měli dobře porozumět hlavním funkcím Elements, jako jsou důvěrné transakce a vydaná aktiva, a procesům spojeným s provozem jádra Elements.

Každá část bude obsahovat lekce s vysvětlujícím textem a video, které bude zakončeno kvízem. Počet otázek se vztahuje k rozsahu předchozího tématu. Oddíl 10 bude shrnovat obsah kurzu a bude zakončen větším kvízem.

Jakékoli dotazy, žádosti o doplňující informace nebo dotazy týkající se odpovědí na kvízové otázky můžete směřovat na svého učitele Jamese Dorfmana.

## Přehled prvků

<chapterId>7a7f2712-5300-4a6d-b1ed-05eab731bc35</chapterId>

![Video](https://youtu.be/ns-JLGdkNig?si=fmWye_boRSvVF1Bt)

Elements je blockchainová platforma s otevřeným zdrojovým kódem, která umožňuje přístup k výkonným funkcím vyvinutým členy komunity, jako jsou důvěrné transakce a emitovaná aktiva.

Elements je ve své podstatě protokol, který umožňuje dosáhnout konsenzu kolem historie transakcí a pravidel, jimiž se řídí převod a vytváření aktiv uložených v distribuované blockchainové účetní knize.

Další základní informace o systému Elements lze snadno nalézt na webových stránkách projektu Elements (https://elementsproject.org/), na oficiálním blogu Liquidu (https://blog.liquid.net/) a na portálu pro vývojáře(https://liquid.net/devs).

### Prvky

Systém Elements, který byl spuštěn v roce 2015, snižuje interní náklady na vývoj a výzkum a využívá nejnovější technologii blockchain, čímž otevírá mnoho nových případů použití. Blockchain založený na platformě Elements může fungovat buď jako samostatný blockchain, nebo může být připojen k jinému a fungovat jako Sidechain. Provozování Elements jako Sidechainu umožňuje ověřitelný převod aktiv mezi různými blockchainy.

Je postaven na kódové základně Bitcoinu a rozšiřuje ji, takže vývojáři, kteří znají rozhraní API Bitcoind, mohou rychle a levně vytvářet funkční blockchainy a testovat zkušební projekty. Díky tomu, že je postaven na kódové základně Bitcoinu, může Elements fungovat také jako testovací prostředí pro změny samotného protokolu Bitcoin.

Některé z hlavních funkcí aplikace Elements jsou uvedeny níže.

#### Důvěrné transakce

Ve výchozím nastavení jsou všechny adresy v prvcích zaslepeny pomocí důvěrných transakcí. Zaslepení je proces, při kterém je částka a typ převáděného aktiva kryptograficky skryta před všemi, kromě účastníků a těch, kterým se rozhodnou zaslepovací klíč prozradit.

#### Vydaná aktiva

Vydaná aktiva na prvcích umožňují vydávat a převádět mezi účastníky sítě více typů aktiv. Vydaná aktiva rovněž využívají výhod důvěrných transakcí a mohou být znovu vydána nebo zničena kýmkoli, kdo je držitelem příslušného tokenu pro opětovné vydání.

#### Federativní dvoucestný kolík

Elements je univerzální blockchainová platforma, kterou lze také "přichytit" k existujícímu blockchainu (například k Bitcoinu), aby bylo možné obousměrně převádět aktiva z jednoho řetězce do druhého. Implementace Elements jako sidechainu umožňuje obejít některé z inherentních vlastností hlavního řetězce a zároveň zachovat značnou míru bezpečnosti, kterou poskytují aktiva zajištěná na hlavním řetězci.

#### Podepsané bloky

Elements využívá Silnou federaci signatářů, tzv. Block Signers, kteří spolehlivě a včas podepisují a vytvářejí bloky. Tím se odstraní transakční zpoždění procesu těžby PoW, které je v důsledku náhodného poissonského rozdělení zatíženo velkým rozptylem času bloku. Proces federativního podepisování bloků dosahuje spolehlivého vytváření bloků bez nutnosti zavádět důvěru třetí strany nebo výpočetní těžbu založenou na `algoritmech`.

Elements přidává všechny tyto funkce nad kódovou základnu Bitcoin Core, rozšiřuje možnosti mainchain protokolu a umožňuje nové obchodní případy použití při nasazení jako sidechain nebo jako samostatné blockchainové řešení.

# Prvek

<partId>ac68d611-be84-432f-a3a8-620d310e131c</partId>

## Jak prvky fungují

<chapterId>05d88877-58b0-455b-9ae6-a72d19070525</chapterId>

![Video](https://youtu.be/v0lzmfH81AY?si=V-xDWfmDLKyBcdPs)

Elements poskytuje technické řešení problémů, se kterými se uživatelé blockchainu denně potýkají: zpoždění transakcí, nedostatek soukromí a riziko zaměnitelnosti.

Elements tyto problémy překonává použitím federativního blokového podepisování a důvěrných transakcí.

Na rozdíl od sítě Bitcoin není proces podepisování bloků v rámci Elements závislý na dynamických podpisech více stran (DMMS) a důkazu práce (PoW). Místo toho Elements využívá silnou federaci podepisujících osob, tzv. block signers, které mohou spolehlivě a včas podepisovat a vytvářet bloky. Tím se odstraní transakční zpoždění procesu těžby PoW, které podléhá velkému rozptylu času bloku v důsledku jeho náhodného poissonového rozdělení. Proces federativního podepisování bloků dosahuje spolehlivého vytváření bloků, aniž by zaváděl potřebu důvěry třetí strany.

Elements může běžet jako sidechain jiného blockchainu, například Bitcoinu, nebo jako samostatný blockchain bez závislosti na jiných sítích.

Pokud se Strong Federation používá jako sidechain, obsahuje také členy, kteří umožňují bezpečný a kontrolovaný převod aktiv mezi hlavním řetězcem a sidechainem Elements. Řízený přenos aktiv se nazývá Federated 2-Way Peg a členové, kteří plní roli přenosu aktiv, se nazývají Watchmen.

Pro pochopení fungování sítě Elements jsou důležité procesy spojené s jejím provozem a role účastníků sítě.

Ať už je implementován jako sidechain nebo samostatný blockchain, Elements využívá k vytváření bloků silné federace podepisujících osob.

### Silné federace

Elements používá model konsensu, který poprvé navrhla společnost Blockstream a který se nazývá Strong Federations. Silná federace nepotřebuje důkaz práce (PoW) a místo toho se spoléhá na kolektivní akce skupiny vzájemně si nedůvěřujících účastníků, tzv. funkcionářů.

Funkcionář může v rámci silné federace plnit tyto role: Funkcionáři jsou: Signatáři bloků a Strážci. Blokoví signatáři jsou vyžadováni, pokud provozujete prvky v režimu sidechainu nebo samostatného blockchainu, zatímco strážci jsou vyžadováni pouze v nastavení sidechainu.

Akce, které může člen silné federace provádět, jsou rozděleny mezi dvě různé role, aby se zvýšila bezpečnost a omezily škody, které může útočník způsobit.

V kombinaci těchto účastníků umožňuje Elements rychlé vytváření bloků (rychlejší a konečné potvrzení transakcí) a zaručená, převoditelná aktiva (vázaná aktiva přímo propojitelná s jiným blockchainem).

Dokument Strong Federations si můžete přečíst zde: https://blockstream.com/strong-federations.pdf

### Blokování signatářů

Řetězec bloků, jako je ten bitcoinový, se rozšiřuje, když kdokoli, kdo je součástí dynamické skupiny signatářů bloků, rozšíří řetězec tím, že prokáže vynaložení práce. Dynamická povaha množiny přináší problémy s latencí, které jsou těmto systémům vlastní.

Federativní model nahrazuje dynamickou množinu známou množinou a používá schéma s více podpisy. Snížení počtu účastníků potřebných k rozšíření blockchainu zvyšuje rychlost a škálovatelnost systému, zatímco validace všemi stranami zajišťuje integritu historie transakcí.

Federativní podepisování bloků se skládá z několika fází:


- Krok 1 - Podepisovatelé bloků navrhují všem ostatním zúčastněným podepisovatelům bloků kandidáty na bloky.
- Krok 2 - Každý podepisovatel bloku signalizuje svůj záměr tím, že se předem zaváže podepsat daný kandidátský blok.
- Krok 3 - Pokud je splněna daná prahová hodnota pro předběžný závazek, každý podepisovatel bloku blok podepíše.
- Krok 4 - Pokud je splněna prahová hodnota podpisu (která se může lišit od prahové hodnoty v kroku 3), blok je přijat a odeslán do sítě. Silná federace dosáhla konsensu o posledním bloku transakcí.
- Krok 5 - Další blok je poté navržen dalším podepisovatelem bloku v kruhovém robindu a proces se opakuje.

Vzhledem k tomu, že generování bloků Silné federace není pravděpodobnostní a je založeno na pevné množině signatářů, nikdy nebude podléhat reorganizaci více bloků. To umožňuje výrazně zkrátit čekací dobu spojenou s potvrzováním transakcí. Odstraňuje také motivaci k těžbě za účelem zisku (tj. odměny za bloky) a nahrazuje ji motivací k produktivní účasti v síti, kde mají všichni účastníci stejný společný cíl; zajistit, aby síť nadále fungovala způsobem, který je výhodný pro všechny. Toho dosahuje bez zavedení jediného bodu selhání nebo vyšších požadavků na důvěryhodnost.

### Prvky jako vedlejší řetězec - Strážci a federativní dvoucestný kolík

Pokud je veden jako vedlejší řetězec, mají někteří členové Silné federace další roli, kterou musí plnit, a to roli Strážců. Strážci jsou zodpovědní za převod aktiv do sidechainu Elements a z něj, což jsou procesy známé jako `Peg-In` a `Peg-Out`.

Aby sidechain fungoval důvěryhodně, musí účastníkům umožnit ověřit, že je nabídka aktiv kontrolovaná a ověřitelná. Sidechain Elements používá dvoucestný federativní kolíček, který umožňuje obousměrný převod aktiv do blockchainu Elements a z něj. Tím jsou splněny požadavky na prokazatelnou emisi a převody mezi řetězci.

Funkce Federated 2-way Peg umožňuje, aby aktivum bylo interoperabilní s jinými blockchainy a reprezentovalo nativní aktivum jiného blockchainu. Připojením svého blockchainu k jinému můžete rozšířit možnosti mainchainu a překonat některá jeho přirozená omezení.

Na vysoké úrovni dochází k převodům do sidechainu, když někdo pošle aktiva z mainchainu na adresu kontrolovanou peněženkou Watchmen s více podpisy. Tím se aktiva v mainchainu účinně zmrazí. Watchmen pak transakci ověří a uvolní stejné množství přidružených aktiv v rámci sidechainu. Uvolněná aktiva jsou odeslána do sidechainové peněženky, která může prokázat nárok na původní aktiva v mainchainu. Tento proces účinně přesouvá aktiva z hlavního řetězce do sidechainu.

Aby mohl uživatel převést aktiva zpět do mainchainu, provede v sidechainu speciální transakci peg-out. Tuto transakci zkontrolují Strážci, kteří poté podepíší transakční výdaj z peněženky s více podpisy, kterou kontrolují na hlavním řetězci. Aby se transakce na mainchainu stala platnou, musí ji podepsat určitý prahový počet účastníků federace. Když Strážci pošlou aktivum zpět do mainchainu, zničí také odpovídající částku na sidechainu, čímž efektivně převedou aktiva mezi blockchainy.

## Nastavení a spuštění prvků

<chapterId>cc806e5a-81ab-457b-9531-9f863120a019</chapterId>

![Video](https://youtu.be/Frr_OjTEPAM?si=iq5XonJyQk8S5OAu)

Protože Elements vychází z kódové základny Bitcoinu, jsou komponenty, které tvoří fungující síť, velmi podobné.

Samotný software uzlu Elements se nazývá `elementsd` a běží jako démon na počítači uživatele. Démon (nebo služba v systému Windows) je program, který běží jako služba na pozadí, aniž by vyžadoval přímé řízení přihlášeného uživatele.

Poznámka: V tomto dokumentu budeme vždy odkazovat na elementsd jako na verzi démona, ale vše lze provádět pomocí elements-qt, pokud je povolena volba server.

Démon Elements se připojuje k ostatním uzlům v síti, aby si mohl vyměňovat data o transakcích a blocích, ověřovat a rozšiřovat svou místní kopii řetězce bloků sítě.

Součástí softwaru Elements je také klientský program `elements-cli`, který umožňuje odesílat příkazy RPC (Remote Procedure Call) do elementsd z příkazového řádku. To lze použít například k dotazování na zůstatek peněženky, zobrazení dat o transakcích nebo blokacích nebo k vysílání transakcí. Toto nastavení by mělo být známé každému, kdo používal ekvivalenty Bitcoinu: bitcoind a bitcoin-cli.

Vzhledem k tomu, že uzel Elements lze konfigurovat předáním parametrů při spuštění nebo prostřednictvím konfiguračního souboru, je možné mít na stejném počítači spuštěno více instancí. To je užitečné pro účely testování a vývoje, protože si můžete na jednom stroji nastavit vlastní lokální síť, přičemž každý uzel Elements bude mít vlastní kopii dat blockchainu, bude spravovat vlastní fond nepotvrzených platných transakcí a naslouchat požadavkům RPC na různých portech.

### Úložiště kódu prvků a komunita

Elements je projekt s otevřeným zdrojovým kódem a jeho zdrojový kód najdete v repozitáři Elements GitHub na adrese https://github.com/ElementsProject/elements. Úložiště obsahuje zdrojové kódy programů elementsd a elements-cli spolu s podpůrnými nástroji pro instalaci a sestavení, sadou testů a instruktážní dokumentací.

Úložiště kódu doplňuje webová stránka https://elementsproject.org, která je zaměřena na komunitu a obsahuje vysvětlení, co je to Elements, jak funguje, a obsáhlou výukovou sekci. Výukový program se zaměřuje na poznávání systému Elements na příkladech z příkazového řádku a ukazuje, jak nad ním vytvářet jednoduché desktopové a webové aplikace. Na webu jsou také uvedena populární diskusní fóra komunity Elements a sám je hostován na GitHubu, což umožňuje komunitní příspěvky k obsahu webu.

Chcete-li spustit aplikaci Elements na svém počítači, musíte nejprve naklonovat (stáhnout kopii) zdrojový kód, nainstalovat všechny závislosti, které kód obsahuje, a nakonec sestavit spustitelné soubory démona a klienta. Poté je software Elements připraven ke konfiguraci a spuštění.

## Konfigurace uzlů a sítě

<chapterId>df1ec0aa-84ea-4149-af7a-b4523d67e1d9</chapterId>

Konfigurační nastavení lze uzlu Elements předat při spuštění, aby se změnil způsob, jakým běží, ověřuje data, připojuje se k ostatním uzlům a inicializuje svá data blockchainu.

Nastavení se načítají z určeného souboru `elements.conf` nebo se předávají jako parametry z příkazového řádku.

Některé z nich lze změnit pomocí těchto parametrů:


- Název výchozího aktiva používaného v samostatných implementacích blockchainu.
- Číslo vytvořeného počátečního aktiva.
- Aktivum, které se použije při placení transakčních poplatků v síti.
- Místo uložení datových souborů blockchainu.
- Pověření RPC používané k připojení k uzlu Bitcoin.
- Prahová hodnota `n z m`, kterou je třeba splnit, a platné veřejné klíče, které mohou podepisovat bloky.
- Skript, který je třeba splnit, aby bylo možné převádět aktiva do sidechainu a z něj.
- Zda se připojit k uzlu Bitcoin jako k sidechainu, nebo ne.

Mnohé z nich jsou součástí pravidel konsensu sítě, proto je důležité, aby byly při spuštění použity ve všech uzlech. Některá lze změnit po inicializaci řetězce, ale některá je třeba opravit až po jejich použití k inicializaci řetězce.

Použití parametrů bude popsáno později v průběhu kurzu, pokud se budou týkat jednotlivých oddílů.

### Základní operace pomocí příkazového řádku

V tomto kurzu si ukážeme příklady, které používají program `elements-cli` k volání RPC na jeden nebo více uzlů Elements. To se provádí z terminálu a pro zkrácení příkazů se použije `alias`. Podle této konvence, když uvidíte něco jako následující příkazy:

```bash
e1-dae
e1-cli getnewaddress
```

`e1-dae` a `e1-cli` jsou vlastně typografické zkratky, které využívají funkci terminálu `alias`. Znaky `e1-dae` a `e1-cli` budou při spuštění příkazu skutečně nahrazeny a příkaz, který se spustí, bude vypadat podobně:

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir1
$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir1 getnewaddress
```

Výše vidíme volání pro spuštění démona Elements a volání programů elements-cli umístěných v adresáři `$HOME/elements/src` a hodnotu parametru `datadir`. Parametr `datadir` nám umožňuje sdělit instancím démona a klienta, kde mají umístit své konfigurační soubory a v případě démona, kde má být uložena jeho kopie blockchainu. Protože sdílejí konfigurační soubor, bude klient schopen provádět RPC volání na démona.

Opětovným spuštěním výše uvedeného příkazu, ale s jinou hodnotou `datadir`, můžeme spustit více instancí systému Elements, každou s vlastní kopií blockchainu a konfiguračním nastavením. Podle této konvence budeme v dalším průběhu používat alias `e2-dae` a `e2-cli` pro odkaz na jiný adresář datadir než e1. Takže výše uvedený příklad pro naši druhou instanci `e2` by byl:

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir2
$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir2 getnewaddress
```

To nám umožní provádět nejrůznější operace, jako jsou transakce s aktivy mezi uzly, vydávání aktiv a kontrola použití zaslepení v důvěrných transakcích mezi různými uzly ve stejné síti.

# Použití prvku Praktický případ použití

<partId>3f31a30a-957a-4813-b5fe-5dccbb5366f3</partId>

## Důvěrné transakce

<chapterId>263b1c5b-59ed-49e7-b811-95c354f41eae</chapterId>

![Video](https://youtu.be/-by2xBtXQeE?si=7bLo_geGn3qh7MXN)

V této části se dozvíte, jak používat funkci Důvěrné transakce v aplikaci Elements.

Všechny adresy v Elements jsou ve výchozím nastavení zaslepeny pomocí důvěrných transakcí, díky nimž je množství a typ převedených aktiv viditelný pouze pro účastníky transakce (a ty, kterým se rozhodnou prozradit zaslepovací klíč), přičemž je stále kryptograficky zaručeno, že nelze utratit více mincí, než je k dispozici.

### Důvěrné adresy a důvěrné transakce

Ve výchozím nastavení je při vytváření nové adresy v prvcích Elements pomocí příkazu `getnewaddress` vytvořena jako důvěrná adresa.

Abychom demonstrovali důvěrné transakce, necháme e2 odeslat nějaké prostředky a poté se pokusíme zobrazit transakci z e1. Tím demonstrujeme důvěrnou povahu transakcí v systému Elements.

Každá nová adresa generovaná uzlem Elements je ve výchozím nastavení důvěrná. Můžeme to demonstrovat tak, že necháme e2 vygenerovat novou adresu.

```
e2-cli getnewaddress
```

Všimněte si, že adresa začíná písmenem e1. To ji označuje jako důvěrnou adresu. Podrobnější prozkoumání adresy pomocí příkazu getaddressinfo ukáže další podrobnosti o adrese.

```
e2-cli getaddressinfo <address>
```

Vidíte, že existuje vlastnost confidential_key, která nám říká, že se jedná o důvěrnou adresu.

Confidential_key je veřejný zaslepující klíč, který je přidán k samotné důvěrné adrese. To je důvod, proč je důvěrná adresa tak dlouhá.

Má také přidruženou nedůvěrnou adresu. Pokud si přejete používat běžné, nedůvěrné transakce v rámci prvků Elements, měly by být prostředky zasílány na tuto adresu namísto adresy s předponou lq1.

Nyní můžeme nechat systém e2 odeslat část prostředků na vygenerovanou adresu. To později ukáže, že e1, protože není jednou ze stran transakce, nebude moci zobrazit podrobnosti transakce.

```
e2-cli sendtoaddress <address>
```

Všimněte si ID transakce. Potvrďte transakci.

```
e2-cli -generate 101
```

Podíváme-li se na transakci, při níž si společnost e2 poslala nějaké prostředky, z pohledu samotné společnosti e2.

```
e2-cli gettransaction <txid>
```

Při procházení podrobností o transakci vidíte, že e2 může zobrazit odeslané a přijaté částky a také aktivum, které bylo předmětem transakce. Můžete také vidět vlastnosti amountblinder a assetblinder, které slouží k zaslepení podrobností od ostatních uzlů, které se na transakci nepodílejí.

Abychom mohli zkontrolovat podrobnosti téže transakce z e1, musíme nejprve získat nezpracované podrobnosti transakce.

```
e1-cli getrawtransaction <txid>
```

Ten vrací nezpracované údaje o transakci. Pokud se podíváte do sekce vout, uvidíte, že existují tři instance. První dvě instance jsou částky příjmu a změny a třetí je poplatek za transakci. Z těchto tří částek je poplatek jediná, u které můžete vidět hodnotu, protože samotný poplatek je v rámci prvků Elements vždy nezobrazen.

### Oslepující klíče

První dva oddíly vout ukazují "zaslepené rozsahy" hodnot a údaje o závazcích, které slouží jako důkaz skutečné částky a typu transakcí s aktivy.

I kdybychom importovali soukromý klíč e2 do peněženky e1, stále by nebyla schopna zjistit množství a typ transakcí, protože stále nezná zaslepující klíč používaný e2. Dokážeme to importem soukromého klíče používaného peněženkou e2 do peněženky e1. Nejprve musíme vyexportovat klíč z e2

```
e2-cli dumpprivkey <address>
```

Pak jej importujte do e1.

```
e1-cli importprivkey <privkey>
```

Nyní můžeme dokázat, že e1 stále nevidí hodnoty.

```
e1-cli gettransaction <txid>
```

Ve skutečnosti se jako částka tx zobrazuje 0, i když ve skutečnosti byla 1.

Abychom mohli zobrazit skutečnou, nezakrytou hodnotu, potřebujeme zakrývací klíč. Za tímto účelem nejprve vyexportujeme zaslepovací klíč z e2.

```
e2-cli dumpblindingkey <address>
```

Pak jej importujte do e1.

```
e1-cli importblindingkey <address> <blinding key>
```

Když nyní získáme údaje o transakci z e1.

```
e1-cli gettransaction <txid>
```

Ukazuje, že po importu zaslepovacího klíče můžeme nyní v rámci transakce zobrazit skutečnou hodnotu 1.

V této části jsme viděli, že použití zaslepovacího klíče skrývá množství a typ aktiv v transakci a že importem správného zaslepovacího klíče můžeme tyto hodnoty odhalit. V praktickém použití může být zaslepovací klíč například předán auditorovi, pokud by bylo třeba ověřit množství a typy aktiv v držení strany. Funkce Důvěrné transakce v prvcích také umožňuje provádět "důkazy rozsahu". Důkazy rozsahu mohou prokázat, že částka aktiva je držena v daném rozsahu, aniž by bylo nutné odhalit samotnou částku.

Viděli jsme také, že důvěrné transakce jsou volitelné, ale při generování nové adresy jsou ve výchozím nastavení povoleny.

To je pro tuto lekci vše; hodně štěstí při řešení kvízu a na shledanou v příští lekci!

## Vydaná aktiva

<chapterId>c33c7020-5975-457a-99db-4f8b90d1fa1c</chapterId>

![Video](https://youtu.be/XnY4WZUNSs4?si=dG8I5OoSh_0EBdvL)

V této části se dozvíte, jak používat funkci Vydané prostředky v prvcích Elements.

Vydaná aktiva umožňují vydávat a převádět více typů aktiv mezi účastníky sítě Elements. Každý uzel v síti může vydávat svá vlastní aktiva. Emitovaná aktiva mohou představovat zastupitelné vlastnictví jakéhokoli aktiva včetně poukázek, kupónů, měn, vkladů, dluhopisů, akcií atd. Vydaná aktiva otevírají dveře pro budování nedůvěryhodných burz, opcí a dalších pokročilých inteligentních kontraktů zahrnujících vlastní vydaná aktiva.

Vydané aktivum také využívá výhod důvěrných transakcí a může je znovu vydat kdokoli, kdo vlastní přidružený token.

V prvním kroku budeme potřebovat přístup ke dvěma uzlům Elements, které nazveme e1 a e2. Tyto uzly mají resetované blockchainy a výchozí aktiva jsou mezi ně rozdělena.

Oba uzly jsou ve stejné lokální síti a jsou vzájemně propojeny, a proto sdílejí stejné transakce ve svém transakčním mempoolu a identické blockchainy. Přestože běží na stejném počítači, je třeba poznamenat, že nesdílejí stejné skutečné soubory blockchainu. Každý uzel spravuje svou vlastní lokální kopii blockchainu, která obsahuje stejnou historii transakcí, protože jsou v konsensu a dodržují stejná pravidla protokolu jako ostatní.

Začněme kontrolou pohledu každého uzlu na stávající emise aktiv v síti.

To se provádí pomocí příkazu listissuances.

```
e1-cli listissuances
e2-cli listissuances
```

Jak vidíte, oba uzly vykazují stejnou historii vydávání. Oba zobrazují jedno aktivum, počáteční emisi 21 milionů bitcoinů, které byly vytvořeny při inicializaci řetězce. Ve výsledcích spuštění výše uvedeného příkazu můžete vidět hexadecimální ID aktiva a také označení přiřazené aktivu, které je "bitcoin".

Stojí za zmínku, že výchozímu aktivu je při inicializaci řetězce vždy přidělen štítek. Když vydáváte vlastní aktiva, můžete jim sami nastavit štítky, což brzy uděláme. Než tak budeme moci učinit, musíme vydat vlastní aktivum.

Necháme e1 vydat nové aktivum. To se provádí pomocí příkazu issueasset.

```
e1-cli issueasset 100 1 false
```

`issueasset` přijímá 3 parametry.

Částka nového aktiva k vydání, použili jsme 100. Množství tokenů k vytvoření (tokeny se používají k opětovnému vydání množství aktiva), z nichž jsme zvolili 1. Poslední parametr říká prvkům Elements, že mají emisi aktiv vytvořit buď jako zaslepenou, nebo nezaslepenou. My použijeme unblinded, protože chceme za chvíli zobrazit částky emise z e2, takže zadáme false.

Spuštění příkazu vrátí údaje o vydání. Patří mezi ně ID transakce, které si můžete zkopírovat pro pozdější použití, jedinečná hexadecimální hodnota aktiva a jedinečná hexadecimální hodnota tokenu aktiva.

Generování bloku pro potvrzení transakce vydání.

```
e1-cli -generate 1
```

Znovu spusťte příkaz `listissuances` proti e1.

```
e1-cli listissuances
```

To nám ukazuje, že e1 nyní ví o 2 emisích, o počáteční emisi bitcoinů a o našem nově vydaném aktivu, kterého vidíme 100 kusů. Všimněte si hexadecimální hodnoty nového aktiva a toho, že k němu není přiřazen žádný štítek aktiva, jako je tomu u emise bitcoinů.

Znovu se podívejte do seznamu známých vydání e2.

```
e2-cli listissuances
```

To nám ukazuje, že e2 neví o vydání aktiv, které provedla e1. Vidí pouze počáteční emisi bitcoinů, kterou již mohl vidět.

Je to proto, že e2 nezná a nesleduje adresu, na kterou bylo nové aktivum odesláno, když bylo vydáno e1.

Stojí za zmínku, že i když e2 nevidí samotnou emisi, e1 by přesto mohl poslat e2 část aktiva. Nové aktivum by se pak objevilo jako dostupný zůstatek v peněžence e2, i když o původní emisi neví.

Aby systém e2 mohl zobrazit skutečné vydání (a tedy i vydanou částku), je třeba přidat adresu do systému e2 jako sledovanou adresu.

K tomu potřebujeme zjistit adresu, na kterou byl majetek odeslán. K tomu použijeme ID transakce, které jsme si zkopírovali dříve, a necháme e1 načíst podrobnosti o této transakci, abychom mohli zjistit správnou adresu, kterou přidáme do seznamu sledovaných peněženek e2.

```
e1-cli gettransaction <the-issuance-transaction-id>
```

Po přejití nahoru za hexadecimální údaje transakce uvidíte adresu, která obdržela 100 našich nových aktiv, identifikovanou hexadecimální hodnotou.

Vezměte adresu a zkopírujte ji, abychom ji mohli importovat do e2.

Nyní importujme tuto adresu do systému e2. K tomu použijeme příkaz importaddress.

```
e2-cli importaddress <the-issued-to-address>
```

Pokud nyní zkontrolujeme seznam emisí e2.

```
e2-cli listissuances
```

Vidíte, že naše nově vydané aktivum je nyní zahrnuto v seznamu. Uzel e2 je také schopen určit částku vydaného aktiva spolu s částkou přidruženého tokenu, protože se jednalo o nezaslepenou emisi. Chcete-li v rámci prvků povolit použití mapování ID aktiva na název, nejprve zastavte prvek Elements.

```
e1-cli stop
```

Poté jej znovu spusťte s dalším parametrem, který mapuje hexadecimální kód aktiva na zadaný štítek. To uzlu umožní zobrazit nám údaje o aktivu v lidsky čitelnějším formátu. Pokud si to přejete, můžete tento parametr přidat na konec souboru elements.conf, pak nemusíte tento argument přidávat démonovi při každém spuštění. Například:

```
assetdir=5186d0bc8ed15e6ef85571bd2d8070573adf0e06fd4507082694526975ce4f35:My new asset (MNA)
```

Zde však použijeme metodu argumentů.

```
e1-dae -assetdir=<assetid-here>:<name-of-the-new-asset>
```

Opětovný dotaz na uzel pro seznam vydání.

```
e1-cli listissuances
```

To nám ukazuje, že mapování hexadecimální hodnoty aktiva na jeho popisek funguje. Znovu kontrolujeme seznam emisí uzlu e2.

```
e2-cli listissuances
```

Vidíte, že uzel e2 nemá k tomuto štítku přístup, protože štítky jsou dostupné pouze uzlu, který je nastavil. Ve skutečnosti můžeme stejnému hexu aktiva v uzlu e2 přiřadit jiný štítek než v uzlu e1. Nejprve zastavte uzel e2.

```
e2-cli stop
```

Restartování s jiným štítkem přiřazeným hexadecimálnímu kódu našeho nového aktiva.

```
e2-dae -assetdir=<assetid-here>:<another-name-for-the-new-asset>
```

Výpis emisí z e2.

```
e2-cli listissuances
```

Označení majetku je lokální pro každý uzel, ostatní uzly v síti rozpoznají pouze šestnáctku majetku.

Při provádění akcí, jako jsou transakce a dotazy na zůstatek peněženky, je užitečné mapování štítku na šestnáctinásobek aktiva, protože umožňuje zkrácený způsob odkazu na aktivum. Pokud bychom například chtěli poslat část našeho nového aktiva (částku 10) z e1 do e2 bez použití štítku.

Nejprve musíme získat adresu, na kterou se aktivum odešle.

```
e2-cli getnewaddress
```

Pak použijte příkaz sendtoaddress.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <asset-id-here>
```

Potvrzení transakce vygenerováním bloku.

```
generate 1
```

Kontrola, zda byl majetek přijat na e2.

```
e2-cli getwalletinfo
```

Vidíme, že aktivum bylo skutečně přijato.

Všimněte si, že e2 mapuje šestnáctkovou hodnotu přijatého aktiva a zobrazuje ji pomocí vlastního štítku. Jednodušší způsob, jak provést stejnou věc, by bylo použít při odesílání štítek aktiva e1.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <name-of-the-new-asset>
```

V pozadí aplikace Elements mapuje místní štítky na hexadecimální hodnoty, což usnadňuje používání vydaných prostředků.

V této části jsme si ukázali, jak vydávat a označovat aktiva. V příštím oddíle se podíváme na opětovné vydávání a ničení množství vydaného aktiva.

## Opětovné vydávání aktiv

<chapterId>78751b21-1dc8-4877-a406-e71bc80a95b0</chapterId>

![Video](https://youtu.be/5em79YHtYk0?si=rhponm6Hw9AB6RJp)

V této části se dozvíte, jak vydat více již vydaného aktiva a jak zničit dané množství vydaného aktiva.

Potřeba znovu vydat (vytvořit další) aktivum nebo zničit jeho množství je něco, co pravděpodobně nastane, pokud aktivum představuje něco, co nemá stálou nabídku. To by se mohlo týkat například aktiv, která představují zlato uložené v trezoru; jak se jednotky zlata pohybují dovnitř a ven z trezoru, aktivum představující zásobu trezoru se musí odpovídajícím způsobem upravit nahoru nebo dolů.

Opětovné vydání určitého množství aktiva vyžaduje vlastnictví souvisejícího tokenu, který byl vytvořen spolu s aktivem při jeho původním vydání.

Při vytváření většího množství aktiva nezáleží na tom, který uzel aktivum vydal jako první, pokud uzel, který aktivum znovu vydává, vlastní tzv. reissuance token aktiva. Podíváme se na to, jak na začátku vytvořit reissuance token, jak jej použít k reemisi množství aktiva a také jak reissuance token přenést do jiných uzlů, aby i ony měly oprávnění k reemisi aktiva.

Budeme potřebovat přístup ke dvěma uzlům Elements, které nazveme e1 a e2. Tyto uzly mají resetované blockchainy a výchozí aktiva jsou mezi ně rozdělena.

Necháme e1 vydat 100 kusů nového aktiva a vytvoříme 1 token pro opětovné vydání téhož aktiva. Pro zjednodušení příkladu vytvoříme emisi jako nezaslepenou. Pokračujme tedy v emisi aktiva a s ním spojeného tokenu reemise.

```
e1-cli issueasset 100 1 false
```

Všimněte si ID aktiva a také ID tokenu (opětovného vydání).

Protože později budeme z e2 znovu vydávat další aktiva, musíme si poznamenat ID transakce, ve které byla aktiva vydána, a použít je k importu adresy, na kterou byla aktiva odeslána.

Potvrďte transakci.

```
e1-cli -generate 1
```

Nyní zkontrolujeme podrobnosti transakce pomocí příkazu gettransaction:

```
e1-cli gettransaction <txid>
```

Když projdete nahoru za šestnáctinovou část dat transakce, uvidíte, že v transakci e1 obdržel 1 reissuance token a 100 přidružených aktiv.

Pořiďte si kopii adresy, abychom ji mohli importovat do systému e2.

A nyní import adresy do peněženky e2.

```
e2-cli importaddress <address>
```

Nyní vidíme, že jak e1, tak e2 vědí o emisi aktiv.

```
e1-cli listissuances
e2-cli listissuances
```

V současné době e1 drží určitou částku aktiva a 1 žeton opětovné emise, ale e2 nikoli.

```
e1-cli getwalletinfo
```

Všimněte si také, že e1 má méně výchozího aktiva než dříve, protože zaplatila malou částku na pokrytí transakčních poplatků. Tuto částku má e1 inkasovat, až bude vytvořený blok dospělý do hloubky více než 100 bloků.

```
e2-cli getwalletinfo
```

Protože e1 drží reissuance token, může jich znovu vydat více. To se provádí pomocí příkazu reissueasset. Nechť e1 znovu vydá dalších 100 kusů aktiva.

```
e1-cli reissueasset <asset-id> 100
```

Kontrola opětovného vydání fungovala.

```
e1-cli getwalletinfo
```

Vidíte, že e1 nyní podle očekávání drží 200 aktiv.

Vzhledem k tomu, že společnost e2 nedisponuje částkou tokenu opětovného vydání, obdrží chybu, pokud se pokusí aktivum opětovně vydat.

```
e2-cli reissueasset <asset-id> 100
```

Všimněte si chybové zprávy.

Podrobnosti o opětovném vydání z e1 můžeme zobrazit pomocí příkazu listissuances.

```
e1-cli listissuances
```

Všimněte si příznaku `is_reissuance`.

Pokud nyní pošleme společnosti e2 částku tokenu reemise, bude moci sama reemitovat částku aktiva. Nejprve potřebujeme adresu, na kterou ji pošleme. Stojí za zmínku, že s reissuance tokenem se při odesílání a zobrazování zůstatků zachází stejně jako s jakýmkoli jiným aktivem v rámci elementů a že jej lze také rozdělit na menší nominální hodnoty jako jakékoli jiné aktivum, takže nemusíme posílat 1 reissuance token do e2, aby mohl aktivum znovu vydat. Postačí jakákoli nominální hodnota. Vygenerování adresy, na kterou má e2 obdržet reissuance token.

```
e2-cli getnewaddress
```

Poté pošlete zlomek RIT z e1 do e2.

```
e1-cli sendtoaddress <address-of-e2> 0.1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Potvrďte transakci.

```
e1-cli -generate 1
```

Nyní vidíme, že e2 má hodnotu 0,1, která mu byla zaslána.

```
e2-cli getwalletinfo
```

To znamená, že e2 nyní může znovu vydat více aktiv spojených s RIT, které drží ve své peněžence. Necháme e2 znovu vydat 500 kusů aktiva.

```
e2-cli reissueasset <asset-id> 500
```

Zkontrolujte výsledek opětovného vydání.

```
e2-cli getwalletinfo
```

Vidíte, že e2 nyní drží znovu vydanou částku ve svém zůstatku peněženky a že samotný RIT není v procesu opětovného vydání aktiva spotřebován.

Zničení určitého množství aktiva může provést každý, kdo drží alespoň množství, které je předmětem zničení, a neřídí se žetonem opětovné emise.

```
e2-cli destroyamount <asset-id>
e2-cli getwalletinfo
```

V této části jsme se seznámili s tím, jak vydat aktivum a jak využít žeton opětovného vydání, který je volitelně vytvořen jako součást vydání aktiva. Viděli jsme také, že převod tokenu reissuance je stejně jednoduchý jako převod jakéhokoli jiného aktiva a že držení jakéhokoli množství tokenu reissuance dává držiteli právo vydat další přidružené aktivum. Je proto velmi důležité kontrolovat, kdo má v síti přístup k reissuance tokenům. Viděli jsme také, jak zničit množství aktiva a že tento proces není kontrolován držením tokenu reissue.

# Element Federation

<partId>173a2440-0203-4dcc-8e2b-f8fa2cc8d3ca</partId>

## Podepisování bloků

<chapterId>c47b217e-db14-4843-a66f-3e5f3a00a808</chapterId>

![Video](https://youtu.be/kxWX91fCnus?si=KItm_Am3_RrBcLBN)

Elements podporuje model federativního podepisování, který umožňuje určit počet členů Strong Federation, kteří musí podepsat navrhovaný blok, aby byl blok platný.

Dříve jsme pro zjednodušení vytvářeli bloky pomocí příkazu `generate`, který nemusel splňovat požadavek na více podpisů, aby vytvořené bloky byly sítí akceptovány jako platné.

Nastavíme naše uzly tak, aby vyžadovaly vytváření vícesignálových bloků 2 z 2. To nastavíme pomocí parametru signblockscript, který lze přidat do konfiguračního souboru nebo předat uzlu při spuštění. Abychom mohli inicializovat řetězec s tímto parametrem, musíme nejprve vytvořit skript, ze kterého se skládá.

Provedeme to pomocí některých existujících uzlů, uložíme data, která vypisují, a pak řetězec smažeme, abychom jej mohli znovu spustit pomocí parametru signblockscript. To je nezbytné, protože skript tvoří součást pravidel konsensu sítě a bude třeba jej nastavit při inicializaci řetězce. Nelze jej později přidat do již existujícího řetězce.

Budeme potřebovat přístup ke dvěma uzlům Elements, které nazveme e1 a e2. Tyto uzly mají resetované blockchainy a výchozí aktiva jsou mezi ně rozdělena.

Ujistěte se, že parametr con_max_block_sig_size je v souboru elements.conf nastaven na vysokou hodnotu, jinak se podepisování bloků později v této části nezdaří. Pro tento návod jsme nastavili con_max_block_sig_size=2000.

Vzhledem k tomu, že budeme resetovat blockchain a vymazávat peněženky spojené s e1 a e2, budeme si muset pořídit kopii adres, veřejných a soukromých klíčů, které používáme k vygenerování skriptu pro podepisování bloků, abychom je mohli použít později.

Nejprve je třeba, aby každý z uzlů, které budou podepisovat bloky, vygeneroval novou adresu, jejíž kopii je třeba pořídit.

```
e1-cli getnewaddress
e2-cli getnewaddress
```

Poté musíme z adres získat veřejné klíče a zaznamenat je pro pozdější použití.

```
e1-cli getaddressinfo <e1-address>
e2-cli getaddressinfo <e2-address>
```

Poté získáme soukromé klíče, které později znovu importujeme, aby uzly mohly podepisovat bloky poté, co znovu inicializujeme náš blockchain a data peněženky.

```
e1-cli dumpprivkey <e1-address>
e2-cli dumpprivkey <e2-address>
```

Nyní potřebujeme vygenerovat skript pro vykoupení s požadavky na 2 ze 2 více podpisů. To provedeme pomocí příkazu createmultisig, kterému předáme první parametr 2 a poté zadáme dva veřejné klíče. Právě tyto klíče potřebuje vlastnictví prokázat později při vytváření bloku.

Kterýkoli uzel, e1 nebo e2, může generovat multisig.

```
e1-cli createmultisig 2 '["<e1-pubkey>", "<e2-pubkey>"]'
```

Tím získáme náš redeemscript, který si můžete zkopírovat pro pozdější použití.

Nyní musíme vymazat stávající blockchain a data peněženky, abychom mohli začít znovu s novým signblockscriptem jako součástí pravidel konsensu řetězce. Proto jsme dříve potřebovali pořídit kopii některých dat, například soukromých klíčů, které se budou v novém řetězci používat k podepisování bloků. To je třeba udělat předtím, než budete pokračovat.

Po smazání stávajících dat peněženky a řetězce můžeme nyní spustit naše uzly a nechat je inicializovat nový řetězec pomocí parametru signblockscript. Předáme parametr -evbparams=dynafed:0:::, abychom aktivaci dynafedu zakázali, protože pro tento příklad tuto pokročilou funkci nepotřebujeme.

```
e1-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
e2-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
```

Nyní musíme importovat soukromé klíče, které jsme uložili dříve, aby naše uzly mohly podepisovat a pomáhat dokončit všechny navrhované bloky.

```
e1-cli importprivkey <e1-priv-key>
e2-cli importprivkey <e2-priv-key>
```

Použití příkazu generate by nyní mělo být chybné, protože nesplňuje požadovaná pravidla pro podepisování bloků, která jsou nyní vynucována našimi uzly.

```
e1-cli -generate 1
```

Pro navržení nového bloku může kterýkoli uzel zavolat příkaz getnewblockhex. Ten vrátí hexadecimální kód nového bloku, který bude muset být podepsán předtím, než jej uzly v naší síti přijmou.

```
e1-cli getnewblockhex
```

Nezapomeňte, že příkaz pouze vytvoří navrhovaný blok, ale nevytvoří jej.

Pro potvrzení tohoto tvrzení můžeme vidět, že v našem blockchainu v současné době nejsou žádné bloky.

```
e1-cli getblockcount
```

Pokud se pokusíme odeslat blok hex bez předchozího podpisu.

```
e1-cli submitblock <block-hex>
```

Zobrazí se zpráva, že důkaz bloku je neplatný. Je to proto, že ještě nebyl podepsán dvěma z požadovaných dvou stran.

Přimějme tedy e1, aby navrhovaný blok podepsal.

```
e1-cli signblock <block-hex>
```

Nechte e2 podepsat hex.

```
e2-cli signblock <block-hex>
```

Všimněte si, že e2 nepodepisuje výstup vytvořený podpisem navrženého bloku e1. Oba podepíší navržený blok hex nezávisle na výsledcích toho druhého.

Nyní musíme zkombinovat blokové signatury e1 a e2. To může provést kterýkoli uzel, potřebuje pouze podepsaný šestnáctkový blok z druhého uzlu.

```
e1-cli combineblocksigs <block-hex> '["<signed-hex-from-e1>", "<signed-hex-from-e2>"]'
```

Vidíte, že příkaz combineblocksigs vypíše hexadecimální kód podepsaného bloku a také stav complete, který nám říká, že hexadecimální kód bloku je připraven k odeslání.

Nyní může kterýkoli uzel odeslat dokončený blok hex. My to necháme udělat e1.

```
e1-cli submitblock <combined-signed-hex>
```

Kontrola, zda bylo podání platné.

```
e1-cli getblockcount
e2-cli getblockcount
```

Vidíte, že e1 i e2 přijaly blok jako platný a přidaly jej na konec svých lokálních kopií blockchainu.

Shrnutí procesu. V této části máme:


- Navrhl blok.
- Každý uzel ji podepsal.
- Kombinované podpisy.
- Zkontroloval, zda jsou podpisy platné a zda splňují prahovou hodnotu pro redeemscript řetězce.
- Předložil blok.

Každý uzel v síti blok ověřil a přidal jej do své lokální kopie blockchainu.

### Block SIgning

Ačkoli se proces zpočátku zdá složitý, posloupnost podepisování bloků v systému Elements je vždy stejná a počáteční nastavení je třeba provést pouze jednou:

1. Počáteční nastavení (provádí se jednou)

2. Vytvoří se adresa pro více podpisů s názvem `signblockscript` pomocí veřejných klíčů federovaných blokových podepisovačů.

3. Skript redeem z něj slouží ke spuštění nového blockchainu.

4. Bloková výroba (probíhá)

5. Navrhované bloky jsou generovány a vyměňovány k podpisu.

Jakmile navrhovaný blok podepíše určitý počet signatářů, je spojen a předán do sítě. Pokud splňuje kritéria `signblockscript` řetězce, uzly jej přijmou jako platný blok.

## Prvek jako vedlejší řetězec

<chapterId>432d7a65-255f-44a3-8b38-78508202cb37</chapterId>

![Video](https://youtu.be/egYzj4N8CB8?si=v7_-IXsjHPE-ARDe)

Elements je blockchainová platforma s otevřeným zdrojovým kódem pro všeobecné použití, kterou lze také připojit k existujícímu blockchainu, jako je například Bitcoin. Když je Elements připojen k jinému blockchainu, říká se, že funguje jako `sidechain`. Sidechainy umožňují obousměrný převod aktiv z jednoho řetězce do druhého. Implementace Elements jako sidechainu umožňuje obejít některá omezení vlastní mainchainu a zároveň zachovat značnou míru bezpečnosti, kterou poskytují aktiva zajištěná v mainchainu.

Zatímco vedlejší řetězec má povědomí o hlavním řetězci a jeho transakční historii, hlavní řetězec o vedlejším řetězci povědomí nemá a pro jeho fungování není potřeba. To umožňuje sidechainům inovovat bez omezení a zpoždění spojených s návrhy na vylepšení protokolu mainchainu. Spíše než snaha o jeho přímou změnu umožňuje rozšíření hlavního protokolu, aby samotný mainchain zůstal bezpečný a specializovaný, což je základem hladkého fungování sidechainu.

Rozšířením funkcí Bitcoinu a využitím jeho základního zabezpečení může sidechain založený na prvcích poskytovat nové funkce, které dříve nebyly uživatelům hlavního řetězce k dispozici. Příkladem produkčně využívaného sidechainu založeného na prvcích je síť Liquid Network.

Abychom mohli inicializovat blockchain Elements jako sidechain, musíme použít parametr federated peg script. Tento parametr lze nastavit v konfiguračním souboru uzlu nebo jej předat při spuštění.

Skript federativního peg definuje, kteří členové silné federace mohou provádět funkce peg-in a peg-out. Tito členové jsou označováni jako "hlídači", protože sledují hlavní řetězec a postranní řetězec, zda v nich nejsou platné transakce peg-in a peg-out, a pokud jsou platné, provádějí je. `Peg-out` znamená přesunout zastavená aktiva z postranního řetězce do hlavního řetězce a `peg-in` znamená přesunout zastavená aktiva z hlavního řetězce do postranního řetězce. Když říkáme `přesunout do sidechainu`, myslíme tím vlastně to, že se prostředky uzamknou v multi-signature adrese v mainchainu a odpovídající množství aktiv se vytvoří v sidechainu Elements. Když říkáme `move out of the sidechain`, myslíme tím, že aktiva jsou zničena na sidechainu Elements a odpovídající částka je uvolněna ze zamčených prostředků držených na mainchainu. Oprávnění k provádění funkcí peg-in a peg-out vyžaduje, aby funkcionáři prokázali vlastnictví veřejných klíčů použitých ve federativním skriptu peg. To se provádí pomocí odpovídajících soukromých klíčů.

Abychom mohli vytvořit sdružený skript peg, musíme nejprve nechat každý z našich uzlů vygenerovat veřejný klíč. Musíme také uložit související soukromé klíče pro pozdější použití, protože budeme muset vymazat všechna existující data řetězce a inicializovat nový řetězec pomocí skriptu federated peg. Je to proto, že skript federated peg tvoří součást pravidel konsensu postranního řetězce a nelze jej později použít na existující, nepegovaný blockchain.

Vygenerujme tedy adresu s každým z našich uzlů, uložme příslušná data pro pozdější použití a vygenerujme skript federated peg, který později použijeme k inicializaci našeho sidechainu.

Nejprve je třeba, aby každý z našich uzlů, které budou v naší síti fungovat jako Strážci, vygeneroval novou adresu.

```
e1-cli getnewaddress
e2-cli getnewaddress
```

Poté adresu ověříme a získáme veřejné klíče.

```
e1-cli getaddressinfo <e1-address>
e2-cli getaddressinfo <e2-address>
```

A poté načtěte soukromé klíče přiřazené k jednotlivým adresám.

```
e1-cli dumpprivkey <e1-address>
e2-cli dumpprivkey <e2-address>
```

Soukromý a veřejný klíč uložte pro pozdější použití.

Nyní musíme vymazat stávající blockchain a data peněženky, protože budeme inicializovat nový řetězec pomocí skriptu federated peg. To můžete provést nyní. Nezapomeňte spustit démona Bitcoinu, kterého budeme potřebovat k pegování.

Nyní můžeme inicializovat nový řetězec pomocí skriptu federovaného kolíku vytvořeného pomocí veřejných klíčů, které jsme uložili dříve. Čísla, která zadáme a která obklopují naše veřejné klíče, definují a vymezují počet použitých klíčů a vlastnictví klíčů, které je třeba prokázat, aby bylo možné peg-in a out z našeho sidechainu.

```
e1-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
e2-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
```

Nyní naimportujeme soukromé klíče, které jsme předtím uložili, aby naše uzly mohly později podepsat a dokončit přenos aktiv mezi řetězci a splnit požadavky skriptu federativního kolíku.

```
e1-cli importprivkey <priv-key-1>
e2-cli importprivkey <priv-key-1>
```

Nyní je třeba vyzkoušet některé bloky na obou řetězcích. Zralost bloků je požadavkem procesu peg, protože chrání před reorganizací bloků v hlavním řetězci, která by vedla k inflaci nabídky pegovaných aktiv v rámci sidechainu.

Abychom se v této části zaměřili na sdružený kolík, budeme generovat bloky bez použití modelu podepisování bloků, kterému jsme se věnovali v minulé části, a vrátíme se k použití příkazu "generate" pro vytváření nových bloků.

```
b-cli generate 101
e1-cli generate 1
```

Bloky pro prvky nemusíme nutně generovat hned. Ale přesto si jeden vygenerujme. Je to dobrý postup, abychom se vyhnuli případným nesrovnalostem.

Nyní je náš řetěz připraven k zavěšení. Pro peg-in musíme vygenerovat speciální druh adresy pomocí příkazu getpeginaddress. Všimněte si, že doba mezi vygenerováním adresy peg-in příkazem getpeginaddress a jejím nárokováním příkazem claimpegin by měla být co nejkratší. adresy peg-in nejsou dlouhodobě trvanlivé a neměly by se používat opakovaně.

```
e1-cli getpeginaddress
```

Vidíte, že příkaz vytvoří novou adresu hlavního řetězce a také nový skript, který bude třeba uspokojit, aby bylo možné nárokovat prostředky z peg-in. Adresa mainchainu je adresa `pay to script hash`, kterou budou používat funkcionáři plnící roli hlídače v síti Elements.

Stejně jako getnewaddress přidává getpeginaddress do peněženky volajícího uzlu nový secret, takže je důležité do procesu správy uzlu zahrnout zálohování souboru peněženky.

Nyní pošleme několik bitcoinů z hlavního řetězce do vedlejšího řetězce. Naše peněženka pro regresní testování mainchainu již obsahuje nějaké prostředky.

```
b-cli getwalletinfo
```

Vidíme, že peněženka obsahuje 50 bitcoinů. Jeden bitcoin pošleme z hlavního řetězce do vedlejšího řetězce. Potřebujeme poslat prostředky na adresu mainchainu, kterou náš uzel vygeneroval dříve.

```
b-cli sendtoaddress <e1-pegin-address>
```

ID této transakce si musíme uchovat, protože ho později budeme potřebovat k prokázání financování.

Nyní vidíme, že zůstatek v peněžence mainchain se snížil o částku, kterou jsme poslali, plus další malou částku na pokrytí poplatků za transakce.

```
b-cli getwalletinfo
```

Musíme transakci znovu dokončit.

```
b-cli generate 101
```

Aby náš uzel Elements mohl nárokovat prostředky peg-in, musíme získat `důkaz`, že transakce peg-in byla provedena. Kryptografický důkaz používá ID transakce financování k výpočtu merkelovy cesty a dokazuje, že se transakce nachází v potvrzeném bloku.

```
b-cli gettxoutproof '["<tx-id>"]'
```

Potřebujeme také nezpracované údaje o transakcích.

```
b-cli getrawtransaction <tx-id>
```

S důkazem a nezpracovanými daty pro transakci peg-in může nyní náš uzel s prvky nárokovat peg-in pomocí nezpracované transakce a důkazu transakce.

```
e1-cli claimpegin <raw> <proof>
```

Všimněte si, že existuje nepovinný třetí argument, který jsme mohli zadat do claimpegin. Tento třetí parametr lze použít k určení adresy postranního řetězce, na kterou se mají zaslat nárokované prostředky. V našem příkladu to nebylo potřeba, protože jsme příkaz volali ze stejného uzlu, který vlastní adresu, na kterou jsou nárokované prostředky zasílány.

Kontrola zůstatku e1.

```
e1-cli getwalletinfo
```

Generování bloku pro potvrzení nároku.

```
e1-cli generate 1
```

Kontrola zůstatku e1.

```
e1-cli getwalletinfo
```

Vidíme, že se podařilo úspěšně reklamovat kolík.

Při vytahování kolíčků je postup podobný. Je vygenerována adresa, na kterou jsou zaslány finanční prostředky, a pokud je transakce platná, jsou finanční prostředky uvolněny. Celým procesem peg-out se nebudeme zabývat, protože zahrnuje práci v hlavním řetězci, která je nad rámec tohoto kurzu. Kroky z hlediska událostí prvků jsou následující: V hlavním řetězci je vygenerována adresa.

```
b-cli getnewaddress
```

Prostředky jsou odesílány na adresu mainchain z uzlu Elements pomocí příkazu sendtomainchain.

```
e1-cli sendtomainchain <new-address> 1
```

Generování bloku pro potvrzení transakce.

```
e1-cli generate 1
```

Zkontrolujte zůstatek v peněžence uzlu.

```
e1-cli getwalletinfo
```

A uvidíte, že se zůstatek snížil.

V této části jsme si ukázali, jak:


- Generování skriptu sdruženého kolíku.
- Inicializuje nový řetězec, který používá skript jako pravidlo parametru konsensu sítě.
- Odeslání prostředků z mainchainu do sidechainu.
- Nárok na prostředky v rámci postranního řetězce Elements.
- Pochopte, jak se spouští odesílání prostředků zpět do hlavního řetězce.

### FederatedPegScript

Aby Elements mohl fungovat jako sidechain, musí být blok genesis v jeho blockchainu vytvořen s `fedpegscriptem`. To se provádí předáním parametru `fedpegscript` při spuštění uzlu. Skript pak bude tvořit součást pravidel konsensu blockchainu Elements a umožní ověřování a provádění požadavků na peg-in a peg-out.

`fedpegscript` se skládá z veřejných klíčů, které jsou kontrolovány osobami oprávněnými k provádění akcí peg. Následující příklad ukazuje formát fedpegscriptu s více podpisy 2 z 2:

```
fedpegscript=5221<public key 1>21<public key 2>52ae
```

Poznámka: Znaky mimo veřejné klíče jsou oddělovače, které označují požadavky na veřejný klíč a `n z m`. Například šablona pro 1 z 1 fedpegscript by byla '5121<pub key 1>51ae'.

### Peg-in

Než může být peg-in přijat vedlejším řetězcem Elements, musí mít dostatečný počet potvrzení v hlavním řetězci. To je nezbytné, aby se zabránilo inflaci v nabídce pegovaného aktiva v sidechainu Elements, která by mohla být způsobena reorganizací mainchainu.

V rámci běžného fungování konsensuálního mechanismu Proof of Work (PoW) se očekávají krátké reorganizace hrotu bitcoinového blockchainu. Jako takový uznává Elements peg-in za platný pouze tehdy, když má v rámci bitcoinového blockchainu dostatečnou hloubku. To slouží k tomu, aby Elements nepřijal stejný peg-in více než jednou.

### Peg-Out

K peg-outu dojde, když uzel Elements zavolá příkaz `sendtomainchain`, který jako vstupní údaj přijme adresu mainchainu (cíl peg-outu) a také částku pegovaného aktiva, která má být `vyčerpána`. Tím se na vedlejším řetězci vytvoří transakce peg-out. Jakmile Funkcionáři, kteří plní funkci Hlídačů, zjistí, že transakce peg-out byla na sidechainu potvrzena, postarají se o skutečné uvolnění aktiva na mainchainu do cíle peg-out, jak jsme se učili v předchozích částech kurzu.

## Prvky jako samostatný blockchain

<chapterId>50dff39b-2702-47d7-9c15-0b54b845e99f</chapterId>

![Video](https://youtu.be/u-3rV7DGtD0?si=G1__H0Uelf4sTUDM)

Dosud jsme se zabývali tím, jak spustit Elements jako postranní řetězec. Může však fungovat i jako samostatné blockchainové řešení s vlastním výchozím nativním aktivem. V tomto nastavení si blockchain Elements stále zachovává všechny funkce implementace sidechainu, jako jsou důvěrné transakce a emitovaná aktiva, ale nepotřebuje peg-in nebo peg-out k přidávání nebo odebírání výchozího množství aktiv z oběhu.

V této části se budeme věnovat:

Inicializace nového blockchainu Elements s výchozím aktivem s názvem `newasset`.

Zadejte 1 000 000 `newasset`, který má být vytvořen spolu se 2 žetony pro jeho opětovné vydání.

Získejte všechny mince `newasset`, které může utratit kdokoli.

Požádejte o všechny žetony reissuance, které může kdokoli utratit, pro 'newasset'.

Odeslání aktiva a jeho reissuance tokenu do peněženky jiného uzlu.

Znovu vydat další 'newasset' z obou uzlů.

Aby bylo možné inicializovat síť Elements tak, aby fungovala jako samostatný blockchain, musí být každý uzel spuštěn s několika základními parametry. Ty slouží k tomu, aby uzlu sdělil, že se nemá pokoušet validovat peg-iny z jiného blockchainu, název výchozího aktiva sítě a množství výchozího aktiva a souvisejícího reissue tokenu, který má vytvořit.

Nyní spustíme nový řetězec s použitím těchto parametrů na našich dvou propojených uzlech Elements. Výchozí aktivum pojmenujeme `newasset` a vydáme jich jeden milion a dva žetony `newasset` pro opětovné vydání.

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
e2-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

Všimněte si, že zde použité částky jsou v nejmenší nominální hodnotě, kterou může síť přijmout, takže dvě stě milionů reissue tokenů se ve skutečnosti rovná dvěma celým tokenům. Totéž platí pro nominální hodnotu počátečních volných mincí.

Zkontrolujte aktuální zůstatky v peněžence našeho uzlu.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Vidíme, že inicializace proběhla správně.

Protože počáteční emise aktiv je vytvořena jako `kdokoli může utrácet`, necháme e1, aby si je všechny nárokoval, abychom mohli e2 odebrat přístup k nim.

```
e1-cli getnewaddress
e1-cli sendtoaddress <e1-address> 1000000 "" "" true
```

Všimněte si, že jako aktivum k odeslání nemusíme zadávat "newasset", protože se již jedná o výchozí aktivum, a tedy i výchozí aktivum používané k placení síťových poplatků.

V rámci služby Elements lze na stejnou adresu odeslat více typů aktiv, takže můžeme znovu použít adresu, kterou jsme právě vygenerovali pro příjem výchozího aktiva, a použít ji jako cílovou adresu pro tokeny pro opětovné vydání.

```
e1-cli sendtoaddress <e1-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Potvrzení transakcí.

```
e1-cli generate 101
```

Zkontrolujeme, zda je e1 jediným držitelem aktiva a jeho tokenu opětovného vydání.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Jak vidíme, je tomu skutečně tak.

Nyní pošleme část "newasset" na účet e2, který má v současné době nulový zůstatek.

```
e2-cli getnewaddress
e1-cli sendtoaddress <e2-address> 500 "" "" false
```

Všimněte si, že jsme nemuseli zadávat typ aktiva, které má být odesláno, protože `newasset` bylo vytvořeno jako výchozí aktivum sítě

Pošleme do e2 také některé tokeny reissuance pro `newasset`.

```
e1-cli sendtoaddress <e2-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Potvrzení transakcí.

```
e1-cli generate 101
```

Můžeme zkontrolovat, zda byly peněženky odpovídajícím způsobem aktualizovány.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Nyní znovu vystavíme některé výchozí aktivum z e1. Všimněte si, že tuto možnost umožňuje spouštěcí parametr initialreissuancetokens. Který, pokud je vynechán nebo nastaven na nulu, způsobí, že výchozí aktivum nebude možné později znovu vydat.

```
e1-cli reissueasset newasset 100
```

Mohli jsme použít označení `newasset` místo zadávání hodnoty hexadecimálního id, protože řetězec prvků vždy označuje své výchozí aktivum.

Kontrola, zda opětovné vydání výchozího aktiva fungovalo:

```
e1-cli generate 101
e1-cli getwalletinfo
```

Nyní prokážeme, že protože e2 drží některé žetony `newasset` pro reemisi, může také reemitovat výchozí aktivum.

```
e2-cli reissueasset newasset 100
```

Kontrola, zda opětovné vydání výchozího aktiva společností e2 fungovalo.

```
e2-cli generate 101
e2-cli getwalletinfo
```

V této části jsme nastavili Elements jako samostatný blockchain a ověřili, že základní funkce fungují tak, jak bychom očekávali.

Spouštěcí parametry jsme použili k:

Inicializace nového blockchainu Elements s výchozím aktivem s názvem 'newasset'.

Zadejte množství výchozího aktiva, které se má vytvořit při inicializaci řetězce.

Vytvořte několik žetonů pro opětovné vydání výchozího aktiva a vydejte další výchozí aktivum z obou uzlů.

V naší samostatné síti blockchain Elements budou všechny ostatní transakční operace fungovat stejným způsobem jako příklady uvedené v hlavních částech kurzu, ale jako výchozí a zpoplatněné aktivum se bude používat "newasset" místo "bitcoin".

### Parametry spouštění uzlů a inicializace řetězce

Aby uzel Elements fungoval jako samostatný blockchain, je třeba použít několik parametrů. Na každý z nich se nyní podíváme a zjistíme, k čemu slouží.

#### `validatepegin=0`

Protože samostatný blockchain nepotřebuje ověřovat transakce peg-in nebo peg-out, musíme tyto kontroly vypnout. Při tomto nastavení není třeba spouštět klientský software Bitcoin ani ukládat kopii blokového řetězce Bitcoin, protože síť Elements bude fungovat nezávisle.

#### `defaultpeggedassetname`

To umožňuje zadat název výchozího aktiva vytvořeného při inicializaci blockchainu.

#### `initialfreecoins`

Počet (v ekvivalentu jednotky Satoshi bitcoinu) výchozího aktiva, které se má vytvořit.

#### `první vydání karty`

Počet (v ekvivalentu jednotky Satoshi bitcoinu) žetonů pro opětovné vydání pro výchozí aktivum, které se má vytvořit. Bez něj by nebylo možné vytvořit další výchozí aktivum. Pokud nechcete, aby bylo možné vytvořit více výchozích aktiv, lze tento údaj nastavit na nulu nebo vynechat.

Při použití těchto parametrů by společný postup pro spuštění uzlu vypadal následovně:

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

### Základní operace

Parametr `defaultpeggedassetname` použije na výchozí aktivum štítek. Bez tohoto nastavení bude výchozí aktivum automaticky pojmenováno `bitcoin`. V předchozích částech jsme při odesílání aktiv, která jsme sami vydali, do jiného uzlu museli zadat buď hexadecimální kód aktiva, nebo lokálně použitý štítek aktiva, abychom Elements sdělili, které aktivum posíláme. Protože `defaultpeggedassetname` platí pro všechny uzly, nemusíme jej při odesílání pojmenovávat, i když jeho název není `bitcoin`. Každá funkce, která by předtím ve výchozím nastavení odeslala `bitcoin`, nyní odešle to, co jste zvolili jako označení výchozího aktiva.

Odeslání 10 nových výchozích aktiv na adresu je tedy jednoduché:

```
e1-cli sendtoaddress <destination address> 10 "" "" true
```

Pokud jste také uzlu zadali hodnotu `initialreissuancetokens` větší než nula, budete moci znovu vydat více výchozích aktiv, což není možné, pokud spustíte Elements jako sidechain.

K tomu stačí, aby jakýkoli uzel, který drží množství tokenu přidruženého k výchozímu aktivu, vydal příkaz ve tvaru:

```
e1-cli reissueasset <default asset name> <amount>
```

Pomocí výše uvedených parametrů můžete Elements provozovat jako samostatný blockchain s vlastním výchozím aktivem, oddělený od Bitcoinu a ostatních blockchainů.

## Závěr

<chapterId>7e2c916d-8114-424c-97f5-cbff9d73b8e3</chapterId>

![Video](https://youtu.be/CTMdamTZBBM?si=16LBcXvN4pBfC7lr)

V tomto kurzu jsme se dozvěděli, že Elements je open-source síťový protokol, který lze implementovat jako sidechain k jinému blockchainu nebo jako samostatné blockchainové řešení.

Viděli jsme, že zdrojový kód a webové stránky pro Elements (https://github.com/ElementsProject/elements) jsou umístěny na GitHubu a že existují komunitní diskusní fóra, jako je Build On L2(https://community.liquid.net/c/developers/) nebo Liquid Developers Telegram (https://t.me/liquid_devel), která lze využít k získání dalších informací o nasazování a vývoji aplikací v systémech Elements a Liquid. Byly popsány klíčové funkce, jako jsou důvěrné transakce a vydávaná aktiva, a také to, jak členové silné federace umožňují federativní podepisování bloků a mechanismus 2-Way Peg.

Dalším krokem bude kumulativní kvíz, který se týká všech předchozích částí, a pak se vydáte na cestu k prvkům... hodně štěstí!

# Závěr

<partId>d5dbd616-e291-42bc-aae3-6c44599dbd06</partId>

## Recenze a hodnocení

<chapterId>beae23bd-2fd1-49fe-8f38-ed169acde51d</chapterId>

<isCourseReview>pravdivé</isCourseReview>

## Závěr

<chapterId>15f62056-c69c-467e-9565-af48d439a1f5</chapterId>

Gratulujeme k dokončení kurzu!

Jsme nadšeni, že jste úspěšně dosáhli tohoto milníku na své cestě za vzděláním. Díky svému nasazení a angažovanosti jste získali cenné znalosti a dovednosti, které vám dobře poslouží ve vašem profesním rozvoji.