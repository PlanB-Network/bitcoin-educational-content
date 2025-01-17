---
term: MTP (MEDIÁN UPLYNULÉHO ČASU)

---
Tento koncept se v protokolu Bitcoin používá k určení rozpětí časového razítka konsensu sítě. MTP je definován jako medián časových značek posledních 11 vytěžených bloků. Použití tohoto ukazatele pomáhá v případě nesrovnalostí zabránit neshodám mezi uzly ohledně přesného času. MTP byl původně používán k ověření platnosti časových značek bloků oproti minulosti. Od BIP113 se používá také jako reference pro síťový čas k ověření platnosti transakcí časového bloku (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` a `OP_CHECKSEQUENCEVERIFY`).