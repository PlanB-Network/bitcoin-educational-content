---
name: Macadamia Wallet
description: Cashu mobile wallet do anonimowych i natychmiastowych płatności BTC
---

![cover](assets/cover.webp)



Macadamia Wallet to mobilny wallet na iOS, który implementuje protokół Cashu, system Chaumian ecash umożliwiający całkowicie anonimowe płatności Bitcoin. Dzięki ślepym podpisom żaden obserwator nie może powiązać wpłat z wydatkami, oferując poufność podobną do fizycznej gotówki.



W tym samouczku przyjrzymy się, jak zainstalować i skonfigurować Macadamia, wykonać pierwsze transakcje Cashu (Mint, Send, Receive, Melt) i zarządzać wieloma mintami, aby zabezpieczyć swoje środki.



## Co to jest Macadamia Wallet?



### Protokół Cashu



Cashu wykorzystuje ślepe podpisy wymyślone przez Davida Chauma: użytkownik deponuje bitcoiny na serwerze "mennicy", który wydaje równoważne tokeny w satoshis. Mennica podpisuje te tokeny, nie widząc ich zawartości, co uniemożliwia powiązanie token z użytkownikiem. Wymiana to off-chain, peer-to-peer i jest całkowicie nieprzejrzysta - nawet mennica nie może śledzić, kto komu płaci.



Macadamia to wallet iOS o otwartym kodzie źródłowym opracowany w Swift/SwiftUI. Działa bez konta lub KYC, tokeny są przechowywane lokalnie i chronione frazą seed. Kod można poddać audytowi na GitHub, a tokeny są interoperacyjne z innymi portfelami Cashu (Minibits, Cashu.me).



### Model powierniczy i kompromis



**Ważne**: Cashu działa w oparciu o model powierniczy. Tokeny są obietnicami zapłaty (IOU) popartymi rezerwami Bitcoin mennicy. Jeśli mennica zniknie, tokeny stracą swoją wartość. Jest to kompromis zapewniający maksymalną poufność.



Używaj Macadamia jako fizycznego wallet: tylko niewielkie ilości. Rozłóż swoje środki na kilka mennic, aby rozcieńczyć ryzyko.



## Główne cechy



Macadamia implementuje cztery podstawowe operacje protokołu Cashu. **Mint** konwertuje satoshis na tokeny za pośrednictwem faktury Lightning. **Send** pozwala wysyłać tokeny bezpłatnie za pośrednictwem kodu QR lub linku, całkowicie off-chain. **Receive** pozwala odbierać tokeny lub generate fakturę Lightning. **Melt** opłaca fakturę Lightning poprzez zniszczenie tokenów.



wallet obsługuje zarządzanie wieloma mennicami jednocześnie. Możesz wymieniać tokeny między różnymi mennicami za pośrednictwem Lightning.



## Obsługiwane platformy



Macadamia jest dostępna tylko na iOS 17 lub nowszym dla iPhone'a i iPada. Natywna aplikacja Swift/SwiftUI oferuje optymalną integrację z ekosystemem Apple.



Protokół Cashu gwarantuje interoperacyjność między portfelami. Możesz przywrócić swoją frazę seed w innych aplikacjach, takich jak Minibits na Androida lub Nutstash na komputery stacjonarne.



Aktualna wersja jest dystrybuowana za pośrednictwem TestFlight. Z tej wersji beta należy korzystać w niewielkich ilościach.



## Instalacja



Macadamia jest obecnie dostępna za pośrednictwem TestFlight, programu testów beta firmy Apple. Oto jak ją zainstalować:



### Instalacja za pośrednictwem TestFlight



**Krok 1: Pobierz TestFlight**



Jeśli nie masz jeszcze aplikacji TestFlight na swoim urządzeniu, wyszukaj "TestFlight" w App Store i zainstaluj ją. TestFlight to oficjalna aplikacja Apple do testowania wersji beta aplikacji iOS.



**Krok 2: Dołącz do programu Macadamia beta** (w języku francuskim)



Po zainstalowaniu aplikacji TestFlight, skorzystaj z poniższego linku do zaproszenia z iPhone'a lub iPada: [https://testflight.apple.com/join/RMU6PaRu](https://testflight.apple.com/join/RMU6PaRu)



Link automatycznie otworzy TestFlight i zaproponuje instalację Macadamia Wallet. Kliknij "Accept", a następnie "Install", aby rozpocząć pobieranie. Aplikacja waży około dziesięciu megabajtów, a jej instalacja zajmuje zaledwie kilka sekund.



