---
name: COLDCARD Q - Zaawansowane
description: Korzystanie z zaawansowanych opcji COLDCARD Q
---
![cover](assets/cover.webp)


W poprzednim samouczku omówiliśmy wstępną konfigurację karty COLDCARD Q i jej podstawowe funkcje dla początkujących. Jeśli właśnie otrzymałeś kartę COLDCARD Q i jeszcze jej nie skonfigurowałeś, zalecamy rozpoczęcie od tego samouczka przed kontynuowaniem tutaj:


https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Ten nowy samouczek poświęcony jest zaawansowanym opcjom COLDCARD Q, przeznaczonym dla zaawansowanych i paranoicznych użytkowników. W rzeczywistości COLDCARD wyróżnia się spośród innych portfeli sprzętowych wieloma zaawansowanymi funkcjami bezpieczeństwa. Oczywiście nie musisz korzystać ze wszystkich tych opcji. Wystarczy wybrać te, które pasują do Twojej strategii bezpieczeństwa.


**Ostrzeżenie**, nieprawidłowe użycie niektórych z tych zaawansowanych opcji może spowodować utratę bitcoinów lub zniszczenie Hardware Wallet. Dlatego zdecydowanie zalecam uważne przeczytanie porad i wyjaśnień dotyczących każdej opcji.


Przed rozpoczęciem upewnij się, że masz dostęp do fizycznej kopii zapasowej 12- lub 24-słowowej frazy Mnemonic i sprawdź jej ważność za pomocą następującego menu: `Zaawansowane/Narzędzia > Strefa zagrożenia > Funkcje seed > Wyświetl słowa seed`.


![CCQ](assets/fr/01.webp)


## BIP39 passphrase


Jeśli nie wiesz, czym jest BIP39 passphrase lub nie jest dla ciebie jasne, jak to działa, zdecydowanie zalecam wcześniejsze zapoznanie się z tym samouczkiem, który obejmuje podstawy teoretyczne potrzebne do zrozumienia ryzyka związanego z używaniem passphrase:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Należy pamiętać, że po skonfigurowaniu passphrase na Wallet, sam Mnemonic nie wystarczy do odzyskania dostępu do bitcoinów. Będziesz potrzebować zarówno Mnemonic, jak i passphrase. Co więcej, będziesz musiał wprowadzić passphrase za każdym razem, gdy odblokujesz COLDCARD Q. Zwiększa to bezpieczeństwo, ponieważ fizyczny dostęp do COLDCARD i znajomość kodu PIN są niewystarczające bez passphrase.


W przypadku kart COLDCARD dostępne są dwie opcje zarządzania passphrase:


1. **Klasyczne wprowadzanie danych:** passphrase wprowadza się ręcznie za każdym razem, gdy korzysta się z Hardware Wallet, podobnie jak w przypadku innych portfeli sprzętowych. COLDCARD Q upraszcza to zadanie dzięki pełnej klawiaturze.


2. **Możesz zaszyfrować swój passphrase i przechowywać go na karcie microSD. W takim przypadku konieczne będzie włożenie karty microSD do karty COLDCARD Q za każdym razem, gdy będzie ona używana. Należy pamiętać, że ta karta microSD będzie działać tylko na karcie COLDCARD Q i nie stanowi kopii zapasowej. Dlatego bardzo ważne jest przechowywanie kopii passphrase na nośniku fizycznym, takim jak papier lub metal.


Aby ustawić BIP39 passphrase, przejdź do menu "*passphrase*".


![CCQ](assets/fr/02.webp)


Wprowadź swój passphrase za pomocą klawiatury. Upewnij się, że wybrałeś silny passphrase (długi i losowy) i wykonaj fizyczną kopię zapasową.


![CCQ](assets/fr/03.webp)


Po ustawieniu passphrase COLDCARD Q wyświetli odcisk palca klucza głównego nowego Wallet powiązanego z tym passphrase. Pamiętaj, aby zapisać ten odcisk palca. Po ponownym wprowadzeniu passphrase podczas korzystania z urządzenia w przyszłości będzie można sprawdzić, czy wyświetlany odcisk palca jest zgodny z zapisanym. To sprawdzenie gwarantuje, że nie popełniono błędu podczas wprowadzania odcisku passphrase.


![CCQ](assets/fr/04.webp)


