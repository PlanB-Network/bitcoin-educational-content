---
name: Trezor Model One
description: Konfiguracja i korzystanie z Hardware Wallet Model One
---
![cover](assets/cover.webp)



*Źródło zdjęcia: [Trezor.io](https://trezor.io/)*



Trezor Model One to pierwszy Hardware Wallet w historii, wprowadzony na rynek w 2014 roku przez SatoshiLabs. Po ponad dziesięciu latach istnienia, nadal pozostaje interesującym wyborem, szczególnie dla użytkowników poszukujących Hardware Wallet, który jest dostępny zarówno pod względem technicznym, jak i budżetowym. W rzeczywistości jego cena na oficjalnej stronie Trezor wynosi 49 euro. Jest to jeden z niewielu portfeli sprzętowych w tym przedziale cenowym. Znajduje się w połowie drogi między urządzeniami klasy podstawowej za około 20 euro, takimi jak Tapsigner, które często nie mają ekranu, a urządzeniami średniej klasy za około 80 euro, takimi jak Ledger Nano S Plus lub Trezor Safe 3.



Model One posiada monochromatyczny wyświetlacz OLED o przekątnej 0,96 cala i dwa fizyczne przyciski. Działa bez baterii, wykorzystując jedynie połączenie micro-USB do zasilania i transmisji danych Exchange.



![Image](assets/fr/01.webp)



Główną wadą Model One jest brak Secure Element, co czyni go podatnym na różne ataki fizyczne, z których niektóre są stosunkowo proste do wykonania. Ataki te mogą obejmować analizę kanałów pomocniczych w celu określenia kodu PIN urządzenia lub bardziej zaawansowane techniki wyodrębniania zaszyfrowanego seed w celu jego późniejszego brutalnego wymuszenia. Należy pamiętać, że ataki te wymagają fizycznego dostępu do urządzenia. Podatność tę można jednak znacznie zmniejszyć, stosując solidny passphrase BIP39. Jeśli zdecydujesz się na Hardware Wallet, zdecydowanie zalecam skonfigurowanie passphrase.



Model One oferuje dwie ważne zalety:




- Jest on oparty na całkowicie otwartej architekturze. W przeciwieństwie do nowszych modeli z Secure Element, wszystkie komponenty sprzętowe i programowe Model One są audytowalne;
- Jest on wyposażony w ekran. Według mojej wiedzy jest to jedyny Hardware Wallet na rynku w tym przedziale cenowym z wyświetlaczem. Jest to bardzo ważna cecha, ponieważ umożliwia weryfikację podpisanych informacji i adresów odbioru, zapobiegając w ten sposób wielu atakom cyfrowym.



Trezor Model One może zatem stanowić mądry wybór dla początkujących i średnio zaawansowanych użytkowników z ograniczonym budżetem. Należy jednak pamiętać o jego ograniczeniach w zakresie ochrony fizycznej, ze względu na brak Secure Element. Jeśli masz ograniczony budżet, jest to dobra opcja, ale jeśli możesz sobie pozwolić na wybór lepszego modelu, takiego jak Trezor Safe 3 w cenie 79 euro, jest to lepsze rozwiązanie, ponieważ zawiera Secure Element.



## Unboxing Trezor Model One



Po otrzymaniu urządzenia Model One należy upewnić się, że pudełko i Seal są nienaruszone, aby potwierdzić, że opakowanie nie było otwierane. Podczas późniejszej konfiguracji zostanie również przeprowadzona programowa weryfikacja autentyczności i integralności urządzenia.



Zawartość pudełka obejmuje :




- Trezor Model One;
- Karton do zapisania frazy Mnemonic, naklejki i instrukcje;
- Kabel USB-A do micro-USB.



![Image](assets/fr/02.webp)



Nawigacja po urządzeniu jest bardzo prosta:




- Kliknij prawym przyciskiem myszy, aby potwierdzić i przejść do kolejnych kroków;
- Użyj lewego przycisku, aby wrócić.



## Wymagania wstępne



W tym samouczku pokażę, jak używać Trezor Model One z [oprogramowaniem do zarządzania portfelem Sparrow Wallet] (https://sparrowwallet.com/download/). Jeśli jeszcze nie zainstalowałeś tego oprogramowania, zrób to teraz. Jeśli potrzebujesz pomocy, mamy również szczegółowy samouczek dotyczący konfiguracji Sparrow Wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Potrzebne będzie również oprogramowanie Trezor Suite, aby skonfigurować Model One, sprawdzić jego autentyczność i zainstalować firmware. Będziemy używać tego oprogramowania tylko do tego celu, a później będzie ono potrzebne tylko do aktualizacji oprogramowania układowego. Do codziennego zarządzania Wallet będziemy używać wyłącznie Sparrow Wallet, ponieważ jest on zoptymalizowany pod kątem Bitcoin i łatwy w użyciu, nawet dla początkujących (Sparrow obsługuje tylko Bitcoin, a nie altcoiny).



[Pobierz Trezor Suite z oficjalnej strony internetowej](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



W przypadku obu tych programów zdecydowanie zalecam sprawdzenie zarówno ich autentyczności (za pomocą GnuPG), jak i integralności (za pomocą Hash) przed zainstalowaniem ich na komputerze. Jeśli nie wiesz jak to zrobić, możesz skorzystać z tego poradnika:



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Uruchamianie Trezor Model One



Podłącz urządzenie Model One do komputera, na którym zainstalowano już oprogramowanie Trezor Suite i Sparrow Wallet.



![Image](assets/fr/04.webp)



Otwórz Trezor Suite, a następnie kliknij "*Setup my Trezor*".



![Image](assets/fr/05.webp)



Wybierz "*Bitcoin-only firmware*", a następnie kliknij "*Install Bitcoin-only*".



![Image](assets/fr/06.webp)



Następnie Trezor Suite zainstaluje oprogramowanie sprzętowe w modelu One. Należy poczekać podczas instalacji.



![Image](assets/fr/07.webp)



Kliknij "*Kontynuuj*".



![Image](assets/fr/08.webp)



## Tworzenie portfela Bitcoin



W Trezor Suite kliknij przycisk "*Utwórz nowy Wallet*".



![Image](assets/fr/09.webp)



Zaakceptuj warunki użytkowania Hardware Wallet.



![Image](assets/fr/10.webp)



W Trezor Suite kliknij "*Kontynuuj tworzenie kopii zapasowej*".



![Image](assets/fr/11.webp)



Oprogramowanie zawiera instrukcje dotyczące zarządzania frazą Mnemonic.



Mnemonic zapewnia pełny, nieograniczony dostęp do wszystkich bitcoinów. Każdy, kto jest w posiadaniu tej frazy, może ukraść twoje fundusze, nawet bez fizycznego dostępu do Trezor Model One.



24-wyrazowa fraza przywraca dostęp do bitcoinów w przypadku utraty, kradzieży lub uszkodzenia Hardware Wallet. Dlatego bardzo ważne jest, aby zapisać go ostrożnie i przechowywać w bezpiecznym miejscu.



Napis można umieścić na kartonie dołączonym do pudełka lub, dla większego bezpieczeństwa, zalecam wygrawerowanie go na podstawie ze stali nierdzewnej, aby chronić go przed pożarem, powodzią lub upadkiem.



Potwierdź instrukcje, a następnie kliknij przycisk "*Twórz kopię zapasową Wallet*".



![Image](assets/fr/12.webp)



Model One utworzy frazę Mnemonic przy użyciu generatora liczb losowych. Upewnij się, że nie jesteś obserwowany podczas tej operacji. Zapisz słowa wyświetlone na ekranie na wybranym nośniku fizycznym. W zależności od strategii bezpieczeństwa możesz rozważyć wykonanie kilku pełnych fizycznych kopii frazy (ale przede wszystkim nie dziel jej). Ważne jest, aby słowa były ponumerowane i ułożone w kolejności.



***Oczywiście nigdy nie wolno udostępniać tych słów w Internecie, tak jak robię to w tym samouczku. Ten przykład Wallet będzie używany tylko na Testnet i zostanie usunięty po zakończeniu samouczka



Aby uzyskać więcej informacji na temat prawidłowego sposobu zapisywania i zarządzania frazą Mnemonic, zdecydowanie polecam skorzystanie z tego samouczka, zwłaszcza jeśli jesteś początkującym:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Aby przejść do kolejnych słów, kliknij prawym przyciskiem myszy. Po zapisaniu wszystkich słów, ponownie kliknij prawym przyciskiem myszy, aby przejść do następnego kroku.



![Image](assets/fr/13.webp)



Hardware Wallet ponownie pokazuje wszystkie słowa. Sprawdź, czy wszystkie zostały zapisane.



![Image](assets/fr/14.webp)



## Ustawianie kodu PIN



Następnie należy wprowadzić kod PIN. Kod PIN odblokowuje urządzenie Trezor. Zapewnia on zatem ochronę przed nieautoryzowanym dostępem fizycznym. Kod PIN nie bierze udziału w tworzeniu kluczy kryptograficznych Wallet. Tak więc nawet bez dostępu do kodu PIN, posiadanie 12-wyrazowej frazy Mnemonic umożliwi odzyskanie dostępu do bitcoinów.



W Trezor Suite kliknij przycisk "*Kontynuuj PIN*", a następnie przycisk "*Ustaw PIN*".



![Image](assets/fr/15.webp)



Potwierdź na Modelu One.



![Image](assets/fr/16.webp)



Zalecamy wybranie możliwie losowego kodu PIN. Kod ten należy zapisać w miejscu innym niż miejsce przechowywania urządzenia Trezor (np. w menedżerze haseł). Można zdefiniować kod PIN składający się z od 8 do 50 cyfr. Zalecam wybranie jak najdłuższego kodu PIN w celu zwiększenia bezpieczeństwa.



Kod PIN należy wprowadzić w programie Trezor Suite na komputerze, klikając kropki odpowiadające cyfrom, zgodnie z konfiguracją klawiatury wyświetlaną na urządzeniu Trezor Model One.



Ta konkretna metoda wprowadzania kodu PIN jest wymagana za każdym razem, gdy odblokowujesz Trezor Model One, czy to za pomocą Trezor Suite, czy Sparrow Wallet.



![Image](assets/fr/17.webp)



Po zakończeniu kliknij przycisk "*Enter PIN*".



![Image](assets/fr/18.webp)



Wprowadź ponownie kod PIN, aby potwierdzić.



![Image](assets/fr/19.webp)



W Trezor Suite kliknij przycisk "*Complete setup*".



![Image](assets/fr/20.webp)



Konfiguracja urządzenia Model One została zakończona. Jeśli chcesz, możesz zmienić nazwę i stronę główną Hardware Wallet.



![Image](assets/fr/21.webp)



Nie będziemy już potrzebować oprogramowania Trezor Suite, z wyjątkiem przeprowadzania regularnych aktualizacji oprogramowania układowego na Hardware Wallet lub jeśli chcesz przeprowadzić test odzyskiwania. Do zarządzania portfelem będziemy teraz używać Sparrow, ponieważ oprogramowanie to doskonale nadaje się do użytku wyłącznie z Bitcoin.



## Konfiguracja portfela na Sparrow Wallet



Zacznij od pobrania i zainstalowania Sparrow Wallet [z oficjalnej strony internetowej] (https://sparrowwallet.com/) na swoim komputerze, jeśli jeszcze tego nie zrobiłeś.



Po otwarciu Sparrow Wallet upewnij się, że oprogramowanie jest podłączone do węzła Bitcoin, który jest oznaczony haczykiem w prawym dolnym rogu Interface. Jeśli masz problemy z podłączeniem Sparrow, zalecam zapoznanie się z początkiem tego samouczka:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Kliknij zakładkę "*File*", a następnie "*New Wallet*".



![Image](assets/fr/22.webp)



Nazwij swoje portfolio, a następnie kliknij "*Twórz Wallet*".



![Image](assets/fr/23.webp)



W menu rozwijanym "*Typ skryptu*" wybierz typ skryptu, który zostanie użyty do zabezpieczenia twoich bitcoinów. Zalecam "*Taproot*" lub, jeśli to niemożliwe, "*Native SegWit*".



![Image](assets/fr/24.webp)



Kliknij przycisk "*Connected Hardware Wallet*". Model One musi być oczywiście podłączony do komputera.



![Image](assets/fr/25.webp)



Kliknij przycisk "*Scan*". Powinien pojawić się Twój Model One.



Po podłączeniu Modelu One do komputera z otwartym Sparrow Wallet, zostaniesz poproszony o wprowadzenie passphrase BIP39 w Sparrow. Ta zaawansowana opcja zostanie omówiona w przyszłym samouczku. Na razie można po prostu wybrać opcję "*Toggle passphrase Off*", aby uniemożliwić Trezorowi wyświetlanie monitu o wprowadzenie passphrase przy każdym uruchomieniu.



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

![Image](assets/fr/26.webp)



Kliknij na "*Import Keystore*".



![Image](assets/fr/27.webp)



Możesz teraz zobaczyć szczegóły swojego Wallet, w tym rozszerzony klucz publiczny swojego pierwszego konta. Kliknij przycisk "*Zastosuj*", aby sfinalizować tworzenie Wallet.



![Image](assets/fr/28.webp)



Wybierz silne hasło, aby zabezpieczyć dostęp do Sparrow Wallet. Hasło to zapewni bezpieczny dostęp do danych Sparrow Wallet, chroniąc klucze publiczne, adresy, etykiety i historię transakcji przed nieautoryzowanym dostępem.



Radzę zapisać to hasło w menedżerze haseł, aby go nie zapomnieć.



![Image](assets/fr/29.webp)



A teraz Twoje portfolio zostało zaimportowane do Sparrow Wallet!



![Image](assets/fr/30.webp)



Przed otrzymaniem pierwszych bitcoinów w Wallet, **zalecam wykonanie testu odzyskiwania pustego urządzenia**. Zapisz informacje referencyjne, takie jak xpub, a następnie zresetuj Trezor Model One, gdy Wallet jest nadal pusty. Następnie spróbuj przywrócić Wallet na Trezorze przy użyciu papierowych kopii zapasowych. Sprawdź, czy xpub wygenerowany po przywróceniu jest zgodny z pierwotnie zapisanym. Jeśli tak, możesz mieć pewność, że papierowe kopie zapasowe są niezawodne.



Aby dowiedzieć się więcej o tym, jak wykonać test odzyskiwania, proponuję zapoznać się z tym innym samouczkiem:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Jak odbierać bitcoiny za pomocą Trezor Model One?



W aplikacji Sparrow kliknij zakładkę "*Odbierz*".



![Image](assets/fr/31.webp)



Przed użyciem Address proponowanego przez Sparrow Wallet, należy sprawdzić go na ekranie Trezora. Ta praktyka pozwala potwierdzić, że Address wyświetlany na Sparrow nie jest fałszywy i że Hardware Wallet rzeczywiście posiada klucz prywatny potrzebny do późniejszego wydania bitcoinów zabezpieczonych tym Address. Pomaga to uniknąć kilku rodzajów ataków.



Aby wykonać to sprawdzenie, kliknij przycisk "*Wyświetl Address*".



![Image](assets/fr/32.webp)



Sprawdź, czy Address wyświetlany na twoim Trezorze zgadza się z tym na Sparrow Wallet. Zaleca się również przeprowadzenie tego sprawdzenia tuż przed przekazaniem Address do nadawcy, aby upewnić się co do jego ważności. Możesz nacisnąć prawy przycisk, aby potwierdzić.



![Image](assets/fr/33.webp)



Możesz również dodać "*Label*", aby opisać źródło bitcoinów, które będą zabezpieczone tym Address. Jest to dobra praktyka, która pozwala lepiej zarządzać UTXO.



![Image](assets/fr/34.webp)



Następnie można użyć Address do otrzymywania bitcoinów.



![Image](assets/fr/35.webp)



## Jak wysyłać bitcoiny za pomocą Trezor Model One?



Teraz, gdy otrzymałeś swoje pierwsze Satss w zabezpieczonym Modelu One Wallet, możesz je również wydać! Podłącz Trezor do komputera, uruchom Sparrow Wallet, a następnie przejdź do zakładki "*Wyślij*", aby utworzyć nową transakcję.



![Image](assets/fr/36.webp)



Jeśli chcesz *Coin Control*, czyli wybrać konkretnie, które UTXO mają zostać wykorzystane w transakcji, przejdź do zakładki "*UTXOs*". Wybierz UTXO, które chcesz wydać, a następnie kliknij "*Wyślij wybrane*". Nastąpi przekierowanie do tego samego ekranu w zakładce "*Wyślij*", ale z UTXO już wybranymi do transakcji.



![Image](assets/fr/37.webp)



Wprowadź docelowy adres Address. Można również wprowadzić wiele adresów, klikając przycisk "*+ Add*".



![Image](assets/fr/38.webp)



Zapisz "*Label*", aby zapamiętać cel tego wydatku.



![Image](assets/fr/39.webp)



Wybierz kwotę, która ma zostać wysłana do tego Address.



![Image](assets/fr/40.webp)



Dostosuj stawkę opłaty za transakcję do aktualnej sytuacji rynkowej. Na przykład można użyć [Mempool.space](https://Mempool.space/), aby wybrać odpowiednią stawkę opłaty.



Upewnij się, że wszystkie parametry transakcji są prawidłowe, a następnie kliknij "*Twórz transakcję*".



![Image](assets/fr/41.webp)



Jeśli wszystko jest w porządku, kliknij "*Finalizuj transakcję do podpisu*".



![Image](assets/fr/42.webp)



Kliknij "*Podpisz*".



![Image](assets/fr/43.webp)



Kliknij "*Zapisz*" obok swojego Trezor Model One.



![Image](assets/fr/44.webp)



Sprawdź parametry transakcji na ekranie Hardware Wallet, w tym odbiorcę Address, wysłaną kwotę i opłatę. Po zweryfikowaniu transakcji na urządzeniu Trezor kliknij prawym przyciskiem myszy, aby ją podpisać.



![Image](assets/fr/45.webp)



Transakcja jest teraz podpisana. Sprawdź ostatni raz, czy wszystko jest w porządku, a następnie kliknij "*Broadcast Transaction*", aby rozgłosić ją w sieci Bitcoin.



![Image](assets/fr/46.webp)



Można ją znaleźć w zakładce "*Transakcje*" w Sparrow Wallet.



![Image](assets/fr/47.webp)



Gratulacje, jesteś teraz na bieżąco z podstawową obsługą Trezor Model One z Sparrow Wallet! Aby pójść o krok dalej, polecam ten obszerny samouczek dotyczący korzystania z Hardware Wallet Trezor z passphrase BIP39 w celu zwiększenia bezpieczeństwa:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Jeśli ten poradnik okazał się przydatny, będę wdzięczny za pozostawienie poniżej kciuka Green. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dziękuję bardzo!