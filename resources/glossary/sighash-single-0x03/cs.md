---
term: SIGHASH_SINGLE (0X03)

---
Typ příznaku SigHash Příznak používaný v podpisech bitcoinových transakcí, který označuje, že podpis se vztahuje na všechny vstupy transakce a pouze na jeden výstup, který odpovídá indexu stejného podepsaného vstupu. Každý vstup podepsaný příznakem `SIGHASH_SINGLE` je tedy specificky spojen s konkrétním výstupem. Ostatní výstupy nejsou podpisem vázány, a proto je lze později upravit. Tento typ podpisu je užitečný u složitých transakcí, kde účastníci chtějí propojit určité vstupy s konkrétními výstupy a zároveň ponechat flexibilitu pro ostatní výstupy transakce.