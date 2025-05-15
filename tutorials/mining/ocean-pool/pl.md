---
name: Ocean Mining

description: Wprowadzenie do Ocean Mining
---

![signup](assets/cover.webp)


**Maj 2024**


Ocean Mining jest nieco unikalnym Mining pool. Tutaj nie są wymagane żadne konta, adresy e-mail ani hasła. Podobnie jak w Bitcoin, wszystko jest przejrzyste, pseudonimowe, a współtwórcy mogą wybierać spośród czterech różnych szablonów bloków.


### System wynagrodzeń


System wynagrodzeń Ocean nazywa się TIDES, "Transparent Index of Distinct Extended Shares". System ten rejestruje pracę wykonaną przez górników, znaną jako "udziały". Pula oblicza procent "udziałów" dla każdego współpracownika, a następnie dodaje ich Bitcoin Address do szablonu bloku puli jako beneficjenta tego procentu Block reward.


Szablon bloku jest aktualizowany mniej więcej co 10 sekund, aby uwzględnić najbardziej lukratywne nowe transakcje i w razie potrzeby zmienić dystrybucję Block reward.


![signup](assets/rem.webp)


Nie ma znaczenia, czy maszyny są podłączone, czy nie w momencie, gdy pula wykopuje nowy blok. Praca już przesłana jest przechowywana dla następnych ośmiu bloków znalezionych przez pulę.


Zachowanie pracy dla ośmiu bloków zamiast resetowania liczników do zera z każdym nowym wydobytym blokiem oznacza, że rekompensata wyniesie 100% dopiero po znalezieniu przez pulę ośmiu bloków po rozpoczęciu wnoszenia wkładu. Oznacza to również, że nadal będziesz otrzymywać wynagrodzenie za osiem bloków, jeśli przestaniesz wnosić swój wkład do puli.


Mechanizm ten wygładza kompensację i zniechęca do "przeskakiwania puli", które polega na regularnym przełączaniu puli w zależności od tego, która z nich najprawdopodobniej znajdzie następny blok.


### Wypłaty


Działanie Ocean Mining pozwala jego uczestnikom na odzyskiwanie "czystych" bitcoinów, czyli bitcoinów, które zostały bezpośrednio wyemitowane przez Block reward.


W przeciwieństwie do większości innych pul, Ocean nie otrzymuje nowo wydobytych bitcoinów; adresy współpracowników są bezpośrednio zintegrowane z szablonem bloku.


Na chwilę obecną minimalna kwota, aby naprawdę skorzystać z czystych bitcoinów, wynosi 1 048 576 Sats. Z każdym blokiem wydobytym przez pulę, twój "udział" musi uprawniać cię do więcej niż 1,048,576 Sats, aby zostały one bezpośrednio wypłacone przez Block reward.

W przeciwnym razie Sats będą przechowywane przez Ocean do momentu, gdy łączna wartość nagród przekroczy tę kwotę.


