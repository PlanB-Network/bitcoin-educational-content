---
term: FLAGA SIGHASH
---

Parametr w transakcji Bitcoin, który określa, które składniki transakcji (wejścia i wyjścia) są objęte powiązanym podpisem, a tym samym stają się niezmienne. SigHash Flag jest bajtem dodawanym do podpisu cyfrowego każdego wejścia. Dlatego wybór SigHash Flag bezpośrednio wpływa na to, które części transakcji są zamrożone przez podpis, a które mogą być później modyfikowane. Mechanizm ten zapewnia, że podpisy precyzyjnie i bezpiecznie zatwierdzają dane transakcji zgodnie z intencją podpisującego. Istnieją trzy główne flagi SigHash:



- `SIGHASH_ALL` (`0x01`): Podpis ma zastosowanie do wszystkich wejść i wyjść transakcji, blokując je całkowicie;



- `SIGHASH_NONE` (`0x02`): Podpis dotyczy wszystkich wejść, ale żadnego z wyjść, pozwalając na modyfikację wyjść po podpisie;



- `SIGHASH_SINGLE` (`0x03`): Podpis obejmuje wszystkie wejścia i tylko jedno wyjście odpowiadające indeksowi podpisanego wejścia.


Oprócz tych trzech flag SigHash, modyfikator `SIGHASH_ANYONECANPAY` (`0x80`) może być połączony z każdym z poprzednich typów. Gdy ten modyfikator jest używany, tylko część danych wejściowych jest podpisywana, pozostawiając inne otwarte do modyfikacji. Oto istniejące kombinacje z tym modyfikatorem:



- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): Podpis ma zastosowanie do pojedynczego wejścia, obejmując jednocześnie wszystkie wyjścia transakcji;



- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): Sygnatura obejmuje pojedyncze wejście, bez zobowiązywania się do jakiegokolwiek wyjścia;



- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): Sygnatura ma zastosowanie do pojedynczego wejścia i tylko do wyjścia o tym samym indeksie co to wejście.


> synonimem czasami używanym dla "SigHash" jest "Signature Hash Types"