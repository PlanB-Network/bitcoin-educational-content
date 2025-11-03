---
name: Mullvad Browser
description: Jak korzystać z przeglądarki Mullvad Browser w celu ochrony prywatności?
---

![cover](assets/cover.webp)



W świecie, w którym nadzór cyfrowy staje się wszechobecny, ochrona prywatności w Internecie nigdy nie była tak ważna. Firmy wykorzystują zaawansowane techniki do śledzenia użytkowników:





- **Pliki cookie stron trzecich**: małe pliki umieszczane przez witryny zewnętrzne w celu podążania za użytkownikiem z jednej witryny do drugiej
- **Fingerprinting**: gromadzi unikalne cechy przeglądarki i urządzenia (rozdzielczość ekranu, zainstalowane czcionki, wtyczki itp.) w celu identyfikacji użytkownika bez plików cookie
- **Skrypty śledzące**: niewidoczne kody JavaScript, które analizują zachowanie użytkownika podczas przeglądania (kliknięcia, przewijanie, spędzony czas)
- Analiza **IP Address**: lokalizacja geograficzna i identyfikacja dostawcy usług internetowych



Dane te są następnie łączone w celu stworzenia szczegółowych profili zachowań użytkowników w Internecie i monetyzowane, często bez ich wiedzy. Ta rzeczywistość rodzi fundamentalne pytanie: w jaki sposób można surfować po Internecie, zachowując anonimowość i poufność?



Odpowiedź leży w dużej mierze w wyborze przeglądarki internetowej. To narzędzie, którego używamy każdego dnia, aby uzyskać dostęp do informacji, dokonywać zakupów lub komunikować się, odgrywa decydującą rolę w ochronie naszych danych osobowych. Niestety, popularne przeglądarki, takie jak Google Chrome (która posiada około 65% globalnego rynku), zostały zaprojektowane w oparciu o modele biznesowe oparte na masowym gromadzeniu danych użytkowników.



![MULLVAD BROWSER](assets/fr/01.webp)


*Mullvad Browser wyróżnia się wyjątkowo skutecznym blokowaniem trackerów, znacznie przewyższając przeglądarki konsumenckie*



W obliczu tego wyzwania pojawiają się nowi gracze z inną filozofią: umieszczaniem prywatności w centrum ich projektu. Wśród nich Mullvad Browser wyróżnia się jako innowacyjne rozwiązanie, które łączy najlepszą ochronę prywatności z płynnym, dostępnym przeglądaniem.



W przeciwieństwie do tradycyjnych przeglądarek, które starają się spersonalizować wrażenia użytkownika poprzez gromadzenie jego danych, Mullvad Browser przyjmuje odwrotne podejście: sprawia, że wszyscy jej użytkownicy wyglądają identycznie na stronach internetowych, co praktycznie uniemożliwia indywidualne śledzenie.



W tym samouczku wspólnie odkryjemy, w jaki sposób Mullvad Browser może zmienić sposób przeglądania Internetu, oferując solidną ochronę przed inwigilacją bez poświęcania łatwości użytkowania.




## Przedstawiamy przeglądarkę Mullvad



**Mullvad Browser** to skoncentrowana na prywatności przeglądarka internetowa opracowana we współpracy z Tor Project i dystrybuowana bezpłatnie przez szwedzką firmę Mullvad VPN. Uruchomiona w kwietniu 2023 r., przedstawia się jako **"przeglądarka Tor bez sieci Tor "**, zaprojektowana w celu zminimalizowania śledzenia online i pobierania odcisków palców, jednocześnie umożliwiając użytkownikom przeglądanie za pośrednictwem zaufanej sieci VPN, a nie sieci Tor.



Mullvad Browser to darmowa przeglądarka o otwartym kodzie źródłowym, oparta na Firefoksie ESR (długotrwałej wersji Mozilla Firefox) i wzmocniona przez ekspertów Tor Project. Konkretnie, zawiera ona większość **funkcji ochronnych przeglądarki Tor**, ale **nie kieruje ruchu przez sieć Tor**. Zamiast tego użytkownicy mogą (i powinni) połączyć ją z zaufaną szyfrowaną siecią VPN, aby zanonimizować swoje IP Address.



