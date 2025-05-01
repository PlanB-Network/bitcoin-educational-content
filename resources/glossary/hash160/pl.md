---
term: HASH160
---

Funkcja kryptograficzna używana w Bitcoin, zwłaszcza do generowania adresów odbiorczych Legacy i SegWit v0. Łączy ona dwie funkcje Hash, które są wykonywane kolejno na wejściu: najpierw SHA256, a następnie RIPEMD160. Wyjściem tej funkcji jest zatem 160 bitów.


$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$