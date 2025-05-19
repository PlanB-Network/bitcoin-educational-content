---
name: Tapsigner
description: Konfiguracja i używanie Tapsignera z Nunchukiem
---
![cover](assets/cover.webp)


Hardware Wallet to urządzenie elektroniczne przeznaczone do zarządzania i zabezpieczania kluczy prywatnych Bitcoin Wallet. W przeciwieństwie do portfeli programowych (lub portfeli Hot) instalowanych na maszynach ogólnego przeznaczenia często podłączonych do Internetu, portfele sprzętowe pozwalają na fizyczną izolację kluczy prywatnych, zmniejszając ryzyko włamania i kradzieży.


Głównym celem Hardware Wallet jest zminimalizowanie funkcjonalności urządzenia w celu zmniejszenia jego powierzchni ataku. Mniejsza powierzchnia ataku oznacza również mniej potencjalnych wektorów ataku, tj. mniej słabych punktów w systemie, które atakujący mogliby wykorzystać, aby uzyskać dostęp do bitcoinów.


Zaleca się korzystanie z Hardware Wallet w celu zabezpieczenia bitcoinów, zwłaszcza w przypadku posiadania znacznych ich ilości, zarówno pod względem wartości bezwzględnej, jak i udziału w całkowitych aktywach.


Portfele sprzętowe są używane w połączeniu z oprogramowaniem zarządzającym Wallet na komputerze lub smartfonie. Oprogramowanie to zarządza tworzeniem transakcji, ale podpis kryptograficzny niezbędny do walidacji tych transakcji jest wykonywany wyłącznie w Hardware Wallet. Oznacza to, że klucze prywatne nigdy nie są narażone na potencjalnie wrażliwe środowisko.


Portfele sprzętowe zapewniają użytkownikowi podwójną ochronę: z jednej strony zabezpieczają bitcoiny przed zdalnymi atakami, utrzymując klucze prywatne w trybie offline, a z drugiej strony generalnie oferują lepszą odporność fizyczną na próby wyodrębnienia kluczy. I to właśnie na podstawie tych 2 kryteriów bezpieczeństwa można ocenić i uszeregować różne modele dostępne na rynku.


W tym samouczku proponuję odkryć jedno z tych rozwiązań: Tapsigner firmy Coinkite.


## Wprowadzenie do aplikacji Tapsigner


Tapsigner to Hardware Wallet zaprojektowany w formie karty NFC przez firmę Coinkite, znaną również z produkcji kart Coldcards.


![TAPSIGNER NUNCHUK](assets/notext/01.webp)


Tapsigner umożliwia przechowywanie pary składającej się z głównego klucza prywatnego i kodu łańcucha zgodnie z BIP32, w celu uzyskania drzewa kluczy kryptograficznych. Klucze te mogą być wykorzystywane do podpisywania transakcji poprzez przyłożenie Tapsignera do telefonu lub czytnika kart NFC.

Ta karta NFC jest sprzedawana za 19,99 USD, co jest bardzo przystępną ceną w porównaniu do innych portfeli sprzętowych dostępnych na rynku. Jednak ze względu na swój format, Tapsigner nie oferuje tak wielu opcji, jak inne urządzenia. Nie ma oczywiście baterii, aparatu ani czytnika kart micro SD, ponieważ jest to karta. Moim zdaniem jego największą wadą jest brak ekranu na Hardware Wallet, co czyni go bardziej podatnym na niektóre rodzaje zdalnych ataków. W rzeczywistości zmusza to użytkownika do podpisywania na ślepo i ufania temu, co widzi na ekranie komputera.


Pomimo swoich ograniczeń, Tapsigner może być interesujący ze względu na obniżoną cenę. Ten Wallet może być w szczególności wykorzystany do zwiększenia bezpieczeństwa Wallet wydatkowego oprócz Wallet oszczędnościowego chronionego przez Hardware Wallet wyposażony w ekran. Jest to również dobre rozwiązanie dla tych, którzy posiadają niewielkie ilości bitcoinów i nie chcą inwestować setek euro w bardziej wyrafinowane urządzenie. Co więcej, wykorzystanie Tapsignera w konfiguracjach Multisig lub potencjalnie w systemach Wallet z blokadą czasową w przyszłości, może zaoferować interesujące korzyści.


