---
term: VIN
---

Un elemento específico de una transacción de Bitcoin que especifica la fuente de fondos utilizada para satisfacer las salidas. Cada `vin` hace referencia a una salida no gastada (UTXO) de una transacción anterior. Una transacción puede contener múltiples entradas, cada una identificada por una combinación del `txid` (el identificador de la transacción original) y el `vout` (el índice de la salida en esa transacción).

Cada `vin` incluye la siguiente información:
* `txid`: el identificador de la transacción anterior que contiene la salida utilizada aquí como entrada;
* `vout`: el índice de la salida en la transacción anterior;
* `scriptSig` o `scriptWitness`: un script de desbloqueo que proporciona los datos necesarios para satisfacer las condiciones impuestas por el `scriptPubKey` de la transacción anterior cuyos fondos se están gastando, generalmente proporcionando una firma criptográfica;
* `nSequence`: un campo específico utilizado para indicar cómo esta entrada está bloqueada por tiempo, así como otras opciones como RBF.