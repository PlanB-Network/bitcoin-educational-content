---
name: Podstawy JavaScript i NodeJS
goal: Naucz się podstaw programowania JavaScript i rozwoju NodeJS, aby tworzyć praktyczne aplikacje i narzędzia.
objectives: 

  - Opanuj podstawową składnię JavaScript, typy i przepływ sterowania
  - Zrozumienie funkcji, obiektów i klas w JavaScript
  - Poznaj techniki obsługi błędów i debugowania
  - Zapoznanie się z NodeJS i jego ekosystemem

---

# Rozpocznij swoją podróż rozwojową


Witamy w tym kursie JavaScript i NodeJS.


JavaScript jest najpopularniejszym językiem programowania na świecie: jest to język skryptowy nowoczesnych przeglądarek, więc w zasadzie niemożliwe jest zbudowanie nowoczesnej aplikacji internetowej bez napisania *jakiegoś* JavaScriptu; a dzięki środowisku wykonawczemu NodeJS może być również używany poza przeglądarkami, do tworzenia skryptów i aplikacji uruchamianych bezpośrednio na komputerze.


Ten kurs jest przeznaczony dla osób, które są zupełnie nowe w programowaniu lub które wcześniej używały innych języków, ale chcą zrozumieć, jak działa JavaScript, szczególnie w kontekście NodeJS.


Pod koniec kursu powinieneś być w stanie pisać własne programy w JavaScript, korzystać ze standardowej biblioteki NodeJS oraz instalować i używać pakietów innych firm do tworzenia przydatnych narzędzi.


+++
# Podstawowy JavaScript

<partId>a617327c-e5a2-52ca-9380-c63f44623dd4</partId>


## Konfiguracja

<chapterId>ba05a290-1782-5268-87c9-62fd09590e05</chapterId>




Program JavaScript to po prostu zbiór (jednego lub więcej) plików tekstowych, które zawierają polecenia do wykonania przez środowisko uruchomieniowe JavaScript.


Nazwy tych plików tekstowych zwykle kończą się rozszerzeniem `.js`, takim jak `my_script.js`, `my_program.js` itp.


Zawarte w nich polecenia są napisane w języku programowania JavaScript.


Środowisko uruchomieniowe JavaScript to specjalny program, który wykonuje te pliki.


![](assets/en/1.webp)


### Środowisko uruchomieniowe NodeJS


Najpopularniejszym środowiskiem uruchomieniowym JavaScript jest NodeJS.


Twoje IDE może już to zawierać, albo będziesz musiał pobrać to ze [strony oficjalnej](https://nodejs.org/en/download).


Strona pobierania zawiera instrukcje dla wszystkich trzech głównych systemów operacyjnych: Windows, Linux i MacOS. Zakłada się, że wiesz, jak otworzyć terminal w swoim systemie operacyjnym.


Ponieważ NodeJS jest dostępny dla wszystkich trzech systemów operacyjnych, programy, które piszesz, będą mogły być wykonywane na wszystkich z nich (z wyjątkiem niektórych przypadków brzegowych).


Oznacza to, że można na przykład napisać prostą grę wideo w JavaScript na komputerze z systemem Windows i przekazać ją znajomemu, aby uruchomił ją na swoim komputerze Mac.


![](assets/en/2.webp)














### Pierwszy program (hello world)


Tradycyjnie, podczas nauki języka programowania, pierwszy napisany program polega na wypisaniu "hello world!" na konsolę.


Utwórz katalog o nazwie `my_js_code/`, a w nim plik o nazwie `main.js` (te nazwy są dowolne).


Otwórz katalog w swoim edytorze kodu.


Wpisz ten kod do pliku:


```javascript
console.log("hello world!")
```


Otwórz terminal i wykonaj to polecenie, aby uruchomić program:


```
node main.js
```


Wynik powinien być następujący


```
hello world!
```


### Co się stało?


W JavaScript wszystko jest "obiektem".


`console` jest obiektem, który jest używany do debugowania programu.


`console.log` jest najczęściej używaną metodą `console`. Po prostu wypisuje wszystkie argumenty, które do niej przekażesz.


Przekazujesz argumenty do `console.log` używając nawiasów okrągłych `()`.


Na przykład, jeśli chcesz wydrukować liczbę `1000`, wystarczy napisać


```javascript
console.log(1000)
```


Następnie wykonaj go, uruchamiając


```
node main.js
```


w terminalu (od teraz ten kurs będzie zakładał, że wiesz, w jaki sposób wykonuje się program).


Powinno to zostać wydrukowane


```
1000
```


Możesz przekazać wiele rzeczy, takich jak


```javascript
console.log(16, 8, 1993)
```


Spowoduje to wydrukowanie


```
16 8 1993
```


## Zmienne i komentarze

<chapterId>23050ab7-343b-5edf-9d37-e4e782e27ce0</chapterId>


Programy zazwyczaj wykonują operacje na danych.


Zmienne są jak nazwane pudełka, których używamy do przechowywania danych. Pozwalają nam skojarzyć część danych z określoną nazwą, dzięki czemu możemy je później pobrać przy użyciu tej nazwy.


### deklaracje `let`


Aby zadeklarować zmienną w JavaScript, możemy użyć słowa kluczowego `let`.


Po napisaniu `let`, wpisujemy nazwę, którą chcemy nadać zmiennej, następnie znak `=`, a następnie wartość, którą chcemy przechowywać.


Na przykład:


```javascript
let age = 25

console.log(age)
```


Nazwa zmiennej (technicznie nazywana "identyfikatorem") może zazwyczaj zawierać litery, podkreślenia (`_`), znak dolara (`$`) i liczby, chociaż pierwszy znak nie może być liczbą.


W powyższym kodzie zadeklarowaliśmy zmienną o nazwie `age` i zapisaliśmy w niej wartość `25`.


Następnie wydrukowaliśmy wartość za pomocą `console.log(age)`.


Jeśli uruchomisz ten kod z `node main.js`, wynikiem będzie:


```
25
```


W identyfikatorach rozróżniana jest wielkość liter, co oznacza, że małe i duże litery liczą się jako różnice w identyfikatorach, więc na przykład


```javascript
let age = 25

let Age = 20

console.log(age)
```


wypisze 25, ponieważ są to dwie całkowicie oddzielne zmienne!


W zmiennej można również przechowywać ciągi znaków (tekst):


```javascript
let message = "hello again"

console.log(message)
```


Zostanie to wydrukowane:


```
hello again
```


Tak jak poprzednio, użyliśmy `console.log()`, aby wydrukować wartość przechowywaną w zmiennej.


Teraz zróbmy oba razem:


```javascript
let age = 25

let message = "hello again"

console.log(age)

console.log(message)
```


Uruchomienie tego spowoduje wydrukowanie:


```
25
hello again
```

### Przeniesienie


Zmienne zadeklarowane za pomocą `let` mogą zostać zmienione po ich utworzeniu.


Nazywa się to reassignment.


```javascript
let score = 10

console.log(score)

score = 15

console.log(score)
```


Najpierw przypisujemy `10` do `score`, a następnie wypisujemy go.


Następnie zmieniamy wartość `score` na `15` i wypisujemy ją ponownie.


Wynik będzie następujący:


```
10
15
```


Jest to bardzo przydatne, gdy wartość zmienia się w czasie, na przykład w grze, w której wynik rośnie.


Dodajmy do tego jeszcze jedną zmienną:


```javascript
let score = 10
let player = "Alice"

console.log(score)
console.log(player)

score = 20
player = "Bob"

console.log(score)
console.log(player)
```


Zostanie to wydrukowane:


```
10
Alice
20
Bob
```


Jak widać, zarówno `score` jak i `player` zostały zmienione.


### deklaracje `const`


W większości przypadków nie chcemy jednak, aby zmienna zmieniała się po jej utworzeniu. W tym celu używamy `const`.


`const` jest skrótem od "constant". Po przypisaniu wartości do zmiennej `const`, nie można jej zmienić.


```javascript
const pi = 3.14
console.log(pi)
```


Ten wydruk:


```
3.14
```


Ale jeśli spróbujesz to zrobić:


```javascript
const pi = 3.14
console.log(pi)

pi = 99 // this line will cause an error
console.log(pi)
```


JavaScript wyświetli błąd podobny do:


```
TypeError: Assignment to constant variable.
```


Dzieje się tak, ponieważ `pi` zostało zadeklarowane przy użyciu `const` i nie można później zmienić jego wartości. Komunikujesz interpreterowi JavaScript, że nie chcesz, aby ta zmienna się zmieniła.


Jest to przydatne, ponieważ zmniejsza szanse na zmianę przez pomyłkę. Kiedy programy stają się bardzo duże, z tysiącami linii kodu, niemożliwe jest nadążanie za wszystkim, co dzieje się jednocześnie (to główny powód, dla którego używamy komputerów, do wykonywania złożonych procesów, których nie możemy obliczyć za pomocą naszych mózgów), więc przydatne staje się posiadanie takich ograniczeń, które sprawiają, że program jest bardziej deterministyczny.


Najlepszą praktyką jest zawsze deklarowanie naszych wartości jako `const`, chyba że jesteśmy pewni, że chcemy je później zmodyfikować.


### Komentarze w JavaScript


Czasami chcemy pisać notatki w naszym kodzie, które nie są wykonywane. Są one nazywane komentarzami.


Komentarze są ignorowane przez program podczas jego działania, ale są przydatne do wyjaśniania rzeczy nam lub innym osobom.


Aby napisać jednowierszowy komentarz, należy użyć `//`


```javascript
// This is a comment
const x = 10 // This is also a comment
console.log(x)
```


To nadal będzie drukowane:


```
10
```


Komentarze są tylko po to, by ludzie mogli je czytać.


Można również pisać wielowierszowe komentarze używając `/*` i `*/`


```javascript
/*
This is a multi-line comment.
It can span several lines.
*/
const y = 20
console.log(y)
```


Spowoduje to wydrukowanie


```
20
```


Komentarz zostanie zignorowany.


Komentarze mogą służyć do dodawania niewielkich adnotacji do kodu, dzięki czemu można zapamiętać, co robi i dlaczego jest napisany w określony sposób. Może to również pomóc innym programistom w zrozumieniu kodu.


## Podstawowe typy: liczby, ciągi znaków, wartości logiczne

<chapterId>cfdb04f6-21a8-5143-bbf9-7aaae04962f0</chapterId>


W JavaScript "typ" określa, jakiego rodzaju danymi jest dana wartość.


Javascript ma kilka podstawowych typów, a w tej sekcji omówimy niektóre z nich.


### Liczby i operacje arytmetyczne


Pierwszym typem, który wprowadzimy jest `number`.


Liczby w JavaScript mogą być całkowite (jak `5`) lub dziesiętne (jak `3.14`).


Za ich pomocą można wykonywać działania arytmetyczne: dodawanie, odejmowanie, mnożenie i dzielenie.


Oto podstawowy przykład:


```javascript
const a = 10
const b = 5

const sum = a + b
const difference = a - b
const product = a * b
const quotient = a / b

console.log(sum)
console.log(difference)
console.log(product)
console.log(quotient)
```


Zostanie to wydrukowane:


```
15
5
50
2
```


Można również użyć nawiasów `()` by kontrolować kolejność operacji:


```javascript
const result = (2 + 3) * 4
console.log(result)
```


Ten wydruk:


```
20
```


Bez nawiasów byłoby to `2 + 3 * 4`, czyli:


```javascript
const result = 2 + 3 * 4
console.log(result)
```


To by się wydrukowało:


```
14
```


Ponieważ w zwykłej matematyce mnożenie odbywa się przed dodawaniem.


### Ciągi znaków i interpolacja


Drugim typem JavaScript, który wprowadzimy jest `string`.


Ciągi znaków są fragmentami tekstu. Do ich tworzenia można używać pojedynczych cudzysłowów `'..."` lub podwójnych cudzysłowów `"..."`.


```javascript
const greeting = "hello"
const name = 'Bob'
console.log(greeting)
console.log(name)
```


Ten wydruk:


```
hello
Bob
```


Aby połączyć ciągi znaków, można użyć operatora `+`:


```javascript
const greeting = "hello"
const space = " "
const name = "Bob"

const fullGreeting = greeting + space + name
console.log(fullGreeting)
```


Zostanie to wydrukowane:


```
hello Bob
```


Istnieje jednak przyjemniejszy sposób łączenia ciągów zwany **interpolacją ciągów**. Używasz backticks do zadeklarowania łańcucha `` `...`` i zapisujesz zmienne używając `${...}` wewnątrz łańcucha:


```javascript
const greeting = "hello"
const name = "Bob"

const fullGreeting = `${greeting} ${name}`
console.log(fullGreeting)
```


Jest to również drukowane:


```
hello Bob
```


Wewnątrz `${...}` można zawrzeć dowolne wyrażenie:


```javascript
const age = 30
console.log(`Next year, I will be ${age + 1} years old.`)
```


Ten wydruk:


```
Next year, I will be 31 years old.
```


Interpolacja jest bardzo powszechna w nowoczesnym JavaScript.


### Liczby logiczne, porównywanie i operacje logiczne


Trzecim typem, który wprowadzimy jest `boolean`. Nazwa pochodzi od matematyka George'a Boole'a, który wynalazł logikę boole'owską.


Wartości logiczne są proste: tylko dwie możliwe wartości, `true` i `false`.


Można je przechowywać w zmiennych:


```javascript
const theSkyIsBlue = true
const thisCourseIsBad = false

console.log(theSkyIsBlue)
console.log(thisCourseIsBad)
```


Ten wydruk:


```
true
false
```


Wartości logiczne można łączyć za pomocą operatorów logicznych:



- `&&` oznacza "and" i zwróci `true` tylko wtedy, gdy **obydwie** wartości są `true`, w przeciwnym razie zwróci `false`
- `||` oznacza "lub" i zwróci `true`, jeśli **przynajmniej jedna** z wartości jest `true`, w przeciwnym razie (jeśli obie są fałszywe) zwróci `false`
- `!` oznacza "nie", jest stosowane przed wartością logiczną i odwraca ją: jeśli wartość logiczna jest `true`, zwróci `false` i odwrotnie.


![](assets/en/3.webp)


Przykłady:


```javascript
const isSunny = true
const isWarm = true

console.log(isSunny && isWarm)  // true
console.log(isSunny || isWarm)  // true
console.log(!isSunny)           // false
```


Możesz porównywać wartości w JavaScript używając operatorów takich jak `>`, `<`, `==` i `!==`. Wynikiem tych porównań jest zawsze wartość logiczna.


```javascript
const first = 10
const second = 5

const firstIsGreater   = (a > b)
const secondIsGreater  = (a < b)
const theyAreEqual     = (a === b)
const theyAreDifferent = (a !== b)

console.log(firstIsGreater)   // true
console.log(secondIsGreater)   // false
console.log(theyAreEqual)  // false
console.log(theyAreDifferent)  // true
```


Javascript ma również `>=` oznaczające "większy lub równy" i `<=` oznaczające "mniejszy lub równy".


Wartości logiczne, operatory porównania i logiczne są często łączone w programach w celu zadeklarowania złożonych warunków, takich jak zapewnienie, że "wiadomość e-mail dotarła ORAZ zawiera obraz, którego potrzebuję LUB długość wiadomości e-mail jest dłuższa niż 10000 znaków". Później okaże się, że są to niezbędne elementy do zbudowania logiki programu.


## Tablice, null, undefined

<chapterId>7bf18183-5eae-53ed-83d2-b04982145d81</chapterId>


W tej sekcji omówimy trzy kolejne typy, które są bardzo powszechne w programach JavaScript:



- Tablice**: sekwencje wartości
- undefined**: wartość specjalna, która oznacza "nic nie zostało przypisane"
- null**: kolejna wartość specjalna, która oznacza "celowo pusty"


### Tablice i dostęp do indeksów


Tablica** jest typem, który może przechowywać wiele wartości na liście.


Tablicę tworzy się za pomocą nawiasów kwadratowych `[]` i oddzielając elementy przecinkami.


Oto podstawowy przykład:


```javascript
const numbers = [10, 2, 88]
console.log(numbers)
```


Ten wydruk:


```
[ 10, 2, 88 ]
```


W tablicy można przechowywać wszystko, nie tylko liczby:


```javascript
const things = ["apple", 42, true]
console.log(things)
```


Ten wydruk:


```
[ 'apple', 42, true ]
```


Aby uzyskać dostęp do określonego elementu w tablicy, używamy **index**. Indeks jest pozycją elementu, zaczynając od **0**.


Tak więc w tej tablicy:


```javascript
const colors = ["red", "green", "blue"]
```



- `colors[0]` to `"red"`
- `colors[1]` to `"Green"`
- `colors[2]` to `"niebieski"`


Spróbujmy:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[0])
console.log(colors[1])
console.log(colors[2])
```


Zostanie to wydrukowane:


```
red
green
blue
```


Można przypisać wartość do określonego indeksu tablicy


```javascript
const colors = ["red", "green", "blue"]

colors[1] = "yellow"

console.log(colors)
```


Zostanie to wydrukowane:


```
[ 'red', 'yellow', 'blue' ]
```


Jako indeksu można użyć dowolnej liczby naturalnej, nawet przechowywanej w zmiennej


```javascript

const i = 1
const colors = ["red", "green", "blue"]
console.log(colors[i])
```


Zostanie to wydrukowane:


```
green
```


Ale jeśli spróbujesz uzyskać dostęp do indeksu, który nie istnieje, otrzymasz `undefined`:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[3])
```


Ten wydruk:


```
undefined
```


Co to jest?


### `undefined`


Wartość specjalna `undefined` oznacza "nie przypisano żadnej wartości".


Jeśli utworzysz zmienną, ale nie nadasz jej wartości, będzie ona `niezdefiniowana`:


```javascript
const name
console.log(name)
```


Ten wydruk:


```
undefined
```


Ponieważ nie przypisaliśmy niczego do `name`, JavaScript domyślnie ustawia ją na `undefined`.


Jak widzieliśmy wcześniej, można również uzyskać `undefined`, gdy uzyskuje się dostęp do indeksu tablicy, który nie istnieje:


```javascript
const fruits = ["banana", "apple"]
console.log(fruits[2]) // There is no index 2
```


Ten wydruk:


```
undefined
```


### `null` i jak go traktować


`null` jest również wartością specjalną. Oznacza ona "nic tu nie ma i zrobiłem to celowo"


W przeciwieństwie do `undefined`, które jest automatyczne, `null` jest czymś, co ustawia się samemu.


Na przykład:


```javascript
const currentUser = null
console.log(currentUser)
```


Ten wydruk:


```
null
```


Dlaczego używać `null`? Może spodziewasz się wartości później, ale nie jest ona jeszcze gotowa:


```javascript
let winner = null

