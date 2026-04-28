---
name: Peach
description: Komplett guide til bruk av Peach og handel med bitcoins i P2P
---

![cover](assets/cover.webp)





## Innledning



KYC-frie peer-to-peer-børser (P2P) er avgjørende for å bevare brukernes konfidensialitet og økonomiske autonomi. De muliggjør direkte transaksjoner mellom enkeltpersoner uten behov for identitetsbekreftelse, noe som er avgjørende for dem som verdsetter personvern. For en mer inngående forståelse av teoretiske konsepter, se BTC204-kurset:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### 1. Hva er Peach?



Peach er en P2P utvekslingsplattform som lar brukerne kjøpe og selge bitcoins uten KYC. Den tilbyr et intuitivt grensesnitt og avanserte sikkerhetsfunksjoner. Sammenlignet med andre løsninger som Bisq, HodlHodl og Robosat, skiller Peach seg ut for sin brukervennlighet.


Et multisignature escrow-system (2-2) garanterer sikkerheten til midler under transaksjoner. Peach støtter ulike betalingsmetoder, og har et omdømmesystem for å veilede handelsmenn i deres handlinger. Som vanlig med P2P-plattformer er det derfor viktig å opprettholde et godt omdømme for å opprettholde troverdighet hos andre handelsmenn.



### 2. Personvern og innsamlede data



**Hvilken informasjon samler Peach inn?



Peach bestreber seg på å lagre et absolutt minimum av data om sine brukere. Her er en oversikt over dataene som lagres på serverne våre:





- En hash av din unike applikasjonsidentifikator (AdID)
- En hash av betalingsdataene dine
- Dine krypterte samtaler
- Transaksjonsdata for å sikre at anonyme brukere ikke overskrider handelsgrensen (typer betalingsmetoder som brukes, kjøps- og salgsbeløp)
- Addresses brukes til å sende og motta fra sperret konto
- Bruksdata (Firebase og Google Analytics), kun med ditt samtykke



Som en påminnelse: En hash er data som er gjort ugjenkjennelige, på samme måte som kryptering. De samme dataene vil alltid produsere den samme hash, noe som gjør det mulig å oppdage duplikater uten å kjenne originaldataene.



*For en mer detaljert forklaring av hashing, ta dette kurset:*



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

**Hvem kan se betalingsopplysningene mine?





- Bare motparten din kan se betalingsopplysningene dine
- Data overføres via Peach-servere, men er fullstendig kryptert fra ende til ende
- I tilfelle en tvist, vil betalingsopplysningene og samtalehistorikken din være synlig for den tildelte Peach-mekleren



## Installasjon og konfigurasjon



### 1. Installer Peach-applikasjonen



![Installation de Peach](assets/fr/01.webp)





