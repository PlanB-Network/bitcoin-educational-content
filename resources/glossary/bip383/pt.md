---
term: BIP383

---
Introduz as funções `multi(NUM, KEY, ..., KEY)` e `sortedmulti(NUM, KEY, ..., KEY)` para descritores. Essas funções permitem a descrição de scripts com várias assinaturas nos descritores, com `sortedmulti` ordenando as chaves públicas em ordem lexicográfica para garantir a compatibilidade durante a importação. BIP383 foi implementado junto com todos os outros BIPs relacionados a descritores (exceto BIP386) na versão 0.17 do Bitcoin Core.