---
name: Zorin OS
description: Kompletny przewodnik instalacji i użytkowania systemu Zorin OS jako nowoczesnej alternatywy dla systemu Windows
---

![cover](assets/cover.webp)



## Wprowadzenie



System operacyjny (OS) to podstawowe oprogramowanie, które umożliwia działanie komputera: zarządza sprzętem, oprogramowaniem, bezpieczeństwem i interfejsem użytkownika.


Zorin OS to dystrybucja Linuksa zaprojektowana specjalnie w celu ułatwienia przejścia z systemu Windows, oferując jednocześnie korzyści oprogramowania open source: bezpieczeństwo, stabilność, prywatność i wydajność.



Oparty na Ubuntu LTS, Zorin OS łączy w sobie wysoką kompatybilność oprogramowania ze znajomym, konfigurowalnym interfejsem, co czyni go wiarygodną i dostępną alternatywą dla Windows.



## Dlaczego Zorin OS?





- Interface znajomy**: Wygląd podobny do systemu Windows (menu start, pasek zadań)
- Łatwe przejście**: przeznaczone dla użytkowników korzystających z systemu Windows
- Zwiększone bezpieczeństwo**: Architektura Linux, mniej narażona na wirusy
- Poszanowanie prywatności**: brak inwazyjnego gromadzenia danych
- Zoptymalizowana wydajność**: działa dobrze na skromnych maszynach
- Baza Ubuntu LTS**: stabilność, regularne aktualizacje i szeroka kompatybilność
- Zaawansowana personalizacja**: za pomocą narzędzia Zorin Appearance.



## Instalacja i konfiguracja



### 1. Wymagania wstępne



**Wymagany sprzęt:**





- Klucz USB o pojemności co najmniej **8 GB** (zalecane 12 GB);
- Komputer z co najmniej **25 GB wolnego miejsca na dysku**
- Połączenie internetowe (zalecane).



### 2. Pobierz Zorin OS





- Odwiedź oficjalną stronę internetową: [https://zorin.com/os](https://zorin.com/os)



![Page de téléchargement Balena Etcher](assets/fr/03.webp)





- Wybierz **Zorin OS Core** (zalecana wersja bezpłatna)



![Page de téléchargement Balena Etcher](assets/fr/04.webp)





- Pobierz obraz ISO



Zorin OS oferuje również :





- Zorin OS Lite** (starsze komputery)
- Zorin OS Pro** (płatny, z zaawansowanymi funkcjami i wsparciem)



## Tworzenie bootowalnego klucza USB



Możesz użyć kilku narzędzi, takich jak Balena Etcher :





- Pobierz i zainstaluj [Balena Etcher](https://etcher.balena.io/).
- Otwórz program Balena Etcher, a następnie wybierz obraz Zorin ISO.
- Wybierz klucz USB jako nośnik docelowy.
- Kliknij Flash i poczekaj na zakończenie procesu.



![Utilisation de Balena Etcher](assets/fr/05.webp)



## Uruchamianie za pomocą klawiszy i dostęp do systemu BIOS



Wyłącz komputer, na którym chcesz zainstalować Zorin OS, a następnie podłącz klucz USB.


Po uruchomieniu komputera wejdź do BIOS-u (`ESC`, `F9` lub `F11` w zależności od marki) i wybierz klucz USB jako urządzenie rozruchowe, a następnie naciśnij `Enter`, aby rozpocząć proces rozruchu.





- Podczas uruchamiania wybierz **Try or Install Zorin OS**.



![capture](assets/fr/08.webp)





- Jeśli posiadasz kartę graficzną NVIDIA, wybierz **Try or Install Zorin OS (modern NVIDIA drivers)**.
- Poczekaj, aż pliki zostaną sprawdzone.



![capture](assets/fr/09.webp)





- W instalatorze Zorin OS wybierz język **Francuski**, a następnie kliknij Zainstaluj **Zorin OS**.



![capture](assets/fr/10.webp)





- Wybierz układ klawiatury.



![capture](assets/fr/11.webp)





- Zaznacz pola **Pobierz aktualizacje podczas instalacji Zorin OS** i **Zainstaluj oprogramowanie innych firm dla sprzętu graficznego i Wi-Fi oraz dodatkowych formatów multimediów**.



![capture](assets/fr/12.webp)





- Aby zainstalować Zorin OS na całym dysku: wybierz **Erase disk and install Zorin OS**.



![capture](assets/fr/14.webp)



Aby zainstalować system Zorin OS wraz z systemem Windows (podwójny rozruch) :





- Wybierz **Install Zorin OS obok Windows Boot Manager**.



![capture](assets/fr/15.webp)





- Jeśli dysk nie został podzielony na partycje, wybierz miejsce na dysku, które chcesz przydzielić systemowi Zorin OS, a następnie kliknij przycisk **Zainstaluj teraz**.



![capture](assets/fr/16.webp)





- Dwukrotnie potwierdź zmiany na płycie.



![capture](assets/fr/16.webp)



![capture](assets/fr/17.webp)





- Wybierz obszar geograficzny **Paryż**.



![capture](assets/fr/18.webp)





- Utwórz konto użytkownika i nadaj komputerowi nazwę.



![capture](assets/fr/19.webp)





- Poczekaj, aż system Zorin OS zostanie zainstalowany.



![capture](assets/fr/20.webp)





- Po zakończeniu instalacji kliknij przycisk **Restart Now**.



![capture](assets/fr/21.webp)





- Usuń klucz instalacyjny USB i naciśnij Enter.



![capture](assets/fr/22.webp)



## Odkrywanie i korzystanie z Zorin OS



### Pierwsze uruchomienie



Po uruchomieniu komputera zostaniesz przeniesiony do GRUB - menedżera rozruchu systemu Linux. Domyślnie wybrany jest **Zorin OS**; po 30 sekundach uruchomi się on automatycznie.



![capture](assets/fr/23.webp)



Jeśli system Zorin OS został zainstalowany w trybie podwójnego rozruchu z systemem Windows, można uruchomić system Windows, wybierając opcję **Windows Boot Manager**.



Zaloguj się na swoje konto użytkownika:



![capture](assets/fr/24.webp)



Przy pierwszym uruchomieniu uruchamiana jest aplikacja **Welcome to Zorin OS**, która pomaga odkryć nowy system operacyjny.



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



![capture](assets/fr/27.webp)



![capture](assets/fr/28.webp)



![capture](assets/fr/29.webp)



![capture](assets/fr/30.webp)



![capture](assets/fr/31.webp)



![capture](assets/fr/32.webp)





### Aktualizacja systemu



Menedżer aktualizacji wkrótce się otworzy, informując o dostępności aktualizacji. Zainstaluj je, klikając przycisk **Zainstaluj teraz**.



![capture](assets/fr/33.webp)



Aktualizacje można sprawdzić ręcznie w aplikacji **Software** > Aktualizacje:



![capture](assets/fr/34.webp)



### Personalizacja



Pierwszą rzeczą do zrobienia w Zorin OS jest wybranie **układu pulpitu**, który najbardziej ci odpowiada. Znajdziesz układy podobne do tych, które można znaleźć w systemie Windows (a nawet bardziej w wersji Pro).



Aby to zrobić, otwórz **Zorin Appareance** > **Type** :



![capture](assets/fr/35.webp)



Następnie otwórz **Ustawienia**, aby dostosować swój system:


**Dźwięk - Ustawienia - Zorin OS



![capture](assets/fr/36.webp)



**Konta online - Ustawienia - Zorin OS



![capture](assets/fr/37.webp)



### Zastosowania



Aplikacje można instalować na kilka sposobów:





- Software**, sklep z aplikacjami Zorin OS. Aplikacje pochodzą z kilku źródeł: apt, Flatpak i Snap.



![capture](assets/fr/38.webp)



![capture](assets/fr/39.webp)





- apt** install (wiersz poleceń) :



```bash
sudo apt install gparted
```



![capture](assets/fr/40.webp)



Więcej informacji na temat instalowania aplikacji w systemie Zorin OS można znaleźć na tej stronie: [Install Apps (zorin.com)](https://zorin.com/help/install-apps/).



### Aplikacje Windows



Aby zainstalować aplikacje Windows, należy rozpocząć od instalacji pakietu **zorin-windows-app-support** za pośrednictwem Terminala :



```bash
sudo apt install zorin-windows-app-support
```



Lista kompatybilnych aplikacji Windows i ich poziomów kompatybilności znajduje się na stronie [Wine Application Database] (https://appdb.winehq.org/). Znajdziesz tam następujące odznaki, odpowiadające poziomowi kompatybilności (od najlepszego do najgorszego): Platinum, Gold, Silver, Bronze i Garbage.



Aby zainstalować aplikację Windows .exe lub .msi, dostępne są dwie opcje:





- Otwórz **PlayOnLinux** i kliknij przycisk **Install**, aby przeglądać kompatybilne aplikacje i gry.



![capture](assets/fr/41.webp)





- Kliknij dwukrotnie plik **.exe lub .msi** aplikacji i pozwól, aby program instalacyjny poprowadził Cię.



![capture](assets/fr/42.webp)



![capture](assets/fr/43.webp)



## Wnioski i dodatkowe zasoby



Zorin OS to solidna, niedroga alternatywa dla systemu Windows, łącząca w sobie prostotę, bezpieczeństwo i prywatność.



Umożliwia płynne przejście na system Linux, bez poświęcania wygody i produktywności.



Aby jeszcze bardziej chronić swoje cyfrowe życie, zalecamy korzystanie z usług przyjaznych dla prywatności, zwłaszcza w przypadku szyfrowanej komunikacji:



https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2