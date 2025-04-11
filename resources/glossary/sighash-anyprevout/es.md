---
term: SIGHASH_ANYPREVOUT

---
Propuesta para la implementación de un nuevo modificador SigHash Flag en Bitcoin, introducido con BIP118. `SIGHASH_ANYPREVOUT` permite una mayor flexibilidad en la gestión de transacciones, especialmente para aplicaciones avanzadas como los canales de pago en la Lightning Network y la actualización de Eltoo. `SIGHASH_ANYPREVOUT` permite que la firma no esté vinculada a ninguna UTXO (*Any Previous Output*) anterior específica. Utilizada en combinación con `SIGHASH_ALL`, permitiría firmar todas las salidas de una transacción, pero ninguna de las entradas. Esto permitiría la reutilización de la firma para diferentes transacciones, siempre que se cumplan ciertas condiciones especificadas.

> ► *Este modificador SigHash SIGHASH_ANYPREVOUT deriva de la idea de SIGHASH_NOINPUT propuesta inicialmente por Joseph Poon en 2016 para mejorar su concepto de Lightning Network.*