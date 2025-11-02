---
name: SwapMarket
description: Bitcoin i agregator usług wymiany Lightning
---

![cover](assets/cover.webp)



Transfer środków między Bitcoin, On-Chain i Lightning Network zazwyczaj wymaga albo ręcznego otwarcia kanałów Lightning (technicznego i kosztownego), albo korzystania ze scentralizowanych platform swapowych z KYC. SwapMarket oferuje alternatywę: Swapy atomowe Trustless za pośrednictwem konkurencyjnych dostawców, bez KYC.



Innowacja: chociaż dostawcy są pośrednikami, HTLC (*Kontrakty Hash z blokadą czasową*) matematycznie gwarantują, że Twoje środki pozostają pod Twoją kontrolą. Agregacja kilku dostawców (Boltz, ZEUS Swaps, Eldamar, Middle Way) tworzy konkurencję cenową. Interface web open-source self-hostable.



## Czym jest SwapMarket?



Uruchomiony w 2024 r. agregator typu open source SwapMarket działa jako porównywarka dostawców swapów Bitcoin/Lightning. Użytkownik natychmiast porównuje warunki (opłaty, płynność, limity) i wybiera optymalnego dostawcę.



### Architektura techniczna



**Frontend po stronie klienta**: 100% aplikacja po stronie klienta (Fork Boltz Web App) hostowana na GitHub Pages. Kod działa w przeglądarce bez serwera zaplecza. Historia przechowywana lokalnie (cookies/cache). Publiczny i możliwy do skontrolowania kod źródłowy.



**Provider discovery** : Lista zakodowana w Hard w `src/configs/Mainnet.ts`. Nowi dostawcy dodawani poprzez Pull Request lub e-mail.



**Niezależne backendy**: Każdy dostawca obsługuje swój własny backend Boltz. Interface wysyła zapytania do interfejsów API w czasie rzeczywistym, aby natychmiast porównać oferty.



**HTLC Atomic Swaps**: Kontrakty Hash z blokadą czasową gwarantują atomowość: albo swap zostanie zrealizowany, albo każda ze stron odzyska swoje środki. Ryzyko kontrahenta matematycznie wyeliminowane.



### Filozofia



SwapMarket ogranicza centralizację, tworząc konkurencję między dostawcami w zakresie opłat i płynności. Brak KYC, kod open-source do samodzielnego hostowania, mnożenie niezależnych operatorów w celu uniknięcia pojedynczych punktów awarii.



## Główne cechy



### Rynek dostawców



Interface wyświetla wszystkich aktywnych dostawców: nazwę dostawcy, stosowane opłaty (procentowe i/lub stałe), minimalne/maksymalne dostępne kwoty i obsługiwane typy swapów. Aplikacja bezpośrednio wysyła zapytania do interfejsów API każdego dostawcy wymienionego w pliku konfiguracyjnym w celu uzyskania kwotowań w czasie rzeczywistym. Konkurencja między dostawcami gwarantuje optymalne stawki, zwykle około 0,5% dla standardowych swapów.



### Swapy dwukierunkowe



**Swap-in (On-Chain → Lightning)**: Konwersja BTC On-Chain na satoshis Lightning. Przypadek użycia: zasilanie mobilnego Wallet Lightning, uzyskanie przychodzącej przepustowości na węźle lub natychmiastowa płynność.



**Swap-out (Lightning → On-Chain)**: Konwersja satoshi Lightning na On-Chain BTC. Przypadek użycia: zrzucenie Wallet Lightning do magazynu Cold lub zrównoważenie płynności między warstwami.



### Bezpieczeństwo i odzyskiwanie



**Trustless Atomic Swaps: HTLC gwarantuje, że albo Exchange zostanie zrealizowany w całości, albo każda ze stron odzyska swoją stawkę. Ryzyko kontrahenta jest matematycznie wyeliminowane.



**Mechanizm wykupu**: Każdy swap ma datę wygaśnięcia (TIMELOCK). Jeśli swap się nie powiedzie, środki są automatycznie zwracane po wygaśnięciu. Użytkownik zawsze zachowuje możliwość odzyskania swoich bitcoinów.



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



Aplikacja będzie dostępna pod adresem `http://localhost:3000`. Self-hosting gwarantuje całkowitą kontrolę nad Interface, eliminuje ryzyko cenzury oficjalnej domeny i umożliwia audyt kodu źródłowego przed jego wykonaniem.



### Konfiguracja początkowa



**Wallet Lightning**: Upewnij się, że posiadasz działający Wallet Lightning (Phoenix, Zeus, BlueWallet itp.). W przypadku wymiany generate na Lightning Invoice. Za wymianę zapłacisz Invoice Lightning.



**Wallet On-Chain**: W przypadku wymiany, do wysłania środków potrzebny będzie Wallet Bitcoin On-Chain. W przypadku wymiany należy przygotować Bitcoin otrzymujący Address.



**Opcjonalna konfiguracja**: SwapMarket przechowuje historię swapów i preferencje w plikach cookie przeglądarki. Tworzenie konta nie jest wymagane.



## Dostęp do ustawień i klucza ratunkowego



Przed dokonaniem pierwszej wymiany zdecydowanie zalecamy pobranie **Klucza ratunkowego**. Ten klucz awaryjny umożliwia odzyskanie środków w przypadku problemu technicznego lub utraty dostępu do urządzenia.



### Parametry dostępu



Na stronie głównej SwapMarket kliknij ikonę koła zębatego (⚙️) w prawym górnym rogu Interface, obok formularza wymiany.



![Accès aux paramètres](assets/fr/01.webp)



### Ustawienia strony



Zostanie otwarta strona Ustawienia, na której wyświetlonych zostanie kilka opcji konfiguracji:





- Nominał**: Do wyboru BTC lub Sats
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



Ten pierwszy przykład pokazuje, jak przekonwertować satoshi Lightning na bitcoiny On-Chain.



**Krok 1: Konfiguracja zamiany



Na stronie głównej wybierz formularz wymiany :




- LIGHTNING** (górne pole): Wprowadź kwotę, którą chcesz wysłać w Sats Lightning (przykład: 30 000 Sats)
- Bitcoin** (dolne pole): Kwota, którą otrzymasz jest automatycznie wyświetlana po odjęciu opłat (przykład: Sats 29,320)



W dolnym polu wklej swój **odbierający Bitcoin Address**, gdzie chcesz otrzymać środki. Sprawdź dokładnie ten Address.



Domyślnym dostawcą jest zazwyczaj Boltz Exchange. Opłaty sieciowe i opłaty dostawcy są wyraźnie wyświetlane.



![Configuration swap-out](assets/fr/03.webp)



**Krok 2: Wybór dostawcy**



Kliknij menu rozwijane dostawcy (domyślnie: "Boltz Exchange"), aby wyświetlić wszystkich dostępnych dostawców płynności.



Zostanie otwarte okno modalne z tabelą porównawczą:




- Status**: Wskaźnik Green, jeśli dostawca jest aktywny
- Pseudonim**: Nazwa dostawcy (Boltz Exchange, Middle Way, Eldamar, ZEUS Swaps)
- Opłata**: Opłaty naliczane przez dostawcę (zazwyczaj od 0,49% do 0,5%)
- Max Swap**: Maksymalna kwota akceptowana dla swapu



Porównaj opłaty i maksymalne kwoty, a następnie wybierz odpowiedniego dostawcę.



**Uwaga**: Wybór dostawcy Interface nie wyświetla **minimalnych kwot** dla każdego dostawcy. Informacje te pojawiają się tylko w Interface tworzenia zamiany, po wybraniu dostawcy. Minimalne i maksymalne kwoty mogą się różnić w zależności od dostawcy i mogą się zmieniać w czasie. **Zawsze sprawdzaj te limity w momencie wymiany**: jeśli kwota, którą chcesz zamienić, wykracza poza limity dostawcy, możesz wybrać innego, bardziej odpowiedniego dla Twojej transakcji.



![Sélection du provider](assets/fr/04.webp)



**Krok 3: Utworzenie swapu i płatność Lightning**



Kliknij na żółty przycisk **"UTWÓRZ SWAP ATOMOWY "**. SwapMarket utworzy generate z **Lightning Invoice** (BOLT11), abyś mógł zapłacić ze swojego Wallet Lightning.



Zostanie wyświetlona strona :




- Swap ID**: Unikalny identyfikator swapu (przykład: J4ymFIMVR6Hm)
- Status**: "swap.created" (swap utworzony, oczekuje na płatność)
- Kod QR**: Zeskanuj go za pomocą Wallet Lightning
- Invoice Lightning**: Ciąg znaków zaczynający się od "lnbc" (przykład: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)



Zapłać Invoice ze swojego Wallet Lightning (Phoenix, Zeus, BlueWallet itp.). Wyświetlana jest dokładna kwota do zapłaty (przykład: 30 000 Sats).



![Paiement Lightning](assets/fr/05.webp)



**Krok 4: Potwierdzenie i akceptacja**



Po potwierdzeniu płatności Lightning, SwapMarket natychmiast otrzymuje płatność, a dostawca transmituje transakcję Bitcoin do Address.



Status zmieni się na **"Invoice.settled "** (Invoice opłacony) i pojawi się komunikat potwierdzający.



Twoje bitcoiny On-Chain będą dostępne natychmiast po potwierdzeniu transakcji (zwykle w ciągu kilku minut do kilku godzin, w zależności od opłat Mining wybranych przez dostawcę).



![Confirmation swap-out](assets/fr/06.webp)



Możesz kliknąć **"OTWÓRZ TRANSAKCJĘ KLIENTA "**, aby wyświetlić transakcję Bitcoin w eksploratorze Blockchain.



### Zamiana: Bitcoin → Lightning



Ten drugi przykład pokazuje, jak przekonwertować bitcoiny On-Chain na satoshi Lightning.



**Krok 1: Konfiguracja zamiany



Na stronie głównej wybierz formularz wymiany :




- Bitcoin** (górne pole): Wprowadź kwotę, którą chcesz wysłać w Sats Bitcoin (przykład: 63 400 Sats)
- LIGHTNING** (dolne pole): Kwota, którą otrzymasz jest automatycznie wyświetlana po odjęciu opłat (przykład: 62 884 Sats)



W dolnym polu wklej adres Lightning** Invoice (BOLT11) wygenerowany z urządzenia Wallet Lightning lub użyj adresu LNURL Address, jeśli urządzenie Wallet go obsługuje.



![Configuration swap-in](assets/fr/07.webp)



**Krok 2: Sprawdzenie klucza ratunkowego**



Po kliknięciu na **"CREATE ATOMIC SWAP "**, pojawi się okno modalne z prośbą o weryfikację klucza ratunkowego.



![Modal Rescue Key](assets/fr/08.webp)



**Boltz Rescue Key**: Ponieważ klucz odzyskiwania został już przesłany podczas początkowej konfiguracji (patrz poprzednia sekcja), kliknij przycisk **"VERIFY EXISTING KEY "**, aby zaimportować zapisany klucz.



Wybierz wcześniej pobrany plik klucza ratunkowego. Po pomyślnej weryfikacji Interface automatycznie przejdzie do następnego kroku.



**Krok 3: Bitcoin** depozyt Address



SwapMarket generuje teraz **unikalny Bitcoin Address** zawierający HTLC Contract połączony z twoim Lightning Invoice.



Zostanie wyświetlona strona :




- Swap ID**: Unikalny identyfikator (przykład: 1kGmB6JyGqU4)
- Status** : "Invoice.set" (Invoice ustawiony, oczekuje na płatność Bitcoin)
- Kod QR**: Bitcoin zajezdnia Address
- Bitcoin** Address: Zwykle zaczyna się od "bc1p..." (przykład: bc1p5mvtwxapjkds...9d4n9f)
- Ostrzeżenie w kolorze żółtym** : "Upewnij się, że transakcja zostanie potwierdzona w ciągu ~24 godzin od utworzenia tej zamiany!"



Ten okres ~24 godzin to **timeout** HTLC Contract. Jeśli transakcja Bitcoin nie zostanie potwierdzona w tym czasie, wymiana nie powiedzie się i będziesz musiał użyć klucza ratunkowego, aby odzyskać środki.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Możesz skopiować Address klikając na przycisk **"Address"** lub zeskanować kod QR bezpośrednio z Wallet On-Chain.



**Krok 4: Wysyłanie bitcoinów**



Ze swojego Wallet Bitcoin On-Chain wyślij **dokładnie** wskazaną kwotę (np. 63 400 Sats) do wygenerowanego Address.



**Ważne**: Użyj odpowiednich opłat Mining, aby zagwarantować szybkie potwierdzenie. Jeśli opłata jest zbyt niska, a transakcja pozostanie w Mempool po upływie limitu czasu (~24 godziny), zamiana nie powiedzie się.



Po wysłaniu transakcji SwapMarket wykrywa, że jest ona w Mempool i wyświetla :




- Status** : "transakcja.Mempool"
- Komunikat**: "Transakcja jest w Mempool - Oczekiwanie na potwierdzenie zakończenia zamiany"



![Transaction en mempool](assets/fr/10.webp)



**Krok 5: Potwierdzenie i odbiór błyskawicy**



Gdy tylko transakcja Bitcoin otrzyma swoje pierwsze potwierdzenie, dostawca automatycznie wypłaci środki z karty Lightning Invoice. Natychmiast otrzymujesz satoshis na swoim Wallet Lightning.



Status zmienia się na **"transaction.claim.pending "**, a następnie wyświetlany jest komunikat potwierdzający:



![Confirmation swap-in](assets/fr/11.webp)



Satoshi Lightning są natychmiast dostępne w Wallet.



## Zalety i ograniczenia



### Korzyści



**Konkurencja cenowa**: Agregacja dostawców tworzy naturalną konkurencję, która obniża opłaty (od 0,49% do 0,5%).



**Poufność**: Brak KYC, Interface w 100% po stronie klienta (brak transmisji danych osobowych), kompatybilny z przeglądarką Tor.



**Bez nadzoru**: HTLC matematycznie gwarantuje wyłączną kontrolę nad Twoimi środkami. Albo zamiana się powiedzie, albo odzyskasz swoje bitcoiny.



**Open-source self-hostable**: audytowalny kod publiczny, wdrażany lokalnie dla maksymalnej odporności na cenzurę.



### Ograniczenia



**Ograniczona płynność**: Ograniczona liczba aktywnych dostawców (Boltz, Eldamar, MiddleWay w zależności od okresu). Maksymalne kwoty mogą być ograniczone.



**Czas wygaśnięcia**: Limit czasu od 24h do 48h. Jeśli transakcja On-Chain nie zostanie potwierdzona przed wygaśnięciem, wymagane jest ręczne odzyskanie.



**Centralizacja Interface**: Chociaż Interface można hostować samodzielnie, oficjalny Interface jest hostowany na GitHub Pages. Jeśli GitHub ocenzuruje repozytorium, dostęp przez swapmarket.github.io zostanie zablokowany (rozwiązanie: samodzielny hosting).



**Ślady On-Chain**: Skrypty HTLC są potencjalnie identyfikowalne przez zaawansowaną analizę Blockchain.



## Najlepsze praktyki



### Bezpieczna konfiguracja



**Pobierz klucz ratunkowy**: Przed pierwszą wymianą należy pobrać klucz ratunkowy w Ustawieniach (patrz specjalna sekcja powyżej). Ten unikalny klucz będzie działał dla wszystkich przyszłych swapów, umożliwiając odzyskanie środków w przypadku wystąpienia problemu.



**Użyj przeglądarki Tor**: Aby uzyskać maksymalną poufność, uzyskaj dostęp do SwapMarket za pośrednictwem przeglądarki Tor, aby ukryć swoje IP Address.



