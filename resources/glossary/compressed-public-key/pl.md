---
term: SKOMPRESOWANY KLUCZ PUBLICZNY
---

Klucz publiczny jest używany w skryptach (bezpośrednio w formie klucza publicznego lub jako Address) do odbierania i zabezpieczania bitcoinów. Surowy klucz publiczny jest reprezentowany przez punkt na krzywej eliptycznej, składający się z dwóch współrzędnych (`x, y`) po 256 bitów każda. W surowym formacie klucz publiczny mierzy zatem 512 bitów, nie licząc dodatkowego bajtu identyfikującego format. Z drugiej strony, skompresowany klucz publiczny jest bardziej kompaktową formą reprezentacji klucza publicznego. Używa tylko współrzędnej `x` i prefiksu (`02` lub `03`), który wskazuje parzystość współrzędnej `y` (parzysta lub nieparzysta).


Jeśli uprościmy to do dziedziny liczb rzeczywistych, to biorąc pod uwagę, że krzywa eliptyczna jest symetryczna względem osi x, dla dowolnego punktu $P$ (`x, y`) na krzywej, istnieje punkt $P'$ (`x, -y`), który również będzie na tej samej krzywej. Oznacza to, że dla każdego `x` istnieją tylko dwie możliwe wartości `y`, dodatnia i ujemna. Na przykład, dla danej odciętej `x`, będą dwa punkty $P1$ i $P2$ na krzywej eliptycznej, dzielące tę samą odciętą, ale o przeciwnych rzędnych:


![](../../dictionnaire/assets/29.webp)

Aby wybrać pomiędzy dwoma potencjalnymi punktami na krzywej, do `x` dodawany jest prefiks określający, który `y` wybrać. Metoda ta pozwala zmniejszyć rozmiar klucza publicznego z 520 bitów do zaledwie 264 bitów (8 bitów prefiksu + 256 bitów dla `x`). Ta reprezentacja jest znana jako skompresowana forma klucza publicznego.


Jednak w kontekście kryptografii krzywych eliptycznych nie używamy liczb rzeczywistych, ale skończonego pola rzędu `p` (liczba pierwsza). W tym kontekście "znak" `y` jest określony przez jego parzystość, to znaczy, czy `y` jest parzyste czy nieparzyste. Przedrostek `0x02` oznacza więc parzyste `y`, podczas gdy `0x03` oznacza nieparzyste `y`.


Rozważmy poniższy przykład surowego klucza publicznego (punkt na krzywej eliptycznej) w systemie szesnastkowym:

```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```


Możemy wyizolować przedrostek, `x` i `y`:

```plaintext
Prefix = 04
To determine the parity of `y`, we examine the last hexadecimal character of `y`:
```

Podstawa 16 (szesnastkowa): f

Podstawa 10 (dziesiętna): 15

y jest nieparzyste

```

The prefix for the compressed public key will be `03`. The compressed public key in hexadecimal becomes:
```

K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6

```