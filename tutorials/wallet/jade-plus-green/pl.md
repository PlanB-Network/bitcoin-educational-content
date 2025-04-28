---
name: Jade Plus - Green
description: Łatwa konfiguracja Jade Plus z Green
---
![cover](assets/cover.webp)


Jade Plus to Hardware Wallet zaprojektowany przez Blockstream. Jest to następca klasycznego Jade, z ulepszonym oprogramowaniem, większą liczbą opcji i przeprojektowaną ergonomią dla bardziej intuicyjnego użytkowania. Ta nowa wersja może pochwalić się wspaniałym 1,9-calowym ekranem LCD o szerszej gamie kolorów niż jego poprzednik. Przyciski i nawigacja po menu również zostały zoptymalizowane.


Jade Plus może być używany na wiele sposobów: poprzez przewodowe połączenie USB-C, w trybie "*Air-Gap*" z kartą micro SD (wymagany adapter), przez Bluetooth, a nawet poprzez wymianę kodów QR dzięki zintegrowanej kamerze. Hardware Wallet jest zasilany bateryjnie.


Jest on dostępny od 149,99 USD w podstawowej czarnej wersji, a cena może wzrosnąć nawet o 20 USD w przypadku wersji "*Genesis Grey*" lub "*Lunar Silver*". Jade Plus jest zatem ciekawym wyborem, z zaawansowanymi funkcjami porównywalnymi do tych z wysokiej klasy portfeli sprzętowych, takich jak Coldcard Q lub Passport V2, ale w dość niskiej cenie, zbliżonej do modeli ze średniej półki.


![JADE-PLUS-GREEN](assets/fr/01.webp)


Jade Plus jest kompatybilny z większością oprogramowania do zarządzania Wallet. Oto podsumowanie kompatybilności w momencie pisania tego tekstu (styczeń 2025 r.):


| Desktop | Mobile | USB | Bluetooth | QR | JadeLink | Management software
| ------------------- | ------- | ------ | --- | ----------- | --- | -------- |
| Blockstream Green | 🟢 | 🟢 | 🟢 (Mobile) | 🟢 | 🔴 |
| Liana | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 |
| Sparrow | 🟢 | 🔴 | 🟢 | 🔴 | 🟢 | 🟢 |
| Nunchuk | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |
| Specter | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |
| BlueWallet | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |
| Electrum | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 |
| Keeper | 🔴 | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 |

W tym samouczku skonfigurujemy i użyjemy Jade Plus z aplikacją mobilną Green Wallet firmy Blockstream za pośrednictwem połączenia Bluetooth. Ta konfiguracja jest idealna dla początkujących. Jeśli szukasz bardziej zaawansowanego podejścia, polecam zapoznać się z tym samouczkiem, w którym używamy Jade Plus z Sparrow Wallet w trybie kodów QR:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

## Model bezpieczeństwa Jade Plus


Jade Plus wykorzystuje model bezpieczeństwa oparty na "wirtualnym bezpiecznym elemencie", materializowanym przez "ślepą wyrocznię". Mówiąc konkretnie, mechanizm ten łączy kod PIN wybrany przez użytkownika, sekret hostowany na Jade i sekret przechowywany przez wyrocznię (serwer utrzymywany przez Blockstream), aby utworzyć klucz AES-256 dystrybuowany przez dwa podmioty. Podczas inicjacji ECDH Exchange zabezpiecza komunikację z wyrocznią i szyfruje frazę odzyskiwania na Hardware Wallet. W praktyce, gdy chcesz uzyskać dostęp do seed w celu podpisania transakcji, potrzebujesz dostępu do :




- Do samego urządzenia Jade Plus;
- Aby wprowadzić kod PIN w celu odblokowania urządzenia ;
- I do tajemnicy wyroczni.


