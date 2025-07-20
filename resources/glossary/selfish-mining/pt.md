---
term: SELFISH Mining
---

Estratégia (ou ataque) no Mining, em que um Miner ou um grupo de mineiros retém intencionalmente blocos com um Proof of Work válido sem os libertar imediatamente para a rede. O objetivo é manter-se à frente dos outros mineiros em termos de Proof of Work, permitindo-lhes potencialmente Miner vários blocos seguidos e publicá-los todos de uma só vez, maximizando assim os seus ganhos. Por outras palavras, o grupo de mineiros atacantes não minera no último bloco validado por toda a rede, mas sim num bloco que eles próprios criaram e que é diferente do validado pela rede.


Este processo gera uma espécie de ramo secreto do Blockchain, que permanece desconhecido de toda a rede até que esta cadeia alternativa exceda potencialmente o Blockchain honesto. Quando a cadeia secreta dos mineiros atacantes se torna mais longa (ou seja, contém mais trabalho acumulado) do que a cadeia pública honesta, é então transmitida para toda a rede. Nesta altura, os nós da rede que seguem a cadeia mais longa (com mais trabalho acumulado) sincronizar-se-ão com esta nova cadeia. Portanto, há uma reorganização.


O egoísmo Mining é incómodo para os utilizadores, pois reduz a segurança do sistema ao desperdiçar parte do poder de computação da rede. Se for bem sucedido, também leva a reorganizações Blockchain, afectando a fiabilidade das confirmações de transacções para os utilizadores. Ainda assim, esta prática continua a ser arriscada para o grupo atacante de mineiros, uma vez que é frequentemente mais rentável fazer um Miner normalmente acima do último bloco conhecido publicamente do que atribuir poder de computação a um ramo secreto que provavelmente nunca excederá o Blockchain honesto. Quanto maior for o número de blocos na reorganização, menor será a probabilidade de um ataque bem sucedido.