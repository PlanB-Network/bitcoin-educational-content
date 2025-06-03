---
name: Wysłannik
description: Konfigurowanie i używanie paszportu z aplikacją Envoy
---
![cover](assets/cover.webp)


Envoy to aplikacja do zarządzania Bitcoin Wallet opracowana przez Foundation. Jest ona specjalnie zaprojektowana do użytku z Passport Hardware Wallet.


Passport "*Batch 2*" zaprezentowany w tym poradniku wraz z aplikacją Envoy jest następcą "*Founder's Edition*". Wyróżnia się wysokiej jakości wzornictwem, kolorowym ekranem o wysokiej rozdzielczości i ergonomiczną klawiaturą fizyczną. Działa w trybie "*Air-Gap*", zapewniając, że klucze prywatne Wallet pozostają całkowicie odizolowane, a komunikacja jest możliwa za pośrednictwem karty MicroSD lub kodów QR. Urządzenie jest wyposażone w wymienną, ładowalną baterię Nokia BL-5C o pojemności 1200 mAh. Ten niezastrzeżony akumulator można łatwo wymienić, ponieważ model BL-5C jest powszechnie dostępny w sklepach.


Jeśli chodzi o łączność, Passport jest wyposażony w port MicroSD, port USB-C do ładowania i tylną kamerę do skanowania kodów QR.


Jeśli chodzi o bezpieczeństwo, Passport zawiera bezpieczny element, a kod źródłowy urządzenia jest całkowicie open-source. Oferuje wszystkie funkcje oczekiwane od dobrego Bitcoin Hardware Wallet. Należy pamiętać, że Passport nie obsługuje jeszcze miniscript, ale ta funkcja jest planowana na drugi kwartał 2025 roku.


Wyceniony na 199 USD, Passport jest pozycjonowany jako wysokiej klasy Hardware Wallet, konkurując z modelami Coldcard Q, Jade Plus, Tezor Safe 5 i Ledger z najwyższej półki.


![Image](assets/fr/01.webp)


Aby zarządzać bezpiecznym Wallet na Passport, masz kilka opcji. Ten Hardware Wallet jest kompatybilny z większością oprogramowania do zarządzania Wallet na rynku, w tym między innymi Sparrow Wallet, Specter Desktop, Nunchuk, Keeper.


W tym samouczku, który jest skierowany do początkujących i średnio zaawansowanych użytkowników, dowiemy się, jak korzystać z aplikacji Envoy z Passport. Jest to najprostszy sposób na maksymalne wykorzystanie możliwości Hardware Wallet.


Jeśli jesteś zaawansowanym użytkownikiem i chcesz poznać bardziej złożone funkcje, polecam zapoznać się z tym innym samouczkiem, w którym konfigurujemy Passport za pomocą Sparrow Wallet :


https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

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


## Pobierz aplikację Envoy


Przejdź do sklepu z aplikacjami, aby pobrać Envoy :




