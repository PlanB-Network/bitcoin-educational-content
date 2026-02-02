---
term: Anchor
definition: I RGB-protokollen, en uppsättning data som bevisar inkluderingen av ett åtagande i en Bitcoin-transaktion, utan att offentligt avslöja dess innehåll.
---

I RGB-protokollet representerar en Anchor en uppsättning data på klientsidan som används för att bevisa att en enda Commitment ingår i en transaktion. I RGB-protokollet består en Anchor av följande Elements:




- transaction ID Bitcoin (txid) från Witness Transaction ;
- Multi Protocol Commitment (MPC);
- Deterministic Bitcoin Commitment (DBC);
- Extra transaktionsbevis (ETP) om mekanismen Tapret Commitment används.


En Anchor tjänar därför till att upprätta en verifierbar länk mellan en specifik Bitcoin-transaktion och privata data som validerats av RGB-protokollet. Det garanterar att dessa data verkligen ingår i Blockchain, utan att deras exakta innehåll offentliggörs.