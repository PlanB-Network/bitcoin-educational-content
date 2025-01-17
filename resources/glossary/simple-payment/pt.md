---
term: PAGAMENTO SIMPLES

---
Padrão (ou modelo) de transação utilizado na análise da cadeia caracterizado pelo consumo de um ou mais UTXOs nos inputs e pela produção de 2 UTXOs nos outputs. Este modelo terá, portanto, o seguinte aspeto:

![](../../dictionnaire/assets/5.webp)

Este modelo simples de pagamento indica que estamos provavelmente na presença de uma transação de envio ou de pagamento. O utilizador consumiu o seu próprio UTXO nos inputs para satisfazer nos outputs um UTXO de pagamento e um UTXO de troco (troco devolvido ao mesmo utilizador). Sabemos, portanto, que o utilizador observado já não está provavelmente na posse de um dos dois UTXOs nas saídas (o de pagamento), mas ainda está na posse do outro UTXO (o de troco).