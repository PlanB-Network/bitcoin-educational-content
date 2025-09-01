---
name: LibreWolf
description: Jak korzystać z przeglądarki prywatności LibreWolf?
---

![cover](assets/cover.webp)



Każde kliknięcie, każde wyszukiwanie, każda odwiedzona strona: przeglądarka internetowa stała się wyrafinowanym donosicielem zasilającym globalny komercyjny system nadzoru. Google Chrome, używany przez ponad 3 miliardy ludzi, zamienia codzienne przeglądanie w lukratywne dane dla gigantów reklamowych. Nawet Firefox, pomimo swojej reputacji "etycznej" przeglądarki, domyślnie aktywuje mechanizmy telemetryczne, które przesyłają twoje nawyki przeglądania do Mozilli.



Ta rzeczywistość rodzi zasadnicze pytanie: czy nadal możliwe jest swobodne przeglądanie Internetu bez ciągłego szpiegowania i profilowania? Na szczęście odpowiedź jest twierdząca, dzięki projektom społecznościowym, które stawiają użytkownika z powrotem w centrum zainteresowania.



LibreWolf ucieleśnia tę filozofię cyfrowego oporu. Przeglądarka ta, będąca dziełem społeczności niezależnych deweloperów, przekształca Firefoksa w prawdziwą tarczę przed inwigilacją online. Tam, gdzie komercyjne przeglądarki starają się zarabiać na twojej uwadze, LibreWolf robi coś przeciwnego: czyni cię niewidocznym dla trackerów, zachowując płynne, nowoczesne wrażenia z przeglądania.



W tym samouczku odkryjemy, w jaki sposób LibreWolf może zmienić sposób surfowania po Internecie, oferując solidną ochronę przed śledzeniem bez poświęcania wydajności lub kompatybilności z siecią.



![LIBREWOLF](assets/fr/01.webp)


*Udział w rynku przeglądarek internetowych: Chrome dominuje z 65% rynku, a za nim plasują się Safari i Edge. Ta dominacja rodzi pytania o różnorodność sieci i prywatność*



## Przedstawiamy LibreWolf



**FreeWolf** to przeglądarka internetowa o otwartym kodzie źródłowym wywodząca się z Mozilla Firefox, rozwijana i utrzymywana przez niezależną społeczność entuzjastów wolnego oprogramowania. Jej głównym celem jest oferowanie przeglądania skoncentrowanego na prywatności, bezpieczeństwie i wolności użytkownika.



Mówiąc konkretnie, LibreWolf wykorzystuje silnik Gecko Firefoksa, ale z radykalnie inną filozofią: tam, gdzie Firefox musi zrównoważyć prywatność i łatwość użytkowania, LibreWolf domyślnie wybiera prywatność. Projekt usuwa wszystko, co może naruszać prywatność użytkownika (telemetria, gromadzenie danych, sponsorowane moduły), jednocześnie integrując ulepszone ustawienia bezpieczeństwa.



### Cele: prywatność i wolność



LibreWolf ma na celu zmaksymalizowanie ochrony przed śledzeniem i odciskami palców przy jednoczesnym zwiększeniu bezpieczeństwa przeglądarki. Jego główne cele obejmują:





- Wyeliminowanie wszystkich funkcji telemetrycznych i gromadzenia danych** w przeglądarce Firefox
- Wyłączenie funkcji, które są sprzeczne z wolnością użytkownika**, takich jak zastrzeżone moduły DRM
- Zastosuj ustawienia prywatności/bezpieczeństwa** i określone poprawki od samego początku
- Rozwój społeczności gwarantuje przejrzystość i niezależność** od interesów komercyjnych



Krótko mówiąc, LibreWolf prezentuje się jako "Firefox taki, jaki byłby, gdyby prywatność była najwyższym priorytetem" - przeglądarka, która domyślnie szanuje użytkownika, bez konieczności dodatkowej konfiguracji.



### Główne cechy



Od samego początku LibreWolf oferuje szereg funkcji zorientowanych na prywatność:



**Brak telemetrii lub gromadzenia danych:** W przeciwieństwie do Chrome lub Firefox, które wysyłają pewne statystyki użytkowania, LibreWolf nie gromadzi absolutnie nic z przeglądania. Żadnych raportów o awariach, żadnych badań użytkowników, żadnych sponsorowanych sugestii.



**LibreWolf natywnie integruje rozszerzenie uBlock Origin, jeden z najlepszych programów blokujących reklamy i śledzących na rynku. Domyślnie LibreWolf agresywnie odfiltrowuje wszystko, co może śledzić użytkownika online (natrętne reklamy, skrypty śledzące, kryptowaluta Mining).



**Domyślna prywatna wyszukiwarka:** LibreWolf domyślnie wybiera DuckDuckGo jako początkową wyszukiwarkę, która nie zachowuje historii zapytań. Dostępne są również inne alternatywy zorientowane na prywatność (Searx, Qwant, Whoogle).



**Wzmocniona ochrona przed odciskami palców:** Odciski palców pozwalają na unikalną identyfikację przeglądarki poprzez jej konfigurację, nawet bez plików cookie. Aby temu przeciwdziałać, LibreWolf aktywuje technologię RFP (Resist Fingerprinting) z projektu Tor, aby uczynić przeglądarkę tak ogólną, jak to tylko możliwe. Testy pokazują, że standardowy Firefox jest w ~90% unikalny w narzędziach takich jak coveryourtracks.eff.org, w porównaniu do zaledwie ~10-20% dla LibreWolf (liczby te są orientacyjne i mogą się różnić w zależności od konfiguracji oprogramowania i sprzętu oraz zainstalowanych rozszerzeń).



![LIBREWOLF](assets/fr/07.webp)


