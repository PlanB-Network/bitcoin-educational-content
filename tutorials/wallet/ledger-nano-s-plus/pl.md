---
name: Ledger Nano S Plus
description: Konfiguracja i użytkowanie Ledger Nano S Plus
---
![cover](assets/cover.webp)


Hardware Wallet to urządzenie elektroniczne przeznaczone do zarządzania i zabezpieczania kluczy prywatnych Bitcoin Wallet. W przeciwieństwie do portfeli programowych (lub portfeli Hot) instalowanych na maszynach ogólnego przeznaczenia często podłączonych do Internetu, portfele sprzętowe pozwalają na fizyczną izolację kluczy prywatnych, zmniejszając ryzyko włamania i kradzieży.


Głównym celem Hardware Wallet jest zminimalizowanie funkcjonalności urządzenia tak bardzo, jak to możliwe, aby zmniejszyć jego powierzchnię ataku. Mniejsza powierzchnia ataku oznacza również mniej potencjalnych wektorów ataku, tj. mniej słabych punktów w systemie, które atakujący mogliby wykorzystać, aby uzyskać dostęp do bitcoinów.


Zaleca się korzystanie z Hardware Wallet w celu zabezpieczenia bitcoinów, zwłaszcza w przypadku posiadania znacznych kwot, zarówno pod względem wartości bezwzględnej, jak i proporcji całkowitych aktywów.


Portfele sprzętowe są używane w połączeniu z oprogramowaniem do zarządzania Wallet na komputerze lub smartfonie. Oprogramowanie to zarządza tworzeniem transakcji, ale podpis kryptograficzny niezbędny do walidacji tych transakcji jest wykonywany tylko w Hardware Wallet. Oznacza to, że klucze prywatne nigdy nie są narażone na potencjalnie wrażliwe środowisko.


Portfele sprzętowe zapewniają użytkownikowi podwójną ochronę: z jednej strony zabezpieczają bitcoiny przed zdalnymi atakami, utrzymując klucze prywatne w trybie offline, a z drugiej strony generalnie oferują lepszą odporność fizyczną na próby wyodrębnienia kluczy. I to właśnie na podstawie tych 2 kryteriów bezpieczeństwa można ocenić i uszeregować różne modele dostępne na rynku.


W tym poradniku proponuję odkryć jedno z takich rozwiązań: **Ledger Nano S Plus**.


![NANO S PLUS LEDGER](assets/notext/01.webp)


## Wprowadzenie do Ledger Nano S Plus


Ledger Nano S Plus to Hardware Wallet produkowany przez francuską firmę Ledger, sprzedawany w cenie 79 €.


![NANO S PLUS LEDGER](assets/notext/02.webp)


Nano S Plus jest wyposażony w chip z certyfikatem CC EAL6+ ("*secure element*"), który zapewnia zaawansowaną ochronę przed fizycznymi atakami na sprzęt. Ekran i przyciski są bezpośrednio kontrolowane przez ten chip. Często podnoszonym punktem krytyki jest to, że kod tego chipu nie jest open-source, co wymaga pewnego zaufania do integralności tego komponentu. Niemniej jednak element ten jest kontrolowany przez niezależnych ekspertów.


Pod względem użytkowania, Ledger Nano S Plus działa wyłącznie poprzez przewodowe połączenie USB-C.


Ledger wyróżnia się na tle swoich konkurentów zawsze bardzo szybkim wdrażaniem nowych funkcji Bitcoin, takich jak na przykład Taproot lub Miniscript, co jest bardzo cenione.

