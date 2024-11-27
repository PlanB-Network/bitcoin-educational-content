---
name: Úvod do těžby Bitcoinu
goal: Porozumět fungování těžebního průmyslu prostřednictvím praktického cvičení s opětovným využitím ASICů.
objectives:
  - Porozumět teorii za těžbou
  - Porozumět těžebnímu průmyslu
  - Přeměnit S9 na topení
  - Vytěžit svůj první satoshi
---

# Vaše první kroky v těžbě!

V tomto školení se ponoříme do těžebního průmyslu, abychom odhalili složitost tohoto tématu! Školení je přístupné všem a nevyžaduje žádnou počáteční investici.

První část bude teoretická, kde Ajelex a já budeme mít podrobnou diskusi na různá témata související s těžbou. To nám pomůže lépe porozumět tomuto průmyslu a ekonomickým a geopolitickým otázkám s ním spojeným.
Ve druhé části se zaměříme na praktický případ. Skutečně se naučíme, jak přeměnit použitý těžař S9 na domácí topení! Prostřednictvím psaných průvodců a videí vám ukážeme a vysvětlíme všechny kroky, jak toho dosáhnout u vás doma :)

Prostřednictvím tohoto videa doufáme, že vám ukážeme, že těžební průmysl je složitější, než se zdá, a jeho studium pomáhá nuancovat ekologickou debatu, která je s ním spojena!
Pokud potřebujete pomoc se svým nastavením, pro studenty byla vytvořena skupina na Telegramu a všechny potřebné komponenty lze najít na naší e-commerce platformě!

+++

# Úvod

<partId>a99dc130-3650-563f-8d42-a0b5160af0ab</partId>

## Vítejte!

<chapterId>7ad1abeb-a190-5c85-8bff-44df71331e4d</chapterId>

Vítejte na MINING 201: úvod do těžby. Ajelex, Jim & Rogzy se těší, že vás budou doprovázet ve vašich prvních konkrétních krocích v tomto novém průmyslu. Doufáme, že si kurz užijete a připojíte se k dobrodružství domácí těžby!

### Přehled kurzu

V první části kurzu se zaměříme na teorii těžby s Ajelexem. Budeme mít podrobné diskuse na různá témata související s těžbou, což nám pomůže lépe porozumět tomuto průmyslu a ekonomickým a geopolitickým otázkám s ním spojeným.

Ve druhé části se pustíme do fascinujícího praktického případu, kdy se naučíme, jak přeměnit použitý těžař S9 na domácí topení. Prostřednictvím psaných průvodců a videí budou všechny nezbytné kroky pečlivě vysvětleny, což zajistí váš úspěch v tomto inovativním projektu.

Tato vzdělávací cesta vám ukáže, že těžební průmysl je složitější, než se zdá, a nabídne vyvážený pohled na ekologickou debatu s ním spojenou. Během kurzu bude k dispozici pokračující pomoc prostřednictvím věnované skupiny na Telegramu pro studenty, a všechny potřebné komponenty budou snadno dostupné na naší e-commerce platformě.

### Učební plán:

Teoretická část:

- Vysvětlení těžby.
- Těžební průmysl.
- Nuance těžebního průmyslu.
- Těžba v protokolu Bitcoinu.
- Cena Bitcoinu a Hashrate, korelace? Suverenita a regulace
- Rozhovor s profesionálem z těžebního průmyslu

Praktická část: Attakai

- Úvod do Attakai.
- Nákupní průvodce.
- Úprava softwaru Antmineru S9.
- Výměna ventilátorů pro snížení hluku.
- Konfigurace poolu.
- Konfigurace Antmineru S9 s Braiins OS+.

Jste připraveni vstoupit do této poutavé dobrodružství? Pojďme se společně ponořit do fascinujícího světa domácí těžby!

# Vše, co potřebujete vědět o těžbě

<partId>aa99ef2c-da29-5317-a533-2ffa4f66f674</partId>

## Vysvětlení těžby

<chapterId>36a82de7-87ee-5e7a-b69e-48fc30030447</chapterId>

### Vysvětlení těžby: Analogie s puzzle

Pro zjednodušené vysvětlení konceptu těžby lze použít příhodnou analogii: puzzle. Stejně jako puzzle, těžba je složitý úkol, který je ovšem snadno ověřitelný po jeho dokončení. V kontextu těžby Bitcoinu se těžaři snaží rychle vyřešit digitální puzzle. První těžař, který puzzle vyřeší, prezentuje své řešení celé síti, která poté snadno ověří jeho platnost. Toto úspěšné ověření umožňuje těžaři validovat nový blok a přidat ho do Bitcoinového časového řetězce. Jako uznání za jejich práci, která zahrnuje významné náklady, je těžař odměněn určitým počtem bitcoinů. Tato odměna slouží jako finanční pobídka pro těžaře, aby pokračovali ve své práci validace transakcí a zabezpečení Bitcoinové sítě.

![image](assets/en/01.webp)

Původně v Bitcoinové síti byla odměna za nalezení bloku 50 bitcoinů každých deset minut, paralelně s objevováním bloku těžaři průměrně každých deset minut. Tato odměna prochází halvingem každých 210 000 bloků, přibližně každé čtyři roky. Tato odměna slouží jako silná motivace pro těžaře, aby se zapojili do procesu těžby navzdory jejím energetickým nákladům. Bez odměny by energeticky náročná těžba byla opuštěna, což by ohrozilo bezpečnost a stabilitu celé Bitcoinové sítě.
Současná těžební odměna je dvojí. Na jedné straně zahrnuje vytváření nových bitcoinů, které se snížilo z původních 50 bitcoinů každých deset minut na dnešních 6,25 bitcoinu (2023). Na druhé straně zahrnuje transakční poplatky, neboli těžební poplatky, z transakcí, které si těžař vybere pro zařazení do svého bloku. Když je provedena bitcoinová transakce, jsou zaplaceny transakční poplatky. Tyto poplatky fungují jako druh aukce, kde uživatelé udávají, kolik jsou ochotni zaplatit za zařazení své transakce do dalšího bloku. Těžaři, jednající ve svém vlastním zájmu, si proto vybírají nejvýnosnější transakce pro zařazení do svého bloku s ohledem na omezený dostupný prostor. Takto těžební odměna zahrnuje jak generování nových bitcoinů, tak transakční poplatky, čímž zajišťuje nepřetržitou motivaci pro těžaře a zajišťuje dlouhověkost a bezpečnost Bitcoinové sítě.

### Těžaři a jejich nástroje: Těžba

Proces těžby zahrnuje nalezení platného hash, který je přijatelný pro Bitcoinovou síť. Jakmile je tento hash vypočítán a nalezen, je nevratný, podobně jako když jsou brambory proměněny na bramborovou kaši. Ověřuje určitou funkci bez možnosti návratu. Těžaři, soutěžící mezi sebou, používají stroje k výpočtu těchto hashů. Ačkoli je teoreticky možné tento hash najít ručně, složitost operace činí tuto možnost neproveditelnou. Proto jsou používány počítače, schopné provádět tyto výpočty rychle, přičemž spotřebovávají významné množství elektřiny.

Na začátku dominovala éra CPU, kdy těžaři používali své osobní počítače pro těžbu Bitcoinu. Objev výhod GPU (grafických karet) pro tuto úlohu znamenal zlom, výrazně zvýšil hashrate a snížil spotřebu energie. Pokrok zde ale neskončil, následovalo zavedení FPGA (programovatelných hradlových polí). FPGA sloužily jako platforma pro vývoj ASIC (aplikačně specifických integrovaných obvodů).

![image](assets/en/02.webp)

ASIC jsou čipy, srovnatelné s čipem CPU, nicméně jsou vyvinuty k provádění pouze jednoho konkrétního typu výpočtu co nejefektivnějším způsobem. Jinými slovy, CPU je schopno provádět mnoho různých typů výpočtů, aniž by bylo zvláště optimalizováno pro jeden konkrétní typ výpočtu, zatímco ASIC bude schopno provádět pouze jeden typ výpočtu, ale velmi efektivně. V případě Bitcoin ASIC jsou tyto čipy navrženy pro výpočet algoritmu SHA256. Dnes již těžaři výhradně používají ASIC určené pro tuto operaci, optimalizované tak, aby testovaly maximální počet kombinací s co nejmenší spotřebou energie a co nejrychleji. Tyto počítače, neschopné provádět jiné úkoly než těžbu Bitcoinu, jsou hmatatelným svědectvím neustálého vývoje a rostoucí specializace průmyslu těžby Bitcoinu. Tento neustálý vývoj odráží vnitřní dynamiku Bitcoinu, kde úprava obtížnosti zajišťuje produkci bloku každých deset minut navzdory exponenciálnímu nárůstu těžební kapacity.

Pro ilustraci intenzity tohoto procesu si vezměte typického těžaře schopného dosáhnout 14 TeraHash za sekundu, neboli 14 bilionů pokusů každou sekundu najít správný hash. Na úrovni sítě Bitcoinu dosahujeme nyní přibližně 300 HexaHash za sekundu, což zdůrazňuje kolektivní sílu mobilizovanou v těžbě Bitcoinu.

### Úprava obtížnosti:

Úprava obtížnosti je klíčovým mechanismem v provozu sítě Bitcoin, který zajišťuje, že bloky jsou těženy v průměru každých 10 minut. Toto trvání je průměrem, protože proces těžby je ve skutečnosti hrou pravděpodobnosti, podobně jako házení kostkami v naději, že padne číslo nižší než číslo definované obtížností. Každých 2016 bloků síť upravuje obtížnost těžby na základě průměrného času potřebného k těžbě předchozích bloků. Pokud je průměrný čas větší než 10 minut, obtížnost se sníží, a naopak, pokud je průměrný čas nižší, obtížnost se zvýší. Tento mechanismus úpravy zajišťuje, že čas těžby nových bloků zůstává konstantní v čase, bez ohledu na počet těžařů nebo celkový výpočetní výkon sítě. To je důvod, proč se Bitcoin Blockchain nazývá také Timechain.

![obrázek](assets/en/03.webp)

- Příklad z Číny:
  Případ Číny dokonale ilustruje tento mechanismus úpravy obtížnosti. S hojnou a levnou energií byla Čína hlavním globálním centrem pro těžbu Bitcoinu. V roce 2021 země náhle zakázala těžbu Bitcoinu na svém území, což vedlo k masivnímu poklesu celosvětového hashrate sítě Bitcoin, asi o 50%. Tento rychlý pokles těžební síly mohl vážně narušit síť Bitcoin tím, že by zvýšil průměrný čas těžby bloků. Avšak mechanismus úpravy obtížnosti zasáhl, snížil obtížnost těžby, aby zajistil, že frekvence těžby bloků zůstane v průměru 10 minut. Tento případ demonstruje efektivitu a odolnost mechanismu úpravy obtížnosti Bitcoinu, který zajišťuje stabilitu a předvídatelnost sítě, i v případě náhlých a významných změn v globální krajině těžby.

### Vývoj strojů pro těžbu Bitcoinu

Pokud jde o vývoj strojů pro těžbu Bitcoinu, je důležité poznamenat, že kontext je více orientován směrem k tradičnímu obchodnímu modelu. Těžaři vydělávají svůj příjem z validace bloků, úkolu s relativně nízkou pravděpodobností úspěchu. Současný model v použití, Antminer S9, ačkoli je starší model spuštěný kolem roku 2016, je stále v oběhu na trhu s použitými, obchoduje se za přibližně 100 až 200 €. Cena těžebních strojů se nicméně liší na základě hodnoty Bitcoinu, a novější model, Antminer S19, je v současné době odhadován na přibližně 3000 €.
V oblasti těžby se odborníci musí strategicky pozicovat vzhledem k neustálému technologickému pokroku. Těžební průmysl je předmětem neustálých inovací, jak dokládá nedávné uvedení verze J modelu S19 a očekávané uvedení modelu S19 XP, které nabízí výrazně vyšší těžební schopnosti. Navíc se zlepšení netýkají pouze surového výkonu strojů. Například nový model S19 XP používá systém kapalinového chlazení, technickou úpravu, která umožňuje významné zlepšení energetické účinnosti. Ačkoli inovace zůstávají konstantní, budoucí zisky v účinnosti budou pravděpodobně menší ve srovnání s dosud pozorovanými, kvůli dosažení určitého prahu technologické inovace.

