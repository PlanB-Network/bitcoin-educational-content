---
term: WTXID
---

Rozszerzenie tradycyjnego txid, obejmujące dane świadka wprowadzone w SegWit. Podczas gdy txid jest Hash danych transakcji z wyłączeniem świadka, WTXID jest `SHA256d` całych danych transakcji, w tym świadka. WTXID są przechowywane w oddzielnym Merkle Tree, którego korzeń jest umieszczony w Coinbase Transaction. Ta separacja pozwala na usunięcie zmienności transakcji txid.