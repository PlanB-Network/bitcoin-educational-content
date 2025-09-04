---
name: Przeglądarka Orion
description: Jak używać Orion Browser do ochrony prywatności na Macu i iPhonie?
---

![cover](assets/cover.webp)



## Wprowadzenie



W kontekście, w którym większość przeglądarek masowo gromadzi nasze dane osobowe, wybór przeglądarki przyjaznej prywatności staje się kluczowy. Chrome dominuje z 65% globalnego rynku, ale jego model biznesowy opiera się na wykorzystywaniu danych przeglądania. Safari, choć zintegrowane z ekosystemem Apple, nie posiada zaawansowanych funkcji ochrony i nie obsługuje elastycznie rozszerzeń innych firm.



![Répartition du marché des navigateurs](assets/fr/01.webp)


*Podział rynku przeglądarek internetowych: Chrome dominuje z ponad 65% udziałem w rynku, a za nim plasują się Safari, Edge i Firefox*



**Orion Browser** prezentuje się jako innowacyjna alternatywa dla użytkowników Apple. Opracowana przez Kagi przeglądarka łączy w sobie szybkość silnika WebKit z filozofią zerowej telemetrii. W przeciwieństwie do swoich konkurentów, Orion nie wysyła żadnych danych do zdalnych serwerów i natywnie blokuje 99,9% reklam i trackerów, w tym YouTube.



Jego unikalna cecha? Orion jest **jedyną przeglądarką WebKit**, która natywnie instaluje rozszerzenia Chrome **i** Firefox, oferując to, co najlepsze z obu światów. Ta kompatybilność, w połączeniu z zużyciem pamięci od 2 do 3 razy mniejszym niż w przypadku innych przeglądarek i płynną integracją z ekosystemem Apple (iCloud, Keychain), czyni ją idealnym wyborem dla świadomych prywatności użytkowników komputerów Mac i iPhone.



## Dlaczego warto wybrać Orion Browser?



### Kluczowe korzyści



**Maksymalna ochrona od razu po wyjęciu z pudełka**: Orion domyślnie blokuje 99,9% reklam (w tym YouTube) oraz wszystkie własne i zewnętrzne elementy śledzące. Jego technologia łączy inteligentne zapobieganie śledzeniu WebKit z listami EasyPrivacy dla maksymalnej wydajności. Unikalna funkcja: Orion blokuje skrypty fingerprinting **przed ich wykonaniem**, czyniąc śledzenie dosłownie niemożliwym - jest to bardziej radykalne podejście niż w przypadku innych przeglądarek, które próbują jedynie "maskować" dane.



**Zero weryfikowalnej telemetrii**: Orion przyjmuje radykalne podejście do prywatności, z zerową telemetrią z założenia. W przeciwieństwie do innych przeglądarek, które wykonują setki żądań sieciowych podczas uruchamiania (wykładnik IP, odcisk palca przeglądarki, dane osobowe), Orion nigdy nie "dzwoni do domu". Ta fundamentalna różnica całkowicie eliminuje ryzyko niezamierzonego wycieku danych.



**Wyjątkowa wydajność**: Oparty na zoptymalizowanej wersji WebKit, Orion dorównuje, a nawet przewyższa Safari pod względem szybkości działania na komputerach Mac. Testy Speedometer 2.0/2.1 konsekwentnie plasują go na pierwszym miejscu na procesorach Apple Silicon. Natywne blokowanie reklam dodatkowo przyspiesza ładowanie strony o 20 do 40%.



**Uniwersalna obsługa rozszerzeń**: Główna innowacja, Orion pozwala na instalację rozszerzeń z Chrome Web Store **oraz** Mozilla Add-ons. Obsługa rozszerzeń WebExtensions jest obecnie eksperymentalna, z docelową 100% kompatybilnością w wersji beta. Możesz korzystać z wielu popularnych rozszerzeń, takich jak uBlock Origin, Bitwarden, nawet na iPhonie - po raz pierwszy na świecie na iOS, chociaż niektóre mogą nie działać idealnie.



### Ograniczenia, których należy być świadomym