![Installation TestFlight](assets/fr/01.webp)



### Ważne informacje o wersjach beta



Macadamia jest wciąż w fazie aktywnego rozwoju. Wersje TestFlight są często aktualizowane i mogą wprowadzać nowe funkcje lub poprawiać błędy. Jednakże, jak w przypadku każdej wersji beta, mogą wystąpić usterki. **Zdecydowanie zalecamy używanie tylko niewielkich ilości**, które mogą zostać utracone w przypadku problemów technicznych.



Macadamia nie gromadzi żadnych danych użytkownika zgodnie z wyświetlaną polityką prywatności. Podczas instalacji należy sprawdzić, czy deweloperem jest cypherbase UG.



## Konfiguracja początkowa



Przy pierwszym uruchomieniu Macadamia generuje zdanie BIP-39 składające się z 12 słów. Zapisz je w bezpiecznym miejscu - nigdy jako zrzut ekranu. Te słowa pozwolą ci odtworzyć wallet i wydać żetony.



![Configuration initiale](assets/fr/02.webp)



Wykonaj cztery kroki: powitanie, zaakceptuj warunki, zapisz zdanie seed i ostateczne potwierdzenie.



![Interface principale](assets/fr/03.webp)



Po zakończeniu konfiguracji Macadamia wyświetla trzy główne zakładki. **Wallet** wyświetla saldo i historię transakcji. **Mints** pozwala zarządzać serwerami Cashu. **Ustawienia** dają dostęp do ustawień i frazy seed.



