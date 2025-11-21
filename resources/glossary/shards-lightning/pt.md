---
term: ESTILHAÇOS (RELÂMPAGO)
---

No contexto de *Pagamentos de vários caminhos (MPP)* ou *Pagamentos de vários caminhos atômicos (AMP)*, um Shard é uma fração de um pagamento global. Cada Shard representa uma parte do pagamento total, que é encaminhado separadamente através de uma rota diferente no Lightning.


No MPP, todos os fragmentos partilham o mesmo segredo, enquanto no AMP, cada Shard tem um segredo parcial único. O recetor agrupa os fragmentos para reconstituir e finalizar o pagamento total. Este mecanismo contorna as limitações de liquidez num único canal.