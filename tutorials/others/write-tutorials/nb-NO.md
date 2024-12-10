---
name: Bidrag - Veiledninger
description: Hvordan foreslå en ny veiledning på PlanB Network?
---
![cover](assets/cover.webp)

PlanB sin misjon er å tilby førsteklasses pedagogiske ressurser om Bitcoin, på så mange språk som mulig. Alt innhold publisert på nettstedet er åpen kildekode og hostet på GitHub, noe som gir muligheten for hvem som helst å delta i å berike plattformen. Bidrag kan ta forskjellige former: korrigering og korrekturlesing av eksisterende tekster, oversettelse til andre språk, oppdatering av informasjon, eller å skape nye veiledninger som ennå ikke er tilgjengelige på vår side.

I denne veiledningen vil jeg forklare hvordan du kan endre "Veiledninger"-seksjonen av PlanB Network. Hvis du ønsker å legge til en ny veiledning eller forbedre en eksisterende, er denne artikkelen for deg! Vi vil se nærmere på hvordan du kan bidra til PlanB Network via GitHub, mens du bruker Obsidian, et skriveverktøy.

## Forutsetninger

For å bidra til PlanB Network, har du 3 alternativer avhengig av din erfaring med GitHub:
1. **Erfarne brukere**: Fortsett med dine vanlige metoder og konsulter denne veiledningen for å gjøre deg kjent med strukturen til PlanB-repositoriet, spesifikke krav, og arbeidsflyten.
2. **Nybegynnere klare til å lære**: Jeg anbefaler å sette opp ditt eget arbeidsmiljø. Følg denne veiledningen samt våre andre artikler nedenfor for å veilede deg steg for steg.
3. **Nybegynnere for mindre bidrag**: For oppgaver som krever mindre modifikasjon, som korrekturlesing eller korreksjoner, bruk GitHub sin webgrensesnitt direkte uten å sette opp et komplett lokalt miljø.

