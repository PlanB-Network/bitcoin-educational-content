---
name: Satochip
description: Konfiguracja i korzystanie z karty inteligentnej Satochip
---
![cover](assets/cover.webp)


Hardware Wallet to urządzenie elektroniczne przeznaczone do zarządzania i zabezpieczania kluczy prywatnych Bitcoin Wallet. W przeciwieństwie do portfeli programowych (lub portfeli Hot) instalowanych na maszynach ogólnego przeznaczenia często podłączonych do Internetu, portfele sprzętowe pozwalają na fizyczną izolację kluczy prywatnych, zmniejszając ryzyko włamania i kradzieży.


Głównym celem Hardware Wallet jest zminimalizowanie funkcjonalności urządzenia w celu zmniejszenia jego powierzchni ataku. Mniejsza powierzchnia ataku oznacza również mniej potencjalnych wektorów ataku, tj. mniej słabych punktów w systemie, które atakujący mogliby wykorzystać, aby uzyskać dostęp do bitcoinów.


Zaleca się korzystanie z Hardware Wallet w celu zabezpieczenia bitcoinów, zwłaszcza w przypadku posiadania znacznych ich ilości, zarówno pod względem wartości bezwzględnej, jak i udziału w całkowitych aktywach.


Portfele sprzętowe są używane w połączeniu z oprogramowaniem zarządzającym Wallet na komputerze lub smartfonie. Oprogramowanie to zarządza tworzeniem transakcji, ale podpis kryptograficzny niezbędny do walidacji tych transakcji jest wykonywany wyłącznie w Hardware Wallet. Oznacza to, że klucze prywatne nigdy nie są narażone na potencjalnie wrażliwe środowisko.


Portfele sprzętowe zapewniają użytkownikowi podwójną ochronę: z jednej strony zabezpieczają bitcoiny przed zdalnymi atakami, utrzymując klucze prywatne w trybie offline, a z drugiej strony generalnie oferują lepszą odporność fizyczną na próby wyodrębnienia kluczy. I to właśnie na podstawie tych 2 kryteriów bezpieczeństwa można ocenić i uszeregować różne modele dostępne na rynku.


W tym samouczku proponuję odkryć jedno z tych rozwiązań: Satochip.


## Wprowadzenie do Satochip


Satochip to Hardware Wallet w formie karty z certyfikowanym chipem *EAL6+*, który jest bardzo wysokim standardem bezpieczeństwa (*NXP JCOP*). Jest on produkowany przez belgijską firmę.


![SATOCHIP](assets/notext/01.webp)


Ta inteligentna karta jest sprzedawana za 25 euro, co jest bardzo przystępną ceną w porównaniu do innych portfeli sprzętowych na rynku. Chip jest bezpiecznym elementem, który zapewnia bardzo dobrą odporność na ataki fizyczne. Co więcej, jego kod jest open-source (*AGPLv3*).

Jednak ze względu na swój format, Satochip nie oferuje tak wielu opcji, jak inne urządzenia. Nie ma oczywiście baterii, kamery, ani czytnika kart micro SD, gdyż jest to karta. Jego największą wadą, moim zdaniem, jest brak ekranu na Hardware Wallet, co czyni go bardziej podatnym na niektóre rodzaje zdalnych ataków. W rzeczywistości zmusza to użytkownika do podpisywania na ślepo i ufania temu, co widzi na ekranie komputera.


Pomimo swoich ograniczeń, Satochip pozostaje interesujący ze względu na obniżoną cenę. Ten Wallet może być w szczególności wykorzystany do zwiększenia bezpieczeństwa Wallet wydatkowego, a także Wallet oszczędnościowego chronionego przez Hardware Wallet wyposażony w ekran. Jest to również dobre rozwiązanie dla tych, którzy posiadają niewielkie ilości bitcoinów i nie chcą inwestować setek euro w bardziej zaawansowane urządzenie. Co więcej, wykorzystanie Satochips w konfiguracjach Multisig lub potencjalnie w systemach Wallet z blokadą czasową w przyszłości, może zaoferować interesujące korzyści.


Firma Satochip oferuje również 2 inne produkty. Istnieje Satodime, która jest kartą na okaziciela przeznaczoną do przechowywania bitcoinów offline, ale nie pozwala na transakcje. Jest to rodzaj papierowego Wallet, który jest znacznie bezpieczniejszy i może być używany na przykład do robienia prezentów. Wreszcie jest Seedkeeper, który jest menedżerem fraz Mnemonic. Może być używany do bezpiecznego zapisywania naszych seed bez bezpośredniego zapisywania ich na kartce papieru.


## Jak kupić Satochip?