Można teraz nacisnąć "*ENTER*", aby zastosować passphrase do frazy Mnemonic i aktywować nowy Wallet. Jeśli wolisz zapisać passphrase na karcie microSD, włóż kartę do odpowiedniego gniazda i naciśnij "*1*".


![CCQ](assets/fr/05.webp)


Klucz passphrase został zastosowany. Odcisk klucza pojawi się na ekranie głównym i w górnej części ekranu.


![CCQ](assets/fr/06.webp)


Za każdym razem, gdy odblokujesz kartę COLDCARD Q, musisz wejść do menu "*passphrase*" i wprowadzić swój passphrase w taki sam sposób jak powyżej, aby zastosować go do Mnemonic przechowywanego w urządzeniu i uzyskać dostęp do właściwego Bitcoin Wallet.


![CCQ](assets/fr/07.webp)


Jeśli zapisałeś passphrase na karcie microSD, za każdym razem, gdy jej używasz, włóż ją do COLDCARD i wejdź do menu "*passphrase*". Karta COLDCARD załaduje passphrase bezpośrednio z karty microSD, więc nie trzeba będzie wprowadzać go ręcznie. Kliknij na "*Restore Saved*".


![CCQ](assets/fr/08.webp)


Sprawdź, czy długość i pierwsza litera załadowanego passphrase są prawidłowe.


![CCQ](assets/fr/09.webp)


Potwierdź, że wyświetlony odcisk palca jest zgodny z odciskiem Wallet i kliknij "*Restore*".


![CCQ](assets/fr/10.webp)


Należy pamiętać, że korzystanie z passphrase oznacza konieczność zaimportowania nowego zestawu kluczy pochodzących z kombinacji frazy Mnemonic i passphrase do oprogramowania zarządzającego Wallet (takiego jak Sparrow Wallet). Aby to zrobić, wykonaj krok "*Konfiguracja nowego Wallet w Sparrow*" w tym innym samouczku:


https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

## Opcje odblokowania


Karty COLDCARD korzystają również z wielu opcji procesu odblokowywania urządzenia. Dowiedzmy się więcej o tych zaawansowanych opcjach.


### Podstępne kody PIN


Trick PIN to dodatkowy kod PIN, inny niż ten zdefiniowany podczas początkowej konfiguracji urządzenia. Kod ten jest używany do wyzwalania określonych wstępnie skonfigurowanych działań, gdy tylko zostanie wprowadzony po włączeniu karty COLDCARD. Można skonfigurować kilka kodów Trick PIN, z których każdy jest powiązany z inną czynnością. Funkcje te umożliwiają dostosowanie karty COLDCARD do osobistej strategii bezpieczeństwa. Są one szczególnie przydatne w przypadku przymusu fizycznego, na przykład podczas napadu (powszechnie określanego w społeczności Bitcoin jako "atak kluczem za 5 dolarów").


Aby aktywować Trick PIN i powiązać go z działaniem, przejdź do menu `Settings > Login Settings > Trick PINs`.


![CCQ](assets/fr/11.webp)


Wybierz "*Dodaj nową sztuczkę*".


![CCQ](assets/fr/12.webp)


Ustaw kod PIN, który ma być powiązany z działaniem i pamiętaj, aby go zapisać.


![CCQ](assets/fr/13.webp)


Następnie wybierz czynność, która będzie wykonywana automatycznie za każdym razem, gdy wprowadzisz ten Trick PIN. Oto lista działań dostępnych dla kodu PIN:




- "*Brick Self*: Ta akcja niszczy oba chipy COLDCARD Q, jeśli wprowadzony zostanie Trick PIN, czyniąc urządzenie całkowicie bezużytecznym. Nie będzie można go odsprzedać, ponownie użyć ani nawet zwrócić do Coinkite. Urządzenie stanie się nieodwracalnie przestarzałe. Ta funkcja może być użyta w przypadku napadu, aby przekonać napastnika, że nigdy nie będzie w stanie uzyskać dostępu do twoich bitcoinów. **Uwaga**: bez fizycznej kopii zapasowej frazy Mnemonic i dowolnego passphrase, twoje bitcoiny zostaną trwale utracone.


![CCQ](assets/fr/14.webp)




