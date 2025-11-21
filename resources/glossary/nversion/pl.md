---
term: WERSJA
---

Pole `nVersion` w transakcji Bitcoin jest używane do wskazania wersji używanego formatu transakcji. Pozwala to sieci na rozróżnienie różnych ewolucji formatu transakcji w czasie i zastosowanie odpowiednich reguł. Pole to nie ma wpływu na zasady konsensusu. Oznacza to, że jakakolwiek wartość przypisana do tego pola nie powoduje unieważnienia transakcji. Jednakże, pole `nVersion` posiada reguły standaryzacji, które obecnie akceptują tylko wartości `1` i `2`. Na razie pole to jest użyteczne tylko do aktywacji pola `nSequence`.