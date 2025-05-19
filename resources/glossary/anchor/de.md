---
term: Anchor
---

Im RGB-Protokoll stellt ein Anchor einen Satz von clientseitigen Daten dar, die zum Nachweis der Einbeziehung eines einzelnen Commitment in eine Transaktion verwendet werden. Im RGB-Protokoll setzt sich ein Anchor aus den folgenden Elements zusammen:




- transaction ID Bitcoin (txid) von Witness Transaction ;
- Multi Protocol Commitment (MPC);
- Deterministic Bitcoin Commitment (DBC);
- Extra Transaction Proof (ETP), wenn der Tapret Commitment Mechanismus verwendet wird.


Ein Anchor dient daher dazu, eine überprüfbare Verbindung zwischen einer bestimmten Bitcoin-Transaktion und privaten Daten herzustellen, die durch das RGB-Protokoll validiert wurden. Sie garantiert, dass diese Daten tatsächlich in Blockchain enthalten sind, ohne dass ihr genauer Inhalt öffentlich gemacht wird.