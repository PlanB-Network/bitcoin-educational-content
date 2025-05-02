---
name: Samourai Wallet - Odzysk
description: Jak odzyskać bitcoiny, które utknęły na Samourai Wallet?
---

![cover](assets/cover.webp)


Po aresztowaniu założycieli Samourai Wallet i przejęciu ich serwerów 24 kwietnia, niektóre funkcje aplikacji nie działają, a użytkownicy, którzy nie mają własnego Dojo, nie mogą już transmitować transakcji.


Po udzieleniu pomocy kilku użytkownikom w odzyskaniu ich bitcoinów w ostatnich dniach, uważam, że spotkałem się z większością problemów, które mogą pojawić się podczas przywracania Samourai Wallet. Dlatego też niniejszy poradnik rozpocznie się od raportu sytuacyjnego, aby zidentyfikować funkcje, które nadal działają i te, które nie są już dostępne w ekosystemie Samourai Wallet oraz oprogramowanie, na które miał wpływ ten incydent. Następnie przejdziemy krok po kroku do odzyskiwania Samourai Wallet przy użyciu oprogramowania Sparrow Wallet. Przeanalizujemy wszystkie potencjalne przeszkody napotkane podczas tego procesu i zobaczymy rozwiązania, które pozwolą je rozwiązać. Wreszcie, w ostatniej części, odkryjesz potencjalne zagrożenia dla swojej prywatności po przejęciu serwera.


