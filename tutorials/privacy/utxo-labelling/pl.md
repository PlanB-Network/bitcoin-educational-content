---
name: Etykietowanie UTXO
description: Jak prawidłowo oznaczyć UTXO?
---
![cover](assets/cover.webp)


W tym samouczku dowiesz się wszystkiego, co musisz wiedzieć o etykietowaniu UTXO w Bitcoin Wallet i o kontroli monet. Zaczniemy od części teoretycznej, aby w pełni zrozumieć te koncepcje, a następnie przejdziemy do części praktycznej, w której zbadamy, jak konkretnie używać etykiet w głównym oprogramowaniu Bitcoin Wallet.


## Co to jest oznakowanie UTXO?

"Etykietowanie" to technika polegająca na powiązaniu adnotacji lub etykiety z określonym UTXO w Bitcoin Wallet. Adnotacje te są przechowywane lokalnie przez oprogramowanie Wallet i nigdy nie są przesyłane przez sieć Bitcoin. Etykietowanie jest zatem narzędziem do zarządzania osobistego.


Na przykład, jeśli otrzymam UTXO z transakcji P2P za pośrednictwem Bisq z Charlesem, mogę przypisać mu etykietę `Bisq P2P Purchase Charles`.


Etykietowanie pozwala zapamiętać pochodzenie lub przeznaczenie UTXO, co upraszcza zarządzanie środkami i optymalizuje prywatność użytkownika. Etykietowanie staje się jeszcze bardziej istotne w połączeniu z funkcją "kontroli monet". Kontrola monet jest opcją dostępną w dobrych portfelach Bitcoin, która daje użytkownikowi możliwość ręcznego wyboru, które konkretne UTXO będą używane jako dane wejściowe podczas tworzenia transakcji.


Korzystanie z Wallet z kontrolą monet, w połączeniu z etykietowaniem UTXO, pozwala użytkownikom precyzyjnie rozróżniać i wybierać UTXO dla swoich transakcji, unikając w ten sposób łączenia UTXO z różnych źródeł. Praktyka ta zmniejsza ryzyko związane z heurystyką Common Input Ownership Heuristic (CIOH), która sugeruje wspólne Ownership danych wejściowych transakcji, co może zagrozić prywatności użytkownika.


Wróćmy do przykładu mojego UTXO no-KYC z Bisq; chcę uniknąć łączenia go z UTXO pochodzącym, powiedzmy, z regulowanej platformy Exchange, która zna moją tożsamość. Umieszczając odrębną etykietę na moim UTXO no-KYC i na moim UTXO KYC, będę w stanie łatwo zidentyfikować, który UTXO wykorzystać jako dane wejściowe w celu zaspokojenia wydatków, korzystając z funkcji kontroli monet.


## Jak prawidłowo oznaczyć UTXO?

Nie ma uniwersalnej metody oznaczania UTXO, która odpowiadałaby każdemu. Do użytkownika należy zdefiniowanie systemu etykietowania, aby mógł łatwo odnaleźć się w Wallet.

Kluczowym kryterium przy etykietowaniu jest źródło UTXO. Powinieneś po prostu wskazać, w jaki sposób ta moneta trafiła do Wallet. Czy pochodzi z platformy Exchange? Rozliczenie rachunku przez klienta? Exchange w systemie peer-to-peer? A może reprezentuje zmianę z zakupu? W ten sposób można określić:


- `Wycofanie Exchange.com`;
- `Klient płatności David`;
- `P2P Purchase Charles`;
- `Zmiana z zakupu sofy`.

![labelling](assets/en/1.webp)

Aby udoskonalić zarządzanie UTXO i przestrzegać strategii segregacji funduszy w ramach Wallet, można wzbogacić etykiety o dodatkowy wskaźnik, który odzwierciedla te separacje. Jeśli Wallet zawiera dwie kategorie UTXO, których nie chcesz mieszać, możesz zintegrować znacznik z etykietami, aby wyraźnie odróżnić te grupy.


Te znaczniki separacji będą zależeć od własnych kryteriów, takich jak rozróżnienie między KYC UTXO (znajomość tożsamości) i no-KYC (anonimowość) lub między funduszami zawodowymi i osobistymi. Biorąc pod uwagę wcześniej wspomniane przykłady etykiet, można to przetłumaczyć jako:


- `KYC - Wypłata Exchange.com`;
- `KYC - Klient płatniczy David`;
- `NO KYC - P2P Purchase Charles`;
- `NO KYC - Zmiana z zakupu sofy`.

![labelling](assets/en/2.webp)

W każdym razie należy pamiętać, że dobre oznakowanie to oznakowanie, które będzie zrozumiałe, gdy będzie potrzebne. Jeśli Bitcoin Wallet jest przeznaczony przede wszystkim do oszczędzania, może się okazać, że etykiety będą przydatne dopiero za kilkadziesiąt lat. Dlatego upewnij się, że są one jasne, precyzyjne i wyczerpujące.


Zaleca się również utrwalanie oznaczenia monety w transakcjach. Na przykład, podczas konsolidacji UTXO bez KYC, upewnij się, że wynikowy UTXO jest oznaczony nie tylko jako "konsolidacja", ale konkretnie jako "konsolidacja bez KYC", aby zachować wyraźny ślad pochodzenia monety.


Wreszcie, umieszczanie daty na etykiecie nie jest obowiązkowe. Większość oprogramowania Wallet wyświetla już datę transakcji i zawsze możliwe jest pobranie tej informacji na Block explorer za pomocą txid.


## Samouczek: Etykietowanie w Specter Desktop


Połącz się i otwórz Wallet na Specter Desktop, a następnie wybierz zakładkę `Addresses`.


![labelling](assets/notext/3.webp)

Tutaj zobaczysz listę wszystkich swoich adresów, a także wszystkich bitcoinów, które są na nich zablokowane. Domyślnie adresy są identyfikowane przez ich indeks w kolumnie `Label`. Aby zmienić etykietę, po prostu kliknij na nią, wprowadź żądaną etykietę, a następnie potwierdź, klikając niebieską ikonę.

![labelling](assets/notext/4.webp)


Etykieta pojawi się na liście adresów.


![labelling](assets/notext/5.webp)


Etykietę można również przypisać z wyprzedzeniem, podczas udostępniania odbiorczego Address nadawcy. W tym celu należy przejść do zakładki `Receive` i zapisać etykietę w dedykowanym polu.


![labelling](assets/notext/6.webp)


## Samouczek: Etykietowanie na Electrum


W Electrum Wallet, po zalogowaniu się do Wallet, kliknij transakcję, do której chcesz przypisać etykietę z zakładki `Historia`.


![labelling](assets/notext/7.webp)


Otworzy się nowe okno. Kliknij pole `Opis` i wpisz swoją etykietę.


![labelling](assets/notext/8.webp)


Po wprowadzeniu etykiety można zamknąć to okno.


![labelling](assets/notext/9.webp)


Twoja etykieta została pomyślnie zapisana. Można ją znaleźć w zakładce `Opis`.


![labelling](assets/notext/10.webp)


W zakładce `Coins`, z której można kontrolować monety, etykieta znajduje się w kolumnie `Label`.


![labelling](assets/notext/11.webp)


## Samouczek: Etykietowanie na Green Wallet


W aplikacji Green Wallet uzyskaj dostęp do Wallet i wybierz transakcję, którą chcesz oznaczyć etykietą. Następnie kliknij małą ikonę ołówka, aby zanotować etykietę.


![labelling](assets/notext/12.webp)


Wpisz etykietę, a następnie kliknij przycisk Green `Zapisz`.


![labelling](assets/notext/13.webp)


Etykietę będzie można znaleźć zarówno w szczegółach transakcji, jak i na pulpicie nawigacyjnym Wallet.


![labelling](assets/notext/14.webp)


## Samouczek: Etykietowanie na Samourai Wallet


W Samourai Wallet istnieją różne metody umożliwiające przypisanie etykiety do transakcji. Pierwszą z nich jest otwarcie Wallet i wybranie transakcji, do której chcesz dodać etykietę. Następnie naciśnij przycisk `Add`, znajdujący się obok pola `Notes`.


![labelling](assets/notext/15.webp)


Wpisz swoją etykietę i potwierdź, klikając niebieski przycisk "Dodaj".


![labelling](assets/notext/16.webp)


Etykietę można znaleźć w szczegółach transakcji, ale także na pulpicie nawigacyjnym Wallet.


![labelling](assets/notext/17.webp)

W przypadku drugiej metody, kliknij na trzy małe kropki w prawym górnym rogu ekranu, a następnie na menu `Pokaż niewydane wyniki transakcji`.

![labelling](assets/notext/18.webp)


Tutaj znajdziesz pełną listę wszystkich UTXO obecnych w Twoim Wallet. Wyświetlona lista dotyczy mojego konta depozytowego, jednak operację tę można powielić dla kont Whirlpool, nawigując z dedykowanego menu.


Następnie kliknij UTXO, który chcesz oznaczyć, a następnie przycisk `Dodaj`.


![labelling](assets/notext/19.webp)


Wpisz etykietę i potwierdź, klikając niebieski przycisk "Dodaj". Etykietę będzie można znaleźć zarówno w szczegółach transakcji, jak i na pulpicie nawigacyjnym Wallet.


![labelling](assets/notext/20.webp)


## Samouczek: Etykietowanie na Sparrow Wallet


Oprogramowanie Sparrow Wallet umożliwia przypisywanie etykiet na wiele sposobów. Najprostszą metodą jest dodanie etykiety z góry, podczas przekazywania odbiorczego Address do nadawcy. Aby to zrobić, w menu `Receive` kliknij na pole `Label` i wprowadź wybraną etykietę. Zostanie ona zachowana i będzie dostępna w całym oprogramowaniu, gdy tylko bitcoiny zostaną odebrane na Address.


![labelling](assets/notext/21.webp)


Jeśli zapomniałeś oznaczyć swój Address przy odbiorze, nadal możesz dodać go później za pomocą menu `Transactions`. Wystarczy kliknąć na transakcję w kolumnie `Label`, a następnie wprowadzić żądaną etykietę.


![labelling](assets/notext/22.webp)


Masz również możliwość dodawania lub modyfikowania etykiet z menu `Addresses`.


![labelling](assets/notext/23.webp)


Etykiety można przeglądać w menu `UTXOs`. Sparrow Wallet automatycznie dodaje w nawiasach za etykietą charakter wyjścia, co pomaga odróżnić UTXO wynikające ze zmiany od tych otrzymanych bezpośrednio.


![labelling](assets/notext/24.webp)