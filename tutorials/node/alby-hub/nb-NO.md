---
name: Alby Hub
description: Hvordan lanserer du enkelt din egen Lightning-node?
---
![cover](assets/cover.webp)

Alby Hub er den nyeste programvaren fra Alby, selskapet bak den populære Lightning-nettutvidelsen. Alby Hub er et brukervennlig grensesnitt for administrasjon av Lightning-noder.

I denne veiledningen skal vi se på ulike måter å bruke Alby Hub til å administrere din egen Lightning-node, og hvordan du kobler den til Alby Go, Albys mobilapp. Slik kan du bruke satsene dine mens du er på farten, samtidig som du kan administrere noden din på egen hånd.

![ALBY HUB](assets/fr/01.webp)

## Hva er Alby Hub?

I 2024 markerte Alby et strategisk skifte. I årevis har de tilbudt en rekke verktøy knyttet til Bitcoin og Lightning Network, inkludert den ikoniske Alby-utvidelsen, som lar deg drive en Lightning-lommebok, med eller uten depot. I 2025 planlegger de imidlertid å avvikle sin delte depotlommebokstjeneste og fokusere utelukkende på selvforvaringsløsninger. Alby Hub er satt til å være det nye flaggskipverktøyet i Alby-økosystemet. Denne programvaren gjør det enkelt for brukerne å administrere sin egen Lightning-node, samtidig som de beholder eierskapet til nøklene sine (self-custody).

Alby Hub er et svært tilpasningsdyktig verktøy. Det kan dekke behovene til både nybegynnere og avanserte brukere. Nybegynnere kan enkelt bruke det til å drifte en ekte Lightning-node på egen hånd, uten å måtte forholde seg til den underliggende kompleksiteten. For mer erfarne brukere kan Alby Hub brukes som et komplett grensesnitt for avansert administrasjon av en eksisterende Lightning-node.

Avhengig av dine behov er Alby Hub tilgjengelig i fire konfigurasjoner:


- Alby Hub Cloud :**

Dette første alternativet er ideelt for nybegynnere, og er Alby Cloud-alternativet. Det lar deg distribuere en Lightning-node direkte på en Alby-administrert server, som er tilgjengelig via ditt Alby Hub-grensesnitt. Selv om Alby administrerer serveren, beholder du råderetten over midlene dine, ettersom nøklene dine krypteres med et passord som bare du kjenner til. Nøklene dine må imidlertid forbli dekryptert i RAM-minnet for at noden skal fungere, noe som teoretisk sett utsetter dem for risiko hvis noen får fysisk tilgang til serveren. Det er et interessant kompromiss for nybegynnere, men det er viktig å være klar over risikoen.

Den største fordelen med dette alternativet er at du får en Lightning-node som er oppe og går 24/7, uten at du trenger å administrere hostingen selv. I tillegg er sikkerhetskopieringen av Lightning-noden forenklet og automatisert, sammenlignet med alternativer med egen hosting, der du selv må administrere sikkerhetskopieringen av kanalene.

