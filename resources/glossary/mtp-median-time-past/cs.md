---
term: MTP (MEDIAN TIME PAST)
---

Tento koncept se používá v protokolu Bitcoinu k určení marže na časové značce konsensu sítě. MTP je definován jako medián časových značek posledních 11 vyťažených bloků. Použití tohoto ukazatele pomáhá zabránit neshodám mezi uzly ohledně přesného času v případě rozdílů. MTP bylo původně používáno k ověření platnosti časových značek bloků vzhledem k minulosti. Od BIP113 se také používá jako referenční bod pro síťový čas k ověření platnosti transakcí s časovým zámkem (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` a `OP_CHECKSEQUENCEVERIFY`).