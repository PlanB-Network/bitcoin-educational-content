---
term: AJUSTE DE DIFICULDADE
---

O ajuste de dificuldade é um processo periódico que redefine o alvo de dificuldade para o mecanismo de prova de trabalho (mineração) no Bitcoin. Esse evento ocorre a cada 2016 blocos (aproximadamente a cada duas semanas). Serve para aumentar ou diminuir o fator de dificuldade (também chamado de alvo de dificuldade), dependendo de quão rapidamente os últimos 2016 blocos foram encontrados. O ajuste visa manter uma taxa de produção de blocos estável e previsível, na frequência de um bloco a cada 10 minutos, apesar das variações no poder computacional empregado pelos mineradores. A mudança na dificuldade durante o ajuste é limitada a um fator de 4. A fórmula executada pelos nós para calcular o novo alvo é a seguinte:
$$N = A \cdot \left(\frac{T}{1,209,600}\right)$$
&nbsp;
Onde:
* $N$: O novo alvo;
* $A$: O alvo antigo dos últimos 2016 blocos;
* $T$: O tempo total real dos últimos 2016 blocos em segundos;
* $1,209,600$: O tempo alvo em segundos para produzir 2016 blocos com um intervalo de 10 minutos entre cada um.

> ► *Em francês, o termo "reciblage" também é usado às vezes para se referir ao ajuste. Em inglês, é referido como "Difficulty Adjustment".*