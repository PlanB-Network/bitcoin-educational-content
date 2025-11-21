---
term: FORZA CHIUDERE
---

Meccanismo non cooperativo di chiusura del canale Lightning. Quando due utenti aprono un canale con un Multisig 2/2, ciascuno può chiudere unilateralmente il canale trasmettendo l'ultimo Commitment Transaction già firmato, al fine di recuperare i propri bitcoin sulla catena. Questa operazione è nota come "chiusura forzata".


Questo metodo viene generalmente utilizzato se uno dei partecipanti non risponde più o se la chiusura cooperativa del canale è impossibile. Se la chiusura forzata può essere evitata, è meglio, poiché richiede più tempo per recuperare i fondi onchain e può essere molto più costosa in termini di commissioni.


In una chiusura forzata, uno dei due utenti trasmette il Commitment Transaction, che riflette l'ultimo stato conosciuto del canale Lightning. Si verifica quindi un blocco temporale prima che i bitcoin possano essere recuperati sulla catena, dando all'altra parte il tempo di verificare che la transazione corrisponda all'ultimo stato del canale. Se un utente tenta di imbrogliare pubblicando un Commitment Transaction non aggiornato, l'altra parte può usare il segreto di revoca per punire l'imbroglione e recuperare tutti i fondi nel canale.