// Later in the program:
winner = "Alice"

console.log(winner)
```


Ten wydruk:


```
Alice
```


Tak więc `null` jest przydatne, gdy chcesz powiedzieć, na przykład, "Powinno tu być coś później, ale teraz jest puste"


## Bloki i przepływ sterowania

<chapterId>be985168-2636-5b0d-a48f-ac1bbfbff8a7</chapterId>


Do tej pory pisaliśmy głównie linie kodu, które uruchamiały się jedna po drugiej.


Ale kiedy kodujemy, możemy kontrolować kolejność jego wykonywania.


Nazywa się to **przepływem sterowania**.


Zacznijmy od zrozumienia bloków i zakresu.


### Zakres globalny


Każda zmienna, którą deklarujemy, istnieje w **zakresie**, co oznacza obszar kodu, w którym zmienna jest znana.


Jeśli zadeklarujesz zmienną poza jakimkolwiek blokiem, istnieje ona w **globalnym zakresie**.


```javascript
const color = "blue"
console.log(color)
```


Ta zmienna `color` jest w zakresie globalnym, więc można uzyskać do niej dostęp z dowolnego miejsca w pliku.


Jeśli dodasz więcej linii:


```javascript
const color = "blue"
console.log(color)

const size = "large"
console.log(color)
console.log(size)
```


Zarówno `color` jak i `size` są zmiennymi globalnymi. Są one dostępne wszędzie w pliku.


Ale co dzieje się wewnątrz bloku?


### Bloki i zakres lokalny


Blok** to fragment kodu otoczony nawiasami klamrowymi `{}`.


Zmienne zadeklarowane z `let` lub `const` wewnątrz bloku istnieją **tylko** wewnątrz tego bloku.


```javascript
{
const message = "inside block"
console.log(message)
}
```


Ten wydruk:


```
inside block
```


Ale jeśli spróbujesz tego:


```javascript
{
const message = "inside block"
}
console.log(message) // Error!
```


JavaScript wyświetli błąd podobny do:


```
ReferenceError: message is not defined
```


Dzieje się tak, ponieważ `message` zostało zadeklarowane wewnątrz bloku i nie istnieje poza nim.


Oznacza to, że możemy używać bloków do izolowania części naszego kodu i mieć pewność, że "to, co dzieje się w bloku, pozostaje w bloku" (trochę jak w Las Vegas).


Organizowanie naszego kodu w bloki pozwala nam również na ustrukturyzowanie wykonywania programu, z konstrukcjami przepływu sterowania, takimi jak `if`


### `if`, `else`


Czasami chcemy uruchomić kod **tylko jeśli** coś jest prawdą. Do tego właśnie służy instrukcja `if`.


```javascript
const myAge = 20

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Ten wydruk:


```
Am I an adult?
Yes I am!
```


Jak widać, kod porównuje `myAge` i `18`.

W tym przypadku operator `>=` zwraca `true`, więc blok zostanie wykonany.

Jeśli warunek nie jest `true`, blok nie zostanie wykonany.


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Ten wydruk:


```
Am I an adult?
```


Możesz dodać blok `else`, aby obsłużyć odwrotny przypadek:


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
} else {
console.log("No, I am not.")
}
```


Ten wydruk:


```
Am I an adult?
No, I am not.
```


Zarówno bloki `if` jak i `else` są wciąż blokami - więc zmienne zadeklarowane wewnątrz nich nie istnieją poza nimi.


Jeśli chcemy być pewni, że coś nie jest **prawdą**, co możemy zrobić?


Cóż, jak wspomniano wcześniej, JavaScript ma operator "not", który odwraca wartości logiczne. Możemy więc zrobić


```javascript
const myAge = 17

const adult = myAge >= 18

console.log("Am I an adult?")

if (!adult) {
console.log("No, I am not.")
}
```

To nadal się drukuje:


```
Am I an adult?
No, I am not.
```

Ponieważ użyliśmy operatora `!` do odwrócenia zmiennej `adult`.


`if (!adult) {...}` powinno być czytane jako "if not adult..."


Używając bloków, logiki i operatorów porównania, możemy ustrukturyzować wykonanie programu, definiując zmienne, które muszą być `prawdziwe` (lub `fałszywe`), aby coś się wydarzyło.


### `while`, `break`, `continue`


Pętla `while` powtarza kod *dopóki* warunek jest prawdziwy.


```javascript
let count = 0

while (count < 3) {
console.log("Count is", count)
count = count + 1
}
console.log("the loop is over!")
```


Ten wydruk:


```
Count is 0
Count is 1
Count is 2
the loop is over!
```


Gdy `count` osiągnie wartość 3, pętla zostanie zatrzymana.


Pętlę można zatrzymać wcześniej za pomocą `break`:


```javascript
let number = 1 // Start with number 1

while (true) { // This condition is always true, so this loop will run forever unless we stop it
console.log(number) // Print the current number
if (number === 3) { // If the number is 3, stop the loop
break
}
number = number + 1 // Add 1 to the number
}
```


Ten wydruk:


```
0
1
2
```


Ponieważ kiedy liczba staje się `3`, blok `if` zostaje wykonany i zatrzymuje pętlę.


Resztę pętli można pominąć używając `continue`:


```javascript
let number = 0 // Start with number 0

while (number < 5) { // Keep going while number is less than 5
number = number + 1 // Add 1 to the number

if (number === 3) { // If the number is 3
continue // Skip the rest of the block and go to the next iteration of the loop
}

console.log(number) // Print the number
}
```


Ten wydruk:


```
1
2
4
5
```


Ponieważ gdy liczbą było `3`, `continue` sprawiało, że program pomijał linię wypisującą liczbę.


### `dla ... z ...`


Jeśli masz tablicę i chcesz zrobić coś z każdym elementem w niej, możesz użyć `for ... of ... {...}`.


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const fruit of fruits) {
console.log(fruit)
}
```


Ten wydruk:


```
apple
banana
cherry
```

Blok zostanie wykonany raz dla każdego elementu tablicy.


`fruit` to nowa zmienna, która przyjmuje wartość każdego elementu w tablicy, aby operować na nim wewnątrz bloku.


### `dla ... w ...`


Możesz użyć `for ... in` do pętli nad kluczami (indeksami) tablicy:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(index)
}
```


Ten wydruk:


```
0
1
2
```


Możesz również użyć indeksu, aby uzyskać wartość:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(fruits[index])
}
```


Wypisuje to samo co `for ... of`:


```
apple
banana
cherry
```


W praktyce, w przypadku tablic, powinieneś preferować użycie `for ... of`, ponieważ jest to prostsze i czystsze.


### Pętle ograniczone


Czasami chcemy zapętlić określoną liczbę razy lub ogólnie napisać fragment kodu, który powtarza blok, jednocześnie śledząc coś.

Do tego właśnie służy ograniczona pętla `for`.

Ograniczona pętla zwykle przyjmuje trzy warunki, oddzielone średnikiem `;`, jak w `(... ; ... ; ....)`.


```javascript
for (let i = 0; i < 3; i = i + 1) {
console.log(i)
}
```


Ten wydruk:


```
0
1
2
```


Wyjaśnijmy to:



- `let i = 0`: deklaruje zmienną do użycia w bloku (w tym przypadku jest to licznik, który zaczyna się od 0)
- `i < 3`: deklaruje warunek `true` dla bloku, który ma zostać wykonany (w tym przypadku jest to "repeat while `i` is less than 3")
- `i = i + 1`: deklaracja kodu, który ma być uruchamiany po każdym wykonaniu bloku (w tym przypadku "zwiększ `i` o 1")


Jak widać, w pętli ograniczonej możemy zadeklarować bardziej złożone warunki dla wielokrotnego wykonywania fragmentu kodu, ale w większości przypadków nie jest to konieczne.


### Etykiety bloków


Jeśli musisz napisać bardziej złożony przepływ sterowania, JavaScript pozwala ci nazwać blok używając **etykiety**, która może być użyta przez `break` lub `continue` do określenia *gdzie* przeskoczyć z powrotem.


Przykład:


```javascript
outer: {
console.log("We're inside the outer scope.")

inner: {
console.log("We're inside the inner scope.")
break outer
}

console.log("This will not run")
}

console.log("Done")
```


Ten wydruk:


```
Inside outer block
Inside inner block
Done
```


Użyliśmy `break outer`, aby całkowicie opuścić blok `outer`.


Pętle można również oznaczać etykietami. Weźmy ten przykład:


```javascript
// Declare a variable to count the total number of days in a year
let totalDaysInOneYear = 0

// Declare one variable per month, with the number of the month
const january = 1
const february = 2
const march = 3
const april = 4
const may = 5
const june = 6
const july = 7
const august = 8
const september = 9
const october = 10
const november = 11
const december = 12

// Declare an array that holds the months that have 30 days
const monthsWith30Days = [
april, june, september, november
]

// Declare variables to keep track of the month and day we're in
let currentMonth = january
let currentDay = 1

monthsLoop: while (true) {  // Start a loop labeled "monthsLoop" to process each month

daysLoop: while (true) {  // Start a loop labeled "daysLoop" to process each day in the month
totalDaysInOneYear = totalDaysInOneYear + 1  // Increase the total number of days we counted by 1

if (                                                                   // We want to check if we're at the end of the month.
currentDay === 31                                                  // Check if the current day is 31 (for months with 31 days)...
|| currentDay === 30 && (monthsWith30Days.includes(currentMonth))  // ...or 30 if it's among the 30-days months...
|| currentDay === 28 && (currentMonth === february)                // ...or 28 if it's February. If it's any of these three, then:

){
currentMonth = currentMonth + 1  // Move to the next month
currentDay = 1                   // Reset the day to 1 for the new month
break daysLoop                   // Exit the inner loop (which tracks days) and go back to the outer loop (which tracks months)
}
else { currentDay = currentDay + 1 }                                   // Otherwise, we're not at the end of the month, and we just move to the next day

}
if (currentMonth > 12) {  // After processing a month, check if we've gone past December
break monthsLoop  // If so, break the outer loop and stop the day-counting process
}
}

console.log(totalDaysInOneYear)  // Print the total number of days in the year (should be 365)
```

To był bardzo nudny przykład, ale mam nadzieję, że wyjaśnił (sporadyczną) potrzebę stosowania etykiet.


## Wprowadzenie funkcji

<chapterId>cc324715-09c2-5cf7-9e6f-47a6f16bc04d</chapterId>


W miarę rozwoju programów, często będziesz chciał **ponownie wykorzystać** fragmenty kodu.


Do tego właśnie służą **funkcje**: pozwalają one na zgrupowanie kodu, nadanie mu nazwy i uruchomienie go w dowolnym momencie.


### Deklaracja funkcji


Aby zadeklarować funkcję, możemy użyć słowa kluczowego `function`. Następnie nadajemy jej nazwę, parę nawiasów `()` z argumentami, które przyjmuje, oraz blok kodu `{}` do wykonania. Zacznijmy od funkcji, która nie przyjmuje żadnych argumentów:


```javascript
function sayHello () {console.log(`Hello!`) }
```


Ten kod **deklaruje** funkcję, ale **jeszcze** jej nie uruchamia.


### Wywołania funkcji


Aby uruchomić (lub "wywołać") funkcję, należy wpisać jej nazwę, a następnie nawiasy:


```javascript
function sayHello () {console.log(`Hello!`) }
sayHello()
```


Ten wydruk:


```
Hello!
```


Funkcję można wywołać dowolną liczbę razy:


```javascript
function sayHello() {
console.log("Hello!")
}

sayHello()
sayHello()
```


Ten wydruk:


```
Hello!
Hello!
```


Kod wewnątrz funkcji jest uruchamiany tylko po jej wywołaniu.


### Argumenty funkcji (dane wejściowe do funkcji)


Czasami chcesz, aby funkcja działała z pewnymi danymi wejściowymi. Można to zrobić dodając **argumenty** wewnątrz nawiasów.


Na przykład:


```javascript
function sayHelloTo (friend) {
console.log(`Hello ${friend}!`)
}
```


Teraz ta funkcja przyjmuje **jeden argument** o nazwie `friend`.


Podczas wywoływania funkcji można przekazać wartość:


```javascript
sayHelloTo("Tommy")
```


Ten wydruk:


```
Hello Tommy!
```


Funkcję można wywołać ponownie z inną nazwą:


```javascript
sayHelloTo("Sam")
```


Ten wydruk:


```
Hello Sam!
```


Przekazana wartość zastępuje zmienną `friend` wewnątrz funkcji.


Można również użyć więcej niż jednego argumentu:


```javascript
function greetTwoPeople(person1, person2) {
console.log(`Hello ${person1} and ${person2}!`)
}

greetTwoPeople("Lina", "Marco")
```


Ten wydruk:


```
Hello Lina and Marco!
```


### `return` (wyjście z funkcji)


Funkcje mogą również **zwracać** wartości. Oznacza to, że wysyłają wartość z powrotem do miejsca, w którym funkcja została wywołana.


Oto prosty przykład:


```javascript
function getNumber() {
return 42
}

const result = getNumber()
console.log(result)
```


Ten wydruk:


```
42
```


Funkcja `getNumber()` zwraca `42` i przechowujemy ją w `result`, a następnie wypisujemy.


Możesz również zwrócić coś, co sam obliczyłeś:


```javascript
function add(a, b) {
return a + b
}

const result = add(2, 3)
console.log(result)
```


Ten wydruk:


```
5
```


Po zwróceniu wartości funkcja zatrzymuje się. Wszystko po `return` w tym bloku się nie dzieje.


```javascript
function saySomething() {

return "hi"

console.log("this never runs")

}

const message = saySomething()
console.log(message)
```


Tylko ten wydruk:


```
hi
```


ponieważ zwracane jest tylko "hi". Linia `console.log("this never runs")` jest pomijana.


O funkcjach można myśleć jak o małych podprogramach. Każda funkcja może pobierać dane wejściowe, pracować nad nimi i zwracać dane wyjściowe.


Co się stanie, jeśli spróbujemy użyć wartości zwracanej przez funkcję, która niczego nie zwróciła?


```javascript
function doesNothing () {}

const x = doesNothing()

console.log(x)
```

Spowoduje to wypisanie `undefined`. Wartością zwracaną funkcji, która niczego nie zwróciła jest `undefined`.


## Obiekty i klasy

<chapterId>26689f25-8212-5057-8c21-3a05eee0ac75</chapterId>


JavaScript jest często nazywany językiem obiektowym.


Oznacza to, że pomaga organizować kod poprzez grupowanie wartości i funkcji w **obiekty**.


### Czym jest `obiekt`?


Obiekt może zawierać dane i funkcje, które operują na tych danych. Kiedy funkcja jest umieszczona w obiekcie, mówimy, że jest to `metoda`.


Pierwszym obiektem, który widzieliśmy był obiekt `console`. Jest to obiekt, który zawiera wiele metod do drukowania rzeczy na ekranie i debugowania naszych programów.


Może nawet drukować samodzielnie; można to zrobić


```javascript
console.log(console)
```


i wydrukuje listę metod, które zawiera. Na przykład, na moim komputerze wypisał


```javascript
Object [console] {
log: [Function: log],
warn: [Function: warn],
error: [Function: error],
dir: [Function: dir],
time: [Function: time],
timeEnd: [Function: timeEnd],
timeLog: [Function: timeLog],
trace: [Function: trace],
assert: [Function: assert],
clear: [Function: clear],
count: [Function: count],
countReset: [Function: countReset],
group: [Function: group],
groupEnd: [Function: groupEnd],
table: [Function: table],
debug: [Function: debug],
info: [Function: info],
dirxml: [Function: dirxml],
groupCollapsed: [Function: groupCollapsed],
Console: [Function: Console],
profile: [Function: profile],
profileEnd: [Function: profileEnd],
timeStamp: [Function: timeStamp],
context: [Function: context],
createTask: [Function: createTask]
}
```


Jak widać, ma wiele metod, które można wykorzystać do debugowania!


Javascript zapewnia nam różne sposoby tworzenia nowych obiektów, które mogą robić wszystko, co chcemy.


### Tworzenie obiektu


Najprostszym sposobem na utworzenie obiektu jest zgrupowanie danych i funkcji za pomocą ** nawiasów klamrowych** `{}`.


Tworzy to coś, co nazywamy **anonimowym obiektem**


```javascript
const cat = {
name: "Whiskers",
age: 3
}
```


Tworzy to obiekt i przechowuje go w zmiennej o nazwie `cat`.


Obiekt ma dwie **właściwości**:



- `name` z wartością `"Whiskers"`
- `age` z wartością `3`


Wydrukujmy to:


```javascript
console.log(cat)
```


Ten wydruk:


```
{ name: 'Whiskers', age: 3 }
```


Właściwości można pobrać z obiektu za pomocą kropki, jak w `objectName.propertyName`:


```javascript
console.log(cat.name)  // prints "Whiskers"
console.log(cat.age)   // prints 3
```


Można również **zmienić** właściwość:


```javascript
cat.age = 4
console.log(cat.age)  // now it prints 4
```


Jak widać, nawet jeśli obiekt jest zdefiniowany jako `const`, wciąż można modyfikować zawarte w nim dane.


W przypadku obiektów, `const` powstrzyma cię jedynie przed nadpisaniem całego obiektu:


```javascript
const cat = {
name: "Whiskers",
age: 3
}

cat.age = 5 // this works

cat = 5 // this throws an error, you're trying to reassign the whole object

```


Jak wspomniano wcześniej, obiekty mogą również przechowywać **funkcje**, a gdy funkcja jest częścią obiektu, nazywamy ją **metodą**.


Oto przykład:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log("Meow!")
}
}
```


Ten obiekt posiada:



- Właściwość `name`
- Metoda `speak()`


Wywołajmy metodę:


```javascript
cat.speak()
```


Drukuje:


```
Meow!
```


Metody mogą korzystać z danych zawartych w obiekcie poprzez słowo kluczowe `this`.

`this` odnosi się do bieżącego obiektu. W tym przykładzie zostanie on użyty do wydrukowania nazwy kota:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log(`${this.name} says meow!`)
}
}

cat.speak()
```


