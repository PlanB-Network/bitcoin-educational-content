---
term: EXTRA-Nonce
---

Campo utilizado no `scriptSig` do Coinbase Transaction de um bloco, que permite testar um maior número de possibilidades para obter um Hash inferior ao objetivo de dificuldade, para além do Nonce clássico, que se encontra diretamente no cabeçalho de cada bloco.


A modificação do extra-Nonce no Coinbase Transaction altera o identificador desta transação e, por conseguinte, o Merkle Root de todas as transacções do bloco, o que também modifica o cabeçalho do bloco. Isto permite que o Miner continue a procurar hashes quando o alcance do Nonce clássico já estiver esgotado, sem alterar a estrutura do seu bloco candidato.


Nos pools Mining, o extra-Nonce é frequentemente dividido em duas partes: uma gerada pelo pool para identificar cada chopper, e outra modificada pelo chopper em busca de uma partilha válida. Isto permite que os diferentes choppers do agrupamento trabalhem simultaneamente no mesmo bloco candidato com toda a gama de nonces, sem duplicar o mesmo trabalho a nível do agrupamento.