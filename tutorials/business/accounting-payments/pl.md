---
name: Śledzenie Bitcoin jako działalności gospodarczej

description: Naucz się łatwo i szybko rozliczać płatności Bitcoin w małej firmie.
---

![cover](assets/cover.webp)


## Wprowadzenie


Celem tego samouczka jest umożliwienie właścicielowi małej firmy, najlepiej sklepu, sprzedawcy ulicznego lub innej działalności handlowej, akceptowania Bitcoin jako płatności i życia z nim w prosty sposób. Docelowym odbiorcą jest właściciel firmy, który samodzielnie zarządza działalnością handlową i polega na niektórych pracownikach.


### Znane przykłady


W niektórych regionach świata istnieją społeczności, które można określić jako "obiegowe", gdzie Bitcoin jest zarówno akceptowany, jak i powszechnie używany przez ludność do płacenia za usługi w działalności handlowej. Nawet handlowcy, po otrzymaniu zapłaty w Bitcoin od swoich klientów, zawarli umowy ze swoimi dostawcami, aby płacić za towary w Bitcoin.


## Akceptacja Bitcoin


Następnym krokiem jest akceptowanie Bitcoin bezpośrednio w firmie; najprostszym sposobem na to jest zainstalowanie i skonfigurowanie Lightning Network (LN) Wallet do otrzymywania natychmiastowych płatności, umożliwiając klientom płacenie obniżonych opłat transakcyjnych w tym samym czasie.


Dla uproszczenia użyjemy Wallet z Satoshi jako przykładu. Wykonaj poniższe kroki, aby go zainstalować i skonfigurować:


https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Po zapoznaniu się z instrukcją będziesz gotowy do akceptowania Bitcoin jako metody płatności: po prostu otwórz aplikację mobilną i kliknij przycisk "Odbierz", a następnie wprowadź kwotę (zwykle w lokalnej walucie) do generate i Invoice płatną przez użytkownika.


**Pro Tip**: dodanie notatki do Invoice przed jego utworzeniem pozwala na łatwe powiązanie płatności z konkretnym zdarzeniem (np. sprzedaż 1 kg jabłek za 900 Sats). Notatki wstawiane ręcznie nie są widoczne dla kontrahenta, więc będą ograniczone wyłącznie do użytku wewnętrznego.


### Konfiguracja zaawansowana


Nieco bardziej zaawansowaną konfiguracją jest użycie funkcji punktu sprzedaży Wallet z Satoshi, dostępnej z poziomu aplikacji po kliknięciu menu hamburgera w prawym górnym rogu:


![image](assets/en/01.webp)


Jest to jeden z dwóch sposobów uzyskania dostępu do funkcji punktu sprzedaży. Druga metoda to dedykowana aplikacja [Wallet of Satoshi PoS app](https://www.walletofsatoshi.com/pos.)


Korzyści z korzystania z funkcji punktu sprzedaży są trojakie:


- jedyna funkcja recepcji, idealna do pozostawienia pracownikom zbierania płatności od klientów bez możliwości wydawania tych środków;
- umożliwia tworzenie listy cen i produktów dla Twojego sklepu, dzięki czemu możesz tworzyć faktury Lightning, wybierając zakupione produkty;
- pobiera raporty sprzedaży w formacie CSV.


Aby uzyskać więcej informacji, zapoznaj się z dedykowanym samouczkiem na temat Wallet w Satoshi - Punkt sprzedaży:


https://planb.academy/tutorials/business/point-of-sale/wallet-of-satoshi-pos-efc9f266-cb21-49a8-94a8-5fe15a82eb07

## Rozporządzenie


Przepisy dotyczące Bitcoin różnią się znacznie w zależności od kraju. Niektóre kraje mają jasne i surowe przepisy, podczas gdy inne są bardziej niejednoznaczne i niejasne. Wiele krajów wymaga zgłoszenia posiadanego Bitcoin (zarówno jako osoba fizyczna, jak i firma) do celów monitorowania podatkowego lub opodatkowania.


## Rozwiązanie dla sprzedawców


Niezależnie od przepisów obowiązujących w danym kraju, najprostszym działaniem dla właściciela małej firmy jest przeliczenie otrzymanych Bitcoinów na lokalną walutę natychmiast po ich otrzymaniu. W ten sposób można uniknąć komplikacji związanych z przyjmowaniem, deklarowaniem i rozliczaniem Bitcoin w ramach działalności handlowej.


**Uwaga**: W niektórych rodzajach działalności może nie być żadnych dokumentów papierowych związanych z transakcją między klientem a sprzedawcą, więc dla właściciela firmy będzie to jeszcze łatwiejsze i bardziej natychmiastowe!


Przyjrzyjmy się zaletom i wadom tego rozwiązania:


### Zalety


To proste podejście pozwala uniknąć kilku problemów: eliminuje potrzebę stosowania procedur KYC (Know Your Customer) w odniesieniu do Bitcoinów otrzymanych jako płatność, co jest bardzo szkodliwą praktyką dla prywatności i bezpieczeństwa osób fizycznych; oraz utrzymuje działania księgowe bez zmian, ponieważ nie ma potrzeby rejestrowania tych Bitcoinów.


Nie będziesz musiał inwestować dodatkowego czasu i pieniędzy z doradcą podatkowym, aby śledzić te zarobki, ponieważ będą one równe wszystkim innym zarobkom.


### Wady


Wraz ze wzrostem wolumenu transakcji Bitcoin, wprowadzanie gotówki do kasy może stać się niemożliwe, na przykład dostępna gotówka może nie pokrywać wszystkich wpływów z Bitcoin. Jest to jednak mało prawdopodobny scenariusz dla większości właścicieli firm, którzy zaczynają akceptować Bitcoin. Inną potencjalną kwestią w niektórych krajach europejskich jest to, że rodzaj prowadzonej działalności może uniemożliwiać przyjmowanie gotówki jako metody płatności za towary i usługi dostarczane klientom. W takich przypadkach proponowane rozwiązanie nie będzie już wystarczające.


## Raport Bitcoin


Jak widzieliśmy, łatwo jest zaakceptować Bitcoin bez wprowadzania nowych procedur księgowych szkodliwych dla indywidualnej prywatności; jednak nadal wskazane byłoby prowadzenie równoległego systemu księgowego w celu śledzenia przepływu Bitcoin. Nie martw się, może to być tak proste, jak chcesz, o ile rozumiesz, ile Bitcoinów wchodzi i wychodzi z twojego Wallet.


**Uwaga: wypełnienie pola `Nota` podczas tworzenia LN Invoice dla klienta znacznie ułatwi aktualizację księgowania Bitcoin. To samo dotyczy dokonywania płatności LN na rzecz dostawców. Idealnie byłoby, gdyby każda transakcja była powiązana z notą płatności.**


## Wnioski


Akceptacja Bitcoin to tylko pierwszy krok. W przypadku działalności komercyjnej niezbędne jest śledzenie operacji bez poświęcania prywatności i wolności jednostki. Jak już zauważyliśmy, proste rozwiązanie rozwiązuje wiele problemów i satysfakcjonuje wszystkie strony zaangażowane w transakcję - zarówno firmę, jak i klienta.