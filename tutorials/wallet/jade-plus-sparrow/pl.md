---
name: Jade Plus - Sparrow
description: Zaawansowana konfiguracja Jade Plus z Sparrow Wallet
---
![cover](assets/cover.webp)


Jade Plus to Hardware Wallet zaprojektowany przez Blockstream. Jest to następca klasycznego Jade, z ulepszonym oprogramowaniem, większą liczbą opcji i przeprojektowaną ergonomią dla bardziej intuicyjnego użytkowania. Ta nowa wersja może pochwalić się wspaniałym 1,9-calowym ekranem LCD o szerszej gamie kolorów niż jego poprzednik. Przyciski i nawigacja po menu również zostały zoptymalizowane.


Jade Plus może być używany na wiele sposobów: poprzez przewodowe połączenie USB-C, w trybie "*Air-Gap*" z kartą micro SD (wymagany adapter), przez Bluetooth, a nawet poprzez wymianę kodów QR dzięki zintegrowanej kamerze. Hardware Wallet jest zasilany bateryjnie.


Jest on dostępny od 149,99 USD w podstawowej czarnej wersji, a cena może wzrosnąć nawet o 20 USD w przypadku wersji "*Genesis Grey*" lub "*Lunar Silver*". Jade Plus jest zatem ciekawym wyborem, z zaawansowanymi funkcjami porównywalnymi do tych z wysokiej klasy portfeli sprzętowych, takich jak Coldcard Q lub Passport V2, ale w dość niskiej cenie, zbliżonej do modeli ze średniej półki.


![JADE-PLUS-SPARROW](assets/fr/01.webp)


Jade Plus jest kompatybilny z większością oprogramowania do zarządzania Wallet. Oto podsumowanie kompatybilności w momencie pisania tego tekstu (styczeń 2025 r.):


| Desktop | Mobile | USB | Bluetooth | QR | JadeLink | Management software
| ------------------- | ------- | ------ | --- | ----------- | --- | -------- |
| Blockstream Green | 🟢 | 🟢 | 🟢 (Mobile) | 🟢 | 🔴 |
| Liana | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 |
| Sparrow | 🟢 | 🔴 | 🟢 | 🔴 | 🟢 | 🟢 |
| Nunchuk | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |
| Specter | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |
| BlueWallet | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |
| Electrum | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 |
| Keeper | 🔴 | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 |

W tym samouczku skonfigurujemy zaawansowaną konfigurację Jade Plus z oprogramowaniem stacjonarnym Sparrow Wallet w trybie kodów QR. Ta konfiguracja jest idealna dla średnio zaawansowanych lub doświadczonych użytkowników. Jeśli szukasz prostszego podejścia dla początkujących, polecam zapoznać się z tym samouczkiem, w którym używamy Jade Plus z Green Wallet przez połączenie Bluetooth:


https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0

## Model bezpieczeństwa Jade Plus


Jade Plus wykorzystuje model bezpieczeństwa oparty na "wirtualnym bezpiecznym elemencie", materializowanym przez "ślepą wyrocznię". Mówiąc konkretnie, mechanizm ten łączy kod PIN wybrany przez użytkownika, sekret hostowany na Jade i sekret przechowywany przez wyrocznię (serwer utrzymywany przez Blockstream), aby utworzyć klucz AES-256 dystrybuowany przez dwa podmioty. Podczas inicjacji ECDH Exchange zabezpiecza komunikację z wyrocznią i szyfruje frazę odzyskiwania na Hardware Wallet. W praktyce, gdy chcesz uzyskać dostęp do seed w celu podpisania transakcji, potrzebujesz dostępu do :




- Samo urządzenie Jade Plus;
- Aby wprowadzić kod PIN w celu odblokowania urządzenia ;
- I do tajemnicy wyroczni.


Główną zaletą tego podejścia jest brak pojedynczego punktu awarii na poziomie sprzętowym, ponieważ jeśli atakujący kiedykolwiek uzyska dostęp do Jade, wyodrębnienie kluczy wymaga jednoczesnego naruszenia Jade i wyroczni. Model ten oznacza również, że Jade Plus jest całkowicie open-source, unikając ograniczeń związanych z wykorzystaniem prawdziwie fizycznie bezpiecznych Elements, takich jak te stosowane na przykład w Ledger.


