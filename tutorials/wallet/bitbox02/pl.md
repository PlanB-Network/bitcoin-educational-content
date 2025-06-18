---
name: BitBox02

description: Konfiguracja i korzystanie z BitBox02
---

![cover](assets/cover.webp)


BitBox02 (https://bitbox.swiss/) to wykonany w Szwajcarii fizyczny Wallet zaprojektowany specjalnie do zabezpieczania Bitcoinów. Niektóre z jego kluczowych funkcji obejmują łatwe tworzenie kopii zapasowych i przywracanie za pomocą karty microSD, minimalistyczny i dyskretny wygląd oraz kompleksowe wsparcie dla Bitcoin.


![device](assets/1.webp)


Oferuje najnowocześniejsze zabezpieczenia opracowane przez ekspertów, w tym dwuprocesorową konstrukcję zawierającą bezpieczny chip. Jego kod źródłowy został w pełni skontrolowany przez badaczy bezpieczeństwa i jest całkowicie open-source. BitBox02 jest wyposażony w prostą, ale potężną aplikację BitBoxApp, która zapewnia bezpieczne zarządzanie Bitcoinami. Obsługuje Full node dla Bitcoin i zapewnia szyfrowaną komunikację end-to-end między aplikacją a urządzeniem. Wyprodukowany w Szwajcarii, BitBox02 zyskał pozytywną reputację wśród użytkowników.


![video](https://youtu.be/sB4b2PbYaj0)


Oto specyfikacja Wallet:



- Łączność: USB-C
- Kompatybilność: Windows 7 i nowsze, macOS 10.13 i nowsze, Linux, Android
- Wejście: Pojemnościowe czujniki dotykowe
- Mikrokontroler: ATSAMD51J20A; 120 Mhz 32-bitowy Cortex-M4F; Prawdziwy generator liczb losowych
- Bezpieczny chip: ATECC608B; Prawdziwy generator liczb losowych (NIST SP 800-90A/B/C)
- Wyświetlacz: 128 x 64 px biały OLED
- Materiał: Poliwęglan
- Rozmiar: 54,5 x 25,4 x 9,6 mm z wtyczką USB-C
- Waga: Urządzenie 12g; z opakowaniem i akcesoriami 160g


Arkusze danych można pobrać z ich strony internetowej https://bitbox.swiss/bitbox02/


## Jak korzystać z BitBox02 Hardware Wallet


### Konfiguracja BitBox02


BitBox02 ma złącze USB-C dołączone do obudowy. Jeśli twój komputer korzysta ze zwykłego portu USB, będziesz musiał użyć adaptera dołączonego do urządzenia.


Podłącz go do komputera, a urządzenie włączy się (nie rób tego jeszcze).


Posiada on czujniki powyżej i poniżej i poprosi o dotknięcie górnej lub dolnej części, aby ustawić ekran w pożądany sposób.


![image](assets/2.webp)


### Pobierz aplikację BitBox02


Odwiedź stronę https://shiftcrypto.ch/ i kliknij łącze "App" u góry, aby przejść do strony pobierania:


![image](assets/3.webp)


Kliknij niebieski przycisk Pobierz:


![image](assets/4.webp)


Aby zweryfikować pobieranie (zwiększa to złożoność, ale jest zalecane, szczególnie w przypadku przechowywania wielu Bitcoin), patrz Dodatek A.


Po pobraniu można rozpakować plik. Na komputerze Mac wystarczy dwukrotnie kliknąć pobrany plik, a w katalogu pobierania pojawi się ikona aplikacji BitBox. Możesz przeciągnąć ją na pulpit (lub w dowolne inne miejsce), aby mieć do niej łatwy dostęp.


Kliknij dwukrotnie aplikację, aby ją uruchomić (nie zostanie "zainstalowana").


Na komputerze Mac komputerowa niania wyświetli ostrzeżenie. Zignoruj je i kliknij "Otwórz":


![image](assets/5.webp)


Następnie zobaczysz to:


![image](assets/6.webp)


Podłącz urządzenie do komputera.


Zostanie wyświetlony kod parowania. Sprawdź, czy się zgadzają, a następnie dotknij czujnika, aby zaznaczyć znacznik wyboru. Po powrocie do ekranu dostępny będzie przycisk kontynuowania.


![image](assets/7.webp)


Następnie będziesz mieć możliwość utworzenia nowego seed lub przywrócenia seed. Zademonstruję tworzenie nowego seed (ważne jest również przywrócenie utworzonego seed w celu przetestowania jakości kopii zapasowej przed załadowaniem Bitcoin na Wallet).


![image](assets/8.webp)


Urządzenie zostało dostarczone z kartą microSD. Jeśli jej nie masz, włóż ją.


![image](assets/9.webp)


Nazwij urządzenie i kliknij Kontynuuj, a następnie potwierdź na urządzeniu.


![image](assets/10.webp)


Następnie zostaniesz poproszony o ustawienie hasła dla urządzenia. To nie jest część seed. Nie jest to również passphrase (to część seed). Jest to po prostu hasło blokujące urządzenie. Po włączeniu urządzenia za każdym razem zostaniesz poproszony o wprowadzenie tego hasła. Dozwolone jest 10 kolejnych niepowodzeń, zanim urządzenie wyczyści się z całej pamięci, więc należy zachować ostrożność. Animacja na ekranie nauczy Cię, jak używać elementów sterujących urządzenia do ustawiania hasła.


![image](assets/11.webp)


Przeczytaj następny ekran i zaznacz każde pole, a następnie kontynuuj.


![image](assets/12.webp)

![image](assets/13.webp)

![image](assets/14.webp)


A tak wygląda Wallet, gdy jest już gotowy do pracy.


![image](assets/15.webp)


### NIE TAK SZYBKO!!!


To dość dziwne, ale BitBox02 mówi nam, że jesteśmy gotowi do użycia urządzenia, ale nie obiecał nam zapisania słów seed! Jedyną kopią zapasową, jaką mamy, jest plik zapisany na karcie microSD. Jest to niewystarczające. Te urządzenia pamięci masowej nie działają wiecznie (z powodu "gnicia bitów"). Potrzebujemy papierowej kopii zapasowej i duplikatów przechowywanych w sejfie (jak wyjaśniono w ogólnym przewodniku dotyczącym korzystania z portfeli sprzętowych)


Aby uzyskać naszą frazę seed i zapisać ją, przejdź do zakładki "zarządzaj urządzeniem" po lewej stronie, a następnie kliknij "pokaż słowa odzyskiwania"


![image](assets/16.webp)


Następnie możesz przejść przez potwierdzenie, a urządzenie wyświetli słowa. Zapisz je starannie i nigdy nie pozwól nikomu ich zobaczyć.


![image](assets/17.webp)


Następnie możesz kliknąć zakładkę Bitcoin po lewej stronie, aby uzyskać adresy odbiorcze.


![image](assets/18.webp)


Pokazuje jedną na raz, ale przynajmniej pozwala wybrać Address do użycia z pierwszych 20:


![image](assets/19.webp)


Kliknięcie niebieskiego przycisku spowoduje wyświetlenie pełnego Address i zostaniesz poproszony o sprawdzenie, czy Address pasuje do wyświetlanego na ekranie. Jest to dobra praktyka, aby potwierdzić, że żadne złośliwe oprogramowanie na twoim komputerze nie oszukuje cię, aby wysłać Bitcoin do Address atakującego.


![image](assets/20.webp)


Aby wysłać Bitcoin do Wallet, możesz skopiować Address i wkleić go na stronie wypłat Exchange, gdzie znajdują się Twoje monety. Zalecam wysłanie najpierw małej kwoty testowej, a następnie przećwiczenie wydawania jej z powrotem do Exchange lub do drugiego Address w Wallet.


W przypadku większych ilości sugeruję utworzenie passphrase (patrz poniżej). Oryginalny Wallet (bez passphrase) może być użyty jako wabik Wallet (będzie musiał zawierać rozsądną ilość, aby był wiarygodnym wabikiem).


### Połączenie z węzłem


BitBox02 automatycznie połączy się z węzłem. Zobaczmy, gdzie się łączy. Kliknij zakładkę ustawień po lewej stronie, a następnie "podłącz własny Full node".


![image](assets/21.webp)


Tutaj widzimy, że łączy się z węzłem shiftcrypto. Nie jest dobrze. Zdradziliśmy im wszystkie nasze adresy Bitcoin i nasze IP Address (oczywiście nie seed; widzą nasze adresy/bilanse, ale nie mogą ich wydać). Możemy wprowadzić własne dane węzła na tej stronie (poza zakresem tego konkretnego przewodnika) lub możemy użyć lepszego oprogramowania, takiego jak Sparrow Bitcoin Wallet, Electrum Desktop Wallet lub Specter Desktop. Zademonstruję Sparrow Bitcoin Wallet w dalszej części przewodnika.


![image](assets/22.webp)


Dodaj passphrase


Teraz, gdy skonfigurowaliśmy urządzenie za pomocą aplikacji BitBox02 (i ujawniliśmy nasze adresy, nieuniknione w przypadku tego konkretnego Hardware Wallet), możemy dodać passphrase do naszej frazy seed. Pozwoli nam to utworzyć nowy Wallet przy użyciu tego samego seed, a ShiftCrypto nigdy nie zobaczy naszych nowych adresów. Będziemy łączyć ten Wallet tylko z naszym własnym oprogramowaniem.


### Włącz passphrase


Przejdź teraz i "włącz" funkcję passphrase (ale jeszcze nie ustawiamy passphrase). Przejdź do zakładki "Zarządzaj urządzeniem" i kliknij "Włącz passphrase" (czerwone kółko poniżej).


![image](assets/23.webp)


Przeczytaj wszystkie kroki..


![image](assets/24.webp)

![image](assets/25.webp)

![image](assets/26.webp)


Teraz odłącz urządzenie i zamknij aplikację BitBox02


KONIEC sekcji bitbox02 autorstwa Parman.


Twoje urządzenie jest teraz w pełni gotowe do użycia na dowolnym rozwiązaniu desktopowym, takim jak specter, sparrow i przy użyciu bitbox Interface.