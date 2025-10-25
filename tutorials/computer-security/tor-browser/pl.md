---
name: Tor Browser
description: Jak korzystać z przeglądarki Tor?
---
![cover](assets/cover.webp)


Jak sama nazwa wskazuje, przeglądarka to oprogramowanie używane do poruszania się po Internecie. Służy jako brama między komputerem użytkownika a siecią, tłumacząc kod stron internetowych na interaktywne i czytelne strony. Wybór przeglądarki jest bardzo ważny, ponieważ wpływa nie tylko na komfort przeglądania, ale także na bezpieczeństwo i prywatność w Internecie.


Należy uważać, aby nie pomylić przeglądarki z wyszukiwarką. Przeglądarka to oprogramowanie używane do uzyskiwania dostępu do Internetu (takie jak Chrome lub Firefox), podczas gdy wyszukiwarka to usługa, taka jak na przykład Google lub Bing, która pomaga znaleźć informacje online.


Obecnie Google Chrome jest zdecydowanie najczęściej używaną przeglądarką. Stanowi ona około 65% globalnego rynku w 2024 roku. Chrome jest ceniony za szybkość i wydajność, ale niekoniecznie jest najlepszym wyborem dla wszystkich, zwłaszcza jeśli prywatność jest dla ciebie priorytetem. Chrome należy do Google, firmy znanej z gromadzenia i analizowania ogromnych ilości danych o swoich użytkownikach. I rzeczywiście, ich wewnętrzna przeglądarka jest sercem ich strategii nadzoru. Oprogramowanie to jest centralnym elementem większości interakcji online. Opanowanie gromadzenia danych w przeglądarce jest ważną kwestią dla Google.

![TOR BROWSER](assets/notext/01.webp)

