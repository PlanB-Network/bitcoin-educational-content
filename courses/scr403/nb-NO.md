---
name: Fordypning i Simplicity
goal: Mestre designfilosofien, typesystemet og hele livssyklusen til Simplicity
objectives:
  - Forstå de tre grunnleggende komposisjonsmetodene og de ni kombinatorene som utgjør et komplett språk
  - Bygg boolsk logikk, aritmetikk og SHA-256 fra Simplicitys minimale typesystem
  - Forstå hvordan Failure- og Reader-sideeffektene muliggjør reell interaksjon med blokkjeden
  - Lær hvordan Simplicity-programmer blir Taproot-adresser og løses inn med vitnedata
---

# Fordypning i Simplicity

Et dypdykk i teorien og designbeslutningene bak Simplicity-språket, basert på den komplette femdelte ["Delving Simplicity"](https://delvingbitcoin.org/t/delving-simplicity-part-three-fundamental-ways-of-combining-computations/1902)-artikkelserien av [Dr. Russell O'Connor](https://r6.ca/), skaperen av Simplicity hos Blockstream Research. Dette kurset forklarer *hvorfor* Simplicity ble designet slik det ble, ikke hvordan man skriver det.

Kurset følger Dr. O'Connors artikler gjennom de tre grunnleggende måtene å kombinere beregninger på, det minimale typesystemet og dets fullstendighetsteorem, konstruksjonen av praktiske datatyper og aritmetikk fra grunnleggende prinsipper, den nøye introduksjonen av sideeffekter for interaksjon med blokkjeden, og til slutt hvordan programmer blir forpliktet til adresser og løst inn on-chain.

+++

# Introduksjon

<partId>c362889b-c630-435f-911b-724c4eca505b</partId>

## Kursoversikt

<chapterId>cdcc40b6-c985-45b4-9bee-6f931e984476</chapterId>

Velkommen til SCR403 — Fordypning i Simplicity!

Dette kurset er basert på artikkelserien **"Delving Simplicity"** skrevet av [Dr. Russell O'Connor](https://r6.ca/), en Infrastructure Tech Developer hos [Blockstream](https://blockstream.com/) og skaperen av Simplicity. De originale artiklene ble publisert på forumet [Delving Bitcoin](https://delvingbitcoin.org/u/roconnor-blockstream/summary) og utgjør det primære kildematerialet for dette kurset. Vi er takknemlige for hans banebrytende arbeid, som har gjort dette pedagogiske innholdet mulig.

### Hva du vil lære

Dette kurset utforsker designfilosofien og de matematiske grunnlagene bak Simplicity, det neste generasjons skriptspråket som ble aktivert på [Liquid Network](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/) i juli 2025. Det følger den komplette femdelte artikkelserien og er strukturert i to hovedinnholdsdeler:

1. **Grunnlaget for Simplicity** — Hvorfor beregning på blokkjeden krever et fundamentalt annerledes språk, de tre måtene å kombinere operasjoner på (sekvensiell, parallell, betinget), og de ni kjernekombinatorene som utgjør et matematisk komplett språk
2. **Fra datatyper til programmer** — Bygge boolsk logikk, aritmetikk og SHA-256 fra grunnleggende prinsipper; forstå Failure- og Reader-sideeffektene som muliggjør interaksjon med blokkjeden; og lære hvordan programmer blir forpliktet til Taproot-adresser via Commitment Merkle Roots og løst inn med vitnedata

### Forkunnskaper

Dette er et kurs på **ekspertnivå** (omtrent 10 timer). Du bør være komfortabel med:
- Grunnleggende konsepter innen Bitcoin-scripting (hva transaksjonsvalidering gjør)
- Grunnleggende programmeringskonsepter (typer, funksjoner, komposisjon)
- Noe kjennskap til matematisk notasjon er nyttig, men ikke påkrevd. Vi introduserer alt underveis

### Nøkkelressurser

- **Originale artikler**: ["Delving Simplicity"](https://delvingbitcoin.org/u/roconnor-blockstream/summary) av Dr. Russell O'Connor på Delving Bitcoin
- **Simplicity-repositoriet**: [BlockstreamResearch/simplicity](https://github.com/BlockstreamResearch/simplicity) — kildekode og formelle Rocq-bevis
- **Offisiell nettside**: [simplicity-lang.org](https://simplicity-lang.org/) — dokumentasjon og SimplicityHL-referanse
- **Blockstream-bloggen**: [Simplicity on GitHub](https://blog.blockstream.com/en-simplicity-github/) — teknisk oversikt

Klar for å dykke ned i et av de mest elegante stykkene bitcoin-ingeniørkunst? La oss sette i gang!

## Hva er Simplicity?

<chapterId>d04f3960-d7fb-44e1-b5a3-25b33d03fd38</chapterId>

Hvis du kommer til dette kurset uten bakgrunn i Simplicity, vil dette kapittelet orientere deg før vi dykker ned i dybden.

### Simplicity i et nøtteskall

Simplicity er et **Bitcoin-native smartkontraktspråk**, i live på Liquid Network i dag. Først forestilt av Dr. Russell O'Connor rundt 2012 og beskrevet i detalj i hans artikkel fra 2017 *Simplicity: A New Language for Blockchains*, ble det aktivert på Liquid Network i juli 2025 etter mange års formell verifisering og utvikling.

I motsetning til Ethereums Solidity, som er et Turing-komplett, høynivå kontraktspråk, er Simplicity bevisst minimalt. Det har:
- **Tre typekonstruktører** (unit, sum, produkt)
- **Ni kombinatorer** (grunnleggende operasjoner og komposisjonsregler)
- **Ingen løkker, ingen rekursjon, ingen dynamisk minne**

Fra bare disse primitivene kan du bygge enhver beregning du trenger for transaksjonsvalidering, fra boolsk logikk til full SHA-256-hashing.

### Hva kan du gjøre med Simplicity i dag?

Simplicity driver allerede reelle applikasjoner på Liquid Network. Den mest bemerkelsesverdige er [Simplicity DEX](https://docs.simplicity-lang.org/use-cases/simplicity-dex/), en orakelfri opsjonsmarkedsplass hvor brukere handler kjøpsopsjoner på L-BTC med USDt som sikkerhet (den underliggende kontrakten støtter også salgsopsjoner). Andre aktive Simplicity-prosjekter inkluderer [Swaption](https://swaption.io/) fra SideSwap (opsjoner) og den åpen kildekode-baserte [Deadcat](https://github.com/Resolvr-io/deadcat) fra Resolvr (prediksjonsmarkeder). Utover DeFi muliggjør Simplicity avanserte bruksvilkår som vaults, covenants og komplekse multisig-ordninger som ville vært umulige eller usikre i Bitcoin Script.

### Hva dette kurset er — og ikke er

Dette er **ikke** en praktisk kodetutorial. Du kommer ikke til å skrive Simplicity-programmer her. Hvis du er ute etter det, sjekk ut:
- [simplicity-lang.org](https://simplicity-lang.org/) — offisiell dokumentasjon og det høynivå SimplicityHL-språket
- [Simplicity GitHub-repositoriet](https://github.com/BlockstreamResearch/simplicity) — referanseimplementasjon, eksempler og Rocq-bevis
- [Blockstream-blogginnlegget](https://blog.blockstream.com/en-simplicity-github/) om å komme i gang

Det dette kurset **handler om**: de **filosofiske og tekniske valgene** bak Simplicitys design. Hvorfor ble dette språket laget slik? Hvorfor bare ni kombinatorer? Hvorfor ingen rekursjon? Hvorfor er det viktig at typesystemet kobles til Gentzens sekventkalkyle?

Tenk på det som å forstå **hvorfor motoren ble bygget slik** fremfor å lære å kjøre bilen.

### Hvem er dette for?

Dette kurset er ideelt for:
- **Protokollutviklere** som ønsker å forstå Simplicitys grunnlag før de skriver kode
- **Bitcoin-forskere** interessert i den formelle verifiseringen og den typeteoretiske tilnærmingen
- **Dataforskere** nysgjerrige på sammenhengen mellom sekventkalkyle og beregning på blokkjeden
- **Avanserte bitcoinere** som ønsker å gå utover en overfladisk forståelse av Liquids scripting-muligheter

Hvis begreper som "sumtyper", "kombinatorer" eller "sekventkalkyle" er helt nye for deg, ikke bekymre deg, vi forklarer alt fra bunnen av. Men vær forberedt på en tett, matematisk reise.

### Fra artikler til kurs

Den originale "Delving Simplicity"-serien av Dr. O'Connor er strukturert som fem tekniske artikler. Dette kurset omorganiserer og kommenterer det materialet til en progressiv læringsvei med quizer for å teste forståelsen din underveis. Ideene, definisjonene og bevisene er hans, og vi har tilpasset formatet for strukturert utdanning.

# Grunnlaget for Simplicity

<partId>a5976618-94ab-4b29-b9aa-040d35c68e5d</partId>

## Grunnleggende måter å kombinere beregninger på

<chapterId>6d46e77a-7e60-473b-b230-418da5ae44eb</chapterId>

Nå som Simplicity er aktivert på Liquid Network, ønsker jeg å gjøre et dypdykk i filosofien og designet til Simplicity-språket.

Bitcoins transaksjonsvalidering er en betydelig annerledes anvendelse enn vanlig programmeringsspråkdesign. Blokkplass koster mye, så programmer må være kompakte. Programmene i Bitcoin-transaksjoner blir bare noensinne kjørt på ett enkelt input, og alle kjører programmet på det samme inputet. I tillegg kjenner den autoriserende agenten allerede utfallet av beregningen på forhånd: at transaksjonen er gyldig.

Vanligvis vil den autoriserende agenten kjøre mye dyrere beregninger for å utlede vitnedata som attesterer transaksjonens gyldighet, mens programmer som kjøres på blokkjeden må sjekke vitnedataen for gyldighet. Å sjekke gyldighet er ofte mye billigere enn å bevise gyldighet.

Vi har designet Simplicity med denne typen unike utfordringer innen språkdesign i tankene. For eksempel krever Simplicity at ikke-utførte grener beskjæres slik at de ikke vises på blokkjeden. Forbehandlingstrinn er nøye designet for å utvise (kvasi-)lineær tidskompleksitet i størrelsen på Simplicity-programmet. Statisk analyse brukes i stedet for "gass", som ikke kan beregnes uten å utføre kode på en foreskrevet måte, slik at detaljene i eksekveringsmodellen ikke blir konsensuskritiske. Ingen dynamisk minneallokering under eksekvering. Og så videre.

Før vi går inn i designdetaljene til Simplicity, ønsker jeg å begynne denne serien med litt programmeringsfilosofi om de generelle måtene å kombinere grunnleggende byggeklosser for å skape ny funksjonalitet.

### Komposisjon

Anta at man designer et språk for programmerbare transaksjoner for en blokkjede som Bitcoin. Spesielt har programmer bare tilgang til transaksjonsdataen og UTXO-dataen til inputene, og eksekvering bestemmer bare transaksjonens gyldighet (som lar resultatet av eksekveringen bufres). La oss si at man starter med et sett med grunnleggende operasjoner som kan utføre ulike oppgaver som grunnleggende beregninger, lesing og/eller prosessering av data fra transaksjonen, og signaturverifisering. Hver operasjon konsumerer en type input (eventuelt tom) og returnerer en type output. Hvilke måter kan vi kombinere disse grunnleggende operasjonene til mer komplekse operasjoner?

### Sekvensiell komposisjon

![Sequential Composition](assets/en/001.webp)

Den mest grunnleggende komposisjonsmetoden er sekvensiell komposisjon. Hvis vi har to grunnleggende operasjoner, hvor den ene sin output-datatype samsvarer med den andres input-datatype, kan vi kombinere disse to operasjonene til en ny sammensatt operasjon. Denne nye operasjonen kjører disse to grunnleggende operasjonene i sekvens, tar inputen til den første operasjonen som input, sender outputen fra den første operasjonen inn i inputen til den andre operasjonen, og returnerer til slutt outputen fra den andre operasjonen.

Selvfølgelig trenger vi ikke å begrense oss til bare å kombinere grunnleggende operasjoner. Nå som vi har noen sammensatte operasjoner, kan vi kombinere disse ved hjelp av funksjonell komposisjon også.

I matematikken kalles denne sekvensielle komposisjonen ofte bare "komposisjon", og man kan tro at dette er den eneste måten å komponere ting på. Vi har imidlertid andre måter å komponere operasjoner på.

### Parallell komposisjon

![Parallel Composition](assets/en/002.webp)

Anta at vi har to operasjoner, de kan være grunnleggende eller komplekse operasjoner, og de tar begge samme type input. En annen grunnleggende måte å komponere disse to operasjonene på er å utføre dem begge på samme input. Dette kalles parallell komposisjon, og typen output er "produktet" av typene til outputene til de opprinnelige operasjonene og inneholder paret av de to outputene.

Selv om dette kalles "parallell" komposisjon, og de to operasjonene i prinsippet kunne bli utført parallelt, er parallell eksekvering ikke et operasjonelt krav. Vi kan implementere parallell komposisjon "sekvensielt" ved å utføre den ene operasjonen først og deretter den andre operasjonen. Vi bryr oss ikke om detaljene i hvordan parallell komposisjon er implementert, så lenge outputen er den samme.

### Betinget komposisjon

![Conditional Composition](assets/en/003.webp)

Betinget komposisjon er dualen til parallell komposisjon. I dette tilfellet har vi to operasjoner som produserer samme output, og vi komponerer dem ved å velge én av dem å utføre. Inputen til denne sammensatte operasjonen er "summen" eller "den merkede unionen" av typene til inputene til de opprinnelige operasjonene. I dette tilfellet er merket, "Left" eller "Right", en enkelt bit i inputens data som bestemmer hvilken type data som fraktes, og dermed hvilken av de to operasjonene som kan utføres.

Betinget komposisjon fungerer på samme måte selv når inputen er summen av to identiske typer. Sumtypen inneholder fortsatt et merke, og verdien av det merket bestemmer hvilken av de to operasjonene som skal utføres.

### Komposisjon i Bitcoin Script

Det finnes mange måter å realisere disse tre typene komposisjon på i ulike programmeringsspråk. I Bitcoin Script realiseres sekvensiell komposisjon (tilnærmet) ved sammenkjeding av to rutiner (dette er hvorfor Bitcoin Script kalles et konkatenativt programmeringsspråk), siden outputen til én rutine ligger igjen på stacken for å bli konsumert av den påfølgende rutinen. Parallell komposisjon oppnås ved bruk av duplikat- og bytteoperasjoner for å manipulere stacken slik at to rutiner kan kjøres på samme input. Ting er ikke helt greit, siden det vi kaller "produktet" av typer, typisk realiseres ved å bruke flere stack-elementer. Forhåpentligvis kan du se den generelle ideen.

Betinget komposisjon realiseres selvfølgelig av `OP_IF`, som grener basert på verdien på stacken. I dette tilfellet spiller det øverste stack-elementet rollen som merke, og vanligvis er det neste elementet eller elementene på stacken av ulike "typer" som avhenger av verdien til merket. For hvert tilfelle kan stack-elementtypene bare være egnet for prosessering av én av grenene i `OP_IF`. Etter at vi når `OP_ENDIF`, må imidlertid stack-elementene være av konsistent "type" slik at det gjenværende skriptet er i stand til å fortsette uavhengig av hvilken gren som tidligere ble tatt.

### Komposisjon i Simplicity

Vi designet Simplicity med kombinatorer som direkte implementerer disse tre komposisjonsformene. Sammen med noen få flere kombinatorer for å støtte andre grunnleggende operasjoner relatert til produkt- og sumtyper, ender kjernespråket i Simplicity opp med å bestå av ni kombinatorer som er tilstrekkelige til å uttrykke enhver endelig beregning. Vi vil diskutere dette mer detaljert i neste kapittel.

### En fjerde type komposisjon

Før vi avslutter bør vi nevne at det finnes minst én til type komposisjon i informatikken, nemlig "rekursiv komposisjon". I rekursiv komposisjon itereres én operasjon flere ganger.

Merk at Bitcoin Script ikke støtter rekursiv komposisjon, og på samme måte har vi eksplisitt utelukket ubegrenset rekursjon fra Simplicitys design. Vår tese er at ubegrenset iterativ beregning bedre implementeres ved bruk av rekursive covenants som beregner over flere transaksjoner. Dette lar brukere unngå begrensninger på blokkplass og standardness, og bedre forutsi transaksjonskostnader.

Når det er sagt, finnes det måter å misbruke Simplicitys delegeringsfunksjon på for å oppnå noe som ligner ubegrenset rekursiv komposisjon, noe vi kanskje diskuterer senere i denne serien.

### Konklusjon

Vi gjennomgikk de tre hovedformene for komposisjon for å transformere grunnleggende operasjoner til komplekse operasjoner:

- sekvensiell komposisjon
- parallell komposisjon
- betinget komposisjon

Vi diskuterte hvordan disse komposisjonsformene realiseres i Bitcoin Script, og antydet hvordan de har påvirket designet av Simplicity-språket. Vi bemerket at den fjerde typen komposisjon, rekursiv komposisjon, er spesifikt utelukket fra både Simplicity og Bitcoin Script.

I neste kapittel vil vi beskrive de ni kombinatorene som utgjør kjernen i Simplicity-språket, hvordan de tjener til å direkte realisere disse tre komposisjonsformene, og hvordan dette danner et komplett språk for å beskrive enhver endelig beregning.

## Kombinatorfullstendighet i Simplicity

<chapterId>2a10a6ba-fada-4556-a673-3ae8c0794bf0</chapterId>

I dette kapittelet introduserer vi kjernespråket i Simplicity og viser at språket er fullstendig, noe som betyr at enhver endelig beregning kan uttrykkes innenfor det.

### Simplicity-typer

Simplicity støtter tre grunnleggende typekonstruktører. Produkttypen `A × B` representerer outputene fra parallell komposisjon, mens sumtypen `A + B` (merket union) håndterer inputene til betinget komposisjon. Den tredje typen er unit-typen.

### Unit-type

Unit-typen, betegnet `𝟙` eller `ONE`, inneholder nøyaktig én verdi: den tomme tuppelen `⟨⟩` eller `()`. Denne null-bit-datatypen bærer ingen informasjon.

### Sumtype

En sumtype `A + B` kombinerer to typer med merker som indikerer "venstre" eller "høyre." Verdier skrives som `σᴸ(a)` eller `inl(a)` for venstre-merkede verdier og `σᴿ(b)` eller `inr(b)` for høyre-merkede verdier. Merkene forblir distinkte selv når man kombinerer identiske typer.

#### Boolsk type

Typen `𝟙 + 𝟙`, betegnet `𝟚` eller `TWO`, representerer en énbits type med to verdier. Etter konvensjon representerer `σᴸ⟨⟩` false/null, mens `σᴿ⟨⟩` representerer true/en.

### Produkttype

Produkttyper `A × B` inneholder verdipar skrevet som `⟨a, b⟩` eller `(a, b)`. Typen `𝟚 × 𝟚` har fire verdier, distinkt fra de fire verdiene i `𝟚 + 𝟚`.

### Kjerneuttrykk i Simplicity

Operasjoner betegnes som `f : A ⊢ B`, som betyr input-typen `A` og output-typen `B`. Simplicity er "førsteordens" — det mangler funksjonstyper.

### To grunnleggende operasjoner

Kjernespråket tilbyr to grunnleggende operasjoner:

**Identitet (`iden`).** Identitetsoperasjonen lar inputen passere uendret gjennom:

```
iden : A ⊢ A
⟦iden⟧(a) = a
```

**Unit (`unit`).** Unit-operasjonen forkaster inputen sin og returnerer den tomme tuppelen:

```
unit : A ⊢ 𝟙
⟦unit⟧(a) = ⟨⟩
```

Disse danner familier med én operasjon per type.

### Tre komposisjonskombinatorer

Sekvensiell komposisjon bruker `comp f g` (skrevet `f ⨾ g` eller `f >>> g`):

```
If f : A ⊢ B and g : B ⊢ C, then
comp f g : A ⊢ C
⟦f ⨾ g⟧(a) = ⟦g⟧(⟦f⟧(a))
```

Parallell komposisjon bruker `pair f g` (skrevet `f ▵ g` eller `f &&& g`):

```
If f : A ⊢ B and g : A ⊢ C, then
pair f g : A ⊢ B × C
⟦f ▵ g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩
```

Betinget komposisjon bruker `case f g : (A + B) × C ⊢ D`, som gir grenene tilgang til et delt miljø `C`:

```
If f : A × C ⊢ D and g : B × C ⊢ D, then
case f g : (A + B) × C ⊢ D
⟦case f g⟧⟨σᴸ(a), c⟩ = ⟦f⟧⟨a, c⟩
⟦case f g⟧⟨σᴿ(b), c⟩ = ⟦g⟧⟨b, c⟩
```

Hvorfor tar betinget komposisjon denne formen — en sum paret med et delt miljø `C` — fremfor en enklere `copair f g : A + B ⊢ C` som bare velger en gren? Fordi en ren `copair` ikke kan uttrykke **distribusjon**: funksjonen `dist : (A + B) × C ⊢ A × C + B × C` som skyver et delt input inn i hvilken gren som enn tas. Ved å bygge miljøet `C` direkte inn i `case`, oppnår Simplicity betinget komposisjon *og* distribusjon fra én enkelt kombinator — en av de sentrale designbeslutningene som holder kjernespråket nede på ni kombinatorer.

### Fire til kombinatorer

Produktkonsum bruker `take` og `drop`:

**take** ekstraherer det venstre elementet:

```
If f : A ⊢ C, then
take f : A × B ⊢ C
⟦take f⟧⟨a, b⟩ = ⟦f⟧(a)
```

**drop** ekstraherer det høyre elementet:

```
If f : B ⊢ C, then
drop f : A × B ⊢ C
⟦drop f⟧⟨a, b⟩ = ⟦f⟧(b)
```

Sumproduksjon bruker `injl` og `injr`:

**injl** pakker inn med et venstremerke:

```
If f : A ⊢ B, then
injl f : A ⊢ B + C
⟦injl f⟧(a) = σᴸ(⟦f⟧(a))
```

**injr** pakker inn med et høyremerke:

```
If f : A ⊢ C, then
injr f : A ⊢ B + C
⟦injr f⟧(a) = σᴿ(⟦f⟧(a))
```

### De ni kjernekombinatorene

Totalt har Simplicity nøyaktig ni kjernekombinatorer:

| Combinator | Purpose |
|---|---|
| `iden` | Pass input through |
| `unit` | Discard input |
| `comp` | Sequential composition |
| `pair` | Parallel composition |
| `case` | Conditional composition |
| `take` | Extract left from product |
| `drop` | Extract right from product |
| `injl` | Inject into left of sum |
| `injr` | Inject into right of sum |

### Simplicity og sekventkalkylen

Simplicitys design stammer fra det konjunktiv-disjunktive fragmentet av Gentzens sekventkalkyle. Mer presist er det en variant av den *funksjonelle tolkningen* av sekventkalkylen, som selv er analog med Curry-Howard-korrespondansen mellom naturlig deduksjon og lambdakalkylen. Kombinatorreglene utviser "mindre typer i premissene enn i konklusjonene", noe som gjør at Bit Machine — Simplicitys abstrakte stack-maskin-tolker — kan minimere datakopiering under eksekvering.

### Verdier er ikke uttrykk

Simplicity-uttrykk betegner operasjoner, ikke verdier. Notasjonen `scribe b : A ⊢ B` representerer et unikt uttrykk som alltid returnerer verdien `b`, og tjener som en notasjonell bekvemmelighet snarere enn en kombinator. Dette speiler Bitcoin Script, hvor operasjoner som `OP_1` skyver verdier i stedet for å uttrykke dem direkte.

### Simplicitys fullstendighetsteorem

Med alle ni kombinatorer i hånden, hvordan vet vi at vi ikke mangler noe — at disse ni virkelig er nok? Simplicitys fullstendighetsteorem svarer på dette: for enhver funksjon mellom (endelige) Simplicity-typer finnes det et Simplicity-uttrykk som betegner den. Beviset er konstruktivt — det viser hvordan man bygger uttrykket:

1. **Dekomponer inputen**: Ved å bruke nestede `case`-uttrykk, dekomponer enhver input av enhver type fullstendig til dens bestanddelbiter
2. **Bygg en oppslagstabell**: For hver mulige input, bruk `scribe` til å produsere den tilsvarende outputen
3. **Sett sammen**: De nestede case-ene og scribe-ene danner sammen en gigantisk oppslagstabell som implementerer funksjonen

Dette teoremet er formelt verifisert i bevisassistenten Rocq (tidligere Coq). Beviset er en del av det offisielle Simplicity-repositoriet og har blitt maskinsjekket for korrekthet.

Mens fullstendighetsteoremet garanterer at Simplicitys ni kombinatorer kan uttrykke enhver funksjon mellom (endelige) Simplicity-typer, blir de resulterende uttrykkene fra oppslagstabell-konstruksjonen upraktisk store. En funksjon på 256-bits input ville kreve en oppslagstabell med 2²⁵⁶ oppføringer. Dette er grunnen til at de neste kapitlene fokuserer på å bygge effektive uttrykk som utnytter strukturen i beregninger, i stedet for å brute-force alt gjennom oppslagstabeller.

### Konklusjon

Simplicitys kjernespråk inkluderer et typesystem og kombinatorer som muliggjør enhver endelig beregning. Mens fullstendighetsteoremet garanterer uttrykksevne, blir de resulterende uttrykkene fra den generiske konstruksjonen upraktisk store. Praktisk Simplicity-utvikling innebærer å utnytte beregningsstruktur for konsise uttrykk. De neste kapitlene utforsker datastrukturer, transaksjonsinteraksjoner og flere kombinatorer.

# Fra datatyper til programmer

<partId>08528a6f-d310-4675-b8cd-4e9b93b3c009</partId>

## Bygge datatyper

<chapterId>9981ae62-ae50-4770-adf2-b253d1e08de3</chapterId>

I de forrige kapitlene viste vi hvordan Simplicitys kjernesett av kombinatorer er nok til å implementere enhver endelig ren beregning. Dette kapittelet viser hvordan man bygger praktiske datastrukturer og beregninger fra disse primitivene — på samme måte som datamaskiner bygges fra logiske porter.

### Boolsk logikk

Den boolske typen, betegnet `𝟚`, er lik `𝟙 + 𝟙` og har to verdier: `σᴸ⟨⟩` (false) og `σᴿ⟨⟩` (true). Ved bruk av kjernekombinatorene kan boolske logikkoperatorer konstrueres.

#### And-operasjonen

Den logiske `and : 𝟚 × 𝟚 ⊢ 𝟚`-operasjonen tar to biter og returnerer én bit. Implementasjonen grener på den første biten: hvis false, returner false; ellers, returner den andre biten.

```
and ≔ case (injl unit) (drop iden) : 𝟚 × 𝟚 ⊢ 𝟚
```

Testing med `⟨false, false⟩`:

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

Testing med `⟨true, true⟩`:

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

#### Andre logiske operasjoner

Operasjonen `not` krever en hjelpekombinator:

```
                   f : A ⊢ C    g : B ⊢ C
--------------------------------------------------------------
copair f g ≔ iden ▵ unit ⨾ case (take f) (take g) : A + B ⊢ C
```

Det innledende `iden ▵ unit : A ⊢ A × 𝟙` legger til et tomt "miljø" til inputen, som gjør at `case`-kombinatoren kan brukes. Bruken av `take` i de to grenene forkaster dette tomme miljøet for å utføre `f` eller `g`.

Andre boolske logiske operasjoner:

- `or ≔ case (drop iden) (injr unit) : 𝟚 × 𝟚 ⊢ 𝟚`
- `not ≔ copair (injr unit) (injl unit) : 𝟚 ⊢ 𝟚`
- `xor ≔ case (drop iden) (drop not) : 𝟚 × 𝟚 ⊢ 𝟚`

### Bit-addere

En "halv-adder" tar to biter og legger dem sammen, og produserer en to-bits output: en overføringsbit (carry) og en sumbit.

```
half-adder ≔ and ▵ xor : 𝟚 × 𝟚 ⊢ 𝟚 × 𝟚
```

En "full-adder" legger sammen tre biter, og produserer en to-bits output. Inputen bruker den nestede tuppelen `(𝟚 × 𝟚) × 𝟚`.

For nestede tupler brukes kompakt notasjon:

- `O f` betegner `take f`
- `I f` betegner `drop f`
- `H` betegner `iden`

For eksempel betyr `I O H` `drop (take iden) : A × (B × C) ⊢ B`, som ekstraherer den midterste verdien. Notasjonen minner om binærsifre: når man tenker på nestede tupler som binærtrær, representerer notasjonen reverserte binærsifre for treposisjoner. Disse uttrykkene danner De Bruijn-indekser for Simplicity.

**Merk:** `I`-, `O`- og `H`-notasjonen gjelder bare for deluttrykk som utelukkende består av `take`, `drop` og `iden`.

Full-adderen komponerer to halv-addere, og tar den logiske `or`-en av overføringsbitene:

```
full-adder ≔ take half-adder ▵ I H
           ⨾ O O H ▵ (O I H ▵ I H ⨾ half-adder)
           ⨾ (O H ▵ I O H ⨾ or) ▵ I I H
           : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × 𝟚
```

I den første linjen kjører `take half-adder ▵ I H : (𝟚 × 𝟚) × 𝟚 ⊢ (𝟚 × 𝟚) × 𝟚` halv-adderen på de to første bitene, og lagrer den siste biten.

I den andre linjen lagrer `O O H ▵ (O I H ▵ I H ⨾ half-adder) : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × (𝟚 × 𝟚)` den første biten (overføringen ut fra den første halv-adderen) og kjører halv-adderen på de to siste bitene.

I den siste linjen tar `(O H ▵ I O H ⨾ or) ▵ I I H: 𝟚 × (𝟚 × 𝟚) ⊢ 𝟚 × 𝟚` den logiske OR-en av de to første bitene (overføringene ut fra begge halv-adderne) og returnerer sum-ut-biten fra den andre halv-adderen.

Dette demonstrerer Simplicity-programmering: å bruke `I`-, `O`- og `H`-notasjon for å referere til databiter, og danne egnede "miljøer" for å kalle andre funksjoner via sekvensiell komposisjon.

Brukere definerer ikke lavnivåoperasjoner direkte. Senere i denne serien diskuteres jets fra standardbiblioteket som implementerer vanlige funksjoner. Sluttbrukere forventes ikke å programmere direkte i Simplicity, i likhet med Bitcoin Script. I stedet genererer høynivåspråk som SimplicityHL Simplicity-kode, håndterer "miljøene" til deluttrykk og oversetter navngitte variabler til passende `take`- og `drop`-sekvenser.

### Vektorer

Vektorer med fast lengde defineres ved å danne itererte produkter av typen `A`:

- `A² ≔ A × A`
- `A⁴ ≔ A² × A²`
- `A⁸ ≔ A⁴ × A⁴`
- `…`

Disse kan skrives som `A^2`, `A^4`, `A^8`, osv.

Vektorer er kun definert for lengder som er potenser av to. Andre potenser krever valg av parenteseringskonvensjoner.

Gitt uttrykket `f : A ⊢ B`, "mapper" gjentatt paring det over vektorer med fast lengde:

- `f² ≔ f ▵ f : A² ⊢ B²`
- `f⁴ ≔ f² ▵ f² : A⁴ ⊢ B⁴`
- `f⁸ ≔ f⁴ ▵ f⁴ : A⁸ ⊢ B⁸`

Gitt funksjonen `f : A × B ⊢ B`, iterasjon eller "folding" over vektorer med fast lengde:

- `fold-right-2 f ≔ O O H ▵ (O I H ▵ I H ⨾ f) ⨾ f : A² × B ⊢ B`
- `fold-right-4 f ≔ fold-right-2 (fold-right-2 f) : A⁴ × B ⊢ B`
- `fold-right-8 f ≔ fold-right-2 (fold-right-4 f) : A⁸ × B ⊢ B`

Mange variasjoner finnes. Gitt `f : A × B ⊢ C`, "zip" over parede vektorer med `zip-n f : (Aⁿ × Bⁿ) ⊢ Cⁿ`. Gitt `f : (A × B) × C ⊢ C`, fold over parede vektorer med `bifold-right-n f : (Aⁿ × Bⁿ) ⊢ C`. Kombinasjon av `map` og `fold-right` skaper akkumulerende kombinatorer: `f : A × C ⊢ C × B` gir `map-accum-right-n f : Aⁿ × C ⊢ C × Bⁿ`. Mange flere varianter er mulige.

#### Multi-bit-ord

En bitvektor gir multi-bits heltall. For eksempel er `𝟚³²` en 32-bits ordtype. `𝟚²⁵⁶` er en 256-bits ordtype, egnet for hashverdier og kryptografiske operasjoner.

Ved bruk av full-adderen definerer en variant av vektoroperasjoner en "ripple carry adder" over multi-bits ord:

```
full-adder-n ≔ zip-accum-right-n full-adder : (𝟚ⁿ × 𝟚ⁿ) × 𝟚 ⊢ 𝟚 × 𝟚ⁿ
```

`full-adder-n` tar to n-bits binærtall og en énbits carry-input, og returnerer et énbits carry-out-flagg og en n-bits sum.

#### SHA-256

Ved rekursivt å definere aritmetiske operasjoner på multi-bits ord — subtraksjon, multiplikasjon, divisjon — og bitvise logiske operasjoner som logisk AND, OR, XOR, og ved gjentatt å kombinere disse, kan selv SHA-256s blokk-komprimeringsfunksjon bygges:

```
sha256-hash-block ≔ … : 𝟚²⁵⁶ × 𝟚⁵¹² ⊢ 𝟚²⁵⁶
```

SHA-256-komprimeringen er formelt definert med Simplicity innenfor bevisassistenten Rocq (tidligere Coq), med et formelt bevis på at implementasjonen av `sha256-hash-block` er korrekt.

Komprimeringen kjører for tregt som ren Simplicity. Jets utfører vanlige funksjoner som SHA-256-komprimering nativt. Rene Simplicity-implementasjoner fungerer som formelle spesifikasjoner for jets.

### Option-typer

Option-typer oppstår ved å ta en sum med unit-typen:

```
Option A ≔ 𝟙 + A
```

Typen `Option A` kan skrives som `A?` eller `𝕊 A` (hvor `𝕊` betyr "etterfølger"). Funksjoner mapper over option-typer:

```
                 f : A ⊢ B
------------------------------------------
f? ≔ copair (injl unit) (injr f) : A? ⊢ B?
```

Monadiske kombinatorer som bind kan defineres:

```
              f : A ⊢ B?
---------------------------------------
bind f ≔ copair (injl unit) f : A? ⊢ B?
```

### Buffere med variabel lengde

"Buffere" er typer for delvis fylte vektorer:

- `Aᑉ² ≔ A?`
- `Aᑉ⁴ ≔ A²? × Aᑉ²`
- `Aᑉ⁸ ≔ A⁴? × Aᑉ⁴`
- `…`

Typen `Xᑉ⁸` utvides til `(1 + X⁴) × ((1 + X²) × (1 + X))`. Ved å behandle dette som et polynom og utvide det, får man `1 + X + X² + X³ + X⁴ + X⁵ + X⁶ + X⁷`. Tolket som en type, representerer dette summen av alle mulige tupler av X opp til 7, inkludert den tomme tuppelen. Dette er nøyaktig typen for lister med lengde strengt mindre enn 8.

Som med vektorer kan mapping- og folding-operasjoner defineres over buffere. Stack-operasjoner inkluderer `push-<n : Aᑉⁿ × A ⊢ Aⁿ + Aᑉⁿ` og `pop-<n : Aᑉⁿ ⊢ (Aᑉⁿ × A)?`. `push-<n` legger til et element i bufferet, og returnerer en full vektor hvis overflyt oppstår. `pop-<n` fjerner et element, og returnerer det mindre bufferet og det fjernede elementet, eventuelt returnerer det ingenting hvis det opprinnelige bufferet var tomt.

Definisjonen av `push-<n`, rekursivt:

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

Rå Simplicity blir vanskelig å følge utover visse kompleksitetsnivåer. Sluttbrukere benytter høynivåspråk som SimplicityHL som genererer disse idiomatiske uttrykkene.

### Konklusjon

Dette kapittelet viste hvordan man bygger logiske operasjoner fra biter. Fra disse oppsto bit-nivå-aritmetikk, som muliggjør resonnering om eksekvering. Vektortyper ble utviklet, og demonstrerte iterasjon over multi-bits ord for aritmetikk-definisjon. I fortsettelsen kan kryptografiske operasjoner som SHA-256 og Schnorr-signaturvalidering defineres ved bruk av Simplicity-kombinatorer alene — alle faktisk definert ved bruk av Simplicity.

Dette kapittelet er ikke en fullstendig guide til alle mulige datatyper og operasjoner som kan bygges i Simplicity, men illustrerer oppnåelse av praktisk funksjonalitet innenfor Simplicitys begrensninger. Til tross for endelig avgrensede typer kan nyttige vektorer, buffertyper og operasjoner som itererer over disse strukturene defineres.

Faktiske spesifikasjoner for standardbibliotekoperasjoner avviker noe fra definisjonene her. For eksempel bruker full-adderen en 3-veis XOR og en "majoritets"-logikkfunksjon i stedet for to halv-addere.

I praksis bruker Simplicity-programmer jets for aritmetiske og kryptografiske operasjoner. Jets erstatter imidlertid bare uttrykk. Kombinatorer som itererer over buffere og vektorer kan ikke erstattes av jets, og de forekommer i faktiske Simplicity-programmer. Men i stedet for å bruke disse direkte, benytter sluttbrukere høynivåspråk som SimplicityHL som genererer slike uttrykk.

Rekursivt definerte kombinatorer ser ut til å vokse eksponentielt i uttrykksstørrelse. Dette er ikke problematisk. Under serialisering kodes uttrykk som DAG-er (directed acyclic graphs) i stedet for trær. Den faktiske representasjonen vokser bare lineært.

Så langt har vi bare vurdert rene beregninger. Interaksjon med transaksjonsdata for oppgaver som å signere transaksjoner krever en måte for programmer å feile på hvis signaturer er ugyldige. Neste kapittel diskuterer sideeffekter i Simplicity.

## To sideeffekter

<chapterId>9eafe498-0765-419a-a69d-a74a9cdf3713</chapterId>

I de forrige kapitlene viste vi hvordan man bygger noen datastrukturer og beregninger ved å bruke Simplicitys kjernesett av kombinatorer. Som vi bemerket, er kjernekombinatorene nok til å implementere enhver endelig ren beregning. Dette reiser spørsmålet: hva mer kan oppnås? Vi kan legge til flere sideeffekter til uttrykkene våre.

Det finnes ulike typer mulige sideeffekter for uttrykk: tilstandsoppdatering, skriving til en logg, kasting av et unntak, lesing fra et miljø, kalling av en fortsettelse, osv. Sideeffektene tilgjengelige i Simplicity vil avhenge av applikasjonen.

For Bitcoin- og Liquid-applikasjoner har vi for øyeblikket to sideeffekter: Failure-effekten, som er en unntakseffekt hvor unntaket har typen `𝟙`, og Reader-effekten som tillater tilgang til data fra transaksjonsmiljøet. Kjernekombinatorene våre er "rene"; de har ingen sideeffekter. Jets kan imidlertid introdusere nye primitiver som har sideeffekter.

### Jets med effekter

Vi vil snakke mer om jets senere i dette kurset, men her introduserer vi noen eksempeljets for å illustrere sideeffektene deres.

#### Bip0340-verify

`bip0340-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚⁵¹² ⊢ 𝟙` er en jet for et uttrykk som tar en x-only pubkey, en 256-bits melding og en Schnorr-signatur, og returnerer ingenting! I henhold til typen sin burde den oppføre seg på samme måte som en `unit`. Forskjellen ligger i jetens sideeffekt: hvis signaturvalideringen feiler, avbrytes hele beregningen ved å kaste et unntak (av unit-type). Dette er Failure-effekten.

#### Verify

`verify : 𝟚 ⊢ 𝟙` er en enkel jet for å uttrykke Failure-effekten. Hvis inputen til `verify` er `false`, avbrytes hele beregningen ved å kaste et unntak. Hvis inputen er `true`, returneres ingenting, men beregningen kan fortsette.

#### Transaksjonshasher

`sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` fremstår som en konstant funksjon, siden det bare finnes én mulig inputverdi: den tomme tuppelen. Denne jeten leser imidlertid fra transaksjonsmiljøet og produserer en hash av transaksjonsdata som er analog med `SIGHASH_ALL`-meldingsdigestet brukt i Bitcoin Scripts signaturverifisering. Dette er et eksempel på Reader-effekten: verdien som returneres, avhenger av transaksjonsmiljøet jeten kjøres innenfor. Det finnes flere andre hash-jets som hasher ulike delmengder av transaksjonsmiljødataene for å hjelpe til med å bygge tilpassede meldingsdigester for signaturer.

#### Introspeksjonsjets

`input-sequence : 𝟚³² ⊢ 𝟚³²?` er en funksjon som tar en input-indeks og returnerer transaksjonens sekvensnummer for den inputen, eventuelt returnerer den ingenting hvis indeksen er utenfor grensene. Igjen er outputverdien ikke en ren funksjon av input-indeksen, men i stedet bruker operasjonen Reader-effekten for å få tilgang til transaksjonsmiljøet for å bestemme outputverdien. Det finnes flere andre introspeksjonsjets som returnerer ulike fragmenter av transaksjonsmiljødataene.

### Klassifisering av effekter

Ikke alle sideeffekter er like. Noen sideeffekter oppfører seg penere enn andre. Vi kan klassifisere effekter etter hvor mottagelige de er for programtransformasjoner.

#### Kommutative effekter

En kommutativ effekt er en effekt hvor du, hvis du bytter outputene til to uttrykk, trygt kan bytte selve uttrykkene uten å endre uttrykkets effekt. Betrakt `swap = I H ▵ O H : A × B ⊢ B × A`. Hvis `f ▵ g ⨾ swap = g ▵ f` for hvert uttrykk `f` og `g` med sideeffekter, så er effektene kommutative.

Lesing av transaksjonsdata fra miljøet er en kommutativ effekt fordi resultatet av å lese fra miljøet er det samme, uansett hvilken rekkefølge vi utfører lesingen i.

Generelt er kasting av et unntak ikke en kommutativ effekt. Hvis `f` kaster et unntak `e₁` og `g` kaster et annet unntak `e₂`, avhenger det av rekkefølgen de utføres i hvilket unntak som kastes fra paret av `f` og `g`.

I det spesielle tilfellet med Failure-effekten, hvor bare et unit-typet unntak kan kastes, er effekten imidlertid kommutativ. Uansett om det er `f` eller `g` som kaster et unntak, vil det resulterende unntaket være det samme, fordi det bare finnes én mulig unntaksverdi.

#### Idempotente effekter

En idempotent effekt er en effekt hvor du, hvis du dupliserer outputen til et uttrykk, trygt kan duplisere selve uttrykket uten å endre uttrykkets effekt. Betrakt `dup = iden ▵ iden : A ⊢ A × A`. Hvis `f ⨾ dup = dup ⨾ f ▵ f` for hver `f` med sideeffekter, så er effektene idempotente.

Lesing av transaksjonsdata fra miljøet er en idempotent effekt. Kasting av et unntak er også en idempotent effekt. Selv om bare ett av de to dupliserte uttrykkene vil bli utført, vil ethvert unntak kastet av `dup ⨾ f ▵ f` være det samme som unntaket kastet av `f ⨾ dup`.

Skriving til en logg er imidlertid kanskje ikke idempotent, siden duplisering av effekten ville føre til at loggmeldingen vises to ganger. Men hvis loggen består av et _sett_ med meldinger i stedet for en _liste_ med meldinger, ville effekten være idempotent (og kommutativ), fordi settinnsetting i seg selv er en idempotent operasjon.

#### Unitære effekter

En unitær effekt er en effekt hvor du, hvis du forkaster outputen til et uttrykk, trygt kan forkaste selve uttrykket uten å endre uttrykkets effekter. Hvis det alltid er tilfelle at `f ⨾ unit = unit` for hver `f` med sideeffekter, er effektene dine unitære.

Lesing av data fra miljøet er en av de få typene unitære effekter. Hvis resultatet av å lese transaksjonsdata fra miljøet forkastes, kan hele uttrykket som utfører lesingen, forkastes.

Failure-effekten er ikke unitær. Hvis `f` kaster et unntak, vil også `f ⨾ unit` gjøre det; eksekveringen kommer ikke engang til `unit`-kombinatoren før beregningen avbrytes. På den annen side ville `unit` åpenbart ikke kaste noe unntak, så effektene av `f ⨾ unit` og `unit` ville være forskjellige.

For å oppsummere, her er hvordan effektene diskutert ovenfor forholder seg til disse tre egenskapene:

| Effect | Commutative | Idempotent | Unitary |
| --- | :---: | :---: | :---: |
| Reader (transaction environment) | ✓ | ✓ | ✓ |
| Failure (unit-typed exception) | ✓ | ✓ | ✗ |
| Writer (log as a set) | ✓ | ✓ | ✗ |
| General exceptions (arbitrary type) | ✗ | ✓ | ✗ |

### Effekter tillatt i Simplicity

Jo bedre oppførselen til en type effekt er, jo mer rom har en Simplicity-optimalisering for å transformere programmer som bruker de effektene. Ideelt sett ville vi bare tillate effekter som har alle tre egenskapene: kommutativ, idempotent og unitær. Dette ville tillate en optimalisering å utføre enhver programtransformasjon den ønsker. Imidlertid er lesing fra et miljø den eneste effekten som tilfredsstiller alle tre egenskapene.

I stedet krever vi at Simplicity-effekter er kommutative og idempotente. Begge effektene vi bruker i Simplicity, Failure-effekten og Reader-effekten, er kommutative og idempotente. Dette gjør det mulig å utføre en stor klasse optimaliseringer på Simplicity-kode.

Imidlertid er "forkastnings"-transformasjonen beskrevet ovenfor, som forsøker å erstatte `f ⨾ unit` med `unit`, eller enhver lignende transformasjon, ikke tillatt hvis `f` kan produsere en Failure-effekt. Forestill deg for eksempel at `f` inneholdt en `bip0340-verify`-assertion. Det ville vært katastrofalt å forsøke å optimalisere bort den sjekken.

### Hvorfor tillate sideeffekter i det hele tatt?

Hvorfor tillater Simplicity i det hele tatt sideeffekter? Ville det ikke vært bedre om hvert program tok hele transaksjonen som input og returnerte en boolsk output som avgjør om en transaksjon er gyldig eller ikke?

#### Batchverifisering

En grunn til at vi har Failure-effekten, er å støtte [batchverifisering](https://github.com/bitcoin/bips/blob/c9a6ca6297eb8de850f6b64dafb8e60ee9b64d66/bip-0340.mediawiki#batch-verification) av Schnorr-signaturer. I batchverifisering slås mange individuelle Schnorr-signatursjekker sammen på en slik måte at hvis én enkelt signatursjekk feiler, feiler hele batchen.

Denne batchprosedyren forbedrer effektiviteten sammenlignet med å verifisere hver signatur individuelt. Ulempen er at hvis batchverifiseringen feiler, får vi ikke vite hvilken spesifikk signatursjekk eller sjekker som feilet.

Ved å bruke failure-sideeffekten sikrer `bip0340-verify` at hvis en signatursjekk feiler, feiler hele transaksjonen. Hvis `bip0340-verify` i stedet skulle returnere `𝟚`, en boolsk type, for suksess eller feil, kunne en mislykket signatursjekk fortsatt føre til en gren hvor skriptet lykkes. I et slikt tilfelle måtte vi vite om den bestemte signaturen er gyldig eller ikke, og dermed ville vi ikke kunne dra nytte av batchverifisering.

#### Forhåndsberegnet transaksjonsdata

Et problem i tidlig Bitcoin Script var at hashfunksjonen brukt til å lage meldingsdigester for signaturer var lineær i størrelsen på transaksjonen. Vanligvis skaper hver input minst ett meldingsdigest for signaturverifisering, så samlet sett var mengden hashing kvadratisk i transaksjonsstørrelsen.

Dette problemet ble løst i Segwit og senere iterasjoner av Bitcoin Script ved å redefinere meldingsdigestene slik at de kunne beregnes i konstant tid per signatursjekk. Dette er avhengig av å ha `PrecomputedTransactionData`, som forhåndsberegner hasher av transaksjonsdata én gang og deretter deles av hver inputs sighash-beregninger. Simplicitys transaksjonshash-jets er avhengige av den samme typen forhåndsberegnet transaksjonsdata for å sikre at jetene kjører i konstant tid.

Anta at `sig-all-hash` ikke brukte Reader-effekten. Anta at vi på en eller annen måte klarte å bygge en Simplicity-type for transaksjonsmiljøet. La oss kalle den `TxEnv`, slik at `sig-all-hash : TxEnv ⊢ 𝟚²⁵⁶` var jetens type. En slik definisjon ville kreve at `sig-all-hash`-jeten kunne beregne hashen til enhver transaksjon, ikke bare transaksjonen den er involvert med. Simplicity-programmer kunne kopiere det gitte `TxEnv`-et og sende en modifisert kopi av det til `sig-all-hash`. I et slikt tilfelle kunne `sig-all-hash` ikke stole på `PrecomputedTransactionData`, og vi ville være tilbake til å kreve lineær tid i uansett hvilken transaksjonsdata som ble sendt inn i denne versjonen av `sig-all-hash`.

Fordi `sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` bruker Reader-effekten for å få tilgang til transaksjonsdataen, får den _bare_ tilgang til et fast transaksjonsmiljø. Av den grunn kan jetens implementasjon trygt bruke `PrecomputedTransactionData` og operere i konstant tid.

### Kryssinput-signaturaggregering

Selv om verken Liquid eller Bitcoin støtter [kryssinput-signaturaggregering](https://hrf.org/latest/cisa-research-paper/) på nåværende tidspunkt, vil vi gjerne sjekke at Simplicity kan være kompatibel med det når tiden kommer.

Selv om detaljene ikke er utarbeidet, ser vi for oss at halv-aggregering implementeres ved bruk av en Writer-effekt. Det vil si at en ny jet med en type som `half-agg-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚²⁵⁶ ⊢ 𝟙` ville ta en offentlig nøkkel, et meldingsdigest, og `r`-komponenten til en Schnorr-signatur (en Schnorr-signatur består av en `r`-komponent og en `s`-komponent) og skrive det til en transaksjonslogg før den fortsetter med eksekvering. Deretter, et annet sted i transaksjonen eller med transaksjonen, ville en aggregert `s`-komponent for alle halv-aggregerte Schnorr-signaturer bli oppgitt. Transaksjonen ville bare være gyldig når en slik aggregert `s`-komponent er oppgitt for alle de loggførte nøklene, meldingene og `r`-komponentene.

For å oppfylle Simplicitys krav må denne Writer-effekten være idempotent og kommutativ. Dette kan sikres ved å behandle skriverloggen som et sett med tupler av nøkkel, melding og `r`-komponent. Dette fungerer fordi settoperasjoner er idempotente og kommutative. Å behandle loggen som et sett med verdier ville være kompatibelt med halv-aggregeringsverifiseringsalgoritmen.

### Konklusjon

I dette kapittelet så vi på å legge til sideeffekter til beregningene Simplicity kan gjøre. Vi klassifiserte ulike typer effekter etter hvor godt de oppfører seg med hensyn til ulike typer programtransformasjon. Vi bestemte oss for å begrense Simplicitys effekter til de som er kommutative og idempotente.

De to effektene vi bruker for Bitcoin- og Liquid-applikasjoner er Reader-effekten, for å få tilgang til transaksjonsmiljøet, og Failure-effekten, for å avbryte og få programmet til å feile. Noen jets bruker primitive operasjoner hvor disse typene sideeffekter kan forekomme.

Failure-effekten bestemmer outputen til et Simplicity-program: programmet feiler enten, noe som gjør transaksjonen ugyldig, eller programmet lykkes. Reader-effekten gir én type input til et Simplicity-program: miljøet som inneholder transaksjonsdata. Men vi må også tilby andre inputer, som digitale signaturer, til Simplicity-programmer.

I neste kapittel skal vi se på hva Simplicity-programmer er, hvordan de blir til adresser, og hvordan vi legger til andre inputer, som signaturer, til Simplicity-programmer.

## Programmer og adresser

<chapterId>961652e3-8f7d-4c2a-8b55-9a990b91a0dd</chapterId>

I forrige kapittel beskrev vi to sideeffekter brukt i Simplicity: Failure-effekten, som avgjør et programs suksess eller feil, og Reader-effekten, som gir tilgang til transaksjonsmiljøet. Nå vender vi oss til det praktiske spørsmålet: hva er egentlig et Simplicity-program, og hvordan blir det til en adresse på blokkjeden?

### Simplicity-programmer

Et Simplicity-program er definert som et Simplicity-uttrykk av typen `𝟙 ⊢ 𝟙`. Denne typesignaturen betyr at programmet ikke tar noen meningsfull input (bare unit-verdien) og produserer ingen meningsfull output (bare unit-verdien). Reader-effekten fanger opp inputen fra transaksjonsmiljøet, mens Failure-effekten indikerer suksess eller feil. Disse effektene håndterer I/O snarere enn Simplicity-typene selv.

### Commitment Merkle Root

I stedet for å lagre komplette programmer on-chain, bruker Bitcoin forpliktelser (commitments) — en praksis som stammer fra Pay-to-Script-Hash (P2SH). Simplicity bruker en Commitment Merkle Root (CMR).

Hver kombinator mottar en SHA-256-tag utledet fra mønsteret: `Simplicity␟Commitment␟[identifier]`, hvor `␟` representerer ASCII-kode 31 (unit separator).

Hver tag er SHA-256-hashen av den tilsvarende pre-image-strengen listet opp nedenfor:

| Combinator | Tag pre-image (ASCII string) |
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

Et Simplicity-uttrykk hashes deretter rekursivt til en 256-bits CMR ved å beregne en tagget SHA-256-midtstate for hver kombinator sammen med CMR-ene til argumentene (skriv `#ᶜ(e)` for CMR-en til uttrykket `e`, og `∥` for byte-sammenkjeding):

| Combinator | CMR rule |
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

Binære kombinatorer (`comp`, `pair`, `case`) sammenkjeder CMR-ene til begge barn; unære kombinatorer (`take`, `drop`, `injl`, `injr`) sammenkjeder det ene barnets CMR etter 32 byte med `0x00`-padding; og de nullære bladene (`iden`, `unit`) hasher taggen sin alene. To konvensjoner holder dette billig å beregne: SHA-256-midtstater brukes slik at **hvert uttrykk krever maksimalt ett kall til SHA-256-komprimeringsfunksjonen** (forutsatt at midtstaten opp til de konstante taggene er forhåndsberegnet), og énargumentkonstruktørene prefikser argumentet sitt med 32 byte med `0x00`-padding, noe som gir litt ekstra rom for forhåndsberegning for implementasjoner som ønsker det.

For `unit`-kombinatoren — en nullær konstruktør uten argument-deluttrykk — spesialiserer denne regelen seg til `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)`, hvor `tag_unit = SHA-256(Simplicity␟Commitment␟unit)` (taggen mates inn to ganger). Den resulterende CMR-en for det trivielle `unit`-programmet er:

```
0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

Avgjørende er at CMR-en ikke forplikter seg til typene til Simplicity-uttrykk, men i stedet stoler på typeinferens under innløsning.

### Adresser

Adresser bruker BIP-0341s Taproot-mekanisme med CMR-er forpliktet under TapLeaf-versjon `0xbe`. Prosessen involverer:

1. Beregning av en TapLeaf-tagget hash som kombinerer versjonsbyten, CMR-lengden og selve CMR-en
2. Tweaking av en intern offentlig nøkkel (ved bruk av et NUMS-punkt når ingen nøkkelbrukssti er ønsket)
3. Konvertering til bech32m-format
4. Tillegg av passende sjekksummer

Når ingen nøkkelbrukssti er ønsket, settes den interne offentlige nøkkelen til et **NUMS**-punkt ("Nothing-Up-My-Sleeve"): et kurvepunkt bevisst valgt slik at ingen kjenner dets diskrete logaritme — med andre ord et punkt uten tilsvarende privat nøkkel. Fordi ingen noensinne kan produsere en signatur for det, er nøkkelbrukstien beviselig ubrukelig, og outputen kan bare brukes gjennom den forpliktede Simplicity-skriptstien. I en reell applikasjon bør dette NUMS-punktet randomiseres som anbefalt av BIP-0341, slik at outputer uten nøkkelbrukssti er umulige å skille fra ordinære Taproot-outputer (en personvernfordel).

#### Fra Simplicity til adresse

La oss gå gjennom hele utledningen for det enklest mulige programmet: `unit : 𝟙 ⊢ 𝟙`, en no-op som alltid lykkes.

**1. Kombinatortag.** Beregn først `unit`-taggen:

```
tag_unit = SHA-256(Simplicity␟Commitment␟unit)
         = 0xd723083cff3c75e29f296707ecf2750338f100591c86e0c71717f807ff3cf69d
```

**2. CMR.** Mat taggen inn to ganger for å oppnå programmets CMR:

```
CMR = #ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)
    = 0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

**3. TapLeaf-hash.** Prefiks CMR-en med Simplicitys TapLeaf-versjon `0xbe` og CMR-lengden `0x20` (32 byte), og ta deretter Elements' TapLeaf-taggede hash (en tagget hash er `hash_str(x) = SHA-256(SHA-256(str) ∥ SHA-256(str) ∥ x)`):

```
hash_TapLeaf/elements(0xbe ∥ 0x20 ∥ CMR)
  = 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c
```

Med bare dette ene bladet finnes det ingen TapBranches, så denne hashen er allerede TapTree-roten.

**4. TapTweak.** Siden vi ikke vil ha noen nøkkelbrukssti, bruker vi BIP-0341 NUMS-punktet som intern nøkkel og tweaker det med TapTree-roten:

```
internal_pk = 0x50929b74c1a04954b78b4b6035e97a5e078a5a0f28ec96d547bfee9ace803ac0
t = hash_TapTweak/elements(internal_pk ∥ 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c)
  = 0xb3bef172389b0937d7e5a8b15cfa41e776777f13f2f659cb06220a6ff0658285
```

**5. Output-nøkkel.** Tweak den interne nøkkelen på kurven, `output_pk = lift_x(internal_pk) ⊕ t·G` (den elliptiske kurve-aritmetikken er oppsummert her), noe som gir x-only output-nøkkelen `0x2cb0c20acd7340b4d4b65f6a60e2888d0d64e3267261f3b3cf7290e5af3f9e09`.

**6. Bech32m-adresse.** Kod x-only output-nøkkelen, prefiks en `p` (SegWit v1 witness-versjonstegnet), legg til Liquid-testnettets menneskelesbare prefiks `tex1`, og legg til Bech32m-sjekksummen. Den endelige adressen er:

```
tex1p9jcvyzkdwdqtf49kta4xpc5g35xkfcexwfsl8v70w2gwttelncyshxjk56
```

Det var mye arbeid — men mye av det er pålagt av Taproot selv, ikke av Simplicity.

### Vitneuttrykk

En ny kombinatortype adresserer fraværet av input til Simplicity-programmer: vitneuttrykket. `witness`-kombinatoren tillater at signaturdata og annet vitnemateriale integreres i programmer.

```
      w : B
-----------------
witness w : A ⊢ B
```

Vitneuttrykkets semantikk er enkel: det ignorerer inputen sin og returnerer bare verdien `w` (som kan være av enhver Simplicity-type), altså `⟦witness w⟧(a) = w`. Dette gir **ingen ny uttrykksevne** — ifølge fullstendighetsteoremet kan Simplicity allerede bygge enhver slik konstant funksjon (husk `scribe`-makroen fra de forrige kapitlene). Poenget med `witness`-kombinatoren ligger utelukkende i dens **CMR**: verdien `w` er **ekskludert** fra uttrykkets CMR, slik at adressen kan beregnes før `w` er kjent, og `w` leveres ved innløsningstidspunktet.

Dette designvalget støtter beskjæring — ikke-utførte betingede grener trenger ikke å avsløres on-chain, inkludert deres tilknyttede vitneuttrykk. Når en gren beskjæres, trenger verifikatoren bare CMR-en til det beskårne deltreet, ikke dets faktiske innhold.

### Vitneverdier

Det kan virke som en begrensning at et vitneuttrykk bare kan inneholde en *verdi*, og ikke et mer generelt Simplicity-uttrykk. Men programmer for UTXO-baserte blokkjeder utføres bare én gang. Det er ikke nødvendig å sende et helt deluttrykk inn i en vitneknute: brukeren kan ganske enkelt kjøre det deluttrykket selv, off-chain, og transkribere outputen inn i vitneverdien for å oppnå akkurat det samme resultatet.

(Senere i dette kurset skal vi møte `disconnect`-kombinatoren, som oppfører seg mye som et vitneuttrykk som *faktisk* tar et helt Simplicity-uttrykk som argument.)

Et alternativt design ville mate all vitnedata inn som et argument til det øverste Simplicity-programmet. Vitneuttrykk foretrekkes av to grunner. For det første, **beskjæring**: ikke-utførte grener av `case`-uttrykk avsløres aldri on-chain, og eventuelle vitneuttrykk inne i de grenene beskjæres bort sammen med dem. For det andre, **lokalitet**: vitneuttrykk lar oss plassere hver vitneverdi akkurat der den brukes, i stedet for å tre den ned fra programmets øverste input.

### Typeinferens

Siden CMR-er ikke forplikter seg til typer, rekonstrueres typesystemet under innløsning. Simplicitys typeinferens-algoritme bestemmer de minimale typene for hvert deluttrykk basert på kombinatorstrukturen. Mer presist beregner inferensen den *prinsipielle* (mest generelle) typen til hvert deluttrykk; eventuelle typevariabler som forblir frie, blir deretter instansiert til unit-typen `𝟙`, som gir en unik, minimal type for programmet.

### Konklusjon

I dette kapittelet fastslo vi at Simplicity-programmer er uttrykk av typen `𝟙 ⊢ 𝟙`, forklarte hvordan Commitment Merkle Roots konstrueres fra taggede SHA-256-hasher av hver kombinator, og viste hvordan CMR-er blir til on-chain-adresser via BIP-0341 Taproot. Vi introduserte vitneuttrykk som mekanismen for å tilby signaturdata og andre inputer ved bruk uten å forplikte seg til verdiene deres ved adresseopprettelse.

# Siste seksjon

<partId>96952535-4aa6-4e78-91e2-d12e9df895d4</partId>

## Anmeldelser og vurderinger

<chapterId>fb0b0133-39ea-497b-bd36-198be42c4fab</chapterId>
<isCourseReview>true</isCourseReview>

## Avsluttende eksamen

<chapterId>2cc5e818-abcb-4a0a-9991-7a492c572e2d</chapterId>
<isCourseExam>true</isCourseExam>

## Konklusjon

<chapterId>8ade24bd-a84f-4d25-8f64-bdfa8b58926c</chapterId>
<isCourseConclusion>true</isCourseConclusion>