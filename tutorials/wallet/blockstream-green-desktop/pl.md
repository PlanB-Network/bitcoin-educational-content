---
name: Blockstream Green - Pulpit
description: Korzystanie z Green Wallet na komputerze
---
![cover](assets/cover.webp)


W tym samouczku zbadamy, jak używać oprogramowania Blockstream Green na komputerze do zarządzania bezpiecznym Wallet na Hardware Wallet. Podczas korzystania z Hardware Wallet niezbędne jest użycie oprogramowania na komputerze do zarządzania Wallet. To oprogramowanie zarządzające nie ma dostępu do kluczy prywatnych; służy wyłącznie do sprawdzania salda Wallet, adresów odbiorczych generate oraz tworzenia i dystrybucji transakcji do podpisania przez Hardware Wallet. Green to tylko jedno z wielu dostępnych rozwiązań do zarządzania Bitcoin Hardware Wallet.


W 2024 r. Blockstream Green jest kompatybilny tylko z urządzeniami Ledger Nano S (stara wersja), Ledger Nano X, Trezor One, Trezor T i Blockstream Jade.


## Przedstawiamy Blockstream Green


Blockstream Green to aplikacja dostępna na urządzenia mobilne i stacjonarne. Wcześniej znany jako Green Address, ten Wallet stał się projektem Blockstream po jego przejęciu w 2016 roku.


Green to bardzo łatwa w użyciu aplikacja, dzięki czemu jest szczególnie odpowiednia dla początkujących. Oferuje różne funkcje, takie jak zarządzanie portfelami Hot, portfelami sprzętowymi, a także portfelami na Liquid Sidechain. Można jej również użyć do skonfigurowania Watch-only wallet.


![GREEN-DESKTOP](assets/fr/01.webp)


W tym samouczku skoncentrujemy się wyłącznie na korzystaniu z oprogramowania na komputerze. Aby poznać inne zastosowania Green, zapoznaj się z naszymi innymi dedykowanymi samouczkami:


https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

https://planb.network/tutorials/wallet/mobile/blockstream-green-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

## Instalacja i konfiguracja oprogramowania Blockstream Green


