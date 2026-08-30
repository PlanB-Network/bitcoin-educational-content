---
name: Sparrow Wallet - Multisig
description: Tworzenie portfela z wieloma podpisami w Sparrow
---
![cover](assets/cover.webp)


Portfel z wieloma podpisami (często nazywany "*Multisig*") to struktura portfela Bitcoin, która wymaga kilku podpisów kryptograficznych, pochodzących z różnych kluczy, aby autoryzować wydatek. W przeciwieństwie do zwykłego portfela ("*singlesig*"), w którym jeden klucz prywatny wystarcza do odblokowania UTXO, Multisig opiera się na modelu **m-of-n**: z _n_ kluczy powiązanych z portfelem _m_ musi obowiązkowo współpodpisać każdą transakcję.


Ten mechanizm pozwala dzielić kontrolę nad portfelem między kilka podmiotów lub urządzeń. Na przykład w konfiguracji 2-of-3 generowane są trzy niezależne zestawy kluczy, ale do uwolnienia środków potrzebne są tylko dwa. Taka architektura drastycznie zmniejsza ryzyko związane z naruszeniem lub utratą klucza: złodziej, który ma dostęp tylko do jednego klucza, nie może opróżnić portfela, a użytkownik, który jeden zgubi, nadal ma dostęp do swoich środków przy użyciu dwóch pozostałych.


![Image](assets/fr/01.webp)


Temu większemu bezpieczeństwu towarzyszy jednak większa złożoność. Utworzenie portfela Multisig wymaga zabezpieczenia kilku fraz mnemonicznych (po jednej na każdy czynnik podpisu) oraz rozszerzonych kluczy publicznych ("*xpub*"). Jeśli bowiem używasz portfela Multisig 2-of-3, do odtworzenia portfela musisz mieć albo wszystkie trzy frazy mnemoniczne, albo co najmniej dwie z trzech fraz. Ale jeśli masz tylko dwie z trzech fraz, potrzebujesz również dostępu do trzech *xpub*, bez których nie da się odtworzyć kluczy publicznych niezbędnych do dostępu do chronionych przez nie bitcoinów.


Podsumowując, aby odzyskać portfel Multisig, musisz:


- Albo mieć dostęp do wszystkich fraz mnemonicznych powiązanych z każdym czynnikiem podpisu;
- Albo mieć minimalną liczbę fraz mnemonicznych wymaganą przez próg, aby móc podpisać, a także mieć dostęp do xpub wszystkich czynników, aby odtworzyć niezbędne klucze publiczne.


![Image](assets/fr/02.webp)


Zarządzanie kopiami zapasowymi portfela Multisig ułatwiają *Deskryptory skryptów wyjściowych*, które zbierają wszystkie publiczne dane niezbędne do dostępu do środków. Ta funkcja nie jest jednak jeszcze wdrożona w każdym oprogramowaniu do zarządzania portfelem.


Multisig szczególnie dobrze pasuje do bitcoinerów, którzy szukają wyższego bezpieczeństwa lub zbiorowego zarządzania środkami: firm, stowarzyszeń, rodzin albo pojedynczych użytkowników trzymających znaczną liczbę bitcoinów. Można go użyć do zbudowania zdecentralizowanych schematów zarządzania, na przykład aby rozdzielić prawo do podpisu między kilku menedżerów lub członków zespołu.


W tym samouczku nauczymy się tworzyć i używać klasycznego portfela z wieloma podpisami w **Sparrow Wallet**. Jeśli chcesz utworzyć własny portfel z wieloma podpisami z blokadami czasowymi, polecam zamiast tego skorzystać z Liany:


https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Wymagania wstępne


