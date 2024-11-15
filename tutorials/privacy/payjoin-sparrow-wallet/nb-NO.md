---
name: Payjoin - Sparrow Wallet
description: Hvordan utføre en Payjoin-transaksjon med Sparrow Wallet?
---
![opplæringsdekselbilde sparrow payjoin](assets/cover.webp)

_**ADVARSEL:** Etter arrestasjonen av grunnleggerne av Samourai Wallet og beslagleggelsen av deres servere den 24. april, fungerer nå Payjoins Stowaway på Samourai Wallet kun ved manuelt utveksling av PSBT mellom de involverte partene, forutsatt at begge brukerne er koblet til sin egen Dojo. Når det gjelder Sparrow, fungerer Payjoins via BIP78 fortsatt. Imidlertid kan disse verktøyene bli startet på nytt i de kommende ukene. I mellomtiden kan du alltid lese denne artikkelen for å forstå den teoretiske funksjonen av payjoins._

_Vi følger nøye med på utviklingen av denne saken samt utviklingen angående de tilknyttede verktøyene. Vær trygg på at vi vil oppdatere denne opplæringen når ny informasjon blir tilgjengelig._

_Denne opplæringen er gitt kun for utdannings- og informasjonsformål. Vi støtter eller oppmuntrer ikke bruk av disse verktøyene til kriminelle formål. Det er brukerens ansvar å overholde lovene i sin jurisdiksjon._

---

> *"Tving blockchain-spioner til å tenke om alt de tror de vet."*

Payjoin er en spesifikk Bitcoin-transaksjonsstruktur som forbedrer brukerens personvern under utgifter ved å samarbeide med betalingsmottakeren. Det finnes flere implementeringer som letter oppsettet og automatiseringen av PayJoin. Blant disse implementeringene er den mest kjente Stowaway utviklet av Samourai Wallet-teamet. Denne opplæringen har som mål å veilede deg gjennom prosessen med å utføre en Stowaway Payjoin-transaksjon ved bruk av Sparrow Wallet-programvaren.

## Hvordan fungerer Stowaway?

Som nevnt tidligere, tilbyr Samourai Wallet et PayJoin-verktøy kalt "Stowaway." Det er tilgjengelig gjennom Sparrow Wallet-programvaren på PC eller Samourai Wallet-applikasjonen på Android. For å utføre en Payjoin må mottakeren, som også fungerer som en samarbeidspartner, bruke programvare som er kompatibel med Stowaway, nemlig Sparrow eller Samourai Wallet. Disse to programmene er interoperable, noe som tillater Stowaway-transaksjoner mellom en Sparrow-lommebok og en Samourai-lommebok, og omvendt.

Stowaway støtter seg på en kategori transaksjoner som Samourai refererer til som "Cahoots." En Cahoot er i hovedsak en samarbeidstransaksjon mellom flere brukere som krever utveksling av informasjon utenfor kjeden. For øyeblikket tilbyr Samourai to Cahoots-verktøy: Stowaway (Payjoins) og StonewallX2 (som vi vil utforske i en fremtidig artikkel).

Cahoots-transaksjoner innebærer utveksling av delvis signerte transaksjoner mellom brukere. Denne prosessen kan være lang og tungvint, spesielt når den gjøres på avstand. Imidlertid kan den fortsatt gjøres manuelt med en annen bruker, noe som kan være praktisk hvis samarbeidspartnerne er fysisk nærme. I praksis innebærer dette manuell utveksling av fem QR-koder som må skannes etter hverandre.

Når dette gjøres på avstand, blir prosessen for kompleks. For å adressere dette problemet har Samourai utviklet et kryptert kommunikasjonsprotokoll basert på Tor, kalt "Soroban." Med Soroban automatiseres de nødvendige utvekslingene for en Payjoin bak et brukervennlig grensesnitt. Dette er den andre metoden vi vil utforske i denne artikkelen.

Disse krypterte utvekslingene krever etablering av en forbindelse og autentisering mellom Cahoots-deltakerne. Soroban-kommunikasjoner stoler på brukernes Paynyms. Hvis du ikke er kjent med Paynyms, inviterer jeg deg til å referere til denne artikkelen for flere detaljer: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/paynym-bip47)
For å si det enkelt, er en Paynym en unik identifikator knyttet til lommeboken din som tillater ulike funksjoner, inkludert kryptert meldingsutveksling. Paynym presenteres i form av en identifikator og en illustrasjon som representerer en robot. Her er et eksempel på min på Testnet: ![Paynym Sparrow](assets/en/1.webp)
**Oppsummert:**
- *Payjoin* = Spesifikk struktur av samarbeidstransaksjon;
- *Stowaway* = Payjoin-implementering tilgjengelig på Samourai og Sparrow Wallet;
- *Cahoots* = Navn gitt av Samourai til alle deres typer samarbeidstransaksjoner, inkludert Payjoin Stowaway;
- *Soroban* = Kryptert kommunikasjonsprotokoll etablert på Tor, som tillater samarbeid med andre brukere i konteksten av en Cahoots-transaksjon.
- *Paynym* = Unik identifikator for en lommebok som tillater kommunikasjon med en annen bruker på Soroban, for å gjennomføre en Cahoots-transaksjon.

[**-> Lær mer om Payjoin-transaksjoner og deres nytte**](https://planb.network/tutorials/privacy/payjoin)

## Hvordan etablere en forbindelse mellom Paynyms?

For å utføre en fjern Cahoots-transaksjon, spesifikt en PayJoin (Stowaway) via Samourai eller Sparrow, er det nødvendig å "Følge" brukeren du har til hensikt å samarbeide med, ved å bruke deres Paynym. I tilfellet med en Stowaway, betyr dette å følge personen du ønsker å sende bitcoins til.

**Her er fremgangsmåten for å etablere denne forbindelsen:**

Først må du skaffe mottakerens Paynym-identifikator. Dette kan gjøres ved å bruke deres kallenavn eller betalingskode. For å gjøre dette, fra mottakerens Sparrow-lommebok, velg `Verktøy`-fanen, deretter klikk på `Vis PayNym`.
![Vis Paynym](assets/notext/2.webp)
![Paynym Sparrow](assets/en/1.webp)
På din side, åpne din Sparrow Wallet og få tilgang til samme `Vis PayNym`-meny. Hvis du bruker din Paynym for første gang, vil du trenge å skaffe en identifikator ved å klikke på `Hent PayNym`.
![Hent paynym](assets/notext/3.webp)
Deretter, skriv inn din samarbeidspartners Paynym-identifikator (enten deres kallenavn `+...` eller deres betalingskode `PM...`) i `Finn Kontakt`-boksen, deretter klikk på `Legg til Kontakt`-knappen.
![legg til kontakt](assets/notext/4.webp)
Programvaren vil deretter tilby deg en `Koble Kontakt`-knapp. Det er ikke nødvendig å klikke på denne knappen for vår opplæring. Dette trinnet er kun nødvendig hvis du planlegger å gjøre betalinger til Paynymen indikert i konteksten av BIP47, som er urelatert til vår opplæring.

Når mottakerens Paynym er fulgt av din Paynym, gjenta denne operasjonen i motsatt retning slik at din mottaker også følger deg. Du kan deretter utføre en Payjoin.

## Hvordan utføre en Payjoin på Sparrow Wallet?
Hvis du har fullført disse få forberedende trinnene, er du endelig klar til å utføre Payjoin-transaksjonen! For å gjøre dette, følg vår videoopplæring:
![Payjoin Tutorial - Sparrow Wallet](https://youtu.be/ZQxKod3e0Mg)

**Eksterne ressurser:**
- https://docs.samourai.io/en/spend-tools#stowaway ;
- https://sparrowwallet.com/docs/spending-privately.html.