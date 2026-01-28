---
name: SAFU Ninja
description: Zapisz seed za pomocą metody SAFU Ninja
---

![cover](assets/cover.webp)


## 1. Wprowadzenie



Metoda **Ninja SAFU** to **rozwiązanie DIY (Do It Yourself)**, które pozwala stworzyć **trwałą, bezpieczną i dyskretną** kopię zapasową **frazy seed** (12- lub 24-wyrazowej frazy Mnemonic zdefiniowanej przez standard **BIP-39**). Fraza ta jest niezbędna do przywrócenia Bitcoin Wallet lub innego kompatybilnego Wallet.



Zamiast zapisywać swoje słowa na papierze - co jest prostą, ale wrażliwą metodą - wygrawerujesz je na **podkładkach ze stali nierdzewnej**, zamontowanych na **Bolt**. Rezultatem jest kompaktowa, odporna na ogień, korozję, wodę i wstrząsy kopia zapasowa. W przeciwieństwie do papieru, który może zostać zniszczony przez płomienie, wilgoć lub czas, stal nierdzewna gwarantuje długotrwałą ochronę, nawet w ekstremalnych warunkach (do 1300°C lub 20 ton ciśnienia).



Podejście Ninja SAFU oferuje kilka korzyści:





- **Poufność**: Nie kupujesz produktu zidentyfikowanego jako przeznaczony do tworzenia kopii zapasowych kryptowalut. Komponenty są standardowe (podkładki, śruby, metalowe pudełko), dostępne w sklepach ze sprzętem, co zmniejsza ryzyko namierzenia w przypadku wycieku danych od wyspecjalizowanego dostawcy.





- **Przystępność**: To rozwiązanie kosztuje od **15 do 140 EUR**, w zależności od posiadanych już narzędzi.





