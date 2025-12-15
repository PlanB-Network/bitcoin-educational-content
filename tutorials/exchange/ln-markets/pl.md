---
name: LN Markets
description: Platforma handlowa Bitcoin na Lightning Network
---

![cover](assets/cover.webp)



LN Markets to pierwsza prawdziwie Lightning-natywna platforma handlowa Bitcoin, umożliwiająca handel lewarowanymi instrumentami pochodnymi Bitcoin bezpośrednio z wallet Lightning, bez KYC, natychmiastowych rozliczeń i minimalnej opieki. Uruchomiona w 2020 r., eliminuje tarcia tradycyjnych giełd: brak weryfikacji tożsamości, brak zablokowanych depozytów, brak oczekiwania na potwierdzenia blockchain. wallet Lightning staje się Twoim kontem handlowym.



## Co to jest LN Markets?



LN Markets oferuje **Futures** (kontrakty wieczyste z dźwignią do 100×) i **Opcje** (Call/Put z ryzykiem ograniczonym do zapłaconej premii). Platforma działa jako warstwa agregacji płynności konsolidująca wiele systemów transakcyjnych w celu optymalnej realizacji bez poślizgu. Twoje środki są zablokowane tylko na dokładny czas trwania aktywnych pozycji, a nie na dni lub tygodnie, jak w przypadku tradycyjnego rachunku powierniczego.



### Dostępne produkty handlowe



**Futures (kontrakty wieczyste)**



Kontrakty wieczyste to kontrakty futures bez daty wygaśnięcia, umożliwiające spekulowanie na trendzie cenowym Bitcoin z wykorzystaniem dźwigni finansowej. LN Markets oferuje dwa tryby zarządzania depozytem zabezpieczającym:



**Tryb izolowany**: Każda pozycja ma własny dedykowany depozyt zabezpieczający. Zagrożone są tylko środki przydzielone do tej konkretnej pozycji. Jeśli pozycja osiągnie cenę likwidacji, **tylko ta pozycja jest likwidowana**, nie ma to wpływu na inne pozycje i pozostałe saldo. Idealny do ścisłego ograniczania ryzyka na transakcję.



**Tryb krzyżowy (Cross Margin)** : Depozyt zabezpieczający jest dzielony pomiędzy wszystkie otwarte pozycje. Całkowite saldo konta służy jako zabezpieczenie dla wszystkich pozycji. Jeśli pozycja nie powiedzie się, system wykorzysta całe dostępne saldo, aby uniknąć likwidacji. **Ryzyko**: w przypadku wyczerpania całkowitego salda, wszystkie pozycje mogą zostać zlikwidowane jednocześnie. Zalecane tylko dla doświadczonych traderów, którzy chcą zmaksymalizować wydajność kapitału.



**Zarządzanie stanowiskami** :





- Pozycja długa**: stawiasz na wzrost BTC/USD. Jeśli cena wzrośnie, wygrywasz; jeśli spadnie, przegrywasz. **Przykład**: Bitcoin na poziomie 100 000 USD, otwierasz pozycję Long z 10 000 sats i dźwignią 10×. Jeśli Bitcoin wzrośnie do $105,000 (+5%), twoja pozycja zyska 50% (5% × 10), tj. ~5,000 sats zysku. Jeśli Bitcoin spadnie do $95,000 (-5%), stracisz 50%, tj. stratę w wysokości ~5,000 sats.





- Pozycja krótka**: stawiasz na spadek BTC/USD. Jeśli cena spadnie, wygrywasz; jeśli wzrośnie, przegrywasz. **Przykład**: Bitcoin po cenie 100 000 USD, otwierasz pozycję krótką z 10 000 sats i dźwignią 10×. Jeśli Bitcoin spadnie do $95,000 (-5%), wygrywasz 50%, tj. ~5,000 sats. Jeśli Bitcoin wzrośnie do 105 000 USD (+5%), stracisz 50%.



Dźwignia finansowa (do 100×) proporcjonalnie zwiększa zyski i straty. Mechanizm **stopy finansowania** (okresowe opłaty co 8 godzin) równoważy długie i krótkie pozycje. Użytkownik może zarządzać nawet 100 pozycjami futures jednocześnie.



**Opcje**



Opcja jest jak **bilet loteryjny z datą wygaśnięcia**. Płacisz premię, aby obstawić kierunek ceny Bitcoin. **Główna zaleta**: nigdy nie możesz stracić więcej niż zapłacona premia, nie ma możliwości likwidacji.





- Opcja kupna (byczy zakład)**: Obstawiasz, że Bitcoin wzrośnie powyżej ceny wykonania przed wygaśnięciem. Wygrywasz, jeśli cena wzrośnie, strata jest ograniczona do premii, jeśli cena spadnie.





- Opcja sprzedaży (zakład niedźwiedzi)**: Obstawiasz, że Bitcoin spadnie poniżej ceny wykonania. Wygrywasz, jeśli cena spadnie, strata jest ograniczona do premii, jeśli cena wzrośnie.





- Straddle (zakład na zmienność)**: Kupujesz jednocześnie opcję kupna i sprzedaży. Wygrywasz, jeśli Bitcoin wykona duży ruch w dowolnym kierunku, tracisz obie premie, jeśli cena pozostanie stabilna.



Limit: 50 jednoczesnych pozycji. Idealny dla początkujących inwestorów korzystających z dźwigni finansowej bez obawy o likwidację.



**sats ↔ sUSD**: Natychmiastowa konwersja satoshis na syntetyczne dolary (sUSD) w celu ochrony przed zmiennością lub odwrotnie, aby odzyskać ekspozycję na Bitcoin.



## Dostęp do platformy i tworzenie konta



### Przejdź do LN Markets



