---
term: LevelDB
definition: Lagringsbibliotek för nyckel-värde som används av Bitcoin Core för UTXO-mängden och index.
---

Ett lättviktigt, snabbt och öppen källkodsbaserat nyckelvärdeslagringsbibliotek utformat av Google. Det används i Bitcoin för att lagra UTXO-uppsättningen, transaktionsindexet och blockindexet. Detta databassystem introducerades 2012 som en del av "Ultraprune" Pull Request som syftade till att ersätta BerkeleyDB. Denna förändring hade betydande återverkningar, inklusive skapandet av den första Blockchain-spliten med en större omorganisation av 24 block den 12 mars 2013. Denna incident beskrevs i detalj i BIP50. Senare ledde denna systemförändring till och med till en oavsiktlig Hard Fork den 15 maj 2013.