---
name: Grunnleggende om GitHub
description: Forstå grunnleggende om Git og GitHub
---

![cover](assets/cover.webp)

PlanB's oppdrag er å tilby førsteklasses utdanningsressurser om Bitcoin, tilgjengelig på så mange språk som mulig. Alt innhold som publiseres på nettstedet er åpen kildekode og hostet på GitHub, noe som gir alle muligheten til å bidra til berikelsen av plattformen. Bidrag kan ta forskjellige former: korrigering og korrekturlesing av eksisterende tekster, oversettelse til andre språk, oppdatering av informasjon, eller å skape nye opplæringsprogrammer som ennå ikke er tilgjengelige på nettstedet vårt.

Hvis du ønsker å bidra til PlanB-nettverket, må du bruke Git og GitHub. Hvis disse verktøyene er ukjente for deg, eller hvis deres funksjon virker obskur, ikke få panikk, denne artikkelen er for deg! Vi vil sammen gjennomgå grunnleggende om Git og GitHub, samt tilhørende teknisk jargon, for å gjøre deg i stand til å effektivt bruke disse verktøyene etterpå.

## Hva er Git?

Git er et versjonskontrollsystem, spesielt designet for å håndtere programvareprosjekter. Opprettet i 2005 av Linus Torvalds, har Git raskt blitt standarden i programvareutviklingsindustrien for versjonskontroll. Men hva betyr det egentlig?
![git](assets/1.webp)
I sin kjerne lar Git utviklere spore endringer som er gjort i et prosjekts kildekode over tid. Dette betyr at med hver endring i koden, registrerer Git en ny versjon av prosjektet. Hvis en feil oppstår eller hvis en eksperimentell funksjon ikke fungerer som forventet, er det mulig å gå tilbake til en tidligere tilstand av koden, som en slags tidsmaskin for filer.

En av nøkkelfunksjonene til Git er håndtering av grener. En gren er en slags parallell linje hvor utviklere kan jobbe uavhengig av resten av prosjektet. Dette letter sterkt tilføyelsen av nye funksjoner eller korrigering av feil uten å forstyrre hovedkoden. Når endringene er testet og validert, kan de slås sammen med hovedgrenen.

En av særegenhetene ved Git er dens evne til å operere på en distribuert måte. Hver utvikler har en komplett kopi av prosjektet på sin egen datamaskins harddisk, noe som gjør det mulig for dem å jobbe offline og slå sammen endringer senere når en internettforbindelse er tilgjengelig. Dette reduserer risikoen for konflikter og lar flere utviklere jobbe samtidig på samme prosjekt uten å tråkke på hverandres tær.
Opprinnelig var Git primært designet for programvareutviklingsprosjekter. Imidlertid kan det også brukes til å håndtere prosjekter for skriving av innhold. I stedet for å samarbeide om kode, samarbeider vi om tekst. Og det er nettopp denne metoden PlanB-nettverket har adoptert for å håndtere sitt innhold! Git letter samarbeid om å skrive kurs og opplæringsprogrammer, da det muliggjør nøyaktig sporing av endringer, effektiv versjonsstyring, og også muliggjør gjennomgang og forbedring av innhold av andre bidragsytere.
## Hva er GitHub?

GitHub er en plattform for håndtering og hosting av kildekode basert på Git-versjonskontrollsystemet vi nettopp diskuterte. Lansert i 2008, fikk GitHub raskt popularitet og har blitt en essensiell referanse for utviklere over hele verden. Men hvordan skiller GitHub seg fra Git, og hvorfor er det så avgjørende i vår metode for produksjon av innhold?
![github](assets/2.webp)
Først er det viktig å forstå at GitHub er bygget på Git (som vi diskuterte i forrige avsnitt). Mens Git er verktøyet som sporer kodeendringer, er GitHub den nettbaserte tjenesten som hoster, deler og håndterer denne koden.

