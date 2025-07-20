---
name: IVPN
description: Konfiguracja sieci VPN opłacanej bitcoinami
---
![cover](assets/cover.webp)


VPN ("*Virtual Private Network*") to usługa, która ustanawia bezpieczne i szyfrowane połączenie między telefonem lub komputerem a zdalnym serwerem zarządzanym przez dostawcę VPN.


Technicznie rzecz biorąc, podczas łączenia się z VPN ruch internetowy jest przekierowywany przez zaszyfrowany tunel do serwera VPN. Proces ten utrudnia stronom trzecim, takim jak dostawcy usług internetowych (ISP) lub złośliwi aktorzy, przechwytywanie lub odczytywanie danych użytkownika. Serwer VPN działa następnie jako pośrednik, który łączy się z usługą, z której chcesz korzystać w swoim imieniu. Przypisuje nowy adres IP Address do połączenia, co pomaga ukryć prawdziwy adres IP Address przed odwiedzanymi witrynami. Jednak w przeciwieństwie do tego, co mogą sugerować niektóre reklamy online, korzystanie z VPN nie pozwala na anonimowe przeglądanie Internetu, ponieważ wymaga pewnej formy zaufania do dostawcy VPN, który może zobaczyć cały ruch użytkownika.

![IVPN](assets/fr/01.webp)

Korzyści z korzystania z VPN są liczne. Po pierwsze, chroni prywatność aktywności online przed dostawcami usług internetowych lub rządami, pod warunkiem, że dostawca VPN nie udostępnia informacji o użytkowniku. Po drugie, zabezpiecza dane użytkownika, zwłaszcza gdy jest on połączony z publicznymi sieciami Wi-Fi, które są podatne na ataki MITM (man-in-the-middle). Po trzecie, ukrywając swój adres IP Address, VPN pozwala ominąć ograniczenia geograficzne i cenzurę, aby uzyskać dostęp do treści, które w przeciwnym razie byłyby niedostępne lub zablokowane w danym regionie.


Jak widać, VPN przenosi ryzyko obserwacji ruchu na dostawcę VPN. Dlatego przy wyborze dostawcy VPN ważne jest, aby wziąć pod uwagę dane osobowe wymagane do rejestracji. Jeśli dostawca prosi o podanie takich informacji, jak numer telefonu, adres e-mail Address, dane karty bankowej lub, co gorsza, adres pocztowy Address, zwiększa się ryzyko powiązania tożsamości użytkownika z jego ruchem. W przypadku kompromitacji dostawcy lub zajęcia prawnego, łatwo byłoby powiązać ruch z danymi osobowymi. Dlatego zaleca się wybranie dostawcy, który nie wymaga żadnych danych osobowych i akceptuje anonimowe płatności, takie jak bitcoiny.


W tym samouczku przedstawiam proste, wydajne i niedrogie rozwiązanie VPN, które nie wymaga podawania danych osobowych.


## Wprowadzenie do IVPN


IVPN to usługa VPN zaprojektowana specjalnie dla użytkowników poszukujących formy prywatności. W przeciwieństwie do popularnych dostawców VPN często promowanych na YouTube, IVPN wyróżnia się przejrzystością, bezpieczeństwem i poszanowaniem prywatności.

Polityka prywatności IVPN jest surowa: podczas rejestracji nie są wymagane żadne dane osobowe. Konto można otworzyć bez podawania adresu e-mail Address, imienia i nazwiska lub numeru telefonu. W przypadku płatności nie jest konieczne podawanie danych karty kredytowej, ponieważ IVPN akceptuje płatności w bitcoinach (onchain i Lightning). Co więcej, IVPN twierdzi, że nie prowadzi żadnych dzienników aktywności, co oznacza, że teoretycznie ruch internetowy użytkownika nie jest rejestrowany przez firmę.

