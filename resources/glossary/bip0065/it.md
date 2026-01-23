---
term: BIP0065

definition: Introduzione dell'opcode OP_CHECKLOCKTIMEVERIFY che consente di bloccare i bitcoin fino a una data o a un'altezza del blocco specifica.
---
Introdotto un nuovo opcode denominato `OP_CHECKLOCKTIMEVERIFY` che consente di rendere inutilizzabile un UTXO fino a un momento futuro specificato. L'implementazione di questo BIP ha richiesto un soft fork, avvenuto il 14 dicembre 2015. È stata inoltre introdotta la versione 4 dei blocchi.