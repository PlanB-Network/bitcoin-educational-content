---
name: Stonewall x2
description: Forstå og bruke Stonewall x2 transaksjoner
---
![cover stonewall x2](assets/cover.webp)

***ADVARSEL:** Etter arrestasjonen av grunnleggerne av Samourai Wallet og beslagleggelsen av deres servere den 24. april, fungerer Stonewallx2-transaksjoner kun ved manuelt å utveksle PSBT-er mellom de berørte partene, forutsatt at begge brukerne er koblet til sin egen Dojo. Det er imidlertid mulig at disse verktøyene kan bli relansert i de kommende ukene. I mellomtiden kan du fortsatt konsultere denne artikkelen for å forstå den teoretiske funksjonen av Stonewallx2 og lære hvordan du gjør dem manuelt.*

_Om du vurderer å utføre en Stonewallx2 manuelt, er prosedyren veldig lik den som er beskrevet i denne opplæringen. Hovedforskjellen ligger i valget av typen Stonewallx2-transaksjon: i stedet for å velge `Online`, klikk på `In Person / Manual`. Deretter må du manuelt utveksle PSBT-ene for å konstruere Stonewallx2-transaksjonen. Hvis du er fysisk nær din samarbeidspartner, kan du skanne QR-kodene etter hverandre. Hvis du er på avstand, kan JSON-filer utveksles via en sikker kommunikasjonskanal. Resten av opplæringen forblir uendret._

_Vi følger nøye med på utviklingen av denne saken samt utviklingen angående de tilknyttede verktøyene. Vær trygg på at vi vil oppdatere denne opplæringen etter hvert som ny informasjon blir tilgjengelig._

_Denne opplæringen er kun gitt for utdannings- og informasjonsformål. Vi støtter eller oppmuntrer ikke bruk av disse verktøyene til kriminelle formål. Det er brukerens ansvar å overholde lovene i sin jurisdiksjon._

---

> *Gjør hvert utlegg til en coinjoin.*

## Hva er en Stonewall x2 transaksjon?

Stonewall x2 er en spesifikk form for Bitcoin-transaksjon som har som mål å øke brukerens personvern under en betaling, ved å samarbeide med en tredjepart som ikke er involvert i selve utlegget. Denne metoden simulerer en mini-coinjoin mellom to deltakere, samtidig som den gjør en betaling til en tredjepart. Stonewall x2-transaksjoner er tilgjengelige både på Samourai Wallet-applikasjonen og Sparrow Wallet-programvaren. Begge er interoperable.

Dens funksjon er relativt enkel: vi bruker en UTXO i vår besittelse for å gjøre betalingen og søker assistanse fra en tredjepart som også bidrar med en UTXO av deres egen. Transaksjonen resulterer i fire utdata: to av dem med like beløp, en bestemt for mottakerens adresse for betalingen, den andre til en adresse som tilhører samarbeidspartneren. En tredje UTXO returneres til en annen adresse tilhørende samarbeidspartneren, som lar dem hente det opprinnelige beløpet (en nøytral handling for dem, minus gruvegebyrer), og en endelig UTXO returneres til en adresse som tilhører oss, som utgjør vekselen fra betalingen.

Dermed er tre forskjellige roller definert i Stonewall x2-transaksjoner:
- Avsenderen, som gjør selve betalingen;
- Samarbeidspartneren, som bidrar med bitcoins for å forbedre den generelle anonymiteten til transaksjonen, samtidig som de fullstendig gjenoppretter sine midler til slutt (en nøytral handling for dem, minus gruvegebyrer);
- Mottakeren, som kanskje ikke er klar over den spesifikke naturen til transaksjonen og rett og slett forventer en betaling fra avsenderen.

La oss ta et eksempel for å bedre forstå. Alice er på bakeriet for å kjøpe sin baguette, som koster `4,000 sats`. Hun ønsker å betale i bitcoins samtidig som hun opprettholder et visst nivå av personvern for betalingen. Hun ber derfor sin venn Bob om å assistere henne i denne prosessen.
![schema stonewall x2](assets/en/1.webp)
Ved å analysere denne transaksjonen kan vi se at bakeren faktisk mottok `4,000 sats` som betaling for baguetten. Alice brukte `10,000 sats` som inngang og mottok `6,000 sats` som utgang, noe som resulterte i en netto saldo på `-4,000 sats`, som tilsvarer prisen på baguetten. Når det gjelder Bob, ga han `15,000 sats` som inngang og mottok to utganger: en på `4,000 sats` og den andre på `11,000 sats`, noe som resulterte i en saldo på `0`. I dette eksemplet har jeg med vilje utelatt gruvegebyrer for å lette forståelsen. I virkeligheten deles transaksjonsgebyrer likt mellom betalingssenderen og samarbeidspartneren.

## Hva er forskjellen mellom Stonewall og Stonewall x2?

