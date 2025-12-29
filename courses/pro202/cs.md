---
name: Programování Bitcoin
goal: Vytvoření kompletní knihovny Bitcoin od nuly a pochopení kryptografických základů Bitcoin
objectives: 

 - Implementace aritmetiky konečného pole a operací s eliptickými křivkami v jazyce Python
 - Programová konstrukce a analýza transakcí Bitcoin
 - Vytvoření adres testnetu a vysílání transakcí po síti
 - Zvládnutí matematických základů bezpečnostního modelu Bitcoin

---
# Cesta do skriptů a programů Bitcoin


Tento intenzivní dvoudenní kurz, který vede Jimmy Song, vás zavede hluboko do technických základů Bitcoin a umožní vám vytvořit kompletní knihovnu Bitcoin od základů. Začínáte základní matematikou konečných polí a eliptických křivek a postupujete přes zpracování transakcí, provádění skriptů a síťovou komunikaci. Prostřednictvím praktických kódovacích cvičení v zápisnících Jupyter si vytvoříte vlastní adresu testnetu, ručně zkonstruujete transakce a budete je vysílat přímo do sítě - to vše při hlubokém pochopení kryptografických principů, díky nimž je Bitcoin bezpečný a důvěryhodný.


Užijte si cestu!


+++

# Úvod


<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>


## Přehled kurzů


<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>


Vítejte v kurzu PRO 202 _**Programování Bitcoin**_, který vás intenzivně provede od aritmetiky konečných polí až k vytváření a vysílání reálných transakcí na Bitcoin Testnet.


V tomto kurzu postupně vytvoříte knihovnu Bitcoin v jazyce Python a zároveň si osvojíte základy kryptografie, protokolů a softwaru, které jsou nezbytné pro přesné zdůvodnění bezpečnosti a vnitřního fungování Bitcoin. Přístup PRO 202 je důsledně praktický: každý koncept je okamžitě implementován v zápisnících Jupyter, což zajišťuje, že teorie a kód se vzájemně posilují.


### Základní matematické pojmy pro Bitcoin


V této první části jsou uvedeny nezbytné matematické základy. Zavedete aritmetiku konečného pole a operace s eliptickými křivkami (grupový zákon, sčítání, zdvojení, skalární násobení...) - předpoklady pro ECDSA. Cíl je dvojí: pochopit algebraickou strukturu, která umožňuje kryptografické podpisy, a vytvořit spolehlivé nástroje pro práci s nimi v jazyce Python.


Poté si formalizujete součásti ECDSA: generování klíčů, formátování bodů, hašování, vytváření podpisů a ověřování. Tato část přímo propojuje teorii s praxí a klade důraz na implementační detaily a robustnost základního bezpečnostního modelu.


### Vnitřní fungování transakce Bitcoin


Ve druhé části rozeberete strukturu transakce Bitcoin: UTXO, vstupy/výstupy, sekvence, skripty, kódování a další. Budete psát kód pro konstrukci, podepisování a ověřování transakcí a získáte přesné znalosti o tom, co a proč je odevzdáváno pomocí hash.


Dále implementujete minimální _Script_ executor, zkontrolujete klíčové opcodes a ověříte výdajové cesty. Cílem je, abyste byli schopni kontrolovat chování transakcí, diagnostikovat selhání validace a uvažovat o bezpečnosti výdajových politik.


### Vnitřní fungování sítě Bitcoin


Ve třetím oddíle se pokusíte zařadit transakce do širšího systému: struktura bloků, hlavičky, obtížnost a mechanismus Proof-of-Work. Budete zpracovávat zprávy protokolu, hlavičky bloků a Merklovy stromy.


Nakonec se seznámíte s komunikací mezi uzly peer-to-peer, optimalizací zpráv a zavedením SegWit.


Stejně jako u každého kurzu Plan ₿ Academy obsahuje závěrečná část hodnocení, jehož cílem je upevnit vaše znalosti. Jste připraveni odhalit vnitřní fungování Bitcoin a napsat kód, který jej pohání? Začněme!










# Základní matematické pojmy pro Bitcoin

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Matematika pro implementaci Bitcoin

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>


