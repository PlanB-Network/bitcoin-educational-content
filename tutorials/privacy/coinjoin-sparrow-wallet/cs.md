---
name: Coinjoin - Sparrow Wallet
description: Jak provést coinjoin pomocí Sparrow Wallet?
---
![cover](assets/cover.webp)

***VAROVÁNÍ:** Po zatčení zakladatelů Samourai Wallet a zabavení jejich serverů 24. dubna již nástroj Whirlpool nefunguje, a to ani pro jednotlivce, kteří mají vlastní Dojo nebo používají Sparrow Wallet. Stále však existuje možnost, že by tento nástroj mohl být v nadcházejících týdnech obnoven nebo spuštěn jiným způsobem. Navíc teoretická část tohoto článku zůstává relevantní pro pochopení principů a cílů coinjoinů obecně (nejen Whirlpool), stejně jako pro pochopení efektivity modelu Whirlpool.*

_Sledujeme vývoj této kauzy stejně jako vývoj souvisejících nástrojů. Ujistěte se, že tento tutoriál aktualizujeme, jakmile budou k dispozici nové informace._

_Tento tutoriál je poskytován pouze pro vzdělávací a informační účely. Nepodporujeme ani nevyzýváme k používání těchto nástrojů pro kriminální účely. Je zodpovědností každého uživatele dodržovat zákony ve své jurisdikci._

---

V tomto tutoriálu se dozvíte, co je coinjoin a jak jej provést pomocí softwaru Sparrow Wallet a implementace Whirlpool.

## Co je coinjoin na Bitcoinu?
**Coinjoin je technika, která narušuje sledovatelnost bitcoinů na blockchainu**. Spoléhá na spolupráci v transakci se specifickou strukturou stejného názvu: transakce coinjoin.

Coinjoiny zvyšují soukromí uživatelů Bitcoinu tím, že komplikují analýzu řetězce pro vnější pozorovatele. Jejich struktura umožňuje sloučení více mincí od různých uživatelů do jedné transakce, čímž se zaměňují stopy a stává se obtížné určit vazby mezi vstupními a výstupními adresami.

Princip coinjoinu je založen na spolupráci: několik uživatelů, kteří si přejí smíchat své bitcoiny, vloží stejné částky jako vstupy téže transakce. Tyto částky jsou poté jako výstupy stejné hodnoty rozděleny mezi každého uživatele. Na konci transakce se stává nemožným spojit konkrétní výstup s známým uživatelem na vstupu. Mezi vstupy a výstupy neexistuje přímá vazba, což narušuje spojení mezi uživateli a jejich UTXO, stejně jako historii každé mince.
![coinjoin](assets/notext/1.webp)

Příklad transakce coinjoin (ne ode mě): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

Pro provedení coinjoinu, při kterém každý uživatel neustále udržuje kontrolu nad svými prostředky, začíná proces sestavením transakce koordinátorem, který ji poté přenáší každému účastníkovi. Každý uživatel poté transakci podepíše po ověření, že mu vyhovuje. Všechny shromážděné podpisy jsou nakonec integrovány do transakce. Pokud se uživatel nebo koordinátor pokusí o přesměrování prostředků prostřednictvím úpravy výstupů transakce coinjoin, podpisy se stanou neplatnými, což povede k zamítnutí transakce uzly.

Existuje několik implementací coinjoinu, jako jsou Whirlpool, JoinMarket nebo Wabisabi, každá s cílem řídit koordinaci mezi účastníky a zvýšit efektivitu transakcí coinjoin.
V tomto tutoriálu se zaměříme na implementaci **Whirlpool**, kterou považuji za nejefektivnější řešení pro provádění coinjoinů na Bitcoinu. Ačkoli je dostupná v několika peněženkách, tento tutoriál se výhradně věnuje jejímu použití s desktopovým softwarem Sparrow Wallet.

## Proč provádět CoinJoins na Bitcoinu?

Jedním z počátečních problémů jakéhokoli peer-to-peer platebního systému je dvojí utrácení: jak zabránit zlomyslným jedincům v opakovaném utrácení stejných peněžních jednotek bez nutnosti obracet se na centrální autoritu pro rozhodčí řízení?

Satoshi Nakamoto poskytl řešení tohoto dilematu prostřednictvím protokolu Bitcoin, peer-to-peer elektronického platebního systému, který funguje nezávisle na jakékoli centrální autoritě. Ve své bílé knize zdůrazňuje, že jediný způsob, jak ověřit absenci dvojího utrácení, je zajistit viditelnost všech transakcí v rámci platebního systému.

Aby byl každý účastník informován o transakcích, musí být veřejně zveřejněny. Takto fungování Bitcoinu spočívá na transparentní a distribuované infrastruktuře, která umožňuje jakémukoli operátoru uzlu ověřit celost řetězců elektronických podpisů a historii každé mince od jejího vytvoření těžařem.

Transparentní a distribuovaná povaha blockchainu Bitcoinu znamená, že jakýkoli uživatel sítě může sledovat a analyzovat transakce všech ostatních účastníků. Anonymita na úrovni transakcí je tedy nemožná. Avšak anonymita je zachována na úrovni individuální identifikace. Na rozdíl od tradičního bankovního systému, kde je každý účet spojen s osobní identitou, na Bitcoinu jsou prostředky spojeny s páry kryptografických klíčů, čímž uživatelům nabízí určitou formu pseudonymity za kryptografickými identifikátory.

