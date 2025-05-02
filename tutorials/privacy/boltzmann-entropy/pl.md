---
name: Kalkulator Boltzmanna
description: Zrozumienie pojęcia entropii i sposobu korzystania z metody Boltzmanna
---
![cover](assets/cover.webp)


***OSTRZEŻENIE:** Po aresztowaniu założycieli Samourai Wallet i przejęciu ich serwerów 24 kwietnia, strona KYCP.org jest obecnie niedostępna. Gitlab hostujący kod Python Boltzmann Calculator również został przejęty. Obecnie nie jest już możliwe pobranie tego narzędzia. Możliwe jest jednak, że kod zostanie ponownie opublikowany przez inne osoby w nadchodzących tygodniach. W międzyczasie nadal możesz skorzystać z tego samouczka, aby zrozumieć działanie kalkulatora Boltzmanna. Wskaźniki dostarczane przez to narzędzie mają zastosowanie do każdej transakcji Bitcoin i mogą być również obliczane ręcznie. W tym samouczku przedstawię wszystkie niezbędne obliczenia. Jeśli już pobrałeś narzędzie Python na swój komputer lub jeśli używasz RoninDojo, możesz nadal korzystać z narzędzia i postępować zgodnie z tym samouczkiem, nadal działa


uważnie śledzimy rozwój tej sprawy, a także rozwój związany z powiązanymi narzędziami. Zapewniamy, że będziemy aktualizować ten poradnik w miarę pojawiania się nowych informacji


ten samouczek służy wyłącznie celom edukacyjnym i informacyjnym. Nie popieramy ani nie zachęcamy do korzystania z tych narzędzi w celach przestępczych. Każdy użytkownik jest odpowiedzialny za przestrzeganie prawa obowiązującego w jego jurysdykcji


---

Kalkulator Boltzmanna to narzędzie do analizy transakcji Bitcoin poprzez pomiar jej poziomu entropii wraz z innymi zaawansowanymi wskaźnikami. Zapewnia wgląd w powiązania między danymi wejściowymi i wyjściowymi transakcji. Wskaźniki te oferują ilościową ocenę prywatności transakcji i pomagają zidentyfikować potencjalne błędy.


To narzędzie Python zostało opracowane przez zespoły Samourai Wallet i OXT, ale może być używane w każdej transakcji Bitcoin.


## Jak korzystać z kalkulatora Boltzmanna?

Aby skorzystać z kalkulatora Boltzmanna, dostępne są dwie opcje. Pierwszą z nich jest zainstalowanie narzędzia Python bezpośrednio na komputerze. Alternatywnie, można zdecydować się na stronę KYCP.org (_Know Your Coin Privacy_), która oferuje uproszczoną platformę użytkowania. W przypadku użytkowników RoninDojo należy pamiętać, że narzędzie to jest już zintegrowane z węzłem.


Korzystanie z witryny KYCP jest dość proste: wystarczy wpisać identyfikator transakcji (txid), który chcesz przeanalizować, w pasku wyszukiwania i nacisnąć `ENTER`.

![KYCP](assets/1.webp)

Następnie znajdziesz różne informacje o transakcji, w tym powiązania między wejściami i wyjściami. Kliknij na `deterministic links`.

![KYCP](assets/2.webp)

Zostaniesz przeniesiony na stronę poświęconą wskaźnikom kalkulatora Boltzmanna.

![KYCP](assets/3.webp)

Dla tych, którzy wolą korzystać z narzędzia bezpośrednio z węzła RoninDojo, jest ono dostępne poprzez `RoninCLI > Samourai Toolkit > Boltzmann Calculator`.


Podobnie jak w przypadku strony KYCP.org, po zainstalowaniu narzędzia Python wystarczy wkleić txid transakcji, którą chcesz przeanalizować.


![KYCP](assets/7.webp)


Następnie naciśnij przycisk `ENTER`, aby uzyskać wyniki.


![KYCP](assets/8.webp)


## Jakie są wskaźniki kalkulatora Boltzmanna?

### Kombinacje / interpretacje:

Pierwszym wskaźnikiem obliczanym przez oprogramowanie jest całkowita liczba możliwych kombinacji, wskazana w narzędziu jako `nb kombinacje` lub `interpretacje`.


Biorąc pod uwagę wartości UTXO zaangażowanych w transakcję, wskaźnik ten oblicza liczbę sposobów, w jakie dane wejściowe mogą być powiązane z danymi wyjściowymi. Innymi słowy, określa on liczbę wiarygodnych interpretacji, które transakcja może wywołać z perspektywy analizującego ją zewnętrznego obserwatora.

Na przykład, CoinJoin o strukturze zgodnej z modelem Whirlpool 5x5 przedstawia `1,496` możliwych kombinacji: ![KYCP](assets/4.webp)

Z drugiej strony, Whirlpool Surge Cycle 8x8 CoinJoin przedstawia `9,934,563` możliwych interpretacji: ![KYCP](assets/5.webp)

W przeciwieństwie do tego, bardziej tradycyjna transakcja z 1 wejściem i 2 wyjściami przedstawi tylko jedną interpretację: ![KYCP](assets/6.webp)


