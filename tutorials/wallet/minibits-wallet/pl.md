---
name: Minibits Wallet
description: Przewodnik po Minibitach Wallet
---

![cover](assets/cover.webp)


W tym samouczku przeprowadzę cię przez konfigurację Minibits Wallet do korzystania z ecash. Jest to potężna technologia płatności skoncentrowana na prywatności, która współpracuje z Bitcoin. Minibits to ecash i Lightning Wallet, które umożliwiają natychmiastowe, tanie i prywatne transfery wartości, dzięki czemu idealnie nadają się do codziennych transakcji, w których prywatność ma znaczenie.


Zanim zagłębimy się w temat minibitów, wyjaśnijmy sobie, czym jest, a czym nie jest ecash. Wiele osób myli ecash z technologią Bitcoin lub Blockchain, ale są to zasadniczo różne koncepcje.


Ecash NIE jest Bitcoin. Nie zastępuje samowystarczalnego Bitcoin Wallet, ale raczej go uzupełnia. Ecash NIE jest Blockchain i NIE działa na żadnym publicznym Ledger. Co ciekawe, ecash NIE jest nową technologią - w rzeczywistości poprzedza światową sieć, z koncepcjami opracowanymi w latach 80. i 90. ubiegłego wieku.


Czym jest ecash: niezwykle prywatny (transakcje nie pozostawiają śladów), peer-to-peer (bezpośrednie transfery bez pośredników) i działa jako cyfrowy instrument na okaziciela (jeśli go posiadasz, kontrolujesz go). Kluczową zaletą jest to, że ecash MOŻE być używany offline - zarówno nadawca, jak i odbiorca mogą być odłączeni od Internetu podczas transakcji. Ecash MOŻE być bity przez pojedynczą stronę lub przez federację zaufanych podmiotów i JEST doskonałą technologią uzupełniającą Bitcoin, obsługującą małe, częste transakcje, podczas gdy Bitcoin służy jako Layer rozliczeniowy.


Należy pamiętać, że ta konfiguracja Minibits stanowi "rozwiązanie powiernicze", co oznacza, że powierzasz operatorowi Mint zarządzanie swoimi środkami. Wprowadza to określone ryzyko, które należy zrozumieć przed kontynuowaniem.


Projekt wyświetla to ważne zastrzeżenie:


- Ten Wallet powinien być używany wyłącznie do celów badawczych.
- Wallet to wersja beta z niekompletną funkcjonalnością oraz znanymi i nieznanymi błędami.
- Nie używaj go z dużymi kwotami ecash.
- Gotówka przechowywana w Wallet jest emitowana przez mennicę
- ufasz, że mennica zabezpieczy go Bitcoin, dopóki nie przeniesiesz swoich zasobów na inny Bitcoin z błyskawicą Wallet.
- Protokół Cashu, który implementuje Wallet, nie został jeszcze poddany szczegółowej ocenie ani testom.


Traktuj Minibity jak codzienne Wallet, a nie konto oszczędnościowe i nigdy nie przechowuj na nich znacznych wartości.


## 1️⃣ Konfiguracja Wallet