![Ajout d'un mint](assets/fr/04.webp)



Teraz należy skonfigurować mennicę, tj. serwer Cashu, który będzie wydawał tokeny. Przejdź do zakładki "Mennice", dotknij "Dodaj nowy adres URL mennicy" i wprowadź adres wybranej mennicy (np. mint.cubabitcoin.org). Sprawdź bitcoinmints.com lub cashu.space, aby znaleźć renomowane mennice publiczne. Weryfikuj tylko mennice, których reputację sprawdziłeś, ponieważ będą one sprawować pieczę nad Twoimi satoshis.



## Codzienne użytkowanie



### Tworzenie nowych tokenów (Mint)



Aby zasilić wallet Macadamia ecash, musisz wykonać operację "Mint" (aby utworzyć tokeny). Dotknij "Odbierz", a następnie wybierz opcję "Błyskawica". Wprowadź żądaną kwotę (np. 1000 sats), wybierz mennicę, która ma zostać użyta, a następnie generate fakturę Lightning.



![Opération Mint](assets/fr/05.webp)



Opłać wygenerowaną fakturę Lightning za pomocą zwykłego wallet (Phoenix, Zeus, BlueWallet).



![Confirmation Mint](assets/fr/06.webp)



Tokeny Cashu pojawiają się na saldzie natychmiast po dokonaniu płatności.



### Wysyłanie tokenów



Aby wysłać tokeny Cashu do innego użytkownika, dotknij przycisku "Wyślij" na ekranie głównym, a następnie wybierz "Ecash". Wprowadź kwotę do wysłania (np. 50 sats) i w razie potrzeby dodaj notatkę opisową.



![Envoi Ecash](assets/fr/07.webp)



Udostępnij kod QR lub wygenerowany tekst za pośrednictwem iMessage, Signal lub Telegram. Odbiorca otrzyma środki natychmiast i bezpłatnie.



### Odbieranie tokenów



Aby otrzymać tokeny Cashu wysłane przez innego użytkownika, dotknij "Odbierz", a następnie wybierz "Ecash". Zeskanuj kod QR token lub wklej otrzymany link token.



![Réception Ecash](assets/fr/08.webp)



Dotknij "Redeem", aby odebrać token.



### Płatności Lightning (Melt)



Aby zapłacić fakturę Lightning za pomocą tokenów Cashu, dotknij "Wyślij", a następnie wybierz "Lightning". Wklej fakturę BOLT11, którą chcesz zapłacić.



![Paiement Lightning](assets/fr/11.webp)



Mennica niszczy tokeny i realizuje płatność Lightning. Możesz więc zapłacić za dowolną usługę Lightning, zachowując anonimowość.



### Zamiana między miętówkami



Po otrzymaniu tokenów od mennicy, której nie skonfigurowałeś, Macadamia oferuje kilka opcji zarządzania tymi tokenami.



![Swap inter-mints](assets/fr/09.webp)



Dodaj nową mennicę lub wymień tokeny na istniejącą mennicę. Wymiana wykorzystuje Lightning jako pomost do anonimowego przesyłania środków.



### Zaawansowane zarządzanie wieloma mennicami



Macadamia oferuje zaawansowane narzędzia do zarządzania wieloma mennicami jednocześnie i strategicznej alokacji środków.



![Gestion multi-mints](assets/fr/10.webp)



"Distribute Funds" automatycznie rozdziela saldo zgodnie z wartościami procentowymi (np. 50/50). "Transfer" umożliwia ręczne transfery między mennicami w celu dywersyfikacji ryzyka.



## Zalety i ograniczenia



**Highlights** :





- Maksymalna poufność**: Transakcje niemożliwe do śledzenia, nawet przez mennicę. Brak metadanych blockchain, bezśladowa wymiana peer-to-peer.
- Szybko i za darmo**: Bezpłatne przelewy natychmiastowe w ciągu minuty, idealne do mikropłatności.
- Interoperacyjność**: ustandaryzowane tokeny Cashu do użytku z innymi kompatybilnymi portfelami (Minibits, Nutstash).
- Prostota**: Interface iOS native jest dostępny dla początkujących, pozostając jednocześnie audytowalnym (open source).



**Ograniczenia** :





- Model powierniczy**: wymagane zaufanie mennicy. Jeśli mennica zniknie, tokeny stracą swoją wartość.
- tylko iOS**: Brak wersji Android/desktop. Interoperacyjność Cashu umożliwia dostęp za pośrednictwem innych portfeli, ale optymalnym rozwiązaniem pozostaje iOS.
- Zależność od Mint**: Mint offline = niezdolny do przeprowadzenia transakcji wymagających jego interwencji (Mint, Melt).
- Nowa technologia** : Aktywny rozwój, możliwe błędy, zmieniające się standardy.



## Najlepsze praktyki





- Dywersyfikacja mennic**: Rozłóż swoje żetony na kilka renomowanych mennic, aby zmniejszyć ryzyko.
- Kwoty graniczne**: Używaj Macadamia jako fizycznego wallet do codziennych płatności, a nie jako sejfu.
- Zabezpiecz swój seed**: Przechowuj 12-wyrazową frazę na papierze w bezpiecznym miejscu. Od czasu do czasu testuj przywracanie.
- Sprawdź miętówki**: Sprawdź cashu.space i fora społeczności przed dodaniem mennicy. Wybierz te z dobrym czasem działania i solidną reputacją.
- VPN lub Tor**: Ukryj swoje IP za pomocą VPN/Tor, aby zmaksymalizować prywatność w sieci.
- Dołącz do społeczności**: Grupy Telegram/Discord Cashu w celu uzyskania aktualizacji, zaleceń dotyczących miętówek i najlepszych praktyk.



## Wnioski



Macadamia Wallet wnosi właściwości fizycznej gotówki do cyfrowego Bitcoin. Łącząc ślepe podpisy Chaum i Lightning, oferuje eleganckie rozwiązanie zapewniające poufność transakcji. Jego natywny interfejs iOS sprawia, że zaawansowana technologia kryptograficzna jest dostępna, pozostając jednocześnie open source i interoperacyjna z ekosystemem Cashu.



Model powierniczy wymaga czujności i dobrych praktyk bezpieczeństwa. Prawidłowo używany, Macadamia staje się nieocenionym narzędziem do codziennych płatności wymagających anonimowości, uzupełniając portfele niebędące portfelami powierniczymi w celu oszczędzania.



## Zasoby



### Oficjalna dokumentacja




- Oficjalna strona internetowa: [macadamia.cash](https://macadamia.cash)
- Macadamia FAQ: [macadamia.cash/faq](https://macadamia.cash/faq)
- Kod źródłowy GitHub: [github.com/zeugmaster/macadamia](https://github.com/zeugmaster/macadamia)



### Dokumentacja Cashu




- Dokumentacja techniczna: [docs.cashu.space](https://docs.cashu.space)
- Lista publicznych mennic: [bitcoinmints.com](https://bitcoinmints.com)
- Oficjalna strona protokołu: [cashu.space](https://cashu.space)



### Wspólnota




- Grupa Telegram Cashu: [t.me/cashu_ecash](https://t.me/cashu_ecash)