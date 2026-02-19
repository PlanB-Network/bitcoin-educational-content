---
name: Blitz Wallet
description: Najprostszy portfel Bitcoin.
---

![cover](assets/cover.webp)

Doświadczenie użytkownika jest jednym z decydujących czynników przy wyborze portfela Bitcoin. W tym samouczku przedstawiamy Blitz Wallet — portfel, który stawia prostotę w centrum swojego podejścia: dzięki integracji protokołu **Spark**, Blitz oferuje jeden z najprostszych i najbardziej kompletnych portfeli Bitcoin na rynku, z natychmiastowymi płatnościami i bez konieczności zarządzania kwestiami technicznymi.

## Czym jest Blitz Wallet?

Blitz Wallet to portfel Bitcoin typu **self-custodial** i **open source**, który stawia na Twoją suwerenność oraz płynne i intuicyjne doświadczenie użytkownika.

[Blitz Wallet](https://blitz-wallet.com/) to aplikacja mobilna dostępna na Androida (Play Store) i iOS (App Store).

W przeciwieństwie do tradycyjnych portfeli Lightning, które wymagają zarządzania kanałami płatniczymi i płynnością przychodzącą, Blitz Wallet opiera się na **protokole Spark**, aby wyeliminować te złożone kwestie techniczne. Efekt: natychmiastowe płatności od pierwszego otrzymanego satoshi, bez żadnej wstępnej konfiguracji. Celem Blitz jest uczynienie płatności w bitcoinie tak prostymi jak zwykła aplikacja płatnicza, nigdy nie rezygnując z self-custody Twoich środków.

Blitz Wallet obsługuje również **czytelne adresy** w formacie `użytkownik@domena.com` (przez LNURL), co pozwala wysyłać bitcoiny tak łatwo jak e-mail, bez konieczności operowania długimi fakturami (invoice) czy QR codes przy każdej transakcji.

## Zrozumieć protokół Spark

Zanim przejdziemy do praktyki, warto zrozumieć technologię, która napędza Blitz Wallet od środka: **protokół Spark**.

### Czym jest Spark?

Spark to protokół warstwy nadrzędnej open source zbudowany na Bitcoinie, opracowany przez zespół Lightspark. Umożliwia przeprowadzanie natychmiastowych transakcji o niskim koszcie, zachowując jednocześnie self-custody Twoich bitcoinów.

W przeciwieństwie do Lightning Network, który opiera się na **kanałach płatniczych** między dwiema stronami, Spark wykorzystuje technologię zwaną **statechain** (łańcuch stanów). Podstawowa zasada jest następująca: zamiast przemieszczać bitcoiny na blockchainie przy każdej transakcji, Spark przenosi **prawo do wydawania** z jednego użytkownika na drugiego, bez ruchu on-chain.

### Jak to działa?

Aby zrozumieć Spark w sposób intuicyjny, wyobraźmy sobie, że wydanie bitcoina na Spark wymaga ułożenia puzzla z dwóch elementów:
- Jeden element posiada użytkownik (na przykład Alicja).
- Drugi element posiada grupa operatorów zwana **Spark Entity (SE)**.

Tylko połączenie dwóch pasujących elementów pozwala wydać bitcoiny.

Kiedy Alicja chce wysłać swoje bitcoiny do Boba, dzieje się następująca rzecz: nowy puzzle jest tworzony wspólnie między Bobem a SE. Puzzle zachowuje ten sam kształt, ale elementy, które go tworzą, zmieniają się. Teraz to element Boba pasuje do elementu SE. Stary element Alicji staje się bezużyteczny, ponieważ SE zniszczył swój odpowiadający element. Własność bitcoinów zmieniła ręce, **bez żadnej transakcji na blockchainie**.

Bob może następnie powtórzyć ten sam proces, aby wysłać te bitcoiny do Carol, i tak dalej. Każdy transfer działa poprzez wymianę elementów puzzla, a nie przez ruch środków on-chain.

### Dlaczego to jest bezpieczne?

Pojawia się uzasadnione pytanie: co się stanie, jeśli SE nie zniszczy naprawdę swojego starego elementu?

Spark Entity nie jest pojedynczą jednostką: to grupa niezależnych operatorów. Element SE nigdy nie jest w posiadaniu jednego operatora. Wymiana puzzla wymaga współpracy kilku operatorów. Wystarczy, że **jeden jedyny operator będzie uczciwy** podczas transferu, aby uniemożliwić reaktywację starego puzzla. Żaden pojedynczy operator nie może potajemnie zachować starego aktywnego puzzla ani odtworzyć go później.

Ponadto Spark zawiera mechanizm jednostronnego wyjścia: zawsze możesz odzyskać swoje bitcoiny on-chain bez współpracy SE. Ten mechanizm awaryjny jest integralną częścią architektury Spark i gwarantuje, że nigdy nie jesteś zależny od sieci, aby uzyskać dostęp do swoich środków.

### Spark vs Lightning Network

Spark i Lightning nie konkurują ze sobą: są **komplementarne**. Blitz Wallet integruje oba, co pozwala korzystać z zalet każdego z nich.

|                               | **Spark**                      | **Lightning Network**    |
| ----------------------------- | ------------------------------ | ------------------------ |
| **Technologia**               | Statechains (łańcuchy stanów)  | Kanały płatnicze         |
| **Zarządzanie kanałami**      | Niewymagane                    | Wymagane                 |
| **Płynność przychodząca**     | Niewymagana                    | Wymagana                 |
| **Natychmiastowe transakcje** | Tak                            | Tak                      |
| **Self-custody**              | Tak                            | Tak                      |
| **Kompatybilność Lightning**  | Tak (przez atomic swaps)       | Natywna                  |

Lightning Network pozostaje doskonałym protokołem do natychmiastowych płatności, ale narzuca ograniczenia techniczne (zarządzanie kanałami, płynność przychodząca, węzeł online...), które mogą zniechęcać początkujących. Spark usuwa te ograniczenia, pozostając jednocześnie kompatybilny z Lightning.

## Instalacja i konfiguracja

W tym samouczku opieramy się na wersji Android Blitz Wallet, ale wszystkie przedstawione poniżej procesy są również ważne dla iOS.

![installation](assets/fr/01.webp)

Ponieważ Blitz Wallet jest portfelem self-custody, masz wybór między **utworzeniem nowego portfela** a **zaimportowaniem frazy odzyskiwania** (12 lub 24 słów) z istniejącego portfela.

Tutaj wybieramy utworzenie nowego portfela. Poniżej znajdziesz nasze zalecenia dotyczące tworzenia kopii zapasowej frazy odzyskiwania:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗ **WAŻNE**: Te 12 lub 24 słowa odzyskiwania to **jedyny klucz dostępu do Twoich bitcoinów**. Blitz jest portfelem self-custodial: ani Blitz, ani Spark nie mają dostępu do Twojej frazy odzyskiwania ani do Twoich środków. Jeśli stracisz te słowa, bezpowrotnie utracisz dostęp do swoich bitcoinów. Nie udostępniaj ich nikomu: każdy, kto je posiada, może wydać Twoje bitcoiny.

Następnie utwórz **kod PIN**, aby zabezpieczyć dostęp do portfela.

![setup-wallet](assets/fr/02.webp)

## Pierwsze kroki z Blitz

Przeprowadzanie transakcji w Blitz jest bardziej intuicyjne niż w większości innych portfeli Bitcoin. Interfejs jest minimalistyczny i skoncentrowany na trzech głównych akcjach: wyślij, skanuj i odbierz.

### Odbieranie bitcoinów

Aby otrzymać bitcoiny na portfelu Blitz, kliknij ikonę **"Strzałka w dół"** (↓), wpisz kwotę w satoshi, którą chcesz otrzymać, dodaj opcjonalny opis, a portfel wygeneruje fakturę (invoice), którą możesz udostępnić nadawcy.

⚠️ **UWAGA**: Satoshi (lub "sat") to najmniejsza jednostka bitcoina: **1 bitcoin = 100 000 000 satoshi**.

Jedną z cech wyróżniających Blitz Wallet jest obsługa wielu sieci i protokołów ekosystemu Bitcoin:

- **Lightning Network**: Jedna z warstw nadrzędnych Bitcoina, która umożliwia dokonywanie natychmiastowych mikropłatności z bardzo niskimi opłatami. Idealna do małych codziennych kwot.

- **Bitcoin (on-chain)**: Główny blockchain protokołu Bitcoin, odpowiedni do transakcji o wyższych kwotach, gdzie maksymalne bezpieczeństwo i ostateczność są priorytetem.

- **Liquid Network**: Sidechain (łańcuch równoległy) Bitcoina opracowany przez Blockstream, który umożliwia szybkie i poufne transakcje z wykorzystaniem Liquid Bitcoin (L-BTC).

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Domyślnie Blitz generuje fakturę Lightning, ale możesz wybrać sieć, na której chcesz otrzymać satoshi, klikając przycisk **"Choose format"** (Wybierz format).

![receive-sats](assets/fr/03.webp)

### Tworzenie kontaktów

Blitz Wallet upraszcza cykliczne wysyłanie bitcoinów dzięki systemowi kontaktów.

W menu **Contacts** możesz zapisać nazwy użytkowników Blitz lub adresy Lightning (LNURL), z którymi często wchodzisz w interakcje.

Dzięki temu możesz wysyłać satoshi na te adresy za pomocą kilku kliknięć, bez konieczności skanowania QR code lub ręcznego wpisywania adresu za każdym razem.

### Wysyłanie bitcoinów

Oprócz klasycznych metod wysyłania bitcoinów (skanowanie QR code, ręczne wpisywanie adresu), Blitz oferuje kilka praktycznych opcji:

- **Z obrazu** (*From Image*): Zaimportuj QR code z galerii zdjęć.
- **Ze schowka** (*From Clipboard*): Wklej wcześniej skopiowany adres lub fakturę.
- **Ręczne wprowadzanie** (*Manual Input*): Wpisz bezpośrednio adres Bitcoin, fakturę Lightning lub czytelny adres (na przykład `użytkownik@walletofsatoshi.com`).
- **Z kontaktów**: Wybierz wcześniej zapisanego odbiorcę, aby wysłać za pomocą kilku kliknięć.

W menu **Wallet** kliknij przycisk **"Strzałka w górę"** (↑), wybierz metodę wysyłania, wpisz kwotę do wysłania, dodaj opis i potwierdź transakcję.

Minimalna kwota do wysłania wynosi obecnie **1 000 satoshi**.

![send-bitcoin](assets/fr/05.webp)

## Sklep Blitz

Poza operacjami transferu bitcoinów, Blitz Wallet posiada wbudowany sklep, w którym możesz wydawać bitcoiny na zakup usług cyfrowych bezpośrednio z aplikacji.

Z menu głównego kliknij zakładkę **Store**, aby uzyskać dostęp do sklepu. Znajdziesz tam również dostęp do platformy **Bitrefill**, która pozwala kupować karty podarunkowe u tysięcy sprzedawców na całym świecie, bezpośrednio za bitcoiny.

- **Sztuczna inteligencja**: Uzyskaj dostęp do najnowszych modeli generatywnej sztucznej inteligencji (Claude 3.5 Sonnet, GPT-4o, GPT-4o-mini, Gemini Flash 1.5) i płać za kredyty bezpośrednio w satoshi. Dostępnych jest kilka pakietów w zależności od potrzeb (Casual, Pro, Power).

![ia-credits](assets/fr/06.webp)

- **Anonimowe SMS-y**: Wysyłaj i odbieraj SMS-y na całym świecie bez ujawniania osobistego numeru telefonu. Usługa jest rozliczana w satoshi za każdą wysłaną wiadomość.

![sms-credit](assets/fr/07.webp)

- **VPN WireGuard**: Chroń swoją prywatność online, wykupując subskrypcję VPN WireGuard (tygodniową, miesięczną lub kwartalną), płatną w bitcoinie bezpośrednio ze sklepu Blitz. Wystarczy pobrać aplikację kliencką WireGuard na swoje urządzenie, aby z niej korzystać.

![wireguard](assets/fr/08.webp)

https://planb.academy/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

## Blitz Wallet od kuchni: szczegóły techniczne

Za prostotą użytkowania Blitz Wallet kryje się przemyślana architektura techniczna, która łączy kilka warstw ekosystemu Bitcoin.

### Rozkład salda

Blitz Wallet zarządza Twoim saldem w sposób przejrzysty, rozdzielając środki między różne protokoły w zależności od potrzeb. Gdy Twoje saldo jest niższe niż 500 000 satoshi, Blitz wykorzystuje **Liquid Network** i wymiany atomowe (*atomic swaps*), aby zapewnić płynne doświadczenie i umożliwić transakcje w Lightning Network nawet przy małych kwotach.

Takie podejście gwarantuje prostą obsługę dla nowych użytkowników, bez konieczności rozumienia mechanizmów działających w tle. Rozkład salda między poszczególnymi warstwami możesz sprawdzić w menu **Ustawienia > Balance Info**.

![balance](assets/fr/09.webp)

### Tryb Lightning (opcjonalny)

Domyślnie Blitz Wallet korzysta z Liquid Network i protokołu Spark, aby zapewnić płynne doświadczenie bez konfiguracji technicznej. Jednak Blitz daje możliwość aktywacji **trybu Lightning**, który automatycznie otworzy kanał płatniczy, gdy Twoje saldo osiągnie **500 000 satoshi** (0,005 BTC).

Aby aktywować tryb Lightning, przejdź do **Ustawień**, a następnie w sekcji **Ustawienia techniczne** kliknij opcję **Node Info**.

![enable-lightning](assets/fr/10.webp)

Dzięki protokołowi Spark ta aktywacja jest **opcjonalna**: Spark już umożliwia dokonywanie płatności kompatybilnych z Lightning bez konieczności otwierania kanału ani zarządzania płynnością przychodzącą. Natywny tryb Lightning pozostaje przydatny dla zaawansowanych użytkowników, którzy chcą dysponować własnym węzłem Lightning zintegrowanym z aplikacją.

### Punkt sprzedaży (PoS)

Blitz Wallet posiada wbudowaną funkcję **punktu sprzedaży**, która pozwala sprzedawcom przyjmować płatności w bitcoinie bezpośrednio z aplikacji.

W menu **Ustawienia > Point-of-sale** możesz skonfigurować:

- Unikalny identyfikator Twojego sklepu
- Lokalną walutę fiducjarną, w której wyświetlane są ceny
- Instrukcje dla pracowników
- Opcję napiwku dla klientów

Twoi klienci muszą jedynie zeskanować wygenerowany QR code, aby dokonać natychmiastowej płatności w bitcoinie.

![pos](assets/fr/11.webp)

https://planb.academy/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

Źródła wykorzystane do napisania tego samouczka:
- Blog [Breez](https://breez.technology/) Technology: [*Spark Explained Like You're Five*](https://blog.breez.technology/spark-explained-like-youre-five-8d554aad18d0).
