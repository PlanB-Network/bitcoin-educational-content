---
name: Rust leren met Bitcoin
goal: Je Rust ontwikkelingsvaardigheden verbeteren via Bitcoin codering
objectives: 

  - Wennen aan Rust Taal
  - Begrijpen waarom Rust wordt gebruikt voor het ontwikkelen van Bitcoin
  - Verkrijg de basis van Lightning SDK

---

# Een Rust expeditie voor Bitcoin bouwers



In deze hands-on cursus, gefilmd tijdens een seminar georganiseerd door Fulgur' Ventures in oktober 2023, ontwikkel je je Rust vaardigheden door echte Bitcoin gerichte componenten en mini-projecten te bouwen. We behandelen Rust grondbeginselen, waarom Rust wordt gebruikt voor Bitcoin ontwikkeling (geheugenveiligheid, prestaties en veilige gelijktijdigheid), en hoe je aan de slag kunt met de Lightning SDK om betaalfuncties te bouwen.


Door de hoofdstukken heen oefen je kern Rust patronen (eigendom, levens, eigenschappen, async), werk je met Bitcoin primitieven (sleutels, transacties, scripting) en integreer je geleidelijk Lightning concepten (nodes, kanalen, facturen).


Ervaring met Rust of Bitcoin ontwikkeling is strikt genomen niet vereist, hoewel bekendheid met basisprogrammering helpt. De cursus is beginnersvriendelijk maar praktisch genoeg voor engineers die de overstap maken naar Bitcoin.


+++

# Inleiding

<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>


## Cursusoverzicht

<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>


**Inleiding**


Welkom bij deze beginnersvriendelijke programmeercursus over SDK's. In deze training leer je de basis van Rust, daarna richt je je op Rust toegepast op Bitcoin programmeren, en je eindigt met een aantal use-cases met behulp van SDK's.


De video's van de training zullen voorlopig alleen in het Engels beschikbaar zijn en maakten deel uit van een live seminar dat afgelopen oktober in Toscane werd georganiseerd door Fulgure Venture. Deze training richt zich alleen op de eerste week. De tweede helft was gericht op RGB en is te vinden in de RGB cursus.


https://planb.academy/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

Deze training geeft je de mogelijkheid om je programmeervaardigheden op de Lightning Network te ontwikkelen met behulp van Rust en verschillende SDK's. De training is bedoeld voor ontwikkelaars met een degelijke programmeerachtergrond die zich willen verdiepen in Lightning Network-specifieke ontwikkeling. Je leert de basisprincipes van Rust, waarom het geschikt is voor Bitcoin ontwikkeling, en gaat dan verder met hands-on implementatie met behulp van gespecialiseerde SDK's.


**Deel 2: Leren coderen met Rust**

In dit deel ontdek je de Rust grondbeginselen door middel van een serie progressieve hoofdstukken. In zeven gedetailleerde delen leer je Rust code schrijven, de specifieke kenmerken ervan begrijpen en de essentiële functies beheersen. Deze module is essentieel om te begrijpen waarom Rust een geliefde taal is voor Bitcoin ontwikkeling.


**Deel 3: Rust & Bitcoin**

Hier zullen we diepgaand onderzoeken waarom Rust een relevante keuze is voor Bitcoin ontwikkeling. Je leert over het foutenmodel, de UniFFI tool en asynchrone eigenschappen - allemaal belangrijke elementen in het bouwen van robuuste en veilige software.


**Deel 4: LNP/BP-ontwikkeling met SDK's**

Je leert hoe je LN nodes kunt ontwikkelen met behulp van verschillende SDK's zoals Breez SDK en Greenlight voor Lipa. Je zult zien hoe je Lightning Network toepassingen kunt implementeren met behulp van bibliotheken die zijn ontworpen om de ontwikkeling van Bitcoin en Lightning te vereenvoudigen.


Klaar om je Lightning Network vaardigheden uit te breiden met Rust? Laten we gaan!

# Leer coderen met het roestboek

<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>


## Inleiding tot Rust

<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>

<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>


:::video id=12a518cf-64be-43f1-b6d4-f6592a1324ea:::

### Rust installeren en beheren met Rustup


Wanneer u uw reis met Rust begint, is de eerste stap het opzetten van een goede ontwikkelomgeving. De meest aanbevolen aanpak voor het installeren van Rust is via Rustup, een toolchain management systeem dat installatie en updates afhandelt over verschillende projecten en platformen.


Rustup is meer dan alleen een installatieprogramma. Het functioneert als een uitgebreide beheertool voor uw Rust ontwikkelomgeving. Met Rustup kunt u eenvoudig extra compilatiedoelen installeren voor verschillende platformen, zoals ARM64 voor Android ontwikkeling of andere architecturen die u misschien moet ondersteunen. De tool verwerkt ook naadloos Rust updates, wat bijzonder waardevol is aangezien Rust ongeveer elke zes weken een nieuwe stabiele versie uitbrengt. Wanneer je moet updaten naar de laatste versie, dan kan een eenvoudig `rustup update` commando alles automatisch afhandelen.


Bij het installeren van Rustup is het de moeite waard om het beveiligingsmodel te begrijpen. Het installatieproces downloadt en voert een script uit van de officiële Rust website over HTTPS, dat cryptografische beveiliging van de transportlaag biedt. Pakketten die gedownload worden door Rustup en Cargo komen van betrouwbare bronnen (crates.io en de officiële Rust infrastructuur) en profiteren van HTTPS encryptie. Hoewel deze aanpak veilig is voor de meeste ontwikkelscenario's, kunnen sommige organisaties met een strikt beveiligingsbeleid de voorkeur geven aan het installeren van Rust via de pakketbeheerder van hun Linux-distributie, die een extra vertrouwenslaag biedt via de eigen pakketondertekeningsinfrastructuur van de distributie. Voor leer- en algemene ontwikkelingsdoeleinden is Rustup een gevestigde en alom vertrouwde tool in het Rust ecosysteem.


Voor de meeste ontwikkelscenario's kunt u Rustup installeren door het installatiescript op de officiële Rust website uit te voeren. Het installatieprogramma zal je vragen om te kiezen tussen verschillende toolchain opties, waarbij de stabiele toolchain de aanbevolen keuze is voor de meeste gebruikers. De installatie vindt plaats in je thuismap, vereist geen beheerdersrechten en stelt alle benodigde omgevingsvariabelen in voor direct gebruik.


### Rust Toolchains en componenten begrijpen


Het Rust ontwikkel-ecosysteem bestaat uit verschillende belangrijke componenten die samenwerken om een complete programmeeromgeving te bieden. Inzicht in deze componenten helpt u om effectiever door het Rust ontwikkelproces te navigeren en problemen op te lossen wanneer deze zich voordoen.


De Rust compiler, bekend als `rustc`, vormt de kern van de Rust toolchain. Hoewel je `rustc` theoretisch direct zou kunnen gebruiken om Rust programma's te compileren, vertrouwt het meeste ontwikkelwerk op Cargo, Rust's pakketbeheerder en bouwsysteem. Cargo functioneert vergelijkbaar met npm in het JavaScript ecosysteem, het beheert afhankelijkheden, coördineert builds en biedt handige commando's voor veelvoorkomende ontwikkeltaken. Wanneer je commando's als `cargo build` of `cargo run` uitvoert, regelt Cargo het compilatieproces, worden afhankelijkheden opgelost en wordt de algehele projectstructuur beheerd.


Clippy is een linter die je code analyseert en suggesties voor verbeteringen geeft. In tegenstelling tot standaard syntax checkers, begrijpt Clippy Rust idiomen en kan het meer idiomatische manieren aanbevelen om specifieke taken uit te voeren. Deze tool helpt bij het leren van Rust best practices en het schrijven van beter onderhoudbare code.


De Rust toolchain bevat ook uitgebreide documentatiehulpmiddelen en de standaardbibliotheekdocumentatie, toegankelijk via de officiële Rust documentatiewebsite. Deze documentatie dient als een onmisbare referentie tijdens de ontwikkeling en geeft gedetailleerde informatie over standaard bibliotheekfuncties, types en modules. De documentatie bevat uitgebreide voorbeelden en uitleg die u niet alleen helpen te begrijpen wat functies doen, maar ook hoe u ze effectief in uw programma's kunt gebruiken.


Rust ondersteunt meerdere release kanalen: stable, beta en nightly. Het stable kanaal biedt grondig geteste releases die geschikt zijn voor productiegebruik. Het beta-kanaal biedt een preview van de volgende stabiele release, voornamelijk gebruikt voor laatste testen voor de officiële release. Het nachtelijke kanaal bevat experimentele functies die actief worden ontwikkeld, wat handig kan zijn voor het uitproberen van nieuwe Rust mogelijkheden, hoewel deze functies kunnen veranderen of worden verwijderd in toekomstige releases.


### Rust projecten maken en beheren met Cargo


Moderne Rust ontwikkeling draait om Cargo, dat het aanmaken van projecten, het beheer van afhankelijkheden en het bouwproces stroomlijnt. In plaats van handmatig mappen en bestanden aan te maken, biedt Cargo het `cargo new` commando om generate een complete projectstructuur met verstandige standaardinstellingen te maken.


Wanneer je een nieuw project aanmaakt met `cargo new project_name`, maakt Cargo een standaard mapstructuur aan, creëert een basis `main.rs` bestand met een "Hello, world!" programma, initialiseert een Git repository en genereert een `Cargo.toml` bestand voor project configuratie. Het `Cargo.toml` bestand dient als het centrale configuratiepunt voor je project, het bevat metadata over je project en een lijst met alle afhankelijkheden die je code nodig heeft.


Cargo biedt verschillende essentiële commando's voor het dagelijkse ontwikkelwerk. De opdracht `cargo build` compileert je project en de afhankelijkheden ervan en maakt uitvoerbare bestanden aan in de map `target`. Voor snelle iteratie tijdens de ontwikkeling combineert `cargo run` het bouwen en uitvoeren in één stap. Het `cargo check` commando voert alle compilatiecontroles uit zonder het uiteindelijke uitvoerbare bestand te genereren, waardoor het aanzienlijk sneller is dan een volledige build wanneer je alleen maar wilt controleren of je code correct compileert.


Bij het voorbereiden van code voor productieuitrol schakelt de `--release` vlag optimalisaties in en verwijdert debug asserties. Release builds draaien sneller en produceren kleinere executables, maar het compileren duurt langer en nuttige debug-informatie wordt verwijderd. De compiler past verschillende optimalisaties toe tijdens release builds en schakelt runtime controles zoals integer overflow detectie uit, wat de prestaties verbetert maar enkele veiligheidsgaranties verwijdert die aanwezig zijn in debug builds.


### Variabelen, veranderlijkheid en Rust's veiligheidsfilosofie


Rust hanteert een andere benadering van variabelenbeheer dan de meeste talen. Standaard zijn alle variabelen in Rust onveranderlijk, wat betekent dat hun waarden niet kunnen worden veranderd na de initiële toewijzing. Deze ontwerpbeslissing is bedoeld om veelvoorkomende programmeerfouten te voorkomen, die ontstaan door onverwachte toestandsveranderingen.


Wanneer je een variabele declareert met `laat x = 5`, dan wordt die variabele standaard onveranderlijk. Elke poging om de waarde later te wijzigen zal resulteren in een compilatiefout. Deze onveranderlijkheidseis dwingt ontwikkelaars om goed na te denken over wanneer toestandsveranderingen echt nodig zijn en maakt het gedrag van code voorspelbaarder. Veel programmeerbugs komen voort uit variabelen die onverwacht veranderen, en Rust's standaard onveranderlijkheid helpt deze problemen te voorkomen.


Wanneer je echt de waarde van een variabele moet wijzigen, vereist Rust een expliciete declaratie van veranderlijkheid met het `mut` sleutelwoord: `laat mut x = 5`. Deze expliciete declaratie dient als een duidelijk signaal voor zowel de compiler als andere ontwikkelaars dat de waarde van deze variabele kan veranderen tijdens de uitvoering van het programma. De eis om mutabiliteit expliciet aan te geven moedigt aan om goed na te denken of mutabiliteit echt nodig is voor elke variabele.


Rust ondersteunt ook shadowing, waarmee je een nieuwe variabele kunt declareren met dezelfde naam als een vorige variabele. In tegenstelling tot mutatie, creëert shadowing een geheel nieuwe variabele die toevallig dezelfde naam heeft, waardoor de vorige variabele effectief verborgen wordt. Deze techniek is vooral nuttig bij het transformeren van gegevens door middel van meerdere stappen, zoals het parsen van een tekenreeks in een getal en vervolgens het verder verwerken van dat getal. Met shadowing kun je een consistente variabelenaam behouden tijdens het transformatieproces, terwijl je het type variabele bij elke stap verandert.


Het onderscheid tussen shadowing en mutatie wordt belangrijk als je typeveranderingen bekijkt. Met shadowing kun je zowel de waarde als het type van een variabele veranderen, omdat je een nieuwe variabele maakt. Met mutatie kun je alleen de waarde veranderen met behoud van hetzelfde type, omdat je een bestaande variabele wijzigt in plaats van een nieuwe aanmaakt.


```rust
// Shadowing: creating new variables with the same name
let amount = "100000";           // amount is a &str (string slice)
let amount = amount.parse::<u64>().unwrap();  // amount is now u64
let amount = amount * 100;       // amount is still u64, new value

// Mutation: modifying the same variable
let mut balance = 50000_u64;
balance = balance + amount;      // OK: same type, different value
// balance = "empty";            // ERROR: cannot change type with mutation

// Practical example: processing a Bitcoin amount input
let user_input = "  0.001 ";                    // &str with whitespace
let user_input = user_input.trim();            // &str, whitespace removed
let satoshis: u64 = (user_input.parse::<f64>().unwrap() * 100_000_000.0) as u64;
println!("Amount in satoshis: {}", satoshis);  // 100000
```


### Grondbeginselen gegevenstypen en typesystemen


Rust implementeert een sterk, statisch typesysteem waarbij elke waarde een goed gedefinieerd type moet hebben dat bekend is tijdens het compileren. Hoewel dit beperkend lijkt in vergelijking met dynamisch getypeerde talen, betekenen Rust's type-inferentiemogelijkheden dat je zelden expliciet typen hoeft te specificeren. De compiler kan meestal het juiste type bepalen op basis van hoe je de waarde gebruikt.


Bepaalde situaties vereisen echter expliciete type annotaties. Bij het gebruik van generieke functies zoals `parse()`, die tekenreeksen kunnen omzetten in verschillende numerieke types, moet de compiler weten welk specifiek type je wilt. In deze gevallen geef je type annotaties met de dubbele punt syntaxis: `laat raden: u32 = "42".parse().expect("Geen getal!")`.


De scalaire types van Rust zijn integers, floating-point getallen, booleans en karakters. Het integer type systeem biedt nauwkeurige controle over geheugengebruik en prestatiekenmerken. Integer typen worden systematisch benoemd: `i8`, `i16`, `i32`, `i64`, en `i128` voor signed integers, en `u8`, `u16`, `u32`, `u64`, en `u128` voor unsigned integers. De getallen geven de bitbreedte aan, waardoor geheugengebruik en waardebereiken direct duidelijk worden.


De `isize` en `usize` types verdienen speciale aandacht omdat ze zich aanpassen aan je doelarchitectuur. Op 64-bit systemen zijn deze types 64 bits breed, terwijl ze op 32-bit systemen 32 bits breed zijn. Deze types worden vaak gebruikt voor array indexering en geheugen offsets omdat ze overeenkomen met de natuurlijke woordgrootte van de doelarchitectuur, waardoor efficiënte pointer rekenkundige en geheugen bewerkingen mogelijk zijn.


Rust biedt meerdere manieren om gehele getallen te schrijven, waaronder decimale, hexadecimale (`0x`), octale (`0o`) en binaire (`0b`) formaten. Je kunt ook overal underscores gebruiken binnen numerieke liters om de leesbaarheid te verbeteren, zoals het schrijven van `1_000_000` in plaats van `1000000`. De underscores hebben geen effect op de waarde, maar kunnen grote getallen leesbaarder maken.


Floating-point typen in Rust zijn eenvoudig: `f32` voor single-precision en `f64` voor double-precision floating-point getallen. Het `f64` type heeft over het algemeen de voorkeur vanwege de hogere precisie en het feit dat moderne processoren 64-bit floating-point bewerkingen vaak net zo efficiënt kunnen afhandelen als 32-bit bewerkingen.


### Samengestelde typen en gegevensorganisatie


Naast scalaire types biedt Rust ook samengestelde types die meerdere waarden groeperen. Met tuples kun je waarden van verschillende types combineren in een enkele samengestelde waarde. Je maakt tuples met haakjes en kunt het type van elk element specificeren: `laat tup: (i32, f64, u8) = (500, 6.4, 1)`.


Tuples ondersteunen destructurering, waardoor je individuele waarden kunt extraheren: `laat (x, y, z) = tup`. Deze syntaxis maakt drie afzonderlijke variabelen van de componenten van de tuple. Als alternatief kun je tuple elementen direct benaderen door gebruik te maken van puntnotatie met de element index: `tup.0`, `tup.1`, `tup.2`.


```rust
// Creating a tuple with different types
let transaction: (&str, u64, bool) = ("abc123", 50000, true);

// Destructuring: extract all values at once
let (txid, amount, confirmed) = transaction;
println!("Transaction {} for {} sats", txid, amount);

// Dot notation: access individual elements by index
println!("Confirmed: {}", transaction.2);  // true

// Practical example: function returning multiple values
fn parse_utxo(data: &str) -> (String, u32, u64) {
// Returns (txid, output_index, value_in_sats)
("a]1b2c3".to_string(), 0, 100000)
}

let (txid, vout, value) = parse_utxo("raw_data");
println!("UTXO {}:{} = {} sats", txid, vout, value);
```


Arrays in Rust verschillen aanzienlijk van arrays of lijsten in veel andere talen, omdat ze een vaste grootte hebben die onderdeel wordt van hun type. Een array van vijf gehele getallen heeft het type `[i32; 5]`, waarbij de puntkomma het elementtype scheidt van de arraylengte. Deze informatie over de grootte op type-niveau stelt de compiler in staat om grenscontroles uit te voeren en zorgt ervoor dat functies die arrays ontvangen precies weten hoeveel elementen ze kunnen verwachten.


Je kunt arrays initialiseren door alle elementen expliciet op te sommen: `[1, 2, 3, 4, 5]`, of door een stenografische syntaxis te gebruiken voor arrays met herhaalde waarden: `[3; 5]` creëert een array van vijf elementen, allemaal met de waarde 3. Deze stenografie is handig voor het initialiseren van buffers of het maken van matrices met standaardwaarden.


Array toegang gebruikt vierkante haak notatie zoals de meeste talen, maar Rust biedt zowel compileer- als runtime bounds controle. Wanneer je een array benadert met een constante index, die de compiler kan verifiëren, zal deze out-of-bounds toegang tijdens compilatietijd detecteren. Voor dynamische indices die tijdens runtime worden bepaald, voegt Rust bounds checks toe die ervoor zorgen dat het programma in paniek raakt als je probeert een ongeldige index te benaderen, waardoor schendingen van de geheugenveiligheid worden voorkomen.



## Ownership en geheugenveiligheid in Rust

<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>


:::video id=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::


### Rust's unieke benadering van geheugenbeheer begrijpen


Dit hoofdstuk behandelt een van Rust's belangrijkste concepten. Terwijl voorgaande concepten misschien bekend aanvoelden voor programmeurs die uit andere talen komen, is eigendom Rust's benadering om geheugenveiligheid op te lossen zonder garbage collection.


