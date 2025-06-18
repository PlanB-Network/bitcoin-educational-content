---
term: FRAZA ODZYSKIWANIA
---

Fraza odzyskiwania, czasami nazywana również frazą Mnemonic, seed lub tajną frazą, to sekwencja zwykle składająca się z 12 lub 24 słów, która jest generowana w sposób pseudolosowy ze źródła entropii. Sekwencja pseudolosowa jest zawsze uzupełniana sumą kontrolną. Fraza Mnemonic, wraz z opcjonalną passphrase, jest używana do deterministycznego wyprowadzenia wszystkich kluczy powiązanych z HD (Hierarchical Deterministic) Wallet. Oznacza to, że na podstawie tej frazy możliwe jest deterministyczne generate i odtworzenie wszystkich kluczy prywatnych i publicznych Bitcoin Wallet, a w konsekwencji uzyskanie dostępu do powiązanych z nim środków. Celem frazy odzyskiwania jest zapewnienie sposobu tworzenia kopii zapasowych i odzyskiwania bitcoinów, który jest zarówno bezpieczny, jak i łatwy w użyciu.


Ważne jest, aby przechowywać tę frazę w bezpiecznym miejscu, ponieważ każdy, kto jest w posiadaniu Mnemonic, miałby dostęp do środków odpowiedniego Wallet. Jeśli jest używany w kontekście tradycyjnego Wallet i bez opcjonalnego passphrase, często stanowi SPOF (Single Point Of Failure). Fraza odzyskiwania jest zatem kodowaniem sekwencji pseudolosowej i sumy kontrolnej w codziennych słowach, aby ułatwić jej zapis i czytelność dla ludzi. Jest ona skonstruowana zgodnie ze standardem BIP39, który definiuje i porządkuje listę 2048 słów używanych do tego kodowania.


> lista 2048 słów z BIP39 jest dostępna w kilku językach, jednak zaleca się korzystanie tylko z wersji angielskiej, ponieważ jest ona najczęściej obsługiwana przez oprogramowanie Wallet