Wadą tego systemu jest to, że korzystanie z Jade Plus zależy od wyroczni utrzymywanej przez Blockstream. Jeśli ta wyrocznia stanie się niedostępna, nie będzie już możliwe korzystanie z Hardware Wallet bezpośrednio za pomocą kodu PIN. Nie oznacza to jednak, że bitcoiny zostaną utracone, ponieważ nadal można je odzyskać za pomocą frazy odzyskiwania, którą można wprowadzić w Jade Plus w trybie "*stateless*". Aby obejść tę zależność, można również skonfigurować własny serwer Oracle i zarządzać nim.


Inną opcją zarządzania seed jest po prostu niezarejestrowanie go w Jade Plus. W takim przypadku Jade staje się wyłącznie urządzeniem do podpisu. Podczas inicjalizacji, oprócz zwykłego zapisywania frazy odzyskiwania jako słów, zostanie ona również zapisana jako ręcznie wygenerowany kod QR. W ten sposób za każdym razem, gdy używasz Wallet, możesz zaimportować seed za pomocą kamery Jade. Może to być interesująca opcja dla zaawansowanych użytkowników, w zależności od strategii bezpieczeństwa, ale musisz uważać, aby zarówno zapisać seed, jak i go chronić, ponieważ nawet jako kod QR pozwoliłby każdemu ukraść twoje fundusze. Przyjrzymy się tej opcji w tym samouczku, ale nie jest ona obowiązkowa.


## Rozpakowywanie Jade Plus


Po otrzymaniu Jade Plus sprawdź, czy pudełko i Seal są w dobrym stanie, aby upewnić się, że paczka nie była otwierana.


![JADE-PLUS-SPARROW](assets/fr/02.webp)


W pudełku znajdują się :




- Le Jade Plus;
- Kabel USB-C;
- Karty do nagrywania frazy Mnemonic jako słowa lub jako "*CompactSeedQR*";
- Niektóre instrukcje użytkowania ;
- Przewód;
- Niektóre naklejki.


![JADE-PLUS-SPARROW](assets/fr/03.webp)


Urządzenie posiada 4 przyciski nawigacyjne:




- Przycisk w prawym dolnym rogu włącza Jade;
- Duży przycisk z przodu urządzenia służy do wybierania pozycji;
- Dwa małe przyciski u góry umożliwiają nawigację w lewo i w prawo;
- Można również wybrać element, klikając jednocześnie dwa przyciski w górnej części urządzenia.


![JADE-PLUS-SPARROW](assets/fr/04.webp)


## Konfigurowanie nowego Bitcoin Wallet


Kliknij przycisk Start.


![JADE-PLUS-SPARROW](assets/fr/05.webp)


Kliknij na "*Setup Jade*".


![JADE-PLUS-SPARROW](assets/fr/06.webp)


Wybierz opcję "Ustawienia zaawansowane*".


![Image](assets/fr/07.webp)


Następnie kliknij "*Utwórz nowy Wallet*", aby utworzyć nowy seed. Do wyboru jest 12- lub 24-wyrazowa fraza Mnemonic. Bezpieczeństwo Wallet pozostaje równoważne w przypadku obu opcji, więc wygodniejsze może być wybranie najprostszej opcji zapisu, tj. 12 słów.


![Image](assets/fr/08.webp)


Kliknij przycisk "*Kontynuuj*", aby wyświetlić nową frazę odzyskiwania.


![Image](assets/fr/09.webp)


Jade Plus wyświetla 12-wyrazową frazę Mnemonic. **Mnemonic daje ci pełny, nieograniczony dostęp do wszystkich twoich bitcoinów. Każdy, kto posiada tę frazę, może ukraść Twoje środki, nawet bez fizycznego dostępu do Jade Plus. 12-wyrazowa fraza przywraca dostęp do bitcoinów w przypadku utraty, kradzieży lub uszkodzenia Jade. Dlatego bardzo ważne jest, aby zachować ją ostrożnie i przechowywać w bezpiecznym miejscu.


