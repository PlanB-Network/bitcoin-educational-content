---
term: CAMINHO DE RECUPERAÇÃO
---

Em um software de carteira que utiliza Miniscript, como o Liana, por exemplo, os caminhos de recuperação referem-se a conjuntos de chaves que só se tornam operacionais após um período definido de inatividade no script que bloqueia os bitcoins (timelock). Os caminhos de recuperação só são utilizáveis uma vez que os timelocks tenham expirado, oferecendo assim um método de recuperar fundos quando o caminho primário não está disponível. Considere o exemplo de um script que incorpora 2 chaves distintas: chave A, que autoriza o gasto imediato dos bitcoins, e chave B, que permite gastá-los após um atraso definido por um timelock de 52.560 blocos. Neste exemplo, a chave A vem do caminho primário, enquanto a chave B vem do caminho de recuperação.