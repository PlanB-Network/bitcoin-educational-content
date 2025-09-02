---
name: pfSense
description: Instalacja Pfsense
---
![cover](assets/cover.webp)



___



*Ten samouczek jest oparty na oryginalnej treści autorstwa Floriana BURNELA opublikowanej na stronie [IT-Connect](https://www.it-connect.fr/). Licencja [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). W oryginalnym tekście autora wprowadzono znaczące zmiany w celu uaktualnienia samouczka



___



![Image](assets/fr/027.webp)



## I. Prezentacja



pfSense to darmowy system operacyjny typu open source, który przekształca dowolny komputer, serwer dedykowany lub urządzenie sprzętowe w wysokowydajny, wysoce konfigurowalny router i zaporę sieciową. Oparty na FreeBSD i znany ze swojej stabilnej, solidnej architektury sieciowej, pfSense od ponad piętnastu lat wyznacza standardy dla zapór sieciowych typu open source dla firm, władz lokalnych i wymagających użytkowników domowych.



Jego główne funkcje znacznie ewoluowały na przestrzeni lat i były ulepszane z każdą nową wersją. Do chwili obecnej pfSense oferuje:





- Kompletna, scentralizowana administracja za pośrednictwem nowoczesnego, intuicyjnego i bezpiecznego Interface web Interface.
- Wysokowydajna zapora stanowa z zaawansowaną obsługą NAT (w tym NAT-T) i szczegółowym zarządzaniem regułami.
- Natywna obsługa wielu sieci WAN, umożliwiająca agregację lub redundancję połączeń internetowych.
- Zintegrowany serwer i przekaźnik DHCP.
- Wysoka dostępność dzięki protokołowi CARP do przełączania awaryjnego i możliwości konfigurowania klastrów pfSense.
- Równoważenie obciążenia między kilkoma połączeniami lub serwerami.
- Pełna obsługa VPN: IPsec, OpenVPN i WireGuard (zastępując L2TP, obecnie przestarzałe).
- Konfigurowalny portal captive do kontroli dostępu gości, szczególnie w środowiskach publicznych lub hotelowych.



pfSense posiada również rozszerzalny system pakietów, który ułatwia dodawanie zaawansowanych funkcji, takich jak przezroczysty serwer proxy (Squid), filtrowanie adresów URL lub IDS/IPS (Snort lub Suricata) bezpośrednio z sieci Interface.



pfSense jest dystrybuowany wyłącznie dla platform 64-bitowych, zgodnie z aktualnymi zaleceniami FreeBSD. Można go zainstalować na standardowym sprzęcie (komputery PC, serwery stelażowe) lub na platformach wbudowanych o niskiej mocy, takich jak urządzenia Netgate lub niektóre niskoprofilowe komputery x86, które są znacznie wydajniejsze niż starsze komputery Alix.



Na koniec warto pamiętać, że pfSense wymaga co najmniej dwóch fizycznych interfejsów sieciowych: jednego dedykowanego do strefy zewnętrznej (WAN) i jednego dedykowanego do sieci wewnętrznej (LAN). W zależności od złożoności infrastruktury (DMZ, VLAN, wiele sieci WAN), do pełnego wykorzystania jego możliwości może być wymaganych kilka dodatkowych interfejsów.



## II. Pobierz obraz



Najnowsza stabilna wersja pfSense, w momencie pisania tego poradnika, to 2.8 (wydana w czerwcu 2025 r.). Obraz ISO lub plik instalacyjny dostosowany do posiadanego środowiska sprzętowego można pobrać bezpośrednio z oficjalnej strony:





- [Pobierz pfSense](https://www.pfsense.org/download/)



Portal pobierania umożliwia wybór:





- Architektura (ogólnie **AMD64** dla wszystkich nowoczesnych urządzeń).
- Typ obrazu (**Installer USB Memstick** do instalacji przez pamięć USB, **ISO Installer** do nagrywania lub wirtualnej edycji).
- Najbliższy serwer lustrzany pobierania, aby zoptymalizować prędkość transferu.



Dla tych, którzy chcą wdrożyć pfSense w środowisku zwirtualizowanym (Proxmox, VMware ESXi, VirtualBox...), dostępny jest również obraz **OVA**. Ta gotowa do użycia maszyna wirtualna znacznie upraszcza instalację i początkową konfigurację. Należy jedynie dostosować przydzielone zasoby (CPU, RAM, interfejsy sieciowe) do oczekiwanego obciążenia i topologii sieci.



Przed instalacją zalecamy sprawdzenie integralności pobranego pliku poprzez weryfikację **SHA256** podanego na oficjalnej stronie pobierania. Gwarantuje to, że obraz nie został zmieniony lub uszkodzony.



## III. Instalacja



W tym przykładzie instalacja jest wykonywana na maszynie wirtualnej z systemem VirtualBox. Procedura pozostaje identyczna na maszynie fizycznej lub innym hypervisorze, z wyjątkiem zarządzania urządzeniami wirtualnymi.



### 1. Minimalne wymagania sprzętowe



W przypadku standardowego wdrożenia zalecamy:





- minimum 1 GB pamięci RAM** (zalecane jest 2 GB lub więcej, aby umożliwić obsługę dodatkowych pakietów lub ZFS).
- 8 GB miejsca na dysku** (20 GB lub więcej jest preferowane w przypadku bardziej zaawansowanych konfiguracji, zwłaszcza jeśli instalujesz pamięć podręczną proxy, IDS/IPS lub szczegółowe dzienniki).
- Co najmniej dwa wirtualne interfejsy sieciowe** (jeden dla sieci WAN, jeden dla sieci LAN). W VirtualBox należy dodać je do ustawień maszyny wirtualnej przed jej uruchomieniem.



### 2. Uruchomienie instalatora



Zamontuj pobrany obraz ISO jako wirtualny napęd optyczny w VirtualBox lub włóż klucz USB, jeśli instalujesz na komputerze fizycznym. Po uruchomieniu pojawi się menu rozruchowe:



Jeśli nie wybierzesz żadnych opcji, program pfSense uruchomi się automatycznie z opcjami domyślnymi po kilku sekundach. Naciśnij przycisk "**Enter**", aby rozpocząć normalne uruchamianie.



![Image](assets/fr/027.webp)



Gdy pojawi się menu główne, szybko naciśnij przycisk "**I**", aby rozpocząć instalację.



![Image](assets/fr/001.webp)



### 3. Początkowe ustawienia instalatora



Pierwszy ekran umożliwia ustawienie kilku parametrów regionalnych, takich jak czcionka wyświetlacza i kodowanie znaków. Ustawienia te są przydatne w szczególnych przypadkach (niestandardowe klawiatury, ekrany szeregowe, języki orientalne). W przypadku większości instalacji należy zachować wartości domyślne i wybrać opcję "**Accept these Settings**".



![Image](assets/fr/002.webp)



### 4. Wybór trybu instalacji



Wybierz "**Quick/Easy Install**", aby uruchomić automatyczną instalację z zalecanymi opcjami. Ta metoda usuwa wybrany dysk i konfiguruje pfSense z domyślnym podziałem na partycje.



![Image](assets/fr/003.webp)



Pojawi się ostrzeżenie informujące, że wszystkie dane na dysku zostaną usunięte. Potwierdź przyciskiem "**OK**".



Następnie instalator skopiuje niezbędne pliki na dysk. W zależności od posiadanego sprzętu może to zająć od kilku sekund do kilku minut.



### 5. Wybór rdzenia



Gdy instalator wyświetli monit o wybranie typu jądra, należy wybrać opcję "**Standard Kernel**". To ogólne jądro doskonale nadaje się do standardowych wdrożeń, zarówno na komputerach PC, serwerach, jak i maszynach wirtualnych.



### 6. Zakończenie instalacji i ponowne uruchomienie



Po zakończeniu instalacji wybierz "**Reboot**", aby ponownie uruchomić komputer na nowej instancji pfSense.



**Ważna uwaga**: usuń obraz ISO lub odłącz instalacyjny klucz USB przed ponownym uruchomieniem komputera, aby uniknąć ponownego uruchomienia programu instalacyjnego przy następnym uruchomieniu komputera.



## IV. Pierwsze uruchomienie programu pfSense



Przy pierwszym uruchomieniu pfSense musi być skonfigurowany do rozpoznawania i prawidłowego przypisywania interfejsów sieciowych (WAN, LAN, DMZ, VLAN itp.). Dokładna identyfikacja kart sieciowych jest niezbędna, aby uniknąć błędów konfiguracji, które mogą pozbawić użytkownika dostępu do sieci Interface lub spowodować, że zapora sieciowa przestanie działać.



Po uruchomieniu pfSense automatycznie wykrywa i wyświetla listę wszystkich dostępnych interfejsów sieciowych, wskazując MAC Address dla każdego z nich. Ułatwia to ich rozróżnianie.



### 1. Sieci VLAN



Pierwsze pytanie dotyczy konfiguracji sieci VLAN. Na tym etapie, w przypadku podstawowej konfiguracji, nie będziemy aktywować żadnych sieci VLAN. Naciśnij więc klawisz "**N**", aby pominąć ten krok.



![Image](assets/fr/004.webp)



### 2. WAN i LAN Interface Assignment



następnie program pfSense wyświetli monit o określenie, który Interface będzie używany dla sieci WAN (dostęp do Internetu). Można wybrać pomiędzy:





- Wprowadź nazwę Interface ręcznie (zalecane dla środowisk wirtualnych).
- Użyj automatycznego wykrywania, naciskając "**A**". Ta opcja jest przydatna na fizycznym hoście, pod warunkiem, że kable sieciowe są podłączone, a łącza aktywne.



![Image](assets/fr/005.webp)



W tym przykładzie ręcznie konfigurujemy sieć WAN. Wprowadź dokładną nazwę Interface. W przypadku karty Intela, nazwa będzie często brzmiała "**em0**" pod FreeBSD, ale może się różnić w zależności od sprzętu. Na przykład karta Realtek będzie często wyświetlana jako "**re0**".



![Image](assets/fr/006.webp)



Powtórz tę samą operację, aby zdefiniować Interface LAN. Tutaj używamy "**em1**".



pfSense potwierdza, że Interface LAN aktywuje zarówno firewall, jak i NAT, aby chronić sieć wewnętrzną i zarządzać translacją Address.



Jeśli masz inne interfejsy fizyczne, możesz skonfigurować dodatkowe interfejsy (DMZ, Wi-Fi, określone sieci VLAN) na tym etapie. Każdy logiczny Interface wymaga odpowiedniej karty sieciowej lub wirtualnego Interface. W początkowej konfiguracji ograniczymy się do sieci WAN i LAN.



Po zakończeniu przypisywania program pfSense wyświetli przejrzyste podsumowanie zgodności między interfejsami fizycznymi i przypisanymi rolami. Potwierdź przyciskiem "**Y**".



### 3. Konsola PfSense



Po zakończeniu tego kroku pojawi się menu główne konsoli pfSense. Oferuje ono kilka przydatnych opcji do bezpośredniej administracji, takich jak resetowanie hasła internetowego, ponowne uruchamianie, ponowne ładowanie konfiguracji lub ponowne przypisywanie interfejsów.



![Image](assets/fr/007.webp)



Zobaczysz również podsumowanie bieżących ustawień sieciowych, w tym domyślny adres IP Address sieci LAN Interface, zwykle **192.168.1.1**. Jest to adres Address, który należy wprowadzić w przeglądarce, aby uzyskać dostęp do sieci administracyjnej Interface.



**Uwaga**: Jeśli sieć wewnętrzna korzysta z innego zakresu Address, wybierz "**2)** Set Interface(s) IP Address" w menu, aby przypisać adres IP Address odpowiedni dla danego środowiska.



Domyślnie, jeśli Interface WAN jest podłączony do urządzenia lub modemu skonfigurowanego przez DHCP, pfSense automatycznie pobierze publiczny adres IP Address. Należy zatem skorzystać z natychmiastowego dostępu do Internetu, podłączając klienta do sieci LAN pfSense Interface.



## V. Pierwszy dostęp do sieci Interface



Po zakończeniu wstępnego rozruchu i skonfigurowaniu interfejsów sieciowych można uzyskać dostęp do sieci Interface pfSense, aby sfinalizować i dostosować konfigurację.



### 1. Początkowe połączenie



Podłącz komputer do portu LAN (lub wirtualnej sieci Interface LAN w hiperwizorze) i w razie potrzeby przypisz mu adres IP Address w tym samym zakresie (domyślnie program pfSense automatycznie dystrybuuje adres Address przez DHCP w sieci LAN).



W przeglądarce przejdź do Address wskazanego przez konsolę (domyślnie `https://192.168.1.1`). Należy pamiętać, że pfSense wymaga protokołu HTTPS nawet przy pierwszym połączeniu - należy więc spodziewać się ostrzeżenia o samopodpisanym certyfikacie, które można zignorować, dodając wyjątek.



Zostanie wyświetlony ekran logowania. Domyślne dane logowania to:




- Nazwa użytkownika:** `admin`
- Hasło:** `pfsense`



Identyfikatory te zostaną zmodyfikowane podczas początkowego kreatora konfiguracji.



## VI. Kreator konfiguracji



Przy pierwszym połączeniu pfSense wyświetli monit o wykonanie **Kreatora konfiguracji**. Zdecydowanie zalecamy skorzystanie z niego, aby upewnić się, że wszystkie istotne parametry są poprawnie zdefiniowane.



### 1. Parametry ogólne



Możesz:




- Określ nazwę hosta i domenę lokalną (przykład: `pfsense` i `lan.local`).
- Zdefiniuj serwery DNS i wybierz, czy pfSense ma korzystać z DNS dostawcy usług internetowych, czy z usługi zewnętrznej (Cloudflare, OpenDNS, Quad9...).



### 2. Strefa czasowa



Wskaż strefę czasową witryny, aby dzienniki i harmonogramy były spójne (np. `Europe/Paris`).



### 3. Konfiguracja sieci WAN



Konfiguracja połączenia WAN:




- Domyślnie **DHCP** (wystarczające, jeśli jesteś za skrzynką).
- Jeśli masz stały adres IP, wprowadź parametry (statyczny adres IP, maska, brama, DNS) ręcznie.
- W razie potrzeby zdefiniuj sieć VLAN lub uwierzytelnianie PPPoE (powszechne u niektórych dostawców usług internetowych).



### 4. Konfiguracja sieci LAN



Kreator sugeruje zmianę domyślnej podsieci LAN. Jeśli masz określony plan adresowania, nadszedł czas, aby go dostosować.



### 5. Zmiana hasła administratora



Zabezpiecz pfSense, natychmiast ustawiając silne hasło dla użytkownika `admin`.



## VII. Weryfikacja i aktualizacje



Przed wdrożeniem zapory sieciowej należy upewnić się, że dostępna jest najnowsza wersja:





- Przejdź do **System > Aktualizacja**.
- Wybierz kanał aktualizacji (zazwyczaj **Stabilny**).
- Sprawdź dostępność aktualizacji i zastosuj je.



Dobrym pomysłem jest włączenie powiadomień o aktualizacjach, aby być informowanym o poprawkach bezpieczeństwa.



## VIII. Zapisywanie konfiguracji



Przed wprowadzeniem jakichkolwiek większych zmian należy wdrożyć politykę tworzenia kopii zapasowych:





- Przejdź do **Diagnostyka > Kopia zapasowa i przywracanie**.
- Pobranie kopii bieżącej konfiguracji (`config.xml`).
- Przechowuj go w bezpiecznym miejscu (zaszyfrowany nośnik zewnętrzny).



W przypadku środowisk o krytycznym znaczeniu należy rozważyć automatyczne tworzenie kopii zapasowych konfiguracji na zewnętrznym serwerze lub za pomocą zaprogramowanego skryptu.



## IX. Najlepsze praktyki po instalacji



Aby zakończyć wdrożenie ze spokojem ducha:





- Modyfikacja reguł zapory**: domyślnie program pfSense zezwala na cały ruch wychodzący w sieci LAN i blokuje ruch przychodzący w sieci WAN. Dostosuj te reguły zgodnie z wymaganiami.
- Skonfiguruj bezpieczny dostęp zdalny**: w razie potrzeby włącz dostęp do sieci Interface z sieci WAN tylko przez VPN lub z ograniczeniami IP.
- Włącz powiadomienia**: skonfiguruj serwer SMTP do otrzymywania powiadomień (awarie, aktualizacje, błędy).
- Zainstaluj przydatne rozszerzenia**: na przykład IDS/IPS (Snort, Suricata), proxy (Squid), filtrowanie DNS (pfBlockerNG).



Twoja zapora sieciowa pfSense jest już uruchomiona i gotowa do ochrony Twojej sieci. Dzięki swojej elastyczności i aktywnej społeczności, masz potężne, skalowalne narzędzie, które można dostosować do przyszłych potrzeb (multi-WAN, VLAN, site-to-site VPN, captive portal, itp.).



Regularnie zapoznawaj się z oficjalną dokumentacją ([docs.netgate.com](https://docs.netgate.com/pfsense/en/latest/)), aby odkryć nowe funkcje i upewnić się, że Twoja konfiguracja jest aktualna i bezpieczna.