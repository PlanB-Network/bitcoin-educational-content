---
name: RGB CLI
description: Hvordan oppretter og utveksler jeg smartkontrakter på RGB?
---
![cover](assets/cover.webp)

I denne veiledningen følger vi trinn-for-trinn-prosessen med å skrive en kontrakt ved hjelp av kommandolinjeverktøyet `rgb`, som er opprettet av LNP/BP-foreningen. Målet er å vise hvordan du installerer og manipulerer CLI, kompilerer et skjema, importerer grensesnittet og grensesnittimplementeringen, og deretter utsteder en RGB-ressurs. Vi ser også på den underliggende logikken, inkludert kompilering og tilstandsvalidering. På slutten av denne opplæringen skal du være i stand til å reprodusere prosessen og opprette dine egne RGB-kontrakter.

## Påminnelse om RGB-protokoll

RGB er en protokoll som kjører på toppen av Bitcoin og emulerer smartkontraktsfunksjonalitet og forvaltning av digitale aktiva, uten å overbelaste blokkjeden som den er basert på. I motsetning til konvensjonelle smartkontrakter i kjeden (som for eksempel på Ethereum), baserer RGB seg på et "*Validering på klientsiden*"-system: mesteparten av data og statushistorikk utveksles og lagres utelukkende av de involverte deltakerne, mens Bitcoin-blokkjeden kun er vert for små kryptografiske forpliktelser (via mekanismer som *Tapret* eller *Opret*). I RGB-protokollen fungerer Bitcoin-blokkjeden derfor bare som en tidsstemplingsserver og et system for beskyttelse mot dobbeltbruk.

En RGB-kontrakt er strukturert som en evolusjonær tilstandsmaskin. Den starter med en Genesis som definerer den opprinnelige tilstanden (som for eksempel beskriver tilbudet, tickeren eller andre metadata) i henhold til et strengt typet og kompilert Schema. Deretter brukes State Transitions og, om nødvendig, State Extensions for å endre eller utvide denne tilstanden. Hver operasjon, enten det gjelder overføring av fungible aktiva (RGB20) eller opprettelse av unike aktiva (RGB21), involverer *Single-use Seals*. Disse kobler Bitcoin UTXOer til stater utenfor kjeden og forhindrer dobbeltbruk, samtidig som de sikrer konfidensialitet og skalerbarhet.

Hvis du vil lære mer om hvordan RGB-protokollen fungerer, anbefaler jeg at du tar dette omfattende opplæringskurset:

https://planb.network/courses/csv402
Den interne logikken i RGB er basert på Rust-biblioteker som du som utvikler kan importere til prosjektene dine for å håndtere *Klientsidevalidering*-delen. I tillegg jobber LNP/BP-teamet med bindinger for andre språk, men dette er ennå ikke ferdigstilt. I tillegg utvikler andre enheter som Bitfinex sine egne integrasjonsstabler, men vi vil snakke om disse i en annen veiledning. Inntil videre er `rgb` CLI den offisielle referansen, selv om den fortsatt er relativt upolert.

## Installasjon og presentasjon av rgb CLI-verktøyet

Hovedkommandoen heter ganske enkelt `rgb`. Den er designet for å minne om `git`, med et sett underkommandoer for å manipulere kontrakter, påkalle dem, utstede eiendeler og så videre. Bitcoin Wallet er for øyeblikket ikke integrert, men vil bli det i en nært forestående versjon (0.11). Denne neste versjonen vil gjøre det mulig for brukere å opprette og administrere lommebøker (via deskriptorer) direkte fra `rgb`, inkludert PSBT-generering, kompatibilitet med ekstern maskinvare (f.eks. en maskinvarelommebok) for signering, og interoperabilitet med programvare som Sparrow. Dette vil forenkle hele utstedelses- og overføringsscenarioet.

### Installasjon via Cargo

Vi installerer verktøyet i Rust med :

```bash
cargo install rgb-contracts --all-features
```

(Merk: Kassen heter `rgb-contracts`, og den installerte kommandoen vil hete `rgb`. Hvis det allerede eksisterte en crate med navnet `rgb`, kan det ha vært en kollisjon, derav navnet)

Installasjonen kompilerer et stort antall avhengigheter (f.eks. kommandoanalyse, Electrum-integrasjon, håndtering av nullkunnskapsbevis osv.)

Når installasjonen er fullført, vil :

```bash
rgb
```

Ved å kjøre `rgb` (uten argumenter) vises en liste over tilgjengelige underkommandoer, for eksempel `grensesnitt`, `skjema`, `import`, `eksport`, `utstedelse`, `faktura`, `overføring` osv. Du kan endre den lokale lagringskatalogen (et lager som inneholder alle logger, skjemaer og implementasjoner), velge nettverk (testnet, mainnet) eller konfigurere Electrum-serveren din.

![RGB-CLI](assets/fr/01.webp)

### Første oversikt over kontroller

Når du kjører følgende kommando, vil du se at et `RGB20`-grensesnitt allerede er integrert som standard:

