---
term: ASICBOOST
---

ASICBOOST é um método de otimização algorítmica inventado em 2016, projetado para aumentar a eficiência da mineração de Bitcoin em cerca de 20% ao reduzir a quantidade de cálculos necessários para cada tentativa de hash do cabeçalho. Esta técnica explora uma característica da função de hash SHA256, usada para mineração, que divide os dados em blocos antes de processá-los. O ASICBOOST mantém um desses blocos inalterado através de múltiplas tentativas de hashing, permitindo que o minerador faça apenas parte do trabalho para este bloco em várias tentativas. O compartilhamento de dados possibilita a reutilização de resultados de cálculos anteriores, reduzindo assim o número total de cálculos necessários para encontrar um hash válido.

O ASICBOOST pode ser usado em duas formas: ASICBOOST Aberto e ASICBOOST Oculto. A forma Aberta do ASICBOOST é visível para todos, pois envolve o uso do campo `nVersion` do bloco como um nonce, sem alterar o verdadeiro `Nonce`. A forma Oculta busca esconder essas modificações usando árvores de Merkle. No entanto, este segundo método tornou-se menos eficaz desde a introdução do SegWit devido à segunda árvore de Merkle, que aumenta o número de cálculos necessários para usá-lo.

Em resumo, o ASICBOOST permite que os mineradores não tenham que realizar um verdadeiro SHA256 completo para todas as tentativas de hashing, já que parte do resultado permanece inalterada, o que acelera o trabalho dos mineradores.