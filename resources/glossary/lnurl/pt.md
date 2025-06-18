---
term: LNURL
---

Protocolo de comunicação que especifica um conjunto de caraterísticas concebidas para simplificar as interações entre nós e clientes do Lightning, bem como aplicações de terceiros. Este protocolo baseia-se no HTTP e permite a criação de ligações para várias operações, como um pedido de pagamento, um pedido de levantamento ou outras funcionalidades que melhoram a experiência do utilizador. Cada LNURL é um URL codificado em bech32 com o prefixo `lnurl`, que, ao ser analisado, desencadeia uma série de acções automáticas no Lightning Wallet.


Por exemplo, o LNURL-withdraw (LUD-03) permite-lhe levantar fundos de um serviço digitalizando um código QR, sem ter de utilizar manualmente um generate ou um Invoice. Ou LNURL-auth (LUD-04) permite-lhe ligar-se a serviços online utilizando uma chave privada no seu Lightning Wallet em vez de uma palavra-passe.