W tym samouczku pokażę, jak zbudować Multisig za pomocą [oprogramowania do zarządzania portfelem Sparrow Wallet](https://sparrowwallet.com/download/). Jeśli jeszcze nie zainstalowałeś tego oprogramowania, zrób to teraz. Jeśli potrzebujesz pomocy, mamy również szczegółowy samouczek o konfiguracji Sparrow Wallet:


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Aby skonfigurować portfel z wieloma podpisami, potrzebujesz kilku różnych portfeli sprzętowych. Na przykład dla Multisig 2-of-3 możesz użyć:


- Trezor Model One;
- Ledger Flex;
- Passport Core.


![Image](assets/fr/03.webp)


Warto użyć w konfiguracji Multisig portfeli sprzętowych różnych marek. Dzięki temu poważny problem z jednym konkretnym modelem nie wpłynie na bezpieczeństwo całego Multisig. Co więcej, pozwala to korzystać ze szczególnych zalet każdego urządzenia. Na przykład w mojej konfiguracji:



- Trezor Model One jest całkowicie open-source, co pozwala zweryfikować generowanie seed. Ponieważ jednak nie ma Secure Element, pozostaje podatny na ataki fizyczne;



- Ledger Flex ma z kolei zamknięte oprogramowanie sprzętowe, którego nie da się zweryfikować, ale zawiera Secure Element, który zapewnia doskonałą ochronę fizyczną;



- Passport Core łączy w pełni otwarte oprogramowanie sprzętowe, Secure Element i wymianę danych kodami QR w trybie air-gap. Jest niezależnym trzecim sygnatariuszem, który potrafi weryfikować adresy i podpisywać PSBT bez połączenia danych przez USB.


Przed konfiguracją portfela Multisig upewnij się, że każdy portfel sprzętowy jest poprawnie skonfigurowany (wygenerowanie i zapisanie frazy mnemonicznej, ustawienie kodu PIN). Szczegółowe instrukcje znajdziesz w naszych samouczkach do poszczególnych portfeli sprzętowych, na przykład:


https://planb.academy/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Jak zobaczymy dalej w tym samouczku, do konfiguracji Multisig można też włączyć czynnik, który nie jest powiązany z portfelem sprzętowym, ale którego klucze prywatne są przechowywane na komputerze. Ta metoda jest oczywiście mniej bezpieczna niż używanie wyłącznie portfeli sprzętowych, ale w niektórych przypadkach może mieć sens. Na przykład dla Multisig 2-of-3 możesz wybrać dwa portfele sprzętowe i jeden portfel programowy.

> ⚠️ **Ostrzeżenie o bezpieczeństwie Coldcard MK3:** nie twórz nowego seed na MK3 z oprogramowaniem sprzętowym starszym niż 4.2.0. Seed wygenerowany na starszym oprogramowaniu trzeba zastąpić, a środki przenieść. Dlatego w tym samouczku referencyjnym sygnatariuszem air-gap jest Passport Core.


## Tworzenie portfela Multisig


Otwórz Sparrow Wallet, kliknij zakładkę "*File*", a następnie wybierz "*New Wallet*".


![Image](assets/fr/04.webp)


Nadaj nazwę swojemu portfelowi z wieloma podpisami, a następnie kliknij "*Create Wallet*", aby potwierdzić.


![Image](assets/fr/05.webp)


W rozwijanym menu "*Policy Type*" wybierz opcję "*Multi Signature*".


![Image](assets/fr/06.webp)


W prawym górnym narożniku możesz teraz określić łączną liczbę kluczy w Multisig oraz liczbę współpodpisujących wymaganą do autoryzacji wydatku. W moim przykładzie jest to schemat 2-of-3.


![Image](assets/fr/07.webp)


W dolnej części okna Sparrow Wallet wyświetla trzy "*Keystore*". Każdy z nich reprezentuje zestaw kluczy. Używam tutaj trzech portfeli sprzętowych, więc każdy "*Keystore*" odpowiada jednemu z nich. Teraz je skonfigurujemy.


Zaczynam od Passport Core. W zakładce "*Keystore 1*" wybieram opcję "*Airgapped Hardware Wallet*".


![Image](assets/fr/08.webp)


W Passport otwórz konto, którego chcesz użyć, a następnie wybierz "*Connect Wallet*" > "*Sparrow*" > "*Connect as Multisig*". Passport wyświetli animowany kod QR z informacjami o swoim kluczu publicznym.

W Sparrow wybierz "*Scan...*" obok "*Passport*" i zeskanuj ten animowany kod QR kamerą internetową komputera. Porównaj odcisk palca klucza głównego pokazany przez Sparrow z tym wyświetlonym na Passport, a następnie zaimportuj keystore.

Xpub twojego Passport jest teraz zaimportowany. Powtórz odpowiednią procedurę dla Ledger Flex i Trezor Model One.


Dla Ledger Flex wybieram "*Keystore 2*", a następnie klikam "*Connected Hardware Wallet*". Upewnij się, że Ledger jest podłączony do komputera, odblokowany i że aplikacja Bitcoin jest otwarta.


![Image](assets/fr/15.webp)


Następnie kliknij przycisk "*Scan...*".


![Image](assets/fr/16.webp)


Obok nazwy swojego portfela sprzętowego kliknij "*Import Keystore*".


![Image](assets/fr/17.webp)


Drugi sygnatariusz jest teraz poprawnie zarejestrowany w Sparrow Wallet.


![Image](assets/fr/18.webp)


Powtarzam dokładnie tę samą procedurę z Trezorem One, aby zakończyć konfigurację Multisig.


![Image](assets/fr/19.webp)


W mojej konfiguracji nie omawiamy tego przypadku, ale jeśli chcesz włączyć do swojego Multisig podpis z portfela programowego w Sparrow (hot wallet), wystarczy kliknąć przycisk "*New or Imported Software Wallet*".


Skoro wszystkie urządzenia podpisujące są już zaimportowane do Sparrow Wallet, możesz zakończyć tworzenie Multisig, klikając "*Apply*".


![Image](assets/fr/20.webp)


Wybierz silne hasło, aby zabezpieczyć dostęp do swojego portfela w Sparrow Wallet. To hasło chroni twoje klucze publiczne, adresy, etykiety i historię transakcji przed nieuprawnionym dostępem.


Pamiętaj, aby zapisać to hasło w bezpiecznym miejscu, na przykład w menedżerze haseł, żeby go nie stracić.


![Image](assets/fr/21.webp)


## Tworzenie kopii zapasowej portfela Multisig


Teraz zapiszemy *Deskryptor skryptu wyjściowego* na niezależnym nośniku i zachowamy kilka jego kopii.


*Deskryptor* zawiera wszystkie xpub twojego portfela Multisig oraz ścieżki derywacji użyte do wygenerowania kluczy. Przypomnij sobie to, co zobaczyliśmy w części 1: aby przywrócić portfel Multisig, musisz mieć albo **wszystkie** frazy mnemoniczne, albo tylko minimalną liczbę wymaganą do osiągnięcia progu podpisu. W tym drugim przypadku niezbędne jest jednak również posiadanie **xpub** brakujących sygnatariuszy. *Deskryptor* zawiera wszystkie xpub twojego Multisig.


Jeśli to nie jest jasne, zapamiętaj tylko tyle: aby odzyskać Multisig, potrzebujesz minimalnej liczby fraz mnemonicznych z użytych portfeli sprzętowych, zależnej od progu (w moim przypadku: 2 frazy), oraz *Deskryptora*.


Ten *Deskryptor* nie zawiera kluczy prywatnych, tylko publiczne. Oznacza to, że nie daje dostępu do środków. Nie jest więc tak krytyczny jak frazy mnemoniczne, które dają pełny dostęp do twoich bitcoinów. Ryzyko związane z *Deskryptorem* dotyczy wyłącznie poufności: w razie jego ujawnienia osoba trzecia mogłaby obserwować wszystkie twoje transakcje, ale nie mogłaby wydać twoich środków.


Zdecydowanie zalecam zrobienie kilku kopii tego *Deskryptora* i przechowywanie ich przy każdym urządzeniu podpisującym w Multisig. Na przykład ja drukuję *Deskryptor* na papierze i trzymam jedną kopię przy Passport, drugą przy Trezorze, a trzecią przy Ledgerze. Zapisuję też ten *Deskryptor* jako plik PDF na trzech pendrive'ach, z których każdy jest przechowywany przy jednym z portfeli sprzętowych. W ten sposób maksymalizuję szanse, że nigdy nie stracę tego *Deskryptora*, i mam pewność, że przy każdym urządzeniu są dwie kopie (jedna fizyczna i jedna cyfrowa).


Po utworzeniu portfela Multisig Sparrow automatycznie udostępnia ten *Deskryptor*. Kliknij przycisk "*Save PDF...*", aby zapisać go zarówno jako tekst, jak i jako kod QR.


![Image](assets/fr/22.webp)


Następnie możesz wydrukować ten plik PDF i skopiować go na pendrive'y.


![Image](assets/fr/23.webp)


Passport korzysta z konfiguracji multisig zaimportowanej przez Sparrow, aby wyświetlać i weryfikować odpowiednie informacje o kluczach podczas parowania i podpisywania kodami QR. Przechowuj *Deskryptor* niezależnie: pozostaje on niezbędny do odzyskania portfela, jeśli jeden z sygnatariuszy jest niedostępny.


Poza zapisaniem *Deskryptora* nie zapomnij poświęcić szczególnej uwagi kopiom zapasowym fraz mnemonicznych każdego z urządzeń podpisujących. Jeśli dopiero zaczynasz, bardzo polecam ten inny samouczek, aby dowiedzieć się, jak poprawnie je zapisywać i nimi zarządzać:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Przed otrzymaniem pierwszych bitcoinów na Multisig **zdecydowanie zalecam wykonanie testu odzyskiwania na sucho**. Zanotuj informacje odniesienia, na przykład pierwszy adres odbiorczy, a następnie zresetuj portfele sprzętowe, dopóki portfel jest jeszcze pusty. Potem spróbuj przywrócić portfel Multisig na portfelach sprzętowych, korzystając z papierowych kopii fraz mnemonicznych, a następnie w Sparrow, korzystając z *Deskryptora*. Sprawdź, czy pierwszy adres wygenerowany po przywróceniu zgadza się z tym, który zapisałeś na początku. Jeśli tak, możesz być spokojny, że twoje papierowe kopie zapasowe są niezawodne.


Aby dowiedzieć się więcej o przeprowadzaniu testu odzyskiwania, proponuję zapoznać się z tym innym samouczkiem:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Odbieranie bitcoinów na Multisig


Twój portfel jest teraz gotowy do odbierania bitcoinów. W Sparrow kliknij zakładkę "*Receive*".


![Image](assets/fr/30.webp)


Przed użyciem adresu wygenerowanego przez Sparrow Wallet poświęć chwilę na sprawdzenie go bezpośrednio na ekranach swoich portfeli sprzętowych. Upewnisz się w ten sposób, że adres nie został podmieniony i że twoje urządzenia mają klucze prywatne potrzebne do wydania powiązanych z nim środków. Chroni to przed kilkoma wektorami ataku.


Aby to zrobić, kliknij "*Display Address*", żeby wyświetlić adres na Trezorze lub Ledgerze podłączonym kablem.


![Image](assets/fr/31.webp)


W Passport wybierz konto multisig i wybierz "*Verify Address*". Zeskanuj kod QR adresu odbiorczego wyświetlonego przez Sparrow. Passport potwierdzi na swoim ekranie, czy adres należy do portfela multisig.


Sprawdź, czy adres wyświetlony na każdym portfelu sprzętowym dokładnie odpowiada temu w Sparrow Wallet. Warto zrobić to bezpośrednio przed przekazaniem adresu płatnikowi, aby mieć pewność co do jego integralności.


Następnie możesz przypisać do tego adresu "*Label*", aby wskazać pochodzenie otrzymanych bitcoinów. To dobry sposób na uporządkowanie zarządzania swoimi UTXO.


![Image](assets/fr/34.webp)


Po tej weryfikacji możesz użyć adresu do odbioru bitcoinów.


![Image](assets/fr/35.webp)


## Wysyłanie bitcoinów z Multisig


Skoro otrzymałeś już pierwsze satoshi na portfel Multisig, możesz je też wydać! W Sparrow przejdź do zakładki "*Send*", aby zbudować nową transakcję.


![Image](assets/fr/36.webp)


Jeśli chcesz użyć *Coin Control*, czyli ręcznie wybrać UTXO, które chcesz wydać, przejdź do zakładki "*UTXOs*". Wybierz UTXO do wydania, a następnie kliknij "*Send Selected*". Zostaniesz automatycznie przeniesiony do zakładki "*Send*" z już wypełnionymi UTXO.


![Image](assets/fr/37.webp)


Wpisz adres docelowy. Klikając "*+ Add*", możesz dodać kilka adresów.


![Image](assets/fr/38.webp)


Dodaj "*Label*", aby opisać cel tego wydatku i łatwiej śledzić swoje transakcje.


![Image](assets/fr/39.webp)


Wpisz kwotę, która ma zostać wysłana na wybrany adres.


![Image](assets/fr/40.webp)


Dostosuj stawkę opłat do aktualnych warunków w sieci. Na przykład sprawdź [Mempool.space](https://Mempool.space/), aby wybrać odpowiedni poziom opłat.


Po sprawdzeniu wszystkich parametrów transakcji kliknij "*Create Transaction*".


![Image](assets/fr/41.webp)


Jeśli wszystko ci odpowiada, kliknij "*Finalize Transaction for Signing*".


![Image](assets/fr/42.webp)


W dolnej części ekranu zobaczysz, że Sparrow czeka na 2 podpisy. To normalne: użyty tutaj portfel to Multisig 2-of-3.


![Image](assets/fr/43.webp)


Podpisywanie zaczynam od swojego Passport. W Sparrow kliknij "*Show QR*", aby wyświetlić PSBT (*Partially Signed Bitcoin Transaction*) jako animowane kody QR. W Passport wybierz konto multisig i wybierz "*Sign with QR Code*", a następnie zeskanuj kod QR wyświetlony przez Sparrow.


Na ekranie portfela sprzętowego dokładnie sprawdź parametry transakcji: adres odbiorcy, wysyłaną kwotę i opłaty. Po sprawdzeniu transakcji zatwierdź ją, aby przejść do podpisu.


Po zatwierdzeniu transakcji Passport wyświetla podpisany PSBT jako animowane kody QR. W Sparrow kliknij "*Scan QR*" i zeskanuj te kody kamerą internetową. Podpis z Passport zostanie wtedy dodany. Do drugiego wymaganego podpisu używam teraz Ledgera: podłączam go i odblokowuję, a następnie klikam "*Sign*" w Sparrow.


![Image](assets/fr/48.webp)


Kliknij "*Sign*" obok nazwy swojego portfela sprzętowego.


![Image](assets/fr/49.webp)


Przy pierwszym użyciu Ledgera z tym Multisig Sparrow poprosi cię o weryfikację rozszerzonych kluczy publicznych (xpub) współpodpisujących. Podobnie jak w przypadku Passport, ten krok zapobiega późniejszemu podpisywaniu na ślepo. Aby zatwierdzić te informacje, porównaj xpub wyświetlony na ekranie Ledgera z tymi podanymi bezpośrednio przez pozostałe portfele sprzętowe.


![Image](assets/fr/50.webp)


Sprawdź adres odbiorcy, przekazywaną kwotę i opłatę transakcyjną, a następnie podpisz transakcję.


![Image](assets/fr/51.webp)


Naciśnij ekran, aby podpisać.


![Image](assets/fr/52.webp)


Sparrow ma teraz dwa podpisy potrzebne do uwolnienia środków z portfela Multisig. Sprawdź transakcję po raz ostatni i jeśli wszystko jest w porządku, kliknij "*Broadcast Transaction*", aby rozgłosić ją w sieci.


![Image](assets/fr/53.webp)


Tę transakcję znajdziesz w zakładce "*Transactions*" w Sparrow Wallet.


![Image](assets/fr/54.webp)


Gratulacje, wiesz już, jak skonfigurować portfel z wieloma podpisami w Sparrow i jak z niego korzystać. Jeśli ten samouczek okazał się przydatny, będę wdzięczny za pozostawienie kciuka w górę poniżej. Zapraszam do udostępnienia tego artykułu w swoich sieciach społecznościowych. Dziękuję za udostępnianie!


Aby pójść dalej, polecam ten samouczek o innej metodzie zwiększania bezpieczeństwa portfela Bitcoin — passphrase BIP39:


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
