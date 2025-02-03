---
term: BIP118

---
Propuesta de mejora de Bitcoin destinada a introducir dos nuevos modificadores SigHash Flag: `SIGHASH_ANYPREVOUT` y `SIGHASH_ANYPREVOUTANYSCRIPT`. Estas características amplían las capacidades de las transacciones de Bitcoin, especialmente en términos de contratos inteligentes y soluciones superpuestas como la Lightning Network. BIP118 permitiría, en particular, el uso de Eltoo. La principal ventaja de `SIGHASH_ANYPREVOUT` es permitir la reutilización de firmas a través de múltiples transacciones, lo que ofrece más flexibilidad. En concreto, estos SigHashes permiten una firma que no cubre ninguna de las entradas de la transacción.