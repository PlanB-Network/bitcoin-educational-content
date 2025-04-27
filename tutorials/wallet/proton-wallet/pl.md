---
name: Proton Wallet
description: Instalacja i korzystanie z urządzenia Proton Bitcoin Wallet
---
![cover](assets/cover.webp)


Proton to szwajcarska firma specjalizująca się w prywatności cyfrowej, założona w 2014 roku przez naukowców z CERN. Znana ze swoich rozwiązań open source, Proton oferuje pakiet usług, w tym Proton Mail, Proton VPN i Proton Drive.


Proton niedawno zaprezentował Proton Wallet, open-source'owy, samoobsługowy Bitcoin Wallet dostępny jako aplikacja mobilna lub klient sieciowy, połączony z kontem Proton. Funkcjonalności Wallet są na razie stosunkowo klasyczne, z podstawowymi narzędziami oczekiwanymi od dobrego Bitcoin Wallet, takimi jak RBF (*Replace-by-fee*), tagowanie lub możliwość dodania BIP39 passphrase.


Szczególną cechą tego Wallet jest możliwość wysyłania bitcoinów przy użyciu adresu e-mail Address odbiorcy, dla którego Proton automatycznie generuje pusty Bitcoin Address powiązany z Wallet użytkownika. Proton planuje dodać nowe funkcje w przyszłości, w tym Lightning i coinjoins (prawdopodobnie przy użyciu Whirlpool, jak sugeruje aktywność na ich repozytorium GitHub).


## Utwórz konto Proton


Aby korzystać z Proton Wallet, potrzebujesz konta Proton. Możesz je utworzyć za darmo, wykonując pierwsze kroki tego samouczka poświęconego tworzeniu skrzynki pocztowej Proton (tylko sekcja "*Tworzenie konta Proton*"). Po skonfigurowaniu konta można przejść do dalszej części tego samouczka.


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

## Połączenie z Proton Wallet


