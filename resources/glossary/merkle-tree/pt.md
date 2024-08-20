---
term: MERKLE TREE
---

Uma Merkle Tree é um acumulador criptográfico. É um método para provar a pertença de uma determinada informação dentro de um conjunto maior. É uma estrutura de dados que facilita a verificação de informações em um formato compacto. No sistema Bitcoin, as Merkle Trees são usadas para agrupar e condensar as transações de um bloco em um único hash, chamado de Merkle Root (ou "*Root Hash*"). Cada transação é hasheada, depois os hashes adjacentes são hasheados juntos hierarquicamente até que o Merkle Root seja obtido.

![](../../dictionnaire/assets/1.png)

Esta estrutura permite a rápida verificação de se uma transação específica está incluída em um dado bloco sem ter que analisar todas as transações. Por exemplo, se eu tenho apenas o Merkle Root e quero verificar que a `TX 7` é de fato parte da árvore, eu precisaria apenas das seguintes provas:
* `TX 7`;
* `HASH 8`;
* `HASH 5-6`;
* `HASH 1-2-3-4`.
Com essas peças de informação, sou capaz de calcular os nós intermediários até o Merkle Root.

![](../../dictionnaire/assets/2.png)

As Merkle Trees são notavelmente usadas para nós leves (conhecidos como "SPV") que mantêm apenas os cabeçalhos dos blocos, mas não as transações. Esta estrutura também é encontrada no protocolo UTREEXO, um protocolo que permite a condensação do conjunto UTXO dos nós, e no MAST Taproot.

> ► *A Merkle Tree é nomeada em homenagem a Ralph Merkle, um criptógrafo que projetou esta estrutura em 1979. Uma Merkle Tree também pode ser chamada de "árvore de hash". Em francês, é referida como "Arbre de Merkle" ou "arbre de hachage".*