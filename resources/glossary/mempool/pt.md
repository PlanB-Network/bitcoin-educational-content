---
term: MEMPOOL

---
Uma contração dos termos "memory" e "pool". Refere-se a um espaço virtual no qual as transacções Bitcoin que aguardam inclusão num bloco são agrupadas. Quando uma transação é criada e transmitida na rede Bitcoin, é primeiro verificada pelos nós da rede. Se for considerada válida, é então colocada no Mempool de cada nó, onde permanece até ser selecionada por um mineiro para ser incluída num bloco.

É importante notar que cada nó na rede Bitcoin mantém seu próprio Mempool, e, portanto, pode haver variações no conteúdo do Mempool entre diferentes nós a qualquer momento. Notavelmente, o parâmetro `maxmempool` no ficheiro `bitcoin.conf` de cada nó permite aos operadores controlar a quantidade de RAM (memória de acesso aleatório) que o seu nó irá utilizar para armazenar transacções pendentes no Mempool. Ao limitar o tamanho do Mempool, os operadores do nó podem evitar que ele consuma muitos recursos em seu sistema. Este parâmetro é especificado em megabytes (MB). O valor padrão para o Bitcoin Core até o momento é 300 MB.

As transacções presentes no Mempool são provisórias. Não devem ser consideradas imutáveis até serem incluídas num bloco, e após um certo número de confirmações. Estas podem ser substituídas ou eliminadas.