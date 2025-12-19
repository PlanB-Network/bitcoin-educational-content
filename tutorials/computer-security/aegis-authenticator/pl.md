---
name: Aegis Authenticator
description: Jak używać Aegis Authenticator do zabezpieczania kont za pomocą podwójnego uwierzytelniania?
---

![cover](assets/cover.webp)



Obecnie uwierzytelnianie dwuskładnikowe (2FA) jest niezbędne do zabezpieczenia kont internetowych. Oprócz hasła dodaje ono drugi czynnik (często 6-cyfrowy kod), który wygasa po 30 sekundach, co znacznie utrudnia zadanie hakerom. Korzystanie z dedykowanej aplikacji TOTP (*Time-based One-Time Password*) jest bezpieczniejsze niż SMS-y, które mogą zostać przejęte przez ataki polegające na zamianie kart SIM.



Jednak nie wszystkie aplikacje uwierzytelniające są sobie równe. Wiele zastrzeżonych rozwiązań (Google Authenticator, Authy itp.) stwarza problemy: są one zastrzeżone i zamknięte (niemożliwe jest przeprowadzenie audytu ich bezpieczeństwa), czasami integrują trackery reklamowe, nie oferują szyfrowanych kopii zapasowych kodów, a nawet mogą uniemożliwić eksportowanie kont, aby zablokować Cię w ich ekosystemie.



Z drugiej strony, Aegis Authenticator przedstawia się jako darmowa i etyczna alternatywa dla tych aplikacji. Aegis to darmowa, bezpieczna aplikacja typu open-source do zarządzania tokenami weryfikacji dwuetapowej w systemie Android. Jej rozwój koncentruje się na podstawowych funkcjach, których nie oferują inne aplikacje, w tym na solidnym szyfrowaniu danych lokalnych i możliwości bezpiecznego tworzenia kopii zapasowych. Podsumowując, Aegis oferuje lokalne, kontrolowane rozwiązanie podwójnego uwierzytelniania, idealne dla każdego, kto chce zachować pełną kontrolę nad swoimi kodami 2FA.



## Przedstawiamy Aegis Authenticator



Aegis Authenticator to aplikacja 2FA o otwartym kodzie źródłowym dla systemu Android, wydana na licencji GPL v3. Wyróżnia się ona filozofią "privacy by design": aplikacja działa całkowicie offline i nie wymaga połączenia ze zdalną usługą. W rezultacie tokeny pozostają przechowywane lokalnie na urządzeniu, w bezpiecznym sejfie, do którego tylko ty posiadasz klucz.



### Najważniejsze cechy



**Szyfrowany sejf:** wszystkie kody OTP są przechowywane w szyfrowanym sejfie AES-256 (tryb GCM), chronionym hasłem głównym zdefiniowanym przez użytkownika. Możesz odblokować ten sejf za pomocą hasła lub danych biometrycznych (odcisk palca, rozpoznawanie twarzy) dla dodatkowej wygody. W przypadku braku hasła dane byłyby niezaszyfrowane, dlatego zdecydowanie zalecamy jego ustawienie.



**Zaawansowana organizacja:** Aegis zapewnia dobrą organizację wielu kont 2FA. Możesz sortować wpisy alfabetycznie lub w wybranej kolejności, grupować je według kategorii (np. Osobiste, Praca, Społecznościowe) w celu łatwego wyszukiwania i przypisywać każdemu wpisowi spersonalizowaną ikonę. Dostępny jest również pasek wyszukiwania, który umożliwia natychmiastowe znalezienie usługi lub konta według nazwy.



**Szyfrowane lokalne kopie zapasowe:** Aby nigdy nie utracić dostępu do swoich kont, Aegis oferuje automatyczne tworzenie kopii zapasowych sejfu. Są one szyfrowane (za pomocą hasła) i mogą być zapisywane w wybranej lokalizacji (pamięć wewnętrzna, folder w chmurze itp.). Aplikacja może również ręcznie wyeksportować bazę danych konta w formacie zaszyfrowanym lub niezaszyfrowanym, w zależności od potrzeb. Importowanie kont z innych aplikacji 2FA jest równie łatwe (Aegis obsługuje import z Authy, Google Authenticator, FreeOTP, andOTP itp.)



