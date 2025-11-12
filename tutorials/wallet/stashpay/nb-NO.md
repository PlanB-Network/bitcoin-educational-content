---
name: StashPay
description: Den minimalistiske Bitcoin Wallet for alle
---

![cover](assets/cover.webp)



Brukeropplevelsen er en nøkkelfaktor når det gjelder å ta i bruk Bitcoin-løsninger over hele verden. Mange lommebøker og Exchange-plattformer prioriterer en smidig, enkel og teknisk ubesværet opplevelse. I så måte skiller StashPay seg ut med sin minimalistiske tilnærming, samtidig som den demonstrerer kraften i Lightning Network.



I denne veiledningen tar vi en titt på denne porteføljen for å finne ut hvordan den fungerer og hvordan den er ideell for små bedrifter eller solopreneurs.



## Kom i gang med StashPay



StashPay er en Lightning Wallet med selvforvaring som først og fremst er anerkjent for sin minimalistiske, brukersentrerte brukeropplevelse.  Med denne Wallet trenger du ingen teknisk kunnskap for å motta og sende dine første satoshier.



StashPay er et åpen kildekode-prosjekt utviklet i React Native og har som mål å løse problemet med høye transaksjonsgebyrer selv med transaksjoner på Bitcoin-protokollens hovedkjede. Den er tilgjengelig som en mobilapp på Android- og iOS-plattformer via nedlastingslenker på [nettsted] (https://stashpay.me/).



![introduce](assets/fr/01.webp)



Det er viktig å laste ned Android-applikasjonen fra nettstedet, siden den ikke er tilgjengelig i Google Play Store.


Når nedlastingen er fullført, må du gi de nødvendige tillatelsene slik at du kan installere applikasjonen på Android-telefonen din.



Når applikasjonen er installert, vil StashPay opprette en første Bitcoin Wallet for deg første gang du åpner den. Vi anbefaler at du tar en sikkerhetskopi av denne Wallet før du foretar en transaksjon. Nedenfor finner du alle retningslinjene våre for å sikre at gjenopprettingsfrasene dine er sikkerhetskopiert på riktig måte.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Åpne StashPay-innstillingene ved å klikke på ikonet "Innstillinger", og klikk deretter på alternativet **Opprett sikkerhetskopi**. Godkjenn deretter visningen av gjenopprettingsfraser. Ikke kopier gjenopprettingsfraser til telefonens utklippstavle, da de kan være tilgjengelige for andre falske applikasjoner som er installert på mobilen din.



![backup](assets/fr/02.webp)



Du kan også hente en Bitcoin Wallet du allerede bruker, ved å klikke på alternativet **Hent Wallet** og sette inn de 12 eller 24 gjenopprettingsordene.



### Motta dine første satoshier på StashPay



På startskjermen klikker du på **Mottak**-knappen og angir et beløp som er større enn beløpet som er angitt i rødt. I vårt tilfelle kan vi ikke motta mindre enn 0,11 USD med StashPay Wallet.



![receive](assets/fr/03.webp)



Når du har definert beløpet, kan du klikke på knappen **Opprett Invoice**, og deretter skanne eller kopiere Invoice for å sende den til satoshis-avsenderen din.



![receive_sats](assets/fr/04.webp)



Du kan se transaksjonshistorikken din ved å klikke på "klokke"-ikonet på startsiden.



![network_fee](assets/fr/05.webp)



Du har sikkert lagt merke til at du må betale en nettverksavgift for å motta satoshier. Disse avgiftene vil bli trukket fra satoshiene du er i ferd med å motta. Dette er fordi StashPay er en Wallet basert på Breez Development Kit. For å motta satoshis med Lightning node-free-implementeringen av kitet, vil Breez belaste kunden (StashPay i vårt tilfelle) med 0,25 % + 40 satoshis. Finn ut mer i vår Misty Breez-veiledning.



https://planb.academy/tutorials/wallet/mobile/misty-breez-738ced2a-0764-4d7f-a150-ec0ce84a9d25

### Send bitcoins med StashPay



Å sende bitcoins med StashPay er ganske intuitivt takket være den minimalistiske Interface. På startskjermen klikker du på **Send**-knappen. Skann QR-koden eller lim inn Address som du ønsker å sende satoshier til. StashPay vil automatisk oppdage Bitcoin-protokollkjeden som du ønsker å sende bitcoins til.



![send](assets/fr/06.webp)



Siden StashPay er en Wallet basert på Breez Development Kit, har den en interessant fordel: å sende bitcoins på hovedkjeden til en lav kostnad. Breez bruker Boltz-tjenesten til å utføre transaksjoner mellom de ulike kjedene i Bitcoin-protokollen, slik at kunder som implementerer Development Kit kan dra nytte av denne tjenesten direkte i applikasjonen sin.



https://planb.academy/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

Breez SDK pålegger imidlertid et minimumsbeløp som du kan sende bitcoins til en Address på hovedkjeden.



![onchain](assets/fr/07.webp)



Du kan også sende bitcoins ved å bruke mottakerens Lightning Address. Se gjennom transaksjonsdetaljene, og bekreft deretter ved å klikke på **Send**-knappen.



![confirm](assets/fr/08.webp)



## Flere konfigurasjoner



I StashPay-innstillingene kan du justere konfigurasjonene for å tilpasse bruken av Wallet.



Med StashPay kan du Exchange satoshier basert på den lokale valutaen du ønsker. Klikk på **Valutaer**-alternativet, og søk deretter etter valutaen din i listen over +113 valutaer som StashPay tilbyr.



![currencies](assets/fr/09.webp)



I menyen **Mottaksalternativer** finner du alle innstillingene for mottak av bitcoins med StashPay. Ved å velge **Velg Lightning eller Onchain** kan du for eksempel aktivere Wallet for å motta bitcoins fra hovedkjeden.



![receive-onchain](assets/fr/10.webp)



Med alternativet **Scan OnChain-adresser** kan du oppdatere Wallet-saldoen ved å sjekke alle UTXO-er (bitcoins du ikke har brukt ennå) som er knyttet til de ulike adressene dine.



![rescan](assets/fr/11.webp)



Menyen **Eksporter logg** viser alle Breez- og Boltz-infrastrukturhandlinger som gjelder transaksjoner og atomutvekslinger mellom de ulike Bitcoin-protokollkjedene.



![export](assets/fr/12.webp)



Du har nettopp blitt kjent med StashPays minimalistiske Bitcoin Wallet. Hvis du synes denne veiledningen var nyttig, anbefaler vi vår veiledning om hvordan du kommer i gang med Bitcoin og tjener dine første bitcoins.



https://planb.academy/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f