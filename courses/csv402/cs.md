---
name: Protokol RGB od teorie k praxi
goal: Získat dovednosti potřebné k pochopení a používání RGB
objectives: 

  - Porozumět základním pojmům protokolu RGB
  - Zvládnutí principů ověřování na straně klienta a závazků Bitcoinu
  - Naučte se vytvářet, spravovat a přenášet smlouvy RGB
  - Jak ovládat uzel Lightning kompatibilní s RGB

---
# Zjištění protokolu RGB

Ponořte se do světa RGB, protokolu navrženého k implementaci a prosazování digitálních práv ve formě smluv a aktiv na základě pravidel konsensu a operací blockchainu Bitcoinu. Tento komplexní výukový kurz vás provede technickými a praktickými základy RGB, od konceptů "Ověřování na straně klienta" a "Pečetí na jedno použití" až po implementaci pokročilých inteligentních smluv.

Prostřednictvím strukturovaného programu krok za krokem se seznámíte s mechanismy ověřování na straně klienta, deterministickými závazky na Bitcoinu a vzorci interakce mezi uživateli. Naučíte se vytvářet, spravovat a převádět RGB tokeny v Bitcoinu nebo Lightning Network.

Ať už jste vývojář, nadšenec do Bitcoinu, nebo vás prostě jen zajímá, jak se o této technologii dozvědět více, tento vzdělávací kurz vám poskytne nástroje a znalosti, které potřebujete k ovládnutí RGB a vytváření inovativních řešení na Bitcoinu.

Kurz je založen na živém semináři pořádaném společností Fulgur'Ventures a vedeném třemi renomovanými učiteli a odborníky na RGB.

+++
# Úvod

<partId>c6f7a70f-d894-595f-8c0a-b54759778839</partId>

## Prezentace kurzu

<chapterId>cf2f087b-6c6b-5037-8f98-94fc9f1d7f46</chapterId>

Zdravím všechny a vítám vás na tomto školení věnovaném RGB, systému inteligentních smluv validovaných na straně klienta, který běží na Bitcoinu a Lightning Network. Struktura tohoto kurzu je navržena tak, aby umožnila hloubkové prozkoumání tohoto složitého tématu. Zde je uvedeno, jak je kurz uspořádán:

**Díl 1: Teorie

První část je věnována teoretickým konceptům potřebným k pochopení základů ověřování na straně klienta a RGB. Jak zjistíte v tomto kurzu, RGB zavádí řadu technických konceptů, které se v Bitcoinu obvykle nevyskytují. V této části také najdete slovníček pojmů, který poskytuje definice všech pojmů specifických pro protokol RGB.

**Díl 2: Cvičení

Druhá část se zaměří na aplikaci teoretických konceptů uvedených v části 1. Naučíme se vytvářet a manipulovat s kontrakty RGB. Ukážeme si také, jak s těmito nástroji programovat. Tyto první dva oddíly uvádí Maxim Orlovsky.

**Odddíl 3: Aplikace

Závěrečná část je vedena dalšími přednášejícími, kteří představí konkrétní aplikace založené na RGB, aby poukázali na reálné případy použití.

