---
name: Teoretyczne wprowadzenie do Lightning Network
goal: Odkrywanie Lightning Network z technicznego punktu widzenia
objectives:
  - Zrozumienie funkcjonowania kanałów sieci.
  - Zapoznanie się z terminami takimi jak HTLC, LNURL i UTXO.
  - Przyswajanie zarządzania płynnością finansową i opłatami w LNN.
  - Rozpoznawanie Lightning Network jako sieci.
  - Zrozumienie teoretycznych zastosowań Lightning Network.
---

# Podróż do drugiej warstwy Bitcoina

Ten kurs to teoretyczna lekcja na temat technicznego funkcjonowania Lightning Network.

Witamy w ekscytującym świecie Lightning Network, drugiej warstwie Bitcoina, która jest zarówno zaawansowana, jak i pełna potencjału. Zaraz zagłębimy się w techniczne głębie tej technologii, nie skupiając się na konkretnych poradnikach czy scenariuszach użycia. Aby w pełni wykorzystać ten kurs, niezbędna jest solidna znajomość Bitcoina. To doświadczenie wymaga poważnego i skoncentrowanego podejścia. Możesz również rozważyć równoległe uczestnictwo w kursie LN 202, który oferuje bardziej praktyczny aspekt tej eksploracji. Przygotuj się na podróż, która może zmienić Twoje postrzeganie ekosystemu Bitcoina.

Miłego odkrywania!

+++

# Podstawy
## Zrozumienie Lightning Network

