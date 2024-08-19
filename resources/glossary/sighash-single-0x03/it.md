---
termine: SIGHASH_SINGLE (0X03)
---

Tipo di flag SigHash utilizzato nelle firme delle transazioni Bitcoin per indicare che la firma si applica a tutti gli input della transazione e a un solo output, corrispondente all'indice dello stesso input firmato. Pertanto, ogni input firmato con `SIGHASH_SINGLE` è specificamente collegato a un particolare output. Gli altri output non sono vincolati dalla firma e possono quindi essere modificati successivamente. Questo tipo di firma è utile in transazioni complesse, dove i partecipanti vogliono collegare certi input a specifici output, lasciando al contempo flessibilità per gli altri output della transazione.