![image](assets/en/04.webp)

Závěrem, průmysl těžby Bitcoinu pokračuje v adaptaci a rozvoji, a hráči v průmyslu musí očekávat snižující se zisky v účinnosti do budoucna a přizpůsobit své strategie podle toho. Budoucí technologické pokroky, ačkoli stále přítomné, pravděpodobně nastanou na menší škále, což odráží rostoucí zralost sektoru.

## Těžební průmysl

<chapterId>0896dfc1-c97e-5bec-9bf1-8c20b3388a2c</chapterId>

### Těžební pooly

V současnosti se těžba Bitcoinu vyvinula v vážný a rozsáhlý průmysl, s mnoha veřejně známými hráči a stále větším počtem významných těžařů. Tento vývoj učinil těžbu téměř nedostupnou pro malé hráče kvůli vysokým nákladům spojeným s pořízením nových těžebních strojů. To vyvolává otázku distribuce hashrate mezi různé tržní hráče. Situace je složitá, protože je nezbytné zkoumat jak distribuci hashrate mezi různými společnostmi, tak mezi různými těžebními pooly.

![image](assets/en/05.webp)

Těžební pool je skupina těžařů, kteří kombinují své výpočetní zdroje, aby zvýšili své šance na těžbu. Tato spolupráce je nutná, protože izolovaný malý těžební stroj soutěží s průmyslovými giganty, čímž se jeho šance na úspěch snižují na zanedbatelnou úroveň. Těžba funguje na principu loterie, a šance na vyhrání bloku (a tedy odměny v Bitcoinech) každých deset minut jsou pro jednotlivého malého těžaře extrémně nízké. Spojením sil mohou těžaři kombinovat svůj výpočetní výkon, častěji nalézat bloky a poté rozdělovat odměny proporcionálně k příspěvku každého těžaře do poolu.

Například, pokud pool najde blok a vyhraje 6.25 bitcoinů, těžař přispívající 1% celkového výpočetního výkonu poolu by obdržel 1% z 6.25 bitcoinů. Je třeba poznamenat, že těžební pooly obvykle berou malou provizi (obvykle kolem 2%) na pokrytí provozních nákladů spolupráce.

### Software používaný průmyslem

V kontextu těžby Bitcoinu je role softwaru stejně důležitá jako hardware. Příkladem toho je role společnosti Bitmain, významného výrobce, který vyvinul Antminer S9. Kromě těžebního hardwaru se průmysl silně spoléhá na kolaborativní těžební pooly, jako je Brainspool, který kontroluje přibližně 5% celosvětového hashrate Bitcoinové sítě.
Akteři v tomto průmyslu neustále usilují o zvýšení účinnosti prostřednictvím hardwaru a softwaru. Například populární software používaný v tomto kontextu je BrainsOS Plus. Tento software nahrazuje původní operační systém těžebního stroje, což umožňuje provádět stejné operace efektivněji. S takovým softwarem může těžař zvýšit účinnost svého stroje o 25%. To znamená, že za stejné množství elektřiny může stroj produkovat dalších 25% hashrate, čímž zvyšuje odměny přijímané těžařem. Tato optimalizace softwaru je zásadním prvkem konkurenceschopnosti v těžbě Bitcoinu, což ukazuje důležitost integrovaného přístupu, který kombinuje zlepšení hardwaru i softwaru, aby maximalizoval účinnost a výnosy.

### Regulace a Elektrické Tarify

Jak bylo pozorováno v Číně a jinde, regulace má významný vliv na těžbu. Ačkoliv ve Francii nejsou žádní významní těžaři, regulace a vysoké elektrické tarify v Evropě představují hlavní překážky. Těžaři neustále hledají elektrickou energii za nízké ceny, aby maximalizovali své zisky. Proto vysoké náklady na elektrickou energii v Evropě a ve Francii nepřitahují těžaře do těchto regionů.

Těžaři mají tendenci gravitovat k regionům s nízkými elektrickými tarify, často v rozvíjejících se zemích nebo zemích s energetickými přebytky. Například velká část globálního hashrate se nachází v Texasu, ve Spojených státech. Texas má nezávislou energetickou síť, která nesdílí své energetické zdroje s ostatními státy. Tato jedinečnost často vede Texas k tomu, že produkuje více elektrické energie, než je nutné, aby se vyhnul nedostatkům, čímž vytváří přebytek. Bitcoinoví těžaři využívají této nadprodukce tím, že zřizují operace v Texasu, kde mohou těžit bitcoiny za velmi nízké elektrické sazby během období energetického přebytku. Tato situace ukazuje významný vliv regulací a elektrických tarifů na těžbu Bitcoinu, zdůrazňující důležitost těchto faktorů v rozhodování těžařů o umístění jejich těžebních operací.

### Kam těžaři směřují a řízení energie?

Zdůrazněním dopadu bitcoinových těžařů na svět energie je jasné: tito aktéři neustále hledají zdroje levné elektrické energie, často ty, které jsou plýtvány nebo nevyužité. Tento jev je zřejmý v regionech s novou elektrickou infrastrukturou, jako jsou ty vybavené nedávnými hydroelektrárnami.

Pojďme uvést příklad. V zemi, která je v procesu stavby přehrady, často začíná výroba elektrické energie dříve, než jsou plně provozuschopné distribuční linky. Tato časová mezera může vést k významným nákladům a odrazovat od investic do takových infrastrukturních projektů. Bitcoinoví těžaři však mohou působit jako flexibilní zdroj poptávky, připraveni spotřebovat tuto "opuštěnou" elektrickou energii, čímž pomáhají kompenzovat náklady na infrastrukturu. Implikace zde je, že nové instalace mohou být okamžitě ziskové, podporující vytváření nových zdrojů elektrické energie. Tento princip platí i v menším měřítku. Ať už jde o jednotlivce používajícího hydroelektrický generátor na malé řece nebo domácnost vybavenou solárními panely, přebytečná vyrobená elektrická energie může být využita k napájení bitcoinových těžebních operací.

Ve Francii, například, je přebytečná elektrická energie z solárních panelů injektována zpět do sítě a producenti jsou kompenzováni kreditem na spotřebu od EDF. Podobně si lze představit těžaře, který provozuje na této přebytečné elektrické energii, vypínající se, když místní poptávka rovná se nabídce. Ačkoliv se to může jevit sobecky, prioritizace produkce bitcoinů nad podporou místní energetické sítě, představuje to další úhel pohledu: stabilizaci energetické sítě. Složité řízení přebytečné elektrické energie, někdy i s přidruženými náklady na likvidaci, může být výrazně zjednodušeno. Bitcoinoví těžaři mohou absorbovat tyto přebytky, působí jako flexibilní tlumič, upravující poptávku spíše než nabídku. Ve světě, kde produkce elektrické energie z obnovitelných (nekontrolovatelných) zdrojů neustále roste, mohou těžaři hrát klíčovou roli v zajištění rovnováhy našich energetických sítí, zatímco těží z levné nebo přebytečné elektrické energie pro své těžební operace.

### Centralizace Těžby

Centralizace těžby je adresována jako hlavní výzva. Velcí hráči, jako je Foundry, dominují trhu, což může potenciálně vést k cenzuře transakcí. Tato centralizace také může způsobit, že síť bude zranitelná vůči útokům, včetně útoku 51%, kdy aktér nebo skupina kontroluje více než 50% výpočetní síly sítě, což jim umožňuje kontrolovat a manipulovat se sítí.

Riziko Regulace Je zdůrazněno, že pokud by země jako Spojené státy rozhodly regulovat nebo zakázat určité Bitcoinové transakce, mohlo by to mít významný dopad na síť, zejména pokud je velká část výpočetní síly centralizována v této zemi.

![obrázek](assets/en/06.webp)

Pro boj s touto centralizací jsou diskutovány různé strategie:

- Domácí těžba: Myšlenka domácí těžby je založena na decentralizaci těžební činnosti. Podporuje jednotlivce, aby se zapojili do těžby ze svých domovů, čímž se distribuce hashrate rozšiřuje.
- Stratum V2: Protokol Stratum V2 nabízí jiný přístup. Na rozdíl od svého předchůdce umožňuje Stratum V2 těžařům vybírat, které transakce zahrnou do bloků, které těží. Tato schopnost posiluje odolnost vůči cenzuře a snižuje schopnost velkých těžebních poolů dominovat v síti. Dáváním větší moci jednotlivým těžařům může protokol Stratum V2 hrát rozhodující roli v boji proti centralizaci hashrate.
  Otevření zdrojového kódu těžebního softwaru
- Otevření zdrojového kódu těžebního softwaru: Toto je další potenciálně účinná strategie. Tím, že se těžební software stane přístupným pro všechny, měli by malí těžaři stejné příležitosti jako velké těžební společnosti účastnit se a přispívat do blockchainové sítě. Tento přístup by podpořil širší distribuci hashrate, čímž by přispěl k decentralizaci sítě.
- Diverzifikace aktérů a geografie: Podpora účasti rozmanitých aktérů z různých geografických regionů v těžbě kryptoměn může být také účinná. Diverzifikací hashrate geograficky se stává obtížnější, aby jeden aktér nebo země vyvíjel nepřiměřenou kontrolu nebo vliv nad sítí. Tento přístup může pomoci chránit síť proti potenciálním útokům a posílit její decentralizaci.

Obecný závěr je, že decentralizace je klíčová pro bezpečnost a odolnost Bitcoinové sítě. Ačkoliv centralizace může nabídnout výhody v efektivitě, vystavuje síť významným rizikům, včetně cenzury a 51% útoků. Iniciativy jako Takai a přijetí nových protokolů jako Stratum V2 jsou důležitými kroky směrem k decentralizaci a ochraně Bitcoinové sítě proti těmto hrozbám.

## Nuance těžebního průmyslu

<chapterId>7b9ee427-316a-54e3-a2d4-4ea97839a31b</chapterId>

### Princip Attakai

V současném kontextu může těžba Bitcoinu pomocí modelu S9 působit složitě, ale hlubší analýza otevírá dveře k inovativním alternativám. Princip Attakai je založen na úvaze o využití těžebních zařízení v různých typech budov, jako jsou školy nebo nemocnice. Hlavní myšlenkou je rozmístit několik těžebních strojů na různá místa, což umožní znovu využít teplo vyzařované těmito stroji k vytápění budov. Pokud by se zvolily výkonnější modely, jako je S19, bylo by možné rozložit těžební činnost, čímž by se zlepšil celkový výkon a zároveň přispělo k užitečné činnosti pro společnost. Tato iniciativa si klade za cíl konkurovat velkým centralizovaným těžebním instalacím tím, že produktivně a efektivně využije teplo generované těžebními stroji.

