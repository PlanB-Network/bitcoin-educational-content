---
term: WTXID
---

Proširenje tradicionalnog txid, uključujući podatke svedoka uvedene sa SegWit. Dok je txid Hash transakcijskih podataka isključujući svedoka, WTXID je `SHA256d` celokupnih transakcijskih podataka, uključujući svedoka. WTXID-ovi su smešteni u zasebnom Merkle Tree čiji je koren postavljen u Coinbase Transaction. Ovo razdvajanje omogućava uklanjanje promenljivosti transakcija txid.