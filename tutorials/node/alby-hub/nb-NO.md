---
name: Alby Hub
description: Hvordan lanserer du enkelt din egen Lightning-node?
---
![cover](assets/cover.webp)

Alby Hub er den nyeste open-source-programvaren fra Alby, selskapet bak den populære Lightning-nettleserutvidelsen. Alby Hub er en selvforvaltet lommebok med den enkleste Lightning-noden å bruke, tilgjengelig fra hvor som helst for å integrere med dusinvis av apper. Alby Hub er et brukervennlig grensesnitt for å administrere Lightning-noder.

I denne veiledningen skal vi se på forskjellige måter å bruke Alby Hub på, og hvordan koble det til Alby Go, Alby's mobilapp eller Alby-nettleserutvidelsen. Dette vil gjøre det mulig for deg å bruke satsene dine på farten mens du opprettholder autonomi i administrasjonen av noden din.


![ALBY HUB](assets/fr/01.webp)

## Hva er Alby Hub?

Alby Hub er satt til å bli det nye flaggskipverktøyet i Alby-økosystemet. Denne programvaren lar brukere enkelt administrere sin egen selvforvaltede lommebok med en integrert Lightning-node, samtidig som de beholder eierskap til sine nøkler (self-custody).

Alby Hub er et svært tilpasningsdyktig verktøy. Det kan dekke behovene til både nybegynnere og avanserte brukere. Nybegynnere kan enkelt bruke det til å drifte en ekte Lightning-node på egen hånd, uten å måtte forholde seg til den underliggende kompleksiteten. For mer erfarne brukere kan Alby Hub brukes som et komplett grensesnitt for avansert administrasjon av en eksisterende Lightning-node.

Avhengig av dine behov er Alby Hub tilgjengelig i fire konfigurasjoner:


- Alby Hub Cloud :**

Ideell for nybegynnere, dette første alternativet er Alby-skyalternativet. Det lar deg distribuere en Hub direkte på en Alby-administrert server, tilgjengelig via din Alby Hub-grensesnitt. Selv om Alby administrerer serveren, beholder du suvereniteten over midlene dine, ettersom nøklene dine er kryptert med et passord som bare du kjenner. Imidlertid må nøklene dine forbli dekryptert i RAM for at noden skal fungere, noe som teoretisk sett utsetter dem for risiko hvis noen fysisk får tilgang til serveren. Det er et interessant kompromiss for nybegynnere, men det er viktig å være klar over risikoene.

Den største fordelen med dette alternativet er at du får en Lightning-node som er oppe og går 24/7, uten at du trenger å administrere hostingen selv. I tillegg er sikkerhetskopieringen av Lightning-noden forenklet og automatisert, sammenlignet med alternativer med egen hosting, der du selv må administrere sikkerhetskopieringen av kanalene.