Napis można umieścić na kartonie dołączonym do pudełka lub, dla większego bezpieczeństwa, zalecam wygrawerowanie go na podstawie ze stali nierdzewnej, aby chronić go przed pożarem, powodzią lub upadkiem.


![Image](assets/fr/10.webp)


Aby uzyskać więcej informacji na temat prawidłowego sposobu zapisywania i zarządzania frazą Mnemonic, zdecydowanie polecam skorzystanie z tego samouczka, zwłaszcza jeśli jesteś początkującym:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

oczywiście nigdy nie wolno dzielić się tymi słowami w Internecie, tak jak robię to w tym samouczku. Ten przykładowy Wallet będzie używany tylko na Testnet i zostanie usunięty pod koniec samouczka.**_


Kliknij strzałkę po prawej stronie ekranu, aby wyświetlić następujące słowa.


![Image](assets/fr/11.webp)


Po zapisaniu frazy Jade Plus poprosi o jej potwierdzenie. Wybierz właściwe słowo zgodnie z kolejnością za pomocą przycisków w górnej części urządzenia i kliknij środkowy przycisk, aby przejść do następnego słowa.


![Image](assets/fr/12.webp)


Następnie dostępne są 2 opcje. Jak wyjaśniono we wstępie, możesz zapisać seed bezpośrednio na urządzeniu i użyć systemu ochrony Blockstream "*Virtual Secure Element*", aby uzyskać dostęp do Wallet (opcja 1) lub zapisać seed jako kod QR i skanować go za każdym razem, gdy go używasz (opcja 2).


Dla Opcji 1 wybierz "*Nie*", a dla Opcji 2 wybierz "*Tak*".


![Image](assets/fr/13.webp)


### Opcja 1: Odblokowanie kodem QR PIN


Jeśli wybrałeś opcję 1 (CompactSeedQR: "*No*"), zostaniesz przeniesiony bezpośrednio do wyboru metody połączenia. W tym samouczku chcemy używać urządzenia w trybie Air-Gap poprzez wymianę kodów QR, więc wybierz "*QR*".


![Image](assets/fr/27.webp)


Kliknij "*Kontynuuj*".


![Image](assets/fr/28.webp)


Kod PIN służy do odblokowania urządzenia Jade i zapewnia ochronę przed nieautoryzowanym dostępem fizycznym. Ten kod PIN nie bierze udziału w tworzeniu kluczy kryptograficznych Wallet. Tak więc, nawet bez dostępu do tego kodu PIN, posiadanie 12-wyrazowej frazy Mnemonic umożliwi odzyskanie dostępu do bitcoinów. Zalecamy wybranie jak najbardziej losowego kodu PIN. Upewnij się również, że zapisujesz ten kod w miejscu innym niż to, w którym przechowujesz swoje Jade, na przykład w menedżerze haseł.


Wybierz 6-cyfrowy kod PIN na urządzeniu Jade, używając przycisków w lewo i w prawo do przewijania cyfr oraz środkowego przycisku do potwierdzania każdej cyfry.


![Image](assets/fr/29.webp)


Potwierdź kod PIN po raz drugi.


![Image](assets/fr/30.webp)


Jak wyjaśniono we wstępie, seed jest przechowywany zaszyfrowany w Jade Plus. Aby go odszyfrować, należy podać :




- Prawidłowy kod PIN (który właśnie skonfigurowaliśmy);
- Sekret wyroczni utrzymywanej przez Blockstream.


W tym zaawansowanym samouczku użyjemy Sparrow Wallet do zarządzania naszym Bitcoin Wallet. Jednak w przeciwieństwie do oprogramowania Green Wallet firmy Blockstream, Sparrow nie ma dostępu do wyroczni na serwerach Blockstream. Dlatego będziemy korzystać ze strony internetowej Blockstream, aby pobrać sekret wyroczni za każdym razem, gdy odblokujemy Jade Plus.


Odwiedź https://jadefw.blockstream.com/pinqr/index.html


Kliknij na "*Start QR Unlock*".


![Image](assets/fr/31.webp)


