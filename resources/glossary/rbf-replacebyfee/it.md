---
termine: RBF (REPLACE-BY-FEE)
---

Un meccanismo transazionale che consente al mittente di sostituire una transazione con un'altra pagando commissioni più elevate, al fine di accelerarne la conferma. Se una transazione con commissioni troppo basse rimane bloccata, il mittente può utilizzare *Replace-By-Fee* per aumentare le commissioni e dare priorità alla loro transazione sostitutiva nei mempool.

RBF è applicabile finché la transazione si trova nei mempool; una volta in un blocco, non può più essere sostituita. Al momento dell'invio iniziale, la transazione deve specificare la sua disponibilità a essere sostituita regolando il valore `nSequence` a un numero inferiore a `0xfffffffe`. Questo è noto come un "flag" RBF. Questa impostazione segnala la possibilità di aggiornare la transazione dopo che è stata trasmessa, consentendo successivamente un RBF. Tuttavia, a volte è possibile sostituire una transazione che non ha segnalato RBF. I nodi che utilizzano il parametro di configurazione `mempoolfullrbf=1` accettano questa sostituzione anche se RBF non era stato inizialmente segnalato.

A differenza di CPFP (*Child Pays For Parent*), dove il destinatario può agire per accelerare la transazione, RBF (*Replace-By-Fee*) consente al mittente di prendere l'iniziativa per accelerare la propria transazione aumentando le commissioni.