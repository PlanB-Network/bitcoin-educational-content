---
name: Specter DIY
description: Instrukcja konfiguracji Specter DIY
---

![cover](assets/cover.webp)


## Specter-DIY


> Cypherpunks piszą kod. Wiemy, że ktoś musi napisać oprogramowanie do obrony prywatności, a ponieważ nie możemy uzyskać prywatności, chyba że wszyscy to zrobimy, napiszemy je.

*Manifest Cypherpunk - Eric Hughes - 9 marca 1993 r.*


Ideą projektu jest zbudowanie sprzętowego wallet z gotowych komponentów.

Mimo że mamy płytkę rozszerzeń, która umieszcza wszystko w ładnej formie i pomaga uniknąć lutowania, będziemy nadal wspierać i utrzymywać kompatybilność ze standardowymi komponentami.


![image](assets/fr/01.webp)


Chcemy również zachować elastyczność projektu, tak aby mógł on działać na dowolnym innym zestawie komponentów przy minimalnych zmianach. Może chcesz stworzyć sprzętowy wallet na innej architekturze (RISC-V?), z modemem audio jako kanałem komunikacyjnym - powinieneś być w stanie to zrobić. Dodawanie lub zmienianie funkcjonalności Spectera powinno być łatwe, a my staramy się abstrahować moduły logiczne tak bardzo, jak to tylko możliwe.


Kody QR są domyślnym sposobem komunikacji Spectera z hostem. Kody QR są dość wygodne i pozwalają użytkownikowi kontrolować transmisję danych - każdy kod QR ma bardzo ograniczoną pojemność, a komunikacja odbywa się jednokierunkowo. I jest airgapped - nie trzeba podłączać wallet do komputera w żadnym momencie.


W przypadku przechowywania sekretów obsługujemy tryb agnostyczny (wallet zapomina o wszystkich sekretach po wyłączeniu), tryb lekkomyślny (przechowuje sekrety w pamięci flash mikrokontrolera aplikacji), a integracja secure element nastąpi wkrótce.


