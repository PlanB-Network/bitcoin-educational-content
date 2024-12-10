---
name: Coinjoin - Dojo
description: Jak provést coinjoin se svým vlastním Dojo?
---
![cover](assets/cover.webp)

***VAROVÁNÍ:** Po zatčení zakladatelů peněženky Samourai a zabavení jejich serverů 24. dubna nástroj Whirlpool již nefunguje, a to ani pro jednotlivce, kteří mají vlastní Dojo nebo používají Sparrow Wallet. Stále však existuje možnost, že tento nástroj bude v nadcházejících týdnech znovu zaveden nebo spuštěn jiným způsobem. Navíc teoretická část tohoto článku zůstává relevantní pro pochopení principů a cílů coinjoinů obecně (nejen Whirlpool), stejně jako pro pochopení účinnosti modelu Whirlpool.*

_Sledujeme vývoj této kauzy i vývoj souvisejících nástrojů. Ujistěte se, že tento návod aktualizujeme, jakmile budou k dispozici nové informace._

_Tento návod je poskytován pouze pro vzdělávací a informační účely. Nepodporujeme ani nevyzýváme k používání těchto nástrojů pro kriminální účely. Je odpovědností každého uživatele dodržovat zákony ve své jurisdikci._

---

V tomto návodu se dozvíte, co je coinjoin a jak jej provést pomocí softwaru Samourai Wallet a implementace Whirlpool, využívající vaše vlastní Dojo. Podle mého názoru je tato metoda aktuálně nejlepší pro míchání vašich bitcoinů.

## Co je coinjoin na Bitcoinu?
**Coinjoin je technika, která narušuje sledovatelnost bitcoinů na blockchainu**. Spoléhá na spolupráci v transakci se specifickou strukturou stejného názvu: transakce coinjoin.

Coinjoiny zvyšují soukromí uživatelů Bitcoinu tím, že komplikují analýzu blockchainu pro vnější pozorovatele. Jejich struktura umožňuje sloučení více mincí od různých uživatelů do jediné transakce, čímž se zaměňují stopy a stává se obtížným určit vazby mezi vstupními a výstupními adresami.

Princip coinjoinu je založen na spolupráci: několik uživatelů, kteří si přejí smíchat své bitcoiny, vloží identické částky jako vstupy téže transakce. Tyto částky jsou poté redistribuovány jako výstupy stejné hodnoty každému uživateli. Na konci transakce se stává nemožným spojit konkrétní výstup s známým uživatelem na vstupu. Mezi vstupy a výstupy neexistuje přímá vazba, což narušuje spojení mezi uživateli a jejich UTXO, stejně jako historii každé mince.
![coinjoin](assets/notext/1.webp)

Příklad transakce coinjoin (ne ode mě): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

Pro provedení coinjoinu při zajištění, že každý uživatel má po celou dobu kontrolu nad svými prostředky, začíná proces sestavením transakce koordinátorem, který ji poté přenáší účastníkům. Každý uživatel poté transakci podepíše po ověření, že mu vyhovuje. Všechny shromážděné podpisy jsou nakonec integrovány do transakce. Pokud uživatel nebo koordinátor pokusí o přesměrování prostředků prostřednictvím úpravy výstupů transakce coinjoin, podpisy se stanou neplatnými, což povede k zamítnutí transakce uzly.

Existuje několik implementací coinjoinu, jako jsou Whirlpool, JoinMarket nebo Wabisabi, každá s cílem řídit koordinaci mezi účastníky a zvýšit efektivitu transakcí coinjoin.
V tomto tutoriálu se ponoříme do implementace **Whirlpool**, který považuji za nejefektivnější řešení pro provádění coinjoinů na Bitcoinu. Ačkoli je dostupný v několika peněženkách, v tomto tutoriálu se budeme výhradně věnovat jeho použití s mobilní aplikací Samourai Wallet, bez Dojo.
## Proč provádět coinjoiny na Bitcoinu?
Jedním z počátečních problémů jakéhokoli peer-to-peer platebního systému je dvojí utrácení: jak zabránit zlomyslným jedincům v opakovaném utrácení stejných peněžních jednotek bez nutnosti obracet se na centrální autoritu, která by rozhodovala?

Satoshi Nakamoto poskytl řešení tohoto dilematu prostřednictvím protokolu Bitcoin, peer-to-peer elektronického platebního systému, který funguje nezávisle na jakékoli centrální autoritě. Ve své bílé knize zdůrazňuje, že jediný způsob, jak certifikovat absenci dvojího utrácení, je zajistit viditelnost všech transakcí v rámci platebního systému.

Aby byl každý účastník informován o transakcích, musí být veřejně zveřejněny. Proto fungování Bitcoinu spočívá na transparentní a distribuované infrastruktuře, která umožňuje jakémukoli operátoru uzlu ověřit celost řetězců elektronických podpisů a historii každé mince, od jejího vytvoření těžařem.

Transparentní a distribuovaná povaha blockchainu Bitcoinu znamená, že jakýkoli uživatel sítě může sledovat a analyzovat transakce všech ostatních účastníků. V důsledku toho je anonymita na úrovni transakcí nemožná. Avšak anonymita je zachována na úrovni individuální identifikace. Na rozdíl od tradičního bankovního systému, kde je každý účet spojen s osobní identitou, na Bitcoinu jsou finanční prostředky spojeny s páry kryptografických klíčů, čímž uživatelům nabízejí formu pseudonymity za kryptografickými identifikátory.