Wejdź na [stronę internetową Proton Wallet] (https://proton.me/Wallet) i kliknij przycisk "*Get Proton Wallet*".


![Image](assets/fr/01.webp)


Wybierz opcję subskrypcji "*Free*", a następnie kliknij "*Sign In*".


![Image](assets/fr/02.webp)


Wprowadź adres e-mail i hasło powiązane z kontem Proton, aby się zalogować.


![Image](assets/fr/03.webp)


Twoje konto powinno teraz zostać wyświetlone. Kliknij "*Zacznij korzystać z Proton Wallet teraz*".


![Image](assets/fr/04.webp)


## Utwórz Bitcoin Wallet


Wybierz domyślną walutę fiat dla swojego konta, a następnie kliknij "*Utwórz nowy Wallet*".


![Image](assets/fr/05.webp)


Twój Bitcoin Wallet został utworzony. Teoretycznie możesz zacząć go używać natychmiast, ale bardzo ważne jest, aby najpierw zapisać Mnemonic. Aby to zrobić, kliknij "*Zabezpiecz swój Wallet*" w prawym górnym rogu Interface.


![Image](assets/fr/06.webp)


Jeśli jeszcze tego nie zrobiłeś w Proton, zostaniesz poproszony o utworzenie kopii zapasowej swojego konta i zabezpieczenie go za pomocą metody 2FA. Te środki bezpieczeństwa, choć mają zastosowanie do całego konta Proton, są tym bardziej istotne, gdy Bitcoin Wallet jest z nim zintegrowany. Zdecydowanie zalecam ich wdrożenie.


![Image](assets/fr/07.webp)


Aby zapisać frazę Mnemonic, kliknij na "*Backup this Wallet's seed phrase*".


![Image](assets/fr/08.webp)


Wprowadź hasło do aplikacji Proton.


![Image](assets/fr/09.webp)


Następnie kliknij "*Wyświetl frazę Wallet seed*", aby wyświetlić frazę Wallet Mnemonic.


![Image](assets/fr/10.webp)


Proton Wallet wyświetla 12-wyrazową frazę Mnemonic. **Ten Mnemonic daje ci pełny, nieograniczony dostęp do wszystkich twoich bitcoinów**. Każdy, kto posiada tę frazę, może ukraść twoje środki, nawet bez dostępu do twojego konta Proton. 12-wyrazowa fraza może być użyta do przywrócenia dostępu do bitcoinów w przypadku utraty dostępu do konta. Dlatego bardzo ważne jest, aby zapisać ją ostrożnie i przechowywać w bezpiecznym miejscu.


Możesz napisać go na kartce papieru lub dla większego bezpieczeństwa polecam wygrawerowanie go na podstawie ze stali nierdzewnej, aby chronić go przed pożarem, powodzią lub upadkiem.


![Image](assets/fr/11.webp)


Aby uzyskać więcej informacji na temat prawidłowego sposobu zapisywania i zarządzania frazą Mnemonic, zdecydowanie polecam skorzystanie z tego samouczka, zwłaszcza jeśli jesteś początkującym:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

oczywiście nigdy nie powinieneś robić zdjęć tych słów, w przeciwieństwie do tego, co robię w tym samouczku


Po zapisaniu frazy kliknij przycisk "*Done*".


![Image](assets/fr/12.webp)


## Odkryj Interface


Proton Wallet Interface jest bardzo intuicyjny. Po lewej stronie znajdują się różne portfele i powiązane z nimi konta. Konto "*Primary*" jest kontem głównym. Ze względu na poufność, bitcoiny otrzymane za pośrednictwem poczty elektronicznej Proton Address są umieszczane na osobnym koncie o nazwie "*Bitcoin via Email*".


![Image](assets/fr/13.webp)


Aby dodać nowe konto, kliknij "*Dodaj konto*".


![Image](assets/fr/14.webp)


Aby utworzyć nowy Wallet, kliknij symbol "*+*" obok "*Wallets*".


![Image](assets/fr/15.webp)


W tym miejscu można dodać BIP39 passphrase do nowego Wallet.


![Image](assets/fr/16.webp)


Aby pogłębić swoją wiedzę na temat passphrase, polecam ten samouczek:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## Odbieranie bitcoinów


Aby otrzymać bitcoiny w Wallet, wybierz żądane konto po lewej stronie Interface, a następnie kliknij przycisk "*Odbierz*".


![Image](assets/fr/17.webp)


Następnie Proton Wallet automatycznie generuje nowy, pusty Address.


![Image](assets/fr/18.webp)


Po zakończeniu transakcji znajdziesz ją w sekcji "*Transakcje*". Kliknij "*+Add*", aby przypisać etykietę do transakcji.


![Image](assets/fr/19.webp)


## Wysyłanie bitcoinów


Teraz, gdy masz już bitcoiny w Wallet, możesz je wysłać. Wybierz konto po lewej stronie Interface, a następnie kliknij "*Wyślij*".


![Image](assets/fr/20.webp)


Wprowadź Bitcoin Address odbiorcy. Kod QR można zeskanować, klikając małe logo. Aby wysłać na adres e-mail Address, wprowadź go bezpośrednio w tym polu. Po wprowadzeniu Bitcoin Address, kliknij na małą strzałkę, a następnie na "*Potwierdź*".


![Image](assets/fr/21.webp)


Wprowadź kwotę do wysłania, w walucie fiducjarnej lub w bitcoinach, a następnie kliknij "*Review*".


![Image](assets/fr/22.webp)


Wybierz opłatę transakcyjną w oparciu o aktualną sytuację rynkową.


![Image](assets/fr/23.webp)


Dodaj etykietę do transakcji, a następnie sprawdź wszystkie szczegóły. Jeśli wszystko się zgadza, kliknij "*Potwierdź i wyślij*", aby podpisać i wysłać transakcję.


![Image](assets/fr/24.webp)


Twoja transakcja będzie teraz oczekiwała na potwierdzenie w sekcji "*Transakcje*" na Twoim koncie.


![Image](assets/fr/25.webp)


## Logowanie do aplikacji


Oprócz klienta internetowego, Proton Wallet jest również dostępny za pośrednictwem aplikacji mobilnej. Łącząc Wallet z kontem Proton, można synchronizować Wallet między klientem internetowym a aplikacją mobilną.


Pobierz Proton Wallet ze swojego sklepu z aplikacjami:




- [W App Store](https://apps.apple.com/us/app/proton-Wallet-secure-btc/id6479609548);
- [W sklepie Google Play](https://play.google.com/store/apps/details?id=me.proton.Wallet.android).


![Image](assets/fr/26.webp)


Po instalacji kliknij "*Log in*" i wprowadź swój adres e-mail Address oraz hasło Proton.


![Image](assets/fr/27.webp)


Będziesz mieć wtedy dostęp do swojego Bitcoin Wallet, z tymi samymi funkcjami, co w kliencie internetowym.


![Image](assets/fr/28.webp)


Gratulacje, wiesz już jak skonfigurować i używać Proton Wallet. Jeśli ten poradnik okazał się przydatny, będę wdzięczny za pozostawienie poniżej kciuka Green. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dzięki za udostępnienie!


Aby przejść dalej, polecam ten samouczek na temat Jade Plus, najnowszego Hardware Wallet Blockstream:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262