```bash
rgb interfaces
```

Hvis dette grensesnittet ikke er integrert, kloner du :

```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```

Kompilere den:

```bash
cargo run
```

Importer deretter grensesnittet du ønsker:

```bash
rgb import interfaces/RGB20.rgb
```

![RGB-CLI](assets/fr/02.webp)

Vi har imidlertid fått beskjed om at det ennå ikke er importert noe skjema til programvaren. Det finnes heller ingen kontrakt i lageret. For å se den, kjør kommandoen :

```bash
rgb schemata
```

Deretter kan du klone repositoryet for å hente ut bestemte skjemaer:

```bash
git clone https://github.com/RGB-WG/rgb-schemata
```

![RGB-CLI](assets/fr/03.webp)

I katalogen `src/` inneholder dette depotet flere Rust-filer (for eksempel `nia.rs`) som definerer skjemaer (NIA for "*Non Inflatable Asset*", UDA for "*Unique Digital Asset*" osv.) For å kompilere kan du deretter kjøre :

```bash
cd rgb-schemata
cargo run
```

Dette genererer flere `.rgb`- og `.rgba`-filer som svarer til de kompilerte skjemaene. Du finner for eksempel `NonInflatableAsset.rgb`.

### Import av skjema og grensesnittimplementering

Du kan nå importere skjemaet til `rgb` :

```bash
rgb import schemata/NonInflatableAssets.rgb
```

![RGB-CLI](assets/fr/04.webp)

Dette legger det til i det lokale lageret. Hvis vi kjører følgende kommando, ser vi at skjemaet nå vises:

```bash
rgb schemata
```

## Opprettelse av kontrakt (utstedelse)

Det finnes to måter å opprette en ny ressurs på:


- Enten bruker vi et skript eller kode i Rust som bygger en kontrakt ved å fylle ut skjemafelter (global tilstand, Owned States osv.) og produserer en `.rgb`- eller `.rgba`-fil;
- Eller bruk underkommandoen `issue` direkte, med en YAML-fil (eller TOML) som beskriver tokenets egenskaper.

Du finner eksempler i Rust i mappen `examples`, som illustrerer hvordan du bygger en `ContractBuilder`, fyller inn `global state` (asset name, ticker, supply, date, etc.), definerer Owned State (hvilken UTXO den er tilordnet), og deretter kompilerer alt dette til en *contract consignment* som du kan eksportere, validere og importere til et stash.

Den andre måten er å redigere en YAML-fil manuelt for å tilpasse `ticker`, `name`, `supply`, og så videre. Anta at filen heter `RGB20-demo.yaml`. Du kan spesifisere :


- `spec`: ticker, navn, presisjon ;
- `terms`: et felt for juridiske merknader ;
- `issuedSupply` : mengden token som er utstedt ;
- `assignments`: angir engangsforseglingen (*forseglingsdefinisjon*) og mengden som er låst opp.

Her er et eksempel på en YAML-fil som kan opprettes:

```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```

![RGB-CLI](assets/fr/05.webp)

Deretter kjører du bare kommandoen :

```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```

![RGB-CLI](assets/fr/06.webp)

I mitt tilfelle er den unike skjemaidentifikatoren (som skal være omsluttet av enkle anførselstegn) `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k`, og jeg har ikke lagt inn noen utsteder. Så bestillingen min er :

```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```

Hvis du ikke kjenner skjema-ID-en, kan du kjøre kommandoen :

```bash
rgb schemata
```

CLI svarer at en ny kontrakt er utstedt og lagt til i lageret. Hvis vi skriver inn følgende kommando, ser vi at det nå finnes en ekstra kontrakt som tilsvarer den som nettopp ble utstedt:

```bash
rgb contracts
```

![RGB-CLI](assets/fr/07.webp)

Deretter viser den neste kommandoen de globale tilstandene (navn, ticker, forsyning ...) og listen over Owned States, dvs. allokeringer (for eksempel 1 million `PBN`-tokens definert i UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).

```bash
rgb state '<ContractId>'
```

![RGB-CLI](assets/fr/08.webp)

## Eksport, import og validering

Hvis du vil dele kontrakten med andre brukere, kan den eksporteres fra lageret til en :

```bash
rgb export '<ContractId>' myContractPBN.rgb
```

![RGB-CLI](assets/fr/09.webp)

Filen `myContractPBN.rgb` kan sendes videre til en annen bruker, som kan legge den til sin stash med kommandoen :

```bash
rgb import myContractPBN.rgb
```

Ved import, hvis det er en enkel *kontraktsforsendelse*, får vi meldingen "`Importing consignment rgb`". Hvis det er en større *statovergangsforsendelse*, vil kommandoen være annerledes (`rgb accept`).

Du kan også bruke den lokale valideringsfunksjonen for å sikre gyldighet. Du kan for eksempel kjøre :

```bash
rgb validate myContract.rgb
```

### Bruk, verifisering og visning av lagerbeholdning

