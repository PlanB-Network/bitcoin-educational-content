---
name: Satscard
description: Konfiguracja i używanie karty Satscard z Nunchukiem
---
![cover](assets/cover.webp)


Bitcoin to elektroniczny system gotówkowy, który pozwala nam przeprowadzać transakcje peer-to-peer. Jednakże, aby być przekonanym, że transakcja jest niezmienna, konieczne jest poczekanie na kilka potwierdzeń (zwykle 6), aby uniknąć jakichkolwiek prób podwójnego wydania środków przez nadawcę. To opóźnienie walidacji może być czasami niewygodne, zwłaszcza gdy pożądana jest natychmiastowa finalność podobna do fizycznej gotówki. W przeciwieństwie do gotówki, gdzie posiadanie banknotu jest przenoszone natychmiast, transakcje Bitcoin wymagają czasu oczekiwania, zanim zostaną ostatecznie uznane za nieodwracalne.


W tym miejscu pojawia się Satscard. Oferuje ona metodę umożliwiającą fizyczną i natychmiastową transmisję bitcoinów, bez konieczności przeprowadzania transakcji On-Chain. Satscard funkcjonuje jako karta na okaziciela, która pozwala na bezpieczny transfer Bitcoin Ownership, oferując tym samym doświadczenie bliższe tradycyjnej gotówce. W tym poradniku przedstawię to rozwiązanie.


## Co to jest karta Satscard?


Satscard firmy Coinkite jest następcą Opendime. Jest to karta NFC, która umożliwia fizyczną transmisję bitcoinów, podobnie jak banknot lub moneta. W przeciwieństwie do tradycyjnego Hardware Wallet, Satscard jest kartą na okaziciela, co oznacza, że fizyczne posiadanie karty jest równoznaczne z Ownership bitcoinów, które są zabezpieczone przechowywanymi na niej kluczami. Jej cena waha się od 6,99 USD do 17,99 USD w zależności od wybranego wzoru.


![SATSCARD](assets/notext/01.webp)


Chip Satscard jest wyposażony w 10 slotów, dzięki czemu może przechowywać bitcoiny do 10 razy na 10 różnych adresach. Każdy slot działa niezależnie i teoretycznie powinien być użyty tylko raz, aby zablokować w nim bitcoiny. Aby wydać bitcoiny, wystarczy odblokować slot za pomocą kompatybilnej aplikacji, takiej jak Nunchuk, wprowadzając 6-cyfrowy kod weryfikacyjny podany na odwrocie karty Satscard.


Karta zapewnia, że klucz prywatny zabezpieczający bitcoiny na Blockchain nie może zostać zatrzymany przez poprzedniego właściciela po fizycznym rozstaniu się z kartą. Odbiorca może również zweryfikować ważność slotu i przechowywaną w nim kwotę w momencie Exchange.


System ten jest szczególnie przydatny do kupowania fizycznych towarów za bitcoiny lub do dawania bitcoinów w prezencie.


## Jak kupić kartę Satscard?


