---
name: Merking av UTXO
description: Hvordan merke UTXOene dine på riktig måte?
---
![cover](assets/cover.webp)

I denne veiledningen vil du oppdage alt du trenger å vite om merking av UTXOer i din Bitcoin-lommebok og om myntkontroll. Vi starter med en teoretisk del for å fullt ut forstå disse konseptene, før vi går videre til en praktisk del hvor vi utforsker hvordan man konkret bruker etiketter i hovedprogramvaren for Bitcoin-lommeboken.

## Hva er UTXO-merking?
"Merking" er en teknikk som innebærer å knytte en annotasjon eller etikett til en spesifikk UTXO innenfor en Bitcoin-lommebok. Disse annotasjonene lagres lokalt av lommebokprogramvaren og overføres aldri over Bitcoin-nettverket. Merking er dermed et verktøy for personlig forvaltning.

For eksempel, hvis jeg mottar en UTXO fra en P2P-transaksjon via Bisq med Charles, kunne jeg tildele den etiketten `Bisq P2P Kjøp Charles`.

Merking lar en huske opprinnelsen eller det tiltenkte bestemmelsesstedet for UTXOen, noe som forenkler fondsforvaltningen og optimaliserer brukerens personvern. Merking blir enda mer relevant når det kombineres med "myntkontroll"-funksjonaliteten. Myntkontroll er en mulighet tilgjengelig i gode Bitcoin-lommebøker, som gir brukeren muligheten til manuelt å velge hvilke spesifikke UTXOer som vil bli brukt som inndata når man oppretter en transaksjon.

Å bruke en lommebok med myntkontroll, sammenkoblet med UTXO-merking, lar brukere presist skille og velge UTXOer for sine transaksjoner, og dermed unngå å slå sammen UTXOer fra forskjellige kilder. Denne praksisen reduserer risikoene forbundet med Common Input Ownership Heuristic (CIOH), som antyder felles eierskap av inndataene i en transaksjon, noe som kan kompromittere brukerens personvern.

La oss gå tilbake til eksemplet med min no-KYC UTXO fra Bisq; jeg ønsker å unngå å kombinere den med en UTXO som kommer, si, fra en regulert utvekslingsplattform som kjenner min identitet. Ved å plassere en distinkt etikett på min no-KYC UTXO og på min KYC UTXO, vil jeg kunne enkelt identifisere hvilken UTXO som skal forbrukes som inndata for å tilfredsstille et utlegg, ved å bruke myntkontrollfunksjonaliteten.

## Hvordan merke UTXOen din på riktig måte?
Det finnes ingen universell metode for merking av UTXOer som passer for alle. Det er opp til deg å definere et merkesystem slik at du enkelt kan finne veien rundt i lommeboken din.
Et avgjørende kriterium i merkingen er kilden til UTXOen. Du bør ganske enkelt angi hvordan denne mynten ankom lommeboken din. Er den fra en utvekslingsplattform? En regningsoppgjør fra en klient? En peer-to-peer-utveksling? Eller representerer den vekslepenger fra et kjøp? Således kunne du spesifisere:
- `Uttak Exchange.com`;
- `Betaling Klient David`;
- `P2P Kjøp Charles`;
- `Vekslepenger fra sofakjøp`.
![labelling](assets/en/1.webp)
For å forfine din UTXO-forvaltning og holde deg til dine fondssegregasjonsstrategier innenfor lommeboken din, kunne du berike etikettene dine med en ekstra indikator som reflekterer disse separasjonene. Hvis lommeboken din inneholder to kategorier av UTXOer som du ikke ønsker å blande, kunne du integrere en markør i etikettene dine for å tydelig skille disse gruppene.

Disse separasjonsmarkørene vil avhenge av dine egne kriterier, som forskjellen mellom KYC UTXO (kjenner din identitet) og no-KYC (anonym), eller mellom profesjonelle og personlige midler. Tar de tidligere nevnte etiketteksemplene, dette kunne oversettes som:
- `KYC - Uttak Exchange.com`;
- `KYC - Betaling Klient David`;
- `NO KYC - P2P Kjøp Charles`;
- `NO KYC - Vekslepenger fra sofakjøp`.
![merking](assets/en/2.webp)Uansett, husk at god merking er merking som du vil kunne forstå når du trenger det. Hvis din Bitcoin-lommebok hovedsakelig er ment for sparing, kan det hende at etikettene bare vil være nyttige for deg om flere tiår. Derfor, sørg for at de er klare, presise og omfattende.

Det er også tilrådelig å videreføre merkingen av en mynt gjennom transaksjoner. For eksempel, under en no-KYC UTXO-konsolidering, sørg for å merke den resulterende UTXO ikke bare som `konsolidering`, men spesifikt som `no-KYC konsolidering` for å opprettholde en klar spor av myntens opprinnelse.

Til slutt, det er ikke obligatorisk å sette en dato på en etikett. De fleste lommebokprogramvarer viser allerede transaksjonsdatoen, og det er alltid mulig å hente denne informasjonen på en blokkutforsker ved hjelp av dens TXID.

