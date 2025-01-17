---
term: SIGHASH_SINGOLO (0X03)

---
Tipo di flag SigHash utilizzato nelle firme delle transazioni Bitcoin per indicare che la firma si applica a tutti gli input della transazione e a un solo output, corrispondente all'indice dello stesso input firmato. In questo modo, ogni input firmato con `SIGHASH_SINGLE` è specificamente collegato a un particolare output. Le altre uscite non sono impegnate dalla firma e possono quindi essere modificate in seguito. Questo tipo di firma è utile nelle transazioni complesse, in cui i partecipanti desiderano collegare determinati input a specifiche uscite, lasciando al contempo una certa flessibilità per le altre uscite della transazione.