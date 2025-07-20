---
term: PRZYMIERZE
---

Mechanizm, który pozwala na nałożenie określonych warunków na sposób, w jaki dana waluta może zostać wydana, w tym w przyszłych transakcjach. Poza warunkami zwykle dozwolonymi przez język skryptowy na UTXO, przymierze wymusza dodatkowe ograniczenia dotyczące sposobu, w jaki ten Bitcoin może zostać wydany w kolejnych transakcjach. Technicznie rzecz biorąc, ustanowienie przymierza ma miejsce, gdy `scriptPubKey` UTXO definiuje ograniczenia na `scriptPubKey` wyjścia transakcji, która wydaje wspomniany UTXO. Rozszerzając zakres skryptu, pakty umożliwiłyby liczne zmiany w Bitcoin, takie jak dwustronne zakotwiczenie łańcuchów napędowych, wdrożenie skarbców lub ulepszenie systemów nakładkowych, takich jak Lightning. Propozycje paktów są zróżnicowane w oparciu o trzy kryteria:


- Ich zakres;
- Ich wdrożenie;
- Ich powtarzalność.


Istnieje wiele propozycji, które pozwoliłyby na stosowanie przymierzy na Bitcoin. Najbardziej zaawansowane w procesie implementacji są: `OP_CHECKTEMPLATEVERIFY` (CTV), `SIGHASH_ANYPREVOUT` (APO) oraz `OP_VAULT`. Wśród innych propozycji znajdują się: `OP_TX`, `OP_TAPLEAFUPDATEVERIFY` (TLUV), `OP_EVICT`, `OP_CHECKSIGFROMSTACKVERIFY` (CSFSV), `OP_CAT` itd.


Aby lepiej zrozumieć koncepcję przymierza, rozważmy następującą analogię: wyobraźmy sobie sejf zawierający 500 euro w drobnych banknotach. Jeśli uda ci się odblokować ten sejf za pomocą odpowiedniego klucza, możesz wykorzystać te pieniądze, jak chcesz. Jest to normalna sytuacja w przypadku Bitcoin. Teraz wyobraź sobie, że ten sam sejf nie zawiera 500 euro w banknotach, ale raczej bony na posiłki o równoważnej wartości. Jeśli uda ci się otworzyć ten sejf, będziesz mógł użyć tej sumy. Twoja swoboda wydawania pieniędzy jest jednak ograniczona, ponieważ możesz używać tych bonów tylko do płacenia w określonych restauracjach. Istnieje więc pierwszy warunek wydania tych pieniędzy, którym jest otwarcie sejfu za pomocą odpowiedniego klucza. Istnieje jednak również dodatkowy warunek dotyczący przyszłego wykorzystania tej kwoty: musi ona zostać wydana wyłącznie w restauracjach partnerskich, a nie dowolnie. Ten system ograniczeń dotyczących przyszłych transakcji nazywany jest przymierzem.


> w języku francuskim nie ma terminu, który dokładnie oddawałby znaczenie słowa "przymierze". Można by mówić o "klauzuli", "pakcie" lub "Commitment", ale nie odpowiadałyby one dokładnie terminowi "przymierze". Termin ten został zapożyczony z terminologii prawniczej, która pozwala opisać klauzulę umowną nakładającą trwałe zobowiązania na nieruchomość*