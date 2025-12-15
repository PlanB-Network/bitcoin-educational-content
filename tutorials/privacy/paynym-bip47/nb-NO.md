---
name: BIP47 - PayNym
description: Bruk en gjenbrukbar betalingskode på Ashigaru
---
![cover](assets/cover.webp)



Den verste personvernfeilen du kan gjøre på Bitcoin, er å gjenbruke adresser. Hver gang den samme adressen mottar flere betalinger, kobles disse transaksjonene sammen og gir verden et kart over transaksjonene dine. Det anbefales derfor på det sterkeste at du alltid bruker en unik generate-adresse for hver kvittering. Men for noen Bitcoin-applikasjoner er dette ikke en enkel sak.



BIP47, som ble foreslått av Justus Ranvier i 2015, gir et elegant svar på dette problemet. Den introduserer konseptet med en **gjenbrukbar betalingskode**: en unik identifikator som gjør det mulig å motta et tilnærmet ubegrenset antall bitcoin-betalinger i kjeden, uten å måtte gjenbruke en adresse. Takket være en kryptografisk mekanisme basert på en ECDH-utveksling (*Diffie-Hellman på elliptiske kurver*) resulterer hver betaling til samme kode i en tom adresse, som er spesifikk for forholdet mellom avsender og mottaker.



![Image](assets/fr/01.webp)



Dette BIP47-prinsippet er særlig implementert i **PayNym**, systemet som opprinnelig ble utviklet av Samourai Wallet og nå er overtatt av Ashigaru. I denne veiledningen skal vi se på hvordan du aktiverer PayNym, utveksler betalingskoder med en korrespondent og gjennomfører transaksjoner uten å gjenbruke en adresse.



Jeg vil ikke gå inn på den detaljerte bruken av BIP47 her. Hvis du ønsker å gå dypere inn i emnet, kan du lese kapittel 6.6 i BTC 204-kurset mitt.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Forutsetninger



For å følge denne veiledningen trenger du bare en wallet på Ashigaru-appen. Hvis du ikke vet hvordan du laster ned, verifiserer, installerer applikasjonen eller oppretter en wallet, anbefaler jeg at du leser denne veiledningen først:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

## Be om PayNym



Det første trinnet er å gjøre krav på PayNym. Denne operasjonen trenger bare å utføres én gang per wallet. Den knytter BIP47-betalingskoden fra seed (`PM...`) til en unik identifikator som er spesifikk for PayNym-implementeringen. Denne kortere, mer lesbare identifikatoren kan deretter overføres til korrespondentene dine for å forenkle utvekslingen, uten at du trenger å dele den lange, fullstendige BIP47-koden.



Dette gjør du ved å klikke på PayNym-bildet ditt øverst til venstre i grensesnittet, og deretter på betalingskoden `PM...`.



![Image](assets/fr/02.webp)



Klikk deretter på de tre små prikkene øverst i høyre hjørne, og velg `Claim PayNym`.



![Image](assets/fr/03.webp)



Bekreft ved å klikke på knappen `CLAIM YOUR PAYNYM`.



![Image](assets/fr/04.webp)



Oppdater siden: PayNym-ID-en din vises nå under bildet ditt, rett over BIP47-betalingskoden din.



![Image](assets/fr/05.webp)



Ditt PayNym er nå aktivt og klart til å brukes til dine første BIP47-transaksjoner.



## Koble deg til en kontakt



Det finnes to typer tilkoblinger mellom PayNym: **følge** og **koble**. `follow`-operasjonen er helt gratis. Den etablerer en kobling mellom to PayNym gjennom Soroban, en Tor-basert kryptert kommunikasjonsprotokoll som er utviklet av Samourai-teamet og tatt i bruk av Ashigaru. Denne koblingen gjør det mulig for to brukere som følger hverandre å utveksle informasjon privat, spesielt for å koordinere samarbeidstransaksjoner som Stowaway eller StonewallX2, som vi skal se på i en annen veiledning. Dette trinnet er spesifikt for PayNym og er ikke en del av BIP47-protokollen.



![Image](assets/fr/06.webp)



