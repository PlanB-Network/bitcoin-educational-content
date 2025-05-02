---
name: Liana
description: Konfiguracja i korzystanie z Wallet na Liana
---
![cover](assets/cover.webp)


W tym samouczku wyjaśnimy krok po kroku, jak korzystać z aplikacji Liana na komputerze. Dowiesz się między innymi, jak skonfigurować automatyczny plan sukcesji, odbierać i wysyłać bitcoiny w normalnych sytuacjach oraz odzyskiwać środki z istniejącego Wallet po określonym czasie.


W styczniu 2025 r. portfele sprzętowe kompatybilne z Liana to: BitBox02, Blockstream Jade, Blockstream Jade Plus, COLDCARD MK4, COLDCARD Q, Ledger Nano S, Ledger Nano S Plus, Ledger Nano X, Ledger Flex, Specter DIY.


Jeśli chcesz odzyskać środki z istniejącego Liana Wallet, przeczytaj poniższą prezentację i przejdź bezpośrednio do sekcji "Odzyskiwanie bitcoinów".


## Przedstawiamy oprogramowanie Liana


Liana to pakiet oprogramowania typu open source przeznaczony do tworzenia i zarządzania zaawansowanymi portfelami, w szczególności jako część zautomatyzowanego systemu dziedziczenia lub solidnego mechanizmu tworzenia kopii zapasowych. Projekt jest rozwijany od 2022 roku przez Wizardsardine, firmę współzałożoną przez Kévina Loaeca i Antoine'a Poinsota. Na oficjalnej stronie internetowej Liana jest przedstawiany jako "prosty Wallet do osobistej kurateli, z funkcjami odzyskiwania i dziedziczenia". Oprogramowanie działa na komputerach - Linux, MacOS, Windows - a jego (otwarty) kod źródłowy jest dostępny [na GitHub] (https://github.com/wizardsardine/Liana).


Liana opiera się na programowalności Bitcoin, tworząc zaawansowany Wallet. W szczególności wykorzystuje on blokady czasowe (*timelocks*), które pozwalają na wydawanie środków dopiero po upływie określonego czasu i które są zaangażowane w odzyskiwanie Bitcoinów. Liana Wallet składa się zatem z kilku ścieżek wydawania:




- Główna ścieżka wydatków, która jest zawsze dostępna;
- Co najmniej jedna ścieżka odzyskiwania, która staje się dostępna po pewnym czasie.


Poniższy schemat ilustruje działanie Wallet z dwoma ścieżkami wydatków:


![Schéma explicatif](assets/fr/01.webp)


Ta operacja umożliwia ustawienie różnych konfiguracji, w tym :




