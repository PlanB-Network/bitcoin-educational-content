---
name: Proton Authenticator
description: Jak mogę użyć Proton Authenticator do zabezpieczenia moich kont za pomocą 2FA?
---
![cover](assets/cover.webp)



Uwierzytelnianie dwuskładnikowe (2FA) dodaje dodatkową barierę bezpieczeństwa do kont, wymagając, oprócz hasła, dodatkowego dowodu, że tylko Ty je posiadasz. Włączenie 2FA drastycznie zmniejsza ryzyko włamania, nawet jeśli hasło zostanie naruszone w wyniku phishingu lub wycieku danych. Bez 2FA atakujący potrzebowałby tylko hasła, aby uzyskać dostęp do kont; z 2FA potrzebowałby również drugiego czynnika, udaremniając większość prób kradzieży konta.



Istnieją różne rodzaje 2FA. Kody SMS są lepsze niż nic, ale pozostają podatne na ataki polegające na zamianie kart SIM i przechwytywaniu. Nie zalecamy SMS-ów jako podstawowego 2FA. Aplikacje uwierzytelniające (TOTP) generate tymczasowe kody lokalnie na urządzeniu, co znacznie utrudnia ich przechwycenie. Fizyczne klucze bezpieczeństwa zapewniają najlepsze bezpieczeństwo, ale wymagają dedykowanego sprzętu.



Proton Authenticator jest aplikacją uwierzytelniającą TOTP. Jest to odpowiedź firmy Proton na ograniczenia istniejących aplikacji: wiele z nich jest zastrzeżonych, zawiera elementy śledzące reklamy i nie oferuje szyfrowanych kopii zapasowych. Proton Authenticator wyróżnia się tym, że zapewnia aplikację open source, wolną od reklam i trackerów, z szyfrowaną kopią zapasową end-to-end.



## Przedstawiamy Proton Authenticator



Proton Authenticator to mobilna i stacjonarna aplikacja do uwierzytelniania TOTP opracowana przez firmę Proton, znaną z usług skoncentrowanych na prywatności. Podobnie jak wszystkie produkty Proton, aplikacja jest open source i przeszła niezależne audyty bezpieczeństwa. Jest dostępna bezpłatnie na wszystkich platformach (Android, iOS, Windows, macOS, Linux).



Proton Authenticator oferuje następujące kluczowe funkcje:





- Generowanie kodów TOTP** dla kont 2FA, kompatybilnych z większością witryn korzystających z Google Authenticator, Authy itp.





- Opcjonalna szyfrowana kopia zapasowa w chmurze**: możesz połączyć aplikację ze swoim kontem Proton, aby tworzyć kopie zapasowe i synchronizować kody z szyfrowaniem typu end-to-end. W przypadku utraty urządzenia wystarczy podłączyć nowe, aby przywrócić wszystkie kody.





- Synchronizacja z wieloma urządzeniami**: logując się do aplikacji Proton, kody 2FA są automatycznie synchronizowane między wieloma urządzeniami za pomocą szyfrowania end-to-end. W systemie iOS alternatywą jest synchronizacja przez iCloud.





- Lokalna blokada hasłem lub danymi biometrycznymi**: aplikacja oferuje blokadę kodem PIN i/lub odciskiem palca/identyfikatorem twarzy. Więc nawet jeśli ktoś fizycznie uzyska dostęp do odblokowanego telefonu, nie będzie w stanie otworzyć Proton Authenticator.





- Brak gromadzenia danych lub urządzeń śledzących**: Proton zobowiązuje się nie gromadzić żadnych danych osobowych za pośrednictwem aplikacji. Nie ma ukrytych reklam ani analizy behawioralnej.





- Łatwy import/eksport**: jedną z mocnych stron Proton Authenticator jest kreator importu istniejących kont, kompatybilny z innymi aplikacjami (Google Authenticator, Authy, Aegis itp.). W razie potrzeby można również wyeksportować kody do pliku.