- **Niezawodność**: Testowana od 2020 roku metoda została wypróbowana i przetestowana przez ekspertów ds. bezpieczeństwa, takich jak [Jameson Lopp](https://jlopp.github.io/metal-Bitcoin-storage-reviews/reviews/safu-ninja/), którzy poddali ją rygorystycznym testom obciążeniowym (ekstremalne ciepło, korozja, nacisk mechaniczny).



Ten przewodnik krok po kroku pokaże ci, jak wykonać własną kopię zapasową Ninja SAFU, aby lepiej chronić swoje bitcoiny przed utratą lub zniszczeniem. Jeśli chcesz dowiedzieć się więcej na temat tworzenia kopii zapasowych i ochrony frazy seed, zapoznaj się z załącznikami.




## 2. Sprzęt



Aby utworzyć kopię zapasową Ninja SAFU, potrzebne będą następujące komponenty, wszystkie dostępne w sklepach ze sprzętem lub online.



### 2.1 Wymagane materiały





- **Podkładki ze stali nierdzewnej (zalecane M8)**:
- **Materiał**: Stal nierdzewna (np. 304 lub V4A dla zwiększonej odporności na korozję)
- **Rozmiar**: M8 (średnica wewnętrzna 8 mm, średnica zewnętrzna ~24 mm). Podkładki M6 są zbyt małe i trudne do grawerowania.
- **Ilość**: 12 lub 24 podkładki dla standardowego zdania seed, plus opcjonalne podkładki (patrz sekcja 3.4) i dziesięć lub więcej dla testów lub błędów.





- **Bolt ze stali nierdzewnej i nakrętka (M8)**:
- **Specyfikacja**: Bolt o długości od 2,5 do 5 cm, w zależności od liczby i grubości podkładek, średnica 8 mm. Nakrętka motylkowa ułatwia otwieranie bez użycia narzędzi, ale można również użyć zwykłej nakrętki.



![image](assets/fr/03.webp)





- **Zestaw dziurkaczy do liter i cyfr (3 mm lub 6 mm)**:
- **Specyfikacja**: znaki o wysokości 6 mm ułatwiają czytelność i mogą być preferowane, jeśli część napisu uległa degradacji. Wybierz wytrzymały zestaw do wielokrotnego użytku.



![image](assets/fr/04.webp)





- **Młotek lub młot kowalski**:
    - Dla uzyskania wystarczającej i precyzyjnej siły tłoczenia preferowany jest młot kowalski





- **Kowadło lub wytrzymała powierzchnia**:
 - Gruba powierzchnia Hard (np. kowadło o wadze 1 kg lub kostka brukowa o grubości 10 cm) pochłaniająca wstrząsy.



Jeśli nie chcesz inwestować w zestaw stempli, możesz również wygrawerować podkładki za pomocą pióra grawerskiego. Rozwiązanie to jest często bardziej ekonomiczne, ale wymaga większej staranności, aby uzyskać zadowalający efekt.



### 2.2 Narzędzia opcjonalne





- **Urządzenie stemplujące**: Przytrzymuje podkładkę i prowadzi stempel, umożliwiając precyzyjne, czyste stemplowanie, lepszą orientację i równe odstępy między literami



![image](assets/fr/05.webp)





- **Urządzenia uszczelniające**: Szczelna torebka lub taśma uszczelniająca



![image](assets/fr/06.webp)





- **Hermetycznie zamknięty pojemnik**: Do przechowywania bloku podkładek



![image](assets/fr/07.webp)


### 2.3 Bezpieczeństwo





- Zalecane **rękawice** i **okulary ochronne**.
- Klucz do rur, w który należy wsunąć stempel, tak aby trzymać stempel kluczem do rur, a nie palcami.



### 2.4 Ilości i szacunkowy koszt





- **Ilość dla kopii zapasowej 24 słów**: 24 podkładki (minimum), 1 Bolt, 1 nakrętka motylkowa, 1 zestaw stempli, 1 młotek/maseta, 1 kowadełko/podpórka.





- **Całkowity koszt**:
 - Podkładki i śruby/nakrętki: ~ 15 EUR
 - Zestaw dziurkaczy: ~ 45 EUR
 - Etui ochronne: ~ 55 EUR
 - Ze wszystkimi akcesoriami: ~ 140 EUR





- Przykładowy sprzęt znajduje się w załączniku.




## 3. Instrukcje krok po kroku



1. **Przygotowanie:**




 - Prywatna lokalizacja, brak kamer (w tym smartfonów)
 - Wytrzymała, pochłaniająca wstrząsy powierzchnia
 - Rękawice i okulary ochronne
 - Oczyść spryskiwacze ze smaru i brudu
 - Ćwiczenia na podkładkach testowych


2. **Spal słowa Mnemonic** :




    - Wygraweruj całe słowo po jednej stronie. Nie ograniczaj się do pierwszych 4 liter, na wypadek gdyby czwarta została uszkodzona.
    - Uderz mocno młotkiem, przytrzymując stempel kluczem do rur


3. **Numer podkładki** :




    - Po tej samej stronie wygraweruj numer pozycji, niezbędny w przypadku poluzowania podkładek.


4. **Informacje o zapisie** (opcjonalne i zalecane) :




    - Wygraweruj zbędne słowo po drugiej stronie krążka
    - Wygrawerowanie identyfikatora Wallet na dodatkowej podkładce
    - Wygraweruj ścieżkę pochodną używanego konta na dodatkowej podkładce. Informacje te można znaleźć w ustawieniach oprogramowania portfela. Na przykład, dla standardowego portfela Taproot, domyślną ścieżką derywacji będzie: `m / 86' / 0' / 0' /`
    - Wpisz kod PIN, aby odblokować Hardware Wallet, lub słowa antyphishingowe, jeśli używasz karty COLDCARD.


5. **Nie spalaj passphrase :**




 - Jeśli używasz passphrase, upewnij się, że nie zapisujesz go na tej samej karcie co Mnemonic. passphrase służy do ochrony Wallet w przypadku kradzieży Mnemonic. Więcej informacji w załączniku.


6. **Sprawdź czytelność** :




    - Upewnij się, że każde słowo i liczba są wyraźne i czytelne.


7. **Montaż podkładek**:




    - Nakręć podkładki na Bolt w kolejności zgodnej z numerami.
    - Opcjonalnie: dodaj puste podkładki na końcach.
    - Przykręć nakrętkę motylkową, aby zabezpieczyć akumulator.
    - Mocno dokręcić, aby zwiększyć ochronę przed wodą, ogniem i naprężeniami mechanicznymi.


8. **Testowa kopia zapasowa** :




    - Z nowej kopii zapasowej spróbuj odzyskać swoje portfolio
- **Uszczelnienie kopii zapasowej** (opcjonalne i zalecane):
 - Poprzez zgrzewanie pasków lub w zapieczętowanych woreczkach.
 - Jeśli używasz woreczka, zanotuj jego unikalny numer identyfikacyjny, abyś mógł sprawdzić, czy jest to właściwy woreczek, a nie przynęta zastępująca oryginał.




## 4. Przechowywanie



### 4.1 Wybierz odpowiednią lokalizację



Przechowuj kopię zapasową w **dyskretnym miejscu**, poza zasięgiem wzroku i dostępnym do okresowych kontroli. Wybierz ognioodporne i wodoszczelne **miejsce przechowywania**, w domu lub w miejscu znajdującym się pod twoją **wyłączną kontrolą**.



Unikaj miejsc, w których jesteś zależny od strony trzeciej (sejf bankowy, notariusz): utracisz autonomiczny dostęp do swoich środków, co jest sprzeczne z zasadami suwerenności Bitcoin.



Nigdy nie ujawniaj, że używasz metody takiej jak Ninja SAFU. Dyskrecja jest sama w sobie Layer bezpieczeństwa.



### 4.2 Nadmiarowość



W razie potrzeby utwórz **kilka kopii** i przechowuj je w **różnych lokalizacjach geograficznych**.


Nawet jeśli materiały wybrane do produkcji urządzenia są odporne na wodę i ogień, nie będzie można uzyskać do niego dostępu, jeśli zostanie ono zakopane pod m3 gruzu w domu, a jego odzyskanie będzie bardzo trudne, jeśli nie niemożliwe.




## 5. Działania następcze i konserwacja



Nawet dobrze przechowywana kopia zapasowa musi być **regularnie sprawdzana**:





- Poza zasięgiem wzroku, sprawdzaj kopię zapasową **raz lub dwa razy w roku**.
- W przypadku **degradacji grawerunków**, odtwórz nową kopię zapasową, **przetestuj ją**, a następnie **ostrożnie zniszcz starą kopię**.
- Jeśli kopia zapasowa znajduje się w zapieczętowanym woreczku:
 - Sprawdź swój login
 - Sprawdź jego integralność
 - Regularnie otwieraj kopertę, aby sprawdzić stan rycin, a jeśli wszystko jest w porządku, umieść kopię zapasową w nowej kieszeni




**STAY SAFU!**


![image](assets/fr/08.webp)




## DODATKI



### A.1 Zapisz frazę odzyskiwania



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### A.2 Zrozumienie passphrase BIP39



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

### A.3 Jak działają portfele Bitcoin



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f


### A.4 Klasyfikacja metody Ninja SAFU



Według Jamesona Loppa:





- [Raport](https://jlopp.github.io/metal-Bitcoin-storage-reviews/reviews/safu-ninja/) na temat metody Ninja SAFU





- Tabela porównawcza [pełna](https://jlopp.github.io/metal-Bitcoin-storage-reviews/?ref=blog.lopp.net)





- Tabela częściowa :


![image](assets/fr/09.webp)



### A.5 Przykład sprzętu





- **Podkładki** dla
 - [Titan](https://pleb.style/fr-fr/products/disques-de-seed-supplementaires-titan-Wallet)
- **Podkładki + nakrętka + etui ochronne** (dla podkładek)
 - [Titan](https://pleb.style/fr-fr/products/titan-Wallet-premium-acier-steel-Wallet-backup?variant=50022696419664)
 - [TerraSteel](https://pleb.style/fr-fr/products/terrasteel-Wallet-plebstyle-acier-backup)
- Zestaw dziurkaczy
 - [PlebStyle](https://pleb.style/fr/products/schlagstempelset-a-z-0-9-3mm)
- **Podstawa typowania**
 - [PlebStyle](https://pleb.style/fr/products/schlagunterlage-10cm-x-10cm-x-1-5cm)
- **Urządzenie do gwintowania** (prowadnica)
 - [TerraSteel](https://pleb.style/fr-fr/products/zubehor-einschlag-vorrichtung?_pos=1&_sid=2767fd66f&_ss=r)
- Urządzenie uszczelniające
 - [Zapieczętowany woreczek](https://pleb.style/fr/products/zubehor-5x-sicherheitstasche-tamper-evident)
 - [Paski uszczelniające](https://pleb.style/fr/products/zubehor-5x-siegel-streifen-fur-dein-seed-backup)
- **Kompletny** zestaw
 - [Titan](https://pleb.style/fr-fr/products/titan-Wallet-diy-kit-premium-seed-backup-steelwallet-plebstyle?pr_prod_strat=e5_desc&pr_rec_id=aa9f36359&pr_rec_pid=8728733155664&pr_ref_pid=8730877788496&pr_seq=uniform)
 - [TerraSteel](https://pleb.style/fr-fr/products/kopie-von-terrasteel-Wallet-starter-kit)



Uwaga: Linki do sklepów internetowych podano wyłącznie w celach informacyjnych.


Pomiędzy Plan B a wyżej wymienionymi sprzedawcami i producentami nie istnieje żadne partnerstwo handlowe.


Plan B nie ponosi odpowiedzialności za wady, różnice cenowe lub problemy związane z jakością lub dostawą produktów. **DYOR**




### A.6 Kredyty fotograficzne



https://pleb.style/fr/


https://x.com/lopp/status/1463155802345193475


https://bitcointalk.org/index.php?topic=5389446.0


https://x.com/econoalchemist/status/1329271981712289797


https://www.waivio.com/@themarkymark/create-your-own-metal-seed-key-backup


https://github.com/minibolt-guide/minibolt/blob/main/bonus/Bitcoin/safu-ninja.md