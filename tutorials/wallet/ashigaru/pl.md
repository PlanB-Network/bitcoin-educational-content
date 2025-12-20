---
name: Ashigaru
description: fork od Samourai Wallet do zabezpieczania, zarządzania i mieszania bitcoinów
---

![cover](assets/cover.webp)



Ashigaru to aplikacja mobilna Bitcoin wallet, która jest kontynuacją projektu Samourai Wallet, ale w nowej formie. Oprogramowanie to narodziło się w szczególnym kontekście: w kwietniu 2024 r. założyciele Samourai Wallet zostali aresztowani przez amerykańskie władze, a ich serwery zostały przejęte. Chociaż sama aplikacja Samurai pozostała użyteczna, obecnie nie jest już utrzymywana. Ashigaru to darmowa wersja fork Samurai Wallet, utrzymywana przez anonimowy zespół w celu zagwarantowania ciągłości funkcjonalności Samurai i ochrony jego oryginalnej filozofii: obrony prywatności i suwerenności użytkowników Bitcoin.



Ashigaru czerpie wiele z DNA Samourai: podobny interfejs, ewidentnie samokontrolujące się podejście, otwarte oprogramowanie i skupienie się na prywatności. Kod jest rozpowszechniany na licencji GNU GPLv3, która zapewnia każdemu możliwość audytu, modyfikacji lub redystrybucji oprogramowania.



Aplikacja Ashigaru integruje zestaw zaawansowanych narzędzi do zachowania poufności i zarządzania UTXO:




- Whirlpool**, protokół coinjoin oparty na Zerolink, umożliwiający zerwanie deterministycznych powiązań między wejściami i wyjściami transakcji, bez utraty suwerenności nad swoimi środkami.
- PayNym**, który implementuje kody płatności wielokrotnego użytku (BIP47), teraz reprezentowane przez system awatarów "*Pepehash*".
- Ricochet**, funkcja, która dodaje pośrednie skoki do transakcji, aby utrudnić ich śledzenie.
- I oczywiście ***Coin Control*** do precyzyjnego wybierania, zamrażania i oznaczania UTXO.
- Batch Spending***, aby obniżyć koszty poprzez zgrupowanie kilku płatności w jedną transakcję.
- Tryb **Stealth**, który ukrywa aplikację na telefonie komórkowym za fałszywym programem uruchamiającym, aby pozostać niezauważonym podczas fizycznej inspekcji telefonu.
- Zaawansowane narzędzia do optymalizacji wydatków (payjoin, stonewall...).
- Zoptymalizowany system odzyskiwania danych przy użyciu hasła BIP39.
- System automatycznej optymalizacji wyboru opłat transakcyjnych.



![Image](assets/fr/01.webp)



Ashigaru jest zatem skierowany do użytkowników, którzy są świadomi kwestii związanych z identyfikowalnością transakcji na Bitcoin. Niezależnie od tego, czy jesteś użytkownikiem dbającym o prywatność, doświadczonym bitcoinerem zaangażowanym w samokontrolę, czy też osobą narażoną na ryzyko zwiększonego nadzoru, ta aplikacja wallet zapewnia narzędzia potrzebne do odzyskania kontroli nad swoją aktywnością na Bitcoin.



Ashigaru jest dostępny w wersji mobilnej za pośrednictwem aplikacji, którą omówimy w tym samouczku. Ale można go również używać na komputerze PC z ***Ashigaru Terminal***, który przedstawimy w przyszłym samouczku.



![Image](assets/fr/02.webp)



W tym poradniku chciałbym przedstawić podstawy korzystania z Ashigaru: instalację, połączenie z Dojo, tworzenie kopii zapasowych, odbieranie i wysyłanie bitcoinów. Zaawansowane narzędzia zostaną przedstawione w innych dedykowanych poradnikach.



## 1. Wymagania wstępne dla Ashigaru



Aplikacja wymaga kilku warunków wstępnych do prawidłowego działania. Przede wszystkim, nie jest to aplikacja dostępna w klasycznych sklepach, takich jak Google Play Store czy App Store. Instaluje się ręcznie na telefonie tylko z pliku `.apk`, który można pobrać za pośrednictwem sieci Tor. Jeśli więc korzystasz z iPhone'a, ta metoda nie zadziała: będziesz potrzebować urządzenia z Androidem.



