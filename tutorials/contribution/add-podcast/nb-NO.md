---
name: Legge til en Podcast i PlanB Nettverk
description: Hvordan legge til en ny podcast i PlanB Nettverk?
---
![podcast](assets/cover.webp)

PlanBs oppdrag er å tilby førsteklasses pedagogiske ressurser om Bitcoin på så mange språk som mulig. Alt innhold publisert på nettstedet er åpen kildekode og hostet på GitHub, noe som tillater hvem som helst å delta i å berike plattformen.

Ser du etter å legge til en Bitcoin-podcast på PlanB Nettverk-siden og øke synligheten for showet ditt, men vet ikke hvordan? Denne veiledningen er for deg!
![podcast](assets/01.webp)
- Først må du ha en GitHub-konto. Hvis du ikke vet hvordan du oppretter en, har vi laget en detaljert veiledning for å veilede deg.

https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Gå til [GitHub-repositoriet til PlanB dedikert til data](https://github.com/DecouvreBitcoin/sovereign-university-data/tree/dev/resources/podcasts) i `resources/podcasts/`-seksjonen:
![podcast](assets/02.webp)
- Klikk øverst til høyre på `Add file`-knappen, deretter på `Create new file`:
![podcast](assets/03.webp)
- Hvis du aldri har bidratt til innholdet på PlanB Nettverk før, må du opprette din egen fork av det originale repositoriet. Å forke et repositorium betyr å lage en kopi av det repositoriet på din egen GitHub-konto, noe som tillater deg å jobbe på prosjektet uten å påvirke det originale repositoriet. Klikk på `Fork this repository`-knappen:
![podcast](assets/04.webp)
- Du vil da komme til GitHub-redigeringssiden:
![podcast](assets/05.webp)
- Opprett en mappe for din podcast. For å gjøre dette, i `Name your file...`-boksen, skriv navnet på din podcast med små bokstaver og bindestreker istedenfor mellomrom. For eksempel, hvis showet ditt heter "Super Podcast Bitcoin", bør du skrive `super-podcast-bitcoin`:
![podcast](assets/06.webp)
- For å validere opprettelsen av mappen, legg ganske enkelt til en skråstrek etter navnet på podcasten din i samme boks, for eksempel: `super-podcast-bitcoin/`. Å legge til en skråstrek oppretter automatisk en mappe i stedet for en fil:
![podcast](assets/07.webp)
- I denne mappen vil du opprette en første YAML-fil med navnet `podcast.yml`:
![podcast](assets/08.webp)
- Fyll ut denne filen med informasjon om din podcast ved å bruke denne malen:

```yaml
name: 
host: 
language: 
links:
  podcast: 
  twitter: 
  website: 
description: |
  
tags:
  - 
  - 
contributors:
  - 
```

Her er detaljene du må fylle ut for hvert felt:

- **`name`**: Angi navnet på podcasten din.
- **`host`**: List opp navnene eller pseudonymene til talerne eller verten for podcasten. Hvert navn skal være adskilt med et komma.
- **`language`**: Angi språkkoden for språket som snakkes i podcasten din. For eksempel, for engelsk, noter `en`, for italiensk `it`...

- **`links`**: Oppgi lenker til innholdet ditt. Du har to alternativer:
	- `podcast`: lenken til podcasten din,
	- `twitter`: lenken til Twitter-profilen til podcasten eller organisasjonen som produserer den,
	- `website`: lenken til nettstedet til podcasten eller organisasjonen som produserer den.
```yaml
name: Super Podcast Bitcoin
host: Rogzy, JohnOnChain, Lounes, Fanis, Ajlex, Guillaume, Pantamis, Sosthene, Loic
language: en
links:
  podcast: https://podcasts.apple.com/us/podcast/decouvrebitcoin-replay/id1693844092
  twitter: https://twitter.com/decouvrebitcoin
  website: https://decouvrebitcoin.fr
description: |
  Super Podcast Bitcoin er en teknisk LIVE-sesjon som holdes en gang i uken på Twitter for å dykke dypt inn i Bitcoin-protokollen, løsninger på lag to, og alt annet som blåser hodet av deg. Våre verter Lounes, Pantamis, Loïc og Sosthene vil svare på spørsmålene dine og tilby det mest tekniske showet om Bitcoin i verden.

tags:
  - bitcoin
  - teknologi
contributors:
  - rabbit-hole
```

![podcast](assets/09.webp)

- Når du har fullført endringene i denne filen, lagre dem ved å klikke på `Commit changes...`-knappen:
![podcast](assets/10.webp)
- Legg til en tittel for endringene dine, samt en kort beskrivelse:
![podcast](assets/11.webp)
- Klikk på den grønne `Propose changes`-knappen:
![podcast](assets/12.webp)
- Du vil da komme til en side som oppsummerer alle endringene dine:
![podcast](assets/13.webp)
- Klikk på GitHub-profilbildet ditt øverst til høyre, deretter på `Your Repositories`:
![podcast](assets/14.webp)
- Velg din fork av PlanB Network-repositoriet:
![podcast](assets/15.webp)
- Du bør se en notifikasjon øverst i vinduet med din nye branch. Den heter sannsynligvis `patch-1`. Klikk på den:
![podcast](assets/16.webp)
- Du er nå på din arbeidsbranch:
![podcast](assets/17.webp)
- Gå tilbake til `resources/podcast/`-mappen og velg podcast-mappen du nettopp opprettet i forrige commit: ![podcast](assets/18.webp)
- I podcast-mappen din, klikk på `Add file`-knappen, deretter på `Create new file`:
![podcast](assets/19.webp)
- Navngi denne nye mappen `assets` og bekreft opprettelsen ved å legge til en skråstrek `/` på slutten:
![podcast](assets/20.webp)
- I denne `assets`-mappen, opprett en fil med navn `.gitkeep`:
![podcast](assets/21.webp)
- Klikk på `Commit changes...`-knappen:
![podcast](assets/22.webp)
- La commit-tittelen være som standard, og sørg for at boksen `Commit directly to the patch-1 branch` er merket av, deretter klikk på `Commit changes`:
![podcast](assets/23.webp)
- Gå tilbake til `assets`-mappen:
![podcast](assets/24.webp)
- Klikk på `Add file`-knappen, deretter på `Upload files`:
![podcast](assets/25.webp)
- En ny side vil åpne seg. Dra og slipp podcast-logoen din inn i området. Dette bildet vil bli vist på PlanB Network-nettstedet: ![podcast](assets/26.webp)
- Vær forsiktig, bildet må være kvadratisk for å passe best på vår nettside: ![podcast](assets/27.webp)
- Når bildet er lastet opp, verifiser at `Commit directly to the patch-1 branch`-boksen er krysset av, deretter klikk på `Commit changes`: ![podcast](assets/28.webp)
- Vær forsiktig, bildet ditt må være navngitt `logo` og må være i `.webp`-format. Det fullstendige filnavnet skal derfor være: `logo.webp`: ![podcast](assets/29.webp)
- Gå tilbake til din `assets`-mappe og klikk på den mellomliggende filen `.gitkeep`: ![podcast](assets/30.webp)
- Når du er på filen, klikk på de tre små prikkene øverst til høyre og deretter på `Delete file`: ![podcast](assets/31.webp)
- Verifiser at du fortsatt er på samme arbeidsgren, deretter klikk på `Commit changes`-knappen: ![podcast](assets/32.webp)
- Legg til en tittel og beskrivelse til ditt commit, deretter klikk på `Commit changes`: ![podcast](assets/33.webp)
- Gå tilbake til roten av ditt repositorium: ![podcast](assets/34.webp)
- Du bør se en melding som indikerer at din gren har gjennomgått endringer. Klikk på `Compare & pull request`-knappen: ![podcast](assets/35.webp)
- Legg til en klar tittel og beskrivelse til din PR: ![podcast](assets/36.webp)
- Klikk på `Create pull request`-knappen: ![podcast](assets/37.webp)
Gratulerer! Din PR har blitt opprettet med suksess. En administrator vil nå gjennomgå den og, hvis alt er i orden, flette den inn i hovedrepositoriet til PlanB Network. Du bør se din podcast dukke opp på nettstedet noen dager senere.

Vennligst sørg for å følge med på fremgangen til din PR. En administrator kan legge igjen en kommentar som ber om ytterligere informasjon. Så lenge din PR ikke er validert, kan du se den i `Pull requests`-fanen på PlanB Network GitHub-repositoriet: ![podcast](assets/38.webp)
Tusen takk for ditt verdifulle bidrag! :)