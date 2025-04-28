---
term: Anchor
---

No protocolo RGB, um Anchor representa um conjunto de dados do lado do cliente utilizados para provar a inclusão de um único Commitment numa transação. No protocolo RGB, um Anchor é composto pelos seguintes Elements:




- transaction ID Bitcoin (txid) a partir de Witness Transaction ;
- Multi Protocol Commitment (PPM);
- Deterministic Bitcoin Commitment (DBC);
- Prova de transação extra (ETP) se for utilizado o mecanismo Tapret Commitment.


Um Anchor serve, por conseguinte, para estabelecer uma ligação verificável entre uma transação Bitcoin específica e os dados privados validados pelo protocolo RGB. Garante que estes dados estão efetivamente incluídos no Blockchain, sem que o seu conteúdo exato seja tornado público.