---
name: Gruszki
description: Jak zainstalować i używać aplikacji na Pears?
---

![cover](assets/cover.webp)



W tym samouczku dowiemy się, jak uruchamiać aplikacje na **Pears**, technologii peer-to-peer (P2P) opracowanej przez **Holepunch** i wspieranej przez **Tether**. Cel jest prosty: umożliwić dystrybucję i korzystanie z aplikacji internetowych bez polegania na jakiejkolwiek scentralizowanej infrastrukturze (bez serwerów, bez hostów, bez pośredników). Innymi słowy, nawet jeśli dostawca usług w chmurze zostanie zamknięty lub kraj zablokuje domenę, aplikacja będzie działać wśród użytkowników sieci.



## 1. Co to jest gruszka?



Pears to środowisko uruchomieniowe, narzędzie programistyczne i platforma wdrożeniowa dla aplikacji peer-to-peer. To narzędzie o otwartym kodzie źródłowym umożliwia tworzenie, udostępnianie i uruchamianie oprogramowania bez serwera lub infrastruktury, bezpośrednio między użytkownikami. Konkretnie oznacza to, że zamiast hostować aplikację na centralnym serwerze, każdy użytkownik staje się węzłem sieci, udostępniającym część aplikacji i danych innym użytkownikom. Cały system tworzy rozproszoną sieć, w której każda instancja współpracuje w celu utrzymania dostępności usługi.



![Image](assets/fr/01.webp)



Podejście to opiera się na zestawie modułowych cegiełek oprogramowania opracowanych przez Holepunch:




- Hypercore**: rozproszony dziennik gwarantujący spójność i bezpieczeństwo danych bez centralnej bazy danych.
- Hyperbee**: indeksator na Hypercore, zapewniający wydajną organizację i przeglądanie danych.
- Hyperdrive**: rozproszony system plików używany do przechowywania i synchronizowania plików aplikacji między urządzeniami równorzędnymi.
- Hyperswarm** i **HyperDHT**: warstwy sieciowe, które umożliwiają wykrywanie i łączenie sieci równorzędnych na całym świecie, bez centralnego serwera.
- Secretstream**: protokół szyfrowania E2E służący do zabezpieczania wymiany danych między dwoma użytkownikami.



Łącząc te komponenty, Pears umożliwia tworzenie autonomicznych, szyfrowanych i rozproszonych aplikacji, w których każdy użytkownik aktywnie uczestniczy w sieci. Ta zdecentralizowana architektura eliminuje koszty infrastruktury, ryzyko cenzury i SPOF (*Single Point of Failure*).



## 2. Geneza i filozofia projektu



Pears jest rozwijany przez Holepunch, firmę założoną przez Mathiasa Buusa i Paolo Ardoino (CEO Tether i CTO Bitfinex), z misją rozszerzenia logiki peer-to-peer poza Bitcoin. Ich ambicją jest zbudowanie "Internetu Peer-to-Peer", w którym każda aplikacja może działać bez autoryzacji, bez serwerów i bez pośredników. Holepunch stoi już za **Keet**, w pełni P2P aplikacją do wideokonferencji i przesyłania wiadomości.



*Ten samouczek instalacji Pears jest podzielony na kilka sekcji w zależności od systemu operacyjnego. Przejdź bezpośrednio do sekcji odpowiadającej Twojemu środowisku, aby postępować zgodnie z odpowiednimi instrukcjami :*




- Linux (Debian)** → Część **3**
- Windows** → Część **4**
- macOS** → Część **5**



## 3. Jak zainstalować Pears w systemie Linux (Debian)



Instalacja Pears w systemie Debian jest stosunkowo prosta, ale wymaga spełnienia kilku warunków wstępnych, które szczegółowo omówimy w tej sekcji.



### 3.1. aktualizacja systemu



Przede wszystkim należy upewnić się, że system jest aktualny.



```bash
sudo apt update && sudo apt upgrade -y
```



![Image](assets/fr/02.webp)



### 3.2. zainstalować zależności



Pears opiera się na niektórych bibliotekach systemowych, w szczególności `libatomic1`, używanej przez środowisko uruchomieniowe Bare JavaScript. Zainstaluj ją za pomocą następującego polecenia:



```bash
sudo apt install -y libatomic1 curl git
```



![Image](assets/fr/03.webp)



### 3.3. zainstalować Node.js i npm przez NVM



Pears jest dystrybuowany za pośrednictwem *npm*, menedżera pakietów *Node.js*. Chociaż działanie Pears nie zależy bezpośrednio od *Node.js*, jest on niezbędny do instalacji. Zalecaną metodą instalacji *Node.js* w systemie Linux jest *NVM* (*Node Version Manager*), który pozwala na równoległe zarządzanie kilkoma wersjami Node.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



![Image](assets/fr/04.webp)



Następnie przeładuj terminal, aby aktywować *NVM* :



```bash
source ~/.bashrc
```



![Image](assets/fr/05.webp)



Sprawdź, czy *NVM* jest zainstalowany:



```bash
nvm --version
```



