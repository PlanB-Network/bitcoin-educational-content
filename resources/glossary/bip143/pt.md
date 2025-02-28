---
term: BIP143

---
Introduz uma nova maneira de fazer o hashing da transação para verificação de assinatura em scripts pós-SegWit. O objetivo é minimizar as operações redundantes durante a verificação e incluir o valor dos UTXOs na entrada da assinatura. Isso resolve dois grandes problemas com o algoritmo de hashing de transação original:


- O crescimento quadrático do hashing de dados com o número de assinaturas;
- A ausência de inclusão do valor de entrada na assinatura, o que representava um risco para as carteiras de hardware, especialmente no que diz respeito ao conhecimento das taxas de transação incorridas.

Uma vez que a atualização SegWit, explicada na BIP141, introduz uma nova forma de transacções cujo script não será verificado pelos nós antigos, a BIP143 aproveita esta oportunidade para resolver este problema sem exigir um hard fork. Portanto, o BIP143 faz parte do soft fork SegWit.