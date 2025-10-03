---
name: Nerdminer
description: Start Mining Bitcoin z szansą na wygraną bliską 0
---

![cover](assets/cover.webp)

## Konfiguracja twojego NerdMiner v2


W tym samouczku przeprowadzimy Cię przez niezbędne kroki, aby skonfigurować NerdMiner_v2, który jest urządzeniem sprzętowym (ESP-32 S3) dedykowanym Bitcoin Mining.

Oczywiście moc obliczeniowa takiego urządzenia nie może konkurować z układami ASIC amatorskich lub profesjonalnych górników. Niemniej jednak, NerdMiner jest doskonałym narzędziem edukacyjnym, dzięki któremu Bitcoin Mining staje się namacalne. I kto wie, przy (dużym) szczęściu, być może znajdziesz blok i nagrodę, która się z nim wiąże. Dla ciekawskich, zobaczymy to w sekcji [Oszacowanie prawdopodobieństwa wygranej](#estimation-de-la-probabilite-de-gain). Jeśli chodzi o zużycie energii, NerdMiner zużywa 0,5 W; dla porównania, lampa LED zużywa średnio 20 razy więcej.


Zanim przejdziemy do poszczególnych kroków, wymieńmy niezbędny sprzęt do jego wykonania:



- a [Lilygo T-display S3](https://lilygo.cc/products/t-display-s3)
- a [USB-C power Supply](https://amzn.eu/d/gIOot90)
- etui 3D: jeśli masz drukarkę 3D, możesz pobrać [plik 3D] (https://www.printables.com/model/501547-nerdminer-v2-click-case-w-buttons), w przeciwnym razie możesz go kupić w [sklepie internetowym Silexperience] (https://silexperience.company.site/NerdMiner_V2-p544379757).
- komputer PC z zainstalowaną przeglądarką Chrome
- połączenie internetowe
- a Bitcoin Address


Możesz również kupić wstępnie zmontowany zestaw NerdMiner od kilku sprzedawców, takich jak:



- [DécouvreBitcoin](https://shop.decouvrebitcoin.com/products/nerd-Miner?_pos=1&_psq=nerd&_ss=e&_v=1.0)
- [BitMaker](https://bitronics.store/shop/)


Najpierw zobaczymy, jak sflashować oprogramowanie na ESP-32 S3, a następnie zobaczymy, jak go zrestartować, aby zmienić sieć Wi-Fi. Te kroki są przeznaczone dla użytkowników systemu Windows, jeśli używasz systemu operacyjnego Linux, wykonaj [kroki wstępne] (#etapes-preliminaires-pour-utilisateurs-linux), aby umożliwić rozpoznanie ESP-32 S3 przez system.


**Instalacja oprogramowania NerdMiner_v2** jest znacznie uproszczona dzięki zastosowaniu webflashera.


## Krok 1: Przygotowanie aplikacji Webflasher


Najpierw należy przejść do strony [online NM2 flasher] (https://bitmaker-hub.github.io/diyflasher/).


Następnie wybierz oprogramowanie sprzętowe odpowiadające ESP-32. W większości przypadków jest to oprogramowanie domyślne: T-Display S3. Następnie kliknij "Flash".


**Note⚠️ :** ważne jest, aby korzystać z przeglądarki Chrome - ponieważ domyślnie umożliwia ona korzystanie z pamięci flash i dostęp do portów USB.


![image](assets/webflasher.webp)


## Krok 2: Podłączanie ESP-32


Po uruchomieniu webflashera otworzy się wyskakujące okienko pokazujące różne porty USB rozpoznawane przez przeglądarkę.

Następnie można podłączyć ESP-32 i zostanie wyświetlony nowy port (w tym przypadku jest to port ttyACM0). Następnie należy go wybrać i kliknąć "Połącz".


![image](assets/flasher-port-serial.webp)


Oprogramowanie zostanie następnie pobrane na ESP32 w ciągu kilku sekund.


![image](assets/NM2-sucessfully-installed.webp)


## Krok 3: Konfiguracja NerdMiner


Konfiguracja NerdMiner odbywa się za pośrednictwem smartfona lub komputera.

Włącz WiFi i połącz się z lokalną siecią NerdMinerAP. Jeśli korzystasz ze smartfona, portal konfiguracyjny otworzy się automatycznie. W przeciwnym razie wpisz Address 192.168.4.1 w przeglądarce.

Następnie wybierz "Konfiguruj WiFi".


Możesz teraz skonfigurować NerdMiner.

Najpierw zacznij od połączenia się z siecią Wi-Fi, wybierając nazwę sieci i wprowadzając powiązane hasło.


Następnie możesz wybrać Mining pool, w którym chcesz uczestniczyć. Rzeczywiście, w branży Bitcoin Mining powszechne jest łączenie mocy obliczeniowej w celu zwiększenia szans na znalezienie bloku w Exchange w celu podzielenia się nagrodą proporcjonalnie do dostarczonego Hashrate.

W przypadku NerdMiners można wybrać połączenie z jedną z tych pul:


| Pool URL          | Port  | URL                        | Status                                   |
| ----------------- | ----- | -------------------------- | ---------------------------------------- |
| public-pool.io    | 21496 | https://web.public-pool.io | Default Solo and open-source mining pool |
| pool.nerdminer.io | 3333  | https://nerdminer.io       | Maintained by CHMEX                      |
| pool.vkbit.com    | 3333  | https://vkbit.com/         | Maintained by djerfy                     |

Po wybraniu puli należy wprowadzić Bitcoin Address, aby otrzymać nagrodę w przypadku (wyjątkowo) znalezienia bloku.


Wybierz również swoją strefę czasową, aby NerdMiner mógł poprawnie wyświetlać czas.

Możesz teraz kliknąć przycisk "Zapisz".


![image](assets/wifi-configuration.webp)


Gratulacje, jesteś teraz częścią sieci Bitcoin Mining!


## Działanie NerdMiner


Oprogramowanie NerdMinerv2 ma 3 różne ekrany, do których można uzyskać dostęp, klikając górny przycisk po prawej stronie ekranu:



- Ekran główny zapewnia dostęp do statystyk NerdMiner.
- Drugi ekran zapewnia dostęp do czasu, Hashrate, ceny Bitcoin i wysokości bloku.
- Trzeci ekran zapewnia dostęp do statystyk dotyczących globalnej sieci Bitcoin Mining.

![image](assets/NM2-screens.webp)


Jeśli chcesz zrestartować NerdMiner, na przykład w celu zmiany sieci WiFi, musisz nacisnąć górny przycisk przez 5 sekund.


Jednokrotne naciśnięcie dolnego przycisku spowoduje wyłączenie NerdMiner. Dwukrotne kliknięcie spowoduje obrócenie orientacji ekranu.


### Kroki wstępne dla użytkowników systemu Linux


Oto kroki dla Chrome, aby wykryć port szeregowy w systemie Linux.


1. Identyfikacja powiązanego portu:



- Podłącz ESP-32 do komputera.
- Otwórz terminal.
- Wprowadź następujące polecenie, aby wyświetlić listę wszystkich portów:
  - `dmesg | grep tty`
  - lub `ls /dev/tty*`
- Aby upewnić się co do portu, można przeprowadzić eliminację, powtarzając polecenie bez podłączonego ESP-32.


2. Zmiana uprawnień powiązanego portu:



- Domyślnie dostęp do portów szeregowych może wymagać uprawnień roota, więc udostępnimy je dodając użytkownika do grupy `dialout`.
  - `sudo usermod -a -G dialout YOUR_USERNAME`, zastąp `YOUR_USERNAME` swoją nazwą użytkownika.
  - następnie wyloguj się i zaloguj ponownie jako ten użytkownik lub uruchom ponownie system, aby upewnić się, że zmiany grupy zostaną wprowadzone.


Teraz, gdy ESP-32 jest rozpoznawany przez system, można wrócić do [pierwszego kroku] (#etape-1-preparation-du-webflasher) w celu instalacji oprogramowania.


## Wnioski


I gotowe! Twój NerdMiner_v2 jest teraz skonfigurowany i gotowy do użycia.


Szczęśliwego Mining i niech szczęście będzie po twojej stronie!


### Szacowanie prawdopodobieństwa wygranej


Zabawmy się w szacowanie prawdopodobieństwa wygrania Block reward. Oszacowanie to będzie zgrubne i ma na celu jedynie uzyskanie rzędu wielkości prawdopodobieństwa.

Pula, do której może podłączyć się NerdMiner, to tylko "solo Mining pool", co oznacza, że pula nie dzieli Hashrate wszystkich podłączonych górników, ale po prostu działa jako koordynator.

Załóżmy teraz, że nasz NerdMiner ma Hashrate około 45kH/s.


Wiedząc, że całkowity Hashrate wynosi około 450 EH/s (lub 4,5 x 10^20 hashy na sekundę), możemy uznać, że prawdopodobieństwo znalezienia następnego bloku wynosi 1 na 100 milionów miliardów, co jest bardzo bardzo mało prawdopodobne. Tak więc oprócz bycia narzędziem edukacyjnym i obiektem ciekawości, NerdMiner może służyć jako los na loterię w Bitcoin Mining przy marginalnym koszcie elektrycznym 0,5 W - chociaż, jak właśnie widzieliśmy, prawdopodobieństwo wygranej jest śmiesznie niskie. Dlaczego jednak nie spróbować szczęścia?


### Dodatkowe informacje


Oto kilka linków, jeśli chcesz dowiedzieć się więcej na ten temat:



- [Strona projektu NerdMiner_v2](http://github.com/BitMaker-hub/NerdMiner_v2)
- [Pełna dokumentacja NerdMiners](https://docs.bitwater.ch/nerd-Miner-v2/)