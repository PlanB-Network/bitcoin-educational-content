---
term: HASH160
---

Funzione crittografica utilizzata in Bitcoin, in particolare per la generazione di indirizzi di ricezione Legacy e SegWit v0. Combina due funzioni di hash che vengono eseguite successivamente sull'input: prima SHA256, poi RIPEMD160. L'output di questa funzione è quindi di 160 bit.

$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$