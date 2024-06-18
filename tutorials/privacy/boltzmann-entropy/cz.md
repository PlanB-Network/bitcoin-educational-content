---
name: Boltzmann Calculator
description: Porozumění konceptu entropie a použití Boltzmannova kalkulátoru
---
![cover](assets/cover.webp)

***VAROVÁNÍ:** Po zatčení zakladatelů Samourai Wallet a zabavení jejich serverů 24. dubna je web KYCP.org aktuálně nedostupný. Gitlab hostující kód Boltzmannova kalkulátoru v Pythonu byl také zabaven. Nyní již není možné toto nástroj stáhnout. Existuje však možnost, že kód bude v nadcházejících týdnech znovu zveřejněn jinými osobami. Mezitím můžete stále využít tohoto tutoriálu k pochopení fungování Boltzmannova kalkulátoru. Ukazatele poskytované tímto nástrojem jsou aplikovatelné na jakoukoli Bitcoinovou transakci a lze je také vypočítat ručně. V tomto tutoriálu poskytnu všechny potřebné výpočty. Pokud jste si již Pythonový nástroj stáhli na svůj počítač nebo používáte RoninDojo, můžete nástroj dále používat a tutoriál sledovat jako obvykle, stále funguje.*

_Sledujeme vývoj této kauzy i vývoj souvisejících nástrojů. Ujistěte se, že tento tutoriál aktualizujeme, jakmile budou k dispozici nové informace._

_Tento tutoriál je poskytován pouze pro vzdělávací a informační účely. Nepodporujeme ani nevyzýváme k používání těchto nástrojů pro kriminální účely. Je odpovědností každého uživatele dodržovat zákony ve své jurisdikci._

---

Boltzmannův kalkulátor je nástroj pro analýzu Bitcoinové transakce měřením její úrovně entropie spolu s dalšími pokročilými metrikami. Poskytuje vhledy do spojení mezi vstupy a výstupy transakce. Tyto ukazatele nabízejí kvantifikované hodnocení soukromí transakce a pomáhají identifikovat potenciální chyby.

Tento Pythonový nástroj byl vyvinut týmy Samourai Wallet a OXT, ale lze jej použít na jakoukoli Bitcoinovou transakci.

