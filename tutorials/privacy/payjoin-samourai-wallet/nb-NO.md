---
name: Payjoin - Samourai Wallet
description: Hvordan utføre en Payjoin-transaksjon på Samourai Wallet?
---
![samourai payjoin cover](assets/cover.webp)

***OBS:** Etter arrestasjonen av grunnleggerne av Samourai Wallet og beslagleggelsen av deres servere den 24. april, fungerer Payjoins Stowaway på Samourai Wallet kun ved manuelt utveksling av PSBT mellom de berørte partene, forutsatt at begge brukerne er koblet til sin egen Dojo. Når det gjelder Sparrow, fungerer Payjoins via BIP78 fortsatt. Det er imidlertid mulig at disse verktøyene vil bli relansert i de kommende ukene. I mellomtiden kan du fortsatt lese denne artikkelen for å forstå den teoretiske funksjonen av Stowaway.*

_Om du planlegger å utføre en Stowaway manuelt, er prosedyren veldig lik den som er beskrevet i denne opplæringen. Den viktigste forskjellen ligger i valget av typen Stowaway-transaksjon: i stedet for å velge `Online`, klikk på `In Person / Manual`. Deretter må du manuelt utveksle PSBT-ene for å konstruere Stowaway-transaksjonen. Hvis du er fysisk nær din samarbeidspartner, kan du skanne QR-kodene etter hverandre. Hvis du er på avstand, kan JSON-filer utveksles via en sikker kommunikasjonskanal. Resten av opplæringen forblir uendret._

_Vi følger nøye med på utviklingen av denne saken samt utviklingen angående de tilknyttede verktøyene. Vær trygg på at vi vil oppdatere denne opplæringen etter hvert som ny informasjon blir tilgjengelig._

_Denne opplæringen er kun gitt for utdannings- og informasjonsformål. Vi støtter eller oppmuntrer ikke bruk av disse verktøyene til kriminelle formål. Det er brukerens ansvar å overholde lovene i sin jurisdiksjon._

---

> *"Tving blockchain-spioner til å revurdere alt de tror de vet."*

Payjoin er en spesifikk Bitcoin-transaksjonsstruktur som forbedrer brukerens personvern under en utgift ved å samarbeide med betalingsmottakeren. Det finnes flere implementeringer som letter oppsettet og automatiseringen av PayJoin. Blant disse implementeringene er den mest kjente Stowaway, utviklet av teamene hos Samourai Wallet. Denne opplæringen forklarer hvordan du utfører en Stowaway Payjoin-transaksjon ved bruk av Samourai Wallet-applikasjonen.

## Hvordan fungerer Stowaway?

Som nevnt tidligere, tilbyr Samourai Wallet et PayJoin-verktøy kalt "Stowaway." Det er tilgjengelig gjennom Sparrow Wallet-programvaren på PC eller Samourai Wallet-applikasjonen på Android. For å utføre en Payjoin må mottakeren, som også fungerer som en samarbeidspartner, bruke programvare som er kompatibel med Stowaway, nemlig Sparrow eller Samourai. Disse to programmene er interoperable, noe som tillater en Stowaway-transaksjon mellom en Sparrow-lommebok og en Samourai-lommebok, og omvendt.

Stowaway støtter seg på en kategori transaksjoner som Samourai refererer til som "Cahoots." En Cahoot er i hovedsak en samarbeidstransaksjon mellom flere brukere, som krever utveksling av informasjon utenfor kjeden. Til dags dato tilbyr Samourai to Cahoots-verktøy: Stowaway (Payjoins) og StonewallX2 (som vi vil utforske i en fremtidig artikkel).

Cahoots-transaksjoner involverer utvekslinger av delvis signerte transaksjoner mellom brukere. Denne prosessen kan være lang og tungvint, spesielt når den gjøres på avstand. Det kan imidlertid fortsatt utføres manuelt med en annen bruker, noe som kan være praktisk hvis samarbeidspartnerne er fysisk nær hverandre. I praksis innebærer dette å manuelt utveksle fem QR-koder som skal skannes etter hverandre.
Når dette gjøres på avstand, blir prosessen for kompleks. For å adressere dette problemet har Samourai utviklet et kryptert kommunikasjonsprotokoll basert på Tor, kalt "Soroban." Med Soroban blir utvekslingene som er nødvendige for en Payjoin automatisert bak et brukervennlig grensesnitt. Dette er den andre metoden vi vil studere i denne artikkelen.
Disse krypterte utvekslingene krever etablering av en forbindelse og autentisering mellom Cahoots-deltakerne. Soroban-kommunikasjonen er derfor basert på brukernes Paynyms. Hvis du ikke er kjent med Paynyms, inviterer jeg deg til å konsultere denne artikkelen for flere detaljer: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)

For å si det enkelt, er en Paynym en unik identifikator knyttet til lommeboken din som tillater ulike funksjonaliteter, inkludert kryptert meldingsutveksling. Paynymen presenteres i form av en identifikator og en illustrasjon som representerer en robot. Her er et eksempel på min på Testnet: ![paynym samourai wallet](assets/en/1.webp)

**Oppsummert:**
- _Payjoin_ = Spesifikk struktur av samarbeidstransaksjoner;
- _Stowaway_ = Payjoin-implementering tilgjengelig på Samourai og Sparrow Wallet;
- _Cahoots_ = Navn gitt av Samourai til alle deres typer samarbeidstransaksjoner, inkludert Payjoin Stowaway;
- _Soroban_ = Kryptert kommunikasjonsprotokoll etablert på Tor, som tillater samarbeid med andre brukere i konteksten av en Cahoots-transaksjon;
- _Paynym_ = Unik identifikator for en lommebok som tillater kommunikasjon med en annen bruker på Soroban, for å gjennomføre en Cahoots-transaksjon.

[**-> Lær mer om Payjoin-transaksjoner og deres nytte**](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)

## Hvordan etablere en forbindelse mellom Paynyms?

For å gjennomføre en fjern Cahoots-transaksjon, spesifikt en PayJoin (Stowaway) via Samourai, er det nødvendig å "Følge" brukeren du har til hensikt å samarbeide med, ved å bruke deres Paynym. I tilfellet med en Stowaway, betyr dette å følge personen du ønsker å sende bitcoins til.

**Her er prosedyren for å etablere denne forbindelsen:**

For å begynne, trenger du å skaffe betalingskoden til mottakerens Paynym for Payjoin. I Samourai Wallet-applikasjonen må mottakeren trykke på ikonet til sin Paynym (den lille roboten) som er plassert øverst til venstre på skjermen, og deretter klikke på sitt Paynym-kallenavn, som starter med `+...`. For eksempel, mitt er `+namelessmode0aF`. Hvis din samarbeidspartner bruker Sparrow Wallet, inviterer jeg deg til å konsultere vår dedikerte opplæring ved å klikke her.

![connexion paynym samourai](assets/notext/2.webp)

Din samarbeidspartner vil deretter bli omdirigert til sin Paynym-side. Derfra kan de enten dele sine Paynym-legitimasjoner med deg eller dele sin QR-kode for deg å skanne. For å gjøre dette, må de klikke på det lille "del"-ikonet som er plassert øverst til høyre på skjermen.
![partager paynym samourai](assets/en/1.webp)

På din side, start din Samourai Wallet-applikasjon og få tilgang til "PayNyms"-menyen på samme måte. Hvis dette er første gang du bruker din Paynym, må du skaffe identifikatoren.

![demander un paynym](assets/notext/3.webp)

Deretter klikker du på det blå "+" nederst til høyre på skjermen.
![ajouter paynym collaborateur](assets/notext/4.webp)
Du kan deretter lime inn betalingskoden til din samarbeidspartner ved å velge `COLLER LE CODE PAIEMENT`, eller åpne kameraet for å skanne deres QR-kode ved å trykke `SCANNEZ LE CODE QR`. ![lim inn paynym-identifikator](assets/notext/5.webp)
Klikk på `SUIVRE`-knappen.
![følg paynym](assets/notext/6.webp)
Bekreft ved å klikke `YES`.
![bekreft følg paynym](assets/notext/7.webp)
Programvaren vil deretter tilby deg en `SE CONNECTER`-knapp. Det er ikke nødvendig å klikke på denne knappen for vår opplæring. Dette trinnet er kun nødvendig hvis du planlegger å gjøre betalinger til den andre Paynym som en del av BIP47, noe som ikke er relatert til vår opplæring.
![koble til paynym](assets/notext/8.webp)
Når mottakerens Paynym er fulgt av din Paynym, gjenta denne operasjonen i motsatt retning slik at mottakeren også følger deg. Du kan deretter utføre en Payjoin.

## Hvordan gjøre en Payjoin på Samourai Wallet?

Hvis du har fullført disse innledende trinnene, er du endelig klar til å utføre Payjoin-transaksjonen! For å gjøre dette, følg vår videoopplæring:

![Payjoin Videoopplæring - Samourai Wallet](https://youtu.be/FXW6XZim0ww?si=EXalYwK1t9DT48aE)

**Eksterne ressurser:**
- https://docs.samourai.io/en/spend-tools#stowaway.