Tilkoblingsoperasjonen (`connect`) krever derimot en on-chain-transaksjon. Den består i å utføre en varslingstransaksjon som definert i BIP47. Denne Bitcoin-transaksjonen inneholder metadata i en `OP_RETURN`-utgang, som etablerer en kryptert kommunikasjonskanal mellom betaleren og mottakeren. Fra denne kanalen vil betaleren kunne generate unike mottakeradresser for hver betaling, og mottakeren vil bli varslet om disse betalingene, og vil kunne generate de private nøklene som er knyttet til adressene for å bruke disse midlene senere.



Denne varslingstransaksjonen har en kostnad: avgiften mining og 546 sats som sendes til mottakerens varslingsadresse for å signalisere tilkoblingen. Når forbindelsen er opprettet, kan et nesten uendelig antall betalinger utføres via BIP47.



I et nøtteskall:




- follow": gratis, oppretter kryptert kommunikasjon via Soroban, nyttig for Ashigarus samarbeidsverktøy;
- `Connect`: avgiftsbelagt, utfører BIP47-varslingstransaksjonen for å aktivere kanalen mellom betaler og mottaker.



For å samhandle med et PayNym må du først *følge* det. Dette er det første trinnet før du oppretter en BIP47-tilkobling. La oss si at du ønsker å sende tilbakevendende betalinger til PayNym `+instinctiveoffer10`.



Gå til PayNym-siden din på Ashigaru, og klikk deretter på "+"-knappen nederst til høyre i grensesnittet.



![Image](assets/fr/07.webp)



Deretter kan du enten lime inn mottakerens fullstendige betalingskode, eller skanne QR-koden deres.



![Image](assets/fr/08.webp)



Hvis du bare har PayNym-ID-en hans, kan du gå til [Paynym.rs] (https://paynym.rs/) for å finne QR-koden som er knyttet til betalingskoden hans.



![Image](assets/fr/09.webp)



Når du har skannet QR-koden, klikker du på `FØLG`-knappen for å følge PayNym.



![Image](assets/fr/10.webp)



Handlingen `FOLLOW` er tilstrekkelig for samarbeidstransaksjoner (*cahoots*). For å sende BIP47-betalinger må du imidlertid opprette en forbindelse: klikk på `CONNECT` for å utføre varslingstransaksjonen.



![Image](assets/fr/11.webp)



Meldingen om transaksjonen sendes deretter ut i nettverket. Vent til den har fått minst én bekreftelse før du foretar din første betaling.



![Image](assets/fr/12.webp)



## Foreta en BIP47-betaling



Du er nå koblet til mottakeren og kan sende en betaling til en unik adresse som genereres automatisk ved hjelp av BIP47-protokollen, uten noen forutgående utveksling med mottakeren.



Fra PayNym-hovedsiden klikker du på kontakten du ønsker å sende en betaling til.



![Image](assets/fr/13.webp)



Klikk på pilikonet øverst til høyre i grensesnittet.



![Image](assets/fr/14.webp)



Skriv inn beløpet som skal sendes. Du trenger ikke å oppgi en mottakeradresse: Den blir automatisk utledet ved hjelp av BIP47-protokollen.



![Image](assets/fr/15.webp)



Sjekk nøye transaksjonsdetaljene, inkludert gebyrer, og dra deretter den grønne pilen nederst på skjermen for å signere og sende transaksjonen.



![Image](assets/fr/16.webp)



Transaksjonen er sendt.



![Image](assets/fr/17.webp)



I dette eksempelet ble betalingen gjort til en annen av PayNym-lommebøkene mine. Jeg kan derfor se at den har ankommet min andre Ashigaru wallet, uten at noen adresse har blitt utvekslet manuelt: bare PayNym-identifikatoren ble brukt.



![Image](assets/fr/18.webp)



Du vet nå hvordan du bruker BIP47 gjenbrukbare betalingskoder takket være PayNym-implementeringen i Ashigaru-applikasjonen. Du kan nå dele denne betalingskoden med alle som ønsker å sende deg betalinger (spesielt gjentatte betalinger). Du kan også publisere PayNym-ID-en din på nettstedet ditt eller i sosiale nettverk for å motta donasjoner.



For å få dypere kunnskap om denne protokollen, forstå i detalj hvordan den fungerer og hva den innebærer for konfidensialitet, anbefaler jeg på det sterkeste at du tar BTC 204-kurset mitt:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c