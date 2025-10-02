---
name: RoninDojo v2
description: Instalacja węzła RoninDojo v2 Bitcoin na Raspberry Pi
---
![cover RoninDojo v2](assets/cover.webp)


**OSTRZEŻENIE:** Po aresztowaniu założycieli Samourai Wallet i zajęciu ich serwerów 24 kwietnia, niektóre funkcje RoninDojo, takie jak Whirlpool, przestały działać. Możliwe jest jednak, że narzędzia te zostaną przywrócone lub ponownie uruchomione w inny sposób w nadchodzących tygodniach. Ponadto, ponieważ kod RoninDojo był hostowany na GitLab Samourai, który również został przejęty, obecnie nie jest możliwe zdalne pobranie kodu. Zespoły RoninDojo prawdopodobnie pracują nad ponownym opublikowaniem kodu


uważnie śledzimy rozwój tej sprawy, a także rozwój związany z powiązanymi narzędziami. Zapewniamy, że będziemy aktualizować ten poradnik w miarę pojawiania się nowych informacji


ten samouczek służy wyłącznie celom edukacyjnym i informacyjnym. Nie popieramy ani nie zachęcamy do korzystania z tych narzędzi w celach przestępczych. Każdy użytkownik jest odpowiedzialny za przestrzeganie prawa obowiązującego w jego jurysdykcji


---

> Używaj Bitcoin z zachowaniem prywatności.

W poprzednim samouczku wyjaśniliśmy już procedurę instalacji i korzystania z RoninDojo v1. Jednak w ciągu ostatniego roku zespoły RoninDojo uruchomiły wersję 2 swojej implementacji, co stanowiło znaczący punkt zwrotny w architekturze oprogramowania. Rzeczywiście, odeszli od dystrybucji Linux Manjaro na rzecz Debiana. W związku z tym nie oferują już wstępnie skonfigurowanego obrazu do automatycznej instalacji na Raspberry Pi. Wciąż jednak istnieje metoda ręcznej instalacji. Tego właśnie użyłem dla mojego własnego węzła i od tego czasu RoninDojo v2 działa wspaniale na moim Raspberry Pi 4. Dlatego oferuję nowy samouczek dotyczący ręcznej instalacji RoninDojo v2 na Raspberry Pi.

https://planb.network/tutorials/node/bitcoin/ronin-dojo-31d96647-029b-43e8-9fb5-95ec5dde72b0

## Spis treści:


- Czym jest RoninDojo?
- Jaki sprzęt wybrać do instalacji RoninDojo v2?
- Jak złożyć Raspberry Pi 4?
- Jak zainstalować RoninDojo v2 na Raspberry Pi 4?
- Jak korzystać z węzła RoninDojo v2?


## Czym jest RoninDojo?

Dojo jest początkowo pełną implementacją węzła Bitcoin, opartą na Bitcoin Core i opracowaną przez zespoły Samourai Wallet. Rozwiązanie to można zainstalować na dowolnym sprzęcie. W przeciwieństwie do innych implementacji Core, Dojo zostało specjalnie zoptymalizowane do integracji ze środowiskiem aplikacji Android Samourai Wallet. Jeśli chodzi o RoninDojo, jest to narzędzie zaprojektowane w celu ułatwienia instalacji i zarządzania Dojo, a także różnymi innymi narzędziami uzupełniającymi. Krótko mówiąc, RoninDojo wzbogaca podstawową implementację Dojo poprzez integrację wielu dodatkowych narzędzi, jednocześnie upraszczając jego instalację i zarządzanie.