Satochip jest dostępny w sprzedaży [na oficjalnej stronie internetowej](https://satochip.io/product/satochip/). Aby kupić go w sklepie fizycznym, można również znaleźć [listę certyfikowanych sprzedawców](https://satochip.io/resellers/) na stronie internetowej Satochip.


Satochip oferuje dwie możliwości interakcji z oprogramowaniem do zarządzania Wallet: za pośrednictwem komunikacji NFC lub czytnika kart inteligentnych. W przypadku opcji NFC należy upewnić się, że urządzenie jest kompatybilne z tą technologią lub zaopatrzyć się w zewnętrzny czytnik NFC. Satochip działa na standardowej częstotliwości 13,56 MHz. W przeciwnym razie można również kupić czytnik kart inteligentnych. Można go znaleźć na stronie internetowej Satochip lub w innym miejscu.


![SATOCHIP](assets/notext/02.webp)


## Jak skonfigurować Satochip za pomocą Sparrow?


Po otrzymaniu urządzenia Satochip pierwszym krokiem jest sprawdzenie, czy opakowanie nie zostało otwarte. Opakowanie Satochip powinno zawierać naklejkę plombującą. Brak tej naklejki lub jej uszkodzenie może oznaczać, że karta inteligentna została naruszona i może nie być autentyczna.

![SATOCHIP](assets/notext/03.webp)

W środku znajdziesz Satochip.


![SATOCHIP](assets/notext/04.webp)


Do zarządzania Wallet, w tym poradniku, sugeruję użycie Sparrow. Jeśli nie masz jeszcze tego oprogramowania, [odwiedź oficjalną stronę, aby je pobrać] (https://sparrowwallet.com/download/). Możesz również zapoznać się z naszym samouczkiem na temat Sparrow Wallet (wkrótce).


![SATOCHIP](assets/notext/05.webp)


Włóż Satochip do czytnika kart inteligentnych lub umieść go na czytniku NFC i podłącz czytnik do komputera, na którym otwarta jest aplikacja Sparrow.


![SATOCHIP](assets/notext/06.webp)


Otwórz Sparrow Wallet i upewnij się, że jesteś prawidłowo podłączony do węzła Bitcoin. Aby to zrobić, sprawdź zaznaczenie w prawym dolnym rogu: powinno być żółte, jeśli jesteś podłączony do węzła publicznego, Green dla połączenia z Bitcoin Core lub niebieskie dla Electrum.


![SATOCHIP](assets/notext/07.webp)


W aplikacji Sparrow Wallet kliknij zakładkę "*Plik*".


![SATOCHIP](assets/notext/08.webp)


Następnie w menu "*Nowy Wallet*".


![SATOCHIP](assets/notext/09.webp)


Wybierz nazwę dla swojego Wallet, a następnie kliknij "*Create Wallet*".


![SATOCHIP](assets/notext/10.webp)


Kliknij przycisk "*Podłączony Hardware Wallet*".


![SATOCHIP](assets/notext/11.webp)


Kliknij przycisk "*Scan...*".


![SATOCHIP](assets/notext/12.webp)


Powinien pojawić się twój Satochip. Kliknij na "*Import Keystore*".


![SATOCHIP](assets/notext/13.webp)


Następnie musisz ustawić kod PIN, aby odblokować Satochip. Wybierz silne hasło, składające się z 4 do 16 znaków. Utwórz kopię zapasową tego hasła.


Należy pamiętać, że to hasło nie jest hasłem passphrase. Oznacza to, że nawet bez tego hasła, fraza Mnemonic pozwoli na ponowne zaimportowanie Wallet do oprogramowania, jeśli zajdzie taka potrzeba. Hasło służy wyłącznie do zabezpieczenia dostępu do samego urządzenia Satochip. Jest to odpowiednik kodu PIN, który można znaleźć w innych portfelach sprzętowych.


Po wprowadzeniu hasła kliknij ponownie przycisk "*Import Keystore*".


![SATOCHIP](assets/notext/14.webp)


Ponownie wpisz hasło, a następnie kliknij przycisk "*Initialize*".


![SATOCHIP](assets/notext/15.webp)


Następnie pojawi się okno generowania frazy Mnemonic. Kliknij przycisk "*generate New*".


![SATOCHIP](assets/notext/16.webp)

Wykonaj jedną lub więcej fizycznych kopii frazy odzyskiwania, zapisując ją na papierze lub metalowym nośniku. Należy pamiętać, że ta fraza zapewnia pełny dostęp do bitcoinów bez żadnych dodatkowych zabezpieczeń. Dlatego też, gdyby ktoś ją odkrył, mógłby natychmiast ukraść twoje bitcoiny, nawet bez dostępu do twojego Satochipa lub jego kodu PIN. Dlatego ważne jest, aby zabezpieczyć te kopie zapasowe. Co więcej, ta fraza pozwala odzyskać dostęp do bitcoinów w przypadku utraty, uszkodzenia Satochip lub zapomnienia kodu PIN.

![SATOCHIP](assets/notext/17.webp)


Twój Bitcoin Wallet został pomyślnie utworzony.


![SATOCHIP](assets/notext/18.webp)


Kliknij ponownie przycisk "*Import Keystore*".


![SATOCHIP](assets/notext/19.webp)


Twój Wallet został utworzony. Klucze prywatne są teraz przechowywane na karcie inteligentnej urządzenia Satochip. Kliknij przycisk "*Apply*", aby kontynuować.


![SATOCHIP](assets/notext/20.webp)


Zaleca się ustawienie dodatkowego hasła w celu zabezpieczenia informacji publicznych zarządzanych przez Sparrow Wallet, oprócz kodu PIN Satochip. Hasło to zapewni bezpieczeństwo dostępu do Sparrow Wallet, co pomaga chronić klucze publiczne, adresy i historię transakcji przed nieautoryzowanym dostępem.


![SATOCHIP](assets/notext/21.webp)


Wprowadź hasło w dwóch polach, a następnie kliknij przycisk "*Ustaw hasło*".


![SATOCHIP](assets/notext/22.webp)


I gotowe, twój Satochip jest teraz skonfigurowany na Sparrow Wallet.


![SATOCHIP](assets/notext/23.webp)


Po utworzeniu Wallet można odłączyć Satochip. Przechowuj go w bezpiecznym miejscu!


## Jak odbierać bitcoiny za pomocą Satochip?


Po wejściu do Wallet kliknij zakładkę "*Odbierz*".


![SATOCHIP](assets/notext/24.webp)


Sparrow Wallet generuje Address dla twojego Wallet. Zwykle w przypadku innych portfeli sprzętowych zaleca się kliknięcie "*Wyświetl Address*", aby zweryfikować Address bezpośrednio na ekranie urządzenia. Niestety, ta opcja nie jest dostępna w przypadku Satochip, ale upewnij się, że korzystasz z niej w przypadku innych portfeli.


![SATOCHIP](assets/notext/25.webp)


Możesz dodać "*Label*", aby opisać źródło bitcoinów, które zostaną zabezpieczone za pomocą tego Address. Jest to dobra praktyka, która pomaga lepiej zarządzać UTXO.


![SATOCHIP](assets/notext/26.webp)


Więcej informacji na temat etykietowania można znaleźć w tym poradniku:


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Następnie możesz użyć tego Address, aby otrzymać bitcoiny.


![SATOCHIP](assets/notext/27.webp)

## Jak wysyłać Bitcoiny za pomocą Satochip?

Teraz, gdy otrzymałeś swoje pierwsze Sats w swoim bezpiecznym Wallet z Satochip, możesz je również wydać! Podłącz Satochip do komputera, uruchom Sparrow Wallet, a następnie przejdź do zakładki "*Wyślij*", aby utworzyć nową transakcję.


![SATOCHIP](assets/notext/28.webp)


Jeśli chcesz kontrolować monety, czyli konkretnie wybrać, które UTXO mają zostać wykorzystane w transakcji, przejdź do zakładki "*UTXOs*". Wybierz UTXO, które chcesz wydać, a następnie kliknij "*Wyślij wybrane*". Nastąpi przekierowanie do tego samego ekranu w zakładce "*Wyślij*", ale z UTXO już wybranymi do transakcji.


![SATOCHIP](assets/notext/29.webp)


Wprowadź docelowy adres Address. Można również wprowadzić wiele adresów, klikając przycisk "*+ Add*".


![SATOCHIP](assets/notext/30.webp)


Zanotuj "*Label*", aby zapamiętać cel tego wydatku.


![SATOCHIP](assets/notext/31.webp)


Wybierz kwotę wysłaną do tego Address.


![SATOCHIP](assets/notext/32.webp)


Dostosuj stawkę opłaty za transakcję do aktualnego rynku.


![SATOCHIP](assets/notext/33.webp)


Upewnij się, że wszystkie parametry transakcji są prawidłowe, a następnie kliknij "*Twórz transakcję*".


![SATOCHIP](assets/notext/34.webp)


Jeśli wszystko jest w porządku, kliknij "*Finalizuj transakcję do podpisu*".


![SATOCHIP](assets/notext/35.webp)


Kliknij "*Podpisz*".


![SATOCHIP](assets/notext/36.webp)


Kliknij ponownie "*Sign*" obok swojego Satochipa.


![SATOCHIP](assets/notext/37.webp)


Wprowadź kod PIN swojego Satochip, a następnie ponownie kliknij "*Podpisz*", aby podpisać transakcję.


![SATOCHIP](assets/notext/38.webp)


Transakcja została podpisana. Kliknij "*Rozgłoś transakcję*", aby rozgłosić ją w sieci Bitcoin.


![SATOCHIP](assets/notext/39.webp)


Można ją znaleźć w zakładce "*Transakcje*" w Sparrow Wallet.


![SATOCHIP](assets/notext/40.webp)


Gratulacje, masz już wiedzę na temat korzystania z Satochip! Jeśli ten poradnik okazał się pomocny, będę wdzięczny za kciuk w górę poniżej. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dziękuję bardzo!