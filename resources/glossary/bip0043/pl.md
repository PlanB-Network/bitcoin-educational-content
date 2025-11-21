---
term: BIP0043
---

Propozycja ulepszenia, która wprowadza użycie poziomu ścieżki derywacji do opisania pola celu w strukturze portfeli HD, wcześniej wprowadzonego w BIP32. Zgodnie z BIP43, pierwszy poziom derywacji HD Wallet, zaraz po kluczu głównym oznaczonym jako `m/`, jest zarezerwowany dla numeru celu, który wskazuje standard derywacji używany w pozostałej części ścieżki. Numer ten jest zapisywany jako indeks hartowany. Na przykład, jeśli Wallet jest zgodny ze standardem SegWit (BIP84), początkiem jego ścieżki derywacji będzie: `m/84'/`. BIP43 pozwala zatem na wyjaśnienie standardów przestrzeganych przez każde oprogramowanie Wallet, aby zapewnić lepszą interoperacyjność między nimi. Standaryzacja pozostałej części ścieżki derywacji jest opisana w BIP44.