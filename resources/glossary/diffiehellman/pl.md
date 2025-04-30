---
term: DIFFIE-HELLMAN
---

Metoda kryptograficzna, która umożliwia dwóm stronom generate wspólny sekret za pośrednictwem niezabezpieczonego kanału komunikacyjnego. Sekret ten może być następnie wykorzystany do szyfrowania komunikacji między dwiema stronami. Diffie-Hellman wykorzystuje arytmetykę modularną, więc nawet jeśli atakujący może obserwować wymianę danych, nie może wydedukować współdzielonego sekretu bez rozwiązania trudnego problemu matematycznego: logarytmu dyskretnego. W Bitcoin, wariant DH zwany ECDH, który wykorzystuje krzywą eliptyczną, jest czasami używany, szczególnie w statycznych protokołach Address, takich jak Silent Payments lub BIP47.