Pod względem doświadczenia użytkownika, Mullvad Browser przypomina klasyczną przeglądarkę, oferując płynną nawigację. Jest ona dostępna bezpłatnie w systemach Windows, macOS i Linux (brak wersji mobilnej). Aby z niej korzystać, nie trzeba być subskrybentem Mullvad VPN; jednak **używanie Mullvad Browser bez maskowania swojego IP nie zapewnia pełnej anonimowości** - dlatego zdecydowanie zaleca się korzystanie z niej w połączeniu z niezawodną siecią VPN.



### Cele: prywatność i przeciwdziałanie śledzeniu



Przeglądarka Mullvad została zaprojektowana z myślą o jednym głównym celu: **ochrona prywatności użytkowników** online i przeciwdziałanie powszechnym technikom śledzenia i profilowania. Jej główne cele obejmują:





- Znaczne ograniczenie śledzenia reklam i **śledzenia** przez strony internetowe i agencje reklamowe. Domyślnie Mullvad Browser blokuje zewnętrzne moduły śledzące, śledzące pliki cookie i skrypty odcisków palców, które mogłyby zidentyfikować użytkownika.





- Ustandaryzuj odcisk palca swojej przeglądarki, aby **"wtopić się w tłum"**. Odcisk palca jest jak unikalny "dowód osobisty" stworzony przez połączenie wszystkich cech przeglądarki. Mullvad Browser zapewnia, że wszyscy jego użytkownicy mają dokładnie taki sam "dowód osobisty", co uniemożliwia ich indywidualne rozróżnienie.





- Oferuje natychmiastową ochronę bez dodatkowych rozszerzeń. Mullvad Browser jest dostarczany w konfiguracji "gotowej do użycia": użytkownik nie musi instalować szeregu rozszerzeń ani modyfikować żadnych ustawień, aby być chronionym.





- Nie poświęcaj wydajności ani ergonomii **bardziej niż to konieczne**. W przypadku braku routingu Tor, Mullvad Browser oferuje znacznie szybsze przeglądanie niż Tor Browser, zbliżając się do wydajności standardowej przeglądarki połączonej z VPN.



### Najważniejsze funkcje przeglądarki Mullvad



Mullvad Browser zawiera szereg **funkcji bezpieczeństwa i prywatności** bezpośrednio inspirowanych przez Tor Browser:





- **Przeglądanie prywatne przez cały czas:** Tryb przeglądania prywatnego jest domyślnie włączony i nie można go wyłączyć. **Żadna historia, pliki cookie ani pamięć podręczna nie są przechowywane między sesjami**. Po zamknięciu przeglądarki Mullvad Browser wszystkie dane przeglądania są usuwane.





- **Ulepszona ochrona przed fingerprintingiem:** Przeglądarka stosuje rygorystyczne ustawienia, aby uniemożliwić cyfrowy odcisk palca. Obejmuje to:
- **Standaryzacja agenta użytkownika** i wersji przeglądarki
- Strefa czasowa ustawiona na **UTC** dla wszystkich użytkowników
- **Letterbox**: technika, która automatycznie dodaje szare marginesy wokół stron internetowych, aby ujednolicić rozmiar wyświetlania i zapobiec identyfikacji na podstawie wymiarów ekranu
- **Blokowanie API fingerprinting**: Technologie Canvas (rysowanie 2D), WebGL (grafika 3D) i AudioContext (przetwarzanie dźwięku) są wyłączone, ponieważ mogą ujawniać unikalne szczegóły dotyczące sprzętu
- **Znormalizowane czcionki systemowe** w celu uniknięcia identyfikacji przez zainstalowane czcionki





- **Blokowanie trackerów i reklam:** Mullvad Browser natywnie integruje rozszerzenie **uBlock Origin** (preinstalowane) z dodatkowymi listami ochrony w celu blokowania **zewnętrznych trackerów, skryptów reklamowych i innych złośliwych treści**. Ochronie tej towarzyszy **First-Party Isolation**: technika, która przechowuje pliki cookie w oddzielnych "pulach" dla każdej witryny, uniemożliwiając jednej witrynie odczytywanie plików cookie zdeponowanych przez inną.





- **Przycisk resetowania sesji:** Podobnie jak przycisk "Nowa tożsamość" w przeglądarce Tor Browser, Mullvad Browser oferuje przycisk do **szybkiego ponownego uruchomienia przeglądarki z nową, pustą sesją**.





- **Regulowane poziomy bezpieczeństwa:** Możesz dostosować poziom bezpieczeństwa (*Normal*, *Safer*, *Safest*) w ustawieniach, tak jak w przeglądarce Tor Browser.



## Domyślnie wbudowane rozszerzenia



Mullvad Browser zawiera **trzy preinstalowane rozszerzenia**, które stanowią rdzeń jego ochrony przed śledzeniem. **Ważne jest, aby nigdy ich nie usuwać ani nie modyfikować ich konfiguracji**, ponieważ uczyniłoby to cię wyjątkowym wśród użytkowników Mullvad Browser:



### **uBlock Origin**


To rozszerzenie do blokowania reklam i trackerów jest wstępnie skonfigurowane z **zoptymalizowanymi listami filtrów** do blokowania:




- Natrętne reklamy
- Urządzenia śledzące innych firm gromadzące dane użytkownika
- Złośliwe skrypty
- Śledzenie zachowań Elements



uBlock Origin w Mullvad Browser wykorzystuje standardowe parametry, aby zapewnić, że wszyscy użytkownicy blokują dokładnie ten sam Elements, zachowując w ten sposób jednolitość cyfrowych śladów.



### **NoScript**


NoScript działa w tle, aby zarządzać **poziomami bezpieczeństwa** przeglądarki. To:




- Kontroluje wykonywanie **JavaScript** zgodnie z wybranym poziomem (Normalny/Najbezpieczniejszy/Najbezpieczniejszy)
- Automatycznie filtruje ataki **XSS** (Cross-Site Scripting)
- Blokuje niebezpieczną **aktywną zawartość** w witrynach innych niż HTTPS
- Jego ikona jest domyślnie ukryta, ale można ją wyświetlić za pomocą opcji "Dostosuj pasek narzędzi"



### *rozszerzenie* **Mullvad Browser**


To specyficzne dla Mullvad rozszerzenie oferuje różne funkcje w zależności od tego, czy jesteś klientem Mullvad VPN:



#### **Bez subskrypcji Mullvad VPN:**




- **Podstawowa kontrola połączenia**: wyświetla bieżący publiczny adres IP i niektóre informacje o połączeniu
- **Zalecenia dotyczące prywatności**: wskazówki dotyczące poprawy ustawień bezpieczeństwa (DNS, tylko HTTPS, wyszukiwarka)
- **Kontrola WebRTC**: włączanie/wyłączanie w celu zapobiegania wyciekom IP Address
- Może zostać usunięty bez wpływu na cyfrowy ślad użytkownika, jeśli nie korzysta on z Mullvad VPN



#### **Z subskrypcją Mullvad VPN:**


Rozszerzenie ujawnia swój pełny potencjał dzięki zaawansowanym funkcjom:





- **Zintegrowany serwer proxy SOCKS5**: połączenie z serwerem proxy Mullvad VPN za pomocą jednego kliknięcia
- Stały adres IP Address: w przeciwieństwie do sieci VPN, która może zmieniać swój adres IP Address, serwer proxy zawsze gwarantuje ten sam wyjściowy adres Address
- **Automatyczny wyłącznik awaryjny**: w przypadku rozłączenia sieci VPN ruch w przeglądarce jest natychmiast blokowany
- **Obsługa protokołu IPv6**: Łączność IPv6, nawet jeśli połączenie VPN nie jest włączone





- **Multihop (podwójna sieć VPN)**: możliwość zmiany lokalizacji serwera proxy w celu utworzenia tunelu wewnątrz tunelu
 - Ruch najpierw przechodzi przez serwer VPN, a następnie "przeskakuje" do innego serwera Mullvad
 - Użyj innej lokalizacji tylko dla przeglądarki





- **Zaawansowane monitorowanie połączenia**: monitorowanie w czasie rzeczywistym stanu sieci VPN, połączonego serwera i wykrywanie wycieków DNS





- **Dostęp do Mullvad Leta**: prywatna wyszukiwarka zarezerwowana dla subskrybentów (choć niezalecana przez Mullvad ze względu na korelację z kontem użytkownika)



Te trzy rozszerzenia współpracują ze sobą, tworząc spójny ekosystem ochrony, w którym każdy użytkownik korzysta z dokładnie tych samych zabezpieczeń, bez możliwości dostosowania, które zagroziłoby zbiorowej anonimowości.



## Zalety i wady przeglądarki Mullvad Browser



### Korzyści





- **Doskonała domyślna ochrona prywatności:** Mullvad Browser stosuje bardzo rygorystyczne ustawienia prywatności od samego początku, bez potrzeby ręcznej konfiguracji.





