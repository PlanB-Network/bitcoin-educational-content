---
term: BIP8

---
Sviluppato in seguito ai dibattiti su SegWit, che ha utilizzato BIP9 per la sua attivazione, BIP8 è un metodo di attivazione soft fork che incorpora nativamente un meccanismo automatico UASF (*User-Activated Soft Fork*). Come BIP9, BIP8 utilizza la segnalazione dei minatori ma aggiunge il parametro `LOT` (*Lock-in On Time out*). Se `LOT` è impostato su `true`, allo scadere del periodo di segnalazione senza raggiungere la soglia richiesta, viene automaticamente attivato un UASF, forzando l'attivazione del soft fork. Questo approccio costringe i minatori a collaborare o a rischiare un UASF imposto dagli utenti. Inoltre, a differenza del BIP9, il BIP8 definisce il periodo di segnalazione in base all'altezza del blocco, eliminando le potenziali manipolazioni del tasso di hash da parte dei minatori. Il BIP8 consente anche di impostare una soglia di voto variabile e introduce un parametro per l'altezza minima del blocco per l'attivazione, dando ai minatori il tempo di prepararsi e segnalare il loro accordo in anticipo senza essere necessariamente pronti. Quando un soft fork viene attivato tramite BIP8 con il parametro `LOT=true`, si utilizza un metodo molto aggressivo nei confronti dei minatori che vengono immediatamente messi sotto pressione da un potenziale UASF. In effetti, lascia loro solo due scelte:


- Siate collaborativi e facilitate così il processo di attivazione;
- Essere non collaborativi, nel qual caso gli utenti eseguono automaticamente una UASF per imporre la soft fork.