Główną zaletą tego podejścia jest brak pojedynczego punktu awarii na poziomie sprzętowym, ponieważ jeśli atakujący kiedykolwiek uzyska dostęp do Jade, wyodrębnienie kluczy wymaga jednoczesnego naruszenia Jade i wyroczni. Model ten oznacza również, że Jade Plus jest całkowicie open-source, unikając ograniczeń związanych z wykorzystaniem prawdziwie fizycznie bezpiecznych Elements, takich jak te stosowane na przykład w Ledger.


Wadą tego systemu jest to, że korzystanie z Jade Plus zależy od wyroczni utrzymywanej przez Blockstream. Jeśli ta wyrocznia stanie się niedostępna, nie będzie już możliwe korzystanie z Hardware Wallet bezpośrednio za pomocą kodu PIN. Nie oznacza to jednak, że bitcoiny zostaną utracone, ponieważ nadal można je odzyskać za pomocą frazy odzyskiwania, którą można wprowadzić w Jade Plus w trybie "*stateless*". Aby obejść tę zależność, można również skonfigurować własny serwer Oracle i zarządzać nim.


## Rozpakowywanie Jade Plus


Po otrzymaniu Jade Plus sprawdź, czy pudełko i Seal są w dobrym stanie, aby upewnić się, że paczka nie była otwierana.


![JADE-PLUS-GREEN](assets/fr/02.webp)


W pudełku znajdują się :




- Le Jade Plus;
- Kabel USB-C;
- Karty do nagrywania frazy Mnemonic jako słowa lub jako "*CompactSeedQR*";
- Niektóre instrukcje użytkowania ;
- Przewód;
- Niektóre naklejki.


![JADE-PLUS-GREEN](assets/fr/03.webp)


Urządzenie posiada 4 przyciski nawigacyjne:




- Przycisk w prawym dolnym rogu włącza Jade;
- Duży przycisk z przodu urządzenia służy do wybierania pozycji;
- Dwa małe przyciski u góry umożliwiają nawigację w lewo i w prawo;
- Można również wybrać element, klikając jednocześnie dwa przyciski w górnej części urządzenia.


![JADE-PLUS-GREEN](assets/fr/04.webp)


## Konfiguracja nowego Bitcoin Wallet


Kliknij przycisk Start.


![JADE-PLUS-GREEN](assets/fr/05.webp)


Kliknij na "*Setup Jade*".


![JADE-PLUS-GREEN](assets/fr/06.webp)


Wybierz opcję "Rozpocznij konfigurację". Opcja "*Advanced Setup*" robi to samo, ale z dostępem do zaawansowanych ustawień.


![JADE-PLUS-GREEN](assets/fr/07.webp)


Następnie kliknij "*Create a New Wallet*", aby utworzyć nowy seed w generate.


![JADE-PLUS-GREEN](assets/fr/08.webp)


Kliknij przycisk "*Kontynuuj*", aby wyświetlić nową frazę odzyskiwania.


![JADE-PLUS-GREEN](assets/fr/09.webp)


Jade Plus wyświetla 12-wyrazową frazę Mnemonic. **Mnemonic daje ci pełny, nieograniczony dostęp do wszystkich twoich bitcoinów. Każdy, kto posiada tę frazę, może ukraść środki, nawet bez fizycznego dostępu do Jade Plus. 12-wyrazowa fraza przywraca dostęp do bitcoinów w przypadku utraty, kradzieży lub uszkodzenia Jadeitów. Dlatego bardzo ważne jest, aby zachować ją ostrożnie i przechowywać w bezpiecznym miejscu.


Napis można umieścić na kartonie dołączonym do pudełka lub, dla większego bezpieczeństwa, zalecam wygrawerowanie go na podstawie ze stali nierdzewnej, aby chronić go przed pożarem, powodzią lub upadkiem.


![JADE-PLUS-GREEN](assets/fr/10.webp)


Aby uzyskać więcej informacji na temat prawidłowego sposobu zapisywania i zarządzania frazą Mnemonic, zdecydowanie polecam skorzystanie z tego samouczka, zwłaszcza jeśli jesteś początkującym:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

