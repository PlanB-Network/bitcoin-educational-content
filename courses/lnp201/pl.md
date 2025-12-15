---
name: Teoria Lightning Network
goal: Odkryj sieć Lightning z technicznego punktu widzenia
objectives:
- Zrozumienie działania kanałów sieciowych.
- Zapoznaj się z terminami HTLC, LNURL i UTXO.
- Asymilacja zarządzania płynnością i opłat LNN.
- Rozpoznanie Lightning Network jako sieci.
- Zrozumienie teoretycznych zastosowań sieci Lightning.
---

# Podróż do drugiej warstwy Bitcoina


Zanurz się w sercu sieci Lightning, systemu niezbędnego dla przyszłych transakcji w sieci Bitcoin. LNP201 to kurs teoretyczny na temat technicznego działania sieci Lightning. Odkrywa podstawy i mechanizmy tej drugiej warstwy sieci, zaprojektowanej tak, aby płatności w sieci Bitcoin były szybkie, ekonomiczne i skalowalne.


Dzięki sieci kanałów płatności sieć Lightning umożliwiają szybkie i bezpieczne transakcje bez konieczności rejestrowania każdej wymiany w łańcuchu bloków. W kolejnych rozdziałach dowiesz się, jak działa otwieranie i zamykanie kanałów oraz zarządzanie nimi, w jaki sposób płatności są bezpiecznie kierowane przez węzły pośredniczące przy jednoczesnym zminimalizowaniu potrzeby zaufania oraz jak zarządzać płynnością. Dowiesz się, czym są transakcje zobowiązujące, HTLC (kontrakty haszowe z blokadą czasową), klucze unieważniające, mechanizmy karzące, routowanie warstwowe i faktury.


Niezależnie od tego, czy jesteś początkującym, czy bardziej doświadczonym użytkownikiem Bitcoina, ten kurs dostarczy ci cennych informacji, abyś mógł zrozumieć sieć Lightning i jej używać. Chociaż w pierwszych częściach omówimy niektóre podstawy działania Bitcoina, ważne jest, aby opanować podstawy wynalazku satówego przed zanurzeniem się w kurs LNP201.


Miłego odkrywania!


+++

# Wprowadzenie

<partId>9da7290a-3895-49a2-93ea-2a6272ca4af4</partId>


## Przegląd kursu

<chapterId>f2e71062-5121-4114-a7f8-27df69884ce8</chapterId>


Witamy na kursie LNP201!


Nasze szkolenie ma na celu zapewnienie dogłębnego technicznego zrozumienia sieci Lightning, sieci nakładkowej zaprojektowanej w celu ułatwienia szybkich i często tanich transakcji w sieci Bitcoin. Stopniowo odkryjesz podstawowe koncepcje rządzące tym systemem, od otwierania kanałów płatności po techniki routingu i zarządzanie płynnością.


**Sekcja 1: Podstawy**

Zaczniemy od ogólnego wprowadzenia do sieci Lightning, opisując niezbędne podstawy dotyczące Bitcoina, jego adresów, UTXO i sposobu działania transakcji. Ten podstawowy przegląd jest niezbędny do zrozumienia, w jaki sposób sieć Lightning, aby działać bezpiecznie, opiera się na podstawowych mechanizmach łańcucha bloków.


**Sekcja 2: Otwieranie i zamykanie kanałów**

W tej sekcji zbadamy proces otwierania kanału, który jest kamieniem węgielnym sieci Lightning. Dowiesz się, w jaki sposób tworzone są transakcje zobowiązujące, jaka jest rola kluczy unieważniających dla bezpieczeństwa i w jaki sposób kanały mogą być zamykane wspólnie lub jednostronnie. Każdy krok zostanie wyjaśniony precyzyjnie i technicznie, aby pomóc ci zrozumieć wszystkie subtelności.


**Sekcja 3: Sieć płynności**

Sieć Lightning nie ogranicza się do pojedynczych kanałów; to prawdziwa sieć płatności. Zobaczymy, jak transakcje mogą być kierowane przez węzły pośredniczące za pomocą HTLC. W tej sekcji przedstawimy również wyzwania związane z płynnością przychodzącą i wychodzącą.


**Sekcja 4: Narzędzia wykorzystywane w sieci Lightning**

W tej sekcji przedstawiono praktyczne narzędzia wykorzystywane w sieci Lightning, takie jak *Invoices*, *LNURL* i *Keysend*. Dowiesz się również, jak zarządzać płynnością swoich kanałów, co jest istotnym aspektem zapewniającym płynność płatności i maksymalizującym wydajność transakcji w sieci Lightning.


**Sekcja 5: Dalej**

Na koniec szkolenia podsumujemy omówione koncepcje i utorujemy drogę bardziej zaawansowanym tematom dla tych, którzy chcą pogłębić swoją wiedzę na temat sieci Lightning.


Gotowy do odkrycia technicznych mechanizmów sieci Lightning? Zaczynajmy!


---

*Oto kilka terminów, które napotkasz na schematach kursu w języku angielskim, wraz z ich tłumaczeniem, aby pomóc ci lepiej je zrozumieć w twoim języku:*

| Angielski          | Tłumaczenie - wyjaśnienie     |
| ------------------ | ----------------------------- |
| *timelock*         | Blokada czasowa               |
| *Revocation Key*   | Klucz odwołania               |
| *invoice*          | Faktura / żądanie płatności   |
| *sig* (signature)  | Podpis                        |
| *secret*           | Sekret                        |
| *amount*           | Kwota                         |
| *scan QR code*     | Zeskanuj kod QR               |
| *Show QR code*     | Pokaż kod QR                  |
| *Asks the invoice* | Prosi o fakturę               |
| *Give the invoice* | Dostarcza fakturę             |
| *Payment*          | Płatność                      |
| *Preimage*         | Przedobraz                    |

# Podstawy


<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>


## Zrozumienie sieci Lightning


<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>


:::video id=4315a277-12fe-4946-bb49-a807e60c09a7:::



Lightning Network to sieć kanałów płatności zbudowana w oparciu o protokół Bitcoin, mająca na celu umożliwienie szybkich i tanich transakcji. Umożliwia tworzenie kanałów płatności między uczestnikami, w ramach których transakcje mogą być dokonywane niemal natychmiast i przy minimalnych opłatach, bez konieczności rejestrowania każdej transakcji indywidualnie w łańcuchu bloków. W ten sposób sieć Lightning dąży do poprawy skalowalności Bitcoina i uczynienia go użytecznym do wykonywania płatności o niskiej wartości.


Przed zbadaniem aspektu „sieci” ważne jest, aby zrozumieć koncepcję **kanału płatności** Lightning, to jak działa i jaka jest jego specyfika. Jest to temat naszego pierwszego rozdziału.


### Koncepcja kanału płatności


Kanał płatności pozwala dwóm stronom, nazwanym tutaj **Alicja** i **Bob**, na wymianę funduszy przez sieć Lightning. Każda postać ma węzeł sieci, symbolizowany przez okrąg, a kanał między nimi jest reprezentowany przez odcinek linii.


![LNP201](assets/en/001.webp)


W naszym przykładzie Alicja ma 100 000 satów po swojej stronie kanału, a Bob ma 30 000 satów, co daje łącznie 130 000 satów, co stanowi **przepustowość kanału**.


**Ale czym jest Sat?**


**satów** (lub „sat”) jest jednostką rozliczeniową Bitcoina. Podobnie jak cent dla euro, satów jest po prostu ułamkiem bitcoina. Jeden satów jest równy **0,00000001 bitcoina**, czyli jednej stumilionowej bitcoina. Korzystanie z satów staje się coraz bardziej praktyczne wraz ze wzrostem wartości bitcoina.


### Alokacja funduszy w kanale La Manche


Wróćmy do kanału płatności. Kluczowym pojęciem jest tutaj „**strona kanału**”. Każdy uczestnik ma środki po swojej stronie kanału: Alicja 100 000 satów, a Bob 30 000. Jak widzieliśmy, suma tych środków reprezentuje całkowitą pojemność kanału, liczbę ustaloną w momencie jego otwarcia.


![LNP201](assets/en/002.webp)


Weźmy przykład transakcji Lightning. Jeśli Alicja chce wysłać 40 000 satów do Boba, jest to możliwe, ponieważ ma wystarczającą ilość środków (100 000 satów). Po tej transakcji Alicja będzie miała po swojej stronie 60 000 satów, a Bob 70 000.


![LNP201](assets/en/003.webp)


**Pojemność kanału**, wynosząca 130 000 satów, pozostaje stała. To, co się zmienia, to alokacja środków. System ten nie pozwala na wysyłanie większej ilości środków niż się posiada. Na przykład, jeśli Bob chciałby odesłać Alicji 80 000 satów, nie mógłby, ponieważ ma tylko 70 000.


Inny sposób wyobrażenia sobie alokacji środków to wyobrażenie sobie **kursora**, który wskazuje, gdzie znajdują się środki w kanale. Na początku, gdy Alicja ma 100 000 satów, a Bob 30 000, kursor jest bardziej po stronie Boba, ponieważ Alicja ma znacznie więcej środków. Po transakcji na 40 000 satów kursor przesunie się nieco w stronę Alicji, która teraz posiada 60 000 satów.


![LNP201](assets/en/004.webp)


Ta reprezentacja może być przydatna do wyobrażenia sobie równowagi funduszy w kanale.


### Podstawowe zasady kanału płatności


Pierwszą kwestią do zapamiętania jest to, że **przepustowość kanału** jest stała. Przypomina to nieco średnicę rury: określa maksymalną ilość środków, które można przesłać przez kanał jednocześnie.

Weźmy przykład: jeśli Alicja ma 130 000 satów po swojej stronie, może wysłać Bobowi maksymalnie 130 000 satów w pojedynczej transakcji. Bob może jednak odesłać te środki z powrotem do Alicji, częściowo lub w całości.


Ważne jest, aby zrozumieć, że stała przepustowość kanału ogranicza maksymalną kwotę pojedynczej transakcji, ale nie całkowitą liczbę możliwych transakcji ani ogólny wolumen środków wymienianych w kanale.


**Co powinieneś wynieść z tego rozdziału?**



- Przepustowość kanału jest stała i określa maksymalną kwotę, jaką można przesłać w ramach pojedynczej transakcji.
- Środki w kanale są rozdzielane między dwóch uczestników, a każdy z nich może wysyłać do drugiego tylko te środki, które posiada po swojej stronie.
- Sieć Lightning pozwala zatem na szybką i wydajną wymianę środków, przy jednoczesnym poszanowaniu ograniczeń narzuconych przez przepustowość kanałów.


To koniec pierwszego rozdziału, w którym przedstawiliśmy podstawy sieci Lightning. W kolejnych rozdziałach zobaczymy, jak otworzyć kanał i zgłębimy omawiane tutaj koncepcje.


## Bitcoin, adresy, UTXO i transakcje


<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>


:::video id=75323eef-ea03-45ac-9a6e-46d73ca255de:::


Ten rozdział jest nieco wyjątkowy, ponieważ nie będzie bezpośrednio poświęcony sieci Lightning, ale Bitcoinowi. W rzeczywistości sieć Lightning jest warstwą nałożoną na Bitcoina. Dlatego ważne jest, aby zrozumieć pewne podstawowe koncepcje związane z Bitcoinem, aby w kolejnych rozdziałach właściwie zrozumieć działanie sieci Lightning. W tym rozdziale dokonamy przeglądu podstaw adresów odbiorczych Bitcoina, UTXO, a także funkcjonowania transakcji Bitcoin.


### Adresy Bitcoin, klucze prywatne i klucze publiczne


Adres Bitcoin to seria znaków pochodzących z **klucza publicznego**, który jest obliczany na podstawie **klucza prywatnego**. Jak z pewnością wiesz, jest on używany do blokowania bitcoinów, co jest równoznaczne z otrzymaniem ich w naszym portfelu.


Klucz prywatny jest tajnym elementem, który **nigdy nie powinien być udostępniany**, podczas gdy klucz publiczny i adres mogą być udostępniane bez ryzyka dla bezpieczeństwa (ich ujawnienie stanowi ryzyko jedynie dla prywatności użytkownika). Oto reprezentacja graficzna, którą będzimy posługiwać się podczas tego szkolenia:



- Klucze **prywatne** będą reprezentowane **pionowo**.
- Klucze **publiczne** będą reprezentowane **poziomo**.
- Ich kolor wskazuje, kto je posiada (Alicja na pomarańczowo, Bob na czarno...).


