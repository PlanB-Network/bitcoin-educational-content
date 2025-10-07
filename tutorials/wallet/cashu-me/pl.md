---
name: Cashu.me
description: Przewodnik Cashu.me dotyczący korzystania z ecash
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=LIPw1c74LBU)


*Oto samouczek wideo od BTC Sessions, który przeprowadzi Cię przez proces konfiguracji i korzystania z Cashu.me Bitcoin Wallet, który zapewnia dostęp do prostych, tanich i prywatnych transakcji Bitcoin - bez potrzeby korzystania ze sklepu z aplikacjami!


W tym samouczku poznamy Cashu.me, oparty na przeglądarce Wallet do prywatnych płatności Bitcoin przy użyciu Chaumian ecash. Zanim zagłębimy się w temat, zróbmy krótkie wprowadzenie do ecash i jego działania.


## Wprowadzenie do ecash


Wyobraź sobie cyfrową gotówkę, która działa dokładnie tak, jak fizyczne banknoty w Twojej kieszeni - prywatna, natychmiastowa i użyteczna peer-to-peer bez pośredników. To właśnie umożliwia ecash: cyfrowe podejście do płatności, które przywraca prywatność fizycznej gotówki do cyfrowego świata. W przeciwieństwie do onchain-Bitcoin, który rejestruje każdą transakcję na publicznym Ledger widocznym dla każdego, ecash tworzy prywatne tokeny, które reprezentują rzeczywistą wartość Bitcoin, jednocześnie zachowując poufność nawyków związanych z wydatkami.


Potraktuj ecash jako cyfrowe instrumenty na okaziciela przechowywane na Twoim urządzeniu - jeśli je posiadasz, jesteś ich właścicielem, tak jak w przypadku fizycznej gotówki. Tokeny te są wydawane przez zaufane usługi zwane `Mints`, które przechowują bazowe rezerwy Bitcoin. Kiedy używasz ecash, nie transmitujesz swoich transakcji do całej sieci. Zamiast tego wymieniasz prywatne tokeny bezpośrednio z innymi, tworząc doświadczenie płatnicze, które bardziej przypomina wręczanie komuś gotówki niż dokonywanie tradycyjnej płatności cyfrowej.


Cashu to darmowy i open-source'owy protokół Chaumian ecash zbudowany dla Bitcoin. Technologia ta opiera się na pionierskich badaniach kryptograficznych Davida Chauma z lat 80-tych, wykorzystując "ślepe podpisy" w celu zapewnienia prywatności. Kiedy otrzymujesz tokeny ecash, mennica podpisuje je, nie wiedząc, gdzie zostaną wydane - jest to kluczowa funkcja, która zapobiega śledzeniu transakcji. Co ważne, ecash nie zastępuje Bitcoin; uzupełnia go, rozwiązując niektóre krytyczne kwestie związane z wymaganiami architektury Bitcoin. Zapewnia prywatność oferowaną przez fizyczną gotówkę (której brakuje przezroczystemu Ledger Bitcoin) i umożliwia natychmiastowe mikrotransakcje bez opłat Blockchain lub opóźnień w potwierdzeniu.


Ecash płynnie integruje się z Lightning Network. Używasz Lightning do wpłacania Bitcoin do mennicy (konwertując wartość Bitcoin na tokeny ecash) i do późniejszej wypłaty (konwertując tokeny z powrotem na saldo Lightning do wydania). Razem tworzą potężną kombinację: Bitcoin zapewnia bezpieczne rozliczenie Layer, Lightning umożliwia szybkie transakcje i interoperacyjność sieci, a ecash dodaje prywatność Layer, która sprawia, że płatności cyfrowe znów stają się naprawdę prywatne.


## Cashu.me


Cashu.me to `Progressive Web App (PWA)`, która implementuje protokół Cashu - specyficzną implementację Chaumian ecash zaprojektowaną dla Bitcoin. Jako PWA, działa bezpośrednio w przeglądarce, nie wymagając instalacji ze sklepów z aplikacjami, choć można ją "zainstalować" na urządzeniu dla łatwiejszego dostępu. To internetowe podejście zapewnia szeroką kompatybilność między systemami operacyjnymi, przy jednoczesnym zachowaniu bezpieczeństwa dzięki protokołom kryptograficznym, a nie ograniczeniom platformy.


## kluczowe cechy


Zapoznajmy się z funkcjami i odkryjmy, co Cashu.me ma do zaoferowania:



- Chaumian ecash na Lightning**: Używa ślepych podpisów, więc mennice nie mogą śledzić sald użytkowników ani historii transakcji
- Samodzielna kontrola tokenów**: Kontrolujesz tokeny ecash lokalnie za pomocą frazy seed
- Kopie zapasowe frazy seed**: 12-wyrazowa fraza odzyskiwania dla przywracania Wallet
- Niezależność od mennicy**: Współpracuje z wieloma niezależnymi mennicami - nie jesteś uzależniony od jednego dostawcy
- Natychmiastowe, bezpłatne transakcje**: W tej samej mennicy płatności są finalizowane w ciągu kilku sekund bez żadnych opłat
- Architektura chroniąca prywatność**: Mennice nie widzą, kto z kim dokonuje transakcji
- Offline ecash**: Wysyłanie/odbieranie tokenów za pośrednictwem lokalnego protokołu transmisji, takiego jak NFC, kod QR, Bluetooth itp. bez połączenia z Internetem
- Odkryj mennice ecash za pośrednictwem Nostr**: Znajdź i zweryfikuj zaufane mennice za pomocą protokołu Nostr
- Wymieniaj ecash między mennicami**: Wszystkie mennice posługują się technologią Lightning, co oznacza, że można przesyłać wartość między nimi.
- Zdalne sterowanie Wallet za pomocą Nostr Wallet Connect (NWC)**: Połącz się z innymi aplikacjami, takimi jak Nostr Client i rozpocznij zapping za pomocą NWC


Krytycznym kompromisem jest "zaufanie": podczas gdy kontrolujesz same tokeny, musisz zaufać mennicom, że będą przechowywać podstawowe rezerwy Bitcoin. Jak stwierdza dokumentacja Cashu:


> ...mennica zarządza infrastrukturą Lightning i przechowuje satoshis dla użytkowników ecash mennicy. Użytkownicy muszą zaufać mennicy, że Redeem ich ecash, gdy chcą zamienić na Lightning.

