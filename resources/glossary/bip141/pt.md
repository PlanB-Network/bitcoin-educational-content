---
term: BIP141

---
Introduziu o conceito de Segregated Witness (SegWit) que deu nome ao soft fork SegWit. O BIP141 introduz uma grande modificação no protocolo Bitcoin com o objetivo de resolver o problema da maleabilidade das transacções. O SegWit separa a testemunha (dados de assinatura) do resto dos dados da transação. Esta separação é conseguida através da inserção das testemunhas numa estrutura de dados separada, comprometida numa nova árvore Merkle, que é ela própria referenciada no bloco através da transação coinbase, tornando o SegWit compatível com versões mais antigas do protocolo.