### Transakcje w sieci Bitcoin: Wysyłanie środków i skrypty


Transakcja Bitcoin polega na wysłaniu środków z jednego adresu do drugiego. Weźmy przykład Alicji wysyłającej 0,002 bitcoina do Boba. Alicja używa klucza prywatnego powiązanego z jej adresem, aby **podpisać** transakcję, udowadniając w ten sposób, że rzeczywiście jest w stanie wydać te środki. Ale co dokładnie dzieje się za kulisami tej transakcji? Środki w adresie Bitcoin są zablokowane przez **skrypt**, rodzaj mini-programu, który narzuca pewne warunki wydawania środków.


Najpopularniejszy skrypt wymaga podpisu kluczem prywatnym powiązanym z adresem. Kiedy Alicja podpisuje transakcję swoim kluczem prywatnym, **odblokowuje skrypt**, który blokuje środki, a następnie może je przelać. Transfer środków polega na dodaniu nowego skryptu do tych środków, określającego, że tym razem do ich wydania wymagany będzie podpis kluczem prywatnym **Boba**.


![LNP201](assets/en/005.webp)


### UTXOs: Niewykorzystane środki z poprzednich transakcji


W Bitcoinie to, co faktycznie jest wymieniane, to nie bezpośrednio bitcoiny, ale **UTXOs** (_Unspent Transaction Outputs_), co oznacza „niewydane wyjścia transakcji”.


UTXO to kawałek Bitcoina, który może mieć dowolną wartość, na przykład **2 000 bitcoinów**, **8 bitcoinów**, a nawet **8 000 satów**. Każdy UTXO jest zablokowany przez skrypt i aby go wydać, należy spełnić warunki skryptu, często chodzi o podpis kluczem prywatnym odpowiadający danemu adresowi odbiorcy.


UTXO nie mogą być dzielone. Za każdym razem, gdy są używane do wydania kwoty w bitcoinach, które reprezentują, musi to być zrobione w całości. To trochę jak z banknotem: jeśli masz rachunek na 10 euro i jesteś winien piekarzowi 5 euro, nie możesz po prostu przeciąć rachunku na pół. Musisz dać mu banknot o nominale 10 euro, a on wyda ci 5 euro reszty. UTXO w Bitcoinie działa na dokładnie tej samej zasadzie! Na przykład, gdy Alicja odblokowuje skrypt swoim kluczem prywatnym, odblokowuje cały UTXO. Jeśli chce wysłać tylko część środków reprezentowanych przez ten UTXO do Boba, może „pofragmentować” go na kilka mniejszych. Następnie wyśle 0,0015 BTC do Boba i wyśle pozostałą część, 0,0005 BTC, na **adres zwrotny**.


Oto przykład transakcji z 2 wyjściami:



- UTXO w wysokości 0,0015 BTC dla Boba, zablokowany przez skrypt wymagający podpisu kluczem prywatnym Boba.
- UTXO w wysokości 0,0005 BTC dla Alicji, zablokowany przez skrypt wymagający jej własnego podpisu.


![LNP201](assets/en/006.webp)


### Adresy z wieloma podpisami


Oprócz prostych adresów generowanych z jednego klucza publicznego, możliwe jest tworzenie **adresów wielopodpisowych** z wielu kluczy publicznych. Szczególnie interesującym przypadkiem w sieci Lightning jest **2/2 adres wielopodpisowy**, wygenerowany z dwóch kluczy publicznych:


![LNP201](assets/en/007.webp)


Aby wydać środki zablokowane za pomocą adresu z wieloma podpisami 2/2, konieczne jest podpisanie za pomocą dwóch kluczy prywatnych powiązanych z kluczami publicznymi.


![LNP201](assets/en/008.webp)


Ten typ adresu jest dokładnym odwzorowaniem łańcucha bloków Bitcoina dla kanałów płatności w sieci Lightning.


**Co powinieneś wynieść z tego rozdziału?**



- **Adres Bitcoin** jest wyprowadzany z klucza publicznego, który z kolei jest wyprowadzany z klucza prywatnego.
- Środki w Bitcoinie są blokowane przez **skrypty** i aby je wydać, należy spełnić wymagania skryptu, co zazwyczaj wiąże się z dostarczeniem podpisu z odpowiednim kluczem prywatnym.
- **UTXO** to kawałki bitcoinów zablokowane przez skrypty, a każda transakcja w Bitcoinie polega na odblokowaniu UTXO, a następnie utworzeniu jednego lub więcej nowych UTXO w jego miejsce.
- **Adresy wielopodpisowe 2/2** wymagają podpisu dwóch kluczy prywatnych w celu wydania środków. Te konkretne adresy są używane w sieci Lightning do tworzenia kanałów płatności.


Niniejszy rozdział poświęcony Bitcoinowi pozwolił nam zapoznać się z kilkoma istotnymi pojęciami. W następnym rozdziale dowiemy się, jak działa otwieranie kanałów w sieci Lightning.


# Otwieranie i zamykanie kanałów


<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>


## Otwarcie kanału


<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>


:::video id=6098fee1-735e-4d8d-9f57-0faf5fef6d76:::


W tym rozdziale zobaczymy dokładniej, jak otworzyć kanał płatności w sieci Lightning i zrozumiemy związek między tą operacją a bazowym systemem Bitcoina.


### Kanały sieci Lightining


Jak widzieliśmy w pierwszym rozdziale, **kanał płatności** w sieci Lightning można porównać do „rury” do wymiany środków między dwoma uczestnikami (**Alicja** i **Bob** w naszych przykładach). Przepustowość tego kanału odpowiada sumie dostępnych środków po każdej ze stron. W naszym przykładzie Alicja ma **100 000 satów**, a Bob ma **30 000 satów**, co daje **całkowitą przepustowość** wynoszącą **130 000 satów**.


![LNP201](assets/en/009.webp)


### Poziomy wymiany informacji


Kluczowe jest wyraźne rozróżnienie różnych poziomów wymiany w sieci Lightning:



- **Komunikacja peer-to-peer (protokół Lightning)**: Są to wiadomości, które węzły Lightning wysyłają do siebie nawzajem w celu komunikacji. Na naszych diagramach będziemy reprezentować te wiadomości przerywanymi czarnymi liniami.
- **Kanały płatności (protokół Lightning)**: Są to ścieżki wymiany środków w sieci Lightning, które przedstawimy za pomocą ciągłych czarnych linii.
- **Transakcje w sieci Bitcoin (protokół Bitcoin)**: Są to transakcje dokonywane w łańcuchu bloków, które przedstawimy za pomocą pomarańczowych linii.


![LNP201](assets/en/010.webp)


Warto zauważyć, że węzeł Lightning może komunikować się za pośrednictwem protokołu P2P bez otwierania kanału, ale do wymiany funduszy niezbędny jest kanał.


### Kroki otwierania kanału Lightning



- **Wymiana wiadomości**: Alicja chce otworzyć kanał z Bobem. Wysyła mu wiadomość zawierającą kwotę, którą chce zdeponować w kanale (130 000 satów) oraz swój klucz publiczny. Bob odpowiada, udostępniając swój klucz publiczny.


![LNP201](assets/en/011.webp)



- **Utworzenie adresu wielopodpisowego**: Za pomocą tych dwóch kluczy publicznych Alicja tworzy **2/2 adresy wielopodpisowe**, co oznacza, że środki, które zostaną później zdeponowane pod tym adresem, będą wymagały obu podpisów (Alicji i Boba) do wykonania transakcji.


![LNP201](assets/en/012.webp)



- **Transakcja wpłaty**: Alicja przygotowuje transakcję w sieci Bitcoin, aby zdeponować środki pod tym adresem wielopodpisowym. Na przykład, może zdecydować o wysłaniu na ten adres **130 000 satów**. Ta transakcja jest **stworzona, ale jeszcze nie opublikowana** w łańcuchu bloków.


![LNP201](assets/en/013.webp)



- **Transakcja wypłaty**: Przed opublikowaniem transakcji wpłaty, Alicja tworzy transakcję wypłaty, aby mogła odzyskać swoje środki w przypadku problemu z Bobem. W rzeczywistości, gdy Alicja opublikuje transakcję wpłaty, jej saty zostaną zablokowane pod adresem z wieloma podpisami 2/2, który do odblokowania wymaga zarówno jej podpisu, jak i podpisu Boba. Alicja chroni się przed ryzykiem, tworząc transakcję wypłaty, która pozwala jej odzyskać środki.


![LNP201](assets/en/014.webp)



- **Podpis Boba**: Alicja wysyła transakcję wpłaty do Boba jako dowód i prosi go o podpisanie transakcji wypłaty. Po uzyskaniu podpisu Boba na transakcji wypłaty, Alicja ma pewność, że będzie w stanie odzyskać swoje środki w dowolnym momencie, ponieważ do odblokowania adresu wielopodpisowego potrzebny jest teraz tylko jej własny podpis.


![LNP201](assets/en/015.webp)



- **Publikacja transakcji wpłaty**: Po uzyskaniu podpisu Boba, Alicja może opublikować transakcję wpłaty w łańcuchu bloków Bitcoina, tym samym oficjalnie otwierając kanał Lightning między dwoma użytkownikami.


![LNP201](assets/en/016.webp)


### Kiedy kanał jest otwarty?


Kanał uznaje się za otwarty, gdy transakcja wpłaty zostanie uwzględniona w bloku Bitcoina i osiągnie określoną głębokość potwierdzeń (liczbę kolejnych bloków).


**Co powinieneś zapamiętać z tego rozdziału?**



- Otwarcie kanału rozpoczyna się od wymiany **komunikatów** między dwiema stronami (wymiany kwot i kluczy publicznych).
- Kanał jest tworzony poprzez utworzenie **2/2 adresu wielopodpisowego** i zdeponowanie w nim środków za pośrednictwem transakcji w sieci Bitcoin.
- Osoba otwierająca kanał zapewnia sobie możliwość **odzyskania swoich środków** poprzez utworzenie transakcji wypłaty podpisaną przez drugą stronę przed opublikowaniem transakcji wpłaty.


W następnym rozdziale zbadamy techniczne działanie transakcji w kanale sieci Lightning.


## Transakcja zobowiązująca


<chapterId>7d3fd135-129d-5c5a-b306-d5f2f1e63340</chapterId>


:::video id=c17454f3-14c5-47a0-8c9c-42ee12932bd3:::


W tym rozdziale odkryjemy techniczne funkcjonowanie przepływu transakcji w kanale sieci Lightning, czyli sytuacji gdy środki są przenoszone z jednej strony kanału na drugą.


### Przypomnienie cyklu życia kanału


Jak widzieliśmy wcześniej, kanał Lightning rozpoczyna się od **otwarcia** transakcji w sieci Bitcoin. Kanał może zostać **zamknięty** w dowolnym momencie, również za pośrednictwem transakcji w sieci Bitcoin. Pomiędzy tymi dwoma momentami można wykonać prawie nieskończoną liczbę transakcji w kanale, bez przechodzenia przez łańcuch bloków Bitcoina. Zobaczmy, co dzieje się w kanale podczas transakcji.


![LNP201](assets/en/017.webp)


### Początkowy stan kanału


W momencie otwarcia kanału Alicja zdeponowała **130 000 satów** pod adresem wielopodpisowym kanału. Tak więc w stanie początkowym wszystkie środki są po stronie Alicji. Przed otwarciem kanału Alicja poprosiła Boba o podpisanie **transakcji wypłaty**, która pozwoliłaby jej odzyskać środki, gdyby chciała zamknąć kanał.


![LNP201](assets/en/018.webp)


### Niepublikowane transakcje: transakcje zobowiązujące


Kiedy Alicja dokonuje transakcji w kanale, aby wysłać środki do Boba, tworzona jest nowa transakcja w sieci Bitcoin, aby odzwierciedlić tę zmianę w dystrybucji środków. Transakcja ta, zwana **transakcją zobowiązującą**, nie jest publikowana w łańcuchu bloków, ale reprezentuje nowy stan kanału po transakcji w sieci Lightning.


Weźmy przykład z Alicją wysyłającą 30 000 satów do Boba:



- **Początkowo**: Alicja ma 130 000 satów.
- **Po transakcji**: Alicja ma 100 000 satów, a Bob 30 000 satów.

