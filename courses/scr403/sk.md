---
name: Ponorenie sa do Simplicity
goal: Osvojte si filozofiu návrhu, typový systém a celý životný cyklus Simplicity
objectives:
  - Pochopiť tri základné metódy kompozície a deväť kombinátorov, ktoré tvoria úplný jazyk
  - Vybudovať booleovskú logiku, aritmetiku a SHA-256 z minimálneho typového systému Simplicity
  - Pochopiť, ako vedľajšie efekty Failure a Reader umožňujú skutočnú interakciu s blockchainom
  - Naučiť sa, ako sa programy Simplicity stávajú Taproot adresami a ako sa uplatňujú pomocou witness dát
---

# Ponorenie sa do Simplicity

Hlboký ponor do teórie a návrhových rozhodnutí za jazykom Simplicity, založený na kompletnej päťdielnej sérii článkov ["Ponorenie sa do Simplicity"](https://delvingbitcoin.org/t/delving-simplicity-part-three-fundamental-ways-of-combining-computations/1902) od [Dr. Russella O'Connora](https://r6.ca/), tvorcu Simplicity v Blockstream Research. Tento kurz vysvetľuje, *prečo* bol Simplicity navrhnutý tak, ako bol, nie ako ho písať.

Kurz sleduje články Dr. O'Connora cez tri základné spôsoby kombinovania výpočtov, minimálny typový systém a jeho vetu o úplnosti, konštrukciu praktických dátových typov a aritmetiky od prvých princípov, opatrné zavedenie vedľajších efektov pre interakciu s blockchainom a napokon to, ako sa programy zaväzujú do adries a uplatňujú on-chain.

+++

# Úvod

<partId>c362889b-c630-435f-911b-724c4eca505b</partId>

## Prehľad kurzu

<chapterId>cdcc40b6-c985-45b4-9bee-6f931e984476</chapterId>

Vitajte v SCR403 — Ponorenie sa do Simplicity!

Tento kurz je založený na sérii článkov **"Ponorenie sa do Simplicity"**, ktorú napísal [Dr. Russell O'Connor](https://r6.ca/), Infrastructure Tech Developer v [Blockstream](https://blockstream.com/) a tvorca Simplicity. Pôvodné články boli publikované na fóre [Delving Bitcoin](https://delvingbitcoin.org/u/roconnor-blockstream/summary) a tvoria hlavný zdrojový materiál tohto kurzu. Sme vďační za jeho priekopnícku prácu, vďaka ktorej mohol tento vzdelávací obsah vzniknúť.

### Čo sa naučíte

Tento kurz skúma filozofiu návrhu a matematické základy za Simplicity, skriptovacím jazykom novej generácie aktivovaným na [Liquid Network](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/) v júli 2025. Sleduje kompletnú päťdielnu sériu článkov a je štruktúrovaný do dvoch hlavných obsahových sekcií:

1. **Základy Simplicity** — Prečo blockchainové výpočty vyžadujú zásadne odlišný jazyk, tri spôsoby kombinovania operácií (sekvenčný, paralelný, podmienený) a deväť jadrových kombinátorov, ktoré tvoria matematicky úplný jazyk
2. **Od dátových typov k programom** — Budovanie booleovskej logiky, aritmetiky a SHA-256 od prvých princípov; pochopenie vedľajších efektov Failure a Reader, ktoré umožňujú interakciu s blockchainom; a naučenie sa, ako sa programy zaväzujú do Taproot adries cez Commitment Merkle Roots a uplatňujú pomocou witness dát

### Predpoklady

Toto je kurz na **expertskej úrovni** (približne 10 hodín). Mali by ste sa cítiť pohodlne s:
- Základnými konceptmi skriptovania v Bitcoine (čo robí validácia transakcie)
- Základnými konceptmi programovania (typy, funkcie, kompozícia)
- Určitá znalosť matematickej notácie je užitočná, ale nie je vyžadovaná. Všetko predstavujeme priebežne

### Kľúčové zdroje

- **Pôvodné články**: ["Ponorenie sa do Simplicity"](https://delvingbitcoin.org/u/roconnor-blockstream/summary) od Dr. Russella O'Connora na Delving Bitcoin
- **Repozitár Simplicity**: [BlockstreamResearch/simplicity](https://github.com/BlockstreamResearch/simplicity) — zdrojový kód a formálne dôkazy v Rocq
- **Oficiálna webová stránka**: [simplicity-lang.org](https://simplicity-lang.org/) — dokumentácia a referencia SimplicityHL
- **Blog Blockstream**: [Simplicity na GitHube](https://blog.blockstream.com/en-simplicity-github/) — technický prehľad

Ste pripravení ponoriť sa do jedného z najelegantnejších kúskov bitcoinového inžinierstva? Poďme na to!

## Čo je Simplicity?

<chapterId>d04f3960-d7fb-44e1-b5a3-25b33d03fd38</chapterId>

Ak prichádzate do tohto kurzu bez predchádzajúceho pozadia v Simplicity, táto kapitola vás zorientuje skôr, než sa ponoríme do hĺbky.

### Simplicity v skratke

Simplicity je **bitcoin-native jazyk smart kontraktov**, ktorý dnes beží na Liquid Network. Prvýkrát ho okolo roku 2012 načrtol Dr. Russell O'Connor a podrobne ho opísal vo svojom článku z roku 2017 *Simplicity: A New Language for Blockchains*; na Liquid Network bol aktivovaný v júli 2025 po rokoch formálnej verifikácie a vývoja.

Na rozdiel od ethereumového Solidity, čo je Turingovsky úplný vysokoúrovňový kontraktový jazyk, je Simplicity zámerne minimálny. Má:
- **Tri typové konštruktory** (jednotka, súčet, súčin)
- **Deväť kombinátorov** (základné operácie a pravidlá kompozície)
- **Žiadne cykly, žiadnu rekurziu, žiadnu dynamickú pamäť**

Len z týchto primitív môžete vybudovať akýkoľvek výpočet, ktorý potrebujete na validáciu transakcie, od booleovskej logiky až po plné hašovanie SHA-256.

### Čo môžete robiť so Simplicity dnes?

Simplicity už poháňa skutočné aplikácie na Liquid Network. Najvýznamnejšou je [Simplicity DEX](https://docs.simplicity-lang.org/use-cases/simplicity-dex/), trh opcií bez oraclov, kde používatelia obchodujú call opcie na L-BTC s USDt ako kolaterálom (podkladový kontrakt podporuje aj put opcie). Medzi ďalšie živé projekty Simplicity patria [Swaption](https://swaption.io/) od SideSwap (opcie) a open-source [Deadcat](https://github.com/Resolvr-io/deadcat) od Resolvr (predikčné trhy). Mimo DeFi Simplicity umožňuje pokročilé podmienky míňania, ako sú vaults, covenanty a komplexné multisig schémy, ktoré by boli v Bitcoin Scripte nemožné alebo nebezpečné.

### Čím tento kurz je — a čím nie je

Toto **nie je** praktický tutoriál programovania. Nebudete tu písať programy Simplicity. Ak hľadáte práve to, pozrite si:
- [simplicity-lang.org](https://simplicity-lang.org/) — oficiálnu dokumentáciu a vysokoúrovňový jazyk SimplicityHL
- [Repozitár Simplicity na GitHube](https://github.com/BlockstreamResearch/simplicity) — referenčnú implementáciu, príklady a dôkazy v Rocq
- [Blogový príspevok Blockstream](https://blog.blockstream.com/en-simplicity-github/) o začiatkoch

O čom tento kurz **je**: o **filozofických a technických voľbách** za návrhom Simplicity. Prečo bol tento jazyk vytvorený práve takto? Prečo iba deväť kombinátorov? Prečo žiadna rekurzia? Prečo záleží na tom, že typový systém sa prepája s Gentzenovým sekvenčným kalkulom?

Predstavte si to ako pochopenie toho, **prečo bol motor postavený takto**, a nie ako učenie sa šoférovať auto.

### Pre koho je tento kurz?

Tento kurz je ideálny pre:
- **Vývojárov protokolov**, ktorí chcú pochopiť základy Simplicity pred písaním kódu
- **Výskumníkov Bitcoinu**, ktorých zaujíma formálna verifikácia a typovo-teoretický prístup
- **Informatikov**, ktorí sú zvedaví na spojenie medzi sekvenčným kalkulom a blockchainovými výpočtami
- **Pokročilých bitcoinerov**, ktorí chcú ísť za povrchové pochopenie skriptovacích schopností Liquidu

Ak sú pre vás pojmy ako "súčtové typy", "kombinátory" alebo "sekvenčný kalkulus" úplne nové, nebojte sa, všetko vysvetlíme od základov. Pripravte sa však na hutnú matematickú cestu.

### Od článkov ku kurzu

Pôvodná séria "Ponorenie sa do Simplicity" od Dr. O'Connora je štruktúrovaná ako päť technických článkov. Tento kurz reorganizuje a anotuje tento materiál do progresívnej vzdelávacej cesty s kvízmi, ktoré budú priebežne testovať vaše porozumenie. Myšlienky, definície a dôkazy sú jeho a my sme formát prispôsobili pre štruktúrované vzdelávanie.

# Základy Simplicity

<partId>a5976618-94ab-4b29-b9aa-040d35c68e5d</partId>

## Základné spôsoby kombinovania výpočtov

<chapterId>6d46e77a-7e60-473b-b230-418da5ae44eb</chapterId>

Teraz, keď bol Simplicity aktivovaný na Liquid Network, rád by som sa podrobne ponoril do filozofie a návrhu jazyka Simplicity.

Validácia bitcoinových transakcií je výrazne odlišná aplikácia od bežného návrhu programovacích jazykov. Blokový priestor je drahý, takže programy musia byť kompaktné. Programy v bitcoinových transakciách sa vždy vykonávajú iba na jednom vstupe a každý vykonáva program na tom istom vstupe. Navyše agent autorizujúci transakciu už vopred pozná výsledok výpočtu: že transakcia je platná.

Autorizujúci agent zvyčajne spustí omnoho drahšie výpočty, aby odviedol witness dáta potvrdzujúce platnosť transakcie, zatiaľ čo programy bežiace na blockchaine musia witness dáta skontrolovať na platnosť. Kontrola platnosti je často oveľa lacnejšia než dokazovanie platnosti.

Simplicity sme navrhli s ohľadom na tieto jedinečné výzvy návrhu jazyka. Napríklad Simplicity vyžaduje, aby sa nevykonané vetvy prerezali, takže sa neobjavia na blockchaine. Kroky predspracovania sú starostlivo navrhnuté tak, aby vykazovali (kvázi-)lineárnu časovú zložitosť vzhľadom na veľkosť programu Simplicity. Namiesto "gas" sa používa statická analýza, pretože gas sa nedá vypočítať bez vykonania kódu predpísaným spôsobom, aby sa detaily exekučného modelu nestali konsenzuálne kritickými. Žiadna dynamická alokácia pamäte počas vykonávania. A tak ďalej.

Skôr než sa ponorím do detailov návrhu Simplicity, chcem túto sériu začať trochou programátorskej filozofie o všeobecných spôsoboch kombinovania základných stavebných blokov na vytváranie novej funkcionality.

### Kompozícia

Predstavme si, že niekto navrhuje jazyk pre programovateľné transakcie pre blockchain ako Bitcoin. Programy majú najmä prístup iba k dátam transakcie a k UTXO dátam vstupov a vykonanie iba určuje platnosť transakcie (čo umožňuje uložiť výsledok vykonania do cache). Povedzme, že sa začne s nejakou množinou základných operácií, ktoré môžu vykonávať rôzne úlohy, ako sú základné výpočty, čítanie a/alebo spracovanie dát z transakcie a overovanie podpisov. Každá operácia spotrebuje nejaký typ vstupu (prípadne prázdny) a vráti nejaký typ výstupu. Aké sú spôsoby, ktorými môžeme tieto základné operácie kombinovať do zložitejších operácií?

### Sekvenčná kompozícia

![Sekvenčná kompozícia](assets/en/001.webp)

Najzákladnejšou metódou kompozície je sekvenčná kompozícia. Ak máme dve základné operácie, pričom výstupný dátový typ jednej zodpovedá vstupnému dátovému typu druhej, môžeme tieto dve operácie skombinovať do novej zloženej operácie. Táto nová operácia spustí tieto dve základné operácie za sebou, pričom ako vstup vezme vstup prvej operácie, výstup tejto prvej operácie odovzdá do vstupu druhej operácie a nakoniec vráti výstup tejto druhej operácie.

Samozrejme, nemusíme sa obmedzovať iba na kombinovanie základných operácií. Teraz, keď máme nejaké zložené operácie, môžeme ich kombinovať aj pomocou funkcionálnej kompozície.

V matematike sa táto sekvenčná kompozícia často nazýva jednoducho "kompozícia" a človek by si mohol myslieť, že je to jediný spôsob skladania vecí. Máme však aj iné spôsoby kompozície operácií.

### Paralelná kompozícia

![Paralelná kompozícia](assets/en/002.webp)

Predpokladajme, že máme dve operácie, môžu to byť základné alebo komplexné operácie, a obe prijímajú rovnaký typ vstupu. Druhým základným spôsobom kompozície týchto dvoch operácií je vykonať ich obe na tom istom vstupe. Toto sa nazýva paralelná kompozícia a typ výstupu je "súčin" typov výstupov pôvodných operácií a obsahuje pár oboch výstupov.

Hoci sa to nazýva "paralelná" kompozícia a obe operácie by sa v princípe mohli vykonávať paralelne, paralelné vykonávanie nie je operačná požiadavka. Paralelnú kompozíciu môžeme implementovať "sekvenčne" tak, že najprv vykonáme jednu operáciu a potom druhú. Nezaujímajú nás detaily toho, ako je paralelná kompozícia implementovaná, pokiaľ je výstup rovnaký.

### Podmienená kompozícia

![Podmienená kompozícia](assets/en/003.webp)

Podmienená kompozícia je duálom paralelnej kompozície. V tomto prípade máme dve operácie, ktoré produkujú rovnaký výstup, a skladáme ich tak, že si vyberieme jednu z nich na vykonanie. Vstupom tejto zloženej operácie je "súčet" alebo "tagovaný union" typov vstupov pôvodnej operácie. V tomto prípade je tag, "Left" alebo "Right", jediný bit v dátach vstupu, ktorý určuje, ktorý typ dát sa nesie, a teda ktorá z dvoch operácií sa môže vykonať.

Podmienená kompozícia funguje rovnako aj vtedy, keď je vstup súčtom dvoch identických typov. Súčtový typ stále obsahuje tag a hodnota tohto tagu určuje, ktorá z dvoch operácií sa má vykonať.

### Kompozícia v Bitcoin Scripte

Existuje mnoho spôsobov, ako realizovať tieto tri druhy kompozície v rôznych programovacích jazykoch. V Bitcoin Scripte sa sekvenčná kompozícia realizuje (približne) konkatenáciou dvoch rutín (preto sa Bitcoin Script nazýva konkatenatívny programovací jazyk), keďže výstup jednej rutiny zostáva na zásobníku, aby ho spotrebovala nasledujúca rutina. Paralelná kompozícia sa dosahuje použitím operácií duplicate a swap na manipuláciu so zásobníkom, aby sa dve rutiny mohli spustiť na tom istom vstupe. Veci nie sú úplne priamočiare, pretože to, čo nazývame "súčinom" typov, sa zvyčajne realizuje využitím viacerých položiek zásobníka. Dúfajme, že vidíte všeobecnú myšlienku.

Podmienená kompozícia sa, samozrejme, realizuje pomocou `OP_IF`, ktorý vetví na základe hodnoty na zásobníku. V tomto prípade horná položka zásobníka hrá úlohu tagu a zvyčajne ďalšia položka alebo položky na zásobníku majú rôzne "typy", ktoré závisia od hodnoty tagu. V každom prípade môžu byť typy položiek zásobníka vhodné na spracovanie iba jednou z vetiev v `OP_IF`. Keď však dosiahneme `OP_ENDIF`, položky zásobníka musia mať konzistentný "typ", aby zvyšný script dokázal pokračovať nezávisle od toho, ktorá vetva bola predtým zvolená.

### Kompozícia v Simplicity

Simplicity sme navrhli s kombinátormi, ktoré priamo implementujú tieto tri formy kompozície. Spolu s niekoľkými ďalšími kombinátormi podporujúcimi iné základné operácie súvisiace so súčinovými a súčtovými typmi sa jadrový jazyk Simplicity napokon skladá z deviatich kombinátorov, ktoré postačujú na vyjadrenie ľubovoľného konečného výpočtu. Podrobnejšie o tom budeme hovoriť v nasledujúcej kapitole.

### Štvrtý druh kompozície

Pred koncom by sme mali spomenúť, že v informatike existuje aspoň jeden ďalší druh kompozície, a to "rekurzívna kompozícia". V rekurzívnej kompozícii sa jedna operácia iteruje viackrát.

Všimnite si, že Bitcoin Script nepodporuje rekurzívnu kompozíciu a podobne sme z návrhu Simplicity explicitne vylúčili neobmedzenú rekurziu. Naša téza je, že neobmedzený iteračný výpočet je lepšie implementovať pomocou rekurzívnych covenantov, ktoré počítajú cez viacero transakcií. To používateľom umožňuje vyhnúť sa obmedzeniam blokového priestoru a štandardnosti a lepšie predvídať náklady transakcií.

Napriek tomu existujú spôsoby, ako zneužiť delegačnú funkciu Simplicity na poskytnutie niečoho, čo pripomína neobmedzenú rekurzívnu kompozíciu; o tom možno budeme diskutovať neskôr v tejto sérii.

### Záver

Preskúmali sme tri hlavné formy kompozície na transformáciu základných operácií na komplexné operácie:

- sekvenčná kompozícia
- paralelná kompozícia
- podmienená kompozícia

Diskutovali sme, ako sa tieto formy kompozície realizujú v Bitcoin Scripte, a naznačili sme, ako ovplyvnili návrh jazyka Simplicity. Poznamenali sme, že štvrtý druh kompozície, rekurzívna kompozícia, je špecificky vylúčený zo Simplicity aj z Bitcoin Scriptu.

V nasledujúcej kapitole opíšeme deväť kombinátorov, ktoré tvoria jadro jazyka Simplicity, ako slúžia na priame realizovanie týchto troch foriem kompozície a ako to tvorí úplný jazyk na opis ľubovoľného konečného výpočtu.

## Kombinátorová úplnosť Simplicity

<chapterId>2a10a6ba-fada-4556-a673-3ae8c0794bf0</chapterId>

V tejto kapitole predstavíme jadrový jazyk Simplicity a ukážeme, že jazyk je úplný, čo znamená, že v ňom možno vyjadriť ľubovoľný konečný výpočet.

### Typy Simplicity

Simplicity podporuje tri základné typové konštruktory. Súčinový typ `A × B` reprezentuje výstupy paralelnej kompozície, zatiaľ čo súčtový typ `A + B` (tagovaný union) obsluhuje vstupy podmienenej kompozície. Tretím typom je jednotkový typ.

### Jednotkový typ

Jednotkový typ, označovaný `𝟙` alebo `ONE`, obsahuje presne jednu hodnotu: prázdnu n-ticu `⟨⟩` alebo `()`. Tento nulabitový dátový typ nenesie žiadnu informáciu.

### Súčtový typ

Súčtový typ `A + B` kombinuje dva typy s tagmi označujúcimi "ľavý" alebo "pravý". Hodnoty sa zapisujú ako `σᴸ(a)` alebo `inl(a)` pre hodnoty s ľavým tagom a `σᴿ(b)` alebo `inr(b)` pre hodnoty s pravým tagom. Tagy zostávajú odlišné aj pri kombinovaní identických typov.

#### Booleovský typ

Typ `𝟙 + 𝟙`, označovaný `𝟚` alebo `TWO`, reprezentuje jednobitový typ s dvoma hodnotami. Podľa konvencie `σᴸ⟨⟩` reprezentuje false/nulu, zatiaľ čo `σᴿ⟨⟩` reprezentuje true/jednotku.

### Súčinový typ

Súčinové typy `A × B` obsahujú páry hodnôt zapisované ako `⟨a, b⟩` alebo `(a, b)`. Typ `𝟚 × 𝟚` má štyri hodnoty, odlišné od štyroch hodnôt v `𝟚 + 𝟚`.

### Jadrové výrazy Simplicity

Operácie sa označujú ako `f : A ⊢ B`, čo znamená vstupný typ `A` a výstupný typ `B`. Simplicity je "prvého rádu" — chýbajú mu funkčné typy.

### Dve základné operácie

Jadrový jazyk poskytuje dve základné operácie:

**Identita (`iden`).** Operácia identity odovzdá svoj vstup bez zmeny:

```
iden : A ⊢ A
⟦iden⟧(a) = a
```

**Jednotka (`unit`).** Operácia jednotky zahodí svoj vstup a vráti prázdnu n-ticu:

```
unit : A ⊢ 𝟙
⟦unit⟧(a) = ⟨⟩
```

Tieto tvoria rodiny s jednou operáciou pre každý typ.

### Tri kombinátory kompozície

Sekvenčná kompozícia používa `comp f g` (písané `f ⨾ g` alebo `f >>> g`):

```
If f : A ⊢ B and g : B ⊢ C, then
comp f g : A ⊢ C
⟦f ⨾ g⟧(a) = ⟦g⟧(⟦f⟧(a))
```

Paralelná kompozícia používa `pair f g` (písané `f ▵ g` alebo `f &&& g`):

```
If f : A ⊢ B and g : A ⊢ C, then
pair f g : A ⊢ B × C
⟦f ▵ g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩
```

Podmienená kompozícia používa `case f g : (A + B) × C ⊢ D`, čím vetvám poskytuje prístup k zdieľanému prostrediu `C`:

```
If f : A × C ⊢ D and g : B × C ⊢ D, then
case f g : (A + B) × C ⊢ D
⟦case f g⟧⟨σᴸ(a), c⟩ = ⟦f⟧⟨a, c⟩
⟦case f g⟧⟨σᴿ(b), c⟩ = ⟦g⟧⟨b, c⟩
```

Prečo má podmienená kompozícia takýto tvar — súčet spárovaný so zdieľaným prostredím `C` — namiesto jednoduchšieho `copair f g : A + B ⊢ C`, ktorý len vyberá vetvu? Pretože samotný `copair` nedokáže vyjadriť **distribúciu**: funkciu `dist : (A + B) × C ⊢ A × C + B × C`, ktorá vtlačí zdieľaný vstup do tej vetvy, ktorá sa zvolí. Zabudovaním prostredia `C` priamo do `case` Simplicity získava podmienenú kompozíciu *aj* distribúciu z jediného kombinátora — jedno z kľúčových návrhových rozhodnutí, ktoré drží jadrový jazyk na deviatich kombinátoroch.

### Štyri ďalšie kombinátory

Spotreba súčinu používa `take` a `drop`:

**take** extrahuje ľavý prvok:

```
If f : A ⊢ C, then
take f : A × B ⊢ C
⟦take f⟧⟨a, b⟩ = ⟦f⟧(a)
```

**drop** extrahuje pravý prvok:

```
If f : B ⊢ C, then
drop f : A × B ⊢ C
⟦drop f⟧⟨a, b⟩ = ⟦f⟧(b)
```

Produkcia súčtu používa `injl` a `injr`:

**injl** obaľuje ľavým tagom:

```
If f : A ⊢ B, then
injl f : A ⊢ B + C
⟦injl f⟧(a) = σᴸ(⟦f⟧(a))
```

**injr** obaľuje pravým tagom:

```
If f : A ⊢ C, then
injr f : A ⊢ B + C
⟦injr f⟧(a) = σᴿ(⟦f⟧(a))
```

### Deväť jadrových kombinátorov

Celkovo má Simplicity presne deväť jadrových kombinátorov:

| Kombinátor | Účel |
|---|---|
| `iden` | Odovzdať vstup ďalej |
| `unit` | Zahodiť vstup |
| `comp` | Sekvenčná kompozícia |
| `pair` | Paralelná kompozícia |
| `case` | Podmienená kompozícia |
| `take` | Extrahovať ľavú časť zo súčinu |
| `drop` | Extrahovať pravú časť zo súčinu |
| `injl` | Injektovať do ľavej časti súčtu |
| `injr` | Injektovať do pravej časti súčtu |

### Simplicity a sekvenčný kalkulus

Návrh Simplicity vychádza z konjunktívno-disjunktívneho fragmentu Gentzenovho sekvenčného kalkulu. Presnejšie, ide o variant *funkcionálnej interpretácie* sekvenčného kalkulu, ktorá je sama analogická Curryho-Howardovej korešpondencii medzi prirodzenou dedukciou a lambda kalkulom. Pravidlá kombinátorov vykazujú "menšie typy v premisách než v záveroch", čo umožňuje Bit Machine — abstraktnému zásobníkovému interpretu Simplicity — minimalizovať kopírovanie dát počas vykonávania.

### Hodnoty nie sú výrazy

Výrazy Simplicity označujú operácie, nie hodnoty. Notácia `scribe b : A ⊢ B` reprezentuje jedinečný výraz, ktorý vždy vracia hodnotu `b`, a slúži skôr ako notačná pohodlnosť než ako kombinátor. To zrkadlí Bitcoin Script, kde operácie ako `OP_1` hodnoty vkladajú, a nie vyjadrujú priamo.

### Veta o úplnosti Simplicity

Keď máme v rukách všetkých deväť kombinátorov, ako vieme, že nám nič nechýba — že týchto deväť naozaj stačí? Odpovedá na to veta o úplnosti Simplicity: pre ľubovoľnú funkciu medzi (konečnými) typmi Simplicity existuje nejaký výraz Simplicity, ktorý ju označuje. Dôkaz je konštruktívny — ukazuje, ako tento výraz vybudovať:

1. **Rozložiť vstup**: Pomocou vnorených výrazov `case` úplne rozložte ľubovoľný vstup ľubovoľného typu na jeho konštitučné bity
2. **Vybudovať vyhľadávaciu tabuľku**: Pre každý možný vstup použite `scribe` na vytvorenie príslušného výstupu
3. **Zostaviť**: Vnorené case a scribe spolu tvoria obrovskú vyhľadávaciu tabuľku, ktorá implementuje funkciu

Táto veta je formálne overená v dôkazovom asistentovi Rocq (predtým Coq). Dôkaz je súčasťou oficiálneho repozitára Simplicity a bol strojovo skontrolovaný na korektnosť.

Hoci veta o úplnosti zaručuje, že deväť kombinátorov Simplicity dokáže vyjadriť ľubovoľnú funkciu medzi (konečnými) typmi Simplicity, výsledné výrazy z konštrukcie vyhľadávacej tabuľky sú neprakticky veľké. Funkcia na 256-bitových vstupoch by vyžadovala vyhľadávaciu tabuľku s 2²⁵⁶ položkami. Preto sa nasledujúce kapitoly sústreďujú na budovanie efektívnych výrazov, ktoré využívajú štruktúru výpočtov, namiesto brutálneho riešenia všetkého cez vyhľadávacie tabuľky.

### Záver

Jadrový jazyk Simplicity zahŕňa typový systém a kombinátory umožňujúce ľubovoľný konečný výpočet. Hoci veta o úplnosti zaručuje vyjadrovaciu schopnosť, výsledné výrazy z generickej konštrukcie sú neprakticky veľké. Praktický vývoj v Simplicity zahŕňa využívanie výpočtovej štruktúry na stručné výrazy. Nasledujúce kapitoly preskúmajú dátové štruktúry, interakcie s transakciami a ďalšie kombinátory.

# Od dátových typov k programom

<partId>08528a6f-d310-4675-b8cd-4e9b93b3c009</partId>

## Budovanie dátových typov

<chapterId>9981ae62-ae50-4770-adf2-b253d1e08de3</chapterId>

V predchádzajúcich kapitolách sme ukázali, ako jadrová množina kombinátorov Simplicity stačí na implementáciu ľubovoľného konečného čistého výpočtu. Táto kapitola ukazuje, ako z týchto primitív vybudovať praktické dátové štruktúry a výpočty — rovnakým spôsobom, akým sa počítače budujú z logických hradiel.

### Booleovská logika

Booleovský typ, označovaný `𝟚`, sa rovná `𝟙 + 𝟙` a má dve hodnoty: `σᴸ⟨⟩` (false) a `σᴿ⟨⟩` (true). Pomocou jadrových kombinátorov možno zostrojiť operátory booleovskej logiky.

#### Operácia And

Logická operácia `and : 𝟚 × 𝟚 ⊢ 𝟚` vezme dva bity a vráti jeden bit. Implementácia vetví podľa prvého bitu: ak je false, vráti false; inak vráti druhý bit.

```
and ≔ case (injl unit) (drop iden) : 𝟚 × 𝟚 ⊢ 𝟚
```

Testovanie s `⟨false, false⟩`:

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

Testovanie s `⟨true, true⟩`:

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

#### Ďalšie logické operácie

Operácia `not` vyžaduje pomocný kombinátor:

```
                   f : A ⊢ C    g : B ⊢ C
--------------------------------------------------------------
copair f g ≔ iden ▵ unit ⨾ case (take f) (take g) : A + B ⊢ C
```

Počiatočné `iden ▵ unit : A ⊢ A × 𝟙` pridá k vstupu prázdne "prostredie", čo umožní použiť kombinátor `case`. Použitie `take` v oboch vetvách zahodí toto prázdne prostredie, aby sa vykonalo `f` alebo `g`.

Ďalšie booleovské logické operácie:

- `or ≔ case (drop iden) (injr unit) : 𝟚 × 𝟚 ⊢ 𝟚`
- `not ≔ copair (injr unit) (injl unit) : 𝟚 ⊢ 𝟚`
- `xor ≔ case (drop iden) (drop not) : 𝟚 × 𝟚 ⊢ 𝟚`

### Bitové sčítačky

"Polsčítačka" vezme dva bity a sčíta ich, čím vytvorí dvojbitový výstup: bit prenosu a bit súčtu.

```
half-adder ≔ and ▵ xor : 𝟚 × 𝟚 ⊢ 𝟚 × 𝟚
```

"Plná sčítačka" sčíta tri bity a vytvorí dvojbitový výstup. Vstup používa vnorenú n-ticu `(𝟚 × 𝟚) × 𝟚`.

Pre vnorené n-tice sa používa kompaktná notácia:

- `O f` označuje `take f`
- `I f` označuje `drop f`
- `H` označuje `iden`

Napríklad `I O H` znamená `drop (take iden) : A × (B × C) ⊢ B`, extrahujúc prostrednú hodnotu. Notácia evokuje binárne číslice: keď si vnorené n-tice predstavíme ako binárne stromy, notácia predstavuje obrátené binárne číslice pozícií v strome. Tieto výrazy tvoria De Bruijnove indexy pre Simplicity.

**Poznámka:** Notácia `I`, `O` a `H` sa vzťahuje iba na podvýrazy pozostávajúce výlučne z `take`, `drop` a `iden`.

Plná sčítačka skladá dve polsčítačky a berie logické `or` bitov prenosu:

```
full-adder ≔ take half-adder ▵ I H
           ⨾ O O H ▵ (O I H ▵ I H ⨾ half-adder)
           ⨾ (O H ▵ I O H ⨾ or) ▵ I I H
           : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × 𝟚
```

V prvom riadku `take half-adder ▵ I H : (𝟚 × 𝟚) × 𝟚 ⊢ (𝟚 × 𝟚) × 𝟚` spustí polsčítačku na prvých dvoch bitoch a uloží posledný bit.

V druhom riadku `O O H ▵ (O I H ▵ I H ⨾ half-adder) : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × (𝟚 × 𝟚)` uloží prvý bit (výstupný prenos prvej polsčítačky) a spustí polsčítačku na posledných dvoch bitoch.

V poslednom riadku `(O H ▵ I O H ⨾ or) ▵ I I H: 𝟚 × (𝟚 × 𝟚) ⊢ 𝟚 × 𝟚` vezme logické OR prvých dvoch bitov (výstupné prenosy oboch polsčítačiek) a vráti výstupný bit súčtu druhej polsčítačky.

Toto demonštruje programovanie v Simplicity: používanie notácie `I`, `O` a `H` na referencovanie dátových bitov, tvorbu vhodných "prostredí" na volanie iných funkcií cez sekvenčnú kompozíciu.

Používatelia nedefinujú nízkoúrovňové operácie priamo. Neskôr táto séria rozoberá jets štandardnej knižnice implementujúce bežné funkcie. Od koncových používateľov sa neočakáva, že budú programovať priamo v Simplicity, podobne ako v Bitcoin Scripte. Namiesto toho vyššieúrovňové jazyky ako SimplicityHL generujú kód Simplicity, spravujú "prostredia" podvýrazov a prekladajú pomenované premenné na príslušné sekvencie `take` a `drop`.

### Vektory

Vektory s pevnou dĺžkou sú definované tvorbou iterovaných súčinov typu `A`:

- `A² ≔ A × A`
- `A⁴ ≔ A² × A²`
- `A⁸ ≔ A⁴ × A⁴`
- `…`

Tie sa môžu zapisovať ako `A^2`, `A^4`, `A^8` atď.

Vektory sú definované iba pre dĺžky, ktoré sú mocninami dvojky. Iné mocniny vyžadujú zvoliť konvencie zátvorkovania.

Pre daný výraz `f : A ⊢ B` opakované párovanie "mapuje" tento výraz cez vektory s pevnou dĺžkou:

- `f² ≔ f ▵ f : A² ⊢ B²`
- `f⁴ ≔ f² ▵ f² : A⁴ ⊢ B⁴`
- `f⁸ ≔ f⁴ ▵ f⁴ : A⁸ ⊢ B⁸`

Pre danú funkciu `f : A × B ⊢ B` iterácia alebo "folding" cez vektory s pevnou dĺžkou:

- `fold-right-2 f ≔ O O H ▵ (O I H ▵ I H ⨾ f) ⨾ f : A² × B ⊢ B`
- `fold-right-4 f ≔ fold-right-2 (fold-right-2 f) : A⁴ × B ⊢ B`
- `fold-right-8 f ≔ fold-right-2 (fold-right-4 f) : A⁸ × B ⊢ B`

Existuje mnoho variácií. Pre dané `f : A × B ⊢ C`, "zip" cez spárované vektory s `zip-n f : (Aⁿ × Bⁿ) ⊢ Cⁿ`. Pre dané `f : (A × B) × C ⊢ C`, fold cez spárované vektory s `bifold-right-n f : (Aⁿ × Bⁿ) ⊢ C`. Kombinovanie `map` a `fold-right` vytvára akumulujúce kombinátory: `f : A × C ⊢ C × B` dáva `map-accum-right-n f : Aⁿ × C ⊢ C × Bⁿ`. Možných je mnoho ďalších variantov.

#### Viacbitové slová

Bitový vektor dáva viacbitové celé čísla. Napríklad `𝟚³²` je typ 32-bitového slova. `𝟚²⁵⁶` je typ 256-bitového slova, vhodný pre hashe a kryptografické operácie.

Použitím plnej sčítačky variant vektorových operácií definuje "sčítačku s postupným prenosom" cez viacbitové slová:

```
full-adder-n ≔ zip-accum-right-n full-adder : (𝟚ⁿ × 𝟚ⁿ) × 𝟚 ⊢ 𝟚 × 𝟚ⁿ
```

`full-adder-n` vezme dve n-bitové binárne čísla a jednobitový vstupný prenos a vráti jednobitový príznak výstupného prenosu a n-bitový súčet.

#### SHA-256

Rekurzívnym definovaním aritmetických operácií na viacbitových slovách — odčítanie, násobenie, delenie — a bitových logických operácií, ako sú logické AND, OR, XOR, a ich opakovaným kombinovaním možno vybudovať dokonca aj blokovú kompresnú funkciu SHA-256:

```
sha256-hash-block ≔ … : 𝟚²⁵⁶ × 𝟚⁵¹² ⊢ 𝟚²⁵⁶
```

Kompresia SHA-256 je formálne definovaná pomocou Simplicity v dôkazovom asistentovi Rocq (predtým Coq), s formálnym dôkazom, že implementácia `sha256-hash-block` je korektná.

Kompresia beží ako surový Simplicity príliš pomaly. Jets vykonávajú bežné funkcie, ako je kompresia SHA-256, natívne. Čisté implementácie v Simplicity slúžia ako formálne špecifikácie pre jets.

### Option typy

Option typy vznikajú zobratím súčtu s jednotkovým typom:

```
Option A ≔ 𝟙 + A
```

Typ `Option A` sa môže písať ako `A?` alebo `𝕊 A` (kde `𝕊` znamená "successor"). Funkcie sa mapujú cez option typy:

```
                 f : A ⊢ B
------------------------------------------
f? ≔ copair (injl unit) (injr f) : A? ⊢ B?
```

Možno definovať monadické kombinátory, ako je bind:

```
              f : A ⊢ B?
---------------------------------------
bind f ≔ copair (injl unit) f : A? ⊢ B?
```

### Buffery s premenlivou dĺžkou

"Buffery" sú typy pre čiastočne vyplnené vektory:

- `Aᑉ² ≔ A?`
- `Aᑉ⁴ ≔ A²? × Aᑉ²`
- `Aᑉ⁸ ≔ A⁴? × Aᑉ⁴`
- `…`

Typ `Xᑉ⁸` sa rozvinie na `(1 + X⁴) × ((1 + X²) × (1 + X))`. Ak to považujeme za polynóm a rozvinieme, dostaneme `1 + X + X² + X³ + X⁴ + X⁵ + X⁶ + X⁷`. Interpretované ako typ to reprezentuje súčet všetkých možných n-tíc X do dĺžky 7 vrátane prázdnej n-tice. Presne toto je typ zoznamov s dĺžkou striktne menšou než 8.

Podobne ako pri vektoroch možno nad buffermi definovať operácie mapovania a folding. Operácie so zásobníkom zahŕňajú `push-<n : Aᑉⁿ × A ⊢ Aⁿ + Aᑉⁿ` a `pop-<n : Aᑉⁿ ⊢ (Aᑉⁿ × A)?`. `push-<n` pripojí položku k bufferu a pri pretečení vráti plný vektor. `pop-<n` odstráni položku a vráti menší buffer a odstránenú položku, prípadne nevráti nič, ak bol pôvodný buffer prázdny.

Definícia `push-<n`, rekurzívne:

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

Surový Simplicity sa za určitou úrovňou zložitosti stáva ťažko sledovateľným. Koncoví používatelia využívajú vyššieúrovňové jazyky ako SimplicityHL, ktoré generujú tieto idiomatické výrazy.

### Záver

Táto kapitola ukázala, ako z bitov budovať logické operácie. Z nich vznikla bitová aritmetika, umožňujúca uvažovať o vykonávaní. Boli vyvinuté vektorové typy, ktoré demonštrujú iteráciu cez viacbitové slová na definovanie aritmetiky. Ďalej možno kryptografické operácie ako SHA-256 a validáciu Schnorrových podpisov definovať iba pomocou kombinátorov Simplicity — všetky sú skutočne definované pomocou Simplicity.

Táto kapitola nie je komplexným sprievodcom všetkými možnými dátovými typmi a operáciami, ktoré možno v Simplicity vybudovať, ale ilustruje dosiahnutie praktickej funkcionality v rámci obmedzení Simplicity. Napriek konečne ohraničeným typom možno definovať užitočné vektory, typy bufferov a operácie iterujúce cez tieto štruktúry.

Skutočné špecifikácie operácií štandardnej knižnice sa mierne líšia od tu uvedených definícií. Napríklad plná sčítačka používa 3-cestný XOR a logickú funkciu "majority" namiesto dvoch polsčítačiek.

V praxi programy Simplicity používajú jets pre aritmetické a kryptografické operácie. Jets však nahrádzajú iba výrazy. Kombinátory iterujúce cez buffery a vektory nemožno nahradiť jets a objavujú sa v skutočných programoch Simplicity. Hoci namiesto ich priameho používania koncoví používatelia používajú vyššieúrovňové jazyky ako SimplicityHL, ktoré takéto výrazy generujú.

Rekurzívne definované kombinátory sa zdajú rásť exponenciálne vo veľkosti výrazu. To nie je problém. Počas serializácie sa výrazy kódujú ako DAGy (orientované acyklické grafy), nie ako stromy. Skutočná reprezentácia rastie iba lineárne.

Doteraz sme zvažovali iba čisté výpočty. Interakcia s transakčnými dátami pri úlohách, ako je podpisovanie transakcií, vyžaduje nejaký spôsob, aby programy zlyhali, ak sú podpisy neplatné. Nasledujúca kapitola rozoberá vedľajšie efekty v Simplicity.

## Dva vedľajšie efekty

<chapterId>9eafe498-0765-419a-a69d-a74a9cdf3713</chapterId>

V predchádzajúcich kapitolách sme ukázali, ako budovať niektoré dátové štruktúry a výpočty pomocou jadrovej množiny kombinátorov Simplicity. Ako sme poznamenali, jadrové kombinátory stačia na implementáciu ľubovoľného konečného čistého výpočtu. To vyvoláva otázku: čo viac možno dosiahnuť? Do našich výrazov môžeme pridať ďalšie vedľajšie efekty.

Pre výrazy existujú rôzne možné druhy vedľajších efektov: aktualizácia stavu, zápis do logu, vyhodenie výnimky, čítanie z prostredia, volanie pokračovania atď. Vedľajšie efekty dostupné v Simplicity budú závisieť od aplikácie.

Pre aplikácie Bitcoinu a Liquidu máme aktuálne dva vedľajšie efekty: efekt Failure, čo je efekt výnimky, kde výnimka má typ `𝟙`, a efekt Reader, ktorý umožňuje prístup k dátam z transakčného prostredia. Naše jadrové kombinátory sú "čisté"; nemajú žiadne vedľajšie efekty. Jets však môžu zavádzať nové primitíva, ktoré vedľajšie efekty majú.

### Jets s efektmi

O jets budeme hovoriť neskôr v tomto kurze, ale tu predstavíme niekoľko príkladov jets na ilustráciu ich vedľajších efektov.

#### Bip0340-verify

`bip0340-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚⁵¹² ⊢ 𝟙` je jet pre výraz, ktorý vezme x-only verejný kľúč, 256-bitovú správu a Schnorrov podpis a nevráti nič! Podľa svojho typu by sa mal správať rovnako ako `unit`. Rozdiel spočíva vo vedľajšom efekte jetu: ak validácia podpisu zlyhá, celý výpočet sa preruší vyhodením výnimky (jednotkového typu). Toto je efekt Failure.

#### Verify

`verify : 𝟚 ⊢ 𝟙` je minimalistický jet na vyjadrenie efektu Failure. Ak je vstup `verify` `false`, celý výpočet sa preruší vyhodením výnimky. Ak je vstup `true`, nič sa nevráti, ale výpočet môže pokračovať.

#### Haše transakcií

`sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` sa javí ako konštantná funkcia, keďže existuje iba jedna možná vstupná hodnota: prázdna n-tica. Tento jet však číta z transakčného prostredia a produkuje hash transakčných dát, ktorý je analogický message digestu `SIGHASH_ALL` používanému pri overovaní podpisov v Bitcoin Scripte. Toto je príklad efektu Reader: vrátená hodnota závisí od transakčného prostredia, v ktorom sa jet vykonáva. Existuje niekoľko ďalších hašovacích jets, ktoré hašujú rôzne podmnožiny dát transakčného prostredia, aby pomohli budovať vlastné message digesty pre podpisy.

#### Introspekčné jets

`input-sequence : 𝟚³² ⊢ 𝟚³²?` je funkcia, ktorá vezme index vstupu a vráti sequence number transakcie pre tento vstup, prípadne nevráti nič, ak je index mimo rozsahu. Výstupná hodnota opäť nie je čistou funkciou indexu vstupu; operácia používa efekt Reader na prístup k transakčnému prostrediu, aby určila výstupnú hodnotu. Existuje niekoľko ďalších introspekčných jets, ktoré vracajú rôzne fragmenty dát transakčného prostredia.

### Klasifikácia efektov

Nie všetky vedľajšie efekty sú rovnaké. Niektoré vedľajšie efekty sa správajú krajšie než iné. Efekty môžeme klasifikovať podľa toho, ako dobre sa hodia na transformácie programov.

#### Komutatívne efekty

Komutatívny efekt je taký, pri ktorom, ak zameníte výstupy dvoch výrazov, môžete bezpečne zameniť aj samotné výrazy bez zmeny efektu výrazu. Uvažujme `swap = I H ▵ O H : A × B ⊢ B × A`. Ak `f ▵ g ⨾ swap = g ▵ f` pre každý výraz `f` a `g` s vedľajšími efektmi, potom sú efekty komutatívne.

Čítanie transakčných dát z prostredia je komutatívny efekt, pretože výsledok čítania z prostredia je rovnaký bez ohľadu na to, v akom poradí čítanie vykonáme.

Vo všeobecnosti vyhodenie výnimky nie je komutatívny efekt. Ak `f` vyhodí nejakú výnimku `e₁` a `g` vyhodí nejakú inú výnimku `e₂`, potom to, ktorá výnimka sa vyhodí z páru `f` a `g`, závisí od poradia ich vykonania.

V špeciálnom prípade efektu Failure, v ktorom možno vyhodiť iba výnimku jednotkového typu, je však efekt komutatívny. Bez ohľadu na to, ktorý z `f` alebo `g` vyhodí výnimku, výsledná výnimka bude rovnaká, pretože existuje iba jedna možná hodnota výnimky.

#### Idempotentné efekty

Idempotentný efekt je taký, pri ktorom, ak duplikujete výstup výrazu, môžete bezpečne duplikovať samotný výraz bez zmeny efektu výrazu. Uvažujme `dup = iden ▵ iden : A ⊢ A × A`. Ak `f ⨾ dup = dup ⨾ f ▵ f` pre každé `f` s vedľajšími efektmi, potom sú efekty idempotentné.

Čítanie transakčných dát z prostredia je idempotentný efekt. Vyhodenie výnimky je tiež idempotentný efekt. Hoci sa vykoná iba jeden z dvoch duplikovaných výrazov, každá výnimka vyhodená výrazom `dup ⨾ f ▵ f` bude rovnaká ako výnimka vyhodená výrazom `f ⨾ dup`.

Zápis do logu však nemusí byť idempotentný, pretože duplikovanie efektu by spôsobilo, že log správa sa objaví dvakrát. Ak však log pozostáva z _množiny_ správ namiesto _zoznamu_ správ, potom by bol efekt idempotentný (a komutatívny), pretože vkladanie do množiny je samo idempotentnou operáciou.

#### Unitárne efekty

Unitárny efekt je taký, pri ktorom, ak zahodíte výstup výrazu, môžete bezpečne zahodiť samotný výraz bez zmeny efektov výrazu. Ak vždy platí, že `f ⨾ unit = unit` pre každé `f` s vedľajšími efektmi, potom sú vaše efekty unitárne.

Čítanie dát z prostredia je jeden z mála typov unitárnych efektov. Ak sa výsledok čítania transakčných dát z prostredia zahodí, celý výraz vykonávajúci čítanie možno zahodiť.

Efekt zlyhania nie je unitárny. Ak `f` vyhodí výnimku, potom ju vyhodí aj `f ⨾ unit`; vykonanie sa ani nedostane ku kombinátoru `unit`, kým sa výpočet preruší. Na druhej strane `unit` by zjavne žiadnu výnimku nevyhodil, takže efekty `f ⨾ unit` a `unit` by boli odlišné.

Zhrnutie toho, ako si vyššie diskutované efekty vedú voči týmto trom vlastnostiam:

| Efekt | Komutatívny | Idempotentný | Unitárny |
| --- | :---: | :---: | :---: |
| Reader (transakčné prostredie) | ✓ | ✓ | ✓ |
| Failure (výnimka jednotkového typu) | ✓ | ✓ | ✗ |
| Writer (log ako množina) | ✓ | ✓ | ✗ |
| Všeobecné výnimky (ľubovoľný typ) | ✗ | ✓ | ✗ |

### Efekty povolené v Simplicity

Čím lepšie vlastnosti má typ efektu, tým viac priestoru má optimalizátor Simplicity na transformovanie programov, ktoré tieto efekty používajú. Ideálne by sme povolili iba efekty, ktoré majú všetky tri vlastnosti: komutatívnosť, idempotentnosť a unitárnosť. To by optimalizátoru umožnilo vykonávať akýkoľvek druh programovej transformácie, aký chce. Čítanie z prostredia je však jediný efekt, ktorý spĺňa všetky tri vlastnosti.

Namiesto toho vyžadujeme, aby efekty Simplicity boli komutatívne a idempotentné. Oba efekty, ktoré v Simplicity používame, efekt Failure a efekt Reader, sú komutatívne a idempotentné. To umožňuje vykonávať veľkú triedu optimalizácií na kóde Simplicity.

Transformácia "discard" opísaná vyššie, pokúšajúca sa nahradiť `f ⨾ unit` za `unit`, alebo akákoľvek podobná transformácia však nie je povolená, ak `f` môže produkovať efekt Failure. Predstavte si totiž, že by `f` obsahovalo tvrdenie `bip0340-verify`. Bolo by katastrofálne pokúsiť sa túto kontrolu optimalizovať preč.

### Prečo vôbec povoliť vedľajšie efekty?

Prečo Simplicity vôbec povoľuje vedľajšie efekty? Nebolo by lepšie, keby každý program prijal celú transakciu ako vstup a vrátil booleovský výstup, ktorý rozhodne, či je transakcia platná alebo nie?

#### Dávkové overovanie

Jedným z dôvodov, prečo máme efekt Failure, je podpora [dávkového overovania](https://github.com/bitcoin/bips/blob/c9a6ca6297eb8de850f6b64dafb8e60ee9b64d66/bip-0340.mediawiki#batch-verification) Schnorrových podpisov. Pri dávkovom overovaní sa mnoho jednotlivých kontrol Schnorrových podpisov spojí tak, že ak zlyhá ktorákoľvek jednotlivá kontrola podpisu, zlyhá celá dávka.

Tento dávkovací postup zlepšuje efektivitu oproti individuálnemu overovaniu každého podpisu. Nevýhodou je, že ak dávkové overenie zlyhá, nedozvieme sa, ktorá konkrétna kontrola alebo kontroly podpisov zlyhali.

Použitím vedľajšieho efektu zlyhania `bip0340-verify` zabezpečuje, že ak kontrola podpisu zlyhá, zlyhá celá transakcia. Keby `bip0340-verify` namiesto toho vracal `𝟚`, booleovský typ, pre úspech alebo zlyhanie, potom by zlyhaná kontrola podpisu stále mohla viesť k vetve, v ktorej script uspeje. V takom prípade by sme potrebovali vedieť, či je konkrétny podpis platný alebo nie, a teda by sme nemohli využiť dávkové overovanie.

#### Predpočítané transakčné dáta

Problémom v skorom Bitcoin Scripte bolo, že hašovacia funkcia používaná na vytváranie message digestov pre podpisy bola lineárna vo veľkosti transakcie. Typicky každý vstup vytvára aspoň jeden message digest na overenie podpisu, takže celkové množstvo hašovania bolo kvadratické vo veľkosti transakcie.

Tento problém bol opravený v Segwit a neskorších iteráciách Bitcoin Scriptu redefinovaním message digestov tak, aby sa dali počítať v konštantnom čase na každú kontrolu podpisu. To sa opiera o `PrecomputedTransactionData`, ktoré predpočíta hashe transakčných dát raz a potom ich zdieľa každé sighash počítanie vstupu. Transakčné hašovacie jets Simplicity sa opierajú o rovnaký druh predpočítaných transakčných dát, aby sa zabezpečilo, že jets bežia v konštantnom čase.

Predpokladajme, že `sig-all-hash` nepoužíva efekt Reader. Predpokladajme, že sa nám nejako podarilo vybudovať typ Simplicity pre transakčné prostredie. Nazvime ho `TxEnv`, takže `sig-all-hash : TxEnv ⊢ 𝟚²⁵⁶` by bol typ jetu. Takáto definícia by vyžadovala, aby jet `sig-all-hash` dokázal vypočítať hash ľubovoľnej transakcie, nie iba transakcie, ktorej sa zúčastňuje. Programy Simplicity by mohli kopírovať dané `TxEnv` a odovzdať jeho upravenú kópiu do `sig-all-hash`. V takom prípade by sa `sig-all-hash` nemohol opierať o `PrecomputedTransactionData` a vrátili by sme sa k požiadavke lineárneho času vzhľadom na akékoľvek transakčné dáta odovzdané do tejto verzie `sig-all-hash`.

Pretože `sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` používa efekt Reader na prístup k transakčným dátam, získa prístup _iba_ k pevnému transakčnému prostrediu. Z tohto dôvodu môže implementácia jetu bezpečne používať `PrecomputedTransactionData` a pracovať v konštantnom čase.

### Cross-Input Signature Aggregation

Hoci ani Liquid, ani Bitcoin v tejto chvíli nepodporujú [cross-input signature aggregation](https://hrf.org/latest/cisa-research-paper/), chceli by sme skontrolovať, že Simplicity s ním môže byť kompatibilný, keď príde čas.

Hoci detaily ešte nie sú vypracované, predstavujeme si, že half-aggregation bude implementovaná pomocou efektu Writer. To znamená, že nový jet s typom ako `half-agg-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚²⁵⁶ ⊢ 𝟙` by vzal verejný kľúč, message digest a `r`-komponent Schnorrovho podpisu (Schnorrov podpis pozostáva z `r`-komponentu a `s`-komponentu) a pred pokračovaním vo vykonávaní by ho zapísal do transakčného logu. Potom by inde v transakcii alebo spolu s transakciou bol poskytnutý agregovaný `s`-komponent pre všetky half-aggregated Schnorrove podpisy. Transakcia by bola platná iba vtedy, keď by bol takýto agregovaný `s`-komponent poskytnutý pre všetky zalogované kľúče, správy a `r`-komponenty.

Aby sa splnili požiadavky Simplicity, tento efekt Writer musí byť idempotentný a komutatívny. To možno zabezpečiť tým, že sa writer log bude považovať za množinu n-tíc kľúč, správa, `r`-komponent. Funguje to preto, že množinové operácie sú idempotentné a komutatívne. Považovanie logu za množinu hodnôt by bolo kompatibilné s algoritmom overovania half-aggregation.

### Záver

V tejto kapitole sme sa pozreli na pridávanie vedľajších efektov do výpočtov, ktoré Simplicity dokáže robiť. Klasifikovali sme rôzne druhy efektov podľa toho, ako dobre sa správajú vzhľadom na rôzne druhy programových transformácií. Rozhodli sme sa obmedziť efekty Simplicity na tie, ktoré sú komutatívne a idempotentné.

Dva efekty, ktoré používame pre aplikácie Bitcoinu a Liquidu, sú efekt Reader na prístup k transakčnému prostrediu a efekt Failure na prerušenie a zlyhanie programu. Niektoré jets využívajú primitívne operácie, pri ktorých sa tieto druhy vedľajších efektov môžu objaviť.

Efekt Failure určuje výstup programu Simplicity: program buď zlyhá, čím urobí transakciu neplatnou, alebo program uspeje. Efekt Reader poskytuje jeden druh vstupu do programu Simplicity: prostredie obsahujúce transakčné dáta. Programom Simplicity však musíme poskytovať aj ďalšie vstupy, ako sú digitálne podpisy.

V nasledujúcej kapitole sa pozrieme na to, čo sú programy Simplicity, ako sa menia na adresy a ako do programov Simplicity pridávame ďalšie vstupy, napríklad podpisy.

## Programy a adresy

<chapterId>961652e3-8f7d-4c2a-8b55-9a990b91a0dd</chapterId>

V predchádzajúcej kapitole sme opísali dva vedľajšie efekty používané v Simplicity: efekt Failure, ktorý určuje úspech alebo zlyhanie programu, a efekt Reader, ktorý poskytuje prístup k transakčnému prostrediu. Teraz sa obrátime na praktickú otázku: čo presne je program Simplicity a ako sa z neho stane adresa na blockchaine?

### Programy Simplicity

Program Simplicity je definovaný ako výraz Simplicity typu `𝟙 ⊢ 𝟙`. Táto typová signatúra znamená, že program neprijíma žiadny zmysluplný vstup (iba jednotkovú hodnotu) a neprodukuje žiadny zmysluplný výstup (iba jednotkovú hodnotu). Efekt Reader zachytáva vstup transakčného prostredia, zatiaľ čo efekt Failure indikuje úspech alebo zlyhanie. Tieto efekty obsluhujú I/O, nie samotné typy Simplicity.

### Commitment Merkle Root

Namiesto ukladania kompletných programov on-chain Bitcoin používa záväzky — prax rozšírenú z Pay-to-Script-Hash (P2SH). Simplicity používa Commitment Merkle Root (CMR).

Každý kombinátor dostane SHA-256 tag odvodený zo vzoru: `Simplicity␟Commitment␟[identifier]`, kde `␟` reprezentuje ASCII kód 31 (oddeľovač jednotiek).

Každý tag je SHA-256 hash zodpovedajúceho pre-image reťazca uvedeného nižšie:

| Kombinátor | Pre-image tagu (ASCII reťazec) |
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

Výraz Simplicity sa potom rekurzívne hašuje do 256-bitového CMR výpočtom tagovaného SHA-256 midstate pre každý kombinátor spolu s CMR jeho argumentov (píšeme `#ᶜ(e)` pre CMR výrazu `e` a `∥` pre konkatenáciu bajtov):

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

Binárne kombinátory (`comp`, `pair`, `case`) konkatenujú CMR oboch potomkov; unárne kombinátory (`take`, `drop`, `injl`, `injr`) konkatenujú CMR svojho jediného potomka po 32 bajtoch výplne `0x00`; a nulárne listy (`iden`, `unit`) hašujú iba svoj tag. Dve konvencie udržiavajú tento výpočet lacný: používajú sa SHA-256 midstates, takže **každý výraz vyžaduje nanajvýš jedno volanie kompresnej funkcie SHA-256** (za predpokladu, že midstate po konštantné tagy je predpočítaný), a jednoargumentové konštruktory prefixujú svoj argument 32 bajtmi výplne `0x00`, čo implementáciám, ktoré to chcú, umožňuje trochu dodatočného predpočítania.

Pre kombinátor `unit` — nulárny konštruktor bez argumentových podvýrazov — sa toto pravidlo špecializuje na `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)`, kde `tag_unit = SHA-256(Simplicity␟Commitment␟unit)` (tag sa vloží dvakrát). Výsledné CMR pre triviálny program `unit` je:

```
0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

Kriticky, CMR sa nezaväzuje k typom výrazov Simplicity a namiesto toho sa spolieha na typovú inferenciu počas uplatnenia.

### Adresy

Adresy používajú Taproot mechanizmus BIP-0341 s CMR zaviazanými pod TapLeaf verziou `0xbe`. Proces zahŕňa:

1. Výpočet TapLeaf tagovaného hashu kombinujúceho bajt verzie, dĺžku CMR a samotné CMR
2. Tweaknutie interného verejného kľúča (použitím bodu NUMS, keď nie je želaná cesta míňania kľúčom)
3. Konverziu do formátu bech32m
4. Pridanie príslušných kontrolných súčtov

Keď nie je želaná cesta míňania kľúčom, interný verejný kľúč sa nastaví na bod **NUMS** ("Nothing-Up-My-Sleeve"): bod krivky zámerne zvolený tak, aby nikto nepoznal jeho diskrétny logaritmus — inými slovami, bod bez zodpovedajúceho súkromného kľúča. Pretože preň nikto nikdy nedokáže vytvoriť podpis, cesta míňania kľúčom je preukázateľne nepoužiteľná a výstup možno minúť *iba* cez zaviazanú scriptovú cestu Simplicity. V skutočnej aplikácii by sa tento bod NUMS mal randomizovať podľa odporúčania BIP-0341, aby výstupy bez cesty míňania kľúčom boli nerozlíšiteľné od bežných Taproot výstupov (prínos pre súkromie).

#### Od Simplicity k adrese

Prejdime si celú deriváciu pre najjednoduchší možný program: `unit : 𝟙 ⊢ 𝟙`, no-op, ktorý vždy uspeje.

**1. Tag kombinátora.** Najprv vypočítajte tag `unit`:

```
tag_unit = SHA-256(Simplicity␟Commitment␟unit)
         = 0xd723083cff3c75e29f296707ecf2750338f100591c86e0c71717f807ff3cf69d
```

**2. CMR.** Vložte tag dvakrát, aby ste získali CMR programu:

```
CMR = #ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)
    = 0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

**3. TapLeaf hash.** Prefixujte CMR TapLeaf verziou Simplicity `0xbe` a dĺžkou CMR `0x20` (32 bajtov), potom vezmite Elements TapLeaf tagovaný hash (tagovaný hash je `hash_str(x) = SHA-256(SHA-256(str) ∥ SHA-256(str) ∥ x)`):

```
hash_TapLeaf/elements(0xbe ∥ 0x20 ∥ CMR)
  = 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c
```

S týmto jediným listom neexistujú žiadne TapBranches, takže tento hash je už TapTree root.

**4. TapTweak.** Keďže nechceme cestu míňania kľúčom, použijeme BIP-0341 NUMS bod ako interný kľúč a tweakneme ho TapTree rootom:

```
internal_pk = 0x50929b74c1a04954b78b4b6035e97a5e078a5a0f28ec96d547bfee9ace803ac0
t = hash_TapTweak/elements(internal_pk ∥ 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c)
  = 0xb3bef172389b0937d7e5a8b15cfa41e776777f13f2f659cb06220a6ff0658285
```

**5. Výstupný kľúč.** Tweaknite interný kľúč na krivke, `output_pk = lift_x(internal_pk) ⊕ t·G` (elipticko-krivková aritmetika je tu zhrnutá), čím získate x-only výstupný kľúč `0x2cb0c20acd7340b4d4b65f6a60e2888d0d64e3267261f3b3cf7290e5af3f9e09`.

**6. Bech32m adresa.** Zakódujte x-only výstupný kľúč, prefixujte `p` (znak witness verzie SegWit v1), pridajte ľudsky čitateľný prefix Liquid testnetu `tex1` a pripojte kontrolný súčet Bech32m. Finálna adresa je:

```
tex1p9jcvyzkdwdqtf49kta4xpc5g35xkfcexwfsl8v70w2gwttelncyshxjk56
```

Bolo to veľa práce — ale veľká časť z nej je nariadená samotným Taprootom, nie Simplicity.

### Witness výrazy

Nový typ kombinátora rieši absenciu vstupu do programov Simplicity: witness výraz. Kombinátor `witness` umožňuje integrovať podpisové dáta a iný witness materiál do programov.

```
      w : B
-----------------
witness w : A ⊢ B
```

Sémantika witness výrazu je priamočiara: ignoruje svoj vstup a jednoducho vráti hodnotu `w` (ktorá môže mať ľubovoľný typ Simplicity), t. j. `⟦witness w⟧(a) = w`. Toto nepridáva **žiadnu novú vyjadrovaciu schopnosť** — podľa vety o úplnosti už Simplicity dokáže vybudovať ľubovoľnú takúto konštantnú funkciu (spomeňte si na makro `scribe` z predchádzajúcich kapitol). Zmysel kombinátora `witness` spočíva výlučne v jeho **CMR**: hodnota `w` je **vylúčená** z CMR výrazu, takže adresu možno vypočítať predtým, než je `w` známe, a `w` sa dodá v čase uplatnenia.

Táto návrhová voľba podporuje prerezávanie — nevykonané podmienené vetvy nemusia byť odhalené on-chain, vrátane ich priradených witness výrazov. Keď sa vetva prereže, overovateľ potrebuje iba CMR prerezaného podstromu, nie jeho skutočný obsah.

### Witness hodnoty

Môže sa zdať ako obmedzenie, že witness výraz môže držať iba *hodnotu*, a nie všeobecnejší výraz Simplicity. Programy pre UTXO-based blockchainy sa však vykonávajú iba raz. Nie je potrebné odovzdávať celý podvýraz do witness uzla: používateľ môže tento podvýraz jednoducho spustiť sám off-chain a prepísať jeho výstup do witness hodnoty, aby získal presne rovnaký výsledok.

(Neskôr v tomto kurze stretneme kombinátor `disconnect`, ktorý sa správa veľmi podobne ako witness výraz, ktorý *skutočne* berie celý výraz Simplicity ako svoj argument.)

Alternatívny návrh by privádzal všetky witness dáta ako argument do top-level programu Simplicity. Witness výrazy sa preferujú z dvoch dôvodov. Po prvé, **prerezávanie**: nevykonané vetvy výrazov `case` sa nikdy neodhaľujú on-chain a akékoľvek witness výrazy v týchto vetvách sa prerežú spolu s nimi. Po druhé, **lokalita**: witness výrazy nám umožňujú umiestniť každú witness hodnotu presne tam, kde sa používa, namiesto jej vláčenia z top-level vstupu programu.

### Typová inferencia

Keďže CMR sa nezaväzujú k typom, typový systém sa počas uplatnenia rekonštruuje. Algoritmus typovej inferencie Simplicity určuje minimálne typy pre každý podvýraz na základe štruktúry kombinátorov. Presnejšie, inferencia vypočíta *principal* (najvšeobecnejší) typ každého podvýrazu; všetky typové premenné, ktoré zostanú voľné, sa potom inštancujú na jednotkový typ `𝟙`, čím sa získa jedinečný, minimálny typ programu.

### Záver

V tejto kapitole sme ustanovili, že programy Simplicity sú výrazy typu `𝟙 ⊢ 𝟙`, vysvetlili sme, ako sa Commitment Merkle Roots konštruujú z tagovaných SHA-256 hashov každého kombinátora, a ukázali sme, ako sa CMR premieňajú na on-chain adresy cez BIP-0341 Taproot. Predstavili sme witness výrazy ako mechanizmus na poskytovanie podpisových dát a iných vstupov v čase míňania bez záväzku k ich hodnotám v čase vytvorenia adresy.

# Záverečná sekcia

<partId>96952535-4aa6-4e78-91e2-d12e9df895d4</partId>

## Recenzie a hodnotenia

<chapterId>fb0b0133-39ea-497b-bd36-198be42c4fab</chapterId>
<isCourseReview>true</isCourseReview>

## Záverečná skúška

<chapterId>2cc5e818-abcb-4a0a-9991-7a492c572e2d</chapterId>
<isCourseExam>true</isCourseExam>

## Záver

<chapterId>8ade24bd-a84f-4d25-8f64-bdfa8b58926c</chapterId>
<isCourseConclusion>true</isCourseConclusion>
