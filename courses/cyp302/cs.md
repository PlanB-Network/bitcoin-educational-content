---
name: Úvod do formální kryptografie
goal: Hloubkový úvod do vědy a praxe kryptografie.
objectives:
  - Prozkoumat Bealeovy šifry a moderní kryptografické metody pro pochopení základních a historických konceptů kryptografie.
  - Ponořit se do teorie čísel, grup a polí pro osvojení klíčových matematických konceptů, na kterých kryptografie stojí.
  - Studovat proudovou šifru RC4 a AES s 128bitovým klíčem pro poznání symetrických kryptografických algoritmů.
  - Prozkoumat kryptosystém RSA, distribuci klíčů a hašovací funkce pro průzkum asymetrické kryptografie.

---
# Hloubkový pohled na kryptografii

Je obtížné najít mnoho materiálů, které by nabízely dobrý střední cestu ve vzdělávání v oblasti kryptografie.

Na jedné straně jsou rozsáhlé, formální pojednání, která jsou skutečně přístupná pouze těm s pevným základem v matematice, logice nebo nějaké jiné formální disciplíně. Na druhé straně existují velmi vysoké úrovně úvodů, které skutečně skrývají příliš mnoho detailů pro každého, kdo je alespoň trochu zvědavý.

Tento úvod do kryptografie se snaží zachytit střední cestu. Ačkoli by to mělo být relativně náročné a podrobné pro každého, kdo je nový v kryptografii, není to zajíček v díře typického základního pojednání.

+++

# Úvod
<partId>bbed2f46-d64c-5fb5-b892-d726032f2494</partId>

## Krátký popis
<chapterId>bb8a8b73-7fb2-50da-bf4e-98996d79887b</chapterId>

Tato kniha nabízí hloubkový úvod do vědy a praxe kryptografie. Kde je to možné, zaměřuje se na konceptuální, spíše než formální výklad materiálu.

