---
name: COLDCARD Q
description: Konfigurowanie i używanie karty COLDCARD Q
---
![cover](assets/cover.webp)


Hardware Wallet to urządzenie elektroniczne przeznaczone do zarządzania i zabezpieczania kluczy prywatnych Bitcoin Wallet. W przeciwieństwie do portfeli programowych (lub portfeli Hot) instalowanych na maszynach ogólnego przeznaczenia często podłączonych do Internetu, portfele sprzętowe umożliwiają fizyczne odizolowanie kluczy prywatnych, zmniejszając ryzyko piractwa i kradzieży.


Głównym celem Hardware Wallet jest maksymalne ograniczenie funkcjonalności urządzenia w celu zminimalizowania jego powierzchni ataku. Mniejsza powierzchnia ataku oznacza również mniej potencjalnych wektorów ataku, tj. mniej słabych punktów w systemie, które atakujący mogliby wykorzystać, aby uzyskać dostęp do bitcoinów.


Zaleca się korzystanie z Hardware Wallet w celu zabezpieczenia bitcoinów, zwłaszcza jeśli posiadasz ich duże ilości, zarówno pod względem wartości bezwzględnej, jak i proporcji do całkowitych aktywów.


Portfele sprzętowe są używane w połączeniu z oprogramowaniem zarządzającym Wallet na komputerze lub smartfonie. To ostatnie zarządza tworzeniem transakcji, ale podpis kryptograficzny wymagany do nadania ważności tym transakcjom jest wykonywany wyłącznie w Hardware Wallet. Oznacza to, że klucze prywatne nigdy nie są narażone na potencjalnie wrażliwe środowisko.


Portfele sprzętowe oferują podwójną ochronę dla użytkownika: z jednej strony zabezpieczają bitcoiny przed zdalnymi atakami, utrzymując klucze prywatne w trybie offline, a z drugiej strony generalnie oferują większą fizyczną odporność na próby wyodrębnienia kluczy. I to właśnie na podstawie tych 2 kryteriów bezpieczeństwa możemy ocenić i sklasyfikować różne modele dostępne na rynku.


W tym poradniku chciałbym przedstawić jedno z takich rozwiązań: **COLDCARD Q**.


---
Ponieważ COLDCARD Q oferuje wiele funkcji, proponuję podzielić jego użycie na 2 samouczki. W pierwszym tutorialu przyjrzymy się początkowej konfiguracji i podstawowym funkcjom urządzenia. Następnie, w drugim samouczku, przyjrzymy się, jak wykorzystać wszystkie zaawansowane opcje karty COLDCARD.


https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

---
## Przedstawiamy COLDCARD Q


COLDCARD Q to Bitcoin opracowany przez kanadyjską firmę Coinkite, znaną z poprzednich modeli MK. Q reprezentuje ich najbardziej zaawansowany produkt do tej pory i jest pozycjonowany jako ostateczny Bitcoin Hardware Wallet.


Pod względem sprzętowym COLDCARD Q jest wyposażony we wszystkie funkcje wymagane do optymalnego doświadczenia użytkownika:




- Duży wyświetlacz LCD ułatwia nawigację i obsługę;
- Pełna klawiatura QWERTY;
- Zintegrowana kamera do skanowania kodów QR;
- Dwa gniazda kart microSD;
- W pełni izolowana opcja zasilania za pomocą trzech baterii AAA (brak w zestawie) lub za pomocą kabla USB-C;
- Dwa bezpieczne Elements od dwóch różnych producentów dla dodatkowego bezpieczeństwa;
- Możliwość komunikacji za pośrednictwem NFC.


Moim zdaniem COLDCARD Q ma tylko dwie wady. Po pierwsze, ze względu na wiele funkcji, jest dość nieporęczny, mierząc prawie 13 cm długości i 8 cm szerokości, czyli prawie wielkości małego smartfona. Jest również dość gruby ze względu na komorę baterii. Jeśli szukasz mniejszego, bardziej mobilnego Hardware Wallet, znacznie bardziej kompaktowy MK4 może być lepszą opcją. Drugą wadą jest oczywiście cena urządzenia, która na oficjalnej stronie wynosi 239,99 USD, czyli o 72 USD więcej niż MK4, co stawia Q w bezpośredniej konkurencji z portfelami sprzętowymi premium, takimi jak Ledger Flex lub Foundation's Passport.