Ronin oferuje również [rozwiązanie node-in-box, zwane "*Tanto*"](https://ronindojo.io/en/products), urządzenie z RoninDojo już zainstalowanym w systemie zmontowanym przez ich zespół. Tanto jest płatną opcją, która może być interesująca dla tych, którzy wolą uniknąć komplikacji technicznych. Ponieważ jednak kod źródłowy RoninDojo jest otwarty, możliwe jest również wdrożenie go na własnym sprzęcie. Ta alternatywa, bardziej ekonomiczna, wymaga jednak pewnych dodatkowych manipulacji, które omówimy w tym samouczku.

RoninDojo jest Dojo, dzięki czemu pozwala na łatwą integrację Whirlpool CLI z węzłem Bitcoin, aby zapewnić najlepsze możliwe doświadczenie CoinJoin. Dzięki Whirlpool CLI możliwe staje się ciągłe remiksowanie bitcoinów, 24 godziny na dobę, 7 dni w tygodniu, bez konieczności włączania komputera osobistego.


Poza Whirlpool CLI, RoninDojo zawiera szereg narzędzi zwiększających funkcjonalność Dojo. Wśród nich kalkulator Boltzmanna analizuje poziom prywatności transakcji, serwer Electrum pozwala na połączenie portfeli Bitcoin z węzłem, a serwer Mempool umożliwia przeglądanie transakcji lokalnie, bez wycieku informacji.


W porównaniu do innych rozwiązań węzłowych, takich jak Umbrel, RoninDojo wyraźnie koncentruje się na rozwiązaniach On-Chain i narzędziach do ochrony prywatności. W przeciwieństwie do Umbrel, RoninDojo nie obsługuje konfiguracji węzła Lightning ani integracji bardziej ogólnych aplikacji serwerowych. Chociaż RoninDojo oferuje mniej wszechstronnych narzędzi niż Umbrel, posiada wszystkie niezbędne funkcje do zarządzania aktywnością On-Chain.


Jeśli nie potrzebujesz ogólnych funkcjonalności lub tych związanych z Lightning Network oferowanych przez Umbrel i szukasz prostego, stabilnego węzła z podstawowymi narzędziami, takimi jak Whirlpool lub Mempool, RoninDojo może być idealnym rozwiązaniem. Podczas gdy Umbrel ma tendencję do stawania się mini wielozadaniowym serwerem zorientowanym na Lightning Network i wszechstronność, RoninDojo, zgodnie z filozofią Samourai Wallet, koncentruje się na podstawowych narzędziach do ochrony prywatności użytkownika.


Teraz, gdy mamy już zarys RoninDojo, zobaczmy razem, jak skonfigurować ten węzeł.


## Jaki sprzęt wybrać do instalacji RoninDojo v2?

RoninDojo oferuje obraz do automatycznej instalacji swojego oprogramowania na [RockPro64](https://ronindojo.io/en/download). Nasz poradnik skupia się jednak na procedurze ręcznej instalacji na Raspberry Pi 4. Chociaż Raspberry Pi 5 zostało niedawno wprowadzone na rynek, a ten samouczek teoretycznie powinien być kompatybilny z tym nowym modelem, nie miałem jeszcze okazji przetestować go osobiście i nie znalazłem żadnych opinii od społeczności. Jak tylko zdobędę Pi 5 i kompatybilne z nim komponenty, zaktualizuję ten poradnik, by informować cię na bieżąco. W międzyczasie zalecam priorytetowe traktowanie Pi 4, ponieważ działa idealnie dla mojego węzła.

Ze swojej strony uruchamiam RoninDojo na Raspberry Pi wyposażonym w 8 GB pamięci RAM. Chociaż niektórym członkom społeczności udało się uruchomić go na urządzeniach z zaledwie 4 GB pamięci RAM, to sam nie testowałem takiej konfiguracji. Biorąc pod uwagę niewielką różnicę w cenie, rozsądne wydaje się wybranie wersji z 8 GB pamięci RAM. Może to również okazać się przydatne, jeśli planujesz zmienić przeznaczenie swojego Raspberry Pi do innych zastosowań w przyszłości.

Należy zauważyć, że zespoły RoninDojo zgłaszały częste problemy związane z obudową i adapterem SSD. Sam spotkałem się z tymi problemami. **Dlatego zdecydowanie zaleca się unikanie obudów wyposażonych w kabel USB do dysku SSD węzła. Zamiast tego należy wybrać kartę rozszerzeń pamięci zaprojektowaną specjalnie dla Raspberry Pi:**


![storage expansion card RPI4](assets/notext/1.webp)


Do przechowywania Bitcoin Blockchain potrzebny będzie dysk SSD kompatybilny z wybraną kartą rozszerzeń pamięci. Obecnie (luty 2024 r.) znajdujemy się w fazie przejściowej. Oczekuje się, że za kilka miesięcy dyski o pojemności 1 TB nie będą już wystarczające, aby pomieścić rosnący rozmiar Blockchain, zwłaszcza biorąc pod uwagę różne aplikacje, które planujesz zintegrować z węzłem. Dlatego niektórzy zalecają zainwestowanie w dysk SSD o pojemności 2 TB, aby zapewnić sobie spokój ducha w dłuższej perspektywie. Biorąc jednak pod uwagę tendencję spadkową cen dysków SSD z roku na rok, inni sugerują zadowolenie się dyskiem o pojemności 1 TB, który powinien wystarczyć na rok lub dwa lata, argumentując, że zanim stanie się on przestarzały, koszt modeli o pojemności 2 TB prawdopodobnie spadnie. Wybór zależy więc od osobistych preferencji użytkownika. Jeśli planujesz przechowywać swój RoninDojo przez dłuższy czas i chcesz uniknąć jakichkolwiek problemów technicznych w nadchodzących latach, opcja dysku SSD o pojemności 2 TB wydaje się być najrozsądniejsza, ponieważ oferuje wygodny margines na przyszłość.


Ponadto potrzebne będą różne małe komponenty:


- Obudowa wyposażona w wentylator do przechowywania Raspberry Pi i karty rozszerzeń pamięci masowej. Zestawy zawierające zarówno kartę rozszerzeń SSD, jak i kompatybilną obudowę są dostępne online;
- Kabel zasilający do Raspberry Pi;
- Karta micro SD o pojemności co najmniej 16 GB (choć technicznie wystarczy 8 GB, różnica w cenie między kartami 8 i 16 GB jest często znikoma);
- Kabel Ethernet RJ45 do połączenia sieciowego.


![node material](assets/notext/2.webp)


## Jak złożyć Raspberry Pi 4?

Montaż węzła będzie się różnić w zależności od wybranego sprzętu, a zwłaszcza typu obudowy. Jednak ogólny zarys kroków, które należy wykonać, pozostaje ogólnie podobny w montażu.

Zacznij od zainstalowania dysku SSD na karcie rozszerzeń pamięci masowej, uważając, aby zabezpieczyć dwie śruby blokujące z tyłu.


![assembly1](assets/notext/3.webp)


Następnie podłącz Raspberry Pi do karty rozszerzeń.


![assembly2](assets/notext/4.webp)


Podłącz również wentylator do Raspberry Pi.


![assembly3](assets/notext/5.webp)


Podłącz różne komponenty, zwracając uwagę na użycie prawidłowych pinów, odnosząc się do instrukcji obsługi obudowy. Producenci obudów często oferują samouczki wideo, które pomagają w montażu. W moim przypadku mam dodatkową kartę rozszerzeń wyposażoną w przycisk włączania/wyłączania. Nie jest to niezbędne do stworzenia węzła Bitcoin. Używam go głównie jako przycisku zasilania.


Jeśli, tak jak ja, masz kartę rozszerzeń wyposażoną w przycisk włączania/wyłączania, nie zapomnij zainstalować małej zworki "Auto Power On". Umożliwi to automatyczne uruchomienie węzła zaraz po jego włączeniu. Ta funkcja jest szczególnie przydatna w przypadku awarii zasilania, ponieważ umożliwia ponowne uruchomienie węzła bez ręcznej interwencji użytkownika.


![assembly4](assets/notext/6.webp)


Przed włożeniem całego sprzętu do obudowy ważne jest, aby sprawdzić prawidłowe działanie Raspberry Pi, karty rozszerzeń pamięci masowej i wentylatora, włączając je.


![assembly5](assets/notext/7.webp)


Na koniec zainstaluj Raspberry Pi w jego obudowie. Pamiętaj, że późniejszy krok będzie wymagał dodania karty micro SD do odpowiedniego portu w Raspberry Pi. Jeśli obudowa jest wyposażona w otwór, który umożliwia włożenie karty SD bez konieczności jej otwierania (tak jak w przypadku mojej obudowy pokazanej na zdjęciu), możesz teraz zamknąć obudowę. Jeśli jednak obudowa nie ma bezpośredniego dostępu do portu micro SD, przed sfinalizowaniem montażu należy poczekać na przygotowanie karty micro SD do włożenia.


![assembly6](assets/notext/8.webp)


## Jak zainstalować RoninDojo v2 na Raspberry Pi 4?


### Krok 1: Przygotowanie bootowalnej karty micro SD

Po złożeniu sprzętu, następnym krokiem jest instalacja RoninDojo. W tym celu przygotujemy bootowalną kartę micro SD z komputera, nagrywając na nią odpowiedni obraz dysku.

Będziesz musiał użyć oprogramowania _**Raspberry Pi Imager**_, zaprojektowanego w celu ułatwienia pobierania, konfigurowania i zapisywania systemów operacyjnych na karcie micro SD do użytku z Raspberry Pi. Zacznij od zainstalowania tego oprogramowania na komputerze osobistym:


- Dla Ubuntu/Debian: https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb
- Dla systemu Windows: https://downloads.raspberrypi.org/imager/imager_latest.exe
- Dla komputerów Mac: https://downloads.raspberrypi.org/imager/imager_latest.dmg


Po zainstalowaniu oprogramowania otwórz je i włóż kartę micro SD do komputera osobistego. Z poziomu Raspberry Pi Imager Interface wybierz `CHOOSE OS`:


![choose OS](assets/notext/9.webp)


Następnie przejdź do menu `Raspberry Pi OS (other)`:


![choose OS others](assets/notext/10.webp)


Wybierz system operacyjny o nazwie `Raspberry Pi OS (Legacy, 64-bit) Lite`, który ma rozmiar `0,3 GB`:


![choose OS Legacy Lite](assets/notext/11.webp)


Po wybraniu systemu operacyjnego nastąpi przekierowanie do menu głównego Raspberry Pi Imager. Kliknij na `CHOOSE STORAGE`:


![choose storage](assets/notext/12.webp)


Wybierz kartę micro SD:


![choose micro sd](assets/notext/13.webp)


Po wybraniu systemu operacyjnego i karty micro SD kliknij przycisk `NEXT`:


![choose next](assets/notext/14.webp)


Pojawi się nowe okno. Wybierz `EDYTUJ KONFIGURACJĘ`:


![edit settings](assets/notext/15.webp)


W tym oknie przejdź do zakładki `GENERAL` i wprowadź następujące ustawienia (które są bardzo ważne dla działania):


- Włącz opcję i przypisz `RoninDojo` jako nazwę hosta;
- Włącz `Ustaw nazwę użytkownika i hasło`, wprowadź `pi` jako nazwę użytkownika, wybierz hasło i zanotuj te informacje, ponieważ będą one potrzebne później. Te dane uwierzytelniające są tymczasowe i zostaną później usunięte;
- Wyłącz `Konfiguruj Wi-Fi`;
- Włącz opcję `Set locale settings` i wybierz strefę czasową oraz typ klawiatury odpowiadający Twojemu komputerowi;


![general settings](assets/notext/16.webp)


W zakładce USŁUGI kliknij pole `Włącz SSH` i wybierz `Użyj hasła do uwierzytelniania`:


![services settings](assets/notext/17.webp)


Upewnij się również, że w zakładce `OPTIONS` telemetria jest wyłączona:


![options settings](assets/notext/18.webp)


Kliknij przycisk `ZAPISZ`:


![settings save](assets/notext/19.webp)

Potwierdź, klikając `YES`, aby rozpocząć tworzenie bootowalnej karty micro SD:

![settings yes](assets/notext/20.webp)


Pojawi się komunikat informujący, że wszystkie dane na karcie micro SD zostaną usunięte. Potwierdź, klikając `YES`, aby rozpocząć proces:


![overwrite micro SD](assets/notext/21.webp)


Poczekaj, aż oprogramowanie zakończy przygotowywanie karty micro SD:


![writing micro SD](assets/notext/22.webp)


Po wyświetleniu komunikatu o zakończeniu procesu można wyjąć kartę micro SD z komputera:


![writing micro SD completed](assets/notext/23.webp)


### Krok 2: Zakończenie montażu węzła

Możesz teraz włożyć kartę micro SD do odpowiedniego portu Raspberry Pi.


![micro SD](assets/notext/24.webp)


Następnie podłącz Raspberry Pi do routera za pomocą kabla Ethernet. Na koniec włącz węzeł, podłączając kabel zasilający i naciskając przycisk zasilania (jeśli konfiguracja zawiera taki przycisk).


### Krok 3: Nawiązanie połączenia SSH z węzłem

Po pierwsze, konieczne jest znalezienie adresu IP Address węzła. Możesz użyć narzędzia takiego jak _[Advanced IP Scanner](https://www.advanced-ip-scanner.com/)_ lub _[Angry IP Scanner](https://angryip.org/)_ lub sprawdzić administracyjny Interface routera. Adres IP Address powinien mieć postać `192.168.1.??`. **Dla wszystkich poniższych poleceń, zastąp `[IP]` rzeczywistym IP Address węzła**, (usuwając nawiasy).


Uruchom terminal.


Aby usunąć możliwy klucz już powiązany z IP Address węzła, należy wykonać polecenie:

`ssh-keygen -R [IP]`.


Błąd po tym poleceniu nie jest poważny; oznacza to po prostu, że klucz nie istnieje na liście znanych hostów (co jest raczej prawdopodobne). Na przykład, jeśli adres IP węzła to `192.168.1.40`, polecenie staje się: `ssh-keygen -R 192.168.1.40`.


Następnie nawiąż połączenie SSH z węzłem, wykonując polecenie:

`ssh pi@[IP]`.

Pojawi się komunikat dotyczący autentyczności hosta: `Nie można ustalić autentyczności hosta '[IP]'. Wskazuje to, że autentyczność urządzenia, z którym próbujesz się połączyć, nie może zostać zweryfikowana z powodu braku znanego klucza publicznego. Podczas pierwszego połączenia przez SSH z nowym hostem, ten komunikat zawsze się pojawi. Musisz odpowiedzieć `tak`, aby dodać klucz publiczny do lokalnego katalogu, co zapobiegnie pojawianiu się tego komunikatu ostrzegawczego podczas przyszłych połączeń SSH z tym węzłem. Dlatego wpisz `yes` i naciśnij `enter`, aby zatwierdzić.

Następnie zostaniesz poproszony o wprowadzenie hasła, które wcześniej zostało ustawione jako tymczasowe w kroku 1. Zatwierdź przyciskiem `enter`. Nastąpi połączenie z węzłem przez SSH.


Podsumowując, oto polecenia do wykonania:


- `ssh-keygen -R [IP]`
- `ssh pi@[IP]`
- `tak`
- Wprowadź hasło tymczasowe i zatwierdź je.


### Krok 4: Aktualizacja i przygotowanie

Jesteś teraz połączony z węzłem za pośrednictwem sesji SSH. W terminalu wiersz polecenia powinien wyglądać następująco: `pi@RoninDojo:~ $`. Aby rozpocząć, zaktualizuj listę dostępnych pakietów i zainstaluj aktualizacje dla istniejących pakietów za pomocą następującego polecenia:

`sudo apt update && sudo apt upgrade -y`


Po zakończeniu aktualizacji, przejdź do instalacji *Git* i *Dialog* za pomocą polecenia:

`sudo apt install git dialog -y`


Następnie sklonuj gałąź `master` repozytorium _RoninOS_ Git, wykonując polecenie:

`sudo git clone --branch master https://code.samourai.io/ronindojo/RoninOS.git /opt/RoninOS`


Uruchom skrypt `customize-image.sh` za pomocą polecenia:

`cd /opt/RoninOS/ && sudo ./customize-image.sh`


**Ważne jest, aby pozwolić skryptowi działać bez przerwy i cierpliwie czekać na zakończenie jego procesu**, co zajmuje około 10 minut. Gdy pojawi się komunikat `Setup is complete`, możesz przejść do następnego kroku.


### Krok 5: Uruchomienie RoninOS

Uruchom system RoninOS za pomocą polecenia:

`sudo systemctl start ronin-setup`


Wyświetl linie pliku dziennika za pomocą polecenia:

`tail -f /home/ronindojo/.logs/setup.logs`


Na tym etapie **ważne jest, aby pozwolić RoninOS uruchomić się i poczekać, aż** zakończy działanie. Zajmuje to około 40 minut. Gdy pojawi się komunikat `All RoninDojo feature installations complete!`, możesz przejść do kroku 6.


### Krok 6: Uzyskanie dostępu do RoninUI i zmiana poświadczeń

Po zakończeniu instalacji, aby połączyć się z węzłem za pośrednictwem przeglądarki, upewnij się, że komputer osobisty jest podłączony do tej samej sieci lokalnej co węzeł. Jeśli używasz VPN na swoim komputerze, tymczasowo go wyłącz. Aby uzyskać dostęp do węzła Interface w przeglądarce, wpisz w pasku adresu URL:


- Bezpośrednio IP Address węzła, na przykład `192.168.1.??`;
- Lub wpisz `ronindojo.local`.


Po wejściu na stronę główną RoninUI zostaniesz poproszony o rozpoczęcie instalacji. Aby to zrobić, kliknij przycisk "Rozpocznij".


![lets start](assets/notext/25.webp)


Na tym etapie RoninUI przedstawia hasło `root`. Ważne jest, aby zachować je w bezpiecznym miejscu. Możesz zdecydować się na fizyczną kopię zapasową na papierze lub zapisać ją w [menedżerze haseł](https://planb.network/courses/99c46148-7080-4915-a7e0-9df0e145cd47/0b3c69b2-522c-56c8-9fb8-1562bd55930f).


![root password](assets/notext/26.webp)


Po zapisaniu hasła `root`, zaznacz pole `I have backed up Root user credentials` i kliknij `Continue`, aby kontynuować.


![confirm root password](assets/notext/27.webp)


Następnym krokiem jest utworzenie hasła użytkownika, które będzie używane zarówno do uzyskiwania dostępu do Interface RoninUI, jak i do nawiązywania sesji SSH z węzłem. Wybierz silne hasło i zapisz je w bezpieczny sposób. Będziesz musiał wprowadzić to hasło dwukrotnie przed kliknięciem `Finish` w celu zatwierdzenia. Jeśli chodzi o nazwę użytkownika, zaleca się zachowanie domyślnego wyboru, `ronindojo`. Jeśli zdecydujesz się ją zmienić, pamiętaj o odpowiednim dostosowaniu poleceń w kolejnych krokach.


![user credentials](assets/notext/28.webp)


Po wykonaniu tych czynności należy poczekać na zainicjowanie węzła. Następnie uzyskasz dostęp do RoninUI web Interface. Jesteś prawie na końcu procesu, pozostało tylko kilka małych kroków!

![Ronin UI](assets/notext/29.webp)


### Krok 7: Usuń tymczasowe dane uwierzytelniające

Otwórz nowy terminal na komputerze osobistym i nawiąż połączenie SSH z węzłem, używając następującego polecenia:

`SSH ronindojo@[IP]`


Jeśli na przykład adres IP Address węzła to `192.168.1.40`, odpowiednim poleceniem będzie:

`SSH ronindojo@192.168.1.40`


Jeśli zmieniłeś nazwę użytkownika podczas poprzedniego kroku, zastępując domyślną nazwę użytkownika (`ronindojo`) inną, upewnij się, że używasz tej nowej nazwy w poleceniu. Na przykład, jeśli wybrałeś `planb` jako nazwę użytkownika, a IP Address to `192.168.1.40`, polecenie do wprowadzenia będzie następujące:

`SSH planb@192.168.1.40`

Zostaniesz poproszony o wprowadzenie hasła użytkownika. Wprowadź je, a następnie naciśnij `enter`, aby zatwierdzić. Następnie uzyskasz dostęp do RoninCLI Interface. Użyj klawiszy strzałek na klawiaturze, aby przejść do opcji `Exit RoninDojo` i naciśnij `enter`, aby ją wybrać.

![RoninCLI](assets/notext/30.webp)


W tym momencie znajdujesz się w terminalu węzła, z wierszem polecenia podobnym do: `ronindojo@RoninDojo:~ $`. Aby usunąć tymczasowego użytkownika utworzonego podczas konfiguracji bootowalnej karty micro SD, wprowadź następujące polecenie i naciśnij `enter`:

`sudo deluser --remove-home pi`


Zostaniesz poproszony o potwierdzenie hasła użytkownika. Wprowadź je i potwierdź naciskając `enter`. Poczekaj na zakończenie operacji, a następnie użyj polecenia `exit`, aby opuścić terminal.


Gratulacje! Węzeł RoninDojo v2 jest teraz skonfigurowany i gotowy do użycia. Rozpocznie on IBD (*Initial Block Download*), kontynuując pobieranie i weryfikację Bitcoin Blockchain z bloku Genesis. Ten krok obejmuje pobranie wszystkich transakcji Bitcoin dokonanych od 3 stycznia 2009 r. i zajmuje trochę czasu. Po pełnym pobraniu Blockchain indeksator przystąpi do kompresji bazy danych. Czas trwania IBD może się znacznie różnić. Węzeł RoninDojo będzie w pełni operacyjny po zakończeniu tego procesu.


**Jeśli migrujesz ze starego węzła RoninDojo v1** do nowej wersji za pomocą tego samouczka, zachowując ten sam dysk SSD, węzeł powinien automatycznie wykryć i ponownie wykorzystać istniejące dane na dysku, oszczędzając ci konieczności ponownego wykonywania IBD. W takim przypadku wystarczy poczekać na ponowną synchronizację węzła z najnowszymi blokami.


### Krok 8: **veth** fix

Jeśli napotkasz błąd z RoninDojo v2 na Raspberry Pi, w którym po bezproblemowej instalacji węzeł nagle staje się nieosiągalny przez SSH, ale odzyskuje go po prostym ponownym uruchomieniu, musisz wykonać ten krok 8. Ten powszechny błąd można łatwo naprawić za pomocą rozwiązania opracowanego przez społeczność: "_veth fix_". Ta drobna poprawka trwale usuwa nagłe rozłączenia. Oto jak ją zastosować.


Otwórz nowy terminal na komputerze osobistym i nawiąż połączenie SSH z węzłem, używając następującego polecenia:

`SSH ronindojo@[IP]`


Jeśli na przykład adres IP Address węzła to `192.168.1.40`, odpowiednim poleceniem będzie:

`SSH ronindojo@192.168.1.40`


Zostaniesz poproszony o wprowadzenie hasła użytkownika. Wprowadź je i naciśnij `enter`, aby zatwierdzić. Następnie uzyskasz dostęp do RoninCLI Interface. Użyj strzałek klawiatury, aby przejść do opcji `Exit RoninDojo` i naciśnij `enter`, aby ją wybrać.


W tym momencie znajdujesz się w terminalu węzła, z wierszem polecenia podobnym do: `ronindojo@RoninDojo:~ $`. Aby zastosować poprawkę **veth**, wpisz następujące polecenie i naciśnij `enter`:

`sudo nano /etc/dhcpcd.conf`


Potwierdź ponownie hasło i naciśnij `enter`.


Dojdziesz do pliku `dhcpcd.conf`. Musisz skopiować poniższy tekst, upewniając się, że zawiera gwiazdkę, i dodać go na dole pliku:

`denyinterfaces veth*`


Aby to zrobić, przejdź do dolnej części pliku za pomocą strzałki w dół na klawiaturze, a następnie użyj prawego przycisku myszy, aby wkleić tekst w niezależnej linii.


Po dodaniu tekstu należy nacisnąć `ctrl X`, aby rozpocząć wyjście, a następnie `ctrl Y`, aby potwierdzić zapisanie zmian i nacisnąć `enter`, aby zakończyć i powrócić do wiersza poleceń. Aby upewnić się, że modyfikacja została poprawnie zastosowana, należy ponownie otworzyć plik `dhcpcd.conf` za pomocą odpowiedniego polecenia.


Aby zakończyć stosowanie poprawki, uruchom ponownie węzeł, wykonując polecenie:

`sudo reboot now`


W tym momencie można zamknąć terminal. Poczekaj niezbędny czas na ponowne uruchomienie RoninDojo, po czym powinieneś być w stanie ponownie połączyć się za pomocą graficznego Interface przeglądarki. Ten proces powinien naprawić napotkany błąd.


## Jak korzystać z węzła RoninDojo v2?


### Podłączanie oprogramowania Wallet do Electrs

Pierwszym zastosowaniem świeżo zainstalowanego i zsynchronizowanego węzła będzie rozgłaszanie transakcji do sieci Bitcoin. Prawdopodobnie będziesz chciał podłączyć różne portfele do węzła, aby poufnie transmitować swoje transakcje. Można to zrobić za pomocą Electrum Rust Server (electrs). Ta aplikacja jest zwykle wstępnie zainstalowana na węźle RoninDojo. Jeśli nie, możesz zainstalować ją ręcznie za pomocą RoninCLI Interface w `Applications > Manage Applications > Install Electrum Server`.


Aby uzyskać Tor Address serwera Electrum, z RoninUI web Interface, przejdź do:

`Parowanie > Serwer Electrum > Sparuj teraz`

![Pairing](assets/notext/31.webp)

![Electrs](assets/notext/32.webp)

Następnie należy wprowadzić `nazwę hosta` Address kończącą się na `.onion` w oprogramowaniu Wallet, wraz z portem `50001`. ![hostname](assets/notext/33.webp)

Na przykład w Sparrow Wallet wystarczy przejść do zakładki:

plik > Preferencje > Serwer > Prywatne Electrum`


![Sparrow](assets/notext/34.webp)


### Podłączanie oprogramowania Wallet do Samourai Dojo

Jako alternatywę dla korzystania z Electrs, Dojo umożliwia podłączenie kompatybilnego Software Wallet bezpośrednio do węzła RoninDojo. Portfele takie jak Samourai Wallet i Sentinel oferują tę funkcjonalność.


Aby nawiązać połączenie, wystarczy zeskanować kod QR swojego Dojo. Aby uzyskać dostęp do tego kodu QR za pośrednictwem RoninUI, przejdź do:

`Parowanie > Samourai Dojo > Sparuj teraz`

![Samourai Dojo](assets/notext/35.webp)

Aby połączyć Samourai Wallet z Dojo, wystarczy zeskanować ten kod QR podczas instalacji aplikacji:


![Samourai Wallet connection](assets/notext/36.webp)


Jeśli posiadałeś już Samourai Wallet przed skonfigurowaniem Ronin Dojo, konieczne jest wykonanie kopii zapasowej Wallet, odinstalowanie, a następnie ponowne zainstalowanie aplikacji Samourai Wallet przed przywróceniem Wallet. Po uruchomieniu ponownie zainstalowanej aplikacji będziesz mieć możliwość połączenia się z nowym Dojo. **Upewnij się, że masz kopię zapasową Samourai Wallet w swoich plikach i zweryfikuj ważność passphrase poprzez** `Ustawienia > Rozwiązywanie problemów > passphrase`. **Ważne jest również, aby mieć czytelną kopię zapasową frazy odzyskiwania i passphrase.** Aby uzyskać większą precyzję tej operacji, zaleca się skorzystanie z tego szczegółowego samouczka: [https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai](https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai).


### Korzystanie z własnego Mempool.space Block explorer

Block explorer przekształca surowe informacje z Bitcoin Blockchain w ustrukturyzowany i łatwy do odczytania format. Dzięki narzędziom takim jak *Mempool.space* możliwe jest analizowanie transakcji, wyszukiwanie określonych adresów, a nawet sprawdzanie średnich stawek opłat w mempoolach sieci w czasie rzeczywistym.


Jednak korzystanie z internetowych eksploratorów bloków stwarza ryzyko dla prywatności użytkownika i wiąże się z zaufaniem do danych dostarczanych przez strony trzecie. Rzeczywiście, korzystając z tych usług bez przechodzenia przez własny węzeł, możesz nieumyślnie ujawnić informacje o swoich transakcjach i musisz polegać na dokładności informacji przedstawionych przez właściciela witryny.

Aby ograniczyć to ryzyko, zaleca się korzystanie z własnej instancji *Mempool.space* za pośrednictwem sieci Tor, hostowanej bezpośrednio na węźle użytkownika. To rozwiązanie zapewnia zachowanie prywatności i autonomii danych.

Aby to zrobić, zacznij od zainstalowania *Mempool Space Visualizer* z RoninUI. W Interface przejdź do zakładki `Dashboard` i kliknij `Manage` poniżej `Mempool Space`:

`Pulpit nawigacyjny > Przestrzeń Mempool > Zarządzaj`

![Manage mempool](assets/notext/37.webp)

Następnie kliknij przycisk `Install Mempool visualizer`:

![install mempool](assets/notext/38.webp)

Potwierdź hasło użytkownika:

![password mempool](assets/notext/39.webp)

Poczekaj na zakończenie instalacji, a następnie ponownie kliknij przycisk `Zarządzaj`:

![Mempool Manage](assets/notext/40.webp)

Otrzymasz link `.onion`, aby uzyskać dostęp do własnej instancji *Mempool.space* za pośrednictwem sieci Tor.

![Mempool link](assets/notext/41.webp)

Radzę zapisać ten link w ulubionych w przeglądarce Tor lub dodać go do aplikacji Tor Browser na smartfonie, aby uzyskać łatwy i bezpieczny dostęp z dowolnego miejsca. Jeśli nie masz jeszcze przeglądarki Tor, możesz ją pobrać tutaj: [https://www.torproject.org/download/](https://www.torproject.org/download/)

![Mempool Tor](assets/notext/42.webp)


### Używanie Whirlpool do mieszania bitcoinów

Węzeł RoninDojo integruje również _WhirlpoolCLI_, Interface wiersza poleceń, który umożliwia automatyzację Whirlpool coinjoins, oraz _WhirlpoolGUI_, graficzny Interface zaprojektowany do interakcji z _WhirlpoolCLI_.


Wykonanie CoinJoin za pomocą Whirlpool wymaga, aby używana aplikacja była aktywna do wykonywania remiksów. Warunek ten może być restrykcyjny dla tych, którzy chcą osiągnąć wysoki poziom anonsów. Rzeczywiście, urządzenie obsługujące aplikację integrującą Whirlpool musi pozostawać włączone przez cały czas. Oznacza to, że aby uczestniczyć w remiksach przez 24 godziny na dobę, komputer lub smartfon musi pozostać włączony, a aplikacja Samourai lub Sparrow musi być stale otwarta. Rozwiązaniem tego ograniczenia jest użycie _WhirlpoolCLI_ na maszynie, która jest zawsze włączona, takiej jak węzeł Bitcoin, pozwalając monetom na remiksowanie bez przerwy i bez konieczności utrzymywania włączonego innego urządzenia.


W przygotowaniu jest szczegółowy samouczek, który poprowadzi cię krok po kroku przez proces łączenia z Samourai Wallet i RoninDojo v2, od A do Z.


Aby lepiej zrozumieć CoinJoin i jego użycie na Bitcoin, zapraszam również do zapoznania się z tym artykułem: Zrozumienie i używanie CoinJoin na Bitcoin, gdzie szczegółowo opisuję wszystko, co musisz wiedzieć o tej technice.




### Korzystanie z Whirlpool Stat Tool (WST)


Po wykonaniu coinjoinów za pomocą Whirlpool warto dokładnie ocenić poziom prywatności osiągnięty dla mieszanych UTXO. W tym celu można użyć narzędzia Python *Whirlpool Stat Tool*. Narzędzie to pozwala mierzyć zarówno prospektywne, jak i retrospektywne wyniki UTXO, jednocześnie analizując ich współczynnik dyfuzji w puli.


Aby pogłębić zrozumienie mechanizmów obliczeniowych tych indeksów, polecam przeczytanie artykułu: REMIX - Whirlpool, który szczegółowo opisuje działanie tych indeksów.


https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa



Aby uzyskać dostęp do narzędzia WST, przejdź do RoninCLI. Aby to zrobić, otwórz terminal na komputerze osobistym i nawiąż połączenie SSH z węzłem za pomocą następującego polecenia:

`SSH ronindojo@[IP]`


Jeśli na przykład adres IP Address węzła to `192.168.1.40`, odpowiednim poleceniem będzie:

`SSH ronindojo@192.168.1.40`


Jeśli zmieniłeś nazwę użytkownika podczas kroku 6, zastępując domyślną nazwę użytkownika (`ronindojo`) inną, upewnij się, że używasz tej nowej nazwy w poleceniu. Na przykład, jeśli wybrałeś `planb` jako swoją nazwę użytkownika, a IP Address to `192.168.1.40`, polecenie do wpisania brzmiałoby:

`SSH planb@192.168.1.40`


Zostaniesz poproszony o wprowadzenie hasła użytkownika. Wprowadź je i naciśnij `enter`, aby zatwierdzić. Następnie uzyskasz dostęp do RoninCLI Interface. Użyj klawiszy strzałek na klawiaturze, aby przejść do menu `Samourai Toolkit` i naciśnij `enter`, aby je wybrać:


![Samourai Toolkit](assets/notext/43.webp)


Następnie wybierz `Whirlpool Stat Tool`:


![WST](assets/notext/44.webp)


Po zainicjowaniu WST, narzędzie rozpocznie automatyczną instalację. Na tym etapie należy poczekać. Przewijane będą instrukcje użytkowania. Po zakończeniu instalacji naciśnij dowolny przycisk, aby uzyskać dostęp do terminala WST:


![WST commands](assets/notext/45.webp)


Wyświetlony zostanie następujący wiersz polecenia:

`wst#/tmp>`


Jeśli chcesz wyjść z tego Interface i powrócić do menu RoninCLI, po prostu wpisz :

`quit`


Po pierwsze, konieczne jest skonfigurowanie serwera proxy do korzystania z Tora, aby zapewnić poufność podczas wyodrębniania danych z OXT. Wpisz polecenie:

`socks5 127.0.0.1:9050`


Następnie przejdź do pobierania informacji o puli zawierających transakcję:

`download 0001`

Zastąp `0001` kodem nominału puli, którą jesteś zainteresowany. Kody nominałów są następujące na WST:


- Pula 0,5 bitcoina: `05`
- Pula 0.05 bitcoinów: `005`
- Pula 0,01 bitcoina: `001`
- Pula 0,001 bitcoinów: `0001`


Po pobraniu załaduj dane, zastępując `0001` kodem puli w tym poleceniu: `load 0001`


![WST loading](assets/notext/46.webp)


Poczekaj na zakończenie ładowania, co może potrwać kilka minut. Po załadowaniu danych, aby poznać wyniki anonset swojej monety, wykonaj polecenie `score`, a następnie txid (bez nawiasów):

`wynik [txid]`


![WST score](assets/notext/47.webp)


WST wyświetli następnie wynik retrospektywny (_Backward-looking metrics_), a następnie wynik prospektywny (_Forward-looking metrics_). Oprócz wyników anonset, WST wskaże również wskaźnik dyfuzji transakcji w puli, w stosunku do jej anonset.


**Ważne jest, aby pamiętać, że prospektywny wynik monety powinien być obliczany na podstawie txid początkowego miksu, a nie ostatniego miksu. I odwrotnie, retrospektywny wynik UTXO jest obliczany na podstawie txid z ostatniego cyklu**


### Korzystanie z kalkulatora Boltzmanna

Kalkulator Boltzmanna to narzędzie do analizy transakcji Bitcoin, oferujące możliwość pomiaru poziomu entropii wśród innych zaawansowanych wskaźników. Dane te zapewniają ilościową ocenę prywatności transakcji i pomagają zidentyfikować potencjalne wady. Narzędzie to jest już zintegrowane z węzłem RoninDojo, dzięki czemu jest łatwo dostępne i używane.


Przed szczegółowym opisaniem procedury korzystania z kalkulatora Boltzmanna ważne jest zrozumienie znaczenia tych wskaźników, metody ich obliczania i ich użyteczności. Chociaż wskaźniki te mają zastosowanie do każdej transakcji Bitcoin, są one szczególnie przydatne do oceny jakości transakcji CoinJoin.


**Pierwszym wskaźnikiem** obliczanym przez oprogramowanie jest całkowita liczba możliwych kombinacji, wskazana w narzędziu jako "kombinacjenb". W oparciu o wartości zaangażowanych UTXO, wskaźnik ten określa ilościowo liczbę sposobów, w jakie dane wejściowe mogą być powiązane z danymi wyjściowymi. Innymi słowy, określa on liczbę prawdopodobnych interpretacji, które transakcja może generate. Na przykład, CoinJoin skonstruowany zgodnie z modelem Whirlpool 5x5 przedstawia `1496` możliwych kombinacji:

![combinations](assets/notext/50.webp)

Kredyt: KYCP


**Drugim obliczanym wskaźnikiem** jest entropia transakcji, oznaczona jako `Entropy`. Gdy transakcja ma dużą liczbę możliwych kombinacji, często bardziej odpowiednie jest odniesienie się do jej entropii. Jest ona definiowana jako logarytm binarny liczby możliwych kombinacji. Oto zastosowany wzór:


- $E$: entropia transakcji;
- $C$: liczba możliwych kombinacji dla transakcji.

$$E = \log_2(C)$$


W matematyce logarytm binarny (logarytm o podstawie 2) odpowiada operacji odwrotnej do podnoszenia liczby 2 do potęgi. Innymi słowy, logarytm binarny $x$ jest wykładnikiem, do którego należy podnieść 2, aby otrzymać $x$. Dlatego wskaźnik ten jest wyrażony w bitach. Weźmy przykład obliczania entropii dla transakcji CoinJoin skonstruowanej zgodnie z modelem Whirlpool 5x5, który, jak wspomniano wcześniej, oferuje liczbę możliwych kombinacji `1496`:

$$ C = 1496 $$

$$ E = \log_2(1496) $$

$$ E około 10,5469 \text{bits}$$


Tak więc ta transakcja CoinJoin wykazuje entropię 10,5469 bitów, co jest uważane za bardzo zadowalające. Im wyższa jest ta wartość, tym więcej różnych interpretacji dopuszcza transakcja, zwiększając tym samym jej poziom prywatności.


Weźmy dodatkowy przykład z bardziej konwencjonalną transakcją, zawierającą jedno wejście i dwa wyjścia: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://Mempool.space/en/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce)

W przypadku tej transakcji, jedyną możliwą interpretacją jest: `(inp 0) > (Outp 0 ; Outp 1)`. W konsekwencji, jej entropia jest ustalona na `0`:

$$ C = 1 $$

$$ E = \log_2(1) $$

$$ E około 0 \text{bits}$$

**Trzeci wskaźnik** dostarczany przez kalkulator Boltzmanna nosi nazwę `Wallet Efficiency`. Wskaźnik ten ocenia wydajność transakcji poprzez porównanie jej z optymalną transakcją możliwą do pomyślenia w identycznej konfiguracji. Prowadzi nas to do omówienia koncepcji maksymalnej entropii, która odpowiada najwyższej entropii, jaką teoretycznie może osiągnąć określona struktura transakcji. Tak więc dla struktury Whirlpool 5x5 CoinJoin maksymalna entropia wynosi `10,5469`. Efektywność transakcji jest następnie obliczana poprzez skonfrontowanie tej maksymalnej entropii z rzeczywistą entropią analizowanej transakcji. Zastosowany wzór jest następujący:


- $ER$: rzeczywista entropia transakcji, wyrażona w bitach;
- $EM$: maksymalna możliwa entropia dla danej struktury transakcji, również w bitach;
- $Ef$: wydajność transakcji, w bitach.

$$Ef = ER - EM$$ $$Ef = 10.5469 - 10.5469$$

$$Ef = 0 \text{bits}$$


Wskaźnik ten jest również wyrażony w procentach, a jego formuła jest następująca:


- $CR$: liczba rzeczywistych możliwych kombinacji;
- $CM$: maksymalna liczba możliwych kombinacji o tej samej strukturze;
- $Ef$: wydajność wyrażona w procentach.

$$Ef = \frac{CR}{CM}$$

$$Ef = \frac{1496}{1496}$$

$$Ef = 100\%$$


Skuteczność na poziomie `100%` wskazuje zatem, że transakcja maksymalizuje swój potencjał prywatności w oparciu o jej strukturę.


**Czwarty wskaźnik**, gęstość entropii lub `Gęstość Entropii`, oferuje perspektywę entropii w stosunku do każdego wejścia lub wyjścia transakcji. Wskaźnik ten jest przydatny do oceny i porównywania wydajności transakcji o różnych rozmiarach. Aby go obliczyć, wystarczy podzielić całkowitą entropię transakcji przez całkowitą liczbę zaangażowanych wejść i wyjść. Na przykładzie Whirlpool 5x5 CoinJoin:


- $ED$: gęstość entropii wyrażona w bitach;
- $E$: entropia transakcji wyrażona w bitach;
- $T$: całkowita liczba wejść i wyjść w transakcji.

$$T = 5 + 5 = 10$$

$$ED = \frac{E}{T}$$

$$ED = \frac{10.5469}{10}$$

$$ED = 1,054 \text{bits}$$

**Piątą informacją** dostarczaną przez kalkulator Boltzmanna jest tabela prawdopodobieństw dopasowania między wejściami i wyjściami. Tabela ta wskazuje, poprzez "wynik Boltzmanna", prawdopodobieństwo, że określone wejście jest połączone z danym wyjściem. Biorąc za przykład Whirlpool CoinJoin, tabela prawdopodobieństwa podkreśli szanse na powiązanie każdego wejścia i wyjścia, zapewniając ilościową miarę niejednoznaczności lub przewidywalności powiązań w transakcji:


| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
|---------|----------|----------|----------|----------|----------|
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |


W tym przypadku jasne jest, że każde wejście ma równe szanse na powiązanie z dowolnym wyjściem, co wzmacnia niejednoznaczność i poufność transakcji. Jednak w przypadku prostej transakcji z jednym wejściem i dwoma wyjściami sytuacja wygląda inaczej:


| %       | Output 0 | Output 1 |
|---------|----------|----------|
| Input 0 | 100%     | 100%     |

Tutaj widzimy, że prawdopodobieństwo, że każde wyjście pochodzi z wejścia 0 wynosi 100%. Niższe prawdopodobieństwo przekłada się zatem na większą poufność poprzez rozmycie bezpośrednich powiązań między wejściami i wyjściami.


**Szóstą dostarczaną informacją** jest liczba deterministycznych powiązań, uzupełniona o stosunek tych powiązań. Wskaźnik ten ujawnia, ile połączeń między wejściami i wyjściami w analizowanej transakcji jest niepodważalnych, ze 100% prawdopodobieństwem. Stosunek ten z kolei oferuje perspektywę wagi tych deterministycznych powiązań w ramach wszystkich powiązań transakcji.


Na przykład transakcja Whirlpool typu CoinJoin nie ma deterministycznych powiązań, a zatem wyświetla wskaźnik i współczynnik 0%. Z drugiej strony, w naszej drugiej badanej transakcji (z jednym wejściem i dwoma wyjściami) wskaźnik jest ustawiony na 2, a współczynnik osiąga 100%. Tak więc wskaźnik zerowy sygnalizuje doskonałą poufność dzięki brakowi bezpośrednich i niepodważalnych powiązań między wejściami i wyjściami.


**Jak uzyskać dostęp do kalkulatora Boltzmanna na RoninDojo?**

Aby uzyskać dostęp do narzędzia *Boltzmann Calculator*, przejdź do RoninCLI. Aby to zrobić, otwórz terminal na komputerze osobistym i nawiąż połączenie SSH z węzłem za pomocą następującego polecenia: `SSH ronindojo@[IP]`


Jeśli na przykład adres IP węzła Address to `192.168.1.40`, odpowiednim poleceniem będzie:

`SSH ronindojo@192.168.1.40`


Jeśli zmieniłeś nazwę użytkownika podczas kroku 6, zastępując domyślną nazwę użytkownika (`ronindojo`) inną, upewnij się, że używasz tej nowej nazwy w poleceniu. Na przykład, jeśli wybrałeś `planb` jako swoją nazwę użytkownika, a IP Address to `192.168.1.40`, polecenie do wpisania brzmiałoby:

`SSH planb@192.168.1.40`


Zostaniesz poproszony o wprowadzenie hasła użytkownika. Wprowadź je, a następnie naciśnij `enter`, aby zatwierdzić. Następnie uzyskasz dostęp do RoninCLI Interface. Użyj strzałek na klawiaturze, aby przejść do menu `Samourai Toolkit` i naciśnij `enter`, aby je wybrać:


![Samourai Toolkit](assets/notext/43.webp)


Następnie wybierz `Kalkulator Boltzmanna`:


![boltzmann](assets/notext/49.webp)


Zostanie wyświetlona strona główna oprogramowania:


![boltzmann home](assets/notext/51.webp)


Wprowadź txid transakcji, którą chcesz przeanalizować i naciśnij klawisz `enter`:


![boltzmann txid](assets/notext/52.webp)


Następnie kalkulator udostępnia wszystkie wskaźniki, które omówiliśmy wcześniej:


![boltzmann result](assets/notext/53.webp)


### Inne funkcje RoninDojo v2

Twój węzeł RoninDojo integruje różne inne funkcje. W szczególności masz możliwość skanowania określonych informacji w celu ich uwzględnienia. Na przykład, czasami twój Samourai Wallet, podłączony do RoninDojo, może nie wyświetlać bitcoinów, które faktycznie posiadasz. Jeśli saldo wskazuje 0, podczas gdy jesteś pewien, że masz bitcoiny w tym Wallet, kilka powodów może wyjaśnić tę sytuację, takich jak błąd w ścieżkach derywacji. Ale jedną z przyczyn może być również to, że twój węzeł nie monitoruje prawidłowo twoich adresów. Aby rozwiązać ten problem, można upewnić się, że węzeł rzeczywiście śledzi `xpub` za pomocą narzędzia _xpub_. Aby uzyskać dostęp do tego narzędzia za pośrednictwem RoninUI, podążaj ścieżką:

`Konserwacja > Narzędzie XPUB`


Wprowadź `xpub`, który powoduje problem i kliknij przycisk `Check`, aby zweryfikować te informacje:

![xpub tool](assets/notext/54.webp)

Upewnij się, że wszystkie transakcje są prawidłowo wymienione. Ważne jest również, aby sprawdzić, czy używany typ derywacji odpowiada typowi Wallet. Jeśli tak nie jest, kliknij `Retype`, a następnie wybierz `BIP44`, `BIP49` lub `BIP84` w zależności od potrzeb.

Poza tym narzędziem, zakładka `Maintenance` w RoninUI jest pełna innych przydatnych funkcji:


- **Narzędzie transakcji**: Umożliwia sprawdzenie szczegółów danej transakcji;
- Narzędzie **Address**: Umożliwia potwierdzenie śledzenia danego Address przez Dojo;
- **Rescan Blocks**: Zmusza węzeł do wykonania nowego skanowania określonego zakresu bloków.


Zakładka `Push Tx` to kolejna interesująca funkcja RoninUI, która umożliwia rozgłaszanie podpisanej transakcji w sieci Bitcoin. Transakcja musi być wprowadzona w postaci szesnastkowej.


Jeśli chodzi o inne zakładki dostępne na pulpicie nawigacyjnym RoninUI:


- `Apps`: Hostuje aplikację Whirlpool i z pewnością będzie używana do integracji nowych aplikacji w przyszłości;
- `Logs`: Oferuje dostęp w czasie rzeczywistym do dzienników zdarzeń oprogramowania;
- `Informacje systemowe`: Zapewnia ogólne informacje o węźle, takie jak temperatura procesora, wykorzystanie przestrzeni dyskowej lub dane pamięci RAM. Znajdziesz tu również opcje `Reboot` i `Shut down` do ponownego uruchomienia lub wyłączenia węzła;
- `Ustawienia`: Umożliwia zmianę hasła użytkownika.


I gotowe! Dziękuję za przeczytanie tego poradnika do końca. Jeśli Ci się podobał, zachęcam do udostępnienia go w mediach społecznościowych. Ponadto, jeśli masz taką możliwość, rozważ wsparcie deweloperów, którzy udostępniają te darmowe i otwarte oprogramowanie naszej społeczności, przekazując darowiznę: [https://donate.ronindojo.io/](https://donate.ronindojo.io/). Aby pogłębić swoją wiedzę na temat RoninDojo i odkryć więcej zasobów, gorąco polecam zapoznanie się z linkami do zewnętrznych zasobów wymienionych poniżej.


**Zasoby zewnętrzne:**


- [https://ronindojo.io/index.html](https://ronindojo.io/index.html)
- [https://wiki.ronindojo.io/en/home](https://wiki.ronindojo.io/en/home)
- [https://gist.github.com/LaurentMT/e758767ca4038ac40aaf](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [https://medium.com/@laurentmt/introducing-boltzmann-85930984a159](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)
- [https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry](https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry)