## Veiledning: Merking på Specter Desktop

Koble til og åpne lommeboken din på Specter Desktop, og velg deretter `Addresses`-fanen.

![merking](assets/notext/3.webp)
Her vil du se listen over alle adressene dine, samt eventuelle bitcoins som er låst på dem. Som standard er adresser identifisert av deres indeks under `Label`-kolonnen. For å endre en etikett, klikk bare på den, skriv inn ønsket etikett, og bekreft deretter ved å klikke på det blå ikonet.
![merking](assets/notext/4.webp)

Din etikett vil da vises i listen over adressene dine.

![merking](assets/notext/5.webp)

Du kan også tildele en etikett på forhånd, når du deler mottaksadressen din med avsenderen. For å gjøre dette, ved å få tilgang til `Receive`-fanen, noter etiketten din i det dedikerte feltet.

![merking](assets/notext/6.webp)

## Veiledning: Merking på Electrum

På Electrum Wallet, etter å ha logget inn på lommeboken din, klikk på transaksjonen du ønsker å tildele en etikett fra `History`-fanen.

![merking](assets/notext/7.webp)

Et nytt vindu åpnes. Klikk på `Description`-boksen og skriv inn etiketten din.

![merking](assets/notext/8.webp)

Når etiketten er skrevet inn, kan du lukke dette vinduet.

![merking](assets/notext/9.webp)

Din etikett har blitt vellykket lagret. Du kan finne den under `Description`-fanen.

![merking](assets/notext/10.webp)

I `Coins`-fanen, hvorfra du kan utføre myntkontroll, finnes etiketten din i `Label`-kolonnen.

![merking](assets/notext/11.webp)

## Veiledning: Merking på Green Wallet

I Green Wallet-appen, få tilgang til lommeboken din og velg transaksjonen du ønsker å merke. Deretter klikker du på det lille blyantikonet for å notere etiketten din.

![merking](assets/notext/12.webp)

Skriv inn etiketten din, og klikk deretter på den grønne `Save`-knappen.

![merking](assets/notext/13.webp)

Du vil kunne finne etiketten din både i detaljene til transaksjonen din og på dashbordet til lommeboken din.

![merking](assets/notext/14.webp)

## Veiledning: Merking på Samourai Wallet

I Samourai Wallet er det forskjellige metoder som lar deg tildele en etikett til en transaksjon. For den første, start med å åpne lommeboken din og velg transaksjonen du ønsker å legge til en etikett på. Trykk deretter på `Add`-knappen, som ligger ved siden av `Notes`-boksen.

![merking](assets/notext/15.webp)
Skriv inn etiketten din og bekreft ved å klikke på den blå `Legg til`-knappen.
![labelling](assets/notext/16.webp)

Du vil finne etiketten din i detaljene for transaksjonen din, men også på dashbordet i lommeboken din.

![labelling](assets/notext/17.webp)
For den andre metoden, klikk på de tre små prikkene øverst til høyre på skjermen, deretter på `Vis Ubrukte Transaksjonsutganger`-menyen.
![labelling](assets/notext/18.webp)

Her vil du finne en omfattende liste over alle UTXOene i lommeboken din. Den viste listen gjelder for min innskuddskonto, men denne operasjonen kan replikeres for Whirlpool-kontoer ved å navigere fra den dedikerte menyen.

Klikk deretter på UTXOen du ønsker å merke, etterfulgt av `Legg til`-knappen.

![labelling](assets/notext/19.webp)

Skriv inn etiketten din og bekreft ved å klikke på den blå `Legg til`-knappen. Du vil da finne etiketten din både i detaljene for transaksjonen din og på dashbordet i lommeboken din.

![labelling](assets/notext/20.webp)

## Veiledning: Merking i Sparrow Wallet

Med Sparrow Wallet-programvaren er det mulig å tildele etiketter på flere måter. Den enkleste metoden er å legge til en etikett på forhånd, når du kommuniserer en mottaksadresse til avsenderen. For å gjøre dette, i `Motta`-menyen, klikk på `Etikett`-feltet og skriv inn etiketten du ønsker. Dette vil bli bevart og tilgjengelig gjennom programvaren så snart bitcoins mottas på adressen.

![labelling](assets/notext/21.webp)

Hvis du glemte å merke adressen din ved mottak, er det fortsatt mulig å legge til en senere via `Transaksjoner`-menyen. Klikk bare på transaksjonen din i `Etikett`-kolonnen, og skriv deretter inn ønsket etikett.

![labelling](assets/notext/22.webp)

Du har også muligheten til å legge til eller endre etikettene dine fra `Adresser`-menyen.

![labelling](assets/notext/23.webp)

Til slutt kan du se etikettene dine i `UTXOer`-menyen. Sparrow Wallet legger automatisk til i parentes bak etiketten din naturen til utgangen, noe som hjelper til med å skille UTXOer som kommer fra veksling fra de som er mottatt direkte.

![labelling](assets/notext/24.webp)