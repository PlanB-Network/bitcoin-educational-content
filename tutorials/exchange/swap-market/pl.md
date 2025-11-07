---
name: SwapMarket
description: Bitcoin i agregator usług wymiany Lightning
---

![cover](assets/cover.webp)



Transfer środków między Bitcoin, on-chain i Lightning Network zazwyczaj wymaga albo ręcznego otwarcia kanałów Lightning (technicznego i kosztownego), albo korzystania ze scentralizowanych platform swapowych z KYC. SwapMarket oferuje alternatywę: pozbawione zaufania swapy atomowe za pośrednictwem konkurencyjnych dostawców, bez KYC.



Innowacja: chociaż dostawcy są pośrednikami, HTLC (*Kontrakty Hash z blokadą czasową*) matematycznie gwarantują, że Twoje środki pozostają pod Twoją kontrolą. Agregacja kilku dostawców (Boltz, ZEUS Swaps, Eldamar, Middle Way) tworzy konkurencję cenową. Interface web open-source self-hostable.



## Czym jest SwapMarket?



Uruchomiony w 2024 r. agregator typu open source SwapMarket działa jako porównywarka dostawców swapów Bitcoin/Lightning. Użytkownik natychmiast porównuje warunki (opłaty, płynność, limity) i wybiera optymalnego dostawcę.



### Architektura techniczna



**Frontend po stronie klienta**: 100% aplikacja po stronie klienta (fork Boltz Web App) hostowana na GitHub Pages. Kod działa w przeglądarce bez serwera zaplecza. Historia przechowywana lokalnie (cookies/cache). Publiczny i możliwy do skontrolowania kod źródłowy.



**Provider discovery** : Zakodowana lista w `src/configs/mainnet.ts`. Nowi dostawcy dodawani poprzez Pull Request lub e-mail.



**Niezależne backendy**: Każdy dostawca obsługuje swój własny backend Boltz. Interfejs wysyła zapytania do interfejsów API w czasie rzeczywistym, aby natychmiast porównać oferty.



**HTLC Atomic Swaps**: Kontrakty Hash z blokadą czasową gwarantują atomowość: albo swap zostanie zrealizowany, albo każda ze stron odzyska swoje środki. Ryzyko kontrahenta matematycznie wyeliminowane.



### Filozofia



SwapMarket ogranicza centralizację, tworząc konkurencję między dostawcami w zakresie opłat i płynności. Brak KYC, kod open-source do samodzielnego hostowania, mnożenie niezależnych operatorów w celu uniknięcia pojedynczych punktów awarii.



## Główne cechy



### Rynek dostawców



Interfejs wyświetla wszystkich aktywnych dostawców: nazwę dostawcy, stosowane opłaty (procentowe i/lub stałe), minimalne/maksymalne dostępne kwoty i obsługiwane typy swapów. Aplikacja bezpośrednio wysyła zapytania do interfejsów API każdego dostawcy wymienionego w pliku konfiguracyjnym w celu uzyskania kwotowań w czasie rzeczywistym. Konkurencja między dostawcami gwarantuje optymalne stawki, zwykle około 0,5% dla standardowych swapów.



### Swapy dwukierunkowe



**Swap-in (on-chain → Lightning)**: Konwersja BTC on-chain na satoshis Lightning. Przypadek użycia: zasilanie mobilnego wallet Lightning, uzyskanie przychodzącej przepustowości na węźle lub natychmiastowa płynność.



**Swap-out (Lightning → on-chain)**: Konwersja satoshi Lightning na on-chain BTC. Przypadek użycia: opróżnienie wallet Lightning do chłodni lub zrównoważenie płynności między warstwami.



### Bezpieczeństwo i odzyskiwanie



**Trustless atomic swaps**: HTLC gwarantują, że albo wymiana zostanie zakończona w całości, albo każda ze stron odzyska swoją stawkę. Ryzyko kontrahenta jest matematycznie wyeliminowane.



**Mechanizm spłaty**: Każdy swap posiada blokadę czasową. Jeśli swap się nie powiedzie, środki są automatycznie zwracane po wygaśnięciu. Użytkownik zawsze zachowuje możliwość odzyskania swoich bitcoinów.



**Klucze odzyskiwania**: SwapMarket pozwala eksportować klucze odzyskiwania dla trwających wymian. W przypadku wystąpienia problemu, klucze te mogą być użyte do sfinalizowania lub anulowania wymiany z dowolnego urządzenia.



## Instalacja i dostęp



### Interface web



SwapMarket nie wymaga instalacji. Dostęp można uzyskać za pośrednictwem przeglądarki, odwiedzając stronę https://swapmarket.github.io. Aby uzyskać maksymalną poufność, użyj przeglądarki Brave, Firefox z rozszerzeniami zapobiegającymi śledzeniu lub LibreWolf. Przeglądarka Tor jest zalecana do zachowania anonimowości w sieci.



Nie jest wymagana rejestracja, e-mail ani weryfikacja tożsamości.



### Samodzielny hosting (opcjonalnie)



Dla użytkowników technicznych, którzy chcą wyeliminować jakąkolwiek zależność od oficjalnej domeny GitHub Pages, SwapMarket można uruchomić lokalnie:



**Via npm** :


```
git clone https://github.com/SwapMarket/swapmarket.github.io.git
cd swapmarket.github.io
npm install
npm run dev
```



**Via Docker** :


```
docker run -p 3000:80 ghcr.io/swapmarket/swapmarket:latest
```



Aplikacja będzie dostępna pod adresem `http://localhost:3000`. Self-hosting gwarantuje całkowitą kontrolę nad interfejsem, eliminuje ryzyko cenzury oficjalnej domeny i pozwala na audyt kodu źródłowego przed jego wykonaniem.



### Konfiguracja początkowa



**Wallet Lightning**: Upewnij się, że posiadasz działający wallet Lightning (Phoenix, Zeus, BlueWallet itp.). W przypadku wymiany otrzymasz fakturę Lightning generate. W przypadku wymiany należy zapłacić fakturę Lightning.



**Wallet on-chain**: W przypadku swapów do wysyłania środków potrzebny będzie wallet Bitcoin on-chain. W przypadku wymiany należy przygotować adres odbiorczy Bitcoin.



**Opcjonalna konfiguracja**: SwapMarket przechowuje historię swapów i preferencje w plikach cookie przeglądarki. Tworzenie konta nie jest wymagane.



## Dostęp do ustawień i klucza ratunkowego



Przed dokonaniem pierwszej wymiany zdecydowanie zalecamy pobranie **Klucza ratunkowego**. Ten klucz awaryjny umożliwia odzyskanie środków w przypadku problemu technicznego lub utraty dostępu do urządzenia.



### Parametry dostępu



Na stronie głównej SwapMarket kliknij ikonę koła zębatego (⚙️) w prawym górnym rogu interfejsu, obok formularza wymiany.



![Accès aux paramètres](assets/fr/01.webp)



### Ustawienia strony



Zostanie otwarta strona Ustawienia, na której wyświetlonych zostanie kilka opcji konfiguracji:





- Nominał**: Do wyboru BTC lub sats
- Separator dziesiętny**: Separator dziesiętny (, lub .)
- Powiadomienia dźwiękowe/przeglądarkowe**: Powiadomienia dźwiękowe i powiadomienia przeglądarki
- Klucz odzyskiwania** : Pobierz klucz odzyskiwania
- Dzienniki**: Wyświetlanie, pobieranie lub usuwanie dzienników



![Page Settings](assets/fr/02.webp)



### Pobierz Rescue Key



Kliknij przycisk **Pobierz** obok "Rescue Key".



**Ważne punkty** :




- Rescue Key to **jednorazowy klucz awaryjny**, który działa dla wszystkich przyszłych wymian
- Przechowuj ten klucz w **bezpiecznym i stałym** miejscu (menedżer haseł, sejf cyfrowy)
- W przypadku problemu z wymianą (przekroczenie limitu czasu, awaria techniczna) klucz ten umożliwia odzyskanie środków



## Tworzenie zamiany krok po kroku



### Zamiana: Lightning → Bitcoin



Ten pierwszy przykład pokazuje, jak przekonwertować satoshi Lightning na bitcoiny on-chain.



**Krok 1: Konfiguracja zamiany



Na stronie głównej wybierz formularz wymiany :




- LIGHTNING** (górne pole): Wprowadź kwotę, którą chcesz wysłać w sats Lightning (przykład: 30 000 sats)
- BITCOIN** (dolne pole): Kwota, którą otrzymasz, jest automatycznie wyświetlana po odjęciu opłat (przykład: 29 320 sats)



W dolnym polu wklej swój **adres Bitcoin**, na który chcesz otrzymać środki. Sprawdź dokładnie ten adres.



Domyślnym dostawcą jest zazwyczaj Boltz Exchange. Opłaty sieciowe i opłaty operatora są wyraźnie wyświetlane.



![Configuration swap-out](assets/fr/03.webp)



**Krok 2: Wybór dostawcy**



Kliknij menu rozwijane dostawcy (domyślnie: "Boltz Exchange"), aby wyświetlić wszystkich dostępnych dostawców płynności.



Zostanie otwarte okno modalne z tabelą porównawczą:




- Status**: Wskaźnik Green, jeśli dostawca jest aktywny
- Pseudonim**: Nazwa dostawcy (Boltz Exchange, Middle Way, Eldamar, ZEUS Swaps)
- Opłata**: Opłaty naliczane przez dostawcę (zazwyczaj od 0,49% do 0,5%)
- Max Swap**: Maksymalna kwota akceptowana dla swapu



Porównaj opłaty i maksymalne kwoty, a następnie wybierz odpowiedniego dostawcę.



**Uwaga**: Interfejs wyboru dostawcy nie wyświetla **minimalnych kwot** dla każdego dostawcy. Informacje te pojawiają się tylko w interfejsie tworzenia swapu, po wybraniu dostawcy. Minimalne i maksymalne kwoty mogą się różnić w zależności od dostawcy i mogą się zmieniać w czasie. **Zawsze sprawdzaj te limity w momencie wymiany**: jeśli kwota, którą chcesz wymienić, wykracza poza limity dostawcy, możesz wybrać innego, bardziej odpowiedniego dla Twojej transakcji.



![Sélection du provider](assets/fr/04.webp)



**Krok 3: Utworzenie swapu i płatność Lightning**



Kliknij żółty przycisk **"UTWÓRZ SWAP ATOMOWY "**. SwapMarket wystawi generate **fakturę Lightning** (BOLT11) do opłacenia z twojego wallet Lightning.



Zostanie wyświetlona strona :




- Swap ID**: Unikalny identyfikator swapu (przykład: J4ymFIMVR6Hm)
- Status**: "swap.created" (swap utworzony, oczekuje na płatność)
- Kod QR**: Zeskanuj go za pomocą wallet Lightning
- Invoice Lightning**: Ciąg znaków zaczynający się od "lnbc" (przykład: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)



Zapłać tę fakturę z wallet Lightning (Phoenix, Zeus, BlueWallet itp.). Wyświetlana jest dokładna kwota do zapłaty (przykład: 30 000 sats).



![Paiement Lightning](assets/fr/05.webp)



**Krok 4: Potwierdzenie i akceptacja**



Po potwierdzeniu płatności Lightning, SwapMarket natychmiast otrzymuje płatność, a dostawca transmituje transakcję Bitcoin na Twój adres.



Status zmienia się na **"invoice.settled "** (faktura opłacona) i wyświetlany jest komunikat potwierdzający.



Twoje bitcoiny on-chain będą dostępne natychmiast po potwierdzeniu transakcji (zwykle od kilku minut do kilku godzin, w zależności od opłat mining wybranych przez dostawcę).



![Confirmation swap-out](assets/fr/06.webp)



Możesz kliknąć **"OPEN CLAIM TRANSACTION "**, aby wyświetlić transakcję Bitcoin w przeglądarce blockchain.



### Zamiana: Bitcoin → Lightning



Ten drugi przykład pokazuje, jak przekonwertować bitcoiny on-chain na satoshi Lightning.



**Krok 1: Konfiguracja zamiany



Na stronie głównej wybierz formularz wymiany :




- BITCOIN** (górne pole): Wprowadź kwotę, którą chcesz wysłać w sats Bitcoin (przykład: 63 400 sats)
- LIGHTNING** (dolne pole): Kwota, którą otrzymasz jest automatycznie wyświetlana po odjęciu opłat (przykład: 62 884 sats)



W dolnym polu wklej fakturę Lightning** (BOLT11) wygenerowaną z wallet Lightning lub użyj adresu LNURL, jeśli wallet go obsługuje.



![Configuration swap-in](assets/fr/07.webp)



**Krok 2: Sprawdzenie klucza ratunkowego**



Po kliknięciu na **"CREATE ATOMIC SWAP "**, pojawi się okno modalne z prośbą o weryfikację klucza ratunkowego.



![Modal Rescue Key](assets/fr/08.webp)



**Boltz Rescue Key**: Ponieważ klucz odzyskiwania został już przesłany podczas początkowej konfiguracji (patrz poprzednia sekcja), kliknij przycisk **"VERIFY EXISTING KEY "**, aby zaimportować zapisany klucz.



Wybierz wcześniej pobrany plik Rescue Key. Po pomyślnej weryfikacji interfejs automatycznie przejdzie do następnego kroku.



**Krok 3: Adres depozytowy Bitcoin**



SwapMarket generuje teraz **unikalny adres Bitcoin** zawierający kontrakt HTLC powiązany z fakturą Lightning.



Zostanie wyświetlona strona :




- Swap ID**: Unikalny identyfikator (przykład: 1kGmB6JyGqU4)
- Status**: "invoice.set" (faktura ustawiona, oczekuje na płatność Bitcoin)
- Kod QR**: Adres zajezdni Bitcoin
- Adres Bitcoin**: Zwykle zaczyna się od "bc1p..." (przykład: bc1p5mvtwxapjkds...9d4n9f)
- Ostrzeżenie w kolorze żółtym** : "Upewnij się, że transakcja zostanie potwierdzona w ciągu ~24 godzin od utworzenia tej zamiany!"



Ten okres ~24 godzin to **timeout** kontraktu HTLC. Jeśli transakcja Bitcoin nie zostanie potwierdzona w tym czasie, swap nie powiedzie się i będziesz musiał użyć klucza ratunkowego, aby odzyskać środki.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Możesz skopiować adres, klikając przycisk **"ADRES "** lub zeskanować kod QR bezpośrednio z wallet on-chain.



**Krok 4: Wysyłanie bitcoinów**



Ze swojego wallet Bitcoin on-chain wyślij **dokładnie** wskazaną kwotę (np. 63 400 sats) na wygenerowany adres.



**Ważne**: Użyj odpowiednich opłat mining, aby zagwarantować szybkie potwierdzenie. Jeśli opłata jest zbyt niska, a transakcja pozostanie w mempool po upływie limitu czasu (~24h), zamiana nie powiedzie się.



Gdy transakcja zostanie wysłana, SwapMarket wykryje, że znajduje się ona w mempool i wyświetli :




- Status** : "transaction.mempool
- Komunikat**: "Transakcja jest w mempool - Oczekiwanie na potwierdzenie zakończenia zamiany"



![Transaction en mempool](assets/fr/10.webp)



**Krok 5: Potwierdzenie i odbiór błyskawicy**



Gdy tylko transakcja Bitcoin otrzyma pierwsze potwierdzenie, dostawca automatycznie opłaci Twoją fakturę Lightning. Natychmiast otrzymasz satoshis na swoim wallet Lightning.



Status zmienia się na **"transaction.claim.pending "**, a następnie wyświetlany jest komunikat potwierdzający:



![Confirmation swap-in](assets/fr/11.webp)



Twoje satoshi Lightning są natychmiast dostępne w wallet.



## Zalety i ograniczenia



### Korzyści



**Konkurencja cenowa**: Agregacja dostawców tworzy naturalną konkurencję, która obniża opłaty (od 0,49% do 0,5%).



**Poufność**: Brak KYC, interfejs w 100% po stronie klienta (brak transmisji danych osobowych), kompatybilność z przeglądarką Tor.



**Bez nadzoru**: HTLC matematycznie gwarantuje wyłączną kontrolę nad Twoimi środkami. Albo zamiana się powiedzie, albo odzyskasz swoje bitcoiny.



**Open-source self-hostable**: audytowalny kod publiczny, wdrażany lokalnie dla maksymalnej odporności na cenzurę.



### Ograniczenia



**Ograniczona płynność**: Ograniczona liczba aktywnych dostawców (Boltz, Eldamar, MiddleWay w zależności od okresu). Maksymalne kwoty mogą być ograniczone.



**Czas wygaśnięcia**: Limit czasu od 24h do 48h. Jeśli transakcja on-chain nie zostanie potwierdzona przed wygaśnięciem, wymagane jest ręczne odzyskanie.



**Centralizacja Interface**: Mimo, że self-hostable, oficjalny interfejs jest hostowany na GitHub Pages. Jeśli GitHub ocenzuruje repozytorium, dostęp przez swapmarket.github.io zostanie zablokowany (rozwiązanie: samodzielny hosting).



**Ślady on-chain**: Skrypty HTLC są potencjalnie identyfikowalne przez zaawansowaną analizę blockchain.



## Najlepsze praktyki



### Bezpieczna konfiguracja



**Pobierz klucz ratunkowy**: Przed pierwszą wymianą należy pobrać klucz ratunkowy w Ustawieniach (patrz specjalna sekcja powyżej). Ten unikalny klucz będzie działał dla wszystkich przyszłych swapów, umożliwiając odzyskanie środków w przypadku wystąpienia problemu.



**Użyj przeglądarki Tor**: Aby uzyskać maksymalną poufność, uzyskaj dostęp do SwapMarket za pośrednictwem przeglądarki Tor, aby ukryć swój adres IP.



**Rozważ samodzielny hosting**: Dla użytkowników technicznych, uruchomienie własnej instancji SwapMarket eliminuje zależność od oficjalnej domeny GitHub Pages.



### Optymalizacja wymiany



**Miej oko na mempool**: Sprawdź mempool.space przed wymianą. Wybierz czas niskiej aktywności, aby zminimalizować koszty mining.



**Sprawdź adresy**: W przypadku wymiany należy skrupulatnie sprawdzić adres odbiorczy. Użyj funkcji kopiuj i wklej i sprawdź pierwsze 5 i ostatnie 5 znaków.



**Przetestuj z małymi ilościami**: Zacznij od minimalnej dozwolonej ilości (25 000 do 50 000 sats). Zwiększaj stopniowo, gdy opanujesz proces.



**Dokumentuj swoje swapy**: Zanotuj identyfikator każdego swapu, adres wykupu i datę wygaśnięcia. Informacje te ułatwiają śledzenie i odzyskiwanie środków w przypadku problemów technicznych.



### Strategia użytkowania



**Zrównoważ swoje przepływy pieniężne**: Użyj SwapMarket, aby dostosować alokację między on-chain (oszczędności, długoterminowe bezpieczeństwo) i Lightning (codzienne wydatki, natychmiastowe płatności) zgodnie z rzeczywistymi potrzebami.



**Oblicz rentowność**: W przypadku stałego zapotrzebowania na płynność Lightning, porównaj skumulowany koszt powtarzających się swapów z bezpośrednim otwarciem kanału Lightning. SwapMarket doskonale sprawdza się w przypadku jednorazowych korekt, niekoniecznie w przypadku dużych regularnych przepływów.



## SwapMarket vs Boltz: Jaka jest różnica?



### Boltz: Technologia a usługi



**Boltz to technologia open-source** (`boltz-backend` na GitHub), która implementuje atomowe zamiany poprzez HTLC pomiędzy Bitcoin, Lightning i Liquid.



**Punkt krytyczny**: Wszyscy dostawcy SwapMarket (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) wdrażają własną instancję backendu Boltz. Podstawowa technologia jest zatem identyczna. Luka w backendzie Boltz potencjalnie wpłynęłaby na wszystkich dostawców, ale otwarty charakter systemu pozwala na audyt społeczności.



**Boltz Exchange** to pojedyncza usługa obsługiwana przez zespół Boltz, podczas gdy **SwapMarket** łączy kilku dostawców korzystających z technologii Boltz, tworząc konkurencyjne środowisko cenowe.



Więcej szczegółów można znaleźć w naszych samouczkach Boltz i Zeus Swap:



https://planb.academy/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.academy/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Kluczowe różnice



| Aspect        | Boltz Exchange           | SwapMarket                                 |
| ------------- | ------------------------ | ------------------------------------------ |
| Nature        | Service unique           | Agrégateur multi-providers                 |
| Providers     | Boltz uniquement         | Boltz, ZEUS, Eldamar, Middle Way           |
| Compétition   | Tarifs fixes             | Compétition libre                          |
| Interface     | boltz.exchange           | swapmarket.github.io (self-hostable)       |
| Sécurité      | Non-custodial (HTLC)     | Non-custodial (HTLC)                       |

**Zalety SwapMarket**: Konkurencja cenowa, dywersyfikacja instancji backendowych, porównywanie w czasie rzeczywistym.



**Technologiczne alternatywy** (niekompatybilne ze SwapMarket): Lightning Loop (Lightning Labs), Muun Wallet, NLoop, Breez Wallet. Rozwiązania te wykorzystują własne implementacje swapów podmorskich.



**Zalecenie**: Użyj Boltz Exchange dla uproszczenia lub SwapMarket, aby zoptymalizować koszty poprzez konkurencję. Oba rozwiązania są równoważne pod względem bezpieczeństwa (HTLC nie podlega ograniczeniom).



## Wnioski



SwapMarket ułatwia wymianę Bitcoin/Lightning poprzez agregację wielu dostawców w jednym interfejsie. Architektura HTLC gwarantuje, że swapy nie będą miały charakteru powierniczego, brak KYC zapewnia poufność, a samo-hostowalny kod open-source wzmacnia odporność na cenzurę.



Konkurencja między dostawcami poprawia stawki i zwielokrotnia źródła płynności. Aby zoptymalizować dwupoziomowe zarządzanie (oszczędności on-chain, wydatki Lightning), SwapMarket jest praktycznym narzędziem, które zachowuje suwerenność finansową i poufność.



## Zasoby



### Oficjalna dokumentacja




- [SwapMarket - aplikacja internetowa](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [Dokumentacja techniczna](https://docs.boltz.exchange/)
- [Przewodnik po własnym hostingu](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### Powiązane projekty




- [Boltz Exchange](https://boltz.exchange) - Oryginalna usługa wymiany atomów
- [ZEUS Swaps](https://zeusln.com) - Dostawca błyskawicznych swapów