Krótko mówiąc, Proton Authenticator ma być bezkompromisowym rozwiązaniem 2FA: bezpiecznym, prywatnym i elastycznym.



## Instalacja



Proton Authenticator jest dostępny bezpłatnie na wszystkich platformach. Aby pobrać aplikację, należy przejść na oficjalną stronę: [https://proton.me/fr/authenticator/download](https://proton.me/fr/authenticator/download)



![PROTON AUTHENTICATOR](assets/fr/01.webp)



*Oficjalna strona Proton Authenticator przedstawiająca główne funkcje aplikacji i Interface*



Na tej stronie znajdziesz linki do pobrania dla wszystkich systemów operacyjnych: Android, iOS, Windows, macOS i Linux. Wystarczy kliknąć na wybrany system operacyjny i postępować zgodnie ze standardowymi krokami instalacji.



W tym samouczku pokażemy, jak zainstalować i skonfigurować aplikację na macOS, a następnie przyjrzymy się, jak zainstalować aplikację na iOS i zsynchronizować kody między dwoma urządzeniami.



### Instalacja na macOS



Po pobraniu i zainstalowaniu aplikacji należy uruchomić Proton Authenticator. Przy pierwszym uruchomieniu aplikacja poprowadzi Cię przez kilka początkowych ekranów konfiguracji:



![PROTON AUTHENTICATOR](assets/fr/02.webp)



*Ekran powitalny Proton Authenticator z komunikatem "Bezpieczeństwo w każdym kodzie" i przyciskiem "Rozpocznij "*



### Początkowy import



Jeśli Proton Authenticator wykryje, że wcześniej korzystałeś z innej aplikacji 2FA, może pojawić się kreator importu. Obsługuje on bezpośredni import z niektórych aplikacji (Google Authenticator, 2FAS, Authy, Aegis itp.). Alternatywnie możesz pominąć ten krok i dodać swoje konta ręcznie później.



![PROTON AUTHENTICATOR](assets/fr/03.webp)



*Kreator importu do przesyłania kodów z innych aplikacji uwierzytelniających*



![PROTON AUTHENTICATOR](assets/fr/04.webp)



*Kompatybilne aplikacje importujące: 2FAS, Aegis Authenticator, Authy, Bitwarden Authenticator, Ente Auth i Google Authenticator*



### Lokalna ochrona aplikacji



Ustaw kod odblokowujący PIN lub włącz odblokowywanie biometryczne (Touch ID), jeśli jest dostępne. Ten krok ma kluczowe znaczenie, aby uniemożliwić komukolwiek korzystającemu z komputera Mac uzyskanie bezpłatnego dostępu do kodów 2FA.



![PROTON AUTHENTICATOR](assets/fr/05.webp)



*Ekran konfiguracji Touch ID z komunikatem "Chroń swoje dane" i przyciskiem "Aktywuj Touch ID "*



### Opcje synchronizacji



Aplikacja pozwala również aktywować synchronizację iCloud, aby bezpiecznie tworzyć kopie zapasowe danych między urządzeniami Apple.



![PROTON AUTHENTICATOR](assets/fr/06.webp)



*Opcja synchronizacji ICloud z komunikatem "Bezpiecznie twórz kopie zapasowe danych dzięki szyfrowanej synchronizacji iCloud "*



Po wykonaniu tych kroków Proton Authenticator jest gotowy do użycia.



![PROTON AUTHENTICATOR](assets/fr/07.webp)



*Interface główny pusty Proton Authenticator z opcjami "Utwórz nowy kod" i "Importuj kody "*



## Dodaj konto 2FA za pomocą ProtonMail



Przyjrzymy się teraz, jak dodać swój pierwszy kod 2FA na przykładzie ProtonMail. Metoda ta działa identycznie dla wszystkich usług obsługujących uwierzytelnianie dwuskładnikowe.



### Włącz 2FA w ProtonMail



Po pierwsze, możesz zapoznać się z naszym przewodnikiem po ProtonMail, aby uzyskać więcej informacji:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

Zaloguj się na swoje konto ProtonMail i przejdź do ustawień bezpieczeństwa. Poszukaj opcji "Uwierzytelnianie dwuskładnikowe" i aktywuj ją.



![PROTON AUTHENTICATOR](assets/fr/08.webp)



*Strona ustawień ProtonMail z opcją "Authenticator app" w sekcji "Two-factor authentication "*



Kliknij przycisk, aby aktywować uwierzytelniacz, a ProtonMail wyświetli monit o wybranie aplikacji uwierzytelniającej.



![PROTON AUTHENTICATOR](assets/fr/09.webp)



*Okno konfiguracji ProtonMail 2FA z przyciskami "Anuluj" i "Dalej "*



ProtonMail wyświetli kod QR, który należy zeskanować za pomocą aplikacji uwierzytelniającej.



![PROTON AUTHENTICATOR](assets/fr/10.webp)



*Kod QR ProtonMail do zeskanowania za pomocą aplikacji uwierzytelniającej, z dostępną opcją "Zamiast tego wprowadź klucz ręcznie "*



Jeśli wolisz wprowadzić klucz ręcznie, kliknij "Wprowadź klucz ręcznie", aby wyświetlić tajny klucz.



![PROTON AUTHENTICATOR](assets/fr/11.webp)



*Ręczne wprowadzanie informacji 2FA: Klucz, Interwał (30) i Cyfry (6)*



### Zeskanuj kod QR za pomocą aplikacji Proton Authenticator



W aplikacji Proton Authenticator na macOS kliknij "Utwórz nowy kod". Aplikacja oferuje kilka opcji: **Skanowanie kodu QR** lub **Wprowadzenie klucza ręcznie**.



Użyj kamery komputera Mac, aby zeskanować kod QR wyświetlany na ekranie ProtonMail. Po zeskanowaniu kodu QR zostaniesz przeniesiony do ekranu konfiguracji nowego kodu.



![PROTON AUTHENTICATOR](assets/fr/12.webp)



*Okno tworzenia nowego wpisu z tytułem (ProtonMail), tajnym, nadawcą (Proton), parametrami cyfrowymi i polami interwału*



Proton Authenticator automatycznie uzupełni informacje. Możesz dostosować nazwę, jeśli chcesz, a następnie kliknij "Zapisz".



![PROTON AUTHENTICATOR](assets/fr/13.webp)



*Kod TOTP wygenerowany dla ProtonMail (848 812) z wyświetlonym pozostałym czasem*



### Sprawdź poprawność konfiguracji



ProtonMail poprosi o wprowadzenie 6-cyfrowego kodu wygenerowanego przez Proton Authenticator, aby potwierdzić, że 2FA działa poprawnie.



![PROTON AUTHENTICATOR](assets/fr/14.webp)



*Ekran weryfikacji ProtonMail z prośbą o wprowadzenie 6-cyfrowego kodu (848812)*



Skopiuj kod z aplikacji (klikając go) i wklej go do ProtonMail, aby zakończyć aktywację.



Po zatwierdzeniu ProtonMail poprosi o pobranie kodów odzyskiwania. Ważne jest, aby zapisać je ostrożnie.



![PROTON AUTHENTICATOR](assets/fr/15.webp)



*Ekran kodów odzyskiwania ProtonMail z listą kodów ratunkowych i przyciskiem "Pobierz "*



### Kody awaryjne



Podczas dodawania konta należy zachować kody odzyskiwania dostarczone przez usługę. Większość witryn oferuje statyczne, jednorazowe kody odzyskiwania do przechowywania w bezpiecznym miejscu. Zachowaj te kody zapasowe poza Proton Authenticator, aby móc uzyskać dostęp do konta w przypadku utraty dostępu do aplikacji 2FA.



## Instalacja IOS i import kodu



Po skonfigurowaniu aplikacji Proton Authenticator na macOS, możesz również chcieć korzystać z niej na iPhonie lub iPadzie. Oto jak uzyskać kody 2FA na wielu urządzeniach.



### Pobierz aplikację na iOS



Przejdź do App Store i wyszukaj "Proton Authenticator". Pobierz i zainstaluj aplikację na swoim urządzeniu z systemem iOS.



![PROTON AUTHENTICATOR](assets/fr/16.webp)



*Proces instalacji na iOS: ekran powitalny, kreator importu, wybór kompatybilnych aplikacji i końcowy ekran "Importuj kody z Proton Authenticator "*



### Metoda 1: Eksport/Import przez plik JSON



Jeśli nie korzystasz z automatycznej synchronizacji (iCloud lub konto Proton), będziesz musiał ręcznie przenieść kody z komputera Mac na iPhone'a:



**Krok 1 - Eksport z systemu macOS** :



Na komputerze Mac otwórz aplikację Proton Authenticator i przejdź do Ustawień (ikona koła zębatego). W menu kliknij "Eksportuj".



![PROTON AUTHENTICATOR](assets/fr/17.webp)



*Menu ustawień Proton Authenticator na macOS z widoczną opcją "Eksportuj "*



![PROTON AUTHENTICATOR](assets/fr/18.webp)



*Okno eksportu z nazwą pliku "Proton_Authenticator_backup_2025" i przyciskiem "Zapisz "*



Zapisz plik JSON na komputerze Mac. Możesz wysłać go bezpieczną wiadomością e-mail lub zapisać w usłudze iCloud Drive, aby mieć do niego dostęp z iPhone'a.



**Krok 2 - Import na iOS** :



Na iPhonie zainstaluj aplikację Proton Authenticator i podczas konfiguracji wybierz opcję importowania kodów. Wybierz "Proton Authenticator" z listy i zaimportuj plik JSON.



![PROTON AUTHENTICATOR](assets/fr/19.webp)



*Proces importu w systemie iOS: Lokalizacja pliku JSON, potwierdzenie importu i ekrany konfiguracji z opcjami Face ID i iCloud*



### Metoda 2: Automatyczna synchronizacja



**Za pośrednictwem konta Proton (dla synchronizacji wieloplatformowej)** :



Jeśli nie skonfigurowałeś jeszcze konta Proton i chcesz synchronizować między różnymi systemami operacyjnymi, aplikacja wyświetli monit o utworzenie lub podłączenie konta Proton.



![PROTON AUTHENTICATOR](assets/fr/20.webp)



*Ekran synchronizacji urządzenia z prośbą o utworzenie bezpłatnego konta Proton lub połączenie z istniejącym kontem*



**Przez iCloud (tylko dla ekosystemu Apple)** :


Jeśli korzystasz tylko z urządzeń Apple, możesz wybrać synchronizację iCloud w ustawieniach aplikacji. Ta metoda automatycznie i bezpiecznie zsynchronizuje kody między wszystkimi urządzeniami Apple, bez konieczności posiadania konta Proton.



## Szyfrowane tworzenie i przywracanie kopii zapasowych



Jedną z kluczowych funkcji Proton Authenticator jest kompleksowe tworzenie kopii zapasowych kodów 2FA, dzięki czemu utrata lub zmiana urządzenia nie oznacza konieczności rozpoczynania wszystkiego od nowa.



### Kompleksowe szyfrowanie



Jeśli chodzi o szyfrowane kopie zapasowe w chmurze z Proton Authenticator, sekrety TOTP są szyfrowane lokalnie na urządzeniu przed wysłaniem na serwer Proton. Odszyfrowanie jest możliwe tylko przez użytkownika na urządzeniach połączonych z kontem Proton. Proton AG nie posiada klucza do odczytu zarejestrowanych kodów.



W systemie iOS, jeśli zdecydujesz się na iCloud zamiast konta Proton, Twoje dane będą szyfrowane zgodnie ze standardami Apple. Lokalna kopia zapasowa na Androidzie pozwala zaszyfrować plik kopii zapasowej wybranym hasłem.



### Przywrócenie w przypadku utraty



W przypadku zgubienia, kradzieży lub zmiany słuchawki:



**Z włączoną funkcją kopii zapasowej Proton**: Zainstaluj aplikację Proton Authenticator na nowym urządzeniu. Podczas początkowej konfiguracji zaloguj się na to samo konto Proton. Aplikacja natychmiast zsynchronizuje i pobierze wszystkie kody 2FA z zaszyfrowanej kopii zapasowej.



**Z kopią zapasową iCloud (iOS)**: Podłącz nowego iPhone'a/iPada z tym samym Apple ID i upewnij się, że aktywowałeś iCloud Keychain. Po zainstalowaniu Proton Authenticator, połącz się z iCloud. Twoje kody powinny zsynchronizować się przez iCloud i pojawić się.



**Brak kopii zapasowej w chmurze**: Konieczne będzie ręczne zaimportowanie kont. Jeśli wyeksportowałeś plik kopii zapasowej, użyj funkcji Importuj w Proton Authenticator. W najgorszym przypadku, jeśli nie masz kopii zapasowej, musisz użyć kodów zapasowych dla każdej usługi lub skontaktować się z pomocą techniczną.



Proton Authenticator umożliwia eksportowanie kont w dowolnym momencie, w postaci zaszyfrowanego pliku lub kodu QR dla wielu kont. Opcje te zapewniają dodatkowe bezpieczeństwo.



## Najlepsze praktyki



Korzystanie z uwierzytelniania 2FA znacznie zwiększa bezpieczeństwo, ale należy przestrzegać pewnych najlepszych praktyk:



### Zapisywanie kodów awaryjnych



Kiedy aktywujesz 2FA w usłudze, często otrzymujesz listę kodów odzyskiwania. Przechowuj je poza telefonem (na papierze, w zaszyfrowanym menedżerze haseł itp.). W przypadku całkowitej utraty urządzenia uwierzytelniającego, te statyczne kody uratują Cię.



### Nie mieszaj swoich haseł i kodów 2FA



Kuszące jest korzystanie z menedżera haseł, który przechowuje również TOTP. Jednak przechowywanie hasła i kodu 2FA w tym samym miejscu tworzy pojedynczy punkt awarii i osłabia podwójne uwierzytelnianie. Aby zapewnić maksymalne bezpieczeństwo, wielu ekspertów zaleca rozdzielenie tych dwóch czynników: haseł w bezpiecznym menedżerze i kodów 2FA w oddzielnej aplikacji, takiej jak Proton Authenticator. Jednak korzystanie ze zintegrowanego menedżera jest nadal lepsze niż brak 2FA w ogóle.



### Aktywuj kilka metod 2FA



Najlepiej używać więcej niż jednego drugiego czynnika na krytycznych kontach. Nie wahaj się dodać fizycznego klucza bezpieczeństwa, jeśli usługa na to pozwala. Więcej informacji można znaleźć w naszym samouczku na temat fizycznych kluczy Yubikey:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

Podobnie, należy mieć pod ręką wydrukowane kody awaryjne.



### Zachowaj dyskrecję i chroń swoje urządzenie



Nie pozwól nikomu przeszukiwać odblokowanego telefonu. Dzięki Proton Authenticator kody są chronione kodem PIN/biometrycznym - nie ujawniaj tego kodu PIN. Podobnie, uważaj na phishing: nawet z 2FA, jeśli podasz kod do fałszywej strony w czasie rzeczywistym, może on zostać wykorzystany przez atakującego.



### Aktualizacje i audyty



Aktualizowanie Proton Authenticator (aktualizacje poprawiają ewentualne błędy). Ponieważ kod jest otwarty, społeczność przeprowadza nieformalne audyty, a Proton publikuje wyniki formalnych audytów.



## Porównanie z innymi aplikacjami



Jak wypada Proton Authenticator na tle innych aplikacji uwierzytelniających? Oto podsumowanie porównawcze:



**Proton Authenticator**: Open source, opcjonalne szyfrowane kopie zapasowe E2EE w chmurze, synchronizacja z wieloma urządzeniami, blokada lokalna, brak śledzenia, dostępne na urządzeniach mobilnych i komputerach stacjonarnych.



**Google Authenticator**: Zastrzeżone, tworzenie kopii zapasowych za pośrednictwem konta Google od 2023 r., ale bez szyfrowania end-to-end (klucze mogą być widoczne dla Google), synchronizacja wielu urządzeń dodana w 2023 r., domyślnie brak blokady aplikacji, zawiera trackery Google.



**Aegis Authenticator**: Open source, tylko lokalna kopia zapasowa, brak synchronizacji w chmurze, blokada kodowa/biometryczna, brak śledzenia, tylko Android.



**Authy**: Zastrzeżona, szyfrowana hasłem kopia zapasowa w chmurze, ale zamknięty kod, synchronizacja wielu urządzeń, blokada PIN / odcisk palca, gromadzi numer telefonu, aplikacja desktopowa wycofana w marcu 2024 r.



Poniżej znajduje się nasz przewodnik po Authy:



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Proton Authenticator to jedno z najbardziej wszechstronnych i bezpiecznych rozwiązań dostępnych na rynku: open source, szyfrowana synchronizacja wielu urządzeń, brak komercyjnych działań następczych.



## Zasoby i wsparcie



### Oficjalna dokumentacja




- Oficjalna strona internetowa**: [proton.me/authenticator](https://proton.me/authenticator) - Prezentacja produktu i pliki do pobrania
- Strona pobierania**: [proton.me/en/authenticator/download](https://proton.me/fr/authenticator/download) - Linki dla wszystkich systemów operacyjnych
- Wsparcie Proton**: [proton.me/support/two-factor-authentication-2fa](https://proton.me/support/two-factor-authentication-2fa) - Oficjalny przewodnik aktywacji 2FA
- Blog Proton**: [proton.me/blog/authenticator-app](https://proton.me/blog/authenticator-app) - Zapowiedź i szczegółowe funkcje



### Kod źródłowy i przejrzystość




- GitHub Proton Authenticator** : [github.com/ProtonMail/proton-authenticator](https://github.com/ProtonMail/proton-authenticator) - kod open source
- Audyty bezpieczeństwa**: [proton.me/community/security-audits](https://proton.me/community/security-audits) - Niezależne raporty z audytów



### Zalecane testy bezpieczeństwa


Po skonfigurowaniu przetestuj swoją konfigurację:




- [Have I Been Pwned](https://haveibeenpwned.com/) - Sprawdź, czy Twoje konta zostały przejęte
- [2FA Directory](https://2fa.directory/) - Lista usług obsługujących 2FA



### Społeczności i dyskusje




- Reddit r/Proton** : [reddit.com/r/ProtonMail](https://reddit.com/r/ProtonMail) - Oficjalna społeczność Protona
- Forum Privacy Guides** : [discuss.privacyguides.net](https://discuss.privacyguides.net) - Dyskusje techniczne na temat prywatności
- Reddit r/privacy**: [reddit.com/r/privacy](https://reddit.com/r/privacy) - Ogólne wskazówki dotyczące prywatności



### Inne




- [Have I Been Pwned](https://haveibeenpwned.com/) - Sprawdź, czy Twoje konta zostały przejęte
- [2FA Directory](https://2fa.directory/) - Lista usług obsługujących 2FA