Proto je důvěrnost na Bitcoinu ohrožena, když vnější pozorovatelé dokážou spojit konkrétní UTXO s identifikovanými uživateli. Jakmile je tato asociace navázána, stává se možné sledovat jejich transakce a analyzovat historii jejich bitcoinů. Coinjoin je přesně technika vyvinutá k přerušení sledovatelnosti UTXO, čímž nabízí určitou úroveň důvěrnosti uživatelům Bitcoinu na úrovni transakcí.

## Jak funguje Whirlpool?

Whirlpool se od ostatních metod coinjoin odlišuje použitím transakcí "_ZeroLink_", které zajišťují, že mezi všemi vstupy a výstupy technicky není možné vytvořit žádnou přímou spojitost. Toto dokonalé míchání je dosaženo prostřednictvím struktury, kde každý účastník přispívá stejnou částkou na vstupu (kromě těžebních poplatků), čímž generuje výstupy dokonale stejných částek.

Tento restriktivní přístup k vstupům dává transakcím coinjoin Whirlpool jedinečnou charakteristiku: úplnou absenci deterministických spojení mezi vstupy a výstupy. Jinými slovy, každý výstup má stejnou pravděpodobnost, že bude přiřazen jakémukoli účastníku, ve srovnání se všemi ostatními výstupy transakce.
Původně byl počet účastníků v každém coinjoinu Whirlpool omezen na 5, s 2 novými účastníky a 3 remixéry (tyto koncepty vysvětlíme později). Avšak zvýšení poplatků za on-chain transakce pozorované v roce 2023 přimělo týmy Samourai k přehodnocení jejich modelu za účelem zlepšení soukromí při snižování nákladů. S ohledem na tržní situaci poplatků a počet účastníků může koordinátor nyní organizovat coinjoins zahrnující 6, 7 nebo 8 účastníků. Tyto rozšířené sezení jsou označovány jako "_Surge Cycles_". Je důležité poznamenat, že bez ohledu na nastavení jsou v coinjoinech Whirlpool vždy pouze 2 noví účastníci.

Transakce Whirlpool jsou tedy charakterizovány identickým počtem vstupů a výstupů, které mohou být:
- 5 vstupů a 5 výstupů;
![coinjoin](assets/notext/2.webp)
- 6 vstupů a 6 výstupů;
![coinjoin](assets/notext/3.webp)
- 7 vstupů a 7 výstupů;
![coinjoin](assets/notext/4.webp)
- 8 vstupů a 8 výstupů. ![coinjoin](assets/notext/5.webp)
Model navržený Whirlpool se tedy zakládá na malých transakcích coinjoin. Na rozdíl od Wasabi a JoinMarket, kde robustnost anonymních setů závisí na objemu účastníků v jednom cyklu, Whirlpool sází na řetězení několika malých cyklů.

V tomto modelu uživatel platí poplatky pouze při svém prvním vstupu do poolu, což jim umožňuje účastnit se mnoha remixů bez dalších poplatků. Noví účastníci jsou ti, kdo nesou těžební poplatky za remixéry.

S každým dalším coinjoinem, ve kterém se mince účastní spolu se svými dříve potkanými partnery, budou anonymní sety exponenciálně růst. Cílem je tedy využít těchto bezplatných remixů, které při každém výskytu přispívají ke zvýšení hustoty anonymních setů spojených s každou smíchanou mincí.

Whirlpool byl navržen s ohledem na dvě důležité požadavky:
- Dostupnost implementace na mobilních zařízeních, vzhledem k tomu, že Samourai Wallet je primárně aplikace pro smartphone;
- Rychlost cyklů remixování pro podporu významného nárůstu anonymních setů.

Tyto imperativy vedly vývojáře Samourai Wallet při návrhu Whirlpool k omezení počtu účastníků na cyklus. Příliš málo účastníků by ohrozilo účinnost coinjoinu, drasticky snížilo by anonymní sety generované s každým cyklem, zatímco příliš mnoho účastníků by představovalo problémy s řízením na mobilních aplikacích a bránilo by průběhu cyklů.

**Nakonec není nutné mít vysoký počet účastníků na coinjoin na Whirlpool, protože anonymní sety jsou vytvářeny akumulací několika cyklů coinjoin.**
[-> Zjistěte více o anonymních setech Whirlpool.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)
### Coinjoin pooly a poplatky
Aby se zajistilo, že několik cyklů skutečně zvýší anonymní sety smíchaných mincí, musí být stanoven určitý rámec pro omezení použitých UTXO. Whirlpool pro tento účel definuje různé pooly.

Pool představuje skupinu uživatelů, kteří si přejí smíchat dohromady, a dohodnou se na množství UTXO k použití pro optimalizaci procesu coinjoin. Každý pool určuje pevnou částku pro UTXO, které se uživatel musí držet, aby se mohl zúčastnit. Takže pro provádění coinjoinů s Whirlpool potřebujete vybrat pool. Aktuálně dostupné pooly jsou následující:
- 0,5 bitcoinu;
- 0,05 bitcoinu;
- 0,01 bitcoinu;
- 0,001 bitcoinu (= 100 000 sats).

