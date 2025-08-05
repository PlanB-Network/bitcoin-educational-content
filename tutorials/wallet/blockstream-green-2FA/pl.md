---
name: Blockstream Green - 2FA
description: Konfiguracja Multisig 2/2 na Green Wallet
---
![cover](assets/cover.webp)

___

***Uwaga:** Od maja 2025 roku nie będzie już możliwe aktywowanie nowych kont chronionych uwierzytelnianiem dwuskładnikowym (2FA). Funkcja ta jest dostępna wyłącznie dla użytkowników, którzy wcześniej aktywowali ten typ konta.*

___

Software Wallet to aplikacja instalowana na komputerze, smartfonie lub innym urządzeniu podłączonym do Internetu, umożliwiająca zarządzanie i zabezpieczanie kluczy Bitcoin Wallet. W przeciwieństwie do portfeli sprzętowych, które izolują klucze prywatne, portfele "Hot" działają zatem w środowisku potencjalnie narażonym na ataki cybernetyczne, zwiększając ryzyko piractwa i kradzieży.

Portfele programowe powinny być używane do zarządzania rozsądnymi ilościami bitcoinów, zwłaszcza do codziennych transakcji. Mogą być również interesującą opcją dla osób z ograniczonymi aktywami Bitcoin, dla których inwestycja w Hardware Wallet może wydawać się nieproporcjonalna. Jednak ich stała ekspozycja na Internet sprawia, że są one mniej bezpieczne do przechowywania długoterminowych oszczędności lub dużych funduszy. W tym drugim przypadku najlepiej zdecydować się na bezpieczniejsze rozwiązania, takie jak portfele sprzętowe.

W tym samouczku pokażę, jak poprawić bezpieczeństwo Hot Wallet za pomocą opcji "*2FA*" na Blockstream Green.


![GREEN 2FA MULTISIG](assets/fr/01.webp)


## Przedstawiamy Blockstream Green


Blockstream Green to Software Wallet dostępny na urządzeniach mobilnych i komputerach stacjonarnych. Wcześniej znany jako *Green Address*, ten Wallet stał się projektem Blockstream po jego przejęciu w 2016 roku.


Green jest wyjątkowo łatwą w użyciu aplikacją, co czyni ją interesującą dla początkujących. Oferuje wszystkie niezbędne funkcje dobrego Bitcoin Wallet, w tym RBF (*Replace-by-fee*), opcję połączenia Tor, możliwość podłączenia własnego węzła, SPV (*Simple Payment Verification*), tagowanie monet i kontrolę.


Blockstream Green obsługuje również Liquid Network, Bitcoin Sidechain opracowany przez Blockstream na szybko, Confidential Transactions poza głównym Blockchain. W tym samouczku skupiamy się wyłącznie na Bitcoin, ale przygotowałem również inny samouczek, aby dowiedzieć się, jak korzystać z Liquid na Green:


https://planb.network/tutorials/wallet/mobile/blockstream-green-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

## opcja 2/2 Multisig (2FA)


Na Green można stworzyć klasyczny "*singlesig*" Hot Wallet. Dostępna jest również opcja "*2FA Multisig*", która zwiększa bezpieczeństwo Hot Wallet bez nadmiernego komplikowania codziennego zarządzania.


Skonfigurujesz więc Multisig Wallet 2/2, co oznacza, że każda transakcja będzie wymagała podpisania dwóch kluczy. Pierwszy klucz, pochodzący z 12- lub 24-wyrazowej frazy Mnemonic, jest zabezpieczony lokalnie kodem PIN w telefonie. Użytkownik ma pełną kontrolę nad tym kluczem. Drugi klucz jest przechowywany przez serwery Blockstream i jego użycie do podpisania wymaga uwierzytelnienia, które można uzyskać za pomocą kodu otrzymanego pocztą elektroniczną, SMS-em, rozmową telefoniczną lub, jak zobaczymy w tym samouczku, za pośrednictwem aplikacji uwierzytelniającej (Authy, Google Authenticator itp.).


Aby zapewnić autonomię w przypadku awarii Blockstream (na przykład w przypadku bankructwa firmy lub zniszczenia serwerów przechowujących drugi klucz), do Multisig zastosowano mechanizm blokady czasowej. Mechanizm ten przekształca Multisig 2/2 w Multisig 1/2 po około roku (lub dokładnie 51 840 blokach, ale wartość ta jest modyfikowalna), po którym twój Wallet będzie potrzebował tylko twojego lokalnego klucza do wydawania bitcoinów. Tak więc, jeśli utracisz dostęp do serwerów Blockstream lub uwierzytelniania 2FA, musisz poczekać maksymalnie rok, aby móc swobodnie korzystać z bitcoinów w swojej aplikacji, bez zależności od Blockstream.


![GREEN 2FA MULTISIG](assets/fr/02.webp)


Metoda ta znacznie zwiększa bezpieczeństwo Hot Wallet, jednocześnie pozostawiając kontrolę nad bitcoinami i ułatwiając ich codzienne użytkowanie. Wymaga ona jednak regularnego odświeżania blokady czasowej w celu utrzymania bezpieczeństwa 2FA. Odliczanie 360 dni, podczas których środki są chronione przez 2FA, rozpoczyna się w momencie otrzymania bitcoinów. Jeśli w ciągu 360 dni od otrzymania środków użytkownik nie przeprowadzi transakcji przy użyciu tych środków, bitcoiny będą chronione wyłącznie przez klucz lokalny, bez 2FA.


To ograniczenie sprawia, że opcja 2FA jest bardziej odpowiednia dla Wallet wydatków, gdzie regularne transakcje automatycznie odnawiają blokady czasowe. W przypadku długoterminowych oszczędności Wallet może to być problematyczne, ponieważ będziesz musiał pomyśleć o dokonaniu transakcji zamiany dla siebie każdego roku przed wygaśnięciem blokady czasowej.


Kolejną wadą tej metody zabezpieczeń jest konieczność korzystania z szablonów skryptów mniejszościowych. Oznacza to, że z punktu widzenia poufności sprawy stają się bardziej skomplikowane: bardzo niewiele osób korzysta z tego samego typu skryptu co ty, co ułatwia zewnętrznemu obserwatorowi zidentyfikowanie twojego odcisku palca Wallet. Co więcej, skrypty te wiążą się z wyższymi kosztami transakcji ze względu na ich większy rozmiar.


Jeśli wolisz nie korzystać z opcji 2FA i po prostu chcesz skonfigurować "*singlesig*" Wallet na Green, zapraszam do zapoznania się z tym innym samouczkiem :


https://planb.network/tutorials/wallet/mobile/blockstream-green-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

## Instalacja i konfiguracja oprogramowania Blockstream Green


Pierwszym krokiem jest oczywiście pobranie aplikacji Green. Przejdź do sklepu z aplikacjami:



- [Dla systemu Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [For Apple](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590).

![GREEN 2FA MULTISIG](assets/fr/03.webp)


Użytkownicy Androida mogą również zainstalować aplikację za pomocą pliku `.apk` [dostępnego na GitHubie Blockstream] (https://github.com/Blockstream/green_android/releases).


![GREEN 2FA MULTISIG](assets/fr/04.webp)


Uruchom aplikację, a następnie zaznacz pole "Akceptuję warunki...*".


![GREEN 2FA MULTISIG](assets/fr/05.webp)


Po otwarciu Green po raz pierwszy, ekran główny pojawi się bez skonfigurowanego Wallet. Później, jeśli utworzysz lub zaimportujesz portfele, pojawią się one w tym Interface. Zanim przejdziesz do tworzenia Wallet, radzę dostosować ustawienia aplikacji do swoich potrzeb. Kliknij "Ustawienia aplikacji".


![GREEN 2FA MULTISIG](assets/fr/06.webp)


Opcja "*Enhanced Privacy*", dostępna tylko w systemie Android, zwiększa prywatność poprzez wyłączenie zrzutów ekranu i ukrywanie podglądu aplikacji. Automatycznie blokuje również dostęp do aplikacji, gdy tylko telefon zostanie zablokowany, co utrudnia ujawnienie danych.


![GREEN 2FA MULTISIG](assets/fr/07.webp)


Dla tych, którzy chcą zwiększyć swoją prywatność, aplikacja oferuje opcję rootowania ruchu za pośrednictwem sieci Tor, która szyfruje wszystkie połączenia i utrudnia śledzenie aktywności użytkownika. Chociaż opcja ta może nieco spowolnić działanie aplikacji, jest ona wysoce zalecana w celu ochrony prywatności, zwłaszcza jeśli nie korzystasz z własnego kompletnego węzła.


![GREEN 2FA MULTISIG](assets/fr/08.webp)


Dla użytkowników posiadających własny kompletny węzeł Green Wallet oferuje możliwość połączenia się z nim za pośrednictwem serwera Electrum, gwarantując całkowitą kontrolę nad informacjami sieciowymi Bitcoin i dystrybucją transakcji.


![GREEN 2FA MULTISIG](assets/fr/09.webp)


Inną alternatywną funkcją jest opcja "*SPV Verification*", która umożliwia bezpośrednią weryfikację niektórych danych Blockchain, a tym samym zmniejsza potrzebę ufania domyślnemu węzłowi Blockstream, chociaż ta metoda nie zapewnia wszystkich gwarancji Full node.


![GREEN 2FA MULTISIG](assets/fr/10.webp)


Po dostosowaniu tych ustawień do swoich potrzeb, kliknij przycisk "*Zapisz*" i uruchom ponownie aplikację.


![GREEN 2FA MULTISIG](assets/fr/11.webp)


## Utwórz Bitcoin Wallet na Blockstream Green


Teraz możesz utworzyć Bitcoin Wallet. Kliknij przycisk "*Get Started*".


![GREEN 2FA MULTISIG](assets/fr/12.webp)


Można wybrać między utworzeniem lokalnego Software Wallet lub zarządzaniem Cold Wallet za pośrednictwem Hardware Wallet. W tym samouczku skoncentrujemy się na tworzeniu Hot Wallet, więc musisz wybrać opcję "*On This Device*".


![GREEN 2FA MULTISIG](assets/fr/13.webp)


Następnie można przywrócić istniejący Bitcoin Wallet lub utworzyć nowy. Na potrzeby tego samouczka utworzymy nowy Wallet. Jeśli jednak musisz zregenerować istniejący Bitcoin Wallet z jego frazy Mnemonic, na przykład po utracie starego telefonu, musisz wybrać drugą opcję.


![GREEN 2FA MULTISIG](assets/fr/14.webp)


Następnie można wybrać 12- lub 24-wyrazową frazę Mnemonic. Ta fraza umożliwi odzyskanie dostępu do Wallet z dowolnego kompatybilnego oprogramowania w przypadku problemu z telefonem. Obecnie wybór 24-wyrazowej frazy nie zapewnia większego bezpieczeństwa niż fraza 12-wyrazowa. Dlatego zalecam wybranie 12-wyrazowej frazy Mnemonic.


Green przekaże ci wtedy twoją frazę Mnemonic. Przed kontynuowaniem upewnij się, że nie jesteś obserwowany. Kliknij "*Pokaż frazę odzyskiwania*", aby wyświetlić ją na ekranie.


![GREEN 2FA MULTISIG](assets/fr/15.webp)


**Mnemonic daje pełny, nieograniczony dostęp do wszystkich bitcoinów**. Każdy, kto jest w posiadaniu tej frazy, może ukraść twoje fundusze, nawet bez fizycznego dostępu do twojego telefonu (z zastrzeżeniem wygaśnięcia blokady czasowej lub 2FA w przypadku Wallet 2/2 na Green).


Umożliwia ona przywrócenie dostępu do kluczy lokalnych w przypadku utraty, kradzieży lub uszkodzenia telefonu. Dlatego bardzo ważne jest, aby starannie wykonać kopię zapasową **na nośniku fizycznym (nie cyfrowym)** i przechowywać ją w bezpiecznym miejscu. Można ją zapisać na kartce papieru, a dla zwiększenia bezpieczeństwa, jeśli jest to duży Wallet, zalecam wygrawerowanie jej na wsporniku ze stali nierdzewnej, aby chronić ją przed ryzykiem pożaru, powodzi lub zawalenia (w przypadku Hot Wallet zaprojektowanego do zabezpieczenia niewielkiej ilości bitcoinów, prawdopodobnie wystarczy zwykła kopia zapasowa na papierze).


*Oczywiście nigdy nie wolno udostępniać tych słów w Internecie, tak jak robię to w tym samouczku. Ten przykładowy Wallet będzie używany tylko na Testnet i zostanie usunięty po zakończeniu samouczka


![GREEN 2FA MULTISIG](assets/fr/16.webp)


Po prawidłowym nagraniu frazy Mnemonic na nośniku fizycznym, kliknij "*Kontynuuj*". Green Wallet poprosi o potwierdzenie niektórych słów w frazie Mnemonic, aby upewnić się, że zostały one poprawnie nagrane. Wypełnij puste miejsca brakującymi słowami.


![GREEN 2FA MULTISIG](assets/fr/17.webp)


Wybierz kod PIN urządzenia, który zostanie użyty do odblokowania Green Wallet. Jest to zabezpieczenie przed nieautoryzowanym dostępem fizycznym. Ten kod PIN nie bierze udziału w tworzeniu kluczy kryptograficznych Wallet. Tak więc, nawet bez dostępu do tego kodu PIN, posiadanie 12- lub 24-wyrazowej frazy Mnemonic umożliwi odzyskanie dostępu do kluczy lokalnych.


Zalecamy wybranie możliwie losowego 6-cyfrowego kodu PIN. Pamiętaj, aby zapisać ten kod, aby go nie zapomnieć, w przeciwnym razie będziesz zmuszony do odzyskania Wallet z Mnemonic. Następnie możesz dodać opcję blokowania biometrycznego, aby uniknąć konieczności wprowadzania kodu PIN za każdym razem, gdy go używasz. Ogólnie rzecz biorąc, dane biometryczne są znacznie mniej bezpieczne niż sam kod PIN. Dlatego domyślnie radzę nie ustawiać tej opcji odblokowywania.


![GREEN 2FA MULTISIG](assets/fr/18.webp)


Wprowadź kod PIN po raz drugi, aby go potwierdzić.


![GREEN 2FA MULTISIG](assets/fr/19.webp)


Poczekaj na utworzenie Wallet, a następnie kliknij przycisk "*Utwórz konto*".


![GREEN 2FA MULTISIG](assets/fr/20.webp)


Następnie możesz wybrać między standardowym Wallet z pojedynczym podpisem lub Wallet chronionym uwierzytelnianiem dwuskładnikowym (2FA). W tym samouczku wybierzemy drugą opcję.


![GREEN 2FA MULTISIG](assets/fr/21.webp)


Twój Bitcoin Multisig Wallet został utworzony przy użyciu aplikacji Green!


![GREEN 2FA MULTISIG](assets/fr/22.webp)


## Konfiguracja 2FA


Kliknij swoje konto.


![GREEN 2FA MULTISIG](assets/fr/23.webp)


Kliknij przycisk Green "*Zwiększ bezpieczeństwo swojego konta, dodając 2FA*".


![GREEN 2FA MULTISIG](assets/fr/24.webp)


Następnie będzie można wybrać metodę uwierzytelniania, aby uzyskać dostęp do drugiego klucza 2/2 Multisig. W tym samouczku będziemy używać aplikacji uwierzytelniającej. Jeśli nie jesteś zaznajomiony z tego typu aplikacjami, polecam zapoznać się z naszym samouczkiem na temat Authy :


https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Wybierz "*Authenticator Application*".


![GREEN 2FA MULTISIG](assets/fr/25.webp)


Green wyświetli kod QR i klucz odzyskiwania. Klucz ten umożliwia przywrócenie dostępu do 2FA w przypadku utraty aplikacji Authy. Zaleca się wykonanie bezpiecznej kopii zapasowej tego klucza, chociaż nadal można odzyskać dostęp do bitcoinów po wygaśnięciu blokady czasowej, jak wyjaśniono powyżej.


W aplikacji uwierzytelniającej dodaj nowy kod, a następnie zeskanuj kod QR dostarczony przez Green.


![GREEN 2FA MULTISIG](assets/fr/26.webp)


*Oczywiście nigdy nie wolno udostępniać tego klucza i kodu QR w Internecie, tak jak robię to w tym samouczku. Ten przykładowy Wallet będzie używany tylko na Testnet i zostanie usunięty po zakończeniu samouczka


Kliknij przycisk "*Kontynuuj*".


![GREEN 2FA MULTISIG](assets/fr/27.webp)


Wprowadź 6-cyfrowy kod dynamiczny obecny w aplikacji uwierzytelniającej.


![GREEN 2FA MULTISIG](assets/fr/28.webp)


uwierzytelnianie dwuskładnikowe jest teraz włączone.


![GREEN 2FA MULTISIG](assets/fr/29.webp)


Przeglądając to menu, można również ustawić czas trwania blokady czasowej. Odliczanie to rozpoczyna się natychmiast po otrzymaniu bitcoinów, a po wygaśnięciu blokady czasowej środki można wydać tylko za pomocą klucza lokalnego, bez konieczności stosowania 2FA. Domyślny czas trwania jest ustawiony na 12 miesięcy, ale w przypadku Wallet oszczędnościowego sensowne może być wybranie 15 miesięcy, aby zminimalizować częstotliwość odnawiania blokady czasowej. I odwrotnie, w przypadku Wallet na wydatki, 6-miesięczna blokada czasowa może być preferowana, ponieważ będzie ona często odnawiana wraz z codziennymi transakcjami, a krótsza blokada czasowa skraca czas oczekiwania w przypadku problemu z 2FA. Do Ciebie należy określenie czasu trwania blokady czasowej, który najbardziej Ci odpowiada.


![GREEN 2FA MULTISIG](assets/fr/30.webp)


Można teraz wyjść z tego menu. Urządzenie Multisig Wallet jest gotowe!


![GREEN 2FA MULTISIG](assets/fr/31.webp)


## Konfiguracja Wallet na Blockstream Green


Jeśli chcesz spersonalizować Wallet, kliknij trzy małe kropki w prawym górnym rogu.


![GREEN 2FA MULTISIG](assets/fr/32.webp)


Opcja "*Rename*" pozwala dostosować nazwę Wallet, co jest szczególnie przydatne w przypadku zarządzania kilkoma portfelami w tej samej aplikacji.


![GREEN 2FA MULTISIG](assets/fr/33.webp)


Menu "*Unit*" umożliwia zmianę jednostki bazowej Wallet. Można na przykład wybrać wyświetlanie w satoshis zamiast w bitcoinach.


![GREEN 2FA MULTISIG](assets/fr/34.webp)


Menu "*Ustawienia*" zapewnia dostęp do różnych opcji urządzenia Bitcoin Wallet.


![GREEN 2FA MULTISIG](assets/fr/35.webp)


Tutaj na przykład znajduje się rozszerzony klucz publiczny i jego *deskryptor*, przydatne, jeśli planujesz skonfigurować Wallet w trybie tylko do obserwacji z tego Wallet.


![GREEN 2FA MULTISIG](assets/fr/36.webp)


Można również zmienić kod PIN Wallet i aktywować połączenie biometryczne.


![GREEN 2FA MULTISIG](assets/fr/37.webp)


## Korzystanie z Blockstream Green


Po skonfigurowaniu Bitcoin Wallet możesz odebrać swój pierwszy Sats! Wystarczy kliknąć przycisk "*Odbierz*".


![GREEN 2FA MULTISIG](assets/fr/38.webp)


Green wyświetli wówczas pierwszy pusty odbierający Address w Wallet. Możesz zeskanować powiązany kod QR lub skopiować Address bezpośrednio, aby wysłać bitcoiny. Ten typ Address nie określa kwoty do wysłania przez płatnika. Można jednak wysłać generate na Address z żądaniem określonej kwoty, klikając trzy małe kropki w prawym górnym rogu, a następnie "*Zażądaj kwoty*" i wprowadzając żądaną kwotę.


![GREEN 2FA MULTISIG](assets/fr/39.webp)


Gdy transakcja zostanie wyemitowana w sieci, pojawi się w Wallet.


![GREEN 2FA MULTISIG](assets/fr/40.webp)


Poczekaj, aż otrzymasz wystarczającą liczbę potwierdzeń, aby uznać transakcję za ostateczną.


![GREEN 2FA MULTISIG](assets/fr/41.webp)


Mając bitcoiny w Wallet, możesz teraz również wysyłać bitcoiny. Kliknij "*Wyślij*".


![GREEN 2FA MULTISIG](assets/fr/42.webp)


Na następnej stronie wprowadź numer Address odbiorcy. Można wprowadzić go ręcznie lub zeskanować kod QR.


![GREEN 2FA MULTISIG](assets/fr/43.webp)


Wybierz kwotę płatności.


![GREEN 2FA MULTISIG](assets/fr/44.webp)


W dolnej części ekranu można wybrać stawkę opłaty dla tej transakcji. Użytkownik ma do wyboru zastosowanie się do zaleceń aplikacji lub dostosowanie własnych opłat. Im wyższa opłata w stosunku do innych oczekujących transakcji, tym szybciej transakcja zostanie przetworzona. Informacje na temat rynku opłat można znaleźć na stronie [Mempool.space](https://Mempool.space/) w sekcji "*Opłaty transakcyjne*".


![GREEN 2FA MULTISIG](assets/fr/45.webp)


Kliknij "*Next*", aby przejść do ekranu podsumowania transakcji. Sprawdź, czy Address, kwota i opłaty są prawidłowe.


![GREEN 2FA MULTISIG](assets/fr/46.webp)


Jeśli wszystko pójdzie dobrze, przesuń przycisk Green u dołu ekranu w prawo, aby podpisać i rozgłosić transakcję w sieci Bitcoin.


![GREEN 2FA MULTISIG](assets/fr/47.webp)


W tym momencie należy wprowadzić kod uwierzytelniający, aby odblokować drugi klucz Multisig przechowywany przez Blockstream. Wprowadź 6-cyfrowy kod wyświetlany w aplikacji uwierzytelniającej.


![GREEN 2FA MULTISIG](assets/fr/48.webp)


Transakcja pojawi się teraz na pulpicie nawigacyjnym Bitcoin Wallet w oczekiwaniu na potwierdzenie.


![GREEN 2FA MULTISIG](assets/fr/49.webp)


Teraz już wiesz, jak łatwo skonfigurować 2/2 Multisig Wallet przy użyciu opcji 2FA Blockstream Green!


Jeśli uznałeś ten poradnik za przydatny, będę wdzięczny za pozostawienie kciuka Green poniżej. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dziękuję bardzo!


Polecam również zapoznanie się z innym obszernym samouczkiem na temat aplikacji mobilnej Blockstream Green w celu skonfigurowania Liquid Wallet :


https://planb.network/tutorials/wallet/mobile/blockstream-green-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a