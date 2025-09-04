---
name: Sieci IP - od teorii do praktyki
goal: Opanuj podstawy sieci IP, aby lepiej je konfigurować i rozwiązywać problemy.
objectives: 


  - Zrozumienie architektury i działania protokołu TCP/IP
  - Wyjaśnienie różnic, zalet i ograniczeń protokołów IPv4 i IPv6
  - Identyfikacja i rozróżnianie różnych typów IP Address
  - Konfiguracja i weryfikacja adresacji IP w systemach Unix/Linux
  - Używanie głównych narzędzi diagnostycznych do analizowania i rozwiązywania problemów sieciowych


---

# Umiejętności niezbędne do poruszania się w świecie własności intelektualnej


Zanurz się w sercu świata IP i wyposaż się w wiedzę, aby zrozumieć i skutecznie zarządzać swoimi sieciami. W tym kursie dowiesz się wszystkiego, co musisz wiedzieć o sieciach komputerowych w jasny i praktyczny sposób.


Dowiesz się, jak działają sieci i adresowanie IP, jak odróżnić IPv4 od IPv6, jak zidentyfikować i używać różnych kategorii Address oraz jak zrozumieć pełne znaczenie protokołu TCP/IP i powiązań między adresami IP, adresami fizycznymi i nazwami DNS.


NET 302 jest skierowany głównie do studentów, użytkowników Linuksa lub po prostu ciekawskich, którzy chcą zrozumieć podstawy sieci i wzmocnić swoją autonomię w zarządzaniu, rozwiązywaniu problemów i optymalizacji infrastruktury.


Dołącz do nas i zamień swoją wiedzę w prawdziwe doświadczenie operacyjne!


___