Alby tilbyr denne tjenesten for 21 000 satser per måned (pris for desember 2024, med forbehold om endringer, [sjekk prisene deres] (https://albyhub.com/#pricing)). Avgiften trekkes automatisk fra noden din via en lynfaktura utstedt av Alby. Dette gjøres via en NWC-tilkobling som konfigurerer noden din til å automatisk betale Alby-fakturaer knyttet til abonnementet ditt.


- Alby Hub med en eksisterende node :**

Hvis du allerede har en node hosted, for eksempel på Umbrel eller Start9, kan Alby Hub brukes som et avansert administrasjonsgrensesnitt, på samme måte som ThunderHub eller RTL.


- Alby Hub lokal :**

Det er også mulig å installere Alby Hub og noden direkte på PC-en, selv om dette alternativet er mindre praktisk, ettersom PC-en må være aktiv hele tiden for å få fjerntilgang til Lightning-noden. Dette alternativet kan imidlertid være egnet for dine spesifikke behov.


- Alby Hub på en personlig server :**

For avanserte brukere kan Alby Hub distribueres på en personlig server med en enkel kommando. Dette alternativet er ikke dekket i denne veiledningen, men du kan finne dedikerte instruksjoner [på Albys GitHub] (https://github.com/getAlby/hub?tab=readme-ov-file#docker).

Denne veiledningen fokuserer hovedsakelig på grensesnittet, som vil være det samme uansett hvilket alternativ du velger. Vi ser også på hvordan du distribuerer Alby Hub med det betalte skyalternativet, og deretter med node-in-box-alternativet (Umbrel eller Start9).

![ALBY HUB](assets/fr/02.webp)

For lokal installasjon på PC-en din, [last ned og installer programvaren i henhold til operativsystemet] (https://github.com/getAlby/hub/releases), og følg deretter de samme instruksjonene på grensesnittet.

![ALBY HUB](assets/fr/03.webp)

## Opprett en Alby-konto

Det første trinnet er å opprette en Alby-konto. Selv om dette ikke er avgjørende for å kunne bruke Alby Hub, gir det deg muligheten til å dra full nytte av de tilgjengelige alternativene, inkludert muligheten til å få en Lightning-adresse.

Gå til [det offisielle Alby-nettstedet] (https://getalby.com/) og klikk på "*Opprett konto*"-knappen.

![ALBY HUB](assets/fr/04.webp)

Skriv inn et kallenavn og en e-postadresse, og klikk deretter på "*Sign up*". Denne e-postadressen vil bli brukt til å logge inn på kontoen din senere.

![ALBY HUB](assets/fr/05.webp)

Skriv inn bekreftelseskoden du har mottatt på e-post.

![ALBY HUB](assets/fr/06.webp)

Når du er logget inn på nettkontoen din, klikker du på knappen "*Fortsett*".

![ALBY HUB](assets/fr/07.webp)

Klikk på "*Fortsett*" igjen.

![ALBY HUB](assets/fr/08.webp)

## Alternativet med skyhosting

Deretter må du velge mellom et alternativ der du selv er vert for en Lightning-node på din egen maskinvare, eller det betalte alternativet der du bruker Albys sky. Jeg begynner med å forklare hvordan du går frem med skyalternativet (merk at dette er et betalingsalternativ, se detaljer i forrige avsnitt).

Klikk på "*Oppgrader*".

![ALBY HUB](assets/fr/09.webp)

Bekreft ved å klikke på "*Subscribe Now*".

![ALBY HUB](assets/fr/10.webp)

Klikk på "*Launch Alby Hub*".

![ALBY HUB](assets/fr/11.webp)

Vent et øyeblikk mens noden opprettes.

![ALBY HUB](assets/fr/12.webp)

Og det var det, Alby Hub er nå konfigurert. I neste avsnitt skal jeg vise deg hvordan du installerer Alby Hub på en eksisterende node. Hvis du ikke trenger det, kan du hoppe videre til neste avsnitt for å konfigurere noden.

![ALBY HUB](assets/fr/13.webp)

## Alternativet for selvhosting

Hvis du foretrekker å bruke Alby Hub som et grensesnitt for din eksisterende Lightning-node, har du flere alternativer: du kan installere den på en server, lokalt på datamaskinen eller via en node-in-box (Umbrel eller Start9). Det er gratis å bruke Alby Hub i disse konfigurasjonene. Vi kommer til å konsentrere oss om node-in-box-alternativet, ettersom jeg mener at serveralternativet, uten fysisk tilgang, innebærer samme risiko som skyversjonen, og lokal installasjon på en PC ofte er uegnet.

For å konfigurere dette på Umbrel (trinnene for Start9 er identiske) må du først ha en LND-node som allerede er konfigurert.

Logg inn på Umbrel-grensesnittet ditt og gå til applikasjonsbutikken.

![ALBY HUB](assets/fr/14.webp)

Se etter applikasjonen "*Alby Hub*".

![ALBY HUB](assets/fr/15.webp)

Installer den på noden din.

![ALBY HUB](assets/fr/16.webp)

Alby Hub-grensesnittet ditt er nå klart. Du kan følge resten av veiledningen som om du brukte skygrensesnittet, men uten alternativene i betalingsversjonen. I motsetning til skyversjonen lagres dessuten nøklene dine lokalt på noden din, ikke på Albys servere.

![ALBY HUB](assets/fr/17.webp)

## Lansering av Alby Hub

Klikk på knappen "*Get Started*".

![ALBY HUB](assets/fr/18.webp)

Alby Hub vil deretter be deg om å velge et passord. Dette passordet er svært viktig, ettersom det vil bli brukt til å kryptere lommeboken din. I den betalte skyversjonen lagres nøklene dine på Alby-serveren, krypteres med dette passordet som bare du kjenner, dekrypteres og lagres kun i RAM for å signere transaksjoner når det er nødvendig.

Det er derfor viktig å velge et sterkt passord. Hvem som helst med dette passordet kan potensielt få tilgang til noden din. Sørg for at du også tar en eller flere fysiske sikkerhetskopier av dette passordet på et stykke papir, eller enda bedre, på et stykke metall for ekstra sikkerhet. **Hvis du mister dette passordet, vil det være umulig å få tilgang til bitcoinsene dine igjen**, ettersom Alby ikke har noen mulighet til å tilbakestille det. Tap av dette passordet betyr tap av bitcoinsene dine.

Når du har valgt og lagret passordet ditt, klikker du på "*Opprett passord*".

![ALBY HUB](assets/fr/19.webp)

Du har nå tilgang til Lightning-noden din.

![ALBY HUB](assets/fr/20.webp)

Det første du må gjøre er å lagre gjenopprettingsfrasen din, som nøklene dine er utledet fra. Med denne frasen kan du gjenopprette tilgangen til lommeboken din på kjeden og, med den nyeste tilstanden til kanalene dine, satsene dine på Lightning. For å gjøre dette, klikk på "*Settings*".

![ALBY HUB](assets/fr/21.webp)

Gå deretter til "*Backup*"-fanen. Skriv inn passordet ditt for å få tilgang til det.

![ALBY HUB](assets/fr/22.webp)

Du vil da ha tilgang til din 12-ords gjenopprettingsfrase. Lag en eller flere fysiske sikkerhetskopier av denne frasen på papir eller metall, og oppbevar den på et trygt sted.

![ALBY HUB](assets/fr/23.webp)

Når du har lagret frasen, merker du av i boksen for å bekrefte at du har lagret den, og klikker på "*Fortsett*".

![ALBY HUB](assets/fr/24.webp)

## Hvordan kan jeg få tilgang til bitcoinsene mine?

Før du sender penger til noden din, er det viktig å forstå hvordan du kan gjenopprette dem hvis det skulle oppstå et problem, og hvilken informasjon som kreves for denne gjenopprettingen. Prosessen varierer avhengig av hva slags midler som skal gjenopprettes, og hvordan noden din er hostet.

For betalende skybrukere krever fullstendig gjenoppretting av bitcoins tre viktige elementer:


- Gjenopprettingsfrasen din;
- Passordet ditt (det som brukes for noden din) ;
- Tilgang til Alby-kontoen din for å hente den nyeste statusen for Lightning-kanalene dine.

Hvis noen av disse tre opplysningene mangler, vil det være umulig å få tilbake bitcoinsene dine i sin helhet.

For de som hoster sin egen node, er gjenopprettingsprosessen identisk med den for en hvilken som helst Lightning-node. Du trenger :


- Gjenopprettingsfrasen din;
- Den siste statusen til Lightning-kanalene dine. For å sikre denne informasjonen tilbyr Umbrel [et alternativ] (https://github.com/getumbrel/umbrel/blob/2b266036f62a1594aa60a8a3be30cfb8656e755f/scripts/backup/README.md) for å kryptere den og lagre den dynamisk og anonymt via Tor.

## Kjøp din første Lightning-kanal

Du kan nå følge instruksjonene fra Alby Hub. Klikk på knappen for å åpne din første kanal for innkommende kontanter.

![ALBY HUB](assets/fr/25.webp)

Velg "*Åpen kanal*". Hvis du ikke har tenkt å bli en rutingsnode og ikke har et spesifikt behov for det, anbefaler jeg at du velger private kanaler.

![ALBY HUB](assets/fr/26.webp)

Alby Hub vil generere en faktura som du må betale. Denne betalingen dekker transaksjonsgebyrene som trengs for å åpne kanalen din, samt serviceavgiftene til LSP (*Lightning Service Provider*) som vil åpne en kanal til noden din, slik at du kan motta betalinger umiddelbart.

![ALBY HUB](assets/fr/27.webp)

Når fakturaen er betalt og transaksjonen er bekreftet, er den første Lightning-kanalen din etablert.

![ALBY HUB](assets/fr/28.webp)

I "*Node*"-fanen kan du se at du nå har innkommende kontanter, slik at du kan motta betalinger via Lightning.

![ALBY HUB](assets/fr/29.webp)

For å motta betaling klikker du på fanen "*Wallet*" og deretter på "*Receive*".

![ALBY HUB](assets/fr/30.webp)

Angi et beløp og legg til en beskrivelse om nødvendig, og klikk deretter på "*Opprett faktura*".

![ALBY HUB](assets/fr/31.webp)

Jeg fikk min første utbetaling på 120 000 sats.

![ALBY HUB](assets/fr/32.webp)

Ved å gå tilbake til "*Wallet*"-fanen kan du sjekke saldoen i lommeboken. Merk at Alby Hub automatisk setter av 354 sats når du foretar din første betaling. For hver lynkanal du deretter åpner, vil Alby Hub automatisk sette av en reserve som tilsvarer 1 % av kanalens kapasitet. Denne reserven er et sikkerhetstiltak som gjør det mulig for noden din å gjenopprette kanalens midler i tilfelle forsøk på svindel fra din motpart. Det er derfor, selv om jeg har sendt 120 000 sats, bare 119 646 sats vises på saldoen min.

![ALBY HUB](assets/fr/33.webp)

## Innskudd av bitcoins på kjeden

Hvis du vil ha utgående kontanter for å utføre betalinger, kan du også åpne en kanal selv. For å gjøre dette trenger du bitcoins i kjeden i lommeboken din.

Fra fanen "*Node*" klikker du på "*Deposit*".

![ALBY HUB](assets/fr/34.webp)

Send bitcoins til adressen som vises. Denne adressen er avledet fra den tidligere lagrede gjenopprettingsfrasen din.

![ALBY HUB](assets/fr/35.webp)

Jeg sendte 72 000 sats. De er nå synlige i "*Savings Balance*", som inkluderer alle midlene jeg eier på kjeden, og ikke på Lightning.

![ALBY HUB](assets/fr/36.webp)

## Åpne en Lightning-kanal

Nå som du har midler i kjeden, kan du åpne en ny Lightning-kanal. Det anbefales å åpne flere kanaler, med tilstrekkelige beløp for å sikre at du alltid kan utføre betalinger uten begrensninger. De fleste LSP-er (*Lightning Service Providers*) krever minst 150 000 sats for å åpne en kanal med deg.

I fanen "*Node*" klikker du på "*Open Channel*".

![ALBY HUB](assets/fr/37.webp)

Velg størrelsen på kanalen din. Jeg anbefaler at du ikke åpner kanaler som er for små, med tanke på at dette er en Lightning-node, og at maskinen som er vert for nøklene dine ikke tilbyr samme sikkerhetsnivå som en maskinvarelommebok. Så vær forsiktig med hvor mye du velger å blokkere.

![ALBY HUB](assets/fr/38.webp)

I menyen "*Advanced Options*" kan du velge hvilken LSP du vil åpne kanalen med, eller du kan manuelt angi en annen Lightning-node.

![ALBY HUB](assets/fr/39.webp)

Klikk deretter på "*Åpne kanal*".

![ALBY HUB](assets/fr/40.webp)

Vent mens kanalen din blir bekreftet i kjeden.

![ALBY HUB](assets/fr/41.webp)

Den nye kanalen din vil nå vises i "*Node*"-fanen.

![ALBY HUB](assets/fr/42.webp)

## Koble til en utgiftsapplikasjon

Nå som du har en fungerende Lightning-node, kan du bruke den til å motta og bruke sats på daglig basis. Selv om Alby Hubs webgrensesnitt er praktisk for å administrere noden din, er det ikke ideelt for å gjøre raske transaksjoner på farten. Til dette skal vi bruke en Lightning-lommebok-app installert på smarttelefonen vår.

I denne veiledningen anbefaler jeg at du velger Alby Go, som er veldig enkelt å bruke, men du kan også bruke andre kompatible programmer, for eksempel Zeus.

![ALBY HUB](assets/fr/43.webp)

Gå til applikasjonsbutikken på enheten din for å installere Alby Go:


- [For Android] (https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [For Apple] (https://apps.apple.com/us/app/alby-go/id6471335774).

![ALBY HUB](assets/fr/44.webp)

Android-brukere kan også installere appen via `.apk`-filen [tilgjengelig på Albys GitHub] (https://github.com/getAlby/go/releases).

![ALBY HUB](assets/fr/45.webp)

Når applikasjonen startes, klikker du på "*Connect Wallet*".

![ALBY HUB](assets/fr/46.webp)

I Alby Hub, under fanen "*Connections*", klikker du på "*Add Connection*".

![ALBY HUB](assets/fr/47.webp)

Gi denne tilkoblingen et navn som gjør det enkelt å identifisere den i huben, og velg hvilke tillatelser du ønsker å gi applikasjonen. I mitt tilfelle velger jeg "*Full tilgang*" for å ha full tilgang til Lightning-nodens midler fra smarttelefonen min, men du kan også begrense tilgangen med et maksimalt budsjett, velge hvilke funksjoner som er tillatt, eller angi en utløpsdato for disse tillatelsene. Når du har konfigurert, klikker du på "*Neste*".

![ALBY HUB](assets/fr/48.webp)

Alby Hub genererer deretter en hemmelighet for å opprette forbindelsen.

![ALBY HUB](assets/fr/49.webp)

Gå tilbake til Alby Go-applikasjonen, skann QR-koden eller lim inn hemmeligheten.

![ALBY HUB](assets/fr/50.webp)

Klikk på "Fullfør*".

![ALBY HUB](assets/fr/51.webp)

Du har nå ekstern tilgang til Lightning-noden fra smarttelefonen din, noe som gjør det enkelt å bruke og motta satellitter mens du er på farten hver dag.

![ALBY HUB](assets/fr/52.webp)

Hvis det er nødvendig, kan du administrere tillatelsene for denne tilkoblingen direkte i Alby Hub ved å klikke på den.

![ALBY HUB](assets/fr/53.webp)

For å motta sats klikker du ganske enkelt på "*Mottak*".

![ALBY HUB](assets/fr/54.webp)

Endre fakturabeløp og beskrivelse ved å klikke på "*Faktura*".

![ALBY HUB](assets/fr/55.webp)

Belast fakturaen for å motta sats.

![ALBY HUB](assets/fr/56.webp)

For å sende sats klikker du på "*Send*".

![ALBY HUB](assets/fr/57.webp)

Skann fakturaen du ønsker å betale.

![ALBY HUB](assets/fr/58.webp)

Klikk deretter på "*Betale*".

![ALBY HUB](assets/fr/59.webp)

Transaksjonen din er bekreftet.

![ALBY HUB](assets/fr/60.webp)

Ved å klikke på den lille pilen får du tilgang til transaksjonshistorikken din.

![ALBY HUB](assets/fr/61.webp)

Disse transaksjonene er også synlige på Alby Hub.

![ALBY HUB](assets/fr/62.webp)

## Tilpass Lightning-adressen din

Alby tilbyr deg muligheten til en Lightning-adresse. Dette gjør at du kan motta betalinger på noden din uten å måtte generere en faktura manuelt hver gang. Som standard tildeler Alby deg en Lightning-adresse, men du kan tilpasse den. Logg inn på Alby-kontoen din, klikk på navnet ditt øverst i høyre hjørne, og velg deretter "*Innstillinger*".

![ALBY HUB](assets/fr/63.webp)

Gå til menyen "*Lightning Address*".

![ALBY HUB](assets/fr/64.webp)

Endre adressen din, og bekreft deretter ved å klikke på "*Oppdater lynadressen din*".

![ALBY HUB](assets/fr/65.webp)

Vær oppmerksom på at når adressen din har blitt endret, tilhører den ikke lenger deg. Så sørg for at du aldri sender sats til den igjen.

Nå vet du hvordan du bruker Lightning med din egen node ved hjelp av Alby Hub-verktøyet. Hvis du synes denne veiledningen var nyttig, vil jeg være veldig takknemlig hvis du setter en grønn tommel nedenfor. Del gjerne denne artikkelen på dine sosiale nettverk. Tusen takk skal du ha!

For å forstå i detalj alle Lightning-mekanismene som vi har manipulert i denne opplæringen, anbefaler jeg deg på det sterkeste å oppdage vår gratis opplæring om emnet :

https://planb.network/courses/lnp201