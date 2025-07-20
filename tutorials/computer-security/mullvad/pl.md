---
name: Mullvad VPN
description: Konfiguracja sieci VPN opłacanej bitcoinami
---
![cover](assets/cover.webp)


VPN ("*Virtual Private Network*") to usługa, która ustanawia bezpieczne i szyfrowane połączenie między telefonem lub komputerem a zdalnym serwerem zarządzanym przez dostawcę VPN.


Technicznie rzecz biorąc, podczas łączenia się z VPN ruch internetowy jest przekierowywany przez zaszyfrowany tunel do serwera VPN. Proces ten utrudnia stronom trzecim, takim jak dostawcy usług internetowych (ISP) lub złośliwi aktorzy, przechwytywanie lub odczytywanie danych użytkownika. Serwer VPN działa następnie jako pośrednik, który łączy się z usługą, z której chcesz korzystać w swoim imieniu. Przypisuje nowy adres IP Address do połączenia, co pomaga ukryć prawdziwy adres IP Address przed odwiedzanymi witrynami. Jednak w przeciwieństwie do tego, co mogą sugerować niektóre reklamy online, korzystanie z VPN nie pozwala na anonimowe przeglądanie Internetu, ponieważ wymaga poziomu zaufania do dostawcy VPN, który może zobaczyć cały ruch użytkownika.

![MULLVAD VPN](assets/fr/01.webp)

Korzyści z korzystania z VPN są liczne. Po pierwsze, chroni prywatność aktywności online przed dostawcami usług internetowych lub rządami, pod warunkiem, że dostawca VPN nie udostępnia informacji o użytkowniku. Po drugie, zabezpiecza dane użytkownika, zwłaszcza gdy łączy się on z publicznymi sieciami Wi-Fi, które są podatne na ataki MITM ("**man-in-the-middle**"). Po trzecie, ukrywając swój adres IP Address, VPN pozwala ominąć ograniczenia geograficzne i cenzurę, aby uzyskać dostęp do treści, które w przeciwnym razie byłyby niedostępne lub zablokowane w danym regionie.


Jak widać, VPN przenosi ryzyko obserwacji ruchu na dostawcę VPN. Dlatego przy wyborze dostawcy VPN ważne jest, aby wziąć pod uwagę dane osobowe wymagane do rejestracji. Jeśli dostawca prosi o podanie takich informacji, jak numer telefonu, adres e-mail Address, dane karty bankowej lub, co gorsza, adres pocztowy Address, wzrasta ryzyko powiązania tożsamości użytkownika z jego ruchem. W przypadku kompromitacji dostawcy lub zajęcia prawnego, łatwo byłoby powiązać ruch użytkownika z jego danymi osobowymi. Dlatego zaleca się wybranie dostawcy, który nie wymaga żadnych danych osobowych i akceptuje anonimowe płatności, takie jak bitcoiny.


W tym samouczku przedstawię proste, wydajne i niedrogie rozwiązanie VPN, które nie wymaga podawania danych osobowych.


## Wprowadzenie do Mullvad VPN

Mullvad VPN to szwedzka usługa, która wyróżnia się swoim Commitment dla prywatności użytkowników. W przeciwieństwie do głównych dostawców VPN, Mullvad nie wymaga podawania żadnych danych osobowych podczas rejestracji. Nie ma potrzeby podawania adresu e-mail Address, numeru telefonu ani nazwiska; zamiast tego Mullvad przypisuje ci anonimowy numer konta używany do płatności i uzyskiwania dostępu do usługi. Ponadto Mullvad twierdzi, że nie przechowuje żadnych dzienników aktywności, które przechodzą przez ich serwery.

![MULLVAD VPN](assets/notext/02.webp)

W przypadku płatności niekoniecznie wymagane jest podanie danych karty kredytowej, ponieważ Mullvad akceptuje płatności Bitcoin (onchain tylko na ich oficjalnej stronie, ale istnieje nieoficjalna metoda płatności za pośrednictwem Lightning). Akceptują również płatności gotówkowe za pośrednictwem poczty.


