---
name: Umbrel LND
description: Zaawansowany samouczek dotyczący instalacji i konfiguracji Lightning Network Daemon (LND) na Umbrel
---
![cover](assets/cover.webp)




## Wprowadzenie



Ten zaawansowany samouczek przeprowadzi Cię krok po kroku przez instalację, konfigurację i korzystanie z aplikacji Lightning Node (LND) na węźle Umbrel. Dowiesz się, jak otwierać kanały, zarządzać płynnością i synchronizować węzeł z aplikacją mobilną.



## 1. Wymagania wstępne: funkcjonalny węzeł Bitcoin Umbrel



Przed wdrożeniem Lightning musisz mieć w pełni działający węzeł Bitcoin na Umbrel. Obejmuje to instalację Umbrel (na Raspberry Pi, NAS lub innej maszynie) i pełną synchronizację Blockchain Bitcoin.



Aby zainstalować Umbrel i skonfigurować węzeł Bitcoin, zalecamy skorzystanie z naszego dedykowanego samouczka:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Upewnij się, że węzeł Bitcoin jest aktualny i działa prawidłowo, ponieważ Lightning Network opiera się na nim we wszystkich transakcjach off-chain.



## 2. Wprowadzenie do Lightning Network



Lightning Network to drugi protokół Layer zaprojektowany w celu przyspieszenia i zmniejszenia kosztów transakcji Bitcoin poprzez przeprowadzanie ich poza głównym Blockchain.



Mówiąc konkretnie, Lightning wykorzystuje sieć kanałów płatności między węzłami: dwóch użytkowników otwiera kanał, blokując On-Chain BTC (transakcja początkowa), a następnie może natychmiast dokonać płatności Exchange w ramach tego kanału. Te transakcje off-chain nie są rejestrowane na Blockchain, stąd ich szybkość i praktycznie zerowy koszt.



Płatności mogą być kierowane wieloma kanałami (dzięki węzłom pośredniczącym), aby dotrzeć do dowolnego odbiorcy w sieci, umożliwiając niemal nieograniczoną skalę natychmiastowych transakcji. Lightning oferuje zatem bardzo szybkie, tanie transakcje, idealne do codziennych płatności lub mikrotransakcji, jednocześnie odciążając Blockchain Bitcoin.



Aby działać, węzeł Lightning musi być stale podłączony do sieci i wchodzić w interakcje z innymi węzłami Lightning. Istnieją różne implementacje oprogramowania (LND, Core Lightning, Eclair itp.), z których wszystkie są ze sobą kompatybilne. Umbrel używa LND (Lightning Network Daemon) jako części swojej oficjalnej aplikacji Lightning Node. Ten samouczek koncentruje się na LND.



Aby uzyskać pełne teoretyczne wprowadzenie do Lightning Network, zalecamy skorzystanie z naszego dedykowanego kursu:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Ten kurs zapewni ci gruntowne podstawy podstawowych koncepcji Lightning Network, zanim przejdziesz do praktyki z węzłem LND.



## 3. Dlaczego samodzielny hosting LND?



Obsługa własnego węzła Lightning (LND) na platformie Umbrel zapewnia całkowitą suwerenność nad środkami i kanałami, w porównaniu z rozwiązaniami powierniczymi lub półpowierniczymi.



### Porównanie rozwiązań Lightning :



**Solutions custodiales (ex: Wallet of Satoshi)** :




- Bitcoiny Lightning są zarządzane przez zaufaną stronę trzecią
- Łatwa obsługa, brak złożoności technicznej
- Operator przechowuje środki użytkownika i może śledzić jego transakcje
- Poświęcasz kontrolę i poufność



**Portfele konsumenckie nietowarowe (np. Phoenix, Breez)** :




- Użytkownicy zachowują swoje klucze prywatne, a tym samym Ownership swoich BTC
- Brak pełnego zarządzania węzłami - aplikacja zarządza kanałami w tle
- Kompromis między prostotą a suwerennością
- Zależność od infrastruktury dostawców w zakresie płynności
- Ograniczenia techniczne (jeden smartfon nie może przekierowywać płatności dla innych)



** Samodzielnie hostowany węzeł LND (Umbrel)** :




- Maksymalna suwerenność: twoje BTC On-Chain i off-chain są całkowicie pod twoją kontrolą
- Żadne strony trzecie nie są zaangażowane w otwieranie kanałów ani zarządzanie płatnościami
- Zwiększona poufność (Twoje kanały i transakcje są znane tylko Tobie i Twoim bezpośrednim współpracownikom)
- Swoboda użytkowania: łączenie się z własnymi usługami i portfelami
- Możliwość przekierowywania transakcji dla innych (wynagrodzenie w postaci mikropłatności)
- Zwiększona odpowiedzialność techniczna (konserwacja, zarządzanie płynnością, kopie zapasowe)



