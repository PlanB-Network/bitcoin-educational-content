---
term: ASICBOOST

---
O ASICBOOST é um método de otimização algorítmica inventado em 2016, concebido para aumentar a eficiência da mineração de Bitcoin em cerca de 20%, reduzindo a quantidade de cálculos necessários para cada tentativa de hash do cabeçalho. Esta técnica explora uma caraterística da função hash SHA256, usada para mineração, que divide os dados em blocos antes de os processar. O ASICBOOST mantém um desses blocos inalterado em várias tentativas de hashing, permitindo que o minerador faça apenas parte do trabalho para esse bloco em várias tentativas. Esta partilha de dados permite a reutilização de resultados de cálculos anteriores, reduzindo assim o número total de cálculos necessários para encontrar um hash válido.

O ASICBOOST pode ser utilizado de duas formas: Overt ASICBOOST e Covert ASICBOOST. A forma Overt ASICBOOST é visível para todos, pois envolve o uso do campo `nVersion` do bloco como um nonce, e não altera o verdadeiro `Nonce`. A forma Covert procura esconder essas modificações usando árvores Merkle. No entanto, este segundo método tornou-se menos eficaz desde a introdução do SegWit devido à segunda árvore Merkle, que aumenta o número de cálculos necessários para usá-lo.

Em resumo, o ASICBOOST permite que os mineiros não tenham de efetuar um verdadeiro SHA256 completo para todas as tentativas de hashing, uma vez que parte do resultado permanece inalterado, o que acelera o trabalho dos mineiros.