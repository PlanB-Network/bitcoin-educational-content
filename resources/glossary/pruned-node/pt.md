---
term: NÓ PODADO

---
Um nó podado, em inglês "Pruned Node", é um nó completo que efectua a poda da cadeia de blocos. Isso envolve a remoção progressiva dos blocos mais antigos, depois de devidamente verificados, para manter apenas os blocos mais recentes. O limite de retenção é especificado no arquivo `bitcoin.conf` através do parâmetro `prune=n`, onde `n` é o tamanho máximo ocupado pelos blocos em megabytes (MB). Se `0` for anotado após este parâmetro, então a poda é desabilitada e o nó retém a blockchain em sua totalidade.

Os nós podados são por vezes considerados como tipos de nós diferentes dos nós completos. A utilização de um nó podado pode ser particularmente interessante para os utilizadores que enfrentam restrições de capacidade de armazenamento. Atualmente, um nó completo deve ter quase 600 GB apenas para armazenar a blockchain. Um nó podado pode limitar o armazenamento necessário a até 550 MB. Embora utilize menos espaço em disco, um nó podado mantém um nível de verificação e validação semelhante ao de um nó completo. Os nós podados oferecem, portanto, mais confiança aos seus utilizadores em comparação com os nós leves (SPV).