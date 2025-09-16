---
name: GrapheneOS

description: Mobilny system operacyjny skoncentrowany na bezpieczeństwie i prywatności, oparty na Androidzie
---

![cover](assets/cover.webp)
> [GrapheneOS](https://grapheneos.org/) to non-profitowy, otwartoźródłowy mobilny system operacyjny, zaprojektowany, aby zapewniać wysoki poziom prywatności i bezpieczeństwa, pozostając w pełni kompatybilnym z aplikacjami Android.

GrapheneOS, pierwotnie założony w 2014 roku jako "CopperheadOS", oparty jest na tradycyjnym kodzie Androida (AOSP), ale z wieloma zmianami i ulepszeniami mającymi na celu poprawę prywatności i bezpieczeństwa użytkowników. GrapheneOS daje użytkownikowi kontrolę nad jego telefonem, a nie wielkim firmom technologicznym.


![video](https://youtu.be/VnumtalYLFI)

### Sommaire:



- Wprowadzenie
- Przygotowanie
- Instalacja
- Alternatywy dla aplikacji
- Wady
- Przydatne informacje


*Ten poradnik jest adaptacją oryginalnej treści opublikowanej przez [BitcoinQnA na Bitcoiner.Guide na licencji MIT](https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md), któremu należy się pełne uznanie za pierwotną pracę redakcyjną.*


## Dlaczego warto korzystać z GrapheneOS?


Nowoczesne telefony to kosztujące od 500 do 1000 dolarów urządzenia śledzące i zbierające dane. Każdy aspekt naszego życia przechodzi przez nie i niestety wiele z tych danych jest udostępnianych stronom trzecim w takiej czy innej formie.

GrapheneOS został stworzony specjalnie w celu ograniczenia udostępniania danych i poprawy bezpieczeństwa urządzenia przed potencjalnymi wektorami ataków. Nie ma czegoś takiego jak konto GrapheneOS. Nie jest ono potrzebne do pobierania aplikacji lub interakcji z systemem operacyjnym. Mówiąc prościej, nie jesteś produktem.


GrapheneOS zapewnia dodatkowe bezpieczeństwo systemu Android dzięki kilku prostym podstawowym zasadom.


1. **Zmniejszenie powierzchni ataku** - Usunięcie niepotrzebnego kodu (lub oprogramowania typu bloatware).

2. **Zapobieganie ekspozycji na podatności** - Zapewnienie użytkownikowi wystarczającej szczegółowości, aby mógł wybrać kompromisy, z którymi czuje się komfortowo.

3. **Sandbox containment** - GrapheneOS wzmacnia istniejące piaskownice Androida, dodatkowo blokując możliwość komunikacji każdej aplikacji z resztą telefonu.


Dowiedz się więcej o szczegółach technicznych zestawu funkcji GrapheneOS [tutaj] (https://grapheneos.org/features).


### Ułatwienie przejścia


Jeśli od lat jesteś zakorzeniony w ekosystemie Google lub Apple, myśl o utracie całej tej wygody z dnia na dzień może być przerażająca. Ale dzięki starannie przemyślanym decyzjom dotyczącym instalacji aplikacji (omówionym później), wiele z tych oczekiwanych trudności można zmniejszyć lub usunąć.


Choć alternatywy stają się coraz lepsze, myśl o takiej zmianie wciąż może być zniechęcająca. Jeśli znajdziesz się w takiej sytuacji, moją najlepszą radą jest uruchomienie nowego urządzenia GrapheneOS wraz z istniejącym telefonem na jakiś czas. Stamtąd możesz powoli odzwyczajać się od 2-3 aplikacji tygodniowo, aż w końcu będziesz sięgać tylko po urządzenie z GrapheneOS.


Jeśli przyjmiesz takie podejście, bądź dla siebie surowy i jak najszybciej przestań polegać na monitorowanych alternatywach. My, ludzie, jesteśmy leniwi i często wybieramy drogę najmniejszego oporu. Pamiętaj, dlaczego w ogóle dokonałeś zmiany.


**Zamiast płacić swoimi danymi osobowymi, zdecydowałeś się zapłacić swoim czasem, a czasem zarobionymi pieniędzmi Hard (w zależności od zainstalowanych alternatywnych aplikacji) **


## Pierwsze kroki


GrapheneOS jest obecnie produkowany tylko dla _(raczej ironicznie)_ serii telefonów [Google Pixel](https://grapheneos.org/faq#supported-devices). Nie dzieje się tak jednak bez powodu. Pixele oferują najlepsze zabezpieczenia sprzętowe, które uzupełniają pracę wykonaną w celu wzmocnienia systemu operacyjnego. Obejmuje to takie rzeczy, jak izolacja określonych komponentów i zweryfikowany rozruch.


### Wybór urządzenia


Wybierając Pixela, na którym chcesz zainstalować GrapheneOS, sprawdź, jak długo urządzenie będzie otrzymywać domyślne [aktualizacje zabezpieczeń] (https://support.google.com/pixelphone/answer/4457705?hl=en#zippy=%2Cpixel-xl-a-a-g-a-g).


W chwili pisania tego tekstu Pixel 6a jest najtańszym dostępnym modelem z dobrym długoterminowym wsparciem, gwarantowanym do lipca 2027 roku. Jeśli wybierzesz ten model, odblokowanie OEM nie będzie działać z fabryczną wersją systemu operacyjnego. Musisz zaktualizować go do wersji z czerwca 2022 r. lub nowszej za pomocą aktualizacji bezprzewodowej. Po aktualizacji konieczne będzie również przywrócenie ustawień fabrycznych urządzenia, aby naprawić odblokowanie OEM. Wszystkie inne modele, które są odblokowane przez operatora, będą gotowe na GrapheneOS zaraz po wyjęciu z pudełka.


Wybierając urządzenie, warto również upewnić się, że kupujesz odblokowaną wersję. Niektórzy operatorzy, tacy jak Verizon, dostarczają swoje urządzenia z zablokowanym bootloaderem, co całkowicie uniemożliwia następujący proces.


### Instalacja GrapheneOS


GrapheneOS [web installer](https://grapheneos.org/install/web) sprawia, że cały proces jest bardzo prosty i może być wykonany przez każdego w mniej niż 10 minut.

Poniższe instrukcje są okrojoną wersją zaczerpniętą z powyższego linku.


Wszystko, co musisz podać, to:



- Pixel
- Kabel USB do połączenia telefonu z komputerem
- Komputer umożliwiający uruchomienie przeglądarki internetowej (dowolnej przeglądarki opartej na Chromium: Chrome, Edge, Brave itp.)


Zanurzmy się w to:


1. Pierwszym krokiem jest przejście do **Ustawienia** > **Informacje o telefonie** i kilkakrotne dotknięcie numeru kompilacji, aż pojawi się **"Tryb programisty "**.

2. Następnie przejdź do **Ustawienia** > **System** > **Opcje deweloperskie** i włącz **Odblokowanie OEM**.

3. Teraz zrestartuj urządzenie i przytrzymaj przycisk zmniejszania głośności podczas ponownego włączania telefonu.

4. Podłącz telefon do laptopa i jeśli pojawi się monit o autoryzację, zezwól na połączenie.

5. Na stronie instalatora kliknij "Odblokuj bootloader".

6. Opcje telefonu ulegną zmianie. Użyj przycisku głośności, aby zmienić wybór na "odblokuj" i użyj przycisku zasilania, aby zaakceptować.

7. Następnie kliknij przycisk Download Release na stronie instalatora.

8. Po pełnym pobraniu przejdź do następnego kroku i kliknij "Flash release". Zajmie to minutę lub dwie i nie musisz w ogóle dotykać telefonu.

9. Na koniec przejdź do następnego kroku instalatora internetowego i kliknij **Lock Bootloader**. Będziesz musiał zmienić wybór i potwierdzić przyciskiem zasilania w taki sam sposób, jak wcześniej.

10. Gdy zobaczysz słowo "Start", potwierdź je przyciskiem zasilania, a urządzenie uruchomi się w nowym systemie operacyjnym bez Google.


![image](assets/fr/2.webp)

Ekran startowy GrapheneOS



po pierwszym uruchomieniu i konfiguracji dobrą praktyką jest wyłączenie odblokowywania OEM w Ustawieniach > System > Opcje programisty


możesz także wykonać dodatkowy, opcjonalny, ale zalecany krok weryfikacji instalacji za pośrednictwem aplikacji Auditor. Do wykonania tego kroku potrzebny będzie oddzielny telefon z systemem Android z zainstalowaną aplikacją. Instrukcje na ten temat można znaleźć [tutaj](https://attestation.app/tutorial)._



![video](https://www.youtube.com/embed/L1KZWjZVnAw)

Film przedstawiający proste kroki opisane powyżej



Jeśli te proste kroki wydają się zbyt daleko idące, możesz rozważyć zakup Pixela z oprogramowaniem GrapheneOS [preinstalowanym] (https://ronindojo.io/en/roninmobile). Pamiętaj tylko, że pokładasz niewielkie zaufanie w dostawcy.


### Wstępnie zainstalowane aplikacje


Teraz, gdy jesteś już skonfigurowany, możesz zauważyć, jak gołe kości GrapheneOS pojawiają się przy pierwszej instalacji. Domyślnie zainstalowane są następujące aplikacje:


![image](assets/fr/3.webp)


Domyślne aplikacje


Jedyne dwa, których możesz nie znać, to "Auditor" i "Vanadium".



- Aplikacja [Auditor app](https://play.google.com/store/apps/details?id=app.attestation.auditor) wykorzystuje sprzętowe funkcje zabezpieczeń do weryfikacji tożsamości urządzenia oraz autentyczności i integralności systemu operacyjnego. Weryfikuje, czy na urządzeniu działa standardowy system operacyjny z zablokowanym bootloaderem i czy nie doszło do ingerencji w system operacyjny.
- [Vanadium](https://github.com/GrapheneOS/Vanadium) to wzmocniony pod względem prywatności i bezpieczeństwa wariant przeglądarki internetowej Chromium.


## Personalizacja


Ustawienia telefonu to kwestia osobista, ale oto kilka pierwszych elementów, które zmieniam po zainstalowaniu GrapheneOS, aby poczuć się bardziej jak w domu.


### Ustawianie tapety i aktualizacja motywu


Przejdź do Ustawienia > Tapeta i styl. Stąd:



- Aktualizacja tła ekranu głównego i ekranu blokady dla obrazów pobranych z Internetu.
- Wybór kolorów akcentujących używanych w całym interfejsie użytkownika.
- Włącz ciemny motyw.


### Pokaż procent baterii


Przejdź do **Ustawienia** > **Bateria**, a następnie włącz **Pokaż procent baterii** na pasku stanu.


### Importuj kontakty


**Z innego telefonu z Androidem** - Przejdź do aplikacji Kontakty i poszukaj opcji Eksportuj do VCF.


**Z iOS** - Użyj aplikacji takiej jak Export Contact i użyj opcji eksportu "vCard", aby wyeksportować plik VCF.

Po uzyskaniu pliku VCF można go przenieść na urządzenie GrapheneOS za pomocą zewnętrznej pamięci masowej, takiej jak karta microSD lub dysk USB. Jeśli nie masz pod ręką żadnej z tych opcji, możesz zdecydować się na udostępnienie za pośrednictwem jednej z wielu aplikacji wymienionych poniżej.


![image](assets/fr/4.webp)


Spersonalizowany ekran główny



## Alternatywne aplikacje


Aby uczynić swój telefon użytecznym, będziesz chciał zainstalować kilka aplikacji! Poniższe opcje zostały uwzględnione, ponieważ korzystałem z nich osobiście lub ponieważ otrzymały one silne rekomendacje od szerszej społeczności zajmującej się prywatnością. Istnieje wiele innych świetnych alternatyw, które nie zostały wymienione, a [Awesome Privacy](https://awesome-privacy.xyz) oferuje niezwykle obszerną listę aplikacji chroniących prywatność dla wszystkich typów urządzeń.


Tylko dlatego, że aplikacja jest wolnym i otwartym oprogramowaniem (FOSS), nie oznacza, że jest wolna od potencjalnych wycieków prywatności. Skorzystaj z [Exodus](https://reports.exodus-privacy.eu.org/en/), aby sprawdzić, jak preferowane aplikacje radzą sobie z audytami prywatności.


### F-Droid


[F-Droid](https://f-droid.org/) to instalowalny katalog aplikacji FOSS dla systemu Android. Klient ułatwia przeglądanie, instalowanie i aktualizowanie aplikacji na urządzeniu. Warto wspomnieć, że aktualizacje za pośrednictwem F-Droid mogą być czasami wolniejsze niż w przypadku innych sklepów z aplikacjami. Zależy to głównie od tego, czy aplikacja została znaleziona za pośrednictwem głównego repozytorium F-Droid, czy też niestandardowego.


Aby zainstalować F-Droid, po prostu przejdź do ich strony internetowej za pośrednictwem przeglądarki na telefonie z systemem GrapheneOS i dotknij pobierz. Spowoduje to pobranie pliku `.apk`. Następnie zostaniesz zapytany, czy chcesz zainstalować aplikację.


Oprócz aplikacji znajdujących się w domyślnym repozytorium w F-Droid, wiele projektów Open Source będzie również hostować własne repozytorium, które można dodać w ustawieniach aplikacji F-Droid. W takim przypadku dany projekt przeprowadzi Cię przez bardzo proste kroki wymagane do osiągnięcia tego celu na swojej stronie internetowej.


![image](assets/fr/5.webp)


Ekran główny F-Droid


https://planb.network/tutorials/computer-security/data/f-droid-2cd1aae5-7028-4c04-8fbe-95aeaf278ef4

### Sklep Aurora


[Aurora Store](https://auroraoss.com/) jest wersją FOSS sklepu Google Play. Aurora wygląda i działa bardzo podobnie do tradycyjnego Sklepu Play i umożliwia pobieranie i aktualizowanie dowolnej aplikacji, którą normalnie można znaleźć za pośrednictwem opcji Google.


Najważniejszą cechą Aurory jest anonimowe logowanie. Oznacza to, że możesz pobierać dowolne ulubione aplikacje, które nie są dostępne za pośrednictwem F-Droid lub bezpośredniego APK, bez konieczności logowania się na konto Google.


Zanim pośpieszysz się, aby uczynić tę opcję domyślną opcją instalacji, pamiętaj, że wiele aplikacji, od których próbujemy się uwolnić, zostało zainstalowanych ze Sklepu Play. Tylko dlatego, że są one dostępne z Aurory, nie zmienia faktu, że niektóre z nich mogą mieć wbudowane funkcje śledzenia. Nie zawsze będzie to możliwe, ale jeśli tylko możesz, poszukaj alternatywy F-Droid przed pobraniem za pośrednictwem Aurory.


Aby zainstalować Aurorę, wystarczy wyszukać "Aurora Store" w F-Droid.


Aurora ma również pewne potencjalne wektory ataku, ponieważ "anonimowe konta" są w rzeczywistości tworzone i kontrolowane przez Aurorę. Teoretycznie mogą one obsługiwać złośliwe aktualizacje lub przesyłać aplikacje na telefon, chociaż nadal będziesz musiał zaakceptować monit o instalację na urządzeniu. Aurora ma również czasami pewne problemy z aplikacjami, które nie są wyświetlane z powodu błędnego odczytu regionu i urządzenia. Zwykle można to obejść, wykonując poniższe czynności.


**Główna wskazówka** - Czasami w sklepie Aurora Store występuje ograniczenie szybkości, które ogranicza możliwość wyszukiwania i instalowania aplikacji. Aby to obejść, przejdź do **Ustawienia** > **Apps** > **Aurora** > **Otwórz domyślnie**, a następnie dodaj domenę `play.google.com`. Teraz za każdym razem, gdy przejdziesz do strony internetowej produktu lub usługi, na której znajduje się link "Pobierz ze Sklepu Play", dotknięcie go otworzy tę aplikację w Aurorze do pobrania.



![image](assets/fr/6.webp)


Ekran główny Aurora Store


https://planb.network/tutorials/computer-security/data/aurora-store-b3345da7-1ed1-407e-a9ae-a1c7f0ba9967

### Pobierz APK


Aplikacje na Androida można również pobrać i zainstalować za pomocą pliku `.apk`. Jest to świetna alternatywa, która nie wymaga zewnętrznych sklepów z aplikacjami, wystarczy pobrać plik bezpośrednio ze strony internetowej projektu lub usługi lub repozytorium GitHub.


Wadą tego podejścia jest to, że nie otrzymujesz automatycznych aktualizacji, więc musisz monitorować kanały komunikacji tej usługi, aby dowiedzieć się o nowych wersjach. Istnieje jednak świetny projekt o nazwie Obtanium, który ma to naprawić. [Obtainium](https://github.com/ImranR98/Obtainium) pozwala instalować i aktualizować aplikacje Open-Source bezpośrednio ze stron ich wydań, a także otrzymywać powiadomienia o udostępnieniu nowych wydań.


![image](assets/fr/7.webp)


Zapowiedź Obtanium


### Aplikacje internetowe


W przypadku, gdy chcesz rzadko korzystać z usługi i nie chcesz pobierać natywnej aplikacji, możesz po prostu uzyskać dostęp do wersji internetowej. Wiele witryn oferuje obecnie również obsługę progresywnych aplikacji internetowych (PWA). Polega to na tym, że możesz dodać zakładkę do konkretnej witryny (np. Twitter.com) na ekranie głównym telefonu. Następnie po dotknięciu ikony otwiera się ona jako pełnoekranowa aplikacja bez typowych zakłóceń, które pojawiają się w typowej przeglądarce. Przykład tego, jak to wygląda, można zobaczyć poniżej.


Aby to osiągnąć w Vanadium, natywnej przeglądarce GrapheneOS, wystarczy przejść do wybranej strony internetowej, dotknąć trzech pionowych kropek w prawym górnym rogu ekranu, a następnie dotknąć **"Dodaj do ekranu głównego "**.


Jedyną wadą tego podejścia jest to, że ponieważ jest to tylko strona internetowa z zakładkami, nie otrzymasz żadnej formy powiadomień. Choć niektórzy mogą uznać to za zaletę!


![image](assets/fr/8.webp)


Twitter PWA


### Przeglądarki internetowe


Naprawdę nie można się pomylić z wstępnie spakowaną opcją, Vanadium. Aplikacja zachowuje się identycznie jak każda inna przeglądarka mobilna, którą wypróbowałem i ani razu nie miałem żadnych problemów z kompatybilnością.


W przypadku konieczności uzyskania dostępu do natywnych witryn Tor `.onion`, można pobrać pakiet Tor Browser APK bezpośrednio z ich [strony internetowej] (https://www.torproject.org/download/#android) lub za pośrednictwem F-Droid.


### VPN


Aby chronić swoją aktywność online przed szpiegującym dostawcą usług internetowych (ISP), dobrym rozwiązaniem jest aplikacja wirtualnej sieci prywatnej (VPN). VPN wysyła ruch internetowy w zaszyfrowanym tunelu do współdzielonego adresu IP Address kontrolowanego przez dostawcę usług VPN, aby zapewnić, że aktywność urządzenia nie może być z nim powiązana.


Oto dwie uznane opcje, które umożliwiają opłacenie usługi w Bitcoinach bez podawania jakichkolwiek danych osobowych. Obie są dostępne na F-Droid.





https://planb.network/tutorials/computer-security/communication/ivpn-5a0cd5df-29f1-4382-a817-975a96646e68

https://planb.network/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Wiadomości


W ostatnich latach szyfrowane rozwiązania do przesyłania wiadomości stały się bardzo popularne. Problemem pozostaje jednak to, że możesz mieć najlepszą i najbardziej prywatną opcję zainstalowaną na swoim telefonie, ale jeśli nie masz kontaktów, które z niej korzystają, to jaki to ma sens?


Większość osób, które nie są zainteresowane przestrzenią prywatności, prawdopodobnie korzysta z WhatsApp lub iMessage. Pierwszy z nich można pobrać za pośrednictwem Aurora Store, ale drugi nie będzie działał na GrapheneOS (oczywiście!).



- [Signal](https://signal.org/) to jeden z najpopularniejszych szyfrowanych komunikatorów typu end-to-end (E2EE), który ma duże osiągnięcia i bogaty zestaw funkcji. Signal wymaga podania numeru telefonu do rejestracji, więc jeśli planujesz czatować z osobami, które wolałbyś, aby nie znały Twojego numeru telefonu, być może przyjrzyj się niektórym alternatywom. Signal należy pobrać za pośrednictwem Aurora Store.
- [Simplex](https://f-droid.org/en/packages/chat.simplex.app/) to całkiem nowy komunikator E2EE. Nie ma identyfikatora użytkownika, nie wymaga numeru telefonu ani danych osobowych. Ludzie znajdują cię poprzez zeskanowanie twojego osobistego kodu QR lub odwiedzając twój unikalny link. Simplex pozwala również zaawansowanym użytkownikom na uruchomienie własnego serwera, aby jeszcze bardziej zmniejszyć zależność od jakiegokolwiek scentralizowanego podmiotu. Simplex nie ma klienta desktopowego, więc może nie być odpowiedni, jeśli na liście priorytetów znajduje się wiele urządzeń. Simplex dla systemu Android jest dostępny za pośrednictwem F-Droid.
- [Threema](https://threema.ch/en/faq/libre_installation) oferuje podobne wrażenia jak Simplex, ale istnieje dłużej i w rezultacie wydaje się nieco bardziej dopracowana. Threema nie jest darmowa, dożywotnia licencja kosztuje 4,99 USD i można ją kupić za Bitcoin. Threema oferuje klienta webowego i natywne aplikacje desktopowe. Aplikacja na Androida jest dostępna za pośrednictwem F-Droid.
- [Telegram FOSS](https://f-droid.org/en/packages/org.telegram.messenger/) to nieoficjalny Fork FOSS oficjalnej aplikacji Telegram na Androida. Telegram ma "tajne czaty" E2EE, ale domyślna opcja nie jest prywatna. Telegram FOSS można pobrać z F-Droid.


![image](assets/fr/9.webp)

Po lewej: Threema, po prawej: Simplex


https://planb.network/tutorials/computer-security/communication/signal-8dfb5572-6962-4f1c-bfa5-3192da4e9a4e

https://planb.network/tutorials/computer-security/communication/telegram-09ab3cf3-7625-4267-97a1-24e59a9e5943

https://planb.network/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3

https://planb.network/tutorials/computer-security/communication/simplex-chat-7a1efa11-4d0a-49c4-92aa-e18bf22c22b9

https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74

### Media



- [Spotube](https://f-droid.org/packages/oss.krtirtho.spotube/) to wieloplatformowy klient Spotify, który nie wymaga konta Premium. Spotube jest dostępny za pośrednictwem F-Droid.
- [ViMusic](https://f-droid.org/en/packages/it.vfsfitvnm.vimusic/) to fantastyczna aplikacja do odtwarzania dowolnej muzyki z YouTube za darmo. ViMusic jest dostępny od F-Droid.
- [Newpipe](https://f-droid.org/packages/org.schabi.newpipe/) oferuje YouTube bez irytujących reklam i wątpliwych uprawnień. Dzięki NewPipe możesz subskrybować kanały, słuchać w tle, a nawet pobierać do oglądania offline. NewPipe jest dostępny za pośrednictwem F-Droid.
- [AntennaPod](https://f-droid.org/packages/de.danoeh.antennapod/) to odtwarzacz podcastów, który umożliwia subskrybowanie i zarządzanie wszystkimi ulubionymi programami. AntennaPod jest dostępny za pośrednictwem F-Droid.


![image](assets/fr/11.webp)

Po lewej: Spotube, po prawej: ViMusic


### Mapy


Jeśli chcesz uzyskać pomoc głosową podczas jazdy i korzystania z aplikacji map w systemie GrapheneOS, musisz zainstalować [RHVoice](https://rhvoice.org/installation/) i [skonfigurować](https://discuss.grapheneos.org/d/2488-organic-maps-app-voice-instructions-are-not-available).



- [Magic Earth](https://www.magicearth.com/) to alternatywa dla map, która obsługuje nawigację zakręt po zakręcie, mapy 3D i offline. Magic Earth można pobrać z Aurora Store.
- [Organic Maps](https://f-droid.org/en/packages/app.organicmaps/) to alternatywa dla map dla podróżników, turystów, pieszych i rowerzystów oparta na danych OpenStreetMap pochodzących z tłumu. Jest to skoncentrowana na prywatności, open-source Fork aplikacji Maps.me (wcześniej znanej jako MapsWithMe). Obsługuje 100% funkcji bez aktywnego połączenia z Internetem i można ją pobrać z F-Droid.
- [OsmAnd](https://f-droid.org/en/packages/net.osmand.plus/) to kolejna świetna alternatywa dla map, która obsługuje wszystkie funkcje wymienione powyżej.


![image](assets/fr/13.webp)

Po lewej: Magic Earth, po prawej: Organic Maps


### E-mail



- [Proton Mail](https://proton.me/mail) oferuje bezpłatną usługę prywatnej poczty e-mail, która obsługuje audyt E2EE. Proton oferuje również płatną wersję, która obsługuje niestandardowe domeny i [aliasing](https://proton.me/support/creating-aliases). Proton Mail można pobrać jako bezpośredni APK lub za pośrednictwem Aurory.
- [Tutanota](https://tutanota.com/) oferuje te same funkcje, co Proton Mail, w tym opcjonalne płatne usługi i można go pobrać jako bezpośredni plik APK lub za pośrednictwem F-Droid.
- [K-9 Mail](https://f-droid.org/en/packages/com.fsck.k9/) to klient poczty e-mail o otwartym kodzie źródłowym, który współpracuje z praktycznie każdym dostawcą poczty e-mail. Obsługuje wiele kont, ujednoliconą skrzynkę odbiorczą i standard szyfrowania OpenPGP.


![image](assets/fr/15.webp)

Po lewej: Proton Mail, po prawej: Tutanota


### Wydajność



- [Syncthing](https://f-droid.org/packages/com.nutomic.syncthingandroid/) to program do synchronizacji plików. Synchronizuje pliki między dwoma lub więcej urządzeniami w czasie rzeczywistym, bezpiecznie chronione przed wścibskimi oczami. Twoje dane są wyłącznie Twoimi danymi i zasługujesz na to, aby wybrać, gdzie są przechowywane, czy są udostępniane stronom trzecim i jak są przesyłane przez Internet. Syncthing jest dostępny za pośrednictwem F-Droid.
- [KDE Connect](https://f-droid.org/packages/org.kde.kdeconnect_tp/) wszystkie urządzenia mogą łatwo komunikować się ze sobą po podłączeniu do sieci domowej. Łatwe wysyłanie plików, zdjęć, danych schowka między wszystkimi urządzeniami (nawet na iOS!). KDE Connect można pobrać z F-Droid.
- [Notesnook](https://f-droid.org/en/packages/com.streetwriters.notesnook/) to aplikacja E2EE do synchronizacji myśli i list rzeczy do zrobienia na wszystkich urządzeniach. Ich darmowy plan powinien obejmować większość przypadków osobistego użytku. Notesnook jest dostępny na F-Droid.
- [Standard Notes](https://f-droid.org/en/packages/com.standardnotes/) jest bardzo podobny do Notesnook, ale wymaga płatnego planu, aby dopasować zestaw funkcji. Standard Notes jest dostępny za pośrednictwem F-Droid.
- [Anysoft Keyboard](https://f-droid.org/packages/com.menny.android.anysoftkeyboard/) to aplikacja klawiatury, która pozwala dostosować prawie wszystko, co można sobie wyobrazić, jeśli chodzi o pisanie na telefonie. Można ją pobrać za pośrednictwem F-Droid.
- [GBoard](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin&hl=en&gl=US) to domyślna aplikacja klawiatury Google. Z mojego doświadczenia wynika, że oferuje ona zdecydowanie najlepsze wrażenia podczas pisania i przesuwania. Jeśli pobierzesz tę aplikację, upewnij się, że całkowicie wyłączyłeś wszystkie uprawnienia związane z siecią. Można ją pobrać za pośrednictwem aplikacji Aurora.


![image](assets/fr/17.webp)

Po lewej: Notesnook, po prawej: KDE Connect


### Styl życia



- [Geometric Weather](https://f-droid.org/en/packages/wangdaye.com.geometricweather/) to pięknie zaprojektowana aplikacja pogodowa Open Source dostępna za pośrednictwem F-Droid. Obsługuje również wiele różnych rozmiarów widżetów, dzięki czemu można zobaczyć pogodę w wybranej lokalizacji bezpośrednio z ekranu głównego.
- [Translate You](https://f-droid.org/packages/com.bnyro.translate/) to aplikacja tłumaczeniowa typu open source i chroniąca prywatność, która obsługuje ponad 200 języków. Translate You jest dostępna za pośrednictwem F-Droid.
- [Proton Calendar](https://proton.me/calendar/download) to prosta w użyciu aplikacja E2EE, która płynnie współpracuje z kontami e-mail Proton. Proton Calendar można pobrać jako APK lub za pośrednictwem sklepu Aurora.
- [PassAndroid](https://f-droid.org/en/packages/org.ligi.passandroid/) to aplikacja do wyświetlania i przechowywania kart pokładowych, kuponów, biletów do kina, kart członkowskich itp. Wystarczy pobrać odpowiedni plik `pkpass` lub `espass` i otworzyć go za pomocą aplikacji. PassAndroid jest dostępny za pośrednictwem F-Droid.


![image](assets/fr/19.webp)

Po lewej: Geometryczna pogoda, po prawej: Kalendarz Proton


### Bezpieczeństwo/Prywatność



- [Bitwarden](https://mobileapp.bitwarden.com/fdroid/) oferuje bezpłatne i wieloplatformowe rozwiązanie do zarządzania hasłami E2EE dla wszystkich urządzeń. Ich płatna usługa pozwala zintegrować kody 2FA z aplikacją. Serwer Bitwarden może być hostowany samodzielnie, a aplikacja na Androida jest dostępna za pośrednictwem F-Droid.
- [Proton Pass](https://proton.me/pass/download) oferuje podobną bezpłatną usługę do Bitwarden, ale klienci [Proton Unlimited](https://proton.me/pricing) mają dostęp do dodatkowych zaawansowanych funkcji. Proton Pass jest dostępny za pośrednictwem APK lub Aurora.
- [FreeOTP](https://f-droid.org/packages/org.fedorahosted.freeotp/) to aplikacja do uwierzytelniania dwuskładnikowego dla systemów wykorzystujących protokoły haseł jednorazowych. Tokeny można łatwo dodawać, skanując kod QR. FreeOTP jest dostępny za pośrednictwem F-Droid.
- [Aegis](https://f-droid.org/en/packages/com.beemdevelopment.aegis/) to bezpłatna, bezpieczna i otwarta aplikacja dla systemu Android do zarządzania tokenami weryfikacji dwuetapowej dla usług online. Aegis jest dostępny za pośrednictwem F-Droid.
- [Cryptomator](https://f-droid.org/en/packages/org.cryptomator.lite/) to płatna, wieloplatformowa usługa, która szyfruje dane lokalnie, dzięki czemu można je bezpiecznie przesyłać do ulubionej usługi w chmurze. Cryptomator można pobrać za pośrednictwem F-Droid.


![image](assets/fr/21.webp)

Po lewej: Proton Pass,
po prawej: Bitwarden


https://planb.network/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

https://planb.network/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

https://planb.network/tutorials/computer-security/data/cryptomator-84e52c76-2253-49fe-81da-e05e90c28d0d

### Rozwiązania w chmurze



- [Proton Drive](https://proton.me/drive/download) to płatne rozwiązanie chmurowe E2EE do tworzenia kopii zapasowych i przechowywania wszystkich plików. W chwili pisania tego tekstu firma ogłosiła właśnie wprowadzenie klienta Windows na komputery stacjonarne, ale użytkownicy komputerów Mac i Linux muszą nadal korzystać z wersji internetowej do synchronizacji ze swoimi komputerami (na razie). Klient Android jest dostępny jako APK lub przez Aurora.
- [Skiff](https://skiff.com/download) oferuje również płatne narzędzia do przechowywania i współpracy plików w chmurze E2EE. Oferują one klienta na komputery Mac i Windows (a także aplikację internetową), a ich klientów na Androida należy pobrać z Aurory.
- [Nextcloud](https://f-droid.org/en/packages/com.nextcloud.client/) oferuje w pełni funkcjonalne rozwiązanie oparte na chmurze do współpracy, synchronizacji między urządzeniami i przechowywania plików. Bardziej zaawansowani użytkownicy mogą zdecydować się na samodzielne hostowanie swojego wolnego i otwartego oprogramowania na dowolnym sprzęcie. Klienty Android można pobrać za pośrednictwem F-Droid.
- [Cryptpad](https://cryptpad.fr/) oferuje bezpłatną, opartą na sieci Web, alternatywę E2EE dla Dokumentów Google.


![image](assets/fr/23.webp)

Proton Drive


https://planb.network/tutorials/computer-security/data/proton-drive-03cbe49f-6ddc-491f-8786-bc20d98ebb16

## Wady


Open Source i chroniące prywatność alternatywy dla aplikacji konglomeratów technologicznych, do których przywykłeś, są obfite, a niektóre z nich są często lepsze niż zamknięte, pełne oprogramowania szpiegującego alternatywy.


Jednak przechodząc na GrapheneOS, trzeba zrezygnować z pewnych udogodnień ze względu na brak alternatyw. Obejmują one:



- Apple CarPlay/Android Auto** - będziesz musiał pozostać przy starym, dobrym Bluetooth, USB lub Aux.
- Apple/Google Pay** - i tak prawie każdy ma przy sobie Wallet!
- Aplikacje bankowe** - Nie chodzi o to, że w ogóle nie działają. Niektóre działają doskonale. Inne działają tylko z włączonymi Usługami Google Play (więcej na ten temat poniżej), a jeszcze inne po prostu nie działają wcale. Przeczytaj raport na temat swojego banku [tutaj](https://privsec.dev/posts/android/banking-applications-compatibility-with-grapheneos/), aby zobaczyć aktualny stan rzeczy. Nie obawiaj się, jeśli Twój jest na liście, która nie działa, pamiętaj, że możesz po prostu zapisać adres URL jako aplikację internetową na ekranie głównym.
- Powiadomienia push** - Większość aplikacji, które wysyłają aktualizacje, gdy nie korzystasz z konkretnej aplikacji, robi to za pośrednictwem Usług Google Play. Nie są one domyślnie instalowane w systemie GrapheneOS, więc jeśli nie otrzymasz natychmiastowego powiadomienia, gdy Twój znajomy wyśle Ci wiadomość e-mail, prawdopodobnie jest to przyczyna. Dobrą wiadomością jest to, że niektóre z wyżej wymienionych aplikacji zaimplementowały własne połączenie w tle, aby okresowo sprawdzać dostępność aktualizacji, a następnie wysyłać powiadomienia w razie potrzeby


### Piaskownica Google Play


**Należy pamiętać, że:** GrapheneOS ma kompatybilność Layer zapewniającą opcję instalacji i korzystania z oficjalnych wydań Google Play w standardowej piaskownicy aplikacji. Google Play nie otrzymuje absolutnie żadnego specjalnego dostępu ani przywilejów w GrapheneOS, w przeciwieństwie do omijania piaskownicy aplikacji i otrzymywania ogromnej ilości wysoce uprzywilejowanego dostępu.


Jeśli okaże się, że po prostu nie możesz żyć bez powiadomień push dla swojej ulubionej aplikacji lub pewna aplikacja "must have" jest bezużyteczna bez usług Play, GrapheneOS pozwala [zainstalować](https://grapheneos.org/usage#sandboxed-google-play-installation) te usługi w całkowicie piaskownicowym środowisku. Po zainstalowaniu usługi te nie wymagają do działania konta Google, a uprawnienia każdej z nich można ściśle kontrolować.


Zanim w pośpiechu zainstalujesz je pierwszego dnia, zachęcam do sprawdzenia, jak daleko zajdziesz bez nich. Prawdopodobnie będziesz zaskoczony, jak wiele aplikacji działa bez nich zupełnie normalnie.


Jeśli chcesz je zainstalować, po prostu dotknij wstępnie zainstalowanej aplikacji "Aplikacje", a następnie "Usługi Google Play". Rozważ zainstalowanie ich obok tych mniej prywatnych aplikacji, bez których nie możesz żyć, w całkowicie oddzielnym profilu użytkownika, aby zapewnić dodatkowe Layer oddzielenia od reszty telefonu.


![image](assets/fr/24.webp)

Ekran instalacji usług Play


### Profile


GrapheneOS umożliwia korzystanie z oddzielnego telefonu. Dodatkowe profile mogą instalować własne aplikacje i usługi i nie mają dostępu do żadnych plików ani danych z konta właściciela.

Jeśli masz tylko jedną lub dwie z tych aplikacji, które wymagają Usług Play, ale są używane bardzo rzadko, zainstalowanie ich wraz z Usługami Play w osobnym profilu może być świetnym pomysłem, aby jeszcze bardziej wzmocnić wszelkie implikacje związane z prywatnością, które są pozostawione przez uruchomienie ich w profilu właściciela.


Więcej o tym przypadku użycia można przeczytać [tutaj] (https://discuss.grapheneos.org/d/168-ideas-for-user-profiles/2).


Jeśli zdecydujesz się dodać oddzielny profil, aby dopasować go do swojego przypadku użycia, aplikacja [Insular](https://f-droid.org/en/packages/com.oasisfeng.island.fdroid/) może być dla Ciebie przydatna. Insular pozwala łatwo sklonować dowolną z istniejących aplikacji do nowego profilu bez konieczności przechodzenia przez którąkolwiek z tradycyjnych ścieżek instalacji opisanych wcześniej w tym przewodniku. Insular pozwala również szybko "zamrozić" dowolną z tych aplikacji, aby całkowicie wyłączyć wszystkie usługi działające w tle.


![image](assets/fr/24.webp)

Ekran zarządzania profilem użytkownika


### e-Sims


Jeśli chcesz przenieść prywatność swojego telefonu na wyższy poziom i mieć usługę komórkową, która jest oddzielona od Twojej prawdziwej tożsamości, eSIM może być dla Ciebie. Karta eSIM to wirtualna karta SIM, którą można kupić online i dodać do telefonu za pomocą kodu QR. Firmy oferujące takie usługi, za które można płacić anonimowo za pomocą Bitcoin, to [Silent.Link](https://silent.link/) i [Bitrefill](https://www.bitrefill.com/gb/en/esims/).


karty eSIM nie powinny być postrzegane jako całkowite panaceum na prywatność telefonu. Mogą one być przydatnym narzędziem, gdy znajdują się we właściwych rękach, ale należy przeprowadzić badania na temat [kompromisów](https://grapheneos.org/faq#cellular-tracking) korzystania z dowolnego rodzaju usług komórkowych, jeśli zamierzasz całkowicie "odłączyć się od sieci".


W celu udostępnienia eSIM w systemie GrapheneOS należy zainstalować usługi Play w trybie piaskownicy.


## Kopie zapasowe


Po skonfigurowaniu nowego telefonu Pixel, warto utworzyć kopię zapasową. Ta kopia zapasowa umożliwi przywrócenie telefonu do identycznego stanu w przypadku jego utraty lub zgubienia/kradzieży.


Możesz zdecydować się na przechowywanie pliku kopii zapasowej na dowolnym zewnętrznym nośniku pamięci lub w samodzielnie hostowanym rozwiązaniu chmurowym, takim jak Nextcloud, chociaż niektórzy użytkownicy zgłaszają różne poziomy sukcesu tej drugiej opcji.


Aby utworzyć pierwszą kopię zapasową:


1. Przejdź do **Ustawienia** > **System** > **Kopia zapasowa**, a następnie zapisz 12-wyrazowy kod odzyskiwania. Kod ten jest wymagany do późniejszego odszyfrowania pliku kopii zapasowej. Utrata kodu oznacza utratę dostępu do kopii zapasowej telefonu.

2. Następnie wybierz miejsce przechowywania danych. Polecam zewnętrzny dysk USB lub kartę microSD klasy przemysłowej.

3. Wybierz dane, których kopia zapasowa ma zostać utworzona. Jeśli masz miejsce na określonym nośniku pamięci, radzę wybrać wszystko.

4. Dotknij trzech kropek w prawym górnym rogu i wybierz **Backup now**.


![image](assets/fr/26.webp)


Ekran kopii zapasowej


Pamiętaj, że jeśli tworzysz kopie zapasowe offline na zewnętrznym nośniku pamięci, warto regularnie wykonywać ten krok, aby upewnić się, że wszelkie ostatnie ważne aktualizacje telefonu nie zostaną utracone w przypadku najgorszego.


![video](https://www.youtube.com/embed/eyWmcItzisk)


Film przedstawiający proces tworzenia kopii zapasowej


## Wnioski


W ostatnich latach oprogramowanie GrapheneOS znacznie się rozwinęło. Jest bardziej stabilne i kompatybilne niż kiedykolwiek. W połączeniu z kwitnącym ekosystemem Open Source i aplikacjami chroniącymi prywatność sprawia, że GrapheneOS jest naprawdę realną alternatywą dla standardowego Androida lub iOS, nawet dla "zwykłych" ludzi, takich jak Ty!


Naruszenia danych i inwigilacja są tak powszechne w dzisiejszym świecie, że ledwo trafiają na pierwsze strony gazet. To od Ciebie zależy, jak się zabezpieczysz. Po drodze trzeba będzie dokonać dostosowań i poświęceń, ale zmniejszenie narażenia na takie naruszenia nie jest tak trudne, jak ci się wydaje.


Mam nadzieję, że ten przewodnik pomoże ci w twojej podróży. Jeśli uznałeś ten poradnik za przydatny i chciałbyś wesprzeć moją pracę, rozważ wysłanie [darowizny](/tips).


Jeśli jesteś już użytkownikiem GrapheneOS lub stałeś się nim w wyniku tego przewodnika, rozważ [darowiznę](https://grapheneos.org/donate), aby wesprzeć ich ważną pracę.


### Dowiedz się więcej


GrapheneOS to królicza nora, w której każdy może spędzić tygodnie. Jest tak wiele rzeczy, których można się nauczyć i przy których można majstrować, aby dostosować doświadczenie do swoich wymagań i modeli zagrożeń. Poniżej znajduje się kilka linków, pod którymi można kontynuować swoją podróż:



- [Oficjalny przewodnik użytkowania GrapheneOS](https://grapheneos.org/usage) - Oficjalna strona internetowa
- [Forum GrapheneOS](https://discuss.grapheneos.org/) - Oficjalna strona internetowa
- [GrapheneOS Settings Masterclass](https://www.youtube.com/watch?app=desktop&v=GLJyD9MJgIQ) - wideo przygotowane przez "The Privacy Wayfinder
- [GrapheneOS General Podcast](https://www.youtube.com/watch?app=desktop&v=UCPX0mFFRNA) - Podcast przygotowany przez 'Watchman Privacy'


*Ten poradnik jest adaptacją oryginalnej treści opublikowanej przez [BitcoinQnA na Bitcoiner.Guide na licencji MIT](https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md), któremu należy się pełne uznanie za pierwotną pracę redakcyjną.*

