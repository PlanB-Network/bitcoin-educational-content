---
term: UTREEXO

---
Protocolo concebido por Tadge Dryja para compactar o conjunto UTXO dos nós Bitcoin utilizando um acumulador baseado em árvores Merkle. Ao contrário do conjunto UTXO clássico, que requer um espaço de armazenamento significativo, o Utreexo reduz drasticamente a memória necessária, armazenando apenas as raízes da árvore Merkle. Isto permite ao nó verificar a existência de UTXOs utilizados nas entradas da transação, sem ter de manter o conjunto completo de UTXOs. Ao usar o Utreexo, cada nó retém apenas uma impressão digital criptográfica chamada raiz de Merkle. Quando é feita uma transação, o utilizador fornece as provas de propriedade dos UTXOs e os caminhos de Merkle correspondentes. Assim, o nó pode verificar as transacções sem armazenar todo o conjunto de UTXOs. Vejamos um exemplo com um diagrama para compreender este mecanismo:

![](../../dictionnaire/assets/15.webp)

Neste exemplo, reduzi intencionalmente o conjunto de UTXOs para 4 UTXOs para facilitar a compreensão. Na realidade, é importante imaginar que existem quase 140 milhões de UTXOs no Bitcoin no momento em que escrevo estas linhas. Neste diagrama, o nó Utreexo só precisaria manter o Merkle Root na RAM. Se receber uma transação gastando o UTXO nº 3 (a preto), a prova consistiria nos seguintes elementos:


- UTXO 3;
- HASH 4;
- HASH 1-2.

Com esta informação transmitida pelo remetente da transação, o nó Utreexo efectua as seguintes verificações:


- Calcula a impressão do UTXO 3, o que lhe dá o HASH 3;
- Concatena o HASH 3 com o HASH 4;
- Calcula a sua impressão, o que lhe dá um HASH 3-4;
- Concatena o HASH 3-4 com o HASH 1-2;
- Calcula a sua impressão, o que lhe dá a raiz de Merkle.

Se a raiz de Merkle que obtém através do seu processo for a mesma que a raiz de Merkle que armazenou na sua RAM, então está convencido de que o UTXO n.º 3 faz efetivamente parte do conjunto UTXO.

Este método reduz os requisitos de RAM para operadores de nós completos. No entanto, o Utreexo tem limitações, incluindo um aumento do tamanho do bloco devido a provas adicionais e a potencial dependência dos nós Utreexo dos nós Bridge para obter as provas em falta. Os nós de ponte são nós completos tradicionais que fornecem as provas necessárias aos nós Utreexo, permitindo assim uma verificação completa. Esta abordagem oferece um compromisso entre eficiência e descentralização, tornando a validação de transacções mais acessível a utilizadores com recursos limitados.