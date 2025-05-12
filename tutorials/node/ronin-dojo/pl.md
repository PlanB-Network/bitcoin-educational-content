---
name: RoninDojo

description: Instalowanie i używanie węzła RoninDojo Bitcoin.
---
***OSTRZEŻENIE:** Po aresztowaniu założycieli Samourai Wallet i zajęciu ich serwerów 24 kwietnia, niektóre funkcje RoninDojo, takie jak Whirlpool, przestały działać. Możliwe jest jednak, że narzędzia te zostaną przywrócone lub ponownie uruchomione w inny sposób w nadchodzących tygodniach. Ponadto, ponieważ kod RoninDojo był hostowany na GitLab Samourai, który również został przejęty, obecnie nie jest możliwe zdalne pobranie kodu. Zespoły RoninDojo prawdopodobnie pracują nad ponownym opublikowaniem kodu


uważnie śledzimy rozwój tej sprawy, a także rozwój związany z powiązanymi narzędziami. Zapewniamy, że będziemy aktualizować ten poradnik w miarę pojawiania się nowych informacji


ten samouczek służy wyłącznie celom edukacyjnym i informacyjnym. Nie popieramy ani nie zachęcamy do korzystania z tych narzędzi w celach przestępczych. Każdy użytkownik jest odpowiedzialny za przestrzeganie prawa obowiązującego w jego jurysdykcji


ten samouczek jest poświęcony instalacji RoninDojo v1. Aby skorzystać z najnowszych ulepszeń i funkcji, zdecydowanie zalecamy zapoznanie się z naszym samouczkiem poświęconym bezpośredniej instalacji RoninDojo v2 na Raspberry Pi:_

https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

---

Uruchomienie i korzystanie z własnego węzła jest niezbędne do prawdziwego uczestnictwa w sieci Bitcoin. Choć uruchomienie węzła Bitcoin nie przynosi użytkownikowi żadnych korzyści finansowych, pozwala mu zachować prywatność, działać niezależnie i mieć kontrolę nad zaufaniem do sieci.


W tym artykule przyjrzymy się szczegółowo RoninDojo, świetnemu rozwiązaniu do uruchamiania własnego węzła Bitcoin.


### Spis treści:



- Czym jest RoninDojo?
- Jaki sprzęt wybrać?
- Jak zainstalować RoninDojo?
- Jak korzystać z RoninDojo?
- Wnioski


Jeśli nie wiesz, jak działa węzeł Bitcoin i jaka jest jego rola, polecam zacząć od przeczytania tego artykułu: Węzeł Bitcoin - Część 1/2: Koncepcje techniczne.


![Samourai](assets/1.webp)


## Czym jest RoninDojo?


Dojo to pełny serwer Bitcoin opracowany przez zespół Samourai Wallet. Można go swobodnie zainstalować na dowolnej maszynie.


RoninDojo jest asystentem instalacji i narzędziem administracyjnym dla Dojo i różnych innych narzędzi. RoninDojo wykorzystuje oryginalną implementację Dojo i dodaje do niej wiele innych narzędzi, jednocześnie ułatwiając instalację i zarządzanie.


Oferują również sprzęt typu "plug-and-play", RoninDojo Tanto, z RoninDojo wstępnie zainstalowanym na maszynie zmontowanej przez ich zespół. Tanto to płatne rozwiązanie, odpowiednie dla tych, którzy nie chcą brudzić sobie rąk.


Kod RoninDojo jest open-source, więc możliwe jest również zainstalowanie tego rozwiązania na własnym sprzęcie. Ta opcja jest opłacalna, ale wymaga nieco więcej manipulacji, co zrobimy w tym artykule.


RoninDojo jest Dojo, więc pozwala na łatwą integrację Whirlpool CLI z węzłem Bitcoin, aby uzyskać jak najlepsze wrażenia z CoinJoin. Dzięki Whirlpool CLI nie tylko możesz pozwolić swoim bitcoinom na remiksowanie 24/7 bez konieczności utrzymywania włączonego komputera osobistego, ale możesz także znacznie poprawić swoją prywatność.


RoninDojo integruje wiele innych narzędzi, które polegają na Dojo, takich jak kalkulator Boltzmanna, który określa poziom prywatności transakcji, serwer Electrum do łączenia różnych portfeli Bitcoin z węzłem lub serwer Mempool do prywatnego obserwowania transakcji.

W porównaniu do innego rozwiązania węzłowego, takiego jak Umbrel, które przedstawiłem w tym artykule, RoninDojo jest głęboko skoncentrowany na rozwiązaniach i narzędziach "on chain", które optymalizują prywatność użytkowników. Dlatego RoninDojo nie pozwala na interakcję z Lightning Network.

RoninDojo oferuje mniej narzędzi w porównaniu do Umbrel, ale kilka niezbędnych funkcji dla Bitcoinera obecnych na Ronin jest niezwykle stabilnych.


Jeśli więc nie potrzebujesz wszystkich funkcji serwera Umbrel i chcesz tylko prostego i stabilnego węzła z kilkoma niezbędnymi narzędziami, takimi jak Whirlpool lub Mempool, RoninDojo jest prawdopodobnie dobrym rozwiązaniem dla Ciebie.


Moim zdaniem rozwój Umbrel koncentruje się głównie na Lightning Network i wszechstronnych narzędziach. Wciąż jest to węzeł Bitcoin, ale celem jest uczynienie z niego wielozadaniowego miniserwera. W przeciwieństwie do tego, rozwój RoninDojo jest bardziej dostosowany do zespołów Samourai Wallet i koncentruje się na podstawowych narzędziach dla Bitcoinera, pozwalając na pełną niezależność i zoptymalizowane zarządzanie prywatnością na Bitcoin.