Ten wydruk:


```
Whiskers says meow!
```


Słowo `this` oznacza "ten obiekt"... w tym przypadku obiekt `cat`.



Tego rodzaju obiekty są świetne, gdy potrzebujesz czegoś szybkiego i prostego. Ale jeśli potrzebujesz stworzyć **wiele obiektów** o tej samej strukturze, istnieje lepszy sposób i właśnie tam pojawiają się **klasy**.


### Klasy i konstruktory


**Klasa** jest jak plan. Mówi JavaScript, jak utworzyć określony rodzaj obiektu.


Klasę definiuje się za pomocą słowa kluczowego `class`, po którym następuje nazwa klasy i blok nawiasów klamrowych `{}`.


```javascript
class Dog {}
```


Klasy zwykle zaczynają się wielką literą, zgodnie z konwencją.


Nowy obiekt klasy można utworzyć za pomocą `new`:


```javascript
const hachiko = new Dog()
```


Spróbuj wydrukować obiekt:

```javascript
class Dog {}

const myDog = new Dog()

console.log(myDog)
```


Otrzymasz


```
Dog {}
```


Jak widać, klasa Dog jest pusta, więc obiekt `myDog` również jest pusty.


Możemy zdefiniować jakie właściwości powinny zawierać obiekty Dog poprzez dodanie `konstruktora`.


Konstruktor to specjalna funkcja uruchamiana podczas tworzenia (lub "konstruowania") nowego obiektu.


```javascript
class Dog {
constructor() { }
}
```


Chcemy, aby każdy pies miał nazwę, więc dodajemy parametr `name` do funkcji:


```javascript
class Dog {
constructor(name) { }
}
```


Następnie używamy `this`, aby zadeklarować, że `name` jest `name` obiektu `Dog`, który budujemy


```javascript
class Dog {
constructor(name) {
this.name = name
}}
```


Spróbujmy użyć go teraz:


```javascript
class Dog {
constructor(name) {
this.name = name
}
}

const myDog = new Dog("hachiko")

console.log(myDog)
```


To drukuje coś takiego:


```
Dog { name: 'hachiko' }
```


Jak widać, metoda `constructor` pobiera argumenty przekazane klasie podczas wykonywania `new Dog()` i używa ich do zbudowania obiektu.


Rozłóżmy to na czynniki pierwsze:



- `class Dog` definiuje klasę Dog.
- `constructor(name)` ustawia obiekt podczas jego tworzenia.
- `this.name = name` przechowuje wartość w nowym obiekcie.
- `new Dog("hachiko")` tworzy nowy obiekt z klasy, z właściwością `name` ustawioną na `"hachiko"`.


Dodajmy teraz metodę do naszej klasy:


```javascript
class Dog {
constructor(name) {
this.name = name
}
speak () {
console.log(`${this.name} says barf!`)
}

}

const myDog = new Dog("hachiko")

myDog.speak()
```


Spowoduje to wydrukowanie


```javascript
hachiko says barf!
```


Jeśli zrobimy to samo dla dwóch różnych instancji Dog



```javascript
class Dog {
constructor(name) {
this.name = name
}
speak () {
console.log(`${this.name} says barf!`)
}

}

const myDog = new Dog("hachiko")

myDog.speak()

const yourDog = new Dog("bobby")

yourDog.speak()
```


otrzymujemy


```
hachiko says barf!
bobby says barf!
```


metoda `speak()` używa właściwości `name` obiektu `Dog`, na którym została wywołana.


Jest to główny powód istnienia klas: pozwalają nam one zdefiniować zestaw metod, które działają na danych, a następnie tworzyć wiele obiektów, które dzielą ten sam "kształt" danych.


Gdy wywołamy metodę na jednym z tych obiektów, będzie ona operować na danych przechowywanych przez *ten konkretny obiekt*.


### Zmiana kształtu obiektu


Obiekty w JavaScript są elastyczne. Nawet po ich utworzeniu można dodawać nowe właściwości lub usuwać istniejące.


Jest to dozwolone, ale należy z tego korzystać ostrożnie.


Zacznijmy od naszej prostej klasy `Dog`:


```javascript
class Dog {
constructor(name) {
this.name = name
}

speak() {
console.log(`${this.name} says barf!`)
}
}

const myDog = new Dog("Fido")
```


W tym momencie `myDog` ma tylko jedną właściwość: `name`. Wciąż możemy dodawać nowe właściwości po jego utworzeniu:


```javascript
myDog.age = 5

console.log(myDog.age) // prints 5
```


Możemy również dodać nową metodę:


```javascript
myDog.jump = function () {
console.log(`${this.name} jumps!`)
}

myDog.jump() // Fido jumps!
```


Możemy także usuwać właściwości, używając słowa kluczowego `delete`.


```javascript
delete myDog.name

console.log(myDog.name) // prints 'undefined'
```


To działa, ale jest coś ważnego, o czym warto wiedzieć: Silniki JavaScript, takie jak V8 (używane w Node.js i przeglądarce Chrome) działają szybciej, gdy obiekty zawsze zachowują te same właściwości. Jeśli dodasz lub usuniesz właściwości po utworzeniu obiektu, może to spowolnić działanie.


W małych programach nie ma to większego znaczenia. Ale w większych projektach (takich jak gry) lepiej jest wymienić wszystkie właściwości w konstruktorze od samego początku, nawet jeśli nie używasz ich od razu. Utrzymuje to stabilny kształt obiektu i pomaga w szybszym działaniu kodu.


Na przykład zamiast tego:


```javascript
class Dog {
constructor(name) {
this.name = name
}
}

const dog = new Dog("Rex")
dog.age = 4
dog.breed = "Labrador"
```


Możesz zrobić


```javascript
class Dog {
constructor(name, age, breed) {
this.name = name
this.age = age
this.breed = breed
}
}

const dog = new Dog("Rex", 4, "Labrador")
```


Obie wersje działają, ale druga jest lepsza pod względem wydajności. Mówisz silnikowi z góry, jakie właściwości będzie miał każdy obiekt, i może on odpowiednio zoptymalizować.


JavaScript pozwala na swobodne przekształcanie obiektów, ale podczas korzystania z klas najlepiej jest zaplanować kształt obiektu z wyprzedzeniem.



### Dziedziczenie z `extends` i `super()`


Czasami chcesz stworzyć klasę, która jest *prawie* taka sama jak inna klasa, ale z kilkoma dodatkowymi funkcjami.


Zamiast modyfikować kształt obiektów (co, jak wspomniano wcześniej, nie jest optymalne pod względem wydajności) lub przepisywać nową klasę od zera, JavaScript pozwala na użycie czegoś, co nazywa się **dziedziczeniem**.


Dziedziczenie oznacza, że jedna klasa może **rozszerzyć** inną. Nowa klasa otrzymuje wszystkie właściwości i metody starej, a ty możesz dodać więcej lub zmienić to, czego potrzebujesz.


Załóżmy, że mamy klasę bazową o nazwie `Vehicle`:


```javascript
class Vehicle {
constructor(brand) {
this.brand = brand
}

start() {
console.log(`${this.brand} vehicle is starting...`)
}
}
```


Teraz chcemy stworzyć klasę `Car`. Samochód jest rodzajem pojazdu, ale możemy chcieć, aby miał kilka dodatkowych funkcji lub inny komunikat, gdy się uruchamia. Zamiast przepisywać wszystko, możemy użyć `extends`:


```javascript
class Car extends Vehicle {
start() {
console.log(`${this.brand} car is ready to drive!`)
}
}
```


Klasa `Car` teraz **dziedziczy** wszystko od `Vehicle`. Otrzymuje właściwość `brand` i zastąpiliśmy metodę `start()` naszą własną wersją.


![](assets/en/4.webp)


Wypróbujmy to:


```javascript
const myCar = new Car("Toyota")
myCar.start()
```


Ten wydruk:


```
Toyota car is ready to drive!
```


Nawet jeśli `Car` nie ma własnego konstruktora, wciąż używa tego z `Vehicle`. Ale jeśli chcemy napisać niestandardowy konstruktor w `Car`, możemy to zrobić, musimy tylko dołączyć wywołanie do konstruktora jego rodzica używając `super()`.


Oto jak to zrobić:


```javascript
class Vehicle {
constructor(brand) {
this.brand = brand
}

start() {
console.log(`${this.brand} vehicle is starting...`)
}

}

class Car extends Vehicle {
constructor(brand, model) {
super(brand) // call the parent constructor and passes the brand argument to it
this.model = model
}

start() {
console.log(`${this.brand} ${this.model} is ready to drive!`)
}
}

const myCar = new Car("Toyota", "Corolla")
myCar.start()
```


![](assets/en/5.webp)



Ten wydruk:


```
Toyota Corolla is ready to drive!
```


Podsumowując



- `extends` oznacza, że jedna klasa jest oparta na innej.
- funkcja `super()` jest używana do wywołania konstruktora rozszerzanej klasy.
- Nowa klasa otrzymuje wszystkie właściwości i metody oryginalnej klasy.
- Możesz **nadpisać** metody (takie jak `start()`), aby zrobić coś innego.


Jest to przydatne, gdy masz kilka podobnych rzeczy (takich jak samochody, ciężarówki i rowery) i chcesz, aby współdzieliły kod, ale nadal zachowywały się na swój własny sposób.


### `instanceof`


Słowo kluczowe `instanceof` sprawdza, czy obiekt został utworzony z określonej klasy.


Załóżmy, że mamy klasę o nazwie `User`:


```javascript
class User {
constructor(username) {
this.username = username
}
}

const regularUser = new User("julia123")

console.log(regularUser instanceof User)
```


Ten wydruk:


```
true
```


Potwierdzenie, że `regularUser` jest klasą `User`. To dlatego, że `regularUser` został utworzony przy użyciu klasy `User`.


Działa to również z **dziedziczonymi** klasami. Na przykład, oto klasa `Admin`, która rozszerza klasę `User`:


```javascript
class Admin extends User {}

const ourAdmin = new Admin("admin42")

console.log(ourAdmin instanceof Admin)   // true
console.log(ourAdmin instanceof User)    // true
```


Obie linie zwracają `true`. Dzieje się tak, ponieważ `Admin` jest podklasą `User`, więc `naszAdmin` jest zarówno `Adminem` jak i `Userem`


# JavaScript dla średniozaawansowanych

<partId>243f63ab-4f34-5c30-80cb-84ef46f6761d</partId>


## Obsługa błędów

<chapterId>d0206bc5-d386-5e7f-9917-5803f392448c</chapterId>


Podczas pisania bardziej złożonych programów JavaScript napotkasz **błędy**. Są to nieoczekiwane sytuacje, w których coś idzie nie tak. Może zmienna jest "niezdefiniowana", ale próbujesz jej użyć, lub jakiś kod otrzymuje nieprawidłowy typ danych wejściowych.


Jeśli nie obsłużymy tych błędów prawidłowo, nasz program może ulec awarii lub zachowywać się w nieprzewidywalny sposób. JavaScript zapewnia narzędzia do wykrywania i zarządzania tymi błędami, dzięki czemu możemy radzić sobie z nimi z większą gracją.


### Typowy błąd: dostęp do wartości w `undefined`


Oto częsta sytuacja, która powoduje błąd:


```javascript
const user = undefined
console.log(user.name)
```


Jeśli uruchomisz ten kod, otrzymasz błąd, który wygląda następująco:


```
TypeError: Cannot read properties of undefined (reading 'name')
```


To JavaScript mówi ci: "Hej, próbowałeś pobrać właściwość `name` z czegoś, co jest `undefined`, a to nie ma sensu" Jak widać, gdy wystąpi tego rodzaju błąd, program przestaje działać, chyba że specjalnie napisałeś kod, aby go złapać i obsłużyć.


### `wyrzucenie` błędu


Czasami chcesz ręcznie **wywołać błąd** w swoim kodzie. W takim przypadku należy użyć słowa kluczowego `throw`.


```javascript
throw new Error("This is a custom error message")
```


Spowoduje to natychmiastowe zatrzymanie programu i wydrukowanie:


```
Uncaught Error: This is a custom error message
```


Możesz użyć `throw` do wymuszenia reguł w swoim programie. Na przykład:


```javascript
function divide(a, b) {
if (b === 0) {
throw new Error("You can't divide by zero")
}
return a / b
}

console.log(divide(10, 2))  // OK: prints 5
console.log(divide(10, 0))  // Error!
```


Drugie wywołanie powoduje błąd, ponieważ dzielenie przez zero nie jest dozwolone w tym przykładzie.


### Łapanie błędów za pomocą `try...catch`


Jeśli nie chcesz, aby twój program zawiesił się po wystąpieniu błędu, możesz przechwycić błąd za pomocą bloku `try...catch`. Jest to przydatne, gdy chcesz, aby program **nie przestawał działać**, nawet jeśli coś się nie powiedzie.


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log("Oops! Something went wrong.")
}
```


Wyjście:


```
Oops! Something went wrong.
```


Oto jak to działa:



- Kod wewnątrz bloku `try` jest próbowany jako pierwszy.
- Jeśli wystąpi błąd, JavaScript **przeskakuje do bloku `catch`**, pomijając resztę bloku `try`.
- Blok `catch` odbiera błąd, więc można go wydrukować lub obsłużyć w inny sposób, jak na przykład


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log(`The message of the error was: "${error.message}"`)
}
```


Wyjście:


```
The message of the error was: "Cannot read properties of undefined (reading 'name')"
```


### Blok `finally


Możesz również dodać blok `finally`. Jest to kod, który **zawsze działa**, niezależnie od tego, czy wystąpił błąd, czy nie.


```javascript
try {
console.log("Trying something risky...")
throw new Error("Uh oh!")
} catch (error) {
console.log("Caught the error:", error.message)
} finally {
console.log("This will run no matter what.")
}
```


Wyjście:


```
Trying something risky...
Caught the error: Uh oh!
This will run no matter what.
```


## Unikanie błędów

<chapterId>db12d9f6-5806-514c-998e-0ae24805104e</chapterId>


Ten rozdział pokazuje niektóre z najczęstszych pułapek w JavaScript i jak ich uniknąć.


### `var` i Assignment bez deklaracji


W starszym kodzie JavaScript zmienne były często deklarowane przy użyciu słowa kluczowego `var`. W przeciwieństwie do `let` i `const`, o których już się dowiedziałeś, `var` może zachowywać się w mylący sposób.


Na przykład:


```javascript
{
var message = "hello"
}
console.log(message)
```


Można by oczekiwać, że `message` będzie istnieć tylko wewnątrz bloku, ale tak nie jest. `var` ignoruje zakres bloku i czyni zmienną dostępną w całej funkcji lub pliku.


Może to prowadzić do nieoczekiwanego zachowania, zwłaszcza w większych programach. Z tego powodu nowoczesny kod JavaScript powinien zawsze używać `let` lub `const` zamiast `var`.


Co gorsza, JavaScript pozwala przypisywać wartości do zmiennych **bez deklarowania ich w ogóle**:


```javascript
function greet() {
user = "Alice"
}
greet()
console.log(user) // prints "Alice"
```


Tworzy to nową zmienną globalną `name` bez żadnej deklaracji. Może się to zdarzyć po cichu i prowadzić do błędów, które są Hard do wyśledzenia, zwłaszcza jeśli była to tylko literówka. Zawsze deklaruj zmienne używając `let` lub `const`.


### Słaby system typów


JavaScript jest słabo typowany, co oznacza, że w razie potrzeby automatycznie konwertuje wartości z jednego typu na inny. Nazywa się to przymusem typu i choć może być wygodne, często prowadzi do mylących wyników.


Na przykład:


```javascript
console.log("5" + 1)    // "51"
console.log("5" - 1)    // 4
console.log(true + 1)   // 2
console.log(null + 1)   // 1
```


W tych przykładach JavaScript próbuje odgadnąć, co użytkownik miał na myśli. Czasami zamienia ciągi znaków na liczby, liczby logiczne na liczby lub ciągi znaków na ciągi znaków. Może to sprawić, że kod będzie zachowywał się w nieoczekiwany sposób.


Świadomość słabego systemu typowania JavaScript jest ważna. Gdy coś zaczyna działać dziwnie, może to być spowodowane nieoczekiwanym wymuszeniem typu.


### "use strict"`


Możesz włączyć bardziej rygorystyczny tryb, który zamienia niektóre ciche błędy w prawdziwe błędy i uniemożliwia korzystanie z niektórych bardziej niebezpiecznych funkcji języka.


Aby włączyć ten bardziej rygorystyczny tryb, dodaj tę linię na początku pliku lub funkcji:


```javascript
"use strict"
```


Na przykład:


```javascript
"use strict"
name = "Alice" // ReferenceError: name is not defined
```


Bez trybu ścisłego JavaScript po cichu utworzyłby zmienną globalną o nazwie `name`. Ale w trybie ścisłym staje się to prawdziwym błędem, pomagając wcześniej wychwycić błędy.


Tryb ścisły wyłącza również niektóre przestarzałe funkcje JavaScript i sprawia, że kod jest łatwiejszy do optymalizacji i utrzymania.


## Wartość a odniesienie

<chapterId>bb898425-dc2f-5e5c-864b-0cb7a4a9aea9</chapterId>


JavaScript traktuje różne rodzaje wartości na różne sposoby.


Niektóre wartości są **kopiowane** podczas przypisywania ich do zmiennej.


Inne są **współdzielone** po przypisaniu ich do nowej zmiennej, więc jeśli zmienisz jedną, druga również się zmieni.


### Przechodzenie przez wartość


Gdy wartość jest przekazywana **przez wartość**, JavaScript tworzy jej **kopię**.


Jeśli więc zmienisz jedną z nich, nie wpłynie to na drugą.


Dzieje się tak w przypadku prymitywnych typów, takich jak



- liczby
- ciągi
- booleans (`true` i `false`)
- `null`
- `undefined`


Spójrzmy na przykład:


```javascript
let a = 5
let b = a

b = 10

console.log(a) // 5
console.log(b) // 10
```


Daliśmy `b` wartość `a`, ale potem zmieniliśmy `b` na `10`.


Ponieważ liczby są przekazywane przez wartość, JavaScript skopiował `5` do `b`. `5` w `b` jest niezależne od oryginalnego `5` w `a`, więc zmiana wartości `b` nie miała wpływu na `a`.


Spróbujmy z ciągiem znaków:


```javascript
let name1 = "Alice"
let name2 = name1

name2 = "Bob"

console.log(name1) // Alice
console.log(name2) // Bob
```


Ponownie, zmiana `name2` nie wpłynęła na `name1`, ponieważ łańcuchy są również przekazywane przez wartość.


To samo dzieje się, gdy przekazujesz prymityw do funkcji: zostaje on skopiowany. Funkcja nie może więc zmienić oryginału.


```javascript
function plusOne(x) {
x = x + 1
}

let number = 5

plusOne(number)

console.log(number) // 5
```


Nawet jeśli wewnątrz funkcji `1` zostało dodane do `x`, oryginalna `liczba` nie uległa zmianie.


Dzieje się tak, ponieważ do funkcji została przekazana tylko **kopia**.


### Przekazywanie przez odniesienie


Obiekty są przekazywane **przez odniesienie**.


Oznacza to, że zamiast je kopiować, JavaScript po prostu przekazuje **referencję** do niej, a jeśli ją zmodyfikujesz, wszystkie inne zmienne, które na nią wskazują, również zobaczą zmianę.


Na przykład:


```javascript
const person1 = { name: "Alice" }
const person2 = person1

person2.name = "Bob"

console.log(person1.name) // Bob
console.log(person2.name) // Bob
```


Zarówno `person1` jak i `person2` wskazują na ten sam obiekt w pamięci.


Tak więc, gdy zmieniliśmy `person2.name`, zmieniliśmy również `person1.name`, ponieważ obaj patrzą na to samo.


Tablice są obiektami, więc spróbujmy tego samego z tablicą:


```javascript
const list1 = [1, 2, 3]
const list2 = list1

list2.push(4)

console.log(list1) // [1, 2, 3, 4]
console.log(list2) // [1, 2, 3, 4]
```


Wepchnęliśmy `4` do `list2`, ale `list1` również zostało dotknięte, ponieważ oba odnoszą się do tej samej tablicy.


Zobaczmy, co się stanie, gdy przekażemy obiekt do funkcji:


```javascript
function rename(user) {
user.name = "Charlie"
}

const person = { name: "Dana" }

rename(person)

console.log(person.name) // Charlie
```


Funkcja zmieniła obiekt! To dlatego, że otrzymała **odniesienie** do oryginalnego obiektu `person`.


Nie otrzymał kopii. Uzyskał dostęp do oryginalnego obiektu, a wraz z nim możliwość jego modyfikacji.


Ważne jest, aby pamiętać o tym rozróżnieniu, ponieważ w przeciwnym razie nasz kod może zachowywać się inaczej niż się spodziewamy. Na przykład, możemy napisać funkcję z oczekiwaniem, że nie zmodyfikuje ona otrzymanych argumentów, a później dowiedzieć się, że faktycznie je zmodyfikowała (ponieważ były one obiektami, więc zostały przekazane przez referencję).


## Praca z funkcjami

<chapterId>e0d277a8-c642-5af7-9e53-dee27c811967</chapterId>


Nauczyłeś się już, jak deklarować i używać funkcji w JavaScript. JavaScript oferuje jednak więcej narzędzi do pracy z funkcjami w potężny sposób.


### Funkcje strzałek


Funkcje strzałkowe są krótszym sposobem pisania funkcji. Zamiast używać słowa kluczowego `function`, używamy strzałki (`=>`).


Oto normalna funkcja:


```javascript
function greet(name) {
return `Hello, ${name}!`
}
```


Wersja ze strzałką wygląda następująco:


```javascript
const greet = (name) => {
return `Hello, ${name}!`
}
```


Jeśli funkcja ma **tylko jedną linię**, można pominąć nawiasy klamrowe i `return`:


```javascript
const greet = (name) => `Hello, ${name}!`
```


Jeśli funkcja ma **tylko jeden parametr**, można nawet pominąć nawiasy wokół parametrów:


```javascript
const greet = name => `Hello, ${name}!`
```


Funkcje strzałkowe są bardzo powszechne w nowoczesnym JavaScript, ponieważ pozwalają na wyrażanie prostych funkcji przy znacznie mniejszej ilości boilerplate.


### Parametry domyślne


Czasami chcesz, aby funkcja miała **wartość domyślną**, jeśli nie zostanie przekazany żaden argument.


Można to zrobić w następujący sposób:


```javascript
function sayHello(name = "friend") {
console.log(`Hello, ${name}!`)
}

sayHello("Alice") // Hello, Alice!
sayHello()        // Hello, friend!
```


Domyślna wartość `"friend"` jest używana, gdy nic nie zostanie przekazane.


### Parametry spreadu (`...`)


Co jeśli funkcja przyjmuje elastyczną liczbę argumentów?


Możesz użyć operatora **spread** (`...`), aby zebrać je w tablicę:


```javascript
function logAll(...items) {
console.log(items)
}

logAll(1, 2, 3) // [1, 2, 3]
logAll("a", "b") // ["a", "b"]
```


Następnie można użyć pętli do przetworzenia każdego elementu:


```javascript
function logEach(...items) {
for (const item of items) {
console.log(item)
}
}
```


Operator spread jest przydatny, gdy nie wiadomo, ile argumentów zostanie przekazanych.


### Funkcje wyższego rzędu


Funkcja **wysokiego rzędu** to funkcja, która:



- przyjmuje inną funkcję jako dane wejściowe
- i/lub zwraca funkcję jako dane wyjściowe


Oto prosty przykład:


```javascript
function runTwice(action) {
action()
action()
}

function sayHello(name = "friend") {
console.log(`Hello, ${name}!`)
}

runTwice(sayHello)
```


Ten wydruk:


```
Hello, friend!
Hello, friend!
```


Możemy przekazać do niej funkcję strzałki:


```javascript
runTwice(
() => console.log("Hello!")
)
```


Ten wydruk:


```
Hello!
Hello!
```


Można również pisać funkcje, które **zwracają** inne funkcje:


```javascript
function makeGreeter(name) {
return () => console.log(`Hi, ${name}`)
}

const greetAlice = makeGreeter("Alice")
const greetBob = makeGreeter("Bob")

greetAlice() // Hi, Alice
greetBob() // Hi, Bob
```


Funkcja `makeGreeter` jest funkcją, która tworzy inne funkcje. Otrzymuje ona ciąg znaków i zwraca nową funkcję, która używa tego ciągu w swoim wywołaniu `console.log`.


Ten rodzaj wzorca jest bardzo potężny, ponieważ pozwala na pozostawienie "dziur" w funkcjach, które można później wypełnić potrzebnym zachowaniem.


### `map()`, `filter()`, `reduce()`


JavaScript oferuje kilka przydatnych wbudowanych metod do użycia z tablicami.


Metody te przyjmują funkcje jako argumenty, więc są również funkcjami wyższego rzędu.


`map()` przekształca każdy element tablicy w coś innego.


Przykład:


```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map(x => x * 2)

console.log(doubled) // [2, 4, 6]
```


Każda liczba jest podwajana, a wynikiem jest nowa tablica.


`filter()` usuwa elementy z tablicy, jeśli nie przejdą one testu.


Przykład:


```javascript
const numbers = [1, 2, 3, 4, 5]
const numbersGreaterThanTwo = numbers.filter(x => x > 2)

console.log(numbersGreaterThanTwo) // [3, 4, 5]
```


Zachowywane są tylko te wpisy tablicy, dla których warunek `x > 2` zwraca `true`.


funkcja `reduce()` jest używana do łączenia wszystkich elementów w tablicy w jedną wartość.


Przykład:


```javascript
const numbers = [1, 2, 3, 4]
const total = numbers.reduce((current, next) => current + next)

console.log(total) // 10
```


`reduce` przechodzi przez tablicę i, w tym przykładzie, stosuje operator `+` pomiędzy `1` i `2`, następnie pomiędzy wynikowym `3` i `3`, następnie pomiędzy wynikowym `6` i `4`, aż do uzyskania sumy wszystkich wpisów tablicy (która wynosi 10).


Możesz użyć funkcji `reduce()` do wielu rzeczy, takich jak sumy, średnie lub budowanie nowych wartości krok po kroku.


Metody te (`map`, `filter`, `reduce`) są potężnymi narzędziami do przetwarzania danych bez pisania ręcznych pętli.


Można je nawet łączyć w łańcuch operacji, jak poniżej:


```javascript
const numbers = [1, 2, 3, 4, 5]

const result = numbers
.map(n => n * 2)        // Double each entry, obtain [2, 4, 6, 8, 10]
.filter(n => n > 3) // Keep only the entries bigger than 3, so you get [4, 6, 8, 10]
.reduce((n1, n2) => n1 + n2) // Adds them: 4 + 6 + 8 + 10 = 28

console.log(result) // 28
```


## Praca z obiektami

<chapterId>7842aada-f009-5518-b8e3-1104e166a035</chapterId>


W tym rozdziale poznamy kilka potężnych i nieco bardziej zaawansowanych narzędzi do pracy z obiektami w JavaScript.


### Nieruchomości prywatne


Czasami chcemy ukryć właściwość obiektu, aby nie można było jej zmienić ani uzyskać do niej dostępu spoza obiektu. JavaScript daje nam możliwość zrobienia tego za pomocą `#` przed nazwą właściwości. Tworzy to **prywatną** właściwość, która jest dostępna tylko z wnętrza klasy.


```javascript
class Person {
#age // this is a private property

constructor(name, age) {
this.name = name
this.#age = age
}

getAge() {
return this.#age
}
}

const alice = new Person("Alice", 30)
console.log(alice.name)      // Alice
console.log(alice.getAge())  // 30, the method can access the private property
console.log(alice.#age)      // ❌ Error! You can't access private properties directly
```


Właściwości prywatne są przydatne, gdy chcemy zapobiec przypadkowym zmianom.


### właściwości statyczne


Czasami chcesz, aby właściwość należała do samej klasy, a nie do każdego obiektu utworzonego z tej klasy. Do tego właśnie służy `static`. Właściwość `static` jest zawarta w klasie i wszystkie obiekty tej klasy będą się do niej odwoływać.


```javascript
class User {
static counter = 0 // this belongs to the class, not to instances. The same counter will be shared by all objects

constructor() {
User.counter++ // changes the static property every time an object of this class gets initiated
}
}

const a = new User() // the constructor will change the shared counter from 0 to 1
const b = new User() // the constructor will change the shared counter from 1 to 2

console.log(User.counter) //  prints 2
```


Jest to przydatne do przechowywania współdzielonych danych i metod, które dotyczą całej grupy obiektów, a nie tylko jednego.


### `get` i `set`


W JavaScript, `get` i `set` pozwalają na tworzenie właściwości, które *wyglądają* jak zwykłe zmienne, ale w rzeczywistości uruchamiają specjalny kod w tle.


Metoda `get` jest uruchamiana, gdy próbujesz *odczytać* właściwość. Jest ona deklarowana poprzez napisanie `get` przed metodą z nazwą właściwości.


```javascript
class User {
constructor(firstName, lastName) {
this.firstName = firstName
this.lastName = lastName
}

get fullName() {
return `${this.firstName} ${this.lastName}`
}
}

const user = new User("Jane", "Doe")
console.log(user.fullName) // Jane Doe
```


Mimo że `fullName` nie jest zwykłą właściwością, możemy jej używać jak zwykłej właściwości, a za kulisami uruchamia funkcję `get`, aby utworzyć pełną nazwę.


Metoda `set` uruchamia się, gdy *przypisujesz* wartość do właściwości. Pozwala ona kontrolować, co się stanie, gdy ktoś spróbuje zmienić tę wartość. Jest ona deklarowana poprzez napisanie `set` przed metodą z nazwą właściwości.


```javascript
class User {
constructor() {
this.firstName = "John"
this.lastName = "Doe"
}

get fullName() {
return `${this.firstName} ${this.lastName}`
}

set fullName(input) {            // gets the name that is passed
const parts = input.split(" ") // breaks it into parts
this.firstName = parts[0]      // uses the first part as first name
this.lastName = parts[1]       // uses the second part as last name
}
}

const user = new User()
user.fullName = "John Smith"

console.log(user.firstName) // John
console.log(user.lastName)  // Smith
```


Kiedy robimy `user.fullName = "John Smith"`, uruchamia to metodę `set` i aktualizuje wartości `firstName` i `lastName`.


Więc nawet jeśli wydaje się, że po prostu ustawiamy prostą zmienną, w rzeczywistości uruchamiamy logikę, która aktualizuje inne właściwości.


## Klucze i wartości

<chapterId>01a397b8-c12a-5c39-82b3-6d9ebbb72a29</chapterId>


Każda właściwość w obiekcie JavaScript ma **klucz** (zwany również nazwą właściwości) i **wartość**.


Na przykład:


```javascript
const user = {
name: "Alice",
age: 30
}
```


W tym obiekcie `"name"` i `"age"` są kluczami, a "Alice" i `30` są ich wartościami.


### Dynamiczny dostęp


Czasami nie znasz nazwy właściwości z wyprzedzeniem... może pobierasz ją z danych wejściowych użytkownika lub odczytujesz ze zmiennej. Nadal możesz uzyskać do niej dostęp używając **notacji nawiasowej**, jak `myObject["keyName"]`.


```javascript
const user = {
name: "Alice",
age: 30
}

console.log(user["name"]) // Alice
```


Przekazaliśmy ciąg `name` do obiektu, aby uzyskać odpowiednią wartość.


Możemy zapisać klucz w zmiennej i użyć go, aby uzyskać dostęp do odpowiedniej wartości później, np


```javascript
const user = {
name: "Alice",
age: 30
}

const key = "name"

console.log(user[key]) // Alice
```


### Dynamiczny Assignment


Można również tworzyć lub aktualizować właściwości obiektów przy użyciu zmiennych jako kluczy.


```javascript
const settings = {}

const key = "theme"
settings[key] = "dark"

console.log(settings) // { theme: "dark" }
```


Jest to przydatne, gdy chcesz zbudować obiekt krok po kroku. Na przykład:


```javascript
const user = {}

user["username"] = "bananaFan123"
user["email"] = "banana@fruit.com"

console.log(user)
// { username: "bananaFan123", email: "banana@fruit.com" }
```


Można nawet użyć klucza dynamicznego *podczas tworzenia* obiektu za pomocą nawiasów kwadratowych:


```javascript
const key = "language"
const config = {
[key]: "JavaScript"
}

console.log(config.language) // JavaScript
```


Nazywa się to **właściwością obliczaną**. Wartość wewnątrz nawiasów kwadratowych jest obliczana, a wynik jest używany jako klucz.


### typ `Symbol


Oprócz ciągów znaków, JavaScript pozwala również na użycie specjalnego typu o nazwie `Symbol` jako klucza obiektu.


Zacznijmy od prostego przykładu:


```javascript
const id = Symbol("userID")

const user = {
name: "Bob",
[id]: 12345
}

console.log(user[id]) // 12345
```


W tym przykładzie `id` jest symbolem. Nie jest to ciąg znaków, ale nadal działa jako klucz. Jeśli spróbujesz zalogować `user` do konsoli, zobaczysz to:


```javascript
console.log(user) // { name: 'Bob', [Symbol(userID)]: 12345 }
```


Kolejna ważna rzecz: każdy tworzony symbol jest unikalny, nawet jeśli są one tworzone przy użyciu tego samego ciągu znaków.


```javascript
const a = Symbol("label")
const b = Symbol("label")

console.log(a === b) // false
```


Symbole pozwalają definiować klucze, które nie będą kolidować ze zwykłymi kluczami. Na przykład, powiedzmy, że masz obiekt z właściwością `name`, ale obiekt będzie dostosowywany przez użytkownika w przyszłości, w sposób, którego nie możesz przewidzieć, a ten użytkownik może również dodać właściwość `name`. Jeśli oryginalna właściwość `name` została zdefiniowana jako ciąg znaków, zostanie ona nadpisana przez nową, tak jak poniżej:


```javascript
const obj = {
name: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy' }
```


Jeśli zamiast tego użyjemy Symbolu:


```javascript
const name = Symbol("name")

const obj = {
[name]: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy', [Symbol(name)]: 'John' }
```


Jak widać, oryginalna właściwość `name` zostaje w ten sposób zachowana. Może to być przydatne w niektórych przypadkach.


## Obiekty użytkowe

<chapterId>516e74c8-2a11-545a-a4d1-c2cabb91a273</chapterId>


JavaScript daje nam kilka przydatnych wbudowanych obiektów, które pomagają nam w debugowaniu i operacjach matematycznych.


### Inne metody `console


Widziałeś już `console.log`, który wypisuje wartości na ekran.


Istnieje kilka innych przydatnych metod dostępnych w obiekcie `console`, które mogą pomóc w debugowaniu programów.


#### `console.warn`


Drukuje komunikat w kolorze żółtym (lub z ikoną ostrzeżenia w niektórych środowiskach):


```javascript
console.warn("This is just a warning.")
```


#### `console.error`


Drukuje komunikat w kolorze czerwonym, jak błąd:


```javascript
console.error("Something went wrong!")
```


#### `console.table`


Wyświetla tablicę lub obiekt jako tabelę:


```javascript
const users = [
{ name: "Alice", age: 25 },
{ name: "Bob", age: 30 }
]

console.table(users)
```


Spowoduje to wydrukowanie tabeli takiej jak


```
┌─────────┬────────┬─────┐
│ (index) │  name  │ age │
├─────────┼────────┼─────┤
│    0    │ 'Alice'│  25 │
│    1    │ 'Bob'  │  30 │
└─────────┴────────┴─────┘
```


Może to być przydatne do wizualizacji danych strukturalnych.


#### `console.time` i `console.timeEnd`


Można zmierzyć, jak długo coś trwa:


```javascript
console.time("timer")
for (let i = 0; i < 1000000; i++) {}
console.timeEnd("timer")
```


To drukuje coś takiego:


```
timer: 2.379ms
```


Przydatne do prostych testów wydajności.


### Obiekt `Math


JavaScript udostępnia obiekt `Math` z przydatnymi metodami do wykonywania obliczeń.


#### `Math.random()`


Zwraca liczbę losową z przedziału od 0 (włącznie) do 1 (włącznie):


```javascript
const r = Math.random()
console.log(r)
```


Przykładowe dane wyjściowe:


```
0.4387429859
```


#### `Math.floor()` i `Math.ceil()`



- `Math.floor(n)` zaokrągla **w dół** do najbliższej liczby całkowitej
- `Math.ceil(n)` zaokrągla **w górę** do najbliższej liczby całkowitej


```javascript
console.log(Math.floor(4.9)) // 4
console.log(Math.ceil(4.1))  // 5
```


#### `Math.round()`


Zaokrągla do najbliższej liczby całkowitej:


```javascript
console.log(Math.round(4.4)) // 4
console.log(Math.round(4.6)) // 5
```


#### `Math.max()` i `Math.min()`


Zwraca największą lub najmniejszą wartość z listy liczb:


```javascript
console.log(Math.max(5, 9, 3)) // 9
console.log(Math.min(5, 9, 3)) // 3
```


#### `Math.pow()` i `Math.sqrt()`



- `Math.pow(a, b)` daje `a` do potęgi `b`
- `Math.sqrt(n)` daje pierwiastek kwadratowy z `n`


```javascript
console.log(Math.pow(2, 3))   // 8
console.log(Math.sqrt(16))    // 4
```


# Zaawansowany JavaScript

<partId>72c30671-ca20-5617-92a5-d5ba7aa38c93</partId>


## Inne kolekcje

<chapterId>a9a70c6d-a343-5a46-a383-e288bc2700e3</chapterId>


JavaScript daje nam kilka specjalnych typów kolekcji, które wykraczają poza zwykłe tablice i obiekty. Należą do nich `Map` i `Set`.


Pomagają one przechowywać grupy wartości i zarządzać nimi, ale działają inaczej niż dotychczas.


`Map` jest zbiorem par **klucz-wartość**, tak jak obiekt. Ma jednak kilka ważnych różnic:



- Kluczami mogą być **dowolne wartości**, nie tylko ciągi znaków.
- Kolejność elementów zostanie zachowana.
- Posiada wbudowane metody ułatwiające pracę z nim.


Tworzysz nową mapę w ten sposób:


```javascript
const myMap = new Map()
```


Spowoduje to utworzenie pustej mapy. Aby dodać do niej wpisy, użyj `myMap.set(key, value)`:


```javascript
myMap.set("name", "Alice")
```


Dodaje to klucz `"name"` z wartością `"Alice"`.


Można również użyć numeru jako klucza:


```javascript
myMap.set(42, "The answer")
```


A nawet obiekt jako klucz:


```javascript
const objKey = { id: 1 }
myMap.set(objKey, "Object as key")
```


Nie działałoby to w przypadku zwykłych obiektów, które zezwalają tylko na klucze łańcuchowe.


Aby **uzyskać wartość**, użyj `myMap.get(key)`:


```javascript
console.log(myMap.get("name"))     // Alice
console.log(myMap.get(42))         // The answer
console.log(myMap.get(objKey))     // Object as key
```


Aby **sprawdzić czy klucz istnieje**, użyj `myMap.has(key)`:


```javascript
console.log(myMap.has("name")) // true
```


Aby **usunąć klucz**, użyj `myMap.delete(key)`:


```javascript
myMap.delete("name")
```


Aby **wyczyścić całą mapę**, użyj `myMap.clear()`:


```javascript
myMap.clear()
```


Mapy świetnie nadają się do zarządzania dużymi kolekcjami wartości, ponieważ dostęp do wartości na dużej mapie zapewnia zwykle znacznie lepszą wydajność niż na dużym obiekcie.


### `Set`


"Set" jest zbiorem **tylko wartości** (bez kluczy), gdzie każda wartość musi być **unikalna**. Oznacza to, że:



- Nie można mieć tej samej wartości dwa razy
- Wartości są zapisywane w kolejności ich dodawania


Tworzysz taki zestaw:


```javascript
const mySet = new Set()
```


Aby **dodać wartości**, użyj `mySet.add(value)`:


```javascript
mySet.add(1)
mySet.add(2)
mySet.add(2) // duplicate, will be ignored
```


Nawet jeśli próbowaliśmy dodać `2` dwa razy, zestaw zachowa tylko jedną kopię.


Aby **sprawdzić czy wartość jest w zestawie**, użyj `mySet.has(value)`:


```javascript
console.log(mySet.has(2)) // true
console.log(mySet.has(3)) // false
```


Aby **usunąć wartość**, użyj `mySet.delete(value)`:


```javascript
mySet.delete(2)
```


Aby **wyczyścić wszystko**, użyj `mySet.clear()`:


```javascript
mySet.clear()
```


Zestaw `Set` jest przydatny, gdy chcemy zachować kolekcję unikalnych wartości bez konieczności ręcznego sprawdzania duplikatów:


```javascript
const numberArray = [1, 2, 2, 3, 4, 4, 4, 5]

const numberSet = new Set(numberArray)

console.log(numberSet) // Set(5) { 1, 2, 3, 4, 5 }
```


Funkcja `Set` pozwala uniknąć duplikatów.


## Iteratory

<chapterId>61d24e5e-b7e4-541a-8322-778f61f26a72</chapterId>


Większość rzeczy w JavaScript, nad którymi można wykonywać pętle (jak tablice, łańcuchy, mapy, zbiory) są **iterowalne**: mogą dostarczać iteratory dla swojej zawartości.


**iterator** jest specjalnym obiektem w JavaScript, który pomaga przechodzić przez listę elementów **jeden po drugim**.


### iteratory `Object


W przeciwieństwie do tablic lub map, zwykłe obiekty **nie są iterowalne** za pomocą `for...of`. Jeśli spróbujesz tego:


```javascript
const user = {
name: "Alice",
age: 30
}

for (const value of user) {
console.log(value)
}
```


Pojawi się błąd:


```
TypeError: user is not iterable
```


Dzieje się tak, ponieważ zwykłe obiekty nie mają wbudowanego iteratora. JavaScript oferuje jednak inne narzędzia do tworzenia pętli.


#### `Object.keys()`


Możesz użyć `Object.keys(obj)`, aby uzyskać tablicę **kluczy** obiektu, a następnie zapętlić ją:


```javascript
const user = {
name: "Alice",
age: 30
}

const keys = Object.keys(user)

for (const key of keys) {
console.log(key)
}
```


Ten wydruk:


```
name
age
```


#### `Object.values()`


Aby zapętlić **wartości**, użyj `Object.values()`:


```javascript
const user = {
name: "Alice",
age: 30
}

const values = Object.values(user)

for (const value of values) {
console.log(value)
}
```


Ten wydruk:


```
Alice
30
```


#### `Object.entries()`


Jeśli chcesz **zarówno klucz jak i wartość**, użyj `Object.entries()`:


```javascript
const user = {
name: "Alice",
age: 30
}

const entries = Object.entries(user)

for (const [key, value] of entries) {
console.log(`${key} is ${value}`)
}
```


Ten wydruk:


```
name is Alice
age is 30
```


Nawet jeśli obiekty nie są bezpośrednio iterowalne, metody te dają ci pełny dostęp do ich zawartości w sposób, który działa dobrze z `for...of`.


Ale jak działają iteratory?


### `Symbol.iterator`


Sekretem wszystkich iteratorów jest specjalny **symbol** o nazwie `Symbol.iterator`.


Ten symbol jest wbudowanym kluczem, który mówi JavaScript: "Ten obiekt może być iterowany"


Kiedy wywołujesz `myIterable[Symbol.iterator]()`, JavaScript zwraca ci **obiekt iteratora** z metodą `.next()`.


Zobaczmy, jak to wygląda:


```javascript
const colors = ["red", "green", "blue"]

const iterator = colors[Symbol.iterator]()

console.log(iterator.next()) // { value: 'red', done: false }
```


Każde wywołanie `.next()` daje następną wartość. Kiedy skończy, zwraca ją:


```javascript
{ value: undefined, done: true }
```


### `next()`


Metoda `.next()` jest używana do pobrania następnego elementu z sekwencji.


Za każdym razem, gdy wywołasz `.next()`, otrzymasz obiekt z dwoma kluczami:



- `value`: bieżąca pozycja
- `done`: wartość logiczna informująca o zakończeniu iteracji


Zróbmy pełny przykład:


```javascript
const names = ["Lina", "Tom", "Eva"]      // declare an array
const iterator = names[Symbol.iterator]() // use the Symbol.iterator function to get an iterator for this array

let result = iterator.next()              // get the first element of the array

while (!result.done) {                    // repeat this loop until you reach the last element of the array, which is marked with { done: true }
console.log(result.value)               // print the value of each element
result = iterator.next()                // get the next element of the array
}
```


Ten wydruk:


```
Lina
Tom
Eva
```


Oto jak pętla `for...of` działa pod maską: używa tego wzorca z `.next()`.


Ten sam wynik uzyskasz używając


```javascript
const names = ["Lina", "Tom", "Eva"]

for (const result of names) {
console.log(result)
}
```


### Tworzenie klasy iterowalnej


Można również zdefiniować własną klasę **iterable** poprzez dodanie metody `[Symbol.iterator]()`.


Powiedzmy, że chcemy mieć klasę reprezentującą **zakres liczb**, na przykład od 1 do 5.


```javascript
class Range {
constructor(start, end) {
this.start = start
this.end = end
}

[Symbol.iterator]() {
let current = this.start
const end = this.end

return {
next() {
if (current <= end) {
const result = { value: current, done: false }
current = current + 1
return result
} else {
return { done: true }
}
}
}
}
}

const myRange = new Range(1, 5)

for (const num of myRange) {
console.log(num)
}
```


Ten wydruk:


```
1
2
3
4
5
```


Oto, co się dzieje:



- Zdefiniowaliśmy klasę `Range`
- Wewnątrz klasy zaimplementowaliśmy `[Symbol.iterator]()`, więc JavaScript wie, jak ją iterować
- Metoda `next()` zwraca każdą liczbę po kolei
- Po osiągnięciu `end`, zwraca `{ done: true }`


Teraz nasza klasa `Range` działa jak tablica i możemy jej używać w każdej pętli, która oczekuje iterowalnej tablicy.


### Funkcje generatora i `yield`


Aby ułatwić tworzenie iteratorów, JavaScript udostępnia **funkcje generujące**, używając słowa kluczowego `function*` (to `function` z `*` na końcu) i słowa kluczowego `yield`.


Spróbujmy:


```javascript
function* numberGenerator() {
yield 1
yield 2
yield 3
}

const iterator = numberGenerator()

console.log(iterator.next()) // { value: 1, done: false }
console.log(iterator.next()) // { value: 2, done: false }
console.log(iterator.next()) // { value: 3, done: false }
console.log(iterator.next()) // { value: undefined, done: true }
```


Każdy `yield` zwraca wartość i **wstrzymuje** funkcję aż do następnego wywołania `.next()`.


Można również zapętlić generator za pomocą `for...of`:


```javascript
for (const num of numberGenerator()) {
console.log(num)
}
```


Ten wydruk:


```
1
2
3
```


## Współbieżność z wywołaniami zwrotnymi

<chapterId>f3fc76ca-b3ef-54eb-a06e-501007002054</chapterId>


Do tej pory nasz kod był **synchroniczny**: uruchamiał jedną linię na raz, w kolejności. Ale niektóre rzeczy w prawdziwym świecie wymagają czasu i nie chcemy, aby cały program zatrzymywał się w oczekiwaniu.


W tym rozdziale wprowadzimy nową koncepcję: **walutę**. Pozwala nam ona manipulować kolejnością wykonywania zadań. Jest to przydatne, gdy mamy do czynienia z takimi rzeczami jak timery, dane wejściowe użytkownika lub odczytywanie plików z dysku. JavaScript oferuje różne narzędzia do wykonywania współbieżności.


### `setTimeout`


Funkcja `setTimeout` pozwala **uruchomić funkcję później**, po upływie pewnego czasu.


Przykład:


```javascript
console.log("Start")

setTimeout(
() => console.log("This runs after 2 seconds"),
2000
)

console.log("End")
```


Ten wydruk:


```
Start
End
This runs after 2 seconds
```


Mimo że `setTimeout` pojawia się w środku kodu, nie blokuje reszty. Zamiast tego planuje uruchomienie funkcji **później** i natychmiast przechodzi dalej.


Wartość `2000` oznacza 2000 milisekund (czyli 2 sekundy).

Oto bardziej szczegółowe i przyjazne dla początkujących przepisanie sekcji **Callbacks** i **Promise**, wykorzystujące manipulację danymi i przejrzyste adnotacje:


### Wywołania zwrotne


**Callback** to po prostu funkcja, którą przekazujemy innej funkcji, aby mogła zostać **wywołana później**.


Spójrzmy na rzeczywisty przykład wykorzystujący liczby. Wyobraźmy sobie, że mamy listę liczb i chcemy podwoić każdą z nich, a następnie zastosować funkcję (wywołanie zwrotne) do wynikowej "podwojonej" tablicy, ale chcemy to zrobić z niewielkim opóźnieniem, tak jakbyśmy czekali na coś powolnego (np. ładowanie danych z Internetu).


Oto funkcja, która robi to przy użyciu **callback**:


```javascript
function doubleNumbers(numbersArray, callback) {
// Pretend we're doing a slow operation using setTimeout
setTimeout(() => {
// Use the map method to create a new array where each number is doubled
const doubled = numbersArray.map(n => n * 2)

// When we're done, we call the callback function with the result
callback(doubled)
}, 1000) // Wait 1 second before running the code inside
}
```


Spróbujmy użyć tej funkcji:


```javascript
const input = [1, 2, 3]

doubleNumbers(input, function(result) {
console.log("Here is the doubled array:", result)
})
```


Po 1 sekundzie zostanie to wydrukowane:


```
Here is the doubled array: [ 2, 4, 6 ]
```


**Co tu się dzieje?


1. Przekazujemy `input` jako listę liczb, które chcemy podwoić.

2. Przekazujemy również **funkcję zwrotną**, która mówi programowi, co ma zrobić *po* podwojeniu.

3. Wewnątrz `doubleNumbers` symulujemy opóźnienie używając `setTimeout`, a następnie wykonujemy podwojenie.

4. Gdy to zrobimy, wywołujemy wywołanie zwrotne na wynikowej "podwojonej" tablicy.


Ta technika działa, ale wyobraź sobie, że chcesz wykonać **więcej kroków** po tym, na przykład odfiltrować małe liczby, a następnie je zsumować. Musiałbyś zagnieździć** więcej takich wywołań zwrotnych:


```javascript
doubleNumbers(input, function(doubled) {
filterBigNumbers(doubled, function(filtered) {
sumNumbers(filtered, function(total) {
console.log("Final result:", total)
})
})
})
```


Jest to Hard do czytania i bałagan. Ten styl nazywany jest **callback hell** i jest dokładnie tym, do czego `Promise` został stworzony.


## Współbieżność z obietnicami

<chapterId>30fddaca-729f-5c8d-bf86-8dfc7b3c9800</chapterId>


Obietnica to wbudowany obiekt JavaScript, który reprezentuje wartość, która będzie **gotowa w przyszłości**.


Możemy utworzyć obietnicę w ten sposób:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve("It worked!") // This means everything went OK
})
```


Część `new Promise()` tworzy obietnicę.


Wewnątrz niego podajemy funkcję z dwoma parametrami:



- `resolve`, to funkcja, którą wywołujemy, gdy wszystko się powiedzie
- `reject`, to funkcja, którą wywołujemy, gdy coś pójdzie nie tak


W powyższym przykładzie po prostu rozwiązujemy go natychmiast z komunikatem `"Udało się!"`.


### `.then()`


Aby zrobić coś **po** wykonaniu obietnicy, używamy `.then()`:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve(100) // This means everything went OK
})

promise.then(result => {
console.log("The result is:", result)
})
```


Ten wydruk:


```
The result is: 100
```


Wartość, którą przekazaliśmy do `resolve()` zostanie wysłana do funkcji wewnątrz `.then()` jako `result`.


Zasymulujmy zadanie trwające 2 sekundy przy użyciu `setTimeout`:


```javascript
const delayedPromise = new Promise(
(resolve, reject) => {
setTimeout(
() => resolve("Done waiting!"),
2000
)
})

delayedPromise.then(result => console.log(result))
```


Spowoduje to odczekanie 2 sekund, a następnie wydruk:


```
Done waiting!
```


### `reject()`


Stwórzmy obietnicę, która **nie powiedzie się**:


```javascript
const failingPromise = new Promise((resolve, reject) => {
reject("Something went wrong")
})
```


Teraz, jeśli użyjemy `.then()` na tym, nic się nie stanie, ponieważ `.then()` obsługuje tylko sukces.


Do obsługi błędów używamy `.catch()`:


```javascript
const failingPromise = new Promise((resolve, reject) => {
reject("Something went wrong")
})

failingPromise
.then(
result => console.log("This will NOT run:", result)
)
.catch(
error => console.log("Caught an error:", error)
)
```


To drukuje tylko


```
Caught an error: Something went wrong
```


Wartość przekazana do `reject()` jest wysyłana do funkcji `.catch()`.


Zbudujmy Obietnicę, która **czasami działa, a czasami zawodzi**, w oparciu o pewien warunek.


```javascript
function checkNumber(n) {
return new Promise((resolve, reject) => {
if (n > 0) {
resolve("Positive number")
} else {
reject("Not a positive number")
}
})
}
```


Teraz możemy to wywołać i obsłużyć oba przypadki:


```javascript
checkNumber(5)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Ten wydruk:


```
Success: Positive number
```


A jeśli spróbujemy z innym numerem:


```javascript
checkNumber(-1)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Drukuje:


```
Failure: Not a positive number
```


### Operacje łańcuchowe przy użyciu `Promise`



Możemy przepisać nasz wcześniejszy przykład używając `Promise` i będzie on wyglądał znacznie czyściej.


Zacznijmy od napisania nowej wersji naszej funkcji podwajającej, ale tym razem zwraca ona **obietnicę**:


```javascript
function doubleNumbers(numbers) {
return new Promise(resolve => {
// Wait 1 second before doing the operation
setTimeout(() => {
const doubled = numbers.map(n => n * 2)
resolve(doubled) // Return the result using resolve
}, 1000)
})
}
```


Teraz możemy użyć `.then()`, aby powiedzieć JavaScriptowi, co zrobić z wynikiem:


```javascript
function doubleNumbers(numbers) {
return new Promise(resolve => {
// Wait 1 second before doing the operation
setTimeout(() => {
const doubled = numbers.map(n => n * 2)
resolve(doubled) // Return the result using resolve
}, 1000)
})
}

const input = [1, 2, 3]

doubleNumbers(input)
.then(
result => console.log("Doubled numbers:", result)
)
```


