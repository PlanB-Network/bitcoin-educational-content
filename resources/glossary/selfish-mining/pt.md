---
term: SELFISH MINING
---

Estratégia (ou ataque) na mineração, onde um minerador ou um grupo de mineradores intencionalmente mantém blocos com uma prova de trabalho válida sem imediatamente transmiti-los para a rede. O objetivo é manter uma vantagem sobre outros mineradores em termos de prova de trabalho, o que potencialmente permite que eles minem vários blocos em sequência e os publiquem todos de uma vez, maximizando assim seus ganhos.

Em outras palavras, o grupo de mineradores atacante não minera no último bloco validado por toda a rede, mas sim em um bloco que eles mesmos criaram, o qual difere daquele validado pela rede. Esse processo gera uma espécie de bifurcação secreta da blockchain, que permanece desconhecida para toda a rede até que essa cadeia alternativa potencialmente supere a blockchain honesta. Uma vez que a cadeia secreta dos mineradores atacantes se torna mais longa (ou seja, contém mais trabalho acumulado) do que a cadeia honesta e pública, ela é então transmitida para toda a rede. Nesse ponto, os nós da rede, que seguem a cadeia mais longa (com o maior trabalho acumulado), sincronizarão com esta nova cadeia. Isso resulta em uma reorganização.

O selfish mining é problemático porque diminui a segurança do sistema ao desperdiçar parte do poder computacional da rede. Se bem-sucedido, também leva a reorganizações da blockchain, afetando assim a confiabilidade das confirmações de transações para os usuários. Esta prática permanece arriscada para o grupo de mineradores atacantes, pois muitas vezes é mais lucrativo minerar normalmente no último bloco conhecido publicamente em vez de alocar poder computacional para uma bifurcação secreta que provavelmente nunca superará a blockchain honesta. Quanto maior o número de blocos na reorganização, menor a probabilidade de sucesso do ataque.

> ► *A tradução em inglês de "minage égoïste" é "selfish mining". Note-se que um ataque de selfish mining não deve ser confundido com um ataque de retenção de blocos.*