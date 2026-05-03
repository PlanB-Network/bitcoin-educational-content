---
name: Nastavení prvního uzlu Lightning
goal: Pochopení, instalace, konfigurace a používání uzlu Lightning
objectives: 


  - Porozumět úloze a účelu uzlu Lightning.
  - Identifikujte různá dostupná softwarová řešení.
  - Nainstalujte a nakonfigurujte uzel Lightning (LND).
  - Připojení výdajového účtu.
  - Znáte rizika používání uzlu Lightning.


---

# Váš první krok k autonomii v systému Lightning



Již jste si pořídili svůj první uzel sats, zajistili si prostředky na vlastní úschovu a nasadili uzel Bitcoin, který bude suverénně využívat váš uzel on-chain. Dalším krokem je získat stejnou samostatnost v systému Lightning: právě to je cílem tohoto kurzu.



LNP202 je určen pro středně pokročilé uživatele a provede vás krok za krokem nasazením prvního uzlu Lightning, aniž byste museli mít pokročilé technické znalosti.



Dozvíte se, jak nainstalovat LND na Umbrel, otevřít a spravovat kanály, dohlížet na uzel a připojit mobilní wallet, abyste si mohli užívat zážitek srovnatelný se správcovským wallet a zároveň si zachovali plnou kontrolu nad svými prostředky.



+++


# Úvod


<partId>5e77c17a-0853-4f36-a988-1b4a956f49e4</partId>



## Přehled kurzů


<chapterId>e0871abf-af6d-4221-9389-1a996aea9b79</chapterId>



LNP202 je praktický kurz, jehož cílem je, abyste byli v systému Lightning samostatní a ovládali svůj vlastní uzel. Cíl je jednoduchý: začněte s již existujícím uzlem Bitcoin, nasaďte LND na Umbrel, řádně jej zabezpečte, otevřete a spravujte své první kanály a poté svůj uzel denně používejte z mobilního wallet. Tento kurz předpokládá, že jste již absolvovali kurz BTC 202, protože předpokládám, že váš uzel Bitcoin na Umbrel je na místě a synchronizovaný. Nebudeme se zde vracet k tomu, jak uzel Bitcoin nastavit.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

Pro lepší pochopení vnitřní mechaniky blesku doporučujeme také kurz LNP 201, který však není podmínkou pro tento kurz:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

V první části tohoto kurzu LNP202 se podíváme na to, co je to vlastně uzel Lightning, jak se liší od jednoduchého uzlu wallet a proč je provozování osobního uzlu jediným způsobem, jak používat Lightning bez delegování vašeho sats na důvěryhodnou třetí stranu. Tato část končí strategickou volbou: které řešení je pro vás to pravé, od nejjednodušších přístupů až po klasický uzel Lightning, který budeme v tomto kurzu implementovat.



Ve 2. části kurzu nainstalujete LND na Umbrel a poté zavedete prvky, které zabrání nejnákladnějším chybám: realistickou strategii zálohování a ochranu proti podvádění pomocí strážní věže. Jakmile budou tyto základy zavedeny, otevřete si svůj první kanál, abyste mohli začít platit na Lightning s vlastní infrastrukturou.



Jak vidíte: v tomto kurzu LNP202 budeme nastavovat uzel Lightning v režimu plug-and-play prostřednictvím Umbrel, nikoli klasickým způsobem přes příkazový řádek, aby byl vhodný pro středně pokročilé uživatele. Pokud dáváte přednost instalaci pomocí příkazového řádku, doporučuji vám postupovat podle níže uvedeného návodu. Připravují se také další, pokročilejší kurzy Lightningu orientované na příkazový řádek.



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Ve 3. části se pak dostanete od fungujícího uzlu k uzlu, který umíte ovládat. Nejprve určíte profil operátora uzlu Lightning (spotřebitel, obchodník nebo směrovač) a poté se seznámíte s kompletním softwarovým balíčkem pro správu, abyste mohli sledovat své kanály a čistě jednat ve své topologii. Nakonec se budete zabývat velmi důležitým bodem systému Lightning: jak získat příchozí likviditu, ať už prostřednictvím placených nebo kooperativních řešení.



Část 4 se zaměří na každodenní používání. Budete nastavovat spojení mezi vaším uzlem a mobilním zákazníkem, abyste mohli platit a vybírat jednoduše ze svého chytrého telefonu, aniž byste se museli vzdát vlastní úschovy. Nejprve se podíváme na síťový přístup prostřednictvím *Tailscale*, poté na protokolový přístup prostřednictvím *Nostr Wallet Connect*, s jejich příslušnými výhodami a kompromisy. Kurz bude zakončen závěrečnou kapitolou, která vám poskytne správné návyky pro udržení self-custody, a to jak z provozního, tak z pedagogického hlediska.



Pokud budete postupovat podle tohoto kurzu LNP202 ve správném pořadí, budete mít na jeho konci kompletní konfiguraci uzlu Lightning, funkční pro každodenní použití a především pod kontrolou.




## Porozumění uzlům Lightning


<chapterId>8275dfd8-7a72-48cc-bf7f-bc2a46063003</chapterId>



