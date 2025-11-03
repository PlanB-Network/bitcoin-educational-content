---
name: Mempool
description: Prozkoumejte celý ekosystém Bitcoin.
---

![cover](assets/cover.webp)



Protokol Bitcoin je pseudonymní decentralizovaná síť otevřená ke konzultaci. Členové (uzly), tj. počítače s instancí softwaru Bitcoin, mají neomezený přístup ke všem datům zveřejněným v Bitcoin. V prvních letech existence protokolu Bitcoin však nebyl tak široce přístupný jako dnes.


V počátcích Bitcoin bylo nutné spustit uzel Bitcoin, aby bylo možné přistupovat k příslušným nástrojům (bitcoin-cli) pro dotazování sítě z příkazových řádků.



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Proto byly zahájeny projekty, jejichž cílem je rozšířit komunitu Bitcoin a zpřístupnit ji všem, kteří nevlastní uzel a/nebo nemají potřebné technické dovednosti.



V tomto tutoriálu se podíváme na projekt **Mempool.space**, jeho funkce a dopad, který měl na ekosystém Bitcoin.



## Co je Mempool.space?



**Mempool.space** je open-source průzkumník, který poskytuje užitečné informace o transakcích, transakčních poplatcích, blocích a těžařích v různých sítích protokolu Bitcoin. Byl spuštěn v roce 2020 a přináší výrazné zlepšení uživatelského komfortu díky reprezentativní grafice, plynulým animacím a nenáročným rozhraním.



Pro pochopení projektu je Mempool (paměťový fond) virtuální prostor, ve kterém jsou uloženy všechny transakce čekající na potvrzení v síti Bitcoin. Mempool je jako "čekárna", kde čekají transakce Bitcoin na potvrzení. Každý počítač v síti (uzel) má svou vlastní čekárnu, což vysvětluje, proč nejsou všechny transakce viditelné pro všechny současně.



Hlavní dopad platformy v ekosystému Bitcoin spočívá v tom, že umožňuje přístup k různorodým informacím v paměťových oblastech většiny uzlů přítomných v Bitcoin, aniž by bylo nutné některý z nich spustit. Mempool.space je úložiště pro prohlížení a vyhledávání v sítích protokolů Bitcoin.



Stále rozšířenější použití v ekosystému a skutečnost, že Mempool.space je otevřený zdrojový kód, umožnily jeho integraci do stále většího počtu osobních hostingových systémů. Nyní můžete mít vlastní instanci Mempool.space přímo na svém osobním uzlu. Podívejte se na náš návod na konfiguraci Mempool.space na uzlu Umbrel níže.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Základy Mempool.space



