---
term: NÓ PODADO
---

Um nó podado, em inglês "Pruned Node", é um nó completo que realiza a poda da blockchain. Isso envolve remover progressivamente os blocos mais antigos, após tê-los devidamente verificados, para manter apenas os blocos mais recentes. O limite de retenção é especificado no arquivo `bitcoin.conf` por meio do parâmetro `prune=n`, onde `n` é o tamanho máximo ocupado pelos blocos em megabytes (MB). Se `0` for indicado após este parâmetro, então a poda está desativada, e o nó retém a blockchain em sua totalidade.

Nós podados são, às vezes, considerados como tipos diferentes de nós em relação aos nós completos. O uso de um nó podado pode ser particularmente interessante para usuários enfrentando restrições de capacidade de armazenamento. Atualmente, um nó completo deve ter quase 600 GB apenas para armazenar a blockchain. Um nó podado pode limitar o armazenamento necessário para até 550 MB. Embora use menos espaço em disco, um nó podado mantém um nível de verificação e validação semelhante ao de um nó completo. Portanto, nós podados oferecem mais confiança aos seus usuários em comparação com nós leves (SPV).