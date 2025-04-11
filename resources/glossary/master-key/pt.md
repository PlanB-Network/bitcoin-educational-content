---
term: CHAVE MESTRA

---
No contexto das carteiras HD (Hierarchical Deterministic), a chave mestra privada é uma chave privada única derivada da semente da carteira. Para obter a chave mestra, a função `HMAC-SHA512` é aplicada à seed, usando as palavras "*Bitcoin seed*" literalmente como a chave. O resultado desta operação produz um output de 512 bits, com os primeiros 256 bits a constituírem a chave mestra e os restantes 256 bits a formarem o código da cadeia mestra. A chave mestra e o código da cadeia mestra servem como ponto de partida para derivar todas as chaves públicas e privadas filhas na estrutura de árvore da carteira HD. Portanto, a chave mestra privada está na profundidade 0 da derivação.

![](../../dictionnaire/assets/19.webp)