Rust is ontworpen met het fundamentele doel om geheugen-gerelateerde bugs te voorkomen die low-level talen zoals C en C++ teisteren. Deze problemen omvatten use-after-free bugs, waarbij geheugen wordt benaderd nadat het is vrijgegeven, en buffer overflows, waarbij programma's buiten de toegewezen geheugengrenzen schrijven. Traditionele oplossingen voor deze problemen gingen gepaard met compromissen die Rust probeert te elimineren. Hogere talen zoals Java en Go lossen geheugenveiligheid op door middel van garbage collection, waarbij een automatisch proces periodiek ongebruikt geheugen identificeert en vrijmaakt. Echter, garbage collectors introduceren prestatie-overhead en kunnen onvoorspelbare pauzes veroorzaken tijdens het uitvoeren van programma's, waardoor ze ongeschikt zijn voor systeemprogrammering waar consistente prestaties kritisch zijn.


Rust bereikt geheugenveiligheid voornamelijk door statische analyse tijdens het compileren. De compiler onderzoekt de broncode en kan bepalen of de meeste geheugenbewerkingen veilig zijn zonder dat garbage collection nodig is. Voor gevallen die niet statisch geverifieerd kunnen worden, zoals array-toegang met runtime-berekende indices, voegt Rust bounds checks toe die eerder paniek zaaien dan ongedefinieerd gedrag toe te staan. Deze aanpak verschilt fundamenteel van statische analyzers voor C en C++, die achteraf zijn toegevoegd aan talen die oorspronkelijk niet waren ontworpen voor uitgebreide statische analyse. Rust's syntaxis en taalregels zijn vanaf de grond opgebouwd om uitgebreide compileerbare verificatie mogelijk te maken, zodat een programma, zodra het succesvol gecompileerd is, veilig draait of voorspelbaar in paniek raakt in plaats van ongedefinieerd gedrag te vertonen.


### Het Ownership systeem: Regels en principes


De hoeksteen van Rust's geheugenveiligheidsgaranties is het eigendomssysteem, dat bepaalt hoe geheugen wordt beheerd tijdens de uitvoering van een programma. Ownership werkt met drie fundamentele regels die de compiler altijd afdwingt:


1. Elke waarde in Rust heeft een eigenaar (een variabele die de waarde bevat)

2. Er kan maar één eigenaar tegelijk zijn

3. Wanneer de eigenaar buiten bereik gaat, wordt de waarde verwijderd


Scopes in Rust worden meestal gedefinieerd door accolades, in functie-organen, conditionele blokken of expliciet aangemaakte scope-blokken. Wanneer een variabele wordt gedeclareerd binnen een bereik, wordt dat bereik eigenaar van de waarde van de variabele. De variabele blijft toegankelijk en geldig gedurende de levensduur van de scope, maar zodra de uitvoering de scope verlaat, worden alle variabelen in eigendom automatisch opgeschoond door middel van een proces dat dropping wordt genoemd.


Deze automatische opschoning wordt geïmplementeerd door Rust's drop mechanisme, waarbij de taal impliciet een drop functie aanroept op variabelen die uit scope gaan. Voor basistypes betekent dit simpelweg dat het geheugen wordt gemarkeerd als beschikbaar voor hergebruik. Voor complexere types die bronnen beheren, kunnen aangepaste drop-implementaties aanvullende opschoonoperaties uitvoeren, zoals het sluiten van bestandshandgrepen of het vrijgeven van netwerkverbindingen. Dit patroon, geleend van C++'s RAII (Resource Acquisition Is Initialization), zorgt ervoor dat bronnen altijd op de juiste manier worden vrijgegeven zonder dat expliciete opruimcode van de programmeur nodig is.


### Ownership en geheugenindeling verplaatsen


Om te begrijpen hoe eigendom tussen variabelen wordt overgedragen, moet het verschil tussen eenvoudige typen en complexe typen worden onderzocht in termen van geheugenlayout en kopieergedrag. Eenvoudige types zoals gehele getallen, booleans en drijvende komma getallen hebben een vaste, bekende grootte bij het compileren en kunnen efficiënt worden gekopieerd. Wanneer je een integer variabele toewijst aan een andere, creëert Rust een complete, onafhankelijke kopie van de waarde, waardoor beide variabelen gelijktijdig kunnen bestaan zonder zorgen over eigendom.


Complexe types zoals strings vormen een andere uitdaging, omdat ze dynamisch toegewezen geheugen beheren. Een String in Rust bestaat uit drie componenten die op de stack zijn opgeslagen: een pointer naar door de heap toegewezen karakterdata, de huidige lengte van de string en de totale capaciteit van de toegewezen buffer. Deze structuur maakt het mogelijk om strings efficiënt te laten groeien en krimpen, met behoud van kennis van hun grenzen. Wanneer u een String variabele aan een andere toewijst, staat Rust voor een keuze: het kan alleen de op de stack gebaseerde structuur kopiëren (waarbij twee verwijzingen naar dezelfde heapgegevens worden gemaakt) of een diepe kopie van alle heapgegevens uitvoeren.


Het standaardgedrag van Rust is om eigendom te verplaatsen in plaats van te kopiëren, waarbij de heapgegevens van de bronvariabele naar de doelvariabele worden verplaatst en de bron ongeldig wordt gemaakt. Deze aanpak voorkomt het gevaarlijke scenario waarbij meerdere variabelen hetzelfde heap-geheugen kunnen wijzigen of waarbij hetzelfde geheugen meerdere keren kan worden vrijgemaakt wanneer variabelen uit scope gaan. De move operatie is efficiënt omdat het alleen de kleine stack-gebaseerde structuur kopieert, niet de potentieel grote heap gegevens, terwijl geheugenveiligheid behouden blijft door single ownership te garanderen.


### Referenties en lenen


Hoewel eigendomsverplaatsingen veiligheid bieden, kunnen ze beperkend zijn als je een waarde op meerdere plaatsen moet gebruiken zonder eigendom over te dragen. Rust pakt dit aan met 'borrowing', waarmee functies en variabelen tijdelijk toegang hebben tot gegevens zonder eigenaarschap over te nemen. Een referentie, gemaakt met de ampersand operator, geeft alleen-lezen toegang tot een waarde terwijl het eigendom bij de originele variabele blijft.


Met referenties kunnen functies gegevens gebruiken zonder ze te consumeren, waardoor het mogelijk wordt om dezelfde waarde meerdere keren in een programma te gebruiken. Wanneer je een referentie doorgeeft aan een functie, leen je de gegevens tijdelijk uit en de functie moet de referentie teruggeven voordat de oorspronkelijke eigenaar weer de volledige controle heeft. Deze leenmetafoor weerspiegelt de tijdelijke aard van de toegang: net zoals je een boek uitleent aan een vriend met behoud van eigendom, maken referenties tijdelijke toegang mogelijk met behoud van de oorspronkelijke eigendomsrelatie.


Muteerbare referenties breiden dit concept uit om wijziging van geleende gegevens toe te staan, maar met strikte beperkingen om de veiligheid te handhaven. Rust staat slechts één muteerbare referentie naar een stuk data op een gegeven moment toe, om dataraces te voorkomen waarbij meerdere delen van een programma tegelijkertijd hetzelfde geheugen kunnen wijzigen. Bovendien kun je niet tegelijkertijd zowel muteerbare als onveranderlijke verwijzingen naar dezelfde gegevens hebben, omdat dit kan leiden tot situaties waarin code aanneemt dat gegevens stabiel zijn terwijl andere code ze actief wijzigt. Deze regels worden tijdens het compileren afgedwongen, waardoor hele klassen van concurrency bugs die andere systeemprogrammeertalen plagen, worden geëlimineerd.


```rust
fn main() {
let mut wallet_balance: u64 = 100_000; // 100,000 satoshis

// Immutable borrow: read the balance
let balance_ref = &wallet_balance;
println!("Current balance: {} sats", balance_ref);
// balance_ref goes out of scope here

// Mutable borrow: update the balance
let balance_mut = &mut wallet_balance;
*balance_mut += 50_000; // Receive payment
println!("After deposit: {} sats", balance_mut);
// balance_mut goes out of scope here

// Function that borrows immutably
fn display_balance(balance: &u64) {
println!("Balance check: {} sats", balance);
}

// Function that borrows mutably
fn deduct_fee(balance: &mut u64, fee: u64) {
*balance -= fee;
}

display_balance(&wallet_balance);
deduct_fee(&mut wallet_balance, 1_000);
println!("After fee: {} sats", wallet_balance); // 149,000
}
```


### Soorten strings en plakjes


Rust maakt onderscheid tussen string-literalen en het type String, wat verschillende geheugenbeheerstrategieën en gebruikssituaties weerspiegelt. String literalen zijn direct ingebed in de gecompileerde binary en hebben het type &str (string slice), wat een blik vertegenwoordigt in onveranderlijke string data. Deze literalen zijn efficiënt omdat ze geen runtime toewijzing vereisen, maar ze kunnen niet gewijzigd worden omdat ze deel uitmaken van de programmacode.


Het type String daarentegen beheert dynamisch toegewezen geheugen en kan tijdens runtime groeien, krimpen en worden gewijzigd. Je kunt een String maken van een letterlijke met String::from() of vergelijkbare methoden, die heapgeheugen toewijst en de inhoud van de letterlijke kopieert. Door dit onderscheid kan Rust optimaliseren voor zowel prestatie (gebruik van literalen wanneer mogelijk) als flexibiliteit (gebruik van String wanneer aanpassing nodig is).


String slices (&str) bieden een krachtige abstractie voor het werken met delen van strings zonder gegevens te kopiëren. Een slice bevat een pointer naar het begin van de stringgegevens en een lengte, waardoor je efficiënt naar substrings kunt verwijzen. De slice syntaxis gebruikt bereiken (bijvoorbeeld &s[0..5]) om aan te geven naar welk deel van de string verwezen moet worden. Omdat slices verwijzingen zijn, zijn ze onderhevig aan leenregels, die voorkomen dat de onderliggende string wordt gewijzigd terwijl slices bestaan. Deze compileertijd handhaving voorkomt veel voorkomende bugs zoals toegang tot ongeldig geheugen nadat de originele string is vrijgegeven of gewijzigd.


### Rijen, vectoren en generieke segmenten


Het slice-concept gaat verder dan strings en omvat elke opeenvolging van elementen, en biedt een uniforme manier om te werken met arrays van vaste grootte en dynamische vectoren. Arrays in Rust hebben hun lengte gecodeerd in hun type (bijvoorbeeld, [i32; 5] voor een array van vijf 32-bit gehele getallen), waardoor ze geschikt zijn voor situaties die compileertijd grootte garanties vereisen. Functies die arrays accepteren kunnen exacte lengte eisen afdwingen, handig voor operaties zoals cryptografische functies die invoer van precieze grootte nodig hebben.


Slices (&[T]) bieden een flexibeler alternatief en vertegenwoordigen een blik op elke aaneengesloten reeks elementen, ongeacht de onderliggende opslag. Je kunt slices maken van arrays, vectoren of andere slices, en dezelfde slice kan verwijzen naar verschillende delen van gegevens tijdens zijn levensduur. Deze flexibiliteit maakt slices ideaal voor functies die reeksen moeten verwerken zonder zich zorgen te maken over het specifieke opslagmechanisme of de exacte grootte.


De relatie tussen eigen types (String, Vec<T>) en hun geleende slice tegenhangers (&str, &[T]) volgt een consistent patroon door heel Rust. Types in eigendom beheren hun geheugen en kunnen gewijzigd worden, terwijl slices efficiënte, alleen-lezen toegang bieden tot delen van die data. Dit ontwerp maakt API's mogelijk die zowel flexibel (verschillende invoertypes accepteren via slices) als efficiënt (onnodig kopiëren vermijden) zijn, met behoud van Rust's veiligheidsgaranties via het leensysteem.



## Structuren, Complexe gegevenstypen bouwen

<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>


:::video id=c78a543f-1462-43a1-9845-889d310d31a4:::

Structuren in Rust dienen als basis voor het maken van complexe gegevenstypen, vergelijkbaar met klassen in andere programmeertalen. Hiermee kun je gerelateerde gegevens groeperen in een enkele, samenhangende eenheid die meerdere velden van verschillende typen kan bevatten. De syntax voor het definiëren van een structuur volgt een eenvoudig patroon: je gebruikt het `struct` sleutelwoord gevolgd door de structuurnaam, definieert dan de velden binnen accolades met een dubbele punt syntax om het type van elk veld te specificeren.


Rust volgt specifieke naamgevingsconventies voor structuren die de compiler afdwingt door middel van waarschuwingen. Structuurnamen moeten CamelCase (ook bekend als PascalCase) gebruiken, terwijl veldnamen binnen de structuur snake_case met underscores moeten gebruiken. Deze conventie helpt de consistentie tussen Rust codebases te behouden en maakt code leesbaarder voor andere ontwikkelaars.


Om instanties van structuren te maken, moet je waarden specificeren voor alle velden door de naam van de structuur te gebruiken, gevolgd door accolades die de veldtoewijzingen bevatten. Zodra je een instantie van een structuur hebt, kun je individuele velden benaderen en wijzigen met behulp van puntnotatie, op voorwaarde dat de instantie is gedeclareerd als muteerbaar. Deze puntnotatie werkt consistent in Rust, in tegenstelling tot talen als C++ waar je verschillende operatoren kunt gebruiken voor pointers versus directe objecten.


### Constructorfuncties en sneltoetsen voor velden


Rust heeft geen ingebouwde constructeurs zoals sommige object-georiënteerde talen, maar je kunt functies maken die structuurinstanties teruggeven om hetzelfde doel te dienen. Deze constructorfuncties nemen meestal parameters mee voor sommige of alle velden en kunnen standaardwaarden instellen voor andere velden. Bij het schrijven van zulke functies, biedt Rust een handige steno: als een parameter dezelfde naam heeft als een structuurveld, kun je gewoon de veldnaam één keer schrijven in plaats van deze te herhalen in het `veld: waarde` formaat.


Structure instanties kunnen ook worden gemaakt door waarden te kopiëren van bestaande instanties met behulp van de struct update syntaxis. Met deze functie kun je een nieuwe instantie maken en alleen de velden specificeren die je wilt veranderen, waarbij alle andere velden gekopieerd worden van een bestaande instantie. Deze bewerking volgt echter Rust's eigendomsregels, wat betekent dat niet-kopieerbare types verplaatst worden van de broninstantie, waardoor delen van de originele instantie mogelijk onbruikbaar worden. De compiler volgt deze gedeeltelijke verplaatsingen op intelligente wijze, waardoor je velden die niet verplaatst zijn kunt blijven gebruiken, terwijl toegang tot verplaatste velden wordt voorkomen.


### Tuple-structuren en eenheidsstructuren


Rust ondersteunt tuple structuren, dit zijn structuren met onbenoemde velden die toegankelijk zijn via index in plaats van via naam. Deze zijn handig voor eenvoudige wrapper types of wanneer je een structuur nodig hebt, maar geen velden met naam nodig hebt. Je benadert tuple structuurvelden met puntnotatie gevolgd door de veldindex, zoals `.0` voor het eerste veld, `.1` voor het tweede, enzovoort. Deze aanpak werkt goed voor structuren die een enkele waarde bevatten of slechts een paar nauw verwante waarden waar namen overbodig kunnen zijn.


Eenheidsstructuren zijn de eenvoudigste vorm van structuren - ze bevatten helemaal geen gegevens. Hoewel dit in eerste instantie nutteloos lijkt, worden unitstructuren waardevol bij het werken met Rust's eigenschapssysteem, omdat ze gedrag kunnen implementeren zonder gegevens op te slaan. Deze lege structuren dienen als markers of plaatshouders in meer geavanceerde Rust patronen.


### Methoden en bijbehorende functies


Structuren krijgen extra functionaliteit als je gedrag toevoegt via implementatieblokken. Met behulp van het `impl` sleutelwoord gevolgd door de structuurnaam, kun je methoden definiëren die werken op instanties van je structuur. Methoden zijn functies die `self` als eerste parameter nemen, wat een eigen waarde kan zijn (`self`), een onveranderlijke verwijzing (`&self`), of een muteerbare verwijzing (`&mut self`), afhankelijk van wat de methode moet doen met de instantie.


De keuze van het `self` parametertype bepaalt het gedrag van de methode met betrekking tot eigenaarschap. Methoden die `&self` nemen kunnen van de instantie lezen zonder eigenaarschap te nemen, waardoor ze geschikt zijn voor operaties die de structuur niet wijzigen. Methoden die `&mut self` nemen, kunnen de instantie wijzigen terwijl de aanroeper nog steeds eigenaar blijft. Methoden die `self` als waarde nemen, consumeren de instantie, wat geschikt is voor bewerkingen die de structuur in iets anders veranderen of wanneer de methode de laatste bewerking op die instantie vertegenwoordigt.


Geassocieerde functies zijn functies gedefinieerd binnen een implementatieblok die `zelf` niet als parameter nemen. Deze zijn vergelijkbaar met statische methoden in andere talen en worden vaak gebruikt als constructeurs of nutsfuncties gerelateerd aan het type. Je roept geassocieerde functies aan met de dubbele dubbele punt syntaxis (`Type::function_name()`), wat ze duidelijk onderscheidt van methodes die aangeroepen worden op instanties.


```rust
// Define a struct for a Lightning invoice
struct Invoice {
payment_hash: String,
amount_msat: u64,
description: String,
expiry_secs: u32,
}

impl Invoice {
// Associated function (constructor) - no self parameter
fn new(payment_hash: String, amount_msat: u64, description: String) -> Self {
Invoice {
payment_hash,
amount_msat,
description,
expiry_secs: 3600, // default 1 hour
}
}

// Method with &self - read-only access
fn amount_sats(&self) -> u64 {
self.amount_msat / 1000
}

// Method with &mut self - can modify the instance
fn extend_expiry(&mut self, additional_secs: u32) {
self.expiry_secs += additional_secs;
}

// Method with self - consumes the instance
fn into_payment_request(self) -> String {
format!("lnbc{}n1p{}", self.amount_msat, self.payment_hash)
}
}

fn main() {
// Use associated function to create instance
let mut invoice = Invoice::new(
"abc123".to_string(),
100_000_000, // 100,000 sats in millisats
"Coffee payment".to_string(),
);

println!("Amount: {} sats", invoice.amount_sats());
invoice.extend_expiry(1800); // Add 30 minutes

let request = invoice.into_payment_request();
// invoice is now consumed, cannot be used anymore
println!("Payment request: {}", request);
}
```


#### Opsommingen: Keuzes en varianten modelleren


Enumeraties in Rust hebben meer mogelijkheden dan enums in veel andere talen. Hoewel ze eenvoudige sets van constanten met namen kunnen representeren, kunnen Rust enums ook gegevens bevatten binnen elke variant, waardoor ze geschikt zijn voor het modelleren van situaties waarin een waarde een van verschillende typen of toestanden kan zijn. Elke enum variant kan verschillende soorten en hoeveelheden gegevens bevatten, van helemaal geen gegevens tot complexe structuren met benoemde velden.


De mogelijkheid om gegevens te koppelen aan enumvarianten elimineert veel voorkomende programmeerfouten die in andere talen voorkomen. In plaats van aparte variabelen te onderhouden voor een type-indicator en de bijbehorende gegevens, die gemakkelijk inconsistent kunnen worden, bundelen Rust enums de type-informatie met de gegevens zelf. Dit ontwerp zorgt ervoor dat de gegevens altijd overeenkomen met de variant, waardoor mismatches worden voorkomen die tot runtime fouten kunnen leiden.


Enum varianten kunnen gegevens in verschillende vormen bevatten: geen gegevens voor eenvoudige vlaggen, tuple-achtige gegevens voor velden zonder naam of struct-achtige gegevens met velden met naam. Je kunt deze stijlen zelfs door elkaar gebruiken binnen één enum, waarbij je voor elke variant de meest geschikte vorm kiest. Deze flexibiliteit maakt enums geschikt voor het modelleren van complexe domeinconcepten waarbij verschillende gevallen verschillende informatie vereisen.


#### Het optietype: Veilig omgaan met afwezigheid


Een van Rust's belangrijkste enums is `Option<T>`, die waarden voorstelt die al dan niet aanwezig kunnen zijn. Dit enum heeft twee varianten: `Some(T)` dat een waarde van het type T bevat, en `None` dat de afwezigheid van een waarde representeert. Het Option type dient als Rust's oplossing voor null pointer problemen die veel andere talen plagen, en dwingt ontwikkelaars om expliciet om te gaan met gevallen waarin waarden kunnen ontbreken.