Należy pamiętać, że konfiguracja węzła RoninDojo jest nieco bardziej złożona niż węzła Umbrel.


Teraz, gdy udało nam się namalować obraz RoninDojo, zobaczmy, jak skonfigurować ten węzeł razem.


## Jaki sprzęt wybrać?


Aby wybrać maszynę, która obsługuje i uruchamia RoninDojo, masz kilka opcji.


Jak wyjaśniono wcześniej, najprostszym wyborem jest zamówienie Tanto, maszyny typu plug-and-play zaprojektowanej specjalnie do tego celu. Aby zamówić swoją, przejdź tutaj: [link](https://shop.ronindojo.io/product-category/nodes/).


Ponieważ zespoły RoninDojo tworzą kod open-source, możliwe jest również wdrożenie RoninDojo na innych maszynach. Najnowsze wersje kreatora instalacji można znaleźć na tej stronie: [link](https://ronindojo.io/en/downloads.html), a najnowsze wersje kodu na tej stronie: [link](https://code.samourai.io/ronindojo/RoninDojo).


Osobiście zainstalowałem go na Raspberry Pi 4 8GB i wszystko działa idealnie.


Należy jednak pamiętać, że zespoły RoninDojo wskazują, że często występują problemy z obudową i adapterem SSD. Dlatego nie zaleca się używania obudowy z kablem do dysku SSD urządzenia. Zamiast tego lepiej jest użyć karty rozszerzeń pamięci masowej zaprojektowanej specjalnie dla płyty głównej, takiej jak ta: Raspberry Pi 4 Storage Expansion Card.


Oto przykład, jak skonfigurować własny węzeł RoninDojo:



- Raspberry Pi 4.
- Obudowa z wentylatorem.
- Kompatybilna karta rozszerzeń pamięci masowej.
- Kabel zasilający.
- Przemysłowa karta micro SD o pojemności co najmniej 16 GB.
- Dysk SSD o pojemności 1 TB lub większej.
- Kabel Ethernet RJ45, zalecana kategoria 8.


## Jak zainstalować RoninDojo?


### Krok 1: Przygotowanie bootowalnej karty micro SD.


Po złożeniu komputera można rozpocząć instalację RoninDojo. Aby to zrobić, zacznij od utworzenia bootowalnej karty micro SD, nagrywając na nią odpowiedni obraz dysku.


Włóż kartę micro SD do komputera osobistego, a następnie przejdź do oficjalnej strony RoninDojo, aby pobrać obraz dysku RoninOS: https://ronindojo.io/en/downloads.html.


Pobierz obraz dysku odpowiadający posiadanemu sprzętowi. W moim przypadku pobrałem obraz "MANJARO-ARM-RONINOS-RPI4-22.03.IMG.XZ":


![Download RoninOS disk image](assets/2.webp)


Po pobraniu obrazu należy zweryfikować jego integralność za pomocą odpowiedniego pliku .SHA256. W tym artykule opiszę szczegółowo, jak to zrobić: Jak zweryfikować integralność oprogramowania Bitcoin w systemie Windows?


Szczegółowe instrukcje dotyczące weryfikacji integralności systemu RoninOS są również dostępne na tej stronie: https://wiki.ronindojo.io/en/extras/verify.


Aby nagrać ten obraz na kartę micro SD, można użyć oprogramowania takiego jak Balena Etcher, które można pobrać tutaj: https://www.balena.io/etcher/.


Aby to zrobić, wybierz obraz w Etcher i sflashuj go na kartę micro SD:


![Burn disk image with Etcher](assets/3.webp)


Po zakończeniu operacji można włożyć bootowalną kartę micro SD do Raspberry Pi i włączyć urządzenie.


### Krok 2: Konfiguracja systemu RoninOS.


RoninOS to system operacyjny węzła RoninDojo. Jest to zmodyfikowana wersja Manjaro, dystrybucji Linuksa. Po uruchomieniu urządzenia i odczekaniu kilku minut można rozpocząć jego konfigurację.


Aby połączyć się z nim zdalnie, należy znaleźć adres IP Address urządzenia RoninDojo. Aby to zrobić, można na przykład połączyć się z panelem administracyjnym skrzynki internetowej lub pobrać oprogramowanie, takie jak https://angryip.org/, aby przeskanować sieć lokalną i znaleźć adres IP urządzenia.


Po znalezieniu adresu IP można przejąć kontrolę nad maszyną z innego komputera podłączonego do tej samej sieci lokalnej za pomocą SSH.


Z komputera z systemem macOS lub Linux wystarczy otworzyć terminal. Z komputera z systemem Windows można użyć specjalistycznego narzędzia, takiego jak Putty lub bezpośrednio Windows PowerShell.


Po otwarciu terminala wpisz następujące polecenie:

```
ssh root@192.168.?.?
```


Wystarczy zastąpić dwa znaki zapytania adresem IP wcześniej znalezionego RoninDojo.

Wskazówka: W powłoce kliknij prawym przyciskiem myszy, aby wkleić element.


Następnie przejdziesz do panelu sterowania Manjaro. Wybierz odpowiedni układ klawiatury za pomocą strzałek, aby zmienić cel na liście rozwijanej.


![Manjaro Keyboard Configuration](assets/4.webp)


Wybierz nazwę użytkownika i hasło dla swojej sesji. Użyj silnego hasła i wykonaj bezpieczną kopię zapasową. Możesz opcjonalnie użyć słabego hasła podczas instalacji, a później łatwo je zmienić, "kopiując-wklejając" je do RoninUI. Pozwoli to na użycie bardzo silnego hasła bez poświęcania zbyt wiele czasu na ręczne wpisywanie go podczas konfiguracji Manjaro.


![Manjaro Username Configuration](assets/5.webp)


Następnie zostaniesz poproszony o wybranie hasła głównego. W przypadku hasła roota wprowadź bezpośrednio silne hasło. Nie będzie można go zmienić z poziomu RoninUI. Należy również pamiętać o bezpiecznym utworzeniu kopii zapasowej hasła głównego.


Następnie wprowadź swoją lokalizację i strefę czasową.


![Manjaro Time Zone Configuration](assets/6.webp)


![Manjaro Location Configuration](assets/7.webp)


Następnie wybierz nazwę hosta.


![Manjaro Hostname Configuration](assets/8.webp)


Na koniec zweryfikuj informacje o konfiguracji Manjaro i potwierdź.


![Verification of ManjaroOS Configuration Information](assets/9.webp)


### Krok 3: Pobierz RoninDojo.


Zostanie przeprowadzona wstępna konfiguracja systemu RoninOS. Po zakończeniu, jak pokazano na powyższym zrzucie ekranu, urządzenie uruchomi się ponownie. Poczekaj kilka chwil, a następnie wprowadź następujące polecenie, aby ponownie połączyć się z maszyną RoninDojo:

```
ssh username@192.168.?.?
```


Wystarczy zastąpić "username" nazwą użytkownika, którą wcześniej wybrałeś, a znaki zapytania zastąpić adresem IP RoninDojo.


Następnie wprowadź hasło użytkownika.


W terminalu będzie to wyglądać następująco:


![SSH Connection to RoninOS](assets/10.webp)


Jesteś teraz połączony ze swoją maszyną, która obecnie ma tylko RoninOS. Teraz musisz zainstalować na nim RoninDojo.


Pobierz najnowszą wersję RoninDojo, wpisując następujące polecenie:

```
git clone https://code.samourai.io/ronindojo/RoninDojo
```


Pobieranie będzie szybkie. W terminalu zobaczysz to:


![Cloning RoninDojo](assets/11.webp)


Poczekaj na zakończenie pobierania, a następnie zainstaluj i uzyskaj dostęp do użytkownika Interface RoninDojo za pomocą następującego polecenia:

```
~/RoninDojo/ronin
```


Zostaniesz poproszony o wprowadzenie hasła użytkownika:


![Bitcoin Node Password Verification](assets/12.webp)


To polecenie jest konieczne tylko przy pierwszym dostępie do RoninDojo. Następnie, aby uzyskać dostęp do RoninCLI przez SSH, wystarczy wprowadzić polecenie [SSH username@192.168.?.?], zastępując "username" nazwą użytkownika i wprowadzając adres IP Address węzła. Zostaniesz poproszony o podanie hasła użytkownika.


Następnie zobaczysz tę wspaniałą animację:


![RoninCLI launch animation](assets/13.webp)


Następnie w końcu dotrzesz do RoninDojo CLI użytkownika Interface.


### Krok 4: Zainstaluj RoninDojo.


Z menu głównego przejdź do menu "System" za pomocą klawiszy strzałek na klawiaturze. Naciśnij klawisz Enter, aby potwierdzić wybór.


![RoninCLI navigation menu to System](assets/14.webp)


Następnie przejdź do menu "System Setup & Install".


![RoninCLI navigation menu to RoninDojo system installation](assets/15.webp)


Na koniec zaznacz "System Setup" i "Install RoninDojo" za pomocą spacji, a następnie wybierz "Accept", aby rozpocząć instalację.


![RoninDojo installation confirmation](assets/16.webp)


Instalacja powinna przebiegać spokojnie. W moim przypadku zajęło to około 2 godzin. Podczas procesu terminal powinien być otwarty.


Od czasu do czasu sprawdzaj terminal, ponieważ zostaniesz poproszony o naciśnięcie klawisza na niektórych etapach instalacji, na przykład tutaj:


![RoninDojo installation in progress](assets/17.webp)


Po zakończeniu instalacji zostaną uruchomione różne kontenery:


![Node container startup](assets/18.webp)


Następnie węzeł uruchomi się ponownie. Połącz się ponownie z RoninCLI, aby wykonać następny krok.


![Bitcoin node restart](assets/19.webp)


### Krok 5: Pobierz łańcuch Proof-of-Work i uzyskaj dostęp do RoninUI.


Po zakończeniu instalacji węzeł rozpocznie pobieranie łańcucha Bitcoin Proof-of-Work. Nazywa się to początkowym pobieraniem bloku (IBD). Zwykle trwa to od 2 do 14 dni, w zależności od połączenia internetowego i urządzenia.


Możesz śledzić postęp pobierania łańcucha, uzyskując dostęp do Interface RoninUI.


Aby uzyskać do niego dostęp z sieci lokalnej, wpisz następujące polecenie w pasku Address przeglądarki:



- Albo bezpośrednio wprowadź adres IP Address urządzenia (192.168.??)
- Lub wpisz: ronindojo.local


Pamiętaj, aby wyłączyć VPN, jeśli go używasz.


### Możliwy zwrot akcji


Jeśli nie możesz połączyć się z RoninUI z przeglądarki, sprawdź poprawność działania aplikacji z terminala podłączonego do węzła przez SSH. Połącz się z menu głównym, wykonując poprzednie kroki:



- Typ: SSH username@192.168.?... zastępując je swoimi danymi uwierzytelniającymi.



- Wprowadź hasło użytkownika.


W menu głównym przejdź do: **RoninUI > Restart**


Jeśli aplikacja uruchomi się ponownie poprawnie, oznacza to problem z połączeniem z przeglądarki. Sprawdź, czy nie korzystasz z VPN i upewnij się, że jesteś podłączony do tej samej sieci co węzeł.


Jeśli ponowne uruchomienie spowoduje błąd, spróbuj zaktualizować system operacyjny, a następnie ponownie zainstalować RoninUI. Aby zaktualizować system operacyjny: **System > Aktualizacje oprogramowania > Aktualizuj system operacyjny**


Po zakończeniu aktualizacji i restartu należy ponownie połączyć się z węzłem przez SSH i ponownie zainstalować RoninUI: **RoninUI > Re-install**


Po ponownym pobraniu RoninUI spróbuj połączyć się z RoninUI przez przeglądarkę.


**Wskazówka:** Jeśli przypadkowo opuścisz RoninCLI i znajdziesz się w terminalu Manjaro, po prostu wpisz polecenie "ronin", aby powrócić bezpośrednio do menu głównego RoninCLI.


### Logowanie internetowe


Możesz także zalogować się do RoninUI Interface z dowolnej sieci za pomocą Tor. Aby to zrobić, pobierz Tor Address swojego RoninUI z RoninCLI: **Poświadczenia > Ronin UI**


Pobierz Tor Address kończący się na .onion, a następnie zaloguj się do Ronin UI, wprowadzając ten Address w przeglądarce Tor. Należy uważać, aby nie ujawnić różnych danych uwierzytelniających, ponieważ są to poufne informacje.


![RoninUI web login interface](assets/20.webp)


Po zalogowaniu zostaniesz poproszony o podanie hasła użytkownika. Jest to to samo hasło, którego używasz do logowania się przez SSH.


![RoninUI web interface management panel](assets/21.webp)


Możemy zobaczyć postęp IBD (Initial Block Download) tutaj. Bądź cierpliwy, pobierasz wszystkie transakcje dokonane na Bitcoin od 3 stycznia 2009 roku.


Po pobraniu całego Blockchain indeksator skompaktuje bazę danych. Operacja ta trwa około 12 godzin. Możesz również śledzić jej postęp w sekcji "Indexer" w RoninUI.


Po wykonaniu tych czynności węzeł RoninDojo będzie w pełni funkcjonalny:


![Indexer synchronized at 100% functional node](assets/22.webp)


Jeśli chcesz zmienić hasło użytkownika na silniejsze, możesz to zrobić teraz z zakładki "Ustawienia". W RoninDojo nie ma dodatkowego zabezpieczenia Layer, więc zalecam wybranie naprawdę silnego hasła i zadbanie o jego kopię zapasową.


## Jak korzystać z RoninDojo?


Po pobraniu i skompaktowaniu łańcucha można zacząć korzystać z usług oferowanych przez nowy węzeł RoninDojo. Zobaczmy, jak z nich korzystać.


### Podłączanie oprogramowania Wallet do urządzeń elektrycznych.


Pierwszym zadaniem nowo zainstalowanego i zsynchronizowanego węzła będzie rozgłaszanie transakcji do sieci Bitcoin. Dlatego prawdopodobnie będziesz chciał podłączyć do niego różne oprogramowanie zarządzające Wallet.


Można to zrobić za pomocą Electrum Rust Server (electrs). Aplikacja jest zwykle wstępnie zainstalowana na węźle RoninDojo. Jeśli nie, możesz zainstalować ją ręcznie z RoninCLI Interface.


Wystarczy przejść do: **Aplikacje > Zarządzaj aplikacjami > Zainstaluj Electrum Server**


Aby uzyskać Tor Address serwera Electrum, z menu RoninCLI przejdź do:

**Credentials > Electrs**


Wystarczy wprowadzić link .onion w oprogramowaniu Wallet. Na przykład w Sparrow Wallet przejdź do zakładki:

**Plik > Preferencje > Serwer**


W typie serwera wybierz `Private Electrum`, a następnie wprowadź Tor Address swojego serwera Electrum w odpowiednim polu. Na koniec kliknij "Testuj połączenie", aby przetestować i zapisać połączenie.


![Sparrow Wallet connection interface to an electrs](assets/23.webp)


### Podłączenie oprogramowania Wallet do Samourai Dojo.


Zamiast używać Electrs, można również użyć Samourai Dojo, aby podłączyć kompatybilny Software Wallet do węzła RoninDojo. Na przykład Samourai Wallet oferuje tę opcję.


Aby to zrobić, wystarczy zeskanować kod QR połączenia z Dojo. Aby uzyskać do niego dostęp z RoninUI, kliknij zakładkę "Dashboard", a następnie przycisk "Manage" w polu Dojo. Będziesz wtedy mógł zobaczyć kody QR połączenia dla Dojo i BTC-RPC Explorer. Aby je wyświetlić, kliknij "Wyświetl wartości".


![Retrieving the connection QR code to Dojo](assets/24.webp)


Aby podłączyć Samourai Wallet do Dojo, należy zeskanować ten kod QR podczas instalacji aplikacji:


![Connecting to Dojo from the Samourai Wallet application](assets/25.webp)


### Korzystanie z własnego Mempool Explorer.


Niezbędne narzędzie dla Bitcoinerów, eksplorator pozwala sprawdzić różne informacje o łańcuchu Bitcoin. W przypadku Mempool można na przykład sprawdzić w czasie rzeczywistym opłaty stosowane przez innych użytkowników, aby odpowiednio dostosować swoje. Możesz również sprawdzić status potwierdzenia jednej ze swoich transakcji lub wyświetlić saldo Address.


Te narzędzia eksploracyjne mogą narazić użytkownika na ryzyko związane z prywatnością i wymagają zaufania do bazy danych strony trzeciej. Gdy korzystasz z tego narzędzia online bez przechodzenia przez własny węzeł:



- Istnieje ryzyko ujawnienia informacji o Wallet.



- Ufasz menedżerowi strony internetowej dla sieci Proof-of-Work, którą hostują.


Aby uniknąć tego ryzyka, można użyć własnej instancji Mempool na swoim węźle za pośrednictwem sieci Tor. Dzięki temu rozwiązaniu nie tylko zachowujesz prywatność podczas korzystania z usługi, ale także nie musisz już ufać dostawcy, ponieważ odpytujesz własną bazę danych.


Aby to zrobić, zacznij od zainstalowania Mempool Space Visualizer z RoninCLI:


**Aplikacje > Zarządzaj aplikacjami > Zainstaluj Mempool Space Visualizer**


Po zainstalowaniu, pobierz link do Mempool. Tor Address pozwoli na dostęp do niego z dowolnej sieci. Podobnie, pobieramy ten link za pośrednictwem RoninCLI:


**Poświadczenia > Mempool**


![Retrieve Tor Mempool address](assets/26.webp)


Wystarczy wpisać swój Tor Mempool Address w przeglądarce Tor, aby cieszyć się własną instancją Mempool, opartą na własnych danych. Zalecam dodanie tego Tor Address do ulubionych, aby uzyskać szybszy dostęp. Możesz również utworzyć skrót na pulpicie.


![Mempool Space interface](assets/27.webp)


Jeśli nie masz jeszcze przeglądarki Tor, możesz ją pobrać tutaj: https://www.torproject.org/download/


Można również uzyskać do niego dostęp ze smartfona, instalując przeglądarkę Tor Browser i wpisując ten sam Address. Z dowolnego miejsca można wyświetlić stan łańcucha Bitcoin przy użyciu własnego węzła.


### Korzystanie z Whirlpool CLI.


Węzeł RoninDojo zawiera również WhirlpoolCLI, zdalny wiersz poleceń Interface do automatyzacji miksów Whirlpool.


Podczas wykonywania CoinJoin z implementacją Whirlpool, używana aplikacja musi pozostać otwarta w celu wykonywania miksów i remiksów. Proces ten może być uciążliwy dla użytkowników, którzy chcą mieć wysokie zestawy anonimowe, ponieważ urządzenie obsługujące aplikację z Whirlpool musi być stale włączone. W praktyce oznacza to, że jeśli chcesz zaangażować swoje UTXO w remiksy 24/7, będziesz musiał stale mieć włączony komputer osobisty lub telefon z otwartą aplikacją.


Jednym z rozwiązań tego ograniczenia jest użycie WhirlpoolCLI na maszynie, która ma być stale włączona, takiej jak węzeł Bitcoin. Dzięki temu nasze UTXO mogą być remiksowane 24 godziny na dobę, 7 dni w tygodniu, bez konieczności utrzymywania innej maszyny niż nasz węzeł Bitcoin.

WhirlpoolCLI jest używane z WhirlpoolGUI, graficznym Interface do zainstalowania na komputerze osobistym w celu łatwego zarządzania Coinjoins. Wyjaśnię szczegółowo, jak skonfigurować Whirlpool CLI z własnym dojo w tym artykule: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=dans%20cette%20partie.-,Tutoriel%20%3A%20Whirpool%20CLI%20sur%20Dojo%20et%20Whirlpool%20GUI.,-Si%20vous%20souhaitez).


Aby dowiedzieć się więcej o CoinJoin w ogóle, wyjaśniam wszystko w tym artykule: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin).


