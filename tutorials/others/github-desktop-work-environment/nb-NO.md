---
name: GitHub Desktop
description: Hvordan sette opp ditt lokale arbeidsmiljø?
---
![github](assets/cover.webp)

PlanB's oppdrag er å tilby førsteklasses utdanningsressurser om Bitcoin på så mange språk som mulig. Alt innhold som publiseres på nettstedet er åpen kildekode og hostet på GitHub, noe som gjør at hvem som helst kan delta i å berike plattformen. Bidrag kan ta forskjellige former: korrigering og korrekturlesing av eksisterende tekster, oversettelse til andre språk, oppdatering av informasjon, eller å lage nye veiledninger som ennå ikke er tilgjengelige på nettstedet vårt.

Hvis du ønsker å bidra til PlanB-nettverket, må du bruke GitHub for å foreslå endringer. For å gjøre dette har du to alternativer:
- **Bidra direkte via GitHub's webgrensesnitt**: Dette er den enkleste metoden. Hvis du er nybegynner eller hvis du planlegger å gjøre bare noen få mindre bidrag, er dette alternativet sannsynligvis det beste for deg;
- **Bidra lokalt ved å bruke Git**: Denne metoden er mer passende hvis du planlegger å gjøre regelmessige eller betydelige bidrag til PlanB-nettverket. Selv om det å sette opp ditt lokale Git-miljø på datamaskinen din kan virke komplekst i begynnelsen, er denne tilnærmingen mer effektiv i det lange løp. Det tillater mer fleksibel håndtering av endringer. Hvis du er ny til dette, ikke bekymre deg, **vi forklarer hele prosessen med å sette opp ditt miljø i denne veiledningen** (lovet, du trenger ikke å skrive noen kommandolinjer ^^).

Hvis du ikke har noen ide om hva GitHub er, eller hvis du ønsker å lære mer om de tekniske termene relatert til Git og GitHub, anbefaler jeg at du leser vår introduksjonsartikkel for å gjøre deg kjent med disse konseptene.

https://planb.network/tutorials/others/basics-of-github



- For å starte, vil du åpenbart trenge en GitHub-konto. Hvis du allerede har en, kan du logge inn, ellers kan du bruke vår veiledning for å opprette en ny.

https://planb.network/tutorials/others/create-github-account



## Steg 1: Installer GitHub Desktop

- Gå til https://desktop.github.com/ for å laste ned GitHub Desktop-programvaren. Denne programvaren lar deg enkelt samhandle med GitHub, uten å måtte bruke en terminal:
![github-desktop](assets/1.webp)
- Når du først starter programvaren, vil du bli bedt om å koble din GitHub-konto. For å gjøre dette, klikk på `Logg inn på GitHub.com`:
![github-desktop](assets/2.webp)
- En autentiseringsside vil åpne seg i nettleseren din. Skriv inn din e-postadresse og passord valgt når du opprettet kontoen din, deretter klikk på `Logg inn`-knappen:
![github-desktop](assets/3.webp)
- Klikk på `Autoriser desktop` for å bekrefte tilkoblingen mellom kontoen din og programvaren:
![github-desktop](assets/4.webp)
- Du vil automatisk bli omdirigert til GitHub Desktop-programvaren. Klikk på `Fullfør`: ![github-desktop](assets/5.webp)
- Hvis du nettopp har opprettet din GitHub-konto, vil du bli omdirigert til en side som indikerer at du ennå ikke har opprettet noen repositorier. På dette tidspunktet, sett til side GitHub Desktop-programvaren; vi vil returnere til den senere: ![github-desktop](assets/6.webp)

## Steg 2: Installer Obsidian

