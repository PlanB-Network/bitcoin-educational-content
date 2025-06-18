---
term: BIP0066
---

Wprowadzono standaryzację formatu podpisu w transakcjach. Ten BIP został zaproponowany w odpowiedzi na rozbieżności w sposobie, w jaki OpenSSL obsługiwał kodowanie podpisów w różnych systemach. Ta heterogeniczność stwarzała ryzyko podziału Blockchain. BIP66 ustandaryzował format podpisu dla wszystkich transakcji przy użyciu ścisłego kodowania DER (*Distinguished Encoding Rules*). Zmiana ta wymagała Soft Fork. W celu aktywacji BIP66 wykorzystał ten sam mechanizm, co BIP34, wymagając zwiększenia pola `nVersion` do wersji 3 i odrzucając wszystkie bloki w wersji 2 lub niższej po osiągnięciu progu 95% Miner. Próg ten został przekroczony w bloku numer 363,725 w dniu 4 lipca 2015 roku.