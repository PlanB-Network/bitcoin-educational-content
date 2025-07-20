---
name: Electrum

description: Pełny przewodnik po Electrum, od 0 do bohatera
---

![cover](assets/cover.webp)


Poniżej znajduje się kilka źródeł opisu Electrum:



- [X](https://twitter.com/ElectrumWallet)
- [Strona internetowa Electrum](https://electrum.org/)
- [Dokumentacja Electrum](https://electrum.readthedocs.io/)


Oto co Rogzy sądzi o tym samouczku:


> Muszę przyznać, że kiedy natknąłem się na ten poradnik, byłem w szoku. Gratulacje dla Armana the Parman za to. Byłoby wstyd nie hostować go tutaj i przetłumaczyć na jak najwięcej języków. Szczerze mówiąc, porady tego kolesia.

Oryginalne posty są następujące:


![Electrum Desktop Wallet (Mac / Linux) - download, verify, connect to your node.](https://youtu.be/wHmQNcRWdHM)


![Making a Bitcoin transaction with Electrum](https://youtu.be/-d_Zd7VcAfQ)


## Dlaczego Electrum?


Jest to szczegółowy przewodnik po tym, jak korzystać z Electrum Bitcoin Wallet, z rozwiązaniami wszystkich jego pułapek i dziwactw - coś, co opracowałem po kilku latach użytkowania i nauczania studentów o bezpieczeństwie / prywatności Bitcoin. Electrum nie jest najlepszym Bitcoin Wallet dla osoby, która chce, aby wszystko było tak proste, jak to tylko możliwe i woli pozostać na poziomie początkującym. Zamiast tego jest dla osoby, która jest lub aspiruje do bycia "potężnym" użytkownikiem.


Dla nowego Bitcoinera jest to doskonałe rozwiązanie tylko pod nadzorem doświadczonego użytkownika, który wskaże mu drogę. Jeśli uczą się korzystać z niego samodzielnie, byłoby to bezpieczne, pod warunkiem, że nie spieszą się i używają go w środowisku testowym z niewielką liczbą Sats na początku. Niniejszy przewodnik wspiera to przedsięwzięcie, ale jest również dobrym źródłem informacji dla każdego innego użytkownika.


**Ostrzeżenie:** Ten poradnik jest obszerny. Nie próbuj zrobić tego wszystkiego w jeden dzień. Najlepiej zapisać poradnik i odrabiać go z czasem.


## Pobieranie Electrum


Idealnie byłoby używać dedykowanego komputera Bitcoin do transakcji Bitcoin (mój przewodnik na ten temat https://armantheparman.com/mint/) _(dostępny również w sekcji prywatności)_. Dobrze jest ćwiczyć z małymi kwotami na "brudnym" komputerze, gdy dopiero się uczysz (kto wie, ile ukrytego złośliwego oprogramowania zgromadził twój zwykły komputer przez lata - nie chcesz narażać na nie swoich portfeli Bitcoin).


Pobierz Electrum ze strony https://electrum.org/.


Kliknij kartę Pobierz u góry.


Kliknij łącze pobierania odpowiadające Twojemu komputerowi. Każdy komputer z systemem Linux lub Mac może użyć łącza Python (czerwone kółko). Komputer z systemem Linux i układem Intel lub AMD może korzystać z Appimage (kółko Green; jest to plik wykonywalny systemu Windows). Urządzenie Raspberry Pi ma mikroprocesor ARM i może używać tylko wersji Python (czerwone kółko), a nie Appimage, mimo że Pi działa pod Linuksem. Niebieskie kółko jest przeznaczone dla systemu Windows, a czarne dla komputerów Mac.


![image](assets/1.webp)


## Weryfikacja Electrum


Celem "weryfikacji" pobierania jest upewnienie się, że żaden bit danych nie został naruszony. Zapobiega to użyciu "zhakowanej" złośliwej wersji oprogramowania. Można to pominąć, pod warunkiem, że pobrana kopia jest używana wyłącznie do celów praktycznych, tj. nie korzysta się z portfeli przechowujących poważne pieniądze. Następnie, gdy będziesz gotowy do korzystania z Electrum dla swoich prawdziwych funduszy, powinieneś usunąć swoją kopię i zacząć od nowa, tym razem weryfikując pobieranie.


Aby to zrobić, używamy narzędzi kryptograficznych klucza publicznego/prywatnego - gpg, o których napisaliśmy przewodnik tutaj (https://armantheparman.com/gpg/). Narzędzie gpg jest dostarczane ze wszystkimi systemami operacyjnymi Linux. W przypadku systemów Mac i Windows instrukcje pobierania można znaleźć pod linkiem gpg.


Oprócz pobrania oprogramowania Electrum, dla bezpieczeństwa potrzebny jest również cyfrowy PODPIS oprogramowania. Jest to ciąg tekstu (w rzeczywistości jest to liczba zakodowana za pomocą tekstu), który programista utworzył za pomocą swojego PRYWATNEGO klucza gpg. Korzystając z programu gpg, możemy następnie "przetestować" SYGNATURĘ pod kątem jego klucza PUBLICZNEGO (utworzonego z klucza prywatnego dewelopera), do którego każdy ma dostęp, w porównaniu z plikiem do pobrania.


Innymi słowy, z trzema danymi wejściowymi (podpis, klucz publiczny i plik danych) otrzymujemy prawdziwy lub fałszywy wynik, aby potwierdzić, że plik nie został naruszony.


Aby uzyskać podpis, kliknij łącze odpowiadające pobranemu plikowi (patrz kolorowe strzałki):


![image](assets/2.webp)


Kliknięcie łącza może spowodować automatyczne pobranie pliku do folderu pobierania lub jego otwarcie w przeglądarce. Jeśli plik zostanie otwarty w przeglądarce, należy go zapisać. Możesz kliknąć prawym przyciskiem myszy i wybrać opcję "zapisz jako". W zależności od systemu operacyjnego lub przeglądarki może być konieczne kliknięcie prawym przyciskiem myszy obszaru białej przestrzeni, a nie tekstu.


Poniżej znajduje się wygląd pobranego tekstu. Widać, że istnieje wiele podpisów - są to podpisy różnych osób. Możesz zweryfikować każdy z nich. Pokażę ci, jak zweryfikować tylko dewelopera.


![image](assets/3.webp)


Następnie musisz uzyskać klucz publiczny ThomasaV - jest on głównym deweloperem. Można go uzyskać bezpośrednio od niego, z jego konta Keybase, Github lub od kogoś innego, z serwera kluczy lub ze strony Electrum.


Pobranie go ze strony Electrum jest w rzeczywistości najmniej bezpiecznym sposobem, ponieważ jeśli ta strona jest nieuczciwa (właśnie to sprawdzamy), dlaczego otrzymujemy od niej klucz publiczny (klucz publiczny może być fałszywy)?


Aby zachować prostotę na razie, pokażę ci, jak pobrać go ze strony internetowej, ale pamiętaj o tym. Oto kopia (https://github.com/spesmilo/electrum/blob/master/pubkeys/ThomasV.asc ) na GitHub, z którą można ją porównać.


Przewiń stronę nieco w dół, aby znaleźć link do klucza publicznego ThomasV (czerwone kółko poniżej). Kliknij go i pobierz lub, jeśli otworzy się tekst w przeglądarce, kliknij prawym przyciskiem myszy, aby zapisać.


![image](assets/4.webp)


Masz teraz 3 nowe pliki, prawdopodobnie wszystkie w folderze pobierania. Nie ma znaczenia, gdzie się znajdują, ale ułatwi to proces, jeśli wszystkie zostaną umieszczone w tym samym folderze.


Trzy pliki:


1. Electrum do pobrania

2. Plik podpisu (zwykle jest to ta sama nazwa pliku, co pobrany plik Electrum z dodatkiem ".asc")

3. Klucz publiczny ThomasV.


Otwórz terminal w systemie Mac lub Linux albo wiersz polecenia (CMD) w systemie Windows.


Przejdź do katalogu Downloads (lub gdziekolwiek umieściłeś te trzy pliki). Jeśli nie masz pojęcia, co to oznacza, dowiedz się z tego krótkiego filmu dla systemu Linux/Mac (https://www.youtube.com/watch?v=AO0jzD1hpXc) i tego dla systemu Windows (https://www.youtube.com/watch?v=9zMWXD-xoxc). Pamiętaj, że na komputerach z systemem Linux w nazwach katalogów rozróżniana jest wielkość liter.


W terminalu wpisz to, aby zaimportować klucz publiczny ThomasV do "pęku kluczy" komputera (pęku kluczy to abstrakcyjna koncepcja - w rzeczywistości jest to tylko plik na komputerze):


```bash
gpg --import ThomasV.asc
```


Upewnij się, że nazwa pliku jest zgodna z pobranym plikiem. Zwróć też uwagę, że jest to podwójny myślnik, a nie pojedynczy. Zwróć też uwagę na spację przed i po "-import". Następnie naciśnij <enter>.


Plik powinien zostać zaimportowany. Jeśli pojawi się błąd, sprawdź, czy znajdujesz się w katalogu, w którym plik faktycznie istnieje. Aby sprawdzić, w którym katalogu się znajdujesz (na Macu lub Linuksie), wpisz pwd. Aby zobaczyć, jakie pliki znajdują się w katalogu, w którym jesteś (na Macu lub Linuksie), wpisz ls. Powinieneś zobaczyć plik tekstowy "ThomasV.asc", prawdopodobnie wśród innych plików.


Następnie uruchamiamy polecenie, aby zweryfikować podpis.


```bash
gpg –verify Electrum-4.1.5.tar.gz.asc Electrum-4.1.5.tar.gz
```


Zauważ, że są tu 4 "Elements", każdy oddzielony spacją. Pogrubiłem tekst naprzemiennie, aby pomóc ci zobaczyć. Cztery Elements to:


1. program gpg

2. opcja -verify

3. nazwa pliku podpisu

4. nazwa pliku programu


Co ciekawe, czasami można pominąć czwarty element, a komputer zgadnie, o co chodzi. Nie jestem pewien, ale wydaje mi się, że działa to tylko wtedy, gdy nazwy plików różnią się tylko "asc" na końcu.


Nie kopiuj tylko nazw plików, które tutaj pokazałem - upewnij się, że pasują one do nazwy pliku, który masz w systemie.


Naciśnij <enter>, aby uruchomić polecenie. Powinieneś zobaczyć "dobry podpis od ThomasV", aby wskazać sukces. Pojawią się pewne błędy, ponieważ nie mamy kluczy publicznych dla podpisów innych osób, które są zawarte w pliku podpisu (ten system łączenia podpisów w jednym pliku może ulec zmianie w późniejszych wersjach). Ponadto na dole znajduje się ostrzeżenie, które możemy zignorować (ostrzega nas, że nie powiedzieliśmy komputerowi, że ufamy kluczowi publicznemu ThomasV).


Teraz mamy zweryfikowaną kopię Electrum, która jest bezpieczna w użyciu.


## Uruchamianie Electrum


### Uruchamianie Electrum przy użyciu Pythona


Jeśli pobrałeś wersję Python, oto jak sprawić, by działała. Na stronie pobierania zobaczysz to:


![image](assets/5.webp)


W przypadku Linuksa warto najpierw zaktualizować system:


```bash
sudo apt-get update
sudo apt-get upgrade
```


Skopiuj podświetlony żółty tekst, wklej go do terminala i naciśnij <enter>. Zostaniesz poproszony o podanie hasła, ewentualnie potwierdzenie, aby kontynuować, a następnie zainstaluje te pliki ("zależności").


Konieczne będzie również rozpakowanie spakowanego pliku do wybranego katalogu. Możesz to zrobić za pomocą graficznego użytkownika Interface lub z wiersza poleceń (polecenie podświetlone na różowo) - pamiętaj, że nazwy plików mogą się różnić. (Zwróć uwagę, że kiedy weryfikowaliśmy pobieranie w poprzedniej sekcji, weryfikowaliśmy plik zip, a nie wyodrębniony katalog)


Istnieje opcja "instalacji" za pomocą programu PIP, ale jest to niepotrzebne i dodaje dodatkowe kroki i instalację plików. Wystarczy uruchomić program za pomocą terminala, aby to wszystko ominąć.


Kroki (Linux) są następujące:


1. przejdź do katalogu, w którym pliki zostały wyodrębnione

2. typ: ./run_electrum


Na komputerach Mac kroki są takie same, ale może być konieczne wcześniejsze zainstalowanie Python3 i użycie tego polecenia do uruchomienia:


```bash
python3 ./run_electrum
```


Po uruchomieniu Electrum okno terminala pozostanie otwarte. Jego zamknięcie spowoduje zakończenie programu Electrum. Wystarczy je zminimalizować podczas korzystania z Electrum.


### Uruchamianie Electrum za pomocą Appimage


Jest to nieco łatwiejsze, ale nie tak proste, jak w przypadku pliku wykonywalnego Windows. W zależności od wersji systemu Linux, domyślnie pliki Appimage mogą mieć ustawione atrybuty, które uniemożliwiają ich wykonanie przez system. Musimy to zmienić. Jeśli twój Appimages działa, możesz pominąć ten krok. Przejdź do miejsca, w którym znajduje się plik, używając terminala, a następnie uruchom to polecenie:


```bash
sudo chmod ug+x Electrum-4.1.5-x86_64.AppImage
```


"sudo" nadaje uprawnienia superużytkownika; "chmod" jest poleceniem zmieniającym tryb, zmieniającym, kto może czytać, pisać lub wykonywać; "ug+x" oznacza, że modyfikujemy użytkownika i grupę, aby zezwolić na wykonanie.


Dostosuj nazwę pliku do swojej wersji.


Następnie Electrum uruchomi się po dwukrotnym kliknięciu ikony Appimage.


### Uruchamianie Electrum na komputerze Mac


Wystarczy dwukrotnie kliknąć pobrany plik (jest to "dysk"). Otworzy się okno. Przeciągnij ikonę Electrum w oknie na pulpit lub gdziekolwiek chcesz zachować program. Następnie można "wysunąć" dysk i usunąć dysk (pobrany plik).


Aby uruchomić program, wystarczy kliknąć go dwukrotnie. Mogą pojawić się specyficzne dla komputerów Mac błędy "niani", które należy ominąć.


### Uruchamianie Electrum w systemie Windows


Pomimo tego, że najbardziej nienawidzę systemu Windows, jest to najprostsza metoda. Wystarczy dwukrotnie kliknąć plik wykonywalny, aby go uruchomić.


## Zacznij od atrapy Wallet


Po pierwszym załadowaniu Electrum otworzy się takie okno:


![image](assets/6.webp)


Później wybierzemy serwer ręcznie, ale na razie pozostawmy ustawienie domyślne i automatyczne połączenie.


Następnie utwórz fikcyjny Wallet - nigdy nie wkładaj środków do tego Wallet. Celem tej atrapy Wallet jest przejście przez oprogramowanie i upewnienie się, że wszystko działa dobrze przed załadowaniem prawdziwego Wallet. Staramy się uniknąć przypadkowej utraty prywatności przy użyciu prawdziwego Wallet. Jeśli tylko ćwiczysz, utworzony Wallet i tak można uznać za atrapę Wallet.


Możesz pozostawić nazwę jako "default_wallet" lub zmienić ją na dowolną, a następnie kliknąć przycisk Dalej. Później, jeśli masz wiele portfeli, możesz je znaleźć i otworzyć na tym etapie, klikając najpierw "Wybierz..."


![image](assets/7.webp)


Wybierz "Standard Wallet" i <Next>:


![image](assets/8.webp)


Następnie wybieramy "Mam już seed". Nie chcę, abyś nabrał nawyku tworzenia Electrum seed, ponieważ używa on własnego protokołu, który nie jest kompatybilny z innymi portfelami - dlatego nie klikamy "nowy seed".


![image](assets/9.webp)


Przejdź na stronę https://iancoleman.io/bip39/ i utwórz fikcyjny seed. Najpierw zmień numer słowa na 12 (co jest powszechną praktyką), a następnie kliknij "generate" i skopiuj słowa w polu do schowka.


![image](assets/10.webp)


Następnie wklej słowa do Electrum. Oto przykład:


![image](assets/11.webp)


Electrum będzie szukać słów, które pasują do jego własnego protokołu. Musimy to ominąć. Kliknij opcje i wybierz BIP39 seed:


![image](assets/12.webp)


seed staje się wtedy ważny. (Przed wykonaniem tej czynności Electrum oczekiwało Electrum seed, więc ten seed był postrzegany jako nieważny). Zanim klikniesz dalej, zwróć uwagę na tekst "Suma kontrolna OK". Ważne jest (dla prawdziwego Wallet, którego możesz użyć później), aby zobaczyć to przed kontynuowaniem, ponieważ potwierdza to ważność wprowadzonego seed. Ostrzeżenie na dole można zignorować, jest to narzekanie dewelopera Electrum na BIP39 i ich "FUD'ey" twierdzenia, że ich wersja (która nie jest kompatybilna z innymi portfelami) jest lepsza.


**Krótki objazd dla ważnego ostrzeżenia:** celem sumy kontrolnej jest upewnienie się, że seed został wprowadzony bez błędów literowych. Suma kontrolna jest ostatnią częścią seed (12 słowo jest słowem sumy kontrolnej), która jest matematycznie określona przez pierwszą część seed (11 słów). Jeśli wpiszesz coś nieprawidłowego na początku, słowo sumy kontrolnej nie będzie matematycznie zgodne, a oprogramowanie Wallet wyświetli ostrzeżenie. Nie oznacza to, że seed nie może być użyty do stworzenia funkcjonalnego Bitcoin Wallet. Wyobraź sobie, że tworzysz Wallet z błędem literowym, ładujesz Wallet z Bitcoin, a pewnego dnia możesz potrzebować przywrócić Wallet, ale kiedy to zrobisz, nie odtworzysz błędu literowego - przywrócisz niewłaściwy Wallet! To dość niebezpieczne, że Electrum pozwoli ci kontynuować tworzenie Wallet, jeśli twoja suma kontrolna jest nieprawidłowa, więc bądź ostrzeżony, to twoja odpowiedzialność, aby się upewnić. Inne portfele nie pozwolą ci kontynuować, co jest znacznie bezpieczniejsze. Jest to jedna z rzeczy, które mam na myśli, gdy mówię, że Electrum jest w porządku, gdy nauczysz się go poprawnie używać (twórcy Electrum powinni to naprawić).


Zauważ, że jeśli chcesz dodać passphrase, możliwość wyboru znajduje się w tym oknie opcji, na samej górze.


Po kliknięciu przycisku OK nastąpi powrót do miejsca, w którym wpisano frazę seed. Jeśli wybrano opcję passphrase, NIE należy wprowadzać jej wraz ze słowami seed (monit o to pojawi się później).


Jeśli nie poprosiłeś o passphrase, zobaczysz ten ekran - więcej opcji dla typu skryptu Wallet i ścieżki pochodnej, o których możesz dowiedzieć się tutaj (https://armantheparman.com/public-and-private-keys/), ale po prostu pozostaw domyślne ustawienia i kontynuuj.


![image](assets/13.webp)


**Dodatkowe informacje** Pierwsza opcja umożliwia wybór pomiędzy:



- legacy (adresy zaczynające się od "1"),
- Pay-to-Script-Hash (adresy zaczynające się od "3"),
- bech32/native SegWit (adresy zaczynające się od "bc1q").


W chwili pisania tego tekstu Electrum nie obsługuje jeszcze Taproot (adresy zaczynające się od "bc1p"). Druga opcja w tym oknie pozwala zmodyfikować ścieżkę derywacji. Sugeruję, aby nigdy tego nie modyfikować, zwłaszcza przed zrozumieniem, co to oznacza. Ludzie będą podkreślać znaczenie zapisywania ścieżki pochodnej, aby w razie potrzeby można było odzyskać Wallet, ale jeśli pozostawisz ją jako domyślną, prawdopodobnie wszystko będzie dobrze, więc nie panikuj - ale nadal dobrą praktyką jest zapisywanie ścieżki pochodnej.


Następnie pojawi się opcja dodania HASŁA. Nie należy tego mylić z "passphrase". Hasło blokuje plik na komputerze. passphrase jest częścią składową klucza prywatnego. Ponieważ jest to fikcyjny Wallet, możesz pozostawić hasło puste i kontynuować.


![image](assets/14.webp)


Pojawi się wyskakujące okienko z powiadomieniem o nowej wersji (sugeruję wybrać nie). Wallet będzie wtedy generate i będzie gotowy do użycia (ale pamiętaj, że ten Wallet jest przeznaczony do usunięcia, to tylko atrapa Wallet).


![image](assets/15.webp)


Jest kilka rzeczy, które sugeruję zrobić, aby skonfigurować środowisko oprogramowania (wymagane tylko raz):


### Zmień jednostki na BTC


Przejdź do górnego menu, narzędzia -> preferencje electrum, a tam w zakładce ogólne znajdziesz opcję zmiany "jednostki bazowej" na BTC.

Włącz kartę Adresy i monety


Przejdź do górnego menu, widoku i wybierz "pokaż adresy". Następnie wróć do widoku i wybierz "pokaż monety".


### Włącz serwer Oneserver


Domyślnie Electrum łączy się z losowym węzłem. Łączy się również z wieloma innymi węzłami drugorzędnymi. Nie jestem pewien, jakie dane są wymieniane z tymi drugorzędnymi węzłami, ale nie chcemy, aby tak się działo, ze względu na prywatność. Nawet jeśli określisz węzeł, np. swój własny węzeł, te wiele innych węzłów również zostanie połączonych i nie jestem pewien, jakie informacje są udostępniane. Niezależnie od tego, można temu łatwo zapobiec. Zanim pokażę, jak określić własny węzeł, zmusimy Electrum do łączenia się tylko z jednym serwerem na raz.


**Uwaga:** Istnieje sposób na zrobienie tego poprzez określenie "oneserver" z linii poleceń, ale nie polecam tego sposobu. Pokażę alternatywę, która moim zdaniem jest łatwiejsza na dłuższą metę i bardziej prawdopodobne, że nie pozwoli ci przypadkowo połączyć się z innymi węzłami.


Powodem, dla którego używamy fikcyjnego Wallet, jest to, że gdybyśmy załadowali nasz prawdziwy Wallet z naszym prawdziwym Bitcoin, do tej pory nieumyślnie połączylibyśmy się z losowym węzłem (nawet jeśli wybraliśmy "ustaw serwer ręcznie" na początku, z jakiegoś powodu nadal łączy się z tymi innymi węzłami drugorzędnymi (hej programiści Electrum, powinniście to naprawić). Gdyby nasz Wallet był prywatny, byłaby to katastrofa.


Nie możemy również wykonać kroków, które pokażę poniżej, bez wcześniejszego załadowania jakiegoś typu Wallet. (Będziemy edytować plik konfiguracyjny, który zostanie wypełniony i gotowy do edycji dopiero po załadowaniu Wallet).


Teraz wyłącz Electrum **(WAŻNE: jeśli tego nie zrobisz, następujące zmiany zostaną usunięte)**.


### Plik konfiguracyjny LINUX/MAC


Otwórz terminal w systemie Linux lub Mac (instrukcje dla systemu Windows w późniejszym czasie):


Powinieneś automatycznie znaleźć się w folderze domowym. Stamtąd przejdź do ukrytego folderu ustawień electrum (różni się on od miejsca, w którym znajduje się aplikacja).


```bash
cd .electrum
```


Zwróć uwagę na kropkę przed "electrum", która wskazuje, że jest to ukryty folder.


Innym sposobem, aby się tam dostać, jest wpisanie:


```bash
cd ~/.electrum
```


gdzie "~" reprezentuje ścieżkę do katalogu domowego. Pełną ścieżkę do bieżącego katalogu można zobaczyć za pomocą polecenia "pwd".


Po wejściu do katalogu ".electrum" wpisz "nano config" i naciśnij <enter>.


Otworzy się edytor tekstu (o nazwie nano) z otwartym plikiem konfiguracyjnym. Mysz nie działa tutaj zbyt dobrze. Użyj klawiszy strzałek, aby dostać się do linii, która mówi:


```json
"oneserver": false,
```


Zmień "false" na "true" i nie zmieniaj składni (nie usuwaj przecinka ani średnika).


Naciśnij <ctrl> x, aby wyjść, następnie "y", aby zapisać, a następnie <enter>, który potwierdza zmianę bez edytowania nazwy pliku.


Teraz ponownie uruchom Electrum. Następnie kliknij kółko w prawym dolnym rogu, co otworzy ustawienia sieciowe. Następnie, u góry w zakładce przeglądu, zobaczysz "połączono z 1 węzłem" - oznacza to sukces.


Tuż pod nim znajduje się pole tekstowe, a w nim Address serwera. Jesteś obecnie połączony z tym losowym węzłem. Więcej na temat łączenia się z węzłem w następnej sekcji.


### Plik konfiguracyjny systemu Windows


Plik konfiguracyjny Windows jest nieco trudniejszy do znalezienia. Katalog to: `C:/Users/Parman/AppData/Roaming/Electrum`


Oczywiście musisz zmienić "Parman" na własną nazwę użytkownika komputera.


W folderze tym znajduje się plik konfiguracyjny. Otwórz go za pomocą edytora tekstu i edytuj linię:


```json
"oneserver": false,
```


Zmień "false" na "true"; nie zmieniaj składni (nie usuwaj przecinka ani średnika).


Następnie zapisz plik i wyjdź.


## Podłącz Electrum do węzła


Następnie chcemy podłączyć naszą atrapę Wallet do wybranego węzła. Jeśli nie jesteś gotowy do uruchomienia węzła, możesz wykonać jedną z poniższych czynności:


1. Połączenie z węzłem osobistym znajomego (wymaga sieci Tor)

2. Połączenie z węzłem zaufanej firmy

3. Połącz się z losowym węzłem (niezalecane).


Nawiasem mówiąc, oto instrukcje dotyczące uruchamiania własnego węzła, a oto powody, dla których powinieneś. (sprawdź samouczki w sekcji Node lub w naszych bezpłatnych kursach)


### Połącz się z węzłem znajomego za pośrednictwem sieci Tor (przewodnik wkrótce)


### Połączenie z węzłem zaufanej firmy


Jedynym powodem, dla którego warto to zrobić, jest konieczność uzyskania dostępu do Blockchain i brak własnego węzła (lub węzła znajomego).


Połączmy się z węzłem Bitaroo - powiedziano nam, że nie zbierają danych. Są to Bitcoin Only Exchange, prowadzone przez pasjonata Bitcoinera. Połączenie z nimi wymaga odrobiny zaufania, ale jest lepsze niż połączenie z losowym węzłem, który może być firmą inwigilacyjną.


Przejdź do ustawień sieci, klikając kółko w prawej dolnej części okna Wallet (czerwony oznacza brak połączenia, Green oznacza połączenie, a niebieski oznacza połączenie przez Tor).


![image](assets/16.webp)


Po kliknięciu ikony okręgu pojawi się wyskakujące okienko: Twój Wallet pokaże "podłączony do 1 węzła", ponieważ wymusiliśmy to wcześniej.


Odznacz pole "Wybierz serwer automatycznie", a następnie w polu Serwer wpisz dane Bitaroo, jak pokazano:


![image](assets/17.webp)


Zamknij okno, a teraz powinniśmy być połączeni z węzłem Bitaroo. Aby to potwierdzić, kółko powinno być Green. Kliknij go ponownie i sprawdź, czy dane serwera nie zmieniły się z powrotem na losowy węzeł.


### Połączenie z własnym węzłem


Jeśli masz własny węzeł, to świetnie. Jeśli masz tylko Bitcoin Core, a nie Electrum SERVER, nie będziesz jeszcze w stanie podłączyć Electrum Wallet do swojego węzła.


**Należy pamiętać, że Electrum Server i Electrum Wallet to różne rzeczy:** Serwer jest oprogramowaniem wymaganym dla Electrum Wallet, aby mógł komunikować się z Bitcoin Blockchain - nie wiem, dlaczego został zaprojektowany w ten sposób - prawdopodobnie ze względu na szybkość, ale mogę się mylić.


Jeśli korzystasz z pakietu oprogramowania węzła, takiego jak MyNode (ten, który polecam ludziom na początek), Raspiblitz (zalecany, gdy stajesz się bardziej zaawansowany) lub Umbrel (osobiście nie polecam go jeszcze, ponieważ doświadczyłem zbyt wielu problemów), będziesz mógł podłączyć Wallet po prostu wpisując IP Address komputera (Raspberry Pi) z uruchomionym węzłem, plus dwukropek i 50002, jak pokazano na obrazku w poprzedniej sekcji. (W dalszej części pokażę, jak znaleźć adres IP Address węzła).


Otwórz ustawienia sieciowe (kliknij Green lub czerwone kółko w prawym dolnym rogu). Odznacz pole "wybierz serwer automatycznie", a następnie wprowadź swój adres IP Address, tak jak ja to zrobiłem, Twój będzie inny, ale dwukropek i "50002" powinny być takie same.


![image](assets/18.webp)


Zamknij okno, a teraz powinniśmy być połączeni z Twoim węzłem. Aby potwierdzić, kliknij ponownie kółko i sprawdź, czy dane serwera nie zmieniły się z powrotem na losowy węzeł.


Czasami, pomimo robienia wszystkiego dobrze, pozornie odmawia połączenia. Oto rzeczy do wypróbowania..



- Zaktualizuj Electrum i oprogramowanie węzła do nowszej wersji;
- Spróbuj usunąć folder pamięci podręcznej w katalogu ".electrum";
- Spróbuj zmienić port z 50002 na 50001 w ustawieniach sieciowych;
- Skorzystaj z [tego przewodnika] (https://armantheparman.com/tor/), aby połączyć się za pomocą Tora jako alternatywy;
- Ponownie zainstaluj Electrum Server na węźle.


## Znajdowanie adresu IP węzła Address


IP Address nie jest czymś, co zwykły użytkownik zwykle wie, jak wyszukać i używać. Pomogłem wielu osobom uruchomić węzeł, a następnie podłączyć do niego swoje portfele - przeszkodą często wydaje się być znalezienie jego adresu IP Address.


W przypadku MyNode można wpisać w oknie przeglądarki: `mynode.local`


Czasami "mynode.local" nie działa (upewnij się, że nie wpisujesz go w pasku wyszukiwania Google). Aby zmusić pasek nawigacyjny do rozpoznania tekstu jako Address, a nie wyszukiwania, poprzedź tekst `http://` w następujący sposób: `http://mynode.local`. Jeśli to nie zadziała, spróbuj z literą "s", jak poniżej: `https://mynode.local`.


Spowoduje to uzyskanie dostępu do urządzenia i kliknięcie łącza ustawień (patrz moje niebieskie "kółko" poniżej), aby wyświetlić ekran, na którym znajduje się IP Address:


![image](assets/19.webp)


Strona załaduje się i zobaczysz adres IP węzła (niebieskie "kółko")


![image](assets/20.webp)


Następnie w przyszłości można wpisać w przeglądarce adres 192.168.0.150 lub http://192.168.0.150.


W przypadku Raspiblitz (gdy nie jest podłączony ekran) potrzebna jest inna metoda (która działa również w przypadku MyNode):


Zaloguj się do strony internetowej routera - tutaj znajdziemy IP Address wszystkich podłączonych urządzeń. Strona internetowa routera będzie miała adres IP Address, który należy wpisać w przeglądarce internetowej. Moja wygląda następująco:


http://192.168.0.1


Aby uzyskać dane logowania do routera, można je znaleźć w instrukcji obsługi, a czasem nawet na naklejce na samym routerze. Poszukaj nazwy użytkownika i hasła. Jeśli nie możesz ich znaleźć, spróbuj Użytkownik: "admin" Hasło: "hasło"


Jeśli jesteś w stanie się zalogować, zobaczysz podłączone urządzenia, a z ich nazw może być jasne, który węzeł jest twój. IP Address będzie się tam znajdować.


### Jeśli dwie pierwsze metody zawiodą, ostatnia zadziała, ale jest żmudna:


Najpierw znajdź adres IP Address dowolnego urządzenia w sieci (wystarczy bieżący komputer).


Na komputerach Mac można ją znaleźć w preferencjach sieciowych:


![image](assets/21.webp)


Interesują nas pierwsze 4 Elements (192.168.0), a nie czwarty element, "166", który widzisz na obrazku (twój będzie inny).


W przypadku systemu Linux należy użyć wiersza poleceń:


```bash
ifconfig | grep inet
```


Ta pionowa linia to symbol "pipe", który znajduje się pod klawiszem <delete>. Zobaczysz kilka danych wyjściowych i IP Address. (Zignoruj 127.0.0.1 to nie to i zignoruj maskę sieci)


W systemie Windows otwórz wiersz polecenia (cmd) i wpisz:


```bash
ipconfig/all
```


i naciśnij Enter. IP Address można znaleźć w danych wyjściowych.


To była najłatwiejsza część. Część Hard polega teraz na znalezieniu adresu IP Address węzła - musimy zgadnąć brute-force. Powiedzmy na przykład, że IP Address komputera zaczyna się od 192.168.0.xxx, a następnie dla węzła, w przeglądarce, spróbuj: `https://192.168.0.2`


Najmniejsza możliwa liczba to 2 (0 oznacza dowolne urządzenie, a 1 należy do routera), a najwyższa, jak sądzę, to 255 (tak się składa, że jest to 11111111 w systemie binarnym, największa liczba przechowywana przez 1 bajt).


Jeden po drugim, przesuwaj się w górę do 255. W końcu zatrzymasz się na prawidłowej liczbie, która załaduje stronę MyNode (lub stronę RaspiBlitz). Wtedy będziesz wiedział, jaki numer wprowadzić w ustawieniach sieci Electrum, aby połączyć się z węzłem.


Będzie on wyglądał mniej więcej tak (upewnij się, że po dwukropku i numerze znajduje się kropka):


![image](assets/22.webp)


**Uwaga** warto wiedzieć, że te adresy IP są adresami wewnętrznymi sieci domowej. Nikt z zewnątrz nie może ich zobaczyć i nie są one wrażliwe. Są one czymś w rodzaju numerów wewnętrznych w dużej organizacji, które kierują użytkownika do różnych telefonów.


## Usuń fikcyjny Wallet


Teraz udało nam się połączyć z jednym i tylko jednym węzłem. W ten sposób Electrum będzie ładować się domyślnie od teraz. Powinieneś teraz usunąć fikcyjny Wallet (Menu: plik -> usuń), na wypadek gdybyś przypadkowo wysłał środki do tego niezabezpieczonego Wallet (jest niezabezpieczony, ponieważ nie stworzyliśmy go w bezpieczny sposób).


## Wykonaj ćwiczenie Wallet


Po usunięciu fikcyjnego Wallet, zacznij od nowa i stwórz nowy, w ten sam sposób, tylko tym razem zapisz słowa seed i przechowuj je w miarę bezpiecznie.


Dobrym pomysłem jest nauczenie się, jak działa Electrum z tym praktycznym Wallet, bez uciążliwego Hardware Wallet (potrzebnego do wysokiego bezpieczeństwa). Umieść tylko niewielką ilość Bitcoin w tym Wallet - załóż, że stracisz te pieniądze. Gdy nabierzesz wprawy, naucz się używać Electrum z Hardware Wallet.


W nowym Wallet, który utworzyłeś, zobaczysz listę adresów. Adresy Green są nazywane "adresami odbiorczymi". Są one wypadkową 3 rzeczy:



- Zwrot seed
- passphrase
- Ścieżka wyprowadzania


Nowy Wallet ma zestaw adresów odbiorczych, które mogą być matematycznie i odtwarzalnie utworzone przez dowolny Software Wallet, który ma seed, passphrase i ścieżkę pochodną. Jest ich 4,3 miliarda! Więcej niż będziesz potrzebować. Electrum pokazuje tylko pierwsze 20, a następnie więcej w miarę zużywania pierwszych.


Więcej informacji na temat kluczy prywatnych Bitcoin można znaleźć w tym przewodniku.


![image](assets/23.webp)


To bardzo różni się od niektórych innych portfeli, które prezentują tylko 1 Address na raz.


Ponieważ wprowadziłeś frazę seed podczas tworzenia tego Wallet, Electrum ma klucz prywatny dla każdego z adresów i możliwe jest wydawanie z tych adresów.


Należy również pamiętać, że istnieją żółte adresy, zwane "adresami zmiany" - są to po prostu inne adresy z innej gałęzi matematycznej (istnieje kolejne 4,3 miliarda takich adresów). Są one używane przez Wallet do automatycznego wysyłania nadmiaru środków z powrotem do Wallet jako zmiana. Na przykład, jeśli weźmiesz 1,5 Bitcoin i wydasz 0,5 sprzedawcy, reszta 1,0 musi gdzieś trafić. Twój Wallet wyda je do następnego pustego żółtego Address - w przeciwnym razie trafią one do Miner! Więcej informacji na ten temat (UTXO) można znaleźć w ![ten poradnik](https://armantheparman.com/UTXO/).


Następnie wróć do strony klucza prywatnego Iana Colmana i wprowadź seed (zamiast go generować). Zobaczysz, że poniżej zmieniają się informacje o kluczu prywatnym i publicznym; wszystko poniżej zależy od rzeczy powyżej na stronie.


**Pamiętaj:** nie powinieneś "nigdy" wpisywać seed swojego prawdziwego Bitcoin Wallet lub komputera, złośliwe oprogramowanie może go ukraść. Używamy tylko praktycznego Wallet do celów edukacyjnych, więc na razie jest w porządku.


Przewiń w dół i zmień ścieżkę pochodną na BIP84 (SegWit), aby dopasować Electrum Wallet, klikając kartę BIP84.


![image](assets/24.webp)


Poniżej znajduje się rozszerzony klucz prywatny konta i rozszerzony klucz publiczny konta:


![image](assets/25.webp)


Przejdź do Electrum i porównaj, czy się zgadzają. Na górze znajduje się menu Wallet ->informacje:


![image](assets/26.webp)


Pojawia się to:


![image](assets/27.webp)


Zauważ, że oba klucze publiczne pasują do siebie.


Następnie porównaj adresy. Wróć na stronę Iana Colemana i przewiń w dół:


![image](assets/28.webp)


Zauważ, że są one zgodne z adresami w Electrum.


Teraz sprawdzimy adresy zmian. Przewiń nieco w górę do ścieżki pochodnej i zmień ostatnie 0 na 1:


![image](assets/29.webp)


Teraz przewiń w dół i porównaj adresy z żółtymi adresami w Electrum


Dlaczego to wszystko zrobiliśmy?


Wzięliśmy słowa seed i przepuściliśmy je przez dwa różne niezależne programy, aby upewnić się, że dostarczają nam tych samych informacji. To znacznie zmniejsza ryzyko, że w środku czai się złośliwy kod, który przekazuje nam fałszywe klucze prywatne, publiczne lub adresy.


Następną rzeczą do zrobienia jest otrzymanie małego testu i wydanie go w ramach Wallet z jednego Address do drugiego.


## Testowanie Wallet (naucz się go używać)


Tutaj pokażę, jak otrzymać UTXO do swojego Wallet, a następnie przenieść go (wydać) do innego Address w ramach Wallet. Jest to bardzo mała kwota, której nie będziemy mieli nic przeciwko ryzyku utraty.


Ma to kilka celów.



- Udowodni to, że masz moc wydawania monet w nowym Wallet.
- Zademonstrujemy, jak używać oprogramowania Electrum do wydawania pieniędzy (i niektórych funkcji), zanim dodamy dodatkową złożoność dla bezpieczeństwa (używając Hardware Wallet lub komputera z osłoną powietrzną)
- Wzmocni to przekonanie, że masz wiele adresów do wyboru, aby otrzymywać i wydawać pieniądze w ramach tego samego Wallet.


Otwórz testowy Electrum Wallet i kliknij kartę Adresy, a następnie kliknij prawym przyciskiem myszy pierwszy Address i wybierz Kopiuj -> Address:


![image](assets/30.webp)


Urządzenie Address znajduje się teraz w pamięci komputera.


Teraz przejdź do Exchange, gdzie masz trochę Bitcoin, i wypłać niewielką kwotę do tego Address, powiedzmy 50 000 Sats. Użyję Coinbase jako przykładu, ponieważ jest to najczęściej używany Exchange, mimo że są wrogami Bitcoin, a ja jestem obrzydzony logowaniem się na stare porzucone konto w tym celu.


Zaloguj się i kliknij przycisk Wyślij/Odbierz, który obecnie znajduje się w prawym górnym rogu strony.


![image](assets/31.webp)


Oczywiście nie mam środków w Coinbase, ale wyobraź sobie, że są tutaj środki i postępuj zgodnie z instrukcjami: Wklej Address z Electrum w polu "Do", tak jak ja to zrobiłem. Musisz również wybrać kwotę (sugeruję około 50 000 Sats). Nie umieszczaj "opcjonalnej wiadomości" - Coinbase zbiera wystarczająco dużo Twoich danych (i je sprzedaje), nie ma potrzeby im pomagać. Na koniec kliknij "Kontynuuj". Po tym nie wiem, jakie inne wyskakujące okienka otrzymasz, jesteś zdany na siebie, ale metoda jest podobna dla wszystkich giełd.


![image](assets/32.webp)


W zależności od Exchange, Sats może pojawić się w Wallet natychmiast lub po kilku godzinach/dniach.


Należy pamiętać, że Electrum pokaże otrzymane monety, nawet jeśli nie zostały one potwierdzone na Blockchain. Posiadane monety są odczytywane z listy oczekujących węzła Bitcoin lub "Mempool". Gdy dojdzie do bloku, zobaczysz środki jako potwierdzone.


Teraz, gdy mamy UTXO w naszym Wallet, powinniśmy go oznaczyć. Tylko my widzimy tę etykietę, nie ma ona nic wspólnego z publicznym Ledger. Wszystkie nasze etykiety Electrum są widoczne tylko na komputerze, którego używamy. W rzeczywistości możemy zapisać plik i użyć go do przywrócenia wszystkich naszych etykiet na innym komputerze z tym samym Wallet.


### Tworzenie etykiety dla UTXO


Potrzebowałem darowizny na ten testowy Wallet, dzięki @Sathoarder za dostarczenie mi żywego UTXO (10 000 Sats), a inna osoba (anon) przekazała darowiznę na ten sam Address (5000 Sats). Zauważ, że w pierwszym saldzie Address jest 15 000 Sats i łącznie 2 transakcje (skrajna prawa kolumna). Na dole, saldo wynosi 10 000 potwierdzonych Sats, a kolejne 5 000 Sats jest niepotwierdzonych (wciąż w Mempool).


![image](assets/33.webp)


Teraz, jeśli przejdziemy do zakładki Monety, zobaczymy dwie "otrzymane monety" lub UTXO. Obie znajdują się w tym samym Address.


![image](assets/34.webp)


Wracając do karty Address, jeśli klikniesz dwukrotnie obszar "etykiety" obok Address, będziesz mógł wprowadzić tekst, a następnie nacisnąć <enter>, aby zapisać:


![image](assets/35.webp)


Jest to dobra praktyka, abyś mógł śledzić, skąd pochodzą twoje monety, czy są wolne od KYC, czy nie, i ile kosztował cię każdy UTXO (na wypadek, gdybyś musiał sprzedać i obliczyć podatek, który zostanie ci skradziony przez rząd).


Najlepiej byłoby unikać gromadzenia wielu monet w tym samym Address. Jeśli zdecydujesz się to zrobić (nie rób tego), możesz oznaczyć każdą monetę zamiast wszystkich tą samą etykietą przy użyciu metody Address. W rzeczywistości nie można przejść do zakładki "monety" i edytować tam etykiet (nie, to byłoby zbyt intuicyjne!). Musisz przejść do zakładki Historia, znaleźć transakcję, oznaczyć ją etykietą, a następnie zobaczysz etykiety w sekcji monet. Wszelkie etykiety widoczne w sekcji monet pochodzą z etykiet Address LUB etykiet historii, ale każda etykieta historii zastępuje każdą etykietę Address. Aby utworzyć kopię zapasową etykiet do pliku, można je wyeksportować z menu u góry, Wallet->lables->export.


Następnie wydajmy monety z pierwszego Address do drugiego Address. Kliknij prawym przyciskiem myszy pierwszy Address i wybierz opcję "wydaj z" (w rzeczywistości nie jest to konieczne w tym scenariuszu, ale wyobraźmy sobie, że mamy wiele monet w wielu adresach; korzystając z tej funkcji, możemy zmusić Wallet do wydawania tylko tych monet, które chcemy). Jeśli chcemy wybrać wiele monet w wielu adresach, możemy wybrać adresy, klikając lewym przyciskiem myszy, przytrzymując klawisz polecenia, a następnie kliknąć prawym przyciskiem myszy i wybrać opcję "wydaj z":


![image](assets/36.webp)


Gdy to zrobisz, na dole okna Wallet pojawi się pasek Green wskazujący liczbę wybranych monet i łączną kwotę dostępną do wydania.


Możesz również wydać pojedyncze monety w Address i wykluczyć inne w tym samym Address, ale jest to odradzane, ponieważ pozostawiasz monety w Address, który został osłabiony kryptograficznie z powodu wydania jednej z monet (innym powodem, dla którego nie należy umieszczać wielu monet w jednym Address, poza względami prywatności, jest to, że biorąc pod uwagę, że powinieneś wydać je wszystkie, jeśli wydasz jedną, staje się to niepotrzebnie kosztowne). Oto jak wybrać pojedynczą monetę ze współdzielonego Address, ale nie rób tego:


![image](assets/37.webp)


Teraz mamy dwie monety wybrane do wydania. Następnie zdecydowaliśmy, gdzie je wydać. Wyślijmy je do drugiego Address. Będziemy musieli skopiować Address w następujący sposób:


![image](assets/38.webp)


Następnie przejdź do zakładki "Wyślij" i wklej drugi Address w polu "zapłać do". Nie musisz dodawać opisu; możesz to zrobić później, edytując etykiety. Jako kwotę wybierz "Max", aby wydać wszystkie wybrane przez nas monety. Następnie kliknij "Zapłać", a następnie kliknij przycisk "Zaawansowane" w wyskakującym okienku, które się pojawi.


![image](assets/39.webp)


Na tym etapie zawsze klikamy "zaawansowane", dzięki czemu możemy uzyskać dokładną kontrolę i sprawdzić, co dokładnie znajduje się w transakcji. Oto transakcja:


![image](assets/40.webp)


Widzimy dwa wewnętrzne białe pola/okna. Górne to okno wejściowe (które monety są wydawane), a dolne to okno wyjściowe (gdzie trafiają monety).


Status (w lewym górnym rogu) jest na razie "niepodpisany". "Wysłana kwota" wynosi 0, ponieważ monety są przesyłane w ramach Wallet. Opłata wynosi 481 Sats. Zwróć uwagę, że gdyby było to 480 Sats, ostatnie zero zostałoby usunięte, tak jak tutaj, 0,0000048, a dla zmęczonego oka może to wyglądać jak 48 Sats - bądź ostrożny (coś, co twórcy Electrum powinni naprawić).


Rozmiar transakcji odnosi się do rozmiaru danych w bajtach, a nie do kwoty Bitcoin. Opcja "Replace by fee" jest domyślnie włączona i umożliwia ponowne wysłanie transakcji z wyższą opłatą w razie potrzeby. LockTime pozwala dostosować, kiedy transakcja jest ważna - jeszcze się tym nie bawiłem, ale odradzam korzystanie z tego, chyba że w pełni rozumiesz, co robisz i masz trochę praktyki z małymi kwotami.


Na dole mamy kilka wymyślnych narzędzi do regulacji opłat Mining. Wszystko, co musisz zrobić w przypadku transferów wewnętrznych, to ustawić minimalną opłatę na 1 sat/bajt. Wystarczy ręcznie wpisać liczbę w polu Opłata docelowa. Aby sprawdzić odpowiednią opłatę za płatność zewnętrzną, możesz sprawdzić https://Mempool.space, aby zobaczyć, jak zajęty jest Mempool, a niektóre sugerowane opłaty są wyświetlane.


![image](assets/41.webp)


Wybrałem 1 sat/bajt.


W oknie wprowadzania danych widzimy dwa wpisy. Pierwszy to darowizna w wysokości 5000 sat. Po lewej stronie widzimy transakcję Hash (którą możemy sprawdzić na Blockchain). Obok znajduje się "21" - oznacza to, że jest to wyjście oznaczone jako 21 w tej transakcji (w rzeczywistości jest to 22. wyjście, ponieważ pierwsze jest oznaczone jako zero).


Warto zwrócić na to uwagę: UTXO istnieją tylko wewnątrz transakcji. Aby wydać UTXO, musimy się do niego odwołać i umieścić to odwołanie na wejściu nowej transakcji. Wyjścia stają się wtedy nowymi UTXO, a stary UTXO staje się STXO (wyjście wydanej transakcji).


Drugi wiersz to darowizna w wysokości 10 000 sat. Ma wartość "0" obok transakcji Hash, z której pochodzi, ponieważ jest to pierwszy (i prawdopodobnie jedyny) wynik dla tej transakcji.


W dolnym oknie widzimy nasz Address. Zauważ, że suma wejść Bitcoin nie pokrywa się z sumą wyjść. Różnica trafia do Miner. Miner analizuje rozbieżność we wszystkich transakcjach w bloku, który próbuje wydobyć, i dodaje tę liczbę do swojej nagrody. (Opłaty Mining w ten sposób są całkowicie odłączone od łańcucha transakcji i rozpoczynają nowe życie).


Jeśli dostosujemy opłatę Mining, wartość wyjściowa zmieni się automatycznie.


**Warto tutaj zwrócić uwagę:** na kolor adresów w oknie transakcji. Pamiętaj, że adresy Green są wymienione w zakładce Address. Jeśli Address jest podświetlony Green (lub na żółto) w oknie transakcji, oznacza to, że Electrum rozpoznało Address jako jeden ze swoich. Jeśli Address nie jest podświetlony, oznacza to, że jest to zewnętrzny Address (zewnętrzny w stosunku do aktualnie otwartego Wallet) i należy sprawdzić go ze szczególną ostrożnością.


Po sprawdzeniu wszystkich elementów transakcji i upewnieniu się, że jesteś zadowolony z tego, które monety wydajesz i dokąd one trafiają, możesz kliknąć "sfinalizuj"


![image](assets/42.webp)


Po kliknięciu przycisku "sfinalizuj" nie można już wprowadzać zmian - w razie potrzeby należy zamknąć okno i zacząć od nowa. Zauważ, że przycisk "finalizuj" zmienił się na "eksportuj" i pojawiły się nowe przyciski: "zapisz", "połącz", "podpisz" i "nadaj". Przycisk "broadcast" jest wyszarzony, ponieważ transakcja jest niepodpisana, a więc na tym etapie nieważna.


Po kliknięciu przycisku podpisu, jeśli masz hasło do Wallet, zostaniesz o nie poproszony, a następnie status (w prawym górnym rogu) zmieni się z "Niepodpisany" na "Podpisany". Następnie dostępny będzie przycisk "Broadcast".


Po nadaniu można zamknąć okno transakcji. Jeśli przejdziesz do karty Address, zobaczysz teraz, że pierwszy Address jest pusty, a drugi Address ma 1 UTXO.


Uwaga: Wszystkie te zmiany będą widoczne nawet przed wydobyciem transakcji do bloku lub jej "potwierdzeniem". Dzieje się tak, ponieważ Electrum aktualizuje salda/transakcje w oparciu nie tylko o dane Blockchain, ale także dane Mempool. Nie wszystkie portfele to robią.


Warto zauważyć, że zamiast nadawać, możemy zapisać transakcję na później. Transakcja może być zapisana w stanie niepodpisanym lub podpisanym.


Kliknij przycisk "eksportuj" (paradoksalnie NIE klikaj przycisku "zapisz"), a zobaczysz szereg opcji. Transakcja jest zakodowana tekstem i dlatego może być zapisana na wiele sposobów.


![image](assets/43.webp)


Zapisywanie do kodu QR jest bardzo interesujące. Jeśli wybierzesz tę opcję, pojawi się QR:


![image](assets/44.webp)


Następnie można zrobić zdjęcie kodu QR. Można z tym zrobić wiele rzeczy, ale na razie powiedzmy, że później załadujesz go z powrotem do Wallet. Możesz zamknąć Electrum, ponownie załadować Wallet i przejść do menu Narzędzia:


![image](assets/45.webp)


Spowoduje to załadowanie kamery komputera. Następnie należy pokazać kamerze zdjęcie kodu QR w telefonie, co spowoduje ponowne załadowanie transakcji, dokładnie tak, jak ją pozostawiono.


Wczytywanie zapisanych transakcji nie jest intuicyjne, więc należy zwrócić na to szczególną uwagę. Ładowanie transakcji nie jest "narzędziem", ale opcja jest ukryta w menu narzędzi (kolejna rzecz, którą twórcy Electrum powinni naprawić).


Podobny proces jest możliwy w przypadku transakcji zapisanej jako plik. Spróbuj przećwiczyć obie metody w ramach tego samego Wallet. Nie będę tego tutaj opisywał, ale możesz użyć tej funkcji do przekazywania transakcji między tym samym Wallet na różnych komputerach, między portfelami z wieloma podpisami oraz do iz portfeli sprzętowych. Oto kilka instrukcji.


Wracając do przycisku "Zapisz" - nie jest to sposób na zapisanie tekstu transakcji. W rzeczywistości powoduje to, że Electrum Wallet rozpoznaje tę transakcję na komputerze lokalnym jako przesłaną jako płatność. Jeśli zrobisz to przez przypadek, zobaczysz transakcję z małą ikoną komputera. Możesz kliknąć prawym przyciskiem myszy i usunąć transakcję - nie martw się, nie możesz usunąć Bitcoin w ten sposób. Electrum zapomni wtedy, że ta transakcja kiedykolwiek miała miejsce i "zwróci" Sats z powrotem i wyświetli Sats w prawidłowej lokalizacji, w której faktycznie istnieją.


### Zmiana adresów


Zmiana adresów jest interesująca. Musisz zrozumieć UTXO, aby zrozumieć to wyjaśnienie. Jeśli wydasz na Address kwotę, która jest mniejsza niż UTXO, wówczas pozostały Bitcoin trafi do Miner, chyba że określono wyjście zmiany.


Możesz mieć 6,15 Bitcoin UTXO i chcieć wydać 0,15 Bitcoin, aby przekazać darowiznę na rzecz protestujących, którzy są uciskani przez despotyczny "demokratyczny" rząd gdzieś na świecie. Następnie wziąłbyś 6,15 Bitcoin (używając funkcji "wydaj z" w Electrum) i umieścił je w transakcji.


Wklejasz Address protestujących w polu "wpłać na", być może wpisujesz "EndTheFed & WEF" w polu "opis", a jako kwotę wpisujesz 0,15 Bitcoin i klikasz "zapłać", a następnie "zaawansowane".


Na ekranie transakcji, w oknie wejściowym, zobaczysz 6,15 Bitcoin UTXO. W oknie wyjściowym zobaczysz Address, który nie ma podświetlenia (jest to Address protestujących) z 0,15 Bitcoin obok niego. Zobaczysz także żółty Address z nieco mniej niż 6,0 Bitcoin. Jest to zmiana Address automatycznie wybrana przez Wallet z jednego z jego własnych żółtych adresów zmiany. Celem zmiany Address jest to, aby Wallet mógł umieścić w nich monety zmiany bez zakłócania dostępności adresów odbiorczych, dla których możesz mieć plany lub wysłać faktury. Jeśli na przykład mają one być później używane przez klientów, nie chcesz, aby Wallet automatycznie z nich korzystał i je zapełniał. Jest to nieporządne i szkodliwe dla prywatności.


Należy pamiętać, że po dostosowaniu opłaty Mining automatycznie dostosowana zostanie kwota wyjściowa zmiany, a nie kwota płatności.


### Ręczna zmiana lub płatność dla wielu


To naprawdę interesująca funkcja Electrum. Dostęp do niej można uzyskać w następujący sposób.


![image](assets/46.webp)


Następnie można wprowadzić wiele miejsc docelowych dla wydawanego salda UTXO, w następujący sposób:


![image](assets/47.webp)


Wklej Address, wpisz przecinek, następnie spację, następnie kwotę, następnie <enter>, a następnie zrób to ponownie. NIE WPROWADZAJ KWOT W OKNIE "KWOTA" - Electrum wypełni tutaj sumę, gdy wpiszesz poszczególne kwoty w oknie "Zapłać do".


Pozwala to na ręczne określenie, gdzie trafia zmiana (np. konkretny Address w Wallet lub inny Wallet), lub możesz zapłacić wielu osobom jednocześnie. Jeśli suma nie jest wystarczająco wysoka, aby dopasować rozmiar UTXO, Electrum nadal utworzy dla Ciebie dodatkowe wyjście zmiany.


Funkcja Pay to Many pozwala również na tworzenie własnych "PayJoins" lub "CoinJoins" - poza zakresem tego artykułu, ale mam przewodnik tutaj. (https://armantheparman.com/cj/)


## Portfele


Chcę zademonstrować usługę Watching Only Wallet przy użyciu Electrum. Aby to zrobić, muszę najpierw zdefiniować "Wallet". Istnieją dwa sposoby użycia "Wallet" w Bitcoin:



- Typ A, "Wallet" - odnosi się do oprogramowania, które pokazuje adresy i salda, np. Electrum, Blue Wallet, Sparrow Wallet itp.



- Typ B, "Wallet" - odnosi się do unikalnej kolekcji adresów, które są powiązane z kombinacją naszego seed_phrase/passphrase/derivation_path. W każdym Wallet znajduje się 8,6 miliarda adresów (4,3 miliarda adresów odbierających i 4,3 miliarda adresów zmieniających). Jeśli zmienisz cokolwiek we frazie seed, passphrase lub ścieżce pochodnej, otrzymasz nieużywany Wallet z nowymi i unikalnymi 8,6 miliardami pustych adresów.


To, do jakiego typu odnosi się każdy, kto używa słowa "Wallet", jest oczywiste w kontekście.


## Oglądanie Wallet - ćwiczenie


Nie jest do końca oczywiste, do czego służy oglądanie Wallet, ale zacznę od wyjaśnienia, czym on jest, jak go wykonać, a następnie wrócimy do jego przeznaczenia później, gdy wyjaśnię więcej na temat portfeli sprzętowych. (Szczegółowy przegląd sposobu korzystania z Hardware Wallet i różnych konkretnych marek można znaleźć tutaj)


Stworzymy atrapę zwykłego Wallet (tym razem dodając nieco więcej złożoności za pomocą passphrase), a następnie odpowiadający mu Wallet do oglądania. Jeśli chcesz, możesz skopiować dokładnie ten zrobiony przeze mnie lub stworzyć własny - ten Wallet należy wyrzucić; nie używaj go. Zacznij od wygenerowania 12-słownego seed, korzystając ze strony internetowej Iana Colemana.


Zwróć uwagę na 12 losowych słów na poniższym zrzucie ekranu oraz na to, że w polu passphrase wpisałem passphrase:


passphrase: "Craig Wright jest kłamcą i oszustem i powinien siedzieć w więzieniu. Również Ross Ulbricht powinien zostać natychmiast zwolniony z więzienia"


passphrase może mieć długość do 100 znaków i idealnie powinien być jednoznaczny i niezbyt krótki - ten, którego użyłem, jest tylko dla zabawy - generalnie sugeruję unikanie wielkich liter i symboli, aby zmniejszyć stres związany z próbowaniem kombinacji, jeśli kiedykolwiek miałeś problem z zapamiętaniem swojego passphrase.


![image](assets/48.webp)


Następnie w Electrum przejdź do menu plik->nowy/przywróć. Wpisz unikalną nazwę, aby utworzyć nowy Wallet i kliknij "dalej".


![image](assets/49.webp)


Kolejne kroki powinieneś już znać, więc wymienię je bez obrazków:



- Standard Wallet
- Mam już seed
- Skopiuj i wklej 12 słów w polu lub wpisz je ręcznie.
- Kliknij opcje i wybierz BIP39, a także kliknij znacznik wyboru passphrase ("rozszerz ten seed o niestandardowe słowa")
- Wprowadź dane passphrase dokładnie tak, jak na stronie Ian Coleman
- Pozostaw domyślną semantykę skryptu i ścieżkę pochodną
- Nie ma potrzeby dodawania hasła (blokuje Wallet)


Teraz wróć do strony Iana Colemana, przejdź do sekcji "derivation path" i kliknij zakładkę "BIP 84", aby wybrać tę samą semantykę skryptu, co domyślna w Electrum (Native SegWit).


![image](assets/50.webp)


Rozszerzone klucze prywatne i publiczne znajdują się tuż poniżej i zmieniają się po wprowadzeniu zmian w ścieżce derywacji (lub czymkolwiek innym na górze strony).


![image](assets/51.webp)


Zobaczysz również klucze "BIP32 extended private/public" - na razie należy je zignorować.


Rozszerzony klucz prywatny konta może być użyty do pełnej regeneracji Wallet. Rozszerzony klucz publiczny konta może jednak generować tylko ograniczoną wersję tego samego Wallet (oglądanie Wallet) - jeśli umieścisz ten klucz w Electrum, nadal będzie on generował wszystkie 8,6 miliarda adresów, które miałby seed lub rozszerzony klucz prywatny, ale nie będzie żadnych kluczy prywatnych dostępnych dla Electrum, więc nie będzie możliwe wydawanie pieniędzy. Zróbmy to teraz, aby zademonstrować ten punkt:


Skopiuj "rozszerzony klucz publiczny konta" do schowka.


Następnie przejdź do Electrum, pozostaw otwarty bieżący Wallet i przejdź do file->new/restore. Proces tworzenia Wallet jest nieco inny niż poprzednio:



- Standard Wallet
- Korzystanie z klucza głównego
- Wklej rozszerzony klucz publiczny w polu i kontynuuj
- Nie ma potrzeby wprowadzania passphrase; jest on już częścią rozszerzonego klucza publicznego
- Nie ma potrzeby wprowadzania semantyki skryptu i ścieżki pochodnej
- Nie ma potrzeby dodawania hasła (blokuje Wallet)


Po załadowaniu Wallet powinieneś zauważyć, że ładowane są dokładnie te same adresy, co poprzednio, gdy wprowadzono seed. Powinieneś również zauważyć, że na samej górze na pasku tytułu widnieje napis "oglądanie Wallet". Ten Wallet może pokazywać adresy i salda (sprawdzając salda za pośrednictwem węzła), ale nie można PODPISYWAĆ transakcji (ponieważ obserwowany Wallet nie ma kluczy prywatnych).


Więc jaki to ma sens?


Jednym z powodów, ale nie najważniejszym, jest to, że można potencjalnie obserwować Wallet i jego saldo na komputerze bez narażania kluczy prywatnych na złośliwe oprogramowanie na komputerze.


Innym jest to, że jest to WYMAGANE do dokonywania płatności, jeśli zdecydujesz się trzymać swoje klucze prywatne poza komputerem; wyjaśnię to:


**Portfele sprzętowe (HWW)** zostały stworzone, aby urządzenie mogło bezpiecznie przechowywać klucze prywatne (zablokowane kodem PIN), nigdy nie ujawniać kluczy komputerowi (nawet po podłączeniu do komputera za pomocą kabla) i same nie są w stanie połączyć się z Internetem. Takie urządzenie nie może samodzielnie dokonywać transakcji, ponieważ wszystkie transakcje Bitcoin rozpoczynają się od odniesienia do UTXO(s) na Blockchain (który znajduje się na węźle). Wallet musi określić, w którym transaction ID znajduje się UTXO i które wyjście transakcji jest tym, które ma zostać wydane. Dopiero po określeniu danych wejściowych można w ogóle utworzyć nową transakcję, nie mówiąc już o jej podpisaniu. Portfele sprzętowe nie mogą tworzyć transakcji, ponieważ nie mają dostępu do żadnych UTXO - nie są z niczym połączone!


Rozszerzony klucz publiczny jest zwykle wyodrębniany z HWW, a adresy są następnie wyświetlane na komputerze - wiele osób zna oprogramowanie Ledger lub Trezor Suite wyświetlające adresy i salda na komputerze - jest to oglądanie Wallet. Programy te mogą tworzyć transakcje, ale nie mogą ich podpisywać. Transakcje mogą być podpisywane tylko przez HWW, które są z nimi połączone. HWW pobiera nowo wygenerowaną transakcję z obserwującego Wallet, podpisuje ją, a następnie wysyła z powrotem do komputera w celu rozesłania do węzła. **HWW nie może nadawać samodzielnie**, robi to powiązany z nim obserwujący Wallet. W ten sposób dwa portfele (klucz publiczny Wallet na komputerze i klucz prywatny Wallet w HWW) współpracują w celu generate, podpisywania i nadawania, jednocześnie upewniając się, że klucze prywatne pozostają odizolowane i z dala od urządzenia podłączonego do Internetu.


## Częściowo podpisane transakcje Bitcoin (PSBT)


Możliwe jest utworzenie transakcji i zapisanie jej w pliku, późniejsze ponowne załadowanie, podpisanie, zapisanie, późniejsze ponowne załadowanie, a następnie ostateczne rozesłanie - nie twierdzę, że ktokolwiek musiałby to robić; to po prostu coś, co jest możliwe.


Rozważmy teraz wielopodpisowy Wallet 3 z 5 - 5 kluczy prywatnych tworzy Wallet, a 3 są potrzebne do pełnego podpisania transakcji (zobacz tutaj, aby dowiedzieć się więcej o wielopodpisowych kluczach Wallet). Możliwe jest posiadanie 5 różnych komputerów, z których każdy ma jeden z pięciu kluczy prywatnych.


Komputer nr 1 może dokonać transakcji generate i podpisać ją. Następnie może zapisać ją w pliku i wysłać e-mailem do komputera 2. Komputer 2 może następnie podpisać i potencjalnie zapisać plik do kodu QR i przesłać QR za pośrednictwem połączenia Zoom do komputera 3 po drugiej stronie świata. Komputer 3 może przechwycić QR, załadować transakcję do Electrum i podpisać transakcję. Po pierwszych 2 podpisach transakcja była PSBT (Partially Signed Bitcoin Transaction). Po trzecim podpisie transakcja stała się w pełni podpisana i ważna, gotowa do transmisji.


Aby dowiedzieć się więcej o PSBTS, zobacz ten przewodnik. (https://armantheparman.com/PSBT/)


## Korzystanie z portfeli sprzętowych z Electrum


Mam przewodnik na temat ogólnego korzystania z portfeli sprzętowych, który moim zdaniem byłby ważny dla osób, które dopiero zaczynają korzystać z HWW. (https://armantheparman.com/using-hwws/)


Istnieją również przewodniki dotyczące różnych marek HWW podłączanych do Sparrow Bitcoin Wallet, które można znaleźć tutaj. (https://armantheparman.com/hwws/)


To będzie mój pierwszy przewodnik pokazujący, jak używać Hardware Wallet z Electrum - do demonstracji użyję ColdCard Hardware Wallet. Nie ma to być szczegółowy przewodnik po ColdCard, który można znaleźć tutaj. Pokazuję tylko punkty specyficzne dla Electrum. (https://armantheparman.com/cc/)


### Podłączanie za pomocą karty micro SD (air-gapped)


Przed podłączeniem prawdziwego Wallet przez ColdCard, mam nadzieję, że przeszedłeś przez wcześniejsze kroki ładowania atrapy Electrum Wallet i ustawiania parametrów sieci.


Następnie w ColdCard włóż kartę SD. Zakładam, że seed został już utworzony. Jeśli uzyskujesz dostęp do Wallet za pomocą passphrase, zastosuj go teraz. Przewiń w dół i wybierz menu Zaawansowane/Narzędzia ->Eksportuj Wallet -> Electrum Wallet.


Możesz przewinąć w dół i przeczytać wiadomość. Zawsze oferuje wybór "1", aby wprowadzić niezerowy numer konta (coś, co jest częścią ścieżki derywacji), ale jeśli zastosowałeś się do mojej rady, nie zepsułeś domyślnych ścieżek derywacji, więc nie będziesz chciał niezerowego numeru konta; po prostu naciśnij znacznik wyboru, aby kontynuować.


Następnie wybierz semantykę skryptu. Większość osób wybierze "Native SegWit".


Pojawi się komunikat "Zapisano plik Electrum Wallet" i nazwa pliku. Zanotuj ją w pamięci.


Następnie wyjmij kartę micro SD i włóż ją do komputera z Electrum.


Niektóre systemy operacyjne automatycznie otworzą eksplorator plików po włożeniu karty microSD. Wiele osób zobaczy nowy plik Wallet, kliknie go dwukrotnie i będzie się zastanawiać, dlaczego nie działa. To nie jest dobry projekt. W rzeczywistości należy zignorować eksplorator plików (zamknąć go) i otworzyć plik Wallet za pomocą Electrum:


Otwórz Electrum. Jeśli jest już otwarty z innym Wallet, wybierz plik -> nowy. Szukamy tego okna:


![image](assets/52.webp)


Oto sztuczka, która nie jest intuicyjna. Kliknij "wybierz". Następnie przejdź do systemu plików na karcie microSD, znajdź plik Wallet i otwórz go.


Teraz otworzyłeś swoje Hardware Wallet odpowiadające oglądaniu Wallet. Ładnie.


### Podłączanie za pomocą kabla USB.


Ten sposób powinien być łatwiejszy, ale w przypadku komputerów z systemem Linux jest to znacznie trudniejsze. Należy zaktualizować coś, co nazywa się "Udev rules". Oto jak to zrobić (szczegółowy przewodnik https://armantheparman.com/gpg-articles/ ) i pokrótce:


Warto upewnić się, że system jest aktualny. Następnie:


```bash
sudo apt-get install libusb-1.0-0-dev libudev-dev
```


wtedy...


```bash
python3 -m pip install ckcc-protocol
```


Jeśli pojawi się błąd, upewnij się, że pip jest zainstalowany. Można to sprawdzić za pomocą (pip -version), a zainstalować za pomocą (sudo apt install pythron3-pip)


Utwórz lub zmodyfikuj istniejący plik /etc/udev/rules.d/


Na przykład to:


```bash
sudo nano /etc/udev/rules.d
```


Otworzy się edytor tekstu. Skopiuj tekst z tego miejsca i wklej go do pliku rules.d, zapisz i wyjdź.


![image](assets/53.webp)


Następnie uruchom te polecenia jedno po drugim:


```bash
sudo groupadd plugdev
sudo usermod -aG plugdev $(whoami)
sudo udevadm control –reload-rules && sudo udevadm trigger
```


Jeśli pojawi się komunikat "grupa plugdev" już istnieje, to w porządku, kontynuuj. Po drugim poleceniu nie otrzymasz żadnej informacji zwrotnej/odpowiedzi, po prostu przejdź do trzeciego polecenia.


Konieczne może być odłączenie, a następnie ponowne podłączenie karty ColdCard do komputera.


Jeśli po tym wszystkim nadal nie możesz podłączyć ColdCard, spróbowałbym zaktualizować oprogramowanie układowe (przewodnik wkrótce, ale na razie instrukcje można znaleźć na stronie producenta).


Następnie utwórz nowy Wallet:



- Standard Wallet
- Korzystanie z urządzenia sprzętowego
- Aplikacja przeskanuje i wykryje kartę ColdCard. Kontynuuj.
- Wybór semantyki skryptu i ścieżki wyprowadzania
- Zaszyfrowanie pliku Wallet (zalecane)


### Transakcje przy użyciu karty ColdCard


Po podłączeniu kabla transakcje są łatwe. Podpisywanie transakcji będzie bezproblemowe.


W przypadku korzystania z urządzenia w trybie air-gapped należy ręcznie przekazywać zapisane transakcje między urządzeniami za pomocą karty microSD. Istnieje kilka sztuczek.


Po utworzeniu i sfinalizowaniu transakcji należy kliknąć przycisk eksportu w lewym dolnym rogu. Zobaczysz "zapisz do pliku", co wbrew intuicji nie jest tym, czego chcemy. W rzeczywistości należy najpierw przejść do ostatniej opcji menu, która mówi "dla portfeli sprzętowych", a następnie, w ramach tego wyboru, znaleźć drugą opcję "zapisz do pliku" i wybrać ją. Następnie zapisz plik na karcie microSD, wyjmij kartę i włóż ją do ColdCard. Pamiętaj, że może być konieczne zastosowanie passphrase, aby wybrać prawidłowy Wallet. Na ekranie pojawi się komunikat o gotowości do podpisania. Kliknij znacznik wyboru, sprawdź transakcję i kontynuuj, potwierdzając znacznikiem wyboru. Po zakończeniu wyjmij kartę i włóż ją z powrotem do komputera.


Następnie musimy otworzyć transakcję za pomocą electrum. Funkcja jest ukryta w menu narzędzia -> załaduj transakcję. Przejdź do systemu plików i znajdź plik. Przy każdym podpisie będą trzy pliki. Oryginalny zapisany plik utworzony przez Watching Wallet i dwa utworzone przez ColdCard (nie wiem, dlaczego tak się dzieje). Jeden będzie miał napis "podpisany", a drugi "ostateczny". Nie jest to intuicyjne, ale ten "podpisany" nie jest użyteczny, musimy otworzyć "ostateczną" transakcję.


Po załadowaniu możesz kliknąć "nadaj", a płatność zostanie zrealizowana.


## Aktualizacja Electrum i ukryty katalog ".electrum"


Electrum znajduje się na komputerze w dwóch miejscach. Jest tam sama aplikacja i ukryty folder konfiguracyjny. Folder ten znajduje się w różnych miejscach w zależności od systemu operacyjnego:


Windows:


```bash
C:/Users/your_user_name_goes_here/AppData/Roaming/Electrum
```


Mac:


```bash
/Users/your_user_name_goes_here/.electrum
```


Linux:


```bash
/home/your_user_name_goes_here/.electrum
```


Zwróć uwagę na `.` przed `electrum` w Linuksie i Macu - oznacza to, że reżyser jest ukryty. Należy również pamiętać, że katalog ten jest tworzony (automatycznie) dopiero po pierwszym uruchomieniu Electrum. Katalog zawiera plik konfiguracyjny Electrum, a także katalog, w którym znajdują się zapisane portfele.


Jeśli usuniesz program Electrum z komputera, ukryty katalog pozostanie, chyba że aktywnie go usuniesz.


Aby zaktualizować electrum, należy przejść przez tę samą procedurę, którą opisałem na początku, aby pobrać i zweryfikować. Następnie będziesz mieć dwie kopie programu na swoim komputerze i możesz uruchomić dowolną z nich - każdy program uzyska dostęp do tego samego ukrytego folderu electrum w celu konfiguracji i dostępu do Wallet. Wszystkie rzeczy, które zapisaliśmy, takie jak jednostka bazowa, domyślny węzeł do połączenia, inne preferencje i dostęp do portfeli, pozostaną, ponieważ wszystko to jest zapisane w tym folderze.


### Przenoszenie Electrum i portfeli na inny komputer


W tym celu można skopiować pliki programu na dysk USB, a także skopiować katalog .electrum. Następnie skopiuj lub przenieś je na nowy komputer. Nie ma potrzeby ponownej weryfikacji programu. Upewnij się, że skopiowałeś katalog .electrum do domyślnej lokalizacji (pamiętaj, aby skopiować go PRZED pierwszym uruchomieniem Electrum na tym komputerze, w przeciwnym razie zostanie wypełniony pusty domyślny folder .electrum i możesz się pomylić).


## Etykiety


Jak wyjaśniłem wcześniej, na karcie Address znajduje się kolumna etykiet. Można tam kliknąć dwukrotnie i wprowadzić własne notatki (tylko na swoim komputerze, nie publicznie i nie na Blockchain).


![image](assets/54.webp)


Przenosząc urządzenie Electrum Wallet na inny komputer, nie można utracić wszystkich tych notatek. Można utworzyć ich kopię zapasową w pliku za pomocą menu Wallet > etykiety > eksport, a następnie na nowym komputerze użyć Wallet > etykiety > import.


## Wskazówki:


Jeśli uważasz ten zasób za przydatny i chciałbyś wesprzeć to, co robię dla Bitcoin, możesz przekazać trochę Sats tutaj:


Statyczny piorun Address: dandysack84@walletofsatoshi.com

https://armantheparman.com/electrum/