Wejdź na stronę [lnmarkets.com] (https://lnmarkets.com) i kliknij "Otwórz aplikację".



![Page d'accueil LN Markets](assets/fr/01.webp)



### Utwórz konto



Ekran powitalny oferuje kilka metod połączenia:



![Méthodes de connexion](assets/fr/02.webp)



**Dostępne opcje** :


1. **Zarejestruj się za pomocą Lightning wallet** (zalecane): LNURL-auth z Phoenix, Breez, Zeus lub BlueWallet


2. **Zarejestruj się za pomocą adresu e-mail**: konto klasyczne (ogranicza doświadczenie Lightning)


3. **Alby** lub **Ledger**: rozszerzenia przeglądarki



### Połączenie przez Lightning (LNURL-auth)



Kliknij "Zarejestruj się za pomocą wallet Lightning". Zeskanuj kod QR za pomocą wallet Lightning:



![QR code LNURL-auth](assets/fr/03.webp)



Twój wallet automatycznie podpisuje wniosek kryptograficzny, a Twoje konto jest tworzone natychmiast, bez e-maila ani hasła. Silne zabezpieczenia i całkowita anonimowość.



### Konfiguracja początkowa



![Configuration post-connexion](assets/fr/04.webp)



**Dostępne parametry** :




- Nazwa użytkownika**: spersonalizuj swoją nazwę użytkownika
- Automatyczne wypłaty**: aktywuj automatyczne wypłaty do wallet po zamknięciu transakcji
- Uwierzytelnianie dwuskładnikowe**: zwiększone bezpieczeństwo dzięki 2FA
- Dokumentacja**: dostęp do oficjalnych zasobów



## Wycieczka Interface



Interfejs LN Markets jest podzielony na kilka sekcji dostępnych z menu bocznego:



### Pulpit nawigacyjny



![Dashboard](assets/fr/06.webp)



Wyświetla Twoje wyniki według typu produktu (Futures Cross, Futures Isolated, Options) z P&L, wolumenami transakcji i osobistym Address Lightning (np. `pivi@lnmarkets.com`).



### Profil



![Profil trader](assets/fr/07.webp)



Szczegółowe statystyki: liczba transakcji, typ inwestora (SCALPER itp.), mediana czasu trwania pozycji, podział Long/Short, współczynnik wygranych, średnie (ilość, depozyt zabezpieczający, dźwignia) i progresywna struktura opłat w zależności od wolumenu.



### Handel



![Historique des trades](assets/fr/08.webp)



Zakładka "Transakcje" wyświetla pełną historię pozycji, ze wszystkimi ważnymi wskaźnikami: datą utworzenia, kierunkiem (długa/krótka), wielkością pozycji (ilością), zaangażowanym depozytem zabezpieczającym, ceną wejścia i wyjścia, zrealizowanym zyskiem/stratą (P&L) i opłatami transakcyjnymi. Możesz filtrować według typu produktu (kontrakty terminowe/opcje) i eksportować dane do zewnętrznej analizy lub księgowości.



### Ustawienia



![Paramètres de la plateforme](assets/fr/05.webp)



Zakładka Ustawienia oferuje dwie zakładki: **Konto** i **Interface**.



*zakładka *Konto**:



Zarządzanie kontem z edytowalnymi polami :




- Nazwa użytkownika**: zmień swoją nazwę użytkownika (np. "pivi") za pomocą przycisku "Aktualizuj"
- E-mail**: dodaj/edytuj swój adres e-mail
- Adres wpłaty bitcoin**: adres bitcoin, którego można użyć do wpłaty środków on-chain.



**Trzy przełączniki konfiguracji** :




- Pojawiaj się w rankingach**: wybierz, czy chcesz pojawiać się w publicznych rankingach
- Użyj adresów Taproot**: użyj adresów Bitcoin Taproot dla wpłat/wypłat on-chain
- Włącz automatyczne wypłaty**: aktywuj automatyczne wypłaty do wallet Lightning po zamknięciu transakcji



**Migracja konta**: Sekcja umożliwiająca migrację konta Lightning do klasycznego uwierzytelniania e-mail/hasło.



**Zarządzanie Session**: przycisk "Wyczyść sesję i dane lokalne" do rozłączania i czyszczenia lokalnych danych przeglądarki.



*zakładka *Interface**:



Dostosuj wrażenia użytkownika za pomocą siedmiu przełączników:




- Pomiń potwierdzenie zlecenia**: dezaktywacja trybu potwierdzenia przed wykonaniem transakcji (szybki handel)
- Pokaż podpowiedzi**: wyświetla podpowiedzi po najechaniu kursorem na elementy
- Tryb prywatny (maskuje wrażliwe dane)**: maskuje kwoty i wrażliwe dane w interfejsie (tryb prywatności)
- Pokaż PL netto w profilu**: pokaż zysk/stratę netto w profilu publicznym
- Użyj ikon jednostek**: wyświetlanie ikon jednostek walutowych (sats, $)
- Włącz powiadomienia dźwiękowe**: aktywuj powiadomienia dźwiękowe dla zdarzeń handlowych
- Włącz powiadomienia na pulpicie**: aktywacja powiadomień na pulpicie systemu operacyjnego



### Wallet



![Wallet](assets/fr/09.webp)



Bitcoin i syntetyczne salda USD z historią wpłat, wypłat, przelewów krzyżowych, swapów, finansowania i zarządzania adresami on chain.



### API



![API V3](assets/fr/10.webp)



LN Markets oferuje kompletny API REST (V2 i V3), aby w pełni zautomatyzować handel za pomocą skryptów lub botów. Możesz tworzyć klucze API z konfigurowalnymi uprawnieniami (tylko do odczytu, handlu, wypłat) bezpośrednio z interfejsu. Oficjalne zestawy SDK TypeScript i Python są dostępne dla łatwej integracji. Pełna dokumentacja API V3 jest dostępna pod adresem [api.lnmarkets.com/v3](https://api.lnmarkets.com/v3).



## Pierwsza wpłata środków



Kliknij przycisk "Wpłata". Dostępne są trzy metody:



![Modal de dépôt](assets/fr/11.webp)



1. **LNURL**: zeskanuj kod QR za pomocą wallet Lightning


2. **Invoice**: wprowadź kwotę, a następnie zeskanuj fakturę Lightning


3. **On-Chain**: zajezdnia Bitcoin on chain



## Handel w praktyce



### Handel kontraktami futures typu long: stawianie na wzrosty



Na pulpicie nawigacyjnym kliknij "Futures", a następnie "Isolated". Kliknij **"Kup "**, aby otworzyć pozycję długą.



![Interface Futures Long](assets/fr/12.webp)



Kliknij ikonę **kalkulatora** obok przycisku "Kup", aby wyświetlić kalkulator pozycji:



![Calculateur de position Long](assets/fr/13.webp)



**Konkretny przykład** :




- Ilość**: 100 USD (wielkość pozycji)
- Marża handlowa**: 12.336 sats (zaangażowana marża)
- Dźwignia**: 7.73× (każda zmiana o 1% BTC = 7,73% od twojego kapitału)
- Cena wejścia** : $104,863.5
- Likwidacja**: 92 852 USD (krytyczna cena automatycznej likwidacji)
- Cena wyjścia**: 110 000 USD (do obliczenia zysku)
- PL** : 4,492 sats (zysk przy wyjściu za $110,000)



**Scenariusze** :




- Wzrost +4,9%** (110 000 USD) : +4 492 sats zysku (+36,4%)
- Neutralny** (104 863 USD): -185 sats (tylko opłaty)
- Spadek o -11,5%** (92 852 USD): całkowita likwidacja (-100%)



Kliknij przycisk "Kup", aby potwierdzić transakcję. **Dwa możliwe przypadki** :





- Jeśli masz wystarczającą płynność** na swoim koncie: modal potwierdzenia jest wyświetlany bezpośrednio (obrazek poniżej). Kliknij "Tak", aby natychmiast zrealizować transakcję.



![Confirmation trade Long](assets/fr/14.webp)





- Jeśli nie masz wystarczającej ilości gotówki**: zamiast tego wyświetlany jest kod QR Lightning. Zeskanuj go za pomocą wallet Lightning, aby zapłacić wymagany depozyt zabezpieczający. Transakcja zostanie otwarta automatycznie po otrzymaniu płatności



### Krótki handel kontraktami futures: obstawianie spadków



Kliknij **"Sprzedaj "**, aby otworzyć krótką pozycję (wygrywasz, jeśli cena spadnie). Otwórz kalkulator za pomocą ikony kalkulatora, aby ustawić swoją pozycję:



![Calculateur de position Short](assets/fr/15.webp)



Kliknij "Sprzedaj", aby potwierdzić. Jeśli chodzi o Long, **dwa możliwe przypadki**:





- Jeśli masz wystarczającą ilość gotówki**: tryb bezpośredniego potwierdzenia, kliknij "Tak"
- Jeśli nie masz wystarczającej ilości gotówki**: wyświetlany jest kod QR Lightning (obrazek poniżej). Zeskanuj go za pomocą wallet Lightning, aby zapłacić wymaganą marżę:



![Paiement Lightning pour Short](assets/fr/16.webp)



Po otrzymaniu płatności Lightning pozycja krótka zostanie otwarta automatycznie. Następnie można nią zarządzać z poziomu interfejsu handlowego.



#### Zamykanie pozycji



Aby zamknąć pozycję (długą lub krótką), kliknij na **mały krzyżyk w prawym dolnym rogu** interfejsu zarządzania:



![Interface de clôture](assets/fr/17.webp)



Wyświetlone zostanie okno dialogowe potwierdzenia zamknięcia transakcji:



![Confirmation clôture](assets/fr/18.webp)



W oknie dialogowym zostanie wyświetlony bieżący rachunek zysków i strat. Kliknij "Tak", aby zamknąć. Saldo jest natychmiast dodawane (zysk) lub odejmowane (strata) od Wallet za pośrednictwem Lightning.



### Opcje handlowe Call: warunkowe prawo do zakupu



Opcje oferują **ryzyko ograniczone** do zapłaconej premii, bez możliwości likwidacji. Call daje ci prawo (nie obowiązek) do zakupu Bitcoin po cenie wykonania przed wygaśnięciem. W przeciwieństwie do kontraktów futures, nigdy nie można stracić więcej niż zainwestowana premia.



Na pulpicie nawigacyjnym kliknij "Opcje", a następnie wybierz zakładkę "Połączenia".



![Interface Options Call](assets/fr/19.webp)



Skonfiguruj transakcję z następującymi parametrami:




- Ilość**: 100 USD (wielkość kontraktu)
- Wygaśnięcie** : 2025-11-15 (data wygaśnięcia)
- Strike**: $96,000 (cena docelowa)



Pozostałe pola są obliczane automatycznie:




- Marża**: 1.045 sats (premia do zapłaty, Twoja inwestycja)
- Breakeven**: $96,923 (cena za odzyskanie stawki)
- Delta**: 40 (wrażliwość na cenę Bitcoin)



**Jak obliczyć swoją wygraną?



Twój zysk zależy od ceny Bitcoin w momencie wygaśnięcia. Wzór: **(cena BTC - Strike) × wielkość Contract - zapłacona premia**.



**Konkretne przykłady** :





- Bitcoin po $96,000** (obecna cena): Wartość wewnętrzna = 0 USD **Strata: -1.045 sats** (tracisz premię)





- Bitcoin po cenie $97,000**: Wartość wewnętrzna = (97 000 - 96 000) × 0,00105 BTC = 1,05 USD. Przeliczone na sats ≈ 2,175 sats. ** Zysk: 2,175 - 1,045 = +1,130 sats** (+108% zysku)





- Bitcoin po cenie $98,000**: wartość wewnętrzna = $2,000 ≈ 3,224 sats. **Zysk: +2 179 sats** (+208% zysku)





- Bitcoin za 100.000 USD**: wartość wewnętrzna = 4.000 USD ≈ 5.263 sats. **Zysk: +4 218 sats** (+403% zysku)





- Bitcoin poniżej $96,000**: Opcja wygasa bezwartościowo. **Ograniczona strata: -1,045 sats**, brak możliwości likwidacji



Kliknij na "Kup Call". Pojawi się okno dialogowe potwierdzenia:



![Confirmation Call option](assets/fr/20.webp)



Kliknij ponownie "Buy Call", aby potwierdzić. Opcja pojawi się w zakładce "Running Options". W momencie wygaśnięcia LN Markets automatycznie oblicza wartość wewnętrzną i dostosowuje zysk/stratę.



**Uwaga dotycząca opcji sprzedaży**: Operacja jest identyczna jak w przypadku opcji kupna, ale w odwrotnej kolejności. W przypadku opcji sprzedaży stawiasz na **spadek** ceny Bitcoin. Jeśli Bitcoin spadnie poniżej twojego strike, wygrywasz; jeśli pozostanie powyżej, tracisz tylko zapłaconą premię. Obliczanie zysków odbywa się zgodnie z tą samą logiką: **(strike - cena BTC) × wielkość Contract - zapłacona premia**.



### Błyskawiczna wypłata środków



Kliknij "Wypłać":



![Modal de retrait](assets/fr/21.webp)



**Metody** : LNURL, Invoice, Lightning Address, On-Chain.



**Procedura Invoice** :


1. Generowanie faktury Lightning z urządzenia wallet


2. Skopiuj fakturę (zaczyna się od `lnbc...`)


3. Wklej go do pola LN Markets


4. Potwierdzenie wycofania


5. Twój wallet zostanie uznany w ciągu 1-3 sekund



Brak opłat za wypłaty Lightning, tylko minimalne koszty routingu (<0,1% w praktyce).



## Ryzyko i najlepsze praktyki



**Główne zagrożenia** :




- Całkowita likwidacja**: wysoka dźwignia finansowa może zlikwidować 100% depozytu zabezpieczającego w ciągu kilku minut
- Usługa eksperymentalna**: faza alfa, niepewność technologiczna
- Ryzyko kontrahenta**: platforma pozostaje pojedynczym kontrahentem



**Najlepsze praktyki** :



1. **Zarządzanie kapitałem**: przyjmij strategię zarządzania ryzykiem dostosowaną do Twojego profilu. Na przykład: przeznacz 5% swoich całkowitych aktywów na transakcje lewarowane, a następnie ryzykuj maksymalnie 1% tego kapitału na transakcję (np.: aktywa 1 BTC → 5 mln sats na transakcję → 50 tys. sats maksymalnego ryzyka na pozycję)



2. **Systematyczny stop-loss**: skonfiguruj stop-loss, aby ograniczyć straty na transakcję. Na przykład przy regule 1% ryzyka, nawet 10 kolejnych stratnych transakcji stanowi tylko 10% kapitału handlowego



3. **Zacznij od małych kwot**: przetestuj najpierw kilka tysięcy sesji, aby zrozumieć mechanizmy przed zastosowaniem strategii zarządzania kapitałem



4. **Regularnie wypłacaj swoje zyski**: zabezpiecz swoje zyski na głównym wallet, pozostawiając na platformie tylko aktywny kapitał handlowy



5. **Uważaj na dźwignię finansową**: unikaj dźwigni finansowej >20×, chyba że jesteś w pełni świadomy ryzyka likwidacji



**Koszty**: brak opłat za wpłaty/wypłaty Lightning, spread ~0,1% na transakcję (spada do 0,06% w zależności od wolumenu).



## Zalety i ograniczenia



**Zalety** :




- Bez nadzoru (całkowita kontrola z wyłączeniem okresów handlowych)
- Bez KYC (anonimowość dzięki Lightning/Nostr)
- Natychmiastowe rozliczenia (wpłaty/wypłaty w kilka sekund)
- Realizacja bez poślizgu z agregacją płynności
- Wsparcie publiczne API i Nostr



**Ograniczenia** :




- Usługa alfa (możliwe zmiany)
- Niższa płynność niż w przypadku Binance/Deribit
- Zabronione dla mieszkańców USA



## Wnioski



LN Markets ucieleśnia główną ewolucję handlu Bitcoin poprzez natywną integrację Lightning Network, aby przywrócić kontrolę użytkownikom. Dla doświadczonych bitcoinerów, którzy chcą spekulować bez narażania swojej suwerenności, jest to wyjątkowa alternatywa dla tradycyjnych scentralizowanych giełd.



Platforma nadal ewoluuje dzięki liniowym kontraktom futures USDT i handlowi bez nadzoru za pośrednictwem Discreet Log Contracts (DLC) w fazie rozwoju. Stosując dobre praktyki zarządzania ryzykiem (małe kwoty, stop-loss, regularne wypłaty), LN Markets staje się potężnym narzędziem do odpowiedzialnego korzystania z dźwigni Bitcoin.



Zacznij od małych kwot, przetestuj kilka tysięcy sesji i stopniowo odkrywaj tę nową granicę Lightning Network. Szczęśliwego suwerennego handlu ⚡️!



## Zasoby





- [Oficjalna strona LN Markets](https://lnmarkets.com)
- [Dokumentacja](https://docs.lnmarkets.com)