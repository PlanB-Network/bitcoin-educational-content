---
name: BIP47 - PayNym
description: Użyj kodu płatności wielokrotnego użytku na Ashigaru
---
![cover](assets/cover.webp)



Najgorszym błędem w zakresie prywatności, jaki można popełnić w Bitcoin, jest ponowne wykorzystywanie adresów. Za każdym razem, gdy ten sam adres otrzymuje kilka płatności, transakcje te są ze sobą łączone, zapewniając światu mapę Twoich transakcji. W związku z tym zdecydowanie zaleca się, aby zawsze używać unikalnego adresu generate dla każdego rachunku. Jednak w przypadku niektórych aplikacji Bitcoin nie jest to prosta sprawa.



BIP47, zaproponowany przez Justusa Ranviera w 2015 roku, stanowi elegancką odpowiedź na ten problem. Wprowadza on koncepcję **kodu płatności wielokrotnego użytku**: unikalnego identyfikatora umożliwiającego otrzymywanie praktycznie nieograniczonej liczby płatności bitcoinowych onchain, bez konieczności ponownego użycia adresu. Dzięki mechanizmowi kryptograficznemu opartemu na wymianie ECDH (*Diffie-Hellman na krzywych eliptycznych*), każda płatność na ten sam kod skutkuje pustym adresem, specyficznym dla relacji między nadawcą a odbiorcą.



![Image](assets/fr/01.webp)



Zasada BIP47 jest realizowana w szczególności przez **PayNym**, system pierwotnie opracowany przez Samourai Wallet, a obecnie przejęty przez Ashigaru. W tym samouczku przyjrzymy się, jak aktywować PayNym, wymieniać kody płatności z korespondentem i przeprowadzać transakcje bez ponownego używania adresu.



Nie będę tutaj zagłębiał się w szczegółową obsługę BIP47. Jeśli chcesz zagłębić się w ten temat, zapoznaj się z rozdziałem 6.6 mojego szkolenia BTC 204.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Wymagania wstępne



Aby skorzystać z tego samouczka, potrzebujesz jedynie wallet w aplikacji Ashigaru. Jeśli nie wiesz, jak pobrać, zweryfikować, zainstalować aplikację lub utworzyć wallet, polecam najpierw zapoznać się z tym samouczkiem:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

## Żądanie PayNym



Pierwszym krokiem jest zgłoszenie PayNym. Ta operacja musi być wykonana tylko raz na wallet. Wiąże ona kod płatności BIP47 pochodzący z seed (`PM...`) z unikalnym identyfikatorem specyficznym dla implementacji PayNym. Ten krótszy, bardziej czytelny identyfikator można następnie przesłać do korespondentów w celu ułatwienia wymiany, bez konieczności udostępniania długiego, pełnego kodu BIP47.



Aby to zrobić, kliknij obraz PayNym w lewym górnym rogu interfejsu, a następnie kod płatności `PM...`.



![Image](assets/fr/02.webp)



Następnie kliknij trzy małe kropki w prawym górnym rogu i wybierz `Claim PayNym`.



![Image](assets/fr/03.webp)



Potwierdź, klikając przycisk `CLAIM YOUR PAYNYM`.



![Image](assets/fr/04.webp)



Odśwież stronę: Twój identyfikator PayNym ID jest teraz wyświetlany pod Twoim zdjęciem, tuż nad kodem płatności BIP47.



![Image](assets/fr/05.webp)



Twój PayNym jest teraz aktywny i gotowy do użycia w pierwszych transakcjach BIP47.



## Połącz z kontaktem



Istnieją dwa rodzaje połączeń między PayNym: **follow** i **connect**. Operacja `follow` jest całkowicie darmowa. Ustanawia ona połączenie między dwoma PayNym poprzez Soroban, oparty na Torze szyfrowany protokół komunikacyjny opracowany przez zespół Samourai i przyjęty przez Ashigaru. Łącze to umożliwia dwóm użytkownikom podążającym za sobą prywatną wymianę informacji, w szczególności w celu koordynowania wspólnych transakcji, takich jak Stowaway lub StonewallX2, którym przyjrzymy się w innym samouczku. Ten krok jest specyficzny dla PayNym i nie jest częścią protokołu BIP47.



![Image](assets/fr/06.webp)



