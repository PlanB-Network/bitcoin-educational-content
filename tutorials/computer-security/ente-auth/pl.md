---
name: Ente Auth
description: Kompleksowy, szyfrowany mechanizm uwierzytelniania 2FA o otwartym kodzie źródłowym
---
![cover](assets/cover.webp)



Uwierzytelnianie dwuskładnikowe (2FA) stało się niezbędne do zabezpieczenia naszych kont internetowych. Oprócz zwykłego hasła wymaga ono tymczasowego kodu, zwykle generowanego przez dedykowaną aplikację. Mechanizm ten, znany jako TOTP (Time-Based One-Time Password), gwarantuje, że nawet jeśli hasło zostanie złamane, atakujący nie będzie w stanie uzyskać dostępu do konta bez posiadania tego drugiego czynnika, odnawianego co 30 sekund.



Wybór odpowiedniej aplikacji uwierzytelniającej nie jest jednak trywialny. Google Authenticator, choć popularny, ma poważne ograniczenia: zastrzeżony kod niemożliwy do audytu, synchronizacja bez szyfrowania end-to-end i ryzyko całkowitej utraty kodów w przypadku problemu z telefonem. Inne rozwiązania, takie jak Authy, wymagają podania numeru telefonu i nie gwarantują całkowitej poufności.



