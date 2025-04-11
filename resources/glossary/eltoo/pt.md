---
term: ELTOO

---
Um protocolo geral para as segundas camadas do Bitcoin que define como gerir conjuntamente a propriedade de um UTXO. O Eltoo foi concebido por Christian Decker, Rusty Russell e Olaoluwa Osuntokun, nomeadamente para resolver os problemas associados aos mecanismos de negociação dos estados do canal Lightning, ou seja, entre a abertura e o fecho. A arquitetura Eltoo simplifica o processo de negociação através da introdução de um sistema de gestão linear de estados, substituindo a abordagem baseada em penalizações estabelecida por um método de atualização mais flexível e menos punitivo. Este protocolo requer a utilização de um novo tipo de SigHash que permite ignorar todas as entradas na assinatura de uma transação. Este SigHash foi inicialmente designado por `SIGHASH_NOINPUT` e depois por `SIGHASH_ANYPREVOUT` (*Any Previous Output*). A sua implementação está planeada no BIP118.

> ► *Eltoo é por vezes também designado por "LN-Symmetry"