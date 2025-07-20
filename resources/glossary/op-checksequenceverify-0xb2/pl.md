---
term: OP_CHECKSEQUENCEVERIFY (0XB2)
---

Powoduje, że transakcja staje się nieważna, jeśli zostanie zaobserwowana którakolwiek z tych cech:


- Stos jest pusty;
- Wartość na szczycie stosu jest mniejsza niż `0`;
- Flaga wyłączenia dla wartości na szczycie stosu jest niezdefiniowana i; Wersja transakcji jest mniejsza niż `2` lub; Flaga wyłączenia dla pola `nSequence` wejścia jest ustawiona lub; Typ blokady czasowej nie jest taki sam dla pola `nSequence` i wartości na szczycie stosu (czas rzeczywisty lub liczba bloków) lub; Wartość na szczycie stosu jest większa niż wartość pola `nSequence` wejścia.


Jeśli co najmniej jedna z tych cech jest obserwowana, skrypt zawierający `OP_CHECKSEQUENCEVERIFY` nie może być spełniony. Jeśli wszystkie warunki są prawidłowe, `OP_CHECKSEQUENCEVERIFY` działa jak `OP_NOP`, co oznacza, że nie wykonuje żadnej akcji na skrypcie. To tak, jakby znikał. `OP_CHECKSEQUENCEVERIFY` nakłada zatem względne ograniczenie czasowe na wydawanie UTXO zabezpieczonego zawierającym go skryptem. Może to zrobić w formie czasu rzeczywistego lub jako liczbę bloków. Aby to zrobić, ogranicza możliwe wartości dla pola `nSequence` danych wejściowych, a samo pole `nSequence` ogranicza, kiedy transakcja zawierająca te dane wejściowe może zostać zawarta w bloku.


> ten opcode jest zamiennikiem dla `OP_NOP`. Został on umieszczony na `OP_NOP3`. Jest on często określany skrótem "CSV". Uwaga, `OP_CSV` nie powinno być mylone z polem `nSequence` transakcji. To pierwsze używa tego drugiego, ale ich natura i działanie są różne.*