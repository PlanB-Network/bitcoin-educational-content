---
name: Blockstream Green - Liquid
description: Konfigurowanie Wallet na Liquid Network Sidechain
---
![cover](assets/cover.webp)


Protokół Bitcoin ma celowe ograniczenia techniczne, które pomagają utrzymać decentralizację sieci i zapewnić bezpieczeństwo wszystkim użytkownikom. Ograniczenia te mogą jednak czasami frustrować użytkowników, szczególnie podczas przeciążenia spowodowanego dużą liczbą jednoczesnych transakcji. Debata na temat skalowalności Bitcoin od dawna dzieli społeczność, szczególnie podczas wojny o rozmiar bloków. Od tego czasu w społeczności Bitcoin powszechnie uznaje się, że skalowalność musi być zapewniona przez rozwiązania off-chain w systemach drugiego Layer. Rozwiązania te obejmują łańcuchy boczne, które są nadal stosunkowo nieznane i mało używane w porównaniu z innymi systemami, takimi jak Lightning Network.


Sidechain to niezależny Blockchain, który działa równolegle z głównym Bitcoin Blockchain. Wykorzystuje Bitcoin jako jednostkę rozliczeniową, dzięki mechanizmowi zwanemu "*two-way peg*". System ten umożliwia zablokowanie bitcoinów na głównym łańcuchu w celu odtworzenia ich wartości na Sidechain, gdzie krążą one w formie tokenów zabezpieczonych oryginalnymi bitcoinami. Tokeny te zwykle zachowują parytet wartości z bitcoinami zablokowanymi na głównym łańcuchu, a proces ten można odwrócić w celu odzyskania środków na Bitcoin.


Celem łańcuchów bocznych jest oferowanie dodatkowych funkcji lub ulepszeń technicznych, takich jak szybsze transakcje, niższe opłaty lub obsługa inteligentnych kontraktów. Innowacje te nie zawsze mogą być wdrożone bezpośrednio na Bitcoin Blockchain bez uszczerbku dla jego decentralizacji lub bezpieczeństwa. Łańcuchy boczne umożliwiają zatem testowanie i badanie nowych rozwiązań przy jednoczesnym zachowaniu integralności Bitcoin. Protokoły te często wymagają jednak kompromisów, szczególnie w zakresie decentralizacji i bezpieczeństwa, w zależności od wybranego modelu zarządzania i mechanizmu konsensusu.


Obecnie najbardziej znanym Sidechain jest prawdopodobnie Liquid. W tym samouczku najpierw powiem ci, czym jest Liquid, a następnie poprowadzę cię przez to, jak łatwo zacząć go używać z aplikacją Blockstream Green, abyś mógł cieszyć się wszystkimi jego zaletami.


![LIQUID GREEN](assets/fr/01.webp)


## Czym jest Liquid Network?


Liquid to sfederowana nakładka Sidechain na Bitcoin, opracowana przez Blockstream w celu poprawy szybkości transakcji, poufności i funkcjonalności. Wykorzystuje dwustronny mechanizm kotwiczenia ustanowiony w federacji w celu blokowania bitcoinów w głównym łańcuchu i tworzenia w zamian bitcoinów Liquid (L-BTC), tokenów krążących na Liquid, pozostając wspieranymi przez oryginalne bitcoiny.


![LIQUID GREEN](assets/fr/02.webp)


Liquid Network opiera się na federacji uczestników, złożonej z uznanych podmiotów z ekosystemu Bitcoin, którzy walidują bloki i zarządzają dwustronnym peggingiem. Oprócz L-BTC, Liquid umożliwia również emisję innych aktywów cyfrowych, takich jak stablecoiny i inne kryptowaluty.


![LIQUID GREEN](assets/fr/03.webp)


## Przedstawiamy Blockstream Green


Blockstream Green to Software Wallet dostępny na urządzeniach mobilnych i stacjonarnych. Wcześniej znany jako *Green Address*, ten Wallet stał się projektem Blockstream po jego przejęciu w 2016 roku.


Green jest szczególnie łatwą w użyciu aplikacją, co czyni ją interesującą dla początkujących. Oferuje wszystkie niezbędne funkcje dobrego Bitcoin Wallet, w tym RBF (*Replace-by-fee*), opcję połączenia Tor, możliwość podłączenia własnego węzła, SPV (*Simple Payment Verification*), tagowanie monet i kontrolę.


Blockstream Green obsługuje również Liquid Network i właśnie tego dowiemy się w tym samouczku. Jeśli chcesz użyć Green do innych zastosowań, polecam również zapoznać się z innymi samouczkami:


https://planb.network/tutorials/wallet/desktop/blockstream-green-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da

