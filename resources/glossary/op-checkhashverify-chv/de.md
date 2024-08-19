---
term: OP_CHECKHASHVERIFY (CHV)
---

Ein neuer Opcode, der 2012 in BIP17 von Luke Dashjr vorgeschlagen wurde und die gleichen Funktionen wie `OP_EVAL` oder P2SH bieten sollte. Er war dazu gedacht, das Ende des `scriptSig` zu hashen, das Ergebnis mit dem obersten Element des Stacks zu vergleichen und die Transaktion für ungültig zu erklären, wenn die beiden Hashes nicht übereinstimmten. Dieser Opcode wurde nie implementiert.