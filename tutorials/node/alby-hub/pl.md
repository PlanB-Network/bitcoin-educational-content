---
name: Alby Hub
description: Jak łatwo uruchomić własny węzeł Lightning?
---
![cover](assets/cover.webp)


Alby Hub to najnowsze oprogramowanie open-source od Alby, firmy stojącej za popularnym rozszerzeniem internetowym Lightning. Alby Hub to samowystarczalny Wallet z najłatwiejszym w użyciu węzłem Lightning, dostępnym z dowolnego miejsca w celu integracji z dziesiątkami aplikacji. Alby Hub to łatwy w użyciu Interface do zarządzania węzłami Lightning.


W tym samouczku przyjrzymy się różnym sposobom korzystania z Alby Hub, jak połączyć go z Alby Go, aplikacją mobilną Alby lub rozszerzeniem przeglądarki Alby. Umożliwi to korzystanie z Sats w podróży przy zachowaniu autonomii w zarządzaniu węzłem.


![ALBY HUB](assets/fr/01.webp)


## Czym jest Alby Hub?


Alby Hub ma być nowym flagowym narzędziem w ekosystemie Alby. Oprogramowanie to umożliwia użytkownikom łatwe zarządzanie własnym Wallet ze zintegrowanym węzłem Lightning, przy jednoczesnym zachowaniu Ownership swoich kluczy (self-custody).


Alby Hub to wysoce elastyczne narzędzie. Może zaspokoić potrzeby zarówno początkujących, jak i zaawansowanych użytkowników. Nowicjusze będą go używać do łatwej samodzielnej obsługi prawdziwego węzła Lightning, bez konieczności radzenia sobie z podstawową złożonością. Dla bardziej doświadczonych użytkowników Alby Hub może być używany jako kompletny Interface do zaawansowanego zarządzania istniejącym węzłem Lightning.


W zależności od potrzeb, Alby Hub jest dostępny w 4 konfiguracjach:




- Alby Hub Cloud :**


Pierwsza opcja, idealna dla nowicjuszy, to opcja chmury Alby. Pozwala ona wdrożyć Hub bezpośrednio na serwerze zarządzanym przez Alby, dostępnym za pośrednictwem Alby Hub Interface. Chociaż Alby zarządza serwerem, użytkownik zachowuje suwerenność nad swoimi środkami, ponieważ klucze są szyfrowane przy użyciu hasła znanego tylko użytkownikowi. Jednak klucze muszą pozostać odszyfrowane w pamięci RAM, aby węzeł mógł działać, co teoretycznie naraża je na ryzyko, jeśli ktoś fizycznie uzyska dostęp do serwera. Jest to interesujący kompromis dla początkujących, ale ważne jest, aby być świadomym ryzyka.


Główną zaletą tej opcji jest to, że węzeł Lightning działa 24 godziny na dobę, 7 dni w tygodniu, bez konieczności samodzielnego zarządzania hostingiem. Co więcej, tworzenie kopii zapasowych węzła Lightning jest uproszczone i zautomatyzowane, w porównaniu z opcjami hostowanymi samodzielnie, w których musisz samodzielnie zarządzać kopiami zapasowymi kanałów.