https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

https://planb.network/tutorials/wallet/mobile/blockstream-green-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

## Instalowanie i konfigurowanie aplikacji Blockstream Green


Pierwszym krokiem jest oczywiście pobranie aplikacji Green. Przejdź do sklepu z aplikacjami:



- [Dla systemu Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [For Apple](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590).

![LIQUID GREEN](assets/fr/04.webp)


Użytkownicy Androida mogą również zainstalować aplikację za pomocą pliku `.apk` [dostępnego na GitHubie Blockstream] (https://github.com/Blockstream/green_android/releases).


![LIQUID GREEN](assets/fr/05.webp)


Uruchom aplikację, a następnie zaznacz pole "Akceptuję warunki...*".


![LIQUID GREEN](assets/fr/06.webp)


Po pierwszym otwarciu Green ekran główny pojawia się bez skonfigurowanego Wallet. Później, jeśli utworzysz lub zaimportujesz portfele, pojawią się one w tym Interface. Przed przystąpieniem do tworzenia Wallet zalecam dostosowanie ustawień aplikacji do własnych potrzeb. Kliknij "Ustawienia aplikacji".


![LIQUID GREEN](assets/fr/07.webp)


Opcja "*Enhanced Privacy*", dostępna tylko w systemie Android, zwiększa prywatność poprzez wyłączenie zrzutów ekranu i ukrywanie podglądu aplikacji. Automatycznie blokuje również dostęp do aplikacji, gdy tylko telefon zostanie zablokowany, co utrudnia ujawnienie danych.


![LIQUID GREEN](assets/fr/08.webp)


Dla tych, którzy chcą zwiększyć swoją prywatność, aplikacja oferuje opcję rootowania ruchu za pośrednictwem sieci Tor, która szyfruje wszystkie połączenia i utrudnia śledzenie aktywności użytkownika. Chociaż opcja ta może nieco spowolnić działanie aplikacji, jest ona wysoce zalecana w celu ochrony prywatności, zwłaszcza jeśli nie korzystasz z własnego kompletnego węzła.


![LIQUID GREEN](assets/fr/09.webp)


Dla użytkowników posiadających własny kompletny węzeł Green Wallet oferuje możliwość połączenia się z nim za pośrednictwem serwera Electrum, gwarantując całkowitą kontrolę nad informacjami sieciowymi Bitcoin i rozpowszechnianiem transakcji. Ta funkcja jest jednak przeznaczona dla klasycznych portfeli Bitcoin, więc nie jest potrzebna, jeśli korzystasz z Liquid.


![LIQUID GREEN](assets/fr/10.webp)


Inną alternatywną funkcją jest opcja "*SPV Verification*", która pozwala bezpośrednio zweryfikować niektóre dane Blockchain, a tym samym zmniejszyć potrzebę zaufania domyślnemu węzłowi Blockstream, chociaż ta metoda nie zapewnia wszystkich gwarancji Full node. Ponownie, wpłynie to tylko na portfele onchain Bitcoin, a nie Liquid.


![LIQUID GREEN](assets/fr/11.webp)


Po dostosowaniu tych ustawień do swoich potrzeb, kliknij przycisk "*Zapisz*" i uruchom ponownie aplikację.


![LIQUID GREEN](assets/fr/12.webp)


## Utwórz Liquid Wallet na Blockstream Green


Jesteś teraz gotowy do utworzenia Liquid Wallet. Kliknij przycisk "*Get Started*" (Rozpocznij).


![LIQUID GREEN](assets/fr/13.webp)


Możesz wybrać między utworzeniem lokalnego Software Wallet lub zarządzaniem Cold Wallet za pośrednictwem Hardware Wallet. W tym samouczku skupiamy się na tworzeniu Hot Wallet na Liquid, więc musisz wybrać opcję "*On This Device*". Możesz także użyć kompatybilnego Hardware Wallet, takiego jak Blockstream Jade, aby zabezpieczyć Liquid Wallet.


![LIQUID GREEN](assets/fr/14.webp)


Następnie można przywrócić istniejący Bitcoin Wallet lub utworzyć nowy. Na potrzeby tego samouczka utworzymy nowy Wallet. Jeśli jednak musisz zregenerować istniejący Liquid Wallet z jego frazy Mnemonic, na przykład po utracie Hardware Wallet, musisz wybrać drugą opcję.


![LIQUID GREEN](assets/fr/15.webp)


Następnie można wybrać 12- lub 24-wyrazową frazę Mnemonic. Ta fraza umożliwi odzyskanie dostępu do Wallet z dowolnego kompatybilnego oprogramowania w przypadku problemu z telefonem. Obecnie wybór 24-wyrazowej frazy nie zapewnia większego bezpieczeństwa niż fraza 12-wyrazowa. Dlatego zalecam wybór 12-wyrazowej frazy Mnemonic.


Następnie Green poda frazę Mnemonic. Przed kontynuowaniem upewnij się, że nie jesteś obserwowany. Kliknij "*Pokaż frazę odzyskiwania*", aby wyświetlić ją na ekranie.


![LIQUID GREEN](assets/fr/16.webp)


**Mnemonic zapewnia pełny, nieograniczony dostęp do wszystkich bitcoinów **Każdy posiadacz Mnemonic może ukraść Twoje środki, nawet bez fizycznego dostępu do telefonu.


Przywraca ona dostęp do bitcoinów w przypadku utraty, kradzieży lub uszkodzenia telefonu. Dlatego bardzo ważne jest, aby starannie wykonać kopię zapasową **na nośniku fizycznym (nie cyfrowym)** i przechowywać ją w bezpiecznym miejscu. Możesz zapisać ją na kartce papieru lub dla dodatkowego bezpieczeństwa, jeśli jest to duży Wallet, zalecam wygrawerowanie go na wsporniku ze stali nierdzewnej, aby chronić go przed ryzykiem pożaru, powodzi lub zawalenia (w przypadku Hot Wallet zaprojektowanego do zabezpieczenia niewielkiej ilości bitcoinów, zwykła kopia zapasowa na papierze jest prawdopodobnie wystarczająca).


*Oczywiście nigdy nie wolno dzielić się tymi słowami w Internecie, tak jak robię to w tym samouczku. Ten przykładowy Wallet będzie używany tylko na Liquid's Testnet i zostanie usunięty po zakończeniu samouczka


![LIQUID GREEN](assets/fr/17.webp)


Po prawidłowym nagraniu frazy Mnemonic na nośniku fizycznym, kliknij "*Kontynuuj*". Green Wallet poprosi o potwierdzenie niektórych słów w frazie Mnemonic, aby upewnić się, że zostały one poprawnie nagrane. Wypełnij puste miejsca brakującymi słowami.


![LIQUID GREEN](assets/fr/18.webp)


Wybierz kod PIN urządzenia, który zostanie użyty do odblokowania Green Wallet. Jest to zabezpieczenie przed nieautoryzowanym dostępem fizycznym. Ten kod PIN nie bierze udziału w tworzeniu kluczy kryptograficznych Wallet. Tak więc, nawet bez dostępu do tego kodu PIN, posiadanie 12- lub 24-wyrazowej frazy Mnemonic umożliwi odzyskanie dostępu do bitcoinów.


Zalecamy wybranie możliwie losowego 6-cyfrowego kodu PIN. Pamiętaj, aby zapisać ten kod, aby go nie zapomnieć, w przeciwnym razie będziesz zmuszony do odzyskania Wallet z Mnemonic. Następnie możesz dodać opcję blokowania biometrycznego, aby uniknąć konieczności wprowadzania kodu PIN za każdym razem, gdy go używasz. Ogólnie rzecz biorąc, dane biometryczne są znacznie mniej bezpieczne niż sam kod PIN. Dlatego domyślnie radzę nie ustawiać tej opcji odblokowywania.


![LIQUID GREEN](assets/fr/19.webp)


Wprowadź kod PIN po raz drugi, aby go potwierdzić.


![LIQUID GREEN](assets/fr/20.webp)


Poczekaj na utworzenie Wallet, a następnie kliknij przycisk "*Utwórz konto*".


![LIQUID GREEN](assets/fr/21.webp)


W polu "*Active*" wybierz "*Liquid Bitcoin*". Następnie możesz wybrać między standardowym Wallet z pojedynczym podpisem, którego użyjemy w tym samouczku, a Wallet chronionym uwierzytelnianiem dwuskładnikowym (2FA).


![LIQUID GREEN](assets/fr/22.webp)


I to wszystko, twój Liquid Wallet został utworzony przy użyciu aplikacji Green!


![LIQUID GREEN](assets/fr/23.webp)


Przed otrzymaniem pierwszych bitcoinów na Liquid Wallet, **Zalecam wykonanie pustego testu odzyskiwania**. Zanotuj informacje referencyjne, takie jak xpub lub pierwszy otrzymany Address, a następnie usuń Wallet w aplikacji Green, gdy jest jeszcze pusty. Następnie spróbuj przywrócić Wallet na Green przy użyciu papierowych kopii zapasowych. Sprawdź, czy informacje o plikach cookie wygenerowane po przywróceniu są zgodne z pierwotnie zapisanymi. Jeśli tak, możesz mieć pewność, że papierowe kopie zapasowe są niezawodne. Aby dowiedzieć się więcej o tym, jak przeprowadzić odzyskiwanie testowe, zapoznaj się z tym innym samouczkiem:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Konfiguracja Liquid Wallet


Jeśli chcesz spersonalizować Wallet, kliknij trzy małe kropki w prawym górnym rogu.


![LIQUID GREEN](assets/fr/24.webp)


Opcja "*Rename*" pozwala dostosować nazwę Wallet, co jest szczególnie przydatne w przypadku zarządzania kilkoma portfelami w tej samej aplikacji.


![LIQUID GREEN](assets/fr/25.webp)


Menu "*Unit*" umożliwia zmianę jednostki bazowej Wallet. Można na przykład wybrać wyświetlanie w satoshis zamiast w bitcoinach.


![LIQUID GREEN](assets/fr/26.webp)


Menu "*Ustawienia*" zapewnia dostęp do różnych opcji urządzenia Bitcoin Wallet.


![LIQUID GREEN](assets/fr/27.webp)


Tutaj na przykład znajduje się *deskryptor*, który może się przydać, jeśli planujesz skonfigurować Watch-only wallet z tego Liquid Wallet.


![LIQUID GREEN](assets/fr/28.webp)


Można również zmienić kod PIN Wallet i aktywować połączenie biometryczne.


![LIQUID GREEN](assets/fr/29.webp)


## Korzystanie z Liquid Wallet


Teraz, gdy twój Liquid Wallet jest już skonfigurowany, możesz odebrać swój pierwszy L-Sats!


Jeśli nie masz jeszcze L-BTC, masz kilka opcji. Pierwszą z nich jest przesłanie ich bezpośrednio do ciebie. Jeśli ktoś chce zapłacić ci bitcoinami na Liquid, po prostu daj mu Address. Inną opcją jest Exchange bitcoinów onchain lub Lightning Network dla L-BTC. Aby to zrobić, możesz użyć [mostu takiego jak Boltz](https://boltz.Exchange/). Wystarczy wprowadzić Liquid Address na stronie, a następnie dokonać płatności za pośrednictwem Lightning Network lub onchain.


![LIQUID GREEN](assets/fr/30.webp)


Aby użyć generate a Liquid Address, kliknij przycisk "*Odbierz*".


![LIQUID GREEN](assets/fr/31.webp)


Green wyświetli pierwszy pusty odbierający Address w Wallet. Możesz zeskanować powiązany kod QR lub skopiować Address bezpośrednio, aby wysłać L-BTC.


![LIQUID GREEN](assets/fr/32.webp)


Gdy transakcja zostanie wyemitowana w sieci, pojawi się w Wallet.


![LIQUID GREEN](assets/fr/33.webp)


Poczekaj, aż otrzymasz wystarczającą liczbę potwierdzeń, aby uznać transakcję za ostateczną. W Liquid potwierdzenia powinny być szybkie, ponieważ blok jest publikowany co minutę.


![LIQUID GREEN](assets/fr/34.webp)


Dzięki L-Sats w Liquid Wallet można je teraz również wysyłać. Kliknij "*Wyślij*".


![LIQUID GREEN](assets/fr/35.webp)


Na następnej stronie wprowadź numer Liquid Address odbiorcy. Możesz wprowadzić go ręcznie lub zeskanować jego kod QR.


![LIQUID GREEN](assets/fr/36.webp)


Wybierz kwotę płatności.


![LIQUID GREEN](assets/fr/37.webp)


Kliknij "*Next*", aby przejść do ekranu podsumowania transakcji. Sprawdź, czy Address, kwota i opłaty są prawidłowe.


![LIQUID GREEN](assets/fr/38.webp)


Jeśli wszystko pójdzie dobrze, przesuń przycisk Green u dołu ekranu w prawo, aby podpisać i rozgłosić transakcję w sieci Bitcoin.


![LIQUID GREEN](assets/fr/39.webp)


Transakcja pojawi się teraz na pulpicie nawigacyjnym Bitcoin Wallet w oczekiwaniu na potwierdzenie.


![LIQUID GREEN](assets/fr/40.webp)


A teraz wiesz, jak łatwo korzystać z Liquid Sidechain z aplikacją Blockstream Green!


Jeśli ten poradnik okazał się przydatny, będę wdzięczny za pozostawienie poniżej kciuka Green. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dziękuję bardzo!


Polecam również zapoznanie się z innym obszernym samouczkiem na temat aplikacji mobilnej Blockstream Green, aby skonfigurować onchain Bitcoin Hot Wallet :


https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143