![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


### Bitcoin Základy programování: Základní matematické struktury


Tento kurz shrnuje základní matematiku kryptografických systémů Bitcoin do vysoce praktického pracovního postupu. Koncepty jsou vysvětleny, demonstrovány na příkladech a následně implementovány v Jupyter Notebooku. Hlavní myšlenka je jednoduchá: kryptografickému primitivu skutečně porozumíte, až když ho nakódujete. V průběhu dvoudenní struktury studenti generate testují adresy sítě, vytvářejí a vysílají transakce a nakonec komunikují se sítí bez blokových průzkumníků. To vše vyžaduje solidní základy v oblasti konečných polí a eliptických křivek.


### Konečná pole: Aritmetický motor kryptografie


Konečné pole F(p) je aritmetický systém definovaný prvočíslem p, který obsahuje prvky 0 až p-1. Prvočíselné pole zajišťuje, že každý nenulový prvek má inverzní prvek a všechny operace zůstávají v rámci pole. Aritmetika se obklopuje použitím modulo p pro sčítání, odčítání a násobení. Pythonovská funkce `pow(base, exp, mod)` umožňuje efektivní modulární exponencializaci, která je klíčová pro velké exponenty používané v reálných kryptografických operacích.


#### Multiplikativní chování

Vynásobením libovolného nenulového prvku k všemi prvky prvočíselného pole vznikne permutace pole. Tato vlastnost zaručuje uniformitu a zabraňuje strukturálním slabinám, takže prvočíselná pole jsou ideální pro bezpečné generování klíčů a digitálních podpisů.


#### Dělení a Fermatova malá věta

Dělení se provádí pomocí multiplikativních inverzí. Fermatova malá věta říká, že

n^(p-1) ≡ 1 (mod p),

takže inverzní hodnota je n^(p-2). Python to podporuje přímo pomocí `pow(n, -1, p)`. Tyto operace se neustále objevují v základních kryptografických rutinách ECDSA a Bitcoin.


### Eliptické křivky: Nelineární struktury pro bezpečnost veřejných klíčů


Eliptické křivky se řídí rovnicí y² = x³ + ax + b. Bitcoin používá secp256k1, definovanou jako y² = x³ + 7 nad konečným polem. Body na eliptické křivce tvoří matematickou grupu při sčítání bodů. Přímka vedená dvěma body P a Q protíná křivku ve třetím bodě R; odrazem R přes osu x získáme P + Q. Tato soustava je asociativní a obsahuje prvek identity: bod v nekonečnu.


Při zdvojení bodu se místo úsečky použije tečna, jejíž sklon je odvozen z derivace křivky. Ačkoli tyto vzorce zahrnují výpočet nad reálnými čísly, stávají se plně diskrétními a přesnými, když je křivka definována nad konečným polem - což je kontext použitý v Bitcoin.


### Od matematiky ke kryptografii Bitcoin


Konečná pole poskytují deterministickou, inverzní aritmetiku; eliptické křivky poskytují nelineární strukturu, kde je výpočet k-P snadný, ale jeho obrácení je výpočetně neproveditelné. Kombinace obojího je základem pro veřejné a soukromé klíče Bitcoin, podpisy ECDSA a zabezpečení transakcí. Pochopení těchto základů připraví studenty na přímou implementaci klíčů, transakcí a podpisů - bez abstrakcí nebo externích nástrojů.


## Kryptografie eliptických křivek

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>


![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


Tato kapitola představuje eliptické křivky definované nad konečnými poli a vysvětluje, proč tvoří matematickou páteř kryptografie Bitcoin. Zatímco eliptické křivky nad reálnými čísly se jeví jako hladké a spojité, při použití stejných rovnic nad konečným polem vzniká diskrétní, rozptýlená množina bodů. Navzdory vizuálnímu rozdílu se všechny vzorce pro sčítání bodů, sklony a algebraická pravidla chovají naprosto stejně - pouze aritmetika se mění na modulární aritmetiku. Bitcoin používá křivku y² = x³ + 7 (secp256k1), která zachovává symetrii a nelineární chování důležité pro kryptografickou bezpečnost.


### Ověřování bodů a implementace konečného pole


Bod leží na eliptické křivce s konečným polem, pokud jeho souřadnice splňují rovnici křivky pod modulo p. Ověření bodu, jako je (73,128) na F₁₃₇, vyžaduje ověření, že y² mod p se rovná x³ + 7 mod p. Implementace tohoto postupu v kódu zahrnuje vytvoření tříd pro prvky konečného pole a body křivky. Přetěžování operátorů zajišťuje, že veškerá aritmetika - sčítání, násobení, exponentizace, dělení - se automaticky provádí modulo p. Jakmile tyto abstrakce existují, je jednodušší psát a zdůvodňovat pokročilejší kryptografické operace.


#### Vlastnosti skupiny a sčítání bodů

Body eliptických křivek tvoří matematickou skupinu při sčítání. Tato grupa splňuje podmínky uzavřenosti, asociativity, identity (bod v nekonečnu) a inverze (odraz přes osu x). Geometrické konstrukce tyto vlastnosti potvrzují, takže skalární násobení (P opakovaně přičítané k sobě samému) je dobře definováno. Tato skupinová pravidla umožňují kryptografii eliptických křivek a zajišťují konzistentní, předvídatelné chování při opakovaných operacích s body.


### Cyklické grupy a problém diskrétního logaritmu


Výběr generátorového bodu G na křivce nám umožňuje generate cyklickou grupu: G, 2G, 3G, ..., nG = 0. Body se jeví jako nelineární a nepředvídatelné, i když jsou generovány postupně. Tato nepředvídatelnost vytváří základ problému diskrétního logaritmu: výpočet P = sG je snadný, ale určení s z P je pro velké grupy výpočetně neproveditelné. Díky této jednosměrné funkci je kryptografie s veřejným klíčem bezpečná. Skaláry (soukromé klíče) se zapisují malými písmeny, body (veřejné klíče) velkými.


#### Efektivní skalární násobení

Pro efektivní výpočet sG používají implementace algoritmus double-and-add: skenování binární reprezentace skaláru, zdvojnásobení bodu v každém kroku a přičtení G pouze tehdy, když je bit 1. To snižuje výpočet z O(n) přičtení na O(log n), což umožňuje praktické kryptografické operace i s 256bitovými skaláry.


#### Křivka secp256k1 v Bitcoin


Bitcoin používá křivku secp256k1 definovanou vztahem y² = x³ + 7 nad prvočíselným polem, kde p = 2²⁵⁶ - 2³² - 977. Generátorový bod G má pevné souřadnice zvolené deterministickým postupem NUMS ("nic v rukávu"). Řád grupy n je velké prvočíslo blízké 2²⁵⁶, což zajišťuje, že každý nenulový bod generuje stejnou grupu. Velikost 2²⁵⁶ (~10⁷⁷) je astronomicky velká, což fyzicky znemožňuje hrubé vynucení soukromých klíčů. Ani bilion superpočítačů běžících bilion let by prostor klíčů významně nezmenšil.


### Veřejné klíče, soukromé klíče a serializace SEC


Soukromý klíč je náhodný skalár s; veřejný klíč je P = sG. Protože řešení problému diskrétního logu je neproveditelné, lze P sdílet bez odhalení s. Veřejné klíče musí být pro přenos serializovány pomocí formátu SEC. Nekomprimovaný formát SEC používá 65 bajtů: prefix 0x04 + x-ová souřadnice + y-ová souřadnice. Komprimovaný formát používá pouze 33 bajtů: prefix 0x02 nebo 0x03 (podle parity y) + souřadnice x. Bitcoin původně používal nekomprimované klíče, ale nyní kvůli efektivitě dává přednost komprimovaným.


#### Bitcoin Address Vytvoření


Adresy Bitcoin jsou hashe veřejných klíčů, nikoli samotné surové klíče. Chcete-li adresu generate, serializujte veřejný klíč ve formátu SEC, vypočítejte hash160 (SHA-256 a poté RIPEMD-160), přidejte prefix sítě (0x00 pro mainnet, 0x6F pro testnet), vypočítejte kontrolní součet pomocí dvojnásobku SHA-256, připojte první čtyři bajty kontrolního součtu a výsledek zakódujte pomocí Base58. Toto kódování odstraňuje nejednoznačné znaky a obsahuje kontrolní součet, aby se zabránilo chybám při přepisu. Tento vícekrokový postup skrývá veřejný klíč, dokud nedojde k útratě, přidává identifikaci sítě a zajišťuje lidsky čitelné adresy odolné proti chybám.


# Vnitřní fungování transakce Bitcoin

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Parsování transakcí Bitcoin a podpisy ECDSA

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>


![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


### Principy ECDSA: základ digitálního podpisu Bitcoin


Bitcoin se spoléhá na ECDSA, podpisové schéma založené na eliptické křivce, které nabízí silné zabezpečení s mnohem menší velikostí klíče než RSA. Jeho bezpečnost vychází z problému diskrétního logaritmu eliptických křivek: při zadání P = eG je výpočet P snadný, ale odvození e z P je výpočetně neproveditelné. Tato asymetrie umožňuje kryptografii s veřejným klíčem při zachování bezpečnosti soukromých klíčů.


#### Kódování podpisů ECDSA pomocí DER


Bitcoin kóduje podpisy ECDSA pomocí formátu DER:


- 0x30 (značka sekvence)
- délka bajtu
- 0x02 + délka + R bajtů
- 0x02 + délka + S bajtů


To zvyšuje režii a rozšiřuje 64bajtový podpis na ~71-72 bajtů. Taproot tuto neefektivitu eliminuje přijetím Schnorrových podpisů s pevnou velikostí.


### Podpisové závazky a proces podepisování


Podpisy ECDSA jsou založeny na rovnici závazku: UG + VP = KG. Podepisující osoba si zvolí nenulové hodnoty U a V a náhodnou nonce K, čímž prokáže znalost soukromého klíče, aniž by jej prozradila. Zpráva se zahesluje do Z, vygeneruje se náhodná K, R je x-ová souřadnice KG a S = (Z + RE)/K. Podpis je dvojice (R, S). Bezpečnost kriticky závisí na použití jedinečného, nepředvídatelného K - pokud je K opakovaně použit nebo unikne, je soukromý klíč kompromitován. Moderní implementace používají deterministické generování K (RFC 6979), aby se zabránilo selhání RNG.


#### Ověřování podpisu

Při zadání Z, (R, S) a veřejného klíče P verifikátor vypočítá U = Z/S a V = R/S a pak zkontroluje, zda se x-ová souřadnice UG + VP rovná R. To funguje, protože verifikační algebra rekonstruuje KG, aniž by potřebovala soukromý klíč. Padělání podpisů by vyžadovalo vyřešení problému diskrétního logu nebo prolomení hašovací funkce.


#### Schnorrovy podpisy a historické souvislosti


Schnorrovy signatury jsou matematicky čistší a podporují agregační funkce, ale byly patentovány v době uvedení Bitcoin na trh. ECDSA nabízela bezplatnou alternativu, ovšem s větší složitostí a většími podpisy. Po vypršení platnosti patentů přidal Bitcoin prostřednictvím Taproot podpisy Schnorr, které poskytovaly pevné 64bajtové podpisy a lepší soukromí. ECDSA zůstává podporován kvůli starší kompatibilitě.



### Struktura transakce a vstupy/výstupy


Transakce Bitcoin se skládá z:


- version (4 bajty, little-endian)
- vstupní seznam
- výstupní seznam
- locktime (4 bajty)


Vstupy odkazují na předchozí UTXO pomocí jejich transakčního hashe a výstupního indexu a zahrnují odemykací skript (scriptSig) a pořadové číslo používané pro časové zámky nebo RBF. Výstupy specifikují částku (8 bajtů) a zamykací skript (scriptPubKey), definující podmínky utrácení. Adresy Bitcoin jsou reprezentací těchto skriptů.


#### Model UTXO

Bitcoin sleduje nevyužité výstupy, nikoli zůstatky účtů. UTXO musí být zcela vyčerpány - částečné čerpání není možné. Aby bylo možné utratit 1 BTC ze 100 BTC UTXO, musí transakce obsahovat výstup změny. Zapomenutím na výstup změny se zbytek promění v poplatek těžaři.


#### Serializace a parsování transakcí


Transakce používají kompaktní binární formát. Za polem verze je v poli varint zakódován počet vstupů. Mezi vstupy patří:


- předchozí tx hash (32 bajtů)
- výstupní index (4 bajty)
- scriptSig (varstr)
- sekvence (4 bajty)


Výstupy zahrnují 8bajtovou částku a scriptPubKey (varstr). Locktime řídí, kdy se transakce stane platnou. Serializace používá pro většinu celých čísel uspořádání little-endian. Parsery spotřebovávají bajty postupně a delegují na specializované třídy pro vstupy, výstupy a skripty.


### Poplatky, změny a poddajnost


Poplatky jsou implicitní:

poplatek = součet(vstupní hodnoty) - součet(výstupní hodnoty).

Jakákoli nepřiřazená hodnota se stává poplatkem, a proto je zásadní správná konstrukce změnového výstupu. Před SegWit podpisy umožňovaly malleabilitu - změnou S na N-S vznikla nová platná transakce s jiným ID. Bitcoin nyní prosazuje pravidlo nízkého počtu S a SegWit izoluje podpisy od výpočtu txid, díky čemuž jsou ID stabilní a umožňují protokoly druhé vrstvy, jako je Lightning.


## Ověřování skriptů a transakcí Bitcoin

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>


![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


Bitcoin Script je malý, na zásobníku založený jazyk chytrých smluv, který definuje, jak lze mince utrácet. Každý výstup nese skriptPubKey (zamykací skript) a každý vstup nese skriptSig (odemykací skript). Společně tvoří program, který se musí vyhodnotit jako "true", aby byla útrata platná. Skript záměrně není Turingově úplný, aby všechny cesty provedení byly předvídatelné a snadno ověřitelné v celé síti.


### Operace skriptu a model provádění


Skript je posloupnost datových prvků a operačních kódů. Datové prvky (podpisy, veřejné klíče, hashe) jsou umístěny na zásobník, zatímco opkódy začínající na `OP_` transformují zásobník. Po provedení musí být horní prvek zásobníku nenulový, aby byl úspěšný. Příklady: `OP_DUP` duplikuje horní prvek, `OP_HASH160` aplikuje SHA256 a poté RIPEMD160 a `OP_CHECKSIG` ověří podpis proti sighash transakce a veřejnému klíči, přičemž 1 je platný, 0 neplatný. Pravidla parsování rozlišují mezi surovými daty (s délkovým prefixem) a opcodes (vyhledanými podle hodnoty bajtu) a malý virtuální stroj je provádí deterministicky na každém uzlu.


### P2PK a P2PKH: Základní platební vzory


Nejstarší vzor, Pay-to-Public-Key (P2PK), zamykal mince přímo na úplný veřejný klíč: scriptPubKey je `<pubkey> OP_CHECKSIG` a scriptSig je pouze podpis. Je to jednoduché, ale prostorově nenáročné a odhaluje to veřejný klíč ještě před utracením mincí.


#### P2PKH a adresy

Služba Pay-to-Public-Key-Hash (P2PKH) tuto funkci vylepšuje tím, že zamyká na 20bajtový hash veřejného klíče. SkriptPubKey je `OP_DUP OP_HASH160 <pubkey_hash> OP_EQUALVERIFY OP_CHECKSIG` a skriptSig poskytuje `<signature> <pubkey>`. Provedení zkontroluje, zda se hash poskytnutého veřejného klíče shoduje s odevzdanou hodnotou, a poté ověří podpis. Tím se veřejný klíč skryje až do doby, než se utratí, zmenší se jeho velikost a odpovídá známému "1..." mainnet formátu adresy.


### Ověřování transakcí a funkce Hashing podpisu


Uzel ověřující transakci musí zajistit:

1) Každý vstup odkazuje na existující, nevyužitý výstup.

2) Celková hodnota vstupu ≥ celková hodnota výstupu (rozdíl je poplatek).

3) Každý skriptSig správně odemkne svůj odkazovaný skriptPubKey.


Ověření podpisu vyžaduje sestrojení přesné zprávy, která byla podepsána, tzv. sighash. U staršího ECDSA ověření vyprázdní všechny skriptSigy, nahradí skriptSig aktuálního vstupu odpovídajícím skriptPubKey, přidá 4bajtový typ hashe (obvykle `SIGHASH_ALL`) a výsledek dvakrát zprasí. Tuto 256bitovou hodnotu používá `OP_CHECKSIG`. Alternativní typy hash (např. `SINGLE`, `NONE`, s nebo bez `ANYONECANPAY`) mění, které části transakce se odevzdávají, což umožňuje výklenkové případy použití, jako je společné financování nebo částečně specifikované transakce, ale v praxi se používají zřídka.


#### Kvadratické hašování a SegWit

Vzhledem k tomu, že každý vstup ve starší transakci vyžaduje vlastní výpočet sighash nad strukturou, která zahrnuje všechny vstupy, může čas validace růst kvadraticky s počtem vstupů. Velké transakce s více vstupy kdysi způsobovaly znatelná zpoždění validace. SegWit přepracoval výpočet sighash tak, aby se sdílené části ukládaly do mezipaměti a složitost se snížila na lineární čas, což zlepšilo škálovatelnost a ztížilo útoky typu "denial-of-service".


### Hádanky skriptů a lekce zabezpečení


Skript může vyjádřit mnohem více než jen "jeden podpis odemkne tyto mince" Skriptové hádanky to demonstrují zakódováním libovolných podmínek - matematických problémů, výzev k předobrazu hashe nebo dokonce kolizních odměn -, kdy každý, kdo poskytne správné údaje, může mince utratit. Výstupy, které se spoléhají pouze na veřejná data (bez podpisů), jsou však zranitelné vůči front-runningu těžařů: jakmile se v mempoolu objeví platné řešení, může ho kterýkoli těžař zkopírovat a přesměrovat výplatu na sebe.


Praktickým poznatkem je, že reálné smlouvy téměř vždy obsahují kontrolu podpisu, i když obsahují složitější logiku, jako je multisig, timelocks nebo hashlocks. Podpisy vážou řešení na konkrétní stranu, zachovávají motivaci a brání ostatním v krádeži výplaty. Pochopení modelu zásobníku Script, standardních vzorů a jemných úskalí je nezbytné pro návrh bezpečných chytrých kontraktů Bitcoin a pro úvahy o tom, jak jsou transakce v síti skutečně ověřovány.


## Konstrukce transakcí a Pay-to-Script Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>


![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


### Budova Bitcoin Transakce a P2SH


Konstrukce transakcí Bitcoin propojuje teoretické znalosti protokolu s praktickou implementací. Transakce vybírá UTXO k utrácení, sestavuje výstupy se zamykacími skripty, vytváří podpisy pro každý vstup a vše serializuje v přesném formátu, který uzly očekávají. Tento proces vyžaduje pochopení generování povzdechů, chování skriptů a správné zpracování poplatků a změn.


### Základní konstrukce transakce


Každý vstup transakce odkazuje na předchozí výstup pomocí txid a indexu. Výstupy udávají částky v satoši a zamykacích skriptech. Rozdíl mezi celkovými vstupy a celkovými výstupy je poplatek. Pro podepsání vstupu se serializuje upravená verze transakce, vypočítá se její sosaš a podepíše se soukromým klíčem. Výsledný podpis a veřejný klíč tvoří ScriptSig. Jakmile je každý vstup podepsán, může být surová transakce vysílána do sítě.


### Transakce s více podpisy


Bare multisig používá `OP_CHECKMULTISIG` pro vyžadování m-of-n podpisů. Kvůli časné chybě off-by-one spotřebovává OP_CHECKMULTISIG další prvek zásobníku a vyžaduje počáteční `OP_0` ve ScriptSig. Bare multisig je funkční, ale neefektivní: všechny veřejné klíče se zobrazují jako on-chain, takže skriptPubKeys jsou velké, drahé a obtížně se kódují jako adresy. Tato omezení motivovala zavedení pay-to-script-hash.


#### Architektura P2SH

P2SH skrývá složité skripty za 20bajtovým HASH160. SkriptPubKey je pevně nastaven: `OP_HASH160 <20bajtový hash> OP_EQUAL`. Základní skript vykoupení - obsahující multisig, časové zámky nebo jiné podmínky - je odhalen a spuštěn pouze při utrácení. Odesílatel vidí pouze hash, zatímco příjemce spravuje redeem skript soukromě. Tato konstrukce snižuje velikost on-chain, zlepšuje soukromí a umožňuje uzavírat složité smlouvy, aniž by zatěžovala odesílatele.


### P2SH Výdaje a provádění


Chcete-li strávit výstup P2SH, musí ScriptSig obsahovat potřebné údaje pro odemknutí *plus* samotný skript pro vykoupení. Ověřování probíhá ve dvou krocích:

1) HASH160(redeem_script) se musí shodovat s hashem scriptPubKey.

2) Po ověření se spustí skript vykoupení se zadanými údaji.


