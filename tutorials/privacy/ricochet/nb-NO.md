---
name: Ricochet
description: Forstå og bruke Ricochet-transaksjoner
---
![cover ricochet](assets/cover.webp)

***ADVARSEL:** Etter arrestasjonen av grunnleggerne av Samourai Wallet og beslagleggelsen av deres servere den 24. april, er Ricochet-verktøyet ikke lenger tilgjengelig. Det er imidlertid mulig at dette verktøyet kan bli gjeninnført i de kommende ukene. I mellomtiden kan du kun utføre en Ricochet manuelt. Den teoretiske delen av denne artikkelen forblir relevant for å forstå hvordan det fungerer og lære hvordan man gjør det manuelt.*

_Vi følger nøye med på utviklingen av denne saken samt utviklingen angående de tilknyttede verktøyene. Vær trygg på at vi vil oppdatere denne opplæringen etter hvert som ny informasjon blir tilgjengelig._

_Denne opplæringen er gitt kun for utdannings- og informasjonsformål. Vi støtter eller oppmuntrer ikke bruk av disse verktøyene til kriminelle formål. Det er hver brukers ansvar å overholde lovene i sin jurisdiksjon._

---

> *"Et premium verktøy som legger til ekstra hopp av historikk til transaksjonen din. Stump svartelistene og hjelp til med å beskytte mot urettferdige tredjeparts kontoavslutninger."*

## Hva er Ricochet?
Ricochet er en teknikk som innebærer å utføre flere fiktive transaksjoner til seg selv for å simulere en overføring av bitcoin-eierskap. Dette verktøyet er forskjellig fra andre Samourai-transaksjoner da det ikke gir potensiell anonymitet, men heller en form for retrospektiv anonymitet. Ricochet bidrar til å sløre spesifisitetene som kan kompromittere fungibiliteten til en Bitcoin-mynt.

For eksempel, hvis du utfører en coinjoin, vil myntutgangen din fra miksen bli identifisert som sådan. Kjedeanalyseverktøy er i stand til å oppdage mønstre av coinjoin-transaksjoner og merke myntene som kommer ut av dem. Faktisk har coinjoin som mål å bryte de historiske koblingene til en mynt, men dens passasje gjennom coinjoins forblir detekterbar. For å lage en analogi, er dette fenomenet likt som å kryptere en tekst: selv om vi ikke kan få tilgang til den opprinnelige klarteksten, er det lett å identifisere at kryptering har blitt anvendt.

Nettopp, denne merkelappen av "coinjoin output coin" kan påvirke fungibiliteten til en UTXO. Regulerte enheter, som utvekslingsplattformer, kan nekte å akseptere en UTXO som har gjennomgått en coinjoin, eller til og med kreve forklaringer fra eieren, med risikoen for å få kontoen blokkert eller midler frosset. I noen tilfeller kan plattformen til og med rapportere din oppførsel til statlige myndigheter.

Dette er hvor Ricochet-metoden kommer inn i bildet. For å sløre fotavtrykket etterlatt av en coinjoin, utfører Ricochet fire påfølgende transaksjoner der brukeren overfører sine midler til seg selv på forskjellige adresser. Etter denne sekvensen av transaksjoner, ruter Ricochet-verktøyet til slutt bitcoinene til deres endelige destinasjon, som en utvekslingsplattform. Målet er å skape avstand mellom den opprinnelige coinjoin-transaksjonen og den endelige bruksakten. På denne måten vil kjedeanalyseverktøy tro at det sannsynligvis har vært en overføring av eierskap etter coinjoin, og derfor er det unødvendig å iverksette tiltak mot avsenderen.
![ricochet diagram](assets/en/1.webp)
I møte med Ricochet-metoden, kan man forestille seg at programvare for kjedeanalyse ville utdype sin undersøkelse utover fire sprett. Disse plattformene står imidlertid overfor et dilemma når det gjelder å optimalisere deteksjonsterskelen. De må etablere en grense for antall hopp etter hvilket de innrømmer at en eiendomsendring sannsynligvis har funnet sted, og at koblingen med en tidligere coinjoin bør ignoreres. Det å bestemme denne terskelen er imidlertid risikabelt: hver utvidelse av det observert antallet hopp øker eksponentielt volumet av falske positiver, dvs. individer feilaktig merket som deltakere i en coinjoin, når operasjonen faktisk ble utført av noen andre. Dette scenariet utgjør en stor risiko for disse selskapene, da falske positiver fører til misnøye, noe som kan drive berørte kunder mot konkurransen. På lang sikt fører en terskel som er for ambisiøs til at en plattform mister flere kunder enn sine konkurrenter, noe som kan true dens levedyktighet. Det er derfor komplisert for disse plattformene å øke antallet observert sprett, og 4 er ofte et tilstrekkelig antall for å motvirke deres analyser.
Dermed **oppstår det mest vanlige bruksområdet for Ricochet når det er nødvendig å skjule en tidligere deltakelse i en coinjoin på en UTXO som tilhører deg**. Ideelt sett er det best å unngå å overføre bitcoins som har gjennomgått en coinjoin til regulerte enheter. Imidlertid, i tilfelle det ikke finnes noen annen mulighet, spesielt i hastverket med å likvidere bitcoins til fiatvaluta, tilbyr Ricochet en effektiv løsning.

## Hvordan fungerer Ricochet på Samourai Wallet?
Ricochet er rett og slett en metode hvor man sender bitcoins til seg selv. Det er derfor fullt mulig å manuelt simulere en Ricochet uten å bruke et spesialisert verktøy. Men, for de som ønsker å automatisere prosessen samtidig som de drar nytte av et mer polert resultat, er Ricochet-verktøyet tilgjengelig gjennom Samourai Wallet-applikasjonen en god løsning.

Siden tjenesten er betalt på Samourai, medfører en Ricochet en kostnad på `100,000 sats` som en tjenesteavgift, i tillegg til gruveavgifter. Dermed er bruken mer anbefalt for overføringer av betydelige beløp.

Samourai-applikasjonen tilbyr to varianter av Ricochet:
- Den forsterkede Ricochet, eller "forsinket levering", tilbyr fordelen av å spre Samourai-tjenesteavgiftene over fem påfølgende transaksjoner. Dette alternativet sikrer også at hver transaksjon kringkastes på et distinkt tidspunkt og registreres i en annen blokk, noe som nøye etterligner oppførselen til en eierskapsendring. Selv om det er tregere, er denne metoden å foretrekke for de som ikke har det travelt, da den maksimerer effektiviteten av Ricochet ved å forbedre dens motstand mot kjedeanalyse.
- Den klassiske Ricochet, som er designet for å utføre operasjonen raskt ved å kringkaste alle transaksjoner innenfor et redusert tidsintervall. Denne metoden tilbyr derfor mindre personvern og lavere motstand mot analyse sammenlignet med den forsterkede metoden. Den bør kun foretrekkes for hastende overføringer.

## Hvordan utføre en Ricochet på Samourai Wallet?
For å utføre en Ricochet-transaksjon fra Samourai Wallet-applikasjonen, følg vår videoveiledning:
![Ricochet YouTube video tutorial](https://youtu.be/Gsz0zuVo3N4)

Hvis du ønsker å studere Ricochet-transaksjonene utført i denne veiledningen, her er de:
- Den første Ricochet-transaksjonen: [8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc](https://mempool.space/fr/testnet/tx/8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc)
- Den siste Ricochet-transaksjonen: [27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777](https://mempool.space/fr/testnet/tx/27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777)
**Eksterne Ressurser:**
- https://docs.samourai.io/en/wallet/features/ricochet