Karta Satscard jest dostępna w sprzedaży [na oficjalnej stronie Coinkite](https://store.coinkite.com/store/category/satscard). Aby kupić ją w fizycznym sklepie, można również znaleźć [listę certyfikowanych sprzedawców](https://coinkite.com/resellers) na stronie internetowej.

Potrzebny będzie również telefon kompatybilny z komunikacją NFC lub urządzenie USB do odczytu kart NFC na standardowej częstotliwości 13,56 MHz.

## Jak załadować slot na karcie Satscard?


Po otrzymaniu karty Satscard pierwszym krokiem jest sprawdzenie opakowania, aby upewnić się, że nie zostało ono otwarte. Jeśli opakowanie jest uszkodzone, może to oznaczać, że karta została naruszona i może nie być autentyczna.


Do zarządzania kartą Satscard użyjemy aplikacji mobilnej **Nunchuk Wallet**. Upewnij się, że twój smartfon jest kompatybilny z NFC, a następnie pobierz Nunchuk z [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Store](https://apps.apple.com/us/app/nunchuk-Bitcoin-Wallet/id1563190073) lub bezpośrednio przez [plik `.apk`](https://github.com/nunchuk-io/nunchuk-android/releases).


![SATSCARD](assets/notext/02.webp)


Teoretycznie można bezpośrednio wysyłać bitcoiny na Address podany z tyłu karty Satscard bez korzystania z Nunchuka. Jednak odradzam to, ponieważ najpierw sprawdzimy, czy Address pierwszego slotu rzeczywiście pochodzi z klucza prywatnego przechowywanego na karcie Satscard i czy nie jest to fałszywy Address.


Jeśli używasz Nunchuka po raz pierwszy, aplikacja zaproponuje ci utworzenie konta. Na potrzeby tego samouczka nie jest to konieczne. Wybierz więc "*Kontynuuj jako gość*", aby kontynuować bez konta.


![SATSCARD](assets/notext/03.webp)


Następnie kliknij na "*Unassisted Wallet*".


![SATSCARD](assets/notext/04.webp)


Następnie kliknij przycisk "*Badam na własną rękę*".


![SATSCARD](assets/notext/05.webp)


Na ekranie głównym Nunchuka kliknij logo "*NFC*" w górnej części ekranu.


![SATSCARD](assets/notext/06.webp)


Przytrzymaj kartę Satscard z tyłu telefonu, aby ją zeskanować.


![SATSCARD](assets/notext/07.webp)


Nunchuk wyświetli Address odpowiadający pierwszemu slotowi na karcie Satscard. Zwykle ten Address powinien być identyczny z tym, który został ręcznie zapisany na odwrocie karty. Skopiuj ten Address i użyj go do przesłania bitcoinów, które chcesz zablokować w tym slocie.


![SATSCARD](assets/notext/08.webp)


## Jak sprawdzić bitcoiny na slocie?


Po potwierdzeniu transakcji można sprawdzić saldo powiązane z gniazdem karty Satscard, skanując je za pomocą Nunchuka. W ten sposób podczas transakcji odbiorca bitcoinów może natychmiast zweryfikować za pomocą aplikacji Nunchuk, czy karta rzeczywiście zawiera należne mu bitcoiny.


![SATSCARD](assets/notext/09.webp)

Jeśli kontrahent nie ma aplikacji Nunchuk, nadal może zweryfikować ważność karty Satscard. Wystarczy aktywować NFC na smartfonie i przyłożyć kartę Satscard do tylnej części urządzenia. Spowoduje to automatyczne otwarcie strony internetowej Satscard w przeglądarce, gdzie można sprawdzić ważność karty, a także powiązaną z nią kwotę w bitcoinach.

![SATSCARD](assets/notext/10.webp)


## Jak wypłacić bitcoiny z automatu?


Teraz, gdy pierwszy slot karty Satscard został załadowany określoną ilością bitcoinów, możesz przekazać kartę odbiorcy płatności.


![SATSCARD](assets/notext/11.webp)


Jeśli jesteś odbiorcą, musisz zainstalować Nunchuk. Po wejściu do aplikacji kliknij logo "*NFC*" u góry ekranu.


![SATSCARD](assets/notext/12.webp)


Umieść kartę Satscard z tyłu telefonu.


![SATSCARD](assets/notext/13.webp)


Nunchuk ujawni kwotę zabezpieczoną na Address.


![SATSCARD](assets/notext/14.webp)


Aby odblokować klucz prywatny i przenieść bitcoiny do posiadanego Address, kliknij przycisk "*Unseal and sweep balance*".


![SATSCARD](assets/notext/15.webp)


Opcja "*Wypłać do Wallet*" umożliwia bezpośrednie wysłanie bitcoinów do Wallet już obecnego w aplikacji Nunchuk. Aby przesłać środki do innego Address, wybierz opcję "*Withdraw to an Address*".


![SATSCARD](assets/notext/16.webp)


Wprowadź odbierający Address, na który chcesz wysłać bitcoiny zabezpieczone kartą Satscard. Upewnij się, że wprowadzony Address jest poprawny (jest to jedyny moment, w którym możesz go zweryfikować), a następnie kliknij przycisk "*Twórz transakcję*".


![SATSCARD](assets/notext/17.webp)


Wprowadź kod PIN karty Satscard. Ten 6-cyfrowy kod znajduje się na odwrocie fizycznej karty.


![SATSCARD](assets/notext/18.webp)


Trzymaj kartę Satscard z tyłu smartfona, podpisując transakcję kluczem prywatnym przechowywanym na karcie NFC.


![SATSCARD](assets/notext/19.webp)


Transakcja została podpisana i rozesłana w sieci Bitcoin, co oznacza, że slot na karcie Satscard jest teraz pusty.


![SATSCARD](assets/notext/20.webp)


## Jak ponownie użyć karty Satscard?


W przeciwieństwie do rozwiązań jednorazowego użytku, takich jak Opendime, karta Satscard jest wyposażona w chip zawierający 10 niezależnych gniazd, co pozwala na wykonanie do 10 operacji za pomocą jednej karty. Pierwszy slot, skonfigurowany fabrycznie przez Coinkite, odpowiada odbiorczemu Address zapisanemu na odwrocie karty Satscard.


![SATSCARD](assets/notext/21.webp)

Aby aktywować pozostałe 9 slotów, będziesz musiał użyć pary kluczy generate i Address za pośrednictwem aplikacji Nunchuk. Na stronie głównej aplikacji kliknij logo "*NFC*" u góry ekranu.

![SATSCARD](assets/notext/22.webp)


Umieść kartę Satscard z tyłu telefonu.


![SATSCARD](assets/notext/23.webp)


Nunchuk wskazuje, że żaden slot na karcie nie jest aktywny, co jest normalne, ponieważ pierwszy slot został już wykorzystany, a drugi nie został jeszcze wygenerowany. Aby zobaczyć poprzednio używane sloty, kliknij na "*Wyświetl niezamknięte sloty*". Zdecydowanie odradza się ponowne wykorzystywanie tych slotów, ponieważ doprowadziłoby to do ponownego użycia Address szkodliwego dla prywatności On-Chain. Dlatego utworzymy nowy slot, klikając przycisk "*Tak*".


![SATSCARD](assets/notext/24.webp)


Teraz należy wybrać sposób generate głównego kodu łańcucha.


Sloty na karcie Satscard są zgodne ze standardem BIP32, co oznacza, że wyprowadzanie kluczy kryptograficznych zabezpieczających bitcoiny nie opiera się na frazie Mnemonic, jak w portfelach BIP39, ale bezpośrednio na głównym kluczu prywatnym i głównym kodzie łańcucha. Te dwa Elements są używane jako dane wejściowe w funkcji HMAC-SHA512 do generate pary kluczy podrzędnych. Każdy slot ma własny klucz główny i własny kod łańcucha głównego. Dla każdego slotu istnieje tylko jeden poziom derywacji.


Para kluczy dla pierwszego gniazda jest wstępnie generowana przez Coinkite. Dlatego masz do niego bezpośredni dostęp za pomocą Nunchuka i dlatego odbierający Address jest zapisany z tyłu karty NFC. Jednak w przypadku pozostałych slotów to użytkownik jest odpowiedzialny za wygenerowanie kluczy.


Główny klucz prywatny dla każdego slotu jest generowany bezpośrednio przez kartę Satscard, a główne kody łańcuchowe muszą być dostarczone z zewnątrz. Jeśli chodzi o kod łańcucha dla nowego slotu, masz dwie opcje: pozwolić Nunchukowi generate automatycznie go utworzyć, wybierając "*Automatic*", lub utworzyć go samodzielnie, wybierając "*Advanced*" i wpisując go w przeznaczonym do tego miejscu. Aby kod łańcucha był skuteczny, musi być jak najbardziej losowy.


![SATSCARD](assets/notext/25.webp)


Wprowadź 6-cyfrowy kod PIN podany na odwrocie karty Satscard.


![SATSCARD](assets/notext/26.webp)


Umieść kartę Satscard z tyłu telefonu.


![SATSCARD](assets/notext/27.webp)


Nowy slot został pomyślnie skonfigurowany. Możesz teraz zobaczyć odbierający Address, do którego możesz wpłacić bitcoiny. Aby kontynuować ładowanie, postępuj zgodnie z instrukcjami w sekcji "*Jak załadować slot na Satscard?" tego samouczka.

Proces ten można powtórzyć do 10 razy na każdej karcie Satscard.


Gratulacje, jesteś teraz na bieżąco z korzystaniem z karty Satscard! Jeśli ten poradnik okazał się pomocny, będę wdzięczny za pozostawienie kciuka w górę poniżej. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dziękuję bardzo!