![Image](assets/fr/06.webp)



Następnie zainstaluj stabilną wersję *Node.js* (np. aktualny LTS):



```bash
nvm install --lts
```



![Image](assets/fr/07.webp)



Sprawdź instalacje *Node.js* i *npm*:



```bash
node -v
npm -v
```



![Image](assets/fr/08.webp)



### 3.4 Instalacja Pears za pomocą npm



Po udostępnieniu *npm* można zainstalować Pears CLI globalnie w systemie. Pozwoli to na uruchomienie komendy `pear` z dowolnego katalogu.



```bash
npm install -g pear
```



![Image](assets/fr/09.webp)



### 3.5. Inicjalizacja gruszek



Po instalacji wystarczy uruchomić następujące polecenie w terminalu:



```bash
pear
```



Przy pierwszym uruchomieniu Pears połączy się z siecią peer-to-peer w celu pobrania niezbędnych komponentów. Proces ten nie wymaga centralnego serwera: pliki są pobierane bezpośrednio od innych użytkowników.



![Image](assets/fr/10.webp)



Po zakończeniu pobierania uruchom polecenie ponownie, aby sprawdzić, czy wszystko działa:



```bash
pear
```



![Image](assets/fr/11.webp)



Jeśli wszystko zostało poprawnie zainstalowane, zostanie wyświetlona pomoc Pears z listą dostępnych poleceń.



### 3.6. Testowanie gruszek z Keet



Aby sprawdzić, czy Pears jest w pełni operacyjny, można uruchomić aplikację P2P już dostępną w sieci, taką jak Keet, oprogramowanie open-source Holepunch do przesyłania wiadomości i wideokonferencji.



```bash
pear run pear://keet
```



Polecenie to ładuje aplikację Keet bezpośrednio z sieci Pears, bez przechodzenia przez centralny serwer. Jeśli Keet uruchomi się poprawnie, instalacja Pears jest w pełni funkcjonalna.



![Image](assets/fr/12.webp)



Twój system Linux jest teraz gotowy do uruchamiania i hostowania aplikacji peer-to-peer za pomocą Pears.



## 4. Jak zainstalować Pears w systemie Windows



Instalacja Pears w systemie Windows jest równie łatwa jak w systemie Linux, ale wymaga kilku specjalnych narzędzi.



*Jeśli korzystasz z systemu Linux, możesz przejść do kroku 6.*



### 4.1. otworzyć PowerShell w trybie administratora



Przede wszystkim należy uruchomić PowerShell z uprawnieniami administratora:




- Kliknij menu Start;
- Wpisz PowerShell ;
- Kliknij prawym przyciskiem myszy na "*Windows PowerShell*";
- Wybierz opcję "*Uruchom jako administrator*".



![Image](assets/fr/15.webp)



### 4.2. pobierz NVS



Pears jest instalowany przez *npm*, menedżera pakietów *Node.js*. W systemie Windows metodą zalecaną przez Holepunch jest użycie *NVS* (*Node Version Switcher*), który jest bardziej stabilny niż *NVM* w tym systemie.



W PowerShell uruchom następujące polecenie, aby zainstalować najnowszą wersję *NVS* :



```PowerShell
winget install jasongin.nvs
```



![Image](assets/fr/16.webp)



### 4.3. zainstalować Node.js



Po instalacji uruchom ponownie PowerShell i wprowadź następujące polecenie:



```powershell
nvs
```



Powinieneś zobaczyć listę dostępnych wersji *Node.js*. Wybierz pierwszą z nich, naciskając klawisz `a` na klawiaturze.



![Image](assets/fr/17.webp)



*Node.js* jest zainstalowany.



![Image](assets/fr/18.webp)



### 4.4. Sprawdzić instalacje



Upewnij się, że *Node.js* i *npm* są dostępne:



```powershell
node -v
npm -v
```



Oba polecenia muszą zwracać numer wersji.



![Image](assets/fr/19.webp)



### 4.5. Instalacja Pears za pomocą npm



Gdy *Node.js* i *npm* będą dostępne, zainstaluj **Pears CLI** globalnie w swoim systemie:



```powershell
npm install -g pear
```



Spowoduje to zainstalowanie pliku binarnego `pear` w globalnym katalogu *npm*.



![Image](assets/fr/20.webp)



### 4.6. Sprawdź i zainicjuj Pears



Po zakończeniu instalacji uruchom :



```powershell
pear
```



Przy pierwszym uruchomieniu Pears automatycznie pobierze niezbędne komponenty z sieci peer-to-peer. Proces ten może potrwać kilka chwil.



![Image](assets/fr/21.webp)



Jeśli wszystko poszło dobrze, powinieneś zobaczyć ekran pomocy CLI Pears z listą dostępnych poleceń podrzędnych (run, seed, info...).



### 4.7. Testowanie gruszek z Keet



Aby sprawdzić, czy Pears jest w pełni operacyjny, można uruchomić aplikację P2P już dostępną w sieci, taką jak Keet, oprogramowanie open-source Holepunch do przesyłania wiadomości i wideokonferencji.



