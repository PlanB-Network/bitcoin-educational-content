---
name: Legge til Utdanningsverktøy
description: Hvordan legge til nye utdanningsmaterialer på PlanB Network?
---
![event](assets/cover.webp)

PlanBs oppdrag er å tilby ledende utdanningsressurser om Bitcoin, på så mange språk som mulig. Alt innhold publisert på nettstedet er åpen kildekode og hostet på GitHub, noe som lar hvem som helst delta i å berike plattformen.

Utover veiledninger og opplæring, tilbyr PlanB Network også et stort bibliotek av variert utdanningsinnhold om Bitcoin, tilgjengelig for alle, [i "BET" (_Bitcoin Educational Toolkit_) seksjonen](https://planb.network/resources/bet). Denne databasen inkluderer utdanningsplakater, memes, humoristiske propaganda plakater, tekniske diagrammer, logoer og andre verktøy for brukere. Målet med dette initiativet er å støtte enkeltpersoner og samfunn som underviser i Bitcoin rundt om i verden ved å gi dem de nødvendige visuelle ressursene.

Vil du delta i å berike denne databasen, men vet ikke hvordan? Denne veiledningen er for deg!

*Det er avgjørende at alt innhold integrert på nettstedet er fri for rettigheter eller respekterer lisensen til kildefilen. Også, alle visuelle publisert på PlanB Network er gjort tilgjengelig under [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) lisensen.*
![event](assets/01.webp)
- Først må du ha en konto på GitHub. Hvis du ikke vet hvordan du oppretter en konto, har vi laget en detaljert veiledning for å veilede deg.

https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Gå til [GitHub-repositoriet til PlanB dedikert til data](https://github.com/DecouvreBitcoin/sovereign-university-data/tree/dev/resources/bet) i `resources/bet/` seksjonen:
![event](assets/02.webp)
- Klikk øverst til høyre på `Add file` knappen, deretter på `Create new file`:
![event](assets/03.webp)
- Hvis du aldri har bidratt til innholdet på PlanB Network før, må du opprette din egen fork av det originale repositoriet. Å forke et repositorium betyr å lage en kopi av det repositoriet på din egen GitHub-konto, noe som lar deg jobbe på prosjektet uten å påvirke det originale repositoriet. Klikk på `Fork this repository` knappen:
![event](assets/04.webp)
- Du vil da komme til GitHub-redigeringssiden:
![event](assets/05.webp)
- Opprett en mappe for ditt innhold. For å gjøre dette, i `Name your file...` boksen, skriv navnet på ditt innhold med små bokstaver og bindestreker istedenfor mellomrom. I mitt eksempel, la oss si at jeg vil legge til en PDF-visuell av 2048-ords BIP39-listen. Så, jeg vil kalle mappen min `bip39-wordlist`: ![event](assets/06.webp)
- For å bekrefte opprettelsen av mappen, legg ganske enkelt til en skråstrek etter navnet i samme boks, for eksempel: `bip39-wordlist/`. Å legge til en skråstrek oppretter automatisk en mappe i stedet for en fil:
![event](assets/07.webp)
- I denne mappen vil du opprette en første YAML-fil med navn `bet.yml`:
![event](assets/08.webp)
- Fyll denne filen med informasjon relatert til ditt innhold ved å bruke denne malen:

```yaml
builder: 
type: 
links:
  download: 
  view: 
    - en: 
tags:
  - 
  - 
contributors:
  - 
```

Her er detaljene du må fylle ut for hvert felt:
```yaml
builder: Indiker din organisasjons identifikator på PlanB Network. Hvis du ikke allerede har en "builder" identifikator for ditt firma, kan du opprette en ved å følge denne veiledningen.
https://planb.network/tutorials/others/contribution/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

Hvis du ikke har en, kan du enkelt bruke ditt navn, ditt pseudonym, eller navnet på din bedrift uten å ha opprettet en builder-profil.

type: Velg naturen til ditt innhold blant de følgende to alternativene:
  - `Educational Content` for utdanningsinnhold.
  - `Visual Content` for andre typer diverse innhold.

links: Oppgi lenker til ditt innhold. Du har to alternativer:
  - Hvis du velger å hoste ditt innhold direkte på PlanBs GitHub, vil du trenge å legge til lenkene til denne filen i de følgende stegene.
  - Hvis ditt innhold er hostet andre steder, som på din personlige nettside, indiker de tilsvarende lenkene her:
      - `download`: En lenke for å laste ned ditt innhold.
      - `view`: En lenke for å se ditt innhold (kan være den samme som nedlastingslenken). Hvis ditt innhold er tilgjengelig på flere språk, legg til en lenke for hvert språk.

tags: Legg til to tags assosiert med ditt innhold. Eksempler:
  - bitcoin
  - teknologi
  - økonomi
  - utdanning
  - meme...

contributors: Nevn din bidragsyter identifikator hvis du har en.

For eksempel, din YAML-fil kunne se slik ut:

```yaml
builder: DecouvreBitcoin
type: Educational Content
links:
  download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
  view:
- I mitt eksempel, vil jeg la lenkene være tomme for nå, ettersom jeg vil legge til min PDF direkte på GitHub:
![event](assets/09.webp)
- Når dine modifikasjoner til denne filen er fullført, lagre dem ved å klikke på `Commit changes...` knappen:
![event](assets/10.webp)
- Legg til en tittel for dine modifikasjoner, samt en kort beskrivelse:
![event](assets/11.webp)
- Klikk på den grønne `Propose changes` knappen:
![event](assets/12.webp)
- Du vil da ankomme på en side som oppsummerer alle dine endringer:
![event](assets/13.webp)
- Klikk på ditt GitHub profilbilde øverst til høyre, deretter på `Your Repositories`:
![event](assets/14.webp)
- Velg din fork av PlanB Network repositoriet:
![event](assets/15.webp)
- Du burde se en notifikasjon på toppen av vinduet med din nye branch. Den er sannsynligvis kalt `patch-1`. Klikk på den:
![event](assets/16.webp)
- Du er nå på din arbeidsbranch (**sørg for at du er på samme branch som dine tidligere modifikasjoner, dette er viktig!**):
![event](assets/17.webp)
- Gå tilbake til `resources/bet/` mappen og velg mappen til ditt innhold som du nettopp opprettet i den forrige commiten:
![event](assets/18.webp)
- I mappen til ditt innhold, klikk på `Add file` knappen, deretter på `Create new file`:
![event](assets/19.webp)
- Navngi denne nye mappen `assets` og bekreft dens opprettelse ved å sette en skråstrek `/` på slutten:
![event](assets/20.webp)
- I denne `assets` mappen, opprett en fil navngitt `.gitkeep`: ![event](assets/21.webp)
```
- Klikk på `Commit changes...`-knappen: ![event](assets/22.webp)- La commit-tittelen stå som standard, og sørg for at `Commit directly to the patch-1 branch`-boksen er merket av, deretter klikker du på `Commit changes`: ![event](assets/23.webp)
- Gå tilbake til `assets`-mappen: ![event](assets/24.webp)
- Klikk på `Add file`-knappen, deretter på `Upload files`: ![event](assets/25.webp)
- En ny side vil åpne seg. Dra og slipp et miniatyrbilde som representerer innholdet ditt inn i området. Dette bildet vil bli vist på PlanB Network-siden: ![event](assets/26.webp)
- Det kan være en forhåndsvisning, en logo, eller et ikon: ![event](assets/27.webp)
- Når bildet er lastet opp, sørg for at `Commit directly to the patch-1 branch`-boksen er merket av, deretter klikker du på `Commit changes`: ![event](assets/28.webp)
- Vær forsiktig, bildet ditt må være navngitt `logo` og må være i `.webp`-format. Det fullstendige filnavnet skal derfor være: `logo.webp`: ![event](assets/29.webp)
- Gå tilbake til din `assets`-mappe og klikk på den mellomliggende filen `.gitkeep`: ![event](assets/30.webp)
- Når du er på filen, klikk på de tre små prikkene øverst til høyre deretter på `Delete file`: ![event](assets/31.webp)
- Sørg for at du fortsatt er på samme arbeidsgren, deretter klikker du på `Commit changes`-knappen: ![event](assets/32.webp)
- Legg til en tittel og en beskrivelse til din commit, deretter klikker du på `Commit changes`: ![event](assets/33.webp)
- Gå tilbake til mappen for ditt innhold: ![event](assets/34.webp)
- Klikk på `Add file`-knappen, deretter på `Create new file`: ![event](assets/35.webp)
- Opprett en ny YAML-fil ved å navngi den med indikatoren for ditt morsmål. Denne filen vil bli brukt for innholdsbeskrivelsen. For eksempel, hvis jeg ønsker å skrive min beskrivelse på engelsk, vil jeg navngi denne filen `en.yml`: ![event](assets/36.webp)
- Fyll ut denne YAML-filen ved å bruke denne malen:

```yaml
name: 
description: |
  
```

- For `name`-nøkkelen, kan du legge til navnet på innholdet ditt;
- For `description`-nøkkelen, trenger du bare å legge til et kort avsnitt som beskriver innholdet ditt. Beskrivelsen må være på samme språk som filnavnet. Du trenger ikke å oversette denne beskrivelsen til alle støttede språk på siden, da PlanB-teamene vil gjøre dette med sin modell.
For eksempel, her er hvordan filen din kan se ut:

```yaml
name: BIP39 WORDLIST
description: |
  Komplett og nummerert liste over de 2048 engelske ordene fra BIP39-ordlisten brukt til å kode mnemonic fraser. Dokumentet kan skrives ut på en enkelt side.
```

![event](assets/37.webp)
- Klikk på `Commit changes...`-knappen:
![event](assets/38.webp)
- Sørg for at `Commit directly to the patch-1 branch`-boksen er merket av, legg til en tittel, deretter klikker du på `Commit changes`:
![event](assets/39.webp)
- Innholdsmappen din skal nå se slik ut:
![event](assets/40.webp)
*Hvis du foretrekker å ikke legge til innholdet på GitHub og du allerede har notert lenkene i `bet.yml`-filen i de tidligere stegene, kan du hoppe over denne seksjonen og gå direkte til delen som omhandler opprettelsen av Pull Request.*
- Gå tilbake til `/assets`-mappen:
![event](assets/41.webp)
- Klikk på `Add file`-knappen, deretter på `Upload files`:
![event](assets/42.webp)
- En ny side vil åpne seg. Dra og slipp innholdet du ønsker å dele inn i området:
![event](assets/43.webp)
- For eksempel la jeg til PDF-filen av BIP39-listen:
![event](assets/44.webp)
- Når innholdet er lastet opp, sørg for at boksen `Commit directly to the patch-1 branch` er krysset av, deretter klikk på `Commit changes`:
![event](assets/45.webp)
- Gå tilbake til din `/assets`-mappe og klikk på filen du nettopp lastet opp:
![event](assets/46.webp)
- Hent den mellomliggende URL-en til filen din. For eksempel, i mitt tilfelle, er URL-en:

```url
https://github.com/tutorial-pandul/sovereign-university-data/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Behold kun den siste delen av URL-en fra `/resources` og videre:

```url
/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Legg til følgende informasjon i basen av URL-en for å ha den korrekte lenken:

```url
https://github.com/DiscoverBitcoin/sovereign-university-data/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

Det vi gjør her er å forutse den fremtidige lenken til filen din, en gang ditt forslag har blitt slått sammen med kildearkivet til PlanB Network.
- Gå tilbake til din `bet.yml`-fil og klikk på blyantikonet: ![event](assets/47.webp)
- Legg til lenken din der:
![event](assets/48.webp)
- Når endringene dine er fullførte, klikk på `Commit changes...`-knappen:
![event](assets/49.webp)
- Legg til en tittel for endringene dine, samt en kort beskrivelse:
![event](assets/50.webp)
- Klikk på den grønne `Commit changes`-knappen:
![event](assets/51.webp)

---

- Hvis alt ser bra ut for deg, gå tilbake til roten av din fork:
![event](assets/52.webp)
- Du bør se en melding som indikerer at din gren har blitt endret. Klikk på `Compare & pull request`-knappen:
![event](assets/53.webp)
- Legg til en klar tittel og en beskrivelse for din PR:
![event](assets/54.webp)
- Klikk på `Create pull request`-knappen:
![event](assets/55.webp)
Gratulerer! Din PR har blitt vellykket opprettet. En administrator vil nå gjennomgå den og, hvis alt er i orden, slå den sammen med hovedarkivet til PlanB Network. Du bør se din BET dukke opp på nettsiden noen dager senere.

Sørg for å følge med på fremgangen til din PR. En administrator kan legge igjen en kommentar som ber om ytterligere informasjon. Så lenge din PR ikke er validert, kan du konsultere den i Pull requests-fanen på PlanB Network GitHub-arkivet:
![event](assets/56.webp)
Tusen takk for ditt verdifulle bidrag! :)