Aby rozpocząć, odwiedź [Minibits Website](https://www.minibits.cash/), gdzie znajdziesz opcje pobierania dla wszystkich głównych platform. Użytkownicy iOS mogą pobierać z [App Store](https://testflight.apple.com/join/defJQgTD), podczas gdy użytkownicy UE iOS mają dodatkową opcję instalacji z [Freedom Store](https://freedomstore.io/). Użytkownicy Androida mogą pobrać aplikację z [Google Play Store](https://play.google.com/store/apps/details?id=com.minibits_wallet) lub pobrać plik APK bezpośrednio ze strony [GitHub Releases](https://github.com/minibits-cash/minibits_wallet/releases).


Podczas instalacji Minibits wyświetlone zostaną ekrany wprowadzające, które wyjaśniają podstawowe pojęcia - możesz je przeczytać lub pominąć, jeśli jesteś już zaznajomiony z technologią. Po ukończeniu tych początkowych kroków zostaniesz poproszony o dokonanie wyboru:


- `Zrozumiałem, zabierz mnie do Wallet` dla nowych użytkowników lub
- `Odzyskaj utracone Wallet` w przypadku przywracania z kopii zapasowej.


![image](assets/en/01.webp)

Po zakończeniu wstępnej konfiguracji, użytkownik wyląduje na ekranie głównym, który zawiera kilka ważnych informacji Elements. ① Ikona profilu w górnym rogu prowadzi do strony profilu, gdzie można uzyskać dostęp do swoich Minibitów Wallet Address i wybrać opcje "odbioru wsadowego". ② W środkowej części ekranu wyświetlane są miętówki, których można używać, z domyślnie wybraną miętówką Minibits. ③ Wiersz akcji poniżej zawiera opcje wysyłania płatności ecash lub lightning, skanowania kodu QR i odbierania płatności. ④ Wreszcie, dolny pasek nawigacyjny zawiera skróty do ekranu głównego, historii transakcji, kontaktów i ustawień.


![image](assets/en/02.webp)


## 2️⃣ Zarządzaj miętówkami


Domyślnie mennica Minibits jest włączona po uruchomieniu aplikacji. Jednak jedną z mocnych stron ecash jest możliwość korzystania z wielu mennic w celu zwiększenia decentralizacji i bezpieczeństwa. Aby dodać kolejną mennicę, przejdź do `Ustawień`, następnie wybierz `Zarządzaj mennicami`, a na koniec dotknij `Dodaj mennicę`.


[Bitcoinmints.com](Bitcoinmints.com) zapewnia kompleksową listę dostępnych mennic wraz z ocenami użytkowników, aby pomóc w wyborze renomowanych opcji. Korzystanie z wielu mennic zmniejsza ryzyko. Jeśli jedna mennica doświadczy problemów, środki na innych mennicach pozostaną dostępne.


![image](assets/en/04.webp)


## 3️⃣ Tworzenie kopii zapasowej


Tworzenie kopii zapasowej jest prawdopodobnie najbardziej krytycznym krokiem w całym procesie konfiguracji. Aby uzyskać dostęp do opcji kopii zapasowej, przejdź do `Ustawienia`-> `Kopia zapasowa` Tutaj znajdziesz dwie istotne opcje:

1. `Twoja fraza seed` zawierająca `12 słów`, która pozwala odzyskać saldo ecash w przypadku utraty urządzenia. Ta fraza seed jest kluczem głównym do wszystkich ecash we wszystkich dodanych mennicach. Zapisz ją na nośniku fizycznym (papier lub metal) i przechowuj bezpiecznie w wielu lokalizacjach. Nigdy nie przechowuj swojej frazy seed w formie cyfrowej, gdzie mogłaby zostać naruszona. Rozważ odwiedzenie tego [samouczka](https://planb.network/en/tutorials/Wallet/backup/backup-Mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270), aby zapoznać się z najlepszymi praktykami dotyczącymi ochrony Wallet.

2. `Wallet backup`, który zawiera długi ciąg kopii zapasowej.


**Uwaga**: W przypadku korzystania z tej kopii zapasowej do odzyskania Wallet nadal będzie potrzebna fraza seed.


![image](assets/en/05.webp)


## 4️⃣ Tworzenie minibitów Wallet Address


Następnie przejdź do `Kontakty` na dole i dostosuj dedykowany `Minibits Wallet Address`, dotykając `Zmień` -> `Zmień Wallet Address`. Wprowadź preferowany Address i sprawdź dostępność.


![image](assets/en/07.webp)


Po ustawieniu Address zostaniesz poproszony o niewielką "Darowiznę" w celu wsparcia projektu. Chociaż jest to opcjonalne, zdecydowanie zalecam rozważenie tego, jeśli planujesz regularnie korzystać z usługi. Projekty open-source, takie jak Minibits, polegają na wsparciu społeczności, aby kontynuować rozwój i konserwację. Nawet niewielki wkład pomaga zapewnić długowieczność projektu.


![image](assets/en/08.webp)


## 5️⃣ Konfiguracja Nostr


Jeśli chcesz dawać napiwki osobom, które obserwujesz na Nostr, możesz `Dodaj swój klucz npub`, wybierając `Kontakty`, a następnie `Publiczne`. Spowoduje to połączenie Minibits Wallet z siecią społecznościową Nostr, umożliwiając płynne dawanie napiwków.


Masz również opcję `Użyj własnego profilu`, przechodząc do `Ustawienia`, a następnie `Prywatność`, aby zaimportować własny Nostr Address i klucz. Należy jednak pamiętać, że spowoduje to zatrzymanie komunikacji Wallet z serwerami minibits.cash Nostr i LNURL Address, co wyłączy funkcje Address do odbierania zapów i płatności.


![image](assets/en/09.webp)


## 6️⃣ Otrzymywanie środków


Aby początkowo otrzymać środki, należy doładować Wallet za pomocą piorunującego Invoice. Proces ten jest prosty: dotknij "Doładowanie", wprowadź "Kwotę", którą chcesz dodać, opcjonalnie dodaj "Memo", a następnie dotknij "Utwórz Invoice". Następnie musisz zapłacić Invoice za pomocą innego Lightning Wallet, który konwertuje płatności Bitcoin Lightning na tokeny ecash w Minibits Wallet.


![image](assets/en/10.webp)


## 7️⃣ Wyślij środki


Po sfinansowaniu Wallet możesz wysyłać środki na dwa różne sposoby.


### Wyślij ecash


Pierwszą opcją jest bezpośrednie wysłanie ecash. Stuknij w `Wyślij`, następnie wybierz `Wyślij ecash`, wprowadź `Kwotę` i stuknij w `Utwórz token.` Spowoduje to generate kod QR, który możesz udostępnić odbiorcy lub poprosić go o zeskanowanie bezpośrednio swoim urządzeniem. Odbiorca zobaczy tokeny pojawiające się w jego Wallet niemal natychmiast, bez opłat Blockchain lub opóźnień w potwierdzeniu.


![image](assets/en/11.webp)


### Płać za pomocą Lightning


Drugą opcją jest płatność przez Lightning. Stuknij w `Wyślij`, a następnie wybierz `Zapłać przez Lightning`. Możesz wybrać spośród `kontaktów` Nostr (jeśli podłączyłeś npub) lub wprowadzić/wkleić kod płatności Lightning Address, Invoice lub LNURL za pomocą opcji `Wklej` lub `Skanuj`. Po `Potwierdzeniu` odbiorcy, zostaniesz poproszony o wprowadzenie `Kwoty do zapłaty`, opcjonalnie dodanie notatki, a następnie dotknij `Potwierdź`, a następnie `Zapłać teraz`, aby zakończyć transakcję Lightning.


![image](assets/en/12.webp)


## 8️⃣ Utwórz połączenie NWC


Kolejną potężną funkcją Minibits jest możliwość tworzenia połączeń `Nostr Wallet Connect (NWC) `, które pozwalają innym aplikacjom żądać płatności z Wallet bez ujawniania kluczy prywatnych.


Aby to skonfigurować, przejdź do `Ustawienia`, następnie wybierz `Nostr Wallet Connect` i dotknij `Dodaj połączenie`. Nazwij połączenie czymś opisowym, aby zidentyfikować zarówno aplikację, jak i powiązane konto użytkownika. Ustaw rozsądny maksymalny dzienny limit, aby kontrolować, ile można wydać za pośrednictwem tego połączenia, a następnie dotknij `Zapisz`, aby zakończyć konfigurację.


Ta funkcja jest szczególnie przydatna w przypadku usług takich jak Nostr Clients, w których chcesz włączyć automatyczne napiwki bez ręcznego zatwierdzania każdej transakcji.


![image](assets/en/12.webp)


## wnioski


Minibity stanowią przystępny punkt wejścia do świata ecash, oferując płatności skoncentrowane na prywatności, które uzupełniają zasoby Bitcoin. Pamiętaj, aby zawsze utrzymywać odpowiednie kopie zapasowe, rozważyć użycie wielu mennic w celu zapewnienia redundancji i przechowywać tylko odpowiednie ilości w tym rozwiązaniu powierniczym.


Dodatkowe zasoby można znaleźć w repozytorium Minibits GitHub, na oficjalnej stronie internetowej oraz na kanale Telegram, gdzie społeczność aktywnie dyskutuje na temat rozwoju i rozwiązywania problemów


- [Github](https://github.com/minibits-cash/minibits_wallet)
- [Strona internetowa](https://www.minibits.cash/)
- [Telegram](https://t.me/MinibitsWallet)


Ekosystem ecash wciąż ewoluuje, ale narzędzia takie jak Minibits sprawiają, że ta potężna technologia prywatności staje się coraz bardziej dostępna dla zwykłych użytkowników.