La oss gå videre til å installere skriveprogramvaren. Her har du flere alternativer. Du trenger programvare som støtter redigering av Markdown-filer, ettersom PlanB-nettverket bruker dette formatet for tekstfiler i sitt repositorium.
Det finnes en rekke programvarer spesialisert på å redigere Markdown-filer, som Typora, designet spesifikt for skriving. Selv om det ikke er ideelt, er det også mulig å velge en kodeeditor, som Visual Studio Code (VSC) eller Sublime Text. Imidlertid, som skribent, foretrekker jeg å bruke Obsidian-programvaren. La oss se sammen hvordan vi installerer og kommer i gang med den.
- Gå til https://obsidian.md/download og last ned programvaren: ![github-desktop](assets/7.webp)
- Installer Obsidian, start programvaren, velg språket ditt, og klikk deretter på `Quick Start`: ![github-desktop](assets/8.webp)
- Du vil komme til Obsidian-programvaren. For øyeblikket har du ingen filer åpne: ![github-desktop](assets/9.webp)

## Steg 3: Fork PlanB Network-repositoriet

- Gå til PlanB Network datarepositoriet på følgende adresse: [https://github.com/PlanB-Network/bitcoin-educational-content](https://github.com/PlanB-Network/bitcoin-educational-content): ![github-desktop](assets/10.webp)
- Fra denne siden, klikk på `Fork`-knappen øverst til høyre i vinduet: ![github-desktop](assets/11.webp)
- I opprettelsesmenyen kan du la standardinnstillingene stå. Sørg for at boksen `Copy the dev branch only` er merket av, og klikk deretter på `Create fork`-knappen: ![github-desktop](assets/12.webp)
- Du vil da komme til din egen fork av PlanB Network-repositoriet: ![github-desktop](assets/13.webp)
Denne forken utgjør et separat repositorium fra det originale, selv om det for øyeblikket inneholder de samme dataene. Du vil nå jobbe på dette nye repositoriet.

Vi har på en måte laget en kopi av PlanB Network-kilderepositoriet. Din fork (kopien) og det originale repositoriet vil nå utvikle seg uavhengig av hverandre. På det originale repositoriet kan andre bidragsytere legge til nye data, mens du, på din fork, vil fortsette med dine egne modifikasjoner.
For å opprettholde konsistens mellom disse to repositoriene, vil det være nødvendig å synkronisere dem periodisk slik at de henter den samme informasjonen. For å sende dine endringer til kilderepositoriet, vil du bruke det som kalles en **Pull Request**. Og for å integrere endringer fra kilderepositoriet inn i din fork, vil du bruke **Sync fork**-kommandoen tilgjengelig på GitHub-webgrensesnittet.
![github-desktop](assets/14.webp)

## Steg 4: Clone forken

- Returner til GitHub Desktop-programvaren. På dette tidspunktet bør din fork vises i `Your repositories`-delen. Hvis du ikke ser den umiddelbart, bruk dobbeltpilknappen for å oppdatere listen. Når din fork vises, klikk på den for å velge den:
![github-desktop](assets/15.webp)
- Klikk deretter på den blå knappen: `Clone [brukernavn]/sovereign-university-data`:
![github-desktop](assets/16.webp)
- Behold standardbanen. For å bekrefte, klikk på den blå `Clone`-knappen:
![github-desktop](assets/17.webp)
- Vent mens GitHub Desktop klone din fork lokalt:
![github-desktop](assets/18.webp)
- Etter å ha klonet repositoriet, tilbyr programvaren deg to alternativer. Du må velge det første: `To contribute to the parent project`. Dette valget vil tillate deg å presentere ditt fremtidige arbeid som et bidrag til morsprosjektet (`DecouvreBitcoin/sovereign-university-data`), og ikke utelukkende som en modifikasjon av din personlige fork (`[brukernavn]/sovereign-university-data`). Når alternativet er valgt, klikk på `Continue`:
![github-desktop](assets/19.webp)- GitHub Desktop-en din er nå riktig konfigurert. Nå kan du la programvaren være åpen i bakgrunnen for å følge med på endringene vi vil gjøre.
![github-desktop](assets/20.webp)
Det vi har oppnådd på dette stadiet er opprettelsen av en lokal kopi av ditt repositorium, som er hostet på GitHub. Som en påminnelse, dette repositoriet er en fork av kilde-repositoriet til PlanB Network. Du vil kunne gjøre endringer på denne lokale kopien, som å legge til veiledninger, oversettelser, eller korreksjoner. Når disse endringene er gjort, vil du bruke **Push origin**-kommandoen for å sende dine lokale endringer til din fork hostet på GitHub.

Du kan også hente endringer fra forken, for eksempel, under en synkronisering med PlanB Network-repositoriet. For dette, vil du bruke **Fetch origin**-kommandoen for å laste ned endringene til din lokale kopi (din klon), og deretter **Pull origin**-kommandoen for å slå dem sammen med ditt arbeid. Dette lar deg holde deg oppdatert med de siste utviklingene av prosjektet samtidig som du bidrar effektivt.

![github-desktop](assets/21.webp)
## Steg 5: Opprett et nytt Obsidian-hvelv

- Åpne Obsidian-programvaren og klikk på det lille hvelv-ikonet nederst til venstre i vinduet:
![github-desktop](assets/22.webp)
- Klikk på `Open`-knappen for å åpne en eksisterende mappe som et hvelv: ![github-desktop](assets/23.webp)
- Filutforskeren din vil åpne seg. Du må lokalisere og velge mappen med tittelen `GitHub`, som bør være i din `Documents`-mappe blant filene dine. Denne stien tilsvarer den du etablerte under steg 4. Etter å ha valgt mappen, bekreft valget. Opprettelsen av ditt hvelv på Obsidian vil deretter starte på en ny side av programvaren:

![github-desktop](assets/24.webp)
-> **Oppmerksomhet**, det er viktig å ikke velge `sovereign-university-data`-mappen når du oppretter et nytt hvelv i Obsidian. Velg i stedet overordnet mappe, `GitHub`. Hvis du velger `sovereign-university-data`-mappen, vil konfigurasjonsmappen `.obsidian`, som inneholder dine lokale Obsidian-innstillinger, automatisk bli integrert i repositoriet. Vi ønsker å unngå dette, da det ikke er nødvendig å overføre dine Obsidian-konfigurasjoner til PlanB Network-repositoriet. Et alternativ er å legge til `.obsidian`-mappen i `.gitignore`-filen, men denne metoden ville også endre `.gitignore`-filen til kilde-repositoriet, noe som ikke er ønskelig.

- På venstre side av vinduet kan du se filtrestrukturen med dine forskjellige GitHub-repositorier som har blitt klonet lokalt.
- Ved å klikke på pilene ved siden av mappenavnene, kan du utvide dem for å få tilgang til undermappene til repositoriene og deres dokumenter:
![github-desktop](assets/25.webp)
- Ikke glem å sette Obsidian til mørk modus: "Lys tiltrekker seg bugs" ;)

