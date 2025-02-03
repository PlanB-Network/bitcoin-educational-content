---
term: BIP61

---
Introdotto un messaggio di rifiuto nel protocollo di comunicazione tra nodi. L'obiettivo del BIP61 è quello di aggiungere un meccanismo di feedback quando un nodo riceve una transazione o un blocco da un altro nodo che considera non valido. Questo messaggio di rifiuto permetterebbe a un nodo di segnalare al mittente il motivo del rifiuto. Questo tipo di comunicazione è stato pensato per migliorare l'interoperabilità tra i diversi client e le comunicazioni tra i nodi completi e i client SPV. Le funzionalità apportate da BIP61 sono state abbandonate a partire dalla versione 0.20.0 di Bitcoin Core, in quanto ritenute superflue e perché comportavano un maggiore fabbisogno di banda.