**Ente Auth** wyróżnia się jako nowoczesna, bezpieczna alternatywa. Ta darmowa, wieloplatformowa aplikacja o otwartym kodzie źródłowym, opracowana przez zespół stojący za [Ente Photos](https://ente.io), oferuje kompleksowe szyfrowane kopie zapasowe w chmurze i płynną synchronizację między wszystkimi urządzeniami. W przeciwieństwie do zastrzeżonych rozwiązań, Ente Auth zapewnia pełną kontrolę nad kodami uwierzytelniającymi bez narażania prywatności.



W tym samouczku pokażemy krok po kroku, jak zainstalować i używać Ente Auth oraz dlaczego to rozwiązanie różni się od tradycyjnych uwierzytelniaczy.



## Przedstawiamy Ente Auth



Ente Auth zostało opracowane przez zespół stojący za Ente Photos, kompleksową, szyfrowaną i przyjazną dla prywatności usługą przechowywania zdjęć. Zgodnie z filozofią Ente ("Ente" oznacza "mój" w języku malajalam, symbolizując kontrolę nad danymi), Ente Auth został zaprojektowany tak, aby zapewnić użytkownikom pełną kontrolę nad ich dwuskładnikowymi kodami uwierzytelniającymi.



### Główne cechy



**Standardowe kody TOTP**: Ente Auth generuje tymczasowe kody kompatybilne z większością usług (GitHub, Google, Binance, ProtonMail itp.). Możesz dodać tyle kont 2FA, ile potrzebujesz, a aplikacja obliczy kody na podstawie podanych sekretów.



**Kompleksowe szyfrowane kopie zapasowe w chmurze**: Twoje kody są bezpiecznie przechowywane online. Tylko Ty możesz je odszyfrować - klucz szyfrowania pochodzi z Twojego hasła i jest znany tylko Tobie. Ente (serwer) nie ma wiedzy o twoich sekretach, ani nawet o tytułach twoich kont, ponieważ wszystko jest szyfrowane po stronie klienta przy użyciu architektury zero-knowledge.



**Synchronizacja z wieloma urządzeniami**: Możesz zainstalować Ente Auth na kilku urządzeniach (smartfon, tablet, komputer) i uzyskać dostęp do swoich kodów na wszystkich z nich. Wszelkie zmiany są automatycznie i natychmiastowo propagowane na inne urządzenia za pośrednictwem zaszyfrowanej chmury, co zapewnia dużą elastyczność w codziennej pracy.



**Minimalistyczny, intuicyjny Interface**: Aplikacja oferuje usprawniony Interface, łatwy do opanowania nawet dla nietechnicznych użytkowników. konta 2FA są wyświetlane z nazwą usługi, loginem i 6-cyfrowym kodem, aktualizowanym w czasie rzeczywistym. Ente Auth wyświetla również następny kod z kilkusekundowym wyprzedzeniem, aby uniknąć sytuacji, w której kod wygasa.



**Otwarte źródło i skontrolowane**: Kod źródłowy Ente Auth jest [publiczny na GitHub](https://github.com/ente-io/auth) na licencji AGPL v3.0. Każdy programista może przeprowadzić jego audyt, aby sprawdzić błędy lub niepożądane zachowanie. Zaimplementowana kryptografia była przedmiotem [niezależnego audytu zewnętrznego](https://ente.io/blog/cryptography-audit/), co stanowi gwarancję powagi bezpieczeństwa aplikacji.



### Zalety i ograniczenia



**Korzyści:**




- Prywatność od samego początku dzięki kompleksowemu szyfrowaniu
- Bezpieczna synchronizacja między wszystkimi urządzeniami
- Podlegający audytowi otwarty kod źródłowy
- Interface przejrzysty, intuicyjny w obsłudze Interface
- Automatyczna kopia zapasowa zapobiegająca utracie kodów
- Dostępne na wszystkich platformach (mobilnych i stacjonarnych)



**Ograniczenia:**




- Do synchronizacji wymagane jest połączenie z Internetem
- Zaawansowani użytkownicy mogą preferować rozwiązania w 100% offline, takie jak Aegis (tylko Android)
- Stosunkowo nowe rozwiązanie w porównaniu z rozwiązaniami o ugruntowanej pozycji



## Instalacja



Ente Auth jest dostępny na większości popularnych platform. Aplikację można pobrać z [oficjalnej strony internetowej](https://ente.io/auth) lub z oficjalnych sklepów.



![Installation d'Ente Auth](assets/fr/01.webp)



*Strona pobierania Ente Auth ze wszystkimi dostępnymi platformami*



### Android


Dostępnych jest kilka opcji:




- **Sklep Google Play**: Wyszukaj "Ente Auth" dla klasycznej instalacji
- **F-Droid**: Dostępne z katalogu aplikacji open-source dla systemu Android, z gwarancją sprawdzonej konstrukcji i braku zastrzeżonych treści
- **Instalacja ręczna**: Pliki APK można pobrać z [strony GitHub projektu](https://github.com/ente-io/auth/releases) ze zintegrowanymi powiadomieniami o nowych wersjach



### iOS (iPhone/iPad)


Zainstaluj Ente Auth bezpośrednio z Apple App Store, wyszukując nazwę aplikacji. Aplikację iOS można również uruchomić na komputerach Mac wyposażonych w chipy Apple Silicon (M1/M2) za pośrednictwem Mac App Store.



### Komputery (Windows, macOS, Linux)


Ente Auth oferuje natywne aplikacje desktopowe. Odwiedź [ente.io/download](https://ente.io/download) lub [Releases section of GitHub](https://github.com/ente-io/auth/releases) :





- **Windows**: Dostarczany jest instalator EXE
- **macOS**: Przeciągnij i upuść obraz dysku DMG w aplikacjach
- **Linux**: Dostępnych jest kilka formatów (AppImage portable, .deb dla Debiana/Ubuntu, .rpm dla Fedory/Red Hat)



**Uwaga:** Ten samouczek jest oparty na Ente Auth w wersji 4.4.4 i nowszych. Wcześniejsze wersje mogą mieć drobne różnice Interface.



### Interface Web


Bez instalacji możesz uzyskać dostęp do swoich kodów za pośrednictwem [auth.ente.io](https://auth.ente.io) z dowolnej przeglądarki. Interface web jest ograniczony do przeglądania kodów (przydatne do rozwiązywania problemów), ponieważ dodawanie kont wymaga aplikacji mobilnej lub stacjonarnej ze względów bezpieczeństwa.



## Pierwsza konfiguracja



### Tworzenie konta



Po pierwszym uruchomieniu Ente Auth dostępne są dwie opcje:



![Premier lancement d'Ente Auth](assets/fr/02.webp)



*Ekran główny Ente Auth z opcjami tworzenia konta*



**Z kontem (zalecane)**: Wybierz "Utwórz konto" i wprowadź swój adres e-mail Address oraz hasło. **Ważne**: to hasło służy jako hasło główne do szyfrowania danych. Wybierz silne, unikalne hasło, ponieważ nie ma konwencjonalnej procedury resetowania bez utraty danych. Jeśli je zgubisz, zaszyfrowane dane będą nie do odzyskania.



**Tryb offline**: Wybierz opcję "Używaj bez kopii zapasowych", aby korzystać z aplikacji lokalnie bez chmury. W tym trybie kody pozostają na urządzeniu, ale należy je ręcznie wyeksportować, aby uniknąć ich utraty.



![Vérification email et récupération de clé](assets/fr/03.webp)



*Proces weryfikacji e-mail i generowanie 24-słowowego klucza odzyskiwania*



Weryfikacja e-mail może być wymagana w celu potwierdzenia utworzenia konta i umożliwienia odzyskiwania na nowym urządzeniu. Ente Auth dostarczy również 24-wyrazowy klucz odzyskiwania (oparty na metodzie BIP39). **Konieczne jest zapisanie tego klucza** w bezpiecznym miejscu: jest to jedyny sposób na odzyskanie danych w przypadku zapomnienia hasła.



### Bezpieczeństwo lokalne



Zdecydowanie zalecam włączenie lokalnej ochrony kodem lub biometrycznej. Przejdź do **Ustawienia → Bezpieczeństwo → Ekran blokady** i skonfiguruj :





- **Odblokowywanie biometryczne**: Face ID, odcisk palca w zależności od możliwości urządzenia
- **PIN/hasło specyficzne dla aplikacji**
- **Opóźnienie automatycznej blokady**: np. "Natychmiast" lub po 30 sekundach bezczynności



Ta ochrona zapobiega nieautoryzowanemu dostępowi do kodów, jeśli ktoś uzyska dostęp do odblokowanego telefonu. Należy pamiętać, że ta blokada jest dodatkową barierą: dane pozostają zaszyfrowane od końca do końca nawet bez tej ochrony.



## Dodawanie kont 2FA



### Standardowa procedura



Aby dodać nowe konto 2FA, weźmy konkretny przykład aktywacji 2FA na Bull Bitcoin :



![Configuration du premier compte](assets/fr/04.webp)



*Główny Interface Ente Auth gotowy do dodania pierwszego konta 2FA*



**Po stronie usługi (Bull Bitcoin)**: Zaloguj się na swoje konto Bull Bitcoin, przejdź do ustawień bezpieczeństwa i włącz uwierzytelnianie dwuskładnikowe.



![Paramètres de sécurité Bull Bitcoin](assets/fr/05.webp)



*Menu ustawień zabezpieczeń Interface Bull Bitcoin*



![Activation 2FA Bull Bitcoin](assets/fr/06.webp)



*Opcja włączenia uwierzytelniania dwuskładnikowego w Bull Bitcoin*



Usługa wyświetli kod QR, który należy zeskanować za pomocą aplikacji uwierzytelniającej:



![QR code 2FA Bull Bitcoin](assets/fr/07.webp)



*Kod QR wygenerowany przez Bull Bitcoin do zeskanowania za pomocą urządzenia uwierzytelniającego*



**W Ente Auth**: Kliknij "Enter a setup key", a następnie zeskanuj kod QR wyświetlony przez Bull Bitcoin. Ente Auth automatycznie rozpozna konto i wypełni pola.



![Ajout du compte dans Ente Auth](assets/fr/08.webp)



*Konfiguracja szczegółów konta Bull Bitcoin w Ente Auth*



Możesz dostosować nazwę usługi i swój login, aby ułatwić jej znalezienie. Ustawienia zaawansowane (algorytm SHA1, okres 30s, 6 cyfr) są domyślnie poprawne.



**Weryfikacja po stronie serwisu**: Wróć do Bull Bitcoin i wprowadź 6-cyfrowy kod wygenerowany przez Ente Auth, aby sfinalizować aktywację.



![Saisie du code 2FA](assets/fr/09.webp)



*Wprowadź kod wygenerowany przez Ente Auth, aby potwierdzić aktywację 2FA*



![2FA activée](assets/fr/10.webp)



*Potwierdzenie pomyślnej aktywacji 2FA na Bull Bitcoin*



**Kody zapasowe**: Bull Bitcoin dostarczy ci kody odzyskiwania. **Zachowaj je w bezpiecznym miejscu, oddzielnie od urządzenia uwierzytelniającego.**



![Gestion des codes de sauvegarde](assets/fr/11.webp)



*Opcja awaryjnych kodów zapasowych generate na Bull Bitcoin*



![Codes de récupération](assets/fr/12.webp)



*Lista kodów odzyskiwania, którą należy przechowywać w bezpiecznym miejscu*



### Organizacja i zarządzanie



Ente Auth oferuje kilka praktycznych funkcji:



**Szybkie kopiowanie**: Naciśnij kod, aby skopiować go automatycznie do schowka.



**Działania kontekstowe**: Naciśnij i przytrzymaj (lub kliknij prawym przyciskiem myszy na pulpicie), aby edytować, usunąć, udostępnić lub przypiąć wpis.



**Tagi i wyszukiwanie**: Organizuj swoje konta za pomocą tagów (osobiste/zawodowe, według kategorii usług) i używaj paska wyszukiwania do szybkiego filtrowania.



![Création d'un tag](assets/fr/17.webp)



*Proces tworzenia tagów: menu kontekstowe i okno dialogowe tworzenia*



![Tag appliqué](assets/fr/18.webp)



*Tag "Bitcoin" został pomyślnie zastosowany na koncie Bull Bitcoin*



**Ikony automatyczne**: Każdy wpis może być zilustrowany logo serwisu, dzięki integracji pakietu ikon [Simple Icons](https://simpleicons.org/).



**Tymczasowe bezpieczne udostępnianie**: Unikalna funkcja Ente Auth, bezpieczne udostępnianie, umożliwia przesyłanie kodu 2FA do współpracownika bez ujawniania podstawowego sekretu. generate zaszyfrowany link ważny przez 2, 5 lub maksymalnie 10 minut - odbiorca widzi kod w czasie rzeczywistym, ale nie może go wyeksportować ani uzyskać dostępu do danych konta. Ta metoda jest idealna do pomocy technicznej lub tymczasowej współpracy, oferując poziom bezpieczeństwa niemożliwy do osiągnięcia za pomocą prostego zrzutu ekranu lub wiadomości tekstowej.



![Partage sécurisé](assets/fr/19.webp)



*Interface tymczasowe bezpieczne udostępnianie: wybierz czas trwania (5 min)*



**Bezpieczny eksport/import**: Ente Auth pozwala eksportować kody do innych aplikacji lub importować je z Google Authenticator i innych rozwiązań. Eksport odbywa się za pomocą zaszyfrowanego pliku lub kodu QR, gwarantując możliwość przenoszenia danych bez narażania bezpieczeństwa.



**Klucz odzyskiwania BIP39**: Aplikacja automatycznie generuje 24-wyrazową frazę odzyskiwania zgodnie ze standardem BIP39 (Bitcoin Improvement Proposal), identycznym jak w przypadku portfeli kryptowalutowych. Ta fraza jest ostatecznym kluczem odzyskiwania, umożliwiającym przywrócenie wszystkich kodów, nawet jeśli zapomnisz hasła głównego.



## Konfiguracja i ustawienia



Ente Auth oferuje liczne opcje dostosowywania dostępne za pośrednictwem ustawień aplikacji:



![Paramètres principaux d'Ente Auth](assets/fr/13.webp)



*Przegląd parametrów dostępnych w Ente Auth*



### Zarządzanie kontem i danymi



![Paramètres de sécurité](assets/fr/14.webp)



*Zaawansowane opcje bezpieczeństwa: weryfikacja e-mail, kod PIN, aktywne sesje*



Ustawienia zabezpieczeń umożliwiają :




- Włącz weryfikację e-mail dla nowych połączeń
- Aktywuj klucz dostępu
- Wyświetlanie aktywnych sesji na różnych urządzeniach
- Konfiguracja kodu PIN lub danych biometrycznych



### Interface i opcje użytkowania



![Paramètres généraux](assets/fr/15.webp)



*Parametry Interface i dostosowanie aplikacji*



Ustawienia ogólne obejmują :




- **Język**: Interface wielojęzyczny
- **Wyświetlacz**: Duże ikony, tryb kompaktowy
- **Prywatność**: Ukryj kody, szybkie wyszukiwanie
- **Telemetria**: Raportowanie błędów (można wyłączyć)



## Kopia zapasowa i synchronizacja



### Jak działa szyfrowanie



Po dodaniu konta z połączonym kontem Ente aplikacja natychmiast szyfruje te poufne dane lokalnie przy użyciu klucza głównego (uzyskanego z hasła). Zaszyfrowane dane są następnie wysyłane na serwer Ente w celu ich przechowywania.



Dzięki temu mechanizmowi zawsze dostępna jest zaszyfrowana kopia zapasowa kodów w chmurze. Jeśli zgubisz swoje urządzenie, po prostu zainstaluj ponownie Ente Auth i połącz się ponownie: aplikacja automatycznie pobierze i odszyfruje wszystkie twoje kody.



### Synchronizacja wielu urządzeń



Jeśli korzystasz z Ente Auth zarówno na smartfonie, jak i na komputerze, wszelkie dodatki lub zmiany na jednym urządzeniu pojawiają się w ciągu kilku sekund na drugim. Ta synchronizacja przechodzi przez chmurę Ente, ale ponieważ dane są szyfrowane od końca do końca, serwer widzi tylko nieczytelną zaszyfrowaną zawartość.



![Synchronisation mobile](assets/fr/16.webp)



*Demo synchronizacji: to samo konto Bull Bitcoin dostępne na urządzeniach mobilnych i komputerach*



Synchronizacja jest bezproblemowa: zainstaluj Ente Auth na swoim smartfonie, zaloguj się za pomocą swoich danych uwierzytelniających, a wszystkie kody 2FA (tutaj Bull Bitcoin) pojawią się automatycznie. Powyższy przykład pokazuje idealną synchronizację między komputerem stacjonarnym a urządzeniem mobilnym - ten sam kod Bull Bitcoin jest dostępny na obu urządzeniach.



Jeśli chodzi o poufność, ani Ente, ani żadna strona trzecia nie ma dostępu do Twoich sekretów 2FA. Nawet metadane (tagi, notatki, nazwy usług) są szyfrowane przed wysłaniem. Ta architektura zero-knowledge zapewnia, że tylko Ty możesz odszyfrować swoje kody.



### Użycie offline



Synchronizacja wymaga Internetu, ale Ente Auth działa doskonale w trybie offline na każdym urządzeniu, ponieważ wszystkie dane są przechowywane lokalnie. Zmiany w trybie offline są kolejkowane i synchronizowane natychmiast po przywróceniu połączenia.



## Bezpieczeństwo i prywatność



### Gwarancje kryptograficzne



Ente Auth opiera się na solidnym szyfrowaniu end-to-end z architekturą zero-knowledge. Twoje kody są szyfrowane za pomocą klucza, który posiadasz tylko Ty, pochodzącego z Twojego hasła głównego przy użyciu zaawansowanych funkcji wyprowadzania klucza.



**Architektura zerowej wiedzy:** Ente nie ma fizycznego dostępu do danych użytkownika. Nawet metadane (nazwy usług, tagi, notatki) są szyfrowane po stronie klienta przed transmisją. Takie podejście gwarantuje, że w przypadku ataku na serwery lub żądania władz, Ente może ujawnić tylko zaszyfrowane dane, których nie można odczytać bez hasła użytkownika.



**Szyfrowanie lokalne**: Proces szyfrowania odbywa się w całości na urządzeniu przed wysłaniem danych do chmury. Serwery Ente odbierają i przechowują tylko zaszyfrowane dane, uniemożliwiając nieautoryzowany dostęp, nawet administratorom usług.



### Przejrzystość i audyty



Ponieważ kod jest [open source](https://github.com/ente-io/auth), społeczność może zweryfikować brak backdoorów. Ente zostało poddane [wielokrotnym audytom zewnętrznym](https://ente.io/blog/cryptography-audit/) w celu zweryfikowania bezpieczeństwa jego implementacji:





- **Cure53** (Niemcy): Audyt aplikacji i bezpieczeństwa kryptograficznego
- **Symbolic Software** (Francja): Specjalistyczna wiedza kryptograficzna
- **Fallible** (Indie): Testy penetracyjne i analiza podatności



Te niezależne audyty, przeprowadzone przez uznane firmy, gwarantują, że implementacja kryptograficzna Ente Auth jest zgodna z najlepszymi praktykami bezpieczeństwa i nie ma krytycznych wad.



### Polityka prywatności



Ente Auth stosuje [przykładową politykę prywatności](https://ente.io/privacy/) opartą na minimalnym gromadzeniu danych. Przechowywane są tylko informacje ściśle niezbędne do działania usługi: adres e-mail Address do uwierzytelniania i odzyskiwania konta.



**Brak śledzenia lub telemetrii**: W przeciwieństwie do większości aplikacji, Ente Auth nie gromadzi żadnych wskaźników użytkowania, danych identyfikujących awarie ani informacji behawioralnych. Aplikacja działa bez natrętnych reklam lub modułów śledzących.



**Zgodność z RODO**: Ente w pełni przestrzega europejskiego ogólnego rozporządzenia o ochronie danych. Użytkownik ma prawo do wglądu, poprawienia lub usunięcia swoich danych w dowolnym momencie. Eksport danych](https://ente.io/take-control/) to tylko jedno kliknięcie, a trwałe usunięcie konta usuwa wszystkie dane z serwerów.



**Zdecentralizowane, bezpieczne przechowywanie danych**: Twoje zaszyfrowane dane są replikowane u 3 różnych dostawców, w 3 różnych krajach, gwarantując optymalną dostępność przy jednoczesnym uniknięciu zależności od jednego dostawcy chmury.



Model biznesowy Ente opiera się na płatnej usłudze Ente Photos, umożliwiając nam oferowanie Ente Auth **bez opłat i bez ograniczeń** bez narażania prywatności użytkownika poprzez monetyzację jego danych. Takie podejście gwarantuje stabilność usługi bez polegania na reklamach lub odsprzedaży danych osobowych.



## Porównanie z innymi rozwiązaniami



| Application              | Open Source | Sauvegarde Cloud | E2EE | Sync multi-devices | Plateformes                                        |
| ------------------------ | ----------- | ---------------- | ---- | ------------------ | -------------------------------------------------- |
| **Ente Auth**            | ✅           | ✅                | ✅    | ✅                  | Android, iOS, Linux, macOS, Windows                |
| **Google Authenticator** | ❌           | ✅ (sans E2EE)    | ❌    | ✅                  | Android, iOS                                       |
| **Aegis**                | ✅           | ❌                | ✅    | ❌                  | Android                                            |
| **Authy**                | ❌           | ✅                | ❌    | ✅                  | Android, iOS *(apps desktop supprimées août 2024)* |
| **Proton Auth**          | ✅           | ✅                | ✅    | ✅                  | Android, iOS *(récent, moins établi)*              |

Ente Auth wyróżnia się jako jedno z niewielu rozwiązań łączących wszystkie zalety: przejrzystość kodu źródłowego, szyfrowane kopie zapasowe w chmurze i synchronizację między platformami.



## Zalecane przypadki użycia



### Użytkownicy indywidualni



Ente Auth jest idealnym rozwiązaniem dla osób dbających o bezpieczeństwo, które systematycznie aktywują 2FA. Nie będziesz już musiał martwić się o utratę kodów podczas zmiany telefonu lub konieczność wyboru między wygodą a bezpieczeństwem.



### Użytkowanie rodzinne i na wielu urządzeniach



Aplikacja jest przydatna, jeśli korzystasz z kilku urządzeń. Możesz zapisywać swoje kody na smartfonach i tabletach lub synchronicznie i bezpiecznie udostępniać określone kody rodzinne (Netflix, chmura rodzinna).



### Zastosowanie profesjonalne



Dla zespołów zarządzających wrażliwymi kontami, Ente Auth ułatwia współpracę przy jednoczesnym zachowaniu bezpieczeństwa, dzięki zaawansowanym funkcjom udostępniania zintegrowanym z sekcją "Organizacja i zarządzanie".



## Najlepsze praktyki





- **Zachowaj kody awaryjne**: Kody odzyskiwania dostarczone przez każdą usługę należy przechowywać z dala od telefonu.





- **Użyj silnego hasła głównego**: Hasło główne Ente Auth musi być unikalne i silne, ponieważ chroni wszystkie kody.





- **Aktywuj ochronę lokalną**: Skonfiguruj kod PIN lub dane biometryczne, aby zapobiec nieautoryzowanemu dostępowi fizycznemu.





- **Nie należy nadmiernie dostosowywać**: Unikaj zaawansowanych modyfikacji, które mogą zagrozić synchronizacji.





- **Aktualizuj aplikację**: Aktualizacje usuwają luki w zabezpieczeniach i poprawiają funkcjonalność.





- **Test przywracania**: Od czasu do czasu sprawdź, czy możesz przywrócić swoje kody na innym urządzeniu.



## Wnioski



Ente Auth to nowoczesne, kompleksowe rozwiązanie do uwierzytelniania dwuskładnikowego. Łącząc bezpieczeństwo, przejrzystość i łatwość użytkowania, ta aplikacja open source spełnia potrzeby wymagających użytkowników bez poświęcania wygody.



W przeciwieństwie do zastrzeżonych rozwiązań, które zamykają użytkownika w nieprzejrzystym ekosystemie, Ente Auth zapewnia kontrolę nad danymi uwierzytelniającymi, jednocześnie chroniąc przed przypadkową utratą dzięki szyfrowanym kopiom zapasowym.



Niezależnie od tego, czy jesteś osobą fizyczną, która chce zabezpieczyć swoje konta osobiste, czy zespołem zarządzającym dostępem biznesowym, Ente Auth to mądry wybór, aby zmodernizować swoje podejście do bezpieczeństwa cyfrowego bez narażania prywatności.



## Zasoby i wsparcie



### Oficjalna dokumentacja




- **Oficjalna strona internetowa**: [ente.io/auth](https://ente.io/auth)
- **Centrum pomocy**: [help.ente.io/auth](https://help.ente.io/auth)
- **Blog techniczny**: [ente.io/blog](https://ente.io/blog)



### Kod źródłowy i przejrzystość




- **GitHub**: [github.com/ente-io/auth](https://github.com/ente-io/auth)
- **Audyt kryptografii**: [ente.io/blog/cryptography-audit](https://ente.io/blog/cryptography-audit)



### Wspólnota




- **Discord**: [discord.gg/z2YVKkycX3](https://discord.gg/z2YVKkycX3)
- **Reddit**: [r/enteio](https://reddit.com/r/enteio)