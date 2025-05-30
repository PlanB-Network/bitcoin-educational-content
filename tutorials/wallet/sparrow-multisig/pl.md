---
name: Wróbel Wallet - Multisig
description: Utwórz portfolio z wieloma podpisami w Sparrow
---
![cover](assets/cover.webp)



Wallet z wieloma podpisami (często nazywany "*Multisig*") jest strukturą Bitcoin Wallet, która wymaga kilku podpisów kryptograficznych, z różnych kluczy, aby autoryzować wydatek. W przeciwieństwie do konwencjonalnego ("*singlesig*") Wallet, w którym pojedynczy klucz prywatny wystarcza do odblokowania UTXO, Multisig opiera się na modelu **m-of-n**: z _n_ kluczy powiązanych z Wallet, _m_ musi bezwzględnie współpodpisać każdą transakcję.



Mechanizm ten umożliwia współdzielenie kontroli nad portfelem przez kilka podmiotów lub urządzeń. Na przykład w konfiguracji 2 na 3 generowane są trzy niezależne zestawy kluczy, ale tylko dwa są potrzebne do uwolnienia środków. Taka architektura drastycznie zmniejsza ryzyko związane z naruszeniem lub utratą klucza: złodziej z dostępem tylko do jednego klucza nie może opróżnić Wallet, a użytkownik, który straci jeden z nich, nadal może uzyskać dostęp do swoich środków za pomocą pozostałych dwóch.



![Image](assets/fr/01.webp)



Większe bezpieczeństwo wiąże się jednak z większą złożonością. Konfiguracja Multisig Wallet wymaga zabezpieczenia kilku fraz Mnemonic (po jednej na czynnik podpisu) i rozszerzonych kluczy publicznych ("*xpub*"). Rzeczywiście, jeśli używasz Multisig 2-of-3 Wallet, aby odzyskać Wallet, musisz albo mieć wszystkie trzy frazy Mnemonic, albo co najmniej dwie z trzech fraz. Ale jeśli masz tylko dwie z trzech fraz, potrzebujesz również dostępu do trzech *xpub*, bez których niemożliwe będzie pobranie kluczy publicznych potrzebnych do uzyskania dostępu do bitcoinów, które chronią.



Podsumowując, aby odzyskać portfel Multisig, należy :




- Możesz też uzyskać dostęp do wszystkich fraz Mnemonic powiązanych z każdym czynnikiem sygnatury;
- Albo posiadać minimalną liczbę fraz Mnemonic wymaganą przez próg, aby móc podpisać, a także mieć dostęp do xpubów wszystkich czynników w celu pobrania niezbędnych kluczy publicznych.



![Image](assets/fr/02.webp)



Zarządzanie kopiami zapasowymi portfela Multisig jest ułatwione dzięki *Output Script Descriptors*, które grupują wszystkie publiczne dane wymagane do uzyskania dostępu do funduszy. Jednak ta funkcjonalność nie jest jeszcze zaimplementowana we wszystkich programach do zarządzania portfelem.



Multisig jest szczególnie odpowiedni dla użytkowników bitcoinów poszukujących zwiększonego bezpieczeństwa lub zbiorowego zarządzania funduszami: firm, stowarzyszeń, rodzin lub indywidualnych użytkowników posiadających znaczną ilość bitcoinów. Może być wykorzystywany do tworzenia zdecentralizowanych schematów zarządzania, na przykład do rozdzielania uprawnień do podpisywania między kilku menedżerów lub członków zespołu.



W tym samouczku dowiemy się, jak utworzyć i używać klasycznego portfela wielopodpisowego Wallet z **Sparrow Wallet**. Jeśli chcesz utworzyć niestandardowe portfolio z wieloma podpisami i zegarami, zalecam użycie Liana:



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Wymagania wstępne



