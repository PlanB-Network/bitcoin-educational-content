---
name: Firefox
description: Jak skonfigurować przeglądarkę Firefox, by chronić swoją prywatność?
---

![cover](assets/cover.webp)



## Wprowadzenie



Wszyscy spędzamy godziny online, często nie zdając sobie sprawy z tego, co ujawnia o nas nasza przeglądarka. Każde kliknięcie, każde wyszukiwanie, każda odwiedzana witryna zasila ogromny przemysł gromadzenia danych osobowych.



![Statistiques navigateurs 2024](assets/fr/01.webp)


*Udział w rynku przeglądarek internetowych: Chrome dominuje z 65% rynku, a za nim plasują się Safari i Edge. Źródło: [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*



Jak pokazuje ten wykres, Google Chrome dominuje masowo, z ponad 65% użytkowania na całym świecie. Ta hegemonia oznacza, że większość użytkowników Internetu powierza swoje dane przeglądania Google, firmie, której model biznesowy opiera się na ukierunkowanych reklamach. Firefox, z zaledwie 3% rynku, stanowi alternatywę opracowaną przez Mozillę, organizację non-profit, która nie ma komercyjnego interesu w wykorzystywaniu danych użytkowników.



Wybór Firefoksa to jednak tylko pierwszy krok. Domyślnie nawet Firefox wymaga dostosowania, aby zmaksymalizować ochronę. Niniejszy przewodnik poprowadzi cię krok po kroku, od najprostszych do najbardziej zaawansowanych, aby przekształcić Firefoksa w prawdziwą tarczę przed śledzeniem, zachowując jednocześnie przyjemne wrażenia z przeglądania.



### Dlaczego Firefox?





- Wolne i otwarte oprogramowanie** (silnik Gecko): możliwy do skontrolowania, przejrzysty kod
- Organizacja non-profit**: Fundacja Mozilla, misja użyteczności publicznej
- Wbudowane natywne zabezpieczenia**: Enhanced Tracking Protection (ETP), Total Cookie Protection (TCP), State Partitioning, HTTPS-only mode, DNS over HTTPS (DoH)
- Zaawansowane dostosowywanie**: w przeciwieństwie do Chrome, Firefox pozwala dogłębnie modyfikować swoje zachowanie



### Ważne zasady przed rozpoczęciem





- Brak uniwersalnej recepty**: im więcej modyfikacji, tym większe ryzyko wyróżnienia się (fingerprinting). Celem jest lepsza ochrona bez wyróżniania się z tłumu.
- Postęp krok po kroku**: Zmień ustawienia, przetestuj zwykłe witryny, a następnie kontynuuj. Nie trzeba zmieniać wszystkiego naraz.
- Równowaga osobista**: Znajdź SWÓJ kompromis między prywatnością a łatwością użytkowania.



## Szybka instalacja



![Téléchargement Firefox](assets/fr/02.webp)



**Oficjalne pobieranie:** Przejdź do [firefox.com/browsers/desktop](https://www.firefox.com/en-US/browsers/desktop/). Na tej stronie wybierz swój system operacyjny (Windows, macOS, Linux), aby uzyskać dostęp do odpowiedniej strony pobierania ze szczegółowymi instrukcjami instalacji.





- Windows**: pobierz instalator `.exe`, kliknij dwukrotnie i postępuj zgodnie z instrukcjami kreatora instalacji
- macOS**: pobierz plik `.dmg`, otwórz go i przeciągnij Firefoksa do folderu Aplikacje
- Linux**: dostępnych jest kilka opcji - pakiet `.deb`/`.rpm`, Flatpak (Flathub), Snap lub poprzez menedżer pakietów (apt, dnf, pacman). Preferowane oficjalne źródła Mozilli.



**Wskazówka:** Po zainstalowaniu, sprawdź aktualizacje poprzez Pomoc → **O Firefoksie** (ważne dla poprawek bezpieczeństwa).



![Configuration initiale Firefox](assets/fr/03.webp)


*Pierwszy ekran po uruchomieniu Firefoksa: ustaw Firefoksa jako domyślną przeglądarkę, dodaj go do skrótów, a następnie kliknij "Zapisz i kontynuuj "*



![Création compte Firefox](assets/fr/04.webp)


*Opcjonalny krok: utwórz konto Firefox lub zaloguj się na nie. Możesz pominąć ten krok, klikając "Nie teraz" w prawym dolnym rogu*



![Page d'accueil Firefox](assets/fr/05.webp)


*Ekran główny Firefoksa po zakończeniu konfiguracji. Zwróć uwagę na menu ☰ w prawym górnym rogu, które daje dostęp do Ustawień i Rozszerzeń w celu dostosowania Firefoksa*



## Zabezpieczenia już domyślnie aktywowane (uspokajające)





- Izolacja witryn (Fission)**: w progresywnym wdrożeniu. Ta funkcja uruchamia każdą witrynę w osobnym procesie, aby uniemożliwić jednej złośliwej karcie dostęp do danych innej. Sprawdź jej status poprzez `about:support` (wyszukaj "Fission"). Jeśli nie jest włączona, można ją aktywować ręcznie w `about:config` za pomocą `fission.autostart = true`.
- Total Cookie Protection (TCP)**: domyślnie aktywna. Pliki cookie i inne przechowywanie są ograniczone do pierwszej witryny (jeden "słoik" na witrynę), co neutralizuje śledzenie między witrynami. Tymczasowe wyjątki są dokonywane za pośrednictwem Storage Access API, gdy jest to konieczne (zintegrowane przyciski logowania).
- Ochrona przed przekierowaniami**: Firefox automatycznie wykrywa i czyści pliki cookie pozostawione przez strony odsyłające (linki, które przekierowują użytkownika przez moduł śledzący przed miejscem docelowym), ograniczając ten kanał śledzenia bez żadnych działań ze strony użytkownika.



## Poziom 1 - Podstawowy (≤ 10 minut)



Cel: duży wzrost prywatności bez niszczenia sieci. Dla 90% użytkowników.



Aby uzyskać dostęp do ustawień, kliknij menu ☰ w prawym górnym rogu, a następnie **"Ustawienia "**:



![Paramètres généraux](assets/fr/07.webp)


*Strona ustawień Firefox - zakładka "Ogólne". To tutaj konfiguruje się większość opcji prywatności*



**Zabezpieczenie śledzenia (ETP)**




- Przełącz **ETP** na **Strict**. Blokujesz więcej trackerów (cross-site cookies, fingerprinting, cryptomining, widgety społecznościowe...).
- Jeśli witryna ulegnie uszkodzeniu (wideo, przycisk logowania...), wyłącz ochronę tylko dla tej witryny za pomocą osłony 🛡️, a następnie odśwież kartę.



Oto różne poziomy zabezpieczeń ETP:




- Standard** (zrównoważony, maksymalna kompatybilność)
  - Blokady: trackery społecznościowe, pliki cookie między witrynami (wszystkie okna), śledzenie treści w przeglądaniu prywatnym, koparki kryptowalut, detektory odcisków palców.
  - Obejmuje **Total Cookie Protection** (TCP): jeden słoik na witrynę.
- Ścisłe** (zalecane ze względu na poufność)
  - Blokuje również treści śledzące we wszystkich oknach + znane i podejrzewane odciski palców.
  - Może uszkodzić niektóre witryny; użyj osłony 🛡️ dla lokalnego wyjątku.
- Niestandardowe** (zaawansowane)
  - Dokładne dostosowanie: pliki cookie, śledzenie treści, nieletni, odciski palców (znane/podejrzewane).



![Paramètres protection contre le pistage](assets/fr/06.webp)



**Pliki cookie i dane witryny




- Włącz **"Usuń pliki cookie i dane witryny po zamknięciu "**, aby ponownie uruchomić w czysty sposób przy każdym ponownym uruchomieniu.
- Dodaj **Wyjątki** dla 2-3 istotnych witryn, jeśli chcesz (e-mail, bank).


**Automatyczne wprowadzanie danych, sugestie i strona główna**




- Wyłącz **auto-fill** (identyfikatory, adresy, karty). Zamiast tego użyj menedżera haseł.
- Wyszukiwanie**: wyłącz **"Pokaż sugestie wyszukiwania "**.
- Pasek Address**: wycina **"Sugestie sponsorowane "** i **"Sugestie kontekstowe "**.
- Strona główna**: wyłącz **Pocket** i **zawartość sponsorowaną**.



![Paramètres cookies et mots de passe](assets/fr/08.webp)



**Tylko HTTPPS**




- Aktywuj **"Tryb HTTPS tylko we wszystkich oknach "**.


![Configuration DNS over HTTPS](assets/fr/09.webp)



**Pomiary telemetryczne i reklamowe




- W sekcji "Zbieranie danych przez Firefox" **odznacz wszystkie**.
- Dezaktywuj **"Środki reklamowe przyjazne dla prywatności "** (PPA).
- Bezpieczne przeglądanie**: włącz (zalecane). Firefox sprawdza witryny pod kątem list zagrożeń za pomocą zaszyfrowanych zapytań i lokalnych kontroli, chroniąc przed phishingiem i złośliwym oprogramowaniem przy minimalnym wpływie na prywatność.



**Globalna kontrola prywatności (opcjonalnie)**




- Aktywuj **GPC**, aby zasygnalizować odmowę sprzedaży/udostępniania danych.



**Wyszukiwarka




- Przełącz się na **DuckDuckGo**, **Startpage**, **Qwant** lub **Brave Search** (Ustawienia → Wyszukiwanie).



![Configuration moteur de recherche DuckDuckGo](assets/fr/11.webp)



**Prywatna nawigacja**




- Prywatne okna (Ctrl/Cmd+Shift+P) dla jednorazowych sesji (prezenty, dodatkowe konta...). Unikaj trybu "zawsze prywatnego": rozszerzenia mogą być nieaktywne, a wyjątki plików cookie mniej przydatne.



**Niezbędne rozszerzenia** (zainstaluj z oficjalnego katalogu)




- uBlock Origin**: blokuje reklamy i bieżące śledzenie, lekki.
- Privacy Badger**: uczy się blokować to, co śledzi użytkownika; wysyła Do Not Track / GPC.
- ClearURLs** (opcjonalnie): Firefox (ETP Strict) i uBO już dużo czyszczą; zachowaj to, jeśli nadal widzisz "brudne" adresy URL (utm, fbclid).
- Firefox Multi-Account Containers**: **izoluje pliki cookie/sesje i przechowywanie na kontener; równoległe wiele kont; mniej śledzenia między witrynami**. Oficjalne rozszerzenie: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.



![Extension Multi-Account Containers](assets/fr/12.webp)



**Hasła i 2FA**




- Korzystaj z dedykowanego menedżera haseł** (Bitwarden, KeePassXC). **Unikaj** przechowywania haseł w przeglądarce. **Włącz 2FA** wszędzie tam, gdzie to możliwe.



## Poziom 2 - wzmocniony (podział na przedziały i sieć)



Cel: rozdzielenie działań i ograniczenie wycieków sieciowych.



**DNS przez HTTPS (DoH)**




- Status domyślny**: Aktywowane automatycznie w niektórych regionach (USA, Kanada, Rosja, Ukraina). W innych regionach wymagana jest ręczna aktywacja.
- Konfiguracja**: Ustawienia → Ogólne → Ustawienia sieci → **Włącz DoH** → **Cloudflare** lub **Quad9** → **Maksymalna ochrona**.
- Maksymalna ochrona = tylko TRR** (bez powrotu do systemowego DNS). Jeśli sieć korporacyjna/hotelowa blokuje, przełącz się z powrotem na **Standard** lub wyłącz DoH.
- Redundancja**: Jeśli korzystasz już z zaufanej sieci VPN z własnym bezpiecznym DNS, DoH może być nadmiarowy.
- Test weryfikacyjny**: `https://www.dnsleaktest.com/` powinien wyświetlać tylko wybranego dostawcę DoH.



![Sélection fournisseur DNS Cloudflare](assets/fr/10.webp)



**Podział na przedziały za pomocą kontenerów i profili




- Kontenery z wieloma kontami**: tworzenie przestrzeni (osobiste, praca, finanse, sieci społecznościowe, zakupy, jednorazowe). Skonfiguruj **"Zawsze otwieraj w tym kontenerze "** dla powtarzających się witryn. Oficjalne rozszerzenie: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.
- Dlaczego warto z nich korzystać?
  - Silna izolacja** plików cookie/sesji/przechowywania według przestrzeni.
  - Mniej cross-site tracking**: ograniczenie gigantów (Facebook, Google).
  - Jednoczesne korzystanie z wielu kont** w tej samej usłudze.
  - Mniejsze ryzyko CSRF/XSS** między tożsamościami podzielonymi na segmenty.
  - Wskazówka: przynajmniej dedykowane kontenery dla sieci społecznościowych/Google, pracy, finansów.
- Facebook Container** (opcjonalnie): uproszczona wersja przeznaczona dla FB/Instagram.
- Oddzielne profile**: poprzez `about:profiles` (profil główny, minimalny profil "ultra-bezpieczny", profil testowy). Całkowite rozdzielenie danych i rozszerzeń.



**Zaawansowane rozszerzenia** (do zarezerwowania)




- Cookie AutoDelete**: usuwa pliki cookie witryny natychmiast po zamknięciu karty (przydatne, jeśli Firefox jest otwarty przez długi czas).
- LocalCDN**: obsługuje bieżące biblioteki lokalnie (redukuje połączenia z Google/Microsoft). Częściowa kompatybilność.



**Mobile (Android)**




- Firefox Android + uBlock Origin**: podobna ochrona w podróży.



## Poziom 3 - Ekspert (about:config & Arkenfox)



Cel: zaawansowane hartowanie z akceptowalnymi kompromisami. Zalecane na **oddzielnym profilu**.



Wybierz tylko jedno z dwóch poniższych podejść:



**Podejście A - ręczne modyfikacje**: Kilka ukierunkowanych zmian poprzez `about:config` (prostsza, bardziej precyzyjna kontrola)


**Podejście B - Arkenfox user.js**: W pełni zautomatyzowana konfiguracja (bardziej złożona, maksymalna ochrona)



➡️ **Arkenfox zawiera już WSZYSTKIE zmiany about:config wymienione poniżej** + setki innych. Jeśli wybierzesz Arkenfox, zignoruj sekcję about:config.



### Podejście A: Ręczne modyfikacje za pośrednictwem about:config



Wpisz `about:config` na pasku Address → Zaakceptuj ryzyko.



![Avertissement about:config](assets/fr/13.webp)



![Interface about:config](assets/fr/14.webp)



![Préférences about:config](assets/fr/15.webp)





- Odporność na pobieranie odcisków palców (odziedziczona po przeglądarce Tor)


```text
privacy.resistFingerprinting = true
```


Efekty: Strefa czasowa UTC, **letterboxing** (standardowe rozmiary okien), ustandaryzowane User-Agent/policies, ograniczenia Canvas/WebGL/AudioContext. Większa jednolitość, ale kilka "dziwactw" (przesunięcie czasu, czasami trochę angielskiego).





- Wyłącz WebRTC (unika wycieków IP; psuje Web Visio)


```text
media.peerconnection.enabled = false
```





- Referer plus kompatybilny (domyślnie)


```text
network.http.referer.XOriginPolicy = 1
network.http.referer.trimOnCrossOrigin = true
```


Opcja ścisła (może przerwać płatności/SSO):


```text
network.http.referer.XOriginPolicy = 2
```





- Ograniczenie chattering API i spekulacji


```text
dom.battery.enabled = false
device.sensors.enabled = false
beacon.enabled = false
geo.enabled = false
media.navigator.enabled = false
network.prefetch-next = false
browser.urlbar.speculativeConnect.enabled = false
network.http.speculative-parallel-limit = 0
```



Złota zasada: jeśli coś się zepsuje, wróć do ostatniej zmiany.



### Podejście B: Arkenfox user.js (w pełni zautomatyzowana konfiguracja)



Projekt **Arkenfox** udostępnia utrzymywany przez społeczność plik `user.js`, który automatycznie stosuje setki preferencji Firefoksa zorientowanych na prywatność i bezpieczeństwo. Po ponownym uruchomieniu Firefox odczytuje ten plik z profilu użytkownika i stosuje te ustawienia.





- O co chodzi? Zacznij od **spójnej, utwardzonej bazy** bez "klikania wszędzie"; zmniejsz liczbę niedopatrzeń; oszczędzaj czas.
- Co to zmienia (przykłady): ograniczenie telemetrii, wzmocnienie plików cookie/cache/referrer/HTTPS, **RFP** + letterboxing, **WebRTC wyłączone**, dostosowania DoH/TLS, ograniczenie chatty API.
- Kiedy go używać: jeśli chcesz, by Firefox został zahartowany w 10 minut i akceptujesz kilka wyjątków (DRM/streaming, Web visio, SSO/płatności).
- Zalety: szybki, spójny, **aktualizowany** (zgodny z ESR), bardzo dobrze **udokumentowany** (wiki + komentarze), **możliwy do dostosowania** poprzez nadpisania.
- Ograniczenia: kompatybilność (niektóre aplikacje internetowe), wygoda (UTC, rozmiary okien) i przypomnienie: **to nie jest Tor** (brak anonimowości w sieci).



Instalacja (najlepiej na **dedykowanym profilu**)


1. Zapisywanie profilu/ulubionych i lista witryn z wyjątkami dotyczącymi plików cookie.


2. Pobierz `user.js` ze strony `https://github.com/arkenfox/user.js` (wersja ESR/stabilna).


3. Znajdź folder swojego profilu poprzez `about:profiles`:




   - Windows: `%APPDATA%/Mozilla/Firefox/Profiles/...`
   - Linux: `~/.mozilla/firefox/...`
   - macOS: `~/Library/Application Support/Firefox/Profiles/...`


4. Zamknij przeglądarkę Firefox i przenieś plik `user.js` do katalogu głównego folderu profilu.


5. Ponowne uruchomienie; dostosuj za pomocą `about:config` lub pliku nadpisań.



Aktualizacje




- Postępuj zgodnie z wydaniami Arkenfox (dostosowanymi do ESR), zastąp `user.js`, uruchom ponownie Firefoksa; przeczytaj informacje o wydaniu.



**Dostosowanie za pomocą nadpisań**



Arkenfox jest domyślnie restrykcyjny. Aby dostosować pewne ustawienia do swoich potrzeb (streaming, visio, określone strony), można utworzyć plik `user-overrides.js` w tym samym folderze co `user.js`. Plik ten pozwala na "zastąpienie" niektórych preferencji Arkenfox bez modyfikowania głównego pliku.



Utwórz plik `user-overrides.js` i dodaj swoje dostosowania:


```javascript
// DRM/streaming
user_pref("media.eme.enabled", true);

// Safe Browsing (si vous préférez le garder)
user_pref("browser.safebrowsing.phishing.enabled", true);
user_pref("browser.safebrowsing.malware.enabled", true);

// Historique moins restrictif
user_pref("places.history.expiration.max_pages", 200000);

// Synchronisation Firefox
user_pref("identity.fxaccounts.enabled", true);

// WebRTC (si visio nécessaire)
user_pref("media.peerconnection.enabled", true);

// Referer plus compatible
user_pref("network.http.referer.XOriginPolicy", 1);
user_pref("network.http.referer.trimOnCrossOrigin", true);
```



Najlepsze praktyki




- Użyj oddzielnego **profilu "Arkenfox "** i zachowaj "normalny" profil dla wygody.
- Minimalizacja rozszerzeń (uBlock Origin OK) w celu ograniczenia powierzchni ataku i unikalności.
- W razie potrzeby dodaj wyjątki dla poszczególnych witryn (osłona 🛡️, uBO, NoScript, jeśli jest używany).
- Test po każdej zmianie: WebRTC/DNS leaks, Cover Your Tracks, CreepJS.



## Najlepsze praktyki





- Aktualizacje**: Firefox i rozszerzenia zaktualizowane.
- Rozszerzenia**: rozsądne i niezawodne; uważaj na "wątpliwe" wykupy.
- Pobieranie**: ostrożnie; sprawdź wrażliwe pliki w serwisie VirusTotal.
- Hasła**: **dedykowany menedżer** (Bitwarden, KeePassXC); **2FA** włączone; unikaj przechowywania w przeglądarce.
- Higiena**: ograniczenie Google/Facebooka do kontenerów; regularne zamykanie/otwieranie w celu "zresetowania" kontekstu.



## Ograniczenia i alternatywy





- Wzmocniona przeglądarka ≠ anonimowość sieci: bez **VPN** Twój adres IP pozostaje widoczny; nawet z nim korelacja pozostaje możliwa.
- Zbyt duża modyfikacja może uczynić cię **unikalnym**. **RFP** standaryzuje; narzędzia do randomizacji (np. Chameleon) mogą cię... wyróżnić. Testuj, porównuj, dostosowuj.
- Alternatywy/uzupełnienia:
 - Tor Browser: anonimowość w sieci dzięki przeglądarce Tor; wolniejsza. Zobacz nasz kompletny przewodnik instalacji i konfiguracji**:



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb



 - Mullvad Browser: "Tor bez Tora", do połączenia z VPN; znormalizowany ślad. Dowiedz się, jak ją zainstalować w naszym dedykowanym samouczku**:



https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e



- Zalecane kombinacje: Firefox (poziom 2) + VPN do codziennego użytku; Tor/Mullvad do wrażliwych działań; oddzielne profile do podziału na przedziały.



## Wnioski



Postępując zgodnie z tym przewodnikiem krok po kroku, przekształciłeś Firefoksa w prawdziwy bastion przeciwko cyfrowej inwigilacji. Od podstawowych ustawień poziomu 1 po zaawansowane konfiguracje Arkenfox, każda zmiana wzmacnia twoją prywatność bez negatywnego wpływu na komfort przeglądania.



**Twoja prywatność jest teraz lepiej chroniona**: trackery reklam zablokowane, pliki cookie podzielone na przedziały, wycieki IP Address zneutralizowane, telemetria wyłączona. Firefox nie jest już tylko przeglądarką, ale narzędziem cyfrowej ochrony dostosowanym do Twoich potrzeb.



**Pamiętaj: poufność nigdy nie jest czymś oczywistym. Regularnie testuj swoją ochronę, aktualizuj ustawienia i nie wahaj się dostosowywać konfiguracji do zmieniających się nawyków. Twoja anonimowość online zależy w równym stopniu od narzędzi, jak i praktyk.



## Zasoby



### Plan ₿ Network




- SCU 202 - Poprawa osobistego bezpieczeństwa cyfrowego: Aby dowiedzieć się więcej o koncepcjach bezpieczeństwa cyfrowego omówionych w tym samouczku**



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Dokumentacja Mozilli




- [Enhanced Tracking Protection](https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop): Oficjalny przewodnik po rozszerzonej ochronie przed śledzeniem
- [State Partitioning](https://developer.mozilla.org/docs/Mozilla/Firefox/Privacy/State_Partitioning): Dokumentacja techniczna dotycząca partycjonowania stanów
- [MDN Web Security](https://developer.mozilla.org/docs/Web/Security): Kompletne informacje na temat bezpieczeństwa sieci



### Arkenfox




- [Wiki i instrukcja instalacji](https://github.com/arkenfox/user.js/wiki): Pełna dokumentacja projektu Arkenfox
- [Depozyty i wydania](https://github.com/arkenfox/user.js): Pobierz plik user.js i śledź aktualizacje



### Przewodniki i społeczności




- [PrivacyGuides - Przeglądarki desktopowe](https://www.privacyguides.org/en/desktop-browsers/): Rekomendacje i porównania przeglądarek
- Reddit**: r/firefox, r/privacy - opinie i wsparcie
- Forum PrivacyGuides**: szczegółowe dyskusje techniczne



### Narzędzia testowe




- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/): Cyfrowe odciski palców i skuteczność przeciwdziałania śledzeniu
- [Test wycieku DNS](https://www.dnsleaktest.com/): Test wycieku DNS i skuteczność DoH
- [BrowserLeaks](https://browserleaks.com/): Kompletny zestaw testów (WebRTC, Canvas, Czcionki, itp.)
- [BadSSL](https://badssl.com/): Testy sprawdzania poprawności certyfikatów SSL/TLS
- [CreepJS](https://abrahamjuliot.github.io/creepjs/): Zaawansowana analiza 50+ wektorów fingerprintingu
- [Test DNS Cloudflare](https://1.1.1.1/help): Sprawdzanie, czy Cloudflare DoH działa poprawnie
