---
name: Zagłębianie się w Simplicity
goal: Opanować filozofię projektowania, system typów i pełny cykl życia Simplicity
objectives:
  - Zrozumieć trzy fundamentalne metody kompozycji oraz dziewięć kombinatorów tworzących kompletny język
  - Zbudować logikę boolowską, arytmetykę i SHA-256 z minimalnego systemu typów Simplicity
  - Uchwycić, w jaki sposób efekty uboczne Failure i Reader umożliwiają rzeczywistą interakcję z blockchainem
  - Nauczyć się, jak programy Simplicity stają się adresami Taproot i są realizowane za pomocą danych świadka
---

# Zagłębianie się w Simplicity

Dogłębne omówienie teorii i decyzji projektowych stojących za językiem Simplicity, oparte na kompletnej, pięcioczęściowej serii artykułów ["Zagłębianie się w Simplicity"](https://delvingbitcoin.org/t/delving-simplicity-part-three-fundamental-ways-of-combining-computations/1902) autorstwa [dr. Russella O'Connora](https://r6.ca/), twórcy Simplicity w Blockstream Research. Ten kurs wyjaśnia, *dlaczego* Simplicity zaprojektowano właśnie w ten sposób, a nie jak w nim pisać.

Kurs podąża za artykułami dr. O'Connora przez trzy fundamentalne sposoby łączenia obliczeń, minimalny system typów i twierdzenie o jego kompletności, budowanie praktycznych typów danych i arytmetyki od pierwszych zasad, ostrożne wprowadzenie efektów ubocznych do interakcji z blockchainem, a na końcu pokazuje, jak programy są zobowiązywane do adresów i realizowane on-chain.

+++

# Wprowadzenie

<partId>c362889b-c630-435f-911b-724c4eca505b</partId>

## Przegląd kursu

<chapterId>cdcc40b6-c985-45b4-9bee-6f931e984476</chapterId>

Witamy w SCR403 — Zagłębianie się w Simplicity!

Ten kurs jest oparty na serii artykułów **"Delving Simplicity"** napisanej przez [dr. Russella O'Connora](https://r6.ca/), Infrastructure Tech Developer w [Blockstream](https://blockstream.com/) i twórcę Simplicity. Oryginalne artykuły zostały opublikowane na forum [Delving Bitcoin](https://delvingbitcoin.org/u/roconnor-blockstream/summary) i stanowią podstawowy materiał źródłowy dla tego kursu. Jesteśmy wdzięczni za jego pionierską pracę, która umożliwiła powstanie tej treści edukacyjnej.

### Czego się nauczysz

Ten kurs omawia filozofię projektowania i matematyczne podstawy Simplicity, języka skryptowego nowej generacji aktywowanego w [Liquid Network](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/) w lipcu 2025 roku. Podąża za pełną, pięcioczęściową serią artykułów i jest podzielony na dwie główne sekcje treści:

1. **Podstawy Simplicity** — dlaczego obliczenia blockchainowe wymagają zasadniczo innego języka, trzy sposoby łączenia operacji (sekwencyjny, równoległy, warunkowy) oraz dziewięć podstawowych kombinatorów tworzących matematycznie kompletny język
2. **Od typów danych do programów** — budowanie logiki boolowskiej, arytmetyki i SHA-256 od pierwszych zasad; zrozumienie efektów ubocznych Failure i Reader, które umożliwiają interakcję z blockchainem; oraz nauka tego, jak programy są zobowiązywane do adresów Taproot za pośrednictwem Commitment Merkle Roots i realizowane danymi świadka

### Wymagania wstępne

To kurs na **poziomie eksperckim** (około 10 godzin). Powinieneś swobodnie rozumieć:
- Podstawowe koncepcje skryptów Bitcoin (co robi walidacja transakcji)
- Fundamentalne koncepcje programowania (typy, funkcje, kompozycja)
- Pewna znajomość notacji matematycznej jest pomocna, ale nie wymagana. Wszystko wprowadzamy na bieżąco

### Kluczowe zasoby

- **Oryginalne artykuły**: ["Delving Simplicity"](https://delvingbitcoin.org/u/roconnor-blockstream/summary) autorstwa dr. Russella O'Connora na Delving Bitcoin
- **Repozytorium Simplicity**: [BlockstreamResearch/simplicity](https://github.com/BlockstreamResearch/simplicity) — kod źródłowy i formalne dowody Rocq
- **Oficjalna strona**: [simplicity-lang.org](https://simplicity-lang.org/) — dokumentacja i odniesienie SimplicityHL
- **Blog Blockstream**: [Simplicity na GitHubie](https://blog.blockstream.com/en-simplicity-github/) — przegląd techniczny

Gotowy, by zanurzyć się w jednym z najbardziej eleganckich fragmentów inżynierii Bitcoin? Zaczynajmy!

## Czym jest Simplicity?

<chapterId>d04f3960-d7fb-44e1-b5a3-25b33d03fd38</chapterId>

Jeśli podchodzisz do tego kursu bez wcześniejszego kontaktu z Simplicity, ten rozdział pomoże ci się zorientować, zanim wejdziemy na głęboką wodę.

### Simplicity w pigułce

Simplicity to **natywny dla Bitcoin język inteligentnych kontraktów**, działający dziś w Liquid Network. Po raz pierwszy wyobrażony przez dr. Russella O'Connora około 2012 roku i szczegółowo opisany w jego pracy z 2017 roku *Simplicity: A New Language for Blockchains*, został aktywowany w Liquid Network w lipcu 2025 roku po latach formalnej weryfikacji i rozwoju.

W przeciwieństwie do Solidity z Ethereum, który jest Turingowo kompletnym, wysokopoziomowym językiem kontraktów, Simplicity jest celowo minimalny. Ma:
- **Trzy konstruktory typów** (jednostkę, sumę, iloczyn)
- **Dziewięć kombinatorów** (podstawowe operacje i reguły kompozycji)
- **Brak pętli, brak rekurencji, brak pamięci dynamicznej**

Z samych tych prymitywów można zbudować dowolne obliczenie potrzebne do walidacji transakcji, od logiki boolowskiej po pełne haszowanie SHA-256.

### Co można dziś robić z Simplicity?

Simplicity napędza już rzeczywiste aplikacje w Liquid Network. Najbardziej godna uwagi to [Simplicity DEX](https://docs.simplicity-lang.org/use-cases/simplicity-dex/), rynek opcji bez wyroczni, gdzie użytkownicy handlują opcjami call na L-BTC, używając USDt jako zabezpieczenia (bazowy kontrakt obsługuje również opcje put). Inne działające projekty Simplicity obejmują [Swaption](https://swaption.io/) od SideSwap (opcje) oraz open-source'owy [Deadcat](https://github.com/Resolvr-io/deadcat) od Resolvr (rynki predykcyjne). Poza DeFi Simplicity umożliwia zaawansowane warunki wydawania, takie jak skarbce, covenanty i złożone schematy multisig, które byłyby niemożliwe albo niebezpieczne w Bitcoin Script.

### Czym ten kurs jest — i czym nie jest

To **nie** jest praktyczny samouczek programowania. Nie będziesz tu pisać programów Simplicity. Jeśli tego szukasz, sprawdź:
- [simplicity-lang.org](https://simplicity-lang.org/) — oficjalną dokumentację i wysokopoziomowy język SimplicityHL
- [Repozytorium Simplicity na GitHubie](https://github.com/BlockstreamResearch/simplicity) — implementację referencyjną, przykłady i dowody Rocq
- [Wpis na blogu Blockstream](https://blog.blockstream.com/en-simplicity-github/) o pierwszych krokach

O czym ten kurs **jest**: o **filozoficznych i technicznych wyborach** stojących za projektem Simplicity. Dlaczego ten język powstał w taki sposób? Dlaczego tylko dziewięć kombinatorów? Dlaczego bez rekurencji? Dlaczego ma znaczenie, że system typów łączy się z rachunkiem sekwentów Gentzena?

Pomyśl o tym jak o zrozumieniu **dlaczego silnik zbudowano właśnie tak**, a nie jak o nauce prowadzenia samochodu.

### Dla kogo to jest?

Ten kurs jest idealny dla:
- **Deweloperów protokołów**, którzy chcą zrozumieć podstawy Simplicity przed pisaniem kodu
- **Badaczy Bitcoin**, zainteresowanych formalną weryfikacją i podejściem teoriotypowym
- **Informatyków teoretycznych**, ciekawych związku między rachunkiem sekwentów a obliczeniami blockchainowymi
- **Zaawansowanych bitcoinerów**, którzy chcą wyjść poza powierzchowne rozumienie możliwości skryptowych Liquid

Jeśli terminy takie jak "typy sumy", "kombinatory" czy "rachunek sekwentów" są dla ciebie zupełnie nowe, nie martw się, wyjaśniamy wszystko od zera. Przygotuj się jednak na gęstą, matematyczną podróż.

### Od artykułów do kursu

Oryginalna seria "Delving Simplicity" dr. O'Connora jest zorganizowana jako pięć artykułów technicznych. Ten kurs reorganizuje i opatruje adnotacjami ten materiał jako progresywną ścieżkę nauki z quizami sprawdzającymi zrozumienie po drodze. Idee, definicje i dowody są jego autorstwa, a my dostosowaliśmy format do ustrukturyzowanej edukacji.

# Podstawy Simplicity

<partId>a5976618-94ab-4b29-b9aa-040d35c68e5d</partId>

## Fundamentalne sposoby łączenia obliczeń

<chapterId>6d46e77a-7e60-473b-b230-418da5ae44eb</chapterId>

Teraz, gdy Simplicity zostało aktywowane w Liquid Network, chciałbym dogłębnie omówić filozofię i projekt języka Simplicity.

Walidacja transakcji Bitcoin jest zastosowaniem znacząco różnym od zwykłego projektowania języków programowania. Przestrzeń blokowa jest bardzo kosztowna, więc programy muszą być zwarte. Programy w transakcjach Bitcoin są zawsze wykonywane tylko na jednym wejściu, a każdy wykonuje program na tym samym wejściu. Ponadto podmiot autoryzujący transakcję zna z góry wynik obliczenia: wie, że transakcja jest ważna.

Zazwyczaj podmiot autoryzujący uruchamia znacznie droższe obliczenia, aby wyprowadzić dane świadka poświadczające ważność transakcji, podczas gdy programy uruchamiane na blockchainie muszą sprawdzić ważność danych świadka. Sprawdzenie ważności jest często znacznie tańsze niż udowodnienie ważności.

Zaprojektowaliśmy Simplicity z myślą o tego rodzaju wyjątkowych wyzwaniach projektowania języka. Na przykład Simplicity wymaga przycinania niewykonanych gałęzi, aby nie pojawiały się na blockchainie. Kroki wstępnego przetwarzania są starannie zaprojektowane tak, aby wykazywać (quasi-)liniową złożoność czasową względem rozmiaru programu Simplicity. Zamiast "gazu" używa się analizy statycznej, której — w przeciwieństwie do gazu — nie trzeba obliczać przez wykonywanie kodu w określony sposób, dzięki czemu szczegóły modelu wykonania nie stają się krytyczne dla konsensusu. Brak dynamicznej alokacji pamięci podczas wykonania. I tak dalej.

Zanim zagłębimy się w szczegóły projektu Simplicity, chcę rozpocząć tę serię od pewnej filozofii programowania dotyczącej ogólnych sposobów łączenia podstawowych bloków budulcowych w celu tworzenia nowej funkcjonalności.

### Kompozycja

Załóżmy, że projektuje się język programowalnych transakcji dla blockchaina takiego jak Bitcoin. W szczególności programy mają dostęp tylko do danych transakcji i danych UTXO wejść, a wykonanie określa wyłącznie ważność transakcji (co pozwala buforować wynik wykonania). Powiedzmy, że zaczyna się od pewnego zestawu podstawowych operacji, które mogą wykonywać różne zadania, takie jak podstawowe obliczenia, odczytywanie i/lub przetwarzanie danych z transakcji oraz weryfikacja podpisu. Każda operacja zużywa pewien typ wejścia (być może pusty) i zwraca pewien typ wyjścia. Jakimi sposobami możemy łączyć te podstawowe operacje w bardziej złożone operacje?

### Kompozycja sekwencyjna

![Kompozycja sekwencyjna](assets/en/001.webp)

Najbardziej fundamentalną metodą kompozycji jest kompozycja sekwencyjna. Jeśli mamy dwie podstawowe operacje, z których typ danych wyjściowych jednej odpowiada typowi danych wejściowych drugiej, możemy połączyć te dwie operacje w nową operację złożoną. Ta nowa operacja uruchamia te dwie podstawowe operacje po kolei, przyjmując jako wejście wejście pierwszej operacji, przekazując wyjście tej pierwszej operacji na wejście drugiej operacji, a ostatecznie zwracając wyjście tej drugiej operacji.

Oczywiście nie musimy ograniczać się tylko do łączenia podstawowych operacji. Skoro mamy już pewne operacje złożone, możemy je również łączyć za pomocą kompozycji funkcji.

W matematyce tę kompozycję sekwencyjną często nazywa się po prostu "kompozycją" i można by pomyśleć, że to jedyny sposób składania rzeczy. Mamy jednak także inne sposoby łączenia operacji.

### Kompozycja równoległa

![Kompozycja równoległa](assets/en/002.webp)

Załóżmy, że mamy dwie operacje, które mogą być operacjami podstawowymi albo złożonymi, i obie przyjmują ten sam typ wejścia. Drugim fundamentalnym sposobem kompozycji tych dwóch operacji jest wykonanie ich obu na tym samym wejściu. Nazywa się to kompozycją równoległą, a typem wyjścia jest "iloczyn" typów wyjść pierwotnych operacji i zawiera parę tych dwóch wyjść.

Choć nazywa się to kompozycją "równoległą", a obie operacje w zasadzie mogłyby być wykonywane równolegle, równoległe wykonanie nie jest wymaganiem operacyjnym. Kompozycję równoległą możemy zaimplementować "sekwencyjnie", wykonując najpierw jedną operację, a następnie drugą. Nie obchodzą nas szczegóły implementacji kompozycji równoległej, dopóki wyjście jest takie samo.

### Kompozycja warunkowa

![Kompozycja warunkowa](assets/en/003.webp)

Kompozycja warunkowa jest dualna względem kompozycji równoległej. W tym przypadku mamy dwie operacje, które produkują to samo wyjście, i składamy je przez wybranie jednej z nich do wykonania. Wejściem tej operacji złożonej jest "suma" albo "unia tagowana" typów wejść pierwotnych operacji. W tym przypadku tag, "Left" albo "Right", jest pojedynczym bitem w danych wejściowych, który określa, jaki typ danych jest przenoszony, a zatem którą z dwóch operacji można wykonać.

Kompozycja warunkowa działa tak samo nawet wtedy, gdy wejście jest sumą dwóch identycznych typów. Typ sumy nadal zawiera tag, a wartość tego tagu określa, która z dwóch operacji ma zostać wykonana.

### Kompozycja w Bitcoin Script

Istnieje wiele sposobów realizowania tych trzech rodzajów kompozycji w różnych językach programowania. W Bitcoin Script kompozycja sekwencyjna jest realizowana (w przybliżeniu) przez konkatenację dwóch rutyn (dlatego Bitcoin Script nazywa się konkatenacyjnym językiem programowania), ponieważ wyjście jednej rutyny pozostaje na stosie do zużycia przez kolejną rutynę. Kompozycję równoległą osiąga się przez użycie operacji duplikowania i zamiany w celu manipulowania stosem tak, aby dwie rutyny mogły zostać uruchomione na tym samym wejściu. Sprawy nie są całkiem proste, ponieważ to, co nazywamy "iloczynem" typów, zwykle realizuje się z użyciem wielu elementów stosu. Mam nadzieję, że widać ogólną ideę.

Kompozycja warunkowa jest oczywiście realizowana przez `OP_IF`, który rozgałęzia się na podstawie wartości na stosie. W tym przypadku najwyższy element stosu pełni rolę tagu, a zwykle następny element lub elementy na stosie mają różne "typy" zależne od wartości tagu. W każdym przypadku typy elementów stosu mogą nadawać się do przetwarzania tylko przez jedną z gałęzi w `OP_IF`. Jednak po dojściu do `OP_ENDIF` elementy stosu muszą mieć spójny "typ", tak aby pozostały skrypt mógł kontynuować niezależnie od tego, która gałąź została wcześniej wybrana.

### Kompozycja w Simplicity

Zaprojektowaliśmy Simplicity z kombinatorami, które bezpośrednio implementują te trzy formy kompozycji. Wraz z kilkoma dodatkowymi kombinatorami wspierającymi inne podstawowe operacje związane z typami iloczynu i sumy, rdzeń języka Simplicity składa się ostatecznie z dziewięciu kombinatorów wystarczających do wyrażenia dowolnego skończonego obliczenia. Omówimy to bardziej szczegółowo w następnym rozdziale.

### Czwarty rodzaj kompozycji

Zanim skończymy, warto wspomnieć, że w informatyce istnieje co najmniej jeden dodatkowy rodzaj kompozycji, czyli "kompozycja rekurencyjna". W kompozycji rekurencyjnej jedna operacja jest iterowana wielokrotnie.

Zauważ, że Bitcoin Script nie obsługuje kompozycji rekurencyjnej i podobnie jawnie wykluczyliśmy nieograniczoną rekurencję z projektu Simplicity. Nasza teza jest taka, że nieograniczone obliczenia iteracyjne lepiej implementować przy użyciu rekurencyjnych covenantów, które obliczają przez wiele transakcji. Pozwala to użytkownikom uniknąć ograniczeń przestrzeni blokowej i standardowości oraz lepiej przewidywać koszty transakcji.

Mimo to istnieją sposoby nadużycia funkcji delegacji Simplicity, aby zapewnić coś przypominającego nieograniczoną kompozycję rekurencyjną; być może omówimy to później w tej serii.

### Wniosek

Przejrzeliśmy trzy główne formy kompozycji służące do przekształcania podstawowych operacji w operacje złożone:

- kompozycja sekwencyjna
- kompozycja równoległa
- kompozycja warunkowa

Omówiliśmy, jak te formy kompozycji są realizowane w Bitcoin Script, i zasugerowaliśmy, jak wpłynęły na projekt języka Simplicity. Zauważyliśmy, że czwarty rodzaj kompozycji, kompozycja rekurencyjna, jest wyraźnie wykluczony zarówno z Simplicity, jak i z Bitcoin Script.

W następnym rozdziale opiszemy dziewięć kombinatorów tworzących rdzeń języka Simplicity, jak służą one do bezpośredniej realizacji tych trzech form kompozycji oraz jak tworzy to kompletny język do opisywania dowolnego skończonego obliczenia.

## Kompletność kombinatorowa Simplicity

<chapterId>2a10a6ba-fada-4556-a673-3ae8c0794bf0</chapterId>

W tym rozdziale wprowadzamy rdzeń języka Simplicity i pokazujemy, że język jest kompletny, co oznacza, że można w nim wyrazić dowolne skończone obliczenie.

### Typy Simplicity

Simplicity obsługuje trzy fundamentalne konstruktory typów. Typ iloczynu `A × B` reprezentuje wyjścia kompozycji równoległej, natomiast typ sumy `A + B` (unia tagowana) obsługuje wejścia kompozycji warunkowej. Trzecim typem jest typ jednostkowy.

### Typ jednostkowy

Typ jednostkowy, oznaczany `𝟙` albo `ONE`, zawiera dokładnie jedną wartość: pustą krotkę `⟨⟩` albo `()`. Ten zerobitowy typ danych nie niesie żadnej informacji.

### Typ sumy

Typ sumy `A + B` łączy dwa typy z tagami wskazującymi "lewo" albo "prawo". Wartości zapisuje się jako `σᴸ(a)` albo `inl(a)` dla wartości z lewym tagiem oraz `σᴿ(b)` albo `inr(b)` dla wartości z prawym tagiem. Tagi pozostają odrębne nawet przy łączeniu identycznych typów.

#### Typ boolowski

Typ `𝟙 + 𝟙`, oznaczany `𝟚` albo `TWO`, reprezentuje jednobitowy typ z dwiema wartościami. Zgodnie z konwencją `σᴸ⟨⟩` reprezentuje fałsz/zero, natomiast `σᴿ⟨⟩` reprezentuje prawdę/jeden.

### Typ iloczynu

Typy iloczynu `A × B` zawierają pary wartości zapisywane jako `⟨a, b⟩` albo `(a, b)`. Typ `𝟚 × 𝟚` ma cztery wartości, odrębne od czterech wartości w `𝟚 + 𝟚`.

### Rdzeniowe wyrażenia Simplicity

Operacje oznacza się jako `f : A ⊢ B`, co znaczy: typ wejścia `A` i typ wyjścia `B`. Simplicity jest "pierwszego rzędu" — nie ma typów funkcji.

### Dwie podstawowe operacje

Rdzeń języka zapewnia dwie podstawowe operacje:

**Tożsamość (`iden`).** Operacja tożsamości przekazuje swoje wejście bez zmian:

```
iden : A ⊢ A
⟦iden⟧(a) = a
```

**Jednostka (`unit`).** Operacja jednostkowa odrzuca swoje wejście i zwraca pustą krotkę:

```
unit : A ⊢ 𝟙
⟦unit⟧(a) = ⟨⟩
```

Tworzą one rodziny z jedną operacją na typ.

### Trzy kombinatory kompozycji

Kompozycja sekwencyjna używa `comp f g` (zapisywanego `f ⨾ g` albo `f >>> g`):

```
If f : A ⊢ B and g : B ⊢ C, then
comp f g : A ⊢ C
⟦f ⨾ g⟧(a) = ⟦g⟧(⟦f⟧(a))
```

Kompozycja równoległa używa `pair f g` (zapisywanego `f ▵ g` albo `f &&& g`):

```
If f : A ⊢ B and g : A ⊢ C, then
pair f g : A ⊢ B × C
⟦f ▵ g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩
```

Kompozycja warunkowa używa `case f g : (A + B) × C ⊢ D`, dając gałęziom dostęp do wspólnego środowiska `C`:

```
If f : A × C ⊢ D and g : B × C ⊢ D, then
case f g : (A + B) × C ⊢ D
⟦case f g⟧⟨σᴸ(a), c⟩ = ⟦f⟧⟨a, c⟩
⟦case f g⟧⟨σᴿ(b), c⟩ = ⟦g⟧⟨b, c⟩
```

Dlaczego kompozycja warunkowa ma taki kształt — suma sparowana ze wspólnym środowiskiem `C` — zamiast prostszego `copair f g : A + B ⊢ C`, który tylko wybiera gałąź? Ponieważ goły `copair` nie potrafi wyrazić **dystrybucji**: funkcji `dist : (A + B) × C ⊢ A × C + B × C`, która wpycha wspólne wejście do tej gałęzi, która została wybrana. Wbudowując środowisko `C` bezpośrednio w `case`, Simplicity uzyskuje kompozycję warunkową *i* dystrybucję z pojedynczego kombinatora — jedną z kluczowych decyzji projektowych, które utrzymują rdzeń języka na poziomie dziewięciu kombinatorów.

### Cztery kolejne kombinatory

Zużywanie iloczynu używa `take` i `drop`:

**take** wyodrębnia lewy element:

```
If f : A ⊢ C, then
take f : A × B ⊢ C
⟦take f⟧⟨a, b⟩ = ⟦f⟧(a)
```

**drop** wyodrębnia prawy element:

```
If f : B ⊢ C, then
drop f : A × B ⊢ C
⟦drop f⟧⟨a, b⟩ = ⟦f⟧(b)
```

Wytwarzanie sumy używa `injl` i `injr`:

**injl** opakowuje lewym tagiem:

```
If f : A ⊢ B, then
injl f : A ⊢ B + C
⟦injl f⟧(a) = σᴸ(⟦f⟧(a))
```

**injr** opakowuje prawym tagiem:

```
If f : A ⊢ C, then
injr f : A ⊢ B + C
⟦injr f⟧(a) = σᴿ(⟦f⟧(a))
```

### Dziewięć rdzeniowych kombinatorów

Łącznie Simplicity ma dokładnie dziewięć rdzeniowych kombinatorów:

| Kombinator | Cel |
|---|---|
| `iden` | Przekazuje wejście dalej |
| `unit` | Odrzuca wejście |
| `comp` | Kompozycja sekwencyjna |
| `pair` | Kompozycja równoległa |
| `case` | Kompozycja warunkowa |
| `take` | Wyodrębnia lewą stronę z iloczynu |
| `drop` | Wyodrębnia prawą stronę z iloczynu |
| `injl` | Wstrzykuje do lewej strony sumy |
| `injr` | Wstrzykuje do prawej strony sumy |

### Simplicity i rachunek sekwentów

Projekt Simplicity wywodzi się z koniunkcyjno-dysjunkcyjnego fragmentu rachunku sekwentów Gentzena. Ściślej rzecz biorąc, jest wariantem *interpretacji funkcyjnej* rachunku sekwentów, który sam jest analogiczny do odpowiedniości Curry'ego-Howarda między dedukcją naturalną a rachunkiem lambda. Reguły kombinatorów wykazują "mniejsze typy w przesłankach niż we wnioskach", umożliwiając Bit Machine — abstrakcyjnemu interpreterowi maszyny stosowej Simplicity — minimalizowanie kopiowania danych podczas wykonania.

### Wartości nie są wyrażeniami

Wyrażenia Simplicity oznaczają operacje, a nie wartości. Notacja `scribe b : A ⊢ B` reprezentuje unikalne wyrażenie zawsze zwracające wartość `b`, służące jako wygoda notacyjna, a nie jako kombinator. Odzwierciedla to Bitcoin Script, gdzie operacje takie jak `OP_1` wypychają wartości, zamiast wyrażać je bezpośrednio.

### Twierdzenie o kompletności Simplicity

Mając wszystkie dziewięć kombinatorów, skąd wiemy, że niczego nam nie brakuje — że tych dziewięć naprawdę wystarczy? Odpowiada na to twierdzenie o kompletności Simplicity: dla dowolnej funkcji między (skończonymi) typami Simplicity istnieje pewne wyrażenie Simplicity, które ją oznacza. Dowód jest konstruktywny — pokazuje, jak zbudować wyrażenie:

1. **Rozłożyć wejście**: używając zagnieżdżonych wyrażeń `case`, w pełni rozłożyć dowolne wejście dowolnego typu na jego składowe bity
2. **Zbudować tabelę wyszukiwania**: dla każdego możliwego wejścia użyć `scribe`, aby wyprodukować odpowiadające wyjście
3. **Złożyć całość**: zagnieżdżone przypadki i skryby razem tworzą ogromną tabelę wyszukiwania implementującą funkcję

To twierdzenie zostało formalnie zweryfikowane w asystencie dowodzenia Rocq (dawniej Coq). Dowód jest częścią oficjalnego repozytorium Simplicity i został maszynowo sprawdzony pod kątem poprawności.

Choć twierdzenie o kompletności gwarantuje, że dziewięć kombinatorów Simplicity może wyrazić dowolną funkcję między (skończonymi) typami Simplicity, wynikowe wyrażenia z konstrukcji tabeli wyszukiwania są niepraktycznie duże. Funkcja na 256-bitowych wejściach wymagałaby tabeli wyszukiwania z 2²⁵⁶ wpisami. Dlatego następne rozdziały koncentrują się na budowaniu efektywnych wyrażeń, które wykorzystują strukturę obliczeń, zamiast brutalnie realizować wszystko przez tabele wyszukiwania.

### Wniosek

Rdzeń języka Simplicity obejmuje system typów i kombinatory umożliwiające dowolne skończone obliczenie. Choć twierdzenie o kompletności gwarantuje ekspresywność, wynikowe wyrażenia z ogólnej konstrukcji są niepraktycznie duże. Praktyczny rozwój w Simplicity polega na wykorzystywaniu struktury obliczeniowej dla zwięzłych wyrażeń. Następne rozdziały omawiają struktury danych, interakcje z transakcjami i dodatkowe kombinatory.

# Od typów danych do programów

<partId>08528a6f-d310-4675-b8cd-4e9b93b3c009</partId>

## Budowanie typów danych

<chapterId>9981ae62-ae50-4770-adf2-b253d1e08de3</chapterId>

W poprzednich rozdziałach pokazaliśmy, że rdzeniowy zestaw kombinatorów Simplicity wystarcza do implementacji dowolnego skończonego czystego obliczenia. Ten rozdział pokazuje, jak budować praktyczne struktury danych i obliczenia z tych prymitywów — tak samo, jak komputery buduje się z bramek logicznych.

### Logika boolowska

Typ boolowski, oznaczany `𝟚`, jest równy `𝟙 + 𝟙` i ma dwie wartości: `σᴸ⟨⟩` (fałsz) oraz `σᴿ⟨⟩` (prawda). Korzystając z rdzeniowych kombinatorów, można konstruować operatory logiki boolowskiej.

#### Operacja And

Operacja logiczna `and : 𝟚 × 𝟚 ⊢ 𝟚` przyjmuje dwa bity i zwraca jeden bit. Implementacja rozgałęzia się na pierwszym bicie: jeśli jest fałszem, zwraca fałsz; w przeciwnym razie zwraca drugi bit.

```
and ≔ case (injl unit) (drop iden) : 𝟚 × 𝟚 ⊢ 𝟚
```

Testowanie z `⟨false, false⟩`:

```
⟦and⟧⟨false, false⟩
 = {expand the notation for false}
⟦and⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {expand the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {evaluate case for σᴸ}
⟦injl unit⟧⟨⟨⟩, σᴸ⟨⟩⟩
 = {evaluate injl}
σᴸ(⟦unit⟧⟨⟨⟩, σᴸ⟨⟩⟩)
 = {evaluate unit}
σᴸ⟨⟩
 = {by the notation for false}
false
```

Testowanie z `⟨true, true⟩`:

```
⟦and⟧⟨true, true⟩
 = {expand the notation for true and the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴿ⟨⟩, σᴿ⟨⟩⟩
 = {evaluate case for σᴿ}
⟦drop iden⟧⟨⟨⟩, σᴿ⟨⟩⟩
 = {evaluate drop}
⟦iden⟧(σᴿ⟨⟩)
 = {evaluate iden}
σᴿ⟨⟩
 = {by the notation for true}
true
```

#### Inne operacje logiczne

Operacja `not` wymaga kombinatora pomocniczego:

```
                   f : A ⊢ C    g : B ⊢ C
--------------------------------------------------------------
copair f g ≔ iden ▵ unit ⨾ case (take f) (take g) : A + B ⊢ C
```

Początkowe `iden ▵ unit : A ⊢ A × 𝟙` dodaje do wejścia puste „środowisko”, umożliwiając zastosowanie kombinatora `case`. Użycie `take` w dwóch gałęziach odrzuca to puste środowisko, aby wykonać `f` albo `g`.

Inne boolowskie operacje logiczne:

- `or ≔ case (drop iden) (injr unit) : 𝟚 × 𝟚 ⊢ 𝟚`
- `not ≔ copair (injr unit) (injl unit) : 𝟚 ⊢ 𝟚`
- `xor ≔ case (drop iden) (drop not) : 𝟚 × 𝟚 ⊢ 𝟚`

### Sumatory bitowe

„Półsumator” przyjmuje dwa bity i dodaje je, produkując dwubitowe wyjście: bit przeniesienia i bit sumy.

```
half-adder ≔ and ▵ xor : 𝟚 × 𝟚 ⊢ 𝟚 × 𝟚
```

„Pełny sumator” dodaje trzy bity, produkując dwubitowe wyjście. Wejście używa zagnieżdżonej krotki `(𝟚 × 𝟚) × 𝟚`.

Dla zagnieżdżonych krotek używa się zwartej notacji:

- `O f` oznacza `take f`
- `I f` oznacza `drop f`
- `H` oznacza `iden`

Na przykład `I O H` oznacza `drop (take iden) : A × (B × C) ⊢ B`, wyodrębniając wartość środkową. Notacja przywołuje cyfry binarne: gdy myślimy o zagnieżdżonych krotkach jak o drzewach binarnych, notacja reprezentuje odwrócone cyfry binarne pozycji w drzewie. Te wyrażenia tworzą indeksy De Bruijna dla Simplicity.

**Uwaga:** Notacja `I`, `O` i `H` dotyczy tylko podwyrażeń składających się wyłącznie z `take`, `drop` i `iden`.

Pełny sumator składa dwa półsumatory, biorąc logiczne `or` bitów przeniesienia:

```
full-adder ≔ take half-adder ▵ I H
           ⨾ O O H ▵ (O I H ▵ I H ⨾ half-adder)
           ⨾ (O H ▵ I O H ⨾ or) ▵ I I H
           : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × 𝟚
```

W pierwszej linii `take half-adder ▵ I H : (𝟚 × 𝟚) × 𝟚 ⊢ (𝟚 × 𝟚) × 𝟚` uruchamia półsumator na pierwszych dwóch bitach, zachowując ostatni bit.

W drugiej linii `O O H ▵ (O I H ▵ I H ⨾ half-adder) : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × (𝟚 × 𝟚)` zachowuje pierwszy bit (przeniesienie wyjściowe pierwszego półsumatora) i uruchamia półsumator na ostatnich dwóch bitach.

W ostatniej linii `(O H ▵ I O H ⨾ or) ▵ I I H: 𝟚 × (𝟚 × 𝟚) ⊢ 𝟚 × 𝟚` bierze logiczne OR z pierwszych dwóch bitów (przeniesień wyjściowych obu półsumatorów) i zwraca bit sumy wyjściowej drugiego półsumatora.

To demonstruje programowanie w Simplicity: używanie notacji `I`, `O` i `H` do odwoływania się do bitów danych, tworzenie odpowiednich „środowisk” do wywoływania innych funkcji za pośrednictwem kompozycji sekwencyjnej.

Użytkownicy nie definiują bezpośrednio niskopoziomowych operacji. Dalej w tej serii omówimy jety biblioteki standardowej implementujące typowe funkcje. Od użytkowników końcowych nie oczekuje się programowania bezpośrednio w Simplicity, podobnie jak w Bitcoin Script. Zamiast tego języki wyższego poziomu, takie jak SimplicityHL, generują kod Simplicity, zarządzając „środowiskami” podwyrażeń i tłumacząc nazwane zmienne na odpowiednie sekwencje `take` i `drop`.

### Wektory

Wektory o stałej długości definiuje się przez tworzenie iterowanych iloczynów typu `A`:

- `A² ≔ A × A`
- `A⁴ ≔ A² × A²`
- `A⁸ ≔ A⁴ × A⁴`
- `…`

Można je zapisywać jako `A^2`, `A^4`, `A^8` itd.

Wektory definiuje się tylko dla długości będących potęgami dwóch. Inne potęgi wymagają wyboru konwencji nawiasowania.

Dla danego wyrażenia `f : A ⊢ B` powtarzane parowanie „mapuje” je po wektorach o stałej długości:

- `f² ≔ f ▵ f : A² ⊢ B²`
- `f⁴ ≔ f² ▵ f² : A⁴ ⊢ B⁴`
- `f⁸ ≔ f⁴ ▵ f⁴ : A⁸ ⊢ B⁸`

Dla danej funkcji `f : A × B ⊢ B`, iteracja albo „folding” po wektorach o stałej długości:

- `fold-right-2 f ≔ O O H ▵ (O I H ▵ I H ⨾ f) ⨾ f : A² × B ⊢ B`
- `fold-right-4 f ≔ fold-right-2 (fold-right-2 f) : A⁴ × B ⊢ B`
- `fold-right-8 f ≔ fold-right-2 (fold-right-4 f) : A⁸ × B ⊢ B`

Istnieje wiele wariantów. Dla danego `f : A × B ⊢ C`, „zip” po sparowanych wektorach z `zip-n f : (Aⁿ × Bⁿ) ⊢ Cⁿ`. Dla danego `f : (A × B) × C ⊢ C`, fold po sparowanych wektorach z `bifold-right-n f : (Aⁿ × Bⁿ) ⊢ C`. Łączenie `map` i `fold-right` tworzy kombinatory akumulujące: `f : A × C ⊢ C × B` daje `map-accum-right-n f : Aⁿ × C ⊢ C × Bⁿ`. Możliwych jest wiele kolejnych wariantów.

#### Słowa wielobitowe

Wektor bitów daje liczby całkowite wielobitowe. Na przykład `𝟚³²` jest 32-bitowym typem słowa. `𝟚²⁵⁶` jest 256-bitowym typem słowa, odpowiednim dla hashy i operacji kryptograficznych.

Używając pełnego sumatora, wariant operacji wektorowych definiuje „sumator z propagacją przeniesienia” po słowach wielobitowych:

```
full-adder-n ≔ zip-accum-right-n full-adder : (𝟚ⁿ × 𝟚ⁿ) × 𝟚 ⊢ 𝟚 × 𝟚ⁿ
```

`full-adder-n` przyjmuje dwie n-bitowe liczby binarne i jednobitowe przeniesienie wejściowe, zwracając jednobitową flagę przeniesienia wyjściowego oraz n-bitową sumę.

#### SHA-256

Przez rekurencyjne definiowanie operacji arytmetycznych na słowach wielobitowych — odejmowania, mnożenia, dzielenia — oraz bitowych operacji logicznych, takich jak logiczne AND, OR, XOR, i wielokrotne ich łączenie, można zbudować nawet funkcję kompresji bloku SHA-256:

```
sha256-hash-block ≔ … : 𝟚²⁵⁶ × 𝟚⁵¹² ⊢ 𝟚²⁵⁶
```

Kompresja SHA-256 jest formalnie zdefiniowana przy użyciu Simplicity w asystencie dowodzenia Rocq (dawniej Coq), wraz z formalnym dowodem poprawności implementacji `sha256-hash-block`.

Kompresja działa zbyt wolno jako surowe Simplicity. Jety wykonują typowe funkcje, takie jak kompresja SHA-256, natywnie. Czyste implementacje w Simplicity służą jako formalne specyfikacje dla jetów.

### Typy opcji

Typy opcji wynikają z wzięcia sumy z typem jednostkowym:

```
Option A ≔ 𝟙 + A
```

Typ `Option A` można zapisywać jako `A?` albo `𝕊 A` (gdzie `𝕊` oznacza „następnik”). Funkcje mapują po typach opcji:

```
                 f : A ⊢ B
------------------------------------------
f? ≔ copair (injl unit) (injr f) : A? ⊢ B?
```

Można zdefiniować kombinatory monadyczne, takie jak bind:

```
              f : A ⊢ B?
---------------------------------------
bind f ≔ copair (injl unit) f : A? ⊢ B?
```

### Bufory o zmiennej długości

„Bufory” są typami dla częściowo wypełnionych wektorów:

- `Aᑉ² ≔ A?`
- `Aᑉ⁴ ≔ A²? × Aᑉ²`
- `Aᑉ⁸ ≔ A⁴? × Aᑉ⁴`
- `…`

Typ `Xᑉ⁸` rozwija się do `(1 + X⁴) × ((1 + X²) × (1 + X))`. Traktowanie tego jako wielomianu i rozwinięcie daje `1 + X + X² + X³ + X⁴ + X⁵ + X⁶ + X⁷`. Interpretowane jako typ, reprezentuje sumę wszystkich możliwych krotek X do długości 7 włącznie, w tym pustej krotki. To dokładnie typ list o długości ściśle mniejszej niż 8.

Podobnie jak dla wektorów, operacje mapowania i foldingu można definiować na buforach. Operacje stosu obejmują `push-<n : Aᑉⁿ × A ⊢ Aⁿ + Aᑉⁿ` i `pop-<n : Aᑉⁿ ⊢ (Aᑉⁿ × A)?`. `push-<n` dołącza element do bufora, zwracając pełny wektor, jeśli nastąpi przepełnienie. `pop-<n` usuwa element, zwracając mniejszy bufor i usunięty element, opcjonalnie nie zwracając nic, jeśli pierwotny bufor był pusty.

Definicja `push-<n`, rekurencyjnie:

```
push-<2 ≔ case (drop (injr (injr iden))) (injl iden)

push-<4 ≔ ((O I H ▵ IH) ⨾ push-<2) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ injl unit)) (injl iden))
               (injr (I H ▵ O H))

push-<8 ≔ ((O I H ▵ IH) ⨾ push-<4) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ (injl unit ▵ injl unit))) (injl iden))
               (injr (I H ▵ O H))

…
```

Surowe Simplicity staje się trudne do śledzenia powyżej pewnego poziomu złożoności. Użytkownicy końcowi korzystają z języków wyższego poziomu, takich jak SimplicityHL, które generują te idiomatyczne wyrażenia.

### Wniosek

Ten rozdział pokazał, jak budować operacje logiczne z bitów. Z nich wyłoniła się arytmetyka na poziomie bitów, umożliwiająca rozumowanie o wykonaniu. Rozwinięto typy wektorów, demonstrując iterację po słowach wielobitowych w celu definiowania arytmetyki. Idąc dalej, operacje kryptograficzne, takie jak SHA-256 i walidacja podpisów Schnorra, można definiować wyłącznie przy użyciu kombinatorów Simplicity — wszystkie rzeczywiście są zdefiniowane przy użyciu Simplicity.

Ten rozdział nie jest kompleksowym przewodnikiem po wszystkich możliwych typach danych i operacjach, które da się zbudować w Simplicity, ale ilustruje osiąganie praktycznej funkcjonalności w ramach ograniczeń Simplicity. Mimo skończenie ograniczonych typów można definiować użyteczne wektory, typy buforów i operacje iterujące po tych strukturach.

Rzeczywiste specyfikacje operacji biblioteki standardowej nieco różnią się od definicji tutaj. Na przykład pełny sumator używa 3-argumentowego XOR oraz funkcji logicznej „majority”, a nie dwóch półsumatorów.

W praktyce programy Simplicity używają jetów do operacji arytmetycznych i kryptograficznych. Jednak jety zastępują tylko wyrażenia. Kombinatory iterujące po buforach i wektorach nie mogą być zastąpione jetami i pojawiają się w rzeczywistych programach Simplicity. Choć zamiast używać ich bezpośrednio, użytkownicy końcowi korzystają z języków wyższego poziomu, takich jak SimplicityHL, które generują takie wyrażenia.

Rekurencyjnie zdefiniowane kombinatory wydają się rosnąć wykładniczo pod względem rozmiaru wyrażenia. Nie jest to problematyczne. Podczas serializacji wyrażenia koduje się jako DAG-i (skierowane grafy acykliczne), a nie jako drzewa. Rzeczywista reprezentacja rośnie tylko liniowo.

Dotąd rozważaliśmy tylko czyste obliczenia. Interakcja z danymi transakcji w zadaniach takich jak podpisywanie transakcji wymaga pewnego sposobu, aby programy mogły zawieść, jeśli podpisy są nieprawidłowe. Następny rozdział omawia efekty uboczne w Simplicity.

## Dwa efekty uboczne

<chapterId>9eafe498-0765-419a-a69d-a74a9cdf3713</chapterId>

W poprzednich rozdziałach pokazaliśmy, jak budować pewne struktury danych i obliczenia przy użyciu rdzeniowego zestawu kombinatorów Simplicity. Jak zauważyliśmy, rdzeniowe kombinatory wystarczają do implementacji dowolnego skończonego czystego obliczenia. Rodzi to pytanie: co jeszcze można osiągnąć? Możemy dodać do naszych wyrażeń dodatkowe efekty uboczne.

Istnieją różne możliwe rodzaje efektów ubocznych dla wyrażeń: aktualizacja stanu, zapisywanie do logu, rzucanie wyjątku, odczytywanie ze środowiska, wywoływanie kontynuacji itd. Efekty uboczne dostępne w Simplicity będą zależeć od zastosowania.

Dla zastosowań Bitcoin i Liquid mamy obecnie dwa efekty uboczne: efekt Failure, który jest efektem wyjątku, gdzie wyjątek ma typ `𝟙`, oraz efekt Reader, który pozwala uzyskiwać dostęp do danych ze środowiska transakcji. Nasze rdzeniowe kombinatory są „czyste”; nie mają efektów ubocznych. Jednak jety mogą wprowadzać nowe prymitywy, które mają efekty uboczne.

### Jety z efektami

O jetach powiemy więcej później w tym kursie, ale tutaj wprowadzamy kilka przykładowych jetów, aby zilustrować ich efekty uboczne.

#### Bip0340-verify

`bip0340-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚⁵¹² ⊢ 𝟙` jest jetem dla wyrażenia, które przyjmuje klucz publiczny x-only, 256-bitową wiadomość i podpis Schnorra, i niczego nie zwraca! Zgodnie ze swoim typem powinien zachowywać się tak samo jak `unit`. Różnica leży w efekcie ubocznym jeta: jeśli walidacja podpisu się nie powiedzie, całe obliczenie zostaje przerwane przez rzucenie wyjątku (typu jednostkowego). To jest efekt Failure.

#### Verify

`verify : 𝟚 ⊢ 𝟙` jest bardzo prostym jetem do wyrażania efektu Failure. Jeśli wejściem `verify` jest `false`, całe obliczenie zostaje przerwane przez rzucenie wyjątku. Jeśli wejściem jest `true`, nic nie zostaje zwrócone, ale obliczenie może być kontynuowane.

#### Hashe transakcji

`sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` wydaje się funkcją stałą, ponieważ istnieje tylko jedna możliwa wartość wejściowa: pusta krotka. Jednak ten jet odczytuje ze środowiska transakcji i produkuje hash danych transakcji analogiczny do skrótu wiadomości `SIGHASH_ALL` używanego w weryfikacji podpisów Bitcoin Script. To przykład efektu Reader: zwracana wartość zależy od środowiska transakcji, w którym jet jest wykonywany. Istnieje kilka innych jetów haszujących, które haszują różne podzbiory danych środowiska transakcji, aby pomagać budować niestandardowe skróty wiadomości dla podpisów.

#### Jety introspekcji

`input-sequence : 𝟚³² ⊢ 𝟚³²?` jest funkcją, która przyjmuje indeks wejścia i zwraca numer sekwencji transakcji dla tego wejścia, opcjonalnie nie zwracając nic, jeśli indeks jest poza zakresem. Znów wartość wyjściowa nie jest czystą funkcją indeksu wejścia; operacja używa raczej efektu Reader, aby uzyskać dostęp do środowiska transakcji w celu określenia wartości wyjściowej. Istnieje kilka innych jetów introspekcji, które zwracają różne fragmenty danych środowiska transakcji.

### Klasyfikowanie efektów

Nie wszystkie efekty uboczne są sobie równe. Niektóre efekty uboczne zachowują się lepiej niż inne. Możemy klasyfikować efekty według tego, jak podatne są na transformacje programów.

#### Efekty przemienne

Efekt przemienny to taki, w którym, jeśli zamienisz wyjścia dwóch wyrażeń, możesz bezpiecznie zamienić same wyrażenia bez zmiany efektu wyrażenia. Rozważ `swap = I H ▵ O H : A × B ⊢ B × A`. Jeśli `f ▵ g ⨾ swap = g ▵ f` dla każdego wyrażenia `f` i `g` z efektami ubocznymi, to efekty są przemienne.

Odczytywanie danych transakcji ze środowiska jest efektem przemiennym, ponieważ wynik odczytu ze środowiska jest taki sam niezależnie od kolejności, w której wykonujemy odczyt.

Ogólnie rzucanie wyjątku nie jest efektem przemiennym. Jeśli `f` rzuca jakiś wyjątek `e₁`, a `g` rzuca jakiś inny wyjątek `e₂`, to to, który wyjątek zostanie rzucony z pary `f` i `g`, zależy od kolejności ich wykonania.

Jednak w szczególnym przypadku efektu Failure, w którym można rzucić tylko wyjątek typu jednostkowego, efekt jest przemienny. Niezależnie od tego, które z `f` albo `g` rzuci wyjątek, wynikowy wyjątek będzie taki sam, ponieważ istnieje tylko jedna możliwa wartość wyjątku.

#### Efekty idempotentne

Efekt idempotentny to taki, w którym, jeśli zduplikujesz wyjście wyrażenia, możesz bezpiecznie zduplikować samo wyrażenie bez zmiany efektu wyrażenia. Rozważ `dup = iden ▵ iden : A ⊢ A × A`. Jeśli `f ⨾ dup = dup ⨾ f ▵ f` dla każdego `f` z efektami ubocznymi, to efekty są idempotentne.

Odczytywanie danych transakcji ze środowiska jest efektem idempotentnym. Rzucanie wyjątku również jest efektem idempotentnym. Choć wykonane zostanie tylko jedno z dwóch zduplikowanych wyrażeń, każdy wyjątek rzucony przez `dup ⨾ f ▵ f` będzie taki sam jak wyjątek rzucony przez `f ⨾ dup`.

Zapisywanie do logu może jednak nie być idempotentne, ponieważ zduplikowanie efektu spowodowałoby pojawienie się komunikatu logu dwukrotnie. Jeśli jednak log składa się ze _zbioru_ komunikatów zamiast _listy_ komunikatów, efekt byłby idempotentny (i przemienny), ponieważ wstawienie do zbioru samo jest operacją idempotentną.

#### Efekty unitarne

Efekt unitarny to taki, w którym, jeśli odrzucisz wyjście wyrażenia, możesz bezpiecznie odrzucić samo wyrażenie bez zmiany efektów wyrażenia. Jeśli zawsze zachodzi `f ⨾ unit = unit` dla każdego `f` z efektami ubocznymi, to twoje efekty są unitarne.

Odczytywanie danych ze środowiska jest jednym z nielicznych typów efektów unitarnych. Jeśli wynik odczytu danych transakcji ze środowiska zostanie odrzucony, można odrzucić całe wyrażenie wykonujące odczyt.

Efekt failure nie jest unitarny. Jeśli `f` rzuca wyjątek, to `f ⨾ unit` również go rzuci; wykonanie nie dojdzie nawet do kombinatora `unit`, zanim obliczenie zostanie przerwane. Z drugiej strony `unit` oczywiście nie rzuciłby żadnego wyjątku, więc efekty `f ⨾ unit` i `unit` byłyby różne.

Podsumowując, oto jak omówione wyżej efekty wypadają względem tych trzech własności:

| Efekt | Przemienny | Idempotentny | Unitarny |
| --- | :---: | :---: | :---: |
| Reader (środowisko transakcji) | ✓ | ✓ | ✓ |
| Failure (wyjątek typu jednostkowego) | ✓ | ✓ | ✗ |
| Writer (log jako zbiór) | ✓ | ✓ | ✗ |
| Ogólne wyjątki (dowolny typ) | ✗ | ✓ | ✗ |

### Efekty dozwolone w Simplicity

Im lepiej zachowujące się własności ma dany typ efektu, tym więcej miejsca ma optymalizator Simplicity na transformowanie programów używających tych efektów. Idealnie dopuszczalibyśmy tylko efekty mające wszystkie trzy własności: przemienność, idempotentność i unitarność. Pozwoliłoby to optymalizatorowi wykonywać dowolne transformacje programu, jakie chciałby wykonać. Jednak odczyt ze środowiska jest jedynym efektem spełniającym wszystkie trzy własności.

Zamiast tego wymagamy, aby efekty Simplicity były przemienne i idempotentne. Oba efekty używane w Simplicity, efekt Failure i efekt Reader, są przemienne i idempotentne. Pozwala to wykonywać dużą klasę optymalizacji na kodzie Simplicity.

Jednak opisana wyżej transformacja „odrzucenia”, próbująca zastąpić `f ⨾ unit` przez `unit`, albo jakakolwiek podobna transformacja, nie jest dozwolona, jeśli `f` może wytworzyć efekt Failure. Rzeczywiście, wyobraź sobie, że `f` zawiera asercję `bip0340-verify`. Próba zoptymalizowania tego sprawdzenia byłaby katastrofalna.

### Po co w ogóle dopuszczać efekty uboczne?

Dlaczego Simplicity w ogóle dopuszcza efekty uboczne? Czy nie byłoby lepiej, gdyby każdy program przyjmował całą transakcję jako wejście i zwracał wyjście boolowskie decydujące, czy transakcja jest ważna, czy nie?

#### Weryfikacja wsadowa

Jednym z powodów, dla których mamy efekt Failure, jest obsługa [weryfikacji wsadowej](https://github.com/bitcoin/bips/blob/c9a6ca6297eb8de850f6b64dafb8e60ee9b64d66/bip-0340.mediawiki#batch-verification) podpisów Schnorra. W weryfikacji wsadowej wiele indywidualnych sprawdzeń podpisów Schnorra jest łączonych w taki sposób, że jeśli jakiekolwiek pojedyncze sprawdzenie podpisu zawiedzie, zawiedzie cała partia.

Ta procedura łączenia w partie poprawia efektywność względem indywidualnego weryfikowania każdego podpisu. Wadą jest to, że jeśli weryfikacja wsadowa zawiedzie, nie dowiadujemy się, które konkretne sprawdzenie lub sprawdzenia podpisów zawiodły.

Używając efektu ubocznego failure, `bip0340-verify` zapewnia, że jeśli sprawdzenie podpisu zawiedzie, zawiedzie cała transakcja. Gdyby `bip0340-verify` zamiast tego zwracał `𝟚`, typ boolowski, dla sukcesu albo porażki, nieudane sprawdzenie podpisu nadal mogłoby doprowadzić do gałęzi, w której skrypt się powiedzie. W takim przypadku musielibyśmy wiedzieć, czy dany podpis jest ważny, czy nie, a tym samym nie moglibyśmy skorzystać z weryfikacji wsadowej.

#### Wstępnie obliczone dane transakcji

Problemem we wczesnym Bitcoin Script było to, że funkcja haszująca używana do tworzenia skrótów wiadomości dla podpisów była liniowa względem rozmiaru transakcji. Zazwyczaj każde wejście tworzy co najmniej jeden skrót wiadomości do weryfikacji podpisu, więc ogólna ilość haszowania była kwadratowa względem rozmiaru transakcji.

Ten problem naprawiono w Segwit i późniejszych iteracjach Bitcoin Script przez przedefiniowanie skrótów wiadomości tak, aby można je było obliczać w czasie stałym na sprawdzenie podpisu. Opiera się to na posiadaniu `PrecomputedTransactionData`, które wstępnie oblicza hashe danych transakcji raz, a następnie jest współdzielone przez obliczenia sighash każdego wejścia. Jety haszowania transakcji w Simplicity opierają się na tym samym rodzaju wstępnie obliczonych danych transakcji, aby zapewnić, że jety działają w czasie stałym.

Załóżmy, że `sig-all-hash` nie używa efektu Reader. Załóżmy, że jakimś sposobem udało nam się zbudować typ Simplicity dla środowiska transakcji. Nazwijmy go `TxEnv`, tak aby typem jeta było `sig-all-hash : TxEnv ⊢ 𝟚²⁵⁶`. Taka definicja wymagałaby od jeta `sig-all-hash`, aby potrafił obliczyć hash dowolnej transakcji, nie tylko transakcji, której dotyczy. Programy Simplicity mogłyby kopiować podany `TxEnv` i przekazywać zmodyfikowaną jego kopię do `sig-all-hash`. W takim przypadku `sig-all-hash` nie mógłby polegać na `PrecomputedTransactionData` i wrócilibyśmy do wymogu czasu liniowego względem dowolnych danych transakcji przekazanych do tej wersji `sig-all-hash`.

Ponieważ `sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` używa efektu Reader, aby uzyskać dostęp do danych transakcji, otrzymuje dostęp _wyłącznie_ do stałego środowiska transakcji. Z tego powodu implementacja jeta może bezpiecznie używać `PrecomputedTransactionData` i działać w czasie stałym.

### Agregacja podpisów między wejściami

Choć ani Liquid, ani Bitcoin nie obsługują obecnie [agregacji podpisów między wejściami](https://hrf.org/latest/cisa-research-paper/), chcielibyśmy sprawdzić, czy Simplicity może być z nią kompatybilny, kiedy nadejdzie właściwy czas.

Choć szczegóły nie zostały dopracowane, wyobrażamy sobie implementację półagregacji przy użyciu efektu Writer. To znaczy, nowy jet o typie takim jak `half-agg-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚²⁵⁶ ⊢ 𝟙` przyjmowałby klucz publiczny, skrót wiadomości oraz komponent `r` podpisu Schnorra (podpis Schnorra składa się z komponentu `r` i komponentu `s`) i zapisywałby go do logu transakcji przed kontynuowaniem wykonania. Następnie, gdzie indziej w transakcji albo wraz z transakcją, dostarczany byłby zagregowany komponent `s` dla wszystkich półzagregowanych podpisów Schnorra. Transakcja byłaby ważna tylko wtedy, gdy taki zagregowany komponent `s` zostałby dostarczony dla wszystkich zalogowanych kluczy, wiadomości i komponentów `r`.

Aby spełnić wymagania Simplicity, ten efekt Writer musi być idempotentny i przemienny. Można to zapewnić, traktując log writer jako zbiór krotek klucza, wiadomości i komponentu `r`. Działa to, ponieważ operacje na zbiorach są idempotentne i przemienne. Traktowanie logu jako zbioru wartości byłoby kompatybilne z algorytmem weryfikacji półagregacji.

### Wniosek

W tym rozdziale przyjrzeliśmy się dodawaniu efektów ubocznych do obliczeń, które może wykonywać Simplicity. Sklasyfikowaliśmy różne rodzaje efektów według tego, jak dobrze zachowują się względem różnych rodzajów transformacji programów. Zdecydowaliśmy ograniczyć efekty Simplicity do tych, które są przemienne i idempotentne.

Dwa efekty używane w zastosowaniach Bitcoin i Liquid to efekt Reader, służący do dostępu do środowiska transakcji, oraz efekt Failure, służący do przerywania i niepowodzenia programu. Niektóre jety korzystają z operacji prymitywnych, w których mogą wystąpić tego rodzaju efekty uboczne.

Efekt Failure określa wyjście programu Simplicity: program albo zawodzi, czyniąc transakcję nieważną, albo program się udaje. Efekt Reader zapewnia jeden rodzaj wejścia do programu Simplicity: środowisko zawierające dane transakcji. Musimy jednak dostarczać programom Simplicity także inne wejścia, takie jak podpisy cyfrowe.

W następnym rozdziale przyjrzymy się temu, czym są programy Simplicity, jak zamienia się je w adresy i jak dodajemy do programów Simplicity inne wejścia, takie jak podpisy.

## Programy i adresy

<chapterId>961652e3-8f7d-4c2a-8b55-9a990b91a0dd</chapterId>

W poprzednim rozdziale opisaliśmy dwa efekty uboczne używane w Simplicity: efekt Failure, który określa sukces albo porażkę programu, oraz efekt Reader, który zapewnia dostęp do środowiska transakcji. Teraz przechodzimy do praktycznego pytania: czym dokładnie jest program Simplicity i jak staje się adresem na blockchainie?

### Programy Simplicity

Program Simplicity definiuje się jako wyrażenie Simplicity typu `𝟙 ⊢ 𝟙`. Ta sygnatura typu oznacza, że program nie przyjmuje znaczącego wejścia (tylko wartość jednostkową) i nie produkuje znaczącego wyjścia (tylko wartość jednostkową). Efekt Reader przechwytuje wejście środowiska transakcji, natomiast efekt Failure wskazuje sukces albo porażkę. Te efekty obsługują I/O, a nie same typy Simplicity.

### Commitment Merkle Root

Zamiast przechowywać kompletne programy on-chain, Bitcoin używa zobowiązań — praktyki wywodzącej się z Pay-to-Script-Hash (P2SH). Simplicity używa Commitment Merkle Root (CMR).

Każdy kombinator otrzymuje tag SHA-256 wyprowadzony ze wzorca: `Simplicity␟Commitment␟[identifier]`, gdzie `␟` reprezentuje kod ASCII 31 (separator jednostki).

Każdy tag jest hashem SHA-256 odpowiadającego mu łańcucha preimage wymienionego poniżej:

| Kombinator | Preimage tagu (łańcuch ASCII) |
|---|---|
| `iden` | `Simplicity␟Commitment␟iden` |
| `unit` | `Simplicity␟Commitment␟unit` |
| `comp` | `Simplicity␟Commitment␟comp` |
| `pair` | `Simplicity␟Commitment␟pair` |
| `case` | `Simplicity␟Commitment␟case` |
| `take` | `Simplicity␟Commitment␟take` |
| `drop` | `Simplicity␟Commitment␟drop` |
| `injl` | `Simplicity␟Commitment␟injl` |
| `injr` | `Simplicity␟Commitment␟injr` |

Wyrażenie Simplicity jest następnie rekurencyjnie haszowane do 256-bitowego CMR przez obliczenie tagowanego midstanu SHA-256 dla każdego kombinatora wraz z CMR-ami jego argumentów (zapisz `#ᶜ(e)` dla CMR wyrażenia `e` oraz `∥` dla konkatenacji bajtów):

| Kombinator | Reguła CMR |
|---|---|
| `iden` | `#ᶜ(iden) = SHA-256-midstate(tag_iden ∥ tag_iden)` |
| `unit` | `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)` |
| `comp f g` | `#ᶜ(comp f g) = SHA-256-midstate(tag_comp ∥ tag_comp ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `pair f g` | `#ᶜ(pair f g) = SHA-256-midstate(tag_pair ∥ tag_pair ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `case f g` | `#ᶜ(case f g) = SHA-256-midstate(tag_case ∥ tag_case ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `take f` | `#ᶜ(take f) = SHA-256-midstate(tag_take ∥ tag_take ∥ 32·0x00 ∥ #ᶜ(f))` |
| `drop f` | `#ᶜ(drop f) = SHA-256-midstate(tag_drop ∥ tag_drop ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injl f` | `#ᶜ(injl f) = SHA-256-midstate(tag_injl ∥ tag_injl ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injr f` | `#ᶜ(injr f) = SHA-256-midstate(tag_injr ∥ tag_injr ∥ 32·0x00 ∥ #ᶜ(f))` |

Kombinatory binarne (`comp`, `pair`, `case`) konkatenują CMR-y obu dzieci; kombinatory unarne (`take`, `drop`, `injl`, `injr`) konkatenują CMR swojego jedynego dziecka po 32 bajtach dopełnienia `0x00`; a liście zerowej arności (`iden`, `unit`) haszują sam swój tag. Dwie konwencje utrzymują niski koszt obliczania: używane są midstany SHA-256, tak że **każde wyrażenie wymaga co najwyżej jednego wywołania funkcji kompresji SHA-256** (zakładając, że midstate do stałych tagów jest wstępnie obliczony), a konstruktory jednoargumentowe poprzedzają swój argument 32 bajtami dopełnienia `0x00`, co pozwala na trochę dodatkowego wstępnego obliczania w implementacjach, które tego chcą.

Dla kombinatora `unit` — konstruktora zerowej arności bez podwyrażeń argumentów — ta reguła specjalizuje się do `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)`, gdzie `tag_unit = SHA-256(Simplicity␟Commitment␟unit)` (tag jest podawany dwukrotnie). Wynikowy CMR dla trywialnego programu `unit` to:

```
0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

Co krytyczne, CMR nie zobowiązuje się do typów wyrażeń Simplicity, polegając zamiast tego na inferencji typów podczas realizacji.

### Adresy

Adresy używają mechanizmu Taproot z BIP-0341 z CMR-ami zobowiązanymi pod wersją TapLeaf `0xbe`. Proces obejmuje:

1. Obliczenie tagowanego hasha TapLeaf łączącego bajt wersji, długość CMR i sam CMR
2. Dostosowanie wewnętrznego klucza publicznego (z użyciem punktu NUMS, gdy nie jest pożądana ścieżka wydania kluczem)
3. Konwersję do formatu bech32m
4. Dodanie odpowiednich sum kontrolnych

Gdy nie jest pożądana ścieżka wydania kluczem, wewnętrzny klucz publiczny ustawia się na punkt **NUMS** („Nothing-Up-My-Sleeve”): punkt krzywej celowo wybrany tak, aby nikt nie znał jego logarytmu dyskretnego — innymi słowy, punkt bez odpowiadającego mu klucza prywatnego. Ponieważ nikt nigdy nie może wyprodukować dla niego podpisu, ścieżka wydania kluczem jest dowodliwie nieużywalna, a wyjście może zostać wydane *tylko* przez zobowiązaną ścieżkę skryptu Simplicity. W rzeczywistej aplikacji ten punkt NUMS powinien być randomizowany zgodnie z zaleceniem BIP-0341, tak aby wyjścia bez ścieżki wydania kluczem były nieodróżnialne od zwykłych wyjść Taproot (korzyść prywatnościowa).

#### Od Simplicity do adresu

Przejdźmy przez całe wyprowadzenie dla najprostszego możliwego programu: `unit : 𝟙 ⊢ 𝟙`, no-op, który zawsze się udaje.

**1. Tag kombinatora.** Najpierw oblicz tag `unit`:

```
tag_unit = SHA-256(Simplicity␟Commitment␟unit)
         = 0xd723083cff3c75e29f296707ecf2750338f100591c86e0c71717f807ff3cf69d
```

**2. CMR.** Podaj tag dwukrotnie, aby otrzymać CMR programu:

```
CMR = #ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)
    = 0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

**3. Hash TapLeaf.** Poprzedź CMR wersją TapLeaf Simplicity `0xbe` oraz długością CMR `0x20` (32 bajty), a następnie weź tagowany hash Elements TapLeaf (tagowany hash to `hash_str(x) = SHA-256(SHA-256(str) ∥ SHA-256(str) ∥ x)`):

```
hash_TapLeaf/elements(0xbe ∥ 0x20 ∥ CMR)
  = 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c
```

Ponieważ jest tylko ten jeden liść, nie ma TapBranches, więc ten hash jest już korzeniem TapTree.

**4. TapTweak.** Ponieważ nie chcemy ścieżki wydania kluczem, używamy punktu NUMS z BIP-0341 jako klucza wewnętrznego i dostosowujemy go korzeniem TapTree:

```
internal_pk = 0x50929b74c1a04954b78b4b6035e97a5e078a5a0f28ec96d547bfee9ace803ac0
t = hash_TapTweak/elements(internal_pk ∥ 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c)
  = 0xb3bef172389b0937d7e5a8b15cfa41e776777f13f2f659cb06220a6ff0658285
```

**5. Klucz wyjściowy.** Dostosuj wewnętrzny klucz na krzywej, `output_pk = lift_x(internal_pk) ⊕ t·G` (arytmetyka krzywych eliptycznych jest tutaj podsumowana), co daje klucz wyjściowy x-only `0x2cb0c20acd7340b4d4b65f6a60e2888d0d64e3267261f3b3cf7290e5af3f9e09`.

**6. Adres Bech32m.** Zakoduj klucz wyjściowy x-only, poprzedź znakiem `p` (znak wersji świadka SegWit v1), dodaj czytelny dla człowieka prefiks Liquid-testnet `tex1` i dołącz sumę kontrolną Bech32m. Ostateczny adres to:

```
tex1p9jcvyzkdwdqtf49kta4xpc5g35xkfcexwfsl8v70w2gwttelncyshxjk56
```

To było dużo pracy — ale dużą jej część narzuca sam Taproot, a nie Simplicity.

### Wyrażenia świadka

Nowy typ kombinatora odpowiada na brak wejścia do programów Simplicity: wyrażenie świadka. Kombinator `witness` pozwala integrować dane podpisów i inny materiał świadka z programami.

```
      w : B
-----------------
witness w : A ⊢ B
```

Semantyka wyrażenia świadka jest prosta: ignoruje ono swoje wejście i po prostu zwraca wartość `w` (która może mieć dowolny typ Simplicity), tj. `⟦witness w⟧(a) = w`. Nie dodaje to **żadnej nowej ekspresywności** — na mocy twierdzenia o kompletności Simplicity potrafi już zbudować dowolną taką funkcję stałą (przypomnij sobie makro `scribe` z poprzednich rozdziałów). Sens kombinatora `witness` leży całkowicie w jego **CMR**: wartość `w` jest **wykluczona** z CMR wyrażenia, więc adres można obliczyć, zanim `w` będzie znane, a `w` jest dostarczane w czasie realizacji.

Ten wybór projektowy wspiera przycinanie — niewykonane gałęzie warunkowe nie muszą być ujawniane on-chain, w tym powiązane z nimi wyrażenia świadka. Gdy gałąź zostaje przycięta, weryfikator potrzebuje tylko CMR przyciętego poddrzewa, a nie jego rzeczywistej treści.

### Wartości świadka

Może wydawać się ograniczeniem, że wyrażenie świadka może przechowywać tylko *wartość*, a nie bardziej ogólne wyrażenie Simplicity. Ale programy dla blockchainów opartych na UTXO wykonuje się tylko raz. Nie ma potrzeby przekazywania całego podwyrażenia do węzła witness: użytkownik może po prostu uruchomić to podwyrażenie samodzielnie, off-chain, i przepisać jego wyjście do wartości świadka, aby uzyskać dokładnie ten sam wynik.

(Później w tym kursie poznamy kombinator `disconnect`, który zachowuje się podobnie do wyrażenia świadka, które *rzeczywiście* przyjmuje całe wyrażenie Simplicity jako swój argument.)

Alternatywny projekt podawałby wszystkie dane świadka jako argument do najwyższego poziomu programu Simplicity. Wyrażenia świadka są preferowane z dwóch powodów. Po pierwsze, **przycinanie**: niewykonane gałęzie wyrażeń `case` nigdy nie są ujawniane on-chain, a wszystkie wyrażenia świadka wewnątrz tych gałęzi są przycinane wraz z nimi. Po drugie, **lokalność**: wyrażenia świadka pozwalają umieścić każdą wartość świadka dokładnie tam, gdzie jest używana, zamiast przeciągać ją w dół od wejścia najwyższego poziomu programu.

### Inferencja typów

Ponieważ CMR-y nie zobowiązują się do typów, system typów jest rekonstruowany podczas realizacji. Algorytm inferencji typów Simplicity określa minimalne typy dla każdego podwyrażenia na podstawie struktury kombinatorów. Ściślej, inferencja oblicza *główny* (najbardziej ogólny) typ każdego podwyrażenia; wszystkie zmienne typów, które pozostają wolne, są następnie instancjonowane do typu jednostkowego `𝟙`, co daje unikalny, minimalny typ programu.

### Wniosek

W tym rozdziale ustaliliśmy, że programy Simplicity są wyrażeniami typu `𝟙 ⊢ 𝟙`, wyjaśniliśmy, jak Commitment Merkle Roots konstruuje się z tagowanych hashy SHA-256 każdego kombinatora, oraz pokazaliśmy, jak CMR-y są zamieniane w adresy on-chain przez BIP-0341 Taproot. Wprowadziliśmy wyrażenia świadka jako mechanizm dostarczania danych podpisów i innych wejść w czasie wydawania, bez zobowiązywania się do ich wartości w czasie tworzenia adresu.

# Sekcja końcowa

<partId>96952535-4aa6-4e78-91e2-d12e9df895d4</partId>

## Recenzje i oceny

<chapterId>fb0b0133-39ea-497b-bd36-198be42c4fab</chapterId>
<isCourseReview>true</isCourseReview>

## Egzamin końcowy

<chapterId>2cc5e818-abcb-4a0a-9991-7a492c572e2d</chapterId>
<isCourseExam>true</isCourseExam>

## Wniosek

<chapterId>8ade24bd-a84f-4d25-8f64-bdfa8b58926c</chapterId>
<isCourseConclusion>true</isCourseConclusion>