Aby zweryfikować ten transfer, Alicja i Bob tworzą nową **nieopublikowaną transakcję w sieci Bitcoin**, która z adresu wielopodpisowego wysyła **100 000 satów do Alicji** i **30 000 satów do Boba**. Obie strony tworzą tę transakcję niezależnie, ale z tymi samymi danymi (kwoty i adresy). Po utworzeniu transakcji, każda ze stron ją podpisuje i wymienia swój podpis z drugą stroną. Pozwala to każdej ze stron na opublikowanie transakcji w dowolnym momencie, jeśli jest to konieczne, aby odzyskać swój udział w kanale w głównym łańcuchu bloków Bitcoina.

![LNP201](assets/en/019.webp)


### Proces przelewania środków: Faktura


Kiedy Bob chce otrzymać środki, wysyła Alicji **_fakturę_** na 30 000 satów. Alicja następnie płaci tę fakturę, rozpoczynając transfer w kanale. Jak widzieliśmy, proces ten opiera się na utworzeniu i podpisaniu nowej **transkacji zobowiązującej**.


Każda transakcja zobowiązująca reprezentuje nowy podział środków w kanale po transferze. W tym przykładzie po transakcji Bob ma 30 000 satów, a Alicja 100 000 satów. Jeśli którykolwiek z dwóch uczestników zdecyduje się opublikować transakcję zobowiązującą w łańcuchu bloków, spowoduje to zamknięcie kanału, a środki zostaną rozdzielone zgodnie z ostatnią dystrybucją.


![LNP201](assets/en/020.webp)


### Nowy stan po drugiej transakcji


Weźmy inny przykład: po pierwszej transakcji, w której Alicja wysłała Bobowi 30 000 satów, Bob decyduje się wysłać **10 000 satów z powrotem do Alicji**. Tworzy to nowy stan kanału. Nowa **transakcja zobowiązująca** będzie reprezentowała tę zaktualizowaną dystrybucję:



- **Alicja** ma teraz **110 000 satów**.
- **Bob** ma **20 000 satów**.


![LNP201](assets/en/021.webp)


Ponownie, transakcja ta nie jest publikowana w łańcuchu bloków, ale może zostać opublikowana w dowolnym momencie poprzez zamknięcie kanału.


Podsumowując, gdy środki są przesyłane w ramach kanału sieci Lightning:



- Alicja i Bob tworzą nową **transkację zobowiązującą**, która odzwierciedla nowy podział środków.
- Ta transakcja w sieci Bitcoin jest **podpisana** przez obie strony, ale **nie jest publikowana** w łańcuchu bloków, dopóki kanał pozostaje otwarty.
- Transkacje zobowiązujące zapewniają, że każdy uczestnik może odzyskać swoje środki w łańcuchu bloków w dowolnym momencie, publikując ostatnią podpisaną transakcję.


System ten ma jednak potencjalną wadę, którą omówimy w następnym rozdziale. Zobaczymy, jak każdy uczestnik może zabezpieczyć się przed próbą oszustwa ze strony drugiej strony.


## Klucz odwołania


<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>

:::video id=1d850f23-eff1-4725-b284-ce12456a2c26:::

W tym rozdziale zagłębimy się w to, jak działają transakcje w sieci Lightning, omawiając mechanizmy ochrony przed oszustwami, zapewniając, że każda ze stron przestrzega zasad w kanale.


### Przypomnienie: transakcje zobowiązujące


Jak wspomniano wcześniej, transakcje w sieci Lightning opierają się na niepublikowanych **transakcjach zobowiązujących**. Transakcje te odzwierciedlają bieżącą dystrybucję środków w kanale. Kiedy dokonywana jest nowa transakcja w sieci Lightning, tworzony jest nowa transakcja zobowiązująca podpisywana przez obie strony, aby odzwierciedlić nowy stan kanału.


Weźmy prosty przykład:



- **Stan początkowy**: Alicja ma **100 000 satów**, Bob **30 000 satów**.
- Po transakcji, w której Alicja wysyła Bobowi **40 000 satów**, nowa transakcja zobowiązująca rozdziela środki w następujący sposób:
  - Alicja: **60,000 satów**
  - Bob: **70,000 satów**


![LNP201](assets/en/022.webp)


W dowolnym momencie obie strony mogą opublikować **najnowszą transakcję zobowiązującą** podpisaną w celu zamknięcia kanału i odzyskania środków.


### Wada: oszukiwanie poprzez publikowanie starych transakcji


Potencjalny problem pojawia się, gdy jedna ze stron zdecyduje się **oszukać**, publikując starą transakcję zobowiązującą. Na przykład, Alicja może opublikować starszą transakcję zobowiązującą, w której miała **100 000 satów**, mimo że w rzeczywistości ma tylko **60 000**. To pozwoliłoby jej ukraść Bobowi **40 000 satów**.


![LNP201](assets/en/023.webp)


Co gorsza, Alicja mogła opublikować pierwszą transakcję wypłaty, tę przed otwarciem kanału, w której miała **130 000 satów**, a tym samym ukraść wszystkie fundusze z kanału.


![LNP201](assets/en/024.webp)


### Rozwiązanie: klucz odwołania i blokada czasowa


Aby zapobiec tego rodzaju oszustwom ze strony Alicji, w sieci Lightning do transakcji zobowiązujących dodawane są **mechanizmy bezpieczeństwa**:



- **Blokada czasowa**: Każda transakcja zobowiązująca zawiera blokadę czasową środków Alicji. Blokada czasowa jest prymitywem (podstawowym elementem) kontraktu smart, który ustawia warunek czasowy, który musi zostać spełniony, aby transakcja została dodana do bloku. Oznacza to, że Alicja nie może odzyskać swoich środków, dopóki nie minie określona liczba bloków, jeśli opublikuje jedną z transakcji zobowiązujących. Ta blokada czasowa zaczyna obowiązywać od potwierdzenia transakcji zobowiązującej. Czas jej trwania jest zasadniczo proporcjonalny do wielkości kanału, ale można go również skonfigurować ręcznie.
- **Klucz odwołania**: Środki Alicji mogą być również natychmiast wydane przez Boba, jeśli posiada on **klucz odwołania**. Klucz ten składa się z sekretu posiadanego przez Alicję i sekretu posiadanego przez Boba. Należy pamiętać, że ten sekret jest inny dla każdej transakcji zobowiązującej.

Dzięki tym dwóm połączonym mechanizmom Bob ma czas na wykrycie próby oszustwa Alicji i ukaranie jej poprzez odzyskanie swoich danych wyjściowych za pomocą klucza unieważniającego, co dla Boba oznacza odzyskanie wszystkich środków z kanału. Nasza nowa transakcjia zobowiązująca będzie teraz wyglądała następująco:


![LNP201](assets/en/025.webp)


Prześledźmy razem działanie tego mechanizmu.


### Proces aktualizacji transakcji


Kiedy Alicja i Bob aktualizują stan kanału za pomocą nowej transakcji w sieci Lightning, wymieniają z wyprzedzeniem swoje **sekrety** dla poprzedniej transakcji zobowiązującej (tej, która stanie się nieaktualna i może pozwolić jednemu z nich oszukiwać). Oznacza to, że przy nowym stanie kanału:



- Alicja i Bob mają nową transakcję zobowiązującą reprezentującą bieżącą dystrybucję środków po transakcji w sieci Lightning.
- Każdy z nich ma sekret drugiej strony dla poprzedniej transakcji, co pozwala im użyć klucza odwołania tylko wtedy, gdy jeden z nich próbuje oszukać, publikując transakcję ze starym stanem w mempoolach węzłów Bitcoina. W rzeczywistości, aby ukarać drugą stronę, konieczne jest posiadanie obu sekretów i transakcji zobowiązującej drugiej strony, która zawiera podpisane dane wejściowe. Bez tej transakcji sam klucz odwołania jest bezużyteczny. Jedynym sposobem na uzyskanie tej transakcji jest pobranie jej z mempooli (w transakcjach oczekujących na potwierdzenie) lub w potwierdzonych transakcjach w łańcuchu bloków podczas blokady czasowej, co dowodzi, że druga strona próbuje oszukiwać, celowo lub nie.


Weźmy przykład, aby dobrze zrozumieć ten proces:



- **Stan początkowy**: Alicja ma **100 000 satów**, Bob **30 000 satów**.


![LNP201](assets/en/026.webp)



- Bob chce otrzymać 40 000 satów od Alicji za pośrednictwem ich kanału Lightning. Aby to zrobić:
   - Wysyła jej fakturę wraz ze swoim sekretem klucza odwołania dla poprzedniej transakcji zobowiązującej.
   - W odpowiedzi Alicja dostarcza swój podpis dla nowej transakcji zobowiązującej Boba, a także swój sekret dla klucza odwołania poprzedniej transakcji.
   - Na koniec Bob wysyła swój podpis dla nowej transakcji zobowiązującej Alicji.
   - Te przelewy pozwalają Alicji wysłać Bobowi **40 000 satów** w sieci Lightning za pośrednictwem ich kanału, a nowe transakcje zobowiązujące odzwierciedlają teraz tę nową dystrybucję środków.


![LNP201](assets/en/027.webp)



- Jeśli Alicja spróbuje opublikować starą transakcję zobowiązującą, w której nadal posiadała **100 000 satów**, Bob, po uzyskaniu klucza unieważnienia, może natychmiast odzyskać środki za pomocą tego klucza, podczas gdy Alicja jest zablokowana przez blokadę czasową.


![LNP201](assets/en/028.webp)


Nawet jeśli w tym przypadku Bob nie ma niczego do zyskania na oszustwie, jeśli i tak to robi, Alicja również korzysta z symetrycznej ochrony oferującej jej takie same gwarancje.


**Co powinieneś wynieść z tego rozdziału?**


Transakcje **zobowiązujące** w sieci Lightning zawierają mechanizmy bezpieczeństwa, które zmniejszają zarówno ryzyko oszustwa, jak i zachęty do jego popełnienia. Przed podpisaniem nowej transakcji zobowiązującej, Alicja i Bob wymieniają swoje **sekrety** dla poprzednich transakcji zobowiązujących. Jeśli Alicja spróbuje opublikować starą transakcje zobowiązującą, Bob może użyć **klucza odwołania**, aby odzyskać wszystkie środki, zanim Alicja to zrobi (ponieważ jest zablokowana przez blokadę czasową), co karze ją za próbę oszustwa.


Ten system bezpieczeństwa zapewnia, że uczestnicy przestrzegają zasad sieci Lightning i nie mogą czerpać korzyści z publikowania starych transakcji zobowiązujących.


Na tym etapie szkolenia wiesz już, w jaki sposób otwierane są kanały Lightning i jak działają transakcje w tych kanałach. W następnym rozdziale odkryjemy różne sposoby zamykania kanału i odzyskiwania bitcoinów na głównym łańcuchu bloków.


## Zamknięcie kanału


<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>


:::video id=4d8ad4e6-32ff-46d3-bd17-343929aa863b:::


W tym rozdziale omówimy **zamykanie kanału** w sieci Lightning, które odbywa się za pośrednictwem transakcji w sieci Bitcoin, podobnie jak otwieranie kanału. Po zapoznaniu się z działaniem transakcji w ramach kanału, nadszedł czas, aby zobaczyć, jak zamknąć kanał i odzyskać środki w łańcuchu bloków Bitcoina.


### Przypomnienie cyklu życia kanału


**Cykl życia kanału** rozpoczyna się od jego **otwarcia**, poprzez transakcję w sieci Bitcoin, następnie dokonywane są w nim transakcje w sieci Lightning, a na koniec, gdy strony chcą odzyskać swoje środki, kanał jest **zamykany** poprzez drugą transakcję w sieci Bitcoin. Transakcje pośrednie dokonywane w sieci Lightning są reprezentowane przez niepublikowane **transakcje zobowiązujące**.


![LNP201](assets/en/029.webp)


### Trzy rodzaje zamknięcia kanału


Istnieją trzy główne sposoby zamknięcia tego kanału, które można nazwać **dobrym, brutalnym i łoterskim** (zainspirowane przez Andreasa Antonopoulosa w _Mastering the Lightning Network_):



- **Dobry**: **wspólne zamknięcie**, w którym Alicja i Bob zgadzają się zamknąć kanał.
- **Zły**: **zamknięcie wymuszone**, w którym jedna ze stron decyduje się na uczciwe zamknięcie kanału, ale bez zgody drugiej strony.
- **Łoterski**: **zamknięcie z oszustwem**, w którym jedna ze stron próbuje ukraść fundusze, publikując starą transakcję zobowiązującą (dowolną, ale nie ostatnią, która odzwierciedla rzeczywisty i sprawiedliwy podział funduszy).