Z drugiej strony, operacja połączenia (`connect`) wymaga transakcji on-chain. Polega ona na wykonaniu transakcji powiadomienia zdefiniowanej w BIP47. Ta transakcja Bitcoin zawiera metadane w wyjściu `OP_RETURN`, które ustanawia zaszyfrowany kanał komunikacyjny między płatnikiem a odbiorcą. Z tego kanału płatnik będzie w stanie generate unikalne adresy odbiorcze dla każdej płatności, a odbiorca zostanie powiadomiony o tych płatnościach i będzie mógł generate klucze prywatne związane z adresami, aby wydać te środki później.



Ta transakcja powiadomienia wiąże się z kosztami: opłatą mining i 546 sats wysłanymi na adres powiadomienia odbiorcy w celu zasygnalizowania połączenia. Po nawiązaniu połączenia można dokonać niemal nieskończonej liczby płatności za pośrednictwem BIP47.



W skrócie:




- follow": darmowe, nawiązuje szyfrowaną komunikację przez Soroban, przydatne dla narzędzi współpracy Ashigaru;
- `Connect`: płatne, wykonuje transakcję powiadomienia BIP47 w celu aktywacji kanału między płatnikiem a odbiorcą.



Aby wejść w interakcję z PayNym, musisz go najpierw *obserwować*. Jest to pierwszy krok przed nawiązaniem połączenia BIP47. Załóżmy, że chcesz wysyłać płatności cykliczne do PayNym `+instinctiveoffer10`.



Przejdź do swojej strony PayNym na Ashigaru, a następnie kliknij przycisk `+` w prawym dolnym rogu interfejsu.



![Image](assets/fr/07.webp)



Następnie możesz wkleić pełny kod płatności odbiorcy lub zeskanować jego kod QR.



![Image](assets/fr/08.webp)



Jeśli masz tylko jego identyfikator PayNym, przejdź do [Paynym.rs](https://paynym.rs/), aby znaleźć kod QR powiązany z jego kodem płatności.



![Image](assets/fr/09.webp)



Po zeskanowaniu kodu QR kliknij przycisk `FOLLOW`, aby śledzić PayNym.



![Image](assets/fr/10.webp)



Akcja `FOLLOW` jest wystarczająca dla transakcji opartych na współpracy (*cahoots*). Aby jednak wysłać płatności BIP47, należy ustanowić połączenie: kliknij `CONNECT`, aby wykonać transakcję powiadomienia.



![Image](assets/fr/11.webp)



Transakcja z powiadomieniem jest następnie transmitowana w sieci. Przed dokonaniem pierwszej płatności należy poczekać na co najmniej jedno potwierdzenie.



![Image](assets/fr/12.webp)



## Dokonanie płatności na BIP47



Jesteś teraz połączony z odbiorcą i możesz wysłać płatność na unikalny adres, automatycznie wygenerowany przy użyciu protokołu BIP47, bez konieczności wcześniejszej wymiany danych z odbiorcą.



Na stronie głównej PayNym kliknij kontakt, do którego chcesz wysłać płatność.



![Image](assets/fr/13.webp)



W prawym górnym rogu interfejsu kliknij ikonę strzałki.



![Image](assets/fr/14.webp)



Wprowadź kwotę do wysłania. Nie musisz wprowadzać adresu odbiorcy: zostanie on automatycznie uzyskany przy użyciu protokołu BIP47.



![Image](assets/fr/15.webp)



Dokładnie sprawdź szczegóły transakcji, w tym opłaty, a następnie przeciągnij zieloną strzałkę u dołu ekranu, aby podpisać i wysłać transakcję.



![Image](assets/fr/16.webp)



Transakcja została wysłana.



![Image](assets/fr/17.webp)



W tym przykładzie płatność została dokonana na inny z moich portfeli PayNym. Widzę zatem, że dotarła ona do mojego innego Ashigaru wallet, bez ręcznej wymiany adresu: użyto tylko identyfikatora PayNym.



![Image](assets/fr/18.webp)



Wiesz już, jak korzystać z kodów płatności wielokrotnego użytku BIP47 dzięki implementacji PayNym w aplikacji Ashigaru. Możesz teraz udostępnić ten kod płatności każdemu, kto chce wysłać ci płatności (zwłaszcza płatności cykliczne). Możesz również opublikować swój identyfikator PayNym na swojej stronie internetowej lub w sieciach społecznościowych, aby otrzymywać darowizny.



Aby pogłębić swoją wiedzę na temat tego protokołu, zrozumieć szczegółowo jego działanie i jego implikacje dla poufności, zdecydowanie zalecam wzięcie udziału w moim kursie BTC 204:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c