Iniciativa Attakai vychází z osobního experimentu s domácí těžbou, který provedli dva přátelé toužící aktivně se zapojit do Bitcoinové sítě. Čelili velkým překážkám, jako je vysoká hladina hluku těžebního vybavení, které bylo navrženo pro průmyslové použití, nikoli pro domácí. Aby tento problém vyřešili, provedli na těžebních strojích hardwarové úpravy. Původní vybavení bylo nahrazeno účinnějšími a tiššími ventilátory, což učinilo domácí těžbu přístupnější a méně rušivou. Dále přidali Wi-Fi adaptér, což odstranilo potřebu kabelového připojení přes Ethernet a ještě více zjednodušilo proces domácí těžby. V zimě byly tyto upravené těžební stroje využívány jako zdroj tepla, což proměnilo nepříjemnost ve výhodu.

Po představení svého projektu Bitcoinové komunitě a vzhledem k zájmu, který vzbudil, se vynálezci Attakai rozhodli zveřejnit podrobné návody na platformě Découvre Bitcoin, aby kdokoliv mohl replikovat jejich zkušenost s domácí těžbou. Nyní plánují rozšířit tento koncept i mimo domácí prostředí. Cílem je ukázat, jak může být upravený těžební stroj přeměněn na tiché pomocné topidlo použitelné v zimě, a tím nabídnout plynulý přechod k druhé části školení zaměřené na praktickou realizaci těchto úprav, ilustrované vysvětlujícími videi. Otázkou však zůstává, zda lze tuto iniciativu rozšířit do většího měřítka, a tak nabídnout realistickou a udržitelnou alternativu k současným centralizovaným těžebním strukturám.

![image](assets/en/07.webp)

### Limit této decentralizace?

Ačkoliv myšlenka decentralizace těžby prostřednictvím produktivního využití generovaného tepla vypadá slibně, má určitá omezení a zůstávají otázky. Energeticky náročná zařízení jako sauny a bazény by mohla těžit z tohoto konceptu využitím tepla produkovaného těžaři k ohřevu vody ve svých zařízeních. Tuto praxi již implementují někteří členové Bitcoinové komunity, kteří prozkoumávají různé metody efektivního využití tepla generovaného těžebním zařízením. Například, banketní sál by teoreticky mohl být vytápěn třemi nebo čtyřmi těžaři S19, každý spotřebovávající 3000 wattů a produkující ekvivalentní množství tepla.

Je však třeba poznamenat, že spotřeba energie a produkce tepla jsou ekvivalentní, ať už je energie využívána elektrickým ohřívačem nebo těžařem. Na každý kilowatt použité elektřiny bude množství vyprodukovaného tepla stejné v obou případech. Rozdíl spočívá v tom, že těžař nejenže poskytuje teplo, ale také odměnu v bitcoinech, čímž nabízí ekonomický podnět k použití těžaře místo jednoduchého elektrického ohřívače. Tato dodatečná odměna by mohla pomoci zmírnit obavy z vysoké spotřeby energie těžaři.

Otázka dlouhodobé efektivity a proveditelnosti využívání bitcoinových těžařů pro vytápění zůstává otevřená. Pokračující inovace v hardwaru pro těžbu a technologiích vytápění mohou potenciálně otevřít nové cesty pro efektivnější využití tepla generovaného těžbou, čímž by přispěly k životaschopnosti tohoto přístupu v budoucnosti.

### Proč mít BTC odměny?

Otázka odměňování v bitcoinech namísto jiné měny je zásadní v systému, který představil Satoshi Nakamoto. Vytvoření Bitcoinu je charakterizováno pevným limitem 21 milionů jednotek. Cílem bylo najít spravedlivý způsob, jak distribuovat tyto nově vytvořené jednotky. Těžaři, poskytováním svého výpočetního výkonu k zabezpečení sítě a zvyšováním nákladů na jakýkoliv útok, efektivně chrání síť Bitcoinu. Jako odměnu za tento klíčový příspěvek jsou odměňováni nově vytvořenými bitcoiny, což usnadňuje distribuci mincí v rámci ekosystému.
Je to systém, ve kterém vyhrávají obě strany. Těžaři jsou odměňováni jak za zabezpečení sítě, tak za schvalování transakcí. Nově vytvořené bitcoiny jsou dávány jako pobídka k posílení bezpečnosti, a transakční poplatky jsou dalším příjmem za schválení transakcí. Tyto dva prvky dohromady tvoří celkovou odměnu za těžbu. Otázka budoucnosti těžby vzniká kvůli programovanému snižování odměn za těžbu, které se snižuje každé čtyři roky, událost známá jako "halving". Do roku 2032 bude odměna za blok menší než jeden bitcoin a do roku 2140 nebudou vytvořeny žádné nové bitcoiny. V tomto bodě se těžaři budou spoléhat výhradně na transakční poplatky jako na kompenzaci. Síť Bitcoinu bude muset podporovat velký počet transakcí s dostatečně vysokými poplatky, aby zajistila ziskovost těžby.

Růst Lightning Network, který umožňuje rychlé a nízkonákladové transakce mimo hlavní řetězec Bitcoinu, vyvolává otázky o budoucnosti těžby. Lightning Network má potenciál výrazně snížit transakční poplatky, čímž by mohl ovlivnit příjmy těžařů. To však bude záviset na přijetí a používání Lightning Network ve srovnání s hlavní sítí Bitcoinu. V pesimistickém scénáři mohou těžaři shledat těžbu ziskovou i při ztrátě, pokud si amortizovali své náklady a mají přístup k levné elektřině. V optimističtějším scénáři mohou transakční poplatky v hlavní síti Bitcoinu zůstat dostatečně vysoké, aby udržely ziskovost těžby.

### Co by mělo být zahrnuto v Bitcoinovém bloku?

Pokud jde o otázku, co by mělo být zahrnuto v bitcoinovém bloku, je klíčové zvážit doplňkovou povahu různých vrstev sítě Bitcoinu. Ačkoliv Lightning Network může umožnit rychlejší a levnější transakce, stále spoléhá na základní vrstvu Bitcoinu, často označovanou jako "settlement layer", pro otevírání a zavírání platebních kanálů.

S očekávaným růstem Lightning Network a následným zvýšením počtu otevírání a zavírání kanálů se stane prostor v bitcoinových blocích stále cennějším. Bitcoinová komunita již má tendenci hodnotit zachování tohoto prostoru, uznávajíc jeho vnitřní omezení. Toto povědomí vedlo k diskusím o legitimním využití prostoru v blocích, s obavami o "spam" na blockchainu z transakcí považovaných za neesenciální.

![image](assets/en/08.webp)

Spekulace obklopují budoucí využití prostoru v blocích, ale obecně je přijímáno, že je to vzácný zdroj, který by měl být moudře využíván. I když existuje touha jej naplnit, je zásadní jej zachovat, aby byla zajištěna dlouhodobá životaschopnost sítě Bitcoinu, s předvídáním budoucího nárůstu poptávky po prostoru v blocích. Jako na jakémkoliv volném trhu, nabídka a poptávka budou regulovat využití prostoru v blocích. S omezenou nabídkou budou muset zúčastněné strany činit informovaná rozhodnutí o využití tohoto cenného prostoru, aby zajistily dlouhodobou efektivitu a bezpečnost sítě Bitcoinu.

## Těžba Bitcoinu v protokolu Bitcoinu

<chapterId>879a66b0-c20a-56b5-aad0-8a21be61e338</chapterId>

