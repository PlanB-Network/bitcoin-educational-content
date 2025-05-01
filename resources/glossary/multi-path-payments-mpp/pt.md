---
term: PAGAMENTOS MULTIPERCURSO (MPP)
---

Um termo genérico para todas as técnicas de pagamento no Lightning que permitem que uma transação seja dividida em várias partes mais pequenas e encaminhada através de rotas diferentes. Por outras palavras, cada fração de pagamento segue um caminho de nó diferente. Isso possibilita contornar as limitações de liquidez em um único canal na rota.


Os pagamentos multipercurso também oferecem ligeiras vantagens em termos de confidencialidade, uma vez que se torna mais difícil para um observador associar cada fragmento de pagamento à totalidade da transação. No entanto, na sua versão básica, todos os fragmentos partilham o mesmo segredo para os HTLCs, o que pode tornar a transação rastreável se um observador estiver presente em vários percursos. Além disso, como o segredo é único para todas as fracções do pagamento, não é atómico. Isto significa que algumas partes do pagamento podem ser executadas com sucesso, enquanto outras podem falhar. Estes inconvenientes são corrigidos com o "Atomic Multi-Path Payment".