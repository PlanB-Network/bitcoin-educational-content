---
term: Anchor
---

В протоколе RGB Anchor представляет собой набор данных на стороне клиента, используемых для доказательства включения одного Commitment в транзакцию. В протоколе RGB Anchor состоит из следующих Elements:




- transaction ID Bitcoin (txid) из Witness Transaction ;
- Multi Protocol Commitment (MPC);
- Deterministic Bitcoin Commitment (DBC);
- Дополнительное подтверждение транзакции (ETP), если используется механизм Tapret Commitment.


Таким образом, Anchor служит для установления проверяемой связи между конкретной транзакцией Bitcoin и частными данными, подтвержденными протоколом RGB. Он гарантирует, что эти данные действительно включены в Blockchain, при этом их точное содержание не должно быть обнародовано.