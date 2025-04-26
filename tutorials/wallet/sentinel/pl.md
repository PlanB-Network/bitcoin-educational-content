---
name: Sentinel Watch-Only
description: Czym jest Watch-only wallet i jak z niego korzystać?
---

![cover](assets/cover.webp)


---

**\*OSTRZEŻENIE: Po aresztowaniu założycieli Samourai Wallet i przejęciu ich serwerów 24 kwietnia, aplikacja Sentinel nadal działa, ale **obowiązkowe jest korzystanie z własnego Dojo** w celu uzyskania dostępu do informacji Blockchain i transmisji transakcji


uważnie śledzimy rozwój tej sprawy, a także rozwój związany z powiązanymi narzędziami. Zapewniamy, że będziemy aktualizować ten poradnik w miarę pojawiania się nowych informacji


ten samouczek służy wyłącznie celom edukacyjnym i informacyjnym. Nie popieramy ani nie zachęcamy do korzystania z tych narzędzi w celach przestępczych. Każdy użytkownik jest odpowiedzialny za przestrzeganie prawa obowiązującego w jego jurysdykcji


---

> Klucze prywatne powinny pozostać prywatne.

W tym artykule zbadamy wszystko, co musisz wiedzieć o portfelach tylko do zegarków. Omawiamy sposób ich działania i analizujemy różne aplikacje dostępne na rynku. Na koniec oferujemy szczegółowy samouczek dotyczący jednej z najpopularniejszych aplikacji Watch-only wallet: Sentinel.


## Co to jest Watch-only wallet?


Watch-only wallet lub Wallet tylko do odczytu to rodzaj oprogramowania zaprojektowanego w celu umożliwienia użytkownikowi obserwowania transakcji powiązanych z jednym lub większą liczbą określonych kluczy publicznych Bitcoin, bez dostępu do odpowiadających im kluczy prywatnych.


Ten typ aplikacji przechowuje jedynie dane niezbędne do monitorowania Bitcoin Wallet, w tym przeglądania jego salda i historii transakcji, ale nie ma dostępu do kluczy prywatnych. W związku z tym niemożliwe jest wydawanie bitcoinów przechowywanych w Wallet w aplikacji tylko do monitorowania.

![watch-only](assets/en/1.webp)

Watch-only jest zwykle używany w połączeniu z Hardware Wallet. Pozwala to na przechowywanie kluczy prywatnych Wallet "Cold" na urządzeniu niepodłączonym do Internetu, które ma minimalną powierzchnię ataku, izolując klucze prywatne od potencjalnie wrażliwych środowisk. Z drugiej strony, aplikacja typu watch-only przechowuje wyłącznie rozszerzony klucz publiczny (`xpub`, `zpub` itp.) Bitcoin Wallet. Ten klucz nadrzędny nie pozwala na odkrycie powiązanych kluczy prywatnych, a co za tym idzie, nie pozwala na wydawanie bitcoinów. Pozwala on jednak na wyprowadzenie podrzędnych kluczy publicznych i adresów odbiorczych. Znając adresy Wallet zabezpieczone przez Hardware Wallet, aplikacja watch-only może śledzić te transakcje w sieci Bitcoin, oferując użytkownikowi możliwość monitorowania salda i nowych adresów odbiorczych generate, bez konieczności podłączania Hardware Wallet za każdym razem.


## Którego Watch-only wallet użyć?