Po przetestowaniu stwierdzam, że Ledger Nano S Plus jest doskonałym podstawowym Hardware Wallet. Oferuje wysoki poziom bezpieczeństwa za rozsądną cenę. Jego główną wadą w porównaniu do innych urządzeń w tym samym przedziale cenowym jest fakt, że kod oprogramowania układowego nie jest open-source. Ponadto ekran Nano S Plus jest stosunkowo mały w porównaniu do droższych modeli, takich jak Ledger Flex lub Coldcard Q1. Niemniej jednak, Interface jest bardzo dobrze zaprojektowany: pomimo dwóch przycisków i małego ekranu, pozostaje łatwy w użyciu, w tym w przypadku zaawansowanych funkcji, takich jak BIP39 passphrase. Ledger Nano S Plus nie ma baterii, złącza Air-gap, kamery ani portu micro SD, ale jest to całkiem normalne w tym przedziale cenowym.


Moim zdaniem Ledger Nano S Plus jest dobrą opcją do zabezpieczenia Bitcoin Wallet i jest odpowiedni zarówno dla początkujących, jak i średnio zaawansowanych użytkowników. Jednak w tym przedziale cenowym osobiście wolę Trezor Safe 3, który oferuje mniej więcej te same opcje. Zaletą Trezora, moim zdaniem, jest zarządzanie jego bezpiecznym elementem: fraza i klucze Mnemonic są zarządzane wyłącznie przez kod open-source, ale nadal korzystają z ochrony chipa. Wadą Trezora jest to, że czasami bardzo wolno wdraża nowe funkcje, w przeciwieństwie do Ledger.


## Jak kupić Ledger Nano S Plus?