***Oczywiście nigdy nie wolno dzielić się tymi słowami w Internecie, tak jak robię to w tym samouczku. Ten przykładowy Wallet będzie używany tylko na Testnet i zostanie usunięty pod koniec samouczka


Kliknij strzałkę po prawej stronie ekranu, aby wyświetlić następujące słowa.


![JADE-PLUS-GREEN](assets/fr/11.webp)


Po zapisaniu frazy Jade Plus poprosi o jej potwierdzenie. Wybierz właściwe słowo zgodnie z kolejnością za pomocą przycisków w górnej części urządzenia i kliknij środkowy przycisk, aby przejść do następnego słowa.


![JADE-PLUS-GREEN](assets/fr/12.webp)


## Podłączanie Jade Plus do Green Wallet


W tym samouczku użyjemy aplikacji Green Wallet do zarządzania Wallet hostowanym na Jade Plus. Ta metoda jest szczególnie odpowiednia dla początkujących. Jeśli chcesz bardziej szczegółowo zarządzać Bitcoin Wallet, możesz również użyć Sparrow Wallet, który omówimy w osobnym samouczku:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

Instrukcje dotyczące instalacji i konfiguracji aplikacji Blockstream Green można znaleźć w pierwszej części tego samouczka:


https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143

Po uruchomieniu aplikacji Blockstream Green kliknij przycisk "*Konfiguruj nowy Wallet*".


![JADE-PLUS-GREEN](assets/fr/13.webp)


Wybierz opcję "*On Hardware Wallet*".


![JADE-PLUS-GREEN](assets/fr/14.webp)


Aktywuj Bluetooth na swoim smartfonie, a następnie kliknij przycisk "*Connect your Jade*".


![JADE-PLUS-GREEN](assets/fr/15.webp)


Autoryzuj aplikację Green, aby uzyskać dostęp do połączeń Bluetooth.


![JADE-PLUS-GREEN](assets/fr/16.webp)


Aplikacja szuka Twojego Jade Plus.


![JADE-PLUS-GREEN](assets/fr/17.webp)


W Jade Plus kliknij menu "*Bluetooth*".


![JADE-PLUS-GREEN](assets/fr/18.webp)


Wybierz urządzenie w aplikacji Green.


![JADE-PLUS-GREEN](assets/fr/19.webp)


Potwierdź kod parowania na Jade Plus.


![JADE-PLUS-GREEN](assets/fr/20.webp)


Green oferuje test, aby upewnić się, że twój Jade jest autentyczny. W tym celu należy kliknąć przycisk.


![JADE-PLUS-GREEN](assets/fr/21.webp)


Potwierdź na Jade.


![JADE-PLUS-GREEN](assets/fr/22.webp)


Green potwierdza, że urządzenie jest oryginalne.


![JADE-PLUS-GREEN](assets/fr/23.webp)


## Ustawianie kodu PIN


Kliknij przycisk "*Kontynuuj*", aby wybrać kod PIN Jade.


![JADE-PLUS-GREEN](assets/fr/24.webp)


Kod PIN odblokowuje Jade. Stanowi on zatem ochronę przed nieautoryzowanym dostępem fizycznym. Ten kod PIN nie bierze udziału w tworzeniu kluczy kryptograficznych Wallet. Tak więc, nawet bez dostępu do tego kodu PIN, posiadanie 12-wyrazowej frazy Mnemonic umożliwi odzyskanie dostępu do bitcoinów. Zalecamy wybranie jak najbardziej losowego kodu PIN. I pamiętaj, aby zapisać ten kod w miejscu innym niż to, w którym przechowywane są twoje Jade (np. w menedżerze haseł).


Wybierz 6-cyfrowy kod PIN na urządzeniu Jade, używając przycisków w prawo i w lewo do przewijania cyfr oraz środkowego przycisku do potwierdzenia wprowadzenia cyfry.


