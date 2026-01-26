---
name: KaleidoSwap
description: Avansert guide til handel med RGB-aktiva på Lightning Network med KaleidoSwap
---

![cover](assets/cover.webp)


KaleidoSwap er et sofistikert skrivebordsprogram med åpen kildekode som bygger bro mellom RGB-protokollen og Lightning Network. Den fungerer som et omfattende grensesnitt for å administrere RGB Lightning Nodes, samhandle med RGB Lightning Service Providers (LSP-er) via LSPS1-spesifikasjonen og utføre atombytter av RGB-aktiva.


KaleidoSwap er en løsning som ikke innebærer frihetsberøvelse, og som gir brukerne full kontroll over egne nøkler og data. Ved å utnytte valideringsparadigmet på klientsiden i RGB, muliggjør det private og skalerbare smartkontrakter på toppen av Bitcoin. Denne opplæringen dykker ned i de avanserte funksjonene i KaleidoSwap, og veileder deg gjennom komplikasjonene ved "farget" UTXO-administrasjon, kanallikviditet for spesifikke aktiva og taker-maker-handelsmodellen, slik at du kan utnytte denne kraftige desentraliserte utvekslingsprotokollen fullt ut.


## Installasjon


KaleidoSwap tilbyr forhåndsbygde binære filer for de fleste operativsystemer, men for avanserte brukere kan du bygge fra kildekode for å sikre at du kjører den nyeste koden med dine spesifikke konfigurasjoner.


### Last ned Binaries