Zacznij od zainstalowania oprogramowania Blockstream Green na swoim komputerze. Wejdź na [oficjalną stronę internetową] (https://blockstream.com/Green/) i kliknij przycisk "*Download Now*". Następnie postępuj zgodnie z procesem instalacji w zależności od systemu operacyjnego.


![GREEN-DESKTOP](assets/fr/02.webp)


Uruchom aplikację, a następnie zaznacz pole "Akceptuję warunki...*".


![GREEN-DESKTOP](assets/fr/03.webp)


Po otwarciu Green po raz pierwszy, ekran główny pojawia się bez skonfigurowanego Wallet. Później, jeśli utworzysz lub zaimportujesz portfele, pojawią się one w tym Interface. Przed przystąpieniem do tworzenia Wallet zalecam dostosowanie ustawień aplikacji do własnych potrzeb. Kliknij ikonę Ustawienia w lewym dolnym rogu.


![GREEN-DESKTOP](assets/fr/04.webp)


W menu "*Ogólne*" można zmienić język oprogramowania i aktywować funkcje eksperymentalne.


![GREEN-DESKTOP](assets/fr/05.webp)


W menu "*Sieć*" można włączyć połączenie przez sieć Tor, która szyfruje wszystkie połączenia i utrudnia śledzenie aktywności użytkownika. Chociaż opcja ta może nieco spowolnić działanie aplikacji, jest wysoce zalecana w celu ochrony prywatności, zwłaszcza jeśli nie korzystasz z własnego pełnego węzła.


![GREEN-DESKTOP](assets/fr/06.webp)


Dla użytkowników, którzy posiadają własny kompletny węzeł, Green oferuje opcję połączenia się z nim za pośrednictwem serwera Electrum, gwarantując całkowitą kontrolę nad informacjami sieciowymi Bitcoin i rozpowszechnianiem transakcji. Aby to zrobić, kliknij menu "*Serwery niestandardowe i walidacja*", a następnie wprowadź dane serwera Electrum.


![GREEN-DESKTOP](assets/fr/07.webp)


Inną alternatywną funkcją jest opcja "*SPV Verification*", która pozwala bezpośrednio zweryfikować niektóre dane Blockchain, a tym samym zmniejszyć potrzebę zaufania domyślnemu węzłowi Blockstream, chociaż ta metoda nie zapewnia wszystkich gwarancji Full node. Opcję tę można również znaleźć w menu "*Serwery niestandardowe i walidacja*".


![GREEN-DESKTOP](assets/fr/08.webp)


Po dostosowaniu tych parametrów do własnych potrzeb, można zamknąć Interface.


## Import Bitcoin Wallet na Blockstream Green


Jesteś teraz gotowy do zaimportowania Bitcoin Wallet. Kliknij przycisk "**Get Started**".


![GREEN-DESKTOP](assets/fr/09.webp)


Można wybrać pomiędzy utworzeniem lokalnego Software Wallet lub zarządzaniem Cold Wallet poprzez Hardware Wallet. W tym samouczku skoncentrujemy się na zarządzaniu Hardware Wallet, więc należy wybrać opcję "*On Hardware Wallet*".


Opcja "*Watch-only*" pozwala zaimportować rozszerzony klucz publiczny (`xpub`) w celu przeglądania transakcji Wallet bez możliwości wydawania powiązanych środków.


![GREEN-DESKTOP](assets/fr/10.webp)


Jeśli używasz Jade, kliknij odpowiedni przycisk. W przeciwnym razie wybierz opcję "*Podłącz inne urządzenie sprzętowe*". W moim przypadku używam Ledger Nano S. Użytkownicy Ledger powinni zainstalować aplikację "*Bitcoin Legacy*" na Hardware Wallet, ponieważ Green obsługuje tylko tę wersję.


![GREEN-DESKTOP](assets/fr/11.webp)


Podłącz Hardware Wallet do komputera i wybierz Green.


![GREEN-DESKTOP](assets/fr/12.webp)


Poczekaj, aż Green zaimportuje informacje Wallet, po czym uzyskasz do nich dostęp.


![GREEN-DESKTOP](assets/fr/13.webp)


W tym momencie możliwe są dwa scenariusze. Jeśli korzystałeś już wcześniej z Hardware Wallet, powinieneś zobaczyć swoje konto w oprogramowaniu. Jeśli jednak, tak jak ja, dopiero co zainicjowałeś swój Hardware Wallet, generując frazę Mnemonic i jeszcze z niego nie korzystałeś, musisz utworzyć konto. Kliknij na "*Create Account*".


![GREEN-DESKTOP](assets/fr/14.webp)


Wybierz "*Standard*", jeśli chcesz używać klasycznego Wallet.


![GREEN-DESKTOP](assets/fr/15.webp)


Masz teraz dostęp do swojego konta.


![GREEN-DESKTOP](assets/fr/16.webp)


## Używanie Hardware Wallet z Blockstream Green


Teraz, gdy twój Bitcoin Wallet jest już skonfigurowany, możesz odebrać swój pierwszy Sats! Wystarczy kliknąć przycisk "*Odbierz*".


![GREEN-DESKTOP](assets/fr/17.webp)


Kliknij przycisk "*Kopiuj Address*", aby skopiować Address lub zeskanować jego kod QR.


![GREEN-DESKTOP](assets/fr/18.webp)


Gdy transakcja zostanie wyemitowana w sieci, pojawi się w Wallet. Poczekaj, aż otrzymasz wystarczającą liczbę potwierdzeń, aby uznać transakcję za niezmienną.


![GREEN-DESKTOP](assets/fr/19.webp)


Mając bitcoiny w Wallet, możesz je teraz wysłać. Kliknij przycisk "*Wyślij*".


![GREEN-DESKTOP](assets/fr/20.webp)


Na następnej stronie wprowadź numer Address odbiorcy. Możesz wprowadzić go ręcznie lub zeskanować kod QR za pomocą kamery internetowej.


![GREEN-DESKTOP](assets/fr/21.webp)


Wybierz kwotę płatności.


![GREEN-DESKTOP](assets/fr/22.webp)


W dolnej części ekranu można wybrać stawkę opłaty dla tej transakcji. Użytkownik ma do wyboru zastosowanie się do zaleceń aplikacji lub dostosowanie własnych opłat. Im wyższa opłata w stosunku do innych oczekujących transakcji, tym szybciej transakcja zostanie przetworzona. Informacje na temat rynku opłat można znaleźć na stronie [Mempool.space](https://Mempool.space/) w sekcji "*Opłaty transakcyjne*".


![GREEN-DESKTOP](assets/fr/23.webp)


Jeśli chcesz wybrać konkretnie, które UTXO mają zostać użyte w transakcji, kliknij przycisk "*Ręczny wybór monet*".


![GREEN-DESKTOP](assets/fr/24.webp)


Sprawdź parametry transakcji i, jeśli wszystko jest zgodne z oczekiwaniami, kliknij "*Next*".


![GREEN-DESKTOP](assets/fr/25.webp)


Sprawdź dwukrotnie, czy Address, kwota i opłaty są prawidłowe, a następnie kliknij "*Potwierdź transakcję*".


![GREEN-DESKTOP](assets/fr/26.webp)


Upewnij się, że wszystkie parametry transakcji są prawidłowe na ekranie Hardware Wallet, a następnie podpisz transakcję za jego pomocą.


![GREEN-DESKTOP](assets/fr/27.webp)


Po podpisaniu transakcji z Hardware Wallet, Green automatycznie rozgłasza ją do sieci Bitcoin. Transakcja pojawi się następnie na pulpicie nawigacyjnym Bitcoin Wallet w oczekiwaniu na potwierdzenie.


![GREEN-DESKTOP](assets/fr/28.webp)


Teraz już wiesz, jak łatwo skonfigurować Blockstream Green do zarządzania Bitcoin Wallet na Hardware Wallet.


Jeśli ten poradnik okazał się przydatny, będę wdzięczny za pozostawienie poniżej kciuka Green. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dziękuję bardzo!


Polecam również zapoznanie się z innym obszernym samouczkiem dotyczącym aplikacji mobilnej Blockstream Green w celu skonfigurowania Hot Wallet:


https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143
