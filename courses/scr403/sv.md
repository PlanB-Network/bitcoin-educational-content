---
name: Fördjupning i Simplicity
goal: Bemästra designfilosofin, typsystemet och hela livscykeln för Simplicity
objectives:
  - Förstå de tre grundläggande sätten att kombinera beräkningar och de nio kombinatorer som utgör ett komplett språk
  - Bygg boolesk logik, aritmetik och SHA-256 från Simplicitys minimala typsystem
  - Greppa hur sidoeffekterna Failure och Reader möjliggör verklig interaktion med blockkedjan
  - Lär dig hur Simplicity-program blir Taproot-adresser och löses in med witnessdata
---

# Fördjupning i Simplicity

En djupdykning i teorin och designbesluten bakom språket Simplicity, baserad på den kompletta artikelserien i fem delar ["Delving Simplicity"](https://delvingbitcoin.org/t/delving-simplicity-part-three-fundamental-ways-of-combining-computations/1902) av [Dr. Russell O'Connor](https://r6.ca/), skaparen av Simplicity på Blockstream Research. Denna kurs förklarar *varför* Simplicity designades som det gjorde, inte hur man skriver det.

Kursen följer Dr. O'Connors artiklar genom de tre grundläggande sätten att kombinera beräkningar, det minimala typsystemet och dess fullständighetsteorem, konstruktionen av praktiska datatyper och aritmetik från grunden, den noggranna introduktionen av sidoeffekter för interaktion med blockkedjan, och slutligen hur program bekräftas till adresser och löses in on-chain.

+++

# Introduktion

<partId>c362889b-c630-435f-911b-724c4eca505b</partId>

## Kursöversikt

<chapterId>cdcc40b6-c985-45b4-9bee-6f931e984476</chapterId>

Välkommen till SCR403 — Fördjupning i Simplicity!

Denna kurs bygger på artikelserien **"Delving Simplicity"**, skriven av [Dr. Russell O'Connor](https://r6.ca/), Infrastructure Tech Developer på [Blockstream](https://blockstream.com/) och skaparen av Simplicity. De ursprungliga artiklarna publicerades på forumet [Delving Bitcoin](https://delvingbitcoin.org/u/roconnor-blockstream/summary) och utgör det primära källmaterialet för denna kurs. Vi är tacksamma för hans banbrytande arbete, som gjort detta utbildningsinnehåll möjligt.

### Vad du kommer att lära dig

Denna kurs utforskar designfilosofin och de matematiska grunderna bakom Simplicity, nästa generations skriptspråk som aktiverades på [Liquid Network](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/) i juli 2025. Den följer den kompletta artikelserien i fem delar och är strukturerad i två huvudavsnitt:

1. **Simplicitys grunder** — Varför beräkning på en blockkedja kräver ett fundamentalt annorlunda språk, de tre sätten att kombinera operationer (sekventiellt, parallellt, villkorat) och de nio kärnkombinatorerna som bildar ett matematiskt komplett språk
2. **Från datatyper till program** — Att bygga boolesk logik, aritmetik och SHA-256 från grunden; att förstå sidoeffekterna Failure och Reader som möjliggör interaktion med blockkedjan; och att lära sig hur program bekräftas till Taproot-adresser via Commitment Merkle Roots och löses in med witnessdata

### Förkunskaper

Detta är en kurs på **expertnivå** (cirka 10 timmar). Du bör vara bekväm med:
- Grundläggande koncept inom Bitcoin-skript (vad transaktionsvalidering gör)
- Grundläggande programmeringskoncept (typer, funktioner, komposition)
- Viss förtrogenhet med matematisk notation är till hjälp men inte ett krav. Vi introducerar allt allteftersom

### Nyckelresurser

- **Ursprungliga artiklar**: ["Delving Simplicity"](https://delvingbitcoin.org/u/roconnor-blockstream/summary) av Dr. Russell O'Connor på Delving Bitcoin
- **Simplicity-repositoriet**: [BlockstreamResearch/simplicity](https://github.com/BlockstreamResearch/simplicity) — källkod och formella Rocq-bevis
- **Officiell webbplats**: [simplicity-lang.org](https://simplicity-lang.org/) — dokumentation och referens för SimplicityHL
- **Blockstream-bloggen**: [Simplicity on GitHub](https://blog.blockstream.com/en-simplicity-github/) — teknisk översikt

Redo att dyka ner i en av de mest eleganta delarna av Bitcoin-ingenjörskonst? Nu kör vi!

## Vad är Simplicity?

<chapterId>d04f3960-d7fb-44e1-b5a3-25b33d03fd38</chapterId>

Om du kommer till denna kurs utan bakgrund i Simplicity kommer detta kapitel att orientera dig innan vi dyker ner på djupet.

### Simplicity i ett nötskal

Simplicity är ett **Bitcoin-nativt smart contract-språk**, live på Liquid Network idag. Det föreställdes ursprungligen av Dr. Russell O'Connor omkring 2012 och beskrevs i detalj i hans artikel från 2017, *Simplicity: A New Language for Blockchains*, och aktiverades på Liquid Network i juli 2025 efter åratal av formell verifiering och utveckling.

Till skillnad från Ethereums Solidity, som är ett Turing-komplett, högnivå kontraktsspråk, är Simplicity avsiktligt minimalt. Det har:
- **Tre typkonstruktorer** (unit, sum, product)
- **Nio kombinatorer** (grundoperationer och kompositionsregler)
- **Inga loopar, ingen rekursion, inget dynamiskt minne**

Utifrån bara dessa primitiver kan man bygga vilken beräkning som helst som behövs för transaktionsvalidering, från boolesk logik till fullständig SHA-256-hashning.

### Vad kan man göra med Simplicity idag?

Simplicity driver redan verkliga applikationer på Liquid Network. Den mest anmärkningsvärda är [Simplicity DEX](https://docs.simplicity-lang.org/use-cases/simplicity-dex/), en orakelfri marknadsplats för optioner där användare handlar köpoptioner på L-BTC med USDt som säkerhet (det underliggande kontraktet stöder även säljoptioner). Andra aktiva Simplicity-projekt inkluderar [Swaption](https://swaption.io/) från SideSwap (optioner) och det öppna källkodsprojektet [Deadcat](https://github.com/Resolvr-io/deadcat) från Resolvr (prediktionsmarknader). Utöver DeFi möjliggör Simplicity avancerade utgiftsvillkor som vaults, covenants och komplexa multisig-scheman som skulle vara omöjliga eller osäkra i Bitcoin Script.

### Vad denna kurs är — och inte är

Detta är **inte** en praktisk kodningstutorial. Du kommer inte att skriva Simplicity-program här. Om du letar efter det, kolla in:
- [simplicity-lang.org](https://simplicity-lang.org/) — officiell dokumentation och högnivåspråket SimplicityHL
- [Simplicitys GitHub-repositorium](https://github.com/BlockstreamResearch/simplicity) — referensimplementation, exempel och Rocq-bevis
- [Blockstream-blogginlägget](https://blog.blockstream.com/en-simplicity-github/) om att komma igång

Vad denna kurs **handlar om**: de **filosofiska och tekniska val** som ligger bakom Simplicitys design. Varför skapades detta språk på detta sätt? Varför bara nio kombinatorer? Varför ingen rekursion? Varför spelar det roll att typsystemet ansluter till Gentzens sekvenskalkyl?

Se det som att förstå **varför motorn byggdes på detta sätt** snarare än att lära sig köra bilen.

### Vem är detta för?

Denna kurs är idealisk för:
- **Protokollutvecklare** som vill förstå Simplicitys grunder innan de skriver kod
- **Bitcoin-forskare** intresserade av det formella verifierings- och typteoretiska tillvägagångssättet
- **Datavetare** nyfikna på kopplingen mellan sekvenskalkyl och beräkning på en blockkedja
- **Avancerade bitcoiners** som vill gå bortom en ytlig förståelse av Liquids skriptkapacitet

Om termer som "summtyper", "kombinatorer" eller "sekvenskalkyl" är helt nya för dig, oroa dig inte — vi förklarar allt från grunden. Men var beredd på en tät, matematisk resa.

### Från artiklar till kurs

Den ursprungliga "Delving Simplicity"-serien av Dr. O'Connor är strukturerad som fem tekniska artiklar. Denna kurs omorganiserar och kommenterar det materialet till en progressiv inlärningsväg med quiz som testar din förståelse längs vägen. Idéerna, definitionerna och bevisen är hans, och vi har anpassat formatet för strukturerad utbildning.

# Simplicitys grunder

<partId>a5976618-94ab-4b29-b9aa-040d35c68e5d</partId>

## Grundläggande sätt att kombinera beräkningar

<chapterId>6d46e77a-7e60-473b-b230-418da5ae44eb</chapterId>

Nu när Simplicity har aktiverats på Liquid Network vill jag göra en djupdykning i filosofin och designen bakom Simplicity-språket.

Bitcoins transaktionsvalidering är en väsentligt annorlunda tillämpning än vanlig design av programmeringsspråk. Block space är en bristvara så programmen måste vara kompakta. Programmen i Bitcoin-transaktioner körs bara någonsin på en enda input, och alla kör programmet på samma input. Dessutom vet den agent som auktoriserar transaktionen redan resultatet av beräkningen i förväg: att transaktionen är giltig.

Vanligtvis kör den auktoriserande agenten mycket dyrare beräkningar för att härleda witnessdata som intygar transaktionens giltighet, medan program som körs på blockkedjan behöver kontrollera witnessdatans giltighet. Att kontrollera giltighet är ofta mycket billigare än att bevisa giltighet.

Vi har designat Simplicity med denna typ av unika utmaningar inom språkdesign i åtanke. Till exempel kräver Simplicity att icke-exekverade grenar beskärs så att de inte förekommer på blockkedjan. Förbehandlingssteg är noggrant designade för att uppvisa (kvasi-)linjär tidskomplexitet i storleken på Simplicity-programmet. Statisk analys används istället för "gas", som inte kan beräknas utan att exekvera kod på ett föreskrivet sätt, så att detaljerna i exekveringsmodellen inte blir konsensuskritiska. Ingen dynamisk minnesallokering under exekvering. Och så vidare.

Innan vi går in på designdetaljerna för Simplicity vill jag inleda denna serie med lite programmeringsfilosofi om de generella sätten att kombinera grundläggande byggstenar för att skapa ny funktionalitet.

### Komposition

Anta att man designar ett språk för programmerbara transaktioner för en blockkedja som Bitcoin. I synnerhet har program bara tillgång till transaktionsdatan och UTXO-datan för indata, och exekvering avgör enbart transaktionens giltighet (vilket gör att resultatet av exekveringen kan cachas). Låt oss säga att man börjar med en uppsättning grundoperationer som kan utföra olika uppgifter, såsom grundläggande beräkningar, läsning och/eller bearbetning av data från transaktionen, och signaturverifiering. Varje operation konsumerar någon typ av indata (möjligen tom) och returnerar någon typ av utdata. Vilka sätt finns det att kombinera dessa grundoperationer till mer komplexa operationer?

### Sekventiell komposition

![Sekventiell komposition](assets/en/001.webp)

Den mest grundläggande kompositionsmetoden är sekventiell komposition. Om vi har två grundoperationer, där den ena outputens datatyp matchar den andras inputs datatyp, kan vi kombinera dessa två operationer till en ny sammansatt operation. Denna nya operation kör dessa två grundoperationer i sekvens, tar den första operationens input som input, för in den första operationens output i den andra operationens input, och returnerar slutligen den andra operationens output.

Naturligtvis behöver vi inte begränsa oss till att bara kombinera grundoperationer. Nu när vi har några sammansatta operationer kan vi kombinera dessa med funktionell komposition också.

Inom matematiken kallas denna sekventiella komposition ofta bara "komposition", och man kan tro att detta är det enda sättet att komponera saker på. Vi har dock andra sätt att komponera operationer.

### Parallell komposition

![Parallell komposition](assets/en/002.webp)

Anta att vi har två operationer — de kan vara grundoperationer eller komplexa operationer — och att de båda tar samma typ av input. Ett andra grundläggande sätt att komponera dessa två operationer är att exekvera dem båda på samma input. Detta kallas parallell komposition, och outputens typ är "produkten" av typerna för de ursprungliga operationernas output och innehåller paret av de två utdatavärdena.

Även om detta kallas "parallell" komposition, och de två operationerna i princip skulle kunna exekveras parallellt, är parallell exekvering inget operationellt krav. Vi kan implementera parallell komposition "sekventiellt" genom att exekvera den ena operationen först och sedan den andra. Vi bryr oss inte om detaljerna i hur parallell komposition implementeras, så länge som utdatan blir densamma.

### Villkorad komposition

![Villkorad komposition](assets/en/003.webp)

Villkorad komposition är dualen till parallell komposition. I detta fall har vi två operationer som producerar samma output, och vi komponerar dem genom att välja vilken av dem som ska exekveras. Inputen till denna sammansatta operation är "summan" eller den "taggade unionen" av typerna för de ursprungliga operationernas input. I detta fall är taggen, "Left" eller "Right", en enda bit i inputens data som avgör vilken typ av data som bärs, och därmed vilken av de två operationerna som kan exekveras.

Villkorad komposition fungerar på samma sätt även när inputen är summan av två identiska typer. Summtypen innehåller fortfarande en tagg, och värdet på den taggen avgör vilken av de två operationerna som ska exekveras.

### Komposition i Bitcoin Script

Det finns många sätt att förverkliga dessa tre former av komposition i olika programmeringsspråk. I Bitcoin Script förverkligas sekventiell komposition (ungefär) genom konkatenering av två rutiner (det är därför Bitcoin Script kallas ett konkatenativt programmeringsspråk), eftersom utdatan från en rutin lämnas kvar på stacken för att konsumeras av den efterföljande rutinen. Parallell komposition uppnås genom användning av dupliceringar och swap-operationer för att manipulera stacken så att två rutiner kan köras på samma input. Saken är inte helt okomplicerad, eftersom det vi kallar "produkten" av typer vanligtvis förverkligas genom att använda flera stackelement. Förhoppningsvis ser du den generella idén.

Villkorad komposition förverkligas naturligtvis av `OP_IF`, som förgrenar sig baserat på värdet på stacken. I detta fall spelar det översta stackelementet rollen som en tagg, och vanligtvis är nästa element eller element på stacken av olika "typer" beroende på taggens värde. I varje fall kan stackelementens typer bara vara lämpliga för bearbetning av en av grenarna i `OP_IF`. Efter att vi når `OP_ENDIF` måste dock stackelementen ha en konsekvent "typ", så att det återstående skriptet kan fortsätta oberoende av vilken gren som tidigare togs.

### Komposition i Simplicity

Vi designade Simplicity med kombinatorer som direkt implementerar dessa tre former av komposition. Tillsammans med några ytterligare kombinatorer för att stödja andra grundoperationer relaterade till produkt- och summtyperna, består Simplicitys kärnspråk till slut av nio kombinatorer som är tillräckliga för att uttrycka vilken ändlig beräkning som helst. Vi kommer att diskutera detta mer i detalj i nästa kapitel.

### En fjärde typ av komposition

Innan vi avslutar bör vi nämna att det finns åtminstone ytterligare en typ av komposition inom datavetenskapen, nämligen "rekursiv komposition". Vid rekursiv komposition itereras en operation flera gånger.

Observera att Bitcoin Script inte stöder rekursiv komposition, och på samma sätt har vi uttryckligen uteslutit obegränsad rekursion från Simplicitys design. Vår tes är att obegränsad iterativ beräkning bättre implementeras med hjälp av rekursiva covenants som beräknar över flera transaktioner. Detta gör det möjligt för användare att undvika begränsningar i block space och standardness, samt att bättre förutsäga transaktionskostnader.

Det sagt finns det sätt att missbruka Simplicitys delegeringsfunktion för att åstadkomma något som liknar obegränsad rekursiv komposition, vilket vi kanske kommer att diskutera senare i denna serie.

### Slutsats

Vi gick igenom de tre huvudsakliga formerna av komposition för att omvandla grundoperationer till komplexa operationer:

- sekventiell komposition
- parallell komposition
- villkorad komposition

Vi diskuterade hur dessa kompositionsformer förverkligas i Bitcoin Script, och antydde hur de har påverkat designen av Simplicity-språket. Vi konstaterade att den fjärde typen av komposition, rekursiv komposition, uttryckligen är utesluten från både Simplicity och Bitcoin Script.

I nästa kapitel beskriver vi de nio kombinatorer som utgör kärnan i Simplicity-språket, hur de direkt förverkligar dessa tre former av komposition, och hur detta bildar ett komplett språk för att beskriva vilken ändlig beräkning som helst.

## Simplicitys kombinatoriska fullständighet

<chapterId>2a10a6ba-fada-4556-a673-3ae8c0794bf0</chapterId>

I detta kapitel introducerar vi Simplicitys kärnspråk och visar att språket är fullständigt, det vill säga att vilken ändlig beräkning som helst kan uttryckas inom det.

### Simplicity-typer

Simplicity stöder tre grundläggande typkonstruktorer. Produkttypen `A × B` representerar utdata från parallell komposition, medan summtypen `A + B` (taggad union) hanterar indata för villkorad komposition. Den tredje typen är unit-typen.

### Unit-typen

Unit-typen, betecknad `𝟙` eller `ONE`, innehåller exakt ett värde: den tomma tupeln `⟨⟩` eller `()`. Denna nollbitars datatyp bär ingen information.

### Summtypen

En summtyp `A + B` kombinerar två typer med taggar som anger "vänster" eller "höger". Värden skrivs som `σᴸ(a)` eller `inl(a)` för vänstertaggade värden och `σᴿ(b)` eller `inr(b)` för högertaggade värden. Taggarna förblir distinkta även när identiska typer kombineras.

#### Den booleska typen

Typen `𝟙 + 𝟙`, betecknad `𝟚` eller `TWO`, representerar en enbitars typ med två värden. Enligt konvention representerar `σᴸ⟨⟩` falskt/noll, medan `σᴿ⟨⟩` representerar sant/ett.

### Produkttypen

Produkttyper `A × B` innehåller värdepar skrivna som `⟨a, b⟩` eller `(a, b)`. Typen `𝟚 × 𝟚` har fyra värden, distinkta från de fyra värdena i `𝟚 + 𝟚`.

### Simplicitys kärnuttryck

Operationer betecknas som `f : A ⊢ B`, vilket betyder input-typ `A` och output-typ `B`. Simplicity är "första ordningens" — det saknar funktionstyper.

### Två grundoperationer

Kärnspråket tillhandahåller två grundoperationer:

**Identitet (`iden`).** Identitetsoperationen släpper igenom sin input oförändrad:

```
iden : A ⊢ A
⟦iden⟧(a) = a
```

**Unit (`unit`).** Unit-operationen kasserar sin input och returnerar den tomma tupeln:

```
unit : A ⊢ 𝟙
⟦unit⟧(a) = ⟨⟩
```

Dessa bildar familjer med en operation per typ.

### Tre kompositionskombinatorer

Sekventiell komposition använder `comp f g` (skrivs `f ⨾ g` eller `f >>> g`):

```
If f : A ⊢ B and g : B ⊢ C, then
comp f g : A ⊢ C
⟦f ⨾ g⟧(a) = ⟦g⟧(⟦f⟧(a))
```

Parallell komposition använder `pair f g` (skrivs `f ▵ g` eller `f &&& g`):

```
If f : A ⊢ B and g : A ⊢ C, then
pair f g : A ⊢ B × C
⟦f ▵ g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩
```

Villkorad komposition använder `case f g : (A + B) × C ⊢ D`, vilket ger grenarna tillgång till en delad omgivning `C`:

```
If f : A × C ⊢ D and g : B × C ⊢ D, then
case f g : (A + B) × C ⊢ D
⟦case f g⟧⟨σᴸ(a), c⟩ = ⟦f⟧⟨a, c⟩
⟦case f g⟧⟨σᴿ(b), c⟩ = ⟦g⟧⟨b, c⟩
```

Varför tar villkorad komposition denna form — en summa parad med en delad omgivning `C` — istället för en enklare `copair f g : A + B ⊢ C` som bara väljer en gren? Eftersom en ren `copair` inte kan uttrycka **distribution**: funktionen `dist : (A + B) × C ⊢ A × C + B × C` som skjuter in en delad input i vilken gren som än tas. Genom att bygga in omgivningen `C` direkt i `case` får Simplicity både villkorad komposition *och* distribution från en enda kombinator — ett av de nyckelbeslut i designen som håller kärnspråket nere på nio kombinatorer.

### Fyra kombinatorer till

Produktkonsumtion använder `take` och `drop`:

**take** extraherar det vänstra elementet:

```
If f : A ⊢ C, then
take f : A × B ⊢ C
⟦take f⟧⟨a, b⟩ = ⟦f⟧(a)
```

**drop** extraherar det högra elementet:

```
If f : B ⊢ C, then
drop f : A × B ⊢ C
⟦drop f⟧⟨a, b⟩ = ⟦f⟧(b)
```

Summproduktion använder `injl` och `injr`:

**injl** omsluter med en vänstertagg:

```
If f : A ⊢ B, then
injl f : A ⊢ B + C
⟦injl f⟧(a) = σᴸ(⟦f⟧(a))
```

**injr** omsluter med en högertagg:

```
If f : A ⊢ C, then
injr f : A ⊢ B + C
⟦injr f⟧(a) = σᴿ(⟦f⟧(a))
```

### De nio kärnkombinatorerna

Totalt sett har Simplicity exakt nio kärnkombinatorer:

| Kombinator | Syfte |
|---|---|
| `iden` | Släpper igenom input |
| `unit` | Kasserar input |
| `comp` | Sekventiell komposition |
| `pair` | Parallell komposition |
| `case` | Villkorad komposition |
| `take` | Extraherar vänster element ur produkt |
| `drop` | Extraherar höger element ur produkt |
| `injl` | Injicerar i vänster del av summa |
| `injr` | Injicerar i höger del av summa |

### Simplicity och sekvenskalkylen

Simplicitys design härleds från det konjunktiv-disjunktiva fragmentet av Gentzens sekvenskalkyl. Mer precist är det en variant av sekvenskalkylens *funktionella tolkning*, som i sig är analog med Curry-Howard-korrespondensen mellan naturlig deduktion och lambdakalkylen. Kombinatorreglerna uppvisar "mindre typer i premisserna än i slutsatserna", vilket gör det möjligt för Bit Machine — Simplicitys abstrakta stackmaskintolk — att minimera datakopiering under exekvering.

### Värden är inte uttryck

Simplicity-uttryck betecknar operationer, inte värden. Notationen `scribe b : A ⊢ B` representerar ett unikt uttryck som alltid returnerar värdet `b`, och fungerar som ett notationsmässigt bekvämlighetsverktyg snarare än en kombinator. Detta speglar Bitcoin Script, där operationer som `OP_1` skjuter värden på stacken snarare än att uttrycka dem direkt.

### Simplicitys fullständighetsteorem

Med alla nio kombinatorer i handen, hur vet vi att vi inte saknar något — att dessa nio verkligen räcker? Simplicitys fullständighetsteorem svarar på detta: för varje funktion mellan (ändliga) Simplicity-typer finns det något Simplicity-uttryck som betecknar den. Beviset är konstruktivt — det visar hur man bygger uttrycket:

1. **Dekomponera inputen**: Använd nästlade `case`-uttryck för att fullständigt dekomponera vilken input som helst, av vilken typ som helst, till dess beståndsdelar av bitar
2. **Bygg en uppslagstabell**: För varje möjlig input, använd `scribe` för att producera motsvarande output
3. **Sätt ihop**: De nästlade case- och scribe-uttrycken bildar tillsammans en jättelik uppslagstabell som implementerar funktionen

Detta teorem är formellt verifierat i bevisassistenten Rocq (tidigare Coq). Beviset är en del av det officiella Simplicity-repositoriet och har maskinkontrollerats för korrekthet.

Även om fullständighetsteoremet garanterar att Simplicitys nio kombinatorer kan uttrycka vilken funktion som helst mellan (ändliga) Simplicity-typer, blir de resulterande uttrycken från uppslagstabellskonstruktionen opraktiskt stora. En funktion på 256-bitars input skulle kräva en uppslagstabell med 2²⁵⁶ poster. Det är därför nästa kapitel fokuserar på att bygga effektiva uttryck som utnyttjar beräkningarnas struktur, snarare än att brute-forcea allt genom uppslagstabeller.

### Slutsats

Simplicitys kärnspråk innehåller ett typsystem och kombinatorer som möjliggör vilken ändlig beräkning som helst. Även om fullständighetsteoremet garanterar uttrycksfullhet är de resulterande uttrycken från den generiska konstruktionen opraktiskt stora. Praktisk Simplicity-utveckling handlar om att utnyttja beräkningsstruktur för att få kortfattade uttryck. Nästa kapitel utforskar datastrukturer, transaktionsinteraktioner och ytterligare kombinatorer.

# Från datatyper till program

<partId>08528a6f-d310-4675-b8cd-4e9b93b3c009</partId>

## Att bygga datatyper

<chapterId>9981ae62-ae50-4770-adf2-b253d1e08de3</chapterId>

I de föregående kapitlen visade vi hur Simplicitys kärnuppsättning av kombinatorer räcker för att implementera vilken ändlig, ren beräkning som helst. Detta kapitel visar hur man bygger praktiska datastrukturer och beräkningar utifrån dessa primitiver — på samma sätt som datorer byggs från logiska grindar.

### Boolesk logik

Den booleska typen, betecknad `𝟚`, är lika med `𝟙 + 𝟙` och har två värden: `σᴸ⟨⟩` (falskt) och `σᴿ⟨⟩` (sant). Med hjälp av kärnkombinatorerna kan booleska logikoperatorer konstrueras.

#### And-operationen

Den logiska operationen `and : 𝟚 × 𝟚 ⊢ 𝟚` tar två bitar och returnerar en bit. Implementationen förgrenar sig på den första biten: om falsk, returnera falskt; annars, returnera den andra biten.

```
and ≔ case (injl unit) (drop iden) : 𝟚 × 𝟚 ⊢ 𝟚
```

Testar med `⟨false, false⟩`:

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

Testar med `⟨true, true⟩`:

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

#### Andra logikoperationer

Operationen `not` kräver en hjälpkombinator:

```
                   f : A ⊢ C    g : B ⊢ C
--------------------------------------------------------------
copair f g ≔ iden ▵ unit ⨾ case (take f) (take g) : A + B ⊢ C
```

Den inledande `iden ▵ unit : A ⊢ A × 𝟙` lägger till en tom "omgivning" till inputen, vilket gör det möjligt för `case`-kombinatorn att tillämpas. Användningen av `take` i de två grenarna tar bort denna tomma omgivning för att exekvera `f` eller `g`.

Andra booleska logikoperationer:

- `or ≔ case (drop iden) (injr unit) : 𝟚 × 𝟚 ⊢ 𝟚`
- `not ≔ copair (injr unit) (injl unit) : 𝟚 ⊢ 𝟚`
- `xor ≔ case (drop iden) (drop not) : 𝟚 × 𝟚 ⊢ 𝟚`

### Bitadderare

En "halvadderare" tar två bitar och adderar dem, vilket ger en tvåbitars output: en carry-bit och en summa-bit.

```
half-adder ≔ and ▵ xor : 𝟚 × 𝟚 ⊢ 𝟚 × 𝟚
```

En "heladderare" adderar tre bitar och ger en tvåbitars output. Inputen använder den nästlade tupeln `(𝟚 × 𝟚) × 𝟚`.

För nästlade tupler används kompakt notation:

- `O f` betecknar `take f`
- `I f` betecknar `drop f`
- `H` betecknar `iden`

Till exempel betyder `I O H` `drop (take iden) : A × (B × C) ⊢ B`, vilket extraherar mittvärdet. Notationen anspelar på binära siffror: när man tänker på nästlade tupler som binära träd representerar notationen omvända binära siffror för trädpositioner. Dessa uttryck bildar De Bruijn-index för Simplicity.

**Observera:** `I`-, `O`- och `H`-notationen gäller endast för deluttryck som enbart består av `take`, `drop` och `iden`.

Heladderaren komponerar två halvadderare, och tar den logiska `or`-operationen av carry-bitarna:

```
full-adder ≔ take half-adder ▵ I H
           ⨾ O O H ▵ (O I H ▵ I H ⨾ half-adder)
           ⨾ (O H ▵ I O H ⨾ or) ▵ I I H
           : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × 𝟚
```

I den första raden kör `take half-adder ▵ I H : (𝟚 × 𝟚) × 𝟚 ⊢ (𝟚 × 𝟚) × 𝟚` halvadderaren på de två första bitarna, och sparar den sista biten.

I den andra raden sparar `O O H ▵ (O I H ▵ I H ⨾ half-adder) : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × (𝟚 × 𝟚)` den första biten (carry-out från den första halvadderaren) och kör halvadderaren på de två sista bitarna.

I den sista raden tar `(O H ▵ I O H ⨾ or) ▵ I I H: 𝟚 × (𝟚 × 𝟚) ⊢ 𝟚 × 𝟚` den logiska OR-operationen av de två första bitarna (carry-out från båda halvadderarna) och returnerar summa-out-biten från den andra halvadderaren.

Detta demonstrerar Simplicity-programmering: att använda notationen `I`, `O` och `H` för att referera till databitar, och bilda lämpliga "omgivningar" för att anropa andra funktioner via sekventiell komposition.

Användare definierar inte lågnivåoperationer direkt. Senare i denna serie diskuteras standardbiblioteks-jets som implementerar vanliga funktioner. Slutanvändare förväntas inte programmera direkt i Simplicity, på samma sätt som med Bitcoin Script. Istället genererar högnivåspråk som SimplicityHL Simplicity-kod, hanterar deluttryckens "omgivningar" och översätter namngivna variabler till lämpliga sekvenser av `take` och `drop`.

### Vektorer

Fasta vektorer definieras genom att bilda itererade produkter av typen `A`:

- `A² ≔ A × A`
- `A⁴ ≔ A² × A²`
- `A⁸ ≔ A⁴ × A⁴`
- `…`

Dessa kan skrivas som `A^2`, `A^4`, `A^8`, etc.

Vektorer är endast definierade för längder som är tvåpotenser. Andra potenser kräver att man väljer parenteseringskonventioner.

Givet uttrycket `f : A ⊢ B`, "mappar" upprepad parning det över vektorer med fast längd:

- `f² ≔ f ▵ f : A² ⊢ B²`
- `f⁴ ≔ f² ▵ f² : A⁴ ⊢ B⁴`
- `f⁸ ≔ f⁴ ▵ f⁴ : A⁸ ⊢ B⁸`

Givet funktionen `f : A × B ⊢ B`, iteration eller "vikning" över vektorer med fast längd:

- `fold-right-2 f ≔ O O H ▵ (O I H ▵ I H ⨾ f) ⨾ f : A² × B ⊢ B`
- `fold-right-4 f ≔ fold-right-2 (fold-right-2 f) : A⁴ × B ⊢ B`
- `fold-right-8 f ≔ fold-right-2 (fold-right-4 f) : A⁸ × B ⊢ B`

Många varianter finns. Givet `f : A × B ⊢ C`, "zippa" över parade vektorer med `zip-n f : (Aⁿ × Bⁿ) ⊢ Cⁿ`. Givet `f : (A × B) × C ⊢ C`, vik över parade vektorer med `bifold-right-n f : (Aⁿ × Bⁿ) ⊢ C`. Genom att kombinera `map` och `fold-right` skapas ackumulerande kombinatorer: `f : A × C ⊢ C × B` ger `map-accum-right-n f : Aⁿ × C ⊢ C × Bⁿ`. Många fler varianter är möjliga.

#### Multibitsord

En bitvektor ger multibitsheltal. Till exempel är `𝟚³²` en 32-bitars ordtyp. `𝟚²⁵⁶` är en 256-bitars ordtyp, lämplig för hashar och kryptografiska operationer.

Med hjälp av heladderaren definierar en variant av vektoroperationer en "carry ripple-adderare" över multibitsord:

```
full-adder-n ≔ zip-accum-right-n full-adder : (𝟚ⁿ × 𝟚ⁿ) × 𝟚 ⊢ 𝟚 × 𝟚ⁿ
```

`full-adder-n` tar två n-bitars binära tal och en enbitars carry-input, och returnerar en enbitars carry-out-flagga och en n-bitars summa.

#### SHA-256

Genom att rekursivt definiera aritmetiska operationer på multibitsord — subtraktion, multiplikation, division — och bitvisa logiska operationer som logisk AND, OR, XOR, och genom att upprepade gånger kombinera dessa, kan även SHA-256:s blockkomprimeringsfunktion byggas:

```
sha256-hash-block ≔ … : 𝟚²⁵⁶ × 𝟚⁵¹² ⊢ 𝟚²⁵⁶
```

SHA-256-komprimeringen är formellt definierad med Simplicity inom bevisassistenten Rocq (tidigare Coq), med ett formellt bevis på att implementationen av `sha256-hash-block` är korrekt.

Komprimeringen körs för långsamt som rå Simplicity. Jets exekverar vanliga funktioner som SHA-256-komprimering nativt. Rena Simplicity-implementationer fungerar som formella specifikationer för jets.

### Options-typer

Options-typer skapas genom att ta en summa med unit-typen:

```
Option A ≔ 𝟙 + A
```

Typen `Option A` kan skrivas som `A?` eller `𝕊 A` (där `𝕊` betyder "efterföljare"). Funktioner mappar över options-typer:

```
                 f : A ⊢ B
------------------------------------------
f? ≔ copair (injl unit) (injr f) : A? ⊢ B?
```

Monadiska kombinatorer som bind kan definieras:

```
              f : A ⊢ B?
---------------------------------------
bind f ≔ copair (injl unit) f : A? ⊢ B?
```

### Buffertar med variabel längd

"Buffertar" är typer för delvis fyllda vektorer:

- `Aᑉ² ≔ A?`
- `Aᑉ⁴ ≔ A²? × Aᑉ²`
- `Aᑉ⁸ ≔ A⁴? × Aᑉ⁴`
- `…`

Typen `Xᑉ⁸` expanderar till `(1 + X⁴) × ((1 + X²) × (1 + X))`. Om man behandlar detta som ett polynom och expanderar det, får man `1 + X + X² + X³ + X⁴ + X⁵ + X⁶ + X⁷`. Tolkat som en typ representerar det summan av alla möjliga tupler av X upp till 7, inklusive den tomma tupeln. Detta är exakt typen för listor med längd strikt mindre än 8.

Precis som med vektorer kan mappnings- och vikningsoperationer definieras över buffertar. Stackoperationer inkluderar `push-<n : Aᑉⁿ × A ⊢ Aⁿ + Aᑉⁿ` och `pop-<n : Aᑉⁿ ⊢ (Aᑉⁿ × A)?`. `push-<n` lägger till ett element i bufferten och returnerar en fullständig vektor om overflow uppstår. `pop-<n` tar bort ett element och returnerar den mindre bufferten och det borttagna elementet, och returnerar eventuellt ingenting om den ursprungliga bufferten var tom.

Definitionen av `push-<n`, rekursivt:

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

Rå Simplicity blir svår att följa bortom vissa komplexitetsnivåer. Slutanvändare använder högnivåspråk som SimplicityHL, som genererar dessa idiomatiska uttryck.

### Slutsats

Detta kapitel visade hur man bygger logiska operationer från bitar. Utifrån dessa uppstod bitnivå-aritmetik, vilket möjliggör resonemang om exekvering. Vektortyper utvecklades, vilket demonstrerade iteration över multibitsord för att definiera aritmetik. Fortsättningsvis kan kryptografiska operationer som SHA-256 och validering av Schnorr-signaturer definieras enbart med Simplicity-kombinatorer — allt faktiskt definierat med hjälp av Simplicity.

Detta kapitel är inte en heltäckande guide till alla möjliga datatyper och operationer som kan byggas i Simplicity, men illustrerar hur man uppnår praktisk funktionalitet inom Simplicitys begränsningar. Trots ändligt begränsade typer kan användbara vektorer, buffertyper och operationer som itererar över dessa strukturer definieras.

Faktiska specifikationer för standardbiblioteksoperationer skiljer sig något från definitionerna här. Heladderaren använder till exempel en 3-vägs XOR och en "majoritets"-logikfunktion istället för två halvadderare.

I praktiken använder Simplicity-program jets för aritmetiska och kryptografiska operationer. Jets ersätter dock bara uttryck. Kombinatorer som itererar över buffertar och vektorer kan inte ersättas av jets, och förekommer i faktiska Simplicity-program. Istället för att använda dessa direkt använder slutanvändare dock högnivåspråk som SimplicityHL, som genererar sådana uttryck.

Rekursivt definierade kombinatorer tycks växa exponentiellt i uttryckets storlek. Detta är inte något problem. Vid serialisering kodas uttryck som DAG:ar (riktade acykliska grafer) snarare än som träd. Den faktiska representationen växer bara linjärt.

Hittills har vi bara behandlat rena beräkningar. Interaktion med transaktionsdata för uppgifter som att signera transaktioner kräver något sätt för program att misslyckas om signaturer är ogiltiga. Nästa kapitel diskuterar sidoeffekter i Simplicity.

## Två sidoeffekter

<chapterId>9eafe498-0765-419a-a69d-a74a9cdf3713</chapterId>

I de föregående kapitlen visade vi hur man bygger vissa datastrukturer och beräkningar med hjälp av Simplicitys kärnuppsättning av kombinatorer. Som vi noterade räcker kärnkombinatorerna för att implementera vilken ändlig, ren beräkning som helst. Detta väcker frågan: vad mer kan uppnås? Vi kan lägga till ytterligare sidoeffekter till våra uttryck.

Det finns olika typer av möjliga sidoeffekter för uttryck: tillståndsuppdatering, skrivning till en logg, kastande av ett undantag, läsning från en omgivning, anrop av en fortsättning (continuation), etc. De sidoeffekter som är tillgängliga i Simplicity beror på applikationen.

För Bitcoin- och Liquid-applikationer har vi för närvarande två sidoeffekter: Failure-effekten, som är en undantagseffekt där undantaget har typen `𝟙`, och Reader-effekten som gör det möjligt att komma åt data från transaktionens omgivning. Våra kärnkombinatorer är "rena"; de har inga sidoeffekter. Jets kan dock introducera nya primitiver som har sidoeffekter.

### Jets med effekter

Vi kommer att prata mer om jets senare i denna kurs, men här introducerar vi några exempeljets för att illustrera deras sidoeffekter.

#### Bip0340-verify

`bip0340-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚⁵¹² ⊢ 𝟙` är en jet för ett uttryck som tar en x-only pubkey, ett 256-bitars meddelande och en Schnorr-signatur, och returnerar ingenting! Enligt sin typ borde den bete sig på samma sätt som en `unit`. Skillnaden ligger i jetens sidoeffekt: om signaturvalideringen misslyckas avbryts hela beräkningen genom att ett undantag (av unit-typ) kastas. Detta är Failure-effekten.

#### Verify

`verify : 𝟚 ⊢ 𝟙` är en minimalistisk jet för att uttrycka Failure-effekten. Om `verify`s input är `false` avbryts hela beräkningen genom att ett undantag kastas. Om inputen är `true` returneras ingenting, men beräkningen kan fortsätta.

#### Transaktionshashar

`sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` verkar vara en konstant funktion, eftersom det bara finns ett möjligt inputvärde: den tomma tupeln. Denna jet läser dock från transaktionens omgivning och producerar en hash av transaktionsdata som är analog med det `SIGHASH_ALL`-meddelandedigest som används vid Bitcoin Scripts signaturverifiering. Detta är ett exempel på Reader-effekten: det returnerade värdet beror på den transaktionsomgivning som jeten exekveras inom. Det finns flera andra hashningsjets som hashar olika delmängder av transaktionsomgivningens data för att hjälpa till att bygga anpassade meddelandedigester för signaturer.

#### Introspektionsjets

`input-sequence : 𝟚³² ⊢ 𝟚³²?` är en funktion som tar ett input-index och returnerar transaktionens sekvensnummer för den inputen, och returnerar eventuellt ingenting om indexet är utanför gränserna. Även här är utdatavärdet inte en ren funktion av input-indexet, utan operationen använder istället Reader-effekten för att komma åt transaktionens omgivning för att avgöra utdatavärdet. Det finns flera andra introspektionsjets som returnerar olika fragment av transaktionsomgivningens data.

### Klassificering av effekter

Inte alla sidoeffekter är likadana. Vissa sidoeffekter beter sig snällare än andra. Vi kan klassificera effekter efter hur mottagliga de är för programtransformationer.

#### Kommutativa effekter

En kommutativ effekt är en där, om man byter plats på utdatan för två uttryck, man säkert kan byta plats på själva uttrycken utan att ändra uttryckets effekt. Betrakta `swap = I H ▵ O H : A × B ⊢ B × A`. Om `f ▵ g ⨾ swap = g ▵ f` för varje uttryck `f` och `g` med sidoeffekter, är effekterna kommutativa.

Att läsa transaktionsdata från omgivningen är en kommutativ effekt eftersom resultatet av att läsa från omgivningen är detsamma, oavsett i vilken ordning vi utför läsningen.

Generellt sett är kastande av ett undantag inte en kommutativ effekt. Om `f` kastar något undantag `e₁` och `g` kastar något annat undantag `e₂`, beror det på i vilken ordning de exekveras vilket undantag som kastas från paret av `f` och `g`.

I specialfallet med Failure-effekten, där bara ett unit-typat undantag kan kastas, är effekten dock kommutativ. Oavsett vilken av `f` eller `g` som kastar ett undantag blir det resulterande undantaget detsamma, eftersom det bara finns ett möjligt undantagsvärde.

#### Idempotenta effekter

En idempotent effekt är en där, om man duplicerar utdatan för ett uttryck, man säkert kan duplicera själva uttrycket utan att ändra uttryckets effekt. Betrakta `dup = iden ▵ iden : A ⊢ A × A`. Om `f ⨾ dup = dup ⨾ f ▵ f` för varje `f` med sidoeffekter, är effekterna idempotenta.

Att läsa transaktionsdata från omgivningen är en idempotent effekt. Att kasta ett undantag är också en idempotent effekt. Även om bara ett av de två duplicerade uttrycken kommer att exekveras, kommer alla undantag som kastas av `dup ⨾ f ▵ f` att vara desamma som undantaget som kastas av `f ⨾ dup`.

Att skriva till en logg är dock kanske inte idempotent, eftersom duplicering av effekten skulle göra att loggmeddelandet uppträder två gånger. Om loggen dock består av en _mängd_ av meddelanden istället för en _lista_ av meddelanden, skulle effekten vara idempotent (och kommutativ), eftersom mängdinsättning i sig är en idempotent operation.

#### Unitära effekter

En unitär effekt är en där, om man kasserar utdatan för ett uttryck, man säkert kan kassera själva uttrycket utan att ändra uttryckets effekter. Om det alltid gäller att `f ⨾ unit = unit` för varje `f` med sidoeffekter, är dina effekter unitära.

Att läsa data från omgivningen är en av de få typerna av unitära effekter. Om resultatet av att läsa transaktionsdata från omgivningen kasseras, kan hela uttrycket som utför läsningen kasseras.

Failure-effekten är inte unitär. Om `f` kastar ett undantag gör även `f ⨾ unit` det; exekveringen når inte ens fram till `unit`-kombinatorn innan beräkningen avbryts. Å andra sidan skulle `unit` uppenbarligen inte kasta något undantag, så effekterna av `f ⨾ unit` och `unit` skulle vara olika.

Sammanfattningsvis, så här klarar sig de ovan diskuterade effekterna mot dessa tre egenskaper:

| Effekt | Kommutativ | Idempotent | Unitär |
| --- | :---: | :---: | :---: |
| Reader (transaktionsomgivning) | ✓ | ✓ | ✓ |
| Failure (unit-typat undantag) | ✓ | ✓ | ✗ |
| Writer (logg som en mängd) | ✓ | ✓ | ✗ |
| Generella undantag (godtycklig typ) | ✗ | ✓ | ✗ |

### Effekter som tillåts i Simplicity

Ju fler välfungerande egenskaper en typ av effekt har, desto mer utrymme har en Simplicity-optimerare för att transformera program som använder dessa effekter. Idealt sett skulle vi bara tillåta effekter som har alla tre egenskaperna: kommutativa, idempotenta och unitära. Detta skulle göra det möjligt för en optimerare att utföra vilken typ av programtransformation den vill. Att läsa från en omgivning är dock den enda effekten som uppfyller alla tre egenskaperna.

Istället kräver vi att Simplicitys effekter är kommutativa och idempotenta. Båda de effekter vi använder i Simplicity, Failure-effekten och Reader-effekten, är kommutativa och idempotenta. Detta möjliggör en stor klass av optimeringar på Simplicity-kod.

Den "kasserings"-transformation som beskrivs ovan, som försöker ersätta `f ⨾ unit` med `unit`, eller någon liknande transformation, är dock inte tillåten om `f` kan producera en Failure-effekt. Föreställ dig om `f` innehöll en `bip0340-verify`-assertion. Det skulle vara katastrofalt att försöka optimera bort den kontrollen.

### Varför tillåta sidoeffekter över huvud taget?

Varför tillåter Simplicity över huvud taget sidoeffekter? Vore det inte bättre om varje program tog hela transaktionen som input och returnerade en boolesk output som avgör om en transaktion är giltig eller inte?

#### Batchverifiering

En anledning till att vi har Failure-effekten är för att stödja [batchverifiering](https://github.com/bitcoin/bips/blob/c9a6ca6297eb8de850f6b64dafb8e60ee9b64d66/bip-0340.mediawiki#batch-verification) av Schnorr-signaturer. Vid batchverifiering slås många enskilda Schnorr-signaturkontroller samman på ett sådant sätt att om en enda signaturkontroll misslyckas, misslyckas hela batchen.

Denna batchningsprocedur förbättrar effektiviteten jämfört med att verifiera varje signatur individuellt. Nackdelen är att om batchverifieringen misslyckas, får vi inte veta vilken specifik signaturkontroll eller vilka kontroller som misslyckades.

Genom att använda failure-sidoeffekten säkerställer `bip0340-verify` att om en signaturkontroll misslyckas, misslyckas hela transaktionen. Om `bip0340-verify` istället returnerade `𝟚`, en boolesk typ, för framgång eller misslyckande, skulle en misslyckad signaturkontroll fortfarande kunna leda till en gren där skriptet lyckas. I ett sådant fall skulle vi behöva veta om den specifika signaturen är giltig eller inte, och skulle därmed inte kunna dra nytta av batchverifiering.

#### Förberäknad transaktionsdata

Ett problem i tidig Bitcoin Script var att hashfunktionen som användes för att skapa meddelandedigester för signaturer var linjär i transaktionens storlek. Vanligtvis skapar varje input minst ett meddelandedigest för signaturverifiering, så totalt sett var mängden hashning kvadratisk i transaktionsstorleken.

Detta problem åtgärdades i Segwit och senare iterationer av Bitcoin Script genom att omdefiniera meddelandedigesterna så att de kunde beräknas i konstant tid per signaturkontroll. Detta bygger på att ha `PrecomputedTransactionData`, som förberäknar hashar av transaktionsdata en gång och sedan delas av varje inputs sighash-beräkningar. Simplicitys transaktionshashningsjets bygger på samma typ av förberäknad transaktionsdata för att säkerställa att jetsen körs i konstant tid.

Anta att `sig-all-hash` inte använde Reader-effekten. Anta att vi på något sätt lyckades bygga en Simplicity-typ för transaktionsomgivningen. Låt oss kalla den `TxEnv`, så att `sig-all-hash : TxEnv ⊢ 𝟚²⁵⁶` var jetens typ. En sådan definition skulle kräva att jeten `sig-all-hash` kunde beräkna hashen för vilken transaktion som helst, inte bara den transaktion den är involverad i. Simplicity-program skulle kunna kopiera den givna `TxEnv` och skicka en modifierad kopia av den till `sig-all-hash`. I ett sådant fall skulle `sig-all-hash` inte kunna förlita sig på `PrecomputedTransactionData`, och vi skulle vara tillbaka till att kräva linjär tid i vilken transaktionsdata som helst som skickades in i denna version av `sig-all-hash`.

Eftersom `sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` använder Reader-effekten för att komma åt transaktionsdata, får den _bara_ tillgång till en fast transaktionsomgivning. Av den anledningen kan jetens implementation säkert använda `PrecomputedTransactionData` och köras i konstant tid.

### Aggregering av signaturer över flera inputs

Även om varken Liquid eller Bitcoin stöder [aggregering av signaturer över flera inputs](https://hrf.org/latest/cisa-research-paper/) (cross-input signature aggregation) i dagsläget, vill vi kontrollera att Simplicity kan vara kompatibelt med det när tiden kommer.

Även om detaljerna inte har utarbetats, föreställer vi oss halvaggregering implementerad med hjälp av en Writer-effekt. Det vill säga, en ny jet med en typ som `half-agg-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚²⁵⁶ ⊢ 𝟙` skulle ta en publik nyckel, ett meddelandedigest och `r`-komponenten av en Schnorr-signatur (en Schnorr-signatur består av en `r`-komponent och en `s`-komponent) och skriva den till en transaktionslogg innan exekveringen fortsätter. Sedan, någon annanstans i eller med transaktionen, skulle en aggregerad `s`-komponent för alla halvaggregerade Schnorr-signaturer tillhandahållas. Transaktionen skulle bara vara giltig när en sådan aggregerad `s`-komponent tillhandahålls för alla loggade nycklar, meddelanden och `r`-komponenter.

För att uppfylla Simplicitys krav måste denna Writer-effekt vara idempotent och kommutativ. Detta kan säkerställas genom att behandla writer-loggen som en mängd av tupler bestående av nyckel, meddelande och `r`-komponent. Detta fungerar eftersom mängdoperationer är idempotenta och kommutativa. Att behandla loggen som en mängd av värden skulle vara kompatibelt med algoritmen för verifiering av halvaggregering.

### Slutsats

I detta kapitel tittade vi på att lägga till sidoeffekter till de beräkningar som Simplicity kan göra. Vi klassificerade olika typer av effekter utifrån hur väl de fungerar med avseende på olika typer av programtransformation. Vi beslutade att begränsa Simplicitys effekter till de som är kommutativa och idempotenta.

De två effekter vi använder för Bitcoin- och Liquid-applikationer är Reader-effekten, för att komma åt transaktionsomgivningen, och Failure-effekten, för att avbryta och misslyckas programmet. Vissa jets använder primitiva operationer där denna typ av sidoeffekter kan uppstå.

Failure-effekten avgör utdatan för ett Simplicity-program: programmet misslyckas antingen, vilket gör transaktionen ogiltig, eller så lyckas programmet. Reader-effekten tillhandahåller en typ av input till ett Simplicity-program: omgivningen som innehåller transaktionsdata. Men vi behöver även tillhandahålla andra input, såsom digitala signaturer, till Simplicity-program.

I nästa kapitel tittar vi på vad Simplicity-program är, hur de blir till adresser, och hur vi lägger till andra input, såsom signaturer, till Simplicity-program.

## Program och adresser

<chapterId>961652e3-8f7d-4c2a-8b55-9a990b91a0dd</chapterId>

I föregående kapitel beskrev vi två sidoeffekter som används i Simplicity: Failure-effekten, som avgör om ett program lyckas eller misslyckas, och Reader-effekten, som ger tillgång till transaktionsomgivningen. Nu vänder vi oss till den praktiska frågan: vad exakt är ett Simplicity-program, och hur blir det en adress på blockkedjan?

### Simplicity-program

Ett Simplicity-program definieras som ett Simplicity-uttryck av typen `𝟙 ⊢ 𝟙`. Denna typsignatur betyder att programmet inte tar någon meningsfull input (bara unit-värdet) och inte producerar någon meningsfull output (bara unit-värdet). Reader-effekten fångar transaktionsomgivningens input, medan Failure-effekten anger framgång eller misslyckande. Dessa effekter hanterar I/O snarare än Simplicity-typerna själva.

### Commitment Merkle Root

Istället för att lagra fullständiga program on-chain använder Bitcoin commitments — en praxis som utgår från Pay-to-Script-Hash (P2SH). Simplicity använder en Commitment Merkle Root (CMR).

Varje kombinator får en SHA-256-tagg härledd från mönstret: `Simplicity␟Commitment␟[identifier]`, där `␟` representerar ASCII-koden 31 (unit separator).

Varje tagg är SHA-256-hashen av motsvarande föravtryck (pre-image) som listas nedan:

| Kombinator | Tagg-föravtryck (ASCII-sträng) |
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

Ett Simplicity-uttryck hashas därefter rekursivt till en 256-bitars CMR genom att beräkna ett taggat SHA-256-midtillstånd (midstate) för varje kombinator tillsammans med CMR:erna för dess argument (skriv `#ᶜ(e)` för CMR:en av uttrycket `e`, och `∥` för bytekonkatenering):

| Kombinator | CMR-regel |
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

Binära kombinatorer (`comp`, `pair`, `case`) konkatenerar CMR:erna för båda barnen; unära kombinatorer (`take`, `drop`, `injl`, `injr`) konkatenerar sitt enda barns CMR efter 32 bytes med `0x00`-utfyllnad; och de nullära löven (`iden`, `unit`) hashar bara sin egen tagg. Två konventioner håller detta billigt att beräkna: SHA-256-midtillstånd används så att **varje uttryck kräver högst ett anrop till SHA-256:s komprimeringsfunktion** (givet att midtillståndet fram till de konstanta taggarna är förberäknat), och konstruktorerna med ett argument prefixar sitt argument med 32 bytes av `0x00`-utfyllnad, vilket möjliggör lite extra förberäkning för de implementationer som vill ha det.

För `unit`-kombinatorn — en nullär konstruktor utan argumentdeluttryck — specialiseras denna regel till `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)`, där `tag_unit = SHA-256(Simplicity␟Commitment␟unit)` (taggen matas in två gånger). Den resulterande CMR:en för det triviala `unit`-programmet är:

```
0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

Avgörande är att CMR:en inte binder sig till Simplicity-uttryckens typer, utan istället förlitar sig på typinferens vid inlösen.

### Adresser

Adresser använder BIP-0341:s Taproot-mekanism, där CMR:er commitas under TapLeaf-version `0xbe`. Processen involverar:

1. Beräkning av en taggad TapLeaf-hash som kombinerar versionsbyten, CMR-längden och själva CMR:en
2. Justering (tweak) av en intern publik nyckel (med hjälp av en NUMS-punkt när ingen key-spend-väg önskas)
3. Konvertering till bech32m-format
4. Tillägg av lämpliga kontrollsummor

När ingen key-spend-väg önskas sätts den interna publika nyckeln till en **NUMS**-punkt ("Nothing-Up-My-Sleeve"): en kurvpunkt som avsiktligt valts så att ingen känner till dess diskreta logaritm — med andra ord, en punkt utan motsvarande privat nyckel. Eftersom ingen någonsin kan producera en signatur för den är key-spend-vägen bevisligen oanvändbar, och outputen kan spenderas *endast* via den commitade Simplicity-skriptvägen. I en verklig tillämpning bör denna NUMS-punkt randomiseras enligt rekommendationen i BIP-0341, så att outputar utan key-spend-väg inte går att skilja från vanliga Taproot-outputar (en fördel för integriteten).

#### Från Simplicity till adress

Låt oss gå igenom hela härledningen för det enklast möjliga programmet: `unit : 𝟙 ⊢ 𝟙`, en no-op som alltid lyckas.

**1. Kombinatortagg.** Beräkna först `unit`-taggen:

```
tag_unit = SHA-256(Simplicity␟Commitment␟unit)
         = 0xd723083cff3c75e29f296707ecf2750338f100591c86e0c71717f807ff3cf69d
```

**2. CMR.** Mata in taggen två gånger för att få programmets CMR:

```
CMR = #ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)
    = 0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

**3. TapLeaf-hash.** Prefixa CMR:en med Simplicitys TapLeaf-version `0xbe` och CMR-längden `0x20` (32 bytes), och beräkna sedan Elements taggade TapLeaf-hash (en taggad hash är `hash_str(x) = SHA-256(SHA-256(str) ∥ SHA-256(str) ∥ x)`):

```
hash_TapLeaf/elements(0xbe ∥ 0x20 ∥ CMR)
  = 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c
```

Med bara detta enda leaf finns det inga TapBranches, så denna hash är redan TapTree-roten.

**4. TapTweak.** Eftersom vi inte vill ha någon key-spend-väg använder vi BIP-0341:s NUMS-punkt som intern nyckel och justerar (tweakar) den med TapTree-roten:

```
internal_pk = 0x50929b74c1a04954b78b4b6035e97a5e078a5a0f28ec96d547bfee9ace803ac0
t = hash_TapTweak/elements(internal_pk ∥ 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c)
  = 0xb3bef172389b0937d7e5a8b15cfa41e776777f13f2f659cb06220a6ff0658285
```

**5. Utdatanyckel.** Justera den interna nyckeln på kurvan, `output_pk = lift_x(internal_pk) ⊕ t·G` (den elliptiska kurvans aritmetik sammanfattas här), vilket ger den x-only utdatanyckeln `0x2cb0c20acd7340b4d4b65f6a60e2888d0d64e3267261f3b3cf7290e5af3f9e09`.

**6. Bech32m-adress.** Koda den x-only utdatanyckeln, prefixa med ett `p` (SegWit v1:s witness-versionstecken), lägg till Liquid-testnätets läsbara prefix `tex1`, och lägg till Bech32m-kontrollsumman. Den slutliga adressen är:

```
tex1p9jcvyzkdwdqtf49kta4xpc5g35xkfcexwfsl8v70w2gwttelncyshxjk56
```

Det var en hel del arbete — men mycket av det är mandaterat av Taproot självt, inte av Simplicity.

### Witness-uttryck

En ny kombinatortyp löser bristen på input till Simplicity-program: witness-uttrycket. `witness`-kombinatorn tillåter att signaturdata och annat witness-material integreras i program.

```
      w : B
-----------------
witness w : A ⊢ B
```

Witness-uttryckets semantik är okomplicerad: det ignorerar sin input och returnerar helt enkelt värdet `w` (som kan vara av vilken Simplicity-typ som helst), det vill säga `⟦witness w⟧(a) = w`. Detta tillför **ingen ny uttrycksfullhet** — enligt fullständighetsteoremet kan Simplicity redan bygga vilken sådan konstant funktion som helst (kom ihåg `scribe`-makrot från tidigare kapitel). Poängen med `witness`-kombinatorn ligger helt och hållet i dess **CMR**: värdet `w` är **exkluderat** från uttryckets CMR, så adressen kan beräknas innan `w` är känt, och `w` tillhandahålls vid inlösentillfället.

Detta designval stöder beskärning (pruning) — icke-exekverade villkorsgrenar behöver inte avslöjas on-chain, inklusive deras tillhörande witness-uttryck. När en gren beskärs behöver verifieraren bara CMR:en för det beskurna deltrådet, inte dess faktiska innehåll.

### Witness-värden

Det kan verka vara en begränsning att ett witness-uttryck bara kan innehålla ett *värde*, och inte ett mer generellt Simplicity-uttryck. Men program för UTXO-baserade blockkedjor exekveras bara en gång. Det finns inget behov av att skicka in ett helt deluttryck i en witness-nod: användaren kan helt enkelt köra det deluttrycket själv, off-chain, och skriva av dess output till witness-värdet för att få exakt samma resultat.

(Senare i denna kurs kommer vi att möta `disconnect`-kombinatorn, som beter sig ungefär som ett witness-uttryck som *faktiskt* tar ett helt Simplicity-uttryck som sitt argument.)

En alternativ design skulle mata in all witness-data som ett argument till toppnivåns Simplicity-program. Witness-uttryck föredras av två skäl. För det första **beskärning**: icke-exekverade grenar av `case`-uttryck avslöjas aldrig on-chain, och alla witness-uttryck inuti de grenarna beskärs bort tillsammans med dem. För det andra **lokalitet**: witness-uttryck låter oss placera varje witness-värde exakt där det används, istället för att tråda det ner från programmets toppnivåinput.

### Typinferens

Eftersom CMR:er inte binder sig till typer återuppbyggs typsystemet vid inlösen. Simplicitys typinferensalgoritm avgör de minimala typerna för varje deluttryck baserat på kombinatorstrukturen. Mer precist beräknar inferensen den *principala* (mest generella) typen för varje deluttryck; eventuella typvariabler som förblir fria instansieras därefter till unit-typen `𝟙`, vilket ger en unik, minimal typ för programmet.

### Slutsats

I detta kapitel fastställde vi att Simplicity-program är uttryck av typen `𝟙 ⊢ 𝟙`, förklarade hur Commitment Merkle Roots konstrueras från taggade SHA-256-hashar av varje kombinator, och visade hur CMR:er omvandlas till on-chain-adresser via BIP-0341 Taproot. Vi introducerade witness-uttryck som mekanismen för att tillhandahålla signaturdata och andra input vid spenderingstillfället utan att binda sig till deras värden vid adressskapandet.

# Avslutande avsnitt

<partId>96952535-4aa6-4e78-91e2-d12e9df895d4</partId>

## Recensioner & betyg

<chapterId>fb0b0133-39ea-497b-bd36-198be42c4fab</chapterId>
<isCourseReview>true</isCourseReview>

## Slutprov

<chapterId>2cc5e818-abcb-4a0a-9991-7a492c572e2d</chapterId>
<isCourseExam>true</isCourseExam>

## Slutsats

<chapterId>8ade24bd-a84f-4d25-8f64-bdfa8b58926c</chapterId>
<isCourseConclusion>true</isCourseConclusion>