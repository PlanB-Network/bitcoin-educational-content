---
term: Árvore de Merkle

definition: Estrutura de dados hierárquica que permite verificar rapidamente a inclusão de uma transação num bloco.
---
Uma árvore de Merkle é um acumulador criptográfico. É um método para provar a pertença de uma determinada informação a um conjunto maior. É uma estrutura de dados que facilita a verificação de informações num formato compacto. No sistema Bitcoin, as árvores de Merkle são usadas para agrupar e condensar as transações de um bloco em um único hash, chamado Merkle Root (ou "*Root Hash*"). Cada transação é submetida a um hash e, em seguida, os hashes adjacentes são submetidos a um hash hierárquico até se obter a Merkle Root.



Esta estrutura permite verificar rapidamente se uma transação específica está incluída num determinado bloco sem ter de analisar todas as transacções. Por exemplo, se eu tiver apenas a Raiz de Merkle e quiser verificar que `TX 7` faz de facto parte da árvore, só preciso das seguintes provas:


- `TX 7`;
- `HASH 8`;
- `HASH 5-6`;
- `HASH 1-2-3-4`.

Com estas informações, posso calcular os nós intermédios até à raiz de Merkle.



As árvores de Merkle são utilizadas nomeadamente para os nós leves (conhecidos como "SPV") que apenas conservam os cabeçalhos dos blocos, mas não as transacções. Esta estrutura também é encontrada no protocolo UTREEXO, um protocolo que permite a condensação do conjunto de nós UTXO, e no MAST Taproot.