Ledger Nano S Plus jest dostępny w sprzedaży [na oficjalnej stronie internetowej](https://shop.Ledger.com/products/Ledger-nano-s-plus). Aby kupić go w fizycznym sklepie, można również znaleźć [listę certyfikowanych sprzedawców](https://www.Ledger.com/reseller) na stronie Ledger.


## Wymagania wstępne


Po otrzymaniu Ledger Nano, pierwszym krokiem jest sprawdzenie opakowania, aby upewnić się, że nie zostało ono otwarte. Jeśli jest uszkodzone, może to oznaczać, że Hardware Wallet został naruszony i może nie być autentyczny.


Po otwarciu w pudełku powinny znajdować się następujące elementy:


- Ledger Nano S Plus;
- Kabel USB-C do USB-A;
- Podręcznik użytkownika;
- Karty do zapisania frazy Mnemonic.


Do tego samouczka potrzebne będą 2 aplikacje: Ledger Live do inicjalizacji Ledger oraz Sparrow Wallet do zarządzania Bitcoin Wallet. Pobierz [Ledger Live](https://www.Ledger.com/Ledger-live) i [Sparrow Wallet](https://sparrowwallet.com/download/) z ich oficjalnych stron internetowych.


![NANO S PLUS LEDGER](assets/notext/03.webp)

W przypadku tych dwóch programów zdecydowanie zalecam sprawdzenie zarówno ich autentyczności (za pomocą GnuPG), jak i integralności (za pomocą Hash) przed zainstalowaniem ich na komputerze. Jeśli nie jesteś pewien, jak to zrobić, możesz skorzystać z tego samouczka:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Jak zainicjować Ledger Nano?


Podłącz Nano do komputera, na którym zainstalowane są Ledger Live i Sparrow Wallet. Aby nawigować na Ledger, użyj lewego przycisku, aby przejść w lewo i prawego przycisku, aby przejść w prawo. Aby wybrać lub potwierdzić opcję, naciśnij oba przyciski jednocześnie.


![NANO S PLUS LEDGER](assets/notext/04.webp)


Przewiń różne strony wprowadzające, a następnie kliknij 2 przyciski, aby rozpocząć.


![NANO S PLUS LEDGER](assets/notext/05.webp)


Wybierz opcję "*Setup as a new device*".


![NANO S PLUS LEDGER](assets/notext/06.webp)


Wybierz kod PIN, który zostanie użyty do odblokowania Ledger. Jest to zatem zabezpieczenie przed nieautoryzowanym dostępem fizycznym. Ten kod PIN nie bierze udziału w tworzeniu kluczy kryptograficznych Wallet. Tak więc, nawet bez dostępu do tego kodu PIN, posiadanie 24-wyrazowej frazy Mnemonic pozwoli ci odzyskać dostęp do twoich bitcoinów.


![NANO S PLUS LEDGER](assets/notext/07.webp)


Zaleca się wybranie 8-cyfrowego kodu PIN, możliwie jak najbardziej losowego. Należy również zapisać ten kod w innym miejscu niż to, w którym przechowywany jest telefon Ledger Nano S Plus (na przykład w menedżerze haseł).


Użyj przycisków, aby przejść nad cyframi, a następnie wybierz każdą cyfrę, klikając jednocześnie oba przyciski.


![NANO S PLUS LEDGER](assets/notext/08.webp)


Wprowadź kod PIN po raz drugi, aby go potwierdzić.


![NANO S PLUS LEDGER](assets/notext/09.webp)


Nano zawiera instrukcje dotyczące zarządzania frazą odzyskiwania.


**Ta fraza Mnemonic daje pełny i nieograniczony dostęp do wszystkich bitcoinów**. Każdy, kto posiada tę frazę, może ukraść środki, nawet bez fizycznego dostępu do Ledger. 24-wyrazowa fraza umożliwia przywrócenie dostępu do bitcoinów w przypadku utraty, kradzieży lub uszkodzenia Ledger Nano. Dlatego bardzo ważne jest, aby starannie ją zapisać i przechowywać w bezpiecznym miejscu.


Możesz zapisać go na kartonowym papierze dołączonym do Ledger lub, dla większego bezpieczeństwa, zalecam wygrawerowanie go na nośniku ze stali nierdzewnej, aby zabezpieczyć się przed ryzykiem pożaru, powodzi lub zawalenia.


Możesz przeglądać te instrukcje i pomijać strony, klikając prawy przycisk.


![NANO S PLUS LEDGER](assets/notext/10.webp)

Ledger utworzy frazę Mnemonic przy użyciu generatora liczb losowych. Upewnij się, że nie jesteś obserwowany podczas tej operacji. Zapisz słowa dostarczone przez Ledger na wybranym nośniku fizycznym. W zależności od strategii bezpieczeństwa można rozważyć utworzenie kilku pełnych fizycznych kopii frazy (ale co ważne, nie należy ich dzielić). Ważne jest, aby słowa były ponumerowane i ułożone w kolejności.

***Oczywiście nigdy nie należy udostępniać tych słów w Internecie, w przeciwieństwie do tego, co robię w tym samouczku. Ten przykład Wallet będzie używany tylko na Testnet i zostanie usunięty po zakończeniu samouczka.***


![NANO S PLUS LEDGER](assets/notext/11.webp)


Aby przejść do kolejnych słów, kliknij prawy przycisk.


![NANO S PLUS LEDGER](assets/notext/12.webp)


Po zanotowaniu wszystkich słów kliknij 2 przyciski, aby przejść do następnego kroku.


![NANO S PLUS LEDGER](assets/notext/13.webp)


Kliknij dwa przyciski "*Confirm your Recovery phrase*", a następnie wybierz słowa frazy Mnemonic w ich kolejności, aby potwierdzić, że zostały one poprawnie zapisane. Użyj lewego i prawego przycisku, aby poruszać się między opcjami, a następnie wybierz właściwe słowo, klikając 2 przyciski. Kontynuuj tę procedurę do 24. słowa.


![NANO S PLUS LEDGER](assets/notext/14.webp)


Jeśli potwierdzana fraza odpowiada dokładnie tej, którą Ledger dostarczył w poprzednim kroku, można kontynuować. Jeśli nie, oznacza to, że fizyczna kopia zapasowa frazy Mnemonic jest nieprawidłowa i należy ponownie uruchomić proces.


![NANO S PLUS LEDGER](assets/notext/15.webp)


I gotowe, seed został poprawnie utworzony na Ledger Nano S Plus. Przed przystąpieniem do tworzenia nowego Bitcoin Wallet z tego seed, przeanalizujmy razem ustawienia urządzenia.


## Jak zmodyfikować ustawienia Ledger?


Aby uzyskać dostęp do ustawień, przytrzymaj 2 przyciski przez kilka sekund.


![NANO S PLUS LEDGER](assets/notext/16.webp)


Kliknij menu "*Ustawienia*".


![NANO S PLUS LEDGER](assets/notext/17.webp)


I wybierz "*Ogólne*".


![NANO S PLUS LEDGER](assets/notext/18.webp)


W menu "*Language*" można zmienić język wyświetlacza.


![NANO S PLUS LEDGER](assets/notext/19.webp)


W menu "*Jasność*" można dostosować jasność ekranu. Pozostałe ustawienia ogólne na razie nas nie interesują.


![NANO S PLUS LEDGER](assets/notext/20.webp)


Teraz przejdź do sekcji ustawień "*Security*".


![NANO S PLUS LEDGER](assets/notext/21.webp)


"*Zmień PIN*" umożliwia zmianę kodu PIN.

![NANO S PLUS LEDGER](assets/notext/22.webp)

"*passphrase*" umożliwia skonfigurowanie BIP39 passphrase. passphrase to opcjonalne hasło, które w połączeniu z frazą odzyskiwania zapewnia dodatkowy Layer bezpieczeństwa dla Wallet.


![NANO S PLUS LEDGER](assets/notext/23.webp)


Obecnie klucz Wallet jest generowany na podstawie frazy Mnemonic składającej się z 24 słów. Ta fraza odzyskiwania jest bardzo ważna, ponieważ umożliwia przywrócenie wszystkich kluczy Wallet w przypadku ich utraty. Stanowi ona jednak pojedynczy punkt awarii (SPOF). Jeśli zostanie on naruszony, bitcoiny są w niebezpieczeństwie. W tym miejscu pojawia się passphrase. Jest to opcjonalne hasło, które można dowolnie wybrać, które dodaje się do frazy Mnemonic w celu zwiększenia bezpieczeństwa Wallet.


Kodu passphrase nie należy mylić z kodem PIN. Odgrywa on rolę w tworzeniu kluczy kryptograficznych. Działa w parze z frazą Mnemonic, zmieniając seed, z którego generowane są klucze. Tak więc, nawet jeśli ktoś uzyska 24-wyrazową frazę, bez passphrase nie będzie mógł uzyskać dostępu do Twoich środków. Użycie passphrase zasadniczo tworzy nowy Wallet z odrębnymi kluczami. Modyfikacja (nawet niewielka) passphrase spowoduje, że generate będzie innym Wallet.


passphrase to bardzo potężne narzędzie zwiększające bezpieczeństwo bitcoinów. Jednak bardzo ważne jest, aby zrozumieć, jak działa przed jego wdrożeniem, aby uniknąć utraty dostępu do Wallet. Dlatego radzę zapoznać się z tym innym samouczkiem dedykowanym, jeśli chcesz skonfigurować passphrase na swoim Ledger:


https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

Menu "*PIN lock*" pozwala skonfigurować i aktywować automatyczne blokowanie Ledger po określonym czasie bezczynności.


![NANO S PLUS LEDGER](assets/notext/24.webp)


Menu "* Wygaszacz ekranu*" umożliwia dostosowanie trybu uśpienia Ledger Nano. Należy pamiętać, że wygaszacz ekranu nie wymaga wprowadzenia kodu PIN po przebudzeniu, chyba że opcja "*Blokada PIN*" zostanie aktywowana w trybie uśpienia. Funkcja ta jest szczególnie przydatna w przypadku urządzeń Ledger Nano X wyposażonych w baterię w celu zmniejszenia zużycia energii.


![NANO S PLUS LEDGER](assets/notext/25.webp)


Wreszcie, menu "*Resetuj urządzenie*" umożliwia zresetowanie Ledger. Resetuj urządzenie tylko wtedy, gdy masz pewność, że nie zawiera ono żadnych kluczy zabezpieczających bitcoiny, ponieważ możesz trwale utracić dostęp do swoich środków. Opcja ta może być przydatna do przeprowadzenia pustego testu odzyskiwania, ale o tym opowiem nieco później.


![NANO S PLUS LEDGER](assets/notext/26.webp)

## Jak zainstalować aplikację Bitcoin?


Rozpocznij od uruchomienia oprogramowania Ledger Live na komputerze, a następnie podłącz i odblokuj Ledger Nano. W Ledger Live przejdź do menu "*My Ledger*". Zostaniesz poproszony o autoryzację dostępu do swojego Nano.


![NANO S PLUS LEDGER](assets/notext/27.webp)


Zatwierdź dostęp do Ledger, klikając dwa przyciski.


![NANO S PLUS LEDGER](assets/notext/28.webp)


Po pierwsze, w Ledger Live, upewnij się, że pojawia się "*Genuine check*". Potwierdza to, że urządzenie jest autentyczne.


![NANO S PLUS LEDGER](assets/notext/29.webp)


Jeśli oprogramowanie sprzętowe Ledger Nano nie jest aktualne, Ledger Live automatycznie zaproponuje jego aktualizację. W razie potrzeby kliknij "*Update firmware*", a następnie "*Install update*", aby rozpocząć instalację. Na Ledger kliknij dwa przyciski, aby potwierdzić, a następnie poczekaj podczas instalacji.


Na koniec dodamy aplikację Bitcoin. Aby to zrobić, w Ledger Live kliknij przycisk "*Install*" obok "*Bitcoin (BTC)*".


![NANO S PLUS LEDGER](assets/notext/30.webp)


Aplikacja zostanie zainstalowana na urządzeniu Nano.


![NANO S PLUS LEDGER](assets/notext/31.webp)


Od tej chwili oprogramowanie Ledger Live nie będzie już potrzebne do regularnego zarządzania Wallet. Od czasu do czasu można do niego wrócić, aby zaktualizować oprogramowanie sprzętowe, gdy dostępne są nowe wersje. Do wszystkiego innego będziemy używać Sparrow Wallet, który jest znacznie bardziej wszechstronnym narzędziem do efektywnego zarządzania Bitcoin Wallet.


![NANO S PLUS LEDGER](assets/notext/32.webp)


## Jak skonfigurować nowy Bitcoin Wallet za pomocą Sparrow?


Otwórz Sparrow Wallet i pomiń strony wprowadzające, aby uzyskać dostęp do ekranu głównego. Sprawdź, czy jesteś prawidłowo połączony z węzłem, obserwując przełącznik znajdujący się w prawym dolnym rogu ekranu.


![NANO S PLUS LEDGER](assets/notext/33.webp)


Zdecydowanie zalecam korzystanie z własnego węzła Bitcoin. W tym samouczku używam węzła publicznego (żółty), ponieważ korzystam z Testnet, ale do normalnego użytku lepiej jest wybrać lokalny Bitcoin Core (Green) lub serwer Electrum podłączony do zdalnego węzła (niebieski).


Kliknij menu "*Plik*", a następnie "*Nowy Wallet*".


![NANO S PLUS LEDGER](assets/notext/34.webp)


Wybierz nazwę dla tego Wallet, a następnie kliknij "*Create Wallet*".


![NANO S PLUS LEDGER](assets/notext/35.webp)


W menu rozwijanym "*Typ skryptu*" wybierz typ skryptu, który będzie używany do zabezpieczenia twoich bitcoinów. Zalecam wybranie "*Taproot*" lub, jeśli nie jest dostępny, "*Native SegWit*".


![NANO S PLUS LEDGER](assets/notext/36.webp)

Kliknij przycisk "*Podłączono Hardware Wallet*".

![NANO S PLUS LEDGER](assets/notext/37.webp)


Jeśli jeszcze tego nie zrobiłeś, podłącz Ledger Nano S Plus do komputera, odblokuj go kodem PIN, a następnie otwórz aplikację "*Bitcoin*", klikając 2 przyciski raz na logo Bitcoin.


*W tym samouczku używam aplikacji Bitcoin Testnet, ale procedura pozostaje taka sama dla Mainnet.*


![NANO S PLUS LEDGER](assets/notext/38.webp)


W aplikacji Sparrow kliknij przycisk "*Scan*".


![NANO S PLUS LEDGER](assets/notext/39.webp)


Następnie kliknij "*Import Keystore*".


![NANO S PLUS LEDGER](assets/notext/40.webp)


Możesz teraz zobaczyć szczegóły swojego Wallet, w tym rozszerzony klucz publiczny pierwszego konta. Kliknij przycisk "*Zastosuj*", aby sfinalizować tworzenie Wallet.


![NANO S PLUS LEDGER](assets/notext/41.webp)


Wybierz silne hasło, aby zabezpieczyć dostęp do Sparrow Wallet. To hasło zapewni bezpieczeństwo dostępu do danych Wallet w Sparrow, co pomaga chronić klucze publiczne, adresy, etykiety i historię transakcji przed nieautoryzowanym dostępem.


Radzę zapisać to hasło w menedżerze haseł, aby go nie zapomnieć.


![NANO S PLUS LEDGER](assets/notext/42.webp)


I gotowe, twój Wallet został stworzony!


![NANO S PLUS LEDGER](assets/notext/43.webp)


Przed otrzymaniem pierwszych bitcoinów w Wallet, **Zalecam wykonanie testu odzyskiwania na sucho**. Zanotuj informacje referencyjne, takie jak xpub, a następnie zresetuj Ledger Nano, gdy Wallet jest nadal pusty. Następnie spróbuj przywrócić Wallet na Ledger przy użyciu papierowych kopii zapasowych. Sprawdź, czy plik xpub wygenerowany po przywróceniu jest zgodny z początkowo zapisanym. Jeśli tak, można mieć pewność, że papierowe kopie zapasowe są niezawodne.


Aby dowiedzieć się więcej o tym, jak wykonać test odzyskiwania, radzę zapoznać się z tym innym samouczkiem:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Jak odbierać bitcoiny za pomocą Ledger Nano?


Kliknij zakładkę "*Odbierz*".


![NANO S PLUS LEDGER](assets/notext/44.webp)


Podłącz Ledger Nano S Plus do komputera, odblokuj go kodem PIN, a następnie otwórz aplikację "*Bitcoin*".


![NANO S PLUS LEDGER](assets/notext/45.webp)

Przed użyciem Address dostarczonego przez Sparrow Wallet należy zweryfikować na ekranie Ledger. Ta praktyka pozwala potwierdzić, że Address wyświetlany na Sparrow nie jest fałszywy i że Hardware Wallet rzeczywiście posiada klucz prywatny niezbędny do późniejszego wydania bitcoinów zabezpieczonych tym Address. Pomaga to uniknąć kilku rodzajów ataków.

Aby przeprowadzić tę weryfikację, kliknij przycisk "*Wyświetl Address*".


![NANO S PLUS LEDGER](assets/notext/46.webp)


Upewnij się, że numer Address wyświetlany na urządzeniu Ledger jest zgodny z numerem wskazanym na urządzeniu Sparrow Wallet. Zaleca się również przeprowadzenie tej weryfikacji tuż przed przekazaniem Address nadawcy, aby upewnić się co do jego ważności. Możesz użyć przycisków, aby wyświetlić pełny Address.


![NANO S PLUS LEDGER](assets/notext/47.webp)


Następnie kliknij "*Approve*", jeśli adresy są rzeczywiście identyczne.


![NANO S PLUS LEDGER](assets/notext/48.webp)


Możesz dodać "*Label*", aby opisać źródło bitcoinów, które zostaną zabezpieczone za pomocą tego Address. Jest to dobra praktyka, która pomaga lepiej zarządzać UTXO.


![NANO S PLUS LEDGER](assets/notext/49.webp)


Więcej informacji na temat etykietowania można znaleźć w tym poradniku:


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Następnie można użyć Address do otrzymywania bitcoinów.


![NANO S PLUS LEDGER](assets/notext/50.webp)


## Jak wysyłać bitcoiny za pomocą Ledger Nano?


Teraz, gdy otrzymałeś swoje pierwsze Sats w Wallet zabezpieczonym Nano S Plus, możesz je również wydać! Podłącz swój Ledger do komputera, odblokuj go, uruchom aplikację Sparrow Wallet, a następnie przejdź do zakładki "*Wyślij*", aby utworzyć nową transakcję.


![NANO S PLUS LEDGER](assets/notext/51.webp)


Jeśli chcesz wykonać "*coin control*", czyli konkretnie wybrać, które UTXO mają zostać wykorzystane w transakcji, przejdź do zakładki "*UTXOs*". Wybierz UTXO, które chcesz wydać, a następnie kliknij "*Wyślij wybrane*". Nastąpi przekierowanie do tego samego ekranu w zakładce "*Wyślij*", ale z UTXO już wybranymi do transakcji.


![NANO S PLUS LEDGER](assets/notext/52.webp)


Wprowadź adres docelowy Address. Można również wprowadzić wiele adresów, klikając przycisk "*+ Add*".


![NANO S PLUS LEDGER](assets/notext/53.webp)


Zanotuj "*Label*", aby zapamiętać cel tego wydatku.


![NANO S PLUS LEDGER](assets/notext/54.webp)


Wybierz kwotę wysyłaną do tego Address.


![NANO S PLUS LEDGER](assets/notext/55.webp)


Dostosuj stawkę opłaty transakcyjnej do aktualnej sytuacji rynkowej.


![NANO S PLUS LEDGER](assets/notext/56.webp)

Upewnij się, że wszystkie ustawienia transakcji są prawidłowe, a następnie kliknij "*Twórz transakcję*".

![NANO S PLUS LEDGER](assets/notext/57.webp)


Jeśli wszystko wygląda dobrze, kliknij "*Finalizuj transakcję do podpisania*".


![NANO S PLUS LEDGER](assets/notext/58.webp)


Kliknij "*Podpisz*".


![NANO S PLUS LEDGER](assets/notext/59.webp)


Kliknij "*Zapisz*" obok swojego Ledger Nano S Plus.


![NANO S PLUS LEDGER](assets/notext/60.webp)


Zweryfikuj ustawienia transakcji na ekranie Ledger, w tym otrzymany Address odbiorcy, wysłaną kwotę i kwotę opłaty.


![NANO S PLUS LEDGER](assets/notext/61.webp)


Jeśli wszystko wygląda dobrze, naciśnij dwa przyciski "*Podpisz transakcję*", aby ją podpisać.


![NANO S PLUS LEDGER](assets/notext/62.webp)


Transakcja została podpisana. Sprawdź dokładnie, czy wszystko wygląda dobrze, a następnie kliknij "*Broadcast Transaction*", aby rozgłosić ją w sieci Bitcoin.


![NANO S PLUS LEDGER](assets/notext/63.webp)


Można go znaleźć w zakładce "*Transakcje*" w Sparrow Wallet.


![NANO S PLUS LEDGER](assets/notext/64.webp)


Gratulacje, jesteś teraz na bieżąco z podstawowym użyciem Ledger Nano S Plus z Sparrow Wallet! W przyszłym samouczku zobaczymy, jak używać Ledger z Liana, aby wykorzystać Miniscript.


Jeśli ten poradnik okazał się pomocny, będę wdzięczny za pozostawienie kciuka w górę poniżej. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dziękuję bardzo!


Polecam również zapoznać się z tym kompletnym samouczkiem na temat Ledger Flex:


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a