Kurs NET 302 jest adaptacją kursu *Podstawy sieci: TCP/IP, IPv4 i IPv6*, napisanego po francusku przez Philippe'a Pierre'a i opublikowanego na stronie [IT-Connect](https://www.it-connect.fr/cours/les-bases-du-reseau-tcpip-ipv4-et-ipv6/), na licencji Creative Commons Attribution-NonCommercial 4.0 International ([CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)).



W stosunku do oryginalnej wersji autorstwa Loïca Morela wprowadzono znaczące zmiany: tekst został całkowicie przeredagowany, rozszerzony i wzbogacony, aby zapewnić zaktualizowaną, dogłębną treść, przy jednoczesnym zachowaniu edukacyjnego ducha oryginalnej pracy Philippe'a Pierre'a. Zmienione zostały również diagramy.


+++


# Wprowadzenie


<partId>a52b996d-1e23-470f-a9df-7ad88790099a</partId>



## Przegląd kursu


<chapterId>9f238ecd-c9bb-4886-a205-2beba609fb13</chapterId>


Kurs ten stanowi kompletne wprowadzenie do podstaw sieci IP. Składa się on z czterech głównych sekcji, z których każda obejmuje aspekt niezbędny do zrozumienia, konfigurowania i diagnozowania problemów w sieci komputerowej.


### Protokół TCP/IP


W tej pierwszej części położymy podwaliny, badając koncepcję sieci i historię protokołu TCP/IP. Przeanalizujemy jego główne komponenty: IP, TCP, wraz z krótkim spojrzeniem na protokół IPv5 QoS. Omówimy również prymitywy usług, aby lepiej zrozumieć logikę danych Exchange.


### Adresowanie IPv4


Następnie przejdziemy do modułu poświęconego adresacji IPv4. Dowiesz się, jak IPv4 jest używany w praktyce, jakie są jego różne typy Address (prywatny, publiczny, rozgłoszeniowy itp.), jaka jest podstawowa rola DNS, a także jak działają adresy Ethernet i protokół ARP. Poznasz również NAT (Network Address Translation) i podstawy konfiguracji sieci.


### Adresowanie IPv6


Trzecia część skupia się na adresowaniu IPv6, które jest niezbędne do Address ograniczeń IPv4. Omówimy jego standardy i definicje, Address Assignment w sieci lokalnej, zarządzanie blokami Address oraz związek między IPv6 i DNS.


### Sieciowe narzędzia diagnostyczne


Na koniec przedstawimy główne narzędzia do diagnostyki sieci. Umożliwią one analizowanie, kontrolowanie i usuwanie usterek. Ta część będzie podzielona na warstwy: Dostęp do sieci, Sieć, Transport i Górne warstwy.


Pod koniec tego kursu będziesz miał podstawową wiedzę, aby skutecznie administrować infrastrukturą sieciową i diagnozować potencjalne problemy.


Gotowy do zanurzenia się w świecie sieci komputerowych? Do dzieła!


**UWAGA**: Opisy są oparte na systemie GNU/Linux CentOS 7. Jednak konfiguracje sieciowe są w dużej mierze takie same przy porównywaniu Debiana z systemem CentOS. Nie będziemy więc wprowadzać żadnych rozróżnień. Jeśli takowe istnieje, poprzedzimy je konkretnym logo.


**N.B.**: Jeśli podczas kursu napotkasz nieznane terminy, zapoznaj się z ich definicjami w [słowniczku] (https://planb.network/resources/glossary).



# Protokoły TCP/IP


<partId>53fd4b73-cdf1-4865-ba29-1ac8ec3e9e9a</partId>



## Czym jest sieć?


<chapterId>7370904f-f8f5-4ad4-a63a-5931d94c3b3b</chapterId>



W tym pierwszym module przyjrzymy się dogłębnie protokołowi TCP/IP, który jest kamieniem węgielnym nowoczesnej komunikacji cyfrowej. Omówimy jego pochodzenie, podstawowe zasady i wykorzystywany przez niego system adresowania, który jest niezbędny do zapewnienia przepływu informacji między połączonymi urządzeniami.


Wyszczególnimy również główne komponenty, które tworzą ten model i wyjaśnimy, w jaki sposób współdziałają one w celu utworzenia operacyjnej, niezawodnej i skalowalnej sieci. Najpierw jednak należy wrócić do koncepcji sieci.


Etymologicznie, sieć odnosi się do zestawu punktów połączonych ze sobą, tworzących wzajemnie połączoną strukturę. W telekomunikacji i informatyce definicja ta przekłada się na grupę urządzeń (komputery, routery, przełączniki, punkty dostępowe itp.) zdolnych do wymiany danych za pośrednictwem mediów fizycznych lub bezprzewodowych. Sieć umożliwia zatem ciągły lub przerywany przepływ informacji, w zależności od wymagań, używanych protokołów i charakteru wdrożonej architektury.


Z biegiem czasu opracowano kilka klasycznych topologii, aby zaspokoić różne potrzeby w zakresie kosztów, wydajności, odporności i łatwości konserwacji. Należą do nich:


- sieć pierścieniowa,
- sieć drzew,
- sieć autobusowa,
- sieć gwiazd,
- sieć mesh.



### Sieć pierścieniowa


W topologii pierścienia urządzenia są połączone w zamkniętej pętli: każda stacja jest połączona z następną, a ostatnia łączy się z pierwszą. W tej konfiguracji każde urządzenie działa jak przekaźnik, przekazując dane do następnego łącza. W zależności od typu sieci, informacje mogą krążyć tylko w jednym kierunku lub w obu.


Zaletą tego rozwiązania jest prostota okablowania i brak zależności od jakiegokolwiek centralnego sprzętu. Jednak ciągłość całej sieci zależy od kondycji każdego pojedynczego elementu: awaria pojedynczej stacji może przerwać cały system komunikacji. Dlatego też często stosuje się mechanizmy redundancji lub obejścia.



![Image](assets/fr/001.webp)



### Sieć drzew


Sieć drzewiasta lub topologia hierarchiczna jest wzorowana na strukturze drzewa genealogicznego. Składa się z kolejnych poziomów: węzeł główny na górze łączy się z kilkoma węzłami niższego poziomu, które z kolei mogą łączyć się z innymi węzłami i tak dalej.


Taki hierarchiczny układ sprawdza się szczególnie dobrze w przypadku dużych sieci, które wymagają jasnego podziału obowiązków i zarządzania segmentowego. Jednak sprawia on również, że sieć jest podatna na awarie węzłów wyższego poziomu: utrata korzenia lub głównej gałęzi może odciąć całe sekcje infrastruktury.



![Image](assets/fr/002.webp)



### Sieć autobusowa


W topologii magistrali wszystkie urządzenia współdzielą to samo medium transmisyjne, zazwyczaj linię koncentryczną lub światłowód. Każde urządzenie jest podłączone pasywnie, co oznacza, że nie modyfikuje aktywnie sygnału i może wysyłać lub odbierać dane za pośrednictwem tego współdzielonego kanału.


Główną zaletą topologii magistrali jest niski koszt instalacji dzięki uproszczonemu okablowaniu.  Jednak w starszych implementacjach opartych na kablu koncentrycznym (Ethernet 10BASE2/10BASE5), odłączenie lub utrata pojedynczej stacji może zakłócić lub nawet zatrzymać cały ruch, ponieważ ciągłość elektryczna magistrali i impedancja zakończenia nie będą już utrzymywane. Posiadanie pojedynczego medium fizycznego jest również krytyczną słabością: każda przerwa lub usterka zatrzymuje komunikację dla całej sieci.



![Image](assets/fr/003.webp)



### Sieć gwiazd


Topologia gwiazdy, znana również jako "koncentrator i szprycha", jest obecnie najbardziej powszechna, zwłaszcza w domowych i biurowych sieciach Ethernet. Tutaj wszystkie urządzenia łączą się z jednym urządzeniem centralnym.


Taki układ ułatwia zarządzanie i konserwację: jeśli jedno urządzenie peryferyjne ulegnie awarii, reszta sieci pozostaje nienaruszona. Wadą jest to, że urządzenie centralne jest pojedynczym punktem awarii: jeśli ulegnie awarii, komunikacja zostanie zatrzymana wszędzie. Jakość kabli i długość łącza muszą być również starannie przemyślane, aby utrzymać dobrą wydajność.



![Image](assets/fr/004.webp)



**Uwaga**: nadal istnieją sieci zorganizowane w topologii liniowej, podobnej do magistrali, gdzie sprzęt jest podłączony jeden po drugim. Rozwiązanie to, choć niedrogie we wdrożeniu, ma tę poważną wadę, że pojedyncza przerwa izoluje niektóre hosty, dzieląc sieć na niezależne podzbiory.


### Sieć mesh


Sieć mesh została zaprojektowana z myślą o maksymalnej redundancji: każde urządzenie jest bezpośrednio połączone z każdym innym. Zapewnia to ciągłość usług nawet w przypadku awarii wielu łączy lub urządzeń, ponieważ ruch może być przekierowywany alternatywnymi ścieżkami.


Kompromis polega na tym, że liczba połączeń, które należy ustanowić, szybko rośnie wraz z liczbą terminali. Dla `N` punktów połączeń, wymagane jest `N × (N-1) / 2` oddzielnych łączy, co czyni tę topologię kosztowną i złożoną do wdrożenia. Dlatego też jest ona wykorzystywana głównie w sieciach krytycznych wymagających bardzo wysokiej dostępności, takich jak niektóre części Internetu lub wrażliwe systemy przemysłowe.



![Image](assets/fr/005.webp)



Istnieją inne odmiany, takie jak sieci grid lub hypercube, które zostały zaprojektowane z myślą o specjalistycznych potrzebach w zakresie obliczeń rozproszonych lub przetwarzania równoległego.


W skali globalnej Internet jest ogromnym połączeniem sieci wykorzystujących różne topologie, zunifikowanych przez wspólne adresowanie (IPv4 i IPv6) oraz zbiór standardowych protokołów zdefiniowanych przez IETF (*Internet Engineering Task Force*). Ta różnorodność oznacza, że Internet nie ma jednej topologii: jego struktura jest elastyczna, skalowalna i niezależna od logicznego schematu adresowania, który czyni go użytecznym.



## Początki protokołu TCP/IP


<chapterId>266b6864-8789-48d7-bc85-001cb9f1651f</chapterId>



Początki protokołu TCP związane są z **ARPA** (*Advanced Research Projects Agency*, przemianowana na "DARPA" w 1972 roku), która uruchomiła projekt **ARPANET** w 1966 roku. Pierwszy segment ARPANET został uruchomiony w październiku 1969 roku, łącząc uniwersytety UCLA i Stanford. Celem było połączenie ośrodków badawczych za pomocą sieci z komutacją pakietów, która mogłaby utrzymać komunikację nawet w przypadku częściowej awarii infrastruktury.


W ramach tej dynamiki ARPA sfinansowała Uniwersytet Berkeley, aby zintegrować pierwsze protokoły TCP/IP z systemem BSD Unix. Odegrało to ważną rolę w rozpowszechnianiu i standaryzacji protokołu, najpierw w świecie akademickim, a później w przemyśle.


**Uwaga**: w tamtym czasie informatycy nie mieli jeszcze Linuksa (który pojawiłby się dopiero na początku lat 90.), ani Minixa, systemu edukacyjnego zaprojektowanego przez Andrew Tanenbauma.  Głównymi opcjami były Unix lub, czasami, zastrzeżone komputery mainframe, takie jak OpenVMS. Dzięki swojej elastyczności i otwartości, Unix odegrał kluczową rolę w rozpowszechnianiu pierwszych koncepcji sieciowych.


Ściśle mówiąc, TCP/IP nie jest pojedynczym protokołem, ale zestawem protokołów zbudowanych wokół TCP i IP. Protokół ten zyskał na znaczeniu, ponieważ zapewniał ustandaryzowany Interface programowania do wymiany danych między maszynami w tej samej sieci. Ten Interface, oparty na prymitywach zwanych "gniazdami", umożliwił tworzenie niezawodnych i elastycznych połączeń przy jednoczesnej integracji podstawowych protokołów aplikacji.


ARPANET jest zatem historycznym fundamentem dzisiejszego Internetu. Rzeczywiście, Internet jest globalną siecią opartą na zasadzie przełączania pakietów, w której informacje krążą przy użyciu zestawu standardowych protokołów, które zapewniają kompatybilność i interoperacyjność między heterogenicznymi systemami. Ta otwarta architektura umożliwiła rozwój i wdrażanie niezliczonych usług i aplikacji, w tym:


- e-maile,
- world Wide Web (www),
- przesyłanie i udostępnianie plików...


Zarządzanie i ewolucja tych protokołów są nadzorowane przez ***Internet Architecture Board*** (IAB).

Organizacja ta koordynuje kierunki techniczne poprzez dwie główne struktury:


- IRTF** (_Internet Research Task Force_), która prowadzi długoterminowe badania nad ewolucją i ulepszaniem protokołów.
- IETF** (_Internet Engineering Task Force_), która opracowuje, standaryzuje i dokumentuje protokoły operacyjne używane w Internecie


Dystrybucja zasobów sieciowych (zakresy IP Address, numery systemów autonomicznych, główne nazwy domen itp.) jest koordynowana na poziomie międzynarodowym przez **IANA/ICANN**. Zarządzanie operacyjne opiera się na: **RIR** (*Regionalne Rejestry Internetowe*): **RIPE NCC** (Europa, Bliski Wschód, Azja Środkowa), **ARIN**, **APNIC**, **LACNIC** i **AFRINIC**.


Wszystkie specyfikacje protokołów TCP/IP są rejestrowane w dokumentach zwanych **RFC** (_Request For Comments_), które służą jako autorytatywne referencje techniczne. Dokumenty RFC są stale aktualizowane i numerowane, aby odzwierciedlić ciągłą ewolucję pakietu protokołów.


Stos TCP/IP jest często przedstawiany jako stos czterech warstw funkcjonalnych, często porównywany do siedmiowarstwowego modelu **OSI** (_Open Systems Interconnection_) opracowanego przez **ISO** (_International Standards Organization_), który służy jako konceptualne odniesienie dla sieci.


Cztery warstwy modelu TCP/IP to:


- nETWORK ACCESS Layer, który zapewnia fizyczne łącze i protokoły kontroli dostępu do nośników;
- iNTERNET Layer, który obsługuje routing i adresowanie IP;
- tRANSPORT Layer, który gwarantuje niezawodność i zarządzanie przepływami danych przy użyciu protokołów takich jak TCP lub UDP;
- aPLIKACJA Layer, która grupuje protokoły użytkownika i oprogramowania, takie jak HTTP, FTP, SMTP i DNS.



![Image](assets/fr/006.webp)



Obecnie najczęściej używaną wersją protokołu IP jest IPv4, ale jego 32-bitowa przestrzeń Address ma wyraźne ograniczenia. Doprowadziło to do powstania protokołu IPv6, który wykorzystuje 128-bitowe adresowanie i oferuje praktycznie nieograniczoną przepustowość: niezbędną do wspierania gwałtownego wzrostu liczby podłączonych urządzeń i sprostania wyzwaniom Internetu rzeczy, mobilności i bezpieczeństwa.


Każdy Layer stosu TCP/IP zapewnia określone usługi, umożliwiając Address różne potrzeby sieciowe w sposób modułowy: transmisję fizyczną, adresowanie logiczne, integralność danych i usługi na poziomie aplikacji.


| Device example    | Description                                                                               | 	TCP/IP layer |
| ---------------------- | ----------------------------------------------------------------------------------------- | ----------------------- |
| Web server            | Application services closest to end users                                      | Application             |
| Gateway or proxy    | 	Encodes, encrypts, compresses useful data                                              | Application             |
| Session switch | Establishes sessions between applications                                               | Application             |
| Firewall or L4 router | Establishes, maintains, and terminates sessions between endpoint devices                  | Transport               |
| Router                | Globally addresses interfaces and determines optimal paths through a network | Network                  |
| Switch   | Locally addresses interfaces and forwards traffic via MAC                            | Network Access         |
| Network Interface Card (NIC)     | Signal encoding, cabling, connectors, physical specifications                        | Network Access         |

https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864

## Protokół QoS IPv5


<chapterId>570ded19-be61-4005-844e-9490570a6455</chapterId>



Nagłówek pakietu IP jest istotną strukturą danych, podzieloną na kilka pól, z których każde pełni określoną rolę, aby zapewnić prawidłową transmisję i przetwarzanie pakietów podczas ich podróży przez sieć. Pola te obejmują docelowy adres IP Address (potrzebny do skierowania pakietu do zamierzonego odbiorcy), długość nagłówka wskazaną przez pole IHL (*Internet Header Length*), całkowitą długość pakietu zapisaną w polu *Total Length*, informacje kontrolne i weryfikacyjne oraz inne parametry do zarządzania przepływem i jakością komunikacji.


Pierwsze pole w nagłówku nosi nazwę Version. Ta 4-bitowa wartość określa wersję protokołu IP, której używa pakiet. Jest to ważne, ponieważ mówi każdemu routerowi lub urządzeniu pośredniczącemu, jak interpretować i obsługiwać hermetyzowane dane.


**Uwaga**: Zarządzanie i przypisywanie wersji protokołów IP należy do **IANA**. Pole 4-bitowe pozwala na 16 kombinacji binarnych (wartości od 0 do 15). Na dzień dzisiejszy ich przypisanie wygląda następująco:



| Version Number | Protocol   | Version Description         | Reference               |
| -------------- | ---------- | --------------------------- | ----------------------- |
| 0–1            | Reserved   | Reserved                    |                         |
| 2–3            | Unassigned | Unassigned                  |                         |
| 4              | IP         | Internet Protocol           | RFC 791                 |
| **5**          | **ST**     | **ST Datagram mode**        | **RFC 1190** / RFC 1819 |
| 6              | IPv6       | Internet Protocol version 6 | RFC 8200                |
| 7              | TP/IX      | The Next Internet           | RFC 1475                |
| 8              | PIP        | The P Internet Protocol     | RFC 1621                |
| 9              | TUBA       | Tuba                        | RFC 1347                |
| 10–14          | Unassigned | Unassigned                  |                         |
| 15             | Reserved   | Reserved                    |                         |

Wśród nich jest IPv5, który, choć w dużej mierze nieznany opinii publicznej, istniał jako ST (_Stream Protocol_). Opracowany w latach 80. protokół IPv5 został zaprojektowany w celu zaspokojenia rosnącej w tym czasie potrzeby Address: zapewnienia "jakości usług" (QoS) dla niektórych przepływów danych, które wymagały ciągłej, stabilnej transmisji, takich jak Voice over IP lub strumienie multimedialne. Jego celem było zagwarantowanie przepustowości i priorytetu od końca do końca, koncepcja podobna do tego, co dziś oferuje RSVP (_Resource Reservation Protocol_) do dynamicznego rezerwowania zasobów sieciowych na nowoczesnych routerach.


Protokół IPv5 pozostał jednak eksperymentalny i został wdrożony tylko na niewielkiej liczbie urządzeń sieciowych. Jego ograniczone przyjęcie, w połączeniu z szybko rosnącym zapotrzebowaniem na więcej przestrzeni Address, skłoniło projektantów Internetu do bezpośredniego przejścia z IPv4 na IPv6. Pozwoliło to uniknąć zarówno ograniczeń Address IPv4, jak i ryzyka pomyłki lub niekompatybilności z eksperymentalnymi specyfikacjami IPv5.


Chociaż IPv5 nigdy nie był powszechnie używany, odegrał ważną rolę w kształtowaniu wczesnego myślenia o QoS i zarządzaniu ruchem. Dziś jest to bardziej znacznik historyczny niż działający standard.


**Protokół to zestaw reguł komunikacji: struktur danych, algorytmów, formatów pakietów i konwencji, które umożliwiają różnym urządzeniom niezawodne i zrozumiałe przekazywanie informacji Exchange. Usługa to konkretna implementacja protokołu za pośrednictwem określonych programów (klientów, serwerów), które przestrzegają tych zasad i udostępniają funkcjonalność użytkownikom i aplikacjom.


Możemy teraz przyjrzeć się bliżej strukturze i działaniu protokołu IP, który stanowi podstawę całej komunikacji sieciowej.



## Protokół IP


<chapterId>758fddbd-b652-4c18-bd1e-d038bd2e4d05</chapterId>



### Definicje i informacje ogólne


Protokół IP, czyli "***Internet Protocol***", jest podstawą modelu TCP/IP. Przenosi pakiety danych z jednego hosta do drugiego w sieci, niezależnie od tego, czy jest ona lokalna, czy obejmuje cały świat. Pełni dwie kluczowe role: zarządza logicznym adresowaniem urządzeń i zapewnia kierowanie pakietów przez często heterogeniczne i połączone ze sobą sieci.


Na poziomie fizycznym transmisja opiera się na interfejsach sprzętowych w celu ustanowienia połączeń punkt-punkt między węzłami. Jednak to protokół IP umożliwia komunikację end-to-end, dostarczając każdemu pakietowi informacji potrzebnych do poruszania się po wielu możliwych ścieżkach do miejsca docelowego.


Trzy konfiguracje sieciowe Elements określają sposób wysyłania pakietów:


- IP Address**: jednoznacznie identyfikuje host docelowy w sieci.
- Maska podsieci**: określa, która część Address identyfikuje sieć, a która część identyfikuje hosta, umożliwiając logiczny podział na podsieci.
- Brama**: wskazuje pośredni router, przez który pakiet powinien przejść, aby dotrzeć do sieci zewnętrznej lub innego segmentu sieci lokalnej.


W Internecie dane nie płyną jako jeden ciągły strumień, ale są wysyłane jako **datagramy**: niezależne bloki danych, z których każdy zawiera wszystkie informacje potrzebne do dostarczenia. Jest to zasada **przełączania pakietów**, gdzie informacje są dzielone na samodzielne jednostki, które mogą mieć różne ścieżki, aby dotrzeć do tego samego odbiorcy.


Oprócz ładunku (*payload*), każdy datagram IP zawiera ustrukturyzowany nagłówek z polami takimi jak docelowy Address, źródłowy Address, typ usługi, numer wersji protokołu i inne informacje kontrolne potrzebne do zarządzania transmisją.


Teoretyczny maksymalny rozmiar datagramu IP to **65 536 oktetów**, limit ustalony przez pole całkowitej długości w nagłówku. W praktyce rozmiar ten jest rzadko osiągany, ponieważ fizyczne sieci przenoszące pakiety (Ethernet, Wi-Fi, światłowody...) zwykle narzucają bardziej rygorystyczne limity znane jako **MTU** (_Maximum Transmission Unit_). Jeśli datagram przekracza MTU fizycznego łącza, musi zostać podzielony na mniejsze pakiety, z których każdy jest wysyłany osobno i ponownie łączony po dotarciu do odbiorcy.


Ta zdolność adaptacji sprawia, że IP jest solidnym i elastycznym protokołem, zdolnym do działania w wielu różnych technologiach bazowych, przy jednoczesnym zachowaniu uniwersalnej kompatybilności między heterogenicznymi systemami i sieciami.



### Fragmentacja datagramów IP


Gdy datagram IP musi przejść przez sieć, której przepustowość transmisji jest mniejsza niż sam datagram, musi zostać **pofragmentowany**, aby mógł podróżować bez problemu. Ten fizyczny limit rozmiaru nazywany jest **MTU** (Maximum Transmission Unit): największy rozmiar ramki, który może przejść przez daną sieć bez podziału.


Każda technologia sieciowa narzuca własne MTU, określone przez charakterystykę sprzętu i protokołu. Typowe wartości obejmują:


- ARPANET**: 1000 bajtów
- Ethernet**: 1500 bajtów
- FDDI**: 4470 bajtów


Gdy datagram przekracza MTU segmentu sieci, przez który musi przejść, sprzęt routujący podzieli go na mniejsze **fragmenty**, które są zgodne z limitem. Dzieje się tak zazwyczaj podczas przechodzenia z sieci o wysokim MTU do sieci o niższej przepustowości. Na przykład datagram pochodzący z sieci FDDI może wymagać fragmentacji przed wysłaniem go przez segment Ethernet.



![Image](assets/fr/008.webp)



Proces fragmentacji działa w następujący sposób:


- Router dzieli datagram na fragmenty, które nie są większe niż MTU sieci docelowej.
- Rozmiar każdego fragmentu jest wielokrotnością 8 bajtów, ponieważ protokół IP używa tej jednostki do kodowania przesunięcia ponownego montażu.
- Każdy fragment otrzymuje własny nagłówek IP, który zawiera informacje potrzebne ostatecznemu odbiorcy do ponownego złożenia ich we właściwej kolejności.


Po pofragmentowaniu fragmenty przemieszczają się niezależnie przez sieć. Mogą wybierać różne trasy, w zależności od tablic routingu, obciążenia łącza lub awarii. Nie ma gwarancji, że dotrą w kolejności, w jakiej zostały wysłane.


Po dotarciu, maszyna odbierająca zajmuje się **reassemblingiem**. Korzystając z informacji zawartych w nagłówkach (współdzielony identyfikator, przesunięcie i flagi fragmentacji), umieszcza fragmenty z powrotem we właściwej kolejności, aby zrekonstruować oryginalny datagram przed przesłaniem go do następnego Layer. Jeśli nawet jeden fragment zostanie utracony lub uszkodzony, cały datagram jest zwykle odrzucany, bez każdego fragmentu wynik byłby niekompletny lub bezużyteczny.


Choć skuteczne, fragmentacja i ponowny montaż mają swoje wady: dodatkowe przetwarzanie dla routerów i hostów oraz większe prawdopodobieństwo utraty pakietów, co może zwiększyć liczbę retransmisji. Dlatego też staranne zarządzanie MTU i optymalizacja rozmiaru pakietów są ważne dla płynnej i wydajnej komunikacji IP.



### Hermetyzacja danych


Aby zapewnić prawidłowe przesyłanie danych przez warstwy modelu TCP/IP, kluczową rolę odgrywa proces **enkapsulacji**. Na każdym etapie, gdy wiadomość podróżuje z aplikacji nadawcy do komputera odbiorcy, dodawane są dodatkowe informacje, znane jako nagłówki. Nagłówki te dają urządzeniom pośrednim i warstwom oprogramowania instrukcje potrzebne do przetworzenia, dostarczenia i, w razie potrzeby, ponownego złożenia danych.


Gdy wiadomość jest wysyłana, przechodzi przez cztery warstwy stosu TCP/IP. Na każdym Layer nowy nagłówek jest dodawany przed istniejącymi danymi: każdy nagłówek zawiera określone metadane, takie jak adresy logiczne lub fizyczne, porty komunikacyjne, numery sekwencyjne, flagi kontroli błędów i wszelkie informacje potrzebne do zarządzania transmisją i routingiem.


Transmisja odbywa się zatem zgodnie z ustrukturyzowanym procesem:


- Aplikacja Layer tworzy początkową **wiadomość**, zawierającą nieprzetworzone dane.
- Transportowy Layer hermetyzuje go w **segment**, dodając porty źródłowe i docelowe, numery sekwencyjne i mechanizmy kontroli przepływu.
- Internetowy Layer dodaje do segmentu nagłówek IP, tworząc **datagram**, określający źródłowy i docelowy adres IP.
- Network Access Layer opakowuje datagram w **ramkę**, dodając adresy MAC i kody kontroli integralności (CRC).



![Image](assets/fr/009.webp)



Ten proces enkapsulacji zapewnia zarówno integralność i identyfikowalność danych, jak i ich adaptowalność: podczas przenoszenia z jednej sieci do drugiej nagłówki dostarczają urządzeniom informacji potrzebnych do wyboru trasy, sprawdzenia ważności lub wykonania fragmentacji, jeśli to konieczne.


Po dotarciu na miejsce, proces jest odwracany: maszyna odbierająca otrzymuje ramkę w Network Access Layer, który odczytuje i usuwa odpowiedni nagłówek. Datagram jest następnie przekazywany do Internet Layer, który odczytuje nagłówek IP i usuwa go kolejno, aby dostarczyć segment do Transport Layer. Transportowy Layer przetwarza nagłówki transportowe, sprawdza integralność strumienia i ostatecznie dostarcza **wiadomość** do aplikacji docelowej w jej oryginalnym stanie.



![Image](assets/fr/010.webp)



Transformację danych w każdym Layer można podsumować następująco:


- Komunikat**: blok informacji w aplikacji Layer.
- Segment**: jednostka danych po enkapsulacji przez Transport Layer.
- Datagram**: forma przyjęta po dodaniu nagłówka IP przez Internet Layer.
- Ramka**: końcowy blok gotowy do transmisji przez medium fizyczne przez Layer dostępu do sieci.



![Image](assets/fr/011.webp)



Proces ten, niezbędny dla niezawodności i uniwersalności komunikacji internetowej, zapewnia, że każdy fragment danych, bez względu na to, jak rozdrobniony lub złożony, może być transportowany od końca do końca, pozostając zrozumiałym i użytecznym dla maszyny odbierającej.



### Adresowanie IP


Nawet z przełączaniem pakietów, fragmentacją i enkapsulacją, sieć nadal nie mogłaby funkcjonować bez niezawodnego systemu adresowania. Aby zapewnić, że każdy pakiet danych dotrze do właściwego odbiorcy, Internet Layer używa unikalnego identyfikatora: **IP Address**.

W protokole IPv4 adres IP Address jest kodowany na **32 bitach** i zapisywany jako cztery liczby dziesiętne oddzielone kropkami, w znanym formacie N1.N2.N3.N4 (na przykład: 192.168.1.12).


IP Address składa się z dwóch części:


- _netid_**: identyfikuje sieć, do której należy host
- _hostid_**: identyfikuje określony host w tej sieci

Separacja ta pozwala na logiczne zorganizowanie globalnego Internetu w wiele połączonych ze sobą sieci.


Historycznie, system IPv4 opierał się na schemacie klasowym, oznaczonym od A do E, który definiował zakres Address i ich przeznaczenie. Każda klasa przydzielała określoną liczbę bitów do _netid_ i _hostid_, bezpośrednio wpływając na możliwą liczbę sieci i hostów.



| **Class** | **IPv4 Address Range**            | **Usage**                    |
| --------- | --------------------------------- | ---------------------------- |
| A         | 1.x.x.x to 126.x.x.x              | Unicast addresses            |
|           | (127.x.x.x reserved for loopback) | Local loopback               |
| B         | 128.0.x.x to 191.255.x.x          | Unicast addresses            |
| C         | 192.0.0.x to 223.255.255.x        | Unicast addresses            |
| D         | 224.0.0.0 to 239.255.255.255      | IP Multicast                 |
| E         | 240.0.0.0 to 255.255.255.255      | Reserved for experimentation |

Nie wszystkie możliwe wartości mogą być przypisane do hostów. Na przykład, w **klasie C** Address, ostatni bajt oferuje 8 bitów (256 wartości). Ale dwa z nich są zarezerwowane:


- 0: identyfikuje samą sieć
- 255: to **broadcast** Address, używany do wysyłania pakietów do wszystkich hostów w sieci jednocześnie.

Pozostaje więc 254 użytecznych adresów dla urządzeń.


Liczba dostępnych adresów różni się znacznie w zależności od klasy: od dużych sieci publicznych w klasie A, przez sieci korporacyjne w klasie B, po mniejsze sieci lokalne w klasie C.



![Image](assets/fr/013.webp)



Niektóre zakresy Address są zarezerwowane do użytku prywatnego i nigdy nie są kierowane bezpośrednio do Internetu. Są one znane jako **adresy prywatne** i są używane wewnątrz organizacji, firm lub domów i wymagają translacji Address, zazwyczaj NAT (*Network Address Translation*), aby dotrzeć do publicznego Internetu. Są to:


- Klasa A**: od 10.0.0.0 do 10.255.255.255
- Klasa B**: od 172.16.0.0 do 172.31.255.255
- Klasa C**: od 192.168.0.0 do 192.168.255.255


Gdy urządzenie z prywatnym Address uzyskuje dostęp do Internetu, router lub brama z obsługą NAT zastępuje go prawidłowym publicznym Address.


Przykład: Jeśli host ma Address **192.168.7.5**, możemy wywnioskować:


- 192.168.7.0: sieć Address
- 192.168.7.1: często router lokalny
- 192.168.7.5: sam host


Innym szczególnym przypadkiem jest **127.0.0.1**, znany jako "***loopback***".

W systemach Linux jest on powiązany z Interface **lo**. Ten Address pozwala maszynie na samodzielne Address w celu lokalnego testowania lub diagnostyki, bez przechodzenia przez fizyczny Interface. Cały zakres **127.0.0.0/8** jest zarezerwowany do tego celu.


Aby zoptymalizować użycie Address i zaprojektować złożone sieci, **maska podsieci** (_netmask_) jest niezbędna. Ta binarna maska oddziela _netid_ od _hostid_ w IP Address.

Każda klasa ma domyślną maskę:


- 255.0,0,0** dla klasy A,
- 255.255.0.0** dla klasy B,
- 255.255.255.0** dla klasy C.


Dobry projekt sieci opiera się na podstawowej zasadzie: urządzenia, które muszą komunikować się bezpośrednio, powinny znajdować się w tej samej sieci lub podsieci. Aby podzielić sieć na segmenty, używamy podsieci, dzieląc sieć na mniejsze podsieci za pomocą bardziej szczegółowej maski.


Przykład podsieci:

Sieć **klasy C**: 192.168.1.0/24 z domyślną maską 255.255.255.0.

Potrzebujemy 4 podsieci z maksymalnie 60 hostami każda.


**Krok 1**: Liczba adresów potrzebnych na podsieć = 60 + 2 adresy zarezerwowane (sieć + broadcast) = 62.


**Krok 2**: Znajdź najbliższą potęgę 2 ≥ 62. -> 2⁶ = 64.


**Krok 3: Dostosowanie maski. Zachowaj bity _netid_ i zarezerwuj potrzebne bity _hostid_. Otrzymujemy maskę binarną, która po przekonwertowaniu daje **255.255.255.192**.


```
11111111 11111111 11111111 11000000
```


**Krok 4**: Oblicz zakresy Address dla każdej podsieci, zmieniając bity zarezerwowane dla hosta.



| Subnet ID (bits) | Subnet Address   | Subnet Mask     | Address Range                 | Broadcast Address |
| ---------------- | ---------------- | --------------- | ----------------------------- | ----------------- |
| 00               | 192.168.1.0/26   | 255.255.255.192 | 192.168.1.1 – 192.168.1.62    | 192.168.1.63      |
| 01               | 192.168.1.64/26  | 255.255.255.192 | 192.168.1.65 – 192.168.1.126  | 192.168.1.127     |
| 10               | 192.168.1.128/26 | 255.255.255.192 | 192.168.1.129 – 192.168.1.190 | 192.168.1.191     |
| 11               | 192.168.1.192/26 | 255.255.255.192 | 192.168.1.193 – 192.168.1.254 | 192.168.1.255     |


**Krok 5**: Tworzy to cztery podsieci, z których każda obsługuje do 62 maszyn, przy jednoczesnym zachowaniu ogólnego schematu adresowania. Część _hostid_ jest podzielona na część _subnetid_ i część hosta.



![Image](assets/fr/016.webp)



Ta fundamentalna zasada podsieci pozostaje niezbędna w nowoczesnej inżynierii sieciowej, umożliwiając precyzyjną alokację IP, lepszą kontrolę ruchu, silną izolację segmentów i skalowalne zarządzanie siecią.



### Adresowanie CIDR


Na początku lat 90-tych, gdy Internet szybko rozprzestrzenił się wśród firm i organizacji, tradycyjny system adresowania IP oparty na klasach (A, B, C) zaczął wykazywać swoje ograniczenia.

Jego sztywna struktura doprowadziła do znacznego marnotrawstwa adresów IP i sprawiła, że tablice routingu stawały się coraz większe, bardziej złożone i trudne w utrzymaniu.

W celu Address tych problemów wprowadzono bardziej elastyczną i wydajną metodę: **CIDR** (_Classless Inter-Domain Routing_). CIDR stopniowo stał się standardem, w dużej mierze zastępując stary system oparty na klasach.


Podstawową ideą CIDR jest możliwość grupowania kilku sąsiadujących sieci, zwłaszcza bloków klasy C, w jedną logiczną jednostkę zwaną **supernet** (_supernet_). Dzięki tej agregacji pojedynczy wpis w tablicy routingu może reprezentować wiele podsieci, zmniejszając liczbę tras, które routery muszą obsłużyć i poprawiając ich wydajność.


Podczas gdy sieci klasy C początkowo miały największą potrzebę agregacji ze względu na ich mniejszą przepustowość, zasada ta została również zastosowana do sieci klasy B, a teoretycznie nawet klasy A, choć te ostatnie są mniej dotknięte dzięki dużemu zasięgowi Address.


W przypadku CIDR koncepcja stałych klas znika. Przestrzeń Address jest traktowana jako ciągły zakres, który może być dzielony lub agregowany w zależności od potrzeb. Bloki CIDR są definiowane przy użyciu masek podsieci, które nie są ograniczone do domyślnych klas A, B lub C. Blok CIDR może reprezentować pojedynczą sieć lub ciągły zestaw podsieci współdzielących ten sam prefiks.


Blok CIDR jest zapisywany w formacie "Address/prefix", gdzie liczba po ukośniku wskazuje, ile bitów składa się na część sieciową. Na przykład, /17 oznacza, że pierwsze 17 bitów identyfikuje sieć, podczas gdy pozostałe 15 bitów identyfikuje hosty.


Przykład:

Blok /17 zawiera 2^(32-17) adresów, więc 2^15 = 32 768 adresów ogółem. Po odjęciu dwóch zarezerwowanych adresów (sieciowego i rozgłoszeniowego) pozostaje 32 766 użytecznych adresów hostów. Pozwala to administratorom sieci na precyzyjne dopasowanie rozmiaru podsieci do rzeczywistych potrzeb, unikając niepotrzebnego marnotrawstwa.


Aby ułatwić zrozumienie rozmiaru CIDR, poniżej znajduje się tabela typowych prefiksów i odpowiadających im masek podsieci oraz adresów użytkowych:


| CIDR Prefix | Available Host Bits | Subnet Mask     | Usable Host Addresses         |
| ----------- | ------------------- | --------------- | ----------------------------- |
| /8          | 24                  | 255.0.0.0       | 2^24 - 2 = 16,777,214         |
| /12         | 20                  | 255.240.0.0     | 2^20 - 2 = 1,048,574          |
| /16         | 16                  | 255.255.0.0     | 2^16 - 2 = 65,534             |
| /20         | 12                  | 255.255.240.0   | 2^12 - 2 = 4,094              |
| /24         | 8                   | 255.255.255.0   | 2^8 - 2 = 254                 |
| /26         | 6                   | 255.255.255.192 | 2^6 - 2 = 62                  |
| /27         | 5                   | 255.255.255.224 | 2^5 - 2 = 30                  |
| /28         | 4                   | 255.255.255.240 | 2^4 - 2 = 14                  |
| /29         | 3                   | 255.255.255.248 | 2^3 - 2 = 6                   |
| /30         | 2                   | 255.255.255.252 | 2^2 - 2 = 2                   |
| /31         | 1                   | 255.255.255.254 | 2^1 = 2 (point-to-point only) |
| /32         | 0                   | 255.255.255.255 | 1 (host address only)         |


**UWAGA**: Historycznie, RFC 950 zniechęcał do używania podsieci zero, głównie w celu uniknięcia pomyłek w routingu.  Ograniczenie to stało się nieaktualne wraz z RFC 1878, który w pełni zezwala na jego użycie. Stare ograniczenie wynikało głównie z niekompatybilności ze starszym sprzętem, który nie mógł poprawnie obsługiwać CIDR. Nowoczesny sprzęt nie ma takich problemów.


Na przykład podsieć **1.0.0.0** z maską podsieci **255.255.0.0**, niegdyś niejednoznaczna z identyfikatorem sieci klasy A, jest teraz całkowicie poprawna i użyteczna.


**WSKAZÓWKA**: do bezbłędnych obliczeń podsieci i szybkiej konwersji adresów do notacji CIDR służą przydatne narzędzia, takie jak ***ipcalc***. Ten "kalkulator sieciowy" wyraźnie pokazuje podziały Address, dostępne zakresy i powiązane maski, idealne zarówno dla administratorów, jak i studentów uczących się CIDR.


```shell
sudo apt install ipcalc
```


https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d

## Protokół TCP


<chapterId>860bf7d5-a502-4d10-a12c-9827f6c2d393</chapterId>



Protokół **TCP** (_Transmission Control Protocol_) odgrywa centralną rolę w Layer TRANSPORT modelu TCP/IP. Działa jako pomost między aplikacjami a Internetem Layer, zapewniając niezawodny transfer danych między dwoma odległymi maszynami.

Podczas gdy protokół IP po prostu wysyła pakiety, nie gwarantując ich dostarczenia ani kolejności, TCP zapewnia integralność i spójność przepływu danych, dostarczając je bez strat, we właściwej kolejności i bez duplikatów.


Główne obowiązki TCP obejmują:


- Zmiana kolejności odbieranych segmentów;
- Monitorowanie przepływu danych w celu uniknięcia zatorów;
- Dzielenie lub ponowne łączenie bloków danych w odpowiednie jednostki (segmenty);
- Zarządzanie nawiązywaniem i kończeniem połączeń między oboma końcami komunikacji.


TCP jest protokołem zorientowanym na połączenie, co oznacza, że ustanawia wyraźną, ciągłą relację między klientem a serwerem. W tym celu wykorzystuje **numery sekwencji** i **potwierdzenia**: dla każdego wysłanego segmentu przypisywany jest unikalny identyfikator, dzięki czemu maszyna odbierająca może sprawdzić zarówno kolejność, jak i integralność danych. Odbiorca zwraca następnie segment potwierdzenia z flagą **ACK** ustawioną na 1, potwierdzając odbiór i wskazując następny oczekiwany numer sekwencji.



![Image](assets/fr/018.webp)



Aby poprawić niezawodność, TCP wykorzystuje licznik czasu: po wysłaniu segmentu rozpoczyna się odliczanie. Jeśli potwierdzenie nie nadejdzie w określonym czasie, nadawca automatycznie retransmituje segment, zakładając, że został on utracony w tranzycie. Ten mechanizm automatycznej retransmisji kompensuje straty nieodłącznie związane z sieciami IP, które mogą wystąpić w przypadku przeciążenia, błędów routingu lub awarii sprzętu.



![Image](assets/fr/019.webp)



TCP jest w stanie wykrywać i obsługiwać duplikaty. Jeśli nadejdzie retransmitowany segment, ale pojawi się również oryginał, odbiornik używa numerów sekwencji do identyfikacji duplikatu i zachowuje tylko poprawną kopię, eliminując wszelkie niejasności.


Aby ten proces działał, obie maszyny muszą wspólnie rozumieć swoje początkowe numery sekwencyjne. Jest to zapewnione poprzez przestrzeganie ścisłej procedury połączenia: z jednej strony **serwer** nasłuchuje na określonym porcie, czekając na przychodzące żądanie (tryb pasywny); z drugiej strony **klient** aktywnie inicjuje połączenie, wysyłając żądanie do serwera na tym samym porcie usługi.


**UWAGA**: "Port" to identyfikator numeryczny (od 0 do 65 535) przypisany do aplikacji sieciowej na komputerze. Służy on do rozróżniania wielu usług działających jednocześnie na tym samym adresie IP Address. Gdy klient wysyła dane, określa numer portu, aby system operacyjny serwera wiedział, który program powinien je odebrać (np. 80 dla HTTP, 443 dla HTTPS, 25 dla SMTP). Porty działają jak dedykowane drzwi, kierując ruch do i na zewnątrz, zapobiegając pomyłkom między usługami i umożliwiając precyzyjną kontrolę dostępu za pomocą zapór ogniowych lub reguł filtrowania.


Synchronizacja sekwencji Exchange opiera się na słynnym mechanizmie **"*three-way handshake*"**, podobnym do sposobu, w jaki dwie osoby witają się ze sobą w celu nawiązania kontaktu. Ta faza inicjalizacji, która zapewnia niezawodność TCP, odbywa się w 3 etapach:

1. **SYN:** Klient wysyła początkowy segment synchronizacji (**SYN**) z ustawioną odpowiednią flagą i początkowym numerem sekwencji (np. C);

2. **SYN-ACK:** Serwer odbierający odpowiada segmentem potwierdzenia (**SYN-ACK**), potwierdza numer sekwencji klienta i podaje swój własny początkowy numer sekwencji;

3. **ACK:** Klient wysyła ostateczne potwierdzenie (**ACK**) potwierdzające otrzymanie numeru sekwencji serwera, finalizując synchronizację. Flaga SYN jest teraz wyłączona, a flaga ACK pozostaje ustawiona, wskazując, że połączenie zostało nawiązane.



![Image](assets/fr/020.webp)



Ten protokół Exchange zapewnia, że obie strony korzystają z tej samej bazy numeracyjnej przed przesłaniem danych ładunku. Po zakończeniu synchronizacji sesja jest otwierana: segmenty mogą teraz podróżować w obu kierunkach, każdy potwierdzony po otrzymaniu, zapewniając maksymalną niezawodność przepływu danych.


Ten ***three-way handshake*** dotyczy tylko nawiązywania połączenia. Do zamykania połączeń TCP używa *czterokierunkowego uścisku dłoni*: FIN → ACK → FIN → ACK, który gwarantuje, że żaden segment w tranzycie nie zostanie utracony przed całkowitym zwolnieniem połączenia.


Chociaż proces ten został zaprojektowany z myślą o solidności i niezawodności, doprowadził on również do powstania podatnych na ataki luk. Na przykład ataki takie jak **IP Spoofing** mają na celu ominięcie lub uszkodzenie tej relacji zaufania poprzez udawanie autoryzowanej maszyny za pomocą sfałszowanych numerów sekwencyjnych, tworząc lukę, która umożliwia przechwytywanie lub manipulowanie strumieniem danych.


Aby ograniczyć ryzyko przechwycenia synchronizacji sekwencji i zarządzać obciążeniem sieci, protokół TCP wykorzystuje technikę zarządzania przepływem znaną jako "**_Sliding Window_**". System ten reguluje ilość danych, które mogą być wysyłane bez konieczności natychmiastowego potwierdzenia dla każdego segmentu, zmniejszając w ten sposób niepotrzebne przeciążenie sieci przy jednoczesnym zachowaniu dobrej niezawodności.


W praktyce okno przesuwne definiuje zakres numerów sekwencyjnych, które mogą swobodnie krążyć między nadawcą a odbiorcą bez potwierdzania każdego segmentu. Gdy potwierdzenia są odbierane przez system wysyłający, okno "przesuwa się": przesuwa się w prawo, robiąc miejsce na nowe segmenty do wysłania. Rozmiar tego okna (krytyczny dla optymalizacji przepustowości przy jednoczesnym unikaniu zatorów) jest określony w polu "*Window*" nagłówka TCP.


**Przykład**: jeśli początkowy numer sekwencji wynosi 3, a okno rozciąga się do sekwencji 5, segmenty o numerach od 3 do 5 mogą być wysyłane bez oczekiwania na indywidualne potwierdzenia.



![Image](assets/fr/021.webp)



Rozmiar okna przesuwnego nie jest stały; dostosowuje się dynamicznie do warunków sieciowych i możliwości przetwarzania odbiornika.  Jeśli odbiornik jest w stanie obsłużyć większą ilość danych, wskazuje to za pomocą pola Window, zachęcając nadawcę do rozszerzenia okna. I odwrotnie, w przypadku przeciążenia lub ryzyka nasycenia, odbiorca może zażądać zmniejszenia, a nadawca poczeka, aż okno przesunie się do przodu, aby wysłać dodatkowe segmenty.


Protokół zapewnia symetryczną procedurę zamykania połączenia TCP w celu zapewnienia czystego, uporządkowanego zamknięcia. Każda maszyna może zainicjować zamknięcie, wysyłając segment z flagą **FIN** ustawioną na 1, sygnalizując zamiar zakończenia komunikacji. Następnie czeka, aż wszystkie segmenty w tranzycie zostaną odebrane i ignoruje wszelkie dalsze dane.


Po otrzymaniu tego segmentu, druga maszyna wysyła potwierdzenie, również oznaczone flagą FIN. Następnie kończy wysyłanie pozostałych danych przed poinformowaniem lokalnej aplikacji, że połączenie zostało zamknięte. To podwójne potwierdzenie zapewnia uporządkowane zamknięcie i minimalizuje ryzyko utraty danych.


To precyzyjne zarządzanie, łączące elastyczny routing IP ze ścisłą kontrolą TCP, jest często ilustrowane diagramem kontrastującym szybkość protokołu IP (który działa na zasadzie **"best effort "**, bez gwarancji dostawy) z niezawodnością protokołu TCP (który zarządza transmisją poprzez potwierdzenia i wynegocjowane sekwencje).



![Image](assets/fr/022.webp)



W niektórych przypadkach absolutna niezawodność nie jest jednak priorytetem: liczy się szybkość i prostota. Dotyczy to aplikacji takich jak transmisje strumieniowe na żywo lub VoIP, które mogą tolerować pewne straty pakietów bez poważnego wpływu na wrażenia użytkownika. W takich przypadkach preferowany jest **UDP** (_User Datagram Protocol_).


UDP działa na zasadniczo innej zasadzie niż TCP: jest **bezpołączeniowy**, co oznacza, że między nadawcą a odbiorcą nie jest nawiązywana żadna wcześniejsza relacja. Gdy maszyna wysyła pakiety za pośrednictwem UDP, są one przesyłane w jedną stronę; odbiorca nie wysyła potwierdzeń, a nadawca nie ma potwierdzenia, że wiadomość dotarła. Nagłówek UDP jest celowo minimalny, zawiera tylko port źródłowy, port docelowy, długość segmentu i sumę kontrolną, bez wbudowanego mechanizmu potwierdzania lub kontroli stanu. Jak zawsze, adresy IP są przenoszone przez bazowy nagłówek IP.


Powszechną analogią jest to, że TCP jest jak **rozmowa telefoniczna**, w której obwód jest ustanawiany, śledzony i kontrolowany podczas całej rozmowy. Podczas gdy protokół UDP jest jak **wysyłanie poczty**, gdzie nadawca wrzuca list do skrzynki pocztowej bez natychmiastowego dowodu doręczenia lub systematycznej informacji zwrotnej.


Ta komplementarność TCP i UDP umożliwia nowoczesnym sieciom dostosowanie się do różnych potrzeb, wybierając maksymalną niezawodność lub priorytet prędkości, w zależności od aplikacji.



## Prymitywy usług


<chapterId>4480afb7-e950-4ccb-88fa-d132f9dc3479</chapterId>



### Architektura warstwowa i organizacja Exchange


Jak widzieliśmy, **usługi** są konkretną implementacją protokołów, które opisaliśmy do tej pory. Chociaż model TCP/IP różni się od modelu **OSI**, przyjmuje to samo podejście warstwowe: każdy Layer jest zaprojektowany do wykonywania określonej funkcji i dostarczania **usług** do Layer bezpośrednio nad nim, co skutkuje modułową, solidną i łatwą w utrzymaniu architekturą.


Każdy Layer opiera się na możliwościach Layer znajdującego się poniżej, a z kolei zapewnia Layer powyżej spójny Interface do zarządzania danymi. W tej architekturze każdy Layer ma własne **struktury danych**, starannie zdefiniowane w celu zapewnienia doskonałej kompatybilności z innymi warstwami. Zgodność ta jest niezbędna do płynnej, niezawodnej i przejrzystej komunikacji z jednego punktu końcowego do drugiego.


Wymiany te regulują dwa kluczowe aspekty:


- Aspekt pionowy**: relacja między jednym Layer a Layer znajdującym się nad lub pod nim (od Layer N do Layer N+1 i odwrotnie).



![Image](assets/fr/023.webp)




- Aspekt poziomy**: interakcja między zdalnymi aplikacjami, tj. dialog między **klientem** a **serwerem**, w dowolnym kierunku.



![Image](assets/fr/024.webp)



Architektura warstwowa opiera się na zasadzie, że każdy Layer przetwarza tylko informacje w swoim zakresie: struktury danych, nagłówki i mechanizmy kontrolne różnią się w zależności od Layer, ale razem tworzą spójny system, zapewniając stopniowe kierowanie danych do miejsca docelowego.


**Przypomnienie**: Określona terminologia jest używana do opisania jednostek danych wymienianych między warstwami:


- wiadomość** dla aplikacji Layer,
- segment** dla Layer Transport (TCP),
- datagram** dla Internetu Layer (IP),
- ramka** dla Network Access Layer.


Poniższa tabela podsumowuje terminy dla kontekstów TCP i UDP:


| TCP/IP Layer         | Unit Name (TCP) | Unit Name (UDP) |
|----------------------|------------------|------------------|
| Application Layer    | Stream           | Message          |
| Transport Layer      | Segment          | Packet           |
| Internet Layer       | Datagram         | Datagram         |
| Network Access Layer | Frame            | Frame            |

### Prymitywy usług i jednostki danych


Rdzeniem tego systemu są **prymitywy usług**, które działają jako interfejsy komunikacyjne. Te prymitywy działają jak biurka usług, nasłuchując na zarezerwowanych określonych **portach** i umożliwiając procesom ustanawianie, utrzymywanie i kończenie połączeń sieciowych w kontrolowany sposób. Podczas gdy protokoły organizują format i transmisję danych w sieci, to **usługi i ich prymitywy** zapewniają pionowe połączenie między warstwami.


Łącząc aspekt horyzontalny (komunikacja między rozproszonymi aplikacjami) z aspektem wertykalnym (wewnętrzne interakcje między warstwami), model TCP/IP zapewnia kompletną, skalowalną architekturę. Nałożenie na siebie tych dwóch perspektyw daje jasny przegląd tego, w jaki sposób dane są wymieniane w ustrukturyzowanej komunikacji sieciowej.



![Image](assets/fr/026.webp)



### Podsumowanie części


W tej pierwszej głównej sekcji zbadaliśmy podstawową architekturę, która reguluje konfigurację i działanie dzisiejszych sieci podłączonych do Internetu. Architektura ta opiera się na **modelu czterech Layer**, inspirowanym modelem OSI i zbudowanym wokół pakietu protokołów **TCP/IP**, będącego podstawą nowoczesnej komunikacji. Widzieliśmy, że TCP, ze swoim podejściem zorientowanym na połączenie, zapewnia niezawodne transfery, podczas gdy UDP, lżejszy i szybszy, jest preferowany, gdy szybkość jest ważniejsza niż niezawodność.


Prawidłowe funkcjonowanie tego modelu opiera się na implementacji protokołów poprzez **prymitywy usług**. Zapewniają one połączenie między warstwami, umożliwiając dostosowanie przetwarzania danych do specyficznych wymagań każdego poziomu, od transportu do aplikacji, w tym dostępu do Internetu i sieci. To modułowe podejście sprawia, że system jest zarówno elastyczny, jak i solidny.


Adresowanie IP jest kolejnym kamieniem węgielnym tej infrastruktury. Każde podłączone urządzenie jest identyfikowane przez **unikalny adres IP Address**, pobrany z przestrzeni Address zorganizowanej w **klasy** (od A do E). Niektóre z tych adresów są zarezerwowane do specjalnych celów, takich jak lokalna pętla zwrotna lub multiemisja, podczas gdy inne, znane jako "adresy prywatne", nie są kierowane przez Internet bez translacji (NAT). Klasyfikacja ta umożliwia logiczną, hierarchiczną organizację sieci.


Przeanalizowaliśmy również koncepcję **podsieci**, która umożliwia podział segmentów sieci w celu lepszego zarządzania zasobami IP i optymalizacji przepływu danych. Podczas gdy ręczny podział przy użyciu masek podsieci pozostaje ważną zasadą, został on w dużej mierze zmodernizowany dzięki **CIDR** (_Classless Inter-Domain Routing_). Metoda ta przekształciła zarządzanie Address, umożliwiając bardziej elastyczną i racjonalną alokację zakresów IP, przy jednoczesnym zmniejszeniu rozmiaru tablic routingu.


Dzięki opanowaniu tych pojęć - warstw, protokołów, prymitywów usług, adresowania i podsieci - zyskujesz solidne podstawy do zrozumienia technicznego działania nowoczesnych sieci oraz do wydajnego konfigurowania infrastruktury sieciowej w celu spełnienia dzisiejszych potrzeb.


W następnej sekcji przyjrzymy się bliżej adresowaniu IPv4.



# Adresowanie IPv4


<partId>83f3c3e5-378c-440f-a095-df210842efde</partId>



## Korzystanie z protokołu IPv4


<chapterId>79e4dd18-446a-435b-9f25-c88a00f8bec6</chapterId>



W tej sekcji przejdziemy głębiej i przyjrzymy się, w jaki sposób adresy **IPv4** są faktycznie implementowane w rzeczywistej sieci. Rozbijemy ich format, logikę stojącą za nimi i sposób, w jaki łączą się z innymi kluczowymi sieciowymi Elements, takimi jak **nazwy DNS**, **adresy MAC**, **podsieci** i **techniki tłumaczenia**.


IP Address jest unikalnym identyfikatorem numerycznym przypisanym do każdego **sieciowego Interface** na urządzeniu. Umożliwia on zlokalizowanie tego urządzenia w sieci i dotarcie do niego w celu przesłania danych. Na przykład router, serwer, stacja robocza, drukarka sieciowa, a nawet kamera monitorująca ma co najmniej jeden własny Address IP. IP Address umożliwia **routing**, czyli przenoszenie pakietów z punktu A do punktu B, nawet jeśli są one fizycznie daleko od siebie.


Adresy IP mogą być przypisywane na dwa główne sposoby:


- Statyczny**: Ręczne ustawienie na urządzeniu.
- Dynamiczny**: Automatycznie przypisywany na żądanie przez serwer DHCP (_Dynamic Host Configuration Protocol_). DHCP upraszcza zarządzanie siecią, eliminując potrzebę ręcznej konfiguracji, jednocześnie umożliwiając precyzyjną kontrolę poprzez rezerwacje i czas trwania dzierżawy.


*adresy *IPv4** są zapisywane w **32-bitowym** formacie podzielonym na **cztery bajty**. Każdy bajt zawiera 8 bitów i reprezentuje liczbę dziesiętną od 0 do 255. Cztery bajty są oddzielone kropkami, aby utworzyć jasny, czytelny zapis.


przykład: Address 172.16.254.1_



![Image](assets/fr/027.webp)



Każdy bit w bajcie ma wartość (lub "wagę"): lewy bit (najbardziej znaczący bit) ma wartość 128, następny 64, następnie 32, 16, 8, 4, 2 i 1 dla prawego bitu (najmniej znaczący bit). W ten sposób zapis binarny jest konwertowany na dziesiętny poprzez proste dodanie ustawionych wag.


Poniższa tabela ilustruje tę zgodność:



| Binary Code | Activated Bit Values          | Decimal Value |
|-------------|-------------------------------|---------------|
| 00000000    | 0                             | 0             |
| 00000001    | 1                             | 1             |
| 00000011    | 1 + 2                         | 3             |
| 00000111    | 1 + 2 + 4                     | 7             |
| 00001111    | 1 + 2 + 4 + 8                 | 15            |
| 00011111    | 1 + 2 + 4 + 8 + 16            | 31            |
| 00111111    | 1 + 2 + 4 + 8 + 16 + 32       | 63            |
| 01111111    | 1 + 2 + 4 + 8 + 16 + 32 + 64  | 127           |
| 11111111    | 1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 | 255      |

Aby przekonwertować binarny na dziesiętny, dodaj wagi bitów, które są ustawione na 1.


| Binary     | Decimal Value |
| ---------- | ------------- |
| `10101100` | 172           |
| `00010000` | 16            |
| `11111110` | 254           |
| `00000001` | 1             |

IP Address identyfikuje pojedynczy **sieciowy Interface**, a nie całe urządzenie. Wieloportowy router lub firewall ma wiele interfejsów, z których każdy ma własny adres IP Address. Jeden Interface może mieć nawet kilka adresów IP (na przykład do obsługi wielu sieci wirtualnych lub usług).


Każdy pakiet IP zawiera w nagłówku dwa adresy IP:


- Źródło Address (**nadawca**)
- Docelowy Address (**odbiornik**)

Routery odczytują te adresy, aby ustalić najlepszą ścieżkę do wysłania pakietu, aż dotrze on do miejsca docelowego. Bez ścisłych reguł adresowania ruch sieciowy nie mógłby być prawidłowo kierowany, a globalne połączenie sieci byłoby niemożliwe.


Address IPv4 składa się z dwóch części:


- NetID**: identyfikuje sieć
- HostID**: identyfikuje urządzenie w tej sieci

Maska podsieci** określa, gdzie kończy się NetID, a zaczyna HostID, określając, ile bitów należy do każdej części. Im dłuższy NetID, tym większa liczba możliwych podsieci, ale liczba hostów na podsieć odpowiednio spada.


Pierwotnie sieci IPv4 były podzielone na pięć **klas**: (A, B, C, D i E). Każda klasa odpowiada określonemu zakresowi NetID i definiuje stałą ziarnistość:


- Klasa A: bardzo duże sieci z dużą liczbą hostów
- Klasa B: sieci średniej wielkości
- Klasa C: małe sieci
- Klasa D: adresy zarezerwowane dla multicastingu (_multicast_)
- Klasa E: adresy eksperymentalne, nieużywane do konwencjonalnego adresowania



| Class | Leading Bits | First Byte Range | Default Subnet Mask | Purpose                          |
| ----- | ------------ | ---------------- | ------------------- | -------------------------------- |
| A     | 0            | 0 – 127          | 255.0.0.0           | Very large networks              |
| B     | 10           | 128 – 191        | 255.255.0.0         | Medium-sized networks            |
| C     | 110          | 192 – 223        | 255.255.255.0       | Small networks                   |
| D     | 1110         | 224 – 239        | N/A                 | Multicast addresses              |
| E     | 1111         | 240 – 255        | N/A                 | Experimental (not publicly used) |

Adresy specjalne:


- Sieć Address**: Identyfikuje samą sieć (używaną w tabelach routingu).
- Broadcast Address**: Wysyła dane do wszystkich urządzeń w podsieci jednocześnie (wszystkie bity HostID ustawione na 1).


Następujące zakresy są zarezerwowane do użytku wewnętrznego:


- 10.0.0.0/8** (prywatna klasa A)
- 127.0.0.0/8** (lokalna pętla zwrotna lub _loopback_)
- 172.16.0.0 do 172.31.255.255** (prywatna klasa B)
- 192.168.0.0 do 192.168.255.255** (prywatna klasa C)


Adresy **127.0.0.1** i, bardziej ogólnie, cały zakres 127.0.0.0/8 jest używany do testów wewnętrznych: każde żądanie wysłane do niego nigdy nie opuszcza maszyny. Jest to przydatne do sprawdzania, czy lokalna usługa sieciowa działa bez angażowania szerszej sieci.


Aby lepiej wykorzystać przestrzeń Address, administratorzy często dzielą sieci na **podsieci** przy użyciu masek podsieci lub notacji **CIDR** (_Classless Inter-Domain Routing_). CIDR pozwala na bardziej precyzyjne zarządzanie i pomaga uniknąć marnowania adresów. Obecnie CIDR jest niezbędny do precyzyjnego dostrajania zakresów IP i zmniejszania rozmiaru tablic routingu.


W nowoczesnych sieciach adresowanie IP jest zwykle łączone z innymi identyfikatorami:



- nazwa domeny** zarejestrowana w **DNS** (_Domain Name System_): Kojarzy numeryczny adres IP Address z przyjazną dla człowieka nazwą.
- MAC Address**: fizyczny identyfikator wygrawerowany na karcie sieciowej, używany do transportu lokalnego (_Ethernet_). Gdy pakiet IP musi zostać fizycznie przesłany, tabela ARP dopasowuje IP Address do MAC Address miejsca docelowego.


Aby poradzić sobie z niedoborami Address IPv4 i dodać Layer bezpieczeństwa, sieci często korzystają z translacji Address (_NAT_). NAT umożliwia wielu prywatnym urządzeniom współdzielenie jednego publicznego adresu IP Address podczas uzyskiwania dostępu do Internetu.


**Uwaga**: Internetowe i wbudowane narzędzia systemu operacyjnego, takie jak [Grenoble CRIC calculator](http://cric.grenoble.cnrs.fr/Administrateurs/Outils/CalculMasque/), znacznie ułatwiają obliczenia podsieci i masek.

Narzędzia te pomagają efektywnie planować podział sieci.


Podsumowując, broadcast Address pozostaje praktyczną funkcją wysyłania tej samej wiadomości do wszystkich urządzeń podłączonych do segmentu: osiąga się to poprzez ustawienie wszystkich bitów w części HostID na 1, dzięki czemu wszystkie hosty są kierowane.



## Różne typy protokołów IPv4 Address


<chapterId>2adfad24-a90d-45b5-b808-3d2f6598bebf</chapterId>



Adresy IPv4 dzielą się na dwie główne kategorie: adresy publiczne, bezpośrednio dostępne w Internecie, oraz adresy prywatne, przeznaczone do użytku wewnętrznego w sieci lokalnej.


Publiczny adres IPv4 Address jest globalnie unikalny i routowalny w Internecie. Jest przypisywany przez oficjalne władze i wymagany dla usług publicznych, takich jak strony internetowe, serwery poczty e-mail lub infrastruktura chmury.

Unikalność tych adresów na całym świecie jest niezbędna, aby uniknąć konfliktów lub kolizji routingu.


Organ **IANA** (_Internet Assigned Numbers Authority_), działający w ramach **ICANN** (_Internet Corporation for Assigned Names and Numbers_), zarządza dystrybucją tych zakresów IP. Mówiąc konkretnie, IANA dzieli przestrzeń IPv4 na 256 bloków o rozmiarze /8, zgodnie z notacją CIDR. Każdy blok reprezentuje nieco ponad 16,7 miliona adresów (2³² / 2⁸).


Te unicastowe bloki Address są powierzane przez IANA **Regionalnym Rejestrom Internetowym** (RIR). Te RIR są odpowiedzialne za redystrybucję adresów na poziomie regionalnym, zgodnie z rzeczywistymi potrzebami dostawców dostępu, firm lub administracji. Przestrzeń unicast Address rozciąga się od bloków **1/8 do 223/8**, z częściami zarezerwowanymi do specjalnych zastosowań (badania, dokumentacja, testowanie) lub przydzielonymi bezpośrednio do sieci lub RIR w celu redystrybucji.


Aby sprawdzić, kto jest właścicielem publicznego adresu IP Address, można sprawdzić bazy danych RIR za pomocą polecenia **whois** lub korzystając z interfejsów internetowych udostępnianych przez każdy rejestr. Narzędzia te można wykorzystać do prześledzenia Address z powrotem do organizacji lub dostawcy, który go zadeklarował.


Z drugiej strony istnieją prywatne adresy IPv4, będące praktyczną odpowiedzią na niedobór adresów publicznych. Adresy te, których nie można routować w Internecie, są zarezerwowane dla środowisk lokalnych: sieci korporacyjnych, domowych sieci LAN, centrów danych lub klastrów obliczeniowych. Nie są one unikalne w skali światowej: wiele sieci prywatnych może ponownie wykorzystywać te same zakresy IP bez zakłóceń, o ile pozostają one odizolowane lub korzystają z sieciowego urządzenia translacyjnego Address w celu uzyskania dostępu do Internetu.


Aby umożliwić urządzeniu z prywatnym adresem IP Address dostęp do Internetu, sieci używają NAT (Network Address Translation). NAT działa poprzez dynamiczne zastępowanie prywatnego Address publicznym, umożliwiając dziesiątkom (lub nawet setkom) urządzeń współdzielenie jednego publicznego IP Address. Metoda ta optymalizuje wykorzystanie przestrzeni IPv4, a także dodaje Layer bezpieczeństwa, ukrywając wewnętrzną strukturę sieci.


Inną specjalną kategorią są **nieokreślone** adresy. Notacja IPv4 **0.0.0.0** lub jej wersja IPv6 **::/128** oznacza "brak określonego Address". Taki Address jest nieprawidłowy jako miejsce docelowe Address sieci, ale może być używany lokalnie przez hosta do wskazania "wszystkich interfejsów" lub "jeszcze nie przypisano Address". Jest to powszechne w dynamicznych Assignment DHCP lub do nasłuchiwania na wszystkich interfejsach serwera.


IPv6 obsługuje również adresowanie prywatne, ale standard ogólnie zaleca adresowanie publiczne, aby uniknąć tworzenia wielu warstw NAT. Adresy **site-local** (_site-local_) z bloku **fec0::/10** zostały wycofane przez **RFC 3879** ze względów spójności i bezpieczeństwa. Zostały one zastąpione przez **Unique Local Addresses** (_ULA_) znajdujące się w bloku **fc00::/7**. ULA umożliwiają tworzenie prywatnych sieci IPv6 z czystym routingiem wewnętrznym, przy użyciu losowo generowanego 40-bitowego identyfikatora w celu zapewnienia lokalnej unikalności.


Wyczerpanie IPv4 zostało oficjalnie potwierdzone w 2011 roku. Aby przedłużyć jego żywotność, społeczność internetowa przyjęła kilka strategii:


- Stopniowa migracja do **IPv6**
- Powszechne stosowanie **NAT**
- Bardziej rygorystyczna polityka alokacji od RIR, wymagająca dokładnego uzasadnienia i zarządzania potrzebami Address
- Odzyskiwanie niewykorzystanych lub dobrowolnie zwróconych bloków Address przez firmy


Środki te pokazują, że adresowanie IP jest nie tylko wyzwaniem technicznym, ale także kwestią globalnego zarządzania, kluczową dla ciągłej ekspansji Internetu.



## DNS, katalog Address


<chapterId>511244ec-ba43-44ac-b4c3-b41579a15cff</chapterId>



Bądźmy szczerzy, ludzie nie są świetni w zapamiętywaniu długich ciągów liczb, czy to w postaci binarnej, czy dziesiętnej. Wyzwanie to staje się jeszcze większe w przypadku adresów IP, które mogą być złożone, a pojedynczy adres IP Address może czasami maskować wiele adresów, zwłaszcza gdy stosowane są techniki takie jak NAT lub wirtualny hosting.


Aby ułatwić pracę, aplikacja Layer wykorzystuje system, który łączy adres IP Address z logiczną, czytelną dla człowieka nazwą. Jest to rola **DNS** (*Domain Name System*), ogromnego, hierarchicznego, rozproszonego katalogu, który dopasowuje czytelne nazwy domen do adresów IP. System opiera się na zestawie protokołów i usług. Najczęściej używanym oprogramowaniem serwera DNS jest **BIND** (_Berkeley Internet Name Domain_), pakiet oprogramowania open-source, który odwołuje się do znacznej części internetowej infrastruktury DNS.


Główna idea DNS jest prosta: dla każdej połączonej usługi, niezależnie od tego, czy jest to strona internetowa, serwer pocztowy czy inna usługa sieciowa, istnieje rekord mapujący nazwę domeny na jeden lub więcej adresów IP. Działa to w dwóch kierunkach:


- Forward resolution: tłumaczenie nazwy na adres IP Address.
- Rozdzielczość odwrotna: znajdowanie nazwy domeny powiązanej z danym adresem IP Address.

Sprawia to, że adresowanie sieciowe jest użyteczne dla ludzi, zachowując jednocześnie precyzję, której routery potrzebują do prawidłowego przesyłania danych.


Nazwa domeny ma zawsze strukturę hierarchiczną, z każdym poziomem oddzielonym kropką: pełna nazwa jest nazywana **FQDN** (_Fully Qualified Domain Name_). Najbardziej wysunięta na prawo część to **TLD** (_Top Level Domain_), taka jak `.com`, `.org` lub `.fr`. Najbardziej wysunięta na lewo część określa hosta, tj. konkretną maszynę lub usługę powiązaną z IP Address.


System DNS jest zaprojektowany jako **drzewo stref**. Strefa** jest sekcją przestrzeni nazw domeny zarządzaną przez konkretny serwer DNS. Pojedyncza strefa może zawierać wiele **subdomen**, które mogą być delegowane do innych stref zarządzanych przez różne serwery. Administratorzy są odpowiedzialni za utrzymanie swoich stref: obsługę aktualizacji, delegacji i ogólne zarządzanie.


Struktura ta pozwala nie tylko na wskazywanie na główną domenę (np. `example.com`), ale także na dostrajanie rekordów dla poszczególnych hostów (`www`, `mail`, `ftp`, itp.). We wczesnych dniach sieci, mapowanie to było obsługiwane za pomocą statycznych plików (`/etc/hosts` w systemach Unix), ale taka metoda szybko stała się niepraktyczna dla szybko rozwijającego się, połączonego Internetu.


Ważne jest, aby zrozumieć, że **serwer DNS** może obsługiwać tylko ograniczony zakres. Na przykład wewnętrzny serwer DNS firmy może nie być bezpośrednio dostępny z Internetu. Jeśli ten DNS nie jest skonfigurowany do przekazywania zapytań lub nie ma zaufanej relacji z innymi serwerami, niektóre zapytania zakończą się niepowodzeniem: ani nazwa, ani adres IP Address nie mogą zostać rozwiązane poza zdefiniowaną strefą.


DNS odgrywa również rolę w routingu wiadomości e-mail. Na przykład rekord **MX** (_Mail Exchange_) określa serwery pocztowe odpowiedzialne za odbieranie wiadomości e-mail dla danej domeny. Rekordy te definiują priorytety (współczynnik wagi) i rozwiązania awaryjne. Plik strefy serwera DNS musi zawierać rekord **SOA** (_Start Of Authority_), który wyznacza serwer jako oficjalne źródło informacji dla tej strefy.


Dzięki swojej hierarchicznej, rozproszonej strukturze DNS pozostaje kamieniem węgielnym Internetu, umożliwiając użytkownikom dostęp do usług za pośrednictwem jasnych, łatwych do zapamiętania nazw domen zamiast długich, technicznych adresów IP.


W następnym rozdziale zbadamy kolejną fundamentalną koncepcję: **Adresy Ethernet**, znane również jako **adresy MAC**, które zapewniają dostarczanie danych na fizycznym Layer sieci lokalnych.



## Odkrywanie adresów Ethernet i ARP


<chapterId>d02109f6-9bf9-4261-a8f9-e1aa4398b949</chapterId>



### Definicje


Aby protokół routingu danych działał niezawodnie i konsekwentnie, niezbędny jest jeden kluczowy komponent. Jako ludzie możemy łatwo zidentyfikować maszynę po jej adresie IP Address lub nazwie uzyskanej za pośrednictwem DNS. Maszyna musi jednak być w stanie jednoznacznie rozpoznać urządzenie docelowe w celu dostarczenia pakietów. Aby to zrobić, opiera się na konkretnym identyfikatorze sprzętowym, bezpośrednio używanym przez sieć Interface: MAC Address (_Media Access Control_).


**Uwaga**: Nie ma to nic wspólnego z "fizycznym Address" w architekturze pamięci. W informatyce pamięć fizyczna Address odnosi się do określonej lokalizacji na magistrali pamięci, w przeciwieństwie do wirtualnej Address zarządzanej przez system operacyjny. Natomiast MAC Address odnosi się wyłącznie do sprzętu sieciowego.


MAC Address jest trwale i jednoznacznie przypisany przez producenta sprzętu. MAC Address jednoznacznie identyfikuje kartę sieciową, niezależnie od tego, czy jest to komputer, smartfon, drukarka czy inne podłączone urządzenie. W przeciwieństwie do IP Address, który może zmieniać się dynamicznie (za pośrednictwem serwera DHCP lub ręcznej konfiguracji), MAC Address zwykle pozostaje taki sam przez cały okres użytkowania urządzenia, chyba że zostanie celowo zmieniony.


Każda sieć Interface, przewodowa lub bezprzewodowa, ma swój własny MAC Address. Ten Address jest używany w ramach łącza danych Layer (Layer 2 modelu OSI) do wstawiania i zarządzania sprzętowym Address w każdej wymienianej ramce sieciowej. Jest on czasami określany jako adres _Ethernet_ lub _UAA_ (_Universally Administered Address_). Standardowo ma on długość 48 bitów lub 6 bajtów i jest zapisywany w notacji szesnastkowej, zazwyczaj w postaci bajtów oddzielonych znakami `:` lub `-`.


Na przykład: `5A:BC:17:A2:AF:15`


W tej strukturze pierwsze trzy bajty identyfikują producenta karty sieciowej: jest to znane jako **OUI** (*Organisationally Unique Identifier*). Te prefiksy, przypisane przez IEEE, są również używane w innych schematach adresowania sprzętu, takich jak Bluetooth i LLDP, aby zagwarantować unikalność na całym świecie.


### Zmiana adresu MAC Address (MAC Spoofing)


Teoretycznie MAC Address ma pozostać stały, ale istnieją sposoby na jego modyfikację, zwłaszcza w celu zaspokojenia określonych potrzeb lub obejścia pewnych ograniczeń. Operacja ta, często określana jako _spoofing MAC_, polega na zastąpieniu oryginalnego sprzętowego Address inną wartością, zdefiniowaną na poziomie oprogramowania. Niektóre systemy operacyjne ułatwiają tę modyfikację, zwłaszcza gdy rzeczywisty Address Ethernet nie jest bezpośrednio używany przez sterownik.


Powody takiej zmiany są różne. Może to być potrzeba, aby dana aplikacja wymagała określonej sieci Ethernet Address w celu prawidłowego działania lub rozwiązania konfliktu identycznych adresów między dwoma urządzeniami współdzielącymi tę samą sieć lokalną.


Zmiana MAC Address może być również motywowana względami prywatności: ukrywając unikalny identyfikator wygrawerowany na karcie, użytkownicy zmniejszają możliwość śledzenia ich urządzenia przez sieci lub usługi nadzoru. Praktyka ta nie jest jednak pozbawiona konsekwencji. Zmiana MAC Address może zakłócić działanie niektórych urządzeń filtrujących lub wymagać rekonfiguracji zapór sieciowych w celu autoryzacji nowego sprzętu.


Niektóre sieci, zwłaszcza Wi-Fi, używają filtrowania MAC Address, aby zezwolić tylko na urządzenia z zatwierdzonymi adresami. Chociaż zapewnia to podstawowy poziom kontroli, samo w sobie nie jest bezpieczne. Atakujący może przechwycić prawidłowy MAC Address już autoryzowany w sieci i sklonować go w celu ominięcia ograniczeń. Z tego powodu filtrowanie adresów MAC powinno być zawsze połączone z silniejszymi środkami bezpieczeństwa.


### Korespondencja MAC/IP


Aby sieć lokalna działała wydajnie, musi istnieć wyraźne mapowanie między adresami fizycznymi (adresami MAC) a adresami logicznymi (adresami IP). Bez tego połączenia komputer może znać adres IP Address miejsca docelowego, ale nie będzie wiedział, jak fizycznie wysłać do niego dane w sieci lokalnej.

Mapowanie to jest obsługiwane automatycznie przez protokół ARP (_Address Resolution Protocol_).


W praktyce, gdy użytkownik chce poznać adres MAC Address odpowiadający określonemu adresowi IP Address, może użyć narzędzia `arp`. Narzędzie to sprawdza lokalną tabelę ARP maszyny, aby wyświetlić znane dopasowania między adresami IP i adresami MAC w sieci lokalnej. W ten sposób można szybko zweryfikować efektywne połączenie między warstwą logiczną i fizyczną.


Praktyczny przykład: jeśli chcesz sprawdzić, która karta sieciowa odpowiada adresowi IP Address `192.168.1.5`, użyj następującego polecenia:


```bash
arp –a 192.168.1.5
```


Na wyjściu zostanie wyświetlony powiązany fizyczny Address (MAC), charakter wejścia (statyczny lub dynamiczny) i dany Interface.


```
Interface: 192.168.1.5 --- 0x5
IP Address            MAC Address                Type
192.168.1.5           00:54:BC:17:14:6E          D
```


Ważne jest, aby pamiętać, że MAC Address i IP Address to dwa zupełnie różne identyfikatory, ale ściśle się uzupełniające. MAC Address jest unikalnie wygrawerowany w każdym sieciowym Interface przez producenta i służy do fizycznej identyfikacji urządzenia w sieci lokalnej. IP Address, z drugiej strony, jest logicznym Address przypisywanym dynamicznie lub statycznie, umożliwiając maszynie dołączenie do sieci IP i pakietów Exchange poza siecią lokalną.



- Wizualny przykład MAC Address:


![Image](assets/fr/032.webp)




- Wizualny przykład Address IP:


![Image](assets/fr/027.webp)



W środowisku korporacyjnym te dwa poziomy adresowania nie mogą funkcjonować oddzielnie. Na przykład, gdy serwer DHCP automatycznie przypisuje IP Address, MAC Address urządzenia jest używany jako punkt wyjścia. Komputer wysyła żądanie transmisji DHCP zawierające jego MAC Address, aby serwer mógł przypisać dostępny IP Address do właściwego urządzenia. Bez tej identyfikacji sprzętu serwer DHCP nie wiedziałby, do którego urządzenia dostarczyć Address.


Protokół ARP ma zatem fundamentalne znaczenie: zapewnia połączenie między adresami IP i adresami fizycznymi, umożliwiając maszynom tłumaczenie logicznego miejsca docelowego na rzeczywiste fizyczne miejsce docelowe. Gdy komputer musi wysłać pakiet do maszyny w tej samej sieci, najpierw sprawdza swoją tabelę ARP, aby sprawdzić, czy adres MAC odbiorcy Address jest już znany. Jeśli nie, wysyła żądanie ARP do wszystkich hostów w sieci lokalnej. Maszyna, która rozpoznaje docelowy adres IP Address w tym żądaniu, odpowiada, określając swój adres MAC Address. Następnie nadawca zapisuje tę parę IP/MAC w swojej pamięci podręcznej ARP, aby uniknąć konieczności powtarzania operacji za każdym razem, gdy wysyłane jest żądanie.


Ta tabela ARP działa jak mini katalog mapowania, dynamicznie aktualizowany w podobny sposób, w jaki DNS kojarzy nazwy domen z adresami IP. Bez ARP lokalny Exchange nie byłby możliwy, ponieważ łącze danych Layer musi znać MAC Address, aby poprawnie enkapsulować ramki Ethernet.


I odwrotnie, protokół RARP (_Reverse Address Resolution Protocol_) został zaprojektowany dla odwrotnej sytuacji: umożliwiając maszynie, która zna tylko swój MAC Address, odkrycie swojego IP Address. Było to powszechne w przypadku starszych stacji roboczych bez lokalnego dysku Hard, które musiały uruchamiać się przez sieć i żądać IP Address. RARP został ostatecznie zastąpiony przez **BOOTP**, a następnie **DHCP**, które są bardziej elastyczne i zautomatyzowane.


Te protokoły asocjacyjne odgrywają ważną rolę w routingu. Router jest zasadniczo maszyną z wieloma interfejsami sieciowymi, łączącymi różne segmenty. Gdy router odbiera ramkę, przetwarza ją w celu wyodrębnienia datagramu IP i sprawdza nagłówek IP w celu określenia miejsca docelowego. Jeśli miejsce docelowe znajduje się w bezpośrednio połączonej sieci, datagram jest dostarczany bezpośrednio po zaktualizowaniu nagłówka. Jeśli miejsce docelowe należy do innej sieci, router sprawdza swoją tabelę routingu, aby zidentyfikować najlepszą ścieżkę lub _next hop_ do miejsca docelowego.


Pozwala to podzielić trasę na krótsze, łatwiejsze w zarządzaniu segmenty. Każdy router pośredni zna tylko następny krok, niekoniecznie miejsce docelowe.


**Przypomnienie:** Dostawa bezpośrednia ma miejsce, gdy nadawca i odbiorca znajdują się w tej samej sieci fizycznej. W przeciwnym razie dostawa jest pośrednia i przechodzi przez jeden lub więcej routerów.


Tablica routingu, zarządzana ręcznie (routing statyczny) lub dynamicznie (routing dynamiczny), zawiera informacje potrzebne do podjęcia decyzji o wyborze trasy. W małych sieciach wystarczy konfiguracja statyczna. W większych infrastrukturach routing dynamiczny jest niezbędny do automatycznego dostosowywania tras w przypadku zmiany topologii lub awarii łącza.


Tabela routingu działa jako tabela mapowania między docelowymi adresami IP i następnymi bramami. Zwykle przechowuje ona identyfikatory sieci (_network ID_), a nie każdego hosta Address, co znacznie zmniejsza jej rozmiar.


| Destination Address | Next-Hop Router Address | Interface |
| ------------------- | ----------------------- | --------- |

Korzystając z tych wpisów, router może szybko określić, przez który Interface i do którego węzła powinien zostać wysłany każdy datagram. W połączeniu z ARP do rozwiązywania pasujących adresów MAC, zapewnia to wydajny i niezawodny transfer danych w sieci.


Wreszcie, dynamiczne protokoły routingu obejmują standardy takie jak RIP (_Routing Information Protocol_), oparty na algorytmie odległości i OSPF (_Open Shortest Path First_), który oblicza najkrótsze ścieżki w złożonej topologii. Protokoły te stale aktualizują Exchange w celu optymalizacji tras, zmniejszenia kosztów transmisji i poprawy odporności na awarie lub przeciążenia.



## NAT: Tłumaczenie Address


<chapterId>4f984d5d-f2e0-4faf-b703-ff315f32cef4</chapterId>



### Definicja


Network Address Translation_ (NAT) to technika opracowana w celu Address stopniowego wyczerpywania się dostępnych adresów IPv4. Zaprojektowany jako rozwiązanie tymczasowe przed powszechnym przyjęciem IPv6, NAT umożliwił firmom i osobom prywatnym łączenie dużej liczby maszyn przy użyciu tylko ograniczonego zestawu publicznych adresów IP.


**Ważne przypomnienie:** Przejście z IPv4 na IPv6 teoretycznie rozwiązuje problem wyczerpania poprzez rozszerzenie przestrzeni Address z 32 do 128 bitów, zapewniając niemal nieograniczoną liczbę adresów (2^128). W praktyce jednak przejście to jest nadal niekompletne, a NAT jest nadal szeroko stosowany.


Zasada działania NAT jest prosta, ale bardzo skuteczna: zamiast przypisywać unikalny publiczny adres IP Address do każdego urządzenia w sieci wewnętrznej, dla wszystkich urządzeń prywatnych używany jest pojedynczy routowalny adres Address (lub niewielka pula adresów). Brama NAT, często zintegrowana z routerem lub zaporą sieciową, dynamicznie tłumaczy wewnętrzny adres IP Address wraz z informacjami potrzebnymi do prawidłowego kierowania ruchu do świata zewnętrznego i zapewnia, że odpowiedzi są zwracane do pierwotnego nadawcy.


Takie podejście ma natychmiastową zaletę: całkowicie ukrywa wewnętrzną architekturę sieci. Dla zewnętrznego obserwatora wszystkie żądania ze stacji roboczych, serwerów lub drukarek wydają się pochodzić z tej samej tożsamości publicznej. Adresy prywatne, zwykle pobierane z zarezerwowanych zakresów (np. 192.168.x.x lub 10.x.x.x), pozostają niewidoczne z Internetu.


Oprócz rozwiązania problemu niedoboru IPv4, NAT wzmacnia również bezpieczeństwo, tworząc pierwszą logiczną barierę między sieciami wewnętrznymi i publicznymi. Niechciana komunikacja przychodząca jest naturalnie blokowana, ponieważ tylko połączenia zainicjowane z wewnątrz sieci korzystają z niezbędnej translacji, aby otrzymywać odpowiedzi.



![Image](assets/fr/035.webp)



### Rodzaje tłumaczeń


NAT może być zaimplementowany na różne sposoby w celu dostosowania do konkretnych potrzeb. Dwa główne tryby działania to translacja statyczna i translacja dynamiczna.


**Tłumaczenie statyczne** tworzy stałe mapowanie pomiędzy prywatnym IP Address i publicznym IP Address. Każde urządzenie wewnętrzne jest na stałe powiązane z dedykowanym publicznym Address. Na przykład urządzenie wewnętrzne skonfigurowane jako 192.168.20.1 może być powiązane z rutowalnym Address 157.54.130.1. Gdy pakiet wychodzący opuszcza sieć lokalną, router zastępuje źródłowy Address pakietu publicznym Address i wykonuje odwrotną operację dla ruchu przychodzącego. Ta dwukierunkowa translacja jest przezroczysta dla użytkownika.


**Ostrzeżenie:** Podczas gdy ta metoda izoluje sieć wewnętrzną, nie rozwiązuje problemu niedoboru publicznych adresów IP, ponieważ nadal potrzebujesz tylu adresów publicznych, ile jest maszyn do ujawnienia. Translacja statyczna jest zatem używana głównie wtedy, gdy niektóre zasoby wewnętrzne muszą pozostać osiągalne z zewnątrz (serwer WWW, serwer pocztowy...).


*z drugiej strony * translacja dynamiczna** wykorzystuje pulę publicznych adresów IP. Gdy wewnętrzny host rozpoczyna połączenie, router tymczasowo przypisuje jeden z tych publicznych adresów do prywatnego Address hosta na czas trwania sesji. Połączenie jest 1 do 1, ale tymczasowe: po zakończeniu połączenia publiczny Address staje się dostępny dla innego urządzenia. Dynamiczny NAT zmniejsza zatem liczbę potrzebnych adresów publicznych, gdy nie wszystkie maszyny są online w tym samym czasie, ale nadal wymaga bloku adresów zewnętrznych co najmniej tak dużego, jak maksymalna liczba jednoczesnych połączeń.


**Port translation** (PAT), znany również jako *NAT overload* lub *IP masquerading*, idzie o krok dalej: wszystkie prywatne urządzenia współdzielą jeden publiczny adres IP Address (lub bardzo małą liczbę). Aby rozróżnić sesje, brama modyfikuje nie tylko źródłowy Address, ale także port źródłowy. Utrzymuje tabelę łączącą każdą parę *(prywatny Address, port prywatny)* z unikalną parą *(publiczny Address, port publiczny)*. Ta forma NAT jest używana w prawie wszystkich routerach domowych, umożliwiając dziesiątkom urządzeń (komputerów, smartfonów, podłączonych obiektów itp.) współdzielenie tego samego publicznego adresu IP Address, przy jednoczesnym zachowaniu płynnej komunikacji.


NAT przedłuża zatem żywotność IPv4, jednocześnie dodając cenną Layer segmentacji i bezpieczeństwa. Jednak wraz ze wzrostem popularności protokołu IPv6 i coraz szerszym wykorzystaniem jego ogromnej przestrzeni Address, rola NAT prawdopodobnie spadnie, choć ze względu na kompatybilność i kontrolę będzie on nadal używany w niektórych środowiskach do segmentacji i filtrowania ruchu.


### Implementacja NAT


Aby zapewnić prawidłowe działanie translacji Address, router lub brama NAT musi przechowywać dokładny zapis mapowań ustanowionych między każdym prywatnym Address w sieci wewnętrznej i publicznym Address, którego używa do komunikacji ze światem zewnętrznym. Informacje te są przechowywane w tak zwanej "tabeli translacji NAT", która odgrywa kluczową rolę w zarządzaniu ruchem sieciowym.


Każdy wpis w tej tabeli łączy co najmniej jedną parę: wewnętrzny adres IP Address maszyny wysyłającej i zewnętrzny adres IP Address, który będzie widoczny w Internecie. Gdy pakiet z sieci prywatnej jest wysyłany do publicznego miejsca docelowego, router NAT przechwytuje ramkę, analizuje nagłówki IP i TCP/UDP, a następnie zastępuje prywatny źródłowy Address publicznym Address bramy. Na ścieżce powrotnej ta sama brama przechwytuje przychodzący pakiet, sprawdza tabelę mapowania i wykonuje operację odwrotną, aby przekierować przepływ do oryginalnego wewnętrznego adresu IP Address.


Ta zasada dynamicznej translacji opiera się na precyzyjnym zarządzaniu tabelą: każdy wpis pozostaje ważny tak długo, jak długo istnieje aktywny ruch, który go uzasadnia. Po konfigurowalnym okresie bezczynności wpis jest czyszczony i może być ponownie użyty dla nowych połączeń.


przykład uproszczonej tabeli translacji NAT:_


| Internal IP   | External IP    | Duration (sec) | Reusable? |
| ------------- | -------------- | -------------- | --------- |
| 10.101.10.20  | 193.48.100.174 | 1,200          | no        |
| 10.100.54.251 | 193.48.101.8   | 3,601          | yes       |
| 10.100.0.89   | 193.48.100.46  | 0              | no        |

W tym przykładzie, jeśli żaden pakiet nie przeszedł przez drugi wpis w ciągu ponad godziny (3600 sekund), jest on oznaczony jako wielokrotnego użytku. I odwrotnie, czas trwania równy zero wskazuje na aktywną komunikację z zablokowanym mapowaniem.


Podczas gdy NAT działa w sposób przezroczysty dla większości typowych zastosowań (przeglądanie stron internetowych, poczta e-mail, przesyłanie plików itp. Niektóre technologie polegają na wyraźnej wymianie adresów IP lub portów w ładunku pakietu. Po przejściu przez bramę NAT informacje te stają się niespójne.


Typowe przykłady ograniczeń obejmują:


- Protokoły peer-to-peer (P2P), które wymagają bezpośrednich połączeń między urządzeniami, są utrudnione przez barierę NAT, ponieważ wszystkie wewnętrzne maszyny współdzielą ten sam zewnętrzny adres IP Address i nie mogą być dostępne bezpośrednio bez specjalnej konfiguracji (takiej jak *przekierowanie portów* lub UPnP);
- Protokół IPSec, używany do zabezpieczania komunikacji sieciowej, szyfruje nagłówki pakietów. Ponieważ NAT musi modyfikować te nagłówki, aby zastąpić adresy IP, szyfrowanie uniemożliwia to bez mechanizmów adaptacyjnych, takich jak NAT-T (*NAT Traversal*);
- Protokół X Window, który umożliwia zdalne wyświetlanie aplikacji graficznych w systemie Unix/Linux, działa w taki sposób, że serwer X aktywnie wysyła połączenia TCP do klientów. To odwrócenie zwykłego kierunku połączeń może zostać zablokowane przez NAT.


Ogólnie rzecz biorąc, będzie to miało wpływ na każdy protokół, który wyraźnie zawiera wewnętrzny Address IP w ładunku pakietu, ponieważ ten Address nie będzie już odpowiadał rzeczywistemu, widocznemu w Internecie Address po translacji.


**Ważna uwaga:** W celu Address tych kwestii, niektóre routery NAT oferują _Deep Packet Inspection_ (DPI) lub _Protocol Helpers_ , które sprawdzają zawartość pakietów w celu identyfikacji i dynamicznego zastępowania adresów lub numerów portów w danych aplikacji. Wymaga to dogłębnej znajomości formatu protokołu i może powodować luki w zabezpieczeniach lub zwiększać wykorzystanie zasobów.


**Uwaga:** Chociaż NAT pomaga ukryć sieć wewnętrzną i kontrolować ruch przychodzący, nie zastępuje dedykowanej zapory sieciowej. Samo tłumaczenie nie jest kompletną barierą bezpieczeństwa: zawsze musi być uzupełnione jasnymi regułami filtrowania w celu zablokowania niechcianego lub niepożądanego ruchu.


aby zilustrować, jak to działa w praktyce, rozważmy następujący przykład:_



![Image](assets/fr/037.webp)



W tym scenariuszu wewnętrzna stacja robocza może uzyskać dostęp do wewnętrznego serwera WWW po prostu wywołując adres URL `http://192.168.1.20:80`. Określenie portu jest tutaj opcjonalne, ponieważ `80` jest standardowym portem HTTP. I odwrotnie, jeśli żądanie zostanie zainicjowane z zewnątrz, użytkownik wprowadzi publiczny Address `http://85.152.44.14:80`. Router NAT odbiera żądanie, sprawdza swoją tabelę mapowania i automatycznie tłumaczy publiczny Address na prywatny, przekierowując połączenie na `http://192.168.1.20:80`.


Ta sama zasada dotyczy każdego innego serwera uprawnionego do odbierania połączeń internetowych, takiego jak serwer Extranet (niebieski obwód na schemacie).


**Uwaga praktyczna:** w środowiskach zwirtualizowanych powszechnie używane są interfejsy sieciowe zwane _virbrX_ (od _Virtual Bridge X_). Te wirtualne mosty, dostarczane w szczególności przez bibliotekę libvirt lub hiperwizor Xen, łączą wirtualną sieć wewnętrzną maszyn-gości z siecią fizyczną, jednocześnie stosując NAT. Są one zazwyczaj konfigurowane za pomocą skryptów w `/etc/sysconfig/network-scripts/`, jak pokazano poniżej dla `virbr0`:


```ini
NAME=""
BOOTPROTO=none
MACADDR=""
TYPE=Bridge
DEVICE=virbr0
NETMASK=255.255.255.0
MTU=""
BROADCAST=192.168.0.255
IPADDR=192.168.0.1
NETWORK=192.168.0.0
ONBOOT=yes
```


Po uruchomieniu wirtualnego mostu należy włączyć routing IP i skonfigurować translację portów za pomocą `iptables`:


```shell
echo 1 > /proc/sys/net/ipv4/ip_forward
```


```shell
iptables -t nat -A POSTROUTING -o <WAN> -s 192.168.0.0/24 -j MASQUERADE
```


W tej konfiguracji ruch wychodzący jest kierowany, a translacja NAT jest stosowana, umożliwiając maszynom wirtualnym komunikację ze światem zewnętrznym bez bezpośredniego ujawniania ich wewnętrznych adresów IP.


W następnym rozdziale przyjrzymy się szczegółowo konfiguracji IP Address w systemie Linux, obejmującej zarówno proste, jak i zaawansowane metody dostosowane do różnych kontekstów administracyjnych.



https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864


## Jak skonfigurować sieć za pomocą `ip`?


<chapterId>8ba7e946-d2a0-4841-8d54-e85ba96baa25</chapterId>



### Standardowa konfiguracja


Po omówieniu teoretycznych podstaw sieci i zrozumieniu, jak adresy IP, maski, routing i translacja działają razem, nadszedł czas, aby przejść do praktycznej konfiguracji. W systemie GNU/Linux konfiguracja sieci jest teraz obsługiwana za pomocą polecenia **`ip`** (pakiet _iproute2_), które zastępuje starsze `ifconfig`.


`ip` umożliwia przypisanie lub zmianę adresu IP Address, zmianę maski, uruchomienie lub zatrzymanie Interface lub sprawdzenie jego statusu w dowolnym momencie.


**Aby wyświetlić wszystkie interfejsy (aktywne lub nie): `ip addr show`


Przykład: przypisanie statycznego Address i aktywacja Interface


Dodaj Address `192.168.1.2/24` do Interface `eth0`:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Aktywuj Interface:


```shell
ip link set dev eth0 up
```


Dezaktywacja tego samego Interface:


```shell
ip link set dev eth0 down
```


Wyświetla stan określonego Interface:


```shell
ip addr show dev eth2
```


**Praktyczna wskazówka:** z `ip`, dodanie dodatkowego Address do Interface nie wymaga już przyrostka `:1`. Wystarczy dodać kolejną linię `ip addr add ...`:


```shell
ip addr add 172.18.2.39/24 dev eth2
```


### Skrypty aktywacyjne: ifup / ifdown


Narzędzia `ifup` i `ifdown` odczytują statyczne pliki konfiguracyjne z `/etc/sysconfig/network-scripts/` (w RHEL, CentOS, Rocky Linux, AlmaLinux...) lub `/etc/network/interfaces` (w Debianie/Ubuntu), aby czysto włączać i wyłączać interfejsy.


```shell
ifup eth1
ifdown eth2
```


Pliki konfiguracyjne (podobne do RHEL):


- /etc/sysconfig/network**: ustawienia globalne (NETWORKING, HOSTNAME, GATEWAY...).
- ifcfg-**: ustawienia specyficzne dla każdego Interface.


Przykład statyczny (ifcfg-eth0):


```ini
DEVICE=eth0
BOOTPROTO=none
ONBOOT=yes
IPADDR=192.168.2.5
NETMASK=255.255.255.0
GATEWAY=192.168.2.1
```


Przykład DHCP:


```ini
DEVICE=eth0
BOOTPROTO=dhcp
ONBOOT=yes
```


Ta modułowa struktura jest nadal aktualna i może być łatwo zautomatyzowana w obecnych systemach.


### Konfiguracja zaawansowana: łączenie


W środowiskach profesjonalnych celem jest zagwarantowanie ciągłości usług i/lub agregacja przepustowości. *Mechanizmy bonding* (lub *teaming* z _teamd_) spełniają te potrzeby: kilka fizycznych interfejsów funkcjonuje jako pojedynczy logiczny Interface, często nazywany `bond0` lub `team0`.



![Image](assets/fr/039.webp)



Wymagania wstępne:


- Załaduj moduł `bonding` (lub użyj `teamd`);
- Dostępne są co najmniej dwa interfejsy fizyczne.


#### Różne popularne metody łączenia:


|Mode|Name|Principle|
|---|---|---|
|0|balance-rr|Round-robin, cyclic distribution of frames|
|1|active-backup|Single active interface with hot failover |
|2|balance-xor|Selection based on XOR of src/dst MAC addresses|
|3|broadcast|Broadcast simultaneously on all interfaces   |
|4|802.3ad (LACP)|Standardized dynamic aggregation; requires compatible switch|
|5|tlb (Transmit Load Balancing)|Balancing based on transmit load|
|6|alb (Adaptive Load Balancing)|Adaptive balancing; also balances receive via ARP|

#### Konfiguracja za pomocą `ip link



- Wyłączenie interfejsów fizycznych:


```shell
ip link set eth0 down
ip link set eth1 down
```



- Utwórz połączony Interface:


```shell
ip link add bond0 type bond mode balance-alb
```



- Konfiguracja opcji po utworzeniu


```shell
ip link set bond0 type bond miimon 100
```



- Przypisywanie adresów MAC i IP:


```shell
ip link set dev bond0 address 00:17:56:BC:02:3A
ip addr add 192.168.2.3/24 dev bond0
ip route add default via 192.168.2.1
```



- Dołączanie interfejsów podrzędnych:


```shell
ip link set eth0 master bond0
ip link set eth1 master bond0
```



- Podnieś wszystko z powrotem:


```shell
ip link set bond0 up
ip link set eth0 up
ip link set eth1 up
```


**Wskazówka:** aby odłączyć urządzenie podrzędne bez zdejmowania powiązania: `ip link set eth1 nomaster`


#### Stała konfiguracja (podobna do RHEL)


Utwórz trzy pliki w `/etc/sysconfig/network-scripts`:


_ifcfg-bond0_


```ini
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=none
IPADDR=192.168.2.3
NETMASK=255.255.255.0
BROADCAST=192.168.2.255
GATEWAY=192.168.2.1
BONDING_OPTS="mode=balance-alb miimon=100"
```


_ifcfg-eth0_


```ini
DEVICE=eth0
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```


_ifcfg-eth1_


```ini
DEVICE=eth1
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```


Następnie:


```shell
systemctl restart network
```


#### Dodatkowy adres IP Address (nowoczesny alias)


Dzięki `ip` można po prostu dodać drugi Address do tego samego urządzenia:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Aby alias ten pozostał po restarcie, należy dodać drugi blok `IPADDR2=...` / `PREFIX2=...` do `ifcfg-eth0` lub utworzyć nowe połączenie *NetworkManager* poprzez `nmcli`.


Dzięki `ip` i powiązanym poleceniom (`ip link`, `ip addr`, `ip route`) konfiguracja sieci jest bardziej spójna, skryptowalna i przejrzysta. Łączenie jest kluczowym elementem architektur wysokiej dostępności, a przypisywanie wielu adresów do pojedynczego Interface stało się znacznie prostsze.


W następnym rozdziale przyjrzymy się szczegółom i implementacji adresowania IPv6.


# Adresowanie IPv6


<partId>9b1d87f1-2a68-496e-b5dd-76cf74fb8cde</partId>


## IPv6: Standardy i definicje


<chapterId>d1f16f0a-1104-460d-8d67-f725665f8e3f</chapterId>



Przechodzimy teraz do następnej generacji adresowania IP: protokołu IPv6, pierwotnie znanego jako IPng (_IP Next Generation_). Protokół ten, zaprojektowany w celu przezwyciężenia ograniczeń strukturalnych IPv4, wprowadza znacznie rozszerzoną architekturę adresowania, a także liczne optymalizacje techniczne.


Motywacje stojące za przyjęciem protokołu IPv6 są zróżnicowane i Address krytyczne dla ewolucji Internetu. Po pierwsze, rolą IPv6 jest wspieranie wykładniczego wzrostu liczby podłączonych urządzeń (cel nieosiągalny przy ograniczonej przestrzeni Address IPv4). Po drugie, protokół ten ma na celu zmniejszenie rozmiaru tablic routingu, dzięki czemu wymiana danych będzie bardziej wydajna i zmniejszy obciążenie routerów w dłuższej perspektywie.


IPv6 ma również na celu uproszczenie niektórych aspektów obsługi pakietów, poprawę przepływu datagramów i optymalizację prędkości transferu między sieciami. Z punktu widzenia bezpieczeństwa, nagłówki AH/ESP protokołu *IPsec* są zawarte w specyfikacji bazowej i wszystkie węzły IPv6 muszą być w stanie je obsługiwać (RFC 6434). Ich użycie pozostaje jednak opcjonalne: od administratora zależy ich włączenie w zależności od kontekstu.


Inne cele obejmują bardziej precyzyjną obsługę typów usług, w szczególności w celu zapewnienia lepszej jakości dla aplikacji działających w czasie rzeczywistym (VoIP, wideokonferencje itp.). IPv6 został również zaprojektowany w celu umożliwienia bardziej elastycznego zarządzania mobilnością: urządzenie może zmieniać punkty dostępu bez zmiany swojego Address w sposób widoczny dla swoich rówieśników.


Wreszcie, IPv6 został zaprojektowany do współistnienia ze starszymi protokołami. Chociaż nie jest on bezpośrednio binarnie kompatybilny z IPv4, pozostaje w pełni interoperacyjny z protokołami wyższego poziomu Layer, takimi jak TCP, UDP, ICMPv6 i DNS, a także z protokołami routingu, takimi jak OSPF i BGP, z zastrzeżeniem pewnych dostosowań. Do zarządzania multiemisją, IPv6 wykorzystuje protokół MLD (*Multicast Listener Discovery*), który jest funkcjonalnym odpowiednikiem IGMP w środowisku IPv4.


### Zasady notacji


Jedną z najbardziej znaczących zmian w IPv6 jest format samego adresu IP Address. Aby zaradzić chronicznemu niedoborowi adresów IPv4, długość Address została zwiększona z 32 bitów do 128 bitów, czyli 16 bajtów. Teoretycznie daje to możliwą przestrzeń Address wynoszącą:


$$3,4 razy 10^{38}$$


Zapewnia to praktycznie nieograniczoną pojemność dla wszystkich obecnych i przyszłych urządzeń.


Adresy IPv6 są zapisywane zupełnie inaczej niż w znanej notacji dziesiętnej z kropkami. Adres IPv6 Address składa się z ośmiu 16-bitowych grup, zapisanych w systemie szesnastkowym i oddzielonych dwukropkami `:`.


Na przykład:


```
1987:0c02:0000:84c2:0000:0000:cf2a:9077
```


Aby uprościć zapis, można pominąć początkowe zera w każdej grupie. Powyższy przykład będzie miał postać:


```
1987:c02:0:84c2:0:0:cf2a:9077
```


Ponadto pojedyncza ciągła sekwencja grup zerowych może zostać zastąpiona przez::, co dodatkowo skraca Address:


```
1987:c02:0:84c2::cf2a:9077
```


**Ostrzeżenie:** ta reguła jest ścisła: tylko jedna sekwencja kolejnych zer może być zastąpiona przez `::`. Jeśli Address zawiera wiele sekwencji zer, tylko najdłuższa z nich jest skondensowana. Zapewnia to zarówno unikalność, jak i czytelność.


**Ważny szczegół:** Znak `:` używany do oddzielania bloków szesnastkowych może powodować niejednoznaczność w adresach URL, ponieważ `:` jest również używany do wskazania portu usługi. Aby uniknąć nieporozumień, adresy IPv6 w URL muszą być ujęte w nawiasy kwadratowe `[ ]`.


Przykład dostępu HTTP do określonego portu dla Address `2002:400:2A41:378::34A2:36`:


```
http://[2002:400:2A41:378::34A2:36]:8080
```


Podczas reprezentowania Address IPv4 w kontekście IPv6, można użyć notacji mieszanej w postaci dziesiętnej z kropkami, poprzedzonej`::`:


```
::192.168.1.5
```


Ta kompatybilność pomaga ułatwić przejście między dwoma protokołami, umożliwiając włączenie bloków IPv4 do przestrzeni IPv6 Address.


**Uwaga:** Aby ustandaryzować sposób zapisu adresów, RFC 5952 definiuje format kanoniczny z regułami skrótów, aby uniknąć wielu reprezentacji tego samego Address. Przestrzeganie tych zaleceń pomaga ograniczyć błędną interpretację i zapewnia spójne konfiguracje sieci.


### Typy IPv6 Address


IPv6 różni się od swojego poprzednika szerokim zakresem kategorii Address, z których każda została zaprojektowana do określonych zastosowań, umożliwiając jednocześnie elastyczny routing i zarządzanie siecią. Podobnie jak w przypadku IPv4, adresy mogą być globalne, lokalne, zarezerwowane lub specyficzne dla określonych mechanizmów przejściowych.


Nieokreślony IPv6 Address jest reprezentowany przez `::` lub, bardziej wyraźnie, `::0.0.0.0`. Ta specjalna forma jest używana podczas pozyskiwania Address lub jako wartość domyślna wskazująca na brak Address.



| IPv6 Address Prefix | Description                                 |
| ------------------- | ------------------------------------------- |
|::/8                | Reserved addresses                          |
| 2000::/3            | Unicast addresses, routable on the Internet |
| fc00::/7            | Unique local addresses (1)                  |
| fe80::/10           | Link-local addresses                        |
| ff00::/8            | Multicast addresses                         |

(1): *W prywatnej sieci LAN prefiks `fd00::/8` jest preferowany do przypisywania adresów wewnętrznych, które nie są routowalne w Internecie


#### Zarezerwowane adresy


Niektóre zakresy IPv6 są wyraźnie zarezerwowane i nie mogą być używane jako adresy globalne. Mają one określone cele techniczne:


- `::/128`**: nieokreślony Address, nigdy nie przypisany na stałe do urządzenia, ale używany jako źródłowy Address przez maszynę oczekującą na konfigurację.
- `::1/128`**: _loopback_ Address, bezpośredni odpowiednik `127.0.0.1` w IPv4, który pozwala maszynie na Address.
- `64:ff9b::/96`**: Zarezerwowane dla translatorów protokołów, aby umożliwić wzajemne połączenia IPv4/IPv6, zgodnie z definicją w RFC 6052.
- `::ffff:0:0/96`**: blok zgodności do reprezentowania Address IPv4 w określonej strukturze IPv6, często używany wewnętrznie przez aplikacje.


Bloki te gwarantują interoperacyjność i ułatwiają migrację między dwiema wersjami protokołu.


#### Globalne adresy unicast


Globalne adresy unicastowe stanowią większość publicznie routowalnej przestrzeni IPv6, reprezentując około 1/8 przestrzeni Address. Od 1999 roku IANA przydziela te bloki, takie jak prefiks `2001::/16`, w blokach CIDR (od `/23` do `/12`) do regionalnych rejestrów, które następnie redystrybuują je do dostawców i organizacji.


Niektóre zakresy mają specjalne udokumentowane zastosowania:


- `2001:2::/48`**: Zarezerwowany do testowania wydajności i interoperacyjności (RFC 5180).
- `2001:db8::/32`**: Zarezerwowane dla dokumentacji i przykładów (RFC 3849).
- `2002::/16`**: Używane dla mechanizmu 6to4, który pozwala na ruch IPv6 podróżować przez infrastrukturę IPv4 (przydatne podczas fazy przejściowej między dwoma protokołami).


**Uwaga:** duża część globalnych adresów pozostaje niewykorzystana, służąc jako rezerwa dla przyszłego rozwoju Internetu.


#### Unikalne adresy lokalne (ULA)


Unikalne adresy lokalne (`fc00::/7`) są odpowiednikiem IPv6 dla adresów prywatnych IPv4 (RFC1918). Umożliwiają one tworzenie odizolowanych sieci wewnętrznych bez ryzyka konfliktu z adresacją publiczną. W praktyce, efektywny prefiks to `fd00::/8`, z ósmym bitem ustawionym na 1, aby wskazać użycie lokalne. Każdy blok ULA zawiera 40-bitowy pseudolosowy identyfikator, minimalizujący kolizje Address podczas łączenia oddzielnych sieci prywatnych.


#### Adresy lokalne łącza


Adresy link-local (`fe80::/64`) są używane wyłącznie do komunikacji w obrębie tego samego segmentu Layer 2 (tej samej sieci VLAN lub przełącznika). Nigdy nie są kierowane poza łącze lokalne. Każdy sieciowy Interface automatycznie generuje link-local Address, często pochodzący z jego MAC Address przy użyciu schematu EUI-64.


**Specjalna funkcja**: to samo urządzenie może używać tego samego link-local Address na wielu interfejsach, ale Interface musi być określony podczas komunikacji, aby uniknąć dwuznaczności.


#### Adresy multiemisji


W IPv6, broadcast został zastąpiony przez multicast, bardziej efektywny sposób dostarczania pakietów do zdefiniowanej grupy odbiorców. Zakres multiemisji jest poprzedzony prefiksem `ff00::/8`. Obejmuje to adresy takie jak `ff02::1`, które są skierowane do wszystkich węzłów na łączu lokalnym. Choć wygodny, ten Address nie jest już zalecany dla aplikacji, ponieważ może generate niekontrolowane transmisje.


Powszechnym zastosowaniem multicastu jest _Neighbor Discovery Protocol_ (NDP), który zastępuje ARP w IPv6. NDP używa określonych adresów multicast, takich jak `ff02::1:ff00:0/104`, do automatycznego wykrywania innych hostów podłączonych do tego samego łącza.


Łącząc te typy Address, IPv6 zapewnia kompletny zestaw opcji spełniających potrzeby globalnego routingu, komunikacji lokalnej, migracji IPv4/IPv6 i automatycznej konfiguracji urządzeń, jednocześnie poprawiając wydajność transmisji.


### Zakres Address


Zakres protokołu IPv6 Address definiuje dokładną domenę, w której jest on ważny i unikalny. Zrozumienie tej koncepcji jest kluczem do opanowania routingu pakietów i logicznej organizacji sieci IPv6. Adresy IPv6 są ogólnie podzielone na trzy główne kategorie w oparciu o ich zakres i zastosowanie: unicast, anycast i multicast.


*adresy *Unicast** są najbardziej powszechne i obejmują kilka różnych podtypów.

Obejmują one _loopback_ (`::1`) Address, którego zakres jest ograniczony do hosta, który go używa i który jest używany do wewnętrznego testowania stosu sieciowego bez wysyłania ruchu przez sieć fizyczną.

Następnie istnieją adresy lokalne łącza (_link-local_), których zakres jest ograniczony do pojedynczego segmentu sieci: są one używane do bezpośredniej komunikacji między urządzeniami na tym samym łączu fizycznym lub logicznym (np. pojedynczy przełącznik lub VLAN).

Wreszcie, unikalne adresy lokalne (_ULA_, od _Unique Local Addresses_) są wewnętrzne dla sieci prywatnej. Mogą być kierowane między wieloma segmentami prywatnymi, ale nigdy nie są widoczne w Internecie.


Koncepcyjnie adresy IPv6 są często reprezentowane jako struktura binarna, w której pierwsza połowa (pierwsze 64 bity) identyfikuje prefiks sieci, a druga połowa (również 64 bity) jednoznacznie identyfikuje Interface urządzenia w tej sieci. Podział ten ułatwia autokonfigurację Address poprzez mechanizmy takie jak SLAAC (_Stateless Address Autoconfiguration_), które umożliwiają maszynom automatyczne generate stabilne Address w oparciu o MAC Address lub pseudolosowy identyfikator.


| Field     | Prefix | L | Global ID | Subnet | Interface ID |
|-----------|--------|---|-----------|--------|---------------|
| Bits      | 7      | 1 | 40        | 16     | 64            |

Architektura IPv6 jest zgodna z hierarchicznym globalnym modelem routingu dzisiejszego Internetu. Podział prefiksów umożliwia regionalnym rejestrom i operatorom sieci zarządzanie alokacją Address w sposób zdecentralizowany, przy jednoczesnym zapewnieniu globalnej unikalności. W tych ramach ten sam host może jednocześnie posiadać globalny unicast Address do komunikacji internetowej i link-local Address do lokalnych interakcji, np. z bezpośrednim sąsiedztwem lub dla komunikatów wykrywania routerów.


| Field     | Prefix | Zero | Interface ID |
|-----------|--------|------|--------------|
| Bits      | 10     | 54   | 64           |

**Adresy anycast** reprezentują koncepcję pośrednią, która opiera się na modelu unicast, ale w niektórych przypadkach może zachowywać się jak multicast. Anycast Address jest w istocie unicastem Address przypisanym do kilku interfejsów rozproszonych w różnych węzłach sieci. Gdy pakiet jest wysyłany do anycast Address, protokół IPv6 ma na celu dostarczenie go do jednego z hostów współdzielących ten Address, zazwyczaj najbliższego pod względem topologii routingu. Takie podejście optymalizuje szybkość przetwarzania zapytań i poprawia odporność usług rozproszonych. Klasycznym przykładem są główne serwery DNS, gdzie adresowanie anycast automatycznie kieruje zapytania do najbliższego punktu obecności.



| Field     | Prefix | Subnet | Interface ID |
|-----------|--------|--------|--------------|
| Bits      | 48     | 16     | 64           |

W IPv6, **adresy multicast** zastępują mechanizm rozgłoszeniowy, który został uznany za zbyt kosztowny i nieodpowiedni dla sieci o zasięgu globalnym. Multicast Address identyfikuje grupę interfejsów, zazwyczaj na wielu hostach, które chcą otrzymywać te same pakiety jednocześnie.

Każdy multicast Address zawiera specjalne 4-bitowe pole _scope_, które definiuje geograficzną lub logiczną granicę transmisji:


- Zakres `1` oznacza, że pakiet jest przeznaczony tylko dla lokalnego urządzenia.
- Zakres `2` ogranicza pakiet do lokalnego łącza: wszystkie urządzenia w tym samym segmencie fizycznym lub wirtualnym mogą go odebrać.
- Zakres `5` rozszerza zasięg na witrynę, zazwyczaj całą sieć korporacyjną.
- Zakres `8` rozszerza zasięg na organizację, umożliwiając dostarczanie we wszystkich podsieciach tego samego podmiotu.
- Zakres `e` (14 w systemie szesnastkowym) wskazuje na globalny zasięg, dzięki czemu grupa multicastowa jest dostępna z dowolnego miejsca w Internecie, jeśli infrastruktura routingu ją obsługuje.


Struktura multiemisji IPv6 Address obejmuje:


- pole _Flag_ (4 bity) określa, czy grupa jest stała czy tymczasowa,
- pole _Scope_ (4 bity) definiuje zakres,
- pole identyfikacyjne (112 bitów) identyfikujące numer grupy multicast.


| Field      | Prefix | Flags | Scope | Group ID |
|------------|--------|--------|--------|----------|
| Bits       | 8      | 4      | 4      | 112      |

Dobrze znanym przykładem IPv6 multicast w akcji jest _Neighbor Discovery Protocol_ (NDP). Zamiast używać ARP, jak w IPv4, NDP opiera się na adresach multicastowych, takich jak `ff02::1:ff00:0/104`, aby rozgłaszać żądania wykrywania sąsiadów, kierując je tylko do odpowiednich hostów na tym samym łączu.


Definiując tak precyzyjnie zakresy Address, IPv6 strukturyzuje sposób, w jaki przepływy danych są wysyłane, odbierane i kierowane. Ta szczegółowość sprawia, że protokół jest bardziej elastyczny i wydajny w zarządzaniu zarówno komunikacją lokalną, jak i globalną, unikając jednocześnie wad uogólnionego rozgłaszania.


## Address Assignment w sieci lokalnej


<chapterId>4c9c3e52-59bc-499a-af0a-6dd369a9e029</chapterId>


W tym rozdziale przyjrzymy się jednemu z najbardziej praktycznych aspektów wdrażania IPv6: przypisywaniu adresów IP do hostów w sieci lokalnej. Architektura IPv6 została zaprojektowana z myślą o elastyczności, umożliwiając każdemu urządzeniu automatyczne generate własne Address, jednocześnie umożliwiając w pełni ręczną konfigurację w razie potrzeby.


Sieć lokalna IPv6 systematycznie dzieli Address na dwie części:


- pierwsze 64 bity reprezentują prefiks podsieci, zwykle dostarczany przez router lub organ Address;
- pozostałe 64 bity są używane przez hosta do jednoznacznej identyfikacji w tym segmencie.

Model ten znacznie upraszcza agregację tras i zarządzanie blokami Address.


Do przypisywania adresów do urządzeń stosowane są dwa główne podejścia:


- Konfiguracja ręczna, w której administrator określa dokładny Interface dla każdego Address;
- Automatyczna konfiguracja, w której urządzenia generate lub dynamicznie uzyskują własne adresy.


W konfiguracji ręcznej administrator przypisuje kompletny adres IPv6 Address do każdego Interface. Niektóre wartości pozostają zarezerwowane:


- `::/128`: nieokreślony Address, nigdy nie przypisany na stałe ;
- `::1/128`: pętla zwrotna Address (_loopback_), odpowiednik IPv4: `127.0.0.1`.


W przeciwieństwie do IPv4, nie ma koncepcji _broadcast_; kombinacje "wszystkie zera" lub "wszystkie jedynki" w części hosta nie mają specjalnego znaczenia.

Ręczna konfiguracja jest nadal przydatna w kontrolowanych środowiskach, ale staje się trudna do utrzymania na dużą skalę.


Istnieje kilka metod automatycznej konfiguracji:


- Protokół **NDP** (_Neighbor Discovery Protocol_), określony przez RFC4862, umożliwia *bezstanową* autokonfigurację. W tym trybie host otrzymuje prefiks sieci od lokalnego routera i sam uzupełnia Address identyfikatorem opartym na jego MAC Address. Metoda ta jest prosta do wdrożenia i nie wymaga centralnego serwera.
- Implementacje takie jak te w systemie Windows mogą generate część hosta pseudolosowo, aby poprawić prywatność, unikając bezpośredniej ekspozycji MAC Address. Ujawnienie MAC Address w pakietach IPv6 może budzić obawy o prywatność, ponieważ umożliwia śledzenie urządzenia w różnych sieciach.
- Protokół DHCPv6: Zdefiniowany w RFC3315 i podobny do DHCP używanego dla IPv4, umożliwia bardziej kontrolowaną i scentralizowaną konfigurację, w tym zarządzanie dzierżawą, dodatkowe opcje (DNS, MTU...) i rejestrację baz danych. DHCPv6 może działać samodzielnie lub obok konfiguracji bezstanowej, aby zapewnić dodatkowe parametry bez przypisywania samego adresu IP Address.


**Ważna uwaga:** W metodzie opartej na MAC, MAC Address jest konwertowany na 64-bitowy identyfikator przy użyciu formatu EUI-64. Mechanizm ten wstawia bajty `FF:FE` w środku oryginalnego MAC Address (w 48 bitach) i odwraca siódmy bit, aby wskazać globalną unikalność. Rezultatem jest stabilny identyfikator Interface, używany w pełnym Address IPv6.


Oto przykład, jak przekształcić MAC Address w EUI-64:


![Image](assets/fr/045.webp)



Jednak ze względu na rosnące obawy dotyczące śledzenia urządzeń, nowoczesne systemy operacyjne (zwłaszcza Linux, Windows 10+, macOS, Android) domyślnie włączają rozszerzenia prywatności. Wykorzystują one losowo generowane identyfikatory Interface, które są okresowo odnawiane dla połączeń wychodzących, przy jednoczesnym zachowaniu stabilnego identyfikatora dla komunikacji wewnętrznej (takiej jak DNS lub DHCPv6).


Podobnie jak w przypadku DHCP w IPv4, automatycznie przypisane adresy IPv6 mogą mieć dwa okresy życia, zdefiniowane przez routery lub serwery DHCPv6:


- Preferowany czas życia*: po tym okresie Address pozostaje ważny, ale nie jest już używany do inicjowania nowych połączeń;
- Valid lifetime*: po upływie tego czasu Address jest całkowicie usuwany z konfiguracji Interface.


System ten umożliwia dynamiczne zarządzanie zmianami w sieci, na przykład zapewniając płynne przejście od jednego dostawcy usług internetowych do drugiego. Poprzez aktualizację prefiksu ogłaszanego przez routery i równoległe dostosowywanie rekordów DNS, migracja IPv6 może być przeprowadzona bez zauważalnych przerw w świadczeniu usług.


**Wskazówka:** Połączone wykorzystanie cykli życia Address i DNS umożliwia wdrożenie strategii stopniowego przejścia, w której nowe połączenia przechodzą do nowej topologii, podczas gdy istniejące połączenia są kontynuowane do ich naturalnego końca.


Krótko mówiąc, IPv6 oferuje szeroki zakres elastyczności dla Address Assignment: ręczna konfiguracja, bezstanowa lub stanowa autokonfiguracja, DHCPv6 lub losowe generowanie. Każde podejście ma swoje zalety i ograniczenia i może być dostosowane do wymaganego poziomu kontroli, wielkości sieci lub potrzeb związanych z prywatnością.


## Przypisywanie bloków IPv6 Address


<chapterId>45cce866-1b58-4888-b3fe-15c922180839</chapterId>


### Dystrybucja Address


Schemat alokacji Address IPv6 został skonstruowany tak, aby spełnić dwa cele: zagwarantować globalną unikalność Address i umożliwić logiczną hierarchię, która sprzyja agregacji i uproszczeniu tabel routingu.

Podobnie jak w przypadku IPv4, *Internet Assigned Numbers Authority* (IANA) znajduje się na szczycie tej hierarchii. Zarządza on globalną przestrzenią unicast Address i deleguje bloki Address do pięciu regionalnych rejestrów internetowych (_RIR_).


Pięć istniejących RIR to:


- ARIN (Ameryka Północna),
- RIPE NCC (Europa, Bliski Wschód, Azja Środkowa),
- APNIC (Azja i Pacyfik),
- AFRINIC (Afryka),
- LACNIC (Ameryka Łacińska i Karaiby).


IANA przydziela każdemu RIR bloki IPv6 o różnej wielkości, zazwyczaj od /23 do /12. Takie podejście zapewnia elastyczność przy jednoczesnym zapewnieniu długoterminowej skalowalności. Z kolei RIR redystrybuują te bloki do dostawców usług internetowych (ISP), dużych korporacji i instytucji publicznych.


Od 2006 r. każdy RIR otrzymał od IANA blok IPv6 /12, o stałym rozmiarze zaprojektowanym w celu zapewnienia stabilnej i wystarczająco dużej rezerwy na przyszły rozwój. RIR zazwyczaj dzielą je na bloki /23, /26 lub /29. Dostawcy usług internetowych najczęściej otrzymują bloki /32, chociaż rozmiar ten może się różnić w zależności od wielkości i obszaru geograficznego dostawcy usług internetowych. Zazwyczaj przydzielają oni klientom bloki /48. Każdy blok /48 zapewnia 65 536 odrębnych podsieci /64 (ogromna pojemność w porównaniu do IPv4).


**Ważna uwaga:** Blok /32 zawiera dokładnie 65 536 podbloków /48. Oznacza to, że każdy dostawca usług internetowych może obsługiwać dziesiątki tysięcy klientów bez wyczerpania przydziału. Dzięki blokowi /48, każdy klient będzie miał gigantyczną ilość miejsca na zbudowanie własnej sieci wewnętrznej z dowolną liczbą segmentów /64.


Typowa hierarchia alokacji wygląda następująco:


| IANA | RIR | LIR | Customer | Subnet | Interface |
|------|-----|-----|----------|--------|-----------|
|  3   | 20  |  9  |    16    |   16   |     64    |

Dzięki tej obfitości adresów, NAT (*Network Address Translation*), niegdyś niezbędny w IPv4, aby poradzić sobie z niedoborem Address, nie jest już potrzebny. Każdy host może mieć unikalny, globalnie routowalny publiczny Address, upraszczając łączność end-to-end i ułatwiając korzystanie z protokołów takich jak IPSec, VoIP lub połączenia przychodzące.


Aby sprawdzić, do której organizacji należy IPv6 Address, można użyć polecenia `whois` do zapytania publicznych baz danych RIR. Ta przejrzystość umożliwia identyfikację organizacji, która jest właścicielem prefiksu, co może być przydatne do celów sieciowych, analitycznych lub bezpieczeństwa.


### Adresowanie PA vs PI


Pierwotnie model alokacji IPv6 opierał się wyłącznie na blokach PA (*Provider Aggregatable*), co oznacza powiązanie z dostawcą usług internetowych. W tym modelu organizacja otrzymuje swój prefiks od dostawcy usług internetowych, co oznacza, że zmiana dostawcy wymaga zmiany numeracji całej infrastruktury.


Podczas gdy funkcje automatycznej konfiguracji IPv6 i żywotność Address ułatwiają zmianę numeracji, pozostaje to niewygodne dla organizacji z krytyczną infrastrukturą lub połączeniami wielu dostawców w celu spełnienia wymagań redundancji.


Od 2009 roku zasady alokacji pozwalają na bloki PI (*Provider Independent*). Bloki te (zazwyczaj o rozmiarze /48) są przydzielane bezpośrednio firmie lub instytucji przez RIR, niezależnie od jakiegokolwiek dostawcy usług internetowych. Model ten jest szczególnie odpowiedni dla organizacji praktykujących *multihoming* (co oznacza jednoczesne połączenie z kilkoma operatorami). Na przykład, w Europie, RIPE-512 określa politykę alokacji PI.


### Notacja maski podsieci


Podobnie jak w IPv4, IPv6 wykorzystuje CIDR (*Classless Inter-Domain Routing*). Polega to na wskazaniu liczby bitów tworzących prefiks po Address, przy użyciu znaku `/`.


Weźmy następujący przykład:


```
2001:db8:1:1a0::/59
```


Oznacza to, że pierwsze 59 bitów jest stałych i identyfikuje sieć. Wszystkie pozostałe bity (tutaj 69 bitów) mogą być użyte do identyfikacji podsieci lub hostów.


W ten sposób notacja ta obejmuje adresy od `2001:db8:1:1a0:0:0:0` do `2001:db8:1:1bf:ffff:ffff:ffff:ffff`.


Blok ten obejmuje zatem zestaw 8 podsieci /64, z których każda może obsługiwać ogromną liczbę urządzeń.


Notacja CIDR umożliwia precyzyjne planowanie przestrzeni Address, od dużych sieci po konfiguracje domowe i środowiska zwirtualizowane, a także zachęca do agregacji tras, zmniejszając obciążenie routerów i poprawiając skalowalność.


### Pakiety i nagłówki IPv6


Format pakietów IPv6 różni się od IPv4 tym, że jest zarówno prostszy, jak i bardziej rozszerzalny. Datagram IPv6 zawsze zaczyna się od nagłówka o stałym rozmiarze 40 bajtów, zawierającego wszystkie istotne informacje o routingu. To uproszczone podejście, w porównaniu do zmiennej długości nagłówka IPv4 (od 20 do 60 bajtów), umożliwia szybsze i bardziej wydajne przetwarzanie pakietów przez routery.


IPv6 nie usuwa jednak funkcjonalności: zamiast integrować liczne opcjonalne pola w głównym nagłówku, wprowadza system nagłówków rozszerzeń, umieszczanych bezpośrednio po nagłówku podstawowym. Te opcjonalne nagłówki umożliwiają dodawanie danych lub instrukcji specyficznych dla określonych funkcji, bez niepotrzebnego obciążania zwykłych pakietów.


Niektóre nagłówki rozszerzeń mają stałą strukturę, podczas gdy inne mogą zawierać zmienną liczbę opcji. W Te opcje są kodowane jako triplety `{Type, Length, Value}`:


- Pole "Type" (1 bajt) wskazuje charakter opcji;
- Pierwsze dwa bity "Type" określają, co routery powinny zrobić, jeśli opcja nie zostanie rozpoznana:
 - Zignoruj tę opcję i kontynuuj leczenie,
 - Usunięcie datagramu,
 - Odrzuć i wyślij błąd ICMP do źródła.
 - Odrzucenie datagramu bez powiadomienia (w przypadku pakietów multicast).
- Pole "Length" (1 bajt) określa rozmiar pola "Value", od 0 do 255 bajtów;
- Pole "Wartość" zawiera dane powiązane z opcją.


Oto przegląd różnych typów nagłówków rozszerzeń zdefiniowanych przez IPv6.


#### Nagłówek Hop-by-Hop


Nagłówek ten, jeśli występuje, jest zawsze umieszczany bezpośrednio po nagłówku podstawowym. Zawiera on informacje, które muszą być przetwarzane przez każdy router na ścieżce pakietu, w przeciwieństwie do większości innych nagłówków, które są zwykle obsługiwane tylko przez węzeł docelowy. Typowe zastosowania obejmują sygnalizowanie parametrów globalnych lub żądanie określonych kroków przetwarzania, gdy pakiet przemieszcza się przez sieć.


![Image](assets/fr/047.webp)


#### Nagłówek routingu


Nagłówek routingu określa listę adresów pośrednich, przez które musi przejść pakiet. Istnieją dwa główne tryby routingu:


- Ścisły routing: dokładna ścieżka jest predefiniowana
- Luźny routing: określone są tylko niektóre obowiązkowe kroki.


Pierwsze cztery pola tego nagłówka rootowania to:


- Next Header**: określa typ następnego nagłówka;
- Typ routingu**: definiuje metodę routingu (zazwyczaj `0`);
- Segmenty pozostałe**: liczba segmentów pozostałych do przejścia;
- Address[n]**: lista adresów pośrednich.


Pole "Segments Left" zaczyna się od całkowitej liczby pozostałych segmentów i jest zmniejszane o jeden przy każdym przeskoku.


![Image](assets/fr/048.webp)


#### Nagłówek fragmentacji


W IPv6 tylko host źródłowy może fragmentować datagramy, w przeciwieństwie do IPv4, gdzie routery również mogły to robić. Wszystkie węzły IPv6 muszą być w stanie obsłużyć pakiety o wielkości co najmniej 1280 bajtów. Jeśli router napotka pakiet większy niż MTU następnego łącza, wysyła komunikat *ICMPv6 Packet Too Big* z powrotem do źródła, które następnie dostosowuje rozmiar swoich transmisji.


Nagłówek fragmentacji zawiera następujące pola:


- Identification**: unikalny identyfikator datagramu do ponownego złożenia.
- Fragment Offset**: pozycja fragmentu w oryginalnym datagramie.
- Flaga M**: wskazuje, czy ma nastąpić więcej fragmentów.


![Image](assets/fr/049.webp)


#### Nagłówek uwierzytelniania (AH)


Nagłówek ten został zaprojektowany w celu zabezpieczenia komunikacji poprzez weryfikację zarówno autentyczności nadawcy, jak i integralności danych. Jest on powszechnie używany z protokołem IPsec. Korzystając z kodu uwierzytelniającego, odbiorca może potwierdzić, że wiadomość rzeczywiście pochodzi od oczekiwanego nadawcy i że nie została zmieniona podczas przesyłania.


W przypadku nieuczciwej próby modyfikacji, kod uwierzytelniający nie będzie już pasował, a datagram może zostać odrzucony. Mechanizm ten chroni również przed atakami typu replay, wykrywając nieautoryzowane duplikaty.


![Image](assets/fr/050.webp)


#### Nagłówek opcji miejsca docelowego


Nagłówek ten jest przeznaczony wyłącznie dla końcowego odbiorcy datagramu. Może być używany do dodawania opcji lub metadanych specyficznych dla aplikacji, bez uwzględniania ich przez routery pośrednie.


Początkowo taka opcja nie była zdefiniowana w protokole. Nagłówek ten został jednak wprowadzony podczas projektowania protokołu IPv6, aby umożliwić dodawanie przyszłych rozszerzeń bez modyfikowania ogólnej struktury pakietu. Opcja null, na przykład, jest używana tylko do wypełnienia nagłówka wielokrotnością 8 bajtów w celu wyrównania pamięci.


![Image](assets/fr/051.webp)


Konstrukcja pakietów IPv6 opiera się na wyraźnym oddzieleniu minimalnego nagłówka podstawowego od modułowych nagłówków rozszerzeń. Architektura ta zapewnia zarówno standardową wydajność przetwarzania, jak i elastyczność potrzebną do ewolucji protokołu i integracji bezpieczeństwa, złożonego routingu lub mechanizmów jakości usług, przy jednoczesnym zachowaniu kompatybilności z przyszłymi infrastrukturami.


## Związek między IPv6 a DNS


<chapterId>421eacb8-b80b-4aee-910f-e069ed805f00</chapterId>


W nowoczesnych sieciach DNS (*Domain Name System*) tłumaczy nazwy domen na adresy IP, z których mogą korzystać maszyny. Wraz z wprowadzeniem IPv6, DNS musiał dostosować się do obsługi 128-bitowych adresów, zachowując jednocześnie wsteczną kompatybilność z IPv4. Ta koegzystencja jest szczególnie ważna w środowiskach dual-stack, gdzie obie wersje IP działają jednocześnie.


### Rekordy DNS specyficzne dla protokołu IPv6


Aby powiązać nazwę domeny z Address IPv6, DNS używa rekordu AAAA (*quad-A*), analogicznego do rekordu "A" dla adresów IPv4. Rekord AAAA jawnie mapuje nazwę domeny na IPv6 Address.

Przykład:


```shell
ipv6.mydmn.org.         IN      AAAA    2001:66c:2a8:22::c100:68b
```


Rekord ten wskazuje, że domena `ipv6.mydmn.org` rozpoznaje adres IPv6 Address `2001:66c:2a8:22::c100:68b`. Możliwe jest, a nawet zalecane dla maksymalnej kompatybilności, powiązanie tej samej nazwy domeny z kilkoma adresami IP, zarówno IPv4 (poprzez rekord A), jak i IPv6 (poprzez rekord AAAA). Pozwala to klientom kompatybilnym z IPv6 preferować IPv6, zapewniając jednocześnie, że klienci obsługujący tylko IPv4 pozostaną obsługiwani.


Ponadto DNS obsługuje odwrotne rozpoznawanie, co oznacza, że może wyszukać nazwę domeny powiązaną z danym adresem IP Address. W przypadku IPv6, operacja ta wykorzystuje rekordy PTR umieszczone w strefie `ip6.arpa`. Strefa ta jest specjalnie zarezerwowana dla odwrotnego rozpoznawania IPv6. Dla IPv4 jest to strefa `in-addr.arpa`.


### Odwrócona rozdzielczość


Odwrotne rozwiązywanie IPv6 Address odbywa się według ściśle określonego procesu:

1) Rozwiń Address do pełnego zapisu szesnastkowego (16 bajtów, tj. 32 cyfry szesnastkowe).

Przykład:


```shell
2001:66c:2a8:22::c100:68b
```


Staje się:


```shell
2001:066c:02a8:0022:0000:0000:c100:068b
```


2) Odwróć kolejność każdej cyfry szesnastkowej (nibble), oddziel je kropkami i dołącz `ip6.arpa`:


```shell
b.8.6.0.0.0.1.c.0.0.0.0.0.0.0.0.2.2.0.0.8.a.2.0.c.6.6.0.1.0.0.2.ip6.arpa  IN PTR  ipv6.mydmn.org
```


Struktura ta zapewnia znormalizowane, unikalne wyszukiwanie wsteczne w przestrzeni IPv6 Address.


**Uwaga**: Zapytania DNS mogą być przesyłane przez protokół IPv4 lub IPv6. Używany protokół transportowy nie ma wpływu na typ zwracanych rekordów.

Na przykład:


- Klient połączony przez IPv6 może zażądać rekordu IPv4.
- Klient połączony przez IPv4 może zażądać rekordu IPv6.

Serwer DNS po prostu odpowiada posiadanymi rekordami, niezależnie od protokołu transportowego zapytania.


Gdy nazwa hosta jest mapowana zarówno na IPv4, jak i IPv6, wybór Address do użycia jest regulowany przez RFC 6724, który definiuje algorytm wyboru Address oparty na czynnikach takich jak preferencja prefiksu, zakres i zasięg. Domyślnie preferowany jest protokół IPv6, chyba że zostanie on zastąpiony przez konfigurację systemu lub sieci.


**Ważne przypomnienie**: podczas osadzania IPv6 Address w adresie URL (*Uniform Resource Locator*), musi on być ujęty w nawiasy kwadratowe (`[]`). Pozwala to uniknąć pomyłki między dwukropkiem (`:`) wewnątrz IPv6 Address a dwukropkiem oddzielającym nazwę hosta od portu w adresie URL.


Prawidłowy przykład:


```shell
http://[2001:db8::1]:8080
```


Zapewnia to prawidłowe przetwarzanie adresu URL zarówno przez przeglądarki, jak i serwery internetowe.


Integracja IPv6 z systemem DNS opiera się zatem na nowych typach rekordów, ścisłej metodzie odwrotnego rozwiązywania oraz precyzyjnych regułach wyboru i formatowania w celu zapewnienia kompatybilności i spójności routingu.


### Podsumowanie części


W tej sekcji zbadaliśmy podstawowe zasady adresowania IPv6. Zaczęliśmy od zbadania struktury Address IPv6: jego 128-bitowej długości, zapisu szesnastkowego i zasad upraszczania używanych do skracania powtarzających się sekwencji zer. Taka konstrukcja umożliwia IPv6 przezwyciężenie ograniczeń przestrzeni Address IPv4, gwarantując jednocześnie skalowalność i wydajną hierarchię.


Następnie przyjrzeliśmy się różnym kategoriom adresów IPv6: unicast, anycast i multicast, szczegółowo opisując ich zakres, typowe zastosowanie i reprezentację w przestrzeni Address.


Następnie dokonaliśmy przeglądu metod przypisywania adresów IPv6 w sieci lokalnej, czy to poprzez ręczną konfigurację, za pośrednictwem protokołu DHCPv6, czy też przy użyciu bezstanowych mechanizmów autokonfiguracji, takich jak te oferowane przez NDP. Podejścia te umożliwiają urządzeniom automatyczne generate własnych Address z dostarczonego prefiksu i ich MAC Address (poprzez EUI-64), oferując jednocześnie elastyczność w zakresie zarządzania czasem życia i prywatności.


Opisaliśmy również szczegółowo, w jaki sposób przydzielane są bloki Address, począwszy od IANA, która dystrybuuje je do pięciu RIR (*Registered Internet Regions*), a następnie do dostawców usług internetowych, którzy redystrybuują je do swoich klientów jako podsieci (często w /48, umożliwiając 65536 podsieci /64). Rozróżnienie między blokami _Provider Aggregatable_ (PA) i _Provider Independent_ (PI) pomaga zarządzać scenariuszami _multihoming_ lub zmiany dostawcy.


Widzieliśmy, że DNS dostosował się do IPv6 wraz z wprowadzeniem rekordu AAAA, a mechanizmy odwrotnego rozwiązywania polegają teraz na strefie `ip6.arpa`. Co ważne, DNS pozostaje niezależny od używanego protokołu transportowego (IPv4 lub IPv6), zapewniając płynną interoperacyjność w środowisku dual-stack.


IPv6 nie jest zatem tylko stopniowym ulepszeniem w stosunku do IPv4, ale całkowitym przeprojektowaniem systemu adresowania, zbudowanym tak, aby sprostać zarówno obecnym, jak i przyszłym wyzwaniom globalnego Internetu.


W ostatniej części tego kursu NET 302 przejdziemy do praktyki i skupimy się na narzędziach diagnostycznych sieci.



# Sieciowe narzędzia diagnostyczne


<partId>368a5c6f-ec48-4b28-970f-3a770788ad37</partId>


## Narzędzia dostępu do sieci Layer


<chapterId>1d25a21d-6900-4fbe-a438-e06c8afb9e02</chapterId>


W tym pierwszym rozdziale ostatniej części poświęconej diagnostyce sieci skupiamy się na narzędziach do analizy dostępu do sieci Layer modelu TCP/IP. Ten Layer jest odpowiedzialny za bezpośrednią komunikację między urządzeniami w tej samej sieci fizycznej, w szczególności poprzez wykorzystanie adresów MAC i fizycznych interfejsów sieciowych, takich jak karty Ethernet lub interfejsy Wi-Fi.


Celem jest dostarczenie administratorom praktycznych narzędzi do sprawdzania, testowania i optymalizacji tego istotnego Layer połączenia niskiego poziomu. Narzędzia te mogą być wykorzystywane do weryfikacji prawidłowego działania interfejsów, rozwiązywania problemów z konfiguracją kart sieciowych lub wykrywania anomalii, takich jak kolizje, utrata pakietów lub błędy łącza.


### Narzędzia sąsiedztwa IP/MAC


#### narzędzie `Arp


Jednym z najstarszych narzędzi diagnostycznych w Network Access Layer jest polecenie `arp`. Chociaż coraz częściej zastępowane przez nowoczesne alternatywy, takie jak `ip neigh` (które wkrótce odkryjemy). `Arp` jest nadal obecne w wielu systemach, aby przeglądać lub manipulować pamięcią podręczną ARP (*Address Resolution Protocol*). Ta pamięć podręczna przechowuje mapowania między adresami IP i adresami MAC znanymi lokalnie na komputerze. Innymi słowy, pozwala określić, który fizyczny (MAC) Address odpowiada danemu IP Address w sieci lokalnej.


W praktyce, gdy host chce wysłać pakiet do IP Address w tej samej podsieci, musi najpierw znać MAC Address maszyny docelowej. Mapowanie to jest obsługiwane przez ARP, który rozgłasza żądanie w sieci lokalnej i otrzymuje odpowiedź zawierającą odpowiedni MAC Address. Wynik ten jest następnie tymczasowo przechowywany w lokalnej tabeli zwanej "pamięcią podręczną ARP", aby uniknąć powtarzania żądań dla każdego nowego pakietu.


Aby wyświetlić zawartość tej pamięci podręcznej i sprawdzić wpisy aktualnie znane urządzeniu, użyj:


```bash
arp -a
```


To polecenie wyświetla listę wszystkich lokalnie zarejestrowanych mapowań IP/MAC na wszystkich interfejsach. Każdy wiersz zawiera nazwę hosta (jeśli można ją rozpoznać), IP Address, odpowiadający MAC Address i Interface, w którym obserwowane jest mapowanie.


Aby przefiltrować wyświetlanie do określonego adresu IP Address, wystarczy go określić:


```bash
arp -a 192.168.1.5
```


Ułatwia to sprawdzenie, czy określony adres IP Address jest obecny w pamięci podręcznej, co może pomóc w diagnozowaniu awarii komunikacji między dwoma hostami w tej samej sieci.


Podobnie, aby wyświetlić tylko wpisy ARP powiązane z określoną siecią Interface (na przykład kartą Ethernet o nazwie `eth0`), można użyć:


```bash
arp -a -i eth0
```


Jest to szczególnie przydatne w środowiskach multi-Interface (przewodowych, bezprzewodowych, VPN itp.), gdzie jeden host może mieć kilka kart sieciowych.


Polecenie `arp` nie jest ograniczone tylko do odczytu. Można go również użyć do ręcznej edycji pamięci podręcznej ARP, co jest nieocenioną funkcją w niektórych zaawansowanych scenariuszach rozwiązywania problemów lub podczas symulacji określonych warunków. Na przykład, można ręcznie dodać mapowanie IP/MAC:


```bash
arp -s 192.168.1.7 00:17:BC:56:4F:25 -i eth2
```


To polecenie tworzy statyczny wpis w lokalnej tablicy ARP, kojarząc IP Address `192.168.1.7` z MAC Address `00:17:BC:56:4F:25` na Interface `eth2`.Jeśli nie zostanie określony Interface, system automatycznie użyje pierwszego odpowiedniego.


Można również usunąć wpis z pamięci podręcznej ARP, aby poprawić błąd lub wymusić ponowne wykrycie:


```bash
arp -d 192.168.1.7
```


Powoduje to usunięcie wpisu, zapewniając, że następna próba komunikacji wywoła nowe żądanie ARP.


**UWAGA**: Opcja usuwania akceptuje również nazwę Interface, umożliwiając bardziej precyzyjne ukierunkowanie usuwania określonego wpisu.


Podsumowując, narzędzie `arp` zapewnia niskopoziomową diagnostykę, szczególnie przydatną w sieciach lokalnych, gdzie problemy z łącznością często mogą być powiązane z nieprawidłową lub przestarzałą rozdzielczością Address. Jednak w najnowszych systemach, szczególnie w nowoczesnych dystrybucjach Linuksa, narzędzie to jest coraz częściej zastępowane przez polecenie `ip neigh` z zestawu narzędzi `iproute2`, które oferuje podobną funkcjonalność w bardziej zunifikowanych ramach.


#### narzędzie `Ip neigh`


W nowoczesnych systemach, zwłaszcza w najnowszych dystrybucjach Linuksa, polecenie `ip neigh` jest narzędziem do sprawdzania i zarządzania mapowaniami między adresami IP i MAC. Polecenie to jest częścią pakietu `iproute2`, który stopniowo zastępuje starsze narzędzia, takie jak `arp`, zapewniając bardziej spójne i elastyczne ramy dla diagnostyki łącza danych Layer.


Komenda `ip neigh` odpytuje lokalną pamięć podręczną sąsiadów IP, która jest odpowiednikiem pamięci podręcznej ARP dla IPv4 i pamięci podręcznej NDP (_Neighbor Discovery Protocol_) dla IPv6. Ta pamięć podręczna przechowuje znane powiązania między adresami IP (v4 lub v6) i adresami MAC, wraz z ich statusem (ważne, oczekujące, wygasłe...).


Podstawowym poleceniem do wyświetlenia pamięci podręcznej jest:


```bash
ip neigh
```


Spowoduje to wyświetlenie listy wpisów, pokazującej docelowy adres IP Address, odpowiednią sieć Interface, powiązany adres MAC Address (jeśli jest dostępny) oraz stan wpisu (np. `REACHABLE`, `STALE`, `DELAY`, `FAILED`...).


Przykładowe dane wyjściowe:


```bash
192.168.1.5 dev eth0 lladdr 00:17:BC:56:4F:25 REACHABLE
```


Ten wiersz wskazuje, że urządzenie zna prawidłowe mapowanie pomiędzy IP Address `192.168.1.5` i MAC Address `00:17:BC:56:4F:25` poprzez Interface `eth0`.


Można również filtrować wpisy według kryteriów takich jak IP Address, Interface lub stan. Na przykład, aby zapytać tylko Address `192.168.1.7`:


```bash
ip neigh show 192.168.1.7
```


Lub aby wyświetlić wszystkie wpisy dla Interface `eth1`:


```bash
ip neigh show dev eth1
```


Poza konsultacjami, `ip neigh` może być również użyty do ręcznej edycji pamięci podręcznej. Na przykład, aby dodać statyczny wpis:


```bash
ip neigh add 192.168.1.7 lladdr 00:17:BC:56:4F:25 dev eth1 nud permanent
```


Powoduje to trwałe powiązanie IP Address `192.168.1.7` z określonym MAC Address na Interface `eth1`. Opcja `nud permanent` (dla _Neighbor Unreachability Detection_) zapewnia, że wpis nie zostanie automatycznie unieważniony.


I odwrotnie, aby usunąć wpis z pamięci podręcznej:


```bash
ip neigh del 192.168.1.7 dev eth1
```


Zmusza to system do ponownego rozwiązania mapowania przy następnej komunikacji z Address.


**UWAGA**: Narzędzie `ip neigh` działa zarówno dla IPv4 jak i IPv6. Dla IPv4, łączy się z ARP; dla IPv6, współdziała z NDP. Zapewnia to ujednolicone, spójne podejście do zarządzania relacjami IP/MAC w różnych rodzinach protokołów, czyniąc `ip neigh` nowoczesnym standardem zarządzania sąsiadami w systemach Linux.


### Narzędzia do analizy pakietów


Aby dokładnie przeanalizować to, co dzieje się w sieci komputerowej, administratorzy potrzebują narzędzi, które mogą przechwytywać pakiety wymieniane między maszynami. Dwa narzędzia wyróżniają się jako wzorce: `tcpdump` i `Wireshark`. Narzędzia te są niezbędne do diagnozowania nieprawidłowego zachowania, audytu wymiany protokołów lub badania bezpieczeństwa sieci poprzez inspekcję zawartości ramek.


#### `ttcpdump`: analiza wiersza poleceń


`tcpdump` jest bardzo potężnym narzędziem wiersza poleceń zaprojektowanym do przechwytywania i wyświetlania pakietów podróżujących przez sieć Interface. Działa w czasie rzeczywistym, a dzięki lekkiej konstrukcji może być używany w systemach bez graficznego Interface lub z ograniczonymi zasobami. Opiera się na bibliotece `libpcap`, która zapewnia niezależne od sprzętu funkcje przechwytywania niskiego poziomu.


Powszechnym zastosowaniem `tcpdump` jest monitorowanie aktywności sieciowej maszyny lub segmentu sieci, filtrując pakiety według określonych kryteriów. Wyniki mogą być przekierowane do pliku, umożliwiając archiwizację ruchu w celu późniejszej analizy lub odtworzenia w innym narzędziu, takim jak Wireshark.


Ogólna składnia polecenia to:


```bash
tcpdump -w <file.cap> -i <interface> -s <snapshot_length> -n <filters>
```



- `-w` zapisuje przechwycone pakiety do pliku w formacie `libpcap` (rozszerzenie `.cap` lub `.pcap`);
- `-i` określa sieć Interface do monitorowania (np. `eth0`, `wlan0`);
- `-s` ustawia maksymalną ilość danych przechwytywanych na pakiet. Określenie `0` przechwytuje wszystkie pakiety;
- `-n` wyłącza DNS i rozpoznawanie nazw usług, poprawiając wydajność.


Filtry wyrażeń na końcu polecenia pozwalają ograniczyć przechwytywanie do podzbioru ruchu. Można łączyć słowa kluczowe `host`, `port`, `src`, `dst` itp. w celu zawężenia wyboru.


Przykład: przechwytywanie pakietów HTTP (port 80) do lub z serwera `192.168.25.24` i zapisywanie ich w pliku `fichier.cap`:


```bash
tcpdump -w fichier.cap -i eth0 -s 0 -n port 80 and host 192.168.25.24
```


Wynikowy plik można później przeanalizować w narzędziu graficznym lub odtworzyć w innym systemie.


#### Wireshark: zaawansowana analiza wizualna


Wireshark, wcześniej znany jako *Ethereal*, to kompletny program do analizy sieci z graficznym Interface. W przeciwieństwie do `tcpdump`, zapewnia uporządkowaną, szczegółową wizualizację pakietów, w tym analizę protokołów, wykresy przepływu, statystyki ruchu i interaktywne filtry. Opiera się również na `libpcap`, co oznacza, że może otwierać i przetwarzać pliki przechwytywania wygenerowane przez `tcpdump`.


Wireshark jest dostępny w wielu systemach operacyjnych, w tym Linux i Windows. Instalacja wymaga uprawnień administratora, aby uzyskać dostęp do interfejsów przechwytywania. Po uruchomieniu można wybrać sieć Interface z menu *Capture*. Kliknięcie przycisku *Start* rozpoczyna rejestrowanie pakietów w czasie rzeczywistym. Wyświetlacz jest podzielony na trzy panele:


- lista przechwyconych klatek ;
- szczegóły dekodowane protokołem,
- surowe dane szesnastkowe.



![Image](assets/fr/052.webp)



Wireshark doskonale sprawdza się w scenariuszach, w których trzeba obserwować złożone zachowanie protokołów, rekonstruować okna dialogowe aplikacji (takie jak sesja HTTP lub DNS) lub badać czasy odpowiedzi usług. Obsługuje również wysoce specyficzne filtry wyświetlania przy użyciu dedykowanej składni (innej niż w `tcpdump`), aby skupić się tylko na odpowiednich pakietach.


#### Narzędzia uzupełniające


Należy zauważyć, że `tcpdump` i Wireshark nie są wymienne: każdy z nich ma swoje mocne strony. `tcpdump` lepiej nadaje się do środowisk wiersza poleceń, zautomatyzowanych skryptów i zdalnych interwencji na serwerze, podczas gdy Wireshark jest idealny do szczegółowej, interaktywnej i edukacyjnej analizy ruchu.


Oba narzędzia można połączyć: przechwytywanie może być wykonane na zdalnym systemie za pomocą `tcpdump`, a następnie plik `.cap` jest przesyłany do analizy za pomocą Wireshark na lokalnej maszynie. Takie podejście jest szeroko stosowane w praktyce.


### Narzędzia do analizy Interface


W Network Access Layer często konieczne jest odpytywanie i konfigurowanie fizycznych interfejsów sieciowych w celu zdiagnozowania usterek, optymalizacji wydajności lub weryfikacji integralności połączenia. Jednym z najpotężniejszych narzędzi dostępnych w systemie Linux do tego celu jest `ethtool`, narzędzie wiersza poleceń, które nie tylko dostarcza szczegółowych informacji technicznych o sieci Ethernet Interface, ale także pozwala na dostosowanie niektórych jej parametrów w czasie rzeczywistym.


#### Zobacz specyfikację Interface


Podstawową cechą `ethtool` jest jego zdolność do odpytywania Interface i wyświetlania jego aktualnej charakterystyki. Pozwala to na sprawdzenie:


- prędkość łącza (np. 100 Mbit/s, 1 Gbit/s lub 10 Gbit/s);
- tryb negocjacji (półdupleks lub pełny dupleks) ;
- czy autonegocjacja jest włączona;
- typ portu (miedziany, światłowodowy itp.);
- stan łącza (aktywne lub nie) ;
- obsługa zaawansowanych funkcji, takich jak *Wake-on-LAN*.


Informacje te są szczególnie przydatne do diagnozowania problemów związanych z fizyczną łącznością lub niedopasowanymi ustawieniami negocjacji między kartą sieciową hosta a sprzętem, z którym się łączy (przełącznik, router itp.).


Aby uzyskać te informacje, wystarczy uruchomić aplikację:


```bash
ethtool enp0s3
```


To polecenie wyświetla szczegółowy raport na temat `enp0s3` Interface, wspólnej konwencji nazewnictwa w systemach CentOS lub RHEL.



![Image](assets/fr/053.webp)



#### Dynamicznie modyfikuj parametry Interface


narzędzie `ethtool` nie ogranicza się do obserwacji: pozwala również na dostosowanie niektórych parametrów Interface bez konieczności ponownego uruchamiania urządzenia. Umożliwia to, na przykład, wymuszenie określonej prędkości łącza lub włączenie funkcji zgodnie z potrzebami sieci lokalnej.


Opcja `-s` jest używana do dynamicznego konfigurowania parametrów takich jak:


- prędkość łącza (`speed`), ustawiana jawnie (np. 1000 dla 1 Gbit/s);
- tryb dupleksu (`duplex`), albo `pół` albo `pełny`;
- włączanie lub wyłączanie autonegocjacji (`autoneg`) ;
- włączenie *Wake-on-LAN* (`wol`) ;
- typ portu.


Przykład 1: włączenie autonegocjacji na Interface:


```bash
ethtool -s enp0s3 autoneg on
```


Przykład 2: włączenie funkcji *Wake-on-LAN* (aby umożliwić zdalne wybudzenie urządzenia za pomocą magicznego pakietu):


```bash
ethtool -s enp0s3 wol p
```


W tym przykładzie opcja `p` określa, że wybudzenie nastąpi natychmiast po wykryciu pakietu *Wake-on-LAN*. Ta konfiguracja jest często używana w środowiskach korporacyjnych do wykonywania nocnych aktualizacji lub zdalnej konserwacji.


#### Instalacja narzędzia


Należy zauważyć, że `ethtool` nie zawsze jest instalowany domyślnie. W dystrybucjach Red Hat/CentOS można go zainstalować za pomocą polecenia:


```bash
yum install -y ethtool
```


W Debianie i Ubuntu odpowiednikiem tego polecenia jest:


```bash
sudo apt install ethtool
```


**UWAGA: we wszystkich poleceniach `ethtool` nazwa sieci Interface musi być podana bezpośrednio po opcji (jako `-s`). Jakikolwiek błąd składni w umieszczeniu parametrów spowoduje, że polecenie będzie nieważne lub nieskuteczne.



## Narzędzia sieciowe Layer


<chapterId>d2c5bf35-4284-4af8-8e8b-049c696a511b</chapterId>


### Narzędzia do analizy ruchu


W diagnostyce sieci polecenie `ping` pozostaje jednym z najprostszych, ale najpotężniejszych narzędzi do testowania łączności między dwiema maszynami. Sprawdza, czy zdalny host jest osiągalny w danym czasie, dostarczając jednocześnie informacji na temat opóźnień, stabilności łącza i rozdzielczości DNS.


Polecenie `ping` opiera się na protokole ICMP (*Internet Control Message Protocol*). Gdy użytkownik wysyła żądanie `ping`, system wysyła pakiet ICMP "Echo Request" na adres IP Address lub nazwę hosta. Jeśli maszyna docelowa jest online, a ścieżka sieciowa jest prawidłowa, odpowiada pakietem ICMP "Echo Reply". Ten prosty mechanizm może być wykorzystywany do pomiaru opóźnień i wykrywania problemów z łącznością lub rozpoznawaniem nazw.


Przykład klasycznego polecenia:


```bash
ping 172.17.18.19
```


Typowa odpowiedź:


```bash
mydmn.org (172.17.18.19): 56 data bytes
64 bytes from 172.17.18.19: icmp_seq=0 ttl=56 time=7.7 ms
64 bytes from 172.17.18.19: icmp_seq=1 ttl=56 time=6.0 ms
64 bytes from 172.17.18.19: icmp_seq=2 ttl=56 time=5.5 ms
```


W tym przykładzie rozpoznawanie nazw zostało wykonane automatycznie: domena `mydmn.org` jest powiązana z IP Address `172.17.18.19`, potwierdzając, że rozpoznawanie DNS działa poprawnie. Polecenie dostarcza również szczegółów technicznych, takich jak:


- numer sekwencji iCMP (`icmp_seq`), przydatny do sprawdzania kolejności odpowiedzi;
- TTL (*Time-To-Live*), który wskazuje liczbę pozostałych przeskoków, zanim pakiet zostanie odrzucony;
- czas/opóźnienie w obie strony (`time`), wyrażony w milisekundach, zapewniający oszacowanie opóźnienia łącza.


#### Bardziej szczegółowa analiza parametrów ICMP


TTL jest krytycznym polem w protokole IP. Każdy datagram jest inicjowany wartością TTL przez nadawcę (często 64, 128 lub 255). Każdy router wzdłuż ścieżki zmniejsza tę wartość o 1. Jeśli TTL osiągnie 0 przed dotarciem do miejsca docelowego, pakiet jest odrzucany, a do nadawcy zwracany jest błąd ICMP. Mechanizm ten zapobiega powstawaniu nieskończonych pętli routingu.


Czas propagacji (*round-trip delay/time*) mierzy opóźnienie, z jakim pakiet opuszcza nadawcę, dociera do celu i powraca. W praktyce opóźnienie poniżej 200 ms jest uważane za akceptowalne dla stabilnego łącza. Nienormalnie wysokie opóźnienia mogą wskazywać na przeciążenie sieci, nieefektywny routing lub niską jakość łącza.


#### Zaawansowane użycie `ping`


`ping` zapewnia opcje pozwalające udoskonalić testy i obserwować określone zachowania sieci.


Aby wysyłać żądania rozgłoszeniowe, można użyć opcji `-b`, aby skierować je do wszystkich hostów w podsieci:

```bash
ping -b 192.168.1.255
```


Jest to przydatne w sieciach lokalnych do szybkiego wykrywania aktywnych hostów lub testowania sposobu, w jaki sieć obsługuje żądania rozgłoszeniowe. Jednak w wielu konfiguracjach routery i zapory sieciowe blokują pingi rozgłoszeniowe, aby zapobiec atakom wzmacniającym.


Można również określić niestandardowy interwał między żądaniami za pomocą opcji `-i` (domyślnie: 1 sekunda):


```bash
ping -i 0.2 -c 10 192.168.1.7
```


Powoduje to wysłanie 10 żądań ICMP w odstępach 0,2 sekundy. Takie testy są przydatne do wykrywania wahań opóźnień w krótkim okresie lub do lekkiego obciążania łącza w celu oceny jego stabilności.


### Narzędzia do analizy tabeli routingu


Polecenie `ip route`, część pakietu `iproute2`, jest zalecanym i standardowym narzędziem w nowoczesnych systemach Linux do sprawdzania i zarządzania tablicą routingu IP jądra. Zastępuje przestarzałe polecenie `route`, oferując bardziej przejrzystą składnię, większą spójność i rozszerzone wsparcie dla nowoczesnych funkcji (IPv6, wiele tablic, przestrzenie nazw itp.).


#### Wyświetlanie tablicy routingu


Aby wyświetlić bieżącą tabelę routingu:


```bash
ip route show
```


To wyjście wyświetla wszystkie trasy znane jądru, czyli ścieżki wychodzących pakietów w zależności od ich miejsca docelowego.


Przykładowe dane wyjściowe:


```bash
default via 192.168.1.1 dev eth0 proto dhcp metric 100
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
```


Każda linia reprezentuje trasę. Kluczowe pola obejmują:


- default**: domyślna trasa, używana, gdy nie pasuje żadna bardziej szczegółowa trasa.
- via**: brama używana do dotarcia do miejsca docelowego.
- dev**: używana sieć Interface.
- proto**: w jaki sposób trasa została utworzona (ręcznie, DHCP, jądro itp.).
- metric**: koszt trasy, używany do nadawania priorytetu wielu możliwym ścieżkom.
- scope**: zakres trasy (np. `link` dla trasy połączonej bezpośrednio).
- src**: źródłowy adres IP Address używany dla pakietów wychodzących na tym Interface.


#### Dodawanie i usuwanie tras


Tabelę routingu można również modyfikować dynamicznie, na przykład dodając lub usuwając trasy statyczne.


Dodawanie trasy statycznej:


```bash
ip route add 192.168.1.0/24 via 192.168.1.1 dev eth0
```


Konfiguruje to trasę do sieci `192.168.1.0/24` przez bramę `192.168.1.1` na Interface `eth0`.


Usuń tę trasę:


```bash
ip route del 192.168.1.0/24
```


To polecenie usuwa wcześniej zdefiniowaną trasę.


#### Przydatne polecenia


Oto kilka przydatnych wariantów do analizy lub tworzenia skryptów:


- `ip -4 route`: wyświetla tylko trasy IPv4;
- `ip -6 route`: wyświetla tylko trasy IPv6;
- `ip route list table main`: wyświetla główną tablicę routingu (wartość domyślna);
- `ip route get <Address>`: pokazuje Interface i bramę, której użyje pakiet do danego Address.


Przykład:


```bash
ip route get 8.8.8.8
```


Wyświetla to dokładną trasę, jaką pakiet musiałby pokonać, aby dotrzeć do `8.8.8.8`.


### Narzędzia do śledzenia


Jednym z najskuteczniejszych narzędzi do analizy trasy pokonywanej przez pakiety IP między hostem źródłowym a docelowym jest polecenie `traceroute`. Pokazuje ono, krok po kroku, ścieżkę podążaną przez pakiety i identyfikuje pośrednie routery, przez które przechodzą. W przypadku awarii łącza sieciowego lub przerwy w świadczeniu usług, `traceroute` pomaga wskazać dokładną lokalizację problemu.


Podobnie jak w przypadku polecenia `ping`, cel może być określony przez w pełni kwalifikowaną nazwę domeny (FQDN) lub przez adres IP Address. Na przykład:


```bash
traceroute mydmn.org
```


#### Zasada działania


`traceroute` opiera się na polu TTL (*Time To Live*) w nagłówku pakietów IP. Jak wyjaśniono wcześniej, pole to jest licznikiem dekrementowanym przez każdy router na ścieżce. Gdy TTL osiągnie zero, pakiet jest odrzucany, a router zwraca komunikat ICMP "Time Exceeded" do nadawcy. Mechanizm ten zapobiega powstawaniu nieskończonych pętli w przypadku błędnego routingu.


`traceroute` wykorzystuje to zachowanie do mapowania routerów pomiędzy nadawcą i odbiorcą:


- Najpierw wysyła serię pakietów UDP (zwykle trzy) z TTL równym 1. Pierwszy router napotyka TTL równe 0, więc odrzuca pakiet, a następnie odpowiada komunikatem ICMP, ujawniając swój adres IP Address i czas odpowiedzi.
- Następnie wysyła kolejną serię pakietów z TTL równym 2, ujawniając drugi router.
- Proces ten powtarza się aż do osiągnięcia miejsca docelowego, w którym to momencie host odpowiada komunikatem ICMP Port Unreachable, wskazując, że punkt końcowy został osiągnięty.


Domyślnie `traceroute` używa pakietów UDP wysyłanych na nieużywane porty (zazwyczaj zaczynające się od 33434), ale może być również skonfigurowany do używania ICMP (jak `ping`) lub nawet TCP, w zależności od systemu lub wariantów poleceń.


Przykładowe dane wyjściowe:


```bash
traceroute to www.google.fr (216.58.210.35), 64 hops max, 52 byte packets

1  par81-024.ff.avast.com (62.210.189.205)   25.107 ms  24.235 ms  24.383 ms
2  62-210-189-1.rev.poneytelecom.eu (62.210.189.1)  27.341 ms  27.119 ms  28.184 ms
3  a9k1-45x-s43-1.dc3.poneytelecom.eu (195.154.1.92)  25.910 ms  25.040 ms  25.558 ms
4  72.14.218.182 (72.14.218.182)  36.234 ms  39.907 ms  38.130 ms
5  108.170.244.177 (108.170.244.177)  25.880 ms
108.170.244.240 (108.170.244.240)  25.791 ms
108.170.244.177 (108.170.244.177)  26.449 ms
6  216.239.62.143 (216.239.62.143)  26.491 ms
216.239.43.157 (216.239.43.157)  26.414 ms
216.239.62.139 (216.239.62.139)  26.400 ms
...
9  108.170.246.161 (108.170.246.161)  33.174 ms
108.170.246.129 (108.170.246.129)  34.342 ms
108.170.246.161 (108.170.246.161)  33.707 ms
10  108.170.232.105 (108.170.232.105)  33.845 ms  33.846 ms
108.170.232.103 (108.170.232.103)  34.206 ms
11  lhr25s11-in-f35.1e100.net (216.58.210.35)  34.094 ms  33.353 ms  33.718 ms
```


Każda linia odpowiada przejściu przez router, z maksymalnie trzema pomiarami czasu (w milisekundach) wskazującymi opóźnienie podróży w obie strony do tego routera. Wartości te pomagają ocenić wydajność każdego segmentu sieci.


#### Interpretacja wyników


Jeśli router nie odpowiada lub filtruje komunikaty ICMP, zamiast czasu odpowiedzi wyświetlane są gwiazdki `*`. Może to oznaczać:


- zapora blokująca odpowiedzi ICMP,
- urządzenie skonfigurowane tak, aby nie odpowiadało, lub
- tymczasowy problem z łącznością wzdłuż ścieżki.


W ten sposób `traceroute` nie tylko identyfikuje przebytą trasę, ale także podkreśla punkty nietypowych opóźnień lub przerw.


W niektórych systemach można użyć równoważnego polecenia `tracepath`, które nie wymaga uprawnień roota. Dla IPv6 należy użyć `traceroute6` lub `tracepath6`.


Przykład dla śledzenia IPv6:


```bash
traceroute6 ipv6.google.com
```


### Narzędzia do sprawdzania aktywnych połączeń


Aby zdiagnozować aktywne połączenia sieciowe i monitorować aktywność sieci w systemie Linux, polecenie `ss` (skrót od _socket statistics_) jest nowoczesnym narzędziem referencyjnym. Jest ono częścią pakietu `iproute2` i zastępuje nieaktualne już `netstat`, oferując lepszą wydajność i dokładniejsze wyniki.


`ss` wyświetla aktywne połączenia TCP i UDP, porty nasłuchiwania, adresy lokalne i zdalne, stany połączeń i powiązane procesy.


#### Ogólne zastosowanie


Po uruchomieniu bez opcji, komenda `ss` wyświetla aktywne połączenia TCP. Podstawowa składnia:


```bash
ss [options]
```


Niektóre typowe opcje udoskonalania analizy:


- `-t`: pokazuje tylko połączenia TCP;
- `-u`: pokazuje tylko połączenia UDP;
- `-l`: pokazuje tylko gniazda nasłuchujące;
- `-n`: wyłączenie rozpoznawania nazw (surowe IP i numery portów) ;
- `-p`: wyświetla procesy powiązane z każdym gniazdem (PID i nazwa programu),
- `-a`: pokazuje wszystkie połączenia, w tym nieaktywne,
- `-s`: wyświetla wysokopoziomowe statystyki gniazda.


#### Studia przypadków


Aby wyświetlić wszystkie aktywne połączenia przy użyciu portu TCP 80 (HTTP):


```bash
ss -ant | grep ':80'
```


Pokazuje aktywne połączenia TCP obejmujące port 80. Stany takie jak `LISTEN`, `ESTABLISHED`, `TIME-WAIT` wskazują aktualny status każdego Exchange.


Przykładowe dane wyjściowe:

```
ESTAB 0 0 192.168.1.10:54321  93.184.216.34:80
```


Aby wyświetlić wszystkie połączenia sieciowe z powiązanymi procesami:


```bash
ss -tulnp
```


Aby uzyskać ogólne podsumowanie użycia gniazda:

```bash
ss -s
```


Aby filtrować tylko połączenia UDP:

```bash
ss -unp
```


Polecenia te są szczególnie przydatne do wykrywania podejrzanych połączeń, nieoczekiwanych portów nasłuchiwania lub monitorowania aktywności określonej usługi.


## Transport i odkładanie narzędzi Layer


<chapterId>bce47931-930e-4288-b0fd-666c9a1066b5</chapterId>


### Narzędzia zapytań DNS


W wyższych warstwach modelu TCP/IP, zwłaszcza w Layer aplikacji, ważne jest, aby zrozumieć, jak działa rozpoznawanie nazw. Narzędzia zapytań DNS pozwalają sprawdzić, czy nazwa domeny jest poprawnie powiązana z adresem IP Address, a także pomagają zdiagnozować problemy z serwerem DNS, takie jak błędna konfiguracja, opóźnienia propagacji lub niedostępność. Narzędzia te są niezbędne dla każdego administratora sieci lub każdego użytkownika, który chce lepiej zrozumieć wymianę DNS w środowisku IP.


#### Polecenie `nslookup`


Najprostszym narzędziem zapytań DNS jest `nslookup`. Wysyła ono zapytanie do serwera DNS i zwraca adres IP Address powiązany z nazwą domeny (lub odwrotnie). Domyślnie wysyła zapytanie do skonfigurowanego w systemie serwera DNS, ale można również określić serwer bezpośrednio w poleceniu.


Przykład bezpośredniego wyszukiwania:

```bash
nslookup mydmn.org
```


Odpytywanie określonego serwera DNS:

```bash
nslookup mydmn.org 192.6.23.4
```


Żądanie prosi serwer DNS pod adresem `192.6.23.4` o rozwiązanie nazwy `mydmn.org`. Jest to szczególnie przydatne do sprawdzenia, czy dany serwer DNS rozpoznaje nazwę domeny lub do sprawdzenia, czy serwer działa poprawnie.


#### Polecenie `dig`


`dig` (*Domain Information Groper*) jest bardziej nowoczesnym, kompletnym i elastycznym narzędziem niż `nslookup`. Obsługuje złożone zapytania i dostarcza szczegółowych informacji na temat procesu rozwiązywania, hierarchii zaangażowanych serwerów, typu zwróconego rekordu (A, AAAA, MX, TXT itp.) oraz wszelkich napotkanych błędów.


Przykład zapytania podstawowego:

```bash
dig mydmn.org
```


Odpytywanie określonego serwera DNS:

```bash
dig @192.6.23.4 mydmn.org
```


To polecenie sprawdza dostępność rekordu DNS na danym serwerze.

Jedną z kluczowych zalet `dig` jest to, że pokazuje szczegóły odpowiedzi DNS, co czyni go bardzo przydatnym do diagnozowania błędów konfiguracji.


#### Ręczna konfiguracja resolwerów DNS


Czasami konieczne jest zastąpienie serwerów DNS używanych lokalnie, na przykład w środowiskach testowych lub w celu wymuszenia użycia określonych serwerów. Można to zrobić edytując plik `/etc/resolv.conf`, który definiuje ustawienia rozdzielczości DNS systemu.


Przykładowa konfiguracja:


```bash
vi /etc/resolv.conf

search mydmn.org
nameserver 192.168.1.10
nameserver 192.168.1.11
```



- Pole `search` określa domenę, która ma być automatycznie dołączana podczas rozwiązywania krótkich nazw.
- Wpisy `nameserver` definiują serwery DNS, które mają być używane, w kolejności priorytetów.


W wielu nowoczesnych dystrybucjach (zwłaszcza tych używających `systemd-resolved`), zmiany w `/etc/resolv.conf` są tymczasowe i mogą zostać nadpisane przy ponownym uruchomieniu lub ponownym połączeniu z siecią. Bardziej trwałe metody obejmują użycie `resolvconf`, `systemd-resolved` lub modyfikację konfiguracji *NetworkManager*.


#### Polecenie `host`


Innym prostym, ale skutecznym narzędziem DNS jest `host`. Rozpoznaje nazwy domen na adresy IP (lub odwrotnie) i może pomóc w diagnozowaniu awarii DNS lub błędnych konfiguracji w sieci Interface.


Przykłady:

```bash
host mydmn.org
```


Wyszukiwanie wsteczne:

```bash
host 192.6.23.4
```


`host` jest szczególnie przydatny do szybkiego sprawdzania, zwłaszcza gdy jest używany w skryptach wiersza poleceń.


Powtarzające się lub intensywne zapytania do serwerów DNS innych firm bez pozwolenia mogą być interpretowane jako próby włamania lub złośliwa aktywność. Używane nieprawidłowo lub w sieciach, których nie kontrolujesz, polecenia te mogą przypominać skanowanie rozpoznawcze, które często jest pierwszym krokiem w ataku. Zawsze ograniczaj ich użycie do środowisk, którymi administrujesz lub w których masz wyraźną autoryzację.


### Narzędzia do skanowania sieci


Podczas monitorowania lub zabezpieczania sieci lokalnej lub rozległej kluczowe znaczenie ma identyfikacja aktywnych urządzeń i usług, które udostępniają. Dokładnie to robi narzędzie `nmap` (*Network Mapper*).


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

#### Przedstawiamy `nmap`


`nmap` umożliwia ukierunkowane skanowanie jednego lub więcej hostów w celu wykrycia otwartych portów, dostępnych usług (HTTP, SSH, DNS itp.), a czasem nawet typu używanego systemu operacyjnego. Dzięki wielu opcjom, `nmap` zapewnia dokładny przegląd powierzchni narażenia sieci, niezbędny podczas audytu lub fazy utwardzania zarządzania infrastrukturą.


Podobnie jak polecenie `host`, `nmap` nigdy nie może być używane w sieciach lub infrastrukturach, których nie jesteś właścicielem lub bez wyraźnej autoryzacji. Nieautoryzowane skanowanie portów może zostać oznaczone jako złośliwa próba rekonesansu, jest często wykrywane przez systemy bezpieczeństwa (firewalle, IDS/IPS), a nawet może prowadzić do konsekwencji prawnych.


#### Użycie podstawowe


Aby przeskanować określony host i wyświetlić jego otwarte porty:

```bash
nmap 192.168.0.1
```


To polecenie skanuje 1000 najczęściej używanych portów na hoście `192.168.0.1` i wyświetla usługi, do których uzyskano dostęp i używane protokoły. Jeśli rozdzielczość DNS jest skonfigurowana, można również użyć nazwy hosta zamiast adresu IP Address.


#### Pełne skanowanie sieci


Jedną z zalet `nmap` jest jego zdolność do skanowania całego zakresu adresów za pomocą jednego polecenia. Ułatwia to na przykład szybką inwentaryzację wszystkich aktywnych maszyn w sieci:


```bash
nmap 192.168.0.0/24
```


W tym przypadku, wszystkie hosty w zakresie od `192.168.0.0` do `192.168.0.255` zostaną sprawdzone. Dla każdego IP Address wyniki zawierają listę otwartych portów, ich status (otwarte, filtrowane itp.) oraz, jeśli to możliwe, nazwę odpowiedniej usługi.



![Image](assets/fr/055.webp)



Administrator może polegać na `nmap` w kilku zadaniach:


- Wykrywanie aktywnych hostów**: identyfikacja, które maszyny odpowiadają w podsieci;
- Inwentaryzacja usług**: zapewnienie dostępu tylko do niezbędnych portów (zasada najmniejszych uprawnień);
- Kontrola zgodności**: porównanie otwartych portów z polityką bezpieczeństwa organizacji;
- Zapobieganie lukom w zabezpieczeniach**: wykrywanie niezabezpieczonych lub nieaktualnych usług działających na krytycznych komputerach.


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

### Narzędzia do analizy procesów


W celu dogłębnej analizy aktywnych procesów i otwartych plików, zwłaszcza w kontekście sieciowym, administratorzy Linuksa często korzystają z polecenia `lsof` (*List Open Files*). Pomimo swojej nazwy, `lsof` nie ogranicza się do tradycyjnych plików: w systemach UNIX wszystko jest uważane za plik, w tym gniazda sieciowe, urządzenia i kanały komunikacyjne.


Narzędzie to zapewnia zatem przekrojowy widok systemu poprzez korelację aktywnych procesów, otwartych portów sieciowych, otwieranych plików i zaangażowanych użytkowników.


#### Analiza sieci za pomocą `lsof`


Opcja `-i` ogranicza wyjście do połączeń sieciowych (TCP, UDP, IPv4 lub IPv6). Ułatwia to sprawdzenie, które procesy komunikują się przez sieć:


```bash
lsof -i
```


To polecenie wyświetla listę wszystkich uruchomionych procesów korzystających z gniazda sieciowego, pokazując używany port, protokół (TCP/UDP), stan połączenia, a także PID i powiązanego użytkownika.


#### Filtrowanie według adresu IP Address lub portu


Wyszukiwanie można zawęzić, określając adres IP Address i port, izolując określony przepływ sieciowy. Na przykład, aby sprawdzić sesję SMTP (port 25) z określonym hostem:


```bash
lsof -n -i @192.168.2.1:25
```


Wyświetli to tylko aktywne połączenia sieciowe z hostem `192.168.2.1` na porcie 25, przydatne do diagnozowania podejrzanej aktywności lub problemów z przepływem SMTP.


#### Śledzenie dostępu do urządzenia


Kolejną mocną stroną `lsof` jest śledzenie specjalnych plików, takich jak partycje dyskowe. Na przykład, aby sprawdzić, które procesy otworzyły pliki na `/dev/sda1`:


```bash
lsof /dev/sda1
```


Jest to przydatne, gdy próba odmontowania nie powiedzie się, ponieważ urządzenie jest nadal używane lub podczas sprawdzania, które aplikacje uzyskują dostęp do partycji.


#### Analiza krzyżowa: proces i sieć


Opcje można łączyć w celu uzyskania dokładnego wglądu. Na przykład, aby zobaczyć wszystkie porty sieciowe otwarte przez proces z PID 1521:


```bash
lsof -i -a -p 1521
```


Opcja `-a` przecina kryteria (`-i` i `-p`), ograniczając wyjście tylko do połączeń sieciowych tego procesu.


#### Śledzenie wielu użytkowników


`lsof` może być również używany do analizowania aktywności określonych użytkowników, wyświetlając listę wszystkich otwartych przez nich plików, opcjonalnie filtrowanych według PID:


```bash
lsof -p 1521 -u 500,phil
```


To pokazuje pliki lub połączenia sieciowe używane przez użytkownika `phil` lub UID 500, ograniczone do procesu 1521.


### Podsumowanie sekcji


W tej ostatniej sekcji zbadaliśmy szeroką gamę niezbędnych narzędzi do diagnozowania, analizowania i administrowania sieciami komputerowymi. Zbudowane wokół warstw modelu TCP/IP, badanie to nie tylko wyjaśnia, jak działa komunikacja sieciowa, ale także ustanawia rygorystyczną metodologię identyfikacji, izolowania i rozwiązywania potencjalnych problemów.


Narzędzia te zapewniają administratorom spójny zestaw dźwigni technicznych do monitorowania stanu sieci, analizowania ruchu, audytu połączeń i szybkiej interwencji w przypadku wadliwego sprzętu lub usług.


#### Dostęp do sieci Layer


Narzędzia zapewniające bezpośredni wgląd w interfejsy i ramki:


- arp / ip neigh**: sprawdza i modyfikuje pamięć podręczną ARP/NDP w celu sprawdzenia lub skorygowania powiązań IP-MAC;
- tcpdump**: przechwytywanie pakietów z wiersza poleceń, z możliwością filtrowania i eksportowania;
- Wireshark**: graficzna analiza pakietów z głębokim dekodowaniem protokołów;
- ethtool**: odpytywanie i dostosowywanie fizycznych parametrów karty Ethernet (prędkość, dupleks, WoL itp.).


#### Sieć Layer


Narzędzia do oceny łączności IP, routingu i ruchu pakietów:


- ping**: testuje osiągalność i mierzy opóźnienie za pomocą protokołu ICMP;
- ip route**: sprawdza i modyfikuje tablicę routingu w celu kontrolowania ścieżek pakietów;
- traceroute**: identyfikacja routerów hop-by-hop na trasie do miejsca docelowego;
- ss**: szczegółowy spis gniazd TCP/UDP i powiązanych procesów (następca netstat).


#### Warstwy transportu i aplikacji


Narzędzia do diagnozowania usług i procesów:


- nslookup / dig / host**: Zapytania DNS w celu sprawdzenia rozdzielczości nazwy i analizy rekordów;
- nmap**: badanie otwartych portów i ujawnionych usług w celu oceny powierzchni ataku;
- lsof**: wyświetla listę plików i gniazd otwieranych przez procesy, korelując aktywność systemu i sieci.


Opanowanie tych narzędzi, z których każde jest dostosowane do określonego etapu modelu TCP/IP, umożliwia metodyczne podejście: począwszy od fizycznego Layer, poprzez routing, aż po usługi aplikacji. Ten łańcuch wiedzy pozwala administratorom diagnozować, zabezpieczać i optymalizować infrastrukturę, zapewniając zarówno wydajność, jak i dostępność sieci.


# Część końcowa


<partId>09d5393c-63bc-42fc-bf79-c65e380211bd</partId>


## Recenzje i oceny


<chapterId>114c33c0-9831-4d74-affd-f5d37adc53c3</chapterId>


<isCourseReview>true</isCourseReview>

## Egzamin końcowy


<chapterId>b99e005e-8dd0-4fa4-b302-f940c27a30ac</chapterId>


<isCourseExam>true</isCourseExam>

## Wnioski


<chapterId>3b449814-78f3-41c0-8138-0a04f3682719</chapterId>


<isCourseConclusion>true</isCourseConclusion>