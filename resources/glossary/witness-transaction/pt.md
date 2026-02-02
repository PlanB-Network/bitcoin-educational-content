---
term: Transação witness
definition: Em RGB, transação Bitcoin que fecha o Single-use Seal para fixar o estado de um contrato on-chain.
---

No protocolo RGB, o Witness Transaction refere-se à transação Bitcoin que fecha o Single-Use Seal em torno de uma mensagem que incorpora um Multi Protocol Commitment (MPC). Esta operação consiste em gastar um UTXO existente, ou em criar um novo, para bloquear o Commitment contratual inscrito no protocolo. O Witness Transaction é, portanto, uma prova On-Chain de que o estado do RGB Contract foi fixado num determinado momento.