---
term: MTP (MEDIANA DO TEMPO PASSADO)

---
Este conceito é utilizado no protocolo Bitcoin para determinar uma margem no carimbo de data/hora de consenso da rede. O MTP é definido como a mediana dos carimbos de data/hora dos últimos 11 blocos extraídos. A utilização deste indicador ajuda a evitar desacordos entre nós sobre a hora exacta em caso de discrepâncias. O MTP foi inicialmente utilizado para verificar a validade dos carimbos temporais dos blocos em relação ao passado. Desde o BIP113, também tem sido utilizado como referência para o tempo da rede para verificar a validade das transacções de bloqueio de tempo (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` e `OP_CHECKSEQUENCEVERIFY`).