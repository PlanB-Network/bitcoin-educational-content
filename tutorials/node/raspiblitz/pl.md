---
name: RaspiBlitz
description: Przewodnik po konfiguracji RaspiBlitz
---

![image](assets/0.webp)


RaspiBlitz to węzeł Lightning Node (LND i/lub Core Lightning) działający razem z węzłem Bitcoin-Fullnode na RaspberryPi (1 TB SSD) i ładnym wyświetlaczem ułatwiającym konfigurację i monitorowanie.


RaspiBlitz jest przeznaczony głównie do nauki, jak uruchomić własny węzeł zdecentralizowany z domu - ponieważ: Nie Twój Węzeł, Nie Twoje Zasady. Odkryj i rozwijaj rosnący ekosystem Lightning Network, stając się jego pełnoprawną częścią. Zbuduj go w ramach warsztatów lub jako własny projekt weekendowy.


![video](https://youtu.be/DTHlSPMz3ns)

RASPIBLITZ - Jak uruchomić piorun i Bitcoin Full node przez sesję BTC


# Podręcznik konfiguracji Raspiblitz firmy Parman


Raspiblitz to doskonały system do uruchamiania węzła Bitcoin i powiązanych aplikacji. Polecam go wraz z węzłem MyNode większości użytkowników (najlepiej mieć dwa węzły dla redundancji). Jedną z głównych zalet jest to, że węzeł Raspiblitz jest „Free Open Source Software”, w przeciwieństwie do MyNode lub Umbrel. [Dlaczego to jest ważne? Wyjaśnia Vlad Costa.](https://bitcoin-takeover.com/why-bitcoin-free-open-source-software-matters/amp/?__twitter_impression=true) Możesz także uruchomić Raspiblitz z połączeniem WiFi zamiast ethernet – oto [dodatkowy przewodnik](https://armantheparman.com/headless-wifi/) do tego. (Nie znalazłem sposobu, aby zrobić to z MyNode).


Możesz kupić gotowy węzeł z dołączonym mini ekranem lub zbudować go samodzielnie (nie potrzebujesz ekranu).


[Przewodnik na stronie GitHub](https://github.com/rootzoll/raspiblitz) jest doskonały, ale być może zbyt szczegółowy dla użytkownika o umiarkowanym doświadczeniu. Moje instrukcje będą bardziej zwięzłe i, mam nadzieję, łatwiejsze do naśladowania.


Zasadniczo proces jest bardzo podobny do procesu konfiguracji [węzła MyNode](https://armantheparman.com/mynode-bitcoin-node-easy-setup-guide-raspberry-pi/) z Raspberry Pi 4. Przewodnik Raspiblitz sugeruje zakup monitora, ale naprawdę go nie potrzebujesz i nie polecałbym tego. Nie potrzebujesz nawet dodatkowej klawiatury ani myszy. Wystarczy uzyskać dostęp do menu terminala urządzenia za pomocą komputera w tej samej sieci domowej i użyć polecenia ssh w terminalu. Jest to możliwe w systemie Linux/Mac (łatwe) i trochę trudniejsze w systemie Windows.


## Krok 1: Zakup sprzętu.


Potrzebujesz dokładnie tego samego sprzętu, którego potrzebujesz do uruchomienia węzła MyNode. Możesz spróbować jednego lub drugiego, jedyną różnicą są dane na karcie micro SD.



- Raspberry Pi 4, 4 Gb pamięci lub 8 Gb (4 Gb to dużo)
- Oficjalne zasilanie Raspberry Pi (bardzo ważne! Nie generalizuj, poważnie)
- Obudowa dla Pi. (Obudowa FLIRC jest niesamowita. Cała obudowa jest radiatorem i nie potrzebujesz wentylatora, który może być głośny)
- karta microSD 32 Gb (potrzebna jest jedna, ale kilka się przyda)
- Czytnik kart pamięci (większość komputerów nie ma gniazda na kartę microSD).
- Zewnętrzny dysk SSD 1Tb Hard.
- Kabel Ethernet (do podłączenia do domowego routera).


Nie potrzebujesz monitora (ani klawiatury czy myszy)


Uwaga: To jest niewłaściwy dysk Hard: Jest to przenośny dysk zewnętrzny Hard. Nie jest to dysk SSD. Dysk SSD ma kluczowe znaczenie. Dlatego jest tani (cena w AUD)


![image](assets/1.webp)


Jest to właściwy typ:


![image](assets/2.webp)


Jest to szybsze rozwiązanie, ale niepotrzebnie kosztowne:


![image](assets/3.webp)


## Krok 2: Pobierz obraz Raspiblitz


Przejdź do [strony GitHub Raspiblitz](https://github.com/rootzoll/raspiblitz) i znajdź link „download image”:


![image](assets/4.webp)


Hash sha-256 pobranego pliku jest podany na stronie internetowej. Będzie się zmieniał przy każdej aktualizacji. Jeśli nie rozumiesz, o co chodzi, powinieneś, dlatego napisałem [przewodnik, który możesz przeczytać tutaj.](https://armantheparman.com/gpg/)


![image](assets/5.webp)


## Krok 3: Weryfikacja obrazu


Przed kontynuowaniem, jeśli nie znasz się na systemie plików w wierszu poleceń, łatwo się tego nauczyć i powinieneś to zrobić.


Oto [przydatne wideo dla systemu Linux, ale dotyczy także Maca](https://youtu.be/id3DGvljhT4?list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK).


Dla systemu Windows oto [prosty samouczek](https://www.youtube.com/watch?v=MBBWVgE0ewk&t=1s).


_AKTUALIZACJA: Weryfikacja pgp/gpg jest już dostępna. Będziesz potrzebować klucza publicznego Openoms. [Tutaj](http://parman.org/downloadable/openoms.txt) on jest (może być konieczne użycie trybu incognito, aby link działał – http, nie https)_
Mac/Linux


Poczekaj na zakończenie pobierania pliku (ważne!), a następnie otwórz terminal, przejdź do miejsca pobrania pliku i wpisz następujące polecenie:

```bash
shasum -a 256 xxxxxxxxxxxxxx
```


gdzie `xxxxxxxxxxxxxx` to nazwa właśnie pobranego pliku. Jeśli nie jesteś w katalogu, w którym znajduje się ten plik, musisz wpisać pełną ścieżkę.


Komputer zastanawia się przez około 20 sekund. Sprawdź, czy wyjściowy plik skrótu jest zgodny z plikiem pobranym ze strony internetowej w poprzednim kroku. Jeśli jest identyczny, możesz kontynuować.

Windows


Otwórz wiersz polecenia i przejdź do miejsca pobrania pliku, a następnie wpisz to polecenie:


```bash
certUtil -hashfile xxxxxxxxxxxxxxx SHA256
```


gdzie `xxxxxxxxxxxxxx` to nazwa właśnie pobranego pliku. Jeśli nie jesteś w reżyserze, w którym znajduje się ten plik, musisz wpisać pełną ścieżkę.


Komputer zastanawia się przez około 20 sekund. Sprawdź, czy wyjściowy plik skrótu jest zgodny z plikiem pobranym ze strony internetowej w poprzednim kroku. Jeśli jest identyczny, możesz kontynuować.


## Krok 4: Flashowanie karty SD


Możesz użyć Balena Etcher, aby to zrobić. [Pobierz go tutaj](https://www.balena.io/etcher/).


Etcher jest intuicyjny w obsłudze. Włóż kartę micro SD i sflashuj oprogramowanie Raspiblitz (plik .img) na kartę SD.


![image](assets/6.webp)


![image](assets/7.webp)


![image](assets/8.webp)


![image](assets/9.webp)


Po zakończeniu dysk nie będzie już czytelny. Może pojawić się błąd systemu operacyjnego, a dysk powinien zniknąć z pulpitu. Wyciągnij kartę.


## Krok 5: Konfiguracja Pi i włożenie karty SD


Części (nie pokazano obudowy):


![image](assets/10.webp)


![image](assets/11.webp)


Podłącz kabel ethernet i złącze USB napędu Hard (jeszcze bez zasilania). Unikaj podłączania do niebieskich portów USB na środku. Są to porty USB 3. Użyj portu USB 2, nawet jeśli dysk może obsługiwać USB 3 (bardziej niezawodny).


![image](assets/12.webp)


Karta micro SD znajduje się tutaj:


![image](assets/13.webp)


Na koniec podłącz zasilanie:


![image](assets/14.webp)


## Krok 6: Znajdź adres IP Address komputera Pi


Raspiblitz nigdy nie wymaga monitora. Potrzebujesz jednak innego komputera w sieci domowej. Jeśli Pi nie jest podłączone przez ethernet i chcesz polegać na WiFi, znalezienie adresu IP wymaga pewnych umiejętności komputerowych. Nie mogę ci pomóc, przykro mi. Potrzebujesz połączenia ethernetowego. (Problem wynika z potrzeby dostępu do monitora i systemu operacyjnego, aby podłączyć WiFi i wprowadzić hasło)


Sprawdź router, aby uzyskać listę wszystkich adresów IP wszystkich podłączonych urządzeń.


Wpisałem 192.168.0.1 w przeglądarce (instrukcje dołączone do routera), zalogowałem się i mogłem zobaczyć moje urządzenie z adresem IP 192.168.0.191. Należy pamiętać, że te adresy IP nie są publicznie widoczne w Internecie (najpierw przechodzą przez router), są tylko identyfikatorami urządzeń w sieci domowej.


Znalezienie adresu IP jest kluczowe.


**Uwaga:** Możesz użyć terminala na komputerze Mac lub Linux, aby znaleźć IP Address wszystkich urządzeń podłączonych do sieci Ethernet w sieci domowej za pomocą polecenia "arp -a". Dane wyjściowe nie są tak ładne, jak te wyświetlane przez router, ale zawierają wszystkie potrzebne informacje. Jeśli nie jest oczywiste, które to Pi, wykonaj metodę prób i błędów.


## Krok 7: SSH do Pi


Pamiętaj, aby włożyć kartę SD do Pi przed jego włączeniem. Odczekaj kilka minut, a następnie w innym systemie Linux/Mac otwórz terminal.


W przypadku systemu Mac/Linux wpisz w terminalu:


```bash
ssh admin@You_Pi's_IP_address
```


Dla systemu Windows musisz zainstalować [putty](http://putty.org/), aby połączyć się z Pi przez ssh. Wpisz tę samą komendę, co powyżej.


Za pierwszym razem lub przy każdej zmianie systemu operacyjnego Pi poprzez zmianę karty SD, może pojawić się ten błąd..


![image](assets/15.webp)


Sposobem na naprawienie tego jest przejście do miejsca, w którym znajduje się plik "known_hosts" (informuje o tym komunikat o błędzie) i usunięcie go. Polecenie to "rm known_hosts"


Następnie powtórz polecenie ssh, aby się zalogować. To się stanie..


![image](assets/16.webp)


Wpisz yes (pełne słowo), aby kontynuować.


Jeśli się powiedzie, zostaniesz poproszony o podanie hasła. Nie jest to hasło do komputera, ale do raspiblitz. Ogólne hasło to "raspiblitz", które zmienisz później. Okno terminala zmieni kolor na niebieski i pojawią się opcje menu podobne do starych menu DOS. Nawiguj za pomocą klawiszy strzałek lub myszy.


![image](assets/17.webp)


Postępuj zgodnie z instrukcjami, ustaw hasła, a następnie wykryje dysk Hard i w razie potrzeby umożliwi jego sformatowanie.


Następnie zostaniesz zapytany, czy chcesz skopiować dane Blockchain z innego źródła, czy pobrać je ponownie. Kopiowanie to proces uczenia się, a instrukcje są całkiem dobre i warto je zachować pod ręką....


![image](assets/18.webp)


Prostszym, ale wolniejszym sposobem jest pobranie całego łańcucha od zera..


![image](assets/19.webp)


Na ekranie terminala będzie migać dużo tekstu. Można to pomylić z procesem pobierania Blockchain, ale dla mnie wygląda to na generowanie klucza prywatnego do komunikacji.


Następnie pojawią się opcje błyskawicy.


![image](assets/20.webp)


Utwórz nowe hasło, aby zablokować oświetlenie Wallet, a następnie zostanie utworzony nowy Wallet i otrzymasz 24 słowa do zapisania..


![image](assets/21.webp)


Upewnij się, że to zapisałeś i trzymaj to w bezpiecznym miejscu. Słyszałem o jednej osobie, która tego nie zrobiła, ponieważ nie planowała używać Lightning, ale rok później zdecydowała się go użyć i otworzyła kanały. Następnie zdał sobie sprawę, że jego słowa nie zostały zarchiwizowane, a przypominam, że nie było możliwe ponowne wyodrębnienie słów z urządzenia, musiał zamknąć wszystkie swoje kanały i zacząć od nowa. Uszło mu to na sucho, ale inni mogą nie mieć tyle szczęścia.


Następnie kilka minut tekstu przewija się w dół okna terminala. Następnie..


![image](assets/22.webp)


Nastąpi wylogowanie z sesji ssh. Zaloguj się ponownie, tym razem za pomocą nowego hasła, hasła A. Po zalogowaniu zostaniesz poproszony o podanie hasła C, aby odblokować Lightning Wallet.


Teraz czekamy. Do zobaczenia za 2 tygodnie. Możesz zamknąć terminal, to nic nie robi z Pi, to tylko okno komunikacyjne.


![image](assets/23.webp)


Jeśli z jakiegokolwiek powodu chcesz wyłączyć Pi przed zakończeniem pobierania przez Blockchain, jest to w porządku, o ile zrobisz to poprawnie. Blockchain będzie kontynuować pobieranie od miejsca, w którym zostało przerwane po ponownym nawiązaniu połączenia.


Naciśnij CTRL+c, aby wyjść z niebieskiego ekranu. Uzyskasz dostęp do terminala Linux Pi. Tutaj możesz wpisać "menu", które załaduje następujący ekran, a stamtąd możesz wyłączyć Pi.


![image](assets/24.webp)


KONIEC przewodnika


Od teraz węzeł jest gotowy do pracy. Jeśli nadal potrzebujesz więcej opcji nawigacji, zapoznaj się z githubem, aby uzyskać więcej samouczków i przewodników https://github.com/raspiblitz/raspiblitz#feature-documentation