---
term: OP_CHECKSIGVERIFY (0XAD)
---

Wykonuje tę samą operację co `OP_CHECKSIG`, ale jeśli weryfikacja podpisu nie powiedzie się, skrypt natychmiast zatrzymuje się z błędem, a transakcja jest nieważna. Jeśli weryfikacja się powiedzie, skrypt kontynuuje bez wypychania wartości `1` (true) na stos. Podsumowując, `OP_CHECKSIGVERIFY` wykonuje operację `OP_CHECKSIG`, po której następuje `OP_VERIFY`. Ten opcode został zmodyfikowany w Tapscript w celu weryfikacji podpisów Schnorra.