W tym samouczku pokażę, jak utworzyć Multisig za pomocą [oprogramowania do zarządzania portfelem Sparrow Wallet] (https://sparrowwallet.com/download/). Jeśli jeszcze nie zainstalowałeś tego oprogramowania, zrób to teraz. Jeśli potrzebujesz pomocy, mamy również szczegółowy samouczek dotyczący konfiguracji Sparrow Wallet:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Aby skonfigurować Wallet z wieloma podpisami, potrzebne będą różne portfele sprzętowe. Na przykład dla Multisig 2-de-3 można użyć :




- Trezor Model One;
- Ledger Flex;
- Coldcard MK3.



![Image](assets/fr/03.webp)



Dobrym pomysłem jest użycie różnych marek Hardware Wallet w konfiguracji Multisig. Gwarantuje to, że jeśli konkretny model napotka poważny problem, nie wpłynie to na ogólne bezpieczeństwo Multisig. Co więcej, pozwala to na wykorzystanie specyficznych zalet każdego urządzenia. Na przykład w mojej konfiguracji :





- Trezor Model One jest całkowicie open-source, co umożliwia weryfikację generacji seed. Ponieważ jednak nie jest wyposażony w Secure Element, pozostaje podatny na ataki fizyczne;





- Z drugiej strony Ledger Flex korzysta z nieweryfikowalnego, zastrzeżonego oprogramowania układowego, ale zawiera bezpieczny element, który zapewnia doskonałą ochronę fizyczną;





- Karta Coldcard jest wyposażona w Secure Element, a jej kod można przeszukiwać. Jest to interesujący wybór dla naszej konfiguracji, ponieważ oferuje funkcje weryfikacji niedostępne w innych modelach.



Przed skonfigurowaniem Multisig Wallet należy upewnić się, że każdy Hardware Wallet jest prawidłowo skonfigurowany (generowanie i zapisywanie Mnemonic, definicja kodu PIN). Szczegółowe instrukcje można znaleźć w naszych samouczkach dla każdego Hardware Wallet, na przykład :



https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Jak zobaczymy w dalszej części tego samouczka, możliwe jest również zintegrowanie z konfiguracją Multisig czynnika, który nie jest powiązany z Hardware Wallet, ale którego klucze prywatne są przechowywane na komputerze. Ta metoda jest oczywiście mniej bezpieczna niż wyłączne korzystanie z portfeli sprzętowych, ale może być istotna w niektórych przypadkach. Na przykład w przypadku Multisig 2-de-3 można zdecydować się na dwa portfele sprzętowe i jeden Software Wallet.



## Tworzenie portfolio Multisig



Otwórz Sparrow Wallet, kliknij zakładkę "*File*", a następnie wybierz "*New Wallet*".



![Image](assets/fr/04.webp)



Przypisz nazwę do portfela z wieloma podpisami, a następnie kliknij "*Utwórz Wallet*", aby potwierdzić.



![Image](assets/fr/05.webp)



W menu rozwijanym "*Policy Type*" wybierz opcję "*Multi Signature*".



![Image](assets/fr/06.webp)



W prawym górnym rogu możesz teraz zdefiniować całkowitą liczbę kluczy w Multisig, a także liczbę współsygnatariuszy wymaganych do autoryzacji wydatku. W moim przykładzie jest to schemat 2 na 3.



![Image](assets/fr/07.webp)



W dolnej części okna Sparrow Wallet wyświetla trzy "*Keystore*". Każdy z nich reprezentuje zestaw kluczy. Tutaj używam trzech portfeli sprzętowych, więc każdy "*Keystore*" odpowiada jednemu z nich. Teraz je skonfigurujemy.



Zaczynam od karty Coldcard. W zakładce "*Keystore 1*" wybieram opcję "*Airgapped Hardware Wallet*".



![Image](assets/fr/08.webp)



Na karcie Coldcard, po odblokowaniu urządzenia, przechodzę do menu "*Ustawienia*", a następnie do "*Multisig Wallets*".



![Image](assets/fr/09.webp)



To menu umożliwia zarządzanie portfelami Multisig, w których uczestniczy karta Coldcard. Chcę utworzyć nowy portfel, więc wybieram "*Export XPUB*".



![Image](assets/fr/10.webp)



W przypadku pola "*Numer konta*", jeśli zarządzasz tylko jednym kontem, możesz pozostawić je puste i zatwierdzić bezpośrednio, naciskając przycisk potwierdzenia.



![Image](assets/fr/11.webp)



Coldcard utworzy plik zawierający xpub zapisany na karcie Micro SD.



![Image](assets/fr/12.webp)



Włóż kartę Micro SD do komputera. W aplikacji Sparrow Wallet kliknij przycisk "*Import File...*" obok "*Coldcard Multisig*", a następnie wybierz plik utworzony przez kartę Coldcard na karcie.



![Image](assets/fr/13.webp)



Twój xpub został pomyślnie zaimportowany. Powtórzymy teraz procedurę z pozostałymi dwoma portfelami sprzętowymi.



![Image](assets/fr/14.webp)



W przypadku Ledger Flex wybieram "*Keystore 2*", a następnie klikam "*Connected Hardware Wallet*". Upewnij się, że Ledger jest podłączony do komputera, odblokowany i że aplikacja Bitcoin jest otwarta.



![Image](assets/fr/15.webp)



Następnie kliknij przycisk "*Scan...*".



![Image](assets/fr/16.webp)



Obok nazwy portfela sprzętu kliknij "*Import Keystore*".



![Image](assets/fr/17.webp)



Drugi sygnatariusz jest teraz poprawnie zarejestrowany w Sparrow Wallet.



![Image](assets/fr/18.webp)



Powtarzam dokładnie tę samą procedurę z Trezor One, aby sfinalizować konfigurację Multisig.



![Image](assets/fr/19.webp)



W mojej konfiguracji nie uwzględniamy tego przypadku, ale jeśli chcesz dołączyć podpis za pośrednictwem Software Wallet w Sparrow (Hot Wallet) w Multisig, po prostu kliknij przycisk "*Nowy lub zaimportowany Software Wallet*".



Teraz, gdy wszystkie urządzenia z podpisami zostały zaimportowane do Sparrow Wallet, możesz sfinalizować tworzenie Multisig, klikając "*Zastosuj*".



![Image](assets/fr/20.webp)



Wybierz silne hasło, aby zabezpieczyć dostęp do Sparrow Wallet Wallet. Hasło to chroni klucze publiczne, adresy, etykiety i historię transakcji przed nieautoryzowanym dostępem.



Pamiętaj, aby zapisać to hasło w bezpiecznym miejscu, takim jak menedżer haseł, aby uniknąć jego utraty.



![Image](assets/fr/21.webp)



## Tworzenie kopii zapasowych portfela Multisig



Teraz zapiszemy nasz *Output Script Descriptor* na karcie Coldcard (dotyczy to tylko użytkowników z kartą Coldcard w Multisig), a przede wszystkim będziemy przechowywać jego kopię zapasową na niezależnym nośniku.



*Deskryptor* zawiera wszystkie xpuby w portfelu Multisig, a także ścieżki derywacji użyte do generate kluczy. Pamiętaj, co widzieliśmy w części 1: aby przywrócić portfel Multisig, musisz albo mieć **wszystkie** frazy Mnemonic, albo tylko minimalną liczbę wymaganą do osiągnięcia progu podpisu. Jednak w tym drugim przypadku konieczne jest również posiadanie **pubów** brakujących sygnatariuszy. *Deskryptor* zawiera wszystkie xpubs Multisig.



Jeśli nie jest to jasne, pamiętaj o tym: aby pobrać Multisig, potrzebujesz minimalnej liczby fraz Mnemonic dla każdego użytego Hardware Wallet, w zależności od progu (w moim przypadku: 2 frazy), a także *Deskryptor*.



Ten *Deskryptor* nie zawiera kluczy prywatnych, a jedynie publiczne. Oznacza to, że nie daje on dostępu do środków. Nie jest zatem tak krytyczny jak frazy Mnemonic, które dają pełny dostęp do bitcoinów. Ryzyko związane z *Deskryptorem* jest związane wyłącznie z poufnością: w przypadku kompromitacji strona trzecia może obserwować wszystkie transakcje, ale nie może wydać środków.



Zdecydowanie zalecam utworzenie kilku kopii tego *Deskryptora* i przechowywanie ich z każdym urządzeniem podpisującym na Multisig. Na przykład, w moim przypadku drukuję *Deskryptor* na papierze i przechowuję jedną kopię z kartą Coldcard, inną z Trezorem i jedną z Ledger. Zapisuję również *Deskryptor* jako plik PDF na trzech pamięciach USB, z których każda jest przechowywana z jednym z portfeli sprzętowych. W ten sposób maksymalizuję swoje szanse na to, że nigdy nie zgubię tego *Deskryptora* i jestem pewien, że mam dwie kopie (jedną fizyczną i jedną cyfrową) na każdym urządzeniu.



Po utworzeniu portfolio Multisig, Sparrow automatycznie udostępnia ten *Deskryptor*. Kliknij przycisk "*Zapisz PDF...*", aby zapisać go zarówno jako tekst, jak i kod QR.



![Image](assets/fr/22.webp)



Następnie można wydrukować ten plik PDF i skopiować go do pamięci USB.



![Image](assets/fr/23.webp)



Zarejestrujemy również ten *Deskryptor* w Coldcard (jeśli używasz go w swojej konfiguracji). Pozwoli to Coldcard zweryfikować, czy każda podpisana później transakcja odpowiada oryginalnemu Wallet: poprawne xpubs, poprawny format Address, poprawna ścieżka derywacji.... Bez tego zaimportowanego *Deskryptora*, Coldcard nie może potwierdzić, że adresy Exchange nie zostały przejęte lub że PSBT nie został zmodyfikowany.



To właśnie sprawia, że Coldcard jest tak interesujący w Multisig: oferuje dodatkowe kontrole przed niektórymi wyrafinowanymi atakami, na które nie pozwalają inne portfele sprzętowe (oczywiście pod warunkiem, że używasz go do podpisywania).



W aplikacji Sparrow przejdź do menu "*Ustawienia*", a następnie kliknij "*Eksportuj...*".



![Image](assets/fr/24.webp)



Obok opcji "*Coldcard Multisig*" kliknij "*Export File...*" i zapisz plik tekstowy na karcie Micro SD.



![Image](assets/fr/25.webp)



Następnie włóż kartę do Coldcard. Przejdź do menu "*Settings*", następnie "*Multisig Wallets*" i wybierz "*Import from SD*".



![Image](assets/fr/26.webp)



Wybierz odpowiedni plik i potwierdź import.



![Image](assets/fr/27.webp)



Kliknij nazwę nowo zaimportowanego Multisig.



![Image](assets/fr/28.webp)



Sprawdź parametry konfiguracyjne Multisig, a następnie potwierdź rejestrację.



![Image](assets/fr/29.webp)



Urządzenie Multisig jest teraz prawidłowo zapisane na karcie Coldcard. Jeśli masz kilka kart Coldcard w tym samym Multisig, powtórz tę procedurę dla każdej z nich.



Oprócz zapisania *Deskryptora*, nie zapomnij zwrócić szczególnej uwagi na zapisanie fraz Mnemonic dla każdego z urządzeń z podpisem. Jeśli dopiero zaczynasz, zdecydowanie zalecam zapoznanie się z tym innym samouczkiem, aby dowiedzieć się, jak prawidłowo je zapisywać i zarządzać nimi:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Przed otrzymaniem pierwszych bitcoinów na Multisig, **Zalecam wykonanie pustego testu odzyskiwania**. Zanotuj informacje referencyjne, takie jak pierwszy otrzymany Address, a następnie zresetuj portfele sprzętowe, gdy Wallet jest nadal pusty. Następnie spróbuj przywrócić Multisig Wallet w portfelach sprzętowych przy użyciu papierowych kopii zapasowych Mnemonic, a następnie w Sparrow przy użyciu *Deskryptora*. Sprawdź, czy pierwsza fraza Address wygenerowana po przywróceniu jest zgodna z pierwotnie zapisaną. Jeśli tak, możesz mieć pewność, że papierowe kopie zapasowe są niezawodne.



Aby dowiedzieć się więcej o tym, jak wykonać test odzyskiwania, proponuję zapoznać się z tym innym samouczkiem:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Odbieraj bitcoiny na swoim Multisig



Twój Wallet jest teraz gotowy do odbierania bitcoinów. W aplikacji Sparrow kliknij zakładkę "*Odbierz*".



![Image](assets/fr/30.webp)



Przed użyciem Address wygenerowanego przez Sparrow Wallet należy poświęcić trochę czasu na sprawdzenie go bezpośrednio na ekranie portfeli sprzętowych. Zapewni to, że Address nie został zmieniony, a urządzenia posiadają klucze prywatne potrzebne do wydania powiązanych środków. Pomaga to chronić przed wieloma wektorami ataków.



Aby to zrobić, kliknij "*Wyświetl Address*", aby wyświetlić Address na Trezorze lub Ledger, jeśli jest podłączony kablem.



![Image](assets/fr/31.webp)



Dzięki Coldcard weryfikacja ta może być przeprowadzona bez jakiejkolwiek interakcji ze Sparrow. Wystarczy otworzyć menu "*Address Explorer*", a następnie wybrać Multisig na samym dole.



![Image](assets/fr/32.webp)



Zostaną wyświetlone adresy odbioru wygenerowane przez Multisig.



![Image](assets/fr/33.webp)



Sprawdź, czy Address wyświetlany na każdym Hardware Wallet odpowiada dokładnie temu w Sparrow Wallet. Zaleca się to zrobić tuż przed udostępnieniem Address płatnikowi, aby mieć pewność co do jego integralności.



Następnie można przypisać "*Label*" do tego Address, aby wskazać pochodzenie otrzymanych bitcoinów. Jest to dobry sposób na zorganizowanie zarządzania UTXO.



![Image](assets/fr/34.webp)



Po weryfikacji możesz użyć Address, aby otrzymać bitcoiny.



![Image](assets/fr/35.webp)



## Wysyłanie bitcoinów za pomocą Multisig



Teraz, gdy otrzymałeś swoje pierwsze Satss na Multisig Wallet, możesz je również wydać! W Sparrow przejdź do zakładki "*Wyślij*", aby utworzyć nową transakcję.



![Image](assets/fr/36.webp)



Jeśli chcesz użyć *Coin Control*, czyli ręcznie wybrać UTXO, które chcesz wydać, przejdź do zakładki "*UTXOs*". Wybierz UTXO, które chcesz wydać, a następnie kliknij "*Wyślij wybrane*". Nastąpi automatyczne przekierowanie do zakładki "*Wyślij*" z już wypełnionymi UTXO.



![Image](assets/fr/37.webp)



Wprowadź docelowy adres Address. Można dodać wiele adresów, klikając "*+ Add*".



![Image](assets/fr/38.webp)



Dodaj "*Label*", aby opisać cel tego wydatku, aby ułatwić śledzenie transakcji.



![Image](assets/fr/39.webp)



Wprowadź kwotę, która ma zostać wysłana do wybranego Address.



![Image](assets/fr/40.webp)



Dostosuj szybkość ładowania do bieżących warunków sieciowych. Na przykład sprawdź [Mempool.space](https://Mempool.space/), aby wybrać odpowiedni poziom naładowania.



Po sprawdzeniu wszystkich parametrów transakcji, kliknij "*Twórz transakcję*".



![Image](assets/fr/41.webp)



Jeśli wszystko ci odpowiada, kliknij "*Finalizuj transakcję do podpisania*".



![Image](assets/fr/42.webp)



Na dole ekranu zobaczysz, że Sparrow czeka na 2 podpisy. To normalne: użyty tutaj Wallet to Multisig 2-de-3.



![Image](assets/fr/43.webp)



Rozpoczynam podpisywanie za pomocą karty Coldcard. Aby to zrobić, wkładam kartę Micro SD do komputera, a następnie klikam "*Zapisz transakcję*".



![Image](assets/fr/44.webp)



Istnieją 3 sposoby przesłania transakcji do podpisania do Hardware Wallet, a następnie pobrania jej ze Sparrow. Pierwszym z nich jest użycie karty Micro SD, tak jak zrobimy to w przypadku karty Coldcard. Drugim jest połączenie kablowe, którego użyjemy do drugiego podpisu (Ledger i Trezor). Wreszcie, możliwe jest użycie komunikacji za pomocą kodu QR, dla urządzeń wyposażonych w kamerę, takich jak Coldcard Q, Jade Plus lub Passport V2.



Po zapisaniu PSBT (*Partially Signed Bitcoin Transaction*) na karcie Micro SD, wkładam ją do Coldcard MK3, a następnie wybieram menu "*Ready to Sign*".



![Image](assets/fr/45.webp)



Na ekranie Hardware Wallet dokładnie sprawdź parametry transakcji: Address odbiorcy, wysłaną kwotę i opłaty. Po potwierdzeniu transakcji zatwierdź ją, aby przejść do podpisu.



![Image](assets/fr/46.webp)



Następnie podłącz kartę Micro SD do komputera i kliknij "*Load Transaction*" w aplikacji Sparrow. Wybierz PSBT podpisany przez Coldcard ze swoich plików.



![Image](assets/fr/47.webp)



Widać, że podpis Coldcard został dodany. Teraz użyję drugiego urządzenia, w tym przypadku Ledger, aby wykonać drugi wymagany podpis. Podłączam je, odblokowuję, a następnie klikam "*Podpisz*" na Sparrow.



![Image](assets/fr/48.webp)



Kliknij "*Podpisz*" obok nazwy swojego Hardware Wallet.



![Image](assets/fr/49.webp)



Przy pierwszym użyciu Ledger z tym Multisig, Sparrow poprosi o zweryfikowanie rozszerzonych kluczy publicznych (xpubs) współsygnatariuszy. Podobnie jak w przypadku karty Coldcard, krok ten zapobiega późniejszemu podpisywaniu na ślepo. Aby zweryfikować te informacje, porównaj xpub wyświetlany na ekranie Ledger z tymi dostarczonymi bezpośrednio przez inne portfele sprzętowe.



![Image](assets/fr/50.webp)



Sprawdź Address odbiorcy, kwotę przelewu i opłatę transakcyjną, a następnie podpisz transakcję.



![Image](assets/fr/51.webp)



Naciśnij ekran, aby złożyć podpis.



![Image](assets/fr/52.webp)



Sparrow ma teraz dwa podpisy potrzebne do uwolnienia środków z portfela Multisig. Sprawdź transakcję po raz ostatni, a jeśli wszystko pójdzie dobrze, kliknij "*Broadcast Transaction*", aby rozesłać ją w sieci.



![Image](assets/fr/53.webp)



Transakcję tę można znaleźć w zakładce "*Transakcje*" Sparrow Wallet.



![Image](assets/fr/54.webp)



Gratulacje, wiesz już, jak skonfigurować i używać wielopodpisowego Wallet w Sparrow. Jeśli ten poradnik okazał się przydatny, będę wdzięczny, jeśli zostawisz poniżej kciuk Green. Zachęcam do udostępnienia tego artykułu w sieciach społecznościowych. Dzięki za udostępnienie!



Aby pójść dalej, zalecam zapoznanie się z tym samouczkiem na temat innej metody zwiększania bezpieczeństwa Bitcoin Wallet, passphrase BIP39 :



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7