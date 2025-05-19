---
term: BIP0113
---

Wprowadzono zmianę w obliczeniach wszystkich operacji timelock (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` i `OP_CHECKSEQUENCEVERIFY`). Określa ona, że aby ocenić ważność blokad czasowych, należy je teraz porównać z MTP (*Median Time Past*), który jest medianą znaczników czasu z ostatnich 11 bloków. Wcześniej używano tylko Timestamp poprzedniego bloku. Metoda ta sprawia, że system jest bardziej przewidywalny i zapobiega manipulowaniu odniesieniem czasowym przez górników. BIP113 został wprowadzony za pośrednictwem Soft Fork w dniu 4 lipca 2016 r., obok BIP68 i BIP112, aktywowanych po raz pierwszy przy użyciu metody BIP9.