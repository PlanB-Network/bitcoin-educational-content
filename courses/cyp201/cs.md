---
name: Úvod do kryptografických algoritmů Bitcoinu
goal: Porozumět vytváření Bitcoinové peněženky z kryptografické perspektivy
objectives:
  - Odhalit kryptografickou terminologii související s Bitcoinem.
  - Ovládnout vytváření Bitcoinové peněženky.
  - Porozumět struktuře Bitcoinové peněženky.
  - Porozumět adresám a cestám derivace.
---

# Cesta do světa kryptografie

Fascinuje vás Bitcoin? Zajímá vás, jak funguje Bitcoinová peněženka? Připravte se na poutavou cestu do světa kryptografie! Loïc, náš expert, vás provede složitostmi vytváření Bitcoinové peněženky a odhalí tajemství zastrašujících technických termínů jako jsou hašování, derivace klíčů a eliptické křivky.

Tento trénink vás nejen vybaví znalostmi potřebnými k pochopení struktury Bitcoinové peněženky, ale také vás připraví na hlubší ponoření do vzrušujícího světa kryptografie. Jste připraveni vydat se na tuto cestu? Přidejte se k nám a proměňte svou zvědavost ve znalosti!

+++

# Úvod
<partId>32960669-d13a-592f-a053-37f70b997cbf</partId>

## Úvod do kryptografie
<chapterId>fb4e8857-ea35-5a8a-ae8a-5300234e0104</chapterId>

### Je tento trénink pro vás? ANO!

Jsme potěšeni, že vás můžeme přivítat na novém kurzu s názvem "Krypto 301: Úvod do kryptografie a HD peněženek", který vede expert v oboru, Loïc Morel. Tento kurz vás ponoří do fascinujícího světa kryptografie, základní disciplíny matematiky, která zajišťuje šifrování a bezpečnost vašich dat.

V našem každodenním životě, a zejména ve světě Bitcoinu, hraje kryptografie klíčovou roli. Koncepty související s kryptografií, jako jsou soukromé klíče, veřejné klíče, adresy, cesty derivace, seed a entropie, jsou jádrem používání a vytváření Bitcoinové peněženky. Během tohoto kurzu vám Loïc podrobně vysvětlí, jak se generují soukromé klíče a jak jsou propojeny s adresami. Loïc také věnuje hodinu vysvětlování matematických detailů eliptických křivek. Kromě toho pochopíte, proč je použití HMAC SHA512 důležité pro zabezpečení vaší peněženky a jaký je rozdíl mezi seedem a mnemonickou frází.
Hlavním cílem tohoto tréninku je umožnit vám porozumět technickým procesům zapojeným do vytváření HD peněženky a použitým kryptografickým metodám. Během let se Bitcoinové peněženky vyvinuly, aby byly snadněji použitelné, bezpečnější a standardizované díky konkrétním BIPům. Loïc vám pomůže pochopit tyto BIPy, abyste pochopili volby učiněné vývojáři Bitcoinu a kryptografy. Jako všechny tréninky nabízené naší univerzitou, i tento je zcela zdarma a open source. To znamená, že si jej můžete vzít a používat, jak chcete. Těšíme se na vaši zpětnou vazbu na konci tohoto vzrušujícího kurzu.

### Slovo máte vy, profesore!

Všem zdravím, jsem Loïc Morel, váš průvodce technickým průzkumem kryptografie používané v Bitcoinových peněženkách.

Naše cesta začíná ponorem do hlubin kryptografických hašovacích funkcí. Společně rozebereme vnitřní fungování nezbytného SHA256 a prozkoumáme různé algoritmy věnované derivaci.

Pokračovat budeme odhalením tajemného světa digitálních podpisů. Objevíte, jak magie eliptických křivek platí pro tyto podpisy, a osvětlíme, jak vypočítat veřejný klíč z klíče soukromého. A samozřejmě se ponoříme do procesu digitálního podpisu.
Poté se vrátíme zpět v čase, abychom viděli evoluci Bitcoin peněženek a ponoříme se do konceptů entropie a náhodných čísel. Prozkoumáme slavnou mnemonickou frázi, přičemž se také dotkneme hesla (passphrase). Budete mít dokonce jedinečnou příležitost vytvořit si seed z 128 hodů kostkou!
S těmito pevnými základy budeme připraveni na klíčovou část: vytvoření Bitcoin peněženky. Od zrození seedu a hlavního klíče, přes studium rozšířených klíčů, až po odvození dětských párů klíčů, každý krok bude podrobně rozebrán. Také probereme strukturu peněženky a cesty odvození.

A jako třešnička na dortu zakončíme naši cestu zkoumáním Bitcoin adres. Vysvětlíme, jak jsou vytvořeny a jak hrají zásadní roli v fungování Bitcoin peněženek.

Přidejte se ke mně na této fascinující cestě a připravte se prozkoumat svět kryptografie jako nikdy předtím. Nechte své předsudky za dveřmi a otevřete svou mysl novému způsobu pochopení Bitcoinu a jeho základní struktury.

# Hashovací Funkce
<partId>3713fee1-2ec2-512e-9e97-b6da9e4d2f17</partId>

## Úvod do kryptografických hashovacích funkcí souvisejících s Bitcoinem
<chapterId>dba011f5-1805-5a48-ac2b-4bd637c93703</chapterId>

Vítejte na dnešním sezení věnovaném hlubokému ponoření do kryptografického světa hashovacích funkcí, klíčového pilíře bezpečnosti protokolu Bitcoin. Představte si hashovací funkci jako ultra-efektivního kryptografického dešifrovacího robota, který transformuje informace jakékoli velikosti na jedinečnou a pevně danou velikost digitální otisk, nazývaný "hash", "digest" nebo "kontrolní součet".
Stručně řečeno, hashovací funkce přijme vstupní zprávu libovolné velikosti a převede ji na výstupní otisk pevné velikosti.

Popis profilu kryptografických hashovacích funkcí vyžaduje pochopení dvou zásadních vlastností: jejich nevratnosti a odolnosti proti falšování.

Nevratnost, neboli odolnost proti předobrazu, znamená, že výpočet výstupu z daného vstupu lze snadno provést, ale výpočet vstupu z výstupu je nemožný.
Jedná se o jednosměrnou funkci.

![image](assets/image/section1/0.webp)

Odolnost proti falšování vyplývá z faktu, že i nejmenší úprava vstupu vyústí v zásadně odlišný výstup.
Tyto funkce umožňují ověřování integrity staženého softwaru.

![image](assets/image/section1/1.webp)

Další klíčovou charakteristikou, kterou tyto funkce mají, je odolnost proti kolizím a odolnost proti druhému předobrazu. Kolize nastane, když dva rozdílné vstupy produkují stejný výstup.
Samozřejmě, ve světě hashování jsou kolize nevyhnutelné, ale vynikající kryptografická hashovací funkce je minimalizuje významně. Riziko musí být tak nízké, že je možné jej považovat za zanedbatelné. Je to, jako by každý hash byl domem v obrovském městě; navzdory enormnímu počtu domů, dobrá hashovací funkce zajišťuje, že každý dům má jedinečnou adresu.

Odolnost proti druhému předobrazu závisí na odolnosti proti kolizím; pokud existuje odolnost proti kolizím, pak existuje odolnost proti druhému předobrazu.
Pokud máme danou vstupní informaci, musíme najít druhý vstup, odlišný od prvního, který výstupní hash funkce způsobí kolizi. Odolnost proti druhému předobrazu je podobná odolnosti proti kolizím, s tím rozdílem, že vstup je nám dán.
Pojďme se nyní plavit rozbouřenými vodami zastaralých hashovacích funkcí. SHA0, SHA1 a MD5 jsou nyní považovány za rezavé vraky v oceánu kryptografického hašování. Často se od nich odrazuje, protože ztratily odolnost vůči kolizím. Princip šuplíku vysvětluje, proč navzdory našim nejlepším snahám je kvůli omezení velikosti výstupu nemožné vyhnout se kolizím. Aby byla hashovací funkce skutečně považována za bezpečnou, musí odolávat kolizím, druhým preobrazům a preobrazům.

Klíčovým prvkem v protokolu Bitcoinu je hashovací funkce SHA-256, která je kapitánem lodi. Další funkce, jako je SHA-512, se používají pro derivaci s HMAC a PBKDF. Kromě toho se používá RIPMD160 k redukci otisku na 160 bitů. Když mluvíme o HASH256 a HASH160, odkazujeme na použití dvojitého hašování s SHA-256 a RIPMD.

Pro HASH256 to znamená dvojité hašování zprávy pomocí funkce SHA256.
$$
SHA256(SHA256(zpráva))
$$
Pro HASH160 to znamená dvojité hašování zprávy pomocí SHA256 a poté RIPMD160.
$$
RIPMD160(SHA256(zpráva))
$$
Použití HASH160 je zvláště výhodné, protože umožňuje zabezpečení SHA-256 při snížení velikosti otisku.

Shrnutí, konečným cílem kryptografické hashovací funkce je přeměnit informace libovolné velikosti na otisk pevné velikosti. Aby byla uznána za bezpečnou, musí mít několik silných stránek: nevratnost, odolnost vůči manipulaci, odolnost vůči kolizím a odolnost vůči druhým preobrazům.

![obrázek](assets/image/section1/2.webp)