Připojením do poolu se vaše bitcoiny rozdělí na generování UTXO, které jsou dokonale homogenní s těmi od ostatních účastníků v poolu. Každý pool má maximální limit; takže pro částky přesahující tento limit budete nuceni buď provést dvě samostatné vstupy v rámci stejného poolu nebo přejít do jiného poolu s vyšší částkou:

| Pool (bitcoin) | Maximální částka na vstup (bitcoin) |
|----------------|------------------------------------|
| 0,5            | 35                                 |
| 0,05           | 3,5                                |
| 0,01           | 0,7                                |
| 0,001          | 0,025                              |
Jak bylo zmíněno dříve, UTXO je považováno za součást poolu, když je připraveno být začleněno do coinjoinu. To ovšem neznamená, že uživatel o něj přichází. **Prostřednictvím různých cyklů míchání si uchováváte plnou kontrolu nad svými klíči a tedy i nad svými bitcoiny.** To je to, co odlišuje techniku coinjoin od jiných centralizovaných technik míchání.

Pro vstup do coinjoin poolu je nutné zaplatit servisní poplatky a také poplatky za těžbu. Servisní poplatky jsou pro každý pool pevně stanoveny a mají za úkol kompenzovat týmy odpovědné za vývoj a údržbu Whirlpoolu. Uživatelé Sparrow Walletu tyto poplatky předávají týmům Samourai vývojářům Sparrow.

Servisní poplatky za použití Whirlpoolu se platí jednou při vstupu do poolu. Jakmile je tento krok dokončen, máte možnost účastnit se neomezeného počtu remixů bez dalších poplatků. Zde jsou aktuální pevné poplatky pro každý pool:

| Pool (bitcoin) | Vstupní poplatek (bitcoin) |
|----------------|----------------------------|
| 0.5            | 0.0175                     |
| 0.05           | 0.00175                    |
| 0.01           | 0.0005 (50,000 sats)       |
| 0.001          | 0.00005 (5,000 sats)       |


Tyto poplatky v podstatě fungují jako vstupenka do vybraného poolu, bez ohledu na částku, kterou do coinjoinu vložíte. Takže, ať už vstoupíte do poolu 0.01 s přesně 0.01 BTC nebo vstoupíte s 0.5 BTC, poplatky zůstanou stejné v absolutní hodnotě.

Před provedením coinjoinů má uživatel tedy na výběr mezi 2 strategiemi:
- Zvolit menší pool, aby minimalizoval servisní poplatky, s vědomím, že obdrží několik malých UTXO;
- Nebo dát přednost většímu poolu, souhlasit s vyššími poplatky, aby nakonec získal menší počet UTXO s vyšší hodnotou.

Obecně se nedoporučuje slučování několika smíchaných UTXO po cyklech coinjoinu, protože by to mohlo ohrozit získanou důvěrnost, zejména kvůli heuristice společného vlastnictví vstupu (CIOH). Proto by mohlo být moudré zvolit větší pool, i když to znamená platit více, aby se předešlo mnoha UTXO s malou hodnotou na výstupu. Uživatel musí tyto kompromisy zvážit, aby si vybral preferovaný pool.

Kromě servisních poplatků je nutné zohlednit také poplatky za těžbu, které jsou neodmyslitelnou součástí jakékoli transakce s Bitcoinem. Jako uživatel Whirlpoolu budete muset zaplatit poplatky za těžbu pro přípravnou transakci (`Tx0`) stejně jako ty pro první coinjoin. Všechny následující remixy budou zdarma, díky modelu Whirlpoolu, který se opírá o platby nových účastníků.

Ve skutečnosti, v každém coinjoinu Whirlpoolu jsou dva uživatelé mezi vstupy noví účastníci. Ostatní vstupy pocházejí od remixérů. V důsledku toho jsou poplatky za těžbu pro všechny účastníky transakce pokryty těmito dvěma novými účastníky, kteří poté také těží z bezplatných remixů:
![coinjoin](assets/en/6.webp)
Díky tomuto systému poplatků se Whirlpool skutečně odlišuje od ostatních služeb coinjoin, protože anonsety UTXO nejsou proporcionální k ceně zaplacené uživatelem. Takto je možné dosáhnout výrazně vysokých úrovní anonymity, a to pouze zaplacením vstupních poplatků do poolu a poplatků za těžbu za dvě transakce (za `Tx0` a počáteční mix).
Je důležité poznamenat, že uživatel bude muset také pokrýt těžební poplatky za vybrání svých UTXO z poolu po dokončení jejich několika coinjoinů, pokud si nevybral možnost `mix to`, o které budeme diskutovat v následujícím tutoriálu.
### Účty HD peněženky používané Whirlpoolem
Pro provedení coinjoinu prostřednictvím Whirlpoolu musí peněženka generovat několik odlišných účtů. Účet v kontextu HD (Hierarchické Deterministické) peněženky představuje sekci, která je zcela izolovaná od ostatních, přičemž tato separace nastává na třetí úrovni hloubky hierarchie peněženky, tj. na úrovni `xpub`.
HD peněženka může teoreticky odvodit až `2^(32/2)` různých účtů. Počáteční účet, používaný ve výchozím nastavení ve všech Bitcoinových peněženkách, odpovídá indexu `0'`.

