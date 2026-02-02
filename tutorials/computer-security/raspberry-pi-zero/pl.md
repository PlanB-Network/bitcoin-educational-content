---
name: Raspberry Pi Zero
description: Jak zbudować minimalny, odizolowany i tani komputer, używając Raspberry Pi Zero i zestawu akcesoriów.
---
![cover](assets/cover.webp)



Jeśli jesteś na stronach Plan ₿ Academy od dłuższego czasu, już wiesz, że jednym z najbardziej zalecanych ustawień bezpieczeństwa, niemal obowiązkowym, **jest zarządzanie funduszami poprzez przechowywanie kluczy prywatnych w trybie offline**.



Jeśli jeszcze go nie odkryłeś, w tym samouczku znajdziesz linki do zasobów open source, z których możesz dowiedzieć się więcej na jego temat.



Do zarządzania kluczami prywatnymi offline potrzebne jest zatem urządzenie trwale odłączone od sieci, niezależnie od tego, czy jest to [portfel sprzętowy](https://planb.academy/resources/glossary/hardware-wallet), czy komputer z airgapem, przeznaczony do tej konkretnej funkcji.



Jak to zrobić, jeśli na przykład nie masz możliwości zakupu sprzętu, który wykonuje tylko to zadanie, ale nie chcesz rezygnować z tego kroku bezpieczeństwa?



## Rozwiązanie


A gdybym ci powiedział, że możesz stworzyć urządzenie offline w postaci komputera airgap, który ma rozmiar i wagę pamięci flash USB i kosztuje 35 euro? Nie uwierzyłbyś w to?



Czytaj dalej.



Powiem ci więcej: przeczytaj do końca. Proponowane rozwiązanie jest tanie, ale nie należy do najłatwiejszych. Najpierw zapoznaj się z ogólną ideą, a następnie zdecyduj się zainwestować trochę czasu w osobiste badania i wybierz, z możliwie największym spokojem, czy i jak postępować.



## Wymagania


**1** [Raspberry PI Zero](https://www.raspberrypi.com/products/raspberry-pi-zero/): PI Zero (bez żadnego sufiksu) jest podstawą do stworzenia komputera o minimalnej wydajności, ale przede wszystkim pozbawiony jest kart Wi-Fi i Bluetooth, które są niezbędne do celu tego ćwiczenia.





- **Koszt**: około 15,00 w momencie pisania tego poradnika (sierpień 2025).
- **Ciągłość produkcji**: Raspberry gwarantuje produkcję do stycznia 2030 roku.



PI Zero bez Wi-Fi i Bluetooth stały się niestety praktycznie niedostępne. Możesz być w stanie łatwiej znaleźć alternatywy PI Zero W i PI Zero 2W. W takim przypadku można wyłączyć funkcje połączenia, zmieniając plik konfiguracyjny. Po zainstalowaniu systemu operacyjnego należy dodać te elementy do konfiguracji:



```
dtoverlay=disable-wifi
dtoverlay=disable-bt
```



sekcja tego przewodnika pokaże ci, jak i gdzie to zrobić. Jeśli jednak naprawdę chcesz mieć pewność, możesz znaleźć w Internecie kilka samouczków dotyczących usuwania układu Wi-Fi za pomocą małego noża, odpowiedniego do pracy na płytkach elektronicznych.



**2** Zestaw _starter kit_ dla Raspberry PI Zero: jak to jest praktykowane w świecie Raspberry, gołe kości, bez zewnętrznej obudowy. Ponadto ograniczone zasoby tak małej płytki warunkują możliwości połączenia ze światem zewnętrznym.



Kiedy zdecydowałem się kontynuować, znalazłem [ten zestaw](https://www.amazon.it/-/en/GeeekPi-Raspberry-Aluminum-Passive-Heatsink/dp/B0BJ1WWHGF?crid=1NAFFVHG3IFBU&sprefix=raspberry+pi+zero+kit+geeek+pi%2Caps%2C88&sr=8-65) pełen akcesoriów, aby w pełni wykorzystać potencjał PI Zero. W rzeczywistości zestaw zawiera zasilacz USB A -> micro USB Supply, mały hub USB, adapter mini-HDMI -> HDMI, miedziany radiator i aluminiową obudowę zewnętrzną. W zestawie znajdują się również śruby i klucz imbusowy potrzebne do umieszczenia PI Zero w nowej obudowie.





- **Koszt**: 19.99 euro.



**3** Ten samouczek nie wymaga wydawania dużych pieniędzy na komputer airgap. Powinieneś jednak wiedzieć, że będziesz potrzebować klawiatury i myszy USB (wyłącznie przewodowej, unikaj Bluetooth) oraz monitora. W zależności od wejścia monitora, może być potrzebna przejściówka z mini-HDMI, jedynego wyjścia dostępnego w PI Zero. Wreszcie, spójrz Hard na fakt, że wszyscy mamy gdzieś w domu nie-przewodową klawiaturę i mysz - nadszedł czas, aby je Dust.



## Dodatkowy budżet



**4** Oryginalny zasilacz Supply można kupić w Raspberry, kosztuje około 15,00 euro.



**5** Osobiście zdecydowałem się na użycie Supply dostarczonego w zestawie startowym, łącząc go jednak z kablem USBA → miniUSB, tak zwanym `no data`, kosztującym 3,70 euro.



**6** Karta micro SD o minimalnej pojemności co najmniej 32 GB; jeśli jakość/poziom przemysłowy jest lepszy.



**7** Będziesz potrzebował systemu, adaptera USB do micro SD, takiego jak ten, który widzisz na zdjęciu. System operacyjny i pamięć PI Zero będą działać na tym nośniku.



![img](assets/it/06.webp)



## Instalacja systemu operacyjnego


Przed zamknięciem PI Zero w obudowie zalecam zainstalowanie systemu operacyjnego. Będziesz wtedy mógł od razu sprawdzić diodę LED wskazującą działanie.



Aby wybrać i wypalić system operacyjny, wybrałem najprostszy sposób: użycie narzędzia `PI Imager` Raspberry.



![img](assets/it/01.webp)



Przejdź więc do [Githuba Raspberry](https://github.com/raspberrypi/rpi-imager/releases), aby pobrać najnowsze wydanie Imagera, wybierając to najbardziej odpowiednie dla twojego systemu operacyjnego (v. 1.9.6 w momencie pisania). Zauważysz, że obok każdego zasobu znajduje się również hash odpowiadającego mu pliku. Przyda się nam to do weryfikacji.



![img](assets/it/02.webp)



Zalecam zweryfikowanie systemu operacyjnego, który będzie używany na komputerze airgap, dla własnego spokoju ducha. Da ci to pewność, że pracujesz z legalną (nie złośliwą) wersją Imagera, a co za tym idzie, Raspi OS.



Wykonaj weryfikację natychmiast po pobraniu, na komputerze, którego zwykle używasz, podłączonym do Internetu



Następnie otwórz terminal Linux i przygotuj pobrany plik, tworząc katalog `raspios` przydatny do pracy z nim.



![img](assets/it/19.webp)



Pobierz Imager dla swojej dystrybucji Linuksa za pomocą `wget`.



![img](assets/it/20.webp)



Na koniec uruchom polecenie `sha256sum` i porównaj Hash z tym dostarczonym przez Raspberry na Githubie.



![img](assets/it/21.webp)



Lub, jeśli masz system Windows, otwórz Power Shell i wpisz następujące polecenie:



```
Get-FileHash -Path <yourpath>\imager-1.9.6.exe
```



![img](assets/it/04.webp)



Otrzymasz Hash, który musi być zgodny z tym opublikowanym na Raspberry Github.



Po zweryfikowaniu pobierania, możesz zainstalować Imager na swoim codziennym komputerze i otworzyć go. Imager to narzędzie potrzebne do nagrania systemu operacyjnego na kartę micro SD, która będzie "dyskiem systemowym" PI Zero.



Proces jest niezwykle prosty: najpierw wybierz urządzenie Raspberry, którego zamierzasz używać (więc zwróć uwagę na **twój model** Raspi Zero), następnie wersję systemu operacyjnego, a na końcu punkt montowania karty micro SD, na którą chcesz sflashować system operacyjny.



### Pierwszy krok



![img](assets/it/03.webp)



### Drugi krok



![img](assets/it/07.webp)



**Uwaga**: wybierz `PI OS 32-bit`, jedyny, który działa z PI Zero.



### Trzeci krok



![img](assets/it/08.webp)



(Należy bardzo uważać, aby pozostawić zaznaczoną opcję _Exclude System Drive_, aby uniknąć wyświetlenia monitu o zainstalowanie systemu operacyjnego Raspi na komputerze)



Gdy wszystko zostanie skonfigurowane, wywoływarka zapyta, czy chcesz użyć ustawień niestandardowych. Wybierz to, co chcesz, lub kliknij _No_, aby kontynuować z domyślnymi opcjami.



![img](assets/it/09.webp)



Potwierdź, że chcesz usunąć zawartość karty micro SD



![img](assets/it/10.webp)



Imager rozpocznie flashowanie systemu operacyjnego do micro SD, pasek przewijania poinformuje o postępie.



![img](assets/it/11.webp)



Na końcu następuje automatyczna weryfikacja, radzę jej nie przerywać.



![img](assets/it/12.webp)



W końcu na ekranie pojawi się komunikat, a jeśli wszystko się powiodło, wygląda tak, jak na obrazku.



![img](assets/it/13.webp)



Możesz teraz naprawdę wyjąć kartę micro SD z czytnika i umieścić ją w gnieździe PI Zero. Włącz małego Raspberry i obserwuj diodę LED: spodziewamy się, że będzie zielona i migająca, co wskazuje na normalne ładowanie systemu operacyjnego, a następnie pozostanie włączona na stałe. Jeśli masz inne wskazania, na przykład jeśli dioda LED miga w regularnych odstępach lub jest czerwona, sprawdź FAQ lub [strony forum wsparcia](https://forums.raspberrypi.com/).



## Pierwsza konfiguracja


Pierwsze uruchomienie systemu Raspi OS jest nieco wolniejsze niż zwykle, ponieważ musi on wykonać szereg rzeczywistych zadań instalacyjnych. Ale jeśli wszystko poszło dobrze, pojawi się ekran powitalny.



![img](assets/it/14.webp)



Kliknij przycisk _Next_, aby ustawić region geograficzny, zwłaszcza w celu załadowania prawidłowej klawiatury. Zwróć szczególną uwagę na to ostatnie.



![img](assets/it/15.webp)



Kliknij _Next_, a zostaniesz poproszony o utworzenie użytkownika, zanotowanie danych uwierzytelniających i zachowanie ich.



![img](assets/it/16.webp)



Kreator poprosi o wybranie domyślnej przeglądarki internetowej, między Chromium a Firefox; może również zapytać o ustawienia sieci Wi-Fi, jeśli pracujesz z Zero W lub 2W PI. Kliknij przycisk _Skip_.



W pewnym momencie zostaniesz poproszony o aktualizację oprogramowania pokładowego i systemu operacyjnego. Wybierz _Skip_: dla celów tego ćwiczenia budujemy maszynę offline, która musi pozostać offline od tego czasu.



Na koniec może poprosić o włączenie `ssh`, ale odrzuć również ten krok, ponieważ jest to adres IP z zerową szczeliną powietrzną.



![img](assets/it/17.webp)



Nie ma wiele więcej do skonfigurowania. Po zakończeniu uruchom ponownie Raspberry, aby zmiany zaczęły obowiązywać.



![img](assets/it/18.webp)



## Nowy komputerowy Airgap


Po ponownym uruchomieniu nowy komputer airgap jest gotowy. PI Zero wyświetla nowy pulpit, z którym można pracować za pomocą GUI lub z wiersza poleceń.



![img](assets/it/22.webp)



### Pierwsze kroki dla PI Zero W lub 2W


Jeśli pracujesz z Raspberry PI Zero z serii W lub 2W, na Twojej płytce znajdują się chipy Wi-Fi i Bluetooth. Podczas pierwszej konfiguracji pominięto konfigurację połączenia, więc PI Zero nie jest podłączony do Internetu. Teraz możesz wyłączyć te dwa chipy na stałe za pomocą oprogramowania.



W rzeczywistości Raspi OS udostępnia plik `config.txt`, który można edytować według własnych upodobań. Plik `config` znajduje się na partycji `boot`, w katalogu `firmware` i można go edytować i zapisywać z uprawnieniami `root`.



Otwórz terminal z ikony w lewym górnym rogu, a stanie się on `root`.(1)



![img](assets/it/23.webp)



(1) Jeśli Raspi OS nie kazał ci utworzyć hasła `root` podczas poprzednich kroków, zalecam zrobienie tego teraz, za pomocą polecenia `passwd`. Posiadanie użytkownika `root` poruszającego się niezależnie od użytkownika osobistego może okazać się bardzo wygodne w sytuacjach odzyskiwania.



W terminalu sprawdź plik `config.txt` i przygotuj się do jego edycji za pomocą edytora `nano`.



![img](assets/it/24.webp)



Edycja powinna być wykonana na dole całego `config`, po słowach `[All]`. To właśnie w tym momencie dodasz polecenia `dtoverlay` pokazane na początku samouczka.



![img](assets/it/25.webp)



Zapisz, zamknij i uruchom ponownie. W kolejnym kroku przejdziemy do eksploracji małego Raspberry.



## Czego można oczekiwać od tego urządzenia?


Patrząc na [specyfikacje techniczne](https://www.raspberrypi.com/products/raspberry-pi-zero/) ze strony Raspberry, PI Zero posiada jednordzeniowy procesor BCM2835 oraz 512 MB RAM, więc nie zapowiada się na szczególnie wydajny.



Ponieważ terminal jest lżejszy, użyjemy wiersza poleceń do zbadania konfiguracji systemu.



Po włączeniu zobaczysz krótki ekran w kolorze tęczy, a następnie wiadomość powitalną od Raspberry, a w lewym dolnym rogu komunikaty jądra związane z uruchamianiem.



Gdy pojawi się pulpit PI OS, otwórz terminal i wpisz:



```bash
uname -a
```


To polecenie wyświetli na ekranie aktualnie używaną wersję jądra oraz inne informacje.



![img](assets/it/26.webp)



Można również wyświetlić informacje o procesorze i sprzęcie, wpisując:



```bash
lscpu
```



![img](assets/it/27.webp)



Zobacz także `proc/mem/info`.



![img](assets/it/28.webp)



Aby sprawdzić wersję Debiana i nazwę kodową wydania:



`` bash


lsb_release -a


```

![img](assets/it/29.webp)

Infine, due comandi per controllare la memoria di massa e i dischi:

``` bash
fdisk -l
```



![img](assets/it/31.webp)



`` bash


df


```
![img](assets/it/30.webp)

Per controllare come lavora la CPU:

``` bash
top
```



![img](assets/it/32.webp)



## Użycie


Chociaż wydajność wydaje się ograniczona (na papierze i w porównaniu do mocy dzisiejszych maszyn), PI Zero jest wydajny, zwłaszcza jako terminal.





- Najpierw możesz przejść do menu głównego i zainspirować się panelem _Dodaj/Usuń oprogramowanie_, gdzie znajdziesz szereg narzędzi do programowania i ćwiczeń. Pamiętaj, że możesz to również zrobić z terminala, ale zawsze z uprawnieniami `root`.



![img](assets/it/33.webp)





- Możesz "zaadoptować" to urządzenie offline do przechowywania różnych poufnych dokumentów, które pozostaną dostępne w razie potrzeby, bez narażania ich na kontakt z Internetem.
- Można użyć tej konfiguracji do bezpiecznego generate kluczy GPG.
- Mógłbyś nawet wykorzystać ten nowy „gadżet” jako urządzenie do podpisu airgap, [postępując zgodnie z radami Arman The Parman](https://armantheparman.medium.com/how-to-set-up-a-raspberry-pi-zero-air-gapped-running-latest-version-of-electrum-desktop-wallet-85e59ecaddc0).



Spośród portfeli, które znam, jedynym, który zapewnia wersję 32-bitową, jest Electrum. Cóż: Zero IP, tak jak przygotowaliśmy go w tym samouczku, pozwoli ci zachować klucze prywatne offline w konfiguracji Wallet airgap, którą omówiliśmy w tym samouczku:



https://planb.academy/tutorials/wallet/desktop/electrum-airgap-62b5a4c6-a221-4d41-9a62-4618c53d8223

## Wnioski


Konfiguracja ma prawdopodobnie jedną dużą słabość: micro SD jest nośnikiem, który może powodować problemy. Jest podatny na intensywne użytkowanie; być może masz już doświadczenie w tym zakresie, używając go z telefonem. Po zainstalowaniu całego oprogramowania, którego będziesz chciał używać na Zero airgap IP, zrób dobrą kopię zapasową cennej karty micro SD, używając dostępnego narzędzia Raspi OS.



![img](assets/it/34.webp)



Wraz z rosnącymi potrzebami, a wraz z nimi możliwościami budżetowymi, można eksplorować inne Raspberry lub podobne rozwiązania. Mówiąc na przykład o pamięci, PI 5 oferuje możliwość montażu dysku M2 NVME, który jest z pewnością bardziej wytrzymały niż microSD.



Nie zapomnij robić notatek i dokumentować każdego kroku instalacji oprogramowania narzędziowego, którego zamierzasz używać w trybie offline. **Prędzej czy później pojawi się zaktualizowany system operacyjny Raspi**, z którego na pewno będziesz chciał skorzystać. W tym momencie będziesz musiał usunąć wszystko i zrobić to od nowa (być może z nową kartą micro SD 😂).



Ćwiczenie, które właśnie wykonaliśmy, zakładając, że jest to również twój pierwszy eksperyment, zapamiętasz na długo. Nie zawsze jest możliwe poświęcenie sprzętu na operacje `embedded` w trybie offline, nie zaniedbując przy tym dbałości o maszynę airgapped, którą można od czasu do czasu włączyć i sprawdzić.



Ale udało się, gratulacje! I będziesz mógł zasugerować to rozwiązanie wszystkim, którzy muszą ograniczyć swój budżet.