### Entropia:

Drugim obliczanym wskaźnikiem jest entropia transakcji, oznaczona jako `Entropy`.


W ogólnym kontekście kryptografii i informacji entropia jest ilościową miarą niepewności lub nieprzewidywalności związanej ze źródłem danych lub losowym procesem. Innymi słowy, entropia jest sposobem pomiaru tego, jak trudno jest przewidzieć lub odgadnąć informacje.


W konkretnym kontekście analizy łańcuchowej entropia jest również nazwą wskaźnika, wywodzącego się z entropii Shannona i [wynalezionego przez LaurentMT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf), który jest obliczany za pomocą narzędzia Boltzmanna.


Gdy transakcja przedstawia dużą liczbę możliwych kombinacji, często bardziej odpowiednie jest odniesienie się do jej entropii. Wskaźnik ten pozwala zmierzyć brak wiedzy analityków na temat dokładnej konfiguracji transakcji. Innymi słowy, im wyższa entropia, tym trudniejsze dla analityków staje się zadanie identyfikacji ruchów Bitcoin między wejściami i wyjściami.


W praktyce entropia ujawnia, czy z perspektywy zewnętrznego obserwatora transakcja przedstawia wiele możliwych interpretacji, opartych wyłącznie na ilości danych wejściowych i wyjściowych, bez uwzględnienia innych zewnętrznych lub wewnętrznych wzorców i heurystyk. Wysoka entropia jest wtedy synonimem lepszej poufności transakcji.


Entropia jest definiowana jako logarytm binarny liczby możliwych kombinacji. Oto zastosowany wzór:

```plaintext
E: the entropy of the transaction
C: the number of possible combinations for the transaction

E = log2(C)
```


W matematyce logarytm binarny (logarytm o podstawie 2) odpowiada operacji odwrotnej do potęgowania 2. Innymi słowy, logarytm binarny `x` jest wykładnikiem, do którego należy podnieść `2`, aby otrzymać `x`. Wskaźnik ten jest więc wyrażony w bitach.


Weźmy przykład obliczania entropii dla transakcji CoinJoin skonstruowanej zgodnie z modelem Whirlpool 5x5, który, jak wspomniano wcześniej, oferuje liczbę możliwych kombinacji wynoszącą `1,496`:

```plaintext
C = 1,496
E = log2(1,496)
E = 10.5469 bits
```

Tak więc ta transakcja CoinJoin wykazuje entropię wynoszącą `10,5469 bitów`, co jest uważane za bardzo zadowalające. Im wyższa jest ta wartość, tym więcej różnych interpretacji dopuszcza transakcja, wzmacniając tym samym jej poziom prywatności.

Dla transakcji 8x8 CoinJoin przedstawiającej interpretacje `9,934,563`, entropia wynosiłaby:

```plaintext
C = 9,934,563
E = log2(9,934,563)
E = 23.244 bits
```


Weźmy inny przykład z bardziej konwencjonalną transakcją, zawierającą jedno wejście i dwa wyjścia: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://Mempool.space/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce) W przypadku tej transakcji jedyną możliwą interpretacją jest: `(In.0) > (Out.0 ; Out.1)`. W związku z tym jej entropia jest ustalona na `0`:

```plaintext
C = 1
E = log2(1)
E = 0 bits
```


### Wydajność:

Trzeci wskaźnik dostarczany przez kalkulator Boltzmanna nosi nazwę `Wallet Efficiency`. Wskaźnik ten ocenia efektywność transakcji poprzez porównanie jej z optymalną transakcją możliwą do zrealizowania w identycznej konfiguracji.


Prowadzi nas to do omówienia pojęcia maksymalnej entropii, która odpowiada najwyższej entropii, jaką teoretycznie może osiągnąć określona struktura transakcji. Wydajność transakcji jest następnie obliczana poprzez skonfrontowanie tej maksymalnej entropii z rzeczywistą entropią analizowanej transakcji.


Zastosowany wzór jest następujący:

```plaintext
ER: the actual entropy of the transaction expressed in bits
EM: the maximum possible entropy for a given transaction structure expressed in bits
Ef: the efficiency of the transaction in bits

Ef = ER - EM
```


Na przykład dla struktury Whirlpool 5x5 typu CoinJoin maksymalna entropia wynosi `10,5469`:

```plaintext
ER = 10.5469
EM = 10.5469
Ef = 10.5469 - 10.5469 = 0 bits
```


Wskaźnik ten jest również wyrażony w procentach, a jego formuła jest następująca:

```plaintext
CR: the actual number of possible combinations
CM: the maximum number of possible combinations with the same structure
Ef: the efficiency expressed as a percentage

Ef = CR / CM
Ef = 1,496 / 1,496
Ef = 100%
```


Skuteczność na poziomie `100%` wskazuje zatem, że transakcja maksymalizuje swój potencjał prywatności zgodnie ze swoją strukturą.


### Gęstość entropii:

Czwartym wskaźnikiem jest gęstość entropii, odnotowana w narzędziu `Gęstość entropii`. Zapewnia on perspektywę entropii w stosunku do każdego wejścia lub wyjścia transakcji. Wskaźnik ten jest przydatny do oceny i porównywania wydajności transakcji o różnych rozmiarach. Aby go obliczyć, wystarczy podzielić całkowitą entropię transakcji przez całkowitą liczbę zaangażowanych wejść i wyjść:

```plaintext
ED: the entropy density expressed in bits
E: the entropy of the transaction expressed in bits
T: the total number of inputs and outputs in the transaction

ED = E / T
```


Weźmy przykład Whirlpool 5x5 CoinJoin:

```plaintext
T = 5 + 5 = 10
E = 10.5469
ED = 10.5469 / 10 = 1.054 bits
```


Obliczmy również gęstość entropii dla Whirlpool 8x8 CoinJoin:

```plaintext
T = 8 + 8 = 16
E = 23.244
ED = 23.244 / 16 = 1.453 bits
```


### Wynik Boltzmanna:

Piątą informacją dostarczaną przez kalkulator Boltzmanna jest tabela prawdopodobieństw dopasowania między danymi wejściowymi i wyjściowymi. Tabela ta wskazuje, poprzez wynik Boltzmanna, warunkowe prawdopodobieństwo, że określone wejście jest powiązane z danym wyjściem.


Jest to zatem ilościowa miara warunkowego prawdopodobieństwa wystąpienia związku między wejściem a wyjściem w transakcji, oparta na stosunku liczby korzystnych wystąpień tego zdarzenia do całkowitej liczby możliwych wystąpień w zbiorze interpretacji.


Biorąc ponownie za przykład Whirlpool CoinJoin, tabela prawdopodobieństw warunkowych podkreślałaby szanse na powiązanie między każdym wejściem i wyjściem, zapewniając ilościową miarę niejednoznaczności powiązań w transakcji:


| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
| ------- | -------- | -------- | -------- | -------- | -------- |
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |

Tutaj wyraźnie widać, że każde wejście ma równe szanse na powiązanie z dowolnym wyjściem, co zwiększa poufność transakcji.

Obliczenie wyniku Boltzmanna polega na podzieleniu liczby interpretacji, w których występuje określone zdarzenie, przez całkowitą liczbę dostępnych interpretacji. Tak więc, aby określić wynik kojarzący wejście nr 0 z wyjściem nr 3 (interpretacje `512`), stosuje się następującą procedurę:

```plaintext
Interpretations (IN.0 > OUT.3) = 512
Total Interpretations = 1496
Score = 512 / 1496 = 34%
```


Biorąc za przykład Whirlpool 8x8 CoinJoin (cykl udarowy), tabela Boltzmanna wyglądałaby następująco:


|       | OUT.0 | OUT.1 | OUT.2 | OUT.3 | OUT.4 | OUT.5 | OUT.6 | OUT.7 |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| IN.0  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.1  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.2  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.3  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.4  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.5  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.6  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.7  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |

Jednak w przypadku prostej transakcji z jednym wejściem i dwoma wyjściami sytuacja wygląda inaczej:


| %       | Output 0 | Output 1 |
|---------|----------|----------|
| Input 0 | 100%     | 100%     |

Tutaj zaobserwowano, że prawdopodobieństwo, że każde wyjście pochodzi z wejścia nr 0 wynosi `100%`. Niższe prawdopodobieństwo przekłada się zatem na większą prywatność poprzez rozmycie bezpośrednich powiązań między wejściami i wyjściami.


### Łącza deterministyczne:

Szóstą dostarczaną informacją jest liczba deterministycznych powiązań, uzupełniona o stosunek tych powiązań. Wskaźnik ten ujawnia, ile połączeń między wejściami i wyjściami w analizowanej transakcji jest niepodważalnych, z prawdopodobieństwem `100%`. Z drugiej strony stosunek ten oferuje perspektywę wagi tych deterministycznych powiązań w całym zestawie powiązań transakcyjnych.

Na przykład transakcja Whirlpool typu CoinJoin nie ma deterministycznych powiązań, a zatem wyświetla wskaźnik i współczynnik `0%`. I odwrotnie, w naszej drugiej badanej prostej transakcji (z jednym wejściem i dwoma wyjściami) wskaźnik jest ustawiony na `2`, a współczynnik osiąga `100%`. Tak więc wskaźnik zerowy sygnalizuje doskonałą poufność ze względu na brak bezpośrednich i niepodważalnych powiązań między wejściami i wyjściami.


**Zasoby zewnętrzne:**



- Kod Boltzmanna na Samourai
- [Transakcje Bitcoin i prywatność (część I) Laurent MT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [Bitcoin Transakcje i prywatność (część II) Laurent MT](https://gist.github.com/LaurentMT/d361bca6dc52868573a2)
- [Transakcje Bitcoin i prywatność (część III) Laurent MT](https://gist.github.com/LaurentMT/e8644d5bc903f02613c6)
- Strona internetowa KYCP
- [Średni artykuł na temat wprowadzenia do skryptu Boltzmanna autorstwa Laurenta MT](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)