Alby Cloud jest usługą płatną [sprawdź cennik] (https://albyhub.com/#pricing), aby uzyskać więcej informacji. Opłata jest automatycznie potrącana z twojego Wallet za pośrednictwem Lightning Invoice wydanego przez Alby. Odbywa się to za pośrednictwem połączenia NWC, które konfiguruje węzeł do automatycznego opłacania faktur Alby związanych z subskrypcją.





- Alby Hub z istniejącym węzłem :**


Jeśli masz już węzeł hostowany, na przykład na Umbrel lub Start9, Alby Hub może być używany jako zaawansowane zarządzanie Interface, w taki sam sposób jak ThunderHub lub RTL.




- Lokalny Alby Hub :**


Możliwe jest również zainstalowanie Alby Hub bezpośrednio na komputerze, chociaż ta opcja jest mniej praktyczna, ponieważ komputer musi pozostać aktywny przez cały czas, aby uzyskać zdalny dostęp do węzła Lightning. Ta alternatywa może być jednak odpowiednia dla konkretnych potrzeb.




- Alby Hub na osobistym serwerze :**


Zaawansowani użytkownicy mogą wdrożyć Alby Hub na osobistym serwerze za pomocą prostego polecenia. Ta opcja nie została omówiona w tym samouczku, ale można znaleźć dedykowane instrukcje [na GitHub Alby](https://github.com/getAlby/hub?tab=readme-ov-file#docker).


Ten samouczek koncentruje się głównie na Interface, który będzie taki sam niezależnie od wybranej opcji. Przyjrzymy się również, jak wdrożyć Alby Hub z płatną opcją chmury, a następnie z opcją node-in-box (Umbrel lub Start9).


![ALBY HUB](assets/fr/02.webp)


W przypadku instalacji lokalnej na komputerze PC, [pobierz i zainstaluj oprogramowanie zgodnie z systemem operacyjnym](https://github.com/getAlby/hub/releases), a następnie postępuj zgodnie z tymi samymi instrukcjami na Interface.


![ALBY HUB](assets/fr/03.webp)


## Utwórz konto Alby


Pierwszym krokiem jest utworzenie konta Alby. Chociaż nie jest to niezbędne do korzystania z Alby Hub, pozwala w pełni wykorzystać dostępne opcje, w tym możliwość uzyskania Lightning Address.


Wejdź na [oficjalną stronę Alby] (https://getalby.com/) i kliknij przycisk "*Create Account*".


![ALBY HUB](assets/fr/04.webp)


Wprowadź pseudonim i adres e-mail Address, a następnie kliknij "*Zarejestruj się*". Ten adres e-mail Address będzie później używany do logowania się na konto.


![ALBY HUB](assets/fr/05.webp)


Wprowadź kod weryfikacyjny otrzymany w wiadomości e-mail.


![ALBY HUB](assets/fr/06.webp)


Po zalogowaniu się na swoje konto online kliknij przycisk "*Kontynuuj*".


![ALBY HUB](assets/fr/07.webp)


Kliknij ponownie "*Kontynuuj*".


![ALBY HUB](assets/fr/08.webp)


## Opcja hostingu w chmurze


Następnie będziesz musiał wybrać między opcją samodzielnego hostingu, w której instalujesz Alby Hub na własnym urządzeniu, a opcjami premium. Zacznę od wyjaśnienia, jak postępować z opcją Pro Cloud (pamiętaj, że jest to opcja płatna, zobacz szczegóły w poprzedniej sekcji).


Kliknij na "*Upgrade*".


![ALBY HUB](assets/fr/09.webp)


Potwierdź klikając "*Subskrybuj teraz*".


![ALBY HUB](assets/fr/10.webp)


Kliknij "*Uruchom Alby Hub*".


![ALBY HUB](assets/fr/11.webp)


Poczekaj kilka chwil, aż węzeł zostanie utworzony.


![ALBY HUB](assets/fr/12.webp)


I to wszystko, Alby Hub jest teraz skonfigurowany. W następnej sekcji pokażę, jak zainstalować Alby Hub na istniejącym węźle. Jeśli nie masz jeszcze węzła Lightning, możesz przejść do następnej sekcji, aby skonfigurować Alby Hub w Alby Cloud.


![ALBY HUB](assets/fr/13.webp)


## Opcja samodzielnego hostingu


Jeśli wolisz używać Alby Hub jako Interface dla istniejącego węzła Lightning, masz kilka opcji: zainstaluj go na serwerze, lokalnie na komputerze lub za pośrednictwem węzła w pudełku (Umbrel lub Start9). Korzystanie z Alby Hub w tych konfiguracjach jest bezpłatne. Skoncentrujemy się na opcji node-in-box, ponieważ uważam, że opcja serwera, bez fizycznego dostępu, wiąże się z podobnym ryzykiem jak wersja w chmurze, a lokalna instalacja na komputerze jest często nieodpowiednia.


Aby skonfigurować to na Umbrel (kroki dla Start9 są identyczne), musisz najpierw mieć już skonfigurowany węzeł LND.


Zaloguj się do Umbrel Interface i przejdź do sklepu z aplikacjami.


![ALBY HUB](assets/fr/14.webp)


Poszukaj aplikacji "*Alby Hub*".


![ALBY HUB](assets/fr/15.webp)


Zainstaluj go na swoim węźle.


![ALBY HUB](assets/fr/16.webp)


Twój Alby Hub Interface jest teraz gotowy. Możesz postępować zgodnie z resztą samouczka, tak jakbyś korzystał z Interface w chmurze, ale bez opcji płatnej wersji. Co więcej, w przeciwieństwie do wersji w chmurze, klucze są przechowywane lokalnie na węźle, a nie na serwerach Alby.


![ALBY HUB](assets/fr/17.webp)


## Uruchomienie Alby Hub


Kliknij przycisk "*Get Started*".


![ALBY HUB](assets/fr/18.webp)


Następnie Alby Hub wyświetli monit o wybranie hasła. To hasło jest bardzo ważne, ponieważ będzie używane do szyfrowania Wallet. W płatnej wersji chmurowej klucze są przechowywane na serwerze Alby, szyfrowane hasłem, które znasz tylko Ty, a następnie odszyfrowywane i przechowywane tylko w pamięci RAM w celu podpisywania transakcji w razie potrzeby.


Dlatego ważne jest, aby wybrać silne hasło. Każdy, kto zna to hasło, może potencjalnie uzyskać dostęp do węzła. Upewnij się również, że wykonałeś jedną lub więcej fizycznych kopii zapasowych tego hasła na kartce papieru lub, jeszcze lepiej, na kawałku metalu dla dodatkowego bezpieczeństwa.


Po starannym wybraniu i zapisaniu hasła kliknij "*Create Password*".


![ALBY HUB](assets/fr/19.webp)


Masz teraz dostęp do węzła Lightning.


![ALBY HUB](assets/fr/20.webp)


Pierwszą czynnością, którą należy wykonać, jest zapisanie frazy odzyskiwania, z której pochodzą klucze. Aby to zrobić, kliknij "Ustawienia". Ta fraza umożliwia odzyskanie dostępu do Wallet, jeśli włączono automatyczne tworzenie kopii zapasowych.


![ALBY HUB](assets/fr/21.webp)


Następnie przejdź do zakładki "*Backup*". Wprowadź hasło, aby uzyskać do niej dostęp.


![ALBY HUB](assets/fr/22.webp)


Uzyskasz wtedy dostęp do swojej 12-wyrazowej frazy odzyskiwania. Wykonaj jedną lub więcej fizycznych kopii zapasowych tej frazy na papierze lub metalu i przechowuj je w bezpiecznym miejscu.


![ALBY HUB](assets/fr/23.webp)


Po zapisaniu frazy zaznacz pole, aby potwierdzić jej zapisanie i kliknij "*Kontynuuj*".


![ALBY HUB](assets/fr/24.webp)


## Jak mogę odzyskać dostęp do moich bitcoinów?


Przed wysłaniem środków do Alby Hub ważne jest, aby zrozumieć, jak je odzyskać w przypadku problemu, a także jakie informacje są wymagane do tego odzyskania. Proces ten różni się w zależności od charakteru środków do odzyskania i trybu hostingu węzła.


W przypadku płatnych użytkowników chmury pełne odzyskanie bitcoinów wymaga trzech podstawowych Elements:



- Twoja fraza odzyskiwania;
- Dostęp do konta Alby w celu pobrania automatycznych kopii zapasowych.


Brak którejkolwiek z tych dwóch informacji uniemożliwiłby odzyskanie bitcoinów w całości.


Dla tych, którzy korzystają z Alby Hub na własnym urządzeniu, proces odzyskiwania jest udokumentowany [tutaj] (https://guides.getalby.com/user-guide/alby-account-and-browser-extension/alby-hub/backups-and-recover#alby-hub-self-hosted-with-an-alby-account).


Jeśli zainstalowałeś Alby Hub na istniejącym węźle, musisz postępować zgodnie z procesem odzyskiwania określonego systemu operacyjnego węzła. Na przykład: Umbrel oferuje [opcję](https://github.com/getumbrel/umbrel/blob/2b266036f62a1594aa60a8a3be30cfb8656e755f/scripts/backup/README.md) do szyfrowania najnowszego stanu kanałów Lightning i zapisywania go dynamicznie i anonimowo przez Tor. Należy pamiętać, że tylko automatyczne kopie zapasowe z Alby pozwalają całkowicie odzyskać Hub bez zamykania kanałów.


## Kup swój pierwszy kanał Lightning


Możesz teraz postępować zgodnie z instrukcjami dostarczonymi przez Alby Hub. Kliknij przycisk, aby otworzyć pierwszy kanał dla przychodzącej gotówki.


![ALBY HUB](assets/fr/25.webp)


Wybierz opcję "*Otwórz kanał*". Jeśli nie zamierzasz zostać węzłem routingu i nie potrzebujesz go specjalnie, zalecam wybranie kanałów prywatnych.


![ALBY HUB](assets/fr/26.webp)


Alby Hub wyświetli generate i Invoice do zapłaty. Ta płatność pokrywa opłaty transakcyjne potrzebne do otwarcia kanału, a także opłaty za usługi LSP (*Lightning Service Provider*), który otworzy kanał do węzła, umożliwiając natychmiastowe otrzymywanie płatności.


![ALBY HUB](assets/fr/27.webp)


Po opłaceniu Invoice i potwierdzeniu transakcji zostanie utworzony pierwszy kanał Lightning.


![ALBY HUB](assets/fr/28.webp)


W zakładce "*Node*" możesz zobaczyć, że masz teraz przychodzącą gotówkę, umożliwiającą otrzymywanie płatności za pośrednictwem Lightning.


![ALBY HUB](assets/fr/29.webp)


Aby otrzymać płatność, kliknij zakładkę "*Wallet*", a następnie "*Receive*".


![ALBY HUB](assets/fr/30.webp)


Wprowadź kwotę i w razie potrzeby dodaj opis, a następnie kliknij "*Utwórz Invoice*".


![ALBY HUB](assets/fr/31.webp)


Otrzymałem pierwszą płatność w wysokości 120 000 Sats.


![ALBY HUB](assets/fr/32.webp)


Wracając do zakładki "*Wallet*", można sprawdzić saldo Wallet. Należy pamiętać, że Alby Hub automatycznie odkłada 354 Sats podczas dokonywania pierwszej płatności. Dla każdego otwartego kanału Lightning Alby Hub automatycznie odłoży rezerwę odpowiadającą 1% pojemności kanału. Rezerwa ta jest środkiem bezpieczeństwa, który umożliwia węzłowi odzyskanie środków kanału w przypadku próby oszustwa ze strony użytkownika. To dlatego, mimo że wysłałem 120 000 Sats, na moim saldzie widnieje tylko 119 646 Sats.


![ALBY HUB](assets/fr/33.webp)


## Deponowanie bitcoinów w łańcuchu


Jeśli chcesz mieć wychodzącą gotówkę do dokonywania płatności, możesz również samodzielnie otworzyć kanał. Aby to zrobić, będziesz potrzebować bitcoinów onchain w swoim Wallet.


W zakładce "*Node*" kliknij na "*Deposit*".


![ALBY HUB](assets/fr/34.webp)


Wyślij bitcoiny do wyświetlonego Address. Ten Address pochodzi z wcześniej zapisanej frazy odzyskiwania.


![ALBY HUB](assets/fr/35.webp)


Wysłałem 72 000 Sats. Są one teraz widoczne w "*Savings Balance*", które obejmuje wszystkie środki, które posiadam w łańcuchu, a nie na Lightning.


![ALBY HUB](assets/fr/36.webp)


## Otwórz kanał Lightning


Teraz, gdy masz już środki onchain, możesz otworzyć nowy kanał Lightning. Zaleca się otwarcie kilku kanałów z wystarczającymi kwotami, aby zawsze móc dokonywać płatności bez ograniczeń. Większość dostawców usług LSP (*Lightning Service Providers*) wymaga co najmniej 150 000 Sats, aby otworzyć z tobą kanał.


W zakładce "*Node*" kliknij na "*Open Channel*".


![ALBY HUB](assets/fr/37.webp)


Wybierz rozmiar swojego kanału. Zalecam, aby nie otwierać kanałów, które są zbyt małe, pamiętając, że jest to węzeł Lightning, a maszyna hostująca klucze nie oferuje takiego samego poziomu bezpieczeństwa jak Hardware Wallet. Bądź więc ostrożny z kwotami, które zdecydujesz się zablokować.


![ALBY HUB](assets/fr/38.webp)


W menu "*Advanced Options*" (Opcje zaawansowane) można wybrać LSP do otwarcia kanału lub ręcznie wprowadzić inny węzeł Lightning.


![ALBY HUB](assets/fr/39.webp)


Następnie kliknij "*Otwórz kanał*".


![ALBY HUB](assets/fr/40.webp)


Poczekaj, aż Twój kanał zostanie potwierdzony w łańcuchu.


![ALBY HUB](assets/fr/41.webp)


Nowy kanał pojawi się teraz w zakładce "*Node*".


![ALBY HUB](assets/fr/42.webp)


## Zarządzanie węzłami


Zarządzanie kanałami Lightning jest łatwiejsze niż myślisz. Alby Hub umożliwia przenoszenie Sats między saldem wydatków a saldem On-Chain. W ten sposób można zwiększyć wydatki lub pojemność odbiorczą.


![ALBY HUB](assets/fr/66.webp)


## Podłącz aplikację do wydatków


Teraz, gdy masz już działający węzeł Lightning, możesz go używać do codziennego odbierania i wydawania Sats. Chociaż Interface Alby Hub jest przydatny do zarządzania węzłem, nie jest idealny do dokonywania szybkich transakcji w ruchu. W tym celu użyjemy aplikacji Lightning Wallet zainstalowanej na naszym smartfonie.


W tym samouczku zalecam wybranie Alby Go, która jest bardzo łatwa w użyciu, ale możesz także użyć innych kompatybilnych aplikacji, takich jak Zeus.


![ALBY HUB](assets/fr/43.webp)


Aby zainstalować Alby Go, przejdź do sklepu z aplikacjami na swoim urządzeniu:




- [Dla systemu Android](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Dla Apple](https://apps.apple.com/us/app/alby-go/id6471335774).


![ALBY HUB](assets/fr/44.webp)


Użytkownicy Androida mogą również zainstalować aplikację za pomocą pliku `.apk` [dostępnego na GitHubie Alby'ego] (https://github.com/getAlby/go/releases).


![ALBY HUB](assets/fr/45.webp)


Po uruchomieniu aplikacji kliknij "*Connect Wallet*".


![ALBY HUB](assets/fr/46.webp)


W Alby Hub, w App Store, znajdź "Alby Go" i kliknij "Połącz"

![ALBY HUB](assets/fr/47.webp)

Kliknij "Połącz za pomocą One-Tab Connections". Umożliwi to połączenie Alby Hub jednym kliknięciem z innymi aplikacjami za pomocą Alby Go.


![ALBY HUB](assets/fr/48.webp)


Alby Hub następnie generate tajne, aby ustanowić połączenie z Alby Go.


![ALBY HUB](assets/fr/49.webp)


Wróć do aplikacji Alby Go, zeskanuj kod QR lub wklej sekret.


![ALBY HUB](assets/fr/50.webp)


Kliknij przycisk "Zakończ*".


![ALBY HUB](assets/fr/51.webp)


Masz teraz zdalny dostęp do swojego Alby Hub zasilanego przez węzeł Lightning ze swojego smartfona, co ułatwia wydawanie i odbieranie Sats w podróży każdego dnia.


![ALBY HUB](assets/fr/52.webp)


W razie potrzeby można zarządzać uprawnieniami dla tego połączenia bezpośrednio w Alby Hub, klikając je.


![ALBY HUB](assets/fr/53.webp)


Aby otrzymać Sats, wystarczy kliknąć "*Odbierz*".


![ALBY HUB](assets/fr/54.webp)


Zmodyfikuj kwotę i opis Invoice, klikając "*Invoice*".


![ALBY HUB](assets/fr/55.webp)


Naładuj Invoice, aby otrzymać Sats.


![ALBY HUB](assets/fr/56.webp)


Aby wysłać Sats, kliknij na "*Wyślij*".


![ALBY HUB](assets/fr/57.webp)


Zeskanuj Invoice, którym chcesz zapłacić.


![ALBY HUB](assets/fr/58.webp)


Następnie kliknij "*Pay*".


![ALBY HUB](assets/fr/59.webp)


Transakcja została potwierdzona.


![ALBY HUB](assets/fr/60.webp)


Klikając małą strzałkę, można uzyskać dostęp do historii transakcji.


![ALBY HUB](assets/fr/61.webp)


Transakcje te są również widoczne w Alby Hub.


![ALBY HUB](assets/fr/62.webp)


## Dostosuj swój Lightning Address


Alby oferuje opcję błyskawicznego Address. Pozwala to na otrzymywanie płatności na węźle bez konieczności ręcznego generate i Invoice za każdym razem. Domyślnie Alby przypisuje użytkownikowi Lightning Address, ale można go dostosować. Zaloguj się do swojego konta online Alby, kliknij swoją nazwę w prawym górnym rogu, a następnie wybierz "*Ustawienia*".


![ALBY HUB](assets/fr/63.webp)


Przejdź do menu "*Lightning Address*".


![ALBY HUB](assets/fr/64.webp)


Zmodyfikuj swój Address, a następnie potwierdź, klikając "*Update your lightning Address*".


![ALBY HUB](assets/fr/65.webp)


Należy pamiętać, że po zmianie Address nie należy on już do użytkownika. Upewnij się więc, że nigdy więcej nie wyślesz na niego Sats.


I to wszystko, teraz wiesz, jak używać Lightning z własnym węzłem za pomocą narzędzia Alby Hub. Jeśli ten samouczek okazał się przydatny, będę bardzo wdzięczny, jeśli umieścisz poniżej kciuk Green. Zachęcam również do udostępnienia tego artykułu w sieciach społecznościowych. Dziękuję bardzo!


Aby szczegółowo zrozumieć wszystkie mechanizmy Lightning, którymi manipulowaliśmy w tym samouczku, zdecydowanie radzę zapoznać się z naszym bezpłatnym szkoleniem na ten temat:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb