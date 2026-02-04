---
term: BIP0145

definition: Aggiornamento della chiamata JSON-RPC getblocktemplate per integrare il supporto SegWit e il calcolo del peso delle transazioni.
---
Aggiorna la chiamata JSON-RPC `getblocktemplate` per includere il supporto per SegWit, in conformità con la BIP141. Questo aggiornamento consente ai minatori di costruire i blocchi tenendo conto della nuova misurazione del "peso" delle transazioni e dei blocchi introdotta da SegWit e di altri parametri come il calcolo del limite di sigops.