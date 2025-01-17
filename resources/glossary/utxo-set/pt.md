---
term: UTXO SET

---
Refere-se à coleção de todos os UTXOs existentes num dado momento. Por outras palavras, é uma grande lista de todas as diferentes peças de bitcoins à espera de serem gastas. Se somarmos os montantes de todos os UTXOs no conjunto UTXO, obtemos a massa monetária total de bitcoins em circulação. Cada nó da rede Bitcoin mantém o seu próprio conjunto de UTXOs em tempo real. Actualiza-o à medida que novos blocos válidos são confirmados, com as transacções que incluem, que consomem alguns UTXOs do conjunto UTXO, e criam novos em troca.

Este conjunto de UTXOs é mantido por cada nó para verificar rapidamente se os UTXOs gastos nas transacções são de facto legítimos. Isto permite-lhes detetar e rejeitar tentativas de gasto duplo. O conjunto de UTXOs está frequentemente no centro das preocupações sobre a descentralização do Bitcoin, pois seu tamanho naturalmente aumenta muito rapidamente. Uma vez que uma parte dele deve ser mantida na RAM para verificar as transações em um tempo razoável, o conjunto UTXO poderia gradualmente tornar a operação de um nó completo muito cara. O conjunto UTXO também tem um impacto significativo no IBD (*Initial Block Download*). Quanto mais do conjunto UTXO pode ser colocado na RAM, mais rápido é o IBD. No Bitcoin Core, o conjunto UTXO é armazenado na pasta chamada `/chainstate`.

> ► *Em inglês, "UTXO set" poderia ser traduzido como "conjunto UTXO"