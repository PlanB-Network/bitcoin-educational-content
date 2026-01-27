---
name: Plan ₿ Academy - Pears App
description: Jak zainstalować i korzystać z aplikacji Plan ₿ Academy na Pears?
---

![cover](assets/cover.webp)


Prawdopodobnie wiesz już, że Plan ₿ Academy to największa edukacyjna baza danych poświęcona Bitcoin, gromadząca kursy, samouczki i tysiące zasobów open source. Pierwotnie Plan ₿ Academy była stroną internetową. Ale co by się stało, gdybyś nie mógł już uzyskać do niej normalnego dostępu, na przykład w przypadku cenzury?


W tym samouczku dowiemy się, jak uruchomić platformę **Plan ₿ Academy** w sposób prawdziwie odporny na cenzurę przy użyciu **Pears**, technologii peer-to-peer (P2P) opracowanej przez **Holepunch** i wspieranej przez **Tether**.


Pears to oprogramowanie, które pozwala nam uruchomić platformę Plan ₿ Academy bez polegania na scentralizowanej stronie internetowej. W tym samouczku zainstalujemy Pears na komputerze, aby uzyskać dostęp do Plan ₿ Academy za pośrednictwem Pears.


Cel Pears jest prosty: umożliwić dystrybucję i korzystanie z aplikacji internetowych bez zależności od jakiejkolwiek scentralizowanej infrastruktury (bez serwerów, bez hostów, bez pośredników). Innymi słowy, nawet jeśli dostawca chmury zostanie zamknięty lub kraj zablokuje domenę, aplikacja nadal będzie działać wśród użytkowników sieci. Takie podejście pozwala naszej platformie edukacyjnej, Plan ₿ Academy, pozostać dostępną na całym świecie, bez pojedynczego punktu awarii.


---

**TL;DR:**



- Zainstaluj gruszki;



- Uruchom następujące polecenie, aby uruchomić aplikację Plan ₿ Academy:


