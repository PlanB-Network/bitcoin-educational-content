---
name: Zeus Embedded - Avansert
description: Selvforvaltende Wallet med flere noder
---

![Zeus](assets/cover.webp)


## Introduksjon til ZEUS Wallet


ZEUS er en mobil Bitcoin Wallet- og nodeadministrasjonsapp med alle funksjonene til en Bitcoin lightning Wallet som gjør Bitcoin-betalinger enkle, gir brukerne full kontroll over økonomien og lar mer avanserte brukere administrere Lightning-nodene sine fra håndflaten.


### Hvem er ZEUS for?

For øyeblikket er ZEUS for folk som driver sine egne [Lightning Network Daemon (LND)](https://lightning.engineering/) eller [Core Lightning Lightning (CLN)](https://blockstream.com/lightning/) hjemme- / bedriftsnoder og administrerer dem gjennom Zeus, eksternt.


Selgere som bruker [BTCPay] (https://btcpayserver.org/) eller [LNBits] (https://lnbits.com/) eller [Alby] (https://getalby.com/) (eller en hvilken som helst annen LNDhub-konto) kan også koble seg til, bruke og administrere nodene/kontoene sine fra ZEUS.


[Fra og med v0.8](https://blog.zeusln.com/zeus-v0-8-0-open-beta/) vil ZEUS begynne å henvende seg til gjennomsnittlige brukere som bare vil ha en enkel måte å foreta raske, billige Bitcoin-betalinger fra mobilenheten sin ved å ha en [innebygd mobil Lightning-node](https://docs.zeusln.app/category/embedded-node) med en integrert [Lightning Service Provider (LSP)](https://docs.zeusln.app/lsp/intro).


### Viktige Zeus-ressurser:


- Zeus' offisielle nettside - [https://zeusln.app/](https://zeusln.app/)
- Zeus Documentation - [https://docs.zeusln.app/](https://docs.zeusln.app/)
- [Zeus Github repository] (https://github.com/ZeusLN/zeus)
- [Zeus Telegram støttegruppe] (https://t.me/ZeusLN)
- [Zeus på NOSTR] (https://iris.to/zeus@zeusln.app)
- [Zeus Blog Announcements] (https://blog.zeusln.com)


### Zeus-funksjoner

#### Generelle funksjoner:


- Selvforvaring, kun Bitcoin og Lightning Wallet
- Ingen behandlingsgebyrer, ingen KYC
- Helt åpen kildekode (APGLv3)
- Støtte for flere noder/kontoer (du kan administrere din(e) egen(e) hjemmenode(r), kjøre innebygd LND-node, koble til flere LNDhub-kontoer)
- Brukervennlig aktivitetsmeny
- PIN- eller passphrase-kryptering, personvernmodus - skjul sensitive data
- Kontaktbok, flere temaer, flere språk


#### Tekniske egenskaper


- Koble til via Tor
- Full LNURL-støtte (betaling, uttak, autentisering, kanal), send til Lightning-adresser
- Detaljert styring av belysningskanaler, MPP/AMP-støtte, Keysend, styring av rutingavgifter
- Replace-by-fee (RBF) og Barn betaler for foreldre (CPFP) støtte
- NFC-betalinger og -forespørsler, Signering og verifisering av meldinger
- Støtte for SegWit og Taproot
- Enkle Taproot-kanaler
- Adresser for selvforvaltende lynnedslag (@zeuspay.com)
- Point of Sale by Square (snart åpen PoS)


### Veiledninger og videoveiledninger

For å kunne bruke Zeus og administrere Lightning-kanaler, likviditet, gebyrer osv., er det bedre å først lese noen viktige guider om Lightning Network.


#### Guider:


- [LND - Lightning Network Daemon Dokumentasjon](https://docs.lightning.engineering/)
- [CLN - Core Lightning Documentation] (https://lightning.readthedocs.io/index.html)
- [Lynguide for nybegynnere] (https://bitcoiner.guide/lightning/) - av Bitcoin Q&A
- [Lightning Node Management] (https://www.lightningnode.info/) - by openoms
- [Lightning Network og flyplassanalogien] (https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [Håndtering av lynknutepunktlikviditet] (https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [Vedlikehold av lynknutepunkt] (https://darthcoin.substack.com/p/lightning-node-maintenance)


#### Videoopplæring av BTC Sessions


![Zeus Bitcoin Lightning Wallet - Mobile Node Management](https://youtu.be/hmmehTnV3ys)



## En gjennomgang av hvordan du begynner å bruke Zeus LN innebygd node på den mobile enheten din


![Image](assets/en/01.webp)


Jeg dedikerer denne veiledningen til alle de nye Lightning Network (LN)-brukerne som ønsker å starte en ny suveren reise ved hjelp av en selvforvaringsnode Wallet på sine mobile enheter.


La oss tenke oss at du allerede har gått gjennom all den overfloden av depot LN-lommebøker, men at du ennå ikke er klar til å begynne å kjøre en PUBLIC-routing LN-node, du vil bare stable mer Sats over LN på en mer selvforvaltende måte og foreta de vanlige betalingene dine over LN.


Her kommer Zeus, som starter med [versjon v0.8.0 kunngjort på bloggen deres] (https://blog.zeusln.com/new-release-zeus-v0-8-0/), og tilbyr nå en innebygd LND-node i appen. Inntil nå var Zeus en ekstern nodeadministrasjonsapp + LNDhub-kontoer. Men nå ... noden er i telefonen!


![Image](assets/en/02.webp)


### En rask oppsummering av hovedfunksjonene for Zeus Node:



- Privat LND-node** - Det betyr at denne noden IKKE vil gjøre offentlig ruting av andres betalinger gjennom noden din. Noden og kanalene er uannonserte (private, ikke synlige på den offentlige LN-grafen). Å motta og utføre betalinger vil bli gjort gjennom dine tilkoblede LSP-kolleger. HUSK: Zeus Embedded Node vil IKKE gjøre offentlig ruting!
- Vedvarende LND-tjeneste** - brukeren kan aktivere denne funksjonen og holde LND-tjenesten aktiv kontinuerlig som en vanlig LN-node. Appen trenger ikke å være åpen, den vedvarende tjenesten vil holde all kommunikasjon online.
- Neutrino-blokkfiltre ** - blokksynkronisering gjøres ved hjelp av [blokkfiltre og Neutrino-protokollen] (https://bitcoinops.org/en/topics/compact-block-filters/) (gitt ingen informasjon om våre brukeres On-Chain-midler). Påminnelse: for høy latens / langsomme internettforbindelser kan denne blokksynkroniseringen basert på neutrino noen ganger mislykkes. Hvis du prøver å bytte til en nøytrino-server i nærheten, kan det bidra til å gjenopprette synkroniseringen. Uten denne synkroniseringen kan ikke LND-noden din starte!
- Enkle Taproot-kanaler** - Når disse kanalene stenges, påløper det mindre gebyrer og brukerne får mer privatliv, ettersom de ser ut som alle andre Taproot-utgifter når de undersøker On-Chain-fotavtrykket sitt.
- Integrert LSP** - Olympus er den nye LSP-noden for Zeus. Brukere kan motta Sats over LN med en gang, uten å ha satt opp LN-kanaler tidligere. De må bare opprette en LN Invoice og betale fra en hvilken som helst annen LN Wallet, med Zeus 0-conf-kanaltjeneste. Les mer om Zeus LSP her. LSP gir også brukerne våre ekstra personvern ved å gi dem innpakkede fakturaer som skjuler nodenes offentlige nøkler for betalerne.
- Kontaktbok** - du kan lagre kontakter manuelt eller importere fra NOSTR, slik at du enkelt kan sende betalinger til dine vanlige destinasjoner.
- Full støtte for LNURL, LN Address send og motta** - nå kan du sette opp din egen LN Address med @zeuspay.com. Påminnelse: Du kan også bruke Zeus for LN-autentisering på nettsteder der du kan logge inn med en LN-autentisering. Det er veldig praktisk.
- Point of Sale** - Nå kan kjøpere sette opp sine egne produkter og selge direkte fra Zeus, med integrert PoS. Inneholder for øyeblikket grunnleggende behov, men vil i fremtiden inneholde utvidede funksjoner.
- LND-logger** - brukeren kan lese LND-tjenesteloggene i sanntid og bruke dem til å feilsøke mulige problemer (hovedsakelig for dårlige tilkoblinger)
- Automatiserte sikkerhetskopier ** - LN-nodekanalene sikkerhetskopieres automatisk på Olympus-serveren. Denne automatiserte sikkerhetskopien er kryptert med noden Wallet seed (uten seed er den helt ubrukelig). Brukeren kan også eksportere manuelt en SCB (statisk kanalsikkerhetskopi) for katastrofegjenoppretting.


### Slik kommer du i gang med Zeus LN Node (LND innebygd)


I denne veiledningen vil jeg bare snakke om den innebygde LND-noden, og ikke om de andre måtene å bruke denne fantastiske appen på (ekstern nodeadministrasjon og LNDhub-kontoer). For andre typer tilkoblinger, se [Zeus Docs page] (https://docs.zeusln.app/category/getting-started), som er veldig godt forklart, og det er ikke nødvendig å skrive en egen guide.


#### TRINN 1 - INNLEDENDE OPPSETT


På grunn av det faktum at Zeus er en full LND-node, vil jeg ha noen innledende anbefalinger:



- Ikke bruk en gammel enhet, det kan påvirke bruken av denne kraftige appen. Spesielt i synkroniseringsperioden kan appen bruke CPU og RAM intensivt. Mangel på disse kan til og med gjøre det umulig å bruke Zeus-appen.
- Bruk minst Android 11 som mobil OS og oppdatert så mye som mulig. For iOS det samme, prøv å bruke en mye høyere versjon av OS.
- Du trenger minst 1 GB diskplass for datalagring. Med tiden kan det bli mer, men det finnes en funksjonalitet for å komprimere databasen til et nivå på MB.
- Det er INGEN grunn til å bruke Zeus med Tor eller Orbot-tjenesten. Vennligst ikke kompliser ting mer enn nødvendig. Tor vil i dette tilfellet ikke gi deg mer personvern, men bare gjøre ting verre for den første synkroniseringen. Vær også forsiktig med hvilke VPN-er du bruker, og sjekk ventetiden for tilkoblingen mot Neutrino-servere. Husk at Neutrino blokkeringsfilter ikke lekker eller sporer enhetens identitet, men bare serverer blokkeringer. LN-trafikken er også bak en LSP med private kanaler, så svært lite informasjon er ute, det er ingen grunn til å bekymre seg for personvernet.
- Ha tålmodighet med den første synkroniseringen, som kan ta flere minutter. Prøv å være koblet til en bredbåndstilkobling med god latenstid. Hvis du kjører din egen Bitcoin-node, [kan du aktivere Neutrino-tjenesten] (https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) og koble Zeus til din egen node, til og med ved hjelp av det interne LAN, slik at du får maksimal hastighet.


Når du har konfigurert tilkoblingstypen "Embedded node", vil appen begynne å synkronisere en stund. Vent tålmodig til du er ferdig med den delen, og gå deretter inn på hovedinnstillingssiden.


![Image](assets/en/03.webp)


La oss kort gå inn i hver av innstillingsseksjonene og forstå noen av hovedfunksjonene før du begynner å bruke Zeus:


**A - INNSTILLINGER**


Dette er en seksjon med generelle innstillinger for hele appen


**1 - Lightning Service Provider (LSP)**


Her presenteres to LSP-tjenester:



- _Just in time-kanaler_ - når du ikke har noen kanal åpen eller innkommende likviditet tilgjengelig, vil tjenesten åpne en kanal for deg hvis den er aktivert. Dette alternativet kan deaktiveres hvis du ikke ønsker å åpne flere kanaler av denne typen.
- _Bestill kanaler på forhånd_ - du kan kjøpe inngående kanaler fra Olympus LSP direkte i appen med flere alternativer og beløp (for innkommende og utgående).


LSP bidrar til å koble brukere til Lightning Network ved å åpne opp betalingskanaler til nodene deres. [Les mer om LSP her](https://medium.com/breez-technology/envisioning-lsps-in-the-lightning-economy-832b45871992). ZEUS har en ny LSP integrert i seg som heter [OLYMPUS by ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581), som er tilgjengelig for alle brukere som bruker den nye innebygde noden.


I denne delen er Olympus LSP (https://0conf.lnolymp.us) standard, men snart kan du også angi en annen 0conf LSP som støtter denne protokollen.


_Husk å huske:_

når du åpner en kanal med Olympus LSP ved hjelp av de innpakkede LN-fakturaene, får du også en 100 000 inngående likviditet! Dette er et veldig godt alternativ i tilfelle du trenger å motta mer Sats med en gang

eksempel: du setter inn 400 000 Sats for å åpne en LSP-kanal, så åpner LSP-en en kanal med kapasitet på 500 000 Sats mot Zeus-noden din og skyver de 400 000 Sats du setter inn mot din side

_"Innkommende likviditet" = mer "plass" i kanalen din til å ta imot


I fremtiden håper vi at vi kan ha mange andre LSP-er som kan integreres i Zeus og bruke hver enkelt av dem alternativt. Det er bare et spørsmål om tid før nye LSP-er vil ta i bruk en åpen standard for denne typen 0conf-kanaler.


Hvis du ikke ønsker å åpne nye kanaler "on the fly", kan du deaktivere dette alternativet.


I samme seksjon har du også muligheten til å velge "request Simple Taproot Channels" når LSP-en vil åpne en kanal mot Zeus-noden din. Disse enkle Taproot-kanalene gir bedre On-Chain-personvern og lavere avgifter ved kanalstenging. Det er bare to grunner til at du ikke ønsker å bruke dem:



- De er nye, og det kan fortsatt være feil i LND når du bruker dem.
- Motparten din støtter dem ikke. Selv LND-noder må eksplisitt velge dem, inntil videre.


**2 - Betalingsinnstillinger**


Denne funksjonen gir deg muligheten til å angi dine egne foretrukne gebyrer for betalinger, over LN eller onchain. Du får også muligheten til å øke eller redusere tidsavbruddet for fakturaene dine.


Hvis noen av LN-betalingene dine mislykkes, kan du øke gebyret for å finne en bedre rute. Hvis du gjør tx-er i kjeden, kan du også sette opp et spesifikt gebyr slik at tx-en din ikke kan bli sittende fast i Mempool i lang tid, i tilfelle høye gebyrer.


**3 - Fakturainnstillinger**


I denne delen finner du noen alternativer for generate-fakturaer:



- Angi et standardnotat som skal vises i Invoice eller generate
- Utløpstid i sekunder, i tilfelle du vil ha spesifikk tid, lengre eller kortere for at Invoice skal betales
- Inkluder rutehint - gi informasjon for å finne ikke-annonserte, eller private, kanaler. Dette gjør det mulig å rute betalinger til noder som ikke er offentlig synlige i nettverket. Et rutingstips gir en delvis rute mellom mottakerens private node og en offentlig node. Dette rutingstipset inkluderes deretter i Invoice som genereres av mottakeren og leveres til betaleren. Jeg foreslår at det aktiveres som standard, ellers kan innkommende betalinger mislykkes (ingen rute funnet).
- AMP Invoice - Atomic Multi-path Payments er en ny type lynbetalinger implementert av LND som gjør det mulig å motta Sats uten en spesifikk Invoice, ved hjelp av [keysend] (https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend). Er praktisk talt en statisk betalingskode. [Les mer her](https://docs.lightning.engineering/lightning-network-tools/LND/amp).
- Vis egendefinerte felt i forhåndsbildet - bruk dette alternativet bare i helt spesielle tilfeller når du virkelig ønsker å bruke egendefinerte felt i forhåndsbildet. [Les mer her](https://Bitcoin.stackexchange.com/questions/90797/how-can-i-generate-preimage-for-lightning-network-Invoice-should-i).


Et annet alternativ i denne delen er hvordan du angir hvilken type Address i kjeden du vil bruke: SegWit nestet, SegWit, Taproot.


![Image](assets/en/04.webp)


Klikk på den øverste hjulknappen, og et popup-vindu vises der du kan velge ønsket type Address. Når du har angitt dette, vil neste gang du trykker på mottaksknappen for onchain, vil generate velge den Address-typen du har valgt. Du kan endre den når som helst.


**4 - Kanalinnstillinger**


I denne delen forhåndsinnstiller du noen funksjoner for åpningskanaler, f.eks:



- antall bekreftelser
- Kunngjør kanal (standard er av), det betyr at det vil være uannonserte kanaler
- Enkle Taproot-kanaler
- Vis kjøpsknapp for kanal


**5 - Personverninnstillinger**


Her finner du noen grunnleggende innstillinger for å legge til mer personvern ved hjelp av Zeus-appen:



- Block explorer for å åpne tx-detaljer (Mempool.space, blockstream.info eller tilpasset personlig)
- Les utklippstavle - slå av/på hvis du vil at Zeus skal lese utklippstavlen på enheten din
- Lurker-modus - slå av/på hvis du vil skjule spesifikk sensitiv informasjon fra Zeus-appen din. Er et godt alternativ når du lager demoer eller skjermbilder.
- Mempool avgiftsforslag - aktiver dette alternativet hvis du ønsker å bruke anbefalte avgiftsnivåer fra [Mempool.space] (https://Mempool.space/)


**6 - Sikkerhet**


Denne delen har bare to alternativer for å sikre appen ved åpning: angi et passord eller en PIN-kode.


Når du har angitt en PIN-kode for å åpne appen, kan du også angi en "tvang-PIN-kode". Denne hemmelige ekstra PIN-koden vil KUN bli brukt i en tvangssituasjon, hvis du blir truet. Hvis du setter denne PIN-koden, vil konfigurasjonen bli slettet. Så du bør holde sikkerhetskopiene dine oppdatert. Automatiske sikkerhetskopier er PÅ som standard, men det er bra å ha dine egne sikkerhetskopier også, utenfor enheten.


**7 - Valuta**


Aktiver eller deaktiver muligheten til å vise en fiat-valutakonvertering i Zeus-appen. For øyeblikket støtter appen over 30 fiat-valutaer over hele verden.


**8 - Språk**


Du kan veksle mellom flere oversettelsesspråk, som er gjennomgått av Zeus-fellesskapet med morsmålstalere.


**9 - Display**


I denne delen kan du tilpasse Zeus-skjermen ved å velge ulike fargetemaer, standardskjerm (tastatur eller balanse), vise nodealiaset ditt, aktivere store tastaturknapper og vise flere desimaler.


**10 - Utsalgssted**


Dette er en spesiell funksjon for å aktivere/deaktivere et integrert PoS-system i Zeus. Du kan kjøre en frittstående PoS eller koblet til et Square PoS-system. For øyeblikket støtter grunnleggende funksjoner som en PoS, men nok for en god start og kan hjelpe de små kjøpmennene (barer / restauranter, dagligvarer) til å begynne å akseptere BTC på en innfødt måte.


I disse innstillingene finner du ulike alternativer for å konfigurere PoS:



- Bekreftelse av betalingstype: Kun LN, 0-conf, 1-conf
- Aktiver/deaktiver tips for ansatte som betjener PoS
- Vis / skjul tastaturet
- Skatteprosent som skal brukes på billetten
- Opprett produkter og produktkategorier
- En enkel oversikt over alle salg


Her er en live demo-video om hvordan du bruker Zeus PoS:


**B - Backup Wallet**


Den innebygde noden i ZEUS er basert på LND og bruker [aezeed seed-formatet] (https://github.com/lightningnetwork/LND/blob/master/aezeed/README.md). Dette er annerledes enn det typiske [BIP39-formatet](https://github.com/Bitcoin/bips/blob/master/bip-0039.mediawiki) du ser i de fleste Bitcoin-lommebøker, selv om det kan se ut til å være likt. Aezeed inkluderer noen ekstra data, inkludert fødselsdatoen til Wallet, som vil bidra til at nye skanninger under gjenoppretting skjer mer effektivt.


Aezeed-nøkkelformatet skal være kompatibelt med følgende mobile lommebøker: Blixt, BlueWallet og Breez. Merk at seed alene vil være utilstrekkelig for å gjenopprette alle saldoene dine hvis du har åpne eller ventende lukkingskanaler!


Finn ut mer om sikkerhetskopierings- og gjenopprettingsprosessen på [Zeus Docs page] (https://docs.zeusln.app/for-users/embedded-node/backup-and-recovery).


POWER ADVICE: Når du lagrer seed, må du også lagre nodepubnøkkelen! Noen ganger er det bra å ha den tilgjengelig, sammen med seed og SCB (Static Channels Backup) i tilfelle du trenger å verifisere gjenopprettingen.


SCB er bare nødvendig hvis du har LN-kanaler åpne. Hvis du bare har midler i kjeden, er det ikke nødvendig.


Hvis du ser at etter lang tid fremdeles ikke viser den gamle historikken txs, gå til Embedded node - Peers og deaktiver alternativet for å bruke listen over valgte peers (som standard er btcd.lnolymp.us). Det vil utløse en omstart og vil koble til den første tilgjengelige nøytrino-noden med bedre tidsrespons. Eller bruk de nedenfor nevnte andre velkjente nøytrino-peers.


Hvis du vil se flere gjenopprettingsalternativer for en LND-node, [vennligst les min tidligere guide] (https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), hvor du kan finne trinnene for hvordan du importerer en aezeed seed til Sparrow Wallet eller andre metoder.


**C - Innebygd node**


I denne delen finner du noen grunnleggende verktøy for å administrere den integrerte noden:



- _Disaster Recovery_ - Automatiserte og manuelle sikkerhetskopier for LN-kanalene. Les mer om hvordan du bruker denne funksjonen på Zeus Docs-siden.
- _Express Graph Sync_ - Zeus-appen laster ned LN-sladderdatagrafen fra en dedikert server, for raskere og bedre synkronisering, og tilbyr de beste betalingsveiene. Du kan også velge å slette tidligere grafdata ved oppstart.
- _Peers_ - seksjon for å administrere nøytrino-peers og 0-conf-peers. Hvis du har problemer med innledende synkronisering, kanaler som ikke kommer på nett, er det fordi enheten din har høy ventetid med den konfigurerte neutrino-peeren. Prøv å bytte fra listen over foretrukne motparter eller legg til en bestemt motpart som du vet har bedre ventetid for synkronisering. Velkjente Neutrino-servere er:



 - btcd1.lnolymp.us | btcd2.lnolymp.us - for USA-regionen
 - sg.lnolymp.us - for Asia-regionen
 - btcd-Mainnet.lightning.computer - for USA-regionen
 - uswest.blixtwallet.com (Seattle) - for USA-regionen
 - europe.blixtwallet.com (Tyskland) - for EU-regionen
 - asia.blixtwallet.com - for Asia-regionen
 - node.eldamar.icu - for USA-regionen
 - noad.sathoarder.com - for USA-regionen
 - bb1.breez.technology | bb2.breez.technology - for USA-regionen
 - neutrino.shock.network - amerikansk region



- _LND logs_ - svært nyttig verktøy for å feilsøke problemer med LN-noden og kontrollere i dybden hva som skjer på et mer teknisk nivå.
- _Avanserte innstillinger_ - flere verktøy for å kontrollere bruken av LND-noden:



 - _Pathfinding mode_ - bimodal eller apriori, måter å finne en bedre rute for LN-betalingene dine og også tilbakestille tidligere ruteinformasjon. Vennligst les disse veldig gode guidene om pathfinding: [Pathfinding] (https://docs.lightning.engineering/lightning-network-tools/LND/pathfinding) - av Docs Lightning Engineering og [LN Payment Pathfinding] (https://voltage.cloud/blog/lightning-network-faq/understanding-payment-pathfinding-between-nodes-on-lightning-network/) - av Voltage
 - _Persistent LND_ - aktiver denne modusen hvis du vil at LND-tjenesten skal kjøre kontinuerlig i bakgrunnen og holde noden din online 24/7. Dette er svært nyttig hvis du bruker Zeus som PoS i en liten butikk eller hvis du mottar mange LN-tips via LN Address.
 - _Rescan wallet_ - dette alternativet vil utløse en full skanning av alle tx-er i kjeden på Wallet ved omstart. Aktiver det bare i tilfelle du mangler noen tx-er i Wallet. Rescan-oppgaven vil ta tid, flere minutter, så vær tålmodig og sjekk alltid loggene for å se mer informasjon om fremdriften.
 - _Compact Database_ - dette alternativet er veldig nyttig hvis Zeus-appen din tar opp mye plass på enheten (se appdetaljer i enhetsinnstillingene). Hvis du har mye aktivitet med Zeus, vil jeg anbefale å gjøre denne komprimeringen oftere. Når du ser at du har mer enn 1-1,5 GB data for Zeus-appen, kan du utføre komprimeringen. Det vil starte på nytt og ta litt tid, så vær tålmodig.
 - _Delete Neutrino files_ - dette alternativet for å slette neutrino-filene (med en omstart) vil redusere datalagringsbruken mye. Å redusere databruken har også en stor innvirkning på batteribruken, spesielt hvis du bruker Zeus i vedvarende modus.


**D - Knutepunktinformasjon**


I denne delen finner du mer informasjon om statusen til Zeus-noden din:



- Alias - kort node-ID
- Offentlig nøkkel - den fullstendige offentlige nøkkelen for noden din som kreves for at andre noder skal finne veien til noden din. Husk at denne offentlige nøkkelen IKKE er synlig på de vanlige LN Explorers (Mempool, Amboss, 1ML osv.). Denne offentlige nøkkelen kan KUN nås gjennom dine tilkoblede LN-peers og kanaler.
- LN-implementeringsversjon
- Zeus app-versjon
- Synkronisert med kjede og Synkronisert med grafstatus er svært viktige og viser korrekt status for noden. Hvis disse to ikke viser "true", betyr det at noden fortsatt synkroniserer eller har problemer med synkroniseringen. Vi anbefaler derfor at du ser på LND-loggene eller venter litt lenger.
- Blokkhøyde og Hash - viser den siste blokken og Hash som noden din så og synkroniserte.


**E - Nettverksinfo**


Denne delen viser flere detaljer om den generelle statusen for Lightning Network, hentet fra synkroniseringsdataene for grafen: antall tilgjengelige offentlige kanaler, antall noder, antall zombiekanaler (frakoblet eller døde), grafdiameter, gjennomsnittlig og maksimal grad for grafen.


Denne informasjonen kan være nyttig for feilsøking eller bare brukes til statistikk.


**F - Lyn Address**


I denne delen kan brukeren sette opp sin egen selvforvaring LN Address @zeuspay.com.


ZEUS PAY utnytter brukergenererte preimage-hashes, HODL-fakturaer og Zaplocker Nostr-attestasjonsordningen for å tillate brukere som kanskje ikke er online 24/7 å motta betalinger til en statisk lyn Address. Brukerne trenger bare å logge inn på ZEUS-lommebøkene sine innen 24 timer for å gjøre krav på betalingene, ellers vil de bli returnert til avsenderen.


Hvis du aktiverer "vedvarende modus", vil alle betalinger til din LN Address mottas umiddelbart.


Lær mer om hvordan [Zaplocker](https://github.com/supertestnet/zaplocker#how-it-works) betalinger fungerer og mer om [ZeusPay-gebyrer her](https://docs.zeusln.app/lightning-Address/fees).


**G - Onchain-adresser**


I denne delen kan du se dine genererte onchain-adresser for å få bedre kontroll over mynten


**H - Kontakter**


I Zeus v 0.8.0 ble det introdusert en ny kontaktbok som du kan bruke til å sende betalinger til venner og familie, også med muligheten til å importere kontaktene dine fra Nostr.


Bare skriv inn din Nostr npub eller lesbare NIP-05 Address, så vil ZEUS søke i Nostr etter alle kontaktene dine. Derfra kan du sende en rask betaling til en kontakt, eller importere alle eller utvalgte kontakter til din lokale kontaktbok


Her er en kort video om hvordan du konfigurerer og bruker Zeus-kontaktene dine:


**I - Verktøy**


Her har vi ulike underseksjoner med flere verktøy:



- _Accounts_ - her kan du importere eksterne kontoer/lommebøker, Cold-lommebøker, Hot-lommebøker, for å kontrollere eller bruke som ekstern finansieringskilde for Zeus-nodekanalene dine. Denne funksjonen er fortsatt eksperimentell.
- _Speed up transaction_ - Denne funksjonen kan være nyttig når du har en fastlåst tx inn i Mempool og ønsker å øke avgiften. Du må oppgi tx-utgangen fra tx-detaljer og velge ønsket nytt gebyr du vil bruke. Den må være høyere enn den forrige og krever at du har mer penger tilgjengelig i kjeden din Wallet.


![Image](assets/en/05.webp)


Du må gå til din ventende tx og kopiere txid-utpunktet. Gå deretter til denne delen og lim den inn, og velg deretter den nye avgiften du vil bruke for å øke den. Det vil dukke opp et nytt skjermbilde med anbefalte avgifter i det øyeblikket, eller du kan angi en tilpasset. Husk at den MÅ være høyere enn den forrige.


Det er alltid bedre å ha en UTXO med maksimalt 100k Sats i Zeus onchain Wallet, for å kunne bruke den til å støte avgifter når det er nødvendig.



- _Signer eller verifiser_ - Med denne funksjonen kan du signere en bestemt melding med Wallet-nøklene dine. Den kan også brukes til å verifisere en melding for å bevise at den kommer fra en spesifikk Wallet-nøkkel.
- _Currency converter_ - et enkelt verktøy for å beregne kursomregningen mellom BTC og andre fiat-valutaer.


**J - Merchandise og support**


Her finner du mer informasjon og lenker om Zeus, nettbutikk, sponsorer, sosiale medier.


**K - Hjelp**


I denne siste delen finner du lenker til Zeus-dokumentasjonssiden, Github-problemer (hvis du vil legge inn en feil eller forespørsel direkte til apputviklere), e-poststøtte.



### TRINN 2 - BEGYNN Å BRUKE ZEUS NODE



Husk at Zeus hovedsakelig skal brukes som en LN Wallet, for enkle og raske betalinger over LN. Jada, den inneholder også en Wallet på kjeden, men den skal utelukkende brukes til å åpne / lukke LN-kanaler og ikke for regelmessige betalinger av en kaffe.


Vennligst les den andre guiden min om [hvordan du kan være din egen bank ved hjelp av de tre nivåene i Stash] (https://darth-coin.github.io/beginner/be-your-own-bank-en.html).


I dette øyeblikket har brukeren to måter å begynne å bruke Zeus på:



- Rett over LN, ved hjelp av 0-conf-kanalen fra Olympus LSP
- Sett først inn penger i onchain Wallet, og åpne deretter en vanlig LN-kanal med den motparten du ønsker.


#### Metode A - Bruk av Olympus LSP


Dette er en veldig enkel og rett frem måte å onboarde en ny LN-bruker med Zeus. Det kan være en helt ny Bitcoin-bruker som ikke har noen Sats overhodet, som er onboardet av en venn, eller en ny kjøpmann som starter med sin første LN-betaling.


Som standard vil Zeus bruke sin egen LSP, Olympus. Men senere kan du også bytte til andre LSP-er som støtter denne 0-conf-protokollen for å åpne kanaler.


Ved å opprette en Invoice på Zeus (skriv inn beløpet og klikk på "forespørsel"-knappen), vil du kunne motta disse Sats med en gang.


Invoice du generate vil være [wrapped](https://docs.zeusln.app/lsp/wrapped-invoices), og du vil bli presentert for avgiftene knyttet til tjenesten hvis de er betalt. Denne innpakkede Invoice inneholder rutehint mot Zeus-noden din, slik at LSP-en kan finne den nye noden din og åpne en kanal med de nye midlene du setter inn.


![Image](assets/en/06.webp)


![Image](assets/en/07.webp)


For å få en LN-kanal fra LSP-en med midlene du ønsker å motta første gang, må denne Invoice betales fra en annen LN Wallet og vente noen øyeblikk til LSP-en åpner kanalen mot Zeus-noden din, trekker fra avgiften og skyver det resterende beløpet av betalingen på din side av kanalen.


Alt du trenger å gjøre er å betale Invoice generert for deg i ZEUS med en annen lyn Wallet, og kanalen din vil åpne umiddelbart. [Vennligst se Zeus LSP-avgifter] (https://docs.zeusln.app/lsp/fees).


En annen fordel med å betale for en kanal er ruting uten gebyr. Det betyr at når du ruter betalinger, påløper det ingen rutingsgebyrer for det første hoppet gjennom OLYMPUS by ZEUS. Merk at hopp utover OLYMPUS by ZEUS fortsatt vil belaste deg.


Når kanalen er klar, klikker du på den høyre knappen nederst på skjermen, som viser Zeus-kanalene.


![Image](assets/en/08.webp)


Og du vil se en kanal som denne, som viser din side av kanalbalansen:


![Image](assets/en/09.webp)


For mer du vil bruke fra denne kanalen, vil du ha mer inngående likviditet. For mer Sats du mottar i denne kanalen, vil du ha mindre inngående likviditetsplass.


Her er en enkel visuell demonstrasjon (av Rene Pickhardt) av hvordan LN-kanaler fungerer:


I dette øyeblikket, med tanke på demoskjermen for kanaler, klikker du på kanalnavnet og du vil se mer informasjon om det.


Du har en enkelt kanal med Olympus, med en total kapasitet på 490 000 Sats, med en balanse på 378 000 Sats på din side og 88 000 Sats på Olympus' side. Det betyr at du maksimalt kan motta 88 000 Sats mer i samme kanal.


Hvis du trenger å motta mer enn 88k Sats (den tilgjengelige innkommende likviditeten i dette tilfellet), la oss si ytterligere 500k Sats, ved ganske enkelt å opprette en ny LN Invoice med det beløpet, vil det utløse en ny kanalforespørsel til Olympus LSP. Så du vil få en 2. kanal.


For å unngå å betale flere avgifter for å åpne flere kanaler, anbefales det derfor å åpne en større kanal første gang, la oss si 1-2M Sats. Når den er åpen, kan du bytte ut en del av disse Sats, la oss si 50 %, ved å bruke en ekstern byttetjeneste som er beskrevet i denne veiledningen.


Når du bytter ut fra den kanalen, la oss si 50 %, og får tilbake Sats til din egen Zeus onchain Wallet, er du klar til å gå videre til neste metode for å åpne en ny kanal - fra onchain-balanse.


#### Metode B - Bruk av saldoen din i kjeden


Med denne metoden kan du åpne kanaler mot en hvilken som helst annen LN-node, inkludert den samme Olympus LSP. Men hvis du allerede har en kanal med Olympus, anbefales det å også ha en kanal med en annen node, for mer pålitelighet og også kunne bruke MPP (multi-part payment).


![Image](assets/en/10.webp)


Ovenfor er et eksempel på betaling av en LN Invoice ved hjelp av MPP. Som du kan se nederst på skjermen har du "innstillinger" og åpner en rullegardinmeny med flere detaljer for betalingen du er i ferd med å foreta. Hvis du har minst to kanaler åpne i dette skjermbildet, vil MPP-funksjonen være PÅ som standard. Du kan også aktivere AMP (atomic multi-path) og angi spesifikke deler du ønsker. Dette er en kraftig funksjon!


For en privat node som Zeus vil jeg anbefale å ha 2-3 gode kanaler (maks. 4-5), med gode LSP-er og god likviditet for å dekke alle dine behov for å betale eller motta Sats over LN. [Se flere råd om likviditet i LN-noden i denne veiledningen](/nodes/managing-lightning-node-liquidity-en.html). Her er også en annen [generell veiledning om LN-likviditet](https://Bitcoin.design/guide/how-it-works/liquidity/) fra Bitcoin Design team.


Å velge de riktige jevnaldrende, vet jeg, er ikke en enkel oppgave, selv for erfarne brukere. [Så jeg vil gi deg noen alternativer til å begynne med] (https://github.com/ZeusLN/zeus/discussions/2265), dette er peer-noder som jeg testet selv ved hjelp av Zeus (jeg prøvde å koble meg bare til LND-noder for å unngå inkompatibilitetsproblemer)


Her er også en liste over godkjente nodepeers for Zeus. Hvis du vet om noen som er gode, er du velkommen til å legge dem til i listen.


Du kan åpne en kanal i Zeus ved å gå til kanalvisningen ved å klikke på kanalikonet nederst i høyre hjørne av hovedvisningen, og deretter trykke på +-ikonet øverst i høyre hjørne.


![Image](assets/en/11.webp)


Hvis du vil åpne en kanal med en bestemt node, klikker du på (A) øverst i hjørnet for å skanne nodens QR-nodeID (på Mempool, Amboss, 1ML kan du få denne QR-en), og alle motpartsopplysningene vil bli fylt ut.


PÅMINNELSE:


- Zeus innebygde node bruker ikke Tor-tjenesten! Så vennligst ikke prøv å åpne kanaler med noder som er under Tor! Du gjør mer skade på deg selv enn å legge til mer privatliv. Tor for LN tilbyr ikke mer personvern, men gir mer problemer.
- velg med omhu dine jevnaldrende, bedre være gode LSP-er, gode rutingnoder, ikke tilfeldige pleb-noder som kan stenge kanalene dine og ikke kunne tilby god likviditet. [Her skrev jeg en dedikert guide] (https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) om likviditet og eksempel på noder.


Hvis du klikker direkte på knappen "Åpne kanal til Olympus", vil du fylle ut de nødvendige feltene for å åpne en kanal til [OLYMPUS by ZEUS] (https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581).


I motsetning til betalte LSP-kanaler, vil kanalen din kreve On-Chain-bekreftelse, ved hjelp av dine onchain-midler (du kan velge fra UTXO-ene dine i visningen for åpen kanal); den vil ikke åpnes umiddelbart. Se først de faktiske Mempool-gebyrene og juster dem deretter, avhengig av hvor raskt du ønsker å åpne kanalen.


Før du trykker på knappen for å åpne kanalen, skyver du ned de avanserte alternativene:


![Image](assets/en/12.webp)


Du må også sørge for at kanalen er uannonsert (privat). Som standard er alternativet slått av for annonserte kanaler. Dette alternativet anbefales ikke å være aktivert for Zeus innebygd node, og er bare nyttig når du bruker Zeus med den eksterne noden som en offentlig rutingsnode.


I motsetning til betalte LSP-kanaler vil du ikke dra nytte av ruting uten gebyr ved å åpne kanaler med denne metoden.


Og ferdig, bare klikk på knappen "Open Channel", vent på at tx skal bekreftes av gruvearbeiderne. Når kanalen er åpen, kan du handle som du ønsker med Sats fra kanalene dine.


Husk at disse kanalene vil ha all balansen på DIN side, så du vil ikke ha inngående likviditet. Som jeg sa tidligere, bytt ut eller bruk litt Sats på å kjøpe ting over LN for å "skape mer plass" til å motta.


Tenk på LN-kanalene dine som et glass vann. Du heller litt vann (Sats) i et tomt glass (kanalen din) til du fyller det opp. Du kan ikke helle mer vann før du har drukket litt (brukt/byttet ut). Når glasset nesten er tomt, heller du mer vann (Sats) i det ved å bruke en swap in. [Les mer om eksterne byttetjenester her] (https://darth-coin.github.io/nodes/lightning-submarine-swaps-en.html).


Det finnes også andre LSP-tjenester som selger deg inngående kanaler: LNBig eller Bitrefill. Jeg tror det er flere tjenester som disse, men kan ikke huske dem akkurat nå.


Så hvis du trenger en praktisk talt tom LN-kanal (saldoen er 100 % på motpartens side fra starten av), for å motta flere betalinger enn du kan håndtere på dine eksisterende fylte kanaler, kan dette være et veldig godt alternativ. Du betaler en spesifikk avgift for å åpne disse kanalene, og du får rikelig med innkommende plass.



## TIPS OG TRIKS


### Grenser for inngående reserver


Akkurat nå er det ikke mulig å motta nøyaktig hvor mye som vises i "Inbound" på grunn av noen begrensninger i LN-koden. Husk at du alltid bør fakturere med et litt mindre beløp, henholdsvis "Channel Local Reserve"-beløpet.


![Image](assets/en/13.webp)


Som du kan se i bildet ovenfor, viser "innkommende" det at jeg fortsatt kan motta 5101 Sats, men faktisk i dette øyeblikket er umulig å motta mer. Og du kan observere at det er det samme beløpet som "Local reserve".


Så husk at når du sender inn fakturaer, må du også ta en titt på likviditeten i kanalene dine og trekke fra den lokale reserven fra dette beløpet, hvis du ønsker å presse fordringsbeløpet til det ytterste.


### Et raskt råd til nye brukere som starter med Zeus node:



- Grip de nye kanalene dine på riktig måte.


Hvis du for eksempel vet at du vil motta, la oss si 1 million Sats om en uke, kan du åpne en Sats-kanal på 2 millioner Sats og bytte ut til Wallet i kjeden eller til en annen (midlertidig) LN-depotkonto for 50-60 % av den utgående likviditeten din. Vær alltid forberedt med mer likviditet. Når du trenger mer likviditet tilbake i Zeus-kanalene dine, kan du flytte den tilbake fra depotkontoene.


Hvis du vet at du kommer til å sende, la oss si 500 000 Sats i uken, kan du åpne en kanal med 1 million Sats. På denne måten vil du fortsatt ha en reserve til du fyller den opp igjen.



- Hvis du er en kjøpmann og du alltid vil motta mer enn du bruker regelmessig, bør du kjøpe en dedikert inngående kanal. Det er den billigste måten. Du betaler en minimal avgift og får en "tom" kanal.



- Ikke åpne små meningsløse kanaler på 50-100-300-500k Sats. Du vil fylle dem i løpet av noen dager, selv om du bare bruker dem til zaps. Åpne større og forskjellige, IKKE bare én kanal.


Når du har åpnet en større kanal, kan du alltid bruke eksterne ubåtbytter for å flytte Sats inn i lommebøkene dine i kjeden (inkludert tilbake til Zeus onchain). Det er bra å holde en balanse mellom inn- og utlikviditet, og du kan også "gjenbruke" disse Sats for å åpne flere kanaler hvis du vil.


### Innpakket Invoice


Hvis du vil legge til mer personvern når du mottar, kan du bruke metoden "wrapped Invoice". Påminnelse: for å kunne gjøre dette, trenger du en kanal med Olympus LSP. Innpakkede fakturaer vil "skjule" den endelige destinasjonen (Zeus-noden din) og vise LSP-noden din som destinasjon for betaleren.


For å få en innpakket Invoice, gå til hovedtastaturskjermen, skriv inn beløpet og trykk på forespørsel. Vil vise en vanlig QR-kode for din Invoice. Klikk nå på "X"-knappen øverst til høyre, og du vil bli omdirigert til flere alternativer for Invoice.


![Image](assets/en/14.webp)


Nå må du aktivere det alternativet øverst "Aktiver LSP" og trykke på "Opprett Invoice" -knappen. Dette alternativet vil opprette den innpakkede Invoice og husk, vil belaste et lite gebyr.


### Fakturaer med ruteanvisninger


Dette er en svært nyttig funksjon hvis du ønsker å administrere flere inngående kanaler med likviditet. I praksis kan du angi hvilken inngående kanal du ønsker å motta Sats fra en Invoice til.


Denne funksjonen kan også brukes til sirkulær rebalansering, når du ønsker å flytte likviditet fra en fylt kanal til en annen tømt kanal.


Hvordan oppretter jeg en Invoice med ruteanvisninger?



- På hovedskjermen skyver du LN-skuffen til høyre og klikker på "Mottak"
- I Invoice-oppsettet går du til den nederste delen og aktiverer knappen "Insert route hints", og velger deretter "Custom"-fanen. Det åpnes et skjermbilde med alle tilgjengelige kanaler. Velg den du ønsker å motta.
- Fyll ut alle andre Invoice-detaljer, beløp, memo osv. og klikk på "opprett Invoice".
- Hvis du betaler Invoice, kommer Sats inn i den angitte kanalen.


Hvis du vil betale til deg selv den Invoice (sirkulær rebalansering), når du betaler den fra den samme Zeus-noden, velger du i betalingsskjermbildet den utgående kanalen (en med mer likviditet) du vil bruke til å sende betalingen.


### Betal med Keysend


Keysend er en svært undervurdert LN-funksjon, og brukerne bør bruke den oftere.


[Keysend] (https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend) gjør det mulig for brukere i Lightning Network å sende betalinger til andre, direkte til deres offentlige nøkkel, så lenge noden deres har offentlige kanaler og har keysend aktivert. Keysend krever ikke at betalingsmottakeren utsteder en Invoice.


Så hvordan kan du gjøre det med Zeus?


Skann eller kopier destinasjonsnodeID-en (eller bruk Zeus-kontakter til å lagre de vanlige destinasjonsnodene som kontakter), og klikk deretter på "Send"-knappen i Zeus' hovedskjermbilde. Lim deretter inn nodeID-en i skjermbildet eller velg fra kontaktene dine.


Skriv inn beløpet på Sats, en melding hvis det er nødvendig (ja, du kan også bruke den som en hemmelig chat over LN) og klikk på "Send" -knappen. Nå er du ferdig!


![Image](assets/en/15.webp)


Hvis du har en direkte kanal med motparten, er det INGEN avgifter involvert.


Hvis du ikke har en direkte kanal med destinasjonskollegaen, vil keysend-betalingen betale avgiftene som en vanlig LN Invoice-betaling, rutet på en regulert bane som enhver annen betaling. Husk bare at det ikke vil forbli noe spor som en LN Invoice.


## Konlusjon


Jeg anbefaler at du leser oppfølgingsveiledningen [Avansert bruk av Zeus] (https://darth-coin.github.io/wallets/zeus-node-advanced-usage-en.html) med flere instruksjoner og brukstilfeller.


Og... det var det! Fra nå av bruker du bare Zeus Node som en vanlig BTC/LN Wallet på mobilen din. Brukergrensesnittet er ganske rett frem og enkelt å bruke, intuitivt for alle typer brukere, jeg tror ikke jeg trenger å gå inn på flere detaljer om hvordan du foretar og mottar betalinger.


Til slutt, her er en sammenligning av personvern :


![Image](assets/en/16.webp)