---
name: BIP-39 Passphrase Ledger
description: Jak dodać passphrase do Ledger Wallet?
---
![cover](assets/cover.webp)


BIP39 passphrase to opcjonalne hasło, które w połączeniu z frazą Mnemonic zapewnia dodatkowy Layer bezpieczeństwa dla deterministycznych i hierarchicznych portfeli Bitcoin. W tym samouczku wspólnie przeanalizujemy, jak skonfigurować passphrase na bezpiecznym Bitcoin Wallet na Ledger (niezależnie od modelu).


Przed rozpoczęciem tego samouczka, jeśli nie jesteś zaznajomiony z koncepcją passphrase, jego działaniem i implikacjami dla twojego Bitcoin Wallet, zdecydowanie zalecam zapoznanie się z tym innym artykułem teoretycznym, w którym wyjaśniam wszystko:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## Jak działa passphrase na Ledger?


W przypadku urządzeń Ledger dostępne są dwie różne opcje konfiguracji passphrase na Wallet: opcja "*PIN-tied*" i opcja "*temporary*".


Opcja "*PIN-tied*" umożliwia powiązanie passphrase z drugim kodem PIN na Ledger. Oznacza to, że będziesz mieć 2 kody PIN: jeden, aby uzyskać dostęp do zwykłego Wallet bez passphrase, a drugi, aby uzyskać dostęp do drugiego Wallet chronionego przez passphrase.


![PASSPHRASE BIP39](assets/notext/03.webp)


Zasadniczo, nawet z tą opcją passphrase powiązaną z drugim kodem PIN, twój passphrase pozostaje twoim passphrase. Oznacza to, że w przypadku utraty Ledger i chęci odzyskania bitcoinów na innym urządzeniu lub oprogramowaniu, bezwzględnie potrzebna będzie 24-wyrazowa fraza i **kompletny passphrase**. PIN powiązany z passphrase jest używany tylko w celu uzyskania dostępu do niego na bieżącym Ledger, ale nie działa na innych Ledgerach lub innym oprogramowaniu. Dlatego ważne jest, aby wykonać pełną kopię zapasową passphrase na nośniku fizycznym. **Sama znajomość dodatkowego kodu PIN nie wystarczy do odzyskania dostępu do Wallet**; jest to po prostu wygodna funkcja Ledger.


Ta druga opcja kodu PIN jest szczególnie interesująca w przypadku ataków fizycznych. Na przykład, jeśli atakujący zmusi cię do odblokowania urządzenia w celu kradzieży środków, możesz użyć pierwszego kodu PIN, aby uzyskać dostęp do wabika Wallet zawierającego niewielką ilość bitcoinów, jednocześnie chroniąc główne środki za drugim kodem PIN.


Co więcej, opcja ta oferuje wszystkie korzyści związane z bezpieczeństwem BIP39 passphrase bez konieczności ręcznego wprowadzania go za każdym razem, gdy korzystasz z urządzenia podpisującego. Pozwala to na użycie długiego i losowego passphrase, wzmacniając w ten sposób ochronę przed atakami typu brute force, jednocześnie unikając trudności związanych z koniecznością ręcznego wpisywania go za każdym razem na małych przyciskach urządzenia.

Opcja "tymczasowego passphrase" nie zapisuje passphrase na urządzeniu. Za każdym razem, gdy chcesz uzyskać dostęp do chronionego Wallet, musisz ręcznie wprowadzić passphrase na Ledger. Sprawia to, że użytkowanie jest bardziej uciążliwe, ale także nieznacznie zwiększa bezpieczeństwo, nie pozostawiając śladu passphrase na urządzeniu. Po wyłączeniu urządzenie powraca do stanu domyślnego i wymaga ponownego wprowadzenia pełnego passphrase, aby uzyskać dostęp do ukrytych kont. Ta opcja "tymczasowego passphrase" jest zatem podobna do działania innych portfeli sprzętowych.

W tym samouczku użyję Ledger Flex jako przykładu. Jeśli jednak używasz innego modelu Ledger, proces pozostaje taki sam. W przypadku Ledger Stax, Interface jest taki sam jak Ledger Flex. Jeśli chodzi o modele Nano S, Nano S Plus i Nano X, mimo że Interface jest inny, proces i nazwy menu pozostają takie same.


**Uwaga:** Jeśli otrzymałeś już bitcoiny na swoim Ledger przed aktywacją passphrase, będziesz musiał przenieść je za pośrednictwem transakcji Bitcoin. passphrase generuje zestaw nowych kluczy, tworząc w ten sposób Wallet, który jest całkowicie niezależny od początkowego Wallet. Po dodaniu passphrase otrzymasz nowy Wallet, który będzie pusty. Nie powoduje to jednak usunięcia pierwszego Wallet bez passphrase. Nadal można uzyskać do niego dostęp, bezpośrednio za pośrednictwem Ledger bez wprowadzania passphrase lub za pośrednictwem innego oprogramowania przy użyciu 24-wyrazowej frazy.


Przed rozpoczęciem tego samouczka upewnij się, że zainicjowałeś już swój Ledger i wygenerowałeś frazę Mnemonic. Jeśli tak nie jest, a twój Ledger jest nowy, postępuj zgodnie z samouczkiem dla twojego modelu dostępnym w PlanB Network. Po wykonaniu tego kroku można powrócić do tego samouczka.


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

## Jak skonfigurować tymczasowy passphrase z Ledger?


Na stronie głównej Ledger kliknij koło zębate ustawień.


![PASSPHRASE BIP39](assets/notext/04.webp)


Wybierz menu "Zaawansowane", a następnie "Ustaw passphrase".


![PASSPHRASE BIP39](assets/notext/05.webp)


Jest to krok, w którym możesz wybrać między opcją "połączoną z PIN" lub "tymczasową", o której mówiliśmy w poprzedniej części. Tutaj wyjaśnię, jak skonfigurować tymczasowy passphrase, więc kliknij "Ustaw tymczasowy passphrase".


![PASSPHRASE BIP39](assets/notext/06.webp)

Następnie zostaniesz poproszony o wprowadzenie swojego passphrase. Wybierz silny passphrase i natychmiast przejdź do fizycznej kopii zapasowej, na nośniku takim jak papier lub metal. W tym przykładzie wybrałem passphrase: `fH3&kL@9mP#2sD5qR!82`. Po wprowadzeniu passphrase kliknij przycisk "*Kontynuuj*".

![PASSPHRASE BIP39](assets/notext/07.webp)


Sprawdź, czy twój passphrase zgadza się z tym, co zanotowałeś na fizycznej kopii zapasowej, a następnie kliknij przycisk "*Tak, to prawda*", aby potwierdzić.


![PASSPHRASE BIP39](assets/notext/08.webp)


Aby zakończyć tworzenie passphrase, wprowadź kod PIN Ledger. Od tej pory, gdy będziesz chciał uzyskać dostęp do Wallet za pomocą passphrase na Ledger, będziesz musiał wykonać dokładnie te same kroki, jak opisano tutaj.


![PASSPHRASE BIP39](assets/notext/09.webp)


Możesz teraz zaimportować swój zestaw kluczy publicznych na Sparrow Wallet, aby zarządzać Wallet. W Sparrow będzie to inny Wallet niż początkowy Wallet bez passphrase.


Otwórz Sparrow Wallet. Upewnij się, że oprogramowanie jest podłączone do węzła, a następnie kliknij zakładkę "*File*" i wybierz "*New Wallet*".


![PASSPHRASE BIP39](assets/notext/10.webp)


Wybierz nazwę dla Wallet chronionego przez passphrase. W tym przykładzie wybrałem nazwę wyraźnie zawierającą termin "*passphrase*". Jeśli jednak wolisz zachować dyskrecję tego Wallet na swoim komputerze, możesz wybrać mniej sugestywną nazwę.


![PASSPHRASE BIP39](assets/notext/11.webp)


Wybierz typ skryptu dla Wallet. Radzę wybrać "*Taproot*" lub alternatywnie "*Native SegWit*".


![PASSPHRASE BIP39](assets/notext/12.webp)


Podłącz Ledger do komputera, a następnie kliknij "*Connected Hardware Wallet*". Upewnij się, że wprowadziłeś już swój passphrase na Ledger. Jeśli nie, wróć do poprzednich kroków, aby wprowadzić passphrase. Przed przystąpieniem do skanowania należy również pamiętać o otwarciu aplikacji "*Bitcoin*" na urządzeniu Ledger.


![PASSPHRASE BIP39](assets/notext/13.webp)


Kliknij przycisk "*Scan...*".


![PASSPHRASE BIP39](assets/notext/14.webp)


Kliknij "*Import Keystore*" obok swojego Ledger.


![PASSPHRASE BIP39](assets/notext/15.webp)


Twój Wallet chroniony przez passphrase jest teraz utworzony w Sparrow. Aby potwierdzić, kliknij przycisk "*Zastosuj*".


![PASSPHRASE BIP39](assets/notext/16.webp)

