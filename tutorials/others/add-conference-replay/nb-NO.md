---
name: Legge til en konferansegjentakelse
description: Hvordan legge til en konferansegjentakelse på PlanB Network?
---
![konferanse](assets/cover.webp)

PlanBs oppdrag er å tilby førsteklasses utdanningsressurser om Bitcoin på så mange språk som mulig. Alt innhold publisert på nettstedet er åpen kildekode og hostet på GitHub, noe som tillater hvem som helst å bidra til plattformens berikelse.

Ønsker du å legge til gjentakelsen av din Bitcoin-konferanse på PlanB Network-nettstedet og gi synlighet til dette arrangementet, men vet ikke hvordan? Denne veiledningen er for deg!

Hvis du derimot ønsker å legge til en konferanse som vil finne sted i fremtiden, anbefaler jeg deg å lese denne andre veiledningen der vi forklarer hvordan du legger til et nytt arrangement på nettstedet.

https://planb.network/tutorials/others/contribution/add-event-1d3df554-c2d8-4e93-853f-58f672c5e097


![konferanse](assets/01.webp)
- Først må du ha en konto på GitHub. Hvis du ikke vet hvordan du oppretter en konto, har vi laget en detaljert veiledning for å veilede deg.

https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Gå til [GitHub-repositoriet til PlanB dedikert til data](https://github.com/DecouvreBitcoin/sovereign-university-data/tree/dev/resources/conference) i `resources/conference/`-seksjonen:
![konferanse](assets/02.webp)
- Klikk øverst til høyre på `Add file`-knappen, deretter på `Create new file`:
![konferanse](assets/03.webp)
- Hvis du aldri har bidratt til innholdet på PlanB Network før, må du opprette din egen fork av det originale repositoriet. Å forke et repositorium betyr å lage en kopi av det repositoriet på din egen GitHub-konto, noe som lar deg jobbe på prosjektet uten å påvirke det originale repositoriet. Klikk på `Fork this repository`-knappen:
![konferanse](assets/04.webp)
- Du vil da komme til GitHub-redigeringssiden:
![konferanse](assets/05.webp)
- Opprett en mappe for din konferanse. For å gjøre dette, i `Name your file...`-boksen, skriv navnet på din konferanse med små bokstaver og bindestreker i stedet for mellomrom. For eksempel, hvis din konferanse kalles "Paris Bitcoin Conference", bør du notere `paris-bitcoin-conference`. Legg også til året for din konferanse, for eksempel: `paris-bitcoin-conference-2024`:
![konferanse](assets/06.webp)
- For å validere opprettelsen av mappen, noter rett og slett et skråstrek etter navnet ditt i samme boks, for eksempel: `paris-bitcoin-conference-2024/`. Å legge til et skråstrek oppretter automatisk en mappe i stedet for en fil:
![konferanse](assets/07.webp)
- I denne mappen vil du opprette en første YAML-fil med navn `conference.yml`:
![konferanse](assets/08.webp)
Fyll denne filen med informasjon relatert til din konferanse ved å bruke denne malen:
```yaml
year: 
name: 
builder: 
location: 
language: 
  - 
links:
  website: 
  twitter: 
tags: 
  - 
  - 
```

For eksempel, din YAML-fil kunne se slik ut:

```yaml
year: 2024-08
name: Paris Bitcoin Conference 2024
builder: Paris Bitcoin Conference
location: Paris, France
language: 
  - fr
  - en
links:
  website: https://paris.bitcoin.fr/conference
  twitter: https://twitter.com/ParisBitcoinConference
tags: 
  - International
  - All Public
```

![konferanse](assets/09.webp)
Hvis du ennå ikke har en "*builder*" identifikator for din organisasjon, kan du legge den til ved å følge denne andre opplæringen.
https://planb.network/tutorials/others/contribution/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

- Når du har fullført endringene i denne filen, lagre dem ved å klikke på `Commit changes...` knappen:
![konferanse](assets/10.webp)
- Legg til en tittel for endringene dine, samt en kort beskrivelse:
![konferanse](assets/11.webp)
- Klikk på den grønne `Propose changes` knappen:
![konferanse](assets/12.webp)
- Du vil da komme til en side som oppsummerer alle endringene dine:
![konferanse](assets/13.webp)
- Klikk på GitHub profilbildet ditt øverst til høyre, deretter på `Your Repositories`:
![konferanse](assets/14.webp)
- Velg din fork av PlanB Network repositoriet:
![konferanse](assets/15.webp)
- Du bør se en notifikasjon øverst i vinduet med din nye branch. Den heter sannsynligvis `patch-1`. Klikk på den:
![konferanse](assets/16.webp)
- Du er nå på din arbeidsbranch:
![konferanse](assets/17.webp)
- Gå tilbake til `resources/conference/` mappen og velg mappen til din konferanse som du nettopp opprettet i forrige commit:
![konferanse](assets/18.webp)
- I mappen til din konferanse, klikk på `Add file` knappen, deretter på `Create new file`:
![konferanse](assets/19.webp)
- Navngi denne nye mappen `assets` og bekreft opprettelsen ved å sette en skråstrek `/` på slutten:
![konferanse](assets/20.webp)
- I denne `assets` mappen, opprett en fil med navn `.gitkeep`:
![konferanse](assets/21.webp)
- Klikk på `Commit changes...` knappen:
![konferanse](assets/22.webp)
- La commit-tittelen stå som standard, og sørg for at `Commit directly to the patch-1 branch` boksen er merket av, deretter klikk på `Commit changes`:
![konferanse](assets/23.webp)
- Gå tilbake til `assets` mappen:
![konferanse](assets/24.webp)
- Klikk på `Add file` knappen, deretter på `Upload files`:
![konferanse](assets/25.webp)
- En ny side vil åpne seg. Dra og slipp et bilde som representerer din konferanse og som vil bli vist på PlanB Network nettstedet: ![konferanse](assets/26.webp)
- Det kan være en logo, et miniatyrbilde, eller til og med en plakat:
![konferanse](assets/27.webp)
- Når bildet er lastet opp, sjekk at `Commit directly to the patch-1 branch` boksen er merket av, deretter klikk på `Commit changes`:
![konferanse](assets/28.webp)
- Vær forsiktig, bildet ditt må navngis `thumbnail` og må være i `.webp` format. Det fullstendige filnavnet skal derfor være: `thumbnail.webp`:
![konferanse](assets/29.webp)
- Gå tilbake til din `assets` mappe og klikk på `.gitkeep` mellomfilen:
![konferanse](assets/30.webp)
- Når du er på filen, klikk på de 3 små prikkene i øvre høyre hjørne deretter på `Delete file`:
![konferanse](assets/31.webp)
- Verifiser at du fortsatt er på samme arbeidsbranch, deretter klikk på `Commit changes` knappen:
![konferanse](assets/32.webp)
- Legg til en tittel og en beskrivelse til din commit, deretter klikk på `Commit changes`:
![konferanse](assets/33.webp)
- Gå tilbake til konferansemappen din: ![conference](assets/34.webp)
- Klikk på `Legg til fil`-knappen, deretter på `Opprett ny fil`:
![conference](assets/35.webp)
- Opprett en ny markdown (.md) fil ved å navngi den med indikatoren for ditt morsmål. Denne filen vil bli brukt for opptakene av konferansen din. For eksempel, hvis jeg ønsker å skrive beskrivelsene av konferansene på engelsk, vil jeg navngi denne filen en.md:
![conference](assets/36.webp)
- Fyll ut denne markdown-filen ved å bruke denne malen som du kan tilpasse til konfigurasjonen av konferansen din:

```markdown
---
name: Paris Bitcoin Conference 2024
description: Den største Bitcoin-konferansen i Frankrike med over 8 000 deltakere hvert år!
--- 

# Hovedscene

## Fredag morgen

![video](https://youtu.be/XXXXXXXXXXXX)

## Fredag ettermiddag

![video](https://youtu.be/XXXXXXXXXXXX)

## Lørdag morgen

![video](https://youtu.be/XXXXXXXXXXXX)

## Lørdag ettermiddag

![video](https://youtu.be/XXXXXXXXXXXX)

# Workshoprom

## Fremtiden for Bitcoin Mining: Utfordringer og Innovasjoner

![video](https://youtu.be/XXXXXXXXXXXX)

Foredragsholder: Satoshi Nakamoto, Satoshi Nakamoto

## Er Personvern Fremdeles Mulig På Bitcoin?

![video](https://youtu.be/XXXXXXXXXXXX)

Foredragsholder: Satoshi Nakamoto

## Bitcoin Core: Dypdykk i Kodebasen

![video](https://youtu.be/XXXXXXXXXXXX)

Foredragsholder: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto

## Bygging og Sikring av Bitcoin Lommebøker Med Miniscript

![video](https://youtu.be/XXXXXXXXXXXX)

Foredragsholder: Satoshi Nakamoto
```

![conference](assets/37.webp)
- I begynnelsen av dokumentet ditt, i "front matter", fyll inn `name:`-feltet med navnet på konferansen din og året for opptakene. I `description:`-feltet, skriv en kort beskrivelse av arrangementet ditt på filens språk. For eksempel, for en fil med navn `en.md`, bør beskrivelsen være på engelsk. PlanB Network-teamet vil ta seg av å oversette beskrivelsen din ved hjelp av deres modell.
- Førstenivåstitler, markert med en `#`, brukes til å organisere konferansen etter scener. For eksempel, `# Hovedscene` for hovedscenen og `# Workshoprom` for en scene dedikert til workshops.

- Andre nivåstitler, markert med dobbelt `##`, brukes til å skille de forskjellige opptaksvideoene. Hvis konferansene ble filmet kontinuerlig over en halv dag, indiker, for eksempel, `## Fredag morgen`. Hvis konferansene ble filmet og kringkastet individuelt, navngi konferansen direkte med en andre nivåstittel.

- Under hver andre nivåstittel, sett inn en lenke til den tilsvarende opptaksvideoen. Syntaksen skal være: `![video](https://youtu.be/XXXXXXXXXXXX)`, og erstatte `XXXXXXXXXXXX` med den faktiske videolenken.

- Hvis formatet tillater det (individuelle konferanser), kan du legge til navnene på foredragsholderne. For å gjøre dette, legg til `Foredragsholder:`-feltet etterfulgt av navnet eller pseudonymet til foredragsholderen under videolenken. I tilfelle av flere foredragsholdere, skill hvert navn med et komma, slik for eksempel: `Foredragsholder: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto`.

---

- Når dine endringer til denne filen er fullført, lagre dem ved å klikke på `Bekreft endringer...`-knappen:
![conference](assets/38.webp)
- Legg til en tittel for dine endringer, samt en kort beskrivelse:
![conference](assets/39.webp)
- Klikk på `Commit changes`: ![conference](assets/40.webp)
- Konferansemappen din skal nå se slik ut:
![conference](assets/41.webp)
- Hvis alt er til din tilfredshet, gå tilbake til roten av din fork:
![conference](assets/42.webp)
- Du bør se en melding som indikerer at din branch har gjennomgått endringer. Klikk på `Compare & pull request`-knappen:
![conference](assets/43.webp)
- Legg til en klar tittel og beskrivelse for din PR:
![conference](assets/44.webp)
- Klikk på `Create pull request`-knappen:
![conference](assets/45.webp)
Gratulerer! Din PR har blitt opprettet. En administrator vil nå gjennomgå den og, hvis alt er i orden, flette den inn i hovedlageret til PlanB Network. Du bør se opptakene av konferansen din dukke opp på nettstedet noen dager senere.

Vennligst sørg for å følge med på fremgangen til din PR. Det er mulig at en administrator kan legge igjen en kommentar som ber om ytterligere informasjon. Så lenge din PR ikke er validert, kan du se den under `Pull requests`-fanen på PlanB Networks GitHub-repositorium:
![conference](assets/46.webp)

Tusen takk for ditt verdifulle bidrag! :)