- "*Wipe seed*": To menu oferuje kilka czynności umożliwiających usunięcie seed, tj. zresetowanie karty COLDCARD bez jej niszczenia. W przeciwieństwie do opcji "*Brick Self*", możliwe będzie ponowne skonfigurowanie urządzenia przy użyciu kopii zapasowej frazy Mnemonic. Jednak bez tej kopii zapasowej bitcoiny zostaną utracone. Oto dostępne opcje:
 - "*Wipe & Reboot* : Usuwa seed i restartuje COLDCARD bez wyświetlania jakichkolwiek informacji na ekranie.
 - "*Silent Wipe*": Po cichu czyści seed i odblokowuje COLDCARD na losowym fałszywym Wallet, jak gdyby nic się nie stało.
 - "*Wipe -> Wallet*": Dyskretnie usuwa seed i odblokowuje COLDCARD na wstępnie skonfigurowanym dodatkowym Wallet, zaprojektowanym jako przynęta. Ten Wallet może zawierać niewielką część oszczędności Bitcoin, aby zadowolić atakującego.
 - "*Say Wiped, Stop*": Usuwa seed i wyświetla na ekranie komunikat `seed is wiped, Stop`.


![CCQ](assets/fr/15.webp)




- "*Duress Wallet*": Dzięki tej akcji kod Trick PIN odblokowuje Wallet pochodzący z seed przy użyciu BIP85. Ten dodatkowy Wallet może być użyty jako przynęta, aby zadowolić atakującego. Karta COLDCARD działa tak, jakby była prawdziwym Wallet, ale bez głównego kodu PIN (innego niż Trick PIN) atakujący nigdy nie będzie w stanie uzyskać dostępu do prawdziwego Wallet. Strategia ta ma na celu przekonanie ludzi, że Wallet powiązany z Trick PIN jest jedynym istniejącym.


![CCQ](assets/fr/16.webp)




- "*Odliczanie logowania*": To menu grupuje działania z odliczaniem przed ich wykonaniem. **Ostrzeżenie**, niektóre z nich mogą zniszczyć urządzenie lub spowodować utratę bitcoinów. Oto dostępne podakcje:
 - "*Wipe & Countdown* : Czyści seed z pamięci COLDCARD, a następnie rozpoczyna godzinne odliczanie. Bez zapisania Mnemonic lub passphrase bitcoiny zostaną utracone. Ta opcja ma na celu zmylenie atakującego, aby myślał, że urządzenie odblokuje się po zakończeniu odliczania, podczas gdy w rzeczywistości zostanie zresetowane do ustawień fabrycznych.
 - "*Countdown & Brick*": Rozpoczyna godzinne odliczanie, po zakończeniu którego COLDCARD niszczy swoje dwa bezpieczne chipy, czyniąc ją trwale bezużyteczną. Bez kopii zapasowej bitcoiny zostaną utracone. Działanie to ma na celu oszukanie atakującego, który myśli, że czeka na odblokowanie, podczas gdy w rzeczywistości urządzenie ulegnie samozniszczeniu.
 - "*Just Countdown* : Uruchamia proste jednogodzinne odliczanie, po którym COLDCARD uruchamia się ponownie bez żadnych dalszych działań. seed nie jest usuwany, a urządzenie pozostaje nienaruszone. Należy uważać, aby nie pomylić tej akcji z opcją "*Login Countdown*", omówioną w następnych sekcjach, która dodaje odliczanie do głównego kodu PIN, dając jednocześnie dostęp do prawdziwego Wallet.


![CCQ](assets/fr/17.webp)




- "*Look Blank*": Ta czynność sprawia, że karta COLDCARD wydaje się pusta, sprawiając wrażenie, że seed został usunięty. W rzeczywistości nic się nie dzieje i karta seed pozostaje nienaruszona. Symuluje to nieużywaną lub zresetowaną kartę COLDCARD.


![CCQ](assets/fr/18.webp)




- "*Just Reboot* : Po użyciu kodu Trick PIN karta COLDCARD po prostu uruchamia się ponownie. Nie są wykonywane żadne inne czynności.


![CCQ](assets/fr/19.webp)




- "*Tryb Delta*": Ta złożona akcja, zarezerwowana dla doświadczonych użytkowników, ma na celu przeciwdziałanie wysoce wyrafinowanym atakom pod przymusem, czy to ze strony państwa, czy krewnego posiadającego uprzywilejowane informacje. Po włączeniu trybu Delta COLDCARD zapewnia dostęp do prawdziwego Wallet, umożliwiając atakującemu nawigację i sprawdzenie, czy jest to właściwy Wallet. Podpisy transakcji są jednak blokowane, co uniemożliwia transfer Bitcoin. Ponadto dostęp do frazy Mnemonic jest wyłączony, a każda próba jej odzyskania spowoduje jej usunięcie. Aby zwiększyć wiarygodność, Trick PIN używany w trybie Delta musi mieć ten sam prefiks co prawdziwy PIN (aby wyświetlać te same słowa antyphishingowe), ale sufiks musi być inny.


