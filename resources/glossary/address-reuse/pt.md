---
termo: REUTILIZAÇÃO DE ENDEREÇO
---

Reutilização de endereço refere-se à prática de usar o mesmo endereço de recebimento para bloquear múltiplos UTXOs, às vezes em várias transações diferentes. Os bitcoins são tipicamente bloqueados usando um par de chaves criptográficas que corresponde a um endereço único. Como a blockchain é pública, é fácil ver quais endereços estão associados a quantos bitcoins. No caso de reutilizar o mesmo endereço para múltiplos pagamentos, é razoável imaginar que todos os UTXOs associados pertençam à mesma entidade. Portanto, a reutilização de endereço representa um problema para a privacidade do usuário. Ela permite ligações determinísticas entre múltiplas transações e UTXOs, bem como perpetua o rastreamento de fundos na cadeia. Satoshi Nakamoto já mencionou esse problema em seu White Paper:

> "*Como uma barreira adicional, um novo par de chaves poderia ser usado para cada transação para evitar que elas sejam vinculadas a um proprietário comum.*" - Nakamoto, S. (2008). "Bitcoin: Um Sistema de Dinheiro Eletrônico Peer-to-Peer". Consultado em https://bitcoin.org/bitcoin.pdf.

Para preservar a privacidade no mínimo, é fortemente aconselhado usar cada endereço de recebimento apenas uma vez. Para cada novo pagamento, é apropriado gerar um novo endereço. Para saídas de troco, também deve ser usado um endereço novo. Felizmente, graças às carteiras determinísticas e hierárquicas, tornou-se muito fácil usar uma multiplicidade de endereços. Todos os pares de chaves associados a uma carteira podem ser facilmente regenerados a partir da semente. É por isso que o software de carteira sempre gera um novo endereço diferente quando você clica no botão “Receber”.

> ► *Em inglês, é chamado de "Address Reuse".*