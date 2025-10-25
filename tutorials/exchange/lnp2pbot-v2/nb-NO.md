---
name: LNP2PBot
description: Komplett guide til LNP2PBot og P2P bitcoin-handel
---
![cover](assets/cover.webp)

## Innledning

KYC-frie peer-to-peer-børser (P2P) er avgjørende for å bevare brukernes konfidensialitet og økonomiske uavhengighet. De muliggjør direkte transaksjoner mellom enkeltpersoner uten behov for identitetsbekreftelse, noe som er avgjørende for de som verdsetter personvern. For en mer inngående forståelse av de teoretiske konseptene, ta en titt på BTC204-kurset:

https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Kjøp og salg av bitcoin peer-to-peer (P2P) er en av de mest private metodene for å anskaffe eller avhende bitcoins. LNP2PBot er en Telegram-bot med åpen kildekode som legger til rette for P2P-børser på Lightning-nettverket, noe som muliggjør raske, rimelige og KYC-frie transaksjoner.

### Hvorfor bruke Lnp2pbot?


- Ingen KYC kreves
- Raske transaksjoner på Lightning Network
- Lave kostnader
- Enkelt grensesnitt via Telegram, et populært meldingsprogram som er tilgjengelig fra hvor som helst i verden
- Integrert omdømmesystem
- Automatisk sperring for sikker handel
- Støtte for flere valutaer
- Aktivt og voksende fellesskap

### Forutsetninger

For å bruke Lnp2pbot trenger du :

1. Lightning Network-lommebok (Breez, Phoenix eller Blixt anbefales)

