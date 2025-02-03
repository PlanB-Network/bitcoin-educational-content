---
term: VOUT

---
Elemento específico de una transacción Bitcoin que determina el destino de los fondos enviados. Una transacción puede incluir múltiples salidas, cada una identificada de forma única por la combinación del identificador de transacción (`txid`) y un índice llamado `vout`. Este índice, que comienza en `0`, marca la posición de la salida en la secuencia de salidas de la transacción. Así, la primera salida será designada por `"vout 0`, la segunda por `"vout": 1`, y así sucesivamente.

Cada "salida" contiene principalmente dos informaciones:


- el valor, expresado en bitcoins, que representa la cantidad enviada;
- un script de bloqueo (`scriptPubKey`) que estipula las condiciones necesarias para que los fondos puedan volver a gastarse en una transacción futura.

La combinación del `txid` y el `vout` de una pieza concreta forma lo que se denomina un UTXO, por ejemplo:

```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```