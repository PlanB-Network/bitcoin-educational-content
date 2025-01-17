---
term: SIGHASH_NONE (0X02)

---
Tipo di flag SigHash utilizzato nelle firme delle transazioni Bitcoin per indicare che la firma si applica a tutti gli input della transazione, ma a nessuno dei suoi output. L'uso di `SIGHASH_NONE` implica che il firmatario si impegna solo sugli input, lasciando che gli output rimangano indeterminati o modificabili dopo la firma. Questo tipo di firma è utile nei casi in cui il firmatario desidera autorizzare altre parti a decidere come verranno distribuiti i bitcoin nella transazione.