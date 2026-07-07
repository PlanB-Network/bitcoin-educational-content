---
name: Verdieping in Simplicity
goal: Beheers de ontwerpfilosofie, het typesysteem en de volledige levenscyclus van Simplicity
objectives:
  - Begrijp de drie fundamentele compositiemethoden en de negen combinators die een complete taal vormen
  - Bouw booleaanse logica, rekenkunde en SHA-256 vanuit Simplicity's minimale typesysteem
  - Begrijp hoe de Failure- en Reader-neveneffecten echte blockchain-interactie mogelijk maken
  - Leer hoe Simplicity-programma's Taproot-adressen worden en worden ingelost met witness-data
---

# Verdieping in Simplicity

Een diepgaande verkenning van de theorie en ontwerpbeslissingen achter de Simplicity-taal, gebaseerd op de volledige vijfdelige artikelenreeks ["Delving Simplicity"](https://delvingbitcoin.org/t/delving-simplicity-part-three-fundamental-ways-of-combining-computations/1902) van [Dr. Russell O'Connor](https://r6.ca/), de bedenker van Simplicity bij Blockstream Research. Deze cursus legt uit *waarom* Simplicity op deze manier is ontworpen, niet hoe je ermee programmeert.

Deze cursus volgt de artikelen van Dr. O'Connor door de drie fundamentele manieren om berekeningen te combineren, het minimale typesysteem en de bijbehorende volledigheidsstelling, de opbouw van praktische datatypes en rekenkunde vanuit eerste beginselen, de zorgvuldige introductie van neveneffecten voor blockchain-interactie, en ten slotte hoe programma's worden vastgelegd in adressen en on-chain worden ingelost.

+++

# Inleiding

<partId>c362889b-c630-435f-911b-724c4eca505b</partId>

## Cursusoverzicht

<chapterId>cdcc40b6-c985-45b4-9bee-6f931e984476</chapterId>

Welkom bij SCR403 — Verdieping in Simplicity!

Deze cursus is gebaseerd op de artikelenreeks **"Delving Simplicity"**, geschreven door [Dr. Russell O'Connor](https://r6.ca/), Infrastructure Tech Developer bij [Blockstream](https://blockstream.com/) en de bedenker van Simplicity. De originele artikelen werden gepubliceerd op het [Delving Bitcoin](https://delvingbitcoin.org/u/roconnor-blockstream/summary)-forum en vormen het primaire bronmateriaal voor deze cursus. We zijn dankbaar voor zijn baanbrekende werk, dat deze educatieve inhoud mogelijk heeft gemaakt.

### Wat je zult leren

Deze cursus verkent de ontwerpfilosofie en wiskundige grondslagen achter Simplicity, de scriptingtaal van de volgende generatie die in juli 2025 werd geactiveerd op het [Liquid Network](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/). De cursus volgt de volledige vijfdelige artikelenreeks en is opgebouwd uit twee hoofdonderdelen:

1. **Grondslagen van Simplicity** — Waarom blockchain-berekeningen een fundamenteel andere taal vereisen, de drie manieren om operaties te combineren (sequentieel, parallel, conditioneel), en de negen kerncombinators die een wiskundig complete taal vormen
2. **Van datatypes naar programma's** — Het bouwen van booleaanse logica, rekenkunde en SHA-256 vanuit eerste beginselen; het begrijpen van de Failure- en Reader-neveneffecten die blockchain-interactie mogelijk maken; en het leren hoe programma's via Commitment Merkle Roots worden vastgelegd in Taproot-adressen en worden ingelost met witness-data

### Vereisten

Dit is een cursus op **expertniveau** (ongeveer 10 uur). Je moet vertrouwd zijn met:
- Basisconcepten van Bitcoin scripting (wat transactievalidatie doet)
- Fundamentele programmeerconcepten (types, functies, compositie)
- Enige bekendheid met wiskundige notatie is nuttig maar niet vereist. We introduceren alles gaandeweg

### Belangrijke bronnen

- **Originele artikelen**: ["Delving Simplicity"](https://delvingbitcoin.org/u/roconnor-blockstream/summary) van Dr. Russell O'Connor op Delving Bitcoin
- **Simplicity-repository**: [BlockstreamResearch/simplicity](https://github.com/BlockstreamResearch/simplicity) — broncode en formele Rocq-bewijzen
- **Officiële website**: [simplicity-lang.org](https://simplicity-lang.org/) — documentatie en SimplicityHL-referentie
- **Blockstream-blog**: [Simplicity on GitHub](https://blog.blockstream.com/en-simplicity-github/) — technisch overzicht

Klaar om je te verdiepen in een van de meest elegante staaltjes Bitcoin-engineering? Laten we beginnen!

## Wat is Simplicity?

<chapterId>d04f3960-d7fb-44e1-b5a3-25b33d03fd38</chapterId>

Als je deze cursus begint zonder achtergrond in Simplicity, geeft dit hoofdstuk je de oriëntatie voordat we de diepte induiken.

### Simplicity in een notendop

Simplicity is een **Bitcoin-native smart contract-taal**, die vandaag actief is op het Liquid Network. Voor het eerst bedacht door Dr. Russell O'Connor rond 2012 en uitgewerkt in zijn paper uit 2017 *Simplicity: A New Language for Blockchains*, werd het in juli 2025 geactiveerd op het Liquid Network, na jaren van formele verificatie en ontwikkeling.

In tegenstelling tot Ethereums Solidity, een Turing-complete, high-level contracttaal, is Simplicity opzettelijk minimaal. Het heeft:
- **Drie typeconstructoren** (unit, sum, product)
- **Negen combinators** (basisoperaties en compositieregels)
- **Geen lussen, geen recursie, geen dynamisch geheugen**

Met alleen deze primitieven kun je elke berekening bouwen die je nodig hebt voor transactievalidatie, van booleaanse logica tot volledige SHA-256-hashing.

### Wat kun je vandaag met Simplicity doen?

Simplicity draait vandaag al onder echte toepassingen op het Liquid Network. De bekendste is de [Simplicity DEX](https://docs.simplicity-lang.org/use-cases/simplicity-dex/), een oracle-vrije optiesmarktplaats waar gebruikers callopties op L-BTC verhandelen met USDt als onderpand (het onderliggende contract ondersteunt ook putopties). Andere live Simplicity-projecten zijn [Swaption](https://swaption.io/) van SideSwap (opties) en het open-source [Deadcat](https://github.com/Resolvr-io/deadcat) van Resolvr (voorspellingsmarkten). Naast DeFi maakt Simplicity geavanceerde bestedingsvoorwaarden mogelijk, zoals vaults, covenants en complexe multisig-schema's die in Bitcoin Script onmogelijk of onveilig zouden zijn.

### Wat deze cursus wel — en niet — is

Dit is **geen** hands-on codeertutorial. Je zult hier geen Simplicity-programma's schrijven. Als je daarnaar op zoek bent, bekijk dan:
- [simplicity-lang.org](https://simplicity-lang.org/) — officiële documentatie en de high-level taal SimplicityHL
- De [Simplicity GitHub-repository](https://github.com/BlockstreamResearch/simplicity) — referentie-implementatie, voorbeelden en Rocq-bewijzen
- De [Blockstream-blogpost](https://blog.blockstream.com/en-simplicity-github/) over hoe je aan de slag gaat

Waar deze cursus **wel** over gaat: de **filosofische en technische keuzes** achter het ontwerp van Simplicity. Waarom is deze taal op deze manier gemaakt? Waarom slechts negen combinators? Waarom geen recursie? Waarom is het van belang dat het typesysteem verbonden is met Gentzens sequentenkalkul?

Zie het als het begrijpen van **waarom de motor zo is gebouwd**, in plaats van leren autorijden.

### Voor wie is dit?

Deze cursus is ideaal voor:
- **Protocolontwikkelaars** die de grondslagen van Simplicity willen begrijpen voordat ze code schrijven
- **Bitcoin-onderzoekers** die geïnteresseerd zijn in de formele verificatie en de typetheoretische benadering
- **Informatici** die nieuwsgierig zijn naar de verbinding tussen sequentenkalkul en blockchain-berekeningen
- **Gevorderde bitcoiners** die verder willen kijken dan een oppervlakkig begrip van de scriptingmogelijkheden van Liquid

Als termen als "sum types", "combinators" of "sequentenkalkul" volledig nieuw voor je zijn, geen zorgen: we leggen alles vanaf nul uit. Maar bereid je voor op een dichte, wiskundige reis.

### Van artikelen naar cursus

De originele "Delving Simplicity"-reeks van Dr. O'Connor is opgebouwd uit vijf technische artikelen. Deze cursus herstructureert en annoteert dat materiaal tot een progressief leertraject met quizzen om je begrip onderweg te toetsen. De ideeën, definities en bewijzen zijn van hem; wij hebben het format aangepast voor gestructureerd onderwijs.

# Grondslagen van Simplicity

<partId>a5976618-94ab-4b29-b9aa-040d35c68e5d</partId>

## Fundamentele manieren om berekeningen te combineren

<chapterId>6d46e77a-7e60-473b-b230-418da5ae44eb</chapterId>

Nu Simplicity is geactiveerd op het Liquid Network, wil ik een diepgaande verkenning doen van de filosofie en het ontwerp van de Simplicity-taal.

Transactievalidatie in Bitcoin is een fundamenteel andere toepassing dan het ontwerpen van reguliere programmeertalen. Blockruimte is schaars, dus programma's moeten compact zijn. Programma's in Bitcoin-transacties worden altijd slechts op één input uitgevoerd, en iedereen voert het programma uit op dezelfde input. Bovendien kent de partij die de transactie autoriseert de uitkomst van de berekening al van tevoren: dat de transactie geldig is.

Doorgaans voert de autoriserende partij veel duurdere berekeningen uit om witness-data af te leiden die de geldigheid van de transactie aantoont, terwijl programma's die op de blockchain draaien alleen die witness-data op geldigheid hoeven te controleren. Geldigheid controleren is vaak veel goedkoper dan geldigheid bewijzen.

We hebben Simplicity ontworpen met dit soort unieke uitdagingen op het gebied van taalontwerp in gedachten. Zo vereist Simplicity dat niet-uitgevoerde takken worden weggesnoeid, zodat ze niet op de blockchain verschijnen. Voorbewerkingsstappen zijn zorgvuldig ontworpen om een (quasi-)lineaire tijdscomplexiteit te vertonen ten opzichte van de grootte van het Simplicity-programma. In plaats van "gas", dat niet kan worden berekend zonder code op een voorgeschreven manier uit te voeren, wordt statische analyse gebruikt, zodat de details van het uitvoeringsmodel niet consensuskritisch worden. Geen dynamische geheugentoewijzing tijdens uitvoering. Enzovoort.

Voordat we ingaan op de ontwerpdetails van Simplicity, wil ik deze reeks beginnen met wat programmeerfilosofie over de algemene manieren om basisbouwstenen te combineren tot nieuwe functionaliteit.

### Compositie

Stel dat iemand een taal ontwerpt voor programmeerbare transacties voor een blockchain zoals Bitcoin. Programma's hebben dan alleen toegang tot de transactiedata en de UTXO-data van de inputs, en de uitvoering bepaalt alleen de geldigheid van de transactie (waardoor het resultaat van de uitvoering gecachet kan worden). Stel dat men begint met een verzameling basisoperaties die verschillende taken kunnen uitvoeren, zoals basisberekeningen, het lezen en/of verwerken van data uit de transactie, en handtekeningverificatie. Elke operatie verbruikt een bepaald type input (mogelijk leeg) en levert een bepaald type output. Op welke manieren kunnen we deze basisoperaties combineren tot complexere operaties?

### Sequentiële compositie

![Sequentiële compositie](assets/en/001.webp)

De meest fundamentele compositiemethode is sequentiële compositie. Als we twee basisoperaties hebben waarvan het outputtype van de ene overeenkomt met het inputtype van de andere, dan kunnen we deze twee operaties combineren tot een nieuwe samengestelde operatie. Deze nieuwe operatie voert de twee basisoperaties na elkaar uit: ze neemt als input de input van de eerste operatie, geeft de output van die eerste operatie door als input voor de tweede operatie, en levert uiteindelijk de output van die tweede operatie.

Natuurlijk hoeven we ons niet te beperken tot het combineren van basisoperaties. Nu we een aantal samengestelde operaties hebben, kunnen we die ook combineren via functionele compositie.

In de wiskunde wordt deze sequentiële compositie vaak simpelweg "compositie" genoemd, en men zou kunnen denken dat dit de enige manier is om dingen te combineren. We hebben echter nog andere manieren om operaties te combineren.

### Parallelle compositie

![Parallelle compositie](assets/en/002.webp)

Stel dat we twee operaties hebben — dit kunnen basis- of complexe operaties zijn — die beide hetzelfde inputtype nemen. Een tweede fundamentele manier om deze twee operaties te combineren, is ze beide op dezelfde input uit te voeren. Dit heet parallelle compositie, en het outputtype is het "product" van de outputtypes van de oorspronkelijke operaties, en bevat het paar van de twee outputs.

Hoewel dit "parallelle" compositie wordt genoemd en de twee operaties in principe parallel zouden kunnen worden uitgevoerd, is parallelle uitvoering geen operationele vereiste. We kunnen parallelle compositie ook "sequentieel" implementeren door eerst de ene operatie en dan de tweede operatie uit te voeren. Het maakt ons niet uit hoe parallelle compositie precies wordt geïmplementeerd, zolang de output maar hetzelfde is.

### Conditionele compositie

![Conditionele compositie](assets/en/003.webp)

Conditionele compositie is het duale van parallelle compositie. In dit geval hebben we twee operaties die dezelfde output produceren, en combineren we ze door er één te kiezen om uit te voeren. De input van deze samengestelde operatie is de "som" of "tagged union" van de inputtypes van de oorspronkelijke operaties. De tag, "Left" of "Right", is hierbij één bit in de inputdata die bepaalt welk type data wordt meegedragen, en dus welke van de twee operaties kan worden uitgevoerd.

Conditionele compositie werkt op dezelfde manier, zelfs wanneer de input de som is van twee identieke types. Het somtype bevat nog steeds een tag, en de waarde van die tag bepaalt welke van de twee operaties wordt uitgevoerd.

### Compositie in Bitcoin Script

Er zijn veel manieren om deze drie soorten compositie te realiseren in verschillende programmeertalen. In Bitcoin Script wordt sequentiële compositie (bij benadering) gerealiseerd door de aaneenschakeling van twee routines (dit is waarom Bitcoin Script een concatenatieve programmeertaal wordt genoemd), aangezien de output van de ene routine op de stack achterblijft om door de volgende routine te worden geconsumeerd. Parallelle compositie wordt bereikt door duplicate- en swap-operaties te gebruiken om de stack zo te manipuleren dat twee routines op dezelfde input kunnen worden uitgevoerd. Dit is niet helemaal rechttoe rechtaan, aangezien wat wij het "product" van types noemen typisch wordt gerealiseerd met meerdere stack-items. Hopelijk zie je het algemene idee.

Conditionele compositie wordt uiteraard gerealiseerd door `OP_IF`, dat vertakt op basis van de waarde op de stack. Hierbij speelt het bovenste stack-item de rol van tag, en zijn het volgende item of de volgende items op de stack meestal van een ander "type", afhankelijk van de waarde van de tag. Voor elk geval kunnen de types van de stack-items alleen geschikt zijn voor verwerking door één van de takken in de `OP_IF`. Zodra we echter bij `OP_ENDIF` aankomen, moeten de stack-items van een consistent "type" zijn, zodat het resterende script verder kan gaan ongeacht welke tak eerder werd genomen.

### Compositie in Simplicity

We hebben Simplicity ontworpen met combinators die deze drie vormen van compositie rechtstreeks implementeren. Samen met een paar extra combinators die andere basisoperaties rond product- en somtypes ondersteunen, bestaat de kerntaal van Simplicity uiteindelijk uit negen combinators die voldoende zijn om elke eindige berekening uit te drukken. We bespreken dit in meer detail in het volgende hoofdstuk.

### Een vierde soort compositie

Voordat we afsluiten, moeten we vermelden dat er in de informatica nog minstens één andere vorm van compositie bestaat: "recursieve compositie". Bij recursieve compositie wordt één operatie meerdere keren herhaald.

Merk op dat Bitcoin Script recursieve compositie niet ondersteunt, en op dezelfde manier hebben we onbegrensde recursie expliciet uitgesloten van het ontwerp van Simplicity. Onze stelling is dat onbegrensde iteratieve berekening beter kan worden geïmplementeerd met recursieve covenants die over meerdere transacties heen rekenen. Dit stelt gebruikers in staat om blockruimte- en standaardness-beperkingen te vermijden en transactiekosten beter te voorspellen.

Dat gezegd hebbende, er zijn manieren om Simplicity's delegatiefunctie te misbruiken om iets te bereiken dat lijkt op onbegrensde recursieve compositie; we bespreken dit mogelijk later in deze reeks.

### Conclusie

We hebben de drie belangrijkste vormen van compositie besproken voor het omzetten van basisoperaties in complexe operaties:

- sequentiële compositie
- parallelle compositie
- conditionele compositie

We hebben besproken hoe deze vormen van compositie in Bitcoin Script worden gerealiseerd, en een tipje van de sluier gelicht over hoe ze het ontwerp van de Simplicity-taal hebben beïnvloed. We merkten op dat de vierde soort compositie, recursieve compositie, specifiek is uitgesloten van zowel Simplicity als Bitcoin Script.

In het volgende hoofdstuk beschrijven we de negen combinators die de kern van de Simplicity-taal vormen, hoe ze dienen om deze drie vormen van compositie rechtstreeks te realiseren, en hoe dit een complete taal vormt om elke eindige berekening te beschrijven.

## Combinatorvolledigheid van Simplicity

<chapterId>2a10a6ba-fada-4556-a673-3ae8c0794bf0</chapterId>

In dit hoofdstuk introduceren we de kerntaal van Simplicity en tonen we aan dat de taal compleet is, wat betekent dat elke eindige berekening erbinnen kan worden uitgedrukt.

### Simplicity-types

Simplicity ondersteunt drie fundamentele typeconstructoren. Het producttype `A × B` staat voor outputs van parallelle compositie, terwijl het somtype `A + B` (tagged union) inputs van conditionele compositie afhandelt. Het derde type is het unit-type.

### Unit-type

Het unit-type, aangeduid als `𝟙` of `ONE`, bevat precies één waarde: de lege tuple `⟨⟩` of `()`. Dit nul-bit-datatype draagt geen informatie.

### Somtype

Een somtype `A + B` combineert twee types met tags die "left" of "right" aangeven. Waarden worden geschreven als `σᴸ(a)` of `inl(a)` voor links-getagde waarden en `σᴿ(b)` of `inr(b)` voor rechts-getagde waarden. De tags blijven onderscheiden, zelfs wanneer identieke types worden gecombineerd.

#### Booleaans type

Het type `𝟙 + 𝟙`, aangeduid als `𝟚` of `TWO`, is een één-bit-type met twee waarden. Standaard staat `σᴸ⟨⟩` voor false/nul, terwijl `σᴿ⟨⟩` voor true/één staat.

### Producttype

Producttypes `A × B` bevatten waardeparen geschreven als `⟨a, b⟩` of `(a, b)`. Het type `𝟚 × 𝟚` heeft vier waarden, die verschillen van de vier waarden in `𝟚 + 𝟚`.

### Kernexpressies van Simplicity

Operaties worden aangeduid als `f : A ⊢ B`, wat inputtype `A` en outputtype `B` betekent. Simplicity is "eersteorde" — het heeft geen functietypes.

### Twee basisoperaties

De kerntaal biedt twee basisoperaties:

**Identiteit (`iden`).** De identiteitsoperatie geeft zijn input ongewijzigd door:

```
iden : A ⊢ A
⟦iden⟧(a) = a
```

**Unit (`unit`).** De unit-operatie negeert zijn input en geeft de lege tuple terug:

```
unit : A ⊢ 𝟙
⟦unit⟧(a) = ⟨⟩
```

Deze vormen families met één operatie per type.

### Drie compositiecombinators

Sequentiële compositie gebruikt `comp f g` (geschreven als `f ⨾ g` of `f >>> g`):

```
If f : A ⊢ B and g : B ⊢ C, then
comp f g : A ⊢ C
⟦f ⨾ g⟧(a) = ⟦g⟧(⟦f⟧(a))
```

Parallelle compositie gebruikt `pair f g` (geschreven als `f ▵ g` of `f &&& g`):

```
If f : A ⊢ B and g : A ⊢ C, then
pair f g : A ⊢ B × C
⟦f ▵ g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩
```

Conditionele compositie gebruikt `case f g : (A + B) × C ⊢ D`, waarbij de takken toegang krijgen tot een gedeelde omgeving `C`:

```
If f : A × C ⊢ D and g : B × C ⊢ D, then
case f g : (A + B) × C ⊢ D
⟦case f g⟧⟨σᴸ(a), c⟩ = ⟦f⟧⟨a, c⟩
⟦case f g⟧⟨σᴿ(b), c⟩ = ⟦g⟧⟨b, c⟩
```

Waarom heeft conditionele compositie deze vorm — een som gekoppeld aan een gedeelde omgeving `C` — in plaats van een eenvoudigere `copair f g : A + B ⊢ C` die alleen een tak kiest? Omdat een kale `copair` geen **distributie** kan uitdrukken: de functie `dist : (A + B) × C ⊢ A × C + B × C` die een gedeelde input doorduwt naar welke tak dan ook wordt genomen. Door de omgeving `C` rechtstreeks in `case` in te bouwen, verkrijgt Simplicity conditionele compositie *én* distributie uit één enkele combinator — een van de belangrijkste ontwerpbeslissingen die de kerntaal beperkt houdt tot negen combinators.

### Vier extra combinators

Productconsumptie gebruikt `take` en `drop`:

**take** extraheert het linkerelement:

```
If f : A ⊢ C, then
take f : A × B ⊢ C
⟦take f⟧⟨a, b⟩ = ⟦f⟧(a)
```

**drop** extraheert het rechterelement:

```
If f : B ⊢ C, then
drop f : A × B ⊢ C
⟦drop f⟧⟨a, b⟩ = ⟦f⟧(b)
```

Somproductie gebruikt `injl` en `injr`:

**injl** wikkelt in met een linker-tag:

```
If f : A ⊢ B, then
injl f : A ⊢ B + C
⟦injl f⟧(a) = σᴸ(⟦f⟧(a))
```

**injr** wikkelt in met een rechter-tag:

```
If f : A ⊢ C, then
injr f : A ⊢ B + C
⟦injr f⟧(a) = σᴿ(⟦f⟧(a))
```

### De negen kerncombinators

In totaal heeft Simplicity precies negen kerncombinators:

| Combinator | Purpose |
|---|---|
| `iden` | Geeft input door |
| `unit` | Negeert input |
| `comp` | Sequentiële compositie |
| `pair` | Parallelle compositie |
| `case` | Conditionele compositie |
| `take` | Extraheert links uit product |
| `drop` | Extraheert rechts uit product |
| `injl` | Injecteert links in som |
| `injr` | Injecteert rechts in som |

### Simplicity en het sequentenkalkul

Het ontwerp van Simplicity is afgeleid van het conjunctief-disjunctieve fragment van Gentzens sequentenkalkul. Preciezer gezegd is het een variant van de *functionele interpretatie* van het sequentenkalkul, wat zelf analoog is aan de Curry-Howard-correspondentie tussen natuurlijke deductie en de lambdacalculus. De combinatorregels vertonen "kleinere types in premissen dan in conclusies", waardoor de Bit Machine — Simplicity's abstracte stackmachine-interpreter — dataduplicatie tijdens uitvoering kan minimaliseren.

### Waarden zijn geen expressies

Simplicity-expressies duiden operaties aan, geen waarden. De notatie `scribe b : A ⊢ B` staat voor een unieke expressie die altijd de waarde `b` teruggeeft, en dient als notatiegemak in plaats van als combinator. Dit weerspiegelt Bitcoin Script, waar operaties zoals `OP_1` waarden pushen in plaats van ze direct uit te drukken.

### De volledigheidsstelling van Simplicity

Met alle negen combinators in handen, hoe weten we dat we niets missen — dat deze negen echt genoeg zijn? De volledigheidsstelling van Simplicity beantwoordt dit: voor elke functie tussen (eindige) Simplicity-types bestaat er een Simplicity-expressie die deze aanduidt. Het bewijs is constructief — het laat zien hoe je de expressie opbouwt:

1. **Ontleed de input**: Met geneste `case`-expressies wordt elke input van elk type volledig ontleed in zijn samenstellende bits
2. **Bouw een opzoektabel**: Gebruik voor elke mogelijke input `scribe` om de bijbehorende output te produceren
3. **Stel samen**: De geneste cases en scribes vormen samen een gigantische opzoektabel die de functie implementeert

Deze stelling is formeel geverifieerd in de Rocq-bewijsassistent (voorheen Coq). Het bewijs maakt deel uit van de officiële Simplicity-repository en is machinaal gecontroleerd op correctheid.

Hoewel de volledigheidsstelling garandeert dat Simplicity's negen combinators elke functie tussen (eindige) Simplicity-types kunnen uitdrukken, zijn de resulterende expressies uit de opzoektabel-constructie onpraktisch groot. Een functie op 256-bit inputs zou een opzoektabel met 2²⁵⁶ items vereisen. Daarom richten de volgende hoofdstukken zich op het bouwen van efficiënte expressies die de structuur van berekeningen benutten, in plaats van alles brute-force via opzoektabellen af te handelen.

### Conclusie

De kerntaal van Simplicity omvat een typesysteem en combinators die elke eindige berekening mogelijk maken. Hoewel de volledigheidsstelling expressiviteit garandeert, zijn de resulterende expressies uit de generieke constructie onpraktisch groot. Praktische Simplicity-ontwikkeling draait om het benutten van de computationele structuur voor beknopte expressies. De volgende hoofdstukken verkennen datastructuren, transactie-interacties en aanvullende combinators.

# Van datatypes naar programma's

<partId>08528a6f-d310-4675-b8cd-4e9b93b3c009</partId>

## Datatypes bouwen

<chapterId>9981ae62-ae50-4770-adf2-b253d1e08de3</chapterId>

In de vorige hoofdstukken hebben we laten zien dat Simplicity's kernset van combinators voldoende is om elke eindige zuivere berekening te implementeren. Dit hoofdstuk laat zien hoe je praktische datastructuren en berekeningen bouwt vanuit deze primitieven — op dezelfde manier waarop computers worden gebouwd uit logische poorten.

### Booleaanse logica

Het booleaanse type, aangeduid als `𝟚`, is gelijk aan `𝟙 + 𝟙` en heeft twee waarden: `σᴸ⟨⟩` (false) en `σᴿ⟨⟩` (true). Met de kerncombinators kunnen booleaanse logische operatoren worden geconstrueerd.

#### And-operatie

De logische `and : 𝟚 × 𝟚 ⊢ 𝟚`-operatie neemt twee bits en geeft één bit terug. De implementatie vertakt op het eerste bit: als het false is, wordt false teruggegeven; anders wordt het tweede bit teruggegeven.

```
and ≔ case (injl unit) (drop iden) : 𝟚 × 𝟚 ⊢ 𝟚
```

Testen met `⟨false, false⟩`:

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

Testen met `⟨true, true⟩`:

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

#### Overige logische operaties

De `not`-operatie vereist een hulpcombinator:

```
                   f : A ⊢ C    g : B ⊢ C
--------------------------------------------------------------
copair f g ≔ iden ▵ unit ⨾ case (take f) (take g) : A + B ⊢ C
```

De initiële `iden ▵ unit : A ⊢ A × 𝟙` voegt een lege "omgeving" toe aan de input, waardoor de `case`-combinator kan worden toegepast. Het gebruik van `take` in beide takken laat deze lege omgeving vallen om `f` of `g` uit te voeren.

Overige booleaanse logische operaties:

- `or ≔ case (drop iden) (injr unit) : 𝟚 × 𝟚 ⊢ 𝟚`
- `not ≔ copair (injr unit) (injl unit) : 𝟚 ⊢ 𝟚`
- `xor ≔ case (drop iden) (drop not) : 𝟚 × 𝟚 ⊢ 𝟚`

### Bitoptellers

Een "half-adder" neemt twee bits en telt ze op, wat een tweebits-output oplevert: een carry-bit en een sum-bit.

```
half-adder ≔ and ▵ xor : 𝟚 × 𝟚 ⊢ 𝟚 × 𝟚
```

Een "full-adder" telt drie bits op, wat een tweebits-output oplevert. De input gebruikt de geneste tuple `(𝟚 × 𝟚) × 𝟚`.

Voor geneste tuples wordt compacte notatie gebruikt:

- `O f` staat voor `take f`
- `I f` staat voor `drop f`
- `H` staat voor `iden`

Bijvoorbeeld, `I O H` betekent `drop (take iden) : A × (B × C) ⊢ B`, wat de middelste waarde extraheert. De notatie doet denken aan binaire cijfers: als je geneste tuples ziet als binaire bomen, dan staat de notatie voor omgekeerde binaire cijfers van boomposities. Deze expressies vormen De Bruijn-indices voor Simplicity.

**Opmerking:** De `I`-, `O`- en `H`-notatie is alleen van toepassing op subexpressies die uitsluitend bestaan uit `take`, `drop` en `iden`.

De full-adder combineert twee half-adders en neemt de logische `or` van de carry-bits:

```
full-adder ≔ take half-adder ▵ I H
           ⨾ O O H ▵ (O I H ▵ I H ⨾ half-adder)
           ⨾ (O H ▵ I O H ⨾ or) ▵ I I H
           : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × 𝟚
```

In de eerste regel voert `take half-adder ▵ I H : (𝟚 × 𝟚) × 𝟚 ⊢ (𝟚 × 𝟚) × 𝟚` de half-adder uit op de eerste twee bits, waarbij het laatste bit wordt bewaard.

In de tweede regel bewaart `O O H ▵ (O I H ▵ I H ⨾ half-adder) : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × (𝟚 × 𝟚)` het eerste bit (de carry-out van de eerste half-adder) en voert het de half-adder uit op de laatste twee bits.

In de laatste regel neemt `(O H ▵ I O H ⨾ or) ▵ I I H: 𝟚 × (𝟚 × 𝟚) ⊢ 𝟚 × 𝟚` de logische OR van de eerste twee bits (carry-outs van beide half-adders) en geeft het het sum-out-bit van de tweede half-adder terug.

Dit illustreert Simplicity-programmeren: het gebruik van `I`-, `O`- en `H`-notatie om databits te refereren, waarmee geschikte "omgevingen" worden gevormd voor het aanroepen van andere functies via sequentiële compositie.

Gebruikers definiëren geen low-level operaties rechtstreeks. Verderop in deze reeks bespreken we standaardbibliotheek-jets die veelvoorkomende functies implementeren. Van eindgebruikers wordt niet verwacht dat ze rechtstreeks in Simplicity programmeren, net als bij Bitcoin Script. In plaats daarvan genereren high-level talen zoals SimplicityHL Simplicity-code, waarbij ze subexpressie-"omgevingen" beheren en benoemde variabelen vertalen naar de juiste `take`- en `drop`-reeksen.

### Vectoren

Vectoren met vaste lengte worden gedefinieerd door herhaalde producten van type `A` te vormen:

- `A² ≔ A × A`
- `A⁴ ≔ A² × A²`
- `A⁸ ≔ A⁴ × A⁴`
- `…`

Deze kunnen ook worden geschreven als `A^2`, `A^4`, `A^8`, enz.

Vectoren zijn alleen gedefinieerd voor lengtes die machten van twee zijn. Andere lengtes vereisen het kiezen van haakjesconventies.

Gegeven de expressie `f : A ⊢ B`, "mapt" herhaald paren deze over vectoren met vaste lengte:

- `f² ≔ f ▵ f : A² ⊢ B²`
- `f⁴ ≔ f² ▵ f² : A⁴ ⊢ B⁴`
- `f⁸ ≔ f⁴ ▵ f⁴ : A⁸ ⊢ B⁸`

Gegeven de functie `f : A × B ⊢ B`, "folden" of itereren over vectoren met vaste lengte:

- `fold-right-2 f ≔ O O H ▵ (O I H ▵ I H ⨾ f) ⨾ f : A² × B ⊢ B`
- `fold-right-4 f ≔ fold-right-2 (fold-right-2 f) : A⁴ × B ⊢ B`
- `fold-right-8 f ≔ fold-right-2 (fold-right-4 f) : A⁸ × B ⊢ B`

Er bestaan veel varianten. Gegeven `f : A × B ⊢ C`, "zip" je over gepaarde vectoren met `zip-n f : (Aⁿ × Bⁿ) ⊢ Cⁿ`. Gegeven `f : (A × B) × C ⊢ C`, fold je over gepaarde vectoren met `bifold-right-n f : (Aⁿ × Bⁿ) ⊢ C`. Het combineren van `map` en `fold-right` creëert accumulerende combinators: `f : A × C ⊢ C × B` levert `map-accum-right-n f : Aⁿ × C ⊢ C × Bⁿ` op. Er zijn nog veel meer varianten mogelijk.

#### Multi-bit-woorden

Een bitvector levert multi-bit-gehele getallen op. Zo is `𝟚³²` een 32-bit-woordtype. `𝟚²⁵⁶` is een 256-bit-woordtype, geschikt voor hashes en cryptografische operaties.

Met de full-adder definieert een variant van vectoroperaties een "ripple carry adder" over multi-bit-woorden:

```
full-adder-n ≔ zip-accum-right-n full-adder : (𝟚ⁿ × 𝟚ⁿ) × 𝟚 ⊢ 𝟚 × 𝟚ⁿ
```

`full-adder-n` neemt twee n-bit binaire getallen en een één-bit carry-input, en geeft een één-bit carry-out-vlag en een n-bit som terug.

#### SHA-256

Door rekenkundige operaties op multi-bit-woorden recursief te definiëren — aftrekken, vermenigvuldigen, delen — en bitgewijze logische operaties zoals logische AND, OR, XOR, en deze herhaaldelijk te combineren, kan zelfs de blokcompressiefunctie van SHA-256 worden gebouwd:

```
sha256-hash-block ≔ … : 𝟚²⁵⁶ × 𝟚⁵¹² ⊢ 𝟚²⁵⁶
```

De SHA-256-compressie is formeel gedefinieerd met Simplicity binnen de Rocq-bewijsassistent (voorheen Coq), met een formeel bewijs dat de implementatie van `sha256-hash-block` correct is.

De compressie draait te traag als rauwe Simplicity. Jets voeren veelvoorkomende functies zoals SHA-256-compressie native uit. Zuivere Simplicity-implementaties dienen als formele specificaties voor jets.

### Option-types

Option-types ontstaan door een som te nemen met het unit-type:

```
Option A ≔ 𝟙 + A
```

Het type `Option A` kan ook worden geschreven als `A?` of `𝕊 A` (waarbij `𝕊` "successor" betekent). Functies mappen over option-types:

```
                 f : A ⊢ B
------------------------------------------
f? ≔ copair (injl unit) (injr f) : A? ⊢ B?
```

Monadische combinators zoals bind kunnen worden gedefinieerd:

```
              f : A ⊢ B?
---------------------------------------
bind f ≔ copair (injl unit) f : A? ⊢ B?
```

### Buffers met variabele lengte

"Buffers" zijn types voor gedeeltelijk gevulde vectoren:

- `Aᑉ² ≔ A?`
- `Aᑉ⁴ ≔ A²? × Aᑉ²`
- `Aᑉ⁸ ≔ A⁴? × Aᑉ⁴`
- `…`

Het type `Xᑉ⁸` breidt uit naar `(1 + X⁴) × ((1 + X²) × (1 + X))`. Als je dit als een polynoom behandelt en uitwerkt, krijg je `1 + X + X² + X³ + X⁴ + X⁵ + X⁶ + X⁷`. Als type geïnterpreteerd, staat dit voor de som van alle mogelijke tuples van X tot en met 7, inclusief de lege tuple. Dit is precies het type lijsten met een lengte strikt kleiner dan 8.

Net als bij vectoren kunnen map- en fold-operaties worden gedefinieerd over buffers. Stackoperaties omvatten `push-<n : Aᑉⁿ × A ⊢ Aⁿ + Aᑉⁿ` en `pop-<n : Aᑉⁿ ⊢ (Aᑉⁿ × A)?`. `push-<n` voegt een item toe aan de buffer en geeft een volledige vector terug als er overflow optreedt. `pop-<n` verwijdert een item en geeft de kleinere buffer en het verwijderde item terug, of optioneel niets als de oorspronkelijke buffer leeg was.

De `push-<n`-definitie, recursief:

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

Rauwe Simplicity wordt lastig te volgen voorbij bepaalde complexiteitsniveaus. Eindgebruikers gebruiken high-level talen zoals SimplicityHL die deze idiomatische expressies genereren.

### Conclusie

Dit hoofdstuk liet zien hoe je logische operaties bouwt vanuit bits. Daaruit ontstond bit-niveau rekenkunde, wat redeneren over uitvoering mogelijk maakt. Vectortypes werden ontwikkeld, wat iteratie over multi-bit-woorden voor de definitie van rekenkunde demonstreerde. Verder kunnen cryptografische operaties zoals SHA-256 en Schnorr-handtekeningvalidatie uitsluitend met Simplicity-combinators worden gedefinieerd — en zijn ze dat in werkelijkheid ook, allemaal gedefinieerd met Simplicity.

Dit hoofdstuk is geen uitputtende gids voor alle mogelijke datatypes en operaties die in Simplicity gebouwd kunnen worden, maar illustreert hoe je praktische functionaliteit bereikt binnen de beperkingen van Simplicity. Ondanks eindig begrensde types kunnen bruikbare vectoren, buffertypes en operaties die over deze structuren itereren, worden gedefinieerd.

De daadwerkelijke specificaties van standaardbibliotheekoperaties wijken enigszins af van de definities hier. Zo gebruikt de full-adder een 3-weg-XOR en een "meerderheid"-logicafunctie in plaats van twee half-adders.

In de praktijk gebruiken Simplicity-programma's jets voor rekenkundige en cryptografische operaties. Jets vervangen echter alleen expressies. Combinators die itereren over buffers en vectoren kunnen niet door jets worden vervangen en komen dus voor in daadwerkelijke Simplicity-programma's. Eindgebruikers gebruiken echter, in plaats van deze rechtstreeks te schrijven, high-level talen zoals SimplicityHL die dergelijke expressies genereren.

Recursief gedefinieerde combinators lijken exponentieel te groeien in expressiegrootte. Dit is niet problematisch. Tijdens serialisatie worden expressies gecodeerd als DAG's (directed acyclic graphs, gerichte acyclische grafen) in plaats van als bomen. De daadwerkelijke representatie groeit slechts lineair.

Tot nu toe zijn alleen zuivere berekeningen beschouwd. Interactie met transactiedata voor taken zoals het ondertekenen van transacties vereist een manier waarop programma's kunnen falen als handtekeningen ongeldig zijn. Het volgende hoofdstuk behandelt neveneffecten in Simplicity.

## Twee neveneffecten

<chapterId>9eafe498-0765-419a-a69d-a74a9cdf3713</chapterId>

In de vorige hoofdstukken hebben we laten zien hoe je een aantal datastructuren en berekeningen bouwt met Simplicity's kernset van combinators. Zoals we opmerkten, zijn de kerncombinators voldoende om elke eindige zuivere berekening te implementeren. Dit roept de vraag op: wat kan er nog meer bereikt worden? We kunnen extra neveneffecten aan onze expressies toevoegen.

Er zijn verschillende soorten mogelijke neveneffecten voor expressies: statusupdates, schrijven naar een log, het gooien van een exception, lezen uit een omgeving, het aanroepen van een continuation, enz. De neveneffecten die in Simplicity beschikbaar zijn, hangen af van de toepassing.

Voor Bitcoin- en Liquid-toepassingen hebben we momenteel twee neveneffecten: het Failure-effect, een exception-effect waarbij de exception van het type `𝟙` is, en het Reader-effect, dat toegang geeft tot data uit de transactieomgeving. Onze kerncombinators zijn "puur"; ze hebben geen neveneffecten. Jets kunnen echter nieuwe primitieven introduceren die wél neveneffecten hebben.

### Jets met effecten

We bespreken jets later in deze cursus uitgebreider, maar hier introduceren we een paar voorbeeldjets om hun neveneffecten te illustreren.

#### Bip0340-verify

`bip0340-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚⁵¹² ⊢ 𝟙` is een jet voor een expressie die een x-only pubkey, een 256-bit bericht en een Schnorr-handtekening neemt, en niets teruggeeft! Volgens zijn type zou het zich hetzelfde moeten gedragen als een `unit`. Het verschil zit in het neveneffect van de jet: als de handtekeningvalidatie mislukt, wordt de hele berekening afgebroken door een exception te gooien (van het unit-type). Dit is het Failure-effect.

#### Verify

`verify : 𝟚 ⊢ 𝟙` is een minimale jet om het Failure-effect uit te drukken. Als de input van `verify` `false` is, wordt de hele berekening afgebroken door een exception te gooien. Als de input `true` is, wordt niets teruggegeven, maar kan de berekening doorgaan.

#### Transactiehashes

`sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` lijkt een constante functie te zijn, aangezien er maar één mogelijke inputwaarde is: de lege tuple. Deze jet leest echter uit de transactieomgeving en produceert een hash van transactiedata die analoog is aan de `SIGHASH_ALL`-berichtdigest die gebruikt wordt bij handtekeningverificatie in Bitcoin Script. Dit is een voorbeeld van het Reader-effect: de teruggegeven waarde hangt af van de transactieomgeving waarin de jet wordt uitgevoerd. Er zijn verschillende andere hashing-jets die diverse subsets van de transactieomgevingsdata hashen om aangepaste berichtdigests voor handtekeningen te helpen opbouwen.

#### Introspectiejets

`input-sequence : 𝟚³² ⊢ 𝟚³²?` is een functie die een input-index neemt en het sequence-nummer van de transactie voor die input teruggeeft, of optioneel niets als de index buiten bereik is. Ook hier is de outputwaarde geen zuivere functie van de input-index, maar gebruikt de operatie het Reader-effect om toegang te krijgen tot de transactieomgeving om de outputwaarde te bepalen. Er zijn verschillende andere introspectiejets die diverse fragmenten van de transactieomgevingsdata teruggeven.

### Effecten classificeren

Niet alle neveneffecten zijn gelijk. Sommige neveneffecten gedragen zich netter dan andere. We kunnen effecten classificeren op basis van hoe ontvankelijk ze zijn voor programmatransformaties.

#### Commutatieve effecten

Een commutatief effect is een effect waarbij je, als je de outputs van twee expressies verwisselt, ook veilig de expressies zelf kunt verwisselen zonder het effect van de expressie te veranderen. Beschouw `swap = I H ▵ O H : A × B ⊢ B × A`. Als `f ▵ g ⨾ swap = g ▵ f` geldt voor elke expressie `f` en `g` met neveneffecten, dan zijn de effecten commutatief.

Het lezen van transactiedata uit de omgeving is een commutatief effect, omdat het resultaat van het lezen uit de omgeving hetzelfde is, ongeacht in welke volgorde we het lezen uitvoeren.

Over het algemeen is het gooien van een exception geen commutatief effect. Als `f` een exception `e₁` gooit en `g` een andere exception `e₂`, dan hangt het van de uitvoeringsvolgorde af welke exception wordt gegooid uit het paar `f` en `g`.

In het speciale geval van het Failure-effect, waarbij alleen een exception van het unit-type kan worden gegooid, is het effect echter wel commutatief. Ongeacht of `f` of `g` een exception gooit, de resulterende exception zal hetzelfde zijn, omdat er slechts één mogelijke exception-waarde is.

#### Idempotente effecten

Een idempotent effect is een effect waarbij je, als je de output van een expressie dupliceert, ook veilig de expressie zelf kunt dupliceren zonder het effect van de expressie te veranderen. Beschouw `dup = iden ▵ iden : A ⊢ A × A`. Als `f ⨾ dup = dup ⨾ f ▵ f` geldt voor elke `f` met neveneffecten, dan zijn de effecten idempotent.

Het lezen van transactiedata uit de omgeving is een idempotent effect. Het gooien van een exception is ook een idempotent effect. Ook al wordt slechts één van de twee gedupliceerde expressies uitgevoerd, elke exception die door `dup ⨾ f ▵ f` wordt gegooid, zal dezelfde zijn als de exception die door `f ⨾ dup` wordt gegooid.

Schrijven naar een log is echter mogelijk niet idempotent, omdat het dupliceren van het effect ervoor zou zorgen dat het logbericht twee keer verschijnt. Als het log echter bestaat uit een _verzameling (set)_ berichten in plaats van een _lijst_ berichten, dan zou het effect idempotent zijn (en commutatief), omdat het invoegen in een set zelf een idempotente operatie is.

#### Unitaire effecten

Een unitair effect is een effect waarbij je, als je de output van een expressie negeert, ook veilig de expressie zelf kunt weglaten zonder de effecten van de expressie te veranderen. Als het altijd geldt dat `f ⨾ unit = unit` voor elke `f` met neveneffecten, dan zijn je effecten unitair.

Het lezen van data uit de omgeving is een van de weinige soorten unitaire effecten. Als het resultaat van het lezen van transactiedata uit de omgeving wordt genegeerd, kan de hele expressie die de lezing uitvoert worden weggelaten.

Het Failure-effect is niet unitair. Als `f` een exception gooit, dan doet `f ⨾ unit` dat ook; de uitvoering zal de `unit`-combinator niet eens bereiken voordat de berekening wordt afgebroken. Aan de andere kant zou `unit` uiteraard geen enkele exception gooien, dus de effecten van `f ⨾ unit` en `unit` zouden verschillen.

Samenvattend, hier is hoe de hierboven besproken effecten scoren op deze drie eigenschappen:

| Effect | Commutative | Idempotent | Unitary |
| --- | :---: | :---: | :---: |
| Reader (transactieomgeving) | ✓ | ✓ | ✓ |
| Failure (unit-getypeerde exception) | ✓ | ✓ | ✗ |
| Writer (log als set) | ✓ | ✓ | ✗ |
| Algemene exceptions (willekeurig type) | ✗ | ✓ | ✗ |

### Effecten toegestaan in Simplicity

Hoe beter een type effect zich gedraagt, hoe meer ruimte een Simplicity-optimizer heeft om programma's die deze effecten gebruiken te transformeren. Idealiter zouden we alleen effecten toestaan die alle drie eigenschappen hebben: commutatief, idempotent en unitair. Dit zou een optimizer in staat stellen elke gewenste programmatransformatie uit te voeren. Lezen uit een omgeving is echter het enige effect dat aan alle drie de eigenschappen voldoet.

In plaats daarvan eisen we dat Simplicity-effecten commutatief en idempotent zijn. Beide effecten die we in Simplicity gebruiken, het Failure-effect en het Reader-effect, zijn commutatief en idempotent. Dit maakt een grote klasse aan optimalisaties op Simplicity-code mogelijk.

De "discard"-transformatie die hierboven werd beschreven, waarbij `f ⨾ unit` wordt vervangen door `unit`, of een vergelijkbare transformatie, is echter niet toegestaan als `f` mogelijk een Failure-effect produceert. Stel je voor dat `f` een `bip0340-verify`-assertie bevat: het zou rampzalig zijn om die controle te proberen te optimaliseren.

### Waarom neveneffecten überhaupt toestaan?

Waarom staat Simplicity überhaupt neveneffecten toe? Zou het niet beter zijn als elk programma de volledige transactie als input nam en een booleaanse output teruggaf die bepaalt of een transactie geldig is of niet?

#### Batch-verificatie

Een reden dat we het Failure-effect hebben, is om [batch-verificatie](https://github.com/bitcoin/bips/blob/c9a6ca6297eb8de850f6b64dafb8e60ee9b64d66/bip-0340.mediawiki#batch-verification) van Schnorr-handtekeningen te ondersteunen. Bij batch-verificatie worden veel individuele Schnorr-handtekeningcontroles zo gebundeld dat als één enkele handtekeningcontrole faalt, de hele batch faalt.

Deze batchingprocedure verbetert de efficiëntie ten opzichte van het individueel verifiëren van elke handtekening. Het nadeel is dat als de batch-verificatie faalt, we niet te weten komen welke specifieke handtekeningcontrole(s) faalden.

Door het failure-neveneffect te gebruiken, zorgt `bip0340-verify` ervoor dat als een handtekeningcontrole faalt, de hele transactie faalt. Als `bip0340-verify` in plaats daarvan `𝟚`, een booleaans type, zou teruggeven voor succes of falen, dan zou een mislukte handtekeningcontrole nog steeds kunnen leiden tot een tak waarin het script slaagt. In dat geval zouden we moeten weten of die specifieke handtekening geldig is of niet, en zouden we dus geen gebruik kunnen maken van batch-verificatie.

#### Vooraf berekende transactiedata

Een probleem in vroeg Bitcoin Script was dat de hashingfunctie die werd gebruikt om berichtdigests voor handtekeningen te maken, lineair was in de grootte van de transactie. Doorgaans maakt elke input minstens één berichtdigest voor handtekeningverificatie, dus in totaal was de hoeveelheid hashing kwadratisch in de transactiegrootte.

Dit probleem werd opgelost in Segwit en latere iteraties van Bitcoin Script door de berichtdigests zo te herdefiniëren dat ze in constante tijd per handtekeningcontrole konden worden berekend. Dit steunt op `PrecomputedTransactionData`, die eenmalig hashes van transactiedata vooraf berekent en vervolgens wordt gedeeld door de sighash-berekeningen van elke input. De transactiehashing-jets van Simplicity steunen op dezelfde soort vooraf berekende transactiedata om ervoor te zorgen dat de jets in constante tijd draaien.

Stel dat `sig-all-hash` het Reader-effect niet zou gebruiken. Stel dat we op de een of andere manier een Simplicity-type voor de transactieomgeving zouden bouwen. Laten we het `TxEnv` noemen, zodat `sig-all-hash : TxEnv ⊢ 𝟚²⁵⁶` het type van de jet zou zijn. Zo'n definitie zou vereisen dat de `sig-all-hash`-jet de hash van elke willekeurige transactie kan berekenen, niet alleen van de transactie waarbij hij betrokken is. Simplicity-programma's zouden de gegeven `TxEnv` kunnen kopiëren en een aangepaste kopie ervan doorgeven aan `sig-all-hash`. In dat geval zou `sig-all-hash` niet kunnen steunen op `PrecomputedTransactionData`, en zouden we weer terug zijn bij een lineaire tijd ten opzichte van welke transactiedata dan ook die aan deze versie van `sig-all-hash` werd doorgegeven.

Omdat `sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` het Reader-effect gebruikt om toegang te krijgen tot de transactiedata, krijgt hij _alleen_ toegang tot een vaste transactieomgeving. Daarom kan de implementatie van de jet veilig `PrecomputedTransactionData` gebruiken en in constante tijd draaien.

### Cross-input handtekeningaggregatie

Hoewel noch Liquid noch Bitcoin op dit moment [cross-input handtekeningaggregatie](https://hrf.org/latest/cisa-research-paper/) ondersteunen, willen we controleren dat Simplicity hiermee compatibel kan zijn wanneer het zover is.

Hoewel de details nog niet zijn uitgewerkt, stellen we ons voor dat half-aggregatie geïmplementeerd zou worden met een Writer-effect. Dat wil zeggen: een nieuwe jet met een type zoals `half-agg-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚²⁵⁶ ⊢ 𝟙` zou een publieke sleutel, berichtdigest en de `r`-component van een Schnorr-handtekening nemen (een Schnorr-handtekening bestaat uit een `r`-component en een `s`-component) en deze naar een transactielog schrijven voordat de uitvoering wordt voortgezet. Vervolgens zou, elders in de transactie of bij de transactie, een geaggregeerde `s`-component voor alle half-geaggregeerde Schnorr-handtekeningen worden verstrekt. De transactie zou alleen geldig zijn als zo'n geaggregeerde `s`-component wordt verstrekt voor alle gelogde sleutels, berichten en `r`-componenten.

Om aan de eisen van Simplicity te voldoen, moet dit Writer-effect idempotent en commutatief zijn. Dit kan gewaarborgd worden door het writer-log te behandelen als een set van tuples van sleutel, bericht en `r`-component. Dit werkt omdat set-operaties idempotent en commutatief zijn. Het behandelen van het log als een set van waarden zou compatibel zijn met het half-aggregatie-verificatiealgoritme.

### Conclusie

In dit hoofdstuk hebben we gekeken naar het toevoegen van neveneffecten aan de berekeningen die Simplicity kan uitvoeren. We classificeerden verschillende soorten effecten op basis van hoe goed ze zich gedragen ten opzichte van verschillende soorten programmatransformaties. We besloten om Simplicity's effecten te beperken tot effecten die commutatief en idempotent zijn.

De twee effecten die we gebruiken voor Bitcoin- en Liquid-toepassingen zijn het Reader-effect, voor toegang tot de transactieomgeving, en het Failure-effect, voor het afbreken en laten falen van het programma. Sommige jets maken gebruik van primitieve operaties waarbij dit soort neveneffecten kunnen optreden.

Het Failure-effect bepaalt de output van een Simplicity-programma: het programma faalt, waardoor de transactie ongeldig wordt, of het programma slaagt. Het Reader-effect biedt een soort input voor een Simplicity-programma: de omgeving die de transactiedata bevat. Maar we moeten ook andere inputs, zoals digitale handtekeningen, aan Simplicity-programma's kunnen geven.

In het volgende hoofdstuk kijken we naar wat Simplicity-programma's zijn, hoe ze worden omgezet in adressen, en hoe we andere inputs, zoals handtekeningen, aan Simplicity-programma's toevoegen.

## Programma's en adressen

<chapterId>961652e3-8f7d-4c2a-8b55-9a990b91a0dd</chapterId>

In het vorige hoofdstuk hebben we twee neveneffecten in Simplicity beschreven: het Failure-effect, dat het slagen of falen van een programma bepaalt, en het Reader-effect, dat toegang geeft tot de transactieomgeving. Nu richten we ons op de praktische vraag: wat is een Simplicity-programma precies, en hoe wordt het een adres op de blockchain?

### Simplicity-programma's

Een Simplicity-programma wordt gedefinieerd als een Simplicity-expressie van het type `𝟙 ⊢ 𝟙`. Deze typesignatuur betekent dat het programma geen betekenisvolle input neemt (alleen de unit-waarde) en geen betekenisvolle output produceert (alleen de unit-waarde). Het Reader-effect vangt de input van de transactieomgeving op, terwijl het Failure-effect succes of falen aangeeft. Deze effecten handelen input/output af, niet de Simplicity-types zelf.

### Commitment Merkle Root

In plaats van complete programma's on-chain op te slaan, gebruikt Bitcoin commitments — een praktijk die voortkomt uit Pay-to-Script-Hash (P2SH). Simplicity gebruikt een Commitment Merkle Root (CMR).

Elke combinator krijgt een SHA-256-tag afgeleid van het patroon: `Simplicity␟Commitment␟[identifier]`, waarbij `␟` staat voor ASCII-code 31 (de unit separator).

Elke tag is de SHA-256-hash van de bijbehorende pre-image-string hieronder:

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

Een Simplicity-expressie wordt vervolgens recursief gehasht tot een 256-bit CMR door voor elke combinator, samen met de CMR's van zijn argumenten, een getagde SHA-256-midstate te berekenen (schrijf `#ᶜ(e)` voor de CMR van expressie `e`, en `∥` voor byte-aaneenschakeling):

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

Binaire combinators (`comp`, `pair`, `case`) voegen de CMR's van beide kinderen samen; unaire combinators (`take`, `drop`, `injl`, `injr`) voegen de CMR van hun ene kind samen na 32 bytes opvulling met `0x00`; en de nullaire bladeren (`iden`, `unit`) hashen alleen hun tag. Twee conventies houden dit goedkoop om te berekenen: SHA-256-midstates worden gebruikt zodat **elke expressie hoogstens één aanroep van de SHA-256-compressiefunctie vereist** (ervan uitgaande dat de midstate tot aan de constante tags vooraf is berekend), en de eenargumentconstructors prefixen hun argument met 32 bytes van `0x00`-opvulling, wat wat extra voorberekening mogelijk maakt voor implementaties die dat willen.

Voor de `unit`-combinator — een nullaire constructor zonder argument-subexpressies — specialiseert deze regel zich tot `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)`, waarbij `tag_unit = SHA-256(Simplicity␟Commitment␟unit)` (de tag wordt twee keer ingevoerd). De resulterende CMR voor het triviale `unit`-programma is:

```
0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

Cruciaal is dat de CMR niet vastlegt aan de types van Simplicity-expressies, maar in plaats daarvan steunt op typeinferentie tijdens het inlossen.

### Adressen

Adressen maken gebruik van het Taproot-mechanisme van BIP-0341, waarbij CMR's worden vastgelegd onder TapLeaf-versie `0xbe`. Het proces omvat:

1. Het berekenen van een TapLeaf-getagde hash die de versiebyte, CMR-lengte en de CMR zelf combineert
2. Het tweaken van een interne publieke sleutel (met een NUMS-punt wanneer geen key-spend-pad gewenst is)
3. Omzetten naar bech32m-formaat
4. Het toevoegen van de juiste checksums

Wanneer geen key-spend-pad gewenst is, wordt de interne publieke sleutel ingesteld op een **NUMS**-punt ("Nothing-Up-My-Sleeve"): een curvepunt dat opzettelijk zo gekozen is dat niemand de discrete logaritme ervan kent — met andere woorden, een punt zonder bijbehorende privésleutel. Omdat niemand er ooit een handtekening voor kan produceren, is het key-spend-pad aantoonbaar onbruikbaar, en kan de output *alleen* worden besteed via het vastgelegde Simplicity-scriptpad. In een echte toepassing moet dit NUMS-punt worden gerandomiseerd, zoals aanbevolen door BIP-0341, zodat outputs zonder key-spend-pad niet te onderscheiden zijn van gewone Taproot-outputs (een privacyvoordeel).

#### Van Simplicity naar adres

Laten we de volledige afleiding doorlopen voor het eenvoudigst mogelijke programma: `unit : 𝟙 ⊢ 𝟙`, een no-op die altijd slaagt.

**1. Combinator-tag.** Bereken eerst de `unit`-tag:

```
tag_unit = SHA-256(Simplicity␟Commitment␟unit)
         = 0xd723083cff3c75e29f296707ecf2750338f100591c86e0c71717f807ff3cf69d
```

**2. CMR.** Voer de tag twee keer in om de CMR van het programma te verkrijgen:

```
CMR = #ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)
    = 0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

**3. TapLeaf-hash.** Prefix de CMR met Simplicity's TapLeaf-versie `0xbe` en de CMR-lengte `0x20` (32 bytes), en neem vervolgens de getagde Elements-TapLeaf-hash (een getagde hash is `hash_str(x) = SHA-256(SHA-256(str) ∥ SHA-256(str) ∥ x)`):

```
hash_TapLeaf/elements(0xbe ∥ 0x20 ∥ CMR)
  = 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c
```

Met slechts dit ene blad zijn er geen TapBranches, dus deze hash is al de TapTree-root.

**4. TapTweak.** Aangezien we geen key-spend-pad willen, gebruiken we het BIP-0341 NUMS-punt als de interne sleutel en tweaken we deze met de TapTree-root:

```
internal_pk = 0x50929b74c1a04954b78b4b6035e97a5e078a5a0f28ec96d547bfee9ace803ac0
t = hash_TapTweak/elements(internal_pk ∥ 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c)
  = 0xb3bef172389b0937d7e5a8b15cfa41e776777f13f2f659cb06220a6ff0658285
```

**5. Output-sleutel.** Tweak de interne sleutel op de curve, `output_pk = lift_x(internal_pk) ⊕ t·G` (de elliptische-curve-rekenkunde is hier samengevat), wat de x-only outputsleutel `0x2cb0c20acd7340b4d4b65f6a60e2888d0d64e3267261f3b3cf7290e5af3f9e09` oplevert.

**6. Bech32m-adres.** Codeer de x-only outputsleutel, prefix een `p` (het SegWit v1-witness-versieteken), voeg de Liquid-testnet human-readable prefix `tex1` toe, en voeg de Bech32m-checksum toe. Het uiteindelijke adres is:

```
tex1p9jcvyzkdwdqtf49kta4xpc5g35xkfcexwfsl8v70w2gwttelncyshxjk56
```

Dat was heel wat werk — maar het meeste hiervan wordt opgelegd door Taproot zelf, niet door Simplicity.

### Witness-expressies

Een nieuw combinatortype pakt het ontbreken van input voor Simplicity-programma's aan: de witness-expressie. De `witness`-combinator maakt het mogelijk om handtekeningdata en ander witness-materiaal in programma's op te nemen.

```
      w : B
-----------------
witness w : A ⊢ B
```

De semantiek van de witness-expressie is eenvoudig: ze negeert haar input en geeft simpelweg de waarde `w` terug (die van elk Simplicity-type kan zijn), d.w.z. `⟦witness w⟧(a) = w`. Dit voegt **geen nieuwe expressiviteit** toe — volgens de volledigheidsstelling kan Simplicity al elke dergelijke constante functie bouwen (denk terug aan de `scribe`-macro uit de vorige hoofdstukken). Het punt van de `witness`-combinator ligt volledig in zijn **CMR**: de waarde `w` wordt **uitgesloten** van de CMR van de expressie, zodat het adres kan worden berekend voordat `w` bekend is, en `w` wordt pas geleverd op het moment van inlossen.

Deze ontwerpkeuze ondersteunt pruning — niet-uitgevoerde conditionele takken hoeven niet on-chain onthuld te worden, inclusief de bijbehorende witness-expressies. Wanneer een tak wordt weggesnoeid, heeft de verifier alleen de CMR van de weggesnoeide subboom nodig, niet de daadwerkelijke inhoud ervan.

### Witness-waarden

Het lijkt misschien een beperking dat een witness-expressie alleen een *waarde* kan bevatten, en geen algemenere Simplicity-expressie. Maar programma's voor UTXO-gebaseerde blockchains worden slechts één keer uitgevoerd. Er is geen noodzaak om een hele subexpressie door te geven aan een witness-node: de gebruiker kan die subexpressie gewoon zelf uitvoeren, off-chain, en de output ervan overschrijven in de witness-waarde om precies hetzelfde resultaat te verkrijgen.

(Verderop in deze cursus maken we kennis met de `disconnect`-combinator, die zich in grote lijnen gedraagt als een witness-expressie die *wél* een volledige Simplicity-expressie als argument neemt.)

Een alternatief ontwerp zou alle witness-data als argument aan het top-level Simplicity-programma voeden. Witness-expressies genieten de voorkeur om twee redenen. Ten eerste, **pruning**: niet-uitgevoerde takken van `case`-expressies worden nooit on-chain onthuld, en witness-expressies binnen die takken worden samen met die takken weggesnoeid. Ten tweede, **lokaliteit**: witness-expressies laten ons elke witness-waarde precies daar plaatsen waar hij gebruikt wordt, in plaats van hem vanaf de top-level input van het programma naar beneden te moeten doorvoeren.

### Typeinferentie

Aangezien CMR's zich niet vastleggen aan types, wordt het typesysteem tijdens het inlossen gereconstrueerd. Het typeinferentiealgoritme van Simplicity bepaalt de minimale types voor elke subexpressie op basis van de combinatorstructuur. Preciezer gezegd berekent inferentie het *principale* (meest algemene) type van elke subexpressie; eventuele typevariabelen die vrij blijven, worden vervolgens geïnstantieerd naar het unit-type `𝟙`, wat een uniek, minimaal type voor het programma oplevert.

### Conclusie

In dit hoofdstuk hebben we vastgesteld dat Simplicity-programma's expressies zijn van het type `𝟙 ⊢ 𝟙`, uitgelegd hoe Commitment Merkle Roots worden opgebouwd uit getagde SHA-256-hashes van elke combinator, en laten zien hoe CMR's via BIP-0341 Taproot worden omgezet in on-chain adressen. We introduceerden witness-expressies als het mechanisme om handtekeningdata en andere inputs te leveren op het moment van besteding, zonder ons bij het aanmaken van het adres al vast te leggen op hun waarden.

# Laatste onderdeel

<partId>96952535-4aa6-4e78-91e2-d12e9df895d4</partId>

## Beoordelingen & Ratings

<chapterId>fb0b0133-39ea-497b-bd36-198be42c4fab</chapterId>
<isCourseReview>true</isCourseReview>

## Eindexamen

<chapterId>2cc5e818-abcb-4a0a-9991-7a492c572e2d</chapterId>
<isCourseExam>true</isCourseExam>

## Conclusie

<chapterId>8ade24bd-a84f-4d25-8f64-bdfa8b58926c</chapterId>
<isCourseConclusion>true</isCourseConclusion>
