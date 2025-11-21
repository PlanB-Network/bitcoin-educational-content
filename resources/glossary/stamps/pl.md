---
term: STEMPLE
---

Protokół umożliwiający integrację sformatowanych danych obrazu bezpośrednio na Bitcoin Blockchain poprzez surowe transakcje wielopodpisowe (P2MS). Stamps koduje binarną zawartość obrazu w base 64 i dodaje ją do kluczy 1/3 P2MS. Jeden klucz jest prawdziwy i służy do wydawania środków, podczas gdy pozostałe dwa są kluczami fikcyjnymi (powiązany klucz prywatny jest nieznany), które przechowują dane. Kodując dane bezpośrednio jako klucze publiczne, a nie używając danych wyjściowych `OP_RETURN`, obrazy przechowywane za pomocą protokołu Stamps są szczególnie obciążające dla węzłów. Metoda ta w szczególności tworzy wiele UTXO, co zwiększa rozmiar zestawu UTXO i stwarza problemy dla pełnych węzłów.