### Korzystanie z Whirlpool Stat Tool.


Po wykonaniu CoinJoins z Whirlpool, możesz chcieć poznać rzeczywisty poziom prywatności swoich mieszanych UTXO. Whirlpool Stat Tool pozwala to łatwo zrobić. Za pomocą tego narzędzia można obliczyć wynik prospektywny i retrospektywny mieszanych UTXO. Aby dowiedzieć się więcej o obliczaniu tych zestawów Anon i ich działaniu, polecam przeczytanie tej sekcji: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment).


Narzędzie jest preinstalowane na RoninDojo. Na razie jest dostępne tylko z RoninCLI. Aby uruchomić je z menu głównego, przejdź do:

**Samourai Toolkit > Whirlpool Stat Tool**


Zostanie wyświetlona instrukcja obsługi. Po zakończeniu naciśnij dowolny klawisz, aby uzyskać dostęp do wiersza poleceń:


![Whirlpool Stats Tool software home](assets/28.webp)


Terminal wyświetli:

**wst#/tmp>**


Aby wyjść z tego Interface i powrócić do menu RoninCLI, wystarczy wprowadzić polecenie:

```
quit
```


Na początek ustawimy proxy na Torze, aby wyodrębnić dane OXT z zachowaniem pełnej prywatności. Wpisz polecenie:

```
socks5 127.0.0.1:9050
```


Następnie pobierz dane z puli zawierającej transakcję:

```
download 0001
```


**Uwaga:** zastąp `0001` kodem nominału puli, który Cię interesuje.


Kody nominałów są następujące na WST:



- Pula 0,5 bitcoina: 05
- Pula 0,05 bitcoina: 005
- Pula 0,01 bitcoina: 001
- Pula 0,001 bitcoinów: 0001


![Downloading data from pool 0001 from OXT](assets/29.webp)


Po pobraniu danych załaduj je za pomocą polecenia:

```
load 0001
```


**Uwaga:** zastąp `0001` kodem nominału puli, który Cię interesuje.


![Loading data from pool 0001](assets/30.webp)

Proces ładowania może potrwać kilka minut. Po załadowaniu danych wpisz komendę score, a następnie txid (identyfikator transakcji), aby uzyskać Anon Sets:

```
score TXID
```


**Uwaga:** zastąp `txid` identyfikatorem transakcji.


![Printing the prospective and retrospective scores of the given TXID](assets/31.webp)


WST wyświetli następnie wynik retrospektywny (metryki retrospektywne), a następnie wynik prospektywny (metryki prospektywne). Oprócz wyników zestawów anon, WST zapewnia również wskaźnik dyfuzji wyników w puli w oparciu o zestaw anon.


