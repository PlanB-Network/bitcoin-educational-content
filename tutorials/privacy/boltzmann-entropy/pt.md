---
name: Boltzmann Calculator
description: Entenda o conceito de entropia e como usar a Boltzmann
---
![cover](assets/cover.webp)

***ATENÇÃO:** Após a prisão dos fundadores da Samourai Wallet e a apreensão dos seus servidores em 24 de abril, o site KYCP.org está atualmente inacessível. O Gitlab que hospedava o código do Python Boltzmann Calculator também foi apreendido. Atualmente, não é mais possível baixar essa ferramenta. No entanto, é possível que o código seja republicado por outras pessoas nas próximas semanas. Enquanto isso, você ainda pode se beneficiar deste tutorial para entender o funcionamento do Boltzmann Calculator. Os indicadores fornecidos por esta ferramenta são aplicáveis a qualquer transação Bitcoin e também podem ser calculados manualmente. Eu fornecerei todos os cálculos necessários neste tutorial. Se você já tinha baixado a ferramenta Python em sua máquina ou se está usando um RoninDojo, pode continuar usando a ferramenta e seguir este tutorial normalmente, ainda funciona.*

_Estamos acompanhando de perto a evolução deste caso, bem como os desenvolvimentos relacionados aos ferramentas associadas. Fique assegurado de que atualizaremos este tutorial à medida que novas informações estiverem disponíveis._

_Este tutorial é fornecido apenas para fins educativos e informativos. Não endossamos nem encorajamos o uso dessas ferramentas para fins criminosos. É responsabilidade de cada usuário cumprir as leis em sua jurisdição._

---

A Calculadora Boltzmann é uma ferramenta para analisar uma transação Bitcoin medindo seu nível de entropia junto com outras métricas avançadas. Ela fornece insights sobre as conexões entre as entradas e saídas de uma transação. Esses indicadores oferecem uma avaliação quantificada da privacidade de uma transação e ajudam a identificar potenciais erros.

Esta ferramenta Python foi desenvolvida pelas equipes da Samourai Wallet e OXT, mas pode ser usada em qualquer transação Bitcoin.

## Como usar a Calculadora Boltzmann?
Para usar a Calculadora Boltzmann, duas opções estão disponíveis para você. A primeira é instalar a ferramenta Python diretamente em sua máquina. Alternativamente, você pode optar pelo site KYCP.org (_Conheça a Privacidade da Sua Moeda_), que oferece uma plataforma de uso simplificado. Para usuários do RoninDojo, note que esta ferramenta já está integrada ao seu nó.

Usar o site KYCP é bastante fácil: basta inserir o identificador da transação (TXID) que você deseja analisar na barra de pesquisa e pressionar `ENTER`.
![KYCP](assets/1.webp)
Você então encontrará diferentes informações sobre a transação, incluindo os links entre as entradas e saídas. Clique em `links determinísticos`.
![KYCP](assets/2.webp)
Você chegará à página dedicada aos indicadores da Calculadora Boltzmann.
![KYCP](assets/3.webp)
Para aqueles que preferem usar a ferramenta diretamente de seu nó RoninDojo, ela é acessível via `RoninCLI > Samourai Toolkit > Calculadora Boltzmann`.

Assim como no site KYCP.org, uma vez instalada a ferramenta Python, você simplesmente precisará colar o TXID da transação que deseja analisar.

![KYCP](assets/7.webp)

Em seguida, pressione a tecla `ENTER` para obter os resultados.

![KYCP](assets/8.webp)

## Quais são os indicadores da Calculadora Boltzmann?
### Combinações / Interpretações:
O primeiro indicador que o software calcula é o número total de combinações possíveis, indicado sob `nb combinations` ou `interpretations` na ferramenta.

Levando em conta os valores dos UTXOs envolvidos na transação, este indicador calcula o número de maneiras pelas quais as entradas podem ser associadas às saídas. Em outras palavras, determina o número de interpretações plausíveis que uma transação pode suscitar do ponto de vista de um observador externo analisando-a.
Por exemplo, um coinjoin estruturado de acordo com o modelo Whirlpool 5x5 apresenta `1,496` combinações possíveis: ![KYCP](assets/4.webp)
Um coinjoin Whirlpool Surge Cycle 8x8, por outro lado, apresenta `9,934,563` interpretações possíveis: ![KYCP](assets/5.webp)
Em contraste, uma transação mais tradicional com 1 entrada e 2 saídas apresentará apenas uma única interpretação: ![KYCP](assets/6.webp)

