---
name: Mój węzeł
description: Konfiguracja węzła Bitcoin MyNode
---

![image](assets/0.webp)


[My Node](https://mynodebtc.com/) to najłatwiejszy i najpotężniejszy sposób na uruchomienie węzła Bitcoin i Lightning! Łączymy najlepsze oprogramowanie open source z naszym Interface, zarządzaniem i wsparciem, dzięki czemu możesz łatwo, prywatnie i bezpiecznie korzystać z Bitcoin i Lightning.


## Rodzaje konfiguracji węzłów


Istnieją różne konfiguracje Node. MyNode jest doskonały. Istnieje wiele aplikacji, które są z nim dostarczane, a nawet więcej, jeśli zapłacisz za wersję premium. W przeciwnym razie pobieranie wszystkich tych aplikacji jest bardzo żmudne. MyNode sprawia, że jest to całkiem proste, jak zobaczysz.


Alternatywną i podobną opcją jest RaspiBlitz. Graficzny interfejs użytkownika nie jest tak ładny, a aplikacje w dużej mierze pokrywają się z aplikacjami dostarczanymi z MyNode, ale Raspiblitz jest wolnym oprogramowaniem typu open source (FOSS), a MyNode nie do końca. Kolejną różnicą jest to, że MyNode działa w kontenerze Docker. Uważam, że Docker jest zniechęcający i Hard do rozwiązywania problemów. Jest to problem tylko wtedy, gdy napotkasz błędy lub bugi. Deweloper oferuje pomoc dla użytkowników premium i istnieje również grupa czatu Telegram.


RaspiBlitz to po prostu wiele programów zainstalowanych na Linuksie, bez Dockera. Zewnętrzny dysk Hard można łatwo podłączyć do innej maszyny z Linuksem z Bitcoin Core i w razie potrzeby działać dalej.


Inną opcją jest po prostu zainstalowanie Bitcoin Core i odmiany Electrum Server (jest ich kilka) w systemie operacyjnym. Mam przewodniki dla systemów Linux (Raspberry Pi), Mac i Windows.


## Lista zakupów



- Raspberry Pi 4, 4 Gb pamięci lub 8 Gb (4 Gb to dużo)
- Oficjalne zasilanie Raspberry Pi (bardzo ważne! Nie generalizuj, poważnie)
- Obudowa dla Pi. Obudowa FLIRC jest niesamowita. Cała obudowa jest radiatorem i nie potrzebujesz wentylatora, który może być głośny
- karta microSD 16 Gb (potrzebna jest jedna, ale kilka się przyda)
- Czytnik kart pamięci (większość komputerów nie ma gniazda na kartę microSD).
- Zewnętrzny dysk SSD 1Tb Hard.

Uwaga: dysk SSD ma kluczowe znaczenie. Nie używaj przenośnego zewnętrznego dysku Hard, nawet jeśli jest tańszy


- Kabel Ethernet (do podłączenia do domowego routera)
- Nie potrzebujesz monitora


## Pobierz MyNode Image


Przejdź do witryny MyNode Link


![image](assets/1.webp)


Kliknij `Pobierz teraz`


Pobierz wersję dla Raspberry Pi 4:


![image](assets/2.webp)


To duży plik:


![image](assets/3.webp)


Pobierz skróty SHA 256


![image](assets/4.webp)


Otwórz terminal na komputerze Mac lub Linux albo wiersz polecenia w systemie Windows. Wpisz:


```bash
shasum -a 256 DOWNLOADEDFILENAME # <--- Mac/Linux
certUtil -hashfile DOWNLOADEDFILENAME SHA256 # <--- Windows
```


Komputer zastanawia się przez około 20 sekund. Następnie sprawdź, czy wyjściowy plik skrótu jest zgodny z plikiem pobranym ze strony internetowej w poprzednim kroku. Jeśli jest identyczny, możesz kontynuować.

Flashowanie karty SD


## Pobierz i zainstaluj Balena Etcher. Link


Nie udało mi się znaleźć podpisu cyfrowego. Jeśli wiesz, jak to zrobić, daj mi znać, a zaktualizuję ten artykuł.


Etcher jest łatwy w użyciu. Włóż kartę micro SD i sflashuj oprogramowanie Raspberry Pi (plik .img) na kartę SD.


![image](assets/5.webp)

![image](assets/6.webp)

![image](assets/7.webp)

![image](assets/8.webp)

![image](assets/9.webp)

![image](assets/10.webp)

![image](assets/11.webp)


Po zakończeniu dysk nie będzie już czytelny. Może pojawić się błąd systemu operacyjnego, a dysk powinien zniknąć z pulpitu. Wyciągnij kartę.


## Skonfiguruj Pi i włóż kartę SD


Części (nie pokazano obudowy):


![image](assets/12.webp)

![image](assets/13.webp)


Podłącz kabel ethernet i złącze USB napędu Hard (jeszcze bez zasilania). Unikaj podłączania do niebieskich portów USB na środku. Są to porty USB 3. MyNode zaleca korzystanie z portu USB 2, nawet jeśli dysk może obsługiwać USB 3.


![image](assets/14.webp)


Karta micro SD znajduje się tutaj:


![image](assets/15.webp)


Na koniec podłącz zasilanie:


![image](assets/16.webp)


## Znajdź adres IP Address komputera Pi


MyNode nigdy nie wymaga monitora. Potrzebujesz jednak innego komputera w sieci domowej. Jeśli Pi nie jest podłączone przez ethernet i chcesz polegać na WiFi, znalezienie adresu IP wymaga wysokich umiejętności obsługi komputera. Nie mogę ci pomóc, przykro mi. Potrzebujesz połączenia ethernetowego. (Problem wynika z potrzeby dostępu do monitora i systemu operacyjnego, aby połączyć się z WiFi i wprowadzić hasło).


Sprawdź router, aby uzyskać listę wszystkich adresów IP wszystkich podłączonych urządzeń.


Wpisałem 192.168.0.1 w przeglądarce (instrukcje dołączone do routera), zalogowałem się i mogłem zobaczyć urządzenie "MyNode" z adresem IP 192.168.0.18. Należy pamiętać, że te adresy IP nie są publicznie widoczne w Internecie (najpierw przechodzą przez router), są tylko identyfikatorami urządzeń w sieci domowej.


Znalezienie adresu IP jest kluczowe.


**Uwaga:** Możesz użyć terminala na komputerze Mac lub Linux, aby znaleźć IP Address wszystkich urządzeń podłączonych do sieci Ethernet w sieci domowej za pomocą polecenia "arp -a". Dane wyjściowe nie są tak ładne, jak te wyświetlane przez router, ale zawierają wszystkie potrzebne informacje. Jeśli nie jest oczywiste, które to Pi, wykonaj metodę prób i błędów.


## SSH do Pi


Istnieje możliwość zdalnego zalogowania się do urządzenia za pomocą komendy SSH, ale nie jest to wymagane (w przypadku RaspiBlitz Node). Mimo to pokażę ci, jak to zrobić, ponieważ jest to bardzo przydatne.


Otwórz komputer z systemem Mac lub Linux (w przypadku systemu Windows pobierz putty, narzędzie SSH) i wpisz:


```bash
ssh admin@192.168.0.18
```


Użyj własnego adresu IP Address. Nazwa użytkownika urządzenia MyNode to domyślnie "admin". Hasło to domyślnie "Bolt".


Jeśli wcześniej korzystałeś z Pi i zmieniałeś kartę micro SD, pojawi się ten błąd:


![image](assets/17.webp)


Należy przejść do miejsca, w którym znajduje się plik "known_hosts" i usunąć go. Jest to bezpieczne. Komunikat o błędzie pokazuje ścieżkę. Dla mnie było to /Users/MyUserName/.ssh/


Nie zapomnij o "." przed ssh, oznacza to, że jest to ukryty katalog.


Następnie spróbuj ponownie wykonać polecenie ssh.


Tym razem zobaczysz następujące dane wyjściowe:


![image](assets/18.webp)


Usunięty plik został usunięty i dodawany jest nowy odcisk palca. Wpisz yes i <enter>.


Zostaniesz poproszony o wprowadzenie hasła. Jest to "Bolt"


Masz teraz dostęp terminalowy do MyNode Pi, bez monitora, i możesz potwierdzić, że wszystko ładuje się płynnie.


![image](assets/19.webp)


## Dostęp przez przeglądarkę internetową


Otwórz przeglądarkę. Musi to być komputer w sieci domowej, nie można tego zrobić z zewnątrz. Jest na to sposób, ale to Hard. Nie testowałem go.


Wpisz adres IP Address w oknie przeglądarki Address. Stanie się to możliwe:


![image](assets/20.webp)


Wprowadź hasło "Bolt" - zmień je później.


Wtedy to się stanie:


![image](assets/21.webp)


Wybierz Formatuj dysk


![image](assets/22.webp)


Teraz czekamy.


W pewnym momencie zostaniesz zapytany, czy chcesz wprowadzić klucz produktu, czy skorzystać z bezpłatnej "edycji społecznościowej" - zamierzam pokazać edycję Premium. Polecam zapłacić za wersję Premium, jeśli możesz sobie na to pozwolić, jest to bardzo tego warte.


![image](assets/23.webp)


Następnie zobaczysz postęp pobierania bloków. Zajmuje to kilka dni:


![image](assets/24.webp)


W razie potrzeby można bezpiecznie wyłączyć urządzenie podczas pobierania. Przejdź do ustawień i znajdź przycisk wyłączania urządzenia. Nie szarp za przewód, bo możesz uszkodzić instalację lub dysk Hard.


Upewnij się, że wcześnie przejdziesz do "Ustawień" i wyłączysz quicksync. Spowoduje to rozpoczęcie pobierania początkowego bloku od początku.


![image](assets/25.webp)


Chciałem kontynuować tworzenie przewodnika, więc oto kolejny MyNode, który przygotowałem wcześniej. Tak wygląda strona, gdy Blockchain jest zsynchronizowany, a kilka "aplikacji" zostało włączonych i zsynchronizowanych:


![image](assets/26.webp)


Pamiętaj, że serwer Electrum również wymaga synchronizacji, więc jak tylko Bitcoin Blockchain zostanie zsynchronizowany, kliknij przycisk, aby rozpocząć ten proces - zajmie to dzień lub dwa. Wszystko inne zostanie włączone w ciągu kilku minut po wybraniu opcji włączenia. Możesz klikać różne rzeczy i eksplorować. Niczego nie zepsujesz. Jeśli coś się zepsuje (zdarzyło mi się to, ale myślę, że dlatego, że miałem tanie części), będziesz musiał przeflashować i zacząć pobieranie od nowa. Problem z MyNode polega na tym, że jeśli musisz "przeflashować", musisz ponownie rozpocząć synchronizację Blockchain od zera. Istnieją techniczne sposoby na obejście tego problemu, ale nie jest to łatwe.


Jeśli chcesz wypróbować również inny węzeł, powiedzmy RaspiBlitz, potrzebujesz dodatkowego zewnętrznego dysku SSD Hard i kolejnej karty micro SD do flashowania. W przeciwnym razie jest to ten sam sprzęt, po prostu nie można uruchomić MyNode i RaspiBlitz jednocześnie, oczywiście. Jeśli chcesz to zrobić, czas na zakup innego Raspberry Pi.


Teraz, gdy masz już uruchomiony węzeł, używaj go, nie pozwól, by siedział i nic dla ciebie nie robił. Śledź mój artykuł (i wideo) na temat podłączania Electrum Desktop Wallet do Electrum Server i Bitcoin Core tutaj.