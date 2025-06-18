---
term: BLOCKS/REV*.DAT
---

Nazwa plików w Bitcoin Core, które przechowują informacje potrzebne do potencjalnego odwrócenia zmian wprowadzonych do zestawu UTXO przez wcześniej dodane bloki. Każdy plik jest identyfikowany przez unikalny numer, który jest taki sam jak plik blk*.dat, któremu odpowiada. Pliki rev*.dat zawierają dane odwrócenia odpowiadające blokom przechowywanym w plikach blk*.dat. Dane te są zasadniczo listą wszystkich UTXO użytych jako wejścia w bloku. Te pliki odwrócenia pozwalają węzłowi powrócić do poprzedniego stanu w przypadku reorganizacji Blockchain, która powoduje odrzucenie wcześniej zatwierdzonych bloków.