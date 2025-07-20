---
name: LNP2PBot
description: Kompletny przewodnik po handlu LNP2PBot i P2P Bitcoin
---
![cover](assets/cover.webp)


## Wprowadzenie


Pozbawione KYC giełdy peer-to-peer (P2P) mają zasadnicze znaczenie dla zachowania poufności i autonomii finansowej użytkowników. Umożliwiają one bezpośrednie transakcje między osobami fizycznymi bez konieczności weryfikacji tożsamości, co ma kluczowe znaczenie dla tych, którzy cenią sobie prywatność. Aby uzyskać bardziej dogłębne zrozumienie koncepcji teoretycznych, zapoznaj się z kursem BTC204:


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Kupowanie i sprzedawanie Bitcoin peer-to-peer (P2P) jest jedną z najbardziej prywatnych metod nabywania lub zbywania bitcoinów. LNP2PBot to bot Telegram o otwartym kodzie źródłowym, który ułatwia wymianę P2P na Lightning Network, umożliwiając szybkie, tanie i wolne od KYC transakcje.


### Dlaczego warto korzystać z Lnp2pbot?




- Nie jest wymagany KYC
- Szybkie transakcje na Lightning Network
- Niskie koszty
- Prosty Interface za pośrednictwem Telegram, popularnej aplikacji do przesyłania wiadomości dostępnej z dowolnego miejsca na świecie
- Zintegrowany system reputacji
- Automatyczny depozyt dla bezpiecznego handlu
- Obsługa wielu walut
- Aktywna i rozwijająca się społeczność


### Wymagania wstępne


Aby korzystać z Lnp2pbot, będziesz potrzebować :


1. Lightning Network Wallet (zalecane Breez, Phoenix lub Blixt)