Takto je důvěrnost na Bitcoinu ohrožena, když vnější pozorovatelé dokážou spojit konkrétní UTXO s identifikovanými uživateli. Jakmile je tato asociace navázána, stává se možné sledovat jejich transakce a analyzovat historii jejich bitcoinů. Coinjoin je přesně technika vyvinutá k přerušení sledovatelnosti UTXO, čímž nabízí určitou úroveň důvěrnosti uživatelům Bitcoinu na úrovni transakcí.

## Jak funguje Whirlpool?
Whirlpool se od ostatních metod coinjoin odlišuje použitím transakcí "_ZeroLink_", které zajišťují, že mezi všemi vstupy a výstupy technicky není možné vytvořit žádnou spojitost. Toto dokonalé míchání je dosaženo strukturou, kde každý účastník přispívá identickou částkou na vstupu (kromě těžebních poplatků), čímž generuje výstupy dokonale stejných částek.
Tento restriktivní přístup k vstupům dává transakcím coinjoin Whirlpool jedinečný rys: úplnou absenci deterministických spojení mezi vstupy a výstupy. Jinými slovy, každý výstup má stejnou pravděpodobnost, že bude přiřazen jakémukoli účastníku, ve srovnání se všemi ostatními výstupy v transakci.
Původně byl počet účastníků v každém coinjoinu Whirlpool omezen na 5, s 2 novými účastníky a 3 remixéry (tyto koncepty vysvětlíme dále). Nicméně, zvýšení poplatků za on-chain transakce pozorované v roce 2023 přimělo týmy Samourai k přehodnocení jejich modelu za účelem zlepšení soukromí při snižování nákladů. Takže s ohledem na tržní situaci poplatků a počet účastníků může koordinátor nyní organizovat coinjoiny zahrnující 6, 7 nebo 8 účastníků. Tyto rozšířené sezení jsou označovány jako "_Surge Cycles_". Je důležité poznamenat, že bez ohledu na nastavení jsou v coinjoinech Whirlpool vždy pouze 2 noví účastníci.

Takže transakce Whirlpool se vyznačují identickým počtem vstupů a výstupů, které mohou být:
- 5 vstupů a 5 výstupů;
![coinjoin](assets/notext/2.webp)
- 6 vstupů a 6 výstupů;
![coinjoin](assets/notext/3.webp)
- 7 vstupů a 7 výstupů;
![coinjoin](assets/notext/4.webp) - 8 vstupů a 8 výstupů.
![coinjoin](assets/notext/5.webp)
Model navržený Whirlpool se tedy zakládá na malých transakcích typu coinjoin. Na rozdíl od Wasabi a JoinMarket, kde robustnost anonymních setů závisí na objemu účastníků v jednom cyklu, Whirlpool sází na řetězení více malých cyklů.

V tomto modelu uživatel platí poplatky pouze při svém prvním vstupu do poolu, což jim umožňuje účastnit se mnoha remixů bez dalších poplatků. Noví účastníci pokrývají těžební poplatky za remixéry.

S každým dalším coinjoinem, ve kterém se mince účastní spolu se svými dřívějšími spoluhráči, se anonymní sety budou exponenciálně zvětšovat. Cílem je tedy využít těchto bezplatných remixů, které při každém výskytu přispívají k zvýšení hustoty anonymních setů spojených s každou smíchanou mincí.

Whirlpool byl navržen s ohledem na dvě důležité požadavky:
- Dostupnost implementace na mobilních zařízeních, vzhledem k tomu, že Samourai Wallet je primárně aplikace pro smartphone;
- Rychlost cyklů remixování pro podporu významného nárůstu anonymních setů.
Tyto imperativy vedly vývojáře Samourai Wallet při návrhu Whirlpool k omezení počtu účastníků na cyklus. Příliš málo účastníků by ohrozilo efektivitu coinjoinu, drasticky snížilo by se množství generovaných anonymních setů na cyklus, zatímco příliš mnoho účastníků by představovalo problémy s řízením na mobilních aplikacích a brzdilo by tok cyklů.
**Nakonec není nutné mít ve Whirlpoolu vysoký počet účastníků na coinjoin, protože anonymní sety jsou dosaženy akumulací několika cyklů coinjoinu.**