Na konci tohoto průzkumu jsme odhalili tajemství kryptografických hashovacích funkcí, zdůraznili jejich použití v protokolu Bitcoinu a rozebrali jejich konkrétní cíle. Zjistili jsme, že aby byly hashovací funkce považovány za bezpečné, musí odolávat preobrazům, druhým preobrazům, kolizím a manipulaci. Také jsme pokryli škálu různých hashovacích funkcí používaných v protokolu Bitcoinu. V našem dalším sezení se ponoříme do jádra funkce SHA256 a objevíme fascinující matematiku, která jí dává její jedinečné vlastnosti.

## Vnitřní fungování SHA256
<chapterId>905eb320-f15b-5fb6-8d2d-5bb447337deb</chapterId>

Vítejte v pokračování naší fascinující cesty kryptografickými bludišti hashovací funkce. Dnes odhalíme tajemství SHA256, složitého, ale geniálního procesu, který jsme dříve představili.
Jako připomínka, účelem hashovací funkce SHA256 je vzít vstupní zprávu libovolné velikosti a vygenerovat jako výstup 256bitový hash.

### Předzpracování

Pojďme se v tomto bludišti posunout dále začátkem s předzpracováním SHA256.

#### Doplňkové bity

Cílem tohoto prvního kroku je mít zprávu, která je vyrovnána na násobek 512 bitů. K dosažení tohoto cíle přidáme k zprávě doplňkové bity.

Nechť M je velikost počáteční zprávy.
Nechť 1 je bit vyhrazený pro oddělovač.
Nechť P je počet bitů použitých pro doplnění a 64 je počet bitů vyhrazených pro druhou fázi předzpracování.
Celkový počet by měl být násobkem 512 bitů, což je reprezentováno n.

![obrázek](assets/image/section1/3.webp)

Příklad se vstupní zprávou o 950 bitech:

```
Krok 1: Určete velikost; konečný požadovaný počet bitů.
První násobek 512 > (M + 64 + 1) (kde M = 950) je 1024. 1024 = 2 * 512
Takže n = 2.

Krok 2: Určete P, počet bitů potřebných k doplnění, aby bylo dosaženo konečného požadovaného počtu bitů.
-> M + 1 + P + 64 = n * 512
-> M + 1 + P + 64 = 2 * 512
-> 950 + 1 + P + 64 = 1024
-> P = 1024 - 1 - 64 - 950
-> P = 9

Tedy je třeba přidat 9 doplňkových bitů, aby byla zpráva rovna násobku 512.
```

A co teď?
Hned po původní zprávě je třeba přidat oddělovač 1 následovaný P, což je v našem příkladu devět 0.

```
zpráva + 1 000 000 000
```

#### Doplňování velikosti

Nyní přecházíme do druhé fáze předzpracování, která zahrnuje přidání binární reprezentace velikosti původní zprávy v bitech.

Podívejme se znovu na příklad se vstupem 950 bitů:

```
Binární reprezentace čísla 950 je: 11 1011 0110

Použijeme našich 64 rezervovaných bitů z předchozího kroku. Přidáme nuly, abychom zaokrouhlili naše 64 bitů na náš vyrovnávaný vstup. Poté sloučíme původní zprávu, doplňkové bity a doplňování velikosti, abychom získali náš vyrovnávaný vstup.
```

Zde je výsledek:

![obrázek](assets/image/section1/4.webp)

### Zpracování

#### Pochopení předpokladů

##### Konstanty a inicializační vektory

Nyní se připravujeme na počáteční kroky zpracování funkce SHA-256. Stejně jako v každém dobrém receptu, potřebujeme některé základní ingredience, které nazýváme konstanty a inicializační vektory.

Inicializační vektory, od A do H, jsou první 32 bitů desetinných částí odmocnin prvních 8 prvočísel. Budou sloužit jako základní hodnoty v počátečních krocích zpracování. Jejich hodnoty jsou ve formátu hexadecimální.

Konstanty K, od 0 do 63, představují první 32 bitů desetinných částí třetích odmocnin prvních 64 prvočísel. Používají se v každém kole kompresní funkce. Jejich hodnoty jsou také v hexadecimálním formátu.

![obrázek](assets/image/section1/5.webp)

##### Použité operace

V rámci kompresní funkce používáme specifické operátory jako XOR, AND a NOT. Bity zpracováváme jednotlivě podle jejich pozice, používáme operátor XOR a pravdivostní tabulku. Operátor AND se používá k vrácení 1, pouze pokud oba operandy jsou rovny 1, a operátor NOT se používá k vrácení opačné hodnoty operandu. Také používáme operaci SHR pro posun bitů doprava o zvolený počet.

Pravdivostní tabulka:

![obrázek](assets/image/section1/6.webp)

Operace posunu bitů:

![obrázek](assets/image/section1/7.webp)

#### Kompresní funkce

Před aplikací kompresní funkce rozdělíme vstup na bloky po 512 bitech. Každý blok bude zpracován nezávisle na ostatních.

Každý 512bitový blok je poté dále rozdělen na 32bitové části nazývané W. Takto W(0) představuje prvních 32 bitů 512bitového bloku. W(1) představuje dalších 32 bitů a tak dále, až dosáhneme 512 bitů bloku.
Jakmile jsou definovány všechny konstanty K a části W, můžeme provést následující výpočty pro každou část W v každém kole.
Provádíme 64 kol výpočtů ve funkci komprese. V posledním kole, na úrovni "Výstup funkce", budeme mít mezistav, který bude přidán k počátečnímu stavu kompresní funkce.

Poté opakujeme všechny tyto kroky kompresní funkce na dalším 512-bitovém bloku, až do posledního bloku.

Všechny sčítání v kompresní funkci jsou modulo 2^32 sčítání, aby byl vždy zachován 32-bitový součet.

![obrázek](assets/image/section1/9.webp)

![obrázek](assets/image/section1/8.webp)

##### Jedno kolo kompresní funkce

![obrázek](assets/image/section1/11.webp)

![obrázek](assets/image/section1/10.webp)

Kompresní funkce bude provedena 64krát. Máme naše části W a naše předem definované konstanty K jako vstup.
Červené čtverce/kríže odpovídají sčítání modulo 2^32-bit.

Vstupy A, B, C, D, E, F, G, H budou spojeny s 32-bitovou hodnotou, což dá dohromady 32 * 8 = 256 bitů.
Máme také novou sekvenci A, B, C, D, E, F, G, H jako výstup. Tento výstup bude poté použit jako vstup pro další kolo a tak dále až do konce 64. kola.

Hodnoty vstupní sekvence pro první kolo kompresní funkce odpovídají předem definovaným inicializačním vektorům zmíněným dříve.
Jako připomenutí, inicializační vektory představují prvních 32 bitů desetinných částí odmocnin prvních 8 prvočísel.

Zde je příklad kola:

![obrázek](assets/image/section1/12.1.webp)

##### Mezistav

Jako připomenutí, zpráva je rozdělena na bloky o velikosti 512 bitů, které jsou poté rozděleny na 32-bitové části. Pro každý 512-bitový blok aplikujeme 64 kol kompresní funkce.
Mezistav odpovídá konci 64 kol bloku. Hodnoty výstupní sekvence z tohoto 64. kola jsou použity jako počáteční hodnoty pro vstupní sekvenci prvního kola dalšího bloku.

![obrázek](assets/image/section1/12.2.webp)

#### Přehled hašovací funkce

![obrázek](assets/image/section1/13.webp)

Můžeme si všimnout, že výstup prvního 512-bitového kusu zprávy odpovídá našim inicializačním vektorům jako vstup pro druhý 512-bitový kus zprávy a tak dále.

Výstup posledního kola, posledního kusu, odpovídá konečnému výsledku funkce SHA256.

Závěrem bychom chtěli zdůraznit klíčovou roli výpočtů prováděných v boxech CH, MAJ, σ0 a σ1. Tyto operace, mezi jinými, jsou strážci, kteří zajišťují robustnost hašovací funkce SHA256 proti útokům, což ji činí preferovanou volbou pro zabezpečení mnoha digitálních systémů, zejména v rámci protokolu Bitcoin. Je zřejmé, že ačkoliv složitá, krása SHA256 spočívá ve schopnosti najít vstup z hash, zatímco ověření hash pro daný vstup je mechanicky jednoduchá akce.

## Algoritmy použité pro derivaci
<chapterId>cc668121-7789-5e99-bf5e-1ba085f4f5f2</chapterId>
Algoritmy HMAC a PBKDF2 jsou klíčovými komponentami bezpečnostního mechanismu protokolu Bitcoin. Zabraňují řadě potenciálních útoků a zajišťují integritu Bitcoinových peněženek. HMAC a PBKDF2 jsou kryptografické nástroje používané pro různé úkoly v Bitcoinu. HMAC je primárně používán k odražení útoků typu prodloužení délky při odvozování Hierarchických Deterministických (HD) peněženek, zatímco PBKDF2 slouží k převodu mnemonické fráze na seed.

#### HMAC-SHA512

Dvojice HMAC-SHA512 má dva vstupy: zprávu m (Vstup 1) a klíč K, který si uživatel libovolně zvolí (Vstup 2). Má také pevně stanovenou velikost výstupu: 512 bitů.

Poznamenejme:
- m: zpráva libovolné velikosti zvolená uživatelem (vstup 1)
- K: libovolný klíč zvolený uživatelem (vstup 2)
- K': vyrovnání klíče K. Byl upraven na velikost B bloků.
- ||: operace konkatenace.
- opad: konstanta definovaná bajtem 0x5c opakovaným B krát.
- ipad: konstanta definovaná bajtem 0x36 opakovaným B krát.
- B: Velikost bloků použité hašovací funkce.