Před spuštěním vlastního uzlu se v této kapitole stručně seznámíte se základní teorií [Lightning Network](https://planb.academy/resources/glossary/lightning-network). Je skutečně důležité porozumět příslušným mechanismům, protože vám to umožní identifikovat rizika a přijmout správné postupy k jejich omezení. Nebudu zde však zacházet do podrobností, protože to není hlavním cílem tohoto kurzu. Pokud byste chtěli do tématu proniknout hlouběji, vřele doporučuji prostudovat kurz LNP 201 od Fanise Michalakise, který je v této oblasti referencí:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Co je to uzel Lightning?



Vraťme se k základům: než definujeme, co je to uzel, musíme pochopit, co je to Lightning Network. Je to protokol nejvyšší vrstvy postavený nad protokolem Bitcoin, který je navržen tak, aby umožňoval transakce mimo řetězec BTC, které jsou rychlé (s téměř okamžitou konečností) a obecně levné. "[Offchain](https://planb.academy/resources/glossary/offchain)" znamená, že transakce prováděné na Lightningu nejsou určeny k tomu, aby se objevily v hlavním [blockchainu](https://planb.academy/resources/glossary/blockchain) Bitcoin. Lightning je také částečnou reakcí na rostoucí využívání Bitcoin a na přetížení [onchainu](https://planb.academy/resources/glossary/onchain), které vyvolává obavy o [škálovatelnost](https://planb.academy/resources/glossary/scalability) systému.



Pro své fungování Lightning spoléhá na otevření [platebních kanálů](https://planb.academy/resources/glossary/payment-channel) mezi účastníky, v jejichž rámci lze transakce provádět téměř okamžitě, často s minimálními poplatky, aniž by bylo nutné je postupně registrovat v blockchainu Bitcoin. Tyto kanály mohou zůstat otevřené po velmi dlouhou dobu a vyžadují transakce na řetězci pouze při jejich otevření a uzavření.



[Uzel Lightning](https://planb.academy/resources/glossary/lightning-node) je účastníkem sítě Lightning, který otevírá kanály a provádí platby s jinými uzly. Konkrétně je uzel Lightning kus softwaru běžícího na počítači a implementujícího protokol Lightning Network. Příklady zahrnují LND, Core Lightning nebo Eclair. Hlavním úkolem tohoto softwaru je:




- připojit se k [uzlu Bitcoin](https://planb.academy/resources/glossary/full-node) a získat informace z hlavního blockchainu;
- vytvářet a spravovat obousměrné platební kanály s jinými uzly;
- vyměňovat zprávy s celou sítí Lightning.



![Image](assets/fr/001.webp)



### Uzel vs. Lightning Wallet: důležitý rozdíl



U Bitcoin (onchain) se "*[wallet](https://planb.academy/resources/glossary/wallet)*" vztahuje na software, který spravuje vaše [soukromé klíče](https://planb.academy/resources/glossary/private-key), vypočítává váš zůstatek z vašich [UTXO](https://planb.academy/resources/glossary/utxo) a vytváří vaše transakce. Tento wallet může být založen na vašem vlastním uzlu Bitcoin nebo na uzlu někoho jiného, ale dnes se role uzlu a role onchainu wallet jasně liší.



V aplikaci Lightning je obtížnější tento druh slovní zásoby znovu použít, aniž by došlo ke zmatení. Termín "*Lightning wallet*" je poněkud vágní, protože ve skutečnosti neexistuje nic takového jako skutečně samostatný Lightning wallet, pokud není založen na uzlu. Jsou tedy možné pouze dvě situace:



- Chcete-li mít skutečný uzel Lightning (tj. neúřední): software, který používáte (např. mobilní aplikace jako Phoenix nebo instance LND na Umbrel), skutečně provozuje uzel a vy skutečně držíte klíče k získání vašich bitcoinů. V tomto případě je váš "*Lightning wallet*" ve skutečnosti jen uživatelské rozhraní nad uzlem Lightning, ať už vestavěným nebo vzdáleným.



- Používání služby úschovy: používáte aplikaci, která vám v aplikaci Lightning zobrazuje zůstatek na účtu [sats](https://planb.academy/resources/glossary/satoshi-sat), ale na pozadí jsou prostředky v uzlu poskytovatele (např. Wallet of Satoshi). Nemáte klíče ani kontrolu nad kanály. Váš zůstatek je pouze účetní záznam v databázi společnosti. Je to srovnatelné s ponecháním bitcoinů na burzovní platformě se všemi souvisejícími riziky. V tomto případě je váš "*Lightning wallet*" pouze přístupem k účtu spravovanému operátorem, který zase provozuje skutečný uzel Lightning.



V případě Lightningu tedy neexistuje nic mezi tím: buď máte uzel (dokonce i vestavěný), takže jste ve vlastní péči, nebo nemáte, takže vaše sats vlastní společnost. Jak ale uvidíme v následujících kapitolách, tyto dva způsoby použití lze někdy těžko rozlišit. Například Phoenix je mobilní aplikace, která obsahuje skutečný uzel Lightning, ale uživatel si toho nemusí být nutně vědom, protože celá složitost jejího fungování je téměř zcela skryta.



### Připomenutí fungování systému Lightning Network



V této části vám stručně připomenu, jak Lightning funguje. Ještě jednou opakuji, že pokud byste chtěli podrobnější prezentaci teoretických konceptů, zvu vás, abyste se podívali na specializovaný kurz LNP 201.



#### Platební kanály: otevření, aktualizace a uzavření



Základem sítě Lightning jsou obousměrné platební kanály. Kanál lze otevřít (tj. vytvořit), aktualizovat podle toho, jak probíhají transakce Lightning, a nakonec uzavřít. Z pohledu onchainu není kanál nic jiného než 2/2 [vícepodpisový](https://planb.academy/resources/glossary/multisig) [výstup](https://planb.academy/resources/glossary/output).



![Image](assets/fr/002.webp)



Z pohledu Blesku se jedná o platební kanál s [likviditou](https://planb.academy/resources/glossary/liquidity-lightning) rozdělenou mezi dva účastníky.



![Image](assets/fr/003.webp)





- Otevření kanálu:**



Dva uzly se rozhodnou otevřít kanál. Jeden z nich odevzdá bitcoiny v řetězové transakci nazvané *finanční transakce*. Tato transakce vytvoří výstup založený na multisignature [skriptu](https://planb.academy/resources/glossary/script) 2 z 2, což znamená, že utracení těchto prostředků na Bitcoin vyžaduje [podpis](https://planb.academy/resources/glossary/digital-signature) obou uzlů v kanálu. Před vydáním této transakce strana poskytující prostředky požádá druhou stranu o podepsání transakce *výběr*, která není vydávána onchain, ale která jí umožňuje získat zpět své prostředky v případě problému.



![Image](assets/fr/004.webp)





- Transakce Commitment:**



Stav kanálu (tj. distribuce sats mezi A a B) je reprezentován *[commitment transaction](https://planb.academy/resources/glossary/commitment-transaction)*, který je znám oběma uzlům, ale není okamžitě vysílán do blockchainu. Tato transakce popisuje, jak přerozdělit prostředky kanálu v řetězci podle plateb provedených na Lightningu.



S každou platbou Lightning podepíší oba uzly nový stav, který nahradí ten předchozí. Starý stav je odvolán díky mechanismu odvolávacího klíče: pokud se jeden z účastníků pokusí odvysílat starý stav, může druhý účastník získat zpět celou částku prostředků jako pokutu.



Důležitá je zde myšlenka, že uzly vždy uchovávají podepsanou transakci Bitcoin, která není vysílána v řetězci a která umožňuje vzájemné přerozdělování sats podle plateb provedených na Lightning Network.



![Image](assets/fr/005.webp)





- Uzavření kanálu:**



Kanál může být uzavřen čistě prostřednictvím kooperativního uzavření, kdy se obě strany dohodnou na konečném stavu kanálu, nebo jednostranně (vynucené uzavření), pokud jeden z účastníků přestane spolupracovat nebo se stane nedostupným. Ve všech případech má uzavření podobu transakce v řetězci, která utratí výstup 2/2 a rozdělí prostředky mezi účastníky podle posledního platného stavu kanálu.



![Image](assets/fr/006.webp)



Lightning tak funguje jako sekundární vrstva ukotvená v Bitcoin: v hlavním blockchainu se objevují pouze určité události (otevírání a zavírání kanálů). Průběžné platby zůstávají mimo řetězec.



Než se pustíme do dalších kroků, uvedeme dva základní pojmy pro pochopení toho, jak spravovat kanál Lightning:




- Liquidity*: množství sats dostupné na jedné straně kanálu;
- *[kapacita](https://planb.academy/resources/glossary/lightning-channel-capacity)*: jedná se o celkovou částku zablokovanou v multisigovém výstupu 2/2, tj. součet likvidity na obou stranách kanálu.



#### Síť kanálů a likvidita



Kanál neslouží pouze k platbám mezi dvěma uzly: je součástí globální sítě vzájemně propojených kanálů. Váš uzel může směrovat platby pro jiné uživatele přes své vlastní kanály a vy můžete poslat sats do uzlu Lightning, se kterým nemáte přímý kanál, pokud lze mezi vašimi dvěma uzly najít platnou cestu.



Každý uzel zná prostřednictvím [drbacího protokolu](https://planb.academy/resources/glossary/gossip) mapu této sítě: které kanály existují, které uzly jsou propojeny obousměrným kanálem a které kapacity jsou zveřejněny. Chcete-li poslat platbu příjemci bez přímého kanálu, vypočítá váš uzel trasu sestávající z několika skoků: váš uzel → uzel X → uzel Y → uzel příjemce. V každém skoku platba prochází kanálem, který musí mít dostatečnou likviditu ve směru platby.



![Image](assets/fr/007.webp)



Likvidita kanálu proto není symetrická: jedna strana může být silně zatížená, zatímco druhá je téměř prázdná. Řízení této likvidity, tj. znalost toho, kde se sats nacházejí a kterým směrem mohou proudit, je jedním z nejdůležitějších aspektů provozu uzlu Lightning. Podrobněji se mu budeme věnovat v následujících praktických kapitolách.



#### HTLC: přeprava plateb bez okradení



Aby mohly platby procházet přes zprostředkující uzly bez nutnosti důvěry, používá Lightning [chytré smlouvy](https://planb.academy/resources/glossary/smart-contract) zvané *[HTLC](https://planb.academy/resources/glossary/htlc)* (*Hashed Time-Locked Contracts*). Zjednodušeně řečeno, HTLC podmiňuje převod finančních prostředků odhalením tajemství a obsahuje časové omezení, které chrání odesílatele v případě selhání transakce. Každá platba je tedy podmíněna předložením předběžného obrazu (tajemství, jehož [hash](https://planb.academy/resources/glossary/hash-function) odpovídá dohodnuté hodnotě). Pokud konečný příjemce předloží tento předběžný obraz, může si nárokovat prostředky, což následně umožní každému zprostředkujícímu uzlu získat zpět své vlastní prostředky.



![Image](assets/fr/008.webp)



Ušetřím vás technických podrobností o tom, jak HTLC fungují, protože pro účely tohoto kurzu nejsou podstatné. Podrobné vysvětlení najdete v teoretickém kurzu LNP 201. Jen si pamatujte, že HTLC umožňují atomické výměny: buď je převod dokončen a nikdo není při směrování poškozen, nebo se nezdaří a každý účastník získá zpět své původní prostředky. Neexistuje nic mezi tím.



### Hlavní implementace uzlů Lightning



Stejně jako v případě Bitcoin existuje několik implementací protokolu Lightning. Řada nezávislých týmů vyvíjí vlastní verze, které jsou všechny interoperabilní, protože dodržují stejné specifikace ([BOLT](https://planb.academy/resources/glossary/bolt)). Zde jsou hlavní dnes používané implementace.



#### LND (*Lightning Network Daemon*)



LND je kompletní implementace protokolu Lightning napsaná v jazyce Go a vyvinutá společností Lightning Labs.



![Image](assets/fr/009.webp)



#### Jádro Lightning (*CLN*)



Core Lightning (dříve *C-Lightning*) je implementace vyvinutá společností Blockstream. Je napsána v jazyce C a některé komponenty v Rust.



![Image](assets/fr/010.webp)



#### Eclair



Eclair je implementace napsaná v jazyce Scala a vyvinutá francouzskou společností ACINQ. Společnost ACINQ provozuje jeden z nejdůležitějších směrovacích uzlů v síti Lightning pomocí systému Eclair a používá tuto implementaci jako softwarový základ pro své vlastní produkty, například aplikaci Phoenix.



![Image](assets/fr/011.webp)



#### LDK (*Lightning Development Kit*)



LDK (*Lightning Development Kit*) je vývojová sada Rust, kterou spravuje společnost Spiral (Block, ex-Square). Nejedná se o hotový daemon jako LND nebo CLN, ale o knihovnu pro vývojáře, kteří chtějí integrovat Lightning přímo do svých aplikací.



![Image](assets/fr/012.webp)



V tomto kurzu LNP202 se zaměříme především na LND: implementaci, která se nejčastěji používá v řešeních na klíč pro soukromé zákazníky, jako je například Umbrel.



Tolik stručná připomínka toho, jak Blesk funguje. Ještě jednou připomínám, že pokud některým pojmům nerozumíte nebo pokud byste se chtěli před jejich uvedením do praxe ponořit trochu hlouběji, je pro vás základní příručkou na toto téma kurz Fanise Michalakise:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


## Proč provozovat vlastní uzel Lightning?


<chapterId>421db24e-511c-41ed-ad68-69b0662042ea</chapterId>



Odpověď na tuto otázku je poměrně jednoduchá, protože je řečnická: bez vlastního uzlu už ve skutečnosti nepoužíváte Lightning, ale pouze iluzi Lightningu v rámci firemní infrastruktury.



Použití Lightning custodial wallet znamená, že bitcoiny technicky patří společnosti, která uzel provozuje. Nedržíte soukromé klíče a neovládáte kanály. Váš zůstatek na wallet je jen řádek v databázi poskytovatele služeb. Tato situace je jistě velmi pohodlná pro začátečníky a uživatelská zkušenost je často plynulá, ale zásadní otázka zní: jaká je výhoda používání Bitcoin a Lightning, když se nakonec vzdáte právě těch aspektů, které je odlišují od tradičních měn a bank?



Dvěma hlavními hodnotami Bitcoin jsou peněžní suverenita (vydávání a držení peněz již není závislé na centrálním orgánu) a odolnost vůči cenzuře (nemožnost třetí strany zabránit platbám nebo je filtrovat). Systém úschovy na platformě Lightning jde přímo proti oběma těmto cílům: nemůžete kontrolovat interní peněžní zásobu platformy a z definice může provozovatel, který drží všechny prostředky a všechny kanály, vaše platby cenzurovat, zdržovat, upřednostňovat nebo blokovat. Za těchto podmínek si můžeme oprávněně položit otázku, **jaký smysl má používání bitcoinu prostřednictvím Lightningu, pokud bude reprodukovat stejné vzorce důvěry a závislosti jako u tradičních státních měnových systémů**.



> Potřebujeme elektronický platební systém založený na kryptografickém důkazu místo důvěry, který umožní dvěma ochotným stranám provádět transakce přímo mezi sebou bez potřeby důvěryhodné třetí strany.
*Bílá kniha Satoshi Nakamoto, Bitcoin


Filozofii stranou, konkrétnější nevýhody pro vás jsou následující. Zaprvé nemáte možnost ověřit, zda společnost skutečně vlastní bitcoiny odpovídající zobrazeným zůstatkům. Může pracovat s částečnou rezervou, může být hacknuta, zkrachovat nebo jednoduše zmizet. V takovém případě jste jen dalším věřitelem bez skutečné záruky, že dostanete své peníze zpět.



Za druhé, společnost je vystavena regulačním rizikům: soudním příkazům, zmrazení finančních prostředků, žádostem o zablokování uživatelů nebo transakcí, zesílenému dohledu nebo dokonce úplnému zákazu činnosti v některých jurisdikcích. Každé omezení, které dopadá na poskytovatele služeb, se mechanicky promítá i na vás.



Z hlediska důvěrnosti není situace o nic lepší. Operátor úschovy vidí všechny vaše toky: částky, frekvence, příjemce, zůstatky, výdajové zvyklosti. V kombinaci s informacemi poskytovanými aplikací a případně podkladovou analýzou řetězce Bitcoin mohou tyto informace poskytnout velmi přesný profil vaší finanční aktivity. Opět je to daleko od cíle Bitcoin, kterým je omezení finančního monitoringu.



Dobrou zprávou je, že dnes už není provozování vlastního uzlu Lightning výsadou technických odborníků, jak tomu bylo na konci roku 2010. Pro domácí uživatele jsou k dispozici relativně jednoduchá řešení, která si podrobně vysvětlíme v následující kapitole.




## Výběr správného řešení pro danou úlohu


<chapterId>615870e3-741d-4ec1-875d-a483e70f39d4</chapterId>



Dnes je možné mít uživatelský zážitek velmi podobný tomu, který poskytuje zařízení wallet v režimu Lightning custodial, a přitom zůstat v režimu vlastní péče. Cílem této kapitoly je pomoci vám vybrat cestu, která nejlépe odpovídá vašemu profilu.



### Možnost 1: Nepoužívejte přímo Lightning



Prvním řešením je jednoduše nepoužívat nativně Lightning, ale použít Bitcoin nebo [Liquid](https://planb.academy/resources/glossary/liquid-network) wallet, které obsahují [atomické výměny](https://planb.academy/resources/glossary/atomic-swap). Tuto metodu využívají například aplikace Aqua nebo BULL Wallet, které umožňují platit [faktury Lightning](https://planb.academy/resources/glossary/invoice-lightning), aniž byste sami provozovali uzel Lightning, a přitom zůstávají v režimu self-custody.



Princip je jednoduchý: vaše prostředky zůstávají v Bitcoin, buď v on-chain, nebo v Liquid, a vy k nim přistupujete prostřednictvím wallet, kde držíte klíče tradičním způsobem. Když naskenujete fakturu Lightning, váš wallet iniciuje transakci (on-chain nebo Liquid) do služby atomické výměny. Tato služba pak spravuje platbu Lightning prostřednictvím svého vlastního uzlu a používá bitcoiny, které jste poskytli on-chain nebo prostřednictvím Liquid. Díky tomu nemusíte sami obsluhovat žádné kanály Lightning, a přesto můžete bezproblémově vypořádávat faktury Lightning.



![Image](assets/fr/013.webp)



Hlavní výhodou tohoto přístupu ve srovnání s běžným bleskovým depozitářem wallet je, že své prostředky máte vždy stoprocentně ve své moci. Bitcoiny jsou ve vašem onchainu nebo Liquid wallet s vaší vlastní [mnemotechnickou frází](https://planb.academy/resources/glossary/seed). I během směny zůstáváte ve vlastnictví svých prostředků, protože směna je atomická. Spoléhá na kryptografický mechanismus, který zajišťuje, že existují pouze dva možné výsledky: buď se výměna zcela podaří, nebo se nezdaří a služba si vaše prostředky nemůže přivlastnit.



Většina portfolií nabízejících tento typ funkcí spoléhá na [Boltz](https://boltz.exchange/) pro technickou část výměny.



Toto řešení nabízí také zajímavé výhody z hlediska důvěrnosti, zejména ve spojení s Liquid. Pro začátečníka je také velmi snadné nastavení a uložení: klasická mnemotechnická fráze, žádné kanály, žádná likvidita k vyvážení...



Na druhou stranu má tento přístup svá omezení. Zaprvé, není neocenitelný: jste závislí na dostupnosti a dobré vůli výměnné služby. Pokud již nechce zpracovávat váš účet nebo přestane fungovat, nemůžete jejím prostřednictvím platit faktury Blesku. Pak jsou tu nezanedbatelné poplatky: platíte jak [poplatky za transakce](https://planb.academy/resources/glossary/transaction-fees) v řetězci nebo Liquid, tak provizi swapové služby. Pokud navíc poplatky onchain prudce vzrostou, může se používání služby Lightning velmi prodražit.



Pro příležitostné použití je tedy ještě přijatelný, ale pro velmi aktivní uživatele Lightning je lepší udělat věci správně pomocí skutečného uzlu Lightning.



### Možnost 2: Palubní uzly Lightning



Druhá kategorie řešení je založena na uzlech Lightning zabudovaných přímo do mobilní aplikace. Průkopníkem tohoto modelu byl Phoenix Wallet, který zůstává vzorem. Dnes nabízejí srovnatelné přístupy i další projekty, například Zeus (ve vestavěném režimu) nebo BitKit.



Myšlenka je jednoduchá: aplikace skutečně běží na uzlu Lightning, ale všechny složité operace jsou prováděny automaticky na pozadí. Máte k dispozici rozhraní "*Lightning wallet*" s mnemotechnickou frází pro zálohování, vidíte zůstatek a platíte faktury, ale nespravujete kanály, likviditu ani většinu parametrů.



![Image](assets/fr/014.webp)



Tato řešení jsou vždy samospasitelná. Klíče, které ovládají fondy, jsou generated a jsou uloženy v telefonu a zálohování probíhá prostřednictvím seed nebo ekvivalentního mechanismu. Nemáte pouze účet u poskytovatele služeb, ale skutečně vlastníte bitcoiny uzamčené v kanálech, které vám patří a nemohou být odcizeny.



Výhod palubních uzlů LN je celá řada:




- velmi snadná instalace a používání;
- uživatelský zážitek blízký zážitku z úschovy Lightning wallet, ale s vlastní úschovou;
- žádná manuální správa kanálů nebo likvidity;
- relativně jednoduché zálohování.



Tyto vestavěné wallet však mají také značná omezení. Zaprvé, pokud jde o důvěrnost, provozovatel služby (např. ACINQ v případě Phoenix) má poměrně podrobný přehled o tocích procházejících vaším uzlem: množství, frekvence, příjemci, i když i to se jistě zlepší, zejména s postupným zaváděním *Trampolínových uzlů*. Za druhé jste na tomto operátorovi jako na svém hlavním partnerovi Lightning značně závislí. Pokud se uzel ACINQ stane nedostupným (v případě Phoenix), pokud se společnost dostane pod regulační tlak nebo změní svůj obchodní model, může být vaše uživatelská zkušenost vážně zhoršena, nebo dokonce ohrožena.



Tato jednoduchost má svou cenu. Vestavěné služby uzlu LN si obvykle účtují specifické poplatky za vklady, výběry nebo některé operace správy kanálů. Podle mého názoru má tento model smysl z hlediska nabízených služeb, ale pro intenzivní využití může být mnohem dražší než dobře spravovaný běžný uzel Lightning.



### Možnost 3: klasický uzel Lightning



Třetím řešením, kterému se budeme v tomto kurzu LNP202 věnovat podrobněji, je provozování běžného uzlu Lightning na vyhrazeném serveru nebo zařízení.



Pod pojmem "klasický" rozumím, že si sami nainstalujete a nakonfigurujete implementaci Lightning (např. LND) nad vlastním uzlem Bitcoin. Vyberete si své partnery, otevřete své kanály, spravujete [příchozí a odchozí likviditu](https://planb.academy/resources/glossary/inbound-capacity) a nastavíte zásady směrování poplatků.



Z hlediska suverenity je to nejlepší řešení. Nejste již závislí na konkrétní společnosti, pokud jde o vaše kanály nebo platby: pokud vás některý partner cenzuruje nebo uzavře kanál, můžete si otevřít jiný s jiným uzlem. Pokud služba zanikne, vaše sats zůstanou v kanálech, které máte pod kontrolou, a můžete je repatriovat onchain. Můžete také optimalizovat své dlouhodobé náklady: jakmile jsou vaše kanály správně dimenzovány a spravovány, mohou se celkové náklady na platby stát velmi nízkými.



Pokud jde o důvěrnost, podléháte samozřejmě omezením vlastního modelu Lightning, ale nepředáváte celý svůj podnik jedinému provozovateli.



Naproti tomu nastavení klasického uzlu Lightning je samozřejmě složitější: musíte instalovat, konfigurovat, udržovat, sledovat aktualizace, pochopit logiku kanálů a zásad účtování, spravovat kanály a peněžní toky atd. Špatná konfigurace, nedbalé zálohování nebo nedbalá správa mohou snadněji vést ke ztrátě sats. Uzel také musí běžet nepřetržitě.



Právě tuto cestu vám v tomto kurzu navrhuji, abych vás provázel na každém kroku, omezil rizika a strukturoval váš přístup.



### Které řešení pro který uživatelský profil?



Chcete-li si vybrat správné řešení pro svůj profil uživatele aplikace Lightning, musíte zvážit dva faktory: jak často aplikaci Lightning používáte a jakou máte chuť k technické správě.



Pokud neprovádíte mnoho příležitostných bleskových plateb, ale přesto chcete mít možnost čas od času uhradit faktury LN z telefonu, aniž byste se museli vzdát vlastní úschovy: Bitcoin nebo Liquid wallet s funkcí swapu je pravděpodobně nejlepší volbou. Ponecháte si vlastnictví svých prostředků, nebudete spravovat žádné uzly a výměnou za jednoduchost přijmete o něco vyšší poplatky.



https://planb.academy/tutorials/wallet/mobile/bull-bitcoin-2c72127c-a228-4f50-b833-c6183d56aaf6

https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Pokud používáte službu Lightning poměrně pravidelně a chcete využívat výhody skutečného uzlu, ale nechcete trávit čas správou kanálů, poplatků nebo infrastruktury, je mobilní vestavěný uzel Lightning dobrým řešením. Zachováte si péči o své prostředky, uživatelské rozhraní zůstane velmi přístupné a veškerá složitost je skryta za cenu výrazné závislosti na operátorovi.



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

https://planb.academy/tutorials/wallet/mobile/bitkit-a7224674-85c4-4045-9baf-37018d89550c

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Pokud jste středně pokročilý nebo pokročilý uživatel, chcete investovat čas do pochopení a správy infrastruktury a chcete mít maximální kontrolu nad svými kanály, likviditou a náklady: klasický serverový uzel Lightning je tou správnou volbou. Je to nejnáročnější řešení, ale také nejvíce odpovídá myšlence suverenity Bitcoin.




# Vytvoření prvního uzlu Lightning


<partId>b6db225e-61ab-437a-bccb-33d07503da15</partId>



## Instalace LND s Umbrel


<chapterId>a0014bf3-1bd3-4311-b15b-5ef2354ec744</chapterId>



Nyní, když jsme si prošli základy služby Lightning a dostupná řešení, je čas přejít k práci. K absolvování tohoto kurzu budete potřebovat uzel Bitcoin synchronizovaný s uzlem Umbrel. Tento školicí kurz LNP202 navazuje na kurz BTC 202; pokud ještě nemáte uzel Bitcoin, vyzývám vás, abyste absolvovali tento jiný školicí kurz a teprve poté, co bude váš uzel synchronizován, se sem vrátili. Důrazně doporučuji, abyste se s ním seznámili, protože se nebudu podrobně zabývat jeho fungováním, konfigurací a bezpečnostními opatřeními.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

V této první kapitole se podíváme na to, jak nainstalovat LND na váš Umbrel. Díky způsobu, jakým Umbrel funguje, je tento krok velmi jednoduchý, protože stačí nainstalovat aplikaci.



Na domovské stránce otevřete v dolní části rozhraní položku `App Store`.



![Image](assets/fr/015.webp)



Do vyhledávacího řádku zadejte `Lightning Node` a klikněte na aplikaci.



![Image](assets/fr/016.webp)



Poté klikněte na tlačítko `Install` a spusťte instalaci.



![Image](assets/fr/017.webp)



Na domovské stránce klikněte na aplikaci, aby se otevřela, a poté vyberte možnost `Nastavit nový uzel`.



![Image](assets/fr/018.webp)



Dostanete mnemotechnickou frázi o 24 slovech. Uložte si ji na bezpečné místo. V příští kapitole se podrobněji podíváme na to, jak znovu získat přístup k uzlu Lightning (jedná se o mnohem složitější proces než u jednoduchého Bitcoin wallet), ale prozatím si pamatujte, že tato fráze hraje klíčovou roli a je třeba ji uložit s maximální péčí.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Tuto frázi uložte stejným způsobem jako běžnou mnemotechnickou frázi: na fyzický nosič (papír nebo kov) uložený na bezpečném místě a poté klikněte na tlačítko `NEXT`.



![Image](assets/fr/019.webp)



Poté zadejte slova věty a zkontrolujte, zda jste je zapsali správně.



![Image](assets/fr/020.webp)



Výstražná zpráva vás upozorní, že aplikace je v beta verzi a že Lightning Network zůstává experimentální technologií. Je zřejmé, že do uzlu Lightning nikdy neukládejte částky, o které nejste připraveni přijít.



Poté se dostanete do hlavního rozhraní uzlu Lightning. Vlevo najdete svůj řetězec Bitcoin onchain wallet, který je hostován ve vašem uzlu. Jedná se o jeden generated z 24slovné fráze, kterou jste právě uložili.



Uprostřed najdete blesk wallet. Ve skutečnosti představuje vaši [odchozí hotovost](https://planb.academy/resources/glossary/outbound-capacity), tj. bitcoiny, které vlastníte v rámci svých kanálů Lightning.



Vpravo se zobrazí několik důležitých informací o uzlu:




- Počet připojení a otevřených kanálů;
- Váš celkový odchozí peněžní tok, tj. to, co můžete teoreticky utratit za Blesk;
- Vaše celková příchozí likvidita, tj. to, co můžete teoreticky obdržet na účet Lightning.



![Image](assets/fr/021.webp)



Začněme přizpůsobením našeho uzlu. Klikněte na tři malé tečky v pravém horním rohu rozhraní a poté na `Rozšířená nastavení`. V podnabídce `Personalizace` můžete definovat veřejné jméno uzlu (vyhněte se použití svého skutečného jména) a zvolit jeho barvu.



![Image](assets/fr/046.webp)



Poté klikněte na zelené tlačítko `UCHOVAT A ZRUŠIT`, čímž restartujete uzel a provedete tyto změny.



Váš uzel Lightning je nyní připraven otevřít první kanály pro provádění plateb. Nejprve se však podívejme na to, jak chránit váš sats!



## Uložení uzlu Lightning


<chapterId>638fa75d-62af-4bf3-ab4a-b7d10ea75815</chapterId>



Než odešlete svůj první modul sats do uzlu, je důležité pochopit, jak funguje jeho zálohování a jaká jsou související rizika. Na rozdíl od jednoduchého onchain portfolia Bitcoin je zálohování uzlu Lightning poměrně složité: špatná strategie může vést k trvalé ztrátě vašich prostředků. V této kapitole se podíváme na to, co je skutečně třeba zálohovat, a jak tento proces zvládá Umbrel s LND.



V tomto kurzu budeme používat implementaci LND (*Lightning Network Daemon*). Přestože principy jsou u ostatních implementací podobné, soubory pro obnovu a postupy, o kterých budu hovořit, jsou specifické pro implementaci LND.



### Co bych měl uložit do uzlu Lightning?



V uzlu Lightning nestačí uložit seed a doufat, že se vše vrátí do normálu. Několik prvků hraje různé role, proto je důležité mezi nimi rozlišovat.



#### seed (*aezeed*)



Při inicializaci LND obdržíte 24slovné seed. Jedná se o formát specifický pro LND, který se nazývá "*aezeed*". Nejedná se o klasický formát seed BIP39, i když se mu hodně podobá. Z tohoto seed odvodí LND soukromé klíče vašeho onchainu wallet spojeného s uzlem Lightning, tj. adresy, na které můžete přijímat nebo na které můžete repatriovat bitcoiny po uzavření kanálu.



![Image](assets/fr/019.webp)



Tento seed lze proto použít k obnovení onchainu wallet spojeného s vaším uzlem a k získání prostředků, které již byly repatriovány onchain (např. po uzavření kanálu). Na druhou stranu samotný seed nestačí k obnovení vašich bleskových kanálů, které jsou stále otevřené, protože neobsahuje potřebné informace o stavu vašich kanálů.



#### Databáze kanálů (`channel.db`)



LND ukládá podrobný stav vašich kanálů do databáze s názvem `channel.db`. Tato databáze obsahuje:




- seznam otevřených kanálů;
- své kolegy a jejich identifikátory;
- poslední commitment transaction pro každý kanál (postupné stavy, které určují, kdo co v kanálu vlastní, a umožňují obnovení prostředků v řetězci v případě problému);
- informace potřebné k potrestání kolegy, který se pokusí odvysílat staré hlášení.



Problémem této databáze je, že se neustále mění: každá platba, každé směrování, každé otevření nebo uzavření kanálu mění její obsah. Proto je běžné zálohování (např. pravidelná kopie souboru `channel.db`) nebezpečné. Pokud obnovíte příliš starou verzi souboru `channel.db` a znovu sestavíte uzel s tímto zastaralým stavem, mohou se vaši kolegové domnívat, že vysíláte starý stav kanálu. V takovém případě protokol stanoví sankci: váš vrstevník může získat zpět celou částku prostředků kanálu, jako byste se pokusili podvádět.



V praxi tedy soubor `channel.db` není záložním médiem jako takovým. Je to živý stav vašeho uzlu. Jediná situace, kdy má smysl ji použít k obnově uzlu, je, když tuto databázi obnovujete přímo ze stroje, který právě selhal (např. z disku, který je stále čitelný). V takovém případě obnovíte nejnovější stav a můžete na základě této databáze znovu spustit LND na jiném stroji s jistotou, že tento stav je co nejaktuálnější, protože starý stroj již neběží. Další situací, kdy tato metoda může sloužit jako relevantní záloha, je konfigurace se dvěma disky s dynamickou trvalou kopií z jednoho na druhý. Tento typ nastavení je však složitější na implementaci.



Vytváření pravidelných kopií souboru `channel.db` a jejich ukládání jako záloh k pozdějšímu obnovení je však velmi špatný nápad: v den, kdy je použijete, riskujete, že se potrestáte a přijdete o všechny své soubory sats.



#### Statické zálohování kanálů (SCB)



Aby bylo možné obnovení po havárii, zavedla společnost LND mechanismus *Static Channel Backup* (SCB). Jedná se o speciální soubor, často nazývaný `channel.backup`, který obsahuje statické informace o vašich kanálech: kdo jsou vaši kolegové, jak je kontaktovat a jaké jsou vaše kanály.



Tento soubor neobsahuje podrobný stav kanálu ani historii aktualizací. Neumožňuje znovu otevřít kanály přesně v tom stavu, v jakém byly, ani pokračovat v provozu tohoto uzlu Lightning. Jeho úkolem je spíše fungovat jako kotevní bod, který vám pomůže požádat vaše kolegy, aby vám pomohli čistě uzavřít všechny kanály, a tím získat váš sats onchain, na klíče, které můžete získat díky seed. Takže na rozdíl od souboru `channel.db`, který se mění při každé platbě nebo směrování, se soubor SCB aktualizuje pouze při otevření nebo uzavření kanálu.



Při obnově prostřednictvím SCB je postup následující:




- Obnovíte svůj uzel seed (*aezeed*), který znovu vytvoří váš řetězec wallet spojený s uzlem Lightning;
- Společnosti LND poskytnete svůj poslední SCB;
- LND používá SCB k vyhledání seznamu vašich kolegů a kanálů, které s nimi máte;
- Kontaktuje jednotlivé partnery, oznámí jim, že došlo ke ztrátě dat, a požádá je o nucené uzavření kanálu, abyste mohli obnovit sdílení v řetězci.



Jde o to, že vaši kolegové, kteří si všimnou, že hlásíte ztrátu dat, odvysílají svůj poslední signál commitment transaction a uzavřou silový kanál. Jakmile budou tyto transakce potvrzeny, vaše prostředky se znovu objeví ve vašem onchain portfoliu (spojeném s seed).



Tento mechanismus obnovy však není dokonalý. Za prvé, ve skutečnosti neobnoví váš uzel Lightning, protože všechny kanály budou uzavřeny. Budete tedy muset vytvořit nový uzel Lightning od začátku. Za druhé nezaručuje 100% obnovu, i když v případě problému výrazně zvyšuje šanci na obnovení zůstatků v řetězci. Tento protokol obnovy totiž závisí na spolupráci a dostupnosti vašich peerů: pokud je některý z nich offline, ztratil vlastní data nebo odmítá spolupracovat, vaše prostředky mohou zůstat zablokované, nebo dokonce trvale ztracené. Proto je důležité, abyste v uzlu Lightning nenechávali dlouho otevřené kanály s nedostupnými peery. Pokud v tomto okamžiku dojde ke ztrátě dat a peer zůstane nedostupný, obnovení prostřednictvím SCB bude nemožné a vaše prostředky zůstanou ztraceny, dokud se tento peer nevrátí zpět do provozu (možná navždy).



Dobrá strategie zálohování blesku LND stojí na třech pilířích:




- Váš seed (*aezeed*), pro vrstvu onchain;
- Spolehlivé automatické zálohování SCB;
- Dobré řízení kanálů výběrem spolehlivých partnerů a preventivním uzavíráním těch, které jsou často nedostupné.



### Jak Umbrel spravuje zálohování uzlu LND?



Umbrel nabízí zjednodušený zálohovací mechanismus pro uzel LND, založený právě na SCB. Smyslem je ušetřit vám práci s vlastní manipulací s tímto souborem, vytvořit jeho zálohu a celý proces co nejvíce automatizovat.



Při vytvoření uzlu na Umbrel obdržíte uzel seed, který plní dvojí úlohu:




- odvozuje váš řetězec Bitcoin onchain wallet spojený s vaším uzlem Lightning;
- slouží k odvození identifikátoru zálohy a šifrovacího klíče používaného pro vzdálené zálohy SCB.



Díky tomuto mechanismu Umbrel automaticky vytváří šifrovanou zálohu vašeho SCB a ukládá ji na své servery prostřednictvím sítě Tor. SCB je uložen šifrovaně díky klíči odvozenému od vašeho seed. V případě ztráty dat tedy stačí znovu vytvořit uzel Bitcoin a Lightning na Umbrel, na stejném nebo jiném počítači, a poté vstoupit do vašeho seed. Poté budete moci načíst nejnovější stav SCB ze serverů Umbrel, dešifrovat jej a zahájit proces obnovy svých prostředků.



Tyto zálohy jsou před odesláním lokálně šifrovány vaším uzlem, což zaručuje důvěrnost vašich dat: Umbrel nemůže přečíst obsah SCB. Přenos probíhá přes Tor, což zabraňuje úniku vaší IP adresy. Navíc váš uzel Umbrel přidává do přenosu šum (náhodné vycpávky a falešné zálohy odesílané v nepravidelných intervalech), aby server nemohl přesně odvodit, kdy kanál otevíráte nebo zavíráte.



Hlavní výhodou této metody je, že výrazně zjednodušuje zálohování uzlu Lightning: stačí zálohovat uzel seed pouze jednou během inicializace uzlu. To s sebou nese určité riziko, protože se jedná pouze o zálohu SCB, ale pro rozumné množství je to přijatelný kompromis.



### Osvědčené postupy pro omezení rizika ztráty



I v případě zálohování Umbrel může několik jednoduchých správných postupů výrazně snížit riziko ztráty sats:





- Sledujte dostupnost svých kolegů:



Pokud je důležitý kanál často spojen s nedosažitelným nebo nestabilním partnerem, je bezpečnější jej čistě uzavřít, dokud váš uzel stále funguje. Preventivní kooperativní nebo nucené uzavření eliminuje potenciální zdroj potíží v případě obnovy SCB.





- Vyvarujte se přílišné koncentrace likvidity na neznámé kolegy:



Čím větší kanál s vámi partner má, tím důležitější je, aby byl spolehlivý. Vybírejte seriózní, dobře propojené a aktivní uzly, aby případné budoucí obnovení prostřednictvím SCB mohlo proběhnout hladce.





- Doplňte Umbrel o místní zálohy:



Kromě automatického zálohování v systému Umbrel můžete také uchovávat šifrovanou kopii souboru SCB (`channel.backup`) na externím médiu a pravidelně ji aktualizovat. V ideálním případě byste ji měli obnovovat při každém otevření nebo zavření kanálu. Tím získáte záložní řešení pro případ, že by z jakéhokoli důvodu byla služba automatického zálohování Umbrel nedostupná.





- Správná správa seed



Váš seed Umbrel nejen obnovuje váš řetězec wallet, ale také odvozuje šifrovací klíč pro zálohy. Útočník, který k němu má přístup, by tedy mohl spustit obnovu a převést vaše prostředky na svůj vlastní wallet, aniž by měl fyzický přístup k vašemu uzlu.



Pokud tedy budete potřebovat obnovit uzel, ale nebudete již mít k dispozici seed, nebudete moci obnovit nic: všechny vaše sats budou ztraceny. Proto je velmi důležité, abyste si soubor seed ukládali s maximální opatrností, pouze na fyzická média (papír nebo kov) a uchovávali jej na bezpečném místě. Další informace o správě zařízení seed naleznete v tomto návodu:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### Jak mohu uložit svůj uzel Lightning na Umbrel?



Teď, když jste pochopili, jak funguje teorie, přejděme k samotné podstatě věci. V aplikaci Lightning Node (což je vlastně LND) klikněte na tři malé tečky v pravém horním rohu.



![Image](assets/fr/022.webp)



Pro zálohování jsou zde zajímavé tři prvky:




- Zkontrolujte, zda je povolena možnost `Automatické zálohování`. Tím se zašifrovaný SCB automaticky odešle na servery společnosti Umbrel.
- Pomocí možnosti `Zálohovat přes Tor` si pak můžete vybrat, zda chcete odesílat přes Tor, nebo přes Clearnet. Jak bylo vysvětleno v předchozích částech, důrazně doporučuji používat Tor, abyste zachovali důvěrnost.
- Nakonec je zde tlačítko `Stáhnout soubor zálohy kanálu`, které vám umožní stáhnout do počítače soubor `záloha kanálu`, tj. zašifrovaný snímek vašeho SCB. To vám umožní čas od času vytvářet další místní zálohy kromě těch, které se automaticky odesílají na servery Umbrel.



Nyní víte, jak ochránit uzel sats Lightning před ztrátou dat. V příští kapitole se podíváme na to, jak uzel zabezpečit proti pokusům o podvod.




## Watchtower: úloha a nastavení


<chapterId>e6c654dd-26c5-4e4d-8d11-a215bac37812</chapterId>



V systému Lightning je každý kanál založen na posloupnosti po sobě jdoucích stavů, které jsou reprezentovány nezveřejněnými čísly commitment transaction. S každou platbou nebo směrováním Lightningu vytvoří 2 účastníci kanálu nový pár commitment transaction, který odráží aktuální rozložení prostředků v kanálu. Staré commitment transaction se stávají zastaralými.



Pokud jedna ze stran zveřejní neaktuální stav, má druhá strana právo ji sankcionovat a vymáhat zpět celou částku prostředků kanálu. V této kapitole se krátce podíváme na to, jak tento mechanismus funguje, a poté si vysvětlíme, jak nastavit ***watchtower***: systém, který chrání uzel Lightning před možnými pokusy o podvod.



### Pochopení fungování strážních věží


V každém okamžiku má každá strana v kanálu k dispozici commitment transaction, který by jí v případě zveřejnění umožnil kanál uzavřít a získat zpět svůj podíl na finančních prostředcích. Tento proces je znám jako *vynucené uzavření*. Pokud by se však pokusili zveřejnit starší commitment transaction, odpovídající předchozímu stavu kanálu, kdy měli více sats, pak by tato transakce byla považována za pokus o podvod. V takovém případě může protistrana použít odvolávací klíč spojený s tímto starším stavem a získat zpět plnou výši prostředků v kanálu, zatímco podvodník je dočasně zablokován časovým zámkem.


Tento systém znamená, že zveřejnění starého stavu, tj. pokus o podvod, je velmi riskantní: pokud druhá strana uvidí tuto transakci v mempoolu nebo v blockchainu před vypršením časového zámku, může použít revokační klíč a získat zpět všechny prostředky. **Závisí tedy bezpečnost vašeho kanálu Lightning na vaší schopnosti odhalit pokus o podvod v časovém okně daném časovým zámkem**.



#### Proč jsou strážní věže nutné?



Sankční mechanismus funguje pouze tehdy, pokud je poškozená strana schopna:




- sledovat každý nový blok Bitcoin a zjišťovat, zda byl zveřejněn kanál commitment transaction;
- určit, zda tato transakce odpovídá poslednímu platnému stavu nebo odvolanému stavu;
- v případě odvolaného statusu včas odvysílat legální transakci a pomocí klíče odvolání získat zpět všechny prostředky před vypršením časového zámku.



![Image](assets/fr/023.webp)



V ideálním případě je váš uzel Lightning online 24 hodin denně, 7 dní v týdnu, je synchronizovaný a nepřetržitě monitoruje blockchain. Z tohoto důvodu může sám odhalit pokus o podvod a reagovat. V praxi se však osobní uzel Lightning může vypnout, zejména v případě delšího výpadku proudu nebo výpadku internetového připojení.



Právě v těchto obdobích odstávky se riziko stává reálným: pokud nepoctivý partner zveřejní starý stav v době, kdy je váš uzel offline, a časový zámek vyprší, aniž byste na to jakkoli reagovali, podvod se stává účinným. Přijdete o část nebo všechny své prostředky v kanálu.



Pro snížení tohoto rizika byly zavedeny přístroje Watchtower. Strážní věž je externí služba, která vaším jménem monitoruje blockchain, skenuje případné zveřejnění starého stavu na jednom z vašich kanálů a v případě potřeby automaticky vaším jménem odvysílá trestnou transakci. Takže i když váš uzel Lightning zůstane delší dobu offline, dokud je watchtower, kterou používáte, funkční, bude schopna chránit vaše finanční prostředky tím, že bude monitorovat případné pokusy o podvod a uplatní příslušnou sankci, jakmile ji zjistí.



#### Jak funguje strážní věž



Strážní věž je navržena tak, aby minimalizovala množství informací, které se dozví o vašich kanálech, a zároveň jí poskytla prostředky, které jí umožní jednat v případě problému:




- Pro každý nový stav kanálu s partnerem si váš uzel předem připraví potenciální sankční transakci. V případě, že by tento partner podváděl, tato transakce by vám umožnila získat zpět všechny prostředky v kanálu;
- Váš uzel pak tuto sankční transakci zašifruje pomocí TXID příslušného commitment transaction (toho, který by byl použit, kdyby se podvodník pokusil o podvod). Dokud nedojde k uzavření, nemůže strážní věž tuto transakci dešifrovat, protože nezná plně TXID podvodné transakce;
- Váš uzel odešle strážní věži paket obsahující zašifrovanou trestnou transakci a polovinu TXID potenciální podvodné transakce.



Protože TXID přenesený na strážní věž je neúplný, nemůže dešifrovat transakci spravedlnosti. Může však sledovat blockchain a hledat TXID, které odpovídá části, kterou vlastní. Pokud takovou transakci zjistí, pokusí se použít úplné TXID této transakce k dešifrování vaší transakce trestu. Pokud se dešifrování podaří, ví, že jde o pokus o podvod, a okamžitě pro vás trestnou transakci zveřejní.



![Image](assets/fr/024.webp)



Strážní věž proto nemá žádný přehled o podrobnostech vašich kanálů: ani o identitě vašich kolegů, ani o zůstatcích, ani o struktuře transakcí. Vidí pouze šifrované pakety. Jedinou informací, kterou může odvodit, je rychlost aktualizace vašich kanálů, protože pro každý nový stav obdrží paket, ale není schopna znát jeho obsah. V případě podvádění jistě zjistí informace o kanálech dešifrováním trestné transakce, ale alespoň bude vaše sats zachráněno.



Tento mechanismus je založen na kompromisu: na strážní věž delegujete možnost zveřejnit předem podepsanou sankční transakci, ale tato transakce zůstává pro strážní věž zcela neprůhledná, dokud nedojde k nějakému podvodu. Strážní věž nemůže měnit příjemce ani odklonit prostředky, protože má k dispozici pouze již podepsanou transakci s výstupy zmrazenými ve váš prospěch. Nemůže znát ani podrobnosti kanálu při legitimním vynuceném nebo kooperativním uzavření, protože TXID se neshodují. Na druhou stranu strážní věž zůstává minimálně důvěryhodnou třetí stranou: musíte se spolehnout, že bude online a že bude správně vysílat vaši transakci spravedlnosti, když ji budete potřebovat.



#### Stát se strážní věží



Teoreticky může jakýkoli uzel Lightning fungovat jako strážní věž pro jiné uzly (pokud používají stejnou implementaci, např. LND), přičemž sám je chráněn jinými uzly, které tuto roli hrají za něj. V následujících praktických částech vám ukážu, jak tento jednoduchý mechanismus nastavit na vašem LND pod Umbrel.


Zajímavou strategií by proto mohlo být domluvit se s důvěryhodnými přáteli bitcoinery, aby si navzájem dělali hlídací věž. Vy monitorujete jejich kanály a oni monitorují ty vaše.



### Najděte altruistickou strážní věž



Pokud ve svém okolí neznáte nikoho, kdo by vám mohl poskytnout službu strážní věže, existuje řada altruistických veřejných strážních věží, ke kterým se můžete připojit. Například v tomto kurzu LNP202 vám doporučuji připojit se ke službě strážní věže, kterou společně nabízejí LN+ a Voltage, což je strážní věž pro LND.


Zde jsou uvedeny přihlašovací údaje:



- Přes Tor:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



- Prostřednictvím služby clearnet:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@34.216.52.158:9911
```

Jako poděkování za poskytování této bezplatné služby Strážná věž můžete [přispět prostřednictvím Blesku](https://lightningnetwork.plus/donation).


Nyní, když používáme službu altruistické strážní věže, se podívejme, jak ji nakonfigurovat v uzlu LND v rámci Umbrel.


### Zřízení strážní věže


V aplikaci `Lightning Node` klikněte na tři tečky v pravém horním rohu rozhraní a vyberte možnost `Rozšířená nastavení`.


![Image](assets/fr/025.webp)


Poté přejděte do nabídky `Watchtower`.


![Image](assets/fr/026.webp)



Aktivujte možnost `Watchtower Client` a klikněte na tlačítko `UCHOVÁVAT A OBNOVIT UZEL`. Počkejte, až se LND restartuje.


![Image](assets/fr/027.webp)


Po dokončení restartu se vraťte do stejné nabídky a do příslušného pole zadejte ID vybrané altruistické strážní věže. Poté klikněte na tlačítko `ADD` a potvrďte. Můžete také upravit parametr `Sazba poplatku za prověrku klienta Watchtower`: jedná se o sazbu poplatku, kterou jste ochotni zaplatit za případnou transakci spravedlnosti vysílanou strážní věží. Není třeba volit příliš vysokou sazbu, ale měli byste se vyvarovat i příliš nízké sazby, jinak nebude právní transakce potvrzena včas.


Restartujte uzel pomocí tlačítka `UCHOVAT A RESTARTOVAT UZEL`, aby se tyto změny uplatnily.


![Image](assets/fr/028.webp)



Pokud se vrátíte do stejné nabídky, uvidíte, že váš uzel Lightning je nyní chráněn právě přidanou strážní věží.



![Image](assets/fr/029.webp)



Altruistická strážní věž je obecně dostačující, zejména pokud na svůj bleskový uzel nevkládáte velké množství peněz a pokud svůj uzel dobře spravujete (nenecháváte ho vypnutý příliš dlouho). Pro ještě větší bezpečnost jich můžete opakováním stejného postupu přidat i několik.



## Otevření prvního kanálu Lightning


<chapterId>00642af7-8f3d-4a25-96d7-34e85de7bd5d</chapterId>



Pokud jste se dostali až sem, už víte, že uzel Lightning bez kanálu je něco jako prázdný wallet: existuje, ale je k ničemu. Abyste mohli odesílat nebo přijímat platby, musí být váš uzel připojen k alespoň jednomu dalšímu uzlu v síti Lightning prostřednictvím kanálu. Do budoucna důrazně doporučujeme otevřít několik kanálů, a to z důvodu odolnosti a efektivity směrování. V následujících kapitolách se také podíváme na to, jak spravovat likvidní aktiva, optimalizovat topologii kanálů a používat pokročilejší nástroje, než je základní rozhraní LND na Umbrel.



Cílem této úvodní kapitoly je však jednoduše pochopit, jak si vybrat dobrý partnerský server Lightning, kde najít informace potřebné pro výběr partnerských serverů a jak otevřít první kanál prostřednictvím základního rozhraní LND.



### Jak si vybrat dobrého vrstevníka Lightning?



Při otevírání kanálu je třeba vybrat partnera: jiný uzel Lightning, ke kterému bude váš uzel přímo připojen prostřednictvím kanálu. Tato volba peera je důležitá, protože bude mít přímý vliv na:




- snadné vyhledávání vašich plateb;
- spolehlivost vašich kanálů v průběhu času;
- náklady na směrování.



Neexistuje dokonalá volba pro každého, ale existuje řada spolehlivých kritérií pro identifikaci vhodných kandidátů.



#### 1. Připojení uzlů



Dobrý partner je uzel, který je dobře připojen k síti Lightning. To znamená nejen mít velký počet kanálů (i když i to může být ukazatelem), ale především být propojen s dalšími spolehlivými uzly a zaujímat dostatečně centrální pozici v síťovém grafu.



Dobře propojený uzel zvyšuje šance na nalezení efektivní cesty k většině cílů plateb. Snižuje také počet potřebných zprostředkujících uzlů, což snižuje náklady.



Naopak otevření prvního kanálu do izolovaného nebo slabě připojeného uzlu může omezit vaše možnosti: tomuto partnerovi budete moci zaplatit, ale bude mnohem těžší zaplatit zbytku sítě.



#### 2. Kapitalizace a kapacita kanálu



Dobrý peer je také dostatečně kapitalizovaný uzel. To se pozná podle jeho celkové kapacity kanálů (součet sats přidělených všem jeho kanálům) a průměrné kapacity kanálů (často je lepší mít jen několik dobře kapitalizovaných kanálů než mnoho malých).



Uzel se směšnou kapacitou nebo s malými kanály nebude schopen směrovat platby s velkými částkami, což bude mít za následek selhání směrování.



#### 3. Výdajové zásady



Každý uzel si nastavuje vlastní poplatky za směrování (`základní poplatek` a `sazbu poplatku`). Dobrý partner si nebude účtovat přemrštěné poplatky za strategické kanály. Pro první kanál je nejlepší zvolit uzel se spíše mírnými poplatky, abyste nehandicapovali vlastní platby.



Nezapomeňte, že vaše vlastní poplatky za směrování také ovlivňují to, jak vás ostatní vnímají jako rovnocenného partnera: uzel, který neustále mění své poplatky nebo zavádí absurdní náklady, je málokdy oceňován.



#### 4. Stabilita a seniorita



Velmi důležitým kritériem je vzájemná stabilita. Dobrý uzel má vysoký uptime (je velmi zřídka offline), udržuje své kanály dlouho otevřené a bezdůvodně je neustále neotevírá/neuzavírá.



Staré a stále aktivní kanály jsou dobrým signálem: naznačují, že vztah je pro peera ziskový, že uzel umí hospodařit se svým kapitálem a že se kdykoli neuzavře, takže nemusíte neustále platit onchain poplatky za uzavření a opětovné otevření.



Naopak partner, který je často offline nebo který rychle uzavírá kanály, může být zdrojem problémů a dalších nákladů na otevření nových kanálů.



Ani s těmito kritérii neuděláte dokonalou volbu hned napoprvé. To je normální: skutečnou kvalitu peerů odhalí až jejich používání. Proto je důležité:




- sledovat aktivitu kanálu (směrované objemy, dostupnost atd.);
- zavřít kanály, které neslouží k žádnému účelu nebo jejichž kolegové jsou příliš často offline;
- časem přerozdělit svůj kapitál k lepším partnerům.



Smyslem není každý den otevírat a zavírat kanály (což by bylo nákladné z hlediska nákladů na řetězec), ale postupně rozvíjet topologii tak, aby konvergovala k souboru spolehlivých, dobře propojených partnerů kompatibilních s vašimi potřebami.



### Jak najdu vrstevníka?



K uplatnění těchto kritérií budete potřebovat nástroje, které poskytují přehled o síti Lightning. K tomu je k dispozici několik průzkumníků a služeb. Mezi nejznámější průzkumníky Lightning patří [1ML](https://1ml.com/) a [Amboss](https://amboss.space/).



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017

https://planb.academy/tutorials/node/lightning-network/1ml-37ada2ab-7a24-4473-87fd-007cb7640e7b

Zde však doporučuji použít [nástroj Lightning Terminal od Lightning Labs](https://terminal.lightning.engineering/), který poskytuje žebříček (pravda, založený na částečně subjektivních kritériích) uzlů Lightning považovaných za nejvhodnější pro otevření kanálu.



![Image](assets/fr/030.webp)



Problém s velmi velkými uzly Lightning na vrcholu tohoto žebříčku spočívá v tom, že většina z nich nepřijímá otevření kanálu pod velmi vysokou částkou. Mnohé z nich také uplatňují přísné zásady správy peerů, což může vést k uzavření vašeho kanálu. Na druhou stranu tyto uzly obecně nemají vzhledem k počtu připojení potřebu příchozí likvidity.



Proto bych vám doporučil, abyste se při sestavování žebříčku snažili najít uzel, který je dobře propojený, spolehlivý a dostatečně centrální v síťovém grafu, aniž by byl příliš velký. Zde jsem například identifikoval uzel Lightning na stacker.news, který je velmi dobře připojen, má vysokou kapacitu a zaujímá centrální pozici v síťovém grafu.



![Image](assets/fr/031.webp)



Dalším zajímavým přístupem je otevřít kanál k uzlu, který potřebuje příchozí likviditu, například ke známému obchodníkovi, sdružení nebo komunitě. Tato strategie má tři výhody:




- Protože vybraný subjekt potřebuje příchozí likviditu, bude mít logicky menší motivaci váš kanál bezdůvodně uzavřít;
- Jeho ekonomická aktivita zvyšuje šance na směrování tímto kanálem, a tedy i na výběr některých poplatků;
- Děláte ekosystému laskavost a cenný příspěvek ostatním bitcoinářům.



Jakmile identifikujete příslušný uzel, můžete získat jeho ID uzlu. Jedná se o jednoduchý součet veřejného klíče uzlu, oddělovače `@`, jeho IP adresy nebo adresy Tor a použitého portu. Toto ID je snadno dostupné z profilu uzlu v libovolném průzkumníku Lightning.



### Otevření prvního kanálu prostřednictvím LND



Nyní, když jsme určili uzel, pomocí kterého otevřeme náš první kanál, potřebujeme, aby se k němu uzamkl modul sats. Za tímto účelem je třeba přivést uzel Bitcoin na řetězec wallet spojený s vaším uzlem LND.



V hlavním rozhraní LND vyhledejte svůj počítač `Bitcoin Wallet` a klikněte na tlačítko `Vložit`. Příjemní adresa v řetězci je pak generated: odešlete na ni sats. Množství, které musíte převést, závisí na kapacitě, kterou chcete přidělit prvnímu kanálu, ale mějte na paměti, že musíte poslat o něco více, než je cílová kapacita. Například pokud chcete otevřít kanál s kapacitou 500 000 sats, neposílejte přesně 500 000 sats, ale vyšší částku.



![Image](assets/fr/032.webp)



Jakmile je transakce odvysílána, zobrazí se v rozhraní. Před otevřením kanálu vyčkejte na potvrzení. Po potvrzení se vedle ní zobrazí zelená šipka.



![Image](assets/fr/033.webp)



Přejděte dolů na hlavní rozhraní a klikněte na `+ OTEVŘÍT KANÁL`.



![Image](assets/fr/034.webp)



Zadejte `ID uzlu` uzlu, se kterým chcete otevřít kanál, uveďte částku, kterou chcete uzamknout, a poté upravte poplatek za úvodní transakci podle stavu trhu s poplatky na řetězci. Samozřejmě se předem ujistěte, že máte v portfoliu onchainu LND dostatek prostředků.



Po nastavení všech parametrů klikněte na tlačítko `OPEN CHANNEL`.



![Image](assets/fr/035.webp)



Počkejte na potvrzení úvodní transakce v řetězci. Váš první kanál je nyní oficiálně v provozu: gratulujeme!



Vidíte, že v tuto chvíli je 100 % likvidity kanálu na mé straně: to je normální, protože jsem to já, kdo kanál otevřel. S vývojem plateb a směrování se toto rozložení bude měnit, ale celková kapacita kanálu zůstane vždy stejná.



![Image](assets/fr/036.webp)



Nyní, když máte kanál, můžete provádět první platby Lightning, pokud je vybraný uzel správně připojen k síti. V dalších kapitolách se samozřejmě podíváme na to, jak nastavit pohodlnější způsob placení faktur Lightning z mobilu. Prozatím si však vyzkoušejme provést první platbu přímo z účtu LND do účtu Umbrel.



Za tímto účelem klikněte v části `Lightning Wallet` na tlačítko `Odeslat` a poté vložte fakturu, kterou chcete nastavit.



![Image](assets/fr/037.webp)



Zobrazí se částka faktury. Potvrďte platbu kliknutím na tlačítko `Odeslat`.



![Image](assets/fr/038.webp)



Pokud je nalezena platná trasa, měla by být první platba blesku úspěšná.



![Image](assets/fr/039.webp)



Pokud se pak podíváme na rozložení likvidity v kanálu, zjistíme, že můj kolega má nyní na své straně 5 002 sats. To odpovídá 5 000 sats z platby, kterou jsem právě provedl a kterou směroval do uzlu příjemce. Další 2 sats představují poplatky za směrování, které jsem zaplatil, protože příjemce obdržel přesně 5 000 sats.



![Image](assets/fr/040.webp)



Pro zvýšení spolehlivosti našich plateb bude zřejmě nutné otevřít další kanály. V závislosti na našich cílech budeme muset také najít způsob, jak zpřístupnit příchozí likviditu, abychom mohli přijímat platby na platformě Lightning. To bude předmětem další části.



# Správa uzlu Lightning


<partId>e27c3e1e-487b-4414-ad6b-d67bdb91c7c5</partId>



## Definujte profil operátora uzlu


<chapterId>d3b2e163-50f6-4d1d-a5fc-8fd177dfac76</chapterId>



Nyní, když je váš uzel Lightning spuštěn, je dalším krokem definování profilu obchodníka. To je důležitá volba, protože určuje vaši strategii otevírání kanálů, typ partnerů, které preferujete, a způsob, jakým spravujete likviditu.



Aby to fungovalo, potřebujete likviditu správným směrem. Odchozí likvidita odpovídá vaší schopnosti platit (sats dostupné na vaší straně kanálů). Příchozí likvidita odpovídá vaší schopnosti přijímat (sats dostupný na straně vašich partnerů). Jinými slovy, váš profil se omezuje na jednoduchou otázku: Většinu času váš sats z vašeho uzlu odchází, nebo do něj přichází?



### Spotřebitel



To je profil naprosté většiny uživatelů. Svůj uzel používáte k provádění plateb prostřednictvím služby Lightning: k nákupu zboží a služeb, placení účtů, posílání spropitného - zkrátka k používání služby Lightning jako rychlého platebního prostředku. Na druhou stranu z Lightningu dostáváte málo nebo jen okrajově, například několik darů, vrácení peněz mezi přáteli nebo několik mikroplateb.



Tento profil je nejjednodušší na správu, protože vaší hlavní potřebou je mít možnost platit. V praxi to znamená, že potřebujete odchozí likviditu. Jakmile otevřete jeden nebo více správně dimenzovaných kanálů do stabilních, dobře propojených uzlů, vaše odchozí platby budou mechanicky přesouvat likviditu na druhou stranu vašich kanálů. Právě tento pohyb přirozeně vytváří přiměřené množství příchozí likvidity. Výsledkem je, že i když nechcete přijímat pravidelně, budete moci čas od času přijímat, aniž byste museli implementovat složitou strategii. Nemusíte se tedy obávat o svou příchozí likviditu.



V tomto kurzu LNP202 se zaměříme na tento "spotřebitelský" profil operátora uzlu, protože odpovídá téměř všem uživatelům Bitcoin v systému Lightning.



### Maloobchodní prodejce



Obchodník je svým způsobem opakem spotřebitele. Zde není hlavním cílem platit, ale inkasovat. Podnik, poskytovatel služeb, internetový obchod nebo prodejní místo, které přijímá bleskové platby, bude z tohoto uzlu přijímat mnoho příchozích plateb a provádět relativně málo odchozích plateb.



Tento profil je náročnější, protože odmítnutá platba v systému Lightning představuje potenciálně ztracený prodej. Prioritou se proto stává příchozí likvidita. Pokud váš uzel nemá dostatek příchozí likvidity, vaši zákazníci uvidí, že jejich platby selhávají, i když mají finanční prostředky, jednoduše proto, že neexistuje cesta, jak k vám dostat likviditu správným směrem.



Hlavní výzvou pro obchodníka je také přirozený vývoj kanálů. Pokud budete pouze přijímat, vaše kanály se postupně zaplní na vaší straně. Potřebujete tedy mechanismy pro udržování a obnovování příchozí likvidity.



Existuje však i jednodušší případ: smíšený profil spotřebitele a obchodníka. Pokud inkasujete v systému Lightning, ale také utrácíte v systému Lightning (obchodní výdaje, platby dodavatelům nebo dokonce osobní výdaje), pak se vaše odchozí platby přirozeně obnovují v příchozích. Řízení se stává plynulejším, protože toky se vzájemně vyrovnávají, a vy nemáte tak potřebu uchylovat se k umělým mechanismům určeným výhradně k obnovení příchozí likvidity.



### Směrovač



Směrovač je specifický profil. Nepoužívá svůj uzel Lightning k placení nebo vybírání poplatků, ale ke směrování plateb jiných lidí a vybírání poplatků. Cílem je být užitečnou, spolehlivou a ekonomicky konkurenceschopnou trasou v rámci grafu Lightning.



Upřímně řečeno, být routerem v Lightningu je složitější, než se zdá, a je těžké dosáhnout ziskovosti. Především otevírání a zavírání kanálů je drahé v onchain nákladech. Abyste mohli efektivně směrovat, musíte často upravovat topologii, testovat, uzavírat málo výkonné kanály, otevírat nové a pravidelně vyvažovat likviditu. Zadruhé, konkurence je tvrdá: velké, zavedené uzly přirozeně získávají velký podíl provozu a je obtížné se prosadit bez vázání značného kapitálu v dobře dimenzovaných kanálech.



Je zde také vysoká provozní náročnost. Směrovací uzel musí být extrémně stabilní, monitorovaný, řádně zálohovaný a důsledně spravovaný. Musíte sledovat výkonnost kanálu, přizpůsobovat poplatkovou politiku, udržovat vyváženou likviditu, spravovat partnery a rychle řešit technické problémy. Tato úroveň zapojení může být zajímavá jako technický koníček nebo jako příspěvek k infrastruktuře, ale pokud je vaším cílem jednoduše suverénně používat Lightning, dostat se do směrování kvůli vydělávání peněz je málokdy relevantní. Proto se tento kurz LNP202 nezabývá tímto profilem do hloubky.



### Než se pustíte do dalšího postupu, jasně se zařaďte do situace



Pokud odpovídáte profilu spotřebitele, bude pro vás prioritou možnost spolehlivého placení s jednoduchou správou. Jste-li obchodník, vaší prioritou bude bezchybné inkaso, což předpokládá strategii získávání příchozí likvidity. Pokud uvažujete o směrování, musíte k němu přistupovat jako k náročné, ekonomicky nejisté a časově náročné činnosti.



Definování tohoto profilu vám pomůže vyhnout se klasickému úskalí: použití strategie kanálů určené pro obchodníka nebo směrovač, i když jste pouze uživatel, který chce platit.



## Použití správce uzlů Lightning


<chapterId>02eb4c09-d14b-4ff0-8b04-b90de3307d34</chapterId>



V předchozí části tohoto školení LNP202 jsme používali základní rozhraní aplikace `Lightning Node` na Umbrel. Toto rozhraní je dostatečné pro základní operace (kontrola zůstatků, zobrazení rozdělení hotovosti, otevírání a zavírání kanálů), ale je záměrně velmi zjednodušené. Tato jednoduchost omezuje dostupné možnosti a neumožňuje přístup k mnoha pokročilým funkcím uzlu LND. Z tohoto důvodu budeme nyní používat jiný, komplexnější software pro správu uzlu Lightning.



Tento dodatečný software bude pouze doplňkovým rozhraním pro správu uzlu. To znamená, že můžete nadále paralelně používat rozhraní `Lightning Node`, a pokud chcete, můžete používat i několik různých rozhraní. Jedná se jednoduše o různé způsoby interakce se stejným uzlem Lightning.



Mezi nejznámější programy patří:




- [Alby Hub](https://albyhub.com/);
- [Ride The Lightning](https://www.ridethelightning.info/);
- [ThunderHub](https://thunderhub.io/).



Všechna tři řešení jsou dobrá. Pokud si přejete, můžete si všechna tři řešení vyzkoušet na svém uzlu, než si vyberete to, které vám bude nejlépe vyhovovat. Osobně používám ThunderHub ze zvyku a proto, že se mi zdá úplnější než ostatní. Tento nástroj budu prezentovat v tomto školení, ale můžete si vybrat i jednu z dalších dvou alternativ. Pro každý z těchto programů máme na stránkách Plan ₿ Academy speciální výukový kurz.



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

https://planb.academy/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

### Instalace ThunderHub



Všechny tyto programy lze velmi snadno nainstalovat z obchodu s aplikacemi Umbrel. Jak jsem již řekl, budeme zde používat program ThunderHub, ale pokud byste chtěli později vyzkoušet jiný, postup bude podobný.



![Image](assets/fr/041.webp)



Umbrel poskytuje výchozí heslo pro přístup ke ThunderHub. Zkopírujte si ho: budete ho hned potřebovat. Nezapomeňte si ho také uložit do správce hesel, protože po každém otevření softwaru budete o něj požádáni.



![Image](assets/fr/042.webp)



Klikněte na `Přihlášení` a vložte heslo, které vám poskytl Umbrel, abyste se přihlásili.



![Image](assets/fr/043.webp)



Poté budete přesměrováni na domovskou stránku ThunderHub, kde se zobrazí hlavní informace o uzlu Lightning.



![Image](assets/fr/044.webp)



Pro začátek doporučuji aktivovat dvoufaktorové ověřování (2FA). V nastavení jednoduše klikněte na `Povolit` vedle položky `Povolit 2FA` a poté postupujte podle obvyklého postupu.



![Image](assets/fr/045.webp)



### Použití ThunderHub



ThunderHub je poměrně snadné se naučit. Všechny nabídky jsou přístupné z levého sloupce rozhraní. Pro shrnutí uvádíme, co jednotlivé nabídky dělají:




- home: přehled uzlů, bilance a rychlé akce;
- přístrojový panel: přizpůsobitelný přístrojový panel s widgety a metrikami;
- peers: zobrazení a správa připojení k jiným uzlům Lightning;
- kanály": kompletní správa kanálů (likvidita, poplatky, uzavření atd.);
- rebalance": nástroj pro obnovení rovnováhy kanálů prostřednictvím kruhových plateb;
- transakce: historie odeslaných a přijatých plateb Lightning;
- forwards`: statistiky směrování a náklady generated vašeho uzlu;
- `Chain`: Bitcoin onchain wallet (UTXO a transakce);
- integrace gW-201 pro monitorování a zálohování;
- `Nástroje`: pokročilé nástroje (zálohování, sestavy, makra, podpisy atd.);
- výměna: Výměna blesků/řetězců prostřednictvím Boltz;
- `Stats`: celkové statistiky a výkon uzlu Lightning.



Díky této sadě funkcí máte k dispozici všechny nástroje, které potřebujete k efektivní správě uzlu Lightning. Není nutné hned podrobně zvládnout všechny možnosti: budeme se jimi zabývat postupně v průběhu tohoto kurzu. Pokud se však chcete s programem seznámit hlouběji, podívejte se na náš výukový kurz ThunderHub:



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

Nejvíce nás zajímá nabídka `Kanály`. Nabízí podrobné zobrazení všech kanálů ve vašem uzlu s rozdělením jejich likvidity. Konkrétně můžete vidět, které kanály jsou otevřené v `Open`, které čekají na otevření nebo uzavření v `Pending` a které jsou již uzavřené v `Closed`.



![Image](assets/fr/047.webp)



Pro daný kanál můžete kliknutím na jeho název nebo ID kanálu otevřít jeho stránku Amboss a získat další informace. Můžete také kliknout na ikonu tužky a upravit parametry kanálu, včetně poplatkové politiky uplatňované na tento kanál, pokud váš uzel směruje platby do uzlu vašeho partnera.



![Image](assets/fr/048.webp)



Pokud svůj uzel Lightning používáte hlavně jako "spotřebitel", nemusíte tyto poplatky měnit: můžete ponechat výchozí hodnoty. Na druhou stranu, pokud chcete lépe porozumět tomu, jak směrovací poplatky v systému Lightning fungují, doporučuji školení LNP 201, a to zejména kapitolu 4.1:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Kliknutím na malý křížek vedle kolegy můžete iniciovat uzavření kanálu. Pokud si například všimnete, že je partner pravidelně neaktivní, může být vhodné tento kanál uzavřít a přesunout tak svůj kapitál ke spolehlivějšímu partnerovi.



Pak máte dvě možnosti. První a vždy preferovanou možností je uzavření spolupráce. Potvrzením této akce váš uzel požádá kolegu o společné uzavření kanálu. Pokud souhlasí, můžete odvysílat uzavírací transakci v řetězci a získat zpět svůj podíl prostředků. Výhodou tohoto způsobu je, že si vyberete poplatky za transakci v onchainu, čímž se vyhnete zbytečným nákladům, a že prostředky získáte zpět rychleji, bez časového zámku.



![Image](assets/fr/049.webp)



Druhou možností je nucené uzavření. V tomto případě nežádáte o souhlas partnera a přímo odvysíláte poslední commitment transaction, který máte k dispozici. Tuto metodu bych nedoporučoval, pokud se nejedná o poslední možnost, například pokud partner systematicky odmítá uzavírání spolupráce nebo již neodpovídá. Vynucené uzavření má dvě hlavní nevýhody: poplatky jsou často velmi vysoké, protože byly předem stanoveny tak, aby předvídaly nárůst poplatků v řetězci, a dochází ke zpoždění při vymáhání prostředků, protože jsou blokovány časovým zámkem. Tento timelock dává vašemu partnerovi čas na reakci v případě pokusu o podvod (což samozřejmě není tento případ, ale i tak musíte počkat).



![Image](assets/fr/050.webp)



Chcete-li otevřít nový kanál, přejděte do nabídky `Home` a klikněte na `Otevřít kanál` v části `Liquidity`. Poté budete moci zadat ID vybraného uzlu, kapacitu kanálu, požadovaný poplatek za směrování Lightning a poplatek za otevření transakce v řetězci.



![Image](assets/fr/051.webp)



Toto jsou hlavní úkony, které je třeba provést v systému ThunderHub. Další funkce objevíme v průběhu tohoto kurzu LNP202.



## Získání příchozí likvidity


<chapterId>b740c656-a897-4d95-af4b-116b718447cd</chapterId>



Jak vidíte, mít odchozí likviditu k provádění plateb na účet Lightning není nijak zvlášť složité. Stačí z vlastní iniciativy otevřít kanály do jiných uzlů a začít posílat sats. Na druhou stranu mít příchozí likviditu k přijímání plateb na Lightning je složitější, protože buď potřebujete, aby vám jiné uzly otevřely kanály, nebo musíte likviditu přesunout sami provedením plateb.



Pokud si zvolíte "spotřebitelský" profil, nemusíte se obecně starat o příchozí likviditu. Vaše používání uzlu Lightning bude převážně zaměřeno na platby, nikoli na příjem hotovosti. Prostým provedením několika plateb v uzlu Lightning si časem přirozeně vytvoříte příchozí likviditu.



Na druhou stranu, pokud máte profil "obchodníka", je situace opačná: budete hlavně vybírat platby a jen málo z nich provádět. Nemůžete se tedy spoléhat pouze na vlastní platby, pokud jde o příchozí likviditu. Proto je nutné, aby ostatní uzly Lightning otevřely kanály k tomu vašemu. Jak toho však lze dosáhnout? Jak přimět ostatní provozovatele, aby pro vás vázali kapitál? Právě to budeme zkoumat v této kapitole.



### Nákup příchozí likvidity



Jak se dalo očekávat, nejúčinnějším způsobem, jak někoho přimět k jednání, je zaplatit mu. U příchozí likvidity do vašeho uzlu Lightning je princip naprosto stejný. Nejjednodušší způsob, jak dostat kanály do svého uzlu, je zaplatit za službu a s ní spojené vázání kapitálu.



Pokud jste firma nebo maloobchodní prodejce, tento přístup znamená, že můžete rychle získat spolehlivé kanály pro výběr plateb od zákazníků bez zbytečného tření.



Existuje mnoho způsobů nákupu příchozí likvidity. Osobně používám a doporučuji platformu Amboss [Magma](https://magma.amboss.tech/). Její používání je velmi snadné, otevření kanálu je rychlé a sazby jsou obecně rozumné. Magma funguje jako tržiště s tvůrci a odběrateli, ale verze 2 tuto zkušenost výrazně zjednodušila: stačí vytvořit požadavek, zaplatit cenu prostřednictvím Lightningu a Magma jej automaticky porovná s nejlepší dostupnou nabídkou. Po šesti potvrzeních na řetězci je váš kanál s příchozí likviditou spuštěn. Takto to funguje:



Přejděte na [webové stránky společnosti Magma](https://magma.amboss.tech/buy) v sekci `Koupit kanály`.



![Image](assets/fr/052.webp)



Pokud si přejete, můžete si vytvořit účet pro sledování svých nákupů, ale není to povinné. Pokud si účet nevytvoříte, společnost Magma vám jednoduše poskytne ID relace, které vám později umožní načíst vaše nákupy.



Po vstupu na stránky vyplňte údaje potřebné k nákupu likvidity. Pro jednorázový nákup vyberte možnost `Jednorázový` a zadejte částku, kterou jste ochotni za příchozí likviditu zaplatit. Čím vyšší je zaplacená částka, tím větší kapacita kanálu se otevře vašemu uzlu. Níže se zobrazuje odhad kapacity kanálu: jedná se o přibližnou hodnotu, protože konečná částka bude záviset na nejlepší nabídce nalezené systémem Magma, která je někdy vyšší, jindy nižší.



![Image](assets/fr/053.webp)



Poté zadejte ID uzlu. Najdete ho například v nabídce `Node ID` aplikace `Lightning Node` na Umbrel.



![Image](assets/fr/054.webp)



Po vyplnění všech údajů klikněte na tlačítko `Přezkoumat a otevřít objednávku`.



![Image](assets/fr/055.webp)



Pokud jste si účet nevytvořili, Magma vám poskytne klíč relace a záložní soubor. Tyto dvě položky si uschovejte na bezpečném místě, protože vám umožní získat objednávku později nebo sledovat její stav v případě problému. Po uložení souboru klikněte na tlačítko `Platit bleskem`.



![Image](assets/fr/056.webp)



Magma poté vystaví fakturu generate Lightning na vámi zvolenou částku. Tu musíte zaplatit. Pokud již máte na svém uzlu Lightning kanály, můžete platit přímo z něj nebo použít jiný externí Lightning wallet.



![Image](assets/fr/057.webp)



Po provedení platby se transakce zobrazí v rozhraní Magma jako zpracovaná.



![Image](assets/fr/058.webp)



Po několika minutách je požadavek zpracován: je otevřen kanál s sats do vašeho uzlu Lightning. Jakmile je otevírací transakce potvrzena v řetězci, získáte přístup k odpovídající příchozí likviditě.



![Image](assets/fr/059.webp)



Magma je také integrována přímo do systému ThunderHub. Na kartě `Home` přejděte dolů do sekce `Liquidity` a klikněte na `Koupit příchozí Liquidity`. Stačí zadat požadované množství a potvrdit. Žádné faktury nemusíte platit ručně, protože ThunderHub se o platbu z vašeho uzlu postará automaticky.



![Image](assets/fr/060.webp)



Pokud jste obchodník, je tento typ služby obzvláště vhodný, protože vám umožňuje rychle získat velké množství příchozí likvidity ze spolehlivých uzlů, což zaručuje, že vám vaši zákazníci budou moci bez problémů zaplatit. Na druhou stranu, pokud jste soukromá osoba nebo pokud nechcete za příchozí likviditu platit, existují také bezplatná řešení. Pojďme se na ně podívat.



### Kooperativní příchozí likvidita



Pokud nejste obchodník, ale přesto potřebujete nějakou příchozí likviditu (například na spuštění uzlu, zatímco čekáte na nějaké platby), nemusíte za ni nutně platit. Jedním z mnou preferovaných řešení je spolupráce s ostatními provozovateli uzlů, kteří také potřebují příchozí likviditu, a vzájemné otevření kanálů Lightning. Tímto způsobem vám otevření kanálu přinese odchozí likviditu a zároveň vám poskytne příchozí likviditu, a to zdarma (modulo onchain poplatky za otevření).



Můžete se samozřejmě domluvit přímo s ostatními bitcoinery. Existuje však platforma určená pro tento typ kruhového otevírání: [Lightning Network+](https://lightningnetwork.plus/). Principem je neotevírat dva kanály mezi stejnými lidmi, ale zřídit kruhové otevření zahrnující minimálně tři účastníky, nebo i více.



Podívejme se na příklad, abychom pochopili, jak Lightning Network+ funguje:




- Provozovatel uzlu jménem `A` zveřejní oznámení, že si přeje otevřít kanál sats o hodnotě 1 milion dolarů s dalšími dvěma lidmi;
- Inzerát zůstává aktivní, dokud se nepřidají další účastníci;
- Později se k oznámení uzlu `A` připojí dva operátoři, `B` a `C`. Trojúhelník je nyní kompletní a fáze otevření může začít.
- Uzel `A` otevře kanál do uzlu `B`;
- Uzel `B` otevře kanál do uzlu `C`;
- Uzel `C` otevře kanál do uzlu `A`.



Na konci operace má každý uzel 1 milion sats odchozí likvidity a 1 milion sats příchozí likvidity. Toto schéma lze rozšířit na čtyři nebo pět účastníků.



Samozřejmě neexistuje žádný technický mechanismus, který by zaručil, že účastník skutečně otevře kanál, který se zavázal vytvořit. Proto platforma zřídila systém reputace, založený na pozitivních hodnoceních, když provozovatelé splní své závazky. A v nejhorším případě, pokud narazíte na někoho, kdo nespolupracuje, nepřijdete o žádné peníze: prostě jen propásnete příležitost k příchozí likviditě.



Toto řešení je vhodné zejména pro "spotřebitelský" profil, protože umožňuje získat příchozí likviditu zdarma a zároveň propojit váš uzel s dalšími malými operátory. Na druhou stranu, pokud jste obchodník, není tento přístup obecně relevantní: každý sat příchozí likvidity vyžaduje zablokování sat odchozí likvidity a vaše velké potřeby příchozí likvidity by pak znamenaly vázání příliš velkého kapitálu.



Chcete-li používat aplikaci Lightning Network+, máte dvě možnosti: buď použít aplikaci integrovanou do Umbrel, nebo použít klasickou webovou stránku a vytvořit si účet přihlášením z uzlu. Doporučuji druhou možnost, protože integrovaná aplikace nenabízí celou škálu dostupných funkcí.



Přejděte na webové stránky [Lightning Network+](https://lightningnetwork.plus/) a klikněte na tlačítko `Přihlášení` v pravém horním rohu rozhraní.



![Image](assets/fr/061.webp)



Chcete-li se ověřit, musíte poskytnutou zprávu podepsat pomocí soukromého klíče uzlu Lightning. Pomocí ThunderHub je tato operace velmi jednoduchá. Začněte zkopírováním zprávy zobrazené modulem LN+.



![Image](assets/fr/062.webp)



V programu ThunderHub přejděte na kartu `Nástroje` a v části `Zprávy` klikněte na tlačítko `Podepsat`.



![Image](assets/fr/063.webp)



Vložte ověřovací zprávu poskytnutou společností LN+ a klikněte na tlačítko `Podepsat`.



![Image](assets/fr/064.webp)



ThunderHub pak tuto zprávu podepíše pomocí soukromého klíče vašeho uzlu. Zkopírujte podpis generated.



![Image](assets/fr/065.webp)



Vložte tento podpis do příslušného pole na webu LN+ a klikněte na tlačítko `Přihlásit se`.



![Image](assets/fr/066.webp)



Nyní jste připojeni ke LN+ pomocí uzlu Lightning. Tento proces umožňuje společnosti LN+ ověřit, že jste právoplatným vlastníkem uzlu, který uplatňujete na její platformě.



![Image](assets/fr/067.webp)



Pokud chcete, můžete si svůj profil LN+ přizpůsobit, například přidáním krátkého životopisu.



Chcete-li se zúčastnit prvního otevření kruhového kanálu, přejděte do nabídky `Swaps` v horní části rozhraní. Zde najdete všechny aktuálně dostupné swapy v závislosti na vlastnostech vašeho uzlu.



![Image](assets/fr/068.webp)



Chcete-li se připojit k existující nabídce swapu, jednoduše na ni klikněte a zaregistrujte se. V systému LN+ však může tvůrce swapu účastníkům stanovit určité podmínky, například minimální počet kanálů nebo minimální celkovou kapacitu uzlu. Je proto možné, zejména v počátečních dnech, že pro váš uzel bude k dispozici jen málo nabídek. V mém případě i přes několik již otevřených kanálů nebyly pro můj uzel k dispozici žádné nabídky. Vytvořil jsem si tedy vlastní výměnu, a pokud jste ve stejné situaci, můžete udělat totéž.



Klikněte na `Start Liquidity Swap` a zadejte parametry nabídky:




- Zvolte celkový počet účastníků (3, 4 nebo 5);
- Uveďte počet kanálů, které mají být otevřeny (ujistěte se, že máte v řetězci wallet alespoň toto množství);
- Definujte dobu otevření kanálu. Jedná se o dobu, během níž se účastníci dohodnou, že je nebudou uzavírat;
- Vpravo můžete nastavit omezení pro účastníky: minimální počet kanálů, minimální celkovou kapacitu a typ přijímaného připojení.



Po nastavení všech parametrů klikněte na tlačítko `Start Liquidity Swap`.



![Image](assets/fr/069.webp)



Vaše nabídka výměny byla vytvořena. Nyní stačí počkat, až se přihlásí další provozovatelé uzlů. Pokud nejsou vaše podmínky příliš omezující, nemělo by to trvat příliš dlouho. Nezapomeňte v následujících hodinách nebo dnech sledovat stav swapu.



![Image](assets/fr/070.webp)



Všechna výměnná místa byla obsazena: nyní přecházíme do fáze otevírání kanálů. Každý účastník vidí na svém rozhraní LN+, ke kterému uzlu má otevřít kanál Lightning.



![Image](assets/fr/084.webp)



Na své straně otevřete kanál pomocí ID uzlu poskytnutého společností LN+ a dodržujte uvedenou částku. Jak jsme viděli v předchozích kapitolách, můžete to provést buď prostřednictvím ThunderHub, pomocí jiného správce uzlů Lightning, nebo přímo ze základního rozhraní aplikace Lightning Node.



![Image](assets/fr/085.webp)



Po spuštění se otevření zobrazí v části čekajících kanálů. V mém případě je to kanál s uzlem `Plebian_fr`.



![Image](assets/fr/086.webp)



Poté se můžete vrátit do LN+ a potvrdit, že jste zahájili otevření kanálu. Stačí kliknout na tlačítko `Otevření kanálu zahájeno`.



![Image](assets/fr/087.webp)



Až všichni ostatní účastníci také otevřou kanál, ke kterému se zavázali, nezapomeňte jim zanechat pozitivní hodnocení.



![Image](assets/fr/088.webp)



V případě potíží nebo zpoždění se můžete obrátit přímo na své kolegy prostřednictvím komentářů v dolní části stránky.



![Image](assets/fr/089.webp)



Někteří účastníci si mohou přát vyvážit oběhové kanály od samého počátku tím, že provedou platbu sami sobě. Tím se zajistí vyvážené rozdělení peněžních prostředků v jednotlivých kanálech. Pokud jste v profilu "spotřebitel", není to nezbytné, ale pokud si přejete, můžete toto vyvážení provést sami, nebo dočasně nastavit nulové poplatky za kanál, abyste to usnadnili kolegovi, který to chce udělat. Někdy se do toho nikomu nechce.



![Image](assets/fr/090.webp)




# Využití potenciálu uzlu Lightning


<partId>8dcc24b1-6eb9-4a5f-a56b-8a823e5ac0fd</partId>



## Připojení mobilního zařízení wallet prostřednictvím Tailscale


<chapterId>5fefb222-3f50-4f9d-a170-2ea628be4437</chapterId>



To je vše, nyní máte dobře propojený uzel Lightning s příchozí i odchozí likviditou. Takže jste připraveni používat svůj uzel Lightning v reálném životě. Až dosud jsme vždy používali rozhraní přímo na Umbrel, buď aplikaci `Lightning Node`, nebo rozhraní `ThunderHub`. Tyto nástroje fungují pro odesílání a přijímání plateb, ale zjevně nejsou optimalizovány pro každodenní platby Lightning. Rozhraní je určeno pro použití na počítači, na chytrém telefonu je nepraktické a pro správnou funkci také vyžaduje připojení ke stejné síti (i když je technicky možné se připojit vzdáleně přes Tor).



V praxi jako bitcoináři hledáme klasické rozhraní Lightning wallet na chytrém telefonu: možnost skenovat faktury pomocí QR kódu a jednoduché rozhraní pro placení a proplácení sats. Přesně to budeme implementovat v této a následující kapitole. Obecnou myšlenkou je mít ve smartphonu mobilní aplikaci Lightning wallet, kterou lze používat odkudkoli (nejen z místní sítě), ale která se na pozadí spoléhá na vlastní uzel Lightning pro odesílání a přijímání plateb.



### Jaká jsou řešení pro připojení mobilního zákazníka?



Dnes existuje několik způsobů, jak toho dosáhnout, a to jak z hlediska mobilní aplikace, tak z hlediska typu spojení mezi vaším uzlem a touto aplikací. Existují tři hlavní způsoby připojení:




- prostřednictvím ***Tor***;
- přes VPN ***Tailscale***;
- prostřednictvím ***Nostr Wallet Connect***.



Před několika lety jsem se připojoval přes ***Tor***, ale rychle jsem přestal: počet selhání a zpoždění komunikace byly příliš velké. Teoreticky to funguje, ale v praxi byl uživatelský zážitek katastrofální. Proto bych tento přístup nedoporučoval.



Alternativou, kterou jsem zvolil, bylo použití sítě ***Tailscale*** VPN k zajištění komunikace mezi mobilní aplikací a uzlem. Toto řešení funguje velmi dobře: i v mobilních sítích s nízkou propustností mé platby vždy proběhly bez potíží. Tuto metodu představím jako první v této kapitole, a to s aplikací Zeus.



V příští kapitole se podíváme na jiné, novější řešení, které rovněž funguje velmi dobře: ***Nostr Wallet Connect***. Tentokrát využijeme aplikaci Alby Go, abychom vám představili alternativu, ačkoli Zeus je kompatibilní i s NWC, pokud si to přejete.



### Instalace a konfigurace Tailscale



Pro tuto první metodu budeme potřebovat Tailscale. Jedná se o řešení VPN založené na WireGuard, které umožňuje bezpečné připojení zařízení rozmístěných po celém internetu a zároveň automaticky řídí šifrování, ověřování a překonávání NAT. Zjednodušeně řečeno, je to, jako by všechna vaše zařízení byla připojena ke stejné síti LAN jako váš směrovač, i když mohou být kdekoli na internetu.



Chcete-li ji používat, nejprve si vytvořte účet. Přejděte na webové stránky Tailscale a klikněte na tlačítko `Začítat`.



![Image](assets/fr/071.webp)



Poté vyberte poskytovatele identit pro svůj účet Tailscale. Osobně jsem k přihlášení použil jeden ze svých účtů GitHub.



![Image](assets/fr/072.webp)



Po přihlášení se zobrazí několik otázek o vašem používání. Chcete-li pokračovat, stručně na ně odpovězte.



![Image](assets/fr/073.webp)



Poté vám Tailscale nabídne instalaci klienta do vašeho počítače. To nás v tuto chvíli nezajímá: přejděte přímo na Umbrel a nainstalujte si aplikaci Tailscale z App Store.



![Image](assets/fr/074.webp)



Po otevření aplikace klikněte na `Přihlásit se` a poté proveďte ověření stejným způsobem jako při vytváření účtu.



![Image](assets/fr/075.webp)



Klikněte na tlačítko `Připojit` a potvrďte. Váš Umbrel je nyní připojen k síti VPN.



![Image](assets/fr/076.webp)



Poté si stáhněte aplikaci Tailscale do svého chytrého telefonu a přihlaste se pomocí stejného účtu. Upozornění: v systému Android není možné používat dvě sítě VPN současně. Aby aplikace Tailscale fungovala, musíte vypnout všechny ostatní aktivní sítě VPN. Navíc pokaždé, když budete chtít použít uzel Lightning prostřednictvím aplikace Zeus, budete muset aktivovat VPN Tailscale, jinak se spojení nenaváže.



![Image](assets/fr/077.webp)



Na webu Tailscale, kde jsou nyní připojeni alespoň dva klienti, můžete přistupovat ke konzole pro správu se seznamem všech zařízení připojených k síti a jejich IP adres Tailscale.



![Image](assets/fr/078.webp)



### Připojit Zeus



Nainstalujte si do telefonu aplikaci Zeus. Po jejím otevření vyberte možnost `Rozšířené nastavení` a poté `Vytvořit nebo připojit wallet`.



![Image](assets/fr/079.webp)



V části `Rozhraní Wallet` vyberte možnost `LND (REST)`. Poté zadejte adresu Tailscale vašeho Umbrel, kterou můžete zjistit z ovládacího panelu Tailscale nebo přímo v aplikaci Tailscale na Umbrel. Jako port zadejte `8080`.



![Image](assets/fr/080.webp)



Zeus vás pak požádá, abyste mu poskytli `Makron`. Jedná se o autorizaci token, která umožňuje přesně definovat práva udělená aplikaci (v tomto případě Zeus) k interakci s vaším uzlem Lightning. Je možné získat generate macaroon z ThunderHub, v nabídce `Nástroje`, v podnabídce `Bakery`, ale pro tento účel je nejjednodušší získat jej přímo z aplikace `Světelný uzel`.



Klikněte na tři malé tečky v pravém horním rohu rozhraní a poté na `Připojit Wallet`. Zvolte `REST (Local Network)`. Poté budete moci zkopírovat makaron s příslušnými právy.



![Image](assets/fr/081.webp)



Vložte ji do příslušného pole v programu Zeus a klikněte na tlačítko `UCHOVAT KONFIGURACI PENĚŽENKY`.



![Image](assets/fr/082.webp)



Nyní můžete k uzlu Lightning přistupovat z aplikace Zeus. To znamená, že můžete generate faktury přijímat platby přímo na uzlu Lightning ze svého chytrého telefonu a také platit faktury Lightning, ať jste kdekoli.



![Image](assets/fr/083.webp)



Tip: Tailscale není omezen na vzdálené používání uzlu Lightning. Umožňuje přistupovat ke všem nástrojům Umbrel z jiného softwaru, a to i na dálku. Například můžete použít IP adresu Tailscale svého uzlu Umbrel k připojení uzlu Bitcoin (prostřednictvím Electrs nebo Fulcrum) k uzlu Sparrow Wallet, aniž byste museli procházet přes Tor. Opět se tak vyhnete pomalosti, která je vlastní Toru. Jednoduše nainstalujte klienta Tailscale do svého počítače a připojte jej k síti.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

V příští kapitole se podíváme na jiný, stejně efektivní způsob připojení mobilního klienta k uzlu Lightning: Nostr Wallet Connect. Budeme používat jinou aplikaci než Zeus (i když Zeus je s NWC také kompatibilní), a to Alby Go.



## Připojení mobilního zařízení wallet prostřednictvím NWC


<chapterId>f5c97e43-e66e-4ba3-bcc9-fee1a04fc7f4</chapterId>



Pokud vás připojení Tailscale nepřesvědčilo nebo se vám zdá správa duální sítě VPN příliš náročná, tato kapitola navrhuje jiný způsob, jak pomocí vzdáleného mobilního klienta platit a přijímat sats prostřednictvím uzlu Lightning: ***Připojení Nostr Wallet***.



Pro tento příklad použijeme mobilní aplikaci Alby Go, která je velmi dobře navržená a obzvláště snadná na naučení. Přesto můžete použít také Zeus nebo jakoukoli jinou mobilní aplikaci kompatibilní s NWC. Seznam kompatibilních aplikací najdete na [repozitáři `awesome-nwc` GitHub](https://github.com/getAlby/awesome-nwc).



### Jak funguje Nostr Wallet Connect?



Nostr Wallet Connect je standardizovaný protokol, který umožňuje aplikaci nebo webové stránce spouštět akce na vzdáleném uzlu Lightning, aniž by bylo navázáno přímé síťové spojení s tímto uzlem (žádné vystavení API LND, žádná VPN, žádná služba `.onion`...). NWC definuje, jak aplikace formuluje záměr (např. `zaplatit_fakturu`) a přijímá výsledek.



Funguje to jednoduše. Relace se inicializuje naskenováním QR kódu nebo pomocí hlubokého odkazu `nostr+walletconnect:`. Tento řetězec obsahuje parametry relace a autorizační tajemství. Když pak chce aplikace zaplatit, serializuje požadavek, zašifruje jej a zveřejní jako událost na relay Nostr. Uzel přečte událost na relé, dešifruje ji, zkontroluje, zda je autor pro tuto relaci autorizován, provede platbu a vrátí zašifrovanou odpověď (úspěch s předobrazem, nebo chyba). Relé funguje pouze jako transportní prostředník: nemůže číst obsah, ale může sledovat časování a četnost požadavků.



Ve srovnání s připojením přes Tailscale nebo Tor je hlavní výhodou NWC to, že váš uzel není přímo dosažitelný zvenčí. To značně zjednodušuje mobilní použití: váš uzel nemusí přijímat příchozí spojení, stačí, aby byl schopen komunikovat s relay. Na druhou stranu zavádíte funkční závislost na relé Nostr: pokud jsou nedostupná, zhoršuje se zážitek. Také, i když jsou zprávy šifrované, relé může sledovat určitou úroveň metadat o činnosti.



Důležitý je také rozdíl v modelech zabezpečení. S Tailscale nebo Tor vystavujete přímý přístup k uzlu (prostřednictvím API nebo LND) chráněný vysoce citlivými tajemstvími. To je mocné, protože můžete spravovat vše, ale je to také útočná plocha nižší vrstvy. U NWC je přístup více aplikační: delegujete relaci token, která autorizuje pouze určité akce.



### Nainstalujte Alby Hub do uzlu Lightning



Dříve byla v obchodě s aplikacemi Umbrel k dispozici aplikace určená speciálně pro připojení NWC, ale ta již bohužel není k dispozici. K navázání tohoto typu připojení je nyní nutné použít aplikaci Alby Hub. Za tímto účelem začněte instalací aplikace Alby Hub přímo z obchodu.



![Image](assets/fr/091.webp)



Po otevření přeskočte úvodní obrazovky a klikněte na tlačítko `Začít (LND)`. Je důležité zkontrolovat, zda je v závorce uvedeno `LND`, nikoli `LDK`. Pokud se zobrazí `LND`, znamená to, že Alby Hub správně detekoval váš existující uzel Lightning a nakonfiguruje se jako jeho rozhraní. Pokud se naopak zobrazí `LDK`, znamená to, že Alby Hub váš uzel nedetekoval a chystá se vytvořit nový, což zde není cílem.



![Image](assets/fr/092.webp)



Poté budete vyzváni k nastavení účtu Alby. Pro použití omezené na NWC to není nutné, ale můžete tak učinit, pokud chcete využívat specifické služby Alby. Pokud ne, pokračujte kliknutím na `Možná později`.



![Image](assets/fr/093.webp)



Pak zvolte silné a jedinečné heslo. Tím ochráníte přístup ke Alby Hub ve svém uzlu. Nezapomeňte jej uložit do správce hesel.



![Image](assets/fr/094.webp)



Tím se dostanete do rozhraní Alby Hub. Nemusíte procházet celým procesem konfigurace, pokud jej nechcete používat jako hlavního správce uzlu Lightning. Jak jsme viděli dříve, Alby Hub může ve skutečnosti nahradit používání ThunderHub pro správu vašeho uzlu. Pokud se chcete o možnostech Alby Hub dozvědět více, podívejte se na náš specializovaný návod:



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Přejděte do nabídky `Připojení`.



![Image](assets/fr/095.webp)



Zde se zobrazí všechny aplikace, které se mohou připojit k uzlu Lightning prostřednictvím NWC. Patří mezi ně i Zeus, o kterém jsme se již zmínili v předchozí kapitole. Zde budeme používat Alby Go. Klikněte na Alby Go a poté na tlačítko `Připojit ke Alby Go`, čímž zahájíte proces připojení.



![Image](assets/fr/096.webp)



### Instalace a připojení Alby Go



Do chytrého telefonu nainstalujte aplikaci Alby Go:




- [Obchod Google Play](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Apple App Store](https://apps.apple.com/us/app/alby-go/id6471335774);
- [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq3jhml5fvklgnq9fxpete767txn9zfzqdkc0sxfptmnchfrexje7qqfxxmmd9enk2arpd338jtndda3xjmr9pzj5tk).



V modulu Alby Hub nakonfigurujte práva, která chcete udělit aplikaci Alby Go v uzlu Lightning. Můžete například nastavit limity výdajů za období, datum vypršení platnosti odkazu NWC nebo ponechat úplnou kontrolu. Po nastavení parametrů klikněte na tlačítko `Další`.



![Image](assets/fr/097.webp)



Alby Hub pak pomocí kódu QR generate vytvoří spojení NWC mezi uzlem Lightning a Alby Go.



![Image](assets/fr/098.webp)



Při prvním otevření aplikace Alby Go klikněte na `Připojit Wallet` a poté naskenujte QR kód dodaný Alby Hub.



![Image](assets/fr/099.webp)



Zvolte název pro identifikaci této jednotky wallet. Nyní máte vzdálený přístup k uzlu Lightning prostřednictvím Alby Go. Můžete generate faktury přijímat sats na svém uzlu nebo s ním přímo nastavit faktury Lightning.



![Image](assets/fr/100.webp)



Například jsem z rozhraní Alby Go odeslal 1543 sats.



![Image](assets/fr/101.webp)



Pokud přejdu do základního rozhraní svého uzlu Lightning na Umbrel, vidím, že tato platba byla mým uzlem skutečně provedena.



![Image](assets/fr/102.webp)



Nyní víte, jak snadno používat uzel Lightning odkudkoli.



## Dlouhodobá autonomie v systému Lightning


<chapterId>691a0942-b46d-482a-8fbc-fe19b3814992</chapterId>



Nyní jsme dospěli ke konci tohoto praktického kurzu LNP202. Nyní máte základy, které potřebujete k suverénnímu používání Lightning Network: rozumíte skutečné roli uzlu, kompromisům různých přístupů a nastavili jste instanci LND na Umbrel s konzistentní strategií zálohování a ochrany. Také jste otevřeli své první kanály, naučili jste se řídit likviditu, aby vaše platby byly spolehlivé na denní bázi.



Z provozního hlediska by měl váš uzel nyní přejít do udržovacího rytmu. Hlavní je sledovat jeho provozuschopnost (uptime, synchronizaci, stav kanálů, výpadky plateb atd.), aplikovat aktualizace nabízené Umbrel, jakmile jsou k dispozici stabilní verze, a pravidelně kontrolovat, zda jsou vaše zálohy a konfigurace strážní věže stále aktivní.



Pokud jde o kanály, zaujměte pragmatický přístup: ponechte si ty, které jsou pro vás užitečné, zavřete ty, které jsou trvale neaktivní nebo spojené s nestabilními partnery, a postupně přerozdělujte svůj kapitál směrem k robustnější topologii.



**Jedním z nejčastějších úskalí v této fázi je přidělení příliš velkého kapitálu uzlu Lightning. Mějte na paměti, že váš uzel Lightning je mnohem méně bezpečný než hardwarový wallet a že dostupnost prostředků vyčleněných pro vaše kanály závisí na záložních mechanismech, které zůstávají nedokonalé. Je proto velmi důležité držet se rozumných částek, které si můžete dovolit ztratit v případě problému, a většinu svého sats vždy držet na hardwarovém wallet v řetězci.



Co se týče nástrojů, doporučuji, abyste zůstali zvědaví a pozorně sledovali nový vývoj. V tomto školení jsme jich objevili několik, ať už pro správu uzlu, jeho připojení nebo vzdálené použití k provádění plateb. Lightning je však obzvláště dynamická oblast. Každý rok se objevují nové a nové relevantní nástroje a mnoho nových aplikací se objevuje také na Umbrel. Sledování těchto novinek vám může umožnit objevit výkonnější nebo praktičtější řešení než ta, která byla představena v tomto kurzu.



Co se týče vzdělávání, pokud jste tak ještě neučinili, vřele vám doporučuji absolvovat teoretický kurz LNP 201 Fanise Michalakise, který se věnuje provozu Lightning Network. Pomůže vám lépe pochopit manipulace prováděné v tomto kurzu LNP202 a dodá vám větší jistotu při každodenní správě uzlu.



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

V jiném duchu, ale stejně zásadní pro vaši cestu bitcoinu, doporučuji také vynikající kurz Ludovica Larse o historii vzniku Bitcoin.



https://planb.academy/courses/a51c7ceb-e079-4ac3-bf69-6700b985a082

Než však budete pokračovat, můžete napsat recenzi tohoto kurzu LNP202 a samozřejmě si vzít diplom, abyste potvrdili, že jste porozuměli celému jeho obsahu.



# Závěrečná část


<partId>683c998f-ba0a-4ffb-a7e8-4cd8369cb9b3</partId>



## Recenze a hodnocení


<chapterId>aec048c7-7130-425d-8eca-9cd7f90c27f3</chapterId>



<isCourseReview>true</isCourseReview>

## Závěrečná zkouška


<chapterId>3951ccbb-14a3-4322-b81b-8dd2a6da19cb</chapterId>



<isCourseExam>true</isCourseExam>

## Závěr


<chapterId>30cd6309-5139-40d9-8927-92de0f76414a</chapterId>



<isCourseConclusion>true</isCourseConclusion>