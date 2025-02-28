---
name: Robosats

description: Hvordan bruke Robosats
---

![cover](assets/cover.webp)

RoboSats (https://learn.robosats.com/) er en enkel måte å privat utveksle Bitcoin mot nasjonale valutaer på. Det forenkler peer-to-peer-opplevelsen og bruker lightning hold-fakturaer for å minimere behovet for oppbevaring og tillit.

![video](https://youtu.be/XW_wzRz_BDI)

## Guide

> Denne guiden er fra Bitcoin Q&A (https://bitcoiner.guide/robosats/). All ære til ham, støtt ham der (https://bitcoiner.guide/contribute); BitcoinQ&A er også en bitcoin-mentor. Kontakt ham for veiledning!

![image](assets/0.webp)

RoboSats - En enkel og privat Lightning-basert P2P-utveksling

## Før du starter

### Ting du trenger å vite

| Jargon       | Definisjon                                                                                                                                                                                     |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Robot        | Din automatisk genererte private handelsidentitet. Ikke bruk samme robot mer enn én gang da dette kan forringe personvernet ditt.                                                             |
| Token        | En streng med tilfeldige tegn brukt til å generere din unike robot.                                                                                                                            |
| Maker        | En bruker som oppretter et tilbud om å kjøpe eller selge Bitcoin.                                                                                                                              |
| Taker        | En bruker som tar imot et annet brukers tilbud om å kjøpe eller selge Bitcoin.                                                                                                                 |
| Bond         | Et beløp av Bitcoin låst opp av begge parter som et løfte om å spille rettferdig og fullføre sin del av handelen. Bond er typisk 3% av det totale handelsbeløpet og drives av Hodl Fakturaer. |
| Trade Escrow | Brukes av selgeren som en metode for å holde handelsbeløpet av Bitcoin, igjen ved bruk av Hodl Fakturaer.                                                                                      |
| Fees         | RoboSats tar 0.2% av handelsbeløpet, som deles mellom både maker og taker. Taker betaler 0.175% og maker betaler 0.025%.                                                                       |

## Ting du trenger å ha

### En Lightning Lommebok

RoboSats er Lightning-nativ, så du kommer til å trenge en Lightning-lommebok for å finansiere bonden og motta de kjøpte satsene som kjøper. Du bør være forsiktig når du velger lommeboken din, på grunn av teknologien som brukes for å få RoboSats til å fungere, er ikke alle kompatible.

Hvis du er en nodekjører, er Zeus langt den beste muligheten. Hvis du ikke har din egen node, vil jeg på det sterkeste anbefale Phoenix, en tverrplattform mobil lommebok med enkel oppsett og tilgang til Lightning. Phoenix ble brukt i produksjonen av denne guiden.

### Noe Bitcoin

Kjøpere og selgere trenger å finansiere en bond før noen handel kan finne sted. Dette er vanligvis et veldig lite beløp (~3% av handelsbeløpet), men er likevel et forhåndskrav.

Bruker du RoboSats for å kjøpe dine første sats? Hvorfor ikke få en venn til å låne deg det lille beløpet som kreves for å komme i gang!? Hvis du er alene, her er noen andre flotte alternativer for å skaffe noen noKYC sats for å komme i gang.

### Tilgang til RoboSats

Åpenbart kommer du til å trenge tilgang til RoboSats! Det er fire hovedmåter du kan gjøre dette på:

1. Via Tor Browser (Anbefales!)
2. Via en vanlig nettleser (Ikke anbefalt!)
3. Via Android APK
4. Din egen klient

Hvis du er ny til Tor-nettleseren, lær mer og last den ned [her](https://www.torproject.org/download/).
En kjapp notis for iOS-brukere som ser etter å få tilgang til RoboSats via Tor fra telefonene sine. ‘Onion Browser’ er ikke Tor Browser. Bruk heller Orbot + Safari og Orbot + DuckDuckGo.
## Kjøpe Bitcoin

Følgende steg ble utført i mai 2023 med versjon 0.5.0, tilgjengelig via Tor-nettleseren. Stegene burde være identiske for brukere som får tilgang til RoboSats via Android APK.

På skrivetidspunktet er RoboSats fortsatt under aktiv utvikling, så grensesnittet kan endre seg litt i fremtiden, men de grunnleggende stegene som kreves for å fullføre handelen, bør for det meste forbli uendret.

> Når du først laster RoboSats vil du møte denne landingssiden. Klikk Start.

![bilde](assets/2.webp)

Generer din token og lagre den et sikkert sted som en kryptert notatapp eller passordbehandler. Denne tokenen kan brukes til å gjenopprette din midlertidige Robot-ID i tilfelle nettleseren eller appen lukkes midt i en handel.

![bilde](assets/3.webp)

Møt din nye Robot-identitet, deretter klikk Fortsett.

![bilde](assets/4.webp)

Klikk Tilbud for å bla gjennom ordreboken. Øverst på siden kan du deretter filtrere etter dine preferanser. Husk å ta notat av obligasjonsprosentene og premien over gjennomsnittlig valutakurs.

- Velg Kjøp
- Velg din valuta
- Velg din betalingsmetode(r)

![bilde](assets/5.webp)

> Klikk på tilbudet du ønsker å ta. Skriv inn beløpet (i din valgte fiat-valuta) som du ønsker å kjøpe fra selgeren, deretter ha en siste sjekk av detaljene og klikk Ta Ordre.

Hvis selgeren ikke er online (indikert av en rød prikk på deres profilbilde), vil du se en advarsel om at handelen kan ta lengre tid enn vanlig. Hvis du fortsetter og selgeren ikke fortsetter i tide, vil du bli kompensert med 50% av deres obligasjonsbeløp for din bortkastede tid.

![bilde](assets/6.webp)

Deretter må du låse opp din handelsobligasjon ved å betale fakturaen på skjermen. Dette er en hold-faktura som fryses i lommeboken din. Den vil kun bli belastet hvis du mislykkes med å fullføre din del av handelen.

![bilde](assets/7.webp)

I din Lightning Wallet, skann QR-koden og betal fakturaen.

![bilde](assets/8.webp)

Deretter, i din Lightning Wallet, generer en faktura for det viste beløpet og lim inn i det angitte feltet.

![bilde](assets/9.webp)

Vent på at selgeren låser sitt handelsbeløp. Når dette skjer, vil RoboSats automatisk gå videre til neste steg hvor chattevinduet vil åpne. Si Hei og be selgeren om deres fiat-betalingsinformasjon. Når den er gitt, send betalingen via den valgte metoden og bekreft dette i RoboSats. All chat i RoboSats er PGP-kryptert, noe som betyr at kun du og din handelspartner kan lese meldingene.

![bilde](assets/10.webp)

Når selgeren bekrefter mottak av betalingen, frigjør RoboSats automatisk betalingen ved hjelp av fakturaen som ble gitt tidligere.

![bilde](assets/11.webp)

Når fakturaen er betalt, er handelen ferdig og din obligasjon er låst opp. Du vil da se et handelssammendrag.

![bilde](assets/12.webp)

Sjekk din Lightning Wallet for bekreftelse på at satsene har ankommet.

![bilde](assets/13.webp)

## Tilleggsfunksjoner

I tillegg til det åpenbare kjøpet og salget av Bitcoin, har RoboSats noen andre funksjoner du bør vite om.
Robotgarasjen
Vil du ha flere handler gående samtidig, men ønsker ikke å dele samme identitet på tvers av dem? Ikke noe problem! Klikk på Robot-fanen, generer en ekstra Robot og opprett eller ta din neste ordre.
![bilde](assets/14.webp)

### Opprette Ordre

I tillegg til å ta imot andres tilbud, kan du opprette ditt eget og vente på at en annen Robot kommer til deg.

- Åpne Opprett-siden.
- Definer om ordren din er for å kjøpe eller selge Bitcoin.
- Angi mengden og valutaen du ønsker å Kjøpe/Selge med.
- Angi betalingsmetode(r) du er villig til å bruke.
- Angi 'Premium over Market' % du er villig til å akseptere. Merk at dette kan være en negativ figur for å by til en rabatt sammenlignet med gjeldende markedspris.
- Klikk Opprett Ordre.
- Betal Lightning-fakturaen for å låse din Maker Bond.
- Din ordre er nå aktiv. Sett deg tilbake og vent på at noen aksepterer den.

![bilde](assets/15.webp)

### On-chain Utbetalinger

RoboSats er fokusert på Lightning, men kjøpere har muligheten til å motta sine sats til en on-chain Bitcoin-adresse. Kjøpere kan velge dette alternativet etter å ha låst opp sin bond. Etter å ha valgt on-chain, vil kjøperen se en oversikt over gebyrene. De ekstra gebyrene for denne tjenesten inkluderer:

- Et byttegebyr samlet inn av RoboSats - Dette gebyret er dynamisk og endres avhengig av hvor opptatt Bitcoin-nettverket er.
- Et gruvegebyr for utbetalingstransaksjonen - Dette kan konfigureres av kjøperen.

![bilde](assets/16.webp)

### P2P Bytter

RoboSats lar brukere bytte sats inn i eller ut av deres Lightning Wallet. Klikk ganske enkelt på bytteknappen øverst på tilbudssiden for å se de gjeldende byttetilbudene.

Som kjøper av et 'Swap In'-tilbud, sender du on-chain Bitcoin til peeren og mottar sats tilbake, minus de annonserte gebyrene og/eller premiene, til din Lightning Wallet. Som kjøper av et 'Swap Out'-tilbud, sender du sats via Lightning og mottar Bitcoin, minus eventuelle gebyrer og/eller premier, til din on-chain adresse. Brukere av Samourai eller Sparrow Wallet kan også utnytte Stowaway-funksjonen for å fullføre et bytte.

RoboSats byttetilbud kan også inkludere peggede alternativer til Bitcoin som inkluderer RBTC, LBTC og WBTC. Du bør være ekstremt forsiktig hvis du samhandler med disse tokenene da de alle kommer med ulike kompromisser. Pegged Bitcoin er ikke Bitcoin!

![bilde](assets/17.webp)

### Kjør din egen RoboSats-klient

Umbrel, Citadel og Start9 nodekjørere kan installere sin egen RoboSats-klient direkte på sin node. Fordelene med å gjøre dette er oppført som:

- Dramatisk raskere lastetider.
- Tryggere: du kontrollerer hvilken RoboSats-klientapp du kjører.
- Tilgang til RoboSats trygt fra hvilken som helst nettleser / enhet. Ingen behov for å bruke TOR hvis du er på ditt lokale nettverk eller bruker VPN: din node-backend håndterer torifiseringen som trengs for anonymisering.
- Lar kontroll over hvilken P2P-markedskoordinator du kobler til (standard til robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion)

![bilde](assets/18.webp)

## FAQ

### Kan jeg bli svindlet?
Som kjøper, hvis du har sendt fiat-valutaen som kreves for din del av handelen, men selgeren ikke frigjør satsene til deg, kan du åpne en tvist. Hvis du under denne tvisteprosessen kan bevise for RoboSats-arbitratorene at du faktisk sendte fiat, vil selgerens deponerte midler og deres handelsobligasjon bli frigitt til deg. Hvordan avbryter jeg en handel?

Du kan avbryte en handel etter å ha postet din obligasjon ved å klikke på "Collaborative Cancel"-knappen inne i handelsmenyen. Hvis din handelspartner er villig til å avbryte, vil du ikke pådra deg noen gebyrer. Men hvis din handelspartner ønsker å fullføre handelen og du avbryter uansett, vil du miste din handelsobligasjon.

### Fungerer RoboSats med ‘X’ betalingsmetode?

Det er ingen restriksjoner på betalingsmetoder i RoboSats. Hvis du ikke ser noen tilbud med din ønskede metode, lag ditt eget tilbud ved å bruke den!

![bilde](assets/19.webp)

### Hva lærer RoboSats om meg når jeg bruker det?

Så lenge du bruker RoboSats via Tor eller Android-appen, ingenting i det hele tatt! Lær mer her.

- Tor beskytter ditt nettverks personvern.
- PGP-kryptering holder din handelschat privat.
- Ingen kontoer betyr en Robot per handel. Dette betyr at RoboSats ikke kan korrelere flere handler til en enkelt enhet.

Det er imidlertid noen forbehold! Lightning er ganske privat som sender, men ikke som mottaker. Hvis du mottar til din egen Lightning-node, deles node-ID-en din i fakturaene dine. Denne node-ID-en gir alle med kunnskap om den et utgangspunkt for å prøve å koble din on-chain-aktivitet. Dette er også sant hvis en bruker velger å motta sin handel via en on-chain-utbetaling.

For å redusere dette, kan brukere velge å bruke en løsning som en Proxy Wallet for Lightning eller Coinjoin for on-chain.

### Føderasjon

Akkurat nå er det en enkelt RoboSats-koordinator som drives av RoboSats-utviklerteamet. I Bitcoin gjør enhver form for sentralisering det til et lettere mål for regjeringer eller regulatorer som kanskje ikke ser med blide øyne på en spesifikk tjeneste.

Med RoboSats som et Open Source-prosjekt, kan hvem som helst ta koden og begynne å kjøre sin egen koordinator. Selv om dette i noen grad desentraliserer risikoen bort fra et enkelt mål, fragmenterer det også et allerede tynt likviditetsmarked.

RoboSats-teamet er klar over dette og har startet arbeidet med en føderert modell. Som sluttbruker bør dette ikke endre handelsflyten demonstrert ovenfor mye, men det vil være ekstra visninger eller skjermer for deg å legge til eller fjerne forskjellige koordinatorer som oppstår.

SLUTT på veiledningen
https://bitcoiner.guide/robosats/