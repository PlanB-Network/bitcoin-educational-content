---
name: Blixt

description: Mobil LN Node Lommebok
---

![presentasjon](assets/blixt_intro_en.webp)

## En kraftig BTC/Lightning node i lommen din, uansett hvor du er

Jeg vil gjerne introdusere deg for en interessant og kraftig ny BTC/LN mobil node og lommebok – Blixt. Navnet kommer fra svensk og betyr "lyn".
Hvis du aldri har brukt Bitcoin Lightning Network før, vennligst les [denne enkle forklaringsanalogien om Lightning Network (LN)](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport) før du begynner.

## VIKTIGE ASPEKTER:

### 1. Blixt er en privat node, IKKE en ruter node! Husk det.

Det betyr at alle LN-kanalene i Blixt vil være uannonserte i LN-grafen (såkalte private kanaler). Det betyr at DENNE NODEN IKKE VIL UTFØRE RUTING av andres betalinger gjennom Blixt-noden. [Les mer om private og offentlige kanaler her](https://voltage.cloud/blog/lightning-network-faq/what-are-the-differences-between-public-and-private-channels/).

Blixt mobilnode er IKKE for ruting, jeg gjentar. Den er hovedsakelig for å kunne håndtere dine egne LN-kanaler og gjøre dine LN-betalinger privat, når du trenger det.

Blixt mobilnoden, er nødvendig å være online og synkronisert KUN FØR du skal gjøre transaksjonene dine. Derfor vil du se et ikon øverst som indikerer synkroniseringsstatusen. Det tar bare noen øyeblikk, avhengig av hvor mye tid du holdt den offline og resynkroniserte LN-grafen.

### 2. Blixt bruker LND (aezeed) som lommebok-backend, så ikke prøv å importere andre typer bitcoin-lommebøker inn i den.

[Her har du forklart de ulike typene lommebøker](https://coldbit.com/what-types-of-mnemonic-seeds-are-used-in-bitcoin/). Så hvis du tidligere hadde en LND-node, kan du importere frøet og backup.channels inn i Blixt, [som det er forklart i denne guiden](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario).

### 3. Viktige lenker for Blixt (vennligst bokmerk dem):

- [Blixt Github-repositorium](https://github.com/hsjoberg/blixt-wallet) | [Github Releases](https://github.com/hsjoberg/blixt-wallet/releases) (last ned apk-filen direkte)
- [Blixt Funksjonsside](https://blixtwallet.github.io/features) - forklarer en etter en hver funksjon og funksjonalitet.
- [Blixt FAQ-side](https://blixtwallet.github.io/faq) - Liste over spørsmål og svar og feilsøking av Blixt
- [Blixt Guider-side](https://blixtwallet.github.io/guides) - demoer, videotutorials, ekstra guider og brukstilfeller for Blixt
- [Utskrivbar A4-flyer](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer) med første steg for å bruke Blixt, på forskjellige språk.
- Blixt tilbyr også en fullt funksjonell demo rett på [sin nettside](https://blixtwallet.com) eller på en dedikert [webversjon](https://blixt-wallet-git-master-hsjoberg.vercel.app/), for å ha en full opplevelse med testing, før du begynner å bruke Blixt i den virkelige verden.
- [Geyser crowdfunding-side](https://geyser.fund/project/blixt) - doner sats som du vil for å støtte prosjektet
- [Telegram-støttegruppe](https://t.me/blixtwallet)
# Tilgjengelige nøkkelfunksjoner

## Neutrino Node

Blixt kobler seg som standard til Blixts server for å synkronisere blokker og indeks med Neutrino (SPV-modus for Forenklet Betalingsverifisering), men brukeren kan også koble til sin egen node. Det er overraskende å se at synkronisering av en SPV-node tar mindre enn 5 minutter, i mitt tilfelle på Android 11, for å være klar til å bruke fullnodewalleten (on-chain og LN).

## Komplett Ikke-Forvarings Node

Brukeren kan administrere sine egne kanaler med et brukervennlig grensesnitt og med nok informasjon vist for å ha en god opplevelse. I menyen øverst til venstre kan du gå til Lynkanalene for å begynne å åpne med andre noder, som du ønsker. Ikke glem å aktivere Tor i innstillingene. Det er mye bedre for personvern og også fordi som en mobil node, hvis du endrer internettforbindelsen / clearnet IP ofte, kan dine peers bli forstyrret. Med Tor node URI vil du alltid ha den samme private identifikatoren uavhengig av din plassering / IP.

## Sikkerhetskopiering/Gjenoppretting av en LND Node

En kraftig, lett å administrere og nyttig funksjon er å gjenopprette andre døde LND-noder, med bare 24-ords frølisten og channels.backup-filen.

> [Her er en guide om hvordan du gjenoppretter døde Umbrel-noder i Blixt i tilfelle SHTF.](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario)

Brukeren har også muligheten til å lagre Blixt-kanalens sikkerhetskopi til Google Drive og/eller lokal lagring på sin egen mobile enhet (for å senere flytte den til et sikkert sted, borte fra telefonen din).

Gjenopprettingsprosessen er ganske enkel: sett inn 24-ords frøet, legg til sikkerhetskopifilen (tidligere kopiert til mobilminnet), og klikk på gjenopprett. Det vil ta litt tid å synkronisere og skanne alle blokkene for dine tidligere transaksjoner. Kanalene vil automatisk bli lukket og midlene returnert til din on-chain lommebok (se menyen øverst til venstre - on-chain).

> Hvis du tidligere hadde åpne kanaler med din gamle node bak Tor, må du først aktivere Tor-alternativet (og starte applikasjonen på nytt) fra menyinnstillingene. På denne måten vil ikke lukkeprosedyren mislykkes og/eller alternativet for tvungen lukking vil ikke bli brukt.

Husk å sikkerhetskopiere dine LN-kanaler etter å ha åpnet og/eller lukket kanaler. Det tar bare noen få sekunder å være trygg. Senere kan du flytte sikkerhetskopifilen til et sikkert sted borte fra din mobile enhet.
For å teste frøet ditt i et gjenopprettingsscenario, før du legger til midler, bruk det samme 24-ords frøet (aezeed) i BlueWallet. Hvis den genererte BTC-adressen er den samme i Blixt, er du klar. Det er ikke nødvendig å bruke BlueWallet etter det, du kan ganske enkelt slette den testede lommeboken for gjenoppretting.

## Innebygd Tor

Når du har aktivert det, vil applikasjonen starte på nytt bak Tor-nettverket. Fra dette punktet kan du se i menyinnstillingene din node-ID med en løkadresse, slik at andre noder kan åpne kanaler til din lille Blixt mobile node. Eller la oss si at du har din egen node hjemme og du vil ha små kanaler med din Blixt mobile node. En perfekt kombinasjon.

## Dunder LSP - Liquidity Service Provider

En enkel og fantastisk funksjon som tilbyr nye brukere muligheten til å umiddelbart begynne å akseptere BTC på Lightning Network, uten behov for å sette inn midler on-chain og deretter åpne LN-kanaler.
For nye brukere er dette gode nyheter fordi de skal kunne starte fra bunnen av, direkte på LN. For å gjøre dette, opprett enkelt en LN-faktura fra hovedskjermen på "motta"-knappen, angi beløpet, beskrivelse, osv., og betal fra en annen lommebok. Blixt vil åpne en kanal på opptil 400k sats per transaksjon mottatt. Du kan åpne flere kanaler om nødvendig.
Et interessant og nyttig tilfelle er som følger: la oss si at ditt første mottatte beløp er 200k. Blixt vil åpne en 400k sats kanal med allerede 200k (minus åpningsgebyrer) på din side, men siden du fortsatt har 200k "plass" tilgjengelig, kan du motta mer. Så den neste betalingen, la oss si 100k, vil ankomme direkte gjennom denne kanalen, uten ekstra gebyrer, og du har fortsatt 100k plass til å motta mer.

Men hvis du velger å motta, la oss si, 300k for den tredje betalingen, vil det opprette en annen ny 400k kanal og skyve disse 300k til din side.

Hvis det er for mange forespørsler, kan Blixt-noden justere kanalkapasiteten under åpning.

## Automatisk Kanalåpning

I innstillingene kan brukeren aktivere dette alternativet og ha en automatisert tjeneste som åpner kanaler med de beste nodene og rutene basert på den tilgjengelige saldoen i on-chain lommeboken til Blixt-applikasjonen. Dette er en gunstig funksjon for nye brukere som ikke er sikre på hvilken node de skal åpne en kanal med og/eller hvordan man åpner en LN-kanal. Det er som en autopilot for LN.

> Husk: dette alternativet brukes bare én gang, når du oppretter din nye Blixt-lommebok, og er aktivert som standard. Så hvis den nye brukeren skanner on-chain QR-koden på hovedskjermen og setter inn sine første sats til den adressen, vil Blixt automatisk åpne en kanal med disse satsene, med Blixt offentlige node.

## Tjenester for Innkommende Likviditet

Funksjon dedikert til handlende som trenger mer INNKOMMENDE likviditet, enkel å bruke. For å gjøre dette, velg enkelt en av likviditetsleverandørene fra listen, betal beløpet du ønsker for kanalen, og oppgi din node-ID, og derfra vil en kanal åpne til din Blixt-node.

## Kontaktlister

Nyttig funksjon hvis du ønsker å ha en varig liste over mottakere med hvem du handler mesteparten av tiden. Denne listen kan bestå av LNURLs, Lightning-adresser, eller fremtidig statisk betalingsinformasjon/fakturaer. For nå kan ikke denne listen lagres utenfor applikasjonen, men det er planer om å ha en mulighet til å eksportere den.

## LNURL og Lightning-adresse

Full støtte for LNURL. Du kan betale til LNURL, LN-auth, LN-chan forespørsel med LNURL.
Du kan sende til hvilken som helst LN-adresse og også legge den til i kontaktlisten din.
Også fra og med vers. 0.6.9 er det mulig å motta til din egen LN-adresse *@blixtwallet.com* type, gjennom [Blixt Lightning Box](https://github.com/hsjoberg/lightning-box)-funksjonen.

## Keysend

En veldig kraftig funksjon som få mobile lommebøker har. Du kan sende/skyve midler direkte gjennom en kanal eller peke til en annen node, og legge til en melding om nødvendig. Det er som en hemmelig chat over LN. Denne funksjonen er veldig nyttig for å vise meldinger på Amboss.space oppslagstavlen ([her er en guide på denne Amboss oppslagstavlen](https://darthcoin.substack.com/p/amboss-billboard-amazing-tool)).

## Meldingssignering
Svært nyttig verktøy for å signere meldinger med din Blixt-nodes private nøkkel, autentiseringsmeldinger, og så videre. Svært få mobile lommebøker har denne funksjonen, nesten ingen.
## Flere-kanals Betalinger - Multi-Path Betalinger (MPP)

Nyttig funksjon for LN-betalinger, som lar deg dele en LN-betaling i flere deler, over flere kanaler. Det er en god måte å balansere likviditet på nettverket og forbedre personvern.

## Lynleser

En serie med tredjepartstjenester med LN, organisert innenfor en enkel, tilgjengelig og brukervennlig nettleser. Det er også en god måte å fremme bedrifter som aksepterer BTC på LN. Dette er en funksjon som vil bli videreutviklet i fremtiden. For nå fungerer det ikke bak Tor, så å bla gjennom disse applikasjonene vil være i klar (clearnet).

## Loggutforskere

Dette er et kraftig verktøy for å sjekke LND-loggene og statusen til noden din generelt. Det er en mulighet for å lagre loggfilen. Det er veldig nyttig å ha disse loggene for hånden i tilfelle du trenger utviklerassistanse for å identifisere visse problemer.

## Sikkerhet

Du kan sette i applikasjonsinnstillingene, for større sikkerhet for din lommebok/node, muligheten til å starte applikasjonen med en PIN-kode og/eller fingeravtrykk.

## On-chain Lommebok

Denne funksjonen er litt skjult, i skuffmenyen øverst til venstre. Siden den ikke ofte brukes av en LN-bruker, er den ikke synlig på hovedskjermen. Men det er greit, du kan ha den på en separat lommebok hvor du kan administrere adresser og se transaksjonsloggen, ved å importere din seed på Sparrow for eksempel. Kanskje i fremtiden vil Blixt-lommeboken også inkludere en funksjon for å administrere UTxOer. Men for nå, BRUK kun denne on-chain lommeboken for å åpne eller lukke kanaler på LN.

## Spesielle funksjoner

- Med vers. 0.6.9 ble "persistent mode" introdusert som lar brukeren kjøre Blixt som en alltid online LN-node, og holder LND-tjenestene aktive og LN-lommeboken klar til å motta/sende når som helst.
- Enkle Taproot-kanaler - tillater åpning av Taproot-kanaler for mer personvern og avanserte funksjoner
- Zero-confirmation kanaler med Blixt Dunder LSP
- Speedloader ("LN channel sync") - Dette betyr at alle kanaler vil bli synkronisert raskt ved oppstart, for bedre sti-finning. Selv om det er litt irriterende at du må se synkroniseringsskjermen i begynnelsen, vil det sikre at lommeboken vet om alle kanaler og betalingene vil være raskere og mer pålitelige.
- Oversatt til 25+ språk!

## "Påskeegg"

Ja, i Blixt-applikasjonen, er det noen skjulte funksjoner, små ting som gjør applikasjonen sjarmerende, aktiverer morsomme/interessante handlinger og svar.
Hint: prøv å klikke to ganger på Blixt-logoen i skuffen 🙂 Jeg lar deg oppdage resten.

# Blixt Kom i Gang Steg-for-Steg Guide

> Som ny LN-bruker, hvis du begynner å bruke Blixt LN Node, vil du først trenge å vite hva Lightning Network er og hvordan det fungerer, i det minste på et grunnleggende nivå. [Her har vi satt sammen en enkel liste over ressurser om Lightning Network](https://blixtwallet.github.io/faq#what-is-ln). Vennligst les dem først.”

Å kjøre en full LN-node på en mobil enhet er ikke en enkel oppgave og kan ta litt plass (min 600MB) og minne. Vi anbefaler å ha en god mobil enhet, oppdatert og bruker minst Android 11 som OS.

Når du åpner Blixt, vil “Velkommen”-skjermen gi deg noen valg:

![Demo Blixt 01](assets/blixt_t01.webp)
Øverst i høyre hjørne vil du se 3 prikker som aktiverer en meny med:
- "enable Tor" - brukeren kan starte med Tor-nettverket, spesielt hvis man ønsker å gjenopprette en gammel LND-node som kun kjørte med Tor-peers.

- "Set Bitcoin node" - hvis brukeren ønsker å koble seg direkte til sin egen node for å synkronisere blokkene gjennom Neutrino, kan dette gjøres direkte fra velkomstskjermen. Dette alternativet er også bra i tilfelle internettforbindelsen din eller Tor ikke er stabil nok til å koble til standard bitcoin-node (node.blixtwallet.com).

## Første steg - Opprett ny lommebok

Hvis du velger å "opprette en ny lommebok", vil du bli omdirigert direkte til hovedskjermen til Blixt Wallet.

Dette er ditt "cockpit" og er også "Hoved LN Lommebok", så vær oppmerksom, den vil kun vise saldoen til din LN-lommebok. Onchain-lommeboken vises separat (se C).

![Demo Blixt 02](assets/blixt_t02.webp)

A - Blixt blokksynkroniseringsindikatorikon. Dette er det viktigste for en LN-node: å være synkronisert med nettverket. Hvis det ikonet fortsatt er der og jobber, betyr det at noden DIN IKKE ER KLAR! Så ha tålmodighet, spesielt for den første initielle synkroniseringen. Det kan ta opptil 6-8 min, avhengig av enheten din og internettforbindelsen.

Du kan klikke på det og se statusen for synkroniseringen:

![Demo Blixt 03](assets/blixt_t03.webp)

Du kan også klikke på "Show LND Log" (A)-knappen hvis du vil se og lese mer tekniske detaljer om LND-loggen, i sanntid. Det er veldig nyttig for feilsøking og for å lære mer om hvordan LN fungerer.

B - Her kan du få tilgang til alle Blixt-innstillingene, og det er mange! Blixt tilbyr mange rike funksjoner og alternativer for å administrere din LN-node som en proff. Alle disse alternativene er forklart i detalj på ["Blixt Features Page - Options Menu"](https://blixtwallet.github.io/features#blixt-options).

C - Her har du "Magic Drawer"-menyen, også forklart i detalj her. Her er "Onchain Wallet" (B), Lightning-kanaler (C), Kontakter, Kanalstatusikon (A), Keysend (D).

![Demo Blixt 04](assets/blixt_t04.webp)

D - Er hjelpemenyen, med lenker til FAQ / Guider-siden, kontakt utvikleren, Github-siden og Telegram-støttegruppen.

E - Indikerer din første BTC-adresse, hvor du kan sette inn dine første test-sats. DETTE ER VALGFRITT! Hvis du setter inn direkte til den adressen, åpner det en LN-kanal mot Blixt Node. Det betyr at du vil se dine innsatte sats, gå inn i en annen onchain-transaksjon (tx), for å åpne den LN-kanalen. Du kan sjekke det i Blixt onchain-lommeboken (se punkt C), ved å klikke på TX-menyen øverst til høyre.

![Demo Blixt 05](assets/blixt_t05.webp)

Som du kan se i Onchain Transaction Log, er trinnene veldig detaljert og indikerer hvor satsene går (innskudd, åpne, lukke kanal)

> ANBEFALING: Etter å ha testet flere situasjoner, kom vi til konklusjonen at det er mye mer effektivt å åpne kanaler mellom 1 og 5 M sats. Mindre kanaler har en tendens til å bli tømt raskt og betaler en høyere % av gebyrer sammenlignet med større kanaler.
F - Angi hovedsaldoen i Lightning-lommeboken din. Dette er IKKE din totale Blixt-lommeboksaldo, den representerer kun de satsene du har i Lightning-kanaler, tilgjengelig for å sende. Som det ble indikert tidligere, er Onchain-lommeboken separat. Husk dette aspektet. Onchain-lommeboken er separat av en viktig grunn: den brukes hovedsakelig for å åpne/lukke LN-kanaler.
Ok, så nå har du satt inn noen sats i den onchain-adressen som vises på hovedskjermen. Det anbefales at når du gjør det, å holde Blixt-appen din online og aktiv en stund, til BTC-transaksjonen er tatt av minerne inn i den første blokken.

Etter det kan det ta opptil 20-30 minutter til den er fullstendig bekreftet og kanalen er åpen, og du vil se den i Magic Drawer - Lightning Channels som aktiv. Også den lille fargede prikken på toppen av skuffen, hvis den er grønn vil indikere at din LN-kanal er online og klar til å brukes til å sende sats over LN.

Adressen og velkomstmeldingen som vises vil forsvinne. Det er ikke lenger nødvendig å åpne en automatisk kanal nå. Du kan også deaktivere alternativet i Innstillinger-menyen.

Det er på tide å gå videre, teste andre funksjoner og alternativer for å åpne LN-kanaler.

Nå, la oss åpne en annen kanal med en annen node-peer. Blixt-samfunnet har satt sammen [en liste over gode noder å starte med Blixt.](https://github.com/hsjoberg/blixt-wallet/issues/1033)

### Prosedyre for å åpne en normal uannonsert (privat) LN-kanal i din Blixt mobile node

Dette er veldig enkelt, tar bare noen få steg og litt tålmodighet:
- Gå til [Blixt Community-listen](https://github.com/hsjoberg/blixt-wallet/issues/1033) over gode peers
- Velg en node og klikk på navnetittellinken, det vil åpne Amboss-siden dens
- Klikk for å vise QR-koden for nodens URI-adresse

![Demo Blixt 06](assets/blixt_t06.webp)

Nå, åpne Blixt og gå til toppskuffen - Lightning Channels og klikk på “+”-knappen

![Demo Blixt 07](assets/blixt_t07.webp)

Nå, klikk på (A) kamera for å skanne QR-koden fra Amboss-siden og nodens detaljer vil bli fylt ut. Legg til antallet sats for kanalen du ønsker og velg deretter gebyrsatsen for tx. Du kan la den være auto (B) for en raskere bekreftelse eller justere den manuelt ved å skyve knappen. Du kan også trykke lenge på nummeret og redigere det som du vil.

Ikke sett mindre enn 1 sat/vbyte! Vanligvis er det bedre å [konsultere mempool-gebyrene](https://mempool.space/) før du åpner en kanal og velger et passende gebyr.

Ferdig, nå bare klikk på knappen “åpne kanal” og vent på 3 bekreftelser, som vanligvis tar 30 min (ca. 1 blokk hver 10. min).

Når det er bekreftet, vil du se kanalen aktiv i din seksjon “Lightning Channels”.

## Andre Steg - Skaff mer Inngående Likviditet

Ok, så nå har vi en LN-kanal med kun UTGÅENDE likviditet. Det betyr at vi bare kan SENDE, vi kan fortsatt ikke MOTTAK sats over LN. Hvorfor? Leste du guidene som ble indikert i begynnelsen? Nei? Gå tilbake og les dem. Det er veldig viktig å forstå hvordan LN-kanaler fungerer.

![Demo Blixt 08](assets/blixt_t08.webp)
Som du kan se i dette eksemplet, åpner kanalen med det første innskuddet, ikke har for mye INNKOMMENDE likviditet ("Kan motta") men har mye UTKOMMENDE likviditet ("Kan sende").
Så hvilke alternativer har du hvis du ønsker å motta flere sats over LN?
- Bruk noen sats fra eksisterende kanal. Ja, LN er et betalingsnettverk for Bitcoin, brukt hovedsakelig for å bruke dine sats raskere, billigere, privat og enkelt. LN er IKKE en måte å holde på, for det har du onchain-lommeboken.
- Bytt noen sats, tilbake til din onchain-lommebok, ved å bruke en ubåtbyttetjeneste. På denne måten bruker du ikke dine sats, men gir dem tilbake til din egen onchain-lommebok. Her kan du se i detaljer noen metoder, på [Blixt Guides Side](https://blixtwallet.github.io/guides).
- Åpne en INNKOMMENDE kanal fra hvilken som helst LSP-leverandør. Her er en videodemo om [hvordan bruke LNBig LSP for å åpne en innkommende kanal](https://blixtwallet.github.io/assets/images/blixt-lnbig.mp4). Det betyr at du vil betale en liten avgift for en TOM kanal (på din side) og du vil kunne motta flere sats i den kanalen. Hvis du er en handelsmann som mottar mer enn du bruker, er det et godt alternativ. Også hvis du kjøper sats over LN, ved å bruke Robosats eller en annen LN-utveksling.
- Åpne en Dunder-kanal, med Blixt-node eller en annen Dunder LSP-leverandør. En Dunder-kanal er en enkel måte å få litt INNKOMMENDE likviditet på, men samtidig setter du inn noen sats i den kanalen. Det er også bra fordi det vil åpne kanalen med en [UTXO](https://en.bitcoin.it/wiki/UTXO) som ikke er fra din Blixt-lommebok. Det tilfører litt privatliv.
Det er også bra fordi, hvis du ikke har sats i en onchain-lommebok, for å åpne en normal LN-kanal, men du har dem i en annen LN-lommebok, kan du bare betale fra den andre lommeboken gjennom LN for åpningen og innskuddet (på din side) av den Dunder-kanalen. [Mer detaljer om hvordan Dunder fungerer og hvordan kjøre din egen server her.](https://github.com/hsjoberg/dunder-lsp)

![Demo Blixt 09](assets/blixt_t09.webp)

Her er trinnene for hvordan aktivere åpning av en Dunder-kanal:
- Gå til Innstillinger, i "Eksperimenter"-seksjonen aktiver boksen for "Aktiver Dunder LSP".
- Når du har gjort det, gå tilbake opp til "Lightning Network"-seksjonen og du vil se at alternativet "Sett Dunder LSP Server" har dukket opp. Der, som standard er satt "https://dunder.blixtwallet.com" men du kan endre det med en hvilken som helst annen Dunder LSP-leverandøradresse. [Her er en Blixt-samfunnsliste](https://github.com/hsjoberg/blixt-wallet/issues/1033) med noder som kan tilby Dudner LSP-kanaler for din Blixt.
- Nå kan du gå til hovedskjermen og klikke på "Motta"-knappen. Følg deretter denne prosedyren forklart [i denne guiden](https://blixtwallet.github.io/guides#guide-lsp).

OK, så etter at Dunder-kanalen er bekreftet (vil ta noen minutter) vil du ende opp med å ha 2 LN-kanaler: en åpnet opprinnelig med autopilot (kanal A) og en med mer innkommende likviditet, åpnet med Dunder (kanal B).
![Demo Blixt 10](assets/blixt_t10.webp)
Bra, nå er du klar til å sende og motta nok sats over LN!

## Tredje Steg - Gjenopprettingsprosedyre for Node

La oss nå diskutere hvordan man gjenoppretter en Blixt-lommebok eller en annen LND-node som har krasjet. Dette er litt mer teknisk, men vær oppmerksom. Det er ikke så vanskelig.

> PÅMINNELSE: I fortiden skrev jeg en dedikert guide med flere alternativer [hvordan gjenopprette en krasjet LND-node](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario), hvor jeg også nevnte metoden for å bruke Blixt som en rask gjenopprettingsprosess, ved å bruke seed + channel.backup-filen fra din døde LND-node. Jeg skrev også en guide om hvordan du gjenoppretter din Blixt-node eller migrerer din Blixt til en annen enhet, [her](https://blixtwallet.github.io/faq#blixt-restore).

![Demo Blixt 11](assets/blixt_t11.webp)

Men la oss forklare denne prosessen i enkle steg. Som du kan se på bildet ovenfor, er det 2 ting du må gjøre for å gjenopprette din tidligere Blixt/LND-node:
- øverste boks er hvor du må fylle inn alle 24 ordene fra din seed (gamle / døde node)
- nederst er det to knappealternativer for å sette inn / laste opp channel.backup-filen, tidligere lagret fra din gamle Blixt/LND-node. Det kan være fra en lokal fil (du lastet den opp til enheten din tidligere) eller kan være fra en Google Drive / iCloud fjernplassering. Blixt har denne muligheten til å lagre dine kanalers backup direkte til en Google / iCloud-stasjon. Se flere detaljer på [Blixt Features Page](https://blixtwallet.github.io/features#blixt-options).

Det er også verdt å nevne, hvis du tidligere ikke hadde noen åpne LN-kanaler, er det ikke nødvendig å laste opp noen channels.backup-fil. Bare sett inn de 24 seed-ordene og trykk på gjenopprett-knappen.

Ikke glem å aktivere Tor, fra toppmenyen med 3 prikker, som vi forklarte i "Første Steg"-kapittelet i denne guiden. Det er tilfellet når du KUN hadde Tor-peers og ikke kunne kontaktes over clearnet (domene/IP). Ellers er det ikke nødvendig.

En annen nyttig funksjon er å sette en spesifikk Bitcoin-node fra den øverste menyen. Som standard synkroniserer den blokker fra node.blixtwallet.com (neutrino-modus), men du kan sette en hvilken som helst annen Bitcoin-node som tilbyr neutrino-synkronisering.

Så når du har fylt ut disse alternativene, og trykket på gjenopprett-knappen, vil Blixt først starte å synkronisere blokkene gjennom Neutrino som vi forklarte i "Første Steg"-kapittelet i denne guiden. Så vær tålmodig og følg gjenopprettingsprosessen på hovedskjermen, ved å klikke på synkroniseringsikonet.

![Demo Blixt 12](assets/blixt_t12.webp)

Som du kan se i dette eksemplet, viser det at bitcoin-blokkene er 100% synkronisert (A) og gjenopprettingsprosessen er i gang (B). Det betyr at LN-kanalene du hadde tidligere, vil bli lukket og midlene gjenopprettet til din Blixt onchain-lommebok.

Denne prosessen tar tid! Så vær tålmodig og prøv å holde din Blixt aktiv og online. Den første synkroniseringen kan ta opptil 6-8 min og lukking av kanaler kan ta opptil 10-15 min. Så det er best å ha enheten godt ladet.
Når denne prosessen er startet, kan du sjekke i Magic Drawer - Lightning Channels, statusen for hver av dine tidligere kanaler, som viser at de er i "venter på å lukke"-status. Når hver kanal er lukket, kan du se lukkingstransaksjonen i onchain-lommeboken (se Magic Drawer - Onchain), og åpne transaksjonsmenyloggen.
![Demo Blixt 13](assets/blixt_t13.webp)

Det vil også være bra å sjekke og legge til, hvis de ikke allerede er der, dine tidligere peers du hadde i din gamle LN-node. Så gå til Innstillinger-menyen, ned til "Lightning Network" og gå inn på alternativet "Vis Lightning Peers".

![Demo Blixt 14](assets/blixt_t14.webp)

Innenfor denne seksjonen vil du se de peers du er koblet til i det øyeblikket, og du kan legge til flere, bedre å legge til de du hadde kanaler med før. Bare gå til Amboss-siden, søk etter dine peer-noders aliaser eller nodeID og skann deres node URI.

![Demo Blixt 15](assets/blixt_t15.webp)

Som du kan se på bildet over, er det 3 aspekter:

A - representerer clearnet node-adressen URI (domene/IP)

B - representerer Tor onion node-adressen URI (.onion)

C - er QR-koden for å skanne med Blixt-kameraet ditt eller kopieringsknappen.

Denne node-adressen URI må du legge til i din liste over peers. Så vær oppmerksom på at det ikke er nok bare med node-aliasnavnet eller nodeID.

Nå kan du gå til Magic Drawer (øverste venstre meny) - Lightning Channels, og du kan se ved hvilken modenhetsblokkhøyde midlene vil bli returnert til din onchain-adresse.

![Demo Blixt 16](assets/blixt_t16.webp)

Det blokknummeret 764272 er når midlene vil være brukbare i din bitcoin onchain-adresse. Og det kan ta opptil 144 blokker fra den første bekreftelsesblokken til de blir frigitt. Så sjekk det på [mempool](https://mempool.space/).

Og det er det. Bare vent tålmodig til alle kanaler er lukket og midlene tilbake i din onchain-lommebok.

## Fjerde Steg - Tilpasning

Dette kapittelet handler om tilpasning og å kjenne din Blixt Node bedre. Jeg vil ikke beskrive alle funksjonene som er tilgjengelige, det er for mange og de ble allerede forklart på [Blixt Features Page](https://blixtwallet.github.io/features).

Men jeg vil peke ut noen av de som er nødvendige for å gå videre med å bruke din Blixt og ha en flott opplevelse.

### A - Navn (NameDesc)

![Demo Blixt 17](assets/blixt_t17.webp)

[The NameDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) er en standard for å formidle "mottakernavn" i BOLT11-fakturaer.

Dette kan være hvilket som helst navn og kan endres når som helst.

Dette alternativet er virkelig nyttig i ulike tilfeller, når du ønsker å sende et navn sammen med fakturabeskrivelsen, slik at mottakeren kan få et hint fra hvem de mottok disse satsene fra. Dette er helt valgfritt og også på betalingsskjermen, må brukeren krysse av i boksen som indikerer å sende aliasnavnet.

Her er et eksempel på hvordan det ville se ut når du bruker [chat.blixtwallet.com](https://chat.blixtwallet.com/)

![Demo Blixt 18](assets/blixt_t18.webp)

Dette er et annet eksempel på å sende til en annen lommebokapp som støtter NameDesc:

![Demo Blixt 19](assets/blixt_t19.webp)

### B - Sikkerhetskopiering av LN-kanaler og seed-ord

Dette er en veldig viktig funksjon!
Etter å ha åpnet eller lukket en LN-kanal, bør du ta en sikkerhetskopi. Det kan gjøres manuelt ved å lagre en liten fil på lokal enhet (vanligvis i nedlastingsmappen) eller ved å bruke en Google Drive- eller iCloud-konto.
![Demo Blixt 20](assets/blixt_t20.webp)

Gå til Blixt-innstillinger - Wallet-seksjonen. Der har du mulighetene til å lagre all viktig data for din Blixt-lommebok:
- “Show mnemonic” - vil vise de 24 ordene i frøet slik at du kan skrive dem ned
- “Remove mnemonic from device” - dette er valgfritt og bør kun brukes hvis du virkelig ønsker å fjerne frøordene fra enheten din. Dette vil IKKE slette lommeboken din, kun frøet. Men vær oppmerksom! Det er ingen måte å gjenopprette dem på hvis du ikke skrev dem ned først.
- “Export channel backup” - denne muligheten vil lagre en liten fil på din lokale enhet, vanligvis i “nedlastinger”-mappen, hvor du kan ta den og flytte den ut av enheten din, for sikker oppbevaring.
- “Verify channel backup” - dette er en god mulighet hvis du bruker Google Drive eller iCloud for å sjekke integriteten til sikkerhetskopien gjort eksternt.
- “Google drive channel backup” - vil lagre sikkerhetskopifilen i din personlige Google Drive. Filen er kryptert og lagres i et separat repositorium enn dine vanlige Google-filer. Så det er ingen bekymringer for at den kan leses av noen. Uansett er den filen helt ubrukelig uten frøordene, så ingen kan ta midlene dine fra kun den filen.

Jeg vil anbefale for denne seksjonen følgende:
- bruk en passordbehandler for å trygt lagre ditt frø og sikkerhetskopifil. [KeePass](https://keepass.info/) eller Bitwarden er veldig gode for dette og kan brukes på flere plattformer og være selvhostet eller offline.
- GJØR SIKKERHETSKOPIEN HVER GANG du åpner eller lukker en kanal. Den filen oppdateres med kanalinfo. Det er ikke nødvendig å gjøre det etter hver transaksjon du har gjort på LN. Kanalsikkerhetskopien lagrer ikke den infoen, den lagrer kun statusen til kanalen.

![Demo Blixt 21](assets/blixt_t21.webp)

## Konklusjon

OK, det er mange andre fantastiske funksjoner som Blixt tilbyr, jeg vil la deg oppdage dem en etter en og ha det gøy.

Denne appen er virkelig undervurdert, hovedsakelig fordi den ikke støttes av noen VC-finansiering, den er drevet av fellesskapet, bygget med kjærlighet og lidenskap for Bitcoin og Lightning Network.

Denne mobile LN-noden, Blixt, er et veldig kraftig verktøy i hendene på mange brukere, hvis de vet hvordan de skal bruke det godt. Bare forestill deg, du går rundt i verden med en LN-node i din egen lomme og ingen vil vite det.

Og ikke å snakke om alle de andre rike funksjonene som følger med, som svært få eller ingen andre lommebok-apper kan tilby.

Jeg håper du nyter å bruke den. Personlig elsker jeg den og den er veldig nyttig for meg (se her et bruksområde hvor denne lommeboken er et flott verktøy).

GOD BITCOIN LIGHTNING!

Måtte ₿ITCOIN være med deg!

> FRASKRIVELSE: Jeg blir ikke betalt eller støttet på noen måte av utviklerne av denne appen. Jeg skrev denne guiden fordi jeg så at interessen for denne lommebok-appen øker og nye brukere fortsatt ikke forstår hvordan de skal starte med den. Også for å hjelpe Hampus (hovedutvikleren) med dokumentasjon om bruk av denne noden-lommeboken. Jeg har ingen andre interesser i å fremme denne LN-appen, annet enn å fremme adopsjonen av Bitcoin og LN. Dette er den eneste veien!