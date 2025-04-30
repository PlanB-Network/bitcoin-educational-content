---
term: GOSSIP
---

Gossip je distribuovaný algoritmus peer-to-peer (P2P) pro epidemické šíření informací mezi všemi síťovými agenty. V případě Bitcoin, Lightning a dalších distribuovaných systémů umožňuje tento protokol výměnu a synchronizaci Global State uzlů během několika málo cyklů. Každý uzel šíří informace jednomu nebo více náhodným či nenáhodným sousedům, kteří zase šíří informace dalším sousedům, a tak dále, dokud není dosaženo globálně synchronizovaného stavu.


Gossip je komunikační protokol mezi uzly, který slouží ke sdílení informací o aktuálním stavu a topologii sítě. Protokol gossip umožňuje uzlům znát dynamický stav platebních kanálů a ostatních uzlů a usnadnit tak směrování transakcí v síti, aniž by bylo nutné přímé spojení mezi všemi uzly.


> ► *Francouzský výraz "gossip protocol" by se dal přeložit jako "protocole de bavardage". Zdroj: https://dl.acm.org/doi/pdf/10.1145/41840.41841.*