wielkie podziękowania dla [@Louferlou](https://twitter.com/Louferlou), który pomógł kilku użytkownikom w ich odzyskaniu i podzielił się ze mną swoimi doświadczeniami, a także przyczynił się do testów w celu ustalenia, co nadal działa


## Czy Samourai Wallet nadal działa?


Tak, **aplikacja Samourai Wallet nadal działa**, ale pod pewnymi warunkami.


Po pierwsze, konieczne jest, aby aplikacja była wcześniej zainstalowana na smartfonie. Sklep Google Play usunął aplikację, a plik APK był hostowany na przejętej stronie internetowej. Dlatego instalacja Samourai jest obecnie skomplikowana. Możesz znaleźć pliki APK w Internecie, ale odradzam ich pobieranie, chyba że masz pewność co do źródła.


Biorąc pod uwagę, że strona Samourai Wallet nie jest już dostępna w sklepie Google Play, nie jest możliwe wyłączenie automatycznych aktualizacji. Jeśli aplikacja powróci na platformy pobierania, rozsądnie byłoby **wyłączyć automatyczne aktualizacje** do czasu uzyskania większej ilości informacji na temat rozwoju sprawy.


Jeśli Samourai Wallet jest już zainstalowany na smartfonie, nadal powinieneś mieć dostęp do aplikacji. Aby korzystać z funkcji Wallet Samourai, konieczne jest podłączenie Dojo. Wcześniej użytkownicy bez osobistego Dojo polegali na serwerach Samourai, aby uzyskać dostęp do informacji Bitcoin Blockchain i transmitować transakcje. Po przejęciu tych serwerów aplikacja nie może już uzyskać dostępu do tych danych.

Jeśli wcześniej nie miałeś podłączonego Dojo, ale masz go teraz, możesz skonfigurować go tak, aby ponownie korzystał z aplikacji Samourai. Obejmuje to sprawdzenie kopii zapasowych, usunięcie Wallet (Wallet, nie aplikacji) i odzyskanie Wallet poprzez podłączenie Dojo do aplikacji. Więcej szczegółów na temat tych kroków można znaleźć w [tym samouczku, w sekcji "_Przygotowanie portfela Samourai_" : CoinJoin - DOJO](https://planb.network/tutorials/privacy/On-Chain/CoinJoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2).

Jeśli Twoja aplikacja Samourai była już połączona z Twoim własnym Dojo, to część Wallet działa idealnie. Nadal możesz zobaczyć swoje saldo i transmitować transakcje. Pomimo wszystkiego, co się dzieje, uważam, że Samourai Wallet pozostaje obecnie najlepszym mobilnym oprogramowaniem Wallet. Osobiście planuję nadal z niego korzystać.


Głównym problemem jest brak dostępu do kont Whirlpool z poziomu aplikacji. Zazwyczaj Samourai próbuje nawiązać połączenie z Whirlpool CLI i uruchomić cykle CoinJoin przed udzieleniem dostępu do tych kont. Ponieważ jednak połączenie to nie jest już możliwe, aplikacja kontynuuje wyszukiwanie w nieskończoność, nie dając dostępu do kont Whirlpool. W takim przypadku można odzyskać te konta na innym oprogramowaniu Wallet, zachowując jedynie konto depozytowe na Samourai.


### Jakie narzędzia są nadal dostępne na Samourai?


Z drugiej strony, niektóre narzędzia są albo dotknięte zamknięciem serwera, albo całkowicie niedostępne.


Jeśli chodzi o indywidualne narzędzia do wydawania pieniędzy, wszystko działa normalnie, oczywiście pod warunkiem posiadania własnego Dojo. Normalne transakcje Stonewall (a nie Stonewall x2) działają bez problemu.


W komentarzach na Twitterze podkreślono, że prywatność oferowana przez transakcję Stonewall może teraz zostać ograniczona. Wartość dodana transakcji Stonewall polega na tym, że jest ona nie do odróżnienia od transakcji Stonewall x2 pod względem struktury. Kiedy analityk napotyka ten konkretny wzorzec, nie może określić, czy jest to standardowy Stonewall z jednym użytkownikiem, czy Stonewall x2 z udziałem dwóch użytkowników. Jak jednak zobaczymy w kolejnych akapitach, przeprowadzanie transakcji Stonewall x2 stało się bardziej złożone ze względu na niedostępność Sorobanu. Dlatego niektórzy uważają, że analityk może teraz założyć, że każda transakcja o tej strukturze jest normalnym Stonewall. Osobiście nie podzielam tego założenia. Chociaż transakcje Stonewall x2 mogą być rzadsze (i myślę, że były już przed tym incydentem), fakt, że nadal są możliwe, może unieważnić całą analizę opartą na założeniu, że tak nie jest.

**[-> Dowiedz się więcej o transakcjach Stonewall](https://planb.network/tutorials/privacy/On-Chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)**

Jeśli chodzi o Ricochet, nie byłem w stanie zweryfikować, czy usługa nadal działa, ponieważ nie posiadam Dojo na Testnet i wolę nie ryzykować wydania `100 000 Sats` na Wallet, który może być kontrolowany przez władze. Jeśli miałeś okazję przetestować to narzędzie w ostatnim czasie, zapraszam do kontaktu ze mną, abyśmy mogli zaktualizować ten artykuł.


Jeśli musisz użyć Ricochet, pamiętaj, że zawsze możesz wykonać tę operację ręcznie za pomocą dowolnego oprogramowania Wallet. Aby dowiedzieć się, jak ręcznie prawidłowo wykonać różne przeskoki, zalecam zapoznanie się z tym artykułem: [**RICOCHET**](https://planb.network/tutorials/privacy/On-Chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589)


Narzędzie JoinBot już nie działa, ponieważ było całkowicie zależne od udziału Wallet zarządzanego przez Samourai.


Jeśli chodzi o inne rodzaje transakcji opartych na współpracy, często określane jako "cahoots", pozostają one możliwe, ale tylko ręcznie. Przed wyłączeniem serwera istniały dwie opcje wykonywania transakcji Stonewall x2 lub Stowaway (PayJoin):



- Użyj sieci Soroban do automatycznego i zdalnego Exchange PSBT;
- Można też dokonać tych wymian ręcznie, skanując wiele kodów QR.


Po kilku testach okazało się, że Soroban już nie działa. Aby wykonać te transakcje współpracy, Exchange danych musi być zatem wykonany ręcznie. Oto dwie opcje wykonania tego Exchange:



- Jeśli jesteś fizycznie blisko swojego współpracownika, możesz kolejno skanować kody QR;
- Jeśli jesteś daleko od swojego współpracownika, możesz Exchange PSBT za pośrednictwem zewnętrznego kanału komunikacji z aplikacją. Należy jednak zachować ostrożność, ponieważ dane zawarte w tych PSBT są wrażliwe pod względem prywatności. Zalecam korzystanie z szyfrowanej usługi przesyłania wiadomości, aby zapewnić poufność Exchange.


**[-> Dowiedz się więcej o transakcjach Stonewall x2.](https://planb.network/tutorials/privacy/On-Chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)**


**[-> Dowiedz się więcej o transakcjach Stowaway](https://planb.network/tutorials/privacy/On-Chain/PayJoin-samourai-Wallet-48a5c711-ee3d-44db-b812-c55913080eab)**


Jeśli chodzi o Whirlpool, protokół wydaje się już nie działać, nawet dla użytkowników, którzy mają własne Dojo. Monitorowałem moje RoninDojo przez ostatnie kilka dni i próbowałem kilku podstawowych manipulacji, ale Whirlpool CLI nie był w stanie się połączyć od czasu wyłączenia serwera.


Pozostaję jednak w nadziei, że protokół ten może zostać reaktywowany lub być może inaczej wyobrażony w nadchodzących tygodniach, w zależności od rozwoju sytuacji. Ta przerwa może być okazją do zbadania nowych podejść lub potencjalnych ulepszeń tego systemu.


### Jakie narzędzia zewnętrzne są jeszcze dostępne?


Jeśli chodzi o inne narzędzia związane ze środowiskiem Samourai, niektóre są nadal dostępne, a inne nie.


Bezpłatna strona internetowa z analizą łańcucha OXT.me nie jest już niestety dostępna.


Narzędzie Whirlpool Stats Tool nie jest już dostępne do pobrania, ponieważ było hostowane na GitLab Samourai. Nawet jeśli wcześniej pobrałeś to narzędzie Pythona lokalnie na swój komputer lub jeśli było ono zainstalowane na twoim węźle RoninDojo, WST nie będzie na razie działać. W rzeczywistości jego działanie zależało od danych dostarczonych przez OXT.me, a strona ta nie jest już dostępna. Obecnie WST nie jest szczególnie przydatny, ponieważ protokół Whirlpool jest nieaktywny.


Strona KYCP.org jest obecnie niedostępna.


GitLab, który hostował kod narzędzia Boltzmann Calculator Python, również został przejęty. W tej chwili nie jest już możliwe pobranie tego narzędzia. Jeśli jednak posiadasz RoninDojo, możesz nadal korzystać z Boltzmann Calculator w taki sam sposób jak wcześniej.


Jeśli chodzi o RoninDojo, to oprogramowanie node-in-box nadal działa poprawnie pomimo niedostępności niektórych konkretnych narzędzi, takich jak Whirlpool, CLI i WST. Dzięki Fulcrum lub Electrs można go nadal używać z innym oprogramowaniem Wallet. Jeśli chcesz uzyskać więcej informacji na temat RoninDojo lub masz konkretne pytania, zachęcam do dołączenia do [ich grupy Telegram](https://t.me/RoninDojoNode).


Jednak kod źródłowy RoninDojo nie jest już obecnie dostępny, ponieważ był hostowany na GitLab Samourai. W związku z tym nie jest obecnie możliwe ręczne zainstalowanie go na Raspberry Pi.


Jeśli chodzi o oprogramowanie Watch-only wallet Sentinel, sytuacja jest podobna do tej z aplikacją Samourai. Jeśli posiadasz własne Dojo, możesz nadal korzystać z Sentinel bez żadnych problemów. Jeśli jednak nie posiadasz Dojo, nie będziesz w stanie nawiązać połączenia. W przeciwieństwie do Samourai, strona Sentinel jest nadal dostępna online. Należy jednak zachować ostrożność w przypadku tej strony i oferowanego tam APK, ponieważ nie jest jasne, kto obecnie kontroluje te zasoby.


### Czy ma to wpływ na Sparrow Wallet?


Sparrow Wallet nadal działa normalnie, z wyjątkiem narzędzi Samourai, które nie są już dostępne. Obecnie nie jest już możliwe wykonywanie coinjoinów za pośrednictwem Sparrow. Podobnie, narzędzia do wspólnego wydawania nie są już dostępne, ponieważ Sparrow nie oferuje opcji ręcznego Exchange PSBT, w przeciwieństwie do Samourai. W przypadku wszystkich innych funkcji, Sparrow działa bez zarzutu. W razie potrzeby można również użyć tego oprogramowania do odzyskania Wallet Samourai.


## Jak odzyskać Samourai Wallet?


Jak widzieliśmy w poprzednich sekcjach, jeśli posiadasz własne Dojo, niekoniecznie musisz zmieniać oprogramowanie. **Samourai pozostaje doskonałym wyborem Hot Wallet** do codziennych wydatków. Jeśli jednak nie posiadasz Dojo lub wolisz wybrać inne oprogramowanie, wyjaśnię cały proces odzyskiwania, szczegółowo opisując wszelkie potencjalne przeszkody, które możesz napotkać.


W każdym razie ważne jest, aby nie spieszyć się i nie popełniać błędów. Pamiętaj, że nie ma pośpiechu, ponieważ posiadasz klucze prywatne, a zajęcie serwerów Samourai w żaden sposób na to nie wpływa. Cokolwiek się stanie, oczywiście nie mogą uzyskać dostępu do twoich kluczy prywatnych.


### Weryfikacja passphrase


Aby odzyskać Wallet, musisz mieć passphrase, nawet jeśli zdecydujesz się na odzyskanie za pomocą pliku kopii zapasowej. Zacznij od zweryfikowania ważności passphrase. Otwórz aplikację Samourai Wallet, kliknij ikonę Paynym w lewym górnym rogu, a następnie wybierz `Ustawienia`.


![samourai](assets/1.webp)


Następnie kliknij `Troubleshooting`, a następnie `passphrase/backup test`.


![samourai](assets/2.webp)


Wprowadź swój passphrase i kliknij `Ok`. Jeśli dane są poprawne, Samurai je potwierdzi. Masz również możliwość zweryfikowania pliku kopii zapasowej, jeśli planujesz użyć go później.


![samourai](assets/3.webp)


Ten krok jest opcjonalny, ale zalecany. Potwierdza on, że passphrase jest prawidłowy, eliminując potencjalne źródło późniejszych problemów. Jeśli Samourai wskaże, że passphrase jest nieprawidłowy na tym etapie, odzyskanie danych nie będzie możliwe. Upewnij się, że wprowadziłeś passphrase poprawnie i sprawdź go ponownie.


### Opcja 1: Odzyskaj Wallet na Sparrow z pliku kopii zapasowej


Od wersji 1.8.6 Sparrow Wallet możliwe jest bezpośrednie zaimportowanie Wallet Samourai przy użyciu zapasowego pliku tekstowego o nazwie `samourai.txt`, który aplikacja generuje automatycznie. Plik ten zawiera wszystkie informacje niezbędne do odzyskania Wallet i jest zaszyfrowany wraz z passphrase w celu zapewnienia bezpieczeństwa.


Jeśli wybierzesz tę opcję, będziesz potrzebował aktualnego pliku `samourai.txt` i passphrase. Aby generate ten plik na Samourai Wallet, kliknij na trzy małe kropki w prawym górnym rogu, a następnie wybierz `Export Wallet backup`.


![samourai](assets/4.webp)

Następnie wybierz `Export to Clipboard`. Następnie należy bezpiecznie przesłać plik na komputer. Ponieważ plik jest zaszyfrowany, ale sam passphrase jest wystarczający do jego odszyfrowania, ważne jest, aby podjąć środki ostrożności podczas jego przesyłania. Jeśli zdecydujesz się na bezpośredni transfer jako zwykły tekst, będziesz musiał utworzyć plik `samourai.txt` na swoim komputerze i wkleić do niego zawartość schowka. Alternatywą jest bezpośrednie pobranie pliku `samourai.txt` z plików zapisanych w telefonie.

Po uzyskaniu dostępu do pliku na komputerze, otwórz Sparrow Wallet, kliknij zakładkę `File` i wybierz `Import Wallet`, aby rozpocząć importowanie Wallet.


![samourai](assets/5.webp)


Przewiń w dół do `Samourai Backup`, kliknij `Import File`, a następnie wybierz plik `samourai.txt`.


![samourai](assets/6.webp)


Następnie Sparrow poprosi o hasło do odszyfrowania pliku. Hasło to jest w rzeczywistości passphrase. Wprowadź je w odpowiednim polu i kliknij `Import`.


![samourai](assets/7.webp)


Jeśli na tym etapie Wallet nie pojawi się, możliwe, że popełniłeś błąd podczas kopiowania pliku `samourai.txt` lub podczas wprowadzania passphrase. Więcej informacji można znaleźć w sekcji rozwiązywania problemów.


![samourai](assets/8.webp)


Jeśli chodzi o typ skryptu, jeśli nie skonfigurowałeś innych skryptów w Samourai, powinieneś normalnie używać tylko SegWit V0 (Native SegWit / P2WPKH). Zachowaj ten domyślny skrypt i kliknij `Import`.


![samourai](assets/9.webp)


Nazwij swój Wallet, na przykład "Samourai Recovery", a następnie kliknij `Create Wallet`.


![samourai](assets/10.webp)


Sparrow poprosi o wybranie hasła. To hasło chroni tylko dostęp do Wallet na tym komputerze i nie dotyczy wyprowadzania kluczy Wallet. Upewnij się, że wybrałeś silne hasło, zanotuj je, aby je zapamiętać i kliknij `Set Password`.


![samourai](assets/11.webp)


Następnie Sparrow pobierze klucze Wallet i wyszuka odpowiednie transakcje.


![samourai](assets/12.webp)


Na razie dostępne jest tylko konto depozytowe. Jeśli korzystałeś z Samourai tylko dla tego konta, powinieneś zobaczyć wszystkie swoje środki. Jeśli jednak korzystałeś również z Whirlpool, będziesz musiał wyprowadzić konta `premix`, `postmix` i `badbank`. W aplikacji Sparrow wystarczy kliknąć zakładkę `Ustawienia`, a następnie `Dodaj konta...`.


![samourai](assets/13.webp)

W otwartym oknie wybierz `Whirlpool Accounts` z rozwijanego menu, a następnie kliknij `OK`.

![samourai](assets/14.webp)


Następnie pojawią się różne konta Whirlpool, a Sparrow uzyska niezbędne klucze do korzystania z powiązanych bitcoinów.


![samourai](assets/15.webp)


Jeśli używasz innego oprogramowania niż Sparrow, takiego jak Electrum, do odzyskania Samourai Wallet, oto indeksy kont Whirlpool do ręcznego odzyskiwania:



- Depozyt: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`


Masz teraz dostęp do swoich bitcoinów na Sparrow. Jeśli potrzebujesz pomocy w korzystaniu ze Sparrow Wallet, możesz również zapoznać się z [naszym dedykowanym samouczkiem] (https://planb.network/tutorials/Wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).


Zalecam również ręczne zaimportowanie etykiet powiązanych z UTXO na Samourai. Umożliwi to późniejszą skuteczną kontrolę monet na Sparrow.


### Opcja 2: Odzyskaj Wallet na Sparrow za pomocą frazy Mnemonic


Jeśli nie chcesz wykonywać odzyskiwania za pomocą pliku kopii zapasowej, możesz wybrać bardziej tradycyjną metodę, po prostu używając 12-słowowej frazy odzyskiwania i passphrase. Ta druga opcja jest często prostsza.


Aby rozpocząć, upewnij się, że masz pod ręką frazę odzyskiwania i passphrase. Następnie otwórz oprogramowanie Sparrow Wallet, kliknij zakładkę `File` i wybierz `Import Wallet`, aby rozpocząć importowanie Wallet.


![samourai](assets/16.webp)


Wybierz `Mnemonic Words (BIP39)` i w rozwijanym menu kliknij `Use 12 Words`.


![samourai](assets/17.webp)


Wprowadź 12 słów frazy odzyskiwania w odpowiedniej kolejności.


![samourai](assets/18.webp)


Jeśli Sparrow wyświetli komunikat "Nieprawidłowa suma kontrolna", oznacza to, że suma kontrolna frazy odzyskiwania jest nieprawidłowa, co prawdopodobnie oznacza, że popełniłeś błąd podczas wprowadzania słów.


![samourai](assets/19.webp)


Jeśli fraza jest poprawna, zaznacz pole `Użyj passphrase` i wprowadź passphrase w dedykowanym polu. Na koniec, jeśli wszystko wydaje się poprawne, kliknij przycisk `Odkryj Wallet`.


![samourai](assets/20.webp)


Nazwij swój Wallet, na przykład "Samourai Recovery", a następnie kliknij `Create Wallet`.


![samourai](assets/21.webp)

Sparrow poprosi o wybranie hasła. Hasło to chroni jedynie dostęp do Wallet na tym komputerze i nie jest związane z uzyskiwaniem kluczy Wallet. Upewnij się, że wybrałeś silne hasło, zapisz je, aby je zapamiętać i kliknij `Set Password`.

![samourai](assets/22.webp)


Następnie Sparrow wyprowadzi klucze dla Wallet i wyszuka odpowiednie transakcje.


![samourai](assets/23.webp)


Jeśli na tym etapie Wallet nie pojawi się, możliwe, że popełniłeś błąd podczas wprowadzania passphrase lub frazy odzyskiwania. Więcej informacji można znaleźć w dedykowanej sekcji rozwiązywania problemów.


Na razie dostępne jest tylko konto depozytowe. Jeśli korzystałeś z Samourai tylko dla tego konta, powinieneś zobaczyć wszystkie swoje środki. Jeśli jednak korzystałeś również z Whirlpool, będziesz musiał wyprowadzić konta `premix`, `postmix` i `badbank`. W aplikacji Sparrow wystarczy kliknąć zakładkę "Ustawienia", a następnie "Dodaj konta".


![samourai](assets/24.webp)


W otwartym oknie wybierz `Whirlpool Accounts` z rozwijanej listy, a następnie kliknij `OK`.


![samourai](assets/25.webp)


Następnie pojawią się różne konta Whirlpool, a Sparrow uzyska niezbędne klucze do korzystania z powiązanych bitcoinów.


![samourai](assets/26.webp)


Jeśli używasz innego oprogramowania, takiego jak Electrum, aby odzyskać Samourai Wallet, oto indeksy kont Whirlpool do ręcznego odzyskiwania:



- Depozyt: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`


Masz teraz dostęp do swoich bitcoinów na Sparrow. Jeśli potrzebujesz pomocy w korzystaniu ze Sparrow Wallet, możesz również zapoznać się z [naszym dedykowanym samouczkiem] (https://planb.network/tutorials/Wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).


Zalecam również ręczne zaimportowanie etykiet powiązanych z UTXO na Samourai. Umożliwi to późniejszą skuteczną kontrolę monet na Sparrow.


### Jakie są najczęściej napotykane problemy?


Po udzieleniu pomocy kilku osobom w ciągu ostatnich kilku dni, uważam, że napotkałem większość problemów, które mogą uniemożliwić odzyskanie Wallet. Jeśli nadal nie możesz uzyskać dostępu do Wallet pomimo poprzednich samouczków, oto kilka dodatkowych zaleceń.

Przede wszystkim, aby odzyskiwanie działało, absolutnie konieczne jest, aby fraza odzyskiwania była poprawna. Jeśli nie możesz znaleźć 12-wyrazowej frazy, możesz użyć _opcji 1_, aby odzyskać dane z pliku kopii zapasowej Samourai. Możesz również uzyskać dostęp do frazy odzyskiwania bezpośrednio w Samourai Wallet, przechodząc do `Ustawień`, następnie `Wallet`, a na koniec wybierając `Pokaż 12-słowną frazę odzyskiwania`.


Następnie błąd literowy w passphrase podczas odzyskiwania spowoduje nieprawidłowe klucze pochodne, co uniemożliwi odzyskanie Wallet na Sparrow. **passphrase musi być idealnie dokładny!


Aby rozwiązać ten problem, radzę najpierw sprawdzić ważność passphrase w aplikacji Samourai, jak opisano w sekcji "_Weryfikuj hasło_" tego artykułu:


1. **Weryfikacja w Samourai:** Jeśli Samourai potwierdzi, że passphrase jest poprawny, spróbuj ponownie odzyskać dane od początku, upewniając się, że dokładnie wprowadziłeś passphrase w Sparrow bez błędów;

2. **Błąd passphrase:** Jeśli Samourai wskaże, że passphrase jest nieprawidłowy, nie ma sensu kontynuować prób na Sparrow. Dopóki prawidłowy passphrase nie zostanie znaleziony, odzyskanie Wallet jest niemożliwe. Jeśli trwale utraciłeś passphrase, zachowaj swoją aplikację Samourai w bezpiecznym miejscu. Wszystko, co możesz zrobić, to mieć nadzieję, że serwery zostaną ponownie uruchomione, abyś mógł dokonywać wydatków bezpośrednio z aplikacji bez konieczności odzyskiwania. **Nie próbuj łączyć się z Dojo w tym przypadku**, ponieważ oznaczałoby to zresetowanie Wallet na Samourai, co wymaga dostępu do passphrase.


Wśród innych napotkanych błędów, wiele jest związanych z konfiguracją sieci w Sparrow.


Po pierwsze, upewnij się, że Sparrow jest poprawnie skonfigurowany w trybie `Mainnet`, a nie w trybie `Testnet`. Rzeczywiście, jeśli Sparrow wyszuka transakcje na Testnet, nic nie znajdzie, ponieważ Wallet znajduje się na Mainnet. Testnet jest alternatywną wersją Bitcoin, używaną wyłącznie do testowania i rozwoju, i działa w oddzielnej sieci od sieci głównej (Mainnet), z własnymi blokami i transakcjami. Aby sprawdzić, w której sieci się znajdujesz, kliknij zakładkę `Tools`, a następnie `Restart In`. Jeśli wyświetlana jest opcja `Mainnet`, oznacza to, że nie jesteś w sieci głównej. Wybierz ją, aby ponownie uruchomić Sparrow na Mainnet, a następnie rozpocznij proces odzyskiwania od nowa.


![samourai](assets/27.webp)

Niektórzy napotkali również trudności z podłączeniem Sparrow do swojego węzła. W prawym dolnym rogu aplikacji Sparrow kolorowy przełącznik wskazuje, czy oprogramowanie jest prawidłowo podłączone do węzła Bitcoin. Aby odzyskać transakcje Samourai, ważne jest, aby oprogramowanie było dobrze podłączone. Sprawdź, czy przełącznik jest aktywny, jak na poniższym obrazku (żółty dla węzła publicznego, Green dla Bitcoin Core i niebieski dla serwera Electrum).

![samourai](assets/28.webp)


Jeśli przełącznik nie jest aktywny, kliknij go, aby ponownie aktywować połączenie.


![samourai](assets/29.webp)


Jeśli problem nie ustąpi, oto kilka możliwych rozwiązań:



- Jeśli próbujesz połączyć się z własnym serwerem Electrum (niebieski) lub Bitcoin Core (Green), a Sparrow nie może się połączyć, sprawdź informacje o połączeniu w `File > Preferences. > Serwer`;


![samourai](assets/30.webp)



- Jeśli problem z połączeniem nadal występuje, może to być spowodowane niepełną synchronizacją węzła. Upewnij się, że węzeł i indeksator są w 100% zsynchronizowane. Jeśli to konieczne, w ostateczności odłącz swój węzeł od Sparrow i połącz się z węzłem publicznym;
- Jeśli połączenie z węzłem publicznym nie powiodło się, spróbuj zmienić węzeł, wybierając inny z listy rozwijanej.


![samourai](assets/31.webp)


Jeśli udało ci się odzyskać Wallet, ale wydaje się on niekompletny, może to oznaczać problem związany z derywacją.


Problem może wystąpić, jeśli używałeś konta depozytowego Samourai z innym typem skryptu niż `P2WPKH`. Domyślnie Samourai używa tego typu skryptu, ale jeśli zmieniłeś go ręcznie, musisz go również dostosować podczas odzyskiwania w Sparrow.


Aby wyprowadzić gałęzie dla innych typów skryptów, należy powtórzyć proces odzyskiwania dla każdego używanego typu skryptu. W tym celu przejdź do `File > New Wallet` w Sparrow, wybierz inny typ skryptu z listy rozwijanej, kliknij `New or Imported Software Wallet` i wykonaj te same kroki, co w początkowym samouczku.


![samourai](assets/32.webp)


Kolejny napotkany problem związany jest z wartością Gap Limit. Wartość ta mówi Sparrow po ilu pustych adresach powinien przestać wyprowadzać nowe adresy. Jeśli po odzyskaniu danych zauważysz, że brakuje niektórych transakcji, może to być spowodowane zbyt niską wartością Gap Limit. Aby rozwiązać ten problem, przejdź do konta, które powoduje problem, na przykład konta postmix (jeśli dotyczy to kilku kont, powtórz tę operację dla każdego z nich).


![samourai](assets/33.webp)


Kliknij zakładkę `Ustawienia`, a następnie przycisk `Zaawansowane...`.

![samourai](assets/34.webp)

Stopniowo zwiększaj wartość Gap Limit, na przykład ustawiłem ją tutaj na `400`. Następnie kliknij przycisk "Zamknij".


![samourai](assets/35.webp)


Kliknij "Zastosuj", aby zakończyć. Następnie Sparrow pobierze większą liczbę adresów i wyszuka na nich środki, co powinno pomóc w odzyskaniu wszystkich transakcji.


![samourai](assets/36.webp)


Na tym kończą się różne problemy z odzyskiwaniem, które napotkałem w ciągu ostatnich kilku dni. Jeśli po wypróbowaniu wszystkich tych rozwiązań nadal masz problemy, zapraszam do dołączenia do [Discover Bitcoin Discord](https://discord.gg/xKKm29XGBb), aby poprosić o pomoc. Regularnie odwiedzam ten Discord i z przyjemnością pomogę, jeśli znajdę rozwiązanie. Inni bitcoinerzy również będą mogli podzielić się swoimi doświadczeniami i zaoferować pomoc. **W każdym przypadku ważne jest, aby zachować poufność frazy odzyskiwania, pliku kopii zapasowej i passphrase**. Nie udostępniaj ich nikomu, ponieważ może to umożliwić kradzież twoich bitcoinów.


Po zakończeniu odzyskiwania masz teraz dostęp do swoich bitcoinów. To dobra rzecz, ale może nie wystarczyć. Zajęcie serwerów wiąże się bowiem z nowymi potencjalnymi zagrożeniami dla prywatności użytkowników. W poniższej sekcji szczegółowo przeanalizujemy te zagrożenia i przedstawimy środki ostrożności, które należy podjąć, aby chronić swoją prywatność.


## Jakie są konsekwencje dla prywatności transakcji?


### Jako użytkownik Samourai bez Dojo


Jeśli korzystałeś z Samourai Wallet bez podłączenia własnego Dojo, twoje xpuby musiały zostać przesłane na serwery Samourai, aby aplikacja działała. Po przejęciu tych serwerów możliwe jest, że władze mają teraz dostęp do tych xpubów.


Ten scenariusz pozostaje hipotetyczny. Nie wiemy, czy te xpuby zostały nagrane, czy jakiekolwiek potencjalne przechowywanie zostało zniszczone, czy władze je odzyskały i czy planują wykorzystać je do analizy łańcucha. Jednak w takiej sytuacji rozsądnie jest rozważyć najgorszy scenariusz, w którym władze mają xpuby użytkowników, którzy nie podłączyli własnego Dojo.

Dla porównania, xpub to ciąg znaków, który zawiera wszystkie niezbędne Elements do wygenerowania kluczy publicznych dziecka (klucz publiczny + kod łańcucha). Jest on używany w hierarchicznych deterministycznych portfelach do generate odbierania adresów i obserwowania transakcji na koncie bez ujawniania powiązanych kluczy prywatnych. Pozwala to na przykład na utworzenie Wallet "tylko do obserwacji". Ujawnienie xpubs może jednak zagrozić prywatności użytkownika, ponieważ pozwala stronom trzecim śledzić transakcje i zobaczyć salda powiązanych kont.

Każdy, kto zna twoje xpubs, może w ten sposób zobaczyć wszystkie adresy odbiorcze twojego Wallet, te używane w przeszłości i te, które zostaną wygenerowane w przyszłości.


Dla użytkowników bez Dojo, potencjalny wyciek xpubów ma dwie główne konsekwencje:



- Coinjoiny, które mogłeś wykonać, stają się nieskuteczne z punktu widzenia prywatności dla każdego, kto zna twoje xpubs, przez co twoje monety tracą cały anonset;
- Osoba ta może również śledzić wszystkie adresy odbiorcze Samourai Wallet.


Dlatego ważne jest, aby rozważyć najgorszy scenariusz i rozstać się z tym Wallet, potencjalnie zagrożonym pod względem prywatności. Aby to zrobić, utwórz nowy Wallet od podstaw za pomocą innego oprogramowania, takiego jak Sparrow Wallet. Po zweryfikowaniu ważności kopii zapasowych, przenieś wszystkie swoje środki, dokonując transakcji. Chociaż operacja ta nie zrywa powiązania identyfikowalności monet, uniemożliwi władzom poznanie z całą pewnością adresów nowych Wallet.


Podczas tej operacji transferu zalecam unikanie konsolidacji monet. Jeśli założymy, że twoje xpuby są zagrożone, konsolidacja nie będzie miała żadnego wpływu z punktu widzenia osoby mającej dostęp do tych xpubów, ponieważ twoja prywatność jest już z nimi zagrożona. Radzę jednak nie konsolidować zbytnio swoich monet, głównie w celu ochrony prywatności przed innymi osobami. W najgorszym przypadku tylko władze mogą mieć dostęp do twoich xpubów, ale reszta świata o nich nie wie. Tak więc, z punktu widzenia innych osób, konsolidacja monet może znacznie zaszkodzić twojej prywatności ze względu na heurystykę Common Input Ownership (CIOH).


**Uwaga:** aby definitywnie przerwać śledzenie, można również rozważyć wykonanie coinjoinów z tego nowego Wallet.

**Ostrzeżenie:** Samo odzyskanie Samourai Wallet na Sparrow Wallet nie wystarczy. Konieczne jest utworzenie całkowicie nowego Wallet z nową frazą odzyskiwania, jeśli chcesz uniknąć używania xpubów, które mogły wyciec. Jeśli importujesz istniejący seed do Sparrow, zmieniasz tylko oprogramowanie zarządzające Wallet, ale Wallet pozostaje ten sam.


### Jako użytkownik Sparrow lub Samourai z Dojo


Jeśli twój Wallet jest zarządzany tylko przez Sparrow Wallet, twoje xpuby nie mogły wyciec, niezależnie od tego, czy używasz węzła publicznego, czy własnego węzła Bitcoin. Podobnie, jeśli korzystasz z aplikacji Samourai i zawsze łączyłeś tę aplikację z własnym Dojo od czasu utworzenia Wallet, twoje xpuby są również bezpieczne.


Jeśli jednak korzystałeś z tego samego Wallet w okresie **bez własnego Dojo**, a następnie z własnym Dojo, możliwe jest, że serwery Samourai mogły mieć dostęp do twoich xpubów, a zatem władze mogły je znać. Jeśli jesteś w tej konkretnej sytuacji, radzę postępować zgodnie z zaleceniami z poprzedniej sekcji i uznać swoje xpuby za zagrożone.


Dla tych, którzy zawsze używali Sparrow lub Samourai z własnym Dojo, głównym ryzykiem jest to, że anonsety monet mogą zostać potencjalnie zmniejszone. Załóżmy, w najgorszym przypadku, że wszyscy użytkownicy bez Dojo mają swoje xpuby w rękach władz, wtedy ścieżka ich monet przez cykle CoinJoin może być śledzona przez te władze.


Aby to zilustrować, weźmy konkretny przykład. Wyobraź sobie, że uczestniczyłeś w pierwszym cyklu CoinJoin, po którym nastąpiły dwa dodatkowe cykle CoinJoin. Jeśli xpubs użytkowników bez Dojo nie wyciekły, to potencjalny anonset twojej monety wyniósłby 13.


![samourai](assets/37.webp)


Jeśli jednak weźmiemy pod uwagę, że xpuby wyciekły i że napotkałeś użytkownika bez dojo podczas początkowego CoinJoin, a następnie 2 podczas pierwszego CoinJoin, to twój potencjalny anonset wynosiłby tylko 10 zamiast 13 z punktu widzenia władz.


![samourai](assets/38.webp)

Ten potencjalny spadek anonsetu jest trudny do oszacowania, ponieważ zależy od wielu czynników, a każda moneta ma na niego inny wpływ. Na przykład użytkownik bez Dojo napotkany we wczesnych cyklach wpływa na potencjalny anonset znacznie bardziej niż użytkownik napotkany w późniejszych cyklach. Aby dać ci wyobrażenie o sytuacji, która pozostaje hipotetyczna, najnowsze statystyki dostarczone przez Samourai wskazują, że od 85% do 90% monet zaangażowanych w coinjoiny pochodziło od użytkowników z Dojo, Sparrow lub Bitcoin Keeper, czyli użytkowników, którzy nawet w najgorszym przypadku nie widzieliby wycieku swoich xpubów.

Chociaż dane te są trudne do zweryfikowania, wydają mi się spójne z dwóch powodów:



- Sparrow Wallet jest szeroko stosowany;
- Większość oprogramowania typu node-in-box oferuje implementacje Dojo, a te główne programy, takie jak Umbrel, są obecnie bardzo popularne.


W związku z tym należy wziąć pod uwagę kilka aspektów. Jeśli prywatność twoich monet w stosunku do władz jest dla ciebie niezwykle ważna, rozsądnie byłoby przygotować się na najgorszy scenariusz i trudno jest zagwarantować w 100%, że twoje cykle Whirlpool CoinJoin nie mogą być śledzone z powodu potencjalnego wycieku xpubów od użytkowników bez Dojo. Chociaż takie założenie jest bardzo mało prawdopodobne, nie jest niemożliwe.


Z drugiej strony, jeśli prywatność twoich monet w stosunku do organu potencjalnie będącego w posiadaniu tych xpubów nie jest dla ciebie kluczowa, wówczas sytuację można rozpatrywać inaczej.


Określam "wobec organu", ponieważ ważne jest, aby pamiętać, że tylko organ, który przejął serwery, jest potencjalnie świadomy tych xpubów. Jeśli celem korzystania z CoinJoin było uniemożliwienie piekarzowi śledzenia funduszy, to nie jest on lepiej poinformowany niż przed zajęciem serwera.


Wreszcie, ważne jest, aby wziąć pod uwagę początkowy anonset monety, przed zajęciem serwera. Weźmy przykład monety, która osiągnęła potencjalny anonset w wysokości 40 000; potencjalny spadek tego anonsetu jest prawdopodobnie znikomy. Rzeczywiście, przy już bardzo wysokim bazowym anonsecie, jest mało prawdopodobne, aby obecność kilku użytkowników bez Dojo mogła radykalnie zmienić sytuację. Jeśli jednak twoja moneta miała anonset 40, to potencjalny wyciek może poważnie wpłynąć na anonsety i potencjalnie umożliwić śledzenie.

Ponieważ narzędzie WST nie działa już po zamknięciu OXT.me, można jedynie oszacować te anonsety. W przypadku anonsetu retrospektywnego nie ma się zbytnio czym martwić, ponieważ model Whirlpool zapewnia, że jest on bardzo wysoki od pierwszego CoinJoin, dzięki dziedzictwu twoich rówieśników. Jedynym przypadkiem, w którym może to stanowić problem, jest sytuacja, w której moneta nie była remiksowana przez kilka lat i była mieszana na początku uruchomienia puli. Jeśli chodzi o potencjalny anonset, możesz sprawdzić, jak długo twoja moneta była dostępna dla coinjoinów. Jeśli minęło kilka miesięcy, to prawdopodobnie ma bardzo wysoki potencjalny anonset. Z drugiej strony, jeśli moneta została dodana do puli zaledwie kilka godzin przed zajęciem serwerów, to jej potencjalny anonset jest prawdopodobnie bardzo niski.

[**-> Dowiedz się więcej o anonsetach i metodzie ich obliczania**](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


Innym aspektem, który należy wziąć pod uwagę, jest wpływ konsolidacji na anonsety monet, które zostały zmieszane. Biorąc pod uwagę, że konta Whirlpool nie są już dostępne za pośrednictwem aplikacji Samourai, jest prawdopodobne, że wielu użytkowników przeniosło swoje Wallet do innego oprogramowania i próbowało wypłacić swoje środki z Whirlpool. W szczególności w ostatni weekend, kiedy opłaty transakcyjne w sieci Bitcoin były stosunkowo wysokie, istniała silna techniczna i ekonomiczna zachęta do konsolidacji monet post-mix. Oznacza to, że prawdopodobnie wielu użytkowników dokonało znaczących konsolidacji.


Problem z tymi konsolidacjami post-mix polega na tym, że zawsze zmniejszają one anonsety, nie tylko dla użytkownika, który je wykonuje, ale także dla użytkowników, z którymi zetknęli się podczas swoich cykli CoinJoin. Chociaż nie byłem w stanie dokładnie zweryfikować ani skwantyfikować tego zjawiska, zachęty ekonomiczne związane z opłatami transakcyjnymi w tym czasie mogą prowadzić do założenia, że anonsety są potencjalnie niższe.


### Jako użytkownik Sentinel


Działanie sieciowe aplikacji Watch-only wallet Sentinel jest podobne do działania aplikacji Samourai. Aby uzyskać dostęp do informacji Wallet, aplikacja musi przesłać xpubs, klucze publiczne i adresy dostarczone do Dojo. Jeśli zawsze korzystałeś z własnego Dojo na Sentinelu, nie ma problemu i możesz kontynuować korzystanie z aplikacji bez obaw. Jeśli jednak byłeś zależny od serwerów Samourai dla swojego Sentinela, możliwe jest, że twoje xpuby zostały ujawnione. W takim przypadku zaleca się wykonanie tego samego procesu zmiany Wallet zalecanego dla Samourai Wallet po podłączeniu do serwerów Samourai.


W mało prawdopodobnym przypadku, gdybyś używał Dojo z Samourai, ale nie z Sentinelem, rozsądniej byłoby uznać, że twoje xpuby są zagrożone.


## Wnioski


Dziękuję za przeczytanie tego artykułu do końca. Jeśli uważasz, że brakuje jakichś informacji lub masz sugestie, skontaktuj się ze mną, aby podzielić się swoimi przemyśleniami. Ponadto, jeśli potrzebujesz dalszej pomocy w odzyskaniu Samourai Wallet pomimo tego samouczka, zapraszam do dołączenia do [Discover Bitcoin Discord](https://discord.gg/xKKm29XGBb), aby poprosić o pomoc. Regularnie odwiedzam ten Discord i z przyjemnością pomogę, jeśli znajdę rozwiązanie. Inni bitcoinerzy również będą mogli podzielić się swoimi doświadczeniami i zaoferować wsparcie. **W każdym przypadku ważne jest, aby zachować poufność frazy odzyskiwania, pliku kopii zapasowej i passphrase**. Nie udostępniaj ich nikomu, ponieważ może to umożliwić kradzież twoich bitcoinów.