Het gebruik van optietypen maakt je code robuuster omdat de compiler vereist dat je zowel de aan- als afwezigheid van waarden afhandelt. Je kunt niet per ongeluk een mogelijk ontbrekende waarde gebruiken zonder eerst te controleren of deze bestaat. Deze expliciete afhandeling voorkomt null pointer excepties en soortgelijke runtime fouten die veelvoorkomende bronnen van bugs zijn in andere programmeertalen.


Het Option type integreert met Rust's pattern matching systeem, waardoor je beide gevallen kunt behandelen. Methoden als `unwrap_or()` bieden handige manieren om waarden te extraheren met fallback defaults, terwijl methoden als `map()` en `and_then()` functionele programmeerpatronen mogelijk maken voor het werken met optionele waarden.


### Patroonmatching met matrixuitdrukkingen


Patroonmatching via `match` expressies biedt een manier om met enums en andere gegevenstypen te werken. Een match expressie onderzoekt een waarde en voert verschillende code uit gebaseerd op welk patroon de waarde overeenkomt. Elk patroon kan de gematchte waarde destructureren, door delen ervan te binden aan variabelen die gebruikt kunnen worden in het corresponderende codeblok.


Overeenkomende expressies moeten uitputtend zijn, wat betekent dat ze elk mogelijk geval moeten behandelen voor het type dat wordt gematcht. Deze vereiste voorkomt bugs die kunnen optreden als bepaalde gevallen per ongeluk niet worden afgehandeld. Als je niet elk geval expliciet wilt afhandelen, kun je het jokertekenpatroon (`_`) gebruiken om alle resterende gevallen op te vangen, of niet-afgehandelde gevallen aan een variabele binden als je toegang tot de waarde nodig hebt.


De `if let` constructie biedt een beknopter alternatief voor match als je alleen geeft om één specifiek patroon. Deze syntaxis is vooral handig bij het werken met Optie types of wanneer je alleen code wilt uitvoeren als een waarde overeenkomt met een bepaalde enum variant. De `if let` constructie kan een `else` clausule bevatten voor gevallen waarin het patroon niet overeenkomt, waardoor het een gestroomlijnde manier is om eenvoudige patroon matching scenario's te behandelen.


#### Verzamelingen: Groepen gegevens beheren


De standaardbibliotheek van Rust biedt verschillende verzameltypes voor het beheren van groepen gerelateerde gegevens. Deze verzamelingen zijn generiek, wat betekent dat ze elementen van elk type kunnen opslaan, en ze zorgen automatisch voor geheugenbeheer. De meest gebruikte verzamelingen zijn vectoren voor geordende lijsten, hash maps voor sleutel-waarde associaties en strings voor tekstgegevens.


#### Vectoren: Dynamische matrices


Vectoren vertegenwoordigen groeibare arrays die van grootte kunnen veranderen tijdens de uitvoering van het programma. In tegenstelling tot arrays met een vaste grootte, wijzen vectoren geheugen toe op de heap en kunnen ze naar behoefte groeien of krimpen. Het maken van een vector vereist vaak expliciete type-annotatie als je begint met een lege vector, omdat de compiler moet weten welk type elementen de vector zal bevatten.


Vectoren bieden meerdere manieren om toegang te krijgen tot elementen, elk met verschillende veiligheidskenmerken. Index notatie (`vec[0]`) biedt directe toegang, maar zal in paniek raken als de index buiten de grenzen valt. De `get()` methode retourneert een `Option`, waardoor je de out-of-bounds toegang netjes kunt afhandelen. De keuze tussen deze benaderingen hangt af van of je kunt garanderen dat de index geldig is of dat je mogelijke fouten moet afhandelen.


De leenregels van Rust zijn van toepassing op vectoren, waardoor veelvoorkomende geheugenveiligheidsproblemen worden voorkomen. Als je een verwijzing naar een vectorelement vasthoudt, kun je de vector niet wijzigen totdat die verwijzing uit scope gaat. Dit voorkomt situaties waarin referenties naar gedalloceerd geheugen wijzen na vectorbewerkingen zoals het pushen van nieuwe elementen of het leegmaken van de vector.


#### Hash kaarten: Key-Value opslag


Hash maps bieden efficiënte sleutel-waarde opslag waar je snel waarden kunt opzoeken op basis van hun geassocieerde sleutels. Zowel sleutels als waarden kunnen van elk type zijn, maar sleutels moeten de nodige eigenschappen implementeren voor hashing en vergelijking van gelijkheid. Hash maps worden eigenaar van ingevoegde waarden, tenzij de waarden de eigenschap Copy implementeren.


Hash mappen bieden verschillende methoden voor het invoegen en bijwerken van waarden. De basismethode `insert()` overschrijft bestaande waarden, terwijl `entry()` meer flexibele invoeglogica biedt. Met de entry API kun je waarden alleen invoegen als ze nog niet bestaan, of bestaande waarden bijwerken op basis van hun huidige status. Deze API is nuttig voor patronen zoals het tellen van voorkomens of het bijhouden van lopende totalen.


Bij het ophalen van waarden uit hash maps, retourneert de `get()` methode een `Option` omdat de gevraagde sleutel mogelijk niet bestaat. Je kunt methoden als `copied()` gebruiken om van `Option<&T>` naar `Option<T>` te converteren voor Copy types, en `unwrap_or()` om standaard waarden te geven als sleutels ontbreken.


### Stringverwerking en Unicode


Strings in Rust zijn UTF-8 gecodeerd, wat volledige Unicode ondersteuning biedt, maar complexiteit introduceert vergeleken met eenvoudige ASCII strings. Het `String` type vertegenwoordigt eigen, groeibare tekstgegevens, terwijl string slices (`&str`) geleende weergaven in stringgegevens bieden. Je kunt tussen deze typen converteren als dat nodig is, waarbij string slices vaak gebruikt worden voor functieparameters om zowel eigen strings als string-literalen te accepteren.


Stringmanipulatie bevat methoden om tekst toe te voegen, meerdere waarden samen op te maken en substrings te extraheren. De `push_str()` methode voegt string slices toe zonder eigenaarschap te nemen, terwijl de `format!` macro een flexibele manier biedt om strings te construeren uit meerdere componenten. Wanneer je met string indices werkt, moet je UTF-8 karaktergrenzen respecteren om runtime paniek te voorkomen.


Voor veilige karakter-voor-karakter verwerking, bieden strings iterator methodes zoals `chars()` voor Unicode scalaire waarden en `bytes()` voor ruwe byte toegang. Deze iterators verwerken UTF-8 codering correct, en zorgen ervoor dat je niet per ongeluk multi-byte karakters splitst. Deze aanpak is veiliger en betrouwbaarder dan handmatig indexeren, vooral wanneer je met internationale tekst werkt die complexe Unicode karakters kan bevatten.



## Rust's twee-categorie foutverwerkingssysteem

<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>


:::video id=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::

Rust heeft een fundamenteel andere benadering van foutafhandeling dan de meeste programmeertalen. Terwijl veel talen voornamelijk vertrouwen op uitzonderingen, maakt Rust onderscheid tussen twee verschillende categorieën van fouten en biedt specifieke mechanismen voor het afhandelen van elk type. Dit hoofdstuk verkent Rust's uitgebreide foutafhandelingssysteem, dat zowel onherstelbare fouten omvat, die de programma-uitvoering beëindigen, als herstelbare fouten, die programma's in staat stellen om netjes door te blijven lopen.


### Onherstelbare fouten en paniek


Onherstelbare fouten zijn situaties waarin het programma in een inconsistente of onverwachte toestand terecht is gekomen waarvan het niet veilig kan herstellen. Dit zijn onder andere scenario's zoals een array buiten de grenzen benaderen, bewerkingen proberen die de geheugenveiligheid schenden of omstandigheden tegenkomen die wijzen op fundamentele fouten in de programmalogica. Wanneer zulke fouten optreden, is de gepaste reactie om het programma onmiddellijk te beëindigen in plaats van verdere corruptie of ongedefinieerd gedrag te riskeren.


In Rust veroorzaken onherstelbare fouten een panic, waardoor het programma op een gecontroleerde manier crasht. Voordat Rust afloopt, voert het een proces uit dat unwinding heet, waarbij het terugloopt door de call stack om een gedetailleerde stack trace te geven die precies laat zien waar de panic optrad. Dit unwinding proces helpt ontwikkelaars de bron van het probleem te identificeren tijdens het debuggen. Voor performance-kritische applicaties of embedded systemen, kunt u unwinding uitschakelen en Rust configureren om direct af te breken wanneer een panic optreedt, hoewel dit ten koste gaat van debug-informatie voor snellere beëindiging.


Je kunt een panic expliciet starten met de `panic!` macro met een aangepast bericht. Wanneer een panic optreedt, zie je uitvoer die aangeeft welke thread in paniek raakte en het bijbehorende bericht. Het instellen van de `RUST_BACKTRACE` omgevingsvariabele geeft extra debug-informatie en toont de complete aanroepstack die tot de panic heeft geleid. Bijvoorbeeld, een poging om element 99 van een vector met slechts drie elementen te benaderen zal generate een panic geven met een "index out of bounds" boodschap, samen met een backtrace die de exacte volgorde van functie-aanroepen laat zien die tot de fout hebben geleid.


### Herstelbare fouten met resultaat


Herstelbare fouten zijn verwachte foutcondities die programma's netjes kunnen afhandelen zonder af te sluiten. Voorbeelden hiervan zijn het proberen te openen van een bestand dat niet bestaat, mislukte netwerkverbindingen of ongeldige gebruikersinvoer. Voor deze situaties biedt Rust het enum `Result`, dat expliciet operaties voorstelt die kunnen mislukken en ontwikkelaars dwingt om zowel succes- als mislukkingsgevallen te behandelen.


Het enum `Result` is gedefinieerd met twee varianten: `Ok(T)` voor succesvolle operaties met een waarde van het type `T`, en `Err(E)` voor mislukkingen met een fout van het type `E`. Dit ontwerp gebruikt Rust's type systeem om er zeker van te zijn dat potentiële fouten niet genegeerd kunnen worden. Functies die kunnen falen geven een `Result` terug, en aanroepende code moet expliciet zowel de succes- als de foutgevallen afhandelen, meestal met behulp van patroonherkenning met `match` expressies.


Neem de `File::open` functie, die een `Result<File, std::io::Error>` teruggeeft. Bij het openen van een bestand ontvang je een `Bestand` object als het succesvol is of een `std::io::Error` als de bewerking mislukt. Je kunt op dit resultaat afstemmen om elk geval op de juiste manier af te handelen. In het succesgeval kun je doorgaan met bestandsoperaties, terwijl je in het foutgeval kunt proberen het bestand te maken, een alternatieve aanpak kunt proberen of de fout kunt doorgeven aan de aanroepende code. Deze expliciete afhandeling zorgt ervoor dat uw programma bewuste beslissingen neemt over foutherstel in plaats van onverwacht vast te lopen.


### Patronen en snelkoppelingen voor foutafhandeling


Terwijl expliciete patroonherkenning volledige controle geeft over de foutafhandeling, biedt Rust verschillende gemaksmethodes voor veelvoorkomende foutafhandelingspatronen. De `unwrap` methode haalt de succeswaarde uit een `Result` maar panikeert als er een fout optreedt, waardoor het nuttig is voor snelle prototyping of situaties waarin je er zeker van bent dat een operatie zal slagen. De `expect` methode werkt op dezelfde manier, maar stelt je in staat om een aangepaste paniekboodschap op te geven, waardoor debuggen eenvoudiger wordt als het fout gaat.


Voor meer flexibele foutafhandeling kunt u met methodes als `unwrap_of_else` een afsluiting opgeven die wordt uitgevoerd wanneer er een fout optreedt, waardoor aangepaste herstellogica mogelijk wordt. Je kunt deze operaties aan elkaar koppelen om complexe scenario's af te handelen, zoals het proberen te openen van een bestand en het maken als het niet bestaat, met verschillende foutafhandelingsstrategieën voor elke stap.


De vraagteken operator (`?`) biedt een beknopte syntaxis voor foutvoortplanting, wat veel voorkomt in Rust programma's. Wanneer je `?` toevoegt aan een `Result`, worden succesvolle waarden automatisch uitgepakt en fouten onmiddellijk teruggegeven vanuit de huidige functie. Deze operator kan alleen gebruikt worden in functies die `Result` types teruggeven, om er zeker van te zijn dat fouten goed doorgegeven kunnen worden naar de aanroepstapel. De `?` operator maakt code voor foutafhandeling veel leesbaarder door het elimineren van verbose match expressies met behoud van expliciete foutvoortplanting semantiek.


```rust
use std::fs::File;
use std::io::{self, Read};

// Custom error type for wallet operations
#[derive(Debug)]
enum WalletError {
FileNotFound,
InvalidFormat,
InsufficientFunds,
}

// Function returning Result for recoverable errors
fn load_wallet_balance(path: &str) -> Result<u64, WalletError> {
// Simulate reading from file
let balance_str = "150000"; // Would normally read from file
balance_str
.parse::<u64>()
.map_err(|_| WalletError::InvalidFormat)
}

// Using the ? operator for clean error propagation
fn send_payment(amount: u64) -> Result<String, WalletError> {
let balance = load_wallet_balance("wallet.dat")?; // Propagates error if it fails

if balance < amount {
return Err(WalletError::InsufficientFunds);
}

Ok(format!("Sent {} sats, remaining: {}", amount, balance - amount))
}

fn main() {
// Handle the Result explicitly
match send_payment(50_000) {
Ok(msg) => println!("Success: {}", msg),
Err(WalletError::InsufficientFunds) => println!("Error: Not enough funds"),
Err(WalletError::FileNotFound) => println!("Error: Wallet file not found"),
Err(WalletError::InvalidFormat) => println!("Error: Corrupted wallet file"),
}

// Or use unwrap_or_else for custom fallback
let result = send_payment(200_000)
.unwrap_or_else(|e| format!("Payment failed: {:?}", e));
println!("{}", result);
}
```


### Foutvoortplanting en functieontwerp


Foutvoortplanting is een fundamenteel concept in Rust foutafhandeling, dat functies toestaat om fouten door te geven naar de aanroepstapel in plaats van ze lokaal af te handelen. Wanneer je functies ontwerpt die kunnen falen, moet je `Result` types teruggeven om aanroepers de flexibiliteit te geven om te beslissen hoe ze fouten afhandelen. Deze aanpak bevordert samengestelde foutafhandeling waarbij elke functie in de aanroepketen fouten lokaal kan afhandelen of ze kan doorgeven aan code op een hoger niveau die meer context heeft om herstelbeslissingen te nemen.


De vraagteken operator vereenvoudigt het doorgeven van fouten. In plaats van het schrijven van verbose match expressies voor elke mogelijk falende operatie, kun je operaties aan elkaar rijgen met `?` operatoren, waardoor leesbare code ontstaat die het succespad afhandelt terwijl fouten die optreden automatisch worden doorgegeven. Dit patroon komt zo vaak voor dat veel Rust functies speciaal ontworpen zijn om goed te werken met de `?` operator, waardoor een vloeiende foutafhandeling in je codebase mogelijk is.


Als je moet kiezen tussen paniek zaaien en fouten terugsturen, overweeg dan of de aanroepende code redelijkerwijs kan herstellen van de fout. Als een fout een programmeerfout of een onherstelbare systeemstatus vertegenwoordigt, is paniek zaaien gepast. Als de fout echter een verwachte toestand is die de aanroepende code afhankelijk van de context anders kan afhandelen, biedt het teruggeven van een `Result` meer flexibiliteit en combineerbaarheid.


### Beste praktijken en ontwerpoverwegingen


Effectieve foutafhandeling in Rust vereist een zorgvuldige afweging van wanneer paniek te zaaien versus wanneer fouten terug te sturen. Gebruik paniek voor situaties die programmeerfouten representeren of toestanden die nooit zouden mogen voorkomen in correcte programma's, zoals het benaderen van hard gecodeerde gegevens waarvan je weet dat ze geldig zijn. Bijvoorbeeld, het parsen van een hardcoded IP adres waarvan je hebt geverifieerd dat het correct is, kan veilig `expect` gebruiken met een beschrijvende boodschap die uitlegt waarom de operatie nooit zou mogen mislukken.


Geef bij gebruikersgestuurde invoer of externe systeeminteracties altijd de voorkeur aan het retourneren van `Result` types in plaats van in paniek te raken. Gebruikers maken fouten, bestanden worden verwijderd en netwerkverbindingen falen - dit zijn normale omstandigheden die goed ontworpen programma's netjes moeten afhandelen. Door fouten terug te geven voor deze situaties, kun je aanroepende code de juiste herstelstrategieën laten implementeren, of dat nu is door de gebruiker om andere invoer te vragen, terug te vallen op standaardwaarden of behulpzame foutmeldingen weer te geven.


Overweeg om aangepaste types te maken die validatie afdwingen tijdens het bouwen om te voorkomen dat ongeldige toestanden zich door je programma verspreiden. Als je programma bijvoorbeeld getallen binnen een bepaald bereik vereist, maak dan een wrapper type dat invoer valideert tijdens het bouwen en geen manier biedt om ongeldige instanties te maken. Deze aanpak maakt gebruik van Rust's type systeem om hele klassen van fouten te elimineren door ongeldige toestanden onrepresenteerbaar te maken, waardoor de noodzaak voor runtime foutcontrole in je hele codebase vermindert.


## Functionele programmeerfuncties, sluitingen en slimme aanwijzers


<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>


:::video id=5514da77-5b71-4763-96b8-49eb21291c2b:::

Hoewel Rust geen pure functionele programmeertaal is, bevat het functies die geïnspireerd zijn door functionele programmeerparadigma's. Deze functies stellen ontwikkelaars in staat om beknopte code te schrijven door gebruik te maken van concepten als closures en iterators. Rust bevat deze functionele elementen om flexibele hulpmiddelen te bieden voor gegevensverwerking en callback mechanismen.


De functionele programmeerfuncties in Rust behouden de kernprincipes van de taal, namelijk geheugenveiligheid en nul-kosten abstracties. Wanneer u closures en iterators gebruikt, offert u geen prestaties op voor expressiviteit - de Rust compiler optimaliseert deze constructies om efficiënte machinecode te produceren die vergelijkbaar is met traditionele op lussen gebaseerde benaderingen.


### Sluitingen begrijpen


Closures in Rust zijn anonieme functies die variabelen uit hun omgeving kunnen vastleggen. In andere programmeertalen worden ze vaak lambda-functies genoemd. Het belangrijkste kenmerk van closures is hun vermogen om hun omgeving "af te sluiten", wat betekent dat ze toegang hebben tot en gebruik kunnen maken van variabelen die bestaan in het bereik waar de closure is gedefinieerd.


De syntaxis voor afsluitingen gebruikt pijptekens (`|`) in plaats van haakjes om parameters te definiëren. Voor een closure zonder parameters schrijf je `||`, en voor closures met parameters som je ze op tussen de pipes zoals `|x, y|`. Als de closure uit een enkele expressie bestaat, kun je de accolades weglaten, wat de syntaxis erg beknopt maakt.


Neem dit praktische voorbeeld van een T-shirtbedrijf dat exclusieve shirts weggeeft op basis van de voorkeuren van klanten. Als een klant een favoriete kleur heeft opgegeven, krijgen ze die kleur; anders krijgen ze standaard de kleur die het meest op voorraad is. Met behulp van closures wordt deze logica: `user_preference.unwrap_or_else(|| self.most_stocked())`. De closure `| self.most_stocked()` geeft de standaardwaarde alleen wanneer dat nodig is, en het heeft toegang tot `self` vanuit zijn omgeving.


### Sluitingstype-inferentie en flexibiliteit


Een van Rust's handigste functies met closures is automatische type-inferentie. In tegenstelling tot gewone functies waarbij je expliciet parameter- en terugkeertypes moet specificeren, kunnen closures deze types vaak afleiden uit de context. De compiler analyseert hoe de closure wordt gebruikt en bepaalt automatisch de juiste types. Echter, zodra een closure wordt aangeroepen met specifieke types, worden die types vast voor die closure instantie.


