---
term: Anchor
---

V protokolu RGB představuje Anchor sadu dat na straně klienta, která slouží k prokázání zařazení jednoho Commitment do transakce. V protokolu RGB je Anchor tvořen následujícími Elements:




- transaction ID Bitcoin (txid) z Witness Transaction ;
- Multi Protocol Commitment (MPC);
- Deterministic Bitcoin Commitment (DBC);
- Extra Transaction Proof (ETP), pokud je použit mechanismus Tapret Commitment.


Protokol Anchor proto slouží k vytvoření ověřitelného spojení mezi konkrétní transakcí Bitcoin a soukromými údaji ověřenými protokolem RGB. Zaručuje, že tato data jsou skutečně obsažena v Blockchain, aniž by byl zveřejněn jejich přesný obsah.