IVPN jest również [całkowicie open-source] (https://github.com/ivpn), jeśli chodzi o oprogramowanie, aplikacje, a nawet stronę internetową, umożliwiając każdemu weryfikację i przegląd kodu. Co roku przechodzą również niezależne audyty bezpieczeństwa, których wyniki są publikowane na ich stronie internetowej.


IVPN korzysta wyłącznie z własnych serwerów, eliminując w ten sposób ryzyko związane z korzystaniem z usług chmurowych innych firm, takich jak AWS, Google Cloud lub Microsoft Azure.


Usługa oferuje wiele zaawansowanych funkcji, takich jak multi-hop, który kieruje ruch przez wiele serwerów zlokalizowanych w różnych jurysdykcjach w celu zwiększenia anonimowości. IVPN integruje również funkcję śledzenia i blokowania reklam oraz oferuje opcję wyboru spośród różnych protokołów VPN.


Oczywiście taka jakość usług wiąże się z kosztami, ale odpowiednia cena jest często wskaźnikiem jakości i uczciwości. Może to sygnalizować, że firma ma model biznesowy bez konieczności sprzedaży danych osobowych. IVPN oferuje 2 rodzaje planów: plan Standard, który umożliwia podłączenie do 2 urządzeń, oraz plan Pro, który umożliwia do 7 połączeń i zawiera protokół "*Multi-hop*", który kieruje ruch przez wiele serwerów.


W przeciwieństwie do głównych dostawców VPN, IVPN działa w oparciu o model zakupu czasu dostępu do usługi, a nie w oparciu o cykliczną subskrypcję. Użytkownik płaci bitcoinami jednorazowo za wybrany okres. Na przykład, jeśli kupisz roczny dostęp, możesz korzystać z usługi przez ten okres, po czym będziesz musiał wrócić na stronę IVPN, aby kupić więcej czasu dostępu.


Stawki [IVPN](https://www.ivpn.net/en/pricing/) są progresywne w zależności od wykupionego okresu dostępu. Oto ceny dla planu Standard:


- 1 tydzień: $2
- 1 miesiąc: $6
- 1 rok: 60 USD
- 2 lata: 100 USD
- 3 lata: 140 USD


I dla planu Pro:


- 1 tydzień: $4
- 1 miesiąc: $10
- 1 rok: 100 USD
- 2 lata: 160 USD
- 3 lata: 220 USD


## Jak zainstalować IVPN na komputerze?

Pobierz [najnowszą wersję oprogramowania](https://www.ivpn.net/en/apps-windows/) dla swojego systemu operacyjnego, a następnie kontynuuj instalację, postępując zgodnie z instrukcjami kreatora instalacji. ![IVPN](assets/notext/02.webp)

Użytkownicy systemu Linux powinni zapoznać się z instrukcjami dotyczącymi danej dystrybucji dostępnymi na stronie [this page](https://www.ivpn.net/en/apps-linux/).

![IVPN](assets/notext/03.webp)

Po zakończeniu instalacji należy wprowadzić identyfikator konta. Zobaczymy, jak go uzyskać w kolejnych sekcjach tego samouczka.

![IVPN](assets/notext/04.webp)

## Jak zainstalować IVPN na smartfonie?


Pobierz IVPN ze swojego sklepu z aplikacjami, niezależnie od tego, czy jest to [AppStore](https://apps.apple.com/us/app/ivpn-secure-vpn-for-privacy/id1193122683) dla użytkowników iOS, [Google Play Store](https://play.google.com/store/apps/details?id=net.ivpn.client) dla Androida, czy [F-Droid](https://f-droid.org/en/packages/net.ivpn.client). Jeśli korzystasz z systemu Android, masz również możliwość pobrania pliku `.apk` bezpośrednio z [witryny IVPN](https://www.ivpn.net/en/apps-android/).

![IVPN](assets/notext/05.webp)

Przy pierwszym użyciu aplikacji użytkownik zostanie wylogowany. Aby aktywować usługę, należy wprowadzić identyfikator konta.

![IVPN](assets/notext/06.webp)

Przejdźmy teraz do aktywacji IVPN na swoich urządzeniach.


## Jak opłacić i aktywować IVPN?


Przejdź do oficjalnej strony IVPN [na stronie płatności] (https://www.ivpn.net/en/pricing/).

![IVPN](assets/notext/07.webp)

Wybierz plan, który najlepiej odpowiada Twoim potrzebom. W tym samouczku zdecydujemy się na plan Standard, który pozwala nam na przykład aktywować VPN na naszym komputerze i smartfonie.

![IVPN](assets/notext/08.webp)

Następnie IVPN utworzy konto użytkownika. Nie musisz podawać żadnych danych osobowych. Tylko identyfikator konta umożliwia zalogowanie się. Działa on trochę jak klucz dostępu. Zapisz go w bezpiecznym miejscu, na przykład w menedżerze haseł. Możesz również wykonać kopię papierową.

![IVPN](assets/notext/09.webp)

Na tej samej stronie należy wybrać czas trwania subskrypcji usługi.

![IVPN](assets/notext/10.webp)

Następnie wybierz metodę płatności. Ze swojej strony dokonam płatności za pośrednictwem Lightning Network, więc klikam przycisk "*Bitcoin*".

![IVPN](assets/notext/11.webp)

Sprawdź, czy wszystko się zgadza, a następnie kliknij przycisk "*Pay with Lightning*".

![IVPN](assets/notext/12.webp)

Na serwerze BTCPay zostanie wyświetlony kod Lightning Invoice. Zeskanuj kod QR za pomocą Lightning Wallet i kontynuuj płatność.

![IVPN](assets/notext/13.webp) Once the invoice is paid, click on the "*Return to IVPN*" button.

![IVPN](assets/notext/14.webp)

Twoje konto jest teraz wyświetlane jako "*Active*" i możesz zobaczyć datę, do której Twój dostęp do VPN jest ważny. Po tym terminie konieczne będzie odnowienie płatności.

![IVPN](assets/notext/15.webp)

Aby aktywować połączenie przez IVPN na komputerze, wystarczy skopiować identyfikator konta.

![IVPN](assets/notext/16.webp)

I wklej go do wcześniej pobranego oprogramowania.

![IVPN](assets/notext/17.webp)

Następnie kliknij przycisk "*Login*".

![IVPN](assets/notext/18.webp)

Kliknij znacznik wyboru, aby aktywować połączenie VPN i gotowe, ruch internetowy Twojego komputera jest teraz szyfrowany i kierowany przez serwer IVPN.

![IVPN](assets/notext/19.webp)

W przypadku smartfona procedura jest identyczna. Wklej identyfikator konta lub zeskanuj kod QR powiązany z kontem IVPN dostępnym na stronie internetowej. Następnie kliknij znacznik wyboru, aby nawiązać połączenie.

![IVPN](assets/notext/20.webp)

## Jak używać i konfigurować IVPN?


Pod względem użytkowania i ustawień jest to dość proste. Z głównego Interface można aktywować lub dezaktywować połączenie za pomocą znacznika wyboru.

![IVPN](assets/notext/21.webp)

Istnieje również opcja wstrzymania VPN na określony czas.

![IVPN](assets/notext/22.webp)

Klikając bieżący serwer, można wybrać inny serwer spośród dostępnych.

![IVPN](assets/notext/23.webp)

Możliwe jest również aktywowanie lub dezaktywowanie zintegrowanej zapory sieciowej, a także funkcji anty-śledzenia.

![IVPN](assets/notext/24.webp)

Aby uzyskać dostęp do dodatkowych ustawień, kliknij ikonę ustawień.

![IVPN](assets/notext/25.webp)

W zakładce "*Account*" znajdziesz ustawienia związane z Twoim kontem.

![IVPN](assets/notext/26.webp)

W zakładce "*Ogólne*" znajduje się kilka ustawień klienta. Zalecam zaznaczenie opcji "*Uruchom przy logowaniu*" i "*Przy uruchomieniu*" w sekcji "*Autoconnect*", aby automatycznie nawiązać połączenie z VPN po uruchomieniu komputera.

![IVPN](assets/notext/27.webp)

W zakładce "*Połączenie*" znajdują się różne opcje związane z połączeniem. Tutaj można zmienić używany protokół VPN.

![IVPN](assets/notext/28.webp)

Zakładka "*IVPN Firewall*" umożliwia systematyczną aktywację zapory sieciowej podczas uruchamiania komputera, zapewniając, że żadne połączenie nie zostanie nawiązane poza siecią VPN.

![IVPN](assets/notext/29.webp)

Zakładka "*Split Tunnel*" oferuje możliwość wykluczenia określonego oprogramowania z połączenia VPN. Aplikacje dodane w tym miejscu będą nadal działać z normalnym połączeniem internetowym, nawet gdy VPN jest włączony.

![IVPN](assets/notext/30.webp)

W zakładce "*WiFi control*" użytkownik ma możliwość skonfigurowania określonych działań w zależności od sieci, z którymi jest połączony. Na przykład, możesz oznaczyć swoją sieć domową jako "*Zaufaną*" i skonfigurować VPN tak, aby nie aktywował się w tej sieci, ale automatycznie aktywował się w każdej innej sieci Wi-Fi.

![IVPN](assets/notext/31.webp)

W menu "*AntiTracker*" wybierz profil blokowania dla swojego anty-trackera. Jest on przeznaczony do blokowania reklam, złośliwego oprogramowania i programów śledzących dane poprzez blokowanie żądań do usług śledzenia podczas przeglądania Internetu. Zwiększa to prywatność użytkownika, uniemożliwiając firmom gromadzenie i sprzedawanie danych przeglądania. Dostępny jest również "*Hardcore Mode*", który całkowicie blokuje wszystkie domeny należące do Google i Meta, a także wszystkie zależne usługi.

![IVPN](assets/notext/32.webp)

I gotowe, teraz możesz w pełni cieszyć się IVPN. Jeśli chcesz również zwiększyć bezpieczeństwo swoich kont internetowych za pomocą lokalnego menedżera haseł, zapraszam do zapoznania się z naszym samouczkiem na temat KeePass, darmowego rozwiązania typu open source:


https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Jeśli jesteś zainteresowany odkryciem innego dostawcy VPN podobnego do IVPN, zarówno pod względem funkcji, jak i cen, polecam również zapoznanie się z naszym samouczkiem na temat Mullvad:


https://planb.network/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8