---
name: 1ML
description: Naučte se používat průzkumníka 1ML k pochopení a analýze sítě Lightning Bitcoin.
---
![cover](assets/cover.webp)



## Úvod



Lightning Network je rychlé a levné platební řešení postavené nad Bitcoin, které umožňuje okamžité a bezpečné transakce. Pozorování této sítě je nezbytné pro pochopení jejího fungování, topologie a stavu uzlů, které ji tvoří. K vizualizaci veřejných dat sítě, včetně aktivních uzlů, otevřených kanálů a dostupné kapacity, slouží průzkumník Lightning, jako je 1ML, který poskytuje cenný přehled uživatelům, vývojářům a provozovatelům uzlů.



## Přístup k 1ML a pochopení domovské stránky



Chcete-li získat přístup k 1ML, otevřete webový prohlížeč a zadejte [https://1ml.com](https://1ml.com). Tím se dostanete na domovskou stránku, která slouží jako globální ovládací panel Lightning Network.



![capture](assets/fr/03.webp)



Na této stránce se v horní části obrazovky zobrazuje několik důležitých statistik, včetně :





- **Celkový počet aktivních uzlů** v síti, tj. počítačů zapojených do odesílání a přijímání bleskových plateb.
- **počet otevřených kanálů**, které odpovídají spojením mezi těmito uzly umožňujícím převody finančních prostředků.
- Celková kapacita sítě** vyjádřená v bitcoinech (BTC), která udává součet kapacit všech veřejných kanálů.



Tyto údaje jsou pravidelně aktualizovány, aby odrážely aktuální stav sítě. Poskytují představu o její velikosti, růstu a robustnosti.



![capture](assets/fr/04.webp)



Hned pod tím stránka nabízí seznamy s pořadím:





- **nejvíce připojené uzly**, které mají nejvíce otevřených kanálů k ostatním uzlům.
- **nejvyšší kapacity** uzlů, které udávají, které uzly mohou přenášet největší množství dat.
- Nejdůležitější kanály z hlediska kapacity.



Tyto seznamy lze také pomocí filtrů zpřesnit podle zeměpisné polohy nebo jiných kritérií.



Tato stránka je ideálním výchozím bodem pro zkoumání Lightning Network a pochopení jeho obecné topologie.



![capture](assets/fr/05.webp)



![capture](assets/fr/06.webp)



## Zkoumání uzlů Lightning



Chcete-li prozkoumat uzel na 1ML, začněte pomocí vyhledávacího řádku v horní části stránky. Můžete zadat **ID uzlu**, tj. jedinečný identifikátor uzlu, nebo jeho **alias**, což je snadněji zapamatovatelný název.



Po dokončení vyhledávání se kliknutím na příslušný uzel dostanete na jeho podrobnou stránku.



![capture](assets/fr/07.webp)



Na této stránce se zobrazuje několik důležitých informací:





- ID uzlu**: tento jedinečný identifikátor je dlouhý řetězec znaků, který umožňuje přesnou identifikaci uzlu v celé síti.



![capture](assets/fr/08.webp)





- Alias**: jedná se o název zvolený vlastníkem uzlu, který jej bude veřejně reprezentovat.



![capture](assets/fr/09.webp)





- **Počet kanálů** udává, kolik spojení má uzel otevřených s jinými uzly, zatímco **celková kapacita** představuje součet bitcoinů dostupných v těchto kanálech. Uzel s velkým počtem kanálů a vysokou kapacitou je obecně dobře propojen a je schopen rychle převádět velké množství peněz v síti.



![capture](assets/fr/10.webp)





- Doba dostupnosti** neboli dostupnost udává, jak dlouho je uzel aktivní a dostupný online, což odráží jeho spolehlivost. Stáří** uzlu naproti tomu udává, jak dlouho je uzel v síti přítomen, což odráží jeho stabilitu a zkušenosti v rámci Lightning Network.



![capture](assets/fr/11.webp)



Tyto údaje vám pomohou pochopit význam a spolehlivost uzlu v systému Lightning Network. Například uzel s velkým počtem kanálů, vysokou kapacitou a vysokou dobou provozuschopnosti je často významným hráčem v síti.



## Zkoumání bleskových kanálů



### Co je to kanál Lightning?



Kanál Lightning je přímé spojení mezi dvěma uzly sítě. Umožňuje těmto dvěma uzlům vyměňovat si okamžité a levné platby, aniž by každá transakce musela procházet hlavním řetězcem Bitcoin. Kanály jsou základem, díky němuž je Lightning Network rychlý a škálovatelný.



### Přečtěte si informace o kanálu 1ML



V aplikaci 1ML má každý kanál svou vlastní stránku nebo popisný list, který obsahuje řadu důležitých údajů:



Na stránce uzlu můžete zobrazit seznam jeho kanálů. Po kliknutí na kanál zobrazí 1ML speciální stránku s několika klíčovými informacemi.



![capture](assets/fr/12.webp)



![capture](assets/fr/13.webp)



Hlavní viditelné údaje jsou následující:





- Partnerské uzly**: každý kanál spojuje dva uzly. 1ML zobrazuje oba identifikátory a jejich příslušné aliasy.



![capture](assets/fr/14.webp)





- Kapacita kanálu**: jedná se o celkové množství bitcoinů uzamčených v tomto kanálu. Tato kapacita představuje maximální limit plateb, které mohou tímto kanálem projít.



![capture](assets/fr/15.webp)





- Stáří kanálu**: udává, jak dlouho je kanál otevřený. Starý kanál je často známkou stabilního vztahu mezi dvěma uzly.



![capture](assets/fr/16.webp)



### Omezení viditelnosti kanálu



Je důležité si uvědomit, že 1ML zobrazuje pouze **část** Lightning Network. Průzkumník zobrazuje pouze **veřejné kanály**, tj. ty, které byly oznámeny v síti. Soukromé kanály, často používané z důvodů utajení nebo strategie, vidět nejsou. Kromě toho 1ML nezobrazuje přesné rozložení prostředků na jednotlivých stranách kanálu, ani provedené platby, ani likviditu, která je v daném okamžiku skutečně k dispozici. Zobrazené informace lze tedy použít k analýze **obecné struktury sítě**, nikoli však její skutečné finanční aktivity nebo podrobného stavu likvidity.



## Prozkoumat Lightning Network podle umístění



### Uzly podle zemí a regionů



1ML umožňuje prozkoumat Lightning Network podle **geografického členění**. Na domovské stránce nebo ve vyhrazených sekcích je možné zobrazit uzly podle zemí nebo regionů. Tato funkce je založena na informacích o poloze deklarovaných provozovateli uzlů.


Na navigačním panelu se zobrazí odkaz **Lokalita**. Na stránce jsou uzly seskupeny podle kontinentů, zemí a měst.



![capture](assets/fr/17.webp)



Výběrem země zobrazí 1ML seznam přidružených uzlů spolu s agregovanými statistikami, jako je počet uzlů a celková viditelná kapacita pro danou zeměpisnou oblast.



#### Co to říká o místní adopci





- Přijetí technologie**: Velký počet uzlů v regionu naznačuje, že uživatelé, společnosti nebo služby aktivně zavádějí Bitcoin. To svědčí o technologické vyspělosti a ochotě využívat výhod technologie Lightning (rychlé transakce, nižší náklady).
- Ekonomický ekosystém** : Hustá přítomnost uzlů může také signalizovat místní ekonomickou strukturu kolem Bitcoin: obchodníci přijímající Blesk, startupy vyvíjející nástroje, komunitní akce atd.
- Bezpečnost a odolnost**: Různorodé geografické rozložení zvyšuje odolnost sítě v případě lokálních výpadků nebo omezení. Čím více jsou uzly rozptýlené, tím je síť decentralizovanější a obtížněji cenzurovatelná.
- Zásady a předpisy**: V některých zemích může dojít k rychlejšímu přijetí díky příznivému regulačnímu rámci nebo proaktivní komunitě. Naopak v oblastech, kde jsou předpisy přísné nebo nepřátelské, bude počet uzlů nižší.



#### Limity geografických údajů



Mějte však na paměti, že geolokace uzlů Lightning má své limity a zkreslení:





- Přibližné umístění IP**: 1ML obecně používá veřejnou IP adresu uzlů k odhadu jejich polohy. Tato metoda však může být zkreslena používáním VPN, cloudových serverů (AWS, Google Cloud) nebo hostováním v jiných zemích, než je skutečné bydliště vlastníka uzlu.
- Virtuální uzly**: Někteří provozovatelé hostují své uzly na vzdálených serverech z důvodu spolehlivosti a dostupnosti, což může vyvolávat falešný pocit fyzické polohy.
- Mobilita uživatele**: Provozovatel uzlu může změnit místo, přesunout svou infrastrukturu nebo otevřít několik uzlů v různých regionech, což komplikuje čtení dat.
- Neviditelnost soukromých uzlů**: Některé uzly nezveřejňují svou IP adresu nebo používají metody pro skrytí své polohy, což znemožňuje geolokaci.



## konkrétní případy použití 1ML



### Porozumění topologii sítě



1ML umožňuje vizualizovat **obecnou strukturu Lightning Network**. Sledováním spojení mezi uzly, počtu kanálů a celkové kapacity je možné pochopit, jak je síť uspořádána, které uzly hrají ústřední roli a jak mohou teoreticky obíhat platební toky.



Toto porozumění je nezbytné, pokud chceme pochopit, jak Lightning Network funguje, a to nejen pro použití v portfoliu.



### Identifikace důležitých uzlů



Díky žebříčkům, které nabízí 1ML (nejvíce připojených uzlů, nejvyšší kapacita, stáří), je možné identifikovat uzly, které v síti zaujímají důležité místo. Tyto uzly často slouží jako hlavní brány pro bleskové platby.



![capture](assets/fr/18.webp)



### Kontrola veřejné viditelnosti uzlu



Provozovateli uzlu umožňuje 1ML zkontrolovat, zda je jeho uzel **veřejně inzerován** v systému Lightning Network. Pokud se uzel objeví na 1ML, znamená to, že je viditelný a přístupný ostatním uzlům pro otevření veřejných kanálů.


To může být užitečné při diagnostice problémů s viditelností nebo připojením.



### Sledování vývoje Lightning Network v průběhu času



Porovnáním globálních statistik za různá období nám 1ML umožňuje sledovat vývoj Lightning Network: nárůst nebo pokles počtu uzlů, změny celkové kapacity nebo změny v geografickém rozložení.


Tato pozorování nabízejí zajímavý pohled na růst, zralost a trendy Lightning Network.



## osvědčené postupy a omezení 1ML



### Veřejná data ≠ kompletní realita



1ML vychází pouze z **veřejně oznámených** údajů o Lightning Network. To znamená, že nástroj zobrazuje pouze část skutečnosti. Mnoho kanálů může být neveřejných, některé uzly nemusí být inzerovány a skutečná likvidita dostupná v kanálech není vidět. Je proto nezbytné používat 1ML jako nástroj pro globální analýzu, nikoli jako vyčerpávající zobrazení sítě.



### Soukromí a blesk



Lightning Network byl navržen s důrazem na **soukromí plateb**. Jednotlivé transakce nejsou na 1ML viditelné a přesné zůstatky na kanálech nejsou veřejné. Toto omezení není chybou průzkumníka, ale základní vlastností Lightning Network, která má chránit soukromí uživatelů.



### Nedělejte ukvapené závěry



Uzel s vysokou kapacitou nebo mnoha kanály nemusí být nutně ve všech případech "spolehlivější" nebo "efektivnější". Stejně tak dočasný pokles celkové kapacity sítě nemusí nutně znamenat strukturální problém. Číselné údaje je třeba vždy interpretovat s odstupem času a uvádět je do souvislostí.



### Doplňkovost s ostatními nástroji



1ML je vynikajícím výchozím bodem pro zkoumání Lightning Network, ale nejlépe se používá ve spojení s dalšími nástroji, jako jsou portfolia Lightning, rozhraní pro správu uzlů a další průzkumníci. Tento přístup poskytuje úplnější a diferencovanější pohled na síť.



## možnost připojení 1ML (pokročilé funkce)



společnost 1ML nabízí možnost **přihlášení / vytvoření účtu**, která je na stránkách viditelná, ale pro zobrazení údajů Lightning Network není **nutná**. Všechny funkce, o kterých bylo dosud v tomto návodu pojednáno, jsou k dispozici **bez účtu**.



Připojení je určeno především **provozovatelům bleskových uzlů**. Umožňuje zejména propojení uzlu s účtem 1ML za účelem správy některých veřejných informací, jako je prezentace uzlu, kontaktní odkazy a další metadata. Tato funkce má zlepšit viditelnost a identifikaci uzlu v rámci průzkumníka.



Je důležité si uvědomit, že 1ML není **pečovatelská služba**. Vytvoření účtu neumožňuje přístup k finančním prostředkům, kanálům nebo platbám uzlu. Slouží pouze k interakci s průzkumníkem z deklarativního a informačního hlediska.



V kontextu učení nebo objevování Lightning Network lze proto tuto možnost považovat za **volitelnou** a vyhrazenou pro pokročilejší použití.



## Závěr



1ML je cenným nástrojem pro pozorování a pochopení Lightning Network z jeho veřejných dat. Umožňuje zkoumat strukturu sítě, analyzovat uzly a kanály a sledovat celkový vývoj přijetí Lightning Network v čase. Bez nutnosti mít účet nebo nakládat s finančními prostředky nabízí 1ML přístupnou bránu pro každého, kdo chce prohloubit své porozumění fungování blesku.


Pokud se chcete s Lightning Network dostat dále, doporučuji kompletní kurz Úvod do Lightning Network:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb