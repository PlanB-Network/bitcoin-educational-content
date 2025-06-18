---
name: Ledger Flex
description: Konfiguracja i korzystanie z urządzenia Ledger Flex
---
![cover](assets/cover.webp)


Hardware Wallet to urządzenie elektroniczne przeznaczone do zarządzania i zabezpieczania kluczy prywatnych Bitcoin Wallet. W przeciwieństwie do portfeli programowych (lub portfeli Hot) instalowanych na maszynach ogólnego przeznaczenia często podłączonych do Internetu, portfele sprzętowe pozwalają na fizyczną izolację kluczy prywatnych, zmniejszając ryzyko włamania i kradzieży.


Głównym celem Hardware Wallet jest zminimalizowanie funkcjonalności urządzenia w celu zmniejszenia jego powierzchni ataku. Mniejsza powierzchnia ataku oznacza również mniej potencjalnych wektorów ataku, tj. mniej słabych punktów w systemie, które atakujący mogliby wykorzystać, aby uzyskać dostęp do bitcoinów.


Zaleca się korzystanie z Hardware Wallet w celu zabezpieczenia bitcoinów, zwłaszcza w przypadku posiadania znacznych kwot, zarówno pod względem wartości bezwzględnej, jak i proporcji całkowitych aktywów.


Portfele sprzętowe są używane w połączeniu z oprogramowaniem zarządzającym Wallet na komputerze lub smartfonie. Oprogramowanie to zarządza tworzeniem transakcji, ale podpis kryptograficzny niezbędny do walidacji tych transakcji jest wykonywany tylko w Hardware Wallet. Oznacza to, że klucze prywatne nigdy nie są narażone na potencjalnie wrażliwe środowisko.


Portfele sprzętowe zapewniają użytkownikowi podwójną ochronę: z jednej strony zabezpieczają bitcoiny przed zdalnymi atakami, utrzymując klucze prywatne w trybie offline, a z drugiej strony generalnie oferują lepszą odporność fizyczną na próby wyodrębnienia kluczy. I to właśnie na podstawie tych 2 kryteriów bezpieczeństwa można ocenić i uszeregować różne modele dostępne na rynku.


W tym samouczku proponuję odkryć jedno z tych rozwiązań: **Ledger Flex**.


![LEDGER FLEX](assets/notext/01.webp)


## Wprowadzenie do Ledger Flex


Ledger Flex to Hardware Wallet produkowany przez francuską firmę Ledger, sprzedawany w cenie 249 €.


![LEDGER FLEX](assets/notext/02.webp)


Posiada duży ekran dotykowy E Ink, czarno-biały wyświetlacz. Jest to ta sama technologia, którą można znaleźć w czytnikach elektronicznych. Ekran E Ink pozwala na wyraźne i czytelne wyświetlanie, nawet w jasnym świetle słonecznym, i zużywa bardzo mało energii lub nie zużywa jej wcale, gdy ekran jest statyczny. Działa on w oparciu o mikrokapsułki zawierające czarne i białe cząsteczki pigmentu. Po przyłożeniu ładunku elektrycznego czarne lub białe cząsteczki przemieszczają się na powierzchnię ekranu, umożliwiając w ten sposób tworzenie tekstu lub obrazów.

Ledger Flex jest wyposażony w chip "secure element" z certyfikatem CC EAL6+, oferujący zaawansowaną ochronę przed fizycznymi atakami na sprzęt. Ekran jest bezpośrednio kontrolowany przez ten układ. Częstym punktem krytyki jest fakt, że kod tego chipu nie jest open-source, co wymaga pewnego poziomu zaufania do integralności tego komponentu. Element ten jest jednak kontrolowany przez niezależnych ekspertów.


Pod względem użytkowania Ledger Flex oferuje kilka opcji łączności: Bluetooth, USB-C i NFC. Duży ekran pozwala na łatwą weryfikację szczegółów transakcji. Ledger wyróżnia się również na tle konkurencji szybkim przyjęciem nowych funkcji Bitcoin, takich jak na przykład Miniscript.


Po przetestowaniu jestem pod wrażeniem jakości produktu. Doświadczenie użytkownika jest doskonałe, a urządzenie jest intuicyjne. To doskonały Hardware Wallet. Ma jednak moim zdaniem 2 poważne wady: brak możliwości weryfikacji kodu chipa i oczywiście cenę, która jest znacznie wyższa niż u konkurencji. Dla porównania, najbardziej zaawansowany model od Foundation sprzedawany jest za 199$, Coinkite za 219,99$, a najnowszy Trezor, również wyposażony w duży ekran dotykowy, oferowany jest za 169€.


## Jak kupić Ledger Flex?


Ledger Flex jest dostępny w sprzedaży [na oficjalnej stronie internetowej](https://shop.Ledger.com/pages/Ledger-flex). Aby kupić go w sklepie fizycznym, można również znaleźć [listę certyfikowanych sprzedawców](https://www.Ledger.com/reseller) na stronie internetowej Ledger.


## Wymagania wstępne


Po otrzymaniu Ledger Flex, pierwszym krokiem jest sprawdzenie opakowania, aby upewnić się, że nie było ono otwierane.


![LEDGER FLEX](assets/notext/03.webp)


Opakowanie Ledger powinno zawierać 2 paski plombujące. Jeśli brakuje tych pasków lub są one uszkodzone, może to oznaczać, że Hardware Wallet został naruszony i może nie być autentyczny.


![LEDGER FLEX](assets/notext/04.webp)


Po otwarciu w pudełku powinny znajdować się następujące elementy:


- Ledger Flex;
- Kabel USB-C;
- Podręcznik użytkownika;
- Karty do zapisania frazy Mnemonic.


![LEDGER FLEX](assets/notext/05.webp)


Do tego samouczka potrzebne będą 2 elementy oprogramowania: Ledger Live do inicjalizacji Ledger Flex oraz Sparrow Wallet do zarządzania Bitcoin Wallet. Pobierz [Ledger Live](https://www.Ledger.com/Ledger-live) i [Sparrow Wallet](https://sparrowwallet.com/download/) z ich oficjalnych stron internetowych.


![LEDGER FLEX](assets/notext/06.webp)

Wkrótce udostępnimy samouczek dotyczący weryfikacji autentyczności i integralności pobieranego oprogramowania. Zdecydowanie zalecam zrobienie tego tutaj dla Ledger Live i Sparrow.

## Jak zainicjować Ledger Flex za pomocą Ledger Live?


Włącz urządzenie Ledger Flex, naciskając przez kilka sekund prawy przycisk boczny.


![LEDGER FLEX](assets/notext/07.webp)


Przewiń różne strony wprowadzające.


![LEDGER FLEX](assets/notext/08.webp)


Wybierz opcję "*Setup without Ledger Live*", a następnie kliknij przycisk "*Skip Ledger Live*".


![LEDGER FLEX](assets/notext/09.webp)


Następnie zostaniesz poproszony o wybranie nazwy dla Ledger. Kliknij "*Set name*", a następnie wprowadź wybraną nazwę.


![LEDGER FLEX](assets/notext/10.webp)


Wybierz kod PIN dla swojego urządzenia, który będzie używany do odblokowania Ledger. Jest to zatem zabezpieczenie przed nieautoryzowanym dostępem fizycznym. Ten kod PIN nie bierze udziału w tworzeniu kluczy kryptograficznych Wallet. Tak więc, nawet bez dostępu do tego kodu PIN, posiadanie 24-wyrazowej frazy Mnemonic pozwoli ci odzyskać dostęp do twoich bitcoinów.


Zaleca się wybranie 8-cyfrowego kodu PIN, możliwie jak najbardziej losowego. Należy również zapisać ten kod w innym miejscu niż to, w którym przechowywana jest karta Ledger Flex (na przykład w menedżerze haseł).


![LEDGER FLEX](assets/notext/11.webp)


Wprowadź kod PIN po raz drugi, aby go potwierdzić.


![LEDGER FLEX](assets/notext/12.webp)


Następnie zostaniesz poproszony o wybór między odzyskaniem istniejącego Wallet lub utworzeniem nowego. W tym samouczku zajmiemy się tworzeniem nowego Wallet od podstaw, więc wybierz opcję "*Setup as a new Ledger*", aby generate utworzył nową frazę Mnemonic.


![LEDGER FLEX](assets/notext/13.webp)


Flex dostarczy instrukcje dotyczące zarządzania zwrotem odzyskiwania.


**Ta fraza Mnemonic daje pełny i nieograniczony dostęp do wszystkich bitcoinów**. Każdy, kto posiada tę frazę, może ukraść Twoje środki, nawet bez fizycznego dostępu do Ledger. 24-słowna fraza umożliwia przywrócenie dostępu do bitcoinów w przypadku utraty, kradzieży lub uszkodzenia urządzenia Ledger Flex. Dlatego bardzo ważne jest, aby starannie ją zapisać i przechowywać w bezpiecznym miejscu.


Możesz zapisać go na kartonowym papierze dołączonym do Ledger lub, dla większego bezpieczeństwa, zalecam wygrawerowanie go na nośniku ze stali nierdzewnej, aby zabezpieczyć się przed ryzykiem pożaru, powodzi lub zawalenia.


Możesz przeglądać te instrukcje i pomijać strony, dotykając ekranu.


![LEDGER FLEX](assets/notext/14.webp)

Ledger utworzy frazę Mnemonic przy użyciu generatora liczb losowych. Upewnij się, że nie jesteś obserwowany podczas tej operacji. Zapisz słowa dostarczone przez Ledger na wybranym nośniku fizycznym. W zależności od strategii bezpieczeństwa można rozważyć utworzenie kilku pełnych fizycznych kopii frazy (ale co najważniejsze, nie należy ich dzielić). Ważne jest, aby słowa były ponumerowane i ułożone w kolejności.

***Oczywiście nigdy nie należy udostępniać tych słów w Internecie, w przeciwieństwie do tego, co robię w tym samouczku. Ten przykład Wallet będzie używany tylko na Testnet i zostanie usunięty po zakończeniu samouczka.***


![LEDGER FLEX](assets/notext/15.webp)


Aby przejść do następnej grupy słów, kliknij przycisk "*Next*". Po zanotowaniu wszystkich słów, kliknij przycisk "*Done*", aby przejść do następnego kroku.


![LEDGER FLEX](assets/notext/16.webp)


Kliknij przycisk "*Potwierdź rozpoczęcie*", a następnie wybierz słowa z frazy Mnemonic w ich kolejności, aby potwierdzić, że zostały poprawnie zapisane. Kontynuuj tę procedurę do 24. słowa.


![LEDGER FLEX](assets/notext/17.webp)


Jeśli potwierdzana fraza odpowiada dokładnie tej, którą Flex dostarczył w poprzednim kroku, można kontynuować. Jeśli nie, oznacza to, że fizyczna kopia zapasowa frazy Mnemonic jest nieprawidłowa i należy ponownie uruchomić proces.


![LEDGER FLEX](assets/notext/18.webp)


I gotowe, seed został poprawnie utworzony na Ledger Flex. Przed przystąpieniem do tworzenia nowego Bitcoin Wallet z tego seed, przeanalizujmy razem ustawienia urządzenia.


## Jak zmodyfikować ustawienia Ledger?


Aby zablokować lub odblokować Ledger, naciśnij przycisk boczny. Następnie zostaniesz poproszony o wprowadzenie kodu PIN ustawionego w poprzednim kroku.


![LEDGER FLEX](assets/notext/19.webp)


Aby uzyskać dostęp do ustawień, kliknij symbol koła zębatego w lewym dolnym rogu urządzenia.


![LEDGER FLEX](assets/notext/20.webp)


Menu "*Name*" umożliwia zmianę nazwy Ledger.


![LEDGER FLEX](assets/notext/21.webp)


W sekcji "*About this Ledger*" znajdują się informacje na temat urządzenia Flex.


![LEDGER FLEX](assets/notext/22.webp)


W menu "*Ekran blokady*" istnieje możliwość zmiany obrazu wyświetlanego na ekranie blokady poprzez wybranie opcji "*Dostosuj obraz ekranu blokady*". Dzięki zastosowanej w urządzeniu technologii ekranu E Ink możliwe jest ciągłe włączanie ekranu bez zużywania baterii. Ekrany E Ink nie zużywają energii do utrzymania statycznego obrazu. Zużywają jednak energię podczas zmian wyświetlania.

Podmenu "*Auto-lock*" pozwala skonfigurować i aktywować automatyczne blokowanie Ledger po określonym czasie bezczynności.

![LEDGER FLEX](assets/notext/23.webp)


Menu "*Sounds*" (Dźwięki) umożliwia włączanie i wyłączanie dźwięków urządzenia Flex. W menu "Język" można zmienić język wyświetlacza.


![LEDGER FLEX](assets/notext/24.webp)


Klikając strzałkę w prawo, można uzyskać dostęp do innych ustawień. "*Zmień PIN*" umożliwia zmianę kodu PIN.


![LEDGER FLEX](assets/notext/25.webp)


Menu "*Bluetooth*" i "*NFC*" umożliwiają zarządzanie tą komunikacją.


![LEDGER FLEX](assets/notext/26.webp)


W "*Battery*" można ustawić automatyczne wyłączanie Ledger.


![LEDGER FLEX](assets/notext/27.webp)


Sekcja "*Advanced*" daje dostęp do bardziej zaawansowanych ustawień bezpieczeństwa. Zaleca się aktywowanie opcji "*PIN shuffle*" w celu zwiększenia bezpieczeństwa. W tym menu można również skonfigurować BIP39 passphrase.


![LEDGER FLEX](assets/notext/28.webp)


passphrase to opcjonalne hasło, które w połączeniu z frazą odzyskiwania zapewnia dodatkowe Layer bezpieczeństwo dla Wallet.


Obecnie klucz Wallet jest generowany na podstawie frazy Mnemonic składającej się z 24 słów. Ta fraza odzyskiwania jest bardzo ważna, ponieważ umożliwia przywrócenie wszystkich kluczy Wallet w przypadku ich utraty. Stanowi ona jednak pojedynczy punkt awarii (SPOF). Jeśli zostanie on naruszony, bitcoiny są w niebezpieczeństwie. W tym miejscu pojawia się passphrase. Jest to opcjonalne hasło, które można dowolnie wybrać, które dodaje się do frazy Mnemonic w celu wzmocnienia bezpieczeństwa Wallet.


Kodu passphrase nie należy mylić z kodem PIN. Odgrywa on rolę w tworzeniu kluczy kryptograficznych. Działa w parze z frazą Mnemonic, modyfikując seed, z którego generowane są klucze. Tak więc, nawet jeśli ktoś uzyska 24-wyrazową frazę, bez passphrase nie będzie mógł uzyskać dostępu do Twoich środków. Użycie passphrase zasadniczo tworzy nowy Wallet z odrębnymi kluczami. Modyfikacja (nawet niewielka) passphrase spowoduje generate innego Wallet.


passphrase to bardzo potężne narzędzie zwiększające bezpieczeństwo bitcoinów. Jednak bardzo ważne jest, aby zrozumieć, jak działa przed jego wdrożeniem, aby uniknąć utraty dostępu do Wallet. Wyjaśnię, jak korzystać z passphrase w innym dedykowanym samouczku.


![LEDGER FLEX](assets/notext/29.webp)


passphrase to bardzo potężne narzędzie wzmacniające bezpieczeństwo bitcoinów. Kluczowe jest jednak zrozumienie jego działania przed wdrożeniem, aby uniknąć utraty dostępu do Wallet. Właśnie dlatego wyjaśniam wszystko w dedykowanym samouczku:


https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

Ostatnia strona ustawień umożliwia zresetowanie Ledger. Reset ten należy wykonać tylko wtedy, gdy masz pewność, że nie zawiera on żadnych kluczy zabezpieczających bitcoiny, ponieważ możesz trwale utracić dostęp do swoich środków.

![LEDGER FLEX](assets/notext/30.webp)


## Jak zainstalować aplikację Bitcoin?


Rozpocznij od uruchomienia oprogramowania Ledger Live na komputerze, a następnie podłącz i odblokuj urządzenie Ledger Flex.


![LEDGER FLEX](assets/notext/31.webp)


W Ledger Live przejdź do menu "*Mój Ledger*". Zostaniesz poproszony o autoryzację dostępu do swojego urządzenia Flex.


![LEDGER FLEX](assets/notext/32.webp)


Zatwierdź dostęp do Ledger, klikając przycisk "*Allow*".


![LEDGER FLEX](assets/notext/33.webp)


Po pierwsze, jeśli oprogramowanie sprzętowe Ledger Flex nie jest aktualne, Ledger Live automatycznie zaproponuje jego aktualizację. Jeśli ma to zastosowanie, kliknij "*Update firmware*", a następnie "*Install update*", aby rozpocząć instalację.


![LEDGER FLEX](assets/notext/34.webp)


Na urządzeniu Ledger kliknij przycisk "*Install*", a następnie poczekaj na zakończenie instalacji.


![LEDGER FLEX](assets/notext/35.webp)


Oprogramowanie sprzętowe urządzenia Ledger Flex jest teraz aktualne.


![LEDGER FLEX](assets/notext/36.webp)


Jeśli chcesz, możesz zmienić tapetę ekranu blokady swojego Ledger Flex. Aby to zrobić, kliknij na "*Add >*".


![LEDGER FLEX](assets/notext/37.webp)


Kliknij przycisk "*Prześlij z komputera*" i wybierz tapetę ze swoich zdjęć.


![LEDGER FLEX](assets/notext/38.webp)


Obraz można przyciąć.


![LEDGER FLEX](assets/notext/39.webp)


Wybierz kontrast spośród różnych opcji, a następnie kliknij "*Potwierdź kontrast*".


![LEDGER FLEX](assets/notext/40.webp)


W aplikacji Flex kliknij przycisk "*Załaduj zdjęcie*".


![LEDGER FLEX](assets/notext/41.webp)


Jeśli obraz ci odpowiada, kliknij "*Keep*", aby ustawić go jako tapetę ekranu blokady.


![LEDGER FLEX](assets/notext/42.webp)


Na koniec dodamy aplikację Bitcoin. Aby to zrobić, w Ledger Live kliknij przycisk "*Install*" obok "*Bitcoin (BTC)*".


![LEDGER FLEX](assets/notext/43.webp)


Aplikacja zostanie zainstalowana na urządzeniu Flex.


![LEDGER FLEX](assets/notext/44.webp)


Od tej chwili oprogramowanie Ledger Live nie będzie już potrzebne do regularnego zarządzania Wallet. Można do niego wracać od czasu do czasu, aby zaktualizować oprogramowanie sprzętowe, gdy dostępne są nowe wersje. Do wszystkiego innego będziemy używać Sparrow Wallet, który jest znacznie bardziej wszechstronnym narzędziem do efektywnego zarządzania Bitcoin Wallet.


## Jak skonfigurować nowy Bitcoin Wallet za pomocą Sparrow?

Otwórz Sparrow Wallet i pomiń strony wprowadzające, aby uzyskać dostęp do ekranu głównego. Sprawdź, czy jesteś prawidłowo połączony z węzłem, obserwując przełącznik znajdujący się w prawym dolnym rogu ekranu.

![LEDGER FLEX](assets/notext/45.webp)


Zdecydowanie zalecam korzystanie z własnego węzła Bitcoin. W tym samouczku korzystam z węzła publicznego (żółty), ponieważ jestem na Testnet, ale do normalnego użytku lepiej jest wybrać lokalny Bitcoin Core (Green) lub serwer Electrum podłączony do zdalnego węzła (niebieski).


Kliknij menu "*Plik*", a następnie "*Nowy Wallet*".


![LEDGER FLEX](assets/notext/46.webp)


Wybierz nazwę dla tego Wallet, a następnie kliknij "*Create Wallet*".


![LEDGER FLEX](assets/notext/47.webp)


W menu rozwijanym "*Typ skryptu*" wybierz typ skryptu, który będzie używany do zabezpieczenia twoich bitcoinów. Zalecam wybranie "*Taproot*" lub, jeśli nie jest dostępny, "*Native SegWit*".


![LEDGER FLEX](assets/notext/48.webp)


Kliknij przycisk "*Podłączono Hardware Wallet*".


![LEDGER FLEX](assets/notext/49.webp)


Podłącz urządzenie Ledger Flex do komputera, odblokuj je kodem PIN, a następnie otwórz aplikację "*Bitcoin*". W tym samouczku używam aplikacji "*Bitcoin Testnet*", ale procedura pozostaje taka sama dla Mainnet.


![LEDGER FLEX](assets/notext/50.webp)


W aplikacji Sparrow kliknij przycisk "*Scan*".


![LEDGER FLEX](assets/notext/51.webp)


Następnie kliknij "*Import Keystore*".


![LEDGER FLEX](assets/notext/52.webp)


Możesz teraz zobaczyć szczegóły swojego Wallet, w tym rozszerzony klucz publiczny pierwszego konta. Kliknij przycisk "*Zastosuj*", aby sfinalizować tworzenie Wallet.


![LEDGER FLEX](assets/notext/53.webp)


Wybierz silne hasło, aby zabezpieczyć dostęp do Sparrow Wallet. To hasło zapewni bezpieczeństwo dostępu do danych Wallet w Sparrow, co pomaga chronić klucze publiczne, adresy, etykiety i historię transakcji przed nieautoryzowanym dostępem.


Radzę zapisać to hasło w menedżerze haseł, aby go nie zapomnieć.


![LEDGER FLEX](assets/notext/54.webp)


I gotowe, twój Wallet został stworzony!


![LEDGER FLEX](assets/notext/55.webp)

Przed otrzymaniem pierwszych bitcoinów w Wallet zdecydowanie zalecam wykonanie testu odzyskiwania na sucho. Zanotuj informacje referencyjne, takie jak xpub, a następnie zresetuj Ledger Flex, gdy Wallet jest nadal pusty. Następnie spróbuj przywrócić Wallet na Ledger przy użyciu papierowych kopii zapasowych. Sprawdź, czy xpub wygenerowany po przywróceniu jest zgodny z początkowo zanotowanym. W takim przypadku można mieć pewność, że papierowe kopie zapasowe są niezawodne.


## Jak odbierać bitcoiny za pomocą Ledger Flex?


Kliknij zakładkę "*Odbierz*".


![LEDGER FLEX](assets/notext/56.webp)


Podłącz urządzenie Ledger Flex do komputera, odblokuj je kodem PIN, a następnie otwórz aplikację "*Bitcoin*".


![LEDGER FLEX](assets/notext/57.webp)


Przed użyciem Address dostarczonego przez Sparrow Wallet należy zweryfikować go na ekranie Ledger Flex. Ta praktyka pozwala potwierdzić, że Address wyświetlany na Sparrow nie jest fałszywy i że Ledger rzeczywiście posiada klucz prywatny niezbędny do późniejszego wydania bitcoinów zabezpieczonych tym Address.


Aby przeprowadzić tę weryfikację, kliknij przycisk "*Wyświetl Address*".


![LEDGER FLEX](assets/notext/58.webp)


Upewnij się, że numer Address wyświetlany na urządzeniu Ledger Flex jest zgodny z numerem wskazanym na urządzeniu Sparrow Wallet. Zaleca się również przeprowadzenie tej weryfikacji tuż przed przekazaniem Address nadawcy, aby upewnić się co do jego ważności.


![LEDGER FLEX](assets/notext/59.webp)


Możesz dodać "*Label*", aby opisać źródło bitcoinów, które będą zabezpieczone za pomocą tego Address. Jest to dobra praktyka, która pomaga lepiej zarządzać UTXO.


![LEDGER FLEX](assets/notext/60.webp)


Więcej informacji na temat etykietowania można znaleźć w tym poradniku:


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Następnie można użyć Address do otrzymywania bitcoinów.


![LEDGER FLEX](assets/notext/61.webp)


## Jak wysyłać bitcoiny za pomocą Ledger Flex?


Teraz, gdy otrzymałeś swoje pierwsze Sats w Wallet zabezpieczonym Flexem, możesz je również wydać! Podłącz Ledger do komputera, odblokuj go, uruchom Sparrow Wallet, a następnie przejdź do zakładki "*Wyślij*", aby utworzyć nową transakcję.


![LEDGER FLEX](assets/notext/62.webp)


Jeśli chcesz wykonać "*coin control*", czyli konkretnie wybrać, które UTXO mają zostać zużyte w transakcji, przejdź do zakładki "*UTXOs*". Wybierz UTXO, które chcesz wydać, a następnie kliknij "*Wyślij wybrane*". Nastąpi przekierowanie do tego samego ekranu w zakładce "*Wyślij*", ale z UTXO już wybranymi do transakcji.

![LEDGER FLEX](assets/notext/63.webp)

Wprowadź adres docelowy Address. Można również wprowadzić wiele adresów, klikając przycisk "*+ Add*".


![LEDGER FLEX](assets/notext/64.webp)


Zanotuj "*Label*", aby zapamiętać cel tego wydatku.


![LEDGER FLEX](assets/notext/65.webp)


Wybierz kwotę wysyłaną do tego Address.


![LEDGER FLEX](assets/notext/66.webp)


Dostosuj stawkę opłaty za transakcję do aktualnego rynku.


![LEDGER FLEX](assets/notext/67.webp)


Upewnij się, że wszystkie ustawienia transakcji są prawidłowe, a następnie kliknij "*Twórz transakcję*".


![LEDGER FLEX](assets/notext/68.webp)


Jeśli wszystko jest w porządku, kliknij "*Finalizuj transakcję do podpisu*".


![LEDGER FLEX](assets/notext/69.webp)


Kliknij "*Podpisz*".


![LEDGER FLEX](assets/notext/70.webp)


Kliknij "*Sign*" obok swojego Ledger Flex.


![LEDGER FLEX](assets/notext/71.webp)


Zweryfikuj ustawienia transakcji na ekranie Flex, w tym odbiorcę otrzymującego Address, wysłaną kwotę i kwotę opłaty.


![LEDGER FLEX](assets/notext/72.webp)


Aby podpisać, przytrzymaj palec na przycisku "*Hold to sign*".


![LEDGER FLEX](assets/notext/73.webp)


Transakcja została podpisana. Kliknij "*Rozgłoś transakcję*", aby rozgłosić ją w sieci Bitcoin.


![LEDGER FLEX](assets/notext/74.webp)


Można go znaleźć w zakładce "*Transakcje*" w Sparrow Wallet.


![LEDGER FLEX](assets/notext/75.webp)


Gratulacje, jesteś teraz na bieżąco z podstawowym użyciem Ledger Flex z Sparrow Wallet! W przyszłym samouczku zobaczymy, jak używać Ledger Flex z Liana, aby wykorzystać Miniscript.


Jeśli ten poradnik okazał się pomocny, będę wdzięczny za kciuk w górę poniżej. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dziękuję bardzo!