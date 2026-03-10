---
name: Bitaxe Open Source Mining Mistrovství
goal: Ovládněte celý ekosystém Bitaxe, od sestavení hardwaru až po pokročilé přizpůsobení a optimalizaci výkonu
objectives: 

  - Pochopení filozofie open source hardwaru Bitcoin mining
  - Sestavení zařízení Bitaxe mining od nuly
  - Konfigurace a optimalizace softwaru mining včetně AxeOS a Public Pool
  - Implementace pokročilých optimalizací výkonu včetně přetaktování a benchmarkingu

---

# Váš průvodce Bitaxe Mining


Vítejte v komplexním kurzu Bitaxe, kde si osvojíte revoluční open source hardware Bitcoin mining, který demokratizuje přístup k technologii mining. Tento kurz vás provede od pochopení filozofických základů decentralizovaného systému mining až po pokročilé techniky přizpůsobení hardwaru a optimalizace výkonu.


Projekt Bitaxe představuje změnu paradigmatu v oblasti Bitcoin mining, neboť prolamuje monopol proprietárních výrobců ASIC tím, že poskytuje plně otevřené návrhy, firmware a software. Prostřednictvím těchto praktických kapitol získáte praktické dovednosti v oblasti osazování hardwaru, konfigurace softwaru, návrhu desek plošných spojů a optimalizace výkonu.


Předchozí zkušenosti s mining nejsou nutné, ale základní znalosti elektroniky a znalost GitHubu budou užitečné. Kurz vás promění ze zvědavého pozorovatele ve schopného tvůrce a přispěvatele systému Bitaxe.

Poznámka: Videa k tomuto kurzu jsou dostupná pouze v angličtině.

+++


# Úvod


<partId>6b3cd9f0-0063-40f0-a7bb-00a48f330d88</partId>


## Přehled kurzů


<chapterId>1fac9579-0e1c-48e3-9bc5-e7a2960018c8</chapterId>


Vítejte na kurzu MIN 306 _**Bitaxe Open Source Mining Mastery**_, který je komplexní cestou do světa Bitaxe mining. Tento kurz je určen těm, kteří chtějí pochopit, sestavit a optimalizovat vlastní hardware Bitaxe mining a zároveň prozkoumat filozofické a technické základy, díky nimž je tento projekt v rámci ekosystému Bitcoin jedinečný.


### Porozumění systému Bitaxe


V první části jsou položeny základní základy: dozvíte se o původu projektu Bitaxe, jeho vývoji a hodnotách decentralizace a transparentnosti, které jej definují. Dozvíte se, co to vlastně Bitaxe je, jak se liší od proprietárních ASIC a kde najít komunitní zdroje pro prohloubení svých znalostí. Tato část poskytuje kontext potřebný k pochopení toho, proč Bitaxe představuje zlomový bod v historii Bitcoin mining.


### Software a provoz


Druhá část se zaměřuje na softwarové prostředí a podrobně představuje *AxeOS*: operační systém s otevřeným zdrojovým kódem navržený speciálně pro zařízení Bitaxe. Seznámíte se s jeho hlavními funkcemi a dozvíte se, jak zařízení nakonfigurovat a jak s ním komunikovat, abyste mohli zahájit první provoz mining.


### Společenství a spolupráce


Třetí oddíl zdůrazňuje aspekt spolupráce v rámci projektu. Seznámíte se s filozofií open-source, která se uplatňuje při vývoji hardwaru i softwaru Bitaxe. Prostřednictvím praktických cvičení se naučíte, jak přímo přispívat do zdrojového kódu, a objevíte také _Public Pool_, komunitní platformu pro sdružování výpočetního výkonu. Dozvíte se také, jak ji nainstalovat na uzel Umbrel pro místní a suverénní integraci.


### Montáž hardwaru a řešení problémů


Ve čtvrté části se ponoříte do samotného hardwaru. Dozvíte se, jak identifikovat nástroje potřebné k sestavení Bitaxe, vyřešit problémy s pájením a provést kompletní diagnostiku pomocí *AxeOS* a nástrojů USB. Tato část klade důraz na praktické procvičování a hluboké pochopení vzájemné interakce hardwarových a softwarových komponent.


### Pokročilé přizpůsobení


Pátá část je věnována přizpůsobení. Dozvíte se, jak upravit desku plošných spojů (PCB), vytvořit tovární soubor a používat _Bitaxe Web Flasher_. Tato část je určena těm, kteří chtějí jít nad rámec jednoduchého osazení a skutečně navrhnout vlastní verzi zařízení na míru.


### Optimalizace výkonu


A konečně šestá část se zabývá pokročilými optimalizačními technikami. Dozvíte se, jak provést benchmark počítače Bitaxe, abyste vyhodnotili jeho výkon, a jak jej efektivně přetaktovat. Tyto dovednosti vám pomohou vytěžit z vašeho hardwaru maximum při respektování jeho fyzických omezení.


Stejně jako u každého kurzu v Akademii Plan ₿ obsahuje závěrečná část hodnocení, jehož cílem je upevnit vaše znalosti.


Ponořte se do tohoto technického dobrodružství - budoucnost Bitcoin mining je ve vašich rukou!


# Porozumění systému Bitaxe

<partId>ba1cb4ea-6a77-54fd-916c-57285c8c2418</partId>


## Historie

<chapterId>73d928e5-72f0-5c17-a7a6-8b6ece7f9a30</chapterId>

:::video id=67d2529a-b7cb-4804-b02c-e56c12c9e66e:::

