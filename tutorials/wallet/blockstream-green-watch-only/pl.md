---
name: Blockstream Green - tylko do oglądania
description: Konfiguracja Watch-only wallet
---
![cover](assets/cover.webp)


W tym samouczku dowiesz się, jak łatwo skonfigurować Wallet "tylko do oglądania" na urządzeniach mobilnych za pomocą aplikacji Blockstream Green.


## Co to jest Watch-only wallet?


Wallet tylko do odczytu lub "Watch-only wallet" to rodzaj oprogramowania zaprojektowanego w celu umożliwienia użytkownikowi obserwowania transakcji powiązanych z jednym lub większą liczbą określonych kluczy publicznych Bitcoin, bez dostępu do odpowiadających im kluczy prywatnych.


Ten typ aplikacji przechowuje tylko dane potrzebne do monitorowania Bitcoin Wallet, w szczególności do przeglądania jego salda i historii transakcji, ale nie ma dostępu do kluczy prywatnych. W rezultacie niemożliwe jest wydawanie Bitcoinów posiadanych przez Wallet w aplikacji tylko do monitorowania.


![GREEN-WATCH-ONLY](assets/fr/01.webp)


Watch-only jest zwykle używany w połączeniu z Hardware Wallet. Umożliwia to bezpieczne przechowywanie kluczy prywatnych Wallet na sprzęcie, który nie jest podłączony do Internetu i ma bardzo małą powierzchnię ataku, izolując w ten sposób klucze prywatne od potencjalnie wrażliwych środowisk. Z drugiej strony, aplikacja watch-only przechowuje wyłącznie rozszerzony klucz publiczny (`xpub`, `zpub` itp.) Bitcoin Wallet. Tego klucza nadrzędnego nie można użyć do znalezienia powiązanych kluczy prywatnych, a zatem nie można go użyć do wydawania Bitcoinów. Umożliwia on jednak wyprowadzenie podrzędnych kluczy publicznych i adresów odbiorczych. Dzięki wiedzy Hardware Wallet na temat bezpiecznych adresów Wallet, aplikacja watch-only może śledzić te transakcje w sieci Bitcoin, umożliwiając użytkownikowi monitorowanie jego salda i nowych adresów odbiorczych generate, bez konieczności podłączania Hardware Wallet za każdym razem.


W tym samouczku chciałbym przedstawić jedno z najpopularniejszych rozwiązań mobilnych Wallet: **Blockstream Green**.


![GREEN-WATCH-ONLY](assets/fr/02.webp)


## Przedstawiamy Blockstream Green


Blockstream Green to aplikacja dostępna na urządzenia mobilne i stacjonarne. Wcześniej znany jako Green Address, ten Wallet stał się projektem Blockstream po jego przejęciu w 2016 roku.


Green to bardzo łatwa w użyciu aplikacja, dzięki czemu jest szczególnie odpowiednia dla początkujących. Oferuje szereg funkcji, takich jak zarządzanie portfelami Hot, portfelami sprzętowymi i portfelami Liquid Sidechain.


W tym poradniku skupimy się wyłącznie na tworzeniu Watch-only wallet. Aby poznać inne zastosowania Green, zapoznaj się z naszymi innymi dedykowanymi samouczkami:


https://planb.network/tutorials/wallet/desktop/blockstream-green-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da

https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143

## Instalowanie i konfigurowanie aplikacji Blockstream Green


Pierwszym krokiem jest oczywiście pobranie aplikacji Green. Przejdź do sklepu z aplikacjami:



- [Dla systemu Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [For Apple](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590).

![GREEN-WATCH-ONLY](assets/fr/03.webp)


Użytkownicy Androida mogą również zainstalować aplikację za pomocą pliku `.apk` [dostępnego na GitHubie Blockstream] (https://github.com/Blockstream/green_android/releases).


![GREEN-WATCH-ONLY](assets/fr/04.webp)


Uruchom aplikację, a następnie zaznacz pole "Akceptuję warunki...*".


![GREEN-WATCH-ONLY](assets/fr/05.webp)


Po pierwszym otwarciu Green ekran główny pojawia się bez skonfigurowanego Wallet. Później, jeśli utworzysz lub zaimportujesz portfele, pojawią się one w tym Interface. Zanim przejdziesz do tworzenia Wallet, radzę dostosować ustawienia aplikacji do swoich potrzeb. Kliknij "Ustawienia aplikacji".


![GREEN-WATCH-ONLY](assets/fr/06.webp)


Opcja "*Enhanced Privacy*", dostępna tylko w systemie Android, zwiększa prywatność poprzez wyłączenie zrzutów ekranu i ukrywanie podglądu aplikacji. Automatycznie blokuje również dostęp do aplikacji, gdy tylko telefon zostanie zablokowany, co utrudnia ujawnienie danych.


![GREEN-WATCH-ONLY](assets/fr/07.webp)


Dla tych, którzy chcą zwiększyć swoją prywatność, aplikacja oferuje opcję rootowania ruchu za pośrednictwem sieci Tor, która szyfruje wszystkie połączenia i utrudnia śledzenie aktywności użytkownika. Chociaż opcja ta może nieco spowolnić działanie aplikacji, jest ona wysoce zalecana w celu ochrony prywatności, zwłaszcza jeśli nie korzystasz z własnego kompletnego węzła.


![GREEN-WATCH-ONLY](assets/fr/08.webp)


Dla użytkowników posiadających własny kompletny węzeł Green Wallet oferuje możliwość połączenia się z nim za pośrednictwem serwera Electrum, gwarantując całkowitą kontrolę nad informacjami sieciowymi Bitcoin i dystrybucją transakcji.


![GREEN-WATCH-ONLY](assets/fr/09.webp)


Inną alternatywną funkcją jest opcja "*SPV Verification*", która umożliwia bezpośrednią weryfikację niektórych danych Blockchain, a tym samym zmniejsza potrzebę ufania domyślnemu węzłowi Blockstream, chociaż ta metoda nie zapewnia wszystkich gwarancji Full node.


![GREEN-WATCH-ONLY](assets/fr/10.webp)


Po dostosowaniu tych ustawień do swoich potrzeb, kliknij przycisk "*Zapisz*" i uruchom ponownie aplikację.


![GREEN-WATCH-ONLY](assets/fr/11.webp)


## Utwórz Watch-only wallet na Blockstream Green


Teraz możesz utworzyć Watch-only wallet. Kliknij przycisk "*Get Started*".


![GREEN-WATCH-ONLY](assets/fr/12.webp)


Będziesz mógł wybrać pomiędzy kilkoma typami Wallet. W tym samouczku chcemy utworzyć Watch-only wallet, więc kliknij odpowiedni przycisk.


![GREEN-WATCH-ONLY](assets/fr/13.webp)


Wybierz opcję "Pojedynczy podpis".


![GREEN-WATCH-ONLY](assets/fr/14.webp)


Następnie wybierz "*Bitcoin*". Z mojej strony przeprowadzam ten samouczek na Testnet Wallet, ale procedura pozostaje identyczna na Mainnet.


![GREEN-WATCH-ONLY](assets/fr/15.webp)


Zostaniesz poproszony o podanie rozszerzonego klucza publicznego (`xpub`, `zpub` itp.) lub deskryptora skryptu wyjściowego.


![GREEN-WATCH-ONLY](assets/fr/16.webp)


W związku z tym konieczne będzie pobranie tych informacji z Wallet, który ma być śledzony za pośrednictwem Watch-only wallet. Rozszerzony klucz publiczny nie jest wrażliwy pod względem bezpieczeństwa, ponieważ nie pozwala na dostęp do kluczy prywatnych, ale jest wrażliwy ze względu na poufność, ponieważ ujawnia wszystkie klucze publiczne, a tym samym wszystkie transakcje Bitcoin.


Załóżmy, że używasz Sparrow Wallet do zarządzania Wallet na Hardware Wallet, znajdziesz te informacje w sekcji "*Ustawienia*". Znalezienie tych informacji zależy od używanego oprogramowania do zarządzania Wallet, ale zazwyczaj znajdują się one w ustawieniach.


![GREEN-WATCH-ONLY](assets/fr/17.webp)


Skopiuj swój rozszerzony klucz publiczny i wprowadź go w aplikacji Green, a następnie kliknij "Połącz".


![GREEN-WATCH-ONLY](assets/fr/18.webp)


Będziesz wtedy mógł zobaczyć saldo powiązane z tym kluczem, a także historię transakcji.


![GREEN-WATCH-ONLY](assets/fr/19.webp)


Klikając na "*Odbierz*", możesz generate otrzymać Address, aby otrzymać bitcoiny na Hardware Wallet. Odradzam jednak korzystanie z tej opcji bez uprzedniego sprawdzenia na ekranie Hardware Wallet, czy posiada on klucz prywatny powiązany z wygenerowanym Address, przed użyciem go do zablokowania bitcoinów. Jest to dobra praktyka, której należy przestrzegać.


![GREEN-WATCH-ONLY](assets/fr/20.webp)


Opcja "*Balayer*" umożliwia ręczne wprowadzenie klucza prywatnego w celu wydania środków bezpośrednio z aplikacji Green. Z wyjątkiem bardzo szczególnych przypadków, nie zalecam korzystania z tej funkcji, ponieważ wymaga ona ujawnienia klucza prywatnego na telefonie, który jest znacznie bardziej podatny na ataki komputerowe niż Hardware Wallet.


![GREEN-WATCH-ONLY](assets/fr/21.webp)


Teraz już wiesz, jak łatwo skonfigurować Watch-only wallet na smartfonie! Jest to przydatne narzędzie do monitorowania Wallet na Hardware Wallet bez konieczności podłączania i odblokowywania go za każdym razem.


Jeśli ten poradnik okazał się przydatny, będę wdzięczny za pozostawienie poniżej kciuka Green. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dziękuję bardzo!


Polecam również zapoznanie się z innym obszernym samouczkiem na temat aplikacji Blockstream Green do konfiguracji Hot Wallet:


https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143