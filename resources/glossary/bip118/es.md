---
term: BIP118
---

Propuesta para mejorar Bitcoin dirigida a introducir dos nuevos modificadores de SigHash Flag: `SIGHASH_ANYPREVOUT` y `SIGHASH_ANYPREVOUTANYSCRIPT`. Estas características amplían las capacidades de las transacciones de Bitcoin, particularmente en términos de contratos inteligentes y soluciones de superposición como la Lightning Network. BIP118 permitiría notablemente el uso de Eltoo. La principal ventaja de `SIGHASH_ANYPREVOUT` es permitir la reutilización de firmas a través de múltiples transacciones, lo que ofrece más flexibilidad. Específicamente, estos SigHashes permiten una firma que no cubre ninguna de las entradas de la transacción.