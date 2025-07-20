---
name: Breez
description: Portfel Lightning, który daje Ci pełną kontrolę.
---

![breez-cover](assets/cover.webp)

Portfele samodzielnej opieki stają się najbezpieczniejszą opcją przechowywania bitcoinów, oferując jednocześnie moc i korzyści warstwy Lightning w sieci Bitcoin. Breez wyróżnia się wśród tych portfeli dzięki swojemu podejściu.

## Czym jest portfel Breez?

Breez to portfel samodzielnej opieki (self-custodial) stworzony przez firmę Breez, który daje Ci kontrolę nad Twoimi bitcoinami i oferuje innowacyjne funkcje w jednej aplikacji. Możesz pobrać portfel Breez na Androida i iOS z oficjalnych platform. W tym przewodniku skupimy się na wersji dla Androida. Cały opisany proces dotyczy również wersji na iOS.

⚠️ **WAŻNE**: Pobieraj aplikację wyłącznie z oficjalnych platform, takich jak Google Play Store lub Apple Store, aby zapewnić autentyczność aplikacji i bezpieczeństwo swoich środków.

Oto aplikacja **Breez** na Androidzie (nie mylić z Misty Breez, innym produktem firmy Breez).
![breez-wallet-ps](assets/fr/01.webp)

## Rozpoczęcie pracy z portfelem

Breez umożliwia utworzenie nowego portfela lub przywrócenie istniejącego portfela Lightning. W tym przewodniku utworzymy nowy portfel.

![creer-portefeuille](assets/fr/02.webp)

Jedną z zalet Breez jest to, że posiadasz klucze umożliwiające pełny dostęp do Twoich bitcoinów. Jesteś właścicielem swoich środków.

⚠️ Portfel Breez jest obecnie w fazie rozwoju; zalecamy przeprowadzanie transakcji na umiarkowane kwoty.
![test-breez](assets/fr/03.webp)

> Nie Twoje klucze, nie Twoje bitcoiny.

Portfel synchronizuje się bezpośrednio z protokołem Bitcoin i zapewnia aktywny węzeł do przeprowadzania transakcji.
![bitcoin-connexion](assets/fr/04.webp)

### Zabezpieczanie kluczy

Pierwszym krokiem po utworzeniu portfela Bitcoin/Lightning jest zabezpieczenie kluczy. W menu wybierz **Preferencje**, a następnie **Bezpieczeństwo**. Breez umożliwia zapisanie 12 słów odzyskiwania na Google Drive lub zdalnym serwerze, który możesz skonfigurować. Następnie włącz opcję **Szyfruj kopię zapasową**: ta opcja pokaże Ci słowa kluczowe portfela, które możesz zapisać ręcznie.

![sécurité](assets/fr/06.webp)

Postępuj zgodnie z instrukcjami, aby potwierdzić kopię zapasową i połącz konto zdalnej kopii zapasowej z portfelem Breez.

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

⚠️ **WAŻNE**: Aby zwiększyć bezpieczeństwo portfela Breez, możesz ustawić kod PIN i skonfigurować go do autoryzacji dostępu do portfela.

### Wykonywanie pierwszych transakcji z Breez

Breez kładzie nacisk na intuicyjność aplikacji. Aby otrzymać pierwsze bitcoiny za pomocą tego portfela, wystarczy kliknąć **Odbierz** na stronie głównej, a następnie wybrać metodę odbioru bitcoinów. Breez oferuje trzy opcje:

- **Odbierz za pomocą faktury Lightning lub ID**: Wygeneruj fakturę i otrzymaj płatność.
- **Odbierz przez adres Bitcoin**: Odbierz bitcoiny za pomocą transakcji w sieci głównej Bitcoin.
- **Kup Bitcoin**: Breez umożliwia zakup bitcoinów bezpośrednio za waluty fiducjarne.

![receive-bitcoin](assets/fr/07.webp)

Wprowadź opis faktury, a następnie wpisz kwotę, którą chcesz otrzymać.

⚠️ Przy pierwszej transakcji w Breez będziesz musiał zapłacić opłatę za otwarcie i utrzymanie kanału w wysokości **2500 satoshi**. W przeciwieństwie do większości portfeli Lightning, Breez udostępnia całą infrastrukturę węzła Lightning, dając Ci swobodę zarządzania swoimi bitcoinami. Musisz samodzielnie otwierać kanały płatności i masz możliwość bezpośredniej komunikacji z węzłem Lightning z poziomu aplikacji.

