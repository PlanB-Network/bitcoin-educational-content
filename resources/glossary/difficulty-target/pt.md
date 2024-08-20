---
term: OBJETIVO DE DIFICULDADE
---

O fator de dificuldade, também conhecido como objetivo de dificuldade, é um parâmetro usado no mecanismo de consenso por prova de trabalho (Proof of Work, PoW) no Bitcoin. O objetivo representa um valor numérico que determina a dificuldade para os mineradores resolverem um problema criptográfico específico, chamado prova de trabalho, ao criar um novo bloco na blockchain.

O objetivo de dificuldade é um número ajustável de 256 bits (64 bytes) que determina um limite de aceitabilidade para o hashing de cabeçalhos de blocos. Em outras palavras, para que um bloco seja válido, o hash de seu cabeçalho com `SHA256d` (duplo `SHA256`) deve ser numericamente inferior ou igual ao objetivo de dificuldade. A prova de trabalho consiste em modificar o campo `nonce` do cabeçalho do bloco ou a transação coinbase até que o hash resultante seja menor que o valor do objetivo.

Esse objetivo é ajustado a cada 2016 blocos (aproximadamente a cada duas semanas), durante um evento chamado "ajuste". O fator de dificuldade é recalculado com base no tempo que levou para minerar os 2016 blocos anteriores. Se o tempo total for menor que duas semanas, a dificuldade aumenta ajustando o objetivo para baixo. Se o tempo total for mais de duas semanas, a dificuldade diminui ajustando o objetivo para cima. O objetivo é manter um tempo médio de mineração de 10 minutos por bloco. Esse tempo entre cada bloco ajuda a prevenir divisões da rede Bitcoin, resultando em desperdício de poder computacional. O objetivo de dificuldade é encontrado em cada cabeçalho de bloco, dentro do campo `nBits`. Como este campo é reduzido para 32 bits e o objetivo é na verdade de 256 bits, o objetivo é compactado em um formato científico menos preciso.

![](../../dictionnaire/assets/34.png)

> ► *O objetivo de dificuldade é às vezes também chamado de "fator de dificuldade". Por extensão, pode ser referido com sua codificação nos cabeçalhos de blocos com o termo "nBits".*