---
term: BIP113

---
Introduzida uma mudança no cálculo de todas as operações de timelock (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` e `OP_CHECKSEQUENCEVERIFY`). Especifica que para avaliar a validade dos timelocks, eles devem agora ser comparados com o MTP (*Median Time Past*), que é a mediana dos timestamps dos últimos 11 blocos. Anteriormente, apenas era utilizado o carimbo de data/hora do bloco anterior. Este método torna o sistema mais previsível e impede a manipulação da referência temporal por parte dos mineiros. O BIP113 foi introduzido através de um soft fork em 4 de julho de 2016, juntamente com o BIP68 e o BIP112, ativado pela primeira vez através do método BIP9.