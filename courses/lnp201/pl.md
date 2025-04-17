---
name: Teoretyczne wprowadzenie do Lightning Network
goal: Odkryj Lightning Network z technicznego punktu widzenia
objectives: 

  - Zrozumienie działania kanałów sieciowych.
  - Zapoznaj się z terminami HTLC, LNURL i UTXO.
  - Asymilacja zarządzania płynnością i opłat LNN.
  - Rozpoznanie Lightning Network jako sieci.
  - Zrozumienie teoretycznych zastosowań Lightning Network.

---

# Podróż do drugiego Layer Bitcoin


Zanurz się w sercu Lightning Network, niezbędnego systemu dla przyszłych transakcji Bitcoin. LNP201 to teoretyczny kurs na temat technicznego działania Lightning. Odkrywa podstawy i mechanizmy tej drugiej sieci Layer, zaprojektowanej tak, aby płatności Bitcoin były szybkie, ekonomiczne i skalowalne.


Dzięki sieci kanałów płatności Lightning umożliwia szybkie i bezpieczne transakcje bez konieczności rejestrowania każdego Exchange na Bitcoin Blockchain. W kolejnych rozdziałach dowiesz się, jak działa otwieranie, zarządzanie i zamykanie kanałów, w jaki sposób płatności są bezpiecznie kierowane przez węzły pośredniczące przy jednoczesnym zminimalizowaniu potrzeby zaufania oraz jak zarządzać płynnością. Dowiesz się, czym są transakcje Commitment, HTLC, klucze odwołania, mechanizmy karania, routing cebulowy i faktury.


Niezależnie od tego, czy jesteś początkującym, czy bardziej doświadczonym użytkownikiem Bitcoin, ten kurs dostarczy cennych informacji, aby zrozumieć i używać Lightning Network. Chociaż w pierwszych częściach omówimy niektóre podstawy działania Bitcoin, ważne jest, aby opanować podstawy wynalazku Satoshi przed zanurzeniem się w LNP201.


Miłego odkrywania!


+++

# Wprowadzenie

<partId>9da7290a-3895-49a2-93ea-2a6272ca4af4</partId>


## Przegląd kursu

<chapterId>f2e71062-5121-4114-a7f8-27df69884ce8</chapterId>


Witamy w kursie LNP201!


Szkolenie to ma na celu zapewnienie dogłębnego technicznego zrozumienia Lightning Network, sieci nakładkowej zaprojektowanej w celu ułatwienia szybkich i często tanich transakcji Bitcoin. Stopniowo odkryjesz podstawowe koncepcje rządzące tym systemem, od otwierania kanałów płatności po techniki routingu i zarządzanie płynnością.


**Sekcja 1: Podstawy**

Zaczniemy od ogólnego wprowadzenia do Lightning Network, ustanawiając niezbędne podstawy dotyczące Bitcoin, jego adresów, UTXO i sposobu działania transakcji. Ten podstawowy przegląd jest niezbędny do zrozumienia, w jaki sposób Lightning Network opiera się na podstawowych mechanizmach Blockchain, aby działać bezpiecznie.


**Sekcja 2: Otwieranie i zamykanie kanałów**

W tej sekcji zbadamy proces otwierania kanału, który jest kamieniem węgielnym Lightning Network. Dowiesz się, w jaki sposób tworzone są transakcje Commitment, jaka jest rola kluczy odwołania dla bezpieczeństwa i w jaki sposób kanały mogą być zamykane wspólnie lub jednostronnie. Każdy krok zostanie wyjaśniony precyzyjnie i technicznie, aby pomóc ci zrozumieć wszystkie subtelności.


**Sekcja 3: Sieć płynności**

Lightning Network nie ogranicza się do pojedynczych kanałów; to prawdziwa sieć płatności. Zobaczymy, jak transakcje mogą być kierowane przez węzły pośredniczące za pomocą HTLC. W tej sekcji przedstawimy również wyzwania związane z płynnością przychodzącą i wychodzącą.


**Sekcja 4: Narzędzia Lightning Network**

W tej sekcji przedstawiono praktyczne narzędzia Lightning Network, takie jak *Invoices*, *LNURL* i *Keysend*. Dowiesz się również, jak zarządzać płynnością swoich kanałów, co jest istotnym aspektem zapewniającym płynne płatności i maksymalizującym wydajność transakcji na Lightning.


**Sekcja 5: Dalej**

Na koniec szkolenia podsumujemy omówione koncepcje i utorujemy drogę do bardziej zaawansowanych tematów dla tych, którzy chcą pogłębić swoją wiedzę na temat Lightning Network.


Gotowy do odkrycia technicznych mechanizmów Lightning Network? Zanurzmy się!


# Podstawy


<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>


## Zrozumienie Lightning Network


<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>


:::video id=ba99951f-81d2-418f-b5e7-4b8c9f8b8cc8:::



Lightning Network to sieć kanałów płatności zbudowana w oparciu o protokół Bitcoin, mająca na celu umożliwienie szybkich i tanich transakcji. Umożliwia tworzenie kanałów płatności między uczestnikami, w ramach których transakcje mogą być dokonywane niemal natychmiast i przy minimalnych opłatach, bez konieczności rejestrowania każdej transakcji indywidualnie na Blockchain. W ten sposób Lightning Network dąży do poprawy skalowalności Bitcoin i uczynienia go użytecznym dla płatności o niskiej wartości.


Przed zbadaniem aspektu "sieci" ważne jest, aby zrozumieć koncepcję **kanału płatności** na Lightning, jak to działa i jego specyfikę. Jest to temat tego pierwszego rozdziału.


### Koncepcja kanału płatności


Kanał płatności pozwala dwóm stronom, tutaj **Alice** i **Bob**, na Exchange funduszy przez Lightning Network. Każdy bohater ma węzeł, symbolizowany przez okrąg, a kanał między nimi jest reprezentowany przez odcinek linii.


![LNP201](assets/en/01.webp)


W naszym przykładzie Alice ma 100 000 satoshi po swojej stronie kanału, a Bob ma 30 000 satoshi, co daje łącznie 130 000 satoshi, co stanowi **przepustowość kanału**.


**Ale czym jest Satoshi?


**Satoshi** (lub "sat") jest jednostką rozliczeniową na Bitcoin. Podobnie jak cent dla euro, Satoshi jest po prostu ułamkiem Bitcoin. Jeden Satoshi jest równy **0,00000001 Bitcoin**, czyli jednej stumilionowej Bitcoin. Korzystanie z Satoshi staje się coraz bardziej praktyczne wraz ze wzrostem wartości Bitcoin.


### Alokacja funduszy w kanale La Manche


Wróćmy do kanału płatności. Kluczowym pojęciem jest tutaj "**strona kanału**". Każdy uczestnik ma środki po swojej stronie kanału: Alicja 100 000 satoshi, a Bob 30 000. Jak widzieliśmy, suma tych środków reprezentuje całkowitą pojemność kanału, liczbę ustaloną w momencie jego otwarcia.


![LNP201](assets/en/02.webp)


Weźmy przykład transakcji Lightning. Jeśli Alicja chce wysłać 40 000 satoshi do Boba, jest to możliwe, ponieważ ma wystarczającą ilość środków (100 000 satoshi). Po tej transakcji Alicja będzie miała po swojej stronie 60 000 satoshi, a Bob 70 000.


![LNP201](assets/en/03.webp)


Pojemność kanału**, wynosząca 130 000 satoshi, pozostaje stała. To, co się zmienia, to alokacja środków. System ten nie pozwala na wysyłanie większej ilości środków niż się posiada. Na przykład, jeśli Bob chciałby odesłać Alicji 80 000 satoshi, nie mógłby, ponieważ ma tylko 70 000.


Innym sposobem na wyobrażenie sobie alokacji środków jest pomyślenie o **suwaku**, który wskazuje, gdzie znajdują się środki w kanale. Początkowo, przy 100 000 satoshis dla Alice i 30 000 dla Boba, suwak logicznie znajduje się po stronie Alice. Po transakcji 40 000 satoshi, suwak przesunie się nieco w stronę Boba, który ma teraz 70 000 satoshi.


![LNP201](assets/en/04.webp)


Ta reprezentacja może być przydatna do wyobrażenia sobie równowagi funduszy w kanale.


### Podstawowe zasady kanału płatności


Pierwszą kwestią do zapamiętania jest to, że **przepustowość kanału** jest stała. Przypomina to nieco średnicę rury: określa maksymalną ilość środków, które można przesłać przez kanał jednocześnie.

Weźmy przykład: jeśli Alice ma 130 000 satoshi po swojej stronie, może wysłać maksymalnie 130 000 satoshi do Boba w pojedynczej transakcji. Bob może jednak odesłać te środki z powrotem do Alicji, częściowo lub w całości.


Ważne jest, aby zrozumieć, że stała przepustowość kanału ogranicza maksymalną kwotę pojedynczej transakcji, ale nie całkowitą liczbę możliwych transakcji ani ogólny wolumen środków wymienianych w kanale.


**Co powinieneś wynieść z tego rozdziału?



- Przepustowość kanału jest stała i określa maksymalną kwotę, jaką można przesłać w ramach pojedynczej transakcji.
- Środki w kanale są rozdzielane między dwóch uczestników, a każdy z nich może wysyłać do drugiego tylko te środki, które posiada po swojej stronie.
- Lightning Network pozwala zatem na szybkie i wydajne Exchange środków, przy jednoczesnym poszanowaniu ograniczeń narzuconych przez przepustowość kanałów.


To koniec pierwszego rozdziału, w którym położyliśmy podwaliny pod Lightning Network. W kolejnych rozdziałach zobaczymy, jak otworzyć kanał i zagłębimy się w omawiane tutaj koncepcje.


## Bitcoin, adresy, UTXO i transakcje


<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>


:::video id=75323eef-ea03-45ac-9a6e-46d73ca255de:::


Ten rozdział jest nieco wyjątkowy, ponieważ nie będzie bezpośrednio poświęcony Lightning, ale Bitcoin. W rzeczywistości Lightning Network jest Layer nałożonym na Bitcoin. Dlatego ważne jest, aby zrozumieć pewne podstawowe koncepcje Bitcoin, aby właściwie zrozumieć działanie Lightning w kolejnych rozdziałach. W tym rozdziale dokonamy przeglądu podstaw adresów odbiorczych Bitcoin, UTXO, a także funkcjonowania transakcji Bitcoin.


### Adresy Bitcoin, klucze prywatne i klucze publiczne


Bitcoin Address to seria znaków pochodzących z **klucza publicznego**, który jest obliczany na podstawie **klucza prywatnego**. Jak z pewnością wiesz, jest on używany do blokowania bitcoinów, co jest równoznaczne z otrzymaniem ich w naszym Wallet.


Klucz prywatny jest tajnym elementem, który **nigdy nie powinien być udostępniany**, podczas gdy klucz publiczny i Address mogą być udostępniane bez ryzyka dla bezpieczeństwa (ich ujawnienie stanowi jedynie ryzyko dla prywatności użytkownika). Oto wspólna reprezentacja, którą przyjmiemy podczas tego szkolenia:



- Klucze **prywatne** będą reprezentowane **pionowo**.
- Klucze **publiczne** będą reprezentowane **poziomo**.
- Ich kolor wskazuje, kto je posiada (Alicja na pomarańczowo, Bob na czarno...).


### Transakcje Bitcoin: Wysyłanie środków i skrypty


Na Bitcoin transakcja polega na wysłaniu środków z jednego Address do drugiego. Weźmy przykład Alicji wysyłającej 0,002 Bitcoin do Boba. Alicja używa klucza prywatnego powiązanego z jej Address, aby **podpisać** transakcję, udowadniając w ten sposób, że rzeczywiście jest w stanie wydać te środki. Ale co dokładnie dzieje się za tą transakcją? Środki na Bitcoin Address są zablokowane przez **skrypt**, rodzaj mini-programu, który narzuca pewne warunki do wydania środków.


