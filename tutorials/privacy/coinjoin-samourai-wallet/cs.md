---
name: Coinjoin - Samourai Wallet
description: Jak provést coinjoin pomocí peněženky Samourai Wallet?
---
![cover](assets/cover.webp)

***VAROVÁNÍ:** Po zatčení zakladatelů Samourai Wallet a zabavení jejich serverů 24. dubna nástroj Whirlpool již nefunguje, a to ani pro jednotlivce, kteří mají vlastní Dojo nebo používají Sparrow Wallet. Stále však existuje možnost, že by tento nástroj mohl být v nadcházejících týdnech obnoven nebo spuštěn jiným způsobem. Navíc teoretická část tohoto článku zůstává relevantní pro pochopení principů a cílů coinjoinů obecně (nejen Whirlpool), stejně jako pro pochopení účinnosti modelu Whirlpool.*

_Pozorně sledujeme vývoj této kauzy i vývoj souvisejících nástrojů. Ujistěte se, že tento návod aktualizujeme, jakmile budou k dispozici nové informace._

_Tento návod je poskytován pouze pro vzdělávací a informační účely. Nepodporujeme ani nevyzýváme k používání těchto nástrojů pro kriminální účely. Je odpovědností každého uživatele dodržovat zákony ve své jurisdikci._

---

"*bitcoinová peněženka pro ulici*"

V tomto návodu se dozvíte, co je coinjoin a jak jej provést pomocí softwaru Samourai Wallet a implementace Whirlpool.

## Co je coinjoin na Bitcoinu?
**Coinjoin je technika, která narušuje sledovatelnost bitcoinů na blockchainu**. Spoléhá na kolaborativní transakci se specifickou strukturou stejného názvu: transakce coinjoin.

Coinjoiny zvyšují soukromí uživatelů Bitcoinu tím, že komplikují analýzu řetězce pro vnější pozorovatele. Jejich struktura umožňuje sloučení více mincí od různých uživatelů do jediné transakce, čímž se zaměňují stopy a stává se obtížným určit vazby mezi vstupními a výstupními adresami.

Princip coinjoinu je založen na kolaborativním přístupu: několik uživatelů, kteří si přejí smíchat své bitcoiny, vloží identické částky jako vstupy téže transakce. Tyto částky jsou poté redistribuovány jako výstupy stejné hodnoty každému uživateli. Na konci transakce se stává nemožným spojit konkrétní výstup s známým uživatelem na vstupu. Mezi vstupy a výstupy neexistuje přímá vazba, čímž se přerušuje spojení mezi uživateli a jejich UTXO, stejně jako historie každé mince.
![coinjoin](assets/notext/1.webp)

Příklad transakce coinjoin (ne ode mě): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

Pro provedení coinjoinu při zajištění, že každý uživatel má po celou dobu kontrolu nad svými prostředky, začíná proces sestavením transakce koordinátorem, který ji poté předá účastníkům. Každý uživatel poté transakci podepíše po ověření, že mu vyhovuje. Všechny shromážděné podpisy jsou nakonec integrovány do transakce. Pokud uživatel nebo koordinátor pokusí o přesměrování prostředků úpravou výstupů transakce coinjoin, podpisy se stanou neplatnými, což povede k zamítnutí transakce uzly.

Existuje několik implementací coinjoinu, jako jsou Whirlpool, JoinMarket nebo Wabisabi, každá s cílem řídit koordinaci mezi účastníky a zvýšit efektivitu transakcí coinjoin.
V tomto tutoriálu se ponoříme do implementace **Whirlpool**, který považuji za nejefektivnější řešení pro provádění coinjoinů na Bitcoinu. Ačkoli je dostupný v několika peněženkách, v tomto tutoriálu se budeme výhradně věnovat jeho použití s mobilní aplikací Samourai Wallet, bez Dojo.
## Proč provádět coinjoiny na Bitcoinu?
Jedním z počátečních problémů jakéhokoli peer-to-peer platebního systému je dvojí utrácení: jak zabránit zlým jedincům, aby utráceli stejné peněžní jednotky vícekrát, aniž by bylo nutné uchýlit se k centrální autoritě, která by rozhodovala?

Satoshi Nakamoto poskytl řešení tohoto dilematu prostřednictvím protokolu Bitcoin, peer-to-peer elektronického platebního systému, který funguje nezávisle na jakékoli centrální autoritě. Ve své bílé knize zdůrazňuje, že jediný způsob, jak certifikovat absenci dvojího utrácení, je zajistit viditelnost všech transakcí v rámci platebního systému.

Aby bylo zaručeno, že každý účastník je informován o transakcích, musí být veřejně zveřejněny. Proto provoz Bitcoinu spočívá na transparentní a distribuované infrastruktuře, která umožňuje jakémukoli operátoru uzlu ověřit celost řetězců elektronických podpisů a historii každé mince, od jejího vytvoření těžařem.

Transparentní a distribuovaná povaha blockchainu Bitcoinu znamená, že jakýkoli uživatel sítě může sledovat a analyzovat transakce všech ostatních účastníků. V důsledku toho je anonymita na úrovni transakcí nemožná. Anonymita je však zachována na úrovni individuální identifikace. Na rozdíl od tradičního bankovního systému, kde je každý účet spojen s osobní identitou, na Bitcoinu jsou prostředky spojeny s páry kryptografických klíčů, čímž uživatelům nabízejí formu pseudonymity za kryptografickými identifikátory.

Takto je důvěrnost na Bitcoinu ohrožena, když vnější pozorovatelé dokážou spojit konkrétní UTXO s identifikovanými uživateli. Jakmile je tato asociace navázána, stává se možné sledovat jejich transakce a analyzovat historii jejich bitcoinů. Coinjoin je přesně technika vyvinutá k přerušení sledovatelnosti UTXO, čímž nabízí určitou úroveň důvěrnosti uživatelům Bitcoinu na úrovni transakcí.

## Jak funguje Whirlpool?
Whirlpool se od ostatních metod coinjoinu odlišuje použitím transakcí "_ZeroLink_", které zajišťují, že mezi všemi vstupy a všemi výstupy není technicky možné žádné přímé spojení. Toto dokonalé míchání je dosaženo prostřednictvím struktury, kde každý účastník přispívá stejnou částkou na vstupu (kromě těžebních poplatků), čímž generuje výstupy dokonale stejných částek.
Tento restriktivní přístup k vstupům dává transakcím coinjoin Whirlpool jedinečnou vlastnost: úplnou absenci deterministických spojení mezi vstupy a výstupy. Jinými slovy, každý výstup má stejnou pravděpodobnost, že bude přiřazen jakémukoli účastníku, ve srovnání se všemi ostatními výstupy v transakci.
Původně byl počet účastníků v každém coinjoinu Whirlpool omezen na 5, s 2 novými účastníky a 3 remixéry (tyto koncepty vysvětlíme později). Nicméně, zvýšení poplatků za on-chain transakce pozorované v roce 2023 přimělo týmy Samourai k přehodnocení jejich modelu za účelem zlepšení soukromí při snižování nákladů. Takže s ohledem na tržní situaci poplatků a počet účastníků může koordinátor nyní organizovat coinjoiny zahrnující 6, 7 nebo 8 účastníků. Tyto rozšířené sezení jsou označovány jako "_Surge Cycles_". Je důležité poznamenat, že bez ohledu na konfiguraci jsou v coinjoinech Whirlpool vždy pouze 2 noví účastníci.

Takže transakce Whirlpool jsou charakterizovány stejným počtem vstupů a výstupů, které mohou být:
- 5 vstupů a 5 výstupů;
![coinjoin](assets/notext/2.webp)
- 6 vstupů a 6 výstupů;
![coinjoin](assets/notext/3.webp)
- 7 vstupů a 7 výstupů;
![coinjoin](assets/notext/4.webp) - 8 vstupů a 8 výstupů.
![coinjoin](assets/notext/5.webp)
Model navržený Whirlpool se tedy zakládá na malých transakcích coinjoin. Na rozdíl od Wasabi a JoinMarket, kde robustnost anonsetů závisí na objemu účastníků v jednom cyklu, Whirlpool sází na propojení několika malých cyklů.

V tomto modelu platí uživatel poplatky pouze při svém prvním vstupu do poolu, což jim umožňuje účastnit se mnoha remixů bez dalších poplatků. Jsou to noví účastníci, kteří pokrývají těžební poplatky pro remixéry.

S každým dalším coinjoinem, ve kterém se mince účastní společně se svými dřívějšími společníky, anonsety exponenciálně rostou. Cílem je tedy využít těchto bezplatných remixů, které při každém výskytu přispívají ke zvýšení hustoty anonsetů spojených s každou smíchanou mincí.

Whirlpool byl navržen s ohledem na dvě důležité požadavky:
- Dostupnost implementace na mobilních zařízeních, vzhledem k tomu, že Samourai Wallet je primárně aplikace pro smartphone;
- Rychlost cyklů remixování pro podporu významného nárůstu anonsetů.
Tyto imperativy vedly vývojáře Samourai Wallet při návrhu Whirlpool k omezení počtu účastníků na cyklus. Příliš málo účastníků by ohrozilo efektivitu coinjoinu, drasticky snížilo by se množství generovaných anonsetů v každém cyklu, zatímco příliš mnoho účastníků by představovalo problémy s řízením na mobilních aplikacích a brzdilo by tok cyklů.
**Nakonec není potřeba mít vysoký počet účastníků na coinjoin v Whirlpool, protože anonsety jsou dosaženy akumulací několika cyklů coinjoin.**