> Tento kurz je založen na [JWBurgers's repo](https://github.com/JWBurgers/An_Introduction_to_Cryptography). Všechna práva patří jemu. Obsah ještě není dokončen a je zde pouze pro ukázku, jak bychom ho mohli integrovat, pokud by JWburger souhlasil.

### Motivace a cíle

Je obtížné najít mnoho materiálů, které by nabízely dobrý střední cestu ve vzdělávání v oblasti kryptografie.

Na jedné straně jsou rozsáhlé, formální pojednání, která jsou skutečně přístupná pouze těm s pevným základem v matematice, logice nebo nějaké jiné formální disciplíně. Na druhé straně existují velmi vysoké úrovně úvodů, které skutečně skrývají příliš mnoho detailů pro každého, kdo je alespoň trochu zvědavý.

Tento úvod do kryptografie se snaží zachytit střední cestu. Ačkoli by to mělo být relativně náročné a podrobné pro každého, kdo je nový v kryptografii, není to zajíček v díře typického základního pojednání.

### Cílová skupina

Od vývojářů po intelektuálně zvědavé, tato kniha je užitečná pro každého, kdo chce více než povrchní pochopení kryptografie. Pokud je vaším cílem ovládnout oblast kryptografie, pak je tato kniha také dobrým výchozím bodem.

### Doporučení k četbě

Kniha v současné době obsahuje sedm kapitol: "Co je kryptografie?" (Kapitola 1), "Matematické základy kryptografie I" (Kapitola 2), "Matematické základy kryptografie II" (Kapitola 3), "Symetrická kryptografie" (Kapitola 4), "RC4 a AES" (Kapitola 5), "Asymetrická kryptografie" (Kapitola 6) a "Kryptosystém RSA" (Kapitola 7). Poslední kapitola, "Kryptografie v praxi", bude ještě přidána. Zaměřuje se na různé kryptografické aplikace, včetně zabezpečení transportní vrstvy, onion routingu a systému výměny hodnot Bitcoinu.
Pokud nemáte silné zázemí v matematice, teorie čísel je pravděpodobně nejtěžším tématem v této knize. Přehled o ní nabízím v kapitole 3, a objevuje se také v exponátu AES v kapitole 5 a kryptosystému RSA v kapitole 7.
Pokud se opravdu potýkáte s formálními detaily v těchto částech knihy, doporučuji vám, abyste se při prvním čtení spokojili s vysokoúrovňovým přečtením.

### Poděkování

Nejvíce vlivná kniha, která formovala tuto, byla _Úvod do moderní kryptografie_ od Jonathana Katze a Yehudy Lindella, CRC Press (Boca Raton, FL), 2015. Doprovodný kurz je dostupný na Coursera pod názvem "Kryptografie."

Hlavní další zdroje, které byly užitečné při vytváření přehledu v této knize, jsou Simon Singh, _Kniha kódů_, Fourth Estate (Londýn, 1999); Christof Paar a Jan Pelzl, _Porozumění kryptografii_, Springer (Heidelberg, 2010) a [kurz založený na knize od Paara nazvaný “Úvod do kryptografie”](https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg); a Bruce Schneier, Aplikovaná kryptografie, 2. vydání, 2015 (Indianapolis, IN: John Wiley & Sons).

Budu citovat pouze velmi specifické informace a výsledky, které z těchto zdrojů přebírám, ale zde chci vyjádřit svůj obecný dluh vůči nim.

Pro ty čtenáře, kteří chtějí po tomto úvodu hledat pokročilejší znalosti o kryptografii, velmi doporučuji knihu Katze a Lindella. Katzův kurz na Coursera je poněkud přístupnější než kniha.

### Příspěvky

Podívejte se prosím na [soubor s příspěvky v repozitáři](https://github.com/JWBurgers/An_Introduction_to_Cryptography/blob/master/Contributions.md) pro nějaké pokyny, jak podpořit projekt.

### Notace

**Klíčové termíny:**

Klíčové termíny v úvodech jsou zavedeny zvýrazněním tučně. Například, zavedení šifry Rijndael jako klíčového termínu by vypadalo takto: **šifra Rijndael**.

Klíčové termíny jsou explicitně definovány, pokud nejde o vlastní jména nebo jejich význam je zřejmý z diskuse.

Definice je obvykle dána při zavedení klíčového termínu, i když někdy je vhodnější nechat definici na pozdější místo.

**Zvýrazněná slova a fráze:**

Slova a fráze jsou zvýrazněna kurzívou. Například fráze "Pamatujte si své heslo" by vypadala takto: *Pamatujte si své heslo*.

**Formální notace:**

Formální notace se týká hlavně proměnných, náhodných proměnných a množin.

* Proměnné: Ty jsou obvykle označeny malým písmenem (např. "x" nebo "y"). Někdy jsou pro jasnost psány velkými písmeny (např. "M" nebo "K").
* Náhodné proměnné: Ty jsou vždy označeny velkým písmenem (např. "X" nebo "Y")
* Množiny: Ty jsou vždy označeny tučnými, velkými písmeny (např. **S**)

# Co je kryptografie?
<partId>48e4d6d5-cd00-5c00-8adb-ae8477ff47c4</partId>

## Bealeovy šifry
<chapterId>ae674346-4789-5ab1-9b6f-c8989d83be89</chapterId>
Pojďme zahájit naše zkoumání oblasti kryptografie jednou z nejzajímavějších a nejzábavnějších epizod v její historii: příběhem Bealeových šifer. [1]
Příběh Bealeových šifer je podle mého názoru spíše fikcí než realitou. Ale údajně se odehrál takto.

V zimě roku 1820 a poté znovu v roce 1822 se muž jménem Thomas J. Beale ubytoval v hostinci vlastněném Robertem Morrissem v Lynchburgu (Virginie). Na konci Bealeova druhého pobytu předal Morrissovi železnou skříňku s cennými papíry k bezpečnému uschování.

O několik měsíců později Morrisse obdržel dopis od Bealea datovaný 9. května 1822. Dopis zdůrazňoval velkou hodnotu obsahu železné skříňky a obsahoval některé instrukce pro Morrisse: pokud by se Beale ani žádný z jeho společníků nikdy nepřišli skříňku vyzvednout, měl by ji otevřít přesně deset let od data dopisu (tj. 9. května 1832). Některé papíry uvnitř by byly napsány běžným textem. Několik dalších by však bylo „nesrozumitelných bez pomoci klíče“. Tento „klíč“ by pak Morrissovi měl doručit nejmenovaný přítel Bealea v červnu 1832.

Přes jasné instrukce Morrisse skříňku v květnu 1832 neotevřel a Bealeův tajemný přítel se v červnu toho roku neobjevil. Až do roku 1845 se hostinský konečně rozhodl skříňku otevřít. V ní našel Morrisse poznámku vysvětlující, jak Beale a jeho společníci objevili zlato a stříbro na západě a pohřbili je spolu s nějakými šperky pro bezpečné uschování. Kromě toho skříňka obsahovala tři **šifrované texty**: tj. texty napsané v kódu, které vyžadují **kryptografický klíč**, nebo tajemství, a doprovodný algoritmus k jejich odemčení. Tento proces odemykání šifrovaného textu se nazývá **dešifrování**, zatímco proces zamykání se nazývá **šifrování**. (Jak je vysvětleno v kapitole 3, termín šifra může mít různé významy. V názvu "Bealeovy šifry" je zkratkou pro šifrované texty.)

Tři šifrované texty, které Morrisse našel v železné skříňce, se skládají z řady čísel oddělených čárkami. Podle Bealeovy poznámky tyto šifrované texty samostatně poskytují umístění pokladu, obsah pokladu a seznam jmen s právoplatnými dědici pokladu a jejich podíly (poslední informace jsou relevantní v případě, že by se Beale a jeho společníci nikdy nepřišli skříňku vyzvednout).

Morrisse se pokoušel tři šifrované texty dešifrovat dvacet let. To by bylo snadné s klíčem. Ale Morrisse klíč neměl a jeho pokusy o obnovení původních textů, nebo **otevřených textů**, jak se obvykle nazývají v kryptografii, byly neúspěšné.

Když se blížil ke konci svého života, Morrisse předal skříňku příteli v roce 1862. Tento přítel následně v roce 1885 publikoval brožuru pod pseudonymem J.B. Ward. Obsahovala popis (údajné) historie skříňky, tři šifrované texty a řešení, které pro druhý šifrovaný text našel. (Zdá se, že existuje jeden klíč pro každý šifrovaný text, a ne jeden klíč, který by fungoval na všechny tři šifrované texty, jak Beale původně naznačil ve svém dopise Morrissovi.)

Druhý šifrovaný text můžete vidět na *Obrázku 2* níže. [2] Klíčem k tomuto šifrovanému textu je Deklarace nezávislosti Spojených států. Procedura dešifrování spočívá v aplikaci následujících dvou pravidel:
* Pro jakékoli číslo n v šifrovaném textu, najděte n-té slovo v Deklaraci nezávislosti Spojených států amerických* Nahraďte číslo n prvním písmenem slova, které jste našli


*Obrázek 1: Bealeova šifra č. 2*

![Obrázek 1: Bealeova šifra č. 2](assets/Figure1-1.webp "Obrázek 1: Bealeova šifra č. 2")


Například první číslo druhého šifrovaného textu je 115. 115té slovo Deklarace nezávislosti je “instituted,” takže první písmeno otevřeného textu je “i.” Šifrovaný text přímo neudává mezery mezi slovy a velká písmena. Ale po dešifrování prvních několika slov můžete logicky usoudit, že první slovo otevřeného textu bylo prostě “I.” (Otevřený text začíná frází “I have deposited in the county of Bedford.”)

Po dešifrování druhá zpráva poskytuje detailní obsah pokladu (zlato, stříbro a drahokamy) a naznačuje, že byl pohřben v železných hrncích a pokryt kameny v okrese Bedford (Virginie). Lidé mají rádi dobré záhady, takže bylo vynaloženo velké úsilí na dešifrování ostatních dvou Bealeových šifer, zejména té, která popisuje polohu pokladu. Dokonce i různí prominentní kryptografové se jich pokusili rozluštit. Avšak dosud se nikomu nepodařilo dešifrovat ostatní dvě šifrované zprávy.


**Poznámky:**

[1] Pro dobré shrnutí příběhu viz Simon Singh, *The Code Book*, Fourth Estate (Londýn, 1999), str. 82-99. Krátký film o příběhu byl natočen Andrewem Allenem v roce 2010. Film, “The Thomas Beale Cipher,” můžete najít [na jeho webové stránce](http://www.thomasbealecipher.com/).

[2] Tento obrázek je dostupný na Wikipedii na stránce Bealeových šifer.


## Moderní kryptografie
<chapterId>d07d576f-8a4b-5890-b182-2e5763f550f4</chapterId>

Pestré příběhy, jako je ten o Bealeových šifrách, jsou to, co většina z nás spojuje s kryptografií. Přesto se moderní kryptografie liší alespoň ve čtyřech důležitých bodech od těchto typů historických příkladů.

Za prvé, historicky byla kryptografie zaměřena pouze na **tajnost** (nebo důvěrnost). [3] Šifrované texty byly vytvářeny tak, aby k informacím v otevřeném textu měly přístup pouze určité strany, jako v případě Bealeových šifer. Aby šifrovací schéma dobře sloužilo tomuto účelu, dešifrování šifrovaného textu by mělo být proveditelné pouze pokud máte klíč.

Moderní kryptografie se zabývá širším spektrem témat než jen tajnost. Tato témata zahrnují primárně (1) **integritu zprávy**—to znamená, zajištění, že zpráva nebyla změněna; (2) **autenticitu zprávy**—to znamená, zajištění, že zpráva skutečně pochází od určitého odesílatele; a (3) **neodvolatelnost**—to znamená, zajištění, že odesílatel nemůže později nepravdivě popřít, že zprávu odeslal. [4]

Důležité je mít na paměti rozlišení mezi **šifrovacím schématem** a **kryptografickým schématem**. Šifrovací schéma se týká pouze tajnosti. Zatímco šifrovací schéma je kryptografické schéma, opak není pravda. Kryptografické schéma může sloužit i dalším hlavním tématům kryptografie, včetně integrity, autenticity a neodvolatelnosti.
Témata integrity a autenticity jsou stejně důležitá jako tajnost. Naše moderní komunikační systémy by nemohly fungovat bez záruk ohledně integrity a autenticity komunikace. Nezpochybnitelnost je také důležitým aspektem, například u digitálních smluv, ale v kryptografických aplikacích není potřeba tak všeobecně jako tajnost, integrita a autenticita.

Za druhé, klasické šifrovací schématy, jako jsou Bealeovy šifry, vždy zahrnovaly jeden klíč, který byl sdílen mezi všemi relevantními stranami. Mnoho moderních kryptografických schémat však zahrnuje ne jeden, ale dva klíče: **soukromý** a **veřejný klíč**. Zatímco první by měl zůstat soukromý ve všech aplikacích, druhý je typicky veřejně známý (odtud jejich názvy). V oblasti šifrování může být veřejný klíč použit k zašifrování zprávy, zatímco soukromý klíč může být použit pro dešifrování.

Odvětví kryptografie, které se zabývá schématy, kde všechny strany sdílejí jeden klíč, je známé jako **symetrická kryptografie**. Jednotlivý klíč v takovém schématu se obvykle nazývá **soukromý klíč** (nebo tajný klíč). Odvětví kryptografie, které se zabývá schématy vyžadujícími pár soukromého a veřejného klíče, je známé jako **asymetrická kryptografie**. Tyto obory jsou někdy také označovány jako **kryptografie soukromého klíče** a **kryptografie veřejného klíče**, i když to může způsobit zmatek, protože schémata veřejného klíče také mají soukromé klíče.

Příchod asymetrické kryptografie na konci 70. let 20. století byl jednou z nejdůležitějších událostí v historii kryptografie. Bez ní by většina našich moderních komunikačních systémů, včetně Bitcoinu, nebyla možná, nebo by byla alespoň velmi nepraktická.

Důležité je, že moderní kryptografie není výhradně studiem symetrických a asymetrických kryptografických schémat (i když to pokrývá velkou část oboru). Například kryptografie se také zabývá hašovacími funkcemi a generátory pseudonáhodných čísel, a na těchto primitivních prvcích můžete stavět aplikace, které nejsou související se symetrickou nebo asymetrickou kryptografií.

Za třetí, klasická šifrovací schémata, jako ta používaná v Bealeových šifrách, byla spíše uměním než vědou. Jejich vnímaná bezpečnost byla z velké části založena na intuicích týkajících se jejich složitosti. Obvykle byly opravovány, když byl objeven nový útok proti nim, nebo zcela opuštěny, pokud byl útok zvláště vážný. Moderní kryptografie je však přísná věda s formálním, matematickým přístupem k vývoji a analýze kryptografických schémat.

Konkrétně, moderní kryptografie se soustředí na formální **důkazy bezpečnosti**. Jakýkoliv důkaz bezpečnosti pro kryptografické schéma probíhá ve třech krocích:

1. Vyjádření **kryptografické definice bezpečnosti**, tj. souboru bezpečnostních cílů a hrozby, kterou představuje útočník.
2. Vyjádření jakýchkoli matematických předpokladů týkajících se výpočetní složitosti schématu. Například kryptografické schéma může obsahovat generátor pseudonáhodných čísel. I když nemůžeme dokázat, že existují, můžeme předpokládat, že ano.
3. Expozice matematického **důkazu bezpečnosti** schématu na základě formálního pojmu bezpečnosti a jakýchkoli matematických předpokladů.

Za čtvrté, zatímco historicky byla kryptografie primárně využívána v vojenských nastaveních, v digitálním věku pronikla do našich každodenních aktivit. Ať už bankujete online, přispíváte na sociálních médiích, kupujete produkt na Amazonu svou kreditní kartou, nebo posíláte bitcoin příteli, kryptografie je sine qua non naší digitální doby.

Vzhledem k těmto čtyřem aspektům moderní kryptografie bychom mohli moderní **kryptografii** charakterizovat jako vědu zabývající se formálním vývojem a analýzou kryptografických schémat k zabezpečení digitálních informací proti nepřátelským útokům. Bezpečnost zde by měla být chápána široce jako prevence útoků, které poškozují tajnost, integritu, autentizaci a/nebo nezpochybnitelnost v komunikaci.
Kryptografie je nejlépe chápána jako subdisciplína **kybernetické bezpečnosti**, která se zabývá prevencí před krádeží, poškozením a zneužitím počítačových systémů. Je třeba si všimnout, že mnoho otázek kybernetické bezpečnosti má malou nebo pouze částečnou souvislost s kryptografií.
Například, pokud společnost uchovává drahé servery lokálně, může se obávat zabezpečení tohoto hardwaru proti krádeži a poškození. Ačkoliv se jedná o otázku kybernetické bezpečnosti, má to málo společného s kryptografií.

Jako další příklad, **phishingové útoky** jsou běžným problémem v naší moderní době. Tyto útoky se snaží oklamat lidi prostřednictvím e-mailu nebo jiného komunikačního média, aby vydali citlivé informace, jako jsou hesla nebo čísla kreditních karet. Ačkoliv kryptografie může pomoci řešit phishingové útoky do určité míry, komplexní přístup vyžaduje více než jen použití nějaké kryptografie.

**Poznámky:**

[3] Přesně řečeno, důležité aplikace kryptografických schémat byly zaměřeny na tajnost. Děti, například, často používají jednoduchá kryptografická schémata pro "zábavu". V těchto případech tajnost opravdu není záležitostí.

[4] Bruce Schneier, *Applied Cryptography*, 2. vydání, 2015 (Indianapolis, IN: John Wiley & Sons), str. 2.

[5] Viz Jonathan Katz a Yehuda Lindell, *Introduction to Modern Cryptography*, CRC Press (Boca Raton, FL: 2015), zejména str. 16–23, pro dobrý popis.

[6] Cf. Katz a Lindell, tamtéž, str. 3. Myslím, že jejich charakterizace má některé problémy, tak zde prezentuji mírně odlišnou verzi jejich tvrzení.

## Otevřená komunikace
<chapterId>cb23d0a6-ba9a-5dc6-a55a-258405ae4117</chapterId>

Moderní kryptografie je navržena tak, aby poskytovala záruky bezpečnosti v prostředí **otevřené komunikace**. Pokud je náš komunikační kanál tak dobře chráněný, že odposlouchávači nemají šanci manipulovat s našimi zprávami nebo je dokonce jen pozorovat, pak je kryptografie zbytečná. Většina našich komunikačních kanálů však není takto dobře chráněna.

Základem komunikace v moderním světě je masivní síť vláknových optických kabelů. Telefonování, sledování televize a prohlížení webu v moderní domácnosti se obecně spoléhá na tuto síť vláknových optických kabelů (malé procento může spoléhat čistě na satelity). Je pravda, že doma můžete mít různé datové připojení, jako je koaxiální kabel, (asymetrická) digitální předplatitelská linka a vláknový optický kabel. Ale alespoň ve vyspělém světě se tyto různé datové média rychle spojují mimo váš dům k uzlu v masivní síti vláknových optických kabelů, která spojuje celý svět. Výjimky jsou některé odlehlé oblasti vyspělého světa, jako jsou Spojené státy a Austrálie, kde může datový provoz stále cestovat na značné vzdálenosti po tradičních měděných telefonních drátech.

Bylo by nemožné zabránit potenciálním útočníkům ve fyzickém přístupu k této síti kabelů a její podpůrné infrastruktuře. Ve skutečnosti už víme, že většina našich dat je zachycena různými národními zpravodajskými agenturami na klíčových křižovatkách internetu.[7] To zahrnuje vše od zpráv na Facebooku po webové adresy, které navštěvujete.

Zatímco sledování dat na masivním měřítku vyžaduje mocného protivníka, jako je národní zpravodajská agentura, útočníci s málo zdroji mohou snadno pokusit o špehování na lokálnější úrovni. Ačkoliv se to může stát na úrovni odposlouchávání kabelů, je mnohem snazší prostě zachytit bezdrátovou komunikaci.
Většina dat naší lokální sítě – ať už doma, v kanceláři nebo v kavárně – nyní cestuje prostřednictvím rádiových vln k bezdrátovým přístupovým bodům všestranných routerů, namísto fyzických kabelů. Útočník tedy potřebuje málo prostředků k zachycení jakéhokoli vašeho lokálního provozu. To je obzvláště znepokojivé, protože většina lidí dělá velmi málo pro ochranu dat, která cestují přes jejich lokální sítě. Kromě toho mohou potenciální útočníci cílit i na naše mobilní širokopásmové připojení, jako jsou 3G, 4G a 5G. Všechna tato bezdrátová komunikace je snadným cílem pro útočníky.
Proto je myšlenka udržet komunikaci v tajnosti ochranou komunikačního kanálu pro většinu moderního světa beznadějně iluzorním cílem. Vše, co víme, vyvolává vážnou paranoiu: měli byste vždy předpokládat, že vás někdo poslouchá. A kryptografie je hlavním nástrojem, který máme k získání jakékoli formy bezpečnosti v tomto moderním prostředí.

**Poznámky:**

[7] Viz například Olga Khazan, “The creepy, long-standing practice of undersea cable tapping”, *The Atlantic*, 16. července 2013 (dostupné na [The Atlantic](https://www.theatlantic.com/international/archive/2013/07/the-creepy-long-standing-practice-of-undersea-cable-tapping/277855/)).

# Matematické základy kryptografie 1
<partId>1bf9f0aa-0f68-5493-83fb-2167238ff9de</partId>

## Náhodné proměnné
<chapterId>b623a7d0-3dff-5803-bd4e-8257ff73dd69</chapterId>

Kryptografie se opírá o matematiku. A pokud chcete mít více než povrchní porozumění kryptografii, musíte být s touto matematikou obeznámeni.

Tato kapitola představuje většinu základní matematiky, se kterou se setkáte při studiu kryptografie. Témata zahrnují náhodné proměnné, modulové operace, operace XOR a pseudonáhodnost. Materiál v těchto sekcích byste měli ovládnout pro jakékoli nepovrchní porozumění kryptografii.

Další sekce se zabývá teorií čísel, která je mnohem náročnější.

### Náhodné proměnné

Náhodná proměnná je typicky označena ne-tučným, velkým písmenem. Takže například můžeme mluvit o náhodné proměnné $X$, náhodné proměnné $Y$ nebo náhodné proměnné $Z$. Toto označení budu používat i nadále.

**Náhodná proměnná** může nabývat dvou nebo více možných hodnot, každá s určitou kladnou pravděpodobností. Možné hodnoty jsou uvedeny v **souboru výsledků**.

Pokaždé, když **vzorkujete** náhodnou proměnnou, vyberete konkrétní hodnotu z jejího souboru výsledků podle definovaných pravděpodobností.

Pojďme se podívat na jednoduchý příklad. Předpokládejme proměnnou $X$, která je definována následovně:

- $X$ má soubor výsledků $\{1,2\}$

$$
Pr[X = 1] = 0.5
$$

$$
Pr[X = 2] = 0.5
$$

Je snadné vidět, že $X$ je náhodná proměnná. Za prvé, existují dvě nebo více možných hodnot, které $X$ může nabýt, konkrétně $1$ a $2$. Za druhé, každá možná hodnota má kladnou pravděpodobnost výskytu při vzorkování $X$, konkrétně $0.5$.
Vše, co náhodná proměnná vyžaduje, je množina výsledků se dvěma nebo více možnostmi, kde každá možnost má kladnou pravděpodobnost výskytu při vzorkování. Náhodná proměnná může být tedy v principu definována abstraktně, bez jakéhokoli kontextu. V tomto případě si můžete vzorkování představit jako provádění nějakého přírodního experimentu k určení hodnoty náhodné proměnné.
Proměnná $X$ výše byla definována abstraktně. Můžete si tedy vzorkování proměnné $X$ představit jako hod spravedlivou mincí a přiřazení „2“ v případě hlavy a „1“ v případě orel. Při každém vzorku $X$ minci znovu hodíte.

Alternativně si můžete vzorkování $X$ představit také jako hod spravedlivou kostkou a přiřazení „2“ v případě, že kostka padne na $1$, $3$, nebo $4$, a přiřazení „1“ v případě, že kostka padne na $2$, $5$, nebo $6“. Při každém vzorkování $X$ kostku znovu hodíte.

Opravdu, jakýkoliv přírodní experiment, který by vám umožnil definovat pravděpodobnosti možných hodnot $X$ výše, lze představit s ohledem na kreslení.

Často však nejsou náhodné proměnné zaváděny pouze abstraktně. Místo toho má sada možných výsledných hodnot explicitní reálný význam (spíše než jen jako čísla). Kromě toho mohou být tyto výsledné hodnoty definovány vůči nějakému konkrétnímu typu experimentu (spíše než jako jakýkoliv přírodní experiment s těmito hodnotami).

Pojďme nyní zvážit příklad proměnné $X$, která není definována abstraktně. X je definováno následovně, aby se určilo, který ze dvou týmů začne fotbalový zápas:

- $X$ má množinu výsledků {červený začíná, modrý začíná}
- Hod konkrétní mincí $C$: orel = „červený začíná“; hlava = „modrý začíná“

$$
Pr [X = \text{červený začíná}] = 0.5
$$

$$
Pr [X = \text{modrý začíná}] = 0.5
$$

V tomto případě je množina výsledků X poskytnuta s konkrétním významem, totiž kdo začne ve fotbalovém zápase. Kromě toho jsou možné výsledky a jejich přidružené pravděpodobnosti určeny konkrétním experimentem, totiž hodem konkrétní mincí $C$.

V diskusích o kryptografii jsou náhodné proměnné obvykle zaváděny proti množině výsledků s reálným významem. Může to být sada všech zpráv, které by mohly být zašifrovány, známá jako prostor zpráv, nebo sada všech klíčů, které mohou strany používající šifrování vybrat, známá jako prostor klíčů.

Náhodné proměnné v diskusích o kryptografii však obvykle nejsou definovány proti nějakému konkrétnímu přírodnímu experimentu, ale proti jakémukoli experimentu, který by mohl poskytnout správné pravděpodobnostní rozdělení.

Náhodné proměnné mohou mít diskrétní nebo spojité pravděpodobnostní rozdělení. Náhodné proměnné s **diskrétním pravděpodobnostním rozdělením**—to znamená diskrétní náhodné proměnné—mají konečný počet možných výsledků. Náhodná proměnná $X$ ve všech dosud uvedených příkladech byla diskrétní.

**Spojité náhodné proměnné** mohou místo toho nabývat hodnot v jednom nebo více intervalech. Můžete například říci, že náhodná proměnná při vzorkování nabude jakoukoliv skutečnou hodnotu mezi 0 a 1, a že každé skutečné číslo v tomto intervalu je stejně pravděpodobné. V tomto intervalu existuje nekonečně mnoho možných hodnot.

Pro diskuse o kryptografii budete potřebovat pouze porozumění diskrétním náhodným proměnným. Jakákoli diskuse o náhodných proměnných od tohoto bodu by tedy měla být chápána jako odkazující na diskrétní náhodné proměnné, pokud není výslovně uvedeno jinak.

### Grafy náhodných proměnných
Možné hodnoty a s nimi spojené pravděpodobnosti pro náhodnou proměnnou lze snadno vizualizovat pomocí grafu. Například zvažte náhodnou proměnnou $X$ z předchozí sekce s množinou výsledků $\{1, 2\}$, a $Pr [X = 1] = 0.5$ a $Pr [X = 2] = 0.5$. Takovou náhodnou proměnnou bychom typicky zobrazovali ve formě sloupcového grafu, jak je vidět na *Obrázku 1*.
*Obrázek 1: Náhodná proměnná X*

![Obrázek 1: Náhodná proměnná X.](assets/Figure2-1.webp)

Široké sloupce na *Obrázku 1* samozřejmě neznamenají, že by náhodná proměnná $X$ byla ve skutečnosti spojitá. Místo toho jsou sloupce široké, aby byly vizuálně atraktivnější (jen úzká čára nahoru poskytuje méně intuitivní vizualizaci).

### Rovnoměrné proměnné

Ve výrazu "náhodná proměnná" termín "náhodná" znamená "pravděpodobnostní". Jinými slovy, znamená to, že dvě nebo více možných výsledků proměnné se vyskytuje s určitými pravděpodobnostmi. Tyto výsledky však *nutně* nemusí být stejně pravděpodobné (i když termín "náhodná" může mít v jiných kontextech skutečně tento význam).

**Rovnoměrná proměnná** je speciální případ náhodné proměnné. Může nabývat dvou nebo více hodnot, všechny se stejnou pravděpodobností. Náhodná proměnná $X$ zobrazená na *Obrázku 1* je jasně rovnoměrná proměnná, protože oba možné výsledky se vyskytují s pravděpodobností $0.5$. Existuje však mnoho náhodných proměnných, které nejsou příklady rovnoměrných proměnných.

Zvažte například náhodnou proměnnou $Y$. Má množinu výsledků $\{1, 2, 3, 8, 10\}$ a následující pravděpodobnostní rozdělení:

$$
\Pr[Y = 1] = 0.25
$$

$$
\Pr[Y = 2] = 0.35
$$

$$
\Pr[Y = 3] = 0.1
$$

$$
\Pr[Y = 8] = 0.25
$$

$$
\Pr[Y = 10] = 0.05
$$

Ačkoli dva možné výsledky mají skutečně stejnou pravděpodobnost výskytu, a to $1$ a $8$, $Y$ může také nabývat určitých hodnot s jinými pravděpodobnostmi než $0.25$ při vzorkování. Tedy, ačkoli je $Y$ skutečně náhodná proměnná, není to rovnoměrná proměnná.

Grafické znázornění $Y$ je poskytnuto na *Obrázku 2*.

*Obrázek 2: Náhodná proměnná Y*

![Obrázek 2: Náhodná proměnná Y.](assets/Figure2-2.webp "Obrázek 2: Náhodná proměnná Y")

Jako poslední příklad zvažte náhodnou proměnnou Z. Má množinu výsledků {1,3,7,11,12} a následující pravděpodobnostní rozdělení:

$$
\Pr[Z = 2] = 0.2
$$

$$
\Pr[Z = 3] = 0.2
$$

$$
\Pr[Z = 9] = 0.2
$$

$$
\Pr[Z = 11] = 0.2
$$

$$
\Pr[Z = 12] = 0.2
$$

Jak můžete vidět na *Obrázku 3*, náhodná proměnná Z je, na rozdíl od Y, rovnoměrná proměnná, protože všechny pravděpodobnosti pro možné hodnoty při vzorkování jsou stejné.

*Obrázek 3: Náhodná proměnná Z*
![Obrázek 3: Náhodná proměnná Z.](assets/Figure2-3.webp "Obrázek 3: Náhodná proměnná Z")

### Podmíněná pravděpodobnost

Předpokládejme, že Bob má v úmyslu rovnoměrně vybrat den z posledního kalendářního roku. Jakou bychom měli usuzovat pravděpodobnost, že vybraný den bude v létě?

Pokud si myslíme, že Bobův proces bude skutečně rovnoměrný, měli bychom usuzovat, že pravděpodobnost, že Bob vybere den v létě, je 1/4. To je **bezpodmínečná pravděpodobnost**, že náhodně vybraný den bude v létě.

Předpokládejme nyní, že místo rovnoměrného výběru kalendářního dne Bob vybírá pouze rovnoměrně z těch dnů, kdy byla teplota v poledne u Crystal Lake (New Jersey) 21 stupňů Celsia nebo vyšší. Vzhledem k této dodatečné informaci, jaký závěr můžeme učinit o pravděpodobnosti, že Bob vybere den v létě?

Měli bychom skutečně dospět k jinému závěru než dříve, i bez jakýchkoli dalších konkrétních informací (např. teplota v poledne každý den posledního kalendářního roku).

Vědě, že Crystal Lake je v New Jersey, bychom rozhodně neočekávali, že teplota v poledne bude 21 stupňů Celsia nebo vyšší v zimě. Místo toho je mnohem pravděpodobnější, že se jedná o teplý den na jaře nebo na podzim, nebo o den někde v létě. Proto, vědě, že teplota v poledne u Crystal Lake ve vybraný den byla 21 stupňů Celsia nebo vyšší, pravděpodobnost, že den vybraný Bobem bude v létě, se stává mnohem vyšší. To je **podmíněná pravděpodobnost**, že náhodně vybraný den bude v létě, za předpokladu, že teplota v poledne u Crystal Lake byla 21 stupňů Celsia nebo vyšší.

Na rozdíl od předchozího příkladu mohou být pravděpodobnosti dvou událostí také zcela nesouvisející. V tom případě říkáme, že jsou **nezávislé**.

Předpokládejme například, že určitá spravedlivá mince přistála na hlavě. Vzhledem k této skutečnosti, jaká je potom pravděpodobnost, že zítra bude pršet? Podmíněná pravděpodobnost v tomto případě by měla být stejná jako bezpodmínečná pravděpodobnost, že zítra bude pršet, protože hod mincí obecně nemá žádný vliv na počasí.

Pro zápis výroků o podmíněné pravděpodobnosti používáme symbol "|". Například pravděpodobnost události $A$ za předpokladu, že událost $B$ nastala, lze zapsat takto:

$$
Pr[A|B]
$$

Takže, když jsou dvě události, $A$ a $B$, nezávislé, pak:

$$
Pr[A|B] = Pr[A] \text{ a } Pr[B|A] = Pr[B]
$$

Podmínka pro nezávislost lze zjednodušit takto:

$$
Pr[A, B] = Pr[A] \cdot Pr[B]
$$

Klíčovým výsledkem v teorii pravděpodobnosti je známý jako **Bayesova věta**. Základně říká, že $Pr[A|B]$ lze přepsat následovně:

$$
Pr[A|B] = \frac{Pr[B|A] \cdot Pr[A]}{Pr[B]}
$$

Místo používání podmíněných pravděpodobností se specifickými událostmi můžeme také podívat na podmíněné pravděpodobnosti spojené se dvěma nebo více náhodnými proměnnými v sadě možných událostí. Předpokládejme dvě náhodné proměnné, $X$ a $Y$. Jakoukoli možnou hodnotu pro $X$ můžeme označit $x$ a jakoukoli možnou hodnotu pro $Y$ $y$. Můžeme říci, že dvě náhodné proměnné jsou nezávislé, pokud platí následující tvrzení:

$$
Pr[X = x, Y = y] = Pr[X = x] \cdot Pr[Y = y]
$$

pro všechna $x$ a $y$.

Pojďme být trochu více explicitní o tom, co toto tvrzení znamená.
Předpokládejme, že množiny výsledků pro $X$ a $Y$ jsou definovány následovně: **X** = $\{x_1, x_2, \ldots, x_i, \ldots, x_n\}$ a **Y** = $\{y_1, y_2, \ldots, y_i, \ldots, y_m\}$. (Je typické označovat množiny hodnot tučnými, velkými písmeny.)
Nyní předpokládejme, že vzorkujete $Y$ a pozorujete $y_1$. Výše uvedené tvrzení nám říká, že pravděpodobnost nyní získat $x_1$ vzorkováním $X$ je přesně stejná, jako kdybychom $y_1$ nikdy nepozorovali. To platí pro jakékoli $y_i$, které bychom mohli získat z našeho počátečního vzorkování $Y$. Nakonec to platí nejen pro $x_1$. Pro jakékoli $x_i$ není pravděpodobnost výskytu ovlivněna výsledkem vzorkování $Y$. To vše se také vztahuje na případ, kdy je nejprve vzorkováno $X$.

Ukončeme naši diskusi na mírně filozofičtějším bodu. V jakékoli reálné situaci je pravděpodobnost nějaké události vždy posuzována proti konkrétní sadě informací. Ve velmi přísném smyslu slova neexistuje žádná "bezpodmínečná pravděpodobnost".

Představte si například, že bych se vás zeptal na pravděpodobnost, že prasata budou létat do roku 2030. I když vám nedám žádné další informace, jasně víte hodně o světě, který může ovlivnit váš úsudek. Nikdy jste neviděli létající prasata. Víte, že většina lidí od nich nebude očekávat, že budou létat. Víte, že nejsou opravdu stavěna k létání. A tak dále.

Proto, když mluvíme o "bezpodmínečné pravděpodobnosti" nějaké události v reálném kontextu, tento termín může mít význam pouze pokud ho chápeme jako "pravděpodobnost bez jakýchkoli dalších explicitních informací". Jakékoli pochopení "podmíněné pravděpodobnosti" by pak mělo být vždy chápáno vzhledem k nějakému konkrétnímu kusu informace.

Mohl bych se vás například zeptat na pravděpodobnost, že prasata budou létat do roku 2030, po tom, co vám dám důkazy, že někteří kozli na Novém Zélandu se naučili létat po několika letech tréninku. V tomto případě pravděpodobně upravíte svůj úsudek o pravděpodobnosti, že prasata budou létat do roku 2030. Takže pravděpodobnost, že prasata budou létat do roku 2030, je podmíněna těmito důkazy o kozlech na Novém Zélandu.

## Operace modulo
<chapterId>709b34e5-b155-53d2-abbd-97d67e56db00</chapterId>

### Modulo

Nejzákladnější vyjádření s **operací modulo** má následující formu: $x \mod y$.

Proměnná $x$ se nazývá dělenec a proměnná $y$ dělitel. K provedení operace modulo s kladným dělencem a kladným dělitelem stačí určit zbytek po dělení.

Například, zvažte výraz $25 \mod 4$. Číslo 4 jde do čísla 25 celkem 6krát. Zbytek tohoto dělení je 1. Tedy $25 \mod 4$ se rovná 1. Podobným způsobem můžeme vyhodnotit níže uvedené výrazy:

* $29 \mod 30 = 29$ (jelikož 30 jde do 29 celkem 0krát a zbytek je 29)
* $42 \mod 2 = 0$ (jelikož 2 jde do 42 celkem 21krát a zbytek je 0)
* $12 \mod 5 = 2$ (protože 5 se vejde do 12 celkem 2krát a zbytek je 2)
* $20 \mod 8 = 4$ (protože 8 se vejde do 20 celkem 2krát a zbytek je 4)

Když je dělenec nebo dělitel záporný, mohou programovací jazyky zpracovávat operace modulo různě.

Určitě se setkáte s případy se záporným dělencem v kryptografii. V těchto případech je typický postup následující:

* Nejprve určete nejbližší hodnotu *menší nebo rovnou* dělenci, do které se dělitel vejde s nulovým zbytkem. Tuto hodnotu nazvěme $p$.
* Pokud je dělenec $x$, pak výsledek modulo operace je hodnota $x – p$.

Například, předpokládejme, že dělenec je $–20$ a dělitel 3. Nejbližší hodnota menší nebo rovná $–20$, do které se 3 dělí rovnoměrně, je $–21$. Hodnota $x – p$ v tomto případě je $–20 – (–21)$. To se rovná 1 a tedy $–20 \mod 3$ se rovná 1. Podobným způsobem můžeme vyhodnotit následující výrazy:

* $–8 \mod 5 = 2$
* $–19 \mod 16 = 13$
* $–14 \mod 6 = 4$

Pokud jde o zápis, obvykle uvidíte následující typy výrazů: $x = [y \mod z]$. Kvůli závorkám se operace modulo v tomto případě vztahuje pouze na pravou stranu výrazu. Pokud například $y$ se rovná 25 a $z$ se rovná 4, pak $x$ se vyhodnotí na 1.

Bez závorek se operace modulo vztahuje na *obě strany* výrazu. Předpokládejme například následující výraz: $x = y \mod z$. Pokud $y$ se rovná 25 a $z$ se rovná 4, pak vše, co víme, je, že $x \mod 4$ se vyhodnotí na 1. To je konzistentní s jakoukoliv hodnotou pro $x$ ze sady $\{\ldots,–7, –3, 1, 5, 9,\ldots\}$.

Obor matematiky, který zahrnuje operace modulo s čísly a výrazy, se nazývá **modulární aritmetika**. Můžete na tento obor myslet jako na aritmetiku pro případy, kdy číselná řada není nekonečně dlouhá. Ačkoliv se obvykle setkáváme s operacemi modulo pro (kladná) celá čísla v kryptografii, můžete také provádět operace modulo s jakýmikoli reálnými čísly.

### Caesarova šifra

Operace modulo se často setkává v kryptografii. Abychom to ilustrovali, pojďme se podívat na jedno z nejslavnějších historických šifrovacích schémat: Caesarovu šifru.

Nejprve ji definujme. Předpokládejme slovník *D*, který rovná všechna písmena anglické abecedy, v pořadí, s množinou čísel $\{0, 1, 2, \ldots, 25\}$. Předpokládejme prostor zpráv **M**. **Caesarova šifra** je poté šifrovací schéma definované následovně:

- Jednotně vyberte klíč $k$ z prostoru klíčů **K**, kde **K** = $\{0, 1, 2, \ldots, 25\}$ [1]
- Zašifrujte zprávu $m \in \mathbf{M}$ takto:
    - Rozdělte $m$ na jednotlivá písmena $m_0, m_1, \ldots, m_i, \ldots, m_l$
- Převeďte každé $m_i$ na číslo podle *D*
    - Pro každé $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Převeďte každé $c_i$ na písmeno podle *D*
    - Poté spojte $c_0, c_1, \ldots, c_l$ a získáte šifrový text $c$
- Dešifrování šifrového textu $c$ probíhá následovně:
    - Převeďte každé $c_i$ na číslo podle *D*
    - Pro každé $c_i$, $m_i = [(c_i – k) \mod 26]$
    - Převeďte každé $m_i$ na písmeno podle *D*
    - Poté spojte $m_0, m_1, \ldots, m_l$ a získáte původní zprávu $m$

Operátor modulo v posunové šifře zajišťuje, že písmena se "obalují", takže všechna písmena šifrového textu jsou definována. Pro ilustraci zvažte použití posunové šifry na slovo "DOG".

Předpokládejme, že jste jednotně vybrali klíč s hodnotou 17. Písmeno “O” odpovídá číslu 15. Bez operace modulo by součet tohoto čísla otevřeného textu s klíčem dosáhl čísla šifrového textu 32. Toto číslo šifrového textu by však nemohlo být převedeno na písmeno šifrového textu, protože anglická abeceda má pouze 26 písmen. Operace modulo zajišťuje, že číslo šifrového textu je ve skutečnosti 6 (výsledek $32 \mod 26$), což odpovídá písmenu šifrového textu “G”.

Celé šifrování slova “DOG” s hodnotou klíče 17 je následující:

* Zpráva = DOG = D,O,G = 3,15,6
* $c_0 = [(3 + 17) \mod 26] = [(20) \mod 26] = 20 = U$
* $c_1 = [(15 + 17) \mod 26] = [(32) \mod 26] = 6 = G$
* $c_2 = [(6 + 17) \mod 26] = [(23) \mod 26] = 23 = X$
* $c = UGX$

Každý může intuitivně pochopit, jak posunová šifra funguje, a pravděpodobně ji sám použít. Pro rozšíření vašich znalostí o kryptografii je však důležité začít se cítit pohodlně s formalizací, protože schémata budou mnohem složitější. Proto byly kroky pro posunovou šifru formalizovány.

**Poznámky:**

[1] Toto tvrzení můžeme definovat přesně, použitím terminologie z předchozí sekce. Nechť uniformní proměnná $K$ má $K$ jako svou množinu možných výsledků. Takže:

$$
Pr[K = 0] = \frac{1}{26}
$$

$$
Pr[K = 1] = \frac{1}{26}
$$

...a tak dále. Vzorek uniformní proměnné $K$ jednou, aby se získal konkrétní klíč.

## Operace XOR
<chapterId>22f185cc-c516-5b33-950b-0908f2f881fe</chapterId>

Veškerá počítačová data jsou zpracovávána, ukládána a přenášena v síti na úrovni bitů. Jakékoli kryptografické schémata, která jsou aplikována na počítačová data, také operují na úrovni bitů.

Předpokládejme například, že jste napsali e-mail do své e-mailové aplikace. Jakékoli šifrování, které aplikujete, se neděje přímo na znacích ASCII vašeho e-mailu. Místo toho je aplikováno na bitovou reprezentaci písmen a dalších symbolů ve vašem e-mailu.
Klíčovou matematickou operací, kterou je třeba pro moderní kryptografii rozumět, kromě operace modulo, je **XOR operace**, neboli operace "výhradní nebo". Tato operace bere jako vstupy dva bity a výstupem je další bit. XOR operace bude jednoduše označena jako "XOR". Vrací 0, pokud jsou oba bity stejné, a 1, pokud jsou oba bity různé. Níže můžete vidět čtyři možnosti. Symbol $\oplus$ reprezentuje "XOR":
* $0 \oplus 0 = 0$
* $0 \oplus 1 = 1$
* $1 \oplus 0 = 1$
* $1 \oplus 1 = 0$

Pro ilustraci předpokládejme, že máte zprávu $m_1$ (01111001) a zprávu $m_2$ (01011001). XOR operace těchto dvou zpráv je vidět níže.

* $m_1 \oplus m_2 = 01111001 \oplus 01011001 = 00100000$

Proces je přímočarý. Nejprve provedete XOR nejlevějších bitů $m_1$ a $m_2$. V tomto případě to je $0 \oplus 0 = 0$. Poté provedete XOR druhého páru bitů zleva. V tomto případě to je $1 \oplus 1 = 0$. Tento proces pokračujete, dokud nebudete mít provedenou XOR operaci na nejpravějších bitech.

Je snadné vidět, že XOR operace je komutativní, tedy že $m_1 \oplus m_2 = m_2 \oplus m_1$. Kromě toho je XOR operace také asociativní. To znamená, že $(m_1 \oplus m_2) \oplus m_3 = m_1 \oplus (m_2 \oplus m_3)$.

XOR operace na dvou řetězcích různých délek může mít různé interpretace v závislosti na kontextu. Zde se nebudeme zabývat žádnými XOR operacemi na řetězcích různých délek.

XOR operace je ekvivalentní se speciálním případem provádění operace modulo na součtu bitů, když je dělitel 2. Ekvivalenci můžete vidět v následujících výsledcích:

* $(0 + 0) \mod 2 = 0 \oplus 0 = 0$
* $(1 + 0) \mod 2 = 1 \oplus 0 = 1$
* $(0 + 1) \mod 2 = 0 \oplus 1 = 1$
* $(1 + 1) \mod 2 = 1 \oplus 1 = 0$

## Pseudonáhodnost
<chapterId>20463fc5-3e92-581f-a1b7-3151279bd95e</chapterId>

V naší diskusi o náhodných a rovnoměrných proměnných jsme učinili konkrétní rozdíl mezi "náhodným" a "rovnoměrným". Tento rozdíl se v praxi obvykle udržuje při popisu náhodných proměnných. Nicméně, v našem současném kontextu je třeba tento rozdíl opustit a "náhodný" a "rovnoměrný" se používají synonymně. Vysvětlím proč na konci této sekce.

Na začátek můžeme nazvat binární řetězec délky $n$ **náhodným** (nebo **rovnoměrným**), pokud byl výsledkem vzorkování rovnoměrné proměnné $S$, která dává každému binárnímu řetězci takové délky $n$ stejnou pravděpodobnost výběru.
Představme si například množinu všech binárních řetězců o délce 8: $\{0000\ 0000, 0000\ 0001, \ldots, 1111\ 1111\}$. (Je běžné psát 8-bitový řetězec ve dvou čtveřicích, každá se nazývá **nibble**.) Tuto množinu řetězců pojmenujme **$S_8$**.
Podle výše uvedené definice můžeme pak říci, že konkrétní binární řetězec o délce 8 je náhodný (nebo rovnoměrný), pokud byl výsledkem vzorkování rovnoměrné proměnné $S$, která dává každému řetězci v **$S_8$** stejnou pravděpodobnost výběru. Vzhledem k tomu, že množina **$S_8$** obsahuje $2^8$ prvků, musela by být pravděpodobnost výběru při vzorkování $1/2^8$ pro každý řetězec v množině.

Klíčovým aspektem náhodnosti binárního řetězce je, že je definován s odkazem na proces, kterým byl vybrán. Forma jakéhokoli konkrétního binárního řetězce sama o sobě tedy neodhaluje nic o jeho náhodnosti ve výběru.

Například mnoho lidí intuitivně má za to, že řetězec jako $1111\ 1111$ nemohl být vybrán náhodně. Ale to je zjevně nesprávné.

Definujeme-li rovnoměrnou proměnnou $S$ nad všemi binárními řetězci o délce 8, pravděpodobnost výběru $1111\ 1111$ z množiny **$S_8$** je stejná jako pravděpodobnost výběru řetězce jako $0111\ 0100$. Tedy nemůžete nic říci o náhodnosti řetězce, pouze analýzou samotného řetězce.

Můžeme také mluvit o náhodných řetězcích bez specifického omezení na binární řetězce. Mohli bychom například mluvit o náhodném hexadecimálním řetězci $AF\ 02\ 82$. V tomto případě by řetězec byl vybrán náhodně z množiny všech hexadecimálních řetězců o délce 6. To je ekvivalentní s náhodným výběrem binárního řetězce o délce 24, protože každá hexadecimální číslice reprezentuje 4 bity.

Typicky výraz „náhodný řetězec“, bez další specifikace, odkazuje na řetězec náhodně vybraný z množiny všech řetězců stejné délky. Takto jsem to výše popsal. Řetězec o délce $n$ může být samozřejmě také náhodně vybrán z jiné množiny. Například z takové, která zahrnuje pouze podmnožinu všech řetězců o délce $n$, nebo možná množinu, která zahrnuje řetězce různých délek. V těchto případech bychom ho však nenazývali „náhodný řetězec“, ale spíše „řetězec, který byl náhodně vybrán z nějaké množiny **S**“.

Klíčovým pojmem v kryptografii je pseudonáhodnost. **Pseudonáhodný řetězec** o délce $n$ se jeví *jako by* byl výsledkem vzorkování rovnoměrné proměnné $S$, která dává každému řetězci v **$S_n$** stejnou pravděpodobnost výběru. Ve skutečnosti je však řetězec výsledkem vzorkování rovnoměrné proměnné $S'$, která definuje pravděpodobnostní rozdělení – ne nutně s rovnými pravděpodobnostmi pro všechny možné výsledky – na podmnožině **$S_n$**. Klíčovým bodem zde je, že nikdo nemůže skutečně rozlišit mezi vzorky z $S$ a $S'$, i když jich vezmete mnoho.
Předpokládejme například náhodnou proměnnou $S$. Její množina výsledků je **$S_{256}$**, což je množina všech binárních řetězců o délce 256. Tato množina má $2^{256}$ prvků. Každý prvek má při výběru stejnou pravděpodobnost výběru, $1/2^{256}$.

Kromě toho předpokládejme náhodnou proměnnou $S'$. Její množina výsledků zahrnuje pouze $2^{128}$ binárních řetězců o délce 256. Má určité rozdělení pravděpodobnosti nad těmito řetězci, ale toto rozdělení není nutně rovnoměrné.

Předpokládejme, že jsem nyní vzal tisíce vzorků z $S$ a tisíce vzorků z $S'$ a dal vám obě sady výsledků. Řeknu vám, která sada výsledků je spojena s kterou náhodnou proměnnou. Poté vezmu vzorek z jedné ze dvou náhodných proměnných. Ale tentokrát vám neřeknu, ze které náhodné proměnné jsem vzorek vzal. Pokud by $S'$ bylo pseudonáhodné, pak myšlenka je, že vaše pravděpodobnost správného uhodnutí, ze které náhodné proměnné jsem vzorek vzal, je prakticky ne lepší než $1/2$.

Typicky je pseudonáhodný řetězec o délce $n$ vyroben náhodným výběrem řetězce velikosti $n – x$, kde $x$ je kladné celé číslo, a použitím ho jako vstupu pro expanzní algoritmus. Tento náhodný řetězec velikosti $n – x$ je známý jako **seed**.

Pseudonáhodné řetězce jsou klíčovým konceptem pro praktické použití kryptografie. Vezměme si například proudové šifry. U proudové šifry je náhodně vybraný klíč vložen do expanzního algoritmu, aby se vyprodukoval mnohem delší pseudonáhodný řetězec. Tento pseudonáhodný řetězec je pak kombinován s otevřeným textem prostřednictvím operace XOR, aby se vyprodukoval šifrový text.

Pokud bychom nebyli schopni vyprodukovat tento typ pseudonáhodného řetězce pro proudovou šifru, pak bychom potřebovali klíč, který je tak dlouhý jako zpráva pro její zabezpečení. To není ve většině případů velmi praktická možnost.

Pojem pseudonáhodnosti diskutovaný v této sekci může být definován formálněji. Také se rozšiřuje do dalších kontextů. Ale nemusíme se nyní do této diskuse ponořit. Vše, co opravdu potřebujete intuitivně pochopit pro mnoho aspektů kryptografie, je rozdíl mezi náhodným a pseudonáhodným řetězcem. [2]

Důvod pro opuštění rozlišení mezi „náhodným“ a „rovnoměrným“ v naší diskusi by nyní měl být také jasný. V praxi každý používá termín pseudonáhodný k označení řetězce, který vypadá **jako by** byl výsledkem výběru z rovnoměrné proměnné $S$. Přesně řečeno, měli bychom takový řetězec nazvat „pseudo-uniformní“, přejímajíc naše jazykové vyjádření z dřívějška. Jelikož termín „pseudo-uniformní“ je neohrabaný a nikdo ho nepoužívá, nebudeme ho zde zavádět pro jasnost. Místo toho prostě opustíme rozlišení mezi „náhodným“ a „rovnoměrným“ v současném kontextu.

**Poznámky**

[2] Pokud máte zájem o formálnější výklad těchto záležitostí, můžete konzultovat *Úvod do moderní kryptografie* od Katz a Lindella, zejména kapitolu 3.

# Matematické základy kryptografie 2
<partId>d7245cc9-bb6d-5403-b3d5-9c703d9a2f81</partId>

## Co je teorie čísel?
<chapterId>c0051c34-fd5d-539c-93e2-5c6dfd4c3355</chapterId>
Tato kapitola se zabývá pokročilejším tématem matematických základů kryptografie: teorií čísel. Ačkoliv je teorie čísel důležitá pro symetrickou kryptografii (jako například u Šifry Rijndael), je zvláště důležitá v kontextu asymetrické kryptografie.

Pokud se vám zdají detaily teorie čísel obtížné, doporučuji při prvním čtení zvolit vysokoúrovňový přístup. Vždy se k tomu můžete vrátit později.

___

**Teorii čísel** byste mohli charakterizovat jako studium vlastností celých čísel a matematických funkcí, které pracují s celými čísly.

Vezměte například, že jakákoli dvě čísla $a$ a $N$ jsou **nesoudělná** (nebo **vzájemně prvočísla**), pokud jejich největší společný dělitel je roven 1. Předpokládejme nyní konkrétní celé číslo $N$. Kolik celých čísel menších než $N$ je nesoudělných s $N$? Můžeme o odpovědích na tuto otázku činit obecná tvrzení? To jsou typické typy otázek, na které se teorie čísel snaží odpovědět.

Moderní teorie čísel využívá nástroje abstraktní algebry. Obor **abstraktní algebra** je subdisciplína matematiky, kde hlavními objekty analýzy jsou abstraktní objekty známé jako algebraické struktury. **Algebraická struktura** je soubor prvků spojených s jednou nebo více operacemi, které splňují určité axiomy. Prostřednictvím algebraických struktur mohou matematici získat vhled do konkrétních matematických problémů abstrahováním od jejich detailů.

Obor abstraktní algebry je někdy také nazýván moderní algebra. Můžete se také setkat s pojmem **abstraktní matematika** (nebo **čistá matematika**). Tento poslední termín není odkazem na abstraktní algebru, ale spíše znamená studium matematiky pro její vlastní hodnotu, a ne jen s ohledem na potenciální aplikace.

Sady z abstraktní algebry mohou zacházet s mnoha typy objektů, od transformací zachovávajících tvar na rovnostranném trojúhelníku po vzory na tapetách. Pro teorii čísel zvažujeme pouze sady prvků, které obsahují celá čísla nebo funkce pracující s celými čísly.

## Skupiny
<chapterId>3209b270-f9cd-5224-803e-0ed19fbf7826</chapterId>

Základním konceptem v matematice je sada prvků. Sada je obvykle označována závorkami s prvky oddělenými čárkami.

Například sada všech celých čísel je $\{…, -2, -1, 0, 1, 2, …\}$. Tři tečky zde znamenají, že určitý vzor pokračuje v konkrétním směru. Takže sada všech celých čísel také zahrnuje $3, 4, 5, 6$ a tak dále, stejně jako $-3, -4, -5, -6$ a tak dále. Tato sada všech celých čísel je typicky označována $\mathbb{Z}$.

Dalším příkladem sady je $\mathbb{Z} \mod 11$, neboli sada všech celých čísel modulo 11. Na rozdíl od celé sady $\mathbb{Z}$, tato sada obsahuje pouze konečný počet prvků, a to $\{0, 1, \ldots, 9, 10\}$.
Běžnou chybou je myslet si, že množina $\mathbb{Z} \mod 11$ je ve skutečnosti $\{-10, -9, \ldots, 0, \ldots, 9, 10\}$. To ale není pravda, vzhledem k tomu, jak jsme dříve definovali operaci modulo. Jakékoli záporné celé číslo redukované modulo 11 se promítne do množiny $\{0, 1, \ldots, 9, 10\}$. Například výraz $-2 \mod 11$ se promítne na $9$, zatímco výraz $-27 \mod 11$ se promítne na $5$.
Dalším základním konceptem v matematice je binární operace. To je jakákoli operace, která bere dva prvky a produkuje třetí. Například ze základní aritmetiky a algebry byste byli obeznámeni se čtyřmi základními binárními operacemi: sčítání, odčítání, násobení a dělení.

Tyto dva základní matematické koncepty, množiny a binární operace, se používají k definování pojmu grupa, což je nejzákladnější struktura v abstraktní algebře.

Konkrétně, předpokládejme nějakou binární operaci $\circ$. Kromě toho předpokládejme nějakou množinu prvků **S** vybavenou touto operací. Vše, co „vybaveno“ zde znamená, je, že operaci $\circ$ lze provést mezi jakýmikoli dvěma prvky v množině **S**.

Kombinace $\langle \mathbf{S}, \circ \rangle$ je pak **grupa**, pokud splňuje čtyři konkrétní podmínky, známé jako grupové axiomy.

1. Pro libovolné $a$ a $b$, které jsou prvky $\mathbf{S}$, je $a \circ b$ také prvkem $\mathbf{S}$. To je známé jako **podmínka uzávěru**.
2. Pro libovolné $a$, $b$ a $c$, které jsou prvky $\mathbf{S}$, platí, že $(a \circ b) \circ c = a \circ (b \circ c)$. To je známé jako **podmínka asociativity**.
3. V $\mathbf{S}$ existuje jedinečný prvek $e$, takový, že pro každý prvek $a$ v $\mathbf{S}$ platí následující rovnice: $e \circ a = a \circ e = a$. Jelikož existuje pouze jeden takový prvek $e$, nazývá se **neutrální prvek**. Tato podmínka je známá jako **podmínka identity**.
4. Pro každý prvek $a$ v $\mathbf{S}$ existuje prvek $b$ v $\mathbf{S}$, takový, že platí následující rovnice: $a \circ b = b \circ a = e$, kde $e$ je neutrální prvek. Prvek $b$ zde je známý jako **inverzní prvek**, a běžně se označuje jako $a^{-1}$. Tato podmínka je známá jako **podmínka inverze** nebo **podmínka invertibility**.

Pojďme se podívat na grupy trochu blíže. Označme množinu všech celých čísel jako $\mathbb{Z}$. Tato množina kombinovaná se standardním sčítáním, nebo $\langle \mathbb{Z}, + \rangle$, jasně vyhovuje definici grupy, protože splňuje všechny čtyři výše uvedené axiomy.

1. Pro libovolné $x$ a $y$, které jsou prvky $\mathbb{Z}$, je $x + y$ také prvkem $\mathbb{Z}$. Takže $\langle \mathbb{Z}, + \rangle$ splňuje podmínku uzávěru.
2. Pro libovolné $x$, $y$ a $z$, které jsou prvky množiny $\mathbb{Z}$, platí $(x + y) + z = x + (y + z)$. Takže $\langle \mathbb{Z}, + \rangle$ splňuje podmínku asociativity.
3. V $\langle \mathbb{Z}, + \rangle$ existuje neutrální prvek, konkrétně 0. Pro libovolné $x$ v $\mathbb{Z}$ platí: $0 + x = x + 0 = x$. Takže $\langle \mathbb{Z}, + \rangle$ splňuje podmínku existence neutrálního prvku.
4. Nakonec, pro každý prvek $x$ v $\mathbb{Z}$ existuje $y$ tak, že $x + y = y + x = 0$. Pokud by například $x$ bylo 10, $y$ by bylo $-10$ (v případě, že $x$ je 0, $y$ je také 0). Takže $\langle \mathbb{Z}, + \rangle$ splňuje podmínku existence inverzního prvku.

Je důležité si uvědomit, že skutečnost, že množina celých čísel s operací sčítání tvoří grupu, neznamená, že by tvořila grupu s operací násobení. To můžete ověřit testováním $\langle \mathbb{Z}, \cdot \rangle$ proti čtyřem axiomům grupy (kde $\cdot$ znamená standardní násobení).

První dva axiomy jsou zřejmě splněny. Navíc, při násobení může prvek 1 sloužit jako neutrální prvek. Jakékoli celé číslo $x$ vynásobené jedničkou dává výsledek $x$. Nicméně, $\langle \mathbb{Z}, \cdot \rangle$ nesplňuje podmínku existence inverzního prvku. To znamená, že neexistuje unikátní prvek $y$ v $\mathbb{Z}$ pro každé $x$ v $\mathbb{Z}$, tak aby $x \cdot y = 1$.

Představme si například, že $x = 22$. Jakou hodnotu $y$ z množiny $\mathbb{Z}$, vynásobenou s $x$, bychom dostali neutrální prvek 1? Hodnota $1/22$ by fungovala, ale není to prvek množiny $\mathbb{Z}$. Ve skutečnosti se s tímto problémem setkáte u jakéhokoli celého čísla $x$, kromě hodnot 1 a -1 (kde by $y$ muselo být 1 a -1).

Pokud bychom do naší množiny zařadili reálná čísla, naše problémy by se do značné míry vyřešily. Pro jakýkoli prvek $x$ v množině dá násobení $1/x$ výsledek 1. Jelikož zlomky jsou zahrnuty v množině reálných čísel, pro každé reálné číslo lze najít inverzi. Výjimkou je nula, protože jakékoli násobení s nulou nikdy nedá neutrální prvek 1. Tedy množina nenulových reálných čísel vybavená násobením skutečně tvoří grupu.

Některé grupy splňují pátou obecnou podmínku, známou jako **podmínka komutativity**. Tato podmínka je následující:

* Předpokládejme grupu $G$ s množinou **S** a binárním operátorem $\circ$. Předpokládejme, že $a$ a $b$ jsou prvky **S**. Pokud platí, že $a \circ b = b \circ a$ pro jakékoli dva prvky $a$ a $b$ v **S**, pak $G$ splňuje podmínku komutativity.
Každá skupina, která splňuje podmínku komutativity, je známá jako **komutativní skupina** nebo **Abelova skupina** (po Nielsu Henrikovi Abelovi). Je snadné ověřit, že množina reálných čísel vzhledem k sčítání a množina celých čísel vzhledem k sčítání jsou Abelovy skupiny. Množina celých čísel vzhledem k násobení vůbec není skupinou, a tedy nemůže být Abelovou skupinou. Naopak, množina nenulových reálných čísel vzhledem k násobení je také Abelovou skupinou.
Měli byste dbát na dvě důležité konvence v notaci. První, znaménka "+" nebo "×" budou často používána k symbolizaci operací skupiny, i když prvky ve skutečnosti nejsou čísla. V těchto případech byste neměli tyto znaky interpretovat jako standardní aritmetické sčítání nebo násobení. Místo toho jsou to operace s pouze abstraktní podobností s těmito aritmetickými operacemi.

Pokud konkrétně nemluvíte o aritmetickém sčítání nebo násobení, je jednodušší používat symboly jako $\circ$ a $\diamond$ pro operace skupin, protože tyto nemají silně kulturně zakořeněné konotace.

Druhá, z téhož důvodu, proč jsou "+" a "×" často používány pro označení ne-aritmetických operací, jsou neutrální prvky skupin často symbolizovány "0" a "1", i když prvky v těchto skupinách nejsou čísla. Pokud nemluvíte o neutrálním prvku skupiny s čísly, je jednodušší použít neutrálnější symbol jako "$e$" k označení neutrálního prvku.

Mnoho různých a velmi důležitých množin hodnot v matematice vybavených určitými binárními operacemi jsou skupiny. Kryptografické aplikace však pracují pouze s množinami celých čísel nebo alespoň s prvky, které jsou popsány celými čísly, to znamená, v rámci oboru teorie čísel. Proto množiny s reálnými čísly jinými než celá čísla nejsou v kryptografických aplikacích používány.

Ukončeme tím, že poskytneme příklad prvků, které mohou být "popisovány celými čísly", i když nejsou celými čísly. Dobrým příkladem jsou body na eliptických křivkách. Ačkoli žádný bod na eliptické křivce zřejmě není celé číslo, takový bod je skutečně popsán dvěma celými čísly.

Eliptické křivky jsou například zásadní pro Bitcoin. Jakýkoli standardní soukromý a veřejný klíč Bitcoinu je vybrán z množiny bodů, která je definována následující eliptickou křivkou:

$$
x^3 + 7 = y^2 \mod 2^{256} – 2^{32} – 29 – 28 – 27 – 26 - 24 - 1
$$

(největší prvočíslo menší než $2^{256}$). Souřadnice $x$ je soukromý klíč a souřadnice $y$ je váš veřejný klíč.

Transakce v Bitcoinu typicky zahrnují uzamčení výstupů na jednom nebo více veřejných klíčích nějakým způsobem. Hodnota z těchto transakcí může být poté odemčena vytvořením digitálních podpisů s odpovídajícími soukromými klíči.

## Cyklické skupiny
<chapterId>bfa5c714-7952-5fef-88b1-ca5b07edd886</chapterId>

Důležitým rozlišením, které můžeme učinit, je mezi **konečnou** a **nekonečnou skupinou**. První má konečný počet prvků, zatímco druhá má nekonečný počet prvků. Počet prvků v jakékoli konečné skupině je známý jako **řád skupiny**. Veškerá praktická kryptografie, která zahrnuje použití skupin, se spoléhá na konečné (číselně-teoretické) skupiny.

V rámci kryptografie s veřejným klíčem je určitá třída konečných Abelových skupin známá jako cyklické skupiny obzvláště důležitá. Abychom porozuměli cyklickým skupinám, musíme nejprve pochopit koncept exponentiace prvků skupiny.
Předpokládejme skupinu $G$ s operací skupiny $\circ$, a že $a$ je prvkem skupiny $G$. Výraz $a^n$ by pak měl být interpretován jako prvek $a$ kombinovaný sám se sebou celkem $n – 1$ krát. Například, $a^2$ znamená $a \circ a$, $a^3$ znamená $a \circ a \circ a$ a tak dále. (Poznamenejme, že zde exponentiace není nutně exponentiací ve standardním aritmetickém smyslu.)
Pojďme se podívat na příklad. Předpokládejme, že $G = \langle \mathbb{Z} \mod 7, + \rangle$, a že naše hodnota pro $a$ se rovná 4. V tomto případě, $a^2 = [4 + 4 \mod 7] = [8 \mod 7] = 1 \mod 7$. Alternativně, $a^4$ by reprezentovalo $[4 + 4 + 4 + 4 \mod 7] = [16 \mod 7] = 2 \mod 7$.

Některé abelovské skupiny mají jeden nebo více prvků, které mohou generovat všechny ostatní prvky skupiny prostřednictvím pokračující exponentiace. Tyto prvky se nazývají **generátory** nebo **primitivní prvky**.

Důležitou třídou takových skupin je $\langle \mathbb{Z}^* \mod N, \cdot \rangle$, kde $N$ je prvočíslo. Notace $\mathbb{Z}^*$ zde znamená, že skupina obsahuje všechna nenulová, kladná celá čísla menší než $N$. Taková skupina má tedy vždy $N – 1$ prvků.

Vezměme si například $G = \langle \mathbb{Z}^* \mod 11, \cdot \rangle$. Tato skupina má následující prvky: $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$. Řád této skupiny je 10 (což je skutečně rovno $11 – 1$).

Pojďme prozkoumat exponentiaci prvku 2 z této skupiny. Výpočty až do $2^{12}$ jsou uvedeny níže. Všimněte si, že na levé straně rovnice exponent odkazuje na exponentiaci prvku skupiny. V našem konkrétním příkladu to skutečně zahrnuje aritmetickou exponentiaci na pravé straně rovnice (ale mohlo by to také zahrnovat, například, sčítání). Pro zřetelnost jsem vypsala opakovanou operaci, spíše než formu s exponentem na pravé straně.

* $2^1 = 2 \mod 11$
* $2^2 = 2 \cdot 2 \mod 11 = 4 \mod 11$
* $2^3 = 2 \cdot 2 \cdot 2 \mod 11 = 8 \mod 11$
* $2^4 = 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 16 \mod 11 = 5 \mod 11$
* $2^5 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 32 \mod 11 = 10 \mod 11$
* $2^6 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 64 \mod 11 = 9 \mod 11$
* $2^7 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 128 \mod 11 = 7 \mod 11$
* $2^8 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 256 \mod 11 = 3 \mod 11$
* $2^9 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 512 \mod 11 = 6 \mod 11$
* $2^{10} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 1024 \mod 11 = 1 \mod 11$
* $2^{11} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 2048 \mod 11 = 2 \mod 11$
* $2^{12} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 4096 \mod 11 = 4 \mod 11$

Pokud se pozorně podíváte, můžete vidět, že provádění umocňování na prvku 2 prochází všemi prvky $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ v následujícím pořadí: 2, 4, 8, 5, 10, 9, 7, 3, 6, 1. Po $2^{10}$, pokračující umocňování prvku 2 prochází všemi prvky znovu a ve stejném pořadí. Tedy prvek 2 je generátor v $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$.

Ačkoliv $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ má více generátorů, ne všechny prvky této skupiny jsou generátory. Vezměme si například prvek 3. Procházení prvními 10 umocněními, bez zobrazování zdlouhavých výpočtů, přináší následující výsledky:

* $3^1 = 3 \mod 11$
* $3^2 = 9 \mod 11$
* $3^3 = 5 \mod 11$
* $3^4 = 4 \mod 11$
* $3^5 = 1 \mod 11$
* $3^6 = 3 \mod 11$
* $3^7 = 9 \mod 11$
* $3^8 = 5 \mod 11$
* $3^9 = 4 \mod 11$
* $3^{10} = 1 \mod 11$
Místo procházení všech hodnot v $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, exponentiace prvku 3 vede pouze k podmnožině těchto hodnot: 3, 9, 5, 4 a 1. Po páté exponentiaci se tyto hodnoty začnou opakovat.
Nyní můžeme definovat **cyklickou grupu** jako jakoukoli grupu s alespoň jedním generátorem. To znamená, že existuje alespoň jeden prvek grupy, z něhož můžete prostřednictvím exponentiace vyprodukovat všechny ostatní prvky grupy.

Možná jste si v našem příkladu výše všimli, že jak $2^{10}$, tak $3^{10}$ se rovnají $1 \mod 11$. Ve skutečnosti, ačkoli výpočty provádět nebudeme, exponentiace čísla 10 jakéhokoli prvku v grupě $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ vždy vyústí v $1 \mod 11$. Proč je tomu tak?

To je důležitá otázka, ale její zodpovězení vyžaduje určité úsilí.

Začněme s předpokladem dvou kladných celých čísel $a$ a $N$. Důležitá věta v teorii čísel uvádí, že $a$ má multiplikativní inverzi modulo $N$ (to znamená celé číslo $b$ tak, že $a \cdot b = 1 \mod N$) právě tehdy, když největší společný dělitel mezi $a$ a $N$ se rovná 1. To znamená, pokud jsou $a$ a $N$ nesoudělná.

Takže pro jakoukoli grupu celých čísel vybavenou násobením modulo $N$ jsou v množině zahrnuta pouze menší nesoudělná čísla s $N$. Tuto množinu můžeme označit jako $\mathbb{Z}^c \mod N$.

Předpokládejme například, že $N$ je 10. Pouze celá čísla 1, 3, 7 a 9 jsou nesoudělná s 10. Takže sada $\mathbb{Z}^c \mod 10$ zahrnuje pouze $\{1, 3, 7, 9\}$. Nemůžete vytvořit grupu s celočíselným násobením modulo 10 použitím jakýchkoli jiných celých čísel mezi 1 a 10. Pro tuto konkrétní grupu jsou inverze páry 1 a 9, a 3 a 7.

V případě, kdy je $N$ samo prvočíslo, jsou všechna celá čísla od 1 do $N – 1$ nesoudělná s $N$. Taková grupa má tedy řád $N – 1$. Používáme-li naše dřívější označení, $\mathbb{Z}^c \mod N$ se rovná $\mathbb{Z}^* \mod N$, když je $N$ prvočíslo. Grupa, kterou jsme si pro náš dřívější příklad vybrali, $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, je konkrétním příkladem této třídy grup.

Dále, funkce $\phi(N)$ vypočítává počet nesoudělných čísel až do čísla $N$ a je známá jako **Eulerova funkce Phi**. [1] Podle **Eulerovy věty**, kdykoli jsou dvě celá čísla $a$ a $N$ nesoudělná, platí následující:

* $a^{\phi(N)} \mod N = 1 \mod N$
Toto má důležitý význam pro třídu grup $\langle \mathbb{Z}^* \mod N, \cdot \rangle$, kde $N$ je prvočíslo. Pro tyto grupy reprezentuje exponentiace prvků grupy aritmetickou exponentiaci. To znamená, že $a^{\phi(N)} \mod N$ reprezentuje aritmetickou operaci $a^{\phi(N)} \mod N$. Jelikož každý prvek $a$ v těchto multiplikativních grupách je nesoudělný s $N$, znamená to, že $a^{\phi(N)} \mod N = a^{N – 1} \mod N = 1 \mod N$.
Eulerova věta je opravdu důležitý výsledek. Na začátek to znamená, že všechny prvky v $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ mohou cyklovat pouze skrz určitý počet hodnot exponentiací, který se dělí do $N – 1$. V případě $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ to znamená, že každý prvek může cyklovat pouze skrz 2, 5, nebo 10 prvků. Hodnoty grupy, skrz které jakýkoliv prvek cykluje při exponentiaci, se nazývají **řád prvku**. Prvek s řádem ekvivalentním řádu grupy je generátor.

Dále Eulerova věta naznačuje, že vždy můžeme znát výsledek $a^{N – 1} \mod N$ pro jakoukoliv grupu $\langle \mathbb{Z}^* \mod N, \cdot \rangle$, kde $N$ je prvočíslo. To platí bez ohledu na to, jak složité mohou být skutečné výpočty.

Například, předpokládejme, že naše grupa je $\mathbb{Z}^* \mod 160,481,182$ (kde 160,481,182 je skutečně prvočíslo). Víme, že všechna celá čísla od 1 do 160,481,181 musí být prvky této grupy, a že $\phi(n) = 160,481,181$. I když nemůžeme provést všechny kroky výpočtů, víme, že výrazy jako $514^{160,481,181}$, $2,005^{160,481,181}$ a $256,212^{160,481,181}$ musí všechny vyhodnotit na $1 \mod 160,481,182$.

**Poznámky:**

[1] Funkce funguje následovně. Jakékoliv celé číslo $N$ lze rozložit na součin prvočísel. Předpokládejme, že určité $N$ je rozloženo následovně: $p_1^{e1} \cdot p_2^{e2} \cdot \ldots \cdot p_m^{em}$, kde všechna $p$ jsou prvočísla a všechna $e$ jsou celá čísla větší nebo rovna 1. Potom:

$$
\phi(N) = \sum_{i=1}^m \left[p_i^{e_i} - p_i^{e_i - 1}\right]
$$

Eulerův Phi funkční vzorec pro prvočíselný rozklad $N$.


## Fields
<chapterId>fad52d86-3a22-5c9f-979e-3bec9eaa008e</chapterId>

Grupa je základní algebraická struktura v abstraktní algebře, ale existuje jich mnohem více. Jedinou další algebraickou strukturou, se kterou byste měli být obeznámeni, je **pole**, konkrétně **konečné pole**. Tento typ algebraické struktury se často používá v kryptografii, jako je například v pokročilém šifrovacím standardu. Ten je hlavním symetrickým šifrovacím schématem, se kterým se v praxi setkáte.
Pole je odvozeno z pojmu skupina. Konkrétně, **pole** je množina prvků **S** vybavená dvěma binárními operátory $\circ$ a $\diamond$, která splňuje následující podmínky:
1. Množina **S** vybavená $\circ$ je Abelova skupina.
2. Množina **S** vybavená $\diamond$ je Abelova skupina pro "nenulové" prvky.
3. Množina **S** vybavená oběma operátory splňuje tzv. distributivní podmínku: Předpokládejme, že $a$, $b$ a $c$ jsou prvky **S**. Potom **S** vybavená oběma operátory splňuje distributivní vlastnost, když $a \circ (b \diamond c) = (a \circ b) \diamond (a \circ c)$.

Poznamenejme, že stejně jako u skupin, definice pole je velmi abstraktní. Nečiní žádné tvrzení o typech prvků v **S**, ani o operacích $\circ$ a $\diamond$. Pouze uvádí, že pole je jakákoli množina prvků s dvěma operacemi, pro které platí tři výše uvedené podmínky. (Prvek "nula" ve druhé Abelově skupině může být abstraktně interpretován.)

Tak jaký by mohl být příklad pole? Dobrým příkladem je množina $\mathbb{Z} \mod 7$, nebo $\{0, 1, \ldots, 7\}$ definovaná nad standardním sčítáním (místo $\circ$ výše) a standardním násobením (místo $\diamond$ výše).

Za prvé, $\mathbb{Z} \mod 7$ splňuje podmínku pro být Abelovou skupinou nad sčítáním, a splňuje podmínku pro být Abelovou skupinou nad násobením, pokud uvažujete pouze nenulové prvky. Za druhé, kombinace množiny s oběma operátory splňuje distributivní podmínku.

Je didakticky užitečné prozkoumat tyto tvrzení pomocí některých konkrétních hodnot. Vezměme experimentální hodnoty 5, 2 a 3, některé náhodně vybrané prvky z množiny $\mathbb{Z} \mod 7$, abychom prozkoumali pole $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$. Tyto tři hodnoty použijeme v pořadí, jak je potřeba prozkoumat konkrétní podmínky.

Pojďme nejprve prozkoumat, zda $\mathbb{Z} \mod 7$ vybavená sčítáním je Abelovou skupinou.

1. **Podmínka uzavřenosti**: Vezměme 5 a 2 jako naše hodnoty. V tom případě, $[5 + 2] \mod 7 = 7 \mod 7 = 0$. To je skutečně prvek $\mathbb{Z} \mod 7$, takže výsledek je v souladu s podmínkou uzavřenosti.
2. **Podmínka asociativity**: Vezměme 5, 2 a 3 jako naše hodnoty. V tom případě, $[(5 + 2) + 3] \mod 7 = [5 + (2 + 3)] \mod 7 = 10 \mod 7 = 3$. To je v souladu s podmínkou asociativity.
3. **Podmínka identity**: Vezměme 5 jako naši hodnotu. V tom případě, $[5 + 0] \mod 7 = [0 + 5] \mod 7 = 5$. Takže 0 vypadá, že je identitní prvek pro sčítání.
4. **Podmínka inverze**: Zvažme inverzi čísla 5. Musí platit, že $[5 + d] \mod 7 = 0$ pro nějakou hodnotu $d$. V tomto případě je jedinečná hodnota z $\mathbb{Z} \mod 7$, která splňuje tuto podmínku, 2,5. **Podmínka komutativity**: Vezměme si hodnoty 5 a 3. V tom případě $[5 + 3] \mod 7 = [3 + 5] \mod 7 = 1$. To je v souladu s podmínkou komutativity.

Množina $\mathbb{Z} \mod 7$ vybavená sčítáním se zjevně jeví jako Abelova grupa. Nyní prozkoumejme, zda je $\mathbb{Z} \mod 7$ vybavená násobením Abelovou grupou pro všechny nenulové prvky.

1. **Podmínka uzavřenosti**: Vezměme si hodnoty 5 a 2. V tom případě $[5 \cdot 2] \mod 7 = 10 \mod 7 = 3$. To je také prvek množiny $\mathbb{Z} \mod 7$, takže výsledek je v souladu s podmínkou uzavřenosti.
2. **Podmínka asociativity**: Vezměme si hodnoty 5, 2 a 3. V tom případě $[(5 \cdot 2) \cdot 3] \mod 7 = [5 \cdot (2 \cdot 3)] \mod 7 = 30 \mod 7 = 2$. To je v souladu s podmínkou asociativity.
3. **Podmínka identity**: Vezměme si hodnotu 5. V tom případě $[5 \cdot 1] \mod 7 = [1 \cdot 5] \mod 7 = 5$. Takže 1 se jeví jako neutrální prvek pro násobení.
4. **Podmínka inverze**: Zvažme inverzi čísla 5. Musí platit, že $[5 \cdot d] \mod 7 = 1$ pro nějakou hodnotu $d$. Jedinečná hodnota z $\mathbb{Z} \mod 7$, která splňuje tuto podmínku, je 3. To je v souladu s podmínkou inverze.
5. **Podmínka komutativity**: Vezměme si hodnoty 5 a 3. V tom případě $[5 \cdot 3] \mod 7 = [3 \cdot 5] \mod 7 = 15 \mod 7 = 1$. To je v souladu s podmínkou komutativity.

Množina $\mathbb{Z} \mod 7$ se zjevně jeví, že splňuje pravidla pro být Abelovou grupou, když je spojena buď se sčítáním nebo násobením nad nenulovými prvky.

Nakonec se zdá, že tato množina kombinovaná s oběma operátory splňuje distributivní podmínku. Vezměme si hodnoty 5, 2 a 3. Vidíme, že $[5 \cdot (2 + 3)] \mod 7 = [5 \cdot 2 + 5 \cdot 3] \mod 7 = 25 \mod 7 = 4$.

Nyní jsme viděli, že $\mathbb{Z} \mod 7$ vybavená sčítáním a násobením splňuje axiomy pro konečné pole při testování s konkrétními hodnotami. Samozřejmě to můžeme ukázat i obecně, ale zde to nebudeme dělat.

Klíčovým rozlišením je mezi dvěma typy polí: konečná a nekonečná pole.
**Nekonečné pole** zahrnuje pole, kde množina **S** je nekonečně velká. Množina reálných čísel $\mathbb{R}$ vybavená sčítáním a násobením je příkladem nekonečného pole. **Konečné pole**, známé také jako **Galoisovo pole**, je pole, kde množina **S** je konečná. Náš výše uvedený příklad $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$ je konečné pole.
V kryptografii máme primární zájem o konečná pole. Obecně lze ukázat, že konečné pole existuje pro nějakou množinu prvků **S** právě tehdy, pokud má $p^m$ prvků, kde $p$ je prvočíslo a $m$ kladné celé číslo větší nebo rovno jedné. Jinými slovy, pokud řád nějaké množiny **S** je prvočíslo ($p^m$ kde $m = 1$) nebo nějaká mocnina prvočísla ($p^m$ kde $m > 1$), pak můžete najít dva operátory $\circ$ a $\diamond$ tak, že jsou splněny podmínky pro pole.

Pokud nějaké konečné pole má prvočíselný počet prvků, pak se nazývá **prvočíselné pole**. Pokud počet prvků v konečném poli je mocnina prvočísla, pak se pole nazývá **rozšířené pole**. V kryptografii máme zájem o oba typy, prvočíselná i rozšířená pole. [2]

Hlavní prvočíselná pole zájmu v kryptografii jsou ta, kde množina všech celých čísel je modulována nějakým prvočíslem a operátory jsou standardní sčítání a násobení. Tato třída konečných polí by zahrnovala $\mathbb{Z} \mod 2$, $\mathbb{Z} \mod 3$, $\mathbb{Z} \mod 5$, $\mathbb{Z} \mod 7$, $\mathbb{Z} \mod 11$, $\mathbb{Z} \mod 13$, a tak dále. Pro jakékoli prvočíselné pole $\mathbb{Z} \mod p$ je množina celých čísel pole následující: $\{0, 1, \ldots, p – 2, p – 1\}$.

V kryptografii máme také zájem o rozšířená pole, zejména o pole s $2^m$ prvky, kde $m > 1$. Taková konečná pole jsou například používána v šifře Rijndael, která tvoří základ Advanced Encryption Standard. Zatímco prvočíselná pole jsou relativně intuitivní, tato rozšířená pole na bázi 2 pravděpodobně nebudou pro někoho, kdo není obeznámen s abstraktní algebrou.

Začneme tím, že je skutečně pravda, že jakákoli množina celých čísel s $2^m$ prvky může být přiřazena dvěma operátorům, které by jejich kombinaci učinily polem (pokud je $m$ kladné celé číslo). Nicméně, jen protože pole existuje, neznamená nutně, že je snadné jej objevit nebo že je zvláště praktické pro určité aplikace.

Ukazuje se, že zvláště aplikovatelná rozšířená pole $2^m$ v kryptografii jsou ta, která jsou definována nad konkrétními množinami polynomických výrazů, spíše než nějakou množinou celých čísel.

Předpokládejme například, že bychom chtěli rozšířené pole s $2^3$ (tj. 8) prvky v množině. Zatímco by mohlo existovat mnoho různých množin, které by mohly být použity pro pole této velikosti, jedna taková množina zahrnuje všechny unikátní polynomy ve formě $a_2x^2 + a_1x + a_0$, kde každý koeficient $a_i$ je buď 0 nebo 1. Tedy, tato množina **S** zahrnuje následující prvky:
1. $0$: Případ, kdy $a_2 = 0$, $a_1 = 0$ a $a_0 = 0$.
2. $1$: Případ, kdy $a_2 = 0$, $a_1 = 0$ a $a_0 = 1$.
3. $x$: Případ, kdy $a_2 = 0$, $a_1 = 1$ a $a_0 = 0$.
4. $x + 1$: Případ, kdy $a_2 = 0$, $a_1 = 1$ a $a_0 = 1$.
5. $x^2$: Případ, kdy $a_2 = 1$, $a_1 = 0$ a $a_0 = 0$.
6. $x^2 + 1$: Případ, kdy $a_2 = 1$, $a_1 = 0$ a $a_0 = 1$.
7. $x^2 + x$: Případ, kdy $a_2 = 1$, $a_1 = 1$ a $a_0 = 0$.
8. $x^2 + x + 1$: Případ, kdy $a_2 = 1$, $a_1 = 1$ a $a_0 = 1$.

Takže **S** bude množina $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$. Jaké dvě operace mohou být definovány nad touto množinou prvků, aby jejich kombinace tvořila těleso?

První operace na množině **S** ($\circ$) může být definována jako standardní sčítání polynomů modulo 2. Stačí sčítat polynomy, jak byste to obvykle dělali, a poté aplikovat modulo 2 na každý z koeficientů výsledného polynomu. Zde jsou některé příklady:

* $[(x^2) + (x^2 + x + 1)] \mod 2 = [2x^2 + x + 1] \mod 2 = x + 1$
* $[(x^2 + x) + (x)] \mod 2 = [x^2 + 2x] \mod 2 = x^2$
* $[(x + 1) + (x^2 + x + 1)] \mod 2 = [x^2 + 2x + 2] \mod 2 = x^2 + 1$

Druhá operace na množině **S** ($\diamond$), která je potřebná pro vytvoření tělesa, je složitější. Jedná se o druh násobení, ale ne o standardní násobení z aritmetiky. Místo toho musíte každý prvek vidět jako vektor a operaci chápat jako násobení těchto dvou vektorů modulo neredukovatelný polynom.

Pojďme se nejprve obrátit k pojmu neredukovatelný polynom. **Neredukovatelný polynom** je takový, který nelze faktorizovat (stejně jako prvočíslo nelze faktorizovat na složky jiné než 1 a samotné prvočíslo). Pro naše účely máme zájem o polynomy, které jsou neredukovatelné vzhledem k množině všech celých čísel. (Poznamenejme, že určité polynomy můžete být schopni faktorizovat například pomocí reálných nebo komplexních čísel, i když je nemůžete faktorizovat použitím celých čísel.)
Například vezměme polynom $x^2 - 3x + 2$. Tento lze přepsat jako $(x – 1)(x – 2)$. Tedy, není neredukovatelný. Nyní zvažme polynom $x^2 + 1$. Používajíc pouze celá čísla, není možné tento výraz dále faktorizovat. Tedy, toto je neredukovatelný polynom vzhledem k celým číslům.
Dále se podívejme na koncept násobení vektorů. Toto téma nebudeme prozkoumávat do hloubky, ale stačí, když pochopíte základní pravidlo: Jakékoli dělení vektorů může proběhnout, pokud má dělenec vyšší nebo rovný stupeň než dělitel. Pokud má dělenec nižší stupeň než dělitel, pak dělenec již nemůže být dělitel dělen.

Například zvažme výraz $x^6 + x + 1 \mod x^5 + x^2$. Tento se jasně dále redukuje, protože stupeň dělence, 6, je vyšší než stupeň dělitele, 5. Nyní zvažme výraz $x^5 + x + 1 \mod x^5 + x^2$. Tento také redukuje dále, protože stupeň dělence, 5, a dělitele, 5, jsou stejné.

Nicméně, nyní zvažme výraz $x^4 + x + 1 \mod x^5 + x^2$. Tento se již dále neredukuje, protože stupeň dělence, 4, je nižší než stupeň dělitele, 5.

Na základě těchto informací jsme nyní připraveni najít naši druhou operaci pro množinu $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.

Již jsem řekl, že druhá operace by měla být chápána jako vektorové násobení modulo nějaký neredukovatelný polynom. Tento neredukovatelný polynom by měl zajistit, že druhá operace definuje Abelovu grupu nad **S** a je v souladu s distributivním zákonem. Jaký by tedy měl být tento neredukovatelný polynom?

Vzhledem k tomu, že všechny vektory v množině mají stupeň 2 nebo nižší, měl by být neredukovatelný polynom stupně 3. Pokud jakékoli násobení dvou vektorů v množině vede k polynomu stupně 3 nebo vyššího, víme, že modulo polynom stupně 3 vždy vede k polynomu stupně 2 nebo nižšímu. To je proto, že jakýkoli polynom stupně 3 nebo vyššího je vždy dělitelný polynomem stupně 3. Kromě toho musí polynom, který funguje jako dělitel, být neredukovatelný.

Ukazuje se, že existuje několik neredukovatelných polynomů stupně 3, které bychom mohli použít jako náš dělitel. Každý z těchto polynomů definuje v kombinaci s naší množinou **S** a sčítáním modulo 2 různé pole. To znamená, že máte několik možností, když používáte rozšiřující pole $2^m$ v kryptografii.

Pro náš příklad předpokládejme, že vybereme polynom $x^3 + x + 1$. Tento je skutečně neredukovatelný, protože ho nelze faktorizovat pomocí celých čísel. Kromě toho zajistí, že jakékoli násobení dvou prvků vede k polynomu stupně 2 nebo nižšímu.
Pojďme si projít příklad druhé operace s použitím polynomu $x^3 + x + 1$ jako dělitele, abychom ilustrovali, jak to funguje. Předpokládejme, že násobíte prvky $x^2 + 1$ s $x^2 + x$ v naší množině **S**. Poté potřebujeme vypočítat výraz $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1$. To lze zjednodušit následovně:
* $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1 =$
* $[x^2 \cdot x^2 + x^2 \cdot x + 1 \cdot x^2 + 1 \cdot x] \mod x^3 + x + 1 =$
* $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$

Víme, že $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$ lze zredukovat, protože dělenec má vyšší stupeň (4) než dělitel (3).

Začneme tím, že vidíme, že výraz $x^3 + x + 1$ jde do $x^4 + x^3 + x^2 + x$ celkem $x$ krát. To můžete ověřit vynásobením $x^3 + x + 1$ číslem $x$, což je $x^4 + x^2 + x$. Jelikož poslední člen má stejný stupeň jako dělenec, tedy 4, víme, že to funguje. Zbytek této dělení číslem $x$ můžete vypočítat následovně:

* $[(x^4 + x^3 + x^2 + x) - (x^4 + x^2 + x)] \mod x^3 + x + 1 =$
* $[x^3] \mod x^3 + x + 1 =$
* $x^3$

Takže po dělení $x^4 + x^3 + x^2 + x$ číslem $x^3 + x + 1$ celkem $x$ krát máme zbytek $x^3$. Lze to dále dělit číslem $x^3 + x + 1$?

Intuitivně by se mohlo zdát, že $x^3$ již nelze dělit číslem $x^3 + x + 1$, protože poslední člen se zdá být větší. Nicméně si vzpomeňte na naši diskusi o vektorovém dělení dříve. Pokud má dělenec stupeň větší nebo rovný děliteli, výraz lze dále redukovat. Konkrétně, výraz $x^3 + x + 1$ může jít do $x^3$ přesně 1 krát. Zbytek je vypočítán následovně:

$$
[(x^3) - (x^3 + x + 1)] \mod x^3 + x + 1 = [x + 1] \mod x^3 + x + 1 = x + 1
$$

Možná se divíte, proč $(x^3) - (x^3 + x + 1)$ vyhodnotí na $x + 1$ a ne na $-x - 1$. Pamatujte, že první operace našeho pole je definována modulo 2. Tedy odečítání dvou vektorů dává přesně stejný výsledek jako sčítání dvou vektorů.
Shrnutí násobení $x^2 + 1$ a $x^2 + x$: Když tyto dva výrazy vynásobíte, dostanete polynom čtvrtého stupně, $x^4 + x^3 + x^2 + x$, který je potřeba redukovat modulo $x^3 + x + 1$. Polynom čtvrtého stupně je dělitelný $x^3 + x + 1$ přesně $x + 1$ krát. Zbytek po dělení $x^4 + x^3 + x^2 + x$ modulo $x^3 + x + 1$ přesně $x + 1$ krát je $x + 1$. To je skutečně prvek v naší množině $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.

Proč by mohla být rozšířená pole s bází 2 nad množinami polynomů, jako v příkladu výše, užitečná pro kryptografii? Důvodem je, že koeficienty v polynomech takových množin, buď 0 nebo 1, lze chápat jako prvky binárních řetězců s určitou délkou. Množina **S** v našem příkladu výše by například mohla být místo toho chápána jako množina **S**, která zahrnuje všechny binární řetězce délky 3 (000 až 111). Operace na **S** pak mohou být také použity k provádění operací na těchto binárních řetězcích a produkci binárního řetězce stejné délky.

**Poznámky:**

[2] Rozšířená pole se stávají velmi protiintuitivní. Místo toho, aby měla prvky celých čísel, mají sady polynomů. Navíc se veškeré operace provádějí modulo nějaký neredukovatelný polynom.

## Abstraktní algebra v praxi
<chapterId>ed35b98d-18b4-5790-9911-1078e0f84f92</chapterId>

Přes formální jazyk a abstraktnost diskuse by pojem skupiny neměl být příliš obtížný k pochopení. Jedná se jen o množinu prvků spolu s binární operací, kde výkon této binární operace na těchto prvcích splňuje čtyři obecné podmínky. Abelova skupina má jen jednu další podmínku známou jako komutativita. Cyklická skupina je zase speciální druh Abelovy skupiny, totiž taková, která má generátor. Pole je pouze složitější konstrukt základního pojmu skupiny.

Ale pokud jste prakticky zaměřená osoba, můžete se v tomto okamžiku ptát: Kdo to zajímá? Má vědění, že nějaká sada prvků s operátorem je skupina, nebo dokonce Abelova nebo cyklická skupina, nějaký reálný význam? Má vědění, že něco je pole?

Aniž bychom se pouštěli do přílišných detailů, odpověď je „ano“. Skupiny byly poprvé vytvořeny ve 19. století francouzským matematikem Evaristem Galoisem. Použil je k vyvození závěrů o řešení polynomiálních rovnic stupně vyššího než pět.

Od té doby pomohl koncept skupiny osvětlit řadu problémů v matematice a jinde. Na jejich základě byl například fyzik Murray-Gellman schopen předpovědět existenci částice, než byla skutečně pozorována v experimentech. [3] Jako další příklad, chemici používají teorii skupin k klasifikaci tvarů molekul. Matematikové dokonce použili koncept skupiny k vyvození závěrů o něčem tak konkrétním jako tapeta!
Podstatou ukázání, že množina prvků s nějakým operátorem tvoří skupinu, znamená, že to, co popisujete, má určitou symetrii. Ne symetrii v běžném smyslu slova, ale v abstraktnější formě. A to může poskytnout podstatné vhledy do konkrétních systémů a problémů. Složitější pojmy z abstraktní algebry nám jen poskytují další informace.
Nejdůležitější je, že uvidíte význam číselně teoretických skupin a polí v praxi prostřednictvím jejich aplikace v kryptografii, zejména v asymetrické kryptografii. Již jsme viděli v naší diskusi o polích, například, jak jsou rozšiřující pole využívána v šifře Rijndael. Tento příklad si probereme v *Kapitole 5*.

Pro další diskusi o abstraktní algebře bych doporučil vynikající video sérii o abstraktní algebře od Socratica. [4] Zvláště bych doporučil následující videa: “Co je abstraktní algebra?”, “Definice skupiny (rozšířená)”, “Definice okruhu (rozšířená)”, a “Definice pole (rozšířená)”. Tyto čtyři videa vám poskytnou další vhled do mnoha diskutovaných témat. (Nediskutovali jsme o okruzích, ale pole je jen speciální typ okruhu.)

Pro další diskusi o moderní číselné teorii můžete konzultovat mnoho pokročilých diskusí o kryptografii. Jako návrhy bych nabídl Jonathan Katz a Yehuda Lindell’s Introduction to Modern Cryptography nebo Christof Paar a Jan Pelzl’s Understanding Cryptography pro další diskusi. [5]

**Poznámky:**

[3] Viz [YouTube Video](https://www.youtube.com/watch?v=NOMUnMuxDZY&feature=youtu.be)

[4] Socratica, [Abstraktní Algebra](https://www.socratica.com/subject/abstract-algebra)

[5] Katz a Lindell, *Úvod do Moderní Kryptografie*, 2. vydání, 2015 (CRC Press: Boca Raton, FL). Paar a Pelzl, *Porozumění Kryptografii*, 2010 (Springer-Verlag: Berlín).

# Symetrická Kryptografie
<partId>ef768d0e-fe7b-510c-87d6-6febb3de1039</partId>

## Alice a Bob
<chapterId>47345330-be2d-5faf-afd0-d289a8d21bf1</chapterId>

Jednou ze dvou hlavních větví kryptografie je symetrická kryptografie. Zahrnuje šifrovací schémata stejně jako schémata týkající se autentizace a integrity. Do 70. let by všechna kryptografie spočívala v symetrických šifrovacích schématech.

Hlavní diskuse začíná pohledem na symetrická šifrovací schémata a děláním zásadního rozlišení mezi proudovými šiframi a blokovými šiframi. Poté se obrátíme na kódy pro autentizaci zpráv, které jsou schémata pro zajištění integrity a autentičnosti zpráv. Nakonec prozkoumáme, jak lze symetrická šifrovací schémata a kódy pro autentizaci zpráv kombinovat, aby se zajistila bezpečná komunikace.

Tato kapitola diskutuje různá symetrická kryptografická schémata z praxe mimochodem. Další kapitola nabízí podrobný výklad šifrování s proudovou šifrou a blokovou šifrou z praxe, konkrétně RC4 a AES.

Před zahájením naší diskuse o symetrické kryptografii chci stručně poznamenat několik poznámek k ilustracím Alice a Boba v této a následujících kapitolách.

___

Při ilustrování principů kryptografie se lidé často spoléhají na příklady zahrnující Alice a Boba. Budu to dělat také.

Zvláště pokud jste v oblasti kryptografie nováčci, je důležité si uvědomit, že tyto příklady Alice a Boba jsou určeny pouze jako ilustrace kryptografických principů a konstrukcí v zjednodušeném prostředí. Principy a konstrukce jsou však aplikovatelné na mnohem širší škálu reálných kontextů.
Následují pět klíčových bodů, které je třeba mít na paměti při příkladech zahrnujících Alice a Boba v kryptografii:
1. Mohou být snadno přeloženy do příkladů s jinými typy aktérů, jako jsou společnosti nebo vládní organizace.
2. Mohou být snadno rozšířeny o tři nebo více aktérů.
3. V příkladech jsou Bob a Alice typicky aktivními účastníky při vytváření každé zprávy a při aplikaci kryptografických schémat na tuto zprávu. Ale ve skutečnosti jsou elektronické komunikace většinou automatizované. Když například navštívíte webovou stránku používající zabezpečení transportní vrstvy, kryptografie je typicky zcela zpracovávána vaším počítačem a webovým serverem.
4. V kontextu elektronické komunikace jsou "zprávy", které jsou posílány přes komunikační kanál, obvykle pakety TCP/IP. Mohou patřit k e-mailu, zprávě na Facebooku, telefonnímu hovoru, přenosu souboru, webové stránce, nahrání softwaru a tak dále. Nejedná se o zprávy v tradičním smyslu. Přesto kryptografové často zjednodušují tuto realitu tím, že říkají, že zpráva je například e-mail.
5. Příklady se typicky zaměřují na elektronickou komunikaci, ale mohou být také rozšířeny na tradiční formy komunikace, jako jsou dopisy.

## Symetrická šifrovací schémata
<chapterId>41bfdbe1-6d41-5272-98bb-81f24b2fd6af</chapterId>

Symetrické šifrovací schéma můžeme volně definovat jako jakékoli kryptografické schéma se třemi algoritmy:

1. **Algoritmus generování klíče**, který generuje soukromý klíč.
2. **Šifrovací algoritmus**, který bere soukromý klíč a otevřený text jako vstupy a výstupem je šifrovaný text.
3. **Dešifrovací algoritmus**, který bere soukromý klíč a šifrovaný text jako vstupy a výstupem je původní otevřený text.

Typicky šifrovací schéma - ať už symetrické nebo asymetrické - nabízí šablonu pro šifrování založenou na základním algoritmu, spíše než přesnou specifikaci.

Například vezměme Salsa20, symetrické šifrovací schéma. Lze jej použít jak s 128bitovou, tak s 256bitovou délkou klíče. Volba délky klíče ovlivňuje některé drobné detaily algoritmu (přesněji počet kol v algoritmu).

Ale neřekli bychom, že použití Salsa20 s 128bitovým klíčem je jiné šifrovací schéma než Salsa20 s 256bitovým klíčem. Základní algoritmus zůstává stejný. Pouze když se změní základní algoritmus, opravdu bychom mluvili o dvou různých šifrovacích schématech.

Symetrická šifrovací schémata jsou typicky užitečná ve dvou typech případů: (1) Ty, ve kterých dva nebo více agentů komunikuje na dálku a chtějí udržet obsah své komunikace v tajnosti; a (2) ty, ve kterých jeden agent chce udržet obsah zprávy v tajnosti v průběhu času.

Situaci (1) můžete vidět na *Obrázku 1* níže. Bob chce poslat zprávu $M$ Alici na dálku, ale nechce, aby tuto zprávu mohli číst ostatní.

Bob nejprve zašifruje zprávu $M$ soukromým klíčem $K$. Poté pošle šifrovaný text $C$ Alici. Jakmile Alice šifrovaný text obdrží, může jej dešifrovat pomocí klíče $K$ a přečíst otevřený text. S dobrým šifrovacím schématem by jakýkoli útočník, který zachytí šifrovaný text $C$, neměl být schopen se dozvědět nic skutečně významného o zprávě $M$.

Situaci (2) můžete vidět na *Obrázku 2* níže. Bob chce zabránit ostatním v prohlížení určitých informací. Typická situace by mohla být, že Bob je zaměstnanec ukládající citlivá data na svém počítači, která by neměli číst ani vnější osoby, ani jeho kolegové.
Bob zašifruje zprávu $M$ v čase $T_0$ klíčem $K$, čímž vytvoří šifrový text $C$. V čase $T_1$ potřebuje zprávu znovu a dešifruje šifrový text $C$ klíčem $K$. Jakýkoli útočník, který by se mezitím mohl dostat k šifrovému textu $C$, by z něj neměl být schopen odvodit nic významného o $M$.

*Obrázek 1: Tajemství v prostoru*

![Obrázek 1: Tajemství v prostoru](assets/Figure4-1.webp "Obrázek 1: Tajemství v prostoru")

*Obrázek 2: Tajemství v čase*

![Obrázek 2: Tajemství v čase](assets/Figure4-2.webp "Obrázek 2: Tajemství v čase")

## Příklad: Caesarova šifra
<chapterId>7b179ae8-8d15-5e80-a43f-22c970d87b5e</chapterId>

V kapitole 2 jsme se setkali s Caesarovou šifrou, která je příkladem velmi jednoduchého symetrického šifrovacího schématu. Podívejme se na ni znovu zde.

Předpokládejme slovník *D*, který přiřazuje všechna písmena anglické abecedy, v pořadí, k množině čísel $\{0,1,2,\dots,25\}$. Předpokládejme množinu možných zpráv **M**. Caesarova šifra je potom definována následovně:

- Náhodně vyberte klíč $k$ z množiny možných klíčů **K**, kde **K** = $\{0,1,2,\dots,25\}$
- Zašifrujte zprávu $m \in$ **M**, takto:
    - Rozdělte $m$ na jednotlivá písmena $m_0, m_1,\dots, m_i, \dots, m_l$
    - Převeďte každé $m_i$ na číslo podle *D*
    - Pro každé $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Převeďte každé $c_i$ zpět na písmeno podle *D*
    - Poté spojte $c_0, c_1,\dots, c_l$ k získání šifrového textu $c$
- Dešifrujte šifrový text $c$ takto:
    - Převeďte každé $c_i$ na číslo podle *D*
    - Pro každé $c_i$, $m_i = [(c_i - k) \mod 26]$
    - Převeďte každé $m_i$ zpět na písmeno podle *D*
    - Poté spojte $m_0, m_1,\dots, m_l$ k získání původní zprávy $m$

To, co dělá Caesarovu šifru symetrickým šifrovacím schématem, je použití stejného klíče pro oba procesy, šifrování i dešifrování. Předpokládejme například, že chcete zašifrovat zprávu „DOG“ pomocí Caesarovy šifry a náhodně jste vybrali klíč "24". Zašifrování zprávy s tímto klíčem by vydalo „BME“. Jediný způsob, jak získat původní zprávu, je použití stejného klíče, "24", pro proces dešifrování.

Tato Caesarova šifra je příkladem **monoalfabetické substituční šifry**: šifrovacího schématu, kde je šifrová abeceda pevná (tj. používá se pouze jedna abeceda). Za předpokladu, že dešifrovací algoritmus je deterministický, každý symbol v substitučním šifrovém textu může nejvýše odpovídat jednomu symbolu v otevřeném textu.
Do 18. století se mnoho aplikací šifrování spoléhalo převážně na monoalfabetické substituční šifry, ačkoli ty často byly mnohem složitější než Caesarova šifra. Mohli byste například náhodně vybrat písmeno z abecedy pro každé původní písmeno textu s omezením, že každé písmeno se v šifrovém abecedě vyskytuje pouze jednou. To znamená, že byste měli faktoriál 26 možných soukromých klíčů, což bylo obrovské v době před počítači.
Všimněte si, že se v kryptografii setkáte s termínem **šifra** velmi často. Mějte na paměti, že tento termín má různé významy. Ve skutečnosti znám alespoň pět odlišných významů tohoto termínu v rámci kryptografie.

V některých případech se odkazuje na šifrovací schéma, jak je tomu u Caesarovy šifry a monoalfabetické substituční šifry. Avšak termín může také specificky odkazovat na šifrovací algoritmus, soukromý klíč, nebo pouze na šifrovaný text jakéhokoli takového šifrovacího schématu.

Nakonec termín šifra může také odkazovat na základní algoritmus, z něhož lze konstruovat kryptografická schémata. Mohou zahrnovat různé šifrovací algoritmy, ale také jiné typy kryptografických schémat. Tento význam termínu se stává relevantním v kontextu blokových šifer (viz sekce „Blokové šifry“ níže).

Můžete se také setkat s termíny **zašifrovat** nebo **dešifrovat**. Tyto termíny jsou pouze synonymy pro šifrování a dešifrování.

## Útoky hrubou silou a Kerckhoffův princip
<chapterId>2d73ef97-26c5-5d11-8815-0ddbe89c8003</chapterId>

Caesarova šifra je velmi nezabezpečené symetrické šifrovací schéma, alespoň ve moderním světě. [1] Útočník by mohl jednoduše pokusit dešifrovat jakýkoli šifrovaný text se všemi 26 možnými klíči, aby zjistil, který výsledek dává smysl. Tento typ útoku, kdy útočník pouze prochází klíče, aby zjistil, co funguje, je známý jako **útok hrubou silou** nebo **vyčerpávající hledání klíče**.

Aby jakékoli šifrovací schéma splňovalo minimální požadavky na bezpečnost, musí mít sadu možných klíčů, nebo **prostor klíčů**, který je tak velký, že útoky hrubou silou jsou nepraktické. Všechna moderní šifrovací schémata splňují tento standard. Je to známé jako **princip dostatečného prostoru klíčů**. Podobný princip se obvykle uplatňuje i v různých typech kryptografických schémat.

Abyste si udělali představu o obrovské velikosti prostoru klíčů v moderních šifrovacích schématech, předpokládejme, že soubor byl zašifrován 128bitovým klíčem pomocí pokročilého šifrovacího standardu. To znamená, že útočník má sadu $2^{128}$ klíčů, kterými musí projít pro útok hrubou silou. Šance na úspěch s touto strategií by vyžadovala, aby útočník prošel přibližně $2.65 \times 10^{36}$ klíčů.

Předpokládejme optimisticky, že útočník může zkoušet $10^{16}$ klíčů za sekundu (tj. 10 kvadrilionů klíčů za sekundu). Aby otestoval 0.78% všech klíčů v prostoru klíčů, jeho útok by musel trvat $2.65 \times 10^{20}$ sekund. To je přibližně 8,4 bilionu let. Takže i útok hrubou silou od absurdně mocného protivníka není s moderním 128bitovým šifrovacím schématem realistický. To je princip dostatečného prostoru klíčů v praxi.

Je Caesarova šifra bezpečnější, pokud útočník nezná šifrovací algoritmus? Možná, ale ne o mnoho.
V každém případě moderní kryptografie vždy předpokládá, že bezpečnost jakéhokoli symetrického šifrovacího schématu závisí pouze na udržení tajnosti soukromého klíče. Předpokládá se, že útočník zná všechny ostatní detaily, včetně prostoru zpráv, prostoru klíčů, prostoru šifrovaného textu, algoritmu výběru klíče, šifrovacího algoritmu a dešifrovacího algoritmu.
Myšlenka, že bezpečnost symetrického šifrovacího schématu může spoléhat pouze na tajemství soukromého klíče, je známá jako **Kerckhoffsův princip**.

Jak původně Kerckhoffs zamýšlel, princip se vztahuje pouze na symetrická šifrovací schémata. Obecnější verze principu se však vztahuje i na všechny ostatní moderní typy kryptografických schémat: Návrh jakéhokoli kryptografického schématu nesmí vyžadovat, aby byl tajný, aby byl bezpečný; tajemství může zahrnovat pouze některé řetězce informací, typicky soukromý klíč.

Kerckhoffsův princip je pro moderní kryptografii klíčový ze čtyř důvodů. [2] Za prvé, existuje pouze omezený počet kryptografických schémat pro konkrétní typy aplikací. Například většina moderních aplikací symetrického šifrování používá šifru Rijndael. Takže vaše tajemství ohledně návrhu schématu je jen velmi omezené. Existuje však mnohem větší flexibilita v udržování tajnosti nějakého soukromého klíče pro šifru Rijndael.

Za druhé, je snazší nahradit nějaký řetězec informací než celé kryptografické schéma. Předpokládejme, že všichni zaměstnanci společnosti mají stejný šifrovací software a každí dva zaměstnanci mají soukromý klíč pro důvěrnou komunikaci. Kompromitace klíčů je v tomto scénáři problém, ale alespoň by společnost mohla zachovat software s takovými bezpečnostními problémy. Pokud by se společnost spoléhala na tajemství schématu, jakýkoli únik tohoto tajemství by vyžadoval výměnu veškerého softwaru.

Za třetí, Kerckhoffsův princip umožňuje standardizaci a kompatibilitu mezi uživateli kryptografických schémat. To má obrovské výhody pro efektivitu. Například je těžké si představit, jak by miliony lidí mohly každý den bezpečně připojovat k webovým serverům Google, pokud by toto zabezpečení vyžadovalo udržování tajnosti kryptografických schémat.

Za čtvrté, Kerckhoffsův princip umožňuje veřejnou kontrolu kryptografických schémat. Tento typ kontroly je naprosto nezbytný pro dosažení bezpečných kryptografických schémat. Ilustrativně, hlavní jádrový algoritmus v symetrické kryptografii, šifra Rijndael, byl výsledkem soutěže organizované Národním institutem pro standardy a technologie mezi lety 1997 a 2000.

Jakýkoli systém, který se snaží dosáhnout **bezpečnosti skrze utajení**, je systém, který spoléhá na udržování tajnosti detailů svého návrhu a/nebo implementace. V kryptografii by to byl konkrétně systém, který spoléhá na udržování tajnosti návrhových detailů kryptografického schématu. Takže bezpečnost skrze utajení je v přímém kontrastu s Kerckhoffsův princip.

Schopnost otevřenosti posílit kvalitu a bezpečnost se také šíří šířeji do digitálního světa než jen kryptografie. Svobodné a otevřené distribuce Linuxu, jako je například Debian, mají obecně několik výhod oproti jejich protějškům Windows a MacOS z hlediska soukromí, stability, bezpečnosti a flexibility. Ačkoliv to může mít více příčin, nejdůležitějším principem je pravděpodobně, jak to Eric Raymond vyjádřil ve svém slavném eseji "The Cathedral and the Bazaar", že "při dostatečném počtu očí jsou všechny chyby povrchní." [3] Je to tento princip moudrosti davu, který dal Linuxu jeho nejvýznamnější úspěch.
Nikdy nelze jednoznačně prohlásit, že kryptografické schéma je "bezpečné" nebo "nebezpečné". Místo toho existují různé pojmy bezpečnosti pro kryptografická schémata. Každá **definice kryptografické bezpečnosti** musí specifikovat (1) cíle bezpečnosti, stejně jako (2) schopnosti útočníka. Analýza kryptografických schémat vzhledem k jedné nebo více konkrétním pojmem bezpečnosti poskytuje přehled o jejich aplikacích a omezeních.
Ačkoli se nebudeme zabývat všemi detaily různých pojmů kryptografické bezpečnosti, měli byste vědět, že dvě předpoklady jsou všudypřítomné pro všechny moderní pojmy kryptografické bezpečnosti týkající se symetrických a asymetrických schémat (a v nějaké formě i pro jiné kryptografické primitivy):

* Znalost útočníka o schématu odpovídá Kerckhoffsově principu.
* Útočník nemůže proveditelně provést útok hrubou silou na schéma. Konkrétně, modely hrozeb kryptografických pojmů bezpečnosti typicky ani nepřipouštějí útoky hrubou silou, protože předpokládají, že tyto nejsou relevantní.

**Poznámky:**

[1] Podle Seutonia byl šifrovací systém se stálou klíčovou hodnotou 3 používán Juliusem Caesarem ve vojenské komunikaci. Takže A by se vždy stalo D, B vždy E, C vždy F a tak dále. Tato konkrétní verze šifrovacího systému se tak stala známou jako **Caesarova šifra** (i když to ve skutečnosti není šifra v moderním smyslu slova, protože klíčová hodnota je stálá). Caesarova šifra mohla být bezpečná v prvním století př. n. l., pokud byli nepřátelé Říma velmi neznalí v šifrování. Ale v moderní době by to zřejmě nebylo velmi bezpečné schéma.

[2] Jonathan Katz a Yehuda Lindell, _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL: 2015), str. 7f.

[3] Eric Raymond, “The Cathedral and the Bazaar,” přednáška byla prezentována na Linux Kongress, Würzburg, Německo (27. května 1997). Existuje řada následujících verzí stejně jako kniha. Moje citace jsou ze strany 30 v knize: Eric Raymond, _The Cathedral and the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary_, revidované vydání. (2001), O’Reilly: Sebastopol, CA.

## Proudové šifry
<chapterId>479aa6f4-45c4-59ca-8616-8cf8e61fc871</chapterId>

Symetrická šifrovací schémata jsou standardně rozdělena do dvou typů: **proudové šifry** a **blokové šifry**. Toto rozdělení je však poněkud problematické, jelikož lidé používají tyto termíny nekonzistentním způsobem. V následujících několika sekcích nastíním rozdíl tak, jak si myslím, že je nejlepší. Měli byste však vědět, že mnoho lidí bude používat tyto termíny poněkud odlišně, než zde uvádím.

Pojďme se nejprve zaměřit na proudové šifry. **Proudová šifra** je symetrické šifrovací schéma, kde šifrování se skládá ze dvou kroků.

Nejprve je pomocí soukromého klíče vyprodukován řetězec o délce otevřeného textu. Tento řetězec se nazývá **klíčový proud**.

Poté je klíčový proud matematicky kombinován s otevřeným textem, čímž vznikne šifrovaný text. Tato kombinace je typicky operace XOR. Pro dešifrování můžete jen operaci obrátit. (Poznamenejme, že $A \oplus B = B \oplus A$, v případě, že $A$ a $B$ jsou bitové řetězce. Takže pořadí operace XOR v proudové šifře nemá význam pro výsledek. Tato vlastnost je známá jako **komutativita**.)
Typický proudový šifrovací algoritmus XOR je znázorněn na *Obrázku 3*. Nejprve vezmete soukromý klíč $K$ a použijete ho k vygenerování klíčového proudu. Klíčový proud je poté kombinován s otevřeným textem prostřednictvím operace XOR, čímž vznikne šifrovaný text. Jakýkoli agent, který obdrží šifrovaný text, ho může snadno dešifrovat, pokud má klíč $K$. Vše, co potřebuje, je vytvořit klíčový proud stejně dlouhý jako šifrovaný text podle určeného postupu schématu a XORovat ho se šifrovaným textem.

*Obrázek 3: Proudový šifrovací algoritmus XOR*

![Obrázek 3: Proudový šifrovací algoritmus XOR](assets/Figure4-3.webp "Obrázek 3: Proudový šifrovací algoritmus XOR")

Pamatujte, že schéma šifrování je typicky šablona pro šifrování se stejným základním algoritmem, spíše než přesná specifikace. Rozšířeně, proudový šifrovací algoritmus je typicky šablona pro šifrování, ve které můžete používat klíče různých délek. Ačkoliv délka klíče může ovlivnit některé drobné detaily schématu, neovlivní jeho zásadní formu.

Posunový šifrovací algoritmus je příkladem velmi jednoduchého a nezabezpečeného proudového šifrovacího algoritmu. Použitím jediného písmene (soukromého klíče) můžete vyprodukovat řetězec písmen o délce zprávy (klíčový proud). Tento klíčový proud je poté kombinován s otevřeným textem prostřednictvím modulové operace, čímž vznikne šifrovaný text. (Tato modulová operace může být zjednodušena na operaci XOR při reprezentaci písmen v bitech).

Dalším slavným příkladem proudového šifrovacího algoritmu je **Vigenèrova šifra**, pojmenovaná po Blaisovi de Vigenère, který ji plně rozvinul na konci 16. století (i když před ním již mnoho jiných vykonalo spoustu předchozí práce). Jedná se o příklad **polyalfabetické substituční šifry**: šifrovacího schématu, kde šifrovací abeceda pro symbol otevřeného textu se mění v závislosti na jeho pozici v textu. Na rozdíl od monoalfabetické substituční šifry mohou být symboly šifrovaného textu spojeny s více než jedním symbolem otevřeného textu.

Jak šifrování získávalo na popularitě v renesanční Evropě, také **kryptoanalýza**—to jest, prolomení šifrovaných textů—zejména pomocí **frekvenční analýzy**. Posledně jmenovaná využívá statistické pravidelnosti v našem jazyce k prolomení šifrovaných textů a byla objevena arabskými učenci již v devátém století. Je to technika, která funguje obzvláště dobře s delšími texty. A dokonce i nejsofistikovanější monoalfabetické substituční šifry již nebyly proti frekvenční analýze dostatečné v 1700s v Evropě, zejména v vojenských a bezpečnostních nastaveních. Jelikož Vigenèrova šifra nabídla významný pokrok v bezpečnosti, stala se populární v tomto období a do konce 1700s byla rozšířená.

Neformálně řečeno, šifrovací schéma funguje takto:

1. Vyberte vícepísmenné slovo jako soukromý klíč.
2. Pro jakoukoli zprávu aplikujte posunový šifrovací algoritmus na každé písmeno zprávy použitím odpovídajícího písmene v klíčovém slově jako posun.
3. Pokud jste prošli klíčovým slovem, ale stále jste celý otevřený text nezašifrovali, znovu aplikujte písmena klíčového slova jako posunový šifrovací algoritmus na odpovídající písmena v zbytku textu.
4. Pokračujte v tomto procesu, dokud nebude celá zpráva zašifrována.

Pro ilustraci, předpokládejme, že váš soukromý klíč je "GOLD" a chcete zašifrovat zprávu "CRYPTOGRAPHY". V tom případě byste postupovali podle Vigenèrovy šifry následovně:

- $c_0  = [(2 + 6) \mod 26] = 8 = I$
- $c_1  = [(17 + 14) \mod 26] = 5 = F$
- $c_2  = [(24 + 11) \mod 26] = 9 = J$
- $c_3  = [(15 + 3) \mod 26] = 18 = S$
- $c_4  = [(19 + 6) \mod 26] = 25 = Z$
- $c_5  = [(14 + 14) \mod 26] = 2 = C$
- $c_6  = [(6 + 11) \mod 26] = 17 = R$
- $c_7  = [(17 + 3) \mod 26] = 20 = U$
- $c_8  = [(0 + 6) \mod 26] = 6 = G$
- $c_9  = [(15 + 14) \mod 26] = 3 = D$
- $c_{10} = [(7 + 11) \mod 26] = 18 = S$
- $c_{11} = [(24 + 3) \mod 26] = 1 = B$

Takže šifrový text $c$ = "IFJSZCRUGDSB".

Dalším slavným příkladem proudové šifry je **jednorázový šifrovací blok**. U jednorázového šifrovacího bloku jednoduše vytvoříte řetězec náhodných bitů stejně dlouhý jako zpráva v otevřeném textu a šifrový text vytvoříte pomocí operace XOR. Tedy soukromý klíč a proud klíčů jsou u jednorázového šifrovacího bloku ekvivalentní.

Zatímco šifra posunu a Vigenèrova šifra jsou v moderní době velmi nezabezpečené, jednorázový šifrovací blok je velmi bezpečný, pokud je používán správně. Pravděpodobně nejslavnější aplikací jednorázového šifrovacího bloku byla, alespoň do 80. let, **Washingtonsko-moskevská horká linka**.

Horká linka je přímé komunikační spojení mezi Washingtonem a Moskvou pro naléhavé záležitosti, které bylo nainstalováno po Kubánské raketové krizi. Technologie pro tuto linku se během let transformovala. V současnosti zahrnuje přímý optický kabel a také dva satelitní spoje (pro redundanci), které umožňují e-mail a textové zprávy. Linka končí na různých místech v USA. Pentagon, Bílý dům a hora Raven Rock jsou známé koncové body. Na rozdíl od populárního názoru, horká linka nikdy nezahrnovala telefony.

V podstatě schéma jednorázového šifrovacího bloku fungovalo takto. Washington a Moskva by měly dvě sady náhodných čísel. Jedna sada náhodných čísel, vytvořená Rusy, se týkala šifrování a dešifrování jakýchkoli zpráv v ruštině. Jedna sada náhodných čísel, vytvořená Američany, se týkala šifrování a dešifrování jakýchkoli zpráv v angličtině. Čas od času by více náhodných čísel bylo doručeno na druhou stranu důvěryhodnými kurýry.

Washington a Moskva pak mohly tajně komunikovat pomocí těchto náhodných čísel pro vytváření jednorázových šifrovacích bloků. Pokaždé, když jste potřebovali komunikovat, použili byste další část náhodných čísel pro vaši zprávu.

Přestože je jednorázový šifrovací blok vysoce bezpečný, čelí významným praktickým omezením: klíč musí být stejně dlouhý jako zpráva a žádná část jednorázového šifrovacího bloku nemůže být použita znovu. To znamená, že musíte sledovat, kde se v jednorázovém šifrovacím bloku nacházíte, uchovávat obrovské množství bitů a občas vyměňovat náhodné bity se svými protistranami. V důsledku toho se jednorázový šifrovací blok v praxi často nepoužívá.

Namísto toho jsou v praxi běžně používány **pseudonáhodné proudové šifry**. Salsa20 a úzce související varianta nazvaná ChaCha jsou příklady běžně používaných pseudonáhodných proudových šifer.
S těmito pseudonáhodnými proudovými šiframi nejprve náhodně vyberete klíč K, který je kratší než délka otevřeného textu. Takový náhodný klíč K je obvykle vytvořen naším počítačem na základě nepředvídatelných dat, která sbírá v průběhu času, jako je čas mezi síťovými zprávami, pohyby myši a tak dále.
Tento náhodný klíč $K$ je poté vložen do expanzního algoritmu, který vytvoří pseudonáhodný klíčový proud dlouhý jako zpráva. Můžete přesně určit, jak dlouhý má klíčový proud být (např. 500 bitů, 1000 bitů, 1200 bitů, 29 117 bitů atd.).

Pseudonáhodný klíčový proud se jeví *jako by* byl vybrán zcela náhodně ze sady všech řetězců stejné délky. Proto šifrování s pseudonáhodným klíčovým proudem vypadá, jako by bylo provedeno s jednorázovým šifrovacím blokem. Ale to samozřejmě není pravda.

Jelikož je náš soukromý klíč kratší než klíčový proud a náš expanzní algoritmus musí být deterministický, aby proces šifrování/dešifrování fungoval, ne každý klíčový proud této konkrétní délky by mohl být výstupem z naší expanzní operace.

Předpokládejme například, že náš soukromý klíč má délku 128 bitů a že ho můžeme vložit do expanzního algoritmu, aby vytvořil mnohem delší klíčový proud, řekněme 2500 bitů. Jelikož náš expanzní algoritmus musí být deterministický, náš algoritmus může na výběr mít nejvýše $1/2^{128}$ řetězců s délkou 2500 bitů. Takový klíčový proud by tedy nikdy nemohl být vybrán zcela náhodně ze všech řetězců stejné délky.

Naše definice proudové šifry má dva aspekty: (1) klíčový proud dlouhý jako otevřený text je generován s pomocí soukromého klíče; a (2) tento klíčový proud je kombinován s otevřeným textem, typicky prostřednictvím operace XOR, aby vznikl šifrový text.

Někdy lidé definují podmínku (1) striktněji, tvrdící, že klíčový proud musí být specificky pseudonáhodný. To znamená, že ani posunovací šifra, ani jednorázový šifrovací blok by nebyly považovány za proudové šifry.

Podle mého názoru poskytuje širší definování podmínky (1) jednodušší způsob, jak organizovat šifrovací schémata. Kromě toho to znamená, že nemusíme přestat nazývat určité šifrovací schéma proudovou šifrou jen proto, že se dozvíme, že ve skutečnosti nespoléhá na pseudonáhodné klíčové proudy.

**Poznámky:**

[4] Crypto Museum, "Washington-Moscow hotline," 2013, dostupné na [https://www.cryptomuseum.com/crypto/hotline/index.htm](https://www.cryptomuseum.com/crypto/hotline/index.htm).

## Blokové šifry
<chapterId>2df52d51-943d-5df7-9d49-333e4c5d97b7</chapterId>

První způsob, jakým se obvykle chápe **bloková šifra**, je jako něco primitivnějšího než proudová šifra: Základní algoritmus, který provádí transformaci zachovávající délku na řetězci vhodné délky s pomocí klíče. Tento algoritmus lze použít pro vytváření šifrovacích schémat a možná i dalších typů kryptografických schémat.
Často může bloková šifra přijímat vstupní řetězce různých délek, jako jsou 64, 128 nebo 256 bitů, stejně jako klíče různých délek, jako jsou 128, 192 nebo 256 bitů. Ačkoliv se některé detaily algoritmu mohou v závislosti na těchto proměnných měnit, základní algoritmus se nemění. Kdyby se měnil, hovořili bychom o dvou různých blokových šifrách. Všimněte si, že použití terminologie základního algoritmu zde je stejné jako u šifrovacích schémat.

Znázornění fungování blokové šifry můžete vidět na *Obrázku 4* níže. Zpráva $M$ o délce $L$ a klíč $K$ slouží jako vstupy do blokové šifry. Výstupem je zpráva $M'$ o délce $L$. Klíč nemusí nutně mít stejnou délku jako $M$ a $M'$ u většiny blokových šifer.

*Obrázek 4: Bloková šifra*

![Obrázek 4: Bloková šifra](assets/Figure4-4.webp "Obrázek 4: Bloková šifra")

Bloková šifra sama o sobě není šifrovacím schématem. Ale bloková šifra může být použita s různými **režimy provozu** k vytvoření různých šifrovacích schémat. Režim provozu jednoduše přidává některé další operace mimo blokovou šifru.

Abychom ilustrovali, jak to funguje, předpokládejme blokovou šifru (BC), která vyžaduje 128bitový vstupní řetězec a 128bitový soukromý klíč. Obrázek 5 níže ukazuje, jak lze tuto blokovou šifru použít s **režimem elektronické kódové knihy** (**ECB mode**) k vytvoření šifrovacího schématu. (Elipsy vpravo naznačují, že tento vzor můžete opakovat tak dlouho, jak je potřeba).

*Obrázek 5: Bloková šifra s ECB mode*

![Obrázek 5: Bloková šifra s ECB mode](assets/Figure4-5.webp "Obrázek 5: Bloková šifra s ECB mode")

Proces šifrování elektronické kódové knihy s blokovou šifrou je následující. Zkuste rozdělit vaši otevřenou zprávu na 128bitové bloky. Pokud to není možné, přidejte k zprávě **doplnění** tak, aby výsledek mohl být rovnoměrně rozdělen podle velikosti bloku 128 bitů. To jsou vaše data použitá pro šifrovací proces.

Nyní rozdělte data na části 128bitových řetězců ($M_1$, $M_2$, $M_3$ a tak dále). Každý 128bitový řetězec prožeňte blokovou šifrou s vaším 128bitovým klíčem, abyste vytvořili 128bitové části šifrovaného textu ($C_1$, $C_2$, $C_3$ a tak dále). Tyto části, když jsou znovu spojeny, tvoří úplný šifrovaný text.

Dešifrování je jen opačný proces, ačkoliv příjemce potřebuje nějaký rozpoznatelný způsob, jak odstranit jakékoli doplnění z dešifrovaných dat, aby získal původní otevřenou zprávu.

Ačkoliv je relativně přímočaré, bloková šifra s režimem elektronické kódové knihy postrádá bezpečnost. To je proto, že vede k **deterministickému šifrování**. Jakékoli dva identické 128bitové řetězce dat jsou šifrovány přesně stejným způsobem. Tyto informace mohou být zneužity.

Místo toho by jakékoli šifrovací schéma vytvořené z blokové šifry mělo být **pravděpodobnostní**: to znamená, že šifrování jakékoli zprávy $M$, nebo jakékoli konkrétní části $M$, by mělo obvykle vést k odlišnému výsledku pokaždé. [5]

**Režim řetězení bloků šifer** (**CBC mode**) je pravděpodobně nejběžnější režim používaný s blokovou šifrou. Kombinace, pokud je provedena správně, produkuje pravděpodobnostní šifrovací schéma. Znázornění tohoto režimu provozu můžete vidět na *Obrázku 6* níže.

*Obrázek 6: Bloková šifra s CBC mode*
![Obrázek 6: Bloková šifra s režimem CBC](assets/Figure4-6.webp "Obrázek 6: Bloková šifra s režimem CBC")
Předpokládejme, že velikost bloku je opět 128 bitů. Takže na začátku byste opět museli zajistit, aby vaše původní zpráva v otevřeném textu obdržela potřebnou doplňkovou výplň.

Poté provedete operaci XOR první 128bitové části vašeho otevřeného textu s **inicializačním vektorem** o velikosti 128 bitů. Výsledek je vložen do blokové šifry, aby se vyprodukoval šifrovaný text pro první blok. Pro druhý blok o velikosti 128 bitů nejprve provedete XOR otevřeného textu se šifrovaným textem z prvního bloku, než jej vložíte do blokové šifry. Tento proces pokračuje, dokud nezašifrujete celou vaši zprávu v otevřeném textu.

Když skončíte, odešlete šifrovanou zprávu společně s nezašifrovaným inicializačním vektorem příjemci. Příjemce musí znát inicializační vektor, jinak nemůže dešifrovat šifrovaný text.

Tato konstrukce je mnohem bezpečnější než režim elektronické kódové knihy, pokud je používána správně. Měli byste nejprve zajistit, aby inicializační vektor byl náhodný nebo pseudonáhodný řetězec. Kromě toho byste měli pokaždé, když použijete tento šifrovací systém, použít jiný inicializační vektor.

Jinými slovy, váš inicializační vektor by měl být náhodný nebo pseudonáhodný nonce, kde **nonce** znamená "číslo, které se použije pouze jednou". Pokud si toto pravidlo udržíte, pak režim CBC s blokovou šifrou zajistí, že jakékoli dva identické bloky otevřeného textu budou vždy zašifrovány odlišně.

Nakonec se zaměřme na **režim zpětné vazby výstupu** (**OFB režim**). Tento režim můžete vidět na *Obrázku 7*.

*Obrázek 7: Bloková šifra s režimem OFB*

![Obrázek 7: Bloková šifra s režimem OFB](assets/Figure4-7.webp "Obrázek 7: Bloková šifra s režimem OFB")

V režimu OFB také vyberete inicializační vektor. Ale zde, pro první blok, je inicializační vektor přímo vložen do blokové šifry s vaším klíčem. Výsledných 128 bitů je poté považováno za klíčový proud. Tento klíčový proud je proveden XOR s otevřeným textem, aby se vyprodukoval šifrovaný text pro blok. Pro následující bloky použijete klíčový proud z předchozího bloku jako vstup do blokové šifry a kroky opakujete.

Pokud se podíváte pozorně, co bylo zde vytvořeno s blokovou šifrou v režimu OFB, je to proudová šifra. Generujete části klíčového proudu o velikosti 128 bitů, dokud nemáte délku otevřeného textu (zahodíte bity, které nepotřebujete z poslední 128bitové části klíčového proudu). Poté provedete XOR klíčového proudu s vaší zprávou v otevřeném textu, abyste získali šifrovaný text.

V předchozí sekci o proudových šifrách jsem uvedl, že vytváříte klíčový proud s pomocí soukromého klíče. Přesněji řečeno, nemusí být vytvořen pouze s soukromým klíčem. Jak můžete vidět v režimu OFB, klíčový proud je vytvořen s podporou jak soukromého klíče, tak inicializačního vektoru.

Všimněte si, že stejně jako v režimu CBC, je důležité vybrat pseudonáhodný nebo náhodný nonce pro inicializační vektor pokaždé, když používáte blokovou šifru v režimu OFB. Jinak bude stejný 128bitový řetězec zpráv poslaný v různých komunikacích zašifrován stejným způsobem. To je jeden ze způsobů, jak vytvořit pravděpodobnostní šifrování s proudovou šifrou.
Některé proudové šifry používají pouze soukromý klíč k vytvoření klíčového proudu. U těchto proudových šifer je důležité, abyste pro každou instanci komunikace použili náhodný nonce k výběru soukromého klíče. Jinak budou výsledky šifrování těmito proudovými šiframi také deterministické, což povede k bezpečnostním problémům. 
Nejpopulárnější moderní bloková šifra je **Rijndaelova šifra**. Byla vítězným příspěvkem z patnácti přihlášek do soutěže pořádané Národním institutem pro standardy a technologie (NIST) mezi lety 1997 a 2000 za účelem nahrazení staršího standardu šifrování, **standardu šifrování dat** (**DES**).

Rijndaelova šifra může být použita s různými specifikacemi pro délky klíčů a velikosti bloků, stejně jako v různých režimech provozu. Výbor pro soutěž NIST přijal omezenou verzi Rijndaelovy šifry – konkrétně takovou, která vyžaduje 128bitové velikosti bloků a délky klíčů 128 bitů, 192 bitů nebo 256 bitů – jako součást **pokročilého šifrovacího standardu** (**AES**). To je skutečně hlavní standard pro aplikace symetrického šifrování. Je tak bezpečný, že dokonce i NSA je zjevně ochotna jej používat s 256bitovými klíči pro dokumenty s nejvyšším stupněm utajení. [6]

Bloková šifra AES bude podrobně vysvětlena v *kapitole 5*.


**Poznámky:**

[5] Význam pravděpodobnostního šifrování byl poprvé zdůrazněn Shafim Goldwasserem a Silviem Micalim, „Pravděpodobnostní šifrování,“ _Journal of Computer and System Sciences_, 28 (1984), 270–99.

[6] Viz NSA, "Commercial National Security Algorithm Suite", [https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm](https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm).



## Vyjasnění zmatku
<chapterId>121c1858-27e3-5862-b0ce-4ff2f70f9f0f</chapterId>

Zmatek ohledně rozlišení mezi blokovými a proudovými šiframi vzniká, protože někdy lidé chápou termín bloková šifra jako odkazující konkrétně na *blokovou šifru s režimem šifrování bloků*.

Zvažte režimy ECB a CBC v předchozí sekci. Tyto konkrétně vyžadují, aby data pro šifrování byla dělitelná velikostí bloku (což znamená, že možná budete muset použít doplnění pro původní zprávu). Kromě toho jsou data v těchto režimech také přímo zpracovávána blokovou šifrou (a nejen kombinována s výsledkem operace blokové šifry jako v režimu OFB).

Takže alternativně můžete definovat **blokovou šifru** jako jakékoli šifrovací schéma, které operuje s pevně danými délkami bloků zprávy najednou (kde jakýkoli blok musí být delší než jeden bajt, jinak se to zhroutí do proudové šifry). Jak data pro šifrování, tak i šifrovaný text musí být rovnoměrně dělitelné do této velikosti bloku. Typicky je velikost bloku 64, 128, 192 nebo 256 bitů. Naproti tomu proudová šifra může šifrovat jakékoli zprávy v kusech po jednom bitu nebo bajtu najednou.

S tímto specifičtějším pochopením blokové šifry můžete skutečně tvrdit, že moderní šifrovací schémata jsou buď proudové nebo blokové šifry. Odtud budu termín bloková šifra používat ve všeobecnějším smyslu, pokud není uvedeno jinak.
Diskuse o režimu OFB v předchozí sekci také otevírá další zajímavý bod. Některé proudové šifry jsou postaveny na blokových šifrách, jako je Rijndael s OFB. Některé, jako Salsa20 a ChaCha, nejsou vytvořeny z blokových šifrovacích algoritmů. Tyto byste mohli nazvat **primitivní proudové šifry**. (Ve skutečnosti neexistuje standardizovaný termín pro označení takových proudových šifer.)
Když lidé mluví o výhodách a nevýhodách proudových a blokových šifer, obvykle porovnávají primitivní proudové šifry se šifrovacími schématy založenými na blokových šifrách.

I když můžete vždy snadno sestavit proudovou šifru z blokové šifry, je obvykle velmi obtížné postavit nějaký typ konstrukce s blokovým režimem šifrování (jako je například s CBC režimem) z primitivní proudové šifry.

Z této diskuse byste nyní měli pochopit *Obrázek 8*. Poskytuje přehled o symetrických šifrovacích schématech. Používáme tři druhy šifrovacích schémat: primitivní proudové šifry, proudové šifry na bázi blokových šifer a blokové šifry v blokovém režimu (také nazývané „blokové šifry“ na diagramu).

*Obrázek 8: Přehled symetrických šifrovacích schémat*

![Obrázek 8: Přehled symetrických šifrovacích schémat](assets/Figure4-8.webp "Obrázek 8: Přehled symetrických šifrovacích schémat")


## Kódy pro autentizaci zpráv
<chapterId>19fa7c00-db59-56a0-9654-5350a137939d</chapterId>

Šifrování se týká tajnosti. Ale kryptografie se také zabývá širšími tématy, jako je integrita zpráv, autenticita a nedopustitelnost popření. Takzvané **kódy pro autentizaci zpráv** (MACs) jsou symetrické kryptografické schématy, které podporují autenticitu a integritu v komunikaci.

Proč je něco kromě tajnosti potřebné v komunikaci? Předpokládejme, že Bob pošle Alici zprávu pomocí prakticky nelomitelného šifrování. Jakýkoli útočník, který tuto zprávu zachytí, nebude schopen získat žádné významné informace o jejím obsahu. Avšak útočník má stále k dispozici alespoň dva další vektory útoku:

1. Mohla by zachytit šifrovaný text, změnit jeho obsah a poslat upravený šifrovaný text Alici.
2. Mohla by zcela zablokovat Bobovu zprávu a poslat svůj vlastní vytvořený šifrovaný text.

V obou těchto případech by útočník nemusel mít žádné informace o obsahu šifrovaných textů (1) a (2). Ale stále by mohla způsobit významné škody tímto způsobem. Zde se stávají důležitými kódy pro autentizaci zpráv.

Kódy pro autentizaci zpráv jsou volně definovány jako symetrická kryptografická schémata se třemi algoritmy: algoritmus pro generování klíče, algoritmus pro generování tagu a algoritmus pro ověření. Bezpečný MAC zajišťuje, že tagy jsou **existenčně nezfalšovatelné** pro jakéhokoli útočníka - to znamená, že nemohou úspěšně vytvořit tag na zprávu, který ověří, pokud nemají soukromý klíč.

Bob a Alice mohou bojovat proti manipulaci s konkrétní zprávou pomocí MAC. Předpokládejme na okamžik, že jim nezáleží na tajnosti. Chtějí pouze zajistit, že zpráva přijatá Alicí byla skutečně od Boba a nebyla nijak změněna.

Proces je znázorněn na *Obrázku 9*. Pro použití **MAC** (Message Authentication Code, Kód pro autentizaci zpráv), by nejprve vygenerovali soukromý klíč $K$, který je sdílen mezi oběma z nich. Bob vytvoří tag $T$ pro zprávu pomocí soukromého klíče $K$. Poté pošle zprávu i s tagem zprávy Alici. Ona pak může ověřit, že tag skutečně vytvořil Bob, spuštěním soukromého klíče, zprávy a tagu skrze algoritmus pro ověření.

*Obrázek 9: Přehled symetrických šifrovacích schémat*
![Obrázek 9: Přehled schémat symetrického šifrování](assets/Figure4-9.webp "Obrázek 9: Přehled schémat symetrického šifrování")
Díky **existenční nezfalšovatelnosti** útočník nemůže zprávu $M$ nijak změnit ani vytvořit vlastní zprávu s platným tagem. To platí i v případě, že útočník pozoruje tagy mnoha zpráv mezi Bobem a Alicí, které používají stejný soukromý klíč. Nejvíce, co by útočník mohl udělat, je zabránit Alici v přijetí zprávy $M$ (problém, který kryptografie nemůže řešit).

MAC (Message Authentication Code) zaručuje, že zpráva byla skutečně vytvořena Bobem. Tato autentičnost automaticky znamená integritu zprávy – to znamená, pokud Bob vytvořil nějakou zprávu, pak byla ipso facto nezměněna žádným útočníkem. Od tohoto bodu by jakákoli starost o autentizaci měla být automaticky chápána jako starost o integritu.

Přestože jsem v mé diskusi rozlišil mezi autentičností a integritou zprávy, je také běžné používat tyto termíny jako synonyma. Odkazují pak na myšlenku zpráv, které byly vytvořeny konkrétním odesílatelem a nebyly nijak změněny. V tomto duchu se kódy pro autentizaci zpráv často nazývají také **kódy integrity zpráv**.

## Autentizované šifrování
<chapterId>33f2ec9b-9fb4-5c61-8fb4-50836270a144</chapterId>

Typicky byste chtěli zaručit jak tajnost, tak autentičnost v komunikaci, a proto se obvykle používají společně schémata šifrování a MAC.

**Schéma autentizovaného šifrování** je schéma, které kombinuje šifrování s MAC způsobem, který je vysoce bezpečný. Konkrétně musí splňovat standardy pro existenční nezfalšovatelnost, stejně jako velmi silnou představu o tajnosti, konkrétně odolnost vůči **útokům s vybraným šifrotextem**. [7]

Aby bylo schéma šifrování odolné vůči útokům s vybraným šifrotextem, musí splňovat standardy pro **neměnitelnost**: to znamená, že jakákoli úprava šifrotextu útočníkem by měla vést buď k neplatnému šifrotextu, nebo k šifrotextu, který po dešifrování dává text bez jakékoli souvislosti s původním. [8]

Jelikož schéma autentizovaného šifrování zajišťuje, že šifrotext vytvořený útočníkem je vždy neplatný (protože tag nebude ověřen), splňuje standardy pro odolnost vůči útokům s vybraným šifrotextem. Zajímavé je, že lze dokázat, že schéma autentizovaného šifrování lze vždy vytvořit kombinací existenčně nezfalšovatelného MAC a šifrovacího schématu, které splňuje méně silnou představu o bezpečnosti, známou jako **bezpečnost vůči útokům s vybraným otevřeným textem**.

Nebudeme se zabývat všemi detaily konstrukce schémat autentizovaného šifrování. Ale je důležité znát dva detaily jejich konstrukce.

Za prvé, schéma autentizovaného šifrování nejprve zpracuje šifrování a poté vytvoří tag zprávy na šifrotextu. Ukázalo se, že jiné přístupy – jako je kombinování šifrotextu s tagem na otevřeném textu, nebo nejprve vytvoření tagu a poté šifrování jak otevřeného textu, tak tagu – jsou nebezpečné. Kromě toho obě operace mají svůj vlastní náhodně vybraný soukromý klíč, jinak je vaše bezpečnost vážně ohrožena.

Výše uvedený princip se vztahuje obecněji: *vždy byste měli používat rozdílné klíče při kombinování základních kryptografických schémat*.

Schéma autentizovaného šifrování je znázorněno na *Obrázku 10*. Bob nejprve vytvoří šifrotext $C$ ze zprávy $M$ pomocí náhodně vybraného klíče $K_C$. Poté vytvoří tag zprávy $T$ zpracováním šifrotextu a jiného náhodně vybraného klíče $K_T$ prostřednictvím algoritmu pro generování tagu. Oba, šifrotext i tag zprávy, jsou poslány Alici.
Alice nyní nejprve zkontroluje, zda je značka (tag) platná vzhledem k šifrovanému textu $C$ a klíči $K_T$. Pokud je platná, může poté dešifrovat zprávu pomocí klíče $K_C$. Nejenže má jistotu velmi silného pojmu tajnosti v jejich komunikaci, ale také ví, že zprávu vytvořil Bob.
*Obrázek 10: Schéma autentizovaného šifrování*

![Obrázek 10: Schéma autentizovaného šifrování](assets/Figure4-10.webp "Obrázek 10: Schéma autentizovaného šifrování")

Jak se vytvářejí MAC (Message Authentication Codes)? Ačkoliv lze MAC vytvořit několika metodami, běžným a efektivním způsobem jejich vytváření je prostřednictvím **kryptografických hašovacích funkcí**.

Kryptografické hašovací funkce podrobněji představíme v *Kapitole 6*. Prozatím stačí vědět, že **hašovací funkce** je efektivně vypočitatelná funkce, která přijímá vstupy libovolné velikosti a vrací výstupy pevné délky. Například oblíbená hašovací funkce **SHA-256** (secure hash algorithm 256) vždy generuje 256-bitový výstup bez ohledu na velikost vstupu. Některé hašovací funkce, jako je SHA-256, mají užitečné aplikace v kryptografii.

Nejběžnějším typem značky vytvořené s kryptografickou hašovací funkcí je **hašovací zpráva autentizační kód** (HMAC). Proces je znázorněn na *Obrázku 11*. Strana vytvoří z privátního klíče $K$ dvě odlišné klíče, vnitřní klíč $K_1$ a vnější klíč $K_2$. Čistý text $M$ nebo šifrovaný text $C$ je poté zahašován společně s vnitřním klíčem. Výsledek $T'$ je následně zahašován s vnějším klíčem, aby se vytvořila značka zprávy $T$.

Existuje paleta hašovacích funkcí, které lze použít k vytvoření HMAC. Nejčastěji používanou hašovací funkcí je SHA-256.

*Obrázek 11: HMAC*

![Obrázek 11: HMAC](assets/Figure4-11.webp "Obrázek 11: HMAC")

**Poznámky:**

[7] Konkrétní výsledky diskutované v této sekci jsou z Katz a Lindell, str. 131–47.

[8] Technicky je definice útoků s vybraným šifrovaným textem odlišná od pojmu neovlivnitelnosti. Ale můžete ukázat, že tyto dvě pojmy bezpečnosti jsou ekvivalentní.

## Bezpečné komunikační relace
<chapterId>c7f7dcd3-bbed-53ed-a43d-039da0f180c5</chapterId>

Předpokládejme, že dvě strany jsou v komunikační relaci, takže si posílají zprávy tam a zpět.

Schéma autentizovaného šifrování umožňuje příjemci zprávy ověřit, že byla vytvořena jejím partnerem v komunikační relaci (pokud neunikl privátní klíč). To funguje dostatečně dobře pro jednu zprávu. Typicky však dvě strany posílají zprávy tam a zpět v komunikační relaci. A v tomto nastavení schéma autentizovaného šifrování, jak je popsáno v předchozí sekci, nedokáže poskytnout bezpečnost.

Hlavním důvodem je, že schéma autentizovaného šifrování neposkytuje žádné záruky, že zpráva byla skutečně také odeslána agentem, který ji vytvořil během komunikační relace. Zvažte následující tři vektory útoku:

1. **Útok opakováním**: Útočník znovu pošle šifrovaný text a značku, kterou zachytil mezi dvěma stranami v dřívějším bodě.
2. **Útok změnou pořadí**: Útočník zachytí dvě zprávy v různých časech a pošle je příjemci v opačném pořadí.
3. **Reflexní útok**: Útočník pozoruje zprávu poslanou od A k B a také pošle tu zprávu A.

Ačkoliv útočník nemá znalost šifrovaného textu a nemůže vytvářet padělané šifrované texty, výše uvedené útoky mohou stále způsobit významné škody v komunikaci.
Předpokládejme například, že konkrétní zpráva mezi dvěma stranami zahrnuje převod finančních prostředků. Útok typu replay by mohl způsobit, že se prostředky převedou podruhé. Základní schéma autentizovaného šifrování nemá proti takovým útokům žádnou obranu.
Naštěstí se tyto druhy útoků dají snadno zmírnit v komunikační seanci použitím **identifikátorů** a **indikátorů relativního času**.

Identifikátory lze přidat do otevřeného textu zprávy před šifrováním. To by zabránilo jakýmkoli útokům odrazu. Indikátor relativního času může například být sériové číslo v konkrétní komunikační seanci. Každá strana přidá k zprávě před šifrováním sériové číslo, takže příjemce ví, v jakém pořadí byly zprávy odeslány. To eliminuje možnost útoků přeuspořádáním. Také eliminuje útoky typu replay. Jakákoli zpráva, kterou útočník pošle, bude mít staré sériové číslo a příjemce bude vědět, že zprávu znovu nezpracovávat.

Abychom ilustrovali, jak fungují zabezpečené komunikační seance, představme si znovu Alici a Boba. Posílají si celkem čtyři zprávy tam a zpět. Níže v *Obrázku 11* můžete vidět, jak by fungovalo schéma autentizovaného šifrování s identifikátory a sériovými čísly.

Komunikační seance začíná tím, že Bob pošle Alici šifrovaný text $C_{0,B}$ s tagem zprávy $T_{0,B}$. Šifrovaný text obsahuje zprávu, stejně jako identifikátor (BOB) a sériové číslo (0). Tag $T_{0,B}$ je vytvořen nad celým šifrovaným textem. V jejich následné komunikaci Alice a Bob tento protokol udržují, aktualizují pole podle potřeby.

*Obrázek 12: Zabezpečená komunikační seance*

![Obrázek 12: Zabezpečená komunikační seance](assets/Figure4-12.webp "Obrázek 12: Zabezpečená komunikační seance")

# RC4 a AES
<partId>a48c4a7d-0a41-523f-a4ab-1305b4430324</partId>

## Proudová šifra RC4
<chapterId>5caec5bd-5a77-56c9-b5e6-1e86f0d294aa</chapterId>

V této kapitole se budeme zabývat podrobnostmi šifrovacího schématu s moderní proudovou šifrou, RC4 (neboli "Rivestova šifra 4"), a moderní blokovou šifrou, AES. Ačkoliv šifra RC4 přišla o přízeň jako metoda šifrování, AES je standardem pro moderní symetrické šifrování. Tyto dva příklady by měly poskytnout lepší představu o tom, jak symetrické šifrování funguje "pod kapotou".

___

Abychom měli představu o tom, jak fungují moderní pseudonáhodné proudové šifry, zaměřím se na proudovou šifru RC4. Jedná se o pseudonáhodnou proudovou šifru, která byla používána v bezpečnostních protokolech bezdrátových přístupových bodů WEP a WAP, stejně jako v TLS. Jelikož má RC4 mnoho prokázaných slabostí, přišla o přízeň. Ve skutečnosti Internet Engineering Task Force nyní zakazuje používání sad RC4 klienty a serverovými aplikacemi ve všech instancích TLS. Přesto slouží dobře jako příklad ilustrující, jak funguje primitivní proudová šifra.

Začneme tím, že nejprve ukážu, jak zašifrovat otevřený text zprávy s dětskou šifrou RC4. Předpokládejme, že náš otevřený text zprávy je „SOUP.“ Šifrování s naší dětskou šifrou RC4 pak probíhá ve čtyřech krocích.

### Krok 1
Nejprve definujte pole **S** s $S[0] = 0$ až $S[7] = 7$. Pole zde jednoduše znamená proměnlivou kolekci hodnot organizovanou podle indexu, které se v některých programovacích jazycích říká také seznam (např. Python). V tomto případě index běží od 0 do 7 a hodnoty také běží od 0 do 7. Takže **S** vypadá takto:
- $S = [0, 1, 2, 3, 4, 5, 6, 7]$

Hodnoty zde nejsou ASCII čísla, ale desítkové reprezentace hodnot 1-bajtových řetězců. Takže hodnota 2 by odpovídala $0000 \ 0011$. Délka pole **S** je tedy 8 bajtů.

### Krok 2

Za druhé, definujte klíčové pole **K** o délce 8 bajtů výběrem klíče mezi 1 a 8 bajty (bez možnosti zlomků bajtů). Jelikož každý bajt má 8 bitů, můžete pro každý bajt vašeho klíče vybrat libovolné číslo mezi 0 a 255.

Předpokládejme, že si vybereme náš klíč **k** jako $[14, 48, 9]$, takže má délku 3 bajty. Každý index našeho klíčového pole je poté nastaven podle desítkové hodnoty pro daný prvek klíče, v pořadí. Pokud projdete celým klíčem, začněte znovu od začátku, dokud nevyplníte 8 slotů klíčového pole. Naše klíčové pole je tedy následující:

- $K = [14, 48, 9, 14, 48, 9, 14, 48]$

### Krok 3

Za třetí, transformujeme pole **S** pomocí klíčového pole **K** v procesu známém jako **plánování klíče**. Proces je následující v pseudokódu:

- Vytvořte proměnné **j** a **i**
- Nastavte proměnnou $j = 0$
- Pro každé $i$ od 0 do 7:
    - Nastavte $j = (j + S[i] + K[i]) \mod 8$
    - Vyměňte $S[i]$ a $S[j]$

Transformace pole **S** je zachycena v *Tabulce 1*.

Na začátku můžete vidět počáteční stav **S** jako $[0, 1, 2, 3, 4, 5, 6, 7]$ s počáteční hodnotou 0 pro **j**. To bude transformováno pomocí klíčového pole $[14, 48, 9, 14, 48, 9, 14, 48]$.

Cyklus for začíná s $i = 0$. Podle našeho pseudokódu výše se nová hodnota **j** stane 6 ($j = (j + S[0] + K[0]) \mod 8 = (0 + 0 + 14) \mod 8 = 6 \mod 8$). Výměnou $S[0]$ a $S[6]$, stav **S** po 1 kole se stane $[6, 1, 2, 3, 4, 5, 0, 7]$.
V dalším řádku, $i = 1$. Projdeme znovu cyklem for, **j** získá hodnotu 7 ($j = (j + S[1] + K[1]) \mod 8 = (6 + 1 + 48) \mod 8 = 55 \mod 8 = 7 \mod 8$). Výměnou $S[1]$ a $S[7]$ ze současného stavu **S**, $[6, 1, 2, 3, 4, 5, 0, 7]$, dostaneme $[6, 7, 2, 3, 4, 5, 0, 1]$ po druhém kole.
Tento proces pokračujeme, dokud nevytvoříme konečný řádek na spodku pro pole **S**, $[6, 4, 1, 0, 3, 7, 5, 2]$.

*Tabulka 1: Tabulka plánování klíče*

| Kolo    | i   | j   |     | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| ------- | --- | --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|         |     |     |     |      |      |      |      |      |      |      |      |
| Počáteční |     | 0   |     | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    |
| 1       | 0   | 6   |     | 6    | 1    | 2    | 3    | 4    | 5    | 0    | 7    |
| 2       | 1   | 7   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 3       | 2   | 2   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 4       | 3   | 3   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 5       | 4   | 3   |     | 6    | 7    | 2    | 0    | 3    | 5    | 4    | 1    |
| 6       | 5   | 6   |     | 6    | 4    | 2    | 0    | 3    | 7    | 5    | 1    |
| 7       | 6   | 1   |     | 6    | 4    | 2    | 0    | 3    | 7    | 5    | 2    |
| 8       | 7   | 2   |     | 6    | 4    | 1    | 0    | 3    | 7    | 5    | 2    |

### Krok 4
Jako čtvrtý krok vytváříme **keystream**. Jedná se o pseudonáhodný řetězec o délce rovnající se zprávě, kterou chceme odeslat. Tento bude použit k zašifrování původní zprávy „SOUP.“ Jelikož musí být keystream stejně dlouhý jako zpráva, potřebujeme jeden, který má 4 bajty.
Keystream je vytvořen následujícím pseudokódem:

- Vytvořte proměnné **j**, **i** a **t**.
- Nastavte $j = 0$.
- Pro každé $i$ z otevřeného textu, začínajíc s $i = 1$ a pokračující až do $i = 4$, je každý bajt keystreamu vytvořen následovně:
    - $j = (j + S[i]) \mod 8$
    - Vyměňte $S[i]$ a $S[j]$.
    - $t = (S[i] + S[j]) \mod 8$
    - $i$-tý bajt keystreamu = $S[t]$

Výpočty můžete sledovat v *Tabulce 2*.

Počáteční stav **S** je $S = [6, 4, 1, 0, 3, 7, 5, 2]$. Nastavením $i = 1$, hodnota **j** se stane 4 ($j = (j + S[i]) \mod 8 = (0 + 4) \mod 8 = 4$). Poté vyměníme $S[1]$ a $S[4]$, čímž vytvoříme transformaci **S** ve druhém řádku, $[6, 3, 1, 0, 4, 7, 5, 2]$. Hodnota **t** je poté 7 ($t = (S[i] + S[j]) \mod 8 = (3 + 4) \mod 8 = 7$). Nakonec je bajt pro keystream $S[7]$, neboli 2.

Poté pokračujeme ve vytváření dalších bajtů, dokud nemáme následující čtyři bajty: 2, 6, 3 a 7. Každý z těchto bajtů pak může být použit k zašifrování každého písmene otevřeného textu, "SOUP".

Na začátku, použitím ASCII tabulky, můžeme vidět, že „SOUP“ zakódované desítkovými hodnotami odpovídajících bajtových řetězců je „83 79 85 80“. Kombinace s keystreamem „2 6 3 7“ dává „85 85 88 87“, což zůstává stejné i po operaci modulo 256. V ASCII, šifrovaný text „85 85 88 87“ odpovídá „UUXW“.

Co se stane, pokud by slovo k zašifrování bylo delší než pole **S**? V tom případě se pole **S** jen transformuje tímto způsobem zobrazeným výše pro každý bajt **i** otevřeného textu, dokud nemáme počet bajtů v keystreamu rovnající se počtu písmen v otevřeném textu.

*Tabulka 2: Generování keystreamu*

| i   | j   | t   | Keystream | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| --- | --- | --- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|     | 0   |     |           | 6    | 4    | 1    | 0    | 3    | 7    | 5    | 2    || 1   | 4   | 7   | 2         | 6    | 3    | 1    | 0    | 4    | 7    | 5    | 2    |
| 2   | 5   | 0   | 6         | 6    | 3    | 7    | 0    | 4    | 1    | 5    | 2    |
| 3   | 5   | 1   | 3         | 6    | 3    | 7    | 1    | 4    | 0    | 5    | 2    |
| 4   | 1   | 7   | 2         | 6    | 4    | 7    | 1    | 3    | 0    | 5    | 2    |

Příklad, který jsme právě probírali, je pouze zjednodušená verze **RC4 stream cipher**. Skutečný RC4 stream cipher má pole **S** o délce 256 bajtů, nikoli 8 bajtů, a klíč, který může být mezi 1 a 256 bajty, nikoli mezi 1 a 8 bajty. Pole klíče a keystreamy jsou poté vytvářeny s ohledem na 256bajtovou délku pole **S**. Výpočty se stávají mnohem složitějšími, ale principy zůstávají stejné. Použitím stejného klíče, [14,48,9], se standardním šifrováním RC4 je šifrovaná zpráva "SOUP" zašifrována jako 67 02 ed df ve formátu hexadecimálních čísel.

Streamová šifra, ve které se keystream aktualizuje nezávisle na otevřeném textu nebo šifrovaném textu, je **synchronní streamová šifra**. Keystream je závislý pouze na klíči. Zřejmě, RC4 je příkladem synchronní streamové šifry, protože keystream nemá žádný vztah k otevřenému nebo šifrovanému textu. Všechny naše primitivní streamové šifry zmíněné v předchozí kapitole, včetně posunové šifry, šifry Vigenère a jednorázového bloku, byly také synchronního typu.

Naopak, **asynchronní streamová šifra** má keystream, který je produkován jak klíčem, tak předchozími prvky šifrovaného textu. Tento typ šifry se také nazývá **samo-synchronizující šifra**.

Důležité je, že keystream produkovaný s RC4 by měl být považován za jednorázový blok, a nemůžete produkovat keystream přesně stejným způsobem příště. Spíše než měnit klíč pokaždé, praktické řešení je kombinovat klíč s **nonce** pro vytvoření bytestreamu.

## AES s 128bitovým klíčem
<chapterId>0b30886f-e620-5b8d-807b-9d84685ca8ff</chapterId>

Jak bylo zmíněno v předchozí kapitole, Národní institut pro standardy a technologie (NIST) mezi lety 1997 a 2000 uspořádal soutěž, aby určil nový standard symetrického šifrování. Šifra **Rijndael** se stala vítězným příspěvkem. Název je slovní hříčkou na jména belgických tvůrců, Vincenta Rijmena a Joana Daemena.
Šifra Rijndael je **bloková šifra**, což znamená, že existuje základní algoritmus, který lze použít s různými specifikacemi pro délky klíčů a velikosti bloků. Poté ji můžete použít s různými režimy provozu pro konstrukci šifrovacích schémat.
Výbor pro soutěž NIST přijal omezenou verzi šifry Rijndael – konkrétně takovou, která vyžaduje 128bitové velikosti bloků a délky klíčů 128 bitů, 192 bitů nebo 256 bitů – jako součást **Advanced Encryption Standard (AES)**. Tato omezená verze šifry Rijndael může být také použita v několika režimech provozu. Specifikace standardu je známá jako **Advanced Encryption Standard (AES)**.

Abych ukázal, jak šifra Rijndael funguje, jádro AES, ilustruji proces šifrování s 128bitovým klíčem. Velikost klíče má vliv na počet kol probíhajících pro každý blok šifrování. Pro 128bitové klíče je vyžadováno 10 kol. Pro 192 bitů a 256 bitů by to bylo 12 a 14 kol.

Kromě toho předpokládám, že AES je použit v **ECB režimu**. To činí výklad trochu jednodušším a pro algoritmus Rijndael to není důležité. Jistě, ECB režim není v praxi bezpečný, protože vede k deterministickému šifrování. Nejčastěji používaným bezpečným režimem s AES je **CBC** (Cipher Block Chaining).

Pojmenujme klíč $K_0$. Konstrukce s výše uvedenými parametry pak vypadá jako na *Obrázku 1*, kde $M_i$ označuje část otevřeného textu o velikosti 128 bitů a $C_i$ část šifrovaného textu o velikosti 128 bitů. Pokud nelze otevřený text rovnoměrně rozdělit podle velikosti bloku, přidá se k poslednímu bloku otevřeného textu doplnění.

*Obrázek 1: AES-ECB s 128bitovým klíčem*

![Obrázek 1: AES-ECB s 128bitovým klíčem](assets/Figure5-1.webp "Obrázek 1: AES-ECB s 128bitovým klíčem")

Každý 128bitový blok textu prochází v šifrovacím schématu Rijndael deseti koly. To vyžaduje samostatný kolo klíč pro každé kolo ($K_1$ až $K_{10}$). Tyto jsou vyprodukovány pro každé kolo z původního 128bitového klíče $K_0$ pomocí **algoritmu rozšíření klíče**. Tedy pro každý blok textu, který má být zašifrován, použijeme původní klíč $K_0$ stejně jako deset samostatných kolo klíčů. Poznamenejme, že tyto stejné 11 klíčů se používá pro každý 128bitový blok otevřeného textu, který vyžaduje šifrování.

Algoritmus rozšíření klíče je dlouhý a složitý. Procházení jím má malý didaktický přínos. Můžete si algoritmus rozšíření klíče prohlédnout sami, pokud chcete. Jakmile jsou kolo klíče vyprodukovány, šifra Rijndael manipuluje s prvním 128bitovým blokem otevřeného textu, $M_1$, jak je vidět na *Obrázku 2*. Nyní projdeme těmito kroky.

*Obrázek 2: Manipulace s $M_1$ pomocí šifry Rijndael:*

**Kolo 0:**
- XOR $M_1$ a $K_0$ pro vytvoření $S_0$

---

**Kolo n pro n = {1,...,9}:**
- XOR $S_{n-1}$ a $K_n$
- Substituce bajtů
- Posun řádků
- Míchání sloupců
- XOR $S$ a $K_n$ pro vytvoření $S_n$

---

**Kolo 10:**
- XOR $S_9$ a $K_{10}$ - Substituce bytů
- Posun řádků
- XOR $S$ a $K_{10}$ pro vytvoření $S_{10}$
- $S_{10}$ = $C_1$

### Kolo 0

Kolo 0 šifry Rijndael je přímočaré. Pole $S_0$ je vytvořeno operací XOR mezi 128-bitovým otevřeným textem a soukromým klíčem. To znamená,

- $S_0 = M_1 \oplus K_0$

### Kolo 1

V kole 1 je pole $S_0$ nejprve zkombinováno s klíčem kola $K_1$ pomocí operace XOR. To vytvoří nový stav $S$.

Za druhé, je provedena operace **substituce bytů** na aktuálním stavu $S$. Funguje tak, že vezme každý byt z 16-bytového pole $S$ a nahradí ho bytem z pole nazývaného **Rijndaelova S-box**. Každý byt má unikátní transformaci a jako výsledek je vytvořen nový stav $S$. Rijndaelův S-box je zobrazen v *Obrázku 3*.

*Obrázek 3: Rijndaelův S-Box*

|     | 00  | 01  | 02  | 03  | 04  | 05  | 06  | 07  | 08  | 09  | 0A  | 0B  | 0C  | 0D  | 0E  | 0F  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00  | 63  | 7C  | 77  | 7B  | F2  | 6B  | 6F  | C5  | 30  | 01  | 67  | 2B  | FE  | D7  | AB  | 76  |
| 10  | CA  | 82  | C9  | 7D  | FA  | 59  | 47  | F0  | AD  | D4  | A2  | AF  | 9C  | A4  | 72  | C0  |
| 20  | B7  | FD  | 93  | 26  | 36  | 3F  | F7  | CC  | 34  | A5  | E5  | F1  | 71  | D8  | 31  | 15  |
| 30  | 04  | C7  | 23  | C3  | 18  | 96  | 05  | 9A  | 07  | 12  | 80  | E2  | EB  | 27  | B2  | 75  |
| 40  | 09  | 83  | 2C  | 1A  | 1B  | 6E  | 5A  | A0  | 52  | 3B  | D6  | B3  | 29  | E3  | 2F  | 84  |
Tento text představuje hexadecimální data, která jsou typicky používána v kontextu programování, kryptografie, nebo při analýze dat. Vzhledem k povaze a specifičnosti obsahu, tento typ materiálu obvykle vyžaduje zachování původní formy bez překladu, protože se jedná o univerzální jazyk používaný v technických a vědeckých oborech po celém světě. Překlad nebo změna formátu by mohla vést k zásadním chybám v interpretaci dat.
| F0  | 8C  | A1  | 89  | 0D  | BF  | E6  | 42  | 68  | 41  | 99  | 2D  | 0F  | B0  | 54  | BB  | 16  |

Tato S-Box je jedno z míst, kde se v šifře Rijndael uplatňuje abstraktní algebra, konkrétně **Galoisovy pole**.

Začneme tím, že každý možný bajtový prvek 00 až FF definujeme jako 8-bitový vektor. Každý takový vektor je prvkem **Galoisova pole GF(2^8)**, kde ireducibilní polynom pro operaci modulo je $x^8 + x^4 + x^3 + x + 1$. Galoisovo pole s těmito specifikacemi se také nazývá **Rijndaelovo konečné pole**.

Dále pro každý možný prvek v poli vytvoříme tzv. **Nybergův S-Box**. V tomto boxu je každý bajt zobrazen na svůj **multiplikativní inverz** (tj. tak, aby jejich součin byl roven 1). Tyto hodnoty z Nybergova S-boxu poté zobrazíme do Rijndaelova S-Boxu pomocí **afinní transformace**.

Třetí operace na poli **S** je operace **posunutí řádků**. Bere stav **S** a vypíše všech šestnáct bajtů v matici. Vyplnění matice začíná vlevo nahoře a pokračuje tak, že jde odshora dolů a poté, jakmile je sloupec vyplněn, posune se o jeden sloupec doprava a nahoru.

Jakmile je matice **S** sestavena, čtyři řádky se posunou. První řádek zůstává stejný. Druhý řádek se posune o jedno doleva. Třetí se posune o dva doleva. Čtvrtý se posune o tři doleva. Příklad procesu je uveden na *Obrázku 4*. Původní stav **S** je zobrazen nahoře a výsledný stav po operaci posunutí řádků je zobrazen níže.

*Obrázek 4: Operace posunutí řádků*

| F1   | A0   | B1   | 23   |
|------|------|------|------|
| 59   | EF   | 09   | 82   |
| 97   | 01   | B0   | CC   |
| D4   | 72   | 04   | 21   |

| F1   | A0   | B1   | 23   |
|------|------|------|------|
| EF   | 09   | 82   | 59   |
| B0   | CC   | 97   | 01   |
| 21   | D4   | 72   | 04   |


Ve čtvrtém kroku se opět objevují **Galoisova pole**. Začneme tím, že každý sloupec matice **S** se vynásobí sloupcem 4 x 4 matice viděné na *Obrázku 5*. Ale místo běžného násobení matic jde o vektorové násobení **modulo ireducibilní polynom**, $x^8 + x^4 + x^3 + x + 1$. Výsledné koeficienty vektoru reprezentují jednotlivé bity bajtu.

*Obrázek 5: Matice pro míchání sloupců*

| 02   | 03   | 01   | 01   |
|------|------|------|------|
| 01   | 02   | 03   | 01   |
| 01   | 01   | 02   | 03   || 03   | 01   | 01   | 02   |

Násobení prvního sloupce matice **S** s maticí 4 x 4 výše vede k výsledku v *Obrázku 6*.

*Obrázek 6: Násobení prvního sloupce:*

$$
\begin{matrix}
02 \cdot F1 + 03 \cdot EF + 01 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 02 \cdot EF + 03 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 01 \cdot EF + 02 \cdot B0 + 03 \cdot 21 \\
03 \cdot F1 + 01 \cdot EF + 01 \cdot B0 + 02 \cdot 21
\end{matrix}
$$

Jako další krok by všechny členy v matici měly být převedeny na polynomy. Například F1 reprezentuje 1 byte a stane se $x^7 + x^6 + x^5 + x^4 + 1$, a 03 reprezentuje 1 byte a stane se $x + 1$.

Všechny násobení jsou poté provedeny **modulo** $x^8 + x^4 + x^3 + x + 1$. To vede k součtu čtyř polynomů v každé ze čtyř buněk sloupce. Po provedení těchto sčítání **modulo 2** skončíte se čtyřmi polynomy. Každý z těchto polynomů reprezentuje 8-bitový řetězec, nebo 1 byte, **S**. Tyto výpočty zde na matici v *Obrázku 6* nebudeme provádět, protože jsou rozsáhlé.

Jakmile byl první sloupec zpracován, ostatní tři sloupce matice **S** jsou zpracovány stejným způsobem. Nakonec to vede k matici se šestnácti byty, která může být převedena na pole.

Jako poslední krok je pole **S** opět kombinováno s klíčem kola v operaci **XOR**. To produkuje stav $S_1$. To znamená,

- $S_1 = S \oplus K_0$

### Kola 2 až 10

Kola 2 až 9 jsou pouze opakováním kola 1, *mutatis mutandis*. Poslední kolo vypadá velmi podobně jako předchozí kola, s výjimkou toho, že krok **mix columns** je vynechán. To znamená, že kolo 10 je provedeno následovně:

- $S_9 \oplus K_{10}$
- Substituce bytů
- Posun řádků
- $S_{10} = S \oplus K_{10}$

Stav $S_{10}$ je nyní nastaven na $C_1$, prvních 128 bitů šifrovaného textu. Pokračováním přes zbývající 128-bitové bloky otevřeného textu získáte celý šifrovaný text **C**.

### Operace šifry Rijndael

Jaké jsou důvody různých operací viděných v šifře Rijndael?

Bez vstupu do detailů jsou šifrovací schémata hodnocena na základě míry, jakou vytvářejí zmatek a rozptýlení. Pokud má šifrovací schéma vysokou míru **zmatku**, znamená to, že šifrovaný text vypadá drasticky jinak než otevřený text. Pokud má šifrovací schéma vysokou míru **rozptýlení**, znamená to, že jakákoli malá změna v otevřeném textu produkuje drasticky odlišný šifrovaný text.
Důvodem pro operace za šifrou Rijndael je, že produkují vysoký stupeň zmatení a rozptýlení. Zmatení je vytvořeno operací substituce bytů, zatímco rozptýlení je vytvořeno operacemi posunu řádků a míchání sloupců.
# Asymetrická kryptografie
<partId>868bd9dd-6e1c-5ea9-9ece-54affc13ba05</partId>

## Problém distribuce a správy klíčů
<chapterId>1bb651ba-689a-5a89-a7d3-0b9cc3b694f7</chapterId>

Stejně jako u symetrické kryptografie, asymetrické schéma může být použito k zajištění tajnosti a autentizace. Na rozdíl od toho však tato schémata používají dva klíče místo jednoho: soukromý a veřejný klíč.

Naše zkoumání začíná objevem asymetrické kryptografie, zejména problémy, které ji iniciovaly. Dále diskutujeme, jak na vysoké úrovni fungují asymetrická schémata pro šifrování a autentizaci. Poté představíme hašovací funkce, které jsou klíčové pro pochopení asymetrických schémat autentizace a mají také význam v jiných kryptografických kontextech, jako jsou například hašovací zprávy autentizační kódy, o kterých jsme diskutovali v kapitole 4.

___

Předpokládejme, že Bob chce koupit nový deštník od Jim’s Sporting Goods, online prodejce sportovního zboží s miliony zákazníků v Severní Americe. Bude to jeho první nákup od nich a chce použít svou kreditní kartu. Takže Bob nejprve musí vytvořit účet u Jim’s Sporting Goods, což vyžaduje poslání osobních údajů, jako je jeho adresa a informace o kreditní kartě. Poté může projít kroky potřebnými k nákupu deštníku.

Bob a Jim’s Sporting Goods budou chtít zajistit, aby jejich komunikace byla během tohoto procesu bezpečná, vzhledem k tomu, že Internet je otevřený komunikační systém. Budou chtít zajistit, například, aby žádný potenciální útočník nemohl zjistit Bobovy údaje o kreditní kartě a adrese, a aby žádný potenciální útočník nemohl opakovat jeho nákupy nebo vytvářet falešné v jeho jménu.

Pokročilé schéma autentizovaného šifrování, jak bylo diskutováno v předchozí kapitole, by určitě mohlo zabezpečit komunikaci mezi Bobem a Jim’s Sporting Goods. Ale jsou zde jasně praktické překážky pro implementaci takového schématu.

Abychom ilustrovali tyto praktické překážky, předpokládejme, že žijeme ve světě, ve kterém existují pouze nástroje symetrické kryptografie. Co by Jim’s Sporting Goods a Bob mohli poté udělat, aby zajistili bezpečnou komunikaci?

Za těchto okolností by čelili značným nákladům na bezpečnou komunikaci. Jelikož Internet je otevřený komunikační systém, nemohou si prostě vyměnit sadu klíčů přes něj. Proto by Bob a zástupce pro Jim’s Sporting Goods museli provést výměnu klíčů osobně.

Jednou z možností je, že Jim’s Sporting Goods vytvoří speciální místa pro výměnu klíčů, kde Bob a další noví zákazníci mohou získat sadu klíčů pro bezpečnou komunikaci. To by samozřejmě přineslo značné organizační náklady a výrazně by snížilo efektivitu, s jakou noví zákazníci mohou provádět nákupy.

Alternativně může Jim’s Sporting Goods poslat Bobovi pár klíčů prostřednictvím vysoce důvěryhodného kurýra. To je pravděpodobně efektivnější než organizování míst pro výměnu klíčů. Ale stále by to přineslo značné náklady, zejména pokud mnoho zákazníků provede pouze jeden nebo několik nákupů.

Dále, symetrické schéma pro autentizované šifrování také nutí Jim’s Sporting Goods uchovávat oddělené sady klíčů pro všechny jejich zákazníky. To by byla významná praktická výzva pro tisíce zákazníků, natož pro miliony.
Abychom pochopili tento poslední bod, představme si, že Jim’s Sporting Goods poskytuje každému zákazníkovi stejný pár klíčů. To by umožnilo každému zákazníkovi – nebo komukoli jinému, kdo by se mohl k tomuto páru klíčů dostat – číst a dokonce manipulovat se všemi komunikacemi mezi Jim’s Sporting Goods a jeho zákazníky. Pak byste stejně dobře mohli v komunikaci vůbec nepoužívat kryptografii.

Opakování sady klíčů i pro některé zákazníky je hrozná bezpečnostní praxe. Jakýkoli potenciální útočník by se mohl pokusit využít této vlastnosti schématu (pamatujte, že se předpokládá, že útočníci znají vše o schématu kromě klíčů, v souladu s Kerckhoffsovým principem).

Takže Jim’s Sporting Goods by musel uchovávat pár klíčů pro každého zákazníka, bez ohledu na to, jak jsou tyto páry klíčů distribuovány. To jasně představuje několik praktických problémů.

- Jim’s Sporting Goods by musel uchovávat miliony párů klíčů, jeden set pro každého zákazníka.
- Tyto klíče by musely být řádně zabezpečeny, jelikož by byly jistým cílem pro hackery. Jakékoli porušení bezpečnosti by vyžadovalo opakování nákladných výměn klíčů, buď na speciálních místech pro výměnu klíčů nebo kurýrem.
- Jakýkoli zákazník Jim’s Sporting Goods by musel doma bezpečně uchovávat pár klíčů. Dojde k ztrátám a krádežím, což bude vyžadovat opakování výměn klíčů. Zákazníci by také museli projít tímto procesem pro jakékoli jiné online obchody nebo jiné typy entit, se kterými chtějí komunikovat a obchodovat přes internet.

Tyto dva hlavní problémy, které byly právě popsány, byly do konce 70. let velmi základními obavami. Byly známé jako **problém distribuce klíčů** a **problém správy klíčů**.

Tyto problémy samozřejmě vždy existovaly a často v minulosti způsobovaly bolesti hlavy. Vojenské síly by například musely neustále distribuovat knihy s klíči pro bezpečnou komunikaci personálu v terénu za velkých rizik a nákladů. Ale tyto problémy se zhoršovaly, protože svět se stále více přesouval do éry dlouhodobé digitální komunikace, zejména pro nevládní subjekty.

Pokud by tyto problémy nebyly vyřešeny v 70. letech, efektivní a bezpečné nakupování v Jim’s Sporting Goods by pravděpodobně neexistovalo. Ve skutečnosti by většina našeho moderního světa s praktickým a bezpečným e-mailingem, online bankovnictvím a nakupováním pravděpodobně byla jen vzdálenou fantazií. Něco, co by se i vzdáleně podobalo Bitcoinu, by vůbec nemohlo existovat.

Tak co se stalo v 70. letech? Jak je možné, že můžeme okamžitě provádět nákupy online a bezpečně procházet World Wide Web? Jak je možné, že můžeme okamžitě posílat Bitcoiny po celém světě z našich chytrých telefonů?

## Nové směry v kryptografii
<chapterId>7a9dd9a3-496e-5f9d-93e0-b5028a7dd0f1</chapterId>

V 70. letech problémy s distribucí a správou klíčů upoutaly pozornost skupiny amerických akademických kryptografů: Whitfielda Diffieho, Martina Hellmana a Ralpha Merkleho. Navzdory vážnému skepticismu většiny svých kolegů se odhodlali najít řešení.

Alespoň jedním hlavním motivem jejich snažení byla předvídavost, že otevřená počítačová komunikace bude mít hluboký vliv na náš svět. Jak Diffie a Hellman poznamenávají v roce 1976,
Vývoj počítačem řízených komunikačních sítí slibuje snadný a levný kontakt mezi lidmi nebo počítači na opačných stranách světa, nahrazující většinu poštovních zásilek a mnoho cest telekomunikacemi. Pro mnoho aplikací musí být tyto kontakty zabezpečeny jak proti odposlechu, tak proti vkládání nelegitimních zpráv. V současné době však řešení bezpečnostních problémů výrazně zaostává za ostatními oblastmi komunikační technologie. *Současná kryptografie není schopna splnit požadavky, protože její použití by uživatelům systému uvalilo takové nepříjemnosti, že by eliminovalo mnoho výhod teleprocesingu.* [1]
Vytrvalost Diffieho, Hellmana a Merkleho se vyplatila. První publikace jejich výsledků byla článek od Diffieho a Hellmana v roce 1976 s názvem „New Directions in Cryptography.“ V něm představili dva originální způsoby, jak řešit problémy s distribucí klíčů a správou klíčů.

První řešení, které nabídli, byl protokol pro vzdálenou *výměnu klíčů*, tedy soubor pravidel pro výměnu jednoho nebo více symetrických klíčů přes nezabezpečený komunikační kanál. Tento protokol je nyní známý jako *výměna klíčů Diffie-Hellman* nebo *výměna klíčů Diffie-Hellman-Merkle*. [2]

Při výměně klíčů Diffie-Hellman nejprve dvě strany veřejně vymění nějaké informace přes nezabezpečený kanál, jako je Internet. Na základě těchto informací pak nezávisle vytvoří symetrický klíč (nebo pár symetrických klíčů) pro zabezpečenou komunikaci. Ačkoli obě strany vytvářejí své klíče nezávisle, veřejně sdílené informace zajišťují, že tento proces vytváření klíčů přinese pro obě strany stejný výsledek.

Důležité je, že ačkoli může kdokoli pozorovat informace, které jsou veřejně vyměňovány stranami přes nezabezpečený kanál, pouze dvě strany zapojené do výměny informací mohou z těchto informací vytvořit symetrické klíče.

To samozřejmě zní naprosto protiintuitivně. Jak mohou dvě strany veřejně vyměňovat nějaké informace, které by umožnily pouze jim vytvořit symetrické klíče z nich? Proč by kdokoli jiný, kdo pozoruje výměnu informací, nemohl vytvořit stejné klíče?

To se opírá o nějakou krásnou matematiku, samozřejmě. Výměna klíčů Diffie-Hellman funguje prostřednictvím jednosměrné funkce s pastí. Pojďme diskutovat význam těchto dvou termínů postupně.

Předpokládejme, že máte nějakou funkci $f(x)$ a výsledek $f(a) = y$, kde $a$ je konkrétní hodnota pro $x$. Říkáme, že $f(x)$ je **jednosměrná funkce**, pokud je snadné vypočítat hodnotu $y$ při znalosti $a$ a $f(x)$, ale je výpočetně neuskutečnitelné vypočítat hodnotu $a$ při znalosti $y$ a $f(x)$. Název **jednosměrná funkce** samozřejmě pramení z faktu, že taková funkce je praktická k výpočtu pouze v jednom směru.

Některé jednosměrné funkce mají to, co se nazývá **past**. Zatímco je prakticky nemožné vypočítat $a$ pouze na základě $y$ a $f(x)$, existuje určitý kus informace $Z$, který činí výpočet $a$ z $y$ výpočetně proveditelným. Tento kus informace $Z$ je známý jako **past**. Jednosměrné funkce, které mají past, se nazývají **funkce s pastí**.
Nebudeme se zde podrobně zabývat principy výměny klíčů Diffie-Hellman. V zásadě každý účastník vytvoří určité informace, z nichž část je veřejně sdílená a některé zůstávají tajné. Každá strana pak vezme svůj tajný kus informací a veřejné informace sdílené druhou stranou k vytvoření soukromého klíče. A poněkud zázračně, obě strany skončí se stejným soukromým klíčem.
Každá strana, která sleduje pouze veřejně sdílené informace mezi dvěma stranami ve výměně klíčů Diffie-Hellman, není schopna replikovat tyto výpočty. Potřebovali by soukromé informace od jedné ze dvou stran, aby to bylo možné.

Ačkoliv základní verze výměny klíčů Diffie-Hellman prezentovaná v dokumentu z roku 1976 není velmi bezpečná, sofistikovanější verze základního protokolu jsou dnes určitě stále používány. Nejdůležitější je, že každý protokol výměny klíčů ve nejnovější verzi protokolu zabezpečení transportní vrstvy (verze 1.3) je v podstatě obohacenou verzí protokolu prezentovaného Diffiem a Hellmanem v roce 1976. Protokol zabezpečení transportní vrstvy je převažující protokol pro bezpečnou výměnu informací formátovaných podle protokolu hypertextového přenosu (http), standardu pro výměnu webového obsahu.

Důležité je, že výměna klíčů Diffie-Hellman není asymetrickým schématem. Přesně řečeno, patří spíše do oblasti symetrické kryptografie s klíči. Ale jelikož jak výměna klíčů Diffie-Hellman, tak asymetrická kryptografie spoléhají na jednosměrné číselně-teoretické funkce s pastmi, jsou typicky diskutovány společně.

Druhý způsob, který Diffie a Hellman nabídli k řešení problému distribuce a správy klíčů ve svém dokumentu z roku 1976, byl, samozřejmě, prostřednictvím asymetrické kryptografie.

Na rozdíl od jejich prezentace výměny klíčů Diffie-Hellman, poskytli pouze obecné obrysy, jak by mohly být asymetrické kryptografické schématy pravděpodobně konstruovány. Neposkytli žádnou konkrétní jednosměrnou funkci, která by mohla specificky splnit podmínky potřebné pro rozumnou bezpečnost v takových schématech.

Praktická implementace asymetrického schématu byla však nalezena o rok později třemi různými akademickými kryptografy a matematiky: Ronaldem Rivestem, Adi Shamirem a Leonardem Adlemanem. [3] Kryptosystém, který představili, se stal známým jako **kryptosystém RSA** (podle jejich příjmení).

Pastové funkce používané v asymetrické kryptografii (a výměně klíčů Diffie-Hellman) jsou všechny spojeny se dvěma hlavními **výpočetně obtížnými problémy**: faktorizací prvočísel a výpočtem diskrétních logaritmů.

**Faktorizace prvočísel** vyžaduje, jak název napovídá, rozklad celého čísla na jeho prvočinitele. Problém RSA je zdaleka nejznámějším příkladem kryptosystému souvisejícího s faktorizací prvočísel.

**Problém diskrétního logaritmu** je problém, který se vyskytuje v cyklických skupinách. Při daném generátoru v konkrétní cyklické skupině vyžaduje výpočet unikátního exponentu potřebného k vyprodukování dalšího prvku ve skupině z generátoru.

Schémata založená na diskrétním logaritmu spoléhají na dva hlavní typy cyklických skupin: multiplikativní skupiny celých čísel a skupiny, které zahrnují body na eliptických křivkách. Původní výměna klíčů Diffie-Hellman, jak byla prezentována v "New Directions in Cryptography", pracuje s cyklickou multiplikativní skupinou celých čísel. Digitální podpisový algoritmus Bitcoinu a nedávno představené schéma podpisu Schnorr (2021) jsou oba založeny na problému diskrétního logaritmu pro konkrétní cyklickou skupinu eliptických křivek.

Dále se obrátíme na vysokoúrovňový přehled tajnosti a autentizace v asymetrickém nastavení. Předtím však musíme učinit krátkou historickou poznámku.
Nyní se zdá pravděpodobné, že skupina britských kryptografů a matematiků pracujících pro Government Communications Headquarters (GCHQ) nezávisle na sobě učinila výše zmíněné objevy o několik let dříve. Tuto skupinu tvořili James Ellis, Clifford Cocks a Malcolm Williamson.
Podle jejich vlastních výpovědí a výpovědí GCHQ byl James Ellis ten, kdo jako první v roce 1969 přišel s konceptem veřejného klíče kryptografie. Údajně poté Clifford Cocks objevil v roce 1973 kryptografický systém RSA a Malcolm Williamson koncept výměny klíčů Diffie-Hellman v roce 1974. [4] Jejich objevy však údajně nebyly zveřejněny až do roku 1997, vzhledem k tajné povaze práce prováděné v GCHQ.

**Poznámky:**

[1] Whitfield Diffie a Martin Hellman, “New directions in cryptography,” _IEEE Transactions on Information Theory_ IT-22 (1976), str. 644–654, na str. 644.

[2] Ralph Merkle také diskutuje o protokolu výměny klíčů v “Secure communications over insecure channels”, _Communications of the Association for Computing Machinery_, 21 (1978), 294–99. Ačkoliv Merkle předložil tento článek dříve než článek od Diffieho a Hellmana, byl publikován později. Merkleovo řešení není exponenciálně bezpečné, na rozdíl od Diffie-Hellmanova.

[3] Ron Rivest, Adi Shamir a Leonard Adleman, “A method for obtaining digital signatures and public-key cryptosystems”, _Communications of the Association for Computing Machinery_, 21 (1978), str. 120–26.

[4] Dobrý přehled těchto objevů poskytuje Simon Singh, _The Code Book_, Fourth Estate (Londýn, 1999), Kapitola 6.

## Asymetrické šifrování a autentizace
<chapterId>2f6f0f03-3c3d-5025-90f0-5211139bc0cc</chapterId>

Přehled **asymetrického šifrování** s pomocí Boba a Alice je poskytnut na *Obrázku 1*.

Alice nejprve vytvoří pár klíčů, skládající se z jednoho veřejného klíče ($K_P$) a jednoho soukromého klíče ($K_S$), kde „P“ v $K_P$ znamená „public“ (veřejný) a „S“ v $K_S$ znamená „secret“ (tajný). Poté tento veřejný klíč volně distribuuje ostatním. K podrobnostem tohoto distribučního procesu se vrátíme později. Ale prozatím předpokládejme, že kdokoli, včetně Boba, může bezpečně získat Alicein veřejný klíč $K_P$.

V pozdějším okamžiku chce Bob napsat zprávu $M$ Alici. Jelikož obsahuje citlivé informace, chce, aby obsah zůstal tajný pro všechny kromě Alice. Bob tedy nejprve zašifruje svou zprávu $M$ pomocí $K_P$. Poté pošle výsledný šifrovaný text $C$ Alici, která dešifruje $C$ pomocí $K_S$ a získá tak původní zprávu $M$.

*Obrázek 1: Asymetrické šifrování*

![Obrázek 1: Asymetrické šifrování](assets/Figure6-1.webp "Obrázek 1: Asymetrické šifrování")

Jakýkoli protivník, který odposlouchává komunikaci mezi Bobem a Alicí, může pozorovat $C$. Také zná $K_P$ a algoritmus šifrování $E(\cdot)$. Důležité však je, že tyto informace mu neumožňují šifrovaný text $C$ spolehlivě dešifrovat. Pro dešifrování je specificky vyžadován $K_S$, který útočník nemá.
Symetrické šifrovací schématy obecně musí být bezpečné proti útočníkovi, který může platně šifrovat zprávy v otevřeném textu (známé jako bezpečnost proti útoku s výběrem šifrovaného textu). Nejsou však navrženy s výslovným účelem umožnit vytváření takových platných šifrovaných textů útočníkem nebo kýmkoli jiným.
To je v příkrém kontrastu k asymetrickému šifrovacímu schématu, jehož celý účel je umožnit komukoli, včetně útočníků, vytvářet platné šifrované texty. Asymetrická šifrovací schémata lze tedy označit jako **šifry s více přístupy**.

Pro lepší pochopení toho, co se děje, si představte, že místo elektronického odesílání zprávy by Bob chtěl poslat fyzický dopis v tajnosti. Jedním ze způsobů, jak zajistit tajnost, by bylo, kdyby Alice poslala Bobovi bezpečný zámek, ale klíč si ponechala. Po napsání dopisu by Bob mohl dopis vložit do krabice a zavřít ji Aliceiným zámkem. Poté by mohl poslat zamčenou krabici se zprávou Alici, která má klíč k jejímu odemčení.

I když Bob může zámek zamknout, ani on ani žádná jiná osoba, která krabici zachytí, nemůže zámek odemknout, pokud je skutečně bezpečný. Pouze Alice ji může odemknout a vidět obsah Bobova dopisu, protože má klíč.

Asymetrické šifrovací schéma je, hrubě řečeno, digitální verzí tohoto procesu. Zámek se podobá veřejnému klíči a klíč od zámku soukromému klíči. Protože je zámek digitální, je pro Alici mnohem snazší a ne tak nákladné jej distribuovat komukoli, kdo by jí chtěl posílat tajné zprávy.

Pro autentizaci v asymetrickém nastavení používáme **digitální podpisy**. Ty mají tedy stejnou funkci jako kódy pro ověření zpráv v symetrickém nastavení. Přehled digitálních podpisů je poskytnut na *Obrázku 2*.

Bob nejprve vytvoří pár klíčů, skládající se z veřejného klíče ($K_P$) a soukromého klíče ($K_S$), a distribuuje svůj veřejný klíč. Když chce poslat Alici ověřenou zprávu, nejprve vezme svou zprávu $M$ a svůj soukromý klíč, aby vytvořil **digitální podpis** $D$. Bob poté pošle Alici svou zprávu spolu s digitálním podpisem.

Alice vloží zprávu, veřejný klíč a digitální podpis do **algoritmu pro ověření**. Tento algoritmus produkuje buď **true** pro platný podpis, nebo **false** pro neplatný podpis.

Digitální podpis je, jak název jasně napovídá, digitálním ekvivalentem psaného podpisu na dopisech, smlouvách a tak dále. Ve skutečnosti je digitální podpis obvykle mnohem bezpečnější. S určitým úsilím můžete falšovat psaný podpis; proces usnadněný tím, že psané podpisy nejsou často pečlivě ověřovány. Bezpečný digitální podpis je však, stejně jako bezpečný kód pro ověření zpráv, **existenčně nezfalšovatelný**: to znamená, že s bezpečným schématem digitálního podpisu nikdo nemůže uskutečnitelně vytvořit podpis pro zprávu, který by prošel ověřovacím postupem, pokud nemá soukromý klíč.

*Obrázek 2: Asymetrická autentizace*

![Obrázek 2: Asymetrická autentizace](assets/Figure6-2.webp "Obrázek 2: Asymetrická autentizace")

Stejně jako u asymetrického šifrování vidíme zajímavý kontrast mezi digitálními podpisy a kódy pro ověření zpráv. U posledně jmenovaných může algoritmus pro ověření použít pouze jedna ze stran, které jsou obeznámeny s bezpečnou komunikací. To je proto, že vyžaduje soukromý klíč. V asymetrickém nastavení však může kdokoli ověřit digitální podpis $S$ vytvořený Bobem.
Všechno toto dělá z digitálních podpisů mimořádně mocný nástroj. Tvoří základ, například pro vytváření podpisů na smlouvách, které lze ověřit pro právní účely. Pokud by Bob vytvořil podpis na smlouvě ve výše uvedené výměně, Alice může soudnímu dvoru ukázat zprávu $M$, smlouvu a podpis $S$. Soud poté může ověřit podpis pomocí Bobova veřejného klíče. [5]
Jako další příklad, digitální podpisy jsou důležitým aspektem zabezpečení softwaru a distribuce aktualizací softwaru. Tento typ veřejné ověřitelnosti by nikdy nemohl být vytvořen pouze pomocí kódů pro ověření zpráv.

Jako poslední příklad síly digitálních podpisů vezměme v úvahu Bitcoin. Jedním z nejčastějších nedorozumění o Bitcoinu, zejména v médiích, je, že transakce jsou šifrovány: nejsou. Místo toho Bitcoinové transakce pracují s digitálními podpisy pro zajištění bezpečnosti.

Bitcoiny existují ve dávkách nazývaných nevyužité transakční výstupy (neboli **UTXO’s**). Předpokládejme, že na konkrétní Bitcoinové adrese obdržíte tři platby po 2 bitcoinech každá. Technicky na této adrese nyní nemáte 6 bitcoinů. Místo toho máte tři dávky po 2 bitcoinech, které jsou uzamčeny kryptografickým problémem spojeným s touto adresou. Pro jakoukoli platbu, kterou provedete, můžete použít jednu, dvě nebo všechny tři tyto dávky, v závislosti na tom, kolik potřebujete pro transakci.

Důkaz vlastnictví nad nevyužitými transakčními výstupy je obvykle ukázán prostřednictvím jednoho nebo více digitálních podpisů. Bitcoin funguje přesně proto, že platné digitální podpisy na nevyužitých transakčních výstupech jsou výpočetně nemožné vytvořit, pokud nevlastníte tajné informace potřebné k jejich vytvoření.

V současnosti Bitcoinové transakce transparentně zahrnují veškeré informace, které je třeba ověřit účastníky v síti, jako jsou původy nevyužitých transakčních výstupů použitých v transakci. Ačkoli je možné některé z těchto informací skrýt a stále umožnit ověření (jak to dělají některé alternativní kryptoměny, jako je Monero), vytváří to také konkrétní bezpečnostní rizika.

Zmatek někdy vzniká mezi digitálními podpisy a písemnými podpisy zachycenými digitálně. V posledně jmenovaném případě zachytíte obraz svého písemného podpisu a vložíte jej do elektronického dokumentu, jako je pracovní smlouva. To však v kryptografickém smyslu není digitální podpis. Posledně jmenovaný je jen dlouhé číslo, které lze vyprodukovat pouze při vlastnictví soukromého klíče.

Stejně jako v prostředí symetrického klíče, můžete také používat asymetrické šifrování a autentizační schémata společně. Platí podobné principy. Především byste měli používat různé páry soukromých veřejných klíčů pro šifrování a vytváření digitálních podpisů. Kromě toho byste měli nejprve zprávu zašifrovat a poté ji autentizovat.

Důležitě, v mnoha aplikacích se asymetrická kryptografie nepoužívá po celý komunikační proces. Místo toho bude typicky použita pouze pro *výměnu symetrických klíčů* mezi stranami, které budou skutečně komunikovat.

To je případ, například, když nakupujete zboží online. Znáte-li veřejný klíč prodejce, může vám poslat digitálně podepsané zprávy, jejichž pravost můžete ověřit. Na tomto základě můžete následovat jeden z několika protokolů pro výměnu symetrických klíčů pro bezpečnou komunikaci.

Hlavním důvodem četnosti výše uvedeného přístupu je, že asymetrická kryptografie je mnohem méně efektivní než symetrická kryptografie při vytváření určité úrovně bezpečnosti. To je jeden z důvodů, proč stále potřebujeme symetrickou kryptografii vedle veřejné kryptografie. Kromě toho je symetrická kryptografie mnohem přirozenější v konkrétních aplikacích, jako je šifrování vlastních dat uživatelem počítače.

Tak jak přesně digitální podpisy a šifrování veřejným klíčem řeší problémy s distribucí klíčů a správou klíčů?
Zde není jedna odpověď. Asymetrická kryptografie je nástroj a neexistuje jediný způsob, jak tento nástroj použít. Ale pojďme vzít naše dřívější příklad od Jim’s Sporting Goods, abychom ukázali, jak by se problémy obvykle řešily v tomto příkladu.
Na začátek by Jim’s Sporting Goods pravděpodobně oslovilo **certifikační autoritu**, organizaci, která podporuje distribuci veřejných klíčů. Certifikační autorita by zaregistrovala některé údaje o Jim’s Sporting Goods a udělila by mu veřejný klíč. Poté by Jim’s Sporting Goods poslala certifikát, známý jako **TLS/SSL certifikát**, s veřejným klíčem Jim’s Sporting Goods digitálně podepsaným vlastním veřejným klíčem certifikační autority. Tímto způsobem certifikační autorita potvrzuje, že určitý veřejný klíč skutečně patří Jim’s Sporting Goods.

Klíčem k pochopení tohoto procesu s TLS/SSL certifikáty je, že i když obvykle nebudete mít veřejný klíč Jim’s Sporting Goods uložený kdekoliv ve vašem počítači, veřejné klíče uznávaných certifikačních autorit jsou skutečně uloženy ve vašem prohlížeči nebo v operačním systému. Tyto jsou uloženy v tom, co se nazývá **kořenové certifikáty**.

Takže, když vám Jim’s Sporting Goods poskytne jeho TLS/SSL certifikát, můžete ověřit digitální podpis certifikační autority prostřednictvím kořenového certifikátu ve vašem prohlížeči nebo operačním systému. Pokud je podpis platný, můžete být relativně jisti, že veřejný klíč na certifikátu skutečně patří Jim’s Sporting Goods. Na tomto základě je snadné nastavit protokol pro bezpečnou komunikaci s Jim’s Sporting Goods.

Distribuce klíčů se nyní pro Jim’s Sporting Goods stala mnohem jednodušší. Není těžké vidět, že i správa klíčů se také výrazně zjednodušila. Místo toho, aby museli ukládat tisíce klíčů, Jim’s Sporting Goods stačí ukládat soukromý klíč, který mu umožňuje vytvářet podpisy pro veřejný klíč na jeho SSL certifikátu. Pokaždé, když zákazník přijde na stránku Jim’s Sporting Goods, mohou z tohoto veřejného klíče zahájit bezpečnou komunikační relaci. Zákazníci také nepotřebují ukládat žádné informace (kromě veřejných klíčů uznávaných certifikačních autorit v jejich operačním systému a prohlížeči).

**Poznámky:**

[5] Jakékoli schéma, které se pokouší dosáhnout nedopustitelnosti, dalšího tématu, které jsme diskutovali v kapitole 1, bude v základu potřebovat zahrnout digitální podpisy.

## Hashovací funkce
<chapterId>ea8327ab-b0e3-5635-941c-4b51f396a648</chapterId>

Hashovací funkce jsou všudypřítomné v kryptografii. Nejsou ani symetrické, ani asymetrické schéma, ale spadají do vlastní kryptografické kategorie.

Už jsme se setkali s hashovacími funkcemi v kapitole 4 při vytváření hashovacích autentizačních zpráv. Jsou také důležité v kontextu digitálních podpisů, ačkoliv z mírně odlišného důvodu: Digitální podpisy jsou obvykle vytvářeny nad hash hodnotou nějaké (zašifrované) zprávy, spíše než nad samotnou (zašifrovanou) zprávou. V této sekci nabídnu podrobnější úvod do hashovacích funkcí.

Začněme s definicí hashovací funkce. **Hashovací funkce** je jakákoli efektivně vypočitatelná funkce, která přijímá vstupy libovolné velikosti a vrací výstupy pevné délky.

**Kryptografická hashovací funkce** je prostě hashovací funkce, která je užitečná pro aplikace v kryptografii. Výstup kryptografické hashovací funkce se obvykle nazývá **hash**, **hash-hodnota**, nebo **digest zprávy**.

V kontextu kryptografie se termín „hashovací funkce“ obvykle vztahuje na kryptografickou hashovací funkci. Tuto praxi budu odteď dodržovat.
Příkladem populární hašovací funkce je **SHA-256** (secure hash algorithm 256). Bez ohledu na velikost vstupu (např. 15 bitů, 100 bitů nebo 10 000 bitů) tato funkce vrací 256bitovou hašovací hodnotu. Níže můžete vidět několik příkladů výstupů funkce SHA-256.
“Hello”: `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`

“52398”: `a3b14d2bf378c1bd47e7f8eaec63b445150a3d7a80465af16dd9fd319454ba90`

“Kryptografie je zábavná”: `3cee2a5c7d2cc1d62db4893564c34ae553cc88623992d994e114e344359b146c`

Všechny výstupy jsou přesně 256 bitů zapsaných ve formátu hexadecimální soustavy (každá hexadecimální číslice může být reprezentována čtyřmi binárními číslicemi). Takže i kdybyste do funkce SHA-256 vložili knihu *Pán prstenů* od Tolkiena, výstup by byl stále 256 bitů.

Hašovací funkce jako SHA-256 se používají k různým účelům v kryptografii. Jaké vlastnosti se od hašovací funkce vyžadují, záleží na kontextu konkrétní aplikace. Existují dvě hlavní vlastnosti, které se obecně od hašovacích funkcí v kryptografii požadují:

1.	Odolnost proti kolizím
2.	Skrytí

Hašovací funkce $H$ se považuje za **odolnou proti kolizím**, pokud je nepraktické najít dvě hodnoty, $x$ a $y$, takové, že $x \neq y$, a přesto $H(x) = H(y)$.

Funkce odolné proti kolizím jsou důležité například při ověřování softwaru. Představte si, že byste chtěli stáhnout Windows verzi Bitcoin Core 0.21.0 (serverová aplikace pro zpracování síťového provozu Bitcoinu). Hlavní kroky, které byste museli provést, aby jste ověřili legitimitu softwaru, jsou následující:

1.	Nejprve musíte stáhnout a importovat veřejné klíče jednoho nebo více přispěvatelů Bitcoin Core do softwaru, který dokáže ověřit digitální podpisy (např. Kleopetra). Tyto veřejné klíče můžete najít [zde](https://github.com/bitcoin/bitcoin/blob/master/contrib/builder-keys/keys.txt). Doporučuje se ověřit software Bitcoin Core s veřejnými klíči od více přispěvatelů.
2.	Dále musíte ověřit veřejné klíče, které jste importovali. Alespoň jeden krok, který byste měli provést, je ověření, že veřejné klíče, které jste našli, jsou stejné jako ty, které byly publikovány na různých místech. Můžete například konzultovat osobní webové stránky, Twitterové stránky nebo Githubové stránky lidí, jejichž veřejné klíče jste importovali. Typicky se toto porovnání veřejných klíčů provádí porovnáním krátkého haše veřejného klíče známého jako otisk.
3.	Dále musíte stáhnout spustitelný soubor pro Bitcoin Core z jejich [webové stránky](www.bitcoincore.org). Budou k dispozici balíčky pro operační systémy Linux, Windows a MAC.
4.	Poté musíte najít dva soubory s vydáním. První obsahuje oficiální SHA-256 hash pro stažený spustitelný soubor společně s hashi pro všechny ostatní vydané balíčky. Další soubor s vydáním bude obsahovat podpisy různých přispěvatelů nad souborem s vydáním obsahujícím hashe balíčků. Oba tyto soubory s vydáním by měly být umístěny na webové stránce Bitcoin Core.
5. Dále byste museli vypočítat SHA-256 hash spustitelného souboru, který jste si stáhli z webové stránky Bitcoin Core na svém vlastním počítači. Poté tento výsledek porovnáte s oficiálním hashem balíčku pro spustitelný soubor. Měly by být stejné. 6. Nakonec byste museli ověřit, že jedna nebo více digitálních podpisů nad souborem s vydáním s oficiálními hashemi balíčku skutečně odpovídá jednomu nebo více veřejným klíčům, které jste importovali (vydání Bitcoin Core nejsou vždy podepsána všemi). To můžete udělat s aplikací jako je Kleopetra.

Tento proces ověřování softwaru má dvě hlavní výhody. Zaprvé zajišťuje, že při stahování z webové stránky Bitcoin Core nedošlo k žádným chybám v přenosu. Zadruhé zajišťuje, že vás žádný útočník nemohl přimět ke stažení modifikovaného, škodlivého kódu, ať už hacknutím webové stránky Bitcoin Core nebo zachycením provozu.

Jak přesně proces ověřování softwaru výše chrání proti těmto problémům?

Pokud jste pečlivě ověřili veřejné klíče, které jste importovali, pak můžete být poměrně jisti, že tyto klíče jsou skutečně jejich a nebyly kompromitovány. Vzhledem k tomu, že digitální podpisy mají existenční nezfalšovatelnost, víte, že pouze tito přispěvatelé mohli vytvořit digitální podpis nad oficiálními hashemi balíčku na souboru s vydáním.

Předpokládejme, že podpisy na staženém souboru s vydáním jsou v pořádku. Nyní můžete porovnat hodnotu hash, kterou jste vypočítali lokálně pro spustitelný soubor Windows, který jste stáhli, s tou, která je zahrnuta v řádně podepsaném souboru s vydáním. Jak víte, hashovací funkce SHA-256 je odolná proti kolizím, shoda znamená, že váš spustitelný soubor je přesně stejný jako oficiální spustitelný soubor.

Nyní se podívejme na druhou běžnou vlastnost hashovacích funkcí: **skrývání**. Jakákoli hashovací funkce $H$ se považuje za mající vlastnost skrývání, pokud pro libovolně vybrané $x$ z velmi velkého rozsahu je nemožné najít $x$, když je dáno pouze $H(x)$.

Níže můžete vidět výstup SHA-256 zprávy, kterou jsem napsal. Abych zajistil dostatečnou náhodnost, zpráva zahrnovala na konci náhodně generovaný řetězec znaků. Vzhledem k tomu, že SHA-256 má vlastnost skrývání, nikdo by nebyl schopen dešifrovat tuto zprávu.

- `b194221b37fa4cd1cfce15aaef90351d70de17a98ee6225088b523b586c32ded`

Ale nechám vás v napětí, dokud SHA-256 neoslabí. Původní zpráva, kterou jsem napsal, byla následující:

* „Toto je velmi náhodná zpráva, nebo spíše tak nějak náhodná. Tato první část není, ale skončím s několika relativně náhodnými znaky, abych zajistil velmi nepředvídatelnou zprávu. XLWz4dVG3BxUWm7zQ9qS“.

Běžným způsobem, jakým se hashovací funkce s vlastností skrývání používají, je správa hesel (odolnost proti kolizím je také důležitá pro tuto aplikaci). Jakákoli slušná online služba založená na účtech, jako je Facebook nebo Google, nebude ukládat vaše hesla přímo pro správu přístupu k vašemu účtu. Místo toho budou ukládat pouze hash tohoto hesla. Pokaždé, když na prohlížeči vyplníte své heslo, je nejprve vypočítán hash. Pouze tento hash je odeslán na server poskytovatele služby a porovnán s hashem uloženým v databázi na pozadí. Vlastnost skrývání může pomoci zajistit, že útočníci jej z hodnoty hash nebudou moci získat.
Správa hesel pomocí hashů samozřejmě funguje pouze v případě, že uživatelé skutečně zvolí obtížná hesla. Vlastnost skrývání předpokládá, že x je vybráno náhodně z velmi velkého rozsahu. Výběr hesel jako „1234“, „mojeheslo“ nebo datum vašich narozenin neposkytne žádnou skutečnou bezpečnost. Existují dlouhé seznamy běžných hesel a jejich hashů, které mohou útočníci využít, pokud získají hash vašeho hesla. Tyto typy útoků jsou známé jako **útoky slovníkové**. Pokud útočníci znají některé z vašich osobních údajů, mohou také zkusit některé informované tipy. Proto vždy potřebujete dlouhá, bezpečná hesla (ideálně dlouhé, náhodné řetězce z generátoru hesel).

Někdy může aplikace potřebovat hashovací funkci, která má jak odolnost proti kolizím, tak schopnost skrývání. Ale určitě ne vždy. Proces ověřování softwaru, o kterém jsme diskutovali, například vyžaduje pouze, aby hashovací funkce prokázala odolnost proti kolizím, skrývání není důležité.

Ačkoliv jsou odolnost proti kolizím a schopnost skrývání hlavními vlastnostmi hledanými u hashovacích funkcí v kryptografii, v určitých aplikacích mohou být žádoucí i jiné typy vlastností.

**Poznámky:**

[6] Terminologie „skrývání“ není běžným jazykem, ale je převzata specificky od Arvinda Narayanana, Josepha Bonneaua, Edwarda Feltena, Andrew Millera a Stevena Goldfedera, *Bitcoin and Cryptocurrency Technologies*, Princeton University Press (Princeton, 2016), Kapitola 1.

# Kryptosystém RSA
<partId>864dca42-2a8d-530f-bb94-2e1f68b3f411</partId>

## Problém faktorizace
<chapterId>a31a66e4-52ea-539c-9953-4769ad565d7e</chapterId>

Zatímco symetrická kryptografie je obvykle poměrně intuitivní pro většinu lidí, to obvykle neplatí pro asymetrickou kryptografii. I když jste pravděpodobně pohodlní s vysokou úrovní popisu nabízeného v předchozích sekcích, pravděpodobně se divíte, co přesně jsou jednosměrné funkce a jak jsou přesně používány k konstrukci asymetrických schémat.

V této kapitole odhalím některá tajemství obklopující asymetrickou kryptografii tím, že se podívám hlouběji na konkrétní příklad, konkrétně na kryptosystém RSA. V první sekci představím problém faktorizace, na kterém je založen problém RSA. Poté pokryji několik klíčových výsledků z teorie čísel. V poslední sekci tyto informace spojíme, abychom vysvětlili problém RSA a jak lze tento použít pro vytváření asymetrických kryptografických schémat.

Přidání této hloubky do naší diskuse není snadný úkol. Vyžaduje to představení celé řady teorémů a tvrzení z teorie čísel. Ale nenechte se matematikou odradit. Propracování této diskuse výrazně zlepší vaše pochopení toho, co leží v základu asymetrické kryptografie, a je to investice, která stojí za to.

Nyní se pojďme nejprve obrátit k problému faktorizace.

___

Kdykoli vynásobíte dvě čísla, řekněme $a$ a $b$, označujeme čísla $a$ a $b$ jako **faktory** a výsledek jako **součin**. Pokus o zápis čísla $N$ do násobení dvou nebo více faktorů se nazývá **faktorizace**. [1] Jakýkoli problém, který to vyžaduje, můžete nazvat **problémem faktorizace**.

Přibližně před 2 500 lety objevil řecký matematik Eukleides z Alexandrie klíčový teorém o faktorizaci celých čísel. Je běžně nazýván **teorémem o jedinečné faktorizaci** a říká následující:

**Teorém 1**. Každé celé číslo $N$, které je větší než 1, je buď prvočíslo, nebo lze vyjádřit jako součin prvočíselných faktorů.
Vše, co druhá část tohoto prohlášení znamená, je, že můžete vzít jakékoliv necelé číslo $N$ větší než 1 a zapsat ho jako násobení prvočísel. Níže jsou uvedeny několik příkladů necelých čísel zapsaných jako součin prvočíselných faktorů.
* $18 = 2 \cdot 3 \cdot 3 = 2 \cdot 3^2$
* $84 = 2 \cdot 2 \cdot 3 \cdot 7 = 2^2 \cdot 3 \cdot 7$
* $144 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3 = 2^4 \cdot 3^2$

Pro všechna tři výše uvedená čísla je výpočet jejich prvočíselných faktorů relativně snadný, i když znáte pouze $N$. Začnete nejmenším prvočíslem, tedy 2, a zjistíte, kolikrát je číslo $N$ dělitelné dvěma. Poté pokračujete testováním dělitelnosti $N$ čísly 3, 5, 7 a tak dále. Tento proces pokračuje, dokud není vaše číslo $N$ zapsáno jako součin pouze prvočísel.

Vezměme například číslo 84. Níže můžete vidět proces určování jeho prvočíselných faktorů. Na každém kroku odebereme nejmenší zbývající prvočíselný faktor (vlevo) a určíme zbytek, který má být faktorizován. Pokračujeme, dokud není zbytek také prvočíslem. Na každém kroku je aktuální faktorizace 84 zobrazena vpravo.

* Prvočíselný faktor = 2: zbytek = 42 	($84 = 2 \cdot 42$)
* Prvočíselný faktor = 2: zbytek = 21 	($84 = 2 \cdot 2 \cdot 21$)
* Prvočíselný faktor = 3: zbytek = 7 	($84 = 2 \cdot 2 \cdot 3 \cdot 7$)
* Jelikož 7 je prvočíslo, výsledek je $2 \cdot 2 \cdot 3 \cdot 7$, nebo $2^2 \cdot 3 \cdot 7$.

Předpokládejme nyní, že $N$ je velmi velké. Jak obtížné by bylo rozložit $N$ na jeho prvočíselné faktory?

To opravdu závisí na $N$. Předpokládejme například, že $N$ je 50,450,400. I když toto číslo vypadá zastrašující, výpočty nejsou tak složité a snadno se provádějí ručně. Stejně jako výše, začnete s 2 a pokračujete dále. Níže můžete vidět výsledek tohoto procesu podobným způsobem jako výše.

* 2: 25,225,200 	($50,450,400 = 2 \cdot 25,225,200$)  
* 2: 12,612,600 	($50,450,400 = 2^2 \cdot 12,612,600$)  
* 2: 6,306,300 	($50,450,400 = 2^3 \cdot 6,306,300$)  
* 2: 3,153,150 	($50,450,400 = 2^4 \cdot 3,153,150$)  
* 2: 1,576,575 	($50,450,400 = 2^5 \cdot 1,576,575$)
* 3: 525,525 ($50,450,400 = 2^5 \cdot 3 \cdot 525,525$)
* 3: 175,175 ($50,450,400 = 2^5 \cdot 3^2 \cdot 175,175$)
* 5: 35,035 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5 \cdot 35,035$)
* 5: 7,007 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7,007$)
* 7: 1,001 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7 \cdot 1,001$)
* 7: 143 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 143$)
* 11: 13 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$)
* Jelikož 13 je prvočíslo, výsledek je $2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$.

Vyřešit tento problém ručně zabere nějaký čas. Počítač by to samozřejmě dokázal za zlomek sekundy. Ve skutečnosti může počítač často dokonce faktorizovat extrémně velká celá čísla za zlomek sekundy.

Existují však určité výjimky. Předpokládejme, že nejprve náhodně vybereme dva velmi velké prvočísla. Je typické označovat tyto jako $p$ a $q$, a toto označení zde převezmu.

Pro konkrétnost, řekněme, že $p$ a $q$ jsou obě 1024-bitová prvočísla, a že skutečně vyžadují alespoň 1024 bitů pro jejich reprezentaci (takže první bit musí být 1). Takže například 37 by nemohlo být jedno z prvočísel. Samozřejmě můžete reprezentovat 37 s 1024 bity. Ale jasně *nepotřebujete* tolik bitů pro její reprezentaci. Můžete reprezentovat 37 jakýmkoli řetězcem, který má 6 nebo více bitů. (V 6 bitech by 37 bylo reprezentováno jako $100101$).

Je důležité ocenit, jak velká $p$ a $q$ jsou, pokud jsou vybrána pod výše uvedenými podmínkami. Jako příklad jsem vybral náhodné prvočíslo, které potřebuje alespoň 1024 bitů pro reprezentaci níže.
* 14,752,173,874,503,595,484,930,006,383,670,759,559,764,562,721,397,166,747,289,220,945,457,932,666,751,048,198,854,920,097,085,690,793,755,254,946,188,163,753,506,778,089,706,699,671,722,089,715,624,760,049,594,106,189,662,669,156,149,028,900,805,928,183,585,427,782,974,951,355,515,394,807,209,836,870,484,558,332,897,443,152,653,214,483,870,992,618,171,825,921,582,253,023,974,514,209,142,520,026,807,636,589
Předpokládejme, že nyní po náhodném výběru prvočísel $p$ a $q$ je vynásobíme, abychom získali celé číslo $N$. Toto poslední číslo je tedy 2048bitové číslo, které vyžaduje pro svou reprezentaci alespoň 2048 bitů. Je mnohem, mnohem větší než buď $p$ nebo $q$.

Předpokládejme, že počítači dáte pouze $N$ a požádáte ho, aby našel dva 1024bitové prvočíselné faktory $N$. Pravděpodobnost, že počítač objeví $p$ a $q$, je extrémně malá. Můžete říci, že je to pro všechny praktické účely nemožné. To platí, i kdybyste použili superpočítač nebo dokonce síť superpočítačů.

Začněme tím, že předpokládáme, že počítač se pokusí problém vyřešit procházením 1024bitových čísel, testováním v každém případě, zda jsou prvočísla a zda jsou faktory $N$. Sada prvočísel k testování je pak přibližně $1.265 \cdot 10^{305}$. [2]

I kdybyste vzali všechny počítače na planetě a nechali je pokusit se najít a testovat 1024bitová prvočísla tímto způsobem, šance 1 ku miliardě na úspěšné nalezení prvočíselného faktoru $N$ by vyžadovala období výpočtu mnohem delší než věk Vesmíru.

Nyní v praxi může počítač postupovat lépe než hrubý postup právě popsaný. Existuje několik algoritmů, které může počítač použít k rychlejšímu dosažení faktorizace. Bodem však je, že i při použití těchto efektivnějších algoritmů je úkol počítače stále výpočetně neuskutečnitelný. [3]

Důležité je, že obtížnost faktorizace za právě popsaných podmínek spočívá v předpokladu, že neexistují žádné výpočetně efektivní algoritmy pro výpočet prvočíselných faktorů. Nemůžeme vlastně dokázat, že efektivní algoritmus neexistuje. Přesto je tento předpoklad velmi pravděpodobný: navzdory rozsáhlým snahám trvajícím stovky let jsme dosud nenašli takový výpočetně efektivní algoritmus.

Takže problém faktorizace za určitých okolností může být pravděpodobně považován za těžký problém. Konkrétně, když jsou $p$ a $q$ velmi velká prvočísla, jejich součin $N$ není těžké vypočítat; ale faktorizace pouze s daným $N$ je prakticky nemožná.


**Poznámky:**

[1] Faktorizace může být také důležitá pro práci s jinými typy matematických objektů než čísla. Například může být užitečné faktorizovat polynomiální výrazy jako $x^2 - 2x + 1$. V naší diskusi se budeme zaměřovat pouze na faktorizaci čísel, konkrétně celých čísel.
[2] Podle **věty o prvočíslech** je počet prvočísel menších nebo rovných $N$ přibližně $N/\ln(N)$. To znamená, že počet prvočísel o délce 1024 bitů můžete aproximovat takto:
$$ \frac{2^{1024}}{\ln(2^{1024})} - \frac{2^{1023}}{\ln(2^{1023})} $$

...což se rovná přibližně $1.265 \times 10^{305}$.

[3] Totéž platí pro problémy diskrétního logaritmu. Proto asymetrické konstrukce pracují s mnohem většími klíči než symetrické kryptografické konstrukce.

## Výsledky teorie čísel
<chapterId>23cd2186-8d97-5709-a4a7-b984f1eb9999</chapterId>

Bohužel, problém faktorizace nemůže být přímo použit pro asymetrické kryptografické schéma. Nicméně můžeme použít složitější, ale související problém k tomuto účelu: problém RSA.

Pro pochopení problému RSA je potřeba porozumět několika větám a tvrzením z teorie čísel. Ty jsou v této sekci prezentovány ve třech pododdílech: (1) řád N, (2) inverzibilita modulo N a (3) Eulerova věta.

Některý materiál v těchto třech pododdílech byl již představen v *Kapitole 3*. Zde ale tento materiál pro pohodlí opět uvedu.

### Řád N

Celé číslo $a$ je **vzájemně prvočíselné** nebo **relativně prvočíselné** s celým číslem $N$, pokud největší společný dělitel mezi nimi je 1. Ačkoli 1 není podle konvence prvočíslo, je vzájemně prvočíselná s každým celým číslem (stejně jako $-1$).

Například, pokud $a = 18$ a $N = 37$, jsou to jasně vzájemně prvočíselné čísla. Největší celé číslo, které dělí jak 18, tak 37, je 1. Naopak, pokud $a = 42$ a $N = 16$, nejsou to jasně vzájemně prvočíselné čísla. Obě čísla jsou dělitelná 2, což je větší než 1.

Nyní můžeme definovat řád $N$ takto. Předpokládejme, že $N$ je celé číslo větší než 1. **Řád N** je pak počet všech vzájemně prvočíselných s $N$ tak, že pro každé vzájemně prvočíselné $a$ platí následující podmínka: $1 \leq a < N$.

Například, pokud $N = 12$, pak 1, 5, 7 a 11 jsou jediná vzájemně prvočíselná, která splňují výše uvedenou požadavek. Tedy řád 12 je roven 4.

Předpokládejme, že $N$ je prvočíslo. Pak každé celé číslo menší než $N$, ale větší nebo rovno 1, je s ním vzájemně prvočíselné. To zahrnuje všechny prvky v následující množině: $\{1,2,3,….,N - 1\}$. Tedy, když je $N$ prvočíslo, řád $N$ je $N - 1$. To je uvedeno v tvrzení 1, kde $\phi(N)$ označuje řád $N$.

**Tvrzení 1**. $\phi(N) = N - 1$ když $N$ je prvočíslo
Předpokládejme, že $N$ není prvočíslo. Poté můžete vypočítat jeho řád pomocí **Eulerovy funkce Phi**. Zatímco výpočet řádu malého celého čísla je relativně přímočarý, Eulerova funkce Phi se stává zvláště důležitou pro větší celá čísla. Návrh Eulerovy funkce Phi je uveden níže.
**Věta 2**. Nechť $N$ je rovno $p_1^{e_1} \cdot p_2^{e_2} \cdot \ldots \cdot p_i^{e_i} \cdot \ldots \cdot p_n^{e_n}$, kde množina $\{p_i\}$ obsahuje všechny různé prvočíselné dělitele $N$ a každé $e_i$ udává, kolikrát se prvočíselný dělitel $p_i$ vyskytuje pro $N$. Potom,

$$\phi(N) = p_1^{e_1 - 1} \cdot (p_1 - 1) \cdot p_2^{e_2 - 1} \cdot (p_2 - 1) \cdot \ldots \cdot p_n^{e_n - 1} \cdot (p_n - 1)$$

**Věta 2** ukazuje, že jakmile rozložíte libovolné neprvočíselné $N$ na jeho různé prvočíselné dělitele, je snadné vypočítat řád $N$.

Například, předpokládejme, že $N = 270$. To jasně není prvočíslo. Rozklad $N$ na jeho prvočíselné dělitele dává výraz: $2 \cdot 3^3 \cdot 5$. Podle Eulerovy funkce Phi je potom řád $N$ následující:

$$\phi(N) = 2^{1 - 1} \cdot (2 - 1) + 3^{3 - 1} \cdot (3 - 1) + 5^{1 - 1} \cdot (5 - 1) = 1 \cdot 1 + 9 \cdot 2 + 1 \cdot 4 = 1 + 18 + 4 = 23$$

Předpokládejme dále, že $N$ je součinem dvou prvočísel, $p$ a $q$. **Věta 2** výše potom uvádí, že řád $N$ je následující:

$$p^{1 - 1} \cdot (p - 1) \cdot q^{1 - 1} \cdot (q - 1) = (p - 1) \cdot (q - 1)$$

To je klíčový výsledek zejména pro problém RSA, a je uveden v **Propozici 2** níže.

**Propozice 2**. Pokud je $N$ součinem dvou prvočísel, $p$ a $q$, řád $N$ je součin $(p - 1) \cdot (q - 1)$.

Pro ilustraci předpokládejme, že $N = 119$. Toto celé číslo lze rozložit na dvě prvočísla, a to 7 a 17. Eulerova funkce Phi tedy naznačuje, že řád 119 je následující:

$$\phi(119) = (7 - 1) \cdot (17 - 1) = 6 \cdot 16 = 96$$

Jinými slovy, celé číslo 119 má v rozsahu od 1 do 119 celkem 96 nesoudělných čísel. Ve skutečnosti tato množina zahrnuje všechna celá čísla od 1 do 119, která nejsou násobky ani 7 ani 17.
Od tohoto okamžiku označme množinu nesoudělných čísel, která určuje řád $N$, jako $C_N$. Pro náš příklad, kde $N = 119$, je množina $C_{119}$ příliš velká na to, aby byla úplně vypsána. Ale některé z prvků jsou následující:
$$C_{119} = \{1, 2, \dots 6, 8 \dots 13, 15, 16, 18, \dots 33, 35 \dots 96\}$$

### Inverznost modulo N

Můžeme říci, že celé číslo $a$ je **invertibilní modulo N**, pokud existuje alespoň jedno celé číslo $b$ takové, že $a \cdot b \mod N = 1 \mod N$. Jakékoli takové celé číslo $b$ je označováno jako **inverze** (nebo **multiplikativní inverze**) čísla $a$ při redukci modulo $N$.

Předpokládejme například, že $a = 5$ a $N = 11$. Existuje mnoho celých čísel, kterými můžete násobit 5, takže $5 \cdot b \mod 11 = 1 \mod 11$. Vezměme si například celá čísla 20 a 31. Je snadné vidět, že obě tato celá čísla jsou inverzemi 5 pro redukci modulo 11.

* $5 \cdot 20 \mod 11 = 100 \mod 11 = 1 \mod 11$
* $5 \cdot 31 \mod 11 = 155 \mod 11 = 1 \mod 11$

Zatímco 5 má mnoho inverzí redukce modulo 11, můžete ukázat, že existuje pouze jedna kladná inverze 5, která je menší než 11. Ve skutečnosti to není jedinečné pro náš konkrétní příklad, ale obecný výsledek.

**Propozice 3**. Pokud je celé číslo $a$ invertibilní modulo $N$, musí platit, že přesně jedna kladná inverze $a$ je menší než $N$. (Takže tato jedinečná inverze $a$ musí pocházet z množiny $\{1, \dots, N - 1\}$).

Označme jedinečnou inverzi $a$ z **Propozice 3** jako $a^{-1}$. V případě, kdy $a = 5$ a $N = 11$, můžete vidět, že $a^{-1} = 9$, vzhledem k tomu, že $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$.

Všimněte si, že hodnotu 9 pro $a^{-1}$ v našem příkladu můžete získat také jednoduše redukcí jakékoli jiné inverze $a$ modulo 11. Například, $20 \mod 11 = 31 \mod 11 = 9 \mod 11$. Takže kdykoli je celé číslo $a > N$ invertibilní modulo $N$, pak $a \mod N$ musí být také invertibilní modulo $N$.

Není nutně pravda, že inverze $a$ existuje redukce modulo $N$. Předpokládejme například, že $a = 2$ a $N = 8$. Neexistuje žádné $b$, ani konkrétně žádné $a^{-1}$, takové, že $2 \cdot b \mod 8 = 1 \mod 8$. To je proto, že jakákoli hodnota $b$ vždy vyprodukuje násobek 2, takže žádné dělení 8 nikdy nemůže vyprodukovat zbytek, který se rovná 1.
Jak přesně víme, zda má nějaké celé číslo $a$ inverzi pro dané $N$? Jak jste si možná všimli v předchozím příkladu, největší společný dělitel mezi 2 a 8 je vyšší než 1, konkrétně 2. A to je vlastně ilustrativní pro následující obecný výsledek:
**Propozice 4**. Inverze celého čísla $a$ existuje v případě redukce modulo $N$, a konkrétně jedinečná kladná inverze menší než $N$, právě tehdy, když je největší společný dělitel mezi $a$ a $N$ roven 1 (to znamená, že jsou to nesoudělná čísla).

V případě, kdy $a = 5$ a $N = 11$, jsme dospěli k závěru, že $a^{-1} = 9$, vzhledem k tomu, že $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$. Je důležité si všimnout, že opak je také pravda. To znamená, když $a = 9$ a $N = 11$, platí, že $a^{-1} = 5$.

### Eulerova věta

Než přejdeme k problému RSA, potřebujeme pochopit ještě jednu klíčovou větu, a to **Eulerovu větu**. Tato věta říká následující:

**Věta 3**. Předpokládejme, že dvě celá čísla $a$ a $N$ jsou nesoudělná. Pak $a^{\phi(N)} \mod N = 1 \mod N$.

To je pozoruhodný výsledek, ale na první pohled trochu matoucí. Pojďme se podívat na příklad, abychom to lépe pochopili.

Předpokládejme, že $a = 5$ a $N = 7$. Tyto jsou skutečně nesoudělné, jak vyžaduje Eulerova věta. Víme, že řád čísla 7 je roven 6, vzhledem k tomu, že 7 je prvočíslo (viz **Propozice 1**).

Co nyní Eulerova věta tvrdí, je, že $5^6 \mod 7$ musí být rovno $1 \mod 7$. Níže jsou výpočty ukazující, že to skutečně platí.

* $5^6 \mod 7 = 15,625 \mod 7 = 1 \mod N$

Celé číslo 7 dělí 15,624 celkem 2,233krát. Zbytek po dělení 16,625 sedmičkou je tedy 1.

Dále, použitím Eulerovy funkce Phi, **Věta 2**, můžete odvodit **Propozici 5** níže.

**Propozice 5**. $\phi(a \cdot b) = \phi(a) \cdot \phi(b)$ pro jakákoli kladná celá čísla $a$ a $b$.

Proč to tak je, nebudeme ukazovat. Ale pouze poznamenejme, že jste již viděli důkaz této propozice tím, že $\phi(p \cdot q) = \phi(p) \cdot \phi(q) = (p - 1) \cdot (q - 1)$, když $p$ a $q$ jsou prvočísla, jak je uvedeno v **Propozici 2**.

Eulerova věta ve spojení s **Propozicí 5** má důležité důsledky. Podívejte se, co se stane, například v níže uvedených výrazech, kde $a$ a $N$ jsou nesoudělná.

* $a^{2 \cdot \phi(N)} \mod N = a^{\phi(N)} \cdot a^{\phi(N)} \mod N = 1 \cdot 1 \mod N = 1 \mod N$
* $a^{\phi(N) + 1} \mod N = a^{\phi(N)} \cdot a^1 \mod N = 1 \cdot a^1 \mod N = a \mod N$
* $a^{8 \cdot \phi(N) + 3} \mod N = a^{8 \cdot \phi(N)} \cdot a^3 \mod N = 1 \cdot a^3 \mod N = a^3 \mod N$

Tedy kombinace Eulerovy věty a **Propozice 5** nám umožňuje jednoduše vypočítat řadu výrazů. Obecně můžeme získaný poznatek shrnout jako v **Propozici 6**.

**Propozice 6**. $a^x \mod N = a^{x \mod \phi(N)}$

Nyní musíme všechno spojit v posledním, trochu složitějším kroku.

Stejně jako má $N$ řád $\phi(N)$, který zahrnuje prvky množiny $C_N$, víme, že celé číslo $\phi(N)$ musí mít zase svůj řád a množinu nesoudělných čísel. Označme $\phi(N) = R$. Pak víme, že existuje také hodnota pro $\phi(R)$ a množina nesoudělných čísel $C_R$.

Předpokládejme, že nyní vybereme celé číslo $e$ z množiny $C_R$. Víme z **Propozice 3**, že toto celé číslo $e$ má pouze jedno jedinečné kladné inverzní číslo menší než $R$. To znamená, že $e$ má jedno jedinečné inverzní číslo z množiny $C_R$. Nazvěme toto inverzní číslo $d$. Vzhledem k definici inverze to znamená, že $e \cdot d = 1 \mod R$.

Tento výsledek můžeme použít k formulaci tvrzení o našem původním celém čísle $N$. To je shrnuto v **Propozici 7**.

**Propozice 7**. Předpokládejme, že $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Pak pro jakýkoliv prvek $a$ z množiny $C_N$ musí platit, že $a^{e \cdot d \mod \phi(N)} = a^{1 \mod \phi(N)} = a \mod N$.

Nyní máme všechny teoretické výsledky potřebné k jasnému formulování problému RSA.

## Kryptosystém RSA
<chapterId>0253c2f7-b8a4-5d0e-bd60-812ed6b6c7a9</chapterId>

Nyní jsme připraveni formulovat problém RSA. Předpokládejme, že vytvoříte sadu proměnných skládajících se z $p$, $q$, $N$, $\phi(N)$, $e$, $d$ a $y$. Nazvěme tuto sadu $\Pi$. Je vytvořena následovně:

1. Generujte dva náhodné prvočísla $p$ a $q$ stejné velikosti a vypočítejte jejich součin $N$.
2. Vypočítejte řád $N$, $\phi(N)$, následujícím součinem: $(p - 1) \cdot (q - 1)$.
3. Vyberte $e > 2$ tak, aby bylo menší a nesoudělné s $\phi(N)$.
4. Vypočítejte $d$ tak, že nastavíte $e \cdot d \mod \phi(N) = 1$.
5. Vyberte náhodnou hodnotu $y$, která je menší a nesoudělná s $N$.
Problém RSA spočívá v nalezení $x$ takového, že $x^e = y$, přičemž jsou nám dány pouze některé informace o $\Pi$, konkrétně proměnné $N$, $e$ a $y$. Když jsou $p$ a $q$ velmi velké, obvykle se doporučuje, aby měly velikost 1024 bitů, problém RSA je považován za obtížný. Nyní můžete vidět, proč tomu tak je na základě předchozí diskuse.
Snadný způsob, jak vypočítat $x$, když $x^e \mod N = y \mod N$, je jednoduše vypočítat $y^d \mod N$. Víme, že $y^d \mod N = x \mod N$ na základě následujících výpočtů:

$$ y^d \mod N = x^{e \cdot d} \mod N = x^{e \cdot d \mod \phi(N)} \mod N = x^{1 \mod \phi(N)} \mod N = x \mod N. $$

Problém je, že neznáme hodnotu $d$, protože v problému není dána. Proto nemůžeme přímo vypočítat $y^d \mod N$ a získat $x \mod N$.

Mohli bychom však nepřímo vypočítat $d$ z řádu $N$, $\phi(N)$, protože víme, že $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Ale podle předpokladu problém také neudává hodnotu $\phi(N)$.

Nakonec by se řád mohl vypočítat nepřímo s prvočísly $p$ a $q$, takže bychom nakonec mohli vypočítat $d$. Ale podle předpokladu nám také nebyly poskytnuty hodnoty $p$ a $q$.

Přísně vzato, i když je problém faktorizace uvnitř problému RSA obtížný, nemůžeme dokázat, že je problém RSA také obtížný. Mohou totiž existovat jiné způsoby, jak problém RSA vyřešit, než prostřednictvím faktorizace. Nicméně je obecně přijímáno a předpokládáno, že pokud je problém faktorizace uvnitř problému RSA obtížný, pak je obtížný i samotný problém RSA.

Pokud je problém RSA skutečně obtížný, pak produkuje jednosměrnou funkci s pastí. Funkce zde je $f(g) = g^e \mod N$. S vědomím $f(g)$ by kdokoli mohl snadno vypočítat hodnotu $y$ pro konkrétní $g = x$. Nicméně je prakticky nemožné vypočítat konkrétní hodnotu $x$ pouze na základě znalosti hodnoty $y$ a funkce $f(g)$. Výjimkou je, když máte k dispozici informaci $d$, past. V tom případě můžete jednoduše vypočítat $y^d$ a získat $x$.

Pojďme si projít konkrétní příklad, aby ilustroval problém RSA. Nemohu vybrat problém RSA, který by byl považován za obtížný za výše uvedených podmínek, protože čísla by byla nepraktická. Tento příklad je zde pouze k ilustraci, jak problém RSA obecně funguje.

Začněme tím, že si vyberete dvě náhodná prvočísla 13 a 31. Takže $p = 13$ a $q = 31$. Součin těchto dvou prvočísel rovná se 403. Snadno můžeme vypočítat řád 403. Je ekvivalentní $(13 - 1) \cdot (31 - 1) = 360$.
Dále, jak je určeno krokem 3 problému RSA, musíme vybrat číslo nesoudělné s 360, které je větší než 2 a menší než 360. Tuto hodnotu nemusíme vybírat náhodně. Předpokládejme, že vybereme 103. To je číslo nesoudělné s 360, protože největší společný dělitel s 103 je 1.
Krok 4 nyní vyžaduje, abychom vypočítali hodnotu $d$ tak, že $103 \cdot d \mod 360 = 1$. To není snadný úkol ručně, když je hodnota $N$ velká. Vyžaduje to použití procedury nazvané **rozšířený Euklidův algoritmus**.

Ačkoli zde proceduru neukazuji, při $e = 103$ dává hodnotu 7. Můžete ověřit, že pár hodnot 103 a 7 skutečně splňuje obecnou podmínku $e \cdot d \mod \phi(n) = 1$ prostřednictvím níže uvedených výpočtů.

* $103 \cdot 7 \mod 360 = 721 \mod 360 = 1 \mod 360$

Důležité je, že na základě *Propozice 4* víme, že žádné jiné celé číslo mezi 1 a 360 pro $d$ neprodukuje výsledek, že $103 \cdot d = 1 \mod 360$. Navíc, propozice naznačuje, že výběr jiné hodnoty pro $e$ poskytne jinou jedinečnou hodnotu pro $d$.

V kroku 5 problému RSA musíme vybrat nějaké kladné celé číslo $y$, které je menší nesoudělné s 403. Předpokládejme, že nastavíme $y = 2^{103}$. Exponenciace 2 na 103 dává níže uvedený výsledek.

* $2^{103} \mod 403 = 10,141,204,801,825,835,211,973,625,643,008 \mod 403 = 349 \mod 403$

Problém RSA v tomto konkrétním příkladu je nyní následující: Jsou vám poskytnuty $N = 403$, $e = 103$ a $y = 349 \mod 403$. Nyní musíte vypočítat $x$ tak, že $x^{103} = 349 \mod 403$. To znamená, že musíte najít původní hodnotu před exponenciací 103, která byla 2.

Bylo by snadné (alespoň pro počítač) vypočítat $x$, pokud bychom věděli, že $d = 7$. V tom případě byste mohli jednoduše určit $x$ takto.

* $x = y^7 \mod 403 = 349^7 \mod 403 = 630,634,881,591,804,949 \mod 403 = 2 \mod 403$

Problém je, že vám nebyly poskytnuty informace, že $d = 7$. Samozřejmě byste mohli vypočítat $d$ z faktu, že $103 \cdot d = 1 \mod 360$. Problém je, že vám také nebyly poskytnuty informace, že řád $N = 360$. Nakonec byste mohli také vypočítat řád 403 vypočítáním následujícího součinu: $(p - 1) \cdot (q - 1)$. Ale také vám nebylo řečeno, že $p = 13$ a $q = 31$.

Samozřejmě, počítač by mohl problém RSA pro tento příklad poměrně snadno vyřešit, protože zapojená prvočísla nejsou velká. Ale když prvočísla velmi narostou, stane se to pro něj prakticky nemožným úkolem.
Nyní jsme představili problém RSA, sadu podmínek, za kterých je obtížný, a základní matematiku. Jak nám toto vše pomáhá s asymetrickou kryptografií? Konkrétně, jak můžeme převést obtížnost problému RSA za určitých podmínek na šifrovací schéma nebo schéma digitálního podpisu?
Jedním z přístupů je vzít problém RSA a vytvořit schémata přímočaře. Předpokládejme například, že jste vygenerovali sadu proměnných $\Pi$ jak je popsáno v problému RSA, a zajistili, že $p$ a $q$ jsou dostatečně velké. Nastavíte svůj veřejný klíč na $(N, e)$ a sdílíte tyto informace se světem. Jak bylo uvedeno výše, hodnoty pro $p$, $q$, $\phi(n)$ a $d$ si necháte v tajnosti. Ve skutečnosti je $d$ váš soukromý klíč.

Každý, kdo chce poslat zprávu $m$, která je prvkem $C_N$, ji může jednoduše zašifrovat následovně: $c = m^e \mod N$. (Šifrovaný text $c$ zde odpovídá hodnotě $y$ v problému RSA.) Tuto zprávu můžete snadno dešifrovat pouhým výpočtem $c^d \mod N$.

Můžete se také pokusit vytvořit schéma digitálního podpisu stejným způsobem. Předpokládejme, že chcete někomu poslat zprávu $m$ s digitálním podpisem $S$. Můžete jednoduše nastavit $S = m^d \mod N$ a poslat pár $(m,S)$ příjemci. Každý může ověřit digitální podpis jednoduše kontrolou, zda $S^e \mod N = m \mod N$. Jakýkoliv útočník by však měl velmi těžký čas s vytvořením platného $S$ pro zprávu, vzhledem k tomu, že nevlastní $d$.

Bohužel, přeměna samotného obtížného problému, problému RSA, na kryptografické schéma není takto přímočará. Pro přímočaré šifrovací schéma můžete jako své zprávy vybírat pouze nesoudělná čísla s $N$. To nám nezanechává mnoho možných zpráv, určitě ne dost pro standardní komunikaci. Kromě toho musí být tyto zprávy vybírány náhodně. To se zdá být poněkud nepraktické. Nakonec, jakákoli zpráva, která je vybrána dvakrát, vyprodukuje přesně stejný šifrovaný text. To je v jakémkoliv šifrovacím schématu extrémně nežádoucí a nesplňuje žádnou přísnou moderní standardní představu o bezpečnosti šifrování.

Problémy se stávají ještě horšími pro naše přímočaré schéma digitálního podpisu. Jak to stojí, jakýkoliv útočník může snadno padělat digitální podpisy jednoduše tím, že nejprve vybere nesoudělné číslo s $N$ jako podpis a poté vypočítá odpovídající původní zprávu. To jasně porušuje požadavek na existenční nezfalšovatelnost.

Nicméně, přidáním trochu chytré složitosti, lze problém RSA použít k vytvoření bezpečného schématu veřejného klíče pro šifrování stejně jako bezpečného schématu digitálního podpisu. Do detailů takových konstrukcí zde nebudeme vstupovat. [4] Důležité však je, že tato další složitost nemění základní podstatu problému RSA, na kterém jsou tyto schémata založena.


**Poznámky:**

[4] Viz například Jonathan Katz a Yehuda Lindell, _Úvod do moderní kryptografie_, CRC Press (Boca Raton, FL: 2015), str. 410–32 o šifrování RSA a str. 444–41 pro digitální podpisy RSA.