Wybierz silne hasło, aby zabezpieczyć dostęp do Sparrow Wallet. To hasło zapewni bezpieczeństwo dostępu do danych Wallet w Sparrow, co pomaga chronić klucze publiczne, adresy, etykiety i historię transakcji przed nieautoryzowanym dostępem.

Radzę zapisać to hasło w menedżerze haseł, aby go nie zapomnieć.


![PASSPHRASE BIP39](assets/notext/17.webp)


I gotowe, Wallet został utworzony! W menu "*Ustawienia*", Sparrow dostarczy ci twój "*Master fingerprint*". Jest to odcisk palca klucza głównego, używany jako podstawa do uzyskania Wallet. Zdecydowanie zalecam zachowanie kopii tego odcisku palca. W moim przykładzie odpowiada on: `281ee33a`.


![PASSPHRASE BIP39](assets/notext/18.webp)


Pamiętaj o tym, o czym wspomnieliśmy w poprzednich częściach: błąd, nawet niewielki, przy wprowadzaniu passphrase spowoduje generate zupełnie nowego Wallet z innymi kluczami. Za każdym razem, gdy musisz upewnić się, że uzyskujesz dostęp do właściwego Wallet za pomocą właściwego passphrase, sprawdź, czy odcisk palca klucza głównego jest zgodny z tym, który zanotowałeś. Informacje te same w sobie nie stanowią zagrożenia dla bezpieczeństwa środków ani prywatności użytkownika.


Przed użyciem Wallet z passphrase zdecydowanie zalecam wykonanie testu odzyskiwania na sucho. Zanotuj informacje referencyjne, takie jak xpub lub odcisk palca klucza głównego, a następnie zresetuj Ledger, gdy Wallet jest nadal pusty. Następnie spróbuj przywrócić Wallet na Ledger przy użyciu papierowych kopii zapasowych 24-wyrazowej frazy i passphrase. Sprawdź, czy informacje wygenerowane po przywróceniu są zgodne z początkowo zanotowanymi. Jeśli tak jest, można mieć pewność, że papierowe kopie zapasowe są wiarygodne.


## Jak skonfigurować passphrase połączony z PIN z Ledger?


Na stronie głównej Ledger kliknij koło zębate ustawień.


![PASSPHRASE BIP39](assets/notext/19.webp)


Wybierz menu "*Zaawansowane*", a następnie "*Ustaw passphrase*".


![PASSPHRASE BIP39](assets/notext/20.webp)


Jest to krok, w którym możesz wybrać między opcją "*połączony z PIN*" lub "*tymczasowy*", o której mówiliśmy w poprzedniej części. Tutaj wyjaśnię, jak skonfigurować passphrase dołączony do kodu PIN, więc kliknij "*Ustaw passphrase i dołącz go do nowego kodu PIN*".


![PASSPHRASE BIP39](assets/notext/21.webp)

Następnie należy wybrać kod PIN, który będzie powiązany z urządzeniem passphrase. Podobnie jak w przypadku głównego kodu PIN, zaleca się wybranie 8-cyfrowego kodu PIN, możliwie jak najbardziej losowego. Należy również zapisać ten kod w innym miejscu niż to, w którym przechowywany jest Ledger Flex.

W moim przypadku główny kod PIN to `58293647`, a jako dodatkowy kod PIN powiązany z passphrase wybrałem `71425839`.


![PASSPHRASE BIP39](assets/notext/22.webp)


Następnie zostaniesz poproszony o wprowadzenie swojego passphrase. Wybierz silny passphrase i natychmiast przejdź do fizycznej kopii zapasowej na nośniku takim jak papier lub metal. W tym przykładzie wybrałem passphrase: `fH3&kL@9mP#2sD5qR!82`. Po wprowadzeniu passphrase kliknij przycisk "*Kontynuuj*".


![PASSPHRASE BIP39](assets/notext/23.webp)


Sprawdź, czy twój passphrase zgadza się z tym, co zanotowałeś na fizycznej kopii zapasowej, a następnie kliknij przycisk "*Tak, to prawda*", aby potwierdzić.


![PASSPHRASE BIP39](assets/notext/24.webp)


Aby zakończyć tworzenie passphrase, wprowadź główny kod PIN Ledger (nie ten powiązany z passphrase).


![PASSPHRASE BIP39](assets/notext/25.webp)


Od teraz, gdy chcesz uzyskać dostęp do Wallet za pomocą passphrase na Ledger, będziesz musiał wprowadzić nie główny kod PIN, ale dodatkowy kod PIN:


- Główny kod PIN (`58293647`) > Wallet bez passphrase.
- Dodatkowy kod PIN (`71425839`) > Wallet z passphrase.


Możesz teraz zaimportować swój zestaw kluczy publicznych na Sparrow Wallet, aby zarządzać Wallet. W Sparrow będzie to odpowiadało innemu Wallet niż początkowy Wallet bez passphrase.


Otwórz Sparrow Wallet. Upewnij się, że oprogramowanie jest podłączone do węzła, a następnie kliknij zakładkę "*File*" i wybierz "*New Wallet*".


![PASSPHRASE BIP39](assets/notext/26.webp)


Wybierz nazwę dla Wallet chronionego przez passphrase. W tym przykładzie wybrałem nazwę wyraźnie zawierającą termin "*passphrase*". Jeśli jednak wolisz zachować dyskrecję tego Wallet na swoim komputerze, możesz wybrać mniej sugestywną nazwę.


![PASSPHRASE BIP39](assets/notext/27.webp)


Wybierz typ skryptu dla Wallet. Radzę wybrać "*Taproot*" lub, jeśli to niemożliwe, "*Native SegWit*".


![PASSPHRASE BIP39](assets/notext/28.webp)

Podłącz Ledger do komputera, a następnie kliknij "*Connected Hardware Wallet*". Upewnij się, że masz już passphrase na Ledger, odblokowując go za pomocą dodatkowego kodu PIN. Jeśli nie, uruchom ponownie Ledger i wprowadź kod PIN powiązany z passphrase. Przed przystąpieniem do skanowania należy również pamiętać o otwarciu aplikacji "*Bitcoin*" na urządzeniu Ledger.


![PASSPHRASE BIP39](assets/notext/29.webp)


Kliknij przycisk "*Scan...*".


![PASSPHRASE BIP39](assets/notext/30.webp)


Kliknij na "*Import Keystore*".


![PASSPHRASE BIP39](assets/notext/31.webp)


Twój Wallet chroniony przez passphrase jest teraz utworzony w Sparrow. Aby potwierdzić, kliknij przycisk "*Zastosuj*".


![PASSPHRASE BIP39](assets/notext/32.webp)


Wybierz silne hasło, aby zabezpieczyć dostęp do Sparrow Wallet. To hasło zapewni bezpieczeństwo dostępu do danych Wallet w Sparrow, co pomaga chronić klucze publiczne, adresy, etykiety i historię transakcji przed nieautoryzowanym dostępem.


Radzę zapisać to hasło w menedżerze haseł, aby go nie zapomnieć.


![PASSPHRASE BIP39](assets/notext/33.webp)


I gotowe, Wallet jest już utworzony! W menu "*Ustawienia*" Sparrow dostarczy ci twój "*Master fingerprint*". Jest to odcisk palca klucza głównego, używany jako podstawa do wyprowadzenia Wallet. Zdecydowanie zalecam zachowanie kopii tego odcisku palca. W moim przykładzie odpowiada on: `281ee33a`.


![PASSPHRASE BIP39](assets/notext/34.webp)


Pamiętaj o tym, o czym wspomnieliśmy w poprzednich częściach: pomyłka, nawet drobna, przy wprowadzaniu passphrase spowoduje generate zupełnie nowego Wallet z innymi kluczami. Za każdym razem, gdy musisz zapewnić dostęp do właściwego Wallet z właściwym passphrase, sprawdź, czy odcisk palca klucza głównego jest zgodny z tym, który zanotowałeś. Informacje te same w sobie nie stanowią zagrożenia dla bezpieczeństwa środków ani prywatności użytkownika.

Przed użyciem Wallet z passphrase zdecydowanie zalecam wykonanie testu odzyskiwania na sucho. Zanotuj informacje referencyjne, takie jak xpub lub odcisk palca klucza głównego, a następnie zresetuj Ledger, gdy Wallet jest nadal pusty. Następnie spróbuj przywrócić Wallet na Ledger przy użyciu papierowych kopii zapasowych 24-słownej frazy i passphrase. Sprawdź, czy informacje wygenerowane po przywróceniu są zgodne z początkowo zanotowanymi. Jeśli tak jest, można mieć pewność, że kopie zapasowe na papierze są wiarygodne.


Gratulacje, twój Bitcoin Wallet jest teraz zabezpieczony passphrase! Jeśli ten poradnik okazał się pomocny, będę wdzięczny za pozostawienie kciuka w górę poniżej. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dziękuję bardzo!


Polecam również zapoznanie się z innym kompletnym samouczkiem na temat korzystania z Ledger Flex:


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a