---
name: Legg til et arrangement på PlanB Network
description: Hvordan foreslår jeg å legge til en ny hendelse på PlanB Network?
---
![event](assets/cover.webp)

PlanBs oppdrag er å tilby førsteklasses utdanningsressurser om Bitcoin på så mange språk som mulig. Alt innhold som publiseres på nettstedet er åpen kildekode og hostet på GitHub, noe som gir alle muligheten til å bidra til berikelsen av plattformen.

Ønsker du å legge til en Bitcoin-konferanse på PlanB Network-siden og øke synligheten for ditt arrangement, men vet ikke hvordan? Denne veiledningen er for deg!
![event](assets/01.webp)
- Først må du ha en konto på GitHub. Hvis du ikke vet hvordan du oppretter en konto, har vi laget en detaljert veiledning for å veilede deg.

https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Gå til [GitHub-repositoriet til PlanB dedikert til data](https://github.com/DecouvreBitcoin/sovereign-university-data/tree/dev/resources/conference) i `resources/conference/`-delen:
![event](assets/02.webp)
- Klikk øverst til høyre på `Add file`-knappen, deretter på `Create new file`:
![event](assets/03.webp)
- Hvis du aldri har bidratt til innholdet på PlanB Network før, må du opprette din egen fork av det originale repositoriet. Å forke et repositorium betyr å lage en kopi av det repositoriet på din egen GitHub-konto, noe som lar deg jobbe på prosjektet uten å påvirke det originale repositoriet. Klikk på `Fork this repository`-knappen:
![event](assets/04.webp)
- Du vil da komme til GitHub-redigeringssiden:
![event](assets/05.webp)
- Opprett en mappe for din konferanse. For å gjøre dette, i `Name your file...`-boksen, skriv navnet på konferansen din med små bokstaver og bindestreker i stedet for mellomrom. For eksempel, hvis konferansen din heter "Paris Bitcoin Conference", bør du notere `paris-bitcoin-conference`. Legg også til året for konferansen din, for eksempel: `paris-bitcoin-conference-2024`:
![event](assets/06.webp)
- For å validere opprettelsen av mappen, noter rett og slett et skråstrek etter navnet ditt i samme boks, for eksempel: `paris-bitcoin-conference-2024/`. Å legge til et skråstrek oppretter automatisk en mappe i stedet for en fil:
![event](assets/07.webp)
- I denne mappen vil du opprette en første YAML-fil med navnet `events.yml`:
![event](assets/08.webp)
- Fyll denne filen med informasjon om konferansen din ved å bruke denne malen:

```yaml
- start_date:
  end_date:
  address_line_1:
  address_line_2: 
  address_line_3: 
  name:
  builder:
  type: conference
  book_online: false
  book_in_person: false
  price_dollars: 0
  description:
  language: 
    - 
  links:
    website:
    replay_url:    
    live_url :
  tags: 
    - 
```

For eksempel, din YAML-fil kunne se slik ut:

```yaml
- start_date: 2024-08-15
  end_date: 2024-08-18
  address_line_1: Paris, Frankrike
  address_line_2: 
  address_line_3: 
  name: Paris Bitcoin Conference 2024
  builder: Paris Bitcoin Conference
  type: conference
  book_online: false
  book_in_person: false
  price_dollars: 0
```yaml
description: Den største Bitcoin-konferansen i Frankrike med over 8 000 deltakere hvert år!
language:
    - fr
    - en
    - es
    - it
links:
    website: https://paris.bitcoin.fr/conference
    replay_url:
    live_url:
tags:
    - Bitcoiner
    - Generell
    - Internasjonal
```
![event](assets/09.webp)
Hvis du ennå ikke har en "*builder*" identifikator for din organisasjon, kan du legge den til ved å følge denne andre opplæringen.

https://planb.network/tutorials/others/contribution/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

- Når du har fullført endringene i denne filen, lagre dem ved å klikke på `Commit changes...` knappen:
![event](assets/10.webp)
- Legg til en tittel for endringene dine, samt en kort beskrivelse:
![event](assets/11.webp)
- Klikk på den grønne `Propose changes` knappen:
![event](assets/12.webp)
- Du vil da komme til en side som oppsummerer alle endringene dine:
![event](assets/13.webp)
- Klikk på GitHub-profilbildet ditt øverst til høyre, deretter på `Your Repositories`:
![event](assets/14.webp)
- Velg din fork av PlanB Network-repositoriet:
![event](assets/15.webp)
- Du bør se en notifikasjon øverst i vinduet med din nye branch. Den heter sannsynligvis `patch-1`. Klikk på den:
![event](assets/16.webp)
- Du er nå på din arbeidsbranch:
![event](assets/17.webp)
- Gå tilbake til `resources/conference/` mappen og velg mappen til din konferanse som du nettopp opprettet i forrige commit:
![event](assets/18.webp)
- I mappen til din konferanse, klikk på `Add file` knappen, deretter på `Create new file`:
![event](assets/19.webp)
- Navngi denne nye mappen `assets` og bekreft opprettelsen ved å sette en skråstrek `/` på slutten:
![event](assets/20.webp)
- I denne `assets` mappen, opprett en fil med navn `.gitkeep`:
![event](assets/21.webp)
- Klikk på `Commit changes...` knappen:
![event](assets/22.webp)
- La commit-tittelen være som standard, og sørg for at `Commit directly to the patch-1 branch` boksen er merket av, deretter klikk på `Commit changes`:
![event](assets/23.webp)
- Gå tilbake til `assets` mappen:
![event](assets/24.webp)
- Klikk på `Add file` knappen, deretter på `Upload files`: ![event](assets/25.webp)
- En ny side vil åpne seg. Dra og slipp et bilde som representerer din konferanse og som vil bli vist på PlanB Network-siden:
![event](assets/26.webp)
- Det kan være en logo, et miniatyrbilde, eller til og med en plakat:
![event](assets/27.webp)
- Når bildet er lastet opp, sjekk at `Commit directly to the patch-1 branch` boksen er merket av, deretter klikk på `Commit changes`:
![event](assets/28.webp)
- Vær forsiktig, bildet ditt må være navngitt `thumbnail` og må være i `.webp` format. Det fullstendige filnavnet skal derfor være: `thumbnail.webp`:
![event](assets/29.webp)
- Gå tilbake til din `assets` mappe og klikk på mellomfilen `.gitkeep`:
![event](assets/30.webp)
- Når du er på filen, klikk på de 3 små prikkene øverst til høyre og deretter på `Slett fil`: ![event](assets/31.webp)
- Verifiser at du fortsatt er på samme arbeidsgren, og klikk deretter på `Bekreft endringer`-knappen:
![event](assets/32.webp)
- Legg til en tittel og en beskrivelse til din commit, og klikk deretter på `Bekreft endringer`:
![event](assets/33.webp)
- Gå tilbake til roten av ditt repositorium:
![event](assets/34.webp)
- Du bør se en melding som indikerer at din gren har gjennomgått endringer. Klikk på `Sammenlign & forespør pull`-knappen:
![event](assets/35.webp)
- Legg til en klar tittel og en beskrivelse til din PR:
![event](assets/36.webp)
- Klikk på `Opprett pull forespørsel`-knappen:
![event](assets/37.webp)
Gratulerer! Din PR har blitt vellykket opprettet. En administrator vil nå sjekke den og, hvis alt er i orden, slå den sammen med hovedrepositoriet til PlanB Network. Du bør se ditt arrangement dukke opp på nettsiden noen dager senere.

Sørg for å følge med på fremgangen til din PR. En administrator kan legge igjen en kommentar som ber om ytterligere informasjon. Så lenge din PR ikke er validert, kan du konsultere den i `Pull requests`-fanen på PlanB Network GitHub-repositoriet:
![event](assets/38.webp)
Tusen takk for ditt verdifulle bidrag! :)