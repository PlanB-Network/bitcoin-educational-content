---
term: NULLDUMMY
---

Reguła konsensusu wprowadzona wraz z BIP147 w SegWit Soft Fork, która wymaga, aby fikcyjny element używany w kodach operacyjnych `OP_CHECKMULTISIG` i `OP_CHECKMULTISIGVERIFY` był pustą tablicą bajtów (`OP_0`). Środek ten został zaimplementowany w celu wyeliminowania wektora podatności na manipulacje poprzez zakazanie jakiejkolwiek wartości innej niż `OP_0` dla tego elementu.