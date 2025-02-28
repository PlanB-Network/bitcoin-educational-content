---
term: CAMINHO DE RECUPERAÇÃO

---
Num software de carteira que utiliza Miniscript, como o Liana, por exemplo, os caminhos de recuperação referem-se a conjuntos de chaves que só se tornam operacionais após um período definido de inatividade no script que bloqueia os bitcoins (timelock). Os caminhos de recuperação só podem ser utilizados depois de os timelocks terem expirado, oferecendo assim um método de recuperação de fundos quando o caminho primário não está disponível. Considere o exemplo de um script que incorpora 2 chaves distintas: a chave A, que autoriza o gasto imediato de bitcoins, e a chave B, que permite gastá-los após um atraso definido por um timelock de 52.560 blocos. Neste exemplo, a chave A vem do caminho primário, enquanto a chave B vem do caminho de recuperação.