---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)
---

Sprawia, że transakcja jest nieważna, chyba że wszystkie te warunki są spełnione:


- Stos nie jest pusty;
- Wartość na szczycie stosu jest większa lub równa `0`;
- Typ blokady czasowej jest taki sam pomiędzy polem `nLockTime` i wartością na szczycie stosu (czas rzeczywisty lub numer bloku);
- Pole `nSequence` wejścia nie jest równe `0xffffffff`;
- Wartość na szczycie stosu jest większa lub równa wartości pola `nLockTime` transakcji.


Jeśli którykolwiek z tych warunków nie jest spełniony, skrypt zawierający `OP_CHECKLOCKTIMEVERIFY` nie może zostać spełniony. Jeśli wszystkie te warunki są ważne, to `OP_CHECKLOCKTIMEVERIFY` działa jak `OP_NOP`, co oznacza, że nie wykonuje żadnej akcji na skrypcie. To tak, jakby znikał. `OP_CHECKLOCKTIMEVERIFY` nakłada zatem ograniczenie czasowe na wydawanie UTXO zabezpieczonego zawierającym go skryptem. Może to zrobić w formie uniksowej daty czasowej lub jako numer bloku. Aby to zrobić, ogranicza możliwe wartości dla pola `nLockTime` transakcji, która je wydaje, a samo pole `nLockTime` ogranicza, kiedy transakcja może być zawarta w bloku.


> ten opcode jest zamiennikiem dla `OP_NOP`. Został on umieszczony na `OP_NOP2`. Jest on często określany skrótem "CLTV". Uwaga, `OP_CLTV` nie powinno być mylone z polem `nLockTime` transakcji. To pierwsze wykorzystuje to drugie, ale ich natura i działanie są różne.*