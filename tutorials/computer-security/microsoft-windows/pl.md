---
name: Windows 11
description: Automatyczna instalacja Microsoft Windows 11 za pomocą pliku konfiguracyjnego
---
![cover](assets/cover.webp)


W tym samouczku dowiemy się, jak automatycznie zainstalować system Windows 11 przy użyciu metody innej niż standardowy proces instalacji systemu Windows.


## Pobierz!


Pierwszą rzeczą, której będziesz potrzebować, jest plik instalacyjny. Najbezpieczniejszym i najbardziej niezawodnym miejscem do jego pobrania jest oficjalna strona Microsoftu.


Wystarczy odwiedzić poniższy link i postępować zgodnie z instrukcjami, aby pobrać [plik ISO systemu Windows 11](https://www.microsoft.com/en-us/software-download/windows11)


![Image](assets/en/02.webp)


Gdy znajdziesz się na stronie pobierania, przewiń w dół do sekcji pobierania pliku ISO.


![Image](assets/en/01.webp)


i wybrać odpowiednią wersję.


![Image](assets/en/03.webp)


Po wybraniu systemu Windows 11 kliknij przycisk Potwierdź.


Na tym etapie przetworzenie żądania może potrwać kilka sekund, po czym zostanie wyświetlona następująca strona:


![Image](assets/en/04.webp)


Po potwierdzeniu żądania należy wybrać preferowany język.


![Image](assets/en/05.webp)


Po wybraniu języka i kliknięciu przycisku Potwierdź żądanie zostanie przetworzone. Ten krok może potrwać kilka sekund.


Po pomyślnym przetworzeniu żądania zostanie wyświetlona strona z łączem do pobrania pliku .iso. Kliknij przycisk Download 64-bit, aby rozpocząć pobieranie.


Rozmiar pliku wynosi około 5,5 GB, a wygenerowany link będzie ważny przez 24 godziny.


## Automatyzacja!


Na tym etapie musimy wprowadzić zmiany w standardowej instalacji systemu Windows. Na tym etapie, korzystając z instalacji nienadzorowanej, określamy, które elementy zostaną zainstalowane, bez udziału użytkownika. W rzeczywistości w tej metodzie plik XML jest używany do konfigurowania kroków instalacji i usług instalowanych w systemie Windows. Innymi słowy, użycie pliku Unattended.xml tworzy proces automatyzacji podczas instalacji, zapobiegając konieczności wybierania wielu opcji i unikając żmudnych kroków zwykle wymaganych podczas konfiguracji. Ta metoda jest nietypową, ale standardową metodą wprowadzoną przez Microsoft. Więcej informacji można znaleźć na [oficjalnej stronie Microsoftu](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs?view=windows-11).


W Internecie dostępne są różne narzędzia do generowania nienadzorowanych plików. Niektóre z nich są online, podczas gdy inne są offline. Jednym z narzędzi online do tworzenia tego pliku jest [ta strona](https://schneegans.de/windows/unattend-generator). Po jej otwarciu wyświetli się następująca strona:


![Image](assets/en/06.webp)


Jak wspomniano na górze strony, ta metoda może być używana do instalacji Windows 10 i 11. W pierwszym kroku wybieramy język systemu Windows. Jeśli chcemy dodać drugi lub nawet trzeci język do listy języków wyświetlania i klawiatury systemu Windows, możemy skorzystać z poniższego pola:


![Image](assets/en/07.webp)


W następnym kroku wybieramy żądaną lokalizację.


![Image](assets/en/08.webp)


Na tym etapie możemy również określić architekturę procesora dla komputera. W tym kroku możemy:

1. Zdecyduj, czy ignorować funkcje zabezpieczeń systemu Windows, takie jak TPM i Secure Boot. Funkcja Secure Boot zapewnia, że jeśli jakiekolwiek podstawowe pliki systemu Windows zostaną naruszone podczas procesu rozruchu, problem zostanie wykryty, a ich wykonanie zostanie uniemożliwione. Funkcja ta pomaga również chronić system przed instalacją złośliwych aktualizacji w systemie Windows. Włączenie opcji omijania tych funkcji jest czasami nieuniknione na niektórych komputerach, zwłaszcza starszych modelach. Ogólnie zaleca się jednak, aby funkcje takie jak Secure Boot były włączone.

2. Zignoruj wymóg połączenia internetowego, aby zakończyć proces. Jest to przydatne w sytuacjach, gdy przewodowe połączenie LAN nie jest dostępne, ponieważ w większości przypadków karta bezprzewodowa nie jest jeszcze rozpoznawana podczas instalacji systemu Windows i wymagany jest dostęp do Internetu za pośrednictwem kabla. Aktywacja tej opcji rozwiązuje problemy związane z tym krokiem.


W następnym kroku możemy wybrać nazwę komputera.


![Image](assets/en/09.webp)


Możemy również zezwolić systemowi Windows na wybranie nazwy systemu. W tym kroku możemy wybrać typ systemu Windows, skompresowany lub nieskompresowany, lub pozwolić systemowi Windows określić odpowiednią wersję na podstawie specyfikacji komputera. Na tym etapie można również ustawić strefę czasową.


Kolejny krok obejmuje ustawienia partycji:


![Image](assets/en/10.webp)


Na tym etapie możemy określić typ partycji do instalacji systemu Windows, a także wymagane ustawienia do instalacji środowiska odzyskiwania systemu Windows. Wybierając pierwszą opcję, wybór partycji i partycjonowanie są odkładane na czas instalacji systemu Windows, a podczas instalacji pytania te będą zadawane tak samo, jak w przypadku normalnej metody instalacji.


W tym kroku wybieramy wersję systemu Windows do zainstalowania:


![Image](assets/en/11.webp)


Jeśli dostępny jest klucz produktu, można go również wprowadzić na tym etapie.


Następnym krokiem jest skonfigurowanie konta logowania do systemu Windows:


![Image](assets/en/12.webp)


## Spotkania na koncie


Na tym etapie:


1. Możemy zdefiniować nazwę i hasło dla konta administratora. Możliwe jest również utworzenie wielu kont użytkowników lub administratorów.

2. Tutaj określamy konto, na które należy się zalogować po raz pierwszy po instalacji systemu Windows. Różne opcje dla tej sekcji są pokazane na obrazku.

3. Jeśli nie chcesz tworzyć żadnych kont, wyczyść wszystkie konta i wybierz tę opcję. W takim przypadku po instalacji systemu Windows zostaniesz automatycznie zalogowany na konto administratora systemu Windows.


Kolejny krok obejmuje konfigurację hasła i ustawień pliku hosta:


![Image](assets/en/13.webp)


Na tym etapie określamy, czy hasła powinny mieć okres ważności. Dodatkowo sekcja ta zawiera ustawienia bezpieczeństwa związane z nieudanymi próbami logowania, które można włączyć lub wyłączyć w zależności od potrzeb.


W dolnej części tej sekcji znajdują się ustawienia wyświetlania plików. Żadna z tych opcji nie jest dostępna podczas standardowej instalacji systemu Windows i musi zostać skonfigurowana po instalacji. Natomiast w przypadku metody instalacji nienadzorowanej ustawienia te są łatwo dostępne.


Następnym krokiem jest skonfigurowanie ustawień zabezpieczeń systemu Windows:


![Image](assets/en/14.webp)


## Ustawienia zabezpieczeń


Na tym etapie:


1. Windows Defender można włączyć lub wyłączyć. Ta funkcja działa jak oprogramowanie zabezpieczające w systemie Windows i pomaga zapobiegać wykonywaniu złośliwych plików, niektórym atakom sieciowym i nie tylko.

2. Automatyczne aktualizacje systemu Windows można wyłączyć. Jest to jedno z najczęstszych wyzwań stojących przed użytkownikami systemu Windows!

3. Ta sekcja umożliwia włączenie lub wyłączenie UAC (Kontrola konta użytkownika). Funkcja ta zapobiega uruchamianiu podejrzanych aplikacji z podwyższonymi uprawnieniami do odczytu i zapisu.

4. Ta funkcja jest używana przez system Windows do wykrywania potencjalnie szkodliwego oprogramowania.

5. Włączenie lub wyłączenie obsługi długich ścieżek w aplikacjach systemu Windows, takich jak PowerShell i innych.

6. Włączenie lub wyłączenie Pulpitu zdalnego w celu uzyskania zdalnego dostępu do systemu.


W zależności od używanej wersji systemu Windows niektóre z tych funkcji mogą być obsługiwane lub nie.


Następnym krokiem jest konfiguracja ikon:


![Image](assets/en/15.webp)


W tej sekcji:


1. Wyświetlane są ikony pulpitu, które można dodawać lub usuwać w zależności od potrzeb.

2. Na liście znajdują się ikony menu Start, które można również dodawać lub usuwać w zależności od wymagań.

3. Ta sekcja pozwala skonfigurować, czy narzędzia związane z wirtualizacją są zainstalowane, czy nie. Ta opcja jest specyficzna dla systemu Windows 11 i nie ma zastosowania do systemu Windows 10.


Kolejny krok obejmuje konfigurację ustawień Wi-Fi:


![Image](assets/en/16.webp)


W tej sekcji można skonfigurować ustawienia sieci Wi-Fi. Jak wspomniano wcześniej, w większości przypadków karta Wi-Fi nie jest rozpoznawana podczas instalacji systemu Windows, więc połączenie podczas konfiguracji zwykle nie jest możliwe. Jednak po skonfigurowaniu tej sekcji, jeśli karta bezprzewodowa zostanie wykryta, system może połączyć się z Internetem.


Kolejny krok obejmuje ważne ustawienie:


![Image](assets/en/17.webp)


W tej sekcji określamy, czy informacje o problemach systemowych powinny być wysyłane do firmy Microsoft, czy nie.


Następnym krokiem jest skonfigurowanie domyślnych aplikacji:


![Image](assets/en/18.webp)


## Domyślne włączenie/wyłączenie oprogramowania


W tej sekcji możemy wybrać dowolne aplikacje, których nie chcemy instalować domyślnie. Na przykład możemy zrezygnować z instalacji Cortany lub Copilota.


Kolejny krok obejmuje ustawienia bezpieczeństwa związane z wykonywaniem aplikacji:


![Image](assets/en/19.webp)


Zastosowanie ustawień WDAC może uniemożliwić wykonywanie niektórych aplikacji.


Na koniec, po zastosowaniu żądanych ustawień, można pobrać wygenerowany plik XML:


![Image](assets/en/20.webp)


Kliknięcie Pobierz plik XML spowoduje pobranie pliku autounattend.xml. Aby użyć tego pliku, wystarczy zamontować pobrany plik ISO na dysku USB, umieścić plik autounattend.xml w katalogu głównym, a następnie kontynuować instalację systemu Windows.


Jednym z dostępnych narzędzi do tworzenia bootowalnego dysku USB jest Rufus. Rufus może utworzyć bootowalny instalacyjny dysk flash Windows z danym plikiem ISO instalacji systemu Windows. Jest szybki i prosty, można go pobrać [tutaj](https://rufus.ie/en/#download)


![Image](assets/en/21.webp)


W tym oprogramowaniu, po wybraniu żądanego napędu USB i odpowiedniego pliku ISO, klikamy Start.


![Image](assets/en/22.webp)


Na tym etapie wyłączamy wszystkie opcje, ponieważ ich włączenie może powodować konflikty podczas korzystania z wygenerowanego pliku Unattend. Po skopiowaniu plików na dysk USB, umieszczamy plik autounattend.xml w katalogu głównym:


![Image](assets/en/23.webp)


W tym momencie napęd USB jest gotowy do automatycznej instalacji systemu Windows i można rozpocząć instalację przy użyciu tego napędu.


## Edycja ISO


Jeśli chcesz zainstalować system Windows na maszynie wirtualnej, możesz użyć oprogramowania do tworzenia i edycji plików ISO. Jednym z takich programów jest AnyBurn. Po wyodrębnieniu zawartości pliku ISO pobranego ze strony internetowej Microsoft, umieść plik autounattend.xml w katalogu głównym. Następnie za pomocą AnyBurn utwórz nowy plik ISO ze zaktualizowaną zawartością.


AnyBurn to wielofunkcyjne oprogramowanie do pracy z plikami ISO. Oferuje różne funkcje obsługi plików ISO, z których jedną jest tworzenie bootowalnych obrazów ISO; [tutaj](https://www.anyburn.com/download.php) to oryginalna strona internetowa.


Na stronie głównej oprogramowania wybierz opcję "Utwórz obraz z pliku/folderu":


![Image](assets/en/24.webp)


Na następnej stronie wybierz wszystkie pliki wyodrębnione z ISO wraz z plikiem autounattend.xml.


![Image](assets/en/25.webp)


W tym kroku konfigurujemy ustawienia, aby plik ISO był bootowalny:


![Image](assets/en/26.webp)


Na tym etapie należy ustawić ścieżkę do pliku bootfix.bin, aby umożliwić uruchomienie ISO. Plik ten znajduje się w katalogu głównym ISO, wewnątrz folderu rozruchowego. Zaleca się również włączenie opcji ISO9660 i UDF w sekcji Właściwości.


![Image](assets/en/27.webp)


Po wykonaniu tego kroku, kliknięcie Next spowoduje utworzenie pliku ISO. Plik ten może być używany w oprogramowaniu do wirtualizacji, takim jak Oracle VirtualBox. Poniżej znajduje się samouczek dotyczący VirtualBox:


https://planb.academy/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65