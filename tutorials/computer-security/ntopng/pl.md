---
name: Ntopng
description: Monitorowanie sieci za pomocą ntopng
---
![cover](assets/cover.webp)



___



*Ten samouczek jest oparty na oryginalnej treści autorstwa Floriana Duchemin opublikowanej na stronie [IT-Connect](https://www.it-connect.fr/). Licencja [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). W oryginalnym tekście mogły zostać wprowadzone zmiany



___



## I. Prezentacja



**Niezależnie od tego, czy chodzi o sprawdzenie płynności sieci, uzyskanie jasnego obrazu użytkowania czy statystyk wydajności, monitorowanie przepływu sieci jest ważną częścią sieci korporacyjnej**. Pomaga przewidywać zmiany w infrastrukturze i pomaga zapewnić jakość użytkowania dla użytkowników (znaną również jako QoE dla *Quality of Experience*, w przeciwieństwie do QoS).



W tym celu dostępnych jest wiele technik i oprogramowania/protokołów. Na przykład Netflow, opracowany przez Cisco, może być używany do pobierania statystyk przepływu IP z Interface, ale jego użycie jest ograniczone do kompatybilnego sprzętu.



Dlatego w tym samouczku przedstawię **Ntop** i pokażę, jak używać go w swojej infrastrukturze, aby mieć oko na wykorzystanie sieci.



Ntop to oprogramowanie typu open source, które można zainstalować na dowolnym komputerze z systemem Linux. Jest ono bezpłatne i może gromadzić następujące dane:





- Wykorzystanie przepustowości
- Główni klienci
- Główne miejsca docelowe
- Zastosowane protokoły
- Zastosowane aplikacje
- Używane porty
- Itd.



Teraz przemianowany na **Ntopng (New Generation)**, oferuje wiele podstawowych funkcji bezpłatnie. Dostępna jest również wersja komercyjna, umożliwiająca eksportowanie skonfigurowanych alertów do oprogramowania typu SIEM lub filtrowanie ruchu za pomocą reguł zdefiniowanych bezpośrednio z poziomu sondy.



## II. Wymagania wstępne



Instalacja sondy Ntop różni się w zależności od sprzętu i środowiska. Dlatego nie zamierzam przedstawiać tutaj przewodnika krok po kroku, ale nakreślę różne możliwości.



### A. Tryb pokładowy



Jeśli masz pfSense, OPNSense lub Endian firewall w produkcji, lub nawet stację roboczą Linux z NFTables, dobra wiadomość! Możesz zainstalować Ntopng bezpośrednio i rozpocząć monitorowanie swoich interfejsów.



Zaletą tej techniki jest to, że nie wymaga ona dodatkowego sprzętu. Z drugiej strony zwiększa wykorzystanie zasobów, więc upewnij się, że masz odpowiedni sprzęt lub maszynę wirtualną o wystarczającym rozmiarze (minimum 2 rdzenie i 2 GB pamięci RAM).



### B. Tryb TAP / SPAN



Zaletą tego urządzenia jest to, że nie wymaga ono żadnych modyfikacji istniejącej infrastruktury i może być umieszczone w dowolnym miejscu w celu monitorowania określonych sekcji sieci lub między przełącznikiem rdzeniowym a routerem brzegowym w celu analizy ruchu do/z Internetu.



Dużą wadą tego typu urządzeń jest ich koszt. W dzisiejszych gigabitowych sieciach pasywny kran nie jest w stanie prawidłowo przechwytywać ruchu sieciowego, więc potrzebne jest aktywne urządzenie kosztujące około 200 euro (minimum).



Tryb **SPAN**, znany również jako **port mirroring**, jest używany przez przełącznik do przekazywania ruchu z jednego portu na drugi. Jest to zdecydowanie preferowana przeze mnie metoda, ponieważ jest prosta w konfiguracji i, podobnie jak tap, umożliwia monitorowanie części sieci lub całej sieci do woli. Istnieją jednak dwie wady: przełącznik musi zintegrować tę funkcję, a jej użycie może zwiększyć obciążenie procesora przełącznika.



### C. Tryb routera



Jest całkowicie możliwe zamontowanie routera pod Linuksem i zainstalowanie na nim ntopng. Jedyną wadą tej metody jest to, że zmodyfikuje ona sieć, albo jej wewnętrzne adresowanie, albo adresowanie między "prawdziwym" routerem a tym, który dodajesz.



Uwaga: dla czytelników artykułu [Create a Wifi router with Raspberry Pi and RaspAP](https://www.it-connect.fr/creer-un-routeur-wifi-avec-un-raspberry-pi-et-raspap/) jest całkowicie możliwe zainstalowanie ntopng na Rpi, aby uzyskać dokładne statystyki!



### D. Tryb mostka



Ciekawą alternatywą jest użycie **maszyny z systemem Linux w trybie mostu**. Umieszczona pomiędzy dwoma urządzeniami, pozwala na przechwytywanie całego ruchu bez konieczności ingerencji w konfigurację infrastruktury lub jej wyposażenia. Ze względu na to, że stara maszyna może wykonać to zadanie, koszt tej metody może być również atrakcyjny. Należy pamiętać, że aby być optymalnym, urządzenie powinno mieć trzy karty sieciowe, dwie w trybie mostu, jedną do dostępu do Interface i SSH. Możliwe jest użycie tylko dwóch kart, ale wtedy ruch administracyjny urządzenia będzie również przechwytywany...



Jest to więc **ten ostatni tryb, którego zamierzam użyć**. Ze względów praktycznych do demonstracji użyję maszyn wirtualnych, ale metoda pozostaje taka sama w przypadku użycia na maszynach fizycznych.



## III. Przygotowanie sondy z mostkiem Interface



Dla sondy wybrałem maszynę **Debian 11** w minimalnej instalacji.



Pierwszy krok, zawsze ten sam, aktualizacja pliku:



```
apt-get update && apt-get upgrade
```



Następnie zainstaluj pakiet **bridge-utils**, który pozwoli nam stworzyć nasz most:



```
apt-get install bridge-utils
```



Po zainstalowaniu, pierwszą rzeczą, na którą należy zwrócić uwagę, jest aktualna nazwa naszych kart sieciowych. W Debianie nazwa ta może przybierać różne formy i będziemy jej potrzebować do konfiguracji.



Proste polecenie **ip add** zwróci dane wyjściowe z tymi informacjami:



![Image](assets/fr/016.webp)



Tutaj widzę 3 interfejsy:





- Lo**: jest to Interface pętli zwrotnej; jest to wirtualny Interface, który "zapętla się" nad sprzętem. Zasadniczo ten Interface, którego Address to 127.0.0.1 (chociaż dowolny Address w 127.0.0.0/8 wystarczy, ponieważ ten zakres jest zarezerwowany do tego celu) jest używany do kontaktowania się z samym sprzętem. Jeśli zainstalowałeś stronę internetową na swojej stacji roboczej (na przykład przy użyciu WAMPP), prawdopodobnie użyłeś "*localhost*" Address, aby wyświetlić witrynę hostowaną na własnym komputerze. Ta nazwa hosta jest powiązana z Address 127.0.0.1, a zatem z pętlą zwrotną Interface.
- ens33**: to mój pierwszy Interface, który otrzymał Address z mojego DHCP
- ens36**: mój drugi Interface



Teraz, gdy mam już wszystkie informacje, mogę zmodyfikować plik */etc/network/interfaces*, aby utworzyć mój most. Oto jak to obecnie wygląda (może się różnić):



```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug ens33
iface ens33 inet dhcp
# This is an autoconfigured IPv6 interface
iface ens33 inet6 auto
```



Pierwsza część dotyczy mojego Interface loopback, którego nie będę dotykał, a następnie Interface ens33. Modyfikacje obejmują dodanie drugiego Interface (ens36) i skonfigurowanie mostu z tymi dwoma interfejsami:



```
# The primary network interface
auto ens33
iface ens33 inet manual

#The secondary network interface
auto ens36
iface ens36 inet manual
```



Oto kilka wyjaśnień dotyczących tych pierwszych zmian:





- auto *Interface***: automatycznie "uruchomi" Interface przy starcie systemu
- iface *Interface* inet manual**: aby używać Interface bez żadnego IP Address. Podobnie jak słowo kluczowe "static", aby zdefiniować statyczny adres IP Address lub "dhcp", aby użyć adresowania dynamicznego



Modyfikacje są kontynuowane:



```
# Bridge interface
auto br0
iface br0 inet static
address 192.168.1.23
netmask 255.255.255.0
gateway 192.168.1.1
bridge_ports ens33 ens36
bridge_stp off
```



Jeszcze raz kilka wyjaśnień:





- iface br0 inet static**: tutaj zdefiniowałem mój most Interface (*br0*) ze statycznym Address.
- Address, maska sieci, brama**: informacje o adresowaniu tablicy
- bridge_ports**: interfejsy, które mają być włączone do mostu
- bridge_stp**: protokół Spanning Tree jest używany podczas łączenia przełączników w celu wykrywania nadmiarowych łączy i unikania pętli. Ponieważ most może być wstawiony między dwie ścieżki sieciowe, może być źródłem pętli, stąd możliwość włączenia tego protokołu. Nie potrzebuję go tutaj, więc go wyłączam.



Zapisz zmiany i uruchom ponownie sieć:



```
systemctl restart networking
```



Aby sprawdzić zmiany, należy ponownie wyświetlić wynik polecenia **ip** add:



![Image](assets/fr/021.webp)


Wyraźnie widać **mój nowy Interface "*br0*" z IP Address, które mu przypisałem.** Nawiasem mówiąc, widać również, że moje dwa fizyczne interfejsy są rzeczywiście "UP", ale nie mają IP Address.



## IV. Instalacja NtopNG



Teraz, gdy nasza sonda jest w stanie sniffować ruch między moją siecią a routerem, pozostaje tylko zainstalować ntopng. Aby to zrobić, najpierw zmodyfikuj plik */etc/apt/sources.list* i dodaj **contrib** na końcu każdej linii zaczynającej się od **deb** lub **deb-src**.



Domyślnie źródła pakietów zawierają tylko pakiety zgodne z DFSG (*Debian Free Sotftware Guidelines*), identyfikowane przez słowo kluczowe **main**. Można również dodać te źródła:





- contrib**: pakiety zawierające oprogramowanie zgodne z DFSG, ale korzystające z zależności, które nie są częścią gałęzi **main**
- non-free**: zawiera pakiety, które nie są zgodne z DFSG



Przykład linii w pliku /etc/apt/sources.list:



```
deb http://deb.debian.org/debian/ bullseye main
```



Dodam więc słowo **contrib** do takich linijek.



Pozostałe kroki są wymienione na stronie [NtopNG] (https://packages.ntop.org/apt/), gdzie dla Debiana 11 należy dodać źródła Ntop do przyszłej instalacji. Dodanie to jest zautomatyzowane poprzez użycie pliku:



```
wget https://packages.ntop.org/apt/bullseye/all/apt-ntop.deb
apt install ./apt-ntop.deb
```



Następnie nadchodzi właściwa faza instalacji:



```
apt-get clean all
apt-get update
apt-get install ntopng
```



Pierwsze polecenie usuwa pamięć podręczną menedżera pakietów apt. Drugie zaktualizuje listę pakietów, a trzecie zainstaluje NtopNG.



Po instalacji oprogramowanie **NtopNG jest dostępne bezpośrednio na porcie 3000 maszyny Debiana**. Więc dla mnie jest to `http://192.168.1.23:3000`



![Image](assets/fr/022.webp)



Strona główna NtopNG



Domyślny login i hasło są wyświetlane, więc wszystko, co musisz zrobić, to je wprowadzić!



## V. Korzystanie z NtopNG



Podczas pierwszego logowania pierwszą rzeczą, o którą zostaniesz poproszony, jest zmiana domyślnego hasła administratora i języka. Niestety, francuski nie jest jednym z nich.



Następnie pojawiasz się na desce rozdzielczej:



![Image](assets/fr/023.webp)



Pulpit nawigacyjny NtopNG



Nie przyzwyczajaj się do tego! Jeśli zauważysz żółte pole u góry ekranu, zobaczysz zdanie: "*Licencja wygasa za 04:57*". Domyślnie instalacja uruchamia wersję próbną pełnej wersji NtopNG, ale na (bardzo) ograniczony czas. Po osiągnięciu tego "odliczania", wersja *community* jest aktywowana, a pulpit nawigacyjny zmienia się:



![Image](assets/fr/024.webp)



Nowy pulpit nawigacyjny społeczności NtopNG



Pierwszą rzeczą do zrobienia jest **sprawdzenie, czy właściwy Interface nasłuchuje**. W lewym górnym rogu rozwijana lista dostępnych interfejsów pozwala wybrać interesujący nas Interface: br0



![Image](assets/fr/025.webp)



Wybór Interface



Nowe okno wyświetla "Top Flaw Talkers", czyli urządzenia, które komunikują się najczęściej. Tutaj pojawiają się tylko dwie stacje:



![Image](assets/fr/026.webp)



**Hosty źródłowe pojawiają się po lewej stronie, a docelowe po prawej ** Pozwala to na wizualizację wykorzystania całkowitej przepustowości przez każdy host i uzyskanie ogólnego widoku ruchu sieciowego. Nie jest źle, ale możemy pójść dalej...



Jeśli na przykład kliknę na "*Hosts*", otrzymam wykres pokazujący zużycie energii przez wysyłanie i odbieranie każdego hosta w mojej sieci. Tutaj na przykład widzę, że sam 192.168.1.37 odpowiada za 80% mojego ruchu:



![Image](assets/fr/027.webp)



Jeśli kliknę IP Address danego hosta, zostanę przekierowany na stronę podsumowania:



![Image](assets/fr/028.webp)



Widzę na przykład, że jest to maszyna VMWare (rozpoznając TAK mojego MAC Address), że nazywa się DESKTOP-GHEBGV1 (więc z pewnością jest to host Windows) ORAZ mam **statystyki dotyczące odebranych i wysłanych pakietów, a także ilości danych**.



Zauważysz również nowe menu w górnej części tego podsumowania. Proponuję kliknąć "**Apps**", aby zobaczyć, co generuje tak duży ruch:



![Image](assets/fr/017.webp)


Ha, wygląda na to, że mamy odpowiedź! Na wykresie po lewej stronie widzimy, że 76,6% ruchu pochodzi z... Windows Update**, więc ten host pobiera aktualizacje!



NtopNG wykorzystuje technologię o nazwie DPI dla *Deep Packet Inspection*, umożliwiając kategoryzację każdego przepływu sieciowego i zdefiniowanie aplikacji (lub rodziny aplikacji) za nim.



Aby to zademonstrować, uruchamiam film z YouTube na moim hoście:



![Image](assets/fr/018.webp)



**Ruch został natychmiast rozpoznany i skategoryzowany!



Uwaga: z oczywistych powodów tego rodzaju oprogramowanie może powodować problemy z prywatnością, więc należy uważać, aby używać go w odpowiednich warunkach. Należy również pamiętać, że możliwe jest **anonimizowanie wyników**, opcja ta znajduje się w **Ustawienia > Preferencje > Różne** i nazywa się "**Mask Host IP Address**".



## VI. Wykrycia i alerty



NtopNG jest również w stanie wydawać alerty bezpieczeństwa dla niektórych kanałów. Można je znaleźć w menu **Alerts**, na banerze po lewej stronie. Tutaj, na przykład, mam w sumie 2851 alertów, podzielonych na różne stopnie ważności: Powiadomienie, Ostrzeżenie i Błąd.



![Image](assets/fr/019.webp)



Przyjrzyjmy się alertom o wysokim stopniu krytyczności, mam ich 17!



Kliknięcie tego rysunku powoduje wyświetlenie szczegółów alertów. Nie ma tu nic niepokojącego, jest to fałszywie dodatni wynik, pobieranie aktualizacji jest klasyfikowane jako transfer plików binarnych w strumieniu HTTP, co rzeczywiście może oznaczać atak.



![Image](assets/fr/020.webp)



Ponieważ jednak korzystam z darmowej wersji, nie mogę wykluczyć domen lub hostów, które są źródłem alertów, więc będziesz musiał mieć na nie oko, aby nie przegapić czegoś znacznie bardziej niepokojącego. NtopNG będzie generate alerty w przypadku:





- Pobieranie plików binarnych przez HTTP
- Podejrzany ruch DNS
- Korzystanie z niestandardowego portu
- Wykrywanie iniekcji SQL
- Cross-Site Scripting (XSS)
- Itd.



## VII. Wnioski



W tym samouczku zobaczyliśmy **jak skonfigurować sondę za pomocą NtopNG**, umożliwiając nam **analizę naszego ruchu sieciowego** w celu wizualizacji wykorzystania protokołu i zajętości każdego hosta, ale także wykrywania podejrzanego ruchu.



Niestety, nie jestem w stanie opisać wszystkich funkcji i możliwości w tym artykule, ale zapraszam do zapoznania się z nimi!



Rozwiązanie to można wdrożyć na stałe w ramach infrastruktury przedsiębiorstwa. NtopNG może również eksportować wyniki do bazy danych InfluxDB, umożliwiając tworzenie własnych pulpitów nawigacyjnych za pomocą narzędzia innej firmy, takiego jak Graphana.