---
term: SIGHASH_ANYPREVOUT
---

Propuesta para la implementación de un nuevo modificador de Flag SigHash en Bitcoin, introducido con el BIP118. `SIGHASH_ANYPREVOUT` permite una mayor flexibilidad en la gestión de transacciones, especialmente para aplicaciones avanzadas como los canales de pago en la Lightning Network y la actualización de Eltoo. El `SIGHASH_ANYPREVOUT` posibilita que la firma no esté vinculada a ningún UTXO anterior específico (*Cualquier Salida Anterior*). Utilizado en combinación con `SIGHASH_ALL`, permitiría firmar todas las salidas de una transacción, pero ninguna de las entradas. Esto habilitaría la reutilización de la firma para diferentes transacciones, siempre y cuando se cumplan ciertas condiciones especificadas.

> ► *Este modificador SigHash SIGHASH_ANYPREVOUT se deriva de la idea de SIGHASH_NOINPUT inicialmente propuesta por Joseph Poon en 2016 para mejorar su concepto de la Lightning Network.*