Aby pobrać plik `.apk` przez sieć Tor, potrzebna jest przeglądarka umożliwiająca dostęp do stron `.onion`. Najprostszym sposobem jest zainstalowanie aplikacji Tor Browser na telefonie, dostępnej w [Google Play Store](https://play.google.com/store/apps/details?id=org.torproject.torbrowser) lub bezpośrednio [poprzez `.apk`](https://www.torproject.org/download/#android).



![Image](assets/fr/03.webp)



Większość najnowszych smartfonów domyślnie blokuje instalację aplikacji z nieznanych źródeł. Musisz tymczasowo aktywować tę opcję dla Tor Browser w ustawieniach urządzenia, aby umożliwić instalację. Po zainstalowaniu aplikacji należy pamiętać o wyłączeniu tej funkcji, aby wzmocnić bezpieczeństwo telefonu.



Kolejnym niezbędnym warunkiem korzystania z Ashigaru jest węzeł Bitcoin Dojo. Ze względów bezpieczeństwa i suwerenności zespół Ashigaru nie utrzymuje scentralizowanego serwera do łączenia aplikacji. Musisz więc uruchomić własną instancję Dojo lub połączyć się z zaufaną.



Dojo umożliwia aplikacji Ashigaru sprawdzanie informacji blockchain, przeglądanie sald adresów i transmitowanie transakcji w sieci Bitcoin.



Aby dowiedzieć się więcej o Dojo i dowiedzieć się, jak go zainstalować, zapraszam do śledzenia tego dedykowanego samouczka :



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Jeśli naprawdę nie możesz sobie pozwolić na uruchomienie własnego Dojo, możesz znaleźć ludzi chętnych do udostępnienia swojej instancji za darmo na [dojobay.pw](https://www.dojobay.pw/mainnet/). Może to być tymczasowe rozwiązanie, ale na dłuższą metę zalecam korzystanie z własnego Dojo, aby zagwarantować sobie suwerenność i poufność.



## 2. Sprawdź i zainstaluj aplikację Ashigaru



### 2.1. Pobierz aplikację Ashigaru



W telefonie otwórz przeglądarkę Tor Browser i przejdź do [oficjalnej strony Ashigaru](https://ashigaru.rs/download/), w sekcji `Download`. Następnie kliknij przycisk `Download for Android`, aby pobrać plik instalacyjny.



![Image](assets/fr/04.webp)



Przed zainstalowaniem aplikacji na urządzeniu sprawdzimy jej autentyczność i integralność. Jest to bardzo ważny krok, zwłaszcza w przypadku instalowania aplikacji bezpośrednio z pliku `.apk'.



### 2.2. Sprawdź aplikację Ashigaru



Wróć do [oficjalnej strony Ashigaru](https://ashigaru.rs/download/) w sekcji `Download`, a następnie skopiuj wiadomość wyświetlaną pod tytułem `SHA-256 Hash pliku APK`. Skopiuj cały blok, od `BEGIN PGP SIGNED MESSAGE` do `END PGP SIGNATURE`.



![Image](assets/fr/05.webp)



Nadal na telefonie, otwórz nową kartę w przeglądarce Tor i przejdź do [narzędzia weryfikacji Keybase](https://keybase.io/verify). Wklej skopiowaną wiadomość w odpowiednie pole, a następnie kliknij przycisk `Verify`.



![Image](assets/fr/06.webp)



Jeśli podpis jest prawdziwy, Keybase wyświetli komunikat potwierdzający, że plik został podpisany przez programistów Ashigaru. Możesz również kliknąć profil `ashigarudev` wskazany przez Keybase i sprawdzić, czy jego kluczowy odcisk palca odpowiada dokładnie : `A138 06B1 FA2A 676B`.



Jeśli jednak na tym etapie pojawi się błąd, oznacza to, że podpis jest nieprawidłowy. W takim przypadku **nie instaluj APK**. Zacznij od początku lub poproś społeczność o pomoc przed kontynuowaniem.



![Image](assets/fr/07.webp)



Keybase dostarczyła ci hash aplikacji. Teraz sprawdzimy, czy hash pobranego pliku `.apk` jest zgodny z tym zweryfikowanym w Keybase. Aby to zrobić, przejdź do [HASH FILE ONLINE](https://hash-file.online/).



![Image](assets/fr/08.webp)



Kliknij przycisk `BROWSE...` i wybierz plik `.apk` pobrany w kroku 2.1.


Następnie wybierz funkcję skrótu `SHA-256` i kliknij `CALCULATE HASH`, aby obliczyć skrót pliku.



![Image](assets/fr/09.webp)



Strona wyświetli hash twojego pliku `.apk`. Porównaj go z hashem zweryfikowanym na Keybase.io. Jeśli oba skróty są identyczne, weryfikacja autentyczności i integralności przebiegła pomyślnie. Możesz teraz przystąpić do instalacji aplikacji.



![Image](assets/fr/10.webp)



### 2.3. zainstalować aplikację Ashigaru



Aby zainstalować aplikację, otwórz menedżera plików telefonu i przejdź do folderu pobierania. Następnie kliknij plik `.apk`, który właśnie sprawdziłeś i potwierdź instalację po wyświetleniu monitu.



![Image](assets/fr/11.webp)



Ashigaru jest teraz zainstalowane na Twoim telefonie.



## 3. Zainicjuj aplikację i utwórz portfolio Bitcoin



Przy pierwszym uruchomieniu aplikacji wybierz `MAINNET`.



![Image](assets/fr/12.webp)



Następnie kliknij `Get Started`.



![Image](assets/fr/13.webp)



Utworzymy teraz nowy portfel Bitcoin. Naciśnij przycisk `Utwórz nowy wallet`.



![Image](assets/fr/14.webp)



### 3.1. utworzenie portfela Bitcoin



Ashigaru wymaga passphrase BIP39. Wybierz swój passphrase i wprowadź go w odpowiednich polach. Musi być tak długi i losowy, jak to możliwe, aby oprzeć się atakowi siłowemu.



Natychmiast wykonaj fizyczną kopię zapasową passphrase. Jest to bardzo ważny krok: w przypadku utraty telefonu, **jeśli nie masz już tego passphrase, nie będziesz już w stanie uzyskać dostępu do swoich bitcoinów** przechowywanych w Ashigaru wallet. Ten sam passphrase jest również używany do szyfrowania pliku odzyskiwania wallet.



Jeśli nie wiesz, czym jest passphrase lub nie w pełni rozumiesz, jak działa, zdecydowanie zalecamy przeczytanie tego dodatkowego samouczka. Jest to ważne, ponieważ passphrase jest krytycznym elementem bezpieczeństwa: niezrozumienie jego użycia może spowodować trwałą utratę środków.



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Po wprowadzeniu passphrase kliknij przycisk `NEXT`.



![Image](assets/fr/15.webp)



Następnie wybierz kod PIN. Kod ten będzie używany do odblokowania urządzenia Ashigaru wallet, chroniąc je przed nieautoryzowanym dostępem fizycznym. Nie jest on zaangażowany w kryptograficzne wyprowadzanie kluczy wallet. Oznacza to, że nawet bez znajomości kodu PIN, każda osoba posiadająca Twoją frazę mnemoniczną i passphrase będzie w stanie odzyskać dostęp do Twoich bitcoinów.



Wybierz długi, losowy kod PIN. Pamiętaj, aby przechowywać kopię zapasową w oddzielnej lokalizacji niż telefon, aby zapobiec jednoczesnemu naruszeniu ich bezpieczeństwa.



![Image](assets/fr/16.webp)



Po utworzeniu kodu PIN, Ashigaru wyświetla frazę mnemoniczną wallet. Ostrzeżenie: ta fraza, w połączeniu z passphrase, daje pełny dostęp do bitcoinów. Każdy, kto ją posiada, może przejąć twoje środki, nawet jeśli nie ma dostępu do twojego telefonu. Ta 12-wyrazowa sekwencja może zostać użyta do przywrócenia wallet w przypadku utraty, kradzieży lub uszkodzenia telefonu. Dlatego ważne jest, aby zachować go z najwyższą starannością na nośniku fizycznym (papierowym lub metalowym).



Nigdy nie zapisuj tej frazy w formie cyfrowej, w przeciwnym razie narażasz swoje środki na kradzież. W zależności od strategii bezpieczeństwa możesz utworzyć kilka fizycznych kopii, ale nigdy ich nie dziel. Zachowaj słowa w dokładnej kolejności i upewnij się, że są ponumerowane.



Wreszcie, nigdy nie przechowuj mnemonika i passphrase w tym samym miejscu. Jeśli oba zostaną naruszone jednocześnie, atakujący może uzyskać dostęp do wallet.



![Image](assets/fr/17.webp)



Aby dowiedzieć się więcej o tym, jak zabezpieczyć frazę mnemoniczną, zapoznaj się z tym uzupełniającym samouczkiem :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Następnie Ashigaru poprosi cię o ponowne potwierdzenie passphrase. Skorzystaj z okazji, aby sprawdzić, czy twoja fizyczna kopia zapasowa jest poprawna.



![Image](assets/fr/18.webp)



### 3.2. połączyć dojo



Następnie należy połączyć się z Dojo. Jak wyjaśniono we wstępie, Ashigaru musi być podłączony do Dojo, aby wchodzić w interakcje z siecią Bitcoin.



Zaloguj się do "Narzędzia konserwacji" swojego Dojo i otwórz menu `PAIRING`.



![Image](assets/fr/19.webp)



W Ashigaru naciśnij przycisk `Scan QR`, a następnie zeskanuj kod QR połączenia wyświetlany przez DMT. Następnie kliknij `Kontynuuj`, aby potwierdzić.



![Image](assets/fr/20.webp)



Wprowadź kod PIN, aby odblokować wallet. Spowoduje to przejście do strony synchronizacji. Błędy *PayNym* na tym etapie są normalne, ponieważ wallet jest nowy. Wystarczy kliknąć `Kontynuuj`.



![Image](assets/fr/21.webp)



Zostaniesz przeniesiony na stronę główną swojego portfolio.



![Image](assets/fr/22.webp)



Zanim przejdziemy dalej, zalecam przeprowadzenie testowego odzyskiwania, gdy wallet nadal nie zawiera bitcoinów. Umożliwi to sprawdzenie, czy papierowe kopie zapasowe działają prawidłowo. Aby dowiedzieć się, jak to zrobić, postępuj zgodnie z tym samouczkiem:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 4. Konfiguracja aplikacji Ashigaru



Aby uzyskać dostęp do ustawień aplikacji, kliknij na obrazek swojego *PayNym* w lewym górnym rogu, a następnie wybierz `Ustawienia`.



![Image](assets/fr/23.webp)



Tutaj znajdziesz kilka opcji dostosowania działania Ashigaru do swoich potrzeb. Zdecydowanie zalecam jednak aktywowanie 2 ważnych parametrów od samego początku.



Zacznij od otwarcia menu `Security > Stealth mode`, a następnie aktywuj tę funkcję, jeśli jej potrzebujesz. Ukrywa ona aplikację Ashigaru za nazwą, logo i interfejsem zwykłej aplikacji zainstalowanej na telefonie. Celem jest uniemożliwienie komukolwiek zidentyfikowania Ashigaru w przypadku fizycznej inspekcji telefonu.



![Image](assets/fr/24.webp)



Każda oferowana fałszywa aplikacja ma określoną metodę odblokowywania prawdziwego interfejsu Ashigaru. Na przykład, jeśli wybierzesz kalkulator, aplikacja Ashigaru zniknie z ekranu głównego i zostanie zastąpiona fałszywym kalkulatorem. Kiedy go otworzysz, zobaczysz klasyczny działający interfejs kalkulatora, ale aby uzyskać dostęp do Ashigaru, wszystko, co musisz zrobić, to szybko dotknąć symbolu `=` pięć razy.



Drugim ważnym parametrem, który należy aktywować, jest [**RBF** (*Replace-by-Fee*)](https://planb.academy/resources/glossary/rbf-replacebyfee). Opcja ta pozwala na zwiększenie kosztu transakcji, jeśli utknie ona w mempoolach z powodu zbyt niskiego kosztu. Można ją aktywować poprzez menu `Transakcje > Wydaj używając RBF`.



![Image](assets/fr/25.webp)



Wskazówka: Możesz zmienić jednostkę wyświetlania swojego portfela z `BTC` na `sat` po prostu klikając na całkowite saldo wyświetlane na stronie głównej.



## 5. Otrzymuj bitcoiny na Ashigaru



Teraz, gdy Twoje portfolio działa, możesz otrzymywać płatności. Aby to zrobić, naciśnij przycisk `+` w prawym dolnym rogu interfejsu, a następnie zielony przycisk `Odbierz`.



![Image](assets/fr/26.webp)



Następnie Ashigaru pokazuje pierwszy nieużywany adres odbiorczy w wallet, aby zapobiec ponownemu użyciu adresu (ponowne użycie adresu jest bardzo złą praktyką dla prywatności użytkownika). Możesz następnie przekazać ten adres osobie lub usłudze, która chce wysłać ci bitcoiny.



![Image](assets/fr/27.webp)



Gdy transakcja zostanie wyemitowana w sieci, automatycznie pojawi się na stronie głównej aplikacji.



![Image](assets/fr/28.webp)



## 6. Wysyłaj bitcoiny za pomocą Ashigaru



Teraz, gdy masz bitcoiny w Ashigaru wallet, możesz je również wysłać. Aby to zrobić, naciśnij przycisk `+` w prawym dolnym rogu, a następnie wybierz czerwony przycisk `Wyślij`.



![Image](assets/fr/29.webp)



Następnie wybierz konto, z którego chcesz dokonać wydatków. Na razie nie zajmowaliśmy się jeszcze kontem `Postmix`, zarezerwowanym dla coinjoinów, któremu przyjrzymy się w późniejszym samouczku. Wyślemy więc środki z głównego konta depozytowego.



![Image](assets/fr/30.webp)



Wprowadź szczegóły transakcji: kwotę do wysłania i adres Bitcoin odbiorcy.



![Image](assets/fr/31.webp)



Klikając na trzy małe kropki w prawym górnym rogu, a następnie na `Pokaż niewydane wyniki`, możesz również dokładnie wybrać, które UTXO chcesz wydać, aby zwiększyć swoją prywatność.



![Image](assets/fr/32.webp)



Po wypełnieniu wszystkich danych kliknij białą strzałkę u dołu interfejsu, aby kontynuować.



Następnie zostaniesz przeniesiony na stronę podsumowania zawierającą wszystkie szczegóły transakcji. Wyświetlanych jest kilka ważnych elementów:




- W bloku `Destination` po raz ostatni sprawdź, czy adres odbiorcy i wysłana kwota są prawidłowe;
- W bloku `Fees` można wyświetlić stawkę opłaty automatycznie wybraną przez Ashigaru i, jeśli to konieczne, zmodyfikować ją, klikając `MANAGE` ;
- Blok `Transaction` wskazuje typ transakcji, którą zamierzasz wykonać. Tutaj mówimy o prostej transakcji, ale Ashigaru obsługuje również inne rodzaje transakcji zoptymalizowanych pod kątem prywatności, które omówimy szczegółowo w przyszłym samouczku;
- Czerwony blok "Transaction Alert" ostrzega, jeśli transakcja wykazuje wzorce, które mogą zostać rozpoznane przez narzędzia do analizy łańcucha i które mogą zagrozić prywatności użytkownika. Klikając na niego, można wyświetlić szczegóły. Na przykład w moim przypadku Ashigaru mówi mi, że wysłana kwota jest okrągła (`3000 sats`), co pozwala mi wywnioskować, które wyjście odpowiada wydatkowi, a które wymianie. Aby dowiedzieć się więcej o heurystyce analizy łańcucha, zapraszam do śledzenia mojego szkolenia BTC 204 na Plan ₿ Academy ;
- Na koniec można dodać etykietę do transakcji, aby zachować zapis jej celu.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Po sprawdzeniu wszystkich informacji użyj zielonej strzałki, aby wysłać bitcoiny. Przytrzymaj strzałkę, a następnie przeciągnij ją w prawo, aby potwierdzić wysłanie.



![Image](assets/fr/33.webp)



Twoja transakcja została wyemitowana w sieci Bitcoin.



![Image](assets/fr/34.webp)



## 7. Odzyskiwanie Ashigaru wallet



Odzyskiwanie Ashigaru wallet różni się nieco od odzyskiwania klasycznego Bitcoin wallet, ponieważ aplikacja wykorzystuje te same metody co Samurai Wallet. W przypadku utraty dostępu do wallet (z powodu zapomnienia kodu PIN, odinstalowania lub zgubienia telefonu) istnieje kilka sposobów na odzyskanie bitcoinów.



Jeśli nadal masz dostęp do swojego telefonu lub jeśli wykonałeś kopię zapasową tego pliku, najprostszą metodą jest użycie pliku kopii zapasowej `ashigaru.txt`. Plik ten zawiera wszystkie informacje potrzebne do przywrócenia portfela na nowej instancji Ashigaru (lub na Sparrow Wallet), ale jest zaszyfrowany za pomocą passphrase zdefiniowanego w kroku 3.1 tego samouczka. Musisz więc mieć zarówno plik `ashigaru.txt`, jak i passphrase, aby użyć tej metody.



Dzięki tym dwóm elementom można na przykład przywrócić portfel na Sparrow Wallet.



![Image](assets/fr/35.webp)



Jeśli nie masz dostępu do pliku `ashigaru.txt`, nadal możesz odzyskać dostęp do swoich funduszy za pomocą frazy mnemonicznej passphrase, tak jak w przypadku każdego innego portfela Bitcoin. Zalecam wykonanie tego przywracania albo na nowej instancji Ashigaru, albo bezpośrednio na Sparrow Wallet, aby łatwo odzyskać ścieżki obejścia z Whirlpool, jeśli z niego korzystałeś. Alternatywnie można zaimportować te informacje do dowolnego innego oprogramowania kompatybilnego z BIP39, ręcznie wprowadzając ścieżki pochodne.



Aby uzyskać więcej informacji na temat tego procesu, zapoznaj się z kompletnym samouczkiem, który napisałem na temat odzyskiwania Wallet Samurai wallet. Ponieważ Ashigaru to fork, procedura jest identyczna:



https://planb.academy/tutorials/wallet/backup/samourai-recover-23bb6221-ea3e-42e6-a5b7-e6dbef5073c3

Jak widać, niezależnie od używanej metody przywracania, passphrase jest niezbędny. Dlatego należy starannie tworzyć kopie zapasowe. Można również wykonać kilka kopii, w zależności od strategii bezpieczeństwa.



## 8. Aktualizacja aplikacji



Aby zaktualizować aplikację Ashigaru, ponieważ zainstalowałeś ją z pliku `.apk`, a nie przez Sklep Play jak zwykłą aplikację, musisz pobrać nowy plik `.apk` odpowiadający zaktualizowanej wersji, a następnie zainstalować go ręcznie.



Powtórz kroki opisane w sekcji 2 tego samouczka, z wyjątkiem tego, że po kliknięciu pliku `.apk` w celu uruchomienia instalacji, **telefon z Androidem powinien oferować opcję `Update`, a nie `Install`**.



![Image](assets/fr/41.webp)



To bardzo ważny punkt: jeśli Android wyświetla `Install` zamiast `Update`, prawdopodobnie instalujesz fałszywą wersję. W takim przypadku należy natychmiast przerwać procedurę instalacji.



Podobnie jak w przypadku pierwszej instalacji, przed przystąpieniem do aktualizacji należy sprawdzić autentyczność i integralność pliku `.apk`.



Aby dowiedzieć się, kiedy dostępna będzie nowa wersja, należy od czasu do czasu sprawdzać oficjalną stronę Ashigaru. Zapewniamy, że Ashigaru jest stabilną, dojrzałą aplikacją, odziedziczoną po Samourai Wallet, a aktualizacje są stosunkowo rzadkie w porównaniu z młodszym oprogramowaniem.



## 9. Przekaż darowiznę na rzecz projektu Ashigaru



Ashigaru jest projektem open-source. Jeśli chcesz wesprzeć jego rozwój, możesz przekazać darowiznę bezpośrednio z aplikacji za pośrednictwem PayNym.



Aby to zrobić, kliknij swój PayNym w prawym górnym rogu interfejsu, a następnie wybierz kod płatności zaczynający się od `PM...`.



![Image](assets/fr/36.webp)



Następnie naciśnij przycisk `+` w prawym dolnym rogu ekranu.



![Image](assets/fr/37.webp)



Wybierz `Ashigaru Open Source Project` jako odbiorcę.



![Image](assets/fr/38.webp)



Kliknij przycisk `CONNECT`, aby ustanowić kanał komunikacyjny BIP47 (więcej o tym protokole w samouczku poniżej).



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

![Image](assets/fr/39.webp)



Po potwierdzeniu transakcji powiadomienia można wysłać darowizny do projektu, klikając małą białą strzałkę w prawym górnym rogu interfejsu.



![Image](assets/fr/40.webp)



Wiesz już, jak korzystać z podstawowych funkcji aplikacji Ashigaru. W przyszłych samouczkach przyjrzymy się, jak korzystać z zaawansowanych transakcji wydatków, a także Whirlpool, implementacji coinjoin odziedziczonej po Samurai Wallet.
https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add