2. Zainstalowana aplikacja Telegram (https://telegram.org/)


3. Konto Telegram ze zdefiniowaną nazwą użytkownika


## Instalacja i konfiguracja


### 1. Konfiguracja urządzenia Lightning Wallet


Zacznij od zainstalowania kompatybilnego Lightning Wallet. Oto nasze szczegółowe zalecenia:


**Zalecane portfele**




- [Breez](https://breez.technology)**:
  - Doskonały dla początkujących
  - Intuicyjny, nowoczesny Interface
  - Non-custodial (zachowujesz kontrolę nad swoimi środkami)
  - Doskonała kompatybilność z Lnp2pbot
  - Dostępne na iOS i Androida


Poniżej znajduje się link do samouczka dla tego Wallet:


https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06


- [Phoenix](https://phoenix.acinq.co)** :
  - Prosty i niezawodny
  - Automatyczna konfiguracja kanałów
  - Natywne wsparcie dla faktur BOLT11
  - Doskonały do codziennych transakcji
  - Dostępne na iOS i Androida


Poniżej znajduje się link do samouczka dla tego Wallet:


https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


- [Blixt](https://blixtwallet.github.io)** :
  - Bardziej techniczny, ale bardzo kompletny
  - Zaawansowane opcje konfiguracji
  - Idealny dla doświadczonych użytkowników
  - Otwarte źródło
  - Dostępne na Androida


Poniżej znajduje się link do samouczka dla Wallet:


https://planb.network/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

**Ważne uwagi dotyczące innych portfeli**


⚠️ **Ważne**: Przed sprzedażą Sats upewnij się, że twój Wallet obsługuje faktury "hold", które są używane przez bota jako system escrow.




- Wallet z Satoshi**: Działa dobrze przy odbiorze Sats, ale może mieć opóźnienia w aktualizacji salda, jeśli sprzedaż zostanie anulowana.
- Muun**: Niezalecane, ponieważ płatności mogą się nie powieść ze względu na limity opłat za routing bota (maksymalnie 0,2%).
- Aqua**: Działa w celu otrzymania Sats, ale może mieć duże opóźnienia (do 48 godzin) w aktualizacji salda w przypadku anulowania sprzedaży.


**Wskazówka**: Aby uzyskać optymalne wrażenia, wybierz zalecane portfele (Breez, Phoenix lub Blixt).


⚠️ **Ważne**: Nie zapomnij zapisać fraz odzyskiwania w bezpiecznym miejscu.


### 2. Rozpoczęcie pracy z Lnp2pbot


1. Kliknij ten link, aby uzyskać dostęp do bota: [@lnp2pBot](https://t.me/lnp2pbot)


2. Telegram otworzy się automatycznie


3. Kliknij "Start" lub wyślij polecenie "/start"


4. Bot poprosi o utworzenie nazwy użytkownika, jeśli jeszcze jej nie masz


5. Bot przeprowadzi cię przez początkową konfigurację


### 3. Dołącz do społeczności




- Dołącz do głównego kanału: [@p2plightning](https://t.me/p2plightning)
- Wsparcie: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)


## Kupowanie i sprzedawanie bitcoinów


Istnieją dwa główne sposoby Exchange bitcoinów na Lnp2pbot:


1. Przeglądaj i odpowiadaj na istniejące oferty na rynku


2. Utwórz własną ofertę kupna lub sprzedaży


W tym przewodniku przyjrzymy się szczegółowo, jak :




- Kup bitcoiny z istniejącej oferty
- Sprzedawaj bitcoiny, tworząc własną ofertę


### Jak kupić Bitcoiny


**1. Znajdź i wybierz ofertę**


![Sélection d'une offre de vente](assets/fr/01.webp)


Przejrzyj oferty w [@p2plightning](https://t.me/p2plightning) i kliknij przycisk "Kup satoshis" pod ogłoszeniem, które Cię interesuje.


**2. Zatwierdź ofertę i kwotę**


![Validation de l'offre](assets/fr/02.webp)


1. Powrót do czatu z botem


2. Potwierdź wybór oferty


3. Wprowadź kwotę w walucie fiducjarnej, którą chcesz kupić


4. Bot poprosi Cię o podanie Błyskawicy Invoice dla kwoty w satoshis


**3. Kontakt ze sprzedawcą**


![Mise en relation](assets/fr/03.webp)


Po wysłaniu Invoice bot kontaktuje się ze sprzedawcą.


**4. Komunikacja ze sprzedawcą**


![Chat privé](assets/fr/04.webp)


Kliknij pseudonim sprzedawcy, aby otworzyć prywatny kanał czatu, na którym możesz podać szczegóły płatności fiat Exchange.


**5. Potwierdzenie płatności


![Confirmation du paiement](assets/fr/05.webp)


Po dokonaniu płatności fiat użyj polecenia `/fiatsent` na czacie bota. Po zakończeniu transakcji będziesz mógł ocenić sprzedawcę, a transakcja zostanie zamknięta.


### Jak sprzedawać Bitcoiny


**1. Utwórz ofertę sprzedaży**


![Création d'une offre de vente](assets/fr/06.webp)


Aby utworzyć ofertę sprzedaży, wystarczy użyć polecenia :


`/sell`


Bot poprowadzi użytkownika krok po kroku:


1. Wybierz walutę


2. Wskaż ilość satoshi do sprzedania


3. W tej cenie dostępne są dwie opcje:




   - Ustaw stałą cenę dla ilości satoshi
   - Użyj ceny rynkowej z opcją zastosowania premii (dodatniej lub ujemnej)


**Wskazówka**: Premia pozwala dostosować cenę w stosunku do ceny rynkowej. Na przykład premia w wysokości -1% oznacza, że sprzedajesz za 1% mniej niż cena rynkowa.


**2. Potwierdzenie utworzenia zamówienia**


![Confirmation de l'ordre de vente](assets/fr/07.webp)


Po utworzeniu zamówienia zobaczysz potwierdzenie z opcją anulowania zamówienia za pomocą polecenia `/cancel`.


**3. Zarządzanie sprzedażą**


![Prise de l'ordre par un acheteur](assets/fr/08.webp)




- Gdy kupujący odpowie na Twoją ofertę, otrzymasz powiadomienie z kodem QR i Invoice do zapłaty.
- Sprawdź profil i reputację kupującego.


![Mise en relation avec l'acheteur](assets/fr/09.webp)




- Kliknij pseudonim kupującego, aby otworzyć prywatny kanał dyskusji.
- Przekazanie szczegółów płatności fiat kupującemu.
- Poczekaj na potwierdzenie płatności fiat od kupującego.
- Sprawdź, czy na Twoje konto wpłynęła płatność.


![Confirmation de la fin de l'ordre](assets/fr/10.webp)




- Potwierdź transakcję za pomocą `/release` i sfinalizuj zamówienie. Będziesz mieć możliwość oceny kupującego.


## Dobre praktyki i bezpieczeństwo


### Wskazówki dotyczące bezpieczeństwa




- Zacznij od małych ilości
- Zawsze sprawdzaj reputację użytkowników
- Używaj tylko sugerowanych metod płatności
- Cała komunikacja odbywa się na czacie bota
- Nigdy nie udostępniaj poufnych informacji


### System reputacji




- Każdy użytkownik ma wynik reputacji
- Udane transakcje zwiększają wynik
- Wybierz użytkowników o dobrej reputacji
- Zgłaszaj moderatorom wszelkie podejrzane zachowania


### Rozstrzyganie sporów


1. Gdy pojawią się problemy, zachowaj spokój i profesjonalizm


2. Użyj polecenia `/dispute`, aby otworzyć zgłoszenie


3. Dostarczenie wszystkich niezbędnych dowodów


4. Poczekaj na moderatora


## Porównanie z innymi rozwiązaniami


Lnp2pbot ma kilka zalet i wad w porównaniu z innymi rozwiązaniami P2P Exchange, takimi jak Peach, Bisq, HodlHodl i Robosat:


### Zalety Lnp2pbot




- Brak wymogu KYC** : W przeciwieństwie do niektórych platform, Lnp2pbot nie wymaga weryfikacji tożsamości, zachowując w ten sposób poufność użytkownika.
- Szybkie transakcje**: Dzięki Lightning Network transakcje są niemal natychmiastowe.
- Niskie opłaty** : Koszty transakcji są niższe niż w przypadku tradycyjnych giełd.
- Dostępność mobilna**: LNP2PBot jest dostępny przez Telegram, co ułatwia korzystanie z niego na urządzeniach mobilnych.
- Łatwy w użyciu** : Intuicyjny Interface sprawia, że Lnp2pbot jest łatwy w użyciu, nawet dla mniej doświadczonych użytkowników.


### Wady Lnp2pbot




- Zależność od Telegrama**: Korzystanie z Lnp2pbot wymaga konta Telegram, które może nie być odpowiednie dla wszystkich użytkowników.
- Mniejsza płynność**: W porównaniu do bardziej uznanych platform, takich jak Bisq, płynność może być bardziej ograniczona.


Dla porównania, rozwiązania takie jak Bisq oferują większą płynność i pulpit Interface, ale mogą wiązać się z wyższymi opłatami i dłuższymi czasami transakcji. Tymczasem HodlHodl i Robosat również oferują handel bez KYC, ale z różnymi strukturami opłat i interfejsami.


## Przydatne zasoby




- Oficjalna strona: https://lnp2pbot.com/
- Dokumentacja: https://lnp2pbot.com/learn/
- GitHub: https://github.com/lnp2pBot/bot
- Wsparcie: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)