[-> Zjistěte více o anonsetech Whirlpool.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

### Pooly a poplatky za coinjoin
Aby tyto několik cyklů skutečně zvýšilo anonsety smíchaných mincí, musí být stanoven určitý rámec pro omezení použitých částek UTXO. Whirlpool tak definuje různé pooly.

Pool představuje skupinu uživatelů, kteří chtějí společně míchat, a dohodnou se na částce UTXO, která se má použít k optimalizaci procesu coinjoin. Každý pool specifikuje pevnou částku pro UTXO, které se uživatel musí držet, aby se mohl účastnit. Pro provádění coinjoinů s Whirlpool tedy musíte vybrat pool. Aktuálně dostupné pooly jsou následující:
- 0,5 bitcoinu;
- 0,05 bitcoinu;
- 0,01 bitcoinu;
- 0,001 bitcoinu (= 100 000 sats).

Připojením do poolu s vašimi bitcoiny budou rozděleny tak, aby generovaly UTXO, které jsou dokonale homogenní s těmi od ostatních účastníků v poolu. Každý pool má maximální limit; takže pro částky přesahující tento limit budete nuceni buď provést dvě samostatné vstupy v rámci stejného poolu nebo se orientovat na jiný pool s vyšší částkou:

| Pool (bitcoin) | Maximální částka na vstup (bitcoin) |
|----------------|------------------------------------|
| 0,5            | 35                                 |
| 0,05           | 3,5                                |
| 0,01           | 0,7                                |
| 0,001          | 0,025                              |
Jak bylo zmíněno dříve, UTXO je považováno za součást poolu, když je připraveno být začleněno do coinjoin. To ovšem neznamená, že uživatel o něj přichází. **Prostřednictvím různých cyklů míchání si uchováváte plnou kontrolu nad svými klíči a tím pádem nad svými bitcoiny.** To je to, co odlišuje techniku coinjoin od ostatních centralizovaných technik míchání.

Pro vstup do coinjoin poolu musí být zaplaceny poplatky za službu i těžební poplatky. Poplatky za službu jsou pro každý pool pevně stanoveny a mají za úkol kompenzovat týmy odpovědné za vývoj a údržbu Whirlpool.

Poplatky za použití Whirlpool se platí pouze jednou při vstupu do poolu. Po tomto kroku máte možnost účastnit se neomezeného počtu remixů bez jakýchkoli dalších poplatků. Zde jsou aktuální pevné poplatky pro každý pool:

| Pool (bitcoin) | Vstupní poplatek (bitcoin) |
|----------------|----------------------------|
| 0.5            | 0.0175                     |
| 0.05           | 0.00175                    |
| 0.01           | 0.0005 (50,000 sats)       |
| 0.001          | 0.00005 (5,000 sats)       |


Tyto poplatky v podstatě fungují jako vstupenka do vybraného poolu, bez ohledu na částku, kterou do coinjoin vložíte. Takže ať už vstoupíte do poolu 0.01 s přesně 0.01 BTC nebo do něj vstoupíte s 0.5 BTC, poplatky zůstanou stejné v absolutní hodnotě.

Před pokračováním k coinjoin má uživatel tedy na výběr mezi 2 strategiemi:
- Zvolit menší pool, aby minimalizoval poplatky za službu, s vědomím, že obdrží několik malých UTXO jako návrat;
- Nebo dát přednost většímu poolu, souhlasit s vyššími poplatky, aby nakonec získal menší počet UTXO větší hodnoty.

Je obecně nedoporučováno slučovat několik smíchaných UTXO po cyklech coinjoin, protože to může ohrozit získanou důvěrnost, zejména kvůli heuristice společného vlastnictví vstupů (CIOH). Proto může být rozumné zvolit větší pool, i když to znamená platit více, aby se předešlo mít příliš mnoho UTXO malé hodnoty jako výstup. Uživatel musí tyto kompromisy zvážit, aby si vybral pool, který preferuje.

Kromě poplatků za službu je třeba zvážit i těžební poplatky vlastní každé transakci Bitcoinu. Jako uživatel Whirlpool budete muset zaplatit těžební poplatky za přípravnou transakci (`Tx0`) stejně jako ty za první coinjoin. Všechny následující remixy budou zdarma, díky modelu Whirlpool, který se opírá o platby nových účastníků.

Ve skutečnosti, v každém coinjoin Whirlpool, jsou dva uživatelé mezi vstupy novými účastníky. Ostatní vstupy pocházejí od remixérů. V důsledku toho jsou těžební poplatky pro všechny účastníky transakce pokryty těmito dvěma novými účastníky, kteří pak také budou mít prospěch z bezplatných remixů:
![coinjoin](assets/en/6.webp)
Díky tomuto systému poplatků se Whirlpool skutečně odlišuje od ostatních služeb coinjoin, protože anonsety UTXO nejsou proporcionální k ceně zaplacené uživatelem. Takto je možné dosáhnout výrazně vysokých úrovní anonymity, a to pouze zaplacením vstupního poplatku do poolu a těžebních poplatků za dvě transakce (the `Tx0` a počáteční mix).
Je důležité poznamenat, že uživatel bude muset také pokrýt těžební poplatky, aby mohl vybrat své UTXO z poolu po dokončení svých několika coinjoinů, pokud si nevybral možnost `mix to`, o které si povíme v následujícím tutoriálu.

### Účty HD peněženky používané Whirlpoolem
Pro provedení coinjoinu prostřednictvím Whirlpoolu musí peněženka generovat několik odlišných účtů. Účet, v kontextu HD (*Hierarchical Deterministic*) peněženky, představuje sekci zcela izolovanou od ostatních, tato separace nastává na třetí úrovni hloubky hierarchie peněženky, tedy na úrovni `xpub`.

HD peněženka může teoreticky odvodit až `2^(32/2)` různých účtů. Počáteční účet, používaný ve výchozím nastavení ve všech Bitcoin peněženkách, odpovídá indexu `0'`.

Pro peněženky přizpůsobené Whirlpoolu, jako jsou Samourai nebo Sparrow, se používají 4 účty, aby vyhověly potřebám procesu coinjoin:
- Účet **deposit** (vklad), identifikovaný indexem `0'`;
- Účet **bad bank** (nebo doxxic change), identifikovaný indexem `2 147 483 644'`;
- Účet **premix**, identifikovaný indexem `2 147 483 645'`;
- Účet **postmix**, identifikovaný indexem `2 147 483 646'`.

Každý z těchto účtů plní specifickou funkci v rámci procesu coinjoin.

Všechny tyto účty jsou spojeny s jedním seedem, což umožňuje uživateli obnovit přístup ke všem svým bitcoinům pomocí své obnovovací fráze a případně svého hesla. Je však nutné během této obnovovací operace softwaru specifikovat různé indexy účtů, které byly použity.

Podívejme se nyní na různé fáze coinjoinu Whirlpool v těchto účtech.

### Různé fáze coinjoinů na Whirlpoolu
**Fáze 1: Tx0**
Výchozím bodem jakéhokoli coinjoinu Whirlpool je účet **deposit**. Tento účet automaticky používáte, když vytvoříte novou Bitcoin peněženku. Na tento účet musí být připsány bitcoiny, které si přejete smíchat.
`Tx0` představuje první krok v procesu míchání Whirlpool. Jeho cílem je připravit a vyrovnat UTXO pro coinjoin, rozdělením je na jednotky odpovídající částce vybraného poolu, aby se zajistila homogenita směsi. Vyrovnané UTXO jsou poté odeslány na účet **premix**. Co se týče rozdílu, který nemůže vstoupit do poolu, je oddělen do specifického účtu: **bad bank** (nebo "doxxic change").
Tato počáteční transakce `Tx0` slouží také k úhradě servisních poplatků koordinátorovi směsi. Na rozdíl od následujících kroků, tato transakce není kolaborativní; uživatel musí tedy převzít všechny těžební poplatky:
![coinjoin](assets/en/7.webp)

V tomto příkladu transakce `Tx0` je vstup `372,000 sats` z našeho účtu **deposit** rozdělen na několik výstupních UTXO, které jsou distribuovány následovně:
- Částka `5,000 sats` určená koordinátorovi za servisní poplatky, odpovídající vstupu do poolu `100,000 sats`;
- Tři UTXO připravené pro míchání, přesměrované na náš účet **premix** a zaregistrované u koordinátora. Tyto UTXO jsou vyrovnány na `108,000 sats` každý, aby pokryly těžební poplatky pro jejich budoucí počáteční mix;
- Přebytek, který nemůže vstoupit do poolu, protože je příliš malý, je považován za toxickou změnu. Je poslán na jeho specifický účet. Zde tato změna činí `40,000 sats`;
- Nakonec existují `3,000 sats`, které netvoří výstup, ale jsou to těžební poplatky potřebné k potvrzení `Tx0`.

Například zde je skutečný Whirlpool Tx0 (ne ode mě): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

**Krok 2: Toxická změna**
Přebytek, který nemohl být začleněn do poolu, zde ekvivalentní `40,000 sats`, je přesměrován na účet **špatné banky**, také označovaný jako "toxická změna", aby se zajistilo striktní oddělení od ostatních UTXO v peněžence.

Toto UTXO je nebezpečné pro soukromí uživatele, jelikož nejenže je stále připojeno ke své minulosti, a tedy možná k identitě jeho majitele, ale navíc je označeno jako patřící uživateli, který provedl coinjoin.
Pokud je toto UTXO sloučeno s míchanými výstupy, ztratí veškeré získané důvěrnostní vlastnosti během cyklů coinjoin, zejména kvůli Common-Input-Ownership-Heuristic (CIOH). Pokud je sloučeno s dalšími toxickými změnami, uživatel riskuje ztrátu důvěrnosti, protože to spojí různé vstupy cyklů coinjoin. Proto je nutné s ním zacházet opatrně. Způsob, jakým se má tato toxická UTXO spravovat, bude podrobně popsán v poslední části tohoto článku a budoucí tutoriály na PlanB Network tyto metody pokryjí podrobněji.

**Krok 3: Počáteční míchání**
Po dokončení `Tx0` jsou vyrovnávaná UTXO poslána na **premix** účet naší peněženky, připravena být začleněna do jejich prvního cyklu coinjoin, také nazývaného "počáteční míchání". Pokud, jak je tomu v našem příkladu, `Tx0` generuje více UTXO pro míchání, každé z nich bude začleněno do samostatného počátečního coinjoinu.

Na konci těchto prvních míchání bude **premix** účet prázdný, zatímco naše mince, které zaplatily těžební poplatky za tento první coinjoin, budou přesně upraveny na částku definovanou vybraným poolem. V našem příkladu budou naše počáteční UTXO `108 000 sats` snížena přesně na `100 000 sats`.
![coinjoin](assets/en/8.webp)
**Krok 4: Remixy**
Po počátečním míchání jsou UTXO převedeny na **postmix** účet. Tento účet shromažďuje již smíchaná UTXO a ta, která čekají na remixování. Když je klient Whirlpool aktivní, UTXO na **postmix** účtu jsou automaticky k dispozici pro remixování a budou náhodně vybrána k účasti na těchto nových cyklech.

Jako připomínka, remixy jsou poté 100% zdarma: nejsou vyžadovány žádné další poplatky za službu ani těžební poplatky. Udržení UTXO na **postmix** účtu tak udržuje jejich hodnotu nedotčenou a současně zlepšuje jejich anonsety. Proto je důležité umožnit těmto mincím účastnit se více cyklů coinjoin. Nestojí vás to absolutně nic a zvyšuje jejich úroveň anonymity.
Když se rozhodnete utratit smíšené UTXO, můžete tak učinit přímo z tohoto **postmix** účtu. Je doporučeno uchovávat smíšená UTXO na tomto účtu, abyste mohli využívat zdarma remixy a vyhnuli se jejich odchodu z Whirlpool oběhu, což by mohlo snížit jejich důvěrnost.
Jak uvidíme v následujícím tutoriálu, existuje také možnost `mix to`, která nabízí možnost automaticky poslat vaše smíšené mince do jiné peněženky, například do studené peněženky, po definovaném počtu coinjoinů.
Po probrání teorie se ponořme do praxe s tutoriálem na používání Whirlpool prostřednictvím aplikace Samourai Wallet pro Android!
## Tutoriál: Coinjoin Whirlpool na Samourai Wallet
Existuje mnoho možností, jak používat Whirlpool. Ta, kterou zde chci představit, je možnost Samourai Wallet (bez Dojo), open-source aplikace pro správu Bitcoin peněženky na Androidu.

Míchání na Samourai bez Dojo má tu výhodu, že je poměrně snadno ovladatelné, rychle se nastavuje a vyžaduje kromě telefonu s Androidem a internetového připojení žádné další zařízení.

Tato metoda má nicméně dvě významné nevýhody:
- Coinjoiny se budou odehrávat pouze tehdy, když Samourai běží na pozadí a je připojen. To znamená, že pokud chcete míchat a remixovat své bitcoiny 24/7, musíte neustále nechat Samourai zapnutý;
- Pokud používáte Whirlpool s Samourai Wallet bez toho, abyste se postarali o připojení vlastního Dojo, pak bude vaše aplikace muset být připojena k serveru udržovanému týmy Samourai, a vy tak odhalíte `xpub` vaší peněženky jim. Tyto anonymní informace jsou nezbytné, aby vaše aplikace našla vaše transakce.

Ideálním řešením, jak překonat tyto omezení, je provozovat vlastní Dojo spojené s instancí Whirlpool CLI na vašem osobním Bitcoin uzlu. Tímto způsobem se vyhnete jakémukoli úniku informací a dosáhnete úplné nezávislosti. Ačkoliv je tutoriál prezentovaný níže užitečný pro určité cíle nebo pro začátečníky, pro skutečnou optimalizaci vaší coinjoin session se doporučuje použít vlastní Dojo. Podrobný průvodce nastavením této konfigurace bude brzy dostupný na PlanB Network.

### Instalace Samourai Wallet
Začneme tím, že samozřejmě budete potřebovat aplikaci Samourai Wallet. Stáhnout ji můžete přímo z oficiálních stránek pomocí APK, z jejich GitLabu, nebo z Google Play Store.

### Vytvoření softwarové peněženky
Po instalaci softwaru budete muset pokračovat ve vytvoření Bitcoin peněženky na Samourai. Pokud už jednu máte, můžete přejít přímo k dalšímu kroku.

Po otevření aplikace stiskněte modré tlačítko `Start`. Poté budete vyzváni, abyste vybrali místo ve vašich telefonních souborech, kde bude uložena šifrovaná záloha vaší nové peněženky.

![samourai](assets/notext/9.webp)
Aktivujte Tor kliknutím na příslušný zářez. V této fázi máte také možnost vybrat konkrétní Dojo. V tomto tutoriálu však budeme pokračovat s výchozím Dojo; takže můžete nechat možnost zakázána. Když je Tor připojen, stiskněte tlačítko `Vytvořit novou peněženku`.
![samourai](assets/notext/10.webp)

Samourai Wallet vás poté vyzve k nastavení hesla BIP39. Toto dodatečné heslo je velmi důležité, protože přímo působí na odvození vašich soukromých klíčů. Případná ztráta tohoto hesla by vedla k nemožnosti přístupu k vašim bitcoinům, čímž by se staly nenávratně ztracenými. Pro obnovení vaší peněženky Samourai je nezbytné mít jak vaši 12slovnou obnovovací frázi, tak heslo.
Je tedy nezbytné vybrat si robustní heslovou frázi a udělat jednu nebo více fyzických kopií na papíře nebo na kovovém médiu, aby bylo zajištěno zabezpečení vašich bitcoinů. Po dokončení těchto úkolů zaškrtněte políčko `Jsem si vědom, že v případě ztráty...`, poté stiskněte tlačítko `DALŠÍ`.
![samourai](assets/notext/11.webp)

Poté musíte definovat PIN kód složený z 5 až 8 číslic. Tento kód zajistí přístup k vaší peněžence ve vašem telefonu. Bude požadován pokaždé, když budete chtít otevřít aplikaci Samourai. Zvolte robustní PIN kód a nezapomeňte si udělat záložní kopii. Poté můžete stisknout tlačítko `DALŠÍ`.

![samourai](assets/notext/12.webp)

Samourai vás pozve k opětovnému zadání vašeho PIN kódu pro potvrzení. Zadejte jej, poté stiskněte `DOKONČIT`.

![samourai](assets/notext/13.webp)

Poté získáte přístup k vaší obnovovací frázi složené ze 12 slov. Tato fráze umožňuje obnovit vaši peněženku s dříve zadanou heslovou frází. Je silně doporučeno udělat jednu nebo více kopií této fráze na fyzickém médiu, jako je papír nebo kovový materiál, aby bylo zajištěno zabezpečení vašich bitcoinů v případě problému.

Po provedení těchto záloh budete přesměrováni na rozhraní vaší nové peněženky Samourai.

![samourai](assets/notext/14.webp)

Je vám nabídnuto získat vašeho PayNym Bota. Můžete si jej vyžádat, pokud si přejete, ačkoli to není pro náš tutoriál nezbytné.

![samourai](assets/notext/15.webp)
Předtím, než začnete přijímat bitcoiny na tuto novou peněženku, je silně doporučeno znovu zkontrolovat platnost vašich záloh peněženky (heslová fráze a obnovovací fráze). Pro ověření heslové fráze můžete vybrat ikonu vašeho PayNym Bota umístěnou v levém horním rohu obrazovky, poté postupujte podle cesty:
```plaintext
Nastavení > Řešení problémů > Test heslové fráze/zálohy
```

Zadejte svou heslovou frázi pro provedení ověření.

![samourai](assets/notext/16.webp)

Samourai potvrdí, zda je platná.

![samourai](assets/notext/17.webp)

Pro ověření vaší zálohy obnovovací fráze přistupte k ikoně vašeho PayNym Bota, umístěné v levém horním rohu obrazovky, a postupujte podle této cesty:
```plaintext
Nastavení > Peněženka > Zobrazit 12-slovnou obnovovací frázi
```

Samourai zobrazí okno s vaší obnovovací frází. Ujistěte se, že přesně odpovídá vaší fyzické záloze.

Pro další a úplné ověření testu obnovy si poznamenejte svědecký prvek vaší peněženky, jako je jeden z `xpubs`, poté pokračujte v mazání vaší peněženky (pokud je stále prázdná). Cílem je pokusit se obnovit tuto prázdnou peněženku pouze pomocí vašich fyzických záloh. Pokud je obnova úspěšná, to naznačuje, že vaše zálohy jsou platné a spolehlivé.

### Přijímání bitcoinů
Po vytvoření vaší peněženky začnete s jedním účtem, identifikovaným indexem `0'`. To je **depozitní** účet, o kterém jsme mluvili v předchozích částech. Na tento účet budete potřebovat převést bitcoiny určené pro coinjoins.

K tomu klikněte na modré tlačítko `+` umístěné v pravém dolním rohu obrazovky.

![samourai](assets/notext/18.webp)

Poté klikněte na zelené tlačítko `Přijmout`.

![samourai](assets/notext/19.webp)

Samourai automaticky vygeneruje novou prázdnou adresu pro přijetí bitcoinů.

![samourai](assets/notext/20.webp)
Bitcoiny můžete poslat k mixování tam.
![samourai](assets/notext/21.webp)

### Vytvoření Tx0
Když je transakce potvrzena, můžeme začít s procesem coinjoin. K tomu klikněte na modré tlačítko `+` v pravém dolním rohu obrazovky.

![samourai](assets/notext/22.webp)

Poté klikněte na `Whirlpool` modře.

![samourai](assets/notext/23.webp)

Počkejte, dokud se Whirlpool inicializuje a Samourai vytvoří potřebné účty.

![samourai](assets/notext/24.webp)

Poté se dostanete na úvodní stránku Whirlpool. Klikněte na `Start`.
![samourai](assets/notext/25.webp)
Vyberte UTXO z účtu **deposit**, které chcete poslat do cyklů coinjoin, a poté klikněte na `Next`.

![samourai](assets/notext/26.webp)

V dalším kroku budete muset vybrat úroveň poplatku, který přiřadíte `Tx0` stejně jako vašemu prvnímu mixu. Toto nastavení určí rychlost, s jakou bude váš `Tx0` a váš počáteční coinjoin (nebo počáteční coinjoins) potvrzen. Mějte na paměti, že těžební poplatky za `Tx0` a počáteční mix jsou vaší zodpovědností, ale za následné remixy již těžební poplatky platit nemusíte. Máte na výběr mezi možnostmi `Low`, `Normal` nebo `High`.

![samourai](assets/notext/27.webp)

Ve stejném okně máte možnost vybrat pool, do kterého vstoupíte. Vzhledem k tomu, že jsem původně vybral UTXO `454,258 sats`, moje jediná možná volba je pool `100,000 sats`. Tato stránka vám také představuje poplatky za službu poolu, kromě těžebních poplatků, což vám umožňuje znát celkové náklady na tento cyklus coinjoin. Pokud vám vše vyhovuje, vyberte odpovídající pool a pokračujte kliknutím na modré tlačítko `VERIFY CYCLE DETAILS`.

![samourai](assets/notext/28.webp)

Poté uvidíte všechny detaily vašeho cyklu coinjoin:
- počet UTXO, které vstoupí do poolu;
- různé vzniklé poplatky;
- množství doxxic change...

Ověřte informace, a poté klikněte na zelené tlačítko `START CYCLE`.

![samourai](assets/notext/29.webp)

Objeví se okno, které vám nabídne označit toxickou změnu vzniklou vaším vstupem do cyklu coinjoin jako "nepoužitelnou". Pokud vyberete `YES`, toto UTXO nebude viditelné ve vaší peněžence a nebude možné jej vybrat pro budoucí transakce. Přesto zůstane přístupné v seznamu UTXO ve vaší peněžence, kde můžete ručně změnit jeho stav. Doporučuje se zvolit tuto možnost, aby se předešlo jakékoli chybě při manipulaci, která by později mohla ohrozit vaše soukromí. Pokud zvolíte `NO`, toxická změna zůstane ve vaší peněžence k dispozici pro použití. Pokud se chcete dozvědět více o správě a používání této toxické změny, doporučuji přečíst si poslední část tohoto návodu.

![samourai](assets/notext/30.webp)

Samourai poté odvysílá váš Tx0.

![samourai](assets/notext/31.webp)

### Provádění coinjoinů
Jakmile je Tx0 odvysílán, najdete jej na kartě `Transactions` v menu Whirlpool.

![samourai](assets/notext/32.webp)
Vaše UTXO připravené k mixování se nachází na záložce `Mixing in progress...`, která odpovídá účtu **Premix**.![samourai](assets/notext/33.webp)

Jakmile je `Tx0` potvrzeno, vaše UTXO budou automaticky zaregistrovány u koordinátora a počáteční mixování začne postupně automaticky.

![samourai](assets/notext/34.webp)

Kontrolou záložky `Remixing`, která odpovídá účtu **Postmix**, uvidíte UTXO vzniklé z počátečních mixů. Tyto mince zůstanou připraveny na následné remixování, které nebude vyžadovat žádné další poplatky. Doporučuji si přečíst tento další článek, abyste se dozvěděli více o procesu remixování a efektivitě cyklu coinjoin: [REMIX - WHIRLPOOL](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)

![samourai](assets/notext/35.webp)

Je možné dočasně pozastavit remixování UTXO stisknutím tlačítka pauza umístěného vpravo od něj. Aby bylo znovu způsobilé pro remixování, jednoduše na stejné tlačítko klikněte podruhé. Je důležité poznamenat, že každý uživatel a každý pool může provádět coinjoin pouze s jedním UTXO současně. Takže pokud máte 6 UTXO o `100 000 sats` připravených na coinjoin, může být mixováno pouze jedno z nich. Po mixování UTXO, Samourai Wallet pokračuje v náhodném výběru nového UTXO z vaší dostupnosti, aby diverzifikoval a vyvážil remixování každé mince.

![samourai](assets/notext/36.webp)

Pro zajištění nepřetržité dostupnosti vašich UTXO pro remixování je nutné nechat aplikaci Samourai aktivní na pozadí. Na vašem telefonu byste měli vidět oznámení potvrzující, že Whirlpool běží. Zavření aplikace nebo vypnutí telefonu pozastaví coinjoins.

### Dokončení coinjoinů
Pro utrácení vašich smíšených bitcoinů přejděte na účet **Postmix** označený jako `Remixing` v záložkách menu Whirlpool.

![samourai](assets/notext/37.webp)

Klikněte na modré logo Whirlpool umístěné v pravém dolním rohu.

![samourai](assets/notext/38.webp)

Poté klikněte na `Spend Mixed UTXOs`.

![samourai](assets/notext/39.webp)

Poté můžete zadat adresu příjemce a částku k odeslání stejným způsobem jako u jakékoli jiné transakce provedené s Samourai Wallet. Modré pozadí naznačuje, že prostředky jsou utraceny z účtu Whirlpool, a ne z **vkladového** účtu.

![samourai](assets/notext/40.webp)

Kliknutím na 3 malé tečky v pravém horním rohu máte možnost vybrat konkrétní UTXO.
![samourai](assets/notext/41.webp)
Kliknutím na bílý čtverec v pravém horním rohu okna můžete skenovat QR kód přijímací adresy vaší kamerou.

![samourai](assets/notext/42.webp)

Zadejte potřebné informace pro vaši transakci a poté klikněte na modré tlačítko `VERIFY TRANSACTION`.

![samourai](assets/notext/43.webp)
V dalším kroku máte možnost upravit sazbu poplatku spojenou s vaší transakcí. Také můžete aktivovat možnost Stonewall zaškrtnutím příslušného políčka. Pokud možnost Stonewall není vybratelná, znamená to, že váš účet **Postmix** neobsahuje UTXO dostatečné velikosti pro podporu této konkrétní struktury transakce.
[-> Zjistěte více o transakcích Stonewall.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)

Pokud je vše k vaší spokojenosti, klikněte na zelené tlačítko `SEND ... BTC`.

![samourai](assets/notext/44.webp)

Samourai poté pokračuje v podepisování vaší transakce před jejím vysíláním do sítě. Stačí počkat, až bude přidána do bloku těžařem.

![samourai](assets/notext/45.webp)

### Použití SCODE
Někdy týmy peněženky Samourai nabízejí "SCODEs". SCODE je propagační kód, který poskytuje slevu na poplatcích za službu poolu. Peněženka Samourai občas nabízí takové kódy svým uživatelům během speciálních událostí. Doporučuji vám [sledovat Samourai Wallet](https://twitter.com/SamouraiWallet) na sociálních médiích, abyste nepřišli o budoucí SCODES.

Pro použití SCODE v Samourai, před zahájením nového cyklu coinjoin, jděte do menu Whirlpool a vyberte tři malé tečky umístěné v pravém horním rohu obrazovky.

![samourai](assets/notext/46.webp)

Klikněte na `SCODE (promo kód) Whirlpool`.

![samourai](assets/notext/47.webp)

Zadejte SCODE do otevřeného okna, poté potvrďte kliknutím na `OK`.

![samourai](assets/notext/48.webp)

Whirlpool se automaticky zavře. Počkejte, až Samourai dokončí načítání, poté znovu otevřete menu Whirlpool.

![samourai](assets/notext/49.webp)

Ujistěte se, že váš SCODE byl správně zaregistrován kliknutím ještě jednou na tři malé tečky, poté vyberte `SCODE (promo kód) Whirlpool`. Pokud je vše v pořádku, jste připraveni zahájit nový cyklus Whirlpool se slevou na poplatky za službu. Je důležité poznamenat, že tyto SCODEs jsou dočasné: zůstávají platné několik dní předtím, než se stanou zastaralými.

## Jak poznat kvalitu našich cyklů coinjoin?
Pro skutečně účinný coinjoin je zásadní, aby prokázal dobrou uniformitu mezi částkami vstupů a výstupů. Tato uniformita zvyšuje počet možných interpretací v očích vnějšího pozorovatele, čímž zvyšuje nejistotu obklopující transakci. Pro kvantifikaci této nejistoty generované coinjoinem lze využít výpočet entropie transakce. Pro hlubší průzkum těchto ukazatelů vás odkazuji na tutoriál: [BOLTZMANN CALCULATOR](https://planb.network/en/tutorials/privacy/boltzmann-entropy). Model Whirlpool je uznáván jako ten, který přináší nejvíce homogenity coinjoinům.
Dále je hodnocen výkon několika cyklů coinjoin na základě rozsahu skupin, ve kterých je mince skryta. Velikost těchto skupin definuje, co se nazývá anonsety. Existují dva typy anonsetů: první hodnotí získané soukromí proti retrospektivní analýze (z přítomnosti do minulosti) a druhý proti prospektivní analýze (z minulosti do přítomnosti). Pro podrobné vysvětlení těchto dvou ukazatelů vás zvu, abyste si přečetli tutoriál: [WHIRLPOOL STATS TOOLS - ANONSETY](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)
## Jak spravovat postmix?
Po provedení cyklů coinjoin je nejlepší strategií nechat vaše UTXO na účtu **postmix**, čekající na jejich budoucí použití. Je dokonce doporučeno nechat je remixovat nekonečně, dokud je nepotřebujete utratit.

Někteří uživatelé by mohli zvážit převod svých smíchaných bitcoinů do peněženky zabezpečené hardware peněženkou. To je možné, ale je důležité pečlivě dodržovat doporučení Samourai Wallet, aby nedošlo ke kompromitaci získané důvěrnosti.

Spojování UTXO představuje nejčastěji dělanou chybu. Je nutné vyhnout se kombinování smíchaných UTXO s nesmíchanými UTXO ve stejné transakci, aby se předešlo CIOH (*Common-Input-Ownership-Heuristic*). To vyžaduje pečlivé řízení vašich UTXO v rámci vaší peněženky, zejména z hlediska označování. Kromě coinjoin je spojování UTXO obecně špatnou praxí, která často vede ke ztrátě důvěrnosti, pokud není správně řízena.
Měli byste být také opatrní při konsolidaci smíchaných UTXO mezi sebou. Mírné konsolidace jsou možné, pokud vaše smíchané UTXO mají významné anonsety, ale toto nevyhnutelně sníží soukromí vašich mincí. Ujistěte se, že konsolidace nejsou příliš velké ani provedené po nedostatečném počtu remixů, protože toto riziko vytváří odvoditelné vazby mezi vašimi UTXO před a po cyklech coinjoin. V případě pochybností o těchto operacích je nejlepší praxí nekonsolidovat postmix UTXO a převádět je jeden po druhém do vaší hardware peněženky, přičemž pokaždé generujete novou prázdnou adresu. Opět nezapomeňte správně označit každé přijaté UTXO.

Doporučuje se také nepřevádět vaše postmix UTXO do peněženky používající neobvyklé skripty. Například, pokud vstoupíte do Whirlpoolu z multisig peněženky používající skripty `P2WSH`, je málo pravděpodobné, že budete smícháni s ostatními uživateli, kteří mají původně stejný typ peněženky. Pokud opustíte svůj postmix do této stejné multisig peněženky, úroveň soukromí vašich smíchaných bitcoinů bude výrazně snížena. Kromě skriptů existuje mnoho dalších otisků peněženek, které vás mohou zmást.

Stejně jako u jakékoli bitcoinové transakce, je také vhodné nepoužívat znovu přijímací adresy. Každá nová transakce musí být přijata na novou prázdnou adresu.

Nejjednodušším a nejbezpečnějším řešením je nechat vaše smíchané UTXO odpočívat na jejich účtu **postmix**, nechat je remixovat a dotýkat se jich pouze, když je potřebujete utratit. Peněženky Samourai a Sparrow mají další ochrany proti všem těmto rizikům souvisejícím s analýzou řetězce. Tyto ochrany vám pomáhají vyhnout se chybám.

## Jak spravovat doxxic change?
Dále musíte být opatrní při správě doxxic change, drobných, které nemohly vstoupit do bazénu coinjoin. Tyto toxické UTXO, vzniklé použitím Whirlpoolu, představují riziko pro vaše soukromí, protože vytvářejí spojení mezi vámi a použitím coinjoin. Je tedy nezbytné zacházet s nimi opatrně a nekombinovat je s jinými UTXO, zejména smíchanými UTXO. Zde jsou různé strategie, které je třeba zvážit pro jejich použití:
- **Míchejte je v menších skupinách:** Pokud je váš toxický UTXO dostatečně velký na to, aby vstoupil do menší skupiny samostatně, zvažte jeho míchání. To je často nejlepší možnost. Je však zásadní nesloučit několik toxických UTXO, aby bylo možné vstoupit do skupiny, protože to by mohlo propojit vaše různé záznamy.
- **Označte je jako "nepoužitelné":** Dalším přístupem je přestat je používat, označit je jako "nepoužitelné" na jejich dedikovaném účtu a prostě je držet (Hodl). To zajistí, že je nevydáte omylem. Pokud hodnota bitcoinu vzroste, mohou se objevit nové skupiny lépe vhodné pro vaše toxické UTXO.
- **Dělejte dary:** Zvažte možnost dělat dary, i skromné, vývojářům pracujícím na Bitcoinu a jeho přidruženém softwaru. Můžete také darovat organizacím, které přijímají BTC. Pokud se vám zdá správa vašich toxických UTXO příliš složitá, můžete se jich jednoduše zbavit tím, že uděláte dar.
- **Kupujte dárkové karty:** Platformy jako [Bitrefill](https://www.bitrefill.com/) vám umožňují vyměnit bitcoiny za dárkové karty, které lze použít u různých obchodníků. To může být způsob, jak se zbavit vašich toxických UTXO bez ztráty přidružené hodnoty.
- **Konsolidujte je na Monero:** Samourai Wallet nyní nabízí službu atomické výměny mezi BTC a XMR. To je ideální pro správu toxických UTXO tím, že je konsolidujete na Monero, aniž byste ohrozili své soukromí prostřednictvím KYC, než je pošlete zpět na Bitcoin. Tato možnost však může být nákladná z hlediska poplatků za těžbu a prémie kvůli omezením likvidity.
- **Pošlete je do Lightning Network:** Převod těchto UTXO do Lightning Network, aby bylo možné využít snížené transakční poplatky, je možnost, která může být zajímavá. Tato metoda však může odhalit určité informace v závislosti na vašem používání Lightning a měla by být proto praktikována s opatrností.

Podrobné tutoriály k implementaci těchto různých technik budou brzy nabízeny na PlanB Network.

**Další zdroje:**
[Video tutoriál Samourai Wallet](https://planb.network/tutorials/wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956)
- [Dokumentace Samourai Wallet - Whirlpool](https://docs.samourai.io/whirlpool/basic-concepts);
- [Twitter vlákno o coinjoins](https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [Blogový příspěvek o coinjoins](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin).