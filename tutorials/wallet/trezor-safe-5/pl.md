---
name: Trezor Safe 5
description: Konfigurowanie i używanie Hardware Wallet Safe 5
---
![cover](assets/cover.webp)



*Źródło zdjęcia: [Trezor.io](https://trezor.io/)*



Trezor Safe 5 to Hardware Wallet najnowszej generacji zaprojektowany przez SatoshiLabs i wprowadzony na rynek w 2024 roku. Jest pozycjonowany jako wysokiej klasy wersja Safe 3, z naciskiem na ergonomię i trwałość. Korzysta z tych samych postępów w zakresie bezpieczeństwa, co jego poprzednik, Safe 3, w porównaniu z Model One i Model T.



Wyceniony na 169 euro, Safe 5 jest pozycjonowany w kategorii high-end Hardware Wallet, konkurując z takimi modelami jak Coldcard, Ledger Nano X i Flex, Jade Plus, Passport i Bitbox.



Safe 5 wyróżnia się 1,54-calowym kolorowym ekranem dotykowym, chronionym przez *Gorilla Glass 3*, który jest odporny na wstrząsy i zarysowania. Jest również wyposażony w silnik haptyczny *Trezor Touch*, który emituje niewielkie wibracje po dotknięciu. Podobnie jak Safe 3, zawiera Secure Element i działa za pośrednictwem połączenia USB-C, z dodatkiem portu Micro SD.



Główna różnica między Safe 3 i Safe 5 polega na jakości urządzenia, poza aspektami bezpieczeństwa. Znacznie poprawia wrażenia użytkownika, dzięki płynniejszej pracy i wygodniejszemu ekranowi. Pod względem bezpieczeństwa są one równoważne.



![Image](assets/fr/01.webp)



Safe 5 ma wszystkie podstawowe funkcje, których można oczekiwać od dobrego Hardware Wallet, w tym doskonałą integrację passphrase BIP39. Nie obsługuje jednak jeszcze Miniscript.



Model ten jest szczególnie odpowiedni dla początkujących i średnio zaawansowanych użytkowników. Z drugiej strony, może on nie spełniać wszystkich oczekiwań zaawansowanych użytkowników poszukujących bardziej szczegółowych funkcji dostępnych w urządzeniach takich jak Coldcard. Niemniej jednak, jeśli nie potrzebujesz tych zaawansowanych opcji, Trezor Safe 5 może być doskonałym wyborem.



## Model bezpieczeństwa Trezor Safe 5



Podobnie jak Safe 3, Trezor Safe 5 jest wyposażony w **Secure Element** z certyfikatem EAL6+, co stanowi znaczący postęp w stosunku do wcześniejszych modeli, takich jak Model One i Model T. Jest to chip OPTIGA Trust M V3, który nie przechowuje bezpośrednio seed, ale działa jako komponent kryptograficzny w celu zabezpieczenia dostępu do niego. Secure Element przechowuje sekret, do którego można uzyskać dostęp dopiero po prawidłowym wprowadzeniu kodu PIN przez użytkownika. Sekret ten jest następnie wykorzystywany do odszyfrowania seed, który jest przechowywany zaszyfrowany w pamięci głównej urządzenia.



Ten hybrydowy system bezpieczeństwa zapewnia lepszą ochronę fizyczną, zwłaszcza przed atakami ekstrakcyjnymi lub inwazyjną analizą, na które podatny był Model One, szczególnie w zakresie zarządzania kodami PIN. Luki te są teraz omijane dzięki zastosowaniu Secure Element. Model ten zachowuje również architekturę oprogramowania open-source: kod zarządzający generowaniem i używaniem kluczy prywatnych pozostaje w pełni dostępny i weryfikowalny. Chip OPTIGA zarządza tylko kodem PIN, elementem zewnętrznym w stosunku do zarządzania kluczami Bitcoin Wallet. Jest on ograniczony do ujawnienia sekretu, który może być użyty do odszyfrowania seed. Ponadto chip OPTIGA Trust M V3 korzysta ze stosunkowo wolnej licencji, która upoważnia SatoshiLabs do swobodnego publikowania potencjalnych luk w zabezpieczeniach (NDA-Free).



Ten model bezpieczeństwa stanowi moim zdaniem jeden z najlepszych kompromisów dostępnych obecnie na rynku. Łączy w sobie zalety Secure Element z zarządzaniem oprogramowaniem open-source. Wcześniej użytkownicy musieli wybierać między zwiększonym bezpieczeństwem fizycznym dzięki chipowi a przejrzystością dzięki oprogramowaniu open-source; dzięki Trezor Safe możliwe jest skorzystanie z obu.



W tym samouczku dowiesz się, jak bezpiecznie skonfigurować i używać Trezor Safe 5.



## Unboxing Trezor Safe 5



Po otrzymaniu urządzenia Safe 5 należy upewnić się, że pudełko i Seal są nienaruszone, aby potwierdzić, że opakowanie nie było otwierane. Oprogramowanie sprawdzi autentyczność i integralność urządzenia podczas jego późniejszej konfiguracji.



Zawartość pudełka obejmuje :




- Trezor Safe 5;
- Etui zawierające karton do zapisania frazy Mnemonic, naklejki i instrukcje;
- Kabel USB-C do USB-C.



Po otwarciu Trezor Safe 5 powinien być zabezpieczony ochronnym plastikiem, a port USB-C powinien być zabezpieczony holograficznym Seal. Upewnij się, że tam jest.



![Image](assets/fr/02.webp)



Nawigacja na urządzeniu jest dość intuicyjna:




- Dotknij dolnej połowy ekranu, aby przejść dalej;
- Przesuń w dół, aby wrócić;
- Naciśnij i przytrzymaj ekran, aby potwierdzić operację.



## Wymagania wstępne



W tym samouczku pokażę, jak korzystać z Trezor Safe 5 z [oprogramowaniem do zarządzania portfelem Sparrow Wallet] (https://sparrowwallet.com/download/). Jeśli jeszcze nie zainstalowałeś tego oprogramowania, zrób to teraz. Jeśli potrzebujesz pomocy, mamy również szczegółowy samouczek dotyczący konfiguracji Sparrow Wallet:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Będziesz także potrzebował oprogramowania Trezor Suite, aby skonfigurować Safe 5, sprawdzić jego autentyczność i zainstalować oprogramowanie układowe. Będziemy używać tego oprogramowania tylko do tego celu, a później będzie ono potrzebne tylko do aktualizacji oprogramowania układowego. Do codziennego zarządzania Wallet będziemy używać wyłącznie Sparrow Wallet, ponieważ jest on zoptymalizowany pod kątem Bitcoin i łatwy w użyciu, nawet dla początkujących (Sparrow obsługuje tylko Bitcoin, a nie altcoiny).



[Pobierz Trezor Suite z oficjalnej strony internetowej](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



W przypadku obu tych programów zdecydowanie zalecam sprawdzenie zarówno ich autentyczności (za pomocą GnuPG), jak i integralności (za pomocą Hash) przed zainstalowaniem ich na komputerze. Jeśli nie wiesz jak to zrobić, możesz skorzystać z tego poradnika:



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Uruchamianie Trezor Safe 5



Podłącz urządzenie Safe 5 do komputera, na którym zainstalowano już oprogramowanie Trezor Suite i Sparrow Wallet.



![Image](assets/fr/04.webp)



Otwórz Trezor Suite, a następnie kliknij "*Setup my Trezor*".



![Image](assets/fr/05.webp)



Wybierz "*Bitcoin-only firmware*", a następnie kliknij "*Install Bitcoin-only*".



![Image](assets/fr/06.webp)



Trezor Suite zainstaluje oprogramowanie sprzętowe na urządzeniu Safe 5. Należy poczekać podczas instalacji.



![Image](assets/fr/07.webp)



Kliknij "*Kontynuuj*".



![Image](assets/fr/08.webp)



Następnie przejdź do testu autentyczności, aby upewnić się, że Hardware Wallet nie jest fałszywy lub naruszony.



![Image](assets/fr/09.webp)



Na urządzeniu Safe 5 naciśnij ekran, aby potwierdzić.



![Image](assets/fr/10.webp)



Jeśli urządzenie Trezor jest autentyczne, w aplikacji Trezor Suite zostanie wyświetlony komunikat z potwierdzeniem.



![Image](assets/fr/11.webp)



Następnie można pominąć okna z podstawowymi instrukcjami obsługi.



![Image](assets/fr/12.webp)



## Tworzenie portfela Bitcoin



W Trezor Suite kliknij przycisk "*Utwórz nowy Wallet*".



![Image](assets/fr/13.webp)



Aby utworzyć standardowy BIP39 Wallet, zacznij od wybrania "*Legacy Wallet backup types*" z rozwijanego menu, a następnie wybierz 12- lub 24-słowową frazę Mnemonic (obecnie zalecane jest 12 słów). Umożliwi to utworzenie klasycznego portfela single-sig. Radzę wybrać tutaj parametry zgodne z BIP39, aby ułatwić wyszukiwanie i uniknąć ograniczenia do określonego środowiska. Aby zakończyć, kliknij "*Utwórz Wallet*".



Jeśli chcesz dowiedzieć się więcej o innych opcjach tworzenia kopii zapasowych dostępnych w Trezorze, w tym o *Multi-share Backup*, polecam zapoznać się z tym samouczkiem:



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e


![Image](assets/fr/14.webp)



Zaakceptuj warunki korzystania z Hardware Wallet.



![Image](assets/fr/15.webp)



Naciśnij i przytrzymaj ekran, aby utworzyć nowe portfolio.



![Image](assets/fr/16.webp)



W Trezor Suite kliknij "*Kontynuuj tworzenie kopii zapasowej*".



![Image](assets/fr/17.webp)



Oprogramowanie zawiera instrukcje dotyczące zarządzania frazą Mnemonic.



Ten Mnemonic zapewnia pełny, nieograniczony dostęp do wszystkich bitcoinów. Każdy, kto jest w posiadaniu tej frazy, może ukraść twoje środki, nawet bez fizycznego dostępu do Trezor Safe 5.



12-wyrazowa fraza przywraca dostęp do bitcoinów w przypadku utraty, kradzieży lub uszkodzenia Hardware Wallet. Dlatego bardzo ważne jest, aby zapisać go ostrożnie i przechowywać w bezpiecznym miejscu.



Napis można umieścić na kartonie dołączonym do pudełka lub, dla większego bezpieczeństwa, zalecam wygrawerowanie go na podstawie ze stali nierdzewnej, aby chronić go przed pożarem, powodzią lub upadkiem.



Potwierdź instrukcje, a następnie kliknij przycisk "*Twórz kopię zapasową Wallet*".



![Image](assets/fr/18.webp)



Safe 5 utworzy frazę Mnemonic przy użyciu generatora liczb losowych. Upewnij się, że nie jesteś obserwowany podczas tej operacji. Zapisz słowa wyświetlone na ekranie na wybranym nośniku fizycznym. W zależności od strategii bezpieczeństwa możesz rozważyć wykonanie kilku pełnych fizycznych kopii frazy (ale przede wszystkim nie dziel jej). Ważne jest, aby słowa były ponumerowane i ułożone w kolejności.



***Oczywiście nigdy nie wolno udostępniać tych słów w Internecie, tak jak robię to w tym samouczku. Ten przykład Wallet będzie używany tylko na Testnet i zostanie usunięty po zakończeniu samouczka



Aby uzyskać więcej informacji na temat prawidłowego sposobu zapisywania i zarządzania frazą Mnemonic, zdecydowanie polecam skorzystanie z tego samouczka, zwłaszcza jeśli jesteś początkującym:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/19.webp)



Aby przejść do kolejnych słów, kliknij na dole ekranu. Możesz cofać się, przesuwając palcem w dół. Po zapisaniu wszystkich słów, przytrzymaj palec na ekranie, aby przejść do następnego kroku.



![Image](assets/fr/20.webp)



Wybierz słowa w swojej frazie Mnemonic zgodnie z ich kolejnością, aby potwierdzić, że zapisałeś je poprawnie.



![Image](assets/fr/21.webp)



Po zakończeniu procedury weryfikacji kliknij ekran, aby kontynuować.



![Image](assets/fr/22.webp)



## Ustawianie kodu PIN



Następnie należy wprowadzić kod PIN. Kod PIN odblokowuje urządzenie Trezor. Zapewnia on zatem ochronę przed nieautoryzowanym dostępem fizycznym. Kod PIN nie bierze udziału w tworzeniu kluczy kryptograficznych Wallet. Tak więc nawet bez dostępu do kodu PIN, posiadanie 12-wyrazowej frazy Mnemonic umożliwi odzyskanie dostępu do bitcoinów.



W Trezor Suite kliknij przycisk "*Kontynuuj PIN*", a następnie przycisk "*Ustaw PIN*".



![Image](assets/fr/23.webp)



Potwierdź za pomocą funkcji Safe 5.



![Image](assets/fr/24.webp)



Zalecamy wybranie możliwie losowego kodu PIN. Kod ten należy zapisać w miejscu innym niż miejsce przechowywania urządzenia Trezor (np. w menedżerze haseł). Można zdefiniować kod PIN składający się z od 8 do 50 cyfr. Zalecam wybranie jak najdłuższego kodu PIN w celu zwiększenia bezpieczeństwa.



Użyj panelu dotykowego, aby wprowadzić kod PIN.



![Image](assets/fr/25.webp)



Po zakończeniu kliknij haczyk Green w prawym dolnym rogu, a następnie potwierdź kod PIN po raz drugi.



![Image](assets/fr/26.webp)



Kod PIN został zarejestrowany.



![Image](assets/fr/27.webp)



W Trezor Suite kliknij przycisk "*Complete setup*".



![Image](assets/fr/28.webp)



Konfiguracja urządzenia Safe 5 została zakończona. Jeśli chcesz, możesz zmienić nazwę i stronę główną Hardware Wallet.



![Image](assets/fr/29.webp)



Nie będziemy już potrzebować oprogramowania Trezor Suite, z wyjątkiem wykonywania regularnych aktualizacji oprogramowania układowego na Hardware Wallet lub jeśli chcesz przeprowadzić test odzyskiwania. Do zarządzania portfelem będziemy teraz używać Sparrow, ponieważ oprogramowanie to doskonale nadaje się do użytku wyłącznie z Bitcoin.



## Konfiguracja portfela na Sparrow Wallet



Zacznij od pobrania i zainstalowania Sparrow Wallet [z oficjalnej strony internetowej] (https://sparrowwallet.com/) na swoim komputerze, jeśli jeszcze tego nie zrobiłeś.



Po otwarciu Sparrow Wallet upewnij się, że oprogramowanie jest podłączone do węzła Bitcoin, który jest oznaczony haczykiem w prawym dolnym rogu Interface. Jeśli masz problemy z połączeniem Sparrow, zalecam zapoznanie się z początkiem tego samouczka:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Kliknij zakładkę "*File*", a następnie "*New Wallet*".



![Image](assets/fr/30.webp)



Nazwij swoje portfolio, a następnie kliknij "*Utwórz Wallet*".



![Image](assets/fr/31.webp)



W menu rozwijanym "*Typ skryptu*" wybierz typ skryptu, który zostanie użyty do zabezpieczenia twoich bitcoinów. Zalecam "*Taproot*" lub, jeśli to niemożliwe, "*Native SegWit*".



![Image](assets/fr/32.webp)



Kliknij przycisk "*Connected Hardware Wallet*". Urządzenie Safe 5 musi być oczywiście podłączone do komputera i odblokowane.



Po podłączeniu urządzenia Safe 5 do komputera z otwartym urządzeniem Sparrow Wallet, na ekranie Hardware Wallet zostanie wyświetlony monit o wprowadzenie kodu passphrase BIP39. Ta zaawansowana opcja zostanie omówiona w przyszłym samouczku. Na razie możesz po prostu kliknąć na haczyk Green w prawym górnym rogu, aby potwierdzić, że chcesz użyć pustego passphrase (tj. bez passphrase). Aby uniemożliwić Trezorowi proszenie o wprowadzenie passphrase przy każdym uruchomieniu, należy przejść do Trezor Suite, uzyskać dostęp do ustawień i zmienić opcję w "*Urządzenie*" > "*Wallet default*" na "*Standard*" zamiast "*passphrase*".



![Image](assets/fr/33.webp)



Kliknij przycisk "*Scan*". Powinien pojawić się Safe 5. Kliknij na "*Import Keystore*".



![Image](assets/fr/34.webp)



Możesz teraz zobaczyć szczegóły swojego Wallet, w tym rozszerzony klucz publiczny swojego pierwszego konta. Kliknij przycisk "*Zastosuj*", aby sfinalizować tworzenie Wallet.



![Image](assets/fr/35.webp)



Wybierz silne hasło, aby zabezpieczyć dostęp do Sparrow Wallet. Hasło to zapewni bezpieczny dostęp do danych Sparrow Wallet, chroniąc klucze publiczne, adresy, etykiety i historię transakcji przed nieautoryzowanym dostępem.



Radzę zapisać to hasło w menedżerze haseł, aby go nie zapomnieć.



![Image](assets/fr/36.webp)



A teraz Twoje portfolio zostało zaimportowane do Sparrow Wallet!



![Image](assets/fr/37.webp)



Przed otrzymaniem pierwszych bitcoinów w Wallet, **Zalecam wykonanie testu odzyskiwania pustych środków**. Zapisz informacje referencyjne, takie jak xpub, a następnie zresetuj Trezor Safe 5, gdy Wallet jest nadal pusty. Następnie spróbuj przywrócić Wallet na Trezorze przy użyciu papierowych kopii zapasowych. Sprawdź, czy xpub wygenerowany po przywróceniu jest zgodny z pierwotnie zapisanym. Jeśli tak, możesz mieć pewność, że papierowe kopie zapasowe są niezawodne.



Aby dowiedzieć się więcej o tym, jak wykonać test odzyskiwania, proponuję zapoznać się z tym innym samouczkiem:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Jak mogę odbierać bitcoiny za pomocą Trezor Safe 5?



W aplikacji Sparrow kliknij zakładkę "*Odbierz*".



![Image](assets/fr/38.webp)



Przed użyciem Address proponowanego przez Sparrow Wallet, sprawdź go na ekranie Trezora. Ta praktyka pozwala potwierdzić, że Address wyświetlany na Sparrow nie jest fałszywy i że Hardware Wallet rzeczywiście posiada klucz prywatny potrzebny do późniejszego wydania bitcoinów zabezpieczonych tym Address. Pomaga to uniknąć kilku rodzajów ataków.



Aby wykonać to sprawdzenie, kliknij przycisk "*Wyświetl Address*".



![Image](assets/fr/39.webp)



Sprawdź, czy Address wyświetlany na twoim Trezorze jest zgodny z tym na Sparrow Wallet. Zaleca się również przeprowadzenie tego sprawdzenia tuż przed przekazaniem Address do nadawcy, aby upewnić się co do jego ważności. Możesz nacisnąć ekran, aby potwierdzić.



![Image](assets/fr/40.webp)



Następnie można dodać "*Label*", aby opisać źródło bitcoinów, które będą zabezpieczone tym Address. Jest to dobra praktyka, która pozwala lepiej zarządzać UTXO.



![Image](assets/fr/41.webp)



Następnie możesz użyć tego Address, aby otrzymać bitcoiny.



![Image](assets/fr/42.webp)



## Jak wysyłać bitcoiny za pomocą Trezor Safe 5?



Teraz, gdy otrzymałeś swoje pierwsze Satss na Wallet z zabezpieczeniem Safe 5, możesz je również wydać! Podłącz Trezor do komputera, odblokuj go kodem PIN, uruchom Sparrow Wallet, a następnie przejdź do zakładki "*Wyślij*", aby utworzyć nową transakcję.



![Image](assets/fr/43.webp)



Jeśli chcesz *Coin Control*, czyli wybrać konkretnie, które UTXO mają zostać wykorzystane w transakcji, przejdź do zakładki "*UTXOs*". Wybierz UTXO, które chcesz wydać, a następnie kliknij "*Wyślij wybrane*". Nastąpi przekierowanie do tego samego ekranu w zakładce "*Wyślij*", ale z UTXO już wybranymi do transakcji.



![Image](assets/fr/44.webp)



Wprowadź adres docelowy Address. Można również wprowadzić wiele adresów, klikając przycisk "*+ Add*".



![Image](assets/fr/45.webp)



Zapisz "*Label*", aby zapamiętać cel tego wydatku.



![Image](assets/fr/46.webp)



Wybierz kwotę, która ma zostać wysłana do tego Address.



![Image](assets/fr/47.webp)



Dostosuj stawkę opłaty za transakcję do aktualnej sytuacji rynkowej. Na przykład można użyć [Mempool.space](https://Mempool.space/), aby wybrać odpowiednią stawkę opłaty.



Upewnij się, że wszystkie parametry transakcji są prawidłowe, a następnie kliknij "*Twórz transakcję*".



![Image](assets/fr/48.webp)



Jeśli wszystko jest w porządku, kliknij "*Finalizuj transakcję do podpisu*".



![Image](assets/fr/49.webp)



Kliknij "*Podpisz*".



![Image](assets/fr/50.webp)



Kliknij "*Podpisz*" obok Trezor Safe 5.



![Image](assets/fr/51.webp)



Sprawdź parametry transakcji na ekranie Hardware Wallet, w tym odbiorcę Address, wysłaną kwotę i opłatę. Po zweryfikowaniu transakcji na urządzeniu Trezor naciśnij i przytrzymaj ekran, aby ją podpisać.



![Image](assets/fr/52.webp)



Transakcja jest teraz podpisana. Sprawdź ostatni raz, czy wszystko jest w porządku, a następnie kliknij "*Broadcast Transaction*", aby nadać ją w sieci Bitcoin.



![Image](assets/fr/53.webp)



Można go znaleźć w zakładce "*Transakcje*" w Sparrow Wallet.



![Image](assets/fr/54.webp)



Gratulacje, jesteś teraz na bieżąco z podstawową obsługą Trezor Safe 5 i Sparrow Wallet! Aby pójść o krok dalej, polecam ten obszerny samouczek na temat korzystania z Trezor Hardware Wallet z passphrase BIP39 w celu zwiększenia bezpieczeństwa:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Jeśli uznałeś ten poradnik za przydatny, będę wdzięczny za pozostawienie kciuka Green poniżej. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dziękuję bardzo!