Obecnie najbardziej wszechstronną aplikacją jest [Sentinel](https://sentinel.watch/), opracowany przez zespół Samourai Wallet. Obejmuje ona wszystkie niezbędne funkcje dobrego Watch-only wallet:



- Obsługa kluczy rozszerzonych, kluczy publicznych i adresów;
- Możliwość organizowania wielu kont lub portfeli w kolekcje;
- Generowanie adresów do otrzymywania bitcoinów na swoim Hardware Wallet bez konieczności jego bezpośredniego użycia;
- Możliwość tworzenia i nadawania transakcji w trybie offline;
- Opcja połączenia z własnym węzłem Bitcoin;
- Integracja Tora w celu zwiększenia prywatności.

Unikalne wady Sentinel polegają na tym, że aplikacja jest dostępna wyłącznie na Androida i nie obsługuje portfeli z wieloma podpisami. Dlatego też, jeśli posiadasz urządzenie z Androidem, a twój Wallet to klasyczny pojedynczy podpis, polecam Sentinel.

Dla tych, którzy chcą śledzić Wallet z wieloma podpisami, Blue Wallet jest jedyną znaną mi aplikacją, która oferuje tryb tylko do oglądania dla tego typu portfeli i jest dostępna zarówno na Androida, jak i iOS.


Dla użytkowników iOS szukających alternatywy dla Sentinel, [Green Wallet](https://blockstream.com/Green/) lub [Blue Wallet](https://bluewallet.io/watch-only/) mogą być opcjami, chociaż ich funkcjonalność tylko dla zegarków nie jest tak wszechstronna jak Sentinel.

![watch-only](assets/notext/2.webp)


## Jak korzystać z Sentinel Watch-only wallet?


### Instalacja i konfiguracja


Zacznij od zainstalowania aplikacji Sentinel. Można to zrobić ze Sklepu Google Play lub korzystając z [APK dostępnego do pobrania na oficjalnej stronie](https://sentinel.watch/download/).


![watch-only](assets/notext/3.webp)


Po pierwszym otwarciu aplikacji użytkownik ma możliwość wyboru pomiędzy:



- `Połącz z Dojo`;
- `Połącz się z serwerem Samourai`.


Dojo, opracowane przez zespół Samourai, to pełna wersja węzła Bitcoin, którą można zainstalować samodzielnie lub dodać jednym kliknięciem do rozwiązań node-in-box, takich jak [Umbrel](https://umbrel.com/) i [RoninDojo](https://ronindojo.io/).


[**-> Dowiedz się, jak zainstalować RoninDojo v2 na Raspberry Pi.**](https://planb.network/tutorials/node/Bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8)


Jeśli posiadasz własne Dojo, możesz je podłączyć na tym etapie. W ten sposób skorzystasz z najwyższego poziomu prywatności podczas sprawdzania informacji o transakcjach w sieci Bitcoin.


![watch-only](assets/notext/4.webp)


W przeciwnym razie można wybrać domyślny serwer Samourai. Możesz także wybrać, czy chcesz łączyć się przez Tor, czy nie.


![watch-only](assets/notext/5.webp)


Następnie przejdziesz do strony głównej Sentinel.


![watch-only](assets/notext/6.webp)


Aby rozpocząć, możesz skonfigurować aplikację. Kliknij na trzy małe kropki w prawym górnym rogu, a następnie na `Ustawienia`.


![watch-only](assets/notext/7.webp)

Wybierając `Kod PIN użytkownika`, masz możliwość ustawienia hasła w celu zabezpieczenia dostępu do Watch-only wallet. Masz również możliwość zmiany waluty referencyjnej do przeliczania sald na walutę fiducjarną, a nawet ukrycia wartości fiducjarnych poprzez aktywację opcji `Ukryj wartości fiducjarne`. W celu zwiększenia bezpieczeństwa można aktywować opcję `Disable Screenshots`, która zapobiega wykonywaniu zrzutów ekranu aplikacji Sentinel, a tym samym zapobiega ujawnianiu informacji na ekranie zewnętrznym.

![watch-only](assets/notext/8.webp)


W tym menu ustawień dostępna jest również opcja tworzenia kopii zapasowej Sentinela.


### Korzystanie z Watch-only wallet


Na stronie głównej naciśnij niebieski przycisk `NEW`, aby dodać nowy rozszerzony klucz publiczny do śledzenia. Następnie możesz zeskanować kod QR swojego klucza lub bezpośrednio wkleić klucz (`xpub`, `zpub`...), wybierając `Paste Pubkey`.


![watch-only](assets/notext/9.webp)


Ogólnie rzecz biorąc, `xpub` twojego Wallet jest bezpośrednio dostępny za pośrednictwem używanego oprogramowania do zarządzania Wallet. Na przykład, jeśli zarządzasz Hardware Wallet za pomocą Sparrow, informacje te można znaleźć w zakładce `Settings`, w sekcji `Keystore`.


![watch-only](assets/notext/10.webp)


Po wprowadzeniu rozszerzonego klucza publicznego w Sentinel, aplikacja oferuje utworzenie nowej kolekcji. Kolekcja reprezentuje zestaw rozszerzonych kluczy publicznych zorganizowanych razem. Ta opcja daje możliwość nie tylko wylistowania wszystkich `xpub`, ale także sklasyfikowania ich w uporządkowany sposób. Na przykład, jeśli posiadasz Samourai Wallet z wieloma kontami (depozyt, premix, postmix...), możesz zebrać wszystkie te konta w kolekcji `Samourai`. Dla portfeli zarządzanych dla rodziny można utworzyć kolekcję o nazwie `Family`.


Wybierz `Utwórz nową kolekcję`. Następnie wprowadź nazwę dla zintegrowanego klucza rozszerzonego. Na przykład, jeśli zeskanuję konto depozytowe mojego Samourai Wallet, nadam temu kluczowi nazwę `Deposit`. Kliknij `ZAPISZ`, aby zakończyć.


![watch-only](assets/notext/11.webp)


Następnie przypisz nazwę do tej kolekcji i naciśnij ikonę zatwierdzenia znajdującą się w prawym górnym rogu ekranu, aby zapisać kolekcję. Twoja kolekcja jest teraz widoczna na ekranie głównym Sentinel.


![watch-only](assets/notext/12.webp)


Jeśli chcesz dodać kolejny rozszerzony klucz publiczny, kliknij ponownie `NEW` i wprowadź swój klucz.


![watch-only](assets/notext/13.webp)

Następnie zostaniesz poproszony o wybranie kolekcji, z którą chcesz zintegrować ten klucz, lub o utworzenie nowej. Na przykład w moim przypadku skonfigurowałem kolekcję specjalnie dla mojego Ledger Wallet.

![watch-only](assets/notext/14.webp)


Aby zobaczyć rozszerzone klucze kolekcji w szczegółach, wystarczy na nią kliknąć. Następnie możesz nawigować po różnych zakładkach, aby wyświetlić historię transakcji.


![watch-only](assets/notext/15.webp)


Z poziomu kolekcji, dotykając trzech małych kropek w prawym górnym rogu, a następnie opcji `View Unspent Outputs`, można uzyskać dostęp do listy UTXO przechowywanych przez śledzony Wallet.


![watch-only](assets/notext/16.webp)


### Wysyłanie i odbieranie Bitcoinów z Sentinel


Podobnie jak w przypadku każdego dobrego Watch-only wallet, Sentinel umożliwia generate odbieranie adresów do otrzymywania bitcoinów na śledzonym Wallet. Ale Sentinel oferuje również inną zaawansowaną funkcję: tworzenie i nadawanie Partially Signed Bitcoin Transaction (PSBT). W ten sposób Wallet posiadający klucze prywatne może podpisać tę transakcję, która po podpisaniu może zostać rozesłana do sieci Bitcoin przez Sentinel. Zobaczmy, jak to wszystko zrobić.


**Uwaga, nie zaleca się otrzymywania bitcoinów na Address, który nie został zweryfikowany przez sam Wallet.** Jeśli Wallet posiadający klucze prywatne, taki jak Hardware Wallet, nie potwierdził wyraźnie, że dany Address jest z nim powiązany, wysyłanie bitcoinów do tego Address jest ryzykowną praktyką. Bez takiego potwierdzenia nie ma bowiem gwarancji, że Address rzeczywiście należy do danego Wallet. W związku z tym należy ostrożnie korzystać z funkcji odbierania Watch-only wallet, pamiętając, że wysłane środki mogą zostać potencjalnie utracone.


Aby otrzymać bitcoiny za pośrednictwem Sentinel, wybierz interesującą Cię kolekcję, a następnie kliknij zakładkę odpowiadającą rozszerzonemu kluczowi publicznemu, do którego chcesz przelać środki.


![watch-only](assets/notext/17.webp)


Na koniec kliknij ikonę strzałki w lewym dolnym rogu ekranu. Sentinel wygeneruje dla Ciebie pusty odbiorczy Address. Można go skopiować lub zeskanować za pomocą kodu QR.


![watch-only](assets/notext/18.webp)


Aby dokonać generate na PSBT z Sentinel, a tym samym zainicjować transakcję wydatkową, przejdź do klucza rozszerzonego Wallet, z którego chcesz dokonać płatności. Weźmy na przykład moje konto depozytowe na Wallet Samourai. Następnie kliknij ikonę strzałki znajdującą się w prawym dolnym rogu ekranu.


![watch-only](assets/notext/19.webp)


Wprowadź wszystkie parametry związane z transakcją:



- Wprowadź Address odbiorcy (klikając ikonę kodu QR, masz możliwość zeskanowania tego Address);
- Określ kwotę do wysłania do tego Address;
- Określ opłaty transakcyjne.


Po wypełnieniu wszystkich niezbędnych pól dla transakcji, naciśnij przycisk `COMPOSE UNSIGNED TRANSACTION`.


![watch-only](assets/notext/20.webp)


Następnie uzyskasz dostęp do PSBT, który reprezentuje skonstruowaną, ale niepodpisaną transakcję Bitcoin, ponieważ Sentinel nie ma dostępu do twoich kluczy prywatnych. Możesz skopiować tę transakcję, wyeksportować ją jako plik `.PSBT` lub zeskanować ją za pomocą animowanego kodu QR.


![watch-only](assets/notext/21.webp)


Następnie przejdź do Wallet, który ma klucze prywatne do podpisania transakcji (Samourai, Hardware Wallet...).


![watch-only](assets/notext/22.webp)


Po podpisaniu transakcji możesz wrócić do Sentinel, aby ją rozgłosić. Aby to zrobić, w menu głównym kliknij trzy małe kropki w prawym górnym rogu, a następnie `Rozgłoś transakcję`.


![watch-only](assets/notext/23.webp)


Masz możliwość wprowadzenia podpisanego PSBT na trzy różne sposoby:



- Poprzez wklejenie go bezpośrednio ze schowka;
- Importując go z pliku `.PSBT`;
- Skanując go za pomocą kodu QR.


![watch-only](assets/notext/24.webp)


Po wprowadzeniu podpisanej transakcji w szarej ramce można kliknąć przycisk Green `BROADCAST TRANSACTION`, aby rozgłosić ją w sieci Bitcoin. Sentinel przekaże ci swój txid.


![watch-only](assets/notext/25.webp)