Pro peněženky přizpůsobené Whirlpoolu, jako jsou Samourai nebo Sparrow, se používají 4 účty, aby vyhověly potřebám procesu coinjoin:
- Účet **deposit** (vklad), identifikovaný indexem `0'`;
- Účet **bad bank** (nebo doxxic change), identifikovaný indexem `2 147 483 644'`;
- Účet **premix**, identifikovaný indexem `2 147 483 645'`;
- Účet **postmix**, identifikovaný indexem `2 147 483 646'`.

Každý z těchto účtů plní specifickou funkci v rámci coinjoinu.

Všechny tyto účty jsou spojeny s jedním seedem, což umožňuje uživateli obnovit přístup ke všem svým bitcoinům pomocí své obnovovací fráze a případně svého hesla. Je však nutné při této obnovovací operaci software specifikovat různé použité indexy účtů.

Podívejme se nyní na různé fáze coinjoinu Whirlpool v těchto účtech.

### Různé fáze coinjoinů na Whirlpoolu
**Fáze 1: Tx0**
Výchozím bodem jakéhokoli coinjoinu Whirlpool je účet **deposit**. Tento účet automaticky používáte, když vytvoříte novou Bitcoinovou peněženku. Na tento účet musí být připsány bitcoiny, které si přejete smíchat.

`Tx0` představuje první fázi procesu míchání Whirlpool. Cílem je připravit a vyrovnat UTXO pro coinjoin tím, že je rozdělí na jednotky odpovídající částce vybraného poolu, aby se zajistila homogenita míchání. Vyrovnané UTXO jsou poté odeslány na účet **premix**. Pokud jde o rozdíl, který nemůže vstoupit do poolu, je oddělen do specifického účtu: **bad bank** (nebo "doxxic change").

Tato počáteční transakce `Tx0` slouží také k úhradě služebních poplatků koordinátoru míchání. Na rozdíl od následujících fází tato transakce není kolaborativní; uživatel musí tedy převzít plné těžební poplatky:
![coinjoin](assets/en/7.webp)
V tomto příkladu transakce `Tx0` je vstup `372,000 sats` z našeho účtu **deposit** rozdělen na několik odchozích UTXO, které jsou distribuovány následovně:
- Částka `5,000 sats` určená koordinátorovi za služební poplatky, odpovídající vstupu do poolu `100,000 sats`;
- Tři UTXO připravené pro míchání, přesměrované na náš účet **premix** a zaregistrované u koordinátora. Tyto UTXO jsou vyrovnány na `108,000 sats` každý, aby pokryly těžební poplatky pro jejich budoucí počáteční mix;
- Přebytek, který nemůže vstoupit do poolu, protože je příliš malý, je považován za toxickou změnu. Je poslán na jeho specifický účet. Zde tato změna činí `40,000 sats`;
- Nakonec jsou zde `3,000 sats`, které netvoří výstup, ale jsou to těžební poplatky nutné k potvrzení `Tx0`.

Například zde je skutečný Tx0 Whirlpool (který není ode mě): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

**Krok 2: Toxická změna**
Přebytek, který se nemohl integrovat do poolu, zde ekvivalentní `40,000 sats`, je přesměrován na účet **špatné banky**, také označovaný jako "toxická změna", aby se zajistilo striktní oddělení od ostatních UTXO v peněžence.

Toto UTXO je nebezpečné pro soukromí uživatele, protože nejenže je vždy spojeno se svou minulostí, a tedy možná s identitou jeho majitele, ale navíc je označeno jako patřící uživateli, který provedl coinjoin.

Pokud je toto UTXO sloučeno se smíšenými výstupy, tyto ztratí veškeré soukromí získané během cyklů coinjoin, zejména kvůli CIOH (*Common-Input-Ownership-Heuristic*). Pokud je sloučeno s dalšími toxickými změnami, uživatel riskuje ztrátu soukromí, protože to spojí různé vstupy cyklů coinjoin. Musí být tedy zacházeno s opatrností. Způsob, jakým se má tímto toxickým UTXO zacházet, bude podrobně popsán v poslední části tohoto článku a budoucí tutoriály se budou těmto metodám na PlanB Network věnovat hlouběji.

**Krok 3: Počáteční míchání**
Po dokončení `Tx0` jsou vyrovnány UTXO poslány na **premix** účet naší peněženky, připraveny být zavedeny do jejich prvního cyklu coinjoin, také nazývaného "počáteční míchání". Pokud, jak je tomu v našem příkladu, `Tx0` generuje několik UTXO určených pro míchání, každé z nich bude integrováno do samostatného počátečního coinjoinu.
Na konci těchto počátečních míchání bude **premix** účet prázdný, zatímco naše mince, které zaplatily těžební poplatky za tento první coinjoin, budou přesně upraveny na částku definovanou vybraným poolem. V našem příkladu budou naše počáteční UTXO `108 000 sats` sníženy přesně na `100 000 sats`.
![coinjoin](assets/en/8.webp)
**Krok 4: Remixy**
Po počátečním míchání jsou UTXO převedeny na **postmix** účet. Tento účet shromažďuje již smíšené UTXO a ty, které čekají na remixování. Když je klient Whirlpool aktivní, UTXO umístěné na **postmix** účtu jsou automaticky k dispozici pro remixování a budou náhodně vybrány k účasti na těchto nových cyklech.

