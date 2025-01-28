---
name: OXT - Chain Analysis
description: Zvládněte základy analýzy řetězce na Bitcoinu
---
![obálka](assets/cover.webp)

***VAROVÁNÍ:** Po zatčení zakladatelů peněženky Samourai a zabavení jejich serverů 24. dubna je **webová stránka OXT.me momentálně nedostupná**. Stále však existuje možnost, že toto nástroj bude v nadcházejících týdnech znovu spuštěn. Mezitím můžete stále využít tento tutoriál k pochopení základů analýzy řetězce na Bitcoinu. Všechny heuristiky a vzory prezentované zde zůstávají aplikovatelné na transakce Bitcoinu. I když jsou tyto nástroje méně optimalizované než OXT, můžete dočasně použít [Mempool.space](https://mempool.space/) nebo [Bitcoin Explorer](https://bitcoinexplorer.org/), abyste mohli prakticky aplikovat teoretické koncepty tohoto článku.*

_Pečlivě sledujeme vývoj této kauzy i vývoj souvisejících nástrojů. Ujistěte se, že tento tutoriál aktualizujeme, jakmile budou k dispozici nové informace._

_Tento tutoriál je poskytován pouze pro vzdělávací a informační účely. Nepodporujeme ani nevyzýváme k používání těchto nástrojů pro kriminální účely. Je zodpovědností každého uživatele dodržovat zákony ve své jurisdikci._

---

V tomto článku se naučíte základní teoretické základy potřebné k zahájení základních analýz řetězce na Bitcoinu a co je ještě důležitější, pochopit, jak vás ti, kteří vás sledují, provozují. Ačkoli tento článek není praktickým tutoriálem na nástroj OXT (téma, kterému se budeme věnovat v budoucím tutoriálu), shromažďuje soubor klíčových znalostí pro jeho použití. Pro každý model, metriku a indikátor prezentovaný zde je poskytnut odkaz na příklad transakce na OXT, který vám umožní lépe pochopit jeho použití a procvičovat ho během čtení.

## Úvod
Jednou z funkcí peněz je řešení problému dvojí shody potřeb. V systému založeném na barteru vyžaduje dokončení výměny nejen nalezení jedince, který nabízí zboží, jež splňuje mou potřebu, ale také poskytnutí zboží ekvivalentní hodnoty, které uspokojí jejich vlastní potřebu. Najít tuto rovnováhu je složité. Proto využíváme peněz, které nám umožňují přesouvat hodnotu jak v prostoru, tak v čase.

Aby peníze tento problém vyřešily, je nezbytné, aby strana poskytující zboží nebo službu byla přesvědčena o své schopnosti později tuto sumu utratit. Takže každý racionální jedinec ochotný přijmout kus peněz, ať už digitálních nebo fyzických, se ujistí, že splňuje dva základní kritéria:
- Mince musí být neporušená a pravá;
- a nesmí být dvojnásobně utracena.

Pokud používáme fyzické peníze, je první vlastnost ta nejsložitější k ověření. V různých obdobích historie byla integrita kovových mincí často ovlivněna praktikami jako je zastřihávání nebo vrtání. Například v antickém Římě bylo běžné, že občané škrábali okraje zlatých mincí, aby získali kousek drahého kovu, přičemž je stále uchovávali pro budoucí transakce. To je mimo jiné důvod, proč byly později na okraji mincí razeny drážky. Autenticita je také těžko ověřitelná vlastnost na fyzickém peněžním médiu. V současnosti jsou techniky boje proti padělání stále složitější, což nutí obchodníky investovat do drahých ověřovacích systémů.

Na druhou stranu, kvůli jejich povaze, není dvojí utrácení problém pro fyzické měny. Pokud vám dám bankovku 10 €, neodvolatelně opustí moje vlastnictví, aby vstoupila do vašeho, čímž vylučuje jakoukoli možnost vícekrát utratit peněžní jednotky, které představuje.
Pro digitální měny je výzva odlišná. Zajištění pravosti a integrity mince je často jednodušší, ale zajištění absence dvojího utrácení je složitější. Každé digitální zboží je v podstatě informace. Na rozdíl od fyzického zboží se informace při výměnách nedělí, ale šíří jejich násobením. Například, pokud vám pošlu dokument e-mailem, dojde k jeho duplikaci. Na vaší straně nemůžete s jistotou ověřit, že jsem původní dokument smazal.

Jediný způsob, jak se vyhnout této duplikaci digitálního zboží, je být informován o všech výměnách v systému. Tímto způsobem může člověk vědět, kdo co vlastní, a aktualizovat účty každého na základě provedených transakcí. To se dělá například s knižními penězi. Když zaplatíte obchodníkovi 10 € kreditní kartou, banka si tuto výměnu poznamená a aktualizuje účetní knihu.

Na Bitcoinu se prevence dvojího utrácení provádí stejným způsobem. Snaží se potvrdit absenci transakce, která již mince utratila. Pokud tyto nikdy nebyly použity, pak můžeme být ujištěni, že nedojde k dvojímu utrácení. To je slavná věta od Satoshiho Nakamota v White Paper: "*Jediný způsob, jak potvrdit absenci transakce, je být informován o všech transakcích.*"

Na rozdíl od bankovního modelu na Bitcoinu nechceme muset důvěřovat centrální entitě. Proto musí všichni uživatelé být schopni potvrdit tuto absenci dvojího utrácení, aniž by se spoléhali na třetí stranu. Takže každý musí být informován o všech Bitcoinových transakcích.

Právě toto veřejné šíření informací komplikuje ochranu soukromí na Bitcoinu. V tradičním bankovním systému, teoreticky, pouze finanční instituce ví o provedených transakcích. Avšak na Bitcoinu jsou všichni uživatelé informováni o všech transakcích prostřednictvím jejich příslušných uzlů.

Kvůli tomuto omezení šíření se model soukromí Bitcoinu liší od modelu bankovního systému. V tomto případě jsou transakce spojeny s identitou uživatele, ale tok informací je přerušen mezi důvěryhodnou třetí stranou a veřejností. Jinými slovy, váš bankéř ví, že si každé ráno kupujete bagetu v místní pekárně, ale váš soused není informován o všech těchto transakcích. V případě Bitcoinu, protože tok informací mezi transakcemi a veřejnou doménou nelze přerušit, model soukromí spoléhá na oddělení identity uživatele od samotných transakcí.
![analýza](assets/en/1.webp)
*Diagram inspirovaný Satoshi Nakamotem v White Paper: Bitcoin: A Peer-to-Peer Electronic Cash System, sekce 10 "Privacy".*
Protože transakce Bitcoinu jsou zveřejněny, stává se možným vytvářet mezi nimi vazby a odvodit informace o zúčastněných stranách. Tato činnost dokonce představuje samostatnou specializaci, běžně nazývanou "analýza řetězce". V tomto článku vás zvu, abyste prozkoumali základy analýzy řetězce, abyste pochopili, jak jsou vaše bitcoiny sledovány.

Většina společností specializujících se na analýzu řetězce funguje jako černé skříňky a nesdílí své metodologie. Proto je obtížné získat informace o této praxi. Při psaní tohoto článku jsem se hlavně spoléhal na několik dostupných otevřených zdrojů:
- Většina mého článku je vytěžena ze série čtyř článků nazvaných: [Understanding Bitcoin Privacy with OXT](https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923), které v roce 2021 vyprodukovala Samourai Wallet;
- Také jsem využil různé zprávy od [OXT Research](https://medium.com/oxt-research), stejně jako jejich bezplatný nástroj pro analýzu řetězce;
- Obecněji řečeno, mé znalosti pocházejí z různých tweetů a obsahu od [@LaurentMT](https://twitter.com/LaurentMT) a [@ErgoBTC](https://twitter.com/ErgoBTC);- Také mě inspiroval [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji), ve kterém jsem se zúčastnil společně s [@louneskmt](https://twitter.com/louneskmt), [@TheoPantamis](https://twitter.com/TheoPantamis), [@Sosthene___](https://twitter.com/Sosthene___), a [@LaurentMT](https://twitter.com/LaurentMT).

Chtěl bych poděkovat jejich autorům, vývojářům a producentům. Bez jejich různých obsahů a softwaru by tento článek neexistoval. Děkuji také recenzentům, kteří tento text pečlivě opravili a obdařili mě svými odbornými radami:
- [Gilles Cadignan](https://twitter.com/gillesCadignan);
- [Ludovic Lars](https://twitter.com/lugaxker) ([https://viresinnumeris.fr/](https://viresinnumeris.fr/)).

*Pro vaši informaci jsem na konec článku přidal technický minislovníček k definování určitých termínů. Pokud narazíte na slovo, kterému nerozumíte a je označeno hvězdičkou, jeho definice je na konci stránky.*

## Co je analýza řetězce?
Analýza řetězce je praxe, která zahrnuje všechny metody sledování toků Bitcoinů na blockchainu. Obecně se analýza řetězce spoléhá na pozorování charakteristik v vzorcích předchozích transakcí. Poté zahrnuje identifikaci těchto stejných charakteristik v transakci, kterou chce někdo analyzovat, a odvození pravděpodobných interpretací. Tento způsob řešení problémů, založený na praktickém přístupu k nalezení dostatečně dobrého řešení, se nazývá heuristika.

Zjednodušeně řečeno, analýza řetězce probíhá ve dvou hlavních krocích:
1. Identifikace známých charakteristik;
2. Odvození hypotéz.

Jedním z cílů analýzy řetězce je seskupit různé aktivity na Bitcoinu, aby bylo možné určit jedinečnost uživatele, který je provedl. Následně bude možné pokusit se spojit tento svazek aktivit s skutečnou identitou.

Pamatujte na mé úvodní slovo. Vysvětlil jsem, proč původní model soukromí Bitcoinu spočíval v oddělení identity uživatele od jeho transakcí. Proto by se mohlo zdát, že analýza řetězce je zbytečná, protože i když se podaří seskupit aktivity na řetězci, nemohou být spojeny se skutečnou identitou. Teoreticky je toto tvrzení přesné. Kryptografické páry klíčů se používají k stanovení podmínek na UTXO. Tyto páry klíčů svou podstatou neodhalují žádné informace o identitě jejich držitelů. Takže i když se podaří seskupit aktivity spojené s různými páry klíčů, to nám nic neříká o entitě za těmito aktivitami.
Nicméně, praktická realita je mnohem složitější. Existuje mnoho chování, která riskují spojení skutečné identity s aktivitou na blockchainu. V analýze se tomu říká vstupní bod a existuje jich mnoho. Nejběžnější, samozřejmě, je KYC (Know Your Customer - Poznej svého zákazníka). Pokud vyberete své bitcoiny z regulované platformy na jednu ze svých osobních přijímacích adres, pak někteří lidé mohou spojit vaši identitu s touto adresou. Šířeji vzato, vstupní bod může být jakákoli forma interakce mezi vaším skutečným životem a transakcí Bitcoinu. Například, pokud zveřejníte přijímací adresu na svých sociálních sítích, to může být vstupní bod pro analýzu. Pokud provedete platbu v bitcoinech svému pekaři, mohou spojit vaši tvář (která je součástí vaší identity) s Bitcoinovou adresou. Tyto vstupní body jsou téměř nevyhnutelné při používání Bitcoinu. Ačkoli by člověk mohl usilovat o omezení jejich rozsahu, zůstanou přítomny. Proto je klíčové kombinovat metody zaměřené na ochranu vašeho soukromí. Přestože udržování přijatelného oddělení mezi vaší skutečnou identitou a vašimi transakcemi je chvályhodný přístup, zůstává nedostatečný. Skutečně, pokud lze všechny vaše aktivity na blockchainu seskupit dohromady, pak i nejmenší vstupní bod by mohl ohrozit jedinou vrstvu soukromí, kterou jste si vytvořili.

Proto je také nutné zabývat se analýzou řetězce v našem používání Bitcoinu. Tímto způsobem můžeme minimalizovat agregaci našich aktivit a omezit dopad vstupního bodu na naše soukromí. Přesněji řečeno, pro lepší boj proti analýze řetězce, jaký lepší přístup, než se seznámit s metodami používanými v analýze řetězce? Pokud chcete vědět, jak zlepšit své soukromí na Bitcoinu, musíte tyto metody pochopit. To vám umožní lépe pochopit techniky jako [Coinjoin](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef) nebo [Payjoin](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f) a snížit chyby, které byste mohli udělat.

V tomto můžeme nalézt analogii s kryptografií a kryptoanalýzou. Dobrý kryptograf je především dobrý kryptoanalytik. Aby si člověk mohl představit nový šifrovací algoritmus, musí vědět, jakým útokům bude čelit, a také studovat, proč byly předchozí algoritmy prolomeny. Stejný princip platí pro soukromí na Bitcoinu. Porozumění metodám analýzy řetězce je klíčem k ochraně proti ní. Proto vám nabízím tento článek.

Je zásadní pochopit, že analýza řetězce není přesná věda. Spoléhá na heuristiky odvozené z předchozích pozorování nebo logických interpretací. Tyto pravidla umožňují poměrně spolehlivé výsledky, ale nikdy s absolutní přesností. Jinými slovy, analýza řetězce vždy zahrnuje dimenzi pravděpodobnosti ve vyvozených závěrech. Můžeme odhadnout s větší či menší jistotou, že dvě adresy patří stejné entitě, ale úplná jistota bude vždy nedosažitelná.

Celý cíl analýzy řetězce spočívá přesně v agregaci různých heuristik, aby se minimalizovalo riziko chyby. Je to jakýsi akumulace důkazů, které nám umožňují přiblížit se k realitě.

Tyto slavné heuristiky lze rozdělit do různých kategorií, které společně podrobněji prozkoumáme:
- Vzory transakcí (nebo modely transakcí);
- Interní heuristiky k transakci;
- Externí heuristiky k transakci.

Je důležité poznamenat, že první dvě heuristiky na Bitcoinu formuloval sám Satoshi Nakamoto. Diskutuje o nich v části 10 White Paperu. Jak uvidíme později, je zajímavé pozorovat, že tyto dvě heuristiky si dodnes udržují přednost v analýze řetězce. Jsou to:
- heuristika společného vlastnictví vstupu (CIOH);
- a opětovné použití adresy.
Pojďme společně prozkoumat pozorovatelné charakteristiky a interpretace, které lze vyvodit pro provedení analýzy.
## Vzory transakcí (nebo modely transakcí)
Vzor transakce je jednoduše typický model transakce, který lze nalézt na blockchainu, jehož interpretace je pravděpodobně známá. Při studiu vzorů se zaměříme na jednu konkrétní transakci, kterou budeme analyzovat na vysoké úrovni. Jinými slovy, budeme se dívat pouze na počet vstupů a výstupů, aniž bychom se zabývali jejími specifičtějšími detaily nebo jejím prostředím. Z pozorovaného modelu budeme schopni interpretovat povahu transakce. Poté budeme hledat charakteristiky týkající se její struktury a vyvodíme interpretaci.

### Jednoduché odeslání (nebo jednoduchá platba)
Tento model je charakterizován spotřebou jednoho nebo více UTXO jako vstup a produkcí dvou UTXO jako výstup.

![analýza](assets/en/2.webp)

Interpretace tohoto modelu je, že se nacházíme v přítomnosti transakce odeslání nebo platby. Uživatel spotřeboval své vlastní UTXO jako vstup, aby uspokojil na výstupu platbu UTXO a změnu UTXO (změna se vrací stejnému uživateli). Proto víme, že pozorovaný uživatel pravděpodobně již není v držení jednoho ze dvou UTXO na výstupu (toho platby), ale stále vlastní druhé UTXO (změnu).

V tomto bodě je pro nás nemožné specifikovat, který výstup reprezentuje které UTXO, protože to není cílem tohoto modelu. Budeme to moci udělat spoléháním se na heuristiky, které budeme studovat v následující části. Na této úrovni je náš cíl omezen pouze na identifikaci povahy dotčené transakce, která je v tomto případě jednoduché odeslání.

Například zde je Bitcoinová transakce, která přijímá vzor jednoduchého odeslání:
### Sweep ("sweep" v angličtině)
Tento model je charakterizován spotřebou jediného UTXO jako vstup a produkcí jediného UTXO jako výstup.

![analýza](assets/en/3.webp)

Interpretace tohoto modelu je, že se nacházíme v přítomnosti samopřevodu. Uživatel převedl své bitcoiny na sebe, na jinou adresu, kterou vlastní. Vzhledem k tomu, že v transakci nedochází ke změně, je velmi nepravděpodobné, že bychom měli co do činění s platbou. Poté víme, že pozorovaný uživatel pravděpodobně stále vlastní toto UTXO.

Například zde je Bitcoinová transakce, která přijímá vzor sweep:
[35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d](https://mempool.space/tx/35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d)

Tento typ vzoru však může také odhalit samopřevod na účet burzy (platforma pro výměnu kryptoměn). Studium známých adres a kontext transakce nám umožní zjistit, zda jde o sweep do peněženky s vlastní správou nebo o výběr na platformu.

### Konsolidace
Tento model je charakterizován spotřebou několika UTXO jako vstup a produkcí jediného UTXO jako výstup.

![analýza](assets/en/4.webp)
Interpretace tohoto modelu je, že jsme svědky konsolidace. Jedná se o běžnou praxi mezi uživateli Bitcoinu, jejímž cílem je sloučit několik UTXO v předtušení možného zvýšení poplatků za transakce. Provedením této operace v období, kdy jsou poplatky nízké, je možné ušetřit na budoucích poplatcích.
Můžeme usoudit, že uživatel za touto transakcí pravděpodobně vlastnil všechna UTXO na vstupu a stále vlastní UTXO na výstupu. Proto je to jistě samotransfer.

Stejně jako u sweepu, i tento typ vzoru může odhalit samotransfer na účet burzy. Studium známých adres a kontext transakce nám umožní zjistit, zda jde o konsolidaci do peněženky s vlastní správou nebo o výběr na platformu.

Například zde je Bitcoinová transakce, která přijímá vzor konsolidace:
[77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94](https://mempool.space/tx/77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94)
### Model hromadného utrácení
Tento model je charakterizován použitím několika UTXO jako vstupu (často pouze jednoho) a vytvořením mnoha UTXO jako výstupu.

![analýza](assets/en/5.webp)

Interpretace tohoto modelu je, že jsme svědky hromadného utrácení. Jedná se o praxi, která pravděpodobně odhaluje významnou ekonomickou aktivitu, například burzu. Hromadné utrácení těmto subjektům umožňuje ušetřit na poplatcích kombinací jejich výdajů do jediné transakce.

Můžeme usoudit, že UTXO na vstupu pochází od společnosti s významnou ekonomickou aktivitou a že UTXO na výstupu se rozptýlí. Některé budou patřit klientům společnosti. Jiné mohou směřovat k partnerským společnostem. Nakonec se jistě najde i změna, která se vrátí vydávající společnosti.

Například zde je Bitcoinová transakce, která přijímá vzor hromadného utrácení:
[8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43](https://mempool.space/tx/8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43)

### Transakce specifické pro protokol
Mezi vzory transakcí můžeme také identifikovat modely, které odhalují použití konkrétního protokolu. Například Whirlpool coinjoins budou mít snadno rozpoznatelnou strukturu, která je umožňuje odlišit od ostatních klasických transakcí.

![analýza](assets/en/6.webp)

Analýza tohoto vzoru naznačuje, že pravděpodobně jsme svědky kolaborativní transakce. Je také možné pozorovat coinjoin. Pokud se tato poslední hypotéza ukáže být přesná, pak počet výstupů by nám mohl poskytnout přibližný odhad počtu účastníků.

Například zde je Bitcoinová transakce, která přijímá vzor kolaborativního typu transakce coinjoin:
[00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea](https://mempool.space/tx/00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea)
Existuje mnoho dalších protokolů, které mají své vlastní specifické struktury. Tak můžeme rozlišovat transakce typu Wabisabi nebo transakce Stamps, například.
## Heuristiky interních transakcí
Interní heuristika je specifická charakteristika identifikovaná v rámci samotné transakce, bez nutnosti zkoumat její prostředí, což nám umožňuje dělat závěry. Na rozdíl od vzorců, které se zaměřují na celkovou strukturu transakce, jsou interní heuristiky založeny na sadě extrahovatelných dat. To zahrnuje:
- Množství různých UTXO jak příchozích, tak odchozích;
- Vše související se skripty: přijímací adresy, verzování, locktimes...

Obecně tento typ heuristiky nám umožňuje identifikovat změnu v konkrétní transakci. Tímto způsobem můžeme pak pokračovat ve sledování entity přes několik různých transakcí.

Opět připomínám, že tyto heuristiky nejsou absolutně přesné. Vzaté jednotlivě, umožňují nám identifikovat pravděpodobné scénáře. Je to akumulace několika heuristik, která přispívá ke snížení nejistoty, aniž by ji kdy úplně eliminovala.

### Interní podobnosti
Tato heuristika zahrnuje studium podobností mezi vstupy a výstupy téže transakce. Pokud je stejná charakteristika pozorována na vstupech a pouze na jednom z výstupů transakce, pak je pravděpodobné, že tento výstup představuje změnu.

Nejzřetelnější charakteristikou je opětovné použití přijímací adresy ve stejné transakci.

![analýza](assets/en/7.webp)

Tato heuristika nechává málo prostoru pro pochybnosti. Pokud nebyl jejich soukromý klíč kompromitován, stejná přijímací adresa nevyhnutelně odhaluje aktivitu jednoho uživatele. Interpretace, která následuje, je, že změna transakce je výstup se stejnou adresou jako vstup. To nám umožňuje pokračovat ve sledování jednotlivce od této změny.

Například, zde je transakce, kde by tato heuristika pravděpodobně mohla být aplikována:
[54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0](https://mempool.space/tx/54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0)

Tyto podobnosti mezi vstupy a výstupy nekončí pouze u opětovného použití adresy. Jakákoli podobnost v použití skriptů může umožnit aplikaci heuristiky. Například, někdy lze pozorovat stejné verzování mezi vstupem a jedním z výstupů transakce.

![analýza](assets/en/8.webp)
Na tomto diagramu vidíme, že vstup číslo 0 odemyká skript P2WPKH (SegWit V0 začínající na "bc1q"). Výstup číslo 0 používá stejný typ skriptu. Avšak výstup číslo 1 používá skript P2TR (SegWit V1 začínající na "bc1p"). Interpretace této charakteristiky je, že je pravděpodobné, že adresa se stejným verzováním jako vstup je adresa změny. Tudíž by stále patřila stejnému uživateli.
Zde je transakce, kde by tato heuristika pravděpodobně mohla být aplikována:
[db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578](https://mempool.space/tx/db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578)
V této transakci můžeme vidět, že vstup číslo 0 a výstup číslo 1 používají skripty P2WPKH (SegWit V0), zatímco výstup číslo 0 používá jiný typ skriptu, P2PKH (Legacy).
### Platby s Kulatými Částkami
Další interní heuristika, která nám může pomoci identifikovat změnu, je ta s kulatými částkami. Obecně, když se setkáme s jednoduchým platebním vzorcem (1 vstup a 2 výstupy), pokud jeden z výstupů utratí kulatou částku, pak představuje platbu.

![analýza](assets/en/9.webp)

Procesem eliminace, pokud jeden výstup představuje platbu, druhý představuje změnu. Proto můžeme interpretovat, že je pravděpodobné, že uživatel na vstupu stále vlastní výstup identifikovaný jako změna.

Je třeba poznamenat, že tato heuristika není vždy použitelná, protože většina plateb je stále prováděna v jednotkách fiat měn. Skutečně, když obchodník ve Francii přijímá bitcoiny, obvykle neuvádějí stabilní ceny v sats. Raději by zvolili konverzi mezi cenou v eurech a množstvím bitcoinů k zaplacení. Proto by v transakčním výstupu nemělo být kulaté číslo. Nicméně, analytik by se mohl pokusit provést tuto konverzi s přihlédnutím k směnnému kurzu platnému v době vysílání transakce v síti.

Pokud se jednoho dne bitcoin stane preferovanou jednotkou účtu v našich výměnách, tato heuristika by mohla být ještě užitečnější pro analýzu.

Například, zde je transakce, kde by tato heuristika pravděpodobně mohla být použita:
### Velká Utrata

Když je zjištěn dostatečně velký rozdíl mezi dvěma výstupy transakce v jednoduchém platebním modelu, lze odhadnout, že větší výstup je pravděpodobně změna.

![analýza](assets/en/10.webp)

Tato heuristika největšího výstupu je pravděpodobně nejméně přesná ze všech. Pokud je identifikována samostatně, je poměrně slabá. Tato charakteristika však může být kombinována s dalšími heuristikami, aby se snížila nejistota naší interpretace.

Například, pokud zkoumáme transakci, která obsahuje výstup s kulatou částkou a další výstup s větší částkou, společné použití heuristiky kulatých plateb a té týkající se největšího výstupu nám umožňuje snížit naši úroveň nejistoty.

Například, zde je transakce, kde by tato heuristika pravděpodobně mohla být použita:
[b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf](https://mempool.space/tx/b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf)

## Externí Heuristiky k Transakci
Studium externích heuristik je analýza podobností, vzorců a charakteristik určitých prvků, které nejsou vlastní samotné transakci. Jinými slovy, pokud jsme se dříve omezili na využívání prvků vnitřních k transakci pomocí interních heuristik, nyní rozšiřujeme naše pole analýzy na prostředí transakce díky externím heuristikám.

### Opakované Použití Adresy
To je jedna z nejznámějších heuristik mezi Bitcoinery. Opakované použití adresy umožňuje navázat spojení mezi různými transakcemi a různými UTXOs. Pozoruje se, když je adresa pro příjem Bitcoinů použita vícekrát.

Interpretace opakovaného použití adresy je, že všechny UTXOs uzamčené na této adrese patří (nebo patřily) téže entitě. Tato heuristika nechává málo prostoru pro nejistotu. Když je identifikována, následná interpretace má velkou šanci odpovídat realitě.
Jak je vysvětleno v úvodu, tuto heuristiku objevil sám Satoshi Nakamoto. Ve White Paperu konkrétně zmíní řešení, jak zabránit uživatelům v jejím vytváření, což je jednoduše použití nové adresy pro každou novou transakci: "*Jako další ochrannou bariéru lze pro každou transakci použít nový pár klíčů, aby byly udrženy nespojené s jedním společným majitelem.*"
Například zde je adresa použitá pro více transakcí:
[bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0](https://mempool.space/address/bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0)

### Podobnost skriptů a otisky peněženek
Kromě opakovaného používání adres existuje mnoho dalších heuristik, které mohou spojovat akce se stejnou peněženkou nebo s klastrem adres.

Za prvé, analytik může použít podobnosti ve využívání skriptů. Například určité minoritní skripty jako multisig mohou být snáze identifikovatelné než skripty SegWit V0. Čím větší skupinu se nám podaří skrýt, tím těžší je nás identifikovat. To je významně důvod, proč při protokolu Coinjoin Whirlpool všichni účastníci používají přesně stejný typ skriptu.

Šířeji vzato, analytik se může také zaměřit na charakteristické otisky peněženky. Jsou to specifické procesy používání, které by někdo mohl hledat k identifikaci, aby je využil jako sledovací heuristiky. Jinými slovy, pokud někdo pozoruje akumulaci stejných vnitřních charakteristik na transakcích připsaných sledované entitě, může se pokusit tyto stejné charakteristiky identifikovat na dalších transakcích.

Například lze identifikovat, že sledovaný uživatel systematicky posílá svou změnu na adresy P2TR* (bc1p…). Pokud se tento proces opakuje, může být použit jako heuristika pro pokračování naší analýzy. Další otisky mohou být také použity, jako je pořadí UTXO, umístění změny ve výstupech, signalizace RBF (Replace-by-Fee), nebo dokonce číslo verze a locktime.
Jak [@LaurentMT](https://twitter.com/LaurentMT) specifikuje v [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) (frankofonní podcast), užitečnost otisků peněženek v analýze řetězce významně roste s časem. Skutečně, rostoucí počet typů skriptů a stále postupnější nasazování těchto nových funkcí softwary peněženek zvýrazňuje rozdíly. Dokonce se stává, že lze přesně identifikovat software používaný sledovanou entitou. Proto je důležité pochopit, že studium otisku peněženky je zvláště relevantní pro nedávné transakce, více než pro ty, které byly zahájeny na počátku 2010s.
Shrnutí, otisk může být jakákoli specifická praxe, prováděná automaticky peněženkou nebo ručně uživatelem, která může být nalezena na dalších transakcích, aby pomohla v naší analýze.

### CIOH
CIOH, pro "Common Input Ownership Heuristic," což by se dalo přeložit jako "heuristika společného vlastnictví vstupů" nebo "heuristika společného utrácení," je heuristika tvrdící, že když má transakce více vstupů, pravděpodobně všechny pocházejí od jedné entity. Důsledkem je, že jejich vlastnictví je společné.
Pro aplikaci CIOH nejprve pozorujeme transakci, která má více vstupů. To může být dva vstupy stejně jako třicet vstupů. Jakmile je tato charakteristika rozpoznána, kontroluje se, zda transakce nespadá do známého vzoru. Například, pokud má 5 vstupů s přibližně stejným množstvím a 5 výstupů s přesně stejným množstvím, víme, že jde o strukturu Coinjoin Whirlpool. Proto CIOH nelze aplikovat.
Pokud však transakce nespadá do žádného známého vzoru kolaborativní transakce, pak lze interpretovat, že všechny vstupy pravděpodobně pocházejí od stejné entity. To může být velmi užitečné pro rozšíření již známého klastru nebo pro pokračování v sledování.

![analýza](assets/en/11.webp)

CIOH objevil Satoshi Nakamoto. Diskutuje o tom v části 10 White Paper: "*[...] spojení je nevyhnutelné u transakcí s více vstupy, které nutně odhalují, že jejich vstupy vlastnil stejný majitel. Riziko je, že pokud je majitel klíče odhalen, spojení může odhalit další transakce, které patřily stejnému majiteli.*"
Je obzvláště fascinující poznamenat, že Satoshi Nakamoto, ještě před oficiálním spuštěním Bitcoinu, již identifikoval dvě hlavní slabiny soukromí uživatelů, a to CIOH a opětovné použití adresy. Takový předvídavost je poměrně pozoruhodná, jelikož tyto dvě heuristiky zůstávají, i dnes, nejužitečnějšími v analýze řetězce.

### Data mimo řetězec
Samozřejmě, analýza řetězce není omezena pouze na data na řetězci. Jakákoli data z předchozí analýzy nebo přístupná na internetu mohou být také použita k upřesnění analýzy.

Například, pokud je pozorováno, že sledované transakce jsou systematicky vysílány ze stejného Bitcoinového uzlu a jeho IP adresa může být identifikována, může být možné odhalit další transakce od stejné entity.

Analytik má také možnost spoléhat na analýzy, které byly dříve zveřejněny jako open-source, nebo na vlastní předchozí analýzy. Možná by se mohlo najít výstup, který ukazuje na klastr adres, který byl již identifikován. Někdy je také možné spoléhat na výstupy, které ukazují na burzu, adresy těchto platform jsou obecně známé.

Podobně, lze provádět analýzu vyloučením. Například, pokud během analýzy transakce se dvěma výstupy je jeden z nich spojen s známým, ale odlišným klastrem adres od sledované entity, pak lze interpretovat, že druhý výstup pravděpodobně představuje vrácení peněz.

Analýza řetězce také zahrnuje část OSINT (Open Source Intelligence), která je trochu více generalistická s internetovými vyhledáváními. To je důvod, proč se nedoporučuje přímo zveřejňovat přijímací adresy na sociálních médiích nebo na webové stránce, ať už pod pseudonymem nebo ne.

### Časové modely
Na první pohled by na to člověk nemusel pomyslet, ale určité lidské chování je rozpoznatelné na řetězci. Nejužitečnější ve studii je váš spánkový vzor! Ano, když spíte, pravděpodobně neodesíláte Bitcoinové transakce. Jelikož obvykle spíte v přibližně stejných hodinách, je běžné používat časové analýzy v analýze na řetězci. Jednoduše zahrnuje zaznamenávání časů, kdy jsou transakce dané entity vysílány do Bitcoinové sítě. Analýza těchto časových vzorů nám umožňuje odvodit mnoho informací.
Především časová analýza může někdy identifikovat povahu entity, která je sledována. Pokud pozorujeme, že transakce jsou konzistentně vysílány 24 hodin denně, může to naznačovat silnou ekonomickou aktivitu. Entita za těmito transakcemi je pravděpodobně podnik, potenciálně mezinárodní, a možná s automatizovanými procedurami interně.
Například jsem tento vzor rozpoznal před několika týdny, když jsem analyzoval transakci, která omylem přiřadila 19 bitcoinů na poplatky. Jednoduchá časová analýza mi umožnila hypotetizovat, že máme co do činění s automatizovanou službou, a tedy pravděpodobně s velkou entitou, jako je burza: https://twitter.com/Loic_Pandul/status/1701127409712452072
Skutečně, o několik dní později bylo objeveno, že prostředky patřily PayPalu prostřednictvím burzy Paxos.

Naopak, pokud vidíme, že časový vzor je spíše rozložený přes 16 konkrétních hodin, pak můžeme odhadnout, že máme co do činění s individuálním uživatelem, nebo možná s místním podnikem v závislosti na objemech vyměněných.

Kromě povahy pozorované entity nám časový vzor může také dát přibližnou polohu uživatele. Můžeme tedy korelovat další transakce a použít časové razítko těchto jako další heuristiku, kterou můžeme přidat do naší analýzy.

Například na adrese, která byla několikrát znovu použita, kterou jsem dříve zmínil, lze pozorovat, že transakce, ať už příchozí nebo odchozí, jsou soustředěny do 13hodinového intervalu.
![analýza](assets/notext/12.webp)
*Kredit: OXT*

Tento interval pravděpodobně odpovídá Evropě, Africe nebo Střednímu východu. Proto lze interpretovat, že uživatel za těmito transakcemi žije tam.

V jiném rejstříku je také časová analýza tohoto typu, která umožnila hypotézu, že Satoshi Nakamoto neoperuje z Japonska, ale skutečně ze Spojených států: [https://medium.com/@insearchofsatoshi/the-time-zones-of-satoshi-nakamoto-aa40f035178f](https://medium.com/@insearchofsatoshi/the-time-zones-of-satoshi-nakamoto-aa40f035178f)

### Analýza objemů
Další externí heuristika, která může být použita, je analýza obchodních objemů. Na základě částek přítomných v každé transakci přiřazené entitě může být tato informace použita jako další heuristika pro zbytek analýzy.
Tato heuristika je samozřejmě poměrně slabá, ale může pomoci snížit nejistotu, když je přidána k dalším heuristikám.

## Jak se chránit proti analýze řetězce?
Jako uživatel Bitcoinu máte právo chránit své soukromí. To vyplývá z vašich přirozených práv vlastnit a nakládat se sebou, která jsou každému jednotlivci vlastní, bez ohledu na jakékoli legislativní omezení.

Toto přirozené právo chránit své soukromí je také převedeno na nárokové právo, zakotvené v článku 12 Všeobecné deklarace lidských práv, který uvádí, že "*Nikdo nesmí být podroben libovolnému zasahování do svého soukromí, rodiny, domova nebo korespondence, ani útokům na svou čest a pověst. Každý má právo na ochranu zákona proti takovému zasahování nebo útokům.*".

Nicméně, hlavní činností společností specializujících se na analýzu řetězce spočívá právě v pronikání do vašeho soukromí, čímž kompromituje důvěrnost vaší korespondence. Zatímco bychom mohli doufat, že v souladu s výše uvedeným nárokovým právem by státy naši soukromí energicky bránily, nejenže tak činí nedostatečně, ale také významně financují financování těchto analytických společností. Bylo by také marné doufat v podporu od sektorových asociací, které se zdají být ochotny udělat všechny ústupky vůči zákonodárci.

De facto, toto nárokové právo na soukromí v Bitcoinu neexistuje. Je tedy na vás, uživateli, abyste prosadili své přirozené právo a chránili důvěrnost své korespondence. To zahrnuje přijetí různých technik a způsobů použití, které vám umožní předejít nebo oklamat heuristiky používané pro analýzu řetězce.

### Vyhnout se padání do heuristik
Především, než zvážíme radikálnější metody, je vhodné co nejvíce omezit naši expozici heuristikám používaným pro analýzu řetězce. Jak bylo zmíněno dříve, dvě nejmocnější heuristiky jsou opětovné použití adresy a COINJOIN.
Základním principem pro zajištění vašeho soukromí na Bitcoinu je používání nové, čisté adresy pro každou příchozí transakci do vaší peněženky. Opětovné použití adresy je opravdu hlavní hrozbou pro důvěrnost na Bitcoinu.
Pro jednotlivého uživatele je generování nové adresy pro každou příchozí platbu velmi jednoduché. Moderní peněženky to dělají automaticky, jakmile kliknete na "Přijmout". Takže, pokud kladeš i nejmenší důraz na soukromí svých transakcí, používání nových adres představuje absolutní minimum. Pokud někdy potřebujete statický kontaktní bod na internetu, místo zadání přijímací adresy můžete použít řešení [jako je PayNym, které implementuje BIP47](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093).
Dále, pokud chcete jednat proti analýze řetězce, vyhněte se sloučení UTXO na vstupu transakce. Minimálně, pokud opravdu potřebujete sloučit, preferujte UTXO, které mají stejný zdroj. Toto doporučení znamená mít dobrou správu vašich UTXO. Při nákupu vašich bitcoinů preferujte převody zahrnující velké částky, abyste maximalizovali počet plateb, které můžete provést bez nutnosti sloučení. Také doporučuji označit vaše UTXO ve vašem softwaru, abyste identifikovali jejich původ a vyhnuli se sloučení z různých zdrojů.

Obecněji, pro všechny ostatní heuristiky, potřebujete je znát, abyste se pokusili do nich nespadnout:
- Nepoužívejte minoritní skripty. Preferujte SegWit V0 nebo možná SegWit V1;
- Neprovádějte platby v kulatých číslech. Například, pokud potřebujete poslat 100k sats příteli, pošlete mu 114,486 sats. On vám za to koupí nápoj;
- Snažte se nemít vždy změnu, která je mnohem větší než výstup platby;
- Nepublikujte vaše přijímací adresy na sociálních médiích;
- Používejte vlastní uzel pod Tor pro vysílání vašich transakcí;
- Snažte se nevysílat vaše Bitcoinové transakce vždy ve stejný čas…

### Používání nástrojů pro soukromí
Můžete také přejít k metodám, které činí vaše používání Bitcoinu nejednoznačným, aby se předešlo nebo oklamala analýza řetězce.

Nejpopulárnější technikou je jistě Coinjoin, kolaborativní struktura transakce, která mobilizuje několik UTXO stejných částek. Cílem zde je přerušit deterministické vazby, čímž se zabrání analýzám od současnosti do minulosti a od minulosti do současnosti. Coinjoin umožňuje věrohodné popření tím, že skrývá vaše mince v rámci velké skupiny nerozlišitelných mincí. Pokud se chcete dozvědět více o Coinjoin, jak technicky, tak prakticky, doporučuji si přečíst tyto další články a tutoriály:
- [COINJOIN - SAMOURAI WALLET](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef);
- [COINJOIN - SPARROW WALLET](https://planb.network/tutorials/privacy/on-chain/coinjoin-sparrow-wallet-84def86d-faf5-4589-807a-83be60720c8b);
- [WHIRLPOOL STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375).
![analýza](assets/en/13.webp)

CoinJoin je vynikajícím nástrojem pro vytvoření věrohodného popření pro mince, ale není optimalizován pro všechny potřeby soukromí uživatelů. Konkrétně, CoinJoin nebyl navržen, aby se stal platebním nástrojem. Je velmi striktní co se týče částek vyměněných za účelem dokonalé produkce věrohodného popření. Jelikož nelze volně vybírat částku výstupů transakce, CoinJoin nelze použít k provedení plateb v bitcoinech.
Například si představte, že chci zaplatit za svou bagetu v bitcoinech, přičemž chci optimalizovat své soukromí. Vzhledem k nemožnosti vybrat množství výsledného UTXO z CoinJoin bych se ocitl neschopen přizpůsobit množství mého výdaje ceně stanovené pekařem. Proto se CoinJoin ukazuje jako nedostatečný pro platební transakce.
Byly vymyšleny další nástroje, které splňují potřeby soukromí v konkrétnějších případů použití. Například máme [PayJoin](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f), druh mini-CoinJoin, který zahrnuje pouze dva účastníky a je založen na struktuře, která umožňuje platbu.

Unikátnost PayJoin spočívá v jeho schopnosti vyprodukovat transakci, která vypadá obyčejně, zatímco ve skutečnosti jde o mini-CoinJoin mezi dvěma uživateli. V této struktuře se příjemce transakce podílí na vstupech společně s vlastním odesílatelem. Takto příjemce vloží do transakce platbu sami sobě, která usnadňuje skutečnou platbu.

Například, pokud si kupujete bagetu od svého pekaře za 6 000 sats z UTXO 10 000 sats a chcete provést PayJoin, váš pekař přidá UTXO 15 000 sats, které jim patří, jako vstup do vaší původní transakce, kterou pak plně získají zpět jako výstup, aby oklamali heuristiku:

![analýza](assets/en/14.webp)

Transakční poplatky jsou zanedbány pro zjednodušení pochopení schématu.

Cíle PayJoin jsou dvojí. Zaprvé, jeho cílem je oklamat vnějšího pozorovatele vytvořením návnady prostřednictvím COH. Skutečně, když analytik pozoruje tuto transakci, bude si myslet, že může aplikovat COH, a tedy předpokládat společné vlastnictví různých vstupů. Ve skutečnosti je tento předpoklad nesprávný, protože jeden vstup patří odesílateli, zatímco druhý je ve vlastnictví příjemce. PayJoin tedy kazí analýzu řetězce tím, že analytika vede špatnou cestou.
Druhým cílem PayJoin je oklamat analytika o skutečném množství transakce díky specifické struktuře jejích výstupů. PayJoin se tedy řadí do oblasti steganografie. Umožňuje skrýt skutečnou částku transakce v rámci klamavé transakce.

Skutečně, pokud se vrátíme k našemu příkladu použití PayJoin k nákupu bagety, vnější pozorovatel by si mohl myslet, že jde o platbu 4 000 sats nebo 21 000 sats. Ve skutečnosti je platba za bagetu 6 000 sats: 21 000 - 15 000 = 6 000. Skutečná hodnota platby je tedy skryta v rámci falešné platby, která slouží jako návnada pro analýzu řetězce.

Kromě PayJoin a CoinJoin existuje mnoho dalších struktur transakcí Bitcoinu, které buď blokují analýzu řetězce, nebo ji oklamávají. Mezi tyto patří transakce [Stonewall](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4) a [StonewallX2](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b), které umožňují buď provést flexibilní mini Coinjoin, nebo napodobit flexibilní mini Coinjoin. Existují také transakce [Ricochet](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589), které simulují změnu vlastnictví bitcoinů tím, že provádějí množství falešných převodů na sebe sama.

Všechny tyto nástroje jsou dostupné na mobilní peněžence Samourai Wallet a na PC peněžence Sparrow Wallet. Pokud se chcete dozvědět více o těchto specifických strukturách transakcí, doporučuji objevit mé tutoriály:
- [PAYJOIN](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f);
- [PAYJOIN - SAMOURAI WALLET](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab);
- [PAYJOIN - SPARROW WALLET](https://planb.network/tutorials/privacy/on-chain/payjoin-sparrow-wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62);
- [STONEWALL](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4);
- [STONEWALL X2](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b);
- [RICOCHET](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589).

## Závěr
Analýza řetězce je praxe, která zahrnuje pokusy o sledování toku bitcoinů v blockchainu. Analytici k tomu hledají vzory a charakteristiky, aby mohli vyvodit více či méně pravděpodobné hypotézy a interpretace.

Přesnost těchto heuristik se liší: některé poskytují vyšší stupeň jistoty než jiné, ale žádná nemůže tvrdit, že je neomylná. Avšak akumulace několika konvergujících heuristik může tuto vrozenou pochybnost zmírnit, ačkoli je nemožné ji zcela eliminovat.
Tyto metody můžeme kategorizovat do tří zásadních hlavních kategorií:
- Vzory, zaměřené na celkovou strukturu každé transakce;
- Interní heuristiky, které umožňují vyčerpávající zkoumání všech detailů transakce, aniž by se rozšiřovaly na její kontext;
- Externí heuristiky, které zahrnují analýzu transakce v jejím prostředí, stejně jako jakákoli externí data, která mohou poskytnout vhled.

Pro uživatele Bitcoinu je zásadní ovládnout základní principy analýzy řetězce, aby ji účinně mohli čelit a tím chránit své soukromí.

## Technický mini-slovníček:
**P2PKH:** zkratka pro Pay to Public Key Hash. Jedná se o standardní skriptový model používaný k stanovení podmínek výdaje na UTXO. Umožňuje uzamknout bitcoiny na hash veřejného klíče, tj. na přijímací adresu. Tento skript je spojen se standardem Legacy a byl zaveden v prvních verzích Bitcoinu Satoshi Nakamotem. Na rozdíl od P2PK, kde je veřejný klíč explicitně zahrnut ve skriptu, P2PKH používá kryptografický otisk veřejného klíče s některými metadaty, také nazývanými "přijímací adresa". Tento skript zahrnuje hash RIPEMD160 hashu SHA256 veřejného klíče a stanoví, že pro přístup k prostředkům musí příjemce poskytnout veřejný klíč odpovídající tomuto hashi, stejně jako platný digitální podpis vygenerovaný z přidruženého soukromého klíče. Adresy P2PKH jsou kódovány pomocí formátu Base58Check, který jim dává odolnost proti typografickým chybám prostřednictvím použití kontrolního součtu. Tyto adresy vždy začínají číslem 1.
**P2TR:** zkratka pro Pay to Taproot ("platba do kořene"). Jedná se o standardní skriptový model používaný k určení podmínek výdaje na UTXO. P2TR byl představen s implementací Taprootu v listopadu 2021. Využívá protokol Schnorr pro agregaci kryptografických klíčů, stejně jako Merkleovy stromy pro alternativní skripty, známé jako MAST (Merkelized Alternative Script Tree). Na rozdíl od tradičních transakcí, kde jsou podmínky výdaje veřejně vystaveny (někdy při přijetí, někdy při výdaji), P2TR umožňuje skrýt složité skripty za jediným zdánlivě veřejným klíčem. Technicky skript P2TR uzamkne bitcoiny na unikátním veřejném klíči Schnorr, označeném jako K. Tento klíč K je však ve skutečnosti agregátem veřejného klíče P a veřejného klíče M, přičemž ten druhý je vypočítán z Merkleova kořene seznamu ScriptPubKeys. Agregace klíčů je prováděna pomocí protokolu podpisu Schnorr. Bitcoiny uzamčené skriptem P2TR lze utratit dvěma způsoby: buď zveřejněním podpisu pro veřejný klíč P, nebo splněním jednoho ze skriptů obsažených v Merkleově stromu. První možnost se nazývá "cesta klíče" a druhá "cesta skriptu". P2TR tedy umožňuje uživatelům posílat bitcoiny buď na veřejný klíč, nebo na více skriptů dle jejich výběru. Další výhodou tohoto skriptu je, že ačkoliv existuje více způsobů, jak utratit výstup P2TR, pouze ten použitý musí být odhalen při utrácení, což umožňuje, aby nevyužité alternativy zůstaly soukromé. Například díky agregaci klíčů Schnorr může být veřejný klíč P sám agregovaným klíčem, potenciálně reprezentujícím multisig. P2TR je výstup SegWit verze 1, což znamená, že podpisy pro vstupy P2TR jsou uloženy ve svědkovi transakce, a ne ve ScriptSig. Adresy P2TR používají kódování Bech32m a začínají na bc1p.

**P2WPKH:** Zkratka pro Pay to Witness Public Key Hash. Jedná se o standardní skriptový model používaný k určení podmínek výdaje na UTXO. P2WPKH byl zaveden s implementací SegWit v srpnu 2017. Tento skript je podobný P2PKH (Pay to Public Key Hash), protože také uzamkne bitcoiny na základě hashe veřejného klíče, tj. přijímací adresy. Rozdíl spočívá v tom, jak jsou podpisy a skripty zahrnuty do transakce. V případě P2WPKH jsou informace skriptu podpisu (ScriptSig) přesunuty z tradiční struktury transakce do samostatné sekce nazvané Witness. Tento krok je funkcí aktualizace SegWit (Segregated Witness). Tato technika má tu výhodu, že snižuje velikost dat transakce v hlavním těle, zatímco nezbytné informace skriptu pro validaci jsou uchovány v samostatné sekci. V důsledku toho jsou transakce P2WPKH obecně méně nákladné z hlediska poplatků ve srovnání s Legacy transakcemi. Adresy P2WPKH jsou psány pomocí kódování Bech32, což přispívá k stručnějšímu a méně náchylnému zápisu díky kontrolnímu součtu BCH. Tyto adresy vždy začínají na bc1q, což je činí snadno rozlišitelnými od Legacy přijímacích adres. P2WPKH je výstup SegWit verze 0.
**UTXO:** Zkratka pro Unspent Transaction Output (Nevyčerpaný výstup transakce). UTXO je výstup transakce, který ještě nebyl utracen nebo použit jako vstup pro novou transakci. UTXO představují část bitcoinů, které uživatel vlastní a které jsou v současné době dostupné k utracení. Každé UTXO je spojeno s konkrétním výstupním skriptem, který definuje potřebné podmínky pro utracení bitcoinů. Transakce v Bitcoinu spotřebovávají tyto UTXO jako vstupy a vytvářejí nové UTXO jako výstupy. Model UTXO je základní pro Bitcoin, protože umožňuje snadnou verifikaci, že transakce se nepokouší utratit bitcoiny, které neexistují nebo již byly utraceny. V podstatě je UTXO kus Bitcoinu.






