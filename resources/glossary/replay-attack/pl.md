---
term: POWTÓRZENIE ATAKU
---

W kontekście Bitcoin atak replay ma miejsce, gdy ważna transakcja na jednym Blockchain jest złośliwie powielana na innym Blockchain, który ma tę samą historię transakcji. Innymi słowy, transakcja transmitowana na jednym kanale może zostać powielona na innym bez zgody nadawcy pierwszej transakcji.


Weźmy przykład hipotetycznego Hard Fork z Bitcoin, nazwanego "*BitcoinBis*". Jeśli dokonasz płatności w bitcoinach, aby kupić bagietkę od piekarza na prawdziwym Blockchain Bitcoin, ten sam piekarz może odtworzyć tę legalną transakcję na *BitcoinBis*, aby uzyskać tę samą kwotę w kryptowalutach na tym Fork, bez żadnych działań z twojej strony.


Ten rodzaj ataku może wystąpić tylko w przypadku rozgałęzienia Blockchain z 2 niezależnymi łańcuchami, które utrzymują się w czasie. Zazwyczaj ma to miejsce w przypadku Hard Fork. Aby atak replay był możliwy, 2 łańcuchy bloków muszą mieć wspólną historię, a zduplikowana transakcja musi wykorzystywać jako dane wejściowe UTXO utworzone z poprzednich transakcji, które miały miejsce przed rozdzieleniem dwóch łańcuchów, lub z poprzednich transakcji, które same zostały już odtworzone w poprzednim ataku replay.


Ogólnie rzecz biorąc, w informatyce atak typu replay polega na przechwyceniu i ponownym wykorzystaniu ważnych danych w celu oszukania systemu poprzez powtórzenie oryginalnej transmisji. Może to czasami prowadzić do kradzieży tożsamości w sieci.


> w przypadku ataku typu replay na transakcję Bitcoin, jest to czasami określane po prostu jako "transakcja replay". "*