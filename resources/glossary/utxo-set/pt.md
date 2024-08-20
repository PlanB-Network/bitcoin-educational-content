---
term: UTXO SET
---

Refere-se ao conjunto de todos os UTXOs existentes em um determinado momento. Em outras palavras, é uma grande lista de todas as diferentes partes de bitcoins esperando para serem gastas. Se você somar os montantes de todos os UTXOs no conjunto UTXO, isso nos dá a massa monetária total de bitcoins em circulação. Cada nó na rede Bitcoin mantém seu próprio conjunto UTXO em tempo real. Ele atualiza conforme novos blocos válidos são confirmados, com as transações que eles incluem, que consomem alguns UTXOs do conjunto UTXO e criam novos em retorno.

Este conjunto UTXO é mantido por cada nó para verificar rapidamente se os UTXOs gastos nas transações são de fato legítimos. Isso permite que eles detectem e rejeitem tentativas de duplo gasto. O conjunto UTXO está frequentemente no centro das preocupações sobre a descentralização do Bitcoin, pois seu tamanho naturalmente aumenta muito rapidamente. Uma vez que uma parte dele deve ser mantida em RAM para verificar transações em um tempo razoável, o conjunto UTXO poderia gradualmente tornar a operação de um nó completo muito custosa. O conjunto UTXO também tem um impacto significativo no IBD (*Initial Block Download*). Quanto mais do conjunto UTXO puder ser colocado em RAM, mais rápido é o IBD. No Bitcoin Core, o conjunto UTXO é armazenado na pasta denominada `/chainstate`.

> ► *Em inglês, "UTXO set" poderia ser traduzido como "conjunto UTXO".*