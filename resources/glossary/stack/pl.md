---
term: BATERIA
---

W kontekście języka skryptowego używanego do dołączania warunków wydatkowania do Bitcoin UTXO, stos jest strukturą danych LIFO (*Last In, First Out*) używaną do przechowywania tymczasowych Elements podczas wykonywania skryptu. Każda operacja w skrypcie manipuluje tymi stosami, gdzie Elements mogą być dodawane (*push*) lub usuwane (*pop*). Skrypty wykorzystują stosy do oceny wyrażeń, przechowywania zmiennych tymczasowych i zarządzania warunkami.


Podczas wykonywania skryptu Bitcoin mogą być używane 2 stosy: stos główny i stos alternatywny. Stos główny jest używany do większości operacji skryptu. To na tym stosie operacje skryptu dodają, usuwają lub manipulują danymi. Z kolei stos alternatywny służy do tymczasowego przechowywania danych podczas wykonywania skryptu. Określone kody operacyjne, takie jak `OP_TOALTSTACK` i `OP_FROMALTSTACK`, umożliwiają przeniesienie Elements z głównego stosu na stos alternatywny i odwrotnie.


Na przykład, gdy transakcja jest zatwierdzana, podpisy i klucze publiczne są przesuwane na główny stos i przetwarzane przez kolejne kody operacyjne w celu sprawdzenia, czy podpisy są zgodne z kluczami i danymi transakcji.