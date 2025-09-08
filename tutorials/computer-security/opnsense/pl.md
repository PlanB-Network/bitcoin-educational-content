---
name: OPNsense
description: Jak zainstalować i skonfigurować zaporę sieciową OPNsense?
---
![cover](assets/cover.webp)



___



*Ten samouczek jest oparty na oryginalnej treści autorstwa Floriana BURNELA opublikowanej na stronie [IT-Connect](https://www.it-connect.fr/). Licencja [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). W oryginalnym tekście mogły zostać wprowadzone zmiany



___



## I. Prezentacja



W tym samouczku przyjrzymy się otwartemu firewallowi OPNsense. Przyjrzymy się jego głównym funkcjom, wymaganiom wstępnym i sposobowi instalacji tego rozwiązania opartego na FreeBSD.



Zanim zaczniemy, powinniśmy wiedzieć, że **OPNsense i pfSense są firewallami open source** opartymi na FreeBSD. Można powiedzieć, że pfSense jest w pewnym sensie starszym bratem OPNsense, ponieważ ten ostatni jest Fork stworzonym w 2015 roku. Na koniec należy zauważyć, że od 2017 roku **OPNsense przeszedł na HardenedBSD zamiast FreeBSD**. HardenedBSD to ulepszona wersja FreeBSD z zaawansowanymi funkcjami bezpieczeństwa



OPNsense wyróżnia się bardziej nowoczesnym interfejsem użytkownika Interface i **częstszą częstotliwością aktualizacji**. Rzeczywiście, harmonogram aktualizacji OPNsense obejmuje dwa główne wydania rocznie, które są aktualizowane co około dwa tygodnie (co skutkuje mniejszymi wydaniami). Ta kontynuacja jest bardzo interesująca w porównaniu z pfSense, jeśli spojrzymy na wersje społecznościowe tych rozwiązań.



![Image](assets/fr/050.webp)



## II. Funkcje OPNsense



OPNsense to system operacyjny zaprojektowany do działania jako zapora ogniowa i router, choć jego funkcje są liczne i można je rozszerzyć, instalując dodatkowe pakiety. Nadaje się do użytku produkcyjnego, jest używany głównie do bezpieczeństwa sieci i zarządzania przepływem.



### A. Główne cechy



Oto niektóre z kluczowych funkcji OPNsense:





- Firewall i NAT**: OPNsense zapewnia zaawansowaną funkcję stateful firewall z filtrowaniem stanowym, a także funkcje translacji sieciowej Address (NAT).





- DNS/DHCP**: OPNsense można skonfigurować do zarządzania usługami DNS i DHCP w sieci. Może działać jako serwer DHCP, ale może być również używany jako resolver DNS dla maszyn w sieci lokalnej. Dnsmasq jest również domyślnie zintegrowany.





- VPN**: OPNsense obsługuje kilka protokołów VPN, w tym IPsec, OpenVPN i WireGuard, umożliwiając bezpieczne połączenia w celu zdalnego dostępu do mobilnych stacji roboczych lub połączenia między lokalizacjami.





- Serwer proxy**: OPNsense zawiera internetowy serwer proxy do kontrolowania i filtrowania dostępu do Internetu. Może być również używany do filtrowania treści i zarządzania dostępem do sieci.





- Zarządzanie przepustowością (QoS)**: OPNsense oferuje funkcje zarządzania jakością usług (QoS) w celu nadawania priorytetów ruchowi sieciowemu i lepszego zarządzania przepustowością sieci.





- Captive portal**: ta funkcja umożliwia zarządzanie dostępem użytkowników do sieci za pośrednictwem strony uwierzytelniania (baza lokalna, vouchery itp.). Jest to funkcja powszechnie stosowana w publicznych sieciach Wi-Fi.





- IDS/IPS**: OPNsense integruje Suricata, aby oferować funkcje wykrywania i zapobiegania włamaniom (IDS/IPS) w celu ochrony sieci przed atakami.





- Wysoka dostępność (CARP)**: OPNsense obsługuje CARP (*Common Address Redundancy Protocol*) w celu zapewnienia wysokiej dostępności między wieloma zaporami OPNsense, zapewniając, że usługa pozostanie aktywna nawet w przypadku awarii sprzętu.





- Raportowanie i monitorowanie**: OPNsense zapewnia narzędzia do raportowania i monitorowania w czasie rzeczywistym w celu śledzenia wydajności sieci (z NetFlow) i wykrywania potencjalnych problemów, dzięki tworzeniu dzienników. Obejmuje to również grafikę. Narzędzie Monit jest zintegrowane z OPNsense i umożliwia nadzór nad samym firewallem.



### B. Dodatkowe pakiety



To tylko przegląd funkcji oferowanych przez OPNsense. Ponadto **katalog pakietów** dostępny z poziomu administracyjnego OPNsense Interface pozwala **wzbogacić zaporę sieciową o dodatkowe funkcje**. Obejmują one klienta ACME, agenta Wazuh, usługę NTP Chrony i Caddy jako odwrotne proxy.



![Image](assets/fr/051.webp)



## III. Wymagania wstępne OPNsense



Przede wszystkim musisz zdecydować, gdzie zainstalujesz OPNsense. Istnieje kilka możliwych rozwiązań, w tym instalacja na:





- Hiperwizor jako maszyna wirtualna, czy to Hyper-V, Proxmox, VMware ESXi itp.
- Maszyna jako system *bare-metal*. Może to być mini PC działający jako firewall.



Można również zakupić **urządzenie OPNsense do montażu w szafie rack** za pośrednictwem naszego sklepu internetowego.



Należy wziąć pod uwagę zasoby sprzętowe wymagane do uruchomienia OPNsense. Jest to szczegółowo opisane na [tej stronie dokumentacji] (https://docs.opnsense.org/manual/hardware.html).



**Minimalne i zalecane zasoby do produkcji:**



| Caractéristiques | Minimum | Recommandation |
| --- | --- | --- |
| Processeur | 1 GHz - 2 cœurs | 1.5 GHz - Multi-coeurs |
| Mémoire vive (RAM) | 2 Go | 8 Go |
| Espace de stockage pour le système | Disque dur, disque SSD ou carte SD (4 Go) | 120 Go en SSD |

Wreszcie, **wymagane zasoby zależą przede wszystkim od liczby zarządzanych połączeń**, a zatem od **wymaganej przepustowości**. Ponadto należy **pamiętać o usługach, które będą aktywowane i używane** (proxy, wykrywanie włamań itp.), ponieważ mogą one wymagać dużej ilości procesora i/lub pamięci RAM.



Potrzebny będzie również obraz ISO instalacji OPNsense, który można pobrać z [oficjalnej strony](https://opnsense.org/download/). W przypadku instalacji na maszynie wirtualnej wybierz "**dvd**" jako typ obrazu, aby uzyskać obraz ISO (i zrób z nim, co chcesz...). W przypadku instalacji za pomocą bootowalnego klucza USB, wybierz opcję "**vga**", aby uzyskać plik "**.img**".



![Image](assets/fr/048.webp)



Będziesz także potrzebować komputera do administrowania i testowania OPNsense.



## IV. Konfiguracja docelowa



Naszym celem jest





- Utwórz wewnętrzną sieć wirtualną (192.168.10.0/24 - LAN)**, która może uzyskać dostęp do Internetu za pośrednictwem zapory OPNsense. Do użytku produkcyjnego może to być sieć lokalna, kablowa i/lub Wi-Fi.
- Aktywuj i skonfiguruj NAT**, aby maszyny wirtualne w wewnętrznej sieci wirtualnej mogły uzyskać dostęp do Internetu
- Aktywacja i konfiguracja serwera DHCP w OPNsense** w celu dystrybucji konfiguracji IP do przyszłych maszyn podłączonych do wewnętrznej sieci wirtualnej
- Skonfiguruj zaporę**, aby zezwalała tylko na wychodzące przepływy LAN do WAN w HTTP (80) i HTTPS (443).
- Skonfiguruj zaporę**, aby zezwolić wirtualnej sieci LAN na używanie OPNsense jako resolvera DNS (53).



Jeśli korzystasz z platformy Hyper-V, otrzymasz następującą reprezentację:



![Image](assets/fr/033.webp)



## V. Instalacja zapory sieciowej OPNsense



### A. Przygotowanie rozruchowego klucza USB



Pierwszym krokiem jest przygotowanie nośnika instalacyjnego: **rozruchowego klucza USB z OPNsense**. Jest to oczywiście opcjonalne, jeśli pracujesz w środowisku wirtualnym, ale w każdym przypadku musisz pobrać instalacyjny obraz ISO OPNsense.



Po pobraniu otrzymasz **archiwum zawierające obraz w formacie ".img "**. Możesz **utworzyć bootowalną pamięć USB** za pomocą różnych aplikacji, w tym **balenaEtcher**: bardzo prosty w użyciu. Co więcej, aplikacja rozpozna obraz w archiwum, więc nie trzeba go wcześniej dekompresować.





- [Pobierz balenaEtcher](https://etcher.balena.io/)



Po zainstalowaniu aplikacji wybierz obraz, klucz USB, a następnie kliknij przycisk "Flash! Poczekaj chwilę.



![Image](assets/fr/049.webp)



Teraz możesz przystąpić do instalacji.



### B. Instalacja systemu OPNsense



Uruchom maszynę hostującą OPNsense. Powinieneś zobaczyć stronę powitalną podobną do tej poniżej. Przez kilka sekund w oknie będzie widoczny pokazany ekran. Pozwól procesowi działać...



![Image](assets/fr/019.webp)



Obraz OPNsense jest ładowany do urządzenia, dzięki czemu dostęp do systemu można uzyskać w trybie "**live**", tj. tymczasowo przechowywanym w pamięci.



![Image](assets/fr/025.webp)



Następnie pojawi się Interface podobny do tego poniżej. Zaloguj się za pomocą loginu "**installer**" i hasła "**opnsense**". Należy pamiętać, że klawiatura jest w tej chwili **QWERTY**. W tym momencie **rozpoczniemy proces instalacji OPNsense**.



![Image](assets/fr/026.webp)



Na ekranie pojawi się nowy kreator. Pierwszym krokiem jest wybranie układu klawiatury odpowiadającego konfiguracji. W przypadku klawiatury AZERTY wybierz z listy opcję "**French (accent keys)**", a następnie kliknij dwukrotnie przycisk**.



![Image](assets/fr/027.webp)



Drugim krokiem jest wybór zadania do wykonania. W tym przypadku przeprowadzimy instalację przy użyciu **systemu plików ZFS**. Ustawiamy się w wierszu "**Install (ZFS)**" i zatwierdzamy klawiszem **Enter**.



![Image](assets/fr/028.webp)



W trzecim kroku wybierz "**stripe**", ponieważ nasza maszyna jest wyposażona w **tylko jeden dysk**: nie ma możliwości redundancji, aby zabezpieczyć pamięć zapory i jej dane. Jest to szczególnie istotne w przypadku instalacji na fizycznej maszynie w celu ochrony przed awarią sprzętową dysku, zgodnie z zasadą RAID.



![Image](assets/fr/029.webp)



W czwartym kroku wystarczy nacisnąć **Enter**, aby potwierdzić.



![Image](assets/fr/030.webp)



Na koniec potwierdź, wybierając "**Tak**", a następnie naciskając przycisk **Enter**.



![Image](assets/fr/031.webp)



Teraz będziesz musiał poczekać, aż OPNsense zostanie zainstalowany... Proces ten trwa około 5 minut.



![Image](assets/fr/032.webp)



Po zakończeniu instalacji możemy zmienić hasło "**root**" przed ponownym uruchomieniem systemu. Wybierz "**Root Password**", naciśnij **Enter** i wprowadź dwukrotnie hasło "**root**".



![Image](assets/fr/020.webp)



Na koniec wybierz "**Complete Install**" i naciśnij **Enter**. Skorzystaj z okazji, aby **wysunąć dysk z napędu DVD maszyny wirtualnej**. W ustawieniach maszyny wirtualnej można również ustawić pierwszy rozruch z dysku.



![Image](assets/fr/021.webp)



Maszyna wirtualna uruchomi się ponownie i załaduje system OPNsense z dysku, ponieważ właśnie go zainstalowaliśmy. Zaloguj się za pomocą konta "root" w konsoli i nowego hasła (w przeciwnym razie domyślne hasło to "**opnsense**").



### D. Łączenie interfejsów sieciowych



Pojawi się ekran pokazany poniżej. Wybierz "**1**" i naciśnij **Enter**, aby powiązać karty sieciowe urządzenia z interfejsami OPNsense.



![Image](assets/fr/022.webp)



Najpierw kreator poprosi o skonfigurowanie agregacji łączy i sieci VLAN. Podaj "**n**", aby odmówić i za każdym razem potwierdź swoją odpowiedź przyciskiem **Enter**. Następnie należy przypisać dwa interfejsy "**hn0**" i "**hn1**" do sieci **WAN** i **LAN**. Zasadniczo "**hn0**" odpowiada sieci WAN, a drugi Interface sieci LAN.



Oto jak to działa:



![Image](assets/fr/023.webp)



Mamy teraz:





- Interface **LAN** powiązany z kartą sieciową "**hn1**" i z domyślnym IP OPNsense Address, tj. **192.168.1.1/24**.
- Interface **WAN** powiązany z kartą sieciową "**hn0**" i z IP Address pobranym przez **DHCP** w sieci lokalnej (dzięki naszemu zewnętrznemu przełącznikowi wirtualnemu).



Domyślnie administracja OPNsense Interface jest dostępna tylko z sieci LAN Interface, z oczywistych względów bezpieczeństwa. Dlatego w celu administrowania należy połączyć się z siecią LAN zapory Interface. Jeśli nie jest to możliwe, można tymczasowo administrować OPNsense z sieci WAN. Wymaga to wyłączenia funkcji zapory.



Aby to zrobić, przełącz się do trybu powłoki za pomocą opcji "**8**" i uruchom następujące polecenie:



```
pfctl -d
```



![Image](assets/fr/024.webp)



### E. Dostęp do systemu zarządzania OPNsense Interface



Dostęp do OPNsense Administration Interface można uzyskać przez HTTPS, używając IP Address sieci LAN** Interface (lub WAN). Przeglądarka wyświetli stronę logowania. Zaloguj się przy użyciu wybranego wcześniej konta "root" i hasła.



![Image](assets/fr/034.webp)



Poczekaj kilka sekund... Zostaniesz poproszony o wykonanie podstawowej konfiguracji za pomocą kreatora. Kliknij "**Next**", aby kontynuować.



![Image](assets/fr/036.webp)



Pierwszym krokiem jest zdefiniowanie nazwy hosta, nazwy domeny, wybranie języka i zdefiniowanie serwerów DNS, które będą używane do rozpoznawania nazw. Pozostawienie opcji "**Enable Resolver**" pozwoli na użycie firewalla jako resolvera DNS, co będzie przydatne dla maszyn w naszej wirtualnej sieci LAN.



![Image](assets/fr/037.webp)



Przejdź do następnego kroku. Kreator daje możliwość **zdefiniowania serwera NTP do synchronizacji daty i godziny**, chociaż domyślnie serwery są już skonfigurowane. Ponadto konieczne jest wybranie strefy czasowej odpowiadającej lokalizacji geograficznej (chyba że masz specjalne wymagania).



![Image](assets/fr/038.webp)



Następnie nadchodzi ważny krok: **konfiguracja Interface WAN**. Obecnie jest on skonfigurowany w DHCP i pozostanie w tym trybie konfiguracji, chyba że chcesz ustawić statyczne IP Address.



![Image](assets/fr/039.webp)



Na stronie konfiguracji Interface WAN należy odznaczyć opcję "**Blokuj dostęp do sieci prywatnych przez WAN**", jeśli sieć po stronie WAN używa adresacji prywatnej. Prawdopodobnie będzie to miało miejsce w przypadku korzystania z laboratorium, co może uniemożliwić dostęp do Internetu.



![Image](assets/fr/040.webp)



Następnie możesz **zdefiniować hasło "root "**, ale jest to opcjonalne, ponieważ już to zrobiliśmy.



![Image](assets/fr/041.webp)



Kontynuuj do końca, aby zainicjować przeładowanie konfiguracji. Jeśli chcesz kontynuować przejmowanie kontroli za pośrednictwem sieci WAN, uruchom ponownie powyższe polecenie po zakończeniu tego procesu.



![Image](assets/fr/042.webp)



To wszystko!



![Image](assets/fr/035.webp)



### E. Konfiguracja DHCP



Naszym celem jest wykorzystanie serwera OPNsense DHCP do dystrybucji adresów IP w wirtualnej sieci LAN. Aby to zrobić, musimy uzyskać dostęp do tej lokalizacji menu:



```
Services > ISC DHCPv4 > [LAN]
```



**Jak widać, DHCP jest już domyślnie włączony w sieci LAN ** Jeśli nie jesteś zainteresowany tą usługą, powinieneś ją wyłączyć. Chociaż jest już włączona i chcemy z niej korzystać, ważne jest, aby przejrzeć jej konfigurację.



W razie potrzeby można zmienić zakres adresów IP do dystrybucji: **192.168.10.10** do **192.168.10.245**, w zależności od bieżących ustawień.



![Image](assets/fr/046.webp)



Widzimy również, że pola "**Serwery DNS**", "**Brama**", "**Nazwa domeny**" itp. są domyślnie puste. W rzeczywistości istnieje automatyczne dziedziczenie niektórych opcji i wartości domyślnych dla tych różnych pól. Na przykład, dla serwera DNS, IP Address sieci LAN Interface będzie dystrybuowany, umożliwiając wykorzystanie zapory OPNsense jako resolwera DNS.



W razie potrzeby zapisz konfigurację po wprowadzeniu zmian.



![Image](assets/fr/047.webp)



Aby przetestować serwer DHCP, należy podłączyć urządzenie do sieci LAN zapory.



To urządzenie musi uzyskać adres IP Address z serwera OPNsense DHCP, a nasze urządzenie musi mieć dostęp do sieci. Dostęp do Internetu musi działać. Pamiętaj, że jeśli wyłączyłeś funkcję zapory, aby uzyskać dostęp do OPNsense z sieci WAN, spowoduje to wyłączenie NAT, uniemożliwiając dostęp do sieci.



**Uwaga**: aktualnie wydane dzierżawy DHCP są widoczne z poziomu OPNsense administration Interface. W tym celu należy przejść do następującej lokalizacji: **Services > ISC DHCPv4 > Leases**.



![Image](assets/fr/045.webp)



### F. Konfigurowanie reguł NAT i zapory sieciowej



Dobrą wiadomością jest to, że możemy teraz uzyskać dostęp do administracji OPNsense Interface z sieci LAN.



```
https://192.168.1.10
```



Po zalogowaniu się do OPNsense, odkryjmy konfigurację NAT. Przejdź do tej lokalizacji: **Firewall > NAT > Outbound**. Tutaj można wybrać pomiędzy automatycznym (domyślnym) i ręcznym tworzeniem reguł wychodzących NAT.



Wybierz tryb automatyczny za pomocą opcji "**Automatyczne generowanie wychodzących reguł NAT**" i kliknij "**Zapisz**" (w zasadzie ta konfiguracja jest już aktywna). W trybie automatycznym OPNsense samodzielnie tworzy regułę NAT dla każdej z sieci.



![Image](assets/fr/043.webp)



Na razie wszystkie komputery podłączone do wirtualnej sieci LAN "**192.168.10.0/24**" mogą uzyskać dostęp do Internetu bez ograniczeń. Naszym celem jest jednak ograniczenie dostępu do sieci WAN do protokołów HTTP i HTTPS, a także DNS w sieci LAN Interface firewalla.



Musimy więc utworzyć reguły zapory sieciowej... Przeglądamy menu w następujący sposób: **Firewall > Rules > LAN**.



**Domyślnie istnieją dwie reguły autoryzujące cały wychodzący ruch LAN, w IPv4 i IPv6**. Wyłącz te dwie reguły, klikając strzałkę Green po lewej stronie, na początku każdej linii.



Następnie utwórz trzy nowe reguły, aby autoryzować **sieć LAN** (tj. "**sieć LAN**") do:





- dostęp do wszystkich miejsc docelowych za pomocą **HTTP**.
- dostęp do wszystkich miejsc docelowych za pomocą **HTTPS**.
- zażądać **OPNsense** na swoim **Interface LAN** (tj. "**LAN Address**"), poprzez **protokół DNS** (oznacza to użycie firewalla jako DNS), w przeciwnym razie autoryzować resolver DNS poprzez jego IP Address.



Daje to następujący wynik:



![Image](assets/fr/044.webp)



Pozostaje tylko kliknąć "**Zastosuj zmiany**", aby przełączyć nowe reguły zapory na wersję produkcyjną. **Należy pamiętać, że wszystkie przepływy, które nie są wyraźnie autoryzowane, będą domyślnie blokowane



Urządzenie LAN może uzyskać dostęp do Internetu za pomocą protokołów HTTP i HTTPS. Wszystkie inne protokoły zostaną zablokowane.



![Image](assets/fr/018.webp)



## IV. Wnioski



Postępując zgodnie z tym przewodnikiem, będziesz mógł zainstalować OPNsense i od razu rozpocząć pracę. OPNsense oferuje szeroką gamę funkcji do skutecznego zabezpieczania i zarządzania ruchem sieciowym i nadaje się do użytku w środowiskach profesjonalnych.



Ta instalacja to dopiero początek: nie krępuj się eksplorować menu i konfigurować innych funkcji, aby dostosować OPNsense do swoich potrzeb.