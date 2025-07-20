---
term: PAGAMENTOS MULTIPERCURSO ATÓMICOS
---

Versão melhorada do MPP (*Multi-Path Payments*) em que cada fragmento de pagamento tem um segredo parcial distinto, garantindo que a transação é liquidada atomicamente, ou seja, na totalidade ou não.


Os MPP são técnicas de pagamento no Lightning que permitem que uma transação seja dividida em várias partes mais pequenas e encaminhada através de rotas diferentes. Por outras palavras, cada fração de pagamento segue um caminho de nó diferente. Isso contorna as limitações de liquidez em um único canal na rota. Nos PPM básicos, cada fração de pagamento partilha o mesmo segredo e, por conseguinte, o mesmo Hash nos HTLC. Isto pode tornar a transação rastreável se um observador estiver presente em várias rotas, uma vez que pode associar todos estes segredos idênticos. Além disso, como o segredo é único para todas as partes do pagamento, não é atómico. Isto significa que algumas partes do pagamento podem ser executadas com sucesso, enquanto outras podem falhar.


Na AMP, são utilizados segredos parciais únicos para cada fração. Uma vez recebidos todos os fragmentos, estes permitem ao destinatário reconstruir o segredo geral original e reclamar o pagamento total. Este método torna impossível a liquidação parcial do pagamento, uma vez que a posse de todos os segredos parciais é necessária para desbloquear o pagamento total. Isto garante que o pagamento é totalmente bem sucedido ou totalmente mal sucedido (ou seja, atómico). O AMP também melhora a confidencialidade, uma vez que já não existem ligações visíveis entre as diferentes rotas.


Uma vantagem dos AMPs é o facto de funcionarem mesmo que apenas o destinatário e o remetente tenham implementado este método. Os nós intermediários processam estes pagamentos como transacções convencionais utilizando HTLCs, sem saberem que estão a processar fracções de um pagamento maior.