---
name: Remix - Whirlpool
description: Kolik remixů by mělo být provedeno na Whirlpool?
---
![cover remix- wp](assets/cover.webp)

***VAROVÁNÍ:** Po zatčení zakladatelů peněženky Samourai a zabavení jejich serverů 24. dubna již nástroj Whirlpool Stats Tool není dostupný ke stažení, jelikož byl hostován na Gitlabu Samourai. I když jste si tento nástroj dříve stáhli lokálně na svůj počítač, nebo byl nainstalován na vašem uzlu RoninDojo, WST v tuto chvíli nefunguje. Jeho provoz byl závislý na datech poskytovaných webem OXT.me, který již není přístupný. V současné době není WST zvlášť užitečný, protože protokol Whirlpool je neaktivní. Nicméně je možné, že tyto softwary budou v nadcházejících týdnech znovu zprovozněny. Navíc teoretická část tohoto článku zůstává relevantní pro pochopení principů a cílů coinjoinů obecně (nejen Whirlpool), stejně jako pro pochopení účinnosti modelu Whirlpool. Také se můžete naučit, jak kvantifikovat soukromí poskytované cykly coinjoin.*

_Sledujeme vývoj této kauzy stejně jako vývoj souvisejících nástrojů. Ujistěte se, že tento tutoriál aktualizujeme, jakmile budou k dispozici nové informace._

_Tento tutoriál je poskytován pouze pro vzdělávací a informační účely. Nepodporujeme ani nevyzýváme k používání těchto nástrojů pro kriminální účely. Je zodpovědností každého uživatele dodržovat zákony ve své jurisdikci._

---

> *"Přerušte spojení, které za sebou zanechávají vaše mince"*

Toto je otázka, na kterou jsem často dotazován. **Při provádění coinjoinů s Whirlpool, kolik remixů by mělo být provedeno pro dosažení uspokojivých výsledků?**

Cílem coinjoinu je nabídnout věrohodné popření tím, že smíchá vaši minci s skupinou nerozlišitelných mincí. Cílem této akce je přerušit sledovatelné spojení, jak z minulosti do současnosti, tak ze současnosti do minulosti. Jinými slovy, analytik, který zná vaši počáteční transakci na vstupu do cyklů coinjoin, by neměl být schopen jednoznačně identifikovat vaše UTXO na výstupu z remixových cyklů (analýza od vstupních cyklů k výstupním cyklům).
![past-present links diagram](assets/en/1.webp)

Naopak, analytik, který zná vaše UTXO na výstupu z cyklů coinjoin, by neměl být schopen určit původní transakci na vstupu do cyklů (analýza od výstupních cyklů k vstupním cyklům).
![present-past links diagram](assets/en/2.webp)
Nicméně, počet remixů není spolehlivým kritériem pro hodnocení obtížnosti, kterou by analytik měl při pokusu o navázání spojení mezi minulostí a současností, nebo naopak. Relevantnějším ukazatelem by byla velikost skupin, ve kterých se vaše mince skrývá. Tyto ukazatele se nazývají "anonsety". V případě Whirlpool existují dva typy anonsetů.

Za prvé, můžeme určit velikost skupiny, ve které je vaše UTXO skryto na výstupu z cyklů coinjoin, tj. počet nerozlišitelných mincí přítomných v této skupině.
![probable UTXOs at exit](assets/en/3.webp)
Tento ukazatel, nazývaný ve francouzštině "prospective anonset", v angličtině "forward anonset" nebo "forward-looking metrics", nám umožňuje posoudit odolnost vaší mince vůči analýzám sledujícím její cestu od vstupu do výstupu z cyklů coinjoin. Tato metrika odhaduje míru, do jaké je váš UTXO chráněn proti pokusům o rekonstrukci jeho historie od vstupního bodu po výstupní bod v procesu coinjoin. Například, pokud vaše transakce zúčastnila svého prvního cyklu coinjoin a byly provedeny další dva následné cykly, prospective anonset vaší mince by byl `13`: ![forward anonset](assets/en/4.webp)
Za druhé, další ukazatel lze vypočítat k hodnocení odolnosti vaší mince vůči analýze od současnosti do minulosti. Znáním vašeho UTXO na konci cyklů tento ukazatel určuje počet potenciálních transakcí Tx0, které by mohly tvořit váš vstup v cyklech coinjoin (analýza od konce k začátku cyklů). Tento ukazatel měří, jak obtížné je pro analytika vystopovat původ vaší mince po jejím průchodu coinjoiny. ![Probable sources at input](assets/en/5.webp)
Název tohoto ukazatele je "backward anonset" nebo "backward-looking metrics". Ve francouzštině mám rád označení "anonset rétrospectif". Na níže uvedeném diagramu to odpovídá všem oranžovým bublinám Tx0:
![backward anonset](assets/en/6.webp)
Pokud chcete zjistit více o metodě výpočtu těchto ukazatelů, doporučuji přečíst [můj Twitterový vlákno](https://twitter.com/Loic_Pandul/status/1550850558147395585?s=20) na toto téma. Také připravujeme rozsáhlejší článek o síti PlanB.

Vím, že poskytnutá odpověď se může jevit jako neuspokojivá, protože jste doufali v konkrétní počet remixů, a proto vás odkazuji na dokumentaci. Důvodem je, že počet remixů je nespolehlivým ukazatelem pro hodnocení anonymity získané v cyklech coinjoin. Proto není možné definovat pevný počet remixů jako absolutní a univerzální bezpečnostní práh.

Je pravda, že každý další remix vaší mince zvyšuje její anonymity sets. Je však důležité pochopit, že to jsou primárně remixy prováděné vašimi vrstevníky, které přispívají k růstu vašeho prospective anonset. S modelem Whirlpool může vaše transakce dosáhnout značných úrovní prospective anonset jen s dvěma nebo třemi cykly coinjoin, pouze prostřednictvím aktivity vrstevníků zapojených do předchozích coinjoinů.

Na druhou stranu, retrospective anonset není v našem případě předmětem zájmu. Ve skutečnosti, od vašeho počátečního coinjoinu, těžíte z dědictví předchozích transakcí v poolu, okamžitě dávající vaší minci vysoký backward anonset, s marginálním nárůstem v každém následujícím cyklu.
Je také důležité pochopit, že vytvoření věrohodného popření nikdy není kompletní. Spoléhá se na pravděpodobnost sledování vaší kryptoměny. Tato pravděpodobnost klesá s rostoucí velikostí skupin, které ji skrývají. Proto byste měli přizpůsobit své cíle v termínech anonsetů podle vašich osobních očekávání. Zeptejte se sami sebe na důvody, které vás vedou k používání coinjoinů a na úrovně anonymity, které jsou nutné pro dosažení těchto cílů. Například, pokud je použití coinjoinů zaměřeno pouze na zachování soukromí vaší peněženky při posílání několika satoshi vašemu kmotřenci k narozeninám, velmi vysoké úrovně anonymity nejsou nutné. Váš kmotřenec pravděpodobně není schopen provádět hloubkovou analýzu řetězce a i kdyby byl, důsledky pro váš život by nebyly katastrofické. Nicméně, pokud jste terčem autoritářského režimu, kde nejmenší kousek informace může vést k uvěznění, vaše akce budou muset být řízeny mnohem přísnějšími kritérii.
K určení těchto slavných ukazatelů anonsetu můžete použít Python nástroj nazvaný **WST** (Whirlpool Stats Tool).

Nicméně, není vždy nutné počítat anonsety každé vaší coinjoined mince. Samotný design Whirlpoolu vám již poskytuje záruky. Jak bylo zmíněno dříve, retrospektivní anonset je zřídka obavou. Od vašeho počátečního míchání již získáváte zvláště vysoké retrospektivní skóre. Co se týče budoucího anonsetu, stačí, když necháte vaši minci na post-mix účtu dostatečně dlouhou dobu. Například, zde jsou skóre anonsetu jedné mé mince `100,000 satoshi` po strávení dvou měsíců v coinjoin bazénu:
![WST anonsety](assets/en/7.webp)
Ukazuje retrospektivní skóre `34,593` a budoucí skóre `45,202`. Konkrétně to znamená dvě věci:
- Pokud analytik zná mou minci na konci cyklů a pokusí se vystopovat její původ, narazí na `34,593` potenciálních zdrojů, každý s rovnou pravděpodobností, že je můj.
- Pokud analytik zná mou minci na začátku cyklů a pokusí se určit její korespondenci na konci, bude čelit `45,202` možným UTXO, každé s tou samou pravděpodobností, že je moje.
To je důvod, proč považuji použití Whirlpoolu za zvláště relevantní v strategii `Hodl -> Mix -> Spend -> Replace`. Podle mého názoru je nejlogičtější přístup udržovat většinu úspor v bitcoinech v cold peněžence, zatímco neustále udržovat určitý počet mincí v coinjoinu na Samourai pro pokrytí denních výdajů. Jakmile jsou bitcoiny z coinjoinů utraceny, jsou nahrazeny novými, aby se vrátily na definovanou hranici smíšených mincí. Tato metoda nám umožňuje osvobodit se od starostí o anonsety našich UTXO, zatímco činí čas potřebný pro účinnost coinjoinů mnohem méně restriktivním.

Doufám, že tato odpověď osvětlila model Whirlpool. Pokud se chcete dozvědět více o tom, jak coinjoiny fungují na Bitcoinu, doporučuji přečíst můj podrobný článek na toto téma :

https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2

**Externí zdroje:**
- Samourai Wallet Whirlpool
- https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
Jako zkušený profesionální překladatel je vaším hlavním úkolem přesně přeložit technický obsah z angličtiny do vašeho mateřského jazyka, češtiny. Prosím, řiďte se následujícími pokyny, abyste zajistili kvalitní překlad:

Původní jazyk: Obsah je původně v angličtině.
Povaha obsahu: Setkáte se s technickým materiálem, který může zahrnovat specifickou terminologii daného odvětví.
Odkazy & Technická slova: Neřekládejte URL adresy ani vysoce specifické technické termíny. Pokud si nejste jisti, ponechte původní termín.
Konstantnost formátování: Zachovejte stejné rozložení markdown a formátování jako v původním textu. Konzistence struktury je klíčová.
Vlastnosti YML: Pokud řádek začíná vlastností YAML (např. 'name:', 'goal:', 'objectives:'), ponechte název vlastnosti v angličtině.
Kulturní kontext: U kulturních nebo kontextově specifických odkazů, které nemusí být přímo přeložitelné, parafrázujte, abyste zachovali zamýšlený význam, nebo poskytněte stručné vysvětlení.
Důraz by měl být kladen na udržení integrity technického obsahu, přičemž překlad by měl být srozumitelný a kontextově přesný v češtině.

Tento text je příkladem, jak by měl být přeložen:

- https://estudiobitcoin.com/jak-nainstalovat-a-používat-whirlpool-stats-tools-wst-pro-výpočty-sad-anonymity-transakcí-coinjoins/
- https://medium.com/samourai-wallet/potápění-se-na-hlavičku-do-whirlpool-anonymity-sets-4156a54b0bc7.

Všimněte si, že URL adresy zůstávají nezměněny, protože představují specifické zdroje informací, které nemusí být dostupné v češtině, a proto je důležité je ponechat v jejich původní formě pro uživatele, kteří hledají další informace.