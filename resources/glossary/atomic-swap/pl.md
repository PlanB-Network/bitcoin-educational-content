---
term: ZAMIANA ATOMÓW
---

Technologia umożliwiająca bezpośrednie Exchange kryptowalut między dwiema stronami, bez potrzeby zaufania i bez pośrednika. Wymiany te nazywane są "atomowymi", ponieważ mogą skutkować tylko dwoma rezultatami:


- Albo Exchange zakończy się sukcesem, a obaj uczestnicy skutecznie wymienią swoje kryptowaluty;
- Albo Exchange nie powiedzie się i obaj uczestnicy odejdą ze swoimi oryginalnymi kryptowalutami.


Swapy atomowe mogą być przeprowadzane zarówno z tą samą kryptowalutą, w którym to przypadku określa się je również jako "*coinswap*", jak i pomiędzy różnymi kryptowalutami. W przeszłości opierały się one na "Hash Time-Locked Contracts" (HTLC), systemie blokady czasowej, który gwarantuje zakończenie lub całkowite anulowanie Exchange, zachowując w ten sposób integralność funduszy zaangażowanych stron. Metoda ta wymagała protokołów zdolnych do obsługi zarówno skryptów, jak i blokad czasowych. Jednak w ostatnich latach trend przesunął się w kierunku wykorzystania *Adaptor Signatures*. To drugie podejście ma tę zaletę, że eliminuje potrzebę stosowania skryptów, zmniejszając tym samym koszty operacyjne. Jego inną ważną zaletą jest to, że nie wymaga użycia identycznego haszowania dla obu części transakcji, co pomaga uniknąć ujawnienia powiązania między nimi.