![Kdo má moc? Bitcoin, energie a výrobci](https://www.youtube.com/watch?v=4wywK6BfDw8)
Role těžařů v síti Bitcoin byla předmětem intenzivní debaty během tzv. "válek o velikost bloku". Ačkoliv jsou pro bezpečnost a funkčnost sítě nezbytní, těžaři nutně nevlastní konečnou moc v ekosystému Bitcoinu. Rovnováha mezi těžaři, uzly a koncovými uživateli zajišťuje integritu a distribuci sítě.

### Války o velikost bloku

Během válek o velikost bloku bylo mnoho těžařů proti určitým vývojům v síti, což zdůraznilo napětí mezi různými aktéry v ekosystému. Otázka, jak vyvážit moc mezi těžaři, uzly a uživateli, aby byla zajištěna dlouhodobá bezpečnost Bitcoinu, zůstává otevřená.

![image](assets/en/09.webp)

Bezpečnostní dilema Bitcoinu spočívá v křehké rovnováze. Zatímco těžaři hrají klíčovou roli při ověřování a vytváření bloků, uzly udržují integritu ověřováním a validací transakcí a bloků. Nesprávný nebo podvodný blok bude uzly odmítnut, čímž dojde k cenzurování těžaře a zachování bezpečnosti sítě. Moc mají také uzly a uživatelé sítě Bitcoin. Uzly mají moc ověřování a validace, zatímco uživatelé mají moc rozhodnout, kterou blockchainovou síť použijí. Toto rozdělení moci zajišťuje distribuci a integritu sítě Bitcoin.

Války o velikost bloku odhalily nejistotu a napětí, které jsou vlastní správě sítě Bitcoin. Ačkoliv je v současnosti dominantním řetězcem Bitcoin Core, debata o správě a řízení sítě pokračuje.

Nakonec je odpovědnost sdílena mezi všechny aktéry v síti Bitcoin. Pokles počtu uživatelů, uzlů nebo těžařů by mohl síť oslabit, zvýšit riziko centralizace a zranitelnosti vůči útokům. Každý aktér přispívá k robustnosti a bezpečnosti sítě, což zdůrazňuje důležitost udržení rovnováhy moci a odpovědnosti.

### Moc těžařů

Elegantní teorie her od Satoshiho Nakamota vytvořila situaci, kde každý aktér v síti Bitcoin je motivován jednat správně, aby chránil jak své vlastní zájmy, tak zájmy ostatních účastníků. To vytváří rovnováhu, kde špatné chování může být potrestáno, čímž se zvyšuje bezpečnost a stabilita celého systému. Přesto zůstávají státy potenciální hrozbou. Jak bylo naznačeno na prezentaci na Surfing Bitcoin 2022, státy mohou pokusit o útok na těžební průmysl, čímž vystavují síť Bitcoin rizikům centralizace a útoku. Hypotetické scénáře, jako je vojenský útok zaměřený na výrobní zařízení těžebního hardwaru, zdůrazňují důležitost geografické a průmyslové diverzifikace pro odolnost sítě Bitcoin.

![image](assets/en/10.webp)

Centralizace výroby těžebního hardwaru v Číně představuje další riziko. Odmítnutí exportu těžebních strojů nebo akumulace hashovací síly pro potenciální útok 51% Čínou zdůrazňuje potřebu diverzifikované výroby těžebního hardwaru. Jako reakce na tyto rizika aktivně komunita Bitcoin hledá řešení. Společnosti jako Intel zvažují výrobu těžebního zařízení ve Spojených státech, což přispívá k distribuci výroby. Další iniciativy, jako je open-source Mining Development Kit (MDK) od společnosti Block, mají za cíl snížit monopol na design a výrobu těžebního hardwaru, což umožňuje širší distribuci hashovací síly. V jádru těchto diskusí leží základní poslání Bitcoinu: být sítí pro výměnu hodnot odolnou vůči cenzuře. Komunita Bitcoin neustále usiluje o posílení distribuce, odolnosti vůči cenzuře a anti-křehkosti sítě, odmítajíc předložené návrhy, jako je přechod na proof of stake, které nejsou v souladu s těmito základními principy.

### Fyzická spojitost Proof of Work vs Proof of Stake

Důkaz práce (Proof of Work - PoW) je zásadní, protože představuje fyzickou spojnici mezi skutečným světem a Bitcoinem. Ačkoliv jsou bitcoiny nehmotné, jejich produkce vyžaduje hmatatelnou energii, čímž se navazuje přímé spojení s fyzickým a skutečným světem. Toto spojení zajišťuje, že produkce a validace bitcoinů a bloků mají skutečnou energetickou cenu, čímž je síť Bitcoin ukotvena ve fyzické realitě a brání její úplné dominanci mocnými subjekty. PoW působí jako obrana proti centralizaci, zajišťující, že účast v síti a validace transakcí vyžadují investici do hmatatelných zdrojů. To brání monopolizaci sítě subjekty, které by jinak mohly získat kontrolu bez jakékoliv významné vstupní bariéry, čímž zajišťuje spravedlivější rozdělení moci a vlivu v rámci sítě Bitcoin.

![image](assets/en/11.webp)

### Omezení Důkazu vkladu

Na druhou stranu, Důkaz vkladu (Proof of Stake - PoS), ačkoliv umožňuje účast na malé škále, negarantuje ekvivalentní ochranu proti centralizaci. V síti PoS mají ti, kteří již drží velké množství měny, nepřiměřenou moc, což odráží stávající nerovnosti moci ve společnosti jako celku. Tato dynamika by potenciálně mohla perpetuovat centralizaci a koncentraci moci v rukou několika málo, v rozporu se základními distribučními cíli sítě Bitcoin. Argument, že každý se může na PoS podílet, i na malé škále, připojením se k poolům, není nutně robustní. V síti PoW může i malý přispěvatel s skromným vybavením aktivně participovat a přispívat k bezpečnosti a distribuci sítě.

### Shrnutí

Shrnutí, těžaři posilují síť Bitcoin proti cenzuře používáním elektrické energie k výpočtu důkazu práce Bitcoinu a jsou odměňováni novými bitcoiny a transakčními poplatky. S profesionalizací průmyslu se objevují různí hráči, kteří plní různé role, od tvorby čipů po správu těžebních farem. Kromě toho finance také hrají roli, když rozhodují, kdo přežije během různých tržních fází. Problém centralizace přetrvává, s nejbohatšími subjekty, které by mohly trh ovládnout. Avšak na hardwarové i softwarové úrovni se vyvíjejí alternativy. Je na každém jednotlivci, aby jednal a přispěl k distribuci sítě. Bitcoin představuje mimořádnou příležitost nejen z hlediska svobody, ale také energetické nezávislosti. Navzdory kontroverzím ohledně jeho spotřeby elektrické energie, Bitcoin nabízí ekonomický stimul pro přechod k rozumnějšímu a hojnějšímu využívání energie, realizující to, co bylo dříve ekologickým ideálem.

## Cena Bitcoinu a Hashrate, korelace?

<chapterId>e6676214-007c-5181-968e-c27536231bd6</chapterId>

![Jak získat čistý a nedotčený bitcoin?](https://youtu.be/A5MTtn4mm44?si=D1Yi0dVwkyafeHv-)

### Hashrate, cena a ziskovost

Aktuální hash rate, přestože cena Bitcoinu je na 30 000 dolarů ve srovnání s předchozím maximem 69 000 dolarů, zdůrazňuje hmatatelné spojení mezi těžbou a skutečným světem. Období býčího trhu vedou k vysoké poptávce po těžbě Bitcoinu a k nárůstu objednávek strojů od výrobců jako jsou Avalon a Bitmain. Výroba a dodání však nejsou okamžité, což vytváří nesoulad mezi zvýšenou poptávkou a pozdější dostupností. To může vést k tomu, že stroje objednané během býčího trhu jsou dodány v medvědím trhu, což zdůrazňuje významnou asymetrii mezi nízkou cenou a vysokým hash rate.
Tato situace také ilustruje odolnost Bitcoinu, která je často hodnocena na základě jeho ceny. Avšak pro hlubší analýzu zdraví Bitcoinu je nutné zkoumat jeho hash rate, což měří počet výpočtů za sekundu v síti Bitcoinu. Zatímco cena Bitcoinu kolísá, jeho náklady, spojené s elektřinou potřebnou k provozu těžebních strojů, zůstávají zásadní pro pochopení tržních dynamik. Zaměřením na náklady místo ceny získáme konzistentnější perspektivu na stabilitu a dlouhodobou životaschopnost Bitcoinu. Obecně platí, že náklady na Bitcoin jsou proporcionální jeho ceně, což poskytuje lepší pochopení kolísání cen a budoucích výhledů.

![obrázek](assets/en/12.webp)

### Hash Rate a Odmena

Těžba stanovuje minimální cenu pro Bitcoin, pod kterou by těžaři prodávali se ztrátou. Náklady na těžbu významně ovlivňují cenu, jak ilustruje zákaz těžby v Číně, kde hash rate i cena výrazně klesly, ale rychle se zotavily. Zaměření pouze na cenu může být zavádějící. Studium nákladů, prostřednictvím kalkulaček ziskovosti, nabízí vyváženější perspektivu. Avšak trh se může chovat iracionálně, s možností, že těžaři budou nuceni prodávat se ztrátou, což může snížit cenu pod náklady na těžbu. Pro posouzení zdraví Bitcoinu a jeho decentralizace by mohla být vyvinuta rovnice zahrnující různé faktory, jako je počet uzlů a cena. Tento přístup by mohl poskytnout nuancovanější analýzu Bitcoinu ve srovnání s diskusemi založenými pouze na ceně.

### Těžba pro zisk nebo pro síť?

Otázka je hluboká a zahrnuje několik dimenzí těžby Bitcoinu. Rovnováha mezi hledáním zisku a přispíváním k bezpečnosti a distribuci sítě Bitcoinu je pro těžaře stálým dilematem. Debata v komunitě Bitcoinu pokračuje, s silnými argumenty na obou stranách.

- Těžba pro zisk:

* Pro: Těžaři jsou přirozeně přitahováni potenciálními výdělky z těžby Bitcoinu. Investice do drahého těžebního zařízení mohou být vyváženy těžebními odměnami a transakčními poplatky, zejména když je cena Bitcoinu vysoká.
* Proti: Snaha o zisk může vést k centralizaci výpočetního výkonu, pokud si pouze několik velkých společností může dovolit investovat do špičkového těžebního zařízení. Navíc těžba za účelem zisku může mít významný dopad na životní prostředí.

- Těžba pro síť:

* Pro: Těžba s cílem přispět k bezpečnosti a decentralizaci sítě Bitcoinu je ušlechtilá iniciativa. Pomáhá posílit odolnost sítě a odolávat cenzuře a útokům.
* Proti: Bez dostatečného finančního podnětu může být pro těžaře obtížné pokračovat v podpoře sítě, zejména pokud provozují se ztrátou.
  Iniciativa Attakai zdůrazňuje důležitost přispívání do sítě a zároveň nabízí řešení, jak těžbu udělat dostupnější a méně škodlivou. Možnost těžit doma s cenově dostupnějším vybavením a řešeními na snížení hlukového znečištění může pomoci demokratizovat těžbu Bitcoinu. Podporuje ty, kteří mají zájem o Bitcoin, aby nejen investovali a drželi bitcoiny, ale také aktivně participovali na zabezpečení sítě. Poskytováním otestovaného vybavení a průvodců pro montáž a instalaci usnadňuje Attakai vstup do světa těžby Bitcoinu. Také podporuje inovace a nepřetržité zlepšování, zve komunitu, aby přispívala a sdílela své nápady a zkušenosti, čímž vylepšuje domácí těžbu. Model Attakai je odpovědí na otázku těžby pro zisk nebo pro síť. Nejde jen o zisk, ale také o posílení distribuce a bezpečnosti sítě Bitcoinu, zatímco umožňuje více lidem účastnit se těžby, učit se a rozumět tomuto klíčovému průmyslu. Výzva potenciálního zákazu těžby v Evropě zůstává otevřenou otázkou. To vyvolává obavy o budoucnost těžby Bitcoinu v regionu a potřebu vyvážené regulace, která uznává význam těžby pro bezpečnost a životaschopnost sítě Bitcoinu, zatímco řeší environmentální problémy. Attakai a další podobné iniciativy mohou hrát klíčovou roli v této debatě, ukazujíce, že je možné těžit udržitelnějším a odpovědnějším způsobem, zatímco pozitivně přispívat do sítě Bitcoinu.

## Suverenita a regulace

<chapterId>9d9a5908-2acc-501e-906b-a6fce9ecfebd</chapterId>

### Suverenita před ziskem?

Abychom řešili zásadní otázku bohatství prostřednictvím těžby, je důležité zvážit různé perspektivy a přístupy. Otázky týkající se ziskovosti těžby jsou běžné, s dotazy ohledně nákupu akcií společností jako Riot nebo leasingu těžebních strojů v zemích s nízkými energetickými náklady, jako je Island nebo Rusko. Před vstupem do těžby by klíčovou úvahou mělo být porovnání ziskovosti těžby s přímým nákupem Bitcoinu. Pokud náklady na těžbu Bitcoinu převyšují náklady na jeho přímý nákup, je obvykle rozumnější koupit Bitcoin přímo. To umožňuje vyhnout se mnoha výzvám a nákladům spojeným s procesem těžby.

Nicméně, těžba nabízí jedinečné cesty, jak se zapojit do ekosystému Bitcoinu. Například těžba Bitcoinu v zimě může být chytrým způsobem, jak vytápět váš domov, zatímco generujete příjem v Bitcoinech. Další možností je investovat do společností, které prodávají těžební vybavení a skladují a spravují stroje na místech s nízkými energetickými náklady, čímž poskytují přístup k výhodným elektřinovým sazbám bez nutnosti řízení vybavení.

Přesto těžba představuje významné výzvy. Dobře známé přísloví ve světě kryptoměn, "Nejsou-li to vaše klíče, nejsou to vaše bitcoiny," nachází podobný odraz ve světě těžby: "Není-li to váš hashrate, není to vaše odměna." Příběhy zklamání a odpojených strojů jsou běžné, s mnoha hráči slibujícími výjimečné výsledky, ale nedokáží je dodat. Problémy s dodávkami elektřiny a poruchami strojů mohou investory nechat bezmocnými, s drahým vybavením, které nekontrolují. V tomto kontextu je opatrnost a hluboké porozumění sektoru těžby klíčové před vstupem do něj. Ačkoliv existují příležitosti pro zisky, rizika jsou významná a informovaný a promyšlený přístup je nezbytný pro navigaci v tomto složitém a často nepředvídatelném oboru. Je proto nezbytné provést důkladný výzkum a pečlivě zvážit klady a zápory před zapojením do těžby Bitcoinu.

![image](assets/en/13.webp)

### Původní Bitcoiny

Touha vlastnit vlastní hashrate se jeví jako slibná cesta ve světě těžby. Avšak navigace v tomto složitém ekosystému vyžaduje opatrný přístup. Oblast cloudové těžby je poznamenána velkým počtem podvodů, které jsou poháněny nedostatkem porozumění těžbě ze strany mnoha investorů. Atraktivní nabídky, balené různými způsoby, mohou snadno zmást ty, kteří nejsou dostatečně informováni. Na druhou stranu, vlastnictví vlastního těžebního zařízení nabízí značné výhody. Kromě osobní spokojenosti z aktivního přispívání k zabezpečení sítě Bitcoin a sledování odměn padajících do vaší peněženky, je tu lákavý aspekt "panenských bitcoinů". To jsou čerstvě vytěžené bitcoiny, které nikdy nebyly utraceny a nemají žádnou historii. Tyto bitcoiny jsou často považovány za cennější, protože nikdy nebyly "znečištěny", což nabízí určitou záruku proti odmítnutí regulátory nebo hlavními obchodními platformami.
Možnost těžit panenské bitcoiny při vyhýbání se procedurám Know Your Customer (KYC) představuje další přidanou hodnotu. Mnoho těžebních poolů nevyžaduje identitu těžařů, což umožňuje získání bitcoinů bez nutnosti procházet zdlouhavými kontrolami identity. Panenské bitcoiny jsou vnímány jako "čisté", bez jakékoli minulosti nebo asociace. Jsou obzvláště vyhledávány velkými institucionálními hráči, kteří mohou zaručit legitimitu svých digitálních aktiv před regulačními orgány. Avšak, navzdory těmto výhodám, je zásadní uznat, že těžební průmysl zůstává extrémně konkurenční a nestabilní, a nepředvídané události mohou narušit těžební operace.

V tomto kontextu se jeví jako moudré zvolit autonomní a vzdělaný přístup k těžbě. Získání vlastního hashrate a investice do osobního těžebního zařízení, při zůstávání vědom si rizik a výzev, může potenciálně nabídnout bezpečnější a uspokojivější cestu k získání panenských bitcoinů, čímž zvyšuje finanční suverenitu jednotlivce a současně podporuje ekosystém Bitcoinu jako celku.

### Je těžba zakázána v Evropě?

S otázkou potenciálního zákazu těžby v Evropě se diskuse o regulaci stávají stále relevantnější. Kolísavá regulační krajina skutečně může významně ovlivnit průmysl těžby Bitcoinu. Zákaz těžby v Evropě je představitelný scénář, zejména s ohledem na precedenty v Číně. Ačkoliv těžební operace v Číně pokračují navzdory zákazu, Evropa by mohla jít podobnou cestou. Širší distribuce hashrate mezi různé regiony by mohla pomoci posílit těžební komunitu v Evropě, umožňující jim účinně čelit nedorozuměním a nesprávným představám o těžbě, jejím dopadu na životní prostředí a jejím otisku na elektrické síti.
![obrázek](assets/en/14.webp)

V čele s kampaněmi jako ty od Greenpeace a často zavádějícími čísly z některých studií, zůstává nejlepší zbraní pravdivá informace. Je zásadní informovat širokou veřejnost a rozhodovatele o realitě těžby, její složitosti a jejích nuancích, místo aby se spoléhalo na stereotypy a nepřesné informace. Čím více lidí je informováno a vědomo si, co těžba skutečně je, tím lépe může průmysl bránit se proti potenciálním restriktivním regulacím.

Závěrem, navzdory regulačnímu riziku a možnosti zákazu těžby v Evropě, zůstává nejsilnější zbraní vzdělání a informace. Jasné a přesné porozumění těžbě, jak funguje a jaký má dopad, může pomoci demystifikovat průmysl a bojovat proti dezinformacím, čímž nabízí lepší odolnost proti potenciálně škodlivým regulacím. Iniciativa školit a informovat lidi o těžbě, jak toto diskuse činí, je krokem správným směrem k zajištění udržitelnosti a růstu těžby v Evropě a po celém světě. Nepřetržité úsilí o vzdělávání a informování je zásadní pro zajištění bezpečné a prosperující budoucnosti pro průmysl těžby Bitcoinu.

## Rozhovor s profesionálem z průmyslu těžby

<chapterId>4d613261-d1a8-5ffe-a50c-047a3d77d6c5</chapterId>

### Za scénou průmyslové těžby - Sebastien Gouspillou

![Za kulisami průmyslového těžení - Sebastien Gouspillou](https://www.youtube.com/watch?v=vYaQRLSDr5E&t=69s)

# Domácí těžba a opětovné využití tepla

<partId>78d22d06-2c4a-573f-86bb-1027115dad3a</partId>

## Attakai - umožňuje domácí těžbu a dělá ji přístupnou!

<chapterId>1f5d1b74-2f99-5f31-a088-a73d36491ebf</chapterId>

Attakai, což v japonštině znamená "ideální teplota", je název iniciativy zaměřené na objevování těžby bitcoinů prostřednictvím opětovného využití tepla, kterou spustili @ajelexBTC a @jimzap21 s Découvre Bitcoin.
Tento průvodce úpravou ASIC poslouží jako základ pro další poznání o těžbě, jejím fungování a podkladové ekonomice tím, že ukáže možnost přizpůsobení těžaře bitcoinů pro použití jako radiátory v domácnostech. To nabízí větší pohodlí a úspory, umožňuje účastníkům dostávat ne-KYC BTC cashback na jejich účet za elektrické vytápění.

Bitcoin automaticky upravuje obtížnost těžby a odměňuje těžaře za jejich účast. Koncentrace hashrate však může představovat rizika pro neutralitu sítě. Využití výpočetního výkonu Bitcoinu pro řešení vytápění přímo prospívá samotné síti tím, že zvyšuje distribuci výpočetního výkonu.

### Proč opětovně využít teplo z ASIC?

Je důležité pochopit vztah mezi energií a výrobou tepla v elektrickém systému.

Pro investici 1 kW elektrické energie vyrábí elektrický radiátor 1 kW tepla, ani více, ani méně. Nové radiátory nejsou účinnější než tradiční radiátory. Jejich výhoda spočívá v jejich schopnosti nepřetržitě a rovnoměrně rozdělovat teplo v místnosti, což poskytuje větší pohodlí ve srovnání s tradičními radiátory, které střídají vysoký výkon vytápění a žádné vytápění, čímž generují pravidelné teplotní variace a nepohodlí.

Počítač, nebo obecněji elektronická deska, nekonzumuje energii k provádění výpočtů, jednoduše potřebuje, aby energie protékala jejími komponentami, aby fungovala. Spotřeba energie je způsobena elektrickým odporem komponent, který produkuje ztráty a generuje teplo, známé jako Jouleův jev.

Některé společnosti přišly s nápadem kombinovat potřeby výpočetního výkonu s potřebami vytápění prostřednictvím radiátorů/serverů. Nápad spočívá v distribuci serverů společnosti do malých jednotek, které by mohly být umístěny v domácnostech nebo kancelářích. Tento nápad však čelí několika problémům. Potřeba serverů není spojena s potřebou vytápění a společnosti nemohou flexibilně využívat výpočetní schopnosti svých serverů. Existují také limity pro šířku pásma, kterou mohou jednotlivci mít. Všechna tato omezení brání společnosti v tom, aby tyto nákladné instalace ziskově využívala nebo poskytovala stabilní online serverovou nabídku bez datových center, která mohou převzít, když není potřeba vytápění.

> Teplo generované vaším počítačem není ztraceno, pokud potřebujete vytápět svůj domov. Pokud používáte elektrické vytápění tam, kde žijete, pak teplo z vašeho počítače není ztraceno. Generování tohoto tepla vaším počítačem stojí stejně. Pokud máte levnější systém vytápění než elektrické vytápění, pak ztráta spočívá pouze ve rozdílu nákladů. Pokud je léto a používáte klimatizaci, pak je to dvojnásobná ztráta. Těžba bitcoinů by měla probíhat tam, kde je to levnější. Možná to bude tam, kde je klima chladné a kde je vytápění elektrické, kde se těžba stane zdarma.
> Satoshi Nakamoto - 8. srpna 2010

Bitcoin a jeho proof of work se vyznačují tím, že automaticky upravují obtížnost těžby na základě množství výpočetního výkonu vykonaného celou sítí. Toto množství se nazývá hashrate a vyjadřuje se v hashech za sekundu. Dnes se odhaduje na 380 exahashů za sekundu, což je 380 miliard miliard hashů za sekundu. Tento hashrate představuje práci a tedy i množství spotřebované energie. Čím vyšší je hashrate, tím vyšší je obtížnost a naopak. Těžař Bitcoinu tak může být aktivován nebo deaktivován kdykoliv bez toho, aby to ovlivnilo síť, na rozdíl od radiátorů/serverů, které musí zůstat stabilní, aby poskytovaly svou službu. Těžař je odměněn za svou účast vzhledem k ostatním, bez ohledu na to, jak malá může být.

Shrnutí, elektrický radiátor a těžař Bitcoinu oba produkují 1 kW tepla za 1 kW spotřebované elektřiny. Těžař však také obdrží bitcoiny jako odměnu. Bez ohledu na cenu elektřiny, cenu bitcoinu nebo konkurenci v činnosti těžby Bitcoinu na síti, je ekonomicky výhodnější topit těžařem než elektrickým radiátorem.

### Přidaná hodnota pro Bitcoin

Je důležité pochopit, jak těžba přispívá k decentralizaci Bitcoinu.
Několik stávajících technologií bylo geniálně kombinováno, aby oživilo konsensus Nakamota. Tento konsensus ekonomicky odměňuje poctivé účastníky za jejich příspěvek k provozu sítě Bitcoin, zatímco odrazuje nečestné účastníky. To je jeden z klíčových bodů, který umožňuje síti existovat udržitelně.
Poctiví aktéři, ti, kteří těží podle pravidel, soutěží mezi sebou o získání co největšího podílu na odměně za produkci nových bloků. Tento ekonomický stimul přirozeně vede k určité formě centralizace, protože společnosti se rozhodují specializovat na tuto lukrativní činnost snižováním svých nákladů prostřednictvím ekonomií rozsahu. Tyto průmyslové subjekty mají výhodnou pozici pro nákup a údržbu strojů, stejně jako vyjednávání velkoobchodních cen elektřiny.

> Na začátku by většina uživatelů provozovala uzly sítě, ale jak síť roste za určitý bod, byla by čím dál více ponechána specialistům se serverovými farmami specializovaného hardware. Serverová farma by potřebovala mít na síti pouze jeden uzel a zbytek LAN by se k tomuto uzlu připojoval.
> Satoshi Nakamoto - 2. listopadu 2008

Některé entity drží značný procentuální podíl celkového hashrate ve velkých těžebních farmách. Můžeme pozorovat nedávnou studenou vlnu ve Spojených státech, kde byla významná část hashrate odpojena, aby se energie přesměrovala do domácností s výjimečnou potřebou elektřiny. Po několik dní byli těžaři ekonomicky motivováni k vypnutí svých farem, a tato výjimečná povětrnostní situace je vidět na křivce hashrate Bitcoinu.

Tento problém by se mohl stát problematickým a představuje významné riziko pro neutralitu sítě. Aktér s více než 51% hashrate by mohl snadněji cenzurovat transakce, pokud by si to přál. Proto je důležité rozdělit hashrate mezi více aktérů, než centralizované entity, které by mohly být snadněji zabaveny vládou, například.

**Pokud jsou těžaři rozděleni do tisíců, nebo dokonce milionů, domácností po celém světě, stává se velmi obtížným pro stát, aby je ovládl.**

Když vyjde z továrny, těžař není vhodný k použití jako topení v domácnosti kvůli dvěma hlavním problémům: nadměrnému hluku a nedostatku nastavení. Tyto problémy však lze snadno vyřešit prostřednictvím úprav hardwaru a softwaru, což umožňuje mnohem tišší těžař, který lze konfigurovat a automatizovat jako moderní elektrické radiátory.

**Attakaï je vzdělávací iniciativa, která vás učí, jak nejefektivnějším způsobem přestavět Antminer S9.**
Toto je vynikající příležitost naučit se praxí, zatímco za vaši účast budete odměněni KYC-free satoshi.

## Nákupní průvodce pro použitý ASIC

<chapterId>3b0b3bf0-859b-57f2-b92f-843ac70b7e68</chapterId>

V této části probereme nejlepší postupy pro nákup použitého Bitmain Antminer S9, stroje, na kterém bude založen tento návod na retrofitování radiátoru. Tento průvodce se vztahuje i na další modely ASIC, jelikož jde o obecný nákupní průvodce pro použité těžební hardware.

Antminer S9 je zařízení, které nabízí Bitmain od května 2016. Spotřebuje 1400W elektřiny a produkuje 13,5 TH/s. Přestože je považován za starý, zůstává vynikající možností pro začátek těžby. Jelikož byl vyroben ve velkém množství, je snadné najít v mnoha regionech světa hojně náhradní díly. Obvykle lze získat peer-to-peer na stránkách jako eBay nebo LeBonCoin, jelikož profesionální prodejci jej již nenabízejí kvůli jeho nižší konkurenceschopnosti ve srovnání s novějšími stroji. Je méně efektivní než ASICy jako Antminer S19, který je nabízen od března 2020, ale to z něj činí cenově dostupný použitý hardware a vhodnější pro úpravy, které provedeme.

Antminer S9 existuje v několika variantách (i, j), které přinášejí menší úpravy do hardware první generace. Nemyslíme si, že by to mělo ovlivnit vaše rozhodnutí o koupi, a tento průvodce funguje pro všechny tyto varianty.

Cena ASIC se liší v závislosti na mnoha faktorech, jako je cena bitcoinu, obtížnost sítě, efektivita stroje a cena elektřiny. Proto je obtížné dát přesný odhad pro nákup použitého stroje. V únoru 2023 se očekávaná cena ve Francii obvykle pohybuje od 100 € do 200 €, ale tyto ceny se mohou rychle měnit.

![image](assets/en/15.webp)

Antminer S9 se skládá z následujících částí:

- 3 hashboardy, které obsahují čipy produkující hashovací výkon.

![image](assets/en/16.webp)

- Řídící deska, která zahrnuje slot pro SD kartu, Ethernetový port a konektory pro hashboardy a ventilátory. To je mozek vašeho ASIC.

![image](assets/en/17.webp)

- 3 datové kabely, které propojují hashboardy s řídící deskou.

![image](assets/en/18.webp)

- Zdroj napájení, který pracuje na 220V a může být zapojen jako běžný domácí spotřebič.

![image](assets/en/19.webp)

- 2 120mm ventilátory.

![image](assets/en/20.webp)

- Samec kabelu C13.

![image](assets/en/21.webp)

Při koupi použitého stroje je důležité zkontrolovat, zda jsou všechny části zahrnuty a funkční. Během výměny byste měli prodejce požádat, aby stroj zapnul, abyste zkontrolovali jeho správnou funkci. Je důležité ověřit, že zařízení správně zapne, a poté zkontrolovat připojení k internetu připojením Ethernetového kabelu a přístupem k Bitmain přihlašovacímu rozhraní prostřednictvím webového prohlížeče ve stejné lokální síti. Tuto IP adresu můžete najít připojením k rozhraní vašeho internetového routeru a hledáním připojených zařízení. Tato adresa by měla mít následující formát: 192.168.x.x

![image](assets/en/22.webp)
Také ověřte, že výchozí přihlašovací údaje fungují (uživatelské jméno: root, heslo: root). Pokud výchozí přihlašovací údaje nefungují, bude nutné stroj resetovat.
![image](assets/en/23.webp)

Po připojení byste měli být schopni vidět stav každého hashboardu na palubní desce. Pokud je těžař připojen k poolu, měli byste vidět, že všechny hashboardy fungují. Je důležité poznamenat, že těžaři vydávají hodně hluku, což je normální. Také se ujistěte, že ventilátory pracují správně.

Poté můžete odstranit těžební pool předchozího majitele, abyste později nastavili vlastní. Pokud chcete, můžete také prozkoumat hashboardy rozebráním stroje. Tento krok je však složitější a vyžaduje více času a některé nástroje. Pokud se chcete tohoto rozebírání zúčastnit, můžete se odkázat na další část tohoto návodu, která popisuje, jak na to. Je důležité poznamenat, že těžaři shromažďují hodně prachu a vyžadují pravidelnou údržbu. Tuto akumulaci prachu a kvalitu údržby můžete pozorovat rozebráním stroje.
Po přezkoumání všech těchto bodů můžete svůj stroj koupit s vysokou mírou důvěry. V případě pochybností se poraďte s komunitou.

Shrnutí tohoto průvodce jednou větou: **"Nevěř, ověř."**

[Obrátit se můžete také na profesionály v oblasti rekonfigurace těžebních strojů, jako je náš partner 21energy. Nabízejí testované stroje S9, vyčištěné a s již nainstalovaným softwarem BraiiinOS+. S partnerským kódem "decouvre" obdržíte 10% slevu na nákup S9 a zároveň podpoříte projekt Attakai.](https://21energy.io/en/produkt/bitmain-antminer-s9-bundle/)

## Průvodce nákupem hardwarových úprav pro S9

<chapterId>fa5f5eca-bcbf-5a83-9b03-98ecbadbabd6</chapterId>

Jako majitel Antmineru S9 pravděpodobně víte, jak hlučné a objemné toto zařízení může být. Je však možné jej přeměnit na tichý a připojený ohřívač, pokud budete postupovat podle několika jednoduchých kroků. V této části představíme potřebné vybavení pro provedení úprav.

Pokud jste zručný kutil a chcete přeměnit těžař na ohřívač, tento návod je pro vás. Chceme vás varovat, že úpravy elektronického zařízení mohou představovat elektrická rizika. Je proto nezbytné podniknout veškerá nezbytná opatření, aby se předešlo jakémukoli poškození nebo zranění.

1. Vyměňte ventilátory

Původní ventilátory Antmineru S9 jsou příliš hlučné na to, abyste svůj Antminer mohli používat jako ohřívač. Řešením je nahradit je tichými ventilátory. Náš tým otestoval několik modelů značky Noctua a vybral Noctua NF-A14 iPPC-2000 PWM jako nejlepší kompromis. Ujistěte se, že si vyberete 12V verzi ventilátorů. Tento 140mm ventilátor může produkovat až 1200W tepla při teoretické hladině hluku 31 dB. Pro instalaci těchto 140mm ventilátorů budete potřebovat použít adaptér z 140mm na 120mm, který najdete v obchodě DécouvreBitcoin. Přidáme také ochranné mřížky 140mm.

![image](assets/en/24.webp)
![image](assets/en/25.webp)
![image](assets/en/26.webp)
Ventilátor napájecího zdroje je také poměrně hlučný a potřebuje být vyměněn. Doporučujeme Noctua NF-A6x25 PWM. Všimněte si, že konektory ventilátorů Noctua nejsou stejné jako originální, takže budete potřebovat adaptér konektoru pro jejich připojení. Dva budou stačit. Opět se ujistěte, že si vyberete 12V verzi ventilátoru.
![image](assets/en/27.webp)
![image](assets/en/28.webp)

2. Přidání WIFI/Ethernetového mostu

Místo použití Ethernetového kabelu můžete svůj Antminer připojit přes WIFI přidáním WIFI/Ethernetového mostu. Vybrali jsme vonets vap11g-300, protože snadno umožňuje přijímat WIFI signál z vašeho internetového boxu a přenášet ho do vašeho Antmineru přes Ethernet bez vytváření podřízené sítě. Pokud máte elektrotechnické dovednosti, můžete ho napájet přímo z napájecího zdroje Antmineru bez nutnosti přidávat USB nabíječku. K tomu budete potřebovat samičí jack 5,5mmx2,1mm.

![image](assets/en/29.webp)
![image](assets/en/30.webp)

3. Volitelně: přidání chytré zásuvky
   Pokud chcete zapínat/vypínat svůj Antminer ze svého smartphonu a sledovat jeho spotřebu energie, můžete přidat chytrou zásuvku. Testovali jsme zásuvku ANTELA ve verzi 16A, kompatibilní s aplikací smartlife. Tato chytrá zásuvka umožňuje zobrazit denní a měsíční spotřebu energie a připojuje se přímo k vašemu internetovému routeru přes WiFi.

![image](assets/en/31.webp)

Seznam vybavení a odkazů

- 2X 3D adaptér 140mm na 120mm

- [2X NF-A14 iPPC-2000 PWM](https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW/ref=sr_1_2?__mk_fr_FR=ÅMÅŽÕÑ&crid=JCNLC31F3ECM&keywords=NF-A14+iPPC-2000+PWM&qid=1676819936&sprefix=nf-a14+ippc-2000+pwm%2Caps%2C114&sr=8-2)

- [2X 140mm ventilátorové mřížky](https://www.amazon.fr/dp/B06XD4FTSQ?psc=1&ref=ppx_yo2ov_dt_b_product_details)
- [Noctua NF-A6x25 PWM](https://www.amazon.fr/Noctua-nf-a6-25-PWM-Ventilateur-Marron/dp/B00VXTANZ4/ref=sr_1_1_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=3T313ABZA5EDE&keywords=Noctua+NF-A6x25+PWM&qid=1676819329&sprefix=noctua+nf-a6x25+pwm%2Caps%2C71&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&smid=A38F5RZ72I2JQ)
- [Elektrikářský cukr 2.5mm2](https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS/ref=sr_1_3?__mk_fr_FR=ÅMÅŽÕÑ&crid=25IRJD7A0YN2A&keywords=sucre%2Belectrique%2B2mm2&qid=1676820815&sprefix=sucre%2Belectrique%2B2mm2%2Caps%2C84&sr=8-3&th=1)
- [Vonets vap11g-300](https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W/ref=sr_1_3_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=13Q33UHRKCKG5&keywords=vonet&qid=1676819146&s=electronics&sprefix=vonet%2Celectronics%2C98&sr=1-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)
- [Volitelná chytrá zásuvka ANTELA](https://www.amazon.fr/dp/B09YYMVXJZ/ref=twister_B0B5X46QLW?_encoding=UTF8&psc=1)

# Attakai - Úprava softwaru Antmineru S9

<partId>afc9c29a-84aa-5f1d-82e2-5fd9ff2e1805</partId>

## Nastavení mostu WIFI/Ethernet od Vonet

<chapterId>3cf487a4-21ef-5b24-83d5-789b811f740f</chapterId>

Pro připojení vašeho ASIC přes WIFI budete potřebovat zařízení nazývané most. Toto zařízení umožňuje přijímat WIFI signál z vašeho routeru a přenášet ho na jiné zařízení prostřednictvím Ethernetu.

Mnoho zařízení může tuto funkci plnit, ale doporučujeme WiFi Bridge/Repeater od VONETS pro jeho pohodlí.

Most napájejte připojením přes USB.

Z vašeho počítače se připojte k WIFI síti VONETS\_**\*\*** s heslem 12345678.

![obrázek](assets/en/32.webp)

Přihlaste se pomocí uživatelského jména "admin" a hesla "admin".

![obrázek](assets/en/33.webp)

Vyberte Průvodce.

![obrázek](assets/en/34.webp)

Vyberte WIFI síť, ke které chcete svůj miner připojit, a poté klikněte na Další.

POZNÁMKA: Most Vonet funguje pouze na frekvenci 2.4GHz. V dnešní době routery obvykle nabízejí dvě WIFI sítě, jednu na 2.4GHz a druhou na 5GHz.

![obrázek](assets/en/35.webp)

Zadejte heslo k vaší WIFI síti do pole "Heslo zdrojového WIFI hotspotu". Pokud nechcete používat váš most Vonet k rozšíření vaší WIFI sítě, zaškrtněte políčko "Zakázat Hotspot". V opačném případě nechte nezaškrtnuté.

Poté můžete kliknout na Použít.

Nakonec klikněte na restart, aby se most restartoval. Reboot trvá několik minut.

Most by se měl připojit k vašemu routeru a objevit se pod názvem "[VONETS.COM](http://vonets.com/)". Pokud se stále nepřipojí po několika minutách, možná bude potřeba most odpojit a znovu připojit.
Jakmile je most připojen, připojte Ethernetový kabel z mostu do vašeho ASIC a poté zapojte ASIC do elektrické zásuvky. Poté můžete přistupovat k rozhraní ASIC stejným způsobem, jako by bylo přímo připojeno k vašemu routeru přes Ethernet.

## Resetování Antmineru S9

<chapterId>b518b6bd-9dae-5136-ae3c-1fafb1cb2592</chapterId>

Před instalací BraiinOS+ může být nutné resetovat váš S9 na tovární nastavení.
Tato metoda může být použita mezi 2 a 10 minutami po spuštění mineru.
2 minuty po zapnutí mineru, prosím, stiskněte tlačítko "Reset" na 5 sekund, poté ho uvolněte. Miner bude obnoven na tovární nastavení během 4 minut a automaticky se restartuje (není potřeba ho vypínat).

![image](assets/en/36.webp)

## Instalace BraiinsOS+ na Antminer S9

<chapterId>38e8b1a8-8b1d-51ed-8b92-59d4ddb15184</chapterId>

Původní software instalovaný společností Antminer na jejich těžebních strojích je omezen ve funkcionalitě. Proto v tomto průvodci nainstalujeme jiný software nazvaný BraiinsOS+. Jedná se o software třetí strany vyvinutý prvním Bitcoin mining poolem, který má více funkcí a umožňuje například modifikaci výkonu stroje.

Existuje několik způsobů, jak nainstalovat Braiins OS+ na ASIC. Můžete se odkázat na tento průvodce stejně jako na [oficiální dokumentaci Braiins](https://academy.braiins.com/en/braiins-os/about/).

Zde uvidíme, jak snadno nainstalovat Braiins OS+ přímo na paměť vašeho Antmineru pomocí softwaru BOS toolbox, nahrazením původního operačního systému, prostřednictvím níže uvedených podrobných kroků.

1. Zapněte váš Antminer a připojte ho k vaší internetové boxu.
2. Stáhněte si BOS toolbox pro Windows / Linux.
3. Rozbalte stažený soubor a otevřete soubor bos-toolbox.bat. Vyberte jazyk a po několika okamžicích uvidíte toto okno:

![image](assets/en/37.webp)

4. BOS toolbox vám umožní snadno najít IP adresu vašeho Antmineru a nainstalovat BraiinsOS+. Pokud již znáte IP adresu vašeho stroje, můžete přeskočit na krok 8. V opačném případě přejděte na záložku scan.

![image](assets/en/38.webp)

5. Obvykle je na domácích sítích rozsah IP adres mezi 192.168.1.1 a 192.168.1.255, takže zadejte "192.168.1.0/24" do pole pro rozsah IP. Pokud je vaše síť jiná, prosím, změňte tyto adresy odpovídajícím způsobem. Poté klikněte na "Start".

6. Pozor, pokud má Antminer heslo, detekce nebude fungovat. V tom případě je nejjednodušším řešením provést reset.

7. Zde by se měly objevit všechny Antminery ve vaší síti a IP adresa je 192.168.1.37.

![image](assets/en/39.webp)

8. Klikněte na "Back" a poté na záložku "Install", zadejte dříve nalezenou IP adresu a klikněte na "Start".

> Pokud instalace nefunguje, může být nutné provést reset a zkuste to znovu (viz předchozí sekce).

![image](assets/en/40.webp)

9. Po několika okamžicích se váš Antminer restartuje a vy budete moci přistupovat k rozhraní Braiins OS+ na zadané IP adrese, zde 192.168.1.37, přímo v adresním řádku vašeho prohlížeče. Výchozí uživatelské jméno je "root" a výchozí heslo není nastaveno.

## Konfigurace BraiinsOS+

<chapterId>36e432f2-85bc-52d0-a62a-009fc4c69338</chapterId>

Budete potřebovat připojit se k vašemu ASIC pomocí lokální IP adresy vašeho zařízení ve vaší síti prostřednictvím prohlížeče.

IP adresu vašeho stroje můžete najít pomocí nástroje BOS toolbox nebo přímo na webové stránce vašeho routeru.

Výchozí přihlašovací údaje jsou stejné jako u původního operačního systému.

- uživatelské jméno: root
- heslo: (žádné)

Poté budete přivítáni na palubní desce Braiins OS+.

### Palubní deska

![obrázek](assets/en/41.webp)

Na této první stránce můžete sledovat skutečný výkon vašeho stroje.

- Tři grafy v reálném čase, které ukazují teplotu, hashrate a celkový stav vašeho stroje.
- Vpravo skutečný hashrate, průměrná teplota čipů, odhadovaná účinnost ve W/THs a spotřeba energie.
- Níže rychlost ventilátoru jako procento maximální rychlosti a počet otáček za minutu.

![obrázek](assets/en/42.webp)

- Dále níže najdete detailní pohled na každou hash desku. Průměrná teplota desky a čipů, které obsahuje, stejně jako napětí a frekvence.
- Detaily o aktivních těžebních poolech v Pools.
- Stav autotuningu v Tuner Status.
- Vpravo detaily o datech přenášených do poolu.

### Konfigurace

![obrázek](assets/en/43.webp)

### Systém

![obrázek](assets/en/44.webp)

### Rychlé akce

![obrázek](assets/en/45.webp)

# Attakai - Úprava ventilátoru

<partId>98266a8f-3745-58a0-9f6b-26a9734e1427</partId>

## Výměna ventilátoru zdroje

<chapterId>0c6befa7-f3ef-5bcf-ae8d-0ad5e5d41d70</chapterId>

> VAROVÁNÍ: Je nezbytné mít předtím nainstalovaný Braiins OS+ na vašem těžaři, nebo jakýkoliv jiný software, který může snížit výkon vašeho stroje. Toto opatření je klíčové, protože za účelem snížení hluku nainstalujeme méně výkonné ventilátory, které mohou rozptýlit méně tepla.

![obrázek](assets/en/46.webp)

### Potřebné materiály

- 1 ventilátor Noctua NF-A6x25 PWM
- 2.5mm2 elektrikářský cukr

> VAROVÁNÍ: Především, než začnete, ujistěte se, že jste odpojili váš těžař, abyste předešli jakémukoli riziku úrazu elektrickým proudem.

![obrázek](assets/en/47.webp)

Nejprve odstraňte 6 šroubů na boku pouzdra, které jej drží uzavřené. Jakmile jsou šrouby odstraněny, opatrně otevřete pouzdro, abyste odstranili plastovou ochranu kryjící komponenty.

![obrázek](assets/en/48.webp)
![obrázek](assets/en/49.webp)

Dále je čas odstranit původní ventilátor, přičemž si dávejte pozor, abyste nepoškodili ostatní komponenty. K tomu odstraňte šrouby, které jej drží na místě, a opatrně odlepte bílé lepidlo obklopující konektor. Je důležité postupovat opatrně, aby nedošlo k poškození drátů nebo konektorů.
![image](assets/en/50.webp)
Jakmile odstraníte původní ventilátor, všimnete si, že konektory nového ventilátoru Noctua se neshodují s konektory původního ventilátoru. Nový ventilátor má totiž 3 vodiče, včetně žlutého vodiče, který umožňuje regulaci rychlosti. Tento vodič však v tomto konkrétním případě nebude použit. Pro připojení nového ventilátoru se proto doporučuje použít speciální adaptér. Je však důležité poznamenat, že tento adaptér může být někdy těžko k nalezení.

![image](assets/en/51.webp)

Pokud tento adaptér nemáte, můžete přesto pokračovat v připojení nového ventilátoru pomocí elektrikářské spojky. K tomu budete muset přestřihnout kabely starého a nového ventilátoru.

![image](assets/en/52.webp)
![image](assets/en/53.webp)

Na novém ventilátoru použijte nůž a opatrně přestřihněte obrysy hlavního pláště ve vzdálenosti 1cm, aniž byste přestřihli pláště kabelů pod ním.

![image](assets/en/54.webp)

Poté, táhněte hlavní plášť směrem dolů, přestřihněte pláště červeného a černého kabelu stejným způsobem jako předtím. A žlutý kabel přestřihněte zarovna.

![image](assets/en/55.webp)

U starého ventilátoru je přestřihnutí hlavního pláště bez poškození plášťů červeného a černého drátu delikátnější. K tomu jsme použili jehlu, kterou jsme zasunuli mezi hlavní plášť a červené a černé dráty.

![image](assets/en/56.webp)
![image](assets/en/57.webp)

Jakmile jsou červené a černé dráty odhalené, opatrně přestřihněte pláště, abyste nepoškodili elektrické vodiče.

![image](assets/en/58.webp)

Poté připojte kabely pomocí spojky, černý drát s černým a červený drát s červeným. Můžete také přidat izolační pásku.

![image](assets/en/59.webp)
![image](assets/en/60.webp)

Jakmile je připojení provedeno, je čas nainstalovat nový ventilátor Noctua s mřížkou a starými šrouby. Nové šrouby v balení budou použity později. Ujistěte se, že je umístěn ve správné orientaci. Na jedné straně ventilátoru uvidíte šipku, která označuje směr proudění vzduchu. Je důležité umístit ventilátor tak, aby tato šipka směřovala dovnitř skříně. Poté znovu připojte ventilátor.

![image](assets/en/61.webp)
![image](assets/en/62.webp)

> Volitelně: Pokud se vyznáte v elektřině, můžete přímo přidat samičí konektor jack 5,5mm k 12V výstupu, který bude přímo napájet Wi-Fi most Vonet. Pokud si však nejste jisti svými elektrickými schopnostmi, je lepší použít USB konektor s nabíječkou typu smartphone, abyste předešli jakémukoli riziku zkratu nebo elektrického poškození.

![image](assets/en/63.webp)

Jakmile jsou připojení provedena, umístěte plastový kryt nad plast skříně a ne dovnitř.

![image](assets/en/64.webp)

Nakonec vraťte na místo kryt skříně a přišroubujte 6 šroubů na stranách, aby vše drželo pohromadě. A máte to, vaše skříň zdroje je nyní vybavena novým ventilátorem.

## Výměna hlavních ventilátorů

<chapterId>a29f60f1-3fa3-57fc-a630-9c97cec30e56</chapterId>

> VAROVÁNÍ: Je nezbytné mít předem nainstalovaný Braiins OS+ na vašem těžebním zařízení, nebo jakýkoliv jiný software schopný snížit výkon vašeho stroje. Toto opatření je klíčové, protože za účelem snížení hluku nainstalujeme méně výkonné ventilátory, které budou rozptylovat méně tepla.

![obrázek](assets/en/46.webp)

### Požadovaný materiál

- 2 kusy 3D adaptéru 140mm na 120mm
- 2 ventilátory Noctua NF-A14 iPPC-2000 PWM
- 2 mřížky na 140mm ventilátory

> VAROVÁNÍ: Především, před zahájením se ujistěte, že jste odpojili vaše těžební zařízení, abyste předešli jakémukoliv riziku úrazu elektrickým proudem.

1. Nejprve odpojte ventilátory a odšroubujte je.

![obrázek](assets/en/65.webp)

2. Konektory nových ventilátorů Noctua se neshodují s původními, ale nebojte se! Vezměte si nůž a opatrně odřízněte malé plastové záložky, aby konektory perfektně pasovaly na vaše těžební zařízení.

![obrázek](assets/en/66.webp)
![obrázek](assets/en/67.webp) 3. Je čas nainstalovat 3D díly!
Připevněte je na obě strany těžebního zařízení pomocí šroubů, které jste odstranili z ventilátorů. Zašroubujte je, dokud hlava šroubu není zarovnána s 3D dílem a je pevně na místě. Dávejte pozor, abyste příliš neutahovali, protože byste mohli díl deformovat a jeden ze šroubů by mohl dotknout kondenzátoru!

![obrázek](assets/en/68.webp)

4. Nyní přejděme k ventilátorům.

Připevněte je k 3D dílům pomocí šroubů dodaných v krabici. Dbejte na směr proudění vzduchu, šipky na stranách ventilátorů uvedou směr, kterým máte postupovat. Jděte od strany s Ethernet portem na druhou stranu. Viz foto níže.

![obrázek](assets/en/69.webp)
![obrázek](assets/en/70.webp)
![obrázek](assets/en/71.webp)

5. Poslední krok: připojte ventilátory a připevněte mřížky na vrch s šrouby, které nebyly použity v krabici s ventilátorem zdroje. Máte jich jen 4, ale 2 na mřížku v protilehlých rozích budou stačit. Pokud je potřeba, můžete hledat podobné šrouby v železářství.

![obrázek](assets/en/72.webp)
![obrázek](assets/en/73.webp)

Zatímco čekáte, až budeme moci nabídnout stylovější pouzdro pro váš nový ohřívač, můžete pouzdro a zdroj připevnit pomocí elektrikářských kabelových poutek.

![obrázek](assets/en/74.webp)

A jako poslední úprava připojte Vonet most k Ethernet portu a jeho napájení.

![obrázek](assets/en/75.webp)

A máte to, gratulujeme! Právě jste vyměnili celou mechanickou část vašeho těžebního zařízení. Nyní byste měli slyšet mnohem méně hluku.

# Attakai - Konfigurace

<partId>9c3918a8-d9a3-5a1f-bb9a-70314f7ac175</partId>

## Připojení k těžebnímu poolu

<chapterId>b57a6105-0a53-5fe9-bad1-d6d9daf97c0d</chapterId>
Můžete si představit těžební pool jako družstvo farmářů. Farmáři spojují svou produkci dohromady, aby snížili variabilitu nabídky a poptávky a tím získali stabilnější příjem pro svůj provoz. Těžební pool funguje stejným způsobem, přičemž sdíleným zdrojem jsou hashe. Skutečně, objevení jediného platného hashe umožňuje vytvoření bloku a získání coinbase odměny, aktuálně 6.25 BTC plus transakční poplatky zahrnuté v bloku.
Pokud těžíte sami, budete odměněni pouze tehdy, když najdete blok. V konkurenci proti všem ostatním těžařům na planetě byste měli velmi malou šanci vyhrát tuto loterii a stále byste museli platit poplatky spojené s používáním vašeho těžaře bez jakékoli záruky úspěchu. Těžební pooly řeší tento problém spojením výpočetního výkonu několika (tisíců) těžařů a sdílením jejich odměn na základě procentuální účasti na hashrate poolu, když je blok nalezen. Pro vizualizaci vašich šancí na samostatné těžení bloku můžete použít tento nástroj. Zadáním informací pro Antminer S9 vidíme, že šance na nalezení hashe, který umožňuje vytvoření bloku, jsou 1 z 24,777,849 pro každý blok nebo 1 z 172,068 za den. V průměru (s konstantním hashrate a obtížností) by to trvalo 471 let, než byste našli blok.

Nicméně, protože vše v Bitcoinu je založeno na pravděpodobnosti, někdy se stane, že solo těžaři jsou odměněni za přijetí tohoto rizika: Solo Bitcoin Miner Solves Block With Hash Rate of Just 10 TH/s, Beating Extremely Unlikely Odds – Decrypt

Pokud máte rádi hazard, můžete to zkusit, ale náš průvodce se nebude zaměřovat tímto směrem. Místo toho se zaměříme na těžební pool, který nejlépe vyhovuje našim potřebám pro vytvoření vytápěcího systému.

Při výběru těžebního poolu je třeba zvážit fungování odměn poolu, které se mohou lišit, stejně jako minimální částku před možností vybrat odměny na adresu. Například Braiins, který nabízí software, o kterém zde diskutujeme, nabízí také pool. Tento pool má systém odměn nazvaný "Score", který motivuje těžaře těžit dlouhodobě. Účast zahrnuje faktor uptime vyjádřený jako "scoring hashrate". V našem případě, kde chceme vytápěcí systém, který může být zapnutý pouze několik minut, to není ideální systém odměn. Preferujeme systém odměn, který nám dává stejnou odměnu za každou účast. Navíc minimální částka pro výběr z Braiins Poolu je 100 000 sats a On-Chain. Takže ztrácíme nějaké sats na transakčních poplatcích a část naší odměny může být zamčena, pokud v zimě nedotěžíme dostatek.

Odměnný model, který nás zajímá, je PPS, což znamená "pay-per-share". To znamená, že těžař obdrží odměnu za každý platný podíl. Existuje také varianta tohoto systému, FPPS (Full Pay Per Share), která nejenže rozděluje coinbase odměnu, ale také transakční poplatky zahrnuté v bloku. Těžební pooly, které doporučujeme pro propojení vašeho těžebního/vytápěcího systému, jsou Linecoin Pool (FPPS) a Nicehash (PPS).

- Nicehash: Výhodou Nicehash je, že výběr může být proveden pomocí Lightning s minimálními poplatky. Navíc minimální částka pro výběr je 2000 sats. Nevýhodou je, že Nicehash používá svůj hashrate pro nejvýnosnější blockchain, aniž by skutečně dával uživateli kontrolu, takže nemusí nutně přispívat k hashrate Bitcoinu.
- Linecoin: Výhodou Linecoinu je počet nabízených funkcí, jako je podrobný dashboard, možnost provádět výběry pomocí Paynym (BIP 47) pro lepší ochranu soukromí a integrace Telegram botu, stejně jako přímo konfigurovatelné automatizace v mobilní aplikaci. Tento pool těží pouze bloky Bitcoinu, ale minimální částka pro výběr zůstává vysoká na 100 000 sats. Rozhraní jednoho z těchto poolů si podrobněji prozkoumáme v budoucím článku.
  Pro konfiguraci poolu v Braiins OS+ budete potřebovat vytvořit účet v jednom z poolů dle vašeho výběru. Zde si vezmeme jako příklad Linecoin:

![obrázek](assets/en/76.webp)

Po vytvoření účtu klikněte na Connect To Pool

Poté zkopírujte Stratum adresu a vaše uživatelské jméno:

![obrázek](assets/en/77.webp)

Nyní se můžete vrátit do rozhraní Braiins OS+ a zadat tyto přihlašovací údaje. Pro heslo můžete pole nechat prázdné.

![obrázek](assets/en/78.webp)

## Optimalizace výkonu vašeho Antmineru S9

<chapterId>25380972-31c7-540d-80d8-17a06b171ca0</chapterId>

Jak overclocking, tak autotuning zahrnují úpravu frekvencí na hashovacích deskách za účelem zlepšení výkonu ASIC. Rozdíl mezi nimi spočívá ve složitosti nastavení těchto frekvencí.

Overclocking je jednoduchá úprava, která zahrnuje zvýšení frekvence na hashovacích deskách, čímž se zvyšuje hash rate stroje. Underclocking naopak zahrnuje snížení hodinové frekvence integrovaného obvodu pod jeho jmenovitou frekvenci. Snížením hodinové frekvence ASIC prostřednictvím underclockingu se také snižuje teplo generované hardwarem. To umožňuje snížit rychlost ventilátorů potřebných k chlazení ASIC, protože nemusí pracovat tak tvrdě, aby udržely vhodnou teplotu. Snížením rychlosti ventilátorů se také snižuje hluk generovaný ASIC. To může být obzvláště užitečné pro uživatele, kteří používají ASICy doma a snaží se minimalizovat hlukové rušení způsobené těžebním zařízením.

Braiins OS+ podporuje overclocking, underclocking ASICů a autotuning. Umožňuje uživatelům flexibilně upravovat frekvenci jejich hardware, aby maximalizovali výkon nebo ušetřili energii podle svých preferencí.

### Optimalizace výkonu vašeho Antmineru S9 s auto-tuningem

Před rokem 2018 měli těžaři dvě cesty, jak získat výhodu ve své činnosti: najít elektřinu za rozumnou cenu a kupovat efektivnější hardware. Avšak v roce 2018 byl objeven nový pokrok v oblasti softwaru a firmwaru pro těžbu, nazvaný AsicBoost. Tato technika umožňuje těžařům snížit své náklady přibližně o 13 % úpravou firmwaru běžícího na jejich zařízeních.

Dnes existuje nový pokrok v softwaru a firmwaru pro těžbu nazvaný autotuning, který nabízí ještě větší výhodu než AsicBoost. ASICy jsou složeny z mnoha malých počítačových čipů, které provádějí hashování. Tyto čipy jsou vyrobeny ze silikonu, stejného prvku široce používaného v polovodičích a dalších mikroelektronických komponentách. Klíčové pochopení zde spočívá v tom, že ne všechny silikonové čipy jsou identické, každý se může mírně lišit ve svých elektrických vlastnostech. Výrobci hardwaru si toho jsou vědomi a zveřejňují specifikace výkonu svých těžebních strojů na základě dolní hranice jejich tolerance. Jinými slovy, výrobci znají frekvenci, která nejlépe funguje pro průměrné čipy, a tuto frekvenci používají jednotně pro všechny čipy ve stroji.
Toto stanovuje horní limit pro hash rate, kterého může stroj dosáhnout. Autotuning je proces, při kterém algoritmy vyhodnocují optimální frekvence pro hashování jednotlivých čipů, místo aby byl celý stroj považován za jednotnou jednotku. To znamená, že čip vyšší kvality, který dokáže provést více hashů za sekundu, dostane vyšší frekvenci, a čip nižší kvality, který dokáže provést relativně méně hashů, dostane nižší frekvenci. Autotuning na úrovni čipů je v podstatě způsob, jak optimalizovat výkon ASIC prostřednictvím softwaru a firmware, který na něm běží.
Výsledkem je vyšší hash rate na watt elektrické energie, což znamená větší ziskové marže pro těžaře. Důvodem, proč stroje nejsou distribuovány s tímto typem softwaru, je to, že variabilita strojů je nežádoucí, protože zákazníci chtějí přesně vědět, co kupují, takže je špatný nápad, aby výrobci prodávali produkt, který nemá konzistentní a předvídatelný výkon z jednoho stroje na druhý. Kromě toho vyžaduje autotuning na úrovni čipů značné vývojové zdroje, jelikož je složité jej implementovat. Výrobci již vynakládají mnoho zdrojů na vývoj vlastních firmware. Existují softwarová řešení, která umožňují autotuning, jako například Braiins OS+. Kromě toho zlepšují výkon ASIC až o 20 %.

# Závěr

<partId>fa42ec0b-b1fd-47f6-8268-6eab684c1d2b</partId>

## Zhodnoťte tento kurz

<chapterId>6af13742-df68-5cf4-b7aa-93dc0c2eaae9</chapterId>
<isCourseReview>true</isCourseReview>

## Závěrečná zkouška

<chapterId>f51a7c88-3b7e-48df-b45f-22bb10fe619f</chapterId>
<isCourseExam>true</isCourseExam>

## Závěr

<chapterId>2941f29a-d6ce-4a3c-b61b-6e399f5395b1</chapterId>
Gratulujeme k dokončení tohoto kurzu!

Jsme rádi, že jste dosáhli tohoto důležitého milníku ve své vzdělávací cestě.

Díky vaší oddanosti a závazku jste získali cenné znalosti a dovednosti, které vám poslouží ve vašem profesním rozvoji.

Pro další hluboké zkoumání světa Bitcoinu vás zveme k objevování všech dalších kurzů dostupných na Plan ₿ Network:

#### Objevte Bitcoin a jeho základy s

https://planb.network/courses/btc101

#### Objevte Lightning Network s

https://planb.network/courses/lnp201

#### Ovládněte principy soukromí na Bitcoinu

https://planb.network/courses/btc204

#### Objevte historii původu Bitcoinu s

https://planb.network/courses/his201

#### Pochopte, jak funguje Bitcoin peněženka s

https://planb.network/courses/cyp201
