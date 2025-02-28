---
term: TRANSACÇÃO DE VARRIMENTO

---
Modelo de padrão ou transação utilizado na análise da cadeia para determinar a natureza da transação. Este modelo é caracterizado pelo consumo de um único UTXO como entrada e pela produção de um único UTXO como saída. A interpretação deste modelo é que estamos na presença de uma auto-transferência. O utilizador transferiu os seus bitcoins para si próprio, para outro endereço que possui. Uma vez que não há qualquer alteração na transação, é muito improvável que estejamos perante um pagamento. De facto, quando um pagamento é feito, é quase impossível que o pagador tenha um UTXO que corresponda exatamente ao montante exigido pelo vendedor, para além das taxas de transação. Geralmente, o pagador é, portanto, forçado a produzir uma saída de mudança. Sabemos então que o utilizador observado ainda está provavelmente na posse deste UTXO. No contexto de uma análise em cadeia, se soubermos que o UTXO utilizado como entrada na transação pertence a Alice, podemos assumir que o UTXO na saída também lhe pertence.

![](../../dictionnaire/assets/6.webp)

> ► *Em francês, "sweep transaction" pode ser traduzido como "transaction de balayage"