Jak bylo uvedeno výše, [Mempool.space](https://Mempool.space) je průzkumník protokolů Bitcoin, který umožňuje sledovat transakce a jejich šíření ve vybrané síti Bitcoin v reálném čase z grafického prostředí Interface.



Mempool.space podporuje mnoho sítí protokolu Bitcoin.


Na panelu nabídek najdete následující sítě:




- **Mainnet**: Hlavní síť Bitcoin, kde probíhají skutečné transakce Bitcoin.
- **Signet**: Testovací síť, která používá digitální podpisy k ověřování bloků, aniž by vyžadovala prostředky vyžadované hlavní sítí.
- **Testnet 3**: Bezriziková testovací a vývojová síť na protokolu Bitcoin.
- **Testnet 4**: Nová verze Testnet 3 přináší do testovacího prostředí větší stabilitu a nová pravidla konsensu.



![reseaux](assets/fr/01.webp)



Na domovské stránce vlevo v Green uvidíte možné budoucí bloky (skupiny transakcí) připravené k validaci a integraci (vytěžení) do sítě Bitcoin. V průměru se každých deset minut vytěží jeden blok: tuto informaci si uschovejte, protože se nám bude později při vývoji hodit.


V purpurové barvě na pravé straně najdete poslední vytěžené bloky na Bitcoin, přičemž číslo posledního vytěženého bloku představuje aktuální výšku sítě.



![blocs](assets/fr/02.webp)



Sekce **Transakční poplatky** je odhad transakčních poplatků. Čím vyšší jsou poplatky přidělené vaší transakci, tím větší je pravděpodobnost, že vaše transakce bude přidána do dalšího bloku připraveného k vytěžení.


Transakční poplatky představují náklady, které si od vás Miner vezme za vložení vaší transakce do kandidátského bloku pro Mining. Je definován poměrem sat/vB (Satoshi/Virtuální bajty), který představuje počet satoshis, které zaplatíte za místo, které vaše transakce zabere v kandidátském bloku.



⚠️ DŮLEŽITÉ: V případě nasycení Mempool těžaři upřednostňují transakce s nejlepším poměrem Satoshi/vByte. Čím těžší (větší) je vaše transakce, tím více satošů bude potřebovat k rychlému zařazení.



![fees-visualizer](assets/fr/03.webp)



Sekce **Mempool Goggles** umožňuje vizualizovat prostor zabraný transakcí.



![mempool](assets/fr/04.webp)



Blok se těží přibližně každých deset minut vzhledem k náročnosti Proof of Work, kterou musí těžaři poskytnout, aby přidali svůj kandidátský blok do řetězce vytěžených bloků. Tato obtížnost se mění každých **2016 bloků**, což odpovídá přibližně **2 týdnům**. Vývoj této obtížnosti si můžete prohlédnout zde.



![difficulty](assets/fr/05.webp)



Přidání nového bloku do hlavního řetězce opravňuje Miner validovaného bloku k odměně, která se skládá z fixní části (půlí se každých 210 000 bloků**, což odpovídá přibližně 4 letům** během půlení) a transakčních poplatků.



![halving](assets/fr/06.webp)



## Přístup k údajům o transakci



Do vyhledávacího řádku Mempool.space můžete zadat své číslo Bitcoin Address nebo transaction ID a zjistit více o své historii.



![search](assets/fr/07.webp)



Na stránce s podrobnostmi o transakci najdete obecné informace o transakci:




- **Stav**: Potvrzeno, když je přidáno do bloku, nepotvrzeno, když čeká v Mempool.
- **Transakční poplatky**.
- **Předpokládaný čas příjezdu (ETA)**: Přibližná doba, za kterou bude vaše transakce přidána do bloku. Počítá se podle poměru, který tvoří poplatky spojené s touto transakcí.



![general-txinfo](assets/fr/08.webp)



V části **Flow** se zobrazuje graf složek transakce.



Vstupy (předchozí UTXO), které se používají pro vaši transakci, a výstupy, které dávají příjemcům právo používat bitcoiny z každého výstupu předložením podpisu požadovaného pro jejich vydání.



![flow](assets/fr/09.webp)



Další podrobnosti o použitých adresách najdete v části **Vstupy a výstupy**.



![address](assets/fr/10.webp)



Objevte různá schémata transakcí Bitcoin, která zvýší vaši důvěrnost.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Zrychlení transakcí



V ekosystému Bitcoin je aspekt ověřování transakcí těžaři neodmyslitelně spjat s poplatky za transakce spojené s danou transakcí. Těžaři upřednostňují transakce s vyšším poměrem poplatků (satoshis/vBajty), což by mohlo ovlivnit platnost vaší transakce, pokud nezaplatíte přiměřené poplatky akceptované těžaři. Vaše transakce by se zasekla v Mempool a čekala by na blok, který akceptuje její poměr poplatků.



Naštěstí jsou v síti Bitcoin k dispozici dvě metody, které potvrzení transakce urychlí.





- **RBF** - Náhrada za poplatek: Metoda, která umožňuje utratit stejné položky jako u transakce s nízkým poplatkem, ale tentokrát zvýšením poplatku za transakci, aby se urychlila validace. Vaše nová transakce bude rychleji ověřena a zařazena do bloku, čímž se transakce s nízkým poplatkem zneplatní.



U portfolií, která tento mechanismus akceptují, můžete provést akci nahrazení poplatku. Viz například náš článek o portfoliu Blue Wallet.



https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90



- **CPFP** - Child pay for parent: Přístup inspirovaný RBF, ale na straně přijímače. Když je transakce, v níž jste příjemcem, zablokována v Mempool, máte možnost utratit výstupy (UTXO) této transakce, přestože ještě nebyla potvrzena, a to tak, že této nové transakci přidělíte více poplatků, takže průměrné poplatky - transakce, u níž jste příjemcem, a iniciované transakce - povzbudí těžaře, aby obě transakce zařadili do bloku.



⚠️ První transakce musí být zahrnuta do bloku, aby mohla být potvrzena druhá transakce.



Pokud se vám všechny tyto pojmy zdají příliš odborné, doporučuji vám [nahlédnout do našeho slovníčku](https://planb.academy/resources/glossary), který obsahuje definice všech odborných pojmů týkajících se Bitcoin a jeho ekosystému.



Kromě těchto metod vám Mempool.space díky svému spojení s více než 80 % těžařů přítomných v síti Bitcoin také umožňuje urychlit jakoukoli vaši **nepotvrzenou** transakci, a to i tu, která neaktivuje RBF, tím, že zaplatíte odměnu těžařům v Exchange za vložení vaší nízkonákladové transakce do dalšího bloku připraveného k vytěžení.



Na stránce s podrobnostmi o transakci klikněte na tlačítko **Urychlit** a poté pokračujte v platbě protistrany těžařům.



![accelerate-section](assets/fr/11.webp)


## Nezletilí



Miner označuje osobu, která spravuje důl, tj. počítač zapojený do procesu Mining, který spočívá v účasti na Proof-of-Work. Miner seskupuje nevyřízené transakce ve svém Mempool tak, aby vytvořil kandidátský blok. Poté hledá platný Hash, menší nebo roven cíli, pro záhlaví tohoto bloku úpravou různých nonces. Pokud najde platný Hash, odvysílá svůj blok do sítě Bitcoin a strčí si do kapsy související peněžní odměnu, která se skládá z dotace bloku (vytvoření nových bitcoinů ex-nihilo) a transakčního poplatku.



https://planb.academy/courses/ce272232-0d97-4482-884a-0f77a2ebc036

❗Minery jsou jako "validátoři", kteří ověřují a seskupují transakce do bloků. Aby mohli přidat nový blok do sítě Bitcoin, musí vyřešit složitou matematickou hádanku (Proof-of-Work). Ten, kdo jako první vyřeší hádanku Miner, získává odměnu Bitcoin (dotace bloku + poplatky za transakce zahrnuté do bloku).



Obtížnost tohoto Proof of Work je sledována, což umožňuje vizualizovat vývoj výpočetního výkonu potřebného pro těžaře. V níže uvedených částech najdete :





- Odhad celkových odměn, které těžaři získali během poslední úpravy obtížnosti, a také odhad příštího bloku Halving, ke kterému dochází každých 210 000 bloků (přibližně 04 roky).



![rewards](assets/fr/12.webp)



Tato obtížnost se upravuje každých 2016 bloků (přibližně dva týdny). Je nepřímo úměrná průměrnému času, který horníci potřebují k tomu, aby Miner každých 2016 bloků.


Pokud je průměrná doba, kterou těžaři potřebují, kratší než 10 minut, obtížnost se zvyšuje, což dokazuje, že pro těžaře bylo snazší validovat bloky Miner. Naopak když je průměrná doba potřebná k ověření větší než 10 minut, obtížnost se snižuje.



![mining-pool](assets/fr/13.webp)





- Skupiny horníků: Vzhledem k obtížnosti se skupina horníků snaží spolupracovat při hledání Proof of Work na Bitcoin v takzvaném **poulu**. Když skupina vytěží blok, získaná odměna se rozdělí podle procenta úspěšnosti při hledání dílčího řešení každého Miner, tj. podle příspěvku ve výpočetním výkonu při hledání Proof-of-Work, nebo podle způsobu odměňování, na kterém se dohodnou v rámci spolupráce.





![mining](assets/fr/14.webp)



## Infrastruktura Lightning Network



Mempool neposkytuje pouze informace o síťové infrastruktuře Bitcoin (hlavní řetězec). Integruje také vizualizační a průzkumné nástroje pro překryvnou vrstvu Bitcoin Lightning.



V části **Lightning** můžete zobrazit všechna existující připojení mezi uzly Lightning.



![network-stats](assets/fr/15.webp)



Tento dokument Interface poskytuje informace o :





- Statistika Lightning Network.



![distribution](assets/fr/16.webp)




⚠️ **DŮLEŽITÉ**: Kapacita platebního kanálu určuje maximální částku, kterou může uzel poslat jinému uzlu během transakce Lightning.





- Bleskové uzly jsou přidělovány podle poskytovatele internetových služeb (hostingové služby) a případně podle kapacity platebního kanálu.



![distribution](assets/fr/17.webp)





- Historie celkové kapacity letounu Lightning Network.


Najdete zde také pořadí těchto uzlů podle kapacity jejich platebních kanálů.



![ranking](assets/fr/18.webp)



## Více grafiky



Mempool.space je ideální platformou pro interakci se sítěmi protokolu Bitcoin. Grafy poskytují nejen vizuální údaje, které vám pomohou rozhodnout se, kdy provádět transakce, ale také přesné parametry umožňující v reálném čase vizualizovat sílu a stav sítě Bitcoin a souvisejících infrastruktur Lightning.



V části **Grafika** můžete zobrazit základní údaje o síti Bitcoin:




- Vývoj velikosti Mempool: Můžete sledovat, jak kolísá velikost Mempool, což může indikovat období vysoké nebo nízké aktivity v síti.



![graphs](assets/fr/19.webp)






- Vývoj transakcí a transakčních poplatků ve vybrané síti: Díky sledování změn v počtu transakcí za sekundu můžete předvídat období přetížení nebo nízké aktivity a optimalizovat transakční poplatky. Tento graf vám poskytne přehled o tom, jak síť zvládá objem transakcí.



![graphs](assets/fr/20.webp)



Nyní, když jste se dostali na konec své cesty na Mempool.space, staňte se svým vlastním průzkumníkem a sledujte své transakce v reálném čase. Níže naleznete náš článek o průzkumníkovi **veřejného poolu** Bitcoin.



https://planb.academy/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1