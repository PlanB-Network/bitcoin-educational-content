---
term: BIP32

---
A BIP32 introduziu o conceito de carteira determinística hierárquica (HD wallet). Esta proposta permite a geração de uma hierarquia de pares de chaves a partir de uma "semente-mestre" comum, utilizando funções de derivação unidireccionais. Cada par de chaves gerado pode ser o pai de outras chaves filhas, formando assim uma estrutura em forma de árvore (hierárquica). A vantagem do BIP32 é o facto de permitir a gestão de vários pares de chaves diferentes com a necessidade de manter apenas uma única semente para os regenerar. Esta inovação contribuiu nomeadamente para combater a questão da reutilização de endereços, que é grave para a privacidade dos utilizadores. O BIP32 também permite a criação de sub-ramos dentro da mesma carteira para facilitar a sua gestão.