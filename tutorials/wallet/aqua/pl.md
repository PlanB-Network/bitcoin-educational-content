---
name: Aqua
description: Bitcoin, Lightning i Liquid w pojedynczym Wallet
---
![cover](assets/cover.webp)


Aqua to aplikacja mobilna, która ułatwia tworzenie Hot Wallet dla Bitcoin i Liquid, a także oferuje możliwość korzystania z Lightning bez złożoności zarządzania węzłem, dzięki zintegrowanym swapom. Umożliwia również zarządzanie stablecoinami USDT w różnych sieciach.


Opracowana przez firmę JAN3 pod kierownictwem Samsona Mow, aplikacja Aqua została początkowo zaprojektowana specjalnie na potrzeby użytkowników w Ameryce Łacińskiej, choć jest odpowiednia dla każdego użytkownika na całym świecie. Jest ona szczególnie interesująca dla początkujących i tych, którzy na co dzień korzystają z Bitcoin do swoich płatności.


W tym samouczku dowiemy się, jak korzystać z wielu funkcji Aqua. Ale zanim to zrobimy, poświęćmy chwilę na zrozumienie, czym jest Sidechain w Bitcoin i jak działa Liquid, abyśmy mogli w pełni zrozumieć wartość Aqua.


![AQUA](assets/fr/01.webp)


## Co to jest Sidechain?


Protokół Bitcoin ma celowe ograniczenia techniczne, które pomagają utrzymać decentralizację sieci i zapewnić bezpieczeństwo wszystkim użytkownikom. Ograniczenia te mogą jednak czasami frustrować użytkowników, szczególnie podczas przeciążenia spowodowanego dużą liczbą jednoczesnych transakcji. Debata na temat skalowalności Bitcoin od dawna dzieli społeczność, szczególnie podczas wojny o rozmiar bloków. Od tego czasu w społeczności Bitcoin powszechnie uznaje się, że skalowalność musi być zapewniona przez rozwiązania off-chain w systemach drugiej Layer. Rozwiązania te obejmują łańcuchy boczne, które są nadal stosunkowo nieznane i mało używane w porównaniu z innymi systemami, takimi jak Lightning Network.


Sidechain to niezależny Blockchain, który działa równolegle z głównym Bitcoin Blockchain. Wykorzystuje Bitcoin jako jednostkę rozliczeniową, dzięki mechanizmowi zwanemu "*two-way peg*". System ten umożliwia zablokowanie bitcoinów w głównym łańcuchu w celu odtworzenia ich wartości na Sidechain, gdzie krążą one w formie tokenów zabezpieczonych oryginalnymi bitcoinami. Tokeny te zwykle zachowują parytet wartości z bitcoinami zablokowanymi na głównym łańcuchu, a proces ten można odwrócić w celu odzyskania środków na Bitcoin.


Celem łańcuchów bocznych jest oferowanie dodatkowych funkcji lub ulepszeń technicznych, takich jak szybsze transakcje, niższe opłaty lub obsługa inteligentnych kontraktów. Innowacje te nie zawsze mogą być wdrożone bezpośrednio na Bitcoin Blockchain bez uszczerbku dla jego decentralizacji lub bezpieczeństwa. Łańcuchy boczne umożliwiają zatem testowanie i badanie nowych rozwiązań przy jednoczesnym zachowaniu integralności Bitcoin. Protokoły te często wymagają jednak kompromisów, szczególnie w zakresie decentralizacji i bezpieczeństwa, w zależności od wybranego modelu zarządzania i mechanizmu konsensusu.


## Co to jest Liquid?


Liquid to sfederowana nakładka Sidechain na Bitcoin, opracowana przez Blockstream w celu poprawy szybkości transakcji, poufności i funkcjonalności. Wykorzystuje dwustronny mechanizm kotwiczenia ustanowiony w federacji w celu blokowania bitcoinów w głównym łańcuchu i tworzenia w zamian bitcoinów Liquid (L-BTC), tokenów krążących na Liquid, pozostając wspieranymi przez oryginalne bitcoiny.


![AQUA](assets/fr/02.webp)


Liquid Network opiera się na federacji uczestników, złożonej z uznanych podmiotów z ekosystemu Bitcoin, którzy walidują bloki i zarządzają dwustronnym peggingiem. Oprócz L-BTC, Liquid umożliwia również emisję innych aktywów cyfrowych, takich jak stablecoin USDT i inne kryptowaluty.


![AQUA](assets/fr/03.webp)


## Zainstaluj aplikację Aqua


Pierwszym krokiem jest oczywiście pobranie aplikacji Aqua. Przejdź do sklepu z aplikacjami:



- [Dla systemu Android](https://play.google.com/store/apps/details?id=io.aquawallet.android);
- [Dla Apple](https://apps.apple.com/us/app/Aqua-Wallet/id6468594241).

![AQUA](assets/fr/04.webp)


Użytkownicy Androida mają również możliwość zainstalowania aplikacji za pomocą pliku `.apk` [dostępnego na ich GitHub] (https://github.com/AquaWallet/Aqua-Wallet/releases).


![AQUA](assets/fr/05.webp)


Uruchom aplikację, a następnie zaznacz pole "*Przeczytałem i akceptuję Warunki korzystania z usługi i Politykę prywatności*".


![AQUA](assets/fr/06.webp)


## Utwórz swój Wallet na Aqua


Kliknij przycisk "*Twórz Wallet*".


![AQUA](assets/fr/07.webp)


I voila, twój Wallet jest już utworzony!


![AQUA](assets/fr/08.webp)


Przede wszystkim jednak, ponieważ jest to Wallet do samodzielnego przechowywania, konieczne jest wykonanie fizycznej kopii zapasowej Mnemonic. **Ten Mnemonic daje ci pełny, nieograniczony dostęp do wszystkich twoich bitcoinów**. Każdy, kto jest w posiadaniu tego Mnemonic, może ukraść twoje środki, nawet bez fizycznego dostępu do twojego telefonu.


Umożliwia on przywrócenie dostępu do bitcoinów w przypadku utraty, kradzieży lub uszkodzenia telefonu. Dlatego bardzo ważne jest, aby zapisać go ostrożnie na nośniku fizycznym (nie cyfrowym) i przechowywać w bezpiecznym miejscu. Możesz zapisać go na kartce papieru lub dla dodatkowego bezpieczeństwa, jeśli jest to duży Wallet, zalecałbym wygrawerowanie go na wsporniku ze stali nierdzewnej, aby chronić go przed ryzykiem pożaru, powodzi lub zawalenia (w przypadku Hot Wallet zaprojektowanego do zabezpieczenia niewielkiej ilości bitcoinów, prawdopodobnie wystarczy zwykła kopia zapasowa na papierze).


Aby to zrobić, kliknij menu Ustawienia.


![AQUA](assets/fr/09.webp)


Następnie kliknij "*View seed Phrase*". Utwórz fizyczną kopię zapasową tej 12-wyrazowej frazy.


![AQUA](assets/fr/10.webp)


W tym samym menu ustawień można również zmienić język aplikacji i używaną walutę fiducjarną.


![AQUA](assets/fr/11.webp)


Przed otrzymaniem pierwszych bitcoinów w Wallet, **Zalecam wykonanie testu odzyskiwania pustego konta**. Zanotuj informacje referencyjne, takie jak xpub lub pierwszy otrzymany Address, a następnie usuń Wallet w aplikacji Aqua, gdy jest jeszcze pusty. Następnie spróbuj przywrócić Wallet na Aqua przy użyciu papierowych kopii zapasowych. Sprawdź, czy informacje o plikach cookie wygenerowane po przywróceniu są zgodne z pierwotnie zapisanymi. Jeśli tak, możesz mieć pewność, że papierowe kopie zapasowe są niezawodne. Aby dowiedzieć się więcej o tym, jak przeprowadzić testowe odzyskiwanie, zapoznaj się z tym samouczkiem:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Nie widać tego na moim ekranie, ponieważ używam emulatora, ale w ustawieniach znajdziesz opcję zablokowania aplikacji za pomocą systemu uwierzytelniania biometrycznego. Zdecydowanie zalecam włączenie tej funkcji bezpieczeństwa, ponieważ bez niej każdy, kto ma dostęp do odblokowanego telefonu, może ukraść twoje bitcoiny. Możesz użyć Face ID na iOS lub odcisku palca na Androidzie. Jeśli te metody zawiodą podczas uwierzytelniania, nadal możesz uzyskać dostęp do aplikacji za pomocą kodu PIN telefonu.


## Odbieranie bitcoinów na Aqua


Po skonfigurowaniu Wallet możesz odebrać swój pierwszy Sats! Wystarczy kliknąć przycisk "*Odbierz*" w menu "*Wallet*".


![AQUA](assets/fr/12.webp)


Możesz wybrać otrzymywanie bitcoinów w łańcuchu, na Liquid lub za pośrednictwem Lightning.


![AQUA](assets/fr/13.webp)


W przypadku transakcji onchain, Aqua będzie generate określonym odbierającym Address, w którym można odebrać Sats.


![AQUA](assets/fr/14.webp)


Podobnie, wybierając Liquid, Aqua zapewni ci Liquid Address.


![AQUA](assets/fr/15.webp)


Jeśli wolisz otrzymywać środki za pośrednictwem usługi Lightning, musisz najpierw określić żądaną kwotę.


![AQUA](assets/fr/16.webp)


Następnie kliknij "*generate Invoice*".


![AQUA](assets/fr/17.webp)


Aqua utworzy Invoice, aby otrzymywać środki z Lightning Wallet. Należy pamiętać, że w przeciwieństwie do opcji onchain i Liquid, środki otrzymane za pośrednictwem Lightning zostaną automatycznie przekonwertowane na L-BTC na Liquid za pomocą narzędzia Boltz, ponieważ Aqua nie jest węzłem Lightning. Proces ten umożliwia otrzymywanie i wysyłanie środków za pośrednictwem Lightning, ale bez przechowywania bitcoinów na Lightning.


![AQUA](assets/fr/18.webp)


Osobiście zamierzam zacząć od wysłania bitcoinów przez Lightning do Aqua. Po zakończeniu transakcji z podanym Invoice otrzymujemy potwierdzenie.


![AQUA](assets/fr/19.webp)


Aby śledzić postęp wymiany, wróć do strony głównej Wallet i kliknij konto "*L2 Bitcoin*", które zawiera listę transakcji Lightning (poprzez wymianę) i Liquid.


![AQUA](assets/fr/20.webp)


Tutaj możesz zobaczyć swoje transakcje i saldo L-BTC.


![AQUA](assets/fr/21.webp)


## Zamiana Bitcoin na Aqua


Teraz, gdy masz już aktywa w Aqua Wallet, możesz je wymienić bezpośrednio z aplikacji, aby przenieść je do głównego Bitcoin Blockchain lub Liquid. Możesz również zamienić swoje bitcoiny na stablecoiny USDT (lub inne). Aby to zrobić, przejdź do menu "*Marketplace*".


![AQUA](assets/fr/22.webp)


Kliknij na "*Swaps*".


![AQUA](assets/fr/23.webp)


W polu "*Transfer from*" wybierz aktywa, którymi chcesz handlować. Obecnie posiadam tylko L-BTC, więc to właśnie wybieram.


![AQUA](assets/fr/24.webp)


W polu "*Transfer to*" wybierz aktywa docelowe dla swojej zamiany. Ze swojej strony wybrałem USDT na Liquid Network.


![AQUA](assets/fr/25.webp)


Wprowadź kwotę, którą chcesz przeliczyć.


![AQUA](assets/fr/26.webp)


Potwierdź, klikając "*Kontynuuj*".


![AQUA](assets/fr/27.webp)


Upewnij się, że jesteś zadowolony z ustawień zamiany, a następnie potwierdź, przeciągając przycisk "*Zamiana*" u dołu ekranu.


![AQUA](assets/fr/28.webp)


Twoja zamiana została potwierdzona.


![AQUA](assets/fr/29.webp)


Patrząc wstecz na nasz Wallet, widzimy, że mamy teraz USDT na Liquid.


![AQUA](assets/fr/30.webp)


## Wysyłanie bitcoinów za pomocą Aqua


Teraz, gdy masz bitcoiny w Aqua Wallet, możesz je wysłać. Kliknij przycisk "*Wyślij*".


![AQUA](assets/fr/31.webp)


Wybierz aktywa, które chcesz wysłać lub wybierz sieć do przeprowadzenia transakcji. Ze swojej strony zamierzam wysłać bitcoiny za pośrednictwem Lightning.


![AQUA](assets/fr/32.webp)


Następnie wprowadź informacje potrzebne do wysłania płatności: w przypadku bitcoinów onchain lub Liquid musisz wprowadzić odbierający Address; w przypadku Lightning wymagany jest Invoice. Informacje te można wkleić bezpośrednio w odpowiednie pole lub użyć ikony kodu QR, aby otworzyć aparat i zeskanować Address lub Invoice. Następnie kliknij "*Kontynuuj*".


![AQUA](assets/fr/33.webp)


Kliknij "*Kontynuuj*" ponownie, jeśli wszystkie informacje wydają się prawidłowe.


![AQUA](assets/fr/34.webp)


Następnie Aqua wyświetli podsumowanie transakcji. Upewnij się, że wszystkie informacje są prawidłowe, w tym miejsce docelowe Address, opłaty i kwota. Aby potwierdzić transakcję, przesuń przycisk "*Przesuń, aby wysłać*" znajdujący się w dolnej części ekranu.


![AQUA](assets/fr/35.webp)


Następnie otrzymasz potwierdzenie wysyłki.


![AQUA](assets/fr/36.webp)


Teraz już wiesz, jak korzystać z aplikacji Aqua, aby otrzymywać i wydawać środki na Bitcoin, Lightning i Liquid, a wszystko to z jednego Interface.


Jeśli uznałeś ten poradnik za przydatny, będę wdzięczny za pozostawienie kciuka Green poniżej. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dziękuję bardzo!


Polecam również zapoznanie się z tym obszernym samouczkiem na temat aplikacji mobilnej Blockstream Green, która jest kolejnym interesującym rozwiązaniem do konfiguracji Liquid Wallet:


https://planb.network/tutorials/wallet/mobile/blockstream-green-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a