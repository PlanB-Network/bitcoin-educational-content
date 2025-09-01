---
name: Graylog
description: Łatwa centralizacja i analiza logów
---
![cover](assets/cover.webp)



___



*Ten samouczek jest oparty na oryginalnej treści autorstwa Floriana BURNELA opublikowanej na stronie [IT-Connect](https://www.it-connect.fr/). Licencja [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). W oryginalnym tekście mogły zostać wprowadzone zmiany



___



## Wdrażanie Graylog na Debianie 12



### I. Prezentacja



Graylog to rozwiązanie typu "log sink" o otwartym kodzie źródłowym, zaprojektowane do centralizacji, przechowywania i analizowania logów z maszyn i urządzeń sieciowych w czasie rzeczywistym. W tym poradniku dowiemy się, jak zainstalować darmową wersję Graylog na komputerze z Debianem 12!



W ramach systemu informatycznego każdy **serwer**, niezależnie od tego, czy pracuje pod kontrolą systemu **Linux** czy **Windows**, oraz każde **urządzenie sieciowe** (switch, router, firewall itp.) **generuje własne logi**, przechowywane lokalnie. Z logami przechowywanymi lokalnie na każdej maszynie, analiza i korelacja zdarzeń jest bardzo trudna... Tutaj właśnie wkracza **Graylog**. Będzie on działał jako **log sink**, co oznacza, że **wszystkie twoje maszyny będą wysyłać mu swoje logi** (na przykład przez syslog). Graylog będzie następnie **przechowywać i indeksować te dzienniki**, umożliwiając jednocześnie globalne wyszukiwanie i tworzenie alertów.



Graylog to narzędzie do analizy i monitorowania, które ułatwia identyfikację podejrzanych zachowań i różnych problemów (ze stabilnością, wydajnością itp.).




![Image](assets/fr/034.webp)



**Uwaga: darmowa wersja, **Graylog Open**, nie jest SIEM-em takim jak Wazuh, zwłaszcza że brakuje jej prawdziwych funkcji wykrywania włamań.



### II. Wymagania wstępne



**Stack Graylog** opiera się na **kilku komponentach**, które będziemy musieli zainstalować i skonfigurować. Tutaj zainstalujemy wszystkie komponenty na tym samym serwerze, ale możliwe jest utworzenie klastrów opartych na kilku węzłach i rozłożenie ról na kilka serwerów. Na potrzeby tego samouczka zainstalujemy **Graylog 6.1**, najnowszą jak dotąd wersję.





- MongoDB 7**, aktualna zalecana wersja dla Graylog (minimum 5.0.7, maksimum 7.x)
- OpenSearch**, open source Fork Elasticsearch stworzony przez Amazon (minimum 1.1.x, maksimum 2.15.x)
- OpenJDK 17**



Serwer **Graylog** działa na **Debian 12**, ale instalacja jest możliwa na innych dystrybucjach, w tym za pośrednictwem Dockera. Maszyna wirtualna jest wyposażona w **8 GB pamięci RAM** i **256 GB miejsca na dysku**, aby mieć wystarczającą ilość zasobów dla wszystkich komponentów (w przeciwnym razie może to mieć znaczący wpływ na wydajność). Podaję to jednak orientacyjnie, ponieważ **rozmiar architektury Graylog zależy od ilości przetwarzanych informacji**. Graylog może przetwarzać 30 MB lub 300 MB danych dziennie, a także 300 GB danych dziennie... Jest to **skalowalne rozwiązanie** zdolne do obsługi **terabajtów logów** (patrz [ta strona](https://go2docs.graylog.org/current/planning_your_deployment/planning_your_deployment.html?tocpath=Plan%20Your%20Deployment%7C_____0)).



![Image](assets/fr/032.webp)



Źródło: Graylog



Przed rozpoczęciem konfiguracji należy przypisać statyczny adres IP Address do urządzenia Graylog i zainstalować najnowsze aktualizacje. Pamiętaj, aby ustawić strefę czasową lokalnego komputera i zdefiniować serwer NTP do synchronizacji daty i godziny. Oto polecenie do uruchomienia:



```
sudo timedatectl set-timezone Europe/Paris
```



**Uwaga: **Instalacja OpenSearch jest opcjonalna** w przypadku korzystania z **Graylog Data Node**.



### III Instalacja Graylog krok po kroku



Zacznijmy od zaktualizowania pamięci podręcznej pakietów i zainstalowania narzędzi, których potrzebujemy do tego, co ma nadejść.



```
sudo apt-get update
sudo apt-get install curl lsb-release ca-certificates gnupg2 pwgen
```



![Image](assets/fr/030.webp)



#### A. Instalacja MongoDB



Gdy to zrobimy, rozpoczniemy instalację MongoDB. Pobierz klucz GPG odpowiadający repozytorium MongoDB:



```
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```



Następnie dodaj repozytorium MongoDB 6 do maszyny Debian 12:



```
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```



Następnie zaktualizujemy pamięć podręczną pakietów i spróbujemy zainstalować MongoDB:



```
sudo apt-get update
sudo apt-get install -y mongodb-org
```



Nie można zainstalować MongoDB, ponieważ brakuje zależności: **libssl1.1**. Będziemy musieli zainstalować ten pakiet ręcznie, zanim będziemy mogli kontynuować, ponieważ Debian 12 nie ma go w swoich repozytoriach.



```
Les paquets suivants contiennent des dépendances non satisfaites :
mongodb-org-mongos: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
mongodb-org-server: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
E: Impossible de corriger les problèmes, des paquets défectueux sont en mode « garder en l'état ».
```



Pobierzemy pakiet DEB o nazwie "**libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb**" (najnowsza wersja) za pomocą polecenia **wget**, a następnie zainstalujemy go za pomocą polecenia **dpkg**. Spowoduje to wyświetlenie następujących dwóch poleceń:



```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
```



![Image](assets/fr/028.webp)



Uruchom ponownie instalację MongoDB:



```
sudo apt-get install -y mongodb-org
```



Następnie uruchom ponownie usługę MongoDB i włącz jej automatyczne uruchamianie po uruchomieniu serwera Debian.



```
sudo systemctl daemon-reload
sudo systemctl enable mongod.service
sudo systemctl restart mongod.service
sudo systemctl --type=service --state=active | grep mongod
```



Po zainstalowaniu MongoDB możemy przejść do instalacji kolejnego komponentu.



#### B. Instalacja OpenSearch



Przejdźmy teraz do instalacji OpenSearch na serwerze. Poniższe polecenie dodaje klucz podpisu dla pakietów OpenSearch:



```
curl -o- https://artifacts.opensearch.org/publickeys/opensearch.pgp | sudo gpg --dearmor --batch --yes -o /usr/share/keyrings/opensearch-keyring
```



Następnie dodaj repozytorium OpenSearch, abyśmy mogli później pobrać pakiet z **apt**:



```
echo "deb [signed-by=/usr/share/keyrings/opensearch-keyring] https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable main" | sudo tee /etc/apt/sources.list.d/opensearch-2.x.list
```



Zaktualizuj pamięć podręczną pakietów:



```
sudo apt-get update
```



Następnie **zainstaluj OpenSearch**, uważając, aby **zdefiniować domyślne hasło dla konta administratora** instancji. Tutaj hasło to "**IT-Connect2024!**", ale zastąp tę wartość silnym hasłem. **Unikaj słabych haseł**, takich jak "**P@hasło123**" i używaj co najmniej **8 znaków** z co najmniej jednym znakiem każdego typu (małe litery, wielkie litery, cyfra i znak specjalny), w przeciwnym razie na końcu instalacji pojawi się błąd. **Jest to warunek wstępny od wersji OpenSearch 2.12.**



```
sudo env OPENSEARCH_INITIAL_ADMIN_PASSWORD=IT-Connect2024! apt-get install opensearch
```



Prosimy o cierpliwość podczas instalacji...



Po zakończeniu poświęć chwilę na wykonanie minimalnej konfiguracji. Otwórz plik konfiguracyjny w formacie YAML:



```
sudo nano /etc/opensearch/opensearch.yml
```



Gdy plik jest otwarty, ustaw następujące opcje:



```
cluster.name: graylog
node.name: ${HOSTNAME}
path.data: /var/lib/opensearch
path.logs: /var/log/opensearch
discovery.type: single-node
network.host: 127.0.0.1
action.auto_create_index: false
plugins.security.disabled: true
```



Ta konfiguracja OpenSearch jest przeznaczona do konfiguracji pojedynczego węzła. Oto kilka wyjaśnień dotyczących różnych parametrów, których używamy:





- cluster.name: graylog**: ten parametr określa nazwę klastra OpenSearch o nazwie "**graylog**".
- node.name: ${HOSTNAME}**: nazwa węzła jest ustawiana dynamicznie, aby pasowała do nazwy lokalnej maszyny z systemem Linux. Nawet jeśli mamy tylko jeden węzeł, ważne jest, aby nazwać go poprawnie.
- path.data: /var/lib/opensearch**: ta ścieżka określa, gdzie OpenSearch przechowuje swoje dane na komputerze lokalnym, w tym przypadku w "**/var/lib/opensearch**".
- path.logs: /var/log/opensearch**: ta ścieżka określa, gdzie przechowywane są pliki dziennika OpenSearch, tutaj w "**/var/log/opensearch**".
- discovery.type: single-node**: ten parametr konfiguruje OpenSearch do pracy z pojedynczym węzłem, stąd wybór opcji "**single-node**".
- network.host: 127.0.0.1**: ta konfiguracja zapewnia, że OpenSearch nasłuchuje tylko na lokalnej pętli Interface, co jest wystarczające, ponieważ znajduje się na tym samym serwerze co Graylog.
- action.auto_create_index: false**: wyłączając automatyczne tworzenie indeksu, OpenSearch nie będzie automatycznie tworzyć indeksu, gdy dokument zostanie wysłany bez istniejącego indeksu.
- plugins.security.disabled: true**: ta opcja dezaktywuje wtyczkę bezpieczeństwa OpenSearch, co oznacza, że nie będzie uwierzytelniania, zarządzania dostępem ani szyfrowania komunikacji. To ustawienie oszczędza czas podczas konfigurowania Graylog, ale należy go unikać w produkcji (patrz [ta strona](https://opensearch.org/docs/1.0/security-plugin/index/)).



Niektóre opcje są już obecne, więc wystarczy usunąć "#", aby je aktywować, a następnie wskazać wartość. Jeśli nie możesz znaleźć opcji, możesz zadeklarować ją bezpośrednio na końcu pliku.



![Image](assets/fr/023.webp)



Zapisz i zamknij ten plik.



#### C. Konfiguracja Java (JVM)



Musisz skonfigurować wirtualną maszynę Java używaną przez OpenSearch, aby dostosować ilość pamięci, którą ta usługa może wykorzystać. Edytuj następujący plik konfiguracyjny:



```
sudo nano /etc/opensearch/jvm.options
```



Przy wdrożonej tutaj konfiguracji **OpenSearch uruchomi się z 4 GB przydzielonej pamięci i może wzrosnąć do 4 GB**, więc nie będzie żadnych zmian pamięci podczas pracy. W tym przypadku konfiguracja uwzględnia fakt, że maszyna wirtualna ma łącznie **8 GB pamięci RAM**. Oba parametry muszą mieć taką samą wartość. Oznacza to zastąpienie linii:



```
-Xms1g
-Xmx1g
```



Z tymi liniami:



```
-Xms4g
-Xmx4g
```



Poniżej znajduje się obraz modyfikacji, która ma zostać wykonana:



![Image](assets/fr/022.webp)



Po zapisaniu pliku należy go zamknąć.



Ponadto musimy sprawdzić konfigurację parametru "**max_map_count**" w jądrze Linux. Określa on limit obszarów pamięci mapowanych na proces, w celu zaspokojenia potrzeb naszej aplikacji. **OpenSearch**, podobnie jak Elasticsearch**, zaleca ustawienie tej wartości na "262144", aby uniknąć błędów zarządzania pamięcią.



Zasadniczo na świeżo zainstalowanej maszynie Debian 12 wartość jest już poprawna. Ale sprawdźmy. Uruchom to polecenie:



```
cat /proc/sys/vm/max_map_count
```



Jeśli otrzymasz wartość inną niż "**262144**", uruchom poniższe polecenie, w przeciwnym razie nie jest to konieczne.



```
sudo sysctl -w vm.max_map_count=262144
```



Na koniec włącz autostart OpenSearch i uruchom powiązaną usługę.



```
sudo systemctl daemon-reload
sudo systemctl enable opensearch
sudo systemctl restart opensearch
```



Jeśli wyświetlisz stan systemu, powinieneś zobaczyć proces Java z 4 GB pamięci RAM.



```
top
```



![Image](assets/fr/029.webp)



Następny krok: długo oczekiwana instalacja Graylog!



#### D. Instalacja Graylog



Aby **zainstalować Graylog 6.1** w najnowszej wersji, uruchom następujące 4 polecenia, aby **pobrać i zainstalować Graylog Server**:



```
wget https://packages.graylog2.org/repo/packages/graylog-6.1-repository_latest.deb
sudo dpkg -i graylog-6.1-repository_latest.deb
sudo apt-get update
sudo apt-get install graylog-server
```



Gdy to zrobimy, musimy wprowadzić pewne zmiany w konfiguracji Graylog przed próbą jego uruchomienia.



Zacznijmy od skonfigurowania tych dwóch opcji:





- password_secret**: ten parametr jest używany do zdefiniowania klucza używanego przez Graylog do zabezpieczenia przechowywania haseł użytkowników (w duchu klucza solenia). Klucz ten musi być **unikalny** i **losowy**.
- root_password_sha2**: ten parametr odpowiada domyślnemu hasłu administratora w Graylog. Jest ono przechowywane jako Hash SHA-256.



Zaczniemy od wygenerowania 96-znakowego klucza dla parametru **password_secret**:



```
pwgen -N 1 -s 96
wVSGYwOmwBIDmtQvGzSuBevWoXe0MWpNWCzhorBfvMMhia2zIjHguTbfl4uXZJdHOA0EEb1sOXJTZKINhIIBm3V57vwfQV59
```



Skopiuj zwróconą wartość, a następnie otwórz plik konfiguracyjny Graylog:



```
sudo nano /etc/graylog/server/server.conf
```



Wklej klucz do parametru **password_secret** w następujący sposób:



![Image](assets/fr/027.webp)



Zapisz i zamknij plik.



Następnie należy ustawić hasło dla domyślnie utworzonego konta "**admin**". W pliku konfiguracyjnym należy zapisać Hash hasła, co oznacza, że musi ono zostać obliczone. Poniższy przykład podaje Hash hasła "**LogsWells@**": dostosuj wartość do swojego hasła.



```
echo -n "PuitsDeLogs@" | shasum -a 256
6b297230efaa2905c9a746fb33a628f4d7aba4fa9d5c1b3daa6846c68e602d71
```



Skopiuj uzyskaną wartość jako dane wyjściowe (bez myślnika na końcu linii).



Otwórz ponownie plik konfiguracyjny Graylog:



```
sudo nano /etc/graylog/server/server.conf
```



Wklej wartość do opcji **root_password_sha2** w następujący sposób:



![Image](assets/fr/026.webp)



Będąc w pliku konfiguracyjnym, ustaw opcję "**http_bind_address**". Określ "**0.0.0.0:9000**", aby sieć Interface Graylog była dostępna na porcie **9000**, przez dowolny serwer IP Address.



![Image](assets/fr/024.webp)



Następnie ustaw opcję "**elasticsearch_hosts**" na `http://127.0.0.1:9200`, aby zadeklarować naszą lokalną instancję OpenSearch. Jest to konieczne, ponieważ nie używamy **Graylog Data Node**. Bez tej opcji nie będzie możliwe przejście dalej...



![Image](assets/fr/025.webp)



Zapisz i zamknij plik.



To polecenie aktywuje Graylog tak, aby uruchamiał się automatycznie przy następnym uruchomieniu i natychmiast uruchamiał serwer Graylog.



```
sudo systemctl enable --now graylog-server
```



Gdy to zrobisz, spróbuj połączyć się z Graylog z przeglądarki. Wprowadź adres IP Address (lub nazwę) serwera i port 9000.



**Dla Twojej informacji:**



Nie tak dawno temu, podczas pierwszego logowania do Graylog, pojawiało się okno uwierzytelniania podobne do tego poniżej. Trzeba było wpisać swój login "**admin**" i hasło. A potem byłeś niemile zaskoczony, gdy okazało się, że połączenie nie działa.



![Image](assets/fr/031.webp)



Konieczny był powrót do wiersza poleceń na serwerze Graylog i sprawdzenie logów. Mogliśmy wtedy zobaczyć, że **przy pierwszym połączeniu** konieczne jest **użycie tymczasowego hasła**, określonego w logach.



```
tail -f /var/log/graylog-server/server.log
```



![Image](assets/fr/021.webp)



Następnie trzeba było ponowić próbę połączenia z użytkownikiem "**admin**" i tymczasowym hasłem, co pozwoliło na zalogowanie się!



**To już nie ma miejsca. Wszystko, co musisz zrobić, to zalogować się przy użyciu konta administratora i hasła skonfigurowanego w wierszu poleceń



![Image](assets/fr/033.webp)



**Witamy na Interface Grayloga!



![Image](assets/fr/019.webp)



#### E. Graylog: utworzenie nowego konta administratora



Zamiast korzystać z konta administratora utworzonego natywnie przez Graylog, możesz utworzyć własne konto administratora. Kliknij menu "**System**", a następnie "**Użytkownicy i zespoły**", aby kliknąć przycisk "**Utwórz użytkownika**". Następnie wypełnij formularz i przypisz rolę administratora do swojego konta.



![Image](assets/fr/020.webp)



Spersonalizowane konto może zawierać dodatkowe informacje, takie jak imię i nazwisko oraz adres e-mail Address, w przeciwieństwie do natywnego konta administratora. Co więcej, zapewnia to lepszą identyfikowalność, gdy każda osoba pracuje z nazwanym kontem.



## Wysyłanie dzienników do Graylog za pomocą rsyslog



### I. Prezentacja



W tej drugiej części dowiemy się, jak skonfigurować maszynę z systemem Linux, aby wysyłała swoje dzienniki do serwera Graylog. Aby to zrobić, zainstalujemy i skonfigurujemy Rsyslog w systemie.



### II. Konfigurowanie Graylog do odbierania logów systemu Linux



Zaczniemy od skonfigurowania Graylog. Do wykonania są trzy kroki:





- Utworzenie **Input** w celu stworzenia punktu wejścia umożliwiającego maszynom z systemem Linux **wysyłanie logów Syslog przez UDP**.
- Utworzenie nowego **Indeksu** do przechowywania i **indeksowania wszystkich logów Linuksa**.
- Utworzenie **strumienia** do **kierowania** logów odbieranych przez Graylog do nowego indeksu Linux.



#### A. Tworzenie danych wejściowych dla dziennika Syslog



Zaloguj się do Graylog Interface, kliknij "**System**" w menu, a następnie "**Inputs**". Z rozwijanej listy wybierz "**Syslog UDP**", a następnie kliknij przycisk "**Uruchom nowe wejście**". Możliwe jest również utworzenie wejścia TCP Syslog, ale wymaga to użycia certyfikatu TLS: plus dla bezpieczeństwa, ale nie omówiony w tym artykule.



![Image](assets/fr/001.webp)



Na ekranie pojawi się kreator. Zacznij od nadania temu wejściu nazwy, na przykład "**Graylog_UDP_Rsyslog_Linux**" i wybierz port. Domyślnie port to "**514**", ale można go dostosować. Tutaj wybrano port "**12514**".



![Image](assets/fr/016.webp)



Możesz także zaznaczyć opcję "**Store full message**", aby zapisać pełną wiadomość dziennika w Graylog. Kliknij na "**Launch Input**".



![Image](assets/fr/017.webp)



Nowe wejście zostało utworzone i jest teraz aktywne. Graylog może teraz odbierać logi Syslog na porcie 12514/UDP, ale nie zakończyliśmy jeszcze konfiguracji aplikacji.



![Image](assets/fr/018.webp)


**Uwaga: pojedynczy Input może być używany do przechowywania logów z kilku maszyn z systemem Linux.



#### B. Utwórz nowy indeks systemu Linux



Musimy utworzyć indeks w Graylog, aby przechowywać logi z maszyn z systemem Linux. Indeks** w Graylog to struktura przechowywania, która zawiera otrzymane logi, tj. otrzymane wiadomości. Graylog używa OpenSearch jako silnika pamięci masowej, a wiadomości są indeksowane, aby umożliwić szybkie i wydajne wyszukiwanie.



W programie Graylog kliknij "**System**" w menu, a następnie "**Indeksy**". Na nowo wyświetlonej stronie kliknij "**Utwórz zestaw indeksów**".



![Image](assets/fr/005.webp)



Nazwij ten indeks, na przykład "**Linux Index**", dodaj opis i prefiks przed potwierdzeniem. Tutaj będziemy **przechowywać wszystkie logi Linux w tym indeksie**. Możliwe jest również utworzenie określonych indeksów do przechowywania tylko niektórych dzienników (tylko dzienniki [SSH] (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/ "SSH"), dzienniki usług internetowych itp.)



![Image](assets/fr/006.webp)



Teraz musimy utworzyć nowy strumień, aby kierować wiadomości do tego indeksu.



#### C. Utwórz strumień



Aby utworzyć nowy strumień, kliknij "**Strumienie**" w menu głównym Graylog. Następnie kliknij przycisk "**Twórz strumień**" po prawej stronie. W wyświetlonym oknie nadaj nazwę strumieniowi, na przykład "**Linux Stream**" i wybierz indeks "**Linux Index**" w polu o nazwie "**Index Set**". Potwierdź swój wybór.



**Uwaga: wiadomości odpowiadające temu strumieniowi będą również zawarte w "**Default Stream**", chyba że zaznaczysz opcję "**Remove matches from 'Default Stream'**".



![Image](assets/fr/002.webp)



Następnie w ustawieniach Steam kliknij przycisk "**Dodaj regułę strumienia**", aby dodać nową regułę routingu wiadomości. Jeśli nie możesz znaleźć tego okna, kliknij "**Strumienie**" w menu, a następnie w wierszu odpowiadającym strumieniowi kliknij "**Więcej**", a następnie "**Zarządzaj regułami**".



Wybierz typ "**match input**" i wybierz wcześniej utworzone **wejście Rsyslog w UDP**. Potwierdź przyciskiem "**Utwórz regułę**". Wszystkie wiadomości do naszego nowego wejścia będą teraz wysyłane do Index for Linux.



![Image](assets/fr/003.webp)



Nowy Stream powinien pojawić się na liście i powinien być w stanie "**Running**". Przepustowość komunikatu pokazuje "**0 msg/s**", ponieważ obecnie nie wysyłamy żadnych dzienników do wejścia UDP Rsyslog. Aby wyświetlić dzienniki strumienia, wystarczy kliknąć jego nazwę.



![Image](assets/fr/004.webp)



**Wszystko jest gotowe po stronie Graylog**. Następnym krokiem jest skonfigurowanie maszyny z systemem Linux.



### III. Instalacja i konfiguracja Rsyslog w systemie Linux



Zaloguj się na komputerze z systemem Linux, lokalnie lub zdalnie, i użyj konta użytkownika z uprawnieniami do podniesienia jego uprawnień (poprzez sudo). W przeciwnym razie należy użyć bezpośrednio konta "root".



#### A. Instalacja pakietu Rsyslog



Zacznij od zaktualizowania pamięci podręcznej pakietów i zainstalowania pakietu o nazwie "**rsyslog**".



```
sudo apt-get update
sudo apt-get install rsyslog
```



Następnie sprawdź status usługi. W większości przypadków jest ona już uruchomiona.



```
sudo systemctl status rsyslog
```



#### B. Konfigurowanie Rsyslog



Rsyslog ma główny plik konfiguracyjny znajdujący się tutaj:



```
/etc/rsyslog.conf
```



Ponadto katalog "**/etc/rsyslog.d/**" służy do przechowywania dodatkowych plików konfiguracyjnych dla Rsyslog. W głównym pliku konfiguracyjnym znajduje się dyrektywa Include importująca wszystkie pliki "**.conf**" znajdujące się w tym katalogu. Umożliwia to posiadanie dodatkowych plików do konfiguracji Rsyslog bez modyfikowania głównego pliku.



W tym katalogu należy użyć numerów do zdefiniowania kolejności ładowania, ponieważ pliki są ładowane w kolejności alfabetycznej. Dodanie prefiksu numerycznego pozwala zarządzać priorytetem między kilkoma plikami konfiguracyjnymi. Tutaj mamy tylko jeden dodatkowy plik, więc nie stanowi to problemu.



W tym katalogu utworzymy plik o nazwie "**10-graylog.conf**":



```
sudo nano /etc/rsyslog.d/10-graylog.conf
```



W tym pliku wstaw ten wiersz:



```
*.* @192.168.10.220:12514;RSYSLOG_SyslogProtocol23Format
```



Oto jak interpretować tę linię:





- `*.*`: oznacza wysyłanie wszystkich dzienników Syslog z komputera z systemem Linux do Graylog.
- `@`: wskazuje, że transport jest wykonywany w UDP. Musisz podać "**@@**", aby przełączyć się na TCP.
- `192.168.10.220:12514`: wskazuje Address serwera Graylog i port, na który wysyłane są logi (odpowiadający Wejściu).
- `RSYSLOG_SyslogProtocol23Format`: odpowiada formatowi wiadomości wysyłanych do Graylog.



Po zakończeniu zapisz plik i uruchom ponownie Rsyslog.



```
sudo systemctl restart rsyslog.service
```



Po wykonaniu tej czynności na serwerze Graylog powinny pojawić się pierwsze wiadomości!



### IV. Wyświetlanie logów systemu Linux w Graylog



W Graylog możesz kliknąć na "**Streams**" i wybrać swój nowy stream, aby wyświetlić powiązane z nim wiadomości. Alternatywnie, kliknij "**Szukaj**", wybierz swój Steam i rozpocznij wyszukiwanie.



Oto kilka kluczowych cech Interface:



**1** - Wybór okresu wyświetlania wiadomości. Domyślnie wyświetlane są wiadomości z ostatnich 5 minut.



**2** - Wybór strumieni, które mają być wyświetlane.



**3** - Włącz automatyczne odświeżanie listy wiadomości (na przykład co 5 sekund). W przeciwnym razie będzie ona statyczna i trzeba będzie odświeżać ją ręcznie.



**4** - Kliknij lupę, aby uruchomić wyszukiwanie po zmodyfikowaniu okresu, strumienia lub filtra.



**5** - Pasek wprowadzania do określenia filtrów wyszukiwania. Tutaj określam "**source:srv\-docker**", aby wyświetlić tylko dzienniki nowej maszyny, na której właśnie skonfigurowałem Rsyslog.



Dzienniki są wysyłane przez maszynę z systemem Linux:



![Image](assets/fr/015.webp)



### V. Identyfikacja awarii połączenia SSH



Siła Graylog leży w jego zdolności do indeksowania dzienników i umożliwienia wyszukiwania według różnych kryteriów: maszyna źródłowa, Timestamp, treść wiadomości itp. Możemy chcieć zidentyfikować nieudane połączenia SSH.



Ze zdalnego komputera (na przykład serwera Graylog) spróbuj połączyć się z serwerem Linux, na którym właśnie skonfigurowałeś Rsyslog. Na przykład:



```
ssh [email protected]
```



Następnie celowo wprowadź nieprawidłową **nazwę użytkownika** i **hasło**, aby **wykryć błędy połączenia generate**. W pliku "**/var/log/auth.log**" spowoduje to wyświetlenie komunikatów dziennika generate podobnych do poniższych:



```
Failed password for invalid user it-connect from 192.168.10.199 port 50352 ssh2
```



Wiadomości te można znaleźć na Graylog.



W Graylog użyj następującego filtra wyszukiwania, aby wyświetlić tylko pasujące wiadomości:



```
message:Failed password AND application_name:sshd
```



Jeśli masz kilka serwerów i chcesz przeanalizować dzienniki określonego serwera, określ jego nazwę dodatkowo:



```
message:Failed password AND application_name:sshd AND source:srv\-docker
```



Oto przegląd wyników na maszynie, na której wygenerowałem kilka błędów połączenia o różnych porach dnia:



![Image](assets/fr/009.webp)



Nieudane próby połączenia są podejmowane z maszyny o adresie IP Address "**192.168.10.199**". Jeśli chcesz dowiedzieć się więcej o aktywności tego hosta, możesz **wyszukać ten adres IP Address**. Graylog wyświetli wszystkie dzienniki, w których znajduje się odniesienie do tego adresu IP Address, na wszystkich hostach (dla których skonfigurowano wysyłanie dzienników).



W takim przypadku używany filtr może być:



```
message:"192.168.10.199"
```



Otrzymujemy dodatkowe wyniki (co nie jest zaskakujące, ponieważ nie filtrujemy aplikacji SSH):



![Image](assets/fr/008.webp)



### VI. Wnioski



Postępując zgodnie z tym samouczkiem, powinieneś być w stanie skonfigurować maszynę z systemem Linux tak, aby wysyłała swoje dzienniki do serwera Graylog. W ten sposób będziesz mógł scentralizować logi swoich hostów Linux w swoim log sink!



Aby pójść jeszcze dalej, rozważ utworzenie pulpitów nawigacyjnych i alertów, aby otrzymywać powiadomienia o wykryciu anomalii.



![Image](assets/fr/007.webp)