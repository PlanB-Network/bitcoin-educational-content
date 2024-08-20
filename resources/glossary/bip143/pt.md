---
termo: BIP143
---

Introduz uma nova maneira de realizar o hash da transação para verificação de assinatura em scripts pós-SegWit. O objetivo é minimizar operações redundantes durante a verificação e incluir o valor dos UTXOs na entrada na assinatura. Isso resolve dois problemas principais com o algoritmo original de hash de transação:
* O crescimento quadrático do hash de dados com o número de assinaturas;
* A ausência da inclusão do valor de entrada na assinatura, o que representava um risco para as carteiras de hardware, especialmente em relação ao conhecimento das taxas de transação incorridas.
Desde a atualização do SegWit, explicada no BIP141, que introduz uma nova forma de transações cujo script não será verificado por nós antigos, o BIP143 aproveita esta oportunidade para abordar essa questão sem a necessidade de um hard fork. Portanto, o BIP143 faz parte do soft fork do SegWit.