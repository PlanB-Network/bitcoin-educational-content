---
term: STONEWALL X2

---
En spesifikk form for Bitcoin-transaksjon som tar sikte på å øke brukerens personvern under et forbruk, ved å samarbeide med en tredjepart som ikke er involvert i utgiften. Denne metoden simulerer en mini-coinjoin mellom to deltakere, samtidig som det foretas en betaling til en tredjepart. Stonewall x2-transaksjoner er tilgjengelige både i Samourai Wallet-appen og Sparrow Wallet-programvaren (begge er interoperable).

Operasjonen er relativt enkel: Den bruker en UTXO i vår besittelse til å utføre betalingen og søker hjelp fra en tredjepart som også bidrar med en UTXO de eier. Transaksjonen ender med fire utganger: to av dem med like store beløp, den ene til adressen til betalingsmottakeren, den andre til en adresse som tilhører samarbeidspartneren. En tredje UTXO sendes tilbake til en annen adresse som tilhører samarbeidspartneren, slik at de kan få tilbake det opprinnelige beløpet (en nøytral handling for dem, minus gruveavgiftene), og en siste UTXO returnerer til en adresse vi eier, som utgjør endringen fra betalingen. Dermed er tre forskjellige roller definert i Stonewall x2-transaksjoner:


- Avsenderen, som foretar den faktiske betalingen;
- Samarbeidspartneren, som gir bitcoins for å forbedre den generelle anonymiteten til transaksjonen, samtidig som de får tilbake pengene sine på slutten;
- Mottakeren, som kanskje ikke er klar over transaksjonens spesifikke natur og bare venter på betaling fra avsenderen.

![](../../dictionnaire/assets/3.webp)

Stonewall x2-strukturen tilfører mye entropi til transaksjonen og gjør kjedeanalysen uoversiktlig. Fra utsiden kan en slik transaksjon tolkes som en liten coinjoin mellom to personer. Men i virkeligheten er det en betaling. Denne metoden skaper dermed usikkerhet i kjedeanalysen, eller fører til falske spor. Selv om en ekstern observatør klarer å identifisere mønsteret i Stonewall x2-transaksjonen, vil vedkommende ikke ha all informasjonen. De vil ikke være i stand til å avgjøre hvilken av de to UTXO-ene med like store beløp som tilsvarer betalingen. Videre vil de ikke kunne vite hvem som foretok betalingen. Til slutt vil de ikke kunne avgjøre om de to UTXO-ene kommer fra to forskjellige personer, eller om de tilhører én og samme person som har slått dem sammen. Dette siste punktet skyldes det faktum at klassiske Stonewall-transaksjoner følger nøyaktig samme mønster som Stonewall x2-transaksjoner. Utenfra og uten ytterligere informasjon om konteksten er det umulig å skille en Stonewall-transaksjon fra en Stonewall x2-transaksjon. De førstnevnte er imidlertid ikke samarbeidstransaksjoner, mens de sistnevnte er det. Dette bidrar til enda mer tvil om utgiftene.