```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


---

## 1. Co to jest gruszka?


Pears jest jednocześnie środowiskiem uruchomieniowym, narzędziem programistycznym i platformą wdrożeniową dla aplikacji peer-to-peer. To narzędzie o otwartym kodzie źródłowym umożliwia tworzenie, udostępnianie i uruchamianie oprogramowania bez serwerów lub infrastruktury, bezpośrednio między użytkownikami. W praktyce oznacza to, że zamiast hostować aplikację na centralnym serwerze, każdy użytkownik staje się węzłem w sieci: udostępnia część aplikacji i danych innym użytkownikom. Cały system tworzy rozproszoną sieć, w której każda instancja współpracuje w celu utrzymania dostępności usługi.


![Image](assets/fr/01.webp)


Podejście to opiera się na zestawie modułowych komponentów oprogramowania opracowanych przez Holepunch:



- Hypercore**: rozproszony dziennik, który zapewnia spójność i bezpieczeństwo danych bez centralnej bazy danych.
- Hyperbee**: indeks zbudowany w oparciu o Hypercore, który pozwala na efektywne organizowanie i wyszukiwanie danych.
- Hyperdrive**: rozproszony system plików używany do przechowywania i synchronizowania plików aplikacji między urządzeniami równorzędnymi.
- Hyperswarm** i **HyperDHT**: warstwy sieciowe, które umożliwiają wykrywanie peerów i połączenia na całym świecie bez centralnego serwera.
- Secretstream**: kompleksowy protokół szyfrowania, który zabezpiecza komunikację między użytkownikami.


Łącząc te komponenty, Pears umożliwia tworzenie autonomicznych, szyfrowanych i rozproszonych aplikacji, w których każdy użytkownik aktywnie uczestniczy w sieci. Ta zdecentralizowana architektura eliminuje koszty infrastruktury, ryzyko cenzury i SPOF (*pojedyncze punkty awarii*).


Pears jest rozwijany przez Holepunch, firmę założoną przez Mathiasa Buusa i Paolo Ardoino (CEO Tether i CTO Bitfinex), z misją rozszerzenia logiki peer-to-peer poza Bitcoin. Ich ambicją jest zbudowanie "*Internetu peerów*", w którym każda aplikacja może działać bez pozwolenia, bez serwerów i bez pośredników. Holepunch stoi już za **Keet**, w pełni P2P aplikacją do wideokonferencji i przesyłania wiadomości.


https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*Ten samouczek instalacji Pears jest podzielony na wiele sekcji w zależności od systemu operacyjnego. Przejdź bezpośrednio do sekcji odpowiadającej Twojemu środowisku, aby postępować zgodnie z odpowiednimi instrukcjami:*



- Linux (Debian)** → Sekcja **2**
- Windows** → Sekcja **3**
- macOS** → Sekcja **4**


## 2. Jak zainstalować Pears na Linux (Debian)?


Instalacja Pears na Debianie jest stosunkowo prosta, ale wymaga spełnienia kilku warunków wstępnych, które szczegółowo omówimy w tej sekcji.


### 2.1. Aktualizacja systemu


Przed wszystkim należy upewnić się, że system jest aktualny.


```bash
sudo apt update && sudo apt upgrade -y
```


![Image](assets/fr/02.webp)


### 2.2. Zainstaluj zależności


Pears opiera się na niektórych bibliotekach systemowych, w tym `libatomic1`, używanej przez silnik wykonawczy Bare JavaScript. Zainstaluj ją za pomocą następującego polecenia:


```bash
sudo apt install -y libatomic1 curl git
```


![Image](assets/fr/03.webp)


### 2.3. Instalacja Node.js i npm przez NVM


Pears jest dystrybuowany za pośrednictwem *npm*, menedżera pakietów *Node.js*. Chociaż Pears nie jest bezpośrednio zależny od *Node.js* do działania, jest on wymagany do instalacji. Zalecanym sposobem instalacji *Node.js* w systemie Linux jest *NVM* (*Node Version Manager*), który pozwala na zarządzanie wieloma wersjami Node obok siebie.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


![Image](assets/fr/04.webp)


Następnie przeładuj terminal, aby aktywować *NVM*:


```bash
source ~/.bashrc
```


![Image](assets/fr/05.webp)


Sprawdź, czy *NVM* jest prawidłowo zainstalowany:


```bash
nvm --version
```


![Image](assets/fr/06.webp)


Następnie zainstaluj stabilną wersję *Node.js* (na przykład aktualną wersję LTS):


```bash
nvm install --lts
```


![Image](assets/fr/07.webp)


Sprawdź, czy *Node.js* i *npm* są poprawnie zainstalowane:


```bash
node -v
npm -v
```


![Image](assets/fr/08.webp)


### 2.4. Zainstaluj Pears za pomocą npm


Gdy *npm* jest dostępny, można globalnie zainstalować Pears CLI w systemie. Pozwala to na uruchomienie polecenia `pear` z dowolnego katalogu.


```bash
npm install -g pear
```


![Image](assets/fr/09.webp)


### 2.5. Inicjalizacja gruszek


Po instalacji wystarczy uruchomić następujące polecenie w terminalu:


```bash
pear
```


Przy pierwszym uruchomieniu Pears połączy się z siecią peer-to-peer w celu pobrania niezbędnych komponentów. Proces ten nie opiera się na żadnym centralnym serwerze - pliki są pobierane bezpośrednio od innych użytkowników.


![Image](assets/fr/10.webp)


Po zakończeniu pobierania uruchom polecenie ponownie, aby potwierdzić, że wszystko działa:


```bash
pear
```


![Image](assets/fr/11.webp)


Jeśli wszystko zostało poprawnie zainstalowane, pojawi się menu pomocy Pears z listą dostępnych poleceń.


### 2.6. Gruszki testowe z Keet


Aby sprawdzić, czy Pears jest w pełni operacyjny, można uruchomić istniejącą aplikację P2P dostępną w sieci, taką jak Keet, oprogramowanie open-source do przesyłania wiadomości i wideokonferencji opracowane przez Holepunch.


```bash
pear run pear://keet
```


Polecenie to ładuje aplikację Keet bezpośrednio z sieci Pears, bez użycia centralnego serwera. Jeśli Keet uruchomi się poprawnie, oznacza to, że instalacja Pears jest w pełni funkcjonalna.


![Image](assets/fr/12.webp)


Twój system Linux jest teraz gotowy do uruchamiania i hostowania aplikacji peer-to-peer za pomocą Pears.


## 3. Jak zainstalować Pears w systemie Windows


Instalacja Pears w systemie Windows jest równie prosta jak w systemie Linux, ale wymaga kilku specjalnych narzędzi.


*Jeśli korzystasz z systemu Linux i zainstalowałeś już Pears, możesz przejść bezpośrednio do **Kroku 5**


### 3.1. Otwórz PowerShell jako administrator


Najpierw uruchom PowerShell z uprawnieniami administratora:



- Kliknij menu Start;
- Wpisz "PowerShell";
- Kliknij prawym przyciskiem myszy na "*Windows PowerShell*";
- Wybierz opcję "*Uruchom jako administrator*".


![Image](assets/fr/15.webp)


### 3.2. Pobierz NVS


Pears jest instalowany przez *npm*, menedżera pakietów *Node.js*. W systemie Windows metodą zalecaną przez Holepunch jest użycie *NVS* (*Node Version Switcher*), który jest bardziej stabilny niż *NVM* w tym systemie.


W PowerShell uruchom następujące polecenie, aby zainstalować najnowszą wersję *NVS*:


```PowerShell
winget install jasongin.nvs
```


![Image](assets/fr/16.webp)


### 3.3. Zainstaluj Node.js


Po instalacji uruchom ponownie PowerShell, a następnie wprowadź następujące polecenie:


```powershell
nvs
```


Powinieneś zobaczyć listę dostępnych wersji *Node.js*. Wybierz pierwszą z nich, naciskając klawisz `a` na klawiaturze.


![Image](assets/fr/17.webp)


*Node.js* jest teraz zainstalowany.


![Image](assets/fr/18.webp)


### 3.4. Weryfikacja instalacji


Upewnij się, że *Node.js* i *npm* są dostępne:


```powershell
node -v
npm -v
```


Oba polecenia powinny zwrócić numer wersji.


![Image](assets/fr/19.webp)


### 3.5. Zainstaluj Pears za pomocą npm


Gdy *Node.js* i *npm* będą dostępne, zainstaluj **Pears CLI** globalnie w swoim systemie:


```powershell
npm install -g pear
```


Instaluje to plik binarny `pear` w globalnym katalogu *npm*.


![Image](assets/fr/20.webp)


### 3.6. Weryfikacja i inicjalizacja Pears


Po zakończeniu instalacji uruchom aplikację:


```powershell
pear
```


Przy pierwszym uruchomieniu Pears automatycznie pobierze wymagane komponenty z sieci peer-to-peer. Proces ten może potrwać kilka chwil.


![Image](assets/fr/21.webp)


Jeśli wszystko poszło dobrze, powinieneś zobaczyć menu pomocy Pears CLI z listą dostępnych podpoleceń (run, seed, info...).


### 3.7. Gruszki testowe z Keet


Aby sprawdzić, czy Pears jest w pełni operacyjny, można uruchomić istniejącą aplikację P2P dostępną w sieci, taką jak Keet - oprogramowanie open-source do przesyłania wiadomości i wideokonferencji opracowane przez Holepunch.


```bash
pear run pear://keet
```


Polecenie to ładuje aplikację Keet bezpośrednio z sieci Pears, bez użycia centralnego serwera. Jeśli Keet uruchomi się pomyślnie, oznacza to, że instalacja Pears jest w pełni funkcjonalna.


![Image](assets/fr/22.webp)


System Windows jest teraz gotowy do uruchamiania i hostowania aplikacji peer-to-peer za pomocą Pears.


## 4. Jak zainstalować Pears na macOS


Instalacja Pears w systemie macOS jest podobna do instalacji w systemie Linux, ale wymaga kilku dostosowań specyficznych dla środowiska Apple. Przejdźmy przez te kroki razem.


*Jeśli korzystasz z systemu Linux lub Windows i zainstalowałeś już Pears, możesz przejść bezpośrednio do **Kroku 5**


### 4.1. Sprawdź wymagania wstępne systemu


Przed instalacją należy upewnić się, że w systemie zainstalowano *Xcode Command Line Tools*. Pakiet ten zapewnia niezbędne narzędzia kompilacji dla *Node.js* i jego zależności.


Aby to zrobić, otwórz terminal za pomocą skrótu klawiszowego `Cmd + spacja`, wpisz `Terminal` i naciśnij `Enter`. Następnie uruchom następujące polecenie w terminalu, aby je zainstalować:


```bash
xcode-select --install
```


Jeśli narzędzia są już zainstalowane w systemie, macOS powiadomi o tym użytkownika.


### 4.2. Zainstalować NVM


Pears jest dystrybuowany za pośrednictwem *npm*, menedżera pakietów *Node.js*. Choć działanie Pears nie zależy bezpośrednio od *Node.js*, jest on wymagany do instalacji. Zalecaną metodą instalacji *Node.js* na macOS jest *NVM* (*Node Version Manager*), który pozwala na zarządzanie wieloma wersjami Node jednocześnie.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


Następnie przeładuj terminal, aby aktywować *NVM*:


```bash
source ~/.zshrc
```


Jeśli używasz *bash* zamiast *zsh*, uruchom:


```bash
source ~/.bashrc
```


Następnie sprawdź, czy *NVM* jest poprawnie zainstalowany:


```bash
nvm --version
```


Terminal powinien wyświetlić zainstalowaną wersję *NVM*.


### 4.3. Zainstaluj Node.js i npm


Następnie zainstaluj stabilną wersję *Node.js* (na przykład aktualną wersję LTS):


```bash
nvm install --lts
```


Po zakończeniu instalacji sprawdź zainstalowane wersje:


```bash
node -v
npm -v
```


Oba polecenia powinny zwrócić numer wersji.


### 4.4. Zainstaluj Pears za pomocą npm


Gdy *npm* jest dostępny, można globalnie zainstalować Pears CLI w systemie. Pozwoli to na wykonanie polecenia `pear` z dowolnego katalogu.


```bash
npm install -g pear
```


### 4.5. Inicjalizacja gruszek


Po instalacji wystarczy uruchomić następujące polecenie w terminalu:


```bash
pear
```


Przy pierwszym uruchomieniu Pears łączy się z siecią peer-to-peer w celu pobrania niezbędnych komponentów. Proces ten nie wymaga żadnego centralnego serwera - pliki są pobierane bezpośrednio od innych użytkowników.


Po zakończeniu pobierania ponownie uruchom polecenie, aby sprawdzić, czy wszystko działa:


```bash
pear
```


Jeśli wszystko zostało poprawnie zainstalowane, pojawi się menu pomocy Pears z listą dostępnych poleceń.


### 4.6. Gruszki testowe z Keet


Aby sprawdzić, czy Pears jest w pełni operacyjny, można uruchomić aplikację P2P już dostępną w sieci, taką jak Keet, oprogramowanie open-source do przesyłania wiadomości i wideokonferencji firmy Holepunch.


```bash
pear run pear://keet
```


Polecenie to ładuje aplikację Keet bezpośrednio z sieci Pears, bez użycia centralnego serwera. Jeśli Keet uruchomi się pomyślnie, oznacza to, że instalacja Pears jest w pełni funkcjonalna.


System macOS jest teraz gotowy do uruchamiania i hostowania aplikacji peer-to-peer za pomocą Pears.


## 5. Jak korzystać z Plan ₿ Academy na gruszkach


Po zainstalowaniu i uruchomieniu Pears można bezpośrednio uruchomić platformę **Plan ₿ Academy** za pośrednictwem sieci P2P. Wystarczy uruchomić następujące polecenie w terminalu (to samo polecenie działa w systemach Linux, Windows i macOS):


```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


