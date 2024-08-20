---
termo: MALLEABILITY (TRANSAÇÃO)
---

Refere-se à capacidade de modificar ligeiramente a estrutura de uma transação Bitcoin, sem alterar seu efeito, mas enquanto muda o identificador da transação (*TXID*). Esta propriedade pode ser explorada maliciosamente para enganar os interessados sobre o status de uma transação, causando assim problemas como o duplo gasto. A maleabilidade foi possibilitada pela flexibilidade da assinatura digital usada. O soft fork SegWit foi introduzido notavelmente para prevenir essa maleabilidade das transações Bitcoin, tornando a implementação da Lightning Network complicada. Ele alcança isso removendo os dados maleáveis da transação do cálculo do TXID.

> ► *Embora raro, o termo "mutabilidade" às vezes é usado para se referir ao mesmo conceito.*