**Bezpieczeństwo i prywatność:** Aplikacja domyślnie działa w trybie offline. Nie wymaga żadnych uprawnień sieciowych - co oznacza, że nie przesyła żadnych danych do świata zewnętrznego i nie zawiera modułów śledzących reklamy ani modułów analizy behawioralnej. Aegis nie wyświetla reklam i nie wymaga konta użytkownika: zaraz po zainstalowaniu działa bez konieczności rejestracji. Ponieważ jego kod źródłowy jest publiczny na GitHub, społeczność może go swobodnie audytować, gwarantując brak złośliwych lub ukrytych funkcji.



**Nowoczesny Interface:** Aegis przyjmuje schludny Material Design, z obsługą ciemnych motywów (w tym tryb AMOLED), a nawet opcjonalnym widokiem kafelków, aby wyświetlać kody jako siatki. Interface jest uporządkowany, bez zbędnych dodatków i zapobiega przechwytywaniu kodów z ekranu jako środek bezpieczeństwa.



## Instalacja



Ponieważ Aegis Authenticator jest oprogramowaniem typu open source, jego twórcy preferują przyjazne dla prywatności kanały dystrybucji. Istnieją dwa główne sposoby jego instalacji:



### Przez F-Droid (zalecane)



Najbezpieczniejszym i najłatwiejszym sposobem jest skorzystanie z F-Droid, darmowego alternatywnego sklepu. Jeśli F-Droid nie jest jeszcze zainstalowany na Twoim telefonie, zacznij od pobrania go z oficjalnej strony [F-Droid.org](https://f-droid.org). Następnie :





- Otwórz F-Droid i upewnij się, że zaktualizowałeś swoje repozytoria, aby uzyskać najnowszą listę aplikacji
- Wyszukaj "Aegis Authenticator" w aplikacji F-Droid. Powinna pojawić się oficjalna aplikacja (wydawca: Beem Development)
- Rozpocznij instalację, naciskając Install. Ponieważ Aegis jest jedną z aplikacji zweryfikowanych przez F-Droid, możesz cieszyć się niezawodnym i bezpiecznym pobieraniem



Instalacja za pośrednictwem F-Droid oferuje zaletę otrzymywania automatycznych aktualizacji aplikacji, gdy tylko zostaną one wydane. Co więcej, F-Droid gwarantuje, że aplikacja jest wolna od niechcianych zastrzeżonych komponentów.



### Przez GitHub (podpisany APK)



Jeśli wolisz zainstalować aplikację bez przechodzenia przez sklep, możesz pobrać oficjalny APK bezpośrednio ze strony GitHub projektu. W repozytorium Aegis ([github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis)) należy przejść do sekcji Releases, gdzie publikowane są stabilne wersje.





- Pobierz najnowszą wersję APK
- Przed instalacją APK upewnij się, że autoryzowałeś instalację aplikacji z nieznanych źródeł na swoim urządzeniu (w Ustawieniach Androida)
- APK udostępniony na GitHub jest podpisany przez dewelopera tym samym kluczem, co na F-Droid



Po ręcznej instalacji aplikacja będzie działać identycznie. Należy pamiętać, że aktualizacje nie będą automatyczne: należy okresowo sprawdzać GitHub w poszukiwaniu nowych wersji.



### Sklep Google Play vs F-Droid



Aegis Authenticator jest dostępny zarówno w Google Play Store, jak i F-Droid, co daje możliwość wyboru metody instalacji:



**Sklep Google Play:**




- automatyczne aktualizacje zintegrowane z systemem Android
- prosta, znajoma instalacja
- taki sam podpisany plik APK jak na innych kanałach



**F-Droid (zalecane) :**




- darmowy i otwarty sklep
- powtarzalna i weryfikowalna konstrukcja
- nie jest wymagana usługa Google
- ✅ Szacunek dla filozofii wolnego oprogramowania



Wybór między tymi dwiema opcjami zależy od preferencji dotyczących ekosystemu Google. Jeśli wolisz prostotę, Sklep Play jest idealny. Jeśli chcesz bardziej przyjaznego dla prywatności podejścia, niezależnego od usług Google, F-Droid jest lepszym wyborem.



## Pierwsza konfiguracja



Gdy Aegis jest uruchamiany po raz pierwszy, proponowana jest wstępna procedura konfiguracji w celu zabezpieczenia kodu 2FA:



![Configuration initiale Aegis](assets/fr/01.webp)



*Początkowy proces konfiguracji Aegis: ekran powitalny, wybór zabezpieczeń, definicja hasła głównego i finalizacja*



### Ustawianie hasła głównego



Aegis najpierw poprosi o wybranie hasła głównego. Hasło to będzie używane do szyfrowania wszystkich tokenów uwierzytelniających przechowywanych w skarbcu. Zdecydowanie zalecamy ustawienie silnego, unikalnego hasła, które będzie znane tylko tobie.



**Ostrzeżenie:** nie zapomnij tego hasła - jeśli je zgubisz, zaszyfrowane kody 2FA staną się niedostępne (nie ma tylnego wejścia). Aegis poprosi o dwukrotne wprowadzenie hasła w celu potwierdzenia.



### Włącz odblokowywanie biometryczne (opcjonalnie)



Jeśli urządzenie z Androidem jest wyposażone w czytnik linii papilarnych lub inny czujnik biometryczny, Aegis wyświetli monit o aktywację odblokowywania biometrycznego. Opcja ta jest opcjonalna, ale bardzo praktyczna: pozwala szybko odblokować aplikację za pomocą odcisku palca lub twarzy, zamiast wpisywać hasło za każdym razem.



Należy pamiętać, że dane biometryczne są dodatkowym udogodnieniem: hasło główne jest nadal wymagane, jeśli dane biometryczne zostaną zmienione lub urządzenie zostanie ponownie uruchomione.



### Odkryj ustawienia aplikacji



Po wejściu do aplikacji (główny ekran Interface jest początkowo pusty) zapoznaj się z dostępnymi opcjami konfiguracji. Dostęp do ustawień można uzyskać za pomocą menu rozwijanego w prawym górnym rogu ekranu (trzy pionowe kropki), a następnie wybierając opcję "Ustawienia".



![Interface principale et paramètres](assets/fr/02.webp)



*Interface główny Aegis pusty przy starcie, dostęp do menu parametrów i przegląd dostępnych opcji*



Menu ustawień Aegis grupuje kilka ważnych sekcji:





- **Wygląd**: Dostosuj motyw (jasny, ciemny, AMOLED), język i inne ustawienia wizualne
- **Zachowanie**: Konfiguruje zachowanie aplikacji podczas interakcji z listą wpisów
- **Pakiety ikon**: zarządzanie i importowanie pakietów ikon w celu dostosowania wyglądu i działania kont
- **Bezpieczeństwo**: Ustawienia szyfrowania, odblokowywania biometrycznego, automatycznego blokowania i innych parametrów bezpieczeństwa
- **Kopie zapasowe**: Konfiguracja automatycznego tworzenia kopii zapasowych w wybranej lokalizacji
- **Import i eksport**: Importuj kopie zapasowe z innych aplikacji uwierzytelniających i ręcznie eksportuj swój skarbiec Aegis
- **Dziennik audytu**: Szczegółowy dziennik wszystkich istotnych zdarzeń w aplikacji



Ta przejrzysta organizacja pozwala skonfigurować Aegis zgodnie z własnymi preferencjami i potrzebami w zakresie bezpieczeństwa.



## Dodaj konto 2FA



Po skonfigurowaniu Aegis przejdźmy do podstaw: dodawania kont dwuskładnikowych. Proces ten jest prosty, a Aegis oferuje kilka metod integracji kodów uwierzytelniających.



### Trzy dostępne metody dodawania



W głównym oknie Aegis Interface naciśnij przycisk **+** w prawym dolnym rogu, aby uzyskać dostęp do opcji dodawania. Dostępne są trzy opcje:





- **Skanowanie kodu QR**: Bezpośrednie skanowanie kodu QR wyświetlanego przez usługę internetową
- **Skanuj obraz**: Skanowanie kodu QR z obrazu zapisanego na urządzeniu
- **Wprowadź ręcznie**: Wprowadź informacje o koncie 2FA ręcznie



### Praktyczny przykład: konfiguracja Bitwarden



Weźmy konkretny przykład aktywacji 2FA na Bitwarden, aby zilustrować ten proces:



![Exemple avec Bitwarden](assets/fr/04.webp)



*Przykład aktywacji 2FA na Bitwarden: Interface web z opcjami uwierzytelniania i rekomendacją Aegis*





- **Logowanie i dostęp do ustawień**: Zaloguj się na swoje konto Bitwarden i przejdź do ustawień, zakładka "Bezpieczeństwo"
- **Sekcja dostawców**: Przejdź do sekcji "Dostawcy" i kliknij "Zarządzaj" w sekcji "Aplikacja Authenticator"



![Configuration 2FA avec QR code](assets/fr/05.webp)



*Kompletny proces dodawania konta: Kod QR wyświetlony przez usługę, widoczny tajny klucz i wprowadzony kod weryfikacyjny*





- **Zeskanuj kod QR**: Otworzy się wyskakujące okienko z kodem QR i tajnym kluczem
- **W Aegis**: Użyj opcji "Skanuj kod QR", aby automatycznie przechwytywać informacje
- **Weryfikacja**: Wprowadź 6-cyfrowy kod wygenerowany przez Aegis w polu "Kod weryfikacyjny"
- **Aktywacja**: Kliknij "Włącz", aby sfinalizować aktywację



### Dodaj szczegóły ręcznie



Jeśli wolisz lub nie możesz zeskanować kodu QR, użyj opcji "Wprowadź ręcznie". Formularz umożliwia wprowadzenie :



![Ajout d'un compte 2FA](assets/fr/03.webp)



*Proces dodawania nowego konta 2FA: pusty Interface, dodanie opcji, formularz ręcznego wprowadzania danych i pomyślne dodanie konta*





- **Nazwa**: Nazwa usługi (np. Bitwarden, GitHub...)
- **Emitent**: Emitent (często identyczny z nazwą)
- **Grupa**: Opcjonalnie, aby uporządkować konta według kategorii
- **Uwaga**: Osobiste uwagi dotyczące tego konta
- **Secret**: Tajny klucz dostarczony przez usługę (domyślnie zamaskowany)
- **Zaawansowane**: Zaawansowane parametry (algorytm, okres, liczba cyfr)



Po dodaniu konta pojawi się ono na liście z aktualnym kodem i wskaźnikiem czasu pokazującym czas pozostały do odnowienia.



### Uniwersalna kompatybilność



Aegis jest kompatybilny ze wszystkimi usługami wykorzystującymi standardy TOTP i HOTP, w tym z praktycznie wszystkimi witrynami oferującymi 2FA: sieciami społecznościowymi, bankami, menedżerami haseł, platformami kryptograficznymi itp.



### Organizacja wejścia



Po dodaniu kilku kont docenisz narzędzia organizacyjne Aegis:





- **Sortowanie niestandardowe:** Domyślnie konta są wyświetlane w kolejności alfabetycznej, ale można zmienić kolejność ręcznie
- **Grupy i kategorie:** Utwórz grupy, aby oddzielić konta osobiste od kont firmowych lub pogrupuj je według rodzaju usługi (bankowość, poczta e-mail, sieci społecznościowe itp.)
- **Niestandardowe ikony:** Aegis próbuje automatycznie przypisać odpowiednią ikonę, jeśli jest dostępna, w przeciwnym razie można wybrać jedną z wielu ogólnych ikon lub zaimportować obraz
- **Szybkie wyszukiwanie:** Pasek wyszukiwania u góry pozwala wpisać kilka liter, aby natychmiast odfiltrować pasujące wpisy



Dotykając wpisu, kod OTP jest wyświetlany w pełnym rozmiarze (jeśli był ukryty) i można go skopiować do schowka długim naciśnięciem - przydatne do wklejenia go do aplikacji, z którą chcesz się połączyć.



## Bezpieczeństwo i kopie zapasowe



Ze względu na to, że bezpieczeństwo jest podstawą Aegis, ważne jest, aby zrozumieć, w jaki sposób chronione są kody 2FA i jak zapewnić ich trwałość w przypadku wystąpienia problemu.



### Architektura zabezpieczeń



**Niezawodne szyfrowanie**: Wszystkie kody są przechowywane w zaszyfrowanym sejfie przy użyciu algorytmu **AES-256 w trybie GCM**, w połączeniu z hasłem głównym. Wyznaczanie klucza opiera się na **scrypt**, oferując zwiększoną ochronę przed atakami typu brute-force.



**Bezpieczne odblokowanie** : Do odszyfrowania danych wymagane jest hasło główne. Biometria (opcjonalnie) wykorzystuje **Android Secure Keystore** i TEE (Trusted Execution Environment) do ochrony klucza szyfrowania.



**Minimalne uprawnienia**: Aegis domyślnie działa w trybie offline, wymagając jedynie dostępu do kamery (skanowanie QR), danych biometrycznych i wibratora. Żadne dane nie są gromadzone ani udostępniane.



### Opcje tworzenia kopii zapasowych



Aegis oferuje kilka strategii tworzenia kopii zapasowych, aby zaspokoić różne potrzeby w zakresie bezpieczeństwa i wygody:



![Configuration des sauvegardes](assets/fr/06.webp)



*Interface z dodanym kontem, alertem kopii zapasowej, ustawieniami automatycznej kopii zapasowej i strategiami tworzenia kopii zapasowych*



**1. Automatyczne lokalne kopie zapasowe**




- Skonfiguruj wybrany folder docelowy
- Konfigurowalna częstotliwość (po każdej zmianie, codziennie itp.)
- Zaszyfrowane pliki chronione hasłem (.aesvault)
- Zgodność z folderami zsynchronizowanymi (Nextcloud, Dropbox itp.)



![Sélection du dossier de sauvegarde](assets/fr/07.webp)



*Proces wyboru folderu kopii zapasowej: eksplorator plików, folder docelowy i autoryzacja dostępu*



**2. Kopie zapasowe w chmurze Android**




- Opcjonalna integracja z systemem kopii zapasowych Android
- Dostępne tylko dla szyfrowanych sejfów (bezpieczeństwo zachowane)
- Przejrzysta kopia zapasowa z innymi danymi Androida
- Automatyczne przywracanie przy zmianie urządzenia



**3. Eksport ręczny**




- Eksport na żądanie poprzez **Ustawienia > Import i Eksport**
- Wybór formatu szyfrowanego (zalecane) lub jawnego
- Przydatne w przypadku migracji lub okazjonalnych kopii zapasowych



### Dobre praktyki bezpieczeństwa





- Zachowaj kilka wersji kopii zapasowych, aby zapobiec uszkodzeniu
- Regularnie testuj **swoje kopie zapasowe**, próbując je przywrócić
- Kody odzyskiwania dostarczone przez serwis należy przechowywać osobno
- **Hasło główne** jest nadal wymagane nawet w przypadku kopii zapasowych w chmurze
- **Zabezpiecz swoje hasło główne**: używaj unikalnego, silnego hasła przechowywanego w menedżerze haseł
- **Aktualizuj swoją aplikację** za pomocą najnowszych poprawek zabezpieczeń
- Aktywuj **automatyczną blokadę** w ustawieniach, aby zabezpieczyć dostęp do aplikacji
- Wyłącz **zrzuty ekranu** (opcja domyślna), aby zapobiec przechwytywaniu kodów
- **Oszczędne korzystanie z danych biometrycznych**: preferowanie haseł dla krytycznych dostępów



## Porównanie z innymi aplikacjami



Jak Aegis wypada na tle innych popularnych aplikacji uwierzytelniających?



### Aegis vs Google Authenticator



**Aegis :**




- otwarte źródło i możliwość audytu
- lokalna zaszyfrowana kopia zapasowa
- zaawansowana organizacja (grupy, ikony, wyszukiwanie)
- brak gromadzenia danych
- tylko Android



**Google Authenticator :**




- dostępne na Androida i iOS
- synchronizacja w chmurze (od 2023 r.)
- zamknięty kod źródłowy
- ograniczona funkcjonalność
- potencjalne gromadzenie danych przez Google



### Aegis vs Authy



**Aegis :**




- open source
- konto nie jest wymagane
- możliwość eksportu kodu
- całkowita kontrola danych
- brak natywnej synchronizacji z wieloma urządzeniami



**Authy :**




- synchronizacja wielu urządzeń
- dostępne na Androida i iOS
- zamknięty kod źródłowy
- wymaga podania numeru telefonu
- nie można wyeksportować kodów
- aplikacje desktopowe usunięte w marcu 2024 r



Aegis doskonale nadaje się dla użytkowników Androida, którzy cenią sobie przejrzystość, lokalne bezpieczeństwo i pełną kontrolę nad swoimi danymi. Alternatywy takie jak Authy są bardziej odpowiednie, jeśli absolutnie potrzebujesz automatycznej synchronizacji wielu urządzeń.




## Wnioski



Aegis Authenticator to doskonałe rozwiązanie dla osób poszukujących przyjaznej dla prywatności, bezpiecznej i przejrzystej aplikacji 2FA. Podejście open-source w połączeniu z solidnym szyfrowaniem i zgrabnym Interface sprawia, że jest to pierwszorzędny wybór do zabezpieczania kont online.



Mimo ograniczenia do systemu Android i braku natywnej synchronizacji w chmurze, Aegis z nawiązką nadrabia te ograniczenia filozofią "privacy by design" i całkowitą kontrolą danych. Dla użytkowników dbających o swoją cyfrową prywatność, Aegis oferuje wiarygodną i potężną alternatywę dla dominujących na rynku rozwiązań własnościowych.



Bezpieczeństwo Twoich kont online nie musi zależeć od dobrej woli firm komercyjnych. Dzięki Aegis zachowujesz kontrolę nad swoimi kodami uwierzytelniającymi w cyfrowym sejfie, do którego tylko Ty masz klucz.



## Zasoby



### Oficjalne strony internetowe




- **Oficjalna strona internetowa**: [getaegis.app](https://getaegis.app/) - Prezentacja i pobieranie aplikacji
- **Kod źródłowy**: [github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis) - Oficjalne repozytorium GitHub
- **F-Droid**: [f-droid.org/packages/com.beemdevelopment.aegis](https://f-droid.org/packages/com.beemdevelopment.aegis/) - Instalacja przez darmowy sklep



### Dokumentacja techniczna




- **Dokumentacja Vault**: [Vault design](https://github.com/beemdevelopment/Aegis/blob/master/docs/vault.md) - Opis techniczny szyfrowania i bezpiecznej architektury
- **Oficjalne FAQ**: [getaegis.app/#faq](https://getaegis.app/#faq) - Odpowiedzi na najczęściej zadawane pytania
- **Wiki projektu**: [github.com/beemdevelopment/Aegis/wiki](https://github.com/beemdevelopment/Aegis/wiki) - Pełna dokumentacja użytkownika