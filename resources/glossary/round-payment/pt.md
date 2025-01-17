---
term: PAGAMENTO POR VOLTA

---
Uma heurística interna para análise de cadeias em Bitcoin que permite uma hipótese sobre a natureza dos outputs de uma transação com base em montantes redondos. Geralmente, quando confrontado com um padrão de pagamento simples (1 entrada e 2 saídas), se uma das saídas gasta um montante redondo, então representa o pagamento. Por eliminação, se uma saída representa o pagamento, a outra representa o troco. Pode, portanto, interpretar-se que é provável que o utilizador que introduziu a transação ainda possua o output identificado como sendo o troco.

Note-se que esta heurística nem sempre é aplicável, uma vez que a maioria dos pagamentos continua a ser efectuada em unidades monetárias fiduciárias. Com efeito, quando um comerciante em França aceita bitcoin, geralmente não apresenta preços estáveis em sats. Preferem optar por uma conversão entre o preço em euros e o montante em bitcoins a pagar através do seu POS (como o BTCPay Server, por exemplo). Portanto, não deve haver um número redondo no resultado da transação. No entanto, um analista pode tentar fazer esta conversão tendo em conta a taxa de câmbio em vigor quando a transação foi transmitida na rede. Se, um dia, o bitcoin se tornar a unidade de conta preferida nas nossas bolsas, esta heurística poderá tornar-se ainda mais útil para as análises.

![](../../dictionnaire/assets/11.webp)