Je kunt afsluitingen opslaan in variabelen net als elke andere waarde, waardoor ze eersteklas burgers worden in de taal. Wanneer je een afsluiting aan een variabele toewijst, kun je deze later aanroepen met haakjes: `laat mijn_sluiting = |x| x + 1; laat resultaat = mijn_sluiting(5);`. Dankzij deze flexibiliteit kun je sluitingen als argumenten aan functies doorgeven, ze retourneren vanuit functies en ze gebruiken in gegevensstructuren.


Als de compiler geen types kan afleiden of als je expliciet wilt zijn, kun je closure parameters en return types annoteren met een syntaxis die lijkt op die van functies: `|x: i32| -> i32 { x + 1 }`. Deze expliciete typering is soms nodig in complexe scenario's waar de compiler extra informatie nodig heeft om types correct op te lossen.


### Omgevingsvariabelen vastleggen


Closures kunnen variabelen uit hun omgeving op drie verschillende manieren vastleggen: door onveranderlijke referentie, door muteerbare referentie, of door eigenaarschap te nemen. De Rust compiler bepaalt automatisch de meest beperkende methode die voldoet aan de behoeften van je closure, volgens het principe van de minste privilege.


Als een closure alleen een waarde hoeft te lezen, vangt het op via een onveranderlijke verwijzing. Hierdoor blijft de oorspronkelijke variabele toegankelijk nadat de closure is gedefinieerd en aangeroepen. Bijvoorbeeld, een closure die een lijst afdrukt zal de lijst onveranderbaar lenen, waardoor je de lijst kunt blijven gebruiken nadat de closure is uitgevoerd.


Als een closure een vastgelegde variabele moet wijzigen, moet het vastleggen via een muteerbare referentie. In dit geval moeten zowel de vastgelegde variabele als de closure zelf als muteerbaar worden gedeclareerd. De closure kan dan de vastgelegde variabele wijzigen, maar de leenregels zijn nog steeds van toepassing - je kunt geen andere verwijzingen naar die variabele hebben zolang de mutable closure bestaat.


De meest beperkende capture methode is het nemen van eigenaarschap, wat de vastgelegde variabelen naar de closure verplaatst. Dit is nodig als de closure het bereik waar de variabelen oorspronkelijk gedefinieerd waren kan overschrijden, zoals bij het spawnen van threads. Je kunt het vastleggen van eigendom forceren met het `move` sleutelwoord voor de closure parameters: `move |x| { /* closure body */ }`. Dit is essentieel voor de veiligheid van threads, omdat threads niet veilig kunnen lenen van andere threads die mogelijk eindigen en hun variabelen laten vallen.


### Afsluitingskenmerken en functietypen


Rust vertegenwoordigt afsluitingen door middel van een eigenschapssysteem met drie belangrijke eigenschappen: `FnOnce`, `FnMut` en `Fn`. Deze eigenschappen vormen een hiërarchie die beschrijft hoe afsluitingen kunnen worden aangeroepen en wat ze kunnen doen met vastgelegde variabelen.


`FnOnce` is de meest basale eigenschap die alle closures implementeren. Het vertegenwoordigt closures die minstens één keer aangeroepen kunnen worden. Sommige closures, met name closures die vastgelegde waarden verplaatsen of op een andere manier consumeren, kunnen maar één keer worden aangeroepen omdat ze hun vastgelegde gegevens tijdens de uitvoering vernietigen of verplaatsen.


`FnMut` vertegenwoordigt afsluitingen die meerdere keren aangeroepen kunnen worden en hun vastgelegde omgeving kunnen muteren. Deze afsluitingen vangen variabelen op door middel van muteerbare referentie en kunnen deze wijzigen over meerdere aanroepen. De leenregels zorgen ervoor dat wanneer een `FnMut` closure actief is, deze exclusieve muteerbare toegang heeft tot de vastgelegde variabelen.


`Fn` is de meest beperkende eigenschap, en vertegenwoordigt afsluitingen die meerdere keren aangeroepen kunnen worden zonder hun vastgelegde omgeving te wijzigen. Deze afsluitingen vangen alleen op door onveranderlijke referentie en kunnen gelijktijdig aangeroepen worden zonder Rust's veiligheidsgaranties te schenden. Als een closure `Fn` implementeert, implementeert het automatisch ook `FnMut` en `FnOnce`, aangezien meervoudig aanroepbaar zijn zonder mutatie impliceert dat het aanroepbaar is met mutatie en eenmaal aanroepbaar is.


### Werken met Iteratoren


Iteratoren in Rust bieden een manier om reeksen gegevens te verwerken. Ze zijn lui, wat betekent dat ze geen werk uitvoeren totdat je ze gebruikt door methodes aan te roepen die daadwerkelijk door de gegevens itereren. Deze luie evaluatie maakt een efficiënte keten van bewerkingen mogelijk zonder tussenliggende verzamelingen aan te maken.


De `Iterator` eigenschap definieert de kernfunctionaliteit met een geassocieerd type `Item` dat voorstelt wat de iterator oplevert en een `next` methode die `Option<Self::Item>` teruggeeft. Wanneer `next` `None` teruggeeft, is de iterator uitgeput. Met dit ontwerp kunnen iterators zowel eindige als potentieel oneindige reeksen veilig weergeven.


Je kunt iterators van verzamelingen maken met methoden als `iter()` voor iteratie lenen, `iter_mut()` voor muteerbare iteratie lenen en `into_iter()` voor iteratie consumeren. De keuze tussen deze methoden hangt af van of je elementen moet wijzigen en of je de oorspronkelijke verzameling wilt consumeren.


### Iterator-adapters en -consumenten


Iteratoradapters zijn methoden die de ene iterator transformeren in een andere, waardoor je bewerkingen aan elkaar kunt koppelen. Gebruikelijke adaptors zijn `map` om elk element te transformeren, `filter` om elementen te selecteren op basis van een predicaat en `enumerate` om indices toe te voegen. Deze adaptors zijn lui - ze doen geen werk totdat ze worden geconsumeerd.


De `map` methode past een afsluiting toe op elk element en transformeert het in iets anders. Bijvoorbeeld, `numbers.iter().map(|x| x * 2)` maakt een iterator die elk getal verdubbelt. De `filter` methode bewaart alleen elementen waarvoor de predicaatsluiting waar is: `numbers.iter().filter(|&x| x > 10)` bewaart alleen getallen groter dan tien.


Consumentenmethoden itereren daadwerkelijk door de gegevens en produceren een eindresultaat. De `collect` methode consumeert een iterator en maakt er een collectie van. Je moet vaak het verzameltype specificeren: `let vec: Vec<_> = iterator.collect()`. Andere consumenten zijn `sum` voor het optellen van numerieke elementen, `fold` voor het accumuleren van waarden met een aangepaste bewerking en `for_each` voor het uitvoeren van neveneffecten op elk element.


### Geavanceerde Iteratorpatronen


Extra iteratorbewerkingen zijn `zip` voor het elementgewijs combineren van twee iteratoren, `chain` voor het aaneenrijgen van iteratoren en `filter_map` voor het combineren van filteren en mappen in één bewerking. De `zip` methode creëert paren van overeenkomstige elementen van twee iteratoren: `a.iter().zip(b.iter())` produceert tuples `(a[0], b[0]), (a[1], b[1]), ...`.


De `fold` methode is handig voor het accumuleren van waarden. Het neemt een beginwaarde en een afsluiting die de accumulator combineert met elk element: `numbers.iter().fold(0, |acc, x| acc + x)` telt alle getallen op. Dit patroon kan veel andere bewerkingen implementeren, zoals het vinden van maximale waarden, het bouwen van strings of het maken van complexe gegevensstructuren.


Iterator-ketens kunnen complexe gegevenstransformaties beknopt uitdrukken. Het verwerken van audiogegevens kan bijvoorbeeld het volgende inhouden: `coëfficiënten.iter().zip(buffer.iter()).map(|(c, b)| c * b).sum::<i32>() >> 12`. Dit vermenigvuldigt overeenkomstige coëfficiënten en bufferwaarden, telt de resultaten op en verschuift de uiteindelijke waarde, allemaal in een enkele leesbare expressie.


```rust
fn main() {
// Sample UTXOs: (txid_suffix, amount_sats)
let utxos = vec![
("a1b2", 50_000u64),
("c3d4", 15_000),
("e5f6", 100_000),
("g7h8", 3_000),
("i9j0", 75_000),
];

// Using closures and iterators to process UTXOs

// 1. Filter UTXOs above dust threshold (10,000 sats)
let spendable: Vec<_> = utxos
.iter()
.filter(|(_, amount)| *amount >= 10_000)
.collect();
println!("Spendable UTXOs: {:?}", spendable);

// 2. Calculate total balance with fold
let total_balance: u64 = utxos
.iter()
.map(|(_, amount)| amount)
.fold(0, |acc, amount| acc + amount);
println!("Total balance: {} sats", total_balance);

// 3. Find UTXOs needed to cover a 120,000 sat payment
let target = 120_000u64;
let mut accumulated = 0u64;
let selected: Vec<_> = utxos
.iter()
.filter(|(_, amount)| *amount >= 10_000) // Skip dust
.take_while(|(_, amount)| {
if accumulated >= target {
false
} else {
accumulated += amount;
true
}
})
.collect();
println!("Selected for payment: {:?}", selected);

// 4. Transform to display format using map and collect
let display_strings: Vec<String> = utxos
.iter()
.map(|(txid, amount)| format!("{}...:{} sats", txid, amount))
.collect();
println!("Display: {:?}", display_strings);
}
```


### Inleiding tot Smart Pointers


Smart pointers zijn gegevensstructuren die zich gedragen als traditionele pointers, maar die extra mogelijkheden en automatisch geheugenbeheer bieden. In tegenstelling tot eenvoudige verwijzingen, zijn slimme pointers eigenaar van de data waarnaar ze wijzen en kunnen ze aangepast gedrag implementeren voor geheugentoewijzing, deallocatie en toegangspatronen. Ze zijn essentiële hulpmiddelen voor het beheren van gegevens die op de heap zijn toegewezen en voor het implementeren van complexe eigendomspatronen die verder gaan dan het basiseigendomssysteem van Rust.


Het "slimme" aspect komt van hun vermogen om automatisch geheugenbeheertaken af te handelen die anders handmatige interventie zouden vereisen. Wanneer een smart pointer buiten scope gaat, kan het automatisch geassocieerd geheugen vrijmaken, referentietellingen verlagen of andere opschoonoperaties uitvoeren. Deze automatisering helpt geheugenlekken en "use-after-free" fouten te voorkomen, terwijl het meer flexibiliteit biedt dan alleen toewijzen in stapels.


Smartpointers implementeren gewoonlijk twee belangrijke eigenschappen: `Deref` en `Drop`. Met de `Deref` eigenschap kan de smart pointer worden gebruikt alsof het een verwijzing is naar de gegevens die het bevat. De `Drop` eigenschap maakt aangepaste opruimlogica mogelijk wanneer de smart pointer wordt vernietigd. Samen zorgen deze eigenschappen ervoor dat smart pointer automatisch geheugen beheert.


### De doos Smart Pointer


`Box<T>` is de eenvoudigste smart pointer, die heap allocatie biedt voor elk type `T`. Wanneer je een `Box` maakt, wordt de waarde opgeslagen op de heap in plaats van op de stack, en de `Box` zelf (die gewoon een pointer is) wordt opgeslagen op de stack. Deze indirectie is handig als je grote hoeveelheden gegevens moet opslaan zonder ze te verplaatsen, als je een type nodig hebt met onbekende compileertijdgrootte of als je het eigendom van heapgegevens efficiënt wilt overdragen.


Het maken van een `Box` is eenvoudig: `let boxed_value = Box::new(42);` wijst een geheel getal toe op de heap. De `Box` beheert dit geheugen automatisch - wanneer de `Box` uit scope gaat, wordt het heap geheugen automatisch gedealloceerd. Deze automatische opschoning voorkomt geheugenlekken zonder dat handmatig geheugenbeheer nodig is.


Een van de belangrijkste toepassingen van `Box` is het mogelijk maken van recursieve datastructuren. Neem een gelinkte lijst waar elk knooppunt een waarde bevat en een pointer naar het volgende knooppunt. Zonder `Box` kun je zo'n structuur niet definiëren omdat de compiler de grootte van een type dat zichzelf bevat niet kan bepalen. Door `Box<Node>` te gebruiken voor de volgende pointer, doorbreek je het probleem van recursieve grootte omdat `Box` een bekende, vaste grootte heeft, ongeacht wat het bevat.


### De eigenschap Deref implementeren


Met de `Deref` eigenschap kan een type worden gederefereerd met behulp van de `*` operator, waardoor smart pointer zich gedragen als verwijzingen naar de gegevens die het bevat. Als je `Deref` implementeert voor een smart pointer, schakel je automatisch dereferencen in waardoor de smart pointer transparant wordt om te gebruiken. Dit betekent dat je methoden op het bevatte type direct kunt aanroepen via de smart pointer zonder expliciete dereferencing.


De `Deref` eigenschap definieert een geassocieerd type `Doel` dat specificeert welk type verwijzing de verwijzing moet opleveren. De eigenschap vereist implementatie van een `deref` methode die een verwijzing naar het doeltype teruggeeft. Voor `Box<T>` geeft de implementatie een verwijzing terug naar de waarde `T` die het bevat.


Rust voert automatische deref coercion uit, wat betekent dat de compiler automatisch `deref` kan aanroepen wanneer dat nodig is om types compatibel te maken. Daarom kun je een `String` doorgeven aan een functie die een `&str` verwacht - de compiler derefereert automatisch de `String` om een string slice te krijgen. Deze coërcie kan op meerdere niveaus, dus een `Box<String>` kan automatisch worden geconverteerd naar een `&str` door meerdere deref operaties.


### Aangepaste druppelimplementatie


Met de `Drop` eigenschap kun je aangepaste opschooncode specificeren die wordt uitgevoerd wanneer een waarde buiten scope gaat. Dit is vooral belangrijk voor slimme pointers die bronnen beheren die verder gaan dan alleen geheugen, zoals bestandshandgrepen, netwerkverbindingen of referentietellingen. De `Drop` eigenschap heeft een enkele methode, `drop`, die een muteerbare verwijzing naar `zelf` aanneemt en de opschoning uitvoert.


De meeste types hebben geen aangepaste `Drop` implementaties nodig, omdat Rust het laten vallen van hun velden automatisch afhandelt. Echter, smart pointer hebben vaak aangepaste logica nodig om de bronnen die ze beheren goed op te ruimen. Bijvoorbeeld, een smart pointer met referentietelling moet de referentietelling verlagen en mogelijk gedeelde data dealloceren wanneer de laatste referentie wordt verwijderd.


Je kunt ook expliciet een waarde laten vallen voordat deze uit scope gaat met `std::mem::drop()`. Deze functie neemt het eigendom van een waarde en laat het onmiddellijk vallen, wat handig kan zijn om bronnen vroegtijdig vrij te geven of om ervoor te zorgen dat het opruimen op een specifiek punt in je programma gebeurt. De expliciete drop functie is gewoon een identiteitsfunctie die eigenaarschap neemt - het echte werk gebeurt wanneer de waarde wordt gedropt aan het einde van de functie.


Deze basis van closures, iterators en smart pointers geeft Rust ontwikkelaars tools om expressieve, veilige en efficiënte code te schrijven. Deze functies werken samen om veelgebruikte programmeerpatronen mogelijk te maken, terwijl Rust's kerngaranties voor geheugenveiligheid en prestaties behouden blijven.



## Referentietelling en interne veranderlijkheid

<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>


:::video id=44c681d1-d154-4240-b3e8-15590cbfcbd2:::

### Referentietelling met RC


Referentietelling vertegenwoordigt een ander fundamenteel type smart pointer in Rust, speciaal ontworpen om meerdere eigendomsscenario's mogelijk te maken. In tegenstelling tot Box, dat de traditionele regels voor enkelvoudig eigendom volgt waarbij één entiteit eigenaar is van de gegevens, maakt RC (Reference Counter) het mogelijk dat meerdere delen van je code tegelijkertijd eigenaar zijn van dezelfde gegevens. Dit gedeelde eigendomsmodel werkt door middel van een telmechanisme dat bijhoudt hoeveel referenties er bestaan naar een bepaald stuk data.


Het referentiesysteem werkt door een interne teller in stand te houden die elke keer dat je een RC kloont, wordt verhoogd en wordt verlaagd wanneer een RC wordt verwijderd. Geheugen wordt alleen vrijgemaakt als deze teller nul bereikt, zodat gegevens geldig blijven zolang er een referentie bestaat. Deze aanpak voorkomt voortijdige deallocatie en maakt flexibele patronen voor het delen van gegevens mogelijk die onmogelijk zouden zijn met eenvoudige Box-eigendom.


Een praktisch voorbeeld waarbij RC nuttig is, is het maken van gedeelde gegevensstructuren zoals gekoppelde lijsten waarbij meerdere lijsten naar hetzelfde staartgedeelte kunnen verwijzen. Overweeg een poging om twee afzonderlijke lijsten te maken die beide verwijzen naar een gemeenschappelijke subsequentie. Met Box ownership wordt dit onmogelijk omdat het verplaatsen van het gedeelde gedeelte naar de eerste lijst het eigendom overdraagt, waardoor het niet gebruikt kan worden in de tweede lijst. RC lost dit op door je toe te staan de verwijzing te klonen in plaats van de onderliggende gegevens, waardoor de gedeelde structuur mogelijk wordt met behoud van geheugenveiligheid.


Wanneer je een RC kloont, dupliceer je niet de interne data, ongeacht de grootte of complexiteit ervan. In plaats daarvan creëer je een andere referentie naar dezelfde geheugenlocatie en verhoog je de teller van de referentie. Dit maakt het klonen van RC instanties efficiënt, zelfs voor grote gegevensstructuren, omdat alleen de referentie zelf wordt gekopieerd terwijl de onderliggende gegevens op hun plaats blijven.


### Interne veranderlijkheid met RefCell


RefCell introduceert interne muteerbaarheid, waardoor je gegevens kunt muteren, zelfs als je er alleen een onveranderlijke referentie naar hebt. Deze mogelijkheid verandert fundamenteel hoe Rust's leenregels worden afgedwongen door de controles te verplaatsen van compilatietijd naar runtime. Terwijl normale referenties afhankelijk zijn van de compiler om de leenveiligheid te verifiëren, voert RefCell deze controles uit tijdens de programma-uitvoering, wat meer flexibiliteit biedt tegen de kosten van mogelijke runtime paniek.


Het kernprincipe achter RefCell is het handhaven van dezelfde leenregels die Rust normaal gesproken afdwingt tijdens het compileren, maar ze dynamisch controleert. Op elk gegeven moment kun je één muteerbare verwijzing of een willekeurig aantal onveranderbare verwijzingen naar de gegevens in een RefCell hebben. Als je code deze regels probeert te overtreden door tegelijkertijd conflicterende borrows aan te maken, zal het programma in paniek raken in plaats van ongedefinieerd gedrag te produceren.


Deze runtime controle maakt bepaalde programmeerpatronen mogelijk die de compiler zou kunnen afwijzen, zelfs als ze eigenlijk veilig zijn. De statische analyse van de compiler kan niet altijd bewijzen dat complexe leenpatronen correct zijn, waardoor hij de voorkeur geeft aan voorzichtigheid. RefCell staat je toe om deze conservatieve beperkingen op te heffen als je zeker bent van de correctheid van je code, maar dit vertrouwen komt met de verantwoordelijkheid van het juiste gebruik om runtime crashes te voorkomen.


Een veelvoorkomend gebruik van RefCell betreft mock objecten in testscenario's. Als je een eigenschap implementeert die alleen onveranderlijke toegang tot zelf biedt, maar je mock-implementatie moet statusveranderingen intern bijhouden, dan maakt RefCell dit patroon mogelijk. Je kunt de interne toestand in een RefCell verpakken, waardoor de mock zijn volggegevens kan muteren, zelfs via een onveranderlijke interface.


