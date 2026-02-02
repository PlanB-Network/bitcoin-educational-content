---
name: Pop!_OS
description: Przewodnik instalacji Pop!_OS, dystrybucji systemu Linux
---

![cover](assets/cover.webp)



## Wprowadzenie



Pop!OS to oparty na Linuksie system operacyjny opracowany przez **System76**, amerykańskiego producenta specjalizującego się w maszynach dla programistów, projektantów i zaawansowanych użytkowników.



Zaprojektowany, aby oferować nowoczesne, stabilne i wydajne środowisko, Pop!OS wyróżnia się prostotą obsługi, potężnymi narzędziami i silnym naciskiem na produktywność.



### Kim jest System76?



System76 to amerykańska firma założona w 2005 roku z siedzibą w Denver, specjalizująca się w produkcji notebooków, komputerów stacjonarnych i serwerów zaprojektowanych specjalnie dla systemu Linux.



W przeciwieństwie do tradycyjnych producentów, System76 opracowuje maszyny zaprojektowane tak, aby były otwarte, naprawialne i zorientowane na wolność oprogramowania.



System76 nie tylko produkuje komputery.



Firma opracowuje również :




- Pop!OS**, własny system operacyjny oparty na Linuksie;
- COSMIC**, nowoczesne, wysokowydajne środowisko graficzne używane przez Pop!OS ;
- Open Firmware**, oprogramowanie firmware o otwartym kodzie źródłowym oparte na Coreboot ;
- narzędzia dla programistów i projektantów.



Celem jest zaoferowanie wysokiej jakości integracji sprzętu i oprogramowania, porównywalnej z ekosystemem Apple, ale całkowicie otwartej i skoncentrowanej na Linuksie.



## Nowoczesny, stabilny i dostępny system



Pop!OS opiera się na fundamentach Ubuntu, zapewniając mu doskonałą stabilność, szeroką kompatybilność sprzętową i dostęp do ogromnego ekosystemu oprogramowania.


Zapewnia elegancki interfejs, pulpit COSMIC, zaprojektowany tak, aby był płynny, intuicyjny i konfigurowalny, nawet dla nowych użytkowników.



## Idealny wybór dla programistów, projektantów i wymagających użytkowników



Pop!OS jest szczególnie ceniony przez :





- deweloperzy (preinstalowane narzędzia, zaawansowane zarządzanie kafelkami),
- użytkownicy z kartami graficznymi Nvidia lub AMD,
- studentów i profesjonalistów poszukujących niezawodnego systemu,
- użytkownicy systemu Windows, którzy chcą dokonać prostego przejścia.



Obejmuje automatyczne układanie płytek, przejrzyste centrum oprogramowania i zintegrowane narzędzia zwiększające produktywność, które ułatwiają codzienne użytkowanie.



## Najważniejsze cechy Pop!OS





- Zoptymalizowana wydajność** dzięki regularnym aktualizacjom.
- Dostępne są dwie wersje ISO**: standardowa i zoptymalizowana pod kątem Nvidii.
- Zwiększone bezpieczeństwo** (szyfrowanie LUKS dostępne podczas instalacji).
- Interface COSMIC** ergonomiczny i nowoczesny.
- Wysoka kompatybilność** z oprogramowaniem Ubuntu i Flatpak.



## Pobierz bezpiecznie POP!OS



### 1. Wymagania wstępne



Przed pobraniem i zainstalowaniem POP!OS należy wykonać kilka czynności, aby prawidłowo przygotować środowisko instalacyjne.



### Wymagany sprzęt





- Kompatybilny komputer**: Procesor Intel lub AMD, Karta graficzna Intel / AMD / Nvidia.
- Co najmniej 4 GB pamięci RAM** (zalecane 8 GB dla wygodnego użytkowania).
- minimum 20 GB wolnego miejsca** (zalecane 40 GB lub więcej).
- Klucz USB o pojemności co najmniej 4 GB** do utworzenia nośnika instalacyjnego.



### Połączenie z Internetem



Stabilne połączenie jest przydatne dla :





- pobrać obraz ISO,
- zainstalować aktualizacje po instalacji.



Pop!OS może działać bez połączenia, ale instalacja przebiega znacznie sprawniej przez Internet.



### Kopia zapasowa danych



Jeśli Pop!OS ma zastąpić lub współistnieć z innym systemem (Windows, Ubuntu itp.), zaleca się wykonanie kopii zapasowej ważnych plików przed kontynuowaniem.



### Sprawdź obecność procesora graficznego Nvidia (jeśli dotyczy)



W przypadku komputerów wyposażonych w kartę graficzną Nvidia należy pobrać specjalny obraz ISO zawierający sterowniki Nvidia.