![CCQ](assets/fr/20.webp)


Po wybraniu działania potwierdź swój wybór.


![CCQ](assets/fr/21.webp)


Następnie można wyświetlić wszystkie skonfigurowane kody Trick PIN w dedykowanym menu.


![CCQ](assets/fr/22.webp)


Wybierając istniejący kod Trick PIN, można sprawdzić powiązaną z nim akcję. Można go również ukryć za pomocą opcji "*Hide Trick*", dzięki czemu stanie się niewidoczny w menu Trick PIN. Można go usunąć, klikając "*Delete Trick*", lub zmienić kod PIN, zachowując powiązaną akcję za pomocą "*Change PIN*".


![CCQ](assets/fr/23.webp)


Opcja "*Add If Wrong*", dostępna w menu "*Trick PIN*", umożliwia skonfigurowanie określonego działania, które jest automatycznie uruchamiane po określonej liczbie nieprawidłowych prób wprowadzenia głównego kodu PIN. Liczbę dozwolonych prób można ustawić podczas konfiguracji.


### Scramble Keys


Opcja Scramble Keys umożliwia zakodowanie cyfr wyświetlanych na przyciskach klawiatury podczas wprowadzania kodu PIN. Funkcja ta chroni poufność kodu PIN, nawet w przypadku inwigilacji przez osoby lub kamery.


Aby aktywować tę opcję, przejdź do menu `Ustawienia > Ustawienia logowania > Klawisze szyfrowania`.


![CCQ](assets/fr/24.webp)


Wybierz opcję "*Scramble Keys*".


![CCQ](assets/fr/25.webp)


Od tej pory po odblokowaniu karty COLDCARD Q klawiszom na klawiaturze będą losowo przypisywane nowe numery przy każdym użyciu.


![CCQ](assets/fr/26.webp)


### Odliczanie do logowania


Ta opcja umożliwia systematyczne odliczanie czasu przy każdej próbie odblokowania karty COLDCARD. Można to włączyć do strategii bezpieczeństwa, opóźniając dostęp do urządzenia w przypadku kradzieży lub nakładając opóźnienie przed podpisaniem transakcji, na przykład w celu ochrony w przypadku napadu. Odliczanie ma jednak zastosowanie do wszystkich zastosowań, w tym podczas legalnego korzystania z karty COLDCARD, co również wymaga cierpliwości. Należy uważać, aby nie pomylić tej opcji z akcją "*Just Countdown*", która jest aktywowana tylko w przypadku użycia określonego kodu Trick PIN.


Aby skonfigurować tę opcję, przejdź do menu `Ustawienia > Ustawienia logowania > Odliczanie logowania`.


![CCQ](assets/fr/27.webp)


Wybierz czas odliczania. Na przykład, jeśli wybierzesz 1 godzinę, będziesz musiał czekać 1 godzinę na każdą próbę odblokowania COLDCARD Q.


![CCQ](assets/fr/28.webp)


Przy każdym odblokowaniu pojawi się monit o wprowadzenie kodu PIN.


![CCQ](assets/fr/29.webp)


Następnie odczekaj czas ustawiony przez odliczanie.


![CCQ](assets/fr/30.webp)


Po zakończeniu odliczania konieczne będzie ponowne wprowadzenie kodu PIN w celu uzyskania dostępu do urządzenia.


![CCQ](assets/fr/31.webp)


### Logowanie do kalkulatora


Ta opcja umożliwia ukrycie karty COLDCARD jako kalkulatora podczas odblokowywania. Aby aktywować tę funkcję, przejdź do menu `Ustawienia > Ustawienia logowania > Logowanie kalkulatora`.


![CCQ](assets/fr/32.webp)


Aktywuj opcję, wybierając ją.


![CCQ](assets/fr/33.webp)


Od tej pory przy każdym włączeniu urządzenia wyświetlany będzie działający kalkulator z podstawowymi poleceniami.