### RC en RefCell combineren voor gedeelde muteerbare staat


De combinatie van RC en RefCell creëert een patroon voor gedeelde muteerbare toestand, waarbij meerdere eigenaren mogelijk allemaal dezelfde gegevens kunnen wijzigen. RC biedt de mogelijkheid voor gedeeld eigendom, terwijl RefCell mutatie mogelijk maakt door middel van onveranderlijke referenties. Deze combinatie is handig in scenario's zoals grafiekstructuren, caches of elke andere situatie waarin meerdere delen van je programma zowel lees- als schrijftoegang nodig hebben tot gedeelde gegevens.


Als je een RefCell in een RC wikkelt, creëer je een structuur die gekloond en gedistribueerd kan worden door je programma, waarbij elke kloon toegang geeft tot dezelfde onderliggende muteerbare gegevens. Alle eigenaren kunnen mogelijk de gegevens wijzigen met de borrow_mut methode van RefCell, maar ze moeten nog steeds de leenregels respecteren tijdens runtime. Dit patroon maakt complexe scenario's voor het delen van gegevens mogelijk, met behoud van de veiligheidsgaranties van Rust door middel van runtime controles.


Deze flexibiliteit heeft echter belangrijke nadelen met betrekking tot geheugenlekken en referentiecycli. Bij het gebruik van RC met RefCell wordt het mogelijk om per ongeluk circulaire verwijzingen te maken waarbij gegevensstructuren naar zichzelf verwijzen, hetzij direct of via een keten van verwijzingen. Deze cycli voorkomen dat het aantal verwijzingen ooit nul bereikt, wat geheugenlekken veroorzaakt omdat de gegevens altijd actieve verwijzingen lijken te hebben, zelfs als ze niet meer toegankelijk zijn vanuit de rest van het programma.


De oplossing voor referentiecycli is het gebruik van zwakke referenties, die niet bijdragen aan het aantal referenties dat wordt gebruikt voor beslissingen over geheugenbeheer. Met zwakke verwijzingen kun je verbindingen tussen gegevensstructuren onderhouden zonder ze in leven te houden, waardoor potentiële cycli worden verbroken terwijl de mogelijkheid behouden blijft om toegang te krijgen tot gerelateerde gegevens wanneer deze nog steeds bestaan.


```rust
use std::rc::Rc;
use std::cell::RefCell;

// Simulating a channel state that multiple components need to access and modify
#[derive(Debug)]
struct ChannelState {
channel_id: String,
local_balance_msat: u64,
remote_balance_msat: u64,
is_active: bool,
}

fn main() {
// Rc<RefCell<T>> allows multiple owners with interior mutability
let channel = Rc::new(RefCell::new(ChannelState {
channel_id: "abc123".to_string(),
local_balance_msat: 1_000_000_000,  // 1M sats in msats
remote_balance_msat: 500_000_000,
is_active: true,
}));

// Clone Rc to share ownership (cheap - only increments counter)
let channel_for_ui = Rc::clone(&channel);
let channel_for_router = Rc::clone(&channel);

// Reference count is now 3
println!("Reference count: {}", Rc::strong_count(&channel));

// UI component reads the state (immutable borrow)
{
let state = channel_for_ui.borrow();
println!("UI shows balance: {} msats", state.local_balance_msat);
} // borrow ends here

// Router updates the state after a payment (mutable borrow)
{
let mut state = channel_for_router.borrow_mut();
state.local_balance_msat -= 100_000_000; // Sent 100k sats
state.remote_balance_msat += 100_000_000;
println!("Router updated balances");
} // mutable borrow ends here

// Original reference can still read the updated state
let state = channel.borrow();
println!("New local balance: {} msats", state.local_balance_msat);

// WARNING: This would panic at runtime!
// let borrow1 = channel.borrow();
// let borrow2 = channel.borrow_mut(); // PANIC: already borrowed
}
```


### Thread Safety en Concurrency Fundamentals


Rust's benadering van gelijktijdigheid concentreert zich op het voorkomen van dataraces en geheugenveiligheidsproblemen tijdens het compileren. Het typesysteem dwingt threadveiligheid af door eigenschappen als `Send` en `Sync`, die types respectievelijk markeren als veilig voor overdracht tussen threads of veilig voor gelijktijdige toegang. Deze controle tijdens het compileren vangt veel concurrency bugs op die alleen tijdens runtime zouden verschijnen in andere systeemprogrammeertalen.


Het aanmaken van threads in Rust volgt een eenvoudig patroon met thread::spawn, dat een closure aanneemt om uit te voeren in de nieuwe thread en een handle teruggeeft om de levenscyclus van de thread te beheren. De gespawnde thread draait gelijktijdig met de hoofd thread en je kunt de join methode op de handle gebruiken om te wachten op voltooiing. Zonder expliciet joinen kunnen gespawnde threads worden beëindigd wanneer de hoofd thread afsluit, waardoor mogelijk onvolledig werk wordt afgebroken.


Het move sleutelwoord wordt cruciaal bij het werken met threads omdat closures die worden doorgegeven aan gespawnde threads vaak hun eigen data moeten hebben in plaats van deze te lenen. Aangezien gespawnde threads langer kunnen leven dan de scope die ze heeft aangemaakt, kan het lenen van gegevens van de bovenliggende scope leiden tot mogelijke schending van de levensduur. Het verplaatsen van gegevens naar de threadsluiting draagt het eigendom over en zorgt ervoor dat de gegevens geldig blijven gedurende de gehele levensduur van de thread, terwijl toegang vanuit de oorspronkelijke scope wordt voorkomen.


Het doorgeven van berichten biedt een alternatief voor gedeelde toestandsconcurrency door middel van kanalen die threads toestaan om te communiceren door gegevens te verzenden in plaats van geheugen te delen. De standaardbibliotheek van Rust biedt MPSC-kanalen (Multiple Producer Single Consumer), waarbij meerdere threads berichten naar een enkele ontvangende thread kunnen sturen. Dit patroon elimineert veel synchronisatieproblemen door gedeelde muteerbare toestand volledig te vermijden en in plaats daarvan te vertrouwen op berichtuitwisseling voor coördinatie.


### Gedeelde toestand met Mutex en Arc


Wanneer het doorgeven van berichten niet geschikt is, biedt Rust traditionele gedeelde toestandsconcurrency door middel van Mutex (wederzijdse uitsluiting) gecombineerd met Arc (Atomic Reference Counter). Mutex zorgt ervoor dat slechts één thread tegelijkertijd beschermde gegevens kan benaderen door te eisen dat threads een lock verkrijgen voordat ze de gegevens benaderen. Het slot wordt automatisch vrijgegeven als het bewakingsobject dat wordt teruggegeven door de slotoperatie buiten bereik raakt, waardoor veelvoorkomende deadlockscenario's door vergeten unlocks worden voorkomen.


Arc dient als het thread-veilige equivalent van RC, waarbij atomaire operaties worden gebruikt om de referentietelling veilig over meerdere threads te beheren. Hoewel RC perfect werkt voor single-threaded scenario's, creëert de niet-atomaire referentietelling race conditions wanneer het benaderd wordt vanuit meerdere threads. Arc's atomaire tellers zorgen ervoor dat wijzigingen in de referentietelling veilig gebeuren, zelfs bij gelijktijdige toegang, waardoor het geschikt is voor het delen van gegevens over de grenzen van threads heen.


De combinatie van Arc en Mutex creëert een patroon voor gedeelde muteerbare toestand in gelijktijdige programma's. Door een Mutex in een Arc te wikkelen, kun je de Arc klonen om toegang tot dezelfde mutex te verdelen over meerdere threads, waarbij elke thread het lock kan verkrijgen en de beschermde data veilig kan wijzigen. Dit patroon biedt de flexibiliteit van gedeelde toestand met behoud van Rust's veiligheidsgaranties door middel van compileertijd verificatie en runtime vergrendeling.


De eigenschappen Send en Sync werken achter de schermen om threadveiligheid tijdens het compileren te garanderen. Send geeft aan dat een type veilig overgedragen kan worden aan een andere thread, terwijl Sync aangeeft dat verwijzingen naar een type veilig gedeeld kunnen worden tussen threads. De meeste types implementeren deze eigenschappen automatisch als hun componenten thread-veilig zijn, maar sommige types zoals RC en RefCell implementeren ze expliciet niet omdat ze niet ontworpen zijn voor gelijktijdige toegang. Deze automatische implementatie van eigenschappen voorkomt het per ongeluk introduceren van schendingen van de thread-veiligheid, terwijl veilige types naadloos kunnen werken in gelijktijdige contexten.


## Rust macro's begrijpen

<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>


:::video id=5e96914d-df02-4781-ae54-b06008952301:::

### Inleiding tot macro's in Rust


Macro's in Rust zijn een metaprogrammeerfunctie waarmee ontwikkelaars code kunnen schrijven die andere code genereert tijdens het compileren. In tegenstelling tot functies, die tijdens runtime worden aangeroepen, worden macro's vroeg in het compilatieproces uitgebreid, voor typecontrole en latere stadia. Dit fundamentele onderscheid maakt macro's bijzonder nuttig voor het verminderen van codeherhaling en het creëren van domeinspecifieke talen binnen Rust programma's.


De meest herkenbare indicator van een macro-oproep is het uitroepteken (!) dat volgt op de macronaam. Als je bijvoorbeeld `println!("Hallo, wereld!")` gebruikt, roep je geen functie aan maar een macro. Deze macro breidt zich uit tot complexere code die de opmaak- en uitvoerbewerkingen afhandelt. Het uitroepteken dient als een visueel teken voor ontwikkelaars dat er compileertijd code wordt gegenereerd in plaats van een standaard functie-aanroep.


Rust biedt drie verschillende typen macro's, die elk een ander doel dienen in het ecosysteem van de taal:



- Functie-achtige macro's**: Lijken op functie-aanroepen maar werken tijdens het compileren (bijv. `vec!`, `println!`)
- Macro's afleiden**: Automatisch eigenschappen implementeren voor types (bijv. `#[derive(Debug, Clone)]`)
- Attribuut-achtige macro's**: Wijzig het gedrag van code-elementen waarop ze worden toegepast (bijv. `#[test]`, `#[tokio::main]`)


Inzicht in deze verschillende macro-types is essentieel voor effectief programmeren met Rust, omdat ze elk gericht zijn op specifieke gebruikssituaties en programmeerpatronen.


### Soorten macro's en hun toepassingen


Functieachtige macro's zijn de meest voorkomende macro's in Rust programmering. Deze macro's gebruiken een syntaxis die lijkt op die van functie-aanroepen, maar voeren patroonherkenning uit op hun invoer om generate geschikte code te maken. De `vec!` macro is een veelvoorkomend voorbeeld van deze categorie, waarmee ontwikkelaars vectoren kunnen maken en initialiseren met een beknopte syntaxis. Wanneer je `vec![1, 2, 3, 4]` schrijft, zet de macro dit om in code die een nieuwe vector maakt, elk element afzonderlijk duwt en de voltooide vector teruggeeft.


Derive macro's bieden automatische trait-implementaties voor aangepaste types, wat boilerplate-code aanzienlijk vermindert. Wanneer je `#[derive(Debug)]` toevoegt aan een struct of enum definitie, geef je de compiler opdracht om generate een complete implementatie van de Debug eigenschap voor dat type te genereren. Deze gegenereerde implementatie behandelt de opmaaklogica die nodig is om de inhoud van het type weer te geven in een menselijk leesbaar formaat. Het derive mechanisme ondersteunt vele standaard bibliotheek eigenschappen, inclusief Clone, PartialEq, waardoor het een veelgebruikt hulpmiddel is om boilerplate te reduceren.


Attribuut-achtige macro's wijzigen het gedrag van de code-elementen die ze annoteren en bieden een manier om metadata toe te voegen of compilatiegedrag te wijzigen. Deze macro's verschijnen als attributen boven typedefinities, functies of andere codeconstructies. Bijvoorbeeld, het `#[non_exhaustive]` attribuut op een enum geeft aan dat extra varianten kunnen worden toegevoegd in toekomstige versies, waardoor match expressies een standaard geval moeten bevatten. Dit mechanisme verzekert voorwaartse compatibiliteit terwijl het duidelijke documentatie verschaft over het evolutiepotentieel van het type.


### Aangepaste functie-achtige macro's maken


Voor het schrijven van aangepaste functie-achtige macro's moet je Rust's syntaxis voor het matchen van patronen voor macrodefinities begrijpen. De macrodefinitie gebruikt een declaratieve benadering waarbij je patronen specificeert die overeenkomen met verschillende invoervormen en bijbehorende sjablonen voor het genereren van code. Elke macro kan meerdere takken bevatten, zodat hij verschillende invoerpatronen kan verwerken en generate voor elk geval de juiste code kan genereren.


Overweeg om een aangepaste vectormacro te maken die de basisprincipes van macroconstructie demonstreert. De macrodefinitie begint met `macro_rules!` gevolgd door de macronaam en een reeks pattern-matching vertakkingen. Elke vertakking bestaat uit een patroon dat overeenkomt met specifieke invoersyntaxis en een codesjabloon dat de overeenkomstige Rust code genereert. Een eenvoudige vertakking kan bijvoorbeeld overeenkomen met lege haakjes `[]` en generate code om een lege vector te maken, terwijl een andere vertakking overeenkomt met een enkele uitdrukking en code genereert om een vector met één element te maken.


Macro's zijn vooral handig bij het implementeren van variabele argumentpatronen met herhalingssyntaxis. Het patroon `$($x:expr),*` komt overeen met nul of meer uitdrukkingen gescheiden door komma's, waardoor de macro een willekeurig aantal argumenten kan verwerken. De overeenkomstige codegeneratiesjabloon gebruikt `$(vec.push($x);)*` om alle gematchte uitdrukkingen te doorlopen en generate individuele push-instructies voor elk ervan. Dit herhalingsmechanisme stelt macro's in staat om generate code te genereren die onmogelijk of extreem langdradig zou zijn om handmatig te schrijven.


```rust
// A macro to create a HashMap with Bitcoin-related data
macro_rules! btc_map {
// Empty case
() => {
std::collections::HashMap::new()
};
// Key-value pairs case
($($key:expr => $value:expr),+ $(,)?) => {
{
let mut map = std::collections::HashMap::new();
$(
map.insert($key, $value);
)+
map
}
};
}

// A macro for logging with context (simulating a derive-like pattern)
macro_rules! log_payment {
($level:ident, $($arg:tt)*) => {
println!(
"[{}] [PAYMENT] {}",
stringify!($level).to_uppercase(),
format!($($arg)*)
)
};
}

fn main() {
// Using the btc_map! macro
let fee_rates = btc_map! {
"high_priority" => 50_u64,    // sats/vbyte
"medium" => 25_u64,
"low" => 10_u64,
};

println!("Fee rates: {:?}", fee_rates);

// Using the log_payment! macro
log_payment!(info, "Sending {} sats to {}", 100_000, "bc1q...");
log_payment!(warn, "Fee rate {} sats/vB is above average", 75);
log_payment!(error, "Payment failed: insufficient funds");

// Standard vec! macro usage comparison
let utxos = vec![50_000_u64, 30_000, 20_000];
let total: u64 = utxos.iter().sum();
println!("Total UTXOs: {} sats", total);
}
```


Het compilatieproces zet macro-aanroepen om in uitgebreide code voordat typecontrole en optimalisatie plaatsvinden. Wanneer de compiler een macro-oproep tegenkomt, vergelijkt hij de invoer met de gedefinieerde patronen en vervangt hij de macro-oproep door de gegenereerde code. Deze uitgebreide code ondergaat dan de normale compilatieprocessen, inclusief typecontrole en optimalisatie. Hulpmiddelen zoals `cargo expand` stellen ontwikkelaars in staat om de gegenereerde code te inspecteren, wat waardevolle debugmogelijkheden biedt bij het ontwikkelen van complexe macro's.


### Geavanceerde macroconcepten en debuggen


Macro-ontwikkeling vereist begrip van het onderscheid tussen compileer- en runtime-uitvoering. Macro's worden uitgevoerd tijdens het compileren en genereren code die tijdens runtime wordt uitgevoerd. Deze temporele scheiding betekent dat macro logica niet afhankelijk kan zijn van runtime waarden, maar het maakt ook optimalisaties mogelijk waarbij complexe berekeningen eenmalig uitgevoerd kunnen worden tijdens compilatie in plaats van herhaaldelijk tijdens uitvoering.


Het patroonherkenningssysteem in macro's ondersteunt verschillende fragmentspecificaties die bepalen welk soort code-elementen gematcht kunnen worden. De `expr` specificatie komt overeen met expressies, `ty` komt overeen met types, `ident` komt overeen met identifiers, en verschillende andere geven fijnkorrelige controle over de validatie van invoer. Deze specifiers zorgen ervoor dat macro's syntactisch geldige invoer ontvangen en geven duidelijke foutmeldingen wanneer ongeldige syntaxis wordt aangetroffen.


Het debuggen van macro's brengt unieke uitdagingen met zich mee vanwege hun compileertijdkarakter. Het `cargo expand` commando is nuttig voor macro-ontwikkeling, omdat het de volledig geëxpandeerde code toont die door macro-aanroepen wordt gegenereerd. Met dit gereedschap kunnen ontwikkelaars controleren of hun macro's generate de bedoelde code opleveren en problemen in de expansielogica identificeren. Wanneer de macro gegenereerde code fouten bevat, helpt de uitgebreide uitvoer om te bepalen of het probleem in de macrodefinitie of in de gegenereerde codestructuur zit.


Complexe macro's kunnen recursieve patronen implementeren, waarbij een macro zichzelf aanroept met gewijzigde argumenten om geneste of iteratieve code te genereren. Recursieve macro's moeten echter zorgvuldig ontworpen worden om oneindige uitbreiding en problemen met de compilatieprestaties te voorkomen. De compileertijd aard van macro-expansie betekent dat zelfs inefficiënte macro-implementaties alleen de compilatiesnelheid beïnvloeden, niet de runtime prestaties, maar te complexe macro's kunnen het bouwproces aanzienlijk vertragen.



# Rust & Bitcoin

<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>


## Waarom Rust voor Bitcoin ontwikkeling

<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>


:::video id=f59c4951-e109-4c70-b7da-41721e50ab04:::


De keuze van Rust voor de ontwikkeling van Bitcoin en Lightning is niet toevallig. De ontwikkeling van Bitcoin brengt unieke verantwoordelijkheden met zich mee die het onderscheiden van typische softwareontwikkeling. Wanneer ze met Bitcoin werken, gaan ontwikkelaars vaak om met gebruikersfondsen in een omgeving waar fouten onomkeerbaar kunnen zijn. In tegenstelling tot traditionele financiële systemen met wettelijke bescherming en terugboekingsmechanismen, betekent de gedecentraliseerde aard van Bitcoin dat als een transactie eenmaal is uitgezonden, er geen autoriteit is waartoe men zich kan wenden om fondsen terug te krijgen. Deze realiteit vereist een hoger niveau van verantwoordelijkheid en precisie in softwareontwikkeling.


De "move fast and break things" filosofie die in veel technologiesectoren werkt, is simpelweg niet van toepassing op Bitcoin ontwikkeling. In plaats daarvan heeft het ecosysteem talen en gereedschappen nodig die ontwikkelaars helpen robuuste, veilige software te maken, waarbij fouten worden voorkomen of netjes worden afgehandeld. Dit is de reden waarom veel prominente Bitcoin projecten zich hebben gericht op Rust, waaronder de Bitcoin Development Kit (BDK), Lightning Development Kit (LDK) en BreezSDK.


Rust biedt drie essentiële eigenschappen die het bijzonder geschikt maken voor Bitcoin ontwikkeling: een statisch sterk typesysteem, rijke moderne tooling en cross-platform compatibiliteit. Elk van deze eigenschappen draagt bij aan het vermogen van de taal om ontwikkelaars te helpen veiligere, betrouwbaardere code te schrijven voor het afhandelen van cryptocurrency operaties.


