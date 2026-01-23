---
term: BIP0090

definition: Proposta che semplifica la verifica dell'attivazione dei vecchi soft fork utilizzando l'altezza del blocco invece della segnalazione dei miner.
---
Proposta di semplificare il processo di attivazione di precedenti soft fork sostituendo il meccanismo di segnalazione dei minatori attraverso i numeri di versione dei blocchi con semplici verifiche dell'altezza dei blocchi. Questa modifica eliminerebbe la necessità di verificare i 1000 blocchi precedenti per l'attivazione delle regole di consenso, riducendo così il debito tecnico associato all'implementazione di queste soft fork.