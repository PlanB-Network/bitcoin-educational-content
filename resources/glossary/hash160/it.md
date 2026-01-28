---
term: HASH160

definition: Funzione che combina SHA256 e poi RIPEMD160, utilizzata per generare indirizzi Bitcoin.
---
Funzione crittografica utilizzata in Bitcoin, in particolare per generare indirizzi di ricezione Legacy e SegWit v0. Combina due funzioni di hash che vengono eseguite in successione sull'input: prima SHA256, poi RIPEMD160. L'output di questa funzione è quindi di 160 bit.

$${testo{HASH160}(x) = ´testo{RIPEMD160}(´testo{SHA256}(x))$$