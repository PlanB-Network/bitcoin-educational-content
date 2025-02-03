---
term: LOCK (.LOCK)

---
File utilizzato in Bitcoin Core per bloccare la directory dei dati. Viene creato all'avvio di bitcoind o Bitcoin-qt per evitare che più istanze del software accedano contemporaneamente alla stessa directory di dati. L'obiettivo è quello di prevenire conflitti e corruzione dei dati. Se il software si arresta inaspettatamente, il file .lock può rimanere e deve essere cancellato manualmente prima di riavviare Bitcoin Core.