Ten wydruk:


```
Doubled numbers: [ 2, 4, 6 ]
```


Jak dotąd działa to tak samo jak wersja z wywołaniem zwrotnym, ale teraz kod jest łatwiejszy do rozszerzenia i odczytania.


Powiedzmy, że chcemy dodać więcej kroków:


1. Najpierw należy podwoić wszystkie liczby

2. Następnie usuń liczby mniejsze niż 4

3. Na koniec dodaj je wszystkie razem


Możemy napisać jedną funkcję dla każdego kroku, wszystkie używając obietnic:


```javascript
function doubleNumbers(numbers) {
return new Promise(resolve => {
// Wait 1 second before doing the operation
setTimeout(() => {
const doubled = numbers.map(n => n * 2)
resolve(doubled) // Return the result using resolve
}, 1000)
})
}

function filterBigNumbers(numbers) {
return new Promise(resolve => {
setTimeout(() => {
const filtered = numbers.filter(n => n > 3)
resolve(filtered)
}, 1000)
})
}

function sumNumbers(numbers) {
return new Promise(resolve => {
setTimeout(() => {
const total = numbers.reduce((acc, n) => acc + n, 0)
resolve(total)
}, 1000)
})
}
```


Teraz możemy **połączyć** je ze sobą w następujący sposób:


```javascript
const input = [1, 2, 3]

doubleNumbers(input)
.then(filterBigNumbers)
.then(sumNumbers)
.then(
result => console.log("Final result after all steps:", result)
)
```


Ten wydruk:


```
Final result after all steps: 10
```


Przejdźmy przez to, co to robi:


1. `doubleNumbers` podwaja tablicę: `[2, 4, 6]`

2. `filterBigNumbers` usuwa wszystko ≤ 3: `[4, 6]`

3. `sumNumbers` dodaje pozostałe liczby: `4 + 6 = 10`

4. Na koniec drukujemy wynik.


Każde `.then()` czeka na zakończenie kroku poprzedzającego. Możemy więc zbudować **łańcuch działań** bez zagnieżdżania. Sprawia to, że kod jest bardziej czytelny i łatwiejszy do debugowania.


## Współbieżność z `async`/`await`

<chapterId>6e93d29f-c8bf-5fd1-a9c9-4e794ee6cbd0</chapterId>


Widzieliśmy, jak łańcuchy `Promise` pomagają nam uniknąć piekła wywołań zwrotnych, ale nadal mogą być trochę Hard do odczytania, gdy zaangażowanych jest wiele kroków.


To właśnie tam pojawiają się `async` i `await`. Pozwalają nam pisać asynchroniczny kod **który wygląda jak synchroniczny**, co czyni go łatwiejszym do zrozumienia.


### Czym jest `async`?


Po wpisaniu słowa kluczowego `async` przed funkcją, JavaScript automatycznie zawija wartość zwrotną funkcji w Obietnicę.


Zobaczmy podstawowy przykład:


```javascript
async function greet() {
return "hello"
}
```


Jeśli wywołasz tę funkcję:


```javascript
const result = greet()
console.log(result)
```


Zobaczysz to:


```
Promise { 'hello' }
```


Nawet jeśli właśnie zwróciłeś ciąg znaków, JavaScript zamienia go dla ciebie w obietnicę. Możesz uzyskać rzeczywistą wartość używając `.then()` w ten sposób:


```javascript
greet().then( result => console.log(result) ) // prints "hello"
```


Możesz też użyć `await`...


### Co to jest `await`?


Słowo kluczowe `await` mówi JavaScript: "poczekaj, aż ta Obietnica zostanie wykonana, a następnie podaj mi wynik"


Ale `await` można używać tylko **wewnątrz funkcji asynchronicznej**.


Przepiszmy przykład używając `await`:


```javascript
async function greet() {
return "hello"
}

async function greetAndLog() {
const result = await greet()
console.log(result)
}

greetAndLog() // prints "hello"
```


Teraz możemy użyć wyniku tak, jakby była to zwykła wartość.


Zróbmy teraz coś bardziej użytecznego.


### Symulowanie opóźnienia za pomocą `await`


Stworzymy prostą funkcję `wait`, która przyjmuje liczbę milisekund jako argument i po prostu rozwiązuje po tej liczbie milisekund, nie robiąc nic więcej:


```javascript
function wait(ms) {
return new Promise(resolve => {
setTimeout(resolve, ms)
})
}
```


Spróbujmy go użyć:


```javascript
async function test() {
console.log("waiting 2 seconds...")
await wait(2000)
console.log("done waiting")
}

test()
```


Ten wydruk:


```
waiting 2 seconds...
done waiting
```


Możesz myśleć o `await` jako "zatrzymaj się tutaj, aż obietnica zostanie wykonana, a następnie kontynuuj"


Pozwala to na pisanie kodu w sposób **od góry do dołu**, który zachowuje się asynchronicznie, bez łączenia wywołań `.then()`.


### Oczekiwanie na dane


Powtórzmy nasz poprzedni przykład, w którym podwajamy liczby, następnie filtrujemy, a następnie sumujemy. Ale tym razem użyjemy `async`/`await`.


Stworzymy 3 funkcje, które symulują oczekiwanie i zwracają obietnice:


```javascript
function doubleNumbers(numbers) {
return new Promise(resolve => {
setTimeout(() => {
const doubled = numbers.map(n => n * 2)
resolve(doubled)
}, 1000)
})
}

function filterBigNumbers(numbers) {
return new Promise(resolve => {
setTimeout(() => {
const filtered = numbers.filter(n => n > 3)
resolve(filtered)
}, 1000)
})
}

function sumNumbers(numbers) {
return new Promise(resolve => {
setTimeout(() => {
const total = numbers.reduce((acc, n) => acc + n, 0)
resolve(total)
}, 1000)
})
}
```


Teraz napiszmy funkcję `async`, aby je połączyć:


```javascript
async function process(numbers) {
const doubled = await doubleNumbers(numbers)
const filtered = await filterBigNumbers(doubled)
const total = await sumNumbers(filtered)

console.log("Final result:", total)
}

const input = [1, 2, 3]
process(input)
```


Ten wydruk:


```
Final result: 10
```


Jest to znacznie łatwiejsze do odczytania niż łańcuchowanie `.then()` lub zagnieżdżanie wywołań zwrotnych.


Wygląda jak zwykły program krok po kroku, ale nadal zachowuje się asynchronicznie.


## Iteratory asynchroniczne

<chapterId>438b037d-9931-56d7-9052-7b4470f3c75b</chapterId>


Nauczyłeś się już o **iteratorach** i o tym, jak możemy używać `for...of` do pętli po tablicach i innych iterowalnych rzeczach.


Ale co, jeśli dane, które chcemy iterować, wymagają czasu?


Czasami chcemy zapętlić rzeczy, które przychodzą **asynchronicznie**, takie jak wiadomości z czatu, wiersze z pliku lub liczby z powolnego źródła.


Aby to zrobić, JavaScript daje nam **asynchroniczne iteratory**.


### Funkcje generatora asynchronicznego


Najprostszym sposobem na utworzenie iteratora asynchronicznego jest użycie **funkcji generatora asynchronicznego**.


Piszemy to w ten sposób:


```javascript
async function* generateNumbers() {
yield 1
yield 2
yield 3
}
```


Wygląda to jak zwykły generator, ale z `async` przed nim.


Możemy teraz użyć `for await...of`, aby wykorzystać wartości:


