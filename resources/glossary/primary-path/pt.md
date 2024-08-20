---
termo: CAMINHO PRIMÁRIO
---

Em um software de carteira que utiliza Miniscript, como o Liana por exemplo, o caminho primário refere-se ao conjunto de chaves que permite o gasto imediato de fundos, sem quaisquer condições baseadas em tempo. Este caminho está sempre acessível e é usado para a gestão diária de bitcoins, sem exigir uma espera (timelock) ao contrário dos caminhos de recuperação. Tome o exemplo de um script que incorpora 2 chaves distintas: chave A, que autoriza o gasto imediato de bitcoins, e chave B, que permite gastá-los após um atraso definido por um timelock de 52.560 blocos. Neste exemplo, a chave A vem do caminho primário, enquanto a chave B vem do caminho de recuperação.