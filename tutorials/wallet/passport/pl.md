---
name: Passport Core
description: Konfiguracja i korzystanie z urządzenia Passport Hardware Wallet w trybie ręcznym
---
![cover](assets/cover.webp)

Passport to Bitcoin-only Hardware Wallet, zaprojektowany przez Foundation Devices, amerykańską firmę założoną w kwietniu 2020 roku w Bostonie.

Passport "*Batch 2*" prezentowany w tym poradniku jest następcą "*Founder's Edition*". Wyróżnia się wysokiej jakości wzornictwem, kolorowym ekranem o wysokiej rozdzielczości i ergonomiczną klawiaturą fizyczną. Działa w trybie "*Air-Gap*", zapewniając, że klucze prywatne Wallet pozostają całkowicie odizolowane, a komunikacja jest możliwa za pośrednictwem karty MicroSD lub kodów QR. Urządzenie jest wyposażone w wymienną, ładowalną baterię Nokia BL-5C o pojemności 1200 mAh. Ten niezastrzeżony akumulator można łatwo wymienić, ponieważ model BL-5C jest powszechnie dostępny w sklepach.

💡 **Aktualizacja:** Od marca 2025 roku ta portfel sprzętowy nie nazywa się już „Passport” ani „Passport V2”, lecz „Passport Core”.

Jeśli chodzi o łączność, Passport jest wyposażony w port MicroSD, port USB-C do ładowania i tylną kamerę do skanowania kodów QR.


Jeśli chodzi o bezpieczeństwo, Passport zawiera bezpieczny element, a kod źródłowy urządzenia jest całkowicie open-source. Oferuje wszystkie funkcje oczekiwane od dobrego Bitcoin Hardware Wallet. Należy pamiętać, że Passport nie obsługuje jeszcze miniscript, ale ta funkcja jest planowana na drugi kwartał 2025 roku.


Wyceniony na 199 USD, Passport jest pozycjonowany jako wysokiej klasy Hardware Wallet, konkurując z modelami Coldcard Q, Jade Plus, Tezor Safe 5 i Ledger z najwyższej półki.


![Image](assets/fr/01.webp)


Aby zarządzać bezpiecznym Wallet na Passport, masz kilka opcji. Ten Hardware Wallet jest kompatybilny z większością oprogramowania do zarządzania Wallet na rynku, w tym między innymi Sparrow Wallet, Specter Desktop, Nunchuk, Keeper. W tym samouczku dowiemy się, jak używać go ze Sparrow Wallet.


Jeśli jesteś początkującym użytkownikiem, najłatwiejszą opcją jest użycie Passport z natywną aplikacją Envoy, opracowaną przez Foundation. Aby dowiedzieć się, jak używać Envoy z Passport, zapoznaj się z tym samouczkiem :


https://planb.network/tutorials/wallet/mobile/envoy-3ae5d6c7-623b-45b3-bb34-abcf9572b7cb

## Rozpakowywanie paszportu


Po otrzymaniu paszportu należy upewnić się, że pudełko i Seal na kartonie są nienaruszone, aby potwierdzić, że paczka nie była otwierana. Podczas konfiguracji zostanie również przeprowadzona programowa weryfikacja autentyczności i integralności urządzenia.


![Image](assets/fr/02.webp)


Zawartość pudełka obejmuje :




- Paszport;
- Kawałek kartonu do zapisania frazy Mnemonic;
- Kabel USB-C do ładowania;
- Karta microSD ;
- Dwa adaptery MicroSD do Lightning lub USB-C ;
- Naklejki.


Na urządzeniu znajdują się :




- Klawiatura (1) ;
- Port USB-C (2);
- Przycisk usuwania (3);
- Przycisk powrotu (4) ;
- Przycisk potwierdzenia (5);
- Podkładka kierunkowa (6);
- Przycisk włączania/wyłączania (7);
- Wskaźnik stanu (8);
- Port microSD (9) ;
- Przycisk zmiany trybu aA1 (10) ;
- Tylna kamera.


