---
termine: DIFFICOLTÀ
---

Un parametro regolabile che determina la complessità della prova di lavoro richiesta per aggiungere un nuovo blocco alla blockchain e guadagnare la ricompensa associata. Questa difficoltà è rappresentata dal target di difficoltà, un valore a 256 bit che stabilisce il limite superiore che l'hash dell'intestazione del blocco deve soddisfare per essere considerato valido. L'obiettivo è che l'hash, ottenuto attraverso una doppia esecuzione di SHA256 (SHA256d), sia minore o uguale a questo target. Per raggiungere questo hash, i minatori manipolano il `nonce` nell'intestazione del blocco. La difficoltà si aggiusta ogni 2016 blocchi, o circa ogni due settimane, per mantenere il tempo medio di creazione del blocco a circa 10 minuti.