- Ograniczona dostępność**: Obecnie zarezerwowane dla systemów macOS i iOS/iPadOS. Wersja dla systemu Linux osiąga kamienie milowe rozwoju (kamień milowy 2 w 2025 r.), ale nie jest dostępna publicznie. Systemy Windows i Android nie są rozwijane z powodu braku zasobów.
- Zamknięty kod źródłowy**: Chociaż niektóre komponenty są open-source, Orion pozostaje w przeważającej mierze prawnie zastrzeżony, co jest przedmiotem debaty w społeczności zajmującej się prywatnością.
- Eksperymentalne rozszerzenia**: Obsługa rozszerzeń pozostaje w fazie beta, z częstymi niezgodnościami. Rozszerzenia mogą wpływać na wydajność, a niektóre w ogóle nie działają.
- Bezpieczeństwo WebKit**: W przeciwieństwie do Chromium, WebKit nie oferuje tak solidnej izolacji procesów per-site, co może stanowić zagrożenie dla bezpieczeństwa w niektórych scenariuszach.
- Testy blokowania**: Orion celowo wypada słabo w testach reklam online (26-35%), ponieważ Kagi uważa te testy za "fundamentalnie wadliwe". Rzeczywista skuteczność w codziennym użytkowaniu jest znacznie wyższa.



## Instalacja przeglądarki Orion Browser



### Na macOS



