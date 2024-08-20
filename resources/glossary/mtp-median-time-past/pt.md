---
term: MTP (MEDIAN TIME PAST)
---

Este conceito é utilizado no protocolo Bitcoin para determinar uma margem no timestamp de consenso da rede. MTP é definido como a mediana dos timestamps dos últimos 11 blocos minerados. O uso deste indicador ajuda a evitar desacordos entre os nós sobre o tempo exato em caso de discrepâncias. MTP foi inicialmente usado para verificar a validade dos timestamps dos blocos em relação ao passado. Desde o BIP113, também tem sido usado como referência para o tempo da rede para verificar a validade de transações com bloqueio de tempo (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` e `OP_CHECKSEQUENCEVERIFY`).