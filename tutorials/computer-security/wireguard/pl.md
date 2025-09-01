---
name: WireGuard
description: Konfiguracja WireGuard VPN na Debian i Windows
---
![cover](assets/cover.webp)



___



*Ten samouczek jest oparty na oryginalnej treści autorstwa Floriana BURNELA opublikowanej na stronie [IT-Connect](https://www.it-connect.fr/). Licencja [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). W oryginalnym tekście mogły zostać wprowadzone zmiany



___



## I. Prezentacja



W tym samouczku dowiemy się, jak skonfigurować VPN w oparciu o WireGuard, bezpłatne rozwiązanie VPN typu open source, które zwiększa wydajność bez zaniedbywania bezpieczeństwa.



WireGuard jest stosunkowo nowym rozwiązaniem, dostępnym jako stabilne wydanie od marca 2020 roku i ma zaszczyt być zintegrowanym bezpośrednio z **jądrem Linux od wersji 5.6**. Nie przeszkadza to jednak w dostępie do niego ze starszych dystrybucji Linuksa, które używają innej wersji jądra. W porównaniu z rozwiązaniami takimi jak OpenVPN i IPSec, WireGuard jest prostszy w użyciu i znacznie szybszy, jak zobaczymy na końcu tego artykułu.



Kilka kluczowych punktów dotyczących WireGuard:





- Prosty, lekki i bardzo wydajny!
- Obsługa wyłącznie protokołu UDP (co może być wadą podczas przechodzenia przez niektóre zapory sieciowe)
- Działa w modelu peer-to-peer, a nie klient-serwer
- Uwierzytelnianie za pomocą klucza Exchange, na tej samej zasadzie co SSH z kluczami prywatnymi/publicznymi
- Wykorzystanie kilku algorytmów: symetrycznego szyfrowania za pomocą ChaCha20, uwierzytelniania wiadomości za pomocą Poly1305, a także innych, takich jak Curve25519, BLAKE2 i SipHash24
- Obsługa protokołów IPv4 i IPv6
- Wieloplatformowość: Windows, Linux, BSD, macOS, Android, iOS, OpenWRT (i zaimplementowana w ProtonVPN)
- Tylko 4000 linii kodu, w porównaniu z setkami tysięcy w przypadku innych rozwiązań



Jeśli chodzi o część kryptograficzną, różne stosowane algorytmy są wybierane ręcznie, kontrolowane na kilka sposobów i badane przez badaczy bezpieczeństwa specjalizujących się w tej dziedzinie.



Oficjalna strona projektu: [wireguard.com](https://www.wireguard.com/)



Czy po przeczytaniu tego wstępu jesteś przekonany do tego rozwiązania? Pozostaje tylko czytać dalej!



## II. Schemat Lab WireGuard



Zanim przedstawię moje laboratorium do konfiguracji WireGuard, powinieneś wiedzieć, że możesz sobie wyobrazić **użycie WireGuard do połączenia dwóch zdalnych infrastruktur**, ale także do **podłączenia zdalnego klienta do infrastruktury, takiej jak sieć firmowa lub sieć domowa**. Jest to w tym samym duchu, co w przypadku OpenVPN, jak widzieliśmy ostatnio w samouczku "[OpenVPN na Synology](https://www.it-connect.fr/tuto-vpn-configurer-openvpn-server-sur-un-nas-synology/)".



Jeśli WireGuard nie jest skonfigurowany bezpośrednio na routerze lub zaporze sieciowej, co jest możliwe w przypadku OpenWRT, konieczne będzie skonfigurowanie przekierowania portów, aby przepływ docierał do pary WireGuard.



![Image](assets/fr/034.webp)



Teraz opowiem ci o moim laboratorium i o tym, co dzisiaj przygotujemy.



Zamierzam użyć maszyny Debian 11 jako serwera WireGuard i klienta Windows jako klienta WireGuard VPN. Chociaż mówienie o relacji klient-serwer jest nieco mylące, ponieważ **WireGuard działa w modelu "peer-to-peer "**. To trochę błędne określenie, gdy próbujesz skonfigurować połączenie "klient-serwer". Powiedzmy zamiast tego, że będę miał dwie pary lub **dwa punkty połączenia WireGuard**, jeśli wolisz: jeden pod Debianem 11, a drugi pod Windows.



Te dwie pary mogą komunikować się ze sobą w obu kierunkach, co oznacza, że z mojej maszyny Windows mogę uzyskać dostęp do zdalnej sieci LAN maszyny Debian 11 i odwrotnie: wszystko zależy od konfiguracji tunelu i zapory sieciowej urządzenia równorzędnego WireGuard.



W tym przykładzie skupię się na następującym przypadku: **z mojego Windows Peer 1 podłączonego do mojej sieci domowej, chcę uzyskać dostęp do sieci firmowej, aby uzyskać dostęp do serwerów firmy za pośrednictwem tunelu WireGuard VPN**. Daje to następujący schemat:



![Image](assets/fr/035.webp)



Pod względem adresów IP daje to:





- Sieć domowa**: 192.168.1.0/24
- Sieć firmowa**: 192.168.100.0/24
- Sieć tunelowa WireGuard**: 192.168.110.0/24


+ IP Address peera 1 (Windows) w tunelu: 192.168.110.2/24


+ IP Address peera 2 (Debian) w tunelu: 192.168.110.121/24



To już wszystko! Przejdźmy do konfiguracji!



**Uwaga: domyślnie WireGuard działa w trybie UDP na **porcie 51820**.



## III Instalacja i konfiguracja serwera WireGuard



W tym samouczku będę używał terminów "klient" dla maszyny z systemem Windows i "serwer" dla maszyny z Debianem, ponieważ mimo że jest to peer-to-peer, wydaje się to bardziej znaczące.



### A. Instalacja WireGuard na Debianie 11



Pakiet instalacyjny WireGuard jest dostępny w oficjalnych repozytoriach Debiana 11, więc wszystko, co musimy zrobić, to zaktualizować pamięć podręczną pakietów i zainstalować go:



```
sudo apt-get update
```



```
sudo apt-get install wireguard
```



![Image](assets/fr/022.webp)



Zainstalowana zostanie część serwera WireGuard wraz z różnymi narzędziami dającymi dostęp do przydatnych poleceń do zarządzania konfiguracją.



### B. Instalacja Interface WireGuard



Używając **polecenia "wg "** musimy generate klucz prywatny i klucz publiczny: niezbędne do uwierzytelniania między dwiema parami, tj. serwerem i klientem (który również będzie potrzebował pary kluczy).



Utworzymy klucz prywatny "**/etc/wireguard/wg-private.key**" i klucz publiczny "**/etc/wireguard/wg-public.key**" za pomocą tej sekwencji poleceń:



```
wg genkey | sudo tee /etc/wireguard/wg-private.key | wg pubkey | sudo tee /etc/wireguard/wg-public.key
```



![Image](assets/fr/023.webp)



Wartość klucza publicznego zostanie zwrócona w konsoli. W pliku konfiguracyjnym WireGuard musimy **dodać wartość naszego klucza prywatnego**. Aby pobrać tę wartość, wprowadź poniższe polecenie i skopiuj wartość:



```
sudo cat /etc/wireguard/wg-private.key
```



Nadszedł czas, aby utworzyć plik konfiguracyjny w "**/etc/wireguard/**". Na przykład, możemy nazwać ten plik "**wg0.conf**", jeśli uważamy, że sieć Interface powiązana z WireGuard będzie "wg0", na tej samej zasadzie co "eth0", na przykład.



```
sudo nano /etc/wireguard/wg0.conf
```



W tym pliku musimy najpierw dodać następującą zawartość (wrócimy do jej uzupełnienia później):



```
[Interface]
Address = 192.168.110.121/24
SaveConfig = true
ListenPort = 51820
PrivateKey = <clé privée du serveur>
```



Sekcja `[Interface]` jest używana do zadeklarowania części serwera. Oto kilka informacji:





- Address**: adres IP Address urządzenia Interface WireGuard w tunelu VPN (inna podsieć niż zdalna sieć LAN)
- SaveConfig**: konfiguracja jest przechowywana (i chroniona) tak długo, jak długo Interface jest aktywny
- ListenPort**: Port nasłuchiwania WireGuard. W tym przypadku domyślnym portem jest 51820, ale możesz go dostosować
- PrivateKey**: wartość klucza prywatnego naszego serwera (*wg-private.key*)



Zapisz plik i zamknij go. Za pomocą polecenia "**wg-quick**" możemy uruchomić Interface, określając jego nazwę (wg0, ponieważ plik nosi nazwę wg0.conf):



```
sudo wg-quick up wg0
```



Jeśli wyświetlisz adresy IP serwera Debian 11, zobaczysz nowy Interface o nazwie "wg0" z adresem IP Address zdefiniowanym w pliku konfiguracyjnym:



```
ip a
```



![Image](assets/fr/027.webp)



W tym samym duchu możemy wyświetlić konfigurację Interface "wg0" za pomocą polecenia "wg show":



```
sudo wg show wg0
```



![Image](assets/fr/024.webp)



Na koniec musimy aktywować automatyczne uruchamianie naszego Interface wg0 WireGuard:



```
sudo systemctl enable wg-quick@wg0.service
```



Na razie pominiemy konfigurację serwera WireGuard.



### C. Włącz przekierowanie IP



Aby nasz Debian 11 mógł **przekierowywać pakiety między różnymi sieciami (jak router)**, tj. między siecią VPN a siecią lokalną, musimy włączyć [IP Forwarding](https://www.it-connect.fr/activer-lip-forwarding-sous-linux-ipv4ipv6/). Domyślnie funkcja ta jest wyłączona.



Zmodyfikuj ten plik konfiguracyjny:



```
sudo nano /etc/sysctl.conf
```



Dodaj następującą dyrektywę na końcu pliku i zapisz:



```
net.ipv4.ip_forward = 1
```



To wszystko.



### D. Włącz maskaradę IP



Aby nasz serwer mógł poprawnie kierować pakiety i aby zdalna sieć LAN była dostępna dla komputera z systemem Windows, musimy aktywować Maskaradę IP na naszym serwerze Debian. Jest to rodzaj aktywacji NAT. Zamierzam przeprowadzić tę konfigurację na linuksowym firewallu poprzez UFW, do którego jestem przyzwyczajony ([ufw tutorial on Debian](https://www.it-connect.fr/configurer-un-pare-feu-local-sous-debian-11-avec-ufw/)).



Jeśli nie masz jeszcze UFW i chcesz go skonfigurować (możesz też użyć Nftables), zacznij od zainstalowania:



```
sudo apt install ufw
```



Przede wszystkim musisz włączyć SSH, aby nie stracić kontroli nad zdalnym serwerem (dostosuj numer portu):



```
sudo ufw allow 22/tcp
```



Port 51820 w UDP musi być również autoryzowany, ponieważ używamy go dla WireGuard (ponownie, dostosuj numer portu):



```
sudo ufw allow 51820/udp
```



Następnie będziemy kontynuować konfigurację, aby włączyć maskaradę IP. Aby to zrobić, musimy pobrać nazwę Interface podłączonego do sieci lokalnej. Jeśli nie znasz nazwy, uruchom "ip a", aby zobaczyć nazwę karty. W moim przypadku jest to karta "**ens192**".



![Image](assets/fr/036.webp)



Wykorzystamy te informacje. Edytuj następujący plik:



```
sudo nano /etc/ufw/before.rules
```



Dodaj te linie na końcu pliku, aby **włączyć maskaradę IP na Interface ens192** (dostosuj nazwę Interface) w łańcuchu POSTROUTING tabeli NAT naszej lokalnej zapory ogniowej:



```
# NAT - IP masquerade
*nat
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING -o ens192 -j MASQUERADE

# End each table with the 'COMMIT' line or these rules won't be processed
COMMIT
```



Zdjęcie przedstawia:



![Image](assets/fr/037.webp)



Pozostaw ten plik konfiguracyjny otwarty i przejdź do następnego kroku. 😉



### E. Konfiguracja zapory sieciowej Linux dla WireGuard



Nadal w tym samym pliku konfiguracyjnym zadeklarujemy sieć korporacyjną "192.168.100.0/24", abyśmy mogli się z nią skontaktować. Oto dwie reguły, które należy dodać (najlepiej po sekcji "*# ok icmp code for FORWARD*", aby zgrupować reguły razem):



```
# autoriser le forwarding pour le réseau distant de confiance (+ le réseau du VPN)
-A ufw-before-forward -s 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -s 192.168.110.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.110.0/24 -j ACCEPT
```



Jeśli chcesz autoryzować tylko jednego hosta, na przykład "192.168.100.11", jest to łatwe:



```
-A ufw-before-forward -s 192.168.100.11/32 -j ACCEPT
-A ufw-before-forward -d 192.168.100.11/32 -j ACCEPT
```



Teraz można zapisać plik i zamknąć go. Pozostaje tylko aktywować UFW i ponownie uruchomić usługę, aby zastosować nasze zmiany:



```
sudo ufw enable
```



```
sudo systemctl restart ufw
```



Pierwsza część konfiguracji serwera Debian została zakończona.



## IV. Klient WireGuard dla systemu Windows



Klient WireGuard jest dostępny dla systemów Windows, macOS, Android itp. To świetna wiadomość. Wszystkie pliki do pobrania są dostępne na tej stronie: [WireGuard Client](https://www.wireguard.com/install/). W tym przykładzie skonfiguruję klienta w systemie Windows. Aby skonfigurować klienta WireGuard w systemie Linux, postępuj zgodnie z tą samą zasadą, co w przypadku tworzenia pliku wg0.conf na komputerze z Debianem (bez całego NAT itp.).



### A. Instalacja klienta WireGuard dla systemu Windows



Po pobraniu pliku wykonywalnego lub pakietu MSI instalacja jest prosta: wystarczy uruchomić instalator i... voila, gotowe! 🙂



![Image](assets/fr/038.webp)



### B. Utwórz profil WireGuard



Zacznij od otwarcia oprogramowania, aby utworzyć nowy tunel. Aby to zrobić, kliknij strzałkę po prawej stronie przycisku "**Dodaj tunel**" i kliknij przycisk "**Dodaj pusty tunel**".



![Image](assets/fr/028.webp)



Otworzy się okno konfiguracji. Za każdym razem, gdy tworzona jest nowa konfiguracja tunelu, WireGuard generuje parę kluczy prywatny/publiczny specyficzną dla tej konfiguracji. **W tej konfiguracji musimy zadeklarować "peer", czyli zdalny serwer:



```
[Interface]
PrivateKey = <la clé privée du PC>
```



Musimy uzupełnić tę konfigurację, w szczególności zadeklarować IP Address na tym Interface (*Address*), ale także zadeklarować zdalny serwer WireGuard za pomocą bloku [Peer]. Poniższy obrazek powinien przypominać plik konfiguracyjny, który utworzyliśmy po stronie serwera Linux.



Zacznijmy od bloku `[Interface]`, dodając IP Address "**192.168.110.2**"; pamiętaj, że serwer ma IP Address "**192.168.110.121**" w tym segmencie sieci. Daje to:



```
[Interface]
PrivateKey = <la clé privée du PC>
Address = 192.168.110.2/24
```



Następnie musimy zadeklarować blok "Peer" z trzema właściwościami, w wyniku czego otrzymamy następującą konfigurację:



```
[Peer]
PublicKey = 1D/Gf5yd3hUDoFyYQ3P1zayBHUJhJZq+k6Sv03HnJCQ=
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
Endpoint = <ip-serveur-debian>:51820
```



Na zdjęciach:



![Image](assets/fr/029.webp)



**Kilka wyjaśnień na temat bloku [Peer]:





- PublicKey**: jest to klucz publiczny serwera WireGuard Debian 11 (jego wartość można uzyskać za pomocą polecenia "*sudo wg*")
- AllowedIPs**: są to adresy IP / podsieci dostępne za pośrednictwem tej sieci WireGuard VPN, w tym przypadku podsieci specyficznej dla mojego WireGuard VPN (*192.168.110.0/24*) i mojej zdalnej sieci LAN (*192.168.100.0/24*)
- Punkt końcowy**: jest to adres IP Address hosta Debian 11, ponieważ jest to nasz punkt połączenia WireGuard (musisz określić publiczny adres IP Address)



Na koniec wprowadź nazwę w polu "**Name**" (bez spacji) oraz skopiuj i wklej klucz publiczny klienta, ponieważ będziemy musieli zadeklarować go na serwerze. Klikamy na "**Register**".



### C. Deklaracja klienta na serwerze WireGuard



Nadszedł czas, aby powrócić do serwera Debian, aby zadeklarować "**Peer**", czyli nasz komputer z systemem Windows, w konfiguracji WireGuard. Przede wszystkim musimy **zatrzymać Interface "wg0"**, aby zmodyfikować jego konfigurację:



```
sudo wg-quick down wg0
# ou
sudo wg-quick down /etc/wireguard/wg0.conf
```



Następnie zmodyfikuj wcześniej utworzony plik konfiguracyjny:



```
sudo nano /etc/wireguard/wg0.conf
```



W tym pliku, po bloku `[Interface]`, musimy zadeklarować blok `[Peer]`:



```
[Peer]
PublicKey = 0i2Pg8nwDW2j7yOG09ZXht18o8l8Erb9Y5F4xyAyQV8=
AllowedIPs = 192.168.110.2/32
```



Ten blok [Peer] zawiera klucz publiczny komputera z systemem Windows 10 (**PublicKey**) i adres IP Address komputera Interface (**AllowedIPs**): serwer będzie komunikował się w tym tunelu WireGuard tylko w celu skontaktowania się z klientem Windows, stąd wartość "**192.168.110.2/32**".



Pozostaje tylko zapisać plik (*CTRL+O następnie Enter następnie CTRL+X przez Nano*). Uruchom ponownie Interface "wg0":



```
sudo wg-quick up wg0
# ou
sudo wg-quick up /etc/wireguard/wg0.conf
```



Aby sprawdzić, czy deklaracja peer działa, można użyć tego polecenia:



```
sudo wg show
```



Gdy zdalny host skonfiguruje połączenie WireGuard, jego adres IP Address zostanie przeniesiony do wartości "endpoint".



![Image](assets/fr/033.webp)



Na koniec zabezpieczymy pliki konfiguracyjne, aby ograniczyć dostęp roota:



```
sudo chmod 600 /etc/wireguard/ -R
```



### D. Pierwsze połączenie WireGuard



Teraz, gdy konfiguracja jest gotowa, możemy zainicjować ją z komputera z systemem Windows. Aby to zrobić, w kliencie "**WireGuard**" kliknij przycisk "**Activate**": połączenie **zmieni się z "Off" na "On "**, ale to nie znaczy, że będzie działać. Wszystko zależy od tego, czy konfiguracja jest prawidłowa. **Gdy połączenie zostanie ustanowione, nasze dwie maszyny będą komunikować się za pośrednictwem Interface WireGuard skonfigurowanego po każdej stronie!



![Image](assets/fr/030.webp)



W przypadku wystąpienia problemu będzie to widoczne w zakładce "**Logbook**". Dwa hosty będą regularnie wysyłać pakiety Exchange w celu sprawdzenia stanu połączenia, stąd komunikaty "*Receiving keepalive packet from peer 1*".



![Image](assets/fr/031.webp)



Jeśli zakładka "**Dziennik**" WireGuard wyświetla komunikat podobny do poniższego, należy sprawdzić, czy klucze publiczne zadeklarowane po obu stronach są prawidłowe.



```
Handshake for peer 1 (<ip>:51820) did not complete after 5 seconds, retrying (try 2)
```



Z mojego zdalnego komputera mogę pingować IP Address mojego Interface WireGuard po stronie serwera, a także hosta w mojej zdalnej sieci LAN.



![Image](assets/fr/032.webp)



### E. Wydajność: OpenVPN vs WireGuard



Z mojego zdalnego komputera podłączonego do WireGuard VPN udało mi się uzyskać dostęp do serwera plików i przesłać plik za pośrednictwem [SMB](https://www.it-connect.fr/le-protocole-smb-pour-les-debutants/), aby sprawdzić szybkość transferu. **Dzięki WireGuard osiągam maksymalnie około 45 Mb/s, co jest świetne, ponieważ korzystam z WiFi



![Image](assets/fr/025.webp)



W tych samych warunkach, ale tym razem za pośrednictwem połączenia OpenVPN (w UDP), przy tej samej operacji, przepustowość jest zupełnie inna: około 3 MB/s. Różnica jest oczywista!



![Image](assets/fr/026.webp)



Jest to interesujące, ponieważ jeśli na przykład przełączysz się z połączenia WiFi na połączenie 4G/5G, ponowne połączenie będzie tak szybkie, że przerwa nie będzie widoczna.



### F. Bonus: pełny tunel WireGuard



Przy obecnej konfiguracji część ruchu przepływa przez VPN, a reszta przez połączenie internetowe klienta, w tym przeglądanie Internetu. Jeśli chcemy przełączyć się na **pełny tryb tunelowy** WireGuard, aby wszystko przechodziło przez tunel VPN, musimy wprowadzić kilka zmian w naszej konfiguracji....



Najpierw należy zainstalować pakiet "resolvconf" na serwerze:



```
sudo apt-get update
sudo apt-get install resolvconf
```



Gdy to zrobisz, musisz zmodyfikować profil "wg0.conf" na maszynie Debiana: zatrzymaj Interface, zmodyfikuj go i uruchom ponownie.



```
sudo wg-quick down /etc/wireguard/wg0.conf
```



Następnie **w bloku `[Interface]` dodajemy serwer DNS, który ma być używany**. W moim przypadku jest to kontroler domeny mojego laboratorium, ale możemy również zainstalować Bind9 na Debianie, aby mieć lokalny resolver.



```
DNS = 192.168.100.11
```



Zapisz plik, a następnie uruchom ponownie Interface:



```
sudo wg-quick up /etc/wireguard/wg0.conf
```



Wreszcie, w konfiguracji tunelu na stacji roboczej z systemem Windows 10 należy zmodyfikować sekcję "AllowedIPs", aby wskazać, że wszystko musi przechodzić przez tunel. Zastąp:



```
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
```



Przez:



```
AllowedIPs = 0.0.0.0/0
```



Widać, że włącza to również opcję "**Kill switch*".



![Image](assets/fr/040.webp)



Wreszcie, skorzystałem z tego pełnego tunelu, aby przeprowadzić mały test przepływu, którego wyniki pokazano poniżej:



![Image](assets/fr/039.webp)



Konfiguracja WireGuard jest dość prosta i łatwa do zrozumienia, a przede wszystkim do utrzymania. **WireGuard jest uważany za przyszłość VPN**, więc lepiej miejmy na niego oko! Widzimy również, że korzyści są znaczące pod względem wydajności, co jest ogromną zaletą WireGuard w porównaniu z OpenVPN.



Dodatkowa dokumentacja:





- [Man - Command wg](https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8)
- [Man - Command wg-quick](https://manpages.debian.org/unstable/wireguard-tools/wg-quick.8.en.html)



**Twój WireGuard VPN jest uruchomiony! Gratulacje!