Należy pamiętać, że wynik prospektywny UTXO jest obliczany na podstawie txid początkowego miksu, a nie ostatniego miksu. I odwrotnie, retrospektywny wynik UTXO jest obliczany na podstawie txid z ostatniego cyklu.


Ponownie, jeśli nie rozumiesz tych koncepcji zestawów Anon, polecam przeczytanie tej części mojego artykułu na temat CoinJoin, w której wyjaśniam wszystko szczegółowo za pomocą diagramów: [https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment)


### Korzystanie z kalkulatora Boltzmanna.


Kalkulator Boltzmanna to narzędzie, które pozwala łatwo obliczyć różne zaawansowane wskaźniki transakcji Bitcoin, w tym jej poziom entropii. Wszystkie te dane pozwolą na ilościowe określenie poziomu prywatności transakcji i wykrycie wszelkich potencjalnych błędów. Narzędzie to jest preinstalowane na węźle RoninDojo.


Aby uzyskać do niego dostęp z RoninCLI, połącz się przez SSH, a następnie przejdź do menu:

**Samourai Toolkit > Kalkulator Boltzmanna**


Zanim wyjaśnię, jak korzystać z nich na RoninDojo, wyjaśnię, co reprezentują te metryki, jak są obliczane i do czego służą.


Wskaźniki te mogą być stosowane do każdej transakcji Bitcoin, ale są one szczególnie interesujące do badania jakości transakcji CoinJoin.


