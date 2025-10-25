---
term: HORODATAGE
---

Tidsstämpling, eller "Timestamp" på engelska, är en mekanism för att associera en exakt tidsmarkering med en händelse, data eller ett meddelande. I allmänna sammanhang i datorsystem används tidsstämpling för att fastställa den kronologiska ordningen för operationer och för att verifiera integriteten hos data över tiden.


I det specifika fallet med Bitcoin används tidsstämplar för att fastställa kronologin för transaktioner och block. Varje block i Blockchain innehåller en Timestamp som anger den ungefärliga tiden för dess skapande. Satoshi Nakamoto talar till och med om en "Timestamp-server" i sin vitbok för att beskriva det vi idag skulle kalla "Blockchain". Tidsstämplingens roll på Bitcoin är att fastställa transaktionernas kronologi, så att det utan ingripande av en central myndighet kan fastställas vilken transaktion som anlände först. Denna mekanism gör det möjligt för varje användare att verifiera att en transaktion inte har förekommit tidigare, och därmed förhindra att en illvillig användare gör en dubbel utgift. Denna mekanism motiveras av Satoshi Nakamoto i hans vitbok med den berömda meningen: *Den här standarden är baserad på Unix-tiden, som representerar det totala antalet sekunder som gått sedan den 1 januari 1970.*


> tidsstämplar för block är relativt flexibla på Bitcoin, eftersom det för att en Timestamp ska anses giltig helt enkelt krävs att den är större än mediantiden för de 11 block som föregår den (MTP) och mindre än medianen för de tider som returneras av noderna (nätverksjusterad tid) plus 2 timmar