Krótko mówiąc, samodzielny hosting LND zapewnia maksymalną kontrolę, ale wymaga większych umiejętności technicznych. To kompromis między wygodą a suwerennością.



## 4. Samouczek krok po kroku



### 4.1 Instalacja i konfiguracja aplikacji Lightning Node na platformie Umbrel



Po zsynchronizowaniu węzła Umbrel (Bitcoin) wykonaj następujące kroki:



![Installation de Lightning Node depuis l'App Store Umbrel](assets/fr/01.webp)



Zainstaluj aplikację Lightning Node z sekcji "App Store" w Interface Umbrel.



![Avertissement sur la nature expérimentale de Lightning](assets/fr/02.webp)



LND (Lightning Network Daemon) zostanie wdrożony na twoim Umbrelu jako aplikacja. Gdy otworzysz ją po raz pierwszy, zobaczysz komunikat ostrzegawczy informujący, że Lightning jest technologią eksperymentalną.



![Création ou restauration d'un nœud LND](assets/fr/03.webp)



Do wyboru jest utworzenie nowego węzła lub przywrócenie węzła z kopii zapasowej/seed. W przypadku pierwszej instalacji wybierz utworzenie nowego węzła. Aplikacja Lightning Node wyświetli generate 24-wyrazową frazę Mnemonic (Twój seed Lightning): zapisz ją bardzo uważnie (najlepiej offline, na papierze), ponieważ w razie potrzeby posłuży ona do przywrócenia funduszy Lightning.



**Uwaga: W najnowszych wersjach Umbrel instalacja aplikacji Lightning zapewnia to 24-słowne seed (sam węzeł Bitcoin Umbrel nie).



![Interface principale de Lightning Node](assets/fr/04.webp)



Po inicjalizacji uzyskasz dostęp do głównego Interface Lightning Node.



![Paramètres de l'application](assets/fr/05.webp)



W ustawieniach aplikacji znajduje się kilka ważnych opcji:




   - Sprawdź swój Node ID (unikalny identyfikator węzła)
   - Podłączanie zewnętrznego Wallet (Podłącz Wallet)
   - Zobacz tajne słowa
   - Dostęp do ustawień zaawansowanych
   - Odzyskiwanie kanałów
   - Pobierz plik kopii zapasowej kanału
   - Włącz automatyczne tworzenie kopii zapasowych
   - Konfiguracja kopii zapasowej przez Tor (Backup over Tor)



Opcje te są niezbędne dla bezpieczeństwa i zarządzania węzłem Lightning. Upewnij się, że aktywowałeś automatyczne tworzenie kopii zapasowych i przechowujesz swoje tajne słowa w bezpiecznym miejscu.



**Przydatne zasoby:**




- [Umbrel Community](https://community.umbrel.com) - Forum dyskusyjne dla użytkowników, aby dzielić się problemami i rozwiązaniami dotyczącymi Umbrel i jego ekosystemu


> - [Umbrel App Store - Lightning Node (LND)](https://apps.umbrel.com/app/lightning) - Opis funkcji aplikacji Lightning Node na Umbrel
> - [LND Docs - Quickstart](https://docs.lightning.engineering/lightning-network-tools/LND/run-LND) - Oficjalna dokumentacja LND

### 4.2 Otwieranie kanału Lightning



Po uruchomieniu LND możesz otworzyć swój pierwszy kanał Lightning. Aby znaleźć wysokiej jakości węzły, z którymi można się połączyć:



![Page d'accueil Amboss.space](assets/fr/06.webp)



[Amboss.space](https://amboss.space/) to eksplorator służący do wyszukiwania niezawodnych węzłów do otwierania kanałów.



![Exemple de nœud ACINQ sur Amboss](assets/fr/07.webp)



Na przykład [węzeł ACINQ](https://amboss.space/node/03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f) jest uznanym węzłem z doskonałymi statystykami dostępności i płynności.



![Informations de connexion Swiss Bitcoin Pay](assets/fr/08.webp)



W tym samouczku otworzymy kanał z [Swiss Bitcoin Pay](https://amboss.space/node/03c181e13a09a649c13f60ea3ddbeefc66123c43280da8eebc19f54445f35173ca). Informacje wymagane do połączenia (pubkey@ip:port) są podane na stronie Amboss.



Aby otworzyć kanał :



![Bouton d'ouverture de canal](assets/fr/09.webp)



Na stronie głównej Lightning Node kliknij przycisk "+ OPEN CHANNEL"



![Configuration du canal](assets/fr/10.webp)



Na stronie konfiguracji kanału :




   - Wklej identyfikator węzła skopiowany z Amboss (format: pubkey@ip:port)
   - Zdefiniuj pojemność kanału (niektóre węzły, takie jak ACINQ, mają minimalne wartości, np. 400 tys. Sats)
   - W razie potrzeby dostosuj opłaty za transakcję otwarcia



![Canal en cours d'ouverture](assets/fr/11.webp)



Po wysłaniu transakcji kanał pojawi się jako "otwarty" na stronie głównej. Poczekaj na potwierdzenie transakcji On-Chain.



![Détails du canal](assets/fr/12.webp)



Kliknij kanał, aby wyświetlić jego szczegóły:




   - Aktualny status
   - Całkowita pojemność
   - Podział płynności (przychodzące/wychodzące)
   - Klucz publiczny węzła zdalnego
   - I inne informacje techniczne



### Korzystanie z Lightning Network+ w celu uzyskania płynności przychodzącej



![Lightning Network+ dans l'App Store](assets/fr/13.webp)



Lightning Network+ jest dostępny w Umbrel App Store, aby ułatwić zdobywanie przychodzącej gotówki.



![Interface principale de LN+](assets/fr/14.webp)



Główny Interface oferuje trzy ważne opcje:




- "Swapy płynnościowe: poznaj dostępne oferty swapów
- "Otwórz dla mnie": filtruj swapy, do których się kwalifikujesz
- "To Docs": dostęp do dokumentacji



![Message d'erreur LN+](assets/fr/15.webp)



Uwaga: Jeśli nie masz jeszcze otwartego kanału, zobaczysz ten komunikat o błędzie po kliknięciu "Otwórz dla mnie".



![Liste des swaps disponibles](assets/fr/16.webp)



Strona "Swapy płynnościowe" pokazuje wszystkie oferty swapów dostępne w sieci.



![Swaps éligibles](assets/fr/17.webp)



"Otwórz dla mnie" filtruje tylko te swapy, dla których węzeł spełnia wymagane warunki.



![Détails d'un swap](assets/fr/18.webp)



Przykład szczegółów wymiany:




- Konfiguracja Pentagon (5 uczestników)
- Pojemność 300 tys. Sats na kanał
- Wymagania wstępne: co najmniej 10 otwartych kanałów o łącznej przepustowości 1 M Sats
- Dostępne miejsca: 4/5



### 4.3 Synchronizacja z aplikacją mobilną (Zeus)



Do zdalnego sterowania węzłem Lightning (smartfon) można użyć aplikacji Zeus (aplikacja open-source dostępna na iOS/Android).



**Konfiguracja Zeusa z Umbrelem :**



![Bouton "Connect Wallet" dans l'interface LND](assets/fr/19.webp)



Upewnij się, że twój węzeł Umbrel jest dostępny (domyślnie przez Tor).


W Interface Umbrel otwórz aplikację Lightning Node, a następnie kliknij przycisk "Connect Wallet", jak wskazuje strzałka.



![Page de connexion avec QR code](assets/fr/20.webp)



Pojawi się kod QR zawierający dane dostępu do LND w formacie lndconnect. Ten kod QR zawiera szczególnie dużo informacji, więc nie wahaj się go powiększyć, aby ułatwić jego odczytanie.



![Configuration initiale de Zeus](assets/fr/21.webp)



W telefonie :




   - Otwarty Zeus
   - Na stronie głównej kliknij "Konfiguracja zaawansowana", aby podłączyć własny węzeł Lightning
   - W parametrach wybierz "Utwórz lub podłącz Wallet"



![Configuration de la connexion LND dans Zeus](assets/fr/22.webp)



W Zeus:




   - Jako typ połączenia wybierz "LND (REST)"
   - Możesz zeskanować kod QR (zalecana metoda) lub wprowadzić informacje ręcznie. (Nie wahaj się powiększyć kodu QR Umbrel, ponieważ jest on bardzo gęsty)
   - Ważne: aktywuj opcję "Użyj Tora", jeśli twój Umbrel jest dostępny tylko przez Tora (domyślnie)
   - Zapisz konfigurację



Twój Zeus jest teraz połączony z węzłem Umbrel i umożliwia dokonywanie płatności Lightning, przeglądanie kanałów, sald itp.



**Zaawansowane opcje połączeń:**



Domyślnie połączenie Zeus ↔ Umbrel odbywa się za pośrednictwem sieci Tor. Aby uzyskać szybsze połączenie, istnieją dwie alternatywy:



**Lightning Node Connect (LNC)** :




   - Mechanizm szyfrowanych połączeń Lightning Labs
   - Zainstaluj aplikację Lightning Terminal na Umbrel (obejmuje dostęp do LNC)
   - generate kod QR połączenia w Lightning Terminal (Connect → Connect Zeus via LNC)
   - Zeskanuj go do aplikacji Zeus (jako typ połączenia wybierz "LNC")



**VPN Tailscale**:




   - Łatwa w konfiguracji sieć VPN typu mesh
   - Zainstaluj Tailscale na Umbrel (App Store) i na swoim telefonie komórkowym
   - Połączenie Zeus przez prywatny adres IP Tailscale zamiast Tor Address



Opcje te nie są obowiązkowe, a rozwiązanie Tor + Zeus działa dobrze w większości przypadków.



> **Przydatne zasoby:**
> - [Zeus Documentation - Umbrel Connection](https://community.umbrel.com/t/zeus-LN-mobile/7619) - Oficjalny przewodnik po połączeniu Zeusa z Umbrelem
> - [Zeus GitHub](https://github.com/ZeusLN/zeus) - Projekt open-source Zeus
> - [Umbrel Community - Connecting Zeus via Tailscale](https://community.umbrel.com/t/how-to-use-tailscale-with-umbrel/6782) - Przewodnik po łączeniu Zeusa z Umbrelem za pomocą Tailscale

## 5. Bezpieczeństwo i najlepsze praktyki



Zarządzanie samodzielnie hostowanym węzłem Lightning wymaga szczególnej dbałości o bezpieczeństwo.



### Kopia zapasowa i bezpieczeństwo węzła



**Najważniejsze rodzaje kopii zapasowych**



Węzeł Lightning Umbrel wymaga dwóch rodzajów kopii zapasowych:



**Zdanie seed (24 słowa)**




- Odzyskuje fundusze On-Chain
- Niezbędne do odtworzenia Wallet Lightning
- Do bardzo bezpiecznego przechowywania (offline, na papierze)



*plik *Static Channel Backup (SCB)**




- Zawiera informacje o kanale Lightning
- Umożliwia wymuszone zamknięcie kanału w przypadku awarii
- Ważne:** Nigdy nie zapisuj pliku `channel.db` ręcznie (ryzyko kar)



**Ręczna procedura tworzenia kopii zapasowej



Aby zapisać kanały ręcznie :


1. Dostęp do menu Lightning Node (trzy kropki "⋮" obok "+ Open Channel")


2. Pobierz plik kopii zapasowej kanału


3. Eksport nowego SCB po każdej modyfikacji kanału


4. Bezpieczne przechowywanie SCB (zaszyfrowany nośnik, kopia poza siedzibą firmy)



**Umbrel** automatyczny system tworzenia kopii zapasowych



Umbrel posiada zaawansowany system automatycznego tworzenia kopii zapasowych, który zapewnia :



*Ochrona danych:*




- Szyfrowanie po stronie klienta przed transmisją
- Wysyłanie przez sieć Tor
- Dane uzupełnione losowym wypełnieniem
- Klucz szyfrowania unikalny dla urządzenia



*Zwiększone bezpieczeństwo:*




- Natychmiastowe tworzenie kopii zapasowych przy zmianach statusu
- Kopie zapasowe "przynęty" w losowych odstępach czasu
- Ukryj zmiany rozmiaru kopii zapasowej
- Ochrona przed analizą czasu



*Proces przywracania:*




- Identyfikator i klucz pochodzący z parasola seed
- Kompletna odbudowa możliwa tylko z frazą Mnemonic
- Automatyczne odzyskiwanie najnowszych kopii zapasowych
- Przywracanie ustawień kanału i danych



### Przywracanie sprawności



Jeśli węzeł zostanie utracony (awaria sprzętu, uszkodzona karta SD):




- Ponowny montaż parasola
- Wprowadź swoje 24 słowa seed w aplikacji Lightning
- Zaimportuj plik SCB podczas przywracania



LND skontaktuje się z każdym partnerem Twoich starych kanałów, aby je zamknąć i odzyskać Twój udział w funduszach On-Chain. Kanały zostaną zamknięte na stałe (w razie potrzeby zostaną ponownie otwarte).



### Dostępność i ochrona przed oszustwami



Najlepiej pozostawiać węzeł online tak często, jak to możliwe. W przypadku dłuższej nieobecności:




- Złośliwy peer może próbować rozgłaszać stary stan kanału
- Lightning przewiduje "okres protestacyjny" (około 2 tygodni na LND)
- Jeśli zamierzasz wyjechać na dłuższy czas, skonfiguruj Watchtower



**Konfiguracja Watchtower:**




- W ustawieniach zaawansowanych LND dodaj adres URL zaufanego serwera Watchtower
- Możesz skorzystać z usługi publicznej lub zainstalować własną Watchtower




Aby dowiedzieć się więcej na temat konfigurowania i korzystania z wież strażniczych, zalecamy zapoznanie się z naszym dedykowanym samouczkiem :



https://planb.network/tutorials/node/lightning-network/watch-tower-26937006-dfe5-404e-9ee4-e82e422c5cf2
### Inne najlepsze praktyki





- Aktualizacje oprogramowania:** Aktualizuj Umbrel i LND (poprawki bezpieczeństwa)
- Ochrona sprzętu:** Używaj stabilnego systemu (Raspberry Pi z dyskiem SSD, mini-PC) i zasilacza UPS
- Bezpieczeństwo sieci:** Zachowaj domyślną konfigurację Tora, zmień hasło administratora Umbrel (domyślnie: "moneyprintergobrrr")
- Szyfrowanie:** Włącz szyfrowanie dysku, jeśli to możliwe



## 6. Dodatkowe narzędzia



Aplikacja Lightning Node firmy Umbrel zapewnia podstawowe funkcje do zarządzania kanałami, ale narzędzia innych firm oferują zaawansowane funkcje.



### ThunderHub



Interface nowoczesny, oparty na przeglądarce internetowej system zarządzania węzłami Lightning, który można zainstalować za pośrednictwem Umbrel App Store.



**Cechy:**




- Wizualizacja kanałów w czasie rzeczywistym (pojemności, salda)
- Zintegrowane narzędzia do równoważenia
- Obsługa rozliczeń wielościeżkowych (MPP)
- Generowanie kodu QR LNURL
- Zarządzanie transakcjami On-Chain



ThunderHub jest idealny do monitorowania aktywnego węzła routingu i wykonywania prostego równoważenia.



### Ride The Lightning (RTL)



Interface jest kompatybilny z kilkoma implementacjami Lightning (LND, Core Lightning, Eclair).



**Najważniejsze cechy:**




- Zarządzanie wieloma węzłami
- Pulpity nawigacyjne uwzględniające kontekst
- Obsługa zamiany okrętów podwodnych (Lightning Loop)
- uwierzytelnianie dwuskładnikowe
- Kopie zapasowe kanałów eksportu/importu



RTL to kompletny "szwajcarski scyzoryk" do administrowania węzłem Lightning z podejściem bardziej zorientowanym na eksperta.



### Inne przydatne narzędzia





- Lightning Shell** : Wiersz poleceń (lncli) przez przeglądarkę
- BTC RPC Explorer & Mempool** : Monitorowanie Blockchain
- LNmetrics & Torq**: Analiza wydajności routingu
- Amboss & 1ML**: "Społecznościowe" zarządzanie węzłem (aliasy, kontakty, analiza sieci)



Narzędzia te można zainstalować kilkoma kliknięciami za pośrednictwem sklepu Umbrel App Store, bez skomplikowanej konfiguracji.



**Dodatkowe zasoby narzędziowe:**




- [ThunderHub.io - Features](https://thunderhub.io) - Przegląd funkcji ThunderHub
- [Ride The Lightning (RTL) info](https://www.ridethelightning.info/) - Dokumentacja RTL
- [David Kaspar - Rebalance via ThunderHub](https://blog.davidkaspar.com) - Praktyczny przewodnik po rebalansowaniu
- [Przewodnik "Zarządzanie węzłami Lightning"](https://github.com/openoms/lightning-node-management) - Zaawansowana dokumentacja dla użytkowników zasilania



## Wnioski



Uruchomienie własnego węzła LND na Umbrel jest ważnym krokiem w kierunku suwerenności finansowej. Chociaż wymaga to większego zaangażowania technicznego niż rozwiązanie powiernicze, korzyści w zakresie kontroli, poufności i aktywnego uczestnictwa w Lightning Network są znaczące.



Postępując zgodnie z tym przewodnikiem, powinieneś być teraz w stanie zainstalować LND, otworzyć kanały, zarządzać płynnością i uzyskać zdalny dostęp do węzła. Zachęcamy do stopniowego poznawania zaawansowanych funkcji i dodatkowych narzędzi w miarę zaznajamiania się z ekosystemem.



Pamiętaj, że bezpieczeństwo Twoich środków zależy od stosowanych przez Ciebie zabezpieczeń i praktyk. Poświęć czas na zrozumienie każdego aspektu przed zaangażowaniem dużych kwot.
