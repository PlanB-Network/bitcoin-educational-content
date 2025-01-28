---
term: VOUT

---
Um elemento específico de uma transação Bitcoin que determina o destino dos fundos enviados. Uma transação pode incluir múltiplos outputs, cada um identificado exclusivamente pela combinação do identificador da transação (`txid`) e um índice chamado `vout`. Este índice, que começa em `0`, marca a posição da saída na sequência de saídas da transação. Assim, a primeira saída será designada por `"vout": 0`, a segunda por `"vout": 1`, e assim por diante.

Cada `vout` contém principalmente duas informações:


- o valor, expresso em bitcoins, que representa o montante enviado;
- um script de bloqueio (`scriptPubKey`) que estipula as condições necessárias para que os fundos possam ser gastos novamente numa transação futura.

A combinação do `txid` e do `vout` de uma peça específica forma o que é chamado de UTXO, por exemplo:

```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```