---
name: Alby

description: Rozszerzenie przeglądarki dla Bitcoin i Lightning Network
---

![cover](assets/cover.webp)




Coraz łatwiejsze dokonywanie płatności za pomocą bitcoinów jest wyzwaniem, przed którym stoi wiele firm z tego sektora. Alby wyróżnia się z tłumu dzięki rozszerzeniu Alby wallet dla przeglądarek. Rozszerzenie to ma na celu skonfigurowanie płynnej struktury, która automatycznie wykrywa adresy i umożliwia dokonywanie płatności bitcoinowych bez tarcia. W tym samouczku odkrywamy rozszerzenie Alby i testujemy, w jaki sposób ułatwia ono płatności z poziomu przeglądarki.




![video](https://youtu.be/nd5fX2vHuDw)




## Rozszerzenie Alby



Rozszerzenie Alby to narzędzie, które umożliwia przeglądarce internetowej łatwą i bezpieczną interakcję z siecią Bitcoin i jej warstwą Lightning Network. Charakteryzuje się ono trzema aspektami:




- Lightning Network wallet: Połącz swój węzeł lub konto Alby, aby szybko i tanio wysyłać i odbierać bitcoiny za pośrednictwem warstwy Lightning Network.
- Płynne płatności przez Internet: Eliminuje potrzebę skanowania kodów QR lub przełączania się między aplikacjami do płatności bitcoinami na stronach internetowych obsługujących Lightning. Umożliwia płynne transakcje za pomocą jednego kliknięcia lub bez potwierdzenia, jeśli ustawiłeś budżet.
- Menedżer Nostr: Rozszerzenie zarządza kluczami Nostr, ułatwiając łączenie się i interakcję z aplikacjami Nostr działającymi jako bezpieczni sygnatariusze bez ujawniania klucza prywatnego każdej platformie.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Połączenie z rozszerzeniem



W tym samouczku będziemy używać rozszerzenia Alby w przeglądarce Firefox w systemie operacyjnym Ubuntu. Jest ono jednak również dostępne w systemie Windows i przeglądarkach takich jak Chrome.



Rozszerzenie Alby można dodać do przeglądarki, odwiedzając sklep z rozszerzeniami [Firefox](https://addons.mozilla.org/fr/firefox/addon/alby/) lub sklep z rozszerzeniami [Chrome](https://chromewebstore.google.com/detail/alby-bitcoin-wallet-for-l/iokeahhehimjnekafflcihljlcjccdbe).



![firefox](assets/fr/01.webp)



![chrome](assets/fr/02.webp)



ℹ️ Ważne jest, aby sprawdzić, czy autor rozszerzenia jest rzeczywiście oficjalnym kontem Alby, aby uniknąć jakiejkolwiek formy piractwa lub kradzieży bitcoinów.



Dodaj rozszerzenie do przeglądarki, klikając przycisk po prawej stronie.


Przyznaj niezbędne uprawnienia do instalacji i korzystania z rozszerzenia, a następnie przypnij rozszerzenie do paska narzędzi, aby łatwo je pobrać.



![pin](assets/fr/03.webp)



Należy również zdefiniować kod odblokowujący (bardzo ważny), który zagwarantuje bezpieczny dostęp do urządzenia Lightning wallet z poziomu przeglądarki. Sugerujemy ustawienie silnego hasła alfanumerycznego.



ℹ️ Zapisz to hasło w bezpiecznym miejscu, aby mieć do niego dostęp w razie zapomnienia, ponieważ można je zmienić, ale nie można go odzyskać.



https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

![pass](assets/fr/04.webp)



Alby demonstruje swoje możliwości adaptacyjne, oferując dwie opcje:




- Kontynuuj korzystanie z konta Alby, jeśli chcesz cieszyć się aplikacjami, zachowując kontrolę nad swoimi bitcoinami.
- Podłącz własny węzeł wallet lub Lightning, jeśli jest już obsługiwany przez rozszerzenie.



https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


W tym samouczku zdecydujemy się kontynuować korzystanie z konta Alby, aby skorzystać z funkcji ekosystemu Alby.



https://planb.academy/tutorials/wallet/mobile/alby-go-40202802-b346-4a3c-9863-465c3bde9903

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Zaloguj się na swoje konto Alby lub utwórz je, jeśli jeszcze go nie posiadasz.



![signup](assets/fr/05.webp)



## Dokonywanie pierwszych płatności



Po zalogowaniu możesz kliknąć rozszerzenie Alby na pasku narzędzi, aby uzyskać dostęp do swojego portfolio.



![buzzin](assets/fr/06.webp)



Po utworzeniu konta Alby należy połączyć je z wallet, aby móc wydawać satoshis. Aby połączyć wallet bitcoin z kontem Alby, sugerujemy użycie węzła Alby Hub, który można skonfigurować na komputerze lub zasubskrybować plan oferowany przez Alby.



![hubplan](assets/fr/13.webp)




W tym samouczku nasze konto Alby jest obsługiwane przez lokalną instalację na naszym komputerze.


Aby zbudować własny węzeł Alby, zalecamy nasz samouczek Alby Hub.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Węzeł ten umożliwia tworzenie własnych portfeli Lightning i efektywne zarządzanie kanałami Lightning w celu wysyłania i odbierania satoshi.



![channels](assets/fr/14.webp)



Otwarte kanały odbioru, które definiują całkowitą liczbę satelitów, które można odbierać.



![receivechanal](assets/fr/15.webp)



Otwórz kanały wysyłania, blokując satoshis na adresie bitcoin onchain. Zablokowane satoshi definiują całkowitą ilość satoshi, jaką możesz wydać.



![spend](assets/fr/16.webp)



Możesz teraz wysyłać i odbierać satoshis za pośrednictwem rozszerzenia Alby.



![exchange](assets/fr/08.webp)



Od tego momentu rozszerzenie Alby jest w stanie wykrywać adresy Lightning i faktury dostępne na odwiedzanych stronach internetowych i sugerować ich opłacenie w bitcoinach lub Lightning bezpośrednio z poziomu rozszerzenia.



![suggest](assets/fr/09.webp)



![pay](assets/fr/10.webp)




## Zabezpieczanie kluczy odzyskiwania za pomocą klucza głównego



Klucz główny oferowany przez rozszerzenie Alby działa jako nakładka ochronna, która umożliwia bezpieczną komunikację z główną warstwą sieciową Bitcoin (Onchain), systemem Nostr i umożliwia aktywację połączenia Lightning z aplikacjami Nostr.



![masterKey](assets/fr/11.webp)



Ten klucz główny ma postać 12 słów podobnych do frazy odzyskiwania. Dlatego zalecamy przechowywanie go przy użyciu bezpiecznych metod, aby zapewnić dostęp do niego w dowolnym momencie.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


![masterKey](assets/fr/12.webp)



Dzięki rozszerzeniu Alby możesz teraz doświadczyć płynnych płatności Bitcoin i Lightning. Jeśli spodobał Ci się ten samouczek, polecamy nasz samouczek Alby Hub, aby skonfigurować własny węzeł Alby i kontrolować wszystkie aspekty portfeli Alby za pomocą płynnego i wydajnego interfejsu.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a