Weźmy przykład:



- Alicja posiada **100 000 satów**, a Bob **30 000 satów**.
- Ta dystrybucja jest odzwierciedlona w **2 transakcjach zobowiązujących** (po jednej na użytkownika), które nie są publikowane, ale mogą zostać opublikowane w przypadku zamknięcia kanału.


![LNP201](assets/en/030.webp)


### Plusy: zamknięcie współpracy


We **wspólnym zamknięciu** Alicja i Bob zgadzają się zamknąć kanał. Oto jak to przebiega:



- Alicja wysyła wiadomość do Boba za pośrednictwem protokołu komunikacyjnego sieci Lightning, aby zaproponować zamknięcie kanału.
- Bob zgadza się, a obie strony nie dokonują dalszych transakcji w kanale.


![LNP201](assets/en/031.webp)



- Alicja i Bob wspólnie negocjują opłaty za **zamknięcie transakcji**. Opłaty te są zazwyczaj obliczane na podstawie rynku opłat Bitcoina w momencie zamknięcia. Ważne jest, aby pamiętać, że **to zawsze osoba, która otworzyła kanał** (Alicja w naszym przykładzie) płaci opłaty za zamknięcie.
- Tworzą nową **transakcję zamykającą**. Transakcja ta przypomina transakcję zobowiązującą, ale bez blokad czasowych lub mechanizmów odwoływania, ponieważ obie strony współpracują i nie ma ryzyka oszustwa. Ta kooperacyjna transakcja zamknięcia różni się zatem od transakcji zobowiązującej.


Na przykład, jeśli Alicja posiada **100 000 satów**, a Bob **30 000 satów**, transakcja zamykająca wyśle **100 000 satów** na adres Alicji i **30 000 satów** na adres Boba, bez ograniczeń czasowych. Po podpisaniu transakcji przez obie strony jest ona publikowana przez Alicję. Gdy transakcja zostanie potwierdzona w łańcuchu bloków Bitcoina, kanał Lightning zostanie oficjalnie zamknięty.


![LNP201](assets/en/032.webp)


**Wspólne zamknięcie** jest preferowaną metodą zamknięcia, ponieważ jest szybkie (bez blokady czasowej), a opłaty transakcyjne są dostosowywane do aktualnych warunków rynkowych Bitcoina. Pozwala to uniknąć płacenia zbyt małej kwoty, co mogłoby grozić zablokowaniem transakcji w mempoolach, lub niepotrzebnego przepłacania, co prowadzi do niepotrzebnych strat finansowych dla uczestników.


### Zły: zamknięcie wymuszone


Gdy węzeł Alicji wyśle wiadomość do węzła Boba z prośbą o zamknięcie współpracy, jeśli ten nie odpowie (na przykład z powodu przerwy w dostępie do Internetu lub problemu technicznego), Alicja może przystąpić do **zamknięcia wymuszonego**, publikując **ostatnio podpisaną transakcję zobowiązującą**.

W tym przypadku Alicja po prostu opublikuje ostatnią transakcję zobowiązującą, która odzwierciedla stan kanału w czasie, gdy miała miejsce ostatnia transakcja Lightning z prawidłową dystrybucją środków.


![LNP201](assets/en/033.webp)


Transakcja ta obejmuje **blokadę czasową** środków Alicji, co spowalnia zamknięcie.


![LNP201](assets/en/034.webp)


Ponadto opłaty za transakcję zobowiązującą mogą być nieodpowiednie w momencie zamknięcia, ponieważ zostały ustalone w momencie tworzenia transakcji, czasami kilka miesięcy wcześniej. Ogólnie rzecz biorąc, klienci sieci Lightning zawyżają opłaty, aby uniknąć przyszłych problemów, ale może to prowadzić do zbyt wysokich opłat lub odwrotnie, zbyt niskich.


Podsumowując, **zamknięcie wymuszone** jest opcją ostateczną, gdy partner przestaje odpowiadać. Jest ono wolniejsze i mniej ekonomiczne niż zamknięcie oparte na współpracy. Dlatego należy go unikać w miarę możliwości.


### Łoterstwo: oszukiwanie


Wreszcie, zamknięcie z **oszustwem** ma miejsce, gdy jedna ze stron próbuje opublikować starą transakcję zobowiązującą, często wtedy, gdy posiadała więcej środków niż powinna. Na przykład Alicja może opublikować starą transakcję, w której posiadała **120 000 satów**, podczas gdy w rzeczywistości posiada tylko **100 000 satów**.


![LNP201](assets/en/035.webp)


Bob, aby zapobiec temu oszustwu, monitoruje łańcuch bloków Bitcoina i jego mempool, aby upewnić się, że Alicja nie opublikuje starej transakcji. Jeśli Bob wykryje próbę oszustwa, może użyć **klucza odwołania**, aby odzyskać środki Alicji i ukarać ją, zabierając wszystkie środki z kanału. Ponieważ Alicja jest zablokowana przez blokadę czasową na swoim wyjściu, Bob ma czas na wydanie środków bez blokady czasowej po swojej stronie, aby odzyskać całą sumę na adres, którego jest właścicielem.


![LNP201](assets/en/036.webp)


Oczywiście oszustwo może potencjalnie zakończyć się sukcesem, jeśli Bob nie podejmie działania w czasie narzuconym przez blokadę czasową wyjścia Alicji. W takim przypadku dane wyjściowe Alicji są odblokowane, co pozwala jej wykorzystać je do utworzenia nowych danych wyjściowych dla kontrolowanego przez nią adresu.


**Co powinieneś wynieść z tego rozdziału?**


Istnieją trzy sposoby zamknięcia kanału:



- **Wspólne zamknięcie**: Szybkie i tańsze rozwiązanie, w którym obie strony zgadzają się zamknąć kanał i opublikować dostosowaną transakcję zamknięcia.
- **Zamknięcie wymuszone**: Mniej pożądane, ponieważ polega na opublikowaniu transakcji zobowiązującej z potencjalnie nieodpowiednimi opłatami i blokadą czasową, co spowalnia zamknięcie.
- **Oszustwo**: Jeśli jedna ze stron próbuje ukraść środki, publikując starą transakcję, druga może użyć klucza unieważnienia, aby ukarać to oszustwo.


W kolejnych rozdziałach zbadamy sieć Lightning z szerszej perspektywy, koncentrując się na tym, jak ona działa.


# Sieć płynności


<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>


## Sieć Lightning


<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>


:::video id=38419c23-5592-4573-b0a7-84824a5bfb77:::


W tym rozdziale zbadamy, w jaki sposób płatności w sieci Lightning mogą dotrzeć do odbiorcy, nawet jeśli uczestnicy transakcji nie są bezpośrednio połączeni kanałem płatności. Sieć Lightning jest bowiem **siecią kanałów płatności**, która umożliwia wysyłanie środków do odległego węzła za pośrednictwem kanałów innych uczestników. Dowiemy się, w jaki sposób płatności są kierowane przez sieć, jak płynność przemieszcza się między kanałami i jak obliczane są opłaty transakcyjne.


### Sieć kanałów płatności


W sieci Lightning transakcja odpowiada transferowi środków między dwoma węzłami. Jak pokazano w poprzednich rozdziałach, konieczne jest otwarcie kanału z kimś, aby wykonać transakcję Lightning. Kanał ten pozwala na niemal nieskończoną liczbę transakcji poza łańcuchem bloków (ang. off-chain) przed jego zamknięciem w celu odzyskania salda w łańcuchu bloków (ang. on-chain). Metoda ta ma jednak tę wadę, że wymaga bezpośredniego kanału z drugą osobą w celu otrzymania lub wysłania środków, co oznacza konieczność utworzenia transakcji otwierającej i zamykającej dla każdego kanału. Jeśli planuję dokonać dużej liczby płatności z tą osobą, otwieranie i zamykanie kanału staje się opłacalne. I odwrotnie, jeśli muszę wykonać tylko kilka transakcji Lightning, otwarcie kanału bezpośredniego nie jest korzystne, ponieważ będzie mnie to kosztować 2 transakcje on-chain dla ograniczonej liczby transakcji off-chain. Taki przypadek może wystąpić na przykład, gdy chcę dokonać jednorazowej płatności za pomocą sieci Lightning u jakiegoś sprzedawcy.


Aby rozwiązać ten problem, sieć Lightning pozwala na przekierowanie płatności przez kilka kanałów i węzłów pośredniczących, umożliwiając w ten sposób transakcję bez bezpośredniego kanału z drugą osobą.


Wyobraźmy sobie za przykład taką sytuację:



- **Alicja** (w kolorze pomarańczowym) ma kanał z **Suzie** (w kolorze szarym) ze **100 000 satów** po swojej stronie i **30 000 satów** po stronie Suzie.
- **Suzie** ma kanał z **Bobem**, na którym posiada **250 000 satów**, a Bob nie posiada żadnych satów.


![LNP201](assets/en/037.webp)


Jeśli Alicja chce wysłać środki do Boba bez otwierania z nim bezpośredniego kanału, będzie musiała przejść przez Suzie, a każdy kanał będzie musiał dostosować płynność po obu stronach. **Wysłane saty pozostają w obrębie swoich kanałów**; w rzeczywistości nie „przekraczają” kanałów, ale transfer odbywa się poprzez dostosowanie wewnętrznej płynności w każdym kanale.


Załóżmy, że Alicja chce wysłać **50 000 satów** Bobowi:



- **Alicja** wysyła 50 000 satów **Suzie** na ich wspólnym kanale.
- **Suzie** replikuje ten transfer wysyłając 50 000 satów **Bobowi** na ich kanale.


![LNP201](assets/en/038.webp)


W ten sposób płatność jest kierowana do Boba poprzez ruch płynności w każdym kanale. Na koniec operacji Alicja otrzymuje 50 000 satów. Rzeczywiście przekazała 50 000 satów, ponieważ początkowo miała ich 100 000. Bob, po swojej stronie, otrzymuje dodatkowe 50 000 satów. Dla Suzie (węzła pośredniego) operacja ta jest neutralna: początkowo miała 30 000 satów w swoim kanale z Alicją i 250 000 satów w swoim kanale z Bobem, łącznie 280 000 satów. Po operacji posiada 80 000 satów w swoim kanale z Alicją i 200 000 satów w swoim kanale z Bobem, co jest taką samą sumą jak na początku.


Transfer ten jest zatem ograniczony przez **płynność dostępną** w kierunku transferu.


### Obliczanie limitów trasy i płynności


Weźmy teoretyczny przykład innej sieci:



- **130 000 satów** po stronie Alicji (na pomarańczowo) na jej kanale z **Suzie** (na szaro).
- **90,000 satów** po stronie **Suzie** i **200,000 satów** po stronie **Carol** (w kolorze różowym).
- **150 000 satów** po stronie **Carol** i **100 000 satów** po stronie **Boba**.


![LNP201](assets/en/039.webp)


Maksymalna kwota, jaką Alicja może wysłać Bobowi w tej konfiguracji, wynosi **90 000 satów**, ponieważ jest ona ograniczona przez najmniejszą płynność dostępną w kanale między **Suzie a Carol**. W przeciwnym kierunku (między Bobem a Alicją) płatność nie jest możliwa, ponieważ strona **Suzie** w kanale z **Alicją** nie zawiera żadnych satów. W związku z tym nie ma **żadnej trasy** nadającej się do transferu w tym kierunku.

Alicja wysyła Bobowi kanałami **40 000 satów**:



- Alicja przelewa 40 000 satów na swój kanał z Suzie.
- Suzie przelewa 40 000 satów do Carol na ich wspólnym kanale.
- Carol ostatecznie przekazuje Bobowi 40 000 satów.


![LNP201](assets/en/040.webp)


**Saty wysłane** w każdym kanale **pozostają w tym kanale**, więc saty wysłane Bobowi przez Carol nie są takie same jak te wysłane przez Alicję do Suzie. Transfer odbywa się tylko poprzez dostosowanie płynności wewnątrz każdego kanału. Co więcej, całkowita pojemność kanałów pozostaje niezmieniona.


![LNP201](assets/en/041.webp)