*Źródło: [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*


Istnieje kilka głównych rodzin przeglądarek, z których każda oparta jest na konkretnym silniku renderującym. Przeglądarki takie jak Google Chrome, Microsoft Edge, Brave, Opera czy Vivaldi są oparte na przeglądarce Chromium, lekkiej i otwartej wersji Chrome opracowanej przez Google. Wszystkie te przeglądarki korzystają z silnika renderującego Blink, który jest Fork WebKit, wywodzącego się z KHTML. Dominacja Chromium na rynku sprawia, że wywodzące się z niego przeglądarki są szczególnie wydajne, ponieważ twórcy stron internetowych mają tendencję do optymalizowania swoich witryn głównie pod kątem Blink.


Safari, przeglądarka Apple, korzysta z WebKit, który również pochodzi z KHTML.


Z drugiej strony, przeglądarki takie jak Mozilla Firefox, LibreWolf i Tor Browser opierają się na Gecko, innym silniku renderującym, pochodzącym z przeglądarki Netscape.


Wybór odpowiedniej przeglądarki zależy od potrzeb użytkownika. Jeśli jednak zależy ci przynajmniej na prywatności, a tym samym na bezpieczeństwie, polecam Firefox do ogólnego użytku i przeglądarkę Tor, aby zapewnić jeszcze większą prywatność. W tym samouczku pokażę ci, jak łatwo rozpocząć korzystanie z przeglądarki Tor.

![TOR BROWSER](assets/notext/02.webp)


## Wprowadzenie do przeglądarki Tor


Tor Browser to przeglądarka zaprojektowana specjalnie z myślą o bezpiecznej i jak najbardziej prywatnej nawigacji w Internecie. Przeglądarka bazuje na Firefoksie, a więc na silniku renderującym Gecko.

Przeglądarka Tor wykorzystuje sieć Tor do szyfrowania i kierowania ruchu przez wiele serwerów przekaźnikowych przed przesłaniem go do miejsca docelowego. Ten proces wielowarstwowego routingu, znany jako "*onion routing*", pomaga ukryć prawdziwe IP Address, utrudniając identyfikację lokalizacji i aktywności online. Przeglądanie jest jednak wolniejsze niż w przypadku standardowej przeglądarki, która nie korzysta z sieci Tor, ponieważ jest ona pośrednia.

W przeciwieństwie do innych przeglądarek, Tor Browser integruje określone funkcje zapobiegające śledzeniu aktywności online, takie jak izolowanie każdej odwiedzanej witryny i automatyczne usuwanie plików cookie i historii po zamknięciu. Została również zaprojektowana w celu zminimalizowania ryzyka odcisków palców, dzięki czemu wszyscy użytkownicy wydają się jak najbardziej podobni do odwiedzanych witryn.


Możesz bardzo dobrze używać przeglądarki Tor, aby uzyskać dostęp do standardowej strony internetowej (`.com`, `.org` itp.). W takim przypadku ruch jest anonimizowany poprzez przejście przez kilka węzłów Tor przed dotarciem do węzła wyjściowego, który komunikuje się z ostateczną witryną w Internecie.

![TOR BROWSER](assets/notext/03.webp)

Przeglądarki Tor można również używać do uzyskiwania dostępu do ukrytych usług (adresy kończące się na `.onion`). W tym scenariuszu cały ruch pozostaje w sieci Tor, bez węzła wyjściowego, zapewniając całkowitą prywatność zarówno użytkownikowi, jak i serwerowi docelowemu. Ten tryb działania jest w szczególności wykorzystywany do uzyskiwania dostępu do tego, co jest czasami nazywane "ciemną siecią", częścią Internetu, która nie jest indeksowana przez tradycyjne wyszukiwarki.

![TOR BROWSER](assets/notext/04.webp)


## Jaka jest różnica między siecią Tor a przeglądarką Tor?


Sieć Tor i przeglądarka Tor to dwie różne rzeczy, które nie powinny być mylone, ale wzajemnie się uzupełniają. Sieć Tor to globalna infrastruktura serwerów przekaźnikowych obsługiwanych przez użytkowników, która anonimizuje ruch internetowy, przepuszczając go przez kilka węzłów przed skierowaniem go do miejsca docelowego. Jest to słynny routing cebulowy.


Z drugiej strony, przeglądarka Tor to specjalna przeglądarka zaprojektowana w celu ułatwienia dostępu do tej sieci w prosty sposób. Domyślnie integruje wszystkie ustawienia niezbędne do połączenia się z siecią Tor i wykorzystuje zmodyfikowaną wersję Firefoksa, aby zapewnić znajome wrażenia podczas przeglądania, jednocześnie maksymalizując prywatność i bezpieczeństwo.


Sieć Tor jest używana nie tylko przez przeglądarkę Tor. Może być wykorzystywana przez różne oprogramowanie i aplikacje w celu zabezpieczenia ich komunikacji. Na przykład możliwe jest włączenie komunikacji za pośrednictwem sieci Tor na węźle Bitcoin, aby ukryć swój adres IP Address przed innymi użytkownikami i zapobiec monitorowaniu ruchu związanego z Bitcoin przez dostawcę usług internetowych.

Podsumowując, sieć Tor to infrastruktura, która zapewnia prywatność podczas przeglądania Internetu, a przeglądarka Tor to oprogramowanie, które pozwala nam korzystać z tej sieci w ramach przeglądania stron internetowych.


## Jak zainstalować przeglądarkę Tor?


Przeglądarka Tor Browser jest dostępna na komputery z systemami Windows, Linux i macOS, a także na smartfony z systemem Android. Aby zainstalować Tor Browser na swoim komputerze, odwiedź [oficjalną stronę Tor Project](https://www.torproject.org/).

![TOR BROWSER](assets/notext/05.webp)

Kliknij przycisk "*Pobierz przeglądarkę Tor*".

![TOR BROWSER](assets/notext/06.webp)

Wybierz wersję odpowiednią dla swojego systemu operacyjnego.

![TOR BROWSER](assets/notext/07.webp)

Kliknij plik wykonywalny, aby rozpocząć instalację, a następnie wybierz język.

![TOR BROWSER](assets/notext/08.webp)

Wybierz folder, w którym zostanie zainstalowane oprogramowanie, a następnie kliknij przycisk "*Install*".

![TOR BROWSER](assets/notext/09.webp)

Poczekaj na zakończenie instalacji.

![TOR BROWSER](assets/notext/10.webp)

Na koniec kliknij przycisk "*Zakończ*".

![TOR BROWSER](assets/notext/11.webp)


## Jak korzystać z przeglądarki Tor?


Przeglądarka Tor Browser jest używana jak standardowa przeglądarka.

![TOR BROWSER](assets/notext/12.webp)

Przy pierwszym uruchomieniu przeglądarka wyświetla stronę z zaproszeniem do połączenia się z siecią Tor. Wystarczy kliknąć przycisk "*Połącz*", aby nawiązać połączenie.

![TOR BROWSER](assets/notext/13.webp)

Jeśli chcesz, aby oprogramowanie automatycznie łączyło się z siecią Tor podczas przyszłych zastosowań, zaznacz opcję "*Zawsze łącz się automatycznie*".

![TOR BROWSER](assets/notext/14.webp)

Po połączeniu się z siecią Tor przejdziesz do strony głównej.

![TOR BROWSER](assets/notext/15.webp)

Aby przeprowadzić wyszukiwanie w Internecie, wystarczy wpisać zapytanie w pasku wyszukiwania i nacisnąć klawisz "*enter*".

![TOR BROWSER](assets/notext/16.webp)

Następnie wyniki z wyszukiwarki będą wyświetlane w taki sam sposób, jak w innych przeglądarkach.

![TOR BROWSER](assets/notext/17.webp)

Opcja "*Onionize*" w DuckDuckGo umożliwia korzystanie z wyszukiwarki za pośrednictwem ukrytej usługi w sieci Tor, uzyskując dostęp do Address `.onion`.

![TOR BROWSER](assets/notext/18.webp)


## Jak skonfigurować przeglądarkę Tor?


W górnej części ekranu przeglądarki znajduje się opcja importowania ulubionych. Pozwala to na automatyczną integrację zakładek ze starej przeglądarki z Tor Browser.

![TOR BROWSER](assets/notext/19.webp)

Istnieje również opcja dodawania nowych zakładek poprzez kliknięcie ikony gwiazdki znajdującej się w prawym górnym rogu odwiedzanej strony internetowej.

![TOR BROWSER](assets/notext/20.webp)

W menu po prawej stronie dostępne są różne opcje.

![TOR BROWSER](assets/notext/21.webp)The "*New identity*" button allows you to change your Tor identity. Specifically, this enables you to start a new user session on Tor, meaning changing your IP address and resetting cookies and open sessions.

![TOR BROWSER](assets/notext/22.webp)

Menu "*Zakładki*" umożliwia zarządzanie zakładkami.

![TOR BROWSER](assets/notext/23.webp)

"*Historia*" daje dostęp do historii przeglądania, jeśli została ona włączona w ustawieniach.

![TOR BROWSER](assets/notext/24.webp)

Menu "*Add-ons and themes*" pozwala dostosować wygląd przeglądarki lub dodać rozszerzenia. Ponieważ przeglądarka Tor Browser jest oparta na przeglądarce Mozilla Firefox, można korzystać z motywów i rozszerzeń dostępnych dla przeglądarki Firefox.

![TOR BROWSER](assets/notext/25.webp)

Wreszcie, przycisk "*Ustawienia*" zapewnia dostęp do ustawień przeglądarki.

![TOR BROWSER](assets/notext/26.webp)

W zakładce "*Ogólne*" ustawień znajdują się różne opcje, które pozwalają dostosować przeglądarkę Tor Browser użytkownika Interface.

![TOR BROWSER](assets/notext/27.webp)

W zakładce "*Home*" możesz zmienić domyślną stronę wyświetlaną podczas otwierania przeglądarki Tor Browser i otwierania nowych kart.

![TOR BROWSER](assets/notext/28.webp)

W zakładce "*Search*" można wybrać wyszukiwarkę. Tor Browser domyślnie wybiera DuckDuckGo, wyszukiwarkę skoncentrowaną na ochronie prywatności użytkowników, ale można też wybrać na przykład Google lub Startpage.

![TOR BROWSER](assets/notext/29.webp)

Można również ustawić skróty w wyszukiwarce.

![TOR BROWSER](assets/notext/30.webp)

Na przykład, możesz wpisać "*@wikipedia*", a następnie wyszukiwane hasło, takie jak "*Bitcoin*", w pasku wyszukiwania przeglądarki.

![TOR BROWSER](assets/notext/31.webp)

Funkcja ta przeprowadza następnie wyszukiwanie terminu bezpośrednio w witrynie Wikipedii.

![TOR BROWSER](assets/notext/32.webp)

W ten sposób można skonfigurować inne niestandardowe skróty dla różnych witryn.


Następnie w zakładce "*Prywatność i bezpieczeństwo*" znajdziesz wszystkie ustawienia związane z prywatnością i bezpieczeństwem.

![TOR BROWSER](assets/notext/33.webp)

Użytkownik ma możliwość zachowania lub usunięcia historii przeglądania.

![TOR BROWSER](assets/notext/34.webp)

Możesz także zarządzać uprawnieniami dostępu przyznawanymi różnym witrynom.

![TOR BROWSER](assets/notext/35.webp)

W celu zapewnienia ogólnego bezpieczeństwa przeglądarki, tryby "*Safer*" i "*Safest*" umożliwiają dostosowanie funkcji internetowych i skryptów wykonywanych przez odwiedzane witryny. Minimalizuje to ryzyko wykorzystania luk w zabezpieczeniach, ale w zamian wpływa na wyświetlanie i interaktywność witryn. ![TOR BROWSER](assets/notext/36.webp) Znajdziesz tu inne opcje bezpieczeństwa, w tym blokadę niebezpiecznych treści i tryb tylko HTTPS, który zapewnia, że połączenia z witrynami konsekwentnie przestrzegają tego protokołu. ![TOR BROWSER](assets/notext/37.webp) Wreszcie, w zakładce "*Połączenie*" znajdziesz wszystkie ustawienia związane z łączeniem się z siecią Tor. W tym miejscu można skonfigurować most, aby uzyskać dostęp do sieci Tor z regionów, w których dostęp do niej może być cenzurowany. ![TOR BROWSER](assets/notext/38.webp) I gotowe, jesteś teraz gotowy do poruszania się po Internecie w bezpieczniejszy i bardziej prywatny sposób! Jeśli prywatność online jest tematem, który Cię interesuje, polecam również odkrycie tego innego samouczka na temat Mullvad VPN:


https://planb.network/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8