1. Pierwszym wskaźnikiem obliczanym przez to oprogramowanie jest liczba możliwych kombinacji. Jest on oznaczony w kalkulatorze jako "nb combinations". Biorąc pod uwagę wartości UTXO, wskaźnik ten reprezentuje liczbę możliwych mapowań z wejść na wyjścia.


**Uwaga:** jeśli nie jesteś zaznajomiony z terminem `UTXO`, polecam przeczytanie tego krótkiego artykułu:


> Mechanizm transakcji Bitcoin: UTXO, wejścia i wyjścia.

Innymi słowy, wskaźnik ten reprezentuje liczbę możliwych interpretacji dla danej transakcji. Na przykład struktura Whirlpool 5x5 CoinJoin będzie miała liczbę możliwych kombinacji równą 1496:


![Schema of a Coinjoin transaction on kycp.org](assets/32.webp)


Kredyt: KYCP


2. Drugim obliczanym wskaźnikiem jest entropia transakcji. Ponieważ liczba możliwych kombinacji może być bardzo wysoka dla transakcji, można zamiast tego użyć entropii. Entropia reprezentuje logarytm binarny liczby możliwych kombinacji. Jej wzór jest następujący:



- E: entropia transakcji.
- C: liczba możliwych kombinacji dla transakcji.


**E = log2(C)**


W matematyce logarytm binarny (podstawa 2) jest funkcją odwrotną do funkcji potęgi 2. Innymi słowy, logarytm binarny liczby x to potęga, do której należy podnieść liczbę 2, aby uzyskać wartość x.


Tak więc:


**E = log2(C)**


**C = 2^E**


Wskaźnik ten jest wyrażony w bitach. Dla przykładu, oto obliczenie entropii transakcji Whirlpool 5x5 CoinJoin, ze wspomnianą wcześniej liczbą możliwych kombinacji równą 1496:


**C = 1496**


**E = log2(1496)**


**E = 10,5469 bitów**


Dlatego ta transakcja CoinJoin ma entropię 10,5469 bitów, co jest bardzo dobrym wynikiem.


Im wyższy jest ten wskaźnik, tym więcej jest różnych interpretacji transakcji, a zatem tym bardziej poufna jest transakcja.


Weźmy inny przykład. Oto "klasyczna" transakcja, która ma jedno wejście i dwa wyjścia:


![Bitcoin transaction schema on oxt.me](assets/34.webp)


Kredyt: OXT


Transakcja ta ma tylko jedną możliwą interpretację:


**[(inp 0) > (Outp 0 ; Outp 1)]**


Zatem jego entropia będzie równa 0:


**C = 1**,

**E = log2(C)**,

**E = 0**


3. Trzecim wskaźnikiem zwracanym przez kalkulator Boltzmanna jest wydajność Tx o nazwie "Wallet Efficiency". Wskaźnik ten pozwala po prostu porównać transakcję wejściową z najlepszą możliwą transakcją w tej samej konfiguracji.


