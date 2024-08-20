---
termo: SWEEP TRANSACTION
---

Modelo de padrão ou transação usado na análise de cadeias para determinar a natureza da transação. Este modelo é caracterizado pelo consumo de um único UTXO como entrada e a produção de um único UTXO como saída. A interpretação deste modelo é que estamos na presença de uma auto-transferência. O usuário transferiu seus bitcoins para si mesmo, para outro endereço que possui. Como não há troco na transação, é muito improvável que estejamos lidando com um pagamento. De fato, quando um pagamento é feito, é quase impossível para o pagador ter um UTXO que corresponda exatamente ao montante exigido pelo vendedor, além das taxas de transação. Geralmente, o pagador é, portanto, forçado a produzir uma saída de troco. Então sabemos que o usuário observado provavelmente ainda está na posse deste UTXO. No contexto de uma análise de cadeia, se sabemos que o UTXO usado como entrada na transação pertence a Alice, podemos assumir que o UTXO em saída também pertence a ela.

![](../../dictionnaire/assets/6.png)

> ► *Em francês, "sweep transaction" poderia ser traduzido como "transaction de balayage".*