Najpopularniejszy skrypt wymaga podpisu kluczem prywatnym powiązanym z Address. Kiedy Alice podpisuje transakcję swoim kluczem prywatnym, **odblokowuje skrypt**, który blokuje środki, a następnie można je przelać. Transfer środków polega na dodaniu nowego skryptu do tych środków, określającego, że tym razem do ich wydania wymagany będzie podpis kluczem prywatnym **Boba**.


![LNP201](assets/en/05.webp)


### UTXOs: Niewykorzystane wyjścia transakcji


W Bitcoin to, co faktycznie Exchange, to nie bezpośrednio bitcoiny, ale **UTXOs** (_Unspent Transaction Outputs_), co oznacza "niewydane transakcje wyjściowe".


UTXO to kawałek Bitcoin, który może mieć dowolną wartość, na przykład **2 000 bitcoinów**, **8 bitcoinów**, a nawet **8 000 Sats**. Każdy UTXO jest zablokowany przez skrypt i aby go wydać, należy spełnić warunki skryptu, często podpis z kluczem prywatnym odpowiadającym danemu otrzymanemu Address.


UTXO nie mogą być dzielone. Za każdym razem, gdy są używane do wydania kwoty w bitcoinach, które reprezentują, musi to być zrobione w całości. To trochę jak z banknotem: jeśli masz rachunek na 10 euro i jesteś winien piekarzowi 5 euro, nie możesz po prostu przeciąć rachunku na pół. Musisz dać mu banknot o nominale 10 euro, a on wyda ci 5 euro reszty. Jest to dokładnie ta sama zasada dla UTXO w Bitcoin! Na przykład, gdy Alice odblokowuje skrypt swoim kluczem prywatnym, odblokowuje cały UTXO. Jeśli chce wysłać tylko część środków reprezentowanych przez ten UTXO do Boba, może "pofragmentować" go na kilka mniejszych. Następnie wyśle 0,0015 BTC do Boba i wyśle pozostałą część, 0,0005 BTC, do **zamienionego Address**.


Oto przykład transakcji z 2 wyjściami:



- UTXO w wysokości 0,0015 BTC dla Boba, zablokowany przez skrypt wymagający podpisu klucza prywatnego Boba.
- UTXO w wysokości 0,0005 BTC dla Alice, zablokowany przez skrypt wymagający jej własnego podpisu.


![LNP201](assets/en/06.webp)


### Adresy z wieloma podpisami


Oprócz prostych adresów generowanych z jednego klucza publicznego, możliwe jest tworzenie **adresów wielopodpisowych** z wielu kluczy publicznych. Szczególnie interesującym przypadkiem dla Lightning Network jest **2/2 wielopodpisowy Address**, wygenerowany z dwóch kluczy publicznych:


![LNP201](assets/en/07.webp)


Aby wydać środki zablokowane za pomocą Address z wieloma podpisami 2/2, konieczne jest podpisanie za pomocą dwóch kluczy prywatnych powiązanych z kluczami publicznymi.


![LNP201](assets/en/08.webp)


Ten typ Address jest dokładnie odwzorowaniem na Bitcoin Blockchain kanałów płatności na Lightning Network.


**Co powinieneś wynieść z tego rozdziału?



- Klucz **Bitcoin Address** jest wyprowadzany z klucza publicznego, który z kolei jest wyprowadzany z klucza prywatnego.
- Środki na Bitcoin są blokowane przez **skrypty** i aby je wydać, należy spełnić wymagania skryptu, co zazwyczaj wiąże się z dostarczeniem podpisu z odpowiednim kluczem prywatnym.
- UTXO** to kawałki bitcoinów zablokowane przez skrypty, a każda transakcja na Bitcoin polega na odblokowaniu UTXO, a następnie utworzeniu jednego lub więcej nowych w zamian.
- adresy 2/2 z wieloma podpisami** wymagają podpisu dwóch kluczy prywatnych w celu wydania środków. Te konkretne adresy są używane w kontekście Lightning do tworzenia kanałów płatności.


Niniejszy rozdział poświęcony Bitcoin pozwolił nam zapoznać się z kilkoma istotnymi pojęciami. W następnym rozdziale dowiemy się, jak działa otwieranie kanałów na Lightning Network.


# Otwieranie i zamykanie kanałów


<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>


## Otwarcie kanału


<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>


:::video id=6098fee1-735e-4d8d-9f57-0faf5fef6d76:::


W tym rozdziale zobaczymy dokładniej, jak otworzyć kanał płatności na Lightning Network i zrozumiemy związek między tą operacją a bazowym systemem Bitcoin.


### Kanały błyskawic


Jak widzieliśmy w pierwszym rozdziale, **kanał płatności** na Lightning można porównać do "rury" do wymiany środków między dwoma uczestnikami (**Alice** i **Bob** w naszych przykładach). Przepustowość tego kanału odpowiada sumie dostępnych środków po każdej ze stron. W naszym przykładzie Alice ma **100 000 satoshis**, a Bob ma **30 000 satoshis**, co daje **całkowitą przepustowość** wynoszącą **130 000 satoshis**.


![LNP201](assets/en/09.webp)


### Poziomy informacji Exchange


Kluczowe jest wyraźne rozróżnienie różnych poziomów Exchange na Lightning Network:



- Komunikacja peer-to-peer (protokół Lightning)**: Są to wiadomości, które węzły Lightning wysyłają do siebie nawzajem w celu komunikacji. Na naszych diagramach będziemy reprezentować te wiadomości przerywanymi czarnymi liniami.
- Kanały płatności (protokół Lightning)**: Są to ścieżki wymiany środków na Lightning, które przedstawimy za pomocą ciągłych czarnych linii.
- Transakcje Bitcoin (protokół Bitcoin)**: Są to transakcje dokonywane w łańcuchu, które przedstawimy za pomocą pomarańczowych linii.


![LNP201](assets/en/10.webp)


Warto zauważyć, że węzeł Lightning może komunikować się za pośrednictwem protokołu P2P bez otwierania kanału, ale do funduszy Exchange kanał jest niezbędny.


### Kroki otwierania kanału Lightning Channel



- Wiadomość Exchange**: Alicja chce otworzyć kanał z Bobem. Wysyła mu wiadomość zawierającą kwotę, którą chce zdeponować w kanale (130 000 Sats) oraz swój klucz publiczny. Bob odpowiada, udostępniając swój klucz publiczny.


![LNP201](assets/en/11.webp)



- Utworzenie wielopodpisowego Address**: Za pomocą tych dwóch kluczy publicznych Alicja tworzy **2/2 wielopodpisowy Address**, co oznacza, że środki, które zostaną później zdeponowane na tym Address, będą wymagały obu podpisów (Alicji i Boba) do wydania.


![LNP201](assets/en/12.webp)



- Transakcja wpłaty**: Alice przygotowuje transakcję Bitcoin, aby zdeponować środki na tym wielopodpisowym Address. Na przykład, może zdecydować o wysłaniu **130 000 satoshi** na ten wielopodpisowy Address. Ta transakcja jest **stworzona, ale jeszcze nie opublikowana** na Blockchain.


![LNP201](assets/en/13.webp)



- Transakcja wypłaty**: Przed opublikowaniem transakcji wpłaty, Alicja konstruuje transakcję wypłaty, aby mogła odzyskać swoje środki w przypadku problemu z Bobem. W rzeczywistości, gdy Alicja opublikuje transakcję wpłaty, jej Sats zostanie zablokowany na Address z wieloma podpisami 2/2, który wymaga zarówno jej podpisu, jak i podpisu Boba do odblokowania. Alicja chroni się przed tym ryzykiem, konstruując transakcję wypłaty, która pozwala jej odzyskać środki.


![LNP201](assets/en/14.webp)



- Podpis Boba**: Alicja wysyła transakcję wpłaty do Boba jako dowód i prosi go o podpisanie transakcji wypłaty. Po uzyskaniu podpisu Boba na transakcji wypłaty, Alice ma pewność, że będzie w stanie odzyskać swoje środki w dowolnym momencie, ponieważ do odblokowania wielopodpisu potrzebny jest teraz tylko jej własny podpis.


![LNP201](assets/en/15.webp)



- Publikacja transakcji wpłaty**: Po uzyskaniu podpisu Boba, Alice może opublikować transakcję wpłaty na Bitcoin Blockchain, tym samym oficjalnie otwierając kanał Lightning między dwoma użytkownikami.


![LNP201](assets/en/16.webp)


### Kiedy kanał jest otwarty?


Kanał uznaje się za otwarty, gdy transakcja depozytu zostanie uwzględniona w bloku Bitcoin i osiągnie określoną głębokość potwierdzeń (liczbę kolejnych bloków).


**Co powinieneś zapamiętać z tego rozdziału?



- Otwarcie kanału rozpoczyna się od Exchange **komunikatów** między dwiema stronami (Exchange kwot i kluczy publicznych).
- Kanał jest tworzony poprzez utworzenie **2/2 wielopodpisowego Address** i zdeponowanie w nim środków za pośrednictwem transakcji Bitcoin.
- Osoba otwierająca kanał zapewnia, że może **odzyskać swoje środki** poprzez transakcję wypłaty podpisaną przez drugą stronę przed opublikowaniem transakcji wpłaty.


W następnym rozdziale zbadamy techniczne działanie transakcji Lightning w kanale.


## Commitment Transaction


<chapterId>7d3fd135-129d-5c5a-b306-d5f2f1e63340</chapterId>


:::video id=c17454f3-14c5-47a0-8c9c-42ee12932bd3:::


W tym rozdziale odkryjemy techniczne funkcjonowanie transakcji w kanale na Lightning Network, czyli gdy środki są przenoszone z jednej strony kanału na drugą.


### Przypomnienie cyklu życia kanału


Jak widzieliśmy wcześniej, kanał Lightning rozpoczyna się od **otwarcia** za pośrednictwem transakcji Bitcoin. Kanał może zostać **zamknięty** w dowolnym momencie, również za pośrednictwem transakcji Bitcoin. Pomiędzy tymi dwoma momentami można wykonać prawie nieskończoną liczbę transakcji w kanale, bez przechodzenia przez Bitcoin Blockchain. Zobaczmy, co dzieje się podczas transakcji w kanale.


![LNP201](assets/en/17.webp)


### Początkowy stan kanału


W momencie otwarcia kanału Alice zdeponowała **130 000 satoshi** na wielopodpisowym Address kanału. Tak więc w stanie początkowym wszystkie środki są po stronie Alicji. Przed otwarciem kanału Alice poprosiła Boba o podpisanie **transakcji wypłaty**, która pozwoliłaby jej odzyskać środki, gdyby chciała zamknąć kanał.


![LNP201](assets/en/18.webp)


### Niepublikowane transakcje: Transakcje Commitment


Kiedy Alicja dokonuje transakcji w kanale, aby wysłać środki do Boba, tworzona jest nowa transakcja Bitcoin, aby odzwierciedlić tę zmianę w dystrybucji środków. Transakcja ta, zwana **Commitment Transaction**, nie jest publikowana na Blockchain, ale reprezentuje nowy stan kanału po transakcji Lightning.


Weźmy przykład z Alicją wysyłającą 30 000 satoshi do Boba:



- Początkowo**: Alice ma 130 000 satoshi.
- Po transakcji**: Alicja ma 100 000 satoshi, a Bob 30 000 satoshi.

Aby zweryfikować ten transfer, Alice i Bob tworzą nową **nieopublikowaną transakcję Bitcoin**, która wysyła **100 000 satoshi do Alice** i **30 000 satoshi do Boba** z wielopodpisowego Address. Obie strony konstruują tę transakcję niezależnie, ale z tymi samymi danymi (kwoty i adresy). Po skonstruowaniu, każda ze stron podpisuje transakcję i wymienia swój podpis z drugą stroną. Pozwala to każdej ze stron na opublikowanie transakcji w dowolnym momencie, jeśli jest to konieczne, aby odzyskać swój udział w kanale na głównym Bitcoin Blockchain.

![LNP201](assets/en/19.webp)


### Proces transferu: Invoice


Kiedy Bob chce otrzymać środki, wysyła Alice **_fakturę_** na 30 000 satoshi. Alice następnie płaci tym Invoice, rozpoczynając transfer w kanale. Jak widzieliśmy, proces ten opiera się na utworzeniu i podpisaniu nowego **Commitment Transaction**.


Każdy Commitment Transaction reprezentuje nowy podział środków w kanale po transferze. W tym przykładzie po transakcji Bob ma 30 000 satoshi, a Alicja 100 000 satoshi. Jeśli którykolwiek z dwóch uczestników zdecyduje się opublikować Commitment Transaction na Blockchain, spowoduje to zamknięcie kanału, a środki zostaną rozdzielone zgodnie z ostatnią dystrybucją.


![LNP201](assets/en/20.webp)


### Nowy stan po drugiej transakcji


Weźmy inny przykład: po pierwszej transakcji, w której Alice wysłała 30 000 satoshis do Boba, Bob decyduje się wysłać **10 000 satoshis z powrotem do Alice**. Tworzy to nowy stan kanału. Nowy **Commitment Transaction** będzie reprezentował tę zaktualizowaną dystrybucję:



- Alice** ma teraz **110 000 satoshi**.
- Bob** ma **20 000 satoshi**.


![LNP201](assets/en/21.webp)


Ponownie, transakcja ta nie jest publikowana na Blockchain, ale może zostać opublikowana w dowolnym momencie w przypadku zamknięcia kanału.


Podsumowując, gdy środki są przesyłane w ramach kanału Lightning:



- Alice i Bob tworzą nowy **Commitment Transaction**, który odzwierciedla nowy podział środków.
- Ta transakcja Bitcoin jest **podpisana** przez obie strony, ale **nie jest publikowana** na Bitcoin Blockchain, dopóki kanał pozostaje otwarty.
- Transakcje Commitment zapewniają, że każdy uczestnik może odzyskać swoje środki w dowolnym momencie na Bitcoin Blockchain, publikując ostatnią podpisaną transakcję.


System ten ma jednak potencjalną wadę, którą Address omówi w następnym rozdziale. Zobaczymy, jak każdy uczestnik może zabezpieczyć się przed próbą oszustwa ze strony drugiej strony.


## Klucz odwołania


<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>

:::video id=1d850f23-eff1-4725-b284-ce12456a2c26:::

W tym rozdziale zagłębimy się w to, jak transakcje działają na Lightning Network, omawiając mechanizmy ochrony przed oszustwami, zapewniając, że każda ze stron przestrzega zasad w kanale.


### Przypomnienie: Transakcje Commitment


Jak wspomniano wcześniej, transakcje na Lightning opierają się na niepublikowanych ** transakcjach Commitment**. Transakcje te odzwierciedlają bieżącą dystrybucję środków w kanale. Kiedy dokonywana jest nowa transakcja Lightning, tworzony jest nowy Commitment Transaction i podpisywany przez obie strony, aby odzwierciedlić nowy stan kanału.


Weźmy prosty przykład:



- Stan początkowy**: Alicja ma **100 000 satoshi**, Bob **30 000 satoshi**.
- Po transakcji, w której Alice wysyła **40 000 satoshi** do Boba, nowy Commitment Transaction rozdziela środki w następujący sposób:
  - Alice: **60,000 satoshi**
  - Bob: **70,000 satoshi**


![LNP201](assets/en/22.webp)


W dowolnym momencie obie strony mogą opublikować **najnowszy Commitment Transaction** podpisany w celu zamknięcia kanału i odzyskania środków.


### Wada: oszukiwanie poprzez publikowanie starych transakcji


Potencjalny problem pojawia się, gdy jedna ze stron zdecyduje się **oszukać**, publikując stary Commitment Transaction. Na przykład, Alicja może opublikować starszy Commitment Transaction, w którym miała **100 000 satoshi**, mimo że w rzeczywistości ma tylko **60 000**. To pozwoliłoby jej ukraść **40 000 satoshi** od Boba.


![LNP201](assets/en/23.webp)


Co gorsza, Alice mogła opublikować pierwszą transakcję wypłaty, tę przed otwarciem kanału, w której miała **130 000 satoshi**, a tym samym ukraść wszystkie fundusze kanału.


![LNP201](assets/en/24.webp)


### Rozwiązanie: Klucz odwołania i blokada czasowa


Aby zapobiec tego rodzaju oszustwom ze strony Alice, w Lightning Network, **mechanizmy bezpieczeństwa** są dodawane do transakcji Commitment:



- Blokada czasowa**: Każdy Commitment Transaction zawiera blokadę czasową dla środków Alicji. Blokada czasowa jest prymitywem Smart contract, który ustawia warunek czasowy, który musi zostać spełniony, aby transakcja została dodana do bloku. Oznacza to, że Alicja nie może odzyskać swoich środków, dopóki nie minie określona liczba bloków, jeśli opublikuje jedną z transakcji Commitment. Ta blokada czasowa zaczyna obowiązywać od potwierdzenia Commitment Transaction. Czas jej trwania jest zasadniczo proporcjonalny do wielkości kanału, ale można go również skonfigurować ręcznie.
- Klucz odwołania**: Środki Alice mogą być również natychmiast wydane przez Boba, jeśli posiada on **klucz odwołania**. Klucz ten składa się z sekretu posiadanego przez Alicję i sekretu posiadanego przez Boba. Należy pamiętać, że ten sekret jest inny dla każdego Commitment Transaction.

Dzięki tym dwóm połączonym mechanizmom Bob ma czas na wykrycie próby oszustwa Alicji i ukaranie jej poprzez odzyskanie swoich danych wyjściowych za pomocą klucza unieważniającego, co dla Boba oznacza odzyskanie wszystkich środków z kanału. Nasz nowy Commitment Transaction będzie teraz wyglądał następująco:


![LNP201](assets/en/25.webp)


Prześledźmy razem działanie tego mechanizmu.


### Proces aktualizacji transakcji


Kiedy Alicja i Bob aktualizują stan kanału za pomocą nowej transakcji Lightning, Exchange z wyprzedzeniem ich **sekrety** dla poprzedniego Commitment Transaction (tego, który stanie się nieaktualny i może pozwolić jednemu z nich oszukiwać). Oznacza to, że w nowym stanie kanału:



- Alice i Bob mają nowy Commitment Transaction reprezentujący bieżącą dystrybucję środków po transakcji Lightning.
- Każdy z nich ma sekret drugiej strony dla poprzedniej transakcji, co pozwala im użyć klucza odwołania tylko wtedy, gdy jeden z nich próbuje oszukać, publikując transakcję ze starym stanem w mempoolach węzłów Bitcoin. W rzeczywistości, aby ukarać drugą stronę, konieczne jest posiadanie obu sekretów i Commitment Transaction drugiej strony, który zawiera podpisane dane wejściowe. Bez tej transakcji sam klucz odwołania jest bezużyteczny. Jedynym sposobem na uzyskanie tej transakcji jest pobranie jej z mempooli (w transakcjach oczekujących na potwierdzenie) lub w potwierdzonych transakcjach na Blockchain podczas blokady czasowej, co dowodzi, że druga strona próbuje oszukiwać, celowo lub nie.


Weźmy przykład, aby dobrze zrozumieć ten proces:



- Stan początkowy**: Alicja ma **100 000 satoshi**, Bob **30 000 satoshi**.


![LNP201](assets/en/26.webp)



- Bob chce otrzymać 40 000 satoshi od Alicji za pośrednictwem ich kanału Lightning. Aby to zrobić:
   - Wysyła jej Invoice wraz ze swoim sekretem klucza odwołania poprzedniego Commitment Transaction.
   - W odpowiedzi Alice dostarcza swój podpis dla nowego Commitment Transaction Boba, a także swój sekret dla klucza odwołania poprzedniej transakcji.
   - Na koniec Bob wysyła swój podpis dla nowego Commitment Transaction Alicji.
   - Te giełdy pozwalają Alicji wysłać **40 000 satoshi** do Boba na Lightning za pośrednictwem ich kanału, a nowe transakcje Commitment odzwierciedlają teraz tę nową dystrybucję środków.


![LNP201](assets/en/27.webp)



- Jeśli Alicja spróbuje opublikować stary Commitment Transaction, w którym nadal posiadała **100 000 satoshi**, Bob, po uzyskaniu klucza unieważnienia, może natychmiast odzyskać środki za pomocą tego klucza, podczas gdy Alicja jest zablokowana przez blokadę czasową.


![LNP201](assets/en/28.webp)


Nawet jeśli w tym przypadku Bob nie ma interesu ekonomicznego w próbach oszukiwania, jeśli i tak to robi, Alicja również korzysta z symetrycznej ochrony oferującej jej takie same gwarancje.


**Co powinieneś wynieść z tego rozdziału?


Transakcje **Commitment** na Lightning Network zawierają mechanizmy bezpieczeństwa, które zmniejszają zarówno ryzyko oszustwa, jak i zachęty do jego popełnienia. Przed podpisaniem nowego Commitment Transaction, Alicja i Bob Exchange swoje **sekrety** dla poprzednich transakcji Commitment. Jeśli Alicja spróbuje opublikować stary Commitment Transaction, Bob może użyć **klucza odwołania**, aby odzyskać wszystkie środki, zanim Alicja to zrobi (ponieważ jest zablokowana przez blokadę czasową), co karze ją za próbę oszustwa.


Ten system bezpieczeństwa zapewnia, że uczestnicy przestrzegają zasad Lightning Network i nie mogą czerpać korzyści z publikowania starych transakcji Commitment.


Na tym etapie szkolenia wiesz już, w jaki sposób otwierane są kanały Lightning i jak działają transakcje w tych kanałach. W następnym rozdziale odkryjemy różne sposoby zamknięcia kanału i odzyskania bitcoinów na głównym Blockchain.


## Zamknięcie kanału


<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>


:::video id=4d8ad4e6-32ff-46d3-bd17-343929aa863b:::


W tym rozdziale omówimy **zamykanie kanału** na Lightning Network, które odbywa się za pośrednictwem transakcji Bitcoin, podobnie jak otwieranie kanału. Po zapoznaniu się z działaniem transakcji w ramach kanału, nadszedł czas, aby zobaczyć, jak zamknąć kanał i odzyskać środki na Bitcoin Blockchain.


### Przypomnienie cyklu życia kanału


**Cykl życia kanału** rozpoczyna się od jego **otwarcia**, poprzez transakcję Bitcoin, następnie dokonywane są w nim transakcje Lightning, a na koniec, gdy strony chcą odzyskać swoje środki, kanał jest **zamykany** poprzez drugą transakcję Bitcoin. Transakcje pośrednie dokonywane na Lightning są reprezentowane przez niepublikowane **transakcje Commitment**.


![LNP201](assets/en/29.webp)


### Trzy rodzaje zamknięcia kanału


Istnieją trzy główne sposoby zamknięcia tego kanału, które można nazwać **dobrym, brutalnym i wagarowiczem** (zainspirowane przez Andreasa Antonopoulosa w _Mastering the Lightning Network_):



- The Good**: **kooperatywne zamknięcie**, w którym Alice i Bob zgadzają się zamknąć kanał.
- Złe**: **wymuszone zamknięcie**, w którym jedna ze stron decyduje się na uczciwe zamknięcie kanału, ale bez zgody drugiej strony.
- Brzydki**: **zamknięcie z oszustwem**, w którym jedna ze stron próbuje ukraść fundusze, publikując stary Commitment Transaction (dowolny, ale nie ostatni, który odzwierciedla rzeczywisty i sprawiedliwy podział funduszy).


Weźmy przykład:



- Alicja posiada **100 000 satoshi**, a Bob **30 000 satoshi**.
- Ta dystrybucja jest odzwierciedlona w **2 transakcjach Commitment** (po jednej na użytkownika), które nie są publikowane, ale mogą zostać opublikowane w przypadku zamknięcia kanału.


![LNP201](assets/en/30.webp)


### Plusy: zamknięcie współpracy


W **kooperatywnym zamknięciu** Alice i Bob zgadzają się zamknąć kanał. Oto jak to przebiega:



- Alice wysyła wiadomość do Boba za pośrednictwem protokołu komunikacyjnego Lightning, aby zaproponować zamknięcie kanału.
- Bob zgadza się, a obie strony nie dokonują dalszych transakcji w kanale.


