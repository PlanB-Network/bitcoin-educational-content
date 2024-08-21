---
term: SIGHASH_SINGLE (0X03)
---

Typ příznaku SigHash používaný v podpisech transakcí Bitcoinu, který indikuje, že podpis se vztahuje na všechny vstupy transakce a pouze na jeden výstup, odpovídající indexu stejného vstupu, který byl podepsán. Tímto způsobem je každý vstup podepsaný s `SIGHASH_SINGLE` specificky propojen s určitým výstupem. Ostatní výstupy nejsou podpisem zahrnuty a mohou být tedy později modifikovány. Tento typ podpisu je užitečný v komplexních transakcích, kde účastníci chtějí propojit určité vstupy s konkrétními výstupy, zatímco ponechávají flexibilitu pro ostatní výstupy transakce.