Připomínáme, že remixy jsou poté 100% zdarma: nejsou vyžadovány žádné další poplatky za službu ani těžební poplatky. Udržení UTXO na **postmix** účtu tak udržuje jejich hodnotu nedotčenou a zároveň zlepšuje jejich anonsety. Proto je důležité umožnit těmto mincím účastnit se několika cyklů coinjoin. Nestojí vás to absolutně nic a zvyšuje jejich úroveň anonymity.
Když se rozhodnete utratit smíšené UTXO, můžete tak učinit přímo z tohoto **postmix** účtu. Je doporučeno držet smíšená UTXO na tomto účtu, abyste mohli využívat bezplatných remixů a zabránili jejich odchodu z oběhu Whirlpool, což by mohlo snížit jejich soukromí.
Jak uvidíme v následujícím tutoriálu, existuje také možnost `mix to`, která nabízí možnost automaticky poslat vaše smíšené mince do jiné peněženky, například do studené peněženky, po definovaném počtu coinjoinů.

Po diskuzi o teorii se ponořme do praxe s tutoriálem na používání Whirlpool prostřednictvím desktopového softwaru Sparrow Wallet!

## Tutoriál: Coinjoin Whirlpool na Sparrow Wallet
Existuje mnoho možností, jak používat Whirlpool. První, kterou vám chci představit, je možnost Sparrow Wallet, open-source software pro správu Bitcoin peněženky pro PC.
Používání Sparrow má tu výhodu, že je poměrně snadné začít, rychle se nastaví a vyžaduje kromě počítače a internetového připojení žádné další vybavení. Nicméně, existuje významná nevýhoda: coinjoiny se uskuteční pouze tehdy, když je Sparrow spuštěn a připojen. To znamená, že pokud chcete míchat a remixovat vaše bitcoiny 24/7, budete muset neustále nechat váš počítač zapnutý.