```bash
pear run pear://keet
```



Polecenie to ładuje aplikację Keet bezpośrednio z sieci Pears, bez przechodzenia przez centralny serwer. Jeśli Keet uruchomi się poprawnie, instalacja Pears jest w pełni funkcjonalna.



![Image](assets/fr/22.webp)



System Windows jest teraz gotowy do uruchamiania i hostowania aplikacji peer-to-peer za pomocą Pears.



## 5. Jak zainstalować Pears na macOS?



Instalacja Pears na macOS jest podobna do instalacji na Linuksie, ale wymaga kilku dostosowań specyficznych dla środowiska Apple. Odkryjmy te kroki razem.



*Jeśli korzystasz z systemu Linux lub Windows i zainstalowałeś już Pears, możesz przejść bezpośrednio do **kroku 6**



### 5.1. Sprawdź wymagania systemowe



Przed instalacją należy upewnić się, że *Xcode Command Line Tools* jest obecne w systemie. Pakiet ten zapewnia niezbędne narzędzia do kompilacji _Node.js_ i jego zależności.



Aby to zrobić, otwórz terminal za pomocą skrótu klawiaturowego `Cmd + spacja`, a następnie wpisz `Terminal` i naciśnij klawisz `Enter`. Następnie możesz wpisać to polecenie w terminalu, aby uruchomić instalację:



```bash
xcode-select --install
```



Jeśli narzędzia są już zainstalowane w systemie, macOS poinformuje o tym użytkownika.



### 5.2. zainstalować NVM



Pears jest dystrybuowany za pośrednictwem *npm*, menedżera pakietów *Node.js*. Choć działanie Pears nie zależy bezpośrednio od *Node.js*, jest on niezbędny do instalacji. Zalecaną metodą instalacji *Node.js* na macOS jest *NVM* (*Node Version Manager*), który pozwala na równoległe zarządzanie kilkoma wersjami Node.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



Następnie przeładuj terminal, aby aktywować *NVM* :



```bash
source ~/.zshrc
```



Jeśli używasz *bash* zamiast *zsh*, uruchom :



```bash
source ~/.bashrc
```



Następnie sprawdź, czy *NVM* jest zainstalowany:



```bash
nvm --version
```



Terminal powinien zwrócić wersję *NVM* zainstalowaną w systemie.



### 5.3. zainstalować Node.js i npm



Następnie zainstaluj stabilną wersję *Node.js* (np. aktualny LTS):



```bash
nvm install --lts
```



Po zakończeniu instalacji sprawdź zainstalowane wersje:



```bash
node -v
npm -v
```



Oba polecenia muszą zwracać numer wersji.



### 5.4 Instalacja Pears za pomocą npm



Gdy *npm* jest dostępny, można zainstalować Pears CLI globalnie w systemie. Pozwoli to na uruchomienie polecenia `pear` z dowolnego katalogu.



```bash
npm install -g pear
```



### 5.5. Inicjalizacja gruszek



Po instalacji wystarczy uruchomić następujące polecenie w terminalu:



```bash
pear
```



Przy pierwszym uruchomieniu Pears połączy się z siecią peer-to-peer w celu pobrania niezbędnych komponentów. Proces ten nie wymaga centralnego serwera: pliki są pobierane bezpośrednio od innych użytkowników.



Po zakończeniu pobierania uruchom polecenie ponownie, aby sprawdzić, czy wszystko działa:



```bash
pear
```



Jeśli wszystko zostało poprawnie zainstalowane, zostanie wyświetlona pomoc Pears z listą dostępnych poleceń.



### 5.6. Testowanie gruszek z Keet



Aby sprawdzić, czy Pears jest w pełni operacyjny, można uruchomić aplikację P2P już dostępną w sieci, taką jak Keet, oprogramowanie open-source Holepunch do przesyłania wiadomości i wideokonferencji.



```bash
pear run pear://keet
```



Polecenie to ładuje aplikację Keet bezpośrednio z sieci Pears, bez przechodzenia przez centralny serwer. Jeśli Keet uruchomi się poprawnie, instalacja Pears jest w pełni funkcjonalna.



System macOS jest teraz gotowy do uruchamiania i hostowania aplikacji peer-to-peer za pomocą Pears.



## 6. Jak korzystać z aplikacji na Pears?



Po uruchomieniu Pears można bezpośrednio uruchomić wybraną aplikację za pomocą następującego polecenia:



```bash
pear run pear://[KEY]
```



Wystarczy zastąpić `[KEY]` kluczem aplikacji, którego chcesz użyć.



![Image](assets/fr/13.webp)



Aby dowiedzieć się, jak uruchomić naszą platformę Plan ₿ Academy na Pears, zapoznaj się z tym obszernym samouczkiem:



https://planb.academy/tutorials/contribution/others/pears-plan-b-academy-77f0ae28-28fc-4465-a9f1-1c6654711770

Aby dowiedzieć się, jak korzystać z aplikacji do przesyłania wiadomości Keet, którą właśnie uruchomiłeś na Pears, zapoznaj się z tym samouczkiem :



https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b