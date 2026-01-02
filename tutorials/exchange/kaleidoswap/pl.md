---
name: KaleidoSwap
description: Zaawansowany przewodnik po handlu aktywami RGB na Lightning Network z KaleidoSwap
---

![cover](assets/cover.webp)


KaleidoSwap to zaawansowana aplikacja desktopowa o otwartym kodzie źródłowym, która wypełnia lukę między protokołem RGB a Lightning Network. Służy jako kompleksowy interfejs do zarządzania węzłami RGB Lightning, interakcji z dostawcami usług RGB Lightning (LSP) za pośrednictwem specyfikacji LSPS1 i wykonywania atomowych swapów aktywów RGB.


KaleidoSwap, jako rozwiązanie bez nadzoru, umożliwia użytkownikom zachowanie pełnej kontroli nad kluczami i danymi. Wykorzystując paradygmat walidacji RGB po stronie klienta, umożliwia on zawieranie prywatnych i skalowalnych inteligentnych kontraktów na Bitcoin. Ten samouczek zagłębia się w zaawansowane funkcje KaleidoSwap, prowadząc przez zawiłości "kolorowego" zarządzania UTXO, płynność kanałów dla określonych aktywów oraz model handlu taker-maker, zapewniając pełne wykorzystanie tego potężnego zdecentralizowanego protokołu wymiany.


## Instalacja


KaleidoSwap zapewnia wstępnie zbudowane pliki binarne dla głównych systemów operacyjnych, ale dla zaawansowanych użytkowników budowanie ze źródła zapewnia uruchomienie najnowszego kodu z określonymi konfiguracjami.


### Pobieranie plików binarnych


Najnowszą wersję dla swojego systemu operacyjnego można pobrać z [oficjalnej strony](https://kaleidoswap.com/) lub [strony wydań GitHub](https://github.com/kaleidoswap/desktop-app/releases).


### Metody instalacji


1.  **Windows**: Pobierz instalator `.exe` i uruchom go.

2.  **macOS**: Pobierz plik `.dmg`, otwórz go i przeciągnij KaleidoSwap do folderu Aplikacje.

3.  **Linux**: Pobierz plik `.AppImage` lub `.deb` i zainstaluj/uruchom go.



## Opcje konfiguracji węzła


Po pierwszym uruchomieniu KaleidoSwap zostanie wyświetlony **Ekran połączenia**. Jest to pierwszy krok w konfiguracji środowiska.


![Node Selection Screen](assets/en/01.webp)


Należy wybrać sposób połączenia z RGB Lightning Network. Wybór ten ma wpływ na poziom kontroli i prywatności użytkownika.


### Opcja 1: Węzeł lokalny (zalecany do samodzielnego przechowywania)


**Aby uzyskać pełną kontrolę i prywatność**, uruchom węzeł bezpośrednio na swoim komputerze, zobacz zalety poniżej:


- Samodzielna opieka**: Posiadasz klucze. Żadna strona trzecia nie może zamrozić Twoich środków ani cenzurować Twoich transakcji.
- Prywatność**: Dane użytkownika pozostają na urządzeniu.
- Niezależność**: Brak zależności od zewnętrznych dostawców usług.


Jeśli wybierzesz **Węzeł lokalny**, zostaniesz przeniesiony do ekranu konfiguracji, gdzie możesz utworzyć nowy wallet lub przywrócić istniejący.


![Local Node Setup Screen](assets/en/02.webp)


### Opcja 2: Węzeł zdalny


Połącz się ze zdalnym RGB Lightning Node (hostowanym samodzielnie na VPS lub u hostowanego dostawcy).


- Zalety**: Brak wykorzystania zasobów lokalnych, dostępność 24/7.
- Kompromis**: Wymaga zaufania do hosta lub zarządzania zdalnym serwerem.


![Remote Node Setup Screen](assets/en/03.webp)


**Zdecydowanie zalecamy uruchomienie własnego węzła - lokalnie (opcja 1) lub poprzez samodzielne hostowanie zdalnego węzła - aby w pełni wykorzystać odporne na cenzurę właściwości Bitcoin i RGB.


## Tworzenie Wallet


KaleidoSwap zarządza zarówno zasobami Bitcoin, jak i RGB. Proces tworzenia wallet inicjuje magazyn kluczy, który zabezpiecza fundusze on-chain i stany kanału Lightning.


Oto szczegółowy proces:

1. Otwórz KaleidoSwap i wybierz **Węzeł lokalny**.

2. Kliknij na **Utwórz nowy Wallet**.

3. **Konfiguracja konta**: Wprowadź **nazwę konta** i wybierz **sieć** (np. Bitcoin, Mainnet, Testnet, Signet).

4. **Konfiguracja zaawansowana** (opcjonalnie): Jeśli jesteś zaawansowanym użytkownikiem, możesz skonfigurować niestandardowe punkty końcowe RPC, adresy URL indeksatora lub ustawienia proxy w sekcji "Ustawienia zaawansowane".

5. Kliknij przycisk **Kontynuuj**.

6. **Hasło**: Ustaw silne hasło do lokalnego szyfrowania pliku wallet.

7. **Fraza odzyskiwania**: Zapisz swoją frazę seed i przechowuj ją w bezpiecznym miejscu.


    - Krytyczne**: Ta fraza jest niezbędna do odzyskania środków on-chain i tożsamości węzła.
    - Ostrzeżenie**: **Stanów kanału Lightning nie można w pełni odzyskać za pomocą samego seed**. Należy również utrzymywać statyczne kopie zapasowe kanałów (SCB), aby odzyskać środki zablokowane w kanałach.


![Wallet Creation Screen](assets/en/04.webp)



## Przegląd pulpitu nawigacyjnego


Po utworzeniu wallet zostaniesz przekierowany do głównego **Dashboardu**.


![KaleidoSwap Dashboard](assets/en/05.webp)


uwaga: Powyższy zrzut ekranu przedstawia wallet, który został już sfinansowany i ma aktywne kanały. Nowy wallet będzie wykazywał zerowe saldo i brak aktywnych kanałów, dopóki go nie sfinansujesz


## Finansowanie Wallet


Aby korzystać z aktywów RGB, należy zasilić wallet. KaleidoSwap obsługuje deponowanie zarówno aktywów Bitcoin, jak i RGB za pośrednictwem transakcji on-chain lub Lightning Network.


### Deponowanie Bitcoin


1. Kliknij **Depozyt** w menu szybkich akcji.

2. Wybierz **BTC** z listy aktywów.


![Select BTC Asset](assets/en/06.webp)


3. Wybierz metodę wpłaty: **On-chain** lub **Lightning**.


![BTC Deposit Options](assets/en/07.webp)



- On-chain**: Zeskanuj kod QR lub skopiuj adres, aby wysłać Bitcoin z innego wallet.
- Lightning**: Wygeneruj fakturę na żądaną kwotę.


![BTC On-chain Deposit](assets/en/08.webp)


### Deponowanie aktywów RGB i kolorowych UTXO


Aby otrzymać aktywa RGB (takie jak USDT), potrzebne są określone UTXO dostępne do "pokolorowania" (przypisania aktywa).


1. Kliknij **Depozyt** i wybierz aktywa RGB (np. USDT). **Ważne**: Jeśli jest to **pierwszy raz**, gdy węzeł otrzymuje ten konkretny zasób, **pozostaw pole ID zasobu puste**. Wprowadzenie identyfikatora nieznanego zasobu spowoduje, że węzeł zwróci błąd, ponieważ jeszcze go nie rozpoznaje.

2. Wybierz **On-chain** lub **Lightning**.


![USDT Deposit Options](assets/en/09.webp)


#### Łańcuchowe tryby odbioru: Świadek vs. Zaślepiony


Podczas odbierania zasobów RGB on-chain dostępne są dwa tryby prywatności:



- Blinded Receive (zalecane dla zachowania prywatności)**: Przekazujesz nadawcy UTXO "blinded". Prosisz nadawcę o wysłanie zasobów do istniejącego UTXO, który posiadasz, ale zaciemniasz rzeczywisty identyfikator UTXO. Zapewnia to lepszą prywatność.
- Odbiór przez świadka**: Użytkownik podaje standardowy adres Bitcoin. Prosisz nadawcę o utworzenie *nowego* UTXO, wysyłając aktywa na ten adres. Pozwala to na dołączenie aktywów RGB bezpośrednio do nowego UTXO utworzonego przez transakcję.


#### Lightning Deposit


W przypadku wpłat Lightning wystarczy wystawić fakturę generate. Zasób RGB zostanie przekierowany do Ciebie za pośrednictwem otwartych kanałów.


![USDT Lightning Invoice](assets/en/10.webp)



## Otwieranie kanałów za pomocą zasobów RGB


Aby przekierować aktywa RGB przez Lightning Network, potrzebny jest kanał o wystarczającej płynności i alokacji aktywów. Najłatwiejszym sposobem na rozpoczęcie jest **Kupno kanału** od dostawcy LSP (Lightning Service Provider).


### Zakup kanału od Kaleido LSP


1. Przejdź do zakładki **Kanały**. Zobaczysz opcje "Otwórz kanał" (ręcznie) lub "Kup kanał" (LSP).

2. Kliknij **Kanał zakupu**.


![Channels Dashboard](assets/en/11.webp)


3. **Połącz z LSP**: Aplikacja połączy się z domyślnym LSP Kaleido. Ten dostawca oferuje płynność przychodzącą i obsługuje routing aktywów RGB.


![Connect to LSP](assets/en/12.webp)


4. **Konfiguruj kanał**:


    - Pojemność**: Wybierz całkowitą pojemność Bitcoin dla kanału.
    - Alokacja RGB**: Wybierz zasób RGB (np. USDT), który chcesz otrzymywać lub wysyłać. LSP zapewni, że kanał jest skonfigurowany do obsługi tego zasobu.


![Configure Channel](assets/en/13.webp)



    - Alokacja RGB**: Wybierz zasób RGB (np. USDT), który chcesz otrzymywać lub wysyłać. LSP zapewni, że kanał jest skonfigurowany do obsługi tego zasobu.


![RGB Allocation](assets/en/14.webp)


5.  **Płatność**: Musisz uiścić opłatę na rzecz LSP za otwarcie kanału i zapewnienie płynności. Możesz zapłacić za pomocą **Lightning** lub **On-chain** Bitcoin. Płatności można dokonać z wewnętrznego wallet KaleidoSwap lub zewnętrznego wallet.


![Complete Payment](assets/en/15.webp)


6. Po potwierdzeniu płatności LSP zainicjuje transakcję otwarcia kanału. Zostanie wyświetlony ekran **Zamówienie zrealizowane**.


![Order Completed](assets/en/16.webp)


7. Po potwierdzeniu na blockchainie, Twój kanał będzie aktywny i gotowy na transfery RGB.



## Handel: Model Taker-Maker


Silnik transakcyjny KaleidoSwap działa w oparciu o model **Taker-Maker**. Możesz wymieniać aktywa ręcznie z peerem lub skorzystać z Market Makera (LSP).


### Wymiana z animatorem rynku (LSP)


Jest to najczęstszy sposób handlu. Użytkownik działa jako **Taker**, realizując zlecenia w oparciu o dostępną płynność zapewnianą przez LSP (**Maker**).


1. Przejdź do zakładki **Trade** i wybierz **Market Maker**.

2. **Wprowadź kwotę**: Wprowadź kwotę Bitcoin, którą chcesz wysłać (lub aktywa, które chcesz otrzymać). Interfejs pokaże szacowany kurs wymiany i opłaty.


![Market Maker Swap](assets/en/17.webp)


3. **Potwierdź wymianę**: Przejrzyj szczegóły, w tym kurs wymiany i dokładną kwotę, którą otrzymasz. Kliknij **Potwierdź wymianę**.


![Confirm Swap](assets/en/18.webp)


4. **Przetwarzanie**: Zamiana jest wykonywana atomowo na Lightning Network. Zostanie wyświetlony ekran stanu wskazujący, że wymiana jest w toku.


![Swap Pending](assets/en/19.webp)


5. **Success**: Gdy HTLC zostaną rozliczone, swap zostanie zakończony, a aktywa znajdą się w Twoim kanale.


![Swap Success](assets/en/20.webp)



## Deweloper API


Dla programistów budujących na KaleidoSwap, aplikacja udostępnia API, który obsługuje:



- RGB LSPS1**: Dla zautomatyzowanych usług płynności.
- Swap API**: Dla handlu programowego i animacji rynku.
- WebSocket**: Dla subskrypcji danych rynkowych w czasie rzeczywistym.


Pełna dokumentacja i specyfikacje znajdują się w [API Documentation] (https://docs.kaleidoswap.com/api/introduction).


## Wnioski


KaleidoSwap umożliwia wykorzystanie prywatności i skalowalności aktywów RGB na Lightning Network. Dzięki zrozumieniu kolorowych UTXO i alokacji aktywów kanału można w pełni wykorzystać ten potężny zdecentralizowany protokół wymiany.