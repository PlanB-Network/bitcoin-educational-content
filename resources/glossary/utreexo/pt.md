---
term: UTREEXO
---

Protocolo projetado por Tadge Dryja para compactar o conjunto de UTXOs dos nós do Bitcoin usando um acumulador baseado em árvores de Merkle. Diferentemente do conjunto de UTXOs clássico, que requer um espaço de armazenamento significativo, o Utreexo reduz drasticamente a memória necessária armazenando apenas as raízes da árvore de Merkle. Isso permite que o nó verifique a existência de UTXOs usados em entradas de transações, sem ter que manter o conjunto completo de UTXOs. Ao usar o Utreexo, cada nó retém apenas uma impressão digital criptográfica chamada raiz de Merkle. Quando uma transação é feita, o usuário fornece as provas de propriedade dos UTXOs e os caminhos de Merkle correspondentes. Assim, o nó pode verificar transações sem armazenar o conjunto inteiro de UTXOs. Vamos tomar um exemplo com um diagrama para entender este mecanismo:

![](../../dictionnaire/assets/15.png)

Neste exemplo, reduzi intencionalmente o conjunto de UTXOs para 4 UTXOs para facilitar a compreensão. Na realidade, é importante imaginar que existem quase 140 milhões de UTXOs no Bitcoin no momento de escrever estas linhas. Neste diagrama, o nó Utreexo só precisaria manter a Raiz de Merkle na RAM. Se ele recebe uma transação que gasta o UTXO No. 3 (em preto), a prova consistiria nos seguintes elementos:
* UTXO 3;
* HASH 4;
* HASH 1-2.

Com esta informação transmitida pelo remetente da transação, o nó Utreexo realiza as seguintes verificações:
* Ele calcula a impressão do UTXO 3, o que lhe dá o HASH 3;
* Ele concatena o HASH 3 com o HASH 4;
* Ele calcula a impressão deles, o que lhe dá o HASH 3-4;
* Ele concatena o HASH 3-4 com o HASH 1-2;
* Ele calcula a impressão deles, o que lhe dá a raiz de Merkle.

Se a raiz de Merkle que obtém através de seu processo é a mesma que a raiz de Merkle armazenada em sua RAM, então ele está convencido de que o UTXO No. 3 faz realmente parte do conjunto de UTXOs.
Este método reduz os requisitos de RAM para operadores de nós completos. No entanto, o Utreexo tem limitações, incluindo um aumento no tamanho do bloco devido a provas adicionais e a dependência potencial de nós Utreexo em Bridge Nodes para obter provas faltantes. Bridge Nodes são nós completos tradicionais que fornecem as provas necessárias para nós Utreexo, permitindo assim a verificação completa. Esta abordagem oferece um compromisso entre eficiência e descentralização, tornando a validação de transações mais acessível para usuários com recursos limitados.