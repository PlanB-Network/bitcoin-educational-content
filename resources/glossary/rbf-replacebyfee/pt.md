---
termo: RBF (REPLACE-BY-FEE)
---

Um mecanismo transacional que permite ao remetente substituir uma transação por outra, pagando taxas mais altas, a fim de acelerar sua confirmação. Se uma transação com taxas muito baixas fica presa, o remetente pode usar *Replace-By-Fee* para aumentar as taxas e priorizar sua transação de substituição nos mempools.

O RBF é aplicável enquanto a transação estiver nos mempools; uma vez em um bloco, ela não pode mais ser substituída. No envio inicial, a transação deve especificar sua disponibilidade para ser substituída ajustando o valor `nSequence` para um número menor que `0xfffffffe`. Isso é conhecido como uma "bandeira" RBF. Essa configuração sinaliza a possibilidade de atualizar a transação após ela ter sido transmitida, o que subsequentemente permite um RBF. No entanto, às vezes é possível substituir uma transação que não sinalizou RBF. Nós usando o parâmetro de configuração `mempoolfullrbf=1` aceitam essa substituição mesmo que o RBF não tenha sido inicialmente sinalizado.

Ao contrário do CPFP (*Child Pays For Parent*), onde o destinatário pode agir para acelerar a transação, o RBF (*Replace-By-Fee*) permite que o remetente tome a iniciativa de acelerar sua própria transação aumentando as taxas.