### Rust's statisch sterk type systeem


Rust's typesysteem biedt zowel statische als sterke typekenmerken die samenwerken om fouten op te vangen voordat gebruikers er last van hebben. De statische aard betekent dat typecontrole plaatsvindt tijdens het compileren, waardoor ontwikkelaars typefouten moeten oplossen nog voordat het programma gebouwd kan worden. Dit in tegenstelling tot dynamisch getypeerde talen waar typefouten pas tijdens runtime aan de oppervlakte komen, mogelijk nadat de software is uitgerold en echte gebruikersgelden verwerkt.


De kracht van het typesysteem van Rust verwijst naar de expressiviteit en nauwkeurigheid bij het modelleren van problemen. In tegenstelling tot talen met zwakkere typesystemen zoals C, waar ontwikkelaars beperkt zijn tot basistypes zoals getallen en structs, staat Rust een rijke typemodellering toe die complexe domeinconcepten accuraat kan weergeven. Je kunt bijvoorbeeld types maken die onderscheid maken tussen verschillende soorten lijsten of afdwingen dat bepaalde bewerkingen alleen worden uitgevoerd op specifieke objecttypes.


Wat het type-systeem van Rust relevant maakt voor de ontwikkeling van Bitcoin is de benadering van geheugenveiligheid. Hetzelfde type systeem dat bedrijfslogica modelleert, regelt ook geheugeneigendom en gedeelde toegangscontrole. Deze dubbele verantwoordelijkheid betekent dat veelvoorkomende klassen van kwetsbaarheden, zoals geheugenlekken, dubbelvrije fouten en "race conditions", volledig worden geëlimineerd door de compiler. Het typesysteem dwingt deze veiligheidsgaranties af door concepten als eigendom, lenen en referentietelling, waardoor het extreem moeilijk wordt om geheugengerelateerde bugs te introduceren die de veiligheid of stabiliteit in gevaar kunnen brengen.


```rust
// Example: Type-safe Bitcoin amount handling
// Using newtypes to prevent mixing up satoshis and other values

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct Satoshis(u64);

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct FeeRate(u64); // sats per vbyte

impl Satoshis {
fn from_btc(btc: f64) -> Self {
Satoshis((btc * 100_000_000.0) as u64)
}

fn as_btc(&self) -> f64 {
self.0 as f64 / 100_000_000.0
}
}

// Calculate fee given tx size - type system ensures we can't mix up values
fn calculate_fee(tx_size_vbytes: u32, rate: FeeRate) -> Satoshis {
Satoshis(tx_size_vbytes as u64 * rate.0)
}

fn main() {
let payment = Satoshis::from_btc(0.001); // 100,000 sats
let fee_rate = FeeRate(25);              // 25 sats/vbyte
let tx_size = 250_u32;                   // vbytes

let fee = calculate_fee(tx_size, fee_rate);
println!("Payment: {:?} ({} BTC)", payment, payment.as_btc());
println!("Fee: {:?}", fee);

// This would NOT compile - type safety prevents mixing values:
// let bad_fee = calculate_fee(tx_size, payment); // ERROR: expected FeeRate, found Satoshis
}
```


### Moderne tools en platformoverschrijdende ondersteuning


Het tooling ecosysteem van Rust voorziet ontwikkelaars van gereedschappen die helpen bij de productiviteit en de kwaliteit van de code. De Rust compiler zelf is niet alleen ontworpen om code te vertalen naar binaire vorm, maar om te dienen als een educatief hulpmiddel dat ontwikkelaars helpt te leren en te verbeteren. Wanneer er compilatiefouten optreden, geeft de compiler gedetailleerde uitleg over wat er fout ging en stelt vaak specifieke oplossingen voor. Deze aanpak is vooral waardevol voor ontwikkelaars die nieuw zijn met Rust, omdat de compiler effectief goede praktijken aanleert en veelgemaakte fouten helpt voorkomen.


De taal bevat Cargo, een verenigde pakketbeheerder die zorgt voor het beheer van afhankelijkheden, bouwen, testen en het genereren van documentatie. Deze standaardisatie elimineert de fragmentatie die te zien is in oudere talen zoals C++, waar meerdere concurrerende tools zorgen voor inconsistentie tussen projecten. Cargo ondersteunt ook extensies zoals rustfmt voor codeopmaak en Clippy voor statische analyse, waardoor code consistente stijlrichtlijnen volgt en potentiële problemen worden opgespoord voordat het problemen worden.


Rust's cross-platform mogelijkheden gaan verder dan traditionele besturingssystemen en omvatten mobiele platformen zoals Android en iOS, evenals WebAssembly voor browsergebaseerde toepassingen. Deze platformoverschrijdende ondersteuning is handig voor Bitcoin-toepassingen die in verschillende omgevingen moeten draaien. Bijvoorbeeld, projecten zoals Mutiny Wallet maken gebruik van Rust's WebAssembly compilatie om Lightning wallets te maken die direct in webbrowsers draaien, iets wat onpraktisch zou zijn met traditionele webtechnologieën alleen.


### Fouttypes en hun gevolgen begrijpen


Effectieve foutafhandeling begint met het begrijpen van de verschillende categorieën fouten die kunnen optreden tijdens het uitvoeren van programma's. Neem een eenvoudige routeringstoepassing die paden tussen geografische punten berekent. Dit voorbeeld illustreert drie fundamentele soorten fouten die ontwikkelaars moeten aanpakken: ongeldige invoerfouten, runtime resource fouten en logische fouten.


Ongeldige invoerfouten treden op wanneer een functie parameters ontvangt die niet aan de vereisten voldoen. Als een geografisch coördinatenstelsel bijvoorbeeld gehele getallen voor lengtegraad gebruikt, maar een negatieve waarde ontvangt waar alleen positieve waarden geldig zijn, kan de functie niet zinvol verder gaan. Deze fouten vertegenwoordigen een contractbreuk tussen de aanroeper en de functie, en de gepaste reactie is meestal om de invoer te weigeren en een foutindicatie terug te geven.


Runtime resource fouten treden op wanneer externe afhankelijkheden niet beschikbaar of ontoegankelijk zijn. Het lezen van een mapbestand kan mislukken omdat het bestand niet bestaat, de applicatie niet de juiste rechten heeft of het opslagapparaat niet beschikbaar is. Deze fouten zijn extern aan de programmalogica en vereisen vaak eerder oplossingen in de omgeving dan wijzigingen in de code. Robuuste applicaties moeten echter anticiperen op deze scenario's en ze netjes afhandelen.


Logische fouten zijn fouten in de programma-implementatie of misverstanden over hoe componenten op elkaar inwerken. Als een routeringsalgoritme een leeg pad retourneert wanneer er geldige begin- en eindpunten worden gegeven, duidt dit op een logische fout die in de code zelf moet worden gecorrigeerd. In tegenstelling tot de andere fouttypes, vereisen logische fouten meestal debugging en aanpassing van de code om ze op te lossen.


### Strategieën voor robuust foutenbeheer


Het bouwen van betrouwbare software vereist proactieve strategieën die de kans op fouten minimaliseren en onvermijdelijke fouten netjes afhandelen. De eerste strategie bestaat uit het beperken van mogelijke fouten door zorgvuldig typeontwerp. Door typen te kiezen die alleen geldige waarden kunnen vertegenwoordigen, kunnen ontwikkelaars hele klassen van ongeldige invoerfouten elimineren. Bijvoorbeeld, het gebruik van unsigned integers voor waarden die niet negatief kunnen zijn voorkomt negatieve waarde fouten tijdens het compileren.


Asserties bieden een extra beschermingslaag door expliciet te controleren of verwachte condities waar zijn tijdens het uitvoeren van een programma. Deze controles dienen meerdere doelen: ze vangen bugs tijdens het testen, zorgen ervoor dat programma's vroegtijdig falen als er problemen optreden (wat debuggen makkelijker maakt) en dienen als uitvoerbare documentatie die de aannames van de programmeur beschrijft. Wanneer een assertie faalt, geeft dit aan dat een fundamentele aanname over de toestand van het programma is geschonden, meestal wijzend op een logische fout die onderzocht moet worden.


Het principe van gelaagde abstracties helpt bij het beheren van complexiteit door ervoor te zorgen dat fouten op de juiste niveaus van het systeem worden afgehandeld. Interne implementatiedetails, inclusief specifieke fouttypes uit bibliotheken op een lager niveau, mogen zich niet verder verspreiden dan de grenzen van het subsysteem. In plaats daarvan moet elke laag fouten vertalen in termen die zinvol zijn op dat abstractieniveau. Een wallet-toepassing die een Bitcoin-bibliotheek gebruikt, moet bijvoorbeeld fouten bij het parsen van descriptors op laag niveau vertalen in berichten op hoger niveau, zoals "ongeldige wallet-configuratie", die bruikbare informatie geven aan gebruikers of aanroepende code.


Deze benadering van foutafhandeling, gecombineerd met Rust's typesysteem en tooling, helpt potentiële problemen vroeg in het ontwikkelproces op te sporen, voordat ze gebruikers kunnen beïnvloeden of de veiligheid van Bitcoin-toepassingen in gevaar kunnen brengen.



## Fout model

<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>


:::video id=9fac0184-8443-4c36-8afd-8acb21fb43c3:::

Rust biedt een uitgebreide benadering van foutafhandeling die veiligheid in evenwicht brengt met bruikbaarheid. Terwijl de algemene foutmodelconcepten van toepassing zijn op alle programmeertalen, biedt Rust specifieke hulpmiddelen en patronen die foutafhandeling zowel expliciet als beheersbaar maken. Inzicht in deze mechanismen is cruciaal voor het schrijven van robuuste Rust toepassingen die onverwachte situaties netjes kunnen afhandelen met behoud van prestaties en veiligheid.


### Paniek en het juiste gebruik ervan


Rust's panic mechanisme is de meest directe manier om onherstelbare fouten af te handelen. Wanneer je de `panic!` macro aanroept, stopt het programma onmiddellijk met uitvoeren, afbreken of afwikkelen, afhankelijk van je configuratie. De panic macro accepteert een bericht dat beschrijft wat er fout ging, wat context biedt voor debuggen. Daarnaast dienen methodes als `unwrap()` en `expect()` op Result en Option types als snelkoppelingen naar panic wanneer deze types respectievelijk foutwaarden of geen waarden bevatten. De `expect()` methode staat je toe om een aangepaste boodschap te geven, waardoor het iets informatiever is dan `unwrap()` bij het debuggen van fouten.


Ondanks de eenvoud moet panic verstandig worden gebruikt in productiecode. Er zijn verschillende scenario's waarbij panic niet alleen acceptabel is, maar ook wordt aanbevolen. Bij het schrijven van voorbeelden of prototypes biedt panic een schone manier om te focussen op de kernfunctionaliteit zonder de code te vervuilen met uitgebreide foutafhandeling. In testomgevingen is panic vaak het gewenste gedrag wanneer asserties falen, omdat het duidelijk aangeeft dat er iets onverwachts is gebeurd. De Rust gemeenschap erkent ook situaties waarin ontwikkelaars meer kennis hebben dan de compiler, zoals bij het parsen van hard-gecodeerde IP-adressen waarvan bekend is dat ze geldig zijn.


De schijnveiligheid van "compiler-geverifieerde" panics kan echter misleidend zijn. Beschouw een scenario waarbij je een IP adres hard-codeert en `expect()` gebruikt omdat je weet dat het geldig is. Na verloop van tijd, als code evolueert, kan die hard gecodeerde waarde worden gerefactored in een constante, en later kan die constante worden veranderd in iets als "localhost" voor een betere gebruikerservaring. Plotseling wordt je "veilige" paniek een runtime fout. Deze evolutie laat zien waarom het over het algemeen beter is om paniek te vermijden in productiecode en in plaats daarvan de juiste fouttypes terug te geven die netjes afgehandeld kunnen worden.


Een opmerkelijke uitzondering op de "vermijd paniek" regel betreft mutex operaties. Als je `lock()` aanroept op een mutex, retourneert het een Resultaat omdat het slot kan mislukken als een andere thread in paniek raakt terwijl hij de mutex vasthoudt. Dit creëert een verwarrende situatie waarbij je lokale code een foutmelding krijgt voor iets dat in een compleet andere context gebeurde. Aangezien je redelijkerwijs geen fout kunt afhandelen die afkomstig is van een panic van een andere thread, vinden veel ontwikkelaars het acceptabel om mutex locks uit te pakken, vooral als je elders een panic-vrije codebase onderhoudt.


### Werken met resultaat- en optietypes


Het type Result vormt de ruggengraat van Rust's systeem voor foutafhandeling. Als een enum dat een `Ok(value)` of een `Err(error)` kan bevatten, dwingt Result je expliciet te erkennen dat operaties kunnen mislukken. Het Option type dient een soortgelijk doel voor gevallen waar een waarde simpelweg afwezig kan zijn, door `Some(value)` of `None` te bevatten. Hoewel Option geen gedetailleerde foutinformatie geeft, is het perfect voor situaties waarin de afwezigheid van een waarde zinvol en verwacht is.


Zowel Result als Option bieden verschillende hulpprogramma's die de afhandeling van fouten ergonomischer maken. De `unwrap_or()` methode retourneert de ingesloten waarde als deze aanwezig is, of een standaardwaarde als er een fout is of geen. Dit patroon is vooral nuttig als je een redelijke fallback hebt, zoals het parsen van gebruikersinvoer met een zinvolle standaardwaarde als het parsen mislukt. De `unwrap_or_default()` methode werkt op dezelfde manier, maar gebruikt de standaardwaarde van het type in plaats van dat je er een moet specificeren. Hoewel deze methoden technisch gezien geen fouten afhandelen in de traditionele zin, bieden ze een manier om de functionaliteit sierlijk te degraderen wanneer er problemen optreden.


De vraagteken operator (`?`) is een beknopte syntaxis voor foutvoortplanting. Wanneer het wordt toegepast op een Resultaat of Optie, haalt het de succeswaarde eruit als deze aanwezig is, of retourneert het onmiddellijk de fout van de huidige functie als er een probleem is. Deze operator elimineert de verbose foutcontrolepatronen die gebruikelijk zijn in talen als Go, waar je handmatig fouten moet controleren en retourneren bij elke stap. De vraagteken operator biedt in wezen syntactische suiker voor vroege teruggaven, waardoor je schone, lineaire code kunt schrijven die zich richt op het gelukkige pad terwijl het automatisch de foutvoortplanting afhandelt.


### Patronen voor geavanceerde foutafhandeling


De `map()` methode op Resultaat en Optie types maakt een functionele foutafhandeling mogelijk die code expressiever en beter componeerbaar kan maken. Wanneer je `map()` aanroept op een Resultaat, wordt de geleverde functie toegepast op de succeswaarde indien aanwezig, terwijl fouten automatisch worden doorgegeven zonder wijziging. Dit patroon is handig bij het chainen van bewerkingen, omdat je je kunt richten op het transformeren van waarden zonder herhaaldelijk foutgevallen te behandelen. De `map_err()` methode biedt de omgekeerde functionaliteit, waardoor je fouttypes kunt transformeren terwijl succeswaarden ongewijzigd blijven.


Fouttransformatie wordt cruciaal bij het bouwen van gelaagde applicaties waarbij verschillende componenten verschillende fouttypes nodig hebben. Neem een functie die gebruikersinvoer parseert en die low-level parsingfouten moet omzetten in domeinspecifieke fouten. Met behulp van `map_err()` kunt u eenvoudig een algemene "ongeldig getal formaat" fout vertalen naar een meer contextuele "ongeldige leeftijd" fout die zinvol is binnen het domein van uw applicatie. Deze transformatie vindt plaats op het punt waar de fout optreedt, waardoor de code beter leesbaar en onderhoudbaarder is dan traditionele try-catch blokken waar foutafhandeling wordt gescheiden van de bewerkingen die kunnen mislukken.


De combinatie van de vraagteken operator met error mapping creëert beknopte patronen voor foutafhandeling. U kunt bewerkingen aan elkaar koppelen, fouten waar nodig transformeren en ze voortplanten in de aanroepstapel met minimale boilerplate. Deze aanpak houdt foutafhandeling dicht bij de bewerkingen die kunnen falen, terwijl er een duidelijke scheiding blijft tussen succes- en foutpaden.


```rust
use std::fmt;

// Layered error types for a wallet application
#[derive(Debug)]
enum NetworkError {
ConnectionFailed(String),
Timeout,
}

#[derive(Debug)]
enum WalletError {
Network(NetworkError),
InvalidAddress(String),
InsufficientFunds { required: u64, available: u64 },
}

// Implement Display for user-friendly messages
impl fmt::Display for WalletError {
fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
match self {
WalletError::Network(e) => write!(f, "Network error: {:?}", e),
WalletError::InvalidAddress(addr) => write!(f, "Invalid address: {}", addr),
WalletError::InsufficientFunds { required, available } =>
write!(f, "Need {} sats but only have {} available", required, available),
}
}
}

// Convert from lower-level error to domain error
impl From<NetworkError> for WalletError {
fn from(err: NetworkError) -> Self {
WalletError::Network(err)
}
}

// Simulated network call
fn fetch_balance(address: &str) -> Result<u64, NetworkError> {
if address.starts_with("bc1") {
Ok(500_000) // 500k sats
} else {
Err(NetworkError::ConnectionFailed("Invalid endpoint".into()))
}
}

// Higher-level function using ? with automatic error conversion
fn send_payment(from: &str, amount: u64) -> Result<String, WalletError> {
let balance = fetch_balance(from)?; // NetworkError auto-converts to WalletError

if balance < amount {
return Err(WalletError::InsufficientFunds {
required: amount,
available: balance,
});
}

Ok(format!("Sent {} sats", amount))
}

fn main() {
match send_payment("bc1qtest...", 100_000) {
Ok(msg) => println!("Success: {}", msg),
Err(e) => println!("Failed: {}", e), // User-friendly message
}
}
```


### Externe bibliotheken en systemen voor foutafhandeling


Het Rust ecosysteem bevat verschillende populaire bibliotheken die de mogelijkheden voor foutafhandeling van de standaardbibliotheek uitbreiden. De `anyhow` bibliotheek biedt een vereenvoudigde benadering van foutafhandeling door een universeel fouttype aan te bieden dat automatisch kan converteren van elk fouttype dat de standaard Error eigenschap implementeert. Met deze automatische conversie kunt u de vraagtekenoperator gebruiken met verschillende fouttypen zonder handmatige conversie, waardoor het bijzonder nuttig is voor toepassingen waarbij u geen programmatisch onderscheid hoeft te maken tussen verschillende fouttypen.


Hoewel `anyhow` uitblinkt in het vereenvoudigen van foutafhandeling voor toepassingen waarbij fouten voornamelijk worden weergegeven aan gebruikers, heeft het beperkingen in bibliotheekontwikkeling. Aangezien `anyhow` in wezen alle fouten omzet in tekenreeksen, kunnen gebruikers van uw bibliotheek niet eenvoudig programmatisch reageren op verschillende foutcondities. Deze beperking maakt `anyhow` meer geschikt voor eindgebruikertoepassingen dan voor bibliotheken die gestructureerde foutinformatie moeten bieden aan hun gebruikers.


Meer geavanceerde foutafhandelingsbenaderingen omvatten het maken van aangepaste fouttypes die de specifieke foutmodi van uw toepassing of bibliotheek modelleren. Een goed ontworpen foutmodel kan onderscheid maken tussen ongeldige invoer (die de aanroeper kan herstellen), runtime fouten (die opnieuw geprobeerd kunnen worden) en permanente fouten (die wijzen op bugs of onherstelbare omstandigheden). Deze gestructureerde aanpak stelt gebruikers van uw code in staat om intelligente beslissingen te nemen over hoe te reageren op verschillende soorten fouten, of dat nu het opnieuw proberen van bewerkingen betekent, gebruikers vragen om andere invoer of het rapporteren van bugs aan ontwikkelaars.


