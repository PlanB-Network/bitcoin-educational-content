---
name: Umbrel Nostr
description: Konfigurowanie i używanie aplikacji Nostr na platformie Umbrel
---

![cover](assets/cover.webp)



## Wymagania wstępne: Instalacja Umbrel



Umbrel to platforma open-source, która umożliwia łatwe hostowanie aplikacji Bitcoin i innych usług na własnym serwerze. Jest to kompleksowe rozwiązanie, które znacznie upraszcza samodzielne hostowanie węzłów Bitcoin i zdecentralizowanych aplikacji.



Upewnij się, że zainstalowałeś Umbrel, postępując zgodnie z naszym przewodnikiem instalacji:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Wprowadzenie do Nostr



**Nostr** to otwarty, zdecentralizowany protokół sieciowy przeznaczony dla sieci społecznościowych. Jego nazwa to skrót od _"Notes and Other Stuff Transmitted by Relays"_. Pozwala on każdemu publikować wiadomości (notatki), zarządzane jako zdarzenia JSON, i propagować je za pośrednictwem serwerów przekaźnikowych, a nie scentralizowanej platformy. Każdy użytkownik posiada parę kluczy kryptograficznych (prywatny/publiczny), które służą jako identyfikator: klucz publiczny (npub) identyfikuje użytkownika, a klucz prywatny (nsec) umożliwia podpisywanie wiadomości. Dzięki tej rozproszonej architekturze **Nostr oferuje odporność na cenzurę** i dużą elastyczność: możesz używać kilku klientów i łączyć się z dowolną liczbą przekaźników, bez uzależnienia od jednego serwera.



Krótko mówiąc, Nostr to zdecentralizowany protokół komunikacyjny, w którym **klienci** (aplikacje użytkownika) wysyłają i odbierają zdarzenia za pośrednictwem **relayerów** (serwerów). Protokół ten jest szczególnie popularny wśród społeczności Bitcoin od 2023 roku, ze względu na jego wartości decentralizacji i suwerenności danych.



**Uwaga:** Do korzystania z Nostr potrzebny jest klucz prywatny (wygenerowany przez klienta Nostr lub dedykowane rozszerzenie). **Nigdy nie udostępniaj swojego klucza prywatnego**, ponieważ pozwoliłoby to komukolwiek podszyć się pod ciebie. Przechowuj go w bezpiecznym miejscu i korzystaj z bezpiecznych narzędzi do zarządzania kluczami (patrz Wskazówka poniżej).



## Aplikacje parasolowe dla Nostr



Umbrel oferuje ekosystem zintegrowanych aplikacji, aby w pełni wykorzystać możliwości Nostr na węźle osobistym. Zamierzamy szczegółowo opisać korzystanie z głównych aplikacji związanych z Nostr: **Nostr Relay**, **noStrudel**, **Snort** i **Nostr Wallet Connect**. Każda z nich spełnia określone potrzeby: _Nostr Relay_ jest **prywatnym serwerem przekaźnikowym**, _noStrudel_ i _Snort_ są **klientami Nostr** (interfejsami do czytania/publikowania notatek), podczas gdy _Nostr Wallet Connect_ jest narzędziem do łączenia **portfolio Lightning** z Nostr.



### Nostr Relay - Twój prywatny przekaźnik na Umbrel



![Page d'installation de Nostr Relay sur l'App Store Umbrel](assets/fr/01.webp)



**Nostr Relay** to oficjalna aplikacja Umbrel do uruchamiania **własnego przekaźnika Nostr** na węźle. Głównym celem jest posiadanie **prywatnego** i niezawodnego przekaźnika do **tworzenia kopii zapasowych całej aktywności Nostr** w czasie rzeczywistym. Innymi słowy, używając tego osobistego przekaźnika oprócz publicznych przekaźników, zapewniasz, że wszystkie twoje notatki, wiadomości i reakcje są kopiowane do domu, bezpieczne przed cenzurą lub utratą danych.



**Instalacja:** Z Umbrel App Store (kategoria _Social_), zainstaluj _Nostr Relay_. Po uruchomieniu aplikacja działa w tle (usługa docker).



