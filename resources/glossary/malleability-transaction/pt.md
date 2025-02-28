---
term: MALEABILIDADE (TRANSACÇÃO)

---
Refere-se à capacidade de modificar ligeiramente a estrutura de uma transação Bitcoin, sem alterar o seu efeito, mas alterando o identificador da transação (*TXID*). Esta propriedade pode ser explorada de forma maliciosa para enganar as partes interessadas sobre o estado de uma transação, causando assim problemas como gastos duplos. A maleabilidade foi possível graças à flexibilidade da assinatura digital utilizada. O soft fork SegWit foi introduzido nomeadamente para evitar esta maleabilidade das transacções Bitcoin, tornando a implementação da Lightning Network complicada. Consegue-o removendo os dados maleáveis da transação do cálculo do TXID.

> ► *Embora seja raro, o termo "mutabilidade" é por vezes utilizado para designar o mesmo conceito.*