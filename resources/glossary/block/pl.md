---
term: BLOK
---

Struktura danych w systemie Bitcoin. Blok zawiera zestaw ważnych transakcji i metadanych zawartych w jego nagłówku. Każdy blok jest połączony z następnym przez Hash jego nagłówka, tworząc w ten sposób Blockchain. Blockchain działa jako serwer znaczników czasu, który pozwala każdemu użytkownikowi poznać wszystkie przeszłe transakcje, aby zweryfikować nieistnienie transakcji i zapobiec podwójnym wydatkom. Transakcje są zorganizowane w Merkle Tree. Ten kryptograficzny akumulator pozwala na utworzenie skrótu wszystkich transakcji w bloku, zwanego "Merkle Root" Nagłówek bloku zawiera 6 Elements:


- Wersja bloku;
- Odcisk poprzedniego bloku;
- Korzeń Merkle Tree transakcji;
- Timestamp bloku;
- Docelowy poziom trudności;
- Nonce.


Aby blok był ważny, musi mieć nagłówek, który po zaszyfrowaniu za pomocą `SHA256d`, daje skrót, który jest mniejszy lub równy docelowemu poziomowi trudności.