![Interface de Nostr Relay avec l'URL du relais](assets/fr/02.webp)



Zobaczysz jego sieć Interface za pośrednictwem Umbrel: zawiera podstawowe informacje, a przede wszystkim adres URL twojego przekaźnika (w prawym górnym rogu), który będziesz musiał skopiować do dalszego użytku. Dostępny jest również przycisk synchronizacji (ikona kuli ziemskiej).



**Aby skorzystać z przekaźnika Umbrel:



**Dodaj przekaźnik do klienta Nostr:** W aplikacji klienckiej (np. Damus na iOS, Amethyst na Androida, Snort lub noStrudel na Umbrel, itp.) dodaj adres URL prywatnego przekaźnika, który skopiowałeś wcześniej. Domyślnie przekaźnik Umbrel nasłuchuje na porcie **4848**. Jeśli uzyskujesz do niego dostęp w sieci lokalnej, daje to adres URL taki jak: `ws://umbrel.local:4848` (lub użyć lokalnego IP Umbrela).



Jeśli korzystasz z Tailscale (patrz poniżej), możesz nawet użyć aliasu DNS MagicDNS (zwykle `umbrel` lub automatycznie wygenerowanej nazwy), aby uzyskać do niego dostęp z dowolnego miejsca, zawsze na porcie 4848.



Jeśli wolisz Tor, pobierz Umbrel's .onion Address i użyj go z portem 4848 za pośrednictwem przeglądarki lub klienta kompatybilnego z Tor (patrz sekcja Tor)



Po dodaniu adresu URL do konfiguracji przekaźnika klienta Nostr, połącz się z tym przekaźnikiem. Powinieneś zobaczyć w swoim kliencie, że przekaźnik Umbrel jest podłączony (zwykle wskazywany przez kropkę Green lub podobną).



**Synchronizacja historii (opcjonalnie)**: W sieci Interface _Nostr Relay_ na Umbrel, kliknij na ikonę **globe** 🌐 (na górze strony). Ta czynność zmusi przekaźnik Umbrel do połączenia się z innymi przekaźnikami (skonfigurowanymi w kliencie) w celu **zaimportowania starych działań publicznych**. Oznacza to, że wcześniejsze notatki opublikowane lub przeczytane za pośrednictwem publicznych przekaźników zostaną również pobrane i zapisane w prywatnym przekaźniku. Należy poczekać na synchronizację.



**Używaj Nostr jak zwykle:** Od teraz każda nowa aktywność (opublikowane notatki, reakcje, zaszyfrowane prywatne wiadomości itp.), którą wykonujesz w Nostr, będzie przekazywana jak zwykle do publicznych przekaźników **i równolegle do twojego przekaźnika Umbrel**. Jeśli klient Nostr jest poprawnie skonfigurowany, wyśle każde zdarzenie do wszystkich przekaźników (w tym do twojego). Twój prywatny przekaźnik będzie działał jako kopia zapasowa w czasie rzeczywistym. Nawet w przypadku tymczasowego rozłączenia, klienci będą mogli później ponownie zsynchronizować brakujące dane dzięki temu przekaźnikowi. Daje to pełną kontrolę nad danymi Nostr



W tle, _Nostr Relay_ firmy Umbrel opiera się na projekcie open-source **nostr-rs-relay** (implementacja protokołu Rust). Obsługuje cały protokół Nostr i wiele standardowych NIP-ów (NIP-01, 02, 03, 09, 11, 12, 15, 16, 20, 22, 26, 28, 33 itd.), gwarantując maksymalną kompatybilność z klientami.



### noStrudel - Klient Nostr dla odkrywców



![Page d'installation de noStrudel sur l'App Store Umbrel](assets/fr/03.webp)



**noStrudel** to zorientowany na użytkownika klient sieciowy Nostr, idealny do szczegółowego zrozumienia i eksploracji sieci Nostr. Jest to rodzaj piaskownicy do sprawdzania zdarzeń i przekaźników oraz do eksperymentowania z zaawansowanymi funkcjami protokołu. Interface jest w języku angielskim i jest stosunkowo techniczny, dzięki czemu jest idealny dla doświadczonych użytkowników ciekawych wewnętrznego działania Nostr.



**Instalacja:** Zainstaluj _noStrudel_ z Umbrel App Store (kategoria _Social_). Po uruchomieniu można uzyskać do niego dostęp przez przeglądarkę na Address Umbrel (np. `http://umbrel.local` lub przez .onion/Tailscale, patrz sekcja dostępu zewnętrznego).



![Page d'accueil de noStrudel avec le bouton Setup Relays](assets/fr/04.webp)



**Konfiguracja przekaźników:** Po otwarciu noStrudel, w prawym górnym rogu pojawi się przycisk "Setup Relays". Kliknij go, aby skonfigurować przekaźniki.



![Page de configuration des relais dans noStrudel](assets/fr/05.webp)



Na tej stronie wklej adres URL skopiowanego wcześniej przekaźnika Umbrel. Możesz także dodać inne przekaźniki proponowane domyślnie przez aplikację. Po skonfigurowaniu przekaźników kliknij "Zaloguj się" w lewym dolnym rogu, aby kontynuować.



![Options de connexion dans noStrudel](assets/fr/06.webp)



**Połączenie:** noStrudel oferuje kilka opcji połączenia. W naszym przypadku wybierzemy "Klucz prywatny" i wkleimy wcześniej wygenerowany klucz prywatny Nostr. Jeśli nie masz jeszcze klucza, możesz zainstalować rozszerzenie [Nostr Connect] (https://chromewebstore.google.com/detail/nostr-connect/ampjiinddmggbhpebhaegmjkbbeofoaj), aby utworzyć i/lub zapisać klucze Nostr, a tym samym bezpieczniej komunikować się z różnymi aplikacjami Nostr.



![Interface principale de noStrudel](assets/fr/07.webp)



Po podłączeniu można użyć noStrudel do udostępniania notatek za pośrednictwem Nostr. Interface zapewnia dostęp do :





- Kompletny pulpit nawigacyjny Nostr z osią czasu notatek, powiadomieniami, wiadomościami, wyszukiwaniem profili
- Zarządzanie przekaźnikami i status połączenia
- Zaawansowane narzędzia do analizy zdarzeń i ich zawartości JSON
- Opcje konfiguracji filtrów osi czasu i kodów PIN



**Wskazówka:** W _noStrudel_ można ustawić filtry _timeline_ lub przetestować różne _NIP (Nostr Implementation Possibilities)_. Na przykład sprawdzić wsparcie dla NIP-05 (zdecentralizowane identyfikatory) lub nowszych funkcji. To sprawia, że _noStrudel_ jest doskonałym narzędziem do eksperymentowania w kontrolowanym środowisku.



### Snort - nowoczesny klient Nostr na Umbrel



![Page d'installation de Snort sur l'App Store Umbrel](assets/fr/08.webp)



**Snort** to kolejny klient sieciowy Nostr dostępny na Umbrel, oferujący nowoczesny, szybki i przejrzysty **Interface** do interakcji ze zdecentralizowaną siecią społecznościową. W przeciwieństwie do noStrudel, który jest skierowany do zaawansowanych użytkowników, _Snort_ dąży do prostoty użytkowania bez poświęcania funkcjonalności. Jest zbudowany w React i oferuje schludny UX przypominający klasyczne sieci społecznościowe, dzięki czemu nadaje się do codziennego użytku.



**Instalacja:** Zainstaluj _Snort_ z Umbrel App Store (kategoria _Social_).



![Page d'accueil de Snort avec le bouton S'inscrire](assets/fr/09.webp)



Po otwarciu Snort, w lewym dolnym rogu pojawi się przycisk "Zarejestruj się".



![Options de connexion dans Snort](assets/fr/10.webp)



Możesz wybrać rejestrację lub połączenie z istniejącym kontem (co zamierzamy zrobić w tym samouczku).



![Méthodes de connexion dans Snort](assets/fr/11.webp)



Snort oferuje kilka metod połączenia. Możesz użyć wcześniej zainstalowanego rozszerzenia Nostr Connect lub innych dostępnych metod. Po połączeniu będziesz mógł w pełni korzystać z aplikacji.



Interface od _Snort_ oferuje :





- Wyświetlacz **Posts/Conversations/Global** umożliwia nawigację między notatkami, dyskusjami w wątkach lub globalnym kanałem
- Zakładki **Notifications**, **Messages** (DM), **Search**, **Profile** itd.
- Przycisk **+** lub _Write_ do publikowania nowej notatki
- Zarządzanie **subskrypcjami (następującymi po sobie)** i **listami**
- Menu zarządzania przekaźnikami do dodawania/usuwania przekaźników i śledzenia ich dostępności



**Zalecana konfiguracja przekaźnika:** Aby dodać przekaźnik Umbrel, przejdź do Ustawienia - Przekaźniki. Wprowadź adres URL swojego przekaźnika (`ws://umbrel:4848` lub inny adres URL w zależności od konfiguracji) na liście przekaźników Snort. W ten sposób Snort opublikuje notatki w prywatnym przekaźniku oprócz tych publicznych.



### Nostr Wallet Connect - Połącz swój Lightning Wallet z Nostr



**Nostr Wallet Connect (NWC)** to aplikacja, która **połącza węzeł Umbrel (Lightning)** z kompatybilnymi aplikacjami Nostr w celu dokonywania płatności Lightning (na przykład wysyłania _zaps_, tych mikropłatności za "polubienie" treści). W tym samouczku przyjrzymy się, jak połączyć noStrudel z węzłem Lightning, aby dokonywać płatności bezpośrednio z Interface.



**Instalacja i konfiguracja:**



![Page d'installation de Nostr Wallet Connect sur l'App Store Umbrel](assets/fr/12.webp)



Zainstaluj _Nostr Wallet Connect_ ze sklepu Alby na Umbrel.



![Configuration de NWC dans noStrudel - Étape 1](assets/fr/13.webp)



W noStrudel kliknij na swój profil w prawym górnym rogu, a następnie na przycisk "zarządzaj".



![Configuration de NWC dans noStrudel - Étape 2](assets/fr/14.webp)



Kliknij "Lightning", a następnie "connect Wallet".



![Configuration de NWC dans noStrudel - Étape 3](assets/fr/15.webp)



Spośród dostępnych opcji połączenia wybierz "Umbrel".



![Configuration de NWC dans noStrudel - Étape 4](assets/fr/16.webp)



Kliknij "Połącz", aby zostać automatycznie przekierowanym do sesji Umbrel Nostr Wallet Connect.



![Page de configuration des autorisations NWC](assets/fr/17.webp)



Na stronie Nostr Wallet Connect można :




   - Zdefiniuj swój maksymalny budżet
   - Zatwierdzanie autoryzacji
   - Ustawienie czasu wygaśnięcia połączenia


Kliknij "Połącz", aby zakończyć.



![Confirmation de connexion dans noStrudel](assets/fr/18.webp)



Zostaniesz przekierowany do noStrudel z wiadomością potwierdzającą: możesz teraz zniszczyć cały świat z węzła Wallet/LND!



Dzięki NWC **płatności Lightning za pośrednictwem Nostr** (zapy do nagradzania postów, płatności _Value for Value_ itp.) rozpoczynają się od **własnego węzła**. Nie musisz już przekierowywać swoich transakcji przez zewnętrzne usługi lub skanować QR z telefonu za każdym razem. Doświadczenie użytkownika jest znacznie lepsze, pozostając jednocześnie _non custodial_ i przyjaznym dla prywatności.



Jeśli chcesz dowiedzieć się, jak skonfigurować własny węzeł Lightning na Umbrel, polecam zapoznać się z tym obszernym samouczkiem:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Zaawansowana konfiguracja i zabezpieczenia



Korzystanie z Umbrel i Nostr na zaawansowanym poziomie wymaga szczególnej uwagi na **bezpieczeństwo** i **łączność**. Oto kilka wskazówek, jak chronić swoją konfigurację i uzyskać do niej optymalny dostęp, gdziekolwiek jesteś.



### Bezpieczny dostęp z zewnątrz: Tor i Tailscale



Ze względów bezpieczeństwa Umbrel jest domyślnie dostępny tylko w sieci lokalnej (i przez Tor). Aby korzystać z Nostr poza domem, masz dwa preferowane rozwiązania: **Tor** (anonimowy dostęp przez sieć cebulową) i **Tailscale** (prywatna siatka VPN).





- Dostęp przez Tor:** Umbrel automatycznie konfiguruje **usługę Tor (.onion)** dla Interface web i aplikacji. Oznacza to, że możesz uzyskać dostęp do Interface Umbrel (w tym _noStrudel_ lub _Snort_) z dowolnego miejsca, używając przeglądarki Tor, bez ujawniania swojego publicznego IP. tor służy do uzyskiwania dostępu do usług Umbrel spoza sieci lokalnej, bez wystawiania urządzenia na działanie Internetu ([Setup Tor on your system - Guides - Umbrel Community](https://community.umbrel.com/t/setup-tor-on-your-system/7509#:~:text=Official%20website%3A%20https%3A%2F%2Fwww))._ Aby skorzystać z tej opcji, przejdź do ustawień Umbrel i pobierz adres URL .onion swojego Umbrel (lub zeskanuj dostarczony kod QR). W przeglądarce Tor uzyskaj dostęp do tego .onion Address: otrzymasz ten sam Interface, co lokalnie. Następnie możesz korzystać z aplikacji Nostr tak jak w domu.


**Przekaźnik Nostr przez Tor:** Jeśli chcesz, aby twój przekaźnik Nostr był dostępny przez Tor dla twoich klientów (lub autoryzowanych znajomych), jest to możliwe. Umbrel nie dostarcza bezpośrednio .onion Address przekaźnika, ale ponieważ działa on na porcie 4848, możesz albo :





    - Użyj Address .onion UI Umbrel i skonfiguruj klienta tak, aby łączył się za pośrednictwem tego Interface (niepraktyczne dla WebSocket),





    - Lub** wystawić port 4848 jako oddzielną usługę cebulową. Wymaga to majstrowania przy konfiguracji Tora na Umbrel (zarezerwowane dla zaawansowanych użytkowników, którzy dobrze radzą sobie z SSH). Alternatywnie można rozważyć **tunel Tor** na innym serwerze, który przekierowuje do Umbrel: jednak do użytku osobistego najłatwiej jest użyć Tailscale.





- Dostęp przez Tailscale:** [Tailscale](https://tailscale.com/) to rozwiązanie mesh VPN, które tworzy wirtualną sieć prywatną między urządzeniami a Umbrel. Zaleta: działa tak, jakbyś był w sieci LAN, ale przez Internet, szyfrowany i bez skomplikowanej konfiguracji. **Tailscale przypisuje Umbrel stały adres IP i prywatną nazwę domeny, niezależnie od lokalizacji sieciowej ([Tailscale | Umbrel App Store](https://apps.umbrel.com/app/tailscale#:~:text=Tailscale%20is%20zero%20config%20VPN,reviewed%20and%20trusted%20standard))**. W praktyce, po zainstalowaniu Tailscale na Umbrel (z Umbrel App Store, kategoria _Networking_) **i** na swoich urządzeniach (mobilnych, PC...), będziesz mógł dotrzeć do Umbrel poprzez Address jak `100.x.y.z` (Tailscale IP) lub nazwę jak `umbrel.tailnet123.ts.net`.


dla Nostr_, Tailscale jest niezwykle przydatne: Twój telefon komórkowy, jeśli ma aktywne Tailscale, będzie mógł połączyć się z `ws://umbrel:4848` (dzięki MagicDNS) lub bezpośrednio z IP Tailscale i portem 4848, aby użyć przekaźnika. Klienci tacy jak Damus lub Amethyst będą widzieć Umbrel tak, jakby znajdował się w tej samej sieci lokalnej. **Wskazówka:** Włącz opcję **MagicDNS** w Tailscale, aby używać nazwy hosta `umbrel` zamiast zapamiętywania adresu IP. Zapewni to płynne połączenie z przekaźnikiem, nawet gdy jesteś w ruchu ([Nostr Relay | Umbrel App Store](https://apps.umbrel.com/app/nostr-relay#:~:text=client%20%28e,That%27s%20it%21%20Your%20past)).


Co więcej, Tailscale pozwala uzyskać dostęp do Interface Umbrel (a tym samym klientów internetowych _noStrudel/Snort_) za pośrednictwem zwykłej przeglądarki, przy użyciu prywatnego adresu IP lub przypisanej nazwy domeny. Nie ma potrzeby korzystania z przeglądarki Tor, a prędkość transferu danych jest ogólnie lepsza niż przez sieć Tor.




**Uwaga: Tor i Tailscale nie wykluczają się wzajemnie. Tor może być aktywny w celu uzyskania anonimowego dostępu do określonych usług, a Tailscale można używać na co dzień ze względu na jego prostotę. W obu przypadkach nie trzeba otwierać portu na routerze, co zwiększa bezpieczeństwo.



### Zabezpieczanie przekaźnika Nostr (zalecane praktyki)



Jeśli hostujesz przekaźnik Nostr na Umbrel, szczególnie w zaawansowanym kontekście, pamiętaj o zastosowaniu kilku dobrych praktyk:





- Przekaźnik prywatny lub ograniczony:** Domyślnie przekaźnik Umbrel jest prywatny (nie jest publicznie ogłaszany) i jeśli masz do niego dostęp tylko przez Tailscale lub sieć LAN, pozostanie on niedostępny dla nieznajomych. **Zachowaj link w tajemnicy ** Nie rozgłaszaj go w publicznych sieciach Nostr, chyba że chcesz dobrowolnie gościć innych użytkowników, co jest zupełnie inną kwestią (moderacja, przepustowość itp.). Do użytku osobistego zalecamy ograniczenie dostępu do siebie i, jeśli to konieczne, do kilku zaufanych przyjaciół i rodziny.





- Biała lista / uwierzytelnianie**: Implementacja nostr-rs-relay obsługuje mechanizm uwierzytelniania **NIP-42**, a także _whitelists_ kluczy publicznych. Włączając te opcje, możesz ograniczyć swój przekaźnik tak, aby **akceptował tylko zdarzenia podpisane przez określone klucze (twoje)**, lub aby klienci musieli się uwierzytelniać, aby publikować. Ustawienie tego wymaga edycji pliku konfiguracyjnego `config.toml` przekaźnika w Umbrel (przez SSH w kontenerze Docker)._ Jest to zaawansowana manipulacja, ale na przykład możesz wymienić dozwolone reklamy (`pubkey_whitelist`). W ten sposób, nawet jeśli ktoś odkryje twój przekaźnik, nie będzie w stanie opublikować tam niczego, jeśli nie znajduje się na liście.





- Aktualizacje i konserwacja:** Aktualizuj swoją aplikację Umbrel i _Nostr Relay_. Aktualizacje mogą obejmować ulepszenia wydajności (np. lepszą obsługę spamu) i poprawki bezpieczeństwa. Na Umbrel regularnie sprawdzaj App Store pod kątem aktualizacji _Nostr Relay_ i stosuj je w razie potrzeby.





- Monitorowanie i limity:** Miej oko na to, jak używany jest twój przekaźnik. Jeśli otworzysz go dla innych, miej oko na obciążenie (CPU / pamięć RAM) swojego Umbrela, ponieważ przekaźnik może szybko gromadzić dużo danych. nostr-rs-relay oferuje konfigurowalne **limity szybkości i przechowywania** (`limity` w konfiguracji, np. liczba zdarzeń na sekundę, maksymalny rozmiar zdarzenia, czyszczenie starych zdarzeń...). Do użytku prywatnego prawdopodobnie nie będziesz musiał ich dotykać, ale pamiętaj, że te parametry istnieją, jeśli ich potrzebujesz ([nostr-rs-relay/config.toml at master - scsibug/nostr-rs-relay - GitHub](https://github.com/scsibug/nostr-rs-relay/blob/master/config.toml#:~:text=)).





- Zabezpieczanie kluczy Nostr:** Ten punkt został już wspomniany, ale jest kluczowy: nigdy nie wprowadzaj kluczy prywatnych Nostr w Interface, któremu nie w pełni ufasz. Zamiast tego używaj rozszerzeń przeglądarki lub urządzeń zewnętrznych (takich jak Nostr _signers_ na oddzielnych telefonach) do podpisywania wrażliwych działań. Na Umbrel, klienci internetowi tacy jak _Snort_ i _noStrudel_ mogą działać bez znajomości tajnego klucza, poprzez NIP-07. Skorzystaj z tej możliwości, aby połączyć wygodę i bezpieczeństwo.




Postępując zgodnie z tymi wskazówkami, integracja węzła Umbrel z Nostr będzie zarówno potężna **i** bezpieczna. Będziesz mieć kompletne środowisko: węzeł Bitcoin do płatności Lightning, prywatny przekaźnik Nostr zapewniający suwerenność danych oraz wysokowydajne klienty internetowe Nostr do poruszania się po tej nowej zdecentralizowanej sieci społecznościowej. Zapraszamy do odkrywania Nostr z Umbrel!