[-> Dozvědět se více o anonymních setech Whirlpool.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

### Pooly a poplatky za coinjoin
Aby tyto několik cyklů skutečně zvýšilo anonymní sety smíchaných mincí, musí být stanoven určitý rámec omezující použité množství UTXO. Whirlpool tedy definuje různé pooly.

Pool představuje skupinu uživatelů, kteří si přejí smíchat dohromady, a dohodnou se na množství UTXO, které se má použít k optimalizaci procesu coinjoin. Každý pool specifikuje pevnou částku pro UTXO, které se uživatel musí držet, aby se mohl zúčastnit. Takže pro provádění coinjoinů s Whirlpool musíte vybrat pool. Aktuálně dostupné pooly jsou následující:
- 0,5 bitcoinu;
- 0,05 bitcoinu;
- 0,01 bitcoinu;
- 0,001 bitcoinu (= 100 000 sats).

Připojením do poolu se vaše bitcoiny rozdělí tak, aby generovaly UTXO, které jsou dokonale homogenní s těmi od ostatních účastníků v poolu. Každý pool má maximální limit; takže pro částky přesahující tento limit budete nuceni buď provést dvě samostatné vstupy do stejného poolu, nebo přejít do jiného poolu s vyšší částkou:

| Pool (bitcoin) | Maximální částka na vstup (bitcoin) |
|----------------|------------------------------------|
| 0,5            | 35                                 |
| 0,05           | 3,5                                |
| 0,01           | 0,7                                |
| 0,001          | 0,025                              |
Jak bylo zmíněno dříve, UTXO se považuje za součást poolu, když je připraveno být začleněno do coinjoin. To ovšem neznamená, že uživatel o něj přichází. **Prostřednictvím různých cyklů míchání si uchováváte plnou kontrolu nad svými klíči a tedy i nad svými bitcoiny.** To je to, co odlišuje techniku coinjoin od jiných centralizovaných technik míchání.

Pro vstup do poolu coinjoin je nutné zaplatit servisní poplatky a také poplatky za těžbu. Servisní poplatky jsou pro každý pool pevně stanoveny a mají za úkol kompenzovat týmy odpovědné za vývoj a údržbu Whirlpool.

Servisní poplatky za použití Whirlpool se platí pouze jednou při vstupu do poolu. Po tomto kroku máte možnost účastnit se neomezeného počtu remixů bez jakýchkoli dalších poplatků. Zde jsou aktuální pevné poplatky pro každý pool:

| Pool (bitcoin) | Vstupní poplatek (bitcoin) |
|----------------|----------------------------|
| 0.5            | 0.0175                     |
| 0.05           | 0.00175                    |
| 0.01           | 0.0005 (50,000 sats)       |
| 0.001          | 0.00005 (5,000 sats)       |


Tyto poplatky v podstatě fungují jako vstupenka do vybraného poolu, bez ohledu na částku, kterou do coinjoin vložíte. Takže ať už vstoupíte do poolu 0.01 s přesně 0.01 BTC nebo do něj vstoupíte s 0.5 BTC, poplatky zůstanou stejné v absolutní hodnotě.

Před přistoupením k coinjoin má uživatel tedy na výběr ze 2 strategií:
- Zvolit menší pool, aby minimalizoval servisní poplatky, s vědomím, že obdrží několik malých UTXO;
- Nebo dát přednost většímu poolu, souhlasit s vyššími poplatky za to, že získá menší počet UTXO s vyšší hodnotou.

Obecně se nedoporučuje slučování několika smíchaných UTXO po cyklech coinjoin, protože by to mohlo ohrozit získanou důvěrnost, zejména kvůli heuristice společného vlastnictví vstupů (CIOH). Proto může být rozumné zvolit větší pool, i když to znamená platit více, aby se předešlo mít příliš mnoho UTXO s malou hodnotou na výstupu. Uživatel musí tyto kompromisy zvážit, aby si vybral pool, který preferuje.

Kromě servisních poplatků je také nutné zvážit poplatky za těžbu, které jsou nezbytné pro jakoukoli transakci s Bitcoinem. Jako uživatel Whirlpool budete muset zaplatit poplatky za těžbu pro přípravnou transakci (`Tx0`) stejně jako ty pro první coinjoin. Všechny následující remixy budou zdarma, díky modelu Whirlpool, který se opírá o platby nových účastníků.

Ve skutečnosti, v každém coinjoinu Whirlpool jsou dva uživatelé mezi vstupy noví účastníci. Ostatní vstupy pocházejí od remixérů. V důsledku toho jsou poplatky za těžbu pro všechny účastníky transakce pokryty těmito dvěma novými účastníky, kteří poté také těží z bezplatných remixů:
![coinjoin](assets/en/6.webp)
Díky tomuto systému poplatků se Whirlpool skutečně odlišuje od ostatních služeb coinjoin, protože anonsety UTXO nejsou proporcionální k ceně zaplacené uživatelem. Takto je možné dosáhnout výrazně vysokých úrovní anonymity pouze zaplacením vstupního poplatku do poolu a poplatků za těžbu pro dvě transakce (pro `Tx0` a počáteční míchání).
Je důležité poznamenat, že uživatel bude muset také pokrýt těžební poplatky za vybrání svých UTXO z fondu po dokončení jejich několika coinjoinů, pokud si nevybral možnost `mix to`, o které si povíme v následujícím tutoriálu.

### Účty HD peněženky používané Whirlpoolem
Pro provedení coinjoinu prostřednictvím Whirlpoolu musí peněženka generovat několik odlišných účtů. Účet, v kontextu HD (*Hierarchical Deterministic*) peněženky, představuje sekci zcela izolovanou od ostatních, přičemž tato separace nastává na třetí úrovni hloubky hierarchie peněženky, tedy na úrovni `xpub`.

HD peněženka může teoreticky odvodit až `2^(32/2)` různých účtů. Počáteční účet, používaný ve výchozím nastavení ve všech Bitcoin peněženkách, odpovídá indexu `0'`.

Pro peněženky přizpůsobené Whirlpoolu, jako jsou Samourai nebo Sparrow, se používají 4 účty, aby vyhověly potřebám procesu coinjoin:
- Účet **deposit** (vklad), identifikovaný indexem `0'`;
- Účet **bad bank** (nebo doxxic change), identifikovaný indexem `2 147 483 644'`;
- Účet **premix**, identifikovaný indexem `2 147 483 645'`;
- Účet **postmix**, identifikovaný indexem `2 147 483 646'`.

Každý z těchto účtů plní specifickou funkci v rámci coinjoinu.

Všechny tyto účty jsou spojeny s jedním seedem, což umožňuje uživateli obnovit přístup ke všem svým bitcoinům pomocí své obnovovací fráze a v případě potřeby také svého hesla. Je však nutné během této obnovovací operace softwaru specifikovat různé indexy účtů, které byly použity.

Podívejme se nyní na různé fáze coinjoinu Whirlpool v rámci těchto účtů.

### Různé fáze coinjoinů na Whirlpoolu
**Fáze 1: Tx0**
Výchozím bodem jakéhokoli coinjoinu Whirlpool je účet **deposit** (vklad). Tento účet automaticky používáte, když vytvoříte novou Bitcoin peněženku. Na tento účet musí být připsány bitcoiny, které si přejete smíchat.
`Tx0` představuje první krok v procesu míchání Whirlpool. Jeho cílem je připravit a vyrovnat UTXO pro coinjoin, rozdělením na jednotky odpovídající částce vybraného fondu, aby se zajistila homogenita míchání. Vyrovnané UTXO jsou poté odeslány na účet **premix**. Pokud jde o rozdíl, který nemůže vstoupit do fondu, je oddělen do specifického účtu: **bad bank** (nebo "doxxic change").
Tato počáteční transakce `Tx0` slouží také k úhradě servisních poplatků koordinátoru míchání. Na rozdíl od následujících kroků, tato transakce není kolaborativní; uživatel musí tedy nést všechny těžební poplatky:
![coinjoin](assets/en/7.webp)

V tomto příkladu transakce `Tx0` je vstup `372,000 sats` z našeho účtu **deposit** rozdělen na několik výstupních UTXO, které jsou distribuovány následovně:
- Částka `5,000 sats` určená koordinátorovi za servisní poplatky, odpovídající vstupu do fondu `100,000 sats`;
- Tři UTXO připravené pro míchání, přesměrované na náš účet **premix** a zaregistrované u koordinátora. Tyto UTXO jsou vyrovnány na `108,000 sats` každý, aby pokryly těžební poplatky za jejich budoucí počáteční mix;
- Přebytek, který nemůže vstoupit do poolu, protože je příliš malý, je považován za toxickou změnu. Je poslán na jeho specifický účet. Zde tato změna činí `40,000 sats`;
- Nakonec existují `3,000 sats`, které netvoří výstup, ale jsou to těžební poplatky nutné k potvrzení `Tx0`.

Například zde je skutečná Whirlpool Tx0 (ne ode mě): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

**Krok 2: Toxická změna**
Přebytek, který nemohl být začleněn do poolu, zde ekvivalentní `40,000 sats`, je přesměrován na účet **špatné banky**, také označovaný jako "toxická změna", aby se zajistilo striktní oddělení od ostatních UTXO v peněžence.

Toto UTXO je nebezpečné pro soukromí uživatele, protože nejenže je stále připojeno ke své minulosti, a tedy možná k identitě jeho majitele, ale navíc je označeno jako patřící uživateli, který provedl coinjoin.
Pokud je toto UTXO sloučeno s míchanými výstupy, ztratí veškeré získané soukromí během cyklů coinjoin, zejména kvůli heuristice společného vlastnictví vstupů (CIOH). Pokud je sloučeno s dalšími toxickými změnami, uživatel riskuje ztrátu soukromí, protože to spojí různé vstupy cyklů coinjoin. Proto je nutné s ním zacházet opatrně. Způsob, jakým se má tato toxická UTXO spravovat, bude podrobně popsán v poslední části tohoto článku a budoucí tutoriály na PlanB Network tyto metody podrobněji pokryjí.

**Krok 3: Počáteční míchání**
Po dokončení `Tx0` jsou vyrovnávaná UTXO poslána na **premix** účet naší peněženky, připravena být začleněna do jejich prvního cyklu coinjoin, také nazývaného "počáteční míchání". Pokud, jak je tomu v našem příkladu, `Tx0` generuje několik UTXO určených pro míchání, každé z nich bude začleněno do samostatného počátečního coinjoinu.

Na konci těchto prvních míchání bude **premix** účet prázdný, zatímco naše mince, které zaplatily těžební poplatky za tento první coinjoin, budou přesně upraveny na částku definovanou vybraným poolem. V našem příkladu budou naše počáteční UTXO `108 000 sats` snížena přesně na `100 000 sats`.
![coinjoin](assets/en/8.webp)
**Krok 4: Remixy**
Po počátečním míchání jsou UTXO převedeny na **postmix** účet. Tento účet shromažďuje již smíchaná UTXO a ta, která čekají na remixování. Když je klient Whirlpool aktivní, UTXO umístěná na **postmix** účtu jsou automaticky k dispozici pro remixování a budou náhodně vybrána k účasti na těchto nových cyklech.

Připomeňme si, že remixy jsou poté 100% zdarma: nejsou vyžadovány žádné další poplatky za službu ani těžební poplatky. Udržení UTXO na **postmix** účtu tak udržuje jejich hodnotu nezměněnou a současně zlepšuje jejich anonsety. Proto je důležité umožnit těmto mincím účastnit se více cyklů coinjoin. Nestojí vás to absolutně nic a zvyšuje jejich úroveň anonymity.
Když se rozhodnete utratit smíšené UTXO, můžete tak učinit přímo z tohoto **postmix** účtu. Je doporučeno uchovávat smíšené UTXO na tomto účtu, abyste mohli využívat bezplatných remixů a vyhnout se jejich odchodu z oběhu Whirlpool, což by mohlo snížit jejich důvěrnost.
Jak uvidíme v následujícím tutoriálu, existuje také možnost `mix to`, která nabízí možnost automaticky poslat vaše smíšené mince do jiné peněženky, například do studené peněženky, po definovaném počtu coinjoinů.
Po probrání teorie se ponořme do praxe s tutoriálem na používání Whirlpool prostřednictvím aplikace Samourai Wallet pro Android, synchronizované s Whirlpool CLI a GUI ve vašem vlastním Dojo!
## Tutoriál: Coinjoin Whirlpool s vaším vlastním Dojo
Existuje mnoho možností, jak používat Whirlpool. Možnost, kterou zde chci představit, je použití aplikace Samourai Wallet, open-source správce Bitcoin peněženek pro Android, ale tentokrát **s vaším vlastním Dojo**.

Provádění coinjoinů prostřednictvím aplikace Samourai Wallet s vaším vlastním Dojo je podle mého názoru nejefektivnější strategie pro provádění coinjoinů na Bitcoinu doposud. Tento přístup vyžaduje určitou počáteční investici z hlediska nastavení, ale jakmile je vše na místě, nabízí možnost neustále míchat a remixovat vaše bitcoiny, 24 hodin denně, 7 dní v týdnu, bez nutnosti neustále aktivní aplikace Samourai. Díky Whirlpool CLI, který funguje na Bitcoinovém uzlu, jste vždy připraveni účastnit se coinjoinů. Aplikace Samourai vám poté dává možnost kdykoliv utratit vaše smíšené prostředky, kdekoliv jste, přímo z vašeho smartphonu. Navíc má tato metoda tu výhodu, že vás nikdy nepřipojí k serverům spravovaným týmy Samourai, čímž chrání váš `xpub` před jakoukoliv vnější expozicí.

Tato technika je tedy ideální pro ty, kteří hledají maximální soukromí a nejvyšší kvalitu cyklů coinjoin. Vyžaduje však mít k dispozici Bitcoinový uzel a, jak uvidíme později, vyžaduje určité nastavení. Je tedy více vhodná pro uživatele se středními až pokročilými znalostmi. Pro začátečníky doporučuji seznámit se s coinjoin prostřednictvím těchto dvou dalších tutoriálů, které ukazují, jak na to s Sparrow Wallet nebo Samourai Wallet (bez Dojo):
- **[Tutoriál coinjoin pro Sparrow Wallet](https://planb.network/en/tutorials/privacy/coinjoin-sparrow-wallet)**;
- **[Tutoriál coinjoin pro Samourai Wallet (bez Dojo)](https://planb.network/en/tutorials/privacy/coinjoin-samourai-wallet)**.

### Porozumění nastavení
Na začátek budete potřebovat Dojo! Dojo je implementace Bitcoinového uzlu založená na Bitcoin Core, vyvinutá týmy Samourai.

Pro spuštění vašeho vlastního Dojo máte možnost buď nainstalovat uzel Dojo autonomně, nebo využít Dojo na vrcholu jiného řešení Bitcoinového uzlu "node-in-box". Aktuálně jsou k dispozici tyto možnosti:
- [RoninDojo](https://ronindojo.io/), který je Dojo vylepšený o další nástroje, včetně asistenta pro instalaci a asistenta pro správu. Postup nastavení a používání RoninDojo detailně popisuji v tomto dalším tutoriálu: [RONINDOJO V2](https://planb.network/en/tutorials/node/ronin-dojo-v2);
- [Umbrel](https://umbrel.com/) s aplikací "Samourai Server";
- [MyNode](https://mynodebtc.com/) s aplikací "Dojo";
- [Nodl](https://www.nodl.eu/) s aplikací "Dojo";- [Citadel](https://runcitadel.space/) s aplikací "Samourai".
![coinjoin](assets/notext/9.webp)
V našem nastavení budeme interagovat se třemi rozdílnými rozhraními:
- **Samourai Wallet**, která bude hostit naši Bitcoin peněženku určenou pro coinjoins. Dostupná zdarma na Androidu, tato FOSS aplikace vám umožní kontrolovat vaši mixovací peněženku, zejména pro utrácení vašich postmixů z vašeho smartphonu;
- **Whirlpool CLI** (_Command Line Interface_), který bude fungovat na uzlu hostujícím Dojo. Tento software bude mít přístup k klíčům vaší Samourai peněženky. Je zodpovědný za komunikaci s koordinátorem a správu coinjoins nepřetržitě. Funguje jako kopie vaší Samourai peněženky na vašem uzlu, připravená kdykoliv se zapojit do coinjoins;
- **Whirlpool GUI** (_Graphical User Interface_), grafické uživatelské rozhraní, které budeme používat k monitorování aktivity Whirlpool CLI a iniciaci míchání na dálku. Whirlpool GUI poskytuje vizuální reprezentaci operací prováděných Whirlpool CLI. Tento software musí být nainstalován na počítači odděleném od Dojo. Pro uživatele Umbrel, MyNode, Nodl a Citadel je Whirlpool GUI povinné. Nicméně, s RoninDojo je rozhraní Whirlpool GUI již integrováno do webového rozhraní vašeho uzlu prostřednictvím aplikace `Whirlpool`. Proto jej nebudete potřebovat instalovat na samostatný PC.

Podle mého názoru představuje použití RoninDojo nejlepší řešení pro provádění coinjoins s Dojo. Jelikož je tento software uzlu v krabici v přímém partnerství s týmy Samourai, RoninDojo je pro toto mnohem více optimalizován. Navíc integrace Whirlpool GUI do webového rozhraní výrazně zjednodušuje proces nastavení. V tomto tutoriálu vám přesto vysvětlím, jak to udělat s ostatními řešeními, která integrují Dojo (Umbrel, Nodl, MyNode a Citadel).

### Příprava vašeho Dojo
Začněte tím, že nainstalujete Dojo a získáte QR kód nebo odkaz, který vám umožní k němu připojit se na dálku. Tento odkaz je Tor adresa končící na `.onion`. Pokud používáte RoninDojo, jednoduše přejděte do menu `Pairing` pro přístup k těmto informacím.
![coinjoin](assets/notext/10.webp)

Pod `Samourai Dojo` klikněte na tlačítko `Pair now`.

![coinjoin](assets/notext/11.webp)

Zobrazí se váš QR kód pro připojení a odpovídající odkaz.

![coinjoin](assets/notext/12.webp)

Pokud jste na Umbrel, přejděte do App Store a vyhledejte aplikaci `Samourai Server`. Nachází se v záložce `Bitcoin`.

![coinjoin](assets/notext/13.webp)

Nainstalujte aplikaci.

![coinjoin](assets/notext/14.webp)

Po otevření aplikace pak budete mít přístup k QR kódu pro připojení k vašemu Dojo.

![coinjoin](assets/notext/15.webp)

Pokud používáte jiný software uzlu v krabici, jako je MyNode, Citadel nebo Nodl, proces je podobný jako u Umbrel. Musíte nainstalovat aplikaci Samourai nebo Dojo, abyste získali potřebné informace pro připojení k vašemu Dojo.

![coinjoin](assets/notext/16.webp)

### Příprava vaší Samourai peněženky
Po získání informací o připojení k vašemu Dojo je nyní čas nastavit vaši peněženku pro coinjoins. Existují dva scénáře: pokud ještě nemáte na svém smartphonu peněženku Samourai, proces je jednoduchý, stačí vytvořit novou.
Na druhé straně, pokud už peněženku Samourai máte, bude nutné aplikaci přeinstalovat, aby byla asociována s novým Dojo. Tento krok je nutný, protože připojení k Dojo lze navázat pouze při prvním spuštění aplikace. Díky automaticky generovanému šifrovanému záložnímu souboru od Samourai na vašem telefonu je tento postup jednoduchý a rychlý.

*Pokud jste Samourai nikdy nepoužívali, můžete tyto předběžné kroky přeskočit a přejít přímo k instalaci aplikace.*

Především se ujistěte, že vaše aplikace Samourai Wallet je aktualizovaná. K tomu zkontrolujte Google Play Store nebo porovnejte verzi vaší aplikace v `Nastavení > Další` s tou dostupnou na webu Samourai.

![coinjoin](assets/notext/17.webp)

Ujistěte se, že máte svou obnovovací frázi peněženky Samourai a že je čitelná. Poté proveďte test vaší BIP39 fráze navigací do `Nastavení > Řešení problémů > Test fráze/zálohy` a potvrďte její přesnost.

![coinjoin](assets/notext/18.webp)
Zadejte svou frázi, poté ověřte, že Samourai potvrdí její platnost.
![coinjoin](assets/notext/19.webp)

Pokud je vaše fráze neplatná, nebo pokud nemáte svou obnovovací frázi, je nezbytné okamžitě proceduru zastavit! **Riskujete ztrátu vašich bitcoinů během této operace.** V tomto případě se doporučuje převést vaše prostředky do jiné peněženky a začít s novou prázdnou peněženkou Samourai. Následující kroky by měly být provedeny pouze pokud jste si jisti, že máte veškeré potřebné záložní informace a že vaše fráze je platná.

Poté pokračujte vytvořením šifrované zálohy vaší peněženky a zkopírujte ji do schránky. K provedení této operace klikněte na tři malé tečky umístěné v pravém horním rohu obrazovky, poté vyberte `Exportovat zálohu peněženky`.

![coinjoin](assets/notext/20.webp)

**Od tohoto kroku nic dalšího do schránky nekopírujte!** Je naprosto nezbytné, abyste si uchovávali vaši zkopírovanou zálohu.

Pokud jste předchozí kroky provedli správně, nyní můžete bezpečně odstranit vaši peněženku Samourai. K tomu přejděte do: `Nastavení > Peněženka > Bezpečně vymazat peněženku`.

![coinjoin](assets/notext/21.webp)

![coinjoin](assets/notext/22.webp)

*Pokud jste Samourai nikdy nepoužívali a instalujete aplikaci od začátku, můžete pokračovat v tutoriálu od tohoto kroku.*

Vaše aplikace Samourai je nyní resetována. Otevřete aplikaci a pokračujte v krocích nastavení, jako byste ji používali poprvé.

![coinjoin](assets/notext/23.webp)

V dalším kroku získáte přístup na stránku určenou pro konfiguraci vašeho Dojo. Vyberte možnost `Dojo`, poté zadejte přihlašovací údaje vašeho Dojo. K tomu máte možnost skenovat informace stisknutím `Skenovat QR`.

![coinjoin](assets/notext/24.webp)

*Pro nové uživatele Samourai bude poté nutné vytvořit peněženku od začátku. Pokud potřebujete pomoc, můžete se poradit s návodem na nastavení nové peněženky Samourai [v tomto tutoriálu, konkrétně v sekci "Vytvoření softwarové peněženky"](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef)*
Pokud pokračujete v obnově již existující peněženky Samourai, vyberte `Restore existing wallet`, poté zvolte `I have a Samourai backup file`.
![coinjoin](assets/notext/25.webp)
Obvykle byste měli mít svůj soubor pro obnovu vždy ve schránce. Poté klikněte na `PASTE` pro vložení vašeho souboru do určeného místa. Pro jeho dešifrování bude také nutné zadat BIP39 heslovou frázi vaší peněženky do příslušného pole, které se nachází hned pod ním. Pro dokončení klikněte na `FINISH`.
![coinjoin](assets/notext/26.webp)

Poté budete přesměrováni do vaší peněženky Samourai, která bude tentokrát připojena k vašemu vlastnímu Dojo.

![coinjoin](assets/notext/27.webp)

### Instalace Whirlpool GUI
Nyní je čas na instalaci Whirlpool GUI, grafického uživatelského rozhraní, které vám umožní spravovat vaše cykly coinjoin z vašeho běžného PC. Pro uživatele RoninDojo tento krok není nutný, protože správa coinjoinů může být provedena přímo prostřednictvím webového rozhraní v `Apps > Whirlpool`. Pokud však používáte jiné řešení Bitcoin "node-in-box", je nezbytné s touto instalací pokračovat.
![coinjoin](assets/notext/28.webp)
Přejděte na svůj osobní počítač a stáhněte software Whirlpool z oficiálních stránek peněženky Samourai, vyberte verzi, která odpovídá vašemu operačnímu systému.

![coinjoin](assets/notext/29.webp)

Před spuštěním Whirlpool GUI je nutné na vašem stroji nainstalovat JAVA 8 nebo vyšší verzi. Pro toto můžete nainstalovat OpenJDK [zde](https://adoptium.net/).
![coinjoin](assets/notext/30.webp)
Je také nutné mít v pozadí na vašem počítači funkční Tor Daemon nebo Tor Browser. Před každou použitím Whirlpool GUI se ujistěte, že Tor je spuštěn. Pokud Tor ještě není na vašem stroji nainstalován, [můžete si jej stáhnout a nainstalovat z oficiálního webu projektu](https://www.torproject.org/download/), poté se ujistěte, že jej spustíte na pozadí.

![coinjoin](assets/notext/31.webp)

Jakmile je JDK nainstalováno na vašem systému a Tor je spuštěn na pozadí, můžete spustit Whirlpool GUI.

![coinjoin](assets/notext/32.webp)

Ve Whirlpool GUI klikněte na `Advanced: Remote CLI` pro připojení vašeho Whirlpool CLI, který je na vašem Dojo. Budete potřebovat Tor adresu vašeho Whirlpool CLI.

![coinjoin](assets/notext/33.webp)

Pro lokalizaci vaší Tor adresy na Umbrel a dalších řešeních "node-in-box" jednoduše spusťte aplikaci Samourai Server nebo Dojo (název se může lišit v závislosti na použitém softwaru). Tor adresa bude přímo viditelná na stránce aplikace.
![coinjoin](assets/notext/34.webp)
Ve Whirlpool GUI zadejte Tor adresu, kterou jste dříve získali, do pole `CLI address`. Ponechte prefix `http://`, ale na konec nepřidávejte port `:8899`. Vložte pouze adresu tak, jak vám byla poskytnuta.
![coinjoin](assets/notext/35.webp)
V poli Tor Proxy zadejte `socks5://127.0.0.1:9050`, pokud používáte Tor Daemon, nebo `socks5://127.0.0.1:9150`, pokud jde o Tor Browser. Když se poprvé připojujete k Whirlpool CLI prostřednictvím Whirlpool GUI, je možné nechat pole pro API klíč prázdné. Pokud se nepřipojujete poprvé, prosím, vložte váš API klíč do příslušného pole. Tento klíč najdete na stejné stránce jako vaše Tor adresa.
![coinjoin](assets/notext/36.webp)

Jakmile vyplníte vše potřebné, klikněte na tlačítko `Connect`. Prosím čekejte, připojení může trvat několik minut.

![coinjoin](assets/notext/37.webp)

### Spárování vaší peněženky Samourai s Whirlpool GUI
*Uživatelé RoninDojo mohou pokračovat v tutoriálu zde.*

Nyní spárujeme dříve nakonfigurovanou peněženku Samourai s softwarem Whirlpool GUI, nebo přímo s RoninDojo pro ty, kteří používají tento software. Ať už používáte Whirlpool GUI nebo RoninDojo, budete požádáni o vložení nebo naskenování spárovacích informací vaší peněženky Samourai.

![coinjoin](assets/notext/38.webp)

Tyto informace najdete v nastavení vaší peněženky.

![coinjoin](assets/notext/39.webp)

Klikněte na `Transakce`, poté na `Spárovat s Whirlpool GUI`.

![coinjoin](assets/notext/40.webp)

Samourai vám poté poskytne potřebné informace pro navázání spojení. Buďte opatrní, tato data jsou citlivá! Můžete je přenést na váš PC buď přímým kopírováním, nebo naskenováním zobrazeného QR kódu pomocí webové kamery vašeho počítače po kliknutí na symbol QR kódu.

![coinjoin](assets/notext/41.webp)

Po provedení této operace ve Whirlpool GUI vyberte `Initialize GUI`. Prosím čekejte, tento krok může chvíli trvat.

![coinjoin](assets/notext/42.webp)

Ať už používáte Whirlpool GUI nebo RoninDojo, budete požádáni o zadání heslové fráze vaší peněženky Samourai. Vložte ji do příslušného pole, poté stiskněte tlačítko `Login` a pokračujte.

![coinjoin](assets/notext/43.webp)

Poté se dostanete na domovskou stránku Whirlpool CLI

![coinjoin](assets/notext/44.webp)

### Iniciace coinjoinů z Whirlpool GUI
*Pro uživatele RoninDojo je postup stejný. Aplikace Whirlpool integrovaná do RoninDojo nabízí stejné možnosti a funkce jako software Whirlpool GUI na desktopu. Proto můžete postupovat podle těchto pokynů stejným způsobem.*
Nyní, když je vše nastaveno, jste připraveni začít míchat vaše bitcoiny. K tomu přeneste bitcoiny, které chcete míchat, na účet **Deposit** vaší peněženky Samourai. Tuto operaci můžete provést buď přímo prostřednictvím aplikace Samourai Wallet nebo na Whirlpool GUI. Na hlavní stránce klikněte na tlačítko `+ Deposit` umístěné v levém horním rohu.

![coinjoin](assets/notext/45.webp)
Whirlpool GUI vygeneruje přijímací adresu. Zobrazí také minimální částku potřebnou k účasti v každém coinjoin poolu. Tato částka se liší v závislosti na trhu s poplatky. Doporučuje se vložit částku mírně vyšší než je minimálně požadovaná, protože pokud těžební poplatky neklesnou, váš UTXO nemusí být přijat do požadovaného poolu. Proto pošlete své bitcoiny na uvedenou adresu. Pro získání nové adresy jednoduše klikněte na tlačítko `Obnovit adresu`.
![coinjoin](assets/notext/46.webp)

Jakmile je vklad potvrzen, uvidíte ho na Whirlpool GUI v účtu **Vklad**.

![coinjoin](assets/notext/47.webp)

Pro zahájení cyklů coinjoin vyberte UTXO, které chcete míchat, a stiskněte tlačítko `Předmixovat`. Buďte opatrní: pokud vyberete několik různých UTXO současně, budou během přípravné transakce `TX0` sloučeny. Toto sloučení může vést k snížení soukromí, zejména pokud UTXO pocházejí z různých zdrojů, kvůli heuristice společného vlastnictví vstupů (CIOH).

![coinjoin](assets/notext/48.webp)

Otevře se stránka konfigurace Whirlpool. Můžete si vybrat pool, do kterého chcete vstoupit. Vyberte také těžební poplatky určené pro `TX0` a první coinjoins. Na spodní části této stránky vám souhrn představí částku doxxic change i částku a počet UTXO, které budou vyrovnány a zahrnuty do cyklů coinjoin. Pokud jste s touto konfigurací spokojeni, stiskněte tlačítko `Předmixovat` pro zahájení cyklů coinjoin.
![coinjoin](assets/notext/49.webp)

Jakmile je `TX0` vytvořeno, uvidíte svá vyrovnána UTXO v účtu **Předmix**, čekající na potvrzení. Aby vaše mince mohly být automaticky míchány 24 hodin denně, 7 dní v týdnu, doporučuji aktivovat možnost `Automaticky míchat předmix & postmix`. Tuto funkci najdete na kartě `Konfigurace`, umístěné vlevo od okna Whirlpool GUI.
![coinjoin](assets/notext/50.webp)
Po zahájení coinjoinů můžete Whirlpool GUI i Samourai Wallet zavřít. Pouze váš uzel musí zůstat připojen, aby mohl pokračovat v účasti na coinjoinech. Doporučuje se však pravidelně kontrolovat průběh vašich cyklů coinjoin. Pokud si všimnete, že vaše UTXO nejsou již nějakou dobu vybírána pro coinjoin, může to naznačovat chybu. V tom případě přejděte na Whirlpool CLI a vyberte `Start` pro restartování vaší dostupnosti pro coinjoins.

![coinjoin](assets/notext/51.webp)

Vaše smíchaná UTXO jsou viditelná z účtu **Postmix** na Whirlpool GUI. Kromě toho máte možnost je přímo zobrazit a utratit prostřednictvím rozhraní Whirlpool ve vaší Samourai Wallet. Pro přístup k tomuto menu klikněte na modré `+` ve spodní části obrazovky a poté vyberte `Whirlpool`.

![coinjoin](assets/notext/52.webp)

Účty Whirlpool jsou na Samourai Wallet snadno rozpoznatelné podle jejich modré barvy. To vám umožňuje utrácet vaše smíchaná UTXO odkudkoli a kdykoli přímo z vašeho smartphonu.

![coinjoin](assets/notext/53.webp)
Abychom sledovali vaše automatické coinjoins, doporučuji také nastavit sledovací (watch-only) peněženku prostřednictvím aplikace Sentinel. Přidejte ZPUB vašeho účtu **Postmix** a sledujte průběh vašich cyklů coinjoin v reálném čase. Pokud chcete pochopit, jak používat Sentinel, doporučuji se poradit s tímto dalším tutoriálem na PlanB Network: [**SENTINEL WATCH-ONLY**](https://planb.network/tutorials/wallet/mobile/sentinel-9876f960-e964-4d20-8a6e-36231de1f4d9)