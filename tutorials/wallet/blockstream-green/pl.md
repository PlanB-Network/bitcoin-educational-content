---
name: Blockstream Green - Mobile
description: Konfiguracja mobilnego Software Wallet
---
![cover](assets/cover.webp)


Software Wallet to aplikacja instalowana na komputerze, smartfonie lub innym urządzeniu podłączonym do Internetu, umożliwiająca zarządzanie i zabezpieczanie kluczy Bitcoin Wallet. W przeciwieństwie do portfeli sprzętowych, które izolują klucze prywatne, portfele "Hot" działają zatem w środowisku potencjalnie narażonym na ataki cybernetyczne, zwiększając ryzyko piractwa i kradzieży.


Portfele programowe powinny być używane do zarządzania rozsądnymi ilościami bitcoinów, zwłaszcza do codziennych transakcji. Mogą być również interesującą opcją dla osób z ograniczonymi aktywami Bitcoin, dla których inwestycja w Hardware Wallet może wydawać się nieproporcjonalna. Jednak ich stała ekspozycja na Internet sprawia, że są mniej bezpieczne do przechowywania długoterminowych oszczędności lub dużych funduszy. W tym drugim przypadku najlepiej zdecydować się na bezpieczniejsze rozwiązania, takie jak portfele sprzętowe.


W tym poradniku chciałbym przedstawić jedno z najlepszych rozwiązań mobilnych Software Wallet: **Blockstream Green**.


![GREEN](assets/fr/01.webp)


Jeśli chcesz dowiedzieć się, jak korzystać z Blockstream Green na swoim komputerze, zapoznaj się z tym innym samouczkiem:


https://planb.network/tutorials/wallet/desktop/blockstream-green-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da

## Przedstawiamy Blockstream Green


Blockstream Green to Software Wallet dostępny na urządzeniach mobilnych i komputerach stacjonarnych. Wcześniej znany jako *Green Address*, ten Wallet stał się projektem Blockstream po jego przejęciu w 2016 roku.


Green jest szczególnie łatwą w użyciu aplikacją, co czyni ją interesującą dla początkujących. Oferuje wszystkie niezbędne funkcje dobrego Bitcoin Wallet, w tym RBF (*Replace-by-fee*), opcję połączenia Tor, możliwość podłączenia własnego węzła, SPV (*Simple Payment Verification*), tagowanie monet i kontrolę.


Blockstream Green obsługuje również Liquid Network, Bitcoin Sidechain opracowany przez Blockstream na szybko, Confidential Transactions poza głównym Blockchain. Ten samouczek koncentruje się wyłącznie na Bitcoin, ale w późniejszym czasie zostanie omówione korzystanie z Liquid.


## Instalowanie i konfigurowanie aplikacji Blockstream Green


Pierwszym krokiem jest oczywiście pobranie aplikacji Green. Przejdź do sklepu z aplikacjami:



- [Dla systemu Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [For Apple](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590).

![GREEN](assets/fr/02.webp)


Użytkownicy Androida mogą również zainstalować aplikację za pomocą pliku `.apk` [dostępnego na GitHubie Blockstream] (https://github.com/Blockstream/green_android/releases).


![GREEN](assets/fr/03.webp)


Uruchom aplikację, a następnie zaznacz pole "Akceptuję warunki...*".


![GREEN](assets/fr/04.webp)


Po pierwszym otwarciu Green ekran główny pojawia się bez skonfigurowanego Wallet. Później, jeśli utworzysz lub zaimportujesz portfele, pojawią się one w tym Interface. Zanim przejdziesz do tworzenia Wallet, radzę dostosować ustawienia aplikacji do swoich potrzeb. Kliknij "Ustawienia aplikacji".


![GREEN](assets/fr/05.webp)


Opcja "*Enhanced Privacy*", dostępna tylko w systemie Android, zwiększa prywatność poprzez wyłączenie zrzutów ekranu i ukrywanie podglądu aplikacji. Automatycznie blokuje również dostęp do aplikacji, gdy tylko telefon zostanie zablokowany, co utrudnia ujawnienie danych.


![GREEN](assets/fr/06.webp)


Dla tych, którzy chcą zwiększyć swoją prywatność, aplikacja oferuje opcję rootowania ruchu za pośrednictwem sieci Tor, która szyfruje wszystkie połączenia i utrudnia śledzenie aktywności użytkownika. Chociaż opcja ta może nieco spowolnić działanie aplikacji, jest ona wysoce zalecana w celu ochrony prywatności, zwłaszcza jeśli nie korzystasz z własnego kompletnego węzła.


![GREEN](assets/fr/07.webp)


Dla użytkowników posiadających własny kompletny węzeł Green Wallet oferuje możliwość połączenia się z nim za pośrednictwem serwera Electrum, gwarantując całkowitą kontrolę nad informacjami sieciowymi Bitcoin i dystrybucją transakcji.


![GREEN](assets/fr/08.webp)


Inną alternatywną funkcją jest opcja "*SPV Verification*", która umożliwia bezpośrednią weryfikację niektórych danych Blockchain, a tym samym zmniejsza potrzebę ufania domyślnemu węzłowi Blockstream, chociaż ta metoda nie zapewnia wszystkich gwarancji Full node.


![GREEN](assets/fr/09.webp)


Po dostosowaniu tych ustawień do swoich potrzeb, kliknij przycisk "*Zapisz*" i uruchom ponownie aplikację.


![GREEN](assets/fr/10.webp)


## Utwórz Bitcoin Wallet na Blockstream Green


Teraz możesz utworzyć Bitcoin Wallet. Kliknij przycisk "*Get Started*".


![GREEN](assets/fr/11.webp)


Można wybrać między utworzeniem lokalnego Software Wallet lub zarządzaniem Cold Wallet za pośrednictwem Hardware Wallet. W tym samouczku skoncentrujemy się na tworzeniu Hot Wallet, więc będziesz musiał wybrać opcję "*On This Device*". W przyszłym samouczku pokażę, jak korzystać z drugiej opcji.


Opcja "*Watch-only*" pozwala zaimportować rozszerzony klucz publiczny (`xpub`), aby zobaczyć transakcje Wallet bez możliwości wydawania powiązanych środków, co jest przydatne na przykład do śledzenia Wallet na Hardware Wallet.


![GREEN](assets/fr/12.webp)


Następnie można przywrócić istniejący Bitcoin Wallet lub utworzyć nowy. Na potrzeby tego samouczka utworzymy nowy Wallet. Jeśli jednak musisz zregenerować istniejący Bitcoin Wallet z jego frazy Mnemonic, na przykład po utracie Hardware Wallet, musisz wybrać drugą opcję.


![GREEN](assets/fr/13.webp)


Następnie można wybrać 12- lub 24-wyrazową frazę Mnemonic. Ta fraza umożliwi odzyskanie dostępu do Wallet z dowolnego kompatybilnego oprogramowania w przypadku problemu z telefonem. Obecnie wybór 24-wyrazowej frazy nie zapewnia większego bezpieczeństwa niż fraza 12-wyrazowa. Dlatego zalecam wybór 12-wyrazowej frazy Mnemonic.


Green przekaże następnie frazę Mnemonic. Przed kontynuowaniem upewnij się, że nie jesteś obserwowany. Kliknij "*Pokaż frazę odzyskiwania*", aby wyświetlić ją na ekranie.


![GREEN](assets/fr/14.webp)


**Mnemonic zapewnia pełny, nieograniczony dostęp do wszystkich bitcoinów **Każdy posiadacz Mnemonic może ukraść Twoje środki, nawet bez fizycznego dostępu do telefonu.


Przywraca ona dostęp do bitcoinów w przypadku utraty, kradzieży lub uszkodzenia telefonu. Dlatego bardzo ważne jest, aby starannie wykonać kopię zapasową **na nośniku fizycznym (nie cyfrowym)** i przechowywać ją w bezpiecznym miejscu. Możesz zapisać ją na kartce papieru lub dla dodatkowego bezpieczeństwa, jeśli jest to duży Wallet, zalecam wygrawerowanie jej na wsporniku ze stali nierdzewnej, aby chronić ją przed ryzykiem pożaru, powodzi lub zawalenia (w przypadku Hot Wallet zaprojektowanego do zabezpieczenia niewielkiej ilości bitcoinów, prawdopodobnie wystarczy zwykła kopia zapasowa na papierze).


*Oczywiście nigdy nie wolno udostępniać tych słów w Internecie, tak jak robię to w tym samouczku. Ten przykładowy Wallet będzie używany tylko na Testnet i zostanie usunięty po zakończeniu samouczka


![GREEN](assets/fr/15.webp)


Po prawidłowym nagraniu frazy Mnemonic na nośniku fizycznym, kliknij "*Kontynuuj*". Green Wallet poprosi o potwierdzenie niektórych słów w frazie Mnemonic, aby upewnić się, że zostały one poprawnie nagrane. Wypełnij puste miejsca brakującymi słowami.


![GREEN](assets/fr/16.webp)


Wybierz kod PIN urządzenia, który zostanie użyty do odblokowania Green Wallet. Jest to zabezpieczenie przed nieautoryzowanym dostępem fizycznym. Ten kod PIN nie bierze udziału w tworzeniu kluczy kryptograficznych Wallet. Tak więc, nawet bez dostępu do tego kodu PIN, posiadanie 12- lub 24-wyrazowej frazy Mnemonic umożliwi odzyskanie dostępu do bitcoinów.


Zalecamy wybranie możliwie losowego 6-cyfrowego kodu PIN. Pamiętaj, aby zapisać ten kod, aby go nie zapomnieć, w przeciwnym razie będziesz zmuszony do odzyskania Wallet z Mnemonic. Następnie możesz dodać opcję blokowania biometrycznego, aby uniknąć konieczności wprowadzania kodu PIN za każdym razem, gdy go używasz. Ogólnie rzecz biorąc, dane biometryczne są znacznie mniej bezpieczne niż sam kod PIN. Dlatego domyślnie radzę nie ustawiać tej opcji odblokowywania.


![GREEN](assets/fr/17.webp)


Wprowadź kod PIN po raz drugi, aby go potwierdzić.


![GREEN](assets/fr/18.webp)


Poczekaj na utworzenie Wallet, a następnie kliknij przycisk "*Utwórz konto*".


![GREEN](assets/fr/19.webp)


Następnie możesz wybrać między standardowym Wallet z pojedynczym podpisem, którego użyjemy w tym samouczku, a Wallet chronionym uwierzytelnianiem dwuskładnikowym (2FA).


![GREEN](assets/fr/20.webp)


Opcja 2FA w Green tworzy wielopodpisowy Wallet 2/2, z jednym kluczem przechowywanym przez Blockstream. Oznacza to, że do przeprowadzenia transakcji wymagane są oba klucze: klucz lokalny chroniony kodem PIN w telefonie oraz klucz zdalny zabezpieczony przez 2FA na serwerach Blockstream. W przypadku utraty dostępu do 2FA lub niedostępności usług Blockstream, mechanizmy odzyskiwania oparte na skryptach blokady czasowej zapewniają, że środki można odzyskać autonomicznie. Chociaż taka konfiguracja znacznie zmniejsza ryzyko kradzieży bitcoinów, jest ona bardziej złożona w zarządzaniu i częściowo zależna od Blockstream. W tym poradniku zdecydujemy się na klasyczny Wallet z pojedynczym podpisem, z kluczami przechowywanymi lokalnie na telefonie.


Twój Bitcoin Wallet został utworzony przy użyciu aplikacji Green!


![GREEN](assets/fr/21.webp)


Przed otrzymaniem pierwszych bitcoinów w Wallet, **Zalecam wykonanie testu odzyskiwania pustego konta**. Zanotuj informacje referencyjne, takie jak xpub lub pierwszy otrzymany Address, a następnie usuń Wallet w aplikacji Green, gdy jest jeszcze pusty. Następnie spróbuj przywrócić Wallet na Green przy użyciu papierowych kopii zapasowych. Sprawdź, czy informacje o plikach cookie wygenerowane po przywróceniu są zgodne z pierwotnie zapisanymi. Jeśli tak, możesz mieć pewność, że papierowe kopie zapasowe są niezawodne. Aby dowiedzieć się więcej o tym, jak przeprowadzić testowe odzyskiwanie, zapoznaj się z tym samouczkiem:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Konfiguracja Wallet na Blockstream Green


Jeśli chcesz spersonalizować Wallet, kliknij trzy małe kropki w prawym górnym rogu.


![GREEN](assets/fr/22.webp)


Opcja "*Rename*" pozwala dostosować nazwę Wallet, co jest szczególnie przydatne, jeśli zarządzasz kilkoma portfelami w tej samej aplikacji.


![GREEN](assets/fr/23.webp)


Menu "*Unit*" umożliwia zmianę jednostki bazowej Wallet. Można na przykład wybrać wyświetlanie w satoshis zamiast w bitcoinach.


![GREEN](assets/fr/24.webp)


Menu "*Ustawienia*" zapewnia dostęp do różnych opcji urządzenia Bitcoin Wallet.


![GREEN](assets/fr/25.webp)


Tutaj na przykład znajduje się rozszerzony klucz publiczny i jego *deskryptor*, przydatne, jeśli planujesz skonfigurować Wallet w trybie tylko do obserwacji z tego Wallet.


![GREEN](assets/fr/26.webp)


Można również zmienić kod PIN Wallet i aktywować połączenie biometryczne.


![GREEN](assets/fr/27.webp)


## Korzystanie z Blockstream Green


Po skonfigurowaniu Bitcoin Wallet możesz odebrać swój pierwszy Sats! Wystarczy kliknąć przycisk "*Odbierz*".


![GREEN](assets/fr/28.webp)


Green wyświetli pierwszy pusty Address w Wallet. Możesz zeskanować powiązany kod QR lub skopiować Address bezpośrednio, aby wysłać bitcoiny. Ten typ Address nie określa kwoty do wysłania przez płatnika. Można jednak wysłać Address z żądaniem określonej kwoty, klikając trzy małe kropki w prawym górnym rogu, a następnie "*Żądaj kwoty*" i wprowadzając żądaną kwotę.


Ponieważ używasz konta SegWit v0 (BIP84), twój Address będzie zaczynał się od `bc1q...`. W moim przykładzie używam Testnet Wallet, więc prefiks jest nieco inny.


![GREEN](assets/fr/29.webp)


Gdy transakcja zostanie wyemitowana w sieci, pojawi się w Wallet.


![GREEN](assets/fr/30.webp)


Poczekaj, aż otrzymasz wystarczającą liczbę potwierdzeń, aby uznać transakcję za ostateczną.


![GREEN](assets/fr/31.webp)


Mając bitcoiny w Wallet, możesz teraz również wysyłać bitcoiny. Kliknij "*Wyślij*".


![GREEN](assets/fr/32.webp)


Na następnej stronie wprowadź numer Address odbiorcy. Można wprowadzić go ręcznie lub zeskanować kod QR.


![GREEN](assets/fr/33.webp)


Wybierz kwotę płatności.


![GREEN](assets/fr/34.webp)


W dolnej części ekranu można wybrać stawkę opłaty dla tej transakcji. Użytkownik ma do wyboru zastosowanie się do zaleceń aplikacji lub dostosowanie własnych opłat. Im wyższa opłata w stosunku do innych oczekujących transakcji, tym szybciej transakcja zostanie przetworzona. Informacje na temat rynku opłat można znaleźć na stronie [Mempool.space](https://Mempool.space/) w sekcji "*Opłaty transakcyjne*".


![GREEN](assets/fr/35.webp)


Kliknij "*Next*", aby przejść do ekranu podsumowania transakcji. Sprawdź, czy Address, kwota i opłaty są prawidłowe.


![GREEN](assets/fr/36.webp)


Jeśli wszystko pójdzie dobrze, przesuń przycisk Green u dołu ekranu w prawo, aby podpisać i rozgłosić transakcję w sieci Bitcoin.


![GREEN](assets/fr/37.webp)


Transakcja pojawi się teraz na pulpicie nawigacyjnym Bitcoin Wallet w oczekiwaniu na potwierdzenie.


![GREEN](assets/fr/38.webp)


*Ten samouczek jest oparty na [oryginalnej wersji należącej do Bitstack](https://www.bitstack-app.com/blog/installer-portefeuille-Bitcoin-Green-Wallet) napisanej przez Loïca Morela. Bitstack to francuski neo-bank Bitcoin, który oferuje możliwość oszczędzania w bitcoinach, zarówno w DCA (Dollar Cost Averaging), jak i poprzez automatyczny system zaokrąglania codziennych wydatków.* Bitstack to francuski neo-bank Bitcoin, który oferuje możliwość oszczędzania w bitcoinach, zarówno w DCA (Dollar Cost Averaging), jak i poprzez automatyczny system zaokrąglania codziennych wydatków