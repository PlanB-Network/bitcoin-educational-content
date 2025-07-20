---
term: OP_TOALTSTACK (0X6B)
---

Pobiera wierzchołek głównego stosu (*main stack*) i przenosi go na stos alternatywny (*alt stack*). Ten kod operacyjny jest używany do tymczasowego przechowywania danych do późniejszego wykorzystania w skrypcie. Przeniesiony element jest w ten sposób usuwany z głównego stosu. opcja `OP_FROMALTSTACK` zostanie następnie użyta do umieszczenia go z powrotem na szczycie głównego stosu.