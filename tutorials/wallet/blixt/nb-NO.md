---
name: Blixt Wallet
description: Hvordan begynne å bruke en kraftig LN-node på mobilen?
---
![cover](assets/cover.webp)


Denne veiledningen er dedikert til alle nye brukere som ønsker å begynne å bruke Bitcoin Lightning Network (LN) på en GRATIS ÅPEN KILDE, FULLSTENDIG IKKE-CUSTODIAL måte.


Ved hjelp av [Blixt Wallet] (https://blixtwallet.com/), en komplett LN-node på mobilen, uansett hvor du er.


Hvis du aldri har brukt Bitcoin Lightning Network, før du begynner, [vennligst les denne enkle forklaringsanalogien om Lightning Network (LN)](https://darth-coin.github.io/beginner/LN-airport-analogy-en.html).


## VIKTIGE ASPEKTER:



- Blixt er en privat node, IKKE en rutingsnode! Husk det: Det betyr at alle LN-kanalene i Blixt vil være uanmeldt til LN-grafen (såkalte private kanaler). Det betyr at DENNE NODEN IKKE GJØR RUTING av andre betalinger gjennom Blixt-noden. Denne Blixt-noden er IKKE for ruting, jeg gjentar. Er hovedsakelig for å kunne administrere dine egne LN-kanaler og gjøre dine LN-betalinger privat, når du trenger det. Denne Blixt-noden er nødvendig for å være online og synkronisert KUN FØR du skal gjøre transaksjonene dine. Det er derfor du vil se et ikon på toppen som indikerer synkroniseringsstatusen. Det tar bare noen få øyeblikk, avhengig av hvor lenge du har holdt den frakoblet.



- Blixt bruker LND (aezeed) som Wallet backend, så ikke prøv å importere andre typer Bitcoin lommebøker til den. [Her har du forklart typene Wallet Mnemonic frø] (https://coldbit.com/what-types-of-Mnemonic-seeds-are-used-in-Bitcoin/). Og her er [en mer omfattende liste over alle typer lommebøker](https://walletsrecovery.org/). Så hvis du tidligere hadde en LND-node, kan du importere seed og backup.channels til Blixt, [slik det er forklart i denne veiledningen](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html).



- På slutten av denne guiden finner du en egen seksjon med ["tips og triks"] (https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#tips)



- Neste viktige lenker - se dem på slutten av denne veiledningen, og legg dem gjerne inn som bokmerker.


---

## Blixt - Første kontakt


Darths mor bestemte seg for å begynne å bruke LN med Blixt. Hard-beslutning, men klok. Blixt er bare for smarte mennesker og de som virkelig ønsker å lære mer, dyp bruk av LN.


![blixt](assets/en/01.webp)


Darth advarte moren sin:


"*Mor, hvis du begynner å bruke Blixt LN Node, må du først vite hva Lightning Network er og hvordan det fungerer, i det minste på grunnleggende nivå. [Her har jeg satt sammen en enkel liste over ressurser om Lightning Network](https://blixtwallet.github.io/faq#what-is-LN). Vennligst les dem først*."


Darth's Mom leste ressursene og tok sitt første skritt: hun installerte Blixt på sin splitter nye Android-enhet. Blixt er også tilgjengelig for iOS og macOS (desktop). Men disse er ikke noe for Darths mor... Likevel anbefales det å bruke en nyere versjon av Android, minst 9 eller 10, for bedre kompatibilitet og opplevelse. Å kjøre en full LN-node på en mobil enhet er ikke en enkel oppgave og kan ta en del plass (min. 600 MB) og minne.


Når du åpner Blixt, får du noen alternativer på "Velkommen"-skjermen:


![blixt](assets/en/02.webp)


Øverst i høyre hjørne ser du tre prikker som aktiverer en meny med:



- "enable Tor" - brukeren kan starte med Tor-nettverket, spesielt hvis man ønsker å gjenopprette en gammel LND-node som bare kjørte med Tor-peers.
- "Set Bitcoin node" - hvis brukeren ønsker å koble til sin egen node direkte, for å synkronisere blokkene gjennom Neutrino, kan du gjøre det rett fra velkomstskjermen. Dette alternativet er også bra i tilfelle internettforbindelsen din eller Tor ikke er så stabil at du kan koble til standard Bitcoin-node (node.blixtwallet.com).
- Snart vil det bli lagt til språk der, slik at brukeren kan starte rett med et språk som er komfortabelt. Hvis du ønsker å bidra til dette open source-prosjektet med oversettelser til andre språk, [vennligst bli med her] (https://explore.transifex.com/blixt-Wallet/blixt-Wallet/).


### ALTERNATIV A - Opprett en ny Wallet


Hvis du velger å "opprette en ny Wallet", vil du bli omdirigert direkte til hovedskjermen til Blixt Wallet.


Dette er din "cockpit" og er også "Main LN Wallet", så vær oppmerksom på at den kun viser deg balansen til din LN Wallet. Wallet i kjeden vises separat (se C).


![blixt](assets/en/03.webp)


A - Blixt blokkerer synkroniseringsindikatorikonet. Dette er det viktigste for en LN-node: å være synkronisert med nettverket. Hvis dette ikonet fortsatt fungerer, betyr det at noden din IKKE ER KLAR! Så ha tålmodighet, spesielt for den første innledende synkroniseringen. Det kan ta opptil 6-8 minutter, avhengig av enheten din og internettforbindelsen.


Du kan klikke på den og se status for synkroniseringen:


![blixt](assets/en/04.webp)


Du kan også klikke på knappen "Vis LND-logg" (A) hvis du vil se og lese flere tekniske detaljer i LND-loggen, i sanntid. Er veldig nyttig for feilsøking og for å lære mer om hvordan LN fungerer.


B - Her får du tilgang til alle Blixt-innstillingene, og det er mange! Blixt tilbyr mange funksjoner og alternativer for å administrere LN-noden din som en proff. Alle disse alternativene er forklart i detalj i "[Blixt Features Page] (https://blixtwallet.github.io/features#blixt-options) - Options Menu".


C - Her har du menyen "Magic Drawer", [også forklart i detalj her] (https://blixtwallet.github.io/features#blixt-drawer). Her er "Onchain Wallet" (B), Lightning Channels (C), Contacts, Channels statusikon (A), Keysend (D).


![blixt](assets/en/05.webp)


D - Er hjelpemenyen, med lenker til FAQ / Guides-side, kontakt utvikler, Github-side og Telegram supportgruppe.


E - Angi din første BTC Address, hvor du kan sette inn din første testing Sats. DETTE ER VALGFRITT! Hvis du setter inn rett inn i den Address, åpner en LN-kanal mot Blixt Node. Det betyr at du vil se din innskudd Sats, som går inn i en annen onchain-transaksjon (tx), for å åpne den LN-kanalen. Du kan sjekke det inn i Blixt onchain Wallet (se punkt C) ved å klikke på TX-menyen øverst til høyre.


![blixt](assets/en/06.webp)


Som du kan se i Onchain-transaksjonsloggen, er trinnene svært detaljerte og viser hvor Sats går (innskudd, åpne, lukke kanal).


ANBEFALING:


Etter å ha testet flere situasjoner kom vi frem til at det er mye mer effektivt å åpne kanaler på mellom 1 og 5 M Sats. Mindre kanaler har en tendens til å bli tømt raskt og betale en høyere prosentandel av avgiftene sammenlignet med større kanaler.


F - Angi hovedbalansen din for Lightning Wallet. Dette er IKKE din totale Blixt Wallet-saldo, den representerer kun den Sats du har i Lightning Channels, tilgjengelig for sending. Som tidligere angitt er Onchain Wallet separat. Husk på dette aspektet. Onchain Wallet er separat av en viktig grunn: Den brukes hovedsakelig til å åpne/lukke LN-kanaler.


Ok, så nå har Darth's Mom satt inn noen Sats i den onchain Address som vises på hovedskjermen. Det anbefales at når du gjør det, må du holde Blixt-appen din online og aktiv en stund, til BTC tx blir tatt av gruvearbeiderne i den første blokken.


Etter det kan det ta opptil 20-30 minutter før det er fullstendig bekreftet og kanalen er åpen, og du vil se den i Magic Drawer - Lightning Channels som aktiv. Også den lille fargede prikken på toppen av skuffen, hvis det er Green, vil indikere at LN-kanalen din er online og klar til å bli brukt til å sende Sats over LN.


Address og velkomstmeldingen som vises, forsvinner. Det er ikke lenger nødvendig å åpne en automatisk kanal nå. Du kan også deaktivere alternativet i Innstillinger-menyen.


Det er på tide å gå videre og teste andre funksjoner og alternativer for å åpne LN-kanaler.


La oss nå åpne en annen kanal med en annen node peer. Blixt-fellesskapet har satt sammen [en liste over gode noder å begynne å bruke med Blixt] (https://github.com/hsjoberg/blixt-Wallet/issues/1033).


**Fremgangsmåte for å åpne en LN-kanal i Blixt**


Dette er veldig enkelt, det tar bare noen få skritt og litt tålmodighet:



- Kom til [Blixt Community](https://github.com/hsjoberg/blixt-Wallet/issues/1033) listen over jevnaldrende
- Velg en node og klikk på navnelinken for å åpne Amboss-siden
- Klikk for å vise QR-koden for noden URI Address


![blixt](assets/en/07.webp)


Åpne Blixt og gå til øverste skuff - Lightning Channels og klikk på "+" -knappen


![blixt](assets/en/08.webp)


Klikk nå på (A)-kameraet for å skanne QR-koden fra Amboss-siden, og nodeopplysningene vil bli fylt ut. Legg til beløpet for Sats for kanalen du ønsker, og velg deretter avgiftssatsen for tx. Du kan la den være automatisk (B) for en raskere bekreftelse eller justere den manuelt ved å skyve på knappen. Du kan også trykke lenge på nummeret og redigere det som du vil.


Ikke legg mindre enn 1 sat/vbyte! Vanligvis er det bedre å konsultere [Mempool-avgifter] (https://Mempool.space/) før du åpner en kanal, og velge en passende avgift.


Ferdig, nå er det bare å klikke på knappen "åpne kanal" og vente på 3 bekreftelser, det tar vanligvis 30 min (1 blokk aprox hver 10min).


Når kanalen er bekreftet, vil du se at den er aktiv i seksjonen "Lightning Channels".


---

## Blixt - Andre kontakt


Ok, så nå har vi en LN-kanal med bare OUTBOUND-likviditet. Det betyr at vi bare kan SENDE, vi kan fortsatt ikke MOTTA Sats over LN.


![blixt](assets/en/09.webp)


Hvorfor det? Leste du veiledningene som ble angitt i begynnelsen? Har du ikke? Gå tilbake og les dem. Det er svært viktig å forstå hvordan LN-kanalene fungerer.


![blixt](assets/en/10.webp)


Som du kan se i dette eksempelet, har kanalen som er åpen med det første innskuddet, ikke for mye INBOUND-likviditet ("Kan motta"), men har mye OUTBOUND-likviditet ("Kan sende").


Så hvilke alternativer har du hvis du ønsker å motta mer Sats enn LN?



- Bruk litt Sats fra eksisterende kanal. Ja, LN er et betalingsnettverk av Bitcoin, som hovedsakelig brukes til å bruke Sats raskere, billigere, privat og enkelt. LN er IKKE en hodling-måte, for det har du onchain Wallet.



- Bytt noen Sats tilbake til din Wallet i kjeden ved hjelp av en ubåtbyttetjeneste. På denne måten bruker du ikke Sats, men gir dem tilbake til din egen Wallet i kjeden. Her kan du se noen metoder i detalj, i [Blixt Guides Page] (https://blixtwallet.github.io/guides).



- Åpne en INBOUND-kanal fra en hvilken som helst LSP-leverandør. Her er en videodemo om hvordan du bruker LNBig LSP for å åpne en innkommende kanal. Det betyr at du betaler en liten avgift for en TOM kanal (på din side), og du vil kunne motta flere Sats til den kanalen. Hvis du er en kjøpmann som mottar mer enn du bruker, er det et godt alternativ. Også hvis du kjøper Sats over LN, ved hjelp av Robosats eller andre LN Exchange.



- Åpne en Dunder-kanal, med Blixt node eller en annen Dunder LSP-leverandør. En Dunder-kanal er en enkel måte å få litt INBOUND-likviditet på, men samtidig setter du inn litt Sats i den kanalen. Det er også bra fordi det vil åpne kanalen med en [UTXO] (https://en.Bitcoin.it/wiki/UTXO) som ikke er fra din Blixt Wallet. Det gir litt privatliv. Det er også bra fordi, hvis du ikke har Sats i en onchain Wallet, for å åpne en normal LN kanal, men du har dem i en annen LN Wallet, kan du bare betale fra den andre Wallet gjennom LN åpningen og innskuddet (på din side) av den Dunder-kanalen. [Flere detaljer om hvordan Dunder fungerer og hvordan du kjører din egen server her] (https://github.com/hsjoberg/dunder-lsp).


![blixt](assets/en/11.webp)


Her er trinnene for å aktivere åpning av en Dunder-kanal:



- Gå til Innstillinger, i delen "Eksperimenter" aktiverer du boksen for "Aktiver Dunder LSP".
- Når du har gjort det, går du tilbake til "Lightning Network" -delen, og du vil se at det dukket opp alternativet "Set Dunder LSP Server". Der er som standard satt "https://dunder.blixtwallet.com", men du kan endre det med en hvilken som helst annen Dunder LSP-leverandør Address. [Her er en Blixt community list](https://github.com/hsjoberg/blixt-Wallet/issues/1033) med noder som kan tilby Dudner LSP-kanaler for din Blixt.
- Nå kan du gå til hovedskjermen og klikke på "Receive" -knappen. Følg deretter denne prosedyren [forklart i denne veiledningen] (https://blixtwallet.github.io/guides#guide-lsp).


OK, så etter at Dunder-kanalen er bekreftet (det tar noen minutter), vil du ende opp med å ha to LN-kanaler: én som opprinnelig ble åpnet med autopilot (kanal A), og én med mer innkommende likviditet, åpnet med Dunder (kanal B).


![blixt](assets/en/12.webp)


Bra, nå er du klar til å sende og motta nok Sats over LN!


GRATULERER MED Bitcoin LIGHTNING!


---

## Blixt - Tredje kontakt


Husk at i kapittel 1 "Første kontakt" var det to alternativer på velkomstskjermen:


- [Alternativ A](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#option-a) - Opprett ny Wallet
- Alternativ B - Gjenopprett Wallet


Så la oss nå diskutere hvordan du gjenoppretter en Blixt Wallet eller en hvilken som helst annen LND krasjet node. Dette er litt mer teknisk, men vær oppmerksom. Er ikke det Hard.


### ALTERNATIV B - Gjenopprett Wallet


Tidligere skrev jeg en dedikert guide om [hvordan gjenopprette en krasjet Umbrel-node] (https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), hvor jeg også nevnte metoden for å bruke Blixt som rask gjenopprettingsprosess, ved hjelp av seed + channel.backup-filen fra Umbrel.


Jeg har også skrevet en veiledning om hvordan du gjenoppretter Blixt-noden din eller migrerer Blixt til en annen enhet, [her] (https://blixtwallet.github.io/faq#blixt-restore).


![blixt](assets/en/13.webp)


Men la oss forklare denne prosessen i enkle trinn. Som du kan se på bildet ovenfor, er det to ting du bør gjøre for å gjenopprette din tidligere Blixt/LND-node:



- øverste boksen er der du må fylle inn alle 24 ordene fra din seed (gammel/død node)
- nederst er det to knappalternativer for å sette inn / laste opp filen channel.backup, som tidligere er lagret fra din gamle Blixt/LND-node. Det kan være fra en lokal fil (du laster den opp til enheten din tidligere) eller kan være fra en Google-stasjon / iCloud ekstern plassering. Blixt har dette alternativet for å lagre sikkerhetskopien av kanalene dine direkte på en Google-/iCloud-stasjon. Se flere detaljer i [Blixt Features Page] (https://blixtwallet.github.io/features#blixt-options).


Likevel å nevne, hvis du tidligere ikke hadde noen åpne LN-kanaler, er det ikke nødvendig å laste opp noen channels.backup-fil. Bare sett inn de 24 ordene seed og trykk på gjenopprettingsknappen.


Ikke glem å aktivere Tor, fra menyen med de tre øverste punktene, som vi forklarte i Alternativ A-seksjonen. Det er tilfelle når du KUN hadde Tor-peers og ikke kunne kontaktes over clearnet (domene / IP). Ellers er det ikke nødvendig.


En annen nyttig funksjon er å angi en spesifikk Bitcoin-node fra toppmenyen. Som standard synkroniserer den blokker fra node.blixtwallet.com (nøytrino-modus), men du kan angi hvilken som helst annen Bitcoin-node som tilbyr nøytrino-synkronisering.


Så når du har fylt ut disse alternativene og trykket på gjenopprettingsknappen, begynner Blixt først å synkronisere blokkene gjennom Neutrino, slik vi forklarte i kapittelet Første kontakt. Så vær tålmodig og følg med på gjenopprettingsprosessen i hovedskjermbildet ved å klikke på synkroniseringsikonet.


![blixt](assets/en/14.webp)


Som du kan se i dette eksemplet, viser det at Bitcoin-blokkene er 100 % synkronisert (A) og gjenopprettingsprosessen er i gang (B). Det betyr at LN-kanalene du hadde tidligere, vil bli stengt og midlene gjenopprettet i din Blixt onchain Wallet.


Denne prosessen tar tid! Vær derfor tålmodig og prøv å holde Blixt aktiv og på nett. Den første synkroniseringen kan ta opptil 6-8 minutter, og det kan ta opptil 10-15 minutter å lukke kanalene. Så du bør ha enheten godt ladet.


Når denne prosessen er startet, kan du sjekke i Magic Drawer - Lightning Channels, statusen til hver av dine tidligere kanaler, som viser at de er i "venter på å lukke" -status. Når hver kanal er lukket, kan du se den avsluttende tx-en i onchain Wallet (se Magic Drawer - Onchain), og åpne tx-menyloggen.


![blixt](assets/en/15.webp)


Det vil også være bra å sjekke og legge til hvis de ikke er der, dine tidligere jevnaldrende du hadde i din gamle LN-node. Så gå til Innstillinger-menyen, ned til "Lightning Network" og gå inn i alternativet "Vis Lightning Peers".


![blixt](assets/en/16.webp)


Inne i seksjonen vil du se de jevnaldrende du er koblet til i det øyeblikket, og du kan legge til flere, det er bedre å legge til de du hadde kanaler før. Bare gå til [Amboss-siden] (https://amboss.space/), søk etter aliasene eller nodeID for dine jevnaldrende noder og skann node-URI-en deres.


![blixt](assets/en/17.webp)


Som du kan se på bildet over, er det tre aspekter:


A - representerer clearnet-noden Address URI (domene/IP)


B - representerer Tor onion-noden Address URI (.onion)


C - er QR-koden som skal skannes med Blixt-kameraet eller kopieringsknappen.


Denne noden Address URI må du legge den til i listen over jevnaldrende. Så vær oppmerksom på at det ikke er nok med bare nodealiasnavnet eller nodeID.


Nå kan du gå til Magic Drawer (menyen øverst til venstre) - Lightning Channels, og du kan se ved hvilken forfallsblokkhøyde midlene vil bli returnert til din onchain Address.


![blixt](assets/en/18.webp)


Blokk nummer 764272 er når midlene vil være brukbare i din Bitcoin onchain Address. Og det kan ta opptil 144 blokker fra den første bekreftelsesblokken til de frigjøres. [Så sjekk det i Mempool] (https://Mempool.space/).


Og det er det hele. Bare vent tålmodig til alle kanalene er stengt og pengene tilbake i din Wallet-kjede.


👉 **Sekret gjenopprettingsmetode :**


Det er en annen metode for å gjenopprette Blixt LND-noden din uten å lukke kanalene. Men er skjult for vanlige noob-brukere, fordi denne metoden KUN er for de som vet hva de gjør.


Hvis du trenger å migrere din eksisterende (fungerende) Blixt-node til en annen ny enhet, uten å stenge de eksisterende LN-kanalene, må du gjøre disse trinnene:



- Vi antar at du allerede har lagret Blixt Wallet seed (24 ord aezeed)
- På den gamle enheten går du til "Settings" - debug section - "Compact LND database". Dette trinnet er valgfritt, men anbefales hvis du vil ha en mindre størrelse på channel.db-filen. Vanligvis er den ganske stor, avhengig av nodeaktiviteten. Dette vil starte Blixt på nytt og komprimere db-filstørrelsen.
- Når du har startet på nytt, går du til "Innstillinger" og endrer det vanlige aliasnavnet ditt til "Hampus". Dette vil aktivere de skjulte alternativene, kun for avanserte brukere.
- Gå helt ned til "Debug" -delen, og du vil se et nytt alternativ "Export channel.db file". ADVARSEL! Når du gjør denne eksporten, vil den eksisterende Blixt LN-noden deaktiveres på denne gamle enheten og eksportere hele nodedatabasen (channel.db) klar til å importeres til en ny enhet.
- Denne db-filen lagres i en bestemt mappe på den gamle enheten (Dokumenter eller Nedlastinger), og derfra må du flytte den som den er til den nye enheten. Du kan for eksempel bruke [LocalSend FOSS app] (https://github.com/localsend/localsend) for å overføre filen direkte mellom enheter.
- I dette øyeblikket MÅ din gamle Blixt forbli stengt. IKKE ÅPNE DEN IGJEN!
- Når du har overført filen channel.db til den nye enheten, starter du den nye installasjonen av Blixt og velger "Restore Wallet" i det første skjermbildet.
- På knappen der det står "Velg SCB-fil", trykk lenge (IKKE enkelt klikk!), Og så vil du se muligheten til å velge en channel.db-fil der du lagrer den lokalt på den nye enheten. Hvis du bare trykker på den knappen, vil den som standard bruke en SCB-fil (med lukkede kanaler), det fungerer ikke for full sikkerhetskopiering av live-kanaler.
- Skriv inn de 24 ordene seed og klikk deretter på "Gjenopprett"
- Du vil se at Blixt begynner å synkronisere med Neutrino. Du kan også se synkroniseringsloggene.
- HUSK PÅ! Prøv å holde Blixt åpen hele tiden i denne fasen! Ikke la den gå i dvale eller lukke appskjermen. Det kan forstyrre den første synkroniseringen, og du må gjøre det på nytt. Vent tålmodig, det tar ikke mer enn noen få minutter.
- Når den første synkroniseringen av blokker er fullført, vil den raskt skanne de tidligere Wallet-adressene dine, og deretter vil kanalene dine være tilbake på nettet, i live og i god behold.
- Dessverre er det (ennå) ikke mulig å gjenopprette tidligere betalingshistorikk og kontakter. Men det er ikke så viktig uansett.


Og FERDIG! Nå har du en fullstendig gjenopprettet Blixt LN node. Det kan også fungere med andre LND-sikkerhetskopier (Umbrel, Raspiblitz osv.) Hvis du tidligere har lagret channel.db-filen riktig. Så Blixt kan bokstavelig talt redde enhver død LND-node.


---

## Blixt - Fjerde kontakt


Dette kapittelet handler om tilpasning og om å bli bedre kjent med Blixt Node. Jeg vil ikke beskrive alle funksjonene som er tilgjengelige, de er for mange og er allerede forklart på [Blixt Features Page] (https://blixtwallet.github.io/features).


Men jeg vil peke på noen av de som er nødvendige for å fortsette å bruke Blixt og få en god opplevelse.


### A - Navn (NameDesc)


![blixt](assets/en/19.webp)


[NamDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) er en standard for å formidle "mottakernavn" i BOLT11-fakturaer.


Dette kan være et hvilket som helst navn og kan endres når som helst.


Dette alternativet er veldig nyttig i ulike tilfeller, når du vil sende et navn sammen med Invoice-beskrivelsen, slik at mottakeren kan få et hint om hvem som har mottatt disse Sats. Dette er helt valgfritt, og i betalingsskjermbildet må brukeren også krysse av i boksen for å indikere at aliasnavnet skal sendes.


Her er et eksempel på hvordan det vil se ut når du bruker [chat.blixtwallet.com] (https://chat.blixtwallet.com/)


![blixt](assets/en/20.webp)


Dette er et annet eksempel på sending til en annen Wallet-app som støtter NameDesc:


![blixt](assets/en/21.webp)


### B - Lynboks


Fra og med den nye v0.6.9-420 [nylig kunngjort] (https://github.com/hsjoberg/blixt-Wallet/releases/tag/v0.6.9-420) introduserte Blixt en ny, kraftig funksjon for Lightning Address i Blixt.


Denne nye funksjonen er valgfri, og er ikke PÅ som standard!


For øyeblikket drives standard LN Box av Blixt-serveren og tilbyr en @blixtwallet.com LN Address. Men ALLE med en LND offentlig node kan kjøre Lightning Box-serveren og tilby LN Address for sitt eget domene, selvforvaring.


Akkurat nå videresender Blixt-serveren kun betalinger sendt til LN-adresser @blixtwallet.com til Blixt-brukere som har satt LN til Address. Brukere må sette sin Blixt-node Wallet i "vedvarende modus" for å kunne motta disse betalingene til sine @blixtwallet.com LN-adresser.


Se videodemoen om hvordan du konfigurerer LN Address i Blixt i utgivelsesmerknadene.


Denne LN Address implementert i Blixt Wallet-appen, er som en chat over LN, øyeblikkelig og morsom, og støtter også [LUD-18] (https://github.com/lnurl/luds/blob/luds/18.md) (legge til et aliasnavn til en betaling). Du kan legge til i kontaktlisten alle dine vanlige LN-adresser du bruker ofte og ha den for hånden for å chatte. Nå kan Blixt betraktes som en full LN chat-app 😂😂.


En annen nyttig funksjon er full støtte for LUD-18 (som også [Stacker.News] (https://stacker.news/r/DarthCoin) og andre støtter det).


![blixt](assets/en/22.webp)


Som du kan se på skjermbildet ovenfor, når du sender fra en Stacker News-konto, vises logoen + LN Address + melding pent. Samme måte fungerer for å sende fra Blixt, du kan legge ved Blixt LN Address eller bare legge til aliasnavnet (tidligere angitt i Blixt-innstillingene) eller til og med begge deler.


Dette alternativet fra LUD-18 kan også være nyttig for abonnementstjenester, der brukeren kan sende et spesifikt alias (er IKKE ditt nodealias eller ditt virkelige navn!), og basert på det kan du bli registrert eller motta en spesifikk melding eller noe annet. Å knytte et aliasnavn ([LUD-18](https://github.com/lnurl/luds/blob/luds/18.md))+ kommentar ([LUD-12](https://github.com/lnurl/luds/blob/luds/12.md)) til en LN-betaling kan ha flere bruksområder!


Her er koden for [Lightning Box] (https://github.com/hsjoberg/lightning-box) hvis du kjører den for deg selv, for familie og venner, på din egen node.


Her kan du også kjøre [LSP Dunder-serveren] (https://github.com/hsjoberg/dunder-lsp) for Blixt-mobilnoder og tilby likviditet til Blixt-brukere hvis du har en god offentlig LN-node (fungerer bare med LND).


### C - Backup LN-kanaler og seed-ord


Dette er en svært viktig funksjon!


Etter at du har åpnet eller lukket en LN-kanal, bør du ta en sikkerhetskopi. Det kan gjøres manuelt ved å lagre en liten fil på en lokal enhet (vanligvis nedlastingsmappe) eller ved å bruke en Google Drive- eller iCloud-konto.


![blixt](assets/en/23.webp)


Gå til Blixt-innstillinger - Wallet-delen. Der har du muligheten til å lagre alle viktige data for din Blixt Wallet:



- "Vis Mnemonic" - viser de 24 ordene seed for å skrive dem ned
- "Fjern Mnemonic fra enheten" - dette er valgfritt og skal bare brukes hvis du virkelig ønsker å fjerne seed-ordene fra enheten din. Dette vil IKKE slette Wallet, bare seed. Men vær oppmerksom! Det er ikke mulig å gjenopprette dem hvis du ikke skrev dem ned først.
- "Eksporter sikkerhetskopi av kanal" - dette alternativet lagrer en liten fil på den lokale enheten din, vanligvis i mappen "nedlastinger", hvor du kan ta den og flytte den utenfor enheten din for sikker oppbevaring.
- "Verify channel backup" - dette er et godt alternativ hvis du bruker Google Drive eller iCloud for å sjekke integriteten til sikkerhetskopien som er gjort eksternt.
- " Sikkerhetskopiering av Google-stasjonskanal" - lagrer sikkerhetskopifilen på din personlige Google-stasjon. Filen er kryptert og lagres i et eget lager enn de vanlige Google-filene dine. Så det er ingen bekymringer som kan leses av noen. Uansett er den filen helt ubrukelig uten seed-ordene, så ingen kan ta pengene dine bare fra den filen.


Jeg vil anbefale følgende for denne delen:



- bruk en passordadministrator for å lagre seed og sikkerhetskopifilen trygt. KeePass eller Bitwarden er veldig bra for det, og kan brukes på flere plattformer og på egen vert eller offline.
- GJØR EN BACKUP HVER GANG du åpner eller lukker en kanal. Den filen oppdateres med kanalinformasjonen. Det er ikke nødvendig å gjøre det etter hver transaksjon du har gjort på LN. Kanalbackupen lagrer ikke denne informasjonen, den lagrer bare kanalens status.


![blixt](assets/en/24.webp)


---

## Blixt - tips og triks


### CASE 1 - SYNKRONISERINGSPROBLEMER


"_My Blixt synkroniserer ikke... Blixt viser ikke saldoen ... Blixt-en min kan ikke åpne kanaler ... Jeg prøvde å gjenopprette den på en annen enhet ... osv_"


Alle disse problemene starter fordi ENHETEN DIN IKKE SYKONTRERER GODT. Vennligst forstå dette viktige aspektet: Blixt er en mobil LND-node, som bruker Neutrino for synkronisering / lesing av blokkene.



- Her er en mindre teknisk forklaring fra [Bitcoin Magazine] (https://bitcoinmagazine.com/technical/why-Bitcoin-wallets-need-block-filters)
- Her er flere tekniske ressurser fra [Bitcoin Optech] (https://bitcoinops.org/en/topics/compact-block-filters/)
- Slik kan du aktivere Neutrino på din egen hjemmenode og servere blokkeringsfiltre for mobilnoden din, fra [Docs Lightning Engineering] (https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core)


PÅMINNELSE: Å bruke Neutrino over clearnet er helt trygt, din IP eller xpub er ikke lekket. Du leser bare blokker fra en ekstern node med Neutrino. Det er alt. Resten gjøres på din lokale enhet.


Så det er INGEN grunn til å bruke det med Tor. Tor vil legge til en enorm ventetid på synkroniseringsprosessen og vil gjøre Blixt veldig ustabil. Hvis du virkelig vil bruke Tor, må du være sikker på hva du gjør og ha en god tilkobling og tålmodighet. Samme sak for bruk av VPN. Vær forsiktig med hvilken ventetid du får fra VPN-et.


Du kan teste ventetiden til en nøytrino-server ved å pinge den fra en PC eller fra mobilen.


![blixt](assets/en/25.webp)


Dette er en vanlig ping til neutrino-serveren europe.blixtwallet.com, dette viser at forbindelsen er veldig god med en responstid på gjennomsnittlig 50 ms og en TTL på 51. Svartiden kan variere, men ikke for mye. TTL må være stabil.


Hvis disse verdiene er høyere enn 100-150 ms, vil synkroniseringsprosessen bli uaktuell, eller enda verre, det kan føre til stengte kanaler hos motparter! Ikke ignorer dette aspektet.


Uten en skikkelig synkronisering kan du heller ikke se riktig balanse, eller LN-kanalene dine vil ikke komme online og i drift. Uansett hvor mange giga ultra terra mbps du har nedlastingshastigheten, spiller det ingen rolle. Det betyr noe for tidsresponsen og TTL (tid til live).


Dette er et generelt tilfelle for LATAM-brukere. Jeg vet ikke hva som skjer der nede, men dere har en forferdelig tilkobling med pinger på over 200 ms som kan forstyrre enhver synkronisering.


Så hva er løsningen for disse desperate brukerne?



- slutt å bruke Blixt med Tor. Er helt ubrukelig
- du kan bruke et VPN, men velg det med omhu og overvåke pingen hele tiden. Bruk en som er nærmere din geografiske plassering. Avstand betyr mer ms responstid, husk det.
- velg nøytrino-partnere med omhu, her er en liste over kjente offentlige nøytrino-servere:


```txt
For US region
btcd1.lnolymp.us | btcd2.lnolymp.us
btcd-mainnet.lightning.computer
swest.blixtwallet.com (Seattle)
node.eldamar.icu
noad.sathoarder.com
bb1.breez.technology | bb2.breez.technology
neutrino.shock.network
For EU region
europe.blixtwallet.com (Germany)
For Asia region
sg.lnolymp.us
asia.blixtwallet.com
```


En annen måte er å velge en fra denne listen over noder som kunngjør "kompakte filtre" (BIP157 / nøytrino) - [Bitnodes Page Neutrino filter] (https://bitnodes.io/nodes/?q=NODE_COMPACT_FILTERS). Velg en som er nærmere din geografiske plassering.


En annen måte (den beste måten) er å koble seg til en lokal node, drevet av en venn eller en gruppe som du kjenner, og som tilbyr nøytrinotilkobling. (Her er instruksjonene for hvordan du gjør det) (https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) Noden deres vil ikke bli påvirket på noen måte, de trenger bare en stabil og offentlig tilkobling.


Det er behov for flere Neutrino-servere i LATAM-regionen, for en bedre og raskere synkronisering. Så vennligst organiser deg selv, med ditt lokale Bitcoin-fellesskap og bestem hvem og hvor som kjører en Bitcoin Core + Neutrino til eget bruk. Det er nok med bare en offentlig IP. Hvis du ikke har tilgang til en offentlig IP, kan du bruke en VPS-IP og lage wireguard-tunnel til hjemmenoden din. På den måten omdirigerer du all trafikk til din lokale VPS-IP, uten å avsløre noen privat informasjon om hjemmenoden din.


### TILFELLE 2 - ALDRI FULLFØRE SYNKRONISERINGEN


"_My Blixt har god forbindelse med Neutrino-serveren, men synkroniseringen står fast._"


#### Tidsserver


Noen ganger bruker folk forskjellige gamle enheter eller er ikke riktig koblet til en tidsserver. Neutrino synkroniserer ok til de faktiske blokkene som ikke samsvarer med reell lokal tid. Du vil se i Blixt LND-logger en feil som sier at "blokkens tidsstempel er langt fra fremtiden" eller noe relatert til "header don't pass sanity check".


Rask løsning: Still inn riktig klokkeslett og dato for enheten din, og start Blixt på nytt.


#### Lite plass på enheten


Noen ganger bruker en gammel enhet, med lite plass, kan den nå en terskelgrense og sitte fast. Faktisk for mer du bruker denne mobile LND-noden, blir nøytrino-filene større og også channel.db-filen.


Rask løsning: Gå til Blixt Options - Debug-seksjonen - Velg "stopp LND og slett nøytrino-filer". Det vil starte appen på nytt og starte en ny synkronisering. Noen ganger kan denne raske løsningen også reparere ødelagte data. Husk at det vil ta litt tid, mellom 1 og 3 minutter å synkronisere helt på nytt. Det sletter IKKE eksisterende midler eller kanaler, men ja, etter resynkronisering kan det utløse en ny skanning av Bitcoin-adressene dine, og det kan ta mer tid.


Neste trinn er å sjekke hvor mye data som fortsatt er opptatt. Du kan se dette i Android App info - data. Hvis den fortsatt er større enn 400-500 MB, kan du komprimere LND-filene. Så gå til Blixt Options - Debug-delen - Velg "Compact DB LND". Start Blixt-appen på nytt hvis den ikke gjør det automatisk. Komprimeringen skjer ved oppstart og er bare en gang. Nå vil du se at Blixt-data er mer mindre opptatt.


#### Vedvarende modus


Noen ganger åpner ikke folk Blixt på lenge, så synkroniseringen er altfor gammel. Men de forventer å bli synkronisert umiddelbart når de åpner den.


Vær tålmodig, og se på det øverste spinnende hjulet. Du kan eventuelt gå til Alternativer - Se nodeinfo og se om det er synkronisert til kjeden og synkronisert til grafen merket som "sant". Uten denne "true"-markeringen kan du ikke bruke Blixt riktig, du kan ikke se saldoen riktig, du kan ikke se LN-kanalene på nettet, du kan ikke utføre betalinger.


Rask løsning: Det finnes et kraftig alternativ for å "holde liv i" Blixt-noden din. Gå til Options - Experiments - Velg "Activate Persistent Mode". Det vil starte Blixt på nytt og sette LND-tjenesten i vedvarende modus, dvs. at den alltid vil være aktiv og holde synkroniseringen online, selv om du bytter til en annen app eller bare lukker Blixt (ikke tvangslukk eller drep oppgaven). Du kan ha det slik hele dagen hvis du har en stabil tilkobling og du trenger å bruke Blixt flere ganger. Det vil ikke forbruke for mye batteri.


### TILFELLE 3 - JEG VIL MIGRERE TIL EN ANNEN ENHET


OK om dette scenariet skrev jeg en omfattende guide på [FAQ-siden] (https://blixtwallet.github.io/faq#blixt-restore): med to alternativer, raskt (samarbeidende lukking av kanaler før migrering) og sakte (tving lukke kanaler fordi den gamle enheten er død).


Men jeg vil her gjenta noen viktige aspekter og legge til en ny "hemmelig" prosedyre.


PÅMINNELSE:



- Ta alltid en sikkerhetskopi av kanalstatusen (SCB) ETTER hver gang du åpner eller lukker en kanal. Det tar bare noen sekunder å gjøre det.
- Ikke ta vare på de gamle SCB-filene for ikke å bli forvirret og gjenopprette dem. De er helt ubrukelige og kan utløse en straffeprosedyre hvis du ser dem. Bruk alltid den siste versjonen av SCB-filen hvis du fortsetter å gjenopprette.
- Lagre SCB-filen (er en kryptert tekst med filtypen .bin) på et trygt sted utenfor enheten. Du kan bruke [LocalSend] (https://github.com/localsend/localsend) for å flytte denne filen til en PC eller en annen enhet.
- Lagre også seed til din Blixt Wallet på et trygt sted, for eksempel en offline passordbehandler/kryptert USB.


Hemmelig metode: Slik migrerer du Blixt node uten å lukke de eksisterende kanalene. For dette må du lese nøye den forrige delen "Tredje kontakt" i denne veiledningen om "Gjenopprett Wallet".


Denne prosedyren er IKKE FOR NOOBS, det er bare for avanserte brukere! Det er derfor ikke allment åpent, og jeg anbefaler å gjøre det bare med hjelp fra Blixt devs eller min støtte. Vennligst ikke ignorere dette rådet.


### CASE 4 - HVILKE PEERS SKAL MAN BRUKE FOR Å ÅPNE KANALER?


Som jeg skrev i [Blixt guides side] (https://blixtwallet.github.io/guides) er det mange måter å åpne kanaler med denne mobile LND-noden på. Men noen viktige aspekter vil jeg gjerne minne deg på her:



- åpne med velkjente LSP-noder og med community vouched peers. [Se en liste her](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- ikke åpne med tilfeldige Tor-noder. De er verdiløse, og du vil bare få problemer med at du ikke kan utføre betalinger. Uansett hvor god din venn "the node runner" er med en dårlig Tor-node i en jungel, vil den aldri gi deg de beste rutene for en mobil privat node. Du åpner ikke kanaler med noen fordi de er dine venner. Dette er ikke Facebook! Du åpner en kanal for: gode ruter, små avgifter, tilgjengelighet.
- det er ikke nødvendig å åpne massevis av små kanaler, 2-3 eller maks 4, men med en god mengde Sats. Ikke åpne små kanaler, er helt ubrukelige. Mindre enn 200k for en mobil har ikke mye bruk.
- husk LSP-ene som tilbyr innkommende kanaler og JIT-kanaler (just in time). Disse er veldig nyttige fordi du ikke trenger å bruke noen av UTXO-ene dine, du kan betale åpningskanalen med midler du allerede har i andre LN-lommebøker, stable og forberede dem for at en større kanal skal åpne. Du bør bruke disse JIT-kanalene til din fordel. [Jeg har forklart i denne guiden](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) flere alternativer for jevnaldrende for private noder som Blixt. Også [her i denne guiden lagt ut på SN](https://stacker.news/items/679242/r/DarthCoin) forklarte jeg hvordan du administrerer likviditeten til private mobile noder.


---

## Konklusjon


OK, det er mange andre fantastiske funksjoner som Blixt tilbyr, jeg vil la deg oppdage dem en etter en og ha det gøy.


Denne appen er virkelig undervurdert, hovedsakelig fordi den ikke er støttet av noen VC-fond, er samfunnsdrevet, bygget med kjærlighet og lidenskap for Bitcoin og Lightning Network.


Denne mobile LN-noden, Blixt, er et veldig kraftig verktøy i hendene på mange brukere, hvis de vet hvordan de skal bruke det godt. Tenk deg at du går rundt i verden med en LN-node i lommen uten at noen vet om det.


Og da snakker vi ikke om alle de andre funksjonene som følger med, som svært få eller ingen andre Wallet-apper kan tilby.


I mellomtiden er her alle lenkene om denne fantastiske Bitcoin Lightning Node:



- [Blixt Official Webpage](https://blixtwallet.com/)
- [Blixt Github-side] (https://github.com/hsjoberg/blixt-Wallet/)
- [Blixt Features page] (https://blixtwallet.github.io/features) - forklarer hver enkelt funksjon og funksjonalitet.
- [Blixt FAQ-side](https://blixtwallet.github.io/faq) - Liste over spørsmål og svar og feilsøking av Blixt
- [Blixt Guides page](https://blixtwallet.github.io/guides) - demoer, videoveiledninger, ekstra guider og brukstilfeller for Blixt
- Last ned: [Android Play Store] (https://play.google.com/store/apps/details?id=com.blixtwallet) | [iOS] (https://testflight.apple.com/join/EXvGhRzS) | [APK direkte nedlasting] (https://github.com/hsjoberg/blixt-Wallet/releases)
- [Telegramgruppe for direkte støtte] (https://t.me/blixtwallet)
- [Twitter] (https://twitter.com/BlixtWallet)
- [Geyser crowdfunding-side] (https://geyser.fund/project/blixt) - doner Sats som du vil for å støtte prosjektet
- [LNURL Chat Blixt](https://chat.blixtwallet.com/) - anonym LN chat
- [Blixt presentation - promo video](https://lightning.video/06fdf68f99e246a6ec6ba1470677b9e632faaad4aa0ca9773c38714b682a4ac1)
- [Blixt Girls Calendar] (https://lightning.video/eeb744202ad3f14c18bf6d719970ebd9c53f0f13b79c94d299c6be623fba64b6) - promo-video (du kan teste din første bruk av LN)
- [A4-folder med de første skrittene med Blixt, på flere språk] (https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer).
- [Blixt tilbyr også en fullt funksjonell demo] (https://blixt-Wallet-git-master-hsjoberg.vercel.app/) rett på nettstedet eller på en dedikert versjon på nettet, for å få en full testopplevelse før du begynner å bruke den i den virkelige verden.


---
**DISCLAIMER:**


*Jeg får ikke betalt eller støtte fra utviklerne av denne appen på noen måte. Jeg skrev denne guiden fordi jeg så at interessen for denne Wallet-appen øker, og at nye brukere fortsatt ikke forstår hvordan de skal begynne med den. Også for å hjelpe Hampus (hovedutvikleren) med dokumentasjon om bruk av denne noden Wallet.*


*Jeg har ingen andre interesser i å promotere denne LN-appen, annet enn å fremme innføringen av Bitcoin og LN. Dette er den eneste måten!*


---