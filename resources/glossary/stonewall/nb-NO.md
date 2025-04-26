---
term: STONEWALL

---
En spesifikk form for Bitcoin-transaksjon som tar sikte på å øke brukerens personvern under et forbruk ved å etterligne en coinjoin mellom to personer, uten å faktisk være en. Denne transaksjonen er faktisk ikke samarbeidende. En bruker kan konstruere den alene, med bare sine egne UTXO-er som input. Derfor kan du opprette en Stonewall-transaksjon til enhver anledning, uten å måtte synkronisere med en annen bruker.

Stonewall-transaksjonen fungerer på følgende måte: Ved inngangen til transaksjonen bruker avsenderen 2 UTXO-er som tilhører dem. Transaksjonen produserer deretter 4 utganger, hvorav 2 vil være nøyaktig det samme beløpet. De andre 2 vil utgjøre endringen. Av de to utgangene med samme beløp er det bare én som faktisk går til mottakeren av betalingen.

Det er altså bare to roller i en Stonewall-transaksjon:


- Avsenderen, som foretar selve betalingen;
- Mottakeren, som kanskje ikke er klar over hva transaksjonen går ut på, og som bare venter på betaling fra avsenderen.

![](../../dictionnaire/assets/33.webp)

Stonewall-transaksjoner er tilgjengelige både i Samourai Wallet-applikasjonen og Sparrow Wallet-programvaren.

Stonewall-strukturen tilfører mye entropi til transaksjonen og gjør det vanskelig å analysere kjeden. Fra utsiden kan en slik transaksjon tolkes som en liten coinjoin mellom to personer. Men i virkeligheten er det, akkurat som Stonewall x2-transaksjonen, en betaling. Denne metoden skaper dermed usikkerhet i kjedeanalysen, eller fører til falske spor. Selv om en ekstern observatør klarer å identifisere mønsteret i Stonewall-transaksjonen, vil vedkommende ikke ha all informasjonen. De vil ikke være i stand til å avgjøre hvilken av de to UTXO-ene med samme beløp som tilsvarer betalingen. De vil heller ikke kunne avgjøre om de to UTXO-ene ved inngangen kommer fra to forskjellige personer, eller om de tilhører én og samme person som har slått dem sammen. Dette siste poenget skyldes at Stonewall x2-transaksjoner følger nøyaktig samme mønster som Stonewall-transaksjoner. Utenfra og uten ytterligere kontekstinformasjon er det umulig å skille en Stonewall-transaksjon fra en Stonewall x2-transaksjon. De førstnevnte er imidlertid ikke samarbeidstransaksjoner, mens de sistnevnte er det. Dette bidrar til å så enda mer tvil om denne utgiften.