![JADE-PLUS-GREEN](assets/fr/25.webp)


Potwierdź kod PIN po raz drugi.


![JADE-PLUS-GREEN](assets/fr/26.webp)


Twój Bitcoin Wallet został utworzony.


![JADE-PLUS-GREEN](assets/fr/27.webp)


## Utwórz konto Bitcoin


Musisz teraz utworzyć konto w Wallet. Kliknij przycisk "*Create an account*" (Utwórz konto).


![JADE-PLUS-GREEN](assets/fr/28.webp)


Wybierz "*Standard*", jeśli chcesz utworzyć klasyczny pojedynczy kod Wallet.


![JADE-PLUS-GREEN](assets/fr/29.webp)


Więcej informacji na temat opcji "*2FA*" można znaleźć w tym poradniku:


https://planb.network/tutorials/wallet/mobile/blockstream-green-2fa-37397d5c-5c27-44ad-a27a-c9ceac8c9df9

Twoje konto zostało utworzone.


![JADE-PLUS-GREEN](assets/fr/30.webp)


Jeśli chcesz spersonalizować Green Wallet, kliknij trzy małe kropki w prawym górnym rogu.


![JADE-PLUS-GREEN](assets/fr/31.webp)


Opcja "*Rename*" umożliwia dostosowanie nazwy Wallet, co jest szczególnie przydatne w przypadku zarządzania kilkoma portfelami w tej samej aplikacji. Menu "*Unit*" pozwala zmienić podstawową jednostkę Wallet. Można na przykład wybrać wyświetlanie w satoshis zamiast w bitcoinach. Wreszcie, menu "*Parameters*" daje dostęp do innych opcji. Znajdziesz tu na przykład rozszerzony klucz publiczny i jego deskryptor, przydatne, jeśli planujesz skonfigurować Watch-only wallet z Jade.


![JADE-PLUS-GREEN](assets/fr/32.webp)


Aby ponownie połączyć się z urządzeniem Jade po jego wyłączeniu, naciśnij przycisk włączania/wyłączania znajdujący się w dolnej części urządzenia. W aplikacji Green wybierz urządzenie ze strony głównej:


![JADE-PLUS-GREEN](assets/fr/33.webp)


Następnie wprowadź kod PIN na Jade, aby ponownie nawiązać połączenie.


![JADE-PLUS-GREEN](assets/fr/34.webp)