Alby Cloud er en betalt tjeneste [Sjekk deres priser](https://albyhub.com/#pricing) for mer informasjon. Avgiften trekkes automatisk fra lommeboken din via en Lightning-faktura utstedt av Alby. Dette gjøres via en NWC-tilkobling som konfigurerer noden din til automatisk å betale Alby-fakturaer relatert til abonnementet ditt.


- Alby Hub med en eksisterende node :**

Hvis du allerede har en node hosted, for eksempel på Umbrel eller Start9, kan Alby Hub brukes som et avansert administrasjonsgrensesnitt, på samme måte som ThunderHub eller RTL.


- Alby Hub lokal :**

Det er også mulig å installere Alby Hub direkte på PC-en din, selv om dette alternativet er mindre praktisk, siden PC-en din må være aktiv hele tiden for å få fjernadgang til Lightning-noden. Imidlertid kan dette alternativet være egnet for dine spesifikke behov.


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

Du må deretter velge mellom et selvhostet alternativ, hvor du installerer Alby Hub på din egen enhet, eller premium-alternativer. Jeg vil starte med å forklare hvordan du går frem med Pro Cloud-alternativet (merk at dette er et betalt alternativ, se detaljer i forrige avsnitt).

Klikk på "*Oppgrader*".

![ALBY HUB](assets/fr/09.webp)

Bekreft ved å klikke på "*Subscribe Now*".

![ALBY HUB](assets/fr/10.webp)

Klikk på "*Launch Alby Hub*".

![ALBY HUB](assets/fr/11.webp)

Vent et øyeblikk mens noden opprettes.

![ALBY HUB](assets/fr/12.webp)

Og det er det, din Alby Hub er nå konfigurert. I neste seksjon vil jeg vise deg hvordan du installerer Alby Hub på en eksisterende node. Hvis du ikke allerede har en Lightning-node, kan du hoppe videre til neste seksjon for å konfigurere Alby Hub på Alby Cloud.


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

Det er derfor essensielt å velge et sterkt passord. Alle som har dette passordet, kan potensielt få tilgang til noden din. Sørg også for å lage en eller flere fysiske sikkerhetskopier av dette passordet på et papir, eller enda bedre, på et stykke metall for økt sikkerhet.

Når du har valgt og lagret passordet ditt, klikker du på "*Opprett passord*".

![ALBY HUB](assets/fr/19.webp)

Du har nå tilgang til Lightning-noden din.

![ALBY HUB](assets/fr/20.webp)

Den første handlingen du må gjøre er å lagre din gjenopprettingsfrase, som nøklene dine er avledet fra. For å gjøre dette, klikk på "Innstillinger". Denne frasen lar deg gjenopprette tilgang til lommeboken din hvis du har aktivert automatiske sikkerhetskopier.

![ALBY HUB](assets/fr/21.webp)

Gå deretter til "*Backup*"-fanen. Skriv inn passordet ditt for å få tilgang til det.

![ALBY HUB](assets/fr/22.webp)

Du vil da ha tilgang til din 12-ords gjenopprettingsfrase. Lag en eller flere fysiske sikkerhetskopier av denne frasen på papir eller metall, og oppbevar den på et trygt sted.

![ALBY HUB](assets/fr/23.webp)

Når du har lagret frasen, merker du av i boksen for å bekrefte at du har lagret den, og klikker på "*Fortsett*".

![ALBY HUB](assets/fr/24.webp)

## Hvordan kan jeg få tilgang til bitcoinsene mine?

Før du sender midler til din Alby Hub, er det viktig å forstå hvordan du kan gjenopprette dem i tilfelle et problem, samt hvilken informasjon som kreves for denne gjenopprettingen. Prosessen varierer avhengig av arten av midlene som skal gjenopprettes og vertsmåten for noden din.

For betalte skytjenestebrukere krever full gjenoppretting av bitcoinene dine tre essensielle elementer:

- Din gjenopprettingsfrase;
- Tilgang til din Alby-konto for å hente de automatiserte sikkerhetskopiene.

Fraværet av noen av disse to informasjonene vil gjøre det umulig å gjenopprette dine bitcoins fullt ut.

For de som kjører Alby Hub på sin egen enhet, er gjenopprettingsprosessen dokumentert [her](https://guides.getalby.com/user-guide/alby-account-and-browser-extension/alby-hub/backups-and-recover#alby-hub-self-hosted-with-an-alby-account).

Hvis du har installert Alby Hub på en eksisterende node, må du følge gjenopprettingsprosessen for det spesifikke node-operativsystemet. For eksempel: Umbrel tilbyr [en mulighet](https://github.com/getumbrel/umbrel/blob/2b266036f62a1594aa60a8a3be30cfb8656e755f/scripts/backup/README.md) til å kryptere den nyeste statusen til Lightning-kanalene dine og lagre den dynamisk og anonymt via Tor. Vær oppmerksom på at kun de automatiserte sikkerhetskopiene fra Alby lar deg gjenopprette din Hub helt uten å lukke noen kanaler.

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

## Nodeadministrasjon

Å administrere dine Lightning-kanaler er enklere enn du tror. Alby Hub lar deg overføre sats mellom din utgiftsbalanse og din on-chain-balanse. Slik kan du øke din kapasitet til å sende eller motta.

![ALBY HUB](assets/fr/66.webp)


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

I din Alby Hub, under App Store, finn “Alby Go” og klikk på “Connect”  
![ALBY HUB](assets/fr/47.webp)  
Klikk på “Connect with One-Tab Connections”. Dette lar deg koble Alby Hub til andre apper med ett klikk ved å bruke Alby Go.  

![ALBY HUB](assets/fr/48.webp)  

Alby Hub vil deretter generere en hemmelighet for å opprette forbindelsen til Alby Go.


![ALBY HUB](assets/fr/49.webp)

Gå tilbake til Alby Go-applikasjonen, skann QR-koden eller lim inn hemmeligheten.

![ALBY HUB](assets/fr/50.webp)

Klikk på "Fullfør*".

![ALBY HUB](assets/fr/51.webp)

Du har nå fjernadgang til din Lightning-node drevet av Alby Hub fra smarttelefonen din, noe som gjør det enkelt å sende og motta sats på farten hver dag.


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

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
