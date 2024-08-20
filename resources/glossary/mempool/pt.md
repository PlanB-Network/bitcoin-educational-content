---
term: MEMPOOL
---

Uma contração dos termos "memory" (memória) e "pool" (piscina, conjunto). Refere-se a um espaço virtual no qual transações de Bitcoin que aguardam inclusão em um bloco são agrupadas. Quando uma transação é criada e transmitida na rede Bitcoin, ela é primeiro verificada pelos nós da rede. Se for considerada válida, é então colocada no Mempool de cada nó, onde permanece até ser selecionada por um minerador para ser incluída em um bloco.

É importante notar que cada nó na rede Bitcoin mantém seu próprio Mempool, e, portanto, pode haver variações no conteúdo do Mempool entre diferentes nós em qualquer momento dado. Notavelmente, o parâmetro `maxmempool` no arquivo `bitcoin.conf` de cada nó permite que os operadores controlem a quantidade de RAM (memória de acesso aleatório) que seu nó usará para armazenar transações pendentes no Mempool. Ao limitar o tamanho do Mempool, os operadores de nós podem impedir que ele consuma muitos recursos em seu sistema. Este parâmetro é especificado em megabytes (MB). O valor padrão para o Bitcoin Core até o momento é de 300 MB.

Transações presentes no Mempool são provisórias. Elas não devem ser consideradas imutáveis até que sejam incluídas em um bloco e após um certo número de confirmações. Estas podem frequentemente ser substituídas ou purgadas.