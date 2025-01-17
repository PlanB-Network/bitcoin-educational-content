---
term: OP_CHECKHASHVERIFY (CHV)

---
Ein neuer Opcode, der 2012 in BIP17 von Luke Dashjr vorgeschlagen wurde und die gleichen Funktionen wie `OP_EVAL` oder P2SH bieten würde. Er sollte das Ende der `scriptSig` hashen, das Ergebnis mit dem oberen Ende des Stapels vergleichen und die Transaktion ungültig machen, wenn die beiden Hashes nicht übereinstimmen. Dieser Opcode wurde nie implementiert.