---
term: Anchor
---

En el protocolo RGB, una Anchor representa un conjunto de datos del lado del cliente utilizados para demostrar la inclusión de una única Commitment en una transacción. En el protocolo RGB, una Anchor se compone de las siguientes Elements:




- transaction ID Bitcoin (txid) de Witness Transaction ;
- Multi Protocol Commitment (MPC);
- Deterministic Bitcoin Commitment (DBC);
- Extra Transaction Proof (ETP) si se utiliza el mecanismo Tapret Commitment.


Por lo tanto, una Anchor sirve para establecer un vínculo verificable entre una transacción específica de Bitcoin y los datos privados validados por el protocolo RGB. Garantiza que estos datos están efectivamente incluidos en Blockchain, sin que se haga público su contenido exacto.