![Image](assets/fr/03.webp)


## Paszport startowy


Naciśnij przycisk włączania/wyłączania z boku urządzenia, aby je uruchomić.


![Image](assets/fr/04.webp)


Naciśnij przycisk potwierdzenia, aby przejść do następnego menu.


![Image](assets/fr/05.webp)


W tym samouczku użyjemy Sparrow Wallet do zarządzania Wallet zabezpieczonym paszportem. Wybierz "*Ustawienia ręczne*".


![Image](assets/fr/06.webp)


Następnie zaakceptuj warunki użytkowania.


![Image](assets/fr/07.webp)


Następnym krokiem jest sprawdzenie urządzenia. Potwierdza to autentyczność paszportu i zapewnia, że nie został on naruszony podczas transportu. Zostaniesz poproszony o zeskanowanie kodu QR.


![Image](assets/fr/08.webp)


Wejdź na [oficjalną stronę weryfikacji] (https://validate.foundationdevices.com/) i wybierz "*Passport*".


![Image](assets/fr/09.webp)


Użyj aparatu w paszporcie, aby zeskanować kod QR wyświetlany na stronie.


![Image](assets/fr/10.webp)


Urządzenie wyświetli wówczas 4 słowa.


![Image](assets/fr/11.webp)


Wpisz te słowa na stronie internetowej, aby potwierdzić autentyczność paszportu i kliknij "*Validate*".


![Image](assets/fr/12.webp)


Jeśli pojawi się komunikat "*Passed*", oznacza to, że urządzenie Hardware Wallet jest autentyczne. Można go teraz użyć do zabezpieczenia Bitcoin Wallet.


![Image](assets/fr/13.webp)


Potwierdź wynik testu w paszporcie.


![Image](assets/fr/14.webp)


## Ustawianie kodu PIN


Następnie należy wprowadzić kod PIN. Kod PIN odblokowuje paszport. Zapewnia on zatem ochronę przed nieautoryzowanym dostępem fizycznym. Kod PIN nie bierze udziału w tworzeniu kluczy kryptograficznych Wallet. Tak więc nawet bez dostępu do kodu PIN, posiadanie 12- lub 24-wyrazowej frazy Mnemonic umożliwi odzyskanie dostępu do bitcoinów.


![Image](assets/fr/15.webp)


Zalecamy wybranie możliwie losowego kodu PIN. Należy również pamiętać o zapisaniu tego kodu w miejscu innym niż miejsce przechowywania paszportu (np. w menedżerze haseł).


Możesz wybrać kod PIN składający się z 6 do 12 cyfr. Radzę wybrać jak najdłuższy kod.


Użyj klawiatury, aby wprowadzić numery PIN. Po zakończeniu kliknij przycisk potwierdzenia.


![Image](assets/fr/16.webp)


Potwierdź kod PIN po raz drugi.


![Image](assets/fr/17.webp)


Kod PIN został zarejestrowany.


![Image](assets/fr/18.webp)


## Aktualizacja oprogramowania sprzętowego Passport


Hardware Wallet sugeruje aktualizację oprogramowania sprzętowego. Zalecam natychmiastową aktualizację, aby skorzystać z ulepszeń i poprawek wprowadzonych przez najnowsze wersje. Aby kontynuować, kliknij przycisk potwierdzenia po prawej stronie.


![Image](assets/fr/19.webp)


Passport jest gotowy do odebrania nowego oprogramowania sprzętowego za pośrednictwem karty MicroSD.


![Image](assets/fr/20.webp)


Aby to zrobić, użyj karty MicroSD dołączonej do pudełka Passport (lub innej) i włóż ją do komputera. Pobierz najnowszą wersję oprogramowania układowego z [strony dokumentacji Foundation](https://docs.foundation.xyz/firmware-updates/passport/) lub [ich repozytorium GitHub](https://github.com/Foundation-Devices/passport2/releases).


![Image](assets/fr/21.webp)


Przed zainstalowaniem go na urządzeniu zdecydowanie zalecamy sprawdzenie autentyczności i integralności pobranego oprogramowania układowego. Jeśli potrzebujesz pomocy, zapoznaj się z tym samouczkiem :


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Po sprawdzeniu pliku `.bin` umieść go na karcie MicroSD, a następnie włóż ją do urządzenia Passport. Otworzy się eksplorator plików Passport. Wybierz plik `vN.N.N-passport.bin`.


![Image](assets/fr/22.webp)


Kliknij "*Wybierz*".


![Image](assets/fr/23.webp)


Następnie potwierdź instalację oprogramowania sprzętowego.


![Image](assets/fr/24.webp)


Poczekaj na zakończenie aktualizacji.


![Image](assets/fr/25.webp)


Po zakończeniu aktualizacji wprowadź kod PIN, aby odblokować urządzenie i kontynuować konfigurację.


![Image](assets/fr/26.webp)


## Utwórz nowy Bitcoin Wallet


Teraz nadszedł czas, aby utworzyć nowy Bitcoin Wallet. Kliknij przycisk potwierdzenia.


![Image](assets/fr/27.webp)


Aby utworzyć nowy Wallet, kliknij "*Create New seed*".


![Image](assets/fr/28.webp)


Do wyboru jest 12- lub 24-wyrazowa fraza Mnemonic. Bezpieczeństwo oferowane przez obie opcje jest podobne, więc możesz wybrać tę, która jest najłatwiejsza do zapisania, tj. 12 słów.


![Image](assets/fr/29.webp)


Kliknij "*Kontynuuj*".


![Image](assets/fr/30.webp)


Twój Paszport wyświetli teraz generate "*Backup Code*". Jest to seria liczb, które mogą być użyte do odszyfrowania kopii zapasowej Wallet zapisanej na karcie MicroSD. Ten system kopii zapasowej, specyficzny dla urządzeń Foundation, stanowi dodatkową kopię zapasową frazy Mnemonic, ale nie jest kompatybilny z innym oprogramowaniem Bitcoin.


Jeśli zdecydujesz się użyć tego "*Kodu kopii zapasowej*", pamiętaj, aby przechowywać go w innym miejscu niż kartę MicroSD zawierającą zaszyfrowaną kopię zapasową Wallet. Możesz jednak zrezygnować z tego systemu, jeśli uważasz, że dobra kopia zapasowa frazy Mnemonic jest wystarczająca.


![Image](assets/fr/31.webp)


Wprowadź swój "*Backup Code*", aby potwierdzić, że zapisałeś go poprawnie.


![Image](assets/fr/32.webp)


Jeśli włożono kartę MicroSD, zaszyfrowana kopia zapasowa Wallet została tam zapisana.


![Image](assets/fr/33.webp)


W paszporcie zostanie wyświetlona 12-wyrazowa fraza Mnemonic. Mnemonic zapewnia pełny, nieograniczony dostęp do wszystkich bitcoinów. Każdy, kto posiada tę frazę, może ukraść twoje środki, nawet bez fizycznego dostępu do twojego paszportu.


12-wyrazowa fraza przywraca dostęp do bitcoinów w przypadku utraty, kradzieży lub zniszczenia paszportu. Dlatego bardzo ważne jest, aby zachować go ostrożnie i przechowywać w bezpiecznym miejscu.


Napis można umieścić na kartonie dołączonym do pudełka lub, dla większego bezpieczeństwa, zalecam wygrawerowanie go na podstawie ze stali nierdzewnej, aby chronić go przed pożarem, powodzią lub upadkiem.


Kliknij przycisk potwierdzenia, aby zobaczyć swoją frazę Mnemonic.


![Image](assets/fr/34.webp)


Aby uzyskać więcej informacji na temat prawidłowego sposobu zapisywania i zarządzania frazą Mnemonic, zdecydowanie polecam skorzystanie z tego samouczka, zwłaszcza jeśli jesteś początkującym:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

oczywiście nigdy nie wolno dzielić się tymi słowami w Internecie, tak jak robię to w tym samouczku. Ten przykładowy Wallet będzie używany tylko na Testnet i zostanie usunięty po zakończeniu samouczka.**_


Utwórz fizyczną kopię zapasową tego zdania.


![Image](assets/fr/35.webp)


Paszport został pomyślnie skonfigurowany. Kliknij przycisk potwierdzenia, aby kontynuować.


![Image](assets/fr/36.webp)


## Odkrywanie menu


Passport Interface posiada trzy główne menu:




- "*Konto*";
- "*Więcej*";
- "*Ustawienia*".


Do poruszania się między tymi menu służą strzałki w lewo i w prawo na panelu kierunkowym.


### *Menu "Konto*


W menu "*Konto*" znajdują się główne funkcje Bitcoin Wallet. Transakcję można podpisać za pośrednictwem kamery lub portu MicroSD.


![Image](assets/fr/37.webp)


Podmenu "*Account Tools*" oferuje opcje takie jak weryfikacja Address, podpisywanie wiadomości lub sprawdzanie adresów w Wallet.


![Image](assets/fr/38.webp)


W podmenu "*Manage Account*" można podłączyć Bitcoin Wallet do oprogramowania zarządzającego Wallet (co omówimy w kolejnych krokach tego samouczka) lub wyświetlić i zmienić nazwę konta.


![Image](assets/fr/39.webp)


### Menu "Więcej


W menu "*More*" można utworzyć nowe konto w Wallet, powiązane z tą samą frazą Mnemonic.


![Image](assets/fr/40.webp)


Można również wprowadzić BIP39 passphrase (patrz następna sekcja) lub użyć tymczasowego seed.


![Image](assets/fr/41.webp)


### Menu "Ustawienia


W menu "*Ustawienia*" znajdują się wszystkie ustawienia Wallet i urządzenia.


![Image](assets/fr/42.webp)


Podmenu "*Urządzenie*" umożliwia dostosowanie jasności ekranu, ustawienie opóźnienia przed automatyczną blokadą, zmianę kodu PIN lub zmianę nazwy urządzenia.


![Image](assets/fr/43.webp)


Podmenu "*Backup*" umożliwia wyeksportowanie zaszyfrowanej kopii zapasowej Wallet, sprawdzenie ważności istniejącej kopii zapasowej lub ponowne wyszukanie "*Backup Code*".


![Image](assets/fr/44.webp)


Podmenu "*Firmware*" służy do aktualizacji oprogramowania sprzętowego urządzenia Passport. Zalecamy regularne wykonywanie tych aktualizacji, aby korzystać z najnowszych poprawek i funkcji.


![Image](assets/fr/45.webp)


Podmenu "*Bitcoin*" umożliwia zmianę wyświetlanej jednostki (BTC lub satoshis), zarządzanie możliwym Multisig Wallet lub przejście do trybu "*Testnet*".


![Image](assets/fr/46.webp)


W "*Advanced*" można wyświetlić słowa frazy Mnemonic, wykonać działania na włożonej karcie MicroSD, zresetować Passport do ustawień fabrycznych lub przeprowadzić kontrolę autentyczności, tak jak to miało miejsce wcześniej.


![Image](assets/fr/47.webp)


Można aktywować "*Security Words*", funkcję, która dodaje Layer bezpieczeństwa, wyświetlając dwa określone słowa podczas odblokowywania urządzenia po wprowadzeniu pierwszych czterech cyfr kodu PIN. Słowa te, które zostaną zapisane podczas konfiguracji, zapewniają, że Passport nie został wymieniony ani zmodyfikowany. W przypadku jakichkolwiek rozbieżności w późniejszym terminie zalecamy nieużywanie urządzenia. Zalecam aktywowanie tej opcji, aby zapobiec większości zagrożeń związanych z fizycznym naruszeniem urządzenia.


![Image](assets/fr/48.webp)


Wreszcie, podmenu "*Extensions*" umożliwia aktywację funkcji specyficznych dla niektórych zastosowań urządzenia, takich jak protokół Whirlpool CoinJoin.


![Image](assets/fr/49.webp)


## Dodaj BIP39 passphrase


Przed kontynuowaniem, jeśli chcesz, możesz dodać BIP39 passphrase. BIP39 passphrase to opcjonalne hasło, które można dowolnie wybrać i które jest dodawane do frazy Mnemonic w celu wzmocnienia bezpieczeństwa Wallet. Po włączeniu tej funkcji dostęp do Bitcoin Wallet będzie wymagał zarówno Mnemonic, jak i passphrase. Bez nich odzyskanie Wallet byłoby niemożliwe.


Przed skonfigurowaniem tej opcji w urządzeniu Passport zdecydowanie zaleca się przeczytanie tego artykułu, aby w pełni zrozumieć teoretyczne działanie passphrase i uniknąć błędów, które mogą prowadzić do utraty bitcoinów:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Aby ją aktywować, przejdź do menu "*More*" i kliknij "*Enter passphrase*".


![Image](assets/fr/50.webp)


Wprowadź swoje passphrase za pomocą klawiatury aA1 i upewnij się, że zapisałeś je jeden lub więcej razy na nośniku fizycznym (papierowym lub metalowym). W przykładzie użyłem bardzo słabego passphrase, ale powinieneś wybrać silny, losowy passphrase, zawierający wszystkie typy znaków i wystarczająco długi (jak silne hasło).


![Image](assets/fr/51.webp)


Należy pamiętać, że w hasłach BIP39 wielkość liter ma znaczenie. Jeśli wprowadzisz passphrase nieznacznie różniący się od początkowo skonfigurowanego, Passport nie zgłosi błędu, ale wyprowadzi inny zestaw kluczy kryptograficznych, które nie będą tymi w początkowym Wallet.


Dlatego ważne jest, aby podczas konfiguracji zanotować gdzieś odcisk palca klucza głównego, który zostanie podany w następnym kroku. Na przykład, w moim passphrase `Plan B Network`, mój odcisk palca klucza głównego to `745D526B`.


![Image](assets/fr/52.webp)


Za każdym razem, gdy odblokujesz Passport, będziesz musiał wrócić do tego menu, aby wprowadzić passphrase i zastosować go do Wallet. Aplikacja Passport nie zapisuje passphrase.


Przy każdym odblokowaniu, po zapisaniu passphrase, sprawdź na ekranie potwierdzenia, czy podany odcisk palca jest taki sam, jak ten zapisany podczas konfiguracji. Jeśli tak, passphrase jest prawidłowy i uzyskujesz dostęp do prawidłowego Bitcoin Wallet. Jeśli nie, jesteś na niewłaściwym Wallet i musisz spróbować ponownie, uważając, aby nie popełnić żadnych błędów wejściowych.


Przed otrzymaniem pierwszych bitcoinów na Wallet, **Zalecam wykonanie pustego testu odzyskiwania**. Zanotuj informacje referencyjne, takie jak xpub lub pierwszy otrzymany Address, a następnie usuń Wallet z Paszportu, gdy jest jeszcze pusty (`Ustawienia -> Zaawansowane -> Wymaż Paszport`). Następnie spróbuj przywrócić Wallet przy użyciu papierowych kopii zapasowych frazy Mnemonic i dowolnego passphrase. Sprawdź, czy informacje o plikach cookie wygenerowane po przywróceniu są zgodne z pierwotnie zapisanymi. Jeśli tak, możesz mieć pewność, że Twoje papierowe kopie zapasowe są wiarygodne. Aby dowiedzieć się więcej o tym, jak przeprowadzić odzyskiwanie testowe, zapoznaj się z tym innym samouczkiem :


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

![Image](assets/fr/53.webp)


## Konfiguracja Wallet na Sparrow Wallet


W tym samouczku pokażę zaawansowane użycie Passport z Sparrow Wallet. Jednak Hardware Wallet jest również kompatybilny z Envoy (aplikacja Foundation), Keeper, BlueWallet, Nunchuk, Specter i wieloma innymi...


Zacznij od pobrania i zainstalowania Sparrow Wallet [z oficjalnej strony internetowej](https://sparrowwallet.com/) na swoim komputerze, jeśli jeszcze tego nie zrobiłeś.


![Image](assets/fr/54.webp)


Przed instalacją należy sprawdzić autentyczność i integralność oprogramowania. Jeśli nie wiesz, jak to zrobić, zapoznaj się z tym samouczkiem:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Po otwarciu Sparrow Wallet kliknij zakładkę "*Plik*", a następnie "*Nowy Wallet*".


![Image](assets/fr/55.webp)


Nadaj nazwę swojemu Wallet, a następnie kliknij "*Create Wallet*".


![Image](assets/fr/56.webp)


Wybierz "*Airgapped Hardware Wallet*".


![Image](assets/fr/57.webp)


Kliknij "*Scan...*" obok opcji "*Passport*". Spowoduje to otwarcie kamery internetowej.


![Image](assets/fr/58.webp)


W Hardware Wallet przejdź do menu "*Account*", wybierz podmenu "*Manage Account*" i kliknij "*Connect Wallet*".


![Image](assets/fr/59.webp)


Z wyświetlonej listy rozwijanej wybierz "*Sparrow*".


![Image](assets/fr/60.webp)


Następnie wybierz "*Single-sig*" dla normalnej konfiguracji, bez Multisig.


![Image](assets/fr/61.webp)


Wybierz opcję "*QR Code*".


![Image](assets/fr/62.webp)


Paszport wyświetli dynamiczne kody QR generate. Użyj kamery internetowej komputera, aby zeskanować je do oprogramowania Sparrow.


![Image](assets/fr/63.webp)


Powinieneś teraz zobaczyć swój xpub i odcisk palca klucza głównego, który powinien być zgodny z tym pokazanym w paszporcie po wprowadzeniu passphrase. Kliknij przycisk "*Apply*" (Zastosuj).


![Image](assets/fr/64.webp)


Ustaw silne hasło, aby zabezpieczyć dostęp do urządzenia Sparrow Wallet. Hasło to będzie chronić klucze publiczne, adresy, etykiety i historię transakcji przed nieautoryzowanym dostępem. Dobrym pomysłem jest zapisanie tego hasła w menedżerze haseł, aby go nie zapomnieć.


![Image](assets/fr/65.webp)


Następnie Passport wyświetli monit o zeskanowanie pierwszego odbioru Address w celu potwierdzenia, że import się powiódł.


![Image](assets/fr/66.webp)


W aplikacji Sparrow przejdź do zakładki "*Odbierz*" i zeskanuj kod QR pierwszego Address.


![Image](assets/fr/67.webp)


Jeśli operacja się powiedzie, w paszporcie pojawi się komunikat "*Verified*".


![Image](assets/fr/68.webp)


Potwierdza to, że import się powiódł.


![Image](assets/fr/69.webp)


## Odbieranie bitcoinów


Teraz, gdy Paszport jest skonfigurowany, możesz odebrać swój pierwszy Sats na nowym Bitcoin Wallet. Aby to zrobić, w aplikacji Sparrow kliknij menu "*Odbierz*".


![Image](assets/fr/70.webp)


Sparrow wyświetli pierwszy pusty paragon Address w Wallet. Można dodać etykietę.


![Image](assets/fr/71.webp)


Przed użyciem sprawdzimy Address na ekranie Passport, aby upewnić się, że należy do naszego Bitcoin Wallet. W aplikacji Sparrow można powiększyć kod QR Address, klikając go w razie potrzeby. W menu Passport "*Konto*" wybierz "*Narzędzia konta*".


![Image](assets/fr/72.webp)


Kliknij "*Verify Address*", a następnie zeskanuj kod QR wyświetlony na urządzeniu Sparrow Wallet.


![Image](assets/fr/73.webp)


Upewnij się, że Address wyświetlany na Paszporcie odpowiada dokładnie temu wyświetlanemu na Sparrow i że pojawia się "*Verified*".


![Image](assets/fr/74.webp)


Możesz teraz używać go do otrzymywania bitcoinów. Gdy transakcja zostanie rozgłaszana w sieci, pojawi się na Sparrow. Poczekaj, aż otrzymasz wystarczającą liczbę potwierdzeń, aby uznać transakcję za ostateczną.


![Image](assets/fr/75.webp)


## Wysyłanie bitcoinów


Teraz, gdy masz już kilka Sats w swoim Wallet, możesz je również wysłać. Aby to zrobić, kliknij menu "*UTXO*".


![Image](assets/fr/76.webp)


Wybierz UTXO, których chcesz użyć jako danych wejściowych dla tej transakcji, a następnie kliknij "*Wyślij wybrane*".


![Image](assets/fr/77.webp)


Wprowadź Address odbiorcy, etykietę przypominającą o celu transakcji i kwotę, którą chcesz wysłać na ten Address.


![Image](assets/fr/78.webp)


Dostosuj stawkę opłaty do aktualnych warunków rynkowych, a następnie kliknij "*Twórz transakcję*".


![Image](assets/fr/79.webp)


Sprawdź, czy wszystkie parametry transakcji są prawidłowe, a następnie kliknij "*Finalize Transaction for Signing*".


![Image](assets/fr/80.webp)


Kliknij "*Pokaż QR*", aby wyświetlić PSBT (*Partially Signed Bitcoin Transaction*). Sparrow utworzył transakcję, ale nadal brakuje jej podpisów do odblokowania bitcoinów użytych w danych wejściowych. Te podpisy mogą być wykonane tylko przez Passport, który hostuje seed, dając dostęp do kluczy prywatnych potrzebnych do podpisania transakcji.


![Image](assets/fr/81.webp)


W aplikacji Passport przejdź do menu "*Account*" i kliknij "*Sign with QR Code*".


![Image](assets/fr/82.webp)


Zeskanuj PSBT (*Partially Signed Bitcoin Transaction*) wyświetlany na Sparrow Wallet.


![Image](assets/fr/83.webp)


Potwierdź, że odbierany numer Address i wysłana kwota są prawidłowe, a następnie naciśnij przycisk potwierdzenia.


![Image](assets/fr/84.webp)


Sprawdź Exchange Address. W moim przykładzie nie ma żadnego, ponieważ transakcja obejmuje pojedyncze wyjście.


![Image](assets/fr/85.webp)


Upewnij się, że opłata jest taka, jaką wybrałeś.


![Image](assets/fr/86.webp)


Jeśli wszystkie informacje są poprawne, kliknij przycisk potwierdzenia, aby podpisać transakcję.


![Image](assets/fr/87.webp)


W aplikacji Sparrow Wallet kliknij "*Scan QR*" i zeskanuj kod QR wyświetlony na paszporcie.


![Image](assets/fr/88.webp)


Podpisana transakcja jest teraz gotowa do transmisji w sieci Bitcoin i włączenia do bloku przez Miner. Jeśli wszystko jest w porządku, kliknij "*Broadcast Transaction*".


![Image](assets/fr/89.webp)


Twoja transakcja została wysłana i oczekuje na potwierdzenie.


![Image](assets/fr/90.webp)


Gratulacje, wiesz już jak skonfigurować i używać Passport. Jeśli ten poradnik okazał się przydatny, będę wdzięczny za pozostawienie poniżej kciuka Green. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dzięki za udostępnienie!


Więcej informacji można znaleźć w naszym samouczku na temat oprogramowania Liana:


https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04
