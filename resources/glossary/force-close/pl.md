---
term: WYMUŚ ZAMKNIĘCIE
---

Niekooperacyjny mechanizm zamykania kanałów Lightning. Gdy dwóch użytkowników otworzy kanał z Multisig 2/2, każdy z nich może jednostronnie zamknąć kanał, transmitując ostatni Commitment Transaction, który został już podpisany, w celu odzyskania swoich bitcoinów onchain. Jest to znane jako "wymuszenie zamknięcia".


Ta metoda jest zwykle stosowana, gdy jeden z uczestników przestaje odpowiadać lub gdy kooperacyjne zamknięcie kanału jest niemożliwe. Jeśli można uniknąć wymuszenia zamknięcia, jest to najlepsze rozwiązanie, ponieważ odzyskanie środków onchain trwa dłużej i może być znacznie droższe pod względem opłat.


Podczas wymuszonego zamknięcia jeden z dwóch użytkowników nadaje Commitment Transaction, który odzwierciedla ostatni znany stan kanału Lightning. Następnie następuje blokada czasowa, zanim bitcoiny mogą zostać odzyskane w łańcuchu, dając drugiej stronie czas na zweryfikowanie, czy transakcja odpowiada najnowszemu stanowi kanału. Jeśli użytkownik próbuje oszukiwać, publikując nieaktualny Commitment Transaction, druga strona może użyć sekretu odwołania, aby ukarać oszusta i odzyskać wszystkie środki w kanale.