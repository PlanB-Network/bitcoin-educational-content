---
term: OBJECTIVO DE DIFICULDADE

---
O fator de dificuldade, também conhecido como objetivo de dificuldade, é um parâmetro utilizado no mecanismo de consenso por prova de trabalho (Proof of Work, PoW) na Bitcoin. O objetivo representa um valor numérico que determina a dificuldade para os mineiros resolverem um problema criptográfico específico, chamado prova de trabalho, ao criarem um novo bloco na cadeia de blocos.

O alvo de dificuldade é um número ajustável de 256 bits (64 bytes) que determina um limite de aceitabilidade para o hash de cabeçalhos de blocos. Em outras palavras, para que um bloco seja válido, o hash do seu cabeçalho com `SHA256d` (double `SHA256`) deve ser numericamente menor ou igual ao difficulty target. A prova de trabalho consiste em modificar o campo `nonce` do cabeçalho do bloco ou da transação coinbase até que o hash resultante seja menor que o valor alvo.

Este objetivo é ajustado a cada 2016 blocos (aproximadamente a cada duas semanas), durante um evento chamado "ajustamento" O fator de dificuldade é recalculado com base no tempo que demorou a minerar os blocos de 2016 anteriores. Se o tempo total for inferior a duas semanas, a dificuldade aumenta, ajustando o objetivo para baixo. Se o tempo total for superior a duas semanas, a dificuldade diminui, ajustando o objetivo para cima. O objetivo é manter um tempo médio de extração de 10 minutos por bloco. Este tempo entre cada bloco ajuda a evitar divisões da rede Bitcoin, resultando num desperdício de poder de computação. O objetivo de dificuldade é encontrado no cabeçalho de cada bloco, dentro do campo `nBits`. Uma vez que este campo é reduzido a 32 bits e o objetivo é na realidade 256 bits, o objetivo é compactado num formato científico menos preciso.

![](../../dictionnaire/assets/34.webp)

> ► *O objetivo de dificuldade é por vezes também designado por "fator de dificuldade" Por extensão, pode ser referido com a sua codificação nos cabeçalhos dos blocos com o termo "nBits"