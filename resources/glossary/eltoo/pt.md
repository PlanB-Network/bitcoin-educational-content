---
term: ELTOO
---

Um protocolo geral para as segundas camadas do Bitcoin que define como gerenciar conjuntamente a propriedade de um UTXO. Eltoo foi projetado por Christian Decker, Rusty Russell e Olaoluwa Osuntokun, especialmente para resolver os problemas associados aos mecanismos de negociação dos estados de canais do Lightning, isto é, entre a abertura e o fechamento. A arquitetura Eltoo simplifica o processo de negociação ao introduzir um sistema de gestão de estados linear, substituindo a abordagem baseada em penalidades estabelecida por um método de atualização mais flexível e menos punitivo. Este protocolo requer o uso de um novo tipo de SigHash que permite ignorar todas as entradas na assinatura de uma transação. Esse SigHash foi inicialmente chamado de `SIGHASH_NOINPUT`, depois `SIGHASH_ANYPREVOUT` (*Qualquer Saída Anterior*). Sua implementação está planejada no BIP118.

> ► *Eltoo é às vezes também referido como "LN-Symmetry".*