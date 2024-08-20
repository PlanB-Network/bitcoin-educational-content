---
termo: SIMPLE PAYMENT
---

Padrão de transação (ou modelo) usado em análise de cadeias caracterizado pelo consumo de um ou mais UTXOs nas entradas e a produção de 2 UTXOs nas saídas. Este modelo, portanto, se parecerá com isto:

![](../../dictionnaire/assets/5.png)

Este modelo de pagamento simples indica que provavelmente estamos na presença de uma transação de envio ou pagamento. O usuário consumiu seu próprio UTXO nas entradas para satisfazer nas saídas um UTXO de pagamento e um UTXO de troco (troco retornado ao mesmo usuário). Portanto, sabemos que o usuário observado provavelmente não está mais na posse de um dos dois UTXOs nas saídas (o de pagamento), mas eles ainda estão na posse do outro UTXO (o de troco).