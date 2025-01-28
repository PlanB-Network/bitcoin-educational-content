---
term: ACÇÕES

---
No contexto de pools de mineração, uma quota é um indicador usado para quantificar a contribuição de um mineiro individual dentro do pool. Esta medida serve de base para calcular a recompensa que o pool redistribui a cada mineiro. Cada quota corresponde a um hash que satisfaz um objetivo de dificuldade inferior ao da rede Bitcoin.

Para explicar com uma analogia, considere um dado de 20 lados. Na Bitcoin, suponha que a prova de trabalho requer o lançamento de um número inferior a 3 para validar um bloco (ou seja, obter um resultado de 1 ou 2). Agora, imagine que, dentro de um grupo de mineração, o objetivo de dificuldade para uma ação é fixado em 10. Assim, para um mineiro individual no grupo, cada lançamento de dados que resulte num número inferior a 10 conta como uma ação válida. Estas acções são então transmitidas à pool pelo mineiro, de forma a reclamar a sua recompensa, mesmo que não correspondam a um resultado válido para um bloco de Bitcoin.

Para cada hash calculado, um mineiro individual numa pool pode encontrar três cenários diferentes:


- Se o valor do hash for maior ou igual ao objetivo de dificuldade definido pelo grupo para uma ação, então este hash não tem utilidade. O minerador então muda seu nonce para tentar um novo hash: `hash > share > block`.
- Se o hash for inferior ao objetivo de dificuldade da ação, mas maior ou igual ao objetivo de dificuldade da Bitcoin, então este hash constitui uma ação válida que, no entanto, não é suficiente para validar um bloco. O mineiro pode enviar este hash para o seu pool para reclamar a recompensa associada à ação: `share > hash > block`.
- Se o hash for inferior ao objetivo de dificuldade da rede Bitcoin, é considerado tanto uma ação válida como um bloco válido. O minerador transmite esse hash para seu pool, que se apressa em difundi-lo na rede Bitcoin. Este hash também é contado como uma ação válida para o minerador: `share > bloc > hash`.

![](../../dictionnaire/assets/32.webp)

Este sistema de partilha é utilizado para estimar o trabalho realizado por cada mineiro individual dentro de um grupo, sem ter de recalcular individualmente todos os hashes gerados por um mineiro, o que seria completamente ineficiente para o grupo.

As pools de mineração ajustam a dificuldade das acções para equilibrar a carga de verificação e garantir que cada mineiro, seja ele pequeno ou grande, submeta acções aproximadamente a cada poucos segundos. Isto permite um cálculo exato do hashrate de cada mineiro e a distribuição de recompensas de acordo com o método de cálculo de compensação escolhido (PPS, PPLNS, TIDES...).

> ► *Em francês, "shares" pode ser traduzido por "parte"