![Image](assets/fr/13.webp)


Po zakończeniu ładowania, Plan ₿ Academy otworzy się w środowisku Pears, gotowa do użycia tak jak oryginalna strona internetowa - ale bez żadnej zależności od centralnego serwera.


![Image](assets/fr/14.webp)


## 6. Jak planować nasiona ₿ Akademia na gruszkach


W sieci Pears *seed* aplikacji oznacza jej redystrybucję do innych użytkowników z własnego komputera. W praktyce, gdy użytkownik korzysta z seed Plan ₿ Academy, jego komputer staje się źródłem danych, które umożliwia innym użytkownikom pobieranie aplikacji bez konieczności polegania na centralnym serwerze.


Mechanizm ten wzmacnia odporność naszej aplikacji na cenzurę w sieci Pears. Im więcej peerów seed aplikacji, tym bardziej staje się ona dostępna i zdecentralizowana, nawet jeśli niektóre oryginalne węzły przejdą w tryb offline.


Aby pomóc w dystrybucji Plan ₿ Academy, wystarczy uruchomić następujące polecenie:


```bash
pear seed pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


Dopóki to polecenie pozostaje aktywne, urządzenie będzie uczestniczyć w dystrybucji plików aplikacji. Zamknięcie terminala spowoduje zatrzymanie procesu udostępniania.


Aby kontynuować rozsiewanie po ponownym uruchomieniu, można uruchomić polecenie w tle lub utworzyć usługę systemową - na przykład usługę systemd w systemie Linux, LaunchAgent w systemie macOS lub zaplanowane zadanie w systemie Windows. Metody te zapewniają, że aplikacja Plan ₿ Academy automatycznie wznawia seedowanie przy starcie systemu.


Dziękujemy za przyczynienie się do zdecentralizowanej dystrybucji Plan ₿ Academy na Pears i pomoc w uczynieniu edukacji Bitcoin naprawdę odporną na cenzurę!