---
name: Tails

description: Zainstaluj Tails na kluczu USB
---

![image](assets/cover.webp)


Przenośny i amnezyjny system operacyjny, który chroni przed inwigilacją i cenzurą.


## Po co mieć klucz USB z zainstalowanym Tails?


Tails (https://tails.boum.org/) to najprostszy sposób na posiadanie bezpiecznego komputera, który nie pozostawia żadnych śladów na komputerze, z którym jest używany.


Aby korzystać z Tails, wyłącz komputer, do którego masz dostęp (u rodziców, u znajomych, w kafejce internetowej...) i uruchom go za pomocą klucza USB Tails zamiast systemu Windows, macOS lub Linux.


W ten sposób uzyskasz przestrzeń roboczą i środowisko komunikacyjne, które jest niezależne od zwykłego systemu operacyjnego i nigdy nie korzysta z dysku Hard.


Tails nigdy nie zapisuje danych na dysku Hard i do działania wykorzystuje jedynie pamięć RAM komputera. Pamięć ta jest całkowicie wymazywana po wyłączeniu Tails, usuwając w ten sposób wszelkie możliwe ślady.


## Kilka konkretnych przypadków użycia


Aby dać ci konkretne wyobrażenie o korzyściach płynących z posiadania klucza USB z Tails, oto mała, niewyczerpująca lista opracowana przez zespół Agora256:



- Połącz się z Internetem i Tor w nieocenzurowany i anonimowy sposób, aby przeglądać strony internetowe bez pozostawiania śladów;
- Otwórz plik PDF z podejrzanej witryny;
- Przetestuj kopię zapasową klucza prywatnego Bitcoin za pomocą Electrum Wallet;
- Korzystaj z pakietu biurowego (LibreOffice) i pracuj na komputerze, który nie należy do Ciebie;
- Postaw swoje pierwsze kroki w środowisku Linux, aby dowiedzieć się, jak opuścić świat Microsoft i Apple.


## Jak zaufać Tailsowi?


Korzystanie z oprogramowania zawsze wiąże się z zaufaniem, ale nie musi być ono ślepe. Narzędzie takie jak Tails musi dążyć do zapewnienia swoim użytkownikom środków do bycia godnym zaufania. Dla Tails oznacza to:



- Publiczny kod źródłowy: https://gitlab.tails.boum.org/;
- Projekt oparty na renomowanych projektach: Tor i Debian;
- Weryfikowalne i powtarzalne pliki do pobrania;
- Rekomendacje różnych osób i organizacji.


## Instrukcja instalacji i użytkowania


Celem niniejszego przewodnika instalacji jest przeprowadzenie użytkownika przez każdy etap instalacji. Nie będziemy opisywać działań, które należy podjąć bardziej niż oficjalny przewodnik, ale wskażemy ci właściwy kierunek, dając ci wskazówki i triki.


Ze względów praktycznych porady te będą koncentrować się na platformach macOS i Linux.

🛠️

Przed rozpoczęciem tej procedury upewnij się, że masz klucz USB o minimalnej prędkości odczytu 150 MB/s i pojemności co najmniej 8 GB, najlepiej USB 3.0.


Wymagania wstępne:



- 1 klucz USB, tylko dla Tails, o pojemności co najmniej 8 GB
- Komputer podłączony do Internetu z systemem Linux, macOS (lub Windows)
- Około jednej godziny wolnego czasu, w zależności od szybkości połączenia internetowego, w tym ½ godziny na instalację (do pobrania plik o rozmiarze 1,3 GB)


## Krok 1: Pobierz Tails ze swojego komputera


![image](assets/1.webp)


🔗 **Oficjalna sekcja Tails:** https://tails.boum.org/install/linux/index.fr.html#download


Pobieranie pliku instalacyjnego z rozszerzeniem .img może zająć trochę czasu w zależności od szybkości pobierania z Internetu, więc zaplanuj to z wyprzedzeniem. Przy nowoczesnym i wydajnym łączu zajmie to mniej niż 5 minut.


Zapisz plik w znanym folderze, takim jak Pobrane, ponieważ będzie on potrzebny w następnym kroku.


## Krok 2: Zweryfikuj pobieranie


![image](assets/2.webp)


🔗 **Oficjalna sekcja Tails:** https://tails.boum.org/install/linux/index.fr.html#verify


Weryfikacja pobierania zapewnia, że zostało ono wydane przez programistów Tails i nie zostało uszkodzone lub przechwycone podczas pobierania.


Możliwe jest ręczne sprawdzenie, czy właśnie pobrany plik jest tym oczekiwanym przy użyciu PGP, ale bez zaawansowanej wiedzy weryfikacja ta oferuje taki sam poziom bezpieczeństwa jak weryfikacja JavaScript na stronie pobierania, ale jest znacznie bardziej skomplikowana i podatna na błędy.


Aby zweryfikować plik, użyj przycisku "Wybierz pobieranie..." dostępnego w oficjalnej sekcji!


## Krok 3: Zainstaluj Tails na kluczu USB


![image](assets/3.webp)


🔗 **Oficjalna sekcja Tails:**



- **Linux:** https://tails.boum.org/install/linux/index.fr.html#install
- **macOS:** https://tails.boum.org/install/mac/index.fr.html#etcher i https://tails.boum.org/install/mac/index.fr.html#install


Ten krok instalacji Tails na kluczu USB jest najtrudniejszy w całym przewodniku, zwłaszcza jeśli nigdy wcześniej tego nie robiłeś. Najważniejszą kwestią jest wybranie właściwej procedury w oficjalnej sekcji dla danego systemu operacyjnego: Linux lub macOS.


Po zainstalowaniu i przygotowaniu narzędzi zgodnie z zaleceniami, plik z rozszerzeniem .img można skopiować do klucza (usuwając wszystkie istniejące dane), aby uczynić go "bootowalnym" niezależnie.


Powodzenia i do zobaczenia na 4. etapie.


## Krok 4: Uruchom ponownie klucz USB Tails


![image](assets/4.webp)


🔗 **Oficjalna sekcja Tails:** https://tails.boum.org/install/linux/index.en.html#restart


Nadszedł czas, aby uruchomić jeden z komputerów za pomocą nowej pamięci USB. Włóż ją do jednego z portów USB i uruchom ponownie!


**Uwaga💡: Większość komputerów nie uruchamia się automatycznie z pamięci USB Tails, ale można nacisnąć przycisk menu rozruchu, aby wyświetlić listę możliwych urządzeń do uruchomienia**


Aby określić, który klawisz należy nacisnąć, aby upewnić się, że menu rozruchowe umożliwia wybranie pamięci USB zamiast zwykłego dysku Hard, poniżej znajduje się niewyczerpująca lista według producenta:


| Manufacturer | Key              |
| ------------ | ---------------- |
| Acer         | F12, F9, F2, Esc |
| Apple        | Option           |
| Asus         | Esc              |
| Clevo        | F7               |
| Dell         | F12              |
| Fujitsu      | F12, Esc         |
| HP           | F9               |
| Huawei       | F12              |
| Intel        | F10              |
| Lenovo       | F12              |
| MSI          | F11              |
| Samsung      | Esc, F12, F2     |
| Sony         | F11, Esc, F10    |
| Toshiba      | F12              |
| others...    | F12, Esc         |

Po wybraniu pamięci USB powinieneś zobaczyć nowy ekran rozruchowy, co jest bardzo dobrym znakiem, więc pozwól komputerowi kontynuować uruchamianie....


![image](assets/5.webp)


## Krok 5: Witamy w Tails!


![image](assets/6.webp)


🔗 **Oficjalna sekcja Tails:** https://tails.boum.org/install/linux/index.en.html#tails


Po jednej lub dwóch minutach od uruchomienia programu ładującego i wyświetlenia ekranu ładowania pojawi się ekran powitalny.


![image](assets/7.webp)


Na ekranie powitalnym wybierz język i układ klawiatury w sekcji Język i region. Kliknij przycisk Start Tails.


![image](assets/8.webp)


Jeśli komputer nie jest podłączony przewodowo do sieci, zapoznaj się z oficjalnymi instrukcjami Tails, aby połączyć się z siecią bez Wi-Fi (sekcja "Przetestuj swoją sieć Wi-Fi").


Po połączeniu z siecią lokalną pojawi się kreator połączenia Tor, który pomoże ci połączyć się z siecią Tor.


![image](assets/9.webp)


Możesz rozpocząć przeglądanie anonimowo, odkrywać opcje i oprogramowanie zawarte w Tails. Baw się dobrze, masz dużo miejsca na błędy, ponieważ nic nie jest modyfikowane na pamięci USB... Następny restart pozwoli zapomnieć o wszystkich doświadczeniach!


## W przyszłym przewodniku...


Gdy już trochę poeksperymentujesz z własną pamięcią USB Tails, omówimy inne, bardziej zaawansowane tematy w innym artykule, takie jak:



- Zaktualizuj klucz za pomocą **najnowszej wersji Tails**;
- Skonfiguruj i używaj **trwałej pamięci masowej**;
- Zainstaluj **dodatkowe oprogramowanie**.


Do tego czasu, jak zawsze, jeśli masz jakieś pytania, podziel się nimi ze społecznością Agora256. Uczymy się razem, aby jutro być lepszymi niż dziś!