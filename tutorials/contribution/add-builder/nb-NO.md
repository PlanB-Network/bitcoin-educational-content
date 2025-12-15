---
name: Legge til en Bygger
description: Hvordan foreslå å legge til en ny bygger på Plan ₿ Academy?
---
![project](assets/cover.webp)

PlanB's oppdrag er å tilby førsteklasses utdanningsressurser om Bitcoin, på så mange språk som mulig. Alt innhold publisert på nettstedet er åpen kildekode og hostet på GitHub, noe som lar hvem som helst delta i å berike plattformen.

Ønsker du å legge til en ny Bitcoin "bygger" på Plan ₿ Academy-nettstedet og gi synlighet til din bedrift eller programvare, men vet ikke hvordan? Denne veiledningen er for deg!
![project](assets/01.webp)
- Først må du ha en GitHub-konto. Hvis du ikke vet hvordan du oppretter en konto, har vi laget en detaljert veiledning for å veilede deg.

https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Gå til [GitHub-repositoriet til PlanB dedikert til data](https://github.com/DecouvreBitcoin/sovereign-university-data/tree/dev/resources/projects) i `resources/project/`-seksjonen:
![project](assets/02.webp)
- Klikk øverst til høyre på `Add file`-knappen, deretter på `Create new file`:
![project](assets/03.webp)
- Hvis du aldri har bidratt til innholdet på Plan ₿ Academy før, må du opprette din egen fork av det originale repositoriet. Å forke et repositorium betyr å lage en kopi av det repositoriet på din egen GitHub-konto, noe som lar deg jobbe på prosjektet uten å påvirke det originale repositoriet. Klikk på `Fork this repository`-knappen:
![project](assets/04.webp)
- Du vil da komme til GitHub-redigeringssiden:
![project](assets/05.webp)
- Opprett en mappe for din bedrift. For å gjøre dette, skriv navnet på bedriften din med små bokstaver og bindestreker i stedet for mellomrom i `Name your file...`-boksen. For eksempel, hvis bedriften din heter "Bitcoin Baguette", bør du skrive `bitcoin-baguette`:
![project](assets/06.webp)
- For å validere opprettelsen av mappen, legg ganske enkelt til en skråstrek etter navnet ditt i samme boks, for eksempel: `bitcoin-baguette/`. Å legge til en skråstrek oppretter automatisk en mappe i stedet for en fil:
![project](assets/07.webp)
- I denne mappen vil du opprette en første YAML-fil med navnet `project.yml`:
![project](assets/08.webp)
- Fyll denne filen med informasjon om bedriften din ved å bruke denne malen:

```yaml
name:

address_line_1:
address_line_2:
address_line_3: 

language:
  - 

links:
  website:
  twitter:
  Github:
  youtube:
  nostr:

tags:
  - 
  - 

category:
```

Her er hva du skal fylle inn for hver nøkkel:
- `name`: Navnet på bedriften din (obligatorisk);
- `address` : Bedriftens lokasjon (valgfritt);
- `language` : Landene bedriften din opererer i eller språkene som støttes (valgfritt);
- `links` : De ulike offisielle lenkene til bedriften din (valgfritt);
- `tags` : 2 termer som kvalifiserer bedriften din (obligatorisk);
- `category` : Kategorien som best beskriver feltet bedriften din opererer innenfor blant følgende valg:
	- `wallet`,
	- `infrastructure`,
	- `exchange`,
	- `education`,
	- `service`,
	- `communities`,
	- `conference`,
	- `privacy`,
	- `investment`,
	- `node`,
	- `mining`,
	- `news`,
	- `manufacturer`.
For eksempel kan din YAML-fil se slik ut:
```yaml
name: Bitcoin Baguette

address_line_1: Paris, Frankrike
address_line_2:
address_line_3: 

language:
  - fr
  - en

links:
  website: https://bitcoin-baguette.com
  twitter: https://twitter.com/bitcoinbaguette
  Github:
  youtube:
  nostr:

tags:
  - bitcoin
  - utdanning

category: utdanning
```

![project](assets/09.webp)
- Når du har gjort endringer i denne filen, lagre dem ved å klikke på `Commit changes...`-knappen:
![project](assets/10.webp)
- Legg til en tittel for endringene dine, sammen med en kort beskrivelse:
![project](assets/11.webp)
- Klikk på den grønne `Propose changes`-knappen:
![project](assets/12.webp)
- Du vil da komme til en side som oppsummerer alle endringene dine:
![project](assets/13.webp)
- Klikk på GitHub-profilbildet ditt øverst til høyre, deretter på `Your Repositories`:
![project](assets/14.webp)
- Velg din fork av Plan ₿ Academy-repositoriet:
![project](assets/15.webp)
- Du bør se en notifikasjon øverst i vinduet med din nye branch. Den heter sannsynligvis `patch-1`. Klikk på den:
![project](assets/16.webp)
- Du er nå på din arbeidsbranch (**sørg for at du er på samme branch som dine tidligere modifikasjoner, dette er viktig!**):
![project](assets/17.webp)
- Gå tilbake til `resources/projects/`-mappen og velg mappen til din virksomhet som du nettopp opprettet i den forrige commiten:
![project](assets/18.webp)
- I mappen til din virksomhet, klikk på `Add file`-knappen, deretter på `Create new file`:
![project](assets/19.webp)
- Navngi denne nye mappen `assets` og bekreft opprettelsen ved å sette en skråstrek `/` på slutten:
![project](assets/20.webp)
- I denne `assets`-mappen, opprett en fil med navn `.gitkeep`:
![project](assets/21.webp)
- Klikk på `Commit changes...`-knappen:
![project](assets/22.webp)
- La commit-tittelen være som standard, og sørg for at `Commit directly to the patch-1 branch`-boksen er merket av, deretter klikk på `Commit changes`: ![project](assets/23.webp)
- Gå tilbake til `assets`-mappen:
![project](assets/24.webp)
- Klikk på `Add file`-knappen, deretter på `Upload files`:
![project](assets/25.webp)
- En ny side vil åpne seg. Dra og slipp et bilde av din bedrift eller ditt programvare inn i området. Dette bildet vil bli vist på Plan ₿ Academy-nettstedet:
![project](assets/26.webp)
- Det kan være logoen eller et ikon:
![project](assets/27.webp)
- Når bildet er lastet opp, verifiser at `Commit directly to the patch-1 branch`-boksen er merket av, deretter klikk på `Commit changes`:
![project](assets/28.webp)
- Vær forsiktig, bildet ditt må være kvadratisk, må være navngitt `logo`, og må være i `.webp`-format. Det fullstendige filnavnet skal derfor være: `logo.webp`:
![project](assets/29.webp)
- Gå tilbake til din `assets`-mappe og klikk på `.gitkeep` mellomfilen:
![project](assets/30.webp)- Når du er på filen, klikk på de tre små prikkene øverst til høyre og deretter på `Slett fil`:
![project](assets/31.webp)
- Sjekk at du fortsatt er på samme arbeidsgren, og klikk deretter på `Bekreft endringer`-knappen:
![project](assets/32.webp)
- Legg til en tittel og en beskrivelse på din commit, og klikk deretter på `Bekreft endringer`:
![project](assets/33.webp)
- Gå tilbake til mappen til selskapet ditt:
![project](assets/34.webp)
- Klikk på `Legg til fil`-knappen, og deretter på `Opprett ny fil`:
![project](assets/35.webp)
- Opprett en ny YAML-fil ved å navngi den med indikatoren for ditt morsmål. Denne filen vil bli brukt for beskrivelsen av byggeren. For eksempel, hvis jeg ønsker å skrive min beskrivelse på engelsk, vil jeg navngi denne filen `en.yml`:
![project](assets/36.webp)
- Fyll ut denne YAML-filen ved å bruke denne malen:
```yaml
description: |
 
contributors:
 - 
```

- For `contributors`-nøkkelen, kan du legge til din bidragsyteridentifikator til Plan ₿ Academy hvis du har en. Hvis ikke, la dette feltet stå tomt.
- For `description`-nøkkelen, trenger du bare å legge til et kort avsnitt som beskriver ditt selskap eller din programvare. Beskrivelsen må være på samme språk som filnavnet. Du trenger ikke å oversette denne beskrivelsen til alle språkene som støttes på nettstedet, ettersom PlanB-teamene vil gjøre dette ved hjelp av deres modell. For eksempel, her er hvordan filen din kunne se ut:
```yaml
description: |
Grunnlagt i 2017, er Bitcoin Baguette en Paris-basert forening dedikert til å organisere Bitcoin-møter og tekniske workshops. Vi samler entusiaster, eksperter og nysgjerrige sinn for å utforske og diskutere Bitcoin-teknologiens intrikatesser. Våre arrangementer tilbyr en plattform for kunnskapsdeling, nettverksbygging og fremme en dypere forståelse av Bitcoins indre virkemåte. Bli med oss i Bitcoin Baguette for å være en del av Paris' Bitcoin-samfunn og holde deg oppdatert med de siste fremskrittene innen feltet.

contributors:
- 
```
![project](assets/37.webp)
- Klikk på `Bekreft endringer`-knappen:
![project](assets/38.webp)
- Sørg for at `Bekreft direkte til patch-1-grenen`-boksen er merket av, legg til en tittel, og klikk deretter på `Bekreft endringer`:
![project](assets/39.webp)
- Mappen til selskapet ditt bør nå se slik ut:
![project](assets/40.webp)
- Hvis alt er til din tilfredshet, gå tilbake til roten av din fork:
![project](assets/41.webp)
- Du bør se en melding som indikerer at din gren har gjennomgått endringer. Klikk på `Sammenlign & be om sammenslåing`-knappen:
![project](assets/42.webp)
- Legg til en klar tittel og beskrivelse til din PR:
![project](assets/43.webp)
- Klikk på `Opprett pull request`-knappen:
![project](assets/44.webp)
Gratulerer! Din PR har blitt vellykket opprettet. En administrator vil nå gjennomgå den og, hvis alt er i orden, integrere den i hovedlageret til Plan ₿ Academy. Du bør se din byggerprofil dukke opp på nettstedet noen dager senere.

Sørg for å følge med på fremgangen til din PR. En administrator kan legge igjen en kommentar som ber om ytterligere informasjon. Så lenge din PR ikke er validert, kan du konsultere den i `Pull requests`-fanen på Plan ₿ Academy GitHub-lageret:
![project](assets/45.webp)
Tusen takk for ditt verdifulle bidrag! :)