Wprowadzimy teraz pojęcie maksymalnej entropii, która reprezentuje najwyższą możliwą do osiągnięcia entropię dla danej struktury transakcji. Na przykład struktura Whirlpool 5x5 CoinJoin będzie miała maksymalną entropię wynoszącą 10,5469. Wskaźnik wydajności porównuje tę maksymalną entropię z rzeczywistą entropią transakcji wejściowej. Jego formuła jest następująca:



- ER: Rzeczywista entropia wyrażona w bitach.
- EM: Maksymalna entropia o tej samej strukturze wyrażona w bitach.
- Ef: Wydajność wyrażona w bitach.


**Ef = ER - EM**


**Ef = 10,5469 - 10,5469**


**Ef = 0 bitów**


Wskaźnik ten jest również wyrażony jako wartość procentowa, więc formuła staje się:



- CR: Rzeczywista liczba możliwych kombinacji.
- CM: Maksymalna liczba możliwych kombinacji o tej samej strukturze.
- Ef: Wydajność wyrażona w procentach.


**Ef = CR/CM**


**Ef = 1496/1496**


**Ef = 100%**


Skuteczność 100% oznacza, że ta transakcja ma najwyższą możliwą prywatność w stosunku do swojej struktury.


4. Czwartym obliczanym wskaźnikiem jest gęstość entropii. Pozwala nam ona odnieść entropię do każdego wejścia lub wyjścia. Wskaźnik ten można wykorzystać do porównania wydajności transakcji o różnych rozmiarach.


Jego obliczenie jest bardzo proste: dzielimy entropię transakcji przez liczbę obecnych wejść i wyjść. Na przykład, dla Whirlpool 5x5 CoinJoin, mielibyśmy:


ED: Gęstość entropii wyrażona w bitach.

E: entropia transakcji wyrażona w bitach.

T: Całkowita liczba wejść i wyjść w transakcji.


T = 5 + 5 = 10

ED = E / T

ED = 10,5469 / 10

ED = 1,054 bitów


Piątą informacją dostarczaną przez kalkulator Boltzmanna jest tabela prawdopodobieństwa powiązań między wejściami i wyjściami. Tabela ta podaje po prostu prawdopodobieństwo (wynik Boltzmanna), że dane wejście odpowiada danemu wyjściu.


Jeśli weźmiemy nasz przykład z Whirlpool CoinJoin, tabela prawdopodobieństwa będzie następująca:


| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
|---------|----------|----------|----------|----------|----------|
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |


Tutaj widzimy, że każde wejście ma równe prawdopodobieństwo powiązania z każdym wyjściem.


Jeśli jednak weźmiemy przykład transakcji z jednym wejściem i dwoma wyjściami, wyglądałoby to następująco:


| Input | Output 0 | Output 1 |
| ----- | -------- | -------- |
| 0     | 100%     | 100%     |

W tym przykładzie widzimy, że prawdopodobieństwo każdego wyjścia pochodzącego z wejścia 0 wynosi 100%.


Im niższe prawdopodobieństwo, tym wyższy poziom poufności.


6. Szóstą obliczaną informacją jest liczba deterministycznych linków. Podany zostanie również współczynnik deterministycznych powiązań. Wskaźnik ten podkreśla liczbę powiązań między wejściami i wyjściami danej transakcji, które mają prawdopodobieństwo 100%, co oznacza, że są niezaprzeczalne.


Współczynnik wskazuje liczbę deterministycznych połączeń w transakcji w porównaniu do całkowitej liczby połączeń.


Na przykład transakcja CoinJoin Whirlpool nie ma deterministycznych powiązań między wejściami i wyjściami. Wskaźnik wyniesie zero, a współczynnik również 0%.


Jednak w przypadku drugiej badanej transakcji (1 wejście i 2 wyjścia) wskaźnik wynosi 2, a współczynnik 100%.


Dlatego też, jeśli wskaźnik ten wynosi zero, oznacza to dobrą poufność.


Teraz, gdy zapoznaliśmy się ze wskaźnikami, zobaczmy, jak je obliczyć za pomocą tego oprogramowania. Z RoninCLI przejdź do menu:

**Samourai Toolkit > Kalkulator Boltzmanna**


![Boltzmann Calculator software homepage](assets/35.webp)


Po uruchomieniu oprogramowania wprowadź numer transaction ID, który chcesz przeanalizować. Można wprowadzić wiele transakcji jednocześnie, oddzielając je przecinkiem, a następnie nacisnąć klawisz Enter:


![Enter a TXID to study on Boltzmann Calculator](assets/36.webp)


Kalkulator zwróci wtedy wszystkie wskaźniki, które widzieliśmy wcześniej:


![Printing of Boltzmann Calculator data for this TXID](assets/37.webp)


Wpisz polecenie "Quit", aby zamknąć oprogramowanie i powrócić do menu RoninCLI.


Aby dowiedzieć się więcej o kalkulatorze Boltzmanna, polecam przeczytać te artykuły:



- https://medium.com/@laurentmt/introducing-boltzmann-85930984a159



- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf


### Podłączanie Bisq.


Bisq to platforma peer-to-peer Exchange, która umożliwia kupowanie i sprzedawanie bitcoinów. Jest używana z oprogramowaniem komputerowym, które działa na Torze i pozwala na Exchange bitcoinów bez konieczności podawania swojej tożsamości.

Bisq zabezpiecza wymiany peer-to-peer poprzez system wielopodpisowy 2/2. Możesz używać tego oprogramowania z własnym węzłem RoninDojo, aby zoptymalizować prywatność swoich wymian i zaufać danym z Blockchain własnego węzła.


Aby pobrać oprogramowanie Bisq, odwiedź ich oficjalną stronę internetową: https://bisq.network/