- Last ned applikasjonen fra [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/). På iOS må du først installere appen [testflight](https://apps.apple.com/us/app/testflight/id899247664).
- Følg installasjonsinstruksjonene på enheten din.
- Under installasjonen blir du bedt om å velge om du ønsker å dele visse data for å forbedre Peach-applikasjonen. (bilde 1)
- På det neste skjermbildet (bilde 2) har du to alternativer:
 - Hvis du er en ny bruker, klikker du på "Ny bruker" for å opprette en ny profil
 - Hvis du allerede har en konto, kan du bruke "Gjenopprett" for å gjenopprette din eksisterende profil
- Hvis du har en henvisningskode, kan du oppgi den her.
- For å gjenopprette en eksisterende konto (bilde 3), trenger du :
 - Sikkerhetskopifilen din
 - Passordet for å dekryptere denne filen



### 2. Oversikt over hovedskjermbildene



Peach-applikasjonen er organisert rundt fire hovedskjermbilder som er tilgjengelige fra den nederste navigasjonslinjen:



![Navigation dans l'application](assets/fr/02.webp)





- Hjem (4)** : Hovedskjermbildet der du kan velge å kjøpe eller selge, opprette nye transaksjoner og få tilgang til tilgjengelige tilbud:
 - opprett tilbud med de to knappene nedenfor (opprett kjøp / opprett salg)
 - dra nytte av eksisterende tilbud opprettet av andre brukere, ved å bruke de to knappene nedenfor ("Kjøp"/"Selg").





- Wallet (5)** : Din integrerte bitcoin wallet som lar deg :
 - Sjekk saldoen din
 - Motta bitcoins
 - Envoyer bitcoins (med myntkontroll)
 - Se transaksjonshistorikken din
 - Finansiering av salget ditt





- Handler (6)**: dine nåværende og tidligere kontrakter, under tre faner:
 - Innkjøp under utførelse
 - Pågående salg
 - Historikken til børsene dine





- Innstillinger (7)** : Konfigurasjonsknutepunktet for
 - Se profilen din (omdømme, merker, grenser osv.)
 - Håndtering av sikkerhet (backup, pin)
 - Administrer betalingsmåtene dine
 - Kontakt support
 - Endre språk
 - osv.



### 3. Konfigurer betalingsmåtene dine



![Accès aux paramètres de paiement](assets/fr/03.webp)



Du kan administrere betalingsmåtene dine i innstillingene (bilde 8)



Peach tilbyr betaling på nett og personlig betaling (kun på registrerte møter).



**Online-betalinger



**Viktig:**


for å beskytte brukerne krever Peach at kilden til midlene samsvarer med den annonserte. Det er opp til de næringsdrivende å sørge for at dette er tilfelle, for deres egen beskyttelse.



![Configuration des paiements en ligne](assets/fr/04.webp)



Slik legger du til en metode :




- Klikk på "Legg til en valuta/metode" i "online"-fanen
- Velg valuta
- Velg ønsket betalingsmåte



*Betalingsmåter som er tilgjengelige:*



***For bankoverføringer: ***




- SEPA (standard eller øyeblikkelig)
- Fyll inn SEPA-bankopplysningene dine.



***Online wallet aksepteres :***




- Flere alternativer er tilgjengelige avhengig av hvilket land du bor i (Revolut, Paypal, Wise, Strike osv.)
- Følg instruksjonene for å legge til påloggingsinformasjonen din



*gavekort brukbart:*** Gavekort brukbart:*** Gavekort brukbart:*** Gavekort brukbart:*** Gavekort brukbart:*** Gavekort brukbart:*** Gavekort brukbart:***




- Amazon, Steam osv.
- Angi kortets utstedelsesland og annen nødvendig informasjon



***Nasjonale betalingsalternativer:***


Landspesifikke betalingssystemer :




- Satispay (Italia)
- MB Way (Portugal)
- Bizum (Spania)
- Raskere betalinger (Storbritannia)
- osv.



***For betalinger ansikt til ansikt: ***



![Configuration des paiements en personne](assets/fr/05.webp)





- Velg "Meetup" (bilde 12)
- Velg deretter møtet ditt fra listen (bilde 13)



### Bruksanvisning





- Du kan legge til flere betalingsmåter
- Jo flere metoder du legger til, desto flere tilbud får du tilgang til
- Kontroller at opplysningene dine er korrekte før du registrerer deg
- Du kan når som helst endre eller slette betalingsmåtene dine



**Sikkerhetsnotat**: Betalingsinformasjonen din er kryptert og deles kun med vekslingspartneren din under en transaksjon, bortsett fra i tilfelle en tvist, der en Peach-mekler også vil ha tilgang.



### 4. Slik sikrer du porteføljen din



**Forståelse av Peach-kontoen din



En Peach-konto har ikke noe brukernavn og passord. Det er en fil som er lagret lokalt på telefonen din, noe som betyr at Peach ikke trenger å lagre dataene dine eller kjenne identiteten din: Du har kontrollen. Denne filen inneholder alle dataene dine: inkludert de 12 bitcoin-gjenopprettingsordene, PGP-nøkler, betalingsdetaljer og så videre. Det er derfor viktig å lagre denne filen og beskytte den med et __robust__-passord.



Denne tilnærmingen garanterer en viss grad av konfidensialitet, og overlater ansvaret for data- og sikkerhetskopihåndtering til brukeren. Hvis du mister telefonen din uten sikkerhetskopi, mister du tilgangen til Peach-kontoen og pengene dine.



**Opprett sikkerhetskopiene dine**






- Åpne innstillinger fra fanen nederst til høyre på startskjermen
- Velg alternativet "sikkerhetskopier" i innstillingsmenyen



![Processus de sauvegarde](assets/fr/06.webp)



To typer sikkerhetskopiering er tilgjengelig:



**Lagre kontofilen (bilde 14)**




- Klikk på "Opprett ny sikkerhetskopi"
- Opprett et **sterkt** passord for å kryptere sikkerhetskopifilen
- Send denne filen til et sted som sikrer at den er redundant i tilfelle telefonen skulle gå tapt.



Filsikkerhetskopien gjenoppretter hele Peach-kontoen din, inkludert :




- Din portefølje
- Betalingsmåtene dine
- Betalingsdata
- Transaksjonshistorikk med detaljer om motparter og samtaler med dem



**Lagring av gjenopprettingsfrasen (bilde 15)**




- Følg instruksjonene for å vise gjenopprettingsfrasen din
- Skriv ordene nøye ned i riktig rekkefølge
- Lagre denne sikkerhetskopien på et sikkert sted, helst et annet sted enn kontofilen



Gjenopprettingsfrasen lar deg gjenopprette :




- Ditt omdømme, dine bransjer
- Dine bitcoin-midler



Men **IKKE** følgende:




- Dine nåværende og tidligere samtaler
- Betalingsdata
- Motpartsinformasjon i transaksjonshistorikken




## Kjøp og salg av bitcoins



### 1.a Hvordan kjøpe bitcoins: Ta et tilbud om å selge



En kjøpers første refleks bør være å sjekke ut tilbudene til salgs som allerede er finansiert med bitcoin.



![Vue des offres de vente et filtres](assets/fr/07.webp)





- Klikk på "Kjøp"-knappen på startskjermen (bilde 16)
- Du kan deretter bla gjennom en liste over bitcoins som har blitt plassert i escrow-systemet og er klare for salg (bilde 17). Du kan se beløpet, prisen (i % i forhold til KYCmarkedet), betalingsmåtene og hvilke valutaer som aksepteres.
- Bruk filtre til å sortere og ordne tilbudene (bilde 18).
- Merk: Knappen nederst på filtersiden gjør at du kan motta varsel når et tilbud som samsvarer med filtrene dine, har blitt publisert, og "tilbakestill"-knappen, som ganske enkelt sletter alle filtrene (bilde 18).



![Sélection et confirmation d'achat](assets/fr/08.webp)





- Se tilbudet som passer deg, og send en bytteforespørsel (bilde 19)
- Du kan sende inn flere bytteforespørsler, og det første positive tilbudet vil kansellere de andre forespørslene dine.
- Betal på avtalt måte.


**Påminnelse:** Pengekilden må stemme overens med den du oppga da du la til betalingsmåten.




- Bekreft betalingen i applikasjonen så snart den er utført**.
- Vent på at selgeren mottar betalingen, og erklær den som sådan (bilde 20)
- Og til slutt, evaluer opplevelsen din med selgeren (bilde 21)



![Réception des bitcoins](assets/fr/09.webp)





- Følg med på statusen til transaksjonen din
- Sjekk bekreftelse på mottak av bitcoins
- Midlene vil være tilgjengelige i Peach-porteføljen din (bilde 22 og 23)



### 1.b Hvordan kjøpe bitcoins: Opprett et bud



Hvis du ikke finner et passende tilbud om å selge, kan du opprette et tilbud om å kjøpe. Siden dette ikke forplikter noen bitcoin på dette stadiet, har du mindre sjanse til å finne en byttepartner, spesielt hvis du har et dårlig eller ikke-eksisterende rykte. For å bøte på dette er det viktig at du, når du oppretter tilbudet, *gir et høypremietilbud* for å motivere selgere til å velge tilbudet ditt. La oss gå videre:



![Creation d'ordre d'achat](assets/fr/10.webp)





- Klikk på knappen "Opprett et kjøpstilbud" på startskjermen (bilde 24)
- Legg til en betalingsmetode, hvis du ikke allerede har gjort det, og angi preferansene dine (antall, premium osv.) (bilde 25).


Med alternativet "øyeblikkelig" kan du godta en handelsforespørsel automatisk.




 - Klikk igjen på "Opprett et bud" for å fortsette
- Når du har opprettet en bytteforespørsel, er det selgerens tur til å henvende seg til deg. Du kan lukke og avslutte appen uten bekymringer.
- Du kan endre premien hvis du ikke mottar noen forespørsler. Husk at en høyere premie vil motivere selgerne til å lete etter tilbudet ditt (bilde 26).
- Du finner tilbudet ditt i "Kjøp"-fanen, som i sin tur befinner seg i "Exchange"-vinduet (fig. 27)



![Reception d'une demande de vente, messagerie](assets/fr/11.webp)





- Når du mottar en kjøpsforespørsel (fig. 28) (og hvis du ikke har deaktivert øyeblikkelig handel i fig. 25), godtar du handelen etter å ha sjekket selgerens omdømme. Hvis øyeblikkelig handel er aktivert, hopper du direkte til bilde 29.
- Selgeren må deretter plassere bitcoinene i escrow-systemet ("fund the safe"). (bilde 29)
- Betal deretter selgeren på destinasjonen som vises i figur 30, via ditt personlige banksystem. Ikke dra markøren "Jeg har betalt" før du har gjort det!
- Du kan kommunisere med selgeren via meldingssystemet (P2P kryptert). Hvis det oppstår et problem, kan du åpne en tvist ved å klikke på ikonet øverst i høyre hjørne (bilde 31). En Peach-mekler vil da gå inn i diskusjonen.



![Offre de vente completée](assets/fr/12.webp)





- Når selgeren har mottatt pengene, vil han rapportere det, og escrow-systemet vil frigjøre bitcoinene, som vil være på vei til din wallet (som standard via GroupHug, Peachs transaksjonsgrupperingssystem, som kjører en gang om dagen),
- Vurder din erfaring med selgeren



Nå er det nok!



**Merknad for nye kjøpere:** Selgerne baserer sine handler på kjøpernes omdømme, og har en tendens til å unngå bud fra kjøpere som ikke har gjennomført noen handler. Det er i første omgang lettere å bygge opp et rykte ved å akseptere eksisterende salgstilbud.




### 2.a Hvordan selge bitcoins: Opprett et salg



Den raskeste og enkleste måten å selge på Peach er å **opprette et salgstilbud**.



![Création d'un ordre de vente](assets/fr/13.webp)





- Klikk på "Opprett et salgstilbud" på startsiden (bilde 32)
- Konfigurer tilbudet ditt, sørg for at du legger inn en betalingsmetode og de riktige parameterne


du kan også :




  - opprette flere identiske tilbud
  - aktiver "øyeblikkelig bytte", slik at den første kjøperen som dukker opp, kan overta kontrakten (uten din bekreftelse) og gå videre med betalingen.
  - velg en refusjonsadresse
  - finansiere bagasjerommet fra din wallet Peach
- Finansier transaksjonen ved å sende bitcoins til den oppgitte adressen (bilde 34)
- Vent på bekreftelse av transaksjonen. Når dette er gjort, vil tilbudet ditt være synlig på markedet.



![Attente du paiement](assets/fr/14.webp)





- Vent på at en kjøper skal akseptere tilbudet ditt. Vurder å øke premien (%) hvis du ønsker å få fortgang i prosessen (bilde 36)
- Når du har mottatt en bytteforespørsel, kan du sjekke kjøperens omdømme. Vurder selv om profilen passer for deg, og klikk "godta" hvis den gjør det. (37)
- Nå er det kjøperens tur til å foreta betalingen fra sin bank til din. Han vil deretter videresende betalingen til deg. Ikke nøl med å kontakte kjøperen i chatten.
- etter at du har kontrollert at pengene er mottatt av banken din*, frigjør du pengene ved å klikke på knappen "jeg har mottatt betaling" (bilde 38). Bekreft aldri mottak av en betaling før du har sjekket at den er mottatt på kontoen din.
- Evaluer transaksjonen
- Bitcoin frigjøres automatisk til kjøperen,



Vær så god!



**Sikkerhetsmerknader og tips for en vellykket transaksjon:**




 - Følg med på kjøperens opplysninger, og kontroller at opprinnelsen til pengene stemmer overens med den som er beskrevet på Peach. Hvis opprinnelsen til pengene ikke stemmer overens med den som er oppgitt, går du til Chat og åpner en diskusjon (bilde 39), og sender pengene tilbake til opprinnelsen.
 - Følg instruksjonene i den gule katten.
 - Svar raskt på meldinger fra motparten din
 - vær på vakt mot kjøperens holdning, spesielt når du har å gjøre med en profil med lite erfaring
 - Ikke nøl med å bruke meklingstjenesten hvis du har et problem



### 2.b Hvordan selge bitcoins: ta et bud



Det er også mulig å se og velge kjøpstilbud. Her må du være ekstra forsiktig, for det er her de fleste svindlerne er å finne.



![Prendre une offre d'achat](assets/fr/15.webp)





- Klikk på "Salg" på startsiden (bilde 40)
- Bruk filtrene til å se og velge de mest attraktive tilbudene (bilde 41)



![vérification de la réputation](assets/fr/16.webp)





- før du ber om en handel, anbefaler vi at du vurderer egnetheten til kjøperens profil. Du kan klikke på et tilbud og deretter på brukerens ID for å se profilen hans. Tilbudet på bilde 42 kan for eksempel anses som "risikabelt" (ny bruker, relativt høyt beløp). "Risikoen" du løper ved å benytte deg av dette tilbudet er ganske enkelt å kaste bort tid, så lenge du ikke gjør den feilen å frigjøre bitcoinsene uten å ha mottatt pengene. Du kan fortsatt sette inn bitcoinsene i safen.


Den på bilde 43 kommer derimot fra en erfaren trader (bilde 44), uten noen tvister i historikken. Det er derfor et mindre risikabelt tilbud.



![Match avec vendeur](assets/fr/17.webp)





- Når du har bedt om et tilbud, og hvis kjøperen aksepterer forespørselen din, vil applikasjonen ta deg til bilde 34, der du kan fortsette handelen som beskrevet nedenfor.




## Fordeler og ulemper



### Fordeler med Peach





- Ingen KYC kreves**: Bevarer brukernes konfidensialitet.
- Ingen tilgang til bankopplysninger**: Peach har ingen tilgang til bankopplysningene dine eller identiteten din.
- Interface intuitiv**: Enkel å bruke for middels erfarne brukere.
- Åpen kildekode** : Kildekoden er offentlig og kan verifiseres av fellesskapet.



### Peach ulemper





- Begrenset Liquidity**: Mindre handelsvolum enn mer etablerte plattformer.
- Regulatorisk risiko** : Applikasjonen administreres av et sveitsisk selskap. Den er derfor underlagt sveitsisk regelverk, som kan utvikle seg og potensielt sensurere applikasjonen.



## Nyttige ressurser





- Fransk forklaringsvideo: [YouTube] (https://youtu.be/ziwhv9KqVkM)
- Hurtigstartveiledning: [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/)
- [Support telegram] (t.me/peachtopeach) (pass opp for svindlere, administratorer vil aldri skrive til deg først via privat melding)