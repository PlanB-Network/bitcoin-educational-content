---
term: INDEKS (KLUCZ)
---

W kontekście portfela HD odnosi się do sekwencyjnego numeru przypisanego do klucza podrzędnego wygenerowanego z klucza nadrzędnego. Indeks ten jest używany w połączeniu z kluczem nadrzędnym i kodem ciągu nadrzędnego w celu deterministycznego uzyskania unikalnych kluczy podrzędnych. Umożliwia uporządkowaną organizację i powtarzalne generowanie wielu par siostrzanych kluczy podrzędnych z jednego klucza nadrzędnego. Jest to 32-bitowa liczba całkowita używana w funkcji wyprowadzania `HMAC-SHA512`. Numer ten może być używany do rozróżniania kluczy podrzędnych w ramach portfela HD.