### Instalace Sparrow Wallet
Začněte tím, že samozřejmě budete potřebovat software Sparrow Wallet. Můžete ho přímo stáhnout z [oficiálních stránek](https://sparrowwallet.com/download/) nebo na [jejich GitHubu](https://github.com/sparrowwallet/sparrow/releases).

Před instalací softwaru bude důležité ověřit podpis a integritu staženého spustitelného souboru. Pokud chcete více informací o procesu instalace a ověření softwaru Sparrow, doporučuji si přečíst tento další tutoriál: *[The Sparrow Wallet Guides](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607)*

### Vytvoření softwarové peněženky
Po instalaci softwaru budete muset pokračovat ve vytvoření Bitcoin peněženky. Je důležité poznamenat, že pro účast na coinjoinech je nezbytné použití softwarové peněženky (také nazývané "hot wallet"). Proto **nebude možné provádět coinjoiny s peněženkou zabezpečenou hardware peněženkou**.

Ačkoli to není nezbytné, v případě, že plánujete míchat významné částky, je vysoce doporučeno zvolit použití silné BIP39 fráze pro tuto peněženku.

Pro vytvoření nové peněženky otevřete Sparrow, poté klikněte na záložku `File` a `New Wallet`.

![sparrow](assets/notext/9.webp)

Vyberte název pro tuto peněženku, například: "Coinjoin Wallet". Klikněte na tlačítko `Create Wallet`.

![sparrow](assets/notext/10.webp)

Ponechte výchozí nastavení, poté klikněte na tlačítko `New or Imported Software Wallet`.

![sparrow](assets/notext/11.webp)

Když se dostanete do okna pro vytvoření peněženky, doporučuji vybrat sekvenci 12 slov, protože je to více než dostatečné. Vyberte `Generate New` pro generování nové obnovovací fráze a klikněte na `Use Passphrase`, pokud si přejete přidat BIP39 frázi. Je důležité udělat fyzickou zálohu vašich obnovovacích informací, ať už na papíře nebo na kovovém nosiči, aby byla zajištěna bezpečnost vašich bitcoinů.

![sparrow](assets/notext/12.webp)
Před kliknutím na `Confirm Backup...` ověřte platnost vaší zálohy obnovovací fráze. Sparrow vás poté požádá, abyste svou frázi znovu zadali pro ověření, že jste si ji vzali na vědomí. Po dokončení tohoto kroku pokračujte kliknutím na `Create Keystore`.
![sparrow](assets/notext/13.webp)
Ponechte navrhovanou cestu derivace jako výchozí a stiskněte `Import Keystore`. V mém příkladu se cesta derivace mírně liší, protože používám Testnet pro tento tutoriál. Cesta derivace, která by se vám měla zobrazit, je následující:
```plaintext
m/84'/0'/0'
```

![sparrow](assets/notext/14.webp)

Poté Sparrow zobrazí detaily derivace vaší nové peněženky. V případě, že jste nastavili heslovou frázi, je vysoce doporučeno si poznamenat váš `Master fingerprint`. Ačkoliv tento otisk hlavního klíče není citlivá data, bude pro vás užitečný pro pozdější ověření, že skutečně přistupujete ke správné peněžence a pro potvrzení absence chyb při zadávání heslové fráze.

Klikněte na tlačítko `Apply`.

![sparrow](assets/notext/15.webp)

Sparrow vás vyzve k vytvoření hesla pro vaši peněženku. Toto heslo bude vyžadováno pro přístup k ní prostřednictvím softwaru Sparrow Wallet. Vyberte silné heslo, udělejte si jeho zálohu a poté klikněte na `Set Password`.

![sparrow](assets/notext/16.webp)

### Přijímání bitcoinů
Po vytvoření vaší peněženky budete mít zpočátku jediný účet s indexem `0'`. To je **vkladový** účet, o kterém jsme mluvili v předchozích částech. To je účet, na který budete potřebovat poslat bitcoiny k mixování.

K tomu vyberte záložku `Receive` na levé straně okna. Sparrow automaticky vygeneruje novou prázdnou adresu pro přijímání bitcoinů.

![sparrow](assets/notext/17.webp)

Můžete zadat štítek pro tuto adresu a poté na ni poslat bitcoiny k mixování.

![sparrow](assets/notext/18.webp)

### Provádění Tx0
Jakmile je vaše transakce potvrzena, můžete přejít na záložku `UTXOs`.

![sparrow](assets/notext/19.webp)

Dále vyberte UTXO(s), které chcete předložit do cyklů coinjoin. Pro současné vybrání více UTXO držte stisknutou klávesu `Ctrl` při klikání na UTXO vaší volby.

![sparrow](assets/notext/20.webp)

Poté klikněte na tlačítko `Mix Selected` na spodní části okna. Pokud se toto tlačítko nezobrazuje ve vašem rozhraní, je to proto, že používáte peněženku zabezpečenou hardwarovou peněženkou. Pro provádění coinjoinů se Sparrow musíte použít softwarovou peněženku.
![sparrow](assets/notext/21.webp)
Otevře se okno, které vysvětluje, jak Whirlpool funguje. To je zjednodušení toho, co jsem vysvětlil v předchozích částech. Klikněte na `Next` a pokračujte.

![sparrow](assets/notext/22.webp)

Na další stránce můžete zadat "SCODE", pokud jej máte. SCODE je propagační kód, který nabízí slevu na poplatcích za službu poolu. Samourai Wallet občas poskytuje takové kódy svým uživatelům během speciálních událostí. Doporučuji vám [sledovat Samourai Wallet](https://twitter.com/SamouraiWallet) na sociálních médiích, abyste nepřišli o budoucí SCODES.
Na stejné stránce budete také muset nastavit sazbu poplatku pro `Tx0` a váš první mix. Toto rozhodnutí ovlivní rychlost potvrzení vaší přípravné transakce a vašeho prvního coinjoinu. Pamatujte, že jste zodpovědní za těžební poplatky pro `Tx0` a počáteční mix, ale za následné remixy již těžební poplatky platit nebudete. Přizpůsobte posuvník `Premix Priority` podle vašich preferencí, poté klikněte na `Next`.
![sparrow](assets/notext/23.webp)

V tomto novém okně budete mít možnost vybrat pool, do kterého chcete vstoupit, pomocí rozbalovacího seznamu. V mém případě, když jsem původně vybral UTXO `456 214 sats`, je mojí jedinou možnou volbou pool `100 000 sats`. Toto rozhraní vás také informuje o servisních poplatcích, které je třeba zaplatit, stejně jako o počtu UTXO, které budou do poolu začleněny. Pokud se vám podmínky zdají uspokojivé, pokračujte kliknutím na `Preview Premix`.

![sparrow](assets/notext/24.webp)

Po tomto kroku vás Sparrow požádá o zadání hesla k vaší peněžence, které jste nastavili při jejím vytváření v softwaru. Po zadání hesla získáte náhled vašeho `Tx0`. Na levé straně okna uvidíte, že Sparrow vygeneroval různé účty potřebné pro použití Whirlpool (`Deposit`, `Premix`, `Postmix` a `Badbank`). Budete mít také příležitost prohlédnout si strukturu vašeho `Tx0`, s různými výstupy:
- Servisní poplatky;
- Vyrovnané UTXO určené k vstupu do poolu;
- Toxická změna (Doxxic Change).

![sparrow](assets/notext/25.webp)

Pokud vám transakce vyhovuje, klikněte na `Broadcast Transaction` k odeslání vašeho `Tx0`. V opačném případě máte možnost upravit parametry tohoto `Tx0` výběrem `Clear` k vymazání zadaných dat a začít proces vytváření od začátku.

### Provádění Coinjoinů
Jakmile je Tx0 odeslán, najdete vaše UTXO připravené k mixování v účtu `Premix`.
![sparrow](assets/notext/26.webp)

Jakmile je `Tx0` potvrzen, vaše UTXO budou zaregistrována u koordinátora a počáteční mixy začnou automaticky postupně.

![sparrow](assets/notext/27.webp)

Kontrolou účtu `Postmix` pozorujete UTXO vzniklé z počátečních mixů. Tyto mince zůstanou připraveny na následné remixování, které nebude vyžadovat žádné další poplatky.

![sparrow](assets/notext/28.webp)

Ve sloupci `Mixes` je možné vidět počet coinjoinů provedených každou vaší mincí. Jak uvidíme v následujících částech, co skutečně záleží, není tolik počet remixů jako takových, ale spíše přidružené anonsety, ačkoli tyto dva ukazatele jsou částečně související.

![sparrow](assets/notext/29.webp)

Pro dočasné zastavení coinjoinů jednoduše klikněte na `Stop Mixing`. Máte možnost kdykoliv obnovit operace výběrem `Start Mixing`.

![sparrow](assets/notext/30.webp)
Aby bylo zajištěno nepřetržité dostupnost vašich UTXO pro remixování, je nutné nechat software Sparrow aktivní. Uzavření softwaru nebo vypnutí počítače pozastaví coinjoiny. Řešením, jak tomuto problému předejít, je zakázání funkce spánku prostřednictvím nastavení operačního systému. Kromě toho Sparrow nabízí možnost zabránit automatickému přechodu počítače do režimu spánku, kterou najdete pod záložkou `Nástroje` s názvem `Zabránit spánku počítače`.
![sparrow](assets/notext/31.webp)

### Dokončení coinjoinů
Pro utrácení vašich smíchaných bitcoinů máte několik možností. Nejpřímější metodou je přístup k účtu `Postmix` a výběr záložky `Odeslat`.

![sparrow](assets/notext/32.webp)

V této sekci budete mít možnost zadat cílovou adresu, částku k odeslání a poplatky za transakci stejným způsobem jako u jakékoli jiné transakce provedené s Sparrow Wallet. Pokud chcete, můžete také využít pokročilých funkcí soukromí, jako je Stonewall, kliknutím na tlačítko `Soukromí`.

![sparrow](assets/notext/33.webp)

[-> Zjistěte více o transakcích Stonewall.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)

Pokud si přejete provést přesnější výběr vašich mincí k utracení, přejděte na záložku `UTXO`. Vyberte UTXO, které konkrétně chcete spotřebovat, a poté stiskněte tlačítko `Odeslat vybrané` pro zahájení transakce.

![sparrow](assets/notext/34.webp)
Nakonec možnost `Mix do...` dostupná ve Sparrow umožňuje automatické odstranění vybraného UTXO z cyklů coinjoin, bez dalších poplatků. Tato funkce umožňuje určit počet remixů, po kterých nebude UTXO reintegrováno do vašeho účtu `Postmix`, ale místo toho bude přímo převedeno do jiné peněženky. Tato možnost je často používána k automatickému odesílání smíchaných bitcoinů do studené peněženky.
Pro použití této možnosti nejprve otevřete vedle vaší coinjoin peněženky v softwaru Sparrow příjemcovu peněženku.

![sparrow](assets/notext/35.webp)

Poté přejděte na záložku `UTXO` a vyberte mince, které vás zajímají, poté klikněte na tlačítko `Mix do...` na spodní části okna.

![sparrow](assets/notext/36.webp)

Otevře se okno, začněte výběrem cílové peněženky ze seznamu.

![sparrow](assets/notext/37.webp)

Vyberte práh coinjoinu, po jehož překročení bude výběr proveden automaticky. Nemohu vám dát přesný počet remixů k provedení, protože to se liší podle vaší osobní situace a cílů soukromí, ale vyhněte se výběru příliš nízkého prahu. Doporučuji se poradit s tímto dalším článkem, abyste se dozvěděli více o procesu remixování: [REMIX - WHIRLPOOL](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)

Možnost `Rozsah indexu` můžete nechat na její výchozí hodnotě, `Plný`. Tato funkce umožňuje míchání současně z různých klientů, ale to není to, co chceme v tomto tutoriálu dělat. Pro dokončení a aktivaci možnosti `Mix do...` stiskněte `Restartovat Whirlpool`.

![sparrow](assets/notext/38.webp)

Buďte však opatrní při používání možnosti `Mix do`, protože odstranění smíchaných mincí z vašeho účtu `Postmix` může výrazně zvýšit riziko ohrožení vašeho soukromí. Důvody pro tuto možnost jsou podrobně popsány v následujících sekcích.

## Jak poznat kvalitu našich cyklů coinjoin?
Aby byl coinjoin skutečně účinný, je zásadní, aby prezentoval dobrou homogenitu mezi množstvím vstupů a výstupů. Tato uniformita zvyšuje počet možných interpretací v očích vnějšího pozorovatele, čímž se zvyšuje nejistota kolem transakce. Pro kvantifikaci této nejistoty generované coinjoinem lze využít výpočet entropie transakce. Pro hlubší průzkum těchto ukazatelů vás odkazuji na tutoriál: [BOLTZMANN CALCULATOR](https://planb.network/en/tutorials/privacy/boltzmann-entropy). Model Whirlpool je uznáván jako ten, který přináší největší homogenitu v coinjoinech. Dále je hodnocen výkon několika cyklů coinjoin na základě velikosti skupin, ve kterých je mince skryta. Velikost těchto skupin definuje to, co se nazývá anonsety. Existují dva typy anonsetů: první hodnotí získané soukromí proti retrospektivní analýze (od současnosti do minulosti) a druhý, proti prospektivní analýze (od minulosti do současnosti). Pro podrobné vysvětlení těchto dvou ukazatelů vás zvu, abyste si přečetli tutoriál: [WHIRLPOOL STATS TOOLS - ANONSETY](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

## Jak spravovat postmix?
Po provedení cyklů coinjoin je nejlepší strategií uchovávat vaše UTXO na účtu **postmix**, čekajíc na jejich budoucí použití. Je dokonce doporučeno nechat je remixovat nekonečně, dokud je nepotřebujete utratit.

Někteří uživatelé by mohli zvážit převod svých smíchaných bitcoinů do peněženky zabezpečené hardware peněženkou. To je možné, ale je důležité přesně dodržovat doporučení Samourai Wallet, aby nedošlo ke kompromitaci získané důvěrnosti.

Slučování UTXO je nejčastější chybou. Je nutné vyhnout se kombinování smíchaných UTXO s nesmíchanými UTXO ve stejné transakci, aby se předešlo CIOH (*Common-Input-Ownership-Heuristic*). To vyžaduje pečlivé řízení vašich UTXO ve vaší peněžence, zejména z hlediska označování. Mimo coinjoin je slučování UTXO obecně špatnou praxí, která často vede ke ztrátě soukromí, pokud není správně řízena.

Je také důležité být opatrný při konsolidaci smíchaných UTXO mezi sebou. Mírné konsolidace jsou představitelné, pokud vaše smíchané UTXO mají významné anonsety, ale toto nevyhnutelně sníží důvěrnost vašich mincí. Ujistěte se, že konsolidace nejsou příliš velké ani provedené po nedostatečném počtu remixů, protože toto riziko vytváří odvoditelné vazby mezi vašimi UTXO před a po cyklech coinjoin. V případě pochybností o těchto manipulacích je nejlepší praxí nekonsolidovat postmix UTXO a převádět je jeden po druhém do vaší hardware peněženky, přičemž pokaždé generujete novou prázdnou adresu. Opět nezapomeňte správně označit každé přijaté UTXO.
Doporučuje se také nepřevádět vaše postmix UTXO do peněženky používající neobvyklé skripty. Například, pokud vstoupíte do Whirlpoolu z multisig peněženky používající skripty `P2WSH`, je málo pravděpodobné, že budete smícháni s ostatními uživateli, kteří mají původně stejný typ peněženky. Pokud své postmix vyberete do této stejné multisig peněženky, úroveň soukromí vašich smíchaných bitcoinů bude výrazně snížena. Kromě skriptů existuje mnoho dalších otisků peněženek, které vás mohou zmást.
Stejně jako u jakékoli bitcoinové transakce je také důležité neopakovat používání přijímacích adres. Každá nová transakce by měla být přijata na novou, prázdnou adresu.
Nejjednodušším a nejbezpečnějším řešením je nechat vaše smíšené UTXO odpočívat na jejich **postmix** účtu, nechat je remixovat a dotýkat se jich pouze při utrácení. Peněženky Samourai a Sparrow mají další ochrany proti všem těmto rizikům spojeným s analýzou blockchainu. Tyto ochrany vám pomáhají vyhnout se chybám.
## Jak spravovat doxxic změnu?
Dále je třeba být opatrný při správě doxxic změny, změny, která nemohla vstoupit do poolu coinjoin. Tyto toxické UTXO, vzniklé použitím Whirlpool, představují riziko pro vaše soukromí, protože vytvářejí spojení mezi vámi a použitím coinjoin. Proto je nezbytné s nimi zacházet opatrně a nespojovat je s ostatními UTXO, zejména smíšenými UTXO. Zde jsou různé strategie, které je třeba zvážit při jejich použití:
- **Smíchejte je v menších poolech:** Pokud je vaše toxické UTXO dostatečně velké, aby samo vstoupilo do menšího poolu, zvažte jeho smíchání. To je často nejlepší možnost. Je však zásadní nesloučit několik toxických UTXO pro přístup k poolu, protože by to mohlo spojit vaše různé vstupy;
- **Označte je jako "nepoužitelné":** Dalším přístupem je již je nepoužívat, označit je jako "nepoužitelné" na jejich dedikovaném účtu a prostě Hodlovat. To zajistí, že je omylem neutratíte. Pokud hodnota bitcoinu vzroste, mohou se objevit nové pooly vhodnější pro vaše toxické UTXO;
- **Dělejte dary:** Zvažte možnost dělat dary, i skromné, vývojářům pracujícím na Bitcoinu a jeho přidruženém softwaru. Můžete také darovat organizacím, které přijímají BTC. Pokud se vám zdá správa vašich toxických UTXO příliš složitá, jednoduše se jich můžete zbavit tím, že uděláte dar;
- **Kupujte dárkové karty:** Platformy jako [Bitrefill](https://www.bitrefill.com/) vám umožňují vyměnit bitcoiny za dárkové karty, které lze použít u různých obchodníků. To může být způsob, jak se zbavit vašich toxických UTXO bez ztráty přidružené hodnoty.
- **Konsolidujte je na Monero:** Peněženka Samourai nyní nabízí službu atomické výměny mezi BTC a XMR. To je ideální pro správu toxických UTXO tím, že je konsolidujete na Monero, aniž byste ohrozili své soukromí prostřednictvím CIOH, než je pošlete zpět na Bitcoin. Tato možnost však může být nákladná z hlediska poplatků za těžbu a prémie kvůli omezením likvidity.
- **Pošlete je do Lightning Network:** Převod těchto UTXO do Lightning Network za účelem využití snížených transakčních poplatků je možnost, která by mohla být zajímavá. Tato metoda však může odhalit určité informace v závislosti na vašem používání Lightning a měla by se proto praktikovat s opatrností.

Podrobné tutoriály k implementaci těchto různých technik budou brzy nabízeny na PlanB Network.

**Další zdroje:**
[Video tutoriál Sparrow Wallet](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607)
[Video tutoriál Samourai Wallet](https://planb.network/tutorials/wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956)
- [Dokumentace Samourai Wallet - Whirlpool](https://docs.samourai.io/whirlpool/basic-concepts);
- [Twitter vlákno o CoinJoins](https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [Blogový příspěvek o CoinJoins](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin).