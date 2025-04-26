---
name: Payjoin
description: Hva er en Payjoin på Bitcoin?
---
![Payjoin miniatyrbilde - steganografi](assets/cover.webp)

***OBS:** Etter arrestasjonen av grunnleggerne av Samourai Wallet og beslagleggelsen av deres servere den 24. april, fungerer Payjoins Stowaway på Samourai Wallet kun ved manuell utveksling av PSBT mellom de berørte partene, forutsatt at begge brukerne er koblet til sitt eget Dojo. Når det gjelder Sparrow, fungerer Payjoins via BIP78 fortsatt. Det er imidlertid mulig at disse verktøyene vil bli relansert i de kommende ukene. I mellomtiden kan du fortsatt lese denne artikkelen for å forstå den teoretiske funksjonen av payjoins.*

_Vi følger nøye med på utviklingen av denne saken samt utviklingen angående de tilknyttede verktøyene. Vær trygg på at vi vil oppdatere denne opplæringen etter hvert som ny informasjon blir tilgjengelig._

_Denne opplæringen er gitt kun til utdannings- og informasjonsformål. Vi støtter eller oppmuntrer ikke bruk av disse verktøyene til kriminelle formål. Det er brukerens ansvar å overholde lovene i sin jurisdiksjon._

---
## Forståelse av Payjoin-transaksjoner på Bitcoin

Payjoin er en spesifikk struktur av Bitcoin-transaksjon som forbedrer brukerens personvern under en betaling ved å samarbeide med betalingsmottakeren.

I 2015 nevnte [LaurentMT](https://twitter.com/LaurentMT) først denne metoden som "steganografiske transaksjoner" i et dokument tilgjengelig [her](https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt). Denne teknikken ble senere adoptert av Samourai Wallet, som ble den første klienten til å implementere den med Stowaway-verktøyet i 2018. Konseptet med Payjoin finnes også i [BIP79](https://github.com/bitcoin/bips/blob/master/bip-0079.mediawiki) og [BIP78](https://github.com/bitcoin/bips/blob/master/bip-0078.mediawiki). Flere termer brukes for å referere til Payjoin:
- Payjoin
- Stowaway
- P2EP (Pay-to-End-Point)
- Steganografisk transaksjon

Det unike med Payjoin ligger i dens evne til å generere en transaksjon som ved første øyekast ser vanlig ut, men som faktisk er en mini Coinjoin mellom to parter. For å oppnå dette involverer transaksjonsstrukturen betalingsmottakeren sammen med den faktiske avsenderen i inngangene. Mottakeren inkluderer en betaling til seg selv midt i transaksjonen, noe som gjør det mulig for dem å bli betalt.

La oss ta et konkret eksempel: hvis du kjøper en baguette for `4000 sats` ved å bruke en UTXO på `10,000 sats` og velger en Payjoin, vil bakeren din legge til en UTXO på `15,000 sats` som tilhører dem som en inngang, som de vil motta i sin helhet som en utgang, i tillegg til dine `4000 sats`:
![Payjoin transaksjonsdiagram](assets/en/1.webp)
I dette eksemplet introduserer bakeren `15,000 sats` som en inngang og kommer ut med `19,000 sats`, med en forskjell på nøyaktig `4000 sats`, som er prisen på baguetten. På din side, går du inn med `10,000 sats` og ender opp med `6,000 sats` som en utgang, som representerer en balanse på `-4000 sats`, som er prisen på baguetten. For å forenkle eksemplet, har jeg med vilje utelatt gruvegebyrer i denne transaksjonen.
## Hva er formålet med en Payjoin-transaksjon?

En Payjoin-transaksjon tjener to mål som lar brukere forbedre personvernet til betalingen sin.
For det første, Payjoin har som mål å villede en ekstern observatør ved å skape en avledning i kjedeanalyse. Dette gjøres mulig gjennom Common Input Ownership Heuristic (CIOH). Vanligvis, når en transaksjon på blokkjeden har flere innganger, antas det at alle disse inngangene sannsynligvis tilhører samme enhet eller bruker. Dermed, når en analytiker undersøker en Payjoin-transaksjon, blir de ledet til å tro at alle inngangene kommer fra samme person. Imidlertid er denne oppfatningen feil fordi betalingsmottakeren også bidrar med innganger sammen med den faktiske betaleren. Derfor blir kjedeanalysen omdirigert mot en tolkning som viser seg å være falsk.

Videre tillater Payjoin også å bedra en ekstern observatør om det faktiske beløpet av betalingen som har blitt gjort. Ved å undersøke transaksjonsstrukturen, kan analytikeren tro at betalingen tilsvarer beløpet til en av utgangene. Men i virkeligheten tilsvarer ikke betalingsbeløpet noen av utgangene. Det er faktisk forskjellen mellom mottakerens utgangs-UTXO og mottakerens inngangs-UTXO. I denne forstand faller Payjoin-transaksjonen innenfor domenet av steganografi. Det tillater å skjule det faktiske beløpet av en transaksjon innenfor en falsk transaksjon som fungerer som en avledning.

> Steganografi er en teknikk for å skjule informasjon innenfor andre data eller objekter på en slik måte at tilstedeværelsen av den skjulte informasjonen ikke er merkbar. For eksempel kan en hemmelig melding skjules inne i et punkt i en tekst som ikke har noe med det å gjøre, noe som gjør det uoppdagelig for det blotte øye (dette er teknikken med mikropunkt). I motsetning til kryptering, som gjør informasjon uforståelig uten dekrypteringsnøkkelen, endrer ikke steganografi informasjonen. Den forblir vist åpenlyst. Målet er heller å skjule eksistensen av den hemmelige meldingen, mens kryptering tydelig avslører tilstedeværelsen av skjult informasjon, selv om den er utilgjengelig uten nøkkelen.

La oss gå tilbake til vårt eksempel på en Payjoin-transaksjon for betaling av en baguette.
![Payjoin-transaksjonsskjema fra utsiden](assets/en/2.webp)
Ved å se denne transaksjonen på blokkjeden, vil en ekstern observatør som følger de vanlige heuristikkene for kjedeanalyse tolke det som følger: "*Alice slo sammen 2 UTXOs som innganger av transaksjonen for å betale `19,000 sats` til Bob*."
![Feilaktig tolkning av Payjoin-transaksjon fra utsiden](assets/en/3.webp)
Denne tolkningen er åpenbart feil fordi, som du allerede vet, tilhører ikke de to inngangs-UTXOene samme person. Videre er den faktiske verdien av betalingen ikke `19,000 sats`, men heller `4,000 sats`. Analysen av den eksterne observatøren er dermed rettet mot en feilaktig konklusjon, noe som sikrer bevaringen av interessentenes konfidensialitet.![payjoin-transaksjonsdiagram](assets/en/1.webp)
Hvis du ønsker å analysere en ekte Payjoin-transaksjon, her er en som jeg utførte på testnet: [8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c](https://mempool.space/fr/testnet/tx/8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c)  
[**-> Oppdag vår veiledning om hvordan du gjør en Payjoin med Samourai Wallet**](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab)  

[**-> Oppdag vår veiledning om hvordan du gjør en Payjoin med Sparrow Wallet**](https://planb.network/tutorials/privacy/on-chain/payjoin-sparrow-wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62)


**Eksterne ressurser:**
- https://docs.samourai.io/en/spend-tools#stowaway;
- https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt;
- https://github.com/bitcoin/bips/blob/master/bip-0078.mediawiki.