En StonewallX2-transaksjon fungerer nøyaktig som en Stonewall-transaksjon, bortsett fra at den førstnevnte er samarbeidende mens den sistnevnte ikke er det. Som vi har sett, involverer en Stonewall x2-transaksjon deltakelsen av en tredjepart, som er ekstern til betalingen, og som vil tilby sine bitcoins for å forbedre transaksjonsprivatlivet. I en typisk Stonewall-transaksjon, tas rollen som samarbeidspartner av senderen.

La oss gjenbesøke vårt eksempel med Alice på bakeriet. Hvis hun ikke kunne finne noen som Bob til å følge henne i hennes utgift, kunne hun ha gjort en Stonewall-transaksjon alene. Dermed ville de to inngangs-UTXOene vært hennes, og hun ville ha mottatt 3 ved utgangen.
![transaksjon stonewall](assets/en/2.webp)

Fra et eksternt synspunkt, ville transaksjonsmønsteret ha forblitt det samme.
![Stonewall eller Stonewall x2?](assets/en/5.webp)
Derfor bør logikken være som følger når man bruker et Samourai-utgiftsverktøy:
- Hvis handelsmannen ikke støtter Payjoin Stowaway, kan en samarbeidstransaksjon gjøres med en annen person ekstern til betalingen ved å bruke Stonewall x2.
- Hvis ingen blir funnet for å gjøre en Stonewall x2-transaksjon, kan en Stonewall-transaksjon gjøres alene, som etterligner oppførselen til en Stonewall x2-transaksjon.
- Til slutt ville det siste alternativet være å gjøre en transaksjon med JoinBot, en server vedlikeholdt av Samourai, som kan, på forespørsel, opptre som samarbeidspartneren i en Stonewall x2-transaksjon.

Hvis du ønsker å finne en samarbeidspartner som er villig til å assistere deg i en Stonewall X2-transaksjon, kan du også besøke denne Telegram-gruppen (uoffisiell) vedlikeholdt av Samourai-brukere for å koble sendere og samarbeidspartnere: [Make Every Spend a Coinjoin](https://t.me/EverySpendACoinjoin).

[**-> Lær mer om Stonewall-transaksjoner**](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)

## Hva er formålet med en Stonewall x2-transaksjon?

Stonewall x2-strukturen legger til en betydelig mengde entropi til transaksjonen og forvirrer kjedeanalyse. Utenfra kan en slik transaksjon tolkes som en liten Coinjoin mellom to individer. Men i virkeligheten er det en betaling. Denne metoden genererer usikkerheter i kjedeanalyse, og fører til og med til falske spor.

La oss gå tilbake til eksemplet med Alice, Bob og Bakeren. Transaksjonen på blokkjeden ville se slik ut:
![stonewall x2 offentlig](assets/en/3.webp)
En ekstern observatør som stoler på vanlige heuristikker for kjedeanalyse, kan feilaktig konkludere med at "Alice og Bob utførte en liten coinjoin, med én UTXO hver som inngang og to UTXOer hver som utgang."![misforståelse stonewall x2](assets/en/4.webp)Denne tolkningen er feil fordi, som du vet, ble en UTXO sendt til Baker, Alice har bare ett vekselutgang, og Bob har to.
![transaksjon stonewall x2](assets/en/1.webp)
Selv om den eksterne observatøren klarer å identifisere mønsteret til Stonewall x2-transaksjonen, vil de ikke ha all informasjonen. De vil ikke kunne bestemme hvilken av de to UTXOene med samme beløp som tilsvarer betalingen. Videre vil de ikke kunne vite om det er Alice eller Bob som gjorde betalingen. Til slutt vil de ikke kunne bestemme om de to inngangs-UTXOene kommer fra to forskjellige personer eller om de tilhører en enkelt person som slo dem sammen. Dette siste punktet skyldes det faktum at klassiske Stonewall-transaksjoner, som vi diskuterte ovenfor, følger nøyaktig samme mønster som Stonewall x2-transaksjoner. Fra utsiden og uten ytterligere informasjon om konteksten, er det umulig å skille en Stonewall-transaksjon fra en Stonewall x2-transaksjon. Imidlertid er ikke de førstnevnte samarbeidstransaksjoner, mens de sistnevnte er det. Dette legger enda flere tvil om denne utgiften.
![Stonewall eller Stonewall x2 ?](assets/en/5.webp)

## Hvordan etablere en forbindelse mellom Paynyms for å kunne samarbeide via Soroban?

Som med andre samarbeidstransaksjoner på Samourai (*Cahoots*), involverer utførelsen av en Stonewall x2 utvekslingen av delvis signerte transaksjoner mellom avsenderen og samarbeidspartneren. Denne utvekslingen kan gjøres manuelt, i tilfelle du fysisk er sammen med din samarbeidspartner, eller automatisk gjennom Soroban kommunikasjonsprotokollen.

Hvis du velger det andre alternativet, må du etablere en forbindelse mellom Paynyms før du kan utføre en Stonewall x2. For å gjøre dette, må din Paynym "følge" din samarbeidspartners Paynym, og omvendt.

**Å få tilgang til samarbeidspartnerens Paynym:**

For å starte, er det nødvendig å skaffe betalingskoden til din samarbeidspartners Paynym. I Samourai Wallet-applikasjonen, må din samarbeidspartner trykke på ikonet til deres Paynym (den lille roboten) som er plassert øverst til venstre på skjermen, deretter klikke på deres Paynym-kallenavn, som starter med `+...`. For eksempel er mitt `+namelessmode0aF`.

![samourai paynym](assets/notext/6.webp)
Hvis din samarbeidspartner bruker Sparrow Wallet, bør de klikke på 'Verktøy'-fanen, deretter på 'Vis PayNym'.![paynym sparrow](assets/notext/7.webp)
**Å følge din samarbeidspartners PayNym fra Samourai Wallet:**

Hvis du bruker Samourai Wallet, start applikasjonen og få tilgang til 'PayNyms'-menyen på samme måte. Hvis dette er første gang du bruker din PayNym, må du skaffe identifikatoren din.

![forespørsel paynym samourai](assets/notext/8.webp)

Deretter klikker du på det blå '+' nederst til høyre på skjermen.
![legg til samarbeidspartner paynym](assets/notext/9.webp)
Du kan deretter lime inn din samarbeidspartners betalingskode ved å velge 'LIM INN BETALINGSKODE', eller åpne kameraet for å skanne deres QR-kode ved å trykke 'SKANN QR-KODE'.
![lim inn paynym-identifikator](assets/notext/10.webp)
Klikk på 'FOLLOW'-knappen.
![følg paynym](assets/notext/11.webp)
Bekreft ved å klikke 'YES'.
![bekreft følg paynym](assets/notext/12.webp)
Programvaren vil deretter tilby deg en 'CONNECT'-knapp. Det er ikke nødvendig å klikke på denne knappen for vår opplæring. Dette trinnet er kun nødvendig hvis du planlegger å gjøre betalinger til den andre PayNym som en del av BIP47, noe som er urelatert til vår opplæring.
![koble til paynym](assets/notext/13.webp)
Når din PayNym følger din samarbeidspartners PayNym, gjenta denne prosessen i motsatt retning slik at din samarbeidspartner også kan følge deg. Du kan deretter utføre en Stonewall x2-transaksjon.

**Følge din samarbeidspartners PayNym fra Sparrow Wallet:**

Hvis du bruker Sparrow Wallet, åpne lommeboken din og få tilgang til 'Show PayNym'-menyen. Hvis du bruker din PayNym for første gang, må du skaffe en identifikator ved å klikke på 'Retrieve PayNym'.
![forespør paynym sparrow](assets/notext/14.webp)
Skriv deretter inn din samarbeidspartners PayNym-identifikator (enten deres kallenavn '+...' eller deres betalingskode 'PM...') i 'Find Contact'-boksen, og klikk på 'Add Contact'-knappen.
![legg til kontakt paynym](assets/notext/15.webp)
Programvaren vil deretter tilby deg en 'Link Contact'-knapp. Det er ikke nødvendig å klikke på denne knappen for vår opplæring. Dette trinnet er kun nødvendig hvis du planlegger å gjøre betalinger til den angitte PayNym som en del av BIP47, noe som er urelatert til vår opplæring.

Når din PayNym følger din samarbeidspartners PayNym, gjenta denne prosessen i motsatt retning slik at din samarbeidspartner også kan følge deg. Du kan deretter utføre en Stonewall x2-transaksjon.
## Hvordan utføre en Stonewall x2-transaksjon på Samourai Wallet?

Hvis du har fullført de foregående trinnene med å koble Paynyms, er du endelig klar til å utføre Stonewall x2-transaksjonen! For å gjøre dette, følg vår videoopplæring på Samourai Wallet:
![Stonewall x2 Tutorial - Samourai Wallet](https://youtu.be/89oYE1Hw3Fk?si=QTqUZ6IypiR6PPMr)

## Hvordan utføre en Stonewall x2-transaksjon på Sparrow Wallet?

Hvis du har fullført de foregående trinnene med å koble Paynyms, er du endelig klar til å utføre Stonewall x2-transaksjonen! For å gjøre dette, følg vår videoopplæring på Sparrow Wallet:
![Stonewall x2 Tutorial - Sparrow Wallet](https://youtu.be/mO3Xpp34Hhk?si=bfYiTl0Gxjs9sNQq)

**Eksterne ressurser:**
- https://sparrowwallet.com/docs/spending-privately.html;
- https://docs.samourai.io/en/spend-tools#stonewallx2.