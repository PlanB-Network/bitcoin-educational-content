---
term: Anchor
---

Nel protocollo RGB, un Anchor rappresenta un insieme di dati lato client utilizzati per dimostrare l'inclusione di un singolo Commitment in una transazione. Nel protocollo RGB, un Anchor è composto dai seguenti Elements:




- transaction ID Bitcoin (txid) da Witness Transaction ;
- Multi Protocol Commitment (MPC);
- Deterministic Bitcoin Commitment (DBC);
- Extra Transaction Proof (ETP) se si utilizza il meccanismo Tapret Commitment.


Un Anchor serve quindi a stabilire un collegamento verificabile tra una specifica transazione Bitcoin e i dati privati validati dal protocollo RGB. Garantisce che questi dati sono effettivamente inclusi nel Blockchain, senza che il loro contenuto esatto sia reso pubblico.