### Entropia:
O segundo indicador calculado é a entropia de uma transação, designada por `Entropia`.
No contexto geral de criptografia e informação, entropia é uma medida quantitativa da incerteza ou imprevisibilidade associada a uma fonte de dados ou um processo aleatório. Em outras palavras, entropia é uma maneira de medir quão difícil é prever ou adivinhar informações.
No contexto específico de análise de cadeias, entropia também é o nome de um indicador, derivado da entropia de Shannon e [inventado por LaurentMT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf), que é calculado com a ferramenta Boltzmann.

Quando uma transação apresenta um alto número de combinações possíveis, é frequentemente mais relevante referir-se à sua entropia. Este indicador permite medir a falta de conhecimento dos analistas sobre a configuração exata da transação. Em outras palavras, quanto maior a entropia, mais difícil se torna a tarefa de identificar movimentos de bitcoin entre entradas e saídas para os analistas.

Na prática, a entropia revela se, do ponto de vista de um observador externo, uma transação apresenta múltiplas interpretações possíveis, baseando-se apenas nas quantidades de entradas e saídas, sem considerar outros padrões e heurísticas externos ou internos. Alta entropia é então sinônimo de melhor confidencialidade para a transação.

A entropia é definida como o logaritmo binário do número de combinações possíveis. Aqui está a fórmula usada:
```plaintext
E: a entropia da transação
C: o número de combinações possíveis para a transação

E = log2(C)
```

Em matemática, o logaritmo binário (logaritmo de base-2) corresponde à operação inversa de elevar 2. Em outras palavras, o logaritmo binário de `x` é o expoente ao qual `2` deve ser elevado para obter `x`. Este indicador é, portanto, expresso em bits.

Vamos tomar o exemplo do cálculo da entropia para uma transação coinjoin estruturada de acordo com o modelo Whirlpool 5x5, que, como mencionado anteriormente, oferece um número de combinações possíveis de `1,496`:
```plaintext
C = 1,496
E = log2(1,496)
E = 10.5469 bits
```
Assim, esta transação coinjoin exibe uma entropia de `10.5469 bits`, o que é considerado muito satisfatório. Quanto maior esse valor, mais diferentes interpretações a transação admite, fortalecendo assim seu nível de privacidade.
Para uma transação coinjoin 8x8 apresentando `9,934,563` interpretações, a entropia seria:
```plaintext
C = 9,934,563
E = log2(9,934,563)
E = 23.244 bits
```

Vamos tomar outro exemplo com uma transação mais convencional, apresentando uma entrada e duas saídas: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://mempool.space/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce) No caso desta transação, a única interpretação possível é: `(In.0) > (Out.0 ; Out.1)`. Consequentemente, sua entropia é estabelecida em `0`:
```plaintext
C = 1
E = log2(1)
E = 0 bits
```

### Eficiência:
O terceiro indicador fornecido pelo Calculador Boltzmann é denominado `Eficiência da Carteira`. Este indicador avalia a eficiência da transação comparando-a com a transação ótima concebível em uma configuração idêntica.
Isso nos leva a discutir o conceito de entropia máxima, que corresponde à maior entropia que uma estrutura de transação específica poderia teoricamente alcançar. A eficiência da transação é então calculada confrontando essa entropia máxima com a entropia real da transação analisada.
A fórmula utilizada é a seguinte:
```plaintext
ER: a entropia real da transação expressa em bits
EM: a entropia máxima possível para uma dada estrutura de transação expressa em bits
Ef: a eficiência da transação em bits

Ef = ER - EM
```

Por exemplo, para uma estrutura de coinjoin do tipo Whirlpool 5x5, a entropia máxima é definida em `10.5469`:
```plaintext
ER = 10.5469
EM = 10.5469
Ef = 10.5469 - 10.5469 = 0 bits
```

Este indicador também é expresso como uma porcentagem, sua fórmula é então:
```plaintext
CR: o número real de combinações possíveis
CM: o número máximo de combinações possíveis com a mesma estrutura
Ef: a eficiência expressa como uma porcentagem

Ef = CR / CM
Ef = 1.496 / 1.496
Ef = 100%
```

Uma eficiência de `100%` indica, portanto, que a transação maximiza seu potencial de privacidade de acordo com sua estrutura.

### Densidade de Entropia:
O quarto indicador é a densidade de entropia, notada na ferramenta como `Densidade de Entropia`. Ela oferece uma perspectiva sobre a entropia relativa a cada entrada ou saída da transação. Este indicador é útil para avaliar e comparar a eficiência de transações de diferentes tamanhos. Para calculá-lo, basta dividir a entropia total da transação pelo número total de entradas e saídas envolvidas:
```plaintext
ED: a densidade de entropia expressa em bits
E: a entropia da transação expressa em bits
T: o número total de entradas e saídas na transação

ED = E / T
```