Tenk på Git som en slags loggbok som hver utvikler bruker på sin egen datamaskin for å registrere alle endringene i prosjektet sitt. GitHub, derimot, er som et offentlig bibliotek hvor alle disse loggbøkene kan deles, sammenlignes og kombineres.
Den grunnleggende forskjellen mellom Git og GitHub ligger i deres funksjon: Git er verktøyet som brukes lokalt av hver utvikler for å håndtere sine kodeversjoner, mens GitHub er den nettbaserte plattformen som huser disse versjonene og letter samarbeid.
GitHub er mye mer enn bare en tjeneste for hosting av kode. Det er en samarbeidsplattform som lar utviklere jobbe sammen effektivt. Og faktisk, PlanB Network bruker denne plattformen til å huse ikke bare all koden som driver nettstedet, men også, og dette er det som interesserer oss, alt innholdet (veiledninger, opplæring, ressurser...).

## Noen Tekniske Termer

På Git og GitHub vil du støte på kommandoer og funksjoner hvis navn kan virke komplekse. I denne siste delen gir jeg enkle definisjoner for å forstå de tekniske termene du kan komme over når du bruker Git og GitHub:

- **Fetch origin:** Kommando som henter nylig informasjon og endringer fra et eksternt repositorium uten å slå dem sammen med ditt lokale arbeid. Det oppdaterer ditt lokale repositorium med nye grener og commits som er til stede i det eksterne repositoriet.

- **Pull origin:** Kommando som henter oppdateringer fra et eksternt repositorium og umiddelbart integrerer dem i din lokale gren for å synkronisere den. Dette kombinerer trinnene for fetch og merge til en enkelt kommando.
- **Sync Fork:** En funksjon på GitHub som lar deg oppdatere din fork av et prosjekt med de siste endringene fra kilde repositoriet. Dette sikrer at din kopi av prosjektet holder seg oppdatert med hovedutviklingen.
- **Push origin:** Kommando brukt for å sende dine lokale endringer til et eksternt repositorium.

- **Pull Request:** En forespørsel sendt av en bidragsyter for å indikere at de har pushet endringer til en gren i et eksternt repositorium og ønsker at disse endringene skal bli vurdert og potensielt slått sammen med hovedgrenen i repositoriet.

- **Commit:** Lagre dine endringer. En commit er som et øyeblikksbilde av ditt arbeid på et gitt øyeblikk, som lar deg holde en historikk av endringer. Hver commit inkluderer en beskrivende melding som forklarer hva som har blitt endret.

- **Branch:** En parallell versjon av repositoriet, som lar deg jobbe med endringer uten å påvirke hovedgrenen (ofte kalt "main" eller "master"). Grener letter utviklingen av nye funksjoner og korrigering av feil uten risikoen for å forstyrre stabil kode.

- **Merge:** Sammenslåing består av å integrere endringene fra en gren inn i en annen. Det brukes for eksempel til å legge til endringene fra en arbeidsgren på hovedgrenen, som lar deg legge til de ulike bidragene.

- **Fork:** Å forke et repositorium betyr å lage en kopi av det repositoriet på din egen GitHub-konto, som lar deg jobbe på prosjektet uten å påvirke det originale repositoriet. Forken kan enten gå sin egen vei og bli et annet prosjekt fra det originale, eller den kan regelmessig synkronisere med det originale prosjektet for å bidra til det.

- **Clone:** Å klone et repositorium betyr å lage en lokal kopi på din datamaskin, som gir deg tilgang til alle filene og historikken. Dette lar deg jobbe direkte lokalt på prosjektet.

- **Repository:** Lagringsplass for et prosjekt på GitHub. Et repositorium inneholder alle prosjektfilene samt historikken over alle endringene som har blitt gjort på det. Det er grunnlaget for lagring og samarbeid på GitHub.

- **Issue:** Et verktøy for sporing av oppgaver og feil på GitHub. Issues lar deg rapportere problemer, foreslå forbedringer, eller diskutere nye funksjoner. Hver issue kan tildeles, merkes, og kommenteres på.

Denne listen er åpenbart ikke uttømmende. Det finnes mange andre tekniske termer spesifikke for Git og GitHub. Imidlertid er de nevnt her de viktigste du vil ofte støte på.
Etter å ha lest denne artikkelen, er det mulig at noen aspekter ved Git og GitHub fortsatt er uklare for deg. Jeg oppfordrer deg til å begynne å bruke disse verktøyene selv. Praksis er ofte den beste måten å forstå hvordan maskinen fungerer på! Og for å komme i gang, kan du utforske disse 2 andre veiledningene: **[Opprett din GitHub-konto](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c)**
**[Sette opp ditt lokale miljø for å bidra til PlanB Network](https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba)**