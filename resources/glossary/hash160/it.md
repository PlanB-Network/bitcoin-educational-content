---
term: HASH160

---
Funzione crittografica utilizzata in Bitcoin, in particolare per generare indirizzi di ricezione Legacy e SegWit v0. Combina due funzioni di hash che vengono eseguite in successione sull'input: prima SHA256, poi RIPEMD160. L'output di questa funzione è quindi di 160 bit.

$${testo{HASH160}(x) = ´testo{RIPEMD160}(´testo{SHA256}(x))$$