**Rozważ samodzielny hosting**: Dla użytkowników technicznych, uruchomienie własnej instancji SwapMarket eliminuje zależność od oficjalnej domeny GitHub Pages.



### Optymalizacja wymiany



**Pilnuj Mempool**: Sprawdź Mempool.space przed wymianą. Wybierz czas niskiej aktywności, aby zminimalizować koszty Mining.



**Sprawdź adresy**: W przypadku wymiany należy skrupulatnie sprawdzić otrzymany adres Address. Użyj funkcji kopiuj i wklej i sprawdź pierwsze 5 i ostatnie 5 znaków.



**Przetestuj z małymi ilościami**: Zacznij od minimalnej dozwolonej ilości (25 000 do 50 000 Sats). Zwiększaj stopniowo, gdy opanujesz proces.



**Dokumentuj swoje swapy**: Zanotuj identyfikator każdego swapu, Address wykupu i datę wygaśnięcia. Informacje te ułatwiają śledzenie i odzyskiwanie środków w przypadku problemów technicznych.



### Strategia użytkowania



**Zrównoważ swoje przepływy pieniężne**: Użyj SwapMarket, aby dostosować alokację między On-Chain (oszczędności, długoterminowe bezpieczeństwo) i Lightning (codzienne wydatki, natychmiastowe płatności) zgodnie z rzeczywistymi potrzebami.



**Oblicz rentowność**: W przypadku stałego zapotrzebowania na płynność Lightning, porównaj skumulowany koszt powtarzających się swapów z bezpośrednim otwarciem kanału Lightning. SwapMarket doskonale sprawdza się w przypadku jednorazowych korekt, niekoniecznie w przypadku dużych regularnych przepływów.



## SwapMarket vs Boltz: Jaka jest różnica?



### Boltz: Technologia a usługi



**Boltz to technologia open-source** (`boltz-backend` na GitHub), która implementuje atomowe zamiany poprzez HTLC pomiędzy Bitcoin, Lightning i Liquid.



**Punkt krytyczny**: Wszyscy dostawcy SwapMarket (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) wdrażają własną instancję backendu Boltz. Podstawowa technologia jest zatem identyczna. Luka w backendzie Boltz potencjalnie wpłynęłaby na wszystkich dostawców, ale otwarty charakter systemu umożliwia audyt społeczności.



**Boltz Exchange** to pojedyncza usługa obsługiwana przez zespół Boltz, podczas gdy **SwapMarket** łączy kilku dostawców korzystających z technologii Boltz, tworząc konkurencyjne środowisko cenowe.



Więcej szczegółów można znaleźć w naszych samouczkach Boltz i Zeus Swap:



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.network/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

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



**Zalecenie**: Użyj Boltz Exchange dla uproszczenia lub SwapMarket, aby zoptymalizować koszty poprzez konkurencję. Oba te rozwiązania są równoważne pod względem bezpieczeństwa (HTLC nie podlega ograniczeniom).



## Wnioski



SwapMarket ułatwia wymianę Bitcoin/Lightning poprzez agregację wielu dostawców w jeden Interface. Architektura HTLC gwarantuje, że swapy nie mają charakteru powierniczego, brak KYC zapewnia poufność, a samohostowalny kod open-source wzmacnia odporność na cenzurę.



Konkurencja między dostawcami poprawia stawki i zwielokrotnia źródła płynności. Aby zoptymalizować zarządzanie dwoma Layer (oszczędności On-Chain, wydatki Lightning), SwapMarket jest praktycznym narzędziem, które zachowuje suwerenność finansową i poufność.



## Zasoby



### Oficjalna dokumentacja




- [SwapMarket - aplikacja internetowa](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [Dokumentacja techniczna](https://docs.boltz.Exchange/)
- [Przewodnik po własnym hostingu](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### Powiązane projekty




- [Boltz Exchange](https://boltz.Exchange) - Oryginalna usługa wymiany atomów
- [ZEUS Swaps](https://zeusln.com) - Dostawca swapów Lightning