Mullvad VPN wyróżnia się również przejrzystością i bezpieczeństwem. Ich oprogramowanie jest typu open-source i regularnie przechodzą niezależne audyty bezpieczeństwa w celu oceny swoich aplikacji i infrastruktury, których wyniki są [publikowane na ich stronie internetowej] (https://mullvad.net/fr/blog/tag/audits). Firma stojąca za Mullvad ma siedzibę w Szwecji, kraju znanym z surowych przepisów dotyczących prywatności. Korzysta wyłącznie z serwerów hostowanych samodzielnie, eliminując w ten sposób ryzyko związane z korzystaniem z usług chmurowych stron trzecich, takich jak hiperskalery AWS, Google Cloud lub Microsoft Azure.


Pod względem funkcji Mullvad oferuje wszystko, czego można oczekiwać od dobrego klienta VPN, w tym wyłącznik awaryjny, który chroni ruch w przypadku rozłączenia VPN, opcję wyłączenia VPN dla określonych aplikacji oraz możliwość kierowania ruchu przez wiele serwerów VPN.


Oczywiście taka jakość usług wiąże się z kosztami, ale uczciwa cena jest często wskaźnikiem jakości i uczciwości. Może to sygnalizować, że firma ma model biznesowy bez konieczności sprzedaży danych osobowych stronom trzecim. Mullvad VPN oferuje zryczałtowaną stawkę 5 euro miesięcznie, możliwą do wykorzystania na maksymalnie 5 różnych urządzeniach.

![MULLVAD VPN](assets/notext/03.webp)

W przeciwieństwie do głównych dostawców VPN, Mullvad ma model zakupu czasu dostępu do usługi, a nie cyklicznej, automatycznej subskrypcji. Użytkownik po prostu dokonuje jednorazowej płatności w bitcoinach za wybrany okres. Na przykład, jeśli kupisz roczny dostęp, możesz korzystać z usługi przez ten okres, po czym musisz wrócić na stronę Mullvad, aby odnowić swój czas dostępu.

W porównaniu do IVPN, innego wysokiej jakości dostawcy VPN, Mullvad jest nieco bardziej ekonomiczny. Na przykład, nawet przy wyborze trzyletniego zakupu z IVPN, miesięczny koszt wynosi około 5,40 €. IVPN oferuje jednak pewne dodatkowe usługi i ma również tańszy plan niż Mullvad (plan Standard), ale jest on ograniczony tylko do 2 urządzeń i nie obejmuje protokołu "multi-hop".

Przeprowadziłem również kilka nieformalnych testów prędkości, aby porównać IVPN i Mullvad. Chociaż IVPN wykazał niewielką przewagę pod względem wydajności, prędkości w Mullvad były nadal bardzo zadowalające. W porównaniu z głównymi dostawcami VPN, IVPN i Mullvad okazały się co najmniej tak samo wydajne, jeśli nie lepsze w niektórych przypadkach.


## Jak zainstalować Mullvad VPN na komputerze?


Odwiedź [oficjalną stronę Mullvad](https://mullvad.net/en/download/) i kliknij menu "*Downloads*".

![MULLVAD VPN](assets/notext/04.webp)

Użytkownicy systemów Windows lub macOS mogą pobrać oprogramowanie bezpośrednio ze strony i postępować zgodnie z instrukcjami kreatora instalacji, aby dokończyć instalację.

![MULLVAD VPN](assets/notext/05.webp)

Użytkownicy systemu Linux mogą znaleźć instrukcje specyficzne dla danej dystrybucji w sekcji ["*Linux*"](https://mullvad.net/en/download/vpn/linux).

![MULLVAD VPN](assets/notext/06.webp)

Po zakończeniu instalacji należy wprowadzić identyfikator konta. Zobaczymy, jak go uzyskać w kolejnych sekcjach tego samouczka.


## Jak zainstalować Mullvad VPN na smartfonie?


Pobierz Mullvad VPN ze swojego sklepu z aplikacjami, niezależnie od tego, czy jest to [AppStore](https://apps.apple.com/us/app/mullvad-vpn/id1488466513) dla użytkowników iOS, [Google Play Store](https://play.google.com/store/apps/details?id=net.mullvad.mullvadvpn) dla Androida, czy [F-Droid](https://f-droid.org/packages/net.mullvad.mullvadvpn/). Jeśli korzystasz z systemu Android, masz również możliwość pobrania pliku `.apk` bezpośrednio z [witryny Mullvad](https://mullvad.net/en/download/vpn/android).

![MULLVAD VPN](assets/notext/07.webp)

Przy pierwszym użyciu aplikacji użytkownik zostanie wylogowany. Aby aktywować usługę, należy wprowadzić identyfikator konta.

![MULLVAD VPN](assets/notext/08.webp)

Przejdźmy teraz do aktywacji Mullvad na urządzeniach.


## Jak zapłacić i aktywować Mullvad VPN?


Wejdź na [oficjalną stronę Mullvad] (https://mullvad.net/) i kliknij przycisk "*Get Started*".

![MULLVAD VPN](assets/notext/09.webp)

Kliknij przycisk "*Numer konta generate*".

![MULLVAD VPN](assets/notext/10.webp)Mullvad will then create your account. You do not need to provide any personal information. It is only your account number that will allow you to log in. It acts somewhat like an access key. Save it in a safe place like your password manager, for example. You can also make a paper copy.

![MULLVAD VPN](assets/notext/11.webp)

Następnie kliknij przycisk "*Dodaj czas do swojego konta*".

![MULLVAD VPN](assets/notext/12.webp)

Zostanie wyświetlona strona logowania do konta. Wprowadź numer konta, a następnie kliknij przycisk "*Zaloguj się*".

![MULLVAD VPN](assets/notext/13.webp)

Wybierz metodę płatności. Zalecam płatność w bitcoinach, ponieważ skorzystasz z 10% zniżki, co obniży koszt do 4,50 € miesięcznie. Jeśli wolisz płacić za pośrednictwem Lightning, w dalszej części przedstawię alternatywną metodę.

![MULLVAD VPN](assets/notext/14.webp)

Kliknij przycisk "*Utwórz płatność jednorazową Address*".

![MULLVAD VPN](assets/notext/15.webp)

Następnie zapłać swoim Bitcoin Wallet kwotę wskazaną na otrzymanym Address.

![MULLVAD VPN](assets/notext/16.webp)

Po potwierdzeniu transakcji może minąć kilka minut, zanim witryna wykryje płatność. Po wykryciu płatności przez Mullvad, czas trwania subskrypcji pojawi się w lewym górnym rogu strony, zamiast napisu "*Nie pozostało czasu*".

![MULLVAD VPN](assets/notext/17.webp)

Następnie można wprowadzić numer konta w oprogramowaniu, aby aktywować VPN.

![MULLVAD VPN](assets/notext/18.webp)

Aby aktywować VPN w aplikacji mobilnej, proces jest dokładnie taki sam. Wystarczy wprowadzić numer konta.

![MULLVAD VPN](assets/notext/19.webp)

## Jak zapłacić za Mullvad VPN za pomocą Lightning?


Jak zrozumiałeś, Mullvad nie akceptuje jeszcze płatności za pośrednictwem Lightning Network. Jednak dzięki rekomendacji od [Lounès](https://x.com/louneskmt) odkryłem nieformalną usługę, która pozwala ominąć to ograniczenie. Usługa ta, dostępna na [vpn.sovereign.engineering](https://vpn.sovereign.engineering/), akceptuje płatności na Lightning i zapewnia w zamian ważny plan dla Mullvad.

![MULLVAD VPN](assets/notext/20.webp)

Na stronie dostępne są dwie różne opcje: można zaufać menedżerowi strony i bezpośrednio wprowadzić numer konta, a następnie kliknąć przycisk "*Zaloguj się*", aby pakiet Mullvad został automatycznie zatwierdzony. Możesz też kliknąć przycisk "*Heck yeah!", aby kupić Voucher w Lightning, którego możesz następnie użyć na oficjalnej stronie Mullvad, aby otrzymać swój pakiet. ![MULLVAD VPN](assets/notext/21.webp) W obu przypadkach zostaniesz poproszony o wybranie czasu trwania pakietu. Do wyboru są okresy od 6 miesięcy do 1 roku. ![MULLVAD VPN](assets/notext/22.webp) Następnie kliknij przycisk "*Top-up with Lightning*". ![MULLVAD VPN](assets/notext/23.webp) Aby sfinalizować zakup, zapłać Invoice za pomocą Lightning Wallet. ![MULLVAD VPN](assets/notext/24.webp) Jeśli zdecydowałeś się na zakup Vouchera, na stronie Mullvad wybierz "*Voucher*" spośród metod płatności dostępnych na Twoim koncie. Następnie wprowadź numer Vouchera otrzymany ze strony vpn.sovereign.engineering w wyznaczonym polu. ![MULLVAD VPN](assets/notext/25.webp) ## Jak używać i konfigurować Mullvad VPN?


Teraz, gdy masz już aktywne konto i wprowadziłeś swój numer konta w oprogramowaniu lub aplikacji Mullvad, możesz w pełni cieszyć się usługami VPN. ![MULLVAD VPN](assets/notext/26.webp) Aby rozłączyć się z VPN, wystarczy kliknąć przycisk "*Disconnect*". ![MULLVAD VPN](assets/notext/27.webp) Mała czerwona strzałka obok przycisku "*Disconnect*" umożliwia zmianę serwera bez zmiany bieżącej lokalizacji. ![MULLVAD VPN](assets/notext/28.webp) Jeśli chcesz zmienić miasto dla swojego serwera VPN, kliknij "*Zmień lokalizację*", aby wybrać nową lokalizację. ![MULLVAD VPN](assets/notext/29.webp) W górnej części ekranu zobaczysz pseudonim swojego urządzenia, a także pozostały czas trwania pakietu. ![MULLVAD VPN](assets/notext/30.webp) Klikając ikonę małego ludzika, uzyskasz dostęp do szczegółowych informacji o swoim koncie. ![MULLVAD VPN](assets/notext/31.webp) Aby uzyskać dostęp do ustawień, kliknij koło zębate. ![MULLVAD VPN](assets/notext/32.webp) W menu "*Ustawienia Interface użytkownika*" można dostosować ustawienia oprogramowania, w tym język Interface i jego zachowanie w systemie. ![MULLVAD VPN](assets/notext/33.webp) W menu "*Ustawienia VPN*" znajdziesz opcje związane z Twoją siecią VPN. Zalecam włączenie opcji "*Launch app on start-up*" i "*Auto-connect*", aby połączenie VPN uruchamiało się automatycznie po uruchomieniu komputera.

![MULLVAD VPN](assets/notext/34.webp) In the "*DNS content blockers*" submenu, you have the option to filter and block DNS requests to malicious, advertising, or unwanted websites.

![MULLVAD VPN](assets/notext/35.webp)

Wreszcie, menu "*Split tunneling*" pozwala wybrać określone aplikacje na komputerze, dla których ruch internetowy nie będzie kierowany przez VPN.

![MULLVAD VPN](assets/notext/36.webp)

Aby uzyskać przegląd swojego konta Mullvad i zarządzać różnymi podłączonymi urządzeniami, możesz kliknąć menu "*Urządzenia*" na stronie internetowej.

![MULLVAD VPN](assets/notext/37.webp)

I to wszystko, jesteś teraz przygotowany, aby w pełni cieszyć się Mullvad VPN. Jeśli chcesz odkryć innego dostawcę VPN podobnego do Mullvad, zarówno pod względem funkcji, jak i cen, polecam również zapoznanie się z naszym samouczkiem na temat IVPN:


https://planb.network/tutorials/computer-security/communication/ivpn-5a0cd5df-29f1-4382-a817-975a96646e68