Projekt Bitaxe představuje průlomový posun ve vývoji hardwaru Bitcoin [mining](https://planb.academy/resources/glossary/mining) a přináší principy open source do odvětví, kterému dominují proprietární řešení. Tato vzdělávací série se zabývá komplexní historií, technickými inovacemi a komunitou řízeným vývojem projektu Bitaxe a poskytuje vhled do toho, jak se vize jednoho inženýra proměnila v prosperující ekosystém decentralizovaného hardwaru mining. Prostřednictvím zkoumání původu projektu, jeho výzev a úspěchů získáme cenné poznatky jak o technické složitosti vývoje [ASIC](https://planb.academy/resources/glossary/asic), tak o síle spolupráce v oblasti Bitcoin na bázi open source.


### Příběh o původu: Od objevu hedvábné stezky k vizi solárního Mining


Skot, zakladatel společnosti Bitaxe, začal svou cestu ke Bitcoin na vysokoškolském večírku, kde se o Bitcoin poprvé dozvěděl od někoho, kdo nakupoval zboží na Hedvábné stezce. Toto počáteční seznámení s Bitcoin za přibližně 20 dolarů za minci podnítilo zvědavost, která se později vyvinula v revoluční projekt mining. Technické základy jeho budoucí práce vznikly během jeho studia na univerzitě, kde měl přístup k rozsáhlým prostředkům FPGA v laboratorním prostředí. Ve spolupráci se svým nadřízeným začal Skot experimentovat s open source bitovými proudy FPGA pro Bitcoin mining, zpočátku se skromným cílem, aby mining stačil Bitcoin na nákup pizzy do jejich kanceláře.


Přechod od akademického experimentování k serióznímu vývoji nastal o několik let později, když Skot pracoval na solárně napájených branách pro dálkový sběr dat v Africe. Tato profesionální zkušenost se solárními napájecími systémy vedla k poznání, že ASIC Bitcoin mining, který je v podstatě nízkonapěťovým stejnosměrným zařízením, by se skvěle hodil k solárním panelům. Tento koncept se zdál přirozený a elegantní. Když však Skot začal zkoumat existující řešení, objevil na trhu významnou mezeru: na rozdíl od počátků Bitcoin mining, kdy byly návrhy FPGA otevřeně k dispozici, se s nástupem ASIC průmysl posunul směrem ke zcela proprietárním, uzavřeným řešením.


Nedostatek otevřeného hardwaru mining se stal pro Skota důvodem k frustraci, zejména vzhledem k jeho zkušenostem s vývojem softwaru s otevřeným zdrojovým kódem a jeho přesvědčení, že otevřený zdrojový kód Bitcoin by se měl vztahovat i na infrastrukturu mining. Tento filozofický soulad s principy open source v kombinaci s technickou výzvou reverzního inženýrství proprietárních návrhů ASIC připravil půdu pro to, co se stalo projektem Bitaxe. Původní vize byla ambiciózní a zároveň praktická: vytvořit solárně poháněný [těžař](https://planb.academy/resources/glossary/miner) Bitcoin, který by mohl pracovat samostatně, aniž by k ovládání potřeboval samostatný počítač, což by bylo vhodné pro nasazení na vzdálených místech pod solárními panely.


### Technické výzvy a průlomy v reverzním inženýrství


Vývoj Bitaxe vyžadoval překonání značných technických překážek, které se soustředily především na naprostou absenci dokumentace čipů ASIC společnosti Bitmain. Skotův přístup k této výzvě byl příkladem odhodlání a vynalézavosti, které jsou pro úspěšné reverzní inženýrství nezbytné. Bez přístupu k oficiálním datovým listům nebo technickým specifikacím se uchýlil ke zkoumání čipů pod mikroskopy, měření roztečí pinů pomocí třmenů a dokonce ke skenování čipů, aby zjistil jejich přesné požadavky na rozměry. Výsledkem tohoto náročného procesu bylo několik neúspěšných prototypů, přičemž první dvě iterace "denního horníka" nefungovaly správně kvůli nesprávným výpočtům rozměru patice.


Průlom přišel s třetí iterací v květnu 2022, kdy Skot úspěšně vytvořil funkční dvoučipový návrh s použitím čipů BM1387 získaných z jednotek Antminer S9. Tento úspěch znamenal zrod názvu Bitaxe, inspirovaného konceptem krumpáče pro Bitcoin mining. Úspěch tohoto návrhu potvrdil přístup reverzního inženýrství a ukázal, že nezávislí vývojáři mohou vytvořit funkční hardware mining bez podpory výrobce. Technické výzvy však přesahovaly rámec propojení čipů a zahrnovaly i složitý návrh napájení, protože ASIC vyžadovaly přesnou regulaci napětí při vysokých proudech, často pracovaly s napětím pouhých 0,6 V a zároveň odebíraly značný proud.


Vývoj firmwaru představoval další vrstvu složitosti, protože projekt vyžadoval vytvoření softwaru mining, který by mohl běžet přímo na mikrokontroléru ESP32 a nespoléhal se na externí počítače se softwarem, jako je CGMiner. Tento samostatný přístup byl nezbytný pro Skotovu vizi nasaditelných, nezávislých jednotek mining. Kombinace reverzního inženýrství hardwaru a vývoje vestavěného firmwaru vytvořila komplexní technickou výzvu, která vyžadovala odborné znalosti z více oborů, od elektrotechniky a návrhu desek plošných spojů až po vestavěné programování a síťové protokoly.


### Vytváření komunit a spolupráce v oblasti otevřeného softwaru


Přeměna Bitaxe ze samostatného projektu na prosperující komunitní iniciativu představuje jeden z nejvýznamnějších aspektů jeho úspěchu. Zpočátku se Skotovy pokusy o získání zájmu generate prostřednictvím fór Bitcoin a sociálních médií setkávaly s omezenou odezvou a občasnou skepsí. Průlom nastal, když členové komunity jako SirVapesAlot rozpoznali potenciál open source mining a založili server Open Source Miners United (OSMU) Discord. Tato platforma poskytla prostředí pro spolupráci nezbytné pro rozkvět projektu a přilákala přispěvatele z různých prostředí, kteří měli společný zájem na demokratizaci technologie Bitcoin mining.


Model vývoje řízeného komunitou se ukázal jako pozoruhodně efektivní, protože se objevili klíčoví přispěvatelé jako johnny9 a Ben, kteří řešili konkrétní technické problémy. Johnny9 díky svým odborným znalostem v oblasti vývoje firmwaru vyřešil kritické problémy s implementací softwaru, zatímco Ben díky svým dovednostem v oblasti vývoje front-endu vytvořil intuitivní ovládací panel AxeOS, který zjednodušil konfiguraci a monitorování zařízení. Mezi Benovy další příspěvky patřilo vytvoření výrobních kapacit a vytvoření Public Pool, open source [fondu mining](https://planb.academy/resources/glossary/pool-mining) optimalizovaného pro zařízení Bitaxe. Tento společný přístup ukázal, jak mohou principy open source urychlit vývoj nad rámec toho, čeho by mohl dosáhnout každý jednotlivý přispěvatel sám.


Komunita OSMU také podporovala inkluzivní prostředí, kde se noví uživatelé mohli učit a přispívat bez ohledu na své počáteční technické znalosti. Benova vlastní cesta od pájecího nováčka k významnému výrobci je příkladem tohoto vstřícného přístupu k rozvoji dovedností. Závazek komunity ke vzdělávání a vzájemné podpoře vytvořil pozitivní cyklus, v němž zkušení členové mentorovali nováčky, kteří se pak sami stali přispěvateli. Tento model se ukázal jako zásadní pro rozšíření projektu nad jeho původní rozsah a vytvoření udržitelného ekosystému pro další inovace a růst.


### Vize decentralizovaného systému Mining a budoucí dopady


Skotova dlouhodobá vize pro Bitaxe sahá mnohem dále než k vytvoření dalšího zařízení mining: jde o zásadní transformaci prostředí Bitcoin mining. Ambiciózní cíl vyrobit milion těžařů s jedním terahem by vytvořil exahash distribuované energie mining, což by představovalo významný krok směrem k decentralizaci mining. Tato vize řeší kritické obavy z centralizace mining, kdy by velké pooly a průmyslové provozy mohly potenciálně podléhat tlaku vlády nebo regulačnímu záboru. Distribucí energie mining mezi nespočet domácích těžařů se síť stává odolnější a je v souladu s decentralizovanými principy Bitcoin.


Ekonomický model podporující tuto vizi se opírá o jedinečné vlastnosti domácího mining, kde jsou náklady na infrastrukturu v podstatě nulové a těžaři mohou pracovat s minimálním dohledem. Na rozdíl od průmyslových provozů mining, které vyžadují masivní kapitálové investice do zařízení, energetické infrastruktury a chladicích systémů, mohou domácí těžaři jednoduše zapojit zařízení do stávajících elektrických zásuvek a internetových připojení. Tento přístup by teoreticky mohl přinést značnou [míru hašování](https://planb.academy/resources/glossary/hashrate) online bez tradičních překážek vstupu, které charakterizují rozsáhlé operace mining.


Úspěch projektu již začal ovlivňovat širší ekosystém Bitcoin mining a má potenciál inspirovat další výrobce k přijetí modelů vývoje s otevřeným zdrojovým kódem. Finanční životaschopnost, kterou výrobci Bitaxe prokázali, dokazuje, že open source hardware může být komerčně úspěšný při zachování transparentnosti a zapojení komunity. Vzhledem k tomu, že se projekt nadále vyvíjí s novými integracemi čipů, vylepšenými návrhy a rozšířenými výrobními partnerstvími, slouží jako důkaz konceptu, jak se Bitcoin mining může vrátit ke svým decentralizovaným kořenům a zároveň přijmout moderní technologii ASIC. Konečný cíl přesahuje pouhou distribuci hash rate a zahrnuje i vzdělávací dopad, který přivádí více lidí do přímého kontaktu se základním procesem Bitcoin mining a podporuje hlubší pochopení bezpečnostního modelu sítě.


## Co je to Bitaxe?

<chapterId>6a56af56-35ce-51af-999b-4bc7305e6464</chapterId>

:::video id=12b26c7a-74b1-4ea9-afc0-e3ef90cf5837:::

### Přehled hardwaru a možností


Ekosystém Bitaxe zahrnuje několik iterací hardwaru, z nichž každá je navržena tak, aby optimalizovala různé aspekty zážitku z používání mining při zachování základní filozofie přístupnosti s otevřeným zdrojovým kódem. Tato zařízení slouží nejen jako funkční hardware mining, ale také jako vzdělávací nástroje, které uživatelům umožňují pochopit složitý vztah mezi čipy ASIC, mikrokontroléry a procesem Bitcoin mining. Pochopení filozofie návrhu a technické realizace zařízení Bitaxe poskytuje cenné poznatky o fungování moderního hardwaru mining na úrovni komponent i systému.



### Bitaxe Max, implementace první generace


Bitaxe Max představuje základní implementaci konceptu Bitaxe, která využívá čip BM1397 ASIC původně vyvinutý společností Bitmain pro řadu S17 mining. Tato integrace čipu demonstruje, jak může open-source hardware znovu využít stávající technologii ASIC k vytvoření dostupných řešení mining. Bitaxe Max poskytuje odhadovanou rychlost hašování mezi 300 až 400 gigahash za sekundu, což jej staví spíše do pozice vzdělávací a experimentální platformy mining než komerčního řešení.


Integrace čipu BM1397 do počítače Bitaxe Max vyžadovala pečlivé zvážení správy napájení, řízení teploty a komunikačních protokolů. Konstrukce desky vyhovuje specifickým požadavkům tohoto ASIC a zároveň poskytuje nezbytné podpůrné obvody pro stabilní provoz. Tato implementace je ukázkou toho, jak může vývoj hardwaru s otevřeným zdrojovým kódem využít stávající polovodičovou technologii k vytvoření nových aplikací a možností vzdělávání v rámci komunity mining.


### Bitaxe Ultra, pokročilá technologie čipů


Bitaxe Ultra představuje evoluci platformy Bitaxe, která obsahuje pokročilejší čip BM1366 ASIC z řady S19 společnosti Bitmain. Tato novější čipová technologie přináší platformě Bitaxe lepší účinnost a výkonnostní charakteristiky při zachování stejné základní filozofie návrhu. Upgrade na čip BM1366 demonstruje přizpůsobivost platformy a závazek komunity začlenit technologický pokrok do open-source řešení mining.


Přechod z čipu BM1397 na BM1366 si vyžádal úpravy systémů napájení, řízení teploty a řídicích algoritmů desky. Tyto změny ilustrují iterativní povahu vývoje hardwaru a důležitost zachování kompatibility při současném zvyšování výkonu. Implementace Bitaxe Ultra poskytuje uživatelům přístup k novější technologii ASIC a zároveň zachovává vzdělávací a experimentální charakter platformy.


### Mikrokontroléry a komunikační systémy


Srdcem každého zařízení Bitaxe je mikrokontrolér ESP, který slouží jako hlavní rozhraní mezi uživatelem a čipem ASIC. Na tomto mikrokontroléru běží specializovaný software vyvinutý komunitou Open Source Miners United (OSMU), který umožňuje přesnou kontrolu nad provozními parametry ASIC. Komunikace mezi mikrokontrolérem a čipem ASIC probíhá prostřednictvím pečlivě navržených sériových komunikačních linek, které jsou vyleptány přímo na desce plošných spojů jako viditelné stopy.


Úloha mikrokontroléru přesahuje rámec jednoduchého ovládání ASIC: zahrnuje správu napájení, monitorování teploty a funkce uživatelského rozhraní. Prostřednictvím integrovaného displeje mohou uživatelé sledovat kritické provozní parametry, jako je teplota, rychlost hash, IP adresa a další důležité statistiky mining. Tento systém zpětné vazby v reálném čase poskytuje cenné informace o výkonu zařízení a pomáhá uživatelům optimalizovat provoz mining a zároveň se dozvídat o základním chování hardwaru.


### Správa napájení a bezpečnostní aspekty


Platforma Bitaxe pracuje s přísnými požadavky na napájení 5 V, takže správný výběr zdroje napájení je pro životnost a bezpečnost zařízení zásadní. Systém řízení napájení na deskách Bitaxe zahrnuje sofistikované obvody navržené tak, aby regulovaly dodávku napětí do čipu ASIC a zároveň monitorovaly spotřebu energie v různých provozních režimech. Tato schopnost řízení napájení umožňuje zařízení efektivně pracovat v celém rozsahu vnitřních frekvencí a napětí, přičemž spotřeba se obvykle pohybuje mezi 5 až 25 watty v závislosti na konfiguraci.


Pochopení požadavků na napájení se stává klíčovým, když uvážíme, že nesprávné použití napětí může zařízení trvale poškodit. Vztah mezi frekvencí, napětím, spotřebou energie a rychlostí hash ukazuje základní principy fungování ASIC, které platí pro veškerý hardware mining. Uživatelé mohou experimentovat s různými nastaveními napájení, aby pochopili kompromisy v účinnosti, které jsou vlastní provozu mining, a získali praktické zkušenosti s koncepty, které se uplatní při implementacích mining ve větším měřítku.


### Sólo Mining Zaměření a účast v síti


Platforma Bitaxe se zaměřuje zejména na samostatné aplikace mining, kdy se jednotliví těžaři snaží řešit [bloky](https://planb.academy/resources/glossary/block) Bitcoin samostatně, místo aby se účastnili velkých poolů mining. Ačkoli rychlost hashování zařízení Bitaxe činí úspěšné objevení bloku statisticky nepravděpodobným, slouží tento přístup k důležitým vzdělávacím a filozofickým účelům v rámci komunity Bitcoin. Sólo mining se zařízeními Bitaxe pomáhá uživatelům pochopit základní mechaniku systému Bitcoin a zároveň přispívá k decentralizaci sítě.


Důraz na sólo mining odráží závazek komunity OSMU podporovat individuální účast na bezpečnostním modelu Bitcoin. Poskytnutím dostupného hardwaru, který může pracovat samostatně, umožňuje platforma Bitaxe uživatelům provozovat vlastní operace mining bez závislosti na infrastruktuře poolu. Tento přístup podporuje hlubší pochopení [konsensuálního](https://planb.academy/resources/glossary/consensus) mechanismu Bitcoin a zároveň podporuje decentralizovanou povahu sítě díky větší rozmanitosti těžařů.


### Vývoj hardwaru a zlepšení výroby


Platforma Bitaxe se neustále vyvíjí na základě zpětné vazby od komunity a optimalizace výroby, přičemž novější verze obsahují vylepšení, která zvyšují vyrobitelnost a uživatelský komfort. Aktualizace verzí se obvykle zaměřují spíše na efektivitu výroby než na zásadní změny výkonu, což zajišťuje, že stávající uživatelé nebudou čelit tlaku na zastarávání. Funkce, jako je přechod z konektorů micro-USB na USB-C a vylepšené systémy připojení napájení, odrážejí pozornost komunity věnovanou praktickému zlepšení použitelnosti.


Tento evoluční přístup ukazuje výhody vývoje hardwaru s otevřeným zdrojovým kódem, kdy příspěvky komunity vedou k postupnému zlepšování, z něhož mají prospěch všichni uživatelé. Filozofie "if it hashes, it hashes" zdůrazňuje zaměření platformy na funkčnost namísto neustálých aktualizací a podporuje uživatele, aby svá zařízení udržovali a provozovali spíše než aby se snažili získat nejnovější verze. Tento přístup podporuje udržitelné hardwarové postupy a zároveň zachovává vzdělávací hodnotu Bitaxe.


## Kde se mohu dozvědět více?

<chapterId>706f2fff-fa1c-5d8e-b14c-ece6e42c016f</chapterId>

:::video id=90088397-3a16-485f-bbd2-89cdbb844e4a:::

Projekt Bitaxe představuje komplexní iniciativu mining s otevřeným zdrojovým kódem, která dalece přesahuje rámec jednoho zařízení. Pro každého, kdo se chce zapojit do tohoto ekosystému, je zásadní pochopit, kde najít spolehlivé informace, technické zdroje a podporu komunity. Tato kapitola poskytuje kompletního průvodce základními platformami a zdroji, které tvoří základ komunity Bitaxe a Open Source Miners United (OSMU).


### Bitaxe.org, centrální centrum


Webové stránky Bitaxe.org slouží jako hlavní brána ke všem informacím a zdrojům souvisejícím s projektem. Tato centralizovaná platforma slouží jako první referenční bod, kdykoli se potřebujete dozvědět něco o zařízeních Bitaxe nebo prozkoumat další projekty v rámci komunity OSMU. Design webu upřednostňuje přístupnost a uspořádání a představuje návštěvníkům pečlivě vybrané odkazy, které odkazují na různé specializované zdroje v celém ekosystému.


Význam tohoto centrálního uzlu nelze přeceňovat, protože odstraňuje zmatek, který často provází decentralizované projekty s otevřeným zdrojovým kódem. Namísto hledání na více platformách nebo spoléhání se na potenciálně zastaralé informace z neoficiálních zdrojů mohou uživatelé důvěřovat webu Bitaxe.org, který poskytuje aktuální a ověřené odkazy na všechny důležité zdroje. Tento přístup zajišťuje, že jak nováčci, tak zkušení členové komunity mohou efektivně vyhledat konkrétní informace, které potřebují pro své projekty.


### Technické zdroje a vývojové materiály


Úložiště souborů návrhu hardwaru na GitHubu představuje jeden z nejcennějších zdrojů pro všechny, kteří se zajímají o pochopení nebo konstrukci zařízení Bitaxe. Toto veřejné úložiště obsahuje komplexní dokumentaci, která pokrývá všechny aspekty procesu návrhu hardwaru, od počátečních konceptů až po konečné výrobní specifikace. Úložiště obsahuje podrobné obrázky, cíle projektu, popisy funkcí a vysvětlení vestavěných komponent, které poskytují technickou hloubku i praktické pokyny.


Zájemci o výrobu vlastních zařízení mohou v úložišti najít konkrétní dokumentační soubory, jako je například soubor building.md, který obsahuje pokyny krok za krokem pro celý výrobní proces. Tato dokumentace zahrnuje softwarové nástroje potřebné pro návrh desek plošných spojů, postupy pro odesílání souborů výrobcům a kroky spojené s příjmem a validací vyrobených desek plošných spojů. Tato úroveň podrobností zajišťuje, že jednotlivci nebo malé organizace mohou úspěšně projít výrobním procesem i bez rozsáhlých předchozích zkušeností s výrobou hardwaru.


Úložiště ESP-Miner slouží jako centrální místo pro veškerý kód a dokumentaci související s firmwarem. Tento repozitář GitHub obsahuje každý řádek kódu napsaný pro firmware Bitaxe spolu s komplexní dokumentací, která vysvětluje systémové požadavky, specifikace hardwaru a možnosti konfigurace. Struktura úložiště je navržena tak, aby vyhovovala jak uživatelům, kteří dávají přednost předkompilovaným binárním souborům, tak vývojářům, kteří chtějí firmware sestavit ze zdrojového kódu.


Dokumentace v tomto úložišti obsahuje podrobné části o požadavcích na hardware, možnostech předkonfigurace a doporučených hodnotách různých nastavení. Tyto informace jsou neocenitelné pro uživatele, kteří chtějí přizpůsobit svá zařízení nebo řešit konkrétní problémy. Úložiště navíc obsahuje informace o novějším vývoji, například o integraci systému Raspberry Pi, což zajišťuje, že dokumentace zůstává aktuální s probíhajícím vývojem projektu.


### Nástroje pro správu a údržbu zařízení


Webový blesk Bitaxe představuje praktické řešení pro údržbu a aktualizace zařízení. Tento webový nástroj umožňuje uživatelům flashovat firmware do svých zařízení, aniž by k tomu potřebovali specializovaný software nebo složité postupy příkazového řádku. Flasher podporuje více variant zařízení, včetně Bitaxe Ultra s různými verzemi portů a starších modelů Bitaxe Max. Uživatelé si mohou vybrat mezi aktualizací stávajícího firmwaru prostřednictvím webového rozhraní nebo provedením kompletního továrního resetu pomocí připojení USB.


Tento nástroj řeší jeden z nejčastějších problémů, se kterým se potýkají hardwaroví nadšenci: údržbu a aktualizaci firmwaru zařízení. Díky uživatelsky přívětivému webovému rozhraní flasher odstraňuje mnoho technických překážek, které by jinak mohly uživatelům bránit v udržování aktuálního firmwaru jejich zařízení. Návrh nástroje upřednostňuje jednoduchost při zachování flexibility potřebné pro různé konfigurace zařízení a scénáře aktualizací.


### Komunitní platformy a komunikační kanály


Server Discord představuje srdce interakce a podpory komunity v reálném čase v rámci ekosystému Bitaxe. Organizace serveru odráží různorodé zájmy a potřeby členů komunity, přičemž pečlivě strukturované kanály usnadňují cílené diskuse o konkrétních tématech. Noví členové se setkávají s ověřovacím procesem, který vyžaduje přečtení a přijetí pravidel komunity, což zajišťuje, že všichni účastníci chápou očekávání respektující a produktivní interakce.


Struktura kanálů serveru zahrnuje obecné diskusní oblasti zahrnující témata, jako je integrace solární energie, bazény mining a diskuse týkající se Bitcoin. Specializovanější sekce se zaměřují na konkrétní zařízení, včetně vyhrazených kanálů pro varianty Bitaxe Ultra, Hex a Supra. Kanál firmwaru poskytuje cílený prostor pro technické diskuse o vývoji softwaru a řešení problémů, zatímco kanál oficiálních verzí zajišťuje, že členové komunity dostávají včasná oznámení o novém vývoji.


Jeho součástí je také předplatitelská zóna, která poskytuje další výhody členům komunity, kteří se rozhodnou projekt finančně podpořit. Tento odstupňovaný přístup umožňuje komunitě nabízet rozšířené služby a zároveň zachovat otevřený přístup k základním informacím a podpůrným kanálům. Kanál nápovědy slouží jako vyhrazený prostor pro řešení problémů a technickou pomoc, což zajišťuje, že uživatelé mohou při potížích získat rychlou podporu.



Wiki Open Source Miners United (osmu.wiki) poskytuje komplexní dokumentaci, která doplňuje diskuse probíhající v reálném čase na Discordu. Na rozdíl od chatovacích platforem nabízí wiki strukturovanou dokumentaci s možností vyhledávání, která pokrývá všechny aspekty projektu Bitaxe a souvisejících iniciativ. Způsob jejího uspořádání odráží strukturu projektu, obsahuje specializované sekce pro různé řady zařízení a komplexní průvodce nastavením.


Otevřený zdrojový kód wiki umožňuje členům komunity přispívat přímo do dokumentace. Uživatelé mohou upravovat stránky, zadávat opravy a přidávat nové informace prostřednictvím integrace s GitHubem, což zajišťuje, že znalostní báze zůstává aktuální a transparentní. Tento přístup založený na spolupráci využívá kolektivní odborné znalosti komunity a zároveň zachovává kontrolu kvality prostřednictvím procesu revize zadaných změn.


Wiki obsahuje praktické zdroje, například průvodce nastavením ve formátu PDF, které poskytují pokyny krok za krokem pro konfiguraci a používání zařízení. Tyto příručky slouží jako cenné odkazy pro nové uživatele i zkušené členy komunity, kteří potřebují rychlý přístup ke konkrétním postupům nebo podrobnostem konfigurace.


### Informace o nákupu a prodejcích


Legitimní seznam Bitaxe řeší zásadní potřebu komunity open-source hardwaru: identifikovat důvěryhodné prodejce a vyhnout se podvodným prodejcům. Tento kurátorský seznam zahrnuje ověřené prodejce a výrobce, kteří splňují specifická kritéria legitimity a podpory komunity. Každý seznam obsahuje přímé odkazy na webové stránky prodejců, regionální informace a popisy společností, které uživatelům pomáhají činit informovaná rozhodnutí o nákupu.


Důležité je, že v seznamu je uvedeno, zda každý prodejce přispívá zpět komunitě OSMU, ať už finančně nebo jinými formami podpory. Tato transparentnost pomáhá členům komunity pochopit, kteří prodejci aktivně podporují rozvoj a udržitelnost projektu. Seznam také slouží jako ochranné opatření proti běžným podvodům, jako jsou neoprávněné předobjednávky nevydaných produktů, které v minulosti způsobovaly v komunitě problémy.


Důraz na nepropojené odkazy je důkazem snahy komunity poskytovat nestranná doporučení prodejců. Uživatelé mohou věřit, že doporučení jsou založena na legitimitě prodejců a přínosu komunity, nikoli na finančních pobídkách, což zajišťuje, že nákupní rozhodnutí podporují jak individuální potřeby, tak udržitelnost komunity.



# Software a provoz

<partId>04b302a9-42ba-5ad4-834c-6979950c2948</partId>


## Co je AxeOS?

<chapterId>a0cdf10d-e007-58e2-a17b-b588fd393b5e</chapterId>

:::video id=de7bcbf2-f9ac-4057-ad40-29dc223b4798:::

AxeOS je firmware a webové rozhraní pro zařízení Bitaxe mining, které uživatelům poskytuje kompletní možnosti ovládání a monitorování prostřednictvím intuitivního ovládacího panelu v prohlížeči. Tento systém mění složitý úkol správy zařízení ASIC v přístupný zážitek a umožňuje těžařům sledovat výkon, upravovat nastavení a spravovat více zařízení z jediného rozhraní. Porozumění systému AxeOS je nezbytné pro maximalizaci potenciálu zařízení Bitaxe a udržení optimálního provozu mining.


### Přehled přístrojového panelu a základní metriky


Přístrojový panel AxeOS slouží jako hlavní okno do výkonnosti zařízení Bitaxe a zobrazuje kritické metriky mining v uspořádaném formátu v reálném čase. Když přejdete na IP adresu zařízení Bitaxe, okamžitě se vám zobrazí čtyři klíčové ukazatele výkonnosti, které definují aktuální stav provozu mining. Zobrazení hash rate ukazuje skutečnou výpočetní rychlost, kterou váš čip ASIC produkuje při zpracování aktuální blokové šablony, a poskytuje tak okamžitou zpětnou vazbu o základní funkčnosti vašeho zařízení.


Vedle rychlosti hashování sleduje počítadlo podílů každé platné řešení, které vaše zařízení Bitaxe odešle do fondu mining. S každým úspěšným odesláním se zvyšuje a slouží jako přímý ukazatel příspěvku vašeho zařízení k úsilí fondu mining. Metrika účinnosti poskytuje zásadní přehled o výkonnosti vašeho zařízení tím, že vypočítává poměr rychlosti hashování a spotřeby energie, což vám pomůže optimalizovat ziskovost vašeho provozu. Ukazatel nejlepší obtížnosti uchovává záznam o nejvyšším podílu obtížnosti, který kdy vaše zařízení nalezlo, a udržuje tento úspěch i při restartech a aktualizacích, resetuje se pouze při provedení úplného továrního flashování.


Rozšiřitelný systém nabídek na přístrojové desce, ovládaný přepínacím tlačítkem, umožňuje přístup ke všem funkcím systému AxeOS při zachování přehledného rozhraní. Graf živého hash rate představuje jednu z nejcennějších funkcí, zobrazuje údaje o výkonu v reálném čase, které jsou tím přesnější a informativnější, čím déle relaci udržujete. Sekce napájení, tepla a výkonu poskytují komplexní sledování provozního stavu vašeho zařízení, včetně varování před vstupním napětím, které vás upozorní na možné problémy s napájením a zároveň zajistí pokračování provozu v rámci bezpečných parametrů.


### Pokročilé monitorování a systémové informace


Monitorovací funkce systému AxeOS dalece přesahují základní sledování hash rate a poskytují podrobný přehled o všech aspektech provozu zařízení Bitaxe. Sekce napájení zobrazuje vypočtenou spotřebu energie odvozenou z integrovaných obvodů na desce, měření vstupního napětí z vašeho napájecího připojení a požadované úrovně napětí ASIC. Pokud dojde k poklesu napětí, systém AxeOS okamžitě zobrazí varovná oznámení, která však obvykle nemají vliv na provoz mining a pouze naznačují potenciální možnosti optimalizace napájení.


Monitorování teploty se zaměřuje na tepelnou správu čipu ASIC, přičemž měření se provádí ze strategických míst na zařízení, aby bylo možné získat přesné tepelné údaje s vhodným posunem pro přesnost na úrovni čipu. Zobrazení frekvence a napětí nabízí zpětnou vazbu v reálném čase o parametrech ladění ASIC, přičemž naměřené napětí představuje nejpřesnější dostupný údaj, který byl pořízen přímo v místě čipu ASIC. Tato přesnost umožňuje jemné doladění výkonnostních parametrů při zachování bezpečných provozních podmínek.


Část Stav připojení poskytuje okamžitý přehled o konfiguraci fondu mining a zobrazuje aktuální adresu URL vrstvy, port a identifikaci uživatele. Pro zařízení připojená k veřejným poolům generuje systém AxeOS praktické rychlé odkazy, které vás přenesou přímo do webového rozhraní vašeho poolu, kde máte přístup k podrobným statistikám, výpisům zařízení a historickým údajům o výkonu. Tato integrace zefektivňuje proces monitorování tím, že propojuje informace na úrovni zařízení a na úrovni bazénu v plynulém pracovním postupu.


### Správa roje a řízení více zařízení


Funkce Swarm představuje řešení společnosti AxeOS pro složitou správu více zařízení Bitaxe v síti, které eliminuje nutnost pamatovat si a navigovat na mnoho IP adres. Tento centralizovaný systém správy umožňuje přidávat zařízení jednoduchým zadáním jejich IP adres, automaticky detekuje aktivní těžaře Bitaxe a začleňuje je do jednotného ovládacího panelu. Po konfiguraci poskytuje Swarm komplexní kontrolu nad celým provozem mining z jediného rozhraní.


Prostřednictvím rozhraní Swarm můžete provádět kritické úlohy správy na více zařízeních současně nebo jednotlivě, včetně změn konfigurace fondu, restartů zařízení, úprav frekvence a monitorování výkonu. Tento centralizovaný přístup výrazně snižuje administrativní režii správy rozsáhlých operací mining a zároveň zajišťuje konzistentní konfiguraci všech zařízení. Systém zachovává identitu jednotlivých zařízení a zároveň poskytuje možnosti kolektivní správy, čímž dosahuje optimální rovnováhy mezi granulární kontrolou a provozní efektivitou.


Na řídicím panelu Swarm je u každého spravovaného zařízení uveden jeho aktuální stav, metriky výkonu a ovládací prvky s rychlým přístupem, což umožňuje rychle reagovat na problémy s výkonem nebo změny konfigurace. Tato funkce se ukazuje jako obzvláště cenná pro těžaře, kteří provozují více zařízení na různých místech, nebo pro ty, kteří často upravují parametry mining na základě tržních podmínek nebo výkonu fondu.


### Správa konfigurace a nastavení systému


Sekce Nastavení systému AxeOS poskytuje komplexní kontrolu nad všemi konfigurovatelnými aspekty zařízení Bitaxe, od síťového připojení až po parametry mining a optimalizaci hardwaru. Konfigurace sítě začíná nastavením Wi-Fi, kde zadáte název sítě a heslo, přičemž systém AxeOS doporučuje jednoslovné názvy sítě bez mezer, aby bylo zajištěno spolehlivé připojení. Systém zvládá kompletní proces konfigurace bezdrátové sítě a umožňuje vzdálenou správu a možnosti monitorování.


Konfigurace Mining se soustředí na nastavení vrstvy, kde zadáváte adresu URL vybraného fondu mining bez předpon protokolů nebo čísel portů, které jsou zpracovány v samostatných polích. Pole stratum user (uživatel) vyhovuje různým požadavkům na pool, podporuje jak adresy Bitcoin pro sólo mining, tak systémy uživatelských jmen pro pool mining s možností připojit identifikátory zařízení pro operace s více zařízeními. Nedávno přidaná funkce stratum password podporuje pooly vyžadující autentizaci, ačkoli většina veřejných poolů funguje bez tohoto požadavku.


Optimalizace hardwaru prostřednictvím nastavení frekvence a napětí jádra představuje nejvýkonnější možnost ladění výkonu systému AxeOS. V závislosti na verzi zařízení a prohlížeči se tato nastavení mohou zobrazovat jako rozbalovací nabídky s přednastavenými konfiguracemi nebo jako otevřená pole umožňující zadávání vlastních hodnot. Výchozí nastavení frekvence 485 MHz a napětí jádra 1200 mV zajišťuje stabilní provoz pro počáteční testování, zatímco pokročilí uživatelé mohou tyto parametry optimalizovat pro dosažení maximálního výkonu nebo účinnosti na základě svých specifických požadavků a provozních podmínek.


### Údržba systému a pokročilé funkce


Systém AxeOS obsahuje sofistikované funkce údržby systému, které jsou navrženy tak, aby udržovaly zařízení Bitaxe v provozu na špičkové úrovni a zároveň poskytovaly diagnostické informace pro řešení problémů a optimalizaci. Aktualizační systém zjednodušuje správu firmwaru tím, že přímo v rozhraní zobrazuje nejnovější dostupnou verzi a poskytuje přímé odkazy ke stažení oficiálních souborů firmwaru. Tato integrace eliminuje nutnost ručně procházet úložiště GitHub nebo spravovat stahování souborů, čímž zjednodušuje proces aktualizace na několik kliknutí.


Aktualizační rozhraní přijímá správně pojmenované soubory firmwaru, konkrétně esp-miner.bin a www.bin, čímž je zajištěna kompatibilita a zabráněno chybám při instalaci. Pro uživatele, kteří mají potíže se standardním aktualizačním procesem, poskytuje AxeOS odkazy na komplexní postupy továrního flashování, které mohou obnovit původní funkčnost zařízení. Tento dvojí přístup vyhovuje jak běžným aktualizacím, tak scénářům obnovy.


Systém protokolování poskytuje přehled o provozu zařízení v reálném čase a zobrazuje podrobné informace o modelech čipů ASIC, době provozu systému, stavu připojení Wi-Fi, dostupné paměti, verzích firmwaru a revizích desek. Tyto protokoly jsou neocenitelné pro vývojáře a pokročilé uživatele, kteří chtějí porozumět chování zařízení, diagnostikovat problémy nebo optimalizovat výkon. Prohlížeč protokolů v reálném čase prezentuje živá provozní data, včetně zpracování [nonce](https://planb.academy/resources/glossary/nonce), výpočtů obtížnosti a parametrů odesílání mining, a nabízí tak bezprecedentní přehled o samotném procesu mining.


Mezi další funkce systému patří ovládání orientace obrazovky pro zařízení používaná ve vlastních skříních, inverze polarity ventilátoru pro specializované konfigurace chlazení a automatické ovládání ventilátoru, které upravuje chlazení na základě teploty ASIC. Manuální řízení otáček ventilátoru zajišťuje přesné řízení chlazení v případech, kdy automatické systémy nesplňují specifické požadavky. Všechny změny konfigurace vyžadují uložení a restart zařízení, aby se projevily, což zajišťuje stabilní provoz a zabraňuje částečným stavům konfigurace, které by mohly ovlivnit výkon mining.



# Společenství a spolupráce

<partId>eed1ce48-6752-5744-91f7-91e4e20ff6b2</partId>


## Přehled příspěvků do otevřených zdrojů

<chapterId>715d026e-cebc-536e-a34e-728f5653b999</chapterId>

:::video id=7298ba19-28d2-4a7c-ac0b-44ad0c4770cf:::

### GitHub a jeho úloha při vývoji softwaru


GitHub představuje zásadní změnu ve způsobu správy a sdílení projektů vývoje softwaru v celosvětové programátorské komunitě. Jako cloudová platforma, která hostuje projekty vývoje softwaru pomocí distribuovaného systému správy verzí Git, umožňuje GitHub vývojářům bezproblémovou spolupráci na projektech bez ohledu na jejich fyzické umístění. Platforma slouží jako technický nástroj i sociální síť pro programátory, kterým umožňuje sledovat změny, slučovat aktualizace, udržovat různé verze svého kódu a přispívat do iniciativ s otevřeným zdrojovým kódem, jako je například projekt BitX od organizace Open Source Miners United.


Síla služby GitHub spočívá ve schopnosti zjednodušit složitý proces společného vývoje. Pokud na jednom projektu pracuje více vývojářů, GitHub poskytuje infrastrukturu pro správu příspěvků, revizi změn, řešení problémů projektu a udržování komplexní dokumentace. Díky tomuto kolaborativnímu přístupu se GitHub stal základní součástí moderních pracovních postupů vývoje softwaru a změnil přístup jednotlivých vývojářů i velkých organizací ke správě projektů a sdílení kódu.


### Navigace ve službě GitHub Interface a struktuře úložiště


Pochopení rozhraní GitHubu začíná poznáním klíčových prvků, které tvoří stránku úložiště. Horní navigační lišta obsahuje několik důležitých sekcí: Kód, Problémy, Žádosti o stažení, Diskuse, Akce, Projekty, Zabezpečení a Přehled. Každá sekce slouží v ekosystému správy projektů k určitému účelu, přičemž sekce Kód zobrazuje skutečné soubory a složky, které tvoří projekt.


Samotná struktura úložiště odráží organizační přístup správců projektu. Některé repozitáře obsahují pouze jediný soubor, třeba jednoduchý shellový skript, zatímco jiné, jako například hardwarový projekt BitX, obsahují množství souborů uspořádaných do adresářů a podadresářů. Název úložiště se objevuje na viditelném místě a slouží jako identifikátor i stručný popis účelu projektu. Mezi základní interaktivní prvky patří tlačítko Watch pro příjem oznámení o aktualizacích úložiště, tlačítko Fork pro vytváření osobních kopií úložiště a tlačítko Star, které funguje jako systém podpory komunity podobný funkci "palec nahoru".


V části O projektu jsou uvedeny zásadní informace o projektu ve zkrácené podobě, včetně jednořádkového popisu, informací o licencích a klíčových údajů o projektu. V případě projektu BitX je v této části uveden jako "open source hardware pro miner ASIC Bitcoin" a je zde uvedena licence GPL 3.0. Pochopení licencí je obzvláště důležité, protože GitHub funguje jako open-source platforma, kde jsou veřejné repozitáře přístupné celé komunitě, ale obsah lze používat a šířit pouze v souladu s pravidly pro dodržování jednotlivých licencí.


### Práce s větvemi a verzemi projektu


Koncept větví představuje jednu z nejmocnějších funkcí služby GitHub pro správu různých verzí a vývojových stop v rámci jednoho projektu. Větev v podstatě vytváří kopii nebo upravenou verzi hlavní kódové základny a umožňuje vývojářům pracovat na konkrétních funkcích, opravách chyb nebo experimentálních změnách, aniž by ovlivnila hlavní vývojovou linii. Hlavní větev obvykle slouží jako výchozí a nejstabilnější verze projektu, zatímco další větve slouží pro různé iterace, fáze testování nebo zcela odlišné varianty produktu.


V hardwarovém projektu BitX existuje více větví pro správu různých verzí a konfigurací hardwaru. Například větev Ultra v2 obsahuje soubory specifické pro tuto hardwarovou iteraci, zatímco větev Super 401 se zaměřuje na implementace využívající čip S21 ASIC pro zvýšení efektivity. Každá větev může být o několik revizí napřed nebo za hlavní větví, což naznačuje rozsah změn a vývojových aktivit. Při zkoumání různých větví si uživatelé všimnou zcela odlišných struktur souborů, dokumentace, a dokonce i vizuálního znázornění, což odráží jedinečné požadavky a specifikace jednotlivých hardwarových variant.


Systém větví zabraňuje zmatkům mezi přispěvateli a uživateli tím, že jasně odděluje různé vývojové cesty. Namísto míchání experimentálních funkcí se stabilními verzemi nebo kombinování různých verzí hardwaru na jednom místě poskytují větve čisté oddělení a zároveň zachovávají možnost začlenit úspěšné změny zpět do hlavní vývojové linie, pokud je to vhodné. Tento organizační přístup zajišťuje, že uživatelé mohou snadno najít konkrétní verzi, kterou potřebují, zatímco vývojáři mohou pracovat na vylepšeních, aniž by narušili hlavní projekt.


### Přispívání prostřednictvím problémů


Sekce Problémy slouží jako hlavní komunikační kanál mezi uživateli a správci projektu pro hlášení problémů, návrhy na zlepšení a dokumentaci chyb. Je však důležité si uvědomit, že sekce Problémy je určena speciálně pro legitimní technické problémy, nikoli pro obecné dotazy nebo žádosti o podporu. Pokud se uživatelé setkají se skutečnými poruchami, neočekávaným chováním nebo identifikují potenciální vylepšení, vytvoření dobře zdokumentovaného problému pomáhá celé komunitě tím, že upozorňuje na problémy, které se mohou týkat více uživatelů.


Efektivní hlášení problémů vyžaduje podrobnou dokumentaci problému, včetně okolností, které k problému vedly, kroků k reprodukci problému a všech relevantních technických detailů. Projekt BitX demonstruje tuto zásadu prostřednictvím různých uzavřených problémů, které ukazují proces řešení od počáteční identifikace problému přes komunitní diskusi až po konečné řešení. Některé problémy vedou k vylepšení hardwaru, například k přidání montážních otvorů pro zvýšení možností chlazení, zatímco jiné mohou být vyřešeny prostřednictvím vzdělávání uživatelů nebo aktualizací softwaru.


Rozlišení mezi otázkami a diskusemi je důležité pro zachování organizované interakce komunity. Zatímco sekce Issues se zaměřuje na konkrétní technické problémy, sekce Discussions poskytuje prostředí podobné fóru pro otázky, nápady a obecné zapojení komunity. Ačkoli se server Discord stal hlavním komunikačním kanálem pro komunitu BitX, sekce GitHub Discussions zůstává k dispozici pro formálnější konverzace nebo konverzace s možností vyhledávání, které těží ze stálé dokumentace a snadného odkazování.


### Porozumění požadavkům na stažení


Požadavky na stažení představují mechanismus, jehož prostřednictvím externí přispěvatelé navrhují změny v úložišti projektu. Když někdo zjistí, že by mohl projekt vylepšit, opravit chybu nebo přidat novou funkci, může vytvořit požadavek na stažení a předložit své změny ke kontrole a případnému začlenění do hlavní kódové základny. Tento proces zajišťuje, že všechny změny projdou kontrolou předtím, než se stanou součástí oficiálního projektu, což udržuje kvalitu kódu a soudržnost projektu a zároveň umožňuje přispívat komunitě.


Pracovní postup pro žádosti o stažení obvykle začíná, když přispěvatel rozdělí úložiště, vytvoří vlastní kopii, ve které může provádět změny, a poté tyto změny odešle zpět do původního projektu prostřednictvím žádosti o stažení. Správci projektu pak mohou navrhované změny zkontrolovat, diskutovat o úpravách s přispěvatelem a nakonec rozhodnout, zda změny sloučí do hlavního projektu. Tento proces společného přezkumu pomáhá udržovat standardy projektu a zároveň podporuje účast komunity a její zlepšování.


Porozumění značkám a verzím přidává další vrstvu do správy projektů a řízení verzí. Značky slouží jako značky na časové ose vývoje a označují konkrétní body, které představují určité verze nebo milníky. V hardwarových projektech, jako je BitX, značky často odpovídají konkrétním číslům modelů nebo revizím hardwaru, což uživatelům poskytuje jasné referenční body pro hledání konkrétních verzí. Vydání, která se častěji používají v softwarových projektech, představují formální distribuce dokončených funkcí a oprav chyb, často doprovázené podrobnými poznámkami k vydání a balíčky ke stažení.


Ekosystém GitHub vytváří komplexní prostředí pro spolupráci v oblasti otevřených zdrojů, které zdaleka přesahuje rámec prostého sdílení souborů. Pochopením těchto různých součástí a jejich správného používání se mohou přispěvatelé efektivně zapojit do projektů, pomáhat zlepšovat návrhy softwaru a hardwaru a těžit z kolektivních znalostí a úsilí celosvětové vývojářské komunity. Ať už jde o hlášení problémů, návrhy na vylepšení nebo přispívání kódem, GitHub poskytuje nástroje a strukturu nezbytné pro smysluplnou spolupráci ve světě open source.


## Příspěvek k otevřenému zdrojovému kódu Hands-on

<chapterId>84d033f5-7182-584f-b1a5-697172bc7a1c</chapterId>

:::video id=7d318fd0-6f0b-422a-9f30-2c470b56951d:::

V návaznosti na základy vytváření problémů a zkoumání projektů s otevřeným zdrojovým kódem se tato kapitola zaměřuje na praktické aspekty přímého přispívání prostřednictvím žádostí o stažení a správy repozitářů. Porozumění tomu, jak fork repozitáře, provádět změny a odesílat žádosti o stažení, představuje klíčovou sadu dovedností pro každého vývojáře, který chce smysluplně přispívat do projektů s otevřeným zdrojovým kódem, ať už se jedná o vývoj softwaru nebo návrh hardwaru.


Proces přispívání změn kódu probíhá podle standardizovaného pracovního postupu, který zajišťuje integritu projektu a zároveň umožňuje společný vývoj. Tento pracovní postup zahrnuje vytvoření vlastní kopie úložiště projektu, provedení změn v kontrolovaném prostředí a následné navržení těchto změn zpět do původního projektu prostřednictvím formálního procesu kontroly. Ačkoli se příklady v této kapitole zaměřují především na softwarové příspěvky, stejné principy a postupy platí i pro hardwarové projekty zahrnující návrhy desek plošných spojů, schémata a další technickou dokumentaci.


### Porozumění vidlicím a struktuře úložiště


Základem přispívání do jakéhokoli projektu s otevřeným zdrojovým kódem je vytvoření fork, který slouží jako vaše osobní kopie původního úložiště. Když přejdete do úložiště GitHub a kliknete na tlačítko "fork", vytvoříte nezávislou kopii pod vlastním účtem GitHub, která si zachovává jasné spojení s původním zdrojovým kódem. Tento forknutý repozitář se zobrazí ve vašem účtu s jasným označením jeho původu, přičemž se pod názvem repozitáře zobrazí text jako "forked from [original-owner]/[repository-name]".


Váš forknutý repozitář funguje nezávisle na původním, což vám umožňuje provádět změny bez vlivu na hlavní projekt. Díky synchronizačním funkcím GitHubu však bude mít povědomí o aktualizacích původního úložiště. Když původní repozitář obdrží aktualizace, které váš fork postrádá, GitHub zobrazí stavové informace, jako například "Tato větev je o X revizí pozadu" nebo "O X revizí napřed", což poskytuje jasný přehled o vztahu mezi vaším fork a upstreamovým repozitářem. Svůj fork můžete kdykoli synchronizovat s původním repozitářem kliknutím na tlačítko "Sync fork", čímž dojde k přetažení nejnovějších změn z upstreamového zdroje.


Vztah mezi vaším úložištěm fork a původním úložištěm je obzvláště důležitý, když začnete provádět změny. Jakmile provedete změny a odevzdáte je do svého fork, GitHub tyto rozdíly sleduje a zobrazuje je jako revize před původním úložištěm. Tento systém sledování umožňuje proces žádostí o stažení, kdy můžete navrhnout své změny k začlenění do hlavního projektu a zároveň si zachovat jasnou historii toho, co bylo upraveno.


### Nastavení vývojového prostředí


Vytvoření efektivního vývojového prostředí vyžaduje pečlivou pozornost jak obecným vývojovým nástrojům, tak specifickým požadavkům projektu. Visual Studio Code slouží jako vynikající integrované vývojové prostředí (IDE) pro většinu příspěvků s otevřeným zdrojovým kódem a poskytuje základní funkce pro úpravu kódu, integraci správy verzí a správu projektu. První kritickou součástí je instalace a konfigurace rozšíření Git, které umožňuje bezproblémovou integraci s repozitáři GitHub přímo z vývojového prostředí.


Moderní verze Visual Studia Code obvykle obsahují podporu systému Git ve výchozím nastavení, ale pro aktivaci plné funkčnosti je nutné se ověřit pomocí účtu GitHub. Tento proces ověřování zahrnuje přihlášení ke službě GitHub prostřednictvím IDE, což vám následně umožní klonovat úložiště, odevzdávat změny a odesílat aktualizace přímo z vývojového prostředí. Integrace služby GitHub se zobrazuje jako ikona v levém postranním panelu a poskytuje přístup k funkcím klonování úložišť, správy větví a synchronizace, aniž by vyžadovala operace příkazového řádku.


U projektů zahrnujících vestavěné systémy nebo specifické hardwarové platformy jsou nutné další nástroje. Rozšíření ESP-IDF představuje klíčovou součást pro projekty zaměřené na mikrokontroléry ESP32, které vyžadují specifickou kompatibilitu verzí pro zajištění správné funkčnosti. Proces instalace zahrnuje výběr vhodné verze ESP-IDF, konfiguraci cest k nástrojům a nastavení prostředí vývojového kontejneru. Verze 5.1.3 v současné době představuje doporučenou konfiguraci pro mnoho projektů založených na ESP32, ačkoli tyto požadavky se mohou vyvíjet s tím, jak projekty aktualizují své závislosti a řetězce nástrojů.


### Provádění změn a správa odevzdaných souborů


Jakmile je vývojové prostředí správně nakonfigurováno, začíná proces vytváření smysluplných příspěvků stažením nebo naklonováním forknutého repozitáře do místního počítače. Toho můžete dosáhnout buď stažením souboru ZIP s obsahem úložiště, nebo pomocí integrované funkce klonování aplikace Visual Studio Code, která poskytuje efektivnější pracovní postup pro průběžný vývoj. Proces klonování vytvoří místní kopii úložiště, která zůstane synchronizovaná s vaším GitHub fork, což vám umožní pracovat offline při zachování možností správy verzí.


Při práci s místním úložištěm získáte přístup ke kompletní struktuře projektu, včetně souborů zdrojového kódu, konfiguračních souborů, dokumentace a všech souborů návrhu hardwaru. Většina projektů firmwaru využívá programovací jazyky, jako je jazyk C pro základní funkce, s dalšími komponentami napsanými v jazyce TypeScript pro uživatelská rozhraní nebo Java pro specifické nástroje. Porozumění struktuře projektu vám pomůže určit vhodné soubory k úpravě a zajistí, že vaše změny budou v souladu s architektonickými vzory a standardy kódování projektu.


Proces odevzdání představuje základní aspekt správy verzí, který vyžaduje pečlivou pozornost jak z hlediska technické přesnosti, tak z hlediska srozumitelnosti komunikace. Před provedením jakýchkoli změn byste měli důkladně porozumět stávajícímu kódu a otestovat veškeré změny v místním prostředí. Základní pravidlo přispívání do otevřeného zdrojového kódu zdůrazňuje, že nikdy nezveřejňujte netestovaný kód, protože tím můžete zavést chyby nebo bezpečnostní zranitelnosti, které ovlivní celou komunitu projektu. Kromě toho nesmíte do veřejných repozitářů nikdy odevzdávat citlivé informace, jako jsou hesla, tokeny API nebo osobní pověření, protože tyto informace se stávají trvale přístupné komukoli, kdo má k repozitáři přístup.


### Vytváření a správa požadavků na stažení


Vyvrcholením vašeho úsilí o přispění je vytvoření žádosti o stažení, která slouží jako formální návrh na sloučení vašich změn do původního úložiště projektu. Tento proces začíná ve vašem úložišti GitHub fork, kde si můžete prohlédnout rozdíly mezi vaším úložištěm a zdrojovým kódem v upstreamu. Rozhraní GitHubu přehledně zobrazuje počet revizí před nebo za, což poskytuje okamžitý přehled o rozsahu vámi navrhovaných změn. Před vytvořením požadavku na stažení byste se měli ujistit, že je váš zdrojový kód fork synchronizován s nejnovějšími změnami v upstreamu, abyste minimalizovali potenciální konflikty.


Vytvoření efektivního požadavku na stažení vyžaduje víc než pouhé odeslání změn kódu. Popis žádosti o stažení slouží jako příležitost sdělit správcům projektu a komunitě účel, rozsah a dopad vašich úprav. Dobře napsaný popis vysvětluje, jaké problémy vaše změny řeší, jak jste řešení implementovali a jaké jsou případné důsledky pro další části projektu. Tato dokumentace se stává obzvláště důležitou u složitých změn, které nemusí být okamžitě zřejmé pouze ze zkoumání rozdílů v kódu.


Proces recenzování představuje aspekt spolupráce při vývoji otevřeného zdrojového kódu, kdy správci projektu a zkušení přispěvatelé hodnotí vámi navrhované změny. Můžete požádat o konkrétní recenzenty, kteří mají odborné znalosti v oblastech, jichž se vaše změny týkají, čímž zajistíte, že vaši práci posoudí kompetentní členové komunity. Proces přezkoumání může zahrnovat několik iterací, kdy recenzenti poskytují zpětnou vazbu, požadují úpravy nebo další testování. Tento společný proces vylepšování pomáhá udržovat kvalitu kódu a zároveň poskytuje cenné příležitosti k učení pro přispěvatele na všech úrovních zkušeností.


Pochopení toho, že ne všechny žádosti o stažení jsou přijaty, pomáhá nastavit vhodná očekávání pro proces přispívání. Správci projektu mohou odmítnout žádosti o stažení z různých důvodů, včetně nesouladu s cíli projektu, nedostatečného testování nebo existence alternativních řešení, která jsou již ve vývoji. Spíše než jako neúspěch je třeba odmítnutí považovat za příležitost poučit se ze zpětné vazby, zdokonalit přístup a případně přispět alternativními řešeními, která lépe vyhovují potřebám projektu. Komunita open source prosperuje díky tomuto iterativnímu procesu navrhování, přezkoumávání a zdokonalování, který nakonec posouvá projekty kupředu díky společnému úsilí a sdíleným odborným znalostem.



## Co je Public-Pool?

<chapterId>b461bf94-4a90-5bb8-ba3f-976d5d57be0d</chapterId>


:::video id=d4652496-1ed4-4415-8048-0b6871b9ed51:::

Veřejný pool představuje revoluční přístup ke Bitcoin mining, který řeší mnoho obav těžařů z tradičních poolů mining. Jako plně open-source sólo pool Bitcoin mining Public Pool zásadně mění model distribuce odměn, na který si těžaři zvykli. Na rozdíl od běžných poolů mining, kde se účastníci dělí o odměny, když kterýkoli těžař v poolu najde blok, Public Pool funguje na principu sólo mining, kde si jednotliví těžaři ponechávají 100 % odměn, když úspěšně vytěží blok.


Nejpřesvědčivějším rysem služby Public Pool je její nulová struktura poplatků. Když těžaři úspěšně naleznou blok pomocí Public Pool, obdrží kompletní odměnu za blok spolu se všemi souvisejícími [transakčními poplatky](https://planb.academy/resources/glossary/transaction-fees) bez jakýchkoli srážek za náklady na provoz poolu. To je v ostrém kontrastu s tradičními pooly mining, které si obvykle účtují poplatky v rozmezí 1-3 % z odměny mining. Díky modelu nulových poplatků je Public Pool obzvláště atraktivní pro těžaře, kteří chtějí maximalizovat své potenciální výnosy a zároveň si zachovat plnou kontrolu nad svými operacemi mining.


Pro pochopení jedinečného postavení fondu Public Pool je důležité pochopit základní rozdíl mezi samostatným a sdruženým fondem mining. Skutečný sólo mining znamená, že těžíte nezávisle a v případě nalezení bloku obdržíte odměnu v plné výši (v současné době 3,125 BTC + poplatky), ale pravděpodobnost je úměrná vašemu hash rate oproti celé síti - což vytváří extrémní rozptyl, který může mezi odměnami trvat měsíce nebo roky. Tradiční pooly kombinují hashovací sílu, aby našly bloky častěji, rozdělují odměny proporcionálně a poskytují stabilní, předvídatelný příjem. Pro těžaře se značným kapitálem investovaným do hardwaru a provozních nákladů je čistě sólový mining obvykle nepraktický bez ohledu na jeho filozofické výhody - rozptyl téměř znemožňuje pokrýt náklady na elektřinu a získat zpět investice. Tato ekonomická realita znamená, že většina těžařů si z praktických finančních důvodů zvolí sdružený mining. Public Pool funguje jako pool mining, což znamená, že se stále potýkáte s rozptylem sólového těžení mining (odměnu získáte pouze tehdy, když osobně najdete blok), ale využíváte výhod infrastruktury poolu a transparentního provozu s nulovými poplatky.


### Výhoda open source a technická implementace


Závazek společnosti Public Pool vyvíjet open-source poskytuje těžařům bezprecedentní transparentnost a kontrolu nad jejich operacemi mining. Celá kódová základna je k dispozici na GitHubu, což těžařům umožňuje přesně prozkoumat, jak software funguje, upravit jej podle svých potřeb a dokonce přispět k jeho vývoji. Tato transparentnost řeší významné obavy komunity mining týkající se neznámých konfigurací a postupů tradičních poolů mining.


Softwarová architektura zahrnuje jak základní funkce fondu mining, tak samostatný repozitář uživatelského rozhraní, které jsou volně k dispozici ke stažení a úpravám. Těžaři mohou Public Pool provozovat v různých konfiguracích, včetně kontejnerů Docker, díky čemuž je možné jej přizpůsobit různým hardwarovým konfiguracím a technickým preferencím. Obsáhlá dokumentace poskytovaná v repozitářích GitHub nabízí podrobné návody k instalaci, možnosti konfigurace a pokyny k úpravám, takže je přístupná těžařům s různou úrovní technických znalostí.


Připojení k veřejnému poolu vyžaduje minimální konfiguraci ve srovnání s tradičními nastaveními mining. Těžaři jednoduše musí nakonfigurovat svá zařízení mining s údaji o připojení [Stratum](https://planb.academy/resources/glossary/stratum) a jako uživatelské jméno zadat svou adresu Bitcoin. Pro organizační účely lze za oddělovač teček přidat volitelné jméno pracovníka.


### Funkce komunity a model udržitelnosti


Veřejný bazén obsahuje několik inovativních prvků, které posilují komunitu Bitcoin mining při zachování nulového poplatku za provoz. Platforma zobrazuje komplexní statistiky včetně celkové rychlosti hašování připojených těžařů, která se v roce 2024 obvykle pohybovala mezi 1 až 2 PetaHash za sekundu a v listopadu 2025 kolem 40 PH/s, a poskytuje podrobné informace o připojených zařízeních mining. Za zvláštní pozornost stojí důraz platformy na open-source hardware mining, přičemž zařízení označená hvězdičkami označují plně open-source návrhy, doplněné o odkazy na jejich příslušné repozitáře GitHub.


Udržitelnost provozu Public Pool s nulovými poplatky závisí na kreativním partnerství partnerského programu s dodavateli hardwaru mining. Když těžaři nakoupí vybavení od partnerských společností s použitím slevového kódu "SOLO", padesát procent výdělku z affiliate podpoří provozní náklady Public Pool, zatímco zbývajících padesát procent je rozděleno jako odměna těžařům, kteří každý měsíc dosáhnou nejvyššího podílu obtížnosti. Tento model vytváří symbiotický vztah, v němž těžaři získávají slevy na nákup vybavení, prodejci získávají zákazníky a Public Pool udržuje svůj provoz bez účtování přímých poplatků.


### Filozofie decentralizace a osvědčené postupy


Ačkoli Public Pool nabízí vynikající alternativu k tradičním poolům mining, je důležité pochopit jeho roli v širším kontextu decentralizace Bitcoin. Platforma slouží jako odrazový můstek ke konečnému cíli, kterým je provozování vlastních poolů mining jednotlivými těžaři. Provozování vlastního poolu mining představuje nejvyšší úroveň decentralizace, protože eliminuje závislost na infrastruktuře nebo softwaru třetích stran, bez ohledu na to, jak transparentní nebo dobře míněná tato třetí strana může být.


Veřejný pool je díky své open-source povaze ideální výukovou platformou pro těžaře, kteří chtějí pochopit fungování poolu před implementací vlastních řešení. Dostupnost instalačních příruček pro více operačních systémů a obsáhlá dokumentace poskytují těžařům znalosti potřebné k přechodu od používání Public Poolu k provozování vlastní infrastruktury mining. Tento vzdělávací aspekt je v souladu se základními principy Bitcoin, kterými jsou vlastní suverenita a decentralizace, a dává jednotlivým těžařům možnost převzít plnou kontrolu nad svými operacemi mining a zároveň přispět k celkovému zabezpečení a decentralizaci sítě Bitcoin.


Uživatelské rozhraní platformy poskytuje těžařům podrobné možnosti monitorování, včetně stavu pracovníků, statistik hash rate a výkonnostních ukazatelů. Tyto funkce pomáhají těžařům optimalizovat jejich provoz a zároveň se seznamují s principy správy poolů, které mohou později aplikovat na vlastní implementace poolů mining.


## Jak nainstalovat Public-Pool na Umbrel

<chapterId>7f6d0307-7715-5581-89ea-f13cf8754f9a</chapterId>


:::video id=3a4fe0a9-bbf5-458a-8ec1-52c3b83afd87:::

Provozování vlastního bazénu Bitcoin mining doma je díky modernímu hardwaru a zjednodušeným softwarovým řešením stále dostupnější. Tato kapitola se zabývá praktickou realizací domácího veřejného bazénu s využitím cenově dostupného hardwaru mini PC a zjednodušeného softwaru pro správu [uzlů](https://planb.academy/resources/glossary/node). Na konci této příručky budete rozumět hardwarovým požadavkům, procesu nastavení softwaru a základní konfiguraci potřebné k vytvoření vlastní infrastruktury bazénu mining.


### Požadavky na hardware a nastavení


Základem každé domácí sestavy bazénu mining je výběr vhodného hardwaru, který vyvažuje výkon, náklady a energetickou účinnost. Ideální řešení pro tuto aplikaci představuje miniaturní počítač, který nabízí dostatečný výpočetní výkon při zachování kompaktních rozměrů a rozumné spotřeby energie. Doporučená konfigurace zahrnuje procesor Intel N100, který poskytuje dostatečné výpočetní zdroje pro operace poolu, ve spojení s alespoň jedním terabajtem úložiště NVMe pro uložení blokového řetězce Bitcoin a souvisejících dat.


Požadavek na úložiště je obzvláště důležitý, protože provoz fondu mining vyžaduje udržování plně synchronizovaného uzlu Bitcoin. Jednotka NVMe o kapacitě jednoho terabajtu zajišťuje rychlé operace čtení/zápisu, které jsou nezbytné pro synchronizaci [blockchainu](https://planb.academy/resources/glossary/blockchain) a průběžné zpracování [transakcí](https://planb.academy/resources/glossary/transaction-tx). Dostatečná alokace paměti RAM navíc podporuje bezproblémový provoz jak základního operačního systému Linux, tak softwaru pro správu uzlu, který bude koordinovat činnosti poolu.


### Architektura softwaru a správa uzlů


Softwarový stack pro domácí pool mining je postaven na linuxovém základu, který zajišťuje stabilitu a zabezpečení nezbytné pro provoz Bitcoin. Nad tímto základním systémem vytváří specializovaný software pro správu uzlů, jako je Umbrel, intuitivní rozhraní pro správu infrastruktury Bitcoin. Tento přístup abstrahuje velkou část složitosti tradičně spojované s provozem uzlů Bitcoin a zpřístupňuje provoz poolu uživatelům bez rozsáhlého technického vzdělání.


Umbrel slouží jako komplexní platforma pro správu uzlů, která zajišťuje instalaci, synchronizaci a průběžnou údržbu [jádra Bitcoin](https://planb.academy/resources/glossary/bitcoin-core) prostřednictvím webového rozhraní. Model obchodu s aplikacemi této platformy umožňuje snadnou instalaci dalších služeb, včetně softwaru fondu mining, prostřednictvím jednoduchých operací typu "ukaž a klikni". Tato architektura zajišťuje, že se uživatelé mohou soustředit spíše na provoz fondu než na správu systému, a přitom si zachovávají plnou kontrolu nad svou infrastrukturou Bitcoin.


### Instalace a konfigurace veřejného bazénu


Instalace softwaru pro veřejné bazény prostřednictvím platformy Umbrel demonstruje zjednodušenou povahu nasazení moderní infrastruktury Bitcoin. Proces začíná přístupem do obchodu s aplikacemi Umbrel prostřednictvím webového rozhraní, kde se jednoduchým vyhledáváním "public pool" zobrazí dostupný software mining pool. Instalace vyžaduje pouze několik kliknutí: výběr aplikace, potvrzení instalace a čekání na dokončení automatického procesu nastavení.


Instalační proces automaticky nakonfiguruje potřebná připojení mezi softwarem veřejného fondu a základním uzlem Bitcoin. Tato integrace zajišťuje, že pool může ověřovat transakce, sestavovat šablony bloků a distribuovat práci připojeným těžařům, aniž by bylo nutné ručně konfigurovat složité síťové parametry. Po dokončení instalace je rozhraní poolu okamžitě přístupné prostřednictvím místní sítě a poskytuje možnosti monitorování a správy v reálném čase.


### Připojení horníků a úvahy o síti


Připojení hardwaru mining k nově vytvořenému poolu vyžaduje konfiguraci nastavení poolu těžaře tak, aby ukazoval na vaši místní infrastrukturu. To zahrnuje nahrazení výchozí adresy poolu vaší místní IP adresou a příslušným číslem portu přiděleným během instalace veřejného poolu. Změna konfigurace přesměruje výpočetní úsilí vašeho hardwaru mining z externích poolů na vaši domácí infrastrukturu, což vám umožní zachovat si plnou kontrolu nad provozem mining a potenciálními odměnami.


Konfigurace sítě hraje klíčovou roli v dostupnosti a funkčnosti bazénu. Nastavení místní sítě obvykle zahrnuje standardní adresování IP, ale uživatelé se mohou setkat s rozdíly v rozlišení DNS v závislosti na konfiguraci směrovače. Některé směrovače poskytují místní služby DNS, které vytvářejí přátelské názvy pro místní služby, zatímco jiné vyžadují přímý přístup k adresám IP. Pro širší přístupnost mimo místní síť může být nutná konfigurace přesměrování portů na směrovači, což však přináší další bezpečnostní aspekty, které vyžadují pečlivé posouzení souvisejících rizik a přínosů.


Úspěšné vytvoření domácího fondu mining představuje významný krok směrem k decentralizované infrastruktuře Bitcoin, která poskytuje jak vzdělávací hodnotu, tak praktické možnosti mining při zachování úplné kontroly nad provozem Bitcoin.


# Montáž hardwaru a řešení problémů

<partId>f6987088-5ba4-52e2-b2d0-aa122080940c</partId>


## Jaké nástroje použít?

<chapterId>733935b5-0171-5a22-838c-e192df6f7ccf</chapterId>


:::video id=bddd0e47-7b43-4685-ba2e-bf3a8ff653c9:::

Ve světě pájení zařízení pro povrchovou montáž (SMD), zejména při práci s projekty Bitaxe, je rozdíl mezi frustrací a úspěchem dán tím, že máte k dispozici správné nástroje. Tento komplexní průvodce se zabývá základním vybavením potřebným k efektivnímu řešení projektů pájení SMD, od základního ručního nářadí až po specializované vybavení, které zvýší vaše pájecí schopnosti.


Chcete-li se podívat na dokumentaci ke schématům, podívejte se na tuto stránku [GitHub repo](https://github.com/skot/bitaxe-doc/tree/main).


### Základní ruční nářadí a přesné nástroje


Základem každé sestavy pro pájení SMD je kvalitní pinzeta, která slouží jako hlavní nástroj pro umístění součástek. Při této práci se nejvíce osvědčují dva typy pinzet: standardní pinzety s rovnou špičkou a pinzety s mírným ohybem na špičce. Pinzety s rovnou špičkou zvládnou většinu SMD součástek, které se nacházejí v typických sadách Bitaxe, zatímco pinzety s ohnutou špičkou vynikají při práci s extrémně malými součástkami, které vyžadují přesné umístění. Tyto nástroje jsou často součástí opravárenských sad, jako jsou například sady iFixit určené pro opravy telefonů, takže jsou snadno dostupné většině amatérů.


K pinzetě se hodí dobré nůžky, které jsou nepostradatelné pro stříhání elektrické pásky, která v projektech elektroniky slouží k mnoha účelům. Elektrická páska poskytuje nezbytnou izolaci pro kabely a součástky a mít kvalitní pásku snadno dostupnou zefektivňuje proces pájení. Tyto základní potřeby lze pořídit v železářstvích nebo v internetových obchodech, aniž by bylo třeba specializovaných dodavatelů elektroniky.


### Aplikace a správa pájecí pasty


Nanášení pájecí pasty představuje jeden z nejdůležitějších aspektů pájení SMD a díky správným nástrojům je tento proces přesný a příjemný. Malé, neostré injekční stříkačky naplněné pájecí pastou poskytují výjimečnou kontrolu nad umístěním pasty. Tato metoda umožňuje přesné nanášení přesného množství pájecí pasty potřebného pro každý spoj a většina lidí si díky praktickému nácviku rychle osvojí správnou techniku ovládání tlaku a průtoku.


Samotná volba pájecí pasty významně ovlivňuje úspěšnost pájení. ChipQuik TS391SNL50 vyniká jako výjimečná pájecí pasta pro projekty Bitaxe a obecné práce s SMD. Tato pasta si zachovává správnou konzistenci a vlastnosti tání, čímž se vyhýbá problémům spojeným s levnějšími alternativami, které mají příliš nízké teploty tání. Nekvalitní pájecí pasty mohou způsobit problémy, kdy se dříve pájené spoje při zahřívání přilehlých oblastí stanou opět tekutými, což vede k posunu součástek a špatnému spojení. Kvalitní pájecí pasta sice představuje vyšší počáteční investici, ale lepší výsledky a snížení frustrace tyto náklady ospravedlňují.


### Nástroje pro řešení problémů a čištění


Dokonce i zkušení páječi se setkávají s problémy, které vyžadují nápravu, a proto je odpájení nezbytné pro každou kompletní sadu nástrojů. Odpájecí zařízení, v podstatě vyhřívaný vakuový nástroj, odstraňuje přebytečnou pájku a opravuje přemostěné spoje mezi vývody součástek. Tyto nástroje fungují nejefektivněji v kombinaci s tavidlem, které zlepšuje tok pájky a napomáhá efektivnějšímu procesu odpájení.


Flux se dodává v různých formách, včetně pevných a kapalných, a slouží k mnoha účelům, kromě pomoci při odpájení. Když pájecí pasta začne během delší práce ztrácet svou účinnost, použití dalšího tavidla obnoví správné tokové vlastnosti a zajistí spolehlivé spoje. Malý nástroj ve tvaru lžičky, který se často nachází v přesných opravárenských sadách, usnadňuje přesné nanášení tavidla na konkrétní místa bez znečištění okolních součástek.


Čištění desek je posledním krokem profesionální práce a vyžaduje isopropanolový líh a speciální čisticí kartáč. K tomuto účelu se výborně hodí starý zubní kartáček a stlačovací láhev s isopropanolem umožňuje kontrolované nanášení čisticího roztoku. Tato kombinace odstraní zbytky tavidla a pasty a zanechá desky s čistým, profesionálním vzhledem, který také usnadní kontrolu pájecích spojů.


### Specializované vybavení a pokročilé nástroje


U projektů zahrnujících složité integrované obvody, zejména ASIC, šablony mění proces pájení z únavného ručního umisťování na efektivní a přesné nanášení pasty. Tyto přesně vyřezávané šablony zajišťují konzistentní tloušťku a umístění pasty, čímž výrazně zkracují čas potřebný pro složité součástky a zároveň zvyšují spolehlivost. Investice do kvalitních šablon se vyplatí jak v úspoře času, tak v lepších výsledcích.


Při práci s výkonovými součástmi je tepelný management klíčový, a proto je tepelná pasta nebo tepelné mazivo nezbytným spotřebním materiálem. Tyto materiály zajišťují správný přenos tepla mezi chladiči a integrovanými obvody, zabraňují tepelnému poškození a zajišťují spolehlivý provoz. Kvalitní materiály pro tepelné rozhraní představují malou investici, která chrání mnohem dražší komponenty.


Srdcem každé sestavy pro pájení SMD je horkovzdušná přepracovací stanice, která poskytuje řízené teplo potřebné pro práci s povrchovou montáží. Levné stanice v cenovém rozmezí 30-50 dolarů sice mohou fungovat přiměřeně, ale často jim chybí spolehlivost a přesnost zařízení vyšší třídy. Tyto základní stanice obvykle efektivně pracují při teplotě 355 °C a jsou vybaveny automatickým snížením teploty při návratu rukojeti do držáku. Jejich spolehlivost však může být nekonzistentní, přičemž některé jednotky předčasně selhávají. Pro seriózní práci poskytuje investice do kvalitnějšího vybavení od specializovaných dodavatelů elektroniky lepší dlouhodobou hodnotu díky vyšší spolehlivosti a přesnějšímu řízení teploty.


Kombinace těchto nástrojů vytváří kompletní možnosti pájení SMD, které dalece přesahují projekty Bitaxe a jsou určeny pro běžnou práci s elektronikou. Pochopení úlohy každého nástroje a výběr kvalitního vybavení odpovídajícího vaší úrovni dovedností a požadavkům projektu zajistí úspěšné výsledky a příjemný zážitek z pájení.



## Oprava problémů s pájením

<chapterId>96663744-b4f7-5154-930f-a68ba7954603</chapterId>


:::video id=9286c0dc-acd6-44d9-b34e-59cfb2da9748:::


Sada transceiverů Bitaxe představuje při montáži jedinečnou výzvu, která vyžaduje pečlivou pozornost při orientaci součástek, prevenci pájecích můstků a správné řízení tepla. Pochopení těchto běžných problémů a jejich řešení je nezbytné pro úspěšnou konstrukci stavebnice a předcházení nákladnému poškození komponent. Tato kapitola se zabývá nejčastějšími problémy s pájením, s nimiž se setkáváme při montáži sady Bitaxe, a uvádí praktické techniky jejich identifikace a řešení.


### Orientace a identifikace součástí


Správná orientace součástek představuje jeden z nejdůležitějších aspektů úspěšné montáže Bitaxe, zejména u tranzistorů MOSFET Q1 a Q2. Tyto součástky mají výrazné orientační značky, které je třeba při montáži pečlivě dodržovat. Každý MOSFET obsahuje malé bodové označení, které odpovídá specifickému uspořádání plošek na desce plošných spojů. Klíč ke správné orientaci spočívá v pochopení fyzické struktury těchto součástek, které mají čtyři vývody uspořádané s jednou velkou podložkou a třemi menšími podložkami, které nemají žádné spojení s velkou podložkou.


Při instalaci Q1 a Q2 pečlivě zkontrolujte součástku i desku plošných spojů. Rozložení desky jasně ukazuje zamýšlenou orientaci díky konfiguraci plošek se čtyřmi vývody umístěnými tak, aby odpovídaly struktuře MOSFETu. Před pájením jakékoli velké součástky vždy ověřte orientaci porovnáním fyzických značek součástky s uspořádáním plošek na desce. Tento jednoduchý ověřovací krok zabrání frustraci z odpájení a opětovné instalace nesprávně orientovaných součástek.


Důsledky nesprávné orientace přesahují rámec prostých funkčních problémů. Špatně orientované tranzistory MOSFET mohou způsobit poruchy obvodu, které se obtížně diagnostikují a mohou vyžadovat kompletní výměnu součástek. Pokud věnujete čas ověření orientace před zahřátím, zajistíte správnou funkci obvodu a předejdete zbytečnému řešení problémů v pozdější fázi montáže.


### Správa pájecích můstků a přebytečné pájky


Pájecí můstky představují další častou výzvu při montáži Bitaxe, zejména u součástek s jemnou roztečí, jako je U10. Tato nežádoucí spojení mezi sousedními piny mohou způsobit poruchy obvodu a vyžadují pečlivé techniky odstranění. Nejúčinnější přístup zahrnuje použití odpájovacích knotů, měděného opleteného materiálu, který po zahřátí absorbuje přebytečnou pájku. Tato technika vyžaduje trpělivost a správný výběr nástroje, aby nedošlo k poškození choulostivých součástek.


Při řešení pájecích můstků na integrovaných obvodech používejte držák desky plošných spojů nebo kloubovou svorku, abyste součástku při práci bezpečně přidrželi. Na postiženou oblast přiložte mírné teplo a opatrně přetáhněte pájecí knot přes přemostěné spoje. Měděný oplet přirozeně absorbuje přebytečnou pájku a oddělí nežádoucí spoje. Tento proces může vyžadovat několik pokusů, ale vytrvalost přináší čisté, řádně oddělené spoje.


Nejlepším přístupem ke správě pájecích můstků zůstává prevence. Používání přiměřeného množství pájecí pasty a pevná kontrola rukou při umísťování součástek výrazně omezuje tvorbu můstků. Pokud se můstky objeví, řešte je okamžitě a nedoufejte, že neovlivní provoz obvodu. I zdánlivě drobné můstky mohou způsobit významné problémy s funkčností, které se po kompletním sestavení desky obtížně diagnostikují.


### Kritické součásti a zvláštní aspekty


Zvláštní pozornost si zaslouží buck konvertor U9, který hraje klíčovou roli při převodu 5 V na 1,2 V pro čip ASIC. Tato součástka představuje jedinečnou výzvu kvůli svým pěti malým spojům a sklonu k poruchám. Správná instalace vyžaduje přesné nanesení pájecí pasty a pečlivé řízení tepla. Nedostatečné množství pájecí pasty pod U9 může mít za následek špatné spoje, které brání správné konverzi napětí, zatímco nadbytek pasty může vytvořit můstky, které způsobí nefunkčnost obvodu.


U9 vytváří při problémech s pájecím můstkem charakteristické zvukové signály a generuje vysokofrekvenční šum, který se liší od běžného provozu ASIC. Tato technika sluchové diagnostiky může pomoci identifikovat problémy, i když k jejímu odhalení je zapotřebí dobrý vysokofrekvenční sluch. Pokud není zvuková diagnostika možná, je nezbytná vizuální kontrola. Pečlivě prozkoumejte všechny spoje a hledejte můstky nebo nedostatečné pokrytí pájkou.


Pokud U9 nevydává požadovaných 1,2 V, přestože se zdá být správně připájen, je pravděpodobnou příčinou nedostatečné množství pájecí pasty. Vyjměte součástku, naneste malé množství další pájecí pasty a znovu ji nainstalujte. V případech, kdy jednotlivé piny nemají dostatečné pokrytí pájkou, naneste opatrně malé množství pájecí pasty na konkrétní místa pomocí pinzety. Pájecí pasta při zahřátí přirozeně steče pod součástku a vytvoří správné spoje díky kapilárnímu působení.


### Řízení tepla a ochrana součástí


Správné řízení tepla chrání citlivé součástky před tepelným poškozením a zároveň zajišťuje spolehlivé pájecí spoje. Komponenty, jako je krystalový oscilátor Y1 a U1, jsou obzvláště citlivé na dlouhodobé působení tepla a vyžadují pečlivou kontrolu teploty. Udržujte teplotu páječky na 350 stupních Celsia, ale minimalizujte dobu působení tepla, aby nedošlo k poškození součástek. Rychlé a účinné techniky pájení chrání tyto citlivé součástky a zároveň umožňují dosáhnout spolehlivých spojů.


Čip ASIC vyžaduje speciální manipulační techniky vzhledem ke složité struktuře vývodů a citlivosti na mechanické namáhání. Při použití šablon pro nanášení pájecí pasty zajistěte rovnoměrné pokrytí všech pinů, abyste zabránili nerovnoměrnému usazení součástek. Pokud nadměrné množství pájecí pasty způsobí nerovnoměrné usazení čipu ASIC, nechte sestavu před provedením oprav zcela vychladnout. Při zahřívání vyvíjejte jemný tlak pouze na označené okraje součástky, nikdy ne na centrální oblast matrice, abyste dosáhli správného usazení.


Součástka U8 představuje jedinečnou výzvu vzhledem ke svému velkému počtu vývodů a možnosti ohnutí vodičů. Pokud se vývody při manipulaci ohnou, použijte držák desky plošných spojů nebo kloubovou svorku, abyste součástku zajistili, a postižené vývody opatrně narovnejte. Pracujte pomalu a trpělivě, aby nedošlo k přetržení jemných vodičů. Pochopení, že určité skupiny pinů na U8 jsou vnitřně propojeny, může zjednodušit řešení problémů, protože můstky mezi těmito konkrétními piny nemají vliv na činnost obvodu. Můstky mezi ostatními piny však vyžadují opatrné odstranění, aby byla zajištěna správná funkčnost.


## Jak ladit Bitaxe pomocí AxeOS

<chapterId>603f5c0d-4b7c-51e1-9bad-318a8b8e9db7</chapterId>

:::video id=d23d748b-510e-4748-9617-b875da757031:::

Při práci se zařízeními Bitaxe mining se mohou poruchy hardwaru projevit různými způsoby, které nemusí být okamžitě zřejmé. Porozumění tomu, jak tyto problémy systematicky diagnostikovat pomocí operačního systému AxeOS, může ušetřit značnou část času a zabránit zbytečným výměnám komponent. Tato kapitola se zabývá diagnostickými technikami a metodikami řešení problémů, které zkušení technici používají k identifikaci konkrétních hardwarových problémů pomocí softwarové analýzy.


### Porozumění indikátorům spotřeby energie


Prvním a nejdůležitějším diagnostickým ukazatelem v systému AxeOS je sledování spotřeby energie. Běžná zařízení Bitaxe, včetně modelů Bitaxe Ultra a Bitaxe Supra, spotřebovávají při standardním provozu obvykle 10 až 17 wattů. Toto základní měření slouží jako hlavní ukazatel stavu celého systému. Pokud spotřeba energie výrazně klesne pod toto rozmezí, zejména pod 3 watty, signalizuje to zásadní problém s čipem ASIC nebo jeho podpůrnými obvody.


Scénářům s nízkou spotřebou energie je třeba věnovat okamžitou pozornost, protože naznačují, že čip mining je buď zcela nefunkční, nebo pracuje v závažně zhoršeném stavu. Už jen toto měření vám pomůže rychle rozlišit mezi problémy s výkonem a úplným selháním hardwaru. Údaj o výkonu v systému AxeOS poskytuje zpětnou vazbu v reálném čase, která vám umožní sledovat účinnost všech pokusů o opravu, které na zařízení provedete.


### Analýza měření napětí ASIC


Funkce měření napětí ASIC v systému AxeOS poskytuje důležité diagnostické informace, které pomáhají přesně určit povahu hardwarových problémů. Při zkoumání naměřených hodnot napětí je třeba pochopit vztah mezi naměřeným napětím a požadovaným napětím, aby bylo možné správně diagnostikovat problémy. Systém zobrazuje jak napětí dodávané čipu ASIC, tak napětí, které čip požaduje od systému správy napájení.


Pokud zaznamenáte měření napětí ASIC přesně 1,2 V v kombinaci se spotřebou energie nižší než 3 W, znamená tato specifická kombinace buď problém s pájením čipu ASIC, nebo úplnou poruchu ASIC. Toto naměřené napětí naznačuje, že napájení se dostává do místa čipu, ale samotný čip nefunguje správně. Fyzická kontrola matrice ASIC může odhalit praskliny nebo jiná viditelná poškození, která by vysvětlovala tento vzorec chování.


Jiný diagnostický scénář se objeví, když vidíte nízkou spotřebu energie ve spojení s velmi nízkými hodnotami požadovaného napětí, jako je 100 milivoltů nebo 0,5 voltu. Tento vzorec naznačuje, že čip ASIC nedostává dostatečné napájecí napětí, což obvykle ukazuje na problémy s komponentou buck konvertoru U9. Buckův měnič je zodpovědný za zajištění přesné regulace napětí, kterou čipy ASIC vyžadují pro správnou činnost.


### Interpretace dat protokolu a komunikace s ASIC


Záznamový systém AxeOS poskytuje cenné informace o tom, zda váš čip ASIC komunikuje s řídicím systémem. Při přístupu k protokolům prostřednictvím funkce "show logs" přítomnost záznamů "ASIC results" potvrzuje, že čip je nejen napájen, ale také aktivně zpracovává práci a vrací výsledky. Tato komunikace naznačuje, že čip ASIC je správně připájen a udržuje spojení s řídicím obvodem.


Absence výsledků ASIC v protokolech, zejména v kombinaci s dalšími příznaky, pomáhá zúžit problém na konkrétní komponenty nebo problémy s připojením. Tento diagnostický přístup umožňuje rozlišit mezi čipy, které zcela nereagují, a těmi, které mohou mít přerušované problémy s připojením. Analýza protokolů se stává zvláště cennou při řešení složitých problémů, kdy více příznaků může naznačovat různé základní příčiny.


### Systematický přístup k řešení problémů


Při diagnostice problémů s hardwarem Bitaxe je třeba dodržovat systematický přístup, který zabrání přehlédnutí kritických problémů a zajistí efektivní proces opravy. Začněte dokumentací spotřeby energie a naměřených hodnot napětí, poté tato měření korelujte s daty protokolu a vytvořte si kompletní obraz o chování systému. Tento metodický přístup pomáhá určit, zda problémy pramení ze samotného čipu ASIC, systému dodávky energie nebo komunikačních cest mezi součástmi.


V případech, kdy se zdá, že problémem je buck konvertor U9, může být nutná fyzická kontrola a případné přepájení. Součástka U9 je obzvláště náchylná k problémům s pájením, zejména při první montáži. Při podezření na problémy s regulací napětí lze pomocí multimetru ověřit, zda je na pinech ASIC skutečně přítomno 1,2 V, což definitivně potvrdí problémy s dodávkou energie. Pokud je na pinech napětí přítomno, ale ASIC stále nefunguje a fyzická kontrola neodhalí žádné poškození, je dalším logickým krokem výměna čipu ASIC. Pokud problémy přetrvávají i po výměně ASIC, může být jako poslední prvek v sekvenci řešení problémů nutné věnovat pozornost součásti U2, která řídí čip ASIC.


## Jak ladit pomocí USB?

<chapterId>f3182763-e1ef-5460-8bc0-f2ea53e3a410</chapterId>


:::video id=fe1b4b48-5f8a-4fd7-9417-ca03a36bce9f:::


Při řešení problémů se zařízeními Bitaxe mining poskytuje přímý přístup k internímu systému protokolování zařízení neocenitelné informace, které webová rozhraní nemohou nabídnout. V této kapitole se dozvíte, jak navázat přímé sériové připojení USB k zařízení Bitaxe pomocí rámce ESP-IDF, které umožňuje sledování systémových protokolů, spouštěcích sekvencí a chybových hlášení v reálném čase. Tento přístup k ladění je zvláště důležitý při práci se zařízeními, u nichž dochází k častým restartům nebo selháním hardwaru, protože zachycuje všechny diagnostické informace, které by se mohly ztratit při restartech systému.


Proces ladění vyžaduje Visual Studio Code s rozšířením ESP-IDF, lze však použít libovolné kompatibilní IDE. Tato metoda funguje se všemi variantami Bitaxe, které obsahují port USB, včetně Bitaxe Ultra 204 a dalších modelů této řady. Přímé sériové připojení obchází případná omezení webového rozhraní a poskytuje nefiltrovaný přístup k informacím o vnitřním stavu zařízení.


### Nastavení sériové komunikace


Navázání komunikace se zařízením Bitaxe začíná připojením kabelu USB a otevřením terminálu ESP-IDF ve vývojovém prostředí. Příkaz `idf.py monitor` zahájí proces připojení a automaticky prohledá dostupné porty COM, aby navázal komunikaci UART s čipem ESP32 v zařízení Bitaxe. Systém obvykle prochází dostupné porty (COM3, COM4, COM16 atd.), dokud nenajde správné připojení.


Po připojení terminál zobrazí kompletní zaváděcí sekvenci a průběžné provozní protokoly. Počáteční proces připojení může trvat několik okamžiků, než systém identifikuje správný komunikační port. Pokud automatická detekce portu selže, můžete port COM zadat ručně prostřednictvím rozhraní pro výběr portu IDE. Tento přímý komunikační kanál zůstává aktivní po celou dobu provozu zařízení a poskytuje nepřetržitý přístup k diagnostice systému a výkonnostním metrikám.


### Interpretace záznamů spouštěcí sekvence a běžného provozu


Zaváděcí sekvence poskytuje důležité informace o hardwarové konfiguraci a inicializačním procesu zařízení Bitaxe. Normální spouštěcí protokoly začínají informacemi o verzi ESP-IDF, po nichž následuje charakteristické "Welcome to the Bitaxe. Hack the planet", která potvrzuje úspěšné nahrání firmwaru. Poté systém zobrazí konfiguraci frekvence ASIC, identifikaci modelu zařízení a podrobnosti o verzi desky.


Správně fungující zařízení bude vykazovat úspěšnou inicializaci I2C a regulaci napětí ASIC nastavenou na 1,2 V. V protokolech se zobrazí informace o stavu GPIO a inicializační sekvence Wi-Fi, po nichž následuje konfigurace serveru DHCP a přiřazení IP adresy. Jedním z nejdůležitějších ukazatelů je zpráva o detekci čipu ASIC, která by měla u jednočipového zařízení hlásit "detekován jeden čip ASIC". Toto potvrzení potvrzuje, že hardware mining je správně připojen a komunikuje s řadičem ESP32.


Provozní protokoly ukazují, že na zařízení probíhá více souběžných úloh, včetně komunikace vrstvy API, koordinace hlavní úlohy, správy úlohy ASIC a zpracování úlohy vrstvy. Tyto různé identifikátory úloh pomáhají izolovat problémy na konkrétní součásti systému. Běžný provoz zahrnuje navazování spojení s poolem, zprávy o nastavení obtížnosti, řazení a rušení úloh a hlášení o generování nonce. Úspěšné operace mining zobrazují výsledky ASIC s výpočty obtížnosti a potvrzení o odeslání mining, pokud podíly splňují požadovanou hranici.


### Identifikace poruch hardwaru a chybových vzorců


Selhání hardwaru se v protokolech projevují prostřednictvím specifických chybových vzorů, které ukazují, které komponenty nefungují správně. Nejčastějším způsobem selhání jsou chyby komunikace I2C s konkrétními integrovanými obvody na desce Bitaxe. Například poruchy komunikace s DS4432U se objevují jako zprávy "ESP_ERROR_CHECK failed" s indikátory časového limitu, které poukazují na problémy s regulací napětí nebo problémy s pájením ovlivňující součástku U10 odpovědnou za komunikaci se zobrazovačem.


Tato chybová hlášení obsahují podrobné ladicí informace, například konkrétní zdrojový soubor (main_ds4432u.c), chybné volání funkce a jádro procesoru, které úlohu zpracovává. Informace o zpětné stopě poskytují další kontext pro pokročilé řešení problémů. Podobné chybové vzorce se mohou vyskytnout u čipu EMC2101 pro řízení teploty a ventilátoru, přičemž každý z nich generuje charakteristické signatury protokolu, které pomáhají identifikovat selhávající součást.


Fyzické problémy s hardwarem se často projevují jako opakované chybové cykly, po nichž následuje restart systému. Pokud zařízení během provozu vydává slyšitelný hluk, obvykle to znamená problémy s pájením, jako jsou můstky mezi vývody součástek nebo nedostatečné pájecí spoje. I když tyto mechanické problémy nemusí vždy generate konkrétní záznamy v protokolu, vytvářejí nestabilní provozní podmínky, které se ve výstupu monitorování projevují častými pády a cykly restartů.


### Pokročilé strategie řešení problémů


Sériové monitorování poskytuje oproti webovým rozhraním pro ladění několik výhod, zejména v případě přerušovaných poruch nebo zařízení, u nichž dochází k častým restartům. Průběžné zachycování protokolů zajišťuje, že během restartů systému nedojde ke ztrátě diagnostických informací, na rozdíl od webových rozhraní, která mohou ztratit data při událostech odpojení. Tato komplexní schopnost záznamu umožňuje identifikovat vzorce poruch a korelovat konkrétní chybové stavy s hardwarem nebo faktory prostředí.


Při analýze problematických zařízení se zaměřte spíše na sled událostí vedoucích k poruchám než na izolovaná chybová hlášení. Úspěšná komunikace ASIC by měla vykazovat pravidelné zpracování úloh, generování nonce a cykly odesílání sdílených úloh. Chybějící výsledky ASIC v protokolech naznačují selhání komunikace mezi zařízením ESP32 a čipem mining, často způsobené problémy s napájením, poškozenými stopami nebo poruchami komponent.


Při systematickém řešení problémů dokumentujte vzory chyb a poruchy specifické pro jednotlivé komponenty, než vyhledáte podporu komunity. Podrobné záznamy o chybách, včetně specifických identifikátorů čipů a způsobů selhání, umožňují zkušeným uživatelům poskytovat cílené pokyny k opravám, jako jsou postupy výměny komponent nebo opravy pájení. Tento metodický přístup k ladění hardwaru výrazně zvyšuje úspěšnost oprav a zkracuje dobu řešení složitých problémů.


# Pokročilé přizpůsobení

<partId>8d333102-ecb5-5f05-bfb5-03a27b2d0d70</partId>


## Úprava desky plošných spojů

<chapterId>ca08d2a4-2b34-575b-aecc-7482a03c190e</chapterId>


:::video id=30fb0010-f560-4e96-a05b-c21dc172746e:::

KiCad představuje jeden z nejvýkonnějších dostupných open-source nástrojů pro návrh a trasování desek plošných spojů (PCB). Tento profesionální software umožňuje inženýrům i amatérům vytvářet složité elektronické návrhy umisťováním součástek na virtuální desky a trasováním složitých stop, které tyto součástky spojují. Pro vzdělávací a vývojové účely je KiCad obzvláště cenný díky své kompletní open-source povaze, která uživatelům umožňuje upravovat, přizpůsobovat a učit se z existujících návrhů bez licenčních omezení.


Projekt Bitaxe je příkladem síly vývoje hardwaru s otevřeným zdrojovým kódem a poskytuje kompletní návrh desky plošných spojů, který mohou uživatelé zkoumat, upravovat a přizpůsobovat podle svých specifických potřeb. Tato přístupnost vytváří vynikající výukové prostředí, kde mohou studenti i odborníci z praxe zkoumat reálné návrhy desek plošných spojů a zároveň rozvíjet své znalosti elektronických systémů. Možnost přizpůsobení vizuálních prvků, jako jsou loga, poskytuje přístupný vstupní bod pro uživatele, kteří mohou být zastrašeni technickou složitostí elektronického návrhu.


### Nastavení prostředí KiCad


Před zahájením jakýchkoli úprav je nezbytné správně nastavit vývojové prostředí. Úložiště Bitaxe je třeba stáhnout do místního počítače, což se obvykle provádí pomocí funkce stahování ZIP na GitHubu. Tento repozitář obsahuje všechny potřebné soubory projektu, včetně souborů projektu KiCad, knihoven komponent a konstrukční dokumentace, které jsou nezbytné pro úspěšnou úpravu.


Instalace KiCadu by měla být dokončena pomocí oficiální distribuce z webových stránek KiCadu, čímž se zajistí kompatibilita s projektovými soubory a přístup k nejnovějším funkcím. Jakmile jsou úložiště i KiCad správně nainstalovány, otevření projektu vyžaduje navigaci na soubor projektu Bitaxe Ultra KiCad ve struktuře staženého úložiště. Tento projektový soubor slouží jako centrální centrum, které propojuje všechny související návrhové soubory, knihovny komponent a konfigurační nastavení.


Prvotní pohled na komplexní návrh desky plošných spojů může působit ohromujícím dojmem, protože množství součástek, stop a vrstev vytváří hustou vizuální krajinu. Funkce 3D prohlížeče KiCadu však poskytuje neocenitelný nástroj pro pochopení fyzického rozložení a prostorových vztahů v návrhu. Tato trojrozměrná perspektiva transformuje abstraktní schématické zobrazení do realistické vizualizace finálního vyrobeného produktu, což usnadňuje pochopení rozmístění součástek a celkové estetiky návrhu.


### Proces přizpůsobení loga


Přizpůsobení loga na návrzích desek plošných spojů představuje jednu z nejpřístupnějších úprav pro nové uživatele KiCadu, která vyžaduje minimální technické znalosti a zároveň poskytuje okamžité vizuální výsledky. Proces začíná nástrojem pro převod obrázků, který transformuje standardní obrazové soubory do formátů otisků kompatibilních se softwarem pro návrh desek plošných spojů. Tento proces převodu vyžaduje pečlivou pozornost parametrům rozměrů, které se obvykle měří v milimetrech, aby bylo zajištěno správné měřítko na konečné vyrobené desce.


Pracovní postup konvertoru obrázků zahrnuje několik důležitých kroků, které určují konečný vzhled a umístění vlastních log. Výběr zdrojového obrázku by měl upřednostňovat vysoce kontrastní návrhy, které se dobře převedou do procesu sítotisku používaného při výrobě desek plošných spojů. Klíčovou se stává specifikace velikosti, protože loga musí být dostatečně velká, aby zůstala čitelná i po výrobě a zároveň nenarušovala umístění nebo funkčnost součástek. Volba mezi přední a zadní sítotiskovou vrstvou ovlivňuje jak viditelnost, tak výrobní hlediska.


Správa knihovny otisků představuje základní aspekt přizpůsobení programu KiCad, který vyžaduje, aby uživatelé pochopili, jak software organizuje a zpřístupňuje prvky návrhu. Přidání vlastních log zahrnuje vytvoření nových knihoven otisků nebo úpravu stávajících a následné správné propojení těchto knihoven ve struktuře projektu. Tento proces zajišťuje, že vlastní prvky zůstanou přístupné v různých návrhových relacích a lze je snadno sdílet s ostatními členy týmu nebo spolupracovníky.


### Pokročilý průzkum a porozumění designu


Kromě jednoduchého přizpůsobení loga poskytuje KiCad výkonné nástroje pro zkoumání a pochopení složitých návrhů desek plošných spojů. Systém správy vrstev umožňuje uživatelům selektivně zobrazovat různé aspekty návrhu, od umístění a směrování součástek až po výrobní specifikace a informace o sestavě. Tento vrstevnatý přístup umožňuje podrobnou analýzu konkrétních prvků návrhu bez vizuálního nepořádku způsobeného nesouvisejícími součástmi.


Analýza trasování stop představuje jeden z nejvzdělávanějších aspektů průzkumu DPS, který odhaluje, jak probíhají elektrická spojení mezi součástmi a subsystémy. Sledováním jednotlivých stop nebo skupin souvisejících signálů si uživatelé mohou vytvořit představu o funkčnosti obvodu a rozhodnutích o návrhu. Například zkoumání napájecích distribučních sítí odhaluje, jak regulace napětí a filtrační komponenty spolupracují, aby poskytovaly čisté a stabilní napájení citlivým elektronickým součástkám.


Vztah mezi návrhem schématu a fyzickým uspořádáním je zřejmý díky pečlivému zkoumání umístění součástek a rozhodnutí o směrování. Pochopení toho, proč jsou konkrétní součástky umístěny na určitá místa, jak tepelné aspekty ovlivňují rozhodnutí o uspořádání a jak požadavky na integritu signálu ovlivňují volbu směrování, poskytuje cenné informace o profesionálních postupech při navrhování desek plošných spojů. Tyto znalosti jsou neocenitelné pro uživatele, kteří vyvíjejí vlastní návrhy nebo upravují stávající návrhy pro konkrétní aplikace.


Komplexní nástroje KiCad pro kontrolu a ověřování návrhových pravidel zajišťují, že změny zachovávají elektrickou a výrobní kompatibilitu. Tyto automatizované systémy pomáhají předcházet běžným návrhovým chybám a zároveň vzdělávají uživatele v oblasti průmyslových norem a osvědčených postupů. Integrace 3D vizualizace s elektrotechnickými návrhovými daty vytváří výkonné výukové prostředí, kde se teoretické koncepty stávají hmatatelnými prostřednictvím vizuálního zobrazení a interaktivního zkoumání.


## Jak vytvořit tovární soubor?

<chapterId>e9da631c-e6d1-50c1-bb59-bc8455c29d3e</chapterId>


:::video id=07f980bf-6052-4ed4-bf7b-75e8aba585df:::

Sestavení vlastního firmwaru pro zařízení mining na bázi ESP vyžaduje pečlivou pozornost konfiguraci, závislostem a správnému procesu sestavení. Tento komplexní průvodce vás provede kompletním procesem vytváření standardních binárních souborů firmwaru i továrních souborů, které obsahují předkonfigurovaná nastavení, což zefektivňuje nasazení a zkracuje dobu nastavení pro koncové uživatele.


Všimněte si, že tato kapitola je poměrně odborná a můžete ji jednoduše projít, pokud vás zajímá.


### Nastavení vývojového prostředí


Chcete-li začít s vývojem firmwaru ESP-Miner, měli byste vytvořit vhodné vývojové prostředí v programu Visual Studio Code, nejlépe na linuxové distribuci. Základem tohoto nastavení je rozšíření ESP-IDF, které poskytuje potřebné nástroje a integraci rámce pro vývoj ESP32. Při první instalaci rozšíření ESP-IDF se uživatelé setkají s průvodcem nastavením, který usnadňuje proces konfigurace.


Důležitým faktorem v procesu nastavení je výběr vhodné verze ESP-IDF. Ačkoli dříve byla doporučována verze 5.1.3, praktické zkušenosti ukázaly, že tato verze může způsobovat problémy při sestavování, které komplikují proces vývoje. Doporučený postup nyní zahrnuje použití ESP-IDF verze 5.3 Beta 1, která tyto komplikace při sestavování prokazatelně řeší a zajišťuje správnou funkci zařízení Bitaxe. Proces instalace vyžaduje výběr možnosti expresní instalace a konkrétní výběr verze 5.3 Beta 1 z dostupných možností.


Nastavení vývojového prostředí přesahuje rámec instalace ESP-IDF a zahrnuje i správnou konfiguraci terminálu. Visual Studio Code poskytuje několik metod přístupu k funkcím ESP-IDF, včetně možnosti otevřít terminál ESP-IDF pomocí příkazové palety nebo pomocí speciální ikony terminálu umístěné v rozhraní. Toto specializované terminálové prostředí zajišťuje správnou funkci všech příkazů ESP-IDF a poskytuje přístup ke kompletnímu řetězci nástrojů.


### Konfigurace nastavení ESP-Miner


Konfigurační soubor představuje jádro procesu přizpůsobení ESP-Miner a obsahuje všechny základní parametry, které určují, jak bude zařízení fungovat v cílovém prostředí. Tato konfigurace zahrnuje nastavení sítě, připojení k poolu mining a parametry specifické pro hardware, které musí být přizpůsobeny konkrétnímu scénáři nasazení.


Konfigurace sítě je hlavní součástí procesu nastavení a vyžaduje zadání pověření Wi-Fi včetně identifikátoru SSID a hesla. Namísto použití zástupných hodnot jako "test" by produkční konfigurace měly obsahovat skutečná síťová pověření, která bude zařízení používat v provozním prostředí. Konfigurace také umožňuje různá nastavení poolu mining, přičemž podporuje jak konfigurace soukromého poolu s konkrétními IP adresami, tak veřejné pooly, jako je public-pool.io, s odpovídajícím nastavením portů.


Konfigurační parametry specifické pro Mining zahrnují nastavení uživatele vrstvy, které obvykle odpovídá adrese Bitcoin, kam mají být směrovány odměny mining. Další hardwarové parametry, jako je nastavení frekvence, konfigurace napětí a specifikace typu ASIC, musí odpovídat cílové hardwarové platformě. Úložiště GitHub poskytuje předkonfigurované příklady pro různé hardwarové varianty, například konfiguraci BM1368 určenou pro zařízení Super a nastavení BM1366 pro varianty Ultra. Specifikace verze desky, jako je nastavení verze portu na 401 pro novější revize hardwaru, zajišťují kompatibilitu se specifickými vlastnostmi cílového zařízení.


### Sestavení webového Interface a základního firmwaru


Projekt ESP-Miner obsahuje sofistikované webové rozhraní, které vyžaduje samostatnou kompilaci před zahájením hlavního procesu sestavování firmwaru. Toto webové rozhraní, označované jako firmware AxeOS, poskytuje uživatelům komplexní rozhraní pro správu a monitorování a ovládání zařízení mining.


Proces sestavení webového rozhraní začíná přechodem do adresáře serveru HTTP v rámci hlavní struktury úložiště, konkrétně do podadresáře AxeOS. Toto umístění obsahuje webovou aplikaci založenou na Node.js, která vyžaduje instalaci závislostí prostřednictvím příkazu npm install. Systém sestavení předpokládá, že je Node.js ve vývojovém systému řádně nainstalován, protože to představuje základní požadavek pro proces kompilace webového rozhraní.


Po instalaci závislostí příkaz npm run build zkompiluje komponenty webového rozhraní a vytvoří potřebné soubory, které budou vloženy do firmwaru ESP32. Tento proces kompilace vytváří optimalizované webové prostředky, které poskytují funkce uživatelského rozhraní při zachování efektivního využití paměti na omezené platformě ESP32. Úspěšné dokončení tohoto kroku sestavení je nezbytné před pokračováním v kompilaci hlavního firmwaru, protože firmware ESP-Miner obsahuje tyto komponenty webového rozhraní jako nedílnou funkcionalitu.


### Vytváření továrních souborů s vloženou konfigurací


Vytvoření továrních souborů představuje pokročilou strategii nasazení, která vkládá konfigurační nastavení přímo do binárního souboru firmwaru, čímž se eliminuje nutnost ruční konfigurace během nastavování zařízení. Tento přístup se osvědčuje zejména při rozsáhlém nasazení nebo v situacích, kdy je nezbytná konzistentní konfigurace více zařízení.


Proces vytváření továrního souboru začíná vygenerováním konfiguračního binárního souboru z konfiguračního souboru CSV pomocí nástroje generátoru oddílů NVS ESP-IDF. Tento nástroj, který se nachází v adresáři komponent ESP-IDF pod položkou nvs-flash/nvs-partition-generator, převádí lidsky čitelnou konfiguraci do binárního formátu vhodného pro přímé uložení do paměti flash. Skript nvs-partition-gen.py zpracuje soubor config.csv a vygeneruje soubor config.binary, který je zaměřen na adresní prostor paměti 0x6000.


Konečné sestavení továrních souborů využívá specializované slučovací skripty, které kombinují binární soubory jádra firmwaru s konfiguračními daty. Úložiště poskytuje několik možností sloučení, včetně standardního slučovacího skriptu pro základní tovární soubory a slučovacího skriptu zahrnujícího konfiguraci pro komplexní tovární soubory. Skript merge-bin-with-config.sh vytváří tovární soubory, které obsahují jak funkce firmwaru, tak předkonfigurovaná nastavení, čímž vzniká kompletní balíček pro nasazení. Tento přístup umožňuje vytvářet tovární soubory specifické pro konkrétní zařízení, například verze přizpůsobené pro zařízení Bitaxe Ultra s konkrétními revizemi desek, a zároveň zachovává flexibilitu pro obecné tovární soubory generate bez vložených konfigurací pro scénáře vyžadující flexibilitu ručního nastavení.


Hotové tovární soubory poskytují týmům pro nasazení binární soubory připravené k flashování, které obsahují všechny potřebné součásti firmwaru a konfigurační nastavení, což zjednodušuje proces poskytování zařízení a zajišťuje konzistentní provozní parametry všech nasazených zařízení mining.


## Jak používat Bitaxe Web Flasher?

<chapterId>8c3e2d4c-c038-53ec-93cb-cc30a29e4394</chapterId>


:::video id=291757b9-f459-48f6-8766-56387f907859:::

Webový instalátor Bitaxe představuje zjednodušený přístup ke správě firmwaru pro zařízení Bitaxe a poskytuje uživatelům více možností instalace prostřednictvím webového rozhraní. Tento komplexní nástroj odstraňuje složitost tradičně spojenou s aktualizacemi firmwaru a novými instalacemi a zpřístupňuje správu zařízení uživatelům bez ohledu na jejich technické znalosti. Pochopení správného používání tohoto instalačního programu je klíčové pro udržení optimálního výkonu zařízení a vyhnutí se běžným nástrahám, které mohou zařízení dočasně vyřadit z provozu.


### Požadavky na přístup a kompatibilitu prohlížeče


Webový instalátor Bitaxe je přístupný prostřednictvím vyhrazené adresy URL [https://bitaxeorg.github.io/bitaxe-web-flasher/](https://bitaxeorg.github.io/bitaxe-web-flasher/) (adresa uvedená ve videu je nyní zastaralá) a slouží jako centrální centrum pro všechny činnosti spojené s instalací firmwaru. Úspěšné fungování tohoto webového nástroje však vyžaduje kompatibilitu s prohlížečem, protože instalátor spoléhá na specifické webové technologie, které nejsou univerzálně podporovány ve všech prohlížečích. Jako hlavní doporučený prohlížeč pro instalační program je Chrome, který poskytuje plnou kompatibilitu se všemi funkcemi a vlastnostmi. Ostatní prohlížeče založené na Chromu mohou nabízet podobné funkce, ale populární alternativy, jako jsou Brave a Firefox, postrádají potřebnou podporu webových sérií API, takže jsou nekompatibilní se základními operacemi instalačního programu.


Toto omezení prohlížeče vyplývá z toho, že instalátor spoléhá na přímou sériovou komunikaci se zařízeními Bitaxe prostřednictvím webového rozhraní. Webové sériové rozhraní API, které tuto komunikaci umožňuje, zůstává relativně novým webovým standardem, který zatím nedosáhl všeobecného přijetí v prohlížečích. Uživatelé, kteří se pokusí přistupovat k instalačnímu programu prostřednictvím nepodporovaných prohlížečů, se setkají s chybami připojení a nemožností komunikovat se svými zařízeními, což vyžaduje přechod na kompatibilní prohlížeč před pokračováním v jakýchkoli instalačních činnostech.


### Požadavky na napájení a příprava zařízení


Zařízení Bitaxe vykazují různé požadavky na napájení v závislosti na konkrétním modelu a verzi, takže správná správa napájení je pro úspěšnou instalaci firmwaru nezbytná. Zařízení s verzí 204 nebo nižší mohou pracovat výhradně prostřednictvím napájení z USB a odebírat z připojeného počítače dostatečný proud pro zachování provozu během procesu flashování. Díky tomuto zjednodušenému způsobu napájení jsou tyto starší verze obzvláště vhodné pro aktualizaci firmwaru, protože uživatelům stačí k zahájení instalačního procesu připojit jediný kabel USB.


Zařízení s verzí 205 a vyšší však vyžadují kromě připojení USB také externí zdroje napájení, což odráží změny ve spotřebě energie a konstrukci obvodů v novějších revizích hardwaru. Tato zařízení nemohou odebírat dostatečné množství energie pouze prostřednictvím rozhraní USB, což vyžaduje připojení k jejich standardním zdrojům napájení během instalace firmwaru. Nezajištění odpovídajícího napájení těchto novějších zařízení bude mít za následek selhání instalace a možné poškození procesu aktualizace firmwaru.


Proces fyzického připojení vyžaduje specifické načasování a manipulaci s tlačítky, aby byla zajištěna správná komunikace mezi instalátorem a zařízením. Uživatelé musí před připojením kabelu USB-C k počítači stisknout a podržet spouštěcí tlačítko na zařízení Bitaxe. Tato sekvence uvede zařízení do režimu zavaděče a umožní instalačnímu programu komunikovat přímo s úložištěm firmwaru zařízení. Připojení kabelu USB před stisknutím spouštěcího tlačítka povede k normálnímu provozu zařízení, nikoli k režimu bootloaderu, který je nutný pro instalaci firmwaru, a zabrání instalačnímu programu v navázání potřebného komunikačního kanálu.


### Možnosti instalace a jejich použití


Webový instalátor Bitaxe nabízí čtyři různé možnosti instalace, z nichž každá je určena pro specifické případy použití a konfigurace zařízení. Bitaxe Superboard verze 4.0.1 představuje nejaktuálnější firmware pro zařízení modelu Super, verze 4.0.2 je plánována na budoucí vydání. Tato možnost zahrnuje jak tovární, tak aktualizační varianty, což poskytuje flexibilitu v přístupu k instalaci na základě potřeb uživatele a stavu zařízení.


Tovární instalace představují kompletní výměnu firmwaru, která odráží původní výrobní proces, včetně komplexních postupů autotestování, které ověřují funkčnost zařízení ve všech systémech. Když uživatelé zvolí tovární instalaci, instalátor provede úplné vymazání stávajícího firmwaru a konfiguračních dat a nahradí je novou, čistou instalací, která je identická s instalací použitou při výrobě. Tento proces zahrnuje automatické autotestování, které ověřuje správnou funkci hardwaru a po jehož dokončení musí uživatelé zařízení restartovat, aby mohli pokračovat v normálním provozu. Tovární instalace se osvědčují zejména v případech, kdy se u zařízení objevují přetrvávající problémy nebo kdy si uživatelé přejí vrátit svá zařízení do původních továrních specifikací.


Aktualizační instalace představují konzervativnější přístup, který zachovává stávající konfigurační data a aktualizuje pouze základní součásti firmwaru. Tato možnost je ideální pro uživatele, kteří si přizpůsobili nastavení svého zařízení a chtějí zachovat své osobní konfigurace a zároveň využívat vylepšení firmwaru a opravy chyb. Proces aktualizace se zaměřuje pouze na součásti firmwaru, které vyžadují změnu, přičemž specifická uživatelská nastavení, pověření WiFi a adresy Bitcoin zůstávají během celého procesu instalace nedotčeny.


### Kritické aspekty instalace a ochrany dat


Rozdíl mezi instalací z výroby a aktualizací má významné důsledky pro konfiguraci zařízení a zachování uživatelských dat. Tovární instalace provede úplné vymazání zařízení a odstraní všechna uživatelská nastavení včetně pověření WiFi, adres Bitcoin a všech personalizovaných parametrů zařízení. Po tovární instalaci se uživatelé musí znovu připojit k výchozí síti WiFi zařízení a znovu nakonfigurovat všechna osobní nastavení od začátku, což v podstatě znamená, že se zařízením zachází, jako by bylo zcela nové od výrobce.


Při instalaci aktualizací je třeba věnovat zvýšenou pozornost možnosti vymazání zařízení, která se zobrazuje během instalačního procesu. Instalační program vyzve uživatele otázkou "Do you want to erase the device before installing Bitaxe Flasher?" (Chcete vymazat zařízení před instalací programu Bitaxe Flasher?), která je doprovázena varováním, že všechna data v zařízení budou ztracena. Uživatelé provádějící instalaci aktualizací musí tuto možnost odmítnout kliknutím na tlačítko "Další", místo aby potvrdili operaci vymazání. Přijetí možnosti vymazání během instalace aktualizace odstraní konfigurační soubor zařízení, což může způsobit, že zařízení nebude funkční, dokud nebude obnovena správná konfigurace. Tato situace sice zařízení trvale nepoškodí, ale způsobuje zbytečné komplikace a vyžaduje další konfigurační kroky k obnovení normálního provozu.


Samotný proces instalace probíhá automaticky, jakmile uživatelé provedou výběr a potvrdí své volby. Instalační program se stará o všechny technické aspekty přenosu a ověření firmwaru a v průběhu celého procesu poskytuje ukazatele průběhu a aktualizace stavu. Tento automatizovaný přístup eliminuje potřebu uživatelů rozumět složitým postupům instalace firmwaru a zároveň zajišťuje spolehlivé a konzistentní výsledky u různých modelů zařízení a verzí firmwaru.


## Jak vytvořit a objednat desku plošných spojů?

<chapterId>566f5e06-9ec9-55c0-84f6-101d6ca4c2ff</chapterId>


:::video id=9a56ad84-d9cf-4f85-ab98-301fb3101228:::

Tato kapitola se zaměřuje na praktický postup generování výrobních souborů z projektů KiCad a objednávání profesionálních desek plošných spojů od online výrobců. Na příkladu projektu Bitaxe projdeme celý pracovní postup od generování souborů až po objednávku u výrobce desek plošných spojů.


### Pochopení procesu výroby desek plošných spojů


Cesta od dokončeného návrhu v programu KiCad k fyzickému PCB zahrnuje několik důležitých kroků, které překlenují propast mezi digitálním návrhem a fyzickou výrobou. Při práci na složitých projektech, jako je Bitaxe, poskytuje editor DPS v KiCadu komplexní pohled na váš návrh a zobrazuje všechny komponenty a jejich vzájemná propojení prostřednictvím barevných stop. Červené a modré čáry, které vidíte, představují elektrická spojení mezi různými integrovanými obvody a součástkami na desce. Funkce 3D prohlížeče v KiCadu umožňuje vizualizovat, jak bude vypadat konečná sestavená deska, a poskytuje tak cenný přehled o rozmístění součástek a případných mechanických konfliktech.


Výrobní proces vyžaduje specifické formáty souborů, které mohou výrobci desek plošných spojů interpretovat a použít k výrobě vašich desek. Tyto soubory obsahují přesné informace o vrstvách mědi, vrtaných otvorech, umístění součástek a další výrobní specifikace. Pochopení tohoto pracovního postupu je nezbytné, ať už pracujete se standardním návrhem Bitaxe, nebo vytváříte úpravy, jako je přidání vlastních log, změna hodnot součástek nebo úprava rozložení desky podle konkrétních požadavků.


### Generování souborů Gerber pro výrobu


Soubory Gerber slouží jako průmyslový standard pro předávání informací o návrhu PCB výrobcům. Tyto soubory obsahují všechna data potřebná pro výrobu DPS, včetně vzorů měděných vrstev, definic pájecích masek a umístění vrtaných otvorů. Chcete-li tyto soubory generate v programu KiCad, přejděte do editoru DPS a přes nabídku Soubory získejte přístup k výstupům pro výrobu. Software automaticky nakonfiguruje příslušná nastavení pro standardní výrobní procesy, včetně správné struktury výstupních adresářů obvykle organizovaných jako "výrobní soubory/gerbery"


Proces generování vytvoří několik souborů Gerber, z nichž každý představuje různé aspekty návrhu desky plošných spojů. Tyto soubory spolupracují a poskytují výrobcům kompletní výrobní pokyny. Po vygenerování musí být tyto soubory zkomprimovány do archivu ZIP, protože většina výrobců desek plošných spojů očekává právě tento standardní formát. Soubor ZIP obsahuje všechna potřebná výrobní data a zajišťuje, že během procesu odesílání na webové stránky výrobce nedojde ke ztrátě nebo poškození souborů.


Stojí za zmínku, že mnoho projektů s otevřeným zdrojovým kódem, včetně Bitaxe, často obsahuje ve svých úložištích předem vygenerované výrobní soubory. Při úpravách návrhu nebo práci s různými verzemi desek je však zásadní pochopit, jak tyto soubory generate sami vytvořit. Tyto znalosti se stávají obzvláště cennými při přizpůsobování návrhů nebo řešení problémů s výrobou.


### Výběr výrobců PCB a porozumění možnostem


V oblasti výroby desek plošných spojů existuje několik renomovaných možností, z nichž mezi nejoblíbenější patří společnosti JLCPCB a PCBWay, a to jak pro amatérské, tak pro profesionální uživatele. Oba výrobci poskytují podobné služby s konkurenceschopnými cenami a spolehlivou kvalitou, ačkoli každý z nich má specifické výhody v závislosti na požadavcích vašeho projektu. JLCPCB často láká začínající uživatele na propagační ceny a uživatelsky přívětivá rozhraní, zatímco PCBWay může nabízet různé možnosti materiálů nebo specializované služby.


Při nahrávání souborů Gerber na webové stránky výrobce systém automaticky analyzuje váš návrh a nabídne různé možnosti výroby. Výchozí nastavení poskytovaná těmito platformami jsou obvykle vhodná pro většinu standardních návrhů a obecně se doporučuje tato nastavení zachovat, pokud nemáte specifické požadavky. Mezi klíčové parametry patří tloušťka desky plošných spojů, hmotnost mědi, povrchová úprava a minimální množství. Většina výrobců vyžaduje minimální objednávky pěti desek, což ve skutečnosti dobře funguje u hobby projektů, kde je výhodné mít náhradní desky nebo se o ně podělit s přáteli.


Barevné varianty představují jednu z mála estetických možností, které jsou během výrobního procesu k dispozici. Zatímco zelená zůstává tradiční a cenově nejvýhodnější variantou, výrobci obvykle nabízejí alternativy včetně modré, červené, žluté, fialové a černé. Volba barvy je čistě estetická a nemá vliv na elektrický výkon desky plošných spojů, ačkoli některé barvy mohou mít mírný vliv na náklady nebo delší dobu výroby.


### Úvahy o pokročilé výrobě a možnosti montáže


Kromě základní výroby desek plošných spojů nabízejí moderní výrobci další služby, které mohou výrazně zefektivnit dokončení vašeho projektu. Jednou z nejcennějších doplňkových služeb jsou šablony, zejména pro návrhy s komponentami s jemnou roztečí, jako jsou čipy ASIC, které se nacházejí v projektech Bitcoin mining. Šablona je v podstatě přesně vyřezaná hliníková šablona s otvory, které přesně odpovídají umístění pájecích plošek na desce plošných spojů. Tento nástroj umožňuje konzistentní a přesné nanášení pájecí pasty, což výrazně zlepšuje kvalitu montáže a snižuje pravděpodobnost chyb při pájení.


Možnosti šablon obvykle zahrnují jednotlivé šablony s horním i spodním vzorem nebo samostatné šablony pro každou stranu desky. Pro většinu projektů se jako pohodlnější a cenově výhodnější jeví kombinovaná šablona. Tloušťka šablony je pečlivě vypočtena tak, aby se naneslo odpovídající množství pájecí pasty pro konkrétní typy součástek a velikosti podložek. Použití šablony mění to, co by mohlo být zdlouhavým a na chyby náchylným ručním procesem, v rychlý a profesionální krok montáže.


Někteří výrobci sice nabízejí částečnou nebo kompletní montáž, ale u složitých projektů, jako je Bitaxe, je třeba tyto možnosti pečlivě zvážit. Při rozhodování je třeba zohlednit dostupnost součástek, náklady a vzdělávací hodnotu vlastní montáže. Mnohé specializované součásti potřebné pro projekty Bitcoin mining nemusí být snadno dostupné prostřednictvím standardních služeb osazování desek plošných spojů, a proto je praktičtějším přístupem obstarávání součástí a ruční osazování. Další díly tohoto seriálu se budou zabývat strategiemi získávání součástek a technikami osazování, které vám pomohou úspěšně dokončit projekt Bitaxe od holé desky plošných spojů až po funkční zařízení.


Výrobní a montážní proces představuje klíčový most mezi digitálním návrhem a fyzickou realizací. Pochopení těchto pracovních postupů vám umožní převzít kontrolu nad svými projekty, snížit náklady a získat cenné praktické zkušenosti s profesionálními výrobními procesy. Ať už vytváříte jediný prototyp, nebo plánujete malou sériovou výrobu, zvládnutí těchto dovedností vám otevře nové možnosti, jak uvést vaše elektronické návrhy do života.


# Optimalizace výkonu

<partId>87b8790f-b7a9-5286-a7f8-328176ef7cb5</partId>


## Srovnávací test zařízení Bitaxe

<chapterId>7259a4b1-93c1-5956-87d3-baaee58115af</chapterId>


:::video id=2491a783-9750-4ea5-a40c-1d1d611784d5:::

Snaha o dosažení optimálního výkonu mining vyžaduje systematický přístup ke konfiguraci hardwaru, který vyvažuje hashrate, účinnost a tepelné řízení. Bitaxe nabízí řadu konfiguračních parametrů, které mohou významně ovlivnit výkon, ale ruční testování každé kombinace nastavení by bylo nepraktické a časově náročné. Tato kapitola se zabývá tím, jak využít automatizované nástroje pro benchmarking k vědecké optimalizaci výkonu zařízení Bitaxe při zachování bezpečných provozních podmínek.


### Porozumění metrikám výkonu Bitaxe a základní konfiguraci


Než se začnete zabývat optimalizačními technikami, je nezbytné pochopit klíčové ukazatele výkonnosti, které definují provozní efektivitu vašeho systému Bitaxe. Mezi hlavní ukazatele patří hashrate měřený v terahash za sekundu, energetická účinnost vyjádřená v joulech na terahash, frekvence ASIC v megahertzích a napětí jádra ve voltech. Dobře nakonfigurovaný Bitaxe by mohl dosáhnout přibližně 1,1 terahash s účinností přibližně 17 joulů na terahash, pracující na frekvenci 550 megahertzů s naměřeným napětím ASIC 1,14 voltu. Tato základní čísla poskytují referenční bod pro pochopení potenciálních zlepšení, která jsou k dispozici díky systematické optimalizaci.


Vztah mezi těmito ukazateli je složitý a vzájemně závislý. Vyšší frekvence obvykle zvyšují hashrate, ale také zvyšují spotřebu energie a produkci tepla. Podobně úpravy napětí ovlivňují jak výkon, tak tepelné charakteristiky. Výzva spočívá v nalezení optimální rovnováhy, která maximalizuje buď hashrate, nebo účinnost při zachování stabilního provozu v bezpečných teplotních mezích. Tento optimalizační proces vyžaduje metodické testování v mnoha kombinacích parametrů, díky čemuž jsou pro dosažení optimálních výsledků neocenitelné automatizované nástroje.


### Architektura benchmarkového nástroje Bitaxe Hashrate


Nástroj [Bitaxe Hashrate Benchmark](https://github.com/mrv777/Bitaxe-Hashrate-Benchmark/) představuje sofistikované řešení založené na Pythonu, které původně vyvinul WhiteCookie a následně vylepšil mrv777. Tento nástroj s otevřeným zdrojovým kódem, šířený pod licencí GPLv3, automatizuje složitý proces testování mnoha kombinací konfigurace s cílem určit optimální nastavení pro konkrétní hardware. Hlavní síla nástroje spočívá v jeho systematickém přístupu k testování parametrů, kdy postupně upravuje nastavení frekvence a napětí a zároveň průběžně sleduje výkonnostní metriky a tepelné podmínky.


Proces srovnávání obvykle trvá 30 až 40 minut, během nichž nástroj metodicky testuje různé kombinace nastavení frekvence a napětí ASIC. Nástroj začíná s konzervativním základním nastavením, které obvykle začíná na 1,15 V a 500 megahertzích, a poté tyto parametry postupně zvyšuje, přičemž sleduje hashrate, teplotu a stabilitu. Důležité je, že nástroj upřednostňuje bezpečný provoz před maximálním výkonem a automaticky ustupuje od nastavení, která způsobují nadměrnou tvorbu tepla nebo nestabilitu. Tento konzervativní přístup zajišťuje, že proces optimalizace neohrozí životnost nebo spolehlivost hardwaru.


### Požadavky na instalaci a nastavení


Implementace nástroje Bitaxe Hashrate Benchmark vyžaduje několik nezbytných softwarových komponent v místním počítači. Mezi hlavní požadavky patří Python pro spouštění benchmarkových skriptů, Git pro správu úložiště a volitelně Visual Studio Code pro rozšířené možnosti vývojového prostředí. Nástroj lze sice ovládat z rozhraní příkazového řádku, ale použití integrovaného vývojového prostředí, jako je VS Code, poskytuje lepší přehled o procesu srovnávání a analýze výsledků.


Instalační proces probíhá podle standardních postupů pro vývoj Pythonu a začíná klonováním úložiště z GitHubu do místního počítače. Po stažení úložiště je třeba vytvořit virtuální prostředí, abyste izolovali závislosti nástroje od instalace Pythonu ve vašem systému. Tato izolace zabrání možným konfliktům s jinými aplikacemi Python a zajistí konzistentní fungování. Po aktivaci virtuálního prostředí nainstalujete požadované závislosti pomocí dodaného souboru s požadavky, který automaticky nakonfiguruje všechny potřebné knihovny a moduly pro správnou funkci nástroje.


### Provádění srovnávacích testů a interpretace výsledků


Spuštění benchmarku vyžaduje provedení jediného příkazu Pythonu, který jako parametr obsahuje IP adresu vašeho zařízení Bitaxe. Nástroj se automaticky připojí k webovému rozhraní vašeho těžaře a zahájí systematický proces testování. Během provádění nástroj poskytuje podrobné informace o záznamu, které ukazují aktuální iteraci testu, použité nastavení napětí a frekvence, výsledné hodnoty hashrate, vstupní napětí, naměřené teploty a tepelné údaje z kritických komponent, jako je například buck konvertor. Tato zpětná vazba v reálném čase umožňuje sledovat průběh srovnávacího testu a pochopit, jak různá nastavení ovlivňují výkon vašeho mineru.


Inteligentní tepelná správa nástroje se projeví, když se teplota přiblíží bezpečnostní hranici 66 stupňů Celsia. Namísto překročení bezpečných provozních limitů benchmark automaticky sníží nastavení, aby byla zachována tepelná stabilita. Tento konzervativní přístup zajišťuje, že optimalizační proces upřednostňuje dlouhodobou spolehlivost hardwaru před krátkodobým zvýšením výkonu. Po dokončení nástroj vygeneruje komplexní výsledky ve formátu JSON a sestaví žebříček pěti nejlepších konfigurací pro maximální hashrate i optimální účinnost. Tyto výsledky poskytují jasné vodítko pro výběr konfigurace, která nejlépe odpovídá vašim provozním prioritám, ať už je zaměřena na maximální výkon nebo energetickou účinnost.


Nástroj pro benchmarking nabízí také možnosti přizpůsobení pro pokročilé uživatele, kteří chtějí upravit parametry testování. Argumenty příkazového řádku umožňují zadat vlastní počáteční napětí a frekvence, což umožňuje cílenější optimalizaci pro konkrétní případy použití. Například pokud již víte, že váš hardware funguje dobře při vyšších frekvencích, můžete benchmark spustit při vyšších nastaveních, místo abyste začali od konzervativních výchozích hodnot. Díky této flexibilitě je nástroj cenný jak pro začínající uživatele, kteří hledají automatickou optimalizaci, tak pro zkušené těžaře, kteří chtějí doladit konkrétní výkonnostní charakteristiky.


## Přetaktování zařízení Bitaxe

<chapterId>6b48c0c6-51c3-51a3-b317-850a374ae61e</chapterId>


:::video id=46c7a442-cd72-477c-8c91-b2c489ada1e6:::

Přetaktování zařízení Bitaxe vyžaduje pečlivé zvážení hardwarových omezení i požadavků na chlazení. Zatímco mnoho uživatelů dává přednost podtaktování svých zařízení pro tišší provoz, pochopení správných technik přetaktování je nezbytné pro ty, kteří hledají maximální výkon bez poškození hardwaru. Tento proces zahrnuje zvýšení frekvence a případnou úpravu nastavení napětí nad rámec továrních specifikací, což ze své podstaty zvyšuje produkci tepla a zatížení komponent.


Základem úspěšného přetaktování je odpovídající chladicí infrastruktura. Než se pokusíte o jakoukoli úpravu frekvence, musíte se ujistit, že váš Bitaxe má správné možnosti odvodu tepla. Bitaxe Gamma s kvalitním chladičem a ventilátorem poskytuje potřebnou tepelnou správu pro bezpečné přetaktování. Zařízení s malými chladiči a nedostatečnými ventilátory by se neměla přetaktovávat, protože špatný výkon chlazení povede k tepelnému throttlingu a možnému poškození hardwaru. Vztah mezi teplem a životností komponent je velmi důležité pochopit - nadměrné teplo vytváří napětí, které časem degraduje elektronické komponenty a výrazně snižuje provozní životnost zařízení.


### Strategické umístění chladiče


Nejkritičtější součástí vyžadující dodatečné chlazení je buck konvertor, malá černá součástka umístěná na zadní straně Bitaxe v blízkosti velké cívky. Toto zařízení převádí přicházející 5V napájení na napětí vhodné pro čip ASIC, obvykle kolem 1,2 V. Buckův měnič, často označovaný jako TPS, generuje během provozu značné množství tepla a představuje tepelné úzké hrdlo, které omezuje potenciál přetaktování. Instalace malého přilnavého chladiče na tuto součástku umožňuje nejen vyšší přetaktovací prostor, ale také zlepšuje celkovou účinnost snížením tepelných ztrát.


Další umístění chladiče může být přínosem pro další oblasti desky s vysokým proudem. Obvody regulace napětí jsou značně elektricky namáhány, protože napájení proudí ze vstupní části dolů přes různé stopy desky a napájí čip ASIC. Mnoho zkušených overclockerů instaluje na přední stranu desky Bitaxe v těchto oblastech s vysokým proudem chladiče, které dále zlepšují odvod tepla. Ačkoli tato dodatečná chladicí opatření nejsou pro mírné přetaktování nezbytně nutná, stávají se důležitými při zvyšování frekvencí na extrémní úroveň.


### Úvahy a omezení chladicího systému


Řadič ESP32, viditelný jako stříbrná součástka na desce, obvykle nevyžaduje další chlazení. Tato součástka samostatně generuje minimum tepla a zahřívá se pouze v důsledku tepelného přenosu z okolních komponent. Instalace chladičů v blízkosti ESP32 může potenciálně rušit přilehlou anténu Wi-Fi, což zhoršuje bezdrátové připojení a kvalitu signálu. Zaměřte úsilí na chlazení spíše na komponenty regulace napájení a oblast ASIC než na řídicí obvody.


Konfigurace se dvěma ventilátory představují příležitosti i omezení. Přidání druhého ventilátoru, který vyfukuje vzduch přes zadní stranu Bitaxe, sice může zlepšit chladicí výkon, ale firmware zařízení dokáže správně ovládat pouze jeden ventilátor. Zařízení Bitaxe má dvě hlavičky ventilátorů, ale pouze jeden ovladač ventilátorů, což znamená, že připojení dvou ventilátorů zmate firmware, protože dostává protichůdné signály o otáčkách. Tato konfigurace bude fungovat, ale může mít za následek nepředvídatelné chování řízení ventilátorů.


### Základní posouzení výkonnosti


Než se pokusíte o jakékoliv úpravy přetaktování, stanovte základní výkonnostní parametry tak, že Bitaxe budete několik hodin provozovat se základním nastavením. Prostřednictvím webového rozhraní sledujte teplotu ASIC, teplotu regulátoru napětí a procento otáček ventilátoru. Optimální provozní teploty by měly udržovat teplotu ASIC pod 60 °C a teplotu regulátoru napětí pod 60 °C za normálních podmínek. Pokud vaše zařízení již pracuje s teplotou vyšší než 65 °C u ASIC nebo 70-80 °C u regulátoru napětí při standardním nastavení, je před zahájením přetaktování nutné použít další chladicí hardware.


Systematický přístup ke zvyšování frekvence zahrnuje postupné kroky pomocí předdefinovaných možností frekvence v nabídce nastavení. Začněte výběrem dalšího dostupného kroku frekvence nad aktuálním nastavením při zachování výchozího napětí jádra. Tento konzervativní přístup vám umožní vyhodnotit tepelné dopady a dopady na stabilitu před provedením dalších změn. Nechte zařízení pracovat při každém novém nastavení frekvence po dobu nejméně 30 minut až jedné hodiny a po celou dobu vyhodnocování sledujte trendy teploty a stabilitu hash frekvence.


### Pokročilá vlastní konfigurace


Přístup k vlastnímu nastavení frekvence a napětí vyžaduje povolení rozhraní pro pokročilé přetaktování připojením "?OC" k adrese URL webového rozhraní zařízení. Tím se odemknou ruční vstupní pole pro přesné řízení frekvence a napětí, doprovázené příslušnými varováními o rizicích provozu mimo navržené parametry. Vlastní rozhraní umožňuje jemné ladění nad rámec standardních frekvenčních kroků a umožňuje zkušeným uživatelům optimalizovat výkon pro jejich specifické konfigurace chlazení.


Při použití vlastních nastavení dodržujte konzervativní velikosti přírůstků 10-15 MHz na krok nastavení. Tento metodický přístup zabraňuje náhlým tepelným skokům a umožňuje řádné testování stability na každé frekvenční úrovni. Někteří pokročilí uživatelé dosahují frekvencí kolem 700 MHz s napětím jádra nastaveným na 1,175 V nebo podobné hodnoty, ale tato extrémní nastavení vyžadují rozsáhlé úpravy chlazení a pečlivé monitorování. Regulátor napětí může pracovat při teplotách do 100 °C bez okamžitého poškození, ale vyšší teploty snižují účinnost a dlouhodobou spolehlivost. Úspěšné přetaktování vyžaduje trpělivost, systematické testování a průběžné monitorování, aby bylo dosaženo stabilního zvýšení výkonu při zachování integrity hardwaru.


# Závěrečná část

<partId>33367393-17a7-58d4-8359-79fffc6221fb</partId>


## Vyhodnoťte tento kurz

<chapterId>785f8b92-c8a6-5a65-aa39-e9753a7edf51</chapterId>

<isCourseReview>true</isCourseReview>

## Závěr

<chapterId>758baee6-2404-56fb-b534-6a39e441ae29</chapterId>

<isCourseConclusion>true</isCourseConclusion>