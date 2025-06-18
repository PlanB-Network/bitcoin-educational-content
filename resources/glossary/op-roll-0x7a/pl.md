---
term: OP_ROLL (0X7A)
---

Przenosi element ze stosu na jego wierzchołek, w oparciu o głębokość określoną przez wartość na wierzchołku stosu przed operacją. Na przykład, jeśli wartość na wierzchołku stosu wynosi `4`, `OP_ROLL` wybierze czwarty element od wierzchołka stosu i przeniesie tę wartość na wierzchołek. `OP_ROLL` pełni tę samą funkcję co `OP_PICK`, z wyjątkiem tego, że usuwa element z jego pierwotnej pozycji.