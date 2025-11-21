---
term: ŚR. CZAS TRWANIA RUNDY
---

Średni czas trwania rundy jest wskaźnikiem używanym do oszacowania czasu potrzebnego Mining pool na znalezienie bloku, w oparciu o trudność sieci i Hashrate puli. Oblicza się go, biorąc liczbę akcji oczekiwanych do znalezienia bloku i dzieląc ją przez Hashrate puli. Na przykład, jeśli Mining pool ma 200 górników, a każdy z nich generuje średnio 4 akcje na sekundę, całkowita moc obliczeniowa puli wynosi 800 akcji na sekundę:


```text
200 * 4 = 800
```


Zakładając, że znalezienie ważnego bloku zajmuje średnio 1 milion akcji, *Avg. Round Duration* wynosiłby 1250 sekund, czyli około 21 minut:


```text
1,000,000 / 800 = 1,250
```


W praktyce oznacza to, że średnio Mining pool powinien znajdować blok co około 21 minut. Wskaźnik ten zmienia się wraz ze zmianami Hashrate puli: wzrost Hashrate zmniejsza *Avg. Czas trwania rundy*, podczas gdy spadek wydłuża go. Będzie się on również zmieniał wraz z każdym okresowym dostosowaniem docelowego poziomu trudności Bitcoin (co 2016 bloków). Ta miara nie uwzględnia bloków znalezionych przez inne pule i skupia się wyłącznie na wewnętrznej wydajności badanej puli.