---
Tento školící kurz původně vznikl na základě dvoutýdenního výcvikového tábora pro pokročilé vývojáře ve Viareggiu v Toskánsku, který pořádala společnost [Fulgur'Ventures](https://fulgur.ventures/). První týden, zaměřený na Rust a SDK, najdete v tomto jiném kurzu:

https://planb.network/courses/lnp402
V tomto kurzu se zaměříme na druhý týden bootcampu, který je zaměřen na RGB.

**Týden 1 - LNP402:**

![RGB-Bitcoin](assets/fr/001.webp)

**2. týden - aktuální školení CSV402:**

![RGB-Bitcoin](assets/fr/002.webp)

Děkujeme organizátorům těchto živých kurzů a třem učitelům, kteří se jich zúčastnili:


- Maxim Orlovsky: *Tenebrae sententia sapiens dominabitur astris. Cypher, umělá inteligence, robotika, transhumanismus. Tvůrce RGB, Prime, Radiant a lnp_bp, mycitadel_io & cyphernet_io* ;
- Hunter Trujilo: *Vývojář, Rust, Bitcoin, Lightning, RGB* ;
- Federico Tenga: *Dělám vše pro to, aby se svět změnil v cypherpunkovou dystopii. V současné době pracuji na RGB v Bitfinexu*.

Písemná verze tohoto vzdělávacího kurzu byla vypracována s využitím 2 hlavních zdrojů:


- Videa ze semináře Maxima Orlovského, Huntera Trujila a Frederica Tengy na Lightning Bootcampu ;
- Dokumentace RGB, jejíž výrobu sponzorovala společnost [Bitfinex](https://www.bitfinex.com/).

# Teoreticky RGB

<partId>80e797ee-3f33-599f-ab82-e82eeee08219</partId>

## Úvod do konceptů distribuovaných výpočtů

<chapterId>f52f8af5-5d7c-588b-b56d-99b97176204b</chapterId>

![video](https://youtu.be/AF2XbifPGXM)

RGB je protokol navržený k uplatňování a vymáhání digitálních práv (ve formě smluv a aktiv) škálovatelným a důvěrným způsobem, který je založen na pravidlech konsensu a operacích blockchainu Bitcoin. Cílem této první kapitoly je představit základní pojmy a terminologii týkající se protokolu RGB a zdůraznit zejména jeho úzké propojení se základními koncepty distribuovaných výpočtů, jako je ověřování na straně klienta a pečetě na jedno použití.

V této kapitole prozkoumáme základy **distribuovaných konsensuálních systémů** a zjistíme, jak do této skupiny technologií zapadá RGB. Představíme si také hlavní principy, které nám pomohou pochopit, proč se RGB snaží být rozšiřitelný a nezávislý na vlastním konsensuálním mechanismu Bitcoinu, a přitom se na něj v případě potřeby spoléhat.

### Úvod

Distribuovaná výpočetní technika, specifický obor informatiky, studuje protokoly používané k oběhu a zpracování informací v síti uzlů. Tyto uzly a pravidla protokolů společně tvoří tzv. distribuovaný systém. Mezi základní vlastnosti, které takový systém charakterizují, patří :


- **možnost nezávislého ověřování a validace** určitých údajů každým uzlem;
- Možnost uzlů vytvořit (v závislosti na protokolu) úplný nebo částečný pohled na informace. Tyto pohledy jsou **stavem** distribuovaného systému;
- **chronologické pořadí** operací tak, aby data byla spolehlivě časově označena a aby existovala shoda o posloupnosti událostí (posloupnosti stavů).

Pojem **konsensus** v distribuovaném systému zahrnuje zejména dva aspekty:


- Rozpoznání platnosti** změn stavu (podle pravidel protokolu);
- Dohoda o pořadí** těchto změn stavu, která znemožňuje dodatečné přepsání nebo obrácení ověřených operací (v Bitcoinu je to také známo jako "ochrana proti dvojímu utracení").

První funkční implementaci distribuovaného konsensu bez oprávnění představil Satoshi Nakamoto v Bitcoinu díky kombinaci datové struktury blockchain a algoritmu Proof-of-Work (PoW). V tomto systému závisí důvěryhodnost historie bloku na výpočetním výkonu, který mu věnují uzly (těžaři). Bitcoin je tedy významným a historickým příkladem distribuovaného konsensuálního systému otevřeného všem (*permissionless*).

Ve světě blockchainu a distribuovaných výpočtů můžeme rozlišit dvě základní paradigmata: ***blockchain*** v tradičním smyslu a ***státní kanály***, jejichž nejlepším příkladem ve výrobě je Lightning Network. Blockchain je definován jako registr chronologicky uspořádaných událostí, replikovaných na základě konsensu v rámci otevřené sítě bez oprávnění. Naproti tomu státní kanály jsou peer-to-peer kanály, které umožňují dvěma (nebo více) účastníkům udržovat aktualizovaný stav mimo řetězec, přičemž blockchain používají pouze při otevírání a zavírání těchto kanálů.

V souvislosti s Bitcoinem jste nepochybně obeznámeni s principy těžby, decentralizace a konečnosti transakcí v blockchainu, stejně jako s fungováním platebních kanálů. S RGB zavádíme nové paradigma nazvané **Client-side Validation**, které na rozdíl od blockchainu nebo Lightningu spočívá v lokálním (klientském) ukládání a ověřování přechodů stavu chytrého kontraktu. Od ostatních technik "DeFi" (_rollups_, _plasma_, _ARK_ atd.) se liší také tím, že Client-side Validation se spoléhá na blockchain, aby se zabránilo dvojímu utrácení a na systém časového razítkování, přičemž registr stavů a přechodů mimo řetězec zůstává pouze u příslušných účastníků.

![RGB-Bitcoin](assets/fr/003.webp)

Později také zavedeme důležitý termín: pojem "**stash**", který označuje sadu dat na straně klienta potřebných k zachování stavu smlouvy, protože tato data nejsou replikována globálně v síti. Nakonec se podíváme na důvody vzniku protokolu RGB, který využívá výhod ověřování na straně klienta, a proč doplňuje stávající přístupy (blockchain a stavové kanály).

### Trilemata v distribuované výpočetní technice

Abychom pochopili, jak ověřování na straně klienta a RGB řeší problémy, které neřeší blockchain a Lightning, objevme 3 hlavní "trilemata" v distribuovaných výpočtech:


- Škálovatelnost, decentralizace, soukromí** ;
- Věta CAP** (konzistence, dostupnost, tolerance rozdělení) ;
- Trilema CIA** (důvěrnost, integrita, dostupnost).

#### 1. Škálovatelnost, decentralizace a důvěrnost


- Blockchain (Bitcoin)**

Blockchain je vysoce decentralizovaný, ale není příliš škálovatelný. Navíc vzhledem k tomu, že je vše v globálním, veřejném registru, je důvěrnost omezená. Důvěrnost se můžeme pokusit zlepšit technologiemi s nulovou znalostí (důvěrné transakce, schémata mimblewimble atd.), ale veřejný řetězec nemůže skrýt graf transakcí.


- Bleskové/státní kanály**

Státní kanály (jako v případě Lightning Network) jsou škálovatelnější a soukromější než blockchain, protože transakce probíhají mimo řetězec. Povinnost veřejně oznamovat určité prvky (transakce financování, topologie sítě) a monitorování síťového provozu však mohou částečně ohrozit důvěrnost. Decentralizace také trpí: směrování je náročné na hotovost a hlavní uzly se mohou stát centralizačními body. Právě tento jev začínáme pozorovat u sítě Lightning.


- Ověřování na straně klienta (RGB)**

Toto nové paradigma je ještě lépe škálovatelné a důvěrnější, protože nejenže můžeme integrovat techniky důkazu znalosti s nulovou mírou prozrazení, ale neexistuje ani globální graf transakcí, protože nikdo nemá v držení celý registr. Na druhou stranu to také znamená určitý kompromis v oblasti decentralizace: vydavatel chytrého kontraktu může mít centrální roli (podobně jako "nasazovač kontraktu" v Ethereu). Na rozdíl od blockchainu se však u technologie Client-side Validation ukládají a ověřují pouze kontrakty, které vás zajímají, což zlepšuje škálovatelnost, protože není nutné stahovat a ověřovat všechny existující stavy.

![RGB-Bitcoin](assets/fr/004.webp)

#### 2. Věta CAP (konzistence, dostupnost, tolerance rozdělení)

Věta CAP zdůrazňuje, že není možné, aby distribuovaný systém současně splňoval požadavky na konzistenci (*Konsistence*), dostupnost (*Dostupnost*) a toleranci rozdělení (*Tolerance rozdělení*).


- Blockchain**

Blockchain upřednostňuje konzistenci a dostupnost, ale neporadí si dobře s rozdělením sítě: pokud nevidíte blok, nemůžete jednat a mít stejný pohled jako celá síť.


- Blesk** (ve francouzštině)

Systém stavových kanálů má toleranci dostupnosti a rozdělení (protože dva uzly mohou zůstat navzájem propojeny, i když je síť fragmentována), ale celková konzistence závisí na otevírání a zavírání kanálů v blockchainu.


- Ověřování na straně klienta (RGB)**

Systém, jako je RGB, nabízí konzistenci (každý účastník ověřuje svá data lokálně, bez dvojznačnosti) a toleranci rozdělení (data uchováváte autonomně), ale nezaručuje globální dostupnost (každý se musí ujistit, že má příslušné části historie, a někteří účastníci nemusí nic zveřejnit nebo přestanou sdílet určité informace).

![RGB-Bitcoin](assets/fr/005.webp)

#### 3. Trilema CIA (důvěrnost, integrita, dostupnost)

Toto trilema nám připomíná, že důvěrnost, integrita a dostupnost nemohou být optimalizovány současně. Blockchain, Lightning a ověřování na straně klienta spadají do této rovnováhy různě. Jde o to, že žádný systém nemůže poskytnout vše; je nutné kombinovat několik přístupů (časové razítkování blockchainu, synchronní přístup Lightningu a lokální ověřování pomocí RGB), aby vznikl ucelený balíček nabízející dobré záruky v každé dimenzi.

![RGB-Bitcoin](assets/fr/006.webp)

### Úloha blockchainu a pojem sharding

Blockchain (v tomto případě Bitcoin) slouží především jako mechanismus _časového razítkování_ a ochrana proti dvojímu utrácení. Namísto vkládání kompletních dat chytrého kontraktu nebo decentralizovaného systému do něj jednoduše vkládáme **kryptografické závazky** (_commitments_) k transakcím (ve smyslu Client-side Validation, které budeme nazývat "stavové přechody"). Tedy :


- Osvobozujeme blockchain od velkého množství dat a logiky;
- Každý uživatel ukládá pouze historii potřebnou pro svou část smlouvy (svůj "*shard*"), nikoli replikuje globální stav.

Sharding je koncept, který vznikl v distribuovaných databázích (např. MySQL pro sociální sítě, jako je Facebook nebo Twitter). Pro řešení problému objemu dat a latencí synchronizace je databáze rozdělena na _shardy_ (USA, Evropa, Asie atd.). Každý segment je lokálně konzistentní a s ostatními je synchronizován pouze částečně.

U inteligentních smluv typu RGB rozdělujeme podle samotných smluv. Každá smlouva je nezávislý _shard_. Pokud například držíte pouze tokeny USDT, nemusíte ukládat ani ověřovat celou historii jiného tokenu, například USDC. U Bitcoinu se v blockchainu neprovádí _sharding_: máte globální sadu UTXO. Při ověřování na straně klienta si každý účastník uchovává pouze data kontraktu, která drží nebo používá.

Ekosystém si proto můžeme představit takto:


- Blockchain (Bitcoin)** jako základ, který zajišťuje úplnou replikaci minimálního registru a slouží jako vrstva pro časové razítkování;
- Blesková síť** pro rychlé a důvěrné transakce, která je stále založena na zabezpečení a konečném vypořádání blockchainu bitcoinu;
- RGB a ověřování na straně klienta** pro přidání složitější logiky chytrých smluv, aniž by došlo k zahlcení blockchainu nebo ztrátě důvěrnosti.

![RGB-Bitcoin](assets/fr/007.webp)

Tyto tři prvky tvoří trojúhelníkový celek, nikoli lineární zásobník "vrstva 2", "vrstva 3" atd. Lightning se může připojit přímo k Bitcoinu nebo může být spojen s bitcoinovými transakcemi, které obsahují data RGB. Podobně se může použití "BiFi" (finance na Bitcoinu) skládat s blockchainem, s Lightningem a s RGB podle potřeb důvěrnosti, škálovatelnosti nebo smluvní logiky.

![RGB-Bitcoin](assets/fr/008.webp)

### Pojem stavových přechodů

V každém distribuovaném systému je cílem validačního mechanismu **určit platnost a chronologické pořadí změn stavu**. Cílem je ověřit, zda byla dodržena pravidla protokolu, a prokázat, že tyto změny stavu následují za sebou v definitivním, nezpochybnitelném pořadí.

Abychom pochopili, jak toto ověřování funguje v kontextu **Bitcoinu**, a obecněji, abychom pochopili filozofii ověřování na straně klienta, podívejme se nejprve zpětně na mechanismy blockchainu Bitcoinu, než zjistíme, jak se od nich ověřování na straně klienta liší a jaké optimalizace umožňuje.

![RGB-Bitcoin](assets/fr/009.webp)

V případě blockchainu Bitcoinu je ověřování transakcí založeno na jednoduchém pravidle:


- Všechny síťové uzly stahují každý blok a transakci;
- Tyto transakce ověřují správný vývoj sady UTXO (všechny nespotřebované výstupy);
- Tato data ukládají (ve formě bloků), aby bylo možné historii v případě potřeby přehrát.

![RGB-Bitcoin](assets/fr/010.webp)

Tento model má však dvě hlavní nevýhody:


- Škálovatelnost**: protože každý uzel musí zpracovat, ověřit a archivovat transakce všech uživatelů, existuje zřejmý limit pro kapacitu transakcí, spojený zejména s maximální velikostí bloku (1 MB v průměru za 10 minut u Bitcoinu, bez cookies);
- Soukromí**: vše se vysílá a ukládá veřejně (částky, cílové adresy atd.), což omezuje důvěrnost výměny.

![RGB-Bitcoin](assets/fr/012.webp)

V praxi tento model funguje pro Bitcoin jako základní vrstva (vrstva 1), ale může se stát nedostatečným pro složitější použití, které současně vyžaduje vysokou propustnost transakcí a určitý stupeň důvěrnosti.

Ověřování na straně klienta je založeno na opačné myšlence: namísto toho, aby celá síť ověřovala a ukládala všechny transakce, každý účastník (klient) ověří pouze tu část historie, která se ho týká:


- Když osoba obdrží aktivum (nebo jakýkoli jiný digitální majetek), potřebuje pouze znát a ověřit řetězec operací (stavových přechodů), které vedou k tomuto aktivu, a prokázat jeho legitimitu;
- Tato posloupnost operací od ***Genesis*** (počáteční vydání) až po poslední transakci tvoří acyklický směrovaný graf (DAG) neboli shard, tj. část celkové historie.

![RGB-Bitcoin](assets/fr/013.webp)

Zároveň, aby zbytek sítě (přesněji řečeno podkladová vrstva, jako je Bitcoin) mohl uzamknout konečný stav, aniž by viděl detaily těchto dat, spoléhá se ověřování na straně klienta na pojem ***commitment***.

*Závazek* je kryptografický závazek, obvykle _hash_ (například SHA-256) vložený do transakce Bitcoinu, který dokazuje, že byla zahrnuta soukromá data, aniž by tato data byla odhalena.

Díky těmto _závazkům_ můžeme dokázat:


- Existence informací (protože jsou zapsány v hash) ;
- Anteriorita těchto informací (protože jsou ukotveny a časově označeny v blockchainu s datem a pořadím bloků).

Přesný obsah však není zveřejněn, čímž je zachována jeho důvěrnost.

Konkrétně funguje přechod stavu RGB takto:


- Připravíte nový přechod stavu (např. přenos tokenu RGB);
- Vygenerujete kryptografický závazek k tomuto přechodu a vložíte jej do transakce Bitcoin (tyto závazky se v protokolu RGB nazývají "*kotvy*");
- Protistrana (příjemce) načte historii na straně zákazníka spojenou s tímto aktivem a ověří konzistenci od vzniku chytrého kontraktu až po přechod, který mu předáte.

![RGB-Bitcoin](assets/fr/014.webp)

Ověřování na straně klienta nabízí dvě hlavní výhody:


- Škálovatelnost:**

Závazky (*commitments*) obsažené v blockchainu jsou malé (řádově několik desítek bajtů). Tím je zajištěno, že prostor bloku není zaplněn, protože je třeba zahrnout pouze hash. Umožňuje to také vývoj protokolu mimo řetězec, protože každý uživatel musí ukládat pouze svůj fragment historie (svou _schránku_).


- Ochrana osobních údajů :**

Samotné transakce (tj. jejich podrobný obsah) se v řetězci nezveřejňují. Pouze jejich otisky (*hash*). Částky, adresy a logika smluv tedy zůstávají soukromé a příjemce si může lokálně ověřit platnost svého shardu kontrolou všech předchozích transakcí. Neexistuje žádný důvod, proč by měl příjemce tyto údaje zveřejňovat, s výjimkou případu sporu nebo v případě, kdy je vyžadován důkaz.

V systému, jako je RGB, lze více přechodů stavu z různých smluv (nebo různých aktiv) agregovat do jediné transakce Bitcoin prostřednictvím jediného _commitmentu_. Tento mechanismus vytváří deterministické spojení s časovým razítkem mezi transakcí v řetězci a daty mimo řetězec (přechody ověřené na straně klienta) a umožňuje, aby bylo v jednom kotevním bodě současně zaznamenáno více oddílů, což dále snižuje náklady a stopu v řetězci.

V praxi to znamená, že když je tato transakce bitcoinu potvrzena, trvale "uzamkne" stav podkladových smluv, protože je nemožné změnit hash již zapsaný v blockchainu.

![RGB-Bitcoin](assets/fr/015.webp)

### Koncept skrýše

**Schránka** je soubor dat na straně klienta, která musí účastník bezpodmínečně uchovávat, aby zachoval integritu a historii inteligentního kontraktu RGB. Na rozdíl od kanálu Lightning, kde lze určité stavy rekonstruovat lokálně ze sdílených informací, není stash kontraktu RGB replikována jinam: pokud ji ztratíte, nikdo vám ji nebude moci obnovit, protože jste zodpovědní za svůj podíl na historii. Proto je třeba přijmout systém se spolehlivými postupy zálohování v RGB.

![RGB-Bitcoin](assets/fr/016.webp)

### Těsnění na jedno použití: vznik a fungování

Při přijímání aktiva, jako je měna, jsou nezbytné dvě záruky:


- Pravost obdržené položky;
- Jedinečnost obdržené položky, aby se zabránilo dvojím výdajům.

U fyzických aktiv, jako je bankovka, stačí fyzická přítomnost k prokázání, že nebyla duplikována. V digitálním světě, kde jsou aktiva čistě informační, je však toto ověření složitější, protože informace se mohou snadno množit a duplikovat.

Jak jsme viděli dříve, odhalení historie stavových přechodů odesílatelem nám umožňuje zajistit pravost tokenu RGB. Tím, že máme přístup ke všem transakcím od transakce geneze, můžeme potvrdit pravost tokenu. Tento princip je podobný jako u Bitcoinu, kde lze historii mincí sledovat až k původní transakci na coinbase a ověřit tak jejich platnost. Na rozdíl od Bitcoinu je však tato historie stavových přechodů v RGB soukromá a uchovává se na straně klienta.

Abychom zabránili dvojímu utrácení žetonů RGB, používáme mechanismus nazvaný "**Jednorázová pečeť**". Tento systém zajišťuje, že každý žeton, který byl jednou použit, nelze podvodně použít podruhé.

Jednorázové pečetě jsou kryptografické primitivy, které v roce 2016 navrhl Peter Todd a které se podobají konceptu fyzických pečetí: jakmile je pečeť jednou umístěna na kontejner, je nemožné ji otevřít nebo upravit, aniž by byla pečeť nevratně porušena.

![RGB-Bitcoin](assets/fr/018.webp)

Tento přístup přenesený do digitálního světa umožňuje prokázat, že sled událostí skutečně proběhl a že jej již nelze dodatečně změnit. Jednorázové pečetě tak překračují jednoduchou logiku `hash + časové razítko` a přidávají pojem pečetě, kterou lze uzavřít **pouze jednou**.

![RGB-Bitcoin](assets/fr/017.webp)

Aby pečetě na jedno použití fungovaly, je třeba mít k dispozici médium, které dokáže prokázat existenci či neexistenci publikace a které je obtížné (ne-li nemožné) zfalšovat, jakmile je informace rozšířena. Tuto roli může plnit **blockchain** (jako Bitcoin), stejně jako například papírové noviny s veřejným nákladem. Myšlenka je následující:


- Chceme dokázat, že určitý závazek týkající se zprávy `h(m)` byl publikován, aniž bychom odhalili obsah zprávy `m` ;
- Chceme dokázat, že místo `h(m)` nebyl zveřejněn žádný jiný konkurenční závazek zprávy `h(m)` ;
- Chceme také ověřit, zda zpráva `m` existuje před určitým datem.

Blockchain se pro tuto roli ideálně hodí: jakmile je transakce zařazena do bloku, má celá síť stejný nefalzifikovatelný důkaz o její existenci a obsahu (alespoň částečně, protože _závazek_ může skrýt podrobnosti a zároveň prokázat pravost zprávy).

Pečeť na jedno použití lze tedy chápat jako formální slib, že zpráva (v této fázi ještě neznámá) bude zveřejněna pouze jednou, a to způsobem, který mohou ověřit všechny zúčastněné strany.

Na rozdíl od jednoduchých _závazků_ (hash) nebo časových razítek, které potvrzují datum existence, nabízí jednorázová pečeť dodatečnou záruku, že **žádný alternativní závazek** nemůže existovat současně: nemůžete uzavřít stejnou pečeť dvakrát nebo se pokusit nahradit zapečetěnou zprávu.

Následující srovnání pomáhá pochopit tento princip:


- Kryptografický závazek (hash)**: Pomocí hashovací funkce se můžete zavázat k určitému úseku dat (číslu) zveřejněním jeho hashe. Data zůstávají tajná, dokud nezveřejníte předobraz, ale můžete prokázat, že jste je znali předem;
- Časové razítko (blockchain)**: Vložením tohoto hashe do blockchainu zároveň prokazujeme, že jsme jej znali v přesném okamžiku (v okamžiku zařazení do bloku);
- Těsnění na jedno použití**: V případě jednorázových pečetí jdeme ještě o krok dál a závazek je jedinečný. Pomocí jediné hash můžete paralelně vytvořit několik protichůdných závazků (problém lékaře, který rodině oznámí "*Je to chlapec*" a do svého osobního deníku "*Je to dívka*"). Jednorázová pečeť tuto možnost eliminuje tím, že závazek připojí k médiu prokazujícímu jeho zveřejnění, jako je například bitcoinový blockchain, takže vynaložení UTXO závazek definitivně zpečetí. Jakmile je jednou utraceno, nemůže být stejné UTXO znovu utraceno, aby závazek nahradilo.

| Jednorázové pečetě | Časové značky | Jednoduchý závazek (digest/hash) | Jednorázové pečetě |

| -------------------------------------------------------------------------------- | ------------------------------- | ---------- | ---------------- |

| Zveřejnění závazku neprozrazuje zprávu | Ano | Ano | Ano | Ano | Ano

| Důkaz data závazku / existence zprávy před určitým datem | Nemožné | Možné | Možné | Možné | Možné

| Důkaz, že žádný jiný alternativní závazek nemůže existovat | Nemožné | Možné |

Jednorázové těsnění pracuje ve třech hlavních fázích:

**Definice těsnění :**


- Alice předem definuje pravidla pro zveřejnění pečeti (kdy, kde a jak bude zpráva zveřejněna);
- Bob tyto podmínky přijímá nebo uznává.

![RGB-Bitcoin](assets/fr/021.webp)

**Zavírání těsnění :**


- Za běhu Alice uzavře pečeť zveřejněním skutečné zprávy (obvykle ve formě _commitment_, např. hash);
- Poskytuje také **svědectví** (kryptografický důkaz) prokazující, že pečeť je uzavřená a neodvolatelná.

![RGB-Bitcoin](assets/fr/019.webp)

**Ověření těsnění :**


- Jakmile je pečeť uzavřena, Bob ji již nemůže otevřít: může pouze zkontrolovat, zda byla uzavřena;
- Bob shromáždí pečeť, **svědka** a zprávu (nebo svůj závazek), aby se ujistil, že vše souhlasí a že neexistují žádné konkurenční pečetě nebo různé verze.

Tento proces lze shrnout následovně:

```txt
# Défini par Alice, validé ou accepté par Bob
seal <- Define()
# Fermeture du sceau par Alice avec le message
witness <- Close(seal, message)
# Vérification par Bob
bool <- Verify(seal, witness, message)
```

Ověřování na straně klienta však jde ještě o krok dál: pokud definice samotné pečeti zůstává mimo blockchain, je (teoreticky) možné, aby někdo zpochybnil existenci nebo legitimitu dané pečeti. K překonání tohoto problému se používá řetězec vzájemně propojených pečetí na jedno použití:


- Každá uzavřená pečeť obsahuje definici následující pečeti;
- Tyto uzávěry (s jejich _závazky_) registrujeme v blockchainu (v transakci Bitcoin);
- Jakýkoli pokus o změnu předchozí pečeti by tedy byl v rozporu s historií obsaženou v Bitcoinu.

Přesně to dělá systém RGB:


- Zveřejněné zprávy jsou _závazky_ k datům ověřeným na straně klienta;
- Definice pečetě je spojena s bitcoinovým UTXO ;
- Plomba se uzavře, jakmile je tento UTXO vyčerpán nebo jakmile je do stejného závazku připsán nový výstup;
- Transakční řetězec, který tyto UTXO utrácí, odpovídá důkazu o zveřejnění: každý přechod nebo změna stavu na RGB je tedy ukotven v Bitcoinu.

Shrnuto a podtrženo:


- Definice _plomby_ je UTXO, kterým hodláte zapečetit budoucí závazek;
- Uzavření _závěrky_ nastane, když utratíte tento UTXO a vytvoříte transakci, která obsahuje závazek;
- Svědkem_ je samotná transakce, která dokazuje, že jste pečeť uzavřeli tímto obsahem;
- Nemůžete dokázat, že pečeť nebyla uzavřena (nemůžete si být zcela jisti, že UTXO již nebylo utraceno nebo nebude utraceno v bloku, který jste ještě neviděli), ale můžete dokázat, že skutečně bylo uzavřeno.

Tato jedinečnost je důležitá pro ověřování na straně klienta: při ověřování přechodu stavu se kontroluje, zda odpovídá jedinečnému UTXO, které nebylo dříve použito v konkurenčním závazku. Právě to zaručuje, že v chytrých kontraktech mimo řetězec nedochází k dvojímu utrácení.

### Vícenásobné závazky a kořeny

Inteligentní kontrakt RGB může potřebovat utratit několik jednorázových pečetí (několik UTXO) současně. Navíc jedna bitcoinová transakce může odkazovat na několik různých smluv, z nichž každá pečetí svůj vlastní přechod stavu. To vyžaduje mechanismus **multi-commitment**, který deterministicky a jednoznačně prokáže, že žádný ze závazků neexistuje duplicitně. V tomto případě vstupuje do hry pojem **kotva** v RGB: speciální struktura spojující bitcoinovou transakci a jeden nebo více závazků (stavových přechodů) na straně klienta, z nichž každý potenciálně patří k jiné smlouvě. Na tento koncept se blíže podíváme v příští kapitole.

![RGB-Bitcoin](assets/fr/023.webp)

Dva z hlavních repozitářů projektu na GitHubu (pod organizací LNPBP) sdružují základní implementace těchto konceptů studovaných v první kapitole:


- client_side_validation** : Obsahuje primitiva Rust pro lokální validaci ;
- single_use_seals**: Implementuje logiku pro bezpečné definování a uzavření těchto pečetí.

![RGB-Bitcoin](assets/fr/020.webp)

Všimněte si, že tyto softwarové cihly jsou agnostické vůči Bitcoinu; teoreticky by mohly být použity na jakékoli jiné médium prokazující zveřejnění (jiný registr, časopis atd.). V praxi se RGB spoléhá na Bitcoin kvůli jeho robustnosti a širokému konsensu.

![RGB-Bitcoin](assets/fr/021.webp)

### Otázky veřejnosti

#### Na cestě k širšímu používání jednorázových těsnění

Peter Todd také vytvořil protokol _Open Timestamps_ a koncept jednorázové pečeti je přirozeným rozšířením těchto myšlenek. Kromě RGB lze uvažovat i o dalších případech použití, například o konstrukci _sidechains_, aniž by bylo nutné uchýlit se k _merge mining_, nebo o návrzích souvisejících s drivechain, jako je BIP300. Tento kryptografický primitiv může v zásadě využívat jakýkoli systém vyžadující jediný závazek. RGB je dnes první významnou implementací v plném rozsahu.

#### Problémy s dostupností dat

Vzhledem k tomu, že při ověřování na straně klienta ukládá každý uživatel svou vlastní část historie, není dostupnost dat zaručena globálně. Pokud vydavatel smlouvy určité informace zatají nebo odvolá, může se stát, že nebudete vědět o skutečném vývoji nabídky. V některých případech (např. u stablecoinů) se očekává, že emitent bude udržovat veřejná data, aby prokázal objem v oběhu, ale není k tomu žádná technická povinnost. Je tedy možné navrhnout záměrně neprůhledné kontrakty s neomezenou nabídkou, což vyvolává otázky důvěryhodnosti.

#### Oddělování a izolace smluv

Každá smlouva představuje izolovaný _střep_: USDT a USDC například nemusí sdílet svou historii. Atomické výměny jsou stále možné, ale nejedná se o slučování jejich registrů. Vše probíhá pomocí kryptografického závazku, aniž by každý účastník odhalil celý graf historie.

### Závěr

Viděli jsme, jak koncept ověřování na straně klienta zapadá do blockchainu a _stavových kanálů_, jak reaguje na trilemata distribuovaného počítání a jak jedinečně využívá blockchain Bitcoinu k zamezení dvojího utrácení a k *časovému razítkování*. Myšlenka je založena na pojmu **jednorázové pečeti**, která umožňuje vytvářet jedinečné závazky, které nelze libovolně znovu utratit. Každý účastník tak nahraje pouze nezbytně nutnou historii, čímž se zvýší škálovatelnost a důvěrnost chytrých smluv a zároveň se zachová bezpečnost Bitcoinu jako pozadí.

V dalším kroku podrobněji vysvětlíme, jak se tento mechanismus jednorázových pečetí uplatňuje v Bitcoinu (prostřednictvím UTXO), jak se vytvářejí a ověřují kotvy a jak se pak v RGB vytvářejí kompletní chytré kontrakty. Zejména se podíváme na problematiku vícenásobných závazků, tedy na technickou výzvu, jak dokázat, že transakce v Bitcoinu současně zapečetí více přechodů mezi stavy v různých smlouvách, aniž by došlo k zavedení zranitelností nebo dvojitých závazků.

Než se ponoříte do technických detailů druhé kapitoly, neváhejte si znovu přečíst klíčové definice (ověření na straně klienta, pečeť na jedno použití, kotvy atd.) a pamatujte na celkovou logiku: snažíme se sladit silné stránky bitcoinového blockchainu (bezpečnost, decentralizace, časové razítkování) s výhodami řešení mimo řetězec (rychlost, důvěrnost, škálovatelnost), a právě toho se snaží dosáhnout RGB a ověření na straně klienta.

## Vrstva závazků

<chapterId>cc2fe85a-9cc7-5b8c-a00a-c0a867241061</chapterId>

![video](https://youtu.be/FS6PDprWl5Q)

V této kapitole se podíváme na implementaci ověřování na straně klienta a jednorázových pečetí v rámci blockchainu Bitcoin. Představíme si hlavní principy vrstvy **commitment** (vrstva 1) systému RGB se zvláštním zaměřením na schéma **TxO2**, které systém RGB používá k definování a uzavření pečetě v transakci Bitcoin. Dále probereme dva důležité body, které dosud nebyly podrobně popsány:


- _deterministické závazky Bitcoinu_;
- Víceprotokolové závazky.

Právě kombinace těchto konceptů nám umožňuje navrstvit několik systémů nebo kontraktů na jeden UTXO, a tedy na jeden blockchain.

Je třeba připomenout, že popsané kryptografické operace lze v absolutních číslech použít i na jiné blockchainy nebo publikační média, ale vlastnosti Bitcoinu (pokud jde o decentralizaci, odolnost vůči cenzuře a otevřenost vůči všem) z něj činí ideální základ pro vývoj pokročilé programovatelnosti, jakou vyžaduje **RGB**.

### Schémata závazků v Bitcoinech a jejich použití v systému RGB

Jak jsme viděli v první kapitole kurzu, jednorázové pečetě jsou obecným konceptem: slibujeme, že do určitého místa transakce zahrneme závazek (_commitment_), a toto místo funguje jako pečeť, kterou zprávu uzavřeme. V blockchainu Bitcoinu však existuje několik možností, jak vybrat místo, kam tento _závazek_ umístit.

Abychom pochopili logiku, připomeňme si základní princip: chceme-li uzavřít _jednorázovou pečeť_, strávíme zapečetěnou oblast vložením _závazku_ na danou zprávu. V Bitcoinu to lze provést několika způsoby:


- Použití veřejného klíče nebo adresy**

Můžeme se rozhodnout, že konkrétní veřejný klíč nebo adresa je _jednorázovou pečetí_. Jakmile se tento klíč nebo adresa objeví v řetězci v transakci, znamená to, že pečeť je uzavřena určitou zprávou.


- Použijte výstup transakce Bitcoin**

To znamená, že _jednorázová pečeť_ je definována jako přesný _výstupní bod_ (dvojice TXID + výstupní číslo). Jakmile je tento _výstupní bod_ vyčerpán, je pečeť uzavřena.

Při práci na RGB jsme identifikovali nejméně 4 různé způsoby, jak tyto pečetě implementovat do Bitcoinu:


- Definujte pečeť pomocí veřejného klíče a uzavřete ji ve _výstupu_ ;
- Definujte pečeť pomocí _outpoint_ a uzavřete ji pomocí _output_ ;
- Definujte pečeť pomocí hodnoty veřejného klíče a uzavřete ji v _vstupu_ ;
- Definujte pečeť pomocí _outpoint_ a uzavřete ji v _input_.

| Definice plomby | Uzávěr plomby | Další požadavky | Hlavní použití | Možná schémata zapojení |

| ------------- | ------------------------- | --------------------- | ----------------------------------------------------------------- | ---------------------------- | ------------------------------ |

| P2(W)PKH | V současné době neexistuje | Keytweak, taptweak, opret |

| TxO2 | Transakční výstup | Transakční výstup | Vyžaduje deterministické závazky u Bitcoinu | RGBv1 (univerzální) | Keytweak, tapret, opret |

| PkI | Hodnota veřejného klíče | Záznam o transakci | Pouze Taproot a není kompatibilní se staršími peněženkami | Identity založené na Bitcoinech | Sigtweak, witweak |

| TxO1 | Transakční výstup | Transakční vstup | Pouze Taproot a nekompatibilní se staršími peněženkami | V současné době neexistuje | Sigtweak, witweak |

Nebudeme se podrobně zabývat každou z těchto konfigurací, protože v RGB jsme se rozhodli použít jako definici pečeti **výstupní bod** a umístit _commitment_ do výstupu transakce, která tento _výstupní bod_ utrácí. Můžeme tedy zavést následující pojmy pro pokračování:


- "Definice pečeti "** : Daný _výstupní bod_ (identifikovaný TXID + výstupní č.) ;
- "Uzavření pečeti "**: Transakce, která stráví tento _výstupní bod_, v němž je ke zprávě přidán _závazek_.

Toto schéma bylo vybráno pro jeho kompatibilitu s architekturou RGB, ale pro různá použití by mohly být užitečné i jiné konfigurace.

Písmeno "O2" ve slově "TxO2" nám připomíná, že definice i uzávěrka jsou založeny na vydání (nebo vytvoření) výstupu transakce.

### Příklad diagramu TxO2

Připomínáme, že definice _jednorázové pečeti_ nemusí nutně vyžadovat zveřejnění transakce v řetězci. Stačí, aby například Alice již měla nevydané UTXO. Může se rozhodnout: "Tento _outpoint_ (již existující) je nyní mou pečetí". Zaznamená to lokálně (na straně _klienta_) a dokud toto UTXO nebude utraceno, je pečeť považována za otevřenou.

![RGB-Bitcoin](assets/fr/024.webp)

V den, kdy chce uzavřít pečeť (aby signalizoval událost nebo ukotvil určitou zprávu), utratí toto UTXO v nové transakci (tato transakce se často nazývá "_svědecká transakce_" (nesouvisí s _segwit_, je to jen termín, který jsme jí dali). Tato nová transakce bude obsahovat _závazek_ ke zprávě.

![RGB-Bitcoin](assets/fr/025.webp)

Všimněte si, že v tomto příkladu :


- Nikdo kromě Boba (nebo lidí, kterým se Alice rozhodne odhalit úplný důkaz) se nedozví, že v této transakci je ukryta určitá zpráva;
- Všichni vidí, že _výstupní bod_ byl utracen, ale pouze Bob má důkaz, že zpráva je skutečně zakotvena v transakci.

Pro ilustraci tohoto schématu TxO2 můžeme použít _jednorázovou pečeť_ jako mechanismus pro odvolání klíče PGP. Místo zveřejnění certifikátu o odvolání na serverech může Alice říci: "Tento výstup z Bitcoinu, pokud byl utracen, znamená, že můj klíč PGP je odvolán".

Alice má tedy konkrétní UTXO, ke kterému je lokálně (na straně klienta) přiřazen určitý stav nebo data (známá pouze jí).

Alice informuje Boba, že pokud je tento UTXO vyčerpán, bude se mít za to, že došlo k určité události. Zvenčí vidíme pouze transakci Bitcoin, ale Bob ví, že tento výdaj má skrytý význam.

![RGB-Bitcoin](assets/fr/026.webp)

Jakmile Alice utratí tento UTXO, uzavře pečeť na zprávě, která označuje její nový klíč, nebo jednoduše odvolání starého klíče. Tímto způsobem každý, kdo monitoruje řetězec, uvidí, že UTXO je utraceno, ale pouze ti, kteří mají úplný důkaz, budou vědět, že se jedná právě o odvolání klíče PGP.

![RGB-Bitcoin](assets/fr/027.webp)

Aby Bob nebo kdokoli jiný mohl zkontrolovat skrytou zprávu, musí mu Alice poskytnout informace mimo řetězec.

![RGB-Bitcoin](assets/fr/028.webp)

Alice proto musí Bobovi poskytnout :


- Samotná zpráva (například nový klíč PGP) ;
- Kryptografický důkaz, že zpráva byla zapojena do transakce (známý jako _extra transaction proof_ nebo _anchor_).

![RGB-Bitcoin](assets/fr/029.webp)

Třetí strany tyto informace nemají. Vidí pouze to, že UTXO bylo vynaloženo. Důvěrnost je tedy zajištěna.

Pro objasnění struktury shrňme proces do dvou transakcí:


- Transakce 1**: Obsahuje _definici pečetě_, tj. _výstupní bod_, který bude sloužit jako pečeť.

![RGB-Bitcoin](assets/fr/031.webp)


- Transakce 2**: Utratí tento _výstupní bod_. Tím se uzavře pečeť a v téže transakci se vloží _závazek_ na zprávu.

![RGB-Bitcoin](assets/fr/033.webp)

Druhou transakci proto nazýváme "_svědecká transakce_".

Abychom to ilustrovali z jiného úhlu, můžeme si představit dvě vrstvy:


- Vrchní vrstva (blockchain, veřejná)**: každý vidí transakci a ví, že byl utracen _outpoint_;
- Nižší vrstva (na straně klienta, soukromá)** : pouze Alice (nebo dotyčná osoba) ví, že tento výdaj odpovídá takové a takové zprávě, a to prostřednictvím kryptografického důkazu a zprávy, kterou uchovává lokálně.

![RGB-Bitcoin](assets/fr/034.webp)

Při uzavírání pečeti však vyvstává otázka, kam má být vložen _závazek_

V předchozí části jsme se stručně zmínili o tom, jak lze model ověřování na straně klienta aplikovat na systémy RGB a další systémy. Zde se budeme zabývat částí o **deterministických závazcích Bitcoinu** a o tom, jak je začlenit do transakce. Jde o to, abychom pochopili, proč se snažíme do _svědecké transakce_ vložit jediný závazek, a především jak zajistit, aby nemohly existovat žádné další nezveřejněné konkurenční závazky.

### Místa závazků v transakci

Když někomu poskytnete důkaz, že je v transakci obsažena určitá zpráva, musíte být schopni zaručit, že v téže transakci neexistuje jiná forma závazku (druhá, skrytá zpráva), která vám nebyla odhalena. Aby ověření na straně klienta zůstalo robustní, potřebujete **deterministický** mechanismus pro umístění jediného _závazku_ do transakce, který uzavře _jednorázovou pečeť_.

Na _svědeckou transakci_ se vydává slavné UTXO (neboli _definice pečeti_) a tento výdaj odpovídá uzavření pečeti. Technicky vzato víme, že každý výstupní bod lze utratit pouze jednou. Právě na tom je založena odolnost Bitcoinu proti dvojímu utrácení. Výdajová transakce však může mít několik _vstupů_, několik _výstupů_ nebo může být složena komplexním způsobem (spojení mincí, kanály Lightning atd.). Potřebujeme proto jednoznačně a jednotně definovat, kam v této struktuře vložit _závazek_.

Bez ohledu na metodu (PkO, TxO2 atd.) lze vložit _závazek_ :


- Ve vstupu** prostřednictvím :
    - Sigtweak** (modifikuje složku `r` podpisu ECDSA, podobně jako princip "Sign-to-contract") ;
    - Witweak** (data _segregovaného svědka_ transakce jsou upravena).
- Ve výstupu** prostřednictvím :
    - Keytweak** (veřejný klíč příjemce je "upraven" spolu se zprávou) ;
    - Opret** (zpráva je umístěna v nevýdejním výstupu `OP_RETURN`) ;
    - Tapret** (nebo _Taptweak_), který se spoléhá na taproot a vkládá závazek do skriptové části taproot klíče, čímž deterministicky modifikuje veřejný klíč.

![RGB-Bitcoin](assets/fr/035.webp)

Zde jsou uvedeny podrobnosti o jednotlivých metodách:

![RGB-Bitcoin](assets/fr/038.webp)

***Změna podpisu (sign-to-contract) :***

Dřívější schéma využívalo náhodnou část podpisu (ECDSA nebo Schnorr) k vložení _závazku_: tato technika je známá jako "**Sign-to-contract**". Náhodně vygenerovanou nonce nahradíte hashem obsahujícím data. Tímto způsobem podpis implicitně odhalí váš závazek, aniž by v transakci bylo třeba věnovat další místo. Tento přístup má řadu výhod:


- Žádné přetížení v řetězci (používáte stejné místo jako základní nonce);
- Teoreticky to může být docela diskrétní, protože nonce je zpočátku náhodný údaj.

Objevily se však dvě hlavní nevýhody:


- Multisig před Taproot: pokud máte několik signatářů, musíte se rozhodnout, který podpis ponese _závazek_. Podpisy mohou být různě seřazeny, a pokud některý z signatářů odmítne, ztrácíte kontrolu nad výsledkem _závazku_;
- MuSig a sdílená nonce: u Schnorrova multisig (*MuSig*) je generování nonce algoritmem více stran a je prakticky nemožné nonce individuálně upravovat.

V praxi není **sig tweak** příliš kompatibilní se stávajícím hardwarem (hardwarové peněženky) a formáty (Lightning atd.). Takže tento skvělý nápad je těžko realizovatelný v praxi.

***Klíčové vylepšení (pay-to-contract) :***

**Klíčová změna** přebírá historický koncept _platby na smlouvu_. Vezmeme veřejný klíč `X` a upravíme jej přidáním hodnoty `H(message)`. Konkrétně, pokud `X = x * G` a `h = H(zpráva)`, pak nový klíč bude `X' = X + h * G`. Takto upravený klíč skrývá závazek k `zprávě`. Držitel původního soukromého klíče může přidáním `h` ke svému soukromému klíči `x` dokázat, že má klíč k vydání výstupu. Teoreticky je to elegantní, protože :


- _závazek_ se zadává bez přidání dalších polí;
- Neukládáte žádná další data v řetězci.

V praxi však narážíme na následující problémy:


- Peněženky již nerozpoznávají standardní veřejný klíč, protože byl "upraven", takže nemohou snadno přiřadit UTXO k vašemu obvyklému klíči;
- Hardwarové peněženky nejsou určeny k podepisování pomocí klíče, který není odvozen z jejich standardní derivace;
- Musíte přizpůsobit své skripty, deskriptory atd.

V souvislosti s RGB se s touto cestou počítalo až do roku 2021, ale ukázalo se, že je příliš složitá na to, aby fungovala se současnými normami a infrastrukturou.

***Svědectví o vylepšení :***

Další myšlenkou, kterou některé protokoly, jako například _inscriptions Ordinals_, zavedly do praxe, je umístění dat přímo do sekce `svědek` transakce (odtud výraz "witness tweak"). Tato metoda však :


- Okamžitě zviditelňuje zapojení (doslova vložíte surová data do svědka);
- Může podléhat cenzuře (těžaři nebo uzly mohou odmítnout přenos, pokud je příliš velký nebo má jinou libovolnou vlastnost);
- Zabírá místo v blocích, což je v rozporu s cílem diskrétnosti a lehkosti RGB.

Kromě toho je svědek navržen tak, aby se dal v určitých kontextech prořezat, což může komplikovat robustní důkazy.

***Open-return (opret) :***

Velmi jednoduchá operace `OP_RETURN` umožňuje uložit hash nebo zprávu do speciálního pole transakce. Je však okamžitě zjistitelný: každý vidí, že v transakci je _commitment_, a může být cenzurován nebo zahozen, stejně jako přidán další výstup. Protože to zvyšuje transparentnost a velikost, je to považováno za méně uspokojivé z hlediska řešení pro validaci na straně klienta.

```txt
34-byte_Opret_Commitment =
OP_RETURN   OP_PUSHBYTE_32   <mpc::Commitment>
|_________| |______________| |_________________|
1-byte       1-byte         32 bytes
```

### Tapret

Poslední možností je použití **Taproot** (zavedeno s BIP341) se schématem *Tapret*. *Tapret* je složitější forma deterministického závazku, která přináší zlepšení z hlediska stopy v blockchainu a důvěrnosti operací se smlouvou. Hlavní myšlenkou je skrýt závazek v části `Script Path Spend` transakce [taproot](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki).

![RGB-Bitcoin](assets/fr/036.webp)

Než popíšeme, jak je závazek vložen do transakce taproot, podívejme se na **přesný tvar** závazku, který musí **imperativně** odpovídat 64bajtovému řetězci [konstruovanému](https://github.com/BP-WG/bp-core/blob/master/dbc/src/tapret/mod.rs#L179-L196) takto:

```txt
64-byte_Tapret_Commitment =
OP_RESERVED ...  ... .. OP_RESERVED   OP_RETURN   OP_PUSHBYTE_33  <mpc::Commitment>  <Nonce>
|___________________________________| |_________| |______________| |_______________|  |______|
OP_RESERVED x 29 times = 29 bytes      1 byte         1 byte          32 bytes        1 byte
|________________________________________________________________| |_________________________|
TAPRET_SCRIPT_COMMITMENT_PREFIX = 31 bytes                    MPC commitment + NONCE = 33 bytes
```


- 29 bajtů `OP_RESERVED`, po nichž následuje `OP_RETURN` a poté `OP_PUSHBYTE_33`, tvoří 31bajtovou _prefixovou_ část;
- Následuje 32bajtový _commitment_ (obvykle kořen Merkle z **MPC**), ke kterému přidáme 1 bajt **Nonce** (celkem 33 bajtů pro tuto druhou část).

64bajtová metoda `Tapret` tedy vypadá jako `Opret`, ke kterému jsme předřadili 29 bajtů `OP_RESERVED` a přidali další bajt jako Nonce.

Aby byla zachována flexibilita, pokud jde o implementaci, důvěrnost a škálování, bere schéma Tapret v úvahu různé případy použití v závislosti na požadavcích:


- Jedinečné začlenění závazku Tapret do transakce Taproot bez předchozí struktury Script Path;
- Integrace závazku Tapret do transakce Taproot, která je již vybavena cestou skriptu.

Podívejme se blíže na každý z těchto dvou scénářů.

#### Začlenění Tapret bez existující cesty Script

V tomto prvním případě vycházíme z výstupního klíče taproot (*Taproot Output Key*) `Q`, který obsahuje pouze interní veřejný klíč `P` *(Internal Key*) bez přidružené cesty ke skriptu (*Script Path*):

![RGB-Bitcoin](assets/fr/047.webp)


- `P`: interní veřejný klíč pro _Key Path Spend_.
- `G`: generující bod eliptické křivky [secp256k1](https://en.bitcoin.it/wiki/Secp256k1).
- t = tH_TWEAK(P)` je tweak faktor vypočtený pomocí _tagovaného hashe_ (např. `SHA-256(SHA-256(TapTweak) || P)`) podle [BIP86](https://github.com/bitcoin/bips/blob/master/bip-0086.mediawiki#address-derivation). To dokazuje, že neexistuje žádný skrytý skript.

Chcete-li zahrnout závazek **Tapret**, přidejte **Skript Path Spend** s **unikátním skriptem** takto:

![RGB-Bitcoin](assets/fr/048.webp)


- t = tH_TWEAK(P || Script_root)` se pak stane novým faktorem vylepšení, včetně **Script_root**.
- `Script_root = tH_BRANCH(64-byte_Tapret_Commitment)` představuje kořen tohoto **skriptu**, což je jednoduše hash typu `SHA-256(SHA-256(TapBranch) || 64-byte_Tapret_Commitment)`.

Důkaz začlenění a jedinečnosti v kořenovém stromu se zde omezuje na jediný vnitřní veřejný klíč `P`.

#### Integrace Tapret do již existující cesty skriptů

Druhý scénář se týká složitějšího výstupu `Q` taproot**, který již obsahuje několik skriptů. Například máme strom 3 skriptů:

![RGB-Bitcoin](assets/fr/049.webp)


- tH_LEAF(x)` označuje normalizovanou tagovanou hashovací funkci listového skriptu.
- a, B, C` představují skripty, které jsou již zahrnuty ve struktuře taproot.

Abychom mohli přidat závazek Tapret, musíme na první úroveň stromu vložit *nevyužitelný skript* a stávající skripty posunout o úroveň níže. Vizuálně se strom změní na :

![RGB-Bitcoin](assets/fr/050.webp)


- tHABC` představuje tagovaný hash seskupení nejvyšší úrovně `A, B, C`.
- tHT` představuje hash skriptu odpovídající 64bajtovému `Tapret`.

Podle pravidel taproot musí být každá větev/list kombinována podle lexikografického pořadí hash. Existují dva možné případy:


- `tHT` > `tHABC`: závazek Tapret se posune vpravo od stromu. K důkazu jedinečnosti stačí `tHABC` a `P` ;
- tHT` < `tHABC`**: závazek Tapret je umístěn vlevo. Abychom dokázali, že vpravo není žádný jiný Tapretův závazek, musíme odhalit `tHAB` a `tHC`, abychom prokázali neexistenci jiného takového skriptu.

Vizuální příklad pro první případ (`tHABC < tHT`):

![RGB-Bitcoin](assets/fr/051.webp)

Příklad pro druhý případ (`tHABC > tHT`):

![RGB-Bitcoin](assets/fr/052.webp)

#### Optimalizace pomocí nonce

Abychom zvýšili důvěrnost, můžeme "vydolovat" (přesnější termín by byl "bruteforcing") hodnotu `<Nonce>` (poslední bajt 64bajtového `Tapret`) a pokusit se získat hash `tHT` takový, že `tHABC < tHT`. V tomto případě je závazek umístěn vpravo, čímž je uživatel ušetřen nutnosti prozrazovat celý obsah existujících skriptů, aby dokázal jedinečnost Tapretu.

Souhrnně lze říci, že `Tapret` nabízí diskrétní a deterministický způsob začlenění závazku do transakce taproot, přičemž respektuje požadavek na jedinečnost a jednoznačnost, který je nezbytný pro logiku ověřování na straně klienta a logiku jednorázové pečetě RGB.

#### Platné výstupy

Pro závazkové transakce RGB je hlavním požadavkem platného závazkového schématu bitcoinu následující: Transakce (*svědecká transakce*) musí prokazatelně obsahovat jediný závazek. Tento požadavek znemožňuje sestavení alternativní historie pro data ověřená na straně klienta v rámci téže transakce. To znamená, že zpráva, kolem níž se uzavírá _jednorázová pečeť_, je jedinečná.

Pro splnění této zásady a bez ohledu na počet výstupů v transakci požadujeme, aby **jen jeden výstup** mohl obsahovat závazek (*závazek*). Pro každé z použitých schémat (*Opret* nebo *Tapret*) jsou jedinými platnými výstupy, které mohou obsahovat RGB _závazek_, :


- První výstup `OP_RETURN` (pokud je přítomen) pro schéma *Opret*;
- První výstup taproot (pokud existuje) pro schéma *Tapret*.

Všimněte si, že je docela dobře možné, aby transakce obsahovala jeden závazek `Opret` a jeden závazek `Tapret` ve dvou samostatných výstupech. Díky deterministické povaze Definice pečetí pak tyto dva závazky odpovídají dvěma různým datům ověřeným na straně klienta.

### Analýza a praktické volby v RGB

Při spuštění systému RGB jsme všechny tyto metody přezkoumali, abychom určili, kam a jak deterministicky umístit _commitment_ v transakci. Definovali jsme některá kritéria:


- Kompatibilita s různými scénáři (např. multisig, Lightning, hardwarové peněženky atd.);
- Dopad na prostor v řetězci ;
- Obtížnost implementace a údržby ;
- Důvěrnost a odpor vůči cenzuře.

| Trace a on-chain sizing | Client-side sizing | Portfolio integration | Hardware compatibility | Lightning compatibility | Taproot compatibility |

| --------------------------------------------------- | ------------------------ | ------------------ | ----------------------------- | ------------------------ | ----------------------- | --------------------- |

| Keytweak (deterministické P2C) | 🟢 | 🟡 | 🔴 | 🟠 | 🔴 BOLT, 🔴 Bifrost | 🟠 Taproot, 🟢 MuSig |

| Sigtweak (deterministické S2C) | 🟢 | 🟠 | 🔴 | 🔴 BOLT, 🔴 Bifrost | 🟠 Taproot, 🔴 MuSig |

| Opret (OP_RETURN) | 🔴 | 🟢 | 🟢 | 🟠 | 🔴 BOLT, 🟠 Bifrost | - |

| Algoritmus Tapret: levý horní uzel | 🟠 | 🔴 | 🟠 | 🟢 | 🔴 BOLT, 🟢 Bifrost | 🟢 Taproot, 🟢 MuSig |

| Tapret algoritmus #4: libovolný uzel + důkaz | 🟢 | 🟠 | 🟢 | 🔴 BOLT, 🟢 Bifrost | 🟢 Taproot, 🟢 MuSig |

| Deterministické schéma závazků | Standardní | Náklady na řetězec | Velikost důkazů na straně zákazníka |

| ------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |

| Úprava klíče (deterministické P2C) | LNPBP-1, 2 | 0 bajtů | 33 bajtů (neupravený klíč) |

| Sigtweak (deterministické S2C) | WIP (LNPBP-39) | 0 bajtů | 0 bajtů |

| Opret (OP_RETURN) | - | 36 (v)bytů (TxOut additional) | 0 bytů |

| Tapretův algoritmus: levý horní uzel | LNPBP-6 | 32 bajtů ve svědkovi (8 vbytů) na libovolném n-of-m multisig a strávit na cestu skriptu | 0 bajtů na taproot skriptech bez skriptu ~270 bajtů v případě jednoho skriptu, ~128 bajtů, pokud je více než jeden skript |

| Tapret algoritmus #4: libovolný uzel + důkaz jedinečnosti | LNPBP-6 | 32 bajtů ve svědkovi (8 vbytů) pro případy s jedním skriptem, 0 bajtů ve svědkovi ve většině ostatních případů | 0 bajtů u skriptů bez taprootu, 65 bajtů, dokud Taptree nemá tucet skriptů |

| Vrstva | Náklady na řetězec (bajty/byt) | Náklady na řetězec (bajty/byt) | Náklady na řetězec (bajty/byt) | Náklady na řetězec (bajty/byt) | Náklady na řetězec (bajty/byt) | Náklady na straně klienta (bajty) | Náklady na straně klienta (bajty) | Náklady na straně klienta (bajty) | Náklady na straně klienta (bajty) | Náklady na straně klienta (bajty) | Náklady na straně klienta (bajty) | Náklady na straně klienta (bajty) | Náklady na straně klienta (bajty)

| ------------------------------ | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ |

| **Type** | **Tapret** | **Tapret #4** | **Keytweak** | **Sigtweak** | **Opret** | **Tapret** | **Tapret #4** | **Keytweak** | **Sigtweak** | **Opret** | **Type** | **Type** | **Type** | **Keytweak** | **Tapret #4** | **Keytweak** | **Sigtweak** | **Opret** | **Typ**

| Single-sig | 0 | 0 | 0 | 0 | 32 | 0 | 0 | 32 | 0? | 0 | 0 |

| MuSig (n-of-n) | 0 | 0 | 0 | 32 | 0 | 0 | 0 | 32 | ? > 0 | 0 |

| Multi-sig 2-of-3 | 32/8 | 32/8 nebo 0 | 0 n/a | 32 | ~270 | 65 | 32 | n/a | 0 |

| Multi-sig 3 z 5 | 32/8 | 32/8 nebo 0 | 0 n/a | 32 | ~340 | 65 | 32 | n/a | 0 |

| Multi-sig 2-of-3 s časovým limitem | 32/8 | 0 | 0 n/a | 32 | 64 | 65 | 32 | n/a | 0 | 0

| Vrstva | Náklady v řetězci (vbytes) | Náklady v řetězci (vbytes) | Náklady v řetězci (vbytes) | Náklady na straně klienta (bajty) | Náklady na straně klienta (bajty) |

| -------------------------------- | ---------------------- | ---------------------- | ---------------------- | ------------------------ | ------------------------ |

| **Typ** | **Základna** | **Tapret #2** | **Tapret #4** | **Tapret #2** | **Tapret #4** | **Tapret #4**

| MuSig (n-of-n) | 16,5 | 0 | 0 | 0 | 0 | 0 | 0

| FROST (n-of-m) | ? | 0 | 0 | 0 | 0 |

| Multi_a (n-of-m) | 1+16n+8m | 8 | 8 | 33 * m | 65 |

| MuSig branch / Multi_a (n-of-m) | 1+16n+8n+8xlog(n) | 8 | 0 | 64 | 65 |

| S časovými limity (n-of-m) | 1+16n+8n+8xlog(n) | 8 | 0 | 64 | 65 |

| Metoda | Důvěrnost a škálovatelnost | Interoperabilita | Kompatibilita | Přenositelnost | Složitost |

| ----------------------------------------- | ------------------------------ | ---------------- | ------------- | ----------- | ---------- |

| Keytweak (deterministické P2C) | 🟢 | 🔴 | 🔴 | 🟡 | 🟡 | 🟡 |

| Sigtweak (deterministické S2C) | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 |

| Opret (OP_RETURN) | 🔴 | 🟠 | 🔴 | 🟢 | 🟢 | |

| Algo Tapret: levý horní uzel | 🟠 | 🟢 | 🔴 | 🟠 | 🟠 |

| Algo Tapret #4: Jakýkoli uzel + důkaz | 🟢 | 🟢 | 🔴 | 🔴 |

V průběhu studie se ukázalo, že žádné z těchto schémat závazků není plně kompatibilní se současným standardem Lightning (který nepoužívá Taproot, _muSig2_ ani další podporu _závazků). Probíhá úsilí o úpravu konstrukce kanálu Lightning (*BiFrost*) tak, aby umožňovala vkládání závazků RGB. To je další oblast, kde je třeba přezkoumat strukturu transakcí, klíče a způsob, jakým se podepisují aktualizace kanálů.

Analýza ukázala, že ostatní metody (key tweak, sig tweak, witness tweak atd.) ve skutečnosti představují jiné formy komplikací:


- Buď máme velký objem v řetězci;
- Buď existuje radikální nekompatibilita se stávajícím kódem peněženky;
- Buď je řešení v nekooperativním multisignu neproveditelné.

V případě RGB vynikají zejména dvě metody: ***Opret*** a ***Tapret***, obě klasifikované jako "Transaction Output" a kompatibilní s režimem TxO2 používaným protokolem.

### Závazky více protokolů - MPC

V této části se podíváme na to, jak **RGB** zpracovává agregaci více smluv (přesněji řečeno jejich _přechodových balíčků_) v rámci jednoho závazku (*závazku*) zaznamenaného v transakci Bitcoin pomocí deterministického schématu (podle `Opret` nebo `Tapret`). Za tímto účelem se pořadí merkelizace různých kontraktů odehrává ve struktuře zvané **MPC Tree** (_strom více protokolových závazků_). V této části se podíváme na konstrukci tohoto MPC stromu, jak získat jeho kořen a jak může více kontraktů důvěrně a jednoznačně sdílet stejnou transakci.

Systém MPC (Multi Protocol Commitment) je navržen tak, aby splňoval dvě potřeby:


- Konstrukce hashe `mpc::Commitment`: tento hash bude zahrnut do blockchainu Bitcoinu podle schématu `Opret` nebo `Tapret` a musí odrážet všechny změny stavu, které mají být ověřeny;
- Současné uložení více smluv v jediném _commitmentu_, což umožňuje spravovat samostatné aktualizace více aktiv nebo smluv RGB v rámci jediné transakce Bitcoin.

Konkrétně každý _přechodový svazek_ patří k určité smlouvě. Všechny tyto informace jsou vloženy do **Stromu MPC**, jehož kořen (`mpc::Root`) je pak opět hashován, aby vznikl `mpc::Commitment`. Právě tento poslední hash je podle zvolené deterministické metody vložen do bitcoinové transakce (_transakce svědectví_).

![RGB-Bitcoin](assets/fr/042.webp)

#### MPC Root Hash

Hodnota skutečně zapsaná v řetězci (v `Opret` nebo `Tapret`) se nazývá `mpc::Commitment`. Ta se vypočítá ve tvaru [BIP-341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki) podle vzorce :

```txt
mpc::Commitment = SHA-256(SHA-256(mpc_tag) || SHA-256(mpc_tag) || depth || cofactor || mpc::Root )
```

kde :


- `mpc_tag` je značka: `urn:ubideco:mpc:commitment#2024-01-31`, zvolený podle [konvence pro značení RGB](https://github.com/RGB-WG/rgb-core/blob/master/doc/Commitments.md);
- `depth` (1 byte) označuje hloubku *MPC stromu* ;
- kofaktor` (16 bitů, v malém endiánu) je parametr používaný k podpoře jedinečnosti pozic přiřazených jednotlivým smlouvám ve stromu;
- `mpc::Root` je kořen *MPC stromu*, vypočtený podle postupu popsaného v následující části.

![RGB-Bitcoin](assets/fr/044.webp)

#### Konstrukce stromu MPC

Pro sestavení tohoto stromu MPC musíme zajistit, aby každé smlouvě odpovídala jedinečná pozice na listu. Předpokládejme, že máme :


- c` smluv, které mají být zahrnuty, indexovaných pomocí `i` v `i = {0,1,..,C-1}` ;
- Pro každou smlouvu `c_i` máme identifikátor `ContractId(i) = c_i`.

Poté sestrojíme strom o šířce `w` a hloubce `d` tak, že `2^d = w`, přičemž `w > C`, takže každou smlouvu lze umístit do samostatného _listu_. Pozice `pos(c_i)` každé smlouvy ve stromu je určena vztahem :

```txt
pos(c_i) = c_i mod (w - cofactor)
```

kde `kofaktor` je celé číslo, které zvyšuje pravděpodobnost získání různých pozic pro každou smlouvu. V praxi se konstrukce provádí iteračním procesem:


- Začínáme od minimální hloubky (`d=3` podle konvence, abychom skryli přesný počet smluv);
- Vyzkoušíme různé `kofaktory` (až do `w/2` nebo maximálně 500 z výkonnostních důvodů);
- Pokud se nám nepodaří umístit všechny smlouvy bez kolize, zvýšíme hodnotu `d` a začneme znovu.

Cílem je vyhnout se příliš vysokým stromům a zároveň snížit riziko kolize na minimum. Všimněte si, že jev kolize se řídí logikou náhodného rozdělení, která souvisí s [Výročním paradoxem](https://en.wikipedia.org/wiki/Birthday_problem).

#### Obydlené listy

Po získání `C` různých pozic `pos(c_i)` pro smlouvy `i = {0,1,..,C-1}` je každý list vyplněn hashovací funkcí (*tagged hash*):

```txt
tH_MPC_LEAF(c_i) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x10 || c_i || BundleId(c_i))
```

kde :


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, je vždy zvolen podle Merkleho konvence RGB ;
- `0x10` označuje _smluvní list_ ;
- `c_i` je 32bajtový identifikátor smlouvy (odvozený z hashe Genesis);
- bundleId(c_i)` je 32bajtový hash popisující množinu `State Transitions` vzhledem k `c_i` (shromážděných do *Transition Bundle*).

#### Neobydlené listy

Zbývající listy, které nejsou přiřazeny smlouvě (tj. listy `w - C`), jsou vyplněny "fiktivní" hodnotou (_entropický list_):

```txt
tH_MPC_LEAF(j) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x11 || entropy || j )
```

kde :


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, je vždy zvolen podle Merkleho konvence RGB ;
- `0x11` označuje _entropický list_ ;
- `entropie` je náhodná hodnota 64 bajtů, kterou vybere ten, kdo strom sestavuje;
- `j` je pozice (ve 32 bitech Little Endian) tohoto listu ve stromu.

#### Uzly MPC

Po vygenerování listů `w` (obydlených či neobydlených) přistoupíme k merkelizaci. Veškeré vnitřní uzly jsou zaheslovány následujícím způsobem:

```txt
tH_MPC_BRANCH(tH1 || tH2) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || b || d || w || tH1 || tH2)
```

kde :


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, je vždy zvolen podle Merkleho konvence RGB ;
- b` je _větvící faktor_ (8 bitů). Nejčastěji je `b=0x02`, protože strom je binární a úplný;
- d` je hloubka uzlu ve stromu;
- `w` je šířka stromu (v 256bitové binární soustavě Little Endian);
- tH1` a `tH2` jsou hashe podřízených uzlů (nebo listů), které již byly vypočteny výše uvedeným způsobem.

Tímto způsobem získáme kořen `mpc::Root`. Poté můžeme vypočítat `mpc::Commitment` (jak je vysvětleno výše) a vložit jej do řetězce.

Pro ilustraci si představme příklad, kdy `C=3` (tři smlouvy). Předpokládáme, že jejich pozice jsou `pos(c_0)=7`, `pos(c_1)=4`, `pos(c_2)=2`. Ostatní listy (pozice 0, 1, 3, 5, 6) jsou _entropické listy_. Následující diagram ukazuje posloupnost hashů ke kořeni s :


- `BUNDLE_i`, který představuje `BundleId(c_i)` ;
- `tH_MPC_LEAF(A)` a tak dále, které představují listy (některé pro smlouvy, jiné pro entropii);
- Každá větev `tH_MPC_BRANCH(...)` kombinuje hashe svých dvou potomků.

Konečným výsledkem je **mpc::Root** a poté `mpc::Commitment`.

![RGB-Bitcoin](assets/fr/053.webp)

#### Kontrola hřídele MPC

Pokud chce ověřovatel zajistit, aby byl kontrakt `c_i` (a jeho `BundleId`) zahrnut do konečného `mpc::Commitment`, jednoduše obdrží Merkleův důkaz. Tento důkaz označuje uzly potřebné k dohledání listů (v tomto případě _listu_ smlouvy `c_i`) zpět ke kořeni. Není třeba zveřejňovat celý *strom MPC*: tím se chrání důvěrnost ostatních smluv.

V příkladu potřebuje ověřovatel `c_2` pouze mezihash (`tH_MPC_LEAF(D)`), dva `tH_MPC_BRANCH(...)`, důkaz pozice `pos(c_2)` a hodnotu `cofactor`. Poté může lokálně rekonstruovat kořen, následně přepočítat `mpc::Commitment` a porovnat jej s tím, který byl zapsán v transakci Bitcoin (v rámci `Opret` nebo `Tapret`).

![RGB-Bitcoin](assets/fr/054.webp)

Tento mechanismus zajišťuje, že :


- Stav vztažený k `c_2` je skutečně zahrnut do bloku souhrnných informací (na straně klienta);
- Nikdo nemůže vytvořit alternativní historii se stejnou transakcí, protože _závazky_ v řetězci ukazují na jediný kořen MPC.

#### Shrnutí struktury MPC

Multi Protocol Commitment* (MPC) je princip, který umožňuje RGB sdružovat více smluv do jedné transakce Bitcoin při zachování jedinečnosti závazků a důvěrnosti vůči ostatním účastníkům. Díky deterministické konstrukci stromu je každé smlouvě přiřazena jedinečná pozice a přítomnost "fiktivních" listů (*Entropy Leaves*) částečně maskuje celkový počet smluv účastnících se transakce.

Celý Merkleův strom není nikdy uložen v klientovi. Pro každou příslušnou smlouvu jednoduše vygenerujeme _Merklovu cestu_, která se předá příjemci (který pak může závazek ověřit). V některých případech můžete mít několik aktiv, která prošla stejným UTXO. Pak můžete sloučit několik cest _Merkle_ do takzvaného bloku _multiprotokolového závazku_, abyste se vyhnuli duplikaci příliš velkého množství dat.

Každý _Merkleho důkaz_ je proto lehký, zejména proto, že hloubka stromu nepřesáhne 32 v RGB. Existuje také pojem "Merkleho blok", který uchovává více informací (průřez, entropie atd.), což je užitečné pro spojení nebo oddělení několika větví.

Proto trvalo tak dlouho, než bylo RGB dokončeno. Od roku 2019 jsme měli celkovou vizi: vše umístit na stranu klienta a tokeny dávat do oběhu mimo řetězec. Ale kvůli detailům, jako je sharding pro více kontraktů, struktura Merkleova stromu, jak řešit kolize a merge proofs... to vše vyžadovalo iterace.

### Kotvy: globální sestava

V návaznosti na konstrukci našich závazků (`Opret` nebo `Tapret`) a našeho MPC (*Multi Protocol Commitment*) se musíme zabývat pojmem **Anchor** v protokolu RGB. Kotva je struktura ověřená na straně klienta, která sdružuje prvky potřebné k ověření, zda závazek Bitcoinu skutečně obsahuje konkrétní smluvní informace. Jinými slovy, Kotva shrnuje všechny údaje potřebné k ověření výše popsaných _závazků_.

Kotva se skládá ze tří uspořádaných polí:


- `Txid`
- `MPC Proof`
- extra Transaction Proof - ETP

Každé z těchto polí hraje v procesu ověřování určitou roli, ať už jde o rekonstrukci podkladové transakce bitcoinu, nebo o prokázání existence skrytého závazku (zejména v případě `Tapret`).

#### TxId

Pole `Txid` odpovídá 32bajtovému identifikátoru transakce Bitcoin obsahující závazek `Opret` nebo `Tapret`.

Teoreticky by bylo možné najít toto `Txid` sledováním řetězce stavových přechodů, které samy o sobě ukazují na každou svědeckou transakci, podle logiky jednorázových pečetí. Pro usnadnění a urychlení ověřování je však toto `Txid` jednoduše zahrnuto do Kotvy, čímž se ověřovatel nemusí vracet k celé historii mimo řetězec.

#### Důkaz MPC

Druhé pole, `MPC Proof`, označuje důkaz, že tato konkrétní smlouva (např. `c_i`) je zahrnuta do _Multi Protocol Commitment_. Jedná se o kombinaci :


- `pos_i`, pozice této smlouvy ve stromu MPC;
- kofaktor`, hodnota definovaná pro řešení kolizí pozic;
- `Merkleho důkaz`, tj. množinu uzlů a hashů použitých k rekonstrukci kořene MPC a ověření, že identifikátor smlouvy a její `Přechodový svazek` jsou odevzdány do kořene.

Tento mechanismus byl popsán v předchozí části o sestavení *Stromu MPC*, kde každá smlouva získá jedinečný list díky :

```txt
pos(c_i) = c_i mod (w - cofactor)
```

Poté se použije deterministické merkelizační schéma k agregaci všech listů (smlouvy + entropie). Nakonec `MPC Proof` umožňuje lokálně rekonstruovat kořen a porovnat jej s `mpc::Commitment` obsaženým v řetězci.

#### Extra Transaction Proof - ETP

Třetí pole, **ETP**, závisí na typu použitého závazku. Pokud je závazek typu `Opret`, není vyžadován žádný další důkaz. Validátor kontroluje první výstup `OP_RETURN` transakce a najde `mpc::Commitment` přímo v něm.

**Je-li závazek typu `Tapret`**, musí být poskytnut další důkaz zvaný *Extra Transaction Proof - ETP*. Obsahuje :


- Interní veřejný klíč (`P`) výstupu taproot, ve kterém je vložen *commitment*;
- Partnerské uzly `Skript Path Spend` (když je Tapret *commitment* vložen do skriptu), aby bylo možné prokázat přesné umístění tohoto skriptu ve stromu taproot:
 - Pokud je `Tapret` *commitment* na pravé větvi, odhalíme levý uzel (např. `tHABC`),
 - Pokud se vlevo nachází *závazek `Tapret`, je třeba odhalit 2 uzly (např. `tHAB` a `tHC`), aby se prokázalo, že na pravé straně není žádný jiný *závazek*.
- Funkci `nonce` lze použít k "vytěžení" nejlepší konfigurace, což umožňuje umístit *závazek* na pravou stranu stromu (optimalizace důkazu).

Tento dodatečný důkaz je nezbytný, protože na rozdíl od `Opret` je závazek `Tapret` integrován do struktury taproot skriptu, což vyžaduje odhalení části taproot stromu, aby bylo možné správně ověřit umístění *závazku*.

![RGB-Bitcoin](assets/fr/045.webp)

**Anchory** proto obsahují všechny informace potřebné k ověření závazku Bitcoinu v kontextu RGB. Uvádějí jak příslušnou transakci (`Txid`), tak důkaz o umístění smlouvy (`MPC Proof`), přičemž v případě `Tapret` spravují dodatečný důkaz (`ETP`). Kotva tak chrání integritu a jedinečnost stavu mimo řetězec tím, že zajišťuje, aby stejná transakce nemohla být reinterpretována pro jiné smluvní údaje.

### Závěr

V této kapitole se zabýváme :


- Jak aplikovat koncept jednorázových pečetí v Bitcoinu (zejména prostřednictvím _outpointu_);
- Různé metody deterministického vložení _commitmentu_ do transakce (Sig tweak, Key tweak, witness tweak, op_return, Taproot/Tapret) ;
- Důvody, proč se RGB zaměřuje na závazky společnosti Tapret ;
- Správa více smluv prostřednictvím _multi-protokolových závazků_, což je nezbytné, pokud nechcete vystavit celý stav nebo jiné smlouvy, když chcete prokázat konkrétní bod;
- Viděli jsme také roli _Anchors_, které spojují vše dohromady (TXID transakcí, důkaz Merkleho stromu a důkaz Taproot) v jednom balíčku.

V praxi je technická implementace rozdělena mezi několik specializovaných _krabic_ Rust (v _client_side_validation_, _commit-verify_, _bp_core_ atd.). Základní pojmy tam jsou:

![RGB-Bitcoin](assets/fr/046.webp)

V příští kapitole se podíváme na čistě neřetězcovou složku RGB, konkrétně na logiku smluv. Uvidíme, jak kontrakty RGB, organizované jako částečně replikované _konečné stavové stroje_, dosahují mnohem vyšší expresivity než bitcoinové skripty a zároveň zachovávají důvěrnost svých dat.

## Úvod do chytrých smluv a jejich stavů

<chapterId>04a9569f-3563-5382-bf53-0c7069343ba0</chapterId>

![video](https://youtu.be/tmAVdyXGmj4)

V této a následující kapitole se budeme zabývat pojmem **chytrá smlouva** v prostředí RGB a prozkoumáme různé způsoby, jakými mohou tyto smlouvy definovat a vyvíjet svůj *stav*. Uvidíme, proč architektura RGB pomocí uspořádané posloupnosti jednorázových pečetí umožňuje provádět různé typy ***smluvních operací*** škálovatelným způsobem a bez průchodu centralizovaným registrem. Podíváme se také na zásadní roli ***Business Logic*** v rámci vývoje stavu smlouvy.

### Inteligentní smlouvy a práva na digitální nosiče

Cílem RGB je poskytnout infrastrukturu pro implementaci chytrých smluv na Bitcoinu. Pod pojmem "chytrá smlouva" rozumíme dohodu mezi několika stranami, která je automaticky a výpočetně vynucována bez lidského zásahu k vynucení ustanovení. Jinými slovy, právo smlouvy je vynucováno softwarem, nikoli důvěryhodnou třetí stranou.

Tato automatizace vyvolává otázku decentralizace: jak se můžeme osvobodit od centralizovaného registru (např. centrální platformy nebo databáze) pro správu vlastnictví a plnění smluv? Původní myšlenkou, kterou převzala organizace RGB, je návrat ke způsobu vlastnictví známému jako "nástroje na doručitele". Historicky byly některé cenné papíry (dluhopisy, akcie atd.) vydávány ve formě na doručitele, což umožňovalo každému, kdo dokument fyzicky vlastnil, uplatnit svá práva.

![RGB-Bitcoin](assets/fr/055.webp)

RGB tento koncept aplikuje na digitální svět: práva (a povinnosti) jsou zapouzdřena v datech, se kterými se manipuluje mimo řetězec, a stav těchto dat ověřují sami účastníci. To umožňuje a priori mnohem větší míru důvěrnosti a nezávislosti, než jakou nabízejí jiné přístupy založené na veřejných rejstřících.

### Úvod do inteligentní smlouvy Stav RGB

Na inteligentní smlouvu v RGB lze pohlížet jako na stavový stroj definovaný pomocí :


- **Stav**, tj. soubor informací odrážející aktuální konfiguraci smlouvy;
- **Business logika** (soubor pravidel), která popisuje, za jakých podmínek a kdo může stav změnit.

![RGB-Bitcoin](assets/fr/056.webp)

Je důležité si uvědomit, že tyto smlouvy se neomezují na pouhý převod tokenů. Mohou ztělesňovat širokou škálu aplikací: od tradičních aktiv (tokeny, akcie, dluhopisy) až po složitější mechanismy (práva na užívání, obchodní podmínky atd.). Na rozdíl od jiných blockchainů, kde je kód smlouvy přístupný a spustitelný pro všechny, přístup RGB rozděluje přístup a znalost smlouvy na účastníky ("***účastníci smlouvy***"). Existuje několik rolí:


- Emitent** nebo tvůrce smlouvy, který definuje genezi smlouvy a její počáteční proměnné;
- Strany s právy** (*vlastnictví*) nebo jinými možnostmi vymáhání ;
- Pozorovatelé**, kteří mohou vidět pouze určité informace, ale nemohou vyvolat změny.

Toto rozdělení rolí přispívá k odolnosti vůči cenzuře tím, že zajišťuje, aby se smluvním státem mohly komunikovat pouze oprávněné osoby. Dává RGB také možnost horizontálního škálování: většina validací probíhá mimo blockchain a do Bitcoinu se zapisují pouze kryptografické kotvy (*závazky*).

### Stav a obchodní logika v RGB

Z praktického hlediska má **obchodní logika** smlouvy podobu pravidel a skriptů definovaných v tzv. schématu**. Schéma kóduje :


- Struktura státu (která pole jsou veřejná? Která pole jsou ve vlastnictví kterých stran?
- Podmínky platnosti (co je třeba zkontrolovat před povolením aktualizace stavu?) ;
- Oprávnění (kdo může iniciovat *přechod státu*? Kdo může pouze přihlížet?).

Současně se **smluvní stát** často rozpadá na dvě složky:


- **Globální stav**: veřejná část, kterou mohou sledovat všichni (v závislosti na konfiguraci);
- Vlastněné státy**: soukromé části, přidělené konkrétně vlastníkům prostřednictvím UTXO, na které se odkazuje logika smlouvy.

Jak uvidíme v následujících kapitolách, každá aktualizace stavu (*Smluvní operace*) musí být spojena s _závazkem_ Bitcoinu (prostřednictvím `Opret` nebo `Tapret`) a musí být v souladu se skripty *Business Logic*, aby byla považována za platnou.

### Smluvní operace: vznik a vývoj státu

Ve světě RGB je ***Smluvní operace*** jakákoli událost, která změní smlouvu ze **starého stavu** do **nového stavu**. Tyto operace se řídí následující logikou:


- Bereme na vědomí aktuální stav smlouvy;
- Aplikujeme pravidlo nebo operaci (***Přechod stavu***, ***Geneze***, pokud se jedná o úplně první stav, nebo ***Prodloužení stavu***, pokud existuje veřejná *valence* pro opětovné spuštění);
- Změnu ukotvíme prostřednictvím nového _commitmentu_ v blockchainu, čímž uzavřeme jednu _jednorázovou pečeť_ a vytvoříme další;
- Příslušní držitelé práv lokálně (na straně klienta*) ověří, že přechod je v souladu se *Schématem* a že související transakce Bitcoin je registrována v řetězci.

![RGB-Bitcoin](assets/fr/057.webp)

Konečným výsledkem je aktualizovaná smlouva, nyní s jiným stavem. Tento přechod nevyžaduje, aby se detaily zabývala celá síť Bitcoin, protože v blockchainu je zaznamenán pouze malý kryptografický otisk (_commitment_). Sekvence pečetí na jedno použití zabraňuje jakémukoli dvojímu utracení nebo dvojímu použití stavu.

### Operační řetězec: od Genesis po terminální stav

Abychom to uvedli na pravou míru, inteligentní smlouva RGB začíná s **Genesis**, což je úplně první stav. Poté na sebe navazují různé operace kontraktu, které tvoří DAG (*Directed Acyclic Graph*) operací:


- Každý přechod je založen na předchozím stavu (nebo několika, v případě konvergentních přechodů);
- Chronologické pořadí je zaručeno zahrnutím každého přechodu do kotvy bitcoinu, která je časově označena a nezměnitelná díky konsenzu Proof-of-Work ;
- Pokud již neprobíhají žádné další operace, je dosaženo **koncového stavu**: posledního a úplného stavu smlouvy.

![RGB-Bitcoin](assets/fr/012.webp)

Tato topologie DAG (namísto jednoduchého lineárního řetězce) odráží možnost, že se různé části smlouvy mohou vyvíjet paralelně, pokud si navzájem neodporují. RGB se pak stará o to, aby se zabránilo jakýmkoli nesrovnalostem pomocí *ověřování na straně klienta* každého zúčastněného účastníka.

### Souhrn

Inteligentní smlouvy v RGB zavádějí model digitálních nástrojů na doručitele, decentralizovaných, ale ukotvených v Bitcoinu pro časové razítkování a zaručení pořadí transakcí. Automatizované provádění těchto smluv je založeno na :


- **Stav smlouvy*, který udává aktuální konfiguraci smlouvy (práva, zůstatky, proměnné atd.);
- **Business logika** (*Schema*), která definuje, které přechody jsou povoleny a jak musí být ověřeny;
- Contract Operations**, které tento stav postupně aktualizují díky závazkům ukotveným v bitcoinových transakcích.

V příští kapitole se budeme podrobněji zabývat konkrétní reprezentací těchto ***stavů*** a ***přechodů mezi stavy*** na úrovni mimo řetězec a jejich vztahem k UTXO a jednorázovým pečetím zabudovaným v Bitcoinu. To bude příležitost podívat se, jak vnitřní mechanika RGB, založená na ověřování na straně klienta, dokáže udržet konzistenci chytrých kontraktů a zároveň zachovat důvěrnost dat.

## Smluvní operace RGB

<chapterId>78c44e88-50c4-5ec4-befe-456c1a9f080b</chapterId>

![video](https://youtu.be/lUTjeuM0oTA)

V této kapitole se podíváme na to, jak fungují operace v chytrých smlouvách a přechody mezi stavy, opět v rámci protokolu RGB. Cílem bude také pochopit, jak několik účastníků spolupracuje na převodu vlastnictví aktiva.

### Přechody stavů a jejich mechanika

Obecným principem je stále princip ověřování na straně klienta, kdy jsou údaje o stavu uchovávány vlastníkem a ověřovány příjemcem. Specifičnost u RGB zde však spočívá v tom, že Bob jako příjemce žádá Alici o začlenění určitých informací do smluvních dat, aby měl skutečnou kontrolu nad přijatým aktivem, a to prostřednictvím skrytého odkazu na jeden ze svých UTXO.

Pro ilustraci procesu *přechodu stavu* (což je jedna ze základních ***smluvních operací*** v RGB) si uveďme příklad převodu majetku mezi Alicí a Bobem krok za krokem:

**Počáteční situace:**

Alice má ***sklad RGB*** lokálně ověřených dat (*na straně klienta*). Tato skrýš se vztahuje k jednomu z jejích UTXO na Bitcoinu. To znamená, že _definice pečeti_ v těchto datech ukazuje na UTXO patřící Alici. Smyslem je umožnit jí převést určitá digitální práva spojená s aktivem (např. RGB tokeny) na Boba.

![RGB-Bitcoin](assets/fr/058.webp)

**Bob má také UTXO :**

Na druhé straně Bob má alespoň jedno vlastní UTXO bez přímého spojení s Alenčiným. V případě, že Bob nemá UTXO, je stále možné provést převod na něj pomocí samotné *svědecké transakce*: výstup této transakce pak bude obsahovat závazek (_commitment_) a implicitně spojí vlastnictví nové smlouvy s Bobem.

![RGB-Bitcoin](assets/fr/059.webp)

**Výstavba nové nemovitosti (*Nový stav*) :**

Bob pošle Alici informaci zakódovanou ve formě faktury*** (podrobněji se konstrukci faktury budeme věnovat v dalších kapitolách) a požádá ji o vytvoření nového stavu, který odpovídá pravidlům smlouvy. Tento stav bude obsahovat novou *definici pečetě*, která bude ukazovat na jeden z Bobových UTXO. Tímto způsobem získá Bob vlastnictví aktiv definovaných v tomto novém stavu, například určitého množství žetonů RGB.

![RGB-Bitcoin](assets/fr/060.webp)

**Příprava vzorové transakce:**

Alice pak vytvoří transakci Bitcoin, při které utratí UTXO, na který se odkazuje v předchozí pečeti (ta, která ji legitimovala jako držitele). Do výstupu této transakce se vloží *závazek* (prostřednictvím `Opret` nebo `Tapret`), který ukotví nový stav RGB. Závazky `Opret` nebo `Tapret` jsou odvozeny ze stromu *MPC* (jak jsme viděli v předchozích kapitolách), který může agregovat několik přechodů z různých smluv.

**Předání zásilky Bobovi:**

Před odvysíláním transakce Alice pošle Bobovi zprávu ***Consignment*** obsahující všechna potřebná data na straně klienta (jeho *stash*) a informace o novém stavu v Bobův prospěch. V tomto okamžiku Bob použije pravidla konsensu RGB:


- Ověří všechna data RGB obsažená v *Consignment*, včetně nového stavu, který mu uděluje vlastnictví aktiva;
- Na základě *Anchors* obsažených v *Consignment* ověřuje chronologii svědeckých transakcí (od Genesis po nejnovější přechod) a ověřuje odpovídající závazky v blockchainu.

**Dokončení přechodu:**

Pokud je Bob spokojen, může dát svůj souhlas (například podpisem *zaslání*). Alice pak může vysílat připravenou vzorovou transakci. Po potvrzení se tím uzavře pečeť, kterou předtím držela Alice, a formalizuje se vlastnictví Boba. Zabezpečení proti dvojímu utracení je pak založeno na stejném mechanismu jako v Bitcoinu: UTXO je utraceno, což dokazuje, že Alice jej již nemůže znovu použít.

![RGB-Bitcoin](assets/fr/061.webp)

Nový stav nyní odkazuje na Bobův UTXO, čímž Bob získává vlastnictví, které dříve vlastnila Alice. Výstup Bitcoinu, kde jsou ukotvena data RGB, se stává neodvolatelným důkazem převodu vlastnictví.

Příklad minimálního DAG (*Directed Acyclic Graph*) zahrnujícího dvě smluvní operace (**Genesis** a poté ***State Transition***) může ilustrovat, jak se stav RGB (vrstva *client-side*, červeně) připojuje k blockchainu Bitcoin (vrstva *Commitment*, oranžově).

![RGB-Bitcoin](assets/fr/062.webp)

Ukazuje, že Genesis definuje pečeť (*definice pečetě*), poté *přechod stavu* tuto pečeť uzavře a vytvoří novou v jiném UTXO.

V této souvislosti si připomeňme několik terminologických poznámek:


- ***Zadání*** kombinuje :
    - Definice těsnění*** (která ukazuje na UTXO);
    - Vlastněné stavy**, tj. údaje spojené s vlastnictvím (například množství převedených tokenů).
- **Globální stav** sdružuje obecné vlastnosti smlouvy, které jsou viditelné pro všechny a zajišťují globální konzistenci vývoje.

Přechody mezi stavy**, popsané v předchozí kapitole, jsou hlavní formou operace se smlouvou. Odkazují na jeden nebo více předchozích stavů (z Genesis nebo jiného Přechodu stavu) a aktualizují je na nový stav.

![RGB-Bitcoin](assets/fr/063.webp)

Tento diagram ukazuje, jak lze ve svazku *Přechod stavu* v rámci jedné vzorové transakce uzavřít několik pečetí a současně otevřít nové pečetě. Zajímavou vlastností protokolu RGB je totiž jeho schopnost škálování: několik přechodů lze agregovat do Svazku přechodů, přičemž každé agregaci je přiřazen samostatný list stromu *MPC* (jedinečný identifikátor svazku). Díky mechanismu *Deterministic Bitcoin Commitment* (DBC) se celá zpráva vloží do výstupu `Tapret` nebo `Opret`, přičemž se uzavřou předchozí pečetě a případně se definují nové. `Kotva* slouží jako přímé spojení mezi závazkem uloženým v blockchainu a validační strukturou na straně klienta (*klientská strana*).

V následujících kapitolách se podíváme na všechny součásti a procesy spojené s vytvářením a ověřováním přechodu stavu. Většina těchto prvků je součástí konsensu RGB, který je implementován v knihovně **RGB Core Library**.

### Přechodový balíček

V systému RGB je možné spojovat různé stavové přechody patřící ke stejné smlouvě (tj. sdílející stejné **ContractId**, odvozené od Genesis **OpId**). V nejjednodušším případě, jako mezi Alicí a Bobem ve výše uvedeném příkladu, obsahuje **svazek přechodů** pouze jeden přechod. Podpora operací s více uživateli (jako je např. spojování mincí, otevírání kanálů Lightning atd.) však znamená, že několik uživatelů může kombinovat své stavové přechody v jednom svazku.

Po shromáždění jsou tyto přechody ukotveny (mechanismem MPC + DBC) v jedné transakci Bitcoin:


- Každý přechod stavu je zaheslován a seskupen do svazku přechodů ;
- Přechodový svazek je sám zaheslován a vložen do listu stromu MPC odpovídajícího této smlouvě (BundleId);
- Strom MPC je nakonec zapojen prostřednictvím `Opret` nebo `Tapret` v transakci svědka, která tak uzavře spotřebované pečetě a definuje nové pečetě.

Technicky vzato se **BundleId** vložený do listu MPC získá z tagovaného hashe použitého na striktní serializaci pole *InputMap* svazku:

```txt
BundleId = SHA256( SHA256(bundle_tag) || SHA256(bundle_tag) || InputMap )
```

V němž `bundle_tag = urn:lnp-bp:rgb:bundle#2024-02-03` například.

*InputMap* je datová struktura, která pro každý vstup `i` vzorové transakce uvádí odkaz na *OpId* odpovídajícího přechodu stavu. Například:

```txt
InputMap =
N               input_0    OpId(input_0)    input_1    OpId(input_1)   ...    input_N-1  OpId(input_N-1)
|____________________| |_________||______________| |_________||______________|       |__________||_______________|
16-bit Little Endian   32-bit LE   32-byte hash
|_________________________| |_________________________|  ...  |___________________________|
MapElement1                MapElement2                       MapElementN
```


- `N` je celkový počet záznamů v transakci, které odkazují na `OpId`;
- opId(input_j)` je identifikátor operace jednoho ze stavových přechodů přítomných ve svazku.

Tím, že se na každou položku odkazuje pouze jednou a uspořádaně, zabráníme tomu, aby se stejná pečeť použila dvakrát při dvou současných přechodech stavu.

### Generování stavu a aktivní stav

Převody státu lze tedy použít k převodu vlastnictví majetku z jedné osoby na druhou. Nejsou to však jediné možné operace v protokolu RGB. Protokol definuje tři **smluvní operace** :


- Přechod stavu** ;
- Genesis** ;
- Státní prodloužení**.

Z nich se **Genesis** a **Prodloužení stavu** někdy nazývají "operace generování stavu*", protože vytvářejí nové stavy bez okamžitého uzavření některého z nich. To je velmi důležitý bod: **Genesis** a **Prodloužení stavu** nezahrnují uzavření pečeti. Spíše definují novou pečeť, která pak musí být utracena následnou operací **Přechod stavu**, aby byla skutečně potvrzena v historii blockchainu.

![RGB-Bitcoin](assets/fr/064.webp)

**Aktivní stav** kontraktu je často definován jako množina posledních stavů vyplývajících z historie (DAG) transakcí, počínaje Genesis a po všech kotvách v blockchainu Bitcoinu. Všechny staré stavy, které jsou již zastaralé (tj. připojené k vyčerpaným UTXO), se již nepovažují za aktivní, ale zůstávají zásadní pro kontrolu konzistence historie.

### Genesis

Genesis je výchozím bodem každé smlouvy RGB. Vytváří ji emitent smlouvy a definuje počáteční parametry v souladu se **Schématem**. V případě tokenu RGB může Genesis specifikovat například :


- Počet původně vytvořených žetonů a jejich vlastníků;
- Celkový strop možných emisí ;
- Případná pravidla pro opětovné vydání a to, kteří účastníci jsou způsobilí.

Vzhledem k tomu, že se jedná o první transakci ve smlouvě, neodkazuje Genesis na žádný předchozí stav a neuzavírá žádnou pečeť. Aby se však Genesis objevil v historii a byl ověřen, musí být **konzumován** (uzavřen) prvním přechodem stavu (často transakcí skenování/autorizace pro samotného emitenta nebo počáteční distribucí uživatelům).

### Státní prodloužení

Rozšíření stavu** nabízí originální funkci pro chytré kontrakty. Umožňují vykoupit určitá digitální práva (*Valence*) stanovená v definici kontraktu, aniž by bylo nutné pečeť okamžitě uzavřít. Nejčastěji se to týká :


- Distribuované emise tokenů;
- Mechanismy výměny aktiv ;
- Podmíněné opětovné vydání (které může zahrnovat zničení jiných aktiv atd.).

Technicky řečeno, rozšíření stavu odkazuje na *Redeem* (konkrétní typ vstupu RGB), který odpovídá dříve definované *Valenci* (například v Genesis nebo jiném Přechodu stavu). Definuje novou pečeť, která je k dispozici osobě nebo stavu, který ji využívá. Aby se tato pečeť stala účinnou, musí být vynaložena následným Přechodem stavu.

![RGB-Bitcoin](assets/fr/065.webp)

Například: Genesis vytváří právo na vydání (*Valence*). To může uplatnit oprávněný aktér, který pak vybuduje státní rozšíření :


- Odkazuje na valenci (redeem);
- Vytvoří nové *přidělení* (nová data *vlastního stavu*) ukazující na UTXO ;
- Budoucí přechod stavu, který vydá vlastník tohoto nového UTXO, skutečně převede nebo distribuuje nově vydané tokeny.

### Součásti smluvní operace

Nyní bych se rád podrobněji podíval na jednotlivé prvky **smluvní operace** v RGB. Operace smlouvy je akce, která mění stav smlouvy a která je na straně klienta deterministicky ověřována oprávněným příjemcem. Konkrétně uvidíme, jak smluvní operace zohledňuje na jedné straně **starý stav** (*Old State*) smlouvy a na druhé straně definici **nového stavu** (*New State*).

```txt
+---------------------------------------------------------------------------------------------------------------------+
|  Contract Operation                                                                                                 |
|                                                                                                                     |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|  | Ffv |     | ContractId | SchemaId |      | TransitionType | ExtensionType |      | Testnet |     | AltLayers1 |  |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Metadata                                      |  | Global State                                               |  |
|  |                                               |  | +----------------------------------+                       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  | |          Structured Data            |       |  | | |  GlobalStateType  | |  Data  | |     ...     ...       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  |                                               |  | +----------------------------------+                       |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|                                                                                                                     +---------> OpId |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|  | Inputs                                        |  | Assignments                                                |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #1                                  | |  | | Assignment #1                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ + ---------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #2                                  | |  | | Assignment #2                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  |       ...           ...          ...          |  |     ...          ...             ...                       |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Redeems                                       |  | Valencies                                                  |  |
|  |                                               |  |                                                            |  |
|  | +------------------------------+              |  |                                                            |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
| OpId +--------------> PrevOpId | | ValencyType | |  ...   ...   |  |  | ValencyType |  | ValencyType |         ...              |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
|  | +------------------------------+              |  |                                                            |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------+
```

Pokud se podíváme na výše uvedený diagram, vidíme, že operace smlouvy obsahuje prvky odkazující na **Nový stav** a další prvky odkazující na aktualizovaný **Starý stav**.

Prvky **Nového státu** jsou :


- Zadání**, ve kterých jsou definovány :
 - Definice **těsnění**;
 - **Vlastní stát**.
- **Globální stát**, který lze upravit nebo obohatit ;
- Valence**, případně definované ve stavu Přechod nebo Genesis.

Na **Starý stát** se odkazuje prostřednictvím :


- Vstupy**, které ukazují na *Připojení* předchozích stavových přechodů (v Genesis nejsou);
- Redeems**, které se vztahují k dříve definovaným valencím (pouze ve State Extensions).

Kromě toho obsahuje smluvní operace obecnější pole specifická pro danou operaci:


- ffv` (*Rychlá verze dopředu*): 2bajtové celé číslo označující verzi smlouvy;
- transitionType` nebo ExtensionType`: 16bitové celé číslo určující typ přechodu nebo rozšíření podle obchodní logiky;
- `ContractId`: genesis: 32bajtové číslo odkazující na *OpId* smlouvy. Zahrnuto v Transitions a Extensions, ale ne v Genesis ;
- schemaId: je uveden pouze v Genesis, jedná se o 32bajtový hash reprezentující strukturu (*Schema*) smlouvy;
- testnet`: V případě, že se nacházíte v síti Testnet nebo Mainnet, je třeba použít tento parametr: Boolean určující, zda jste v síti Testnet nebo Mainnet. Pouze Genesis;
- altlayers1`: proměnná identifikující alternativní vrstvu (sidechain nebo jinou) použitou k ukotvení dat kromě Bitcoinu. Přítomna pouze v Genesis ;
- metadata": pole, které může uchovávat dočasné informace, užitečné pro ověřování složité smlouvy, které však nesmí být zaznamenány v historii konečného stavu.

Nakonec se všechna tato pole zkondenzují pomocí vlastního procesu hashování, aby se získal jedinečný otisk prstu, `OpId`. Toto `OpId` je pak integrováno do přechodového svazku, což umožňuje jeho ověření a validaci v rámci protokolu.

Každá *smluvní operace* je proto identifikována 32bajtovým hashem s názvem `OpId`. Tento hash se vypočítá pomocí hashe SHA256 všech prvků tvořících operaci. Jinými slovy, každá *Smluvní operace* má svůj vlastní kryptografický závazek, který obsahuje všechny údaje potřebné k ověření pravosti a konzistence operace.

Smlouva RGB je pak identifikována pomocí `ContractId`, odvozeného od `OpId` Genesis (protože před Genesis neexistuje žádná operace). Konkrétně vezmeme `OpId` Genesis, obrátíme pořadí bajtů a použijeme kódování Base58. Toto kódování usnadňuje zpracování a rozpoznání `ContractId`.

### Metody a pravidla aktualizace stavu

**Stav smlouvy** představuje soubor informací, které musí protokol RGB sledovat pro danou smlouvu. Skládá se z :


- Jeden globální stav**: jedná se o veřejnou, globální část smlouvy, která je viditelná pro všechny;
- Jeden nebo více vlastněných států**: každý vlastněný stát je spojen s jedinečnou pečetí (a tedy UTXO na Bitcoinu). Rozlišuje se mezi :
    - Státy ve **veřejném** vlastnictví,
    - Státy ve **soukromém** vlastnictví.

![RGB-Bitcoin](assets/fr/066.webp)

*Globální stav* je přímo zahrnut do *Smluvní operace* jako jeden blok. *Vlastní stavy* jsou definovány v každém *Přidělení* spolu s *Definice těsnění*.

Hlavním rysem RGB je způsob, jakým se upravuje globální stav a vlastní stavy. Obecně existují dva typy chování:


- Mutable**: je-li stavový prvek popsán jako mutabilní, každá nová operace nahradí předchozí stav novým stavem. Stará data jsou pak považována za zastaralá;
- Akumulační**: pokud je stavový prvek definován jako akumulační, každá nová operace přidává nové informace k předchozímu stavu, aniž by jej přepisovala. Výsledkem je jakási kumulovaná historie.

Není-li ve smlouvě prvek stavu definován jako proměnlivý nebo kumulativní, zůstane tento prvek pro následné operace prázdný (jinými slovy, pro toto pole neexistují žádné nové verze). O tom, zda je stav (globální nebo vlastní) proměnlivý, kumulativní nebo pevný, rozhoduje schéma smlouvy (tj. kódovaná obchodní logika). Po definování Geneze lze tyto vlastnosti měnit pouze tehdy, pokud to samotný kontrakt umožňuje, například prostřednictvím specifického rozšíření stavu.

Následující tabulka ukazuje, jak mohou jednotlivé typy smluvních operací manipulovat (nebo nemanipulovat) s globálním stavem a vlastněným stavem:

| Geneze | Rozšíření stavu | Přechod stavu |

| ---------------------------- | :-----: | :-------------: | :--------------: |

| **Přidání globálního stavu** | + | - | + |

| n/a | - | + | **Mutace globálního stavu** | - | + |

| **Přidání vlastního státu** | + | - | + | |

| **Mutace vlastněného stavu** | n/a | Ne | + |

| **Přidání valencí** | + | + | + | + | |

**`+`** : akce je možná, pokud to schéma smlouvy umožňuje.

**`-`**: operace musí být potvrzena následným přechodem stavu (samotné prodloužení stavu neuzavře jednorázovou pečeť).

Kromě toho lze v následující tabulce rozlišit časový rozsah a práva aktualizace jednotlivých typů dat:

| Metadata | Globální stav | Vlastní stav |

| ------------------------------- | ---------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |

| Definováno pro jednu operaci smlouvy | Definováno globálně pro smlouvu | Definováno pro každou plombu (*Přidělení*) | Definováno pro jednu operaci smlouvy | Definováno globálně pro smlouvu | Definováno pro každou plombu (*Přidělení*) | Definováno pro každou plombu (*Přidělení*) | Definováno pro každou smlouvu

| Neaktualizovatelné (efemérní údaje) | Transakce vydaná aktéry (emitentem atd.) | Závisí na oprávněném držiteli pečeti (ten, kdo ji může utratit v následné transakci) |

| Stav je definován před operací (podle *definice těsnění* předchozí operace) | Stav je stanoven na konci operace | Stav je stanoven na konci operace | Stav je definován před operací (podle *definice těsnění* předchozí operace) | Stav je stanoven na konci operace | Stav je definován před operací (podle *definice těsnění* předchozí operace)

### Globální stát

Globální stát je často popisován jako "nikdo nevlastní, všichni vědí". Obsahuje obecné informace o smlouvě, které jsou veřejně viditelné. Například u kontraktu vydávajícího tokeny potenciálně obsahuje :


- Ticker (symbolická zkratka tokenu): `ticker` ;
- Úplný název tokenu: `name` ;
- Přesnost (počet desetinných míst): `přesnost` ;
- Počáteční nabídka (a/nebo maximální limit tokenů): `issuedSupply` ;
- Datum vydání: `vytvořeno` ;
- Právní údaje nebo jiné veřejné informace: `data`.

Tento globální stav může být umístěn na veřejných zdrojích (webové stránky, IPFS, Nostr, Torrent atd.) a distribuován komunitě. Také ekonomická motivace (potřeba držet a přenášet tyto tokeny atd.) přirozeně vede smluvní uživatele k tomu, aby tato data sami udržovali a šířili.

### Zadání

*Přiřazení* je základní strukturou pro definování :


- Plomba (*Definice plomby*), která ukazuje na konkrétní UTXO;
- *Vlastní stav*, tj. vlastnost nebo data spojená s touto pečetí.

*Přidělení* lze považovat za obdobu výstupu transakce Bitcoin, ale s větší flexibilitou. V tom spočívá logika převodu majetku: *Assignment* spojuje určitý typ majetku nebo práva (`AssignmentType`) s pečetí. Ten, kdo vlastní soukromý klíč UTXO spojený s touto pečetí (nebo ten, kdo může toto UTXO utratit), je považován za vlastníka tohoto *Vlastněného stavu*.

Jedna z velkých předností systému RGB spočívá v možnosti libovolně odhalit (*odhalit*) nebo skrýt (*skrýt*) pole *Definice těsnění* a *Vlastní stav*. To nabízí silnou kombinaci důvěrnosti a selektivity. Můžete například prokázat, že přechod je platný, aniž byste odhalili všechna data, a to tak, že odhalenou verzi poskytnete osobě, která má přechod ověřit, zatímco třetí strany uvidí pouze skrytou verzi (hash). V praxi se `OpId` přechodu vždy počítá ze *skrytých* dat.

![RGB-Bitcoin](assets/fr/067.webp)

#### Definice pečeti

Definice *Těsnění* má v odhalené podobě čtyři základní pole: `txptr`, `vout`, `blinding` a `method` :


- txptr**: toto je odkaz na UTXO v systému Bitcoin :
    - V případě pečeti **Genesis** ukazuje přímo na existující UTXO (ten, který je spojen s Genesis);
    - V případě **Grafické pečeti** můžeme mít :
        - Jednoduché `txid`, pokud ukazuje na konkrétní UTXO,
        - Nebo `WitnessTx`, který označuje autoreferenci: pečeť ukazuje na samotnou transakci. To je užitečné zejména v případech, kdy není k dispozici externí UTXO, například při transakcích otevírání kanálů Lightning, nebo pokud příjemce nemá UTXO.
- vout** : výstupní číslo transakce označené `txptr`. Uvádí se pouze pro standardní pečeť Graph (nikoli pro `WitnessTx`);
- blinding**: náhodné číslo o velikosti 8 bajtů, které má posílit důvěrnost a zabránit pokusům o zjištění identity UTXO hrubou silou;
- method** : označuje použitou metodu ukotvení (`Tapret` nebo `Opret`).

*Skrytá* podoba definice pečeti je hash SHA256 (označený) konkatenace těchto 4 polí s označením specifickým pro RGB.

![RGB-Bitcoin](assets/fr/068.webp)

#### Vlastněné státy

Druhou složkou *Přidělení* je Vlastní stav. Na rozdíl od globálního stavu může existovat ve veřejné nebo soukromé podobě:


- Stát ve veřejném vlastnictví**: každý zná údaje spojené s pečetí. Například veřejný obraz;
- Soukromý stav**: data jsou skrytá, známá pouze vlastníkovi (a případně validátoru, pokud je to nutné). Například počet držených tokenů.

RGB definuje čtyři možné typy stavů (*StateTypes*) pro vlastní stav:


- Deklarativní**: neobsahuje žádné číselné údaje, pouze deklarativní právo (např. právo volit). Skrytá a zjevná forma jsou totožné;
- Fungible**: představuje zastupitelné množství (jako žetony). V odhalené podobě máme `mount` a `blinding`. Ve skryté podobě máme jediný *Pedersenův závazek*, který skrývá množství a zaslepení;
- Strukturovaný**: ukládá strukturovaná data (až 64 kB). V odhalené podobě je to datový blob. Ve skryté podobě je to označený hash tohoto blobu:

```txt
SHA-256(SHA-256(tag_data) || SHA-256(tag_data) || blob)
```

Například s :

```txt
tag_data = urn:lnp-bp:rgb:state-data#2024-02-12
```


- Attachments**: propojí soubor (audio, obrázek, binární soubor atd.) s Vlastním stavem a uloží hash souboru `file_hash`, typ MIME `media type` a kryptografickou sůl `salt`. Samotný soubor je umístěn jinde. Ve skryté podobě je to hash označený třemi předchozími datovými položkami:

```txt
SHA-256(SHA-256(tag_attachment) || SHA-256(tag_attachment) || file_hash || media_type || salt)
```

Například s :

```txt
tag_attachment = urn:rgb:state-attach#2024-02-12
```

Shrňme si 4 možné typy stavu ve veřejné a skryté podobě:

```txt
State                      Concealed form                              Revealed form
+---------------------------------------------------------------------------------------------------------
+--------------------------------------------------------------------------------+
|                                                                                |
Declarative        |                              < void >                                          |
|                                                                                |
+--------------------------------------------------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------+ +----------+       |
Fungible           | | Pedersen Commitement | | <========== |         | Amount | | Blinding |       |
| +----------------------+ |             |         +--------+ +----------+       |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------------------+        |
Structured         | |     Tagged Hash      | | <========== |         |     Data Blob      |        |
| +----------------------+ |             |         +--------------------+        |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             | +-----------+ +------------+ +------+ |
Attachments        | |     Tagged Hash      | | <========== | | File Hash | | Media Type | | Salt | |
| +----------------------+ |             | +-----------+ +------------+ +------+ |
+--------------------------+             +---------------------------------------+
```

| **Deklarativní** | **Fungující** | **Strukturované** | **Přílohy** | **Přílohy**

| --------------------- | -------------- | ------------------------------------ | ----------------------------- | ---------------------------- |

| Žádný | 64bitové celé číslo se znaménkem nebo bez znaménka | Jakýkoli striktní datový typ | Jakýkoli soubor |

| Typ informace** | Žádné | Signované nebo nepodepsané | Přísné typy | Typ MIME |

| Pedersenův závazek | Hashování se zaslepením | Hashované ID souboru

| Omezení velikosti** | N/A | 256 bajtů | Až 64 KB | Až ~500 Gb |

### Vstupy

Vstupy operace *Smlouva* se vztahují k *Přidělením*, která jsou v této nové operaci použita. Vstup označuje :


- prevOpId` : identifikátor (`OpId`) předchozí operace, ve které se nacházelo *Přidělení*;
- assignmentType` : typ *Assignment* (například `assetOwner` pro token) ;
- `Index`: index *Přidělení* v seznamu přiřazeném předchozímu `OpId`, určený po lexikografickém seřazení skrytých pečetí.

Vstupy se v Genesis nikdy neobjeví, protože neexistují žádná předchozí Přiřazení. Neobjevují se ani v Rozšířeních stavu (protože Rozšíření stavu neuzavírají pečetě, ale nadefinovávají nové pečetě na základě Valencí).

Pokud máme Vlastní stavy typu `Fungible`, ověřovací logika (prostřednictvím skriptu AluVM uvedeného ve Schématu) kontroluje konzistenci součtů: součet příchozích tokenů (*Inputs*) se musí rovnat součtu odchozích tokenů (v nových *Assignments*).

### Metadata

Pole **Metadata** může mít velikost až 64 KiB a slouží k zahrnutí dočasných údajů užitečných pro ověření, které však nejsou integrovány do trvalého stavu smlouvy. Zde mohou být například uloženy meziproměnné pro výpočet složitých skriptů. Toto pole není určeno k ukládání do globální historie, proto je mimo oblast působnosti Vlastních stavů nebo Globálního stavu.

### Valence

Valence** jsou originálním mechanismem protokolu RGB. Lze je nalézt v Genesis, State Transitions nebo State Extensions. Představují číselná práva, která mohou být aktivována Rozšířením stavu (prostřednictvím *Redeems*) a poté dokončena následným Přechodem. Každá Valence je identifikována pomocí `ValencyType` (16 bitů). Její sémantika (právo na opětovné vydání, výměna tokenu, právo na spálení atd.) je definována ve Schématu.

Konkrétně bychom si mohli představit Genesis definující valenci "právo na opětovné vydání". Rozšíření státu ji spotřebuje (*Redeem*), pokud jsou splněny určité podmínky, aby zavedlo nové množství tokenů. Přechod stavu vycházející od držitele takto vytvořené pečeti pak může tyto nové tokeny převést.

### Vykoupí

Redeemy jsou valenčním ekvivalentem vstupů pro přiřazení. Objevují se pouze v Rozšířeních stavu, protože zde se aktivuje dříve definovaná Valence. Redeem se skládá ze dvou polí:


- `PrevOpId` : `OpId` operace, u které byla zadána platnost;
- `ValencyType`: typ valence, který chcete aktivovat (každý `ValencyType` může být použit pouze jednou v rámci rozšíření státu).

Příklad: Redeem může odpovídat provedení výměny mincí v závislosti na tom, co bylo zakódováno ve Valencii.

### Stavové charakteristiky RGB

Nyní se podíváme na několik základních charakteristik stavu RGB. Zejména se podíváme na :


- **Strict Type System**, který zavádí přesnou a typizovanou organizaci dat;
- Důležitost oddělení **potvrzení** od **vlastnictví** ;
- Systém **konsensuální evoluce** v RGB, který zahrnuje pojmy *rychlý posun vpřed* a *přesun zpět*.

Jako vždy mějte na paměti, že vše, co souvisí se stavem smlouvy, se ověřuje na straně klienta podle pravidel konsensu stanovených v protokolu, jehož konečná kryptografická reference je ukotvena v transakcích Bitcoinu.

#### Přísný typový systém

RGB používá *Strict Type System* a deterministický režim serializace (*Strict Encoding*). Tato organizace je navržena tak, aby zaručovala dokonalou reprodukovatelnost a přesnost při definování, zpracování a ověřování smluvních údajů.

V mnoha programovacích prostředích (JSON, YAML...) může být datová struktura flexibilní, dokonce až příliš liberální. Naproti tomu v RGB jsou Struktura a Typy jednotlivých polí definovány explicitními omezeními. Například :


- Každá proměnná má specifický typ (například 8bitové celé číslo bez znaménka `u8` nebo 16bitové celé číslo se znaménkem atd.);
- Typy lze skládat (vnořené typy). To znamená, že můžete definovat typ založený na jiných typech (např. agregovaný typ obsahující pole `u8`, pole `bool` atd.);
- Lze také zadat kolekce: seznamy (*list*), množiny (*set*) nebo slovníky (*map*) s deterministickým pořadím postupu;
- Každé pole je ohraničené (*dolní hranice* / *horní hranice*). Rovněž zavádíme omezení počtu prvků v kolekcích (containment);
- Data jsou zarovnána na bajty a serializace je přesně definovaná a jednoznačná.

Díky tomuto přísnému protokolu kódování :


- Pořadí polí je vždy stejné, bez ohledu na implementaci nebo použitý programovací jazyk;
- Hesla vypočtená na stejném souboru dat jsou proto reprodukovatelná a identická (striktně deterministické *závazky*);
- Hranice zabraňují nekontrolovanému růstu velikosti dat (např. příliš mnoho polí);
- Tato forma kódování usnadňuje kryptografické ověřování, protože každý účastník přesně ví, jak data serializovat a hashovat.

V praxi se zkompiluje struktura (*Schema*) a výsledný kód (*Interface* a související logika). K definování kontraktu (typy, pole, pravidla) a generování striktního binárního formátu se používá popisný jazyk. Po kompilaci je výsledkem :


- *Rozložení paměti* pro každé pole;
- Sémantické identifikátory (které udávají, zda má změna názvu proměnné vliv na logiku, i když struktura paměti zůstává stejná).

Striktní systém typů také umožňuje přesné sledování změn: jakákoli změna struktury (dokonce i změna názvu pole) je zjistitelná a může vést ke změně celkového otisku.

Nakonec se při každé kompilaci vytvoří otisk prstu, kryptografický identifikátor, který potvrzuje přesnou verzi kódu (data, pravidla, validace). Například identifikátor ve tvaru :

```txt
BEiLYE-am9WhTW1-oK8cpvw4-FEMtzMrf-mKocuGZn-qWK6YF#ginger-parking-nirvana
```

To umožňuje řídit konsensus nebo aktualizace implementace a zároveň zajišťuje podrobnou sledovatelnost verzí používaných v síti.

Aby se zabránilo tomu, že se stav smlouvy RGB stane příliš těžkopádným pro validaci na straně klienta, ukládá pravidlo konsensu maximální velikost `2^16` bajtů (64 Kio) pro jakákoli data zapojená do validačních výpočtů. To platí pro každou proměnnou nebo strukturu: ne více než 65536 bajtů nebo ekvivalent v číslech (32768 16bitových celých čísel atd.). To platí také pro kolekce (seznamy, množiny, mapy), které nesmí překročit `2^16` prvků.

Tento limit zaručuje :


- Řídí maximální velikost dat, se kterými se bude manipulovat při přechodu stavu;
- Kompatibilita s virtuálním počítačem (*AluVM*) používaným ke spuštění validačních skriptů.

#### Paradigma ověřování != vlastnictví

Jednou z hlavních inovací systému RGB je striktní oddělení dvou konceptů:


- Validace**: kontrola, zda přechod stavu respektuje pravidla smlouvy (obchodní logika, historie atd.);
- **Vlastnictví** (vlastnictví nebo kontrola): skutečnost, že vlastníte Bitcoin UTXO, která umožňuje utratit (nebo uzavřít) jednorázovou pečeť, a tím uskutečnit přechod stavu.

Validace** probíhá na úrovni softwarového zásobníku RGB (knihovny, protokol *commitments* atd.). Jeho úkolem je zajistit, aby byla dodržována vnitřní pravidla smlouvy (částky, oprávnění atd.). Pozorovatelé nebo jiní účastníci mohou rovněž ověřovat historii údajů.

Vlastnictví** naproti tomu zcela spoléhá na bezpečnost Bitcoinu. Vlastnit soukromý klíč UTXO znamená kontrolovat možnost spustit nový přechod (uzavření jednorázové pečeti). Takže i když někdo může vidět nebo ověřit data, nemůže změnit stav, pokud dotyčné UTXO nevlastní.

![RGB-Bitcoin](assets/fr/069.webp)

Tento přístup omezuje klasické zranitelnosti, které se vyskytují u složitějších blockchainů (kde je veškerý kód chytrého kontraktu veřejný a může jej kdokoli upravovat, což někdy vede k hackerským útokům). V RGB nemůže útočník jednoduše zasahovat do stavu v řetězci, protože právo jednat se stavem (*vlastnictví*) je chráněno vrstvou Bitcoin.

Toto oddělení navíc umožňuje přirozenou integraci RGB se sítí Lightning. Kanály Lightning lze použít k zapojení a přesunu aktiv RGB, aniž by bylo nutné pokaždé zapojovat *závazky* v řetězci. Na tuto integraci RGB na Lightning se blíže podíváme v dalších kapitolách kurzu.

#### Konsenzuální vývoj v RGB

Kromě sémantického verzování kódu obsahuje RGB systém pro vývoj nebo aktualizaci pravidel konsensu smlouvy v průběhu času. Existují dvě hlavní formy evoluce:


- Rychlý posun vpřed**
- Push-back** (ve francouzštině)

K rychlému posunu vpřed dojde, když se dříve neplatné pravidlo stane platným. Například pokud se smlouva vyvíjí tak, že umožňuje nový typ `AssignmentType` nebo nové pole :


- To nelze srovnávat s klasickým hardforkem blockchainu, protože RGB funguje při ověřování na straně klienta a nemá vliv na celkovou kompatibilitu blockchainu ;
- V praxi se tento typ změny označuje polem `Ffv` (*rychlá předsunutá verze*) v operaci smlouvy;
- Stávající držitelé nejsou poškozeni: jejich status zůstává v platnosti;
- Noví příjemci (nebo noví uživatelé) naopak musí aktualizovat svůj software (peněženku), aby rozpoznali nová pravidla.

Push-back znamená, že dříve platné pravidlo se stává neplatným. Jedná se tedy o "zpřísnění" pravidel, ale ne přesně řečeno o softfork:


- Stávající držitelé mohou být ovlivněni (mohli by se ocitnout v situaci, kdy by jejich aktiva byla v nové verzi zastaralá nebo neplatná);
- Můžeme se domnívat, že vlastně vytváříme nový protokol: kdo přijme nové pravidlo, odchýlí se od starého;
- Vydavatel se může rozhodnout znovu vydat aktiva v tomto novém protokolu, což uživatele donutí udržovat dvě samostatné peněženky (jednu pro starý protokol, druhou pro nový), pokud chtějí spravovat obě verze.

V této kapitole o operacích se smlouvami RGB jsme prozkoumali základní principy, na kterých je tento protokol založen. Jak jste si jistě všimli, vlastní složitost protokolu RGB vyžaduje používání mnoha odborných termínů. V následující kapitole vám proto poskytnu slovníček, který shrne všechny pojmy, jimiž se zabývala tato první teoretická část, s definicemi všech technických termínů týkajících se protokolu RGB. V další části se pak podíváme na praktický pohled na definici a implementaci smluv RGB.

## Slovník RGB

<chapterId>545e16a4-3cca-44a3-9fd5-dbc5868abf97</chapterId>

Pokud se budete potřebovat vrátit k tomuto krátkému slovníčku důležitých technických termínů používaných ve světě RGB (řazených abecedně), bude se vám hodit. Tato kapitola není nezbytná, pokud jste již porozuměli všemu, co jsme probrali v první části.

#### AluVM

Zkratka AluVM znamená "_Algorithmic logic unit Virtual Machine_", virtuální stroj založený na registrech a určený pro ověřování chytrých smluv a distribuované výpočty. Používá se (ale není výhradně vyhrazen) pro validaci kontraktů RGB. Skripty nebo operace obsažené ve smlouvě RGB lze tedy provádět v prostředí AluVM.

Další informace: [oficiální stránky AluVM](https://www.aluvm.org/)

#### Kotva

Kotva představuje sadu dat na straně klienta, která slouží k prokázání zahrnutí jedinečného _závazku_ do transakce. V protokolu RGB se kotva skládá z následujících prvků:


- Identifikátor transakce v bitcoinech (TXID) **svědecké transakce** ;
- **Závazek více protokolů (MPC)** ;
- **Deterministický bitcoinový závazek (DBC)**;
- **Extra Transaction Proof (ETP)**, pokud je použit mechanismus závazku **Tapret** (viz oddíl věnovaný tomuto modelu).

Kotva tedy slouží k vytvoření ověřitelného spojení mezi konkrétní transakcí Bitcoin a soukromými údaji ověřenými protokolem RGB. Zaručuje, že tato data jsou skutečně obsažena v blockchainu, aniž by byl jejich přesný obsah veřejně odhalen.

#### Zadání

V logice RGB je přiřazení ekvivalentem výstupu transakce, který mění, aktualizuje nebo vytváří určité vlastnosti v rámci stavu smlouvy. Přiřazení se skládá ze dvou prvků:


- A **Definice těsnění** (odkaz na konkrétní UTXO) ;
- **Vlastněný stát** (údaje popisující stát spojený s tímto novým vlastníkem).

Přiřazení tedy znamená, že část stavu (například aktivum) je nyní přidělena konkrétnímu držiteli, který je identifikován prostřednictvím jednorázové pečeti spojené s UTXO.

#### Obchodní logika

Obchodní logika sdružuje všechna pravidla a interní operace smlouvy popsané jejím **schématem** (tj. strukturou samotné smlouvy). Určuje, jak se může stav smlouvy vyvíjet a za jakých podmínek.

#### Ověřování na straně klienta

Ověřování na straně klienta označuje proces, při kterém každá strana (klient) ověřuje sadu soukromě vyměňovaných dat v souladu s pravidly protokolu. V případě RGB jsou tato vyměňovaná data seskupena do takzvaných **konsignací**. Na rozdíl od protokolu Bitcoin, který vyžaduje, aby byly všechny transakce zveřejňovány v řetězci, RGB umožňuje, aby byly veřejně uloženy pouze _závazky_ (ukotvené v Bitcoinu), zatímco základní informace o smlouvě (přechody, atesty, důkazy) zůstávají mimo řetězec, sdílené pouze mezi dotčenými uživateli.

#### Závazky

Závazek (v kryptografickém smyslu) je matematický objekt, označený `C`, odvozený deterministicky z operace na strukturovaných datech `m` (zpráva) a náhodné hodnotě `r`. Píšeme :

$$
C = \text{commit}(m, r)
$$

Tento mechanismus zahrnuje dvě hlavní operace:


- Commit**: Na zprávu `m` a náhodné číslo `r` se aplikuje kryptografická funkce, která vytvoří `C` ;
- Ověřit**: pomocí `C`, zprávy `m` a hodnoty `r` ověříme, zda je tento závazek správný. Funkce vrací `Pravda` nebo `Pravda`.

Závazek musí respektovat dvě vlastnosti:


- Vazba**: musí být nemožné nalézt dvě různé zprávy, které produkují stejné `C` :

$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$

Jako například :

$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$


- Skrytí**: znalost `C` nesmí odhalit obsah `m`.

V protokolu RGB je součástí transakce bitcoinu závazek, který má prokázat existenci určité informace v daném čase, aniž by byla informace samotná odhalena.

#### Zásilky

**Poslání** sdružuje údaje vyměňované mezi stranami, které podléhají ověření na straně klienta v RGB. Existují dvě hlavní kategorie zásilek:


- Konsignace smlouvy**: dodává ji *vydavatel* (emitent smlouvy), obsahuje inicializační informace, jako je schéma, geneze, rozhraní a implementace rozhraní.
- Převodní zásilka**: dodá ji platící strana (*platitel*). Obsahuje celou historii stavových přechodů vedoucích ke konečné zásilce (tj. konečnému stavu, který obdržel plátce).

Tyto zásilky nejsou veřejně zaznamenávány v blockchainu; vyměňují se přímo mezi zúčastněnými stranami prostřednictvím komunikačního kanálu, který si zvolí.

#### Smlouva

Smlouva je soubor práv uzavřený digitálně mezi několika účastníky prostřednictvím protokolu RGB. Má aktivní stav a obchodní logiku definovanou schématem, které určuje, které operace jsou oprávněné (převody, rozšíření atd.). Stav smlouvy i pravidla její platnosti jsou vyjádřeny ve Schématu. V každém okamžiku se smlouva vyvíjí pouze v souladu s tím, co je povoleno tímto Schématem a validačními skripty (spuštěnými například v AluVM).

#### Smluvní provoz

Operace smlouvy je aktualizace stavu smlouvy provedená podle pravidel schématu. V RGB existují následující operace:


- Přechod stavu** ;
- Genesis** ;
- Státní prodloužení**.

Každá operace mění stav přidáním nebo nahrazením určitých údajů (globální stav, vlastní stav...).

#### Účastník smlouvy

Účastník smlouvy je subjekt, který se účastní operací souvisejících se smlouvou. V RGB se rozlišuje mezi :


- Emitent smlouvy, který vytváří Genesis (původ smlouvy);
- Smluvní strany, tj. držitelé práv ke stavu smlouvy;
- Veřejné strany, které mohou stavět státní rozšíření, pokud smlouva nabízí veřejnosti přístupné nemovitosti.

#### Smluvní práva

Smluvní práva označují různá práva, která mohou uplatňovat účastníci smlouvy RGB. Rozdělují se do několika kategorií:


- Vlastnická práva** spojená s vlastnictvím konkrétního UTXO (prostřednictvím _definice pečetí_);
- Výkonná práva**, tj. možnost vytvořit jeden nebo více přechodů (State Transitions) v souladu se schématem ;
- Veřejná práva**, kdy schéma povoluje určitá veřejná použití, například vytvoření rozšíření státu prostřednictvím odkupu valence.

#### Smluvní stát

Stav smlouvy odpovídá aktuálnímu stavu smlouvy v daném okamžiku. Může se skládat z veřejných i soukromých údajů, které odrážejí stav smlouvy. RGB rozlišuje mezi :


- **Globální stav**, který zahrnuje veřejné vlastnosti smlouvy (nastavené v Genesis nebo přidané prostřednictvím autorizovaných aktualizací);
- Vlastněné státy**, které patří konkrétním vlastníkům, identifikovaným podle jejich UTXO.

#### Deterministický Bitcoin Commitment - DBC

Deterministický Bitcoin Commitment (DBC) je soubor pravidel používaných k prokazatelné a jednoznačné registraci _commitmentu_ v transakci Bitcoin. V protokolu RGB existují dvě hlavní formy DBC:


- Opret**
- Tapret**

Tyto mechanismy přesně definují, jak je _závazek_ zakódován ve výstupu nebo struktuře transakce Bitcoin, aby bylo zajištěno, že tento závazek je deterministicky sledovatelný a ověřitelný.

#### Směrovaný acyklický graf - DAG

DAG (neboli *Acyklický řízený graf*) je graf bez cyklů, který umožňuje topologické plánování. Blockchainy, stejně jako _střepy_ smluv RGB, lze reprezentovat pomocí DAG.

Další informace: [Directed Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph)

#### Gravírování

Gravírování je nepovinný datový řetězec, který mohou do historie smlouvy zadat následní vlastníci smlouvy. Tato funkce existuje například v rozhraní **RGB21** a umožňuje přidávat do historie smluv pamětní nebo popisné informace.

#### Extra Transaction Proof - ETP

ETP (*Extra Transaction Proof*) je část kotvy, která obsahuje dodatečná data potřebná k ověření **Tapret** *závazku* (v kontextu _taproot_). Obsahuje mimo jiné interní veřejný klíč skriptu taproot (_internal PubKey_) a informace specifické pro _výdaj cesty skriptu_.

#### Genesis

Genesis označuje soubor dat, který se řídí schématem a který tvoří počáteční stav každé smlouvy v RGB. Lze ji přirovnat ke konceptu _Genesis Block_ Bitcoinu nebo ke konceptu transakcí Coinbase, zde však na úrovni _klientské strany_ a tokenů RGB.

#### Globální stát

Globální stav je soubor veřejných vlastností obsažených ve stavu smlouvy. Je definován v Genesis a v závislosti na pravidlech smlouvy může být aktualizován autorizovanými přechody. Na rozdíl od vlastněných stavů nepatří globální stav konkrétnímu subjektu, ale má blíže k veřejnému registru v rámci smlouvy.

#### Rozhraní

Rozhraní je soubor instrukcí, které se používají k dekódování binárních dat sestavených ve schématu nebo ve smluvních operacích a jejich stavů, aby byly čitelné pro uživatele nebo jeho peněženku. Funguje jako interpretační vrstva.

#### Implementace rozhraní

Implementace rozhraní je sada deklarací, které spojují **rozhraní** se **schématem**. Umožňuje sémantický překlad prováděný samotným Rozhraním tak, aby uživatel nebo příslušný software (peněženky) rozuměl surovým datům kontraktu.

#### Faktura

Faktura má podobu adresy URL kódované v [base58](https://en.wikipedia.org/wiki/Binary-to-text_encoding#Base58), která obsahuje údaje nezbytné pro sestavení **Převodu stavu** (plátcem). Jinými slovy, je to faktura umožňující protistraně (*plátci*) vytvořit odpovídající přechod pro převod aktiva nebo aktualizaci stavu smlouvy.

#### Síť Lightning

Lightning Network je decentralizovaná síť platebních kanálů (nebo _státních kanálů_) v Bitcoinu, kterou tvoří 2/2 peněženky s více podpisy. Umožňuje rychlé a nízkonákladové _off-chain_ transakce, přičemž se v případě potřeby spoléhá na arbitráž (nebo uzavření) na 1. vrstvě Bitcoinu.

Další informace o tom, jak Lightning funguje, najdete v tomto dalším kurzu:

https://planb.network/courses/lnp201
#### Multi Protocol Commitment - MPC

Multi Protocol Commitment (MPC) odkazuje na Merkleho stromovou strukturu používanou v RGB, která v rámci jedné bitcoinové transakce zahrnuje několik **přechodových balíčků** z různých smluv. Smyslem je seskupit několik závazků (potenciálně odpovídajících různým smlouvám nebo různým aktivům) do jednoho kotevního bodu s cílem optimalizovat obsazení prostoru bloku.

#### Vlastněný stát

Vlastněný stav je část smluvního stavu, která je uzavřena v přiřazení a spojena s konkrétním držitelem (prostřednictvím jednorázové pečeti ukazující na UTXO). Představuje například digitální aktivum nebo konkrétní smluvní právo přidělené dané osobě.

#### Vlastnictví

Vlastnictví se vztahuje k možnosti kontrolovat a utrácet UTXO, na který se odkazuje definice pečeti. Pokud je vlastněný stát spojen s UTXO, má vlastník tohoto UTXO právo potenciálně převést nebo vyvinout spojený stát podle pravidel smlouvy.

#### Částečně podepsaná transakce Bitcoin - PSBT

PSBT (_Partially Signed Bitcoin Transaction_) je transakce Bitcoin, která ještě není plně podepsaná. Může být sdílena mezi několika subjekty, z nichž každý může přidat nebo ověřit určité prvky (podpisy, skripty...), dokud není transakce považována za připravenou k distribuci v řetězci.

Další informace: [BIP-0174](https://github.com/bitcoin/bips/blob/master/bip-0174.mediawiki)

#### Pedersenův závazek

Pedersenův závazek je typ kryptografického závazku s vlastností **homomorfní** vzhledem k operaci sčítání. To znamená, že je možné ověřit součet dvou závazků, aniž by byly odhaleny jednotlivé hodnoty.

Formálně platí, že pokud :

$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$

pak :

$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$

Tato vlastnost je užitečná například pro utajení množství vyměněných žetonů, přičemž je možné ověřit celkové částky.

Další informace: [Pedersen commitment](https://link.springer.com/chapter/10.1007/3-540-46766-1_9)

#### Vykoupit

V rozšíření stavu se Redeem vztahuje k akci znovuzískání (nebo využití) dříve deklarované **Valence**. Jelikož je valence veřejným právem, umožňuje Redeem oprávněnému účastníkovi nárokovat si konkrétní rozšíření stavu smlouvy.

#### Schéma

Schéma v systému RGB je deklarativní část kódu popisující soubor proměnných, pravidel a obchodní logiky (*Business Logic*), které řídí fungování smlouvy. Schéma definuje stavovou strukturu, typy povolených přechodů a podmínky validace.

#### Definice pečeti

Definice pečeti je část přiřazení, která spojuje _závazek_ s UTXO ve vlastnictví nového držitele. Jinými slovy označuje, kde se podmínka nachází (ve kterém UTXO), a zakládá vlastnictví aktiva nebo práva.

#### Střep

Střípek představuje větev v DAG historie přechodů stavu smlouvy RGB. Jinými slovy, je to souvislá podmnožina celkové historie smlouvy, která odpovídá například posloupnosti přechodů potřebných k prokázání platnosti daného aktiva od _Geneze_.

#### Těsnění na jedno použití

Pečeť na jedno použití je kryptografický slib závazku k dosud neznámé zprávě, která bude v budoucnu odhalena pouze jednou a musí ji znát všichni členové určitého publika. Cílem je zabránit vytvoření více konkurenčních závazků pro tutéž pečeť.

#### Úschovna

Úschovna je soubor dat na straně klienta, který uživatel ukládá pro jednu nebo více smluv RGB za účelem ověření (*Ověření na straně klienta*). Patří sem historie přechodů, zásilky, doklady o platnosti atd. Každý držitel si uchovává pouze ty části historie, které potřebuje (*shards*).

#### Státní prodloužení

Rozšíření stavu je operace smlouvy, která slouží k opětovnému spuštění aktualizací stavu vykoupením dříve deklarovaných **Valencí**. Aby bylo prodloužení stavu účinné, musí být následně uzavřeno přechodem stavu (který aktualizuje konečný stav smlouvy).

#### Přechod stavu

Přechod stavu je operace, která mění stav smlouvy RGB na nový stav. Může měnit data globálního stavu a/nebo vlastního stavu. V praxi je každý přechod ověřen pravidly Schema a ukotven v bitcoinovém blockchainu prostřednictvím _commitmentu_.

#### Taproot

Vztahuje se na formát transakcí Segwit v1 Bitcoinu, který byl představen v [BIP341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki) a [BIP342](https://github.com/bitcoin/bips/blob/master/bip-0342.mediawiki). Taproot zlepšuje důvěrnost a flexibilitu skriptů, zejména tím, že transakce jsou kompaktnější a hůře se od sebe odlišují.

#### Koncová zásilka - koncový bod zásilky

Koncová zásilka (nebo _Consignment Endpoint_) je *převodní zásilka* obsahující konečný stav smlouvy, včetně Přechodu stavu vytvořeného z faktury příjemce (*příjemce*). Jedná se tedy o koncový bod převodu s údaji nezbytnými k prokázání, že došlo k převodu vlastnictví nebo stavu.

#### Přechodový balíček

Svazek přechodů je sada přechodů stavu RGB (patřících ke stejné smlouvě), které jsou všechny zapojeny do stejné ***svědecké transakce*** Bitcoin. Díky tomu je možné spojit několik aktualizací nebo převodů do jedné kotvy v řetězci.

#### UTXO

Bitcoinové UTXO (*Unspent Transaction Output*) je definováno hashem transakce a výstupním indexem (*vout*). Někdy se mu také říká _výstupní bod_. V protokolu RGB umožňuje odkaz na UTXO (prostřednictvím **definice pečetě**) umístění **vlastního stavu**, tj. majetku drženého v blockchainu.

#### Valence

Valence je veřejné právo, které samo o sobě nevyžaduje státní úložiště, ale které lze uplatnit prostřednictvím **Státního rozšíření**. Jedná se tedy o formu možnosti, která je otevřená všem (nebo určitým hráčům) a je deklarována v logice smlouvy za účelem pozdějšího provedení určitého rozšíření.

#### Transakce se svědky

Transakce svědka je transakce Bitcoinu, která uzavírá jednorázovou pečeť kolem zprávy obsahující víceprotokolový závazek (MPC). Tato transakce utratí UTXO nebo jej vytvoří, aby zapečetila závazek spojený s protokolem RGB. Funguje jako on-chain důkaz, že stav byl nastaven v určitém časovém okamžiku.

# Programování na RGB

<partId>148a7436-d079-56d9-be08-aaa4c14c6b3a</partId>

## Implementace smluv RGB

<chapterId>8333ea5f-51c7-5dd5-b1d7-47d491e58e51</chapterId>

![video](https://youtu.be/Uo1UoxiImsI)

V této kapitole se blíže podíváme na to, jak je definována a implementována smlouva RGB. Uvidíme, jaké jsou součásti kontraktu RGB, jaké jsou jejich role a jak jsou konstruovány.

### Složky smlouvy RGB

Dosud jsme již probrali **Genesis**, který představuje počáteční bod smlouvy, a viděli jsme, jak zapadá do logiky *Smluvní operace* a stavu protokolu. Úplná definice kontraktu RGB se však neomezuje pouze na Genesis: zahrnuje tři doplňující složky, které společně tvoří jádro implementace.

První složka se nazývá **Schema**. Jedná se o soubor popisující základní strukturu a obchodní logiku (*business logic*) smlouvy. Specifikuje použité datové typy, validační pravidla, povolené operace (např. počáteční vydání tokenu, převody, zvláštní podmínky atd.) - zkrátka obecný rámec, který určuje, jak smlouva funguje.

Druhou složkou je **Rozhraní**. Zaměřuje se na to, jak budou uživatelé (a následně i software portfolia) s touto smlouvou komunikovat. Popisuje sémantiku, tj. čitelnou reprezentaci různých polí a akcí. Zatímco tedy schéma definuje, jak smlouva technicky funguje, rozhraní definuje, jak tyto funkce prezentovat a vystavit: názvy metod, zobrazení dat atd.

Třetí složkou je **Implementace rozhraní**, která doplňuje předchozí dvě složky tím, že funguje jako jakýsi most mezi schématem a rozhraním. Jinými slovy, spojuje sémantiku vyjádřenou Rozhraním se základními pravidly definovanými ve Schématu. Právě tato implementace bude řídit například převod mezi parametrem zadaným v peněžence a binární strukturou uloženou protokolem nebo kompilaci validačních pravidel ve strojovém jazyce.

Tato modularita je zajímavou vlastností RGB, protože umožňuje různým skupinám vývojářů pracovat na těchto aspektech (*Schema*, *Rozhraní*, *Implementace*) odděleně, pokud dodržují pravidla konsensu protokolu.

Souhrnně lze říci, že každá smlouva se skládá z :


- Genesis**, což je počáteční stav smlouvy (a lze jej přirovnat ke zvláštní transakci definující první vlastnictví aktiva, práva nebo jiného parametrizovatelného údaje);
- Schéma**, které popisuje obchodní logiku smlouvy (datové typy, validační pravidla atd.);
- Rozhraní**, které poskytuje sémantickou vrstvu pro peněženky i lidské uživatele a objasňuje čtení a provádění transakcí;
- Implementace** rozhraní, které překlenuje mezeru mezi obchodní logikou a prezentací, aby bylo zajištěno, že definice smlouvy je v souladu s uživatelským prostředím.

![RGB-Bitcoin](assets/fr/070.webp)

Je důležité si uvědomit, že aby peněženka mohla spravovat aktivum RGB (ať už jde o zastupitelný token nebo právo jakéhokoli druhu), musí mít všechny tyto prvky sestaveny: *Schema*, *Interface*, *Interface Implementation* a *Genesis*. To se předává prostřednictvím ***smluvní zásilky***, tj. datového balíčku obsahujícího vše potřebné k ověření platnosti smlouvy na straně klienta.

Pro objasnění těchto pojmů uvádíme souhrnnou tabulku, která porovnává součásti smlouvy RGB s pojmy známými z objektově orientovaného programování (OOP) nebo z ekosystému Ethereum:

| Komponenta smlouvy RGB | Význam | Ekvivalent OOP | Ekvivalent Ethereum |

| ---------------------------- | --------------------------------------- | -------------------------------------------------- | ---------------------------------- |

| Konstruktor třídy | Konstruktor smlouvy | Počáteční stav smlouvy

| Třída | Obchodní logika smlouvy

| Sémantika smlouvy | Rozhraní (Java) / rys (Rust) / protokol (Swift) | ERC Standard |

| Binární rozhraní aplikace (ABI) | Impl (Rust) / Implements (Java) | Mapování sémantiky a logiky

V levém sloupci jsou uvedeny prvky specifické pro protokol RGB. Prostřední sloupec ukazuje konkrétní funkci jednotlivých prvků. Ve sloupci "OOP ekvivalent" pak najdeme ekvivalentní výraz v objektově orientovaném programování:


- Funkce **Genesis** má podobnou úlohu jako *konstruktor třídy*: zde se inicializuje stav smlouvy;
- **Schema** je popis třídy, tj. definice jejích vlastností, metod a základní logiky;
- Rozhraní** odpovídá *rozhraním* (Java), *truhům* (Rust) nebo *protokolům* (Swift): jedná se o veřejné definice funkcí, událostí, polí... ;
- Implementace rozhraní** odpovídá *Impl* v jazyce Rust nebo *Implements* v jazyce Java, kde určujeme, jak bude kód skutečně provádět metody oznámené v rozhraní.

V kontextu Etherea má Genesis blíže ke *konstruktoru smlouvy*, Schema k definici smlouvy, Interface ke standardu, jako je ERC-20 nebo ERC-721, a Interface Implementation k ABI (*Application Binary Interface*), který specifikuje formát interakce se smlouvou.

Výhoda modularity RGB spočívá také v tom, že různé zainteresované strany mohou napsat například vlastní implementaci rozhraní, pokud respektují logiku *Schema* a sémantiku *Rozhraní*. Emitent by tedy mohl vyvinout nový, uživatelsky přívětivější front-end (Rozhraní), aniž by měnil logiku smlouvy, nebo naopak by bylo možné rozšířit Schéma o další funkce a poskytnout novou verzi upravené Implementace rozhraní, zatímco staré implementace by zůstaly platné pro základní funkce.

Při sestavování nové smlouvy generujeme Genesis (první krok při vydávání nebo distribuci aktiva) a jeho součásti (schéma, rozhraní, implementace rozhraní). Poté je kontrakt plně funkční a může být propagován do peněženek a uživatelům. Tento způsob, kdy je Genesis kombinován s těmito třemi komponentami, zaručuje vysoký stupeň přizpůsobení (každý kontrakt může mít vlastní logiku), decentralizace (každý může přispět k dané komponentě) a bezpečnosti (validace zůstává striktně definována protokolem, aniž by závisela na libovolném kódu v řetězci, jak je tomu často u jiných blockchainů).

Nyní bych se rád blíže podíval na každou z těchto složek: **Schéma**, **Rozhraní** a **Implementace rozhraní**.

### Schéma

V předchozí části jsme viděli, že v ekosystému RGB se smlouva skládá z několika prvků: Genesis, který stanovuje počáteční stav, a několika dalších doplňujících složek. Účelem schématu je deklarativně popsat veškerou obchodní logiku kontraktu, tj. strukturu dat, použité typy, povolené operace a jejich podmínky. Je proto velmi důležitým prvkem při zprovozňování kontraktu na straně klienta, protože každý účastník (například peněženka) musí kontrolovat, zda přechody mezi stavy, které přijímá, odpovídají logice definované ve Schématu.

Schéma lze přirovnat ke "třídě" v objektově orientovaném programování (OOP). Obecně řečeno, slouží jako model definující součásti smlouvy, jako je :


- Různé typy vlastních stavů a přiřazení ;
- Valence, tj. speciální práva, která mohou být spuštěna (*vykoupena*) pro určité operace;
- Pole globálního stavu, která popisují globální, veřejné a sdílené vlastnosti smlouvy;
- Struktura Genesis (úplně první operace, která aktivuje smlouvu) ;
- Povolené formy přechodů mezi stavy a rozšíření stavů a způsob, jakým mohou tyto operace změnit ;
- Metadata přidružená ke každé operaci pro uložení dočasných nebo dodatečných informací;
- Pravidla, která určují, jak se mohou interní data smlouvy vyvíjet (například zda je pole proměnlivé nebo kumulativní);
- Posloupnosti operací, které jsou považovány za platné: například pořadí přechodů, které je třeba dodržet, nebo soubor logických podmínek, které je třeba splnit.

![RGB-Bitcoin](assets/fr/071.webp)

Když *vydavatel* aktiva v systému RGB zveřejní smlouvu, poskytne s ní spojenou genezi a schéma. Uživatelé nebo peněženky, kteří chtějí s aktivem komunikovat, si toto schéma načtou, aby pochopili logiku kontraktu a mohli si později ověřit, že přechody, kterých se budou účastnit, jsou legitimní.

Prvním krokem pro každého, kdo obdrží informace o aktivu RGB (např. převod tokenu), je ověření těchto informací podle schématu. To zahrnuje použití kompilace Schématu k :


- Zkontrolujte, zda jsou Vlastní stavy, Přiřazení a další prvky správně definovány a zda respektují stanovené typy (tzv. *přísný typový systém*);
- Zkontrolujte, zda jsou splněna pravidla přechodu (validační skripty). Tyto skripty lze spouštět prostřednictvím AluVM, který je přítomen na straně klienta a je zodpovědný za ověřování konzistence obchodní logiky (výše převodu, speciální podmínky atd.).

V praxi není schéma spustitelný kód, jak je vidět u blockchainů, které ukládají kód na řetězci (EVM na Ethereu). RGB naopak odděluje obchodní logiku (deklarativní) od spustitelného kódu na blockchainu (který je omezen na kryptografické kotvy). Schéma tedy určuje pravidla, ale aplikace těchto pravidel probíhá mimo blockchain, u každého účastníka, podle principu Client-side Validation.

Před použitím v aplikacích RGB musí být schéma zkompilováno. Výsledkem této kompilace je binární soubor (např. `.rgb`) nebo šifrovaný binární soubor (`.rgba`). Když peněženka tento soubor importuje, pozná :


- Jak vypadají jednotlivé datové typy (celá čísla, struktury, pole...) díky přísnému typovému systému ;
- Jak by měla být strukturována databáze Genesis (pro pochopení inicializace aktiv);
- Různé typy operací (přechody stavu, rozšíření stavu) a způsob, jakým mohou měnit stav ;
- Pravidla skriptování (zavedená ve schématu), která bude engine AluVM používat ke kontrole platnosti operací.

Jak bylo vysvětleno v předchozích kapitolách, *přísný typový systém* nám poskytuje stabilní, deterministický formát kódování: všechny proměnné, ať už vlastní stavy, globální stavy nebo valence, jsou přesně popsány (velikost, dolní a horní hranice, pokud je to nutné, typ se znaménkem nebo bez znaménka atd.). Je také možné definovat vnořené struktury, například pro podporu složitých případů použití.

Volitelně může schéma odkazovat na kořenové `SchemaId`, což usnadňuje opakované použití existující základní struktury (šablony). Tímto způsobem lze rozvíjet smlouvu nebo vytvářet její varianty (např. nový typ tokenu) z již osvědčené šablony. Tato modularita zabraňuje nutnosti znovu vytvářet celé smlouvy a podporuje standardizaci osvědčených postupů.

Dalším důležitým bodem je, že logika vývoje stavu (přenosy, aktualizace atd.) je popsána ve schématu ve formě skriptů, pravidel a podmínek. Pokud si tedy tvůrce smlouvy přeje povolit opětovné vydání nebo zavést mechanismus spalování (zničení tokenů), může v části Schema věnované validaci specifikovat odpovídající skripty pro AluVM.

#### Rozdíl oproti programovatelným blockchainům na řetězci

Na rozdíl od systémů, jako je Ethereum, kde je kód (spustitelný) chytré smlouvy zapsán v samotném blockchainu, RGB ukládá smlouvu (její logiku) mimo řetězec, ve formě zkompilovaného deklarativního dokumentu. To znamená, že :


- V každém uzlu sítě Bitcoin neběží žádný virtuální počítač s Turingovým systémem. Pravidla RGB kontraktu se neprovádějí v blockchainu, ale v každém uživateli, který chce potvrdit stav;
- Údaje o smlouvách neznečišťují blockchain: do transakcí Bitcoinu se vkládají pouze kryptografické důkazy (*závazky*) (prostřednictvím `Tapret` nebo `Opret`);
- Schéma může být aktualizováno nebo odmítnuto (*rychle dopředu*, *přesun zpět* atd.), aniž by to vyžadovalo rozvětvení blockchainu Bitcoinu. Peněženky jednoduše musí importovat nové Schéma a přizpůsobit se změnám konsensu.

#### Použití vydavatelem a uživateli

Když *emitent* vytvoří aktivum (například neinflační zastupitelný token), připraví :


- Schéma popisující pravidla emisí, přenosu atd. ;
- Genesis přizpůsobený tomuto schématu (s celkovým počtem vydaných tokenů, identitou původního vlastníka, případnými zvláštními oprávněními pro opětovné vydání atd.).

Poté zpřístupní sestavené schéma (soubor `.rgb`) uživatelům, takže každý, kdo obdrží přenos tohoto tokenu, může lokálně zkontrolovat konzistenci operace. Bez tohoto Schématu by uživatel nebyl schopen interpretovat stavové údaje nebo zkontrolovat, zda jsou v souladu s pravidly smlouvy.

Když tedy chce nová peněženka podporovat aktivum, musí jednoduše integrovat příslušné schéma. Tento mechanismus umožňuje přidat kompatibilitu s novými typy aktiv RGB, aniž by bylo nutné invazivně měnit softwarovou základnu peněženky: stačí importovat binární schéma a porozumět jeho struktuře.

Schéma definuje obchodní logiku v RGB. Uvádí pravidla vývoje smlouvy, strukturu jejích dat (Vlastní stavy, Globální stav, Valence) a související validační skripty (spustitelné AluVM). Díky tomuto deklarativnímu dokumentu je jasně oddělena definice smlouvy (sestavený soubor) od skutečného provádění pravidel (na straně klienta). Toto oddělení dává RGB velkou flexibilitu a umožňuje širokou škálu případů použití (zastupitelné tokeny, NFT, sofistikovanější kontrakty), přičemž se vyhýbá složitosti a nedostatkům typickým pro programovatelné on-chain blockchainy.

#### Příklad schématu

Podívejme se na konkrétní příklad schématu pro smlouvu RGB. Jedná se o výtah v jazyce Rust ze souboru `nia.rs` (iniciály pro "*Non-Inflationable Assets*"), který definuje model pro zastupitelné tokeny, které nelze znovu vydat nad rámec jejich počáteční dodávky (neinflační aktivum). Tento typ tokenu lze v RGB univerzu považovat za ekvivalent ERC20 na Ethereu, tj. zastupitelné tokeny, které respektují určitá základní pravidla (např. o převodech, inicializaci zásob atd.).

Než se ponoříme do kódu, je vhodné připomenout obecnou strukturu schématu RGB. Je zde řada deklarací rámujících :


- Případné `SchemaId` označující použití jiného základního schématu jako šablony;
- **Globální státy** a **Vlastní státy** (s jejich přísnými typy) ;
- Valence** (pokud existují);
- **Operace** (Geneze, Přechody stavů, Rozšíření stavů), které mohou odkazovat na tyto stavy a valence;
- **Systém přísných typů** používaný k popisu a ověřování dat;
- Ověřovací skripty** (spouštěné prostřednictvím AluVM).

![RGB-Bitcoin](assets/fr/072.webp)

Níže uvedený kód ukazuje kompletní definici schématu Rust. Budeme ji komentovat po částech podle níže uvedených poznámek (1) až (9):

```rust
// ===== PART 1: Function Header and SubSchema =====
fn nia_schema() -> SubSchema {
// definitions of libraries and variables
// ===== PART 2: General Properties (ffv, subset_of, type_system) =====
Schema {
ffv: zero!(),
subset_of: None,
type_system: types.type_system(),
// ===== PART 3: Global States =====
global_types: tiny_bmap! {
GS_NOMINAL => GlobalStateSchema::once(types.get("RGBContract.DivisibleAssetSpec")),
GS_DATA => GlobalStateSchema::once(types.get("RGBContract.ContractData")),
GS_TIMESTAMP => GlobalStateSchema::once(types.get("RGBContract.Timestamp")),
GS_ISSUED_SUPPLY => GlobalStateSchema::once(types.get("RGBContract.Amount")),
},
// ===== PART 4: Owned Types =====
owned_types: tiny_bmap! {
OS_ASSET => StateSchema::Fungible(FungibleType::Unsigned64Bit),
},
// ===== PART 5: Valencies =====
valency_types: none!(),
// ===== PART 6: Genesis: Initial Operations =====
genesis: GenesisSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: tiny_bmap! {
GS_NOMINAL => Occurrences::Once,
GS_DATA => Occurrences::Once,
GS_TIMESTAMP => Occurrences::Once,
GS_ISSUED_SUPPLY => Occurrences::Once,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
},
// ===== PART 7: Extensions =====
extensions: none!(),
// ===== PART 8: Transitions: TS_TRANSFER =====
transitions: tiny_bmap! {
TS_TRANSFER => TransitionSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: none!(),
inputs: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
}
},
// ===== PART 9: Script AluVM and Entry Points =====
script: Script::AluVM(AluScript {
libs: confined_bmap! { alu_id => alu_lib },
entry_points: confined_bmap! {
EntryPoint::ValidateGenesis => LibSite::with(FN_GENESIS_OFFSET, alu_id),
EntryPoint::ValidateTransition(TS_TRANSFER) => LibSite::with(FN_TRANSFER_OFFSET, alu_id),
},
}),
}
}
```


- (1) - Záhlaví funkce a dílčí schéma**

Funkce `nia_schema()` vrací `SubSchema`, což znamená, že toto schéma může částečně dědit z obecnějšího schématu. V ekosystému RGB tato flexibilita umožňuje opakovaně použít určité standardní prvky hlavního schématu a poté definovat pravidla specifická pro danou smlouvu. Zde jsme se rozhodli dědičnost neumožnit, protože `subset_of` bude `None`.


- (2) - Obecné vlastnosti: ffv, subset_of, type_system**

Vlastnost `ffv` odpovídá *rychle dopředné* verzi smlouvy. Hodnota `nula!()` zde znamená, že se nacházíme ve verzi 0 nebo v počáteční verzi tohoto schématu. Pokud si později přejete přidat nové funkce (nový typ operace atd.), můžete tuto verzi inkrementovat, abyste naznačili změnu konsensu.

Příkaz `subset_of: Vlastnost None` potvrzuje nepřítomnost dědičnosti. Pole `type_system` odkazuje na striktní typový systém již definovaný v knihovně `types`. Tento řádek označuje, že všechna data používaná kontraktem používají striktní implementaci serializace poskytovanou danou knihovnou.


- (3) - Globální státy

V bloku `global_types` deklarujeme čtyři prvky. Pomocí klíče, například `GS_NOMINAL` nebo `GS_ISSUED_SUPPLY`, se na ně později odkazujeme:


- `GS_NOMINAL` odkazuje na typ `DivisibleAssetSpec`, který popisuje různá pole vytvořeného tokenu (plné jméno, ticker, přesnost...);
- `GS_DATA` představuje obecná data, například prohlášení o vyloučení odpovědnosti, metadata nebo jiný text;
- `GS_TIMESTAMP` odkazuje na datum vydání;
- `GS_ISSUED_SUPPLY` nastavuje celkovou zásobu, tj. maximální počet tokenů, které lze vytvořit.

Klíčové slovo `once(...)` znamená, že každé z těchto polí se může objevit pouze jednou.


- (4) - Vlastní typy

V poli `vlastní_typy` deklarujeme `OS_ASSET`, které popisuje zaměnitelný stav. Použijeme `StateSchema::Fungible(FungibleType::Unsigned64Bit)`, což znamená, že množství aktiv (tokenů) je uloženo jako 64bitové celé číslo bez znaménka. Každá transakce tedy odešle určité množství jednotek tohoto tokenu, které bude validováno podle této striktně typované číselné struktury.


- (5) - Valence**

Uvádíme `valency_types: none!()`, což znamená, že v tomto schématu nejsou žádné valence, jinými slovy žádná speciální nebo dodatečná práva (jako je reissue, podmíněné vypalování atd.). Pokud by schéma nějaké obsahovalo, byly by deklarovány v této sekci.


- (6) - Genesis: první operace

Zde zadáme část, která deklaruje smluvní operace. Genesis je popsána slovy :


- Absence `metadat` (pole `metadata: Ty::<SemId>::UNIT.id(None)`) ;
- Globální stavy, které musí být přítomny vždy jednou (`Once`);
- Seznam přiřazení, ve kterém se musí objevit `OS_ASSET`. To znamená, že Genesis vyžaduje alespoň jedno přiřazení `OS_ASSET` (počáteční držitel);
- Žádná valence : `valence: žádná!()`.

Tímto způsobem omezíme definici počátečního vydání tokenu: musíme deklarovat vydanou zásobu (`GS_ISSUED_SUPPLY`) a alespoň jednoho držitele (vlastněný stav typu `OS_ASSET`).


- (7) - Rozšíření

Pole `extensions: none!()` označuje, že se v této smlouvě nepředpokládá žádné rozšíření stavu. To znamená, že neexistuje žádná operace pro vykoupení digitálního práva (Valence) nebo pro provedení rozšíření stavu před Přechodem. Vše se provádí prostřednictvím Genesis nebo Přechodů stavu.


- (8) - Přechody: TS_TRANSFER

V poli `transitions` definujeme typ operace `TS_TRANSFER`. Vysvětlujeme, že :


- Nemá žádná metadata;
- Nemění globální stav (který je již definován v Genesis);
- Jako vstup přijímá jeden nebo více `OS_ASSET`. To znamená, že musí utratit existující vlastní stavy;
- Vytvoří (`přidělí`) alespoň jeden nový `OS_ASSET` (jinými slovy, příjemce nebo příjemci obdrží tokeny) ;
- Nevytváří žádnou novou valenci.

To modeluje chování základního převodu, který spotřebovává tokeny na UTXO, poté vytváří nové Vlastní stavy ve prospěch příjemců, a tím zachovává rovnost celkové částky mezi vstupy a výstupy.


- (9) - Skript AluVM a vstupní body** (francouzsky)

Nakonec deklarujeme skript AluVM (`Script::AluVM(AluScript { ... })`). Tento skript obsahuje :


- Jedna nebo více externích knihoven (`libs`), které mají být použity při ověřování;
- Vstupní body ukazující na offsety funkcí v kódu AluVM, které odpovídají validaci Genesis (`ValidateGenesis`) a každého deklarovaného Přechodu (`ValidateTransition(TS_TRANSFER)`).

Tento validační kód je zodpovědný za použití obchodní logiky. Bude například kontrolovat :


- Že během Genesis není překročena hodnota `GS_ISSUED_SUPPLY` ;
- Součet `vstupů` (vynaložených tokenů) se rovná součtu `přidělení` (přijatých tokenů) pro `TS_TRANSFER`.

Pokud tato pravidla nebudou dodržena, bude přechod považován za neplatný.

Tento příklad schématu "*Nenafukovací zastupitelné aktivum*" nám umožňuje lépe pochopit strukturu jednoduchého kontraktu RGB zastupitelných tokenů. Jasně vidíme oddělení popisu dat (globální a vlastní stavy), deklarace operací (geneze, přechody, rozšíření) a implementace validace (skripty AluVM). Díky tomuto modelu se token chová jako klasický fungibilní token, ale zůstává validován na straně klienta a při provádění svého kódu není závislý na infrastruktuře on-chainu. V bitcoinovém blockchainu jsou ukotveny pouze kryptografické závazky.

### Rozhraní

Rozhraní je vrstva určená k tomu, aby byla smlouva čitelná a manipulovatelná jak pro uživatele (čtení člověkem), tak pro portfolia (čtení softwarem). Rozhraní tedy hraje roli srovnatelnou s rozhraním v objektově orientovaném programovacím jazyce (Java, Rust trait atd.), neboť odhaluje a objasňuje funkční strukturu smlouvy, aniž by nutně odhalovalo vnitřní detaily obchodní logiky.

Na rozdíl od schématu, které je čistě deklarativní a zkompilované do binárního souboru, který je obtížné používat v původní podobě, rozhraní poskytuje klíče pro čtení potřebné k :


- Vyjmenujte a popište globální státy a vlastní státy zahrnuté do smlouvy;
- Přístup k názvům a hodnotám jednotlivých polí, aby bylo možné je zobrazit (např. pro token zjistit jeho ticker, maximální částku atd.);
- Interpretovat a konstruovat smluvní operace (Geneze, Přechod stavu nebo Rozšíření stavu) přiřazením dat ke srozumitelným názvům (např. provést převod jasným uvedením "částky", nikoli binárního identifikátoru).

![RGB-Bitcoin](assets/fr/073.webp)

Díky rozhraní můžete například v peněžence napsat kód, který místo manipulace s poli přímo manipuluje se štítky, jako je "počet tokenů", "název aktiva" atd. Správa kontraktu se tak stává intuitivnější. Tímto způsobem se správa smluv stává intuitivnější.

#### Obecný provoz

Tato metoda má mnoho výhod:


- Standardizace:**

Stejný typ smlouvy může být podporován standardním rozhraním, které je sdíleno několika implementacemi peněženek. To usnadňuje kompatibilitu a opakované použití kódu.


- Jasné oddělení schématu a rozhraní:**

V návrhu RGB jsou schéma (obchodní logika) a rozhraní (prezentace a manipulace) dvě nezávislé entity. Vývojáři, kteří píší smluvní logiku, se mohou soustředit na Schema, aniž by se starali o ergonomii nebo reprezentaci dat, zatímco jiný tým (nebo stejný tým, ale na jiné časové ose) může vyvíjet Rozhraní.


- Flexibilní vývoj:**

Rozhraní lze po vydání aktiva upravit nebo doplnit, aniž by bylo nutné měnit samotnou smlouvu. To je zásadní rozdíl oproti některým on-chain smart contract systémům, kde je Rozhraní (často smíšené s prováděcím kódem) zmrazeno v blockchainu.


- Možnost použití více rozhraní

Stejná smlouva by mohla být vystavena prostřednictvím různých rozhraní přizpůsobených různým potřebám: jednoduché rozhraní pro koncového uživatele, jiné, pokročilejší, pro vydavatele, který potřebuje spravovat složité konfigurační operace. Peněženka si pak může vybrat, které Rozhraní bude importovat, v závislosti na svém použití.

![RGB-Bitcoin](assets/fr/074.webp)

V praxi to znamená, že když peněženka načte smlouvu RGB (prostřednictvím souboru `.rgb` nebo `.rgba`), importuje také související rozhraní, které je rovněž zkompilováno. Za běhu může peněženka například :


- Procházet seznam států a číst jejich názvy, aby se v uživatelském rozhraní zobrazoval Ticker, Počáteční částka, Datum emise atd., nikoli nečitelný číselný identifikátor;
- Sestavit operaci (například převod) pomocí explicitních názvů parametrů: místo zápisu `přidělení { OS_ASSET => 1 }` může uživateli nabídnout pole "Částka" ve formuláři a převést tuto informaci do striktně typizovaných polí očekávaných smlouvou.

#### Rozdíl oproti Ethereu a jiným systémům

Na platformě Ethereum je rozhraní (popsané pomocí ABI, *Application Binary Interface*) obecně odvozeno od kódu uloženého v řetězci (smart contract). Úprava konkrétní části rozhraní může být nákladná nebo komplikovaná, aniž by se dotkla samotného kontraktu. RGB je však založeno na zcela off-chain logice, přičemž data jsou ukotvena v *commitments* na Bitcoinu. Tento design umožňuje měnit rozhraní (nebo jeho implementaci), aniž by to mělo dopad na základní bezpečnost kontraktu, protože validace obchodních pravidel zůstává ve schématu a odkazovaném kódu AluVM.

#### Sestavení rozhraní

Stejně jako u schématu je rozhraní definováno ve zdrojovém kódu (často v jazyce Rust) a zkompilováno do souboru `.rgb` nebo `.rgba`. Tento binární soubor obsahuje všechny informace, které peněženka vyžaduje pro :


- Identifikace polí podle názvu ;
- Propojte každé pole (a jeho hodnotu) s přísným systémovým typem definovaným ve smlouvě;
- Znát různé povolené operace a způsob jejich provádění.

Po importu rozhraní může peněženka správně zobrazit smlouvu a navrhnout uživateli interakce.

### Rozhraní standardizovaná sdružením LNP/BP

V ekosystému RGB se rozhraní používá k tomu, aby se datům a operacím smlouvy dal čitelný a manipulovatelný význam. Rozhraní tak doplňuje schéma, které interně popisuje obchodní logiku (striktní typy, validační skripty atd.). V této části se podíváme na standardní Rozhraní vyvinutá sdružením LNP/BP pro běžné typy smluv (zastupitelné tokeny, NFT atd.).

Připomínáme, že každé rozhraní popisuje, jak zobrazit a manipulovat se smlouvou na straně peněženky, jasně pojmenovává pole (například `spec`, `ticker`, `issuedSupply`...) a definuje možné operace (například `Transfer`, `Burn`, `Rename`...). Několik rozhraní již funguje, ale v budoucnu jich bude přibývat.

#### Některá rozhraní připravená k použití

**RGB20** je rozhraní pro zastupitelná aktiva, které lze přirovnat ke standardu ERC20 pro Ethereum. Jde však o krok dál a nabízí rozsáhlejší funkce:


- Například možnost přejmenovat aktivum (změna *tickeru* nebo celého názvu) po jeho vydání nebo upravit jeho přesnost (*rozdělení akcií*);
- Může také popisovat mechanismy pro druhotnou reemisi (omezenou nebo neomezenou) a pro spálení a následné nahrazení, aby byl emitent oprávněn aktiva za určitých podmínek zničit a následně znovu vytvořit;

Rozhraní RGB20 lze například propojit se schématem **Non-Inflatable Asset (NIA)**, které zavádí neinflatabilní počáteční dodávku, nebo s jinými pokročilejšími schématy podle potřeby.

**RGB21** se týká smluv typu NFT nebo obecněji jakéhokoli jedinečného digitálního obsahu, například reprezentace digitálních médií (obrázků, hudby atd.). Kromě popisu vydání a převodu jednotlivého aktiva zahrnuje funkce, jako je např:


- Integrovaná podpora pro přímé vložení souboru (až 16 MB) do smlouvy (pro načtení na straně klienta);
- Možnost vlastníka zadat do historie "*vyrytí*", aby prokázal minulé vlastnictví NFT.

**RGB25** je hybridní standard kombinující zaměnitelné a nezaměnitelné aspekty. Je určen pro částečně zaměnitelná aktiva, jako je tokenizace nemovitostí, kdy chcete rozdělit nemovitost a zároveň zachovat vazbu na jedno kořenové aktivum (jinými slovy, máte zaměnitelné části domu, které jsou propojeny s nezaměnitelným domem). Technicky lze toto rozhraní propojit se schématem **Collectible Fungible Asset* (CFA)**, které zohledňuje pojem rozdělení při sledování původního aktiva.

#### Rozhraní ve vývoji

Další rozhraní jsou plánována pro specializovanější použití, ale zatím nejsou k dispozici:


- RGB22**, věnovaný digitálním identitám, pro správu identifikátorů a profilů na řetězci v ekosystému RGB;
- RGB23**, pro pokročilé časové razítkování, využívající některé myšlenky *Opentimestamps*, ale s funkcemi sledovatelnosti;
- RGB24**, jehož cílem je vytvořit obdobu decentralizovaného systému názvů domén (DNS) podobného systému *Ethereum Name Service* ;
- RGB26**, určený pro správu DAO (*Decentralizovaná autonomní organizace*) ve složitějším formátu (řízení, hlasování atd.);
- RGB30**, velmi podobný RGB20, ale s tím rozdílem, že zohledňuje decentralizované počáteční vydávání a používá státní rozšíření. To by se používalo pro aktiva, jejichž opětovnou emisi spravuje několik subjektů, nebo podléhá jemnějším podmínkám.

V závislosti na datu konzultace tohoto kurzu mohou být tato rozhraní samozřejmě již funkční a přístupná.

#### Příklad rozhraní

Tento úryvek kódu v jazyce Rust zobrazuje rozhraní [RGB20](https://github.com/RGB-WG/rgb-std/blob/master/src/interface/rgb20.rs) (zaměnitelné aktivum). Tento kód je převzat ze souboru `rgb20.rs` ve standardní knihovně RGB. Podívejme se na něj, abychom pochopili strukturu rozhraní a to, jak poskytuje most mezi obchodní logikou (definovanou ve schématu) na jedné straně a funkcemi vystavenými peněženkám a uživatelům na straně druhé.

```rust
// ...
fn rgb20() -> Iface {
let types = StandardTypes::with(rgb20_stl());
Iface {
version: VerNo::V1,
name: tn!("RGB20"),
global_state: tiny_bmap! {
fname!("spec") => GlobalIface::required(types.get("RGBContract.DivisibleAssetSpec")),
fname!("data") => GlobalIface::required(types.get("RGBContract.ContractData")),
fname!("created") => GlobalIface::required(types.get("RGBContract.Timestamp")),
fname!("issuedSupply") => GlobalIface::one_or_many(types.get("RGBContract.Amount")),
fname!("burnedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
fname!("replacedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
},
assignments: tiny_bmap! {
fname!("inflationAllowance") => AssignIface::public(OwnedIface::Amount, Req::NoneOrMore),
fname!("updateRight") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnEpoch") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnRight") => AssignIface::public(OwnedIface::Rights, Req::NoneOrMore),
fname!("assetOwner") => AssignIface::private(OwnedIface::Amount, Req::NoneOrMore),
},
valencies: none!(),
genesis: GenesisIface {
metadata: Some(types.get("RGBContract.IssueMeta")),
global: tiny_bmap! {
fname!("spec") => ArgSpec::required(),
fname!("data") => ArgSpec::required(),
fname!("created") => ArgSpec::required(),
fname!("issuedSupply") => ArgSpec::required(),
},
assignments: tiny_bmap! {
fname!("assetOwner") => ArgSpec::many(),
fname!("inflationAllowance") => ArgSpec::many(),
fname!("updateRight") => ArgSpec::optional(),
fname!("burnEpoch") => ArgSpec::optional(),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_RESERVES
},
},
transitions: tiny_bmap! {
tn!("Transfer") => TransitionIface {
optional: false,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("previous") => ArgSpec::from_non_empty("assetOwner"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_non_empty("assetOwner"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Issue") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.IssueMeta")),
globals: tiny_bmap! {
fname!("issuedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_non_empty("inflationAllowance"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_many("inflationAllowance"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
ISSUE_EXCEEDS_ALLOWANCE,
INSUFFICIENT_RESERVES
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("OpenEpoch") => TransitionIface {
optional: true,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnEpoch"),
},
assignments: tiny_bmap! {
fname!("next") => ArgSpec::from_optional("burnEpoch"),
fname!("burnRight") => ArgSpec::required()
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("burnRight")),
},
tn!("Burn") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("burnedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: None,
},
tn!("Replace") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("replacedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS,
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Rename") => TransitionIface {
optional: true,
metadata: None,
globals: tiny_bmap! {
fname!("new") => ArgSpec::from_required("spec"),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("updateRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("updateRight"),
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("future")),
},
},
extensions: none!(),
error_type: types.get("RGB20.Error"),
default_operation: Some(tn!("Transfer")),
type_system: types.type_system(),
}
}
```

V tomto rozhraní si všimneme podobností se strukturou schématu: najdeme zde deklaraci globálního stavu, vlastních stavů, smluvních operací (Genesis a Transitions) a také zpracování chyb. Rozhraní se však zaměřuje na prezentaci a manipulaci s těmito prvky pro peněženku nebo jinou aplikaci.

Rozdíl oproti schématu spočívá v povaze typů. Schema používá striktní typy (například `FungibleType::Unsigned64Bit`) a více technických identifikátorů. Rozhraní používá názvy polí, makra (`fname!()`, `tn!()`) a odkazy na třídy argumentů (`ArgSpec`, `OwnedIface::Rights`...). Cílem je zde usnadnit funkční pochopení a organizaci prvků pro peněženku.

Rozhraní může navíc do základního schématu zavést další funkce (např. správu práva `burnEpoch`), pokud zůstane v souladu s konečnou ověřenou logikou na straně klienta. Část "skriptu" AluVM ve Schématu zajistí kryptografickou platnost, zatímco Rozhraní popisuje, jak uživatel (nebo peněženka) s těmito stavy a přechody pracuje.

#### Globální stav a přiřazení

V sekci `global_state` najdeme pole jako `spec` (popis aktiva), `data`, `created`, `issuedSupply`, `burnedSupply`, `replacedSupply`. Jedná se o pole, která může peněženka číst a prezentovat. Například:


- `spec` zobrazí konfiguraci tokenu;
- `issuedSupply` nebo `burnedSupply` nám udávají celkový počet vydaných nebo spálených žetonů atd.

V části `Přidělení` definujeme různé role nebo práva. Například:


- `assetOwner` odpovídá držení tokenů (je to zaměnitelný *Vlastněný stav*) ;
- `burnRight` odpovídá schopnosti vypalovat žetony ;
- updateRight` odpovídá právu přejmenovat aktivum.

Klíčové slovo `public` nebo `private` (např. `AssignIface::public(...)`) označuje, zda jsou tyto stavy viditelné (`public`) nebo důvěrné (`private`). Pokud jde o `Req::NoneOrMore`, `Req::Optional`, označují očekávaný výskyt.

#### Geneze a přechody

Část `genesis` popisuje způsob inicializace aktiva:


- Pole `spec`, `data`, `created`, `issuedSupply` jsou povinná (`ArgSpec::required()`) ;
- Přiřazení jako `assetOwner` mohou být přítomna ve více kopiích (`ArgSpec::many()`), což umožňuje distribuovat tokeny více počátečním držitelům;
- Pole jako `inflationAllowance` nebo `burnEpoch` mohou (ale nemusí) být zahrnuta v Genesis.

Rozhraní pak pro každý přechod (`Přenos`, `Vydání`, `Vypálení`...) definuje, která pole operace očekává jako vstup, která pole operace vytvoří jako výstup a jaké chyby se mohou vyskytnout. Například:

**Přechod :**


- Vstupy : `previous` → musí být `assetOwner` ;
- Přiřazení : `příjemce` → bude novým `vlastníkem majetku` ;
- Chyba: `NON_EQUAL_AMOUNTS` (peněženka tak bude schopna zpracovat případy, kdy vstupní součet neodpovídá výstupnímu součtu).

**Přechodné `problémy` :**


- Nepovinné (`optional: true`), protože další emise nemusí být nutně aktivovány;
- Vstupy: `used` → an `inflationAllowance`, tj. povolení přidávat další tokeny ;
- Zadání: (nově obdržené žetony) a `budoucí` (zbývající `inflační příspěvek`);
- Možné chyby: příklady chyb: `SUPPLY_MISMATCH`, `ISSUE_EXCEEDS_ALLOWANCE` atd.

**Přechod na spalování :**


- Vstupy : `použitý` → a `pálitPravý` ;
- Globals : `burnedSupply` required ;
- Zadání: `future` → možné pokračování `burnRight`, pokud jsme nespálili vše ;
- Chyby: cHYBY: `SUPPLY_MISMATCH`, `INVALID_PROOF`, `INSUFFICIENT_COVERAGE`.

Každá operace je proto popsána způsobem, který je čitelný pro peněženku. Díky tomu je možné zobrazit grafické rozhraní, ve kterém to uživatel přehledně vidí: "Máte právo vypálit. Chcete spálit určité množství? Kód ví, že je třeba vyplnit pole `vypálenoZásoba` a zkontrolovat, zda je platný údaj `oprávnění k vypálení`.

Závěrem je důležité mít na paměti, že rozhraní, ať je jakkoli úplné, samo o sobě nedefinuje vnitřní logiku smlouvy. Jádro práce odvádí **Schema**, které zahrnuje striktní typy, strukturu Genesis, přechody atd. Rozhraní pouze vystavuje tyto prvky intuitivnějším a pojmenovaným způsobem pro použití v aplikaci.

Díky modularitě RGB lze rozhraní upgradovat (například přidáním přechodu `Rename`, opravou zobrazení pole atd.), aniž by bylo nutné přepisovat celou smlouvu. Uživatelé tohoto Rozhraní pak mohou tato vylepšení využívat okamžitě, jakmile aktualizují soubor `.rgb` nebo `.rgba`.

Jakmile však rozhraní deklarujete, musíte jej propojit s odpovídajícím schématem. To se provádí prostřednictvím implementace rozhraní***, která určuje, jak mapovat každé pojmenované pole (například `fname!("assetOwner")`) na striktní ID (například `OS_ASSET`) definované ve schématu. Tím je například zajištěno, že když peněženka manipuluje s polem `burnRight`, jedná se o stav, který ve Schématu popisuje schopnost vypalovat tokeny.

### Implementace rozhraní

V architektuře RGB jsme viděli, že každá komponenta (schéma, rozhraní atd.) může být vyvíjena a kompilována nezávisle. Stále však existuje jeden nepostradatelný prvek, který tyto různé stavební bloky spojuje dohromady: ***Implementace rozhraní***. Právě ta explicitně mapuje identifikátory nebo pole definované ve Schématu (na straně obchodní logiky) na názvy deklarované v Rozhraní (na straně prezentace a interakce s uživatelem). Když tedy peněženka načte smlouvu, může přesně pochopit, které pole odpovídá čemu a jak operace pojmenovaná v Rozhraní souvisí s logikou Schématu.

Důležité je, že implementace rozhraní nemusí nutně odhalovat všechny funkce schématu ani všechna pole rozhraní: může se omezit na určitou podmnožinu. V praxi to umožňuje omezit nebo filtrovat určité aspekty Schématu. Například můžete mít Schéma se čtyřmi typy operací, ale Rozhraní Implementace mapuje v daném kontextu pouze dva z nich. A naopak, pokud Rozhraní navrhuje další koncové body, můžeme se rozhodnout je zde neimplementovat.

Zde je klasický příklad implementace rozhraní, kdy přiřazujeme schéma *Non-Inflatable Asset* (NIA) k rozhraní RGB20:

```rust
fn nia_rgb20() -> IfaceImpl {
let schema = nia_schema();
let iface = Rgb20::iface();
IfaceImpl {
version: VerNo::V1,
schema_id: schema.schema_id(),
iface_id: iface.iface_id(),
script: none!(),
global_state: tiny_bset! {
NamedField::with(GS_NOMINAL, fname!("spec")),
NamedField::with(GS_DATA, fname!("data")),
NamedField::with(GS_TIMESTAMP, fname!("created")),
NamedField::with(GS_ISSUED_SUPPLY, fname!("issuedSupply")),
},
assignments: tiny_bset! {
NamedField::with(OS_ASSET, fname!("assetOwner")),
},
valencies: none!(),
transitions: tiny_bset! {
NamedType::with(TS_TRANSFER, tn!("Transfer")),
},
extensions: none!(),
}
}
```

V tomto implementačním rozhraní :


- Na schéma se explicitně odkazujeme prostřednictvím `nia_schema()` a na rozhraní prostřednictvím `Rgb20::iface()`. Volání `schema.schema_id()` a `iface.iface_id()` slouží k ukotvení implementace rozhraní na straně kompilace (to spojuje kryptografické identifikátory těchto dvou komponent);
- Mezi prvky schématu a prvky rozhraní je vytvořeno mapování. Například pole `GS_NOMINAL` ve schématu je propojeno s řetězcem `"spec"` na straně rozhraní (`NamedField::with(GS_NOMINAL, fname!("spec"))`). Stejně postupujeme i u operací, jako je `TS_TRANSFER`, které na straně Rozhraní propojíme s `"Transfer"`... ;
- Vidíme, že zde nejsou žádné valence (`valencies: none!()`) ani rozšíření (`extensions: none!()`), což odráží skutečnost, že tato smlouva NIA tyto funkce nepoužívá.

Výsledkem kompilace je samostatný soubor `.rgb` nebo `.rgba`, který se kromě schématu a rozhraní importuje do peněženky. Software tedy ví, jak konkrétně propojit tento kontrakt NIA (jehož logika je popsána jeho Schématem) s Rozhraním "RGB20" (které poskytuje lidská jména a režim interakce pro zaměnitelné tokeny), přičemž použije tuto Implementaci rozhraní jako bránu mezi nimi.

#### Proč oddělená implementace rozhraní?

Oddělení zvyšuje flexibilitu. Jedno schéma může mít několik různých implementací rozhraní, z nichž každá mapuje jinou sadu funkcí. Navíc se samotná implementace rozhraní může vyvíjet nebo být přepsána, aniž by bylo nutné měnit schéma nebo rozhraní. Tím je zachován princip modularity RGB: každá komponenta (Schéma, Rozhraní, Implementace rozhraní) může být verzována a aktualizována nezávisle, pokud jsou dodržena pravidla kompatibility stanovená protokolem (stejné identifikátory, konzistence typů atd.).

Při konkrétním použití musí peněženka při načítání smlouvy :


- Načtení sestaveného **Schema** (pro zjištění struktury obchodní logiky) ;
- Načtení zkompilovaného **rozhraní** (pro pochopení názvů a operací na straně uživatele) ;
- Načtení zkompilované **implementace rozhraní** (propojení logiky schématu s názvy rozhraní, operace po operacích, pole po polích).

Tato modulární architektura umožňuje použití scénářů, jako je :


- Omezit některé operace pro určité uživatele: nabídnout částečné rozhraní implementace, které umožňuje pouze základní přenosy, ale nenabízí například funkce vypalování nebo aktualizace;
- Prezentace změn: navrhněte implementaci rozhraní, která přejmenuje pole v rozhraní nebo je zmapuje jinak, aniž by se změnil základ smlouvy;
- Podpora více schémat: peněženka může načíst více implementací rozhraní pro stejný typ rozhraní, aby bylo možné zpracovávat různá schémata (různé logiky tokenů), pokud je jejich struktura kompatibilní.

V příští kapitole se podíváme na to, jak funguje převod smlouvy a jak se generují faktury RGB.

## Převody smluv

<chapterId>f043a307-d420-5752-b0d7-ebfd845802c0</chapterId>

![video](https://youtu.be/sVoKIi-1XbY)

V této kapitole budeme analyzovat proces převodu smlouvy v ekosystému RGB. Pro ilustraci se podíváme na Alici a Boba, naše obvyklé protagonisty, kteří si přejí vyměnit aktivum RGB. Ukážeme si také několik výňatků z příkazů nástroje `rgb` pro příkazový řádek, abychom viděli, jak funguje v praxi.

### Porozumění přenosu smlouvy RGB

Uveďme příklad přenosu mezi Alicí a Bobem. V tomto příkladu předpokládáme, že Bob právě začíná používat RGB, zatímco Alice již má ve své peněžence aktiva RGB. Uvidíme, jak Bob nastaví své prostředí, importuje příslušný kontrakt, poté požádá Alici o převod a nakonec Alice provede skutečnou transakci v blockchainu Bitcoinu.

#### 1) Instalace peněženky RGB

Bob si musí nejprve nainstalovat peněženku RGB, tj. software kompatibilní s protokolem. Ta na začátku neobsahuje žádné smlouvy. Bob bude také potřebovat :


- Bitcoinová peněženka pro správu UTXO;
- Připojení k uzlu Bitcoin (nebo k serveru Electrum), abyste mohli identifikovat své UTXO a šířit své transakce v síti.

Připomínáme, že **Vlastní státy** v RGB se vztahují k bitcoinovým UTXO. Proto musíme být vždy schopni spravovat a utrácet UTXO v bitcoinové transakci, která obsahuje kryptografické závazky (`Tapret` nebo `Opret`) směřující k datům RGB.

#### 2) Získávání informací o zakázce

Bob pak musí načíst údaje o smlouvě, které ho zajímají. Tato data se mohou šířit jakýmkoli kanálem: přes webové stránky, e-mail, aplikaci pro zasílání zpráv... V praxi se seskupují do ***konsignace***, tj. malého balíčku dat obsahujícího :


- **Geneze**, která definuje počáteční stav smlouvy;
- **Schema**, které popisuje obchodní logiku (striktní typy, validační skripty atd.);
- **Rozhraní**, které definuje prezentační vrstvu (názvy polí, dostupné operace);
- Implementace rozhraní**, která konkrétně propojuje schéma s rozhraním.

![RGB-Bitcoin](assets/fr/075.webp)

Celková velikost se často pohybuje v řádu několika kilobajtů, protože každá komponenta obvykle váží méně než 200 bajtů. Tuto zásilku může být možné vysílat také ve formátu Base58, prostřednictvím kanálů odolných vůči cenzuře (jako je například Nostr nebo prostřednictvím sítě Lightning) nebo jako kód QR.

#### 3) Import a validace smlouvy

Jakmile Bob zásilku obdrží, importuje ji do své peněženky RGB. Ta pak :


- Zkontrolujte, zda jsou Genesis a Schema platné;
- Rozhraní pro načítání a implementace rozhraní ;
- Aktualizujte datovou zásobu na straně klienta.

Bob nyní vidí majetek ve své peněžence (i když ho ještě nevlastní) a ví, jaká pole jsou k dispozici, jaké operace jsou možné... Poté musí kontaktovat osobu, která aktivum, jež má být převedeno, skutečně vlastní. V našem příkladu je to Alice.

Proces zjišťování, kdo je držitelem určitého aktiva RGB, je podobný jako hledání plátce bitcoinu. Podrobnosti tohoto spojení závisí na použití (tržiště, soukromé chatovací kanály, fakturace, prodej zboží a služeb, mzda...).

#### 4) Vystavení faktury

Aby mohl Bob zahájit převod aktiva RGB, musí nejprve vystavit fakturu. Tato faktura slouží k :


- Řekněte Alici typ operace, která se má provést (například `Přenos` z rozhraní RGB20);
- Poskytněte Alici Bobovu *definici pečetě* (tj. UTXO, kde si přeje získat aktivum);
- Uveďte požadované množství účinné látky (např. 100 jednotek).

Bob používá nástroj `rgb` na příkazovém řádku. Předpokládejme, že chce 100 jednotek tokenu, jehož `ContractId` je známé, chce spoléhat na `Tapret` a zadá jeho UTXO (`456e3..dfe1:0`) :

```bash
bob$ rgb invoice RGB20 100 <ContractId> tapret1st:456e3..dfe1:0
```

Na strukturu faktur RGB se blíže podíváme na konci této kapitoly.

#### 5) Předávání faktur

Vygenerovaná faktura (např. jako adresa URL: `rgb:2WBcas9.../RGB20/100+utxob:...`) obsahuje všechny informace, které Alice potřebuje k přípravě převodu. Stejně jako u zásilky ji lze kompaktně zakódovat (Base58 nebo jiný formát) a odeslat prostřednictvím aplikace pro zasílání zpráv, e-mailu, Nostr....

![RGB-Bitcoin](assets/fr/076.webp)

#### 6) Příprava transakcí na straně Alice

Alice obdrží Bobovu fakturu. Ve své peněžence RGB má schránku obsahující aktivum, které má být převedeno. Aby mohla utratit UTXO obsahující aktivum, musí nejprve vygenerovat PSBT (*Partially Signed Bitcoin Transaction*), tj. neúplnou bitcoinovou transakci, pomocí UTXO, které má:

```bash
alice$ wallet construct tx.psbt
```

Tato základní transakce (prozatím nepodepsaná) bude použita k ukotvení kryptografického závazku spojeného s převodem na Boba. Alicino UTXO tak bude utraceno a na výstup umístíme závazek `Tapret` nebo `Opret` pro Boba.

#### 7) Generování převodní zásilky

Dále Alice vytvoří ***terminální zásilku*** (někdy nazývanou "přenosová zásilka") pomocí příkazu :

```bash
alice$ rgb transfer tx.psbt <invoice> consignment.rgb
```

Tento nový soubor `consignment.rgb` obsahuje :


- Úplná historie přechodů státu potřebná k ověření majetku až do současnosti (od Genesis);
- Nový přechod stavu, který převede aktiva z Alice na Boba podle faktury, kterou Bob vystavil;
- Neúplná transakce Bitcoin (*transakce svědectví*) (`tx.psbt`), která utrácí Alicinu jednorázovou pečeť upravenou tak, aby obsahovala kryptografický závazek vůči Bobovi.

V této fázi transakce ještě není vysílána v síti Bitcoin. Zásilka je větší než základní zásilka, protože obsahuje celou historii (*důkazní řetězec*), která prokazuje legitimitu aktiva.

#### 8) Bob zásilku zkontroluje a přijme

Alice předá tuto **konečnou zásilku** Bobovi. Bob poté :


- Zkontrolujte platnost přechodu stavu (ujistěte se, že historie je konzistentní, že jsou dodržena pravidla smlouvy atd.);
- Přidejte ji do místní zásoby;
- Případně vygenerovat na zásilce podpis (`sig:...`), který prokáže, že byla zkontrolována a schválena (někdy se nazývá "*výplatní list*").

```bash
bob$ rgb accept consignment.rgb
sig:DbwzvSu4BZU81jEpE9FVZ3xjcyuTKWWy2gmdnaxtACrS
```

![RGB-Bitcoin](assets/fr/077.webp)

#### 9) Možnost: Bob pošle Alici zpět potvrzení (*výplatní lístek*)

Pokud si to Bob přeje, může tento podpis poslat zpět Alici. To znamená, že:


- Že uznává přechod jako platný;
- Že souhlasí s vysíláním transakce Bitcoin.

Není to povinné, ale Alici to může poskytnout jistotu, že nedojde k následným sporům ohledně převodu.

#### 10) Alice transakci podepíše a zveřejní

Alice pak může :


- Kontrola Bobova podpisu (`rgb check <sig>`) ;
- Podepište *svědeckou transakci*, která je stále PSBT (`podpis peněženky`);
- Zveřejnění svědecké transakce v síti Bitcoin (`-publish`).

```bash
alice$ rgb check <sig>
alice$ wallet sign —publish tx.psbt
```

![RGB-Bitcoin](assets/fr/078.webp)

Potvrzením této transakce se převod uzavírá. Bob se stává novým vlastníkem aktiva: nyní má vlastněný stav ukazující na UTXO, které ovládá, což dokazuje přítomnost závazku v transakci.

Zde je shrnut celý proces přenosu:

![RGB-Bitcoin](assets/fr/079.webp)

### Výhody přenosů RGB


- Důvěrnost** :

Přístup ke všem datům o přechodech stavů mají pouze Alice a Bob. Tyto informace si vyměňují mimo blockchain prostřednictvím zásilek. Kryptografické závazky v transakci Bitcoin neprozrazují typ aktiva ani jeho výši, což zaručuje mnohem větší důvěrnost než jiné systémy tokenů v řetězci.


- Ověřování na straně zákazníka** :

Bob může zkontrolovat konzistenci převodu porovnáním *odeslání* s *kotvami* v blockchainu Bitcoinu. Nepotřebuje ověření třetí stranou. Alice nemusí zveřejňovat celou historii v blockchainu, což snižuje zatížení základního protokolu a zvyšuje důvěrnost.


- Zjednodušená atomicita** :

Složité výměny (například atomické swapy mezi BTC a aktivem RGB) lze provést v rámci jediné transakce, takže není třeba používat skripty HTLC nebo PTLC. Pokud se dohoda nevysílá, může každý své UTXO znovu použít jiným způsobem.

### Souhrnný diagram přenosu

Než se na faktury podíváme podrobněji, uvádíme souhrnný diagram celkového toku převodu RGB:


- Bob nainstaluje peněženku RGB a získá počáteční smluvní zásilku;
- Bob vystaví fakturu, na které uvede UTXO, kde má majetek obdržet;
- Alice obdrží fakturu, sestaví PSBT a vygeneruje koncovou zásilku;
- Bob ji přijme, zkontroluje, přidá údaje do své zásoby a případně podepíše (*výplatní páska*);
- Alice zveřejní transakci v síti Bitcoin;
- Potvrzením transakce se převod stává oficiálním.

![RGB-Bitcoin](assets/fr/080.webp)

Tento převod ilustruje veškerou sílu a flexibilitu protokolu RGB: soukromá výměna, ověřená na straně klienta, minimálně a diskrétně ukotvená v blockchainu Bitcoinu a zachovávající nejlepší zabezpečení protokolu (žádné riziko dvojího utracení). Díky tomu je RGB slibným ekosystémem pro převody hodnot, které jsou důvěrnější a škálovatelnější než programovatelné blockchainy na řetězci.

### Faktury RGB

V této části podrobně vysvětlíme, jak **faktury** fungují v ekosystému RGB a jak umožňují provádět operace (zejména převody) se smlouvou. Nejprve se podíváme na používané identifikátory, pak na to, jak jsou kódovány, a nakonec na strukturu faktury vyjádřené jako adresa URL (formát, který je dostatečně praktický pro použití v peněženkách).

#### Identifikátory a kódování

Pro každý z následujících prvků je definován jedinečný identifikátor:


- Smlouva RGB;
- Jeho schéma (obchodní logika) ;
- Jeho rozhraní a implementace rozhraní ;
- Jeho aktiva (tokeny, NFT atd.),

Tato jedinečnost je velmi důležitá, protože každá součást systému musí být odlišitelná. Například smlouva X nesmí být zaměnitelná s jinou smlouvou Y a dvě různá rozhraní (například RGB20 vs. RGB21) musí mít odlišné identifikátory.

Aby byly tyto identifikátory efektivní (malá velikost) a čitelné, používáme :


- Kódování Base58, které se vyhýbá používání matoucích znaků (např. `0` a písmeno `O`) a poskytuje relativně krátké řetězce;
- Předpona označující povahu identifikátoru, obvykle ve tvaru `rgb:` nebo podobného URN.

Například `ContractId` by mohlo být reprezentováno něčím jako :

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

Předpona `rgb:` potvrzuje, že se jedná o identifikátor RGB, nikoli o odkaz HTTP nebo jiný protokol. Díky této předponě jsou peněženky schopny tento řetězec správně interpretovat.

#### Segmentace identifikátorů

Identifikátory RGB jsou často poměrně dlouhé, protože základní (kryptografické) zabezpečení může vyžadovat pole o velikosti 256 bitů nebo více. Abychom usnadnili čtení a ověřování, rozdělíme tyto řetězce do několika bloků oddělených pomlčkou (`-`). Místo dlouhého nepřerušovaného řetězce znaků jej tedy rozdělíme do kratších bloků. Tento postup je běžný u čísel kreditních karet nebo telefonních čísel a pro snadnější ověření se uplatňuje i zde. Uživateli nebo partnerovi tak můžeme například sdělit: "*Prosím, zkontrolujte, zda je třetí blok `9GEgnyMj7`*", místo aby se porovnával celý najednou. Poslední blok se často používá jako **kontrolní součet**, aby byl k dispozici systém detekce chyb nebo překlepů.

Příkladem může být `ContractId` v kódování base58 a segmentaci :

```txt
2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

Každá z pomlček rozděluje řetězec na části. To nemá vliv na sémantiku kódu, pouze na jeho prezentaci.

#### Používání adres URL pro faktury

Faktura RGB je prezentována jako adresa URL. To znamená, že na ni lze kliknout nebo ji naskenovat (jako QR kód) a peněženka ji může přímo interpretovat a provést transakci. Tato jednoduchost interakce se liší od některých jiných systémů, kde je třeba kopírovat a vkládat různé údaje do různých polí v softwaru.

Faktura za zaměnitelný token (např. token RGB20) může vypadat takto:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Proveďme analýzu této adresy URL:


- `rgb:`** (prefix): označuje odkaz vyvolávající protokol RGB (obdoba `http:` nebo `bitcoin:` v jiných kontextech);
- `2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX`**: představuje `ContractId` tokenu, se kterým chcete manipulovat;
- `/RGB20/100`**: označuje, že je použito rozhraní `RGB20` a že je požadováno 100 jednotek aktiva. Syntaxe je: `/Interface/amount` ;
- `+utxob:`**: určuje, že jsou přidány informace o příjemci UTXO (přesněji definice jednorázové pečeti);
- `egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb`**: toto je *zaslepený* UTXO (nebo definice pečeti). Jinými slovy, Bob zamaskoval své přesné UTXO, takže odesílatel (Alice) neví, jaká je jeho přesná adresa. Ví pouze, že existuje platná pečeť odkazující na UTXO ovládané Bobem.

Skutečnost, že se vše vejde do jediné adresy URL, uživateli usnadňuje život: stačí kliknout nebo naskenovat peněženku a operace je připravena k provedení.

Lze si představit systémy, kde se místo `ContractId` používá jednoduchý ticker (např. `USDT`). To by však vyvolalo velké problémy s důvěryhodností a bezpečností: ticker není jedinečný odkaz (několik smluv by mohlo tvrdit, že se jmenují `USDT`). V případě RGB chceme jedinečný, jednoznačný kryptografický identifikátor. Proto byl přijat 256bitový řetězec, zakódovaný v base58 a segmentovaný. Uživatel ví, že manipuluje právě s kontraktem, jehož ID je `2WBcas9-yjz...`, a ne s žádným jiným.

#### Další parametry adresy URL

Do adresy URL můžete také přidat další parametry stejným způsobem jako u protokolu HTTP, například :

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb?sig=6kzbKKffP6xftkxn9UP8gWqiC41W16wYKE5CYaVhmEve
```


- `?sig=...`: představuje například podpis spojený s fakturou, který mohou některé peněženky ověřit;
- Pokud peněženka tento podpis nespravuje, jednoduše tento parametr ignoruje.

Vezměme si případ NFT přes rozhraní RGB21. Mohli bychom mít například :

```txt
rgb:7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK/RGB21/DbwzvSu-4BZU81jEp-E9FVZ3xj-cyuTKWWy-2gmdnaxt-ACrS+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Zde vidíme :


- `rgb:`**: Předpona URL ;
- `7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK`**: ID smlouvy (NFT) ;
- rGB21**: rozhraní pro nehmotný majetek (NFT) ;
- `DbwzvSu-4BZU81jEp-...`**: explicitní odkaz na jedinečnou část NFT, například hash datového blobu (média, metadata...) ;
- `+utxob:egXsFnw-...`**: definice pečeti.

Myšlenka je stejná: přenést jedinečný odkaz, který peněženka dokáže interpretovat a který jasně identifikuje jedinečné aktivum, jež má být převedeno.

#### Další operace prostřednictvím adresy URL

Adresy URL RGB se nepoužívají pouze k žádosti o přenos. Mohou také kódovat pokročilejší operace, například vydávání nových tokenů (*issuance*). Například:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/issue/100000+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Zde nalezneme :


- `rgb:` : protokol ;
- `2WBcas9-...`: ID smlouvy ;
- `/RGB20/issue/100000`: označuje, že chcete vyvolat přechod "*Issue*" a vytvořit dalších 100 000 tokenů;
- `+utxob:`: definice pečeti.

Na peněžence může být například napsáno: "Byl jsem požádán, abych provedl operaci `vydání` z rozhraní `RGB20`, na takovou a takovou smlouvu, za 100 000 jednotek, ve prospěch takové a takové jednorázové pečeti.*"

Nyní, když jsme se seznámili s hlavními prvky programování RGB, vás v další kapitole seznámím s tím, jak sestavit smlouvu RGB.

## Příprava inteligentních smluv

<chapterId>0e0a645c-0049-588d-8965-b8c536590cc9</chapterId>

![video](https://youtu.be/GRwS-NvWF3I)

V této kapitole si krok za krokem ukážeme, jak napsat smlouvu pomocí nástroje příkazového řádku `rgb`. Cílem je ukázat, jak nainstalovat CLI a pracovat s ním, zkompilovat **schéma**, importovat **rozhraní** a **implementaci rozhraní** a poté vydat (*vydat*) aktivum. Podíváme se také na základní logiku, včetně kompilace a ověřování stavu. Na konci této kapitoly byste měli být schopni reprodukovat tento proces a vytvořit vlastní smlouvy RGB.

Připomínáme, že vnitřní logika systému RGB je založena na knihovnách Rust, které můžete jako vývojáři importovat do svých projektů a spravovat tak část ověřování na straně klienta. Kromě toho tým sdružení LNP/BP pracuje na vazbách pro další jazyky, ale to ještě není dokončeno. Kromě toho další subjekty, jako například Bitfinex, vyvíjejí vlastní integrační balíčky (o nich budeme hovořit v posledních dvou kapitolách kurzu). Prozatím je tedy CLI `rgb` oficiální referencí, i když zůstává relativně nedoladěný.

### Instalace a prezentace nástroje rgb

Hlavní příkaz se nazývá jednoduše `rgb`. Je navržen tak, aby připomínal `git`, se sadou dílčích příkazů pro manipulaci se smlouvami, jejich vyvolávání, vydávání aktiv atd. Bitcoinová peněženka není v současné době integrována, ale bude v nejbližší verzi (0.11). Tato příští verze umožní uživatelům vytvářet a spravovat peněženky (prostřednictvím deskriptorů) přímo z `rgb`, včetně generování PSBT, kompatibility s externím hardwarem (např. hardwarovou peněženkou) pro podepisování a interoperability se softwarem, jako je Sparrow. Tím se zjednoduší celý scénář vydávání a převodu aktiv.

#### Instalace prostřednictvím služby Cargo

Nástroj nainstalujeme v jazyce Rust pomocí :

```bash
cargo install rgb-contracts --all-features
```

(Poznámka: bedna se jmenuje `rgb-contracts` a nainstalovaný příkaz se bude jmenovat `rgb`. Pokud by bedna s názvem `rgb` již existovala, mohlo by dojít ke kolizi, proto ten název)

Instalace kompiluje velké množství závislostí (např. parsování příkazů, integrace Electrum, správa důkazů nulové znalosti atd.).

Po dokončení instalace se spustí :

```bash
rgb
```

Při spuštění příkazu `rgb` (bez argumentů) se zobrazí seznam dostupných dílčích příkazů, například `interfaces`, `schema`, `import`, `export`, `issue`, `invoice`, `transfer` atd. Můžete změnit adresář místního úložiště (skrýš, která obsahuje všechny protokoly, schémata a implementace), zvolit síť (testnet, mainnet) nebo nakonfigurovat server Electrum.

![RGB-Bitcoin](assets/fr/081.webp)

#### První přehled kontrol

Když spustíte následující příkaz, uvidíte, že rozhraní `RGB20` je již ve výchozím nastavení integrováno:

```bash
rgb interfaces
```

Pokud toto rozhraní není integrováno, klonujte :

```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```

Zkompilujte ji:

```bash
cargo run
```

Poté importujte vybrané rozhraní:

```bash
rgb import interfaces/RGB20.rgb
```

![RGB-Bitcoin](assets/fr/082.webp)

Na druhou stranu nám bylo sděleno, že do softwaru zatím nebylo importováno žádné schéma. Ve skrýši není ani žádná smlouva. Chcete-li si ji prohlédnout, spusťte příkaz :

```bash
rgb schemata
```

Poté můžete úložiště klonovat a získat určitá schémata:

```bash
git clone https://github.com/RGB-WG/rgb-schemata
```

![RGB-Bitcoin](assets/fr/083.webp)

Toto úložiště obsahuje v adresáři `src/` několik souborů Rust (například `nia.rs`), které definují schémata (NIA pro "*Non Inflatable Asset*", UDA pro "*Unique Digital Asset*" atd.). Pro kompilaci pak můžete spustit příkaz :

```bash
cd rgb-schemata
cargo run
```

Tím se vygeneruje několik souborů `.rgb` a `.rgba` odpovídajících sestaveným schématům. Najdete zde například soubor `NonInflatableAsset.rgb`.

#### Import schématu a implementace rozhraní

Nyní můžete schéma importovat do `rgb` :

```bash
rgb import schemata/NonInflatableAssets.rgb
```

![RGB-Bitcoin](assets/fr/084.webp)

Tím se přidá do místní zásoby. Pokud spustíme následující příkaz, uvidíme, že se schéma nyní zobrazí:

```bash
rgb schemata
```

### Vytvoření smlouvy (vystavení)

Existují dva přístupy k vytvoření nového aktiva:


- Buď použijeme skript, nebo kód v jazyce Rust, který sestaví smlouvu vyplněním polí schématu (globální stav, Vlastní stavy atd.) a vytvoří soubor `.rgb` nebo `.rgba`;
- Nebo použijte přímo dílčí příkaz `issue` se souborem YAML (nebo TOML) popisujícím vlastnosti tokenu.

Ve složce `examples` najdete příklady v jazyce Rust, které ukazují, jak sestavit `ContractBuilder`, vyplnit `globální stav` (název aktiva, ticker, dodávku, datum atd.), definovat Vlastní stav (ke kterému UTXO je přiřazen), a pak to vše zkompilovat do *kontraktní zásilky*, kterou můžete exportovat, validovat a importovat do skrýše.

Druhým způsobem je ruční úprava souboru YAML pro přizpůsobení `tickeru`, `jména`, `dodávky` atd. Předpokládejme, že se soubor jmenuje `RGB20-demo.yaml`. Můžete zadat :


- `spec`: ticker, name, precision ;
- `terms`: pole pro právní upozornění ;
- `issuedSupply` : množství vydaných tokenů ;
- `assignments`: označuje jednorázovou plombu (*definice plomby*) a odemčené množství.

Zde je příklad souboru YAML, který je třeba vytvořit:

```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```

![RGB-Bitcoin](assets/fr/085.webp)

Pak jednoduše spusťte příkaz :

```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```

![RGB-Bitcoin](assets/fr/086.webp)

V mém případě je jedinečný identifikátor schématu (uzavřený v jednoduchých uvozovkách) `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` a neuvedl jsem žádného vydavatele. Takže moje objednávka je :

```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```

Pokud ID schématu neznáte, spusťte příkaz :

```bash
rgb schemata
```

CLI odpoví, že byla vydána nová smlouva a přidána do zásoby. Pokud zadáme následující příkaz, uvidíme, že nyní existuje další smlouva, která odpovídá právě vydané smlouvě:

```bash
rgb contracts
```

![RGB-Bitcoin](assets/fr/087.webp)

Další příkaz pak zobrazí globální stavy (jméno, ticker, nabídka...) a seznam vlastněných stavů, tj. alokací (například 1 milion tokenů `PBN` definovaných v UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).

```bash
rgb state '<ContractId>'
```

![RGB-Bitcoin](assets/fr/088.webp)

### Export, import a validace

Chcete-li tuto smlouvu sdílet s ostatními uživateli, můžete ji exportovat ze skrýše do souboru :

```bash
rgb export '<ContractId>' myContractPBN.rgb
```

![RGB-Bitcoin](assets/fr/089.webp)

Soubor `myContractPBN.rgb` lze předat jinému uživateli, který jej může přidat do své skrýše příkazem :

```bash
rgb import myContractPBN.rgb
```

Pokud se jedná o jednoduchou *smluvní zásilku*, zobrazí se při importu zpráva "`Importuji zásilku rgb`". Pokud se jedná o větší *přechodovou zásilku*, bude příkaz jiný (`rgb accept`).

K zajištění platnosti můžete také použít funkci místní validace. Můžete například spustit funkci :

```bash
rgb validate myContract.rgb
```

#### Používání, ověřování a zobrazování zásob

Připomínáme, že úložiště je lokální inventář schémat, rozhraní, implementací a kontraktů (Genesis + přechody). Pokaždé, když spustíte příkaz "import", přidáte do zásobníku prvek. Tuto skrýš si můžete podrobně prohlédnout příkazem :

```bash
rgb dump
```

![RGB-Bitcoin](assets/fr/090.webp)

Tím se vygeneruje složka s podrobnostmi o celé skrýši.

### Převod a PSBT

Chcete-li provést převod, musíte manipulovat s místní peněženkou Bitcoin, abyste mohli spravovat závazky `Tapret` nebo `Opret`.

#### Vytvořit fakturu

Ve většině případů probíhá interakce mezi účastníky smlouvy (např. Alicí a Bobem) prostřednictvím vystavení faktury. Pokud Alice chce, aby Bob něco provedl (převod tokenu, reissue, akci v DAO atd.), Alice vytvoří fakturu s podrobnými instrukcemi pro Boba. Máme tedy :


- Alice** (vystavitel faktury) ;
- Bob** (který přijímá a provádí fakturaci).

Na rozdíl od jiných ekosystémů není faktura RGB omezena na pojem platby. Může obsahovat jakýkoli požadavek spojený se smlouvou: odvolání klíče, hlasování, vytvoření rytiny (*rytiny*) na NFT atd. Příslušnou operaci lze popsat v rozhraní smlouvy. Odpovídající operaci lze popsat v rozhraní smlouvy.

Následující příkaz vygeneruje fakturu RGB:

```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```

S :


- `$CONTRACT`: Identifikátor smlouvy (*ContractId*) ;
- `$INTERFACE`: použité rozhraní (např. `RGB20`) ;
- `$ACTION`: název operace zadané v rozhraní (pro jednoduchý přenos tokenu to může být "Transfer"). Pokud rozhraní již poskytuje výchozí akci, nemusíte ji zde znovu zadávat;
- `$STATE`: stavové údaje, které se mají přenést (například množství tokenů, pokud se přenáší zastupitelný token);
- `$SEAL`: jednorázová pečeť příjemce (Alice), tj. explicitní odkaz na UTXO. Bob použije tuto informaci k sestavení svědecké transakce a příslušný výstup pak bude patřit Alici (v *zaslepené UTXO* nebo nezašifrované podobě).

Například pomocí následujících příkazů

```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```

CLI vygeneruje fakturu jako :

```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```

Bobovi ji lze předat jakýmkoli kanálem (text, QR kód atd.).

#### Provedení převodu

Převod z této faktury :


- Bob (který má žetony ve své skrýši) má peněženku Bitcoin. Potřebuje připravit bitcoinovou transakci (ve formě PSBT, např. `tx.psbt`), která utratí UTXO, v nichž se nacházejí požadované RGB tokeny, plus jedno UTXO pro měnu (směnu) ;
- Bob provede následující příkaz:

```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```


- Tím se vygeneruje soubor `consignment.rgb`, který obsahuje :
 - Historie přechodu prokazuje Alici, že žetony jsou pravé;
 - Nový přechod, který přenáší žetony do Alenčiny jednorázové pečeti ;
 - Svědecká transakce (nepodepsaná).
- Bob odešle tento soubor `consignment.rgb` Alici (e-mailem, prostřednictvím serveru pro sdílení nebo protokolu RGB-RPC, Storm atd.);
- Alice obdrží soubor `consignment.rgb` a přijme jej do své vlastní zásoby:

```bash
alice$ rgb accept consignment.rgb
```


- CLI zkontroluje platnost přechodu a přidá jej do Aliciny zásoby. Pokud je neplatný, příkaz selže s podrobným chybovým hlášením. V opačném případě uspěje a oznámí, že vzorová transakce ještě nebyla vysílána do sítě Bitcoin (Bob čeká na Alicino zelené světlo);
- Jako potvrzení vrátí příkaz `přijmout` podpis (*výplatní pásku*), který může Alice odeslat Bobovi, aby mu ukázala, že potvrdila platnost *zaslání* ;
- Bob pak může podepsat a zveřejnit (`--publish`) svou transakci Bitcoin:

```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```


- Jakmile je tato transakce potvrzena v řetězci, vlastnictví aktiva se považuje za převedené na Alici. Alicina peněženka, která sleduje těžbu transakce, vidí, že se v její skrýši objevil nový vlastněný stát.

V příští kapitole se blíže podíváme na integraci RGB do sítě Lightning.

## RGB v síti Lightning

<chapterId>0962980a-8f94-5d0f-9cd0-43d7f884a01d</chapterId>

![video](https://youtu.be/mqCupTlDbA0)

V této kapitole navrhnu, jak lze RGB využít v rámci sítě Lightning Network k integraci a přesunu aktiv RGB (tokenů, NFT atd.) prostřednictvím platebních kanálů mimo řetězec.

Základní myšlenka spočívá v tom, že přechod stavu RGB (*Přechod stavu*) může být odevzdán do transakce Bitcoin, která zase může zůstat mimo řetězec, dokud se kanál Lightning neuzavře. Takže při každé aktualizaci kanálu může být nový přechod stavu RGB začleněn do nové commitující transakce, která pak zneplatní starý přechod. Tímto způsobem lze kanály Lightning používat k převodu aktiv RGB a lze je směrovat stejným způsobem jako běžné platby Lightning.

### Vytvoření kanálu a financování

K vytvoření kanálu Lightning, který přenáší prostředky RGB, potřebujeme dva prvky:


- Financování Bitcoinu pro vytvoření multisignu kanálu 2/2 (základní UTXO pro kanál);
- Financování RGB, které odesílá prostředky do stejného multisignu.

Z hlediska Bitcoinu musí existovat transakce financování, která definuje referenční UTXO, i když obsahuje jen malé množství sátů (jde jen o to, aby každý výstup v budoucích závazkových transakcích zůstal nad prachovým limitem). Alice se například může rozhodnout poskytnout 10 tisíc satelitů a 500 USDT (vydaných jako aktivum RGB). Při transakci financování přidáme závazek (`Opret` nebo `Tapret`), který zakotví přechod stavu RGB.

![RGB-Bitcoin](assets/fr/091.webp)

Jakmile je transakce financování připravena (ale ještě není odvysílána), jsou vytvořeny transakce závazků, takže kterákoli strana může kanál kdykoli jednostranně uzavřít. Tyto transakce se podobají klasickým závazkovým transakcím Lightningu s tím rozdílem, že přidáváme další výstup obsahující kotvu RGB (OP_RETURN nebo Taproot) spojenou s novým přechodem stavu.

Přechod stavu RGB pak přesune aktiva z multisignálu 2/2 financování do výstupů závazkové transakce. Výhodou tohoto procesu je, že zabezpečení stavu RGB přesně odpovídá mechanice trestání Blesku: pokud Bob odvysílá starý stav kanálu, Alice ho může potrestat a utratit výstup, aby získala zpět jak saty, tak tokeny RGB. Motivace je tedy ještě silnější než v kanálu Lightning bez prostředků RGB, protože útočník může přijít nejen o saty, ale také o prostředky RGB kanálu.

Transakce závazku podepsaná Alicí a odeslaná Bobovi by tedy vypadala takto:

![RGB-Bitcoin](assets/fr/092.webp)

A doprovodná transakce závazku, podepsaná Bobem a odeslaná Alici, bude vypadat takto:

![RGB-Bitcoin](assets/fr/093.webp)

### Aktualizace kanálu

Když dojde k platbě mezi dvěma účastníky kanálu (nebo když si přejí změnit alokaci aktiv), vytvoří nový pár závazkových transakcí. Částka v sátech na každém výstupu může, ale nemusí zůstat nezměněna v závislosti na implementaci, protože její hlavní úlohou je umožnit konstrukci platných UTXO. Na druhé straně výstup OP_RETURN (nebo Taproot) musí být upraven tak, aby obsahoval novou kotvu RGB, která představuje nové rozdělení aktiv v kanálu.

Například pokud Alice převede 30 USDT Bobovi v kanálu, nový přechod stavu bude odrážet zůstatek 400 USDT pro Alici a 100 USDT pro Boba. Transakce odevzdání je přidána (nebo upravena) do kotvy OP_RETURN/Taproot, aby zahrnovala tento přechod. Všimněte si, že z pohledu RGB zůstává vstupem do přechodu počáteční multisig (kde jsou aktiva v řetězci skutečně alokována až do uzavření kanálu). Mění se pouze výstupy RGB (alokace) v závislosti na přerozdělení, o kterém bylo rozhodnuto.

Transakce závazku podepsaná Alicí, připravená k distribuci Bobem :

![RGB-Bitcoin](assets/fr/094.webp)

Transakce závazku podepsaná Bobem, připravená k distribuci Alicí :

![RGB-Bitcoin](assets/fr/095.webp)

### Řízení HTLC

Síť Lightning Network ve skutečnosti umožňuje směrování plateb více kanály pomocí smluv HTLC (*Hashed Time-Locked Contracts*). Stejné je to s RGB: pro každou platbu, která prochází kanálem, je k odevzdávající transakci přidán výstup HTLC a k tomuto HTLC je přiřazen příděl RGB. Kdo tedy utratí výstup HTLC (díky tajence nebo po vypršení časového zámku), získá zpět jak saty, tak související aktiva RGB. Na druhou stranu je samozřejmě potřeba mít na cestě dostatek hotovosti v podobě sats i RGB aktiv.

![RGB-Bitcoin](assets/fr/096.webp)

Fungování systému RGB v síti Lightning je proto třeba posuzovat souběžně s fungováním samotné sítě Lightning. Pokud byste se chtěli tomuto tématu věnovat hlouběji, vřele doporučuji podívat se na toto další komplexní školení:

https://planb.network/courses/lnp201
### Kódová mapa RGB

Nakonec, než přejdeme k další části, bych vám rád poskytl přehled kódu použitého v RGB. Protokol je založen na sadě knihoven Rust a specifikacích open source. Zde je přehled hlavních repozitářů a beden:

![RGB-Bitcoin](assets/fr/097.webp)

#### Ověřování na straně klienta


- Úložiště**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- Bedny** : [client_side_validation](https://crates.io/crates/client_side_validation), [single_use_seals](https://crates.io/crates/single_use_seals)

Správa logiky validace mimo řetězec a logiky jednorázových pečetí.

#### Deterministické závazky Bitcoinu (DBC)


- Úložiště**: [bp-core](https://github.com/BP-WG/bp-core)
- Bedna**: [bp-dbc](https://crates.io/crates/bp-dbc)

Správa deterministického ukotvení v transakcích Bitcoin (Tapret, OP_RETURN atd.).

#### Závazky více protokolů (MPC)


- Úložiště**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- Bedna** : [commit_verify](https://crates.io/crates/commit_verify)

Více kombinací zapojení a integrace s různými protokoly.

#### Přísné typy a přísné kódování


- Specifikace**: [webová stránka strict-types.org](https://www.strict-types.org/)
- Úložiště**: [strict-types](https://github.com/strict-types/strict-types), [strict-encoding](https://github.com/strict-types/strict-encoding)
- Bedny** : [strict_types](https://crates.io/crates/strict_types), [strict_encoding](https://crates.io/crates/strict_encoding)

Systém přísného typování a deterministické serializace používaný pro validaci na straně klienta.

#### Jádro RGB


- Úložiště**: [rgb-core](https://github.com/RGB-WG/rgb-core)
- Bedna**: [rgb-core](https://crates.io/crates/rgb-core)

Jádro protokolu, které zahrnuje hlavní logiku ověřování RGB.

#### Standardní knihovna RGB a peněženka


- Úložiště**: [rgb-std](https://github.com/RGB-WG/rgb-std)
- Bedna** : [rgb-std](https://crates.io/crates/rgb-std)

Standardní implementace, správa zásob a peněženek.

#### RGB CLI


- Úložiště**: [rgb](https://github.com/RGB-WG/rgb)
- Bedny**: [rgb-cli](https://crates.io/crates/rgb-cli), [rgb-wallet](https://crates.io/crates/rgb-wallet)

CLI `rgb` a peněženka crate pro manipulaci s kontrakty z příkazového řádku.

#### Schéma RGB


- Úložiště**: [rgb-schemata](https://github.com/RGB-WG/rgb-schemata/)

Obsahuje příklady schémat (NIA, UDA atd.) a jejich implementací.

#### ALuVM


- Informace** : [aluvm.org](https://www.aluvm.org/)
- Úložiště**: [aluvm-spec](https://github.com/AluVM/aluvm-spec), [alure](https://github.com/AluVM/alure)
- Bedny**: [aluvm](https://crates.io/crates/aluvm), [aluasm](https://crates.io/crates/aluasm)

Virtuální počítač založený na registru, který se používá ke spouštění ověřovacích skriptů.

#### Protokol Bitcoin - BP


- Úložiště** : [bp-core](https://github.com/BP-WG/bp-core), [bp-std](https://github.com/BP-WG/bp-std), [bp-wallet](https://github.com/BP-WG/bp-wallet)

Doplňky pro podporu protokolu Bitcoin (transakce, obchvaty atd.).

#### Všudypřítomné deterministické výpočty - UBIDECO


- Úložiště**: [UBIDECO](https://github.com/UBIDECO)

Ekosystém spojený s deterministickým vývojem s otevřeným zdrojovým kódem.

# Stavba na RGB

<partId>3b4b0d66-0c1b-505a-b5ca-4b2e57dd73c2</partId>

## DIBA a projekt Bitmask

<chapterId>dc92a5e8-ed93-5a3f-bcd0-d433932842f4</chapterId>

![video](https://youtu.be/nbUtV8GOR_U)

Tato závěrečná část kurzu je založena na prezentacích různých řečníků z bootcampu RGB. Obsahuje výpovědi a úvahy o RGB a jeho ekosystému a také prezentace nástrojů a projektů založených na tomto protokolu. Tuto první kapitolu moderuje Hunter Beast a další dvě Frederico Tenga.

### Od JavaScriptu k Rustu a do ekosystému Bitcoinu

Zpočátku Hunter Beast pracoval hlavně v jazyce JavaScript. Pak objevil **Rust**, jehož syntaxe se mu zpočátku zdála nevábná a frustrující. Postupně však ocenil sílu tohoto jazyka, kontrolu nad pamětí (*heap* a *stack*) a s tím související bezpečnost a výkon. Zdůrazňuje, že jazyk Rust je vynikajícím tréninkovým prostředím pro hluboké pochopení fungování počítače.

Hunter Beast vypráví o své minulosti v různých projektech v *altcoinovém* ekosystému, jako je Ethereum (se Solidity, TypeScriptem atd.) a později Filecoin. Vysvětluje, že zpočátku byl některými protokoly nadšen, ale nakonec se většinou z nich cítil rozčarován, v neposlední řadě kvůli jejich tokenomii. Odsuzuje pochybné finanční pobídky, inflační tvorbu tokenů, která ředí investory, a potenciálně vykořisťovatelský aspekt těchto projektů. Nakonec tedy zaujal **Bitcoinový maximalistický** postoj, a to i proto, že mu někteří lidé otevřeli oči, aby si uvědomil, že Bitcoin má pevnější ekonomické mechanismy a že tento systém je robustní.

### Přitažlivost RGB a vytváření vrstev

O významu Bitcoinu ho podle jeho slov definitivně přesvědčil objev RGB a konceptu vrstev. Je přesvědčen, že stávající funkce na jiných blockchainech by mohly být reprodukovány na vyšších vrstvách, nad Bitcoinem, aniž by se změnil základní protokol.

V únoru 2022 nastoupil do společnosti **DIBA**, aby pracoval konkrétně na RGB, a zejména na peněžence **Bitmask**. V té době byl Bitmask stále ve verzi 0.01 a RGB běžel ve verzi 0.4, pouze pro správu jednotlivých tokenů. Poznamenává, že to bylo méně orientované na vlastní úschovu než dnes, protože logika byla částečně založena na serveru. Od té doby se architektura vyvinula směrem k tomuto modelu, který bitcoináři velmi oceňují.

### Základy protokolu RGB

Protokol **RGB** je nejnovějším a nejpokročilejším ztělesněním konceptu _barevných mincí_, který byl zkoumán již v letech 2012-2013. V té době se několik týmů snažilo přiřadit různé hodnoty bitcoinů na UTXO, což vedlo k několika roztroušeným implementacím. Tento nedostatek standardizace a nízká poptávka v té době zabránily tomu, aby se tato řešení trvale prosadila.

Dnes se RGB vyznačuje koncepční robustností a jednotnými specifikacemi prostřednictvím sdružení LNP/BP. Princip je založen na validaci na straně klienta. V bitcoinovém blockchainu jsou uloženy pouze kryptografické závazky (_commitments_, prostřednictvím Taproot nebo OP_RETURN), zatímco většinu dat (definice smluv, historie převodů atd.) ukládají příslušní uživatelé. Tímto způsobem je rozloženo zatížení úložiště a posílena důvěrnost výměn, aniž by byl blockchain zatížen. Tento přístup umožňuje vytvářet zastupitelná aktiva (standard **RGB20**) nebo jedinečná aktiva (standard **RGB21**), a to v modulárním a škálovatelném rámci.

### Funkce tokenu (RGB20) a unikátní aktiva (RGB21)

Pomocí **RGB20** definujeme zastupitelný token v Bitcoinu. Emitent si zvolí _dodávku_, _přesnost_ a vytvoří _smlouvu_, ve které pak může provádět převody. Každý převod je vztažen k bitcoinovému UTXO, který funguje jako *jednorázová pečeť*. Tato logika zajišťuje, že uživatel nebude moci utratit stejné aktivum dvakrát, protože klíč k aktualizaci stavu kontraktu na straně klienta má ve skutečnosti pouze osoba schopná UTXO utratit.

**RGB21** se zaměřuje na jedinečné prostředky (neboli "NFT"). Aktivum má zásobu 1 a může být spojeno s metadaty (obrazový soubor, zvuk atd.) popsanými prostřednictvím konkrétního pole. Na rozdíl od NFT na veřejných blockchainech mohou data a jejich identifikátory MIME zůstat soukromé, distribuované peer-to-peer podle uvážení vlastníka.

### Řešení Bitmask: peněženka pro RGB

Pro využití možností RGB v praxi navrhl projekt **DIBA** peněženku s názvem [Bitmask](https://bitmask.app/). Smyslem je poskytnout nástroj založený na technologii Taproot, který není založen na úschově a je přístupný jako webová aplikace nebo rozšíření prohlížeče. Bitmask spravuje aktiva RGB20 i RGB21 a integruje různé bezpečnostní mechanismy:


- Jádro kódu je napsáno v jazyce Rust a poté zkompilováno v jazyce WebAssembly, aby mohlo běžet v prostředí JavaScriptu (React);
- Klíče jsou generovány lokálně a následně uloženy šifrované lokálně;
- Stavová data (stash) jsou uložena v paměti, serializována a šifrována pomocí knihovny **Carbonado**, která provádí kompresi, opravu chyb, šifrování a ověřování datových toků pomocí Blake3.

Díky této architektuře probíhají všechny transakce s aktivy na straně klienta. Z vnějšího pohledu není bitcoinová transakce ničím jiným než klasickou výdajovou transakcí Taproot, u které by nikdo netušil, že v sobě nese také převod zastupitelných tokenů nebo NFT. Absence přetěžování na řetězci (žádná veřejně uložená metadata) zaručuje určitou míru diskrétnosti a usnadňuje odolávání případným pokusům o cenzuru.

### Bezpečnost a distribuovaná architektura

Vzhledem k tomu, že protokol RGB vyžaduje, aby každý účastník uchovával historii svých transakcí (aby prokázal platnost převodů, které přijímá), vyvstává otázka ukládání. Bitmask navrhuje tuto úschovu serializovat lokálně a poté ji odeslat na několik serverů nebo cloudů (volitelně). Data zůstávají zašifrována uživatelem prostřednictvím **Carbonado**, takže je server nemůže přečíst. V případě částečného poškození může vrstva pro opravu chyb obsah obnovit.

Použití CRDT (_Conflict-free replicated data type_) umožňuje sloučit různé verze zásobníku, pokud se rozcházejí. Každý může tato data hostovat, kdekoli si přeje, protože žádný plný uzel nenese všechny informace spojené s aktivem. To přesně odráží filozofii *Ověřování na straně klienta*, kdy každý vlastník odpovídá za ukládání důkazů o platnosti svého aktiva RGB.

### Směrem k širšímu ekosystému: trh, interoperabilita a nové funkce

Společnost Bitmask se neomezuje na pouhý vývoj peněženky. DIBA má v úmyslu vyvinout :


- **Tržiště** pro výměnu žetonů, zejména ve formě **RGB21**;
- Kompatibilita s jinými peněženkami (například *Iris Wallet*);
- Techniky dávkování přenosů**, tj. možnost zahrnout několik po sobě jdoucích přenosů RGB do jedné transakce.

Zároveň pracujeme na **WebBTC** nebo **WebLN** (standardy umožňující webovým stránkám požádat peněženku o podepsání transakcí Bitcoin nebo Lightning) a také na možnosti "teleburn" záznamů Ordinals (pokud chceme repatriovat Ordinals do diskrétnějšího a flexibilnějšího formátu RGB).

### Závěr

Celý proces ukazuje, jak lze ekosystém RGB nasadit a zpřístupnit koncovým uživatelům prostřednictvím robustních technických řešení. Přechod od altcoinového pohledu k vizi více zaměřené na Bitcoin spolu s objevem *Client-side Validation* ilustruje poměrně logickou cestu: chápeme, že je možné implementovat různé funkce (zastupitelné tokeny, NFT, smart contracts...) bez forkování blockchainu, jednoduše využitím kryptografických závazků na transakcích Taproot nebo OP_RETURN.

Peněženka **Bitmask** je součástí tohoto přístupu: na straně blockchainu vidíte pouze obyčejnou transakci s Bitcoinem, na straně uživatele manipulujete s webovým rozhraním, kde vytváříte, vyměňujete a ukládáte nejrůznější aktiva mimo řetězec. Tento model jasně odděluje peněžní infrastrukturu (Bitcoin) od logiky vydávání a převodů (RGB) a zároveň zajišťuje vysokou úroveň důvěrnosti a lepší škálovatelnost.

## Práce společnosti Bitfinex na RGB

<chapterId>d4d80e07-5eac-5b29-a93a-123180e97047</chapterId>

![vidéo](https://youtu.be/5iAhsgCSL3U)

V této kapitole, založené na prezentaci Frederica Tengy, se podíváme na soubor nástrojů a projektů vytvořených týmem Bitfinex, které se věnují RGB a jejichž cílem je podpořit vznik bohatého a rozmanitého ekosystému kolem tohoto protokolu. Původním cílem týmu není vydat konkrétní komerční produkt, ale spíše poskytnout softwarové stavební kameny, přispět k samotnému protokolu RGB a navrhnout konkrétní referenční implementace, jako je mobilní peněženka (*Iris Wallet*) nebo uzel Lightning kompatibilní s RGB.

### Souvislosti a cíle

Zhruba od roku 2022 se tým Bitfinex RGB soustředí na vývoj technologického balíčku, který umožňuje efektivní využívání a testování RGB. Bylo vytvořeno několik příspěvků:


- Účast na specifikacích zdrojového kódu a protokolu, včetně psaní návrhů na vylepšení, opravování chyb atd;
- Nástroje pro vývojáře, které zjednodušují integraci RGB do jejich aplikací;
- Návrh mobilní peněženky s názvem [Iris](https://iriswallet.com/) pro experimentování a ilustraci osvědčených postupů pro používání RGB ;
- Vytvoření přizpůsobeného uzlu Lightning, který dokáže spravovat kanály s prostředky RGB;
- Podpora dalších týmů, které vytvářejí řešení na platformě RGB, s cílem podpořit rozmanitost a silný ekosystém.

Cílem tohoto přístupu je pokrýt celý řetězec potřeb: od nízkoúrovňové knihovny (*[RGBlib](https://github.com/RGB-Tools/rgb-lib)*), která umožňuje implementaci peněženky, až po produkční aspekt (uzel Lightning, peněženka pro Android atd.).

### Knihovna RGBlib: zjednodušení vývoje aplikací RGB

Důležitým bodem demokratizace tvorby peněženek a aplikací RGB je zpřístupnění dostatečně jednoduché abstrakce, aby se vývojáři nemuseli učit vše o vnitřní logice protokolu. Přesně to je cílem **RGBlib** napsaného v jazyce Rust.

RGBlib funguje jako most mezi velmi flexibilními (ale někdy složitými) požadavky na RGB, které jsme mohli studovat v předchozích kapitolách, a konkrétními potřebami vývojáře aplikací. Jinými slovy, peněženka (nebo služba), která chce spravovat převody tokenů, vydávání aktiv, ověřování atd. se může spolehnout na RGBlib, aniž by znala každý kryptografický detail nebo každý přizpůsobitelný parametr RGB.

Knihkupectví nabízí :


- Funkce na klíč pro vydávání (_vydávání_) aktiv (zastupitelných i nezastupitelných);
- Schopnost přenášet (odesílat/přijímat) aktiva pomocí manipulace s jednoduchými objekty (adresy, částky, UTXO atd.);
- Mechanismus pro ukládání a načítání stavových informací (*přihlášek*) potřebných pro Ověřování na straně klienta.

RGBlib se proto spoléhá na složité pojmy specifické pro RGB (ověřování na straně klienta, kotvy Tapret/Opret), ale zapouzdřuje je tak, aby konečná aplikace nemusela vše přeprogramovávat nebo činit riskantní rozhodnutí. RGBlib je navíc již svázán s několika jazyky (Kotlin a Python), což otevírá dveře k využití i mimo prostý svět Rustu.

### Peněženka Iris: příklad peněženky RGB v systému Android

Aby tým Bitfinexu prokázal účinnost RGBlib, vyvinul **Iris Wallet**, v této fázi výhradně pro Android. Jedná se o mobilní peněženku, která ilustruje uživatelské prostředí podobné běžným bitcoinovým peněženkám: můžete vydat aktivum, odeslat ho, přijmout a zobrazit jeho historii, přičemž zůstává v modelu self-custody.

Iris má řadu zajímavých funkcí:

**Používání serveru Electrum:**

Stejně jako každá peněženka potřebuje Iris vědět o potvrzeních transakcí v blockchainu. Namísto vložení kompletního uzlu se Iris ve výchozím nastavení obrací na server Electrum spravovaný týmem Bitfinex. Uživatelé si však mohou nakonfigurovat vlastní server nebo jinou službu třetí strany. Tímto způsobem lze modulárním způsobem ověřovat bitcoinové transakce a vyhledávat informace (indexovat).

**Proxy server RGB:**

Na rozdíl od Bitcoinu vyžaduje RGB výměnu metadat mimo řetězec (*konsignace*) mezi odesílatelem a příjemcem. Pro zjednodušení tohoto procesu nabízí Iris řešení, kdy komunikace probíhá prostřednictvím proxy serveru. Přijímající peněženka vygeneruje *fakturu*, ve které je uvedeno, kam má odesílatel poslat data na straně *klienta*. Ve výchozím nastavení URL ukazuje na proxy server hostovaný týmem Bitfinex, ale tento proxy server můžete změnit (nebo hostovat svůj vlastní). Myšlenkou je návrat ke známému uživatelskému prostředí, kdy příjemce zobrazí QR kód a odesílatel tento kód naskenuje pro transakci, bez jakýchkoli složitých dalších manipulací.

**Kontinuální zálohování:**

V čistě bitcoinovém kontextu je zálohování seedu obecně dostačující (i když v dnešní době doporučujeme zálohovat spíše seed a deskriptory). V případě RGB to nestačí: musíte také uchovávat místní historii (*konsignace*), která dokazuje, že aktivum RGB skutečně vlastníte. Pokaždé, když obdržíte příjemku, zařízení uloží nová data, která jsou nezbytná pro následné utrácení. Iris automaticky spravuje šifrovanou zálohu na uživatelově Disku Google. To nevyžaduje žádnou zvláštní důvěru ve společnost Google, protože záloha je šifrovaná, a do budoucna se plánují robustnější možnosti (například osobní server), aby se předešlo riziku cenzury nebo vymazání třetím provozovatelem.

**Další funkce:**


- Vytvořte kohoutek pro rychlé testování nebo distribuci žetonů pro experimentování nebo propagaci;
- Certifikační systém (v současné době centralizovaný), který umožňuje rozlišit legitimní token od falešného tokenu kopírujícího známý ticker. V budoucnu se tato certifikace může stát více decentralizovanou (prostřednictvím DNS nebo jiných mechanismů).

Celkově vzato nabízí Iris uživatelský zážitek blízký klasické peněžence Bitcoin a maskuje další složitost (správa zásob, historie *zasílání* atd.) díky RGBlib a použití proxy serveru.

### Proxy server a uživatelské prostředí

Výše představený proxy server si zaslouží podrobnější popis, protože je klíčem k bezproblémovému uživatelskému prostředí. Namísto toho, aby odesílatel musel ručně předávat *odkazy* příjemci, probíhá transakce RGB na pozadí prostřednictvím serveru :


- Příjemce vygeneruje *fakturu* (obsahující mimo jiné adresu zmocněnce);
- Odesílatel odešle (prostřednictvím požadavku HTTP) přechodový projekt (*zaslání*) proxy serveru ;
- Příjemce načte tento projekt a provede lokální ověření na straně klienta;
- Příjemce pak prostřednictvím zprostředkovatele zveřejní přijetí (nebo případně odmítnutí) přechodu stavu ;
- Odesílatel si může prohlédnout stav ověření a v případě jeho přijetí odvysílat transakci Bitcoin, čímž převod dokončí.

Tímto způsobem se peněženka chová téměř jako běžná peněženka. Uživatel si není vědom všech mezikroků. Je sice pravda, že současná proxy není šifrovaná ani ověřená (což ponechává obavy o důvěrnost a integritu), ale tato vylepšení jsou možná v pozdějších verzích. Koncept proxy zůstává velmi užitečný pro obnovení zážitku "pošlu QR kód, ty naskenuješ a zaplatíš".

### Integrace RGB v síti Lightning

Dalším klíčovým bodem práce týmu Bitfinex je zajištění kompatibility sítě Lightning s aktivy RGB. Cílem je umožnit Lightning kanály v USDT (nebo jakémkoli jiném tokenu) a využívat stejné výhody jako bitcoin v Lightningu (téměř okamžité transakce, směrování atd.). Konkrétně jde o vytvoření uzlu Lightning upraveného na :


- Otevřete kanál tak, že do financujícího multisignálu UTXO umístíte nejen satelity, ale také jeden nebo více prostředků RGB;
- Generování transakcí Lightning commitment (na straně Bitcoinu) doprovázených odpovídajícími přechody stavů RGB. Při každé aktualizaci kanálu se přechodem RGB předefinuje rozložení aktiv ve výstupech Lightning;
- Umožňuje jednostranné uzavření, kdy je aktivum získáno ve výlučném UTXO v souladu s pravidly Lightning Network (HTLC, časový zámek, trest atd.).

Toto řešení, nazvané "**RGB Lightning Node**", používá jako základ sadu LDK (*Lightning Dev Kit*) a přidává mechanismy potřebné k vkládání tokenů RGB do kanálů. Závazky Lightning si zachovávají klasickou strukturu (bodovatelné výstupy, časový zámek...) a navíc ukotvují přechod do stavu RGB (prostřednictvím `Opret` nebo `Tapret`). Uživateli se tak otevírá cesta k Lightning kanálům ve stablecoinech nebo v jakémkoli jiném aktivu emitovaném prostřednictvím RGB.

### Potenciál DEX a dopad na Bitcoin

Jakmile je prostřednictvím služby Lightning spravováno několik aktiv, je možné si představit **atomickou výměnu** na jediné směrovací cestě služby Lightning, která využívá stejnou logiku tajemství a časových zámků. Například uživatel A drží bitcoin na jednom kanálu Lightning a uživatel B drží USDT RGB na jiném kanálu Lightning. Mohou vytvořit cestu spojující jejich dva kanály a současně vyměnit BTC za USDT, aniž by potřebovali důvěru. Nejedná se o nic jiného než o **atomickou výměnu** probíhající v několika skocích, díky čemuž si vnější účastníci téměř neuvědomují, že provádějí obchod, nikoliv jen směrování. Tento přístup nabízí :


- Velmi nízká latence, protože vše zůstává mimo řetězec Lightning.
- Vynikající **privátnost**: nikdo neví, že jde o obchod, a ne o běžné směrování ;
- Vyhnutí se frontrunningu, který je opakovaným problémem pro DEX v řetězci ;
- Snížení nákladů (neplatíte blokovací prostor, pouze poplatky za směrování blesku).

Můžeme si pak představit ekosystém, kde uzly Lightning nabízejí swapové ceny (poskytováním likvidity). Každý uzel, pokud chce, může hrát roli _tvůrce trhu_ a nakupovat a prodávat různá aktiva na platformě Lightning. Tato perspektiva _vrstvy-2_ DEX posiluje myšlenku, že k získání decentralizované burzy aktiv není nutné forkovat nebo používat blockchainy třetích stran.

Dopad na Bitcoin by mohl být pozitivní: Infrastruktura Lightningu (uzly, kanály a služby) by byla plněji využívána díky objemům generovaným těmito *stablecoiny*, deriváty a dalšími tokeny. Obchodníci, kteří mají zájem o platby USDT na Lightningu, by mechanicky objevili platby BTC na Lightningu (spravované stejným stackem). Údržba a financování infrastruktury Lightning Network by také mohly těžit z multiplikace těchto ne-BTC toků, z čehož by nepřímo profitovali uživatelé Bitcoinu.

### Závěr a zdroje

Tým Bitfinexu, který se věnuje RGB, svou prací ilustruje rozmanitost toho, co lze nad protokolem provádět. Na jedné straně je tu RGBlib, knihovna, která usnadňuje návrh peněženek a aplikací. Na straně druhé tu máme Iris Wallet, praktickou ukázku přehledného rozhraní pro koncové uživatele na systému Android. A konečně integrace RGB s Lightningem ukazuje, že stablecoinové kanály jsou možné, a otevírá cestu k potenciálnímu decentralizovanému DEX na Lightningu.

Tento přístup zůstává do značné míry experimentální a nadále se vyvíjí: knihovna RGBlib se zdokonaluje za pochodu, Iris Wallet dostává pravidelná vylepšení a specializovaný uzel Lightning zatím není hlavním klientem Lightning.

Pro ty, kteří se chtějí dozvědět více nebo přispět, je k dispozici několik zdrojů, včetně :


- [Úložiště nástrojů GitHub RGB](https://github.com/RGB-Tools);
- [Informační stránka věnovaná peněžence Iris](https://iriswallet.com/) a otestovat peněženku v systému Android.

V příští kapitole se blíže podíváme na to, jak spustit uzel RGB Lightning.

## RLN - RGB Lightning Node

<chapterId>ecaabe32-20ba-5f8c-8ca1-a3f095792958</chapterId>

![vidéo](https://youtu.be/piQQH4Q2nr0)

V této závěrečné kapitole vás Frederico Tenga krok za krokem provede nastavením uzlu Lightning RGB v prostředí Regtest a ukáže vám, jak v něm vytvořit tokeny RGB. Spuštěním dvou samostatných uzlů také zjistíte, jak mezi nimi otevřít kanál Lightning a vyměňovat aktiva RGB.

Toto video slouží jako výukový program podobný tomu, který jsme probírali v předchozí kapitole, ale tentokrát se zaměřuje konkrétně na Lightning!

Hlavním zdrojem pro toto video je repozitář Github [RGB Lightning Node](https://github.com/RGB-Tools/rgb-lightning-node), který vám usnadní spuštění této konfigurace v Regtestu.

### Nasazení uzlu Lightning kompatibilního s RGB

Tento proces přebírá a v praxi uplatňuje všechny koncepty, které byly popsány v předchozích kapitolách:


- Myšlenka, že **UTXO** blokován na 2/2 multisig kanálu Lightning může přijímat nejen bitcoins, ale také být jednorázové pečeť RGB aktiv (zaměnitelné nebo ne);
- Přidání výstupu (`Tapret` nebo `Opret`) určeného k ukotvení přechodu stavu RGB v každé transakci Lightning engagement;
- Související infrastruktura (bitcoind/indexer/proxy) pro ověřování transakcí Bitcoin a výměnu dat na straně klienta.

### Představujeme rgb-lightning-node

Projekt **`rgb-lightning-node`** je démon Rustu založený na vidlici `rust-lightning` (LDK) upravené tak, aby zohledňovala existenci RGB aktiv v kanálu. Při otevření kanálu lze zadat přítomnost aktiv a při každé aktualizaci stavu kanálu se vytvoří přechod RGB, který odráží rozložení aktiv ve výstupech Lightning. To umožňuje :


- Otevřete například kanály Lightning v USDT;
- Směrovat tyto tokeny po síti za předpokladu, že směrovací cesty mají dostatečnou likviditu;
- Využití logiky trestu a časového zámku blesku bez úprav: stačí ukotvit přechod RGB v dalším výstupu transakce závazku.

Kód je stále ve fázi alfa: doporučujeme jej používat pouze v **regtestu** nebo na **testnetu**.

### Instalace uzlů

Pro kompilaci a instalaci binárního souboru `rgb-lightning-node` začneme klonováním úložiště a jeho podmodulů a poté spustíme příkaz :

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RGB-Bitcoin](assets/fr/098.webp)


- Volba `--recurse-submodules` rovněž klonuje potřebná dílčí zařízení (včetně upravené verze `rust-lightning`);
- Volba `--shallow-submodules` omezuje hloubku klonu, aby se urychlilo stahování, a zároveň poskytuje přístup k základním revizím.

V kořenovém adresáři projektu spusťte následující příkaz pro kompilaci a instalaci binárního souboru :

```bash
cargo install --locked --debug --path .
```

![RGB-Bitcoin](assets/fr/099.webp)


- `--locked` zajišťuje, že verze závislostí je striktně dodržována;
- `--debug` není povinné, ale může vám pomoci se soustředit (pokud chcete, můžete použít `--release`) ;
- `--path .` říká `cargo install`, aby instaloval z aktuálního adresáře.

Na konci tohoto příkazu bude ve vašem `$CARGO_HOME/bin/` k dispozici spustitelný soubor `rgb-lightning-node`. Ujistěte se, že je tato cesta ve vašem `$PATH`, abyste mohli příkaz vyvolat z libovolného adresáře.

### Požadavky na výkon

Démon `rgb-lightning-node` vyžaduje pro svou funkci přítomnost a konfiguraci :


- Uzel `bitcoind`**

Každá instance RLN bude muset komunikovat s `bitcoind`, aby mohla vysílat a monitorovat své transakce v řetězci. Démonovi bude třeba poskytnout autentizaci (přihlašovací jméno/heslo) a adresu URL (hostitel/port).


- Indexer** (Electrum nebo Esplora)

Démon musí být schopen vypsat a prozkoumat transakce v řetězci, zejména najít UTXO, na kterém bylo aktivum ukotveno. Je třeba zadat adresu URL serveru Electrum nebo Esplora.


- Proxy server RGB**

Jak bylo uvedeno v předchozích kapitolách, **proxy server** je komponenta (volitelná, ale velmi doporučená), která zjednodušuje výměnu *přenosů* mezi vrstevníky Lightning. Opět je třeba zadat adresu URL.

ID a adresy URL se zadávají při _odemknutí_ démona prostřednictvím rozhraní API. Více o tom později.

### Spuštění Regtestu

Pro jednoduché použití je k dispozici skript `regtest.sh`, který prostřednictvím nástroje Docker automaticky spustí sadu služeb: `bitcoind`, `electrs` (indexer), `rgb-proxy-server`.

![RGB-Bitcoin](assets/fr/100.webp)

To umožňuje spustit místní, izolované a předem nakonfigurované prostředí. Při každém restartu vytvoří a zničí kontejnery a datové adresáře. Začneme tím, že spustíme :

```bash
./regtest.sh start
```

Tento skript bude :


- Vytvoření adresáře `docker/` pro uložení ;
- Spusťte `bitcoind` v regtestu, stejně jako indexer `electrs` a `rgb-proxy-server` ;
- Počkejte, až bude vše připraveno k použití.

![RGB-Bitcoin](assets/fr/101.webp)

Dále spustíme několik uzlů RLN. V samostatných shellech spusťte například (pro spuštění 3 uzlů RLN) :

```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```

![RGB-Bitcoin](assets/fr/102.webp)


- Parametr `--network regtest` označuje použití konfigurace regtest;
- `--daemon-listening-port` udává, na kterém portu REST bude uzel Lightning naslouchat voláním API (JSON);
- `--ldk-peer-listening-port` určuje, na kterém portu Lightning p2p se má naslouchat;
- `dataldk0/`, `dataldk1/` jsou cesty k úložným adresářům (každý uzel ukládá své informace samostatně).

Příkazy na uzlech RLN můžete spouštět také z prohlížeče:

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

Aby mohl uzel otevřít kanál, musí mít nejprve bitcoiny na adrese vygenerované následujícím příkazem (například pro uzel č. 1):

```bash
curl -X POST http://localhost:3001/address
```

Odpověď vám poskytne adresu.

![RGB-Bitcoin](assets/fr/103.webp)

V regtestu `bitcoind` budeme těžit několik bitcoinů. Spusťte :

```bash
./regtest.sh mine 101
```

![RGB-Bitcoin](assets/fr/104.webp)

Zašlete finanční prostředky na výše vygenerovanou adresu uzlu:

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RGB-Bitcoin](assets/fr/105.webp)

Poté vytěžte blok a potvrďte transakci:

```bash
./regtest.sh mine 1
```

![RGB-Bitcoin](assets/fr/106.webp)

### Spuštění Testnetu (bez Dockeru)

Pokud chcete otestovat realističtější scénář, můžete v testovací síti místo v Regtestu spustit 3 uzly RLN, které budou směřovat na veřejné služby:

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

Ve výchozím nastavení, pokud není nalezena žádná konfigurace, se démon pokusí použít :


- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`

S přihlášením :


- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`

Tyto prvky můžete také přizpůsobit prostřednictvím rozhraní API `init`/`unlock`.

### Vydání tokenu RGB

Pro vydání tokenu začneme vytvořením "barevných" UTXO:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```

![RGB-Bitcoin](assets/fr/107.webp)

Pořadí můžete samozřejmě upravit. Pro potvrzení transakce těžíme :

```bash
./regtest.sh mine 1
```

Nyní můžeme vytvořit aktivum RGB. Příkaz bude záviset na typu aktiva, které chcete vytvořit, a jeho parametrech. Zde vytvářím token NIA (*Non Inflatable Asset*) s názvem "PBN" se zásobou 1000 jednotek. Příkaz `přesnost` umožňuje definovat dělitelnost jednotek.

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```

![RGB-Bitcoin](assets/fr/108.webp)

Odpověď obsahuje ID nově vytvořeného aktiva. Nezapomeňte si tento identifikátor poznamenat. V mém případě je to :

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RGB-Bitcoin](assets/fr/109.webp)

Poté ji můžete přenést v řetězci nebo přidělit v kanálu Lightning. Přesně to uděláme v následující části.

### Otevření kanálu a přenos aktiva RGB

Nejprve je nutné připojit uzel k partnerovi v síti Lightning pomocí příkazu `/connectpeer`. V mém příkladu ovládám oba uzly. Tímto příkazem tedy získám veřejný klíč svého druhého uzlu Lightning:

```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```

Příkaz vrátí veřejný klíč mého uzlu č. 2 :

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RGB-Bitcoin](assets/fr/110.webp)

Dále otevřeme kanál zadáním příslušného aktiva (`PBN`). Příkaz `/openchannel` umožňuje definovat velikost kanálu v satoshi a rozhodnout se pro zařazení aktiva RGB. Záleží na tom, co chcete vytvořit, ale v mém případě je příkaz :

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```

Více informací najdete zde:


- `peer_pubkey_and_opt_addr`: Identifikátor peera, ke kterému se chceme připojit (veřejný klíč, který jsme našli dříve);
- `capacity_sat`: Celková kapacita kanálu v satoshi ;
- `push_msat`: (zde okamžitě přenesu 10 000 sats, aby mohl později provést přenos RGB) ;
- `asset_amount`: Množství prostředků RGB, které mají být přiděleny kanálu ;
- `asset_id` : Jedinečný identifikátor aktiva RGB zapojeného do kanálu;
- `public`: Uvádí, zda má být kanál veřejný pro směrování v síti.

![RGB-Bitcoin](assets/fr/111.webp)

K potvrzení transakce je vytěženo 6 bloků:

```bash
./regtest.sh mine 6
```

![RGB-Bitcoin](assets/fr/112.webp)

Kanál Lightning je nyní otevřen a obsahuje také 500 tokenů `PBN` na straně uzlu č. 1. Pokud chce uzel č. 2 obdržet tokeny `PBN`, musí vygenerovat fakturu. Zde je návod, jak to udělat:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```

S :


- `amt_msat`: (minimálně 3000 sats) ;
- `expiry_sec` : Doba platnosti faktury v sekundách ;
- `asset_id` : Identifikátor aktiva RGB přiřazeného k faktuře ;
- `asset_amount`: Částka aktiva RGB, která má být převedena s touto fakturou.

V reakci na to se zobrazí faktura RGB (jak je popsáno v předchozích kapitolách):

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RGB-Bitcoin](assets/fr/113.webp)

Tuto fakturu nyní zaplatíme z prvního uzlu, který má potřebnou hotovost s tokenem `PBN`:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```

![RGB-Bitcoin](assets/fr/114.webp)

Platba byla provedena. To lze ověřit provedením příkazu :

```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```

![RGB-Bitcoin](assets/fr/115.webp)

Zde se dozvíte, jak nasadit uzel Lightning upravený pro přenos prostředků RGB. Tato ukázka je založena na :


- Prostředí regtest (přes `./regtest.sh`) nebo testnet ;
- Uzel Lightning (`rgb-lightning-node`) založený na `bitcoind`, indexeru a `rgb-proxy-serveru` ;
- Řada rozhraní JSON REST API pro otevírání/uzavírání kanálů, vydávání tokenů, přenos aktiv prostřednictvím služby Lightning atd.

Díky tomuto procesu :


- Transakce Lightning engagement zahrnují další výstup (OP_RETURN nebo Taproot) s ukotvením přechodu RGB;
- Převody se provádějí úplně stejným způsobem jako tradiční platby Lightning, ale s přidáním tokenu RGB;
- Více uzlů RLN může být propojeno, aby bylo možné směrovat a experimentovat s platbami napříč více uzly, pokud je na cestě dostatečná likvidita jak v bitcoinech, tak v aktivech RGB.

Projekt zůstává ve fázi alfa. Proto se důrazně doporučuje omezit se na testovací prostředí (regtest, testnet).

Možnosti, které se díky této kompatibilitě LN-RGB otevírají, jsou značné: stablecoiny na Lightningu, DEX layer-2, převod zastupitelných tokenů nebo NFT za velmi nízké náklady... V předchozích kapitolách byla nastíněna koncepční architektura a logika ověřování. Nyní máte praktický pohled na to, jak takový uzel zprovoznit, pro váš budoucí vývoj nebo testy.

# Závěr

<partId>b0baebfc-d146-5938-849a-f835fafb386f</partId>

## Recenze a hodnocení

<chapterId>0217e8b0-942a-5fee-bd91-9a866551eff3</chapterId>

<isCourseReview>pravdivé</isCourseReview>

## Závěr

<chapterId>0309536d-c336-56a0-869e-a8395ed8d9ae</chapterId>

<isCourseConclusion>true</isCourseConclusion>
