---
term: Assume utxo
definition: Een Bitcoin Core-parameter die snelle synchronisatie van een nieuw knooppunt mogelijk maakt door een snapshot van de UTXO-set die als geldig wordt aangenomen, te gebruiken, voordat de geschiedenis op de achtergrond wordt geverifieerd.
---
Configuratieparameter in de meerderheidsclient Bitcoin Core die een node die net is geïnitialiseerd (maar nog geen IBD heeft gedaan) in staat stelt de verificatie van transacties en de UTXO-set uit te stellen vóór een bepaald snapshot. Het concept is gebaseerd op het gebruik van een UTXO-set (lijst van alle bestaande UTXO's op een bepaald moment) geleverd door Core en verondersteld accuraat te zijn, waardoor de node zeer snel gesynchroniseerd kan worden op de keten met de meeste verzamelde arbeid. Omdat de node de lange IBD-stap overslaat, is deze zeer snel functioneel voor de gebruiker.

Assume UTXO verdeelt de synchronisatie (IBD) in twee delen: Eerst voert de node de Header First Sync uit (alleen verificatie van de headers) en beschouwt de door Core geleverde UTXO-set als geldig; Daarna, zodra deze functioneel is, zal de node de volledige blokgeschiedenis op de achtergrond verifiëren en een nieuwe UTXO-set bijwerken die hij zelf heeft geverifieerd. Als deze laatste niet overeenkomt met de door Core geleverde UTXO-set, zal hij een foutmelding geven.

Assume UTXO maakt het dus mogelijk om de voorbereiding van een nieuwe Bitcoin-node te versnellen door het verificatieproces van transacties en de UTXO-set uit te stellen dankzij een bijgewerkte snapshot die in Core wordt geleverd.







