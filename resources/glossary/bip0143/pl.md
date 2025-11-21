---
term: BIP0143
---

Wprowadza nowy sposób haszowania transakcji w celu weryfikacji podpisu w skryptach post-SegWit. Celem jest zminimalizowanie zbędnych operacji podczas weryfikacji i uwzględnienie wartości UTXO w danych wejściowych w podpisie. Rozwiązuje to dwa główne problemy związane z oryginalnym algorytmem haszowania transakcji:


- Kwadratowy wzrost haszowania danych wraz z liczbą podpisów;
- Brak uwzględnienia wartości wejściowej w podpisie, co stanowiło ryzyko dla portfeli sprzętowych, zwłaszcza w odniesieniu do wiedzy o poniesionych opłatach transakcyjnych.

Ponieważ aktualizacja SegWit, wyjaśniona w BIP141, wprowadza nową formę transakcji, których skrypt nie będzie weryfikowany przez stare węzły, BIP143 wykorzystuje tę okazję do Address tej kwestii bez konieczności Hard Fork. Dlatego BIP143 jest częścią SegWit Soft Fork.