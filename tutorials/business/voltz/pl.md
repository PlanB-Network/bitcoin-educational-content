---
name: Voltz
description: Kompleksowe rozwiązanie Lightning wallet dla Twojej firmy.
---

![cover](assets/cover.webp)



Pomysł na platformę Voltz wyszedł od grupy bitcoinerów, którzy chcieli zapewnić własną usługę bitcoin wallet. W rezultacie powstała kompletna infrastruktura do akceptowania bitcoinów w handlu detalicznym. W tym samouczku zabierzemy Cię na wycieczkę po Voltz i możliwościach integracji bitcoinów, które platforma ma do zaoferowania.



## Rozpoczęcie pracy z Voltz



Voltz to nie tylko depozyt Lightning wallet, który umożliwia codzienne wysyłanie, odbieranie i płacenie, ale także kompletna platforma, która zapewnia liczne rozszerzenia do integracji bitcoinów jako punktu sprzedaży lub rynku w Twojej firmie.



Przejdź do platformy [Voltz] (https://www.voltz.com/en) i utwórz konto, klikając przycisk "Wypróbuj teraz".



![voltz](assets/fr/01.webp)



![login](assets/fr/02.webp)



⚠️ Ważne jest, aby ustawić silne hasło alfanumeryczne, aby zwiększyć swoje szanse na ataki typu brute-force i sprawdzić, czy rzeczywiście jesteś na oficjalnej stronie Voltz, aby wprowadzić dane logowania w celu ochrony przed phishingiem.



Interfejs Voltz jest bardzo podobny do interfejsu platformy LnBits.



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

Voltz jest w rzeczywistości zbudowany na serwerze LnBits; sprawdź nasz samouczek, aby dowiedzieć się, jak zamontować własne serwery LnBits i zbudować na nich swoje rozwiązania.



https://planb.academy/tutorials/business/others/lnbits-server-6a406046-3cef-4a64-a82b-8d8f0f82a192

Platforma umożliwia efektywne zarządzanie wieloma portfelami. Domyślnie, gdy się zarejestrujesz, automatycznie masz portfel Lightning. Możesz jednak dodać inne portfele.



![wallets](assets/fr/03.webp)



### Przenośność



Voltz nie ogranicza się do interfejsu internetowego: w sekcji **Mobile Access** można połączyć aktywny Voltz wallet z aplikacjami takimi jak Zeus lub Blue Wallet.



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

Aby to zrobić, należy zainstalować i aktywować rozszerzenie **LndHub** na platformie.



![lndhub](assets/fr/04.webp)



Wybierz swój aktywny portfel Voltz i, w zależności od praw, które chcesz przyznać, zeskanuj odpowiedni kod QR.




- Kod QR faktury umożliwia jedynie odczytanie historii portfela i generate nowych faktur.
- Kod QR administratora umożliwia przeglądanie historii, faktur generate, a także opłacanie faktur Lightning.



![qrs](assets/fr/05.webp)



W tym samouczku podłączamy nasz Voltz wallet do aplikacji Blue Wallet.



![connect](assets/fr/06.webp)



Po połączeniu naszego portfela wszystkie wykonywane działania będą synchronizowane między Blue Wallet i Voltz. Na przykład, gdy generate wystawia fakturę w Blue Wallet, ma również historię w Voltz.



![sync](assets/fr/07.webp)



W sekcji **Konfiguracja portfela** znajdziesz minimalne parametry, takie jak dostosowanie nazwy portfela i waluty, w której chcesz otrzymywać płatności.



![config](assets/fr/08.webp)



### Rozszerzenia



Jedną ze szczególnych cech platformy Voltz jest jej modułowość, umożliwiająca aktywację potrzebnych rozszerzeń. Listę rozszerzeń można znaleźć w menu **Extensions**.



![extensions](assets/fr/09.webp)



Wśród tych rozszerzeń znajduje się TPoS, terminal w punkcie sprzedaży, którego można używać do przechowywania zapasów i zbierania płatności od klientów.



![tpos](assets/fr/10.webp)



Z terminala w punkcie sprzedaży można :




- Uzyskaj stronę internetową, którą możesz udostępnić swoim klientom i partnerom;
- Zarządzanie zapasami produktów;
- Generowanie faktur Lightning;
- Płatności gotówkowe za pomocą kart Bolt.



Rozszerzenie jest dostępne w wersji darmowej i płatnej, oferującej bardziej zaawansowane funkcje. Aby utworzyć terminal POS, kliknij przycisk **Open** poniżej logo rozszerzenia, a następnie kliknij **New POS**.



![new_tpos](assets/fr/11.webp)



Zdefiniuj nazwę swojego punktu sprzedaży, a następnie podłącz Voltz wallet do terminala, aby zbierać płatności. Możesz aktywować napiwki, zaznaczając pole **Activate gratuities**. Aktywuj również opcję drukowania faktur, jeśli chcesz wystawiać paragony swoim klientom (ta funkcja jest wciąż w fazie rozwoju, więc mogą wystąpić usterki).



Terminal w punkcie sprzedaży zawiera również konfigurację podatkową, jeśli chcesz zastosować podatek obowiązujący w Twoim kraju bezpośrednio do swoich produktów.



![tpos](assets/fr/12.webp)



Po utworzeniu terminala POS można dodać wstępnie skonfigurowane produkty i usługi, aby zapewnić płynną obsługę płatności i księgowości dla siebie i swoich klientów.



![product](assets/fr/13.webp)



Utwórz swoje produkty, definiując ich nazwę, dodając obraz i ustalając cenę sprzedaży.  Możesz kategoryzować swoje produkty, aby ułatwić ich śledzenie. Możesz zastosować podatki bezpośrednio do konkretnego produktu. Jeśli produkt nie ma zastosowanego podatku, podatek skonfigurowany na etapie tworzenia terminala w punkcie sprzedaży zostanie zastosowany automatycznie.



![products](assets/fr/14.webp)



Możesz automatycznie zaimportować listę produktów z formatu JSON, klikając przycisk **Import/Export**.



![exports](assets/fr/15.webp)



Uzyskaj dostęp do obszaru kasy za pośrednictwem łącza, klikając ikonę **Nowa karta** lub udostępnij klientom swoją platformę POS za pomocą kodu QR, klikając ikonę **Kod QR**.



![lien](assets/fr/16.webp)



![qr](assets/fr/17.webp)



Klienci mogą zapoznać się z katalogiem i dokonać płatności z poziomu tego interfejsu.



![pos](assets/fr/18.webp)



![chose](assets/fr/19.webp)



![pay](assets/fr/20.webp)



![checkout](assets/fr/21.webp)



W grupie dostępnych rozszerzeń znajdują się również narzędzia takie jak **Invoice** i **Payment Link**, które umożliwiają wystawianie faktur generate z określonymi produktami w celu pobierania pojedynczych płatności bez przechodzenia przez terminal POS.



## Śledź swoje płatności



W menu **Payments** Voltz zapewnia przegląd płatności do różnych portfeli.


Możesz śledzić swoje płatności przez :




- Status.
- Etykieta: na przykład **TPOS** dla płatności w punktach sprzedaży i **lnhub** poprzez połączenie mobilne w portfelach Zeus i Blue Wallet.
- Portfolio kolekcji.
- Suma płatności przychodzących i wychodzących.
- Dobrze zdefiniowany okres.



![payments](assets/fr/22.webp)



## Więcej opcji



Voltz jest również infrastrukturą, na której można budować własne rozwiązania. W sekcji **Extensions** znajdziesz przewodnik po tworzeniu własnych rozszerzeń w ramach ekosystemu Voltz i LnBits.



![build](assets/fr/23.webp)



W przypadku, gdy chcesz opracować rozwiązania poza ekosystemem, ale nadal korzystać z ich infrastruktury, w sekcji **URL węzła** znajdziesz klucze API i informacje o dokumentacji wraz z przykładem tego, co możesz zrobić z tymi danymi.



Możesz tworzyć faktury Lightning ze swoich aplikacji za pomocą Voltz wallet, opłacać faktury Lightning, dekodować i weryfikować faktury.



![keys](assets/fr/24.webp)



Masz już dobre pojęcie o Voltz. Jeśli spodobał Ci się ten samouczek, jesteśmy pewni, że dowiesz się więcej o najlepszych metodach i narzędziach do integracji bitcoina z Twoją firmą dzięki naszemu kursowi: Bitcoin dla firm.



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a