## Jak používat Boltzmannův kalkulátor?
K použití Boltzmannova kalkulátoru máte dvě možnosti. První je přímo nainstalovat Pythonový nástroj na váš počítač. Alternativně můžete využít web KYCP.org (_Know Your Coin Privacy_), který nabízí zjednodušenou platformu pro použití. Pro uživatele [RoninDojo](https://planb.network/tutorials/node/ronin-dojo-v2) vězte, že tento nástroj je již do vašeho uzlu integrován.

Použití webu KYCP je velmi jednoduché: stačí zadat identifikátor transakce (TXID), který chcete analyzovat, do vyhledávacího pole a stisknout `ENTER`.
![KYCP](assets/1.webp)
Poté najdete různé informace o transakci, včetně spojení mezi vstupy a výstupy. Klikněte na `deterministické spojení`.
![KYCP](assets/2.webp)
Dostanete se na stránku věnovanou ukazatelům Boltzmannova kalkulátoru.
![KYCP](assets/3.webp)
Pro ty, kteří dávají přednost použití nástroje přímo z jejich uzlu RoninDojo, je přístupný přes `RoninCLI > Samourai Toolkit > Boltzmann Calculator`.

Stejně jako na webu KYCP.org, jakmile je Pythonový nástroj nainstalován, jednoduše vložíte TXID transakce, kterou chcete analyzovat.

![KYCP](assets/7.webp)

Poté stiskněte klávesu `ENTER`, abyste získali výsledky.

![KYCP](assets/8.webp)

## Jaké jsou ukazatele Boltzmannova kalkulátoru?
### Kombinace / Interpretace:
Prvním ukazatelem, který software vypočítá, je celkový počet možných kombinací, označený pod `nb combinations` nebo `interpretations` v nástroji.
Při zohlednění hodnot UTXO zapojených do transakce tento ukazatel vypočítává počet způsobů, jakými mohou být vstupy spojeny s výstupy. Jinými slovy, určuje počet pravděpodobných interpretací, které může transakce vyvolat z pohledu vnějšího pozorovatele, který ji analyzuje. Například coinjoin strukturovaný podle modelu Whirlpool 5x5 představuje `1,496` možných kombinací: ![KYCP](assets/4.webp)
Na druhou stranu coinjoin Whirlpool Surge Cycle 8x8 představuje `9,934,563` možných interpretací: ![KYCP](assets/5.webp)
Naopak, tradičnější transakce s 1 vstupem a 2 výstupy bude mít pouze jednu interpretaci: ![KYCP](assets/6.webp)

### Entropie:
Druhým vypočítaným ukazatelem je entropie transakce, označovaná jako `Entropy`.

V obecném kontextu kryptografie a informací je entropie kvantitativní míra nejistoty nebo nepředvídatelnosti spojené se zdrojem dat nebo náhodným procesem. Jinými slovy, entropie je způsob měření, jak obtížné je informace předpovědět nebo uhodnout.

Ve specifickém kontextu analýzy řetězců je entropie také název ukazatele, odvozeného od Shannonovy entropie a [vynalezeného LaurentMT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf), který se vypočítává pomocí nástroje Boltzmann.

Když transakce představuje vysoký počet možných kombinací, je často relevantnější odkazovat na její entropii. Tento ukazatel umožňuje měřit nedostatek znalostí analytiků o přesné konfiguraci transakce. Jinými slovy, čím vyšší entropie, tím obtížnější úkol identifikovat pohyby bitcoinů mezi vstupy a výstupy pro analytiky.

V praxi entropie odhaluje, zda z pohledu vnějšího pozorovatele transakce představuje více možných interpretací, založených pouze na částkách vstupů a výstupů, aniž by se zohledňovaly další vnější nebo vnitřní vzory a heuristiky. Vysoká entropie je pak synonymem lepší důvěrnosti pro transakci.

Entropie je definována jako binární logaritmus počtu možných kombinací. Zde je použitý vzorec:
```plaintext
E: entropie transakce
C: počet možných kombinací pro transakci

E = log2(C)
```

V matematice odpovídá binární logaritmus (logaritmus o základu 2) inverzní operaci umocňování čísla 2. Jinými slovy, binární logaritmus `x` je exponent, na který musí být `2` zvýšeno, aby se získalo `x`. Tento ukazatel je tedy vyjádřen v bitech.

Vezměme si příklad výpočtu entropie pro coinjoin transakci strukturovanou podle modelu Whirlpool 5x5, která, jak bylo zmíněno dříve, nabízí počet možných kombinací `1,496`:
```plaintext
C = 1,496
E = log2(1,496)
E = 10.5469 bitů
```
Takže tato coinjoin transakce vykazuje entropii `10.5469 bitů`, což je považováno za velmi uspokojivé. Čím vyšší tato hodnota, tím více různých interpretací transakce připouští, čímž posiluje její úroveň soukromí.
Pro 8x8 coinjoin transakci představující `9,934,563` interpretací by entropie byla:
```plaintext
C = 9,934,563
E = log2(9,934,563)
E = 23.244 bitů
```
Podívejme se na další příklad s konvenčnější transakcí, která obsahuje jeden vstup a dva výstupy: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://mempool.space/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce) V případě této transakce je jediná možná interpretace: `(In.0) > (Out.0 ; Out.1)`. V důsledku toho je její entropie stanovena na `0`:```plaintext
C = 1
E = log2(1)
E = 0 bitů
```

### Efektivita:
Třetím ukazatelem, který poskytuje Kalkulačka Boltzmann, je pojmenován `Efektivita Peněženky` (Wallet Efficiency). Tento ukazatel hodnotí efektivitu transakce porovnáním s optimální transakcí, která by byla možná ve stejné konfiguraci.

To nás přivádí k diskusi o konceptu maximální entropie, která odpovídá nejvyšší entropii, kterou by konkrétní struktura transakce teoreticky mohla dosáhnout. Efektivita transakce je poté vypočítána porovnáním této maximální entropie s aktuální entropií analyzované transakce.

Použitý vzorec je následující:
```plaintext
ER: aktuální entropie transakce vyjádřená v bitech
EM: maximální možná entropie pro danou strukturu transakce vyjádřená v bitech
Ef: efektivita transakce vyjádřená v bitech

Ef = ER - EM
```

Například pro strukturu coinjoin typu Whirlpool 5x5 je maximální entropie stanovena na `10.5469`:
```plaintext
ER = 10.5469
EM = 10.5469
Ef = 10.5469 - 10.5469 = 0 bitů
```

Tento ukazatel je také vyjádřen jako procento, jeho vzorec je poté:
```plaintext
CR: aktuální počet možných kombinací
CM: maximální počet možných kombinací se stejnou strukturou
Ef: efektivita vyjádřená jako procento

Ef = CR / CM
Ef = 1,496 / 1,496
Ef = 100%
```

Efektivita `100%` tedy naznačuje, že transakce maximalizuje svůj potenciál pro soukromí podle své struktury.

### Hustota Entropie:
Čtvrtým ukazatelem je hustota entropie, označovaná na nástroji jako `Hustota Entropie` (Entropy Density). Poskytuje perspektivu entropie vzhledem ke každému vstupu nebo výstupu transakce. Tento ukazatel se ukazuje užitečný pro hodnocení a porovnávání efektivity transakcí různých velikostí. Pro její výpočet jednoduše vydělte celkovou entropii transakce celkovým počtem zapojených vstupů a výstupů:
```plaintext
ED: hustota entropie vyjádřená v bitech
E: entropie transakce vyjádřená v bitech
T: celkový počet vstupů a výstupů v transakci

ED = E / T
```

Podívejme se na příklad coinjoinu Whirlpool 5x5:
```plaintext
T = 5 + 5 = 10
E = 10.5469
ED = 10.5469 / 10 = 1.054 bitů
```

Spočítejme také hustotu entropie pro coinjoin Whirlpool 8x8:
```plaintext
T = 8 + 8 = 16
E = 23.244
ED = 23.244 / 16 = 1.453 bitů
```

### Boltzmannovo Skóre:
Pátý kus informace poskytnutý kalkulačkou Boltzmann je tabulka pravděpodobností shody mezi vstupy a výstupy. Tato tabulka ukazuje prostřednictvím Boltzmannova skóre podmíněnou pravděpodobnost, že určitý vstup souvisí s daným výstupem.
Jedná se tedy o kvantitativní míru podmíněné pravděpodobnosti, že mezi vstupem a výstupem v transakci dojde k asociaci, na základě poměru počtu příznivých výskytů této události k celkovému počtu možných výskytů, v sadě interpretací.

Při použití příkladu s Whirlpool coinjoin znovu, tabulka podmíněných pravděpodobností by zdůraznila šance na propojení mezi každým vstupem a výstupem, poskytující kvantitativní míru nejednoznačnosti asociací v transakci:

| %       | Výstup 0 | Výstup 1 | Výstup 2 | Výstup 3 | Výstup 4 |
| ------- | -------- | -------- | -------- | -------- | -------- |
| Vstup 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Vstup 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Vstup 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Vstup 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Vstup 4 | 34%      | 34%      | 34%      | 34%      | 34%      |

Zde můžeme jasně vidět, že každý vstup má stejnou šanci být spojen s jakýmkoli výstupem, což zvyšuje důvěrnost transakce.
Výpočet Boltzmannova skóre zahrnuje dělení počtu interpretací, ve kterých určitá událost nastane, celkovým počtem dostupných interpretací. Takto, pro určení skóre spojující vstup č. 0 s výstupem č. 3 (`512` interpretací), se použije následující postup:
```plaintext
Interpretace (IN.0 > OUT.3) = 512
Celkové interpretace = 1496
Skóre = 512 / 1496 = 34%
```

Při použití příkladu s Whirlpool 8x8 coinjoin (surge cycle), by tabulka Boltzmann vypadala takto:

|       | OUT.0 | OUT.1 | OUT.2 | OUT.3 | OUT.4 | OUT.5 | OUT.6 | OUT.7 |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| IN.0  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.1  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.2  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.3  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.4  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.5  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.6  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.7  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |

Nicméně, v případě jednoduché transakce s jedním vstupem a dvěma výstupy je situace odlišná:

| %       | Výstup 0 | Výstup 1 |
|---------|----------|----------|
| Vstup 0 | 100%     | 100%     |

Zde je pozorováno, že pravděpodobnost, že každý výstup pochází z vstupu č. 0, je `100%`. Nižší pravděpodobnost tedy překládá do většího soukromí tím, že rozptyluje přímé vazby mezi vstupy a výstupy.

### Deterministické vazby:
Šestý poskytnutý kus informace je počet deterministických vazeb doplněný o poměr těchto vazeb. Tento ukazatel odhaluje, kolik spojení mezi vstupy a výstupy v analyzované transakci je nesporných, s pravděpodobností `100%`. Poměr na druhé straně nabízí perspektivu na váhu těchto deterministických vazeb v celém souboru transakčních spojení.
Například transakce typu Whirlpool coinjoin nemá žádné deterministické vazby a proto zobrazuje ukazatel a poměr `0%`. Naopak, v naší druhé zkoumané jednoduché transakci (s jedním vstupem a dvěma výstupy) je ukazatel nastaven na `2` a poměr dosahuje `100%`. Tedy nulový ukazatel signalizuje vynikající důvěrnost díky absenci přímých a nesporných spojení mezi vstupy a výstupy.

**Externí zdroje:**

- Boltzmannův kód na Samourai
- [Bitcoinové transakce & Soukromí (Část I) od Laurenta MT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [Bitcoinové transakce & Soukromí (Část II) od Laurenta MT](https://gist.github.com/LaurentMT/d361bca6dc52868573a2)
- [Bitcoinové transakce & Soukromí (Část III) od Laurenta MT](https://gist.github.com/LaurentMT/e8644d5bc903f02613c6)
- Webová stránka KYCP
- [Článek na Medium o úvodu do Boltzmannova skriptu od Laurenta MT](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)