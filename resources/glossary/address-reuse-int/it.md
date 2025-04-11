---
term: RIUTILIZZO DELL'INDIRIZZO (INT)

---
Il riutilizzo degli indirizzi è detto "interno" quando si verifica all'interno della stessa transazione sia come ingresso che come uscita. In questa configurazione, il riutilizzo interno degli indirizzi è un'euristica di analisi della blockchain che consente di formulare un'ipotesi plausibile sulla modifica della transazione. Infatti, se ci sono due uscite e una di queste utilizza lo stesso indirizzo di ricezione dell'ingresso, è probabile che la seconda uscita stia uscendo dal possesso dell'utente iniziale. L'uscita con l'indirizzo riutilizzato rappresenta probabilmente il cambiamento.

![](../../dictionnaire/assets/10.webp)