Podobnie jak w poprzednim przykładzie, po transakcji węzeł źródłowy (Alicja) ma 40 000 satów mniej. Węzły pośrednie (Suzie i Carol) zachowują tę samą łączną kwotę, dzięki czemu operacja jest dla nich neutralna. Wreszcie, węzeł docelowy (Bob) otrzymuje dodatkowe 40 000 satów.


Rola węzłów pośrednich jest zatem bardzo ważna w funkcjonowaniu sieci Lightning. Ułatwiają one transfery, oferując wiele ścieżek płatności. Aby zachęcić te węzły do zapewnienia płynności i uczestniczenia w routingu płatności, uiszczane są na ich rzecz **opłaty routingowe**.


### Opłaty Routingowe


Węzły pośrednie pobierają opłaty, aby umożliwić przekazywanie płatności przez ich kanały. Opłaty te są ustalane przez **każdy węzeł dla każdego kanału**. Opłaty składają się z 2 elementów:



- „**Opłata podstawowa**”: stała kwota za kanał, często domyślnie **1 sat**, ale z możliwością dostosowania.
- „**Opłata zmienna**”: wartość procentowa przesyłanej kwoty, obliczana w **częściach na milion (ppm)**. Domyślnie jest to **1 ppm** (1 sat na milion przesłanych satów), ale można ją również dostosować.


Opłaty różnią się również w zależności od kierunku przelewu. Na przykład w przypadku przelewu od Alicji do Suzie, Alicję obowiązują opłaty. I odwrotnie, przy przelewie od Suzie do Alicji, opłaty zapłaci Suzie.


Na przykład, dla kanału między Alicją a Suzie, możemy mieć:



- **Alicja**: opłata podstawowa w wysokości 1 sat i 1 ppm dla opłat zmiennych.
- **Suzie**: opłata podstawowa w wysokości 0,5 sata i 10 ppm dla opłat zmiennych.


![LNP201](assets/en/042.webp)


Aby lepiej zrozumieć, jak działają opłaty, przeanalizujmy tę sama sieć Lightning, co poprzednio, ale teraz z następującymi opłatami za routing:



- Kanał **Alicja - Suzie**: opłata podstawowa w wysokości 1 sata i 1 ppm dla Alicji.
- Kanał **Suzie - Carol**: opłata podstawowa 0 satów i 200 ppm dla Suzie.
- Kanał **Carol - Bob**: opłata podstawowa w wysokości 1 sata i 1 ppm dla Suzie 2.

![LNP201](assets/en/043.webp)


Aby dokonać tej samej płatności w wysokości **40 000 satów** na rzecz Boba, Alicja będzie musiała wysłać nieco więcej, ponieważ każdy węzeł pośredniczący potrąci swoje opłaty:



- **Carol** odejmuje 1,04 sat na kanale z Bobem:

$$ f_{\text{Carol-Bob}} = \text{opłata podstawowa} + \left(\frac{\text{ppm} \times \text{amount}}{10^6}\right) $$

$$ f*{\text{Carol-Bob}} = 1 + \frac{1 \times 40000}{10^6} = 1 + 0.04 = 1.04 \text{ satów} $$



- **Suzie** odejmuje 8 satów za opłaty na kanale z Carol:

$$ f_{\text{Suzie-Carol}} = \text{opłata podstawowa} + \left(\frac{\text{ppm} \times \text{amount}}{10^6}\right) $$

$$ f*{\text{Suzie-Carol}} = 0 + \frac{200 \times 40001.04}{10^6} = 0 + 8.0002 \approx 8 \text{ satów} $$


Całkowite opłaty za tę płatność na tej ścieżce wynoszą zatem **9,04 satów**. Zatem Alicja musi wysłać **40 009,04 satów**, aby Bob otrzymał dokładnie **40 000 satów**.


![LNP201](assets/en/044.webp)


Płynność jest zatem aktualizowana:


![LNP201](assets/en/045.webp)


### Routowanie warstwowe


Aby skierować płatność od nadawcy do odbiorcy, sieć Lightning wykorzystuje metodę zwaną „**routingiem warstwowym**”. W przeciwieństwie do routingu klasycznych danych, gdzie każdy router decyduje o kierunku danych w oparciu o ich miejsce docelowe, routing warstwowy działa inaczej:



- **Węzeł wysyłający oblicza całą trasę**: Alicja, na przykład, określa, że jej płatność musi przejść przez Suzie i Carol, zanim dotrze do Boba.
- **Każdy węzeł pośredniczący zna tylko swojego bezpośredniego sąsiada**: Suzie wie tylko, że otrzymała środki od Alicji i że musi je przekazać Carol. Suzie nie wie jednak, czy Alicja jest węzłem źródłowym, czy węzłem pośredniczącym, a także nie wie, czy Carol jest węzłem odbiorczym, czy tylko innym węzłem pośredniczącym. Zasada ta dotyczy również Carol i wszystkich innych węzłów na ścieżce. W ten sposób routing warstwowy pomaga zachować poufność transakcji poprzez maskowanie tożsamości nadawcy i odbiorcy końcowego.

Aby zapewnić, że węzeł nadawczy może obliczyć pełną trasę do odbiorcy w routingu warstwowym, musi on utrzymywać **graf sieciowy**, aby znać swoją topologię i określić możliwe trasy.

**Co powinieneś wynieść z tego rozdziału?**



- W sieci Lightning płatności mogą być kierowane między węzłami połączonymi pośrednio przez kanały pośredniczące. Każdy z tych węzłów pośredniczących ułatwia przekazywanie płynności.
- Węzły pośredniczące otrzymują prowizję za swoje usługi, składającą się z opłat stałych i zmiennych.
- Routowanie warstwowe pozwala węzłowi nadawczemu obliczyć pełną trasę bez informowania węzłów pośredniczących o źródle lub miejscu docelowym transakcji.


W tym rozdziale zbadaliśmy routing płatności w sieci Lightning. Pojawia się jednak pytanie: co uniemożliwia węzłom pośredniczącym akceptowanie płatności przychodzących bez przekazywania ich do następnego miejsca docelowego w celu przechwycenia transakcji? To jest właśnie rola kontraktów haszowych z blokadą czasową lub HTLC, którą przeanalizujemy w następnym rozdziale.


## HTLC - kontrakt haszowy z blokadą czasową


<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>


:::video id=6f204b92-55a5-4939-9440-7c5b96a297bf:::


W tym rozdziale odkryjemy, w jaki sposób sieć Lightning umożliwia przesyłanie płatności przez węzły pośredniczące bez konieczności ufania im, dzięki **kontraktom HTLC** (_Hashed Time-Locked Contracts_). Te inteligentne kontrakty zapewniają, że każdy węzeł pośredniczący otrzyma środki ze swojego kanału tylko wtedy, gdy przekaże płatność ostatecznemu odbiorcy, w przeciwnym razie płatność nie zostanie zatwierdzona.


Kwestią, która pojawia się w przypadku routingu płatności, jest zatem niezbędne zaufanie do węzłów pośredniczących i między samymi węzłami pośredniczącymi. Aby to zilustrować, powróćmy do naszego uproszczonego przykładu sieci Lightning z 3 węzłami i 2 kanałami:



- Alicja ma kanał z Suzie.
- Suzie ma kanał z Bobem.


Alicja chce wysłać 40 000 satów Bobowi, ale nie ma z nim bezpośredniego kanału i nie chce go otwierać. Szuka trasy i decyduje się przejść przez węzeł Suzie.


![LNP201](assets/en/046.webp)


Jeśli Alicja naiwnie wyśle 40 000 satów Suzie, mając nadzieję, że Suzie przeleje tę sumę Bobowi, Suzie może zatrzymać środki dla siebie i nie przekaże niczego Bobowi.


![LNP201](assets/en/047.webp)

Aby uniknąć takiej sytuacji, w sieci Lightning używamy kontraktów HTLC (Hashed Time-Locked Contracts), które sprawiają, że płatność do węzła pośredniczącego jest warunkowa, co oznacza, że Suzie musi spełnić określone warunki, aby uzyskać dostęp do środków Alicji i przekazać je Bobowi.


### Jak działają kontrakty HTLC


HTLC jest specjalnym kontraktem opartym na dwóch zasadach:



- **Warunek dostępu**: Odbiorca musi ujawnić sekret, aby odblokować należną mu płatność.
- **Wygaśnięcie**: Jeśli płatność nie zostanie w pełni zrealizowana w określonym czasie, zostanie anulowana, a środki wrócą do nadawcy.


Oto jak ten proces działa w naszym przykładzie z Alicją, Suzie i Bobem:


![LNP201](assets/en/048.webp)


**Tworzenie sekretu**: Bob generuje losowy sekret oznaczony jako _s_ (obraz wstępny) i oblicza jego hasz oznaczony jako _r_ za pomocą funkcji hasz oznaczonej jako _h_. Mamy:


$$
r = h(s)
$$


Użycie funkcji hasz uniemożliwia znalezienie _s_ tylko z _h(s)_, ale jeśli _s_ jest podane, łatwo jest zweryfikować, że odpowiada _h(s)_.


![LNP201](assets/en/049.webp)


**Wysłanie żądania płatności**: Bob wysyła **fakturę** Alicji z prośbą o płatność. Ta faktura zawiera hasz _r_.


![LNP201](assets/en/050.webp)


**Wysłanie płatności warunkowej**: Alicja wysyła Suzie kontrakt HTLC w wysokości 40 000 satów. Warunkiem otrzymania tych środków przez Suzie jest dostarczenie Alicji tajnego _s'_ spełniającego następujące równanie:


$$
h(s') = r
$$


![LNP201](assets/en/051.webp)


**Przekazanie kontraktu HTLC ostatecznemu odbiorcy**: Suzie, aby otrzymać 40 000 satów od Alicji, musi przekazać Bobowi podobny kontrakt HTLC o wartości 40 000 satów, który ma ten sam warunek, a mianowicie musi dostarczyć Suzie sekret _s'_, który spełnia równanie:


$$
h(s') = r
$$


![LNP201](assets/en/052.webp)


**Weryfikacja przez tajne _s_**: Bob przekazuje _s_ Suzie, aby otrzymać 40 000 satów obiecanych w kontrakcie HTLC. Dzięki temu sekretowi Suzie może odblokować HTLC Alicji i otrzymać od niej 40 000 satów. Płatność jest następnie prawidłowo kierowana do Boba.


![LNP201](assets/en/053.webp)

Proces ten uniemożliwia Suzie zatrzymanie środków Alicji bez ukończenia transferu do Boba, ponieważ musi ona wysłać płatność do Boba, aby uzyskać tajne _s_, a tym samym odblokować kontrakt HTLC Alicji. Operacja pozostaje taka sama, nawet jeśli trasa obejmuje kilka węzłów pośredniczących: jest to po prostu kwestia powtórzenia kroków Suzie dla każdego węzła pośredniczącego. Każdy węzeł jest chroniony przez warunki kontraktu HTLC, ponieważ odblokowanie ostatniego HTLC przez odbiorcę automatycznie uruchamia odblokowanie wszystkich innych HTLC w kaskadzie.


### Wygaśnięcie i zarządzanie kontraktem HTLC w przypadku problemów


Jeśli podczas procesu płatności jeden z węzłów pośredniczących lub węzeł odbiorcy przestanie odpowiadać, szczególnie w przypadku awarii Internetu lub zasilania, wówczas płatność nie może zostać zakończona, ponieważ sekret potrzebny do odblokowania kontraktu HTLC nie został przesłany. W naszym przykładzie z Alicją, Suzie i Bobem, problem ten wystąpi na przykład, gdy Bob nie prześle Suzie sekretu _s_. W takim przypadku wszystkie kontrakty HTLC znajdujące się przed ścieżką i zabezpieczone przez nie środki zostaną zablokowane.


![LNP201](assets/en/054.webp)


Aby tego uniknąć, kontrakty HTLC w sieci Lightning mają okres ważności, który pozwala na usunięcie HTLC, jeśli nie zostanie on ukończony po określonym czasie. Wygaśnięcie następuje w określonej kolejności, ponieważ zaczyna się najpierw od kontraktu HTLC najbliższego odbiorcy, a następnie stopniowo przesuwa się w górę do emitenta transakcji. W naszym przykładzie, jeśli Bob nigdy nie przekaże tajemnicy _s_ Suzie, spowoduje to wygaśnięcie HTLC Suzie wobec Boba.


![LNP201](assets/en/055.webp)


Następnie HTLC od Alicji do Suzie.


![LNP201](assets/en/056.webp)


Gdyby kolejność wygaśnięcia została odwrócona, Alicja mogłaby odzyskać swoją płatność, zanim Suzie zdołałaby uchronić się przed potencjalnym oszustwem. Rzeczywiście, jeśli Bob wróciłby, aby odebrać swój kontrakt HTLC, podczas gdy Alicja już usunęła swój, Suzie znalazłaby się w niekorzystnej sytuacji. Ta kaskadowa kolejność wygasania HTLC zapewnia zatem, że żaden węzeł pośredniczący nie ponosi nieuczciwych strat.


### Reprezentacja kontraktów HTLC w transakcjach zobowiązujących


Transakcje zobowiązujące reprezentują kontrakty HTLC w taki sposób, że warunki, które nakładają na sieć Lightning, mogą zostać przeniesione do sieci Bitcoin w przypadku wymuszonego zamknięcia kanału w trakcie życia HTLC. Dla przypomnienia, transakcje zobowiązujące reprezentują aktualny stan kanału między dwoma użytkownikami i pozwalają na jednostronne wymuszone zamknięcie w przypadku wystąpienia problemów. Z każdym nowym stanem kanału tworzone są 2 transakcje zobowiązujące: po jednej dla każdej ze stron. Powróćmy do naszego przykładu z Alicją, Suzie i Bobem, ale przyjrzyjmy się bliżej temu, co dzieje się na poziomie kanału między Alicją i Suzie, gdy tworzony jest kontrakt HTLC.

![LNP201](assets/en/057.webp)


Przed rozpoczęciem płatności na 40 000 satów między Alicją a Bobem, Alicja posiada 100 000 satów w swoim kanale z Suzie, podczas gdy Suzie posiada 30 000 satów. Ich transakcje zobowiązujące wyglądają następująco:


![LNP201](assets/en/058.webp)


Alicja właśnie otrzymała fakturę Boba, która zawiera _r_, hasz sekretu. Może więc skonstruować kontrakt HTLC o wartości 40 000 satów z Suzie. Ten HTLC jest reprezentowany w ostatnich transakcjach zobowiązujących jako wyjście o nazwie „**_HTLC Out_**” po stronie Alicji, ponieważ fundusze są wychodzące, i „**_HTLC In_**” po stronie Suzie, ponieważ fundusze są przychodzące.


![LNP201](assets/en/059.webp)


Te wyjścia powiązane z kontraktem HTLC mają dokładnie takie same warunki, a mianowicie:



- Jeśli Suzie jest w stanie podać tajne _s_, może natychmiast odblokować to wyjście i przesłać je na kontrolowany przez siebie adres.
- Jeśli Suzie nie posiada sekretu _s_, nie może odblokować tego wyjścia, a Alicja będzie w stanie odblokować je po blokadzie czasowej, aby wysłać je na kontrolowany przez nią adres. Blokada czasowa daje więc Suzie czas na reakcję, jeśli zdobędzie _s_.


Warunki te mają zastosowanie tylko wtedy, gdy kanał zostanie zamknięty (tj. transakcja zobowiązująca zostanie opublikowana on-chain), podczas gdy kontrakt HTLC jest nadal aktywny w sieci Lightning, co oznacza, że płatność między Alicją a Bobem nie została jeszcze sfinalizowana, a HTLC jeszcze nie wygasły. Dzięki tym warunkom Suzie może odzyskać należne jej 40 000 satów z HTLC poprzez dostarczenie _s_. W przeciwnym razie Alicja odzyska środki po wygaśnięciu blokady czasowej, ponieważ jeśli Suzie nie zna _s_, oznacza to, że nie przekazała 40 000 satów Bobowi, a zatem środki Alicji nie należą sie jej.


Ponadto, jeśli kanał zostanie zamknięty, podczas gdy kilka kontraktów HTLC jest w toku, będzie tyle dodatkowych wyjść, ile trwa HTLC.

Jeśli kanał nie zostanie zamknięty, to po wygaśnięciu lub dokonaniu płatności Lightning tworzone są nowe transakcje zobowiązujące, aby odzwierciedlić nowy, teraz stabilny stan kanału, czyli bez żadnych oczekujących kontraktów HTLC. Dane wyjściowe związane z HTLC można zatem usunąć z transakcji zobowiązującej.

![LNP201](assets/en/060.webp)


Wreszcie, w przypadku zamknięcia kanału współpracy, gdy aktywny jest kontrakt HTLC, Alicja i Suzie przestają akceptować nowe płatności i czekają na rozwiązanie lub wygaśnięcie trwających kontraktów HTLC. Pozwala im to opublikować lżejszą transakcję zamknięcia, bez danych wyjściowych związanych z HTLC, zmniejszając w ten sposób opłaty i unikając oczekiwania na ewentualną blokadę czasową.


**Co powinieneś wynieść z tego rozdziału?**


Kontrakty HTLC umożliwiają kierowanie płatności Lightning przez wiele węzłów bez konieczności ufania im. Oto kluczowe punkty do zapamiętania:



- Kontrakty HTLC zapewniają bezpieczeństwo płatności poprzez sekret (obraz wstępny) i czas wygaśnięcia.
- Rozwiązanie lub wygaśnięcie kontraktu HTLC następuje w określonej kolejności: następuje od miejsca docelowego do źródła, w celu ochrony każdego węzła.
- Dopóki HTLC nie zostanie rozwiązany ani nie wygaśnie, jest on utrzymywany jako ważny w ostatnich transakcjach zobowiązujących.


W następnym rozdziale dowiemy się, w jaki sposób węzeł inicjujący transakcję Lightning znajduje i wybiera trasy dla swojej płatności, aby dotrzeć do węzła odbiorcy.


## Znajdowanie drogi


<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>


:::video id=e5baa834-111d-46f5-a28b-3538bed2bbb0:::


W poprzednich rozdziałach zobaczyliśmy, jak korzystać z kanałów innych węzłów do kierowania płatności i docierania do węzła bez bezpośredniego połączenia z nim za pośrednictwem kanału. Omówiliśmy również, jak zapewnić bezpieczeństwo transferu bez ufania węzłom pośredniczącym. W tym rozdziale skupimy się na znalezieniu najlepszej możliwej trasy dotarcia do węzła docelowego.


### Problem routingu w sieci Lightning


Jak widzieliśmy, w sieci Lightning to węzeł wysyłający płatność musi obliczyć pełną trasę do odbiorcy, ponieważ używamy systemu routingu warstwowego. Węzły pośredniczące nie znają ani punktu początkowego, ani ostatecznego miejsca docelowego. Wiedzą tylko, skąd pochodzi płatność i do którego węzła muszą ją następnie przesłać. Oznacza to, że węzeł wysyłający musi utrzymywać dynamiczną lokalną topologię sieci, z istniejącymi węzłami Lightning i kanałami między nimi, biorąc pod uwagę otwarcia, zamknięcia i aktualizacje stanu.


![LNP201](assets/en/061.webp)

Nawet przy takiej topologii sieci Lightning, niektóre informacje istotne dla routingu pozostają niedostępne dla węzła wysyłającego - nie widzi on dokładnego rozkładu płynności w kanałach w danym momencie. Rzeczywiście, każdy kanał wyświetla tylko swoją **całkowitą pojemność**, ale wewnętrzna dystrybucja środków jest znana tylko dwóm uczestniczącym węzłom. Stanowi to wyzwanie dla efektywnego routingu, ponieważ powodzenie płatności zależy w szczególności od tego, czy jej kwota jest mniejsza niż najniższa płynność na wybranej trasie. Płynności nie są jednak widoczne dla węzła wysyłającego.

![LNP201](assets/en/062.webp)


### Aktualizacja mapy sieci


Aby mapa sieci była aktualna, węzły regularnie wymieniają wiadomości za pomocą algorytmu o nazwie „**_gossip_**”. Jest to rozproszony algorytm używany do rozprzestrzeniania informacji w sposób epidemiczny do wszystkich węzłów w sieci, co pozwala na wymianę i synchronizację ogólnego stanu kanałów w kilku cyklach komunikacyjnych. Każdy węzeł rozprzestrzenia informacje do jednego lub więcej sąsiadów wybranych losowo lub nie, ci z kolei rozprzestrzeniają informacje do innych sąsiadów i tak dalej, aż do osiągnięcia globalnie zsynchronizowanego stanu.


Dwie główne wiadomości wymieniane między węzłami sieci Lightning są następujące:



- „**Channel Announcements**”: wiadomości sygnalizujące otwarcie nowego kanału.
- „**Channel Updates**”: wiadomości aktualizacyjne dotyczące stanu kanału, w szczególności ewolucji opłat (ale nie dystrybucji płynności).


Węzły sieci Lightning monitorują również łańcuch bloków Bitcoina w celu wykrycia transakcji zamknięcia kanału. Zamknięty kanał jest następnie usuwany z mapy, ponieważ nie może być już używany do kierowania naszych płatności.


### Routing płatności


Weźmy przykład małej sieci Lightning Network z 7 węzłami: Alicja, Bob, 1, 2, 3, 4 i 5. Wyobraźmy sobie, że Alicja chce wysłać płatność do Boba, ale musi przejść przez węzły pośredniczące.


![LNP201](assets/en/063.webp)


Oto rzeczywista dystrybucja środków w tych kanałach:



- **Kanał pomiędzy Alicją i 1**: 250 000 satów po stronie Alicji, 80 000 po stronie 1 (całkowita przepustowość 330 000 satów).
- **Kanał pomiędzy 1 i 2**: 300 000 satów po stronie 1, 200 000 po stronie 2 (całkowita pojemność 500 000 satów).
- **Kanał pomiędzy 2 i 3**: 50 000 satów po stronie 2, 60 000 po stronie 3 (całkowita pojemność 110 000 satów).
- **Kanał pomiędzy 2 i 5**: 90 000 satów po stronie 2, 160 000 po stronie 5 (całkowita pojemność 250 000 satów).
- **Kanał między 2 i 4**: 180 000 satów po stronie 2, 110 000 po stronie 4 (całkowita pojemność 290 000 satów).
- **Kanał pomiędzy 4 i 5**: 200 000 satów po stronie 4, 10 000 po stronie 5 (całkowita pojemność 210 000 satów).
- **Kanał pomiędzy 3 i Bob**: 50 000 satów po stronie 3, 250 000 po stronie Bob (całkowita pojemność 300 000 satów).
- **Kanał pomiędzy 5 i Bob**: 260 000 satów po stronie 5, 100 000 po stronie Bob (całkowita pojemność 360 000 satów).


![LNP201](assets/en/064.webp)


Aby dokonać płatności w wysokości 100 000 satów od Alicji do Boba, opcje routingu są ograniczone przez płynność dostępną w każdym kanale. Optymalną trasą dla Alicji, w oparciu o znane rozkłady płynności, może być sekwencja „Alicja → 1 → 2 → 4 → 5 → Bob”:


![LNP201](assets/en/065.webp)


Ponieważ jednak Alicja nie zna dokładnej dystrybucji środków w każdym kanale, musi oszacować optymalną trasę w sposób probabilistyczny, biorąc pod uwagę następujące kryteria:



- **Prawdopodobieństwo sukcesu**: kanał o wyższej całkowitej przepustowości z większym prawdopodobieństwem będzie zawierał wystarczającą płynność. Na przykład, kanał między węzłem 2 a węzłem 3 ma całkowitą przepustowość 110 000 satów, więc znalezienie 100 000 satów lub więcej po stronie węzła 2 jest mało prawdopodobne, choć nadal możliwe.
- **Opłaty transakcyjne**: wybierając najlepszą trasę, węzeł wysyłający bierze również pod uwagę opłaty stosowane przez każdy węzeł pośredni i dąży do zminimalizowania całkowitego kosztu routingu.
- **Wygaśnięcie kontraktu HTLC**: aby uniknąć zablokowania płatności, czas wygaśnięcia kontraktu HTLC jest również parametrem, który należy wziąć pod uwagę.
- **Liczba węzłów pośrednich**: wreszcie, bardziej ogólnie, węzeł wysyłający będzie starał się znaleźć trasę z jak najmniejszą liczbą węzłów, aby zmniejszyć ryzyko niepowodzenia i ograniczyć opłaty za transakcje błyskawiczne.


Analizując te kryteria, węzeł wysyłający może przetestować najbardziej prawdopodobne trasy i spróbować je zoptymalizować. W naszym przykładzie Alicja mogłaby uszeregować najlepsze trasy w następujący sposób:



- `Alicja → 1 → 2 → 5 → Bob`, ponieważ jest to najkrótsza trasa o największej przepustowości.
- `Alicja → 1 → 2 → 4 → 5 → Bob`, ponieważ ta trasa oferuje dobrą przepustowość, chociaż jest dłuższa niż pierwsza.
- `Alicja → 1 → 2 → 3 → Bob`, ponieważ ta trasa obejmuje kanał `2 → 3`, który ma bardzo ograniczoną przepustowość, ale pozostaje potencjalnie użyteczny.


### Realizacja płatności


Alicja postanawia przetestować swoją pierwszą trasę (`Alicja → 1 → 2 → 5 → Bob`). W związku z tym wysyła kontrakt HTLC w wysokości 100 000 satów do węzła 1. Węzeł ten sprawdza, czy ma wystarczającą płynność z węzłem 2 i kontynuuje transmisję. Węzeł 2 odbiera następnie HTLC z węzła 1, ale zdaje sobie sprawę, że nie ma wystarczającej płynności w swoim kanale z węzłem 5, aby skierować płatność w wysokości 100 000 satów. Następnie wysyła komunikat o błędzie z powrotem do węzła 1, który przesyła go do Alicji. Ta trasa nie powiodła się.


![LNP201](assets/en/066.webp)


Następnie Alicja próbuje skierować swoją płatność przy użyciu drugiej trasy (`Alicja → 1 → 2 → 4 → 5 → Bob`). Wysyła HTLC o wartości 100 000 satów do węzła 1, który przesyła go do węzła 2, następnie do węzła 4, do węzła 5 i wreszcie do Boba. Tym razem płynność jest wystarczająca, a trasa działa. Każdy węzeł odblokowuje swój HTLC kaskadowo przy użyciu obrazu wstępnego dostarczonego przez Boba (sekret _s_), co pozwala na pomyślne sfinalizowanie płatności Alicji na rzecz Boba.


![LNP201](assets/en/067.webp)


Poszukiwanie trasy odbywa się w następujący sposób: węzeł wysyłający rozpoczyna od zidentyfikowania najlepszych możliwych tras, a następnie próbuje kolejno dokonywać płatności, aż do znalezienia funkcjonalnej trasy.


Warto zauważyć, że Bob może dostarczyć Alicji informacji w **fakturze**, aby ułatwić routing. Na przykład może wskazać pobliskie kanały o wystarczającej płynności lub ujawnić istnienie kanałów prywatnych. Wskazówki te pozwolą Alicji uniknąć tras o niewielkich szansach powodzenia i w pierwszej kolejności wypróbować ścieżki zalecane przez Boba.


**Co powinieneś wynieść z tego rozdziału?**



- Węzły utrzymują mapę topologii sieci poprzez ogłoszenia i monitorowanie zamknięć kanałów w łańcuchu bloków Bitcoina.
- Poszukiwanie optymalnej trasy dla płatności pozostaje probabilistyczne i zależy od wielu kryteriów.
- Bob może dostarczyć wskazówek w **fakturze**, aby pokierować trasą Alicji i uchronić ją przed testowaniem mało efektywnych tras.


W następnym rozdziale zajmiemy się funkcjonowaniem faktur, a także kilkoma innymi narzędziami używanymi w sieci Lightning.


# Narzędzia sieci Lightning


<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>


## Faktura, wypłata LNURL i keysend


<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>

:::video id=309c3412-506e-4189-ad46-5e5088c55008:::


W tym rozdziale przyjrzymy się bliżej działaniu **faktur** Lightning, czyli żądań płatności wysyłanych przez węzeł odbiorcy do węzła nadawcy. Celem jest zrozumienie, jak płacić i otrzymywać płatności w sieci Lightning. Omówimy również 2 alternatywy dla klasycznych faktur: wypłatę LNURL i keysend.


![LNP201](assets/en/068.webp)


### Struktura faktur Lightning


Jak wyjaśniono w rozdziale dotyczącym kontraktów HTLC, każda płatność rozpoczyna się od wygenerowania **faktury** przez odbiorcę. Faktura ta jest następnie przesyłana do płacącego (za pomocą kodu QR lub przez kopiowanie-wklejanie) w celu zainicjowania płatności. Faktura składa się z dwóch głównych części:



- **Część czytelna dla człowieka**: ta sekcja zawiera wyraźnie widoczne metadane w celu poprawy komfortu użytkowania.
- **Ładunek danych faktury**: ta sekcja zawiera informacje dotyczące przetwarzania płatności przeznaczone dla maszyn.


Typowa struktura faktury zaczyna się od identyfikatora `LN` dla „Lightning”, po którym następuje `bc` dla Bitcoina, a następnie wysokość faktury. Separator `1` odróżnia część czytelną dla człowieka od części danych (ładunku).


Weźmy następującą fakturę jako przykład:


```invoice
lnbc100u1p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```


Możemy już podzielić ją na 2 części. Pierwsza to część czytelna dla człowieka:


```invoice
lnbc100u
```


Następnie część przeznaczona na ładunek:


```invoice

p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```


Obie części są oddzielone znakiem `1`. Separator ten został wybrany zamiast znaku specjalnego, aby umożliwić łatwe kopiowanie i wklejanie całej faktury poprzez dwukrotne kliknięcie.


W pierwszej części możemy zobaczyć następujące elementy:



- `LN` wskazuje, że jest to transakcja Lightning.
- `bc` wskazuje, że sieć Lightning znajduje się w łańcuchu bloków Bitcoina (a nie na Testnet lub na Litecoin).
- `100u` oznacza wysokość faktury, wyrażoną w **mikrobitcoinach** (`u` oznacza „mikro”), co tutaj jest równoważne 10 000 satom.


Kwota płatności jest wyrażana w podjednostkach Bitcoina. Oto używane jednostki:



- **Millibitcoin (oznaczany `m`):** Reprezentuje jedną tysięczną Bitcoina.


$$
1 \, \text{mBTC} = 10^{-3} \, \text{BTC} = 10^5 \, \text{satów}
$$



- **Microbitcoin (oznaczany `u`):** Czasami nazywany również „bitem”, reprezentuje jedną milionową Bitcoina.


$$
1 \, \mu\text{BTC} = 10^{-6} \, \text{BTC} = 100 \, \text{satów}
$$



- **Nanobitcoin (oznaczany `n`):** Reprezentuje jedną miliardową Bitcoina.


$$
1 \, \text{nBTC} = 10^{-9} \, \text{BTC} = 0.1 \, \text{satów}
$$



- **Picobitcoin (oznaczany jako `p`):** Reprezentuje jedną bilionową Bitcoina.

$$
1 \, \text{pBTC} = 10^{-12} \, \text{BTC} = 0.0001 \, \text{satów}
$$


### Ładunek danych faktury


Ładunek danych faktury zawiera kilka informacji niezbędnych do przetworzenia płatności:



- **Stempel czasu:** Moment utworzenia faktury, wyrażony w Unix Timestamp (liczba sekund, które upłynęły od 1 stycznia 1970 r.).
- **Haszowanie sekretu**: Jak widzieliśmy w sekcji dotyczącej kontraktów HTLC, węzeł odbierający musi dostarczyć węzłowi wysyłającemu hasz obrazu wstępnego. W kontrakcie HTLC służy to do zabezpieczenia transakcji. Określiliśmy to jako „_r_”.
- **Sekret płatności**: Kolejny sekret jest generowany przez odbiorcę, ale tym razem jest on przesyłany do węzła wysyłającego. Jest on używany w routingu warstwowym, aby uniemożliwić węzłom pośrednim odgadnięcie, czy następny węzeł jest odbiorcą końcowym, czy nie. W ten sposób odbiorca zachowuje pewną formę poufności w odniesieniu do ostatniego węzła pośredniego na trasie.
- **Klucz publiczny odbiorcy**: Wskazuje płatnikowi identyfikator osoby, która ma otrzymać płatność.
- **Czas wygaśnięcia**: Maksymalny czas, w ciągu którego faktura ma być opłacona (domyślnie 1 godzina).
- **Wskazówki dotyczące trasy**: Dodatkowe informacje dostarczone przez odbiorcę, aby pomóc nadawcy zoptymalizować trasę płatności.
- **Podpis**: Gwarantuje integralność faktury poprzez uwierzytelnienie wszystkich informacji.


Faktury są następnie kodowane w **bech32**, takim samym formacie jak adresy Bitcoin SegWit (format zaczynający się od `bc1`).


### Wypłata LNURL


W tradycyjnej transakcji, takiej jak zakupy w sklepie, faktura jest generowana dla całkowitej kwoty do zapłaty. Klient otrzymuje fakturę w postaci kodu QR lub ciągu znaków, który może zeskanować i sfinalizować transakcję. Płatność przebiega następnie zgodnie z tradycyjnym procesem, który przeanalizowaliśmy w poprzedniej sekcji. Jednak proces ten może być czasami bardzo uciążliwy dla użytkownika, ponieważ wymaga od odbiorcy wysłania informacji do nadawcy za pośrednictwem faktury.


W niektórych sytuacjach, takich jak wypłata bitcoinów za pomocą usługi online, tradycyjny proces jest zbyt uciążliwy. W takich przypadkach funkcja wypłaty **LNURL** upraszcza ten proces, wyświetlając kod QR, który skanuje portfel odbiorcy, aby automatycznie utworzyć fakturę. Następnie usługa płaci fakturę, a użytkownik po prostu widzi natychmiastową wypłatę.


![LNP201](assets/en/069.webp)


LNURL to protokół komunikacyjny, który określa zestaw funkcji zaprojektowanych w celu uproszczenia interakcji między węzłami Lightning i klientami, a także aplikacjami innych firm. Wypłata LNURL, jak właśnie widzieliśmy, jest więc tylko jednym z przykładów funkcjonalności.

Protokół ten opiera się na protokole HTTP i umożliwia tworzenie linków do różnych operacji, takich jak żądanie płatności, żądanie wypłaty lub inne funkcje, które poprawiają komfort użytkowania. Każdy LNURL to zakodowany w bech32 adres URL z prefiksem lnurl, który po zeskanowaniu uruchamia serię automatycznych działań w portfelu Lightning.

Na przykład funkcja LNURL-withdraw (LUD-03) umożliwia wypłacanie środków za pomocą usługi poprzez zeskanowanie kodu QR, bez konieczności ręcznego generowania faktury. Podobnie, LNURL-auth (LUD-04) umożliwia logowanie się do usług online przy użyciu klucza prywatnego w portfelu Lightning zamiast hasła.


### Wysyłanie płatności błyskawicznej bez faktury: Keysend


Innym interesującym przypadkiem jest transfer środków bez wcześniejszego otrzymania faktury, znany jako „**keysend**”. Protokół ten umożliwia wysyłanie środków poprzez dodanie obrazu wstępnego do zaszyfrowanych danych płatności, dostępnych tylko dla odbiorcy. Ten obraz wstępny umożliwia odbiorcy odblokowanie kontraktu HTLC, a tym samym odzyskanie środków bez wcześniejszego wygenerowania faktury.


Dla uproszczenia, w tym protokole to nadawca generuje sekret używany w HTLC, a nie odbiorca. W praktyce pozwala to nadawcy na dokonanie płatności bez konieczności wcześniejszej interakcji z odbiorcą.


![LNP201](assets/en/070.webp)


**Co powinieneś wynieść z tego rozdziału?**



- **Faktura Lightning** to żądanie płatności składające się z części czytelnej dla człowieka i części zawierającej dane maszynowe.
- Faktura jest zakodowana w **bech32**, z separatorem `1` ułatwiającym kopiowanie i częścią danych zawierającą wszystkie informacje niezbędne do przetworzenia płatności.
- W sieci Lightning istnieją inne procesy płatności, w szczególności wypłata **LNURL** w celu ułatwienia wypłat oraz **Keysend** do bezpośrednich przelewów bez faktury.


W następnym rozdziale zobaczymy, jak operator węzła może zarządzać płynnością w swoich kanałach, aby nigdy nie zostać zablokowanym i zawsze móc wysyłać i odbierać płatności w sieci Lightning.


## Zarządzanie płynnością


<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>


:::video id=96096aef-e4ce-4c44-a022-57e27082232a:::


W tym rozdziale omówimy strategie skutecznego zarządzania płynnością w sieci Lightning. Zarządzanie płynnością różni się w zależności od typu użytkownika i kontekstu. Przyjrzymy się głównym zasadom i istniejącym technikom, aby lepiej zrozumieć, jak zoptymalizować to zarządzanie.


### Potrzeby w zakresie płynności


Istnieją trzy główne profile użytkowników Lightning, z których każdy ma określone potrzeby w zakresie płynności:



- **Płacący**: Jest to osoba, która dokonuje płatności. Potrzebuje płynności wychodzącej, aby móc przekazywać środki innym użytkownikom. Może to być na przykład konsument.
- **Sprzedawca (lub odbiorca płatności)**: Jest to osoba, która otrzymuje płatności. Potrzebuje płynności przychodzącej, aby móc akceptować płatności do swojego węzła. Może to być na przykład firma lub sklep internetowy.
- **Router**: Węzeł pośredniczący, często specjalizujący się w przekierowywaniu płatności, który musi zoptymalizować swoją płynność w każdym kanale, aby przekierować jak najwięcej płatności i zarobić na opłatach.


Profile te nie są oczywiście stałe; użytkownik może przełączać się między płacącym a odbiorcą w zależności od transakcji. Przykładowo, Bob może otrzymywać swoją pensję od swojego pracodawcy, co stawia go w pozycji „sprzedawcy” wymagającego płynności przychodzącej. Następnie, jeśli chce wykorzystać swoją pensję do zakupu żywności, staje się „płacącym” i musi mieć płynność wychodzącą.


Aby lepiej to zrozumieć, weźmy przykład prostej sieci składającej się z trzech węzłów: kupującego (Alicja), routera (Suzie) i sprzedawcy (Bob).


![LNP201](assets/en/071.webp)


Wyobraźmy sobie, że kupujący chce wysłać 30 000 satów do sprzedającego i że płatność przechodzi przez węzeł routera. Każda ze stron musi wtedy posiadać minimalną ilość płynności w kierunku płatności:



- Płacący musi mieć co najmniej 30 000 satów po swojej stronie kanału z routerem.
- Sprzedawca musi mieć kanał, w którym 30 000 satów znajduje się po przeciwnej stronie, aby móc je odbierać.
- Router musi mieć 30 000 satów po stronie płacącego w swoim kanale, a także 30 000 satów po swojej stronie w kanale ze sprzedawcą, aby móc przekierować płatność.


![LNP201](assets/en/072.webp)


### Strategie zarządzania płynnością


Płacący muszą zapewnić utrzymanie wystarczającej płynności po swojej stronie kanałów, aby zagwarantować płynność wychodzącą. Okazuje się to stosunkowo proste - wystarczy otworzyć nowe kanały Lightning. Rzeczywiście, na początku środki zablokowane adresem wielopodpisowym w łańcuchu bloków są w kanale Lightning w całości po stronie płacącego. Zdolność płatnicza jest zatem zapewniona tak długo, jak długo kanały z wystarczającą ilością środków są otwarte. Gdy płynność wychodząca zostanie wyczerpana, wystarczy otworzyć nowe kanały.

Z drugiej strony, dla sprzedawcy zadanie jest bardziej złożone. Aby móc otrzymywać płatności, musi mieć płynność po przeciwnej stronie swoich kanałów. Dlatego otwarcie kanału nie wystarczy: sprzedający musi również dokonać płatności w tym kanale, aby przenieść płynność na drugą stronę, zanim będzie mógł sam otrzymywać płatności. W przypadku niektórych profili użytkowników sieci Lightning, takich jak handlowcy, istnieje wyraźna dysproporcja między tym, co ich węzeł wysyła, a tym, co otrzymuje, ponieważ celem firmy jest przede wszystkim zarobienie więcej niż wydaje, aby przynieść sobie zysk. Na szczęście dla użytkowników z określonymi potrzebami w zakresie płynności przychodzącej istnieje kilka rozwiązań:



- **Przyciąganie kanałów**: Sprzedawca korzysta z przewagi wynikającej z wolumenu płatności przychodzących oczekiwanych na jego węźle. Biorąc to pod uwagę, może próbować przyciągnąć węzły routingu, które szukają dochodu z opłat transakcyjnych i które mogą otworzyć kanały w jego kierunku, mając nadzieję na przekierowanie płatności i pobranie powiązanych opłat.



- **Ruch płynności**: Sprzedający może również otworzyć kanał i przenieść część środków na przeciwną stronę, dokonując fikcyjnych płatności na rzecz innego węzła, który zwróci pieniądze w inny sposób. W następnej części zobaczymy, jak przeprowadzić tę operację.



- **Otwarcie trójkątne**: Istnieją platformy dla węzłów, które chcą wspólnie otwierać kanały, umożliwiając każdemu z nich czerpanie korzyści z natychmiastowej płynności przychodzącej i wychodzącej. Na przykład [LightningNetwork+](https://lightningnetwork.plus/) oferuje taką usługę. Jeśli Alicja, Bob i Suzie chcą otworzyć kanał ze 100 000 satów, mogą uzgodnić na tej platformie, że Alicja otworzy kanał w kierunku Boba, Bob w kierunku Suzie, a Suzie w kierunku Alicji. W ten sposób każdy z nich ma 100 000 satów płynności wychodzącej i 100 000 satów płynności przychodzącej, a jednocześnie ma zablokowanych tylko 100 000 satów.


![LNP201](assets/en/073.webp)



- **Kupowanie kanałów**: Istnieją również usługi wynajmu kanałów Lightning w celu uzyskania płynności przychodzącej, takie jak [Bitrefill Thor](https://www.bitrefill.com/thor-lightning-network-channels/) lub [Lightning Labs Pool](https://lightning.engineering/pool/). Na przykład Alicja może kupić kanał o wartości miliona satów dla swojego węzła, aby móc otrzymywać płatności.


![LNP201](assets/en/074.webp)


Wreszcie, węzły przekierowujące, których celem jest maksymalizacja liczby przetwarzanych płatności i pobieranych opłat, muszą:



- Otworzyć dobrze finansowane kanały ze strategicznymi węzłami.
- Regularne dostosowywać dystrybucję środków w kanałach do potrzeb sieci.


### Usługa Loop Out


Usługa [Loop Out](https://lightning.engineering/loop/), oferowana przez Lightning Labs, pozwala na przeniesienie płynności na przeciwną stronę kanału przy jednoczesnym odzyskaniu środków w łańcuchu bloków Bitcoina. Na przykład Alicja wysyła 1 milion satów za pośrednictwem sieci Lightning do węzła pętli, który następnie zwraca jej te środki w bitcoinach on-chain. Równoważy to jej kanał z 1 milionem satów po każdej stronie, optymalizując jej zdolność do otrzymywania płatności.


![LNP201](assets/en/075.webp)


Usługa ta umożliwia uzyskanie płynności przychodzącej podczas odzyskiwania bitcoinów on-chain, co pomaga ograniczyć unieruchomienie gotówki potrzebnej do akceptowania płatności za pomocą sieci Lightning.


**Co powinieneś wynieść z tego rozdziału?**



- Aby wysyłać płatności w sieci Lightning, musisz mieć wystarczającą płynność po swojej stronie w swoich kanałach. Aby zwiększyć tę zdolność wysyłania, wystarczy otworzyć nowe kanały.
- Aby otrzymywać płatności, musisz mieć płynność po przeciwnej stronie swoich kanałów. Zwiększenie tej zdolności odbiorczej jest bardziej złożone, ponieważ wymaga od innych otwarcia kanałów w twoim kierunku lub dokonania (fikcyjnych lub rzeczywistych) płatności w celu przeniesienia płynności na drugą stronę.
- Utrzymanie płynności tam, gdzie jest to pożądane, może być jeszcze trudniejsze w zależności od wykorzystania kanałów. Dlatego istnieją narzędzia i usługi, które pomagają zrównoważyć kanały zgodnie z potrzebami.


W następnym rozdziale proponuję przegląd najważniejszych koncepcji tego szkolenia.


# Idź dalej


<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>


## Podsumowanie kursu



<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>


:::video id=5f4f4344-ef27-4765-8f09-8262e6833bde:::


W tym ostatnim rozdziale na koniec szkolenia LNP201, proponuję powrócić do ważnych koncepcji, które wspólnie omówiliśmy.


Celem tego szkolenia było zapewnienie kompleksowego i technicznego zrozumienia sieci Lightning. Odkryliśmy, w jaki sposób sieć Lightning opiera się na ańcuchu bloków Bitcoina w celu wykonywania transakcji off-chain, zachowując jednocześnie podstawowe cechy Bitcoina, w szczególności brak potrzeby ufania innym węzłom.


### Kanały płatności


W początkowych rozdziałach zbadaliśmy, w jaki sposób dwie strony, otwierając kanał płatności, mogą przeprowadzać transakcje poza łańcuchem bloków Bitcoina. Oto omówione kroki:



- **Otwarcie kanału**: Utworzenie kanału odbywa się za pośrednictwem transakcji Bitcoin, która blokuje środki adresem wielopodpisowym 2/2. Depozyt ten reprezentuje kanał Lightning w łańcuchu bloków.


![LNP201](assets/en/076.webp) 2. **Transakcje w kanale**: W tym kanale można dokonać wielu transakcji bez konieczności publikowania ich w łańcuchu bloków. Każda transkacja Lightning powoduje zmianę w kanale reprezentowaną przez transkacje zobowiązującą.

![LNP201](assets/en/077.webp)



- **Zabezpieczenie i zamknięcie**: Uczestnicy zatwierdzają nowy stanu kanału poprzez wymianę kluczy odwołania, aby zabezpieczyć środki i zapobiec wszelkim oszustwom. Obie strony mogą wspólnie zamknąć kanał, dokonując nowej transakcji w łańcuchu bloków Bitcoina lub w ostateczności poprzez zamknięcie wymuszone. Ta ostatnia opcja, choć mniej wydajna, ponieważ jest dłuższa i czasami słabo oceniana pod względem opłat, nadal pozwala na odzyskanie środków. W przypadku oszustwa ofiara może ukarać oszusta, odzyskując wszystkie środki z kanału w łańcuchu bloków.


![LNP201](assets/en/078.webp)


### Sieć kanałów


Po omówieniu pojedynczych kanałów, rozszerzyliśmy naszą analizę na sieć kanałów:



- **Routing**: Gdy dwie strony nie są bezpośrednio połączone kanałem, sieć umożliwia routing przez węzły pośredniczące. Płatności są następnie przekazywane z jednego węzła do drugiego.


![LNP201](assets/en/079.webp)



- **Kontrakty HTLC**: Płatności przechodzące przez węzły pośredniczące są zabezpieczone przez „_Hash Time-Locked Contracts_” (HTLC), które pozwalają na zablokowanie środków do momentu całkowitego zakończenia płatności.


![LNP201](assets/en/080.webp)



- **Routing warstwowy**: Aby zapewnić poufność płatności, routing warstwowy maskuje przed węzłami pośredniczącymi ostateczne miejsce docelowe płatności. Węzeł wysyłający musi zatem obliczyć całą trasę, ale wobec braku pełnych informacji na temat płynności kanałów, wykonuje kolejne próby, aby przekierować płatność.


![LNP201](assets/en/081.webp)


### Zarządzanie płynnością


Widzieliśmy, że zarządzanie płynnością przepływu płatności jest wyzwaniem dla sieci Lightning. Wysyłanie płatności jest stosunkowo proste: wymaga jedynie otwarcia kanału. Jednak otrzymywanie płatności wymaga posiadania płynności po przeciwnej stronie swoich kanałów. Oto kilka omówionych strategii:



- **Przyciąganie kanałów**: Zachęcając inne węzły do otwierania kanałów do siebie, użytkownik uzyskuje płynność przychodzącą.



- **Przenoszenie płynności**: Wysyłanie płatności do innych kanałów powoduje przeniesienie płynności na przeciwną stronę.


![LNP201](assets/en/082.webp)



- **Korzystanie z usług takich jak Loop i Pool**: Usługi te umożliwiają równoważenie płynności lub kupowanie kanałów z płynnością po przeciwnej stronie.

![LNP201](assets/en/083.webp)


- **Wspólne otwarcia**: Dostępne są również platformy do łączenia się w celu wykonywania otwarć trójkątnych i posiadania płynności przychodzącej.


![LNP201](assets/en/084.webp)


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