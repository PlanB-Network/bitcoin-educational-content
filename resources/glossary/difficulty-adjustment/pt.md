---
term: AJUSTAMENTO DE DIFICULDADES

---
O ajuste de dificuldade é um processo periódico que redefine o objetivo de dificuldade para o mecanismo de prova de trabalho (mineração) na Bitcoin. Este evento ocorre a cada 2016 blocos (aproximadamente a cada duas semanas). Serve para aumentar ou diminuir o fator de dificuldade (também chamado de objetivo de dificuldade), dependendo da rapidez com que os últimos blocos de 2016 foram encontrados. O objetivo do ajustamento é manter uma taxa de produção de blocos estável e previsível, com uma frequência de um bloco a cada 10 minutos, apesar das variações na potência computacional utilizada pelos mineiros. A alteração da dificuldade durante o ajustamento é limitada a um fator de 4. A fórmula executada pelos nós para calcular o novo objetivo é a seguinte

$$N = A \cdot \left(\frac{T}{1,209,600}\right)$$

&nbsp;

Onde:


- $N$: O novo objetivo;
- $A$: O antigo objetivo dos últimos 2016 blocos;
- $T$: O tempo total efetivo dos últimos 2016 blocos em segundos;
- $1,209,600$: O tempo alvo em segundos para produzir 2016 blocos com um intervalo de 10 minutos entre cada um.

> ► *Em francês, o termo "reciblage" é por vezes também utilizado para designar o ajustamento. Em inglês, é referido como "Difficulty Adjustment"