---
name: Portal
description: Konfiguracja i korzystanie z Portalu Hardware Wallet TwentyTwo-Devices
---
![cover](assets/cover.webp)


Portal to Bitcoin Hardware Wallet zaprojektowany przez TwentyTwo Devices, firmę specjalizującą się w tworzeniu open-source'owych portfeli sprzętowych dla bitcoinerów. Założona przez Alekosa Filiniego, twórcę projektu Magical Bitcoin ([odtąd nazywanego BDK](https://github.com/bitcoindevkit)) i pracującego dla Blockstream i BHB Network, TwentyTwo Devices koncentruje się na autonomii użytkownika, prostocie i bezpieczeństwie.


To, co odróżnia Portal od innych portfeli sprzętowych na rynku, to natywna integracja ze smartfonami. Działa bez kabli i baterii. Wykorzystuje technologię NFC do zasilania i komunikacji z dowolnym kompatybilnym urządzeniem mobilnym Wallet. Jego intrygująca konstrukcja została zaprojektowana z myślą o ergonomicznym użytkowaniu. Okrągła część jest umieszczona z tyłu smartfona, aby odsłonić ekran, na którym można sprawdzić szczegóły transakcji przed ich podpisaniem za pomocą dedykowanego przycisku.


![Image](assets/fr/01.webp)


W całości open-source'owy, Portal bazuje na firmware napisanym w Rust i wykorzystuje BDK (Bitcoin Dev Kit) do zarządzania kluczami i transakcjami. Sprzedawany jest za 89 euro [na oficjalnej stronie internetowej] (https://store.twenty-two.xyz/products/portal-hardware-Wallet).


W chwili pisania tego tekstu Portal jest kompatybilny z aplikacjami Nunchuk i Bitcoin Keeper. W tym samouczku skonfigurujemy go z Nunchukiem.


## Unboxing


Po otrzymaniu portalu należy sprawdzić, czy pudełko i etykieta zabezpieczająca są w dobrym stanie. Portal znajduje się w zapieczętowanym woreczku.


Upewnij się, że Seal jest nienaruszony, aby potwierdzić, że woreczek nie został otwarty. Unikalny numer wyświetlany dużymi literami na woreczku powinien odpowiadać numerowi zapisanemu na czarno pod niebieskim Seal, numerowi na etykiecie pudełka oraz numerowi, który pojawi się na ekranie podczas pierwszego uruchomienia.


![Image](assets/fr/02.webp)


## Instalacja nunchuka