## Jak kupić Tapsigner?


Tapsigner jest dostępny do zakupu [na oficjalnej stronie Coinkite](https://store.coinkite.com/store/category/tapsigner). Aby kupić go w sklepie fizycznym, można również znaleźć [listę certyfikowanych sprzedawców](https://coinkite.com/resellers) na stronie.


Potrzebny będzie również telefon kompatybilny z komunikacją NFC lub urządzenie USB do odczytu kart NFC na standardowej częstotliwości 13,56 MHz.


## Jak zainicjować Tapsignera za pomocą Nunchuka?


Po otrzymaniu karty Tapsigner, pierwszym krokiem jest sprawdzenie opakowania, aby upewnić się, że nie zostało ono otwarte. Jeśli opakowanie jest uszkodzone, może to oznaczać, że karta została naruszona i może nie być autentyczna. CoinKite dostarczy twój Tapsigner z etui, które blokuje fale radiowe. Upewnij się, że znajduje się ono w opakowaniu.


![TAPSIGNER NUNCHUK](assets/notext/02.webp)


Do zarządzania Wallet będziemy używać aplikacji mobilnej **Nunchuk Wallet**. Upewnij się, że twój smartfon jest kompatybilny z NFC, a następnie pobierz Nunchuk z [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Store](https://apps.apple.com/us/app/nunchuk-Bitcoin-Wallet/id1563190073) lub bezpośrednio przez [plik `.apk`](https://github.com/nunchuk-io/nunchuk-android/releases).


![TAPSIGNER NUNCHUK](assets/notext/03.webp)

Jeśli używasz Nunchuka po raz pierwszy, aplikacja poprosi cię o utworzenie konta. Na potrzeby tego samouczka nie jest to konieczne. Wybierz więc "*Kontynuuj jako gość*", aby kontynuować bez konta.

![TAPSIGNER NUNCHUK](assets/notext/04.webp)


Następnie kliknij na "*Unassisted Wallet*".


![TAPSIGNER NUNCHUK](assets/notext/05.webp)


Następnie kliknij przycisk "*Badam na własną rękę*".


![TAPSIGNER NUNCHUK](assets/notext/06.webp)


Po wejściu do Nunchuka kliknij przycisk "*+*" obok zakładki "*Keys*".


![TAPSIGNER NUNCHUK](assets/notext/07.webp)


Wybierz "*Dodaj klucz NFC*".


![TAPSIGNER NUNCHUK](assets/notext/08.webp)


Następnie kliknij "*Add TAPSIGNER*".


![TAPSIGNER NUNCHUK](assets/notext/09.webp)


Kliknij "*Kontynuuj*", a następnie przyłóż kartę Tapsigner NFC do smartfona.


![TAPSIGNER NUNCHUK](assets/notext/10.webp)


Jeśli Tapsigner jest nowy, Nunchuk zaproponuje jego inicjalizację. Kliknij "*Tak*".


![TAPSIGNER NUNCHUK](assets/notext/11.webp)


Teraz należy wybrać sposób generate głównego kodu łańcucha.


Tapsigner wykorzystuje standard BIP32. Oznacza to, że wyprowadzanie kluczy kryptograficznych zabezpieczających bitcoiny nie opiera się na frazie Mnemonic, jak w przypadku portfeli BIP39, ale bezpośrednio na głównym kluczu prywatnym i głównym kodzie łańcucha. Te 2 Elements są przekazywane przez funkcję HMAC w celu deterministycznego i hierarchicznego wyprowadzenia reszty Wallet.


Główny klucz prywatny jest generowany bezpośrednio przez TRNG (*True Random Number Generator*) zintegrowany z Tapsigner. Z drugiej strony, główny kod łańcucha musi być dostarczony z zewnątrz. Na tym etapie masz wybór: pozwolić Nunchukowi na generate automatycznie, klikając "*Automatic*", lub generate samodzielnie, wybierając "*Advanced*" i wprowadzając go w odpowiednim polu.


![TAPSIGNER NUNCHUK](assets/notext/12.webp)


Następnie należy wybrać kod PIN. W polu "*Starting PIN*" wprowadź kod PIN zapisany z tyłu urządzenia Tapsigner.


![TAPSIGNER NUNCHUK](assets/notext/13.webp)


Wybierz kod PIN, aby zabezpieczyć fizyczny dostęp do urządzenia Tapsigner. Ten kod PIN nie odgrywa żadnej roli w procesie odzyskiwania Wallet. Jego jedyną funkcją jest odblokowanie urządzenia Tapsigner w celu podpisywania transakcji. Pamiętaj, aby zapisać ten kod PIN, aby go nie zapomnieć. Kliknij "*Kontynuuj*", aby kontynuować.


![TAPSIGNER NUNCHUK](assets/notext/14.webp)

Umieść teraz kartę Tapsigner z tyłu telefonu, aby ją zainicjować.

![TAPSIGNER NUNCHUK](assets/notext/15.webp)


Nunchuk następnie generate plik odzyskiwania dla Wallet, który pozwala odzyskać dostęp do bitcoinów w przypadku utraty karty NFC. Plik ten jest zaszyfrowany kodem zapasowym zapisanym na odwrocie Tapsignera. Aby odzyskać swoje bitcoiny, będziesz bezwzględnie potrzebować tego pliku, a także kodu do jego odszyfrowania. Dlatego ważne jest, aby wykonać papierową kopię tego kodu, ponieważ w przypadku utraty karty NFC dostęp do tego kodu również zostanie utracony, ponieważ na razie jest on zapisany tylko na karcie. Upewnij się również, że utworzyłeś kilka kopii zapasowych zaszyfrowanego pliku odzyskiwania.


![TAPSIGNER NUNCHUK](assets/notext/16.webp)


Wybierz nazwę dla swojego Wallet.


![TAPSIGNER NUNCHUK](assets/notext/17.webp)


Podstawa Wallet jest teraz skonfigurowana. Aby zweryfikować autentyczność urządzenia Tapsigner, w dowolnym momencie można kliknąć przycisk "*Run health check*".


![TAPSIGNER NUNCHUK](assets/notext/18.webp)


Wprowadź kod PIN.


![TAPSIGNER NUNCHUK](assets/notext/19.webp)


Następnie umieść kartę z tyłu telefonu.


![TAPSIGNER NUNCHUK](assets/notext/20.webp)


## Jak utworzyć Wallet na Tapsigner?


Po powrocie na stronę główną Nunchuka możesz zobaczyć, że Twój Tapsigner jest zarejestrowany w dostępnych urządzeniach podpisujących.


![TAPSIGNER NUNCHUK](assets/notext/21.webp)


Teraz należy utworzyć klucze generate dla Bitcoin Wallet. Aby to zrobić, kliknij przycisk "*+*" po prawej stronie zakładki "*Wallets*".


![TAPSIGNER NUNCHUK](assets/notext/22.webp)


Kliknij "*Twórz nowy Wallet*".


![TAPSIGNER NUNCHUK](assets/notext/23.webp)


Następnie wybierz opcję "*Utwórz nowy Wallet przy użyciu istniejących kluczy*".


![TAPSIGNER NUNCHUK](assets/notext/24.webp)


Wybierz nazwę dla Wallet, a następnie kliknij "*Kontynuuj*".


![TAPSIGNER NUNCHUK](assets/notext/25.webp)


Wybierz Tapsigner jako urządzenie podpisujące dla tego nowego zestawu kluczy, a następnie kliknij "*Kontynuuj*".


![TAPSIGNER NUNCHUK](assets/notext/26.webp)


Jeśli wszystko jest w porządku, potwierdź utworzenie.


![TAPSIGNER NUNCHUK](assets/notext/27.webp)

Następnie można zapisać plik konfiguracyjny Wallet. Plik ten zawiera wyłącznie klucze publiczne użytkownika, co oznacza, że nawet jeśli ktoś uzyska do niego dostęp, nie będzie mógł ukraść bitcoinów. Może jednak śledzić wszystkie transakcje. Dlatego plik ten stanowi jedynie zagrożenie dla prywatności użytkownika. W niektórych przypadkach może być niezbędny do odzyskania Wallet.

![TAPSIGNER NUNCHUK](assets/notext/28.webp)


I gotowe, Wallet został pomyślnie utworzony!


![TAPSIGNER NUNCHUK](assets/notext/29.webp)


Gdy nie używasz Tapsignera, pamiętaj o przechowywaniu go w etui dostarczonym przez Coinkite, które blokuje fale radiowe w celu ochrony przed nieautoryzowanymi odczytami.


## Jak otrzymywać bitcoiny na Tapsigner?


Aby otrzymać bitcoiny, kliknij na swój Wallet.


![TAPSIGNER NUNCHUK](assets/notext/30.webp)


Następnie użyj wygenerowanego Address, aby otrzymać bitcoiny. Jeśli wcześniej otrzymałeś bitcoiny na tym Wallet, będziesz musiał kliknąć przycisk "*Odbierz*", aby generate nowy pusty odbierający Address.


![TAPSIGNER NUNCHUK](assets/notext/31.webp)


Gdy transakcja nadawcy zostanie nadana, pojawi się ona w Wallet.


![TAPSIGNER NUNCHUK](assets/notext/32.webp)


Kliknij "*Wyświetl monety*".


![TAPSIGNER NUNCHUK](assets/notext/33.webp)


Wybierz swój nowy UTXO.


![TAPSIGNER NUNCHUK](assets/notext/34.webp)


Kliknij "*+*" obok "*Tags*", aby dodać etykietę do UTXO. Jest to dobra praktyka, ponieważ pomaga zapamiętać pochodzenie monet i zoptymalizować swoją prywatność pod kątem przyszłych wydatków.


![TAPSIGNER NUNCHUK](assets/notext/35.webp)


Wybierz istniejący tag lub utwórz nowy, a następnie kliknij "*Zapisz*". Masz również możliwość tworzenia "*kolekcji*", aby organizować swoje monety w bardziej uporządkowany sposób.


![TAPSIGNER NUNCHUK](assets/notext/36.webp)


## Jak wysyłać bitcoiny za pomocą Tapsigner?


Teraz, gdy masz bitcoiny w swoim Wallet, możesz je również wysłać. Aby to zrobić, kliknij wybrany Wallet.


![TAPSIGNER NUNCHUK](assets/notext/37.webp)


Kliknij przycisk "*Wyślij*".


![TAPSIGNER NUNCHUK](assets/notext/38.webp)


Wybierz kwotę do wysłania, a następnie kliknij "*Kontynuuj*".


![TAPSIGNER NUNCHUK](assets/notext/39.webp)


Dodaj "*note*" do przyszłej transakcji, aby zapamiętać jej cel.


![TAPSIGNER NUNCHUK](assets/notext/40.webp)

Następnie ręcznie wprowadź Address odbiorcy w wyznaczonym polu.

![TAPSIGNER NUNCHUK](assets/notext/41.webp)


Można również zeskanować kod QR zakodowany w Address, klikając ikonę znajdującą się w prawym górnym rogu ekranu.


![TAPSIGNER NUNCHUK](assets/notext/42.webp)


Kliknij przycisk "*Twórz transakcję*".


![TAPSIGNER NUNCHUK](assets/notext/43.webp)


Zweryfikuj szczegóły transakcji, a następnie kliknij przycisk "*Podpisz*" obok swojego podpisu Tapsigner.


![TAPSIGNER NUNCHUK](assets/notext/44.webp)


Wprowadź kod PIN, aby go odblokować.


![TAPSIGNER NUNCHUK](assets/notext/45.webp)


Następnie umieść Tapsigner z tyłu smartfona.


![TAPSIGNER NUNCHUK](assets/notext/46.webp)


Transakcja została podpisana. Sprawdź jeszcze raz, czy wszystko się zgadza, a następnie kliknij "*Broadcast Transaction*", aby rozgłosić transakcję w sieci Bitcoin.


![TAPSIGNER NUNCHUK](assets/notext/47.webp)


Twoja transakcja oczekuje teraz na potwierdzenie.


![TAPSIGNER NUNCHUK](assets/notext/48.webp)


## Jak odzyskać Wallet w przypadku utraty Tapsignera?


W przypadku zgubienia Tapsignera można odzyskać Wallet za pomocą kodu znajdującego się na odwrocie karty. Dlatego ważne jest, aby zapisać ten kod oddzielnie od Tapsignera, ponieważ w przypadku utraty karty dostęp do tego kodu również zostanie utracony. Potrzebna będzie również zaszyfrowana kopia zapasowa Wallet.


Do odzyskania środków użyjemy aplikacji Nunchuk, ale należy pamiętać, że oznacza to tymczasowe zabezpieczenie środków w Hot Wallet. Jeśli twój Tapsigner zabezpieczał znaczne kwoty, rozważ wykonanie tego samego procesu odzyskiwania z nową kartą Coldcard.


Otwórz aplikację Nunchuk i kliknij przycisk "*+*" obok zakładki "*Keys*".


![TAPSIGNER NUNCHUK](assets/notext/49.webp)


Wybierz "*Dodaj klucz NFC*".


![TAPSIGNER NUNCHUK](assets/notext/50.webp)


Wybierz opcję "*Odzyskaj klucz TAPSIGNER z kopii zapasowej*".


![TAPSIGNER NUNCHUK](assets/notext/51.webp)


Nastąpi przekierowanie do eksploratora plików urządzenia. Zlokalizuj i wybierz zaszyfrowany plik kopii zapasowej Wallet. Zazwyczaj nazwa tego pliku zaczyna się od `backup...`.


![TAPSIGNER NUNCHUK](assets/notext/52.webp)


Wprowadź hasło odszyfrowujące plik kopii zapasowej. Hasło to odpowiada hasłu podanemu na odwrocie urządzenia Tapsigner.


![TAPSIGNER NUNCHUK](assets/notext/53.webp)

Następnie wybierz nazwę dla odzyskiwania Wallet.

![TAPSIGNER NUNCHUK](assets/notext/54.webp)


Odzyskałeś dostęp do swoich bitcoinów. Twój Wallet jest teraz zarządzany jako Hot Wallet widoczny w zakładce "*Klucze*" aplikacji Nunchuk. Następnie musisz utworzyć nowy zestaw kluczy kryptograficznych w sekcji "*Wallets*", kojarząc z nim ten klucz. Aby to zrobić, możesz ponownie wykonać kroki opisane w części "*Jak utworzyć Wallet na Tapsignerze?" tego samouczka.


![TAPSIGNER NUNCHUK](assets/notext/55.webp)


Jeśli utraciłeś swój Tapsigner, zdecydowanie radzę natychmiast przenieść swoje bitcoiny na inny Wallet, który posiadasz, najlepiej chroniony przez Hardware Wallet. W rzeczywistości utracony Tapsigner może potencjalnie trafić w niepowołane ręce. Dlatego ważne jest, aby opróżnić Wallet, który właśnie odzyskałeś i przestać go używać.


Gratulacje, jesteś teraz na bieżąco z korzystaniem z Tapsigner! Jeśli ten poradnik okazał się pomocny, będę wdzięczny za pozostawienie kciuka w górę poniżej. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dziękuję bardzo!