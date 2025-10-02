---
name: Nastavení prvního uzlu Bitcoin
goal: Pochopení, instalace, konfigurace a používání uzlu Bitcoin
objectives: 


  - Porozumět úloze a účelu uzlu Bitcoin.
  - Identifikovat různá dostupná hardwarová a softwarová řešení.
  - Nainstalujte a nakonfigurujte zařízení Full node (Bitcoin core).
  - Použijte deštník Interface a přidejte užitečné aplikace.
  - Připojení osobního modulu Wallet k jeho vlastnímu uzlu.
  - Prozkoumejte pokročilá nastavení a osvědčené postupy zabezpečení.


---
# Staňte se suverénním bitcoinerem



Pravděpodobně znáte pořekadlo "Ne vaše klíče, ne vaše mince", které nabádá k vlastní úschově vašich bitcoinů. Držení vlastních klíčů je skutečně nezbytným prvním krokem, ale nestačí to. Abyste dosáhli skutečné měnové suverenity, musíte si také nainstalovat a používat vlastní uzel Bitcoin. Tento kurz je navržen tak, aby vás provedl tímto základním krokem na vaší cestě Bitcoin!



BTC 202 je přístupný kurz, který vás naučí spřádat vlastní uzel Bitcoin, i když nejste technický expert. Začneme tím, že si definujeme, co je to uzel Bitcoin, k čemu slouží a proč je naprosto nezbytné, abyste si ho sami upředli. Poté vás krok za krokem provedu výběrem hardwaru, instalací potřebného softwaru, připojením uzlu Wallet a provedením prvních možných optimalizací, které vás posunou dále.



Provozování uzlu Bitcoin není jen možností pro odborníky, je to nutnost. Je to nástroj odolnosti, který musí pochopit a zavést každý uživatel. Tento kurz je vaším výchozím bodem k tomu, abyste se stali suverénním bitcoinářem!




+++




# Úvod


<partId>fc46ccd7-5d6d-40c3-9e9f-fbbb323c760a</partId>




## Přehled kurzů


<chapterId>916b1f86-38a4-4ede-bdb7-83841d5a7abe</chapterId>



Vítejte v kurzu BTC 202, kde se naučíte snadno a samostatně instalovat, konfigurovat a používat uzel Bitcoin. To však není vše: dozvíte se také více o místě a funkci uzlů v systému Bitcoin. V kurzu se střídá teoretický výklad s řízenou praktickou ukázkou.



### Část 1 - Úvod



V této první části kurzu si objasníme základní pojmy a poté přejdeme k přesnějším definicím. Co je to uzel? Jaké jsou rozdíly mezi uzlem, Wallet a Miner? Poté se seznámíte s protokolem Bitcoin core a jeho implementacemi. Cílem je mluvit stejným jazykem, vyhnout se zmatkům a vytvořit si pevné teoretické základy.



### Část 2 - Stát se suverénním bitcoinářem



V této druhé části začnu vysvětlením, proč je důležité provozovat vlastní uzel Bitcoin. Poté se budeme zabývat různými typy uzlů, které existují (kompletní, pruned, SPV...), jejich fungováním a technickými důsledky.



Poté vám poskytneme přehled softwaru dostupného pro provoz uzlu Bitcoin, včetně jeho výhod a nevýhod. Na závěr uvedeme několik velmi praktických doporučení pro výběr vhodného hardwaru pro vaše potřeby a rozpočet.



Tento oddíl tedy znázorňuje cestu suverénního bitcoinera: pochopit, proč je nutné provozovat uzel, zvolit typ uzlu, na základě této volby vybrat software a v závislosti na zvoleném softwaru určit vhodný hardware.



### Část 3 - Snadná instalace uzlu Bitcoin



Po dokončení této přípravy je čas přejít k praktickému využití 3. části věnované Umbrelu: domácímu cloudovému operačnímu systému, který zjednodušuje selfhosting a instalaci uzlu Bitcoin a Lightning.



Po krátkém úvodu do systému Umbrel vám poskytneme podrobný návod, který vás provede procesem instalace a konfigurace na vašem vlastním počítači. Cíl této části je jasný: mít svůj první plně funkční a synchronizovaný uzel Bitcoin.



### Část 4 - Připojení Wallet k uzlu



Nyní, když jste nastavili uzel Bitcoin, je čas jej začít používat! V této části se dozvíte, jak připojit software pro správu Wallet (jako Sparrow wallet) k vlastnímu indexeru Address (Electrs nebo Fulcrum) nebo přímo ke Bitcoin core, abyste již nebyli závislí na veřejných serverech.



Prozkoumáme také roli indexerů a různé metody připojení k uzlu (LAN, Tor, Tailscale atd.). Nakonec v poslední kapitole probereme nejužitečnější aplikace, které jsou na Umbrelu k dispozici pro běžného bitcoinera.



### Část 5 - Pokročilé koncepty a osvědčené postupy



Cílem této závěrečné části kurzu BTC 202 je prohloubit vaše znalosti. Nejprve se podíváme na osvědčené postupy, které je třeba přijmout u nového uzlu Bitcoin, a na to, jak jej dlouhodobě udržovat.



Poté se budeme věnovat některým teoretickým poznatkům z dřívějších částí kurzu, včetně podrobného pochopení procesu IBD a zjišťování vrstevníků, prozkoumání anatomie uzlu a nakonec se naučíme, jak používat soubor `Bitcoin.conf` k doladění nastavení.



### Část 6 - Závěrečná část



Stejně jako u všech kurzů Plan ₿ Network najdete v závěrečné části závěrečný test, který prověří vaše znalosti uzlů Bitcoin.



Jste připraveni zapnout svůj první uzel Bitcoin? Nastavte kurz na suverenitu!



## Co je uzel Bitcoin?


<chapterId>0a9fd4e0-94ab-405e-924c-023397393027</chapterId>



Jak popisuje jeho tvůrce Satoshi Nakamoto, Bitcoin se prezentuje jako peer-to-peer systém elektronických peněz. Tato jednoduchá věta, která je názvem bílé knihy, obsahuje mnoho vodítek k povaze Bitcoin:




- Především Satoshi popisuje Bitcoin jako "systém", jinými slovy jako ucelený soubor hardwarových a softwarových komponent, které vzájemně spolupracují za účelem poskytování určité služby nebo vykonávání určité funkce;
- Dále vysvětluje, že tento systém umožňuje používat elektronickou hotovost, tj. formu nehmotné měny;
- V neposlední řadě zdůrazňuje, že tento systém není závislý na žádném centrálním subjektu: je to systém "peer-to-peer", což znamená, že systém ovládají sami uživatelé.



Protože Bitcoin je systém, musí být nutně spuštěn na počítačích. A vzhledem k jeho peer-to-peer povaze jsou to samotní uživatelé, kdo přebírá odpovědnost za provoz těchto počítačů. To, čemu říkáme "uzel Bitcoin", je právě ten počítač, na kterém běží software implementující protokol Bitcoin (stejně jako Bitcoin core, ale k tomu se vrátíme později). Právě to umožňuje, aby protokol Bitcoin fungoval bez centrální autority: ověřování probíhá distribuovaně, na tisících nezávislých strojích patřících tisícům uživatelů.



![Image](assets/fr/047.webp)



Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. https://Bitcoin.org/Bitcoin.pdf



Právě tito uživatelé zajišťují bezpečnost systému Bitcoin. Jak vysvětluje Eric Voskuil ve své knize *Cryptoeconomics*, bezpečnost Bitcoin nespočívá ani na Blockchain, ani na hashovací síle, ani na validaci, decentralizaci, kryptografii, open source, ani na teorii her. Bezpečnost Bitcoin závisí především na jednotlivcích, kteří jsou ochotni vystavit se osobnímu riziku. Decentralizace umožňuje toto riziko rozložit na velké množství jednotlivců a pouze jejich schopnost odolat zajišťuje robustnost systému.



Tento princip je snadno pochopitelný: pokud by Bitcoin závisel na jediném uzlu, který by vlastnila jediná osoba, stačilo by k odstavení sítě uvěznit tuto osobu, protože by sama nesla veškerá rizika. V případě desítek tisíc uzlů rozmístěných po celém světě se riziko šíří: k odstavení Bitcoin by bylo třeba zneškodnit každého z těchto provozovatelů.



![Image](assets/fr/048.webp)



Můžeme tedy rozlišit a pojmenovat několik pojmů, které nám objasní další průběh tohoto kurzu:




- Bitcoin měna: zúčtovací jednotka používaná pro transakce v tomto systému;
- Síť Bitcoin: množina všech propojených uzlů;
- Uzly Bitcoin: počítače s implementací Bitcoin;
- Implementace Bitcoin: software, který převádí protokol na spustitelné instrukce;
- Protokol Bitcoin: soubor pravidel, jimiž se řídí fungování systému;
- Systém Bitcoin: ucelená kombinace všech těchto Elements.



### Úloha uzlu Bitcoin



Uzly Bitcoin dohromady tvoří takzvanou síť Bitcoin. Umožňují celému systému pracovat autonomně, bez využití centrálního orgánu nebo hierarchie serverů.



Systém Bitcoin byl od počátku navržen tak, aby si každý uživatel mohl spustit svůj osobní uzel. Tento případ zůstává v platnosti i u dnešního softwaru Bitcoin core, který kombinuje role Wallet a uzlu. V dnešní době je však tato funkce často oddělena: mnoho moderních peněženek Bitcoin jsou pouze peněženky, které se připojují k externím uzlům (ať už vlastněným stejnou osobou, nebo ne).



### Uchovávejte Blockchain



Prvním úkolem uzlu je udržovat místní kopii Blockchain. Aby bylo možné zabránit Double-spending na Bitcoin bez zapojení centrální autority, musí každý uživatel zkontrolovat, zda v systému neexistuje žádná transakce. Jediný způsob, jak si tím být jistý, je znát všechny transakce provedené na Bitcoin. Z tohoto důvodu jsou všechny transakce opatřeny časovým razítkem a seskupeny do bloků a každý uzel ukládá celý Blockchain.



> Jediný způsob, jak potvrdit neexistenci transakce, je mít povědomí o všech transakcích.

Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. https://Bitcoin.org/Bitcoin.pdf



Blockchain je tedy vyvíjející se registr: pokaždé, když je nový blok zveřejněn uzlem Miner, uzel zkontroluje jeho platnost a teprve poté jej přidá do své vlastní lokální kopie řetězce. K dnešnímu dni (červenec 2025) přesahuje kompletní registr Blockchain 675 GB a tato velikost stále roste, protože nový blok je přidáván v průměru každých 10 minut.



![Image](assets/fr/049.webp)



Uzel také udržuje místní záznam všech UTXO, které v daném okamžiku existují, známý jako sada **UTXO**. Tato databáze obsahuje všechny nespotřebované fragmenty Bitcoin. K tomuto tématu se podrobně vrátíme v závěrečné části kurzu.



### Ověřování a distribuce transakcí



Druhou úlohou uzlu je zajistit ověřování a šíření transakcí. Když do uzlu dorazí nová transakce (buď prostřednictvím softwaru Wallet, nebo jiného uzlu), uzel zkontroluje, zda je v souladu se souborem pravidel (pravidla konsensu a pravidla předávání). Např:




- utracené bitcoiny musí existovat v jeho sadě UTXO (databáze neutracených výstupů);
- podpis musí být platný a musí být splněny všechny podmínky výdajů (platný skript);
- celkový objem výstupů nesmí být vyšší než celkový objem vstupů, což znamená, že náklady nemohou být záporné.



![Image](assets/fr/050.webp)



Po ověření se transakce uloží do Mempool, dočasného paměťového prostoru uzlu vyhrazeného pro nepotvrzené transakce, a poté se předá ostatním síťovým partnerům, ke kterým je uzel připojen. Tento mechanismus distribuce a ověřování pokračuje z uzlu do uzlu. Tímto způsobem se transakce šíří napříč sítí Bitcoin a každý uzel ji ukládá do Mempool, dokud ji do platného bloku nezařadí uzel Miner, který pak provede její první potvrzení.



### Kontrola a distribuce bloků



Třetí úloha uzlu spočívá ve správě vytěžených bloků. Když Miner objeví nový blok s platným Proof of Work, je vysílán do sítě. Uzly jej přijmou, zkontrolují, zda odpovídá všem pravidlům protokolu, a pokud je platný, začlení jej do své vlastní lokální kopie Blockchain. Stejně jako u transakcí jsou pak nově ověřené bloky předány všem rovnocenným uzlům připojeným k uzlu. Tento proces pokračuje, dokud se o novém bloku nedozvědí všechny uzly v síti Bitcoin.



![Image](assets/fr/051.webp)



## Jaký je rozdíl mezi lukem a Wallet?


<chapterId>de5af634-a628-4b90-b869-468c208e178b</chapterId>



Při používání softwaru Bitcoin je nutné rozlišovat dva různé typy softwaru: uzel a Wallet.



Uzel Bitcoin, jak bylo uvedeno výše, je software, který se aktivně účastní sítě peer-to-peer. Plní tři hlavní úkoly:




- záloha Blockchain,
- ověřování a předávání transakcí,
- validace a předávání bloků.



Bitcoin Wallet je naopak software určený k ukládání a správě soukromých klíčů. Tyto klíče vám umožňují utrácet vaše bitcoiny splněním požadavků zamykacích skriptů (obvykle prostřednictvím podpisu). Wallet se může připojit k uzlu (ať už místnímu, nebo vzdálenému), aby mohl konzultovat stav Blockchain a vysílat transakce, které sestavuje, ale jako takový není účastníkem sítě.



V některých případech tyto dvě funkce existují současně v rámci jednoho softwaru, jako je tomu v případě Bitcoin core, který slouží jako Full node i Wallet. Mnoho populárních programů Wallet (Sparrow, BlueWallet atd.) však vyžaduje připojení k externímu uzlu (ať už vlastnímu, nebo cizímu), aby bylo možné vysílat transakce a zjišťovat zůstatek na Wallet.



![Image](assets/fr/052.webp)



## Jaký je rozdíl mezi uzlem a uzlem Miner?


<chapterId>d2992614-7ab7-4bf9-81b1-f548cda67257</chapterId>



Pojmy uzel a Miner se často zaměňují. Přesto tyto dva Elements plní v systému radikálně odlišné funkce.



Zpočátku, když Bitcoin v roce 2009 spustil Satoshi Nakamoto, se očekávalo, že se každý uživatel zapojí do sítě jako celek. Původní software Bitcoin tedy kombinoval několik funkcí najednou: fungoval jako Wallet, uzel, a také jako Miner, schopný generovat nové bloky. Obtížnost Mining byla v té době velmi nízká. Stačilo na počítači spustit software Bitcoin, abyste našli bloky a jako odměnu získali bitcoiny.



S postupnou popularizací Bitcoin a nárůstem počtu těžařů se však konkurenční prostředí v Mining radikálně změnilo. Dnes se z Mining stala mimořádně konkurenční činnost, které dominují průmysloví hráči vybavení specializovanou infrastrukturou. Výkon potřebný k vytěžení nového bloku je nyní tak velký, že je prakticky nemožné, aby toho jednotlivý uživatel dosáhl pouze pomocí běžného počítače. V důsledku toho se nyní těžba Mining provádí především pomocí specializovaných strojů zvaných ASIC (*Application-Specific Integrated Circuits*). Tyto čipy jsou optimalizovány výhradně pro běh dvojnásobného algoritmu SHA-256, který se používá pro Mining na Bitcoin.



![Image](assets/fr/053.webp)



Vzhledem k tomuto vývoji se role uzlu Bitcoin a uzlu Miner jasně odlišily. Jak bylo ukázáno výše, úloha uzlu Bitcoin je čistě informační a validační. Úloha uzlu Miner je jiná:




- Vybírá nevyřízené transakce v systému Mempool.
- Vytvoří kandidátský blok integrující tyto transakce.
- Pokusem a omylem hledá platný kód Proof of Work.
- Pokud najde platný důkaz, odvysílá blok prostřednictvím svého uzlu ostatním uzlům.



K interakci se sítí potřebuje uzel Miner uzel Bitcoin.



Úloha Miner se také někdy odlišuje od úlohy vrtulníku. Sekáček je stroj, jehož úkolem je Hash šablonovat bloky dodané serverem poolu a hledat hashe, které splňují cíl obtížnosti definovaný pro sdílení, a nikoliv pro Bitcoin. Zbytek procesu Mining, který zahrnuje vlastní konstrukci bloků, výběr transakcí nebo vyhledávání Proof-of-Work podle vlastní obtížnosti Bitcoin a také distribuci, provádí přímo pooly.



![Image](assets/fr/054.webp)



A konečně, mezi Miner a uzlem je důležitý rozdíl z hlediska ekonomické motivace. Provoz uzlu Bitcoin nepřináší žádný přímý finanční prospěch. Naproti tomu účast v uzlu Mining přináší odměny (dotace a transakční poplatky) za každý nalezený blok.



Ve 2. části se budeme podrobněji zabývat praktickými a osobními výhodami instalace a používání uzlu Bitcoin, a to nejen z čistě finančního hlediska.



## Bitcoin core a implementace protokolu


<chapterId>72381876-9317-4faa-8d41-2b252a945b8a</chapterId>



Protokol Bitcoin není software: je to soubor tichých pravidel sdílených mezi uživateli sítě. Definuje podmínky platnosti transakcí, mechanismy vytváření peněz, formát bloků, podmínky Proof-of-Work a mnoho dalších specifikací. Pro interakci s tímto protokolem musí uživatelé spustit software, který tato pravidla implementuje: ten je znám jako **implementace** protokolu Bitcoin.



Implementace je tedy software uzlu: program schopný komunikovat s ostatními počítači v síti Bitcoin, stahovat, ověřovat, ukládat a šířit bloky a transakce a lokálně vynucovat pravidla konsensu a přenosu. Každá implementace je konkrétní interpretací protokolu, napsaná v daném programovacím jazyce, s vlastní architekturou, výkonem a ergonomií. Každá implementace bude mít také svou vlastní organizaci vývoje s vlastním rozdělením odpovědností.



Mezi těmito implementacemi zdaleka dominuje jedna: **Bitcoin core**.



![Image](assets/fr/055.webp)



### Historická implementace, která se stala měřítkem



Bitcoin core je referenční software pro protokol Bitcoin. Je odvozen z původního kódu, který napsal Satoshi Nakamoto v letech 2008-2009, a je jeho přímým pokračováním. Původně byl znám jako "*Bitcoin*", poté jako "*Bitcoin QT*" (kvůli přidání grafického prostředí Interface prostřednictvím knihovny Qt) a v roce 2014 byl přejmenován na "*Bitcoin core*", aby se software jasně odlišil od sítě. Od verze 0.5 je distribuován se dvěma komponentami: (grafický Interface) a `bitcoind` (Interface pro příkazový řádek).



Teoreticky Bitcoin core nepředstavuje protokol Bitcoin; je to spíše jen jedna z mnoha implementací. Vyznačuje se však masovým přijetím, stářím, robustností kódu a přísností vývojového procesu. V důsledku toho jsou v praxi pravidla uplatňovaná protokolem Bitcoin core de facto pravidly protokolu Bitcoin: uživatelé, vývojáři, těžaři a ekosystémové služby se odvolávají téměř výhradně na něj.



### Současné rozložení implementací



