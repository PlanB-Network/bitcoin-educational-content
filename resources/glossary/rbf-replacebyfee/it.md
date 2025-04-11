---
term: RBF (REPLACE-BY-FEE)

---
Meccanismo transazionale che consente al mittente di sostituire una transazione con un'altra pagando tariffe più alte, al fine di accelerarne la conferma. Se una transazione con tariffe troppo basse si blocca, il mittente può usare *Replace-By-Fee* per aumentare le tariffe e dare priorità alla transazione sostitutiva nei mempool.

La RBF è applicabile finché la transazione si trova nei mempool; una volta in un blocco, non può più essere sostituita. Al momento dell'invio iniziale, la transazione deve specificare la sua disponibilità a essere sostituita regolando il valore `nSequence` a un numero inferiore a `0xfffffffe`. Questo è noto come "flag" RBF. Questa impostazione segnala la possibilità di aggiornare la transazione dopo che è stata trasmessa, consentendo quindi un RBF. Tuttavia, a volte è possibile sostituire una transazione che non ha segnalato RBF. I nodi che utilizzano il parametro di configurazione `mempoolfullrbf=1` accettano questa sostituzione anche se la RBF non è stata inizialmente segnalata.

A differenza del CPFP (*Child Pays For Parent*), in cui il destinatario può agire per accelerare la transazione, il RBF (*Replace-By-Fee*) consente al mittente di prendere l'iniziativa di accelerare la propria transazione aumentando le commissioni.