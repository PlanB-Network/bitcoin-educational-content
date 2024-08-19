---
termine: BIP61
---

Introduce un messaggio di rifiuto nel protocollo di comunicazione tra nodi. L'obiettivo del BIP61 è aggiungere un meccanismo di feedback quando un nodo riceve una transazione o un blocco da un altro nodo che considera non valido. Questo messaggio di rifiuto permetterebbe a un nodo di segnalare al mittente il motivo per cui è stato rifiutato. Questo tipo di comunicazione era inteso a migliorare l'interoperabilità tra diversi clienti e le comunicazioni tra nodi completi e clienti SPV. Le funzionalità introdotte da BIP61 sono state eventualmente abbandonate a partire dalla versione 0.20.0 di Bitcoin Core, in quanto considerate non necessarie mentre comportavano un aumento del fabbisogno di banda.