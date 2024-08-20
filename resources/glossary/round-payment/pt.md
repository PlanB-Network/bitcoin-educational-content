---
termo: PAGAMENTO ARREDONDADO
---

Uma heurística interna para análise de cadeias no Bitcoin que permite formular uma hipótese sobre a natureza das saídas de uma transação baseada em quantias arredondadas. Geralmente, quando confrontado com um padrão de pagamento simples (1 entrada e 2 saídas), se uma das saídas gasta uma quantia arredondada, então ela representa o pagamento. Por eliminação, se uma saída representa o pagamento, a outra representa o troco. Pode-se, portanto, interpretar que é provável que o usuário que inseriu a transação ainda possua a saída identificada como sendo o troco.

Deve-se notar que essa heurística nem sempre é aplicável, já que a maioria dos pagamentos ainda é feita em unidades de moeda fiduciária. De fato, quando um comerciante na França aceita bitcoin, geralmente, eles não exibem preços estáveis em sats. Eles prefeririam optar por uma conversão entre o preço em euros e a quantidade em bitcoins a ser paga através de seu POS (como o BTCPay Server, por exemplo). Portanto, não deveria haver um número arredondado na saída da transação. No entanto, um analista poderia tentar fazer essa conversão levando em conta a taxa de câmbio vigente quando a transação foi transmitida na rede. Se um dia, o bitcoin se tornar a unidade de conta preferida em nossas trocas, essa heurística poderia se tornar ainda mais útil para análises.

![](../../dictionnaire/assets/11.png)