- Plan sukcesji (lub dziedziczenia), umożliwiający spadkobiercom odzyskanie środków w przypadku śmierci użytkownika. Aby uzyskać więcej informacji na ten temat, zalecamy przeczytanie [części 4](https://planb.network/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f/233c88d3-2e8e-5eba-ac06-efe67a209038) kursu BTC102.
- Wzmocniona kopia zapasowa z czasem odzyskiwania, dająca użytkownikowi możliwość korzystania z Wallet bez konieczności przechowywania odpowiedniej tajnej frazy i ryzyka kradzieży, na przykład podczas włamania.
- Siatka bezpieczeństwa dla osób rozpoczynających z Bitcoin: będą zarządzać własnym Wallet, a ich "opiekun" (na przykład krewny) zastrzeże sobie prawo do odzyskania środków po określonym czasie.
- Schemat podpisu wielostronnego (*Multisig*) ze zmniejszonymi wymaganiami w czasie, aby poradzić sobie ze zniknięciem jednego lub więcej uczestników, takich jak partnerzy firmy.


Ogromną siłą Liana jest to, że wprowadza znormalizowany sposób gwarantowania odzyskania środków w przypadku utraty głównego klucza, wykorzystywanego do bieżących wydatków. Stanowi to ogromną innowację w zakresie czystego przechowywania środków, które jest obarczone ryzykiem, zwłaszcza jeśli nie jesteś dobrze poinformowany na ten temat. Liana może zatem zachęcić nawet najbardziej niechętnych ryzyku użytkowników do zaprzestania korzystania z usług powiernika (takiego jak platforma Exchange) do przechowywania swoich środków i odzyskania Ownership swoich pieniędzy, zgodnie z etosem Bitcoin Cypherpunk.


Oczywiście Liana ma swoje wady. Pierwszą z nich jest konieczność regularnego aktualizowania Wallet poprzez dokonywanie transakcji na Bitcoin Blockchain. Może to być uciążliwe (w zależności od częstotliwości korzystania z oprogramowania) i kosztowne (w zależności od poziomu opłat w danym momencie), ale jest to cena, jaką płacisz za dodatkowe bezpieczeństwo.


Drugim negatywnym aspektem może być poufność. Gdy w konfigurację zaangażowana jest inna osoba, ma ona dostęp do wszystkich adresów użytkownika i może monitorować jego aktywność. Nie będzie to jednak problemem, jeśli zdecydujesz się na wzmocnioną kopię zapasową lub plan sukcesji, w którym spadkobierca nie będzie miał natychmiastowej wiedzy o szczegółach Wallet.


## Przygotowanie


W tym samouczku skonfigurujemy plan sukcesji. Będziemy używać :




- Ledger Nano S Plus, na codzienne wydatki;


https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4


- Blockstream Jade, używany do odzyskiwania środków;


https://planb.network/tutorials/wallet/hardware/jade-7d62bf0c-f460-4e68-9635-af9b731dabc3


- Dwa nośniki pamięci (pamięci USB) do przechowywania deskryptora Wallet;
- Pismo spadkowe zawierające instrukcje dotyczące odzyskania środków;
- Numerowana zapieczętowana torba, aby zapewnić, że urządzenie do odzyskiwania (Jade) nie było używane.


## Instalacja i konfiguracja


Odwiedź oficjalną stronę Wizardsardine i pobierz Liana pod adresem https://wizardsardine.com/Liana/. Możesz również pobrać najnowszą wersję [z repozytorium GitHub](https://github.com/wizardsardine/Liana/releases), gdzie możesz sprawdzić autentyczność oprogramowania. Wersja używana w tym poradniku to 0.9.


![Télécharger Liana](assets/fr/02.webp)


Aby dowiedzieć się, jak ręcznie zweryfikować autentyczność i integralność oprogramowania przed instalacją, zalecamy zapoznanie się z tym samouczkiem :


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Zainstaluj oprogramowanie na swoim komputerze i uruchom je. Wybierz opcję "*Create a new Liana Wallet*", aby skonfigurować Wallet.


![Accueil Liana](assets/fr/03.webp)


Wybierz typ Wallet. Jeśli chcesz skonfigurować rozszerzoną kopię zapasową z czasem odzyskiwania, możesz wybrać opcję "*Zbuduj własną*" i wybrać domyślny schemat. Będzie to działać w podobny sposób, z wyjątkiem tego, że nie będzie konieczne zachowanie frazy odzyskiwania Hardware Wallet.


Pomijamy tutaj przypadek *Expanding Multisig*, który tworzy bardziej złożoną konfigurację.


Na potrzeby tego samouczka będziemy używać prostego dziedziczenia.


![Choisir type de portefeuille](assets/fr/04.webp)


Poniżej krótkie wyjaśnienie.


![Rapide explication](assets/fr/05.webp)


Po zapoznaniu się z wyjaśnieniami będziesz mógł skonfigurować klucze do swojego Liana Wallet. Jest to kluczowy krok, ponieważ określa on charakterystykę wydatków na koncie.


![Configurer clés](assets/fr/06.webp)


Po pierwsze, w menu "Ustawienia zaawansowane" można zdecydować o "typie deskryptora", tj. sposobie, w jaki Contract będzie zapisywany na łańcuchu. Do wyboru są dwa typy: P2WSH (SegWit) lub Taproot. W obu przypadkach semantyka warunków wydatków będzie taka sama. Podczas gdy P2WSH sprawia, że Contract jest łatwiejszy do zrozumienia, Taproot jest lepszy, ponieważ ukrywa nieużywane warunki i oszczędza koszty podczas wyszukiwania.


Wybór ten jest opcjonalny: w razie wątpliwości należy pozostawić opcję domyślną (P2WSH w przypadku wersji 0.9, ale może ona ulec zmianie).


![Choisir le type de descripteur](assets/fr/07.webp)


Następnie należy skonfigurować klucz główny (*primary key*). Ten klucz (a raczej ten zestaw kluczy) będzie używany do bieżącego wydatkowania środków, które nie podlega żadnym warunkom czasowym. Klikając na "*Set*", można wybrać odpowiednie *urządzenie podpisujące*. W naszym przypadku wybraliśmy Ledger Nano S Plus Hardware Wallet.


Autoryzuj udostępnianie rozszerzonego klucza publicznego z urządzenia. Nadaj temu kluczowi znaczącą nazwę (w tym przypadku "Nano S+"). Należy pamiętać, że wszystkie aplikacje zainstalowane na urządzeniu będą nadal działać normalnie.


![Configurer clé principale](assets/fr/08.webp)


Następnie należy ustawić opóźnienie zwrotu, tj. czas, po którym środki mogą zostać wydane przez *klucz dziedziczenia*. Opóźnienie to jest definiowane w blokach, przy czym każdy blok jest oddzielony średnio o 10 minut. Może ono wynosić od 10 minut (1 blok) do około 15 miesięcy (65 535 bloków). Ten górny limit jest ograniczeniem protokołu Bitcoin, ponieważ czas blokady jest zakodowany na 16 bitach.


Z wyjątkiem szczególnych okoliczności, wybierz najdłuższy czas realizacji: 15 miesięcy lub 65 535 bloków. Pozwoli to zaoszczędzić koszty. Zalecamy jednak przeprowadzanie procedury aktualizacji (opisanej w sekcji "Aktualizacja Wallet") raz w roku, zawsze o tej samej porze roku, aby "zrytualizować" tę praktykę i uniknąć zapomnienia.


Tutaj ustawiliśmy czas odzyskiwania na jedną godzinę (6 bloków), aby przeprowadzić nasze testy.


![Configurer temps de verrouillage](assets/fr/09.webp)


Na koniec skonfiguruj klucz do majątku. Ten klucz (a raczej zestaw kluczy) będzie używany do odzyskiwania środków w przypadku twojego zniknięcia. Kliknij "*Set*", wybierz urządzenie podpisujące i potwierdź na nim udostępnienie rozszerzonego klucza publicznego.


Na potrzeby tego samouczka wybraliśmy Jade. Nadaj kluczowi sugestywną nazwę (tutaj "Jade"). Podobnie jak w przypadku pierwszego urządzenia, konwencjonalne konta będą nadal działać.


![Configurer clé de succession](assets/fr/10.webp)


Po wykonaniu wszystkich tych czynności sprawdź, czy wszystko jest w porządku i kliknij "*Kontynuuj*", aby potwierdzić swoje wybory.


![Confirmer clés](assets/fr/11.webp)


Następnym krokiem jest zapisanie deskryptora Wallet. Jest to informacja potrzebna do znalezienia środków na koncie. W przeciwieństwie do frazy Mnemonic, deskryptor nie pozwala na wydawanie środków, więc ujawnienie go spowoduje jedynie problem z poufnością (dana osoba będzie znała wszystkie twoje transakcje).


Zapisz dwie kopie deskryptora na nośniku elektronicznym, takim jak pamięć USB. Upewnij się, że wydrukowałeś również dwie kopie na papierze, aby mieć do nich dostęp w przypadku uszkodzenia nośnika elektronicznego. Każda kopia zapasowa musi być powiązana z urządzeniem podpisującym.


![Sauvegarder descripteur](assets/fr/12.webp)


Nasz deskryptor (który jest analizowany na końcu samouczka) jest następujący:


```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```


Ostatnim krokiem w początkowej konfiguracji Wallet jest weryfikacja deskryptora w każdym z portfeli sprzętowych, które służą jako urządzenia podpisujące.


![Enregistrer descripteur](assets/fr/13.webp)


Zrób to samo dla każdego urządzenia podpisującego. Konieczne będzie sprawdzenie i potwierdzenie, że deskryptor został dodany do każdego Hardware Wallet.


![Enregistrer descripteur Nano S Plus](assets/fr/14.webp)


Informacje o Wallet są teraz zarejestrowane i pozostaje tylko skonfigurować sposób połączenia z siecią Bitcoin. Możesz użyć własnego węzła (lokalnego lub zdalnego) lub skorzystać z infrastruktury WizardSardine. W tym drugim przypadku należy połączyć e-mail Address z Wallet, co umożliwi pobranie deskryptora. WizardSardine będzie miał dostęp do wszystkich transakcji. Dlatego sugerowana jest pierwsza opcja.


![Sélectionner connexion réseau](assets/fr/15.webp)


Zdecydowaliśmy się użyć własnego węzła. Możesz użyć istniejącego węzła lub zainstalować *przycięty węzeł* na swoim komputerze. Jeśli nie masz dostępu do żadnego innego węzła, zainstaluj własny węzeł na swojej maszynie, co powinno zająć trochę czasu (rzędu kilku dni).


![Choisir type de nœud](assets/fr/16.webp)


W tym samouczku wykorzystaliśmy istniejący (publiczny) serwer Electrum. Ale uwaga! Miał on dostęp do całej naszej aktywności z Liana Wallet. Więc użyj własnego węzła, jeśli chcesz chronić swoją prywatność.


![Connexion serveur Electrum public](assets/fr/17.webp)


Po zakończeniu konfiguracji węzła powinien zostać otwarty ekran główny, wyświetlający świeżo utworzony Liana Wallet.


Skorzystaj z okazji, aby przechować urządzenie do odzyskiwania danych w bezpiecznym miejscu. Powinien on być przechowywany w strategicznym miejscu, aby spadkobiercy mogli go znaleźć w przypadku śmierci.


Aby zwiększyć bezpieczeństwo, można umieścić komponenty używane do odzyskiwania danych w zapieczętowanej torbie (*tamper-evident bag*) i zapisać gdzieś jej numer seryjny. Gwarantuje to, że nikt nie miał do niego dostępu i że urządzenie pozostaje ważne.


W naszym przykładzie zmontowaliśmy następujący Elements:




- Blockstream Jade jako urządzenie do podpisywania nieruchomości;
- Kabel USB do podłączania i ładowania urządzenia;
- Papierowa kopia zapasowa zdania na wypadek awarii lub uszkodzenia urządzenia (należy pamiętać, że nośnik może być również metalowy, a zatem chroniony przed Elements, jak ma to miejsce na przykład w przypadku kapsuł Cryptosteel);
- Klucz USB zawierający deskryptor Wallet;
- Papierowa kopia zapasowa deskryptora na wypadek awarii lub uszkodzenia klucza USB (ta kopia zapasowa nie została tutaj sfotografowana);
- Pismo spadkowe opisujące kroki, jakie należy podjąć w celu odzyskania środków.


![Éléments de récupération](assets/fr/18.webp)


I umieściliśmy te przedmioty pod Seal!


![Sachet scellé récupération](assets/fr/19.webp)


## Otrzymanie środków


Główny ekran Liana wyświetla saldo i transakcje (przeszłe i bieżące) powiązane z Wallet. W naszym przypadku saldo wynosi zero, co jest normalne.


![Écran principal](assets/fr/20.webp)


Aby otrzymać środki, przejdź do zakładki "*Odbierz*" i kliknij "*generate Address*". Na ekranie powinien pojawić się nowy Address. Jest on dłuższy niż w konwencjonalnych portfelach: jest to Address połączony z samodzielnym Contract (P2WSH lub Taproot).


![Générer nouvelle adresse](assets/fr/21.webp)


Musisz zweryfikować ten Address na swoim Hardware Wallet, klikając "*Weryfikuj na urządzeniu sprzętowym*".


![Vérifier adresse portefeuille matériel](assets/fr/22.webp)


Po wysłaniu środków transakcja pojawia się na ekranie głównym (najpierw jako niepotwierdzona, a następnie jako potwierdzona). W tym teście wysłaliśmy 50 000 satoshi (nieco ponad 50 USD w momencie transferu). Jest rzeczą oczywistą, że kwota przelewu w twoim przypadku będzie musiała być o rząd wielkości wyższa niż ta wartość, ze względu na opłaty transakcyjne.


![Vérifier solde](assets/fr/23.webp)


Możesz sprawdzić status wygaśnięcia swoich środków, przechodząc do zakładki "*Coins*". Ta zakładka pokazuje różne monety (UTXO) w Wallet. Tutaj widzimy, że moneta 50 000 satoshis utworzona przez naszą transakcję wygasa tego samego dnia (za godzinę).


![Obtenir informations pièce](assets/fr/24.webp)


Aby lepiej zrozumieć model reprezentacji UTXO używany w Bitcoin, można zapoznać się z pierwszą częścią kursu na temat poufności w Bitcoin napisaną przez Loïca Morela:


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Wydatki bieżące


Bieżące wydatki to normalna sytuacja podczas korzystania z Liana. Wysyłanie bitcoinów za pomocą klucza głównego działa jak we wszystkich klasycznych portfelach Bitcoin, takich jak Electrum lub Sparrow.


Aby dokonać opłaty, przejdź do zakładki "*Wyślij*" i wprowadź niezbędne informacje: BTC Address odbiorcy, kwotę do wysłania i żądaną stawkę opłaty. Dla własnej wygody można również dodać opis (zapisany lokalnie). W naszym przykładzie wysłaliśmy 10 000 satoshis do pewnego Boba, za stawkę 4 sat/ov, czyli 0,67 USD w momencie transakcji.


Liana oferuje również "kontrolę monet": wskazujesz, którą monetę (UTXO) chcesz wydać. Tutaj wybraliśmy wcześniej utworzoną monetę 50 000 satoshi.


![Envoyer fonds clé principale](assets/fr/25.webp)


Następnie podpisz transakcję za pomocą urządzenia do podpisu połączonego z kluczem głównym, klikając "*Podpisz*". Będziesz musiał zweryfikować i potwierdzić transakcję na swoim Hardware Wallet. Tutaj użyliśmy Nano S Plus do podpisania transakcji.


![Signer transaction clé principale](assets/fr/26.webp)


Na koniec roześlij transakcję do sieci, klikając "*Broadcast*". Należy pamiętać, że wysłanie środków zresetuje czas odzyskiwania zużytych monet.


![Diffuser transaction clé principale](assets/fr/27.webp)


Transakcja pojawi się na ekranie głównym, a saldo zostanie zaktualizowane.


![Solde après dépense](assets/fr/28.webp)


## Aktualizacja portfolio


Jak wyjaśniono powyżej, Liana Wallet wymaga regularnego aktualizowania środków poprzez wykonywanie transakcji na Blockchain. Jeśli tego nie zrobisz, Twoje środki mogą zostać odzyskane przez spadkobiercę (lub przez drugie urządzenie w przypadku rozszerzonej kopii zapasowej). Sytuacja ta nie jest ekstremalnie niebezpieczna, ale niweczy cel stworzenia tego mechanizmu: zachowanie kontroli nad bitcoinami bez uciekania się do zaufanej strony trzeciej, przy jednoczesnym korzystaniu z sieci bezpieczeństwa.


Ostrzeżenie zostanie wyświetlone przed wygaśnięciem środków (lub ich części), które można wydać za pomocą klucza odzyskiwania. Wskazuje ono, że "ścieżka odzyskiwania" (*ścieżka odzyskiwania*) będzie wkrótce dostępna. Biorąc pod uwagę krótki czas odzyskiwania środków (jedna godzina), komunikat ten jest wyświetlany bezpośrednio w naszym przypadku.


![Avertissement chemin récupération](assets/fr/29.webp)


Gdy zbliża się termin, pojawi się przycisk z prośbą o aktualizację danych środków.


![Actualiser pièces depuis l'écran principal](assets/fr/30.webp)


Aby zaktualizować swoje monety, przejdź do zakładki "*Coins*" i kliknij "*Refresh coin*" w odpowiednim polu monet. Jeśli posiadasz kilka monet, powinieneś odświeżać je pojedynczo i w stosunkowo krótkich odstępach czasu, ze względu na poufność. Aby obniżyć koszty, możesz skonsolidować swoje środki, wysyłając cały Wallet do nowego odbierającego Address, ale wpłynie to na poufność.


![Actualiser pièce](assets/fr/31.webp)


Wskaż żądaną stawkę opłaty za transakcję. Ponieważ jest to przelew do siebie, możesz ustawić dość niską stawkę opłaty, zwłaszcza jeśli zrobisz to kilka dni przed wygaśnięciem.


![Transfert à soi-même](assets/fr/32.webp)


Transakcja (oznaczona jako "*przelew własny*") będzie widoczna tylko w zakładce "*Transakcje*".


![Transactions après auto-transfert](assets/fr/33.webp)


Po potwierdzeniu, moneta jest bezpieczna! Możesz spać spokojnie do następnej daty wygaśnięcia.


## Odzyskiwanie Bitcoin


Podczas odzyskiwania środków z Liana Wallet może wystąpić jedna z dwóch sytuacji. Możesz mieć dostęp do komputera, na którym zainstalowane jest oprogramowanie, w którym to przypadku wszystko, co musisz zrobić, to je otworzyć (co nastąpi w przypadku rozszerzonego modelu kopii zapasowej). Możesz jednak nie mieć dostępu do tego komputera, więc zaczniemy od zera. Należy pamiętać, że procedura odzyskiwania jest taka sama w obu przypadkach.


Aby rozpocząć, pobierz Liana z [oficjalnej strony Wizardsardine](https://wizardsardine.com/Liana/) lub z [repozytorium GitHub](https://github.com/wizardsardine/Liana/releases), gdzie możesz sprawdzić autentyczność oprogramowania. Zainstaluj oprogramowanie i uruchom je. Wersja używana w naszym przypadku to 0.9, więc wizualizacje mogły ulec zmianie. Na ekranie powitalnym wybierz opcję "Dodaj istniejący Liana Wallet".


![Ajouter portefeuille existant](assets/fr/34.webp)


Skonfiguruj sposób połączenia z siecią. Możesz wybrać własny węzeł (lokalny lub zdalny) lub skorzystać z infrastruktury WizardSardine. W tym drugim przypadku będziesz potrzebować adresu e-mail Address używanego przez twórcę Wallet, aby fundusze mogły zostać zlokalizowane automatycznie. Jeśli nie posiadasz tych informacji, wybierz pierwszą opcję.


![Sélectionner connexion réseau](assets/fr/35.webp)


Jeśli korzystasz z własnego węzła, zaimportuj deskryptor Wallet. Jest to techniczny opis konta, umożliwiający pobranie znajdujących się na nim środków. W naszym przypadku są to następujące informacje:


```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```


![Importer descripteur](assets/fr/36.webp)


Następnie Liana poprosi o wprowadzenie frazy Mnemonic. Jeśli posiadasz działające urządzenie podpisujące (Hardware Wallet), pomiń tę część. Jeśli brakuje urządzenia lub jest ono uszkodzone, ale masz odpowiednie 12 lub 24 słowa, nadal możesz skorzystać z tej opcji. Na wszelki wypadek (jeśli ilość danych do odzyskania jest wysoka) zalecamy zakup nowego Hardware Wallet i użycie Mnemonic do przywrócenia kluczy.


W naszym przypadku używamy Blockstream Jade Hardware Wallet jako urządzenia do odzyskiwania danych i decydujemy się pominąć ("*Skip*") ten krok.


![Passer phrase mnémotechnique](assets/fr/37.webp)


Sprawdź i zapisz deskryptor w urządzeniu podpisującym, wybierając go na ekranie. Jeśli urządzenie Hardware Wallet nie pojawi się, sprawdź, czy jest podłączone i odblokowane. Sprawdź i potwierdź, że te informacje zostały dodane do urządzenia.


![Enregistrer descripteur sur l'appareil de récupération](assets/fr/38.webp)


Konfiguracja węzła. Możesz użyć istniejącego węzła lub zainstalować *przycięty węzeł* na swoim komputerze. W naszym przypadku użyliśmy istniejącego węzła.


![Choisir type de nœud](assets/fr/39.webp)


W tym samouczku wykorzystaliśmy publiczny serwer Electrum. Miał on jednak dostęp do całej naszej aktywności z Liana Wallet. Jeśli chcesz chronić swoją prywatność, lepiej użyj własnego węzła.


![Connexion serveur Electrum public](assets/fr/17.webp)


Po skonfigurowaniu węzła zostaniesz przeniesiony do głównego ekranu Wallet, gdzie możesz wyświetlić saldo i poprzednie transakcje powiązane z kontem. Można również sprawdzić, czy można pobrać środki. Tutaj widzimy, że można pobrać monetę.


![Accueil Liana récupération](assets/fr/40.webp)


Aby odzyskać środki w Wallet, przejdź do Ustawień ("*Ustawienia*") w lewym dolnym rogu i kliknij "*Odzyskiwanie*".


![Récupération dans paramètres](assets/fr/41.webp)


Wydaj monetę w Wallet, zaznaczając odpowiednie pole. Wskaż BTC Address, do którego chcesz wysłać środki, a także stawkę opłaty transakcyjnej. Następnie kliknij "*Dalej*".


![Récupération des pièces](assets/fr/42.webp)


Podpisz transakcję, klikając "*Podpisz*" i zatwierdzając transakcję na swoim Hardware Wallet.


![Signer transaction clé de récupération](assets/fr/43.webp)


Następnie wyemituj go w sieci, klikając "*Broadcast*".


![Diffuser transaction clé de récupération](assets/fr/44.webp)


Transakcja powinna pojawić się na ekranie głównym. Po potwierdzeniu odzyskiwanie jest zakończone!


![Écran principal après récupération](assets/fr/45.webp)


## Bonus: analiza deskryptorów


Deskryptor to czytelny dla człowieka ciąg znaków, który wyczerpująco opisuje zestaw adresów. Łączy w sobie szereg istotnych informacji umożliwiających pobieranie części (UTXO) zaawansowanego Wallet. Sposób zapisu deskryptora jest oparty na [Miniscript syntax](https://bitbox.swiss/blog/understanding-Bitcoin-miniscript-part-2/), języku skryptowym opracowanym przez Andrew Poelstrę, Pietera Wuille'a i Sanketa Kanjalkara w 2019 roku.


Aby lepiej zrozumieć, dlaczego ten ciąg znaków jest ważny, przeanalizujmy deskryptor w naszym przykładzie, którym jest :


```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```


Z tego deskryptora można wyodrębnić następujące informacje:




- `wsh` (skrót od *witness script Hash*): Jest to typ utworzonego wyjścia transakcyjnego. Gdybyśmy zdecydowali się użyć Taproot, identyfikatorem byłby `tr`.
- `or_d`: Jest to operator logiczny wskazujący, że *jeden z następujących dwóch* warunków musi być spełniony, aby wydatek został zaakceptowany (`_d` wskazuje konkretną składnię).
- `pk` (skrót od *public key*): Ten operator sprawdza dany podpis z następującym kluczem publicznym i podaje odpowiedź jako wartość logiczną (PRAWDA lub FAŁSZ).
- `[3689a8e7/48'/0'/0'/2']`: Ten element zawiera *odcisk palca* klucza głównego dla głównego Hardware Wallet (w tym przypadku Nano S Plus) oraz ścieżkę pochodną do połączonego rozszerzonego klucza prywatnego (z którego pochodzą wszystkie inne klucze prywatne).
- `xpub6FKY ... WQa`: Jest to rozszerzony klucz publiczny powiązany z głównym Hardware Wallet (tutaj Nano S Plus)
- `/<0;1>/*`: Są to ścieżki wyprowadzania dla uzyskania prostych kluczy i adresów: `0` dla odbioru, `1` dla operacji wewnętrznych (*change*), z "symbolem wieloznacznym" (`*`) umożliwiającym sekwencyjne wyprowadzanie kilku adresów w konfigurowalny sposób, podobny do zarządzania "limitem luk" w klasycznym oprogramowaniu Wallet.
- and_v`: Jest to operator logiczny wskazujący, że *następujące dwa* warunki muszą być spełnione, aby wydatek został zaakceptowany (`_v` wskazuje konkretną składnię).
- `v:pkh` (skrót od *verify: public key Hash*): Ten operator weryfikuje dany podpis i klucz publiczny względem klucza publicznego Hash (*Hash*), który następuje. Jest to zasadniczo to samo sprawdzenie, co w przypadku skryptów P2PKH i P2WPKH.
- `[42e629dd/48'/0'/0'/2']`: Jest to ten sam element, co powyżej (składający się ze śladu i ścieżki wyprowadzania), z wyjątkiem tego, że wskazany jest ślad klucza głównego odzyskiwania sprzętu Wallet (w tym przypadku Jade).
- `xpub6DpQ ... WQd`: Jest to rozszerzony klucz publiczny powiązany z odzyskiwaniem sprzętowym Wallet (tutaj Jade).
- `older(6)`: Ten operator sprawdza, czy utworzone wyjście transakcyjne musi mieć wiek ściśle większy niż 6 bloków, aby mogło zostać wydane.


Ostatnia pozycja danych (`8alrve5h`) jest sumą kontrolną deskryptora i odpowiada identyfikatorowi Wallet.


Skrypty utworzone przez ten Wallet będą miały następującą postać:


```plaintext
<primary_key> CHECKSIG IFDUP NOTIF DUP HASH160 <recovery_key_hash> EQUALVERIFY CHECKSIGVERIFY <locktime> CHECKSEQUENCEVERIFY ENDIF
```


Ponieważ bezpieczeństwo Bitcoin Wallet zależy również od zrozumienia sposobu jego działania, sugeruję dogłębne zapoznanie się z mechanizmami deterministycznych i hierarchicznych portfeli, biorąc udział w tym bezpłatnym szkoleniu na temat Plan ₿ Network :


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f