Do zarządzania Wallet hostowanym na Portalu użyjemy aplikacji Nunchuk. Pobierz aplikację z [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Store](https://apps.apple.com/us/app/nunchuk-Bitcoin-Wallet/id1563190073) lub bezpośrednio przez [plik `.apk`](https://github.com/nunchuk-io/nunchuk-android/releases).


![Image](assets/fr/03.webp)


Jeśli używasz Nunchuka po raz pierwszy, aplikacja poprosi cię o utworzenie konta. Na potrzeby tego samouczka nie jest to konieczne. Wybierz "*Kontynuuj jako gość*", aby kontynuować bez konta.


![Image](assets/fr/04.webp)


## Konfiguracja portalu


Na ekranie głównym Nunchuka kliknij logo "*NFC*" w górnej części ekranu.


![Image](assets/fr/05.webp)


Umieść portal z tyłu smartfona, aby go aktywować.


![Image](assets/fr/06.webp)


Nunchuk rozpozna twój portal. Następnie kliknij "*Kontynuuj*".


![Image](assets/fr/07.webp)


Aby utworzyć nowy Wallet, wybierz "*generate seed on Portal*", a następnie kliknij "*Continue*".


![Image](assets/fr/08.webp)


Do wyboru jest 12- lub 24-wyrazowa fraza Mnemonic. Bezpieczeństwo oferowane przez obie opcje jest podobne, więc możesz wybrać tę, która jest najłatwiejsza do zapisania, tj. 12 słów.


![Image](assets/fr/09.webp)


Następnie zostaniesz poproszony o wybranie hasła. Hasło odblokowuje portal. Zapewnia zatem ochronę przed nieautoryzowanym dostępem fizycznym. Hasło to nie bierze udziału w tworzeniu kluczy kryptograficznych Wallet. Tak więc, nawet bez dostępu do tego hasła, posiadanie 12- lub 24-wyrazowej frazy Mnemonic umożliwi odzyskanie dostępu do bitcoinów. Zaleca się wybranie hasła, które jest jak najbardziej losowe i wystarczająco długie. Upewnij się, że zapisujesz to hasło w miejscu innym niż to, w którym przechowywany jest Twój portal (np. w menedżerze haseł).


![Image](assets/fr/10.webp)


Portal wyświetli 12-wyrazową frazę Mnemonic. Mnemonic daje pełny, nieograniczony dostęp do wszystkich bitcoinów. Każdy, kto posiada tę frazę, może ukraść środki, nawet bez fizycznego dostępu do portalu.


12-wyrazowa fraza przywraca dostęp do bitcoinów w przypadku utraty, kradzieży lub uszkodzenia portalu. Dlatego bardzo ważne jest, aby zapisać ją ostrożnie i przechowywać w bezpiecznym miejscu.


Można go wygrawerować na kartce papieru lub dla większego bezpieczeństwa polecam wygrawerowanie go na podstawie ze stali nierdzewnej, aby chronić go przed pożarem, powodzią lub zawaleniem.


Aby uzyskać więcej informacji na temat prawidłowego sposobu zapisywania i zarządzania frazą Mnemonic, zdecydowanie polecam skorzystanie z tego samouczka, zwłaszcza jeśli jesteś początkującym:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

oczywiście nigdy nie wolno dzielić się tymi słowami w Internecie, tak jak ja to robię w tym poradniku. Ten przykładowy Wallet będzie używany tylko na Testnet i zostanie usunięty pod koniec samouczka


Naciśnij mocno przycisk na portalu, aby przejść do następnych słów. Upewnij się, że umieściłeś cały palec na przycisku i przytrzymałeś nacisk przez kilka sekund, aby interakcja została prawidłowo wykryta.


![Image](assets/fr/11.webp)


Portal potwierdzi hasło wprowadzone w Nunchuk.


![Image](assets/fr/12.webp)


Zakończyłeś konfigurację portalu i tworzenie frazy Mnemonic!


![Image](assets/fr/13.webp)


## Konfiguracja Bitcoin Wallet


Na Nunchuku kliknij "*Kontynuuj*", wciąż trzymając portal z tyłu telefonu.


![Image](assets/fr/14.webp)


W tym samouczku zamierzam skonfigurować Wallet single-sig, więc wybieram tę opcję.


![Image](assets/fr/15.webp)


Użyj domyślnego konta, tj. pierwszego konta w Wallet (numer 0). Nunchuk poprosi o potwierdzenie hasła do Portalu, aby go odblokować.


![Image](assets/fr/16.webp)


Na Portalu potwierdź eksport swojego xpub do Nunchuka. Pozwala to na zarządzanie Wallet ze smartfona bez możliwości wydawania bitcoinów bez Portalu. Naciśnij przycisk, aby potwierdzić.


Należy pamiętać, że ścieżka wyprowadzania wskazana w twoim przypadku będzie inna niż moja, ponieważ ten samouczek jest wykonywany na Testnet.


![Image](assets/fr/17.webp)


Nazwij swój Wallet, na przykład "*Portal*", a następnie kliknij "*Kontynuuj*".


![Image](assets/fr/18.webp)


Następnie Nunchuk wyświetli Deskryptor. Dobrym pomysłem jest zrobienie kopii zapasowej. Chociaż Deskryptor nie pozwala na wydawanie bitcoinów, umożliwia on śledzenie ścieżek wyprowadzania kluczy z frazy Mnemonic w przypadku odzyskania Wallet. Przechowuj go w bezpiecznym miejscu, ponieważ jego wyciek może nie stanowić problemu w zakresie bezpieczeństwa, ale stanowi problem w zakresie poufności.


Kliknij na "*Done*".


![Image](assets/fr/19.webp)


Teraz należy utworzyć klucze publiczne generate dla Bitcoin Wallet. Aby to zrobić, kliknij przycisk "*Utwórz nowy Wallet*".


![Image](assets/fr/20.webp)


Kliknij ponownie na "*Twórz nowy Wallet*". Następnie wybierz opcję "*Utwórz nowy Wallet przy użyciu istniejących kluczy*".


![Image](assets/fr/21.webp)


Wybierz nazwę dla Wallet i kliknij "*Kontynuuj*".


![Image](assets/fr/22.webp)


Wybierz swój portal jako urządzenie podpisujące dla tego nowego zestawu kluczy, a następnie kliknij "*Kontynuuj*".


![Image](assets/fr/23.webp)


Jeśli wszystko jest satysfakcjonujące, zatwierdź utwór.


![Image](assets/fr/24.webp)


Następnie można zapisać plik konfiguracyjny Wallet. Plik ten zawiera tylko klucze publiczne, co oznacza, że nawet jeśli ktoś uzyska do niego dostęp, nie będzie w stanie ukraść bitcoinów. Będzie jednak w stanie śledzić wszystkie twoje transakcje. Plik ten stanowi zatem jedynie zagrożenie dla prywatności użytkownika. W niektórych przypadkach może być niezbędny do odzyskania Wallet.


![Image](assets/fr/25.webp)


I to już wszystko!


![Image](assets/fr/26.webp)


## Jak mogę otrzymywać bitcoiny za pomocą Portal?


Aby otrzymywać bitcoiny, wybierz Wallet.


![Image](assets/fr/27.webp)


Przed użyciem wygenerowanego Address należy sprawdzić go na ekranie portalu. Aby to zrobić, kliknij "*Receive*".


![Image](assets/fr/28.webp)


Kliknij trzy kropki, a następnie wybierz "*Weryfikuj Address przez PORTAL*". Następnie wprowadź hasło.


![Image](assets/fr/29.webp)


Umieść portal z tyłu telefonu, a następnie potwierdź, naciskając przycisk.


![Image](assets/fr/30.webp)


Upewnij się, że adres Address wyświetlany na Portalu zgadza się z adresem na Twoim Nunchuku, a następnie potwierdź naciskając przycisk ponownie. Jeśli adresy są identyczne, możesz przekazać Address płatnikowi.


![Image](assets/fr/31.webp)


Gdy transakcja płatnika zostanie nadana, pojawi się ona w Wallet.


![Image](assets/fr/32.webp)


Kliknij "*Wyświetl narożniki*".


![Image](assets/fr/33.webp)


Wybierz swój nowy UTXO.


![Image](assets/fr/34.webp)


Kliknij na "*+*" obok "*Tags*", aby dodać tag do swojego UTXO. Jest to dobra praktyka, ponieważ pomaga zapamiętać, skąd pochodzą monety i optymalizuje prywatność podczas wydawania w przyszłości.


![Image](assets/fr/35.webp)


Wybierz istniejący tag lub utwórz nowy, a następnie kliknij "*Zapisz*". Możesz także utworzyć "*kolekcje*", aby zorganizować swoje części w bardziej uporządkowany sposób.


![Image](assets/fr/36.webp)


## Jak wysyłać bitcoiny za pomocą Portalu?


Teraz, gdy masz bitcoiny w swoim Wallet, możesz je również wysłać. Aby to zrobić, kliknij wybrany Wallet.


![Image](assets/fr/37.webp)


Kliknij przycisk "*Wyślij*".


![Image](assets/fr/38.webp)


Wybierz kwotę do wysłania, a następnie kliknij "*Kontynuuj*".


![Image](assets/fr/39.webp)


Dodaj "*notatkę*" do przyszłej transakcji, aby przypomnieć sobie o jej celu.


![Image](assets/fr/40.webp)


Następnie wprowadź Address odbiorcy w odpowiednim polu. Możesz również zeskanować Address zakodowany jako kod QR, klikając ikonę w prawym górnym rogu ekranu. Następnie kliknij przycisk "*Twórz transakcję*".


![Image](assets/fr/41.webp)


Sprawdź szczegóły transakcji, a następnie kliknij przycisk "*Podpisz*" obok portalu i wprowadź hasło.


![Image](assets/fr/42.webp)


Umieść swój portal z tyłu telefonu. Sprawdź, czy numer Address odbiorcy i kwota są prawidłowe. Jeśli tak, naciśnij przycisk, aby kontynuować.


![Image](assets/fr/43.webp)


Sprawdź, czy opłata za transakcję jest prawidłowa, a następnie ponownie naciśnij przycisk, aby podpisać transakcję.


![Image](assets/fr/44.webp)


Transakcja została podpisana. Możesz po raz ostatni sprawdzić jej szczegóły na Nunchuku, a następnie kliknąć przycisk "*Rozgłoś transakcję*", aby rozgłosić ją w sieci Bitcoin.


![Image](assets/fr/45.webp)


Twoja transakcja oczekuje teraz na potwierdzenie.


![Image](assets/fr/46.webp)


Gratulacje, masz już opanowaną obsługę Portalu! Jeśli ten poradnik okazał się przydatny, będę wdzięczny za pozostawienie kciuka Green poniżej. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dziękuję bardzo!


Aby dowiedzieć się więcej, zapoznaj się z naszym kompletnym szkoleniem na temat działania portfeli HD:


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f