---
term: Transaktionsavgifter
definition: Belopp som ersätter miners för att inkludera en transaktion i ett block, beräknat som skillnaden mellan inputs och outputs.
---

Transaktionsavgifter utgör en summa som syftar till att kompensera miners för deras deltagande i Proof of Work-mekanismen. Dessa avgifter uppmuntrar miners att inkludera transaktioner i de block de skapar. De uppstår genom skillnaden mellan den totala mängden inmatningar och den totala mängden utmatningar i en transaktion:


```text
fees = inputs - outputs
```


De uttrycks i `Sats/vBytes`, vilket innebär att avgifterna inte beror på mängden bitcoins som skickas, utan på transaktionens vikt. De väljs fritt av avsändaren av en transaktion och bestämmer dess hastighet för inkludering i ett block genom en auktionsmekanism. Låt oss till exempel säga att jag gör en transaktion med en input på 100 000 Sats, en output på 40 000 Sats och en annan output på 58 500 Sats. Den totala summan av utdata är 98 500 Sats`. De avgifter som allokerats till denna transaktion är 1 500 Sats`. Den Miner som inkluderar min transaktion kan skapa 1 500 Sats` i sin Coinbase Transaction i Exchange för de 1 500 Sats` som jag inte återvann i mina outputs.


Transaktioner med högre avgifter, i förhållande till sin storlek, behandlas som en prioritet av miners, vilket kan påskynda bekräftelseprocessen. Omvänt kan transaktioner med lägre avgifter försenas under perioder med hög överbelastning. Det är värt att notera att Bitcoin:s transaktionsavgifter skiljer sig från blocksubventionen, som är ett ytterligare incitament för miners. Block reward består av nya bitcoins som skapas med varje minat block (blocksubvention), samt de insamlade transaktionsavgifterna. Blocksubventionen minskar över tid på grund av den totala Supply-gränsen för bitcoins, men transaktionsavgifterna kommer att fortsätta att spela en avgörande roll för att uppmuntra miners att delta.


På protokollnivå finns det inget som hindrar användare från att inkludera transaktioner utan några avgifter i ett block. I verkligheten är denna typ av avgiftsfri transaktion exceptionell. Som standard vidarebefordrar Bitcoin-noder inte transaktioner med avgifter som är lägre än `1 sat/vBytes`. Om några avgiftsfria transaktioner har passerat beror det på att de integrerades direkt av den vinnande Miner, utan att passera nätverket av noder. Till exempel innehåller följande transaktion inga avgifter:


```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```


I detta specifika exempel var det en transaktion som initierades av direktören för F2Pool Mining pool. Som vanlig användare är den nuvarande nedre gränsen därför `1 sat/vBytes`.

Det är också nödvändigt att ta hänsyn till gränserna för rensning. Under perioder med hög belastning rensar nodernas mempools sina väntande transaktioner under ett visst tröskelvärde för att respektera deras tilldelade RAM-gräns. Denna gräns väljs fritt av användaren, men många lämnar standardvärdet för Bitcoin Core på 300 MB. Det kan modifieras i filen `Bitcoin.conf` med parametern `maxmempool`.