Wszystkie bitcoiny tymczasowo przechowywane przez Ocean znajdują się na tym Address: [37dvwZZoT3D7RXpTCpN2yKzMNs2i2Fd1n, wszystko jest weryfikowalne na TimeChain](https://Mempool.space/Address/37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n)

Możliwe jest również wypłacenie Sats za pośrednictwem Lightning przy użyciu BOLT12. Zobaczymy, jak to skonfigurować.


### Opłaty za korzystanie z basenu


Opłaty wahają się od 0% do 2% w zależności od wybranego szablonu bloku.


## Przejrzystość oceanu


### Dane dostawcy


![signup](assets/1.webp)


Wszystkie informacje o puli są przejrzyste, w tym wszystkie dane użytkownika. Aby zrozumieć ten punkt, weźmy przykład:


[Na pulpicie nawigacyjnym Ocean](https://ocean.xyz/dashboard) znajdują się liczne informacje, takie jak Hashrate w ciągu ostatnich sześciu miesięcy, liczba uczestników w puli, całkowita liczba wydobytych bitcoinów itp.


Skupimy się na sekcji "Współtwórcy". Możesz zobaczyć listę wszystkich współtwórców z ich średnim Hashrate w ciągu ostatnich trzech godzin, a także procent **"udziałów "** i **"Hash"** w stosunku do reszty puli.


**"Shares %"** to procent pracy dostarczonej przez autora w oknie ostatnich ośmiu bloków w porównaniu do reszty puli.


**"Hash%"** to wartość procentowa średniego Hashrate dostarczonego przez dostawcę w ciągu ostatnich trzech godzin w porównaniu z resztą puli.


![signup](assets/2.webp)


Zauważysz, że "Współtwórcy" są identyfikowani przez Bitcoin Address. Możesz kliknąć dowolny z tych adresów, aby uzyskać więcej szczegółów.


Jeśli weźmiemy pierwszy z nich, ten z najwyższym Hashrate [1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ](https://ocean.xyz/stats/1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ), można zobaczyć wszystkie szczegóły dotyczące tego użytkownika: Hashrate, liczbę wydobytych bitcoinów, z którym blokiem, a nawet szczegóły każdej z jego maszyn (ASIC). Pozostają oni jednak anonimowi, podobnie jak w przypadku Bitcoin.


### Szablon bloku


W lewym górnym rogu pulpitu nawigacyjnego znajduje się opcja "Następny blok". Na tej stronie znajdują się cztery różne szablony bloków. Ocean pozwala każdemu współpracownikowi wybrać szablon bloku, który chce wspierać. Nie ma to bezpośredniego wpływu na wynagrodzenie. Gdy pula wydobywa blok, wszyscy współautorzy otrzymują wynagrodzenie niezależnie od wybranego szablonu. Pozwala to każdemu "zagłosować" na szablon bloku, który mu odpowiada.


![signup](assets/3.webp)


**CORE:** Opłata 2%, jest to klasyczny szablon Bitcoin Core bez filtra, jak napisano na ich stronie "Obejmuje transakcje i większość spamu"


**CORE+ANTISPAM:** Opłata 0%, Bitcoin Core z filtrem przeciwko niektórym transakcjom, takim jak Ordinals "Obejmuje transakcje i ogranicza spam"


**OCEAN:** Opłata 0%, węzeł Bitcoin "Obejmuje tylko transakcje i stosunkowo małe dane"


**DANE-FREE:** Opłata 0%, Bitcoin Knot "Obejmuje tylko transakcje bez żadnych arbitralnych danych"


### Rozróżnienie między Bitcoin Core i Bitcoin Knot

Bitcoin Core to oprogramowanie, które umożliwia działanie około 99% węzłów Bitcoin na całym świecie. Bitcoin jest protokołem, co oznacza, że podobnie jak w Internecie, gdzie istnieje wiele przeglądarek, może istnieć kilka różnych programów współistniejących w tym samym TimeChain. Jednak w trosce o kompatybilność i ograniczenie ryzyka błędów, które pozostawiłyby niezatarte ślady na TimeChain, prawie wszyscy programiści Bitcoin pracują na Bitcoin Core. Bitcoin Knots jest Fork Bitcoin Core, co oznacza, że współdzieli większość ich kodu, znacznie ograniczając ryzyko błędów. Ten Fork został stworzony przez Luke'a Dashjra, który chciał zastosować bardziej restrykcyjne zasady niż Bitcoin Core bez tworzenia Hard Fork. Obecnie Bitcoin Core i Bitcoin Knots współistnieją dzięki konsensusowi Nakamoto.


## Dodawanie pracownika


Aby dodać pracownika, zacznij od wybrania szablonu bloku. Wybór ten określi adres URL puli, który należy wprowadzić w Miner (ASIC).



- CORE**: `stratum+tcp://core.mine.ocean.xyz:3202`
- CORE+ANTISPAM**: `stratum+tcp://ordis.mine.ocean.xyz:3303`
- OCEAN**: `stratum+tcp://mine.ocean.xyz:3334`
- DATA-FREE**: `stratum+tcp://datafree.mine.ocean.xyz:3404`


Następnie w polu użytkownika wprowadź posiadany Bitcoin Address. Oto lista kompatybilnych typów Address:


- P2PKH** (Oryginalny typ Address. Zaczyna się od "1")
- P2SH** (Wielopodpis lub P2SH-SegWit. Zaczyna się od "3")
- Bech32** (SegWit. Zaczyna się od "bc")
- Bech32m** (Taproot. Zaczyna się od "bc". Dłuższy niż Bech32)


Jeśli masz wielu górników, możesz wprowadzić ten sam Address dla wszystkich z nich, aby ich stawki Hash zostały połączone i wyświetlane jako pojedynczy Miner. Można je również rozróżnić, dodając odrębną nazwę dla każdego z nich. Aby to zrobić, wystarczy dodać ".workername" po Bitcoin Address.


Wreszcie, dla pola hasła użyj `x`.


**Przykład:**

Jeśli wybierzesz szablon **OCEAN**, twój Bitcoin Address to `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv` i chcesz nazwać swój Miner "Brrrr", musisz wprowadzić następujące informacje w Miner Interface:



- URL**: `stratum+tcp://mine.ocean.xyz:3334`
- USER**: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr`
- HASŁO**: `x`


Kilka minut po uruchomieniu Mining będziesz mógł zobaczyć swoje dane na stronie Ocean, wyszukując Address.


### Przegląd pulpitu nawigacyjnego


- Udziały w oknie nagród**: Te dane wskazują liczbę udziałów, pracy wysłanej do puli w oknie ostatnich 8 bloków wydobytych przez pulę.
- Szacowane nagrody w systemie Windows**: Szacunkowa liczba Sats, które zarobisz dzięki już wykonanej pracy. Nie uwzględnia to opłat transakcyjnych, a jedynie coinbase, nowe bitcoiny emitowane przez sieć.
- Szacowany zarobek w następnym bloku**: Szacunkowa liczba zarobionych Sats, jeśli blok zostanie wydobyty teraz. Pamiętaj, że jeśli ta wartość jest mniejsza niż 1 048 576 Sats, nie otrzymasz Sats bezpośrednio do swojego Address. Będą one wysyłane do Address Oceanu, dopóki Twoje zarobki nie przekroczą tego progu.


Poniżej znajduje się wykres przedstawiający historię Hashrate do 6 miesięcy.


![signup](assets/4.webp)


W tym miejscu możesz zobaczyć swój średni Hashrate w różnych skalach czasowych, od 60s do 24h, a także historię bloków wydobytych przez pulę, za które zostałeś nagrodzony.


![signup](assets/5.webp)


Istnieje możliwość wyeksportowania pliku CSV tej historii za pomocą przycisku **Pobierz CSV**.


![signup](assets/6.webp)


W poniższej sekcji znajduje się lista wszystkich górników podłączonych do puli z tym Address. Masz oczywiście ich indywidualne Hashrate, ale także liczbę Sats, które indywidualnie otrzymali za swoją pracę.


![signup](assets/7.webp)


Możesz kliknąć na **Nickname** dowolnego Miner. Wyświetlą się wszystkie informacje, które widzieliśmy przed chwilą, ale konkretnie dla tego Miner.


Na dole strony znajdują się dodatkowe informacje, w których można zobaczyć historię płatności za Address, Sats, które zostały wydobyte, ale nie zostały jeszcze opłacone, oraz całkowitą liczbę wydobytych Sats.


![signup](assets/8.webp)


Tutaj możesz zobaczyć, że w polu **Estimated Time Until Minimum Payout** jest napisane Lightning, ponieważ skonfigurowaliśmy ofertę BOLT12.


### Konfiguracja wypłat błyskawicznych


Jak zrozumiałeś, Ocean dąży do maksymalizacji przejrzystości i minimalizacji opieki (przechowywanie Sats w Twoim imieniu).


Dlatego w przypadku wypłat Lightning konieczne jest skorzystanie z ofert **BOLT12**. Jest to nowy sposób dokonywania płatności na Lightning Network, który zaczyna się pojawiać w 2024 roku i pozwala na kilka rzeczy:


- Jest to łącze płatnicze wielokrotnego użytku, umożliwiające automatyczne płatności i, w przeciwieństwie do Lightning Address, BOLT12 nie podlega ograniczeniom.
- Jest to również metoda płatności, która zapewnia dowód dokonania płatności, co nie ma miejsca w przypadku adresów LNURL.
- Co bardzo ważne, można go użyć w połączeniu z podpisem Bitcoin, aby udowodnić, że jesteś zarówno posiadaczem BTC Address, jak i oferty BOLT12.

Na dzień dzisiejszy (maj 2024 r.) istnieje niewiele rozwiązań umożliwiających korzystanie z tej metody. W tym przykładzie użyjemy serwera Start9 z Core Lightning. Gdy inne narzędzia, takie jak na przykład Phoenix Wallet, zintegrują oferty BOLT12, ten samouczek pozostanie aktualny. Upewnij się, że masz otwarte kanały z przychodzącą płynnością, w przeciwnym razie płatności nie będą działać.


Zacznij od przejścia do pulpitu nawigacyjnego na stronie Ocean, wprowadzając swój BTC Address, a następnie kliknij kartę **Konfiguracja**.


![signup](assets/9.webp)


Skopiujemy tutaj tekst **Opis**:

wypłatyOCEAN dla bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`


Teraz przejdź do swojego Interface Core Lightning na serwerze Start9 (lub dowolnego Wallet zdolnego do dostarczenia oferty BOLT12).


![signup](assets/10.webp)


Kliknij przycisk **Odbierz**.


Zaznacz opcję **Oferta**, a następnie wklej skopiowany wcześniej tekst w polu **Opis** i pozostaw pole **Kwota** puste.


![signup](assets/11.webp)


Kliknij na **Oferta generate**.


![signup](assets/12.webp)


Wygenerowałeś stały link do płatności wielokrotnego użytku, który nie wymaga centralnego serwera, jak ma to miejsce w przypadku adresów Lightning. Skopiuj link i wróć do strony Ocean.


W polu **Lightning BOLT12 Offer** wklej link do płatności i pozostaw pole **Block Height** na domyślnej wartości. Kliknij na **generate**.


![signup](assets/13.webp)


Aby Ocean mógł upewnić się, że ten link do płatności rzeczywiście należy do Ciebie bez korzystania z systemu kont, musisz podpisać wiadomość, która właśnie została wygenerowana za pomocą klucza prywatnego odpowiadającego używanemu Bitcoin Address. Istnieje wiele rozwiązań umożliwiających podpisanie wiadomości kluczem prywatnym. W tym samouczku weźmiemy przykład BlueWallet, ale metoda jest taka sama dla wszystkich portfeli.


![signup](assets/14.webp)


Zakładając, że klucz prywatny znajduje się w BlueWallet (to samo można zrobić z Hardware Wallet), kliknij odpowiedni Wallet.


![signup](assets/15.webp)


Następnie wybierz **...** w prawym górnym rogu.


![signup](assets/15bis.webp)


I **podpisz/weryfikuj wiadomość**.


![signup](assets/16.webp)


W tym oknie dostępne są trzy pola: **Address**, **Podpis** i **Wiadomość**.


W polu **Address** wpisz Bitcoin Address. Jeśli wrócimy do naszego przykładu, jest to Address: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`.


Pozostaw pole **Podpis** puste.

Następnie wklej wygenerowaną wiadomość do pola **Message** na stronie Ocean: `{"height":845900,"lightning_bolt12":"lno1pg7y7s69g98zq5rp09hh2arnypnx7u3qvf3nzufjv4jrs7ncwyuxu6n3wdaxu6msxank5wp5dcc8samv89j8qv3jx36kscfjvempvggz84uzkn26vyzq8y2mr2s8fv0j76wesq43dz72kqrk33nl2tk9j45s"}`

Kliknij na **Podpisz**.


Będzie to generate podpis kryptograficzny, który udowodni, że jesteś właścicielem Address `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`, a podpis ten jest unikalny dzięki wiadomości dostarczonej przez Ocean, wygenerowanej z linku płatności BOLT12.


![signup](assets/17.webp)


Skopiuj podpis i wklej go na stronie Ocean, a następnie kliknij **POTWIERDŹ**.


![signup](assets/18.webp)


Powinien zostać wyświetlony komunikat z potwierdzeniem.


![signup](assets/19.webp)


Teraz przejdź do zakładki **Moje statystyki**. Dodatkowe informacje są wyświetlane u góry wraz z linkiem do płatności BOLT12, który wcześniej wygenerowałeś za pomocą Core Lightning na Start9.


![signup](assets/20.webp)