---
name: ArkadeOS
description: Komplett guide til Arkade-porteføljen og Ark-protokollen
---

![cover](assets/cover.webp)



Bitcoin-nettverket står overfor en stor utfordring: skalerbarhet. Selv om hovedlaget (lag 1) tilbyr uovertruffen sikkerhet og desentralisering, kan det bare håndtere et begrenset antall transaksjoner per sekund. Lightning Network har vokst frem som en lovende løsning for det andre laget (lag 2), som muliggjør raske og rimelige betalinger. Lightning har imidlertid sine egne begrensninger: kanaladministrasjon, behovet for innkommende likviditet og en teknisk kompleksitet som kan avskrekke nye brukere.



Dette er bakgrunnen for **Ark**, en ny lag 2-protokoll som er utviklet for å tilby en forenklet brukeropplevelse uten å gi avkall på suverenitet. **ArkadeOS** (eller Arkade) er den første store implementeringen av denne protokollen, og tilbyr en neste generasjons Bitcoin-portefølje.



Denne veiledningen vil guide deg gjennom Arkade-verdenen. Vi utforsker hvordan Ark-protokollen fungerer, hvordan du installerer og konfigurerer Arkade wallet, og hvordan du kan bruke den til å sende og motta bitcoins umiddelbart, konfidensielt og uten de vanlige Lightning Network-friksjonene.



## Forståelse av Ark-protokollen



Før vi går nærmere inn på bruken av Arkade, er det viktig å forstå nøkkelbegrepene i Ark-protokollen som driver den. Ark er ikke en separat blokkjede, men en intelligent koordineringsmekanisme på toppen av Bitcoin.



### VTXO-konseptet


Kjernen i Ark er **VTXO** (Virtual UTXO). En VTXO er en UTXO som ennå ikke er publisert på Bitcoin-blokkjeden: Den eksisterer utenfor hovedkjeden (off-chain), men støttes av transaksjoner som er forhåndssignert på blokkjeden.



I motsetning til en saldo på en sentralisert børs, tilhører en VTXO virkelig deg. Du har et kryptografisk bevis som gjør at du når som helst kan gjøre krav på de tilsvarende ekte bitcoinsene i blokkjeden, selv om Ark-serveren forsvinner. VTXO-er gjør at du kan overføre verdier umiddelbart mellom brukere uten å vente på blokkbekreftelser.



### Rollen til ASP (Ark Service Provider)


Ark-protokollen fungerer etter en klient-server-modell. Serveren kalles **ASP** (Ark Service Provider). ASP spiller rollen som dirigent:




- Det gir den nødvendige likviditeten til nettverket.
- Den koordinerer transaksjoner mellom brukere.
- Den organiserer "oppgjørsrunder" på blokkjeden.



Det er viktig å merke seg at ASP er **ikke-frihetsberøvende**. De har aldri dine private nøkler, og de kan heller ikke stjele pengene dine. Dens rolle er rent teknisk og logistisk. Hvis en ASP sensurerer transaksjonene dine eller går ned, kan du alltid få tilbake pengene dine via en unilateral exit-prosedyre.



### Runder og privatliv


Transaksjoner på Ark fullføres i grupper kalt **Rounds**. Med jevne mellomrom (f.eks. med noen sekunders mellomrom) samler ASP alle ventende transaksjoner og forankrer dem i Bitcoin-blokkjeden i én enkelt optimalisert transaksjon.


Denne mekanismen har to store fordeler:




- Skalerbarhet**: En enkelt on-chain-transaksjon kan validere tusenvis av off-chain-betalinger, noe som reduserer kostnadene for brukerne drastisk.
- Konfidensialitet**: Hver runde fungerer som en **CoinJoin**. Pengene fra alle deltakerne blandes i en felles pott før de omfordeles i form av nye VTXO-er. Dette bryter forbindelsen mellom avsender og mottaker, noe som gjør det ekstremt vanskelig, om ikke umulig, for en utenforstående observatør å spore betalinger.



## Presentasjon av ArkadeOS



ArkadeOS er den konkrete applikasjonen som gjør Ark-protokollen tilgjengelig for allmennheten. Den er utviklet av Ark Labs, og er et komplett økosystem som består av en portefølje (Wallet), en server (Operator) og utviklerverktøy.



For sluttbrukeren tar Arkade form av en elegant, intuitiv web-wallet (PWA - Progressive Web App). Den skjuler den kryptografiske kompleksiteten til VTXO-er og runder bak et velkjent grensesnitt. Med Arkade har du en adresse å motta, en knapp å sende og en transaksjonshistorikk, akkurat som med en klassisk wallet, men med kraften i Arks umiddelbarhet og konfidensialitet.



## Installasjon og konfigurasjon



Ettersom Arkade er en Progressive Web App, er den spesielt enkel å installere, og involverer ikke nødvendigvis tradisjonelle applikasjonslagre.



### Tilgang og installasjon


Du kan få tilgang til Arkade direkte fra alle moderne nettlesere (Chrome, Safari, Brave) på datamaskin eller mobil.





- Besøk programmets offisielle nettside: **[arkade.money](https://arkade.money)**.



![arkade homepage](assets/fr/01.webp)



Du vil bli møtt av en rekke introduksjonsskjermbilder som introduserer deg til Arkades nøkkelkonsepter: et nytt økosystem for Bitcoin, viktigheten av selvforvaring og fordelene med batch-transaksjoner.



![arkade onboarding](assets/fr/02.webp)





- På Android (Chrome/Brave)** : Trykk på nettlesermenyen (tre prikker) og velg "Installer program" eller "Legg til på startskjermen".
- På iOS (Safari)**: Trykk på delingsknappen (firkantet med en pil oppover) og velg "På startskjermen".



Når Arkade er installert, starter den som et vanlig program, i fullskjerm og uten adresselinje.



### Opprettelse av portefølje


Ved første oppstart blir du bedt om å konfigurere porteføljen din.





- Klikk på **"Opprett ny Wallet"**.



![create wallet](assets/fr/03.webp)





- wallet opprettes umiddelbart. I motsetning til tradisjonelle Bitcoin-lommebøker bruker **Arkade ikke en 12- eller 24-ords gjenopprettingsfrase**. I stedet genererer Arkade automatisk en **privat nøkkel** i Nostr (nsec)-format, som vil bli brukt til å sikkerhetskopiere og gjenopprette din wallet. Husk å lagre denne nøkkelen umiddelbart (se neste avsnitt).





- Du vil se skjermbildet "Din nye wallet er live!", som bekrefter at din wallet er klar til bruk. Klikk på **"GO TO WALLET"** for å få tilgang til hovedgrensesnittet.



Når du er inne i wallet, kommer du til Arkades hovedgrensesnitt. Her finner du saldoen din, knapper for å sende og motta penger, og en "Apper"-fane som gir tilgang til integrerte applikasjoner som Boltz (lynbørs), LendaSat og LendaSwap (utlånstjenester) og Fuji Money (syntetiske eiendeler).



![wallet interface](assets/fr/04.webp)



### Tilkobling til ASP


Som standard er porteføljen automatisk konfigurert til å koble seg til den offisielle Arkade Labs ASP. Du kan sjekke hvilken server du er koblet til ved å gå til **Innstillinger** > **Om**, der du vil se serveradressen (for øyeblikket `https://arkade.computer`).



I den nåværende versjonen av Arkade (Beta) er det ikke mulig å endre ASP-serveren manuelt. Programmet kobler seg automatisk til Arkade Labs' offisielle ASP. I fremtiden vil brukerne kanskje kunne velge mellom ulike ASP-er i henhold til egne preferanser, men denne funksjonen er ikke tilgjengelig ennå.



### Sikkerhetskopiering av din private nøkkel


**Arkade bruker en privat nøkkel i Nostr (nsec)-format som en metode for sikkerhetskopiering og gjenoppretting. For å sikkerhetskopiere din private nøkkel :





- Gå til **Innstillinger** fra hovedskjermen.
- Velg **"Sikkerhetskopiering og personvern"**.
- Du vil se din **private nøkkel** vist i `nsec...`-format. Denne lange tegnstrengen er den eneste måten du kan gjenopprette wallet på.
- Trykk på **"COPY NSEC TO CLIPBOARD"** for å kopiere den private nøkkelen.
- Oppbevar denne nøkkelen på et trygt sted**: skriv den ned på papir, lagre den i en sikker passordbehandler, eller bruk en annen sikkerhetskopimetode som passer deg.
- Arkade tilbyr også alternativet **"Aktiver Nostr-sikkerhetskopier"**. Denne funksjonen bruker Nostr-protokollen (et desentralisert nettverk) til automatisk å sikkerhetskopiere visse data fra wallet i kryptert form til Nostr-reléer. Dette forenkler synkronisering mellom flere enheter og gjør det enklere å gjenopprette wallet-status.



**Viktig**: Nostr-sikkerhetskopier er kun en **komfort**-funksjon. De erstatter ikke sikkerhetskopien av nsec-nøkkelen din. Nostr-reléer garanterer ikke permanent datalagring. Din private nsec-nøkkel er fortsatt din eneste garanterte måte å få tilbake pengene dine på.



![backup private key](assets/fr/05.webp)




## Bruk av Arkade



Når du har satt opp wallet, er du klar til å utforske Arkades muligheter. Grensesnittet er utformet for å forene de ulike typene Bitcoin-betalinger (On-chain, Lightning, Ark) på en sømløs måte.



### Mottak av midler



For å finansiere porteføljen din trykker du på **"Motta"**. Arkade tilbyr tre metoder for mottak:





- Ark-betaling**: Hvis avsenderen også bruker Arkade, kan du dele Ark-adressen din for en øyeblikkelig, konfidensiell og praktisk talt gratis overføring.
- Innskudd i kjeden (ombordstigning)**: Bruk Bitcoin-adressen (`bc1p...`) for å motta fra en klassisk wallet eller en børs. Vent på bekreftelse (~10 min) før midlene konverteres til VTXO-er.
- Lightning-bytte**: Generer en Lightning-faktura og betal den fra en ekstern wallet Lightning. Pengene kommer umiddelbart via en automatisk swap.



![receive amount](assets/fr/06.webp)



Kvitteringsskjermen viser alle tilgjengelige alternativer: QR-kode, Ark-adresse, Bitcoin-adresse (BIP21) og Lightning-faktura. For Lightning-betalinger må du holde applikasjonen åpen under transaksjonen.



![receive confirmation](assets/fr/07.webp)



### Sende midler



For å sende penger trykker du på **"Send"** og limer inn mottakerens adresse eller skanner QR-koden. Arkade registrerer automatisk hvilken type betaling som kreves:





- Ark** betaling: Til en Ark-adresse er overføringen øyeblikkelig, privat og praktisk talt gratis (0 SATS gebyr). Mottakeren trenger ikke å være online.
- Lightning**-betaling: Skann en Lightning-faktura (`lnbc...`), og Arkade utfører automatisk en swap. ASP-en betaler fakturaen for deg og belaster Arkade-saldoen din.
- Betaling i kjeden**: Mot en klassisk Bitcoin-adresse (`bc1q...` eller `bc1p...`) initierer Arkade en "Collaborative Output" som vil bli inkludert i neste on-chain-runde.



Kontroller detaljene på skjermbildet "Signer transaksjon", og bekreft deretter med **"TAPP FOR Å SIGNERE"**.



![send payment](assets/fr/08.webp)



**Nåværende begrensning (Beta)**: VTXOer som er opprettet for mindre enn 24 timer siden, kan ikke brukes for on-chain-utganger. Hvis du støter på en feil, må du vente til VTXOene dine er "modne".



**on-chain-utdatakonfidensialitet**: Eksemplet nedenfor viser en [Ark-utgangstransaksjon på mempool.space](https://mempool.space/fr/tx/153a70384d1c8a183c0e408e29b0a11820fd71a8bd5b4b00b12bc9b7f9decacb). Vi observerer en distribuert inngang til 4 forskjellige utganger, som en CoinJoin. For en ekstern observatør er det umulig å avgjøre hvilket beløp som tilhører hvilken bruker.



![transaction ark mempool](assets/fr/11.webp)



## Avanserte funksjoner



### VTXO utløpshåndtering


En teknisk egenskap ved Ark-protokollen er at VTXO-er har en **begrenset levetid**. Denne tidsbegrensningen ligger i protokollens design. Utløpstiden kan konfigureres av hver ASP-server; på den offisielle ASP-en til Arkade Labs er denne perioden rundt **4 uker (≈30 dager)**.



**Denne begrensningen gjør det mulig for Arks server å administrere likviditeten effektivt og rydde opp i VTXO-er fra inaktive brukere. Etter utløpet kan Ark-serveren teknisk sett gjøre krav på de gjenværende midlene i VTXO-treet.



**For å holde VTXO-ene dine aktive, må de "oppdateres" før de utløper. Oppdateringen består i å delta i en ny "runde" der VTXO-er som nærmer seg utløp, byttes ut mot nye VTXO-er med en ny full gyldighetsperiode (≈30 dager på Arkade Labs ASP).



Arkade-porteføljen håndterer denne prosessen automatisk: applikasjonen overvåker kontinuerlig statusen til VTXO-ene dine og oppdaterer dem automatisk noen dager før de utløper. Så lenge du åpner applikasjonen regelmessig (minst én gang i uken), vil VTXO-ene dine automatisk holdes aktive.



**Hvis du ikke åpner porteføljen din på mer enn 4 uker, utløper VTXO-ene dine. Du mister imidlertid ikke midlene dine: Du har fortsatt muligheten til å få dem tilbake via en **unilateral exit** (se neste avsnitt). Denne prosedyren er mer kostbar og langsommere, men den sikrer at midlene dine fortsatt kan gjenvinnes.



Behovet for å åpne applikasjonen regelmessig gjør Arkade til en **"Hot Wallet"** designet for daglige utgifter, ikke en safe for langsiktig sparing. For å lagre bitcoins uten å bruke dem i lange perioder, foretrekker du en kald wallet-maskinvare.



**Sjekk statusen til VTXO-ene dine**: Du kan overvåke statusen til VTXO-ene dine i **Innstillinger** > **Avansert**. Se "Neste fornyelse" for å se når neste automatiske fornyelse vil finne sted, og "Virtuelle mynter" for å se en detaljert liste over alle VTXO-ene dine med utløpsdato.



![vtxo management](assets/fr/09.webp)



### Sortie Unilatérale (ensidig utreise)



Unilateral exit er en **fundamental kryptografisk garanti** i Ark-protokollen som sikrer at du får pengene dine tilbake, selv om ASP-en forsvinner, sensurerer transaksjonene dine eller nekter å samarbeide. Teknisk sett er VTXO-ene dine **forhåndssignerte Bitcoin-transaksjoner** som du eier. I en absolutt nødsituasjon kan du kringkaste disse transaksjonene på Bitcoin-blokkjeden for å få tilbake pengene dine uten noens autorisasjon.



**Hvordan fungerer det? Prosessen foregår i to trinn. Først **Unrolling**: Du sender ut de forhåndssignerte transaksjonene som utgjør VTXO-ene dine i transaksjonstreet i rekkefølge. Deretter **Finalization**: Når tidslåsene har utløpt (vanligvis 24 timer), henter du bitcoinsene dine fra en standardadresse.



**Nåværende status i Arkade**: I betaversjonen finnes det ennå ikke en knapp eller et enkelt brukergrensesnitt for ensidig utdata. Denne funksjonaliteten krever for øyeblikket bruk av Arkade SDK og teknisk kunnskap om TypeScript-programmering.



**Selv om prosedyren ikke er tilgjengelig ved å trykke på en knapp, er den kryptografiske garantien der. VTXOene dine inneholder forhåndssignerte transaksjoner som legitimt tilhører deg. Det er denne tekniske garantien som gjør Ark til en **ikke-forvaringsverdig** protokoll: Selv i verste fall kan pengene dine teknisk sett gjenvinnes. Et forenklet grensesnitt vil sannsynligvis bli lagt til i fremtidige versjoner av Arkade.



## Fordeler og begrensninger



La oss oppsummere Arkades nåværende styrker og svakheter for å sette Arkade inn i den rette konteksten.



### Høydepunkter




- Brukeropplevelse (UX)**: Ingen kanaladministrasjon, innkommende kapasitet eller komplekse kanalbackuper som med Lightning. Bare installer og bruk.
- Personvern** : Standard CoinJoin-arkitekturen tilbyr et mye høyere nivå av anonymitet enn standard on-chain- eller Lightning-transaksjoner.
- Interoperabilitet**: Betal med alle Bitcoin QR-koder (On-chain eller Lightning) fra ett enkelt grensesnitt.



### Begrensninger




- Ung protokoll**: Ark er en svært ny teknologi. Det kan forekomme feil. Det anbefales ikke å bruke Ark til å lagre beløp som det er kritisk å miste.
- Avhengighet av ASP**: Selv om systemet ikke er avhengig av ASP, er det avhengig av at ASP er tilgjengelig for å sikre flyt. Hvis ASP-en er frakoblet, kan du ikke lenger utføre transaksjoner umiddelbart (bare sende ut on-chain-midlene dine).
- Kun Hot Wallet** : Behovet for å åpne programmet regelmessig for å oppdatere VTXO-er er ikke egnet for kald lagring (Cold Lagring).



## Sammenligning: Arkade vs Lightning vs Cashu



For å forstå Arkades posisjonering bedre, kan vi sammenligne den med de to andre store skalerbarhetsløsningene.



| Critère | Arkade (Ark) | Lightning Network | Cashu (E-cash) |
| :--- | :--- | :--- | :--- |
| **Modèle** | UTXO partagé coordonné par serveur (ASP) | Réseau P2P de canaux de paiement | Jetons aveugles émis par une banque (Mint) |
| **Custodie** | **Non-custodial** (vous avez les clés) | **Non-custodial** (vous avez les clés) | **Custodial** (le Mint a les fonds) |
| **Confidentialité** | **Élevée** (CoinJoin natif, aveugle pour le public) | **Moyenne** (Routage en oignon, mais canaux visibles) | **Très Élevée** (Aveugle même pour le Mint) |
| **Scalabilité** | Excellente (Batching massif on-chain) | Excellente (Transactions infinies off-chain) | Excellente (Simples signatures serveur) |
| **Expérience** | Simple (proche d'un wallet on-chain) | Complexe (gestion de canaux, liquidité) | Très simple (comme du cash numérique) |
| **Risque principal** | Disponibilité de l'ASP & Expiration | Gestion des canaux & Backups | Confiance dans le Mint (risque de vol) |

**Arkade** er det ideelle kompromisset: enkelheten og konfidensialiteten til Cashu, men med suvereniteten (ikke-frihetsberøvende) til Lightning.



## Støtte og assistanse



Hvis du støter på problemer eller har spørsmål mens du bruker Arkade, tilbyr programmet flere supportalternativer:





- Gå til **Innstillinger** > **Support**.
- Du finner flere alternativer:
  - Kundestøtte**: Få hjelp med porteføljen din, rapporter feil eller still spørsmål.
  - Sikker chat**: Samtalene dine er sikre og private, og historikken opprettholdes mellom øktene.
  - Feilrapporter**: Rapporter eventuelle problemer du støter på, inkludert fremgangsmåte for å reprodusere dem.
  - Spor fremdriften**: Hold oversikt over supporthenvendelser og samtaler til enhver tid.



![support](assets/fr/10.webp)



Arkade-teamet er også aktive på Telegram via kanalen @arkade_os for support og integrasjonsmuligheter.



## Viktig merknad: Applikasjonen er i beta



**⚠️ Arkade er for tiden i offentlig betaversjon på mainnet Bitcoin**. Selv om applikasjonen er funksjonell med ekte bitcoins, er det viktig å ta visse forholdsregler.



### Anbefalinger for bruk




- Bruk små beløp**: Unngå å lagre store summer på Arkade. Bruk denne wallet til daglige utgifter, og oppbevar sparepengene dine på en kald wallet-maskinvare.
- Mulige feil og begrensninger**: Som med alle applikasjoner under aktiv utvikling, kan Arkade inneholde feil eller uventet oppførsel. Rapporter eventuelle problemer via integrert support.
- Rask utvikling** : Programmet og protokollen forbedres kontinuerlig. Noen funksjoner kan bli endret eller lagt til i fremtidige versjoner.



### Nåværende kjente begrensninger




- 24-timers forsinkelse på VTXOer** : Nyopprettede VTXO-er kan ikke brukes umiddelbart for on-chain-utganger.
- ASP unik**: Det er ennå ikke mulig å endre ASP-serveren i applikasjonen.
- Teknisk unilateral utdata**: Det finnes ikke noe forenklet grensesnitt for unilateral utdata ennå (krever SDK).



Arkade Labs jobber aktivt med å lempe på disse begrensningene i fremtidige versjoner.



## Konklusjon



ArkadeOS representerer et stort gjennombrudd i Bitcoin-økosystemet. Ved å implementere Ark-protokollen beviser den at det er mulig å forene enkel bruk med de grunnleggende prinsippene i Bitcoin: ikke stol på, verifiser.



Selv om Arkade fortsatt er i sin spede begynnelse, gir den et fascinerende glimt av hvordan fremtidens Bitcoin-betalinger kan se ut: umiddelbar, privat og tilgjengelig for alle uten tekniske forutsetninger. Det er det perfekte verktøyet for dine daglige utgifter, som et supplement til din sikre spareløsning (Cold Wallet).



Vi oppfordrer deg til å teste Arkade med små beløp for å oppdage denne nye protokollen selv. Økosystemet utvikler seg raskt, og Arkade ligger i forkant av denne innovasjonen.



## Ressurser



For å finne ut mer, se de offisielle ressursene:





- Arkade** nettsted: [arkadeos.com](https://arkadeos.com)
- Dokumentasjon**: [docs.arkadeos.com](https://docs.arkadeos.com)
- Ark**-protokollen: [ark-protocol.org](https://ark-protocol.org)
- Kildekode** : [GitHub Arkade](https://github.com/arkade-os)