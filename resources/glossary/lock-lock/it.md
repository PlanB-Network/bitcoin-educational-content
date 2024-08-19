---
termine: LOCK (.LOCK)
---

File utilizzato in Bitcoin Core per bloccare la directory dei dati. Viene creato quando bitcoind o Bitcoin-qt si avviano per impedire a più istanze del software di accedere contemporaneamente alla stessa directory dei dati. L'obiettivo è prevenire conflitti e corruzione dei dati. Se il software si ferma inaspettatamente, il file .lock può rimanere e deve essere eliminato manualmente prima di riavviare Bitcoin Core.