---
name: Dojo
description: Węzeł Bitcoin o otwartym kodzie źródłowym zapewniający prywatność i autonomię
---

![cover](assets/cover.webp)



*Ten samouczek jest oparty na [oficjalnej dokumentacji Ashigaru](https://ashigaru.rs/docs/), którą przejąłem i rozszerzyłem. Przepisałem wszystkie sekcje, aby poprawić przejrzystość, dodałem dalsze szczegółowe wyjaśnienia, a także ilustracje dla początkujących, aby instalacja i użytkowanie były łatwiejsze do zrozumienia *



---

Dojo to program typu open-source zaprojektowany do działania jako serwer zaplecza dla niektórych zorientowanych na prywatność portfeli Bitcoin, opartych na węźle Bitcoin core. Historycznie, został on opracowany do współpracy z Samourai Wallet, mobilnym Wallet, który oferował zaawansowane funkcje prywatności, takie jak Whirlpool (CoinJoin), Ricochet, Stonewall, PayNym.... Samourai Wallet został zamknięty po aresztowaniu jego twórców, ale jego społecznościowy następca, **Ashigaru Wallet**, przejął go i nadal polega na Dojo, oferując pełne doświadczenie użytkownikom, którzy chcą zachować kontrolę nad swoimi danymi podczas korzystania z Bitcoin.



![Image](assets/fr/01.webp)



W praktyce Dojo działa jako brama między Wallet a siecią Bitcoin. Bez Dojo, lekki mobilny Wallet musiałby odpytywać serwery stron trzecich, aby uzyskać status UTXO i historię lub rozgłaszać transakcje. Oznacza to zależność i wyciek wrażliwych danych do serwera strony trzeciej (użyte adresy, kwoty, częstotliwość płatności itp.). Dzięki Dojo sam hostujesz ten serwer, bezpośrednio podłączony do własnego węzła Bitcoin. W ten sposób wszystkie żądania portfela przechodzą przez infrastrukturę, którą kontrolujesz, bez pośredników, wzmacniając Twoją poufność i suwerenność.



## Wymagania dotyczące założenia Dojo



Konfiguracja serwera Dojo nie wymaga ultra wydajnej maszyny. Każdy z podstawowym komputerem, stabilnym połączeniem internetowym i możliwością pozostawienia go włączonego bez przerwy (24/7) może skonfigurować działające Dojo.



### Wybierz typ urządzenia



Można użyć :




- laptop ;
- komputer stacjonarny;
- mini-PC (np. Intel NUC, Lenovo Thincentre Tiny...).



Każda opcja ma swoje wady i zalety:




- Cena: odnowiony mini-PC lub komputer stacjonarny będzie często tańszy niż nowy laptop.
- Zajmowana powierzchnia: Mini-PC zajmuje mniej miejsca.
- Zasilanie Supply: laptop ma przewagę w postaci baterii, co oznacza, że nie wyłączy się w przypadku przerwy w dostawie prądu, w przeciwieństwie do mini-PC.
- Możliwość rozbudowy: barbony zazwyczaj umożliwiają dodanie pamięci lub łatwą wymianę dysku Hard.



Więcej informacji na temat wyboru sprzętu można znaleźć w tym kursie:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

### Zalecany sprzęt



Nie ma potrzeby kupowania nowej maszyny. Odnowiony komputer o poniższych specyfikacjach zapewni znacznie lepszą wydajność niż elektronika jednopłytkowa (taka jak Raspberry Pi).



**Minimalne specyfikacje:**




- Architektura X86-64 (procesor 64-bitowy).
- dwurdzeniowy procesor 2 GHz lub szybszy.
- minimum 8 GB pamięci RAM.
- 2 TB lub więcej NVMe SSD (do przechowywania Blockchain i Bitcoin oraz niezbędnych indeksów).



**Zalecany system operacyjny: **




- Dystrybucja oparta na Debianie, taka jak Ubuntu 24.04 LTS.



**Zalecany sprzęt:**




- HP EliteDesk / EliteBook
- Dell OptiPlex
- Lenovo ThinkCentre / ThinkPad
- Intel NUC
- itp.



Uruchomienie serwera Dojo na innych konfiguracjach sprzętowych jest całkowicie możliwe. Aby jednak uzyskać najlepszą wydajność i ograniczyć problemy, zalecamy przestrzeganie powyższych zaleceń.



W tym poradniku użyję starego ThinkCentre Tiny z dwurdzeniowym procesorem Intel Pentium G4400T, 8 GB pamięci RAM i dyskiem SSD o pojemności 2 TB.



## 1 - Instalacja Ubuntu



*Jeśli chcesz zainstalować Dojo na już skonfigurowanym urządzeniu, możesz pominąć ten krok i przejść bezpośrednio do kroku 2.*



Po przygotowaniu wybranego sprzętu czas na instalację systemu operacyjnego. Możesz użyć praktycznie dowolnej dystrybucji Debiana, ale polecam wybrać wersję LTS Ubuntu, ponieważ idealnie nadaje się do naszych celów. Oto kroki, które należy wykonać:



### 1.1. utworzyć bootowalny klucz USB



Z już działającego komputera (zwykłej maszyny) pobierz obraz ISO Ubuntu LTS [z oficjalnej strony](https://ubuntu.com/download/desktop) (`24.04` w momencie pisania tego tekstu, ale weź najnowszy, jeśli inny jest dostępny).



![Image](assets/fr/02.webp)



Włóż klucz USB o pojemności co najmniej 8 GB do tego komputera, a następnie utwórz klucz rozruchowy za pomocą oprogramowania takiego jak [Balena Etcher](https://etcher.balena.io/). Wybierz obraz ISO Ubuntu, który właśnie pobrałeś, wybierz klucz USB jako urządzenie docelowe, a następnie rozpocznij proces tworzenia (bądź cierpliwy, może to potrwać kilka minut).



![Image](assets/fr/03.webp)



Włóż bootowalny klucz USB do wyłączonego komputera (tego, na którym chcesz uruchomić Dojo). Uruchom komputer i natychmiast naciśnij **F12** lub **F10** na klawiaturze (w zależności od modelu), aby uzyskać dostęp do menu rozruchowego. Następnie wybierz klucz USB jako urządzenie priorytetowe w kolejności uruchamiania komputera.



![Image](assets/fr/04.webp)



### 1.2. zainstalować system operacyjny



Pojawi się ekran główny Ubuntu. Wybierz "Wypróbuj lub zainstaluj Ubuntu*".



![Image](assets/fr/05.webp)



Następnie postępuj zgodnie z klasycznym procesem instalacji Ubuntu:




- Wybierz język.
- Wybierz typ klawiatury.
- W przypadku połączenia kablem RJ45 nie ma potrzeby konfigurowania sieci Wi-Fi.
- Kliknij "*Install Ubuntu*" i zaznacz opcję instalacji oprogramowania innych firm (sterowniki Wi-Fi, kodeki multimedialne itp.).
- Gdy kreator zapyta o typ instalacji, wybierz "*Erase disk and install Ubuntu*". **Ostrzeżenie**: ta operacja całkowicie usunie zawartość dysku. Sprawdź dokładnie, czy wybrany dysk odpowiada NVMe SSD przeznaczonemu dla Dojo.
- Utwórz prostą nazwę użytkownika (np. "*loic*").
- Przypisz nazwę do maszyny (np. "*dojo-node*").
- Ustaw silne hasło i przechowuj je w bezpiecznym miejscu.
- Włącz opcję "*Poproś o moje hasło, aby się zalogować*", aby zwiększyć bezpieczeństwo.
- Wskaż swoją strefę czasową, a następnie kliknij "*Install*".
- Poczekaj na zakończenie instalacji. Po jej zakończeniu system uruchomi się ponownie automatycznie.
- Odłącz klucz instalacyjny USB podczas ponownego uruchamiania komputera.



Więcej szczegółów na temat procesu instalacji Ubuntu można znaleźć w naszym dedykowanym samouczku :



https://planb.academy/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

### 1.3. aktualizacja systemu



Po pierwszym uruchomieniu należy otworzyć terminal za pomocą kombinacji klawiszy ***Ctrl + Alt + T*** i uruchomić następujące polecenia, aby zaktualizować system:



```bash
sudo apt update
sudo apt upgrade -y
```



![Image](assets/fr/06.webp)



## 2. Instalacja w budynku gospodarczym



Aby Dojo działało poprawnie, w systemie muszą być obecne pewne elementy oprogramowania. Służą one do zarządzania repozytoriami oprogramowania, komunikacji, dekompresji archiwów i wykonywania Dojo wewnątrz kontenerów Docker. Wszystkie te operacje wykonywane są w terminalu.



### 2.1. Przygotowanie



Poniższe polecenie powoduje powrót do folderu osobistego. Jest to dobra praktyka przed uruchomieniem serii instalacji.



```bash
cd ~/
```



Przed zainstalowaniem jakiegokolwiek oprogramowania należy upewnić się, że baza danych oprogramowania dostępnego na komputerze jest aktualna. Pozwoli to uniknąć instalowania przestarzałych wersji.



```bash
sudo apt-get update
```



![Image](assets/fr/07.webp)



### 2.2. zainstalować narzędzia



Do systemu należy dodać kilka narzędzi:




- `apt-transport-https`: pozwala na bezpieczne pobieranie pakietów przez HTTPS
- `ca-certificates`: zarządza certyfikatami wymaganymi dla szyfrowanych połączeń
- `curl`: do pobierania plików z Internetu
- `gnupg-agent`: do zarządzania kluczami GPG
- software-properties-common`: zapewnia narzędzia do manipulowania repozytoriami APT
- `unzip`: rozpakowuje pliki w formacie ZIP



```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common unzip
```



Podczas instalacji system może poprosić o potwierdzenie. Naciśnij przycisk "*y*", a następnie "*Enter*".



![Image](assets/fr/08.webp)



### 2.3. zainstalować Torsocks



Torsocks umożliwia wykonywanie niektórych poleceń za pośrednictwem sieci Tor, poprawiając poufność komunikacji.



```bash
sudo apt install torsocks
```



![Image](assets/fr/09.webp)



### 2.4. zainstalować Docker i Docker Compose



Dojo działa wewnątrz kontenerów Docker. Oznacza to, że każda usługa jest izolowana w niezależnym środowisku, co upraszcza konserwację i bezpieczeństwo. Aby to zrobić, należy zainstalować Docker i narzędzie Docker Compose, które umożliwia zarządzanie kilkoma kontenerami jednocześnie.



#### Dodaj klucz podpisywania Docker



Docker udostępnia własny klucz podpisu cyfrowego. Dodanie go weryfikuje autentyczność pobranych pakietów.



```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```



![Image](assets/fr/10.webp)



#### Dodano oficjalne repozytorium Docker



Następnie należy powiedzieć systemowi, gdzie znaleźć oficjalne pakiety Docker. To polecenie dodaje nowe repozytorium do konfiguracji menedżera pakietów.



```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "*$VERSION_CODENAME*") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```



![Image](assets/fr/11.webp)



#### Instalacja Docker i Docker Compose



Teraz można zainstalować główne komponenty Dockera.



```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```



![Image](assets/fr/12.webp)



#### Autoryzacja użytkownika



Domyślnie tylko polecenia wykonywane z uprawnieniami administratora mogą uruchomić Dockera. Dla większej wygody zalecam dodanie bieżącego użytkownika do grupy "*docker*". Pozwoli to na korzystanie z Dockera bez konieczności wpisywania `sudo` za każdym razem.



```bash
sudo usermod -aG docker $USER
```



![Image](assets/fr/13.webp)



## 3. Tworzenie pojedynczego użytkownika (opcjonalnie)



Jeśli chcesz poprawić bezpieczeństwo swojego systemu, zalecam utworzenie osobnego użytkownika wyłącznie do uruchamiania Dojo. Taka separacja ogranicza ryzyko: jeśli problem z bezpieczeństwem wystąpi w Dojo, nie zagrozi on bezpośrednio głównemu kontu.



### 3.1. tworzenie konta użytkownika



Poniższe polecenie tworzy nowego użytkownika o nazwie "*dojo*". Użytkownik ten będzie miał katalog domowy `/home/dojo` i dostęp do terminala bash. Zostanie również dodany do grupy sudo, aby umożliwić wykonywanie poleceń administratora.



```bash
sudo useradd -s /bin/bash -d /home/dojo -m -G sudo dojo
```



### 3.2. Ustawianie hasła



Ważne jest, aby przypisać silne hasło do tego konta. Najlepiej byłoby użyć menedżera haseł, takiego jak Bitwarden, aby generate było długą kombinacją Hard do odgadnięcia.



```bash
sudo passwd dojo
```



System poprosi o wprowadzenie wybranego hasła, a następnie potwierdzi je po raz drugi.



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

### 3.3. Autoryzacja użytkownika do korzystania z Dockera



Aby umożliwić użytkownikowi "*dojo*" uruchamianie kontenerów potrzebnych do uruchomienia Dojo, musi on zostać dodany do grupy Docker. Pozwala to uniknąć konieczności poprzedzania każdego polecenia poleceniem `sudo`.



```bash
sudo usermod -aG docker dojo
```



### 3.4. Restart systemu



Aby zmiany grupy zaczęły obowiązywać, należy ponownie uruchomić urządzenie.



```bash
sudo reboot
```



### 3.5. Zaloguj się jako nowy użytkownik



Po ponownym uruchomieniu systemu zaloguj się przy użyciu loginu ***dojo*** i zdefiniowanego wcześniej hasła. Wszystkie kolejne kroki muszą być wykonywane z tego dedykowanego konta.



## 4. Pobierz i sprawdź Dojo



Przed instalacją Dojo należy upewnić się, że pliki pochodzą od oficjalnego dewelopera i nie zostały zmodyfikowane. Ten krok opiera się na wykorzystaniu PGP i skrótów do weryfikacji autentyczności i integralności plików.



### 4.1. zaimportować klucz PGP dewelopera



Pobierz klucz publiczny dewelopera przez Tor i zaimportuj go do lokalnego pęku kluczy. Klucz ten będzie używany do weryfikacji podpisów powiązanych z plikami Dojo.



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/14.webp)



### 4.2. pobrać najnowszą wersję Dojo



Pobierz skompresowane archiwum zawierające kod źródłowy Dojo. W tym przykładzie najnowsza wersja to `1.27.0`: zmodyfikuj polecenie zgodnie z [najnowsza wersja tutaj na oficjalnym repozytorium GitHub](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases).



```bash
torsocks wget -O samourai-dojo-1.27.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.27.0.zip
```



![Image](assets/fr/15.webp)



### 4.3. Pobierz odciski palców i podpis



Deweloperzy publikują plik z listą cyfrowych odcisków palców archiwów, a także plik podpisany ich kluczem PGP. Pobierz je, aby porównać swoje pliki lokalnie.



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt.sig
```



![Image](assets/fr/16.webp)



### 4.4. Sprawdź podpis PGP



Sprawdź, czy plik odcisku palca został podpisany zaimportowanym kluczem.



```bash
gpg --verify samourai-dojo-1.27.0-fingerprints.txt.sig
```



Prawidłowy wynik wyświetla ważny podpis z kluczem `E53AD419B242822F19E23C6D3033D463D6E544F6` i powiązanym Address `dojocoder@pm.me`. Może pojawić się ostrzeżenie informujące, że klucz nie jest certyfikowany: można je zignorować.



Jeśli natomiast podpis jest nieprawidłowy, należy natychmiast przerwać proces instalacji i rozpocząć go od początku.



![Image](assets/fr/17.webp)



### 4.5. Sprawdź integralność archiwum



Oblicz odcisk palca SHA256 pobranego pliku, a następnie otwórz plik odcisku palca, aby porównać dwie wartości.



```bash
sha256sum samourai-dojo-1.27.0.zip
cat samourai-dojo-1.27.0-fingerprints.txt
```



Jeśli oba odciski palców są identyczne, można mieć pewność, że archiwum nie zostało zmodyfikowane. Jeśli się różnią, nie idź dalej i usuń pliki.



![Image](assets/fr/18.webp)



### 4.6. Wyodrębnianie i porządkowanie plików



Po pomyślnym zakończeniu weryfikacji można rozpakować archiwum i przygotować folder dedykowany instalacji Dojo.



```bash
unzip samourai-dojo-1.27.0.zip -d .
mkdir ~/dojo-app
mv ~/samourai-dojo-1.27.0/* ~/dojo-app/
```



![Image](assets/fr/19.webp)



### 4.7. Wyczyść niepotrzebne pliki



Usuń pliki tymczasowe i archiwa, które nie są już potrzebne, aby utrzymać środowisko w czystości.



```bash
rm -r samourai-dojo-1.27.0 && rm samourai-dojo-1.27.0.zip && rm samourai-dojo-1.27.0-fingerprints.txt && rm samourai-dojo-1.27.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/20.webp)



## 5. Konfiguracja Dojo



Dojo to serwer zaplecza, który łączy kilka usług do interakcji z portfolio i zarządzania węzłem Bitcoin. Jego konfiguracja może być złożona, ale projekt oferuje uproszczoną metodę, która automatycznie instaluje i konfiguruje następujące komponenty:




- Dojo (główne API)
- Bitcoin core (kompletny węzeł Bitcoin)
- BTC-RPC Explorer (web Block explorer)
- Fulcrum Indexer (szybkie indeksowanie bloków i transakcji)
- Serwer Fulcrum Electrum dostępny w sieci Tor
- Serwer Fulcrum Electrum dostępny w sieci lokalnej
- Poświadczenia administracyjne



### 5.1. poświadczenia administracyjne



Aby zabezpieczyć dostęp do różnych usług, należy użyć generate kilku unikalnych identyfikatorów:




- `BITCOIND_RPC_USER`
- `BITCOIND_RPC_PASSWORD`
- `MYSQL_ROOT_PASSWORD`
- mYSQL_USER
- `MYSQL_PASSWORD`
- nODE_API_KEY`
- `NODE_ADMIN_KEY`
- `NODE_JWT_SECRET`



Identyfikatory te **muszą być unikalne** (jest to bardzo ważne: nie wolno używać tego samego hasła do kilku usług), składać się wyłącznie z cyfr, wielkich i małych liter (alfanumerycznych) i mieć długość około 40 znaków, aby zagwarantować wysoki poziom bezpieczeństwa. Po raz kolejny zdecydowanie zalecam korzystanie z menedżera haseł.



### 5.2. Dostęp do plików konfiguracyjnych



Pliki konfiguracyjne Dojo znajdują się w folderze `conf/`. Przejdź do tego katalogu:



```bash
cd ~/dojo-app/docker/my-dojo/conf/
```



![Image](assets/fr/21.webp)



### 5.3. Konfiguracja Bitcoin core



Otwórz plik konfiguracyjny Bitcoin core za pomocą edytora tekstu nano:



```bash
nano docker-bitcoind.conf.tpl
```



![Image](assets/fr/22.webp)



W tym pliku należy wprowadzić wygenerowane identyfikatory:



```
BITCOIND_RPC_USER=your-ID-here
BITCOIND_RPC_PASSWORD=your-password-here
```



⚠️ ***Zastąp `your-ID-here` i `your-password-here` własnymi loginami (z silnym hasłem).***



Możesz także dostosować rozmiar pamięci podręcznej używanej przez Bitcoin core, aby poprawić wydajność (możesz nawet użyć więcej, jeśli masz dużo dostępnej pamięci RAM):



```
BITCOIND_DB_CACHE=2048
```



Aby zapisać zmiany i zamknąć edytor :




- naciśnij `Ctrl + X
- typ `y`
- następnie naciśnij "*Enter*"



### 5.4. Konfiguracja MySQL



Następnie otwórz konfigurację bazy danych MySQL:



```bash
nano docker-mysql.conf.tpl
```



Wprowadź swoje dane logowania:



```
MYSQL_ROOT_PASSWORD=your-password-here
MYSQL_USER=your-ID-here
MYSQL_PASSWORD=your-password-here
```



⚠️ ***Zastąp `your-ID-here` i `your-password-here` własnymi loginami (z silnymi, unikalnymi hasłami)



Zapisz w ten sam sposób (`Ctrl + X`, `y`, "*Enter*").



![Image](assets/fr/23.webp)



### 5.5. Konfiguracja indeksatora Fulcrum



Otwórz następujący plik:



```bash
nano docker-indexer.conf.tpl
```



Dodaj parametry, aby aktywować Fulcrum i poprawnie zintegrować go z Dojo :



```
INDEXER_INSTALL=on
INDEXER_TYPE=fulcrum
INDEXER_BATCH_SUPPORT=active
INDEXER_EXTERNAL=on
```



![Image](assets/fr/24.webp)



Następnie istnieją 2 możliwości, w zależności od konfiguracji. Jeśli Dojo jest zainstalowane na maszynie oddzielonej od codziennego komputera (na dedykowanej maszynie, serwerze...), wprowadź jego IP Address w sieci lokalnej, na przykład :



```
INDEXER_EXTERNAL_IP=192.168.1.157
```



![Image](assets/fr/25.webp)



Aby sprawdzić lokalny adres IP Address komputera, otwórz inny terminal i wprowadź następujące polecenie:



```bash
hostname -I
```



Druga możliwość: jeśli Dojo jest uruchamiane bezpośrednio na codziennym komputerze osobistym, należy zachować domyślną wartość już obecną w pliku konfiguracyjnym :



```
INDEXER_EXTERNAL_IP=127.0.0.1
```



Zapisz i wyjdź z edytora (`Ctrl + X`, `y`, "*Enter*").



### 5.6. Konfiguracja usługi węzła



Na koniec otwórz konfigurację głównej usługi Dojo:



```bash
nano docker-node.conf.tpl
```



Wprowadź swoje dane logowania:



```
NODE_API_KEY=your-password-here
NODE_ADMIN_KEY=your-password-here
NODE_JWT_SECRET=your-password-here
```



⚠️ ***Zastąp `twoje-hasło-tutaj` własnymi danymi uwierzytelniającymi (z silnymi, unikalnymi hasłami).***



![Image](assets/fr/26.webp)



Następnie aktywuj lokalny indeksator:



```
NODE_ACTIVE_INDEXER=local_indexer
```



Zapisz i wyjdź z edytora (`Ctrl + X`, `y`, "*Enter*").



### 5.7. Zarządzanie logowaniem



Po zakończeniu konfiguracji nie jest konieczne zapisywanie wszystkich wygenerowanych identyfikatorów. Jedynym, który bezwzględnie musi zostać zapisany jest :



```
NODE_ADMIN_KEY
```



Ten login umożliwi późniejsze zalogowanie się do narzędzia konserwacji Dojo. Wszystkie pozostałe loginy można usunąć z menedżera haseł lub odręcznych notatek. Pozostają one dostępne z plików konfiguracyjnych Dojo, jeśli zajdzie potrzeba ich odzyskania w przyszłości.



## 6. Instalacja Dojo



Na tym etapie Dojo zostanie zainstalowane i uruchomione na komputerze. Operacja uruchomi kilka usług (Bitcoin core, indeksator Fulcrum, backend Dojo itp.) i zainicjuje pełną synchronizację Blockchain Bitcoin. Może to potrwać kilka dni, w zależności od sprzętu i połączenia internetowego.



### 6.1. Sprawdź, czy Docker działa poprawnie



Przed rozpoczęciem instalacji upewnij się, że Docker działa. Uruchom następujące polecenie:



```bash
docker run hello-world
```



To polecenie pobiera i uruchamia mały kontener testowy. Jeśli wszystko działa poprawnie, powinieneś zobaczyć komunikat podobny do :



```
Hello from Docker!
This message shows that your installation appears to be working correctly...
```



![Image](assets/fr/27.webp)



Jeśli ten komunikat nie jest wyświetlany, należy rozpocząć od ponownego uruchomienia komputera za pomocą :



```bash
sudo reboot
```



Następnie zaloguj się ponownie na swoje konto **dojo** i ponownie uruchom polecenie testowe. Jeśli błąd nadal występuje, Docker nie został poprawnie zainstalowany. W takim przypadku wróć do kroku `2.4.` instalacji Dockera i dokładnie sprawdź każde polecenie.



### 6.2. Przejdź do katalogu instalacyjnego Dojo



Skrypty wymagane do instalacji znajdują się w folderze `my-dojo`. Przejdź do tego katalogu:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/28.webp)



Użyj polecenia `ls`, aby sprawdzić obecność pliku `dojo.sh`. Jest to główny skrypt, który automatyzuje instalację Dojo i uruchamianie wszystkich jego usług.



![Image](assets/fr/29.webp)



### 6.3. Rozpocznij instalację



Rozpocznij instalację, uruchamiając program :



```bash
./dojo.sh install
```



Potwierdź instalację, naciskając `y`, a następnie "*Enter*".



![Image](assets/fr/30.webp)



Ten skrypt będzie :




- pobrać i uruchomić niezbędne kontenery Docker,
- zainicjować Bitcoin core i rozpocząć synchronizację Blockchain,
- uruchom indeksator Fulcrum, aby śledzić transakcje i adresy,
- aktywuje backend Dojo i jego API.



Zobaczysz stały strumień przewijających się dzienników, z kolorowymi odniesieniami, takimi jak `bitcoind`, `soroban`, `nodejs` lub `fulcrum`. To przewijanie wskazuje, że Dojo jest uruchomione i zaczyna wykonywać różne usługi.



![Image](assets/fr/31.webp)



### 6.4. Zakończenie wyświetlania dziennika



Dzienniki pojawiają się w czasie rzeczywistym w terminalu. Aby powrócić do wiersza poleceń, gdy Dojo działa w tle, wpisz :



```
Ctrl + C
```



Nie martw się: zatrzymanie wyświetlania dziennika nie zatrzymuje usług. Docker nadal uruchamia Dojo w tle (oczywiście nie musisz zatrzymywać komputera, jeśli chcesz, aby IBD nadal działał).



### 6.5. Zrozumienie *Initial Block Download* (IBD)



Podczas uruchamiania, Bitcoin core musi pobrać i zweryfikować cały Blockchain od 2009 roku. Krok ten nazywany jest ***Initial Block Download* (IBD)**. Jest on niezbędny, ponieważ umożliwia węzłowi Dojo weryfikację każdego bloku Bitcoin i transakcji niezależnie.



Czas trwania tej synchronizacji zależy od kilku czynników:




- moc procesora i ilość dostępnej pamięci RAM,
- prędkość dysku,
- liczba i jakość peerów, z którymi łączy się węzeł,
- szybkość połączenia internetowego.



W praktyce operacja ta trwa zazwyczaj od **2 do 7 dni**. W tym czasie można pozostawić urządzenie włączone bez przerwy. Im dłużej maszyna jest włączona, tym szybciej synchronizacja zostanie zakończona. Radzę regularnie sprawdzać stan synchronizacji, przeglądając dzienniki Bitcoin core lub korzystając z narzędzia do konserwacji Dojo po zainstalowaniu (patrz następna sekcja).



Aby pogłębić swoją wiedzę na temat IBD i, bardziej ogólnie, działania i roli węzła Bitcoin, polecam zapoznać się z tym kursem:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426


## 7. Monitorowanie synchronizacji



Podczas pierwszej instalacji Dojo należy poczekać na zakończenie dwóch głównych operacji: pełne pobranie Blockchain Bitcoin (*IBD*) i indeksowanie tego Blockchain przez Fulcrum. W zależności od połączenia i mocy urządzenia może to potrwać kilka dni. W tym czasie można monitorować postęp procesu, aby upewnić się, że wszystko przebiega sprawnie.



Istnieją dwa sposoby monitorowania stanu synchronizacji:




- korzystanie z Dojo Maintenance Tool (lub DMT), które jest proste, ale zapewnia niewiele szczegółów podczas IBD;
- bezpośrednie sprawdzanie logów Dojo na komputerze, bardziej techniczne, ale znacznie bardziej precyzyjne.



### 7.1. Sprawdź za pomocą Dojo Maintenance Tool (DMT)



Dojo Maintenance Tool to bezpieczny, internetowy Interface, który pozwala monitorować stan instalacji i wykonywać określone operacje. Jest to najłatwiejszy i najbardziej dostępny sposób monitorowania postępów IBD. Podczas początkowej fazy synchronizacji wyświetlane informacje mogą być ograniczone. Na przykład DMT nie pokazuje szczegółowego postępu indeksowania Fulcrum. Z drugiej strony, po zakończeniu synchronizacji, DMT będzie wyraźnie wyświetlać :




- wszystkie światła na Green;
- ostatni zatwierdzony blok dla każdej usługi (Node, Indexer, Dojo DB).



Aby uzyskać do niego dostęp, musisz znać adres URL swojego DMT i połączyć się z nim [za pośrednictwem przeglądarki Tor](https://www.torproject.org/download/). Aby to zrobić, otwórz terminal i przejdź do katalogu `/my-dojo`:



```bash
cd ~/dojo-app/docker/my-dojo
```



Następnie uruchom następujące polecenie:



```bash
./dojo.sh onion
```



![Image](assets/fr/32.webp)



Będziesz wtedy miał dostęp do wszystkich informacji dotyczących połączeń z Dojo za pośrednictwem Tora. Interesujący nas tutaj jest następujący adres URL:



```
Dojo API and Maintenance Tool =
```



Aby uzyskać dostęp do DMT z dowolnego komputera w dowolnej sieci (nawet zdalnie), otwórz przeglądarkę Tor Browser i wprowadź ten adres URL, a następnie `/admin`. Na przykład, jeśli twój adres URL to `wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion`, musisz wpisać w pasku [Tor Browser](https://www.torproject.org/download/):



```
wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion/admin
```



⚠️ **Prosimy o zachowanie tego Address w ścisłej tajemnicy



Nastąpi przekierowanie do strony uwierzytelniania. DMT jest zalogowany przy użyciu wygenerowanego wcześniej hasła `NODE_ADMIN_KEY`.



![Image](assets/fr/33.webp)



Po zalogowaniu można uzyskać dostęp do *Dojo Maintenance Tool*! Podczas IBD można zobaczyć informacje "*Latest Block*" w menu "*Full node*", które pozwalają poznać aktualny stan węzła Bitcoin.



![Image](assets/fr/34.webp)



Pamiętaj, aby dodać ten Address do zakładek w przeglądarce Tor Browser w celu późniejszego łatwego odnalezienia.



Gdy Dojo zostanie w pełni zsynchronizowane, powinieneś zobaczyć Green check ✅ na wszystkich wskaźnikach na stronie głównej DMT.



### 7.2. Weryfikacja za pomocą logów Dojo



Drugim sposobem śledzenia postępów IBD jest bezpośrednie sprawdzanie dzienników maszyny. To podejście oferuje znacznie bardziej precyzyjne monitorowanie w czasie rzeczywistym. Możesz zobaczyć, jak Bitcoin core postępuje w pobieraniu bloków i jak Fulcrum je indeksuje.



Połącz się z maszyną hostującą Dojo i otwórz terminal. Wszystkie polecenia powinny być wykonywane z katalogu `my-dojo`. Ustaw się w tym folderze:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/35.webp)



#### Dzienniki Bitcoin core



Wyświetlanie dzienników Bitcoin core w celu śledzenia postępów IBD:



```bash
./dojo.sh logs bitcoind
```



Na początku widoczna jest faza wstępnej synchronizacji nagłówków bloków:



```
bitcoind | Pre-synchronizing blockheader, height : NNNNNN
```



Gdy liczba ta osiągnie 100%, Bitcoin core rozpocznie pełne pobieranie Blockchain. Zobaczysz postęp IBD. Aby sprawdzić aktualną wysokość bloku, spójrz na wartość wskazaną przez `height=`. Można również śledzić klucz `progress=`, który wskazuje procent postępu IBD.



![Image](assets/fr/36.webp)



Jak zawsze, aby zamknąć dzienniki i powrócić do wiersza poleceń, użyj kombinacji klawiszy `Ctrl + C`.



#### Dzienniki Fulcrum



Po zakończeniu wstępnej synchronizacji nagłówka Bitcoin core, Fulcrum rozpoczyna indeksowanie Blockchain. Wyświetl jego logi za pomocą :



```bash
./dojo.sh logs fulcrum
```



Zobaczysz wtedy wysokość ostatniego zindeksowanego bloku, wskazaną po `height:`, a także procentowy postęp indeksowania.



![Image](assets/fr/37.webp)



### 7.3. Uszkodzenie bazy danych Fulcrum



Fulcrum jest szczególnie potężnym indeksatorem, ale jego instalacja może być skomplikowana, nie tylko ze względu na delikatne zarządzanie bazą danych. W przypadku przerwy w zasilaniu lub nagłego wyłączenia maszyny podczas początkowej synchronizacji, baza danych indeksera może zostać uszkodzona. Można to zaobserwować na przykład w następujących dziennikach:



```bash
fulcrum | The database has been corrupted etc...
```



**Uwaga:** Ten typ błędu powinien zostać poprawiony w nadchodzącej wersji Fulcrum 2.0.



Jeśli tak się stanie, nie będzie to miało wpływu na bitcoind (węzeł Bitcoin): jego IBD będzie kontynuowany niezależnie od Fulcrum. Nie będziesz jednak mógł korzystać z Fulcrum, dopóki nie usuniesz uszkodzonych danych i nie uruchomisz ponownie synchronizacji od początku. Oto jak to działa:



Stop Dojo:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Usuń tylko kontener i wolumin Fulcrum:



```bash
docker rm -f fulcrum || true
docker volume ls | grep -i fulcrum
docker volume rm my-dojo_data-fulcrum
```



Zwykle nazwa to `my-dojo_data-fulcrum`, jeśli tak nie jest w twoim przypadku, dostosuj nazwę zwróconą przez poprzednie polecenie.



Następnie ponownie uruchom Dojo i odbuduj Fulcrum od podstaw:



```bash
./dojo.sh upgrade
```



Następnie można sprawdzić, czy Fulcrum działa poprawnie, przeglądając dzienniki:



```bash
docker logs -f fulcrum
```




## 8. Korzystanie z narzędzia konserwacji Dojo



Gdy węzeł Bitcoin zostanie zsynchronizowany z głowicą osnowy za pomocą Proof of Work, a Blockchain zostanie w 100% zindeksowany przez Fulcrum, można rozpocząć korzystanie z Dojo.



Dojo oferuje szeroki zakres funkcji, regularnie ulepszanych z każdą nową wersją. Moim zdaniem 2 najważniejsze z nich to :




- możliwość podłączenia Ashigaru Wallet w celu korzystania z własnego węzła do przeglądania danych Blockchain i nadawania transakcji,
- i Block explorer, który zapewnia dostęp do informacji o Blockchain Bitcoin bez ujawniania danych zewnętrznej instancji, której nie kontrolujesz.



Dowiedzmy się, jak z nich korzystać.


### 8.1. Podłącz Ashigaru do swojego Dojo



Podłączenie Ashigaru Wallet do Dojo jest bardzo proste: po uruchomieniu DMT otwórz menu "*Pairing*". Pojawi się kod QR, który można zeskanować bezpośrednio za pomocą aplikacji Ashigaru.



![Image](assets/fr/38.webp)



W aplikacji Ashigaru, przy pierwszym uruchomieniu po utworzeniu lub przywróceniu Wallet, zostaniesz przekierowany na stronę "*Konfiguruj swój serwer Dojo*". Naciśnij "*Scan QR*", a następnie zeskanuj kod QR wyświetlony na DMT.



![Image](assets/fr/39.webp)



Następnie kliknij przycisk "*Kontynuuj*".



![Image](assets/fr/40.webp)



Jesteś teraz połączony ze swoim Dojo.



![Image](assets/fr/41.webp)



### 8.2. Korzystanie z Block explorer



Dojo automatycznie instaluje Block explorer, [BTC-RPC Explorer](https://github.com/janoside/btc-RPC-explorer), który czerpie bezpośrednio z danych z własnego węzła Bitcoin. Eksplorator umożliwia dostęp do nieprzetworzonych informacji z Blockchain i Mempool za pośrednictwem łatwej do zrozumienia sieci Interface. Można więc na przykład sprawdzić status oczekującej transakcji, wyświetlić saldo Address lub z łatwością zbadać skład bloku.



Aby uzyskać do niego dostęp, wystarczy pobrać Tor Address z przeglądarki. Aby to zrobić, uruchom to samo polecenie, którego użyłeś do uzyskania Address swojego DMT:



```bash
./dojo.sh onion
```



![Image](assets/fr/42.webp)



Będziesz mieć dostęp do wszystkich informacji o połączeniu Dojo za pośrednictwem Tora. Ten, który nas tutaj interesuje, to następujący adres URL:



```
Block Explorer =
```



Jeśli jesteś już połączony ze swoim DMT, możesz również znaleźć ten Address w menu "*Pairing*", wewnątrz JSON połączenia:



![Image](assets/fr/43.webp)



Aby uzyskać dostęp do przeglądarki z dowolnego komputera w dowolnej sieci (nawet zdalnie), otwórz [Tor Browser](https://www.torproject.org/download/) i wprowadź adres URL, który właśnie pobrałeś.



⚠️ **Prosimy o zachowanie tego Address w ścisłej tajemnicy



Uzyskasz wtedy dostęp do własnego Block explorer.



![Image](assets/fr/44.webp)



*Źródło zdjęcia: https://ashigaru.rs/.*



Aby śledzić transakcję, wystarczy wpisać txid w pasku wyszukiwania w prawym górnym rogu.



![Image](assets/fr/45.webp)



*Źródło zdjęcia: https://ashigaru.rs/.*



Aby sprawdzić ruchy powiązane z Address, postępuj w ten sam sposób, wpisując Address w pasku wyszukiwania.



![Image](assets/fr/46.webp)



*Źródło zdjęcia: https://ashigaru.rs/.*



Możesz także wpisać Hash lub wysokość bloku w pasku wyszukiwania, aby wyświetlić szczegóły.



![Image](assets/fr/47.webp)



*Źródło zdjęcia: https://ashigaru.rs/.*



## 9. Konserwacja Dojo



### 9.1 Zatrzymaj swoje Dojo



Nigdy nie odcinaj nagle zasilania Dojo, ponieważ może to spowodować uszkodzenie niektórych baz danych, w szczególności indeksatora Fulcrum. Jeśli musisz go wyłączyć, zawsze wykonaj czyste zamknięcie Dojo, a następnie, po zakończeniu wszystkich procedur, wyłącz również maszynę:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



### 9.2 Zaktualizuj swoje Dojo



Dojo ewoluuje regularnie, a nowe wersje są wydawane w celu naprawienia błędów, poprawy stabilności i dodania funkcji. Dlatego ważne jest [regularne sprawdzanie aktualizacji](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) i aktualizowanie Dojo. Proces ten jest podobny do początkowej instalacji, ale wymaga zastąpienia niektórych plików najnowszą dostępną wersją, przy jednoczesnym zachowaniu konfiguracji. Oto szczegółowe kroki, które należy wykonać, aby przeprowadzić czystą i bezpieczną aktualizację:



Aby sprawdzić aktualną wersję Dojo, uruchom polecenie :



```bash
./dojo.sh version
```



Chociaż ten krok jest opcjonalny, zalecam rozpoczęcie od aktualizacji systemu operacyjnego. Zmniejsza to ryzyko niezgodności i zapewnia, że zależności używane przez Dojo są aktualne:



```bash
sudo apt-get update
sudo apt-get upgrade
```



Przejdź do katalogu Dojo i zatrzymaj bieżące usługi:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Następnie uruchom ponownie system, aby uzyskać czyste konto:



```bash
sudo reboot
```



Dojo jest dostarczane z cyfrowo podpisanymi plikami. Te podpisy PGP zapewniają, że pliki pochodzą od dewelopera i nie zostały w żaden sposób zmienione. Ważne jest, aby sprawdzać je za każdym razem, gdy aktualizujesz Dojo, tak jak przy pierwszej instalacji. Zacznij od pobrania klucza publicznego dewelopera przez Tor, a następnie zaimportuj go :



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



Powrót do katalogu osobistego:



```bash
cd ~/
```



Pobierz najnowszą wersję Dojo z GitHub przez Tor. W tym przykładzie jest to wersja `1.28.0` (która jeszcze nie istnieje w momencie pisania: to tylko przykład). Pamiętaj, aby zastąpić plik i link [wersją, którą chcesz zainstalować](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases):



```bash
torsocks wget -O samourai-dojo-1.28.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.28.0.zip
```



Pobierz również plik zawierający odciski palców i podpis PGP (ponownie pamiętaj o dostosowaniu wersji w poleceniu):



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt.sig
```



Sprawdź, czy pobrany plik odcisku palca został podpisany kluczem dewelopera:



```bash
gpg --verify samourai-dojo-1.28.0-fingerprints.txt.sig
```



Prawidłowy wynik powinien zostać wyświetlony :



```
gpg: Signature made [date + time]
gpg: using EDDSA key E53AD419B242822F19E23C6D3033D463D6E544F6
gpg: Good signature from "dojocoder@pm.me" <dojocoder@pm.me> [unknown]
```



Może pojawić się ostrzeżenie, że klucz jest niecertyfikowany, ale nie ma to znaczenia. Z drugiej strony, jeśli podpis jest nieprawidłowy lub odpowiada innemu kluczowi, nie idź dalej i zacznij od nowa, sprawdzając linki.



Następnie oblicz odcisk palca SHA256 archiwum i porównaj go z oficjalnym plikiem odcisku palca:



```bash
sha256sum samourai-dojo-1.28.0.zip
cat samourai-dojo-1.28.0-fingerprints.txt
```



Jeśli oba odciski palców pasują idealnie, archiwum jest oryginalne i nienaruszone. Jeśli się różnią, natychmiast usuń pliki i nie kontynuuj.



Rozpakuj archiwum w katalogu domowym:



```bash
unzip samourai-dojo-1.28.0.zip -d .
```



Następnie skopiuj zawartość do katalogu Dojo, nadpisując stary plik :



```bash
cp -a samourai-dojo-1.28.0/. dojo-app/
```



Ta operacja zachowuje pliki konfiguracyjne znajdujące się w `~/dojo-app/docker/my-dojo/conf`, ale zastępuje wszystkie inne pliki zaktualizowanymi wersjami.



Aby utrzymać środowisko w czystości, należy usuwać niepotrzebne pliki:



```bash
rm -r samourai-dojo-1.28.0 && rm samourai-dojo-1.28.0.zip && rm samourai-dojo-1.28.0-fingerprints.txt && rm samourai-dojo-1.28.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



Wróć do katalogu skryptów Dojo i uruchom polecenie aktualizacji:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh upgrade -y
```



To polecenie instruuje Dockera, aby odbudował obrazy z nowymi plikami, a następnie automatycznie zrestartował wszystkie usługi. Pod koniec procesu sprawdź dzienniki, aby upewnić się, że Bitcoin core, Fulcrum i Dojo działają poprawnie:



```bash
./dojo.sh logs bitcoind
./dojo.sh logs fulcrum
```



Jeśli usługi uruchamiają się bez błędów, a dzienniki pokazują przetwarzane bloki, Dojo jest teraz aktualne i sprawne.