Du kan laste ned den nyeste versjonen for operativsystemet ditt fra [offisiell nettside](https://kaleidoswap.com/) eller [GitHub-utgivelsessiden](https://github.com/kaleidoswap/desktop-app/releases).


### Installasjonsmetoder


1.  **Windows**: Last ned installasjonsprogrammet `.exe` og kjør det.

2.  **macOS**: Last ned `.dmg`-filen, åpne den og dra KaleidoSwap til Programmer-mappen din.

3.  **Linux**: Last ned `.AppImage`- eller `.deb`-filen og installer/kjør den.



## Alternativer for nodeoppsett


Når du starter KaleidoSwap for første gang, får du opp **Connection Screen**. Dette er det første trinnet i konfigurasjonen av miljøet ditt.


![Node Selection Screen](assets/en/01.webp)


Du må velge hvordan du vil koble deg til RGB Lightning Network. Dette valget påvirker kontrollnivået og personvernet ditt.


### Alternativ 1: Lokal node (anbefalt for selvoppbevaring)


**For full kontroll og personvern** kan du kjøre en node direkte på maskinen din, se fordelene nedenfor:


- Selvforvaltet**: Du sitter med nøklene. Ingen tredjepart kan fryse pengene dine eller sensurere transaksjonene dine.
- Personvern**: Dataene dine forblir på enheten din.
- Uavhengighet**: Ingen avhengighet av eksterne tjenesteleverandører.


Hvis du velger **Local Node**, kommer du til oppsettskjermbildet der du kan opprette en ny wallet eller gjenopprette en eksisterende.


![Local Node Setup Screen](assets/en/02.webp)


### Alternativ 2: Ekstern node


Koble til en ekstern RGB Lightning Node (selv-hostet på en VPS eller hos en hostet leverandør).


- Fordeler**: Ingen lokal ressursbruk, tilgjengelighet 24/7.
- Kompromiss**: Krever tillit til verten eller administrasjon av en ekstern server.


![Remote Node Setup Screen](assets/en/03.webp)


**Vi anbefaler på det sterkeste at du kjører din egen node - enten lokalt (alternativ 1) eller ved å være vert for en ekstern node - for å dra full nytte av de sensurresistente egenskapene til Bitcoin og RGB.


## Opprette en Wallet


KaleidoSwap administrerer både Bitcoin- og RGB-aktiva. wallet-opprettelsesprosessen initialiserer et keystore som sikrer on-chain-midlene dine og Lightning-kanalstatusene dine.


Her er den detaljerte prosessen:

1. Åpne KaleidoSwap og velg **Local Node**.

2. Klikk på **Opprett ny Wallet**.

3. **Kontooppsett**: Skriv inn et **Kontonavn** og velg **Nettverk** (f.eks. Bitcoin, Mainnet, Testnet, Signet).

4. **Avansert konfigurasjon** (valgfritt): Hvis du er en avansert bruker, kan du konfigurere egendefinerte RPC-sluttpunkter, indekserings-URL-er eller proxy-innstillinger under "Avanserte innstillinger".

5. Klikk på **Fortsett**.

6. **Passord**: Angi et sterkt passord for å kryptere wallet-filen lokalt.

7. **Gjenopprettingsfrase**: Skriv ned seed-frasen din, og oppbevar den på et sikkert sted.


    - Kritisk**: Denne setningen er nødvendig for å gjenopprette on-chain-midler og nodeidentiteten din.
    - Advarsel**: **Kanalstatusene kan ikke gjenopprettes fullstendig fra seed alene**. Du må også vedlikeholde statiske kanalsikkerhetskopier (SCB) for å gjenopprette midler som er låst i kanaler.


![Wallet Creation Screen](assets/en/04.webp)



## Oversikt over dashbordet


Når wallet er opprettet, vil du bli sendt til hovedvinduet **Dashboard**.


![KaleidoSwap Dashboard](assets/en/05.webp)


merk: Skjermbildet ovenfor viser en wallet som allerede har blitt finansiert og har aktive kanaler. En ny wallet vil vise null saldo og ingen aktive kanaler før du finansierer den


## Finansiering av din Wallet


For å operere med RGB-aktiva må du finansiere wallet. KaleidoSwap støtter innskudd av både Bitcoin- og RGB-eiendeler via on-chain-transaksjoner eller Lightning Network.


### Deponering av Bitcoin


1. Klikk på **Deposit** i menyen Quick Actions.

2. Velg **BTC** fra listen over aktiva.


![Select BTC Asset](assets/en/06.webp)


3. Velg innskuddsmetoden din: **På kjede** eller **Lightning**.


![BTC Deposit Options](assets/en/07.webp)



- På kjeden**: Skann QR-koden eller kopier adressen for å sende Bitcoin fra en annen wallet.
- Lyn**: Generer en faktura på ønsket beløp.


![BTC On-chain Deposit](assets/en/08.webp)


### Sette inn RGB-eiendeler og fargede UTXO-er


For å motta RGB-aktiva (som USDT) trenger du spesifikke UTXO-er som er tilgjengelige for å bli "farget" (tildelt et aktivum).


1. Klikk på **Deposit** og velg aktivumet RGB (f.eks. USDT). **Viktig**: Hvis dette er **første gang** noden din mottar dette spesifikke aktivumet, må du **la aktivum-ID-feltet stå tomt**. Hvis du skriver inn en ID for en ukjent eiendel, vil noden returnere en feilmelding fordi den ikke gjenkjenner den ennå.

2. Velg **På-kjede** eller **Lightning**.


![USDT Deposit Options](assets/en/09.webp)


#### Mottaksmoduser i kjeden: Vitne vs. blindet


Når du mottar RGB-aktiver on-chain, har du to personvernmoduser:



- Blinded Receive (anbefalt for personvern)**: Du gir en "blinded" UTXO til avsenderen. Du ber avsenderen om å sende ressurser til en eksisterende UTXO som du eier, men du skjuler den faktiske UTXO-identifikatoren. Dette gir bedre personvern.
- Vitne mottar**: Du oppgir en standard Bitcoin-adresse. Du ber avsenderen om å opprette en *ny* UTXO for deg ved å sende eiendelene til den adressen. Dette gjør at RGB-aktiva kan knyttes direkte til den nye UTXO som opprettes av transaksjonen.


#### Lyninnskudd


For lyninnskudd trenger du bare generate en faktura. RGB-aktivaen vil bli sendt til deg gjennom dine åpne kanaler.


![USDT Lightning Invoice](assets/en/10.webp)



## Åpne kanaler med RGB Assets


For å dirigere RGB-eiendeler over Lightning Network trenger du en kanal med tilstrekkelig likviditet og allokering av eiendeler. Den enkleste måten å komme i gang på er å **Kjøpe en kanal** fra en LSP (Lightning Service Provider).


### Kjøpe en kanal fra Kaleido LSP


1. Gå til fanen **Kanaler**. Du vil se alternativene "Åpne kanal" (manuell) eller "Kjøp kanal" (LSP).

2. Klikk på **Buy Channel**.


![Channels Dashboard](assets/en/11.webp)


3. **Koble til LSP**: Appen kobler seg til Kaleidos standard LSP. Denne leverandøren tilbyr inngående likviditet og støtter RGB asset routing.


![Connect to LSP](assets/en/12.webp)


4. **Konfigurer kanal**:


    - Kapasitet**: Velg den totale Bitcoin-kapasiteten for kanalen.
    - RGB Allokering**: Velg RGB-aktivaen (f.eks. USDT) du ønsker å kunne motta eller sende. LSP vil sørge for at kanalen er konfigurert til å støtte dette aktivumet.


![Configure Channel](assets/en/13.webp)



    - RGB Allokering**: Velg RGB-aktivaen (f.eks. USDT) du ønsker å kunne motta eller sende. LSP vil sørge for at kanalen er konfigurert til å støtte dette aktivumet.


![RGB Allocation](assets/en/14.webp)


5.  **Betaling**: Du må betale en avgift til LSP-en for å åpne kanalen og stille likviditet til rådighet. Du kan betale ved hjelp av **Lightning** eller **On-chain** Bitcoin. Betalingen kan gjøres fra din interne KaleidoSwap wallet eller en ekstern wallet.


![Complete Payment](assets/en/15.webp)


6. Når betalingen er bekreftet, vil LSP sette i gang transaksjonen for åpning av kanalen. Du vil se en **Bestilling fullført**-skjerm.


![Order Completed](assets/en/16.webp)


7. Etter bekreftelse på blokkjeden vil kanalen din være aktiv og klar for RGB-overføringer.



## Handel: Taker-Maker-modellen


KaleidoSwaps handelsmotor fungerer etter en **Taker-Maker-modell**. Du kan bytte aktiva manuelt med en motpart eller bruke en Market Maker (LSP).


### Bytte med en market maker (LSP)


Dette er den vanligste måten å handle på. Du opptrer som **Taker**, og utfører ordre mot tilgjengelig likviditet fra LSP-en (**Maker**).


1. Gå til **Trade**-fanen og velg **Market Maker**.

2. **Skriv inn beløp**: Skriv inn beløpet i Bitcoin du vil sende (eller eiendelen du vil motta). Grensesnittet vil vise estimert valutakurs og gebyrer.


![Market Maker Swap](assets/en/17.webp)


3. **Bekreft byttet**: Se gjennom detaljene, inkludert valutakursen og det nøyaktige beløpet du vil motta. Klikk på **Bekreft byttet**.


![Confirm Swap](assets/en/18.webp)


4. **Bearbeiding**: Byttet utføres atomisk på Lightning Network. Du vil se et statusskjermbilde som indikerer at byttet venter.


![Swap Pending](assets/en/19.webp)


5. **Suksess**: Når HTLC-ene er gjort opp, er byttet fullført, og eiendelene er i kanalen din.


![Swap Success](assets/en/20.webp)



## Utvikler API


For utviklere som bygger på toppen av KaleidoSwap, eksponerer applikasjonen en API som støtter:



- RGB LSPS1**: For automatiserte likviditetstjenester.
- Swap API**: For programmatisk handel og market making.
- WebSocket**: For abonnement på markedsdata i sanntid.


Se [API Documentation](https://docs.kaleidoswap.com/api/introduction) for fullstendige endepunkter og spesifikasjoner.


## Konklusjon


KaleidoSwap gir deg muligheten til å utnytte personvernet og skalerbarheten til RGB-aktiva på Lightning Network. Ved å forstå fargede UTXO-er og allokering av kanalaktiva, kan du utnytte denne kraftige desentraliserte utvekslingsprotokollen fullt ut.