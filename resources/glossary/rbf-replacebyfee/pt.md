---
term: RBF (REPLACE-BY-FEE)

---
Um mecanismo transacional que permite ao remetente substituir uma transação por outra pagando taxas mais elevadas, de forma a acelerar a sua confirmação. Se uma transação com taxas demasiado baixas ficar bloqueada, o remetente pode usar *Replace-By-Fee* para aumentar as taxas e dar prioridade à sua transação de substituição nos mempools.

RBF é aplicável enquanto a transação estiver nos mempools; uma vez num bloco, ela não pode mais ser substituída. No envio inicial, a transação deve especificar sua disponibilidade para ser substituída ajustando o valor `nSequence` para um número menor que `0xfffffffe`. Este valor é conhecido como "flag" RBF. Esta definição assinala a possibilidade de atualizar a transação depois de esta ter sido transmitida, o que permite subsequentemente uma RBF. No entanto, é por vezes possível substituir uma transação que não tenha sinalizado RBF. Os nós que utilizam o parâmetro de configuração `mempoolfullrbf=1` aceitam esta substituição mesmo que a RBF não tenha sido inicialmente sinalizada.

Ao contrário do CPFP (*Child Pays For Parent*), em que o destinatário pode agir para acelerar a transação, o RBF (*Replace-By-Fee*) permite que o remetente tome a iniciativa de acelerar a sua própria transação aumentando as taxas.