*Nie martw się, tę opłatę płacisz tylko raz, podczas inicjalizacji portfela.*
![receive-invoice](assets/fr/08.webp)

Po wygenerowaniu faktury możesz ją udostępnić lub zeskanować, aby uregulować płatność i otrzymać bitcoiny.

Wysyłanie bitcoinów za pomocą Breez jest równie intuicyjne jak ich odbieranie. Breez oferuje trzy opcje wysyłania bitcoinów:

- **Wklej fakturę lub ID użytkownika**: Zapłać fakturę Lightning.
- **Połącz się, aby zapłacić**: Utwórz sesję i zaproś odbiorcę do dołączenia, aby wysłać mu bitcoiny.
- **Wyślij na adres BTC**: Wykonaj transakcję w sieci głównej Bitcoin.

![send-bitcoins](assets/fr/09.webp)

Następnie wprowadź informacje odbiorcy lub zeskanuj, aby zainicjować płatność faktury, a następnie zatwierdź.

![validate-send](assets/fr/10.webp)

### Cechy szczególne tego portfela

Oprócz bycia intuicyjnym portfelem do przechowywania bitcoinów, Breez to innowacyjny ekosystem. W aplikacji znajdziesz przydatne usługi:

- **Słuchanie podcastów**: Breez działa jako odtwarzacz podcastów 2.0, umożliwiając wspieranie ulubionych twórców darowiznami w bitcoinach. W menu wybierz **Podcasty**, aby odkrywać i słuchać ulubionych twórców treści.

![podcasts](assets/fr/11.webp)

Wspieraj twórców treści bezpośrednio z aplikacji, przekazując darowizny.

![boost](assets/fr/12.webp)

- **Punkt sprzedaży (POS)**: Breez doskonale nadaje się do Twojego biznesu, umożliwiając prowadzenie punktu sprzedaży w aplikacji. Możesz zarządzać inwentarzem sklepu, odbierać płatności od klientów i generować faktury do wydruku dla każdego zakupu. Ponadto możesz ustawić lokalne waluty spośród wielu obsługiwanych przez Breez.

Możesz dostosować waluty w menu **Preferencje > Waluty fiducjarne**.

![custom-fiat](assets/fr/13.webp)

W menu **Punkt sprzedaży (POS)** możesz skonfigurować artykuły, które sprzedajesz w swoim sklepie.

![products](assets/fr/14.webp)

Po skonfigurowaniu inwentarza możesz łatwo fakturować zakupy tych produktów swoim klientom i akceptować bitcoiny w swoim biznesie.

![print-receipe](assets/fr/15.webp)

- **Dostęp do usług zewnętrznych**: Breez integruje usługi zewnętrzne, które pozwalają na więcej działań bez opuszczania portfela. Znajdziesz m.in. Bitrefill, LN Markets, Wavlake, Fold, Fixed Float, The Bitcoin Company, Azteco, Boltz, Geyser, Lightsats, SMS Sats, LN.PIZZA, LNCAL.

![apps](assets/fr/16.webp)

### Siła Breez

Breez stawia na Twoją autonomię. Infrastruktura Breez udostępnia funkcjonalny węzeł, z którym możesz interagować z poziomu aplikacji (opcja **Deweloperzy**). Masz również autonomię w dostosowywaniu podstawowych konfiguracji, takich jak:

- Połączenie z węzłem Bitcoin/Lightning: Menu **Preferencje > Sieć**.

![reseau](assets/fr/17.webp)

- Personalizacja opłat transakcyjnych: Menu **Preferencje > Opłaty Lightning**.

![fees](assets/fr/18.webp)

- Zarządzanie kanałami płatności: Menu **Preferencje > Zamknij kanały**.

![channels](assets/fr/19.webp)

⚠️ **WAŻNE**: Zalecamy posiadanie pewnego doświadczenia z konfiguracjami Lightning przed wprowadzeniem jakichkolwiek zmian. Twoje przyszłe transakcje będą bezpośrednio wpływane przez te zmiany, a Twoje bitcoiny mogą zostać utracone.

Dla bardziej zaawansowanych użytkowników możesz interagować z węzłem z menu **Preferencje > Deweloperzy**. Znajdziesz tam linie poleceń Lightning, które możesz wykonać, dodając wymagane argumenty.

![dev-mode](assets/fr/20.webp)

Gratulacje, teraz masz dobre rozeznanie w portfelu Breez. Jeśli uważasz, że ten artykuł był pomocny, prosimy o zostawienie zielonego kciuka w górę. To sprawi nam ogromną radość. Dziękujemy!