- **Lepsza wydajność niż Tor Browser:** W przypadku braku routingu cebulowego, Mullvad Browser jest **znacznie szybszy i bardziej responsywny** niż Tor Browser do klasycznego przeglądania stron internetowych.





- **Znajoma prostota Interface:** Mullvad Browser bazuje na Interface Firefoksa. Jeśli jesteś przyzwyczajony do Firefoksa lub nawet przeglądarki Tor, nie poczujesz się nie na miejscu.





- **Zaufana współpraca i audytowany kod:** Mullvad Browser korzysta z doświadczenia Projektu Tor, a cały kod źródłowy jest dostępny do zewnętrznego audytu.



### Wady





- Brak anonimowości w sieci bez VPN: Najważniejszą kwestią jest to, że **Mullvad Browser nie ukrywa twojego IP Address samodzielnie** (jak wszystkie inne przeglądarki, z wyjątkiem Tor Browser). IP Address jest jak "pocztowy Address" w Internecie: ujawnia lokalizację i dostawcę usług internetowych. Dlatego **w dużym stopniu zależy od VPN** (wirtualnej sieci prywatnej), aby ukryć te kluczowe informacje.





- **Brak wersji mobilnej:** Do tej pory Mullvad Browser jest dostępny tylko na PC (Windows, Mac, Linux).





- Niekompatybilne z niektórymi nawykami: **Stały tryb prywatny** oznacza, że nie można utrzymać sesji od jednego użycia do następnego. Nie można pozostać połączonym z kontem internetowym od jednej sesji do następnej.





- **Ograniczone funkcje:** Aby zachować jednolitość odcisków palców, Mullvad Browser **wyłączył kilka funkcji** obecnych w Firefoksie i nie jest przeznaczony do dostosowywania.



## Instalacja przeglądarki Mullvad



