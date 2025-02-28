---
name: Legge til en bok i PlanB-nettverket
description: Hvordan legge til en ny bok i PlanB-nettverket?
---
![book](assets/cover.webp)

PlanB sitt oppdrag er å tilby førsteklasses utdanningsressurser om Bitcoin på så mange språk som mulig. Alt innhold publisert på nettstedet er åpen kildekode og hostet på GitHub, noe som gjør det mulig for hvem som helst å bidra til berikelsen av plattformen.

**Ønsker du å legge til en bok relatert til Bitcoin på PlanB-nettverkets side og øke synligheten av ditt arbeid, men vet ikke hvordan? Denne veiledningen er for deg!**
![book](assets/01.webp)
- Først må du ha en GitHub-konto. Hvis du ikke vet hvordan du oppretter en konto, har vi laget en detaljert veiledning for å veilede deg.

https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Gå til [GitHub-repositoriet til PlanB dedikert til data](https://github.com/DecouvreBitcoin/sovereign-university-data/tree/dev/resources/books) i `resources/books/`-seksjonen:
![book](assets/02.webp)
- Klikk øverst til høyre på `Add file`-knappen, deretter på `Create new file`:
![book](assets/03.webp)
- Hvis du aldri har bidratt til innholdet på PlanB-nettverket før, må du opprette din egen fork av det originale repositoriet. Å forke et repositorium betyr å lage en kopi av det repositoriet på din egen GitHub-konto, noe som gjør at du kan jobbe på prosjektet uten å påvirke det originale repositoriet. Klikk på `Fork this repository`-knappen:
![book](assets/04.webp)
- Du vil da komme til GitHub-redigeringssiden:
![book](assets/05.webp)
- Opprett en mappe for boken din. For å gjøre dette, skriv navnet på boken din i `Name your file...`-boksen, i små bokstaver med bindestreker i stedet for mellomrom. For eksempel, hvis boken din heter "*My Bitcoin Book*", bør du notere `my-bitcoin-book`:
![book](assets/06.webp)
- For å validere opprettelsen av mappen, legg ganske enkelt til en skråstrek etter boknavnet ditt i samme boks, for eksempel: `my-bitcoin-book/`. Å legge til en skråstrek oppretter automatisk en mappe i stedet for en fil:
![book](assets/07.webp)
- I denne mappen vil du opprette en første YAML-fil med navn `book.yml`:
![book](assets/08.webp)
- Fyll ut denne filen med informasjon om boken din ved å bruke denne malen:

```yaml
author: 
level: 
tags:
  - 
  - 
```

Her er detaljene du må fylle ut for hvert felt:
- **`author`**: Angi navnet på bokens forfatter.
- **`level`**: Angi det nødvendige nivået for å kunne lese og forstå boken godt. Velg et nivå blant følgende:
	- `beginner`
	- `intermediate`
- `advanced` - `expert`
- **`tags`**: Legg til to eller tre tagger relatert til boken din. For eksempel:
    - `bitcoin`
    - `history`
    - `technology`
    - `economy`
    - `education`...

For eksempel, din YAML-fil kunne se slik ut:

```yaml
author: Loïc Morel
level: beginner
tags:
  - bitcoin
  - technology
```

![book](assets/09.webp)
- Når du har fullført endringene i denne filen, lagre dem ved å klikke på `Commit changes...`-knappen:
![book](assets/10.webp)
- Legg til en tittel for endringene dine, samt en kort beskrivelse:
![bok](assets/11.webp)- Klikk på den grønne `Foreslå endringer`-knappen:
![bok](assets/12.webp)
- Du vil da komme til en side som oppsummerer alle endringene dine:
![bok](assets/13.webp)
- Klikk på GitHub-profilbildet ditt øverst til høyre, deretter på `Dine Repositories`:
![bok](assets/14.webp)
- Velg din fork av PlanB Network-repositoriet:
![bok](assets/15.webp)
- Du bør se en notifikasjon øverst i vinduet med din nye branch. Den heter sannsynligvis `patch-1`. Klikk på den:
![bok](assets/16.webp)
- Du er nå på din arbeidsbranch:
![bok](assets/17.webp)
- Gå tilbake til `resources/books/`-mappen og velg mappen til boken din som du nettopp opprettet i forrige commit:
![bok](assets/18.webp)
- I mappen til boken din, klikk på `Legg til fil`-knappen, deretter på `Opprett ny fil`:
![bok](assets/19.webp)
- Navngi denne nye mappen `assets` og bekreft opprettelsen ved å sette en skråstrek `/` på slutten:
![bok](assets/20.webp)
- I denne `assets`-mappen, opprett en fil med navn `.gitkeep`:
![bok](assets/21.webp)
- Klikk på `Bekreft endringer...`-knappen:
![bok](assets/22.webp)
- La commit-tittelen stå som standard, og sørg for at boksen `Bekreft direkte til patch-1-branchen` er merket av, deretter klikk på `Bekreft endringer`:
![bok](assets/23.webp)
- Gå tilbake til `assets`-mappen:
![bok](assets/24.webp)
- Klikk på `Legg til fil`-knappen, deretter på `Last opp filer`:
![bok](assets/25.webp)
- En ny side vil åpne seg. Dra og slipp omslagsbildet til boken din inn i området. Dette bildet vil bli vist på PlanB Network-nettstedet:
![bok](assets/26.webp)
- Vær forsiktig, bildet må være i formatet til en bok, for å best tilpasse seg nettstedet vårt, som for eksempel:
![bok](assets/27.webp)
- Når bildet er lastet opp, sørg for at boksen `Bekreft direkte til patch-1-branchen` er merket av, deretter klikk på `Bekreft endringer`:
![bok](assets/28.webp)- Vær oppmerksom på at bildet ditt må navngis `cover_en` hvis omslaget er på engelsk og må være i `.webp`-format. Derfor skal det komplette filnavnet være `cover_en.webp`, `cover_fr.webp`, `cover_it.webp`, osv. Hvis du ønsker å bruke et forskjellig omslagsbilde for hvert språk, for eksempel i tilfelle av en bokoversettelse, kan du plassere dem på samme sted i `assets`-mappen:
![bok](assets/29.webp)
- Gå tilbake til din `assets`-mappe og klikk på `.gitkeep` mellomfilen:
![bok](assets/30.webp)
- Når du er på filen, klikk på de 3 små prikkene øverst til høyre og deretter på `Slett fil`:
![bok](assets/31.webp)
- Sørg for at du fortsatt er på samme arbeidsbranch, deretter klikk på `Bekreft endringer...`-knappen:
![bok](assets/32.webp)
- Legg til en tittel og beskrivelse til din commit, deretter klikk på `Bekreft endringer`:
![bok](assets/33.webp)
- Gå tilbake til mappen til boken din:
![bok](assets/34.webp)
- Klikk på `Legg til fil`-knappen, deretter på `Opprett ny fil`: ![bok](assets/35.webp)
- Opprett en ny YAML-fil ved å navngi den med språkindikatoren for boken. Denne filen vil bli brukt for bokens beskrivelse. For eksempel, hvis jeg ønsker å skrive min beskrivelse på engelsk, vil jeg navngi denne filen `en.yml`:
![bok](assets/36.webp)
- Fyll ut denne YAML-filen ved å bruke denne malen:
```yaml
title: ""
publication_year: 
cover: cover_en.webp
original: true
description: |

contributors:
  - 
```

Her er detaljene du skal fylle inn for hvert felt:
- **`title`**: Angi navnet på boken i anførselstegn.
- **`publication_year`**: Angi året boken ble publisert.
- **`cover`**: Angi navnet på filen som tilsvarer omslagsbildet, i samsvar med språket til YAML-filen du for øyeblikket redigerer. For eksempel, hvis du redigerer `en.yml`-filen og du tidligere har lagt til det engelske omslagsbildet med tittelen `cover_en.webp`, bare angi `cover_en.webp` i dette feltet.
- **`description`**: Legg til et kort avsnitt som beskriver boken. Beskrivelsen må være på samme språk som angitt i tittelen på YAML-filen.
- **`contributors`**: Legg til ditt bidragsyter-ID hvis du har ett.

For eksempel, din YAML-fil kunne se slik ut:

```yaml
title: "Min Bitcoin Bok"
publication_year: 2021
cover: cover_en.webp
original: true
description: |
Oppdag den banebrytende verdenen av Bitcoin med denne omfattende guiden tilpasset for nybegynnere. Min Bitcoin Bok avmystifiserer kompleksitetene ved Bitcoin, og gir en klar og konsis introduksjon til hvordan protokollen fungerer. Fra dens revolusjonerende teknologi til dens potensielle innvirkning på den globale økonomien, tilbyr denne boken uvurderlige innsikter og praktisk kunnskap. Perfekt for de som er nye til Bitcoin, dekker den grunnleggende, sikkerhetstips, og fremtiden for digital finans. Dykk inn i fremtiden for penger og styrk deg selv med kunnskapen til å navigere den digitale tidsalderen med selvtillit.

contributors:
  - pretty-private

![bok](assets/37.webp)
- Klikk på `Bekreft endringer...`-knappen:
![bok](assets/38.webp)
- Sørg for at `Bekreft direkte til patch-1-grenen`-boksen er merket av, legg til en tittel, og klikk deretter på `Bekreft endringer`:
![bok](assets/39.webp)
- Bokmappen skal nå se slik ut:
![bok](assets/40.webp)
- Hvis alt ser bra ut for deg, gå tilbake til roten av din forgrening:
![bok](assets/41.webp)
- Du bør se en melding som indikerer at din gren har blitt endret. Klikk på `Sammenlign & be om trekk`-knappen:
![bok](assets/42.webp)
- Legg til en klar tittel og en beskrivelse til din PR:
![bok](assets/43.webp)
- Klikk på `Opprett trekkforespørsel`-knappen:
![bok](assets/44.webp)
Gratulerer! Din PR har blitt vellykket opprettet. En administrator vil nå gjennomgå den og, hvis alt er i orden, slå den sammen med hovedlageret til PlanB Network. Du bør se boken din dukke opp på nettstedet noen dager senere.

Sørg for å følge med på fremgangen til din PR. En administrator kan legge igjen en kommentar som ber om ytterligere informasjon. Så lenge din PR ikke er validert, kan du se den i `Trekkforespørsler`-fanen på PlanB Networks GitHub-lager:
![bok](assets/45.webp)
Tusen takk for ditt verdifulle bidrag! :)