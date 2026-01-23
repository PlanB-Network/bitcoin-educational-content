---
term: Reutilização de endereços

definition: Uma prática desaconselhada de usar o mesmo endereço Bitcoin várias vezes para receber pagamentos, o que prejudica a privacidade permitindo que fundos sejam rastreados.
---
A reutilização de endereços refere-se à prática de utilizar o mesmo endereço de receção para bloquear vários UTXOs, por vezes em várias transacções diferentes. Os bitcoins são normalmente bloqueados usando um par de chaves criptográficas que corresponde a um endereço único. Como a blockchain é pública, é fácil ver quais endereços estão associados a quantos bitcoins. No caso de reutilizar o mesmo endereço para vários pagamentos, é razoável imaginar que todos os UTXOs associados pertencem à mesma entidade. Por conseguinte, a reutilização de endereços constitui um problema para a privacidade do utilizador. Permite ligações determinísticas entre múltiplas transacções e UTXOs, bem como a perpetuação do rastreio de fundos na cadeia. Satoshi Nakamoto já mencionou este problema no seu Livro Branco:

> *Como firewall adicional, deve ser utilizado um novo par de chaves para cada transação, a fim de evitar que sejam vinculadas a um proprietário comum.*

Nakamoto, S. (2008). "*Bitcoin: A Peer-to-Peer Electronic Cash System*". https://bitcoin.org/bitcoin.pdf.

Para preservar o mínimo de privacidade, recomenda-se vivamente que cada endereço de receção seja utilizado apenas uma vez. Para cada novo pagamento, é adequado gerar um novo endereço. Para saídas de mudança, um novo endereço também deve ser usado. Felizmente, graças às carteiras determinísticas e hierárquicas, tornou-se muito fácil usar uma infinidade de endereços. Todos os pares de chaves associados a uma carteira podem ser facilmente regenerados a partir da semente. É também por esta razão que o software da carteira gera sempre um endereço novo e diferente quando se clica no botão "Receber".
