---
term: PSBT
---

Skrót od "Partially Signed Bitcoin Transaction". Jest to specyfikacja wprowadzona wraz z BIP174 w celu standaryzacji sposobu, w jaki niedokończone transakcje są konstruowane w oprogramowaniu związanym z Bitcoin, takim jak oprogramowanie Wallet. PSBT hermetyzuje transakcję, w której dane wejściowe mogą nie być w pełni podpisane. Zawiera on wszystkie informacje niezbędne uczestnikowi do podpisania transakcji bez konieczności podawania dodatkowych danych. W związku z tym PSBT może przybierać 3 różne formy:


- W pełni skonstruowana transakcja, ale jeszcze nie podpisana;
- Częściowo podpisana transakcja, w której niektóre dane wejściowe są podpisane, a inne jeszcze nie;
- Lub w pełni podpisana transakcja Bitcoin, którą można przekonwertować, aby była gotowa do transmisji w sieci.


Format PSBT ułatwia interoperacyjność między różnym oprogramowaniem Wallet i urządzeniami podpisującymi (Hardware Wallet). Obecnie używana jest wersja 0 formatu PSBT, jak określono w BIP174, ale wersja 2 jest proponowana za pośrednictwem BIP370.


> wersja 1 PSBT nie istnieje. Ponieważ wersja 0 była pierwszą wersją, druga wersja została nieformalnie nazwana wersją 2. Ava Chow, która jest autorką BIP370, zdecydowała się przypisać numer 2 do tej nowej wersji, aby uniknąć zamieszania