Mullvad Browser jest dostępna bezpłatnie dla systemów Windows, macOS i Linux. Aby ją zainstalować, odwiedź [oficjalną stronę Mullvad](https://mullvad.net/browser).



![MULLVAD BROWSER](assets/fr/02.webp)



*Oficjalna strona główna Mullvad Browser z wyróżnionym przyciskiem pobierania.*



![MULLVAD BROWSER](assets/fr/03.webp)



*Wybierz swój system operacyjny na stronie pobierania Mullvad Browser.*



Kliknij przycisk **"Pobierz "** odpowiadający Twojemu systemowi operacyjnemu.



W przypadku systemu Linux można wybrać różne formaty w zależności od dystrybucji. Po zakończeniu pobierania:



### W systemie Windows


Uruchom pobrany plik `.exe` i postępuj zgodnie z instrukcjami instalacji.



### Na macOS


Otwórz pobrany plik `.dmg` i przeciągnij aplikację Mullvad Browser do folderu Aplikacje.



### W systemie Linux


Rozpakuj archiwum `.tar.xz` do wybranego katalogu i uruchom plik `start-mullvad-browser.desktop`.



## Konfiguracja i pierwsze użycie



Po pierwszym uruchomieniu Mullvad Browser zobaczysz Interface bardzo podobny do tego z Tor Browser. Przeglądarka jest wstępnie skonfigurowana pod kątem prywatności i nie wymaga żadnych specjalnych modyfikacji.



![MULLVAD BROWSER](assets/fr/04.webp)



*Interface Strona główna Mullvad Browser z rozszerzeniami, ikona miotły do generate nowa tożsamość i menu aplikacji w prawym górnym rogu.*



**Ważne:** Mullvad Browser domyślnie nie maskuje adresu IP Address. Aby zapewnić pełną ochronę, zdecydowanie zalecamy równoległe korzystanie z VPN. Możesz użyć Mullvad VPN lub dowolnej innej zaufanej usługi VPN.



Przeglądarka zawiera również **DNS-over-HTTPS (DoH)** przy użyciu usługi DNS firmy Mullvad: technologia ta szyfruje żądania DNS (tłumacząc nazwy witryn na adresy IP), aby uniemożliwić dostawcy usług internetowych monitorowanie odwiedzanych witryn.



### Ustawienia bezpieczeństwa



Możesz dostosować poziom bezpieczeństwa, klikając **menu aplikacji** (trzy poziome paski) w prawym górnym rogu, następnie **"Ustawienia "**, a następnie zakładkę **"Prywatność i bezpieczeństwo "**. Przewiń w dół do sekcji **"Bezpieczeństwo "**:



![MULLVAD BROWSER](assets/fr/05.webp)



*Wybór poziomów bezpieczeństwa: strzałki wskazują ścieżkę z menu aplikacji do zakładki "Prywatność i bezpieczeństwo" do opcji bezpieczeństwa*



Mullvad Browser oferuje trzy poziomy zabezpieczeń:





- **Normalny** (bieżący poziom domyślny): Wszystkie funkcje przeglądarki i strony internetowej są włączone





- **Bezpieczniej**: Wyłącza często niebezpieczne funkcje stron internetowych, co może prowadzić do utraty funkcjonalności niektórych witryn:
 - JavaScript jest wyłączony dla witryn nieobsługujących protokołu HTTPS
 - Niektóre czcionki i symbole matematyczne są wyłączone
 - Dźwięk i wideo (media HTML5), a także WebGL są dostępne w trybie "kliknij, aby odtworzyć"





- **Najbezpieczniejszy**: Zezwala tylko na funkcje witryny wymagane dla witryn statycznych i podstawowych usług:
 - JavaScript jest domyślnie wyłączony dla wszystkich witryn
 - Niektóre czcionki, ikony, obrazy i symbole matematyczne są wyłączone
 - Dźwięk i wideo (media HTML5), a także WebGL są dostępne w trybie "kliknij, aby odtworzyć"



### Przycisk nowej sesji



Aby ponownie uruchomić pustą sesję bez zamykania przeglądarki, kliknij ikonę miotły lub użyj menu aplikacji > **"Nowa sesja "**.



![MULLVAD BROWSER](assets/fr/06.webp)



*Funkcja "Resetuj swoją tożsamość" umożliwia ponowne uruchomienie przeglądarki z całkowicie nową sesją*



## Codzienne użytkowanie



### Normalna nawigacja



Mullvad Browser zachowuje się jak klasyczna przeglądarka do codziennego przeglądania. Wszystkie strony internetowe są dostępne jak zwykle, z dodatkową korzyścią w postaci zwiększonej ochrony przed śledzeniem.



### Zarządzanie plikami cookie i logowanie



Ze względu na stały tryb prywatny, będziesz musiał ponownie łączyć się ze swoimi kontami za każdym razem, gdy się zalogujesz. Jest to cena za maksymalną poufność.



### Rozszerzenia



Mullvad Browser technicznie pozwala na instalację dodatkowych rozszerzeń z katalogu Firefox, ale **ważne jest, aby zrozumieć konsekwencje**. Każde dodane rozszerzenie zmienia twój cyfrowy ślad i odróżnia cię od innych użytkowników Mullvad Browser, co jest sprzeczne z podstawową zasadą przeglądarki: aby wszyscy użytkownicy wyglądali identycznie.



Jak wyjaśnia Mullvad: *"Czasami brak konkretnej obrony jest lepszy niż jej posiadanie. Chcąc zwiększyć prywatność online, instalujesz rozszerzenia, które ostatecznie sprawiają, że jesteś jeszcze bardziej widoczny. "*



Jeśli mimo to zdecydujesz się zainstalować rozszerzenia, pamiętaj, że tworzysz unikalny odcisk palca, który może być używany do śledzenia Cię z witryny do witryny. Aby uzyskać maksymalną ochronę, najlepiej trzymać się trzech wstępnie zainstalowanych rozszerzeń, które są identyczne dla wszystkich użytkowników.



## Najlepsze praktyki z przeglądarką Mullvad



1. **Zawsze używaj VPN: Mullvad Browser nie maskuje twojego IP. VPN jest niezbędny do zachowania pełnej anonimowości.**



2. **Nie dostosowuj przeglądarki**: Unikaj zmiany ustawień lub dodawania rozszerzeń, ponieważ może to sprawić, że zostaniesz zidentyfikowany.



3. **Użyj przycisku nowej sesji**: Pomiędzy różnymi aktywnościami użyj funkcji resetowania, aby podzielić sesje.



4. **Wybierz poziom bezpieczeństwa, który najlepiej odpowiada Twoim potrzebom**:




- **Normalny (zalecany)**: Do codziennego przeglądania. Oferuje doskonałą ochronę przy jednoczesnym zachowaniu funkcjonalności stron internetowych. To najlepsza równowaga dla 95% użytkowników.
- **Bezpieczniej**: W przypadku odwiedzania nieznanych lub potencjalnie niebezpiecznych witryn lub w celu zapewnienia dodatkowej ochrony w publicznych sieciach Wi-Fi. Niektóre witryny mogą działać nieprawidłowo.
- **Najbezpieczniejszy**: Zarezerwowane dla sytuacji wysokiego ryzyka (dziennikarstwo śledcze, wrażliwa komunikacja, wrogie środowiska). Większość nowoczesnych witryn zostanie złamana, ale taka jest cena maksymalnego bezpieczeństwa.



5. **Regularnie sprawdzaj dostępność aktualizacji**: Aktualizuj swoją przeglądarkę o najnowsze poprawki zabezpieczeń.



6. **Używaj wyszukiwarek przyjaznych prywatności**: Wybierz DuckDuckGo, Startpage lub Searx zamiast Google.



7. **Włącz tryb tylko HTTPS**: W ustawieniach upewnij się, że tryb "Tylko HTTPS" jest włączony, aby wymusić bezpieczne połączenia.



8. **NIE zmieniaj żadnych zaawansowanych ustawień**: W przeciwieństwie do innych przeglądarek, Mullvad Browser została zaprojektowana tak, aby WSZYSCY użytkownicy mieli dokładnie taką samą konfigurację. Modyfikacja ustawień w `about:config` lub zmiana ustawień uBlock Origin/NoScript uczyniłaby cię unikalnym i całkowicie cofnęłaby anonimowość przeglądarki.



## Zalecana konfiguracja DNS



Mullvad Browser automatycznie integruje Mullvad DNS-over-HTTPS. Jeśli korzystasz z Mullvad VPN, rozszerzenie zaleci **wyłączenie Mullvad DoH**, ponieważ szybciej jest korzystać z serwera DNS serwera VPN. Jeśli nie korzystasz z Mullvad VPN, włącz Mullvad DoH, aby uniknąć monitorowania DNS przez dostawcę usług internetowych.



## Wnioski



Mullvad Browser to doskonałe rozwiązanie dla osób poszukujących przyjaznego dla prywatności przeglądania stron internetowych bez ograniczeń wydajności sieci Tor. W połączeniu z wysokiej jakości siecią VPN oferuje solidną ochronę przed śledzeniem i inwigilacją online.



Mimo pewnych ograniczeń (brak wersji mobilnej, nietrwałe sesje), Mullvad Browser jest cennym narzędziem w arsenale każdego, kto chce odzyskać kontrolę nad swoją cyfrową prywatnością. Łatwość obsługi i domyślna konfiguracja sprawiają, że jest to mądry wybór dla świadomych prywatności użytkowników, zarówno początkujących, jak i doświadczonych.



## Zasoby



### Oficjalna dokumentacja




- [Oficjalna strona przeglądarki Mullvad](https://mullvad.net/fr/browser)
- [Strona pobierania przeglądarki Mullvad](https://mullvad.net/en/download/browser)
- [Szczegółowe specyfikacje techniczne](https://mullvad.net/en/browser/Hard-facts)
- [Rozszerzenie przeglądarki Mullvad](https://mullvad.net/en/help/mullvad-browser-extension)



### Przewodniki i wyjaśnienia




- [Dlaczego prywatność ma znaczenie](https://mullvad.net/en/why-privacy-matters/how-mass-surveillance-companies-collect-your-data)
- [Tor bez Tora: koncepcja przeglądarki Mullvad](https://mullvad.net/en/browser/tor-without-tor)
- [Jak wybrać przeglądarkę przyjazną prywatności](https://mullvad.net/en/browser/things-to-look-for-when-choosing-a-browser)
- [Zrozumienie fingerprintingu przeglądarki](https://mullvad.net/en/browser/browser-fingerprinting)



### Wsparcie i pomoc




- [Centrum pomocy przeglądarki Mullvad](https://mullvad.net/en/help/tag/mullvad-browser)
- [Pierwsze kroki do prywatności online](https://mullvad.net/en/help/first-steps-towards-online-privacy)



### Zasoby wspólnotowe




- [Mullvad Browser Guide - Privacy Guides](https://www.privacyguides.org/en/desktop-browsers/)
- [Dyskusje społeczności](https://discuss.privacyguides.net/t/about-changing-settings-in-mullvad-browser/18330)