Som en påminnelse er lageret en lokal beholdning av skjemaer, grensesnitt, implementasjoner og kontrakter (Genesis + overganger). Hver gang du kjører "import", legger du til et element i lageret. Dette lageret kan vises i detalj med kommandoen :

```bash
rgb dump
```

![RGB-CLI](assets/fr/10.webp)

Dette vil generere en mappe med informasjon om hele lageret.

## Overføring og PSBT

For å gjennomføre en overføring må du manipulere en lokal Bitcoin-lommebok for å administrere `Tapret`- eller `Opret`-forpliktelsene.

### Generer en faktura

I de fleste tilfeller foregår interaksjonen mellom deltakerne i en kontrakt (f.eks. Alice og Bob) ved at det genereres en faktura. Hvis Alice vil at Bob skal utføre noe (en tokenoverføring, en reutstedelse, en handling i en DAO osv.), oppretter Alice en faktura som beskriver instruksjonene hennes til Bob. Så vi har :


- Alice** (utstederen av fakturaen) ;
- Bob** (som mottar og utfører fakturaen).

I motsetning til andre økosystemer er en RGB-faktura ikke begrenset til betalingsbegrepet. Den kan inneholde en hvilken som helst forespørsel knyttet til kontrakten: tilbakekalle en nøkkel, stemme, opprette en gravering (*gravering*) på en NFT osv. Den tilsvarende operasjonen kan beskrives i kontraktsgrensesnittet. Den tilsvarende operasjonen kan beskrives i kontraktsgrensesnittet.

Følgende kommando genererer en RGB-faktura:

```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```

Med :


- `$CONTRACT`: Kontraktsidentifikator (*ContractId*) ;
- `$INTERFACE`: grensesnittet som skal brukes (f.eks. `RGB20`) ;
- `$ACTION`: navnet på operasjonen som er angitt i grensesnittet (for en enkel fungibel tokenoverføring kan dette være "Transfer"). Hvis grensesnittet allerede har en standardhandling, trenger du ikke å oppgi den igjen her;
- `$STATE`: statusdataene som skal overføres (for eksempel en mengde tokens hvis en fungibel token overføres);
- `$SEAL`: mottakerens (Alices) engangsforsegling, dvs. en eksplisitt referanse til en UTXO. Bob vil bruke denne informasjonen til å lage vitnetransaksjonen, og den tilsvarende utdataen vil da tilhøre Alice (i *blindet UTXO* eller ukryptert form).

For eksempel med følgende kommandoer

```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```

CLI vil generere en faktura som :

```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```

Den kan sendes til Bob via en hvilken som helst kanal (tekst, QR-kode osv.).

### Foreta en overføring

For å overføre fra denne fakturaen :


- Bob (som har tokens i sin stash) har en Bitcoin-lommebok. Han må forberede en Bitcoin-transaksjon (i form av en PSBT, f.eks. `tx.psbt`) som bruker UTXOene der de nødvendige RGB-tokens befinner seg, pluss én UTXO for valuta (veksling);
- Bob utfører følgende kommando:

```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```


- Dette genererer en `consignment.rgb`-fil som inneholder :
 - Overgangshistorikken beviser for Alice at symbolene er ekte;
 - Den nye overgangen som overfører tokens til Alice's Single-use Seal ;
 - En vitnetransaksjon (usignert).
- Bob sender denne `consignment.rgb`-filen til Alice (via e-post, en delingsserver eller en RGB-RPC-protokoll, Storm, etc.);
- Alice mottar `consignment.rgb` og aksepterer det i sin egen stash :

```bash
alice$ rgb accept consignment.rgb
```


- CLI kontrollerer gyldigheten av overgangen og legger den til i Alices lager. Hvis den er ugyldig, mislykkes kommandoen med en detaljert feilmelding. Hvis ikke, lykkes den, og rapporterer at eksempeltransaksjonen ennå ikke har blitt kringkastet på Bitcoin-nettverket (Bob venter på grønt lys fra Alice);
- Som bekreftelse returnerer kommandoen `accept` en signatur (*betalingsslipp*) som Alice kan sende til Bob for å vise ham at hun har godkjent *forsendelsen* ;
- Bob kan deretter signere og publisere (`--publisere`) sin Bitcoin-transaksjon:

```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```


- Så snart denne transaksjonen er bekreftet i kjeden, anses eierskapet til eiendelen som overført til Alice. Alices lommebok, som overvåker transaksjonens utvinning, ser den nye Owned State dukke opp i sin stash.

Du vet nå hvordan du utsteder og overfører en RGB-kontrakt. Hvis du synes denne veiledningen var nyttig, vil jeg være veldig takknemlig hvis du setter en grønn tommel nedenfor. Del gjerne denne artikkelen på dine sosiale nettverk. Tusen takk skal du ha!

Jeg anbefaler også denne andre veiledningen, der jeg forklarer hvordan du starter en RGB-kompatibel Lightning-node for å utveksle tokens nesten umiddelbart:

https://planb.network/tutorials/node/rgb/rln-ffc02528-329b-4e16-bd83-873d0299feea