Kliknij "*Done*", ponieważ kod PIN został już wybrany w Jade Plus.


![Image](assets/fr/32.webp)


Użyj kamery komputera, aby zeskanować kody QR wyświetlane na ekranie tabletu Jade.


![Image](assets/fr/33.webp)


Potwierdź na Jade, aby przejść do następnego ekranu.


![Image](assets/fr/34.webp)


Zeskanuj kod QR widoczny teraz na stronie, aby odzyskać sekret wyroczni.


![Image](assets/fr/35.webp)


Po utworzeniu Wallet można przejść do kolejnych kroków i pominąć podsekcję "*Opcja 2: CompactSeedQR*".


![Image](assets/fr/36.webp)


Przy każdym uruchomieniu należy kliknąć "*QR Mode*".


![Image](assets/fr/37.webp)


Wybierz opcję "*QR PIN Unlock*".


![Image](assets/fr/38.webp)


Wprowadź kod PIN.


![Image](assets/fr/39.webp)


Następnie przejdź do [strony Blockstream] (https://jadefw.blockstream.com/pinqr/qrpin.html), aby Exchange kody QR z wyrocznią.


![Image](assets/fr/40.webp)


Jadeit jest teraz odblokowany.


![Image](assets/fr/41.webp)


### Opcja 2: CompactSeedQR


Jeśli wybrałeś opcję 2 (CompactSeedQR: "*Yes*"), kliknij ponownie "*Yes*".


![Image](assets/fr/14.webp)


Kliknij "*Start*".


![Image](assets/fr/15.webp)


Możesz użyć bazy kodów QR dostarczonej w pudełku Jade Plus. Wybierz odpowiednie pole w zależności od tego, czy zdecydowałeś się na zdanie składające się z 12 czy 24 słów. Można również [wydrukować szablon ze strony internetowej Blockstream](https://help.blockstream.com/hc/article_attachments/41928319071769).


Jade Plus wyświetli każdą strefę kodu QR.


![Image](assets/fr/16.webp)


Użyj długopisu, aby pokolorować kwadraty i odtworzyć seed jako kod QR. Bądź precyzyjny, aby kamera Jade Plus mogła go później zeskanować. Użyj strzałki, aby przejść do następnego obszaru.


![Image](assets/fr/17.webp)


Po zakończeniu kliknij "*Done*".


![Image](assets/fr/18.webp)


Zeskanuj ręcznie wykonany kod QR za pomocą Jade Plus, aby sprawdzić jego ważność.


![Image](assets/fr/19.webp)


Jeśli kopia zapasowa papieru jest prawidłowa, kliknij "*Kontynuuj*".


![Image](assets/fr/20.webp)


W tym samouczku będziemy używać trybu połączenia opartego wyłącznie na skanowaniu kodów QR, więc wybierz "*QR*".


![Image](assets/fr/21.webp)


Możesz także dodać kod PIN oprócz kopii zapasowej CompactSeedQR, jak w opcji 1. Zapewnia to dwa sposoby dostępu do Wallet: albo za pomocą kodu PIN i systemu "Virtual Secure Element" Blockstream, albo za pośrednictwem CompactSeedQR.


Jeśli zdecydujesz się na opcję podwójnego kodu PIN, wybierz "*PIN*" i wykonaj te same kroki, co w opcji 1, aby ustawić kod PIN.


Jeśli wolisz kontynuować tylko z CompactSeedQR, wybierz "*SeedQR*".


![Image](assets/fr/22.webp)


Po utworzeniu Wallet możesz przejść do kolejnych kroków.


![Image](assets/fr/23.webp)


Przy każdym uruchomieniu należy kliknąć przycisk "*QR Mode*", a następnie "*Scan SeedQR*".


![Image](assets/fr/24.webp)


Użyj aparatu urządzenia, aby zeskanować zapisany seed jako kod QR.


![Image](assets/fr/25.webp)


Jadeit jest teraz odblokowany.


![Image](assets/fr/26.webp)


## Dodaj BIP39 passphrase


BIP39 passphrase to opcjonalne hasło, które można dowolnie wybrać i które jest dodawane do frazy Mnemonic w celu wzmocnienia bezpieczeństwa Wallet. Po włączeniu tej funkcji dostęp do Bitcoin Wallet będzie wymagał zarówno Mnemonic, jak i passphrase. Bez nich odzyskanie Wallet byłoby niemożliwe.


Przed skonfigurowaniem tej opcji w Jade Plus zdecydowanie zaleca się przeczytanie tego artykułu, aby w pełni zrozumieć teoretyczne działanie passphrase i uniknąć błędów, które mogą prowadzić do utraty bitcoinów:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Gdy urządzenie Jade jest nadal zablokowane (do passphrase można wejść tylko wtedy, gdy urządzenie nie jest odblokowane), przejdź do menu "*Opcje*".


![Image](assets/fr/42.webp)


Wybierz "*BIP39 passphrase*".


![Image](assets/fr/43.webp)


W opcji "*Częstotliwość*" można wybrać, czy Jade Plus będzie prosić o wprowadzenie passphrase przy każdym uruchomieniu:




- "*Disabled*" wyłącza korzystanie z passphrase;
- "*Next Login Only*" będzie wymagać powrotu do tego menu w celu aktywowania żądania dla passphrase przy następnym uruchomieniu. Ta opcja pozwala nie ujawniać jej użycia;
- "*Zawsze pytaj*" powoduje, że Jade systematycznie pyta o passphrase przy każdym uruchomieniu, ujawniając w ten sposób, że Wallet jest chroniony przez passphrase.


Wybierz opcję zgodnie ze swoją strategią bezpieczeństwa. Osobiście wybieram opcję "*Zawsze pytaj*".


![Image](assets/fr/44.webp)


Następnie można wybrać jedną z dwóch metod wprowadzania passphrase:




- "*Ręczna*: Wirtualna klawiatura umożliwia wprowadzanie liter (dużych i małych), cyfr i symboli, znak po znaku. Jest to standardowa metoda dla wszystkich portfeli sprzętowych;
- "*WordList*": Specyficzna metoda zaprojektowana przez Blockstream dla Jade, która przyspiesza wprowadzanie passphrase i zwiększa jego entropię. Podczas wprowadzania system sugeruje słowa z listy BIP39, ułatwiając odblokowanie. Ta metoda automatycznie generuje zdanie, łącząc wybrane słowa, oddzielone spacjami (przykład: `abandon ability able`).


Osobiście radzę skorzystać z pierwszej metody, ponieważ jest to standard, który można znaleźć na wszystkich innych wspornikach Wallet.


![Image](assets/fr/45.webp)


Następnie można powrócić do ekranu głównego i odblokować Wallet w normalny sposób, używając kodu PIN lub CompactSeedQR (jak pokazano powyżej). Następnie zostaniesz poproszony o wprowadzenie swojego passphrase.


![Image](assets/fr/46.webp)


Wprowadź je na klawiaturze Jade i pamiętaj o utworzeniu jednej lub więcej kopii zapasowych na nośniku fizycznym (papierowym lub metalowym). W przykładzie użyłem bardzo słabego passphrase, ale musisz wybrać silny, losowy passphrase, który zawiera wszystkie typy znaków i jest wystarczająco długi (jak silne hasło).


![Image](assets/fr/47.webp)


Jeśli passphrase jest ważny, potwierdź.


![Image](assets/fr/48.webp)


Należy pamiętać, że w hasłach BIP39 rozróżniana jest wielkość liter i literówki. Jeśli wprowadzisz passphrase nieznacznie różniący się od początkowo skonfigurowanego, Jade nie zgłosi błędu, ale wyprowadzi inny zestaw kluczy kryptograficznych, które nie będą tymi w początkowym Wallet.


Dlatego ważne jest, aby podczas konfiguracji zanotować odcisk palca klucza głównego, który można znaleźć w prawym dolnym rogu ekranu. Na przykład, w przypadku mojego passphrase `PBN`, mój odcisk palca klucza głównego to `3AD1AE65`.


![Image](assets/fr/49.webp)


Za każdym razem, gdy odblokowujesz urządzenie Jade za pomocą passphrase, sprawdź, czy odcisk palca jest taki sam, jak ten wprowadzony podczas konfiguracji. Jeśli tak, passphrase jest prawidłowy i uzyskujesz dostęp do właściwego Bitcoin Wallet. Jeśli nie, jesteś na niewłaściwym Wallet i musisz spróbować ponownie, uważając, aby nie popełnić żadnych błędów.


Przed otrzymaniem pierwszych bitcoinów w Wallet, **Zalecam wykonanie pustego testu odzyskiwania**. Zanotuj informacje referencyjne, takie jak xpub lub pierwszy otrzymany Address, a następnie usuń Wallet na Jade Plus, gdy jest jeszcze pusty (`Opcje -> Urządzenie -> Przywracanie ustawień fabrycznych`). Następnie spróbuj przywrócić Wallet przy użyciu papierowych kopii zapasowych frazy Mnemonic i dowolnego passphrase. Sprawdź, czy informacje o plikach cookie wygenerowane po przywróceniu są zgodne z pierwotnie zapisanymi. Jeśli tak, możesz mieć pewność, że Twoje papierowe kopie zapasowe są wiarygodne. Aby dowiedzieć się więcej o tym, jak przeprowadzić odzyskiwanie testowe, zapoznaj się z tym samouczkiem:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Konfiguracja Wallet na Sparrow Wallet


W tym samouczku przedstawiam zaawansowane wykorzystanie Jade Plus przy użyciu Sparrow Wallet. Hardware Wallet jest jednak kompatybilny z wieloma innymi programami, takimi jak Liana, Nunchuk, Specter, Green i Keeper. Kompatybilności te różnią się pod względem połączeń: USB, Bluetooth lub kod QR (szczegóły w tabeli we wstępie).


Zacznij od pobrania i zainstalowania Sparrow Wallet [z oficjalnej strony internetowej] (https://sparrowwallet.com/) na swoim komputerze, jeśli jeszcze tego nie zrobiłeś.


![Image](assets/fr/50.webp)


Przed instalacją należy sprawdzić autentyczność i integralność oprogramowania. Jeśli nie wiesz, jak to zrobić, zapoznaj się z tym samouczkiem:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Po otwarciu Sparrow Wallet kliknij zakładkę "*File*", a następnie "*New Wallet*".


![Image](assets/fr/51.webp)


Nazwij swój Wallet, a następnie kliknij "*Create Wallet*".


![Image](assets/fr/52.webp)


Wybierz "*Airgapped Hardware Wallet*".


![Image](assets/fr/53.webp)


Kliknij "*Scan...*" obok opcji "*Jade*".


![Image](assets/fr/54.webp)


Odblokuj Jade Plus i, jeśli go używasz, wprowadź passphrase. Następnie przejdź do menu "*Opcje*", wybierz "*Wallet*" i kliknij "*Eksportuj Xpub*".


![Image](assets/fr/55.webp)


Jade wyświetli Keystore za pomocą kilku kodów QR. Zeskanuj je na swoim urządzeniu za pomocą aplikacji Sparrow.


![Image](assets/fr/56.webp)


Powinieneś teraz zobaczyć swój xpub i odcisk palca klucza głównego, który powinien pasować do tego na Jade Plus. Kliknij "*Zastosuj*".


![Image](assets/fr/57.webp)


Ustaw silne hasło, aby zabezpieczyć dostęp do Sparrow Wallet. Hasło to będzie chronić klucze publiczne, adresy, etykiety i historię transakcji przed nieautoryzowanym dostępem. Dobrym pomysłem jest zapisanie tego hasła w menedżerze haseł, aby go nie zapomnieć.


![Image](assets/fr/58.webp)


Twój Wallet jest teraz poprawnie skonfigurowany w Sparrow.


![Image](assets/fr/59.webp)


## Odbieranie bitcoinów


Teraz, gdy Jade Plus jest skonfigurowany, możesz odebrać swój pierwszy Sats na nowym Bitcoin Wallet. Aby to zrobić, w aplikacji Sparrow kliknij menu "*Receive*".


![Image](assets/fr/60.webp)


Sparrow wyświetli pierwszy pusty odbiór Address w Wallet.


![Image](assets/fr/61.webp)


Przed użyciem sprawdźmy go na ekranie Jade Plus, aby upewnić się, że należy do naszego Bitcoin Wallet. Na Jade kliknij "*Scan QR*", a następnie zeskanuj kod QR Address wyświetlany na Sparrow.


![Image](assets/fr/62.webp)


Sprawdź, czy Address wyświetlany na ekranie Jade odpowiada temu wyświetlanemu na Sparrow Wallet. Jeśli tak, kliknij znacznik wyboru, aby kontynuować.


![Image](assets/fr/63.webp)


Następnie Hardware Wallet potwierdzi, że Address jest częścią Wallet i że posiada powiązany klucz prywatny.


![Image](assets/fr/64.webp)


Jeśli Address zostanie zatwierdzony przez Jade, możesz teraz użyć go do otrzymania bitcoinów. Gdy transakcja zostanie rozgłaszana w sieci, pojawi się na Sparrow. Poczekaj, aż otrzymasz wystarczającą liczbę potwierdzeń, aby uznać transakcję za ostateczną.


![Image](assets/fr/65.webp)


## Wysyłanie bitcoinów


Teraz, gdy masz już kilka Sats w swoim Wallet, możesz je również wysłać. Aby to zrobić, kliknij menu "*UTXO*".


![Image](assets/fr/66.webp)


Wybierz UTXO, których chcesz użyć jako danych wejściowych dla tej transakcji, a następnie kliknij "*Wyślij wybrane*".


![Image](assets/fr/67.webp)


Wprowadź numer Address odbiorcy, etykietę przypominającą o celu transakcji oraz kwotę, którą chcesz wysłać na ten numer Address.


![Image](assets/fr/68.webp)


Dostosuj stawkę opłaty do aktualnych warunków rynkowych, a następnie kliknij "*Twórz transakcję*".


![Image](assets/fr/69.webp)


Sprawdź, czy wszystkie parametry transakcji są prawidłowe, a następnie kliknij "*Finalize Transaction for Signing*".


![Image](assets/fr/70.webp)


Kliknij "*Pokaż QR*", aby wyświetlić PSBT (*Partially Signed Bitcoin Transaction*). Sparrow utworzył transakcję, ale nadal brakuje jej podpisów do odblokowania bitcoinów użytych w danych wejściowych. Te podpisy mogą być wykonane tylko przez Jade Plus, który hostuje seed, dając dostęp do kluczy prywatnych potrzebnych do podpisania transakcji.


![Image](assets/fr/71.webp)


Na Jade Plus kliknij "*Scan QR*", aby zeskanować PSBT wyświetlany na Sparrow.


![Image](assets/fr/72.webp)


Potwierdź, że przesyłka Address i wysłana kwota są prawidłowe, a następnie kliknij strzałkę, aby zatwierdzić.


![Image](assets/fr/73.webp)


Upewnij się, że kwota opłaty jest zgodna z wybraną, a następnie kliknij ikonę zaznaczenia w lewym górnym rogu Interface, aby podpisać transakcję.


![Image](assets/fr/74.webp)


W aplikacji Sparrow Wallet kliknij "*Scan QR*" i zeskanuj kod QR wyświetlony na urządzeniu Jade.


![Image](assets/fr/75.webp)


Podpisana transakcja jest teraz gotowa do transmisji w sieci Bitcoin i włączenia do bloku przez Miner. Jeśli wszystko jest w porządku, kliknij "*Broadcast Transaction*".


![Image](assets/fr/76.webp)


Twoja transakcja została nadana i oczekuje na potwierdzenie.


![Image](assets/fr/77.webp)


Gratulacje, wiesz już jak skonfigurować i używać Jade Plus w trybie QR. Jeśli ten poradnik okazał się przydatny, będę wdzięczny za pozostawienie poniżej kciuka Green. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dzięki za udostępnienie!


Aby przejść dalej, polecam ten inny samouczek dotyczący Jade Plus, w którym konfigurujemy go przez Bluetooth za pomocą aplikacji mobilnej Green:


https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0