Podle [údajů, které v srpnu 2025 shromáždil Luke Dashjr](https://luke.dashjr.org/programs/Bitcoin/files/charts/software.html) (známý vývojář v ekosystému) je rozložení implementací mezi veřejnými uzly sítě následující:




- Bitcoin core**: 87.3 % uzlů
- Bitcoin Knots**: 12.5
- Další kumulativní implementace**: 0.(btcsuite, Bcoin, BTCD...)



![Image](assets/fr/056.webp)



Jinými slovy, přibližně 9 z 10 veřejných uzlů používá Bitcoin core. Zbytek sítě se spoléhá na okrajovější klienty (i když podíl uzlů v posledních měsících prudce vzrostl, v neposlední řadě v důsledku debat o limitu velikosti OP_RETURN). Tyto alternativní implementace často spravuje jedna osoba nebo malý tým.



**Poznámka:** Tyto údaje jsou však stále odhady, protože jsou založeny především na *poslouchajících uzlech*, tj. uzlech přijímajících příchozí spojení (s otevřeným portem 8333). U neposlouchajících uzlů* je počítání mnohem složitější, protože se k nim nelze připojit přímo: musíte čekat, až od nich přijde iniciativa v podobě odchozího spojení. Stránky Luka Dashjra tvrdí, že se snaží počítat i tyto *neposlouchající uzly*, ale získat o nich naprosto přesné údaje je nadále nemožné a aktualizace těchto statistik nevyhnutelně zaostává za skutečností.



### Vnitřní provoz Bitcoin core



Bitcoin core je napsán v jazyce C++. Je to také projekt s otevřeným zdrojovým kódem, o který se stará komunita vývojářů, kteří pracují jako dobrovolníci nebo jsou placeni různými subjekty (často společnostmi v ekosystému, které mají na vývoji jádra zájem). [Kód je umístěn na serveru GitHub](https://github.com/Bitcoin/Bitcoin) a vývoj probíhá podle přísného:




- Přispěvatelé** předkládají návrhy ve formě _žádostí o stažení_ (PR). V zásadě může změnu navrhnout kdokoli, ale musí být otestována, zdokumentována a projít procesem vzájemného hodnocení.
- Správci** mají právo schvalovat a slučovat PR. Jsou to oni, kdo zaručují soudržnost a stabilitu projektu. V červenci 2025 je jich pět: Hennadii Stepanov, Michael Ford, Andrew Chow, Gloria Zhao a Ryan Ofsky.
- Od února 2023 není žádný **hlavní správce**. Tuto roli původně zastával Satoshi Nakamoto při spuštění Bitcoin, poté Gavin Andresen po Nakamotově odchodu na začátku roku 2011 a nakonec Wladimir J. Van Der Laan od roku 2014 do roku 2023.



![Image](assets/fr/057.webp)



Vývoj Bitcoin core se řídí meritokratickou logikou: noví přispěvatelé jsou vybízeni k tomu, aby si kód prohlédli a otestovali, než sami navrhnou nějaké změny. Rozhodnutí jsou založena na technickém konsensu a zásadní změny (zejména v oblastech, kde panuje shoda) vyžadují diskusi na veřejných kanálech, jako jsou poštovní konference nebo PR review kluby.



### Další implementace Bitcoin



Ačkoli je jejich přijetí okrajové, existují i další klienti. Hlavním z nich je Bitcoin Knots, vyvinutý Lukášem Dashjrem, Fork Bitcoin core, který obsahuje další možnosti a konzervativnější přístup k vývoji. Patří mezi ně přísnější omezení formátů transakcí.



![Image](assets/fr/058.webp)



Můžeme také zmínit:




- Libbitcoin**: modulární knihovna C++, kterou vyvinul Amir Taaki a udržuje Eric Voskuil;
- Bcoin**: implementace v jazyce JavaScript, která již není aktivně udržována;
- BTCD/btcsuit**e: implementace v jazyce Go.



Tyto projekty přispívají k rozmanitosti ekosystému, ale jejich přijetí je stále velmi omezené, což ztěžuje samostatný vývoj Bitcoin core.



### Síla vývojářů Core



Mohlo by se zdát, že vývojáři Bitcoin core mají přímou kontrolu nad Bitcoin, ale není tomu tak. Nemohou vnutit změnu protokolu. Jejich úlohou je navrhovat kód. Je na každém uživateli, aby se prostřednictvím svého uzlu rozhodl, zda tento kód použije, nebo ne.



To znamená, že pokud změna v Bitcoin core nevyhovuje konsensu, mohou ji uzly ignorovat, a to buď tím, že nebudou Bitcoin core aktualizovat, nebo jednoduše změní implementaci. Naopak, pokud je funkce požadovaná uživateli zablokována v procesu vývoje jádra, je vždy možné přejít na jinou implementaci nebo Fork projekt.



Jak si řekneme později v tomto kurzu, jsou to uzly, které podle své ekonomické váhy (tj. obchodníci) udělují verzi protokolu (a tedy i příslušné měně) užitek tím, že přijímají jednotky, které respektují jeho pravidla. Skutečnou moc nad řízením Bitcoin tedy mají tito obchodníci, nikoli vývojáři.




# Staňte se suverénním bitcoinerem


<partId>df64cad2-e92d-4949-9cca-14394aad0bc6</partId>




## Proč si zamotávat vlastní uzel?


<chapterId>39c0cd19-67f9-4c64-bfb3-dbd6eec0bf42</chapterId>



Všeobecně panuje přesvědčení, že provozování uzlu Bitcoin je čistě altruistický čin bez osobního prospěchu, výhradně ve službách decentralizace sítě. Někteří to považují za formu povinnosti bitcoinářů podporovat systém a projevit Bitcoin svou vděčnost.



Jak jsme zdůraznili v předchozích kapitolách, spřádání uzlu nepřináší žádný přímý finanční zisk. Mohlo by se tedy zdát, že na tom není žádný osobní zájem. Přesto provozování vlastního uzlu přináší mnoho individuálních výhod. Abych vás o tom přesvědčil, uvedu v této kapitole všechny důvody, jak technické, tak strategické, proč byste si měli nainstalovat a používat vlastní uzel Bitcoin.



### Důvěrnější šíření transakcí



Když se software Wallet připojí k externímu uzlu, přenáší své transakce do infrastruktury, která není pod vaší kontrolou. To s sebou nese zjevná rizika sledování: provozovatel vzdáleného uzlu může analyzovat podrobnosti vašich transakcí, včetně částek a četnosti, a na základě křížové kontroly určitých metadat (jako jsou IP adresy, časy a místa) je potenciálně spojit s vaší identitou.



Jak bylo uvedeno v předchozí kapitole, peněženky se sítí Bitcoin nekomunikují zázrakem; aby mohly konzultovat zůstatky nebo vysílat transakce, musí se připojit k uzlu. Pokud jste si nikdy nezřídili vlastní uzel, znamená to, že váš Wallet závisí na infrastruktuře třetí strany (obvykle společnosti, která stojí za softwarem). Tato třetí strana, zejména pokud se jedná o společnost, může tyto údaje sledovat, využívat nebo dokonce zveřejňovat: ať už z komerčních důvodů, pod zákonným omezením nebo v důsledku pirátství.



![Image](assets/fr/059.webp)



Pomocí vlastního uzlu vysíláte své transakce přímo do sítě, čímž obcházíte prostředníky. Za předpokladu, že svůj uzel řádně zabezpečíte (o čemž si povíme později) nebo dodržíte určité standardy, nedochází k odhalení žádných informací: vaše IP adresa Address ani podrobnosti o vašich transakcích neprochází přes subjekt, který nemáte pod kontrolou. To je základní předpoklad pro zachování vaší důvěrnosti na Bitcoin.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Transakce, které nepodléhají cenzuře



Ze stejných důvodů, které byly uvedeny výše, je software Wallet založený na uzlu třetí strany zranitelný vůči riziku cenzury: provozovatel vzdáleného uzlu může z různých důvodů odmítnout předat určité transakce. Může je považovat za podezřelé nebo v rozporu se svou politikou. Transakce může být také zablokována, pokud není v souladu s pravidly pro předávání uzlu. V neposlední řadě se může operátor speciálně zaměřit na vaši IP adresu Address a zablokovat vysílání vašich transakcí.



Naopak použitím vlastního uzlu zajistíte šíření svých transakcí v rámci sítě peer-to-peer. To znamená, že si zachováte plnou kontrolu nad šířením svých transakcí bez závislosti na zprostředkovateli. Pokud transakce vyhovuje pravidlům konsensu a přenosu v uzlech připojených k vašemu uzlu, bude v síti vysílána a poté, za předpokladu, že obsahuje dostatečné poplatky, začleněna do bloku pomocí Miner. Mít vlastní uzel zaručuje neutrální potvrzování transakcí bez oprávnění.



### Nezávislé ověřování údajů



Bez osobního uzlu zůstáváte závislí na třetí straně, pokud jde o přístup k informacím, jako je zůstatek na účtu Address, stav potvrzení transakce a platnost bloku. To znamená implicitní důvěru v přesnost a integritu externího uzlu.



![Image](assets/fr/060.webp)



Spuštění Full node znamená, že můžete sami zkontrolovat všechna pravidla protokolu pro každou transakci a každý blok. Výsledkem je, že zůstatek zobrazený vaším Wallet nejsou data přijatá ze vzdáleného serveru, ale výsledek vypočtený lokálně z kompletní kopie Blockchain, ověřený blok po bloku. Tento přístup dává plný smysl výroku bitcoinářů:



> Nedůvěřujte, ale ověřujte.

### Lepší distribuce zabezpečení systému



Každý uzel, který se připojí k síti, posiluje redundanci a odolnost Bitcoin. Usnadňuje šíření informací a umožňuje vzájemné propojení nových partnerů. Bez uzlů by byl systém jednoduše nefunkční.



Jak jsme viděli, bezpečnost systému Bitcoin není založena na decentralizaci, Mining nebo kryptografii: jako každý systém se spoléhá na jednotlivce. Přesněji řečeno, závisí na schopnosti provozovatelů uzlů odolat nátlaku.



Decentralizované systémy, jako je Bitcoin, se vyznačují rozdělením rizika mezi všechny subjekty zapojené do jejich provozu. Provozovat vlastní uzel Bitcoin znamená přijmout část tohoto rizika zajištěním bezpečnosti své instance; tím také snižujete břemeno rizika pro ostatní provozovatele uzlů.



Nejedná se tedy o přímý osobní přínos: provozováním uzlu jste částečně zodpovědní za bezpečnost sítě. Je to především kolektivní výhoda, protože vaše zapojení pomáhá rozložit riziko. Na oplátku zvyšujete svou vlastní schopnost spolehlivě používat Bitcoin.



### Prohloubení znalostí o systému



Instalace zařízení Full node není triviální. Zahrnuje instalaci softwaru, pochopení základní obsluhy, sledování synchronizace, zkoumání protokolů v případě problémů a dokonce i používání terminálu. To vás nutně povede k prohloubení znalostí protokolu. To je sice nepřímá, ale nezanedbatelná výhoda.



Získání těchto znalostí posílí vaši důvěru v nástroj a může snížit riziko chyby nebo vystavení podvodům. Spřádání vlastního uzlu je také formou učení.



### Výběr pravidel, která se použijí



Důležitým aspektem, který je často špatně chápán, je to, že provoz uzlu umožňuje zvolit pravidla, která se použijí na místě. Existují dva hlavní typy pravidel:





- Pravidla konsensu**:



Jedná se o základní pravidla protokolu Bitcoin, která zajišťují integritu systému a stanovují kritéria pro ověřování transakcí a bloků. Transakce, která není v souladu s těmito pravidly konsensu, nemůže být nikdy zařazena do platného bloku. Například transakce s neplatným podpisem na jedné ze svých položek bude systematicky vyloučena.



Změna těchto pravidel se rovná změně protokolu, a tedy i měny (Hard Fork). Avšak i bez snahy o jejich změnu propůjčuje prostý fakt striktního uplatňování stávajících pravidel určitou moc: pokud blok pravidla porušuje, uzel jej okamžitě odmítne.





- Pravidla štafety**:



Jedná se o pravidla specifická pro každý uzel Bitcoin, která jsou přidána k pravidlům konsensu, aby definovala strukturu nepotvrzených transakcí přijatých v Mempool a předaných rovnocenným uzlům. Každý uzel konfiguruje a uplatňuje tato pravidla lokálně, což vysvětluje, proč se mohou v jednotlivých uzlech lišit. Vztahují se pouze na nepotvrzené transakce: transakce, kterou uzel považuje za "nestandardní", bude přijata pouze v případě, že se již objevila v platném bloku. Změna těchto pravidel neznamená vyloučení uzlu ze systému Bitcoin.



Například transakce bez poplatků je podle pravidel konsensu naprosto platná, ale podle zásad přenosu Bitcoin core bude standardně odmítnuta, protože parametr `minRelayTxFee` je nastaven na `0,00001` (v BTC/kB). Na vlastním uzlu je však možné tuto hranici snížit, aby bylo možné reléovat transakce s nižšími poplatky, nebo naopak zvýšit limit například na 2 Sats/vB, aby nebylo možné reléovat transakce s nízkými poplatky.



Spřádání vlastního uzlu znamená tvrzení: "Potvrzuji to, co jsem se rozhodl potvrdit, podle pravidel, která jsem sám přijal "*. Stáváte se tak aktérem řízení systému, který může odmítnout vývoj, který se vám zdá nepřijatelný, nebo schválit aktualizaci podle vlastních kritérií.



Můžeme se tedy rychle pokusit pochopit, jak velkou moc máte nad pravidly díky svému uzlu. A rozsah této moci bude záviset na typu pravidla.



#### Pravidla pro štafety



Co se týče pravidel předávání, podstatné je prosté vlastnictví uzlu bez ohledu na jeho ekonomickou aktivitu. Jde o to, zda souhlasíte s předáváním určitých typů transakcí.



Pokud se například domníváte, že transakce s poplatky nižšími než 1 sat/vB by měly být přijímány na Bitcoin, můžete toto pravidlo ve svém uzlu upravit tak, aby tyto transakce vysílal, a tím usnadnil jejich šíření po síti, dokud je Miner nakonec nezařadí do platného bloku. V podstatě se tedy jedná o moc nad šířením transakcí: každý uzel má rozhodovací pravomoc, protože souhlas s předáváním určitého typu transakce se rovná podpoře jejího přijetí v síti Bitcoin. Výsledkem je, že pokud provozujete několik uzlů, máte větší vliv na politiku předávání, protože každý uzel má vlastní spojení a oblasti vlivu na síť.



Mít jeden nebo více uzlů nakonfigurovaných se specifickými pravidly pro přenos znamená určit, která část sítě akceptuje šíření daného typu transakce. Šíření zprávy v grafu peer-to-peer, jako je tomu v případě transakcí Bitcoin, se řídí logikou teorie perkolace. Představte si každý uzel jako místo, které může být aktivní (`p` = přenáší) nebo neaktivní (`1-p`). Jakmile podíl `p` překročí kritickou hranici (`p_c`), vznikne obří komponenta: transakci se podaří projít sítí a má všechny šance dosáhnout Miner. V síti jako Bitcoin, kde každý uzel udržuje v průměru 8 odchozích spojení, je práh `p_c` obvykle nastaven na pouhých několik procent, dokonce i na nižší hodnotu, pokud mají některé uzly velmi velký počet spojení.



![Image](assets/fr/061.webp)



Dokud `p` zůstává pod `p_c`, transakce zůstává omezena na izolované kapsy a nedosáhne hodnoty Miner. Jakmile je tato hranice překročena, rozšíří se téměř okamžitě po celé síti.



O zařazení či nezařazení transakce do bloku nakonec vždy rozhodují těžaři. Uzly však zasahují na vyšší úrovni tím, že ovlivňují distribuci transakcí: určují, zda se těžaři o dané transakci dozvědí, či nikoli. Pokud transakce není těžařům předána, je zřejmé, že ji nemohou do bloku zařadit.



Přidání několika dalších uzlů bude mít proto pouze okrajový dopad, pokud je síť pro daný typ transakce již ve fázi perkolace, ale může se ukázat jako rozhodující, jakmile se přiblíží práh perkolace. Vlastnictví nebo ovlivňování několika uzlů, zejména pokud jsou dobře propojeny, může zvýšit nebo snížit hodnotu `p` a následně nepřímo řídit pravidla relay, která určují, které transakce budou viděny a nakonec přijaty těžaři.



#### Pro pravidla konsensu



Pokud jde o vliv vašeho uzlu na pravidla konsensu, rozhodující je především jeho ekonomická váha. To je zásadní koncept: hodnota jakékoli měny přímo souvisí s její schopností usnadnit Exchange. Pokud totiž nějaký objekt není v Exchange nikým akceptován za zboží nebo služby, nemá teoreticky žádnou peněžní užitečnost. Pokud například žádný obchodník nepřijímá oblázky jako platební prostředek, nemají jako peníze žádný užitek. Užitek samozřejmě zůstává subjektivním pojmem v individuálním měřítku, ale na daném území platí, že čím větší je počet obchodníků, kteří akceptují nějaký předmět jako prostředek Exchange, tím je pravděpodobnější, že tento předmět má pro lidi žijící na tomto území peněžní užitek.



Vezměme si příklad vesnice, kde mnoho obchodníků přijímá zlato v Exchange za zboží: je pravděpodobné, že zlato má pro vesničany peněžní užitek. To naznačuje, že užitečnost měny přímo závisí na rozhodnutí obchodníků, zda ji přijmou, nebo odmítnou.



Tento koncept je klíčový pro pochopení dynamiky moci v systému Bitcoin. Satoshi to říká jasně: Bitcoin je elektronický peněžní systém; jinými slovy, poskytuje službu, která nabízí určitou formu měny, Bitcoin (nebo BTC). Pokud jsou pravidla protokolu upravena způsobem, který není zpětně kompatibilní (Hard Fork), rovná se to vytvoření nového systému, a tedy i nové měny. Úspěch či neúspěch tohoto Fork pak závisí na velikosti jeho ekonomiky, která je zase určena počtem obchodníků, kteří tuto novou formu měny přijímají.



![Image](assets/fr/062.webp)



Vezměme si příklad: předpokládejme, že Bitcoin utrpí Hard Fork. Pak by existovaly 2 různé formy měny: BTC-1 (původní, nezměněná verze) a BTC-2 (nová měna s jinými pravidly konsensu). Pokud by všichni obchodníci, kteří přijímali BTC-1, v tom pokračovali, ale odmítali by BTC-2, pak by tato druhá měna měla teoreticky velmi omezenou peněžní užitečnost. Jako uživatel bych neměl zájem si BTC-2 ponechat a používat ho, protože bych věděl, že ho žádný obchodník v Exchange nebude chtít za zboží nebo služby. A naopak, pokud se 50 % obchodníků rozhodne přijímat výhradně BTC-2 a zbývajících 50 % bude přijímat pouze BTC-1, pak se užitek BTC-1 teoreticky sníží na polovinu. Používám výraz "teoreticky", protože užitečnost zůstává na individuální úrovni subjektivní a závisí na mnoha faktorech (jako je území a spotřební zvyklosti), které je obtížné pochopit případ od případu.



V případě Bitcoin role "obchodníka", kterým se rozumí jakýkoli subjekt s určitou ekonomickou vahou, samozřejmě zahrnuje podniky (fyzické obchody, internetové prodejní stránky, poskytovatele služeb atd.), ale také platformy Exchange, protože přijímají Bitcoin v Exchange za jiné měny, a těžaře, protože přijímají Bitcoin prostřednictvím poplatků v Exchange za službu zařazení transakce do bloku.



Co se týče pravidel konsensu, váš uzel vám umožňuje zaměřit svou ekonomickou aktivitu na jednu nebo druhou měnu. Například pokud máte doma 10 plných uzlů, ale žádnou významnou ekonomickou aktivitu, bude váš vliv během Fork téměř nulový. Naopak jediný uzel používaný ke správě řetězce 200 obchodů přijímajících Bitcoin propůjčuje významnou ekonomickou váhu.



Nezáleží tedy na počtu uzlů, ale na významu hospodářské činnosti, kterou podporují. A co víc, pokud vaše ekonomická aktivita závisí na uzlu, který neovládáte, jeho vlastník bude rozhodovat o tom, jakou měnu budete používat, dokud budete k tomuto uzlu připojeni. Proto je provozování a používání vlastního uzlu v kontextu správy systému obzvláště důležité:



> Ne váš uzel, ne vaše pravidla.


## Různé typy uzlů Bitcoin


<chapterId>be8f0baa-41f2-4b54-b011-092f4ccc93aa</chapterId>



Uzel Bitcoin je tedy počítač s implementací protokolu Bitcoin. Za touto společnou definicí uzlů se skrývá několik možných konfigurací, z nichž ne všechny nabízejí stejnou úroveň autonomie, spotřeby zdrojů a užitečnosti pro síť. V této kapitole se pokusíme tyto rozdíly pochopit, abychom vám pomohli vybrat architekturu uzlu, která vyhovuje vašemu použití a hardwarovým omezením.



### Kompletní uzel



Uzel Full node je jednoduše uzel Bitcoin, který stahuje celý blok Blockchain z bloku Genesis, ověřuje každý blok samostatně a lokálně ukládá historii všech těchto bloků Blockchain. To je "normální" podoba uzlu Bitcoin, jak si ji představuje Satoshi Nakamoto.



![Image](assets/fr/063.webp)



Systém Full node nemusí nikomu důvěřovat, protože ověřuje a zná všechny informace v systému. Je to typ uzlu, který vám dává největší záruky: bez spoléhání na třetí stranu víte, zda je platba platná, zda je blok platný, zda je reorganizace legitimní atd.



V praxi vyžaduje Full node netriviální zdroje, včetně několika stovek gigabajtů pro blokové soubory, procesoru schopného validovat skripty, paměti RAM pro Mempool a mezipaměti a stabilní šířky pásma. První synchronizace (*IBD*) načte a ověří kompletní historii: je náročná, ale probíhá pouze jednou. Full node se aktivně účastní sítě, předává bloky a transakce a může přijímat příchozí spojení, aby pomohl ostatním kolegům.



V závislosti na svých potřebách můžete do systému Full node přidat indexátor. Bitcoin core nabízí indexování transakcí jako volitelnou funkci (ve výchozím nastavení je deaktivováno), která může být užitečná pro specifické účely. Neobsahuje však indexátor Address, který je pro jednotlivé uživatele často nejvyhledávanější funkcí. Chcete-li to napravit, můžete si do uzlu nainstalovat specializovaný software, například Electrs nebo Fulcrum, který urychlí dotazy na ověření zůstatku Address z přidružených UTXO. K úloze indexeru se podrobněji vrátíme v samostatné kapitole.



### Uzel pruned



Uzel pruned ověřuje vše jako Full node, od bloku Genesis až po hlavu řetězce s největším množstvím práce, ale **uchovává pouze nejnovější část blokových souborů**. Jakmile jsou staré bloky zkontrolovány, postupně je maže, aby se nedostaly pod vámi nastavený limit místa. Tato konfigurace je ideální, pokud máte omezené místo na disku: zachováte si nezávislost ověřování bloků, aniž byste museli ukládat kompletní archiv historie Blockchain. Tato možnost je obzvláště užitečná, pokud chcete jednoduše nainstalovat Bitcoin core na svůj osobní počítač, aniž byste museli používat vyhrazený počítač.



![Image](assets/fr/064.webp)



Technické důsledky této možnosti jsou poměrně přímočaré: uzel pruned je dokonale schopen vysílat vaše transakce, podílet se na relay, ověřovat bloky a transakce a sledovat řetězec. Na druhou stranu nemůže sloužit jako zdroj historických dat nad rámec svých možností pro jiné aplikace (např. úplné průzkumníky, indexátory, peněženky). Funkce vyžadující archiv (nebo globální index) proto nebudou k dispozici.



Z praktického hlediska můžete uzel pruned použít k připojení softwaru pro správu Wallet, například Sparrow wallet. Nebudete však moci skenovat transakce na Wallet, které byly provedeny před limitem prořezávání. Například pokud máte transakci registrovanou v bloku 901 458, ale váš uzel uchovává pouze bloky od 905 402 výše (protože nejstarší byly pruned), nebudete moci tuto transakci skenovat. Na druhou stranu, pokud jste ji skenovali již v době, kdy váš uzel měl ještě tuto výšku bloku, pak váš software pro správu Wallet tuto informaci uloží a správně zobrazí zůstatek příslušných UTXO.



Stručně řečeno, sledování Wallet funguje v uzlu pruned bez problémů, pokud vytvoříte nový uzel Wallet, zatímco je váš software k tomuto uzlu již připojen. Na druhou stranu se můžete setkat s potížemi, pokud obnovíte starý Wallet, protože minulé transakce, které již uzel neuchovává, zřejmě nebude možné obnovit.



### Lehký uzel / SPV



Uzel SPV (*Simplified Payment Verification*) neboli odlehčený uzel uchovává pouze hlavičky bloků, nikoli podrobnosti o transakcích, a při získávání důkazů o tom, že transakce je v bloku (Merkleho důkazy prostřednictvím stromů), pro který má hlavičku, spoléhá na ostatní plné uzly. Koncept zjednodušeného ověřování plateb není nový, navrhl jej sám Satoshi Nakamoto v 8. části Bílé knihy.



![Image](assets/fr/066.webp)



Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. https://Bitcoin.org/Bitcoin.pdf



Tento typ uzlu je samozřejmě mnohem méně náročný na úložiště a využití procesoru než uzel Full node nebo dokonce pruned. Uzel SPV je proto vhodný pro menší zařízení a přerušovaná připojení. Ve skutečnosti je často integrován přímo do Wallet, zejména do mobilního softwaru, jako je aplikace Blockstream.



Kompromisem je důvěryhodnost a důvěrnost: klient SPV sám nekontroluje skripty ani zásady ověřování; předpokládá, že řetězec s největším počtem prací je platný, a závisí na odpovědích jednoho nebo více plných uzlů. Použití tohoto typu uzlu je proto lepší možností než připojení k uzlu třetí strany; je však stále méně výhodné než mít uzel Full node nebo dokonce pruned.



![Image](assets/fr/065.webp)



### Který uzel pro kterou potřebu?





- Mobilní uživatel / začátečník



Pro začínajícího uživatele s pouhým Wallet v mobilní aplikaci je použití uzlu SPV jistě nejlepší způsob, jak začít. Instalace je rychlá, nevyžaduje mnoho prostředků a ovládání je jednoduché a plynulé. To znamená, že si můžete sami ověřit určité informace, a proto se méně spoléhat na uzly třetích stran a zároveň být nezávislejší, pokud jde o vysílání transakcí.





- PC / středně pokročilý uživatel



Středně pokročilý uživatel s počítačem může nainstalovat uzel pruned a využívat téměř všechny výhody uzlu Full node, aniž by denně přetěžoval svůj počítač: plná validace, mírné využití disku a jednoduchá údržba. Je to ideální řešení pro připojení peněženek na stolním počítači a zachování nezávislosti při distribuci transakcí, aniž byste museli investovat do vyhrazeného stroje nebo přetěžovat diskový prostor.





- Suverénní Bitcoiner / pokročilý



Full node zůstává nejlepším řešením, pokud chcete být při používání Bitcoin zcela nezávislí a neomezovat se později na pokročilé použití, jako je indexer, uzel Lightning nebo dokonce Block explorer. Přesně to budeme v tomto kurzu zkoumat!



## Přehled softwarových řešení


<chapterId>0d48b89a-e8b5-441e-a707-537a035fc15e</chapterId>



Na straně softwaru existují dva hlavní způsoby, jak provozovat uzel Bitcoin:




- přímo nainstalovat implementaci protokolu, například Bitcoin core (doporučeno) nebo Bitcoin Knots,
- nebo použít distribuci na klíč (často nazývanou "_node-in-a-box_"), která stejným způsobem integruje implementaci Bitcoin, ale obsahuje také systém správy Interface, úložiště aplikací a nástroje připravené k použití (Lightning, prohlížeče, indexové servery, dokonce i aplikace pro vlastní hostování mimo Bitcoin...).



Oba přístupy vedou ke stejnému cíli: mít vlastní uzel, ale liší se z hlediska instalace a používání Interface, údržby, rozšiřitelnosti a nákladů. Právě to budeme zkoumat v této kapitole.



### Surové implementace uzlů Bitcoin



Instalace surové implementace znamená přímé použití softwaru implementace protokolu Bitcoin (například Core) bez jakéhokoli dalšího softwaru Layer. Konfiguraci, aktualizace a související služby (indexování, API, Lightning, zálohování atd.) si spravujete sami podle svých potřeb.



Jedná se o nejsugestivnější a nejpružnější přístup: přesně víte, co běží, kde jsou data a jak vše funguje. Na druhou stranu se stává složitějším, jakmile chcete překročit rámec jednoduchého provozu uzlu Bitcoin. Pokud je vaším cílem mít pouze uzel, je složitost srovnatelná s uzlem v krabici, nebo dokonce menší, protože jde pouze o instalaci softwaru.



#### Bitcoin core (zákazník s nadpoloviční většinou)



[Bitcoin core je klientem sítě s ultravětšinovým podílem](https://bitcoincore.org/). Stahuje, ověřuje a udržuje Blockchain, poskytuje rozhraní API RPC/REST a může integrovat Wallet. Pokud dáváte přednost standardním nástrojům a cítíte se pohodlně, když si sami přidáváte služby (například server Electrum, průzkumník a LND), je lepší používat jádro tak, jak je.



**Výhody:** Maximální stabilita, předvídatelné chování, hrubé zkušenosti, snadná instalace a konfigurace.



**Nevýhody:** Pro vytvoření kompletního aplikačního prostředí je nutné ručně sestavit zbytek zásobníku, nikoli pouze uzel Bitcoin.



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

#### Bitcoin Knots (hlavní alternativní zákazník)



[Bitcoin Knots je Fork z Bitcoin core](https://bitcoinknots.org/), kterou spravuje Luke Dashjr. Je to hlavní alternativní klient k jádru pro implementaci protokolu Bitcoin. Je plně kompatibilní se zbytkem sítě (v žádném případě se nejedná o Hard Fork jako Bitcoin Cash), nicméně nabízí další funkce, včetně možností relay policy, které v Core chybí nebo jsou ve výchozím nastavení aplikovány přísněji, aby se omezilo to, co někteří považují za spam.



Existují 2 možné důvody, proč se rozhodnout pro uzly místo jádra:




- Techniky**: V porovnání s jádrem se liší zejména v oblasti správy relé tím, že určuje, které transakce uzel přijímá a vysílá.
- Zásady**: Někteří lidé dávají přednost používání alternativních klientů, jako je Knots, z netechnických důvodů, zejména proto, aby podpořili alternativu k jádru a omezili tak jeho monopol. Pokud by někdy došlo k ohrožení jádra, bylo by užitečné mít nejen solidní a dobře udržované alternativní klienty, ale také vědět, jak je efektivně využívat. Jiní používají Knots z protestních důvodů, protože ztratili důvěru ve vývojáře Core nebo nesouhlasí s většinou vedení klienta.


https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Osobně doporučuji zvolit jádro, a to hlavně proto, abyste mohli rychleji využívat bezpečnostní záplaty. Některé zranitelnosti objevené v Knots jsou totiž opravovány se zpožděním. Obecněji řečeno, proces vývoje Core je pevně strukturovaný a podporovaný velkým počtem přispěvatelů, zatímco Knots je udržován jedinou osobou a má mnohem menší komunitu. Na druhou stranu pravidla relay mají dnes tendenci ztrácet svou užitečnost, zejména pokud je aplikuje jen malá část sítě (jako perkolační teorie).



### Distribuce uzlu v krabici



Uzel v krabici_ kombinuje Bitcoin core (nebo Knots) s předkonfigurovaným operačním systémem, webem Interface a obchodem s aplikacemi pro samoobslužné služby (Lightning, explorers, server Electrum, Mempool, BTCPay Server, Nextcloud atd.). Jedním kliknutím můžete tyto různé moduly nainstalovat, aktualizovat a propojit.



Je to mnohem jednodušší řešení pro každodenní spouštění a správu mnoha pomocných aplikací. Nevýhodou je, že když se vyskytne problém (např. konflikt obrazů Docker, chybná aktualizace, poškozená databáze), může být ladění velmi složité, protože jste závislí na vlastní integraci distribuce. Navíc komunitní nebo oficiální podpora je často komplikovaná.



Uzel v krabici se tedy používá velmi snadno, pokud vše funguje správně, ale v případě chyby musíte být připraveni na zdlouhavé hledání, čekání na pomoc a špinavé ruce.



Většina těchto řešení je k dispozici ve dvou formátech:




- Předmontovaný počítač: kompletní počítač s již nainstalovaným operačním systémem. Tyto placené počítače stačí zapojit do elektrické sítě a připojit k internetu, aby byly funkční. Pokud to váš rozpočet umožňuje, je výhodou této možnosti velmi jednoduché nastavení, často přednostní podpora a příspěvek k financování vývoje, protože obchodní model těchto společností je zpravidla založen na prodeji hardwaru.
- Udělej si sám: nainstalujte si distribuční operační systém na svůj vlastní počítač (starý počítač, NUC, Raspberry Pi, domácí server...). Jedná se o nejekonomičtější řešení, protože můžete recyklovat starý stroj nebo si vybrat hardware, který přesně odpovídá vašim potřebám a rozpočtu. Je to také nejflexibilnější možnost, jejíž konfigurace je nejuspokojivější. Právě tomuto přístupu se budeme věnovat v praktické části kurzu.



Zde je přehled hlavních dostupných řešení typu node-in-a-box (v roce 2025):



### Umbrel (umbrelOS & Umbrel Home)



[Dnes je společnost Umbrel lídrem v oblasti řešení typu node-in-a-box (https://umbrel.com/). Za jeho úspěchem stojí především jednoduchá instalace (kdy byl spuštěn na jednoduchém počítači Raspberry Pi), elegantní a intuitivní Interface a ekosystém aplikací, který se rychle rozrostl a nyní je velmi rozsáhlý.



![Image](assets/fr/067.webp)



Umbrel, který byl v roce 2020 spuštěn jako jednoduchý uzel Bitcoin doplněný několika pomocnými aplikacemi, se postupně vyvinul v plnohodnotný moderní domácí cloud.



Nebudu zde podrobněji popisovat, jak funguje a jaké jsou jeho specifické vlastnosti, protože těmi se budeme podrobněji zabývat v první kapitole dalšího dílu. Pro účely tohoto kurzu BTC 202 jsem se totiž rozhodl používat systém UmbrelOS, který považuji za nejlepší současné řešení typu node-in-a-box pro začínající a středně pokročilé uživatele.



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

### Start9 (StartOS)



[Start9 nabízí StartOS (https://start9.com/), systém určený pro "suverénní výpočetní techniku": cílem je, aby každý mohl vlastnit a spravovat svůj soukromý server, rozšířený o tržiště samoobslužných aplikací. Server Start9 si můžete zakoupit (Server One za 619 dolarů, Server Pure za 899 dolarů) nebo si jej sestavit v režimu DIY na vlastním počítači.



Na straně Bitcoin umožňuje StartOS nainstalovat Full node, uzel Lightning, server BTCPay, Electrs a mnoho dalších služeb. Přitažlivost systému Start9 však sahá dále: nabízí možnost objevovat, konfigurovat a vystavovat různý software (souborový cloud, zasílání zpráv, monitorování) jednotným způsobem a s plnou kontrolou. Projekt je tedy určen uživatelům, kteří chtějí robustní samohostitelskou platformu, nikoliv jen jednoduchý uzel Bitcoin. Po Umbrelu je to pravděpodobně nejkomplexnější ekosystém.



![Image](assets/fr/068.webp)



Hlavní rozdíl oproti společnosti Umbrel spočívá v modelu Interface. Umbrel si zakládá na vysoce vybroušeném uživatelském rozhraní, zatímco Start9 nabízí hrubší a funkčnější Interface. Ekosystém aplikací Start9 je méně bohatý než ekosystém Umbrel, ale kompenzuje to několika technickými výhodami: přístup k pokročilým nastavením aplikací je zjednodušený, zatímco Umbrel se rychle stává omezujícím, pokud požadovanou možnost Interface neposkytuje. Start9 také vyniká ve správě zálohování: kromě efektivního řešení Umbrel pro LND neexistuje na rozdíl od Start9 žádný jednotný mechanismus. Navíc nabízí přístupnější monitorovací nástroje a šifrované vzdálené připojení (`https`), zatímco místní přístup k Umbrelu je přes `http`.



Stručně řečeno, pokud potřebujete pouze základní aplikace pro Bitcoin, nemáte zvláštní zájem o velmi bohatý ekosystém Umbrel a uživatel Interface není prioritou, pak je Start9 lepší volbou. V opačném případě je lepší volbou Umbrel.



https://planb.network/tutorials/node/bitcoin/start9-8c8b6827-8423-4929-bcba-89057670ed6a

### MyNode



[MyNode je distribuce zaměřená výhradně na Bitcoin a Lightning](https://mynodebtc.com/), která nabízí web Interface, tržiště aplikací a upgrady jedním kliknutím. Můžete si buď zakoupit hardware připravený k použití (*Model Two* je k dispozici za 549 USD), nebo si MyNode nainstalovat zdarma na vlastní počítač. Projekt nabízí také verzi softwaru *Premium* (94 USD), která zahrnuje přednostní podporu a pokročilé funkce.



![Image](assets/fr/069.webp)



V praxi MyNode sdružuje všechny základní stavební prvky potřebné k provozu Full node a také aplikace nezbytné pro uživatele Bitcoin. Proto je vhodným řešením, pokud nevyžadujete aplikace mimo ekosystém Bitcoin, jako jsou například samohostitelné aplikace, které se nacházejí v systémech Start9 a Umbrel.



https://planb.network/tutorials/node/bitcoin/mynode-a481fef3-2fd3-4df3-91c0-112cffa094eb

### RaspiBlitz



[RaspiBlitz je 100% open source projekt](https://docs.raspiblitz.org/) (licence MIT) pro montáž uzlu Bitcoin a uzlu Lightning na Raspberry Pi. Stačí stáhnout obraz, spustit systém a poté postupovat podle průvodce, abyste měli na Raspberry Pi funkční uzel v krabici. Předmontované sady jsou k dispozici také od třetích stran, obvykle se pohybují mezi 300 a 400 dolary v závislosti na hardwaru. RaspiBlitz také nabízí řadu dalších, snadno instalovatelných aplikací.



![Image](assets/fr/070.webp)



Pokud vlastníte Raspberry Pi, je to vynikající volba, protože kompletnější systémy jako Umbrel jsou pro tento typ mini PC stále těžší.



https://planb.network/tutorials/node/bitcoin/raspiblitz-d8cdba2e-a682-46cf-9fdc-d8602fbeac02

### RoninDojo



[RoninDojo je uzel v krabici zaměřený na ochranu soukromí](https://wiki.ronindojo.io/en/home), který automatizuje nasazení Samurai Dojo a Whirlpool, s vyhrazeným Interface a zásuvnými moduly speciálně navrženými pro ekosystém Samurai.



Princip je jednoduchý: pokud používáte Ashigaru Wallet (nástupce Fork Samurai Wallet po zatčení jeho vývojářů) nebo chcete využívat pokročilé nástroje pro ochranu soukromí, je RoninDojo určen právě vám.



![Image](assets/fr/071.webp)



Projekt dříve nabízel předkonfigurovaný stroj Tanto, který však v současné době není k dispozici. Je možné, že se vrátí později. Do té doby je možné RoninDojo snadno nainstalovat na Rock5B+ nebo Rockpro64, případně i nepřímo na Raspberry Pi.



https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

### Nodl



Dalším řešením [node-in-a-box je Nodl](https://www.nodl.eu/). Stejně jako u předchozích projektů si můžete zakoupit předkonfigurovaný hardware (v závislosti na modelu od 599 do 799 EUR) nebo si jej nainstalovat sami v režimu DIY.



Na straně softwaru Nodl integruje Bitcoin core, LND, BTCPay Server, Electrs, Dojo, Whirlpool, Lightning Terminal, RTL a také BTC RPC Explorer, vše s integrovaným aktualizačním řetězcem a open-source kódem pod licencí MIT.



![Image](assets/fr/072.webp)



Po prozkoumání různých softwarových řešení je nyní čas vybrat počítač, který bude hostitelem vašeho uzlu!




## Přehled hardwarových řešení


<chapterId>245d6add-9cda-46b9-9343-31dcdd70456e</chapterId>



Nyní, když jsme prozkoumali všechny softwarové možnosti, se zaměřme na hardware potřebný pro váš uzel. Poskytnu vám několik konkrétních rad pro výběr komponent spolu s konfiguracemi přizpůsobenými různým rozpočtům. Samozřejmě se jedná o můj osobní názor a zpětnou vazbu: kromě zde uvedených alternativ jistě existují i další relevantní možnosti. Navíc se nebudu vracet k předem sestaveným strojům, které nabízejí projekty node-in-a-box, jimiž jsme se již zabývali v předchozí kapitole. Zde se zaměříme výhradně na řešení typu "udělej si sám".



### Opravdu potřebujete speciální stroj?



V posledních několika letech si bitcoináři stále více uvědomují běžnou mylnou představu, zejména s popularizací uzlu v krabici na začátku roku 2020: uzel Bitcoin by měl nutně běžet na stroji určeném výhradně k tomuto účelu. To však není pravda. K provozu uzlu Bitcoin není nutně zapotřebí vyhrazený počítač: Bitcoin core lze dokonale spustit na běžném počítači. Pokud máte dostatek místa na disku pro Blockchain nebo povolíte prořezávání, můžete řetězec ověřit, připojit svůj Wallet, a dokonce program zavřít, až jej přestanete používat. Výhoda tohoto přístupu je značná: nulová počáteční investice a minimální složitost.



![Image](assets/fr/074.webp)



Přesto je použití vyhrazeného stroje často pohodlnější. Může běžet nepřetržitě (24 hodin denně, 7 dní v týdnu), je neustále vzdáleně přístupný, nemonopolizuje prostředky vašeho hlavního stroje a především izoluje použití (dobrá bezpečnostní praxe: pokud se váš osobní počítač dostane do problému, váš uzel funguje dál a naopak). Otázka tedy nezní "Potřebuji vyčlenit stroj?", ale spíše "Potřebuji uzel, který je neustále online, přístupný dalším zařízením a schopný se vyvíjet?" (Lightning, indexery, další aplikace...). Pokud je odpověď kladná, volba samostatného stroje vše výrazně zjednoduší.



### 3 způsoby pořízení: recyklace, použitá a nová technika



#### Recyklace starého počítače



Je to nejekonomičtější řešení. Většina z nás má doma nebo u přátel a rodiny starý počítač, který shromažďuje Dust: toto je ideální příležitost, jak ho znovu uvést do provozu! Chcete-li jej upravit pro použití jako uzel Bitcoin, jednoduše přidejte 2TB SSD a podle svých potřeb vyměňte nebo přidejte lišty RAM, abyste zvýšili paměť RAM. Počítejte s tím, že za plně funkční stroj zaplatíte 100 až 200 eur.



Před nákupem hardwaru zkontrolujte počet dostupných diskových slotů, typ připojení (M.2 nebo SATA), formát paměti RAM (SODIMM nebo DIMM) a její generaci (DDR4 atd.). Měli byste také využít příležitosti k vyčištění počítače, zejména ventilátoru, abyste zajistili optimální výkon.



Buďte však opatrní, pokud používáte notebook: baterie se může časem stát problémem (více o tom později v této kapitole).



#### Repasované nebo použité



Trh je plný repasovaných firemních mini počítačů, jako jsou *Lenovo ThinkCentre Tiny*, *HP EliteDesk Mini* nebo *Dell OptiPlex Micro*. Tyto stroje jsou pevné, kompaktní, tiché a energeticky úsporné. Jejich cena je hluboko pod cenou nových a snadno najdete modely vybavené procesory i5/i7 6. až 10. generace a 8 až 16 GB RAM, to vše za velmi atraktivní ceny, zpravidla mezi 70 a 200 EUR v závislosti na konfiguraci. Podle mého názoru je to pravděpodobně nejlepší volba, pokud hledáte specializovaný stroj pro uzel Bitcoin.



![Image](assets/fr/075.webp)



Je také možné najít několik let staré použité počítače a notebooky se zajímavými konfiguracemi a vynikajícím poměrem ceny a výkonu.



**Poznámka:** stroje z firemních flotil, jako je *ThinkCentre Tiny*, jsou často vybaveny pouze portem *DisplayPort* (DP) pro obrazovku bez výstupu HDMI. Nezapomeňte si proto vzít adaptér nebo kabel DP-HDMI, pokud jej potřebujete.



#### Nákup nového



Pokud vám to rozpočet dovolí, můžete se také rozhodnout pro nový stroj. To je dobrá volba, pokud chcete mít nejnovější hardware s dobrým výkonem, zejména pokud plánujete používat Umbrel nebo Start9 s dalšími aplikacemi mimo ekosystém Bitcoin pro vlastní hostování.



### Jaký typ stroje si mám vybrat?



#### Mini-PC "NUC" / barebone



Minipočítače podle mého názoru představují nejlepší kompromis pro domácí hostování uzlu Bitcoin. Šetří místo, snadno se vejdou na poličku, spotřebovávají minimum energie a lze je snadno hardwarově upravit, například přidat paměť RAM nebo vyměnit disk SSD.



Osobně dávám přednost modelu *Lenovo ThinkCentre Tiny*, který je na trhu s použitými počítači (z firemních flotil) velmi rozšířený; je obzvláště robustní a snadno se upravuje. Existuje samozřejmě mnoho ekvivalentů od jiných výrobců: **Dell OptiPlex Micro*, *HP ProDesk / EliteDesk Mini / Micro*, *Intel NUC*, *Gigabyte BRIX*, *MSI Cubi*..



![Image](assets/fr/001.webp)



**Významné vlastnosti:** malé rozměry, mírná spotřeba energie, nízká hlučnost, škálovatelnost (v závislosti na modelu) a spolehlivost.



**Slabé stránky:** o něco dražší než SBC typu Raspberry Pi, žádná vestavěná obrazovka (vzdálený přístup nebo přes externí monitor), žádná baterie (náhlé vypnutí v případě výpadku proudu).



#### Vyhrazený notebook



Jedná se o vynikající levnou alternativu k mini PC: dnes můžete najít použité nebo dokonce nové notebooky za nízké ceny, vybavené slušnými procesory, mnoha porty a také integrovanou obrazovkou a klávesnicí (velmi praktické pro počáteční instalaci). Především baterie funguje jako přirozená UPS: v případě výpadku proudu se uzel náhle nevypne a může zůstat v provozu i několik hodin.



![Image](assets/fr/076.webp)



**Zajímavé vlastnosti:** Řešení vše v jednom, baterie funguje jako UPS (žádné výpadky), zjednodušená instalace díky integrovanému displeji a klávesnici, integrovaná karta Wi-Fi a široký výběr na trhu s použitými i novými produkty (což často znamená, že můžete vyjednávat o cenách).



**Slabé stránky:** mírně vyšší spotřeba energie než u holého Mini-PC, postupné opotřebení baterie při nepřetržitém provozu se ztrátou kapacity, vzácné, ale reálné riziko nabobtnání baterie nebo tepelného vybití s věkem. Hlavně kvůli tomuto aspektu považuji mini-PC za lepší volbu než notebook: postupné opotřebení baterie a s tím spojená rizika.



Pokud se rozhodnete pro toto řešení, doporučuji pečlivě sledovat stav baterie, abyste předešli jakémukoli nebezpečí. Dávejte pozor na nadměrné teplo, neobvyklý zápach, nestabilitu nebo deformovaný plášť. V případě poplachu okamžitě vypněte a odpojte počítač od sítě a poté baterii zlikvidujte ve specializovaném recyklačním zařízení.



**Tip:** Pokud to systém BIOS/UEFI nebo nástroj výrobce umožňuje, nastavte limit zátěže (např. 60 % nebo 80 %), abyste prodloužili životnost baterie.



#### Raspberry Pi a další SBC: špatný nápad



Na počátku roku 2020 se s rozvojem softwaru node-in-a-box objevila také mánie kolem počítače Raspberry Pi jako prostředku pro provoz uzlu Bitcoin. Myšlenka se zdála být atraktivní: levná, kompaktní a dostupná.



![Image](assets/fr/073.webp)



Pokud je vaším cílem provozovat pouze uzel Bitcoin bez dalších aplikací, může v praxi stačit počítač Raspberry Pi. Jakmile ale budete chtít používat Umbrel, Start9 nebo bohatší ekosystém (Block explorer, Address indexer, Lightning node, selfhostingové aplikace...), stroj rychle dosáhne svých limitů.



Raspberry Pi má řadu nevýhod:




- příliš tenké procesory s architekturou ARM, které jsou někdy nekompatibilní s určitým softwarem nebo vyžadují větší manipulaci;
- Pájená paměť RAM, nemožnost upgradu, omezené konfigurace (často maximálně 8 GB);
- externí boxy pro SSD připojené kabelem, časté zdroje chyb, vyžadující nákup specifické karty pro stabilní SSD;
- tendence k rychlému zahřívání a potíže se zajištěním správného chlazení;
- je třeba zakoupit další hardware (skříň, ventilátor, kartu SSD atd.);
- velmi omezená konektivita.



Historicky byla velkou výhodou SBC, jako je Raspberry Pi, jejich cena: za několik desítek eur jste mohli získat specializovaný stroj. Dnes však ceny prudce vzrostly a po přidání veškerého nezbytného dodatečného hardwaru se cena blíží ceně prvních použitých nebo repasovaných mini PC x86, které podle mého názoru nabízejí mnohem více výhod. Z tohoto důvodu nedoporučuji volit SBC.



### Výběr komponent



#### Diskové úložiště: SSD povinně, minimálně 2 TB



Technicky je možné provozovat uzel Bitcoin na HDD. Problémem je, že se vše výrazně zpomalí, zejména IBD, který bude extrémně dlouhý kvůli tomu, že Bitcoin core intenzivně využívá disk jako mezipaměť (zejména u sady UTXO). Proto důrazně nedoporučuji používat HDD: vytváří skutečné úzké hrdlo, výrazně omezuje budoucí vývoj (např. pro uzel Lightning) a může vést i k nesouladu synchronizace s hlavou Blockchain. Navíc neustálé namáhání mechanického disku zvyšuje riziko jeho předčasného opotřebení.



Disky SSD radikálně mění uživatelskou zkušenost: vše je rychlejší a plynulejší a mnohem spolehlivější. Použití SSD je proto pro váš uzel (téměř) povinné a nebudete toho litovat, zejména proto, že vysokokapacitní modely jsou nyní relativně dostupné.



![Image](assets/fr/077.webp)



Co se týče kapacity, 2 TB se postupně stávají novým rozumným minimem. V létě 2025 se již kapacita Blockchain blíží 700 GB, a pokud přidáte Umbrel, indexer Address a několik aplikací, bude 1 TB SSD rychle nasycen. S 2 TB máte pohodlnou rezervu na další roky (v hrubém odhadu na 5 až 15 let). Můžete se také rozhodnout pro 4 TB, pokud plánujete používat mnoho aplikací na Umbrelu, ukládat velké soubory v samoobsluze nebo pokud chcete do značné míry předvídat své potřeby diskového prostoru.



![Image](assets/fr/078.webp)



Co se týče formátu, bude záležet na portech, které máte v počítači k dispozici; pokud je to však možné, doporučuji použít SSD disk M.2 s rozhraním NVMe.



#### Paměť (RAM): 8 až 16 GB



Pro samotnou aplikaci Bitcoin core (bez překryvné vrstvy Umbrel) je podle doporučení vývojářů potřeba minimálně 256 MB RAM s nejnižším nastavením, 512 MB s výchozím nastavením a 1 GB pro běžné použití.



Na druhou stranu, pokud používáte systém uzel v krabici, jako je Umbrel nebo Start9, jsou požadavky na paměť RAM výrazně vyšší. Vývojáři systému Umbrel doporučují minimálně 4 GB RAM. To sice může stačit na provoz pouze jádra, ale brzy budete omezeni. Proto doporučují 8 GB, což také považuji za minimum pro základní konfiguraci kolem Bitcoin (jádro, LND, indexer a několik aplikací). Podle mých zkušeností je s Umbrelem a několika dalšími službami 8 GB stále trochu málo. Chcete-li být opravdu pohodlní a mít nějakou rezervu, doporučil bych 16 GB RAM.



#### Procesor (CPU)



Minimálním požadavkem na uzel Umbrel je dvoujádrový 64bitový procesor Intel nebo AMD. Pokud chcete kromě Bitcoin core používat i několik dalších aplikací, čtyřjádro (nebo vyšší) bude mít z hlediska plynulosti skutečný význam. Například procesory i5/i7 6. až 10. generace jsou na trhu s použitými počítači vynikající volbou.



### Příklady konkrétních konfigurací



Níže navrhuji tři konkrétní konfigurace, přizpůsobené různým rozpočtům a potřebám, s přesnými modely, které je podporují. Tyto volby jsou uvedeny jako příklady pro ilustraci informací v této kapitole; nejste povinni zvolit přesně tyto modely. Protože považuji Mini-PC za dlouhodobě nejlepší volbu, budu u těchto tří navrhovaných konfigurací vycházet z tohoto formátu.



*Níže uvedené ceny jsou pouze orientační a mohou se lišit v závislosti na regionu, prodejci a období*



V první řadě potřebujete SSD disk, který je dostatečně velký na to, aby se na něj Blockchain vešel, a zároveň vám zůstane manévrovací prostor. Disky SSD mají omezenou životnost z hlediska cyklů zápisu a celkového objemu zapsaných dat. Uzel Bitcoin však disk při zápisu výrazně zatěžuje. Proto nedoporučuji základní modely; místo toho doporučuji SSD disk NVMe, který nabízí výrazně vyšší výkon.



Jako příklad jsem pro účely tohoto kurzu zvolil následující model: *2Tb*, který je na Amazonu k dostání za přibližně 120 EUR: Samsung 990 EVO Plus NVMe M.2 SSD 2Tb*. Můžete se rozhodnout i pro jiné známé značky, jako jsou Crucial, Western Digital nebo Kingston.



![Image](assets/fr/046.webp)



#### Nízkorozpočtová konfigurace



Pokud je váš rozpočet velmi omezený (pod 200 EUR), doporučuji vám neinvestovat do specializovaného stroje, ale raději nainstalovat Bitcoin core přímo na váš běžný počítač (v režimu pruned, pokud máte málo místa na disku).



V opačném případě doporučuji pro základní rozpočet *HP EliteDesk 800 G2 Mini*. Na Amazonu jsem našel repasovaný model za 96 eur, vybavený procesorem Intel Core i5 6. generace a 8 GB RAM. Jedná se o obzvláště zajímavou volbu pro začátečníky: tento procesor a toto množství paměti jsou více než dostatečné pro provoz jádra Umbrel i několika aplikací současně, například indexeru Electrs, uzlu Lightning a instance Mempool, pokud jádru nepřidělíte příliš mnoho mezipaměti. Navíc tento typ minipočítače umožňuje v případě potřeby snadno zvýšit paměť RAM například na 16 GB (počítejte s tím, že za jednu nebo dvě kvalitní paměťové karty si připlatíte asi 30-40 EUR).



![Image](assets/fr/045.webp)



Poté jednoduše přidejte SSD do rozpočtu. Začneme-li 2TB diskem Samsung za 120 eur, dostaneme se na celkovou cenu 216 eur za kompletní a funkční stroj.



#### Středněrozpočtová konfigurace



Pokud máte na počítač, který bude hostitelem vašeho uzlu, průměrný rozpočet kolem 300 eur, doporučuji například *Lenovo ThinkCentre Tiny*, vybavený výkonným procesorem a dostatečnou pamětí RAM. Na Amazonu jsem našel repasovaný model za 180 EUR, který je vybaven procesorem Intel Core i7 6. generace a 16 GB paměti RAM. Když se k tomu přidá 2TB SSD za 120 eur, celkové náklady se vyšplhají na 300 eur.



![Image](assets/fr/044.webp)



S tímto strojem máte k dispozici pohodlnou konfiguraci: rychlý IBD a možnost bez problémů spouštět řadu aplikací na Umbrelu nebo Start9. Přesně takovou konfiguraci používám pro tento kurz BTC 202.



#### Špičková konfigurace



S větším rozpočtem se možnosti výrazně rozšiřují. Můžete zvolit konfiguraci "udělej si sám", nebo se dokonce rozhodnout pro předem sestavený stroj, který nabízí přímo projekt node-in-a-box.



Například *ASUS NUC 14 Pro* je na Amazonu k dostání nový za 540 eur. Za tuto cenu získáte procesor Intel Core Ultra 5 (nejnovější a mimořádně výkonný) doplněný 16 GB paměti DDR5 RAM. S takovou konfigurací budete moci dokončit IBD v rekordním čase a bez problémů instalovat náročné aplikace.



Jedná se o velmi pohodlnou konfiguraci, která je dokonce nadbytečná, pokud je původním cílem pouhý provoz uzlu Bitcoin. Na druhou stranu, pokud chcete naplno využít všechny samoobslužné aplikace dostupné v systémech Umbrel a Start9, je pro vás tato úroveň výkonu jako stvořená.



![Image](assets/fr/043.webp)



V závislosti na zamýšleném použití se můžete rozhodnout buď pro 2TB SSD jako v ostatních konfiguracích, nebo přímo pro 4TB SSD za 260 eur, pokud chcete ukládat i osobní soubory a rozšířit své využití pro vlastní hosting. S 2TB SSD činí celkové náklady na konfiguraci 660 eur, zatímco se 4TB SSD dosahují 800 eur.



### Několik dalších tipů





- Pokud si chcete koupit použité vybavení a platit bitcoiny, přijďte na setkání ve vašem okolí! Při konverzaci s ostatními účastníky určitě najdete vhodné vybavení za dobrou cenu a zároveň pomůžete udržet oběhové hospodářství kolem Bitcoin při životě. Je to také příležitost, jak využít dobré rady komunity.





- Pro připojení k internetu budete samozřejmě potřebovat ethernetový kabel RJ45, alespoň pro instalaci systému.





- Některá prostředí, například Umbrel, pak umožňují používat Wi-Fi, ale výkon je obecně nižší (zejména pokud chcete uzel Lightning používat vzdáleně, což může mít vliv). Pokud se rozhodnete pro Wi-Fi, ujistěte se, že váš počítač má vestavěnou kartu, nebo přidejte kompatibilní klíč.





- Pro svůj stroj vždy používejte originální napájecí zdroj Supply od výrobce. Je to nezbytné, abyste zabránili poškození zařízení a předešli riziku vzniku požáru.





- Pokud váš stroj nemá vestavěnou baterii, je dobré investovat do měniče, abyste se vyhnuli náhlému vypnutí.





- V závislosti na hodnotě vašeho zařízení a zeměpisné poloze může být vhodný také systém svodičů bleskových proudů, a to buď přímo v rozváděči, nebo na použité napájecí liště.





- A nakonec nezapomeňte optimalizovat chlazení počítače: pravidelně ho čistěte a instalujte ho na chladném, dobře větraném a nepřeplněném místě, abyste zabránili přehřátí, které by mohlo vést k throttlingu (samovolnému omezení rychlosti procesoru).



# Snadná instalace uzlu Bitcoin


<partId>ca6cf2a5-0bcc-41d9-b556-0d38865bf98f</partId>




## Deštník: mnohem více než uzel Bitcoin


<chapterId>dd4c04f1-924a-43e1-94f3-ea9fbc83dd43</chapterId>



Umbrel je osobní serverový operační systém navržený tak, aby zpřístupnil selfhosting: nainstalujete Umbrel, otevřete prohlížeč na `umbrel.local` a vše spravujete prostřednictvím jednoduchého vzdáleného serveru Interface.



Projekt nejprve zpopularizoval myšlenku uzlu Bitcoin a Lightning na jedno kliknutí, poté se rozšířil na skutečný "domácí cloud": úložiště souborů a fotografií, streamování multimédií, síťové nástroje, domácí automatizaci, místní umělou inteligenci a stovky aplikací instalovatelných z integrovaného obchodu App Store.



V systému Umbrel běží každá aplikace v kontejneru Docker (izolace, atomické aktualizace, nezávislé spouštění a zastavování). Interface centralizuje přístup ke všem těmto aplikacím a nabízí jednotné přihlášení (s volitelným 2FA), aktualizace operačního systému a aplikací jedním kliknutím, živé monitorování počítače (CPU, RAM, teplota, úložiště), správu oprávnění mezi aplikacemi a přehled o jejich spotřebě.



Cílem společnosti Umbrel je proto vrátit vám kontrolu a důvěrnost nad vašimi daty, aniž byste se museli spoléhat na cloudové služby, nad rámec pouhého provozování uzlu Bitcoin.



### Umbrel Home vs umbrelOS



Společnost Umbrel nabízí dva různé přístupy:





- [**Umbrel Home**](https://umbrel.com/umbrel-home): jedná se o miniserver připravený k použití, speciálně navržený a optimalizovaný pro umbrelOS. Je kompaktní, tichý, připojený k Ethernetu, vybavený diskem NVMe SSD (volitelně až 4 TB), 16 GB RAM a čtyřjádrovým procesorem. Objednáte si jej, zapojíte a přejdete na `umbrel.local`. Funkční Umbrel můžete mít zprovozněný během několika minut. To je možnost plug-and-play.



![Image](assets/fr/081.webp)





- [**umbrelOS**](https://umbrel.com/umbrelos): jedná se o operační systém, který si můžete sami nainstalovat na svůj vlastní hardware (mini-PC, NUC, tower, dedikovaný notebook...). K dispozici máte stejný Interface a stejný obchod s aplikacemi jako v systému Umbrel Home.



![Image](assets/fr/080.webp)



V obou případech je uživatelské prostředí na straně softwaru stejné: správa v prohlížeči, aktualizace jedním kliknutím, instalace aplikací na vyžádání... Řešení typu "udělej si sám" je často ekonomičtější než nákup systému Umbrel Home (v závislosti na použitém stroji). Nedoporučoval bych však nutně vždy volit variantu DIY, protože **koupí Umbrel Home přímo přispívá k financování vývoje projektu**, protože jeho obchodní model je založen na prodeji hardwaru. A upřímně řečeno, cena 389 EUR za 2TB úložiště zůstává vzhledem ke kvalitě nabízeného zařízení velmi příznivá.



![Image](assets/fr/079.webp)



V příští kapitole se budeme zabývat tím, jak nainstalovat systém umbrelOS DIY na vlastní počítač. Stejným způsobem však můžete postupovat i v tomto kurzu BTC 202, pokud jste se rozhodli pro umbrelLOS Home.



### Případ použití: z uzlu Bitcoin do domácího cloudu



Umbrel může zůstat velmi minimalistický a zaměřený pouze na Bitcoin, nebo se může vyvinout ve skutečný multifunkční osobní server, v závislosti na vašich potřebách. Zde jsou hlavní možnosti využití serveru Umbrel:





- Jednoduchý uzel Bitcoin**: na toto základní použití se společnost Umbrel spoléhá od samého počátku. Můžete spustit Bitcoin core (nebo Knots), připojit peněženky přímo k uzlu, vystavit server Electrum, hostovat Mempool Block explorer pro zobrazení Blockchain a odhadovat poplatky... Právě na tato využití se v tomto kurzu zaměříme.



![Image](assets/fr/082.webp)





- Lightning Network**: Umbrel také umožňuje nasadit LND nebo Core Lightning, dvě implementace Lightning Network, pro správu vlastního uzlu Lightning. Díky mnoha dostupným aplikacím budete moci otevírat kanály, spravovat likviditu, provádět platby, automatizovat vyvažování, nabízet služby, připojit vzdálený Wallet nebo využívat pokročilou správu Interface. Tomuto konkrétnímu případu použití se budeme věnovat v příštím kurzu LNP 202.



![Image](assets/fr/083.webp)





- Obecný self-hosting**: s Nextcloud, Immich, Jellyfin/Plex, blokátory reklamy v rámci DNS (Pi-hole/AdGuard), VPN (WireGuard, Tailscale), domácí automatizace (Home Assistant), zálohování, správa poznámek, kancelářské nástroje, místní AI (Ollama + Open WebUI)... Umbrel se může stát vaším osobním serverem, který vám umožní získat kontrolu nad vašimi daty. Služby, které denně používáte, hostujete sami, s vyladěným uživatelským prostředím, které se velmi podobá externím řešením, a přitom si zachováváte plnou kontrolu nad svými daty a soukromím.



Díky nasazení aplikací v kontejnerech si můžete Umbrel utvářet podle svých představ: začněte s jednoduchým uzlem Bitcoin a několika aplikacemi propojenými s jeho ekosystémem, pak nainstalujte uzel Lightning vedle uzlu Bitcoin a postupně obohacujte svou instanci o vlastní aplikace, které potřebujete.



### Společenství a vzájemná pomoc



Jednou z klíčových výhod společnosti Umbrel oproti konkurenci je rozsáhlá a velmi aktivní komunita uživatelů. Můžete se s nimi spojit především prostřednictvím [jejich Discordu](https://discord.gg/efNtFzqtdx) a [jejich online fóra](https://community.umbrel.com/). Zde najdete nejen praktické rady, ale především řešení pro řešení problémů nebo opravu chyb. Je to skvělé místo, kde můžete začít, postupovat a případně pomáhat ostatním uživatelům, abyste se svým Coin nezůstali sami.



![Image](assets/fr/084.webp)



### Licence UmbrelOS



Kód Umbrelu je veřejně dostupný (můžete si ho prohlížet, Fork a upravovat), ale není pod skutečnou open-source licencí. Ve skutečnosti je umbrelOS šířen pod licencí [*PolyForm Noncommercial 1.0*] (https://polyformproject.org/licenses/noncommercial/1.0.0/), ačkoli některé související vývojové nástroje jsou k dispozici pod licencí MIT.



Z praktického hlediska můžete se systémem umbrelOS dělat v podstatě cokoli, pokud je to pro osobní, nekomerční použití: úpravy, šíření pro neziskové účely, vytváření odvozenin pro sebe nebo pro neziskové organizace za předpokladu, že dodržíte právní upozornění.



Je však zakázáno prodávat Umbrel nebo jeho odvozeniny (například předem sestavený počítač s předinstalovaným systémem umbrelOS), komerčně nabízet služby související s Umbrelem nebo integrovat jeho kód do produktu za účelem zisku.



Z technického hlediska tato licence neomezuje instalaci, audit ani přizpůsobení aplikace Umbrel pro osobní použití. Z právního hlediska chrání projekt před neoprávněným dalším prodejem nebo komerčním hostováním, zejména poskytovateli cloudových služeb. Umbrel tedy není open source, ačkoli jeho kód zůstává veřejně přístupný.



Každá aplikace ve Store si však zachovává vlastní licenci, často open source.




## Instalace zařízení Full node s deštníkem


<chapterId>61bc09c7-787d-4649-b142-457ec018b0f4</chapterId>



Nyní, když máme všechny potřebné informace, je čas proniknout do detailů. V tomto návodu vám ukážeme, jak nainstalovat kompletní uzel Bitcoin pomocí systému UmbrelOS.



### Požadované materiály



Zde budeme používat obraz UmbrelOS x86 (přesněji verzi x86_64). Tento návod budete moci použít na jakémkoli počítači, který si vyberete, pokud není vybaven procesorem architektury ARM (žádný Apple Silicon, Raspberry Pi atd.). To znamená, že vám bude stačit jakýkoli počítač s 64bitovým procesorem Intel nebo AMD, pokud splňuje minimální požadavky podle toho, jak hodláte Umbrel používat (doporučuje se alespoň dvoujádrový procesor).



Pokud jste se rozhodli pro Raspberry Pi 5 (tuto možnost nedoporučuji, jak je uvedeno v předchozí části), instalace se mírně liší. Pak můžete postupovat podle tohoto specializovaného návodu a po návratu na můj kurz na webu Interface `http://umbrel.local`:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Jak je uvedeno v předchozí části, rozhodl jsem se tento výukový program spustit na malém repasovaném počítači, který jsem našel za dobrou cenu: *Lenovo ThinkCentre M900 Tiny* s procesorem Intel Core i7 a 16 GB RAM. Jedná se o velmi pohodlnou konfiguraci pro běh Umbrelu, zejména pro uzel Bitcoin. Tuto konfiguraci jsem však zvolil proto, že chci později nainstalovat uzel Lightning a další náročnější aplikace. Do svého ThinkCentra jsem také přidal 2TB SSD, abych zachoval plný výkon Blockchain a stále měl pohodlnou rezervu. Při této konfiguraci jsou celkové náklady 270 eur včetně všech výdajů.



![Image](assets/fr/001.webp)



Obzvláště se mi líbí řada ThinkCentre Tiny od společnosti Lenovo, protože se jedná o kompaktní, tiché a velmi robustní stroje. Tyto počítače jsou velmi oblíbené u firem, a proto se hojně vyskytují na trhu s použitými počítači, kde lze najít zajímavé konfigurace v ceně od 70 do 200 eur.



Pokud jste se stejně jako já rozhodli pro počítač bez monitoru, **budete muset připojit monitor a klávesnici** pouze po dobu instalace. Poté k němu budete moci přistupovat vzdáleně z jiného počítače ve stejné síti (nebo jinými metodami, o kterých si povíme v dalších kapitolách). Budete také potřebovat ethernetový kabel RJ45 pro připojení počítače k místní síti a USB klíč o velikosti alespoň 4 GB pro uložení instalačního obrazu.



Zde jsou shrnuty požadavky na vybavení:




- Počítač s procesorem x86_64 (minimálně dvoujádrový, doporučený čtyřjádrový);
- Paměť RAM (minimálně 4 GB, pro delší použití se doporučuje 8 GB nebo více);
- SSD (doporučeno + 2 TB);
- Klíč USB (+ 4 GB) pro instalaci obrazu systému UmbrelOS;
- Monitor a klávesnice (užitečné pouze pro počáteční instalaci, pokud jimi počítač není vybaven);
- Ethernetový kabel RJ45.



### Krok 1 - Montáž počítače



V závislosti na vybraném hardwaru je prvním krokem sestavení jednotlivých součástí počítače. Například v mém případě měl původní disk SSD kapacitu pouze 256 GB, takže ho zrecykluji pro další použití a nahradím ho 2TB diskem SSD. Pokud chcete vyměnit také moduly RAM, je na to nyní ten správný čas.



### Krok 2: Příprava spouštěcího klíče USB



Před instalací systému UmbrelOS do počítače je třeba vytvořit bootovací USB klíč s operačním systémem. Všechny kroky v kroku 2 je třeba provést na vašem osobním počítači (a ne přímo na počítači určeném jako uzel).





- Začněte stažením nejnovější verze systému UmbrelOS ve formátu USB:



Přejděte na [oficiální webové stránky společnosti Umbrel a stáhněte si obraz ISO](https://download.umbrel.com/release/latest/umbrelos-amd64-usb-installer.iso) pro instalaci prostřednictvím klíče USB. Ujistěte se, že jste vybrali verzi kompatibilní s architekturou x86_64 (soubor s názvem `umbrelos-amd64-usb-installer.iso`). Stahování může chvíli trvat, protože obraz je poměrně velký.



![Image](assets/fr/002.webp)





- Nainstalujte zařízení Balena Etcher:



K vytvoření bootovacího USB flash disku použijete jednoduchý multiplatformní nástroj s názvem [Balena Etcher](https://www.balena.io/etcher/). Stáhněte si jej a nainstalujte do počítače.



![Image](assets/fr/003.webp)





- Vložte prázdný klíč USB o velikosti nejméně 4 GB:



Připojte USB klíč k počítači (k tomu, do kterého jste právě stáhli obraz UmbrelOS a Balena Etcher). **Upozornění: všechna data na klíči budou smazána**. Ujistěte se, že neobsahuje žádné důležité soubory.





- Pomocí programu Balena Etcher vypalte obraz ISO na paměť USB:



Spusťte Balena Etcher a vyberte právě stažený soubor ISO `umbrelos-amd64-usb-installer.iso` kliknutím na tlačítko "*Flash from file*". Poté vyberte USB klíč jako cílové zařízení a kliknutím na tlačítko "*Flash!*" zahajte zápis.



![Image](assets/fr/004.webp)



Po dokončení operace získáte bootovatelný USB klíč obsahující systém UmbrelOS, který je připraven ke spuštění a instalaci systému Umbrel na vašem počítači.



![Image](assets/fr/005.webp)



### Krok 3: Spuštění počítače z klíče USB



Nyní, když je bootovací USB flash disk se systémem UmbrelOS připraven, můžete z něj spustit počítač a zahájit instalaci systému. Odpojte klíč USB od hlavního počítače a vložte jej do zařízení, na které chcete nainstalovat systém Umbrel a uzel Bitcoin.



Jak bylo vysvětleno na začátku této kapitoly, k dokončení instalace budete potřebovat zobrazovací zařízení a vstupní zařízení. Připojte displej přes HDMI (nebo jiný port, v závislosti na počítači) a připojte k počítači klávesnici přes USB. Tato zařízení jsou nutná pouze pro instalaci; později je nebudete potřebovat, protože k aplikaci Umbrel budete přistupovat vzdáleně z jiného počítače. Připojte tato dvě zařízení k počítači.



**Tip:** Pokud doma nemáte periferní obrazovku, můžete použít televizor. Díky vstupu HDMI (nebo jinému) ji lze použít jako dočasnou obrazovku během instalace operačního systému.



Umbrel samozřejmě vyžaduje připojení k internetu. Připojte ethernetový kabel RJ45 mezi zařízení a směrovač.



![Image](assets/fr/006.webp)



Zapněte počítač. Ve většině případů by měl automaticky detekovat USB klíč a spustit z něj počítač. Poté se zobrazí instalační obrazovka systému UmbrelOS Interface.



Pokud se zařízení spustí v jiném systému nebo zobrazí chybovou zprávu, znamená to pravděpodobně, že se z klíče USB nespustí automaticky. V takovém případě restartujte počítač a vstupte do nastavení systému BIOS/UEFI (obvykle se k němu dostanete stisknutím kláves `DEL`, `F2`, `F12` nebo `ESC` v závislosti na výrobci počítače). Poté změňte pořadí spouštění tak, aby byla dána přednost klíči USB. Poté restartujte zařízení a spusťte systém UmbrelOS.



### Krok 4: Instalace systému UmbrelOS do počítače



Po spuštění zařízení z paměti USB vás přivítá instalace systému Interface UmbrelOS. Tento krok zahrnuje instalaci systému přímo na interní disk počítače Hard.



Na obrazovce, která se zobrazí, jsou uvedena všechna interní úložná zařízení zjištěná počítačem. U každého disku je uvedeno číslo, název a úložná kapacita. Vyhledejte disk, na který chcete nainstalovat Umbrel. **Upozornění: všechny soubory na tomto disku budou trvale smazány**



![Image](assets/fr/007.webp)



Jakmile určíte správný disk (obvykle ten s největší kapacitou, na který se vejde Blockchain), poznamenejte si číslo, které mu bylo přiděleno. Pokud se například vybraný disk objeví pod číslem `2`, jednoduše zadejte `2` a stiskněte klávesu `Enter` na klávesnici.



![Image](assets/fr/008.webp)



Program naformátuje vybraný disk, nainstaluje systém UmbrelOS a automaticky nakonfiguruje systém. To může trvat několik minut. Nechte proces běžet bez přerušení.



![Image](assets/fr/009.webp)



Po dokončení instalace budete vyzváni k vypnutí zařízení. Stisknutím libovolné klávesy počítač vypnete.



![Image](assets/fr/010.webp)



Nyní můžete odebrat klíč USB, klávesnici a obrazovku, které již nejsou pro zařízení Umbrel nutné. Z vašeho uzlu zůstane pouze napájecí kabel Supply a ethernetový kabel RJ45.



![Image](assets/fr/011.webp)



Před restartováním zařízení zkontrolujte následující dva body:





- Klíč USB je odpojen**: pokud zůstane připojen, může se systém restartovat na něm místo na interním disku;
- Ethernetový kabel je zapojen**: aby zařízení fungovalo, musí být připojeno k routeru.



Stiskněte tlačítko napájení. Systém se automaticky spustí z interního disku, na který byl nainstalován systém UmbrelOS. První spuštění může trvat přibližně **5 minut**. Během této doby systém Umbrel inicializuje své služby a systém Interface.



Na jiném počítači (vašem běžném počítači) připojeném ke **stejné místní síti** otevřete webový prohlížeč (Firefox, Chrome...) a přejděte na:



```
http://umbrel.local
```



Tato funkce Address slouží ke vzdálenému přístupu ke grafickému uživatelskému rozhraní Interface společnosti Umbrel a k zahájení konfigurace.



Pokud po uplynutí alespoň 5 minut nefunguje v prohlížeči Address `http://umbrel.local`, jednoduše to zkuste:



```
http://umbrel
```



Pokud to stále nefunguje, zadejte místní IP adresu Address zařízení Umbrel přímo do prohlížeče. Například (nahraďte `42` číslem počítače, na kterém je Umbrel v místní síti umístěn):



```
http://192.168.1.42
```



K identifikaci zařízení Umbrel IP Address existuje několik metod, od nejjednodušších až po nejpokročilejší:





- Vstupte do administrace směrovače Interface a najděte IP adresu Address zařízení Umbrel v místní síti.





- Pomocí softwaru pro skenování sítě, jako je například Angry IP Scanner, zjistěte připojená zařízení a najděte IP Address Umbrel.



![Image](assets/fr/012.webp)



https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d



- V krajním případě k zařízení znovu připojte monitor a klávesnici, přihlaste se (výchozí přihlašovací jméno: `umbrel`, heslo: `umbrel`) a zadejte následující příkaz:



```
hostname -I
```



Nyní jste připraveni používat Umbrel!



### Krok 5: Začínáme s aplikací Umbrel



Chcete-li zahájit konfiguraci zařízení Umbrel, klikněte na tlačítko "*Start*".



![Image](assets/fr/013.webp)



#### Vytvoření účtu



Zvolte si pseudonym nebo zadejte své jméno a nastavte silné heslo. Buďte opatrní: toto heslo je jedinou překážkou, která chrání přístup k vašemu Umbrelu ze sítě (a tedy potenciálně i k vašim bitcoinům, pokud na Umbrelu provozujete uzel Lightning). Chrání také vzdálený přístup přes Tor nebo VPN, pokud jsou tyto služby povoleny.



Zvolte si silné heslo a zajistěte si alespoň jednu zálohu (doporučujeme použít správce hesel).



https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Po zadání hesla klikněte na tlačítko "*Vytvořit*".



![Image](assets/fr/014.webp)



Konfigurace produktu Umbrel je nyní dokončena.



![Image](assets/fr/015.webp)



#### Objev Interface



Model Interface společnosti Umbrel je poměrně intuitivní:





- Na domovské stránce můžete zobrazit nainstalované aplikace a widgety.



![Image](assets/fr/016.webp)





- "Obchod s aplikacemi*" umožňuje instalovat nové aplikace,



![Image](assets/fr/017.webp)





- Nabídka "*Soubory*" soustřeďuje všechny dokumenty uložené v zařízení Umbrel.



![Image](assets/fr/018.webp)





- Nabídka "*Nastavení*" umožňuje upravit nastavení zařízení Umbrel a získat přístup k jeho informacím, včetně:
    - Aktualizujte, restartujte nebo zastavte počítač;
    - Zkontrolujte dostupný úložný prostor, využití paměti RAM a teplotu procesoru;
    - Změna tapety;
    - Správa vzdáleného přístupu přes Tor, aktivace Wi-Fi nebo 2FA.



![Image](assets/fr/019.webp)



#### Nastavení zabezpečení a připojení



V první řadě důrazně doporučuji zapnout dvoufaktorové ověřování (2FA). To přidá vašemu heslu další stupeň zabezpečení Layer. Je téměř nepostradatelné, pokud plánujete používat Umbrel k ukládání osobních souborů, spouštět uzel Lightning nebo provádět jakoukoli jinou citlivou činnost.



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

To provedete kliknutím na příslušné políčko v nastavení.



![Image](assets/fr/020.webp)



Poté naskenujte zobrazený QR kód pomocí autentizační aplikace. Poté zadejte šestimístný dynamický kód do pole, které je k dispozici na zařízení Umbrel.



Od této chvíle bude každé nové připojení k vašemu Umbrelu vyžadovat jak heslo, tak šestimístný kód vygenerovaný vaší aplikací dvoufaktorového ověřování (2FA).



![Image](assets/fr/021.webp)



Pokud jde o vzdálený přístup přes Tor, pokud jej nepotřebujete, doporučuji nechat tuto možnost vypnutou, abyste omezili plochu útoku na Umbrel. Ve výchozím nastavení lze k vašemu uzlu přistupovat pouze ze stroje připojeného ke stejné místní síti. Povolení přístupu přes Tor vám nicméně umožní spravovat váš Umbrel na cestách.



Pokud tuto funkci povolíte, bude teoreticky možné, aby se jakýkoli počítač na světě pokusil připojit k vašemu uzlu, pokud zná Tor Address. Heslo a 2FA vás však budou chránit i nadále.



Pokud tuto možnost aktivujete, ujistěte se, že máte povoleno dvoufaktorové ověřování (2FA), silné heslo a nikdy neprozrazujte své připojení k síti Tor Address.



Jednoduše zadejte tento Tor Address do prohlížeče Tor a získejte přístup k Umbrel Interface z jakékoli sítě.



![Image](assets/fr/026.webp)



Na této stránce nastavení můžete také aktivovat připojení Wi-Fi. Pokud je váš počítač hostující Umbrel vybaven síťovou kartou Wi-Fi nebo klíčem Wi-Fi, umožní vám to přístup k internetu bez použití kabelu RJ45. V závislosti na konfiguraci však toto řešení může zpomalit připojení, což může ovlivnit počáteční synchronizaci (IBD) a budoucí používání uzlu (např. pro transakce Lightning). Osobně tuto možnost nedoporučuji, protože uzel není určen k mobilnímu použití: vždy se k němu přistupuje vzdáleně, takže jej můžete rovnou nechat připojený.



### Krok 6: Instalace uzlu Bitcoin v systému Umbrel



Nyní, když je systém UmbrelOS v počítači správně nainstalován a nakonfigurován, můžete pokračovat v instalaci uzlu Bitcoin. Nic nemůže být jednodušší: přejděte do obchodu App Store, otevřete kategorii "*Bitcoin*" a poté vyberte aplikaci "*Bitcoin Node*" (ve skutečnosti se jedná o Bitcoin core).



![Image](assets/fr/022.webp)



Poté klikněte na tlačítko "*Install*".



![Image](assets/fr/023.webp)



Po dokončení instalace uzel Bitcoin spustí IBD (*Initial Block Download*): stáhne a ověří všechny transakce a bloky od vytvoření Bitcoin v roce 2009.



![Image](assets/fr/024.webp)



Tato fáze je obzvláště časově náročná, protože její trvání závisí na několika faktorech, včetně množství paměti RAM přidělené mezipaměti uzlu, rychlosti disku, rychlosti internetového připojení a výkonu procesoru. Rozsah doby trvání je proto v závislosti na konfiguraci velmi široký. S výkonným počítačem (disk NVMe SSD, +32 GB RAM, výkonný procesor a dobré internetové připojení) lze IBD dokončit přibližně za deset hodin. Na druhou stranu starý procesor, málo paměti RAM nebo ještě hůře mechanický disk Hard (důrazně nedoporučujeme) mohou tuto operaci prodloužit na několik týdnů.



S počítačem běžné konfigurace (slušný procesor, 8 až 16 GB RAM a SSD) vydrží zhruba 2 až 7 dní.



Chcete-li mírně zrychlit IBD, můžete zvýšit paměť RAM přidělenou mezipaměti uzlu (používá se především pro sadu UTXO, ke které se vrátíme později v kurzu) pomocí parametru `dbcache`. V systému Umbrel se tato úprava provádí v parametrech uzlu na kartě "*Optimalizace*".



![Image](assets/fr/025.webp)



Ve výchozím nastavení je hodnota parametru `dbcache` v Bitcoin core nastavena na 450 MiB, tedy přibližně 472 MB. Zvýšením této hodnoty můžete mírně zrychlit IBD. Nedoporučuji však nutně tento parametr příliš zvyšovat: i nastavení na 4 GiB zrychlí synchronizaci jen asi o 10 % a může způsobit ztrátu času v případě přerušení během IBD.



Dávejte pozor, abyste nepřidělili hodnotu, která je pro váš počítač příliš velká. Pokud dojde paměť RAM dostupná pro systém UmbrelOS, může se váš uzel náhle zastavit, přerušit IBD a vyžadovat ruční restartování, což způsobí značnou časovou ztrátu.



Chcete-li se dozvědět více o vlivu parametru `dbcache` na počáteční synchronizaci, doporučuji tuto analýzu od Jamesona Loppa: [*Effects of DBcache Size on Bitcoin Node Sync Speed*](https://blog.lopp.net/effects-dbcache-size-Bitcoin-node-sync-speed/)



Po dokončení IBD uzlu (100% synchronizace) máte plně funkční uzel Bitcoin. Gratulujeme, nyní jste nedílnou součástí sítě Bitcoin!



![Image](assets/fr/027.webp)



V příští části se budeme zabývat praktickým využitím vašeho nového uzlu: jak k němu připojit Wallet a jaké aplikace byste si měli nainstalovat, abyste se stali suverénními uživateli Bitcoinu.





# Připojení Wallet k uzlu


<partId>418d0afd-3a61-4b5a-9db4-203c0335fd29</partId>



## Indexéry: úloha, fungování a řešení


<chapterId>4f93c07a-f0cb-435f-8b68-162f316d7039</chapterId>



Pokud jste již před absolvováním tohoto kurzu zkoumali uzly Bitcoin, možná jste se setkali s pojmem "indexer". Jedná se o nástroje jako Electrs nebo Fulcrum, které lze přidat k uzlu Bitcoin core. Jaká je však přesně jejich úloha? Jak fungují v praxi? A měli byste si nějaký nainstalovat na svůj nový uzel Bitcoin? Právě to prozkoumáme v této kapitole.



### Co je to indexer?



Obecně lze říci, že indexátor je program, který prohledává soubor nezpracovaných dat, extrahuje relevantní klíče (například slova, identifikátory a adresy) a vytváří pomocný soubor nazývaný "index", kde každý klíč odkazuje na přesné umístění dat v korpusu. Tato fáze předběžného zpracování využívá čas procesoru a vyžaduje určitý prostor na disku, ale eliminuje potřebu zpracovávat celý korpus při každém dotazu do databáze; pouhý dotaz na index poskytuje téměř okamžitou odpověď.



Laicky řečeno, jde o stejný princip jako rejstřík v knize: pokud hledáte konkrétní informaci, místo abyste znovu četli celou knihu, vyhledáte v rejstříku přímo stránku, kde se hledaná informace nachází.



V uzlu Bitcoin, jako je Bitcoin core, jsou data Blockchain uložena v nezpracované, chronologické podobě. Každý blok obsahuje transakce, které zase obsahují vstupy a výstupy, bez zvláštního třídění podle Address, identifikátoru nebo Wallet. Toto lineární uspořádání je optimální pro ověřování bloků, ale nevhodné pro cílené vyhledávání. Pokud byste například chtěli najít všechny transakce spojené s konkrétním Address v neindexovaném uzlu, museli byste ručně procházet celý Blockchain, blok po bloku a transakci po transakci. Právě k tomu slouží indexátor v uzlu Bitcoin.



![Image](assets/fr/085.webp)



Indexer je specializovaný softwarový program, který analyzuje tuto masu nezpracovaných dat (sada Blockchain, Mempool, UTXO) a extrahuje klíče, jako jsou identifikátory transakcí, adresy a výšky bloků. Z těchto klíčů sestaví svůj index, přičemž každý klíč přiřadí k přesnému umístění informace v úložišti uzlu.



![Image](assets/fr/086.webp)



Indexování umožňuje rychlé, přesné a efektivní vyhledávání informací v uzlu. Když například připojíte k uzlu Wallet jako Sparrow, může se téměř okamžitě zobrazit zůstatek Address. Konkrétně se dotazuje indexeru s požadavkem jako např: "_Které UTXO jsou spojeny s tímto skriptem-Hash?_" Indexer odpoví téměř okamžitě, aniž by musel znovu číst celý Blockchain, protože tyto údaje jsou již uvedeny v jeho databázi.



### Má Bitcoin core indexer?



Bez potřeby dalšího softwaru nenabízí Bitcoin core, přísně vzato, kompletní indexátor Address srovnatelný s těmi, které lze nalézt v softwaru Electrs nebo Fulcrum. Nicméně obsahuje několik interních indexovacích mechanismů a také volitelné možnosti pro rozšíření svých dotazovacích schopností. Abychom situaci plně pochopili, musíme se oklikou podívat do historie projektu.



Do verze 0.8.0 systému Bitcoin core bylo ověřování transakcí založeno na globálním indexu transakcí, známém jako `txindex`. Tento index odkazoval na všechny transakce Blockchain a jejich výstupy. Když uzel obdržel novou transakci, nahlédl do tohoto indexu, aby ověřil, že spotřebované výstupy (na vstupech) skutečně existují a nebyly již utraceny. `txindex` byl tedy v té době pro ověřování transakcí nepostradatelný.



Tento přístup však měl svá omezení: byl pomalý, nákladný z hlediska ukládání a redundantní z hlediska informací. Aby se to napravilo, verze 0.8.0 zavádí přepracování validačního modelu nazvaného ***Ultraprune***. Namísto ukládání všeho ve formě transakčních indexů udržuje Bitcoin core jednoduchou databázi určenou výhradně pro UTXO, nazvanou `chainstate` (v běžném jazyce se jí říká "sada UTXO"), a aktualizuje její seznam podle toho, jak jsou výstupy spotřebovávány a vytvářeny.



Tato metoda je mnohem rychlejší a ukládá pouze aktuální stav registru, takže indexer `txindex` není nutný. Místo odstranění kódu `txindex` se však vývojáři rozhodli ponechat tuto funkci za jednoduchým parametrem (`txindex=1`). Povolením tohoto parametru v uzlu se můžete dotazovat na libovolnou transakci z jeho `txid`.



Navzdory všeobecnému přesvědčení Bitcoin core nenabízí indexování na bázi Address jako Electrs nebo Fulcrum. Tato volba má několik důvodů:





- Úkolem Bitcoin core není stát se kompletním Block explorer ani poskytovat rozhraní API přizpůsobené každému použití. Integrace indexu založeného na Address by znamenala dlouhodobou údržbu Commitment, která přesahuje původní rozsah softwaru.





- Většinu případů použití lze již pokrýt jinými způsoby. Například pro odhad bilance sady Address můžete použít příkaz `scantxoutset`, který se přímo dotazuje na sadu UTXO, aniž by vyžadoval úplný index.





- Každý softwarový program má specifické požadavky na formát nebo typ dat, která mají být indexována (skript Address, Hash, proprietární značka atd.). Je pružnější a logičtější nechat tyto programy vytvořit vlastní indexy na míru, než opravovat obecné řešení v Bitcoin core.



Bitcoin core má volitelný transakční indexátor (`txindex`), pozůstatek svého historického fungování, ale neposkytuje index Address ani přímý Interface pro komplexní vyhledávání. V některých případech proto může být užitečné přidat externí indexer.



### Měli byste do uzlu přidat indexer Address?



Přidání indexeru Address, například Electrs nebo Fulcrum, není povinné; záleží na vašich konkrétních potřebách.



Pokud chcete jednoduše připojit k uzlu Wallet, například Sparrow, abyste mohli zobrazit zůstatky a vysílat transakce, je to zcela možné přímo prostřednictvím Interface RPC Bitcoin core, a to buď lokálně, nebo vzdáleně přes Tor.



Na druhou stranu, pro použití pokročilejšího softwaru, jako je například spuštění Mempool. Místně se instalace indexeru Address stává nezbytnou pro prostor Block explorer.



Indexer vyžaduje určitý čas synchronizace (méně než IBD) a zabere další místo na disku. Pokud má váš SSD disk po stažení Blockchain stále dostatek volného místa, můžete indexer snadno přidat.



### Který indexer zvolit?



K vytvoření tohoto typu indexu Address a jeho zpřístupnění se běžně používají dva softwarové programy: **Electrs** a **Fulcrum**. Tyto nástroje indexují Blockchain podle skriptů-Hash (adresy) a následně navrhují standardizovaný Interface (protokol Electrum), ke kterému se připojují četné peněženky, například Electrum Wallet, Sparrow nebo Phoenix.



![Image](assets/fr/087.webp)



Jednoduše řečeno, Electrs je poměrně kompaktní: indexuje Blockchain rychleji a zabírá méně místa na disku, ale v dotazech si vede o něco hůře než Fulcrum. Naproti tomu Fulcrum spotřebuje více místa na disku a jeho indexování trvá déle, ale nabízí lepší výkonnost při dotazování.



Pro individuální použití doporučuji Electrs: spotřebovává méně místa, je dobře udržovatelný, a i když je v některých požadavcích o něco pomalejší než Fulcrum, pro každodenní použití je stále více než dostatečný. Pokud máte čas a místo na disku, můžete vyzkoušet také Fulcrum, který bude fungovat výrazně lépe, zejména u peněženek s mnoha adresami k ověření.



Konkrétně v srpnu 2025 bude společnost Electrs potřebovat přibližně 56 GB úložného prostoru, zatímco společnost Fulcrum přibližně 178 GB. Volba indexeru tedy závisí také na kapacitě úložiště:




- Pokud máte na disku velmi málo místa, budete si muset vystačit s nástrojem Bitcoin core bez externího indexeru Address.
- Pokud chcete používat indexer, ale jste stále omezeni kapacitou, zvolte Electrs.
- Pokud máte dostatek místa na disku, může být Fulcrum přesně to, co hledáte.



Ve zbytku tohoto kurzu BTC 202 budu používat Electrum, ale můžete snadno postupovat i s Fulcrumem: postup instalace je totožný, stejně jako připojení Interface ke Wallet, protože oba vystavují server Electrum.



### Jak nainstaluji indexer v systému Umbrel?



Postup instalace aplikace Electrs (nebo Fulcrum) do zařízení Umbrel je jednoduchý: přejděte do obchodu App Store, vyhledejte příslušnou aplikaci (nachází se na kartě Bitcoin) a klikněte na tlačítko "*Install*".



![Image](assets/fr/028.webp)



Po dokončení instalace přejde společnost Electrs k synchronizační (indexovací) fázi, která může trvat několik hodin.



![Image](assets/fr/029.webp)



Po dokončení synchronizace můžete připojit software Wallet k serveru Electrum, který je hostován na serveru Umbrel.



## Jak připojím svůj Wallet k uzlu Bitcoin?


<chapterId>35519b1a-f681-4a69-a652-9fbe510cd17f</chapterId>



Nyní, když máte kompletní uzel Bitcoin, je na čase jej dobře využít! V příští kapitole se budeme zabývat dalšími možnostmi využití vaší instance Umbrel. Začněme však od základů: připojte svůj software Wallet tak, aby využíval informace z vašeho vlastního uzlu Blockchain a distribuoval transakce prostřednictvím vašeho vlastního uzlu.



Jak bylo uvedeno výše, existují dvě hlavní rozhraní pro připojení:




- Přímé připojení ke Bitcoin core prostřednictvím RPC;
- Nebo se připojte k serveru Electrum (Electrs nebo Fulcrum).



V tomto návodu se zaměříme na připojení k uzlu přes Tor, protože je to jednoduché a bezpečné řešení pro začátečníky. Důrazně nedoporučuji vystavovat port RPC vašeho uzlu v otevřeném režimu, protože chybná konfigurace představuje značné riziko pro bezpečnost a důvěrnost vašich dat. Hlavní nevýhodou komunikace přes Tor je její pomalost. V příští kapitole se budeme zabývat rychlou a bezpečnou alternativou k Toru pro vzdálený přístup k vašemu uzlu: VPN.



V této kapitole budeme jako příklad používat Sparrow, ale postup je stejný pro všechny ostatní softwary pro správu Wallet, které přijímají připojení k serverům Electrum. Stačí najít příslušné nastavení v parametrech aplikace (obvykle v položkách "*Server*", "*Network*", "*Node*"...).



V systému Sparrow otevřete kartu "*Soubor*" a přejděte do nabídky "Nastavení".



![Image](assets/fr/030.webp)



Poté klikněte na položku "*Server*" a získáte přístup k parametrům připojení.



![Image](assets/fr/031.webp)



Poté se dozvíte tři možnosti propojení softwaru s uzlem Bitcoin:




- Veřejný server* (žlutá): ve výchozím nastavení, pokud nevlastníte uzel Bitcoin, vás tato možnost připojí k veřejnému uzlu, který nevlastníte (obvykle k uzlu společnosti). Tato volba zde není relevantní, protože máte svůj vlastní uzel Umbrel.
- Bitcoin core* (Green): tato možnost odpovídá připojení přes Interface RPC, tj. přímo ke Bitcoin core.
- Private Electrum* (modrá): tato možnost umožňuje připojení prostřednictvím serveru Electrum Interface indexeru (Electrs nebo Fulcrum).



### Připojení ke Bitcoin core RPC



Pokud váš uzel Umbrel nemá indexer, je třeba vybrat tuto možnost. Na obrazovce Sparrow klikněte na položku "*Bitcoin core*".



![Image](assets/fr/032.webp)



Poté je třeba zadat několik informací pro vytvoření připojení k uzlu. Všechny tyto údaje jsou přístupné z aplikace "*Bitcoin Node*" v aplikaci Umbrel po kliknutí na tlačítko "*Connect*" v pravém horním rohu Interface.



![Image](assets/fr/033.webp)



Na kartě "*RPC Details*" se zobrazí všechny potřebné informace pro připojení. Zvolte připojení přes Tor Address (v `.onion`).



![Image](assets/fr/034.webp)



Zadejte tyto údaje do odpovídajících polí na Sparrow wallet a klikněte na tlačítko "*Test Connection*".



![Image](assets/fr/035.webp)



Pokud je připojení úspěšné, zobrazí se zaškrtnutí Green a potvrzovací zpráva.



![Image](assets/fr/036.webp)



Zaškrtávátko vpravo dole u Interface Sparrow wallet bude nyní Green (což znamená přímé spojení s Bitcoin core).



**Poznámka:** Aby bylo připojení úspěšné, musí být váš uzel 100% synchronizován. Pokud tomu tak není, vyčkejte do konce IBD.



### Připojení k Electrs



Pokud má váš uzel indexer, je lepší se připojit k němu než přímo ke Bitcoin core, protože vaše dotazy budou zpracovány rychleji.



V systému Sparrow přejděte na kartu "*Soukromé Electrum*".



![Image](assets/fr/037.webp)



Poté budete muset zadat několik informací, abyste navázali spojení s indexerem. Tyto údaje naleznete v aplikaci "*Electrs*" (případně "*Fulcrum*") na serveru Umbrel.



Výběrem karty "*Tor*" získáte připojení `.onion` Address. Pokud chcete připojit mobilní software Wallet, můžete také přímo naskenovat QR kód.



![Image](assets/fr/038.webp)



Do pole "*URL*" jednoduše zadejte Tor Address svého serveru Electrum a poté klikněte na tlačítko "*Test Connection*".



![Image](assets/fr/039.webp)



Pokud je připojení úspěšné, zobrazí se zaškrtnutí a potvrzovací zpráva.



![Image](assets/fr/040.webp)



Zaškrtnutí v pravém dolním rohu zařízení Interface Sparrow wallet zmodrá (barva spojená s připojením k serveru Electrum).



**Poznámka:** Aby připojení fungovalo, musí být váš indexer 100% synchronizován. Pokud tomu tak není, počkejte, dokud nebude proces indexování dokončen.



Nyní víte, jak připojit Wallet k uzlu Bitcoin! V další kapitole vás seznámím s několika dalšími aplikacemi dostupnými v systému Umbrel, které jsem si obzvláště oblíbil a které vám umožní rozšířit každodenní používání systému Bitcoin prostřednictvím vašeho uzlu.




## Přehled dostupných aplikací


<chapterId>2a5ccfbe-0b17-44c9-863c-b7e8cb4b4594</chapterId>



Umbrel nabízí rozsáhlý obchod s aplikacemi. Jak uvidíte, je zde mnoho nástrojů souvisejících s Bitcoin, ale také široká škála aplikací z velmi odlišných oblastí: řešení pro selfhosting služeb a souborů, aplikace pro produktivitu, obecnější finanční nástroje, správa médií, zabezpečení a správa sítě, vývoj, umělá inteligence, sociální sítě, a dokonce i domácí automatizace.



V tomto kurzu BTC 202 se zaměříme výhradně na aplikace související s Bitcoin. Neváhejte však prozkoumat zbytek katalogu, kde najdete nástroje, které by se vám mohly hodit.



Samozřejmě by bylo nemožné uvést zde všechny aplikace Bitcoin. V této kapitole bych vás rád seznámil se základními nástroji, které vám usnadní a obohatí každodenní používání Bitcoin.



### Mempool.space



Pokud je při každodenním používání Bitcoin nějaký nástroj skutečně nepostradatelný, je to Block explorer. Ať už je přístupný online nebo nainstalovaný lokálně, transformuje surová data Blockchain do strukturovaného, přehledného a snadno čitelného formátu. Je také vybaven vyhledávačem, který uživatelům umožňuje rychle vyhledat konkrétní blok, transakci nebo Address.



Konkrétně vám průzkumník umožní odhadnout poplatky potřebné pro zařazení transakce do bloku, poté sledovat její průběh: zjistit, zda bude v blízké budoucnosti pravděpodobně zařazena v závislosti na trhu s poplatky, a nakonec potvrdit, že byla do bloku skutečně zařazena. Nabízí také možnost analyzovat své minulé transakce a nahlížet do jejich historie. Stručně řečeno, je to švýcarský armádní nůž bitcoinera.



Jak již bylo zmíněno, průzkumník může být umístěn online na webové stránce nebo může být spuštěn lokálně v počítači. Hlavní nevýhodou online služeb je, že mohou ohrozit vaše soukromí. Bez VPN nebo Tor může server hostující průzkumníka propojit vaši IP adresu Address s prohlíženými transakcemi, což může poskytnout ideální vstupní bod pro řetězovou analýzu.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Navíc váš poskytovatel internetových služeb (ISP) může vědět, že si určitou transakci prohlížíte prostřednictvím webu Block explorer. To s sebou nese i otázku důvěryhodnosti: musíte se spoléhat na to, že vám online služba poskytne přesné informace o vašich transakcích, aniž byste si jejich pravdivost mohli sami ověřit.



Proto je vždy nejlepší použít vlastní místní službu Block explorer. Tímto způsobem neuniknou žádná data související s vaší vyhledávací činností, protože všechny dotazy jsou zpracovávány přímo na počítači, který máte pod kontrolou, aniž by procházely Internetem. Navíc se místní průzkumník spoléhá na data z vašeho vlastního uzlu Bitcoin, která jste si sami ověřili podle vlastních pravidel a kterým můžete důvěřovat.



Umbrel nabízí několik blokových průzkumníků:




- Mempool.Space
- Bitfeed
- BTC RPC Explorer



Obzvláště se mi líbí Mempool.Space, který jsem nainstaloval na svůj uzel. Upozornění: k použití většiny blokových průzkumníků v Umbrelu je zapotřebí indexátor Address. Potřebujete tedy aplikaci Bitcoin Node (nebo Bitcoin Knots), která má 100% synchronizaci s Blockchain, a také indexer, například Electrs nebo Fulcrum, který je také 100% synchronizovaný.



Po instalaci aplikace ji jednoduše otevřete a získáte přístup k vlastnímu průzkumníkovi.



![Image](assets/fr/041.webp)



Chcete-li se dozvědět více o používání průzkumníka Mempool.Space, doporučuji tento obsáhlý návod:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

### Uzel Lightning



Nyní, když máte vlastní uzel Bitcoin, můžete také nastavit vlastní uzel Lightning pro provádění transakcí off-chain, aniž byste se museli spoléhat na infrastrukturu třetí strany.



Společnost Umbrel nabízí řadu aplikací, které vám pomohou uzel Lightning zprovoznit. Již nyní si můžete vybrat mezi dvěma hlavními implementacemi:




- LND prostřednictvím aplikace *Lightning Node*;
- Jádro Lightning.



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Svůj uzel pak můžete spravovat z hlavního okna Interface nebo si pro ještě větší funkčnost a pokročilé možnosti nainstalovat *Ride The Lightning* nebo *ThunderHub*. Tyto nástroje vám poskytnou mnohem komplexnější webový systém správy uzlu Interface.



https://planb.network/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.network/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

![Image](assets/fr/088.webp)



Nakonec doporučuji aplikaci *Lightning Network+*, která umožňuje vyhledat partnery, s nimiž lze otevřít kanály, což umožňuje odchozí i příchozí peněžní transakce.



![Image](assets/fr/089.webp)



Díky Umbrelu se správa osobního uzlu Lightning výrazně zjednodušila, ale stále je poměrně složitá. Z tohoto důvodu se tomuto tématu budeme blíže věnovat v některém z budoucích kurzů, který bude celý věnován tomuto využití.



### Stupnice ocasu



Další aplikací, která se mi na Umbrelu obzvlášť líbí, je Tailscale. Jedná se o aplikaci VPN, která je navržena tak, aby zjednodušila vytváření bezpečných sítí mezi více zařízeními, ať už se nacházejí kdekoli na světě. Na rozdíl od tradičních sítí VPN, které se spoléhají na centralizované servery, využívá Tailscale protokol WireGuard k navázání end-to-end šifrovaných spojení mezi různými počítači. To znamená, že funkční VPN můžete nasadit během několika minut, aniž byste museli složitě konfigurovat síť.



Instalace Tailscale připojí váš uzel Bitcoin k vaší vlastní virtuální privátní síti. Po konfiguraci získá váš uzel soukromou IP adresu Tailscale Address, která je přístupná pouze z jiných zařízení připojených ke stejné síti Tailscale (například z počítačů, chytrých telefonů a tabletů). Toto připojení je šifrované od konce ke konci a neprochází nechráněnou veřejnou sítí, což výrazně zvyšuje bezpečnost ve srovnání s nešifrovaným připojením.



![Image](assets/fr/090.webp)



Konkrétně vám Tailscale nabízí několik výhod při používání Umbrelu:





- Můžete spravovat Interface Umbrel nebo přistupovat k aplikacím propojeným s vaším uzlem (například Mempool, Ride The Lightning, ThunderHub...) odkudkoli, jako byste byli ve stejné místní síti, aniž byste vystavovali porty na internetu a aniž byste museli procházet přes Tor, který je velmi pomalý;





- Můžete se připojit k serveru Electrum (Electrs nebo Fulcrum) nebo přímo ke službě Bitcoin core prostřednictvím sítě VPN a obejít tak Tor. Tím získáte bezpečné připojení srovnatelné s použitím Toru, ale s mnohem vyšší rychlostí a nižší latencí. Stručně řečeno, zachováte si soukromí a bezpečnostní výhody Toru a zároveň si budete užívat rychlosti připojení Clearnet. Pro On-Chain Wallet se tento zisk může zdát zanedbatelný, ale pokud plánujete později zřídit vlastní uzel Lightning, rozdíl je značný. Provádění plateb přes váš uzel za pohybu na Toru je totiž extrémně pomalé kvůli četným potřebným výměnám, zatímco s Tailscale to funguje perfektně.





- Není třeba konfigurovat pravidla NAT, otevírat porty ani nastavovat běžný server VPN. Jakmile je aplikace nainstalována v zařízeních Umbrel a vašich zařízeních, síť se vytvoří automaticky.



Tailscale na platformě Umbrel je proto velmi zajímavým řešením, pokud chcete ke svému uzlu přistupovat odkudkoli na světě bezpečným, vysoce výkonným a snadno konfigurovatelným způsobem, aniž byste museli obětovat soukromí nebo bezpečnost.



Postup instalace a konfigurace Tailscale v systému Umbrel naleznete v tomto návodu v části 4: "*Použití Tailscale v systému Umbrel*":



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Nostr



Nostr, zkratka pro "*Notes and Other Stuff Transmitted by Relays*", je otevřený, decentralizovaný protokol navržený tak, aby umožňoval publikování a výměnu zpráv na internetu bez závislosti na centralizované platformě. Každý uživatel má dvojici kryptografických klíčů: veřejný klíč (`npub`), který slouží jako identifikátor, a soukromý klíč (`nsec`), který se používá k podepisování zpráv a zaručuje jejich pravost.



Zprávy se přenášejí prostřednictvím sítě nezávislých relé. Díky této distribuované architektuře je Nostr odolný vůči cenzuře: žádný jednotlivý server nekontroluje přístup ani distribuci a uživatel se může připojit k libovolnému počtu relé.



Tento protokol je v komunitě Bitcoin velmi populární, protože stejně jako Bitcoin řeší Nostr otázky digitální suverenity a kontroly dat. Jeho tvůrce, Fiatjaf, je vývojář, který je již v ekosystému uznáván za své četné příspěvky.



Pomocí nástroje Umbrel můžete optimalizovat používání služby Nostr. Instalací aplikace ***Nostr Relay*** můžete hostovat vlastní soukromé relay přímo na svém počítači, čímž zajistíte, že všechny vaše příspěvky a interakce na Nostru budou uloženy lokálně a nemohou být ztraceny smazáním veřejnými relay.



Klienti Nostr ***noStrudel*** nebo ***Snort*** jsou také k dispozici na Umbrel. Díky těmto aplikacím můžete publikovat, číst, vyhledávat profily a komunikovat s ekosystémem Nostr přímo z webu Interface na serveru Umbrel.



A konečně je tu aplikace ***Nostr Wallet Connect*** na platformě Umbrel, která umožňuje nativní platby Lightning v aplikaci Nostr. Konkrétně můžete propojit svůj budoucí uzel Lightning se zákazníky Nostr a posílat mikroplatby, tzv *zaps*, za odměnu za obsah nebo monetizovanou interakci, aniž byste museli procházet službou třetí strany. Tyto platby jsou odesílány přímo z vašeho osobního uzlu prostřednictvím vašich kanálů.



Chcete-li zjistit, jak všechny tyto aplikace používat, doporučuji vám podívat se na tento kompletní návod:



https://planb.network/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

### Server BTCPay



BTCPay Server je bezplatný platební procesor s otevřeným zdrojovým kódem, který vám umožňuje přijímat platby prostřednictvím Bitcoin a Lightning Network bez zprostředkovatelů, přičemž si zachovává vlastní úschovu prostředků.



Architektura BTCPay Serveru je založena na uzlu Bitcoin a v případě Lightningu na kompatibilní implementaci (LND, Core Lightning...), což z něj činí jedno z mála řešení PoS, které je zcela nezávislé. Je to také nejkomplexnější software pro sledování a účtování.



![Image](assets/fr/091.webp)



Pokud vlastníte firmu a chcete přijímat platby Bitcoin přímo prostřednictvím uzlu Umbrel, je pro vás aplikace BTCPay Server ideální. Chcete-li se o tomto tématu dozvědět více, doporučuji vám nahlédnout do následujících zdrojů:





- Kurz BIZ 101 o používání Bitcoin ve vaší firmě:



https://planb.network/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a



- Kurz POS 305 o používání serveru BTCPay:



https://planb.network/courses/6fc12131-e464-4515-9d3f-9255365d5fa1



- Výukový program serveru BTCPay:



https://planb.network/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


# Pokročilé koncepty a osvědčené postupy


<partId>fc77a62a-8d9f-4144-9080-3057b04db2c6</partId>



## Údržba deštníkového uzlu


<chapterId>06d77d09-bf24-4555-b2ba-c08bbda477c7</chapterId>



Na úvod této závěrečné části a předtím, než přejdeme k pokročilejší teorii, bych se v této krátké kapitole rád věnoval osvědčeným postupům a konkrétním činnostem, které můžete provést po instalaci, synchronizaci a správné konfiguraci uzlu Umbrel. Jak jej udržujete na každodenní bázi?



### Udržování zařízení v dobrém stavu



Spolehlivý uzel začíná u stabilního hardwaru. Zajistěte, aby byl stroj, v němž je uzel umístěn, řádně větraný, bez Dust a nainstalovaný v suchém prostředí, mimo zdroje tepla a vlhkosti. Vyvarujte se jeho nacpání do stísněného prostoru a zvolte dobře větrané místo.



U počítačů Raspberry Pi a mini-PC Dust nakonec ucpává chladiče, zvyšuje teplotu a vede k throttlingu (dobrovolnému omezování využívání zdrojů), což má za následek pokles účinnosti uzlu. Proto doporučuji pravidelně čistit přívod vzduchu a ventilátor, ideálně každých několik měsíců.



Ujistěte se, že používáte vysoce kvalitní napájecí zdroj Supply, protože nestabilní napětí může vést k poškození systému a dokonce k nebezpečí požáru. V ideálním případě byste měli používat originální napájecí zdroj Supply dodávaný výrobcem vašeho stroje. Dávejte si také pozor na přehřátí v důsledku Jouleova jevu u napájecích lišt: vždy dodržujte maximální přípustný výkon a nikdy nezapojujte několik napájecích lišt do kaskády.



Doporučuji také investovat do UPS. To ochrání váš uzel před náhlým vypnutím, umožní čistě vypnout Umbrel v případě výpadku a zajistí kontinuitu provozu při mikro výpadcích nebo krátkodobých poruchách.



Na straně úložiště sledujte vývoj: pokud se disk blíží k nasycení, zvažte uvolnění místa (odinstalujte nepoužívané aplikace, upravte nastavení indexátoru) nebo přejděte na větší SSD. Nevýhodou plného uzlu Bitcoin je, že jeho nároky na úložiště se neustále zvyšují, protože každých 10 minut se generuje nový blok a staré bloky nelze odstranit (pokud se nejedná o uzel pruned). Proto doporučuji při nákupu hardwaru počítat s dostatečně velkou kapacitou (minimálně 2 TB).



### Aktualizace



Aktualizace uzlů jsou důležité ze tří hlavních důvodů: zaprvé z důvodu bezpečnosti (opravy zranitelností, posílení sítě a ochrana před útoky DoS), zadruhé z důvodu kompatibility (změny zásad přenosu, změny formátu a aktualizace protokolu) a zatřetí z důvodu spolehlivosti a výkonu (opravy chyb, snížení spotřeby prostředků a další vylepšení). Pravidelně proto kontrolujte, zda jsou systém UmbrelOS a vaše aplikace aktuální:





- Aktualizace systému: Otevřete nabídku nastavení a klikněte na tlačítko "*Zkontrolovat aktualizaci*" vedle parametru "*UmbrelOS*".



![Image](assets/fr/042.webp)





- Aktualizace aplikací: Přejděte do obchodu App Store. Pokud některá z vašich aplikací vyžaduje aktualizaci, zobrazí se v pravém horním rohu zařízení Interface tlačítko s červenou bublinou. Jednoduše na něj klikněte a poté jednotlivé aplikace aktualizujte.



Tuto operaci provádějte pravidelně, abyste udrželi operační systém a aplikace aktuální.



### Zálohování



Pokud k ověřování a distribuci transakcí používáte pouze uzel Bitcoin, ale vaše peněženky jsou spravovány mimo Umbrel (např. pomocí Hardware Wallet a Sparrow wallet), není co zálohovat přímo do Umbrelu. V takovém případě zůstává zásadní záloha obnovovací fráze a Descriptor vašeho externího uzlu Wallet, a to platí bez ohledu na to, zda používáte vlastní uzel, nebo ne. Na vaší předchozí konfiguraci se tedy nic nemění.



Na druhou stranu, v závislosti na dalších aplikacích, které v systému Umbrel používáte, může být zapotřebí dalších záloh. To platí zejména v případě, že na platformě Umbrel provozujete uzel Lightning. V takovém případě je naprosto nezbytné zálohovat uzel seed dodaný při instalaci uzlu Lightning. Kromě seed potřebujete také aktuální ***Static Channel Backup (SCB)***, abyste mohli v případě problému obnovit svůj uzel Lightning. SCB umožňuje obnovit vaše prostředky násilným uzavřením kanálů. Pokud chybí buď seed, nebo SCB, není možné obnovit uzel Lightning.



Společnost Umbrel také nabízí možnost automatického a dynamického zálohování tohoto SCB na svých serverech prostřednictvím sítě Tor, aby byl vždy k dispozici aktuální soubor. V tomto případě je k obnovení uzlu potřeba pouze seed.



K těmto aspektům se podrobně vrátíme v příštím kurzu LNP202.



### Každodenní provozní bezpečnost



Pokud jde o zabezpečení, používejte dlouhé, jedinečné a náhodné heslo pro Interface Umbrel a nezapomeňte aktivovat dvoufaktorové ověřování (2FA). U aplikací, které nabízejí ochranu heslem i 2FA, vždy aktivujte obě tyto ochrany a změňte výchozí hesla.



Nikdy nevystavujte ovládací panel internetu bez použití zabezpečené brány (například VPN, Tor nebo pouze místní přístup). Omezte počet instalovaných aplikací a pravidelně odstraňujte ty, které již nepotřebujete, abyste omezili plochu pro útoky.



Chcete-li prohloubit své znalosti o počítačové bezpečnosti obecně, doporučuji vám podívat se na tento další bezplatný kurz:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Diagnostika a svépomoc



V případě chyby v systému Umbrel nejprve proveďte diagnostiku pomocí diagnostického balíčku generate v sekci pro řešení problémů v systému UmbrelOS nebo v příslušné aplikaci a poté aplikaci čistě restartujte. V případě potřeby se také pokuste o úplný restart systému.



Pokud problém přetrvává, doporučuji vám [připojit se ke komunitě uživatelů Umbrel na jejich Discordu](https://discord.gg/efNtFzqtdx). Začněte vyhledáváním, zda se již někdo nesetkal se stejnými potížemi a nenašel řešení. Pokud ne, můžete napsat zprávu do kanálu `general-support`. Můžete také použít [fórum Umbrel](https://community.umbrel.com/).



V těchto oblastech můžete nejen sledovat bezpečnostní oznámení a aktualizace, ale také klást dotazy a nakonec pomáhat ostatním uživatelům. Právě v těchto výměnách názorů se často objevují osvědčené postupy.



Díky těmto jednoduchým návykům zůstane váš uzel Umbrel stabilní, bezpečný a užitečný jak pro vás, tak pro síť Bitcoin.




## Porozumění IBD a procesu vzájemného zjišťování informací


<chapterId>175ac9d1-ea23-45d9-9918-d3e7352435cd</chapterId>



Uzel Bitcoin se spouští bez předchozí znalosti historie transakcí. Zpočátku je to jen počítač se spuštěným softwarem (Bitcoin core nebo podobným). Aby se stal plně synchronizovaným a funkčním uzlem Bitcoin, musí lokálně rekonstruovat stav Ledger kontrolou všech bloků zveřejněných od bloku Genesis (blok 0, zveřejněný Satoshi Nakamotem 3. ledna 2009). Tento krok se nazývá **IBD (_Initial Block Download_)**.



IBD spočívá ve stažení a ověření každého bloku a transakce jednotlivě za použití pravidel konsensu, čímž se vytvoří vlastní verze Blockchain. Cílem není pouze načíst kopii neověřených dat, ale dospět ke stejnému závěru zcela nezávisle, jako poctivá většina sítě.



![Image](assets/fr/092.webp)



### Milníky IBD



Synchronizace začíná krokem _**headers-first**_. Váš uzel si vyžádá posloupnost hlaviček bloků od několika rovnocenných uzlů a u každého z nich ověří Proof of Work, úpravu obtížnosti, syntaxi, jakož i pravidla Timestamp a číslo verze. Stručně řečeno, zajistí, aby každá přijatá hlavička vyhovovala pravidlům konsensu.



![Image](assets/fr/093.webp)



Připomínáme, že blok Bitcoin se skládá z 80bajtové hlavičky a seznamu transakcí. Otisk bloku se získá použitím dvojité SHA-256 Hash na tuto hlavičku, která obsahuje 6 polí:




- verze
- Hash předchozího bloku
- Merkle Root transakcí
- Timestamp (delší než medián času předchozích 11 bloků)
- cíl obtížnosti
- Nonce



![Image](assets/fr/094.webp)



Transakce se zapisují do zařízení Merkle Tree. Jedná se o strukturu, která shrnuje velkou množinu dat (v tomto případě všechny transakce v bloku) tak, že jejich hashe postupně agreguje po dvou až do jediného "kořene", čímž se prokáže, že prvek patří do množiny (a zjistí se případná změna). Tímto způsobem jakákoli modifikace transakce modifikuje také kořen Merkle Tree, a tedy otisk záhlaví bloku. SegWit zavedl samostatný dodatečný Commitment pro cookies (podpisy), umístěný v bázi mincí.



![Image](assets/fr/095.webp)



Tento krok _**headers-first**_ umožňuje uzlu identifikovat větev s největším objemem práce (bez ohledu na počet bloků), což je větev, na které se uzly Bitcoin synchronizují. Jakmile je tato větev identifikována, uzel paralelně stáhne obsah bloků z několika spojení a poté ověří platnost každé transakce: formát, platnost skriptů (kromě `assumevalid=1`), částky a nepřítomnost dvojího výdeje. Při každé úspěšné kontrole je v databázi `chainstate/` aktualizován aktuální stav nevydaných mincí (sada UTXO): vydané výstupy jsou odstraněny, zatímco nové platné výstupy jsou přidány.



Naproti tomu Mempool vstupuje do hry pouze tehdy, když se blíží ke špičce řetězce: dokud se uzel opozdí, nemá žádné nevyřízené transakce, které by mohl uložit.



Jakmile je IBD dokončena, uzel přejde do své běžné fáze: ověřuje nové bloky při jejich zveřejnění, udržuje svůj Mempool s čekajícími transakcemi podle svých pravidel pro předávání, předává transakce a bloky a řídí případnou reorganizaci řetězce.



### AssumeValid



Bitcoin core obsahuje mechanismus navržený tak, aby se zkrátila doba potřebná k plnému zprovoznění uzlu, přičemž podstata principu autonomního ověřování zůstává zachována: AssumeValid.



Parametr `assumevalid` je založen na minulém referenčním bloku, jehož Hash je integrován do každé verze softwaru. Pokud uzel během IBD zjistí, že tento blok je skutečně na větvi s největším množstvím práce, může ignorovat ověřování skriptů pro všechny transakce před tímto bodem.



Všechna ostatní pravidla (struktura bloku, Proof of Work, limity velikosti, výše transakcí, UTXO atd.) zůstávají plně ověřena. Pouze výpočet skriptů před tímto referenčním blokem je ignorován. Přírůstek výkonu je u IBD značný, protože ověřování podpisů představuje hlavní část zátěže procesoru. Za tímto referenčním blokem se ověřování vrátí do normálního stavu.



Pomocí parametru `assumevalid=0` v souboru `Bitcoin.conf` si můžete vynutit úplné ověření všech skriptů vypnutím tohoto mechanismu za cenu mnohem delšího IBD.



### PředpokládejmeUTXO



`assumeutxo` je další existující parametr, ale na rozdíl od `assumevalid` není ve výchozím nastavení aktivován. Tento mechanismus umožňuje softwaru načíst snímek sady UTXO spolu s jejími metadaty a předběžně jej považovat za referenční stav po ověření, že hlavičky skutečně vedou ke Blockchain s největším množstvím práce.



Uzel se tak rychle zprovozní pro běžné použití (RPC, připojení peněženek atd.) a současně se na pozadí spustí kompletní ověřená rekonstrukce vlastní sady UTXO. Po dokončení této fáze je počáteční snímek nahrazen lokálně rekonstruovaným stavem. Tento přístup odděluje rychlé poskytování uzlů od úplného ověřování, aniž by tím bylo ohroženo druhé jmenované.



### Vzájemné zjišťování: Jak váš uzel najde síť Bitcoin?



Když se uzel spouští poprvé, nezná ještě žádné vrstevníky. Musí však v internetu najít jiné uzly Bitcoin, které si vyžádají hlavičky a poté bloky, aby mohl dokončit IBD. Pro navázání těchto spojení se Bitcoin core řídí logikou určování priorit.



![Image](assets/fr/096.webp)



Když se uzel restartuje poté, co již byl používán, jádro se nejprve pokusí znovu připojit k odchozím partnerům registrovaným před vypnutím, přičemž informace jsou uloženy v souboru `anchors.dat`. Poté vyhledá svou knihu IP Address **`peers.dat`**, která uchovává seznam dříve nalezených peerů, aby se k nim znovu připojil. Jedná se jednoduše o místní soubor, který je aktualizován a uchováván jádrem. Naproti tomu pro nový uzel, který byl právě spuštěn, jsou tyto 2 soubory prázdné, protože ještě nikdy nekomunikoval s jinými uzly Bitcoin.



V tomto případě se software dotazuje na _**DNS seed**_. Jedná se o [servery spravované uznávanými vývojáři ekosystému](https://github.com/Bitcoin/Bitcoin/blob/master/src/kernel/chainparams.cpp), které vracejí seznam IP adres předpokládaných aktivních uzlů. Tyto adresy umožňují novému uzlu navázat první spojení a vyžádat si potřebná data z IBD. Zde je seznam *zárodků DNS*, které jsou k dnešnímu dni (srpen 2025) aktivní:




- Pieter Wuille: `seed.Bitcoin.sipa.be.`
- Matt Corallo: `dnsseed.bluematt.me.`
- Luke Dashjr: `dnsseed.Bitcoin.dashjr-list-of-P2P-nodes.us.`
- Jonas Schnelli: `seed.Bitcoin.jonasschnelli.ch.`
- Peter Todd: `seed.btc.petertodd.net.`
- Sjors Provoost: `seed.Bitcoin.sprovoost.nl.`
- Stephan Oeste: `dnsseed.emzy.de.`
- Jason Maurice: `seed.Bitcoin.wiz.biz.`
- Ava Chow: `seed.Mainnet.achownodes.xyz.`



V naprosté většině případů postačí k navázání prvních spojení s ostatními uzly krok *DNS seeds*. Pokud tyto servery výjimečně neodpoví do 60 sekund, uzel přejde na jinou metodu: [statický seznam více než 1 000 adres](https://github.com/Bitcoin/Bitcoin/blob/master/src/chainparamsseeds.h) _seed uzlů_ je zabudován do kódu Bitcoin core a je pravidelně aktualizován. Pokud první dva způsoby získání IP adres selžou, toto poslední řešení vytvoří počáteční spojení, ze kterého si pak uzel může vyžádat nové IP adresy.



![Image](assets/fr/097.webp)



V krajním případě můžete pomocí souboru `peers.dat` ručně vynutit konkrétní připojení pomocí IP adres Supply.



Po spuštění interní správce Address diverzifikuje zdroje (samostatné autonomní sítě, clearnet a Tor a různé geografické oblasti), aby se snížilo riziko topologické izolace. Uzel navazuje tato odchozí spojení (spojení, která si sám vybírá, a která jsou proto bezpečnější).



Pokud váš uzel naslouchá na otevřeném portu (ve výchozím nastavení 8333), přijímá příchozí připojení. Ty posilují celkovou odolnost sítě tím, že poskytují kontaktní místo pro nové uzly, aniž by přinášely nějaký zvláštní užitek vašemu vlastnímu IBD. Pokud váš uzel běží na síti Tor, logika zůstává stejná, ale používané adresy jsou služby `.onion`.




## Anatomie uzlu Bitcoin


<chapterId>b420bd9d-7e2a-4984-bc70-2b732a94c8ce</chapterId>



Po dokončení počáteční synchronizace uzel lokálně uloží několik doplňkových datových sad, což mu umožní ověřovat bloky a transakce, obsluhovat síťové partnery a rychle restartovat systém při zachování jeho stavu. v uzlu jsou nezbytné 3 hlavní cihly:




- gW-402 **bloky** uložené na disku,
- sada **UTXO** vedená v databázi klíč-hodnota,
- a **Mempool** se ukládá do paměti RAM a pravidelně se serializuje.



Kromě toho je doplňuje několik pomocných souborů (vrstevníci, odhady poplatků, seznamy vyloučených osob, peněženky atd.). Pojďme zjistit, jakou roli všechny tyto soubory hrají.



### Kde jsou data uzlu skutečně umístěna?



Ve výchozím nastavení ukládá Bitcoin core svá data do určitého pracovního adresáře. V systému GNU/Linux je to obvykle adresář `~/.Bitcoin/`, v systému Windows adresář `%APPDATA%\Bitcoin/` a v systému MacOS adresář `~/Library/Application Support/Bitcoin/`. Pokud používáte balíčkové řešení (např. v rámci distribuce uzlů), může být tento adresář připojen jinde, ale jeho struktura zůstává stejná. Důležité podsložky a soubory popsané níže jsou stále umístěny zde.



![Image](assets/fr/098.webp)



### Bloky



Blockchain je tedy soubor bloků. Full node ukládá tyto bloky jako sekvenční ploché soubory a udržuje paralelní index pro rychlé vyhledávání. V případě potřeby (reorganizace, opětovné skenování Wallet, peer servis) jsou tato data znovu načtena tak, jak jsou.



**Poznámka:** Reorganizace neboli resynchronizace je jev, při kterém dochází k modifikaci struktury Blockchain v důsledku existence konkurenčních bloků ve stejné výšce. K tomu dochází, když je část bloku Blockchain nahrazena jiným řetězcem s větším množstvím nahromaděné práce. Tyto resynchronizace jsou přirozenou součástí fungování řetězce Bitcoin. Různí těžaři v něm mohou nacházet nové bloky téměř současně, čímž dochází k rozdělení sítě Bitcoin na dvě části. V takových případech se síť může dočasně rozdělit na konkurenční řetězce. Nakonec, když jeden z těchto řetězců nahromadí více práce, uzly ostatní řetězce opustí a jejich bloky se stanou známými jako "zastaralé bloky" nebo "osiřelé bloky" Tento proces nahrazení jednoho řetězce jiným se nazývá resynchronizace.



#### Soubory Blk*.dat (nezpracovaná bloková data)



Přijaté a ověřené bloky se zapisují do sekvenčních kontejnerů s názvem `blkNNNNN.dat`, uložených ve složce `blocks/`. Každý soubor se plní postupně, dokud nedosáhne maximální velikosti 128 MiB, načež jádro otevře další soubor. Uvnitř je každý blok serializován v síťovém formátu, kterému předchází magický identifikátor a délka. Tato organizace umožňuje rychlý zápis na disk a usnadňuje blokovou službu pro synchronizaci vrstevníků.



![Image](assets/fr/099.webp)



V režimu pruned uzel uchovává pouze poslední okno těchto souborů, aby omezil diskovou stopu. Odstraní nejstarší kontejnery `blk*.dat`, jakmile je dosaženo nakonfigurovaného cílového prostoru, přičemž zachová dostatečnou historii, aby zůstal konzistentní s nejznámějším řetězcem. Index a sada UTXO zůstávají normální, což umožňuje ověřování dalších transakcí a bloků.



#### Soubory Rev*.dat (údaje o zrušení)



Aby bylo možné se během reorganizace vrátit v čase, ukládá jádro souběžně s každým souborem `blk` soubor `revNNNNN.dat` do složky `blocks/`. Tento soubor obsahuje informace potřebné ke zrušení účinku bloku na sadu UTXO: pro každý výstup spotřebovaný blokem je uložen předchozí stav příslušného UTXO (množství, skript, výška...). V případě přerušení bloku může uzel rychle obnovit předchozí stav, aniž by musel znovu skenovat celý řetězec.



![Image](assets/fr/100.webp)



#### Index bloku (bloky/index)



Vyhledávání bloku přímo v plochých souborech by bylo příliš časově náročné. Jádro proto udržuje databázi LevelDB v adresáři `blocks/index/`, která pro každý známý blok uvádí metadata, jako je Hash, výška, stav validace, soubor `blk` a offset, kde se nachází. Když partner požádá o blok nebo když interní komponenta potřebuje získat přístup k určitému bloku, tento index poskytuje rychlý přístup. Bez tohoto indexu by bylo nutné provádět příliš mnoho operací.



![Image](assets/fr/101.webp)



#### Volitelné indexy (indexy/)



Některé indexy jsou volitelné a ve výchozím nastavení jsou zakázány, protože zvyšují diskovou stopu:




- `indexes/txindex/`, o kterém jsme se již zmínili, poskytuje tabulku mapování transakce → umístění, která umožňuje načíst jakoukoli potvrzenou transakci bez znalosti bloku, který ji obsahuje. To je užitečné pro dotazy mimo Wallet `getrawtransaction` typu RPC, ale je to poměrně drahé.
- indexes/blockfilter/`, který může obsahovat kompaktní blokové filtry (BIP157/158) pro tenké klienty. Tyto struktury urychlují ověřování na straně klienta na úkor dalšího úložiště v uzlu indexeru.



### Sada UTXO (řetězový stav)



Model UTXO (*Nevyčerpaný výstup transakce*) je účetní reprezentací modelu Bitcoin: každý nevyčerpaný výstup je dostupný "Coin", který lze použít jako vstup pro budoucí transakci.



![Image](assets/fr/102.webp)



Souhrn všech těchto dílů v daném okamžiku T tvoří sadu UTXO: rozsáhlý seznam všech dílů, které jsou nyní k dispozici. Právě tento stav konzultuje uzel při rozhodování, zda transakce utratí legitimní jednotky, které ještě nebyly použity v předchozí transakci (aby se vyhnul Double-spending).



![Image](assets/fr/103.webp)



Sada UTXO je uložena ve složce `chainstate/` jako kompaktní databáze LevelDB. Každá část spojuje klíč odvozený od Hash transakce a výstupního indexu s hodnotou obsahující: částku, zámek `scriptPubKey`, výšku bloku vytvoření a indikátor coinbase.



![Image](assets/fr/104.webp)



Uzel udržuje paměť cache nad úrovní LevelDB, která absorbuje časté operace čtení a zápisu. Parametr `dbcache` lze použít k úpravě velikosti této mezipaměti: čím je větší, tím větší výhody má přístup do paměti IBD a aktuální validace, ovšem za cenu vyšší spotřeby paměti RAM. Když uzel Miner nalezne nový blok, odstraní ze sady UTXO výstupy spotřebované (nebo spotřebované) transakcemi obsaženými v bloku a přidá nově vytvořené výstupy.



Teoreticky bychom mohli transakci ověřit tak, že bychom znovu prohledali historii bloků a zkontrolovali, že výstup nebyl nikdy utracen. V praxi by to však bylo příliš časově náročné, protože pro každou novou transakci by se musel skenovat celý blok Blockchain. Sada UTXO proto poskytuje minimální zobrazení potřebné k tomu, aby bylo možné na místě a v přiměřeném čase prokázat neexistenci Double-spending.



Všimněte si, že sada UTXO je často jádrem obav z decentralizace Bitcoin, protože její velikost přirozeně rychle roste. To je částečně způsobeno rostoucí cenou Bitcoin, která podporuje fragmentaci dílů, a částečně rostoucím přijetím systému: čím více uživatelů, tím větší poptávka po UTXO.



![Image](assets/fr/105.webp)



Růst souboru UTXO vychází také ze struktury jednoduchých platebních transakcí na Bitcoin. Při platbě totiž spotřebováváte jeden UTXO jako vstup a vytváříte 2 nové UTXO jako výstup (jeden pro platbu a druhý pro Exchange). A konečně, heuristika analýzy řetězce, nazývaná CIOH (*Common Input Ownership Heuristic*), poskytuje další podnět k tomu, aby se zabránilo konsolidaci Coin.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Vzhledem k tomu, že část z nich musí být uchovávána v paměti RAM, aby bylo možné ověřit transakce v přiměřeném čase, může sada UTXO postupně způsobit, že provoz Full node bude příliš nákladný. K řešení tohoto problému již existuje několik návrhů, zejména [Utreexo](https://planb.network/resources/glossary/utreexo).



### Mempool



Mempool je místní soubor platných transakcí, které byly přijaty, ale ještě nebyly potvrzeny. Připomínáme, že "potvrzená transakce" je transakce, která byla zařazena do platného bloku. Každý uzel si udržuje svůj vlastní Mempool, který se může lišit od Mempool ostatních uzlů v síti v závislosti na:




- velikost přidělená Mempool pomocí parametru `maxmempool`: uzel s větším Mempool bude schopen pojmout více transakcí než uzel s menším Mempool (pokud se tento nevyprázdní);
- pravidla gW-433: jsou podmnožinou pravidel přenosu uzlu a definují vlastnosti, které musí nepotvrzená transakce splňovat, aby byla přijata v Mempool;
- pronikání transakcí: v důsledku různých faktorů může být daná transakce distribuována do jedné části sítě, ale do jiné ještě nedorazila.



Je důležité poznamenat, že mempooly uzlů nemají žádnou konsenzuální hodnotu. Bitcoin funguje bezchybně, i když má každý uzel jiný Mempool. Autoritativní jsou nakonec vždy bloky přidané do Blockchain. Například i když uzel zpočátku odmítne danou transakci ve svém Mempool (platném podle pravidel konsensu), bude ji muset přijmout, pokud bude nakonec zařazena do bloku s platným Proof of Work. Pokud by tak neučinil a tento blok odmítl, přestože by byl v souladu s pravidly konsensu, vyvolal by Hard Fork, tj. vytvoření nového, samostatného Bitcoin, na kterém by byl sám.



#### Politika a správa paměti



Po přijetí transakce provede jádro řadu kontrol podle pravidel konsensu (syntaxe, platné skripty, žádné dvojí výdaje atd.) a pravidel Mempool, která jsou místní politikou (RBF, minimální hranice poplatků, datový limit v `OP_RETURN` atd.). Pokud transakce tato pravidla dodržuje, je uložena do paměti.



Velikost paměti Mempool je omezena parametrem `maxmempool` v souboru `Bitcoin.conf` (více v další kapitole). Ve výchozím nastavení je limit 300 MB. Když je plný, uzel dynamicky zvýší práh minimálního poplatku a nejprve vyloučí nejméně ziskové transakce (tj. ponechá si transakce, které by měly být vytěženy jako první). Příliš staré transakce mohou také po nastavené prodlevě vypršet.



#### Persistence Mempool na disku



Pro urychlení restartů jádro při vypínání uzlu pravidelně serializuje stav Mempool do souboru `Mempool.dat`. Kromě skutečného stavu Mempool, který zůstává v paměti, ukládá jádro tento soubor `Mempool.dat` na disk. Při příštím spuštění uzlu tento snímek znovu načte a odstraní vše, co již není platné pro aktuální Blockchain.



### Pomocné soubory a databáze



Na správném fungování se podílí několik dalších souborů na stejné úrovni jako `blocks/`, `chainstate/` a `indexes/`:




- soubor `peers.dat` uchovává knihu IP Address potenciálních partnerů, která je založena na počátečním zjišťování DNS, síťových výměnách a ručním přidávání. Při spuštění může uzel čerpat z tohoto souboru při navazování odchozích spojení.
- Když je uzel vypnutý, soubor `anchors.dat` uloží adresy odchozích partnerů, abyste se s nimi mohli při příštím spuštění znovu rychle spojit.
- `banlist.json` obsahuje lokální zákazy, o kterých rozhodl operátor nebo uzel (opakované neplatné chování), aby se uzlu zabránilo v opětovném připojení nebo přijímání připojení od těchto konkrétních peerů.
- v souboru `fee_estimates.dat` jsou uloženy statistiky pozorovaných potvrzení v časovém horizontu, které odhadce poplatků používá k navrhování sazeb poplatků v souladu s cíli zpoždění zvolenými při vytváření transakce.
- gW-446.conf` obsahuje konfigurační parametry uzlu. Zde můžete upravit pravidla přenosu. Více se o tom dozvíte v další kapitole.
- `settings.json` obsahuje další parametry souboru `Bitcoin.conf`.
- `debug.log` je diagnostický textový protokol, který lze použít k pochopení činnosti uzlu v případě chyby.
- gW-448.pid` ukládá identifikátor procesu za běhu, což umožňuje jiným aplikacím nebo skriptům snadno identifikovat bitcoind (*Bitcoin daemon*) a v případě potřeby s ním komunikovat. Vytváří se při spuštění uzlu a odstraňuje se při vypnutí.
- `ip_asn.map` je mapovací tabulka IP → ASN (samostatný systém) používaná pro bucketing a diverzifikaci peerů (volba `-asmap`).
- `onion_v3_private_key` ukládá soukromý klíč služby Tor v3, když je povolena volba `-listenonion`, aby bylo možné udržet stabilní cibuli Address mezi restarty.
- `i2p_private_key` ukládá soukromý klíč I2P, pokud je použito `-i2psam=`, k navázání odchozích a případně i příchozích spojení na I2P.
- `.cookie` obsahuje efemérní ověřování RPC token (vytvoří se při spuštění, odstraní se při vypnutí), pokud se používá ověřování pomocí cookie. To lze použít například pro připojení softwaru Wallet.
- `.lock` je zámek datového adresáře, který zabraňuje současnému zápisu více instancí do stejného datového adresáře.
- `guisettings.ini.bak` je automatické uložení nastavení grafického uživatelského rozhraní (*Bitcoin Qt*) při použití volby `-resetguisettings`.



Jak jsme viděli v prvních částech tohoto kurzu BTC 202, Bitcoin core je jak software uzlu Bitcoin, tak Wallet. Není to však nutně řešení, které bych doporučil pro správu peněženek, protože jeho Interface zůstává základní a jeho funkce jsou omezené ve srovnání s moderním softwarem, jako je Sparrow nebo Liana. Jádro obsahuje také soubory pro správu peněženek:





- `wallets/` je výchozí adresář, který hostí jeden nebo více adresářů;
- `wallets/<název>/Wallet.dat` je databáze SQLite Wallet (klíče, deskriptory, metadata transakcí atd.);
- wallets/<name>/Wallet.dat-journal` je protokol SQLite rollback.



Stručně shrnuto, zde je struktura souboru Bitcoin core:



```
~/.bitcoin/
├── bitcoin.conf
├── blocks/
│   ├── blk00000.dat
│   ├── blk00001.dat
│   ├── rev00000.dat
│   ├── rev00001.dat
│   └── index/
├── chainstate/
├── indexes/
│   ├── txindex/
│   ├── blockfilter/
│   │   └── basic/
│   │       ├── db/
│   │       └── fltrNNNNN.dat
│   └── coinstats/
│       └── db/
├── wallets/
│   └── <wallet_name>/
│       ├── wallet.dat
│       └── wallet.dat-journal
├── peers.dat
├── anchors.dat
├── banlist.json
├── mempool.dat
├── fee_estimates.dat
├── bitcoind.pid
├── debug.log
├── ip_asn.map
├── onion_v3_private_key
├── i2p_private_key
├── settings.json
├── guisettings.ini.bak
├── .cookie
└── .lock
```



### Cesta ověření nového bloku



Po přijetí nového bloku váš uzel zkontroluje Proof of Work a obecněji soulad s pravidly konsensu. Pokud je vše v pořádku, aplikuje změny transakci po transakci na svou sadu UTXO: zkontroluje, zda každá položka utrácí existující UTXO s platným skriptem, odstraní tyto UTXO a přidá nové výstupy. Pokud je vše platné, jsou změny zapsány do `chainstate/`.



Souběžně jsou data o zrušení zápisu zapisována do souboru `rev*.dat` a metadata do indexu `blocks/index/`. Blok je poté serializován do správného souboru `blk*.dat`. V případě reorganizace uzel zpětně načte soubor `rev*.dat`, aby čistě odpojil opuštěné bloky, obnovil sadu UTXO a poté připojil bloky nového nejlepšího řetězce.





## Porozumění souboru Bitcoin.conf


<chapterId>c54a629a-ddb1-41cb-9a88-21dfd9be50ca</chapterId>



Soubor `Bitcoin.conf` je hlavní konfigurační soubor Interface pro Bitcoin core. Umožňuje upravit chování a parametry uzlu, aniž byste museli překompilovat jeho zdrojový kód nebo provádět úpravy příkazového řádku. Konkrétně se jedná o textový soubor strukturovaný do dvojic klíč-hodnota, což znamená, že každý řádek souboru odkazuje na konkrétní parametr (klíč) a k němu přiřazenou hodnotu, kterou lze upravit tak, aby se daný parametr upravil.



Síťové parametry, parametry přenosu transakcí, výkonu, indexování, protokolování a přístupu ke RPC lze definovat v souboru `Bitcoin.conf`. Tento konfigurační soubor však nikdy nemění pravidla konsensu protokolu: nastavuje pouze lokální politiku uzlu (pravidla předávání), způsob připojení, indexování a vystavování služeb.



### Umístění a priorita



Ve výchozím nastavení se soubor `Bitcoin.conf` nachází v datovém adresáři Bitcoin core. Jedná se o známý adresář, o kterém jsme se zmínili v předchozí kapitole. Tento soubor však není automaticky vytvářen systémem Bitcoin core, s výjimkou určitých prostředí, jako je například Umbrel. Pokud ještě neexistuje, budete si ho muset vytvořit sami generate jednoduše tak, že vytvoříte soubor s názvem `Bitcoin.conf` a poté ho otevřete v textovém editoru a provedete v něm úpravy.



Parametry definované v souboru `Bitcoin.conf` lze přepsat pomocí 2 vrstev:




- `settings.json` (dynamicky zapsaný grafikou Interface nebo některým RPC),
- a možností upravených pomocí příkazových řádků.



Všimněte si, že jakákoli změna souboru `Bitcoin.conf` vyžaduje restart uzlu, aby se projevila.



### Formát a struktura



Formát souboru `Bitcoin.conf` je proto velmi jednoduchý: jedna řádka pro každou volbu ve tvaru `volba=hodnota`. Nepotřebné mezery a prázdné řádky jsou ignorovány a komentáře kódu začínají znakem `#`.



Téměř všechny logické volby lze zakázat pomocí předpony `no`. Například `listen=0` a `nolisten=1` jsou v závislosti na verzi ekvivalentní.



Chcete-li rozdělit konfiguraci podle sítí, můžete použít sekce: `[main]`, `[test]` (testnet3), `[testnet4]`, `[bookmark]`, `[regtest]`. Případně můžete před název volby vložit předponu `regtest.maxmempool=100`.



### Co soubor Bitcoin.conf umí a co neumí



Jak bylo vysvětleno výše, pravidla konsensu samozřejmě nelze konfigurovat v souboru `Bitcoin.conf`, protože by to mohlo vést k vytvoření Hard Fork. Na druhou stranu mnoho dalších aspektů konfigurovatelných je. Existují 3 užitečné třídy, které je třeba mít na paměti:




- Čistě lokální parametry. Ty ovlivňují pouze váš uzel: velikost cache (`dbcache`), režim pruned (`prune`), volitelné indexy... Ovlivňují výkon vašeho počítače, ale ne sítě.
- Zásady pro relé a Mempool. Ty rozhodují o tom, co váš uzel přijme, uchová a předá před potvrzením: minimální práh poplatků (`minrelaytxfee`), velikost a doba uchovávání Mempool (`maxmempool`, `mempoolexpiry`), nahrazování transakcí (RBF)... Tato pravidla nejsou součástí konsensu, takže dva různé uzly mohou mít různé zásady a přesto budou plně kompatibilní. Na druhou stranu tyto parametry budou mít vliv na síť Bitcoin (jak bylo vysvětleno v první části, zejména pomocí teorie perkolace).
- Síťové připojení. Tyto možnosti určují, jak uzel vyhledává partnery, naslouchá, překonává NAT, používá Tor nebo proxy server nebo omezuje šířku pásma. Utvářejí vaši topologii, ale nemění přenos transakcí.



Pochopení tohoto oddělení je klíčové: pokud transakce nedodržuje pravidla konsensu, váš uzel ji v každém případě odmítne. Přísnější místní pravidla však mohou odmítnout předat transakci, která je platná ve smyslu konsensu.



### Síť a topologie



Především je důležité jasně rozlišovat mezi dvěma typy připojení, které může mít uzel Bitcoin:




- Odchozí spojení, která jsou iniciována naším uzlem do jiného uzlu;



![Image](assets/fr/106.webp)





- Příchozí spojení iniciovaná jiným uzlem k našemu uzlu.



![Image](assets/fr/107.webp)



Tyto dva typy připojení jsou schopny vyměňovat si stejná data v obou směrech; nejde o omezení směru toku, ale pouze o rozdíl v iniciátorovi připojení. Z pohledu našeho uzlu jsou odchozí spojení obecně považována za bezpečnější, protože je iniciujeme my a přesně si vybíráme, ke kterému uzlu se připojíme, takže je nepravděpodobné, že by spojení bylo škodlivé. Ve výchozím nastavení udržuje Bitcoin core 10 odchozích spojení (8 "*full-relay*" + 2 "*block-relay-only*").



Zařízení Full node přidává do sítě další hodnotu tím, že přijímá příchozí připojení. Parametr `listen=1` umožňuje naslouchání na výchozím portu 8333 dané sítě, což umožňuje přijímat tato příchozí spojení v síti clearnet. Aby tato funkce fungovala, musí být tento port otevřen také na vašem směrovači. Pokud tomu tak není, bude váš uzel nadále pracovat pouze s odchozími spojeními, což nebude mít žádný vliv na vaše osobní používání Bitcoin. Volba, zda povolit příchozí připojení, je na vás; neexistuje žádná "nejlepší volba"



Pokud nechcete na svém směrovači otevírat port, ale přesto přijímat příchozí připojení, můžete aktivovat parametr `listenonion=1`. Tím dosáhnete stejného výsledku, ale pouze prostřednictvím sítě Tor, nikoliv sítě Clearnet.



Na úrovni sítě máme také:




- `addnode`: přidá přátelského partnera ke kontaktu navíc k obvyklému zjišťování (lze zadat několikrát).
- connect`: striktně omezuje připojení na poskytnutý server Address (lze zadat několikrát). Jádro se nepřipojí k žádnému jinému uzlu.
- `seednode`: slouží pouze k vyplnění knihy-Address při připojení k uzlu, poté se odpojí.
- `maxconnections`: definuje globální strop pro příchozí + odchozí spojení. Ve výchozím nastavení je tento parametr nastaven na 125, což znamená, že váš uzel nikdy nepřijme více než 125 spojení.
- maxuploadtarget`: omezuje nahrávání na šířku pásma v klouzavém 24hodinovém okně. Tento limit neobětuje šíření zásadních nedávných Elements.
- `onlynet`: omezuje odchozí připojení pouze na vybrané sítě (`ipv4`, `ipv6`, `onion`, `i2p`, `cjdns`). Pokud například chcete, aby se váš uzel připojoval k síti Bitcoin pouze přes Tor, můžete povolit parametr `onlynet=onion` a zakázat příchozí připojení (nebo povolit připojení také pouze přes Tor).
- `dnsseed`: povoluje nebo zakazuje _DNS seed_ vyžádat si peery, když je váš místní fond Address nízký (výchozí: `1`, pokud `-connect` nebo `-maxconnections=0`).
- `forcednsseed`: vynucuje vyžádání _DNS seed_ při spuštění, i když již máte adresy na skladě (výchozí: `0`).
- `fixedseeds`: (seznam Address), pokud _DNS seeds_ selžou nebo jsou zakázány (výchozí: `1`).
- `dns`: Autorizuje DNS rezoluce obecně (např. pro `-addnode`/`-seednode`/`-connect`).



Ve výchozím nastavení váš uzel komunikuje přes sítě Clearnet, Tor a I2P. To znamená, že peeři, se kterými se spojuje v síti clearnet, vidí vaši veřejnou IP adresu Address a poskytovatel internetu pravděpodobně zjistí, že používáte uzel Bitcoin (ačkoli díky P2P Transport V2 je pro poskytovatele internetu obtížnější odposlouchávat). To nemusí nutně představovat problém, ale pokud se chcete vyhnout úniku těchto informací, můžete svůj uzel připojit výhradně prostřednictvím sítě Tor.



Chcete-li plně podporovat Tor, musíte Bitcoin core přinutit používat pouze tuto síť a vytvořit skrytou službu pro příchozí připojení (pokud je chcete povolit). Do souboru `Bitcoin.conf` je třeba přidat tuto konfiguraci:




- `onlynet=onion`,
- `proxy=127.0.0.1:9050`,
- `listenonion=1`,
- `torcontrol=127.0.0.1:9051`,
- `proxyrandomize=1`,
- `listen=1`,
- bind=127.0.0.1`,
- `upnp=0`,
- `natpmp=0`.



Všechna připojení P2P probíhají přes Tor. Váš uzel obdrží pro příchozí spojení `.onion` Address, takže na routeru není třeba otevírat žádné porty. Váš poskytovatel internetu vidí pouze provoz přes Tor a vaši kolegové neznají vaši skutečnou veřejnou IP adresu Address.



Chcete-li se vyhnout překladu DNS v otevřeném režimu, můžete do konfigurace přidat `dnsseed=0` a `dns=0`. Poté budete muset ručně poskytnout `.onion` peery prostřednictvím `seednode=` nebo `addnode=`, protože jinak bude zjišťování nových uzlů obtížné.



Pokud jste začátečník, doporučuji vám, abyste všechna tato síťová nastavení prozatím nechali být. Výchozí konfigurace je často dostačující.



### Mempool a zásady předávání



#### Základní parametry



Zde jsou uvedeny základní parametry, které můžete upravit v souboru `Bitcoin.conf` a které se týkají správy vašeho Mempool a předávání nepotvrzených transakcí:





- `maxmempool=<n>`: (výchozí: `300`): Omezí maximální velikost místního Mempool na `<n>` megabajtů (výchozí: `300`). Po dosažení limitu uzel dynamicky zvýší svůj efektivní práh poplatků a upřednostní nejméně ziskové transakce (na základě sazby poplatků, nikoli absolutní hodnoty), aby zůstaly pod limitem. Toto nastavení můžete ponechat jako výchozí. Jeho zvýšení může být užitečné, pokud jste Mining sólo, nebo pokud chcete získat přesnější přehled o přetížení Mempool a zlepšit odhad poplatků. Naopak jeho snížením ušetříte paměť RAM a v menší míře i další systémové prostředky.





- `mempoolexpiry=<n>`: Maximální doba uchovávání nepotvrzených transakcí v Mempool (v hodinách, výchozí: `336`). Po uplynutí této doby jsou transakce odstraněny, i když zůstává volné místo.





- `persistmempool=1`: (výchozí: `1`). To urychluje obnovu po restartu a zamezuje nutnosti opětovného učení stavu přes síť.





- `maxorphantx=<n>`: Maximální počet ponechaných osiřelých transakcí (závislé vstupy z UTXO, které ještě nebyly viděny v sadě UTXO, výchozí: `100`). Po překročení této prahové hodnoty jsou nejstarší transakce smazány, aby se zabránilo nekontrolovanému růstu mezipaměti.





- bloky=1`: Zakáže přijímání a opakované zasílání nepotvrzených transakcí přijatých od partnerů (pokud nejsou udělena zvláštní oprávnění). Uzel nyní odesílá a inzeruje pouze bloky. Transakce vytvořené lokálně lze stále vysílat (pro použití uzlu se softwarem Wallet). To výrazně snižuje nároky na šířku pásma a paměť RAM, i když za cenu menší užitečnosti pro relay a naprosté neznalosti Mempool.





- `minrelaytxfee=<n>`: Minimální sazba poplatku (v BTC/kvB), pod kterou nejsou transakce v uzlu Mempool přijímány a nejsou předávány peerům (výchozí: `0,00001` = 1 sat/vB). Čím vyšší je tato hodnota, tím agresivněji váš uzel filtruje nízkonákladové transakce.





- `mempoolfullrbf=1`: Přijímat transakce RBF i bez explicitní signalizace RBF v nahrazované transakci. S touto politikou "*full-RBF*" může transakce nabízející vyšší sazbu poplatku nahradit jinou transakci v Mempool, pokud jsou splněny ostatní podmínky nahrazení.



Připomínáme, že RBF je transakční mechanismus, který umožňuje odesílateli nahradit transakci transakcí s vyššími poplatky, aby se urychlilo potvrzení. Pokud transakce s příliš nízkým poplatkem zůstane zablokovaná, může odesílatel použít *Replace-by-fee* ke zvýšení poplatku a upřednostnění své náhradní transakce v mempoolech a u těžařů.



#### Pokročilá a specifická nastavení



Zde jsou uvedena pokročilá nastavení pro Mempool a zásady přenosu. Pokud jste začátečník, neměli byste tato nastavení upravovat:





- datacarrier=1`: Umožňuje předávání a (v případě Mining přes uzel) zahrnutí transakcí nesoucích nefinanční data prostřednictvím výstupu `OP_RETURN` (výchozí: `1`). Deaktivace tohoto parametru mírně zmenšuje plochu pro spam nefinančních dat za cenu snížené kompatibility s některými způsoby použití. Ve všech případech je nutné akceptovat vytěžené `OP_RETURN`.





- `datacarriersize=<n>`: Maximální velikost (v bajtech) `OP_RETURN`, kterou uzel předává (výchozí: `83`). Snížením této hodnoty se omezí užitečné zatížení přenášené prostřednictvím `OP_RETURN`. Všimněte si, že tento limit bude ve výchozím nastavení odstraněn v některé z budoucích verzí Bitcoin core.





- `bytespersigop=<n>`: Parametr, který převádí podpisové transakce na ekvivalentní bajty pro vyhodnocení limitu relé (výchozí: `20`). To ovlivní přijímání transakcí bohatých na `sigops` podle pravidel místní politiky.





- `permitbaremultisig=1`: (výchozí: `1`). Jedná se o nejstarší šablonu skriptu pro stanovení podmínek pro více podpisů na UTXO (vynalezl ji v roce 2011 Gavin Andresen).





- `whitelistrelay=1`: Automaticky uděluje oprávnění k relay příchozím peerům na whitelistu (výchozí: `1`). Tito peeři mají své transakce přijaty relay, i když váš uzel není v obecném režimu relay.





- `whitelistforcerelay=1`: Přiřadí oprávnění "*forcerelay*" peerům na bílé listině s výchozími oprávněními (výchozí: `0`). Uzel pak předává jejich transakce, i když jsou již přítomny v Mempool, čímž obchází mechanismy proti redundanci.





- `whitebind=<[permissions@]addr>` / `whitelist=<[permissions@]CIDR>`: Váže rozsah Interface nebo Address a přiřazuje odpovídajícím peerům jemně rozlišená oprávnění: `relay`, `forcerelay`, `Mempool` (požadavek na obsah Mempool), `noban`, `download`, `addr`, `bloomfilter`. To může být užitečné při udělování privilegovaného zacházení důvěryhodným partnerům (například bránám, LAN a interním službám).





- peerbloomfilters=1`: (výchozí: `0`). Upozornění: Tím se zvýší zatížení zdrojů.





- peerblockfilters=1`: (*Neutrino*) kompaktní filtry pro peery (výchozí: `0`).





- `blockreconstructionextratxn=<n>`: Dodatečný počet transakcí uchovávaných v paměti pro obnovu kompaktních bloků (výchozí: `100`). Zlepšuje úspěšnost rekonstrukcí při kompaktních synchronizacích za cenu malého množství paměti.



Připomínáme, že všechna tato pravidla relay nemají žádný vliv na platnost transakcí zahrnutých do platného bloku. Slouží k úpravě vašeho příspěvku do relay, ochraně vašich zdrojů a předvídatelnosti vašeho uzlu v omezeném prostředí, ale nikdy vám neumožňují odmítnout bloky, které respektují pravidla konsensu.



### Peněženky



Způsob správy peněženek můžete také upravit v souboru `Bitcoin.conf`. Pokud nepoužíváte Wallet přímo v jádře, ale spíše externí software pro správu, jako je Sparrow nebo Liana, nebudou mít tyto parametry velký význam:





- addresstype=<legacy|P2SH-SegWit|bech32|bech32m>`: Definuje formát adres generovaných Wallet pro příjem.





- `changetype=<legacy|P2SH-SegWit|bech32|bech32m>`: Exchange Address (zbytek vstupu při jedné platbě).





- `Wallet=<cesta>`: Při spuštění načte existující Wallet (lze opakovat pro načtení více peněženek).





- `walletdir=<dir>`: (výchozí: `<datadir>/wallets`, pokud existuje, jinak `<datadir>`). To může být užitečné, pokud si přejete uložit peněženky na vyhrazený nebo šifrovaný svazek.





- `walletbroadcast=1`: Automaticky vysílá transakce vytvořené načtenými peněženkami (výchozí: `1`). Nastavte na `0`, pokud si přejete řídit vysílání jiným kanálem.





- `walletrbf=1`: (výchozí: `1`). Umožňuje pozdější zvýšení poplatků v případě zablokované transakce.





- `txconfirmtarget=<n>`: Cíl potvrzení transakce (v počtu bloků, výchozí: `6`). Wallet automaticky nastaví poplatek za potvrzení transakce do tohoto počtu bloků.





- `paytxfee=<amt>`: Pevná sazba poplatku (BTC/kvB) pro transakce Wallet. Vyhněte se obecně: použijte adaptivní odhad prostřednictvím `txconfirmtarget`.





- fallbackfee=<amt>`: (BTC/kvB) použitá v případě, že estimátoru dojdou data (výchozí: `0,00`). Nastavení na 0 zcela vypne fallback.





- `mintxfee=<amt>`: Minimální práh (BTC/kvB) pro vytvoření transakce Wallet (výchozí: `0,00001`). Wallet odmítne vytvořit transakci pod touto prahovou hodnotou.





- `maxtxfee=<amt>`: (výchozí: `0,10` BTC). Chrání před abnormálně vysokými poplatky, které by zbytečně ničily bitcoiny.





- `avoidpartialspends=1`: Vybírá UTXO podle klastrů Address, aby se zabránilo částečným výdajům.





- `spendzeroconfchange=1`: UTXO Exchange může být znovu použit jako položka v nové transakci (výchozí: `1`).





- `consolidatefeerate=<amt>`: Maximální rychlost (BTC/kvB), při jejímž překročení se Wallet vyhne přidání více vstupů, než je nutné ke konsolidaci. To umožňuje oportunistické konsolidace za nízké ceny a snižuje náklady, když jsou náklady vysoké.





- `maxapsfee=<n>`: (BTC, absolutní hodnota), které Wallet souhlasí zaplatit za aktivaci možnosti "*vyhnout se částečným výdajům*".





- `discardfee=<amt>`: (BTC/kvB) udávající vaši toleranci k zahození Exchange přičtením k poplatku. Výstupy, které by při této sazbě stály více než třetinu své hodnoty, jsou zahozeny.





- `keypool=<n>`: (výchozí: `1000`). Příliš malé hodnoty zvyšují riziko neúplného obnovení.





- `disablewallet=1`: Spustí Bitcoin core bez subsystému Wallet a zakáže související RPC. Snižuje plochu útoku a stopu, pokud je uzel používán pouze pro ověřování/uvolňování.



### Ukládání, indexování a výkon



Konfigurační soubor také umožňuje upravit parametry týkající se vašeho počítače. To může být důležité zejména v případě, že máte omezené zdroje, nebo naopak velkou dostupnou kapacitu:





- `datadir=<dir>`: Nastaví hlavní datový adresář Bitcoin core.





- `blocksdir=<dir>`: Oddělí umístění souborů bloků (`blocks/blk*.dat` a `blocks/rev*.dat`) od `datadiru`. To může být užitečné například pro umístění archivu bloků na jiný svazek, zatímco stavová základna (`chainstate/`) zůstane na rychlejším médiu.





- `dbcache=<n>`: Přidělí `<n>` MiB do mezipaměti databáze (*LevelDB*), kterou používá blokový index a `chainstate` (výchozí: `450`). Čím vyšší hodnota, tím rychlejší IBD a aktuální validace za cenu vyšší spotřeby RAM.





- `prune=<n>`: (výchozí: `0` = vypnuto; `1` = ruční ořezávání prostřednictvím RPC; `>=550` = automatické ořezávání pod cílovou hodnotu). Nekompatibilní s `txindex=1`. Uzel zůstává plně validním uzlem, ale nemůže již poskytovat starou historii. Tato volba je obzvláště užitečná, pokud máte omezené místo na disku, například při instalaci uzlu na domácím počítači.





- txindex=1`: Vytváří a udržuje globální index potvrzených transakcí. Nezbytné pro některé dotazy (`getrawtransaction` non-Wallet) a pro účely průzkumu, ale výrazně zvyšuje diskovou stopu. Nekompatibilní s režimem pruned.





- `assumevalid=<hex>`: (nastavte `0` pro kontrolu všech bloků): Označuje blok, který je považován za platný, což umožňuje vynechat kontrolu skriptů pro jeho předky. Další informace naleznete v předchozí kapitole.





- `reindex=1`: Rekonstruuje indexy bloků a stav (`chainstate`) ze souborů `blk*.dat` na disku. Přestaví také volitelné aktivní indexy. Jedná se o časově náročnou operaci, kterou lze použít k opravě poškozené databáze nebo k čisté aktivaci/deaktivaci těžkých indexů.





- `reindex-chainstate=1`: Obnoví pouze `chainstate` z aktuálního indexu bloku. Preferováno, pokud jsou blokové soubory zdravé.





- `blockfilterindex=<type>`: Udržuje indexy kompaktních blokových filtrů (např. `basic`) používaných tenkými klienty (BIP157/158) a některými RPC. Ve výchozím nastavení zakázáno (`0`). Spotřebovává další místo na disku a čas na indexování.





- `coinstatsindex=1`: Udržuje index statistik sady UTXO, který je obsluhován voláním `gettxoutsetinfo`. Užitečné pro audity a metriky, protože eliminuje nutnost nákladného přepočítávání. Ve výchozím nastavení zakázáno.





- `loadblock=<file>`: Při spuštění importuje bloky z externího souboru `blk*.dat`. Používá se k přednačtení historie z offline zdroje (místní kopie, externí médium) pro urychlení inicializace.





- `par=<n>`: (od `-10` do `15`, `0` = automaticky, `<0` = ponechává tento počet jader volný). Umožňuje nastavit paralelizmus procesoru během ověřování. Automatický režim je vhodný ve většině případů.





- `debuglogfile=<soubor>`: Určuje umístění protokolu `debug.log`.





- `shrinkdebugfile=1`: (výchozí: `1`, když `-debug` není aktivní).





- `settings=<soubor>`: Cesta k souboru dynamických nastavení `settings.json`.



### RPC přístup a provozní bezpečnost



Soubor `Bitcoin.conf` také umožňuje konfigurovat přístupové parametry pro váš uzel. S těmito nastaveními buďte opatrní, zejména pokud s nimi teprve začínáte: vyhněte se jejich změnám bez důkladného pochopení důsledků, protože by to mohlo přinést zranitelnosti.





- `server=1`: Aktivuje server JSON-RPC. Nezbytné, pokud používáte `bitcoind` prostřednictvím `bitcoin-cli` nebo aplikace třetí strany. Zakázat (`0`) na čistě validačním uzlu, který nevystavuje žádné API nebo již používá server Electrum.





- `rpcbind=<addr>[:port]`: RPC server naslouchá Address/port. Ve výchozím nastavení se naslouchání provádí pouze lokálně (`127.0.0.1` a `::1`). Tento parametr je ignorován, pokud není definován také parametr `rpcallowip`. Použijte jej pro explicitní omezení Interface.





- `rpcport=<port>`: (výchozí: `8332` na Mainnet, `18332` na Testnet, `38332` na záložce, `18443` na regtestu).





- `rpcallowip=<ip|cidr>`: Povolí klienty RPC z dané IP nebo podsítě (lze opakovat). Použijte ve spojení s `rpcbind` pro zpřístupnění API pouze důvěryhodnému segmentu (LAN/VPN).





- `rpcauth=<USERNAME>:<SALT>$<Hash>`: Doporučená metoda ověřování RPC (hashované heslo). Umožňuje vícenásobné zadání a zabraňuje ukládání tajemství v otevřeném textu.





- `rpccookiefile=<cesta>`: Cesta k autentizačnímu souboru cookie (výchozí: soubor `.cookie` v adresáři `datadir/`). Používá se pro místní přístup stejného uživatele bez správy trvalých hesel. Můžete jej například použít pro připojení Liana Wallet ke svému Bitcoin core na stejném počítači.





- `rpcuser=<uživatel>` / `rpcpassword=<pw>`: Klasické ověřování RPC s heslem v prostém textu. Vyhněte se použití tohoto způsobu ve prospěch `rpcauth` nebo cookie.





- `rpcthreads=<n>`: Počet vláken pro obsluhu volání RPC (výchozí: `4`). Zvyšte jej, pokud máte vysoké špičky volání na straně monitorování/externího nástroje.





- `rpcwhitelist=<USERNAME>:<rpc1>,<rpc2>,...`: Whitelist autorizovaných API. Omezením přístupných metod snižuje plochu útoku.





- `rpcwhitelistdefault=1|0`: Pokud je povoleno a je použit whitelist, jsou odmítnuta volání bez seznamu. To může také vynutit výchozí prázdnou sadu (žádná volání nejsou povolena), pokud není nic explicitně uvedeno v seznamu.





- `rest=1`: (ve výchozím nastavení vypnuto). Má být vystaveno pouze v důvěryhodné síti (stejné upozornění jako u JSON-RPC).





- `conf=<soubor>`: V příkazovém řádku určuje konfigurační soubor pouze pro čtení. Užitečné pro zmrazení profilu provádění (neměnný) na straně operací.





- `includeconf=<soubor>`: Načte další konfigurační soubor (cesta relativní k `datadir/`). Umožňuje rozdělení rolí: společný základ + citlivé lokální přetížení.





- `daemon=1` / `daemonwait=1`: Spustí `bitcoind` na pozadí a s `daemonwait` počká na dokončení inicializace před předáním. To usnadňuje integraci se supervizory (systemd, runit).





- `pid=<soubor>`: Umístění souboru PID.





- `sandbox=<log-and-abort|abort>`: Povoluje experimentální sandboxing syscallů: povoleny jsou pouze očekávané syscally.





- `startupnotify=<cmd>` / `shutdownnotify=<cmd>`: Provede příkaz při spuštění nebo vypnutí.





- `alertnotify=<cmd>`: Spustí příkaz při přijetí upozornění.





- `blocknotify=<cmd>`: Provede příkaz pro každý nový blok.





- `debug=<category>|1` / `debugexclude=<category>`: Zapne/vypne podrobné kategorie logů (např. `net`, `Mempool`, `RPC`, `validace`...).





- `logips=1`: IP adresy.





- `logsourcelocations=1` / `logthreadnames=1` / `logtimestamps=1`: Přidá do logů umístění zdrojů, názvy vláken a přesné časové značky.





- `printtoconsole=1`: Odesílá stopy/chybová hlášení do konzole (*stdout*).





- `help-debug=1`: Zobrazí nápovědu k ladicí volbě a ukončí se.





- `uacomment=<cmt>`: Přidá komentář k User-Agent P2P.



Nyní jsme dokončili výpis většiny konfiguračních parametrů. Tento soubor `Bitcoin.conf` tak představuje skutečný řídicí panel vašeho uzlu: definuje konfiguraci sítě, správu Mempool, využití disku a paměti, indexování a obecnou správu. Pokud se chcete o tomto souboru dozvědět více a vytvořit si jej na míru svým potřebám, doporučuji použít [generátor Jamesona Loppa](https://jlopp.github.io/Bitcoin-core-config-generator/).



Dostali jsme se k závěru tohoto kurzu BTC 202, který vám umožní nejen pochopit základy fungování uzlů a jejich interakce v systému, ale také si založit vlastní. Nyní jste suverénním Bitcoinerem s vlastním samospádem Wallet, který vysílá své transakce prostřednictvím vlastního uzlu. Gratulujeme!



Nyní můžete přejít k závěrečné části kurzu, kde si budete moci vyhodnotit BTC 202 a poté si vyzvednout diplom, abyste si ověřili, že jste zvládli všechny probírané koncepty.



Nyní máte několik možností. Dalším logickým krokem je zřízení vlastního uzlu Lightning, který vám umožní být plně nezávislý na transakcích off-chain. To bude předmětem připravovaného kurzu, který bude zveřejněn na podzim tohoto roku 2025 na téma Plan ₿ Network.



Mezitím vás zvu na školení BTC 204, které vám umožní pochopit a osvojit si zásady ochrany soukromí při používání systému Bitcoin:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


# Závěrečná část


<partId>679169f5-b990-47e1-9a00-45098ba8096b</partId>





## Recenze a hodnocení


<chapterId>c18f672d-1074-427e-9505-eecd7ae43e71</chapterId>




<isCourseReview>true</isCourseReview>


## Závěrečná zkouška


<chapterId>a4c97701-996c-4cc5-81fa-37d2dc4ee856</chapterId>




<isCourseExam>true</isCourseExam>


## Závěr


<chapterId>28c5cf1f-7b9c-4b68-8b8f-eee109629764</chapterId>




<isCourseConclusion>true</isCourseConclusion>