![CCQ](assets/fr/001.webp)


Od strony oprogramowania, COLDCARD Q jest tak samo dobrze wyposażony jak inne urządzenia Coinkite, z wieloma zaawansowanymi funkcjami:




- Rzut kostką, aby generate własną frazę odzyskiwania;
- Kod PIN ;
- Odliczanie do ostatecznej blokady PIN;
- BIP39 passphrase ;
- PIN blokady końcowej ;
- Odliczanie połączenia ;
- SeedXOR;
- BIP85...


Krótko mówiąc, COLDCARD Q oferuje lepsze wrażenia użytkownika w porównaniu do MK4 i może być idealnym rozwiązaniem dla średnio zaawansowanych i zaawansowanych użytkowników poszukujących większej łatwości użytkowania.


COLDCARD Q jest dostępny w sprzedaży [na oficjalnej stronie Coinkite] (https://store.coinkite.com/store/coldcard). Można ją również nabyć u sprzedawcy detalicznego.


## Przygotowanie samouczka


Po otrzymaniu karty COLDCARD pierwszym krokiem jest sprawdzenie opakowania, aby upewnić się, że nie zostało ono otwarte. Jeśli opakowanie jest uszkodzone, może to oznaczać, że karta Hardware Wallet została naruszona i może nie być oryginalna.


![CCQ](assets/fr/002.webp)


Po otwarciu pudełka powinieneś znaleźć następujące elementy:




- Karta COLDCARD Q znajduje się w zapieczętowanej torbie;
- Karta do zapisania frazy Mnemonic.


![CCQ](assets/fr/003.webp)


Upewnij się, że torba nie została rozpieczętowana lub uszkodzona. Sprawdź również, czy numer na torbie jest zgodny z numerem na papierze wewnątrz torby. Zachowaj ten numer na przyszłość.


![CCQ](assets/fr/004.webp)


Jeśli wolisz zasilać kartę COLDCARD bez podłączania jej do komputera (air-gap), włóż trzy baterie AAA z tyłu urządzenia. Alternatywnie można podłączyć ją do komputera za pomocą kabla USB-C.


![CCQ](assets/fr/005.webp)


Do tego samouczka potrzebny będzie również Sparrow Wallet do zarządzania Bitcoin Wallet na komputerze. Pobierz [Sparrow Wallet](https://sparrowwallet.com/download/) z oficjalnej strony internetowej. Zdecydowanie zalecam sprawdzenie zarówno jego autentyczności (za pomocą GnuPG), jak i integralności (za pomocą Hash) przed przystąpieniem do instalacji. Jeśli nie wiesz, jak to zrobić, postępuj zgodnie z tym samouczkiem:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Wybór kodu PIN


Teraz można włączyć kartę COLDCARD, naciskając przycisk w lewym górnym rogu.


![CCQ](assets/fr/006.webp)


Naciśnij przycisk "*ENTER*", aby zaakceptować warunki użytkowania.


![CCQ](assets/fr/007.webp)


Karta COLDCARD Q wyświetli numer w górnej części ekranu. Upewnij się, że numer ten zgadza się z numerem na zapieczętowanej torbie i na kawałku plastiku wewnątrz torby. Gwarantuje to, że paczka nie była otwierana między zapakowaniem przez Coinkite a otwarciem przez użytkownika. Naciśnij "*ENTER*", aby kontynuować.


![CCQ](assets/fr/008.webp)


Przejdź do menu "*Choose PIN Code*" i potwierdź przyciskiem "*ENTER*".


![CCQ](assets/fr/009.webp)


Ten kod PIN służy do odblokowania karty COLDCARD. Stanowi on zatem zabezpieczenie przed nieautoryzowanym dostępem fizycznym. Ten kod PIN nie bierze udziału w tworzeniu kluczy kryptograficznych Wallet. Tak więc, nawet bez dostępu do tego kodu PIN, posiadanie frazy Mnemonic umożliwi odzyskanie dostępu do bitcoinów.


Kody PIN COLDCARD składają się z dwóch części: prefiksu i sufiksu, z których każdy może zawierać od 2 do 6 cyfr, co daje łącznie od 4 do 12 cyfr. Podczas odblokowywania karty COLDCARD należy najpierw wprowadzić prefiks, po czym urządzenie wyświetli 2 słowa. Następnie należy wprowadzić sufiks. Te dwa słowa zostaną podane podczas tego etapu konfiguracji i należy je starannie zapisać, ponieważ będą potrzebne przy każdym odblokowaniu karty COLDCARD. Jeśli dwa słowa wyświetlone podczas odblokowywania są zgodne z tymi zapisanymi podczas konfiguracji, potwierdzi to, że urządzenie nie zostało naruszone od czasu jego ostatniego użycia.


Kliknij ponownie na "*Wybierz PIN*"


![CCQ](assets/fr/010.webp)


Potwierdź, że przeczytałeś ostrzeżenia.


![CCQ](assets/fr/011.webp)


Teraz należy wybrać kod PIN. Zalecamy wybranie długiego, losowego kodu PIN. Kod ten należy przechowywać w innym miejscu niż karta COLDCARD. Możesz użyć karty dostarczonej w paczce, aby zapisać ten kod.


Wprowadź wybrany prefiks, a następnie naciśnij przycisk "*ENTER*", aby potwierdzić pierwszą część kodu PIN.


![CCQ](assets/fr/012.webp)


Na ekranie zostaną wyświetlone dwa słowa antyphishingowe. Zapisz je uważnie na przyszłość. Możesz użyć karty dołączonej do pakietu, aby je zapisać.


![CCQ](assets/fr/013.webp)


Następnie wprowadź drugą część kodu PIN i naciśnij "*ENTER*".


![CCQ](assets/fr/014.webp)


Potwierdź kod PIN, wprowadzając go po raz drugi, sprawdzając, czy dwa słowa antyphishingowe są zgodne z tymi, które zapisałeś wcześniej.


![CCQ](assets/fr/015.webp)


Od teraz, za każdym razem, gdy odblokujesz kartę COLDCARD, pamiętaj, aby sprawdzić ważność dwóch słów antyphishingowych, które pojawiają się na ekranie po wprowadzeniu prefiksu kodu PIN.


## Aktualizacja oprogramowania sprzętowego


Podczas korzystania z urządzenia po raz pierwszy należy sprawdzić i zaktualizować oprogramowanie sprzętowe. W tym celu należy przejść do menu "*Zaawansowane/Narzędzia*".


![CCQ](assets/fr/016.webp)


**Ważne:** Jeśli planujesz aktualizację oprogramowania sprzętowego i nie jest to Twoje pierwsze użycie COLDCARD (tj. masz już Wallet utworzony na COLDCARD), upewnij się, że masz frazę Mnemonic i że jest ona funkcjonalna (a także opcjonalny passphrase, jeśli dotyczy). Jest to ważne, aby uniknąć utraty bitcoinów w przypadku wystąpienia problemu podczas aktualizacji urządzenia.


Wybierz opcję "*Upgrade Firmware*".


![CCQ](assets/fr/017.webp)


Wybierz opcję "*Pokaż wersję*".


![CCQ](assets/fr/018.webp)


Można sprawdzić aktualną wersję oprogramowania sprzętowego karty COLDCARD. Na przykład w moim przypadku jest to wersja "*1.2.3Q*".


![CCQ](assets/fr/019.webp)


Sprawdź [na oficjalnej stronie COLDCARD](https://coldcard.com/downloads), czy dostępna jest nowsza wersja. Kliknij "*Download*", aby pobrać nowe oprogramowanie sprzętowe.


![CCQ](assets/fr/020.webp)


W tym momencie zdecydowanie zalecamy sprawdzenie integralności i autentyczności pobranego oprogramowania układowego. W tym celu należy pobrać [dokument zawierający skróty wszystkich wersji, podpisany przez deweloperów](https://raw.githubusercontent.com/Coldcard/firmware/master/releases/signatures.txt), zweryfikować podpis za pomocą [klucza publicznego dewelopera](https://keybase.io/dochex) i upewnić się, że Hash wskazany w podpisanym dokumencie jest zgodny z oprogramowaniem pobranym ze strony. Jeśli wszystko się zgadza, można przystąpić do aktualizacji.


Jeśli nie jesteś zaznajomiony z tym procesem weryfikacji, zalecam skorzystanie z tego samouczka:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Weź kartę microSD i przenieś na nią plik oprogramowania sprzętowego (dokument w formacie `.dfu`). Włóż kartę microSD do jednego z portów COLDCARD.


![CCQ](assets/fr/021.webp)


Następnie w menu aktualizacji oprogramowania sprzętowego wybierz opcję "*Z MicroSD*".


![CCQ](assets/fr/022.webp)


Wybierz plik odpowiadający oprogramowaniu sprzętowemu.


![CCQ](assets/fr/023.webp)


Potwierdź wybór, naciskając przycisk "*ENTER*".


![CCQ](assets/fr/024.webp)


Poczekaj na aktualizację oprogramowania sprzętowego.


![CCQ](assets/fr/025.webp)


Po zakończeniu aktualizacji wprowadź kod PIN, aby odblokować urządzenie.


![CCQ](assets/fr/026.webp)


Oprogramowanie sprzętowe jest teraz aktualne.


## Parametry COLDCARD Q


Jeśli chcesz, możesz zapoznać się z ustawieniami karty COLDCARD, przechodząc do menu "*Ustawienia*".


![CCQ](assets/fr/027.webp)


W tym menu znajdziesz różne opcje dostosowywania, takie jak ustawienie jasności ekranu lub wybór domyślnej jednostki miary.


![CCQ](assets/fr/028.webp)


Innym zaawansowanym ustawieniom przyjrzymy się w następnym samouczku:


https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

## Tworzenie Bitcoin Wallet


Teraz nadszedł czas na generate nowego Bitcoin Wallet! Aby to zrobić, należy utworzyć frazę Mnemonic. W Coldcard dostępne są trzy metody generowania tej frazy:




- Używaj tylko wewnętrznego generatora liczb losowych (TRNG);
- Użyj kombinacji TRNG i rzutu kostką, aby dodać entropię;
- Używaj tylko rzutów kostką.


**Dla początkujących i średnio zaawansowanych użytkowników zalecamy korzystanie wyłącznie z wewnętrznego generatora liczb losowych COLDCARD**


Nie polecam opcji tylko kości, ponieważ złe wykonanie może prowadzić do wyroku z niewystarczającą entropią, zagrażając bezpieczeństwu Wallet.


Jednak najlepszą opcją jest z pewnością druga, która łączy użycie TRNG z zewnętrznym źródłem entropii. Metoda ta gwarantuje minimalną entropię równoważną entropii samego TRNG i dodaje dodatkowy poziom bezpieczeństwa w przypadku ewentualnej awarii wewnętrznego generatora (dobrowolnej lub nie). Wybierając tę opcję, która łączy TRNG i rzucanie kośćmi, zyskujesz większą kontrolę nad generowaniem zdań, bez zwiększania ryzyka w przypadku złej realizacji z Twojej strony.


Kliknij "*Nowe słowa seed*".


![CCQ](assets/fr/029.webp)


Możesz wybrać długość swojego wyroku. Zalecam wybranie zdania składającego się z 12 słów, ponieważ jest ono mniej skomplikowane w zarządzaniu i zapewnia nie mniejsze bezpieczeństwo Wallet niż zdanie składające się z 24 słów.


![CCQ](assets/fr/030.webp)


Następnie COLDCARD wyświetli wygenerowaną przez TRNG frazę odzyskiwania. Jeśli chcesz dodać dodatkową entropię zewnętrzną, naciśnij przycisk "*4*".


![CCQ](assets/fr/031.webp)


Spowoduje to przejście do strony, na której można dodać entropię, rzucając kośćmi. Wykonaj tak wiele rzutów, jak to możliwe (zalecane jest minimum 50, ale mniej nie jest dużym problemem, ponieważ już korzystasz z entropii TRNG) i zapisz wyniki za pomocą klawiszy od "*1*" do "*6*". Po zakończeniu naciśnij "*ENTER*", aby potwierdzić.


![CCQ](assets/fr/032.webp)


Wyświetlona zostanie nowa fraza Mnemonic, oparta na entropii, którą właśnie podałeś i entropii TRNG.


**Ostrzeżenie: Ten Mnemonic daje pełny, nieograniczony dostęp do wszystkich bitcoinów**. Każdy, kto posiada tę frazę, może ukraść twoje środki, nawet bez fizycznego dostępu do COLDCARD. 12-wyrazowa fraza przywraca dostęp do bitcoinów w przypadku utraty, kradzieży lub uszkodzenia karty COLDCARD. Dlatego bardzo ważne jest, aby zachować ją ostrożnie i przechowywać w bezpiecznym miejscu.


Możesz zapisać go na kartonie dołączonym do karty COLDCARD lub dla większego bezpieczeństwa zalecam wygrawerowanie go na wsporniku ze stali nierdzewnej, aby chronić go przed ryzykiem pożaru, powodzi lub zawalenia. W każdym razie nigdy nie zapisuj go na nośniku cyfrowym, w przeciwnym razie możesz stracić swoje bitcoiny.


Zapisz słowa wyświetlone na ekranie na wybranym nośniku fizycznym. W zależności od strategii bezpieczeństwa możesz rozważyć wykonanie kilku pełnych fizycznych kopii zdania (ale przede wszystkim nie dziel go). Ważne jest, aby słowa były ponumerowane i ułożone w kolejności.


Oczywiście, **nie wolno udostępniać tych słów** w Internecie, w przeciwieństwie do tego samouczka. Ta próbka Wallet będzie używana tylko na Testnet i zostanie usunięta po zakończeniu samouczka.


Po zapisaniu słów naciśnij "*ENTER*".


![CCQ](assets/fr/033.webp)


Aby upewnić się, że fraza została poprawnie zapisana, system poprosi o potwierdzenie niektórych słów. Wybierz numer odpowiadający każdemu słowu na klawiaturze.


![CCQ](assets/fr/034.webp)


Twój Wallet został utworzony! W prawym górnym rogu ekranu widoczny jest odcisk palca głównego klucza prywatnego. Naciśnij "*ENTER*".


![CCQ](assets/fr/035.webp)


Nastąpił dostęp do menu głównego karty COLDCARD.


![CCQ](assets/fr/036.webp)


## Konfiguracja nowego Wallet na Sparrow


Istnieje kilka opcji nawiązania komunikacji między oprogramowaniem Sparrow Wallet a kartą COLDCARD. Najprostszą z nich jest użycie kabla USB-C. Jednak domyślnie karta COLDCARD ma wyłączoną komunikację kablową i NFC. Aby je ponownie aktywować, przejdź do "*Ustawienia*", a następnie "*Włączanie/wyłączanie sprzętu*" i aktywuj żądaną opcję komunikacji.


![CCQ](assets/fr/037.webp)


Jeśli wolisz całkowicie odizolować kartę COLDCARD od komputera, możesz wybrać pośrednią komunikację "air-gap", używając kodów QR lub karty microSD. Jest to metoda, której będziemy używać w tym samouczku.


Przejdź do "*Zaawansowane/Narzędzia*".


![CCQ](assets/fr/038.webp)


Wybierz "*Export Wallet*".


![CCQ](assets/fr/039.webp)


Następnie wybierz "*Sparrow Wallet*".


![CCQ](assets/fr/040.webp)


Naciśnij "*ENTER*", aby generate plik konfiguracyjny.


![CCQ](assets/fr/041.webp)


Następnie wybierz sposób wysłania tego pliku do Sparrow. W tym przykładzie włożyłem kartę microSD do gniazda "*A*", więc wybiorę przycisk "*1*". Możesz również wyświetlić informacje jako kod QR na ekranie COLDCARD, naciskając przycisk "*QR*" i skanując ten kod QR za pomocą kamery internetowej komputera.


![CCQ](assets/fr/042.webp)


Uruchom Sparrow Wallet i pomiń strony wprowadzające, aby przejść do ekranu głównego. Upewnij się, że jesteś prawidłowo podłączony do węzła, sprawdzając przełącznik w prawym dolnym rogu ekranu.


![CCQ](assets/fr/043.webp)


Zdecydowanie zaleca się korzystanie z własnego węzła Bitcoin. W tym samouczku korzystam z węzła publicznego (żółty), ponieważ jestem na Testnet, ale do użytku produkcyjnego najlepiej jest używać Bitcoin Core lokalnie (Green) lub serwera Electrum na węźle zdalnym (niebieski).


Wejdź do menu "*File*" i wybierz "*New Wallet*".


![CCQ](assets/fr/044.webp)


Nazwij swój Wallet i kliknij "*Create Wallet*".


![CCQ](assets/fr/045.webp)


W menu rozwijanym "*Typ skryptu*" wybierz typ skryptu, który zabezpieczy twoje bitcoiny.


![CCQ](assets/fr/046.webp)


Kliknij na "*Airgapped Hardware Wallet*".


![CCQ](assets/fr/047.webp)


W zakładce "*Coldcard*" kliknij "*Scan...*", jeśli planujesz zeskanować kod QR wyświetlany na karcie COLDCARD, lub "*Import File...*", aby zaimportować plik z microSD (jest to plik `.json`).


![CCQ](assets/fr/048.webp)


Po zaimportowaniu sprawdź, czy "*Master fingerprint*" wyświetlany w aplikacji Sparrow jest zgodny z odciskiem wyświetlanym na karcie COLDCARD. Potwierdź utworzenie, klikając "*Apply*".


![CCQ](assets/fr/049.webp)


Ustaw silne hasło, aby zabezpieczyć dostęp do Sparrow Wallet. Hasło to będzie chronić klucze publiczne, adresy, tagi i historię transakcji przed nieautoryzowanym dostępem.


Dobrym pomysłem jest zapisanie tego hasła, aby go nie zapomnieć (np. w menedżerze haseł).


![CCQ](assets/fr/050.webp)


Twój Wallet jest teraz skonfigurowany na Sparrow Wallet.


![CCQ](assets/fr/051.webp)


Przed otrzymaniem pierwszych bitcoinów w Wallet, **zalecam wykonanie testu odzyskiwania pustej karty**. Zapisz informacje referencyjne, takie jak xpub, a następnie zresetuj COLDCARD Q, gdy Wallet jest nadal pusty. Następnie spróbuj przywrócić Wallet na COLDCARD przy użyciu papierowych kopii zapasowych. Sprawdź, czy xpub wygenerowany po przywróceniu jest zgodny z pierwotnie zapisanym. Jeśli tak, możesz mieć pewność, że papierowe kopie zapasowe są niezawodne.


Aby dowiedzieć się więcej o tym, jak wykonać test odzyskiwania, proponuję zapoznać się z tym innym samouczkiem:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Odbieranie bitcoinów


Aby otrzymać swoje pierwsze bitcoiny, zacznij od włączenia i odblokowania karty COLDCARD.


![CCQ](assets/fr/052.webp)


W aplikacji Sparrow Wallet kliknij zakładkę "*Odbierz*".


![CCQ](assets/fr/053.webp)


Przed użyciem Address proponowanego przez Sparrow Wallet należy sprawdzić go na ekranie COLDCARD. Ta praktyka pozwala potwierdzić, że Address wyświetlany na Sparrow nie jest fałszywy i że Hardware Wallet rzeczywiście posiada klucz prywatny potrzebny do późniejszego wydania bitcoinów zabezpieczonych tym Address. Pomaga to uniknąć kilku rodzajów ataków.


Aby wykonać to sprawdzenie, kliknij menu "*Address Explorer*" na karcie COLDCARD.


![CCQ](assets/fr/054.webp)


Wybierz typ skryptu, którego używasz w Sparrow. W moim przypadku jest to SegWit P2WPKH. Klikam na niego.


![CCQ](assets/fr/055.webp)


Następnie można wyświetlić różne adresy pochodne w kolejności.


![CCQ](assets/fr/056.webp)


Sprawdź w Sparrow, czy Address pasuje. W moim przypadku Address ze ścieżką pochodną `m/84'/1'/0'/0/0` jest rzeczywiście `tb1qwfwwvzssep4wyjg3vsgezmwa037ehvd4fhmjvr` zarówno na Sparrow jak i COLDCARD.


![CCQ](assets/fr/057.webp)


Innym sposobem weryfikacji Ownership tego Address jest zeskanowanie jego kodu QR bezpośrednio do Sparrow z COLDCARD. Na ekranie głównym COLDCARD wybierz "*Scan Any QR Code*". Można również użyć klawisza "*QR*" na klawiaturze.


![CCQ](assets/fr/058.webp)


Zeskanuj kod QR Address wyświetlany na Sparrow Wallet.


![CCQ](assets/fr/059.webp)


Upewnij się, że Address wyświetlany na COLDCARD jest zgodny z tym wyświetlanym na Sparrow. Następnie naciśnij przycisk "*1*".


![CCQ](assets/fr/060.webp)


W ten sposób Address został pomyślnie potwierdzony.


![CCQ](assets/fr/061.webp)


Możesz teraz dodać "*Label*", aby opisać źródło bitcoinów, które zostaną zabezpieczone za pomocą tego Address. Jest to dobra praktyka, która pozwala lepiej zarządzać UTXO.


![CCQ](assets/fr/062.webp)


Więcej informacji na temat etykietowania można znaleźć w tym poradniku:


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Następnie możesz użyć tego Address do otrzymywania bitcoinów.


![CCQ](assets/fr/063.webp)


## Wysyłanie bitcoinów


Teraz, gdy otrzymałeś swój pierwszy Sats w Wallet zabezpieczonym kartą COLDCARD, możesz je również wydać!


Jak zawsze, zacznij od włączenia i odblokowania COLDCARD Q, a następnie otwórz Sparrow Wallet i przejdź do zakładki "*Wyślij*", aby przygotować nową transakcję.


![CCQ](assets/fr/064.webp)


Jeśli chcesz "kontrolować monety", tj. wybrać konkretnie, które UTXO mają zostać wykorzystane w transakcji, przejdź do zakładki "*UTXOs*". Wybierz UTXO, które chcesz wydać, a następnie kliknij "*Wyślij wybrane*". Nastąpi przekierowanie do tego samego ekranu w zakładce "*Wyślij*", ale z UTXO już wybranymi do transakcji.


![CCQ](assets/fr/065.webp)


Wprowadź adres docelowy Address. Można również wprowadzić wiele adresów, klikając przycisk "*+ Add*".


![CCQ](assets/fr/066.webp)


Zapisz "*Label*", aby zapamiętać cel tego wydatku.


![CCQ](assets/fr/067.webp)


Wybierz kwotę, która ma zostać wysłana do tego Address.


![CCQ](assets/fr/068.webp)


Dostosuj stawkę opłaty za transakcję do aktualnego rynku.


![CCQ](assets/fr/069.webp)


Upewnij się, że wszystkie parametry transakcji są prawidłowe, a następnie kliknij "*Twórz transakcję*".


![CCQ](assets/fr/070.webp)


Jeśli wszystko jest w porządku, kliknij "*Finalizuj transakcję do podpisu*".


![CCQ](assets/fr/071.webp)


Po utworzeniu transakcji w aplikacji Sparrow nadszedł czas, aby podpisać ją za pomocą karty COLDCARD. Aby przesłać PSBT (niepodpisaną transakcję) do urządzenia, masz kilka opcji. Jeśli włączona jest przewodowa transmisja danych, możesz wysłać transakcję bezpośrednio przez połączenie USB-C, tak jak w przypadku każdego innego Hardware Wallet. W tym przypadku w aplikacji Sparrow należy kliknąć przycisk "*Podpisz*" w prawym dolnym rogu. W moim przykładzie przycisk ten jest zablokowany, ponieważ karta COLDCARD nie jest podłączona kablem.


![CCQ](assets/fr/072.webp)


Jeśli wolisz utrzymywać połączenie "air-gap" bez bezpośredniego kontaktu między Hardware Wallet a komputerem, masz 2 opcje. Pierwszą i bardziej złożoną jest użycie karty microSD. Włóż kartę microSD do komputera, zarejestruj transakcję za pomocą przycisku "*Zapisz transakcję*" w aplikacji Sparrow, a następnie przenieś tę kartę do portu na karcie COLDCARD.


![CCQ](assets/fr/073.webp)


Następnie przejdź do menu "*Ready To Sign*".


![CCQ](assets/fr/074.webp)


Sprawdź szczegóły transakcji na swojej karcie COLDCARD, w tym otrzymany Address, wysłaną kwotę i opłatę transakcyjną.


![CCQ](assets/fr/075.webp)


Jeśli wszystko się zgadza, naciśnij przycisk "*ENTER*", aby podpisać transakcję.


![CCQ](assets/fr/076.webp)


Następnie umieść kartę microSD z powrotem w komputerze i w aplikacji Sparrow kliknij "*Load Transaction*", aby załadować podpisaną transakcję z karty microSD. Będziesz wtedy mógł przeprowadzić ostateczną kontrolę przed przesłaniem jej do sieci Bitcoin.


![CCQ](assets/fr/077.webp)


Druga metoda podpisywania za pomocą karty COLDCARD w Air-Gap, która jest znacznie prostsza niż metoda microSD, polega na zeskanowaniu PSBT bezpośrednio za pomocą aparatu urządzenia. W aplikacji Sparrow wybierz opcję "*Pokaż QR*".


![CCQ](assets/fr/078.webp)


Na karcie COLDCARD wybierz opcję "*Scan Any QR Code*". Można również użyć klawisza "*QR*" na klawiaturze.


![CCQ](assets/fr/079.webp)


Użyj kamery COLDCARD, aby zeskanować kod QR wyświetlany na Sparrow.


![CCQ](assets/fr/080.webp)


Szczegóły transakcji pojawią się ponownie w celu weryfikacji. Naciśnij "*ENTER*", aby podpisać, jeśli wszystko jest w porządku.


![CCQ](assets/fr/081.webp)


Karta COLDCARD wyświetli podpisaną transakcję jako kod QR. Użyj kamery internetowej komputera, aby zeskanować ten kod QR, wybierając opcję "*Scan QR*" w aplikacji Sparrow.


![CCQ](assets/fr/082.webp)


Podpisana transakcja jest teraz widoczna w serwisie Sparrow. Sprawdź po raz ostatni, czy wszystko się zgadza, a następnie kliknij "*Broadcast Transaction*", aby nadać ją w sieci Bitcoin.


![CCQ](assets/fr/083.webp)


Możesz śledzić swoje transakcje w zakładce "*Transakcje*" Sparrow Wallet.


![CCQ](assets/fr/084.webp)


Gratulacje, jesteś teraz na bieżąco z podstawową obsługą COLDCARD Q z Sparrow Wallet!


Jeśli uznałeś ten poradnik za przydatny, będę bardzo wdzięczny, jeśli zostawisz poniżej kciuk Green. Zachęcam również do udostępnienia tego poradnika w sieciach społecznościowych. Dziękuję bardzo!


Polecam również zapoznanie się z tym innym samouczkiem, w którym omawiamy zaawansowane opcje COLDCARD Q :


https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0