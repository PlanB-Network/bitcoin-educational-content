---
name: Hluboký ponor do Simplicity
goal: Ovládněte návrhovou filozofii, typový systém a celý životní cyklus jazyka Simplicity
objectives:
  - Pochopte tři základní metody kompozice a devět kombinátorů, které dohromady tvoří úplný jazyk
  - Postavte booleovskou logiku, aritmetiku a SHA-256 z minimálního typového systému jazyka Simplicity
  - Pochopte, jak vedlejší efekty Failure a Reader umožňují skutečnou interakci s blockchainem
  - Naučte se, jak se programy v jazyce Simplicity stávají Taproot adresami a jak se uplatňují pomocí witness dat
---

# Hluboký ponor do Simplicity

Hloubkový ponor do teorie a návrhových rozhodnutí, která stojí za jazykem Simplicity, založený na kompletní pětidílné sérii článků [„Delving Simplicity"](https://delvingbitcoin.org/t/delving-simplicity-part-three-fundamental-ways-of-combining-computations/1902) od [Dr. Russella O'Connora](https://r6.ca/), tvůrce jazyka Simplicity v Blockstream Research. Tento kurz vysvětluje, *proč* byl Simplicity navržen tak, jak byl, nikoli jak jej psát.

Kurz sleduje články Dr. O'Connora: tři základní způsoby kombinování výpočtů, minimální typový systém a jeho větu o úplnosti, konstrukci praktických datových typů a aritmetiky od základů, opatrné zavedení vedlejších efektů pro interakci s blockchainem a nakonec to, jak se programy commitují do adres a jak se uplatňují on-chain.

+++

# Úvod

<partId>c362889b-c630-435f-911b-724c4eca505b</partId>

## Přehled kurzu

<chapterId>cdcc40b6-c985-45b4-9bee-6f931e984476</chapterId>

Vítejte v kurzu SCR403 — Hluboký ponor do Simplicity!

Tento kurz vychází ze série článků **„Delving Simplicity"**, kterou napsal [Dr. Russell O'Connor](https://r6.ca/), Infrastructure Tech Developer ve společnosti [Blockstream](https://blockstream.com/) a tvůrce jazyka Simplicity. Původní články byly publikovány na fóru [Delving Bitcoin](https://delvingbitcoin.org/u/roconnor-blockstream/summary) a tvoří primární zdrojový materiál tohoto kurzu. Jsme vděční za jeho průkopnickou práci, která tento vzdělávací obsah umožnila.

### Co se naučíte

Tento kurz zkoumá návrhovou filozofii a matematické základy jazyka Simplicity, skriptovacího jazyka nové generace aktivovaného na [síti Liquid](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/) v červenci 2025. Sleduje kompletní pětidílnou sérii článků a je rozdělen do dvou hlavních obsahových částí:

1. **Základy jazyka Simplicity** — Proč blockchainový výpočet vyžaduje zásadně odlišný jazyk, tři způsoby kombinování operací (sekvenční, paralelní, podmíněný) a devět základních kombinátorů, které tvoří matematicky úplný jazyk
2. **Od datových typů k programům** — Budování booleovské logiky, aritmetiky a SHA-256 od základů; pochopení vedlejších efektů Failure a Reader, které umožňují interakci s blockchainem; a to, jak se programy commitují do Taproot adres prostřednictvím Commitment Merkle Roots a jak se uplatňují pomocí witness dat

### Předpoklady

Toto je kurz **na expertní úrovni** (přibližně 10 hodin). Měli byste se pohodlně orientovat v:
- Základních konceptech skriptování v Bitcoinu (co dělá validace transakcí)
- Základních konceptech programování (typy, funkce, kompozice)
- Určitá znalost matematické notace je užitečná, ale není nutná. Vše zavádíme postupně

### Klíčové zdroje

- **Původní články**: [„Delving Simplicity"](https://delvingbitcoin.org/u/roconnor-blockstream/summary) od Dr. Russella O'Connora na Delving Bitcoin
- **Repozitář Simplicity**: [BlockstreamResearch/simplicity](https://github.com/BlockstreamResearch/simplicity) — zdrojový kód a formální důkazy v Rocq
- **Oficiální web**: [simplicity-lang.org](https://simplicity-lang.org/) — dokumentace a reference SimplicityHL
- **Blog Blockstream**: [Simplicity on GitHub](https://blog.blockstream.com/en-simplicity-github/) — technický přehled

Připraveni ponořit se do jednoho z nejelegantnějších kousků bitcoinového inženýrství? Jdeme na to!

## Co je Simplicity?

<chapterId>d04f3960-d7fb-44e1-b5a3-25b33d03fd38</chapterId>

Pokud přicházíte do tohoto kurzu bez znalostí jazyka Simplicity, tato kapitola vás zorientuje, než se ponoříme do hloubky.

### Simplicity v kostce

Simplicity je **smart kontraktový jazyk nativní pro Bitcoin**, který je dnes v provozu na síti Liquid. Poprvé jej okolo roku 2012 promyslel Dr. Russell O'Connor a podrobně popsal ve svém článku z roku 2017 *Simplicity: A New Language for Blockchains*; na síti Liquid byl aktivován v červenci 2025 po letech formální verifikace a vývoje.

Na rozdíl od jazyka Solidity od Etherea, což je Turingovsky úplný, vysokoúrovňový kontraktový jazyk, je Simplicity záměrně minimalistický. Má:
- **Tři konstruktory typů** (jednotkový, součtový a součinový)
- **Devět kombinátorů** (základní operace a pravidla kompozice)
- **Žádné smyčky, žádnou rekurzi, žádnou dynamickou paměť**

Jen z těchto primitiv můžete postavit jakýkoli výpočet, který potřebujete pro validaci transakcí, od booleovské logiky až po plné hašování SHA-256.

### Co dnes se Simplicity dokážete?

Simplicity už dnes pohání reálné aplikace na síti Liquid. Nejvýznamnější je [Simplicity DEX](https://docs.simplicity-lang.org/use-cases/simplicity-dex/), tržiště opcí bez orákula, kde uživatelé obchodují kupní opce (call) na L-BTC s využitím USDt jako kolaterálu (základní kontrakt podporuje i prodejní opce – put). Mezi další živé projekty postavené na Simplicity patří [Swaption](https://swaption.io/) od SideSwapu (opce) a open-source [Deadcat](https://github.com/Resolvr-io/deadcat) od Resolvr (predikční trhy). Kromě DeFi umožňuje Simplicity pokročilé podmínky utracení, jako jsou trezory, covenanty a komplexní multisig schémata, která by v Bitcoin Scriptu byla nemožná nebo nebezpečná.

### Čím tento kurz je — a čím není

Toto **není** praktický programovací tutoriál. Programy v jazyce Simplicity zde psát nebudete. Pokud hledáte právě to, podívejte se na:
- [simplicity-lang.org](https://simplicity-lang.org/) — oficiální dokumentace a vysokoúrovňový jazyk SimplicityHL
- [Repozitář Simplicity na GitHubu](https://github.com/BlockstreamResearch/simplicity) — referenční implementace, příklady a důkazy v Rocq
- [Blogový příspěvek Blockstreamu](https://blog.blockstream.com/en-simplicity-github/) o tom, jak začít

Čím tento kurz **je**: jde o **filozofická a technická rozhodnutí** stojící za návrhem jazyka Simplicity. Proč byl tento jazyk vytvořen právě takto? Proč jen devět kombinátorů? Proč žádná rekurze? Proč záleží na tom, že typový systém navazuje na Gentzenův sekventový kalkul?

Berte to jako pochopení toho, **proč byl motor postaven právě takto**, spíše než jako učení se řídit auto.

### Pro koho je určen?

Tento kurz je ideální pro:
- **Vývojáře protokolů**, kteří chtějí porozumět základům jazyka Simplicity ještě předtím, než začnou psát kód
- **Výzkumníky Bitcoinu**, které zajímá formální verifikace a přístup teorie typů
- **Informatiky**, které zajímá souvislost mezi sekventovým kalkulem a blockchainovým výpočtem
- **Pokročilé bitcoinery**, kteří chtějí jít za povrchní pochopení skriptovacích schopností sítě Liquid

Pokud jsou pro vás pojmy jako „součtové typy", „kombinátory" nebo „sekventový kalkul" úplně nové, nebojte se – vše vysvětlíme od nuly. Buďte však připraveni na hutnou, matematickou cestu.

### Od článků ke kurzu

Původní série „Delving Simplicity" od Dr. O'Connora je strukturována jako pět technických článků. Tento kurz tento materiál přeuspořádává a doplňuje poznámkami do postupné vzdělávací cesty s kvízy, které cestou prověřují vaše porozumění. Myšlenky, definice a důkazy jsou jeho; my jsme pouze přizpůsobili formát pro strukturované vzdělávání.

# Základy jazyka Simplicity

<partId>a5976618-94ab-4b29-b9aa-040d35c68e5d</partId>

## Základní způsoby kombinování výpočtů

<chapterId>6d46e77a-7e60-473b-b230-418da5ae44eb</chapterId>

Nyní, když byl Simplicity aktivován na síti Liquid, bych se rád do hloubky ponořil do filozofie a návrhu jazyka Simplicity.

Validace bitcoinových transakcí je výrazně odlišná aplikace než běžný návrh programovacích jazyků. Místo v bloku je drahé, takže programy musí být kompaktní. Programy v bitcoinových transakcích se vždy vykonávají jen na jediném vstupu a každý vykonává program na tomtéž vstupu. Navíc agent, který transakci autorizuje, už dopředu zná výsledek výpočtu: že transakce je platná.

Autorizující agent obvykle spustí mnohem nákladnější výpočty, aby odvodil witness data dosvědčující platnost transakce, zatímco programy běžící na blockchainu musí platnost witness dat pouze ověřit. Ověřování platnosti je často mnohem levnější než platnost dokazovat.

Simplicity jsme navrhli právě s ohledem na tyto jedinečné výzvy návrhu jazyka. Například Simplicity vyžaduje, aby nevykonané větve byly prořezány, takže se na blockchainu vůbec neobjeví. Kroky předzpracování jsou pečlivě navrženy tak, aby vykazovaly (kvazi)lineární časovou složitost vzhledem k velikosti programu v jazyce Simplicity. Namísto „gasu", který nelze spočítat bez vykonání kódu předepsaným způsobem, se používá statická analýza, takže detaily výpočetního modelu se nestanou kritickými pro konsensus. Žádná dynamická alokace paměti během vykonávání. A tak dále.

Než se ponoříme do detailů návrhu jazyka Simplicity, chci tuto sérii začít trochou programovací filozofie o obecných způsobech kombinování základních stavebních bloků za účelem vytvoření nové funkcionality.

### Kompozice

Předpokládejme, že navrhujeme jazyk pro programovatelné transakce pro blockchain, jako je Bitcoin. Konkrétně programy mají přístup pouze k datům transakce a k datům UTXO vstupů a vykonání pouze určuje platnost transakce (což umožňuje výsledek vykonání ukládat do mezipaměti). Řekněme, že začneme s nějakou sadou základních operací, které umí provádět různé úkoly, jako jsou základní výpočty, čtení a/nebo zpracování dat z transakce a ověřování podpisů. Každá operace spotřebuje nějaký typ vstupu (případně prázdný) a vrací nějaký typ výstupu. Jakými způsoby lze tyto základní operace kombinovat do složitějších operací?

### Sekvenční kompozice

![Sekvenční kompozice](assets/en/001.webp)

Nejzákladnější metodou kompozice je sekvenční kompozice. Máme-li dvě základní operace, z nichž typ výstupních dat jedné odpovídá typu vstupních dat druhé, můžeme tyto dvě operace zkombinovat do nové složené operace. Tato nová operace spustí obě základní operace v posloupnosti: jako vstup vezme vstup první operace, výstup této první operace předá na vstup druhé operace a nakonec vrátí výstup této druhé operace.

Samozřejmě se nemusíme omezovat jen na kombinování základních operací. Když už máme nějaké složené operace, můžeme i ty kombinovat pomocí funkcionální kompozice.

V matematice se této sekvenční kompozici často říká jednoduše „kompozice" a člověk by si mohl myslet, že je to jediný způsob, jak věci skládat. My však máme i další způsoby skládání operací.

### Paralelní kompozice

![Paralelní kompozice](assets/en/002.webp)

Předpokládejme, že máme dvě operace – mohou to být základní nebo složené operace – a obě berou stejný typ vstupu. Druhým základním způsobem, jak tyto dvě operace složit, je vykonat je obě na tomtéž vstupu. Tomu se říká paralelní kompozice a typ výstupu je „součinem" typů výstupů původních operací a obsahuje dvojici obou výstupů.

Ačkoli se tomu říká „paralelní" kompozice a obě operace by v principu mohly být vykonány paralelně, paralelní vykonání není provozním požadavkem. Paralelní kompozici můžeme implementovat „sekvenčně" tak, že nejprve vykonáme jednu operaci a poté druhou. Nezáleží nám na detailech toho, jak je paralelní kompozice implementována, pokud je výstup stejný.

### Podmíněná kompozice

![Podmíněná kompozice](assets/en/003.webp)

Podmíněná kompozice je duální k paralelní kompozici. V tomto případě máme dvě operace, které produkují stejný výstup, a skládáme je tak, že si jednu z nich vybereme k vykonání. Vstupem této složené operace je „součet" neboli „označkované sjednocení" (tagged union) typů vstupů původních operací. V tomto případě je značka (tag) „Left" nebo „Right" jediným bitem ve vstupních datech, který určuje, jaký typ dat je nesen, a tedy kterou ze dvou operací lze vykonat.

Podmíněná kompozice funguje stejně i tehdy, když je vstupem součet dvou identických typů. Součtový typ stále obsahuje značku a hodnota této značky určuje, která ze dvou operací se má vykonat.

### Kompozice v Bitcoin Scriptu

Existuje mnoho způsobů, jak tyto tři druhy kompozice realizovat v různých programovacích jazycích. V Bitcoin Scriptu se sekvenční kompozice realizuje (přibližně) zřetězením dvou rutin (proto se Bitcoin Script nazývá konkatenativní programovací jazyk), neboť výstup jedné rutiny zůstává na zásobníku, aby jej spotřebovala následující rutina. Paralelní kompozice se dosahuje použitím operací duplikace a prohození k manipulaci se zásobníkem, aby bylo možné dvě rutiny spustit na tomtéž vstupu. Věci nejsou zcela přímočaré, protože to, čemu říkáme „součin" typů, se obvykle realizuje využitím více položek zásobníku. Snad je celková myšlenka zřejmá.

Podmíněná kompozice se samozřejmě realizuje pomocí `OP_IF`, které větví na základě hodnoty na zásobníku. V tomto případě hraje roli značky vrchní položka zásobníku a obvykle je následující položka nebo položky na zásobníku různých „typů", které závisí na hodnotě značky. V každém případě mohou být typy položek zásobníku vhodné ke zpracování pouze jednou z větví v `OP_IF`. Poté, co však dosáhneme `OP_ENDIF`, musí být položky zásobníku konzistentního „typu", aby zbytek skriptu mohl pokračovat nezávisle na tom, která větev byla předtím zvolena.

### Kompozice v jazyce Simplicity

Simplicity jsme navrhli s kombinátory, které tyto tři formy kompozice implementují přímo. Spolu s několika dalšími kombinátory podporujícími další základní operace související se součinovými a součtovými typy se jádro jazyka Simplicity nakonec skládá z devíti kombinátorů, které postačují k vyjádření libovolného konečného výpočtu. Budeme to podrobněji rozebírat v další kapitole.

### Čtvrtý druh kompozice

Než skončíme, měli bychom zmínit, že v informatice existuje ještě alespoň jeden druh kompozice, kterým je „rekurzivní kompozice". Při rekurzivní kompozici se jedna operace opakuje vícekrát.

Všimněte si, že Bitcoin Script rekurzivní kompozici nepodporuje, a podobně jsme neomezenou rekurzi z návrhu jazyka Simplicity výslovně vyloučili. Naší tezí je, že neomezený iterativní výpočet je lépe implementovat pomocí rekurzivních covenantů, které počítají napříč více transakcemi. To uživatelům umožňuje vyhnout se omezením místa v bloku a standardnosti a lépe předvídat náklady transakcí.

Nicméně existují způsoby, jak zneužít funkci delegace v jazyce Simplicity k poskytnutí něčeho, co připomíná neomezenou rekurzivní kompozici, o čemž možná pojednáme později v této sérii.

### Závěr

Prošli jsme tři hlavní formy kompozice pro přeměnu základních operací na složité operace:

- sekvenční kompozice
- paralelní kompozice
- podmíněná kompozice

Probrali jsme, jak jsou tyto formy kompozice realizovány v Bitcoin Scriptu, a naznačili, jak ovlivnily návrh jazyka Simplicity. Poznamenali jsme, že čtvrtý druh kompozice, rekurzivní kompozice, je z jazyka Simplicity i z Bitcoin Scriptu specificky vyloučen.

V další kapitole popíšeme devět kombinátorů, které tvoří jádro jazyka Simplicity, jak přímo realizují tyto tři formy kompozice a jak z toho vzniká úplný jazyk pro popis libovolného konečného výpočtu.

## Úplnost kombinátorů jazyka Simplicity

<chapterId>2a10a6ba-fada-4556-a673-3ae8c0794bf0</chapterId>

V této kapitole představíme jádro jazyka Simplicity a ukážeme, že tento jazyk je úplný, což znamená, že v něm lze vyjádřit libovolný konečný výpočet.

### Typy v jazyce Simplicity

Simplicity podporuje tři základní konstruktory typů. Součinový typ `A × B` reprezentuje výstupy paralelní kompozice, zatímco součtový typ `A + B` (označkované sjednocení) obsluhuje vstupy podmíněné kompozice. Třetím typem je jednotkový typ.

### Jednotkový typ

Jednotkový typ, značený `𝟙` nebo `ONE`, obsahuje přesně jednu hodnotu: prázdnou n-tici `⟨⟩` nebo `()`. Tento nulabitový datový typ nenese žádnou informaci.

### Součtový typ

Součtový typ `A + B` kombinuje dva typy pomocí značek označujících „left" nebo „right". Hodnoty se zapisují jako `σᴸ(a)` nebo `inl(a)` pro hodnoty označené vlevo a `σᴿ(b)` nebo `inr(b)` pro hodnoty označené vpravo. Značky zůstávají odlišné i při kombinování identických typů.

#### Typ Boolean

Typ `𝟙 + 𝟙`, značený `𝟚` nebo `TWO`, reprezentuje jednobitový typ se dvěma hodnotami. Konvencí je, že `σᴸ⟨⟩` reprezentuje false/nulu, zatímco `σᴿ⟨⟩` reprezentuje true/jedničku.

### Součinový typ

Součinové typy `A × B` obsahují dvojice hodnot zapisované jako `⟨a, b⟩` nebo `(a, b)`. Typ `𝟚 × 𝟚` má čtyři hodnoty, odlišné od čtyř hodnot v `𝟚 + 𝟚`.

### Základní výrazy jazyka Simplicity

Operace se značí jako `f : A ⊢ B`, což znamená vstupní typ `A` a výstupní typ `B`. Simplicity je „prvořádový" jazyk — postrádá funkční typy.

### Dvě základní operace

Jádro jazyka poskytuje dvě základní operace:

**Identita (`iden`).** Operace identity propouští svůj vstup beze změny:

```
iden : A ⊢ A
⟦iden⟧(a) = a
```

**Unit (`unit`).** Operace unit zahodí svůj vstup a vrátí prázdnou n-tici:

```
unit : A ⊢ 𝟙
⟦unit⟧(a) = ⟨⟩
```

Ty tvoří rodiny s jednou operací pro každý typ.

### Tři kompoziční kombinátory

Sekvenční kompozice používá `comp f g` (zapisováno `f ⨾ g` nebo `f >>> g`):

```
If f : A ⊢ B and g : B ⊢ C, then
comp f g : A ⊢ C
⟦f ⨾ g⟧(a) = ⟦g⟧(⟦f⟧(a))
```

Paralelní kompozice používá `pair f g` (zapisováno `f ▵ g` nebo `f &&& g`):

```
If f : A ⊢ B and g : A ⊢ C, then
pair f g : A ⊢ B × C
⟦f ▵ g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩
```

Podmíněná kompozice používá `case f g : (A + B) × C ⊢ D`, čímž větvím poskytuje přístup ke sdílenému prostředí `C`:

```
If f : A × C ⊢ D and g : B × C ⊢ D, then
case f g : (A + B) × C ⊢ D
⟦case f g⟧⟨σᴸ(a), c⟩ = ⟦f⟧⟨a, c⟩
⟦case f g⟧⟨σᴿ(b), c⟩ = ⟦g⟧⟨b, c⟩
```

Proč má podmíněná kompozice právě tento tvar — součet spárovaný se sdíleným prostředím `C` — spíše než jednodušší `copair f g : A + B ⊢ C`, který pouze vybere větev? Protože holý `copair` neumí vyjádřit **distribuci**: funkci `dist : (A + B) × C ⊢ A × C + B × C`, která protlačí sdílený vstup do té větve, jež je zvolena. Zabudováním prostředí `C` přímo do `case` získává Simplicity podmíněnou kompozici *i* distribuci z jediného kombinátoru — jde o jedno z klíčových návrhových rozhodnutí, které udržuje jádro jazyka na pouhých devíti kombinátorech.

### Další čtyři kombinátory

Spotřeba součinu používá `take` a `drop`:

**take** extrahuje levý prvek:

```
If f : A ⊢ C, then
take f : A × B ⊢ C
⟦take f⟧⟨a, b⟩ = ⟦f⟧(a)
```

**drop** extrahuje pravý prvek:

```
If f : B ⊢ C, then
drop f : A × B ⊢ C
⟦drop f⟧⟨a, b⟩ = ⟦f⟧(b)
```

Produkce součtu používá `injl` a `injr`:

**injl** obalí levou značkou:

```
If f : A ⊢ B, then
injl f : A ⊢ B + C
⟦injl f⟧(a) = σᴸ(⟦f⟧(a))
```

**injr** obalí pravou značkou:

```
If f : A ⊢ C, then
injr f : A ⊢ B + C
⟦injr f⟧(a) = σᴿ(⟦f⟧(a))
```

### Devět základních kombinátorů

Celkem má Simplicity přesně devět základních kombinátorů:

| Kombinátor | Účel |
|---|---|
| `iden` | Propustí vstup |
| `unit` | Zahodí vstup |
| `comp` | Sekvenční kompozice |
| `pair` | Paralelní kompozice |
| `case` | Podmíněná kompozice |
| `take` | Extrahuje levou část ze součinu |
| `drop` | Extrahuje pravou část ze součinu |
| `injl` | Vloží do levé části součtu |
| `injr` | Vloží do pravé části součtu |

### Simplicity a sekventový kalkul

Návrh jazyka Simplicity vychází z konjunktivně-disjunktivního fragmentu Gentzenova sekventového kalkulu. Přesněji jde o variantu *funkcionální interpretace* sekventového kalkulu, která je sama analogická Curryho-Howardově korespondenci mezi přirozenou dedukcí a lambda kalkulem. Pravidla kombinátorů vykazují „menší typy v premisách než v závěrech", což umožňuje Bit Machine — abstraktnímu zásobníkovému interpretu jazyka Simplicity — minimalizovat kopírování dat během vykonávání.

### Hodnoty nejsou výrazy

Výrazy v jazyce Simplicity označují operace, nikoli hodnoty. Notace `scribe b : A ⊢ B` reprezentuje jedinečný výraz, který vždy vrací hodnotu `b`, a slouží spíše jako notační pohodlí než jako kombinátor. To odráží Bitcoin Script, kde operace jako `OP_1` hodnoty vkládají na zásobník, místo aby je přímo vyjadřovaly.

### Věta o úplnosti jazyka Simplicity

Když máme v ruce všech devět kombinátorů, jak víme, že nám něco nechybí — že těchto devět opravdu stačí? Na to odpovídá věta o úplnosti jazyka Simplicity: pro libovolnou funkci mezi (konečnými) typy jazyka Simplicity ji označuje nějaký výraz jazyka Simplicity. Důkaz je konstruktivní — ukazuje, jak takový výraz sestavit:

1. **Rozložte vstup**: Pomocí vnořených výrazů `case` úplně rozložte libovolný vstup libovolného typu na jeho jednotlivé bity
2. **Sestavte vyhledávací tabulku**: Pro každý možný vstup použijte `scribe` k vytvoření odpovídajícího výstupu
3. **Sestavte dohromady**: Vnořené výrazy `case` a `scribe` dohromady tvoří obrovskou vyhledávací tabulku, která tuto funkci implementuje

Tato věta je formálně ověřena v důkazovém asistentu Rocq (dříve Coq). Důkaz je součástí oficiálního repozitáře Simplicity a jeho správnost byla strojově ověřena.

Přestože věta o úplnosti zaručuje, že devět kombinátorů jazyka Simplicity dokáže vyjádřit libovolnou funkci mezi (konečnými) typy jazyka Simplicity, výsledné výrazy z konstrukce vyhledávací tabulky jsou neprakticky velké. Funkce nad 256bitovými vstupy by vyžadovala vyhledávací tabulku s 2²⁵⁶ položkami. Proto se další kapitoly zaměřují na budování efektivních výrazů, které využívají strukturu výpočtů, spíše než na řešení všeho hrubou silou přes vyhledávací tabulky.

### Závěr

Jádro jazyka Simplicity zahrnuje typový systém a kombinátory umožňující libovolný konečný výpočet. Přestože věta o úplnosti zaručuje vyjadřovací sílu, výsledné výrazy z generické konstrukce jsou neprakticky velké. Praktický vývoj v jazyce Simplicity zahrnuje využívání výpočetní struktury k dosažení úsporných výrazů. Další kapitoly zkoumají datové struktury, interakce s transakcemi a další kombinátory.

# Od datových typů k programům

<partId>08528a6f-d310-4675-b8cd-4e9b93b3c009</partId>

## Budování datových typů

<chapterId>9981ae62-ae50-4770-adf2-b253d1e08de3</chapterId>

V předchozích kapitolách jsme ukázali, jak základní sada kombinátorů jazyka Simplicity stačí k implementaci libovolného konečného čistého výpočtu. Tato kapitola ukazuje, jak z těchto primitiv budovat praktické datové struktury a výpočty — stejným způsobem, jakým se počítače staví z logických hradel.

### Booleovská logika

Typ Boolean, značený `𝟚`, se rovná `𝟙 + 𝟙` a má dvě hodnoty: `σᴸ⟨⟩` (false) a `σᴿ⟨⟩` (true). Pomocí základních kombinátorů lze zkonstruovat operátory booleovské logiky.

#### Operace and

Logická operace `and : 𝟚 × 𝟚 ⊢ 𝟚` bere dva bity a vrací jeden bit. Implementace větví podle prvního bitu: je-li false, vrátí false; jinak vrátí druhý bit.

```
and ≔ case (injl unit) (drop iden) : 𝟚 × 𝟚 ⊢ 𝟚
```

Test s `⟨false, false⟩`:

```
⟦and⟧⟨false, false⟩
 = {expand the notation for false}
⟦and⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {expand the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {evaluate case for σᴸ}
⟦injl unit⟧⟨⟨⟩, σᴸ⟨⟩⟩
 = {evaluate injl}
σᴸ(⟦unit⟧⟨⟨⟩, σᴸ⟨⟩⟩)
 = {evaluate unit}
σᴸ⟨⟩
 = {by the notation for false}
false
```

Test s `⟨true, true⟩`:

```
⟦and⟧⟨true, true⟩
 = {expand the notation for true and the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴿ⟨⟩, σᴿ⟨⟩⟩
 = {evaluate case for σᴿ}
⟦drop iden⟧⟨⟨⟩, σᴿ⟨⟩⟩
 = {evaluate drop}
⟦iden⟧(σᴿ⟨⟩)
 = {evaluate iden}
σᴿ⟨⟩
 = {by the notation for true}
true
```

#### Další logické operace

Operace `not` vyžaduje pomocný kombinátor:

```
                   f : A ⊢ C    g : B ⊢ C
--------------------------------------------------------------
copair f g ≔ iden ▵ unit ⨾ case (take f) (take g) : A + B ⊢ C
```

Úvodní `iden ▵ unit : A ⊢ A × 𝟙` přidá ke vstupu prázdné „prostředí", což umožňuje použití kombinátoru `case`. Použití `take` ve dvou větvích toto prázdné prostředí zahodí a vykoná `f` nebo `g`.

Další booleovské logické operace:

- `or ≔ case (drop iden) (injr unit) : 𝟚 × 𝟚 ⊢ 𝟚`
- `not ≔ copair (injr unit) (injl unit) : 𝟚 ⊢ 𝟚`
- `xor ≔ case (drop iden) (drop not) : 𝟚 × 𝟚 ⊢ 𝟚`

### Bitové sčítačky

„half-adder" (poloviční sčítačka) bere dva bity a sečte je, čímž vytvoří dvoubitový výstup: bit přenosu a bit součtu.

```
half-adder ≔ and ▵ xor : 𝟚 × 𝟚 ⊢ 𝟚 × 𝟚
```

„full-adder" (úplná sčítačka) sečte tři bity a vytvoří dvoubitový výstup. Vstup používá vnořenou n-tici `(𝟚 × 𝟚) × 𝟚`.

Pro vnořené n-tice se používá kompaktní notace:

- `O f` značí `take f`
- `I f` značí `drop f`
- `H` značí `iden`

Například `I O H` znamená `drop (take iden) : A × (B × C) ⊢ B`, tedy extrakci prostřední hodnoty. Notace evokuje binární číslice: uvažujeme-li vnořené n-tice jako binární stromy, notace představuje obrácené binární číslice pozic ve stromě. Tyto výrazy tvoří De Bruijnovy indexy pro Simplicity.

**Poznámka:** Notace `I`, `O` a `H` platí pouze pro podvýrazy sestávající výhradně z `take`, `drop` a `iden`.

„full-adder" skládá dvě „half-adder" a bere logické `or` bitů přenosu:

```
full-adder ≔ take half-adder ▵ I H
           ⨾ O O H ▵ (O I H ▵ I H ⨾ half-adder)
           ⨾ (O H ▵ I O H ⨾ or) ▵ I I H
           : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × 𝟚
```

Na prvním řádku `take half-adder ▵ I H : (𝟚 × 𝟚) × 𝟚 ⊢ (𝟚 × 𝟚) × 𝟚` spustí „half-adder" na první dva bity a poslední bit uloží.

Na druhém řádku `O O H ▵ (O I H ▵ I H ⨾ half-adder) : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × (𝟚 × 𝟚)` uloží první bit (přenos z první „half-adder") a spustí „half-adder" na poslední dva bity.

Na posledním řádku `(O H ▵ I O H ⨾ or) ▵ I I H: 𝟚 × (𝟚 × 𝟚) ⊢ 𝟚 × 𝟚` vezme logické OR prvních dvou bitů (přenosů z obou „half-adder") a vrátí výstupní bit součtu druhé „half-adder".

To demonstruje programování v jazyce Simplicity: použití notace `I`, `O` a `H` k odkazování na datové bity a vytváření vhodných „prostředí" pro volání dalších funkcí prostřednictvím sekvenční kompozice.

Uživatelé nízkoúrovňové operace nedefinují přímo. Později v této sérii probereme jety standardní knihovny, které implementují běžné funkce. Od koncových uživatelů se neočekává, že budou programovat přímo v jazyce Simplicity, podobně jako u Bitcoin Scriptu. Namísto toho vyšší úrovně jazyků, jako je SimplicityHL, generují kód jazyka Simplicity, spravují „prostředí" podvýrazů a překládají pojmenované proměnné na příslušné posloupnosti `take` a `drop`.

### Vektory

Vektory pevné délky se definují vytvářením iterovaných součinů typu `A`:

- `A² ≔ A × A`
- `A⁴ ≔ A² × A²`
- `A⁸ ≔ A⁴ × A⁴`
- `…`

Ty lze zapsat jako `A^2`, `A^4`, `A^8` atd.

Vektory jsou definovány pouze pro délky, které jsou mocninami dvou. Ostatní mocniny vyžadují zvolení konvencí uzávorkování.

Máme-li výraz `f : A ⊢ B`, opakované párování jej „namapuje" přes vektory pevné délky:

- `f² ≔ f ▵ f : A² ⊢ B²`
- `f⁴ ≔ f² ▵ f² : A⁴ ⊢ B⁴`
- `f⁸ ≔ f⁴ ▵ f⁴ : A⁸ ⊢ B⁸`

Máme-li funkci `f : A × B ⊢ B`, iterace neboli „skládání" (folding) přes vektory pevné délky:

- `fold-right-2 f ≔ O O H ▵ (O I H ▵ I H ⨾ f) ⨾ f : A² × B ⊢ B`
- `fold-right-4 f ≔ fold-right-2 (fold-right-2 f) : A⁴ × B ⊢ B`
- `fold-right-8 f ≔ fold-right-2 (fold-right-4 f) : A⁸ × B ⊢ B`

Existuje mnoho variant. Máme-li `f : A × B ⊢ C`, provedeme „zip" přes spárované vektory pomocí `zip-n f : (Aⁿ × Bⁿ) ⊢ Cⁿ`. Máme-li `f : (A × B) × C ⊢ C`, skládáme přes spárované vektory pomocí `bifold-right-n f : (Aⁿ × Bⁿ) ⊢ C`. Kombinací `map` a `fold-right` vznikají akumulující kombinátory: `f : A × C ⊢ C × B` dává `map-accum-right-n f : Aⁿ × C ⊢ C × Bⁿ`. Možných je mnohem více variant.

#### Vícebitová slova

Bitový vektor dává vícebitová celá čísla. Například `𝟚³²` je typ 32bitového slova. `𝟚²⁵⁶` je typ 256bitového slova, vhodný pro haše a kryptografické operace.

Pomocí „full-adder" definuje varianta vektorových operací „ripple carry adder" (sčítačku s postupným přenosem) nad vícebitovými slovy:

```
full-adder-n ≔ zip-accum-right-n full-adder : (𝟚ⁿ × 𝟚ⁿ) × 𝟚 ⊢ 𝟚 × 𝟚ⁿ
```

`full-adder-n` bere dvě n-bitová binární čísla a jednobitový vstupní přenos a vrací jednobitový příznak výstupního přenosu a n-bitový součet.

#### SHA-256

Rekurzivním definováním aritmetických operací nad vícebitovými slovy — odčítání, násobení, dělení — a bitových logických operací, jako je logické AND, OR, XOR, a jejich opakovaným kombinováním lze sestavit i blokovou kompresní funkci SHA-256:

```
sha256-hash-block ≔ … : 𝟚²⁵⁶ × 𝟚⁵¹² ⊢ 𝟚²⁵⁶
```

Komprese SHA-256 je formálně definována pomocí jazyka Simplicity v důkazovém asistentu Rocq (dříve Coq), spolu s formálním důkazem, že implementace `sha256-hash-block` je správná.

Jako čistý Simplicity běží komprese příliš pomalu. Jety vykonávají běžné funkce, jako je komprese SHA-256, nativně. Čisté implementace v jazyce Simplicity slouží jako formální specifikace pro jety.

### Typy Option

Typy Option vznikají vytvořením součtu s jednotkovým typem:

```
Option A ≔ 𝟙 + A
```

Typ `Option A` lze zapsat jako `A?` nebo `𝕊 A` (kde `𝕊` znamená „následník"). Funkce lze mapovat přes typy Option:

```
                 f : A ⊢ B
------------------------------------------
f? ≔ copair (injl unit) (injr f) : A? ⊢ B?
```

Lze definovat monadické kombinátory, jako je bind:

```
              f : A ⊢ B?
---------------------------------------
bind f ≔ copair (injl unit) f : A? ⊢ B?
```

### Buffery proměnné délky

„Buffery" jsou typy pro částečně naplněné vektory:

- `Aᑉ² ≔ A?`
- `Aᑉ⁴ ≔ A²? × Aᑉ²`
- `Aᑉ⁸ ≔ A⁴? × Aᑉ⁴`
- `…`

Typ `Xᑉ⁸` se rozvine na `(1 + X⁴) × ((1 + X²) × (1 + X))`. Budeme-li s tím zacházet jako s polynomem a rozvineme jej, dostaneme `1 + X + X² + X³ + X⁴ + X⁵ + X⁶ + X⁷`. Interpretujeme-li to jako typ, reprezentuje to součet všech možných n-tic X až do 7, včetně prázdné n-tice. To je přesně typ seznamů s délkou striktně menší než 8.

Stejně jako u vektorů lze nad buffery definovat operace mapování a skládání. Mezi zásobníkové operace patří `push-<n : Aᑉⁿ × A ⊢ Aⁿ + Aᑉⁿ` a `pop-<n : Aᑉⁿ ⊢ (Aᑉⁿ × A)?`. `push-<n` přidá položku do bufferu a vrátí plný vektor, dojde-li k přetečení. `pop-<n` položku odebere a vrátí menší buffer a odebranou položku, případně nevrátí nic, byl-li původní buffer prázdný.

Definice `push-<n`, rekurzivně:

```
push-<2 ≔ case (drop (injr (injr iden))) (injl iden)

push-<4 ≔ ((O I H ▵ IH) ⨾ push-<2) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ injl unit)) (injl iden))
               (injr (I H ▵ O H))

push-<8 ≔ ((O I H ▵ IH) ⨾ push-<4) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ (injl unit ▵ injl unit))) (injl iden))
               (injr (I H ▵ O H))

…
```

Čistý Simplicity se za určitou úrovní složitosti obtížně sleduje. Koncoví uživatelé využívají vyšší úrovně jazyků, jako je SimplicityHL, které tyto idiomatické výrazy generují.

### Závěr

Tato kapitola ukázala, jak z bitů budovat logické operace. Z nich vzešla aritmetika na úrovni bitů, umožňující uvažovat o vykonávání. Vyvinuli jsme vektorové typy a předvedli iteraci přes vícebitová slova pro definici aritmetiky. Dále lze pouze pomocí kombinátorů jazyka Simplicity definovat kryptografické operace, jako je SHA-256 a validace Schnorrových podpisů — vše je skutečně definováno pomocí jazyka Simplicity.

Tato kapitola není vyčerpávajícím průvodcem všemi možnými datovými typy a operacemi, které lze v jazyce Simplicity postavit, ale ilustruje dosažení praktické funkcionality v rámci omezení jazyka Simplicity. Navzdory konečně omezeným typům lze definovat užitečné vektory, typy bufferů a operace iterující přes tyto struktury.

Skutečné specifikace operací standardní knihovny se od zdejších definic mírně liší. Například „full-adder" používá spíše trojcestný XOR a logickou funkci „většiny" (majority) než dvě „half-adder".

V praxi programy v jazyce Simplicity používají pro aritmetické a kryptografické operace jety. Jety však pouze nahrazují výrazy. Kombinátory iterující přes buffery a vektory nelze jety nahradit a objevují se ve skutečných programech jazyka Simplicity. Namísto jejich přímého použití však koncoví uživatelé využívají vyšší úrovně jazyků, jako je SimplicityHL, které takové výrazy generují.

Zdá se, že rekurzivně definované kombinátory rostou ve velikosti výrazu exponenciálně. To není problém. Během serializace se výrazy kódují jako DAGy (orientované acyklické grafy) místo stromů. Skutečná reprezentace roste pouze lineárně.

Zatím jsme uvažovali pouze čisté výpočty. Interakce s daty transakce pro úkoly, jako je podepisování transakcí, vyžaduje nějaký způsob, jak mohou programy selhat, jsou-li podpisy neplatné. Další kapitola pojednává o vedlejších efektech v jazyce Simplicity.

## Dva vedlejší efekty

<chapterId>9eafe498-0765-419a-a69d-a74a9cdf3713</chapterId>

V předchozích kapitolách jsme ukázali, jak pomocí základní sady kombinátorů jazyka Simplicity budovat některé datové struktury a výpočty. Jak jsme poznamenali, základní kombinátory stačí k implementaci libovolného konečného čistého výpočtu. To vyvolává otázku: čeho víc lze dosáhnout? Do našich výrazů můžeme přidat další vedlejší efekty.

Pro výrazy existují různé druhy možných vedlejších efektů: aktualizace stavu, zápis do logu, vyhození výjimky, čtení z prostředí, volání pokračování atd. Vedlejší efekty dostupné v jazyce Simplicity budou záviset na aplikaci.

Pro aplikace Bitcoinu a Liquidu máme v současnosti dva vedlejší efekty: efekt Failure, což je efekt výjimky, kde výjimka má typ `𝟙`, a efekt Reader, který umožňuje přístup k datům z prostředí transakce. Naše základní kombinátory jsou „čisté"; nemají žádné vedlejší efekty. Jety však mohou zavést nová primitiva, která vedlejší efekty mají.

### Jety s efekty

O jetech budeme mluvit více později v tomto kurzu, ale zde představíme několik ukázkových jetů pro ilustraci jejich vedlejších efektů.

#### Bip0340-verify

`bip0340-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚⁵¹² ⊢ 𝟙` je jet pro výraz, který bere x-only veřejný klíč, 256bitovou zprávu a Schnorrův podpis a nevrací nic! Podle svého typu by se měl chovat stejně jako `unit`. Rozdíl spočívá ve vedlejším efektu jetu: pokud validace podpisu selže, celý výpočet se přeruší vyhozením výjimky (typu unit). To je efekt Failure.

#### Verify

`verify : 𝟚 ⊢ 𝟙` je nejjednodušší jet pro vyjádření efektu Failure. Je-li vstupem `verify` `false`, celý výpočet se přeruší vyhozením výjimky. Je-li vstupem `true`, nevrátí se nic, ale výpočet může pokračovat.

#### Haše transakcí

`sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` se zdá být konstantní funkcí, neboť existuje jen jedna možná vstupní hodnota: prázdná n-tice. Tento jet však čte z prostředí transakce a vytváří haš dat transakce, který je analogický otisku zprávy `SIGHASH_ALL` používanému při ověřování podpisů v Bitcoin Scriptu. To je příklad efektu Reader: vrácená hodnota závisí na prostředí transakce, ve kterém je jet vykonán. Existuje několik dalších hašovacích jetů, které hašují různé podmnožiny dat prostředí transakce a pomáhají tak sestavovat vlastní otisky zpráv pro podpisy.

#### Introspekční jety

`input-sequence : 𝟚³² ⊢ 𝟚³²?` je funkce, která bere index vstupu a vrací sekvenční číslo transakce pro daný vstup, případně nevrátí nic, je-li index mimo rozsah. Výstupní hodnota opět není čistou funkcí indexu vstupu, ale operace používá efekt Reader k přístupu k prostředí transakce, aby výstupní hodnotu určila. Existuje několik dalších introspekčních jetů, které vracejí různé fragmenty dat prostředí transakce.

### Klasifikace efektů

Ne všechny vedlejší efekty jsou si rovny. Některé vedlejší efekty se chovají lépe než jiné. Efekty můžeme klasifikovat podle toho, jak dobře se hodí k transformacím programů.

#### Komutativní efekty

Komutativní efekt je takový, kde platí, že prohodíte-li výstupy dvou výrazů, můžete bezpečně prohodit i samotné výrazy, aniž byste změnili efekt výrazu. Uvažte `swap = I H ▵ O H : A × B ⊢ B × A`. Platí-li `f ▵ g ⨾ swap = g ▵ f` pro každou dvojici výrazů `f` a `g` s vedlejšími efekty, pak jsou efekty komutativní.

Čtení dat transakce z prostředí je komutativní efekt, protože výsledek čtení z prostředí je stejný bez ohledu na to, v jakém pořadí čtení vykonáváme.

Obecně vyhození výjimky není komutativní efekt. Vyhodí-li `f` nějakou výjimku `e₁` a `g` nějakou jinou výjimku `e₂`, pak to, která výjimka je z dvojice `f` a `g` vyhozena, závisí na pořadí, v jakém jsou vykonány.

Ve zvláštním případě efektu Failure, v němž lze vyhodit pouze výjimku typu unit, je však efekt komutativní. Ať už výjimku vyhodí `f`, nebo `g`, výsledná výjimka bude stejná, protože existuje jen jedna možná hodnota výjimky.

#### Idempotentní efekty

Idempotentní efekt je takový, kde platí, že zduplikujete-li výstup výrazu, můžete bezpečně zduplikovat i samotný výraz, aniž byste změnili efekt výrazu. Uvažte `dup = iden ▵ iden : A ⊢ A × A`. Platí-li `f ⨾ dup = dup ⨾ f ▵ f` pro každý výraz `f` s vedlejšími efekty, pak jsou efekty idempotentní.

Čtení dat transakce z prostředí je idempotentní efekt. Vyhození výjimky je také idempotentní efekt. I když bude vykonán jen jeden ze dvou zduplikovaných výrazů, jakákoli výjimka vyhozená výrazem `dup ⨾ f ▵ f` bude stejná jako výjimka vyhozená výrazem `f ⨾ dup`.

Zápis do logu však nemusí být idempotentní, neboť zduplikování efektu by způsobilo, že se zpráva v logu objeví dvakrát. Pokud však log sestává z _množiny_ zpráv místo ze _seznamu_ zpráv, pak by efekt byl idempotentní (a komutativní), protože vložení do množiny je samo o sobě idempotentní operace.

#### Unitární efekty

Unitární efekt je takový, kde platí, že zahodíte-li výstup výrazu, můžete bezpečně zahodit i samotný výraz, aniž byste změnili efekty výrazu. Platí-li vždy `f ⨾ unit = unit` pro každý výraz `f` s vedlejšími efekty, pak jsou vaše efekty unitární.

Čtení dat z prostředí je jedním z mála druhů unitárních efektů. Je-li výsledek čtení dat transakce z prostředí zahozen, lze zahodit celý výraz, který čtení provádí.

Efekt Failure unitární není. Vyhodí-li `f` výjimku, vyhodí ji i `f ⨾ unit`; vykonávání se ke kombinátoru `unit` ani nedostane, než se výpočet přeruší. Na druhou stranu `unit` by zjevně žádnou výjimku nevyhodil, takže efekty `f ⨾ unit` a `unit` by se lišily.

Pro shrnutí uvádíme, jak výše probírané efekty obstojí vůči těmto třem vlastnostem:

| Efekt | Komutativní | Idempotentní | Unitární |
| --- | :---: | :---: | :---: |
| Reader (prostředí transakce) | ✓ | ✓ | ✓ |
| Failure (výjimka typu unit) | ✓ | ✓ | ✗ |
| Writer (log jako množina) | ✓ | ✓ | ✗ |
| Obecné výjimky (libovolný typ) | ✗ | ✓ | ✗ |

### Efekty povolené v jazyce Simplicity

Čím více „dobře se chovajících" vlastností daný druh efektu má, tím více prostoru má optimalizátor jazyka Simplicity pro transformaci programů, které tyto efekty používají. V ideálním případě bychom povolili pouze efekty, které mají všechny tři vlastnosti: komutativní, idempotentní a unitární. To by optimalizátoru umožnilo provést jakoukoli transformaci programu, kterou by chtěl. Čtení z prostředí je však jediný efekt, který splňuje všechny tři vlastnosti.

Namísto toho požadujeme, aby efekty jazyka Simplicity byly komutativní a idempotentní. Oba efekty, které v jazyce Simplicity používáme, efekt Failure i efekt Reader, jsou komutativní a idempotentní. To umožňuje provádět na kódu jazyka Simplicity širokou třídu optimalizací.

Výše popsaná transformace „zahození", která se pokouší nahradit `f ⨾ unit` výrazem `unit`, ani žádná podobná transformace však není povolena, může-li `f` vyprodukovat efekt Failure. Představte si totiž, že by `f` obsahoval aserci `bip0340-verify`. Pokoušet se tuto kontrolu optimalizací odstranit by bylo katastrofální.

### Proč vůbec povolovat vedlejší efekty?

Proč Simplicity vůbec vedlejší efekty povoluje? Nebylo by lepší, kdyby každý program bral jako vstup celou transakci a vracel booleovský výstup, který rozhoduje, zda je transakce platná, nebo ne?

#### Dávkové ověřování

Jedním z důvodů, proč máme efekt Failure, je podpora [dávkového ověřování](https://github.com/bitcoin/bips/blob/c9a6ca6297eb8de850f6b64dafb8e60ee9b64d66/bip-0340.mediawiki#batch-verification) Schnorrových podpisů. Při dávkovém ověřování se mnoho jednotlivých kontrol Schnorrových podpisů sdruží dohromady tak, že selže-li kontrola jakéhokoli jednoho podpisu, selže celá dávka.

Tento dávkový postup zlepšuje efektivitu oproti individuálnímu ověřování každého podpisu. Nevýhodou je, že selže-li dávkové ověření, nedozvíme se, která konkrétní kontrola nebo kontroly podpisu selhaly.

Použitím vedlejšího efektu Failure zajišťuje `bip0340-verify`, že selže-li kontrola podpisu, selže celá transakce. Pokud by `bip0340-verify` místo toho vracel `𝟚`, booleovský typ, pro úspěch nebo selhání, pak by neúspěšná kontrola podpisu stále mohla vést k větvi, kde skript uspěje. V takovém případě bychom potřebovali vědět, zda je konkrétní podpis platný, nebo ne, a nemohli bychom tak využít výhod dávkového ověřování.

#### Předpočítaná data transakce

Problémem raného Bitcoin Scriptu bylo, že hašovací funkce používaná k vytváření otisků zpráv pro podpisy byla lineární vzhledem k velikosti transakce. Obvykle každý vstup vytváří alespoň jeden otisk zprávy pro ověření podpisu, takže celkové množství hašování bylo kvadratické vzhledem k velikosti transakce.

Tento problém byl vyřešen v SegWitu a pozdějších iteracích Bitcoin Scriptu předefinováním otisků zpráv tak, aby je bylo možné počítat v konstantním čase na jednu kontrolu podpisu. To se opírá o `PrecomputedTransactionData`, která jednou předpočítá haše dat transakce a poté je sdílí mezi výpočty sighash jednotlivých vstupů. Hašovací jety transakcí v jazyce Simplicity se opírají o stejný druh předpočítaných dat transakce, aby zajistily, že jety běží v konstantním čase.

Předpokládejme, že by `sig-all-hash` efekt Reader nepoužíval. Předpokládejme, že bychom nějak dokázali sestavit typ jazyka Simplicity pro prostředí transakce. Nazvěme jej `TxEnv`, takže typem jetu by bylo `sig-all-hash : TxEnv ⊢ 𝟚²⁵⁶`. Taková definice by vyžadovala, aby jet `sig-all-hash` uměl spočítat haš libovolné transakce, nejen té, které se týká. Programy jazyka Simplicity by mohly daný `TxEnv` zkopírovat a předat jetu `sig-all-hash` jeho upravenou kopii. V takovém případě by se `sig-all-hash` nemohl opírat o `PrecomputedTransactionData` a byli bychom zpět u požadavku na lineární čas vzhledem k jakýmkoli datům transakce předaným do této verze `sig-all-hash`.

Protože `sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` k přístupu k datům transakce používá efekt Reader, získává přístup _pouze_ k pevnému prostředí transakce. Z toho důvodu může implementace jetu bezpečně použít `PrecomputedTransactionData` a fungovat v konstantním čase.

### Agregace podpisů napříč vstupy

Ačkoli ani Liquid, ani Bitcoin v současnosti [agregaci podpisů napříč vstupy](https://hrf.org/latest/cisa-research-paper/) nepodporují, rádi bychom si ověřili, že Simplicity s ní může být kompatibilní, až přijde čas.

Ačkoli detaily ještě nebyly dopracovány, představujeme si, že poloviční agregace by byla implementována pomocí efektu Writer. Tedy nový jet s typem jako `half-agg-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚²⁵⁶ ⊢ 𝟙` by bral veřejný klíč, otisk zprávy a `r`-komponentu Schnorrova podpisu (Schnorrův podpis sestává z `r`-komponenty a `s`-komponenty) a zapsal by je do logu transakce, než by pokračoval ve vykonávání. Poté by jinde v transakci nebo spolu s transakcí byla poskytnuta agregovaná `s`-komponenta pro všechny napůl agregované Schnorrovy podpisy. Transakce by byla platná pouze tehdy, když je taková agregovaná `s`-komponenta poskytnuta pro všechny zalogované klíče, zprávy a `r`-komponenty.

Aby vyhověl požadavkům jazyka Simplicity, musí být tento efekt Writer idempotentní a komutativní. To lze zajistit tím, že budeme s logem writeru zacházet jako s množinou n-tic klíč, zpráva, `r`-komponenta. Funguje to, protože množinové operace jsou idempotentní a komutativní. Zacházení s logem jako s množinou hodnot by bylo kompatibilní s ověřovacím algoritmem poloviční agregace.

### Závěr

V této kapitole jsme se zabývali přidáváním vedlejších efektů k výpočtům, které Simplicity umí. Klasifikovali jsme různé druhy efektů podle toho, jak dobře se chovají vzhledem k různým druhům transformace programů. Rozhodli jsme se omezit efekty jazyka Simplicity na ty, které jsou komutativní a idempotentní.

Dva efekty, které používáme pro aplikace Bitcoinu a Liquidu, jsou efekt Reader pro přístup k prostředí transakce a efekt Failure pro přerušení a selhání programu. Některé jety využívají primitivní operace, u nichž se tyto druhy vedlejších efektů mohou vyskytnout.

Efekt Failure určuje výstup programu jazyka Simplicity: program buď selže, čímž transakci zneplatní, nebo uspěje. Efekt Reader poskytuje programu jazyka Simplicity jeden druh vstupu: prostředí obsahující data transakce. Musíme však programům jazyka Simplicity poskytovat i další vstupy, jako jsou digitální podpisy.

V další kapitole se podíváme na to, co programy jazyka Simplicity jsou, jak se z nich stávají adresy a jak k programům jazyka Simplicity přidáváme další vstupy, jako jsou podpisy.

## Programy a adresy

<chapterId>961652e3-8f7d-4c2a-8b55-9a990b91a0dd</chapterId>

V předchozí kapitole jsme popsali dva vedlejší efekty používané v jazyce Simplicity: efekt Failure, který určuje úspěch nebo selhání programu, a efekt Reader, který poskytuje přístup k prostředí transakce. Nyní se obrátíme k praktické otázce: co přesně je program jazyka Simplicity a jak se z něj stává adresa na blockchainu?

### Programy jazyka Simplicity

Program jazyka Simplicity je definován jako výraz jazyka Simplicity typu `𝟙 ⊢ 𝟙`. Tato typová signatura znamená, že program nebere žádný smysluplný vstup (pouze hodnotu unit) a neprodukuje žádný smysluplný výstup (pouze hodnotu unit). Efekt Reader zachycuje vstup prostředí transakce, zatímco efekt Failure indikuje úspěch nebo selhání. Vstup/výstup obstarávají tyto efekty, nikoli samotné typy jazyka Simplicity.

### Commitment Merkle Root

Namísto ukládání kompletních programů on-chain používá Bitcoin závazky (commitments) — praxi navazující na Pay-to-Script-Hash (P2SH). Simplicity používá Commitment Merkle Root (CMR).

Každý kombinátor obdrží SHA-256 značku odvozenou ze vzoru: `Simplicity␟Commitment␟[identifier]`, kde `␟` představuje ASCII kód 31 (oddělovač jednotek, unit separator).

Každá značka je SHA-256 haš odpovídajícího řetězce předobrazu (pre-image) uvedeného níže:

| Kombinátor | Předobraz značky (ASCII řetězec) |
|---|---|
| `iden` | `Simplicity␟Commitment␟iden` |
| `unit` | `Simplicity␟Commitment␟unit` |
| `comp` | `Simplicity␟Commitment␟comp` |
| `pair` | `Simplicity␟Commitment␟pair` |
| `case` | `Simplicity␟Commitment␟case` |
| `take` | `Simplicity␟Commitment␟take` |
| `drop` | `Simplicity␟Commitment␟drop` |
| `injl` | `Simplicity␟Commitment␟injl` |
| `injr` | `Simplicity␟Commitment␟injr` |

Výraz jazyka Simplicity se pak rekurzivně zahašuje do 256bitového CMR výpočtem označkovaného SHA-256 midstate pro každý kombinátor spolu s CMR jeho argumentů (píšeme `#ᶜ(e)` pro CMR výrazu `e` a `∥` pro zřetězení bajtů):

| Kombinátor | Pravidlo CMR |
|---|---|
| `iden` | `#ᶜ(iden) = SHA-256-midstate(tag_iden ∥ tag_iden)` |
| `unit` | `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)` |
| `comp f g` | `#ᶜ(comp f g) = SHA-256-midstate(tag_comp ∥ tag_comp ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `pair f g` | `#ᶜ(pair f g) = SHA-256-midstate(tag_pair ∥ tag_pair ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `case f g` | `#ᶜ(case f g) = SHA-256-midstate(tag_case ∥ tag_case ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `take f` | `#ᶜ(take f) = SHA-256-midstate(tag_take ∥ tag_take ∥ 32·0x00 ∥ #ᶜ(f))` |
| `drop f` | `#ᶜ(drop f) = SHA-256-midstate(tag_drop ∥ tag_drop ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injl f` | `#ᶜ(injl f) = SHA-256-midstate(tag_injl ∥ tag_injl ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injr f` | `#ᶜ(injr f) = SHA-256-midstate(tag_injr ∥ tag_injr ∥ 32·0x00 ∥ #ᶜ(f))` |

Binární kombinátory (`comp`, `pair`, `case`) zřetězují CMR obou potomků; unární kombinátory (`take`, `drop`, `injl`, `injr`) zřetězují CMR svého jediného potomka po 32 bajtech výplně `0x00`; a nulární listy (`iden`, `unit`) hašují pouze svou značku. Dvě konvence udržují tento výpočet levný: používají se SHA-256 midstates, takže **každý výraz vyžaduje nejvýše jedno volání kompresní funkce SHA-256** (za předpokladu, že midstate až po konstantní značky je předpočítán), a jednoargumentové konstruktory předsazují svému argumentu 32 bajtů výplně `0x00`, což umožňuje trochu předpočítání navíc pro implementace, které o něj stojí.

Pro kombinátor `unit` — nulární konstruktor bez argumentových podvýrazů — se toto pravidlo specializuje na `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)`, kde `tag_unit = SHA-256(Simplicity␟Commitment␟unit)` (značka se vloží dvakrát). Výsledný CMR pro triviální program `unit` je:

```
0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

Zásadní je, že CMR se nezavazuje k typům výrazů jazyka Simplicity, ale spoléhá na odvození typů (type inference) během uplatnění.

### Adresy

Adresy využívají mechanismus Taproot z BIP-0341 s CMR commitovanými pod verzí TapLeaf `0xbe`. Proces zahrnuje:

1. Výpočet označkovaného hashe TapLeaf kombinujícího bajt verze, délku CMR a samotný CMR
2. Vyladění (tweak) interního veřejného klíče (s použitím bodu NUMS, když není žádoucí cesta klíče)
3. Převod do formátu bech32m
4. Přidání příslušných kontrolních součtů

Když není žádoucí žádná cesta klíče, interní veřejný klíč se nastaví na bod **NUMS** („Nothing-Up-My-Sleeve"): bod na křivce záměrně zvolený tak, aby nikdo neznal jeho diskrétní logaritmus — jinými slovy bod bez odpovídajícího privátního klíče. Protože pro něj nikdo nikdy nedokáže vytvořit podpis, je cesta klíče prokazatelně nepoužitelná a výstup lze utratit *pouze* prostřednictvím commitované skriptové cesty jazyka Simplicity. Ve skutečné aplikaci by měl být tento bod NUMS randomizován, jak doporučuje BIP-0341, aby výstupy bez cesty klíče byly nerozlišitelné od běžných Taproot výstupů (přínos pro soukromí).

#### Od Simplicity k adrese

Projděme si celé odvození pro nejjednodušší možný program: `unit : 𝟙 ⊢ 𝟙`, prázdnou operaci, která vždy uspěje.

**1. Značka kombinátoru.** Nejprve spočítáme značku `unit`:

```
tag_unit = SHA-256(Simplicity␟Commitment␟unit)
         = 0xd723083cff3c75e29f296707ecf2750338f100591c86e0c71717f807ff3cf69d
```

**2. CMR.** Vložíme značku dvakrát, abychom získali CMR programu:

```
CMR = #ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)
    = 0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

**3. Hash TapLeaf.** Před CMR předsadíme verzi TapLeaf jazyka Simplicity `0xbe` a délku CMR `0x20` (32 bajtů) a poté vezmeme označkovaný hash TapLeaf pro Elements (označkovaný hash je `hash_str(x) = SHA-256(SHA-256(str) ∥ SHA-256(str) ∥ x)`):

```
hash_TapLeaf/elements(0xbe ∥ 0x20 ∥ CMR)
  = 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c
```

S jediným tímto listem neexistují žádné TapBranche, takže tento hash je již kořenem TapTree.

**4. TapTweak.** Protože nechceme žádnou cestu klíče, použijeme jako interní klíč bod NUMS z BIP-0341 a vyladíme (tweak) jej kořenem TapTree:

```
internal_pk = 0x50929b74c1a04954b78b4b6035e97a5e078a5a0f28ec96d547bfee9ace803ac0
t = hash_TapTweak/elements(internal_pk ∥ 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c)
  = 0xb3bef172389b0937d7e5a8b15cfa41e776777f13f2f659cb06220a6ff0658285
```

**5. Výstupní klíč.** Vyladíme interní klíč na křivce, `output_pk = lift_x(internal_pk) ⊕ t·G` (aritmetika eliptické křivky je zde shrnuta), čímž získáme x-only výstupní klíč `0x2cb0c20acd7340b4d4b65f6a60e2888d0d64e3267261f3b3cf7290e5af3f9e09`.

**6. Adresa Bech32m.** Zakódujeme x-only výstupní klíč, předsadíme `p` (znak verze witness pro SegWit v1), přidáme lidsky čitelný prefix Liquid-testnetu `tex1` a připojíme kontrolní součet Bech32m. Konečná adresa je:

```
tex1p9jcvyzkdwdqtf49kta4xpc5g35xkfcexwfsl8v70w2gwttelncyshxjk56
```

To byla spousta práce — ale velkou část z ní vyžaduje samotný Taproot, nikoli Simplicity.

### Witness výrazy

Nový druh kombinátoru řeší absenci vstupu do programů jazyka Simplicity: witness výraz. Kombinátor `witness` umožňuje integrovat do programů data podpisů a další witness materiál.

```
      w : B
-----------------
witness w : A ⊢ B
```

Sémantika witness výrazu je přímočará: ignoruje svůj vstup a jednoduše vrátí hodnotu `w` (která může být libovolného typu jazyka Simplicity), tj. `⟦witness w⟧(a) = w`. Toto nepřidává **žádnou novou vyjadřovací sílu** — podle věty o úplnosti dokáže Simplicity libovolnou takovou konstantní funkci sestavit už teď (vzpomeňte si na makro `scribe` z předchozích kapitol). Smysl kombinátoru `witness` spočívá výhradně v jeho **CMR**: hodnota `w` je z CMR výrazu **vyloučena**, takže adresu lze spočítat dříve, než je `w` známa, a `w` se dodá v čase uplatnění.

Toto návrhové rozhodnutí podporuje prořezávání — nevykonané podmíněné větve není třeba odhalovat on-chain, včetně jim příslušejících witness výrazů. Když je větev prořezána, ověřovatel potřebuje pouze CMR prořezaného podstromu, nikoli jeho skutečný obsah.

### Witness hodnoty

Může se zdát omezením, že witness výraz může obsahovat pouze *hodnotu*, a nikoli obecnější výraz jazyka Simplicity. Programy pro blockchainy založené na UTXO se však vykonávají pouze jednou. Není třeba předávat do witness uzlu celý podvýraz: uživatel může tento podvýraz jednoduše spustit sám, off-chain, a jeho výstup přepsat do witness hodnoty, aby získal naprosto stejný výsledek.

(Později v tomto kurzu se setkáme s kombinátorem `disconnect`, který se chová velmi podobně jako witness výraz, jenž *bere* jako svůj argument celý výraz jazyka Simplicity.)

Alternativní návrh by všechna witness data přiváděl jako argument do nejvyšší úrovně programu jazyka Simplicity. Witness výrazy se upřednostňují ze dvou důvodů. Zaprvé **prořezávání**: nevykonané větve výrazů `case` nejsou nikdy odhaleny on-chain a jakékoli witness výrazy uvnitř těchto větví jsou prořezány spolu s nimi. Zadruhé **lokalita**: witness výrazy nám umožňují umístit každou witness hodnotu přesně tam, kde se používá, namísto jejího protahování od nejvyšší úrovně vstupu programu.

### Odvození typů

Protože CMR se nezavazují k typům, typový systém se rekonstruuje během uplatnění. Algoritmus odvození typů jazyka Simplicity určuje minimální typy pro každý podvýraz na základě struktury kombinátorů. Přesněji, odvození počítá *principální* (nejobecnější) typ každého podvýrazu; jakékoli typové proměnné, které zůstanou volné, jsou pak instanciovány na jednotkový typ `𝟙`, což dává programu jedinečný, minimální typ.

### Závěr

V této kapitole jsme stanovili, že programy jazyka Simplicity jsou výrazy typu `𝟙 ⊢ 𝟙`, vysvětlili, jak se Commitment Merkle Roots konstruují z označkovaných SHA-256 hashů každého kombinátoru, a ukázali, jak se z CMR stávají on-chain adresy prostřednictvím Taproot z BIP-0341. Představili jsme witness výrazy jako mechanismus pro poskytování dat podpisů a dalších vstupů v čase utrácení, aniž bychom se v čase vytváření adresy zavazovali k jejich hodnotám.

# Závěrečná část

<partId>96952535-4aa6-4e78-91e2-d12e9df895d4</partId>

## Recenze a hodnocení

<chapterId>fb0b0133-39ea-497b-bd36-198be42c4fab</chapterId>
<isCourseReview>true</isCourseReview>

## Závěrečná zkouška

<chapterId>2cc5e818-abcb-4a0a-9991-7a492c572e2d</chapterId>
<isCourseExam>true</isCourseExam>

## Závěr

<chapterId>8ade24bd-a84f-4d25-8f64-bdfa8b58926c</chapterId>
<isCourseConclusion>true</isCourseConclusion>