- Dokumentacja Cashu, [Ogólne pytania dotyczące bezpieczeństwa i prywatności](https://docs.cashu.space/faq#general-safety-and-privacy-questions)


To sprawia, że ecash jest rozwiązaniem powierniczym dla samego Bitcoin, choć użytkownik zachowuje pełną kontrolę nad tokenami.


## 1️⃣ Konfiguracja początkowa


① Rozpocznij od odwiedzenia strony [Wallet.cashu.me](https://Wallet.cashu.me) w przeglądarce. Ponieważ Cashu.me to `PWA`, nie musisz pobierać go ze sklepów z aplikacjami, po prostu otwórz witrynę bezpośrednio w przeglądarce. Aby uzyskać łatwiejszy dostęp, można opcjonalnie zainstalować ją na ekranie głównym urządzenia.


② Aby zainstalować PWA, dotknij przycisku menu ⋮ w przeglądarce i wybierz "Dodaj do ekranu głównego". Po zainstalowaniu zamknij kartę przeglądarki i uruchom Cashu.me z ekranu głównego urządzenia. Na ekranie powitalnym dotknij `Next`, aby kontynuować.


③ Bezpieczeństwo ma kluczowe znaczenie. Przechowuj swoją frazę seed bezpiecznie w menedżerze haseł lub, jeszcze lepiej, zapisz ją na papierze. Ta 12-wyrazowa fraza odzyskiwania to jedyny sposób na odzyskanie środków w przypadku utraty dostępu do urządzenia. Stuknij ikonę 👁️, aby wyświetlić swoją frazę seed, starannie zapisz wszystkie 12 słów w kolejności, a następnie zaznacz pole oznaczone `Zapisałem`. Dotknij "Dalej", aby kontynuować, i zaznacz pole, aby potwierdzić akceptację "warunków" na następnym ekranie.


![image](assets/en/01.webp)


Po zakończeniu konfiguracji musisz połączyć się z `Mint`. Stuknij w `ADD MINT`, a następnie `DISCOVER MINTS`, aby wyświetlić mennice polecane przez społeczność Nostr. Aby uzyskać dodatkową weryfikację, możesz przejrzeć oceny mennic na stronie [bitcoinmints.com](bitcoinmints.com).


Następnie stuknij w `Click to browse mints`, aby zobaczyć pełną listę. Wybierz miętę, kopiując jej adres URL, wklejając go w polu adresu URL i nadając mu rozpoznawalną nazwę. W tym przykładzie użyjemy:


URL: `https://mint.minibits.cash/Bitcoin`

Nazwa: `Minibits`


![image](assets/en/02.webp)


Stuknij `ADD MINT`, aby zakończyć proces. Na ekranie potwierdzenia sprawdź, czy ufasz operatorowi tego minta, a następnie ponownie dotknij `ADD MINT`. Minibits mint pojawi się teraz na ekranie głównym. Po skonfigurowaniu Wallet należy go zasilić przed dokonaniem transakcji.


![image](assets/en/03.webp)


## 2️⃣ Finansowanie Wallet


Cashu.me oferuje dwie różne metody finansowania Wallet. Po dotknięciu opcji `Odbierz` na ekranie głównym, zobaczysz opcje otrzymania środków za pomocą `ECASH` lub `LIGHTNING.` Przyjrzyjmy się obu opcjom.


![image](assets/en/04.webp)


### Finansowanie przez LIGHTNING


Pierwszą opcją jest zasilenie Wallet poprzez Lightning Invoice. wybierz mennicę, jeśli dodałeś różne mennice i zdefiniuj kwotę (Sats)`, którą chcesz otrzymać. Następnie stuknij w "UTWÓRZ Invoice". Teraz wyświetli się kod QR, który możesz zeskanować za pomocą innego Wallet lub po prostu "SKOPIOWAĆ" Invoice i wkleić do innego Wallet, aby zapłacić i zasilić swój cashu.me Wallet.


![image](assets/en/05.webp)


### Otrzymywanie ecash


Metoda ecash umożliwia otrzymywanie tokenów bezpośrednio od innego gracza ecash Wallet. Zacznij od dotknięcia przycisku `Odbierz` i wybrania opcji `ECASH`. Będziesz mógł `Wkleić`, `Skanować` lub użyć `NFC`, aby przesłać Cashu token z innego Wallet. Jeśli zdecydujesz się wkleić, wprowadź ciąg token, który skopiowałeś z innego Wallet, `Amount` i `Mint` zostaną automatycznie wyświetlone. Dotknij `RECEIVE`, aby zakończyć transakcję, a Sats pojawi się w Twoim Wallet. Zauważ, że saldo jest teraz rozłożone na wiele mennic. Na przykład, możesz mieć 1,000 Sats w Minibits `Mint` i dodatkowe 1,000 Sats w Coinos `Mint`. Ta separacja między różnymi mennicami jest ważnym aspektem architektury Cashu.


![image](assets/en/06.webp)


### Zamiana między miętówkami


Jeśli nie ufasz już konkretnej mennicy, którą dodałeś, cashu.me oferuje funkcję `Zamiany` środków z jednej mennicy na inną. Przejdź do zakładki mennic i przewiń w dół, aż zobaczysz `Multimint Swaps`. Wybierz mennicę `FROM` i `TO` z rozwijanego menu i wprowadź kwotę, którą chcesz przelać. Naciśnij `SWAP`, aby przenieść tokeny między mennicami. Zostanie to wykonane za pośrednictwem transakcji Lightning, więc musisz zostawić miejsce na potencjalne opłaty Lightning. W moim przykładzie wystarczył 1 sat.


![image](assets/en/07.webp)


## 3️⃣ Wysyłanie środków


Aby wysłać Sats, Cashu.me oferuje dwie opcje. Aby wysłać przez `ecash` lub przez `lightning`. Przyjrzyjmy się obu opcjom.


### Wysyłanie przez Lightning


Aby wysłać wiadomość przez Lightning, wykonaj następujące kroki:


1. Stuknij w `WYŚLIJ` na ekranie głównym i wybierz `Piorun`

2. Aplikacja poprosi o wprowadzenie `Lightning Invoice` lub `-Address`. Możesz wkleić Invoice/Address bezpośrednio lub użyć opcji skanowania kodu QR, aby przechwycić go wizualnie, a następnie potwierdzić przyciskiem `ENTER`

3. Wybierz Mint, z którego chcesz zapłacić, korzystając z pola rozwijanego i dotknij `PŁACĘ`, aby potwierdzić. **Uwaga**: istnieje również opcja użycia `Multinut` w `Ustawieniach` -> `Eksperymentalne`, która pozwala na płacenie faktur z wielu mennic jednocześnie.

4. Po pomyślnym zakończeniu zobaczysz potwierdzenie płatności i kwotę odliczoną od salda.


![image](assets/en/08.webp)


### Wysyłanie przez ecash


Wysyłanie ecash jest równie proste.


1. Stuknij w "WYŚLIJ" i tym razem wybierz opcję "PIENIĄDZE".

2. `Wybierz mennicę` i wprowadź `Kwotę`, którą chcesz wysłać w Sats i dotknij `WYŚLIJ`, aby potwierdzić

3. Tworzy to `Animowany kod QR`, który można dostosować, dostosowując parametry prędkości i rozmiaru. Każdy może zeskanować ten kod QR do Redeem Sats natychmiast, lub można dotknąć KOPIUJ, aby wysłać ciąg token do kogoś innego za pośrednictwem alternatywnych kanałów, takich jak Bluetooth, NFC lub standardowe wiadomości.

4. Otwieram kolejny Wallet. Wklejam ze schowka i wybieram `Odbierz ecash` w drugim Wallet.


![image](assets/en/09.webp)


## 4️⃣ Dodatkowe funkcje


Poza podstawowymi funkcjami wysyłania i odbierania, Cashu.me oferuje potężne dodatkowe funkcje, które zwiększają komfort korzystania z Bitcoin w ekosystemie Nostr.


### Nostr Wallet Connect


Nostr Wallet Connect (`NWC`) zmienia sposób interakcji z aplikacjami Nostr, tworząc płynne połączenie między Wallet a aplikacjami społecznościowymi. Protokół ten umożliwia aplikacjom takim jak [Damus](https://damus.io/) lub [Primal](https://primal.net/home) żądanie płatności bezpośrednio przez przekaźniki Nostr bez konieczności opuszczania aplikacji.


Aby skonfigurować `NWC` w Cashu.me:


1. Przejdź do `Ustawienia` w lewym górnym menu hamburgera

2. Przewiń do sekcji `NOSTR Wallet CONNECT` i dotknij przycisku `Enable`

3. Następnie ustawisz dodatek, aby ustalić maksymalną kwotę, jaką aplikacje mogą wydać z Wallet.

4. Po skonfigurowaniu można skopiować ciąg połączenia i wkleić go do dowolnego klienta Nostr, który obsługuje `NWC`, umożliwiając natychmiastową funkcję zappingu i tippingu.


![image](assets/en/10.webp)


### Lightning Address via npub.cash


Cashu.me integruje się z [npub.cash](https://npub.cash/), aby zapewnić ci Lightning Address, który działa płynnie z protokołem Nostr. Tutaj możesz zarejestrować się i odebrać swoją nazwę użytkownika, podając swój Nostr `nsec`, który kosztuje 5000 Sats i wspiera projekt npub.cash, lub możesz użyć dowolnego klucza publicznego Nostr (`npub`) bez rejestracji.


Najpierw przejdź do `Ustawień` i dotknij `Włącz` Lightning Address z npub.cash. Spowoduje to generate npub.cash Address przy użyciu ciągu `npub` pochodzącego domyślnie z frazy Wallet seed.


Alternatywnie, odwiedź [tę stronę](https://npub.cash/username), aby ubiegać się o niestandardową nazwę użytkownika przy użyciu własnego Nostr `nsec`, co da ci spersonalizowany Lightning Address, taki jak username@npub.cash.


![image](assets/en/11.webp)


## wnioski


Cashu.me zapewnia prywatne płatności Bitcoin, które działają jak fizyczna gotówka - natychmiastowo i peer-to-peer bez ujawniania historii transakcji. Osobiście doceniam architekturę PWA, ponieważ działa ona bez ograniczeń sklepu z aplikacjami. Łącząc bezpieczeństwo Bitcoin, szybkość Lightning i prywatność ecash, Wallet oferuje przypadki użycia, które mogą zwiększyć codzienną adopcję Bitcoin.


Chociaż masz pełną kontrolę nad swoimi tokenami ecash poprzez samodzielne przechowywanie, pamiętaj, że mennice działają jako zaufane strony trzecie, które przechowują bazowe rezerwy Bitcoin. Możliwość korzystania z wielu mennic i wymiany między nimi zapewnia elastyczność przy jednoczesnym zachowaniu prywatności.


Dzięki funkcjom takim jak NWC i adresy npub.cash, Cashu.me jest atrakcyjną opcją Wallet dla klientów społecznościowych, którzy cenią sobie prywatność i suwerenność ponad ograniczenia polityki dużych technologii.


## zasoby


[https://github.com/cashubtc/cashu.me](https://github.com/cashubtc/cashu.me)


[https://github.com/cashubtc](https://github.com/cashubtc)


[https://github.com/cashubtc/awesome-cashu](https://github.com/cashubtc/awesome-cashu)


[https://cashu.space/](https://cashu.space/)