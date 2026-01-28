---
term: OP_CHECKSIG (0XAC)
definition: Opkod sprawdzający ważność podpisu względem klucza publicznego.
---

Weryfikuje ważność podpisu względem danego klucza publicznego. Pobiera dwa górne Elements ze stosu: podpis i klucz publiczny i ocenia, czy podpis jest poprawny dla transakcji Hash i określonego klucza publicznego. Jeśli weryfikacja przebiegnie pomyślnie, na stos trafia wartość `1` (prawda), w przeciwnym razie `0` (fałsz). Ten kod operacyjny został zmodyfikowany w Tapscript w celu weryfikacji podpisów Schnorra.