- W sklepie [Google Play Store] (https://play.google.com/store/apps/details?id=com.foundationdevices.envoy);
- W [App Store](https://apps.apple.com/us/app/envoy-by-foundation/id1584811818);
- Na [F-Cold](https://foundation.xyz/fdroid/).


![Image](assets/fr/50.webp)


Plik APK można również pobrać bezpośrednio [z repozytorium GitHub Fundacji] (https://github.com/Foundation-Devices/envoy/releases).


![Image](assets/fr/51.webp)


Po otwarciu aplikacji wybierz "*Manage Passport*".


![Image](assets/fr/52.webp)


Wybierz, czy chcesz aktywować połączenie Tor, aby zwiększyć poufność, a następnie naciśnij "*Kontynuuj*".


![Image](assets/fr/53.webp)


Wybierz "*Podłącz istniejący Paszport*", jeśli Paszport jest już skonfigurowany, lub "*Ustaw nowy Paszport*", jeśli inicjujesz Hardware Wallet po raz pierwszy.


![Image](assets/fr/54.webp)


Zaakceptuj warunki użytkowania.


![Image](assets/fr/55.webp)


Następnie zostaniesz poproszony o zweryfikowanie autentyczności paszportu. Kliknij "*Next*".


![Image](assets/fr/56.webp)


## Paszport startowy


Naciśnij przycisk włączania/wyłączania z boku urządzenia, aby je uruchomić.


![Image](assets/fr/04.webp)


Naciśnij przycisk potwierdzenia, aby przejść do następnego menu.


![Image](assets/fr/05.webp)


W tym samouczku użyjemy Envoy do zarządzania Wallet zabezpieczonym paszportem. Wybierz "*Envoy App*".


![Image](assets/fr/57.webp)


Kliknij na "*Kontynuuj na Envoy*".


![Image](assets/fr/58.webp)


Następnym krokiem jest sprawdzenie urządzenia. Potwierdza to autentyczność paszportu i zapewnia, że nie został on naruszony podczas transportu. Zostaniesz poproszony o zeskanowanie kodu QR.


![Image](assets/fr/08.webp)


Zeskanuj dynamiczne kody QR wyświetlane w aplikacji za pomocą paszportu. Po zakończeniu skanowania kliknij "*Next*".


![Image](assets/fr/59.webp)


Następnie zeskanuj telefonem kod QR wyświetlony na paszporcie.


![Image](assets/fr/60.webp)


Jeśli pojawi się komunikat "*Twój paszport jest zabezpieczony*", oznacza to, że Hardware Wallet jest autentyczny. Można go teraz użyć do zabezpieczenia Bitcoin Wallet.


![Image](assets/fr/61.webp)


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


### Bez aplikacji Envoy


Aby to zrobić, użyj karty MicroSD dołączonej do pudełka Passport (lub innej) i włóż ją do komputera. Pobierz najnowszą wersję oprogramowania układowego z [strony dokumentacji Foundation](https://docs.foundation.xyz/firmware-updates/passport/) lub [ich repozytorium GitHub](https://github.com/Foundation-Devices/passport2/releases).


![Image](assets/fr/21.webp)


Przed zainstalowaniem go na urządzeniu zdecydowanie zalecamy sprawdzenie autentyczności i integralności pobranego oprogramowania układowego. Jeśli potrzebujesz pomocy, zapoznaj się z tym samouczkiem :


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### Z aplikacją Envoy


Inną, prostszą opcją jest skorzystanie bezpośrednio z aplikacji Envoy. Kliknij na "*Download Firmware*".


![Image](assets/fr/62.webp)


Do podłączenia karty MicroSD do telefonu należy użyć adaptera dostarczonego z urządzeniem Passport.


![Image](assets/fr/63.webp)


Wybierz kartę MicroSD w eksploratorze plików, aby zapisać oprogramowanie sprzętowe.


![Image](assets/fr/64.webp)


Oprogramowanie sprzętowe zostało zapisane. Wyjmij kartę MicroSD ze smartfona i włóż ją do urządzenia Passport.


![Image](assets/fr/65.webp)


Otworzy się eksplorator plików Passport. Wybierz plik `vN.N.N-passport.bin`.


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


Paszport będzie teraz zawierał generate "*Backup Code*". Jest to seria liczb, które mogą być użyte do odszyfrowania kopii zapasowej Wallet zapisanej na karcie MicroSD. Ten system kopii zapasowych, specyficzny dla urządzeń Foundation, stanowi dodatkową kopię zapasową frazy Mnemonic, ale nie jest kompatybilny z innym oprogramowaniem Bitcoin.


Jeśli zdecydujesz się użyć tego "*Kodu kopii zapasowej*", pamiętaj, aby przechowywać go w innym miejscu niż kartę MicroSD zawierającą zaszyfrowaną kopię zapasową Wallet. Możesz jednak zrezygnować z tego systemu, jeśli uważasz, że dobra kopia zapasowa frazy Mnemonic jest wystarczająca.


![Image](assets/fr/31.webp)


Wprowadź swój "*Backup Code*", aby potwierdzić, że zapisałeś go poprawnie.


![Image](assets/fr/32.webp)


Jeśli karta MicroSD została włożona, zaszyfrowana kopia zapasowa Wallet została na niej zapisana.


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


## Konfiguracja Wallet na Envoy


W tym samouczku pokażę, jak używać Passport z aplikacją Envoy. Jednak ten Hardware Wallet jest również kompatybilny z Sparrow Wallet, Keeper, BlueWallet, Nunchuk, Specter i wieloma innymi...


![Image](assets/fr/66.webp)


Użyj aplikacji Envoy, aby zeskanować kod QR wyświetlony na paszporcie.


![Image](assets/fr/67.webp)


Klucze publiczne zostały zaimportowane do aplikacji. Kliknij na "*Validate receive Address*".


![Image](assets/fr/68.webp)


Użyj paszportu, aby zeskanować Address wyświetlany na Envoy.


![Image](assets/fr/69.webp)


Twój paszport potwierdzi, czy Wallet zaimportowany przez Envoy jest ważny. Potwierdź to w aplikacji.


![Image](assets/fr/70.webp)


Możesz teraz uzyskać dostęp do publicznych informacji Wallet na Envoy, ale aby wydać bitcoiny, musisz użyć swojego paszportu.


![Image](assets/fr/71.webp)


## Menu Discover Passport


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


Można również wprowadzić BIP39 passphrase lub użyć tymczasowego seed.


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


Można aktywować funkcję "*Security Words*", która zwiększa bezpieczeństwo Layer, wyświetlając dwa określone słowa podczas odblokowywania urządzenia po wprowadzeniu pierwszych czterech cyfr kodu PIN. Słowa te, zapisywane podczas konfiguracji, zapewniają, że Passport nie został wymieniony ani zmodyfikowany. W przypadku jakichkolwiek rozbieżności w późniejszym terminie zalecamy nieużywanie urządzenia. Zalecam aktywowanie tej opcji, aby zapobiec większości zagrożeń związanych z fizycznym naruszeniem urządzenia.


![Image](assets/fr/48.webp)


Wreszcie, podmenu "*Extensions*" umożliwia aktywację funkcji specyficznych dla niektórych zastosowań urządzenia, takich jak protokół Whirlpool CoinJoin.


![Image](assets/fr/49.webp)


## Odbieranie bitcoinów


Teraz, gdy Paszport jest już skonfigurowany, możesz odebrać swój pierwszy Sats na nowym Bitcoin Wallet. Aby to zrobić, w Envoy kliknij na swoje konto "*Primary 0*".


![Image](assets/fr/72.webp)


Kliknij przycisk "*Odbierz*".


![Image](assets/fr/73.webp)


Aplikacja Envoy wyświetla pierwszy dostępny pusty Address na Wallet. Przed użyciem sprawdźmy Address na ekranie Passport, aby upewnić się, że naprawdę należy do naszego Bitcoin Wallet. W menu Passport "*Konto*" wybierz "*Narzędzia konta*".


![Image](assets/fr/74.webp)


Kliknij na "*Verify Address*", a następnie zeskanuj kod QR wyświetlony na Envoy.


![Image](assets/fr/75.webp)


Upewnij się, że Address wyświetlany na Paszporcie odpowiada dokładnie temu wyświetlanemu na Sparrow i że pojawia się "*Verified*".


![Image](assets/fr/76.webp)


Możesz teraz używać go do otrzymywania bitcoinów. Gdy transakcja zostanie rozgłaszana w sieci, pojawi się na Envoy. Poczekaj, aż otrzymasz wystarczającą liczbę potwierdzeń, aby uznać transakcję za ostateczną.


![Image](assets/fr/77.webp)


## Wysyłanie bitcoinów


Teraz, gdy masz już kilka Sats w swoim Wallet, możesz je również wysłać. Aby to zrobić, kliknij przycisk "*Wyślij*".


![Image](assets/fr/78.webp)


Wprowadź Address odbiorcy, wklejając go bezpośrednio lub skanując kod QR za pomocą aparatu smartfona.


![Image](assets/fr/79.webp)


Określ kwotę, którą chcesz wysłać, a następnie kliknij "*Potwierdź*".


![Image](assets/fr/80.webp)


Wybierz opłatę transakcyjną zgodnie z aktualną sytuacją rynkową, a następnie sprawdź informacje o transakcji. Jeśli wszystko się zgadza, kliknij "*Podpisz paszportem*".


![Image](assets/fr/81.webp)


Dodaj etykietę do transakcji, aby zachować jasny zapis jej celu.


![Image](assets/fr/82.webp)


Następnie Envoy wyświetla PSBT (*Partially Signed Bitcoin Transaction*). Aplikacja utworzyła transakcję, ale nadal brakuje podpisu (podpisów), aby odblokować bitcoiny użyte w danych wejściowych. Te podpisy mogą być wykonane tylko przez Passport, który hostuje seed dając dostęp do kluczy prywatnych potrzebnych do podpisania transakcji.


![Image](assets/fr/83.webp)


W aplikacji Passport przejdź do menu "*Account*" i kliknij "*Sign with QR Code*".


![Image](assets/fr/84.webp)


Zeskanuj PSBT (*Partially Signed Bitcoin Transaction*) wyświetlany na Envoy.


![Image](assets/fr/85.webp)


Potwierdź, że odbierany Address i wysłana kwota są prawidłowe, a następnie naciśnij przycisk potwierdzenia.


![Image](assets/fr/86.webp)


Sprawdź Exchange Address. W moim przykładzie nie ma żadnego, ponieważ transakcja obejmuje jedno wyjście.


![Image](assets/fr/87.webp)


Upewnij się, że opłata jest taka, jaką wybrałeś.


![Image](assets/fr/88.webp)


Jeśli wszystkie informacje są poprawne, kliknij przycisk potwierdzenia, aby podpisać transakcję.


![Image](assets/fr/89.webp)


Paszport pokazuje podpisaną transakcję w postaci kodu QR.


![Image](assets/fr/90.webp)


W aplikacji Envoy kliknij ikonę kodu QR, a następnie zeskanuj PSBT wyświetlony na ekranie paszportu.


![Image](assets/fr/91.webp)


Sprawdź szczegóły transakcji po raz ostatni. Jeśli wszystko się zgadza, naciśnij "*Wyślij transakcję*", aby rozgłosić ją w sieci Bitcoin.


![Image](assets/fr/92.webp)


Twoja transakcja oczekuje teraz na potwierdzenie. Możesz śledzić jej status bezpośrednio ze swojego konta.


![Image](assets/fr/93.webp)


Gratulacje, wiesz już jak skonfigurować i używać Passport z aplikacją Envoy. Jeśli ten poradnik okazał się przydatny, będę wdzięczny za pozostawienie kciuka Green poniżej. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dzięki za udostępnienie!


Więcej informacji można znaleźć w naszym samouczku na temat oprogramowania Liana:


https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04