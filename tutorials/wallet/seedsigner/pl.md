---
name: SeedSigner
description: Bezstanowy, niedrogi i w pełni hermetyzowany sprzęt wallet do samodzielnego montażu
---

![cover](assets/cover.webp)



SeedSigner to sprzęt wallet Bitcoin o otwartym kodzie źródłowym, który każdy może samodzielnie zbudować przy użyciu niedrogich komponentów elektronicznych ogólnego przeznaczenia. W przeciwieństwie do produktów komercyjnych, takich jak Ledger, Coldcard lub Trezor, nie jest to gotowe do użycia urządzenie wyprodukowane przez firmę: jest to projekt społecznościowy, który pozwala każdemu stworzyć własne urządzenie, kontrolując każdy krok.



SeedSigner został zaprojektowany tak, aby był w 100% ***air-gapped***: nigdy nie łączy się z Internetem, nie ma Wi-Fi ani Bluetooth (w przypadku Raspberry Pi Zero v1.3) i nigdy nie jest podłączony do komputera w celu wymiany danych. Komunikacja odbywa się wyłącznie za pośrednictwem systemu wymiany kodów QR. Mówiąc konkretnie, oprogramowanie do zarządzania portfelem (takie jak Sparrow Wallet) wyświetla transakcję do podpisania w postaci kodów QR; skanujesz je za pomocą kamery SeedSigner, a następnie urządzenie podpisuje transakcję przy użyciu kluczy prywatnych tymczasowo przechowywanych w pamięci RAM. Na koniec generuje kody QR zawierające podpisaną transakcję, które użytkownik skanuje za pomocą oprogramowania, aby wysłać je do sieci Bitcoin.



![Image](assets/fr/001.webp)



SeedSigner jest również ***bezstanowy***. Innymi słowy, nie zapisuje seed ani kluczy prywatnych na stałe, w przeciwieństwie do innych portfeli sprzętowych. Przy każdym ponownym uruchomieniu jego pamięć jest całkowicie pusta, chyba że urządzenie zostanie skonfigurowane do zapisywania ustawień na karcie microSD. W związku z tym konieczne jest ponowne wprowadzanie seed za każdym razem, gdy z niego korzystasz, a najbardziej praktyczną metodą jest przechowywanie go w postaci kodu QR, który należy zeskanować przy uruchomieniu za pomocą kamery SeedSigner. Ten tryb działania znacznie zmniejsza powierzchnię ataku: nawet jeśli złodziej ukradnie urządzenie, nie znajdzie na nim żadnych informacji, ponieważ domyślnie jest ono zawsze puste.



Inną opcją przechowywania seed i używania go z SeedSigner jest użycie karty inteligentnej *SeedKeeper* w połączeniu z kompatybilnym czytnikiem. Daje to bardzo solidny *Secure Element* do przechowywania seed, przy jednoczesnym wykorzystaniu ekranu SeedSigner do podpisywania transakcji. Ale ta konkretna konfiguracja jest tematem innego dedykowanego samouczka. Tutaj skoncentrujemy się na podstawowym użyciu SeedSigner:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

Projekt SeedSigner zajmuje ważne miejsce w ekosystemie Bitcoin, ponieważ oferuje każdemu, na całym świecie, możliwość korzystania z zaawansowanych zabezpieczeń w celu ochrony swoich bitcoinów. Jego główną zaletą jest dostępność: wymagany sprzęt można kupić za mniej niż 50 USD. Co więcej, umożliwia on osobom mieszkającym w krajach o ograniczonym dostępie zbudowanie własnego sprzętu wallet ze standardowych komponentów komputerowych, które są łatwe do znalezienia i mniej podlegają ograniczeniom regulacyjnym.



Ale nawet poza tymi konkretnymi kontekstami, SeedSigner może być interesującą opcją dla ciebie: jest open-source, działa bezstanowo i w trybie airgapped oraz redukuje wektory ataku związane z łańcuchem dostaw twojego sprzętu wallet.



## 1. Wymagany sprzęt



Do zbudowania SeedSigner potrzebne będą następujące komponenty:





- Raspberry Pi Zero
    - Zalecana jest wersja 1.3, ponieważ nie ma ona ani Wi-Fi, ani Bluetooth, co zapewnia całkowitą izolację.
 - Wersje W i v2 są również kompatybilne, ale zawierają układ Wi-Fi/Bluetooth. Dlatego też zaleca się jego fizyczną dezaktywację poprzez usunięcie modułu radiowego z karty. Operacja jest stosunkowo prosta, ale wymaga precyzji (w przypadku Zero W wystarczą cienkie szczypce, natomiast w przypadku v2 do usunięcia metalowej płytki skrywającej moduł potrzebny jest gorący długopis). Nie będę zagłębiał się w szczegóły w tym poradniku, ale wszystkie instrukcje znajdziesz w tym dokumencie: *[Sprzętowe wyłączanie WiFi/Bluetooth](https://github.com/DesobedienteTecnologico/rpi_disable_wifi_and_bt_by_hardware)*.
 - Uwaga: niektóre modele Raspberry Pi Zero są sprzedawane bez wstępnie przylutowanych pinów GPIO. Możesz kupić wersję ze zintegrowanymi pinami bezpośrednio (najprostsze rozwiązanie) lub kupić piny osobno i przylutować je samodzielnie (bardziej złożone rozwiązanie).
 - Nie zapomnij dołączyć zasilacza micro-USB.



![Image](assets/fr/002.webp)





- Ekran Waveshare 1,3" (240×240 px)** (w języku francuskim)
    - Wybór tego konkretnego modelu jest kluczowy: istnieją inne podobne ekrany, ale z inną rozdzielczością. Bez rozdzielczości 240×240 px wyświetlacz będzie bezużyteczny.
    - Na ekranie znajdują się trzy przyciski i mini-joystick do obsługi interfejsu użytkownika.



![Image](assets/fr/003.webp)





- Kamera kompatybilna z Raspberry Pi Zero**
    - Opcja 1: standardowa kamera z szeroką złotą matą (sprawdź kompatybilność z obudową).
    - Opcja 2: bardziej kompaktowa kamera "*Zero*", zaprojektowana specjalnie dla Pi Zero.



![Image](assets/fr/004.webp)





- Karta MicroSD**
    - Zalecana pojemność: od 4 do 32 GB.





- Obudowa (opcjonalna, ale zalecana)** (opcjonalna, ale zalecana)** (opcjonalna, ale zalecana)** (opcjonalna, ale zalecana)**)
    - Chroni urządzenie i ułatwia korzystanie z niego.
    - Najpopularniejszym modelem jest "*Orange Pill Case*", dla którego dostępne są pliki STL do druku 3D (https://github.com/SeedSigner/seedsigner/tree/dev/enclosureshttps://github.com/SeedSigner/seedsigner/tree/dev/enclosures).
    - Pudełka są również dostępne u [niezależnych sprzedawców powiązanych z projektem](https://seedsigner.com/hardware/).



![Image](assets/fr/005.webp)



Możesz kupić te komponenty osobno lub, dla większej prostoty, zdecydować się na gotowe pakiety, które zawierają cały niezbędny sprzęt. Osobiście zamówiłem swój pakiet [na tej francuskiej stronie](https://bitcoinbazar.fr/), ale listę sprzedawców dla każdego regionu świata znajdziesz również na [stronie sprzętu projektu SeedSigner](https://seedsigner.com/hardware/). Jeśli wolisz kupować komponenty pojedynczo, są one dostępne na głównych platformach handlu elektronicznego lub w specjalistycznych sklepach.



## 2. Przygotowanie oprogramowania



Po skompletowaniu sprzętu należy przygotować kartę microSD, instalując na niej system SeedSigner. Aby to zrobić, przejdź do swojego codziennego komputera osobistego i podłącz kartę microSD przeznaczoną dla SeedSigner.



### 2.1. Pobierz



Przejdź do [oficjalnego repozytorium GitHub projektu](https://github.com/SeedSigner/seedsigner/releases). Aby uzyskać najnowszą wersję oprogramowania, pobierz :




- Obraz `.img` odpowiadający posiadanemu modelowi Pi.
- Plik `.sha256.txt`.
- Plik `.sha256.txt.sig`.



![Image](assets/fr/006.webp)



Przed rozpoczęciem instalacji sprawdźmy oprogramowanie.



### 2.2 Weryfikacja w systemach Linux i macOS



Zacznij od zaimportowania oficjalnego klucza publicznego projektu SeedSigner bezpośrednio z Keybase:



```
gpg --fetch-keys https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/007.webp)



Terminal powinien poinformować, że klucz został zaimportowany lub zaktualizowany. Następnie uruchom polecenie weryfikacji na pliku podpisu (pamiętaj, aby zmodyfikować polecenie zgodnie z wersją, tutaj `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/008.webp)



Jeśli wszystko jest w porządku, wyjście powinno brzmieć `Dobry podpis`. Oznacza to, że plik `.sha256.txt` został podpisany kluczem, który właśnie zaimportowałeś i że podpis jest ważny. Zignoruj komunikat ostrzegawczy `OSTRZEŻENIE: Ten klucz nie jest certyfikowany zaufanym podpisem`: jest to normalne, ponieważ teraz do ciebie należy sprawdzenie, czy użyty klucz należy do projektu SeedSigner.



Aby to zrobić, porównaj ostatnie 16 znaków wyświetlanego odcisku palca z tymi dostępnymi na [Keybase.io/SeedSigner](https://keybase.io/seedsigner), na ich [oficjalnym Twitterze](https://twitter.com/SeedSigner/status/1530555252373704707) lub w pliku opublikowanym na [SeedSigner.com](https://seedsigner.com/keybase.txt). Jeśli te identyfikatory dokładnie pasują, możesz być pewien, że klucz jest rzeczywiście kluczem projektu. W razie wątpliwości należy natychmiast przerwać i poprosić o pomoc społeczność SeedSigner (Telegram, X, GitHub...).



Po zatwierdzeniu klucza można sprawdzić, czy pobrany obraz nie został zmodyfikowany (pamiętaj, aby zmodyfikować polecenie zgodnie z wersją, tutaj `0.8.6.`):



```
shasum -a 256 --ignore-missing --check seedsigner.0.8.6.sha256.txt
```



![Image](assets/fr/009.webp)





- W systemie Linux polecenie to jest wbudowane.
- Ostrzeżenie: wersje macOS wcześniejsze niż `Big Sur (11)` nie rozpoznają opcji `--ignore-missing`. W takim przypadku należy ją usunąć i zignorować ostrzeżenia o brakujących plikach.



Oczekiwanym rezultatem jest `OK` obok pliku `.img`. Potwierdza to, że przesłany obraz jest identyczny z tym opublikowanym przez projekt i nie został zmodyfikowany.



### 2.3 Weryfikacja systemu Windows



W systemie Windows procedura jest podobna, ale polecenia są inne. Zacznij od zainstalowania [Gpg4win](https://www.gpg4win.org/) i otwórz aplikację *Kleopatra*. Zaimportuj klucz publiczny projektu SeedSigner z adresu URL Keybase :



```
https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/010.webp)



Następnie otwórz PowerShell w folderze, w którym znajdują się pobrane pliki (`Shift` + prawy przycisk myszy > `Otwórz PowerShell tutaj`). Uruchom następujące polecenie, aby sprawdzić podpis manifestu (pamiętaj, aby zmodyfikować polecenie zgodnie z wersją, tutaj `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/011.webp)



Jeśli wszystko jest w porządku, wyjście powinno brzmieć `Dobry podpis`. Oznacza to, że plik `.sha256.txt` został podpisany kluczem, który właśnie zaimportowałeś i że podpis jest ważny. Zignoruj komunikat ostrzegawczy `OSTRZEŻENIE: Ten klucz nie jest certyfikowany zaufanym podpisem`: jest to normalne, ponieważ teraz do ciebie należy sprawdzenie, czy użyty klucz należy do projektu SeedSigner.



Aby to zrobić, porównaj ostatnie 16 znaków wyświetlanego odcisku palca z tymi dostępnymi na [Keybase.io/SeedSigner](https://keybase.io/seedsigner), na ich [oficjalnym Twitterze](https://twitter.com/SeedSigner/status/1530555252373704707) lub w pliku opublikowanym na [SeedSigner.com](https://seedsigner.com/keybase.txt). Jeśli te identyfikatory dokładnie pasują, możesz być pewien, że klucz jest rzeczywiście kluczem projektu. W razie wątpliwości należy natychmiast przerwać i poprosić o pomoc społeczność SeedSigner (Telegram, X, GitHub...).



Po zweryfikowaniu klucza należy sprawdzić, czy plik obrazu nie został uszkodzony. Aby to zrobić, użyj następującego polecenia w PowerShell :



```
CertUtil -hashfile seedsigner_os.0.8.6.[your-Pi-model].img SHA256
```



Przykład dla Raspberry Pi Zero 2 (pamiętaj, aby zmodyfikować polecenie zgodnie z wersją, tutaj `0.8.6.`):



```
CertUtil -hashfile seedsigner_os.0.8.6.pi02w.img SHA256
```



![Image](assets/fr/012.webp)



Następnie PowerShell oblicza skrót SHA256 pliku obrazu. Porównaj ten skrót z odpowiednią wartością w pliku `seedsigner.0.8.6.sha256.txt`.




- Jeśli obie wartości są identyczne, sprawdzenie zakończy się pomyślnie i można kontynuować.
- Jeśli się różnią, plik jest uszkodzony. Nie używaj go i rozpocznij pobieranie ponownie.



![Image](assets/fr/013.webp)



Pomyślna weryfikacja gwarantuje, że plik `.img` jest zarówno autentyczny (podpisany przez SeedSigner), jak i niezmieniony (niezmodyfikowany). Następnie można bezpiecznie przejść do następnego kroku.



### 2.4. Miganie obrazu



Jeśli jeszcze go nie masz, pobierz oprogramowanie [Balena Etcher](https://etcher.balena.io/), a następnie :




- Włóż kartę microSD do komputera.
- Launch Etcher.
- Wybierz pobrany i zweryfikowany plik `.img`.
- Wybierz kartę microSD jako cel.
- Kliknij na `Flash!`.



![Image](assets/fr/014.webp)



Poczekaj na zakończenie procesu: karta microSD jest gotowa do użycia. Teraz czas na montaż!



## 3. Zespół SeedSigner



Po przygotowaniu karty microSD i sflashowaniu jej oprogramowaniem SeedSigner, można przystąpić do końcowego montażu. Nie spiesz się, ponieważ niektóre części są delikatne (zwłaszcza obrus, kamera i piny GPIO).



### 3.1 Przygotowanie obudowy



Przede wszystkim otwórz obudowę. Sprawdź, czy jest czysta i czy żadne pozostałości plastiku z druku 3D nie przeszkadzają w wewnętrznych zapięciach. Zwróć uwagę na :




- Lokalizacja kamery (mały okrągły otwór z przodu).
- Otwór na ekran.
- Wycięcia na porty micro-USB i gniazdo microSD w Raspberry Pi Zero.



### 3.2 Instalacja kamery



Zlokalizuj złącze taśmowe kamery na Raspberry Pi Zero: jest to cienki czarny pasek z boku płytki, który można lekko podnieść, aby go otworzyć. Podnieś go ostrożnie, bez naciskania: powinien po prostu przechylić się o kilka milimetrów.



![Image](assets/fr/015.webp)



Włóż pokrywę kamery. Brązowa/miedziana część powinna być skierowana w dół. Upewnij się, że jest mocno osadzona w złączu, bez skręcania.



![Image](assets/fr/016.webp)



Zamknij czarny pasek, aby zablokować obrus (poczujesz lekkie kliknięcie). Delikatnie sprawdź, czy obrus pozostaje na miejscu i nie przesuwa się.



![Image](assets/fr/017.webp)



Następnie umieść moduł kamery w odpowiednim otworze w obudowie. W zależności od modelu może on zatrzasnąć się bezpośrednio lub wymagać niewielkiego paska samoprzylepnego, aby utrzymać go na miejscu. Obiektyw musi być idealnie wyrównany i skierowany na zewnątrz.



### 3.3 Instalacja Raspberry Pi Zero



Jeśli używasz obudowy, włóż płytkę Raspberry Pi Zero do środka. Ostrożnie wyrównaj porty z przewidzianymi otworami.



Następnie umieść wyświetlacz Waveshare na Raspberry Pi Zero. Piny GPIO Pi powinny idealnie pokrywać się z żeńskim złączem wyświetlacza. Powoli dociśnij wyświetlacz do pinów, wywierając równomierny nacisk z każdej strony, aby uniknąć ich zgięcia.



![Image](assets/fr/018.webp)



Jeśli posiadasz obudowę, dokończ montaż, dodając panel przedni i joystick.



Na koniec włóż kartę microSD zawierającą sflashowane oprogramowanie do gniazda Raspberry Pi Zero zamontowanego na krawędzi. Upewnij się, że zatrzasnęła się na swoim miejscu.



### 3.4 Pierwsze uruchomienie



Podłącz kabel zasilający micro-USB do dedykowanego portu. Odczekaj około minuty. Powinno pojawić się logo SeedSigner, a następnie ekran główny.



![Image](assets/fr/019.webp)



Na początek sprawdź, czy różne komponenty działają prawidłowo, przechodząc do menu `Ustawienia > Test I/O`.



![Image](assets/fr/020.webp)



Przetestuj wszystkie przyciski i upewnij się, że reagują prawidłowo. Następnie kliknij przycisk `KEY1`, aby sprawdzić, czy kamera działa zgodnie z oczekiwaniami. Spowoduje to zrobienie zdjęcia.



![Image](assets/fr/021.webp)



### 3.5 Regulacja kamery



W zależności od sposobu zamontowania SeedSigner, kamera może wyświetlać odwrócony obraz. Aby to skorygować, przejdź do `Ustawienia > Zaawansowane > Obrót kamery` i w razie potrzeby wybierz obrót o 180°.



![Image](assets/fr/022.webp)



Jeśli zmieniłeś orientację kamery lub chcesz zmienić inne ustawienia (takie jak język interfejsu) w późniejszym terminie, musisz włączyć trwałość ustawień na karcie microSD. W przeciwnym razie ustawienia zostaną przywrócone do domyślnych przy każdym ponownym uruchomieniu, ponieważ Raspberry Pi Zero nie ma trwałej pamięci.



Aby to zrobić, otwórz menu `Ustawienia > Ustawienia trwałe`, a następnie wybierz `Włączone`.



![Image](assets/fr/023.webp)



Jeśli wszystko działa, SeedSigner jest gotowy do użycia!



## 4. Ustawienia SeedSigner



Przed utworzeniem Bitcoin wallet skonfigurujmy SeedSigner. Ponieważ działa on na Raspberry Pi Zero bez pamięci trwałej, jego ustawienia nie są zapisywane automatycznie, chyba że zapiszesz je na karcie microSD. Upewnij się więc, że włączyłeś tę opcję, w przeciwnym razie ustawienia te zostaną utracone po ponownym uruchomieniu (patrz krok 3.5).



### 4.1 Dostęp do menu parametrów



Uruchom SeedSigner i poczekaj, aż pojawi się ekran główny. Za pomocą joysticka przejdź do opcji `Settings`, a następnie zatwierdź ją, naciskając środkowy przycisk. Nastąpi przejście do głównego menu ustawień.



![Image](assets/fr/024.webp)



### 4.2 Wybór oprogramowania do zarządzania portfelem



Następnie przejdź do menu `Coordinator software`.



![Image](assets/fr/025.webp)



"Koordynator" odnosi się do oprogramowania do zarządzania portfelem, z którym SeedSigner komunikuje się za pomocą kodów QR. Oprogramowanie to jest instalowane na komputerze lub smartfonie. Umożliwia ono zarządzanie bitcoinami, ale bez dostępu do kluczy prywatnych. SeedSigner pozostaje jedynym urządzeniem zdolnym do podpisywania transakcji.



Aktualna wersja firmware'u obsługuje kilka programów: Sparrow, Specter, BlueWallet, Nunchuk oraz Keeper. W moim przypadku korzystam z **Sparrow Wallet**, który szczególnie polecam ze względu na prostotę i bogatą funkcjonalność.



Jeśli nie wiesz, jak ją zainstalować, możesz skorzystać z tego samouczka:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Wystarczy wybrać odpowiednie oprogramowanie z menu.



![Image](assets/fr/026.webp)



### 4.3 Wyświetlanie jednostek i ilości



W menu `Denomination Display` można wybrać jednostkę, w której wyświetlane są kwoty:




- `BTC`
- mBTC` (milibitcoin lub 0,001 BTC)
- gW-15 (satoshi lub 1/100,000,000 BTC)



Jednostka **sats** jest generalnie najbardziej praktyczna w przypadku małych ilości.



![Image](assets/fr/027.webp)



### 4.4 Ustawienia zaawansowane



Teraz przejdź do menu `Zaawansowane`. Znajdziesz tam kilka przydatnych opcji:




- gW-17 network`: należy zmodyfikować tylko, jeśli chcesz używać SeedSigner na Testnet.
- qR code density`: dostosowuje ilość informacji zawartych w każdym kodzie QR. Można pozostawić wartość domyślną, chyba że odczytanie kodu podczas skanowania będzie trudne.
- `Xpub export`: włącza lub wyłącza eksport rozszerzonego klucza publicznego (`xpub`, `ypub`, `zpub`) do oprogramowania do zarządzania portfelem za pomocą kodu QR (funkcja, której będziemy używać później, więc na razie pozostaw ją włączoną).
- `Script types`: definiuje typy skryptów dozwolone do blokowania bitcoinów. Nie trzeba modyfikować tego parametru, ponieważ typ skryptu zostanie ustawiony bezpośrednio na Sparrow. Dotyczy to tylko skryptów, którymi SeedSigner może manipulować.



### 4.5 Wybór języka



Wreszcie, w menu `Language` można zmienić język interfejsu zgodnie z własnymi preferencjami.



![Image](assets/fr/028.webp)



## 5. Tworzenie i zapisywanie seed



seed (lub fraza mnemoniczna) stanowi podstawę portfela Bitcoin. Służy do uzyskiwania kluczy prywatnych i adresów oraz zapewnia dostęp do funduszy. SeedSigner oferuje kilka metod jego generowania, którym przyjrzymy się w tej sekcji.



Zanim zaczniemy, kilka istotnych przypomnień:




- Ta fraza daje pełny, nieograniczony dostęp do wszystkich bitcoinów użytkownika.** Każdy, kto jest w posiadaniu tej frazy, może ukraść środki użytkownika, nawet bez fizycznego dostępu do SeedSigner;
- Zazwyczaj 12-wyrazowa fraza jest używana do przywrócenia wallet w przypadku utraty lub kradzieży sprzętu wallet. Ale ponieważ SeedSigner jest urządzeniem *bezstanowym*, nigdy nie rejestruje seed. Tak więc fizyczne kopie zapasowe nie są zwykłymi kopiami zapasowymi, ale **jedynym sposobem korzystania z wallet**. Jeśli utracisz te kopie zapasowe, twoje bitcoiny zostaną trwale utracone. Twórz więc kopie zapasowe ostrożnie, na kilku nośnikach i w bezpiecznych miejscach;
- Jeśli dopiero zaczynasz, zdecydowanie radzę przeczytać ten samouczek, aby uzyskać szczegółowe informacje na temat ryzyka związanego z zarządzaniem frazą mnemoniczną:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.1 Dostęp do narzędzia do tworzenia seed



Na ekranie głównym SeedSigner przejdź do menu `Tools`.



![Image](assets/fr/029.webp)



Otrzymasz teraz generate i seed. seed to po prostu duża liczba losowa. Im bardziej losowo jest generowana, tym jest bezpieczniejsza. SeedSigner oferuje dwa sposoby na zrobienie tego:




- camera": seed jest generowany na podstawie wizualnego szumu zdjęcia. Wykonujesz zdjęcie losowego otoczenia (obiektu, krajobrazu, twarzy itp.), którego zmiany pikseli są wykorzystywane do entropii generate. Jest to szybka metoda, ale nie powtarzalna.
- rzut kostką": rzucasz kostką, aby stworzyć niezbędną entropię. Jest to bardziej czasochłonne, ale powtarzalne, a zatem weryfikowalne. Jeśli zdecydujesz się na tę metodę, postępuj zgodnie z radami zawartymi w tym samouczku (nie ma potrzeby obliczania sumy kontrolnej, SeedSigner się tym zajmuje):



https://planb.academy/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

### 5.2 Tworzenie seed ze zdjęciem



Jeśli wybierzesz metodę fotograficzną, kliknij `Nowy seed` (z ikoną aparatu), zrób zdjęcie i zatwierdź je. Następnie wybierz długość zdania (12 lub 24 słowa), które pojawi się na ekranie w celu zapisania. Kolejne kroki są identyczne jak w części 5.3.



### 5.3 Tworzenie seed za pomocą kości



W tym poradniku użyjemy metody **Rolki kostką**. Kliknij na `New seed` (z ikoną kości).



![Image](assets/fr/030.webp)



Następnie wybierz długość frazy mnemonicznej. 12 słów zapewnia już wystarczający poziom bezpieczeństwa, więc jest to wybór, który polecam.



![Image](assets/fr/031.webp)



Rzuć kostką i wprowadź uzyskane liczby za pomocą kursora. Naciśnij środkowy przycisk, aby zatwierdzić każdy wpis. Jeśli popełnisz błąd, możesz się cofnąć. Użyj kilku różnych kości, aby zmniejszyć wpływ niezrównoważonych kości. Upewnij się, że nie jesteś obserwowany podczas tej operacji.



![Image](assets/fr/032.webp)



Po wprowadzeniu 50 rzutów, SeedSigner wygeneruje zdanie. **Postępuj zgodnie z instrukcjami zawartymi w tym samouczku, jeśli dopiero zaczynasz:**



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.4 Wyświetlanie i zapisywanie seed



Ostrożnie zapisz słowa swojej mnemotechnicznej frazy na odpowiednim fizycznym nośniku (papier lub metal).



![Image](assets/fr/033.webp)



### 5.5 Sprawdzanie kopii zapasowej



Aby uniknąć błędów kopii zapasowej, SeedSigner prosi o zweryfikowanie kopii zapasowej. Kliknij na `Verify`.



![Image](assets/fr/034.webp)



Następnie wprowadź żądane słowo zgodnie z jego kolejnością w zdaniu. Na przykład, tutaj muszę wybrać trzecie słowo w zdaniu.



![Image](assets/fr/035.webp)



Jeśli popełnisz błąd, SeedSigner poinformuje Cię o tym i będziesz musiał zacząć od nowa, pamiętając o zanotowaniu frazy mnemonicznej, gdy zostanie Ci ona podana. Ten krok weryfikacji zapewnia, że kopia zapasowa jest poprawna i kompletna. Po zatwierdzeniu na ekranie pojawi się komunikat "Backup Verified".



![Image](assets/fr/036.webp)



Aby uzyskać bardziej kompletny test przywracania, postępuj zgodnie z tym samouczkiem :



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 5.6 Zrozumienie koncepcji "urządzenia bezstanowego



SeedSigner jest urządzeniem bez pamięci stałej. Oznacza to, że seed nigdy nie jest przechowywany wewnątrz urządzenia (w przeciwieństwie do Ledger, Trezor lub Coldcard, na przykład). Po wyłączeniu zasilania seed całkowicie znika z pamięci RAM. Po ponownym uruchomieniu SeedSigner powraca do pustego stanu: będziesz musiał ponownie podać mu swój seed, aby mógł podpisać twoje transakcje.



Zapewnia to niezbędną ochronę. W przeciwieństwie do innych portfeli sprzętowych, SeedSigner opiera się na Raspberry Pi Zero, który nie ma fizycznej ochrony, w tym *Secure Element*. Ponieważ jednak nie są przechowywane żadne wrażliwe dane, nawet fizycznie naruszone urządzenie nie pozwoliłoby atakującemu na wyodrębnienie kluczy prywatnych lub wydanie bitcoinów.



Z drugiej strony, taka architektura wiąże się z dodatkową odpowiedzialnością: bez kopii zapasowej środki są definitywnie tracone. Dlatego zalecam **podwójną kopię zapasową**. Masz już swoją frazę odzyskiwania: jest to główna długoterminowa kopia zapasowa, którą należy przechowywać w bezpiecznym miejscu. Teraz utworzymy kopię tej frazy w postaci **kodu QR**.



Za każdym razem, gdy korzystasz z SeedSigner, skanujesz ten kod QR za pomocą kamery urządzenia, aby tymczasowo załadować seed do pamięci podczas podpisywania transakcji. Ta druga kopia zapasowa, przeznaczona do codziennego użytku, również musi być przechowywana z najwyższą ostrożnością: każdy, kto jest w posiadaniu tego kodu QR, ma pełny dostęp do twoich bitcoinów.


Radzę również przechowywać kod QR i frazę mnemoniczną w dwóch oddzielnych lokalizacjach, aby uniknąć utraty wszystkiego w przypadku reklamacji.



Wreszcie, bardziej zaawansowaną i bezpieczną alternatywą jest użycie SeedSigner z **SeedKeeper**, który przechowuje seed w secure element. Aby dowiedzieć się więcej, zapoznaj się z tym samouczkiem:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

### 5.7 Zapis odcisku palca klucza głównego



Po zakończeniu weryfikacji SeedSigner wyświetli odcisk palca klucza głównego wallet. Ten odcisk palca identyfikuje wallet i zapewnia użycie prawidłowej frazy odzyskiwania w przyszłości. Nie ujawnia on żadnych informacji o kluczach prywatnych, więc można go bezpiecznie przechowywać na nośniku cyfrowym. Upewnij się tylko, że masz dostępną kopię i nigdy jej nie zgubisz.



![Image](assets/fr/037.webp)



Na tym etapie można również dodać **passphrase BIP39**, aby wzmocnić bezpieczeństwo wallet. W zależności od strategii tworzenia kopii zapasowych, ta opcja może być opłacalna, ale wiąże się również z ryzykiem: jeśli stracisz passphrase, dostęp do twoich bitcoinów zostanie trwale utracony.



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Jeśli nie jesteś jeszcze zaznajomiony z koncepcją passphrase, zapraszam do zapoznania się z tym obszernym samouczkiem na ten temat:



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

![Image](assets/fr/038.webp)



### 5.8 Zapisywanie seed w formacie QR (*SeedQR*)



SeedSigner umożliwia przekształcenie seed w papierowy kod QR o nazwie *SeedQR*. Ta metoda upraszcza ładowanie wallet, ponieważ pozwala uniknąć ręcznego wpisywania każdego słowa.



Aby to zrobić, będziesz potrzebować pustego papieru lub metalowego kodu QR odpowiadającego długości frazy mnemonicznej. Jeśli zakupiłeś kompletny pakiet SeedSigner, szablony są zazwyczaj dołączone. Jeśli nie, możesz je pobrać i wydrukować (lub odtworzyć ręcznie) tutaj :




- [format 12 słów](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)
- [format 24 słowa](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_29x29.pdf)
- [Kompaktowy format 12 słów](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_21x21.pdf)
- [Kompaktowy format 24 słowa](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)



Na ekranie seed wybierz opcję `Backup Seed`.



![Image](assets/fr/039.webp)



Następnie wybierz `Export as SeedQR`.



![Image](assets/fr/040.webp)



Następnie wybierz żądany format (normalny lub kompaktowy) zgodnie z dostępnym szablonem papieru.



![Image](assets/fr/041.webp)



Kliknij `Begin`, aby rozpocząć tworzenie *SeedQR*. SeedSigner wyświetli następnie serię siatek (A1, A2, B1 itd.), z których każda odpowiada części kodu.



![Image](assets/fr/042.webp)



Starannie odtwórz każdą czarną kropkę na arkuszu zapisu, a następnie użyj joysticka, aby przejść do następnego bloku. Nie spiesz się: zwykłe niedopasowanie może sprawić, że kod QR będzie bezużyteczny.



Kilka wskazówek:




- Zacznij od ołówka, aby móc poprawić ewentualne błędy, a po zakończeniu wróć do cienkiego czarnego długopisu;
- Wystarczy dobrze wyśrodkowany punkt na środku kwadratu, nie trzeba go całkowicie wypełniać.



![Image](assets/fr/043.webp)



Następnie kliknij `Confirm SeedQR` i zeskanuj swój kod QR, aby sprawdzić, czy działa poprawnie.



![Image](assets/fr/044.webp)



Jeśli wyświetlony zostanie komunikat `Success`, *SeedQR* jest prawidłowy: można przejść do następnego kroku.



![Image](assets/fr/045.webp)



**Zachowaj ten arkusz tak ściśle, jak frazę odzyskiwania. Każdy, kto jest w posiadaniu tego kodu QR, może zrekonstruować twoje klucze prywatne i ukraść twoje bitcoiny



Gratulacje, Twoje portfolio Bitcoin jest już gotowe i działa! Teraz zaimportujemy jego publiczne komponenty do **Sparrow Wallet**, aby łatwo nim zarządzać.



## 6. Import wallet do Sparrow



Po skonfigurowaniu SeedSigner i prawidłowym wygenerowaniu i zapisaniu seed, następnym krokiem jest połączenie tego portfela z oprogramowaniem do zarządzania, takim jak Sparrow Wallet. Twój seed zawsze pozostanie offline, ponieważ tylko publiczna część portfela zostanie przesłana do Sparrow. Umożliwi to oprogramowaniu wyświetlanie adresów, transakcji i tworzenie nowych transakcji, bez możliwości wydawania bitcoinów. Aby wydać swoje bitcoiny, SeedSigner zawsze będzie musiał podpisać transakcję przygotowaną przez Sparrow.



### 6.1 Przygotowanie SeedSigner



Włóż kartę microSD zawierającą system operacyjny, włącz SeedSigner, a następnie załaduj seed, który właśnie utworzyłeś z zapasowego kodu QR. Na ekranie głównym wybierz `Scan`, a następnie zeskanuj SeedQR za pomocą SeedSigner.



![Image](assets/fr/046.webp)



Sprawdź, czy odcisk palca na kluczu głównym jest zgodny z odciskiem palca na wallet. Jeśli używasz passphrase, wprowadź go na tym etapie.



![Image](assets/fr/047.webp)



Spowoduje to przejście do menu portfolio, w moim przypadku o nazwie `d4149b27`. Jeśli wrócisz do ekranu głównego, wybierz `Seeds`, a następnie wybierz wydruk odpowiadający twojemu portfolio. Następnie kliknij `Export Xpub`.



![Image](assets/fr/048.webp)



Wybierz typ portfela. W naszym przypadku jest to pojedynczy portfel: wybierz `Single Sig`.



![Image](assets/fr/049.webp)



Następnym krokiem jest wybór standardu skryptowego. Najnowszym i najbardziej ekonomicznym pod względem kosztów transakcyjnych jest `Taproot`. Dlatego radzę wybrać ten standard.



![Image](assets/fr/050.webp)



Pojawi się komunikat ostrzegawczy. To normalne: ten rozszerzony klucz publiczny (`xpub`) umożliwia wyświetlenie wszystkich adresów pochodzących z seed (na pierwszym koncie). Nie pozwala na wydawanie środków, ale ujawnia strukturę portfela. Jeśli kiedykolwiek wycieknie, będzie to problem dla twojej prywatności, ale nie dla bezpieczeństwa twoich bitcoinów: pozwala ci je zobaczyć, ale nie wydać.



Kliknij `I Understand`, a następnie `Export Xpub`, jeśli jesteś zadowolony z wyświetlanych informacji.



Następnie SeedSigner generuje xpub w postaci dynamicznego kodu QR zawierającego wszystkie dane potrzebne do zarządzania portfelem w Sparrow Wallet.



![Image](assets/fr/051.webp)



Za pomocą joysticka można dostosować jasność ekranu w celu łatwiejszego skanowania kodów QR.



### 6.2 Importowanie nowego portfela do Sparrow Wallet



Upewnij się, że masz zainstalowane oprogramowanie Sparrow Wallet na swoim komputerze. Jeśli nie wiesz, jak prawidłowo pobrać, sprawdzić i zainstalować oprogramowanie, zapoznaj się z naszym pełnym samouczkiem na ten temat:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Na komputerze otwórz Sparrow Wallet, a następnie na pasku menu kliknij `File → Import Wallet`.



![Image](assets/fr/052.webp)



Przewiń w dół do `SeedSigner`, a następnie wybierz `Scan...`. Otworzy się kamera internetowa: zeskanuj dynamiczny kod QR wyświetlany na ekranie SeedSigner.



![Image](assets/fr/053.webp)



Przypisz nazwę do swojego portfela, a następnie kliknij `Create Wallet`. Sparrow poprosi o ustawienie hasła, aby zablokować lokalny dostęp do wallet. Wybierz silne hasło: chroni ono dostęp do danych portfela w Sparrow (klucze publiczne, adresy, etykiety i historia transakcji). To hasło nie jest potrzebne do przywrócenia portfela w późniejszym terminie: do tego celu wymagana jest tylko fraza mnemoniczna (i ewentualnie passphrase).



Zalecam zapisanie tego hasła w menedżerze haseł, aby uniknąć jego utraty.



![Image](assets/fr/054.webp)



Twój magazyn kluczy został pomyślnie zaimportowany.



![Image](assets/fr/055.webp)



Następnie sprawdź, czy `Master fingerprint` wyświetlany w Sparrow jest zgodny z tym, który został wcześniej zarejestrowany w SeedSigner.



SeedSigner i Sparrow Wallet są teraz bezpiecznie połączone. Sparrow działa jako kompletny interfejs zarządzania, podczas gdy SeedSigner pozostaje jedynym urządzeniem zdolnym do podpisywania transakcji. Jesteś teraz gotowy do odbierania i wysyłania bitcoinów w całkowicie hermetycznej konfiguracji.



## 7. Odbieranie i wysyłanie bitcoinów



Twój SeedSigner i Sparrow Wallet są teraz skonfigurowane do współpracy. W tej ostatniej sekcji przyjrzymy się, jak odbierać i wysyłać bitcoiny przy użyciu tej konfiguracji.



### 7.1 Otrzymywanie bitcoinów



#### 7.1.1 Generowanie adresu odbioru



Na komputerze otwórz Sparrow Wallet i odblokuj SeedSigner wallet za pomocą hasła. Upewnij się, że oprogramowanie jest połączone z serwerem (wycięcie w prawym dolnym rogu). Na pasku bocznym kliknij `Odbierz`.



![Image](assets/fr/056.webp)



Wyświetlony zostanie nowy adres Bitcoin. Wyświetli się :




- Adres tekstowy (zaczynający się od `bc1p...`, jeśli używasz P2TR, tak jak ja),
- Odpowiedni kod QR,
- Pole `Label` do śledzenia transakcji.



Zdecydowanie zalecam dodanie etykiety do każdego paragonu bitcoinów na wallet. Pozwoli to łatwo zidentyfikować pochodzenie każdego UTXO i usprawni zarządzanie prywatnością. Aby zagłębić się w ten ważny temat, możesz zapoznać się z dedykowanym szkoleniem w Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Aby dodać etykietę, wystarczy wpisać nazwę w polu `Label`, a następnie potwierdzić.



Na przykład:



```txt
Label : Sale of the Raspberry Pi Zero
```



Twój adres jest teraz powiązany z tą etykietą we wszystkich sekcjach Sparrow.



![Image](assets/fr/057.webp)



#### 7.1.2 Weryfikacja Address na urządzeniu SeedSigner



Przed udostępnieniem adresu odbiorczego bardzo ważne jest sprawdzenie, czy należy on do seed. Ten krok gwarantuje, że SeedSigner będzie mógł podpisywać transakcje powiązane z tym adresem. Chroni to również przed możliwymi atakami, w których Sparrow wyświetla fałszywy adres. Pamiętaj, że Sparrow działa w niezabezpieczonym środowisku (na Twoim komputerze), które ma znacznie większą powierzchnię ataku niż Twój SeedSigner, który jest całkowicie odizolowany. Dlatego nigdy nie należy ślepo wierzyć adresom odbiorczym prezentowanym na Sparrow, dopóki nie zweryfikuje się ich za pomocą sprzętu wallet.



W Sparrow kliknij kod QR adresu, aby go powiększyć: zostanie on wyświetlony na pełnym ekranie.



![Image](assets/fr/058.webp)



W aplikacji SeedSigner z menu głównego wybierz opcję `Scan`. Zeskanuj kod QR wyświetlony na ekranie komputera, a następnie wybierz seed odpowiadający wallet (w moim przypadku odcisk palca `d4149b27`).



![Image](assets/fr/059.webp)



Jeśli zeskanowany adres jest zgodny z adresem uzyskanym z seed, na ekranie SeedSigner zostanie wyświetlony komunikat: `Address Verified`.



![Image](assets/fr/060.webp)



Potwierdza to, że adres należy do wallet i że można z niego bezpiecznie otrzymywać bitcoiny.



#### 7.1.3 Otrzymanie środków



Możesz teraz przekazać ten adres (w formie tekstu lub kodu QR) osobie lub działowi, który musi wysłać Ci dane. Gdy transakcja zostanie rozesłana w sieci, pojawi się w zakładce "Transakcje" w Sparrow Wallet.



![Image](assets/fr/061.webp)



### 7.2 Wyślij bitcoiny



Wysyłanie bitcoinów za pomocą SeedSigner to 3-etapowy proces:




- Tworzenie transakcji w Sparrow ;
- Podpis transakcji na SeedSigner ;
- Ostateczna dystrybucja transakcji za pośrednictwem Sparrow.



Wszystkie wymiany między tymi dwoma urządzeniami odbywają się wyłącznie za pomocą kodów QR.



#### 7.2.1 Tworzenie transakcji w Sparrow



W Sparrow Wallet można kliknąć na zakładkę `Send` w lewym pasku bocznym. Ja jednak wolę korzystać z zakładki `UTXOs`, która pozwala ćwiczyć "*Coin Control*". Ta metoda zapewnia precyzyjną kontrolę nad używanymi UTXO, dzięki czemu można kontrolować informacje ujawniane podczas transakcji.



W zakładce `UTXOs` wybierz monety, które chcesz wydać, a następnie kliknij `Send Selected`.



![Image](assets/fr/062.webp)



Następnie wypełnij pola transakcji:




- W `Pay to` wklej adres odbiorcy lub kliknij ikonę aparatu, aby zeskanować kod QR;
- W polu `Label` dodaj etykietę, aby śledzić ten wydatek;
- W polu `Amount` wprowadź kwotę do wysłania;
- Na koniec należy wybrać stawkę opłaty w oparciu o aktualne warunki rynkowe (szacunki są dostępne na stronie [mempool.space](https://mempool.space/)).



Po wypełnieniu pól, sprawdź dokładnie informacje, a następnie kliknij `Twórz transakcję >>`.



![Image](assets/fr/063.webp)



Sprawdź szczegóły transakcji, aby upewnić się, że wszystko się zgadza, a następnie kliknij `Finalize Transaction for Signing`.



![Image](assets/fr/064.webp)



Transakcja jest gotowa, ale nie została jeszcze podpisana. Aby wyświetlić [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) jako kod QR, kliknij `Pokaż QR`.



![Image](assets/fr/065.webp)



#### 7.2.2 Podpisywanie transakcji za pomocą SeedSigner



Włącz SeedSigner i zeskanuj SeedQR, aby uzyskać dostęp do portfela, jak zwykle. Na ekranie głównym wybierz `Scan`, a następnie zeskanuj kod QR wyświetlony na Sparrow.



![Image](assets/fr/066.webp)



Następnie wybierz model seed pasujący do Twojego portfolio.



![Image](assets/fr/067.webp)



SeedSigner automatycznie wykrywa, że jest to PSBT i wyświetla podsumowanie transakcji:




   - Wysłana kwota,
   - Adresy wyjściowe,
   - Powiązane koszty transakcyjne.



Kliknij `Review Details` i dokładnie sprawdź wszystkie informacje bezpośrednio na ekranie SeedSigner. Najważniejsze elementy do sprawdzenia to wysłana kwota, adres odbiorcy i kwota naliczonych opłat.



![Image](assets/fr/068.webp)



Jeśli wszystko się zgadza, wybierz `Approve PSBT`, aby podpisać transakcję przy użyciu odpowiednich kluczy prywatnych.



![Image](assets/fr/069.webp)



Po podpisaniu SeedSigner generuje nowy kod QR zawierający podpisaną transakcję, gotowy do zeskanowania przez Sparrow.



![Image](assets/fr/070.webp)



#### 7.2.3 Transmisja transakcji z Sparrow



Teraz, gdy transakcja jest ważna, należy ją rozgłosić w sieci Bitcoin, aby dotarła do górnika, który doda ją do bloku.



W Sparrow kliknij przycisk `QR Scan`.



![Image](assets/fr/071.webp)



Przedstaw kod QR wyświetlony przez SeedSigner (kod podpisanej transakcji) kamerze internetowej. Sparrow zdekoduje podpis i wyświetli pełne szczegóły transakcji. Sprawdź, czy wszystkie informacje są prawidłowe, a następnie kliknij przycisk Broadcast Transaction, aby rozgłosić transakcję w sieci Bitcoin.



![Image](assets/fr/072.webp)



Twoja transakcja została wysłana do sieci Bitcoin. Możesz śledzić jej postęp w zakładce `Transakcje` w Sparrow Wallet.



![Image](assets/fr/073.webp)



Opanowałeś już podstawy korzystania z SeedSigner. Aby pogłębić swoją wiedzę i poznać bardziej zaawansowane zastosowania, zapraszam do zapoznania się z poniższym samouczkiem:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

**[Możesz również wesprzeć rozwój projektu open-source SeedSigner, przekazując darowiznę w bitcoinach!](https://seedsigner.com/donate/)**



*Kredyt: niektóre obrazy w tym samouczku pochodzą z [oficjalnej strony projektu SeedSigner](https://seedsigner.com/) i [repozytorium GitHub](https://github.com/SeedSigner/seedsigner).*