## UniFFI, Rust bibliotheken koppelen aan meerdere talen


<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>


:::video id=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::

### Inleiding tot UniFFI en platformonafhankelijke ontwikkeling


UniFFI is een hulpmiddel om Rust bibliotheken toegankelijk te maken voor meerdere programmeertalen en platformen. Deze tool, ontwikkeld door Mozilla, pakt een fundamentele uitdaging in moderne softwareontwikkeling aan: hoe de prestatie- en veiligheidsvoordelen van Rust te benutten met behoud van compatibiliteit met verschillende ontwikkelingsecosystemen. De tool genereert automatisch taalbindingen voor Rust bibliotheken, waardoor ontwikkelaars niet langer handmatig interfacecode hoeven te maken voor elke doeltaal.


Het kernprobleem dat UniFFI oplost, komt voort uit het feit dat Rust een gecompileerde taal is. Wanneer Rust code wordt gecompileerd, produceert het binaire uitvoer met een Foreign Function Interface (FFI) die een interface op laag niveau biedt die een uitdaging kan zijn om direct te gebruiken vanuit talen op hoger niveau zoals Python, Swift of Kotlin. Traditioneel zou elke bibliotheekontwikkelaar aangepaste bindingscode moeten schrijven voor elke doeltaal, wat een aanzienlijke belemmering vormt voor cross-platform toepassing. UniFFI elimineert deze redundantie door een gestandaardiseerde aanpak te bieden om deze bindingen automatisch te genereren.


De ontwerpfilosofie van de tool is erop gericht om Rust ontwikkelaars in staat te stellen om zich te concentreren op hun core business logica, terwijl hun bibliotheken toegankelijk worden gemaakt voor ontwikkelaars die in andere talen werken. Een iOS-ontwikkelaar die Swift gebruikt, kan bijvoorbeeld een Rust bibliotheek gebruiken via door UniFFI gegenereerde bindingen die een volledig native Swift interface presenteren, zonder enige indicatie dat de onderliggende implementatie in Rust is geschreven. Door deze naadloze integratie kunnen teams profiteren van de prestatievoordelen van Rust zonder dat alle teamleden Rust hoeven te leren.


### De UniFFI-architectuur en -workflow begrijpen


UniFFI werkt via een goed gedefinieerde workflow die Rust bibliotheken omzet in pakketten die compatibel zijn met meerdere talen. Het proces begint met het maken van een Unified Definition Language (UDL) bestand, dat dient als een interface specificatie die beschrijft welke delen van uw Rust bibliotheek blootgesteld moeten worden aan andere talen. Dit UDL-bestand fungeert als een contract tussen uw Rust implementatie en de gegenereerde taalbindingen.


De architectuur volgt een duidelijke scheiding van zorgen. Ontwikkelaars onderhouden hun Rust bibliotheek met standaard Rust idiomen en patronen, en maken vervolgens een apart UDL bestand dat de openbare interface in kaart brengt naar het UniFFI type systeem. De UniFFI bindingsgenerator verwerkt zowel de Rust bibliotheek als de UDL specificatie om bindingen in de moedertaal te produceren voor de gevraagde doelplatformen. Deze gegenereerde bindingen verwerken alle complexe marshaling en unmarshaling van data tussen de vreemde taal runtime en de Rust code.


Tijdens runtime creëert de architectuur een gelaagde aanpak waarbij applicatiecode geschreven in de doeltaal (zoals Kotlin voor Android) interageert met gegenereerde bindingscode die volledig native lijkt voor die taal. Deze bindingslaag zorgt voor de vertaling tussen taalspecifieke types en Rust types, beheert het geheugen veilig over de taalgrenzen heen en biedt foutafhandeling die de conventies van de doeltaal volgt. De onderliggende Rust bedrijfslogica blijft onveranderd en is zich niet bewust van de meerdere taalinterfaces die erop gebouwd zijn.


### Werken met UDL: Interface Definitie en typemapping


De Unified Definition Language vormt de hoeksteen van de functionaliteit van UniFFI en biedt een declaratieve manier om aan te geven welke delen van een Rust bibliotheek zichtbaar moeten zijn en hoe ze moeten worden gepresenteerd in doeltalen. UDL-bestanden moeten ten minste één naamruimte bevatten, die fungeert als een container voor functies die direct kunnen worden aangeroepen zonder dat objectinstantie nodig is. Deze naamruimtefuncties behandelen meestal eenvoudige bewerkingen die waarden als parameters nemen en resultaten teruggeven.


UDL ondersteunt een uitgebreide set ingebouwde types die op natuurlijke wijze overeenkomen met overeenkomstige Rust types. Basistypes zijn onder andere standaard primitieven zoals booleans, verschillende integer groottes (u8, u32, etc.), floating-point getallen en strings. Complexere types zijn onder andere vectoren, hash maps en Rust-specifieke concepten zoals Option types (weergegeven met een vraagteken syntaxis) en Result types voor foutafhandeling. Het typesysteem ondersteunt ook opsommingen, zowel eenvoudige op waarden gebaseerde opsommingen als complexe opsommingen die geassocieerde gegevens bevatten, waardoor gegevensmodellering over taalgrenzen heen mogelijk is.


Structs in Rust worden vertaald naar woordenboeken in UDL, waarbij een bijna één-op-één overeenkomst wordt behouden terwijl ze worden aangepast aan de syntaxconventies van UDL. Wanneer Rust structs geassocieerde methoden hebben, kunnen ze worden blootgesteld als interfaces in UDL, die generate als klassen met methoden in objectgeoriënteerde doeltalen zoals Kotlin of Swift. Deze mapping behoudt de objectgeoriënteerde ontwerppatronen die ontwikkelaars verwachten in deze talen, terwijl de structuur en het gedrag van de onderliggende Rust implementatie behouden blijven.


```
// Example UDL file for a Bitcoin wallet library (wallet.udl)
namespace wallet {
// Namespace functions - called directly without object
string generate_mnemonic();
Wallet create_wallet(string mnemonic);
};

// Dictionary (struct) - becomes data class in Kotlin, struct in Swift
dictionary Balance {
u64 confirmed_sats;
u64 pending_sats;
};

// Interface (class with methods) - becomes class with methods
interface Wallet {
// Constructor
constructor(string mnemonic);

// Methods
Balance get_balance();
string get_new_address();
string send_to_address(string address, u64 amount_sats);
};

// Enum with data - maps to sealed class (Kotlin) or enum with associated values (Swift)
[Enum]
interface TransactionStatus {
Pending(u32 confirmations_needed);
Confirmed(u32 block_height);
Failed(string reason);
};

// Error enum for Result types
[Error]
enum WalletError {
"InsufficientFunds",
"InvalidAddress",
"NetworkError",
};

// Function that can fail - throws in target language
interface Wallet {
[Throws=WalletError]
string send_to_address(string address, u64 amount_sats);
};
```


De overeenkomstige Rust implementatie zou deze types definiëren en het `uniffi::export` attribuut implementeren in generate bindingen voor Kotlin, Swift, Python en andere ondersteunde talen.


### Foutafhandeling en geavanceerde functies


UniFFI biedt foutafhandeling die Rust's resultaatgebaseerde foutmodel behoudt, terwijl het op de juiste manier wordt vertaald voor doeltalen. Functies die Resultaat-types in Rust retourneren, kunnen worden gemarkeerd met het "throws" sleutelwoord in UDL, waarmee wordt gespecificeerd welke fouttypes ze mogen produceren. Deze fouten moeten worden gedefinieerd als error enums in het UDL bestand en moeten Rust's standaard Error eigenschap implementeren in de onderliggende Rust code. De thiserror crate biedt een handige macro voor het implementeren van deze eigenschap, wat de boilerplate code aanzienlijk vermindert.


De vertaling van de foutafhandeling demonstreert de taalbewuste aanpak van UniFFI. In Kotlin, functies gemarkeerd als gooien in UDL generate methoden die uitzonderingen gooien volgens Java/Kotlin conventies. Python-bindingen gebruiken op dezelfde manier het uitzonderingsmodel van Python. Deze vertaling zorgt ervoor dat de foutafhandeling natuurlijk en idiomatisch aanvoelt in elke doeltaal, terwijl de semantische betekenis van de originele Rust fouttypes behouden blijft.


Callback interfaces vertegenwoordigen een andere geavanceerde eigenschap die bidirectionele communicatie tussen Rust bibliotheken en consumerende applicaties mogelijk maakt. Wanneer een Rust bibliotheek moet terugbellen naar applicatiecode, kunnen ontwikkelaars eigenschappen definiëren in Rust en deze markeren als callback interfaces in UDL. De consumerende applicatie implementeert deze interfaces in hun moedertaal en UniFFI handelt de complexe marshaling af die nodig is om deze callbacks vanuit Rust code aan te roepen. Dit patroon vereist zorgvuldige overweging van de veiligheid van threads, omdat callbacks de grenzen van threads kunnen overschrijden, waardoor Send en Sync begrenzingen aan de Rust kant nodig zijn.


### Toepassingen in de praktijk en huidige beperkingen


UniFFI is geadopteerd in de gemeenschap voor de ontwikkeling van cryptocurrency en blockchain, met grote projecten zoals BDK (Bitcoin Development Kit), LDK (Lightning Development Kit) en verschillende wallet-implementaties die het gebruiken om mobiele SDK's aan te bieden. Deze projecten demonstreren het gebruik van UniFFI in productieomgevingen.


Het bestuderen van UDL-bestanden uit de praktijk van deze projecten laat patronen en best practices zien die in de praktijk zijn ontstaan. Het UDL-bestand van BDK laat bijvoorbeeld zien hoe complexe domeinmodellen met meerdere enums, structs en interfaces effectief in kaart kunnen worden gebracht om uitgebreide mobiele SDK's te maken. De consistentie van de UDL-syntaxis in verschillende projecten betekent dat ontwikkelaars die bekend zijn met één bibliotheek die geschikt is voor UniFFI, andere snel kunnen begrijpen en ermee kunnen werken, waardoor een netwerkeffect ontstaat dat het hele ecosysteem ten goede komt.


UniFFI heeft echter opmerkelijke beperkingen waar ontwikkelaars rekening mee moeten houden. De belangrijkste is het gebrek aan ondersteuning voor asynchrone interfaces. Alle gegenereerde bindingen zijn synchroon, waardoor ontwikkelaars asynchrone operaties binnen hun Rust code moeten afhandelen en synchrone interfaces aan consumerende applicaties moeten presenteren. Daarnaast vormt de plaatsing van documentatie een uitdaging: documentatie geschreven in Rust code wordt niet overgedragen naar gegenereerde bindingen, terwijl documentatie in UDL-bestanden niet beschikbaar is voor directe Rust gebruikers van de bibliotheek. Hoewel er pogingen worden ondernomen om deze beperkingen aan te pakken door automatische parsing en generatie, blijven dit overwegingen voor huidige implementaties. Tenslotte genereert UniFFI taalbindingen, maar zorgt niet voor de platform-specifieke verpakking en distributie, waardoor ontwikkelaars de laatste stappen van het maken van distribueerbare pakketten voor elk doelplatform moeten beheren.


# LNP/BP ontwikkelen met SDK

<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>


## LN knooppunt op SDK

<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>


:::video id=94b9bee6-154e-4b9c-a8ce-5e2d9e9656a2:::

### De modulaire architectuur van LDK begrijpen


De Lightning Development Kit (LDK) benadert de implementatie van Lightning Network anders dan traditionele node-software zoals CLightning of LND. Terwijl conventionele Lightning nodes werken als complete daemon toepassingen die continu op een machine draaien, functioneert LDK als een modulaire Rust bibliotheek die primitieve componenten levert voor het bouwen van aangepaste Lightning oplossingen. Dit onderscheid in architectuur maakt LDK flexibel, zodat ontwikkelaars Lightning-functionaliteit kunnen samenstellen op manieren die voldoen aan hun specifieke projectvereisten.


De kernfilosofie achter LDK is gericht op modulariteit en aanpasbaarheid. In plaats van een monolithische oplossing te bieden, biedt LDK individuele componenten die gecombineerd, aangepast of volledig vervangen kunnen worden. Elk onderdeel wordt geleverd met standaard implementaties die direct werken, maar ontwikkelaars behouden de vrijheid om hun eigen implementaties te vervangen wanneer dat nodig is. LDK bevat bijvoorbeeld standaard implementaties voor blockchainbewaking, ondertekening van transacties en netwerkcommunicatie, maar deze kunnen allemaal worden vervangen door aangepaste oplossingen die zijn afgestemd op specifieke gebruikssituaties of omgevingen.


Dankzij dit modulaire ontwerp kan LDK functioneren op verschillende platforms en in scenario's die een uitdaging zouden vormen voor traditionele Lightning nodes. Mobiele toepassingen, webbrowsers, ingebedde apparaten en gespecialiseerde hardware kunnen allemaal gebruikmaken van de componenten van LDK op manieren die passen bij hun unieke beperkingen en vereisten. De architectuur van de bibliotheek zorgt ervoor dat ontwikkelaars Lightning-toepassingen kunnen maken zonder vast te zitten aan vooraf bepaalde operationele patronen of systeemafhankelijkheden.


### LDK-gebruiksgevallen en platformflexibiliteit