![CCQ](assets/fr/34.webp)


Na przykład można obliczyć SHA256 Hash dla "*Plan B Network*".


![CCQ](assets/fr/35.webp)


Aby odblokować COLDCARD z trybu kalkulatora, zacznij od wprowadzenia prefiksu kodu PIN, po którym następuje myślnik. Na przykład, jeśli Twój kod PIN to `00-00` (ten kod jest słaby i stanowi jedynie przykład, więc wybierz silny kod PIN), wpisz `00-`. Następnie COLDCARD wyświetli dwa słowa antyphishingowe.


![CCQ](assets/fr/36.webp)


Następnie wprowadź pełny kod PIN, oddzielając go spacją lub myślnikiem, na przykład: `00 00`.


![CCQ](assets/fr/37.webp)


Karta COLDCARD wyjdzie wówczas z trybu kalkulatora i odblokuje się normalnie.


## Czyste niszczenie karty COLDCARD


Jeśli planujesz pozbyć się karty COLDCARD Q, na przykład dlatego, że używasz teraz innego Hardware Wallet, ważne jest, aby prawidłowo zniszczyć urządzenie. Gwarantuje to, że żadne informacje dotyczące Wallet nie będą mogły zostać odzyskane przez osoby trzecie.


Istnieją trzy poziomy niszczenia informacji, w zależności od potrzeb. Zanim zaczniesz, upewnij się, że twój Wallet został zaimportowany do innego Hardware Wallet, że masz dostęp do wszystkich swoich środków, a przede wszystkim, że masz swoją frazę Mnemonic i dowolny passphrase, z których oba są funkcjonalne. Bez kopii zapasowej Wallet zniszczenie karty COLDCARD spowoduje utratę bitcoinów.


Pierwszy poziom zniszczenia polega na usunięciu tylko seed. Ta opcja usuwa frazę Mnemonic z pamięci karty COLDCARD, pozostawiając urządzenie sprawnym. Jest to idealne rozwiązanie, jeśli chcesz ponownie użyć karty COLDCARD Q w późniejszym terminie. Aby usunąć seed z pamięci, przejdź do menu `Zaawansowane/Narzędzia > Strefa zagrożenia > Funkcje seed > Zniszcz seed`.


![CCQ](assets/fr/38.webp)


Drugi poziom zniszczenia polega na trwałym wyłączeniu dwóch bezpiecznych chipów COLDCARD za pomocą oprogramowania. Ta czynność sprawia, że urządzenie jest całkowicie bezużyteczne. Nie będzie można go odsprzedać, użyć ponownie ani zwrócić do Coinkite: zostanie trwale zniszczone. Aby kontynuować, należy wykonać kroki opisane w poprzedniej sekcji dotyczące kodu PIN "*Brick Me*" PIN, a następnie celowo wprowadź ten kod PIN podczas odblokowywania karty COLDCARD.


Trzeci poziom obejmuje fizyczne zniszczenie bezpiecznych komponentów karty COLDCARD Q. Tak jak poprzednio, spowoduje to, że urządzenie stanie się nieodwracalnie bezużyteczne. Aby to zrobić, użyj wiertarki, aby zrobić dziurę w dwóch chipach w prawym górnym rogu urządzenia (po odwróceniu do góry nogami), w pobliżu napisu "*SHOOT HERE*".


**Ważne środki ostrożności** :




- Aby uniknąć ryzyka porażenia prądem, przed przystąpieniem do obsługi urządzenia należy wyjąć z niego baterie i odłączyć je od zasilania.
- Przed rozpoczęciem wiercenia należy odczekać kilka minut po wyłączeniu urządzenia.
- Aby zapewnić sobie bezpieczeństwo, należy nosić izolowane rękawice i okulary ochronne.


![CCQ](assets/fr/39.webp)


Po wbiciu żetonów nie należy próbować ponownie podłączać karty COLDCARD Q.


Gratulacje, jesteś teraz na bieżąco z zaawansowanymi opcjami COLDCARD Q!


Jeśli uważasz, że ten poradnik jest przydatny, będę bardzo wdzięczny, jeśli zostawisz poniżej kciuk Green. Zapraszam do udostępnienia tego poradnika w sieciach społecznościowych. Dziękuję bardzo!


Polecam również ten inny poradnik, w którym omawiamy wykorzystanie bezpośredniego konkurenta CCQ, Ledger Flex :


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a