## Steg 6: Installer en kodeeditor

De fleste av dine endringer vil være på filer i Markdown-format (`.md`). For å redigere disse dokumentene, kan du bruke Obsidian, programvaren vi diskuterte tidligere. Men, PlanB Network bruker andre filformater, og du vil trenge å modifisere noen av dem.

For eksempel, når du oppretter en ny veiledning, vil du trenge å opprette en YAML (`.yml`)-fil for å angi taggene for din veiledning, dens tittel, og ditt lærer-ID. Obsidian tilbyr ikke muligheten til å modifisere denne typen filer, så du vil trenge en kodeeditor.
For dette har du flere alternativer tilgjengelig. Selv om standard notisblokk på datamaskinen din kan brukes til disse endringene, er ikke denne løsningen ideell for pent arbeid. Jeg anbefaler å velge programvare som er spesifikt designet for dette formålet, slik som [VS Code](https://code.visualstudio.com/download) eller [Sublime Text](https://www.sublimetext.com/download). Sublime Text, som er spesielt lettvekt, vil være mer enn tilstrekkelig for våre behov. - Installer ett av disse programmene, og hold det til side for dine fremtidige modifikasjoner. ![github-desktop](assets/26.webp)
Gratulerer! Ditt arbeidsmiljø er nå satt opp for å bidra til PlanB Network. Du kan nå utforske våre andre spesifikke veiledninger for hver type bidrag (oversettelse, korrekturlesing, skriving.

https://planb.network/tutorials/others

..).