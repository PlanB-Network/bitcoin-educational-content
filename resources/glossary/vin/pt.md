---
term: VIN
---

Um elemento específico de uma transação Bitcoin que especifica a fonte de fundos usada para satisfazer as saídas. Cada `vin` refere-se a uma saída não gasta (UTXO) de uma transação anterior. Uma transação pode conter múltiplas entradas, cada uma identificada por uma combinação do `txid` (o identificador da transação original) e o `vout` (o índice da saída naquela transação).

Cada `vin` inclui as seguintes informações:
* `txid`: o identificador da transação anterior contendo a saída usada aqui como entrada;
* `vout`: o índice da saída na transação anterior;
* `scriptSig` ou `scriptWitness`: um script de desbloqueio que fornece os dados necessários para satisfazer as condições impostas pelo `scriptPubKey` da transação anterior cujos fundos estão sendo gastos, geralmente fornecendo uma assinatura criptográfica;
* `nSequence`: um campo específico usado para indicar como esta entrada está bloqueada pelo tempo, bem como outras opções como RBF.