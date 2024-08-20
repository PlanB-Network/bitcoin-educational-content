---
termo: SHARES
---

No contexto de pools de mineração, uma share é um indicador usado para quantificar a contribuição individual de um minerador dentro da pool. Esta medida serve como base para calcular a recompensa que a pool redistribui a cada minerador. Cada share corresponde a um hash que satisfaz um alvo de dificuldade menor do que o da rede Bitcoin.

Para explicar com uma analogia, considere um dado de 20 lados. No Bitcoin, suponha que a prova de trabalho exija rolar um número menor que 3 para validar um bloco (isto é, alcançar um resultado de 1 ou 2). Agora, imagine que dentro de uma pool de mineração, o alvo de dificuldade para uma share é definido como 10. Assim, para um minerador individual na pool, cada rolagem de dado que resulta em um número menor que 10 conta como uma share válida. Essas shares são então transmitidas para a pool pelo minerador, a fim de reivindicar sua recompensa, mesmo que não correspondam a um resultado válido para um bloco no Bitcoin.

Para cada hash calculado, um minerador individual em uma pool pode encontrar três cenários diferentes:
* Se o valor do hash for maior ou igual ao alvo de dificuldade definido pela pool para uma share, então este hash não é útil. O minerador então muda seu nonce para tentar um novo hash: `hash > share > bloco`.
* Se o hash for menor que o alvo de dificuldade da share, mas maior ou igual ao alvo de dificuldade do Bitcoin, então este hash constitui uma share válida que, no entanto, não é suficiente para validar um bloco. O minerador pode enviar este hash para sua pool para reivindicar a recompensa associada à share: `share > hash > bloco`.
* Se o hash for menor que o alvo de dificuldade da rede Bitcoin, ele é considerado tanto uma share válida quanto um bloco válido. O minerador transmite este hash para sua pool, que se apressa em transmiti-lo na rede Bitcoin. Este hash também é contado como uma share válida para o minerador: `share > bloco > hash`.

![](../../dictionnaire/assets/32.png)

Este sistema de shares é usado para estimar o trabalho realizado por cada minerador individual dentro de uma pool, sem ter que recalcular individualmente todos os hashes gerados por um minerador, o que seria completamente ineficiente para a pool.

As pools de mineração ajustam a dificuldade das shares para equilibrar a carga de verificação e garantir que cada minerador, pequeno ou grande, envie shares aproximadamente a cada poucos segundos. Isso permite um cálculo preciso da taxa de hash de cada minerador e a distribuição de recompensas de acordo com o método escolhido de cálculo de compensação (PPS, PPLNS, TIDES...).

> ► *Em francês, "shares" pode ser traduzido como "part".*