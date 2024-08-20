---
term: BIP383
---

Introduz as funções `multi(NUM, KEY, ..., KEY)` e `sortedmulti(NUM, KEY, ..., KEY)` para descritores. Essas funções permitem a descrição de scripts de assinatura múltipla nos descritores, com `sortedmulti` ordenando as chaves públicas em ordem lexicográfica para garantir compatibilidade durante a importação. O BIP383 foi implementado juntamente com todos os outros BIPs relacionados a descritores (exceto o BIP386) na versão 0.17 do Bitcoin Core.