Aby rozpocząć pracę z oprogramowaniem, zalecam przeczytanie tej strony: https://bisq.network/getting-started/


Aby pobrać link połączenia z RoninDojo, musisz połączyć się z RoninCLI przez SSH. Następnie przejdź do menu:

**Aplikacje > Zarządzaj aplikacjami**


Wprowadź hasło, a następnie zaznacz pole klawiszem spacji:

**[ ] Włącz połączenie Bisq**


Potwierdź swój wybór. Pozwól zainstalować węzeł, a następnie pobierz Tor V3 Address z:

**Poświadczenia > bitcoind**


Skopiuj Address pod "Bitcoin daemon".


Można również pobrać bitcoind Tor V3 Address z RoninUI Interface, klikając "Zarządzaj" w polu "Bitcoin Core" na "Pulpicie nawigacyjnym":


![Retrieve TorV3 Bitcoin Daemon address on RoninUI](assets/38.webp)


Aby połączyć węzeł z Bisq, przejdź do menu:

**Ustawienia > Informacje o sieci**


![Access the node connection interface from the Bisq software](assets/39.webp)


Kliknij dymek "Użyj niestandardowych węzłów Bitcoin Core". Następnie wprowadź Bitcoin TorV3 Address w wyznaczonym polu, z ".onion", ale bez "http://".


![Box to enter the TorV3 address of your node in the Bisq software](assets/40.webp)


Uruchom ponownie oprogramowanie Bisq. Węzeł jest teraz połączony z Bisq.


### Inne funkcje.


Węzeł RoninDojo zawiera również inne podstawowe funkcje. Masz możliwość skanowania określonych informacji, aby upewnić się, że są one brane pod uwagę.


Na przykład czasami może się zdarzyć, że Wallet podłączony do RoninDojo nie znajdzie bitcoinów należących do użytkownika. Saldo wynosi 0, mimo że jesteś pewien, że masz Bitcoin w tym Wallet. Istnieje wiele możliwych przyczyn do rozważenia, w tym błąd w ścieżkach derywacji, a wśród nich możliwe jest również, że węzeł nie obserwuje twoich adresów.


Aby to naprawić, możesz sprawdzić, czy węzeł śledzi xpub za pomocą "narzędzia xpub". Aby uzyskać do niego dostęp z RoninUI, przejdź do menu:

**Konserwacja > Narzędzie XPUB**


Wprowadź problematyczny xpub i kliknij "Sprawdź", aby zweryfikować te informacje.


![XPUB Tool from RoninUI](assets/41.webp)


Jeśli xpub jest śledzony przez węzeł, pojawi się ten komunikat:


![XPUB Tool result showing successful analysis](assets/42.webp)


Sprawdź, czy wszystkie transakcje są wyświetlane prawidłowo. Sprawdź również, czy typ derywacji odpowiada typowi Wallet. Tutaj widzimy, że węzeł interpretuje ten xpub jako pochodną BIP44. Jeśli ten typ derywacji nie pasuje do typu Wallet, kliknij przycisk "Retype", a następnie wybierz BIP44/BIP49/BIP84 zgodnie z wyborem:


![Change the derivation type of the studied xpub from RoninUI](assets/43.webp)


Jeśli twój xpub nie jest śledzony przez twój węzeł, zobaczysz ten ekran z zaproszeniem do zaimportowania go:


![Import an xpub with XPUB Tool on RoninUI](assets/44.webp)


Można również korzystać z innych narzędzi konserwacyjnych:



- Narzędzie transakcji: Pozwala obserwować szczegóły konkretnej transakcji.
- Narzędzie Address: Umożliwia sprawdzenie, czy określony Address jest śledzony przez Dojo.
- Rescan Blocks: Zmusza węzeł do ponownego przeskanowania wybranego zakresu bloków.


W RoninUI można również znaleźć narzędzie "Push Tx". Pozwala ono na wysłanie podpisanej transakcji do sieci Bitcoin. Musi ona zostać wprowadzona w formacie szesnastkowym:


![Tool for broadcasting a signed transaction from RoninUI](assets/45.webp)


## Wnioski.


Widzieliśmy, jak zainstalować i rozpocząć pracę z tym wspaniałym narzędziem, jakim jest RoninDojo. Jest to doskonały wybór do uruchomienia własnego węzła Bitcoin. Jest to stabilne rozwiązanie, które integruje i aktualizuje wszystkie niezbędne narzędzia dla Bitcoinera.


Jeśli korzystanie z terminala cię nie przeraża i nie potrzebujesz narzędzi związanych z Lightning Network, to RoninDojo może ci się spodobać.


Jeśli możesz, rozważ przekazanie darowizny na rzecz deweloperów, którzy za darmo tworzą dla Ciebie to oprogramowanie open-source: https://donate.ronindojo.io/


Aby dowiedzieć się więcej o RoninDojo, polecam sprawdzić linki w moich zasobach zewnętrznych poniżej.


### Więcej informacji:



- Zrozumienie i używanie CoinJoin na Bitcoin.
- Funkcje Hash - fragment ebooka Bitcoin Démocratisé 1.
- Wszystko, co musisz wiedzieć o Bitcoin passphrase.


### Zasoby zewnętrzne:



- https://ronindojo.io/index.html
- https://wiki.ronindojo.io/en/home
- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf
- https://medium.com/@laurentmt/introducing-boltzmann-85930984a159
- https://en.wikipedia.org/wiki/Boltzmann_formula
- https://wiki.ronindojo.io/en/setup/bisq
- https://bisq.network/