![Page d'accueil Kagi avec Orion Browser](assets/fr/02.webp)


*Strona główna Kagi przedstawia Orion Browser jako "przeglądarkę wolną od reklam z całkowitą ochroną prywatności i uniwersalną obsługą rozszerzeń "*





- Przejdź do [kagi.com/orion](https://kagi.com/orion/)
- Kliknij na "**Pobierz Orion dla macOS**"



![Page de téléchargement d'Orion Browser](assets/fr/03.webp)


*Strona pobierania Orion Browser pokazująca dostępność dla macOS i iOS, z linkami do App Store*





- Otwórz pobrany plik `.dmg`
- Przeciągnij aplikację Orion do folderu Aplikacje
- Przy pierwszym uruchomieniu macOS poprosi o potwierdzenie otwarcia



**Alternatywny Homebrew**:


```bash
brew install --cask orion
```



### Na iPhone/iPad





- Otwórz **App Store**
- Wyszukaj "**Orion Browser by Kagi**"
- Zainstaluj bezpłatną aplikację (kompatybilną z iOS 15+)



### Konfiguracja początkowa



Przy pierwszym uruchomieniu Orion prowadzi użytkownika przez kilka kroków:



**1. Ekran powitalny


![Écran de bienvenue d'Orion](assets/fr/04.webp)


*Ekran powitalny Orion Browser podkreślający kluczowe funkcje: szybsze przeglądanie, brak telemetrii, blokowanie reklam i obsługa rozszerzeń*



**2. Dostosowanie Interface**


![Options de personnalisation](assets/fr/05.webp)


*Ekran personalizacji pozwala skonfigurować wygląd kart i Interface zgodnie z własnymi preferencjami*





- Import danych**: Łatwe przenoszenie ulubionych i haseł z przeglądarki Safari, Chrome lub Firefox
- Synchronizacja ICloud**: Aktywuj, aby znaleźć swoje ulubione i zakładki na wszystkich urządzeniach Apple



**3. Instalacja na urządzeniach mobilnych**


![Installation sur iOS](assets/fr/06.webp)


*Ekran instalacyjny na iOS pokazujący kod QR do szybkiego pobrania Orion Browser z App Store*



**4. Interface - powitanie i niezbędne narzędzia



![Page d'accueil Orion](assets/fr/07.webp)


*Strona główna Orion Browser Interface: strzałka wskazuje trzy kluczowe narzędzia dostępne bezpośrednio z paska Address*



Po zakończeniu konfiguracji odkryjesz usprawniony Interface Oriona z **trzema podstawowymi narzędziami** (wskazanymi strzałką):





- Shield 🛡️**: Wyświetla raport prywatności z liczbą elementów zablokowanych na bieżącej stronie
- Pędzel 🖌️**: Dostosuj wyświetlanie strony (motyw, czcionka, usuń rozpraszające Elements)
- Gear ⚙️**: Konfiguracja parametrów specyficznych dla witryny (uprawnienia, blokowanie itp.)



Narzędzia te są zawsze dostępne i pozwalają kontrolować przeglądanie poszczególnych witryn.



**Ważne**: Orion jest darmowy i nie wymaga rejestracji ani tworzenia konta do działania.



![Orion+ dans les préférences](assets/fr/08.webp)


*Ekran subskrypcji Orion+ w preferencjach, oferujący opcjonalną subskrypcję wspierającą rozwój*



**Orion+ (opcjonalnie)**: Aby wesprzeć rozwój projektu, Kagi oferuje Orion+ (5 USD/miesiąc, 50 USD/rok lub 150 USD dożywotnio). Ta dobrowolna subskrypcja umożliwia:




- Bezpośrednia komunikacja z zespołem programistów
- Wpływanie na ewolucję przeglądarki zgodnie z własnymi potrzebami
- Dostęp do wersji Nightly z najnowszymi funkcjami eksperymentalnymi
- Korzystaj z najnowszego silnika WebKit
- Uzyskaj wyróżniającą odznakę na forum opinii



Orion+ gwarantuje niezależność projektu: "Twój wkład finansowy pomaga nam zachować niezależność i dotrzymać obietnicy, że staniemy się najlepszą przeglądarką dla naszych użytkowników". To właśnie ten model finansowania przez użytkowników sprawia, że Orion jest wolny od reklam i telemetrii.



## Konfiguracja zapewniająca maksymalną poufność



### Podstawowe parametry



Dostęp do preferencji poprzez **Orion → Preferencje** (lub ⌘,):



**1. Wyszukiwanie - prywatna wyszukiwarka**



![Configuration du moteur de recherche](assets/fr/09.webp)


*Domyślna konfiguracja wyszukiwarki: DuckDuckGo jest wybrana dla maksymalnej prywatności*





- Domyślny silnik**: Wybierz **DuckDuckGo**, **Startpage** lub **Kagi** dla optymalnej prywatności (unikaj Google/Bing)
- Sugestie wyszukiwania**: Wyłącz je, aby zapobiec wyciekaniu naciśnięć klawiszy do serwerów wyszukiwarek



**2. Prywatność - ochrona ogólna**



![Content Blocker dans les préférences](assets/fr/12.webp)


*Ustawienia prywatności Orion pokazujące blokadę treści z 119 156 aktywnymi regułami, opcjami usuwania elementów śledzących i niestandardowym agentem użytkownika*



**Blokada treści aktywna domyślnie**:




- EasyList**: ponad 119 tys. reguł blokowania reklam
- EasyPrivacy**: Ochrona przed śledzeniem
- Zarządzaj listami filtrów**: Dodaj dodatkowe listy (zalecane Hagezi)



**Opcje prywatności**:




- Usuwa elementy śledzące z adresów URL**: "Tylko do przeglądania prywatnego" usuwa skopiowane linki
- Udostępniaj raporty o awariach**: "Po zapytaniu o zgodę" respektuje zgodę użytkownika
- Niestandardowy agent użytkownika**: Może zostać zmodyfikowany w celu ominięcia niektórych blokad



![YouTube avec Privacy Report](assets/fr/10.webp)


*Przykład YouTube oglądanego z Orionem: brak widocznych reklam i raport prywatności pokazujący wiele zablokowanych Elements*



**3. Ustawienia witryny - kontrola według witryny**



![Website Settings pour YouTube](assets/fr/11.webp)


*Ustawienia witryny dla YouTube pokazujące opcje zgodności, blokowanie treści i uprawnienia specyficzne dla witryny*



**Szybki dostęp**: Kliknij na koło zębate ⚙️ na pasku Address, aby dostosować:




- Tryb zgodności**: Rozwiązuje problemy z wyświetlaniem poprzez zawieszenie rozszerzeń
- Blokady treści**: W razie potrzeby dezaktywuj blokowanie dla określonej witryny
- JavaScript/Cookies**: Szczegółowa kontrola według witryny
- Uprawnienia**: Kamera, mikrofon, lokalizacja konfigurowane indywidualnie



**4. Zaawansowane filtry niestandardowe** (patrz poniżej)



**Utwórz filtry niestandardowe** (Prywatność → Zarządzaj listami filtrów → Filtry niestandardowe):



**Uproszczona składnia** (kompatybilna z Adblock Plus):




- `reddit.com##.promotedlink`: Ukrywa sponsorowane posty Reddit
- `||ads.example.com^`: Całkowicie blokuje domenę reklamową
- `@@||site-utile.com^`: Tworzy wyjątek dla witryny



**Wskazówka: Odwiedź stronę [FilterLists.com](https://filterlists.com), aby uzyskać tysiące gotowych do użycia list specjalistycznych.



### Zalecane rozszerzenia



Orion natywnie obsługuje rozszerzenia dla przeglądarek Chrome i Firefox. Można je zainstalować bezpośrednio z oficjalnych sklepów:



**Essentials**:




- uBlock Origin**: Dodaje szczegółową kontrolę do natywnego blokera
- Bitwarden**: Menedżer haseł o otwartym kodzie źródłowym
- ClearURLs**: Usuwa parametry śledzenia URL



**Opcjonalnie**:




- LocalCDN**: Lokalnie obsługuje biblioteki współdzielone
- Cookie AutoDelete**: Automatycznie usuwa pliki cookie po zamknięciu kart
- NoScript**: Całkowita kontrola nad wykonywaniem skryptów JavaScript (zaawansowani użytkownicy)



Aby zainstalować:




- Odwiedź stronę [chrome.google.com/webstore](https://chrome.google.com/webstore) lub [addons.mozilla.org](https://addons.mozilla.org)
- Kliknij "Dodaj do Chrome/Firefox"
- Orion automatycznie przechwyci i zainstaluje rozszerzenie



**Uwaga**: Ponieważ obsługa rozszerzeń jest eksperymentalna, wiele rozszerzeń może nie działać poprawnie lub może wpływać na wydajność. W przypadku wystąpienia problemu (strona przestaje działać, spowolnienie), należy wyłączać rozszerzenia jedno po drugim, aby zidentyfikować jego źródło.



## Codzienne użytkowanie



### Interface i unikalne cechy




![Outil de personnalisation pinceau](assets/fr/13.webp)


*Menu pędzla Orion do dostosowywania wyświetlania: rozmiar czcionki, motyw (jasny/ciemny), dezaktywacja przyklejonych nagłówków i usuwanie rozpraszających Elements*



**Narzędzie pędzla: zaawansowane dostosowywanie**



Narzędzie Orion **brush** to unikalna funkcja, która pozwala dostosować wyświetlanie każdej strony internetowej:



**Opcje motywu**:




- Przełączanie między jasnymi i ciemnymi motywami dla każdej witryny
- Automatyczna adaptacja do preferencji systemowych



**Kontrola typograficzna**:




- Rozmiar czcionki**: Dostosuj czytelność za pomocą przycisków A- i A+
- Styl czcionki**: Zmień rodzinę czcionki (domyślną lub niestandardową)



**Interface czyszczenie**:




- Wyłącz przyklejone nagłówki**: Usuwa nagłówki, które pozostają na górze podczas przewijania
- Erase Elements**: Trwale usuń irytujące Elements (reklamy, wyskakujące okienka, banery cookie)
  - Kliknij "+ Wymaż", a następnie wybierz element, który ma zostać ukryty
  - Bardzo przydatne w przypadku witryn z trwałymi reklamami lub wizualnym śledzeniem Elements



**Trwałość**: Wszystkie te ustawienia są zapisywane dla każdej domeny i automatycznie stosowane ponownie przy następnej wizycie.



**Zaawansowane zarządzanie kartami**:




- Pionowe zakładki**: Aktywacja za pomocą paska menu (funkcja Tabs on the Side)
- Kompaktowe zakładki**: W Preferencjach → Zakładki → Układ "Kompaktowy", aby zaoszczędzić miejsce
- Grupy kart**: Organizuj sesje według tematów
- Wiele profili**: Tworzenie oddzielnych tożsamości za pomocą paska menu (funkcja Profile) z całkowicie odizolowanymi danymi



**Tryb niskiego zużycia energii**: Zainspirowany iPhonem, tryb ten automatycznie zawiesza nieaktywne karty po 5 minutach i może zmniejszyć zużycie energii nawet o 90%. Aktywuj go za pomocą paska menu Orion na Macu lub w ustawieniach na iOS.



**Wbudowane narzędzia** (menu edycji i inne):




- Edytuj tekst na stronie**: tymczasowa modyfikacja dowolnego tekstu (menu Edycja)
- Zezwalaj na kopiowanie i wklejanie**: Pomija ograniczenia kopiowania (menu Edycja)
- Kopiuj czysty link**: Kliknij łącze prawym przyciskiem myszy, aby usunąć parametry śledzenia
- Tryb Focus**: nawigacja pełnoekranowa bez rozpraszania uwagi
- Obraz w obrazie**: Oglądaj filmy w pływającym oknie
- Otwórz w Internet Archive**: Bezpośredni dostęp do wersji zarchiwizowanych
- Raport prywatności**: Kliknij tarczę 🛡️, aby zobaczyć elementy zablokowane przez stronę



### Zarządzanie prywatnym przeglądaniem



Prywatna nawigacja Orion (⌘⇧N) oferuje:




- Pełna izolacja plików cookie i sesji
- Automatyczne usuwanie po zamknięciu
- Historia i dezaktywacja pamięci podręcznej
- Zwiększona ochrona przed pobieraniem odcisków palców



**Wskazówka**: Aby uzyskać zaawansowaną separację, utwórz **oddzielne profile** za pomocą paska menu (funkcja Profile). Każdy profil pojawia się jako oddzielna aplikacja w Docku, z własnymi ustawieniami, rozszerzeniami i całkowicie odizolowanymi danymi.



### Optymalizacja wydajności i prywatność



Aby Orion był szybki i prywatny:




- Rozszerzenia**: Ogranicz do niezbędnego minimum (może obniżyć wydajność)
- Tryb niskiego zużycia energii**: Aktywacja podczas długich sesji (możliwe 90% oszczędności)
- Raport prywatności**: Kliknij tarczę 🛡️, aby zobaczyć blokady w czasie rzeczywistym
- Personalizacja wizualna**: Użyj pędzla 🖌️, aby dostosować wyświetlanie i usunąć rozpraszające Elements
- Kopiuj czysty link**: Kliknij prawym przyciskiem myszy, aby skopiować linki bez elementów śledzących
- Oddzielne profile**: Korzystaj z dedykowanych profili, aby podzielić swoje działania
- Ustawienia witryny**: Kliknij koło zębate ⚙️, aby dostosować uprawnienia według witryny
- Regularne czyszczenie**: Wyczyść pamięć podręczną przez Orion → Wyczyść dane przeglądania



## Porównanie z alternatywnymi rozwiązaniami



| Critère | Orion | Safari | Chrome | Firefox | Brave |
|---------|-------|--------|---------|----------|--------|
| **Télémétrie** | Aucune | Minimale | Extensive | Modérée | Minimale |
| **Bloqueur natif** | 99,9% efficace | Basique | Absent | Partiel | Complet |
| **Extensions** | Chrome + Firefox | Limitées | Chrome uniquement | Firefox uniquement | Chrome uniquement |
| **Performance Mac** | Excellente | Excellente | Bonne | Moyenne | Bonne |
| **Consommation RAM** | Très faible | Faible | Élevée | Moyenne | Moyenne |
| **Open Source** | Partiel | Partiel (WebKit) | Partiel | Complet | Complet |
| **Plateformes** | Mac/iOS | Mac/iOS | Toutes | Toutes | Toutes |

**W porównaniu do Safari**: Orion oferuje doskonałą ochronę dzięki zaawansowanemu blokerowi i obsłudze rozszerzeń, przy jednoczesnym zachowaniu wydajności WebKit.



**Versus Chrome**: niezrównana prywatność bez uszczerbku dla kompatybilności, dzięki obsłudze rozszerzeń Chrome.



**Wersja Firefox**: Szybszy na Macu, Interface bardziej intuicyjny, ale mniej szczegółowa kontrola i nie open-source.



**Versus Brave**: Podobna filozofia, ale Orion unika kontrowersji związanych z kryptowalutami/BAT i oferuje lepszą integrację z Apple.



## Zalecane przypadki użycia



**Idealny dla**:




- Użytkownicy Apple szukają większej prywatności niż Safari
- Osoby, które chcą blokować wszystkie reklamy (w tym YouTube) bez rozszerzeń
- Deweloperzy wymagający narzędzi WebKit ze zintegrowaną ochroną prywatności
- Użytkownicy iPhone'ów chcą rozszerzeń pulpitu na urządzeniach mobilnych (wyjątkowa innowacja)
- Profesjonaliści, którzy muszą podzielić swoje działania (wiele profili)
- Użytkownicy mobilni szukający lepszego zarządzania baterią (tryb niskiego zużycia energii)



**Unikaj, jeśli**:




- Używasz głównie systemu Windows/Linux (brak dostępnej wersji)
- Pełny open-source jest niezbędny dla modelu zagrożeń
- Polegasz na określonych rozszerzeniach, które mogą nie działać
- Potrzebujesz synchronizacji międzyplatformowej wykraczającej poza ekosystem Apple
- Preferujesz sprawdzone, stabilne rozwiązanie (stały status beta od 2021 r.)



## Punkty uwagi i bezpieczeństwo



### Unikalne funkcje bezpieczeństwa



**Rewolucyjna ochrona przed fingerprintingiem**: Orion jest jedyną przeglądarką, która całkowicie blokuje wykonywanie skryptów fingerprintingowych, zanim zdążą one przeskanować system. To podejście "brak uruchomionego skryptu = brak możliwości pobrania odcisków palców" przewyższa tradycyjne metody maskowania stosowane przez inne przeglądarki.



**Transparent Whitelist**: Orion utrzymuje niewielką publiczną listę witryn (browserbench.org, wizzair.com), w których blokowanie jest automatycznie wyłączane, aby uniknąć nieprawidłowego działania. Ta przejrzystość pozwala użytkownikom dokładnie zrozumieć, kiedy i dlaczego blokowanie jest wyłączane.



**Niekontrolowane rozszerzenia**: Obsługa rozszerzeń Chrome/Firefox wprowadza dodatkowe ryzyko, ponieważ rozszerzenia te nie zostały zaprojektowane dla WebKit i nie są specjalnie audytowane dla tego środowiska.



### Konserwacja i aktualizacje





- Automatyczne aktualizacje**: Orion aktualizuje się automatycznie na macOS poprzez Sparkle
- Śledzenie podatności**: Regularne sprawdzanie informacji o wydaniach pod kątem poprawek zabezpieczeń
- Zgłaszanie błędów**: Użyj [orionfeedback.org](https://orionfeedback.org) do zgłaszania problemów




## Wnioski



Przeglądarka Orion Browser stanowi znaczący krok naprzód w zakresie prywatności w systemach macOS i iOS. Jej zerowe podejście do telemetrii, w połączeniu z ultra-wydajnym natywnym blokerem i unikalną obsługą uniwersalnych rozszerzeń, czyni ją doskonałym wyborem dla świadomych prywatności użytkowników Apple.



**Ważne**: Orion pozostaje w stałej wersji beta od 2021 roku, z ograniczeniami kompatybilności rozszerzeń i nieodłącznym ryzykiem WebKit. Oceń te kompromisy zgodnie ze swoim modelem zagrożeń.



Do codziennego użytku na Macu lub iPhonie jest to prawdopodobnie najlepszy kompromis między poufnością, wydajnością i łatwością użytkowania dostępny w ekosystemie Apple, pod warunkiem, że zaakceptujesz jego ograniczenia.



Pamiętaj: ochrona prywatności nie zależy tylko od przeglądarki. Połącz Orion z najlepszymi praktykami (silne hasła, 2FA, VPN w razie potrzeby), aby uzyskać optymalne bezpieczeństwo online.



## Zasoby i wsparcie



### Oficjalna dokumentacja




- Oficjalna strona internetowa**: [kagi.com/orion](https://kagi.com/orion/)
- Pełne FAQ**: [browser.kagi.com/faq](https://browser.kagi.com/faq)
- Forum społeczności**: [community.kagi.com](https://community.kagi.com)
- Śledzenie błędów**: [orionfeedback.org](https://orionfeedback.org)
- GitHub Orion**: [github.com/OrionBrowser](https://github.com/OrionBrowser) - Komponenty open-source
- Blog Kagi**: [blog.kagi.com](https://blog.kagi.com) - Nowości i aktualizacje



### Zalecane testy weryfikacyjne



Po skonfigurowaniu przetestuj swoją konfigurację:




- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/) - Test odcisków palców
- [DNS Leak Test](https://www.dnsleaktest.com/) - Sprawdź wycieki DNS
- [BrowserLeaks](https://browserleaks.com/) - Kompletny zestaw testów prywatności



### Alternatywy dla Plan ₿ Network


Aby uzyskać maksymalną ochronę, zapoznaj się z naszymi innymi przewodnikami:




- [Firefox hardened](https://planb.network/tutorials/computer-security/communication/firefox-11814cec-3415-4ed9-a06e-f6fda5c9510f) - Zaawansowana konfiguracja wieloplatformowa
- [Tor Browser](https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb) - Pełna anonimowość w sieci
- [Mullvad Browser](https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e) - Maksymalna ochrona przed odciskami palców



Jeśli chcesz dowiedzieć się więcej o historii i działaniu przeglądarek, a także o głównych obiektach cyfrowych w codziennym życiu, zapraszam do odkrycia naszego nowego bezpłatnego szkolenia SCU 202, dostępnego na Plan ₿ Network:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1