Naszym głównym celem jest konfiguracja wielopodpisowa z innymi portfelami sprzętowymi, ale wallet może również działać jako pojedynczy podpisujący. Staramy się, aby był kompatybilny z Bitcoin Core tam, gdzie możemy - PSBT dla niepodpisanych transakcji, deskryptory wallet do importowania/eksportowania portfeli multisig. Aby ułatwić komunikację z Bitcoin Core, pracujemy również nad [Specter Desktop app](https://github.com/cryptoadvance/specter-desktop) - małym serwerem Python Flask komunikującym się z węzłem Bitcoin Core.


Większość oprogramowania układowego jest napisana w języku MicroPython, co ułatwia audyt i zmianę kodu. Używamy biblioteki [secp256k1](https://github.com/bitcoin-core/secp256k1) z Bitcoin Core do obliczeń krzywych eliptycznych i biblioteki [LittlevGL](https://lvgl.io/) do GUI.


## Zastrzeżenie


Projekt znacznie dojrzał, do tego stopnia, że poziom bezpieczeństwa Specter-DIY jest obecnie porównywalny z komercyjnymi portfelami sprzętowymi dostępnymi na rynku. Wdrożyliśmy bezpieczny bootloader, który weryfikuje aktualizacje oprogramowania układowego, dzięki czemu można mieć pewność, że tylko podpisane oprogramowanie układowe może zostać przesłane do urządzenia po początkowej konfiguracji. Jednak w przeciwieństwie do komercyjnych urządzeń podpisujących, bootloader musi być zainstalowany ręcznie przez użytkownika i nie jest ustawiony fabrycznie przez dostawcę urządzenia. Dlatego należy zwrócić szczególną uwagę podczas początkowej instalacji oprogramowania układowego i upewnić się, że zweryfikowano podpisy PGP i sflashowano oprogramowanie układowe z bezpiecznego komputera.


Jeśli coś nie działa, otwórz problem tutaj lub zadaj pytanie w naszej grupie [Telegram](https://t.me/+VEinVSYkW5TUl5Ai).


## Lista zakupów dla Specter-DIY


Tutaj opisujemy co kupić, a w następnej części wyjaśniamy jak to złożyć i kilka uwag o płycie - zworki zasilania, porty USB itp.


### Płyta Discovery


Główną częścią urządzenia jest płytka deweloperska:



- Płytka deweloperska STM32F469I-DISCO (np. z [Mouser](https://eu.mouser.com/ProductDetail/STMicroelectronics/STM32F469I-DISCO?qs=kWQV1gtkNndotCjy2DKZ4w==) lub [Digikey](https://www.digikey.com/product-detail/en/stmicroelectronics/STM32F469I-DISCO/497-15990-ND/5428811))
- Kabel mini**USB
- Standardowy kabel MicroUSB do komunikacji przez USB


Opcjonalne, ale zalecane:


- [Skaner kodów QR Waveshare](https://www.waveshare.com/barcode-scanner-module.htm) z długimi pinami, takimi jak [te](https://eu.mouser.com/ProductDetail/Samtec/DW-02-10-T-S-571?qs=sGAEpiMZZMvlX3nhDDO4AE5PKXAQeC6NPk%2FcLBS9yKI%3D) lub [te](https://www.amazon.com/gp/product/B015KA0RRU/), aby podłączyć skaner do płytki (potrzebne są 4 piny).


Obecnie pracujemy nad płytką rozszerzającą, która zawiera gniazdo kart inteligentnych, skaner kodów QR, baterię i obudowę wydrukowaną w 3D, ale nie zawiera głównej części - płytki discovery, którą należy zamówić osobno. W ten sposób atak na łańcuch dostaw nadal nie jest problemem, ponieważ kluczowe dla bezpieczeństwa komponenty są kupowane w losowym sklepie elektronicznym.


Możesz zacząć korzystać ze Spectera nawet bez żadnych dodatkowych komponentów, ale będziesz mógł komunikować się z nim przez USB lub wbudowane gniazdo kart SD. Używanie Spectera przez USB oznacza, że nie jest on zabezpieczony przed dostępem powietrza, więc tracisz ważną właściwość bezpieczeństwa.


### Skaner QR


W przypadku skanera kodów QR dostępnych jest kilka opcji.


**Opcja 1. Zalecane.** Rozsądnie dobry skaner z Waveshare (40$)


[Skaner Waveshare](https://www.waveshare.com/barcode-scanner-module.htm) - będziesz musiał znaleźć sposób, jak ładnie go zamontować, może użyj jakiejś osłony Arduino Prototype i taśmy klejącej.


Lutowanie nie jest wymagane, ale jeśli masz umiejętności lutownicze, możesz sprawić, że wallet będzie o wiele ładniejszy ;)


**Opcja 2.** Bardzo fajny skaner od Mikroe, ale dość drogi (150$):


[Kliknięcie kodu kreskowego](https://www.mikroe.com/barcode-click) + [Adapter](https://www.mikroe.com/arduino-uno-click-shield)


**Opcja 3.** Dowolny inny skaner QR


W Chinach można znaleźć tanie skanery. Ich jakość często nie jest najlepsza, ale można zaryzykować. Może nawet ESPcamera spełni swoje zadanie. Wystarczy podłączyć zasilanie, UART (piny D0 i D1) i trigger do D5.


**Opcja 4.** Brak skanera.


Wtedy można używać Specter tylko z USB / kartą SD.


Chyba że zbudujesz własny moduł komunikacyjny, który wykorzystuje coś innego zamiast kodów QR - audiomodem, bluetooth lub cokolwiek innego. Jeśli tylko można go uruchomić i wysłać dane przez port szeregowy, można robić, co się chce.


### Komponenty opcjonalne


Jeśli dodasz mały powerbank lub baterię i ładowarkę / wzmacniacz, twój wallet stanie się całkowicie samowystarczalny ;)



## Montaż Specter-DIY



![video](https://youtu.be/1H7FqG_FmCw)


### Podłączanie skanera kodów kreskowych Waveshare


Oprogramowanie sprzętowe wallet skonfiguruje skaner przy pierwszym uruchomieniu, więc nie jest wymagana ręczna konfiguracja wstępna.


Oto jak podłączyć skaner do płyty:


![image](assets/fr/02.webp)


Dla wygody można kupić Arduino Protype shield i przylutować i zamontować wszystko na nim (np. [ten](https://www.digikey.com/catalog/en/partgroup/proto-shield-rev3-uno-size/79347))


### Zarządzanie energią


Na górnej stronie płytki znajduje się zworka, która określa, skąd będzie pobierane zasilanie. Możesz zmienić pozycję zworki i wybrać źródło zasilania jako jeden z portów USB lub pin VIN i podłączyć tam zewnętrzną baterię (powinna być 5V).


### Obudowa dla majsterkowiczów


Sprawdź folder [enclosures](https://github.com/cryptoadvance/specter-diy/tree/master/docs/enclosures).


### Bądź kreatywny!


Złóż swój własny Specter-DIY i prześlij nam zdjęcia (wyślij żądanie ściągnięcia lub skontaktuj się z nami).


Sprawdź [Galerię](https://github.com/cryptoadvance/specter-diy/blob/master/docs/pictures/gallery/README.md) z widmami stworzonymi przez społeczność!




## Instalowanie skompilowanego kodu


Dzięki bezpiecznemu bootloaderowi początkowa instalacja oprogramowania układowego jest nieco inna. Aktualizacje są łatwiejsze i nie wymagają podłączania sprzętu wallet do komputera.


![video](https://youtu.be/eF4cgK_L6T4)


### Flashowanie początkowego oprogramowania sprzętowego


**Uwaga** Jeśli nie chcesz używać plików binarnych z wydań, sprawdź [dokumentację bootloadera](https://github.com/cryptoadvance/specter-bootloader/blob/master/doc/selfsigned.md), która wyjaśnia, jak skompilować i skonfigurować go tak, aby używał twoich kluczy publicznych zamiast naszych.



- Jeśli dokonujesz aktualizacji z wersji poniżej `1.4.0` lub wgrywasz firmware po raz pierwszy, użyj pliku `initial_firmware_<version>.bin` ze strony [releases](https://github.com/cryptoadvance/specter-diy/releases).
 - Zweryfikuj podpis pliku `sha256.signed.txt` względem [klucza PGP Stepana](https://stepansnigirev.com/ss-specter-release.asc)
 - Zweryfikuj hash pliku `initial_firmware_<version>.bin` względem hasha zapisanego w pliku `sha256.signed.txt`
- Jeśli dokonujesz aktualizacji z pustego bootloadera lub widzisz komunikat o błędzie bootloadera informujący, że oprogramowanie sprzętowe jest nieprawidłowe, zapoznaj się z następną sekcją - Flashowanie podpisanego oprogramowania sprzętowego Specter.
- Upewnij się, że zworka zasilania karty wykrywającej znajduje się w pozycji STLK
- Podłącz kartę discovery do komputera za pomocą kabla **miniUSB** znajdującego się w górnej części karty.
    - Płyta powinna pojawić się jako dysk wymienny o nazwie `DIS_F469NI`.
- Skopiuj plik `initial_firmware_<version>.bin` do katalogu głównego systemu plików `DIS_F469NI`.
- Po zakończeniu flashowania oprogramowania układowego płyta zresetuje się i uruchomi ponownie bootloader. Bootloader sprawdzi firmware i uruchomi główne oprogramowanie. Jeśli pojawi się komunikat o błędzie, że nie znaleziono oprogramowania układowego - postępuj zgodnie z instrukcjami aktualizacji i prześlij oprogramowanie układowe za pomocą karty SD.
- Teraz możesz przestawić zworkę zasilania tam, gdzie chcesz i zasilać płytkę z powerbanku lub baterii.


Flashowanie początkowego oprogramowania układowego za pomocą kopiuj-wklej pliku `.bin` czasami kończy się niepowodzeniem - często z powodu kabla lub po podłączeniu urządzenia przez koncentrator USB. W takim przypadku możesz spróbować jeszcze kilka razy (zwykle działa w 2-3 próbach).


Jeśli cały czas się nie udaje, można użyć narzędzia open-source [stlink](https://github.com/stlink-org/stlink/releases/latest). Zainstaluj je i wpisz w terminalu: `st-flash write <path/to/initial_firmare.bin> 0x80000`. Zwykle działa to znacznie bardziej niezawodnie.


### Aktualizacja oprogramowania sprzętowego



- Pobierz `specter_upgrade_<version>.bin` ze strony [releases](https://github.com/cryptoadvance/specter-diy/releases).
- Skopiuj ten plik binarny do katalogu głównego karty SD (sformatowanej w systemie FAT, maks. 32 GB)
 - Upewnij się, że w katalogu głównym znajduje się tylko jeden plik `specter_upgrade***.bin`
- Włóż kartę SD do gniazda SD karty discovery i włącz zasilanie karty
- Bootloader sflashuje oprogramowanie sprzętowe i powiadomi o zakończeniu.
- Zrestartuj płytę - zobaczysz teraz interfejs Specter-DIY, który zasugeruje ci wybranie kodu PIN


Za każdym razem, gdy pojawi się nowa wersja, wystarczy pobrać plik `specter_upgrade_<version>.bin` z wydań, wrzucić go na kartę SD i zaktualizować urządzenie, tak jak w poprzednim kroku. Bootloader upewni się, że na płytę można załadować tylko podpisane oprogramowanie układowe.


### Jak sprawdzić wersję oprogramowania sprzętowego


Przejdź do menu `Ustawienia urządzenia` - pod tytułem ekranu pojawi się numer wersji.


## Użyj Specter-DIY wallet



![video](https://youtu.be/Oysg-hhBusc)



![video](https://youtu.be/XfMr7B_uUIk)



![video](https://youtu.be/BzBlh_knIww)



## Bezpieczeństwo Specter-DIY


### Sprzęt


Wyświetlacz jest kontrolowany przez MCU aplikacji.


Integracja bezpiecznych elementów nie została jeszcze osiągnięta - w tej chwili sekrety są również przechowywane na głównym MCU. Można jednak korzystać z wallet bez przechowywania sekretu - za każdym razem należy wprowadzić frazę odzyskiwania. Po co pamiętać długo passphrase, skoro można zapamiętać cały mnemonik?


Urządzenie wykorzystuje zewnętrzną pamięć flash do przechowywania niektórych plików (QSPI), ale wszystkie pliki użytkownika są podpisywane przez wallet i sprawdzane po załadowaniu.


Funkcja skanowania QR znajduje się na oddzielnym mikrokontrolerze, więc całe przetwarzanie obrazu odbywa się poza krytycznym dla bezpieczeństwa MCU. W tej chwili USB i karta SD są nadal zarządzane przez główny MCU, więc nie używaj karty SD i USB, jeśli chcesz zmniejszyć powierzchnię ataku.


### Ochrona kodem PIN (uwierzytelnianie użytkownika)


Podczas pierwszego uruchomienia na głównym MCU generowany jest unikalny sekret. Ten sekret pozwala zweryfikować, czy urządzenie nie zostało zastąpione złośliwym - po wprowadzeniu kodu PIN zobaczysz listę słów, które pozostaną niezmienione, dopóki sekret tam jest.


Twój kod PIN wraz z tym unikalnym sekretem są używane do generate klucza deszyfrującego dla twoich kluczy Bitcoin (jeśli je przechowujesz). Jeśli więc atakujący będzie w stanie ominąć ekran PIN, odszyfrowanie nadal nie powiedzie się.


Jeśli zablokowałeś firmware (TODO: dodaj link do instrukcji tutaj), skutecznie zablokuje to również sekret, więc jeśli atakujący załaduje inny firmware na płytę, sekret zostanie usunięty i będziesz w stanie go rozpoznać, gdy zaczniesz wprowadzać kod PIN - sekwencja słów będzie inna.


### Generowanie frazy odzyskiwania


Jest to jedna z najważniejszych części wallet - do generate klucz bezpiecznie. Aby zrobić to dobrze, używamy wielu źródeł entropii:



- TRNG mikrokontrolera. Zastrzeżony, certyfikowany i prawdopodobnie dobry, ale nie ufamy mu
- Ekran dotykowy. Za każdym razem, gdy dotkniesz ekranu, mierzymy pozycję i moment, w którym nastąpiło dotknięcie (w tikach mikrokontrolera z częstotliwością 180 MHz).
- Wbudowane mikrofony - jeszcze nie. Płyta ma dwa mikrofony, więc sprzętowy wallet może słuchać użytkownika i mieszać te dane z pulą entropii.


Cała ta entropia jest łączona i konwertowana na frazę odzyskiwania. Wynikowa entropia jest zawsze lepsza niż każde z poszczególnych źródeł.


### Logika wysokiego poziomu - portfele


Specter działa jako magazyn kluczy. Przechowuje klucze prywatne HD, które mogą być zaangażowane w portfele. Portfele są definiowane przez ich deskryptory. Obsługujemy również miniskrypty.


Każdy wallet należy do określonej sieci. Oznacza to, że jeśli zaimportowałeś wallet w `testnet`, nie będzie on dostępny w `mainnet` lub `regtest` - musisz przełączyć się do tej sieci i zaimportować wallet osobno.


### Weryfikacja transakcji


Poniższe zasady mają zastosowanie do transakcji podpisywanych przez wallet:



- jeśli znalezione zostaną mieszane dane wejściowe z różnych portfeli, użytkownik zostanie ostrzeżony ([attack](https://blog.trezor.io/details-of-the-multisig-change-address-issue-and-its-mitigation-6370ad73ed2a))
- wyjścia zmiany pokazują nazwę wallet, do którego są wysyłane
- aby użyć multisig lub miniscript, należy najpierw zaimportować wallet, dodając deskryptor wallet (przez QR, USB lub kartę SD)


## Obsługa deskryptorów


Wszystkie normalne deskryptory Bitcoin działają. Oprócz tego mamy kilka rozszerzeń:


### Wiele gałęzi w deskryptorach


Aby zaoszczędzić trochę miejsca w kodach QR, pozwalamy na dodawanie deskryptorów z wieloma gałęziami za jednym razem. Jeśli chcesz użyć `wpkh(xpub/0/*)` dla adresów odbiorczych i `wpkh(xpub/1/*)` dla adresów zmiany, możesz połączyć je w jednym deskryptorze: `wpkh(xpub/{0,1}/*)` - wallet potraktuje pierwszy indeks części zestawu `{}` jako gałąź dla adresów odbiorczych, a drugi jako adresy zmiany.


Można również określić więcej niż dwie gałęzie, a indeksy gałęzi mogą być różne dla różnych nadawców, więc ten deskryptor jest bardzo dziwny, ale całkowicie poprawny:


```
wsh(sortedmulti(2,xpubA/{22,33,44}/*,xpubB/34/*/{1,8,6},pubkey3))
```


Tutaj do odebrania adresu numer 17 wallet użyje skryptu z `wsh(sortedmulti(2,xpubA/22/17,xpubB/34/17/1,pubkey3))`.


Jedynym wymogiem jest to, aby liczba indeksów we wszystkich zestawach była taka sama (3 w powyższym przypadku).


### Domyślne pochodne


Jeśli deskryptor zawiera główne klucze publiczne, ale nie zawiera pochodnych symboli wieloznacznych, domyślna pochodna `/{0,1}/*` zostanie dodana do wszystkich kluczy rozszerzonych w deskryptorze. Jeśli co najmniej jeden z xpubs ma pochodną z symbolami wieloznacznymi, deskryptor nie zostanie zmieniony.


Deskryptor `wpkh(xpub)` zostanie przekonwertowany na `wpkh(xpub/{0,1}/*)`.


### Miniskrypt


Specter obsługuje miniskrypty, ale nie obsługuje kompilacji polityki do miniskryptów (ponieważ jest to zbyt kosztowne). Wykonujemy pewne kontrole na miniskrypcie, więc tylko skrypty `B` są dozwolone na najwyższym poziomie, a wszystkie argumenty w pod-miniskryptach muszą mieć właściwości zgodne z [spec](http://bitcoin.sipa.be/miniscript/).


Można użyć [bitcoin.sipa.be](http://bitcoin.sipa.be/miniscript/) do generate deskryptora z polityki, a następnie zaimportować go do wallet.


Na przykład polityka "mogę wydać teraz lub za 100 dni moja żona może wydać" może zostać przekonwertowana na wallet w następujący sposób:


Polityka: `or(9@pk(xpubA),and(older(14400),pk(B)))` (mój klucz jest 9 razy bardziej prawdopodobny)


Miniskrypt: `or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400)))`


Descriptor: `wsh(or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400))))`


Ponieważ nie mamy tutaj żadnych pochodnych symboli wieloznacznych, domyślne pochodne `/{0,1}/*` zostaną dołączone do xpubs.



---

Licencja MIT


Copyright (c) 2019 cryptoadvance


---