**Programvare som kreves for å følge min veiledning:**
- [GitHub Desktop](https://desktop.github.com/)
- [Obsidian](https://obsidian.md/)
- En kodeeditor ([VSC](https://code.visualstudio.com/) eller [Sublime Text](https://www.sublimetext.com/))
![tutorial](assets/1.webp)
**Forutsetninger før du starter veiledningen:**
- Ha en [GitHub-konto](https://github.com/signup).
- Ha en fork av [PlanB Network kildekode-repositoriet](https://github.com/PlanB-Network/bitcoin-educational-content).
- Ha [en professorprofil på PlanB Network](https://planb.network/professors) (kun hvis du foreslår en komplett veiledning).

**Hvis du trenger hjelp til å oppnå disse forutsetningene, vil mine andre veiledninger guide deg:**
**[Forstå Git og GitHub](https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb)**
**[Opprette en GitHub-konto](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c)**
**[Sette opp ditt arbeidsmiljø](https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba)**
**[Opprette en professorprofil](https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4)**
## Hvilken type innhold å skrive på PlanB Network?
Vi ser primært etter veiledninger om verktøy relatert til Bitcoin eller dets økosystem. Disse innholdene kan organiseres rundt seks hovedkategorier:
- Lommebok;
- Node;
- Mining;
- Handelsmann;
- Børs;
- Personvern.
![tutorial](assets/2.webp)
Utover disse emnene spesifikt relatert til Bitcoin, ser PlanB også etter bidrag om temaer som fremhever individuell suverenitet, som:
- Åpen kildekode-verktøy;
- Data;
- Kryptografi;
- Energi;
- Matematikk;
- Økonomi;
- Gjør-det-selv;
- LifeHacking...
For eksempel har vi for øyeblikket veiledninger om Tails, Nostr eller GrapheneOS. Disse verktøyene er ikke direkte relatert til Bitcoin, men de er systemer som kan interessere oss i en prosess for suverenitet i den digitale verden. Disse innholdene kan integreres i en underkategori av "Andre"-seksjonen.
Du har valget mellom å designe en veiledning fra bunnen av eller ta en veiledning som tidligere er publisert på nettstedet ditt (forutsatt at du eier opphavsretten) for å også dele den på PlanB Network, og legge til en lenke til den opprinnelige artikkelen.

Uansett hva du velger, husk at alt innhold publisert på PlanB Network er under den frie lisensen [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/). Denne lisensen tillater hvem som helst å kopiere og potensielt modifisere innholdet ditt, forutsatt at den opprinnelige kilden er korrekt kreditert.

## Hvordan foreslå en veiledning på PlanB Network?

Når alt er på plass, og ditt lokale miljø er godt satt opp med din egen fork av PlanB Network, kan du begynne å legge til veiledningen.

### Opprett en ny gren

- Åpne nettleseren din og gå til siden for din fork av PlanB-repositoriet. Dette er forken du har etablert på GitHub. URL-en til din fork bør se slik ut: `https://github.com/[ditt-brukernavn]/sovereign-university-data`:
![veiledning](assets/3.webp)
- Sørg for at du er på hovedgrenen `dev` og deretter klikk på `Sync fork`-knappen. Hvis din fork ikke er oppdatert, vil GitHub tilby å oppdatere grenen din. Fortsett med denne oppdateringen. Hvis, derimot, din gren allerede er oppdatert, vil GitHub informere deg:
![veiledning](assets/4.webp)
- Åpne GitHub Desktop-programvaren og sørg for at din fork er korrekt valgt i øvre venstre hjørne av vinduet:
![veiledning](assets/5.webp)
- Klikk på `Fetch origin`-knappen. Hvis ditt lokale repositorium allerede er oppdatert, vil GitHub Desktop ikke foreslå noen ytterligere handling. Ellers vil `Pull origin`-alternativet dukke opp. Klikk på denne knappen for å oppdatere ditt lokale repositorium: ![veiledning](assets/6.webp)
- Sørg for at du er på hovedgrenen `dev`:
![veiledning](assets/7.webp)
- Klikk på denne grenen, deretter klikk på `New Branch`-knappen:
![veiledning](assets/8.webp)
- Sørg for at den nye grenen er basert på kilde-repositoriet, nemlig `DecouvreBitcoin/sovereign-university-data`.
- Navngi din gren på en måte som tittelen er klar over formålet, ved å bruke bindestreker for å skille hvert ord. For eksempel, la oss si at vårt mål er å skrive en veiledning om bruk av Sparrow Wallet-programvaren. I dette tilfellet kunne arbeidsgrenen dedikert til å skrive denne veiledningen navngis: `tuto-sparrow-wallet-loic`. Når det passende navnet er angitt, klikk på `Create branch` for å bekrefte opprettelsen av grenen:
![veiledning](assets/9.webp)
- Nå klikker du på `Publish branch`-knappen for å lagre din nye arbeidsgren på din online fork på GitHub:
![veiledning](assets/10.webp)
Nå, på GitHub Desktop, bør du være på din nye gren. Dette betyr at alle endringer gjort lokalt på datamaskinen din vil bli registrert eksklusivt på denne spesifikke grenen. Også, så lenge denne grenen forblir valgt på GitHub Desktop, tilsvarer filene lokalt synlige på maskinen din de av denne grenen (`tuto-sparrow-wallet-loic`), og ikke de av hovedgrenen (`dev`).
![veiledning](assets/11.webp)
For hver nye artikkel du ønsker å publisere, må du opprette en ny gren fra `dev`. En gren i Git er en parallell versjon av prosjektet, som lar deg gjøre endringer uten å påvirke hovedgrenen, til arbeidet er klart til å bli slått sammen.
### Legge til opplæringen

Nå som arbeidsgrenen er opprettet, er det på tide å integrere din nye opplæring.
- Åpne filbehandleren din og naviger til `sovereign-university-data`-mappen, som representerer den lokale klonen av repositoriet ditt. Du bør vanligvis finne den under `Documents\GitHub\sovereign-university-data`. Innenfor denne katalogen, vil det være nødvendig å lokalisere den passende undermappen for å plassere opplæringen din. Organiseringen av mappene reflekterer de forskjellige seksjonene av PlanB Network-nettstedet. I vårt eksempel, siden vi ønsker å legge til en opplæring om Sparrow Wallet, er det passende å gå til følgende sti: `sovereign-university-data\tutorials\wallet` som tilsvarer `WALLET`-seksjonen på nettstedet: ![opplæring](assets/12.webp)
- Innenfor `wallet`-mappen, må du opprette en ny mappe spesifikt dedikert til opplæringen din. Navnet på denne mappen må fremkalle programvaren dekket i opplæringen, og sørge for å koble ord med bindestreker. For mitt eksempel, vil mappen bli tittulert `sparrow-wallet`:
![opplæring](assets/13.webp)
- I denne nye undermappen dedikert til opplæringen din, må flere elementer legges til:
	- Opprett en `assets`-mappe, ment for å motta alle illustrasjonene nødvendige for opplæringen din;
    - Innenfor denne `assets`-mappen, må du opprette 8 undermapper navngitt `fr`, `de`, `en`, `it`, `es`, `ja`, `vi`, og `pt`, for å klassifisere visuellene i henhold til de tilsvarende språkene. Du må også legge til en `notext`-undermappe for visuelt materiale som ikke trenger oversettelse, som skjermbilder for eksempel;
	- En `tutorial.yml`-fil må opprettes for å registrere detaljene relatert til opplæringen din;
	- En markdown-formatfil skal opprettes for å skrive det faktiske innholdet i opplæringen din. Denne filen må være tittulert i henhold til språkkoden for skrivingen. For eksempel, for en opplæring skrevet på fransk, bør filen kalles `fr.md`.
![opplæring](assets/14.webp)
- For å oppsummere, her er hierarkiet av filer som skal opprettes:
```plaintext
sovereign-university-data/
└── tutorials/
    └── wallet/ (skal endres med riktig kategori)
        └── sparrow-wallet/ (skal endres med navnet på opplæringen)
            ├── assets/
            │   ├── fr/
            │   ├── de/
            │   ├── en/
            │   ├── it/
            │   ├── es/
            │   ├── pt/
            |   ├── ja/
            |   ├── vi/
            │   └── notext/
            ├── tutorial.yml
            └── fr.md (skal endres i henhold til passende språkkode)
```

- For å starte, åpne din `tutorial.yml`-fil ved hjelp av kodeeditoren din.
- Fyll inn hvert felt med informasjonen spesifisert nedenfor:
- **builder**: Skriv inn navnet på selskapet som produserer programvaren du lager en opplæring for;
- **tags**: Bestem en serie nøkkelord nært relatert til emnet for artikkelen din, for å lette søket og indekseringen;
- **kategori**: Velg en passende underkategori blant de tilgjengelige på PlanB-nettstedet, basert på innholdet i opplæringen din. For eksempel, for en opplæring i `WALLET`-delen, er de tilgjengelige alternativene `Desktop`, `Hardware` og `Mobile`;
- **nivå**: Angi vanskelighetsgraden av opplæringen din ved å velge en av de følgende fire kategoriene:
    - Nybegynner (`beginner`),
    - Mellomnivå (`intermediary`),
    - Avansert (`advanced`),
    - Ekspert (`expert`).
- **professor**: Oppgi din bidragsyter-ID slik den vises på din professorprofil. For flere detaljer, se til [den tilsvarende opplæringen](https://planb.network/fr/tutorials/others/create-teacher-profile);
- **link** (valgfritt): I tilfelle du ønsker å kreditere en kilde nettside for opplæringen du utvikler, som din egen personlige side, er dette stedet du kan legge til den aktuelle lenken.
![opplæring](assets/15.webp)
- Når du har ferdigstilt endringene i din `tutorial.yml`-fil, lagre dokumentet ditt ved å klikke på `Fil > Lagre`:
![opplæring](assets/16.webp)
- Du kan nå lukke kodeeditoren din.
- I `assets`-mappen må du legge til en fil med navnet `logo.webp`, som vil fungere som et miniatyrbilde for artikkelen din. Dette bildet må være i `.webp`-format og må respektere en kvadratisk dimensjon for å harmonisere med brukergrensesnittet. Du har friheten til å velge logoen til programvaren som dekkes i opplæringen eller et annet relevant bilde, forutsatt at det er fri for rettigheter. I tillegg, legg også til et bilde med tittelen `cover.webp` på samme sted. Dette bildet vil bli vist øverst i opplæringen din. Sørg for at dette bildet, som logoen, respekterer bruksrettigheter og er passende for konteksten i opplæringen din:
![opplæring](assets/17.webp)
- Nå kan du åpne filen som vil være vert for opplæringen din, navngitt med koden for språket ditt, som for eksempel `fr.md`. Gå til Obsidian, på venstre side av vinduet, bla gjennom mappetreet til mappen for opplæringen din og til den søkte filen:
![opplæring](assets/18.webp)
- Klikk på filen for å åpne den:
![opplæring](assets/19.webp)
- Vi vil starte med å fylle ut `Properties`-delen øverst i dokumentet. Hvis denne delen mangler fra filen din (hvis dokumentet er helt blankt), kan du reprodusere den ved å kopiere den fra en annen eksisterende opplæring: ![opplæring](assets/20.webp)
- Du kan også legge den til manuelt på denne måten ved hjelp av kodeeditoren din:
```markdown
---
name: [Tittel]
description: [Beskrivelse]
---
```
![opplæring](assets/21.webp)
- Fyll inn navnet på opplæringen din og en kort beskrivelse av den:
![opplæring](assets/22.webp)
- Legg deretter til ditt dekkbilde i begynnelsen av opplæringen din. For å gjøre dette, skriv:
```markdown
![cover-sparrow](assets/cover.webp)
```
- Denne syntaksen vil være nyttig hver gang du trenger å legge til et bilde i opplæringen din. Utropstegnet indikerer at det er et bilde, med alternativ tekst (alt) spesifisert mellom klammeparentesene. Stien til bildet er angitt mellom parentesene:
![opplæring](assets/23.webp)
- Fortsett å skrive opplæringen din ved å skrive innholdet ditt. Når du ønsker å integrere en undertittel, bruk den passende markdown-formateringen ved å prefikse teksten med `##`:
![opplæring](assets/24.webp)

### Hvordan legge til diagrammer i opplæringen?
Språkundermappene i `assets`-mappen er ment for å organisere diagrammer og visuelt materiale som vil følge opplæringen din. Hvis bildene dine inkluderer tekst, sørg for å oversette dem for hvert relevant språk for å gjøre innholdet ditt tilgjengelig for et internasjonalt publikum. For diagrammer uten tekst som trenger oversettelse eller skjermbilder, plasser dem direkte i `notext`-undermappen.![opplæring](assets/25.webp)
For å navngi bildene dine, sett enkelt tall i rekkefølgen de vises i opplæringen. For eksempel, navngi ditt første bilde `1.webp`, ditt andre `2.webp`, og så videre.

Hvis det samme diagrammet er oversatt til flere språk, behold samme filnavn for de forskjellige oversettelsene i språkundermappene, slik som `en/1.webp`, `fr/1.webp`, `pt/1.webp`, osv.

Du har muligheten til å bruke forskjellige bildeformater som `jpeg`, `png`, eller `webp`. Det anbefales å velge `webp`-formatet slik at bildene blir mindre tunge.
![opplæring](assets/26.webp)
For å sette inn et diagram i dokumentet ditt, bruk følgende kommando i Markdown, og sørg for å spesifisere passende alternativ tekst og den korrekte banen til bildet:
```markdown
![spurv](assets/notext/1.webp)
```
Utropstegnet i begynnelsen indikerer at det er et bilde. Den alternative teksten, som hjelper med tilgjengelighet og SEO, er plassert mellom klammeparentesene. Til slutt er banen til bildet angitt mellom parentesene: ![opplæring](assets/27.webp)
Hvis du ønsker å lage dine egne diagrammer, sørg for å følge den grafiske charteren til PlanB Network for å sikre visuell konsistens:
- **Skrift**: Bruk [Rubik](https://fonts.google.com/specimen/Rubik);
- **Farger**:
	- Oransje: #FF5C00
	- Svart: #000000
	- Hvit: #FFFFFF

**Det er avgjørende at alle visuelle elementer integrert i opplæringene dine er royalty-frie eller overholder lisensen til kildefilen**. I tillegg er alle diagrammer publisert på PlanB Network tilgjengelig under CC-BY-SA-lisensen, på samme måte som teksten.

**-> Tips:** Når du deler filer offentlig, som bilder, er det viktig å fjerne all overflødig metadata. Dette kan inneholde sensitiv informasjon, som lokasjonsdata, opprettelsesdatoer, eller detaljer om forfatteren. For å beskytte ditt privatliv, er det tilrådelig å fjerne denne metadataen. For å forenkle denne operasjonen, kan du bruke spesialiserte verktøy som [Exif Cleaner](https://exifcleaner.com/), som tilbyr muligheten til å rense et dokuments metadata med en enkel dra-og-slipp.

### Hvordan lagre og pushe opplæringen?

Når du har fullført å skrive opplæringen din på språket du har valgt, er neste steg å sende inn en **Pull Request**. Administratoren vil deretter legge til de manglende oversettelsene av opplæringen din, takket være vår automatiserte oversettelsesmetode.

- For å fortsette med Pull Request, åpne GitHub Desktop-programvaren.
- Programvaren skal automatisk oppdage endringene du har gjort lokalt sammenlignet med det opprinnelige repositoriet. Før du fortsetter, sjekk nøye på venstre side av grensesnittet at disse endringene nøyaktig tilsvarer det du forventet: ![opplæring](assets/28.webp)
- Legg til en tittel for ditt commit, og klikk deretter på den blå `Commit to [your branch]`-knappen for å validere disse endringene: ![opplæring](assets/29.webp)
Et commit er en lagring av endringene gjort til grenen, ledsaget av en beskrivende melding, som tillater å følge evolusjonen av et prosjekt over tid. Det er altså en slags mellomliggende sjekkpunkt.
- Klikk deretter på `Push origin`-knappen. Dette vil sende din commit til din fork: ![tutorial](assets/30.webp)- Hvis du ikke har fullført opplæringen din, kan du komme tilbake til den senere og gjøre nye commits.
- Hvis du har fullført redigeringene for denne branchen, klikk nå på `Preview Pull Request`-knappen: ![tutorial](assets/31.webp)
- Du kan sjekke en siste gang at endringene dine er korrekte, og deretter klikke på `Create pull request`-knappen:
![tutorial](assets/32.webp)
En Pull Request er en forespørsel om å integrere endringene fra din branch til hovedbranchen til PlanB Network-repositoriet, som tillater gjennomgang og diskusjon av endringene før deres sammenslåing.

- Du vil automatisk bli omdirigert i nettleseren din til GitHub på forberedelsessiden for din Pull Request:
![tutorial](assets/33.webp)
- Oppgi en tittel som kort oppsummerer endringene du ønsker å slå sammen med kilde-repositoriet.
- Legg til en kort kommentar som beskriver disse endringene.
- Klikk på den grønne `Create pull request`-knappen for å bekrefte sammenslåingsforespørselen:
![tutorial](assets/34.webp)
Din PR vil da være synlig i `Pull Request`-fanen til hovedrepositoriet til PlanB Network. Alt du trenger å gjøre nå er å vente til en administrator kontakter deg for å bekrefte sammenslåingen av ditt bidrag eller for å be om eventuelle ytterligere endringer.
![tutorial](assets/35.webp)
Etter sammenslåingen av din PR med hovedbranchen, anbefales det å slette din arbeidsbranch (`tuto-sparrow-wallet`) for å opprettholde en ren historikk på din fork. GitHub vil automatisk tilby deg denne muligheten på siden til din PR:
![tutorial](assets/36.webp)
På GitHub Desktop-programvaren kan du bytte tilbake til hovedbranchen til din fork (`dev`).
![tutorial](assets/7.webp)
Hvis du ønsker å gjøre endringer i ditt bidrag etter å allerede ha sendt inn din PR, avhenger prosedyren du følger av den nåværende tilstanden til din PR:
- Hvis din PR fortsatt er åpen og ikke ennå har blitt sammenslått, utfør endringene lokalt mens du forblir på samme branch. Når endringene er ferdigstilt, bruk `Push origin`-knappen for å legge til en ny commit til din fortsatt åpne PR;
- I tilfelle der din PR allerede har blitt sammenslått med hovedbranchen, må du gjenta prosessen fra begynnelsen ved å opprette en ny branch, og deretter sende inn en ny PR. Sørg for at ditt lokale repositorium er synkronisert med kilde-repositoriet til PlanB Network før du fortsetter.