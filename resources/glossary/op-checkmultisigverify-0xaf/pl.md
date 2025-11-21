---
term: OP_CHECKMULTISIGVERIFY (0XAF)
---

Łączy `OP_CHECKMULTISIG` i `OP_VERIFY`. Pobiera wiele podpisów i kluczy publicznych, aby sprawdzić, czy `M` z `N` podpisów jest ważnych, tak jak robi to `OP_CHECKMULTISIG`. Następnie, podobnie jak w przypadku `OP_VERIFY`, jeśli weryfikacja nie powiedzie się, skrypt natychmiast zatrzyma się z błędem. Jeśli weryfikacja się powiedzie, skrypt kontynuuje działanie bez wypychania żadnej wartości na stos. Ten kod operacyjny został usunięty w Tapscript.