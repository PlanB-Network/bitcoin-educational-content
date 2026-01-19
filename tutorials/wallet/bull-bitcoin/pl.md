---
name: Bull Bitcoin Wallet
description: Dowiedz się, jak korzystać z Wallet Bull Bitcoin
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=6b0xTB2sE8E)


*Ten samouczek wideo od BTC Sessions przeprowadzi Cię przez proces konfiguracji i korzystania z Bull Bitcoin Wallet!*


W tym przewodniku opisano instalację, konfigurację i korzystanie z Bull Bitcoin Wallet. Dowiesz się, jak wysyłać i odbierać środki w sieciach Bitcoin, On-Chain, Liquid i Lightning, a także jak przenosić Bitcoin między nimi. Rozbudowane funkcje wallet sprawiają, że jest to potężne, wszechstronne narzędzie do zarządzania Bitcoin. Zacznijmy.


## Wprowadzenie


Bull Bitcoin Wallet, opracowany przez [Bull Bitcoin](https://www.bullbitcoin.com/), jest **samodzielnym** Bitcoin wallet, co oznacza, że masz pełną kontrolę nad swoimi kluczami prywatnymi, a tym samym środkami, bez zależności od strony trzeciej. Ten Wallet o otwartym kodzie źródłowym i zakorzeniony w filozofii Cypherpunk łączy w sobie prostotę, poufność i zaawansowane funkcje, takie jak swapy międzysieciowe i obsługa PayJoin. Pozwala zarządzać bitcoinami w trzech sieciach: **Bitcoin onchain**, **Liquid** i **Lightning**, z których każda dostosowana jest do konkretnych zastosowań. Na stronie [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49) można sprawdzić bieżące tematy i nadchodzące zmiany. Ponieważ projekt jest w 100% open-source i "budowany publicznie", możesz również przesyłać swoje sugestie i wszelkie napotkane błędy. Podczas gdy niektóre portfele obsługują obecnie wiele sieci, Bull Bitcoin Wallet wyróżnia się głęboką integracją funkcji prywatności we wszystkich z nich, co czyni go potężnym narzędziem do zarządzania Bitcoin we wszystkich głównych sieciach


## 1️⃣ Wymagania wstępne


Przed rozpoczęciem korzystania z **Bull Bitcoin Wallet** upewnij się, że posiadasz następujące elementy:



- Kompatybilny smartfon**: Urządzenie z systemem **iOS** (iPhone lub iPad) lub **Android**
- Połączenie z Internetem
- Zabezpiecz nośnik kopii zapasowej**: Zapisz swoją **frazę odzyskiwania** (12 słów) na papierze lub metalu i przechowuj ją w bezpiecznym miejscu.
- Podstawowa wiedza**: Przydatne jest minimalne zrozumienie koncepcji Bitcoin (adresy, transakcje, opłaty), chociaż ten samouczek wyjaśnia każdy krok dla początkujących.


## 2️⃣ Instalacja


Aplikację można zainstalować poprzez:



- [Apple App Store](https://apps.apple.com/app/bull-bitcoin/id6743380972)[ ](https://apps.apple.com/us/app/bitchat-mesh/id6748219622)(dla urządzeń z systemem iOS)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&hl=en) (dla urządzeń z systemem Android)


Użytkownicy Androida mają również alternatywne opcje:



- Pobierz APK bezpośrednio ze strony [GitHub Releases](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) lub
- Instalacja przez kompatybilny z Nostr [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqtxxmmd9e382mrvvf5hgcm0d9hzumt0vf5kcegnah0ap)


Po zainstalowaniu aplikacji postępuj zgodnie z instrukcjami na ekranie powitalnym, aby skonfigurować swoje konto.


## 3️⃣ Konfiguracja początkowa


Po otwarciu wyświetlony zostanie monit z następującymi opcjami:



- `Twórz nowy Wallet`
- `Odzyskaj Wallet` i
- `Opcje zaawansowane`


Zacznijmy od dotknięcia `Opcji zaawansowanych`.


Tutaj możemy skonfigurować zaawansowane ustawienia przed utworzeniem lub odzyskaniem wallet:


1. Włącz `Tor proxy`, aby kierować ruch przez sieć Tor.

1. [Aplikacja Orbot](https://orbot.app/en/) musi być zainstalowana i uruchomiona przed włączeniem

2. Tor Proxy dotyczy tylko Bitcoin (nie Liquid) i może skutkować wolniejszym połączeniem.

2. Skonfiguruj `Custom Electrum Server` lub

3. Dostosuj ustawienia `Recover Bull`. Więcej informacji na temat funkcji [Recover Bull](https://recoverbull.com/) podamy później.


Po dokonaniu wszystkich opcjonalnych ustawień, dotknij `Done`. Jeśli chcesz ponownie użyć istniejącego Wallet, kliknij `Recover Wallet` i wpisz 12 słów frazy odzyskiwania.


W przeciwnym razie kliknij `Utwórz nowy Wallet`.


![image](assets/en/01.webp)


## 4️⃣ Ekran główny


Zanim zanurzymy się głębiej, spójrzmy na "Ekran główny", aby się zorientować:



- "Przegląd transakcji" i "Menu ustawień" znajdują się na górze.
- Opcja "Dostępne saldo" posiada opcję prywatności, którą można włączyć lub wyłączyć.
- Uzyskaj dostęp do `Bitcoin Bull Exchange`, aby `Kupować, Sprzedawać lub Płacić` (zależy to od jurysdykcji i może wymagać KYC).
- `Transfer` środków między portfelami
- `Secure Bitcoin` równa się Onchain Bitcoin Wallet
- `Instant payments` via Lightning- / Liquid Network *(Uwaga: Bull Bitcoin Wallet umożliwia dokonywanie i otrzymywanie płatności za pośrednictwem Lightning. Środki otrzymane za pośrednictwem Lightning są przechowywane w sieci [*Liquid](https://liquid.net/) (w Wallet Instant Payments) dzięki automatycznej wymianie za pośrednictwem [*Boltz exchange](https://boltz.exchange/). Daje to możliwość interakcji z Lightning bez konieczności zarządzania kanałami płynności, pozostając przy tym pod własną opieką)
- `Wysyłanie` i `Odbieranie` funduszy


![image](assets/en/02.webp)


Najpierw dokonajmy kilku ważnych konfiguracji i zacznijmy od `Backup`.


## 5️⃣ Kopia zapasowa


Aby rozpocząć proces tworzenia kopii zapasowej, dotknij ikony koła zębatego (⚙)` w prawym górnym rogu aplikacji i wybierz `Wallet Backup`. Zostaną przedstawione dwie metody zabezpieczenia wallet: `Encrypted Vault` i `Physical Backup`. Przyjrzyjmy się każdej z nich.


![image](assets/en/03.webp)


### Fizyczna kopia zapasowa


Dotknij opcji "Fizyczna kopia zapasowa", aby wyświetlić listę 12 słów reprezentujących frazę odzyskiwania lub seed. Weź pod uwagę następujące kwestie:



- Zapisz swoją "frazę odzyskiwania" z najwyższą starannością. Zapisz ją na papierze lub metalu i przechowuj w bezpiecznym miejscu (skrytka depozytowa, lokalizacja offline). Ta fraza jest jedynym sposobem na uzyskanie dostępu do bitcoinów w przypadku utraty urządzenia lub usunięcia aplikacji.
- Ważne jest również, aby pamiętać, że każdy, kto ma tę frazę, może ukraść wszystkie twoje bitcoiny. Nigdy nie przechowuj ich cyfrowo:
- Brak zrzutu ekranu
- Brak kopii zapasowych w chmurze, poczcie e-mail lub wiadomościach
- Brak funkcji kopiuj/wklej (ryzyko zapisania w schowku)


![image](assets/en/25.webp)


Na następnym ekranie będziesz musiał umieścić słowo we właściwej kolejności, aby upewnić się, że masz poprawną frazę seed. Po pomyślnym zakończeniu testu otrzymasz potwierdzenie.


! **Ten punkt jest krytyczny**. W celu uzyskania dalszej pomocy :


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### Zaszyfrowany skarbiec


Istnieje również opcja zaszyfrowanej, anonimowej kopii zapasowej w chmurze. Ale czy nie wspomnieliśmy w ostatnim akapicie, że kopie zapasowe w chmurze są ryzykowne i należy ich unikać? Zespół Bull Bitcoin opracował jednak sprytny sposób, aby uczynić ten proces bezpiecznym. Oto jak to działa:


`Recoverbull` to protokół kopii zapasowej, który upraszcza zabezpieczenie Bitcoin wallet poprzez podzielenie kopii zapasowej na dwie części. Po pierwsze, plik kopii zapasowej wallet jest szyfrowany na urządzeniu przy użyciu silnego klucza szyfrującego. Ten zaszyfrowany plik można zapisać w dowolnym miejscu, takim jak Dysk Google lub urządzenie. Po drugie, klucz szyfrowania potrzebny do odblokowania pliku jest przechowywany przez Recoverbull Key Server. Aby odzyskać wallet, potrzebujesz zarówno zaszyfrowanego pliku kopii zapasowej, jak i klucza, do którego uzyskujesz dostęp za pomocą kodu PIN lub hasła. Taka konstrukcja zapewnia, że sama kopia zapasowa w chmurze jest bezużyteczna, a sam serwer klucza jest bezużyteczny bez określonego pliku kopii zapasowej. Zapewnia to bezpieczeństwo środków, nawet jeśli jedna z części zostanie naruszona.


Pomyśl o tym jak o skrytce depozytowej. Zaszyfrowany plik kopii zapasowej to *skrytka*, którą można przechowywać w dowolnym miejscu (np. na Dysku Google). Twój kod Recovery PIN to *klucz*, który jest przechowywany oddzielnie przez Recoverbull Key Server. Złodziej musiałby zdobyć zarówno konkretną skrzynkę, jak i konkretny klucz, aby ją otworzyć. Taka konstrukcja zapewnia, że nawet jeśli ktoś zdobędzie plik kopii zapasowej, będzie on bezużyteczny bez klucza z serwera, a klucz serwera będzie bezużyteczny bez unikalnego pliku kopii zapasowej.


Dowiedz się więcej o protokole tworzenia kopii zapasowych wallet `Recoverbull` [tutaj](https://recoverbull.com/).


Stuknij w `Encrypted vault`, a następnie `Continue`, aby potwierdzić użycie domyślnego serwera. Połączenie zostanie przekierowane przez sieć `Tor`, aby zapewnić prywatność i anonimowość.


**Zrozumienie kodów PIN**



- `App Unlock PIN`**:** Opcjonalny kod PIN ustawiony w `Settings > Security PIN` w celu zablokowania aplikacji na telefonie.
- `Recovery PIN`**:** Obowiązkowy kod PIN utworzony podczas procesu tworzenia kopii zapasowej `Encrypted Vault`, używany do odszyfrowania pliku kopii zapasowej podczas odzyskiwania.


Są to dwa oddzielne kody PIN. Nie zapomnij kodu Recovery PIN, ponieważ jest on niezbędny do przywrócenia wallet"


**Konfiguracja kodu PIN odzyskiwania:**



- Aby odzyskać dostęp do wallet, należy utworzyć kod PIN lub hasło.
- Kod PIN/hasło musi składać się z co najmniej 6 cyfr (np. unikaj prostych sekwencji, takich jak 123456, które nie są akceptowane).
- Bez tego kodu PIN odzyskanie wallet jest niemożliwe.


Następnie wybierz dostawcę skarbca:



- `Google Drive` lub
- niestandardowa lokalizacja (np. urządzenie użytkownika)


![image](assets/en/04.webp)


Teraz zapisz `plik kopii zapasowej`. Następnie dotknij `Test Recovery`, wybierz zapisany plik kopii zapasowej lub skarbiec, a następnie dotknij `Decrypt Vault`. Wprowadź swój `PIN` lub `Hasło`. Jeśli wszystko zadziałało, pojawi się ekran `Test zakończony pomyślnie`.


### Etykiety importowe / eksportowe


Po utworzeniu kopii zapasowej przyjrzyjmy się "Etykietom".  Bull Bitcoin wallet zwiększa prywatność i organizację, umożliwiając użytkownikom tworzenie niestandardowych etykiet dla adresów odbiorczych i transakcji. Etykiety te pomagają kategoryzować środki, ponieważ transakcje wysyłane na adres oznaczony etykietą będą dziedziczyć tę etykietę, a także można oznaczać transakcje wychodzące, aby śledzić ich zmiany. wallet w pełni obsługuje standard [BIP-329](https://bip329.org/), co oznacza, że można wyeksportować wszystkie etykiety do pliku i zaimportować je do innego wallet. Dzięki tej funkcji można płynnie tworzyć kopie zapasowe historii transakcji i kategoryzacji lub migrować je między różnymi instancjami wallet bez utraty spersonalizowanej organizacji.


![image](assets/en/05.webp)


## 6️⃣ Ustawienia


Mając zabezpieczoną podstawową kopię zapasową, przyjrzyjmy się innym funkcjom dostępnym w ustawieniach.


### A - Zabezpieczenie dostępu


Aby zabezpieczyć aplikację, przejdź do `Settings` i wybierz `Security PIN`, aby wybrać kod PIN. Utwórz silny kod PIN, aby zablokować dostęp do wallet. Chociaż ten krok jest opcjonalny, jest wysoce zalecany, aby zapobiec nieautoryzowanemu dostępowi, jeśli ktoś inny korzysta z telefonu.


![image](assets/en/06.webp)


### B - Połączenie z węzłem osobistym (opcjonalnie)


Wallet BullBitcoin domyślnie łączy się z serwerami Electrum: pierwszym zarządzanym przez Bull Bitcoin i dodatkowym serwerem od Blockstream, z których oba są uważane za nieprowadzące logów, co zmniejsza ryzyko śledzenia.


Aby zapewnić większą poufność, można podłączyć aplikację do własnego węzła Bitcoin za pośrednictwem serwera Electrum. Aby to zrobić, dotknij `Ustawienia` > `Ustawienia Bitcoin` > `Ustawienia Electrum Server`, a następnie dotknij `+ Dodaj własny serwer`, aby wprowadzić adres i dane uwierzytelniające serwera.


![image](assets/en/07.webp)


### C - Waluta


Dostępne saldo jest wyświetlane na ekranie głównym w `sats` i `USD`. Aby to zmienić, przejdź do `Ustawienia` > `Waluta`. Tam możesz przełączać się między `sats/BTC` i wybrać swoją `domyślną walutę fiat`.


![image](assets/en/08.webp)


### D - Ustawienia Bitcoin


Menu `Ustawienia Bitcoin` oferuje głęboki dostęp do podstawowych konfiguracji i danych wallet. Tutaj możesz sprawdzić podstawowe szczegóły swoich portfeli `Secure Bitcoin` i `Instant payments`, zapewniając pełną przejrzystość i kontrolę. Kluczowe funkcje tego menu obejmują:



- Szczegóły Wallet:** Przejdź do bezpiecznego Bitcoin lub płatności natychmiastowych wallet, aby wyświetlić szczegółowe informacje.
- Odcisk palca Wallet:** Unikalny identyfikator wallet.
- Klucz publiczny (Pubkey):** Klucz używany do generate adresów odbiorczych Bitcoin.
- Descriptor:** Techniczne podsumowanie struktury wallet.
- Ścieżka pochodna:** Określona ścieżka używana do generate wszystkich adresów z głównego klucza prywatnego.
- Widok Address:** Dostęp do listy nieużywanych adresów odbiorczych i zmiana adresów (wkrótce)


Ponadto użytkownik ma możliwość



- włącz ustawienia automatycznego transferu, aby ustawić maksymalne natychmiastowe saldo wallet, które zostanie następnie automatycznie przeniesione do bezpiecznego bitcoina wallet.
- Importuj portfele generyczne za pomocą frazy `Mnemonic` lub importuj `watch-only`
- Podłącz `portfele sprzętowe`: obecnie obsługiwane urządzenia to ColdcardQ, SeedSigner, Specter, Krux, Blockstream Jade i Foundation Passport


## 7️⃣ Bull Bitcoin Exchange


Bezpośrednio z wallet masz dostęp do [giełdy Bull Bitcoin](https://www.bullbitcoin.com/), umożliwiając kupno, sprzedaż i płatność Bitcoin bez opuszczania aplikacji. Ta integracja zapewnia wygodne rozwiązanie do zarządzania potrzebami Bitcoin. Należy pamiętać, że dostęp do giełdy i jej usług może być ograniczony w zależności od jurysdykcji, a ukończenie weryfikacji Know Your Customer (KYC) może być wymagane w celu zachowania zgodności ze standardami regulacyjnymi i korzystania z pełnych funkcji platformy.


Aby rozpocząć, dotknij `Exchange` w prawym dolnym rogu, a następnie `Sign up` lub `Login` do swojego konta.


Giełda oferuje następujące [funkcje](https://www.bullbitcoin.com/):



- Kup Bitcoin z własnym zabezpieczeniem z konta bankowego
- Bez pozbawienia wolności
- Osoby fizyczne lub korporacje
- Natychmiastowa wypłata
- Brak ukrytych opłat
- Lightning Network dostępny
- Brak limitów transakcji
- Opcje zakupów cyklicznych


![image](assets/en/09.webp)


Aby dowiedzieć się więcej, odwiedź ten samouczek:


https://planb.academy/en/tutorials/exchange/centralized/bull-bitcoin-europe-0ccf713e-efcd-44ec-8205-211f49ac7d53

## 8️⃣ Otrzymywanie funduszy


Odbieranie środków za pomocą **Bull Bitcoin Wallet** jest proste i elastyczne, obsługując trzy różne sieci dostosowane do różnych przypadków użycia:



- Sieć `Bitcoin (onchain)` do bezpiecznego, długoterminowego przechowywania danych.
- Sieć `Liquid` dla szybkich, bardziej poufnych transakcji.
- Sieć `Lightning` do natychmiastowych, tanich płatności.


Aplikacja automatycznie wygeneruje odpowiedni adres lub fakturę na podstawie wybranej sieci. Oto jak postępować dla każdej sieci.


### Odbiór przez Onchain (sieć Bitcoin)


Aby odebrać środki on-chain, możesz wybrać `Secure Bitcoin Wallet` z ekranu głównego i dotknąć `Odbierz` lub dotknąć głównego przycisku `Odbierz`, a następnie wybrać `Sieć Bitcoin`.


Dostępne są dwa podstawowe tryby generowania adresu odbioru:


**Tryb domyślny (URI z dodatkowymi parametrami wejściowymi)


Domyślnie wallet generuje [BIP21 URI](https://bips.dev/21/). Jest to znormalizowany format, który zawiera więcej informacji niż zwykły adres, w tym kwotę, osobistą notatkę i parametry PayJoin w celu zwiększenia prywatności. Ten kompleksowy URI jest zakodowany w kodzie QR i udostępniany do kopiowania. Format wygląda następująco: `bitcoin:<adres>?<parametr1>=<wartość1>&<parametr2>=<wartość2>`.



- Dodatkowe parametry wejściowe:**
    - Kwota:** Podaj żądaną kwotę w BTC, sats lub walucie fiducjarnej.
    - Wiadomość:** Dodaj osobistą notatkę, która będzie widoczna dla nadawcy.
    - PayJoin:** Włącz tę opcję, aby poprawić prywatność, łącząc dane wejściowe zarówno od nadawcy, jak i odbiorcy transakcji.


Przykładowy URI:


```
bitcoin:bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54xxxxx?amount=0.0005&message=Tip+for+tutorial&pj=HTTPS%3A%2F%2FPAYJO.IN%2F78UH9WZUP8KKJ%23RK1Q2H30FASCU9WW09DQY2LK0K8P2DPRJ99V72CA78ACQAEL675QYTMQ+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1L0LYV6G
```


*Ważna uwaga: Nie wysyłaj żadnych środków na adresy podane w tym poradniku, wallet zostaną usunięte


![image](assets/en/10.webp)


**Włączona opcja tylko kopiowania lub skanowania Address


Z włączoną opcją `Copy or scan Address only option`, aplikacja generuje prosty adres Bitcoin w formacie SegWit (bech32).


Przykład:


```javascript
bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54x3g56
```


Nawet jeśli wprowadzisz kwotę lub notatkę, nie zostaną one uwzględnione w kodzie QR ani skopiowanym adresie.


![image](assets/en/11.webp)


### Odbiór za pośrednictwem Liquid Network


Płatność można otrzymać na Liquid Network. Na ekranie `Receive` dostępne są te same dwie opcje generowania żądania płatności:


**1. Prosty Address:** Skopiuj standardowy adres `Liquid`. Jest to unikalny identyfikator wallet w sieci Liquid i nie zawiera żadnej konkretnej kwoty ani wiadomości.


Przykład Address:


```javascript
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7xxxxxxx
```


**2. Szczegółowe żądanie płatności (URI):** W przypadku bardziej ustrukturyzowanego żądania można określić kwotę i osobistą notatkę. Informacje te są automatycznie kodowane do udostępnianego URI i odpowiadającego mu kodu QR.



- Kwota:** Możesz ustawić kwotę w Bitcoin (BTC), Satoshis (Sats) lub w walucie fiducjarnej.
- Uwaga:** Dodaj osobistą wiadomość, aby zidentyfikować transakcję.


**Przykładowy URI:**


```javascript
liquidnetwork:lq1qqdhgs7w537nun55a5sdy4gxkd08pclk3d7v4qz36sy4xp0cq6gvl52fcfv7kdgkgzmfycrud0zsygqgyjclycckpasxxxxxx?amount=0.00001&message=Test&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```


Aby sfinalizować transakcję, należy podać nadawcy `adres` lub `URI`. Możesz to zrobić, kopiując go do schowka lub skanując kod QR bezpośrednio z ekranu.


![image](assets/en/12.webp)


### Odbieranie przez Lightning



Bull Bitcoin Wallet umożliwia również wysyłanie i odbieranie płatności za pośrednictwem Lightning Network. Kluczową cechą jest to, że środki otrzymane za pośrednictwem Lightning są automatycznie zamieniane i przechowywane na `Liquid Network` w ramach `Instant Payments Wallet`. Usługa ta jest zasilana przez `Boltz`. Taka konstrukcja pozwala cieszyć się szybkością i niskim kosztem Lightning bez złożoności zarządzania kanałami płynności, a wszystko to przy zachowaniu pełnej samokontroli środków. Chociaż to hybrydowe podejście jest samoobsługowe i pozwala uniknąć złożoności zarządzania kanałami, wprowadza usługę strony trzeciej (Boltz), niewielką opłatę za swap i polega na federacji osób funkcyjnych Liquid Network jako posiadaczy kluczy, co różni się od tradycyjnego, nieobsługowego Lightning wallet, w którym zarządzasz własnymi kanałami. Więcej informacji na temat Liquid i modelu zarządzania można znaleźć tutaj:


https://planb.academy/en/courses/e17ee350-41d4-49fa-b270-29e4d26d22f8/overview-of-liquid-architecture-and-governance-model-17650c4b-cd1f-4bc6-b490-708f92dc9306


- Limity:**
    - Minimalna kwota:** Wymagana jest minimalna kwota faktury. Sprawdź aktualny limit w aplikacji
    - Opłaty:** Ty, odbiorca, jesteś odpowiedzialny za niewielką opłatę za wymianę. Opłata ta jest odliczana od kwoty przelewu nadawcy i może ulec zmianie
- Korzyści:**
    - Samodzielna kontrola:** Twoje środki są zawsze pod Twoją kontrolą, zabezpieczone w sieci Liquid.
    - Unikanie wysokich opłat On-Chain:** Korzystając z Lightning i przechowując środki na Liquid, omijasz opłaty on-chain związane z otwarciem tradycyjnego kanału Lightning. Możesz zdecydować się na przeniesienie środków do kanału on-chain później, gdy zgromadzona kwota uzasadni wydatek.
    - Wskazówka:** Aby uzyskać najbardziej opłacalną transakcję między dwoma użytkownikami Bull Bitcoin, skorzystaj bezpośrednio z **sieci Liquid**, aby całkowicie uniknąć opłat za wymianę Lightning.


Aby otrzymać płatność, należy wystawić fakturę generate:


1. `Enter an Amount`**:** Określ kwotę, którą chcesz otrzymać w Bitcoin (BTC), Satoshis (Sats) lub w walucie fiducjarnej.

2. `Add a Note` **(Opcjonalnie):** Dołącz notatkę. Zostanie ona umieszczona na fakturze i wyświetlona w historii transakcji po zakończeniu płatności, co ułatwi jej identyfikację.

3. `Invoice Ważność`**:** Faktura Lightning jest wrażliwa na czas i wygasa po **12 godzinach**. Jeśli nie zostanie opłacona w tym czasie, stanie się nieważna i konieczne będzie wystawienie nowej faktury generate.


Przekaż nadawcy fakturę, kopiując ją do schowka lub pozwalając mu zeskanować kod QR wyświetlany na ekranie.


![image](assets/en/13.webp)


## 9️⃣ Wysyłanie środków


Dostęp do ekranu wysyłania można uzyskać bezpośrednio ze strony głównej lub z dowolnego portfela. Bull Bitcoin Wallet upraszcza proces, automatycznie wykrywając sieć docelową - `Bitcoin`, `Liquid` lub `Lightning` - na podstawie wprowadzonego adresu lub faktury, wklejonej lub zeskanowanej za pomocą kodu QR.


### Transmisja On-Chain przez sieć Bitcoin


Wysyłanie środków on-chain oznacza, że transakcja jest rejestrowana bezpośrednio w łańcuchu bloków Bitcoin. Ta metoda jest najlepsza w przypadku większych przelewów lub przelewów niewrażliwych na czas. Aby rozpocząć, możesz dotknąć przycisku "Wyślij" po prawej stronie i zeskanować lub wprowadzić "standardowy adres Bitcoin".


Jeśli podany adres nie zawiera określonej kwoty, zostaniesz poproszony o podanie szczegółów na ekranie wysyłania. Możesz określić kwotę w preferowanej jednostce, takiej jak BTC, satoshis lub ekwiwalent fiat. Masz również możliwość dodania osobistej notatki, która jest prywatną notatką dla własnego odniesienia, aby pomóc Ci później zidentyfikować transakcję. Notatka ta nie jest udostępniana odbiorcy.


I odwrotnie, jeśli wniosek o płatność, który zeskanujesz lub wkleisz, zawiera już wszystkie niezbędne szczegóły, takie jak BIP21 URI z predefiniowaną kwotą, wallet ominie ekran wprowadzania danych i przeniesie Cię bezpośrednio do ekranu potwierdzenia w celu autoryzacji płatności.


![image](assets/en/14.webp)


Przed wysłaniem transakcji zostanie wyświetlony ekran potwierdzenia. Ważne jest, aby poświęcić chwilę i dokładnie przejrzeć każdy parametr, zwracając szczególną uwagę na adres odbiorcy, wysyłaną kwotę i opłaty sieciowe. Ekran ten zapewnia również zaawansowane narzędzia do dostosowywania transakcji.


Opłaty można kontrolować na dwa podstawowe sposoby. Pierwsza metoda polega na wybraniu żądanej szybkości transakcji, takiej jak niska, średnia lub wysoka, a wallet automatycznie obliczy odpowiednią opłatę. Druga metoda pozwala na bardziej precyzyjną kontrolę, umożliwiając ustawienie określonej opłaty, jako bezwzględnej sumy w satoshis lub jako względnej stawki za bajt, która następnie zapewnia szacowany czas potwierdzenia.


Dla zaawansowanych użytkowników wallet oferuje kilka ustawień umożliwiających precyzyjne dostrojenie transakcji. opcja `Replace-by-Fee` (RBF) jest domyślnie włączona, co jest cenną funkcją, która pozwala przyspieszyć transakcję, jeśli utknie ona w mempool, poprzez ponowne nadanie jej z wyższą opłatą. Można również ręcznie wybrać, z których "Wyjść niewydanych transakcji" (UTXO) mają być wydawane środki. Jest to potężne narzędzie do konsolidacji UTXO, strategii polegającej na łączeniu wielu małych wejść w jedno większe. Chociaż może to kosztować więcej opłat za bieżącą transakcję, może znacznie obniżyć opłaty za przyszłe transakcje, zwłaszcza jeśli oczekuje się wzrostu opłat sieciowych.


![image](assets/en/15.webp)


Usługa PayJoin jest uruchamiana automatycznie po zeskanowaniu żądania płatności odbiorcy (BIP21 URI), które zawiera parametr `pj=`. Jeśli po prostu wkleisz zwykły adres bez dodatkowych parametrów, funkcja ta nie zostanie aktywowana. Ta metoda współpracy zwiększa prywatność, łącząc dane wejściowe zarówno od nadawcy, jak i odbiorcy, przełamując heurystykę wspólnego posiadania danych wejściowych i umożliwiając lepsze skalowanie i oszczędność opłat w niektórych okolicznościach.


### Wysyłanie do Liquid Network


Liquid Network jest przeznaczony do szybkich, poufnych transakcji z minimalnymi opłatami. Gdy wysyłasz środki za pośrednictwem Liquid, są one wypłacane z twojego `Instant Payments Wallet`. Proces jest prosty: wystarczy wprowadzić lub zeskanować adres odbiorcy `Liquid`.


Jeśli adres nie określa kwoty, zostaniesz poproszony o jej podanie na ekranie wysyłania. Kwotę można wprowadzić w BTC, satoshis lub fiat. Kluczową zaletą Liquid jest niski próg minimalny. Podobnie jak w przypadku transakcji on-chain, możesz dodać opcjonalną notatkę osobistą do własnych zapisów. Jeśli żądanie płatności zawiera już kwotę, wallet przejdzie bezpośrednio do ekranu potwierdzenia.


Na ekranie potwierdzenia transakcji Liquid można przejrzeć szczegóły. Opłaty są wyjątkowo niskie i są obliczane na podstawie złożoności transakcji. Zazwyczaj wynoszą one około 0,1 sat/vB, co w przypadku prostej transakcji wynosi zaledwie 20-40 satoshis (na przykład 26 satoshis na dzień 21 grudnia 2025 r.).


![image](assets/en/16.webp)


### Wysyłanie do Lightning Network


Można zeskanować wiadomość Lightning Address (np. `runningbitcoin@rizful.com`), która umożliwia ustawienie kwoty i opcjonalnej notatki dla odbiorcy, lub zeskanować fakturę ze wstępnie zdefiniowaną kwotą, co spowoduje bezpośrednie przejście do ekranu potwierdzenia.


*Należy pamiętać, że obowiązują minimalne kwoty i opłaty*


Bull Bitcoin Wallet wysyła płatności Lightning, pobierając środki z twojego `Instant Payments Wallet` (na Liquid) i zamieniając je przez `Boltz`. To hybrydowe podejście jest w pełni samoobsługowe i pozwala uniknąć wysokich opłat on-chain za zarządzanie dedykowanym kanałem Lightning, ale wymaga uiszczenia "opłaty za zamianę". Aby uzyskać najniższy koszt, wysyłaj bezpośrednio na adres Liquid odbiorcy, jeśli korzysta on również z Bull Bitcoin wallet.


## 🔟 Przesyłanie środków między portfelami


Bull Bitcoin umożliwia przenoszenie Bitcoin między `Bezpiecznym Bitcoin` wallet i `Instant Payments Wallet` na Liquid Network lub do `zewnętrznego Wallet`. Aby wykonać transfer, wystarczy przejść do sekcji `Transfer`, wybrać portfel źródłowy i docelowy, wprowadzić kwotę, którą chcesz przenieść, i potwierdzić transakcję.


![image](assets/en/17.webp)


## 1️⃣1️⃣ Odzyskiwanie Bull Bitcoin Wallet


W tej sekcji wyjaśniono, jak odzyskać dostęp do środków Bull Bitcoin Wallet w przypadku utraty urządzenia, odinstalowania aplikacji lub po prostu konieczności zmiany urządzenia na nowe. Jak już wyjaśniono, istnieją dwie podstawowe metody odzyskiwania: przy użyciu unikalnej metody `Recoverbull` i przy użyciu standardowej frazy `BIP39 seed`.


### Metoda 1: Recoverbull


Podsumowanie: Kopie zapasowe Wallet są szyfrowane lokalnie. Zaszyfrowany plik może być przechowywany w chmurze lub na innym urządzeniu. Klucz szyfrowania jest przechowywany przez Recoverbull Key Server. Oba są przechowywane oddzielnie i muszą być połączone w celu odzyskania wallet.


Na początek usunę Wallet ze wszystkimi środkami i ponownie zainstaluję wallet. Ponownie wylądujemy na ekranie powitalnym. Tym razem wybieramy opcję `Odzyskaj Wallet`. Następnie przejdź do metody `Encrypted Vault`, potwierdź użycie `Default Key server` i wybierz lokalizację lub `Vault provider`, gdzie przechowywałeś plik kopii zapasowej.


![image](assets/en/18.webp)


Stwierdzi, że skarbiec został pomyślnie zaimportowany. Naciśnij przycisk `Decrypt Vault` i wprowadź `PIN`. Następny ekran pokaże "salda" i "liczbę transakcji", które zostały odzyskane.


![image](assets/en/19.webp)


### Metoda 2: Fraza zalążkowa


Ta metoda wykorzystuje główną frazę odzyskiwania wallet, standardową listę 12 słów, która służy jako ostateczna kopia zapasowa środków. Jest to najbardziej uniwersalny sposób odzyskiwania Bitcoin wallet, ponieważ nie jest powiązany z żadną konkretną usługą ani serwerem. Tak długo, jak masz tę frazę, możesz przywrócić wallet na dowolnym kompatybilnym urządzeniu, nawet bez dostępu do serwera kluczy Bull Bitcoin.


Na ekranie powitalnym wybierz `Odzyskaj Wallet`. Tym razem wybierz metodę `Fizyczna kopia zapasowa`. Aplikacja wyświetli siatkę słów. Ostrożnie wybierz każde słowo z 12-wyrazowej frazy seed we właściwej kolejności. Bądź skrupulatny, ponieważ pojedynczy błąd spowoduje nieprawidłowy wallet.


## 1️⃣2️⃣ Podłączanie Hardware Wallet


Aby zapewnić najwyższy poziom bezpieczeństwa, wielu użytkowników Bitcoin decyduje się na przechowywanie swoich środków w "zimnym magazynie". Oznacza to przechowywanie "kluczy prywatnych" kontrolujących Bitcoin na urządzeniu, które nigdy nie jest podłączone do Internetu. "Sprzętowy wallet" (lub urządzenie podpisujące) jest wyspecjalizowanym urządzeniem fizycznym zaprojektowanym dokładnie do tego celu. Działa jak cyfrowy skarbiec dla kluczy, zapewniając, że nigdy nie są one narażone na potencjalne zagrożenia związane z komputerem lub smartfonem online.


Podłączając sprzętowy wallet do aplikacji Bull Bitcoin, otrzymujesz to, co najlepsze z obu światów: bezkompromisowe bezpieczeństwo przechowywania kluczy prywatnych w chłodni w połączeniu z zaawansowanymi funkcjami i przyjaznym dla użytkownika interfejsem Bull Bitcoin wallet do przeglądania sald i zarządzania transakcjami. W tym ostatnim rozdziale pokażemy, jak podłączyć sprzętowy wallet, taki jak [Coldcard Q](https://coldcard.com/q), do Bull Bitcoin wallet. Ten samouczek nie obejmuje dogłębnej konfiguracji Coldcard Q; możesz dowiedzieć się o tym tutaj:


https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

### Importowanie Wallet


![image](assets/en/26.webp)


Najpierw z menu głównego karty Coldcard Q wybierz `Export Wallet`, a następnie `Bull Wallet`. Na karcie Coldcard pojawi się kod QR generate.


![image](assets/en/20.webp)


Otwórz Bull Bitcoin Wallet i przejdź do `Ustawienia` > `Ustawienia Bitcoin` > `Importuj wallet` i wybierz `Karta Q` na telefonie i dotknij `Otwórz kamerę`, aby zeskanować ten kod QR w celu zaimportowania kluczy publicznych wallet.


![image](assets/en/21.webp)


### Odbieranie za pomocą Coldcard Q


Aby odbierać Bitcoin za pomocą podłączonej karty Coldcard Q, urządzenie nie musi być fizycznie podłączone do telefonu. Urządzenie Bull Bitcoin Wallet zaimportowało już niezbędne klucze publiczne, umożliwiając samodzielne nadawanie adresów generate.


1. Stuknij zaimportowane urządzenie podpisujące Coldcard Q i wybierz `Odbierz`.

2. Aplikacja automatycznie wyświetli nowy adres Bitcoin z karty Coldcard wallet.

3. Użyj tego adresu, aby otrzymać środki. Bitcoin zostanie zabezpieczony bezpośrednio kluczami sprzętowymi wallet, nawet jeśli urządzenie było w trybie offline podczas tego procesu.


![image](assets/en/22.webp)


### Wysyłanie za pomocą Coldcard Q


Wysłanie Bitcoin z kartą Coldcard Q wymaga fizycznego potwierdzenia w celu autoryzacji każdej transakcji. Podczas gdy aplikacja Bull Wallet jest używana do tworzenia transakcji, ostateczny podpis można złożyć tylko na samym sprzęcie wallet.


Aby rozpocząć, otwórz kartę `Coldcard Q` wallet i dotknij `Wyślij`. Następnie "otwórz kamerę", aby zeskanować kod QR adresu odbiorczego. Po zeskanowaniu wprowadź `kwotę`, którą chcesz wysłać i dostosuj `priorytet opłaty` w razie potrzeby.


Więcej opcji można znaleźć w sekcji Ustawienia zaawansowane. Znajdziesz tam opcję "Zastąp opłatą" (RBF), która jest domyślnie aktywna i pozwala przyspieszyć zablokowaną transakcję. Dostępna jest również opcja `Coin Control`, która pozwala ręcznie wybrać konkretne UTXO, które chcesz wydać.


Po przejrzeniu wszystkich szczegółów stuknij `Pokaż PSBT`, aby przygotować transakcję.


![image](assets/en/23.webp)


Stuknij przycisk `Scan` na karcie Coldcard Q i użyj jej kamery do zeskanowania kodu QR wyświetlanego na telefonie. Na ekranie Coldcard zostaną wyświetlone wszystkie szczegóły transakcji. Dokładnie zweryfikuj kwotę, adres odbiorcy i adres zmiany. Jeśli wszystko się zgadza, naciśnij przycisk `Enter` na karcie Coldcard Q, aby podpisać transakcję. Następnie na ekranie pojawi się kod QR podpisanej transakcji.


![image](assets/en/24.webp)


W Bull wallet stuknij przycisk "Skończyłem", a następnie stuknij przycisk "Kamera", aby zeskanować kod QR "podpisanej transakcji" z karty Coldcard Q. Bull Wallet wyświetli teraz ekran podsumowania podpisanej transakcji. Przejrzyj ją po raz ostatni, a następnie dotknij przycisku `Broadcast` Transaction. Spowoduje to sfinalizowanie procesu poprzez wysłanie transakcji do sieci Bitcoin, a środki będą w drodze.


## wnioski


Zakończyłeś podróż przez Bull Bitcoin Wallet. Aplikacja zapewnia potężne narzędzia prywatności i bezpieczeństwa na wyciągnięcie ręki, dzięki czemu zaawansowane funkcje są łatwe w użyciu. Pomaga zachować prywatność dzięki funkcjom takim jak `PayJoin`, która ukrywa twoje transakcje w łańcuchu bloków, oraz `Integracja Tor`, która maskuje twoją aktywność w sieci przed wścibskimi oczami. Dla tych, którzy chcą mieć najwyższą kontrolę, możesz połączyć się z `własnym osobistym węzłem Bitcoin`, aby przestać polegać na serwerach stron trzecich, i użyć `Hardware wallet`, aby przechowywać swoje klucze prywatne całkowicie offline i bezpiecznie. Dzięki inteligentnym opcjom tworzenia kopii zapasowych i bezproblemowej obsłudze Bitcoin, Liquid i Lightning, Bull Bitcoin Wallet jest mocnym, wszechstronnym wyborem dla każdego, kto poważnie myśli o zachowaniu prywatności, bezpieczeństwa i pełnej kontroli nad swoimi środkami.


## zasoby Bull Wallet


[Github](https://github.com/SatoshiPortal/bullbitcoin-mobile) | [Website ](https://www.bullbitcoin.com/)| [Recoverbull](https://recoverbull.com/)