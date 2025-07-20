---
term: OP_NUMEQUALVERIFY (0X9D)
---

Łączy operacje `OP_NUMEQUAL` i `OP_VERIFY`. Numerycznie porównuje dwie najwyższe wartości Elements na stosie. Jeśli wartości są równe, `OP_NUMEQUALVERIFY` usuwa prawdziwy wynik ze stosu i kontynuuje wykonywanie skryptu. Jeśli wartości nie są równe, wynikiem jest fałsz, a skrypt natychmiast kończy się niepowodzeniem.