Při generování podpisů pro vstup P2SH používá proces sighash místo klíče scriptPubKey skript redeem. Každý podepisující musí vlastnit úplný skript redeem, aby byly podpisy generate platné. Adresy P2SH používají bajt verze 0x05 u mainnet (adresy "3...") a 0xC4 u testnetu (adresy "2...").


#### Praktické úvahy o zabezpečení


Ztráta skriptu pro vykoupení znamená ztrátu finančních prostředků: k utracení jsou zapotřebí soukromé klíče i samotný skript pro vykoupení. Účastníci Multisig musí před přijetím vkladů ověřit, zda jsou jejich veřejné klíče správně zařazeny. P2SH podporuje pokročilé konstrukce, jako je multisig, timelocks a hashlocks, ale chyby v logice skriptu mohou trvale zablokovat prostředky, takže testování v testnetu je nezbytné.


P2SH zlepšuje soukromí tím, že skrývá podmínky utrácení až do prvního utracení, ale jakmile se objeví skript proplacení on-chain, je trvale viditelný. Navzdory tomu se díky výhodám v podobě zmenšené velikosti, zpětné kompatibility a podpory flexibilních smluv stal P2SH významným milníkem, který ovlivnil pozdější upgrady, jako jsou SegWit a Taproot.


# Vnitřní fungování sítě Bitcoin

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bloky Bitcoin a Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>


