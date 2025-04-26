---
name: JoinBot
description: Forstå og bruke JoinBot
---

![DALL·E – samurairobot i en rød skog, 3D-render](assets/cover.webp)

***ADVARSEL:** Etter arrestasjonen av grunnleggerne av Samourai Wallet og beslagleggelsen av deres servere den 24. april, **er JoinBot-tjenesten ikke lenger tilgjengelig**. Fra nå av er det ikke lenger mulig å bruke dette verktøyet. Du kan imidlertid fortsatt gjennomføre Stonewall X2, men du må finne en samarbeidspartner og manuelt utveksle PSBTs. Denne tjenesten kan bli relansert i de kommende månedene, avhengig av utviklingen i saken.*

_Vi følger nøye med på utviklingen av denne saken samt utviklingen angående de tilknyttede verktøyene. Vær trygg på at vi vil oppdatere denne opplæringen så snart ny informasjon blir tilgjengelig._

_Denne opplæringen er kun tilgjengelig for utdannings- og informasjonsformål. Vi støtter eller oppfordrer ikke til bruk av disse verktøyene til kriminelle formål. Det er brukerens ansvar å overholde lovene i sin jurisdiksjon._

---

JoinBot er et nytt verktøy som er lagt til i Samourai Wallet-pakken med den siste oppdateringen 0.99.98f av den berømte Bitcoin-lommebokprogramvaren. Det lar deg enkelt gjøre en samarbeidstransaksjon for å optimalisere ditt personvern, uten å måtte finne en partner.

*Takk til den utmerkede Fanis Michalakis for ideen om å bruke DALL-E for miniatyrbildet!*

## Hva er en samarbeidstransaksjon på Bitcoin?

Bitcoin er basert på en distribuert og gjennomsiktig kontobok. Alle er i stand til å spore transaksjonene til brukere av dette elektroniske kontantsystemet. For å sikre et visst nivå av personvern, kan Bitcoin-brukere gjøre transaksjoner med en spesifikk struktur for å legge til plausibel benektelse i deres tolkning.

Ideen er ikke å direkte skjule informasjonen, men å forvirre den blant andre. Dette målet brukes i Coinjoins, transaksjoner som bryter historikken til en mynt på Bitcoin og gjør sporingen kompleks. For å oppnå dette resultatet, må flere innganger og utganger av samme beløp opprettes i transaksjonen.

Innganger er inngangene til en Bitcoin-transaksjon, og utganger representerer utgangene. Transaksjonen bruker sine innganger for å skape nye utganger ved å endre utgiftsbetingelsene til en mynt. Denne mekanismen tillater bitcoins å bli flyttet mellom brukere.
Jeg diskuterer dette i detalj i denne artikkelen: Bitcoin Transaction Mechanism: UTXO, Inputs, and Outputs.

En måte å sløre sporene i en Bitcoin-transaksjon på er å gjøre en samarbeidstransaksjon. Som navnet antyder, involverer det en avtale mellom flere brukere, hvor hver av dem setter inn et sum bitcoins som inngang i samme transaksjon og mottar en sum som utgang.

Som nevnt tidligere, er den mest kjente strukturen av en samarbeidstransaksjon Coinjoin. For eksempel, på Coinjoin Whirlpool-protokollen, involverer transaksjoner 5 deltakere som innganger og utganger, hver med samme mengde bitcoins.

![Diagram av en Coinjoin-transaksjon på Whirlpool](assets/1.webp)

En ekstern observatør av denne transaksjonen vil ikke kunne vite hvilken utgang som tilhører hvilken bruker som inngang. Hvis vi tar eksemplet med bruker #4 (lilla), kan vi gjenkjenne deres inngangs UTXO, men vi vil ikke vite hvilken av de 5 utgangene som faktisk er deres. Den opprinnelige informasjonen er ikke skjult, men heller forvirret innenfor en gruppe.
Brukeren er i stand til å benekte besittelsen av en bestemt UTXO som utgang. Dette fenomenet kalles "plausibel benektelse", og det tillater konfidensialitet i en gjennomsiktig Bitcoin-transaksjon.

For å lære mer om Coinjoin, forklarer jeg ALT i denne lange artikkelen: Understanding and using CoinJoin on Bitcoin.
Selv om Coinjoin er svært effektivt for å bryte sporingen av en UTXO, er det ikke egnet for direkte bruk. Faktisk innebærer strukturen å måtte bruke inndata av en forhåndsdefinert mengde og utdata av samme verdi (modulo gruvegebyrer). Imidlertid er transaksjonen for bruk av Bitcoin et kritisk øyeblikk for personvern ettersom det ofte skaper en fysisk kobling mellom brukeren og deres aktivitet på kjeden. Det virker derfor essensielt å bruke verktøy for personvern ved bruk. Det finnes andre samarbeidende transaksjonsstrukturer spesifikt designet for faktiske betalingstransaksjoner.
## StonewallX2-transaksjonen

Blant myriaden av brukerverktøy som tilbys på Samourai Wallet, finner vi den samarbeidende transaksjonen StonewallX2. Det er en mini-Coinjoin mellom to brukere designet for betaling. Fra utsiden kan denne transaksjonen lede til flere mulige tolkninger. Den gir dermed plausibel fornektelse og følgelig, konfidensialitet for brukeren.

Dette oppsettet for StonewallX2-samarbeidstransaksjonen er tilgjengelig på Samourai Wallet og Sparrow Wallet. Dette verktøyet er interoperabelt mellom de to programmene.

Mekanismen er ganske enkel å forstå. Her er hvordan det fungerer i praksis:

> - En bruker ønsker å gjøre en betaling i bitcoins (for eksempel, til en handlende).
> - De henter mottaksadressen til den faktiske betalingsmottakeren (den handlende).
> - De konstruerer en spesifikk transaksjon med flere inndata: minst én som tilhører dem og én som tilhører en ekstern samarbeidspartner.
> - Transaksjonen vil ha 4 utdata, inkludert 2 av samme beløp: én til den handlendes adresse for betaling, én som endring som returnerer til brukeren, én utdata av samme verdi som betalingen som går til samarbeidspartneren, og en annen utdata som også returnerer til samarbeidspartneren.

For eksempel, her er en typisk StonewallX2-transaksjon der jeg gjorde en betaling på 50,125 sats. Det første inndataet på 102,588 sats kommer fra min Samourai-lommebok. Det andre inndataet på 104,255 sats kommer fra lommeboken til min samarbeidspartner:

![StonewallX2 transaksjonsdiagram](assets/2.webp)

Vi kan observere 4 utdata, inkludert 2 av samme beløp for å forvirre sporene:

> - 50,125 sats som går til den faktiske mottakeren av betalingen min.
> - 52,306 sats som representerer min endring og derfor returnerer til en adresse i lommeboken min.
> - 50,125 sats som returnerer til min samarbeidspartner.
> - 53,973 sats som returnerer til min samarbeidspartner.
>   Ved slutten av operasjonen vil samarbeidspartneren ha sitt opprinnelige saldo gjenopprettet (minus gruvegebyrer), og brukeren vil ha betalt til den handlende. Dette tilfører en betydelig mengde entropi til transaksjonen og bryter de utvetydige koblingene mellom avsenderen og mottakeren av betalingen.

Styrken til StonewallX2-transaksjonen er at den fullstendig motvirker en av de empiriske reglene brukt av kjedeanalytikere: felles eierskap av inndata i en multi-inndata-transaksjon. Med andre ord, i de fleste tilfeller, hvis vi observerer en Bitcoin-transaksjon med flere inndata, kan vi anta at alle disse inndataene tilhører samme person. Satoshi Nakamoto hadde allerede identifisert dette problemet for brukerens personvern i hans White Paper:

> "Som en ekstra brannmur, kunne et nytt nøkkelpar brukes for hver transaksjon for å holde dem fra å bli knyttet til en felles eier. Imidlertid er koblingen uunngåelig med multi-inndata-transaksjoner, som nødvendigvis avslører at deres inndata ble eid av samme eier."

Dette er en av de mange empiriske reglene brukt i on-chain analyse for å konstruere adressekluster. For å lære mer om disse heuristikkene, anbefaler jeg å lese denne serien av fire artikler av Samourai, som introduserer emnet på en fantastisk måte.
Styrken til StonewallX2-transaksjonen ligger i det faktum at en ekstern observatør vil tro at de forskjellige inngangene til transaksjonen tilhører en felles eier. I virkeligheten er de to forskjellige brukere som samarbeider. Analysen av betalingen blir dermed ledet til en avledning, og brukerens personvern bevares.
Fra utsiden kan en StonewallX2-transaksjon ikke skilles fra en Stonewall-transaksjon. Den eneste effektive forskjellen mellom dem er at Stonewall ikke er samarbeidende. Den bruker kun UTXOene til en enkelt bruker. Imidlertid, i deres strukturer på kontojournalen, er Stonewall og StonewallX2 helt identiske. Dette tillater enda flere mulige tolkninger av denne transaksjonsstrukturen siden en ekstern observatør ikke vil kunne fortelle om inngangene kommer fra samme person eller fra to samarbeidspartnere.

Videre er fordelen med StonewallX2 over en Stowaway-type PayJoin at den kan brukes i enhver situasjon. Den faktiske mottakeren av betalingen bidrar ikke med noen innganger til transaksjonen. Dermed kan en StonewallX2 brukes til å betale hos enhver handelsmann som aksepterer Bitcoin, selv om handelsmannen ikke bruker Samourai eller Sparrow.
På den andre siden er hovedulempen med denne transaksjonsstrukturen at den krever en samarbeidspartner som er villig til å bruke sine bitcoins for å delta i betalingen din. Hvis du har bitcoin-venner som er villige til å hjelpe deg i enhver situasjon, er dette ikke et problem. Men, hvis du ikke kjenner noen andre Samourai Wallet-brukere, eller hvis ingen er tilgjengelige for å samarbeide, da står du fast.

For å løse dette problemet la Samourai-teamet nylig til en ny funksjon i applikasjonen deres: JoinBot.

# Hva er JoinBot?

Prinsippet til JoinBot er enkelt. Hvis du ikke kan finne noen å samarbeide med for en StonewallX2-transaksjon, kan du samarbeide med JoinBot. I praksis vil du faktisk gjennomføre en samarbeidstransaksjon direkte med Samourai Wallet.

Denne tjenesten er veldig praktisk, spesielt for nybegynnere, ettersom den er tilgjengelig 24/7. Hvis du trenger å gjøre en hastebetaling og ønsker å gjøre en StonewallX2, trenger du ikke lenger å kontakte en venn eller søke etter en online samarbeidspartner. JoinBot vil assistere deg.

En annen fordel med JoinBot er at UTXOene den gir som inngang er eksklusivt fra postmix Whirlpool, noe som forbedrer personvernet til betalingen din. I tillegg, siden JoinBot alltid er online, bør du samarbeide med UTXOer som har store potensielle Anonsets.

Åpenbart har JoinBot noen kompromisser som bør noteres:

> Liksom med en klassisk StonewallX2, er din samarbeidspartner nødvendigvis klar over UTXOene som brukes og deres destinasjon. I tilfellet med JoinBot, vet Samourai detaljene om denne transaksjonen. Dette er ikke nødvendigvis en dårlig ting, men det bør holdes i tankene.
> For å unngå spam, tar Samourai en tjenesteavgift på 3,5% på beløpet av den faktiske transaksjonen, med en maksimal grense på 0,01 BTC. For eksempel, hvis jeg sender en ekte betaling på 100 kilosats med JoinBot, vil tjenesteavgiftsbeløpet være 3 500 sats.
> For å bruke JoinBot, må du ha minst to urelaterte og tilgjengelige UTXOer i lommeboken din.
> I en klassisk StonewallX2 deles gruveavgiftene likt mellom de to samarbeidspartnerne. Med JoinBot, vil du åpenbart måtte betale hele gruveavgiftene.
For at en JoinBot-transaksjon skal være nøyaktig den samme som en klassisk StonewallX2 eller Stonewall-transaksjon, blir betalingen av tjenesteavgifter gjort i en helt separat transaksjon. Refusjonen av halvparten av gruveavgiftene som opprinnelig ble betalt av Samourai, vil bli gjort under denne andre transaksjonen. For å optimalisere ditt personvern til slutt, blir avgjørselen av gebyrer gjort ved å bruke en Stowaway (PayJoin) strukturert transaksjon.

## Hvordan bruke JoinBot?

For å utføre en JoinBot-transaksjon, må du ha en Samourai Wallet. Du kan laste den ned her, eller fra Google Playstore.

I motsetning til flertallet av verktøy utviklet av Samourai, har Sparrow Wallet ennå ikke annonsert implementeringen av JoinBot. Dette verktøyet er derfor kun tilgjengelig på Samourai.

Oppdag steg for steg hvordan du utfører en StonewallX2-transaksjon med JoinBot i denne videoen:

![Hvordan bruke Joinbot](https://youtu.be/80MoMz2Ne5g)

Her er transaksjonsdiagrammet som vi nettopp utførte i videoen:

![Diagram av min StonewallX2-transaksjon med JoinBot.](assets/3.webp)

Vi kan se 5 innganger:

> - 3 innganger på 100 kilosats som kommer fra Samourai (JoinBot).
> - 2 innganger som kommer fra min personlige lommebok, på 3,524 sats og 1.8 megasat.

De 4 utgangene av transaksjonen er som følger:

> - 1 på 212,452 sats til den faktiske mottakeren av min betaling.
> - En annen av samme beløp som går tilbake til en Samourai-adresse.
> - 1 veksel som også går tilbake til Samourai for 87,302 sats. Dette representerer forskjellen mellom totalen av deres innganger (300,000 sats) og forvirringsutgangen (212,452 sats) minus gruveavgiftene.
> - 1 veksel som går tilbake til en annen adresse i min lommebok. Den representerer forskjellen mellom totalen av mine innganger og den faktiske betalingen, minus gruveavgiftene.

Som en påminnelse, representerer ikke gruveavgifter transaksjonsutganger. De representerer simpelthen forskjellen mellom total innganger og total utganger.

## Konklusjon

JoinBot er et tilleggsverktøy som legger til flere valg og frihet for Samourai-brukere. Det tillater en samarbeidende StonewallX2-transaksjon direkte med Samourai som en samarbeidspartner. Denne typen transaksjon hjelper med å forbedre brukerens personvern.

Hvis du kan utføre en klassisk StonewallX2 med en venn, anbefaler jeg fortsatt å bruke dette verktøyet. Men, hvis du er fast og ikke kan finne noen samarbeidspartnere for å gjøre en betaling, vet du at JoinBot vil være tilgjengelig 24/7 for å samarbeide med deg.

**Eksterne ressurser:**
- https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
- https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin