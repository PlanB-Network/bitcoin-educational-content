---
term: BIP141
---

Introduziu o conceito de Segregated Witness (SegWit), que deu nome ao soft fork SegWit. O BIP141 introduz uma modificação importante no protocolo Bitcoin com o objetivo de resolver o problema da maleabilidade das transações. O SegWit separa os dados de testemunha (dados de assinatura) do restante dos dados da transação. Essa separação é alcançada inserindo as testemunhas em uma estrutura de dados separada, comprometida em uma nova árvore de Merkle, que por sua vez é referenciada no bloco via a transação coinbase, tornando o SegWit compatível com versões mais antigas do protocolo.