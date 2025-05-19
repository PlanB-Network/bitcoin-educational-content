---
term: FUNKCJA Hash
---

Funkcja matematyczna, która pobiera dane wejściowe o zmiennym rozmiarze (zwane wiadomością) i generuje dane wyjściowe o stałym rozmiarze (zwane Hash, haszowaniem, skrótem lub odciskiem palca). Funkcje Hash są szeroko stosowanymi prymitywami w kryptografii. Wykazują one specyficzne właściwości, które sprawiają, że nadają się do stosowania w bezpiecznych kontekstach:


- Odporność na preobrazy: musi być bardzo trudno znaleźć wiadomość, która tworzy określony Hash, tj. znaleźć preobraz $m$ dla Hash $h$ taki, że $h = H(m)$, gdzie $H$ jest funkcją Hash;
- Druga odporność na preimage: biorąc pod uwagę wiadomość $m_1$, musi być bardzo trudno znaleźć inną wiadomość $m_2$ (różną od $m_1$) taką, że $H(m_1) = H(m_2)$;
- Odporność na kolizje: znalezienie dwóch różnych wiadomości $m_1$ i $m_2$ takich, że $H(m_1) = H(m_2)$ musi być bardzo trudne;
- Odporność na manipulacje: niewielkie zmiany na wejściu muszą powodować znaczące i nieprzewidywalne zmiany na wyjściu.


W kontekście Bitcoin, funkcje Hash są wykorzystywane do kilku celów, w tym mechanizmu Proof-of-Work (*Proof-of-Work*), identyfikatorów transakcji, generowania Address, obliczeń sum kontrolnych i tworzenia struktur danych, takich jak drzewa Merkle. Po stronie protokołu, Bitcoin używa wyłącznie funkcji `SHA256d`, zwanej również `HASH256`, która składa się z podwójnego `SHA256` Hash. funkcja `HASH256` jest również używana do obliczania niektórych sum kontrolnych, zwłaszcza dla kluczy rozszerzonych (`xpub`, `xprv`...). Po stronie Wallet używane są również następujące elementy:


- Prosty `SHA256` dla sum kontrolnych fraz Mnemonic;
- `SHA512` w ramach algorytmów `HMAC` i `PBKDF2` wykorzystywanych w procesie tworzenia deterministycznych i hierarchicznych portfeli;
- `HASH160`, który opisuje kolejne użycie `SHA256` i `RIPEMD160`. `HASH160` jest używany w procesie generowania adresów odbiorczych (z wyjątkiem P2PK i P2TR) oraz w obliczaniu odcisków palców kluczy nadrzędnych dla kluczy rozszerzonych.


> w języku angielskim jest ona określana jako "funkcja Hash"