---
name: Konfiguracja BitAxe
description: Jak skonfigurować BitAxe?

---
![video](https://youtu.be/tvLSK8v0MK8)
### Wprowadzenie


BitAxe to projekt open-source stworzony przez Skota i [dostępny na GitHub](https://github.com/skot/bitaxe), który pozwala na opłacalne eksperymentowanie z Mining.


Udało się odtworzyć działanie słynnego Antminera S19 firmy Bitmain, lidera rynku układów ASIC, wyspecjalizowanych maszyn dla Bitcoin Mining. Teraz możliwe jest wykorzystanie tych potężnych chipów w nowych projektach open-source. W przeciwieństwie do Nerdminera, BitAxe ma wystarczającą moc obliczeniową do podłączenia do Mining pool, co pozwoli ci regularnie zarabiać trochę satoshi. Z drugiej strony, Nerdminer może być podłączony tylko do tak zwanego solopool, który działa jak los na loterii: masz niewielkie szanse na wygranie pełnego Block reward.


Istnieje kilka wersji BitAxe, z różnymi chipami i wydajnością:


| Bitaxe Model Series      | ASIC Chip | Used On                     | Expected Hash Rate          | Ideal For                                                                                                  |
| ------------------------ | --------- | --------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Bitaxe Max (Series 100)  | 1 x BM1397| Antminer Series 17          | 400 GH/s (up to 450 GH/s)   | Bitcoin mining beginners, offering a solid hash rate with moderate power consumption.                      |
| Bitaxe Ultra (Series 200)| 1 x BM1366| Antminer S19 XP and S19k Pro| 500 GH/s (up to 550 GH/s)   | Serious miners aiming to balance efficiency and higher hash rate.                                          |
| Bitaxe Hex (Series 300)  | 6 x BM1366| Antminer S19k Pro and S19 XP| 3.0 TH/s (up to 3.3 TH/s)   | Miners seeking scalability and high performance without sacrificing efficiency.                             |
| Bitaxe Supra (Series 400)| 1 x BM1368| Antminer S21                | 600 GH/s (up to 700 GH/s)   | Serious enthusiasts seeking the highest hash rates and efficiency.                                         |

W tym samouczku będziemy używać BitAxe Ultra 204 wyposażonego w układ BM1366, używany w Antminer S19XP. Ten jest już zmontowany i sflashowany przez sprzedawcę.


### [Lista sprzedawców jest dostępna na tej stronie](https://bitaxe.org/legit.html)


![signup](assets/2.webp)


Zazwyczaj zasilacz Supply jest sprzedawany razem z nim. Jeśli nie, należy zakupić zasilacz Supply z kablem jack 5 V i co najmniej 4 A.


![signup](assets/1.webp)


### Konfiguracja

Po pierwszym podłączeniu BitAxe domyślnie spróbuje połączyć się z siecią Wi-Fi. Po pięciu próbach wyświetli nazwę własnej sieci Wi-Fi, aby można było się z nią połączyć i ją skonfigurować.

Aby to zrobić, możesz użyć dowolnego komputera lub smartfona. Przejdź do ustawień Wi-Fi, wyszukaj nowe sieci, a zobaczysz Wi-Fi o nazwie Bitaxe_XXXX. Tutaj jest to `Bitaxe_A859`. Połącz się z tą siecią Wi-Fi, a okno otworzy się automatycznie.


![signup](assets/3.webp)


W tym oknie kliknij trzy małe poziome paski w lewym górnym rogu, a następnie `Ustawienia`.


![signup](assets/4.webp)


Konieczne będzie ręczne wprowadzenie informacji o sieci Wi-Fi, ponieważ nie ma automatycznego systemu wykrywania.


![signup](assets/5.webp)


Dlatego należy podać identyfikator SSID sieci Wi-Fi, czyli nazwę sieci, hasło, a także informacje o wybranym Mining pool. Uważaj, tutaj adres URL puli nie jest prezentowany w ten sam sposób. Na przykład dla Braiins podany adres URL puli to: `stratum+tcp://eu.stratum.braiins.com:3333`.


![signup](assets/6.webp)


Jak widać na ekranie, należy usunąć części `stratum+tcp://` i `:3333`, pozostawiając tylko `eu.stratum.braiins.com`. Następnie w polu `Port` należy wpisać 4 cyfry na końcu adresu URL podanego przez pulę, ale bez `:`. W tym przypadku jest to `3333`.


W tym samouczku używamy Braiins Mining pool, ale możesz wybrać inny. Nasze samouczki dotyczące basenów Mining można znaleźć [na stronie PlanB Network] (https://planb.network/en/tutorials/mining).


Następnie w `User` wprowadź swój identyfikator, a następnie `Password`, zazwyczaj jest to `"x"` lub `"Anything123"`.


Ustawienie `Core Voltage` powinno być domyślnie ustawione na `1200`, a w przypadku `Frequency` również początkowo należy pozostawić wartość domyślną. Później będzie można dostosować to ustawienie, aby uzyskać większą moc obliczeniową. Ważne jest jednak, aby upewnić się, że temperatura chipa nie przekracza 65-70°C, ponieważ BitAxe nie posiada systemu zmniejszającego wydajność w przypadku przegrzania. Jeśli temperatura przekroczy 65°C, może to spowodować uszkodzenie BitAxe.


![signup](assets/7.webp)


Po poprawnym wprowadzeniu wszystkich ustawień, kliknij przycisk `Zapisz` na dole, a następnie uruchom ponownie BitAxe, po prostu odłączając go i podłączając ponownie.

Jeśli informacje zostały wprowadzone poprawnie, urządzenie powinno szybko połączyć się z siecią Wi-Fi, a następnie z Mining pool i zacząć wyświetlać informacje na małym ekranie. Prawdopodobnie minie kilka minut, zanim pojawią się one na pulpicie nawigacyjnym Mining pool.

### Deska rozdzielcza i ekran


Przewijane będą trzy różne ekrany. Na trzeciej stronie zobaczysz informacje `IP`, czyli adres IP Address, który umożliwia połączenie z pulpitem nawigacyjnym. Tutaj Address to `192.168.1.19`.


![signup](assets/8.webp) ![signup](assets/9.webp) ![signup](assets/10.webp)


Aby uzyskać dostęp do pulpitu nawigacyjnego, wystarczy wpisać ten Address w przeglądarce internetowej.


Na pulpicie nawigacyjnym znajdują się wszystkie informacje wyświetlane na małym ekranie, którym teraz przyjrzymy się szczegółowo.


![signup](assets/11.webp)


| BitAxe Screen | Dashboard                                   | Description                                                                                                                                                                                                               |
| ------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gh            | Hashrate                                    | The current computing power, expressed in GigaHash/s                                                                                                                                                                      |
| W/THs         | Efficiency                                  | This is the efficiency of your BitAxe expressed in W/THs. It's the ratio between the electrical power consumed and the computing power produced.                                                                          |
| A/R           | Shares                                      | Quantity of `Shares` sent by your BitAxe to the pool, representing the amount of work provided.                                                                                                                          |
| UT            | Uptime                                      | Time since your BitAxe has been operating without interruption (available in the left menu under `Logs`).                                                                                                                |
| BD            | Best Difficulty                             | Maximum difficulty reached since the last restart. For comparison, the current network difficulty is about 85T.                                                                                                          |
| FAN           | FAN in the `Heat` box                       | Fan rotation speed, expressed in rotations per minute.                                                                                                                                                                    |
| Temp          | ASIC temperature in the `Heat` box          | Chip temperature, which should not exceed 65°C.                                                                                                                                                                           |
| Pwr           | Power                                       | Power in watts consumed. However, this information does not take into account the screen, the fan, or the power supply. For example, when it displays 11.7W, the total consumption is actually 15.8W.                    |
| mV mA         | Input Voltage Input Current                 | Voltage and current consumed by the machine. The power in watts is equal to the voltage multiplied by the current.                                                                                                        |
| FH            | Free Heap Memory (left menu -> `Logs`)      | The available memory.                                                                                                                                                                                                     |
| vCore         | ASIC Voltage (in the Performance box)       | Voltage measured on the ASIC chip.                                                                                                                                                                                        |
| IP            | NA                                          | IP Address.                                                                                                                                                                                                               |
| V2.1.0       | Version (left menu -> `Logs`)               | Firmware version.                                                                                                                                                                                                         |

Ustawienia Wi-Fi lub puli można zmienić w dowolnym momencie bez żadnych problemów.

W zależności od wentylacji i temperatury w pomieszczeniu, może być konieczne zwiększenie lub zmniejszenie wydajności, aby temperatura nie przekroczyła 65°C. Jeśli zwiększysz wydajność, zarobisz więcej satoshi, ale twój BitAxe będzie również zużywał więcej energii elektrycznej!
