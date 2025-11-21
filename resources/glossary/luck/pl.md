---
term: SZCZĘŚCIE
---

Wskaźnik używany w pulach Mining do pomiaru wydajności puli w stosunku do jej teoretycznych oczekiwań. Jak sugeruje jego nazwa, ocenia on szczęście puli w znalezieniu bloku. Szczęście jest obliczane poprzez porównanie liczby akcji teoretycznie potrzebnych do znalezienia ważnego bloku, w oparciu o bieżącą trudność Bitcoin, z rzeczywistą liczbą akcji wyprodukowanych w celu znalezienia tego bloku. Liczba akcji niższa od oczekiwanej wskazuje na szczęście, podczas gdy wyższa liczba wskazuje na pecha.


Korelując trudność Bitcoin z liczbą akcji produkowanych w każdej sekundzie i trudnością każdej akcji, pula może obliczyć liczbę akcji, które są teoretycznie niezbędne do znalezienia ważnego bloku. Załóżmy na przykład, że teoretycznie pula potrzebuje 100 000 udziałów, aby znaleźć blok. Jeśli pula faktycznie wyprodukuje 200 000 przed znalezieniem bloku, jej szczęście wynosi 50%:


```text
100,000 / 200,000 = 0.5 = 50%
```


I odwrotnie, jeśli ta pula znalazła ważny blok po wyprodukowaniu zaledwie 50 000 akcji, to jej szczęście wynosi 200%:


```text
100,000 / 50,000 = 2 = 200%
```


Luck to wskaźnik, który może być aktualizowany tylko po wykryciu bloku przez pulę, co czyni go statycznym wskaźnikiem, który jest okresowo aktualizowany.