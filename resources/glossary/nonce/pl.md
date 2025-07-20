---
term: Nonce
---

W kontekście informatyki termin "Nonce" odnosi się do liczby, która jest używana tylko raz, a następnie zastępowana. Często jest ona losowa lub pseudolosowa. Nonces są używane w różnych protokołach kryptograficznych w celu zapewnienia bezpieczeństwa procesu. Na przykład podpisy ECDSA używane w protokole Bitcoin obejmują użycie Nonce. Oznacza to, że liczba ta musi być nowa dla każdego podpisu. Jeśli tak nie jest, możliwe jest obliczenie używanego klucza prywatnego poprzez porównanie dwóch podpisów, które używają tego samego Nonce.


Nonces są również używane w procesie Bitcoin Mining. Górnicy zwiększają te modyfikowalne wartości w swoich blokach kandydujących. Modyfikują oni wartość Nonce w celu znalezienia kryptograficznego Hash, który jest niższy lub równy docelowemu poziomowi trudności. Proces ten wymaga znacznej mocy obliczeniowej, ponieważ obejmuje wyczerpujące wyszukiwanie wśród dużej liczby możliwych nonces. Gdy Miner znajdzie Nonce, który po włączeniu do jego bloku tworzy skrót spełniający kryteria trudności, blok jest transmitowany do sieci, a Miner wygrywa nagrodę.


> w 2010 roku badacze odkryli, że konsola PlayStation 3 firmy Sony używała tego samego Nonce do podpisywania różnych pakietów kodu. Ponowne wykorzystanie Nonce pozwoliło atakującym na obliczenie klucza prywatnego używanego do podpisywania oprogramowania. Mając klucz prywatny w ręku, atakujący mogli tworzyć ważne podpisy dla dowolnego kodu, umożliwiając im uruchamianie nieautoryzowanego oprogramowania, w tym pirackich gier lub niestandardowych systemów operacyjnych, bezpośrednio na PS3 *

> istnieje powszechne błędne przekonanie o pochodzeniu terminu "Nonce" Niektórzy twierdzą, że jest to skrót od "liczby używanej tylko raz" W rzeczywistości pochodzenie tego słowa sięga XVIII wieku i wywodzi się z semantycznej ewolucji staroangielskiego wyrażenia "then anes", które oznaczało "na okazję"