![LNP201](assets/en/31.webp)



- Alice i Bob wspólnie negocjują opłaty za **zamknięcie transakcji**. Opłaty te są zazwyczaj obliczane na podstawie rynku opłat Bitcoin w momencie zamknięcia. Ważne jest, aby pamiętać, że **to zawsze osoba, która otworzyła kanał** (Alice w naszym przykładzie) płaci opłaty za zamknięcie.
- Tworzą nową **transakcję zamykającą**. Transakcja ta przypomina Commitment Transaction, ale bez blokad czasowych lub mechanizmów odwoływania, ponieważ obie strony współpracują i nie ma ryzyka oszustwa. Ta kooperacyjna transakcja zamknięcia różni się zatem od transakcji Commitment.


Na przykład, jeśli Alice posiada **100 000 satoshis**, a Bob **30 000 satoshis**, transakcja zamykająca wyśle **100 000 satoshis** do Address Alice i **30 000 satoshis** do Address Boba, bez ograniczeń czasowych. Po podpisaniu transakcji przez obie strony jest ona publikowana przez Alice. Gdy transakcja zostanie potwierdzona na Bitcoin Blockchain, kanał Lightning zostanie oficjalnie zamknięty.


![LNP201](assets/en/32.webp)


**Współpracujące zamknięcie** jest preferowaną metodą zamknięcia, ponieważ jest szybkie (bez blokady czasowej), a opłaty transakcyjne są dostosowywane do aktualnych warunków rynkowych Bitcoin. Pozwala to uniknąć płacenia zbyt małej kwoty, co mogłoby grozić zablokowaniem transakcji w mempoolach, lub niepotrzebnego przepłacania, co prowadzi do niepotrzebnych strat finansowych dla uczestników.


### Złe: przymusowe zamknięcie


Gdy węzeł Alicji wyśle wiadomość do węzła Boba z prośbą o zamknięcie współpracy, jeśli ten nie odpowie (na przykład z powodu przerwy w dostępie do Internetu lub problemu technicznego), Alicja może przystąpić do **wymuszonego zamknięcia**, publikując **ostatnio podpisany Commitment Transaction**.

W tym przypadku Alice po prostu opublikuje ostatni Commitment Transaction, który odzwierciedla stan kanału w czasie, gdy miała miejsce ostatnia transakcja Lightning z prawidłową dystrybucją środków.


![LNP201](assets/en/33.webp)


Transakcja ta obejmuje **timelock** dla środków Alice, co spowalnia zamknięcie.


![LNP201](assets/en/34.webp)


Ponadto opłaty Commitment Transaction mogą być nieodpowiednie w momencie zamknięcia, ponieważ zostały ustalone w momencie tworzenia transakcji, czasami kilka miesięcy wcześniej. Ogólnie rzecz biorąc, klienci Lightning zawyżają opłaty, aby uniknąć przyszłych problemów, ale może to prowadzić do zbyt wysokich opłat lub odwrotnie, zbyt niskich.


Podsumowując, **wymuszone zamknięcie** jest opcją ostateczną, gdy partner przestaje odpowiadać. Jest ono wolniejsze i mniej ekonomiczne niż zamknięcie oparte na współpracy. Dlatego należy go unikać w miarę możliwości.


### Oszustwo: oszukiwanie


Wreszcie, zamknięcie z **oszustwem** ma miejsce, gdy jedna ze stron próbuje opublikować stary Commitment Transaction, często wtedy, gdy posiadała więcej środków niż powinna. Na przykład Alice może opublikować starą transakcję, w której posiadała **120 000 satoshi**, podczas gdy w rzeczywistości posiada tylko **100 000**.


![LNP201](assets/en/35.webp)


Bob, aby zapobiec temu oszustwu, monitoruje Bitcoin Blockchain i jego Mempool, aby upewnić się, że Alicja nie opublikuje starej transakcji. Jeśli Bob wykryje próbę oszustwa, może użyć **klucza odwołania**, aby odzyskać środki Alice i ukarać ją, zabierając wszystkie środki z kanału. Ponieważ Alicja jest zablokowana przez blokadę czasową na swoim wyjściu, Bob ma czas, aby wydać go bez blokady czasowej po swojej stronie, aby odzyskać całą sumę na Address, którego jest właścicielem.


![LNP201](assets/en/36.webp)


Oczywiście oszustwo może potencjalnie zakończyć się sukcesem, jeśli Bob nie podejmie działania w czasie narzuconym przez blokadę czasową wyjścia Alicji. W takim przypadku dane wyjściowe Alicji są odblokowane, co pozwala jej wykorzystać je do utworzenia nowych danych wyjściowych dla kontrolowanego przez nią Address.


**Co powinieneś wynieść z tego rozdziału?


Istnieją trzy sposoby zamknięcia kanału:



- Wspólne zamknięcie**: Szybkie i tańsze rozwiązanie, w którym obie strony zgadzają się zamknąć kanał i opublikować dostosowaną transakcję zamknięcia.
- Wymuszone zamknięcie**: Mniej pożądane, ponieważ polega na opublikowaniu Commitment Transaction z potencjalnie nieodpowiednimi opłatami i blokadą czasową, co spowalnia zamknięcie.
- Oszustwo**: Jeśli jedna ze stron próbuje ukraść środki, publikując starą transakcję, druga może użyć klucza unieważnienia, aby ukarać to oszustwo.


W kolejnych rozdziałach zbadamy Lightning Network z szerszej perspektywy, koncentrując się na tym, jak działa jego sieć.


# Sieć płynności


<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>


## Lightning Network


<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>


:::video id=38419c23-5592-4573-b0a7-84824a5bfb77:::


W tym rozdziale zbadamy, w jaki sposób płatności na Lightning Network mogą dotrzeć do odbiorcy, nawet jeśli nie są oni bezpośrednio połączeni kanałem płatności. Lightning jest bowiem **siecią kanałów płatności**, która umożliwia wysyłanie środków do odległego węzła za pośrednictwem kanałów innych uczestników. Dowiemy się, w jaki sposób płatności są kierowane przez sieć, jak płynność przemieszcza się między kanałami i jak obliczane są opłaty transakcyjne.


### Sieć kanałów płatności


W Lightning Network transakcja odpowiada transferowi środków między dwoma węzłami. Jak pokazano w poprzednich rozdziałach, konieczne jest otwarcie kanału z kimś, aby wykonać transakcje Lightning. Kanał ten pozwala na niemal nieskończoną liczbę transakcji off-chain przed jego zamknięciem w celu odzyskania salda On-Chain. Metoda ta ma jednak tę wadę, że wymaga bezpośredniego kanału z drugą osobą w celu otrzymania lub wysłania środków, co oznacza transakcję otwierającą i zamykającą dla każdego kanału. Jeśli planuję dokonać dużej liczby płatności z tą osobą, otwieranie i zamykanie kanału staje się opłacalne. I odwrotnie, jeśli muszę wykonać tylko kilka transakcji Lightning, otwarcie kanału bezpośredniego nie jest korzystne, ponieważ kosztowałoby mnie to 2 transakcje On-Chain dla ograniczonej liczby transakcji off-chain. Taki przypadek może wystąpić na przykład, gdy chcę zapłacić za pomocą Lightning u sprzedawcy, nie planując powrotu.


Aby rozwiązać ten problem, Lightning Network pozwala na przekierowanie płatności przez kilka kanałów i węzłów pośredniczących, umożliwiając w ten sposób transakcję bez bezpośredniego kanału z drugą osobą.


Wyobraźmy sobie na przykład taką sytuację:



- Alice** (w kolorze pomarańczowym) ma kanał z **Suzie** (w kolorze szarym) z **100 000 satoshis** po swojej stronie i **30 000 satoshis** po stronie Suzie.
- Suzie** ma kanał z **Bobem**, na którym posiada **250 000 satoshi**, a Bob nie posiada żadnych satoshi.


![LNP201](assets/en/37.webp)


Jeśli Alice chce wysłać środki do Boba bez otwierania z nim bezpośredniego kanału, będzie musiała przejść przez Suzie, a każdy kanał będzie musiał dostosować płynność po obu stronach. **Wysłane satoshis pozostają w obrębie swoich kanałów**; w rzeczywistości nie "przekraczają" kanałów, ale transfer odbywa się poprzez dostosowanie wewnętrznej płynności w każdym kanale.


Załóżmy, że Alicja chce wysłać **50 000 satoshi** do Boba:



- Alice** wysyła 50 000 satoshi do **Suzie** na ich wspólnym kanale.
- Suzie** replikuje ten transfer wysyłając 50 000 satoshi do **Boba** na ich kanale.


![LNP201](assets/en/38.webp)


W ten sposób płatność jest kierowana do Boba poprzez ruch płynności w każdym kanale. Na koniec operacji Alice otrzymuje 50 000 Sats. Rzeczywiście przekazała 50 000 Sats, ponieważ początkowo miała 100 000. Bob, po swojej stronie, otrzymuje dodatkowe 50 000 Sats. Dla Suzie (węzła pośredniego) operacja ta jest neutralna: początkowo miała 30 000 Sats w swoim kanale z Alicją i 250 000 Sats w swoim kanale z Bobem, łącznie 280 000 Sats. Po operacji posiada 80 000 Sats w swoim kanale z Alicją i 200 000 Sats w swoim kanale z Bobem, co jest taką samą sumą jak na początku.


Transfer ten jest zatem ograniczony przez **dostępną płynność** w kierunku transferu.


### Obliczanie limitów trasy i płynności


Weźmy teoretyczny przykład innej sieci:



- 130 000 satoshis** po stronie Alice (na pomarańczowo) na jej kanale z **Suzie** (na szaro).
- 90,000 satoshis** po stronie **Suzie** i **200,000 satoshis** po stronie **Carol** (w kolorze różowym).
- 150 000 satoshi** po stronie **Carol** i **100 000 satoshi** po stronie **Boba**.


![LNP201](assets/en/39.webp)


Maksymalna kwota, jaką Alice może wysłać do Boba w tej konfiguracji, wynosi **90 000 satoshi**, ponieważ jest ona ograniczona przez najmniejszą płynność dostępną w kanale od **Suzie do Carol**. W przeciwnym kierunku (od Boba do Alicji) płatność nie jest możliwa, ponieważ strona **Suzie** w kanale z **Alicją** nie zawiera żadnych satoshi. W związku z tym nie ma **żadnej trasy** nadającej się do transferu w tym kierunku.

Alice wysyła kanałami **40 000 satoshi** do Boba:



- Alice przelewa 40 000 satoshi na swój kanał z Suzie.
- Suzie przelewa 40 000 satoshi do Carol na ich wspólnym kanale.
- Carol ostatecznie przekazuje Bobowi 40 000 satoshi.


![LNP201](assets/en/40.webp)


Satoshi wysłane** w każdym kanale **pozostają w kanale**, więc satoshi wysłane przez Carol do Boba nie są takie same jak te wysłane przez Alice do Suzie. Transfer odbywa się tylko poprzez dostosowanie płynności wewnątrz każdego kanału. Co więcej, całkowita pojemność kanałów pozostaje niezmieniona.


![LNP201](assets/en/41.webp)


Podobnie jak w poprzednim przykładzie, po transakcji węzeł źródłowy (Alice) ma 40 000 satoshi mniej. Węzły pośrednie (Suzie i Carol) zachowują tę samą łączną kwotę, dzięki czemu operacja jest dla nich neutralna. Wreszcie, węzeł docelowy (Bob) otrzymuje dodatkowe 40 000 satoshi.


Rola węzłów pośrednich jest zatem bardzo ważna w funkcjonowaniu Lightning Network. Ułatwiają one transfery, oferując wiele ścieżek płatności. Aby zachęcić te węzły do zapewnienia płynności i uczestniczenia w routingu płatności, uiszczane są na ich rzecz **opłaty routingowe**.


### Opłaty Routingowe


Węzły pośrednie stosują opłaty, aby umożliwić przekazywanie płatności przez ich kanały. Opłaty te są ustalane przez **każdy węzeł dla każdego kanału**. Opłaty składają się z 2 Elements:



- "**Opłata podstawowa**": stała kwota za kanał, często domyślnie **1 sat**, ale z możliwością dostosowania.
- "**Opłata zmienna**": wartość procentowa przesyłanej kwoty, obliczana w **częściach na milion (ppm)**. Domyślnie jest to **1 ppm** (1 sat na milion przesłanych satoshi), ale można go również dostosować.


Opłaty różnią się również w zależności od kierunku przelewu. Na przykład w przypadku przelewu z Alice do Suzie obowiązują opłaty Alice. I odwrotnie, z Suzie do Alice, stosowane są opłaty Suzie.


Na przykład, dla kanału między Alice i Suzie, możemy mieć:



- Alice**: opłata podstawowa w wysokości 1 sat i 1 ppm dla opłat zmiennych.
- Suzie**: opłata podstawowa w wysokości 0,5 sata i 10 ppm dla opłat zmiennych.


![LNP201](assets/en/42.webp)


Aby lepiej zrozumieć, jak działają opłaty, przeanalizujmy ten sam Lightning Network, co poprzednio, ale teraz z następującymi opłatami za routing:



- Kanał **Alice - Suzie**: opłata podstawowa w wysokości 1 Satoshi i 1 ppm dla Alice.
- Kanał **Suzie - Carol**: opłata podstawowa 0 Satoshi i 200 ppm dla Suzie.
- Kanał Carol - Bob**: opłata podstawowa w wysokości 1 Satoshi i 1 ppm dla Suzie 2.

![LNP201](assets/en/43.webp)


Aby dokonać tej samej płatności w wysokości **40 000 satoshi** na rzecz Boba, Alicja będzie musiała wysłać nieco więcej, ponieważ każdy węzeł pośredniczący potrąci swoje opłaty:



- Carol** odejmuje 1,04 sat na kanale z Bobem:

$$ f*{\text{Carol-Bob}} = \text{opłata podstawowa} + \left(\frac{\text{ppm} \times \text{amount}}{10^6}\right) $$

$$ f*{\text{Carol-Bob}} = 1 + \frac{1 \times 40000}{10^6} = 1 + 0.04 = 1.04 \text{ Sats} $$



- Suzie** odejmuje 8 Satoshis w opłatach na kanale z Carol:

$$ f*{\text{Suzie-Carol}} = \text{opłata podstawowa} + \left(\frac{\text{ppm} \times \text{amount}}{10^6}\right) $$

$$ f*{\text{Suzie-Carol}} = 0 + \frac{200 \times 40001.04}{10^6} = 0 + 8.0002 \approx 8 \text{ Sats} $$


Całkowite opłaty za tę płatność na tej ścieżce wynoszą zatem **9,04 satoshis**. Zatem Alicja musi wysłać **40 009,04 satoshi**, aby Bob otrzymał dokładnie **40 000 satoshi**.


![LNP201](assets/en/44.webp)


Płynność jest zatem aktualizowana:


![LNP201](assets/en/45.webp)


### Routing cebulowy


Aby skierować płatność od nadawcy do odbiorcy, Lightning Network wykorzystuje metodę zwaną "**routingiem cebulowym**". W przeciwieństwie do routingu klasycznych danych, gdzie każdy router decyduje o kierunku danych w oparciu o ich miejsce docelowe, routing cebulowy działa inaczej:



- Węzeł wysyłający oblicza całą trasę**: Alice, na przykład, określa, że jej płatność musi przejść przez Suzie i Carol, zanim dotrze do Boba.
- Każdy węzeł pośredniczący zna tylko swojego bezpośredniego sąsiada**: Suzie wie tylko, że otrzymała środki od Alice i że musi je przekazać Carol. Suzie nie wie jednak, czy Alice jest węzłem źródłowym, czy węzłem pośredniczącym, a także nie wie, czy Carol jest węzłem odbiorczym, czy tylko innym węzłem pośredniczącym. Zasada ta dotyczy również Carol i wszystkich innych węzłów na ścieżce. W ten sposób routing cebulowy zachowuje poufność transakcji poprzez maskowanie tożsamości nadawcy i odbiorcy końcowego.

Aby zapewnić, że węzeł nadawczy może obliczyć pełną trasę do odbiorcy w routingu cebulowym, musi on utrzymywać **graf sieciowy**, aby znać swoją topologię i określić możliwe trasy.

**Co powinieneś wynieść z tego rozdziału?



- W Lightning płatności mogą być kierowane między węzłami połączonymi pośrednio przez kanały pośredniczące. Każdy z tych węzłów pośredniczących ułatwia przekazywanie płynności.
- Węzły pośredniczące otrzymują prowizję za swoje usługi, składającą się z opłat stałych i zmiennych.
- Trasowanie cebulowe pozwala węzłowi nadawczemu obliczyć pełną trasę bez znajomości źródła lub miejsca docelowego przez węzły pośredniczące.


W tym rozdziale zbadaliśmy routing płatności na Lightning Network. Pojawia się jednak pytanie: co uniemożliwia węzłom pośredniczącym akceptowanie płatności przychodzących bez przekazywania ich do następnego miejsca docelowego w celu przechwycenia transakcji? To jest właśnie rola HTLC, którą przeanalizujemy w następnym rozdziale.


## HTLC - Blokada czasowa Contract


<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>


:::video id=6f204b92-55a5-4939-9440-7c5b96a297bf:::


W tym rozdziale odkryjemy, w jaki sposób Lightning umożliwia przesyłanie płatności przez węzły pośredniczące bez konieczności ufania im, dzięki **HTLC** (_Hashed Time-Locked Contracts_). Te inteligentne kontrakty zapewniają, że każdy węzeł pośredniczący otrzyma środki ze swojego kanału tylko wtedy, gdy przekaże płatność ostatecznemu odbiorcy, w przeciwnym razie płatność nie zostanie zatwierdzona.


Kwestią, która pojawia się w przypadku routingu płatności, jest zatem niezbędne zaufanie do węzłów pośredniczących i między samymi węzłami pośredniczącymi. Aby to zilustrować, powróćmy do naszego uproszczonego przykładu Lightning Network z 3 węzłami i 2 kanałami:



- Alice ma kanał z Suzie.
- Suzie ma kanał z Bobem.


Alice chce wysłać 40 000 Sats do Boba, ale nie ma z nim bezpośredniego kanału i nie chce go otwierać. Szuka trasy i decyduje się przejść przez węzeł Suzie.


![LNP201](assets/en/46.webp)


Jeśli Alice naiwnie wyśle 40 000 satoshi do Suzie, mając nadzieję, że Suzie przeleje tę sumę Bobowi, Suzie może zatrzymać środki dla siebie i nie przekaże niczego Bobowi.


![LNP201](assets/en/47.webp)

Aby uniknąć takiej sytuacji, w Lightning używamy HTLC (Hashed Time-Locked Contracts), które sprawiają, że płatność do węzła pośredniczącego jest warunkowa, co oznacza, że Suzie musi spełnić określone warunki, aby uzyskać dostęp do środków Alicji i przekazać je Bobowi.


### Jak działają HTLC


HTLC jest specjalnym Contract opartym na dwóch zasadach:



- Warunek dostępu**: Odbiorca musi ujawnić sekret, aby odblokować należną mu płatność.
- Wygaśnięcie**: Jeśli płatność nie zostanie w pełni zrealizowana w określonym czasie, zostanie anulowana, a środki wrócą do nadawcy.


Oto jak ten proces działa w naszym przykładzie z Alice, Suzie i Bobem:


![LNP201](assets/en/48.webp)


**Tworzenie sekretu**: Bob generuje losowy sekret oznaczony jako _s_ (obraz wstępny) i oblicza jego Hash oznaczony jako _r_ za pomocą funkcji Hash oznaczonej jako _h_. Mamy:


$$
r = h(s)
$$


Użycie funkcji Hash uniemożliwia znalezienie _s_ tylko z _h(s)_, ale jeśli _s_ jest podane, łatwo jest zweryfikować, że odpowiada _h(s)_.


![LNP201](assets/en/49.webp)


**Wysłanie żądania płatności**: Bob wysyła **Invoice** do Alicji z prośbą o płatność. Ten Invoice zawiera w szczególności Hash _r_.


![LNP201](assets/en/50.webp)


**Wysłanie płatności warunkowej**: Alicja wysyła HTLC w wysokości 40 000 satoshi do Suzie. Warunkiem otrzymania tych środków przez Suzie jest dostarczenie Alicji tajnego _s'_ spełniającego następujące równanie:


$$
h(s') = r
$$


![LNP201](assets/en/51.webp)


**Przekazanie HTLC ostatecznemu odbiorcy**: Suzie, aby otrzymać 40 000 satoshi od Alicji, musi przekazać podobny HTLC o wartości 40 000 satoshi do Boba, który ma ten sam warunek, a mianowicie musi dostarczyć Suzie sekret _s'_, który spełnia równanie:


$$
h(s') = r
$$


![LNP201](assets/en/52.webp)


**Weryfikacja przez tajne _s_**: Bob przekazuje _s_ Suzie, aby otrzymać 40 000 satoshi obiecanych w HTLC. Dzięki temu sekretowi Suzie może odblokować HTLC Alice i otrzymać od niej 40 000 satoshi. Płatność jest następnie prawidłowo kierowana do Boba.


![LNP201](assets/en/53.webp)

Proces ten uniemożliwia Suzie zatrzymanie środków Alicji bez ukończenia transferu do Boba, ponieważ musi ona wysłać płatność do Boba, aby uzyskać tajne _s_, a tym samym odblokować HTLC Alicji. Operacja pozostaje taka sama, nawet jeśli trasa obejmuje kilka węzłów pośredniczących: jest to po prostu kwestia powtórzenia kroków Suzie dla każdego węzła pośredniczącego. Każdy węzeł jest chroniony przez warunki HTLC, ponieważ odblokowanie ostatniego HTLC przez odbiorcę automatycznie uruchamia odblokowanie wszystkich innych HTLC w kaskadzie.


### Wygaśnięcie i zarządzanie HTLC w przypadku problemów


Jeśli podczas procesu płatności jeden z węzłów pośredniczących lub węzeł odbiorcy przestanie odpowiadać, szczególnie w przypadku awarii Internetu lub zasilania, wówczas płatność nie może zostać zakończona, ponieważ sekret potrzebny do odblokowania HTLC nie został przesłany. Biorąc pod uwagę nasz przykład z Alice, Suzie i Bobem, problem ten występuje na przykład, gdy Bob nie przesyła sekretu _s_ do Suzie. W takim przypadku wszystkie HTLC znajdujące się przed ścieżką zostaną zablokowane, a zabezpieczone przez nie środki również.


![LNP201](assets/en/54.webp)


Aby tego uniknąć, HTLC na Lightning mają okres ważności, który pozwala na usunięcie HTLC, jeśli nie zostanie on ukończony po określonym czasie. Wygaśnięcie następuje w określonej kolejności, ponieważ zaczyna się najpierw od HTLC najbliższego odbiorcy, a następnie stopniowo przesuwa się w górę do emitenta transakcji. W naszym przykładzie, jeśli Bob nigdy nie przekaże tajemnicy _s_ Suzie, spowoduje to wygaśnięcie HTLC Suzie wobec Boba.


![LNP201](assets/en/55.webp)


Następnie HTLC od Alice do Suzie.


![LNP201](assets/en/56.webp)


Gdyby kolejność wygaśnięcia została odwrócona, Alice mogłaby odzyskać swoją płatność, zanim Suzie zdołałaby uchronić się przed potencjalnym oszustwem. Rzeczywiście, jeśli Bob wróci, aby odebrać swój HTLC, podczas gdy Alice już usunęła swój, Suzie znalazłaby się w niekorzystnej sytuacji. Ta kaskadowa kolejność wygasania HTLC zapewnia zatem, że żaden węzeł pośredniczący nie ponosi nieuczciwych strat.


### Reprezentacja HTLC w transakcjach Commitment


Transakcje Commitment reprezentują HTLC w taki sposób, że warunki, które nakładają na Lightning, mogą zostać przeniesione do Bitcoin w przypadku wymuszonego zamknięcia kanału w trakcie życia HTLC. Dla przypomnienia, transakcje Commitment reprezentują aktualny stan kanału między dwoma użytkownikami i pozwalają na jednostronne wymuszone zamknięcie w przypadku wystąpienia problemów. Z każdym nowym stanem kanału tworzone są 2 transakcje Commitment: po jednej dla każdej ze stron. Powróćmy do naszego przykładu z Alice, Suzie i Bobem, ale przyjrzyjmy się bliżej temu, co dzieje się na poziomie kanału między Alice i Suzie, gdy tworzony jest HTLC.

![LNP201](assets/en/57.webp)


Przed rozpoczęciem płatności 40 000 Sats między Alice i Bobem, Alice posiada 100 000 Sats w swoim kanale z Suzie, podczas gdy Suzie posiada 30 000. Ich transakcje Commitment wyglądają następująco:


![LNP201](assets/en/58.webp)


Alicja właśnie otrzymała Invoice Boba, który w szczególności zawiera _r_, Hash sekretu. Może więc skonstruować HTLC o wartości 40 000 satoshi z Suzie. Ten HTLC jest reprezentowany w ostatnich transakcjach Commitment jako wyjście o nazwie "**_HTLC Out_**" po stronie Alicji, ponieważ fundusze są wychodzące, i "**_HTLC In_**" po stronie Suzie, ponieważ fundusze są przychodzące.


![LNP201](assets/en/59.webp)


Te wyjścia powiązane z HTLC mają dokładnie takie same warunki, a mianowicie:



- Jeśli Suzie jest w stanie podać tajne _s_, może natychmiast odblokować to wyjście i przesłać je do kontrolowanego przez siebie Address.
- Jeśli Suzie nie posiada sekretu _s_, nie może odblokować tego wyjścia, a Alicja będzie w stanie odblokować je po blokadzie czasowej, aby wysłać je do kontrolowanego przez nią Address. Blokada czasowa daje więc Suzie czas na reakcję, jeśli zdobędzie _s_.


Warunki te mają zastosowanie tylko wtedy, gdy kanał zostanie zamknięty (tj. Commitment Transaction zostanie opublikowany On-Chain), podczas gdy HTLC jest nadal aktywny na Lightning, co oznacza, że płatność między Alice i Bobem nie została jeszcze sfinalizowana, a HTLC jeszcze nie wygasły. Dzięki tym warunkom Suzie może odzyskać należne jej 40 000 satoshi z HTLC poprzez dostarczenie _s_. W przeciwnym razie Alicja odzyska środki po wygaśnięciu blokady czasowej, ponieważ jeśli Suzie nie zna _s_, oznacza to, że nie przekazała 40 000 satoshi Bobowi, a zatem środki Alicji nie są jej należne.


Ponadto, jeśli kanał zostanie zamknięty, podczas gdy kilka HTLC jest w toku, będzie tyle dodatkowych wyjść, ile trwa HTLC.

Jeśli kanał nie zostanie zamknięty, to po wygaśnięciu lub powodzeniu płatności Lightning tworzone są nowe transakcje Commitment, aby odzwierciedlić nowy, teraz stabilny stan kanału, czyli bez żadnych oczekujących HTLC. Dane wyjściowe związane z HTLC można zatem usunąć z transakcji Commitment.

![LNP201](assets/en/60.webp)


Wreszcie, w przypadku zamknięcia kanału współpracy, gdy aktywny jest HTLC, Alice i Suzie przestają akceptować nowe płatności i czekają na rozwiązanie lub wygaśnięcie trwających HTLC. Pozwala im to opublikować lżejszą transakcję zamknięcia, bez danych wyjściowych związanych z HTLC, zmniejszając w ten sposób opłaty i unikając oczekiwania na ewentualną blokadę czasową.


**Co powinieneś wynieść z tego rozdziału?


HTLC umożliwiają kierowanie płatności Lightning przez wiele węzłów bez konieczności ufania im. Oto kluczowe punkty do zapamiętania:



- HTLC zapewniają bezpieczeństwo płatności poprzez sekret (obraz wstępny) i czas wygaśnięcia.
- Rozwiązanie lub wygaśnięcie HTLC następuje w określonej kolejności: następnie od miejsca docelowego do źródła, w celu ochrony każdego węzła.
- Dopóki HTLC nie zostanie rozwiązany ani nie wygaśnie, jest on utrzymywany jako wynik w ostatnich transakcjach Commitment.


W następnym rozdziale dowiemy się, w jaki sposób węzeł wydający transakcję Lightning znajduje i wybiera trasy dla swojej płatności, aby dotrzeć do węzła odbiorcy.


## Znajdowanie drogi


<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>


:::video id=e5baa834-111d-46f5-a28b-3538bed2bbb0:::


W poprzednich rozdziałach widzieliśmy, jak korzystać z kanałów innych węzłów do kierowania płatności i docierania do węzła bez bezpośredniego połączenia z nim za pośrednictwem kanału. Omówiliśmy również, jak zapewnić bezpieczeństwo transferu bez ufania węzłom pośredniczącym. W tym rozdziale skupimy się na znalezieniu najlepszej możliwej trasy dotarcia do węzła docelowego.


### Problem routingu w Lightning


Jak widzieliśmy, w Lightning to węzeł wysyłający płatność musi obliczyć pełną trasę do odbiorcy, ponieważ używamy systemu routingu cebulowego. Węzły pośredniczące nie znają ani punktu początkowego, ani ostatecznego miejsca docelowego. Wiedzą tylko, skąd pochodzi płatność i do którego węzła muszą ją następnie przesłać. Oznacza to, że węzeł wysyłający musi utrzymywać dynamiczną lokalną topologię sieci, z istniejącymi węzłami Lightning i kanałami między nimi, biorąc pod uwagę otwarcia, zamknięcia i aktualizacje stanu.


![LNP201](assets/en/61.webp)

Nawet przy takiej topologii Lightning Network, istnieją istotne informacje dla routingu, które pozostają niedostępne dla węzła wysyłającego, czyli dokładny rozkład płynności w kanałach w danym momencie. Rzeczywiście, każdy kanał wyświetla tylko swoją **całkowitą pojemność**, ale wewnętrzna dystrybucja środków jest znana tylko dwóm uczestniczącym węzłom. Stanowi to wyzwanie dla efektywnego routingu, ponieważ powodzenie płatności zależy w szczególności od tego, czy jej kwota jest mniejsza niż najniższa płynność na wybranej trasie. Płynności nie są jednak widoczne dla węzła wysyłającego.

![LNP201](assets/en/62.webp)


### Aktualizacja mapy sieci


Aby mapa sieci była aktualna, węzły regularnie wysyłają wiadomości Exchange za pomocą algorytmu o nazwie "**_gossip_**". Jest to rozproszony algorytm używany do rozprzestrzeniania informacji w sposób epidemiczny do wszystkich węzłów w sieci, co pozwala na Exchange i synchronizację Global State kanałów w kilku cyklach komunikacyjnych. Każdy węzeł rozprzestrzenia informacje do jednego lub więcej sąsiadów wybranych losowo lub nie, ci z kolei rozprzestrzeniają informacje do innych sąsiadów i tak dalej, aż do osiągnięcia globalnie zsynchronizowanego stanu.


Dwie główne wiadomości wymieniane między węzłami Lightning są następujące:



- "**Channel Announcements**": wiadomości sygnalizujące otwarcie nowego kanału.
- "**Channel Updates**": wiadomości aktualizacyjne dotyczące stanu kanału, w szczególności ewolucji opłat (ale nie dystrybucji płynności).


Węzły Lightning monitorują również Bitcoin Blockchain w celu wykrycia transakcji zamknięcia kanału. Zamknięty kanał jest następnie usuwany z mapy, ponieważ nie może być już używany do kierowania naszych płatności.


### Routing płatności


Weźmy przykład małej sieci Lightning Network z 7 węzłami: Alice, Bob, 1, 2, 3, 4 i 5. Wyobraźmy sobie, że Alicja chce wysłać płatność do Boba, ale musi przejść przez węzły pośredniczące.


![LNP201](assets/en/63.webp)


Oto rzeczywista dystrybucja środków w tych kanałach:



- Kanał pomiędzy Alice i 1**: 250 000 Sats po stronie Alice, 80 000 po stronie 1 (całkowita przepustowość 330 000 Sats).
- Kanał pomiędzy 1 i 2**: 300 000 Sats po stronie 1, 200 000 po stronie 2 (całkowita pojemność 500 000 Sats).
- Kanał pomiędzy 2 i 3**: 50 000 Sats po stronie 2, 60 000 po stronie 3 (całkowita pojemność 110 000 Sats).
- Kanał pomiędzy 2 i 5**: 90 000 Sats po stronie 2, 160 000 po stronie 5 (całkowita pojemność 250 000 Sats).
- Kanał między 2 i 4**: 180 000 Sats po stronie 2, 110 000 po stronie 4 (całkowita pojemność 290 000 Sats).
- Kanał pomiędzy 4 i 5**: 200 000 Sats po stronie 4, 10 000 po stronie 5 (całkowita pojemność 210 000 Sats).
- Kanał pomiędzy 3 i Bob**: 50 000 Sats po stronie 3, 250 000 po stronie Bob (całkowita pojemność 300 000 Sats).
- Kanał pomiędzy 5 i Bob**: 260 000 Sats po stronie 5, 100 000 po stronie Bob (całkowita pojemność 360 000 Sats).


![LNP201](assets/en/64.webp)


Aby dokonać płatności w wysokości 100 000 Sats od Alicji do Boba, opcje routingu są ograniczone przez dostępną płynność w każdym kanale. Optymalną trasą dla Alicji, w oparciu o znane rozkłady płynności, może być sekwencja "Alicja → 1 → 2 → 4 → 5 → Bob":


![LNP201](assets/en/65.webp)


Ponieważ jednak Alice nie zna dokładnej dystrybucji środków w każdym kanale, musi oszacować optymalną trasę w sposób probabilistyczny, biorąc pod uwagę następujące kryteria:



- Prawdopodobieństwo sukcesu**: kanał o wyższej całkowitej przepustowości z większym prawdopodobieństwem będzie zawierał wystarczającą płynność. Na przykład, kanał między węzłem 2 i węzłem 3 ma całkowitą przepustowość 110 000 Sats, więc znalezienie 100 000 Sats lub więcej po stronie węzła 2 jest mało prawdopodobne, choć nadal możliwe.
- Opłaty transakcyjne**: wybierając najlepszą trasę, węzeł wysyłający bierze również pod uwagę opłaty stosowane przez każdy węzeł pośredni i dąży do zminimalizowania całkowitego kosztu routingu.
- Wygaśnięcie HTLC**: aby uniknąć zablokowanych płatności, czas wygaśnięcia HTLC jest również parametrem, który należy wziąć pod uwagę.
- Liczba węzłów pośrednich**: wreszcie, bardziej ogólnie, węzeł wysyłający będzie starał się znaleźć trasę z jak najmniejszą liczbą węzłów, aby zmniejszyć ryzyko niepowodzenia i ograniczyć opłaty za transakcje błyskawiczne.


Analizując te kryteria, węzeł wysyłający może przetestować najbardziej prawdopodobne trasy i spróbować je zoptymalizować. W naszym przykładzie Alice mogłaby uszeregować najlepsze trasy w następujący sposób:



- `Alice → 1 → 2 → 5 → Bob`, ponieważ jest to najkrótsza trasa o największej przepustowości.
- `Alice → 1 → 2 → 4 → 5 → Bob`, ponieważ ta trasa oferuje dobrą przepustowość, chociaż jest dłuższa niż pierwsza.
- `Alice → 1 → 2 → 3 → Bob`, ponieważ ta trasa obejmuje kanał `2 → 3`, który ma bardzo ograniczoną przepustowość, ale pozostaje potencjalnie użyteczny.


### Realizacja płatności


Alice postanawia przetestować swoją pierwszą trasę (`Alice → 1 → 2 → 5 → Bob`). W związku z tym wysyła HTLC w wysokości 100 000 Sats do węzła 1. Węzeł ten sprawdza, czy ma wystarczającą płynność z węzłem 2 i kontynuuje transmisję. Węzeł 2 odbiera następnie HTLC z węzła 1, ale zdaje sobie sprawę, że nie ma wystarczającej płynności w swoim kanale z węzłem 5, aby skierować płatność w wysokości 100 000 Sats. Następnie wysyła komunikat o błędzie z powrotem do węzła 1, który przesyła go do Alice. Ta trasa nie powiodła się.


![LNP201](assets/en/66.webp)


Następnie Alice próbuje skierować swoją płatność przy użyciu drugiej trasy (`Alice → 1 → 2 → 4 → 5 → Bob`). Wysyła HTLC o wartości 100 000 Sats do węzła 1, który przesyła go do węzła 2, następnie do węzła 4, do węzła 5 i wreszcie do Boba. Tym razem płynność jest wystarczająca, a trasa działa. Każdy węzeł odblokowuje swój HTLC kaskadowo przy użyciu obrazu wstępnego dostarczonego przez Boba (sekret _s_), co pozwala na pomyślne sfinalizowanie płatności Alicji na rzecz Boba.


![LNP201](assets/en/67.webp)


Poszukiwanie trasy odbywa się w następujący sposób: węzeł wysyłający rozpoczyna od zidentyfikowania najlepszych możliwych tras, a następnie próbuje kolejno dokonywać płatności, aż do znalezienia funkcjonalnej trasy.


Warto zauważyć, że Bob może dostarczyć Alicji informacje w **Invoice**, aby ułatwić routing. Na przykład może wskazać pobliskie kanały o wystarczającej płynności lub ujawnić istnienie kanałów prywatnych. Wskazówki te pozwalają Alicji unikać tras o niewielkich szansach powodzenia i najpierw wypróbować ścieżki zalecane przez Boba.


**Co powinieneś wynieść z tego rozdziału?



- Węzły utrzymują mapę topologii sieci poprzez ogłoszenia i monitorowanie zamknięć kanałów na Bitcoin Blockchain.
- Poszukiwanie optymalnej trasy dla płatności pozostaje probabilistyczne i zależy od wielu kryteriów.
- Bob może dostarczyć wskazówek w **Invoice**, aby pokierować trasą Alice i uchronić ją przed testowaniem mało prawdopodobnych tras.


W następnym rozdziale zajmiemy się w szczególności funkcjonowaniem faktur, a także kilkoma innymi narzędziami używanymi w Lightning Network.


# Narzędzia Lightning Network


<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>


## Invoice, LNURL i Keysend


<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>

:::video id=309c3412-506e-4189-ad46-5e5088c55008:::


W tym rozdziale przyjrzymy się bliżej działaniu **faktur** Lightning, czyli żądań płatności wysyłanych przez węzeł odbiorcy do węzła nadawcy. Celem jest zrozumienie, jak płacić i otrzymywać płatności w Lightning. Omówimy również 2 alternatywy dla klasycznych faktur: LNURL i Keysend.


![LNP201](assets/en/68.webp)


### Struktura faktur Lightning


Jak wyjaśniono w rozdziale dotyczącym HTLC, każda płatność rozpoczyna się od wygenerowania **Invoice** przez odbiorcę. Ten Invoice jest następnie przesyłany do płatnika (za pomocą kodu QR lub przez kopiowanie-wklejanie) w celu zainicjowania płatności. Invoice składa się z dwóch głównych części:



- Część czytelna dla człowieka**: ta sekcja zawiera wyraźnie widoczne metadane w celu poprawy komfortu użytkowania.
- Payload**: ta sekcja zawiera informacje przeznaczone dla maszyn do przetwarzania płatności.


Typowa struktura Invoice zaczyna się od identyfikatora `LN` dla "Lightning", po którym następuje `bc` dla Bitcoin, a następnie ilość Invoice. Separator `1` odróżnia część czytelną dla człowieka od części danych (ładunku).


Weźmy następujący Invoice jako przykład:


```invoice
lnbc100u1p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```


Możemy już podzielić go na 2 części. Pierwsza to część czytelna dla człowieka:


```invoice
lnbc100u
```


Następnie część przeznaczona na ładunek:


```invoice

p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```


Obie części są oddzielone znakiem `1`. Separator ten został wybrany zamiast znaku specjalnego, aby umożliwić łatwe kopiowanie i wklejanie całego Invoice poprzez dwukrotne kliknięcie.


W pierwszej części możemy to zobaczyć:



- `LN` wskazuje, że jest to transakcja Lightning.
- `bc` wskazuje, że Lightning Network znajduje się na Bitcoin Blockchain (a nie na Testnet lub na Litecoin).
- `100u` oznacza ilość Invoice, wyrażoną w **mikrobitcoinach** (`u` oznacza "mikro"), co tutaj równa się 10 000 Sats.


Aby określić kwotę płatności, jest ona wyrażana w podjednostkach Bitcoin. Oto używane jednostki:



- Millibitcoin (oznaczany `m`):** Reprezentuje jedną tysięczną Bitcoin.


$$
1 \, \text{mBTC} = 10^{-3} \, \text{BTC} = 10^5 \, \text{satoshis}
$$



- Microbitcoin (oznaczany `u`):** Czasami nazywany również "bitem", reprezentuje jedną milionową Bitcoin.


$$
1 \, \mu\text{BTC} = 10^{-6} \, \text{BTC} = 100 \, \text{satoshis}
$$



- Nanobitcoin (oznaczany `n`):** Reprezentuje jedną miliardową Bitcoin.


$$
1 \, \text{nBTC} = 10^{-9} \, \text{BTC} = 0.1 \, \text{satoshis}
$$



- Picobitcoin (oznaczany jako `p`):** Reprezentuje jedną bilionową Bitcoin.

$$
1 \, \text{pBTC} = 10^{-12} \, \text{BTC} = 0.0001 \, \text{satoshis}
$$


### Ładunek użyteczny Invoice


Ładunek Invoice zawiera kilka informacji niezbędnych do przetworzenia płatności:



- Timestamp:** Moment utworzenia Invoice, wyrażony w Unix Timestamp (liczba sekund, które upłynęły od 1 stycznia 1970 r.).
- Hashowanie sekretu**: Jak widzieliśmy w sekcji dotyczącej HTLC, węzeł odbierający musi dostarczyć węzłowi wysyłającemu Hash obrazu wstępnego. Jest to używane w HTLC do zabezpieczenia transakcji. Określiliśmy to jako "_r_".
- Sekret płatności**: Kolejny sekret jest generowany przez odbiorcę, ale tym razem jest on przesyłany do węzła wysyłającego. Jest on używany w routingu cebulowym, aby uniemożliwić węzłom pośrednim odgadnięcie, czy następny węzeł jest odbiorcą końcowym, czy nie. W ten sposób odbiorca zachowuje pewną formę poufności w odniesieniu do ostatniego węzła pośredniego na trasie.
- Klucz publiczny odbiorcy**: Wskazuje płatnikowi identyfikator osoby, która ma otrzymać płatność.
- Czas wygaśnięcia**: Maksymalny czas, przez jaki Invoice ma być opłacany (domyślnie 1 godzina).
- Routing Hints**: Dodatkowe informacje dostarczone przez odbiorcę, aby pomóc nadawcy zoptymalizować trasę płatności.
- Podpis**: Gwarantuje integralność Invoice poprzez uwierzytelnienie wszystkich informacji.


Faktury są następnie kodowane w **bech32**, takim samym formacie jak dla adresów Bitcoin SegWit (format zaczynający się od `bc1`).


### Wycofanie LNURL


W tradycyjnej transakcji, takiej jak zakup w sklepie, Invoice jest generowany dla całkowitej kwoty do zapłaty. Po przedstawieniu Invoice (w postaci kodu QR lub ciągu znaków) klient może go zeskanować i sfinalizować transakcję. Płatność przebiega następnie zgodnie z tradycyjnym procesem, który przeanalizowaliśmy w poprzedniej sekcji. Jednak proces ten może być czasami bardzo uciążliwy dla użytkownika, ponieważ wymaga od odbiorcy wysłania informacji do nadawcy za pośrednictwem Invoice.


W niektórych sytuacjach, takich jak wypłata bitcoinów z usługi online, tradycyjny proces jest zbyt uciążliwy. W takich przypadkach rozwiązanie do wypłat **LNURL** upraszcza ten proces, wyświetlając kod QR, który skanuje Wallet odbiorcy, aby automatycznie utworzyć Invoice. Następnie usługa płaci Invoice, a użytkownik po prostu widzi natychmiastową wypłatę.


![LNP201](assets/en/69.webp)


LNURL to protokół komunikacyjny, który określa zestaw funkcji zaprojektowanych w celu uproszczenia interakcji między węzłami Lightning i klientami, a także aplikacjami innych firm. Wycofanie LNURL, jak właśnie widzieliśmy, jest więc tylko jednym z przykładów wśród innych funkcjonalności.

Protokół ten opiera się na protokole HTTP i umożliwia tworzenie linków do różnych operacji, takich jak żądanie płatności, żądanie wypłaty lub inne funkcje, które poprawiają komfort użytkowania. Każdy LNURL to zakodowany w bech32 adres URL z prefiksem lnurl, który po zeskanowaniu uruchamia serię automatycznych działań na Lightning Wallet.

Na przykład funkcja LNURL-withdraw (LUD-03) umożliwia wypłacanie środków z usługi poprzez zeskanowanie kodu QR, bez konieczności ręcznego generate i Invoice. Podobnie, LNURL-auth (LUD-04) umożliwia logowanie się do usług online przy użyciu klucza prywatnego na urządzeniu Lightning Wallet zamiast hasła.


### Wysyłanie płatności błyskawicznej bez Invoice: Keysend


Innym interesującym przypadkiem jest transfer środków bez wcześniejszego otrzymania Invoice, znany jako "**Keysend**". Protokół ten umożliwia wysyłanie środków poprzez dodanie obrazu wstępnego do zaszyfrowanych danych płatności, dostępnych tylko dla odbiorcy. Ten obraz wstępny umożliwia odbiorcy odblokowanie HTLC, a tym samym odzyskanie środków bez wcześniejszego wygenerowania Invoice.


Dla uproszczenia, w tym protokole to nadawca generuje sekret używany w HTLC, a nie odbiorca. W praktyce pozwala to nadawcy na dokonanie płatności bez konieczności wcześniejszej interakcji z odbiorcą.


![LNP201](assets/en/70.webp)


**Co powinieneś wynieść z tego rozdziału?



- **Lightning Invoice** to żądanie płatności składające się z części czytelnej dla człowieka i części zawierającej dane maszynowe.
- Invoice jest zakodowany w **bech32**, z separatorem `1` ułatwiającym kopiowanie i częścią danych zawierającą wszystkie informacje niezbędne do przetworzenia płatności.
- W Lightning istnieją inne procesy płatności, w szczególności **LNURL-Withdraw** w celu ułatwienia wypłat oraz **Keysend** do bezpośrednich przelewów bez Invoice.


W następnym rozdziale zobaczymy, jak operator węzła może zarządzać płynnością w swoich kanałach, aby nigdy nie zostać zablokowanym i zawsze móc wysyłać i odbierać płatności na Lightning Network.


## Zarządzanie płynnością


<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>


:::video id=96096aef-e4ce-4c44-a022-57e27082232a:::


W tym rozdziale omówimy strategie skutecznego zarządzania płynnością na Lightning Network. Zarządzanie płynnością różni się w zależności od typu użytkownika i kontekstu. Przyjrzymy się głównym zasadom i istniejącym technikom, aby lepiej zrozumieć, jak zoptymalizować to zarządzanie.


### Potrzeby w zakresie płynności


Istnieją trzy główne profile użytkowników Lightning, z których każdy ma określone potrzeby w zakresie płynności:



- Płatnik**: Jest to osoba, która dokonuje płatności. Potrzebują płynności wychodzącej, aby móc przekazywać środki innym użytkownikom. Może to być na przykład konsument.
- Sprzedawca (lub odbiorca płatności)**: Jest to osoba, która otrzymuje płatności. Potrzebują płynności przychodzącej, aby móc akceptować płatności do swojego węzła. Może to być na przykład firma lub sklep internetowy.
- Router**: Węzeł pośredniczący, często specjalizujący się w przekierowywaniu płatności, który musi zoptymalizować swoją płynność w każdym kanale, aby przekierować jak najwięcej płatności i zarobić na opłatach.


Profile te nie są oczywiście stałe; użytkownik może przełączać się między płatnikiem a odbiorcą w zależności od transakcji. Przykładowo, Bob może otrzymywać swoją pensję od swojego pracodawcy, co stawia go w pozycji "sprzedawcy" wymagającego płynności przychodzącej. Następnie, jeśli chce wykorzystać swoją pensję do zakupu żywności, staje się "płatnikiem" i musi mieć płynność wychodzącą.


Aby lepiej to zrozumieć, weźmy przykład prostej sieci składającej się z trzech węzłów: kupującego (Alice), routera (Suzie) i sprzedawcy (Bob).


![LNP201](assets/en/71.webp)


Wyobraźmy sobie, że kupujący chce wysłać 30 000 Sats do sprzedającego i że płatność przechodzi przez węzeł routera. Każda ze stron musi wtedy posiadać minimalną ilość płynności w kierunku płatności:



- Płatnik musi mieć co najmniej 30 000 satoshi po swojej stronie kanału z routerem.
- Sprzedawca musi mieć kanał, w którym 30 000 satoshi znajduje się po przeciwnej stronie, aby móc je odbierać.
- Router musi mieć 30 000 satoshis po stronie płatnika w swoim kanale, a także 30 000 satoshis po swojej stronie w kanale ze sprzedawcą, aby móc przekierować płatność.


![LNP201](assets/en/72.webp)


### Strategie zarządzania płynnością


Płatnicy muszą zapewnić utrzymanie wystarczającej płynności po swojej stronie kanałów, aby zagwarantować płynność wychodzącą. Okazuje się to stosunkowo proste, ponieważ wystarczy otworzyć nowe kanały Lightning, aby mieć tę płynność. Rzeczywiście, początkowe środki zablokowane w Multisig On-Chain są całkowicie po stronie płatnika w kanale Lightning na początku. Zdolność płatnicza jest zatem zapewniona tak długo, jak długo kanały są otwarte z wystarczającą ilością środków. Gdy płynność wychodząca zostanie wyczerpana, wystarczy otworzyć nowe kanały.

Z drugiej strony, dla sprzedawcy zadanie jest bardziej złożone. Aby móc otrzymywać płatności, muszą mieć płynność po przeciwnej stronie swoich kanałów. Dlatego otwarcie kanału nie wystarczy: muszą oni również dokonać płatności w tym kanale, aby przenieść płynność na drugą stronę, zanim będą mogli sami otrzymywać płatności. W przypadku niektórych profili użytkowników Lightning, takich jak handlowcy, istnieje wyraźna dysproporcja między tym, co ich węzeł wysyła, a tym, co otrzymuje, ponieważ celem firmy jest przede wszystkim zebranie więcej niż wydaje, aby generate przyniósł zysk. Na szczęście dla tych użytkowników z określonymi potrzebami w zakresie płynności przychodzącej istnieje kilka rozwiązań:



- Przyciąganie kanałów**: Sprzedawca korzysta z przewagi wynikającej z wolumenu płatności przychodzących oczekiwanych na jego węźle. Biorąc to pod uwagę, mogą próbować przyciągnąć węzły routingu, które szukają dochodu z opłat transakcyjnych i które mogą otworzyć kanały w ich kierunku, mając nadzieję na przekierowanie ich płatności i pobranie powiązanych opłat.



- Ruch płynności**: Sprzedający może również otworzyć kanał i przenieść część środków na przeciwną stronę, dokonując fikcyjnych płatności na rzecz innego węzła, który zwróci pieniądze w inny sposób. W następnej części zobaczymy, jak przeprowadzić tę operację.



- Otwarcie trójkątne**: Istnieją platformy dla węzłów, które chcą wspólnie otwierać kanały, umożliwiając każdemu z nich czerpanie korzyści z natychmiastowej płynności przychodzącej i wychodzącej. Na przykład [LightningNetwork+](https://lightningnetwork.plus/) oferuje taką usługę. Jeśli Alice, Bob i Suzie chcą otworzyć kanał ze 100 000 Sats, mogą uzgodnić na tej platformie, że Alice otworzy kanał w kierunku Boba, Bob w kierunku Suzie, a Suzie w kierunku Alice. W ten sposób każdy z nich ma 100 000 Sats płynności wychodzącej i 100 000 Sats płynności przychodzącej, a jednocześnie ma zablokowane tylko 100 000 Sats.


![LNP201](assets/en/73.webp)



- Kupowanie kanałów**: Istnieją również usługi wynajmu kanałów Lightning w celu uzyskania przychodzącej płynności, takie jak [Bitrefill Thor](https://www.bitrefill.com/thor-lightning-network-channels/) lub [Lightning Labs Pool](https://lightning.engineering/pool/). Na przykład Alice może kupić kanał o wartości miliona satoshi do swojego węzła, aby móc otrzymywać płatności.


![LNP201](assets/en/74.webp)


Wreszcie, routery, których celem jest maksymalizacja liczby przetwarzanych płatności i pobieranych opłat, muszą:



- Otwórz dobrze finansowane kanały ze strategicznymi węzłami.
- Regularne dostosowywanie dystrybucji środków w kanałach do potrzeb sieci.


### Usługa Loop Out


Usługa [Loop Out](https://lightning.engineering/loop/), oferowana przez Lightning Labs, pozwala na przeniesienie płynności na przeciwną stronę kanału, jednocześnie odzyskując środki na Bitcoin Blockchain. Na przykład Alice wysyła 1 milion satoshi za pośrednictwem Lightning do węzła pętli, który następnie zwraca jej te środki w bitcoinach On-Chain. Równoważy to jej kanał z 1 milionem satoshi po każdej stronie, optymalizując jej zdolność do otrzymywania płatności.


![LNP201](assets/en/75.webp)


Dlatego usługa ta umożliwia przychodzącą płynność podczas odzyskiwania bitcoinów On-Chain, co pomaga ograniczyć unieruchomienie gotówki potrzebnej do akceptowania płatności za pomocą Lightning.


**Co powinieneś wynieść z tego rozdziału?



- Aby wysyłać płatności na Lightning, musisz mieć wystarczającą płynność po swojej stronie w swoich kanałach. Aby zwiększyć tę zdolność wysyłania, wystarczy otworzyć nowe kanały.
- Aby otrzymywać płatności, musisz mieć płynność po przeciwnej stronie w swoich kanałach. Zwiększenie tej zdolności odbiorczej jest bardziej złożone, ponieważ wymaga od innych otwarcia kanałów w twoim kierunku lub dokonania (fikcyjnych lub rzeczywistych) płatności w celu przeniesienia płynności na drugą stronę.
- Utrzymanie płynności tam, gdzie jest to pożądane, może być jeszcze trudniejsze w zależności od wykorzystania kanałów. Dlatego istnieją narzędzia i usługi, które pomagają zrównoważyć kanały zgodnie z potrzebami.


W następnym rozdziale proponuję przegląd najważniejszych koncepcji tego szkolenia.


# Idź dalej


<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>


## Podsumowanie kursu



<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>


:::video id=5f4f4344-ef27-4765-8f09-8262e6833bde:::


W tym ostatnim rozdziale, oznaczającym koniec szkolenia LNP201, proponuję powrócić do ważnych koncepcji, które wspólnie omówiliśmy.


Celem tego szkolenia było zapewnienie kompleksowego i technicznego zrozumienia Lightning Network. Odkryliśmy, w jaki sposób Lightning Network opiera się na Bitcoin Blockchain w celu wykonywania transakcji off-chain, zachowując jednocześnie podstawowe cechy Bitcoin, w szczególności brak potrzeby ufania innym węzłom.


### Kanały płatności


W początkowych rozdziałach zbadaliśmy, w jaki sposób dwie strony, otwierając kanał płatności, mogą przeprowadzać transakcje poza Bitcoin Blockchain. Oto omówione kroki:



- Otwarcie kanału**: Utworzenie kanału odbywa się za pośrednictwem transakcji Bitcoin, która blokuje środki w wielopodpisowym Address 2/2. Depozyt ten reprezentuje kanał Lightning na Blockchain.


![LNP201](assets/en/76.webp) 2. **Transactions in the Channel**: In this channel, it is then possible to carry out numerous transactions without having to publish them on the blockchain. Each Lightning transaction creates a new state of the channel reflected in a commitment transaction.

![LNP201](assets/en/77.webp)



- Zabezpieczenie i zamknięcie**: Uczestnicy zobowiązują się do nowego stanu kanału poprzez wymianę kluczy odwołania, aby zabezpieczyć środki i zapobiec wszelkim oszustwom. Obie strony mogą wspólnie zamknąć kanał, dokonując nowej transakcji na Bitcoin Blockchain lub w ostateczności poprzez wymuszone zamknięcie. Ta ostatnia opcja, choć mniej wydajna, ponieważ jest dłuższa i czasami słabo oceniana pod względem opłat, nadal pozwala na odzyskanie środków. W przypadku oszustwa ofiara może ukarać oszusta, odzyskując wszystkie środki z kanału na Blockchain.


![LNP201](assets/en/78.webp)


### Sieć kanałów


Po zbadaniu izolowanych kanałów, rozszerzyliśmy naszą analizę na sieć kanałów:



- Routing**: Gdy dwie strony nie są bezpośrednio połączone kanałem, sieć umożliwia routing przez węzły pośredniczące. Płatności są następnie przekazywane z jednego węzła do drugiego.


![LNP201](assets/en/79.webp)



- HTLC**: Płatności przechodzące przez węzły pośredniczące są zabezpieczone przez "_Hash Time-Locked Contracts_" (HTLC), które pozwalają na zablokowanie środków do momentu zakończenia płatności od końca do końca.


![LNP201](assets/en/80.webp)



- Routing cebulowy**: Aby zapewnić poufność płatności, routing cebulowy maskuje ostateczne miejsce docelowe przed węzłami pośredniczącymi. Węzeł wysyłający musi zatem obliczyć całą trasę, ale w przypadku braku pełnych informacji na temat płynności kanałów, przechodzi przez kolejne próby, aby skierować płatność.


![LNP201](assets/en/81.webp)


### Zarządzanie płynnością


Widzieliśmy, że zarządzanie płynnością jest wyzwaniem dla Lightning, aby zapewnić płynny przepływ płatności. Wysyłanie płatności jest stosunkowo proste: wymaga jedynie otwarcia kanału. Jednak otrzymywanie płatności wymaga posiadania płynności po przeciwnej stronie swoich kanałów. Oto kilka omówionych strategii:



- Przyciąganie kanałów**: Zachęcając inne węzły do otwierania kanałów do siebie, użytkownik uzyskuje przychodzącą płynność.



- Przenoszenie płynności**: Wysyłając płatności do innych kanałów, płynność przenosi się na przeciwną stronę.


![LNP201](assets/en/82.webp)



- Korzystanie z usług takich jak Loop i Pool**: Usługi te umożliwiają równoważenie lub kupowanie kanałów z płynnością po przeciwnej stronie.

![LNP201](assets/en/83.webp)


- Wspólne otwarcia**: Dostępne są również platformy do łączenia się w celu wykonywania otwarć trójkątnych i posiadania płynności przychodzącej.


![LNP201](assets/en/84.webp)


# Sekcja końcowa


<partId>b8715c1c-7ae2-49b7-94c7-35bf85346ad3</partId>


## Recenzje i oceny


<chapterId>38814c99-eb7b-5772-af49-4386ee2ce9b0</chapterId>

<isCourseReview>true</isCourseReview>

## Egzamin końcowy


<chapterId>7ed33400-aef7-5f3e-bfb1-7867e445d708</chapterId>

<isCourseExam>true</isCourseExam>

## Wnioski


<chapterId>afc0d72b-4fbc-5893-90b2-e27fb519ad02</chapterId>

<isCourseConclusion>true</isCourseConclusion>