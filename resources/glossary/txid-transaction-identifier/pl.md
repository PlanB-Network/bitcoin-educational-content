---
term: txid (IDENTYFIKATOR TRANSAKCJI)
---

Unikalny identyfikator powiązany z każdą transakcją Bitcoin. Jest generowany przez obliczenie `SHA256d` Hash danych transakcji. txid służy jako odniesienie do znalezienia konkretnej transakcji w Blockchain. Jest również używany do odniesienia się do UTXO, który jest zasadniczo konkatenacją txid poprzedniej transakcji i indeksu wyznaczonego wyjścia (zwanego również "vout"). W przypadku transakcji po SegWit, txid nie bierze już pod uwagę świadka transakcji, co eliminuje możliwość modyfikacji.