*Strona testowa EFF [Cover Your Tracks](https://coveryourtracks.eff.org/) z przyciskiem TEST YOUR BROWSER. Strona ta służy do oceny ochrony przed trackerami i fingerprintingiem



![LIBREWOLF](assets/fr/08.webp)


*Wynik testu Cover Your Tracks. Wyświetlany jest komunikat "masz silną ochronę przed śledzeniem w sieci", pokazujący skuteczność ochrony LibreWolf.*



**LibreWolf domyślnie aktywuje rygorystyczne ustawienia bezpieczeństwa. Rozszerzona ochrona przed śledzeniem Firefoksa jest ustawiona na poziom Ścisły, aby blokować tysiące trackerów, plików cookie innych firm i złośliwą zawartość. Aktywuje również izolację witryn i plików cookie (*Total Cookie Protection*) w celu partycjonowania danych dla każdej domeny i ogranicza WebRTC (ograniczając *kandydatówICE* i routing przez proxy, gdy obecne jest proxy), aby zmniejszyć ryzyko wycieku IP Address.



**Szybkie aktualizacje silnika:** Projekt bardzo uważnie śledzi rozwój Firefoksa: LibreWolf jest zawsze oparty na najnowszej stabilnej wersji Firefoksa, a opiekunowie starają się wydać nową wersję w ciągu 24 do 72 godzin od każdego oficjalnego wydania Firefoksa.



## Zalety i wady



### Korzyści





- Brak telemetrii lub niechcianych połączeń:** LibreWolf nie przesyła żadnych danych o użytkowaniu, zapewniając całkowite poszanowanie prywatności użytkownika.





- Open-source i oparty na społeczności:** Projekt jest w 100% open-source i utrzymywany przez wolontariuszy. Ta niezależność gwarantuje, że żaden model reklamowy nie wpłynie na rozwój.





- Wstępnie skonfigurowany pod kątem prywatności:** LibreWolf oszczędza cenny czas: nie ma potrzeby spędzania godzin na dostosowywaniu ustawień Firefoksa, wszystko jest już zrobione.





- Natywny ad blocker/tracker:** uBlock Origin jest zintegrowany w standardzie, więc nie musisz nic robić, aby chronić się przed reklamami i błędami.





- Doskonała ochrona przed odciskami palców:** Dzięki RFP i licznym ustawieniom prywatności LibreWolf drastycznie zmniejsza unikalny cyfrowy ślad w sieci.





- Poprawiona wydajność i mniejsza waga:** Dzięki usunięciu telemetrii i niektórych nieistotnych funkcji, LibreWolf może być nieco szybszy i mniej energochłonny niż standardowy Firefox.



### Wady i ograniczenia





- Brak wbudowanych automatycznych aktualizacji:** LibreWolf nie aktualizuje się sam. To ty musisz instalować nowe wersje, gdy tylko zostaną wydane, aby zachować bezpieczeństwo.





- Ograniczona kompatybilność z niektórymi usługami:** Ze względu na bardzo rygorystyczne ustawienia, LibreWolf może napotkać problemy na niektórych stronach internetowych. Platformy streamingowe Netflix i Disney+ nie będą działać, ponieważ LibreWolf domyślnie wyłącza Widevine DRM.





- Brak wbudowanej anonimowej sieci:** W przeciwieństwie do przeglądarki Tor, LibreWolf nie przekierowuje ruchu przez sieć Tor lub VPN. Jeśli potrzebujesz anonimowości w sieci, musisz ręcznie skonfigurować proxy/VPN.





- Nietrwałe pliki cookie i sesje (domyślnie):** Ze względu na poufność LibreWolf usuwa pliki cookie, historię i dane witryny za każdym razem, gdy zamykasz przeglądarkę. Konieczne będzie ponowne zalogowanie się na swoje konta przy każdym logowaniu.





- Brak wersji mobilnej lub synchronizacji w chmurze:** LibreWolf jest dostępny tylko na komputerach stacjonarnych (Windows, Linux, macOS). Nie ma aplikacji mobilnej, a zatem nie ma synchronizacji kont lub zakładek za pośrednictwem chmury.



## Instalacja LibreWolf



**Oficjalna strona internetowa:** [librewolf.net](https://librewolf.net)



LibreWolf jest dostępny dla wszystkich głównych systemów operacyjnych: Linux, Windows i macOS. Aby pobrać LibreWolf, odwiedź oficjalną stronę internetową:



![LIBREWOLF](assets/fr/02.webp)


*Strona główna LibreWolf (librewolf.net) z logo przeglądarki, niebieskim przyciskiem Zainstaluj oraz linkami do kodu źródłowego i dokumentacji. Duża niebieska strzałka wskazuje na przycisk Zainstaluj*



Kliknij przycisk "Instalacja", aby uzyskać dostęp do szczegółowych instrukcji dla swojego systemu operacyjnego:



![LIBREWOLF](assets/fr/03.webp)


*Strona wyboru systemu operacyjnego dla LibreWolf.* download



Instalacja różni się w zależności od systemu operacyjnego:



### W systemie Linux


LibreWolf oferuje kompilacje dla wielu dystrybucji. Dla Debiana/Ubuntu i pochodnych dostępne jest oficjalne repozytorium APT. Alternatywnie, LibreWolf jest publikowany we Flatpak na Flathub:


```
flatpak install flathub io.gitlab.librewolf-community
```



### W systemie Windows


Pobierz instalator (.exe) z oficjalnej strony internetowej lub użyj:




- Chocolatey:** `choco install librewolf`
- WinGet:** `winget install librewolf`



### Na macOS


LibreWolf jest dostępny jako pakiet .dmg dla komputerów Mac. Pobierz obraz dysku z oficjalnej strony internetowej i przeciągnij aplikację LibreWolf do folderu Aplikacje. Alternatywnie, można ją zainstalować za pośrednictwem Homebrew.




## Konfiguracja i pierwsze użycie



Przy pierwszym uruchomieniu zauważysz znajomy Firefox Interface, z wyjątkiem tego, że jest on bardziej okrojony: strona główna zawiera tylko pasek wyszukiwania i nie zawiera sponsorowanych sugestii. Na pasku narzędzi widoczna jest ikona uBlock Origin - znak, że blokada jest aktywna.



![LIBREWOLF](assets/fr/04.webp)


*Strona główna LibreWolf z rozszerzeniami i menu. Niebieska strzałka w prawym górnym rogu wskazuje ikonę menu (trzy poziome paski)



LibreWolf automatycznie ładuje strony w trybie "ścisłym" (zapobiegającym śledzeniu), a domyślną wyszukiwarką będzie DuckDuckGo. Możesz spróbować odwiedzić testową witrynę śledzącą (np. amiunique.org), aby zaobserwować ujawniony ślad - powinien być znacznie bardziej ogólny niż w przypadku standardowej przeglądarki.



### Ustawienia prywatności



LibreWolf jest już optymalnie skonfigurowany pod kątem prywatności. W Menu → Opcje → Prywatność i bezpieczeństwo zobaczysz, że LibreWolf jest ustawiony na tryb Ulepszonej ochrony przed śledzeniem: Strict. Tryb ten blokuje:




- Urządzenia śledzące między witrynami
- Pliki cookie stron trzecich
- Znana zawartość śledzenia
- Cryptomining
- Cyfrowe detektory odcisków palców



![LIBREWOLF](assets/fr/05.webp)


*Strona zakładki Bezpieczeństwo i prywatność pokazująca ustawienia zabezpieczeń LibreWolf.*



WebRTC jest wyłączony (zapobiegając wyciekom IP), a Total Cookie Protection jest na miejscu. Telemetria i ankiety Firefox są całkowicie wyłączone.



### Zarządzanie plikami cookie i historią



Domyślnie LibreWolf usuwa pliki cookie i pamięć lokalną przy każdym zamknięciu. Jeśli przeszkadza ci to zachowanie, możesz je dostosować w sekcji Prywatność i bezpieczeństwo → Pliki cookie i dane witryny, odznaczając opcję "Usuń pliki cookie i dane witryny podczas zamykania LibreWolf".



![LIBREWOLF](assets/fr/06.webp)


*Ta sama strona nieco dalej, pokazująca opcję usuwania plików cookie po zamknięciu przeglądarki*



### Dodawanie przydatnych rozszerzeń



Zasadniczo LibreWolf odradza dodawanie niepotrzebnych rozszerzeń, ponieważ każde rozszerzenie może być wektorem śledzenia. Niemniej jednak, niektóre renomowane rozszerzenia mogą poprawić komfort użytkowania:




- Firefox Multi-Account Containers** (Mozilla) do przeglądania podzielonego na przedziały
- Decentraleyes** lub **LocalCDN** do lokalnej obsługi popularnych bibliotek



W szczególności unikaj "darmowych rozszerzeń VPN" lub wątpliwych serwerów proxy - uBlock Origin zaspokaja już 99% Twoich potrzeb.



## Codzienne użytkowanie



### Codzienne przeglądanie stron internetowych


Używaj LibreWolf do codziennej aktywności w Internecie. Główną różnicą w porównaniu z innymi przeglądarkami jest to, że pozostawia znacznie mniej śladów reklamowych. Banery "Akceptuj ciasteczka" znikają z wielu witryn dzięki listom filtrowania uBlock.



### Używaj prywatnych kart do podziału na przedziały


Mimo że LibreWolf usuwa wszystko po zakończeniu sesji, przydatne może być otwarcie prywatnego okna przeglądarki (Ctrl+Shift+P) dla niektórych zadań podczas sesji, aby oddzielić określoną tożsamość.



### Skorzystaj z kontenerów z wieloma kontami


Zainstalowanie rozszerzenia Multi-Account Containers może znacznie pomóc w segmentacji działań w szczelne silosy. Na przykład można zdefiniować kontener "Bankowość" dla witryn bankowych, kontener "Sieci społecznościowe" dla Facebooka/Twittera itp. Każdy kontener ma własne pliki cookie, sesje i odizolowaną pamięć masową. Każdy kontener ma własne pliki cookie, sesje i izolowaną pamięć masową.



### Precyzyjne zarządzanie uprawnieniami według lokalizacji


LibreWolf pozwala kontrolować uprawnienia nadawane witrynom (lokalizacja, kamera, mikrofon, powiadomienia) w poszczególnych przypadkach. Udzielaj uprawnień tylko zaufanym witrynom i tam, gdzie jest to konieczne.



## Najlepsze praktyki z LibreWolf



1. **Dbaj o aktualność LibreWolf:** Regularnie sprawdzaj stronę pod kątem nowych wersji, zwłaszcza po wydaniu stabilnej wersji Firefoksa.



2. **Unikaj mieszania tożsamości osobistej z prywatnym przeglądaniem:** Najlepiej byłoby, gdybyś nie logował się na swoje osobiste konta w tej samej sesji, w której wykonujesz poufne badania.



3. **Nie przeciążaj LibreWolf zbędnymi rozszerzeniami:** Każde zainstalowane rozszerzenie może wprowadzać ryzyko związane z bezpieczeństwem lub fingerprintingiem.



4. **Używaj dodatkowo VPN lub proxy Tor:** LibreWolf nie zapewnia anonimowości dla dostawcy usług internetowych. Aby uzyskać anonimowość w sieci, można używać LibreWolf za zaufaną siecią VPN.



5. **Zapisywanie ważnych danych:** Zakładki, hasła, jeśli są przechowywane lokalnie. Rozważ zewnętrzny menedżer haseł (KeePassXC, Bitwarden) zamiast podstawowego menedżera haseł przeglądarki.



## Porównanie z innymi przeglądarkami



LibreWolf jest częścią "zestawu narzędzi" przeglądarek zorientowanych na prywatność:



**LibreWolf vs. Firefox:** LibreWolf jest już zahartowany i nie posiada żadnych danych telemetrycznych. Firefox zachowuje przewagę synchronizacji wielu urządzeń i bardzo dużej bazy użytkowników, ale wymaga ręcznej konfiguracji, aby osiągnąć poziom poufności LibreWolf.



**Brave wykorzystuje kod Chrome/Chromium i integruje model biznesowy poprzez opcjonalny program reklamowy. LibreWolf, będąc społecznościowym Fork dla Firefoksa, zachowuje wolny ekosystem Mozilli i nie ma powiązań z Google.



**LibreWolf vs Tor Browser:** Tor Browser jest niezastąpiony do zachowania anonimowości w obliczu potężnej inwigilacji, ale jest powolny i niewygodny w codziennym użytkowaniu. LibreWolf, do codziennego przeglądania klasycznej sieci, jest znacznie szybszy i bardziej praktyczny.



**LibreWolf vs Mullvad Browser:** Mullvad Browser idzie jeszcze dalej w standaryzacji, ale kosztem zmniejszonej użyteczności (niemożliwe jest zachowanie pliku cookie logowania). LibreWolf zachowuje równowagę: bardzo prywatny, ale użyteczny na co dzień.



## Wnioski



LibreWolf stanowi doskonałe rozwiązanie dla tych, którzy szukają ultra-prywatnej przeglądarki "na co dzień", nie posuwając się tak daleko, jak ekstremalna anonimowość Tora. Jest to idealny wybór dla aktywistów, dziennikarzy, programistów lub zaawansowanych użytkowników, którzy chcą klasycznego przeglądania sieci (szybkiego, kompatybilnego z nowoczesnymi witrynami), jednocześnie unikając śledzenia reklam i Big Tech.



Mimo pewnych ograniczeń (brak automatycznych aktualizacji, ograniczona kompatybilność z niektórymi usługami), LibreWolf jest cennym narzędziem w arsenale każdego, kto chce odzyskać kontrolę nad swoją cyfrową prywatnością. Łatwość obsługi i domyślna konfiguracja sprawiają, że jest to mądry wybór dla użytkowników dbających o prywatność.



## Zasoby



### Oficjalna dokumentacja




- [Oficjalna strona LibreWolf](https://librewolf.net)
- [Kod źródłowy na Codeberg](https://codeberg.org/librewolf)
- [Oficjalne FAQ](https://librewolf.net/docs/faq)



### Przewodniki i porównania




- [Privacy Guides](https://www.privacyguides.org/en/desktop-browsers/)
- [Porównawcze testy prywatności](https://privacytests.org)



### Wsparcie społeczności




- [Subreddit r/LibreWolf](https://www.reddit.com/r/LibreWolf/)
- [Canal Matrix LibreWolf](https://matrix.to/#/#librewolf:matrix.org)