![Zrozumienie Lightning Network](https://youtu.be/PszWk046x-I)

Lightning Network to druga warstwa infrastruktury płatniczej zbudowana na sieci Bitcoina, która umożliwia szybkie i tanie transakcje. Aby w pełni zrozumieć, jak działa Lightning Network, niezbędne jest zrozumienie, czym są kanały płatnicze i jak działają.

Kanał płatniczy Lightning to rodzaj "prywatnego pasa" między dwoma użytkownikami, który umożliwia szybkie i powtarzalne transakcje Bitcoin. Gdy kanał jest otwarty, jest przydzielana mu stała pojemność, która jest z góry określona przez użytkowników. Ta pojemność reprezentuje maksymalną ilość Bitcoina, która może być przesłana w kanale w dowolnym momencie.

Kanały płatnicze są dwukierunkowe, co oznacza, że mają dwie "strony". Na przykład, jeśli Alice i Bob otworzą kanał płatniczy, Alice może wysłać Bitcoiny do Boba, a Bob może wysłać Bitcoiny do Alice. Transakcje wewnątrz kanału nie zmieniają całkowitej pojemności kanału, ale zmieniają rozkład tej pojemności między Alice i Bobem.

![explication](assets/chapitre1/0.JPG)

Aby transakcja była możliwa w kanałach płatniczych Lightning, użytkownik wysyłający środki musi mieć wystarczającą ilość Bitcoina po swojej stronie kanału. Jeśli Alice chce wysłać 1 Bitcoina do Boba przez ich kanał, musi mieć przynajmniej 1 Bitcoina po swojej stronie kanału.
Limity i funkcjonowanie kanałów płatniczych w Lightning.
Pomimo że pojemność kanału płatniczego Lightning jest stała, nie ogranicza to całkowitej liczby transakcji ani całkowitej objętości Bitcoina, która może być przesłana przez kanał. Na przykład, jeśli Alice i Bob mają kanał o pojemności 1 Bitcoina, mogą przeprowadzić setki transakcji po 0,01 Bitcoina lub tysiące transakcji po 0,001 Bitcoina, o ile łączna pojemność kanału nie zostanie przekroczona w dowolnym momencie.

Pomimo tych ograniczeń, kanały płatnicze Lightning są efektywnym sposobem na szybkie i tanie przeprowadzanie transakcji Bitcoin. Pozwalają użytkownikom wysyłać i odbierać Bitcoiny bez konieczności płacenia wysokich opłat transakcyjnych lub oczekiwania na długie okresy potwierdzeń w sieci Bitcoina.

Podsumowując, kanały płatnicze Lightning oferują potężne rozwiązanie dla tych, którzy chcą przeprowadzać szybkie i tanie transakcje Bitcoin. Jednak niezbędne jest zrozumienie ich działania i ograniczeń, aby w pełni wykorzystać ich potencjał.

![explication](assets/chapitre1/1.JPG)

Przykład:

- Alice ma 100,000 SAT
- Bob ma 30,000 SAT
Oto aktualny stan kanału. Podczas transakcji, Alice decyduje się wysłać 40,000 SAT do Boba. Może to zrobić, ponieważ 40,000 < 100,000.
Nowy stan kanału wygląda zatem następująco:

- Alice 60,000 SAT
- Bob 70,000 SAT

```
Początkowy stan kanału:
Alice (100,000 SAT) ============== Bob (30,000 SAT)

Po transferze Alice do Boba 40,000 SAT:
Alice (60,000 SAT) ============== Bob (70,000 SAT)

```
![explication](assets/chapitre1/2.JPG)

Teraz Bob chce wysłać 80,000 SAT do Alice. Nie mając wystarczającej płynności, nie może tego zrobić. Maksymalna pojemność kanału to 130,000 SAT, z możliwym wydatkiem do 60,000 SAT dla Alice i 70,000 SAT dla Boba.

![explication](assets/chapitre1/3.JPG)

## Bitcoin, adresy, UTXO i transakcje

![bitcoin, adresy, utxo i transakcje](https://youtu.be/cadCJ2V7zTg)

W tym drugim rozdziale poświęcamy czas na zrozumienie, jak faktycznie działają transakcje Bitcoin, co będzie bardzo przydatne do zrozumienia Lightning. Omawiamy również krótko koncepcję adresów wielopodpisowych, która jest kluczowa dla zrozumienia następnego rozdziału o otwieraniu kanałów w sieci Lightning.

- Klucz prywatny > Klucz publiczny > Adres: Podczas transakcji, Alice wysyła pieniądze do Boba. Ten ostatni podaje adres uzyskany za pomocą swojego klucza publicznego. Alice, która sama otrzymała pieniądze na adres za pośrednictwem swojego klucza publicznego, teraz używa swojego klucza prywatnego, aby podpisać transakcję i w ten sposób odblokować bitcoiny z adresu.
- W transakcji Bitcoin, wszystkie bitcoiny muszą się przemieścić. Nazwane UTXO (Unspend Transaction Output), kawałki bitcoina opuszczają właściciela tylko po to, by potem do niego wrócić.
  Alice ma 0.002 BTC, Bob ma 0 BTC. Alice decyduje się wysłać 0.0015 BTC do Boba. Podpisze transakcję na 0.002 BTC, gdzie 0.0015 trafi do Boba, a 0.0005 wróci do jej portfela.

![explication](assets/chapitre2/0.JPG)

Tutaj, z jednego UTXO (Alice ma 0.0002 BTC na adresie), stworzyliśmy 2 UTXO (Bob ma 0.0015 i Alice ma nowe UTXO (niezależne od poprzedniego) 0.0005 BTC).

```
Alice (0.002 BTC)
  |
  V
Transakcja Bitcoin (0.002 BTC)
  |
  |----> Bob (0.0015 BTC)
  |
  V
Alice (nowe UTXO: 0.0005 BTC)
```

W sieci Lightning używane są wielopodpisy. W związku z tym, do odblokowania środków wymagane są 2 podpisy, czyli dwa klucze prywatne do przesunięcia pieniędzy. Mogą to być Alice i Bob, którzy razem muszą zgodzić się na odblokowanie pieniędzy (UTXO). W LN konkretnie, są to transakcje 2/2, więc oba podpisy są absolutnie konieczne, w przeciwieństwie do wielopodpisów 2/3 lub 3/5, gdzie wymagana jest tylko kombinacja pełnej liczby kluczy.

![explication](assets/chapitre2/1.JPG)

# Otwieranie i zamykanie kanałów
## Otwieranie kanału

![otwórz kanał](https://youtu.be/B2caBC0Rxko)

Teraz przyjrzymy się bliżej otwieraniu kanału i jak jest to realizowane przez transakcję Bitcoin.
Sieć Lightning posiada różne poziomy komunikacji:
- Komunikacja P2P (protokół Sieci Lightning)
- Kanał płatności (protokół Sieci Lightning)
- Transakcja Bitcoin (protokół Bitcoin)

![explication](assets/chapitre3/0.JPG)

Aby otworzyć kanał, dwie strony komunikują się przez kanał komunikacyjny:

- Alice: "Cześć, chcę otworzyć kanał!"
- Bob: "Ok, oto mój publiczny adres."

![explication](assets/chapitre3/1.JPG)

Alice ma teraz 2 publiczne adresy, aby stworzyć adres multi-sig 2/2. Może teraz dokonać transakcji bitcoin, aby wysłać na niego pieniądze.

Załóżmy, że Alice ma UTXO o wartości 0,002 BTC i chce otworzyć kanał z Bobem o wartości 0,0013 BTC. Stworzy transakcję z 2 UTXO jako wyjście:

- UTXO o wartości 0,0013 na adres multi-sig 2/2
- UTXO o wartości 0,0007 na jeden z jej adresów reszty (zwrot UTXO).

Ta transakcja nie jest jeszcze publiczna, ponieważ jeśli jest na tym etapie, to Alice ufa Bobowi, że będzie w stanie odblokować pieniądze z multi-sig.

Ale jak dalej postępować?

Alice stworzy drugą transakcję, zwaną "transakcją wypłaty", przed opublikowaniem depozytu środków w multi-sig.

![explication](assets/chapitre3/2.JPG)

Transakcja wypłaty wyda środki z adresu multi-sig na adres należący do niej (jest to zrobione przed opublikowaniem wszystkiego).
Gdy obie transakcje są zbudowane, Alice informuje Boba, że jest gotowe i prosi go o podpis swoim kluczem publicznym, wyjaśniając, że w ten sposób może odzyskać swoje środki, jeśli coś pójdzie nie tak. Bob zgadza się, ponieważ nie jest nieuczciwy.

Alice może teraz sama odzyskać środki, ponieważ już ma podpis Boba. Publikuje transakcje. Kanał jest teraz otwarty z 0,0013 BTC (130 000 SAT) po stronie Alice.

![explication](assets/chapitre3/3.JPG)

## Transakcja Lightning & Transakcja Zobowiązania

![Transakcja Lightning & Transakcja Zobowiązania](https://youtu.be/aPqI34tpypM)

![cover](assets/chapitre4/1.JPG)

Teraz przeanalizujmy, co naprawdę dzieje się za kulisami podczas transferu środków z jednej strony na drugą kanału w Sieci Lightning, z pojęciem transakcji zobowiązania. Transakcja wypłaty/on-chain zamknięcia reprezentuje stan kanału, gwarantując, kto jest właścicielem środków po każdym transferze. Więc po transferze w Sieci Lightning następuje aktualizacja tej transakcji/kontraktu nie wykonanego między dwoma stronami, Alice i Bobem, którzy tworzą tę samą transakcję z aktualnym stanem kanału w przypadku zamknięcia:

- Alice otwiera kanał z Bobem z 130 000 SAT po jej stronie. Transakcja wypłaty zaakceptowana przez obie strony w przypadku zamknięcia stwierdza, że 130 000 SAT trafi do Alice przy zamknięciu, i Bob zgadza się, ponieważ jest to sprawiedliwe.

![cover](assets/chapitre4/2.JPG)

- Alice wysyła 30 000 SAT do Boba. Teraz jest nowa transakcja wypłaty stwierdzająca, że w przypadku zamknięcia, Alice otrzyma 100 000 SAT, a Bob 30 000 SAT. Obie strony zgadzają się, ponieważ jest to sprawiedliwe.

![cover](assets/chapitre4/3.JPG)

- Alice wysyła 10 000 SAT do Boba, i tworzona jest nowa transakcja wypłaty stwierdzająca, że Alice otrzyma 90 000 SAT, a Bob 40 000 SAT w przypadku zamknięcia. Obie strony zgadzają się, ponieważ jest to sprawiedliwe.
![cover](assets/chapitre4/4.JPG)

```
Początkowy stan kanału:
Alice (130,000 SAT) =============== Bob (0 SAT)

Po pierwszym transferze:
Alice (100,000 SAT) =============== Bob (30,000 SAT)

Po drugim transferze:
Alice (90,000 SAT) =============== Bob (40,000 SAT)
```

Pieniądze nigdy się nie przemieszczają, ale końcowy bilans jest aktualizowany za pomocą podpisanej, ale nieopublikowanej transakcji on-chain. Transakcja wypłaty jest więc transakcją zobowiązującą. Transfery satoshi są kolejną, bardziej nowoczesną transakcją zobowiązującą, która aktualizuje bilans.

## Transakcje zobowiązujące

![transactions part 2](https://youtu.be/RRvoVTLRJ84)

Jeśli transakcje zobowiązujące dyktują stan kanału z płynnością w czasie X, czy możemy oszukać, publikując stary stan? Odpowiedź brzmi tak, ponieważ już mamy wstępną sygnaturę obu uczestników w nieopublikowanej transakcji.

![instruction](assets/Chapitre5/0.JPG)

Aby rozwiązać ten problem, dodamy złożoność:

- Timelock = środki zablokowane do bloku N
- Klucz unieważniający = sekret Alice i sekret Boba'

Te dwa elementy są dodawane do transakcji zobowiązującej. W rezultacie, Alice musi czekać na koniec Timelock, a każdy, kto posiada klucz unieważniający, może przesunąć środki bez czekania na koniec Timelock. Jeśli Alice próbuje oszukać, Bob używa klucza unieważniającego, aby ukraść i ukarać Alice.

![instruction](assets/Chapitre5/1.JPG)

Teraz (i w rzeczywistości) transakcja zobowiązująca nie jest taka sama dla Alice i Boba, są symetryczne, ale każda z różnymi ograniczeniami, dają sobie nawzajem swój sekret, aby stworzyć klucz unieważniający poprzedniej transakcji zobowiązującej. Więc przy tworzeniu, Alice tworzy kanał z Bobem, 130,000 SAT po jej stronie, ma Timelock, który uniemożliwia jej natychmiastowe odzyskanie swoich pieniędzy, musi poczekać chwilę. Klucz unieważniający może odblokować pieniądze, ale tylko Alice go ma (transakcja zobowiązująca Alice). Gdy nastąpi transfer, Alice poda swój stary sekret Bobowi, a więc ten ostatni będzie mógł opróżnić kanał do poprzedniego stanu, w przypadku gdyby Alice próbowała oszukać (Alice jest więc karana).

![instruction](assets/Chapitre5/2.JPG)

Podobnie, Bob poda swój sekret Alice. Tak więc, jeśli spróbuje oszukać, Alice może go ukarać. Operacja jest powtarzana dla każdej nowej transakcji zobowiązującej. Decyduje się na nowy sekret i nowy klucz unieważniający. Więc dla każdej nowej transakcji, poprzednia transakcja zobowiązująca musi być zniszczona przez podanie sekretu unieważniającego. W ten sposób, jeśli Alice lub Bob próbują oszukać, druga strona może działać wcześniej (dzięki Timelock) i w ten sposób uniknąć oszustwa. Podczas transakcji nr 3, sekret transakcji nr 2 jest więc podawany, aby umożliwić Alice i Bobowi obronę przed Alice lub Bobem.

![instruction](assets/Chapitre5/3.JPG)

Osoba, która tworzy transakcję z Timelock (ta, która wysyła pieniądze), może użyć klucza unieważniającego tylko po Timelock. Jednak osoba, która otrzymuje pieniądze, może go użyć przed Timelock w przypadku oszustwa z jednej strony na drugą kanału w sieci Lightning. Szczególnie szczegółowo opisujemy mechanizmy, które pozwalają nas chronić przed możliwym oszustwem ze strony naszego partnera w kanale.

## Zamknięcie kanału

![close a channel](https://youtu.be/FVmQvNpVW8Y)
Jesteśmy zainteresowani zamknięciem kanału za pomocą transakcji Bitcoin, które może przyjmować różne formy w zależności od przypadku. Istnieją 3 typy zamknięcia kanału:
- Dobry: kooperacyjne zamknięcie
- Brutalny: wymuszone zamknięcie (niekooperacyjne)
- Oszust: zamknięcie przez oszusta

![instruction](assets/chapitre6/1.JPG)
![instruction](assets/chapitre6/0.JPG)

### Dobry

Dwie strony komunikują się i zgadzają się na zamknięcie kanału. Zatrzymują wszystkie transakcje i walidują ostateczny stan kanału. Zgadzają się na opłaty sieciowe (osoba, która otworzyła kanał, płaci opłaty za zamknięcie). Teraz tworzą transakcję zamknięcia. Jest to transakcja zamknięcia, różna od transakcji zobowiązań, ponieważ nie ma Timelock i klucza unieważnienia. Transakcja jest następnie publikowana, a Alice i Bob otrzymują swoje odpowiednie salda. Ten typ zamknięcia jest szybki (ponieważ nie ma Timelock) i ogólnie niedrogi.

![instruction](assets/chapitre6/3.JPG)

### Brutalny

Alice chce zamknąć kanał, ale Bob nie odpowiada, ponieważ jest offline (internet lub awaria zasilania). Alice wtedy publikuje najnowszą transakcję zobowiązania (ostatnią). Transakcja jest publikowana, a Timelock jest aktywowany. Wtedy, opłaty zostały ustalone, gdy ta transakcja została utworzona X czasu temu! MemPool to sieć, która się od tego czasu zmieniła, więc protokół domyślnie ustala opłaty 5 razy wyższe niż obecne, gdy transakcja została utworzona. Opłata za utworzenie wynosiła 10 SAT, więc transakcja jest rozważana za 50 SAT. W momencie wymuszonego zamknięcia, sieć jest:

- 1 SAT = przepłacono 50*
- 100 SAT = niedopłacono 2*

To sprawia, że wymuszone zamknięcie jest dłuższe (Timelock) i szczególnie bardziej ryzykowne pod względem opłat i możliwej walidacji przez górników.

![instruction](assets/chapitre6/4.JPG)

### Oszust

Alice próbuje oszukać, publikując starą transakcję zobowiązania. Ale Bob monitoruje MemPool i obserwuje transakcje, które próbują opublikować stare. Jeśli znajdzie taką, używa klucza unieważnienia, aby ukarać Alice i zabrać wszystkie SAT z kanału.

![instruction](assets/chapitre6/5.JPG)

Podsumowując, zamknięcie kanału w sieci Lightning jest kluczowym krokiem, który może przyjmować różne formy. W kooperacyjnym zamknięciu, obie strony komunikują się i zgadzają na ostateczny stan kanału. Jest to najszybsza i najtańsza opcja. Z drugiej strony, wymuszone zamknięcie ma miejsce, gdy jedna ze stron nie odpowiada. Jest to droższa i dłuższa sytuacja ze względu na nieprzewidywalne opłaty transakcyjne i aktywację Timelock. Wreszcie, jeśli uczestnik próbuje oszukać, publikując starą transakcję zobowiązania, oszust, może zostać ukarany utratą wszystkich SAT z kanału. Dlatego kluczowe jest zrozumienie tych mechanizmów dla skutecznego i sprawiedliwego korzystania z sieci Lightning.

# Sieć płynności
## Lightning Network

![Lightning Network](https://youtu.be/RAZAa3v41DM)

W tym siódmym rozdziale badamy, jak Lightning działa jako sieć kanałów i jak płatności są kierowane od ich źródła do miejsca docelowego.

![cover](assets/Chapitre7/0.JPG)
![cover](assets/Chapitre7/1.JPG)

Lightning to sieć kanałów płatniczych. Tysiące równorzędnych użytkowników z własnymi kanałami płynności są połączone ze sobą, co umożliwia przeprowadzanie transakcji między niepołączonymi użytkownikami. Płynność tych kanałów nie może być przeniesiona do innych kanałów płynności.
Alice -> Eden -> Bob. Satosze nie przeszły bezpośrednio z `Alice -> Bob`, ale z `Alice -> Eden` i z `Eden -> Bob`.
Tak więc każda osoba i kanał mają różną płynność finansową. Aby dokonać płatności, musisz znaleźć trasę w sieci z wystarczającą płynnością. Jeśli jej nie ma, płatność nie dojdzie do skutku.

Rozważmy następującą sieć:

```
Początkowy stan sieci:
Alice (130 SAT) ==== (0 SAT) Susie (90 SAT) ==== (200 SAT) Eden (150 SAT) ==== (100 SAT) Bob
```
![cover](assets/Chapitre7/2.JPG)

Jeśli Alice ma przelać 40 SAT do Boba, płynność zostanie przesunięta wzdłuż trasy między dwiema stronami.

```
Po przelewie 40 SAT przez Alice do Boba:
Alice (90 SAT) ==== (40 SAT) Susie (50 SAT) ==== (240 SAT) Eden (110 SAT) ==== (140 SAT) Bob
```

![cover](assets/Chapitre7/4.JPG)

Jednak w początkowym stanie Bob nie może wysłać 40 SAT do Alice, ponieważ Susie nie ma żadnej płynności z Alice, aby wysłać 40 SAT, więc płatność nie jest możliwa tą trasą. Dlatego potrzebujemy innej trasy, gdzie transakcja jest niemożliwa.

W pierwszym przykładzie jest jasne, że Susie i Eden nic nie stracili i nic nie zyskali. Węzły Lightning Network pobierają opłatę za zgodę na używanie ich do przekierowania transakcji!

Opłaty różnią się w zależności od lokalizacji płynności

Alice - Bob

- Opłata Alice = Alice -> Bob
- Opłata Boba = Bob -> Alice

![cover](assets/Chapitre7/5.JPG)

Istnieją dwa rodzaje opłat:

- stała opłata niezależna od kwoty: 1 SAT (domyślnie, ale może być zmodyfikowana)
- zmienna opłata (domyślnie 0,01%)

Przykład opłaty:

- Alice - Susie; 1/1 (1 stała opłata i 1 zmienna opłata)
- Susie - Eden; 0/200
- Eden - Bob; 1/1

Zatem:

- Opłata 1: (płatna przez Alice sobie) 1 + (40,000\*0.000001)
- Opłata 2: 0 + 40,000 \* 0.0002 = 8 SAT
- Opłata 3: 1 + 40,000\* 0.000001 = 0.4 SAT

![cover](assets/Chapitre7/6.JPG)

Wysyłka:

1. Wysyłka 40,009.04 Alice -> Susie; Alice płaci własne wydatki, więc to się nie liczy
2. Susie robi przysługę Edenowi, wysyłając 40 001.04; bierze za to prowizję 8 SAT
3. Eden wykonuje usługę wysyłania 40,000 do Boba, bierze swoją opłatę 1.04 SAT.

Alice zapłaciła opłatę 9.04 SAT, a Bob otrzymał 40,000 SAT.

![cover](assets/Chapitre7/7.JPG)

W sieci Lightning to węzeł Alice decyduje o trasie przed wysłaniem płatności. Dlatego szuka się najlepszej trasy i tylko Alice zna trasę i cenę. Płatność jest wysyłana, ale Susie nie ma żadnych informacji.

![cover](assets/Chapitre7/9.JPG)
Dla Susie lub Edena: nie wiedzą, kto jest ostatecznym odbiorcą, ani kto wysyła płatność. To jest routing cebulowy. Węzeł musi zachować plan sieci, aby znaleźć swoją trasę, ale żaden z pośredników nie ma żadnych informacji.
## HTLC - Hashed Time Locked Contract

![HTLC](https://youtu.be/-JC4mkq7H48)

W tradycyjnym systemie routingu, jak możemy zapewnić, że Eden nie oszuka i dotrzyma swojej części umowy?

HTLC to kontrakt płatniczy, który może zostać odblokowany tylko za pomocą sekretu. Jeśli nie zostanie on ujawniony, wówczas kontrakt wygasa. Jest to więc warunkowa płatność. Jak są używane?

![instrukcja](assets/chapitre8/0.JPG)

Rozważmy następującą sytuację:
`Alice (100,000 SAT) ==== (30,000 SAT) Susie (250,000 SAT) ==== (0 SAT) Bob`

- Bob generuje sekret S (preimage) i oblicza hash r = hash(s)
- Bob wysyła fakturę do Alice z dołączonym "r"
- Alice wysyła HTLC o wartości 40,000 SAT do Susie z warunkiem ujawnienia "s'" tak, aby hash(s') = r
- Susie wysyła podobne HTLC do Boba
- Bob odblokowuje HTLC Susie, pokazując jej "s"
- Susie odblokowuje HTLC Alice, pokazując jej "S"

Jeśli Bob jest offline i nigdy nie odzyska sekretu, który daje mu legitymację do otrzymania pieniędzy, wówczas HTLC wygaśnie po określonej liczbie bloków.

![instrukcja](assets/chapitre8/1.JPG)

HTLC wygasają w odwrotnej kolejności: najpierw wygaśnięcie Susie-Bob, a następnie Alice-Susie. W ten sposób, jeśli Bob wróci, to niczego to nie zmienia. W przeciwnym razie, jeśli Alice anuluje, podczas gdy Bob wraca, będzie to bałagan i ludzie mogą pracować na darmo.

Co więc dzieje się w przypadku zamknięcia? W rzeczywistości nasze transakcje zobowiązań są jeszcze bardziej skomplikowane. Musimy przedstawić pośredni bilans, jeśli kanał zostanie zamknięty.

W związku z tym, w transakcji zobowiązań jest HTLC-out o wartości 40,000 satoshi (z ograniczeniami widzianymi wcześniej) poprzez output #3.

![instrukcja](assets/chapitre8/2.JPG)

Alice ma w transakcji zobowiązań:

- Output #1: 60,000 SAT dla Alice przez Timelock i klucz unieważnienia (co dla niej pozostaje)
- Output #2: 30,000, które już należą do Susie
- Output #3: 40,000 w HTLC

Transakcja zobowiązań Alice jest z HTLC-out, ponieważ wysyła HTLC-in do odbiorcy, Susie.

![instrukcja](assets/chapitre8/3.JPG)

W związku z tym, jeśli opublikujemy tę transakcję zobowiązań, Susie może odzyskać pieniądze HTCL z obrazem "s". Jeśli nie ma pre-image, Alice odzyskuje pieniądze po wygaśnięciu HTCL. Pomyśl o outputach (UTXO) jako o różnych płatnościach z różnymi warunkami.
Gdy płatność zostanie wykonana (wygaśnięcie lub wykonanie), stan kanału zmienia się i transakcja z HTCL już nie istnieje. Wrócimy do czegoś klasycznego.
W przypadku kooperacyjnego zamknięcia: zatrzymujemy płatności i w związku z tym czekamy na wykonanie transferów/HTCL, transakcja jest lekka, więc mniej kosztowna, ponieważ są maksymalnie 1 lub 2 outputy.
Jeśli wymuszone zamknięcie: publikujemy ze wszystkimi trwającymi HTLC, więc staje się to bardzo obciążające i bardzo kosztowne. I to jest bałagan.
Podsumowując, system routingu w Sieci Lightning wykorzystuje Kontrakty z Blokadą Czasową i Hashem (HTLC) do zapewnienia bezpiecznych i weryfikowalnych płatności. HTLC umożliwiają płatności warunkowe, gdzie pieniądze mogą zostać odblokowane tylko za pomocą sekretu, co zapewnia, że uczestnicy wypełniają swoje zobowiązania. W przedstawionym przykładzie, Alicja chce wysłać SAT do Boba przez Susie. Bob generuje sekret, tworzy z niego hash i przekazuje go Alicji. Alicja i Susie ustanawiają HTLC oparte na tym hashu. Gdy Bob odblokuje HTLC Susie, pokazując jej sekret, Susie może następnie odblokować HTLC Alicji.
W przypadku, gdy Bob nie ujawni sekretu w określonym czasie, HTLC wygasa. Wygaśnięcie następuje w odwrotnej kolejności, co zapewnia, że jeśli Bob wróci online, nie ma niepożądanych konsekwencji.

Przy zamykaniu kanału, jeśli jest to zamknięcie współpracujące, płatności są przerywane, a HTLC są rozwiązywane, co jest generalnie mniej kosztowne. Jeśli zamknięcie jest wymuszone, wszystkie trwające transakcje HTLC są publikowane, co może stać się bardzo kosztowne i skomplikowane.
Podsumowując, mechanizm HTLC dodaje dodatkową warstwę bezpieczeństwa do Sieci Lightning, zapewniając, że płatności są wykonane poprawnie i że użytkownicy wypełniają swoje zobowiązania.

## Znajdowanie drogi

![znajdowanie drogi](https://youtu.be/wnUGJjOxd9Q)

Jedynymi publicznymi danymi jest całkowita pojemność kanału (Alicja + Bob), ale nie wiemy, gdzie znajduje się płynność.
Aby uzyskać więcej informacji, nasz węzeł nasłuchuje kanału komunikacyjnego LN w poszukiwaniu ogłoszeń o nowych kanałach i aktualizacjach opłat za kanał. Twój węzeł również sprawdza blockchain pod kątem zamknięć kanałów.

Ponieważ nie mamy wszystkich informacji, musimy szukać grafu/trasy z informacjami, które posiadamy (maksymalna pojemność kanału, a nie gdzie znajduje się płynność).

Kryteria:

- Prawdopodobieństwo sukcesu - Opłaty
- Czas wygaśnięcia HTLC
- Liczba pośrednich węzłów
- Losowość

![graf](assets/chapitre9/1.JPG)

Więc jeśli są 3 możliwe trasy:

- Alicja > 1 > 2 > 5 > Bob
- Alicja > 1 > 2 > 4 > 5 > Bob
- Alicja 1 > 2 > 3 > Bob

Szukamy teoretycznie najlepszej trasy z najniższymi opłatami i największą szansą na sukces: maksymalna płynność i jak najmniej skoków.

Na przykład, jeśli 2-3 ma tylko pojemność 130 000 SAT, wysłanie 100 000 jest bardzo mało prawdopodobne, więc wybór nr 3 nie ma szans na sukces.

![graf](assets/chapitre9/2.JPG)

Teraz algorytm dokonał swoich 3 wyborów i spróbuje pierwszego:

Wybór 1:

- Alicja wysyła HTLC o wartości 100 000 SAT do 1;
- 1 tworzy HTLC o wartości 100 000 SAT do 2;
- 2 tworzy HTLC o wartości 100 000 SAT do 5, ale 5 nie może tego zrobić, więc to ogłasza.

Informacja jest wysyłana z powrotem, więc Alicja decyduje się spróbować drugiej trasy:

- Alicja wysyła HTLC o wartości 100 000 do 1;
- 1 tworzy HTLC o wartości 100 000 do 2;
- 2 tworzy HTLC o wartości 100 000 do 4;
- 4 tworzy HTLC o wartości 100 000 do Boba. Bob ma płynność, więc jest w porządku.
- Bob używa preimage (hash) HTLC i w ten sposób używa sekretu, aby odzyskać 100 000 SAT
- 5 teraz ma sekret HTLC, aby odzyskać zablokowane HTLC od 4
- 4 teraz posiada sekret HTLC, aby odzyskać zablokowany HTLC od 2
- 2 teraz posiada sekret HTLC, aby odzyskać zablokowany HTLC od 1
- 1 teraz posiada sekret HTLC, aby odzyskać zablokowany HTLC Alice

Alice nie zauważyła niepowodzenia trasy 1, po prostu poczekała sekundę dłużej. Niepowodzenie płatności występuje, gdy nie ma możliwej trasy. Aby ułatwić wyszukiwanie trasy, Bob może dostarczyć Alice informacje, które pomogą jej z fakturą:

- Kwota
- Jego adres
- Hash preimage, aby Alice mogła stworzyć HTLC
- Wskazówki dotyczące kanałów Boba

Bob zna płynność kanałów 5 i 3, ponieważ jest bezpośrednio z nimi połączony, może to wskazać Alice. Ostrzega Alice, że węzeł 3 jest bezużyteczny, co zapobiega potencjalnemu tworzeniu przez nią trasy.
Innym elementem mogą być prywatne kanały (a więc niepublikowane w sieci), które Bob może mieć. Jeśli Bob ma prywatny kanał z 1, może powiedzieć Alice, aby go użyła, co dałoby Alice > 1 > Bob'.

![graph](assets/chapitre9/3.JPG)

Podsumowując, trasowanie transakcji w sieci Lightning jest skomplikowanym procesem, który wymaga uwzględnienia różnych czynników. Chociaż całkowita pojemność kanałów jest publiczna, dokładny rozkład płynności nie jest bezpośrednio dostępny. Zmusza to węzły do szacowania najbardziej prawdopodobnych udanych tras, biorąc pod uwagę kryteria takie jak opłaty, czas wygaśnięcia HTLC, liczba pośrednich węzłów i czynnik losowości. Gdy możliwe są wielokrotne trasy, węzły starają się minimalizować opłaty i maksymalizować szanse na sukces, wybierając kanały z wystarczającą płynnością i minimalną liczbą skoków. Jeśli próba transakcji nie powiedzie się z powodu niewystarczającej płynności, próbuje się innej trasy, aż do wykonania udanej transakcji.

Ponadto, aby ułatwić wyszukiwanie trasy, odbiorca może dostarczyć dodatkowe informacje, takie jak adres, kwota, hash preimage i wskazówki dotyczące swoich kanałów. Może to pomóc zidentyfikować kanały z wystarczającą płynnością i uniknąć niepotrzebnych prób transakcji. Ostatecznie system trasowania sieci Lightning jest zaprojektowany tak, aby optymalizować szybkość, bezpieczeństwo i efektywność transakcji, jednocześnie zachowując prywatność użytkownika.

# Narzędzia sieci Lightning
## Faktura, LNURL, Keysend

![invoice, LNURL, Keysend](https://youtu.be/CHnXJuZTarU)

![cover](assets/chapitre10/0.JPG)

Faktura LN (lub faktura) jest długa i nieprzyjemna do czytania, ale pozwala na gęste przedstawienie żądania płatności.

Przykład:
lnbc1m1pskuawzpp5qeuuva2txazy5g483tuv9pznn9ft8l5e49s5dndj2pqq0ptyn8msdqqcqzpgxqrrsssp5v4s00u579atm0em6eqm9nr7d0vr64z5j2sm5s33x3r9m4lgfdueq9qyyssqxkjzzgx5ef7ez3dks0laxayx4grrw7j22ppgzyhpydtv6hmc39skf9hjxn5yd3kvv7zpjdxd2s7crcnemh2fz26mnr6zu83w0a2fwxcqnvujl3

- lnbc1m = czytelna część
- 1 = oddzielenie od reszty
- Potem reszta
- Bc1 = Kodowanie Bech32 (baza 32), więc używanych jest 32 znaków.
- 10 = 1.2.3.4.5.6.7.8.9.0
- 26 = abcdefghijklmnopqrstuvwxyz
- 32 = nie "b-i-o" i nie "1"

### lnbc1m

- ln = Lightning
- Bc = bitcoin (mainnet)
- 1 = kwota
- M = milli (10^-3 / u = micro 10^-6 / n = nano 10^-9 / p = pico 10^-12'
  Tutaj 1m = 1 \* 0.0001btc = 100,000 BTC
  "Proszę zapłacić 100,000 SAT w sieci Lightning sieci Bitcoin mainnet do pskuawzpp5qeuuva2txazy5g483tuv9pznn9ft8l5e49s5dndj2pqq0ptyn8msdqqcqzpgxqrrsssp5v4s00u579atm0em6eqm9nr7d0vr64z5j2sm5s33x3r9m4lgfdueq9qyyssqxkjzzgx5ef7ez3dks0laxayx4grrw7j22ppgzyhpydtv6hmc39skf9hjxn5yd3kvv7zpjdxd2s7crcnemh2fz26mnr6zu83w0a2fwxcqnvujl3"

### Timestamp (kiedy zostało utworzone)

Zawiera 0 lub więcej dodatkowych części:

- Hash preimage
- Tajemnica płatności (onion routing)
- Dowolne dane
- Publiczny klucz LN odbiorcy
- Czas wygaśnięcia (domyślnie 1 godzina)
- Wskazówki dotyczące routingu
- Podpis całego

Istnieją inne typy faktur. Meta-protokół LNURL pozwala na podanie bezpośredniej kwoty w satoshi zamiast składania wniosku. Jest to bardzo elastyczne i pozwala na wiele ulepszeń pod względem doświadczenia użytkownika.

![cover](assets/chapitre10/2.JPG)

Keysend pozwala Alicji wysłać pieniądze do Boba bez konieczności posiadania jego prośby. Alicja pobiera ID Boba, tworzy preimage bez pytania Boba i dołącza go do swojej płatności. W ten sposób Bob otrzyma niespodziewaną prośbę, gdzie może odblokować pieniądze, ponieważ Alicja już wykonała pracę.

![cover](assets/chapitre10/3.JPG)

Podsumowując, faktura sieci Lightning, choć na pierwszy rzut oka wydaje się skomplikowana, skutecznie koduje prośbę o płatność. Każda sekcja faktury zawiera kluczowe informacje, w tym kwotę do zapłaty, odbiorcę, znacznik czasu utworzenia i potencjalnie inne informacje, takie jak hash preimage, tajemnica płatności, wskazówki dotyczące routingu i czas wygaśnięcia. Protokoły takie jak LNURL i Keysend oferują znaczące ulepszenia pod względem elastyczności i doświadczenia użytkownika, pozwalając na przykład na wysyłanie środków bez wcześniejszej prośby od drugiej strony. Te technologie czynią proces płatności płynniejszym i bardziej efektywnym w sieci Lightning.

## Zarządzanie płynnością

![zarządzanie płynnością](https://youtu.be/YuPrbhEJXbg)

![instrukcja](assets/chapitre11/0.JPG)

Podajemy kilka ogólnych wytycznych, aby odpowiedzieć na wieczne pytanie o zarządzanie płynnością w Lightning.

W LN są 3 typy osób:

- Kupujący: mają oni płynność wychodzącą, co jest najprostsze, ponieważ wystarczy, że otworzą kanały
- Sprzedawcy: jest to bardziej skomplikowane, ponieważ potrzebują oni płynności przychodzącej od innych węzłów i aktorów. Muszą mieć osoby połączone z nimi
- Węzły routingu: chcą być zbilansowane z płynnością po obu stronach i mieć dobre połączenie z wieloma węzłami, aby być używanymi jak najczęściej.
Więc jeśli potrzebujesz przychodzącej płynności, możesz ją kupić od usług.

![instruction](assets/chapitre11/1.JPG)

Alice kupuje kanał z Susie za 1 milion satoshi, więc otwiera kanał bezpośrednio z 1,000,000 SAT po stronie przychodzącej. Może wtedy przyjąć do 1 miliona SAT w płatnościach od klientów, którzy są połączeni z Susie (która ma dobre połączenia).

Innym rozwiązaniem byłoby dokonywanie płatności; płacisz 100,000 z jakiegoś powodu, teraz możesz otrzymać 100,000.

![instruction](assets/chapitre11/2.JPG)

### Rozwiązanie Loop Out: Atomic swap LN - BTC

Alice 2 miliony - Susie 0

![instruction](assets/chapitre11/3.JPG)

Alice chce wysłać płynność do Susie, więc wykonuje Loop out (specjalny węzeł, który oferuje profesjonalną usługę do rebalansowania LN/BTC).
Alice wysyła 1 milion do Loop przez węzeł Susie, więc Susie ma płynność, a Loop wysyła saldo on-chain z powrotem do węzła Alice.

![instruction](assets/chapitre11/4.JPG)

Więc 1 milion idzie do Susie, Susie wysyła 1 milion do Loop, Loop wysyła 1 milion do Alice. Alice w ten sposób przeniosła płynność do Susie, ponosząc koszty opłat zapłaconych Loop za usługę.

Najtrudniejszą rzeczą w LN jest utrzymanie płynności.

![instruction](assets/chapitre11/5.JPG)

Podsumowując, zarządzanie płynnością w sieci Lightning jest kluczową kwestią, która zależy od typu użytkownika: kupującego, sprzedawcy lub węzła routingu. Kupujący, którzy potrzebują wychodzącej płynności, mają najprostsze zadanie: po prostu otwierają kanały. Sprzedawcy, którzy wymagają przychodzącej płynności, muszą być połączeni z innymi węzłami i aktorami. Węzły routingu, z kolei, dążą do utrzymania równowagi płynności po obu stronach. Istnieje kilka rozwiązań do zarządzania płynnością, takich jak zakup kanałów lub płacenie za zwiększenie zdolności odbiorczej. Opcja "Loop Out", pozwalająca na Atomic Swap między LN a BTC, oferuje interesujące rozwiązanie do rebalansowania płynności. Pomimo tych strategii, utrzymanie płynności w sieci Lightning pozostaje skomplikowanym wyzwaniem.

# Idź dalej
## Podsumowanie kursu

![conclusion](https://youtu.be/MaWpD0rbkVo)

Naszym celem było wyjaśnienie, jak działa sieć Lightning i jak opiera się na Bitcoinie.

Sieć Lightning to sieć kanałów płatniczych. Widzieliśmy, jak działa kanał płatniczy między dwoma stronami, ale również rozszerzyliśmy naszą wizję na całą sieć, na pojęcie sieci kanałów płatniczych.

![instruction](assets/chapitre12/0.JPG)

Kanały są otwierane za pomocą transakcji Bitcoin i mogą pomieścić jak najwięcej transakcji. Stan kanału jest reprezentowany przez transakcję zobowiązującą, która wysyła każdemu uczestnikowi to, co mają po swojej stronie kanału. Gdy w kanału występuje transakcja, uczestnicy zobowiązują się do nowego stanu, unieważniając stary stan i tworząc nową transakcję zobowiązującą.

![instruction](assets/chapitre12/1.JPG)

Pary chronią się przed oszustwem za pomocą kluczy unieważniających i blokady czasowej. Zamknięcie za wzajemną zgodą jest preferowane do zamknięcia kanału. W przypadku wymuszonego zamknięcia publikowana jest ostatnia transakcja zobowiązująca.

![instruction](assets/chapitre12/3.JPG)
Płatności mogą pożyczać kanały od innych pośrednich węzłów. Warunkowe płatności oparte na blokadzie czasowej hash (HTLC) pozwalają zablokować środki do momentu całkowitego rozwiązania płatności. W sieci Lightning używane jest routowanie cebulowe. Pośrednie węzły nie znają ostatecznego miejsca docelowego płatności. Alicja musi obliczyć trasę płatności, ale nie ma wszystkich informacji o płynności w pośrednich kanałach.
![instrukcja](assets/chapitre12/4.JPG)

Przy wysyłaniu płatności przez sieć Lightning występuje składowa prawdopodobieństwa.

![instrukcja](assets/chapitre12/5.JPG)

Aby otrzymywać płatności, należy zarządzać płynnością w kanałach, co można zrobić, prosząc innych o otwarcie kanałów do nas, otwierając kanały samodzielnie oraz korzystając z narzędzi takich jak Loop lub kupując/wynajmując kanały na rynkach.

## Wywiad z Fanisem

![Wywiad z Fanisem](https://youtu.be/VeJ4oJIXo9k)

Oto podsumowanie wywiadu:

Sieć Lightning to ultranowoczesne rozwiązanie płatnicze w Bitcoinie, które pozwala ominąć ograniczenia związane ze skalowalnością sieci. Jednakże bitcoiny w sieci Lightning nie są tak bezpieczne, jak te na łańcuchu Bitcoin, ponieważ priorytetem jest decentralizacja i bezpieczeństwo kosztem skalowalności.

Nadmierne zwiększanie rozmiaru bloku nie jest dobrym rozwiązaniem, ponieważ kompromituje węzły i pojemność danych. Zamiast tego, sieć Lightning umożliwia tworzenie kanałów płatniczych między dwoma użytkownikami Bitcoina bez pokazywania transakcji na blockchainie, oszczędzając miejsce w blokach i umożliwiając skalowanie Bitcoina już dziś.

Jednakże istnieją krytyki dotyczące skalowalności i centralizacji sieci Lightning, z potencjalnymi problemami związanymi z zamknięciem kanałów i wysokimi opłatami transakcyjnymi. Aby rozwiązać te problemy, zaleca się unikanie otwierania małych kanałów, aby uniknąć przyszłych problemów oraz zwiększenie opłat transakcyjnych za pomocą Child Pay for Parent.

Rozwiązania rozważane na przyszłość sieci Lightning to grupowanie transakcji i tworzenie kanałów w grupach w celu zmniejszenia opłat transakcyjnych, jak również zwiększenie rozmiaru bloku w dłuższej perspektywie. Jednakże ważne jest, aby zauważyć, że bitcoiny w sieci Lightning nie są tak bezpieczne, jak bitcoiny na łańcuchu Bitcoin.

Prywatność w Bitcoinie i Lightning są powiązane, z routowaniem cebulowym zapewniającym pewien poziom prywatności dla transakcji. Jednakże w Bitcoinie wszystko jest domyślnie transparentne, z heurystykami używanymi do śledzenia Bitcoinów z adresu na adres na łańcuchu Bitcoin.

Kupowanie Bitcoinów z KYC pozwala giełdzie znać transakcje wypłaty, podczas gdy okrągłe kwoty i adresy reszty pozwalają wiedzieć, która część transakcji jest przeznaczona dla innej osoby, a która część dla siebie.

Aby poprawić prywatność, wspólne działania i coinjoins pozwalają łamać obliczenia prawdopodobieństwa, wykonując transakcje, w których wiele osób dokonuje transakcji razem. Firmy analizujące łańcuch mają trudności z ustaleniem, co robisz ze swoimi bitcoinami, śledząc.

W sieci Lightning tylko dwie osoby są świadome transakcji, i jest to bardziej poufne niż w Bitcoinie. Routowanie cebulowe oznacza, że pośredni węzeł nie zna nadawcy i odbiorcy płatności.

Aby korzystać z sieci Lightning, zaleca się odbycie szkolenia na kanale YouTube lub bezpośrednio na stronie discover Bitcoin, lub skorzystanie ze szkolenia na Umbrell. Możliwe jest również wysyłanie dowolnego tekstu podczas płatności w sieci Lightning za pomocą dedykowanego pola, co może być przydatne dla darowizn lub komunikacji.
Jednakże ważne jest, aby zauważyć, że węzły routingu Lightning mogą być regulowane w przyszłości, z niektórymi państwami próbującymi regulować węzły routingu. Dla sprzedawców konieczne jest zarządzanie płynnością, aby akceptować płatności w sieci Lightning, z obecnymi ograniczeniami, które można pokonać z odpowiednimi rozwiązaniami.

Wreszcie, przyszłość Bitcoina jest obiecująca z możliwą projekcją jednego miliona w ciągu pięciu lat. Aby zapewnić profesjonalizację branży i stworzenie alternatywnego systemu dla istniejącego systemu bankowego, ważne jest, aby przyczyniać się do sieci i przestać ufać.

## Podziękowania i kontynuuj zgłębianie króliczej nory
Gratulacje! 🎉Ukończyłeś szkolenie LN 201 - Wprowadzenie do Lightning Network!
Możesz być dumny z siebie, ponieważ to nie jest łatwe. Wiedz, że niewiele osób zagłębia się tak głęboko w króliczą norę Bitcoina.

Przede wszystkim, wielkie podziękowania dla Fanisa Makalakisa za oferowanie nam tego wspaniałego darmowego kursu na bardziej etniczny aspekt Lightning. Nie wahaj się śledzić go na Twitterze, na jego blogu, czy poprzez jego pracę na rynku LN.

Następnie, jeśli chcesz pomóc projektowi, nie wahaj się sponsorować nas na Patreonie. Twoje darowizny zostaną wykorzystane do produkcji treści na nowe kursy szkoleniowe i oczywiście, będziesz pierwszy informowany (w tym o następnym kursie Fanisa, który jest w przygotowaniu!).

Przygoda z Lightning Network kontynuuje się z treningiem Umbrel i implementacją węzła Lightning Network. Teoria się skończyła i czas na praktykę z teraz z treningiem LN 202!

Całusy i do zobaczenia wkrótce!

Rogzy'