---
term: ENTROPY

---
Entropi er et kvantitativt mål på usikkerheten eller uforutsigbarheten knyttet til en datakilde eller en tilfeldig prosess i forbindelse med kryptografi og informasjon. Entropi spiller en avgjørende rolle for sikkerheten i kryptografiske systemer, spesielt når det gjelder generering av nøkler og tilfeldige tall. Høy entropi sikrer at de genererte nøklene er tilstrekkelig uforutsigbare og motstandsdyktige mot brute-force-angrep, der en angriper prøver alle mulige kombinasjoner for å gjette seg frem til nøkkelen.

I forbindelse med Bitcoin brukes entropi til å generere private nøkler eller seeds. Når man lager en deterministisk og hierarkisk lommebok, konstrueres den mnemoniske frasen ut fra et tilfeldig tall, som i seg selv stammer fra en entropikilde. Frasen brukes deretter til å generere flere private nøkler, på en deterministisk og hierarkisk måte, for å skape utgiftsbetingelser på UTXO-er.

Det er avgjørende å ha en entropikilde av høy kvalitet for å garantere sikkerheten i kryptografiske systemer. Entropikilder kan være fysiske prosesser, for eksempel elektronisk støy eller termiske variasjoner, eller programvareprosesser, for eksempel pseudotilfeldige tallgeneratorer.