![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


Bitcoin blokuje skupinové transakce a zabezpečuje je pomocí proof of work. Každý blok obsahuje 80bajtovou hlavičku a seznam transakcí. Navzdory velkým energetickým nákladům na výrobu platného bloku je jeho ověření levné: uložení všech ~900k hlaviček vyžaduje pouze ~72 MB, což umožňuje i malým zařízením efektivně ověřovat řetězec proof of work.


### Transakce Coinbase a odměny za bloky


Každý blok začíná přesně jednou transakcí na Coinbase - jediným způsobem, jak se nové bitcoiny dostávají do oběhu. Má vynulovaný prev-tx hash a index 0xffffffff, který jej jednoznačně identifikuje. Dotace začínala na 50 BTC a každých 210 000 bloků se snižuje na polovinu (50, 25, 12,5, 6,25, 3,125, ...). Těžaři zahrnují také transakční poplatky. Protože 4bajtová nonce je pro moderní ASIC příliš malá, těžaři upravují data v transakci Coinbase, aby změnili Merkleho kořen a vytvořili další vyhledávací prostor. BIP34 vyžaduje vložení výšky bloku do skriptu CoinbaseSig, aby bylo zajištěno, že každý blok Coinbase txid je jedinečný.


### Pole záhlaví bloku a signalizace Soft Fork


80bajtová hlavička obsahuje:


- version (4 bajty)
- hash předchozího bloku (32 bajtů)
- Merkleho kořen (32 bajtů)
- časové razítko (4 bajty)
- bitů (cíl obtížnosti, 4 bajty)
- nonce (4 bajty)


Čísla verzí se prostřednictvím BIP9 vyvinula v systém signalizace bitových polí, který umožňuje těžařům koordinovat připravenost soft-fork. Časová značka je 32bitová hodnota unixového času a bude ji třeba aktualizovat kolem roku 2106.


#### Bity Pole a cíle

Pole bitů kóduje cíl v kompaktním tvaru: cíl = koeficient × 256^(exponent-3). Platné blokové hashe musí být číselně nižší než tento cíl. Protože jsou hashe interpretovány jako malá celá čísla, platné hashe se při zobrazení v hexadecimálním tvaru často zobrazují s mnoha koncovými nulami.


### Obtížnost, ověřování a úpravy


Obtížnost je definována jako nejnižší_cíl / aktuální_cíl, což vyjadřuje, o kolik je mining dnes těžší ve srovnání s nejlehčí možnou obtížností. Ověření vyžaduje pouze porovnání hashe hlavičky s cílem - extrémně levné vzhledem ke mining.


Každých 2016 bloků Bitcoin upravuje obtížnost tak, aby se zaměřila na ~10minutové intervaly mezi bloky. Úprava porovnává skutečný čas předchozích bloků roku 2016 s očekávaným časem za dva týdny. Limity omezují úpravy na čtyřnásobek. Významné události v reálném světě - jako například zákaz mining v Číně - ukázaly odolnost tohoto mechanismu, když míra hashování prudce klesla a obtížnost se upravila směrem dolů, aby se vyrovnala.


### Bloková dotace a celková částka Supply


Dotace ve výšce h se vypočítá takto: dotace = 5_000_000_000 >> (h // 210_000). Tím získáme plán půlení, který konverguje k celkové nabídce ~21 milionů BTC. Součet geometrické řady (50 + 25 + 12,5 + ...) × 210 000 vysvětluje horní hranici. Těžaři si mohou nárokovat méně než povolenou dotaci, ale nikdy ne více, jinak se blok stane neplatným. S tím, jak se dotace v průběhu po sobě jdoucích půlení snižují, se transakční poplatky stávají stále důležitější složkou příjmů těžařů a dlouhodobé bezpečnosti sítě.


## Síťová komunikace a Merklovy stromy

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>


![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


### Architektura sítě Bitcoin


Síť Bitcoin peer-to-peer funguje jako decentralizovaný drbací systém, kde si uzly předávají transakce a bloky, aniž by si navzájem důvěřovaly. Nové uzly se zavádějí kontaktováním pevně zakódovaných semen DNS udržovaných hlavními vývojáři. Tato DNS semena vracejí IP adresy aktivních peerů, což uzlům umožňuje zjistit síť a poté požádat o další peery prostřednictvím getaddr. Síť není záměrně kritická pro konsensus, takže implementace se mohou lišit, pokud pravidla konsensu zůstanou nezměněna.


### Struktura zprávy a Handshake


Všechny zprávy Bitcoin P2P používají pevnou obálku: 4bajtovou magickou hodnotu (F9BEB4D9 pro mainnet), 12bajtový příkaz ASCII, 4bajtovou little-endian délku užitečného zatížení, 4bajtový kontrolní součet (první 4 bajty hash256) a užitečné zatížení. Mezi běžné příkazy patří version, verack, inv, getdata, tx, block, getheaders, headers, ping a pong.


Handshake začíná, když připojující se uzel odešle zprávu o verzi. Příjemce odpoví verackem a svou verzí. Jakmile si obě strany vymění tyto dvě zprávy, je spojení aktivní a uzly mohou začít předávat inventáře a data.


### Merklovy stromy a Merklovy kořeny


Bitcoin ukládá do záhlaví každého bloku jeden 32bajtový kořen Merkle jako závazek ke všem transakcím v bloku. Transakce jsou hashovány (hash256), párovány, spojovány a opakovaně hashovány, dokud nezůstane jeden hash. Pokud má úroveň lichý počet, poslední hash se duplikuje. Interně jsou hashe big-endian, zatímco serializovaná data bloku používají little-endian, což vyžaduje reverzaci před a po konstrukci stromu.


#### Merkleho důkazy a SPV

Merkleho důkazy umožňují ověřit, zda je transakce obsažena v bloku, aniž by bylo nutné stahovat celý blok. Důkaz se skládá ze sourozeneckých hashů podél cesty ke kořeni. Lehcí klienti SPV ukládají pouze hlavičky bloků a tyto důkazy vyžadují od plných uzlů. Protože Merkleho strom roste logaritmicky, vyžaduje důkaz zařazení do bloku s tisíci transakcemi pouze několik set bajtů.


Taproot tento koncept rozšiřuje o odevzdávání podmínek výdajů do Merklova stromu skriptů (MAST), přičemž odhaluje pouze provedenou větev spolu s Merklovým důkazem. Tím se zvyšuje efektivita i soukromí.


### Síťové operace a synchronizace bloků


Uzly používají getdata k vyžádání transakcí nebo bloků, přičemž zadávají ID typu (1=tx, 2=blok, 3=filtrovaný blok, 4=kompaktní blok) a 32bajtový identifikátor. Pro synchronizaci řetězce uzly posílají getheaders s počátečním hashem bloku a jako odpověď obdrží až 2000 hlaviček. Každá vrácená hlavička má 80 bajtů, za nimiž následuje fiktivní počet transakcí rovný nule.


Úplné ověření přijatých bloků vyžaduje dvě kontroly:

1. Hash bloku musí být nižší než cíl zakódovaný v poli bits.

2. Kořen Merkle vypočítaný ze všech transakcí (se správným zpracováním endianity) se musí shodovat s kořenem záhlaví.


Pouze pokud obě podmínky splní, uzel blok přijme, což odráží zásadu Bitcoin "nedůvěřuj, ověřuj".


## Pokročilá komunikace uzlů a oddělený svědek

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>


![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)


Tato sekce sjednocuje pokročilé sítě P2P s technologií Segregated Witness a ukazuje, jak moderní software Bitcoin komunikuje přímo s uzly a zároveň využívá transakční struktury s ohledem na SegWit. Vývojáři se naučí načítat bloky, vyhledávat relevantní transakce a konstruovat transakce pouze pomocí surové síťové komunikace - bez potřeby průzkumníků bloků.


### Vyhledávání transakcí na základě bloků a ochrana soukromí


Peněženky musí detekovat příchozí platby tak, že skenují bloky a hledají výstupy odpovídající jejich skriptPubKey. Získávání celých bloků chrání soukromí lépe než vyžádání jednotlivých transakcí, které vypouští silné signály o aktivitě uživatele. I při požadavcích na bloky může dojít k úniku informací o řetězcích s malým objemem, proto jsou pro lehké klienty zachovávající soukromí nezbytné kompaktní blokové filtry (BIP158). Filtry mohou produkovat falešně pozitivní výsledky, ale nikdy ne falešně negativní, což klientům umožňuje stahovat pouze potenciálně relevantní bloky bez odhalení konkrétních adres.


### Trustless Interakce se sítí


Pracovní postup `get_block` demonstruje správné použití sítě: odeslání getdata, přijetí bloku a následné nezávislé ověření jeho kořene Merkle a proof of work. Blok je přijat pouze tehdy, pokud se hash přijaté hlavičky shoduje s požadovaným hashem a jeho vypočtený Merkleho kořen se shoduje s hlavičkou. To ztělesňuje princip "nedůvěřuj, ověřuj", který zajišťuje, že ani škodliví kolegové nemohou uzly oklamat a přimět je k přijetí pozměněných dat.


#### Získávání transakcí z bloků

Transakce bloku lze prohledat na odpovídající skriptPubKeys pomocí jednoduché iterace. Produkční peněženky to provádějí průběžně, jak přicházejí nové bloky, a prokazují vlastnictví výstupů výhradně kryptografickou validací, nikoli spoléháním na rozhraní API třetích stran.


### SegWit Cíle a design


Segregovaný svědek (SegWit) opravil chybovost transakcí tím, že z výpočtu txid odstranil podpisové údaje. To umožnilo vytvořit spolehlivé řetězce předem podepsaných transakcí a učinit Lightning Network praktickým. SegWit také zvýšil kapacitu bloků pomocí "váhy bloku": staré uzly stále vidí bloky o velikosti ≤ 1 MB, zatímco modernizované uzly validují až 4 MB včetně dat svědka. Verzované programy pro svědky (zatím v0-v1) vytvářejí strukturovanou cestu pro upgrade budoucích typů skriptů.


#### P2WPKH (Nativní SegWit)


P2WPKH nahrazuje starší strukturu P2PKH 22bajtovým skriptem: OP_0 + push20 + hash160(pubkey). Výdaje přesouvají podpis a pubkey do samostatného pole svědka.


- Uzly před SegWit: viz "anyone-can-spend", považujte jej za platný.
- Uzly po SegWit: rozpoznání OP_0 + 20bajtový hash a ověření pomocí svědeckých dat.


Toto oddělení řeší poddajnost a snižuje poplatky. Svědek používá varint count, za kterým následuje podpis a pubkey.


#### P2SH-P2WPKH (zpětně kompatibilní s SegWit)


Aby mohly staré peněženky odesílat na adresy SegWit, lze skripty P2WPKH zabalit do P2SH.


- scriptPubKey: standard P2SH hash160(redeemScript)
- scriptSig: redeemScript (program P2WPKH)
- svědek: podpis + pubkey


Ověřovací vrstvy:

1. Uzly před BIP16 přijímají redeemScript jako platný.

2. Uzly po BIP16 jej vyhodnotí a na zásobníku ponechají OP_0 + hash.

3. Uzly SegWit provádějí úplné ověření svědků.


#### P2WSH pro složité skripty


P2WSH zobecňuje SegWit pro multisig a pokročilé skripty tím, že místo hash160 používá SHA256(skript). Typický zásobník svědků multisig 2 ze 3:


- prázdný prvek (chyba CHECKMULTISIG)
- sig1
- sig2
- skript svědka (skript multisig)


Uzly SegWit ověří shodu SHA256(witnessScript) s hashem skriptPubKey a poté jej spustí. Použití SHA256 a 32bajtového hashe umožňuje odlišit P2WSH od P2WPKH a posiluje zabezpečení.


#### P2SH-P2WSH (maximální kompatibilita)


Složité skripty SegWit lze také zabalit do obalu P2SH:


- scriptSig: redeemScript (OP_0 + 32bajtový hash)
- svědek: podpisy + witnessScript


Ověřování prochází třemi generacemi pravidel přesně jako u P2SH-P2WPKH. Tento wrapper byl nezbytný pro raná nasazení Lightningu, která vyžadovala multisig bez malleability. I když se dnes dává přednost nativnímu P2WSH, obalená forma zajišťuje kompatibilitu ve starších systémech wallet.


### Dopad SegWit


SegWit:


- stabilní ID transakce
- nižší poplatky prostřednictvím zlevněných svědeckých údajů
- vyšší propustnost bloků prostřednictvím váhy bloku
- kompatibilita pro staré uzly
- čistá cesta k aktualizaci pro Taproot a budoucí rozšíření


Tyto nástroje spolu s bezdůvěryhodnou síťovou interakcí tvoří základ moderního vývoje Bitcoin.



# Závěrečná část


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Recenze a hodnocení


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Závěrečná zkouška


<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>



<isCourseExam>true</isCourseExam>

## Závěr



<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>


<isCourseConclusion>true</isCourseConclusion>