Vamos tomar o exemplo de um coinjoin Whirlpool 5x5:
```plaintext
T = 5 + 5 = 10
E = 10.5469
ED = 10.5469 / 10 = 1.054 bits
```

Vamos também calcular a densidade de entropia para um coinjoin Whirlpool 8x8:
```plaintext
T = 8 + 8 = 16
E = 23.244
ED = 23.244 / 16 = 1.453 bits
```

### Pontuação Boltzmann:
A quinta informação fornecida pelo Calculador Boltzmann é a tabela de probabilidades de correspondência entre as entradas e saídas. Esta tabela indica, através da pontuação Boltzmann, a probabilidade condicional de que uma entrada específica esteja relacionada a uma saída dada.

É, portanto, uma medida quantitativa da probabilidade condicional de que uma associação entre uma entrada e uma saída em uma transação ocorra, baseada na razão do número de ocorrências favoráveis deste evento ao número total de ocorrências possíveis, em um conjunto de interpretações.

Tomando o exemplo de um coinjoin Whirlpool novamente, a tabela de probabilidades condicionais destacaria as chances de ligação entre cada entrada e saída, fornecendo uma medida quantitativa da ambiguidade das associações na transação:

| %       | Saída 0 | Saída 1 | Saída 2 | Saída 3 | Saída 4 |
| ------- | ------- | ------- | ------- | ------- | ------- |
| Entrada 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Entrada 1 | 34%      | 34%      | 34%      | 34%      | 34%      |


Aqui, podemos ver claramente que cada entrada tem uma chance igual de ser associada a qualquer saída, o que aumenta a confidencialidade da transação.

Calcular a pontuação de Boltzmann envolve dividir o número de interpretações nas quais um certo evento ocorre pelo número total de interpretações disponíveis. Assim, para determinar a pontuação associando a entrada Nº 0 com a saída Nº 3 (`512` interpretações), o seguinte procedimento é usado:
```plaintext
Interpretações (IN.0 > OUT.3) = 512
Total de Interpretações = 1496
Pontuação = 512 / 1496 = 34%
```

Tomando o exemplo de um Whirlpool 8x8 coinjoin (ciclo de aumento), a tabela Boltzmann ficaria assim:

|       | OUT.0 | OUT.1 | OUT.2 | OUT.3 | OUT.4 | OUT.5 | OUT.6 | OUT.7 |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| IN.0  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.1  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.2  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.3  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.4  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.5  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.6  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.7  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |


No entanto, no caso de uma transação simples com uma única entrada e duas saídas, a situação é diferente:

| %       | Saída 0 | Saída 1 |
|---------|---------|---------|
| Entrada 0 | 100%    | 100%    |


Aqui, observa-se que a probabilidade de cada saída originar-se da entrada Nº 0 é de `100%`. Uma probabilidade menor, portanto, traduz-se em maior privacidade ao diluir os vínculos diretos entre entradas e saídas.
### Vínculos Determinísticos:
A sexta informação fornecida é o número de vínculos determinísticos, complementada pela razão desses vínculos. Este indicador revela quantas conexões entre as entradas e saídas na transação analisada são incontestáveis, com uma probabilidade de `100%`. A razão, por outro lado, oferece uma perspectiva sobre o peso desses vínculos determinísticos dentro do conjunto total de vínculos de transação.
Por exemplo, uma transação do tipo Whirlpool coinjoin não possui vínculos determinísticos, e, portanto, exibe um indicador e uma razão de `0%`. Por outro lado, em nossa segunda transação simples examinada (com uma entrada e duas saídas), o indicador está definido em `2` e a razão atinge `100%`. Assim, um indicador nulo sinaliza excelente confidencialidade devido à ausência de vínculos diretos e incontestáveis entre entradas e saídas.

**Recursos Externos:**

- Código Boltzmann no Samourai
- [Transações Bitcoin & Privacidade (Parte I) por Laurent MT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [Transações Bitcoin & Privacidade (Parte II) por Laurent MT](https://gist.github.com/LaurentMT/d361bca6dc52868573a2)
- [Transações Bitcoin & Privacidade (Parte III) por Laurent MT](https://gist.github.com/LaurentMT/e8644d5bc903f02613c6)
- Site do KYCP
- [Artigo no Medium sobre uma Introdução ao Script Boltzmann por Laurent MT](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)