To sprawdzenie jest bardzo proste:





- poprzez sprawdzenie specyfikacji komputera,
- lub sprawdzając model karty graficznej w ustawieniach systemu.



### Pobierz z oficjalnej strony internetowej



Obraz ISO Pop!OS należy pobrać bezpośrednio z oficjalnej strony System76: [system76.com/pop](https://system76.com/pop/).



Ta strona zawsze oferuje najnowszą wersję, dostosowaną do posiadanego sprzętu.



![capture](assets/fr/03.webp)



### Wybierz wersję: Standard lub Nvidia, lub Raspberry Pi (ARM64)



Pop!OS jest dostępny w trzech wariantach:



### Wersja standardowa



Zalecane dla komputerów korzystających z :





- procesor Intel lub AMD;
- zintegrowany procesor graficzny Intel lub AMD;
- karta graficzna AMD Radeon.



![Utilisation de Balena Etcher](assets/fr/04.webp)



### Wersja Nvidia



Zalecane dla komputerów wyposażonych w karty graficzne Nvidia.


Ten obraz zawiera już sterowniki Nvidia, co ułatwia instalację i zmniejsza problemy z grafiką.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### Wersja Raspberry Pi (ARM64)



Dla Raspberry Pi 4 i 400 (procesor ARM).


Dostosowana do architektury ARM, jest to specjalna wersja dla tych minikomputerów.



![Utilisation de Balena Etcher](assets/fr/06.webp)



## Utwórz bootowalny klucz USB



Możesz użyć kilku narzędzi, takich jak Balena Etcher :





- Pobierz i zainstaluj [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/07.webp)



![Installation de Balena Etcher](assets/fr/08.webp)





- Otwórz program Balena Etcher, a następnie wybierz obraz Pop!OS ISO.
- Wybierz klucz USB jako nośnik docelowy.
- Kliknij Flash i poczekaj na zakończenie procesu.



![Utilisation de Balena Etcher](assets/fr/09.webp)



## Instalowanie i zabezpieczanie Pop!OS



### Uruchamianie z klucza USB





- Wyłącz komputer.
- Podłącz klucz USB (zawierający Pop!OS).
- Włącz komputer. Na najnowszych komputerach system powinien automatycznie rozpoznać klucz rozruchowy USB. Jeśli tak się nie stanie, uruchom ponownie komputer, przytrzymując klawisz dostępu do BIOS/UEFI (zwykle F2, F12 lub Delete, w zależności od marki).
  - W menu BIOS/UEFI wybierz klucz USB jako urządzenie rozruchowe.
  - Zapisz i uruchom ponownie.



### Uruchamianie instalacji



Po wybraniu rozruchowego klucza USB jako urządzenia startowego, komputer uruchomi się w środowisku Pop!OS Live.



Wybierz język.



![Capture](assets/fr/10.webp)



Wybierz lokalizację.



![Capture](assets/fr/11.webp)



Wybór języka wprowadzania danych z klawiatury.



![Capture](assets/fr/12.webp)



Wybierz układ klawiatury.



![Capture](assets/fr/13.webp)



Wybierz opcję `Clean Install` dla standardowej instalacji. Jest to najlepsza opcja dla nowych użytkowników Linuksa, ale należy pamiętać, że spowoduje ona usunięcie całej zawartości dysku docelowego. Alternatywnie możesz wybrać opcję `Try Demo Mode`, aby kontynuować testowanie Pop!OS w środowisku rzeczywistym.



![Capture](assets/fr/14.webp)



Wybierz `Custom (Advanced)`, aby uzyskać dostęp do GParted. To narzędzie pozwala skonfigurować zaawansowane funkcje, takie jak podwójne uruchamianie, tworzenie oddzielnej partycji `/home` lub umieszczanie partycji `/tmp` na innym dysku.



Kliknij `Erase and Install`, aby zainstalować Pop!OS na wybranym dysku.



![Capture](assets/fr/15.webp)



### Konfiguracja konta użytkownika



Następna sekcja programu instalacyjnego poprowadzi Cię przez proces tworzenia konta użytkownika, abyś mógł zalogować się do nowego systemu operacyjnego.



Podaj pełną nazwę (może zawierać dowolny tekst, duże lub małe litery), a także nazwę użytkownika (która musi być pisana małymi literami):



![Capture](assets/fr/16.webp)



Po utworzeniu konta zostanie wyświetlony monit o ustawienie nowego hasła.



![Capture](assets/fr/17.webp)



### Pełne szyfrowanie dysku



Szyfrowanie dysku systemowego nie jest konieczne, ale gwarantuje bezpieczeństwo danych użytkownika w przypadku, gdy ktoś uzyska nieautoryzowany fizyczny dostęp do urządzenia.



Dysk można zaszyfrować przy użyciu hasła logowania, zaznaczając opcję `Hasło szyfrowania jest takie samo jak hasło konta użytkownika`. Możesz również odznaczyć to pole i wybrać `Ustaw hasło` na dole. Wybierz `Nie szyfruj`, aby zignorować proces szyfrowania dysku.



![Capture](assets/fr/18.webp)



Jeśli wybrałeś przycisk `Ustaw hasło`, zobaczysz dodatkowy monit o ustawienie hasła szyfrowania.



Przejdź do następnego kroku programu instalacyjnego. Pop!OS rozpocznie teraz instalację na dysku.



![Capture](assets/fr/19.webp)



Po zakończeniu instalacji uruchom ponownie komputer i zaloguj się, aby zakończyć proces konfiguracji konta użytkownika.



Jeśli kolejność rozruchu została zmieniona w celu nadania priorytetu kluczowi Live USB podczas uruchamiania, wyłącz całkowicie komputer i odłącz instalacyjny klucz USB. Jeśli pracujesz w trybie podwójnego rozruchu, naciśnij odpowiednie klawisze, aby uzyskać dostęp do konfiguracji i wybrać dysk zawierający instalację Pop!OS.



![Capture](assets/fr/20.webp)



### NVIDIA Graphics



Jeśli dokonałeś instalacji z Intel/AMD ISO i twój system posiada dyskretną kartę graficzną NVIDIA lub jeśli dodałeś ją w późniejszym terminie, będziesz musiał ręcznie zainstalować sterowniki dla swojej karty, aby osiągnąć optymalną wydajność. Uruchom następujące polecenie w terminalu poleceń, aby zainstalować sterownik:



```bash
sudo apt install system76-driver-nvidia
```



Możesz również zainstalować sterowniki graficzne NVIDIA z Pop!_Shop.



![Capture](assets/fr/20.webp)



## Instalacja niezbędnych narzędzi



Pop!OS oferuje szeroką gamę oprogramowania za pośrednictwem Pop!Shop, ale wiele niezbędnych narzędzi można również zainstalować za pośrednictwem terminala za pomocą `apt` lub `flatpak`. Oto jak zainstalować kluczowe narzędzia dla kompletnego środowiska pracy.



### Instalacja terminala




| Narzędzie | Opis | Polecenie instalacji |
| ---------------------------- | ------------------------------------------ | ----------------------------------------------- |
| Firefox | Wolna i popularna przeglądarka internetowa | `sudo apt install firefox` |
| Brave | Przeglądarka skupiona na prywatności | Instalacja przez Pop!_Shop lub oficjalną stronę |
| Visual Studio Code (VS Code) | Potężny edytor kodu dla programistów | `flatpak install flathub com.visualstudio.code` |
| Git | Menedżer wersji | `sudo apt install git` |
| Flatpak | Alternatywny menedżer pakietów | `sudo apt install flatpak` |
| VLC | Wszechstronny odtwarzacz multimedialny | `sudo apt install vlc` |
| GNOME Terminal | Domyślny terminal | Preinstalowany w Pop!OS |
| Curl | Narzędzie do transferu danych online | `sudo apt install curl` |
| Wget | Pobieranie plików przez HTTP/FTP | `sudo apt install wget` |
| Docker | Konteneryzacja aplikacji | Instalacja przez oficjalny skrypt lub `apt` |
| Node.js | Środowisko JavaScript po stronie serwera | Instalacja przez `apt` lub NodeSource |
| Python3 | Język programowania | `sudo apt install python3 python3-pip` |
| GIMP | Zaawansowany edytor obrazów | `sudo apt install gimp` |
| Thunderbird | Klient poczty e-mail | `sudo apt install thunderbird` |
| Transmission | Lekki klient BitTorrent | `sudo apt install transmission-gtk` |
| Htop | Interaktywny monitor systemu | `sudo apt install htop` |

### Instalacja za pośrednictwem Pop! Shop (interfejs graficzny)





- Otwórz **Pop!_Shop** z menu głównego.
- Użyj paska wyszukiwania, aby znaleźć żądane aplikacje (na przykład "Brave").
- Kliknij **Install** dla każdej aplikacji.
- Pop!_Shop automatycznie zarządza zależnościami i aktualizacjami.



## Aktualizacja systemu



### Opcja 1: Graficzny interfejs użytkownika (GUI)



Pop!OS posiada prosty, intuicyjny graficzny menedżer aktualizacji.



1. Kliknij na **menu główne** (ikona w lewym dolnym rogu).


2. Otwórz **"Pop!_Shop "**.


3. W Pop!_Shop kliknij zakładkę **"Aktualizacje "**.


4. System automatycznie sprawdzi dostępność aktualizacji.


5. Kliknij **"Aktualizuj wszystko "**, aby rozpocząć instalację aktualizacji.


6. Wprowadź hasło, jeśli jest wymagane.


7. Poczekaj na zakończenie procesu, a w razie potrzeby uruchom go ponownie.



### Opcja 2: Przez terminal



Otwórz terminal i wpisz :



```bash
# Mettre à jour la liste des paquets et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyer les paquets inutiles
sudo apt autoremove -y && sudo apt autoclean
```



### Zarządzanie użytkownikami



Do codziennych operacji zalecamy korzystanie ze standardowego konta użytkownika z uprawnieniami sudo.



Aby utworzyć nowego użytkownika :



```bash
sudo adduser votrenom && sudo usermod -aG sudo votrenom
```



Wyloguj się, a następnie zaloguj ponownie jako nowy użytkownik.



### Zarządzanie sterownikami graficznymi





- W przypadku kart Nvidia należy sprawdzić, czy zainstalowane są firmowe sterowniki:



```bash
sudo apt install system76-driver-nvidia
```





- W przypadku AMD/Intel sterowniki są zazwyczaj dołączane domyślnie.



### Aktywuj zaporę sieciową (UFW)



Pop!OS domyślnie nie blokuje ruchu sieciowego. Aktywuj UFW, aby zwiększyć bezpieczeństwo:



```bash
sudo ufw enable && sudo ufw status verbose
```



### Konfiguracja automatycznych aktualizacji



Aktualizowanie systemu bez konieczności ręcznej interwencji:



```bash
sudo apt install unattended-upgrades && sudo dpkg-reconfigure --priority=low unattended-upgrades
```



### Dostosuj wygląd i zachowanie





- Otwórz **Ustawienia systemowe** → **Wygląd**, aby wybrać jasny lub ciemny motyw.
- Skonfiguruj aktywne narożniki, animacje i rozszerzenia za pomocą menedżera COSMIC.
- Dostosuj układ pulpitu, aby zoptymalizować przepływ pracy.



### Konfiguracja automatycznego tworzenia kopii zapasowych



Pop!OS integruje narzędzia takie jak Deja Dup do tworzenia kopii zapasowych:





- Uruchom **Backup** z menu.
- Wybierz dysk zewnętrzny lub lokalizację sieciową.
- Zaplanuj regularne tworzenie kopii zapasowych.



### Instalowanie przydatnych rozszerzeń GNOME/COSMIC



Oto kilka zalecanych rozszerzeń, które poprawią komfort użytkowania:





- Dash to Dock**: pasek aplikacji zawsze widoczny.
- GSConnect**: synchronizacja z systemem Android.
- Wskaźnik schowka**: zaawansowane zarządzanie schowkiem.



Zainstaluj je za pomocą :



```bash
sudo apt install gnome-shell-extensions
```



Następnie aktywuj je w ustawieniach.



### Optymalizacja zarządzania pamięcią i swapami



Sprawdź status wymiany:



```bash
swapon --show
```



W razie potrzeby zwiększ rozmiar wymiany lub skonfiguruj plik wymiany:



```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```



Dodaj go do pliku `/etc/fstab` w celu automatycznego montowania.



## Zarządzanie pakietami i repozytoriami



### Zrozumienie źródeł pakietów



Pop!OS, oparty na Ubuntu, wykorzystuje głównie :





- Oficjalne repozytoria Ubuntu**: dla większości stabilnego oprogramowania.
- Repozytoria System76**: dla sterowników, oprogramowania sprzętowego i określonych narzędzi.
- Flatpak**: dostęp do szerokiej gamy aplikacji typu sandbox.
- Snap** (opcjonalnie): kolejny uniwersalny format pakietu.



---

### Dodawanie repozytoriów PPA i zarządzanie nimi



Aby zainstalować często aktualizowane oprogramowanie, można dodać określone PPA (Personal Package Archives):



```bash
sudo add-apt-repository ppa:nom/ppa
sudo apt update
```



## Wnioski



Pop!OS to nowoczesna, stabilna dystrybucja Linuksa odpowiednia zarówno dla początkujących, jak i zaawansowanych użytkowników.



Dzięki intuicyjnemu interfejsowi COSMIC i zintegrowanym narzędziom oferuje płynne i produktywne doświadczenie, zarówno w zakresie rozwoju, tworzenia, jak i codziennego użytkowania.



Ten samouczek obejmuje kluczowe etapy: przygotowanie, pobieranie, instalację, ustawienia początkowe i niezbędne narzędzia.



Zachęcamy do dalszego odkrywania Pop!OS i dostosowywania środowiska, aby w pełni wykorzystać jego możliwości.