![image](assets/image/section1/14.webp)

HMAC-SHA512, který bere jako vstupy zprávu a klíč, generuje výstup pevné velikosti. Pro zajištění uniformity je klíč upraven na základě velikosti bloků použitých v hašovací funkci. V kontextu odvozování HD peněženek se používá HMAC-SHA-512. Operuje s 1024-bitovými (128-bajtovými) bloky a odpovídajícím způsobem upravuje klíč. Používá konstanty OPAD (0x5c) a IPAD (0x36), opakované podle potřeby pro zvýšení bezpečnosti.

Proces HMAC-SHA-512 zahrnuje konkatenaci výsledku SHA-512 aplikovaného na klíč XOR OPAD a klíč XOR IPAD se zprávou. Při použití s 1024-bitovými (128-bajtovými) bloky je vstupní klíč v případě potřeby doplněn nulami, poté XORován s IPAD a OPAD. Modifikovaný klíč je poté konkatenován se zprávou.

![image](assets/image/section1/15.webp)

Zahrnutí soli do řetězce kódu zvyšuje bezpečnost odvozených klíčů. Bez ní by útok mohl ohrozit celou peněženku a ukrást všechny bitcoiny.

PBKDF2 slouží k převodu mnemonické fráze na seed. Tento algoritmus provádí 2048 kol pomocí HMAC SHA512. Prostřednictvím těchto odvozovacích algoritmů mohou různé vstupy produkovat jedinečný a pevný výstup, což zmírňuje problém možných útoků typu prodloužení délky na funkce rodiny SHA-2.
Útok typu prodloužení délky využívá specifickou vlastnost určitých kryptografických hašovacích funkcí. Při takovém útoku může útočník, který již vlastní haš neznámé zprávy, použít jej k výpočtu haše delší zprávy, která je rozšířením původní zprávy. To je často možné bez znalosti obsahu původní zprávy, což může vést k významným bezpečnostním zranitelnostem, pokud se tento typ hašovací funkce používá pro úkoly jako je ověřování integrity.

![image](assets/image/section1/16.webp)

Závěrem, algoritmy HMAC a PBKDF2 hrají zásadní role v bezpečnosti odvozování HD peněženek v protokolu Bitcoin. HMAC-SHA-512 slouží k ochraně proti útokům typu prodloužení délky, zatímco PBKDF2 umožňuje převod mnemonické fráze na seed. Řetězec kódu přidává další zdroj entropie při odvozování klíče, čímž zajišťuje robustnost systému.

# Digitální Podpisy
<partId>76b58a00-0c18-54b9-870d-6b7e34029db8</partId>
## Digitální podpisy a eliptické křivky
<chapterId>c9dd9672-6da1-57f8-9871-8b28994d4c1a</chapterId>

Kde jsou uloženy ty slavné bitcoiny? Ne v Bitcoin peněžence, jak by si člověk mohl myslet. Ve skutečnosti Bitcoin peněženka uchovává soukromé klíče nezbytné pro prokázání vlastnictví bitcoinů. Samotné bitcoiny jsou zaznamenány na blockchainu, decentralizované databázi, která archivuje všechny transakce.

V systému Bitcoin je jednotkou účtu bitcoin (všimněte si malého "b"). Je dělitelný až na osm desetinných míst, přičemž nejmenší jednotkou je satoshi. UTXO, neboli "Unspent Transaction Outputs", představují nevyužité transakční výstupy patřící veřejnému klíči, který je matematicky spojen se soukromým klíčem. Pro utrácení těchto bitcoinů musí být člověk schopen splnit podmínku utrácení transakce. Typická podmínka utrácení zahrnuje prokázání zbytku sítě, že uživatel je legitimním vlastníkem veřejného klíče spojeného s UTXO. K tomu musí uživatel prokázat držení soukromého klíče odpovídajícího veřejnému klíči spojenému s každým UTXO, aniž by odhalil soukromý klíč.

Zde vstupuje do hry digitální podpis. Slouží jako matematický důkaz držení soukromého klíče spojeného s určitým veřejným klíčem. Tato technika ochrany dat je primárně založena na fascinujícím oboru kryptografie nazývaném kryptografie eliptických křivek (ECC).

Podpis lze matematicky ověřit ostatními účastníky Bitcoin sítě.

![image](assets/image/section2/0.webp)

Pro zajištění bezpečnosti transakcí se Bitcoin spoléhá na dva protokoly digitálních podpisů: ECDSA (Elliptic Curve Digital Signature Algorithm) a Schnorr. ECDSA byl protokolem podpisu integrovaným do Bitcoinu od jeho spuštění v roce 2009, zatímco podpisy Schnorr byly přidány nedávno v listopadu 2021. Ačkoli oba protokoly jsou založeny na kryptografii eliptických křivek a používají podobné matematické mechanismy, hlavně se liší ve struktuře podpisu.

V tomto kurzu představíme algoritmus ECDSA.

### Co je eliptická křivka?

Kryptografie eliptických křivek je soubor algoritmů, které pro své různé geometrické a matematické vlastnosti v kryptografickém kontextu využívají eliptickou křivku, přičemž bezpečnost je založena na obtížnosti výpočtu diskrétního logaritmu.

Eliptické křivky jsou užitečné v různých kryptografických aplikacích v protokolu Bitcoin, od výměn klíčů po asymetrické šifrování a digitální podpisy.

Eliptické křivky mají zajímavé vlastnosti:

- Symetrie: Každá nevertikální čára protínající dva body na eliptické křivce se dotkne křivky ve třetím bodě.
- Každá nevertikální čára tečná k křivce v bodě vždy protne křivku v jedinečném druhém bodě.

Protokol Bitcoin používá pro své kryptografické operace specifickou eliptickou křivku nazvanou Secp256k1.

Předtím, než se ponoříme hlouběji do těchto mechanismů podpisu, je důležité pochopit, co eliptická křivka je. Eliptická křivka je definována rovnicí y² = x³ + ax + b. Každý bod na této křivce má charakteristickou symetrii, která je klíčem k její užitečnosti v kryptografii.

![image](assets/image/section2/1.webp)

Nakonec jsou různé eliptické křivky uznávány jako bezpečné pro kryptografické použití. Nejznámější může být křivka secp256r1. Avšak pro Bitcoin, Satoshi Nakamoto zvolil jinou křivku: secp256k1.
Tato křivka je definována parametry a=0 a b=7, a její rovnice je y² = x³ + 7 modulo n, kde n představuje prvočíslo, které určuje řád křivky.
![image](assets/image/section2/2.webp)

První obrázek představuje křivku secp256k1 nad reálným polem a její rovnici.
Druhý obrázek je reprezentací křivky secp256k1 nad polem ZP, polem kladných přirozených čísel, modulo p, kde p je prvočíslo. Vypadá to jako mrak bodů. Toto pole kladných přirozených čísel používáme, abychom se vyhnuli aproximacím.
p je prvočíslo a je to řád křivky, který se používá.
Nakonec, rovnice použitá v protokolu Bitcoinu je:$$
y^2 = (x^3 + 7) mod(p) $$
Rovnice eliptické křivky v Bitcoinu odpovídá poslední rovnici na předchozím obrázku.

V další části tohoto kurzu budeme používat křivky, které jsou na reálném poli, jednoduše proto, aby se usnadnilo porozumění.

## Výpočet veřejného klíče z privátního klíče
<chapterId>fcb2bd58-5dda-5ecf-bb8f-ad1a0561ab4a</chapterId>

Začněme ponořením do světa algoritmu digitálního podpisu eliptické křivky (ECDSA). Bitcoin využívá tento digitální podpisový algoritmus k propojení privátních a veřejných klíčů. V tomto systému je privátní klíč náhodné nebo pseudonáhodné 256bitové číslo. Teoretický počet možností pro privátní klíč je 2^256, ale ve skutečnosti je to o něco méně. Přesně řečeno, některé 256bitové privátní klíče nejsou pro Bitcoin platné.

Aby byl privátní klíč kompatibilní s Bitcoinem, musí být mezi 1 a n-1, kde n představuje řád eliptické křivky. To znamená, že celkový počet možností pro privátní klíč Bitcoinu je téměř roven 1.158 x 10^77. Pro srovnání, je to přibližně stejný počet atomů přítomných ve viditelném vesmíru.

![image](assets/image/section2/3.webp)

Unikátní privátní klíč, označený jako k, je poté použit k určení veřejného klíče.

Veřejný klíč, označený jako K, je bod na eliptické křivce, který je odvozen z privátního klíče pomocí nevratných algoritmů jako je ECDSA. Když máme znalost privátního klíče, je velmi snadné získat veřejný klíč, ale když máme pouze veřejný klíč, je nemožné získat privátní klíč. Tato nevratnost je základním kamenem bezpečnosti Bitcoin peněženky.

Veřejný klíč má délku 512 bitů, protože odpovídá bodu na křivce s x-ovou souřadnicí 256 bitů a y-ovou souřadnicí 256 bitů. Nicméně, může být komprimován na 264bitové číslo.

![image](assets/image/section2/4.webp)

Generátorový bod (G) je bod na křivce, z kterého jsou veškeré veřejné klíče v protokolu Bitcoinu generovány. Má specifické x a y souřadnice, obvykle reprezentované v hexadecimálním formátu. Pro secp256k1 jsou souřadnice G v hexadecimálu:

- `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
- `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8` Tento bod je užitečný pro odvození všech veřejných klíčů. Pro výpočet veřejného klíče K jednoduše vynásobte bod G soukromým klíčem k, takže: K = k.G

Nyní se budeme zabývat tím, jak přidávat a násobit body na eliptických křivkách.

#### Sčítání a zdvojení bodů na eliptických křivkách

##### Přidání dvou bodů M + L

Jednou z pozoruhodných vlastností eliptických křivek je, že nevertikální přímka protínající křivku ve dvou bodech ji také protne ve třetím bodě, který nazýváme bod O v našem příkladu. Tato vlastnost se používá k určení bodu U, který je opakem bodu O.

M + L = U

![obrázek](assets/image/section2/5.webp)

##### Přidání bodu k sobě = Zdvojení bodu

Přidání bodu G k sobě se provádí nakreslením tečny k křivce v tomto bodě. Tato tečna, podle vlastností eliptických křivek, protne křivku ve druhém jedinečném bodě -J. Opak tohoto bodu, J, je výsledkem přidání bodu G k sobě.
G + G = J

Ve skutečnosti je bod G výchozím bodem pro výpočet všech veřejných klíčů uživatelů systému Bitcoin.

![obrázek](assets/image/section2/6.webp)

#### Skalární násobení na eliptických křivkách

Skalární násobení bodu n je ekvivalentní k přidání tohoto bodu k sobě n-krát.

Podobně jako zdvojení bodu, skalární násobení bodu G bodem n se provádí nakreslením tečny k křivce v bodě G. Tato tečna, podle vlastností eliptických křivek, protne křivku ve druhém jedinečném bodě -2G. Opak tohoto bodu, 2G, je výsledkem přidání bodu G k sobě.

Pokud n = 4, pak se operace opakuje, dokud nedosáhneme 4G.

![obrázek](assets/image/section2/7.webp)

Zde je příklad výpočtu pro 3G:

![obrázek](assets/image/section2/8.webp)

Tyto operace s body na eliptické křivce jsou základem pro výpočet veřejných klíčů. Odvození veřejného klíče znalostí soukromého klíče je velmi jednoduché.
Veřejný klíč je bod na eliptické křivce, je výsledkem našeho sčítání a zdvojení bodu G k-krát. Přičemž k = soukromý klíč.

V tomto příkladu:

- Soukromý klíč k = 4
- Veřejný klíč K = kG = 4G

![obrázek](assets/image/section2/9.webp)

Znát soukromý klíč k, je snadné vypočítat veřejný klíč K. Nicméně, je nemožné získat zpět soukromý klíč na základě veřejného klíče. Je to výsledek sčítání nebo zdvojení bodů?

V naší další lekci se budeme zabývat tím, jak je vytvořen digitální podpis pomocí algoritmu ECDSA s soukromým klíčem pro utrácení bitcoinů.

## Podpis soukromým klíčem
<chapterId>bb07826f-826e-5905-b307-3d82001fb778</chapterId>

Proces digitálního podpisu je klíčovou metodou prokázání, že jste držitelem soukromého klíče, aniž byste jej odhalili. Toho je dosaženo použitím algoritmu ECDSA, který zahrnuje určení jedinečného nonce, výpočet konkrétního čísla V a vytvoření digitálního podpisu složeného ze dvou částí, S1 a S2.
Je zásadní vždy používat jedinečný nonce, aby se předešlo bezpečnostním útokům. Notoricky známým příkladem toho, co se může stát, když se toto pravidlo nedodrží, je hacknutí PlayStation 3, které bylo ohroženo kvůli opětovnému použití nonce.
![](assets/image/section2/10.webp)

Kroky:

- Určete nonce v, což je jedinečné náhodné číslo.
  Nonce = Číslo Použité Pouze Jednou.
  Je určeno osobou provádějící podpis.
- Vypočítejte přidáním a zdvojením bodů na eliptické křivce od bodu G, pozice V na eliptické křivce.
  Tak, že V = v.G
  x a y jsou souřadnice V v rovině.
- Vypočítejte S1.
  S1 = x mod n s n = řád křivky a x souřadnice V v rovině.
  Poznámka: Počet možných veřejných klíčů je větší než počet bodů na eliptické křivce v konečném poli kladných celých čísel používaných v Bitcoinu.
  Řád křivky odpovídá pouze možnostem, které veřejný klíč může na křivce nabývat.
- Vypočítejte S2.
  H(Tx) = Hash transakce
  k = soukromý klíč
- Vypočítejte podpis: spojení S1 + S2.
- Vypočítejte P, výpočet ověření podpisu.
  K = veřejný klíč

Například, abyste získali veřejný klíč 3G, nakreslíte tečnu k bodu G, vypočítáte opak -G, abyste získali 2G, a poté přidáte G a 2G. Pro provedení transakce musíte dokázat, že znáte číslo 3 tím, že odemknete bitcoiny spojené s veřejným klíčem 3G.

Pro vytvoření digitálního podpisu a dokázání, že znáte soukromý klíč spojený s veřejným klíčem 3G, nejprve vypočítáte nonce, poté bod V spojený s tímto nonce (v daném příkladu je to 4G). Poté vypočítáte bod T přidáním veřejného klíče 3G a bodu V, což dá 7G.

![image](assets/image/section2/11.webp)

Pojďme zjednodušit proces digitálního podpisu.
Na předchozím obrázku je soukromý klíč k = 3.
Snadno vypočítáme veřejný klíč K spojený s tímto soukromým klíčem: K = 3G.
Poté generujeme nonce pseudonáhodně: v = 4.
Z tohoto nonce je možné vypočítat V tak, že: V = v.G = 4G.

Z tohoto bodu V vypočítáme bod T tak, že:
T = t.G = 7G (s t = 7).

Nyní je čas pokračovat v ověřování digitálního podpisu.

Ověření digitálního podpisu je zásadní krok při používání algoritmu ECDSA, který umožňuje potvrdit pravost podepsané zprávy bez potřeby soukromého klíče odesílatele. Zde je podrobný popis, jak to funguje:

V našem příkladu máme dvě důležité hodnoty: t a V.
t je číselná hodnota (v tomto příkladu 7) a V je bod na eliptické křivce (zde reprezentovaný jako 4G). Tyto hodnoty jsou generovány během vytváření digitálního podpisu a poté jsou spolu se zprávou odeslány, aby umožnily ověření.

Když ověřovatel obdrží zprávu, obdrží také tyto dvě hodnoty, t a V.

Zde jsou kroky, které ověřovatel provede k ověření podpisu:

1. Nejprve vypočítají hash zprávy, který budeme nazývat H.
2. Poté vypočítají u1 a u2. K tomu použijí následující vzorce:
- u1 = H /* (S2)^-1 mod n - u2 = T /* (S2)^-1 mod n
     Kde S2 je druhá část digitálního podpisu, n je řád eliptické křivky a (S2)^-1 je inverze S2 mod n.
3. Ověřovatel poté vypočítá bod P' na eliptické křivce pomocí vzorce: P' = u1 _ G + u2 _ K
   - G je generující bod křivky
   - K je veřejný klíč odesílatele
4. Ověřovatel poté vypočítá I', což je jednoduše x-ová souřadnice bodu P' modulo n.
5. Nakonec ověřovatel potvrdí, že I' se rovná t. Pokud tomu tak je, podpis je považován za platný. Pokud ne, podpis je neplatný.
Tento postup zajišťuje, že podpis mohl vytvořit pouze odesílatel, který vlastní odpovídající soukromý klíč.

![obrázek](assets/image/section2/12.webp)

Stručně řečeno:
Osoba vytvářející podpis poskytne číslo t (v našem příkladu t = 7) a bod V osobě, která jej ověřuje.

Z čísla 7 a bodu V není možné určit veřejný ani soukromý klíč.

Kroky pro ověření digitálního podpisu jsou následující:

- Na křivce ověřovatel přidá bod veřejného klíče k bodu V, aby získal bod T'.
- Ověřovatel vypočítá číslo t.G.
- Ověřovatel zkontroluje, že výsledek t.G skutečně odpovídá číslu T'.

Závěrem, ověřování digitálního podpisu je zásadní procedura při transakcích s Bitcoinem. Zajišťuje, že podepsaná zpráva nebyla během přenosu změněna a že odesílatel je skutečně držitelem soukromého klíče. Tato technika digitálního ověření je založena na složitých matematických principech, včetně aritmetiky eliptických křivek, přičemž zachovává důvěrnost soukromého klíče. Poskytuje pevný základ bezpečnosti pro kryptografické transakce.

To však neznamená, že správa těchto klíčů, stejně jako jejich vytváření, není další zásadní otázkou v Bitcoinu. Jak generovat nový pár klíčů? Jak bezpečně a efektivně organizovat množství klíčů? Jak je obnovit v případě potřeby?

Na tyto otázky a pro prohloubení vašeho porozumění bezpečnosti kryptografie se náš další kurz zaměří na koncept Hierarchických Deterministických Peněženek (HD peněženky) a použití mnemotechnických frází. Tyto mechanismy nabízejí elegantní způsoby, jak efektivně spravovat vaše kryptoměnové klíče při zvýšení bezpečnosti.

# Mnemotechnická fráze
<partId>4070af16-c8a2-58b5-9871-a22c86c07458</partId>

## Vývoj peněženek Bitcoin
<chapterId>9d9acd5d-a0e5-5dfd-b544-f043fae8840f</chapterId>

Hierarchická Deterministická Peněženka, známější jako HD peněženka, hraje významnou roli v ekosystému kryptoměn. Termín "peněženka" může být pro ty, kteří jsou v tomto oboru noví, zavádějící, protože nejde o držení peněz nebo měn. Místo toho se jedná o sbírku kryptografických soukromých klíčů.

První peněženky byly software, který seskupoval soukromě určené klíče náhodným způsobem, ale neexistovalo mezi nimi žádné spojení. Tyto peněženky se nazývají "Just a Bunch Of Keys" (JBOK).

Vzhledem k tomu, že klíče mezi sebou nemají žádné spojení, musí uživatel pro každý nově vygenerovaný pár klíčů vytvořit novou zálohu.
Ať už uživatel vždy používá stejný pár klíčů a ohrožuje důvěrnost, nebo generuje nový pár klíčů náhodně a proto potřebuje vytvořit novou zálohu těchto klíčů.
Nicméně složitost správy těchto klíčů je vyvážena sadou protokolů nazvaných Bitcoin Improvement Proposals (BIPs). Tyto návrhy na vylepšení jsou jádrem funkčnosti a bezpečnosti HD peněženek. Například [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), spuštěný v roce 2012, zásadně změnil způsob generování a ukládání těchto klíčů tím, že představil koncept deterministicky a hierarchicky odvozených klíčů. Idea spočívá v odvození všech klíčů deterministicky a hierarchicky z jedinečného kusu informace: seedu. Toto výrazně zjednodušuje proces zálohování těchto klíčů při zachování jejich úrovně bezpečnosti.
Následně [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) představil významnou inovaci: 24-slovní mnemonickou frázi. Tento systém přeměnil složitou a těžko zapamatovatelnou sekvenci čísel na sérii obyčejných slov, což ji učinilo mnohem snazší k zapamatování a uložení. Kromě toho [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) navrhl přidání další heslové fráze k zvýšení bezpečnosti jednotlivých klíčů. Tyto postupné vylepšení vedly k standardům BIP43 a BIP44, které standardizovaly strukturu a hierarchizaci HD peněženek, čímž je učinily přístupnějšími a uživatelsky přívětivějšími pro širokou veřejnost.

V následujících sekcích se podrobněji zaměříme na fungování HD peněženek. Budeme diskutovat o principech odvození klíčů a prozkoumáme základní koncepty entropie a generování náhodných čísel, které jsou nezbytné pro zajištění bezpečnosti vaší HD peněženky.

Shrnutí, je nezbytné zdůraznit klíčovou roli BIP32 a BIP39 v návrhu a bezpečnosti HD peněženek. Tyto protokoly umožňují generování více klíčů z jednoho seedu, který má být náhodné nebo pseudonáhodné číslo. Dnes jsou tyto standardy přijaty většinou kryptoměnových peněženek, ať už jsou určeny pro jednu kryptoměnu nebo podporují více typů měn.

## Entropie a generování náhodných čísel
<chapterId>b43c715d-affb-56d8-a697-ad5bc2fffd63</chapterId>

Význam bezpečnosti soukromých klíčů v ekosystému Bitcoinu je nesporný. Jsou skutečně základním kamenem, který zajišťuje bezpečnost transakcí Bitcoinu. Aby se předešlo jakékoli zranitelnosti spojené s předvídatelností, musí být tyto klíče generovány skutečně náhodným způsobem, což se může rychle stát náročným úkolem. Problém je, že v informatice je nemožné generovat skutečně náhodné číslo, protože je nutně odvozeno z deterministického procesu; kódu. Proto je nezbytné se dozvědět více o různých generátorech náhodných čísel (RNG). Typy RNG se liší, od Pseudo-Náhodných Generátorů Čísel (PRNG) po Skutečné Generátory Náhodných Čísel (TRNG), stejně jako PRNG, které zahrnují zdroj entropie.

Entropie se vztahuje na "stav neuspořádanosti" systému. Z externí entropie, tj. externího zdroje informací, je možné pomocí generátoru náhodných čísel získat náhodné číslo.

![image](assets/image/section3/2.webp)

Podívejme se, jak funguje Pseudo-Náhodný Generátor Čísel (PRNG).

Jako vstup bere seed, který odpovídá vnitřnímu stavu 0.
Na tomto vnitřním stavu je aplikována transformační funkce a výsledek, který je pseudonáhodným číslem, odpovídá vnitřnímu stavu 1.
Na tomto vnitřním stavu 1 je znovu aplikována transformační funkce, což vede k novému náhodnému číslu = vnitřní stav 2.
A tak dále.
Hlavní nevýhodou je, že jakýkoliv identický seed vždy vyprodukuje stejný výstup. Také, pokud známe výsledek počátečních transformačních funkcí, budeme schopni získat náhodné číslo na výstupu procesu.
Příkladem transformační funkce je funkce PBKDF2.

**Shrnutí, kryptograficky bezpečný PRNG musí:**

- být statisticky náhodný
- být nepředvídatelný
- být odolný i v případě, že jsou výsledky odhaleny
- mít dostatečně dlouhé období

![obrázek](assets/image/section3/3.webp)

V případě Bitcoinu jsou soukromé klíče generovány z jednoho kusu informace na základě peněženky. Tato informace umožňuje deterministickou a hierarchickou derivaci dceřiných klíčových párů. Entropie je základem každé HD peněženky, ačkoliv neexistuje standard pro generování tohoto náhodného čísla. Proto je generování náhodných čísel hlavní výzvou v zabezpečení Bitcoinových transakcí.

## Mnemonická fráze
<chapterId>8f9340c1-e6dc-5557-a2f2-26c9669987d5</chapterId>

Zabezpečení Bitcoinové peněženky je hlavním znepokojením pro všechny její uživatele. Jedním zásadním způsobem, jak zajistit zálohu peněženky, je generování mnemonické fráze na základě entropie a kontrolního součtu.

![obrázek](assets/image/section3/5.webp)

Pro převod entropie na mnemonickou frázi stačí vypočítat kontrolní součet entropie a spojit entropii a kontrolní součet.

Jakmile je entropie vygenerována, použije se na ni funkce SHA256, aby se vytvořil hash.
Získá se prvních 8 bitů hashe, což je kontrolní součet.
Mnemonická fráze je výsledkem přidání entropie k kontrolnímu součtu.

Kontrolní součet zajišťuje ověření přesnosti obnovovací fráze. Bez tohoto kontrolního součtu by chyba ve frázi mohla vést k vytvoření jiné peněženky a tím k ztrátě prostředků. Kontrolní součet se získá procházením entropie funkcí SHA256 a získáním prvních 8 bitů hashe.

![obrázek](assets/image/section3/6.webp)

Existují různé standardy pro mnemonickou frázi v závislosti na velikosti entropie. Nejčastěji používaný standard pro 24-slovnou obnovovací frázi je entropie 256 bitů. Velikost kontrolního součtu je určena dělením velikosti entropie 32.

Například entropie 256 bitů generuje 8-bitový kontrolní součet. Spojení entropie a kontrolního součtu pak vede k odpovídajícím velikostem 128 bitů, 160 bitů atd. V závislosti na velikosti entropie bude obnovovací fráze obsahovat 12 slov pro 128 bitů, 15 slov pro 160 bitů a 24 slov pro 256 bitů.

**Kódování mnemonické fráze:**

![obrázek](assets/image/section3/7.webp)

Posledních 8 bitů odpovídá kontrolnímu součtu.
Každý 11-bitový segment je převeden na desítkové číslo.
Každé desítkové číslo odpovídá slovu ze seznamu 2048 slov podle BIP39. Je důležité poznamenat, že žádné slovo nemá stejné pořadí prvních čtyř písmen.

Je zásadní zálohovat 24-slovnou obnovovací frázi, aby se zachovala integrita Bitcoinové peněženky. Dva nejčastěji používané standardy jsou založeny na entropii 128 nebo 256 bitů a spojení 12 nebo 24 slov. Přidání hesla je další možností, jak zvýšit zabezpečení peněženky.

Závěrem, generování mnemonické fráze pro zabezpečení Bitcoinové peněženky je klíčový proces. Je důležité dodržovat standardy mnemonické fráze na základě velikosti entropie. Zálohování 24-slovné obnovovací fráze je nezbytné, aby se předešlo jakékoliv ztrátě prostředků.

## Heslo
<chapterId>6a51b397-f3b5-5084-b151-cef94bc9b93f</chapterId>
Heslová fráze je dodatečné heslo, které lze integrovat do Bitcoinové peněženky za účelem zvýšení její bezpečnosti. Její použití je volitelné a je na uvážení uživatele. Přidáním libovolných informací, které společně s mnemonickou frází umožňují výpočet seedu peněženky, heslová fráze zvyšuje její bezpečnost.

![image](assets/image/section3/8.webp)

Heslová fráze je volitelná kryptografická sůl o velikosti zvolené uživatelem. Zlepšuje bezpečnost HD peněženky přidáním libovolných informací, které, když jsou kombinovány s mnemonickou frází, umožní výpočet seedu.

Jakmile je heslová fráze nastavena při vytváření peněženky, je nutná pro odvození všech klíčů peněženky. Funkce pbkdf2 se používá k vygenerování seedu z heslové fráze. Tento seed umožňuje odvození všech dětských párů klíčů peněženky. Pokud je heslová fráze změněna, Bitcoinová peněženka se stane zcela odlišnou.

Heslová fráze je zásadním nástrojem pro zvýšení bezpečnosti Bitcoinových peněženek. Umožňuje implementaci různých bezpečnostních strategií. Například lze použít k vytvoření duplikátů a usnadnění zálohování mnemonické fráze. Také může zlepšit bezpečnost peněženky tím, že sníží rizika spojená s náhodným generováním mnemonické fráze.

Efektivní heslová fráze by měla být dlouhá (20 až 40 znaků) a rozmanitá (používající velká písmena, malá písmena, čísla a symboly). Neměla by být přímo spojena s uživatelem nebo jeho prostředím. Je bezpečnější použít náhodnou sekvenci znaků než jednoduché slovo jako heslovou frázi.

![image](assets/image/section3/9.webp)

Heslová fráze je bezpečnější než jednoduché heslo. Ideální heslová fráze je dlouhá, rozmanitá a náhodná. Může zvýšit bezpečnost peněženky nebo hot software. Také lze použít k vytvoření redundantních a bezpečných záloh.

Je zásadní pečovat o zálohy heslové fráze, aby nedošlo ke ztrátě přístupu k peněžence. Heslová fráze je možností pro HD peněženku. Lze ji generovat náhodně pomocí kostek nebo jiného pseudo-náhodného generátoru čísel. Nedoporučuje se zapamatovat si heslovou frázi nebo mnemonickou frázi.

V naší další lekci se podrobněji podíváme na fungování seedu a prvního párů klíčů generovaných z něj. Neváhejte sledovat tento kurz, abyste pokračovali ve svém učení. Těšíme se na vaše další setkání.

# Vytvoření Bitcoinových peněženek
<partId>9c25e767-7eae-50b8-8c5f-679d8fc83bab</partId>

## Vytvoření seedu a hlavního klíče
<chapterId>63093760-2010-5691-8d0e-9a04732ae557</chapterId>

V této části kurzu prozkoumáme kroky pro odvození Hierarchické Deterministické Peněženky (HD Wallet), která umožňuje hierarchické a deterministické vytváření a správu soukromých a veřejných klíčů.

![image](assets/image/section4/0.webp)

Základem HD peněženky jsou dva zásadní prvky: mnemonická fráze a heslová fráze (volitelné dodatečné heslo). Společně tvoří seed, alfanumerickou sekvenci 512 bitů, která slouží jako základ pro odvození klíčů peněženky. Z tohoto seedu je možné odvodit všechny dětské páry klíčů Bitcoinové peněženky. Seed je klíčem, který umožňuje přístup ke všem bitcoinům spojeným s peněženkou, ať už používáte heslovou frázi, nebo ne.

![image](assets/image/section4/1.webp)
Pro získání seedu se používá funkce pbkdf2 (Password-Based Key Derivation Function 2) spolu s mnemonickou frází a heslem. Výstupem funkce pbkdf2 je 512bitový seed.
Ze seedu je možné určit hlavní soukromý klíč a řetězový kód pomocí algoritmu HMAC SHA-512 (Hash-based Message Authentication Code Secure Hash Algorithm 512). Tento algoritmus vyžaduje pro generování výsledku zprávu a klíč jako vstup. Hlavní soukromý klíč je vypočítán ze seedu a fráze "Bitcoin SEED". Tato fráze je stejná pro všechny derivace všech HD peněženek, což zajišťuje konzistenci napříč peněženkami.

Původně nebyla funkce SHA-512 implementována v protokolu Bitcoinu, a proto se používá HMAC SHA-512. Použití HMAC SHA-512 s frází "Bitcoin SEED" omezuje uživatele na generování peněženky specifické pro Bitcoin. Výsledek HMAC SHA-512 je 512bitové číslo, rozdělené na dvě části: levých 256 bitů představuje hlavní soukromý klíč, zatímco pravých 256 bitů představuje hlavní řetězový kód.

![image](assets/image/section4/2.webp)

Hlavní soukromý klíč je rodičovský klíč všech budoucích klíčů v peněžence, zatímco hlavní řetězový kód se podílí na derivaci dětských klíčů. Je důležité poznamenat, že bez znalosti odpovídajícího řetězového kódu rodičovského páru je nemožné odvodit dětský klíčový pár.

Klíčový pár v peněžence se skládá ze soukromého klíče, veřejného klíče a řetězového kódu. Řetězový kód přináší zdroj náhodnosti do derivace dětských klíčů a izoluje každý klíčový pár, aby nedošlo k úniku jakýchkoli informací.
Je důležité si uvědomit, že hlavní soukromý klíč je první soukromý klíč odvozený ze seedu a nemá žádnou spojitost s rozšířenými klíči peněženky.

V další lekci se podrobněji zaměříme na rozšířené klíče, jako jsou xPub, xPRV, zPub, a pochopíme, proč se používají a jak jsou konstruovány.

## Rozšířené klíče
<chapterId>8dcffce1-31bd-5e0b-965b-735f5f9e4602</chapterId>

V této části lekce se budeme věnovat rozšířeným klíčům (xPub, zPub, yPub) a jejich prefixům, které hrají důležitou roli při odvozování dětských klíčů v Hierarchické Deterministické Peněžence (HD Wallet).

![image](assets/image/section4/3.webp)

Rozšířené klíče se liší od hlavních klíčů. HD peněženka generuje mnemonickou frázi a seed k získání hlavního klíče a hlavního řetězového kódu. Rozšířené klíče se používají k odvození dětských klíčů a vyžadují jak rodičovský klíč, tak odpovídající řetězový kód. Rozšířený klíč kombinuje tyto dvě informace, aby zjednodušil proces derivace.

![image](assets/image/section4/4.webp)

Rozšířené veřejné klíče mohou odvozovat pouze normální dětské veřejné klíče, zatímco rozšířené soukromé klíče mohou odvozovat jak dětské veřejné, tak soukromé klíče, a to jak prostřednictvím normální, tak zpevněné derivace. Zpevněná derivace odpovídá derivaci z rodičovského soukromého klíče, zatímco normální derivace odpovídá derivaci z rodičovského veřejného klíče.

Použití rozšířených klíčů s prefixem XPUB umožňuje odvozování nových adres bez nutnosti vracet se k odpovídajícím soukromým klíčům, čímž poskytuje lepší bezpečnost. Metadata spojená s rozšířenými klíči poskytují důležité informace o jejich roli a pozici v hierarchii klíčů.
Rozšířené klíče jsou identifikovány specifickými předponami (XPRV, XPUB, YPUB, ZPUB), které udávají, zda se jedná o rozšířený soukromý nebo veřejný klíč, stejně jako jejich konkrétní účel. Metadata spojená s rozšířeným klíčem zahrnují verzi (předponu), hloubku, otisk rodičovského klíče, index a payload (řetězec kódů a rodičovský klíč).
![image](assets/image/section4/5.webp)

Verze odpovídá typu klíče: xpub, xprv, ...

Hloubka odpovídá počtu derivací mezi rodičovskými a dětskými klíči od hlavního klíče.

Otisk rodiče je prvních 4 bajty z hash 160 rodičovského klíče.
Index je číslo páru, které se používá k generování rozšířeného klíče mezi jeho sourozenci. (sourozenci = klíče stejné hloubky) Například, pokud chceme odvodit xpub našeho 3. účtu, jeho index bude 2 (protože index začíná na 0).

Payload se skládá z řetězce kódů (32 bajtů) a rodičovského klíče (33 bajtů).

Komprimované veřejné klíče mají velikost 33 bajtů, zatímco surové veřejné klíče jsou 512 bitů. Komprimované veřejné klíče zachovávají stejné informace jako surové klíče, ale s redukovanou velikostí. Rozšířené klíče mají velikost 82 bajtů a jejich předpona je reprezentována v base 58 prostřednictvím konverze na hexadecimální. Kontrolní součet je vypočítán pomocí hash funkce HASH256.

![image](assets/image/section4/6.webp)

Pokročilé derivace začínají od indexů, které jsou mocninami 2 (2^31). Je zajímavé poznamenat, že nejčastěji používané předpony jsou xpub a zpub, které odpovídají respektive legacy standardům a segwit v1 a segwit v0.

V naší další lekci se zaměříme na derivaci dětských klíčových párů s využitím znalostí získaných o rozšířených klíčích a hlavním klíči peněženky.

## Derivace dětských klíčových párů
<chapterId>61c0807c-845b-5076-ad06-7f395b36adfd</chapterId>

Jako připomínka, diskutovali jsme o výpočtu seedu a hlavního klíče, které jsou prvními zásadními prvky pro hierarchickou organizaci a derivaci HD (Hierarchical Deterministic) peněženky. Seed, s délkou 128 až 256 bitů, je generován náhodně nebo z tajné fráze. Hraje deterministickou roli v derivaci všech ostatních klíčů. Hlavní klíč je první klíč odvozený ze seedu a umožňuje derivaci všech ostatních dětských klíčových párů.

Hlavní řetězec kódů hraje důležitou roli při obnově peněženky ze seedu. Je důležité poznamenat, že všechny klíče odvozené ze stejného seedu budou mít stejný hlavní řetězec kódů.

![image](assets/image/section4/7.webp)

Hierarchická organizace a derivace HD peněženky nabízí efektivnější správu klíčů a struktur peněženek. Rozšířené klíče umožňují derivaci dětského klíčového páru z rodičovského klíčového páru pomocí matematických výpočtů a specifických algoritmů.
Existují různé typy dětských klíčových párů, včetně posílených klíčů a normálních klíčů. Rozšířený veřejný klíč umožňuje derivaci pouze normálních dětských veřejných klíčů, zatímco rozšířený soukromý klíč umožňuje derivaci všech dětských klíčů, jak veřejných, tak soukromých, ať už jsou v normálním nebo posíleném režimu. Každý klíčový pár má index, který umožňuje jejich rozlišení od sebe.

![image](assets/image/section4/8.webp)
Odvození dětských klíčů využívá funkci HMAC-SHA512 s použitím rodičovského klíče spojeného s indexem a řetězcovým kódem spojeným s párem klíčů. Normální dětské klíče mají index v rozmezí od 0 do 2 na mocninu 31 mínus 1, zatímco posílené dětské klíče mají index v rozmezí od 2 na mocninu 31 do 2 na mocninu 32 mínus 1.
![image](assets/image/section4/9.webp)

![image](assets/image/section4/10.webp)

Existují dva typy párů dětských klíčů: posílené páry a normální páry. Proces odvození dětských klíčů využívá veřejné klíče pro generování podmínek utrácení, zatímco soukromé klíče jsou používány pro podepisování. Rozšířený veřejný klíč umožňuje odvození pouze normálních dětských veřejných klíčů, zatímco rozšířený soukromý klíč umožňuje odvození všech dětských klíčů, jak veřejných, tak soukromých, v normálním nebo posíleném režimu.

![image](assets/image/section4/11.webp)
![image](assets/image/section4/12.webp)

Posílené odvození využívá rodičovský soukromý klíč, zatímco normální odvození využívá rodičovský veřejný klíč. Funkce HMAC-SHA512 je použita pro posílené odvození, zatímco normální odvození využívá 512-bitový digest. Dětský veřejný klíč je získán násobením dětského soukromého klíče generátorem eliptické křivky.

![image](assets/image/section4/13.webp)
![image](assets/image/section4/14.webp)

Hierarchické odvozování a deterministické odvozování mnoha párů klíčů umožňuje vytvoření stromové struktury pro hierarchické odvozování. V další lekci tohoto školení se budeme zabývat strukturou HD peněženky a cestami odvození, s konkrétním zaměřením na notace cest odvození.

## Struktura peněženky a cesty odvození
<chapterId>34e1bbda-67de-5493-b268-1fded8d67689</chapterId>

V této kapitole se budeme zabývat strukturou odvozovacího stromu v Hierarchické Deterministické Peněžence (HD Peněženka). Již jsme prozkoumali výpočet seedu, hlavní klíč a odvození dětských párů klíčů. Nyní se zaměříme na organizaci klíčů v peněžence.

HD Peněženka využívá vrstvy hloubky pro organizaci klíčů. Každé odvození z rodičovského páru na dětský pár odpovídá vrstvě hloubky.

![image](assets/image/section4/15.webp)

- Hloubka 0 odpovídá hlavnímu klíči a hlavnímu řetězcovému kódu.

- Hloubka 1 je použita pro odvození dětských klíčů pro konkrétní účel, určený indexem. Účely jsou v souladu s BIP 84 a standardy Segwit v0/v1.

- Hloubka 2 umožňuje diferenciaci účtů pro různé kryptoměny nebo sítě. To umožňuje organizovat peněženku na základě různých zdrojů financí. Pro bitcoin bude index 0.

- Hloubka 3 je použita pro organizaci peněženky do různých účtů, což poskytuje jasnější a lépe organizovanou strukturu.

- Hloubka 4 odpovídá vnějším a vnitřním řetězcům, které jsou použity pro adresy určené k veřejnému sdělení. Index 0 je spojen s vnějším řetězcem, zatímco index 1 je spojen s vnitřním řetězcem. Každý účet má dva řetězce: vnější řetězec (0) a vnitřní řetězec (1). Hloubka 4 je také použita pro správu typů skriptů v případě peněženek s více podpisy.

- Hloubka 5 je použita pro přijímací adresy ve standardní peněžence. V další části se podrobněji podíváme na odvození dětských párů klíčů.

![image](assets/image/section4/16.webp)

Pro každou vrstvu hloubky používáme indexy pro diferenciaci dětských párů klíčů.
Index bez apostrofu odpovídá skutečně použitému indexu, zatímco index s apostrofem odpovídá skutečnému indexu + 2^31. Zpevněné derivace používají indexy od 2^31 do 2^32-1. Například, index 44' odpovídá skutečnému indexu 2^31 + 44.
K vygenerování konkrétní přijímací adresy odvodíme dětský klíčový pár z hlavního klíče a hlavního řetězového kódu. Poté použijeme index k rozlišení mezi různými dětskými klíčovými páry ve stejné hloubce.

Rozšířené klíče, jako je XPUB, vám umožňují sdílet vaši peněženku s více lidmi. Cesta derivace se používá k rozlišení mezi vnějším řetězcem (adresy určené k sdílení) a vnitřním řetězcem (adresy pro změnu).

V další kapitole se budeme věnovat přijímacím adresám, jejich výhodám použití a krokům zapojeným do jejich konstrukce.

# Co je Bitcoinová adresa?
<partId>81ec8d17-f8ee-5aeb-8035-d370866f4281</partId>

## Bitcoinové adresy
<chapterId>0a887ed8-3424-5a52-98e1-e4b406150475</chapterId>

V této kapitole se budeme zabývat přijímacími adresami, které hrají klíčovou roli v systému Bitcoinu. Umožňují přijímat prostředky na transakci a generují se z párů soukromých a veřejných klíčů. Ačkoliv existuje typ skriptu nazvaný Pay2PublicKey, který umožňuje uzamknout bitcoiny na veřejný klíč, uživatelé obecně dávají přednost používání přijímacích adres místo tohoto skriptu.

![image](assets/image/section5/0.webp)

Když příjemce chce přijmout bitcoiny, poskytne odesílateli místo svého veřejného klíče přijímací adresu. Adresa je ve skutečnosti hash veřejného klíče s konkrétním formátem. Veřejný klíč je odvozen z dětského soukromého klíče pomocí matematických operací, jako je sčítání bodů a zdvojení na eliptických křivkách.

![image](assets/image/section5/1.webp)

Je důležité poznamenat, že není možné provést reverzi z adresy na veřejný klíč, ani z veřejného klíče na soukromý klíč. Použití adresy snižuje velikost informací o veřejném klíči, která původně činí 512 bitů.

Velikost Bitcoinových adres byla snížena, aby se usnadnilo jejich používání. Mají kontrolní součet, který umožňuje detekovat překlepy a snižuje riziko ztráty bitcoinů. Na druhou stranu, veřejné klíče nemají kontrolní součet, což znamená, že překlepy mohou vést ke ztrátě odpovídajících prostředků.

Adresy také poskytují druhou úroveň bezpečnosti mezi veřejnými a soukromými informacemi, což ztěžuje převzetí kontroly nad soukromým klíčem.

Je zásadní zdůraznit, že každá adresa by měla být použita pouze jednou. Opětovné použití stejné adresy představuje problémy s ochranou soukromí a mělo by se tomu vyhnout.

Pro Bitcoinové adresy se používají různé předpony. Například, BC1Q odpovídá adrese Segwit V0, BC1P adrese Taproot/Segwit V1 a předpony 1 a 3 jsou spojeny s adresami Pay2PublicKeyH/Pay2ScriptH (legacy). V další lekci vysvětlíme krok za krokem, jak odvodit adresu z veřejného klíče.

## Jak vytvořit Bitcoinovou adresu?
<chapterId>6dee7bf3-7767-5f8d-a01b-659b95cfe0a5</chapterId>

V této kapitole se budeme zabývat konstrukcí přijímací adresy pro Bitcoinové transakce. Přijímací adresa je alfanumerické vyjádření komprimovaného veřejného klíče. Převod veřejného klíče na přijímací adresu zahrnuje několik kroků.

### Krok 1: Komprese veřejného klíče
![obrázek](assets/image/section5/14.webp)
Adresa je odvozena z dětského veřejného klíče.

Veřejný klíč je bod na eliptické křivce. Díky symetrii eliptické křivky bude mít bod na eliptické křivce souřadnici x spojenou pouze se dvěma možnými hodnotami pro y: kladnou nebo zápornou.
Nicméně, v protokolu Bitcoinu pracujeme s konečnou množinou kladných celých čísel, nikoli s množinou reálných čísel. Pro rozlišení mezi dvěma možnými hodnotami y stačí uvést, zda je y sudé nebo liché.

Komprese veřejného klíče snižuje jeho velikost z 520 bitů na 264 bitů.

Používáme prefix 0x02 pro sudé y a 0x03 pro liché y. To je komprimovaná forma veřejného klíče.

### Krok 2: Hašování komprimovaného veřejného klíče

![obrázek](assets/image/section5/3.webp)

Hašování komprimovaného veřejného klíče se provádí pomocí funkce SHA256. Poté se aplikuje funkce RIPEMD160 na výsledek.

### Krok 3: Payload = Adresní payload

![obrázek](assets/image/section5/4.webp)

Binární výstup RIPEMD160(SHA256(K)) se používá k vytvoření skupin po 5 bitech. Každá skupina je převedena do základu 16 (hexadecimální) a/nebo základu 10.

### Krok 4: Přidání metadat pro výpočet kontrolního součtu s programem BCH

![obrázek](assets/image/section5/5.webp)

V případě tradičních adres používáme dvojité hašování SHA256 k generování kontrolního součtu adresy. Nicméně, pro adresy Segwit V0 a V1 spoléháme na technologii kontrolního součtu BCH pro zajištění detekce chyb. Program BCH je schopen navrhovat a opravovat chyby s extrémně nízkou pravděpodobností chyby. V současnosti se program BCH používá k detekci a navrhování úprav, ale automaticky je nevykonává jménem uživatele.

Program BCH vyžaduje několik vstupních informací, včetně HRP (Human Readable Part), který je třeba rozšířit. Rozšíření HRP zahrnuje kódování každého písmene v základu 2 podle jejich ASCII kódu. Poté se vezmou první 3 bity výsledku pro každé písmeno a převedou se do základu 10 (modře na obrázku). Vloží se oddělovač 0. Poté se konkatenují následující 5 bitů každého písmene dříve převedeného do základu 10 (žlutě na obrázku).

Rozšíření HRP do základu 10 umožňuje izolovat posledních pět bitů každého znaku, čímž posiluje kontrolní součet.

Verze Segwit V0 je reprezentována kódem 00 a "payload" je v černé, v základu 10. Následuje šest rezervovaných znaků pro kontrolní součet.

### Krok 5: Výpočet kontrolního součtu s programem BCH

![obrázek](assets/image/section5/6.webp)

Vstup obsahující metadata je poté odeslán do programu BCH pro získání kontrolního součtu v základu 10.

Zde máme kontrolní součet.

### Krok 6: Konstrukce adresy a převod na Bech32

![obrázek](assets/image/section5/7.webp)

Konkatenace verze, payloadu a kontrolního součtu umožňuje sestavení adresy. Znaky v základu 10 jsou poté převedeny na znaky Bech32 pomocí tabulky korespondence. Abeceda Bech32 zahrnuje všechny alfanumerické znaky, kromě 1, b, i a o, aby se předešlo jakékoli záměně.

### Krok 7: Přidání HRP a oddělovače

![obrázek](assets/image/section5/8.webp)

V růžové, kontrolní součet.
V černé, zátěž = hash veřejného klíče. V modré, verze.

Vše je převedeno na Bech32, poté je přidáno 'bc' pro bitcoin a '1' jako oddělovač, a zde je adresa.

# Jít dále
<partId>58111408-b734-54db-9ea7-0d5b67f99f99</partId>

## Vytvoření seedu z 128 hodů kostkou!
<chapterId>0f4d40a7-cf0e-5faf-bc4d-691486771ac1</chapterId>

Vytvoření mnemonické fráze je klíčovým krokem pro zabezpečení vaší kryptoměnové peněženky. Existuje několik metod, jak vygenerovat mnemonickou frázi, nicméně se zaměříme na manuální metodu generování pomocí kostek. Je důležité poznamenat, že tato metoda není vhodná pro peněženku s vysokou hodnotou. Doporučuje se použít open-source software nebo hardwarovou peněženku pro generování mnemonické fráze. Pro vytvoření mnemonické fráze použijeme kostky k generování binárních informací. Cílem je pochopit proces vytváření mnemonické fráze.

**Krok 1 - Příprava:**
Ujistěte se, že máte na USB klíči nainstalovanou amnestickou distribuci Linuxu, jako je Tails OS, pro zvýšenou bezpečnost. Poznamenejte si, že tento tutoriál by neměl být použit pro vytvoření hlavní peněženky.
**Krok 2 - Generování náhodného binárního čísla:**
Použijeme kostky k generování binárních informací. Hodíme kostkou 128krát a zaznamenáme každý výsledek (1 pro liché, 0 pro sudé).

**Krok 3 - Organizace binárních čísel:**
Organizujte získaná binární čísla do řádků po 11 číslicích, aby se usnadnily další výpočty. Dvanáctý řádek by měl mít pouze 7 číslic.

**Krok 4 - Výpočet kontrolního součtu:**
Poslední 4 číslice pro dvanáctý řádek odpovídají kontrolnímu součtu. Pro výpočet tohoto kontrolního součtu potřebujeme použít terminál z distribuce Linuxu. Doporučuje se použít [TailOs](https://tails.boum.org/index.fr.html), což je bootovatelná paměťově nezávislá distribuce z USB klíče. Jakmile jste ve svém terminálu, zadejte příkaz `echo <binární číslo> | shasum -a 254 -0`. Nahraďte `<binární číslo>` vaším seznamem 128 nul a jedniček. Výstupem je hexadecimální hash. Zaznamenejte první znak tohoto hashe a převeďte ho na binární. Pro pomoc můžete použít tuto [tabulku](https://www.educative.io/answers/decimal-binary-and-hex-conversion-table). Přidejte binární kontrolní součet (4 číslice) do dvanáctého řádku vašeho listu.

**Krok 5 - Převod na desítkový systém:**
Abychom našli slova spojená s každým z vašich řádků, musíte nejprve převést každou sérii 11 bitů na desítkové číslo. Zde nemůžete použít online převodník, protože tyto bity představují vaši mnemonickou frázi. Proto budete muset převést pomocí kalkulačky a triku, který je následující: každý bit je spojen s mocninou čísla 2, takže zleva doprava máme 11 řad odpovídajících 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1. Pro převod vaší série 11 bitů na desítkové číslo jednoduše sečtěte pouze řady, které obsahují 1. Například pro sérii 00110111011, to odpovídá následujícímu sčítání: 256 + 128 + 32 + 16 + 8 + 2 + 1 = 443. Nyní můžete převést každý řádek na desítkové číslo. A před přechodem na kódování do slov přičtěte ke všem řádkům +1, protože index seznamu slov BIP39 začíná od 1, nikoli od 0.
**Krok 8 - Generování mnemonické fráze:**
Začněte tím, že si vytisknete [seznam 2048 slov](https://seedxor.com/files/wordlist.pdf), abyste mohli převést vaše desítková čísla na slova BIP39. Unikátnost tohoto seznamu spočívá v tom, že žádné slovo nesdílí první 4 písmena s žádným jiným slovem v tomto slovníku. Poté vyhledejte slovo spojené s desítkovým číslem každého z vašich řádků.
**Krok 9 - Test mnemonické fráze:**
Okamžitě otestujte svou mnemonickou frázi na Sparrow Wallet tím, že z ní vytvoříte peněženku. Pokud obdržíte chybu neplatného kontrolního součtu, je pravděpodobné, že jste udělali chybu ve výpočtu. Tuto chybu opravte návratem ke kroku 4 a znovu otestujte na Sparrow Wallet. Voilà! Právě jste vytvořili novou Bitcoin peněženku z 128 hodů kostkou.

Generování mnemonické fráze je důležitý proces pro zabezpečení vaší kryptoměnové peněženky. Doporučuje se používat bezpečnější metody, jako je použití open-source softwaru nebo hardwarové peněženky, pro generování mnemonické fráze. Avšak dokončení tohoto workshopu pomáhá lépe pochopit, jak můžeme vytvořit Bitcoin peněženku z náhodného čísla.

## BONUS: Rozhovor s Théo Pantamisem
<chapterId>39f0ec5a-e258-55cb-9789-bc46d314d816</chapterId>

Další široce používanou kryptografickou metodou v protokolu Bitcoin je metoda digitálních podpisů.

![video](https://youtu.be/c9MvtGJsEvY?si=bQ1N5NCd6op0G6nW)



## Ohodnoťte kurz
<chapterId>0cd71541-a7fd-53db-b66a-8611b6a28b04</chapterId>
<isCourseReview>true</isCourseReview>

## Závěrečná zkouška
<chapterId>a53ea27d-0f84-56cd-b37c-a66210a4b31d</chapterId>
<isCourseExam>true</isCourseExam>


## Závěr a konec
<chapterId>d291428b-3cfa-5394-930e-4b514be82d5a</chapterId>

### Děkujeme a pokračujte ve zkoumání králičí nory

Rádi bychom vám upřímně poděkovali za dokončení kurzu Crypto 301. Doufáme, že pro vás byla tato zkušenost obohacující a vzdělávací. Probrali jsme mnoho vzrušujících témat, od matematiky přes kryptografii až po fungování protokolu Bitcoin.

Pokud byste se chtěli do tématu ponořit hlouběji, máme pro vás další zdroj. Provedli jsme exkluzivní rozhovor s Théo Pantamisem a Loïcem Morelem, dvěma uznávanými odborníky v oblasti kryptografie. Tento rozhovor prozkoumává různé aspekty tématu do hloubky a poskytuje zajímavé perspektivy.

Pokud máte zájem, podívejte se na tento rozhovor, abyste pokračovali v průzkumu fascinujícího světa kryptografie. Doufáme, že to bude pro vás užitečné a inspirující na vaší cestě. Ještě jednou děkujeme za vaši účast a závazek během celého kurzu.

### Podpořte nás
Tento kurz, stejně jako veškerý obsah na této univerzitě, vám byl poskytnut zdarma naší komunitou. Můžete nás podpořit tím, že jej sdílíte s ostatními, stane se členem univerzity a dokonce přispět k jejímu rozvoji prostřednictvím GitHubu. Jménem celého týmu vám děkujeme!
### Ohodnoťte kurz
Systém hodnocení pro školení bude brzy integrován do této nové E-learningové platformy! Mezitím vám velmi děkujeme za absolvování kurzu a pokud se vám líbil, zvažte prosím jeho sdílení s ostatními.