De architecturale flexibiliteit van LDK opent talrijke gebruikssituaties die veel verder reiken dan traditionele Lightning node implementaties. Mobiele wallet ontwikkeling vertegenwoordigt een van de meest aantrekkelijke toepassingen, waar LDK de creatie van niet-custodiale Lightning wallets mogelijk maakt, vergelijkbaar met Phoenix wallet. Deze mobiele implementaties kunnen de gebruikerscontrole over de private sleutels behouden terwijl ze synchroniseren met Lightning Service Providers (LSP's) wanneer ze online komen, wat naadloze ontvangst van betalingen en kanaalbeheer mogelijk maakt, zelfs met intermitterende connectiviteit.


Hardware Security Module (HSM)-integratie laat een andere krachtige gebruiksmogelijkheid voor LDK zien. Door alleen de componenten voor het ondertekenen en verifiëren van transacties te verwijderen, kunnen ontwikkelaars Lightning-bewuste ondertekeningsapparaten maken die de context en implicaties van Lightning-transacties begrijpen. Deze mogelijkheid gaat verder dan alleen het ondertekenen van transacties en omvat ook intelligente analyses van het doorsturen van betalingen, kanaalbewerkingen en beveiligingskritieke beslissingen. De HSM kan evalueren of een transactie een legitieme betaling, een routeringsbewerking of een potentieel kwaadwillige poging vertegenwoordigt, waardoor gebruikers zinvolle beveiligingsinzichten krijgen.


Webgebaseerde Lightning-toepassingen profiteren aanzienlijk van de systeemaanroepvrije ontwerpfilosofie van LDK. Aangezien WebAssembly-omgevingen geen directe toegang hebben tot systeembronnen zoals bestandssystemen, netwerksockets of entropiebronnen, zorgt de zuivere aanpak van LDK ervoor dat Lightning-functionaliteit naadloos werkt in browseromgevingen. Ontwikkelaars kunnen aangepaste netwerklagen implementeren met behulp van WebSockets en browsercompatibele persistentie- en randomness-bronnen bieden met behoud van volledige naleving van het Lightning-protocol.


### Kerncomponenten en gebeurtenisgestuurde architectuur


De interne architectuur van LDK draait om verschillende belangrijke componenten die samenwerken via een gebeurtenisgestuurd systeem. Het peer management systeem handelt alle communicatie met andere Lightning nodes af, implementeert het noise protocol voor encryptie en beheert berichtstructuren voor naleving van het Lightning protocol. Deze component werkt onafhankelijk van het onderliggende transportmechanisme, waardoor ontwikkelaars netwerken kunnen implementeren via TCP sockets, WebSockets, USB seriële verbindingen of elk ander bidirectioneel communicatiekanaal.


De kanaalmanager dient als centrale coördinator voor Lightning-kanaaloperaties en werkt nauw samen met de peermanager om kanaalopenings-, -sluitings- en -betalingsoperaties uit te voeren. Wanneer een ontwikkelaar een kanaal opent, creëert de kanaalbeheerder de nodige protocolberichten en coördineert hij met de peer manager om het onderhandelingsproces in meerdere stappen af te handelen. Deze scheiding van zorgen zorgt voor een zuivere abstractie tussen Lightning protocollogica en netwerkcommunicatiedetails.


Het event-systeem van LDK biedt asynchrone meldingen voor alle belangrijke operaties en statuswijzigingen. Gebeurtenissen omvatten het volledige spectrum van Lightning-operaties, van peerverbindingen en -verbrekingen tot betalingssuccessen en -mislukkingen, kanaalstatuswijzigingen en blockchainbevestigingen. Deze gebeurtenisgestuurde aanpak stelt applicaties in staat om op de juiste manier te reageren op de activiteit van het Lightning-netwerk, met behoud van een duidelijke scheiding tussen de kernfunctionaliteit van LDK en applicatiespecifieke logica. Ontwikkelaars kunnen aangepaste event-handlers implementeren die gebruikersinterfaces bijwerken, meldingen triggeren of vervolgacties initiëren op basis van Lightning-netwerkgebeurtenissen.


### Blockchain Integratie en gegevensbeheer


Blockchain gegevensintegratie vertegenwoordigt een van de abstractielagen van LDK, ontworpen om alles van volledige Bitcoin knooppunten tot lichtgewicht mobiele clients aan te kunnen. LDK ondersteunt twee primaire modi van blockchaininteractie, elk geoptimaliseerd voor verschillende resourcebeperkingen en operationele vereisten. De volledige blokmodus stelt applicaties met toegang tot volledige blockchaingegevens in staat om volledige blokken door te geven aan LDK, waardoor uitgebreide transactiemonitoring en onmiddellijke reacties op relevante blockchaingebeurtenissen mogelijk zijn.


Voor omgevingen met beperkte middelen biedt LDK een op filtering gebaseerde aanpak die de bandbreedte en opslagvereisten vermindert. In deze modus communiceert LDK zijn bewakingsbelangen via abstracte interfaces, waarbij om bewaking van specifieke transactie-ID's, UTXO's of scriptpatronen wordt gevraagd. De toepassingslaag kan deze bewaking dan implementeren met behulp van Electrum servers, block explorers of andere lichtgewicht blockchain databronnen. Deze aanpak stelt mobiele wallets en webapplicaties in staat om Lightning functionaliteit te behouden zonder volledige blockchain synchronisatie.


De persistentielaag in LDK volgt dezelfde abstractieprincipes en voorziet applicaties van binaire gegevensblobs die betrouwbaar moeten worden opgeslagen en opgehaald. LDK handelt alle complexiteit af van het serialiseren en deserialiseren van Lightning kanaaltoestanden, netwerk roddelgegevens en andere kritieke informatie. Toepassingen hoeven alleen maar betrouwbare opslagmechanismen te implementeren, of ze nu lokale bestandssystemen, cloudopslagdiensten of gespecialiseerde databasesystemen gebruiken. Dit ontwerp zorgt ervoor dat het beheer van de Lightning-toestanden robuust blijft, terwijl toepassingen opslagoplossingen kunnen kiezen die overeenkomen met hun operationele vereisten en beveiligingsmodellen.


### Geavanceerde functies en integratiepatronen


De mogelijkheden van LDK strekken zich uit tot Lightning Network-functies zoals multi-path betalingen, routeoptimalisatie en netwerk roddelbeheer. Het routeringssysteem behoudt een uitgebreid overzicht van de Lightning Network topologie door deelname aan het roddelprotocol, waardoor intelligente padbepaling voor betalingen mogelijk is. Toepassingen kunnen de routeringsbeslissingen beïnvloeden via configuratieparameters en kunnen zelfs aangepaste routeringslogica implementeren voor gespecialiseerde toepassingen.


Het taalbindingssysteem van de bibliotheek maakt LDK-integratie in meerdere programmeeromgevingen mogelijk en ondersteunt Java, Kotlin, Swift, TypeScript, JavaScript en C++. Dankzij deze platformonafhankelijke compatibiliteit kunnen mobiele toepassingen die zijn geschreven in native talen de Lightning-functionaliteit integreren met behoud van optimale prestatiekenmerken. Het bindsysteem behoudt de event-driven architectuur en het modulaire ontwerp van LDK in alle ondersteunde talen, waardoor ontwikkelaars verzekerd zijn van consistente ervaringen, ongeacht het doelplatform.


Het schatten van vergoedingen en het uitzenden van transacties zijn andere gebieden waarop LDK flexibiliteit biedt. Toepassingen kunnen aangepaste strategieën voor het schatten van vergoedingen implementeren die rekening houden met hun specifieke operationele patronen en gebruikerseisen. Ook het uitzenden van transacties kan worden aangepast om te werken met verschillende Bitcoin netwerkinterfaces, van directe full node verbindingen tot uitzenddiensten van derden. Deze flexibiliteit zorgt ervoor dat LDK-gebaseerde applicaties hun blockchaininteracties kunnen optimaliseren voor hun specifieke use-cases, terwijl de Lightning protocol compliance en beveiligingsstandaarden behouden blijven.


## Breez sdk

<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>


:::video id=68d1f253-6210-4eab-8329-b676e5772eac:::

### De uitdaging van bliksemontwikkeling


Het ontwikkelen van toepassingen die Lightning-betalingen integreren vormt voor de meeste ontwikkelaars een aanzienlijke barrière. Om een app met Lightning-betalingsfunctionaliteit te maken, moeten ontwikkelaars in wezen Lightning-experts worden en complexe concepten zoals kanaalbeheer, liquiditeitsbalancering en netwerktopologie begrijpen. Deze expertisevereiste creëert een fundamenteel probleem voor de adoptie van Lightning: hoewel het Lightning-netwerk zelf operationeel is en betalingen betrouwbaar zijn, verhindert de technische complexiteit een wijdverspreide integratie in alledaagse toepassingen.


De belangrijkste uitdaging ligt in de kloof tussen wat ontwikkelaars nodig hebben en wat ze willen leveren. Ontwikkelaars werken meestal met strakke deadlines en geven de voorkeur aan eenvoudige oplossingen waarmee ze zich kunnen richten op de kernfunctionaliteit van hun applicatie in plaats van experts te worden in betalingsinfrastructuur. Wanneer Lightning-integratie moeilijk is, neigen ontwikkelaars van nature naar custodial oplossingen omdat die de weg van de minste weerstand bieden. Deze neiging naar custodial services ondermijnt echter Bitcoin's fundamentele waardepropositie van niet-custodial financiële soevereiniteit.


### Breez's Visie, Overal bliksem


Breez is ontstaan uit een eenvoudige, maar ambitieuze visie: iedereen verbinden met het Lightning-netwerk via intuïtieve interfaces voor de Lightning-economie. De aanpak van het bedrijf erkent dat, hoewel het Lightning-netwerk technisch goed functioneert, het wanhopig gebruikersadoptie nodig heeft om zijn volledige potentieel te bereiken. Deze adoptie-uitdaging gaat verder dan individuele gebruikers en omvat het hele ecosysteem van applicaties en diensten die zouden kunnen profiteren van Lightning-integratie.


De originele Breez app demonstreerde deze visie door gebruikers te voorzien van een Lightning-knooppunt dat direct op hun mobiele telefoon draait. Deze app toonde Lightning-mogelijkheden zoals het streamen van microbetalingen naar podcasters en functionaliteit voor verkooppunten. De Breez app onthulde echter ook een kritieke architecturale beperking: het ecosysteem van mobiele apps faciliteert geen gemakkelijke communicatie tussen applicaties, waardoor ontwikkelaars gedwongen worden om alle Lightning-gerelateerde functies in een enkele app te bouwen in plaats van gespecialiseerde applicaties toe te staan om gebruik te maken van gedeelde Lightning-infrastructuur.


De lessen van het bedrijf uit de Breez app leidden tot een cruciaal inzicht: de toekomst van Lightning hangt af van het overtuigen van ontwikkelaars. Als niet-custodiale Lightning-integratie de gemakkelijkste optie wordt voor ontwikkelaars, wordt het de standaardkeuze. Deze aanpak biedt ook voordelen op het gebied van regelgeving, aangezien niet-custodial software met minder regelgevingshindernissen te maken krijgt dan custodial services, waardoor het voor ontwikkelaars eenvoudiger wordt om hun applicaties wereldwijd te verschepen.


### De Breez SDK-architectuur


De Breez SDK biedt een alternatieve benadering voor het integreren van Lightning-functionaliteit in toepassingen. In plaats van te vereisen dat elke app zijn eigen Lightning-node draait, biedt de SDK een architectuur die niet-custodiale principes handhaaft en tegelijkertijd de ervaring van de ontwikkelaar vereenvoudigt. In de kern geeft de SDK elke eindgebruiker zijn eigen persoonlijke Lightning-node die draait op Greenlight-infrastructuur, Blockstream's cloud-gebaseerde Lightning node hosting service.


Deze architectuur lost verschillende kritieke problemen tegelijk op. Gebruikers hoeven zich geen zorgen te maken over databasebeheer, server uptime of infrastructuuronderhoud - zorgen die overweldigend zouden zijn voor typische consumenten. In tegenstelling tot traditionele custodial oplossingen heeft Greenlight echter nooit toegang tot gebruikerssleutels. Het Lightning knooppunt in de cloud kan geen bewerkingen uitvoeren zonder een actief verbonden applicatie die transacties en berichten kan ondertekenen. Dit ontwerp behoudt de beveiligingsvoordelen van self-custody terwijl de operationele complexiteit wordt geëlimineerd.


De SDK ondersteunt ook interoperabiliteit. Meerdere applicaties kunnen verbinding maken met het Lightning-knooppunt van dezelfde gebruiker met dezelfde seed-zin, waardoor gebruikers een enkel Lightning-saldo kunnen behouden voor verschillende gespecialiseerde applicaties. Een gebruiker kan bijvoorbeeld zowel een algemene Lightning wallet app als een gespecialiseerde podcasting app hebben, die beide toegang hebben tot dezelfde fondsen en Lightning kanalen. Deze architectuur maakt de ontwikkeling van gerichte, gespecialiseerde toepassingen mogelijk, terwijl de uniforme financiële infrastructuur behouden blijft.


### Lightning Service Providers en just-in-time liquiditeit


Een cruciaal onderdeel van de Breez SDK is de integratie met Lightning Service Providers (LSP's), die analoog functioneren als Internet Service Providers, maar dan voor het Lightning-netwerk. LSP's lossen een van de meest complexe uitdagingen van Lightning op: liquiditeitsbeheer. In Lightning-kanalen kunnen fondsen alleen stromen in richtingen waar liquiditeit bestaat, vergelijkbaar met kralen op een telraam die alleen kunnen bewegen waar ruimte is.


De SDK implementeert "just-in-time" kanalen via LSP's, waarbij de liquiditeit automatisch wordt beheerd zonder tussenkomst van de gebruiker. Wanneer een gebruiker een betaling moet ontvangen maar niet over voldoende inkomende liquiditeit beschikt, opent de LSP automatisch een nieuw Lightning-kanaal op het moment dat de betaling binnenkomt. Dit proces verloopt naadloos op de achtergrond, zodat gebruikers altijd betalingen kunnen ontvangen zonder inzicht te hebben in de onderliggende kanaalmechanismen.


Deze LSP-integratie gaat verder dan eenvoudig liquiditeitsbeheer. De SDK bevat uitgebreide Lightning-functionaliteit uit de doos: ingebouwde wachttorendiensten voor beveiliging, on-chain interoperabiliteit via onderzeese swaps, fiat on-ramps via diensten zoals MoonPay en ondersteuning voor LNURL-protocollen. Het systeem biedt ook naadloze back-up en herstel, zodat gebruikers nooit de toegang tot hun fondsen verliezen, zelfs als infrastructuurproviders veranderen of onbeschikbaar worden.


### Ervaring met implementatie en ontwikkelaars


De Breez SDK geeft prioriteit aan de ervaring van ontwikkelaars door zijn uitgebreide, op batterijen gebaseerde aanpak. De SDK biedt bindingen voor meerdere programmeertalen, waaronder Rust, Swift, Kotlin, Python, Go, React Native, Flutter en C#, zodat ontwikkelaars Lightning-betalingen kunnen integreren met de ontwikkeltools van hun voorkeur. De architectuur abstraheert de complexiteit van Lightning door middel van API's, terwijl de beveiliging van het Lightning-netwerk behouden blijft.


Belangrijke onderdelen werken samen om deze vereenvoudigde ervaring te bieden. De input parser verwerkt automatisch verschillende betalingsformaten, door te bepalen of een string een factuur, LNURL of andere betalingsmethode vertegenwoordigt en deze door te sturen naar de juiste afhandelingsfunctie. De geïntegreerde ondertekenaar beheert alle cryptografische operaties op de achtergrond, terwijl de swapper on-chain interacties transparant afhandelt. Dankzij dit ontwerp kunnen ontwikkelaars zich richten op de unieke waardepropositie van hun applicatie in plaats van Lightning-infrastructuurexperts te worden.


De vertrouwensloze architectuur van de SDK zorgt ervoor dat Greenlight weliswaar kanaaltoestanden en routeringsinformatie kan observeren, maar geen toegang heeft tot gebruikersgelden of onbevoegde bewerkingen kan uitvoeren. Gebruikers behouden volledige controle over hun privésleutels, die nooit hun apparaten verlaten. Deze aanpak vertegenwoordigt een weloverwogen afweging tussen operationele eenvoud en privacy, en biedt een praktisch pad voor algemene invoering van Lightning, terwijl de kernprincipes van Bitcoin van financiële soevereiniteit behouden blijven.


## LDK vs Breez SDK

<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>


:::video id=c3dec3df-1416-4761-b7c8-e1d66d27e390:::

### De beperkingen van Lightning Development Kit (LDK) begrijpen


De Lightning Development Kit is een verzameling Rust bibliotheken, ontworpen om ontwikkelaars flexibiliteit te bieden bij het bouwen van Lightning Network toepassingen. Deze flexibiliteit gaat echter gepaard met aanzienlijke implementatie-uitdagingen die duidelijk werden tijdens de ontwikkeling in de praktijk op Lipa. Het low-level karakter van de LDK betekent dat ontwikkelaars talrijke complexe taken onafhankelijk moeten uitvoeren, van synchronisatie van netwerkgrafieken tot optimalisatie van betalingsroutering. Hoewel deze aanpak volledige controle biedt over de Lightning-implementatie, vereist het aanzienlijke ontwikkelingsmiddelen en diepgaande technische expertise om productieklare betrouwbaarheid te bereiken.


Een van de belangrijkste ontbrekende functies in LDK was ondersteuning voor LNURL, een breed geaccepteerde standaard die Lightning Network interacties voor eindgebruikers vereenvoudigt. Daarnaast zorgde het ontbreken van ankeruitgangen voor serieuze operationele uitdagingen, vooral in omgevingen met hoge tarieven. Anchor uitgangen lossen een fundamenteel probleem op met Lightning-kanaal geforceerde sluitingen: wanneer netwerkvergoedingen dramatisch stijgen, kunnen kanalen met vooraf gedefinieerde vergoedingen onmogelijk eenzijdig worden gesloten omdat de vooraf ingestelde vergoeding onvoldoende wordt voor transactiebevestiging. Deze beperking bleek vooral problematisch voor mobiele wallet toepassingen, waar gebruikers de wallet kunnen verlaten zonder coöperatieve kanaalsluitingen te coördineren, waardoor fondsen mogelijk gestrand blijven tijdens kostenpieken.


De relatieve onvolwassenheid van de LDK uitte zich ook in onbetrouwbare betalingsroutering, een kritiek probleem voor elke Lightning-toepassing. Ondanks het feit dat het een technisch goede implementatie is, maakte het brede toepassingsgebied van de LDK als generieke oplossing het een uitdaging om specifieke problemen snel aan te pakken. Het ontwikkelteam moest veel tijd besteden aan het oplossen van routeringsproblemen en het implementeren van functies die idealiter op bibliotheekniveau zouden moeten worden afgehandeld, wat uiteindelijk ten koste ging van de ontwikkelingssnelheid en de kwaliteit van de gebruikerservaring.


### De voordelen van Breez SDK en Greenlight ontdekken


De overgang naar Breez SDK betekende een verschuiving in de architecturale aanpak, waarbij werd overgestapt van een zelfbeheerde Lightning-node naar een cloud-gebaseerde oplossing die wordt aangedreven door Blockstream's Greenlight-service. Deze verandering pakte onmiddellijk verschillende kritieke pijnpunten aan die werden ervaren met de LDK-implementatie. De belangrijkste verbetering betrof de betrouwbaarheid van de betaling, voornamelijk dankzij het vermogen van Greenlight om een altijd actuele netwerkgrafiek te onderhouden. In tegenstelling tot traditionele mobiele Lightning-implementaties die netwerkinformatie moeten synchroniseren wanneer de applicatie start, draaien Greenlight nodes continu in de cloud, waardoor ze realtime op de hoogte blijven van het netwerk en direct volledige grafiekgegevens leveren wanneer gebruikers verbinding maken.


Deze architectuur maakt gebruik van de in de strijd geteste Core Lightning (CLN) implementatie, die jarenlang met succes betalingen heeft gerouteerd als een van de oorspronkelijke Lightning Network implementaties. De opgebouwde ervaring en bewezen betrouwbaarheid van CLN zorgde voor onmiddellijke stabiliteitsverbeteringen ten opzichte van het jongere LDK project. Wanneer gebruikers hun Greenlight-aangedreven wallet activeren, erven ze onmiddellijk de volledige netwerkkennis en routingmogelijkheden van een continu draaiend Lightning knooppunt, waardoor de synchronisatievertragingen en routingonzekerheden die de vorige implementatie teisterden, geëlimineerd worden.


De eigenzinnige ontwerpfilosofie van de Breez SDK was nuttig voor de ontwikkeling van wallet. In plaats van een generieke Lightning-toolkit aan te bieden, richt Breez zich specifiek op wallet toepassingen voor eindgebruikers, waardoor het ontwikkelingsteam zich kon concentreren op het creëren van uitgebreide oplossingen voor dit specifieke gebruik. Deze gerichte aanpak stelde Breez in staat om essentiële diensten direct in de SDK te integreren, inclusief Lightning Service Provider (LSP) functionaliteit die gebruikers in staat stelt om direct betalingen te ontvangen na installatie van wallet, zonder dat er handmatige kanaalopeningsprocedures nodig zijn.


### Uitgebreide functies en verbeteringen in de gebruikerservaring


De geïntegreerde aanpak van de Breez SDK gaat verder dan de Lightning-basisfunctionaliteit en bevat functies die de gebruikerservaring verbeteren. De ingebouwde LSP-integratie elimineert de traditionele barrière dat gebruikers inzicht moeten hebben in kanaalbeheer, waardoor nieuwe wallet-installaties onmiddellijk betalingen kunnen ontvangen. Dit onboarding proces helpt bij de mainstream adoptie, omdat gebruikers kunnen beginnen met het ontvangen van Lightning-betalingen zonder enige technische kennis of instellingsprocedures.


De on-chain swapfunctie biedt nog een laag optimalisatie van de gebruikerservaring door de presentatie van een uniform saldo aan gebruikers mogelijk te maken. In plaats van gebruikers te dwingen om het onderscheid tussen Lightning en on-chain Bitcoin te begrijpen, maakt de swapdienst automatische conversie tussen deze lagen mogelijk als dat nodig is. Wanneer gebruikers on-chain betalingen moeten doen, kan het systeem achter de schermen naadloos Lightning fondsen omwisselen naar on-chain Bitcoin, waardoor de illusie van één liquide saldo behouden blijft, terwijl de technische complexiteit intern wordt afgehandeld.


De ondersteuning van de SDK voor nul-kanaalreserves pakt een belangrijke uitdaging op het gebied van gebruikerservaring aan in traditionele Lightning-implementaties. Kanaalreserves voorkomen meestal dat gebruikers hun volledige weergegeven saldo uitgeven, waardoor verwarring ontstaat wanneer betalingen mislukken ondanks dat er ogenschijnlijk voldoende geld is. Door deze reserves te elimineren, stelt Breez gebruikers in staat om hun volledig getoonde saldo uit te geven, hoewel dit van de LSP vereist dat hij extra risico accepteert. Deze afweging is een voorbeeld van Breez's gebruikersgerichte aanpak, waarbij technische complexiteit en risico's worden opgevangen door dienstverleners om intuïtieve gebruikerservaringen te creëren.


Extra functies zoals LNURL-ondersteuning, wisselkoersdiensten en synchronisatie met meerdere apparaten tonen de uitgebreide benadering van de SDK voor wallet-ontwikkeling. De cloud-gebaseerde architectuur stelt gebruikers in staat om toegang te krijgen tot hun Lightning node vanaf meerdere apparaten of applicaties, waarbij Breez de status synchronisatie tussen deze verschillende toegangspunten afhandelt. Toekomstige punten op de roadmap zijn onder andere spend-all functionaliteit voor volledige wallet afwatering, splicing voor dynamisch kanaalbeheer en een marktplaats van concurrerende LSP's om gezonde concurrentie in de dienstverlening te introduceren.


### Evaluatie van compromissen en centralisatieoverwegingen


De overgang naar Breez SDK en Greenlight introduceert belangrijke centralisatie afwegingen die zorgvuldig overwogen moeten worden in de context van Bitcoin's decentralisatieprincipes. De cloud-gebaseerde architectuur betekent dat de Lightning nodes van gebruikers opereren op de infrastructuur van Blockstream, waardoor afhankelijkheid ontstaat van zowel de voortdurende werking van Greenlight als de voortdurende ontwikkeling van Breez. Deze centralisatie gaat verder dan alleen gemak, en heeft mogelijk invloed op het vermogen van gebruikers om geld terug te krijgen als diensten onbeschikbaar worden of als er censuur plaatsvindt.


Herstelscenario's vormen een bijzondere uitdaging in deze architectuur. Hoewel gebruikers de controle over hun privésleutels behouden, zou toegang tot fondsen zonder de infrastructuur van Greenlight technische expertise vereisen om onafhankelijke Core Lightning nodes op te starten en kanaaltoestanden te herstellen. Voor individuele gebruikers zou dit herstelproces waarschijnlijk onbetaalbaar complex zijn, en zelfs wallet aanbieders zouden voor aanzienlijke uitdagingen komen te staan om hele gebruikersbestanden te migreren naar alternatieve infrastructuur als Greenlight diensten zouden worden stopgezet.


Privacyoverwegingen verschuiven ook met deze architecturale verandering. De cloud-gebaseerde routering betekent dat Greenlight potentieel inzicht krijgt in betalingsbestemmingen, terwijl eerdere LSP-only architecturen het lekken van informatie beperkten tot betalingsbedragen en timing. Het genereren van Invoice in de cloud breidt de potentiële blootstelling aan informatie verder uit, aangezien ongebruikte facturen die voorheen privé bleven op de apparaten van gebruikers nu door de infrastructuur van Blockstream gaan.


Ondanks deze zorgen over centralisatie, wegen de praktische voordelen vaak zwaarder dan de theoretische risico's voor veel use cases. De verbeterde betrouwbaarheid, uitgebreide functieset en superieure gebruikerservaring stellen wallet ontwikkelaars in staat om zich te concentreren op innovaties in de applicatielaag in plaats van op het beheer van de Lightning-infrastructuur. Deze taakverdeling weerspiegelt een volwassen ecosysteem waarin gespecialiseerde serviceproviders complexe technische uitdagingen afhandelen, zodat applicatieontwikkelaars zich kunnen concentreren op gebruikerservaring en bedrijfslogica. De sleutel ligt in het duidelijk begrijpen van deze afwegingen en het maken van weloverwogen beslissingen op basis van specifieke use case-eisen en risicotolerantieniveaus.




# Laatste Sectie

<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>



## Beoordelingen

<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>

<isCourseReview>true</isCourseReview>

## Conclusie

<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>

<isCourseConclusion>true</isCourseConclusion>