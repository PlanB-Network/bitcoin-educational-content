---
termo: BIP113
---

Introduziu uma mudança no cálculo de todas as operações de timelock (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` e `OP_CHECKSEQUENCEVERIFY`). Especifica que, para avaliar a validade dos timelocks, agora eles devem ser comparados ao MTP (*Median Time Past*, ou Tempo Médio Passado), que é a mediana dos timestamps dos últimos 11 blocos. Anteriormente, apenas o timestamp do bloco anterior era utilizado. Este método torna o sistema mais previsível e impede a manipulação da referência de tempo pelos mineradores. O BIP113 foi introduzido por meio de um soft fork em 4 de julho de 2016, juntamente com o BIP68 e o BIP112, ativados pela primeira vez usando o método BIP9.