2. Telegram-applikasjon installert (https://telegram.org/)

3. En Telegram-konto med et definert brukernavn

## Installasjon og konfigurasjon

### 1. Konfigurere Lightning-lommeboken din

Begynn med å installere en kompatibel Lightning-lommebok. Her er våre detaljerte anbefalinger:

**Anbefalte porteføljer**


- [Breez](https://breez.technology):
  - Utmerket for nybegynnere
  - Intuitivt, moderne grensesnitt
  - Ikke-forvaring (du beholder kontrollen over midlene dine)
  - Perfekt kompatibel med Lnp2pbot
  - Tilgjengelig på iOS og Android

Nedenfor finner du lenken til veiledningen for denne lommeboken:

https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06

- [Phoenix](https://phoenix.acinq.co) :
  - Enkelt og pålitelig
  - Automatisk kanalkonfigurasjon
  - Innebygd støtte for BOLT11-fakturaer
  - Utmerket for hverdagslige transaksjoner
  - Tilgjengelig på iOS og Android

Nedenfor finner du lenken til veiledningen for denne lommeboken:

https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

- [Blixt](https://blixtwallet.github.io) :
  - Mer teknisk, men svært komplett
  - Avanserte konfigurasjonsalternativer
  - Perfekt for erfarne brukere
  - Åpen kildekode
  - Tilgjengelig på Android

Nedenfor finner du lenken til veiledningen for denne lommeboken:

https://planb.network/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

**Viktige merknader om andre porteføljer**

⚠️ **Viktig**: Før du selger sats, må du sørge for at porteføljen din støtter "hold"-fakturaer, som brukes av boten som et escrow-system.


- **Wallet of Satoshi**: Fungerer bra for å motta sats, men kan ha forsinkelser i oppdateringen av saldoen hvis et salg blir kansellert.
- **Muun**: Anbefales ikke, da betalinger kan mislykkes på grunn av begrensningene for rutinggebyr (maks. 0,2 %).
- **Aqua**: Fungerer for å motta sats, men kan ha lange forsinkelser (opptil 48 timer) for saldooppdateringer i tilfelle et salg kanselleres.

💡 **Tips**: For en optimal opplevelse bør du velge anbefalte porteføljer (Breez, Phoenix eller Blixt).

⚠️ **Viktig**: Ikke glem å lagre gjenopprettingsfrasene dine på et trygt sted.

### 2. Kom i gang med Lnp2pbot

1. Klikk på denne lenken for å få tilgang til boten: [@lnp2pBot] (https://t.me/lnp2pbot)

2. Telegram åpnes automatisk

3. Klikk på "Start" eller send kommandoen "/start"

4. Boten vil be deg om å opprette et brukernavn hvis du ikke allerede har et

5. Boten vil veilede deg gjennom den første konfigurasjonen

### 3. Bli med i fellesskapet


- Bli med på hovedkanalen: [@p2plightning](https://t.me/p2plightning)
- Support: [@lnp2pbotHelp] (https://t.me/lnp2pbotHelp)

## Kjøp og salg av Bitcoins

Det er to hovedmåter å bytte bitcoins på Lnp2pbot:

1. Bla gjennom og svar på eksisterende tilbud på markedet

2. Lag ditt eget tilbud om kjøp eller salg

I denne guiden tar vi en detaljert titt på hvordan :


- Kjøp bitcoins fra et eksisterende tilbud
- Selg bitcoins ved å opprette ditt eget tilbud

### Hvordan kjøpe Bitcoins

**1. Finn og velg et tilbud**

![Sélection d'une offre de vente](assets/fr/01.webp)

Bla gjennom tilbudene i [@p2plightning](https://t.me/p2plightning) og klikk på "Kjøp satoshis" -knappen under annonsen du er interessert i.

**2. Valider tilbud og beløp**

![Validation de l'offre](assets/fr/02.webp)

1. Gå tilbake til bot-chat

2. Bekreft ditt valg av tilbud

3. Angi beløpet i fiat-valuta du ønsker å kjøpe

4. Boten vil be deg om å oppgi en lynfaktura for beløpet i satoshier

**3. Kontakt selgeren**

![Mise en relation](assets/fr/03.webp)

Når fakturaen er sendt, setter boten deg i kontakt med selgeren.

**4. Kommunikasjon med selger**

![Chat privé](assets/fr/04.webp)

Klikk på selgerens kallenavn for å åpne en privat chattekanal der du kan utveksle fiat-betalingsinformasjon.

**5. Bekreftelse av betaling**

![Confirmation du paiement](assets/fr/05.webp)

Etter at du har foretatt fiat-betalingen, bruker du kommandoen `/fiatsent` i bot-chatten. Når transaksjonen er fullført, kan du rangere selgeren, og transaksjonen avsluttes.

### Hvordan selge Bitcoins

**1. Opprett et salgstilbud**

![Création d'une offre de vente](assets/fr/06.webp)

For å opprette et salgstilbud bruker du ganske enkelt kommandoen :

`/salg`

Boten vil deretter veilede deg trinn for trinn:

1. Velg valuta

2. Angi hvor mange satoshier du skal selge

3. For prisen har du to alternativer:


   - Angi en fast pris for antall satoshier
   - Bruk markedsprisen med mulighet for å legge til en premie (positiv eller negativ)

💡 **Tips**: Med påslaget kan du justere prisen i forhold til markedsprisen. En premie på -1 % betyr for eksempel at du selger for 1 % mindre enn markedsprisen.

**2. Bekreftelse på opprettelse av ordre**

![Confirmation de l'ordre de vente](assets/fr/07.webp)

Når bestillingen er opprettet, får du en bekreftelse med mulighet til å kansellere bestillingen ved hjelp av kommandoen `/cancel`.

**3. Administrer salg**

![Prise de l'ordre par un acheteur](assets/fr/08.webp)


- Når en kjøper svarer på tilbudet ditt, mottar du et varsel med en QR-kode og en faktura du må betale.
- Sjekk kjøperens profil og omdømme.

![Mise en relation avec l'acheteur](assets/fr/09.webp)


- Klikk på kjøperens kallenavn for å åpne en privat diskusjonskanal.
- Formidle fiat-betalingsopplysninger til kjøperen.
- Vent på bekreftelse på fiat-betalingen fra kjøperen.
- Sjekk at betalingen er mottatt på kontoen din.

![Confirmation de la fin de l'ordre](assets/fr/10.webp)


- Bekreft transaksjonen med `/release` og fullfør bestillingen. Du vil få muligheten til å vurdere kjøperen.

## God praksis og sikkerhet

### Sikkerhetstips


- Begynn med små mengder
- Sjekk alltid brukernes omdømme
- Bruk kun de foreslåtte betalingsmåtene
- Hold all kommunikasjon i bot-chat
- Del aldri sensitiv informasjon

### Omdømmesystem


- Hver bruker har en omdømmescore
- Vellykkede transaksjoner øker poengsummen din
- Velg brukere med godt omdømme
- Rapportere mistenkelig oppførsel til moderatorene

### Tvisteløsning

1. Hold deg rolig og profesjonell når det oppstår problemer

2. Bruk kommandoen `/dispute` for å åpne en ticket

3. Fremlegg alle nødvendige bevis

4. Vent på en moderator

## Sammenligning med andre løsninger

Lnp2pbot har flere fordeler og ulemper sammenlignet med andre P2P-børsløsninger som Peach, Bisq, HodlHodl og Robosat:

### Fordeler med Lnp2pbot


- Ingen KYC kreves ** : I motsetning til noen plattformer krever Lnp2pbot ikke identitetsbekreftelse, og bevarer dermed brukernes konfidensialitet.
- **Raske transaksjoner**: Takket være Lightning-nettverket er transaksjonene nesten øyeblikkelige.
- **Lave gebyrer**: Transaksjonskostnadene er lavere enn for tradisjonelle børser.
- **Mobil tilgjengelighet**: LNP2PBot er tilgjengelig via Telegram, noe som gjør det enkelt å bruke på mobile enheter.
- **Enkel å bruke**: Lnp2pbots intuitive grensesnitt gjør det enkelt å bruke, selv for mindre erfarne brukere.

### Ulemper med Lnp2pbot


- **Telegram-avhengighet**: Bruk av Lnp2pbot krever en Telegram-konto, noe som kanskje ikke passer for alle brukere.
- **Mindre likviditet**: Sammenlignet med mer etablerte plattformer som Bisq, kan likviditeten være mer begrenset.

Til sammenligning tilbyr løsninger som Bisq større likviditet og et skrivebordsgrensesnitt, men kan innebære høyere gebyrer og lengre transaksjonstid. HodlHodl og Robosat tilbyr også KYC-fri handel, men med ulike gebyrstrukturer og grensesnitt.

## Nyttige ressurser


- Offisiell nettside: https://lnp2pbot.com/
- Dokumentasjon: https://lnp2pbot.com/learn/
- GitHub: https://github.com/lnp2pBot/bot
- Støtte: [@lnp2pbotHelp] (https://t.me/lnp2pbotHelp)