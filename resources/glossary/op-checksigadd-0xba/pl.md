---
term: OP_CHECKSIGADD (0XBA)
---

Wyodrębnia trzy górne wartości ze stosu: `klucz publiczny`, `n` `CScriptNum` i `podpis`. Jeśli podpis nie jest pustym wektorem i nie jest ważny, skrypt kończy działanie z błędem. Jeśli podpis jest ważny lub jest pustym wektorem (`OP_0`), prezentowane są dwa scenariusze:


- Jeśli sygnaturą jest pusty wektor: `CScriptNum` z wartością `n` jest wypychane na stos i wykonywanie jest kontynuowane;
- Jeśli sygnatura nie jest pustym wektorem i pozostaje ważna: `CScriptNum` z wartością `n + 1` jest wypychane na stos i wykonywanie jest kontynuowane.

Dla uproszczenia, `OP_CHECKSIGADD` wykonuje operację podobną do `OP_CHECKSIG`, ale zamiast przesuwać true lub false na stos, dodaje `1` do drugiej wartości na szczycie stosu, jeśli podpis jest ważny, lub pozostawia tę wartość bez zmian, jeśli podpis reprezentuje pusty wektor. `OP_CHECKSIGADD` pozwala na tworzenie takich samych polityk wielopodpisowych w Tapscript, jak w przypadku `OP_CHECKMULTISIG` i `OP_CHECKMULTISIGVERIFY`, ale w sposób weryfikowalny wsadowo, co oznacza, że usuwa proces wyszukiwania w weryfikacji tradycyjnego Multisig, a tym samym przyspiesza weryfikację, jednocześnie zmniejszając obciążenie operacyjne procesorów węzłów. Ten kod operacyjny został dodany w Tapscript wyłącznie na potrzeby Taproot.