---
term: CHAVE MESTRA
---

No contexto das carteiras HD (Hierárquicas Determinísticas), a chave privada mestra é uma chave privada única derivada da semente da carteira. Para obter a chave mestra, a função `HMAC-SHA512` é aplicada à semente, usando as palavras "*Bitcoin seed*" literalmente como a chave. O resultado desta operação produz uma saída de 512 bits, com os primeiros 256 bits constituindo a chave mestra, e os 256 bits restantes formando o código da cadeia mestra. A chave mestra e o código da cadeia mestra servem como ponto de partida para derivar todas as chaves privadas e públicas filhas na estrutura de árvore da carteira HD. Portanto, a chave privada mestra está na profundidade 0 de derivação.

![](../../dictionnaire/assets/19.png)