Jade jest odblokowywany za pomocą "wirtualnego bezpiecznego elementu" Blockstream (patrz pierwsza sekcja tego samouczka). Wymaga to połączenia Bluetooth z aplikacją Green. Jeśli napotkasz trudności z połączeniem Bluetooth podczas odblokowywania, spróbuj rozłączyć i ponownie skojarzyć oba urządzenia. Jeśli problem nie ustąpi, nadal można odblokować Jade, wybierając opcję "*QR Scan*" i postępując zgodnie z instrukcjami dostępnymi [na stronie Blockstream] (https://jadefw.blockstream.com/pinqr/index.html).


Przed otrzymaniem pierwszych bitcoinów w Wallet, **Zalecam wykonanie pustego testu odzyskiwania**. Zanotuj informacje referencyjne, takie jak xpub lub pierwszy otrzymany Address, a następnie usuń Wallet w aplikacji Green i na Jade Plus, gdy jest jeszcze pusty (`Opcje -> Urządzenie -> Przywracanie ustawień fabrycznych`). Następnie spróbuj przywrócić Wallet przy użyciu papierowych kopii zapasowych frazy Mnemonic. Sprawdź, czy informacje cookie wygenerowane po przywróceniu są zgodne z pierwotnie zapisanymi. Jeśli tak, można mieć pewność, że papierowe kopie zapasowe są wiarygodne. Aby dowiedzieć się więcej o tym, jak przeprowadzić odzyskiwanie testowe, zapoznaj się z tym innym samouczkiem :


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Odbieranie bitcoinów


Teraz, gdy twój Bitcoin Wallet jest skonfigurowany, jesteś gotowy, aby odebrać swój pierwszy Sats! Wystarczy kliknąć przycisk "*Odbierz*" w aplikacji Green.


![JADE-PLUS-GREEN](assets/fr/35.webp)


Green wyświetla odbiór Address, ale przed jego użyciem konieczne jest sprawdzenie go na Jade, aby potwierdzić, że faktycznie należy do naszego Wallet. Aby to zrobić, kliknij przycisk "*Weryfikuj na urządzeniu*".


![JADE-PLUS-GREEN](assets/fr/36.webp)


Sprawdź na Jade, czy Address jest taki sam jak na Green, a następnie kliknij przycisk, aby potwierdzić.


![JADE-PLUS-GREEN](assets/fr/37.webp)


Możesz teraz udostępnić Address płatnikowi, aby otrzymać bitcoiny w swoim Wallet. Gdy transakcja zostanie rozgłaszana w sieci, pojawi się w Wallet. Poczekaj, aż otrzymasz wystarczającą liczbę potwierdzeń, aby uznać transakcję za ostateczną.


![JADE-PLUS-GREEN](assets/fr/38.webp)


## Wysyłanie bitcoinów


Mając bitcoiny w Wallet, możesz teraz również wysyłać bitcoiny. Kliknij "*Wyślij*".


![JADE-PLUS-GREEN](assets/fr/39.webp)


Na następnej stronie wprowadź numer Address odbiorcy. Można wprowadzić go ręcznie lub zeskanować kod QR.


![JADE-PLUS-GREEN](assets/fr/40.webp)


Wybierz kwotę płatności.


![JADE-PLUS-GREEN](assets/fr/41.webp)


W dolnej części ekranu można wybrać stawkę opłaty dla tej transakcji. Użytkownik ma do wyboru zastosowanie się do zaleceń aplikacji lub dostosowanie własnych opłat. Im wyższa opłata w stosunku do innych oczekujących transakcji, tym szybciej transakcja zostanie przetworzona. Informacje na temat rynku opłat można znaleźć na stronie [Mempool.space](https://Mempool.space/) w sekcji "*Opłaty transakcyjne*".


![JADE-PLUS-GREEN](assets/fr/42.webp)


Kliknij "*Next*", aby przejść do ekranu podsumowania transakcji. Sprawdź, czy Address, kwota i opłaty są prawidłowe.


![JADE-PLUS-GREEN](assets/fr/43.webp)


Jeśli wszystko pójdzie dobrze, przesuń przycisk Green u dołu ekranu w prawo, aby podpisać i rozgłosić transakcję w sieci Bitcoin.


![JADE-PLUS-GREEN](assets/fr/44.webp)


Zostaniesz teraz poproszony o potwierdzenie transakcji na Jade.


![JADE-PLUS-GREEN](assets/fr/45.webp)


Upewnij się, że numer Address odbiorcy jest prawidłowy. Kliknij znacznik wyboru, aby potwierdzić.


![JADE-PLUS-GREEN](assets/fr/46.webp)


Sprawdź, czy kwota doładowania jest prawidłowa, a następnie zatwierdź.


![JADE-PLUS-GREEN](assets/fr/47.webp)


Twoja transakcja została podpisana i nadana z Green.


![JADE-PLUS-GREEN](assets/fr/48.webp)


Gratulacje, wiesz już jak skonfigurować i używać Jade Plus z aplikacją mobilną Blockstream Green poprzez połączenie Bluetooth. Jeśli ten poradnik okazał się przydatny, będę wdzięczny za pozostawienie poniżej kciuka Green. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dzięki za udostępnienie!


Aby pójść o krok dalej, polecam ten samouczek dotyczący Jade Plus, w którym konfigurujemy go za pomocą oprogramowania Sparrow Wallet w trybie QR. Dowiesz się również, jak korzystać z zaawansowanych ustawień Hardware Wallet:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262