```javascript
async function run() {
for await (const n of generateNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


Zostanie to wydrukowane:


```
Got number: 1
Got number: 2
Got number: 3
Done!
```


Jaka jest więc różnica w porównaniu z normalnym generatorem?


Różnica polega na tym, że możemy teraz użyć `await` wewnątrz generatora.


Ponownie utwórzmy pomocnika opóźnienia:


```javascript
function wait(ms) {
return new Promise(resolve => setTimeout(resolve, ms))
}
```


Teraz **powoli** podajmy liczby:


```javascript
async function* generateSlowNumbers() {
await wait(1000)
yield 1

await wait(1000)
yield 2

await wait(1000)
yield 3
}
```


Spróbuj go użyć:


```javascript
async function run() {
for await (const n of generateSlowNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


### Dlaczego warto używać iteratorów asynchronicznych?


Iteratory asynchroniczne są przydatne, gdy



- Nie wszystkie wartości pojawiają się jednocześnie.
- Chcesz radzić sobie z nimi pojedynczo, **w miarę ich pojawiania się**.
- Pracujesz z Promises i chcesz zapętlić w czysty sposób.


Na przykład, jeśli chcesz ładować wiadomości z serwera czatu jedna po drugiej lub pobrać duży plik w kawałkach, iteratory asynchroniczne dają ci sposób na napisanie pętli `for`, która działa z opóźnionymi danymi.


### `Symbol.asyncIterator`


Możemy również używać asynchronicznych iteratorów w niestandardowych klasach.


Oto przykład, który generuje liczby z opóźnieniem:


```javascript
function wait(ms) {
return new Promise(resolve => setTimeout(resolve, ms))
}

class DelayedNumbers {
constructor(numbers) {
this.numbers = numbers
}

async *[Symbol.asyncIterator]() {
for (const n of this.numbers) {
await wait(1000)
yield n
}
}
}
```


Możemy teraz używać `for await...of` tak jak wcześniej:


```javascript
async function run() {
const source = new DelayedNumbers([10, 20, 30])

for await (const n of source) {
console.log("Received:", n)
}

console.log("All done!")
}

run()
```


Pozwala to na tworzenie obiektów, które mogą być iterowane asynchronicznie


## Cukier składniowy Assignment

<chapterId>8b1ba7d8-ecfd-5470-b86e-73cb84ccc8b7</chapterId>


"Cukier składniowy" oznacza napisanie czegoś w krótszy lub łatwiejszy sposób, bez zmiany tego, co robi. To po prostu ładniejszy sposób na powiedzenie tego samego.


JavaScript ma wbudowany cukier składniowy, który pozwala nam pisać czystsze i krótsze deklaracje. W tym rozdziale przyjrzymy się, jak przypisywać wartości na podstawie warunku, aktualizować zmienne za pomocą matematyki, pobierać wartości z tablic lub obiektów oraz kopiować lub łączyć je za pomocą prostszej składni.


### Operator trójskładnikowy


W JavaScript można przypisać wartość na podstawie warunku przy użyciu **operatora alternatywnego**, który jest skróconym sposobem zapisu `if...else`.


Zamiast robić:


```javascript
let message

if (isMorning) {
message = "Good morning"
} else {
message = "Hello"
}
```


Możesz napisać:


```javascript
const message = isMorning ? "Good morning" : "Hello"
```


Oznacza to:



- Jeśli `isMorning` jest prawdziwe, użyj `"Good morning"`
- W przeciwnym razie należy użyć `"Hello"`


Ogólna forma jest następująca:


```javascript
condition ? valueIfTrue : valueIfFalse
```


Można go również używać wewnątrz innych wyrażeń:


```javascript
console.log(isSunny ? "Go outside" : "Stay in")
```


Upewnij się tylko, że używasz go do **prostych** decyzji. Jeśli logika jest złożona, trzymaj się `if...else`.


### Alternatywni operatorzy Assignment


JavaScript posiada **operatory skrótów** do wykonywania przypisań połączonych z operacjami.


Przyjrzyjmy się normalnemu sposobowi:


```javascript
let counter = 1
counter = counter + 1
```


Można to skrócić do:


```javascript
let counter = 1
counter += 1 // same as counter = counter + 1
```


Oto najpopularniejsze z nich:


| Operator | Meaning             |
| -------- | ------------------- |
| `+=`     | add and assign      |
| `-=`     | subtract and assign |
| `*=`     | multiply and assign |
| `/=`     | divide and assign   |

Przykłady:


```javascript
let score = 10
score += 5  // now score is 15
score *= 2  // now score is 30
score -= 10 // now score is 20
```


Są one przydatne, gdy chcesz zaktualizować zmienną przy użyciu jej własnej wartości.


### Destrukturyzacja


**Destrukturyzacja** pozwala łatwo pobierać wartości z tablic lub obiektów i przechowywać je w zmiennych.


#### Tablice


Załóżmy, że masz:


```javascript
const colors = ["red", "green", "blue"]
```


Zamiast robić:


```javascript
const first = colors[0]
const second = colors[1]
```


Możesz to zrobić:


```javascript
const [first, second] = colors
```


To przypisuje:



- `pierwszy` do `"czerwony"`
- `drugi` do `"Green"`


Możesz także pominąć wartości:


```javascript
const [,, third] = colors
console.log(third) // blue
```


#### Obiekty


Można również wyodrębniać wartości z obiektów:


```javascript
const user = { name: "Alice", age: 30 }

const { name, age } = user
console.log(name) // Alice
console.log(age)  // 30
```


Jeśli właściwość ma inną nazwę niż żądana zmienna, można zmienić jej nazwę:


```javascript
const { name: username } = user
console.log(username) // Alice
```


Destrukturyzacja sprawia, że kod jest bardziej przejrzysty podczas pracy z obiektami i tablicami.


### Składnia spreadu


Składnia **spread** używa `...` do rozpakowywania lub kopiowania wartości.


#### Tablice


Można kopiować lub łączyć tablice:


```javascript
const a = [1, 2]
const b = [3, 4]

const both = [...a, ...b]
console.log(both) // [1, 2, 3, 4]
```


Można również sklonować tablicę:


```javascript
const original = [10, 20, 30]
const clone = [...original]
```


#### Obiekty


To samo można zrobić z obiektami:


```javascript
const a = { x: 1 }
const b = { y: 2 }

const merged = { ...a, ...b }
console.log(merged) // { x: 1, y: 2 }
```


Można również zastąpić wartości:


```javascript
const user = { name: "Alice", age: 30 }
const updated = { ...user, age: 31 }

console.log(updated) // { name: "Alice", age: 31 }
```


Jest to bardzo przydatne podczas aktualizacji obiektów bez zmiany oryginału.


# NodeJS

<partId>42fe4d49-dace-5135-bb9e-b9d75034fb2a</partId>


## Jak dotarliśmy do Node

<chapterId>0da1d60c-06c9-54e6-a181-ae7dabf6e3b8</chapterId>


W tym rozdziale poznamy trochę historycznego kontekstu JavaScript i NodeJS.


Kontekst historyczny jest bardzo ważny w oprogramowaniu, ponieważ często korzystamy z narzędzi stworzonych przez innych ludzi, a zatem jesteśmy pod wpływem decyzji podjętych przez nich w przeszłości.


Zrozumienie powodów tych decyzji i tego, w jaki sposób narzędzia, których używamy, stały się takie, jakie są, pomoże nam poczuć się nieco mniej zdezorientowanym tym, co robimy.


### Początki JavaScript


JavaScript zaczynał jako prosty język zaprojektowany do tworzenia interaktywnych stron internetowych.


W latach 90. przeglądarki internetowe, takie jak Netscape Navigator, dodały JavaScript, aby programiści mogli pisać kod, który działa bezpośrednio w przeglądarce.


Pierwotny pomysł zakładał, że Java będzie podstawowym językiem do tworzenia stron internetowych (z tak zwanymi "apletami Java"), a JavaScript tylko do mniejszych rzeczy.


Główny projekt został wykonany przez Brendana Eicha, który w tym czasie był pracownikiem Netscape, w mniej niż 2 tygodnie.


Jednak większość ludzi wolała używać JavaScriptu niż Javy, a także aplety Javy miały pewne problemy z bezpieczeństwem w tamtym czasie, więc ostatecznie Java została porzucona jako opcja, a JavaScript stał się de facto standardem tworzenia stron internetowych.


### Silnik V8


JavaScript jest językiem interpretowanym, w przeciwieństwie do języków kompilowanych, takich jak C.


Kod napisany w skompilowanym języku jest przekształcany w plik binarny, a ten jest przesyłany bezpośrednio do procesora komputera.


![](assets/en/6.webp)


Z drugiej strony, języki interpred są zwykle bardziej przyjazne dla użytkownika i są bliższe temu, jak myślą ludzie ("wysokiego poziomu"), a nie temu, jak działają maszyny ("niskiego poziomu"); więc zwykle mają zbudowaną maszynę wirtualną do uruchamiania ich kodu.


Maszyna wirtualna to specjalny program, który znajduje się pomiędzy kodem napisanym przez użytkownika a procesorem i wykonuje kod użytkownika (ponieważ procesor nie może go zrozumieć).


Pozwala to programować bez zbytniej wiedzy o maszynie bazowej, ale wiąże się również z kosztami w zakresie wydajności, ponieważ komputer nie uruchamia tylko twojego programu; uruchamia program (maszynę wirtualną), który uruchamia twój program.


W miarę jak aplikacje internetowe stawały się coraz bardziej złożone, pojawiła się potrzeba poprawy wydajności JavaScript. Silnik V8 jest interpreterem, który obsługuje JavaScript w Google Chrome. Został on opracowany przez Google i wydany w 2008 roku.


Podczas gdy starsze silniki JavaScript były w większości tradycyjnymi maszynami wirtualnymi, silnik V8 jest kompilatorem JIT (just-in-time).


Kod JavaScript jest przesyłany do silnika V8, a silnik próbuje skompilować jego części jako natywne pliki binarne w locie. Pozwala to na korzystanie z języka wysokiego poziomu, z wydajnością nieco bliższą językom niskiego poziomu. Dzięki temu JavaScript stał się najszybszym językiem wysokiego poziomu na świecie, trochę na zasadzie "najlepszego z obu światów".


### Środowisko uruchomieniowe NodeJS


Choć był łatwy w użyciu i dość szybki w wykonaniu, po wydaniu V8 JavaScript nadal miał ogromne ograniczenie: mógł działać tylko w przeglądarce.


Dlaczego jest to problem?


Cóż, ponieważ przeglądarki wykonują kod pobrany z milionów różnych źródeł w Internecie, mogą łatwo stać się złośliwym oprogramowaniem, więc są "piaskownicą" od reszty systemu operacyjnego.


![](assets/en/7.webp)


JavaScript nie mógł uzyskać dostępu do systemu plików i innych lokalnych zasobów na komputerze (przynajmniej nie tak łatwo, jak inne języki), więc było to znaczące ograniczenie tego, jakie aplikacje można było za jego pomocą tworzyć.


W 2009 roku Ryan Dahl opublikował NodeJS, który jest środowiskiem wykonawczym umożliwiającym korzystanie z silnika V8 poza przeglądarką, bezpośrednio w natywnym systemie operacyjnym komputera. Dodaje również wiele funkcji przydatnych do pisania programów po stronie serwera i wiersza poleceń. Na przykład, można użyć NodeJS do utworzenia serwera WWW, odczytu i zapisu plików lub tworzenia narzędzi automatyzujących zadania.


![](assets/en/8.webp)


W tym kursie do tej pory zbadaliśmy funkcje JavaScript, które są obecne zarówno w przeglądarce, jak i w NodeJS. Funkcje te pozwoliły nam definiować dane i manipulować nimi w abstrakcyjny sposób. W następnych kilku lekcjach zbadamy funkcje, które są specyficzne dla NodeJS i pozwalają nam na interakcję z systemem operacyjnym.


## Argumenty wiersza poleceń

<chapterId>960d20f3-c424-5d51-a041-ef17d2e94b6d</chapterId>


NodeJS pozwala nam między innymi na tworzenie interfejsów wiersza poleceń (CLI).


W tym celu potrzebujemy sposobu na otrzymywanie argumentów wiersza poleceń, co w Node odbywa się za pomocą wbudowanego obiektu `process`.


### `process`


NodeJS udostępnia specjalny obiekt o nazwie `process`, który reprezentuje aktualnie uruchomiony program.


Można go użyć do sprawdzenia środowiska, bieżącego katalogu roboczego, a nawet wyjścia z programu w razie potrzeby.


Na przykład:


```javascript
console.log(process.platform)
```


Wyświetla platformę systemu operacyjnego, taką jak `win32`, `linux` lub `darwin` (Mac).


### `process.argv`


Kiedy uruchamiasz program NodeJS z terminala, możesz przekazać dodatkowe słowa (argumenty) po nazwie skryptu. Są one przechowywane w `process.argv`.


Na przykład, jeśli uruchomisz to polecenie:


```
node my_script.js alpha beta
```


Argumenty można wydrukować w następujący sposób:


```javascript
console.log(process.argv)
```


Wynik może wyglądać następująco:


```
[ '/path/to/node', '/path/to/my_script.js', 'alpha', 'beta' ]
```


Pierwsze dwa elementy to zawsze ścieżka węzła i ścieżka skryptu. Wszelkie dodatkowe słowa przekazane do skryptu znajdują się po nich.


Tablica `process.argv` może być pocięta jak każda inna tablica przy użyciu metody `.slice()`, więc aby uzyskać tylko argumenty, które zostały przekazane, można wykonać następujące czynności


```javascript
const args = process.argv.slice(2)

console.log(args)
```


Dostęp do argumentów przekazywanych przez użytkownika ma fundamentalne znaczenie dla tworzenia aplikacji wiersza poleceń.


## Moduły

<chapterId>4e1651a5-65fd-50bc-b22a-40313d5659ca</chapterId>


Systemy uruchomieniowe JavaScript, takie jak NodeJS, zwykle traktują każdy plik JavaScript jako oddzielny moduł.


Pomyśl o module jak o pudełku. Pudełko ma własną przestrzeń prywatną, więc zadeklarowane w nim zmienne i funkcje nie kolidują z kodem w innych pudełkach. Zasadniczo każdy moduł ma swój własny zakres.


Moduł może eksportować część swojej zawartości, udostępniając ją innym modułom, i może importować zawartość wyeksportowaną przez inne moduły. JavaScript pozwala eksportować i importować zawartość między modułami, aby łączyć różne pliki.


Program JavaScript często składa się z wielu modułów, które są ze sobą połączone.


Dlaczego warto używać modułów? Dzieląc kod na moduły, można zorganizować program w mniejsze, bardziej przejrzyste i nadające się do ponownego wykorzystania części. Każdy moduł może koncentrować się tylko na jednym typie zadania, takim jak obsługa obliczeń matematycznych, praca z plikami lub formatowanie tekstu.


### Moduły CommonJS


W NodeJS najpopularniejszym systemem do zarządzania modułami jest **CommonJS**.


W tym systemie można udostępniać (eksportować) kod z modułu za pomocą `module.exports` i ładować (importować) go do innego pliku za pomocą `require()`.


Aby udostępnić coś poza modułem, należy przypisać to do `module.exports`:


```javascript
const greeting = "Hello!"

module.exports = greeting
```


Tutaj, ciąg `"Hello!"` jest tym, co ten moduł eksportuje.


Aby użyć wyeksportowanego kodu z innego pliku, należy użyć funkcji `require()` ze ścieżką do tego pliku:


```javascript
const greeting = require("./greeting.js")

console.log(greeting)
```


Ten wydruk:


```
Hello!
```


Można eksportować wiele rzeczy, łącząc je w anonimowy obiekt, np


```javascript
const greeting1 = "hello"

const greeting2 = "hi"

module.exports = {
greeting1, greeting2
}
```


CommonJS był systemem modułów, który został początkowo przyjęty przez NodeJS. Później dodano również moduły ES.


### Moduły ES


NodeJS obsługuje również inny typ modułów o nazwie **ES Modules**, które są popularne w tworzeniu stron internetowych. Używają one słów kluczowych `export` i `import`.


Moduły ES zostały opracowane dla przeglądarki i dopiero później dodane do Node. Jeśli chcesz ich użyć, być może będziesz musiał użyć `.mjs` jako rozszerzenia pliku zamiast `.js`, w zależności od używanej wersji Node.


W jednym pliku o nazwie `greeting.mjs` piszemy


```javascript
export const greeting = "Hello!"
```

Jak widać, eksportujemy stałą bezpośrednio tam, gdzie jest zdefiniowana


Importujemy go do innego pliku o nazwie `index.mjs`:


```javascript
import { greeting } from "./greeting.mjs"

console.log(greeting)
```


Można eksportować różne deklaracje w różnych częściach pliku, np


```javascript
export const num = 10

export function double (x) {
return x*2
}
```


### Standardowa biblioteka NodeJS


NodeJS zawiera również wiele wbudowanych modułów. Są to gotowe moduły dostarczane przez NodeJS, które pomagają w typowych zadaniach, takich jak odczytywanie plików, praca z systemem operacyjnym lub łączenie się z siecią.


Na przykład, moduł `os` dostarcza informacji o systemie operacyjnym:


```javascript
const os = require("os")

console.log(os.platform())
```


Nie musisz instalować tych wbudowanych modułów, są one dostarczane z NodeJS. Tworzą one "standardową bibliotekę" środowiska uruchomieniowego i są używane przez większość aplikacji Node do takich rzeczy, jak czytanie plików lub komunikacja przez Internet.


Następne rozdziały pokażą kilka przydatnych przykładów ich użycia.


## Moduł `fs

<chapterId>911e953a-35ae-5ee7-bd74-372501c32e81</chapterId>


Moduł `fs` (skrót od **file system**) jest częścią standardowej biblioteki NodeJS. Umożliwia on pracę z plikami i katalogami na komputerze: można odczytywać pliki, zapisywać pliki, usuwać je, zmieniać ich nazwy i nie tylko.


Aby z niego skorzystać, należy najpierw zaimportować go w górnej części pliku:


```javascript
const fs = require("fs")
```


### Interfejs API synchronizacji


Najprostszym sposobem użycia `fs` jest użycie jego metod **sync**.


Metody te blokują program do momentu ich zakończenia (więc następna linia kodu nie zostanie uruchomiona, dopóki operacja nie zostanie zakończona).


Oto przykład synchronicznego odczytu pliku:


```javascript
const fs = require("fs")

const data = fs.readFileSync("example.txt", "utf8")

console.log(data)
```


Jeśli w tym samym katalogu co skrypt znajduje się plik o nazwie `example.txt`, spowoduje to wypisanie jego zawartości.


Można również zapisywać do pliku synchronicznie:


```javascript
const fs = require("fs")

fs.writeFileSync("output.txt", "Hello from Node!")

console.log("File written!")
```


Spowoduje to utworzenie (lub nadpisanie) pliku o nazwie `output.txt` tekstem.


Oto kilka typowych operacji, które można wykonać za pomocą tego interfejsu API:


```javascript
const fs = require("fs")

// List files and folders
const items = fs.readdirSync(".")
console.log("Items in current directory:", items)

// Create folder
fs.mkdirSync("my_folder")
console.log("Folder created")

// Delete folder
fs.rmdirSync("my_folder")
console.log("Folder deleted")

// Create & write file
fs.writeFileSync("my_file.txt", "Hello world")
console.log("File created & written")

// Read file
const content = fs.readFileSync("my_file.txt", "utf8")
console.log("File content:", content)

// Delete file
fs.unlinkSync("my_file.txt")
console.log("File deleted")
```


Interfejs API Sync jest prosty i dobry dla małych skryptów, ale ponieważ blokuje program, dopóki nie zostanie wykonany, może spowolnić pracę, jeśli pracujesz z dużymi plikami lub serwerem.


### Asynchroniczny interfejs API wywołania zwrotnego


Interfejs API **callback** jest nieblokujący: pozwala NodeJS wykonywać inne czynności podczas wykonywania operacji na pliku.


Zamiast zwracać wynik bezpośrednio, pobiera funkcję (**callback**), która jest wywoływana po zakończeniu operacji.


```javascript
const fs = require("fs")

fs.readFile("example.txt", "utf8", (err, data) => {
if (err) {
console.error("Error reading file:", err)
} else {
console.log(data)
}
})
```


Oto, co się dzieje:



- `fs.readFile` rozpoczyna czytanie pliku `example.txt`.
- NodeJS nie czeka, przechodzi do wykonywania innego kodu, który mogłeś napisać.
- Po zakończeniu odczytu pliku uruchamiane jest wywołanie zwrotne:



  - Jeśli wystąpił błąd, `err` zawiera błąd.
  - W przeciwnym razie `data` zawiera zawartość.


Oto sposób zapisu do pliku:


```javascript
const fs = require("fs")

fs.writeFile("output.txt", "Hello async!", (err) => {
if (err) {
console.error("Error writing file:", err)
} else {
console.log("File written!")
}
})
```


Ta sama idea: program nie zatrzymuje się podczas zapisywania pliku.


Kilka przykładów rzeczy, które można zrobić za pomocą tego interfejsu API:


```javascript
const fs = require("fs")

// List files and folders
fs.readdir(".", (err, items) => {
if (err) return console.error(err)
console.log("Items in current directory:", items)
})

// Create folder
fs.mkdir("my_folder", (err) => {
if (err) return console.error(err)
console.log("Folder created")
})

// Delete folder
fs.rmdir("my_folder", (err) => {
if (err) return console.error(err)
console.log("Folder deleted")
})

// Create & write file
fs.writeFile("my_file.txt", "Hello world", (err) => {
if (err) return console.error(err)
console.log("File created & written")
})

// Read file
fs.readFile("my_file.txt", "utf8", (err, content) => {
if (err) return console.error(err)
console.log("File content:", content)
})

// Delete file
fs.unlink("my_file.txt", (err) => {
if (err) return console.error(err)
console.log("File deleted")
})
```


Interfejs API wywołania zwrotnego jest lepszy dla serwerów i dużych zadań, ponieważ nie blokuje programu, ale zagnieżdżone wywołania zwrotne mogą powodować bałagan w przypadku łączenia wielu operacji w łańcuchy. Dlatego też dodano asynchroniczne API oparte na obietnicach.


### Obietnica asynchronicznego interfejsu API


API oparte na obietnicach jest nowoczesne i działa świetnie z `.then()` i `async/await`. Jest dostępne jako `fs.promises`.


Należy zaimportować właściwość `promises`:


```javascript
const fs = require("fs").promises
```


Używając `.then()`:


```javascript
const fs = require("fs").promises

fs.readFile("example.txt", "utf8")
.then(data => {
console.log(data)
})
.catch(err => {
console.error("Error reading file:", err)
})
```


Lub nawet lepiej, używając `async/await`:


```javascript
const fs = require("fs").promises

async function readFile(fileName) {
try {
const data = await fs.readFile(fileName, "utf8")
console.log(data)
} catch (err) {
console.error("Error reading file:", err)
}
}

readFile("example.txt")
```


Zapis do pliku:


```javascript
const fs = require("fs").promises

async function writeFile(fileName, content) {
try {
await fs.writeFile(fileName, content)
console.log("File written!")
} catch (err) {
console.error("Error writing file:", err)
}
}

writeFile("output.txt", "Hello from promises!")
```


Zwykła lista przykładów dla API:


```javascript
const fs = require("fs").promises

// Use an async function to await operations
async function main() {
// List files and folders
const items = await fs.readdir(".")
console.log("Items in current directory:", items)

// Create folder
await fs.mkdir("my_folder")
console.log("Folder created")

// Delete folder
await fs.rmdir("my_folder")
console.log("Folder deleted")

// Create & write file
await fs.writeFile("my_file.txt", "Hello world")
console.log("File created & written")

// Read file
const content = await fs.readFile("my_file.txt", "utf8")
console.log("File content:", content)

// Delete file
await fs.unlink("my_file.txt")
console.log("File deleted")
}

main().catch(err => console.error(err))
```



## NPM

<chapterId>a91d9a75-55cc-51a3-a48f-0c0be6fe6e72</chapterId>


Podczas pisania kodu często będziesz musiał korzystać z kodu napisanego przez inne osoby; na przykład z bibliotek pomagających w pracy z datami, kolorami, serwerami lub prawie wszystkim innym.


Zamiast pobierać i kopiować pliki ręcznie, można użyć **menedżera pakietów**.


Menedżer pakietów to narzędzie, które:



- pakiety do pobrania
- śledzi, których pakietów potrzebuje projekt
- upewnia się, że wszyscy w zespole mają te same wersje pakietów


### Co to jest NPM


W świecie NodeJS najpopularniejszym menedżerem pakietów jest **NPM**, co oznacza *Node Package Manager*.


NPM jest pobierany automatycznie podczas instalacji NodeJS.


Możesz sprawdzić, czy masz NPM, uruchamiając to w terminalu:


```
npm -v
```


To wypisuje posiadaną wersję NPM, np:


```
10.2.1
```


### Tworzenie pakietu


W NodeJS, **package** to po prostu katalog z plikiem `package.json`.


Stwórzmy jeden krok po kroku.


1. Utwórz nowy folder dla swojego projektu:


```
mkdir my_project
cd my_project
```


2. Uruchom to polecenie:


```
npm init
```


Uruchamia to interaktywną konfigurację, zadając pytania, takie jak nazwa projektu, wersja, opis itp.


Jeśli nie chcesz odpowiadać na wszystkie pytania i po prostu zaakceptować ustawienia domyślne, możesz użyć tej opcji:


```
npm init -y
```


Po jego uruchomieniu w folderze pojawi się nowy plik o nazwie:


```
package.json
```


### `package.json`


Plik `package.json` jest po prostu plikiem JSON, który przechowuje metadane o projekcie.


Oto przykład:


```json
{
"name": "my_project",
"version": "1.0.0",
"description": "",
"main": "index.js",
"scripts": {
"test": "echo \"Error: no test specified\" && exit 1"
},
"keywords": [],
"author": "",
"license": "ISC",
"type": "commonjs"
}

```


Kilka ważnych pól:



- `name`: nazwa pakietu
- `version`: bieżąca wersja
- `main`: plik punktu wejścia (jak `index.js`)
- `scripts`: polecenia, które można uruchomić (jak `npm start`)
- `dependencies`: wyświetla listę wszystkich pakietów, od których zależy projekt


### Instalowanie pakietu


Powiedzmy, że chcesz użyć pewnego pakietu o nazwie `picocolors`, aby dodać kolory do wyjścia terminala.


Można go zainstalować uruchamiając:


```
npm install picocolors
```


Możesz teraz użyć go w swoim projekcie. Utwórz plik `index.js` z rozszerzeniem


```javascript
const pico = require('picocolors')

console.log(
pico.green("This text is green!")
)
```


i spróbuj go uruchomić. Terminal powinien wydrukować kolorową wersję tekstu.


Co zrobił NPM?



- Pobrał on pakiet i zapisał go w podfolderze o nazwie `node_modules/`
- dodało wpis pod `dependencies` w twoim `package.json`
- zaktualizował plik `package-lock.json`


Co to jest `package-lock.json`?


### `package-lock.json`


Plik ten jest automatycznie tworzony przez NPM.


Można się zastanawiać, skoro mamy już `package.json`, po co nam kolejny plik?

Oto powód:



- `package.json` mówi tylko o **zakresie** wersji pakietu, którego potrzebuje projekt.

Przykład:


```json
"dependencies": {
"picocolors": "^1.1.0"
}
```


`^1.1.0` oznacza "dowolną wersję kompatybilną z 1.1.x", więc jest elastyczne.



- `package-lock.json` **zamraża** dokładne wersje każdego pojedynczego pakietu i ich pod-zależności, dzięki czemu każdy, kto instaluje twój projekt, otrzymuje dokładnie taką samą konfigurację roboczą.


Dlaczego jest to ważne?


Jeśli pracujesz w zespole, wdrażasz projekt na serwerze lub wracasz do niego w przyszłości, chcesz mieć pewność, że nadal będzie działał w ten sam sposób.

Jeśli pakiety zostały zaktualizowane i zainstalujesz je ponownie bez pliku blokady, możesz otrzymać nieco inną wersję, która zachowuje się inaczej.


Zachowując `package-lock.json` w projekcie, NPM zawsze zainstaluje dokładnie te wersje, które są tam wymienione, zapewniając, że każdy ma to samo środowisko.


`package-lock.json` blokuje wszystko do bardzo konkretnej wersji, aby projekt był bardziej odtwarzalny na innych maszynach.


Ale jeśli twój pakiet musi być używany przez wiele osób, możesz zamiast tego nie zatwierdzać go, aby NPM znajdował tylko plik `package.json` i mógł automatycznie instalować najnowsze wersje, które są dozwolone w tym pliku.


Ale są to rzeczy, o które powinieneś się martwić później, gdy zaczniesz publikować własny kod. Na razie wprowadziliśmy podstawy NPM tylko po to, abyś mógł znaleźć i używać bibliotek opublikowanych przez innych programistów w swoich projektach.



## Tworzenie sieci w NodeJS

<chapterId>f2cabd8b-754b-5c97-8d6a-8412a9a184c7</chapterId>


NodeJS jest często używany jako język zaplecza: możesz przekształcić swój skrypt w serwer, a także używać go do wysyłania żądań do innych serwerów.


W tym rozdziale przedstawimy kilka podstawowych funkcji sieciowych, które pozwolą ci to zrobić.


### `fetch()`


Jeśli chcesz, aby twój program pobierał dane ze strony internetowej lub API, musisz wykonać żądanie **HTTP**.


W nowoczesnych wersjach NodeJS można użyć wbudowanej funkcji `fetch()`.


Oto przykład żądania GET do interfejsu API:


```javascript
const response = await fetch("https://jsonplaceholder.typicode.com/posts/1")
const data = await response.text()

console.log(data)
```


Po uruchomieniu tej funkcji zobaczysz coś takiego:


```
{
"userId": 1,
"id": 1,
"title": "...",
"body": "..."
}
```


Oto, co się dzieje:


1. funkcja `fetch()` pobiera adres URL i wysyła żądanie.

2. Zwraca ona **Promise**, który zwraca obiekt `Response`.

3. `response.text()` odczytuje treść odpowiedzi jako ciąg znaków.


Ale zwracany ciąg znaków to w rzeczywistości JSON. Co to jest?


### JSON


Podczas pracy z internetowymi interfejsami API dane są często wysyłane i odbierane jako **JSON**, co oznacza JavaScript Object Notation.


JSON to po prostu format tekstowy, który wygląda bardzo podobnie do obiektów JavaScript. Na przykład:


```json
{
"name": "Alice",
"age": 30,
"likes": ["apples", "bananas"]
}
```


Obiekt `JSON` jest wbudowanym narzędziem w JavaScript, które może być używane do pracy z tym formatem danych.


Obiekt JavaScript można przekonwertować na ciąg JSON za pomocą funkcji `JSON.stringify()`:


```javascript
const user = { name: "Alice", age: 30 }

const jsonString = JSON.stringify(user)

console.log(jsonString)
```


Ten wydruk:


```
{"name":"Alice","age":30}
```


Możesz również przekonwertować tekst JSON z powrotem na obiekt JavaScript używając `JSON.parse()`:


```javascript
const jsonText = '{"name":"Bob","age":25}'

const obj = JSON.parse(jsonText)

console.log(obj)
```


Ten wydruk:


```
{ name: 'Bob', age: 25 }
```


Bądź ostrożny: `JSON.parse()` wyrzuci błąd, jeśli ciąg nie jest prawidłowym JSON.


```javascript
JSON.parse("not json") // ❌ Error!
```


Upewnij się więc, że ciąg znaków jest odpowiednio sformatowany.


### serwer `http


NodeJS umożliwia utworzenie serwera WWW bez instalowania czegokolwiek innego.


Możesz użyć wbudowanego modułu `http` do obsługi żądań od klientów i wysyłania odpowiedzi z powrotem.


Oto bardzo podstawowy przykład:


```javascript
const http = require("http")

const server = http.createServer((req, res) => {
res.statusCode = 200
res.end("Hello from NodeJS server!")
})

server.listen(3000, () => {
console.log("Server running at http://localhost:3000/")
})
```


Po uruchomieniu tego skryptu i otwarciu `http://localhost:3000` w przeglądarce, zobaczysz:


```
Hello from NodeJS server!
```


To właśnie dzieje się w kodzie:


1. Zaimportowałeś serwer `http` ze standardowej biblioteki Node.

2. funkcja `http.createServer()` tworzy serwer. Przekazałeś do `http.createServer()` wywołanie zwrotne `(req, res) => {...}`, które będzie wykonywane za każdym razem, gdy ktoś się połączy.

3. Do odpowiedzi został przypisany kod stanu 200 (oznaczający pomyślną operację). Możesz przeczytać o kodach statusu http [tutaj](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

3. `res.end()` wysyła odpowiedź i kończy połączenie.

4. `server.listen(3000)` uruchamia serwer na porcie 3000.


Można również sprawdzić `req.url` i `req.method` w żądaniu, aby obsłużyć różne ścieżki lub typy żądań.


Przykład z routingiem:


```javascript
const server = http.createServer((req, res) => {
if (req.url === "/") { // handle requests for the root of the website
res.statusCode = 200
res.end("Home page")
} else if (req.url === "/about") { // handle requests for the about page
res.statusCode = 200
res.end("About page")
} else {
res.statusCode = 404 // we send a 404 status code to signal that the requested page is missing
res.end("Not Found")
}
})
```


Są to bardzo podstawowe przykłady. W celu zbudowania bardziej zaawansowanych serwerów, większość deweloperów prawdopodobnie pobierze gotową bibliotekę backendową, taką jak [express](https://www.npmjs.com/package/express).


## Przetwarzanie danych: bufory, zdarzenia, strumienie

<chapterId>8c9623f0-a604-51a4-8fe4-871c849d3e3b</chapterId>


W tym rozdziale przedstawimy przede wszystkim trzy klasy obiektów:



- `Buffer`, który reprezentuje małe fragmenty danych binarnych
- `EventEmitter`, który może być użyty do śledzenia jakiegoś kroku przez proces asynchroniczny poprzez emitowanie sygnałów zwanych "zdarzeniami"
- `Stream`, który pozwala nam przetwarzać dużą porcję danych po jednym `Buforze` na raz i który śledzi proces poprzez emitowanie zdarzeń


Są one niezwykle powszechne w profesjonalnym kodzie NodeJS, więc nawet jeśli nie używasz ich w swoich pierwszych projektach, dobrze jest uzyskać podstawowe zrozumienie, kiedy będziesz musiał z nimi współdziałać. z nich


### Bufory


W NodeJS, **bufor** jest typem obiektu używanym do pracy z danymi binarnymi.


Bufor jest pojemnikiem o stałym rozmiarze na nieprzetworzone bajty.


Oto jak utworzyć bufor z ciągu znaków:


```javascript
const buf = Buffer.from("hello")
console.log(buf)
```


To drukuje coś takiego:


```
<Buffer 68 65 6c 6c 6f>
```


Te liczby (`68`, `65`, `6c`, itd.) są szesnastkowymi reprezentacjami liter w `"hello"`.


Możesz przekonwertować go z powrotem na ciąg znaków w następujący sposób:


```javascript
console.log(buf.toString())
```


Ten wydruk:


```
hello
```


Można również utworzyć bufor o określonym rozmiarze wypełniony zerami:


```javascript
const buf = Buffer.alloc(10)
console.log(buf)
```


To drukuje coś takiego:


```
<Buffer 00 00 00 00 00 00 00 00 00 00>
```


Można zapisywać dane do bufora:


```javascript
buf.write("abc")
console.log(buf)
```


Można też uzyskać dostęp do poszczególnych bajtów:


```javascript
console.log(buf[0]) // prints the ASCII number for 'a', which is 97
```


Bufory są szczególnie przydatne, gdy trzeba manipulować danymi na bardzo niskim poziomie.


### Wydarzenia


W JavaScript, **zdarzenie** to coś, co dzieje się w programie, na co można zareagować.


Na przykład:



- plik kończy ładowanie
- wyłącznik czasowy
- użytkownik kliknie przycisk
- żądanie sieciowe zwraca dane


Zdarzenie** jest po prostu sygnałem, że coś się wydarzyło i można napisać kod, który będzie nasłuchiwał tych zdarzeń i reagował na nie.


W NodeJS wiele obiektów może emitować zdarzenia. Obiekty te nazywane są **EventEmitters**.


Oto przykład:


```javascript
const EventEmitter = require("events")

const emitter = new EventEmitter()

// Listen for an event
emitter.on("greet", () => {
console.log("Hello! An event happened.") // this will get printed when a "greet" event gets fired
})

// Emit the event
emitter.emit("greet")
```


Ten wydruk:


```
Hello! An event happened.
```


Oto co:


1. Tworzymy obiekt `EventEmitter`.

2. Mówimy mu, aby uruchamiał wywołanie zwrotne za każdym razem, gdy wystąpi zdarzenie `"greet"`, używając `.on("greet")`.

3. Później wyzwalamy zdarzenie `"greet"` za pomocą `.emit()`.

4. Nasze wywołanie zwrotne zostanie wykonane


Wraz ze zdarzeniem można przekazać dane:


```javascript
emitter.on("greet",
(name) => console.log(`Hello, ${name}!`)
)

emitter.emit("greet", "Alice") // first argument is the type of event, second argument is the data we pass with this event
```


Ten wydruk:


```
Hello, Alice!
```


Można również rejestrować nasłuchiwaczy dla innych zdarzeń:


```javascript
emitter.on("goodbye", () => {
console.log("Goodbye!")
})

emitter.emit("goodbye")
```


Do danego typu zdarzenia można dołączyć dowolną liczbę nasłuchiwaczy, a z tego samego emitera można wywołać wiele różnych typów zdarzeń.


Wiele obiektów w NodeJS emituje zdarzenia, aby poinformować resztę programu, że coś się dzieje.



### Czym są strumienie?


Strumienie łączą bufory i zdarzenia, aby pomóc nam przetwarzać dane.


Kiedy pracujemy z plikami, danymi z sieci, a nawet długim tekstem, nie zawsze musimy (lub chcemy) ładować wszystko do pamięci naraz. Może to być powolne, a nawet spowodować awarię programu, jeśli dane są zbyt duże.


Zamiast tego, możemy przetwarzać dane **stopniowo**, w miarę ich napływania lub odczytywania, tak jakbyśmy pili wodę przez słomkę, zamiast próbować wypić całą szklankę na raz. Nazywa się to **strumieniem**.


W NodeJS strumień jest obiektem, który pozwala odczytywać dane ze źródła lub zapisywać dane do miejsca docelowego **jeden element na raz**.


NodeJS posiada cztery główne typy strumieni:



- Readable**: strumienie, z których można odczytywać dane (jak odczyt pliku)
- Writable**: strumienie, do których można zapisywać dane (jak zapis do pliku)
- Duplex**: strumienie, które można zarówno odczytywać, jak i zapisywać
- Transform**: jak strumienie dupleksowe, ale mogą zmieniać (przekształcać) dane w trakcie ich przepływu


### Strumienie do odczytu


Powiedzmy, że masz do przetworzenia plik `bigfile.txt`. Możesz utworzyć strumień do odczytu za pomocą modułu `fs`, aby odczytać plik kawałek po kawałku.


```javascript
const fs = require("fs")

const readableStream = fs.createReadStream(
"bigfile.txt"
)

readableStream.on("data", (chunk) => {
console.log("Received chunk:", chunk)
})

readableStream.on("end", () => {
console.log("Finished reading file.")
})

readableStream.on("error", (err) => {
console.error("Error reading file:", err)
})
```


Co się tutaj dzieje?


1. `fs.createReadStream()` tworzy strumień do odczytu.

2. Za każdym razem, gdy fragment pliku jest gotowy, strumień emituje zdarzenie `data` i przekazuje nam "fragment" danych (`Buffer`). Wypisujemy ten fragment.

3. Gdy cały plik zostanie odczytany, uruchamiane jest zdarzenie `end`.

4. Jeśli wystąpi błąd (np. plik nie istnieje), wywoływane jest zdarzenie `error`.


W ten sposób można odczytywać gigantyczne pliki bez ładowania ich wszystkich do pamięci naraz.


Jeśli chcemy, aby dane były dostarczane w formie czytelnej dla człowieka (zamiast binarnej), możemy określić kodowanie strumienia:


```javascript
const fs = require("fs")

const readableStream = fs.createReadStream(
"bigfile.txt",
{ encoding: "utf8" } // we tell NodeJS that the file should be read as utf8
)

readableStream.on("data", (chunk) => {
console.log("Received chunk:", chunk)
})

readableStream.on("end", () => {
console.log("Finished reading file.")
})

readableStream.on("error", (err) => {
console.error("Error reading file:", err)
})
```


Kod wydrukuje teraz plik w formie czytelnej dla człowieka.


### Strumienie zapisywalne


Zapisywalny strumień umożliwia wysyłanie danych gdzieś, kawałek po kawałku.


Oto przykład zapisu do pliku `target.txt` przy użyciu strumienia:


```javascript
const fs = require("fs")

const stream = fs.createWriteStream("target.txt")

stream.write("First line\n")
stream.write("Second line\n")
stream.end("Finished writing\n")

stream.on("finish", () => {
console.log("All data written.")
})

stream.on("error", err => {
console.error("Error:", err)
})
```


Oto, co się dzieje:


1. `fs.createWriteStream()` tworzy zapisywalny strumień.

2. Zapisujemy do niego tekst używając `.write()`.

3. Kiedy skończymy, wywołujemy `.end()`, aby zamknąć strumień.

4. Gdy wszystkie dane zostaną zapisane, emitowane jest zdarzenie `finish`.

5. Jeśli coś pójdzie nie tak, wywoływane jest zdarzenie `error`.


Podobnie jak strumienie do odczytu, strumienie zapisywalne są dobre dla dużych zbiorów danych, ponieważ nie muszą przechowywać wszystkiego w pamięci naraz.


### Strumienie rurociągów


Jedną z najfajniejszych rzeczy w strumieniach jest to, że można **pipe** je razem: połączyć strumień do odczytu bezpośrednio ze strumieniem do zapisu.


```javascript
const fs = require("fs")

const readable = fs.createReadStream("bigfile.txt")
const writable = fs.createWriteStream("target.txt")

readable.pipe(writable)
```


Tutaj:



- Strumień do odczytu jest odczytywany z pliku `bigfile.txt`.
- Zapisywalny strumień zapisuje do `copy.txt`.
- `.pipe()` wysyła dane bezpośrednio ze strumienia do odczytu do strumienia do zapisu.


### Strumienie dupleksowe


Strumień dupleksowy można zarówno odczytywać, jak i zapisywać. Jednym z przykładów jest gniazdo sieciowe: można wysyłać do niego dane i odbierać dane z niego.


Oto bardzo prosty przykład wykorzystujący moduł `net`:


```javascript
const net = require("net")

const server = net.createServer((socket) => {
socket.write("Welcome!\n")

socket.on("data", (chunk) => {
console.log("Received:",
chunk.toString()  // we convert the chunk of data from Buffer to string
)
})
})

server.listen(3000, () => {
console.log("Server listening on port 3000")
})
```


W tym przykładzie:



- Obiekt `socket` jest dupleksowym strumieniem.
- Można do niego `zapisywać()`, a także nasłuchiwać zdarzeń `data`.


### Przekształcanie strumieni


Strumień transformujący to strumień dupleksowy, który również modyfikuje dane, które przez niego przechodzą.


Na przykład, można użyć wbudowanego modułu `zlib` do kompresji lub dekompresji danych.


Oto jak skompresować plik przy użyciu strumienia transformacji:


```javascript
const fs = require("fs")
const zlib = require("zlib")

const readable = fs.createReadStream("bigfile.txt")     // create a readable stream that reads from a file
const zip = zlib.createGzip()                           // create a transform stream that compresses data
const writable = fs.createWriteStream("bigfile.txt.gz") // create a writable stream that writes to a file

readable          // take the readable stream
.pipe(zip)      // pipe it into the transform stream to compress the data
.pipe(writable) // then pipe it into the writable stream that saves the data to a zipped file

writable.on("finish", () => {
console.log("File compressed.")
})
```


I zdekompresować go z powrotem:


```javascript
const readable = fs.createReadStream("bigfile.txt.gz")
const unzip = zlib.createGunzip()
const writable = fs.createWriteStream("bigfile.txt")

readable.pipe(unzip).pipe(writable)

writable.on("finish", () => {
console.log("File decompressed.")
})
```


Strumienie transformacji są bardzo przydatne do zadań takich jak kompresja, szyfrowanie lub zmiana formatów plików podczas przesyłania strumieniowego.


### Ciśnienie wsteczne


Czasami zapisywalny strumień wolno obsługuje dane. Jeśli będziemy przesyłać dane do zapisywalnego strumienia szybciej niż jest on w stanie to obsłużyć, możemy napotkać problemy. Nazywa się to **backpressure**.


Jeśli wywołasz metodę `.write()` na zapisywalnym strumieniu, zwróci ona wartość logiczną, która poinformuje cię, czy strumień potrzebuje pauzy; być może będziesz musiał sprawdzić jej wartość zwracaną, jak poniżej:


```javascript
const fs = require("fs")

const readable = fs.createReadStream("example.txt")
const writable = fs.createWriteStream("copy.txt")
r
readable.on("data", chunk => {               // each chunk of data we read from the readable stream...

const canContinue = writable.write(chunk)  // ...we send it to the writable, which returns us a boolean to confirm we can continue

if (!canContinue) { readable.pause() }     // ...if we can't, we temporarily pause reading
})

writable.on("drain",                // the writable stream emits a "drain" event when the backpressure is gone

() => { readable.resume() }      // so we resume reading (and writing)

)
```


Był to ilustracyjny przykład ręcznego przesyłania danych z Readable do Writable i ręcznego zarządzania ciśnieniem wstecznym.


Zwykle przesyłamy dane za pomocą metody `.pipe()`, która automatycznie obsługuje ciśnienie wsteczne.


Musisz więc martwić się o backpressure tylko wtedy, gdy z jakiegoś powodu ręcznie wywołujesz `.write()`.


## Uwaga końcowa

<chapterId>139e2ab8-df67-525a-85f0-5a2fa5e478f2</chapterId>


Tak więc, jeśli postępowałeś zgodnie z lekcjami, powinieneś być teraz w stanie napisać kilka prostych programów w NodeJS.


Sugerowałbym zrobienie dokładnie tego: po nauczeniu się podstaw, stworzenie kilku osobistych projektów jest najlepszym sposobem na ćwiczenie i stanie się lepszym programistą.


Tak naprawdę nie ma znaczenia, co budujesz, ważne jest to, że stawiasz sobie wyzwanie rozwiązywania problemów za pomocą kodu.


Nowoczesne języki programowania są niezwykle potężne, a NodeJS jest prawdopodobnie najlepszym zestawem narzędzi do eksperymentowania na tym etapie podróży.


Powodzenia!


# Sekcja końcowa


<partId>322624d8-6fbc-11f0-a67a-5b145f10afc1</partId>


## Recenzje i oceny


<chapterId>3e93ac86-6fbc-11f0-8bae-9b2ed7914843</chapterId>

<isCourseReview>true</isCourseReview>

## Wnioski


<chapterId>49b3b9b2-6fbc-11f0-9870-5f5adcd3a0eb</chapterId>


<isCourseConclusion>true</isCourseConclusion>