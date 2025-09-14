---
name: JavaScript en NodeJS grondbeginselen
goal: Leer JavaScript-programmeerfundamenten en NodeJS-ontwikkeling om praktische toepassingen en tools te bouwen.
objectives: 

  - De basis JavaScript-syntaxis, -typen en -besturingsstroom onder de knie krijgen
  - Functies, objecten en klassen in JavaScript begrijpen
  - Leren omgaan met fouten en debuggingtechnieken
  - Maak kennis met NodeJS en het bijbehorende ecosysteem

---

# Begin je ontwikkelingsreis


Welkom bij deze cursus over JavaScript en NodeJS.


JavaScript is de populairste programmeertaal ter wereld: het is de scripttaal van moderne browsers, dus het is in principe onmogelijk om een moderne webapplicatie te bouwen zonder *een beetje* JavaScript te schrijven; en met de NodeJS runtime kan het ook buiten browsers worden gebruikt om scripts en applicaties te maken die direct op je computer draaien.


Deze cursus is bedoeld voor mensen die helemaal nieuw zijn in programmeren, of die eerder andere talen hebben gebruikt maar willen begrijpen hoe JavaScript werkt, vooral in de context van NodeJS.


Aan het einde van de cursus moet je in staat zijn om je eigen programma's in JavaScript te schrijven, de NodeJS standaardbibliotheek te gebruiken en pakketten van derden te installeren en te gebruiken om nuttige tools te bouwen.


+++
# Basis JavaScript

<partId>a617327c-e5a2-52ca-9380-c63f44623dd4</partId>


## Setup

<chapterId>ba05a290-1782-5268-87c9-62fd09590e05</chapterId>




Een JavaScript-programma is gewoon een verzameling van (een of meer) tekstbestanden die opdrachten bevatten die moeten worden uitgevoerd door een JavaScript-runtime.


De namen van deze tekstbestanden eindigen meestal met een `.js` bestandsextensie, zoals `mijn_script.js`, `mijn_programma.js` enz.


De commando's die ze bevatten zijn geschreven in de programmeertaal JavaScript.


Een JavaScript runtime is een speciaal programma dat deze bestanden uitvoert.


![](assets/en/1.webp)


### De NodeJS-runtime


De meest gebruikte JavaScript runtime is NodeJS.


Uw IDE bevat het mogelijk al, of u moet het downloaden van de [officiële website](https://nodejs.org/en/download).


Op de downloadpagina vind je instructies voor alle drie de grote besturingssystemen (OS): Windows, Linux en MacOS. Er wordt van uitgegaan dat je weet hoe je een terminal in je OS moet openen.


Aangezien NodeJS beschikbaar is voor alle drie de besturingssystemen, kunnen de programma's die je schrijft op alle besturingssystemen worden uitgevoerd (afgezien van enkele randgevallen).


Dit betekent dat je bijvoorbeeld een eenvoudige videogame in JavaScript kunt schrijven op je Windows-pc en het aan je vriend kunt geven om het op zijn Mac uit te voeren.


![](assets/en/2.webp)














### Eerste programma (hello world)


Traditioneel, wanneer je een programmeertaal bestudeert, bestaat het eerste programma dat je schrijft uit het afdrukken van "hello world!" naar de console.


Maak een map genaamd `my_js_code/`, met daarin een bestand genaamd `main.js` (deze namen zijn willekeurig).


Open de map met uw code-editor.


Schrijf deze code in je bestand:


```javascript
console.log("hello world!")
```


Open een terminal en voer deze opdracht uit om het programma uit te voeren:


```
node main.js
```


Het resultaat zou moeten zijn


```
hello world!
```


### Wat er gebeurde


In JavaScript is alles een "object".


`console` is een object dat wordt gebruikt om het programma te debuggen.


`console.log` is de meest gebruikte methode van de `console`. Het drukt gewoon de argumenten af die je er aan doorgeeft.


Je geeft argumenten door aan `console.log` met de ronde haakjes `()`.


Dus als je bijvoorbeeld het getal `1000` wilt afdrukken, schrijf je gewoon


```javascript
console.log(1000)
```


Voer het dan uit door


```
node main.js
```


in je terminal (vanaf nu gaat deze cursus ervan uit dat je weet dat dit de manier is om een programma uit te voeren).


Dit zou moeten afdrukken


```
1000
```


Je kunt meerdere dingen doorgeven, zoals


```javascript
console.log(16, 8, 1993)
```


Hiermee wordt het volgende afgedrukt


```
16 8 1993
```


## Variabelen en opmerkingen

<chapterId>23050ab7-343b-5edf-9d37-e4e782e27ce0</chapterId>


Programma's voeren meestal bewerkingen uit op gegevens.


Variabelen zijn als het ware naamvakjes die we gebruiken om gegevens in op te slaan. Ze stellen ons in staat om een gegeven te associëren met een specifieke naam, zodat we het later kunnen ophalen met die naam.


### `let` verklaringen


Om een variabele te declareren in JavaScript, kunnen we het sleutelwoord `let` gebruiken.


Na het schrijven van `let`, schrijven we de naam die we aan de variabele willen geven, dan een `=` teken en dan de waarde die we willen opslaan.


Bijvoorbeeld:


```javascript
let age = 25

console.log(age)
```


De naam van een variabele (technisch gezien de "identifier" genoemd) kan meestal letters, underscores (`_`), het dollarteken (`$`) en cijfers bevatten, hoewel het eerste teken geen cijfer mag zijn.


In de bovenstaande code hebben we een variabele genaamd `leeftijd` gedeclareerd en de waarde `25` erin opgeslagen.


Vervolgens hebben we de waarde afgedrukt met `console.log(age)`.


Als je deze code uitvoert met `node main.js`, is de uitvoer als volgt:


```
25
```


Identifiers zijn hoofdlettergevoelig, wat betekent dat kleine letters en hoofdletters tellen als verschillen in identifiers, dus bijvoorbeeld


```javascript
let age = 25

let Age = 20

console.log(age)
```


zal 25 worden afgedrukt, omdat dit twee volledig afzonderlijke variabelen zijn!


Je kunt ook tekenreeksen (tekst) opslaan in een variabele:


```javascript
let message = "hello again"

console.log(message)
```


Dit wordt afgedrukt:


```
hello again
```


Net als eerder hebben we `console.log()` gebruikt om de waarde af te drukken die is opgeslagen in de variabele.


Laten we nu beide samen doen:


```javascript
let age = 25

let message = "hello again"

console.log(age)

console.log(message)
```


Als je dit uitvoert, wordt het afgedrukt:


```
25
hello again
```

### Overplaatsing


Variabelen gedeclareerd met `let` kunnen worden gewijzigd nadat ze zijn gemaakt.


Dit wordt herplaatsing genoemd.


```javascript
let score = 10

console.log(score)

score = 15

console.log(score)
```


Eerst wijzen we `10` toe aan `score` en drukken het dan af.


Daarna veranderen we de waarde van `score` in `15` en drukken we het opnieuw af.


De uitvoer zal zijn:


```
10
15
```


Dit is erg handig als de waarde na verloop van tijd verandert, zoals in een spel waar de score stijgt.


Laten we nog een variabele aan de mix toevoegen:


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


Dit wordt afgedrukt:


```
10
Alice
20
Bob
```


Zoals je kunt zien, zijn zowel `score` als `speler` gewijzigd.


### `const` declaraties


Meestal willen we echter niet dat een variabele verandert nadat hij is gemaakt. Daarvoor gebruiken we `const`.


`const` is een afkorting voor "constante". Zodra je een waarde toekent aan een `const` variabele, kun je deze niet meer veranderen.


```javascript
const pi = 3.14
console.log(pi)
```


Deze afdrukken:


```
3.14
```


Maar als je dit probeert te doen:


```javascript
const pi = 3.14
console.log(pi)

pi = 99 // this line will cause an error
console.log(pi)
```


JavaScript geeft een foutmelding zoals:


```
TypeError: Assignment to constant variable.
```


Dit komt omdat `pi` is gedeclareerd met `const`, en je kunt de waarde daarna niet meer wijzigen. Je communiceert naar de JavaScript-interpreter dat je niet wilt dat die variabele verandert.


Dit is handig omdat het de kans verkleint dat je het per ongeluk verandert. Wanneer programma's erg groot worden, met duizenden regels code, is het onmogelijk om bij te houden wat er allemaal tegelijk gebeurt (dat is de belangrijkste reden waarom we computers gebruiken, om complexe processen uit te voeren die we niet met onze hersenen kunnen berekenen), dus wordt het nuttig om beperkingen zoals deze te hebben, die het programma deterministischer maken.


Het wordt als de beste gewoonte beschouwd om onze waarden altijd als `const` te declareren, tenzij we zeker weten dat we ze later willen wijzigen.


### Commentaar in JavaScript


Soms willen we notities in onze code schrijven die niet worden uitgevoerd. Dit wordt commentaar genoemd.


Commentaar wordt genegeerd door het programma als het draait, maar is handig om dingen uit te leggen aan onszelf of aan andere mensen.


Om een commentaar van één regel te schrijven, gebruik je `//`


```javascript
// This is a comment
const x = 10 // This is also a comment
console.log(x)
```


Dit wordt nog steeds afgedrukt:


```
10
```


De opmerkingen zijn er alleen voor mensen om te lezen.


Je kunt ook meerregelig commentaar schrijven met `/*` en `*/`


```javascript
/*
This is a multi-line comment.
It can span several lines.
*/
const y = 20
console.log(y)
```


Hiermee wordt het volgende afgedrukt


```
20
```


En de opmerking wordt genegeerd.


Je kunt commentaar gebruiken om kleine annotaties aan je code toe te voegen, zodat je misschien onthoudt wat het doet en waarom het op een bepaalde manier geschreven is. Het kan ook andere programmeurs helpen om het te begrijpen.


## Basistypen: getallen, tekenreeksen, booleans

<chapterId>cfdb04f6-21a8-5143-bbf9-7aaae04962f0</chapterId>


In JavaScript vertelt een "type" je wat voor soort gegevens een waarde is.


Javascript heeft een paar basistypes en in deze sectie zullen we er een paar verkennen.


### Getallen en rekenkundige bewerkingen


Het eerste type dat we gaan introduceren is `getal`.


Getallen in JavaScript kunnen gehele getallen zijn (zoals `5`) of decimalen (zoals `3.14`).


Je kunt ermee rekenen: optellen, aftrekken, vermenigvuldigen en delen.


Hier is een basisvoorbeeld:


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


Dit wordt afgedrukt:


```
15
5
50
2
```


Je kunt ook haakjes `()` gebruiken om de volgorde van bewerkingen te bepalen:


```javascript
const result = (2 + 3) * 4
console.log(result)
```


Deze afdrukken:


```
20
```


Zonder de haakjes zou het `2 + 3 * 4` zijn, wat is:


```javascript
const result = 2 + 3 * 4
console.log(result)
```


Dat zou worden afgedrukt:


```
14
```


Want in gewone wiskunde gaat vermenigvuldiging vóór optelling.


### Ringen en interpolatie


Het tweede JavaScript-type dat we gaan introduceren is `string`.


Strings zijn stukken tekst. Je kunt enkele aanhalingstekens `'...'` of dubbele aanhalingstekens `"..."` gebruiken om ze te maken.


```javascript
const greeting = "hello"
const name = 'Bob'
console.log(greeting)
console.log(name)
```


Deze afdrukken:


```
hello
Bob
```


Om strings te combineren, kun je de `+` operator gebruiken:


```javascript
const greeting = "hello"
const space = " "
const name = "Bob"

const fullGreeting = greeting + space + name
console.log(fullGreeting)
```


Dit wordt afgedrukt:


```
hello Bob
```


Maar er is een mooiere manier om strings te combineren, genaamd **string interpolatie**. Je gebruikt backticks om de string `` `...`` te declareren en schrijft variabelen met `${...}` binnen de string:


```javascript
const greeting = "hello"
const name = "Bob"

const fullGreeting = `${greeting} ${name}`
console.log(fullGreeting)
```


Dit wordt ook afgedrukt:


```
hello Bob
```


Je kunt elke expressie opnemen binnen `${...}`:


```javascript
const age = 30
console.log(`Next year, I will be ${age + 1} years old.`)
```


Deze afdrukken:


```
Next year, I will be 31 years old.
```


Interpolatie is heel gebruikelijk in modern JavaScript.


### Booleans, vergelijking en logische bewerkingen


Het derde type dat we gaan introduceren is `boolean`. Het is vernoemd naar de wiskundige George Boole, die de booleaanse logica uitvond.


Booleans zijn eenvoudig: slechts twee mogelijke waarden, `true` en `false`.


Je kunt ze opslaan in variabelen:


```javascript
const theSkyIsBlue = true
const thisCourseIsBad = false

console.log(theSkyIsBlue)
console.log(thisCourseIsBad)
```


Deze afdrukken:


```
true
false
```


Je kunt booleans combineren met logische operatoren:



- `&&` betekent "en", en retourneert alleen `waar` als **beide** waarden `waar` zijn, anders retourneert het `nietwaar`
- `||` betekent "of", en het zal `waar` teruggeven als **tenminste één** van de waarden `waar` is, anders (als ze allebei onwaar zijn) zal het `onwaar` teruggeven
- `!` betekent "niet", het wordt toegepast voor een boolean en zal het omdraaien: als het boolean `true` is, zal het `false` teruggeven, en vice versa.


![](assets/en/3.webp)


Voorbeelden:


```javascript
const isSunny = true
const isWarm = true

console.log(isSunny && isWarm)  // true
console.log(isSunny || isWarm)  // true
console.log(!isSunny)           // false
```


Je kunt waarden in JavaScript vergelijken met operatoren als `>`, `<`, `==` en `!==`. Het resultaat van deze vergelijkingen is altijd een booleaanse waarde.


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


Javascript heeft ook `>=` om "groter of gelijk" te betekenen en `<=` om "kleiner of gelijk" te betekenen.


Booleans, vergelijkings- en logische operatoren worden vaak gecombineerd in programma's om complexe voorwaarden op te geven, zoals "de e-mail is aangekomen EN hij bevat de afbeelding die ik nodig heb OF de lengte van de e-mail is langer dan 10000 tekens". Later zul je zien dat dit essentiële bouwstenen zijn om de logica van het programma te construeren.


## Rijen, nul, ongedefinieerd

<chapterId>7bf18183-5eae-53ed-83d2-b04982145d81</chapterId>


In dit gedeelte behandelen we nog drie typen die veel voorkomen in JavaScript-programma's:



- Arrays**: opeenvolgingen van waarden
- undefined**: een speciale waarde die betekent "er is niets toegewezen"
- null**: een andere speciale waarde die "opzettelijk leeg" betekent


### Matrices en indextoegang


Een **array** is een type dat meerdere waarden in een lijst kan bevatten.


Je maakt een array door vierkante haakjes `[]` te gebruiken en de items te scheiden met komma's.


Hier is een basisvoorbeeld:


```javascript
const numbers = [10, 2, 88]
console.log(numbers)
```


Deze afdrukken:


```
[ 10, 2, 88 ]
```


Je kunt alles opslaan in een array, niet alleen getallen:


```javascript
const things = ["apple", 42, true]
console.log(things)
```


Deze afdrukken:


```
[ 'apple', 42, true ]
```


Om toegang te krijgen tot een specifiek item in de array, gebruiken we een **index**. De index is de positie van het item, beginnend bij **0**.


Dus in deze matrix:


```javascript
const colors = ["red", "green", "blue"]
```



- `colors[0]` is `"rood"`
- `kleuren[1]` is `"Green"`
- `colors[2]` is `"blauw"`


Laten we het proberen:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[0])
console.log(colors[1])
console.log(colors[2])
```


Dit wordt afgedrukt:


```
red
green
blue
```


Je kunt een waarde toewijzen aan een specifieke index van een matrix


```javascript
const colors = ["red", "green", "blue"]

colors[1] = "yellow"

console.log(colors)
```


Dit wordt afgedrukt:


```
[ 'red', 'yellow', 'blue' ]
```


Je kunt elk natuurlijk getal als index gebruiken, zelfs een getal dat is opgeslagen in een variabele


```javascript

const i = 1
const colors = ["red", "green", "blue"]
console.log(colors[i])
```


Dit wordt afgedrukt:


```
green
```


Maar als je een index probeert te benaderen die niet bestaat, krijg je `undefined`:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[3])
```


Deze afdrukken:


```
undefined
```


Wat is dat?


### `undefined`


De speciale waarde `undefined` betekent "er is geen waarde toegekend".


Als je een variabele aanmaakt maar geen waarde geeft, zal deze `ongedefinieerd` zijn:


```javascript
const name
console.log(name)
```


Deze afdrukken:


```
undefined
```


Omdat we niets hebben toegewezen aan `naam`, stelt JavaScript deze standaard in op `onbepaald`.


Zoals eerder gezien, kun je ook `undefined` krijgen als je een array-index opent die niet bestaat:


```javascript
const fruits = ["banana", "apple"]
console.log(fruits[2]) // There is no index 2
```


Deze afdrukken:


```
undefined
```


### `null` en hoe het te behandelen


`null` is ook een speciale waarde. Het betekent "er is hier niets, en dat heb ik expres gedaan"


In tegenstelling tot `undefined`, dat automatisch is, is `null` iets dat je zelf instelt.


Bijvoorbeeld:


```javascript
const currentUser = null
console.log(currentUser)
```


Deze afdrukken:


```
null
```


Waarom `null` gebruiken? Misschien verwacht je later een waarde, maar is die nog niet klaar:


```javascript
let winner = null

// Later in the program:
winner = "Alice"

console.log(winner)
```


Deze afdrukken:


```
Alice
```


Dus `null` is handig als je bijvoorbeeld wilt zeggen: "Er zou hier later iets moeten zijn, maar op dit moment is het leeg."


## Blokken en besturingsstroom

<chapterId>be985168-2636-5b0d-a48f-ac1bbfbff8a7</chapterId>


Tot nu toe hebben we vooral regels code geschreven die achter elkaar worden uitgevoerd.


Maar wanneer we coderen, kunnen we de volgorde van uitvoering bepalen.


Dit wordt **controlestroom** genoemd.


Laten we beginnen met het begrijpen van blokken en scope.


### De wereldwijde reikwijdte


Elke variabele die we declareren bestaat in een **scope**, dat wil zeggen het deel van de code waar de variabele bekend is.


Als je een variabele buiten een blok declareert, bestaat deze in de **global scope**.


```javascript
const color = "blue"
console.log(color)
```


Deze variabele `kleur` staat in de globale scope, dus hij kan overal in het bestand worden gebruikt.


Als je meer regels toevoegt:


```javascript
const color = "blue"
console.log(color)

const size = "large"
console.log(color)
console.log(size)
```


Zowel `kleur` als `grootte` zijn globale variabelen. Ze zijn overal in het bestand beschikbaar.


Maar wat gebeurt er binnen een blok?


### Blokken en lokaal bereik


Een **block** is een stuk code omgeven door accolades `{}`.


Variabelen gedeclareerd met `let` of `const` binnen een blok bestaan **alleen** binnen dat blok.


```javascript
{
const message = "inside block"
console.log(message)
}
```


Deze afdrukken:


```
inside block
```


Maar als je dit probeert:


```javascript
{
const message = "inside block"
}
console.log(message) // Error!
```


JavaScript geeft een foutmelding zoals:


```
ReferenceError: message is not defined
```


Dat komt omdat `message` in het blok is gedeclareerd en daarbuiten niet bestaat.


Dit betekent dat we blokken kunnen gebruiken om delen van onze code te isoleren en er zeker van te zijn dat "wat in het blok gebeurt, ook in het blok blijft" (een beetje zoals Las Vegas).


Door onze code te organiseren in blokken kunnen we ook de uitvoering van het programma structureren, met controlestroomconstructies zoals `if`


### `if`, `else`


Soms willen we code uitvoeren **alleen als** iets waar is. Daar is het `if` statement voor.


```javascript
const myAge = 20

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Deze afdrukken:


```
Am I an adult?
Yes I am!
```


Zoals je kunt zien, vergelijkt de code `mijn leeftijd` en `18`.

In dit geval geeft de `>=` operator `true`, dus het blok wordt uitgevoerd.

Als de voorwaarde niet `true` is, wordt het blok niet uitgevoerd.


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Deze afdrukken:


```
Am I an adult?
```


Je kunt een `else` blok toevoegen om het tegenovergestelde geval af te handelen:


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
} else {
console.log("No, I am not.")
}
```


Deze afdrukken:


```
Am I an adult?
No, I am not.
```


Zowel de `if` als `else` blokken zijn nog steeds blokken - dus variabelen die erin zijn gedeclareerd bestaan niet buiten deze blokken.


Als we zeker willen weten dat iets **niet** waar is, wat kunnen we dan doen?


Nou, zoals eerder besproken, heeft JavaScript een "not" operator, die booleans omdraait. Dus we kunnen


```javascript
const myAge = 17

const adult = myAge >= 18

console.log("Am I an adult?")

if (!adult) {
console.log("No, I am not.")
}
```

Dit wordt nog steeds afgedrukt:


```
Am I an adult?
No, I am not.
```

Omdat we de `!` operator hebben gebruikt om de `adult` variabele om te keren.


`if (!adult) {...}` moet worden gelezen als "if not adult..."


Met blokken, logica en vergelijkingsoperatoren kunnen we de uitvoering van het programma structureren door variabelen te definiëren die `waar` (of `onwaar`) moeten zijn om iets te laten gebeuren.


### terwijl`, `onderbreken`, `doorgaan`


Een `while` lus herhaalt code *zolang* een voorwaarde waar is.


```javascript
let count = 0

while (count < 3) {
console.log("Count is", count)
count = count + 1
}
console.log("the loop is over!")
```


Deze afdrukken:


```
Count is 0
Count is 1
Count is 2
the loop is over!
```


Wanneer `count` 3 wordt, stopt de lus.


Je kunt een lus vroegtijdig stoppen met `break`:


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


Deze afdrukken:


```
0
1
2
```


Want als het getal `3` wordt, wordt het `if` blok uitgevoerd en stopt de lus.


Je kunt de rest van een lus overslaan met `continue`:


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


Deze afdrukken:


```
1
2
4
5
```


Want toen het getal `3` was, zorgde `continue` ervoor dat het programma de regel oversloeg die het getal afdrukte.


### `voor ... van ...`


Als je een array hebt en iets wilt doen met elk item erin, kun je `for ... of ... gebruiken. {...}`.


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const fruit of fruits) {
console.log(fruit)
}
```


Deze afdrukken:


```
apple
banana
cherry
```

Het blok wordt één keer uitgevoerd voor elk element van de array.


`fruit` is hier een nieuwe variabele die de waarde aanneemt van elk item in de array, om er binnen het blok mee te werken.


### `voor ... in ...`


Je kunt `for ... in` gebruiken om over de sleutels (indexen) van een array te lussen:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(index)
}
```


Deze afdrukken:


```
0
1
2
```


Je kunt de index ook gebruiken om de waarde te krijgen:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(fruits[index])
}
```


Dit drukt hetzelfde af als `voor ... van`:


```
apple
banana
cherry
```


In de praktijk kun je voor arrays beter `for ... of` gebruiken, omdat dat eenvoudiger en schoner is.


### Afgebakende lussen


Soms willen we een specifiek aantal keer lussen, of in het algemeen een stuk code schrijven dat een blok herhaalt terwijl het iets bijhoudt.

Daar is een begrensde `for` lus goed voor.

Een begrensde lus heeft meestal drie voorwaarden, gescheiden door een puntkomma `;`, zoals in `(... ; ... ; ....)`.


```javascript
for (let i = 0; i < 3; i = i + 1) {
console.log(i)
}
```


Deze afdrukken:


```
0
1
2
```


Laten we het uitleggen:



- `laat i = 0`: declareert een variabele die in het blok wordt gebruikt (in dit geval is het een teller die op 0 begint)
- `i < 3`: verklaart een voorwaarde die `waar` moet zijn voor het blok dat moet worden uitgevoerd (in dit geval is dat "herhaal terwijl `i` kleiner is dan 3")
- `i = i + 1`: geef een code op die moet worden uitgevoerd na elke uitvoering van het blok (in dit geval "verhoog `i` met 1")


Zoals je kunt zien kunnen we met de bounded loop complexere voorwaarden opgeven voor het herhaaldelijk uitvoeren van een stuk code, maar meestal is dat niet nodig.


### Bloklabels


Als je een complexere besturingsstroom moet schrijven, kun je in JavaScript een blok een naam geven met een **label** dat kan worden gebruikt door `break` of `continue` om aan te geven *waar* je terug moet springen.


Voorbeeld:


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


Deze afdrukken:


```
Inside outer block
Inside inner block
Done
```


We hebben `break outer` gebruikt om het `outer` blok volledig te verlaten.


Je kunt lussen ook labelen. Laten we dit voorbeeld nemen:


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

Dit was een heel saai voorbeeld, maar hopelijk heeft het de (incidentele) behoefte aan labels verduidelijkt.


## Functies introduceren

<chapterId>cc324715-09c2-5cf7-9e6f-47a6f16bc04d</chapterId>


Als je programma's groeien, zul je vaak stukken code** willen hergebruiken.


Daar zijn **functies** voor: hiermee kun je code groeperen, een naam geven en uitvoeren wanneer je maar wilt.


### Functieverklaring


Om een functie te declareren, kunnen we het sleutelwoord `functie` gebruiken. Dan geven we het een naam, een paar haakjes `()` met de argumenten die het neemt, en een blok code `{}` om uit te voeren. Laten we beginnen met een functie die geen argumenten gebruikt:


```javascript
function sayHello () {console.log(`Hello!`) }
```


Deze code **kondigt** de functie aan, maar voert deze **nog** niet uit.


### Functie-oproepen


Om de functie uit te voeren (of "aan te roepen"), schrijf je de naam gevolgd door haakjes:


```javascript
function sayHello () {console.log(`Hello!`) }
sayHello()
```


Deze afdrukken:


```
Hello!
```


Je kunt de functie zo vaak oproepen als je wilt:


```javascript
function sayHello() {
console.log("Hello!")
}

sayHello()
sayHello()
```


Deze afdrukken:


```
Hello!
Hello!
```


De code in de functie wordt alleen uitgevoerd wanneer je deze aanroept.


### Functieargumenten (invoer voor functies)


Soms wil je een functie laten werken met wat invoer. Je kunt dat doen door **argumenten** toe te voegen binnen de haakjes.


Bijvoorbeeld:


```javascript
function sayHelloTo (friend) {
console.log(`Hello ${friend}!`)
}
```


Nu neemt deze functie **één argument** genaamd `friend`.


Wanneer je de functie aanroept, kun je een waarde doorgeven:


```javascript
sayHelloTo("Tommy")
```


Deze afdrukken:


```
Hello Tommy!
```


Je kunt de functie opnieuw aanroepen met een andere naam:


```javascript
sayHelloTo("Sam")
```


Deze afdrukken:


```
Hello Sam!
```


De waarde die je doorgeeft vervangt de `friend` variabele in de functie.


Je kunt ook meer dan één argument gebruiken:


```javascript
function greetTwoPeople(person1, person2) {
console.log(`Hello ${person1} and ${person2}!`)
}

greetTwoPeople("Lina", "Marco")
```


Deze afdrukken:


```
Hello Lina and Marco!
```


### `return` (uitvoer van functies)


Functies kunnen ook waarden **retourneren**. Dit betekent dat ze een waarde terugsturen naar waar de functie ook werd aangeroepen.


Hier is een eenvoudig voorbeeld:


```javascript
function getNumber() {
return 42
}

const result = getNumber()
console.log(result)
```


Deze afdrukken:


```
42
```


De functie `getNumber()` geeft `42`, we slaan het op in `result` en drukken het vervolgens af.


Je kunt ook iets teruggeven dat je hebt berekend:


```javascript
function add(a, b) {
return a + b
}

const result = add(2, 3)
console.log(result)
```


Deze afdrukken:


```
5
```


Zodra een waarde is `return`, stopt de functie. Alles na `return` in dat blok gebeurt niet.


```javascript
function saySomething() {

return "hi"

console.log("this never runs")

}

const message = saySomething()
console.log(message)
```


Dit drukt alleen af:


```
hi
```


omdat alleen `"hi"` wordt geretourneerd. De regel `console.log("this never runs")` wordt overgeslagen.


Je kunt functies zien als kleine subprogramma's. Elke functie kan invoer aannemen, bewerken en uitvoer teruggeven.


Wat gebeurt er als we de returnwaarde van een functie proberen te gebruiken, maar die functie heeft niets teruggegeven?


```javascript
function doesNothing () {}

const x = doesNothing()

console.log(x)
```

Dit zal `undefined` afdrukken. De retourwaarde van een functie die niets teruggaf is `undefined`.


## Objecten en klassen

<chapterId>26689f25-8212-5057-8c21-3a05eee0ac75</chapterId>


JavaScript wordt vaak een objectgeoriënteerde taal genoemd.


Dat betekent dat het je helpt je code te organiseren door waarden en functies te groeperen in **objecten**.


### Wat is een `object`?


Een object kan gegevens bevatten en functies die op die gegevens werken. Als een functie in een object wordt gestopt, zeggen we dat het een `methode` is.


Het eerste object dat we hebben gezien is het `console` object. Het is een object dat meerdere methodes bevat om dingen op het scherm af te drukken en onze programma's te debuggen.


Het kan zelfs zichzelf afdrukken; je kunt


```javascript
console.log(console)
```


en het zal een lijst afdrukken van de methodes die het bevat. Op mijn machine werd bijvoorbeeld het volgende afgedrukt


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


Zoals je kunt zien, heeft het veel methoden die je kunt gebruiken om te debuggen!


Javascript biedt ons verschillende manieren om nieuwe objecten te maken die kunnen doen wat we maar willen.


### Een object maken


De eenvoudigste manier om een object te maken is door gegevens en functies te groeperen met **curly braces** `{}`.


Dit maakt wat we noemen een **anoniem object**


```javascript
const cat = {
name: "Whiskers",
age: 3
}
```


Dit maakt een object en slaat het op in een variabele genaamd `cat`.


Het object heeft twee **eigenschappen**:



- `naam` met de waarde `"Snorharen"`
- `leeftijd` met de waarde `3`


Laten we het afdrukken:


```javascript
console.log(cat)
```


Deze afdrukken:


```
{ name: 'Whiskers', age: 3 }
```


Je kunt de eigenschappen uit het object halen door een punt te gebruiken, zoals in `objectName.propertyName`:


```javascript
console.log(cat.name)  // prints "Whiskers"
console.log(cat.age)   // prints 3
```


Je kunt een eigenschap ook **wijzigen**:


```javascript
cat.age = 4
console.log(cat.age)  // now it prints 4
```


Zoals je kunt zien, kun je zelfs als een object is gedefinieerd als `const`, nog steeds de gegevens die het bevat wijzigen.


In het geval van objecten zal `const` alleen voorkomen dat je het hele object overschrijft:


```javascript
const cat = {
name: "Whiskers",
age: 3
}

cat.age = 5 // this works

cat = 5 // this throws an error, you're trying to reassign the whole object

```


Zoals eerder vermeld, kunnen objecten ook **functies** bevatten, en als een functie deel uitmaakt van een object, noemen we het een **methode**.


Hier is een voorbeeld:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log("Meow!")
}
}
```


Dit object heeft:



- Een `naam` eigenschap
- Een `spreek()` methode


Laten we de methode aanroepen:


```javascript
cat.speak()
```


Het drukt af:


```
Meow!
```


Methoden kunnen de gegevens gebruiken die het object bevat via het sleutelwoord `this`.

`this` verwijst naar het huidige object. In dit voorbeeld wordt het gebruikt om de naam van de kat af te drukken:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log(`${this.name} says meow!`)
}
}

cat.speak()
```


Deze afdrukken:


```
Whiskers says meow!
```


Het woord `dit` betekent "dit object"... in dit geval het object `kat`.



Dit soort objecten zijn geweldig als je iets snel en eenvoudig wilt maken. Maar als je **veel objecten** moet maken met dezelfde structuur, is er een betere manier, en dat is waar **klassen** van pas komen.


### Klassen en constructeurs


Een **klasse** is als een blauwdruk. Het vertelt JavaScript hoe het een bepaald soort object moet maken.


Je definieert een klasse met het `class` sleutelwoord, gevolgd door de naam van de klasse en door een blok met accolades `{}`.


```javascript
class Dog {}
```


Klassen beginnen gewoonlijk met een hoofdletter.


Je kunt een nieuw object van een klasse maken met `new`:


```javascript
const hachiko = new Dog()
```


Probeer het object af te drukken:

```javascript
class Dog {}

const myDog = new Dog()

console.log(myDog)
```


Je krijgt


```
Dog {}
```


Zoals je kunt zien is de Dog class leeg, dus het `myDog` object is ook leeg.


We kunnen definiëren welke eigenschappen Dog objecten moeten bevatten door een `constructor` toe te voegen.


Een constructor is een speciale functie die wordt uitgevoerd wanneer je een nieuw object maakt (of "construeert").


```javascript
class Dog {
constructor() { }
}
```


We willen dat elke Hond een naam heeft, dus voegen we een `naam` parameter toe aan de functie:


```javascript
class Dog {
constructor(name) { }
}
```


En dan gebruiken we `this` om aan te geven dat `naam` de `naam` is van het `Dog` object dat we bouwen


```javascript
class Dog {
constructor(name) {
this.name = name
}}
```


Laten we het nu proberen te gebruiken:


```javascript
class Dog {
constructor(name) {
this.name = name
}
}

const myDog = new Dog("hachiko")

console.log(myDog)
```


Dit drukt iets af als:


```
Dog { name: 'hachiko' }
```


Zoals je kunt zien, neemt de `constructor` methode de argumenten die je doorgeeft aan de klasse wanneer je `new Dog()` doet, en het gebruikt deze om het object te bouwen.


Laten we het opsplitsen:



- `class Dog` definieert de klasse Dog.
- `constructor(name)` stelt het object in wanneer het wordt gemaakt.
- `this.name = name` slaat de waarde op in het nieuwe object.
- `new Dog("hachiko")` creëert een nieuw object van de klasse, met de `name` eigenschap ingesteld op `"hachiko"`.


Laten we nu een methode toevoegen aan onze klasse:


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


Hiermee wordt het volgende afgedrukt


```javascript
hachiko says barf!
```


Als we hetzelfde doen voor twee verschillende instanties van Hond



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


krijgen we


```
hachiko says barf!
bobby says barf!
```


de `speak()` methode gebruikt de `name` eigenschap van de `Dog` waarop het wordt aangeroepen.


Dit is de belangrijkste reden waarom klassen bestaan: ze stellen ons in staat om een verzameling methoden te definiëren die werken op gegevens en vervolgens meerdere objecten te maken die dezelfde gegevens "vorm" hebben.


Wanneer we een methode aanroepen op een van deze objecten, zal deze methode werken op de gegevens die *dat specifieke object* bevat.


### De vorm van een object wijzigen


Objecten in JavaScript zijn flexibel. Zelfs nadat je er een hebt gemaakt, kun je nog steeds nieuwe eigenschappen toevoegen of bestaande verwijderen.


Het is toegestaan, maar je moet het voorzichtig gebruiken.


Laten we beginnen met onze eenvoudige `Dog` klasse:


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


Op dit moment heeft `mijnHond` slechts één eigenschap: `naam`. We kunnen nog steeds nieuwe eigenschappen toevoegen nadat het is aangemaakt:


```javascript
myDog.age = 5

console.log(myDog.age) // prints 5
```


We kunnen ook een nieuwe methode toevoegen:


```javascript
myDog.jump = function () {
console.log(`${this.name} jumps!`)
}

myDog.jump() // Fido jumps!
```


En we kunnen ook eigenschappen verwijderen met het sleutelwoord `delete`.


```javascript
delete myDog.name

console.log(myDog.name) // prints 'undefined'
```


Dit werkt, maar hier is iets belangrijks om te weten: JavaScript-engines zoals de V8 (gebruikt in Node.js en in de Chrome-browser) werken sneller als je objecten altijd dezelfde eigenschappen behouden. Als je eigenschappen toevoegt of verwijdert nadat het object is gemaakt, kan dit de werking vertragen.


In kleine programma's maakt dit niet veel uit. Maar in grotere projecten (zoals games) is het beter om vanaf het begin alle eigenschappen in de constructor op te sommen, zelfs als je ze niet meteen gebruikt. Dit houdt de objectvorm stabiel en helpt je code sneller te draaien.


Bijvoorbeeld, in plaats van dit:


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


Je zou het volgende kunnen doen


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


Beide versies werken, maar de tweede is beter voor de prestaties. Je vertelt de engine van tevoren welke eigenschappen elk object zal hebben en het kan dienovereenkomstig optimaliseren.


Met JavaScript kun je objecten vrijelijk een andere vorm geven, maar als je klassen gebruikt, kun je de vorm van je object het beste van tevoren plannen.



### Overerving met `extends` en `super()`


Soms wil je een klasse maken die *bijna* hetzelfde is als een andere klasse, maar met een paar extra mogelijkheden.


In plaats van de vorm van objecten aan te passen (wat zoals gezegd niet optimaal is voor de prestaties), of een nieuwe klasse helemaal opnieuw te schrijven, kun je in JavaScript gebruik maken van **inheritance**.


Inheritance betekent dat een klasse een andere klasse kan **uitbreiden**. De nieuwe klasse krijgt alle eigenschappen en methodes van de oude en je kunt meer toevoegen of veranderen wat je nodig hebt.


Laten we zeggen dat we een basisklasse hebben met de naam `Voertuig`:


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


Nu willen we een `auto` klasse maken. Een auto is een soort voertuig, maar we willen misschien dat het wat extra functies heeft of een andere boodschap wanneer het start. In plaats van alles te herschrijven, kunnen we `extends` gebruiken:


```javascript
class Car extends Vehicle {
start() {
console.log(`${this.brand} car is ready to drive!`)
}
}
```


De `Car` klasse **erft** nu alles van `Vehicle`. Het krijgt de `merk` eigenschap en we hebben de `start()` methode vervangen door onze eigen versie.


![](assets/en/4.webp)


Laten we het uitproberen:


```javascript
const myCar = new Car("Toyota")
myCar.start()
```


Deze afdrukken:


```
Toyota car is ready to drive!
```


Ook al heeft `Auto` geen eigen constructor, het gebruikt nog steeds die van `Voertuig`. Maar als we een eigen constructor willen schrijven in `Auto`, dan kunnen we dat. We hoeven alleen maar een aanroep naar de constructor van zijn ouder toe te voegen met `super()`.


Zo:


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



Deze afdrukken:


```
Toyota Corolla is ready to drive!
```


Samengevat



- `extends` betekent dat een klasse gebaseerd is op een andere.
- `super()` wordt gebruikt om de constructor aan te roepen van de klasse die je uitbreidt.
- De nieuwe klasse krijgt alle eigenschappen en methoden van de oorspronkelijke klasse.
- Je kunt **overschrijven** methoden (zoals `start()`) om ze iets anders te laten doen.


Dit is handig als je verschillende dingen hebt die op elkaar lijken (zoals auto's, vrachtwagens en fietsen) en je wilt dat ze code delen maar zich toch op hun eigen manier gedragen.


### `instantie van`


Het `instanceof` sleutelwoord controleert of een object is gemaakt van een bepaalde klasse.


Laten we zeggen dat we een klasse hebben met de naam `User`:


```javascript
class User {
constructor(username) {
this.username = username
}
}

const regularUser = new User("julia123")

console.log(regularUser instanceof User)
```


Deze afdrukken:


```
true
```


Bevestigen dat `regularUser` een `User` is. Dat komt omdat `regularUser` is gemaakt met de `User` klasse.


Het werkt ook met **geërfde** klassen. Bijvoorbeeld, hier is een `Admin` klasse die `User` uitbreidt:


```javascript
class Admin extends User {}

const ourAdmin = new Admin("admin42")

console.log(ourAdmin instanceof Admin)   // true
console.log(ourAdmin instanceof User)    // true
```


Beide regels geven `true` terug. Dat komt omdat `Admin` een subklasse is van `User`, daarom is `onzeAdmin` zowel een `Admin` als een `User`


# JavaScript voor gevorderden

<partId>243f63ab-4f34-5c30-80cb-84ef46f6761d</partId>


## Foutafhandeling

<chapterId>d0206bc5-d386-5e7f-9917-5803f392448c</chapterId>


Naarmate je complexere JavaScript-programma's schrijft, zul je **errors** tegenkomen. Dit zijn onverwachte situaties waarin iets fout gaat. Misschien is een variabele `gedefinieerd` maar probeer je hem toch te gebruiken, of ontvangt een code het verkeerde type invoer.


Als we deze fouten niet goed afhandelen, kan ons programma crashen of zich op onvoorspelbare manieren gedragen. JavaScript biedt hulpmiddelen om deze fouten op te sporen en te beheren, zodat we er beter mee om kunnen gaan.


### Veelvoorkomende fout: een waarde openen op `undefined`


Hier is een veelvoorkomende situatie die een fout veroorzaakt:


```javascript
const user = undefined
console.log(user.name)
```


Als je deze code uitvoert, krijg je een fout die er als volgt uitziet:


```
TypeError: Cannot read properties of undefined (reading 'name')
```


Dat is JavaScript die je vertelt: "Hé, je probeerde de `naam` eigenschap te krijgen van iets dat `ongedefinieerd` is, en dat slaat nergens op." En zoals je kunt zien, wanneer dit soort fouten optreedt, stopt het programma met draaien tenzij je specifiek code hebt geschreven om het op te vangen en af te handelen.


### een fout `gooien


Soms wil je handmatig **een foutmelding** maken in je code. In dat geval gebruik je het `throw` sleutelwoord.


```javascript
throw new Error("This is a custom error message")
```


Hierdoor wordt het programma onmiddellijk gestopt en wordt er afgedrukt:


```
Uncaught Error: This is a custom error message
```


Je kunt `throw` gebruiken om regels af te dwingen in je programma. Bijvoorbeeld:


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


De tweede aanroep veroorzaakt een fout omdat delen door nul niet is toegestaan in dit voorbeeld.


### Fouten opvangen met `try...catch`


Als je niet wilt dat je programma crasht als er een fout optreedt, kun je de fout opvangen met een `try...catch` blok. Dit is handig als je wilt dat je programma **doorgaat** zelfs als er iets mislukt.


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log("Oops! Something went wrong.")
}
```


Uitgang:


```
Oops! Something went wrong.
```


Zo werkt het:



- De code in het `try` blok wordt eerst geprobeerd.
- Als er een fout optreedt, springt JavaScript naar het `catch` blok**, waarbij de rest van het `try` blok wordt overgeslagen.
- Het `catch` blok ontvangt de fout, zodat je deze kunt afdrukken, of op een andere manier kunt afhandelen, zoals bijvoorbeeld


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log(`The message of the error was: "${error.message}"`)
}
```


Uitgang:


```
The message of the error was: "Cannot read properties of undefined (reading 'name')"
```


### Het `finaal` blok


Je kunt ook een `finally` blok toevoegen. Dit is code die **altijd** wordt uitgevoerd, of er nu een fout is opgetreden of niet.


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


Uitgang:


```
Trying something risky...
Caught the error: Uh oh!
This will run no matter what.
```


## Insecten vermijden

<chapterId>db12d9f6-5806-514c-998e-0ae24805104e</chapterId>


Dit hoofdstuk laat een aantal van de meest voorkomende valkuilen in JavaScript zien, en hoe je ze kunt vermijden.


### `var` en Assignment zonder declaratie


In oudere JavaScript-code werden variabelen vaak gedeclareerd met het `var` sleutelwoord. In tegenstelling tot `let` en `const`, waar je al over geleerd hebt, kan `var` zich op verwarrende manieren gedragen.


Bijvoorbeeld:


```javascript
{
var message = "hello"
}
console.log(message)
```


Je zou verwachten dat `message` alleen binnen het blok bestaat, maar dat is niet zo. `var` negeert de blok scope en maakt de variabele beschikbaar in de hele functie of bestand.


Dit kan leiden tot onverwacht gedrag, vooral in grotere programma's. Om deze reden moet moderne JavaScript-code altijd `let` of `const` gebruiken in plaats van `var`.


Erger nog, in JavaScript kun je waarden toewijzen aan variabelen **zonder ze überhaupt te declareren**:


```javascript
function greet() {
user = "Alice"
}
greet()
console.log(user) // prints "Alice"
```


Dit creëert een nieuwe globale variabele `naam` zonder declaratie. Dit kan stilletjes gebeuren en leiden tot bugs die Hard zijn om op te sporen, vooral als het gewoon een typefout was. Declareer variabelen altijd met `let` of `const`.


### Zwak type systeem


JavaScript is zwak getypeerd, wat betekent dat het automatisch waarden van het ene type naar het andere converteert als dat nodig is. Dit heet type coercion en hoewel het handig kan zijn, leidt het vaak tot verwarrende resultaten.


Bijvoorbeeld:


```javascript
console.log("5" + 1)    // "51"
console.log("5" - 1)    // 4
console.log(true + 1)   // 2
console.log(null + 1)   // 1
```


In deze voorbeelden probeert JavaScript te raden wat je bedoelde. Soms verandert het tekenreeksen in getallen, of booleans in getallen, of tekenreeksen in tekenreeksen. Hierdoor kan je code zich op onverwachte manieren gedragen.


Het is belangrijk om je bewust te zijn van het zwakke typesysteem van JavaScript. Als dingen vreemd gaan doen, kan dat komen door onverwachte type coercion.


### `"use strict"`


Je kunt een strengere modus inschakelen die van sommige stille fouten echte fouten maakt en je ervan weerhoudt om sommige van de gevaarlijkere functies van de taal te gebruiken.


Om deze strengere modus in te schakelen, voegt u deze regel toe bovenaan uw bestand of functie:


```javascript
"use strict"
```


Bijvoorbeeld:


```javascript
"use strict"
name = "Alice" // ReferenceError: name is not defined
```


Zonder strikte modus zou JavaScript stilletjes een globale variabele genaamd `naam` aanmaken. Maar met strikte modus wordt dit een echte fout, waardoor je bugs eerder kunt opsporen.


De strikte modus schakelt ook enkele verouderde functies van JavaScript uit en maakt je code eenvoudiger te optimaliseren en te onderhouden.


## Waarde vs Referentie

<chapterId>bb898425-dc2f-5e5c-864b-0cb7a4a9aea9</chapterId>


JavaScript behandelt verschillende soorten waarden op verschillende manieren.


Sommige waarden worden **gekopieerd** wanneer je ze toewijst aan een variabele.


Andere worden **gedeeld** wanneer je ze toewijst aan een nieuwe variabele, dus als je er één verandert, verandert de andere ook.


### Waarde doorgeven


Wanneer een waarde wordt doorgegeven **per waarde**, maakt JavaScript er een **kopie** van.


Dus als je de ene verandert, heeft dat geen invloed op de andere.


Dit gebeurt met primitieve types, zoals:



- nummers
- snaren
- booleans (`true` en `false`)
- `null`
- `undefined`


Laten we een voorbeeld bekijken:


```javascript
let a = 5
let b = a

b = 10

console.log(a) // 5
console.log(b) // 10
```


We hebben `b` de waarde van `a` gegeven, maar toen hebben we `b` veranderd in `10`.


Omdat getallen per waarde worden doorgegeven, heeft JavaScript de `5` in `b` gekopieerd. De `5` in `b` is onafhankelijk van de originele `5` in `a` dus het veranderen van de waarde van `b` had geen effect op `a`.


Laten we het proberen met een string:


```javascript
let name1 = "Alice"
let name2 = name1

name2 = "Bob"

console.log(name1) // Alice
console.log(name2) // Bob
```


Nogmaals, het veranderen van `naam2` had geen invloed op `naam1`, omdat strings ook als waarde worden doorgegeven.


Hetzelfde gebeurt als je een primitieve aan een functie doorgeeft: het wordt gekopieerd. Dus de functie kan het origineel niet veranderen.


```javascript
function plusOne(x) {
x = x + 1
}

let number = 5

plusOne(number)

console.log(number) // 5
```


Hoewel binnen de functie `1` is toegevoegd aan `x`, is het oorspronkelijke `getal` niet veranderd.


Dat komt omdat er alleen een **kopie** is doorgegeven aan de functie.


### Doorgeven door verwijzing


Objecten worden **per referentie** doorgegeven.


Dat betekent dat in plaats van ze te kopiëren, JavaScript er gewoon een **verwijzing** naar doorgeeft, en als je het wijzigt, zullen alle andere variabelen die ernaar verwijzen ook de wijziging zien.


Bijvoorbeeld:


```javascript
const person1 = { name: "Alice" }
const person2 = person1

person2.name = "Bob"

console.log(person1.name) // Bob
console.log(person2.name) // Bob
```


Zowel `person1` als `person2` wijzen naar hetzelfde object in het geheugen.


Dus toen we `person2.name` veranderden, veranderden we ook `person1.name`, omdat ze allebei naar hetzelfde kijken.


Arrays zijn objecten, dus laten we hetzelfde proberen met een array:


```javascript
const list1 = [1, 2, 3]
const list2 = list1

list2.push(4)

console.log(list1) // [1, 2, 3, 4]
console.log(list2) // [1, 2, 3, 4]
```


We hebben `4` in `list2` geduwd, maar `list1` werd ook beïnvloed, omdat ze allebei naar dezelfde array verwijzen.


Laten we eens kijken wat er gebeurt als we een object doorgeven aan een functie:


```javascript
function rename(user) {
user.name = "Charlie"
}

const person = { name: "Dana" }

rename(person)

console.log(person.name) // Charlie
```


De functie veranderde het object! Dat komt omdat het een **verwijzing** ontving naar het oorspronkelijke `person` object.


Het kreeg geen kopie. Het kreeg toegang tot het originele object en daarmee de mogelijkheid om het te wijzigen.


Het is belangrijk om dit onderscheid te onthouden, omdat onze code zich anders anders kan gedragen dan we verwachten. We kunnen bijvoorbeeld een functie schrijven met de verwachting dat het de argumenten die het ontvangt niet zal wijzigen, en er later achter komen dat het ze wel degelijk wijzigde (omdat het objecten waren, dus ze werden doorgegeven per referentie).


## Werken met functies

<chapterId>e0d277a8-c642-5af7-9e53-dee27c811967</chapterId>


Je hebt al geleerd hoe je functies kunt declareren en gebruiken in JavaScript. Maar JavaScript geeft je meer hulpmiddelen om op krachtige manieren met functies te werken.


### Pijl functies


Pijlfuncties zijn een kortere manier om functies te schrijven. In plaats van het sleutelwoord `functie` gebruiken we een pijl (`=>`).


Hier is een normale functie:


```javascript
function greet(name) {
return `Hello, ${name}!`
}
```


De versie met de pijl ziet er als volgt uit:


```javascript
const greet = (name) => {
return `Hello, ${name}!`
}
```


Als de functie **slechts** één regel heeft, kun je de accolades overslaan en `return`:


```javascript
const greet = (name) => `Hello, ${name}!`
```


Als de functie **alleen een parameter** heeft, kun je zelfs de haakjes rond de parameters overslaan:


```javascript
const greet = name => `Hello, ${name}!`
```


Pijl functies zijn heel gebruikelijk in modern JavaScript, omdat ze het mogelijk maken om eenvoudige functies uit te drukken met aanzienlijk minder boilerplate.


### Standaardparameters


Soms wil je dat een functie een **standaardwaarde** heeft als er geen argument wordt doorgegeven.


Je kunt dat als volgt doen:


```javascript
function sayHello(name = "friend") {
console.log(`Hello, ${name}!`)
}

sayHello("Alice") // Hello, Alice!
sayHello()        // Hello, friend!
```


De standaardwaarde `"friend"` wordt gebruikt als er niets wordt doorgegeven.


### Gespreide parameters (`...`)


Wat als je functie een flexibel aantal argumenten neemt?


Je kunt de **spread operator** (`...`) gebruiken om ze in een array te verzamelen:


```javascript
function logAll(...items) {
console.log(items)
}

logAll(1, 2, 3) // [1, 2, 3]
logAll("a", "b") // ["a", "b"]
```


Je kunt dan een lus gebruiken om elk item te verwerken:


```javascript
function logEach(...items) {
for (const item of items) {
console.log(item)
}
}
```


De spread operator is handig als je niet weet hoeveel argumenten er worden doorgegeven.


### Functies van hogere orde


Een **hogere-orde-functie** is een functie die:



- neemt een andere functie als invoer
- en/of geeft een functie terug als uitvoer


Hier is een eenvoudig voorbeeld:


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


Deze afdrukken:


```
Hello, friend!
Hello, friend!
```


We kunnen er een pijlfunctie aan doorgeven:


```javascript
runTwice(
() => console.log("Hello!")
)
```


Deze afdrukken:


```
Hello!
Hello!
```


Je kunt ook functies schrijven die **teruggeven** naar andere functies:


```javascript
function makeGreeter(name) {
return () => console.log(`Hi, ${name}`)
}

const greetAlice = makeGreeter("Alice")
const greetBob = makeGreeter("Bob")

greetAlice() // Hi, Alice
greetBob() // Hi, Bob
```


De `makeGreeter` functie is een functie die andere functies bouwt. Het ontvangt een string en retourneert een nieuwe functie die die string gebruikt in zijn `console.log` aanroep.


Dit soort patronen is erg krachtig, omdat het je in staat stelt om "gaten" in je functies te laten die je later kunt vullen met het gedrag dat je nodig hebt.


### `map()`, `filter()`, `reduce()`


JavaScript geeft je een aantal handige ingebouwde methoden om te gebruiken met arrays.


Deze methoden nemen functies als argumenten, dus het zijn ook hogere-orde functies.


`map()` transformeert elk item in een array in iets anders.


Voorbeeld:


```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map(x => x * 2)

console.log(doubled) // [2, 4, 6]
```


Elk getal wordt verdubbeld en het resultaat is een nieuwe matrix.


`filter()` verwijdert items uit de array als ze niet voldoen aan een test.


Voorbeeld:


```javascript
const numbers = [1, 2, 3, 4, 5]
const numbersGreaterThanTwo = numbers.filter(x => x > 2)

console.log(numbersGreaterThanTwo) // [3, 4, 5]
```


Alleen de array-items waarvoor de voorwaarde `x > 2` `waar` oplevert, worden bewaard.


`reduce()` wordt gebruikt om alle items in een array te combineren tot een enkele waarde.


Voorbeeld:


```javascript
const numbers = [1, 2, 3, 4]
const total = numbers.reduce((current, next) => current + next)

console.log(total) // 10
```


`reduce` gaat door de array en past, in dit voorbeeld, de `+` operator toe tussen `1` en `2`, dan tussen de resulterende `3` en `3`, dan tussen de resulterende `6` en `4`, totdat het de som van alle array-items heeft (wat 10 is).


Je kunt `reduce()` voor veel dingen gebruiken, zoals totalen, gemiddelden of het stap voor stap opbouwen van nieuwe waarden.


Deze methoden (`map`, `filter`, `reduce`) zijn krachtige hulpmiddelen om gegevens te verwerken zonder handmatige lussen te schrijven.


Je kunt ze zelfs combineren in een keten van operaties, zoals dit:


```javascript
const numbers = [1, 2, 3, 4, 5]

const result = numbers
.map(n => n * 2)        // Double each entry, obtain [2, 4, 6, 8, 10]
.filter(n => n > 3) // Keep only the entries bigger than 3, so you get [4, 6, 8, 10]
.reduce((n1, n2) => n1 + n2) // Adds them: 4 + 6 + 8 + 10 = 28

console.log(result) // 28
```


## Werken met objecten

<chapterId>7842aada-f009-5518-b8e3-1104e166a035</chapterId>


In dit hoofdstuk leren we een aantal krachtige en iets geavanceerdere gereedschappen voor het werken met objecten in JavaScript.


### Particuliere eigendommen


Soms willen we een eigenschap van een object verbergen zodat deze niet kan worden gewijzigd of geopend van buiten het object. JavaScript geeft ons een manier om dit te doen met `#` voor de naam van de eigenschap. Dit creëert een **private** eigenschap, die alleen toegankelijk is vanuit de klasse.


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


Privé-eigenschappen zijn handig wanneer u onbedoelde wijzigingen wilt voorkomen.


### `statische` Eigenschappen


Soms wil je dat een eigenschap bij de klasse zelf hoort, niet bij elk object dat je van die klasse maakt. Daar is `static` voor. Een `statische` eigenschap zit in de klasse en alle objecten van die klasse zullen ernaar verwijzen.


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


Dit is handig voor het opslaan van gedeelde gegevens en methoden die van toepassing zijn op de hele groep objecten, niet slechts één.


### `get` en `set`


In JavaScript kun je met `get` en `set` eigenschappen maken die er *uitzien* als normale variabelen, maar eigenlijk speciale code uitvoeren op de achtergrond.


Een `get`ter methode wordt uitgevoerd wanneer je een eigenschap probeert te *lezen*. Deze wordt gedeclareerd door `get` te schrijven voor een methode met de naam van de eigenschap.


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


Hoewel `fullName` geen gewone eigenschap is, kunnen we het wel zo gebruiken en achter de schermen wordt de `get` functie uitgevoerd om de volledige naam op te bouwen.


Een `set`ter methode wordt uitgevoerd wanneer je een waarde *toewijst* aan een eigenschap. Hiermee kun je bepalen wat er gebeurt als iemand die waarde probeert te veranderen. Het wordt gedeclareerd door `set` te schrijven voor een methode met de naam van de eigenschap.


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


Wanneer we `user.fullName = "John Smith"` uitvoeren, wordt de `set` methode uitgevoerd en worden de `firstName` en `lastName` waarden bijgewerkt.


Dus ook al lijkt het alsof we gewoon een eenvoudige variabele instellen, we triggeren eigenlijk logica die andere eigenschappen bijwerkt.


## Sleutels en waarden

<chapterId>01a397b8-c12a-5c39-82b3-6d9ebbb72a29</chapterId>


Elke eigenschap in een JavaScript-object heeft een **key** (ook wel een eigenschapsnaam genoemd) en een **value**.


Bijvoorbeeld:


```javascript
const user = {
name: "Alice",
age: 30
}
```


In dit object zijn `"naam"` en `"leeftijd"` de sleutels en "Alice" en `30` hun waarden.


### Dynamische toegang


Soms weet je de naam van een eigenschap niet van tevoren... misschien krijg je hem van gebruikersinvoer of lees je hem uit een variabele. Je kunt het nog steeds benaderen met **bracket notatie**, zoals `mijnObject["keyName"]`.


```javascript
const user = {
name: "Alice",
age: 30
}

console.log(user["name"]) // Alice
```


We hebben de tekenreeks `naam` doorgegeven aan het object om de bijbehorende waarde te krijgen.


We kunnen een sleutel opslaan in een variabele en deze later gebruiken om de corresponderende waarde te openen, zoals


```javascript
const user = {
name: "Alice",
age: 30
}

const key = "name"

console.log(user[key]) // Alice
```


### Dynamisch Assignment


Je kunt ook objecteigenschappen maken of bijwerken met variabelen als sleutels.


```javascript
const settings = {}

const key = "theme"
settings[key] = "dark"

console.log(settings) // { theme: "dark" }
```


Dit is handig als je een object stap voor stap wilt bouwen. Bijvoorbeeld:


```javascript
const user = {}

user["username"] = "bananaFan123"
user["email"] = "banana@fruit.com"

console.log(user)
// { username: "bananaFan123", email: "banana@fruit.com" }
```


Je kunt zelfs een dynamische sleutel gebruiken *tijdens het maken* van het object door vierkante haken te gebruiken:


```javascript
const key = "language"
const config = {
[key]: "JavaScript"
}

console.log(config.language) // JavaScript
```


Dit wordt een **berekende eigenschap** genoemd. De waarde binnen de vierkante haakjes wordt geëvalueerd en het resultaat wordt gebruikt als sleutel.


### `Symbool` Type


Naast strings kun je in JavaScript ook een speciaal type genaamd `Symbool` gebruiken als objectsleutel.


Laten we beginnen met een eenvoudig voorbeeld:


```javascript
const id = Symbol("userID")

const user = {
name: "Bob",
[id]: 12345
}

console.log(user[id]) // 12345
```


In dit voorbeeld is `id` een Symbool. Het is geen string, maar het werkt nog steeds als een sleutel. Als je `user` probeert te loggen op de console, zie je dit:


```javascript
console.log(user) // { name: 'Bob', [Symbol(userID)]: 12345 }
```


Nog iets belangrijks: elk symbool dat je maakt is uniek, zelfs als ze zijn gemaakt met dezelfde tekenreeks.


```javascript
const a = Symbol("label")
const b = Symbol("label")

console.log(a === b) // false
```


Met symbolen kun je sleutels definiëren die niet botsen met gewone sleutels. Bijvoorbeeld, laten we zeggen dat je een object hebt met een `naam` eigenschap, maar het object zal in de toekomst worden aangepast door een gebruiker, op manieren die je niet kunt voorspellen, en die gebruiker zou ook een `naam` eigenschap kunnen toevoegen. Als de oorspronkelijke `naam` eigenschap was gedefinieerd met een string, zou het worden overschreven door de nieuwe, zoals dit:


```javascript
const obj = {
name: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy' }
```


Als we in plaats daarvan een Symbool gebruiken:


```javascript
const name = Symbol("name")

const obj = {
[name]: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy', [Symbol(name)]: 'John' }
```


Zoals je kunt zien, blijft de oorspronkelijke `naam` eigenschap op de een of andere manier behouden op deze manier. Dit kan handig zijn in bepaalde randgevallen.


## Objecten

<chapterId>516e74c8-2a11-545a-a4d1-c2cabb91a273</chapterId>


JavaScript geeft ons een aantal handige ingebouwde objecten die ons helpen om dingen te doen zoals debuggen en wiskundige bewerkingen.


### Andere `console`-Methoden


Je hebt `console.log` al gezien, dat waarden op het scherm afdrukt.


Er zijn enkele andere nuttige methoden beschikbaar op het object `console` die je kunnen helpen bij het debuggen van je programma's.


#### `console.warn`


Drukt een bericht af in geel (of met een waarschuwingspictogram in sommige omgevingen):


```javascript
console.warn("This is just a warning.")
```


#### `console.error`


Drukt een bericht in rood af, zoals een fout:


```javascript
console.error("Something went wrong!")
```


#### `console.table`


Geeft een matrix of object weer als een tabel:


```javascript
const users = [
{ name: "Alice", age: 25 },
{ name: "Bob", age: 30 }
]

console.table(users)
```


Dit drukt een tabel af zoals:


```
┌─────────┬────────┬─────┐
│ (index) │  name  │ age │
├─────────┼────────┼─────┤
│    0    │ 'Alice'│  25 │
│    1    │ 'Bob'  │  30 │
└─────────┴────────┴─────┘
```


Dit kan handig zijn om gestructureerde gegevens te visualiseren.


#### `console.time` en `console.timeEnd`


Je kunt meten hoe lang iets duurt:


```javascript
console.time("timer")
for (let i = 0; i < 1000000; i++) {}
console.timeEnd("timer")
```


Dit drukt iets af als:


```
timer: 2.379ms
```


Nuttig voor eenvoudige prestatietests.


### Het `Math`-object


JavaScript geeft je een `Math` object met handige methoden om berekeningen uit te voeren.


#### `Math.random()`


Geeft een willekeurig getal tussen 0 (inclusief) en 1 (exclusief):


```javascript
const r = Math.random()
console.log(r)
```


Voorbeelduitvoer:


```
0.4387429859
```


#### `Math.floor()` en `Math.ceil()`



- `Math.floor(n)` rondt **naar beneden** af op het dichtstbijzijnde gehele getal
- `Math.ceil(n)` rondt **naar boven** af op het dichtstbijzijnde gehele getal


```javascript
console.log(Math.floor(4.9)) // 4
console.log(Math.ceil(4.1))  // 5
```


#### `Math.round()`


Rondt af op het dichtstbijzijnde gehele getal:


```javascript
console.log(Math.round(4.4)) // 4
console.log(Math.round(4.6)) // 5
```


#### `Math.max()` en `Math.min()`


Geeft de grootste of kleinste waarde uit een lijst met getallen:


```javascript
console.log(Math.max(5, 9, 3)) // 9
console.log(Math.min(5, 9, 3)) // 3
```


#### `Math.pow()` en `Math.sqrt()`



- `Math.pow(a, b)` geeft je `a` tot de macht van `b`
- `Math.sqrt(n)` geeft je de vierkantswortel van `n`


```javascript
console.log(Math.pow(2, 3))   // 8
console.log(Math.sqrt(16))    // 4
```


# JavaScript voor gevorderden

<partId>72c30671-ca20-5617-92a5-d5ba7aa38c93</partId>


## Andere collecties

<chapterId>a9a70c6d-a343-5a46-a383-e288bc2700e3</chapterId>


JavaScript geeft ons een aantal speciale verzameltypes die verder gaan dan gewone arrays en objecten. Deze omvatten `Map` en `Set`.


Ze helpen je om groepen waarden op te slaan en te beheren, maar ze werken anders dan wat je tot nu toe hebt gezien.


Een `Map` is een verzameling **key-value paren**, net als een object. Maar het heeft een aantal belangrijke verschillen:



- De sleutels kunnen **elke waarde** zijn, niet alleen strings.
- De volgorde van de items blijft behouden.
- Het heeft ingebouwde methoden om het werken ermee te vergemakkelijken.


Zo maak je een nieuwe kaart:


```javascript
const myMap = new Map()
```


Dit maakt een lege map. Gebruik `myMap.set(key, value)` om items toe te voegen:


```javascript
myMap.set("name", "Alice")
```


Dit voegt een sleutel `"naam"` toe met waarde `"Alice"`.


Je kunt ook een nummer als sleutel gebruiken:


```javascript
myMap.set(42, "The answer")
```


En zelfs een object als sleutel:


```javascript
const objKey = { id: 1 }
myMap.set(objKey, "Object as key")
```


Dat zou niet werken met gewone objecten, die alleen tekenreekssleutels toestaan.


Gebruik `myMap.get(key)` om een waarde** te **krijgen:


```javascript
console.log(myMap.get("name"))     // Alice
console.log(myMap.get(42))         // The answer
console.log(myMap.get(objKey))     // Object as key
```


Om te **controleren of een sleutel bestaat**, gebruik je `mijnMap.heeft(sleutel)`:


```javascript
console.log(myMap.has("name")) // true
```


Gebruik `myMap.delete(key)` om **een sleutel** te verwijderen:


```javascript
myMap.delete("name")
```


Om **de hele kaart** te wissen, gebruik je `mijnkaart.wissen()`:


```javascript
myMap.clear()
```


Kaarten zijn geweldig voor het beheren van grote verzamelingen waarden, omdat het benaderen van waarden op een grote kaart meestal veel betere prestaties geeft dan op een groot object.


### `Set`


Een `Set` is een verzameling van **alleen waarden** (geen sleutels), waarbij elke waarde **uniek** moet zijn. Dat betekent:



- Je kunt niet twee keer dezelfde waarde hebben
- De waarden worden opgeslagen in de volgorde waarin je ze toevoegt


Je maakt een set als deze:


```javascript
const mySet = new Set()
```


Om **waarden** toe te voegen, gebruik je `mijnSet.add(waarde)`:


```javascript
mySet.add(1)
mySet.add(2)
mySet.add(2) // duplicate, will be ignored
```


Ook al hebben we geprobeerd `2` twee keer toe te voegen, de set zal slechts één kopie bewaren.


Om **te controleren of een waarde in de set** zit, gebruik je `mijnSet.heeft(waarde)`:


```javascript
console.log(mySet.has(2)) // true
console.log(mySet.has(3)) // false
```


Om een waarde** te **verwijderen, gebruik je `mijnSet.delete(waarde)`:


```javascript
mySet.delete(2)
```


Om **alles** te wissen, gebruik je `mijnSet.wissen()`:


```javascript
mySet.clear()
```


Een `Set` is handig als je een verzameling unieke waarden wilt bewaren zonder handmatig te hoeven controleren op duplicaten:


```javascript
const numberArray = [1, 2, 2, 3, 4, 4, 4, 5]

const numberSet = new Set(numberArray)

console.log(numberSet) // Set(5) { 1, 2, 3, 4, 5 }
```


De `Set` voorkomt duplicaten voor je.


## Iteratoren

<chapterId>61d24e5e-b7e4-541a-8322-778f61f26a72</chapterId>


De meeste dingen in JavaScript waar je overheen kunt lussen (zoals arrays, strings, maps, sets) zijn **iterable**: ze kunnen iterators voor hun inhoud leveren.


Een **iterator** is een speciaal object in JavaScript waarmee je **één voor één** door een lijst met items kunt gaan.


### `Object` iterators


In tegenstelling tot arrays of maps zijn gewone objecten **niet iterabel** met `for...of`. Als je dit probeert:


```javascript
const user = {
name: "Alice",
age: 30
}

for (const value of user) {
console.log(value)
}
```


Je krijgt een foutmelding:


```
TypeError: user is not iterable
```


Dat komt omdat gewone objecten geen ingebouwde iterator hebben. Maar JavaScript geeft je andere hulpmiddelen om erover te lussen.


#### `Object.sleutels()`


Je kunt `Object.keys(obj)` gebruiken om een array te krijgen van de **keys** van het object, en er dan overheen lussen:


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


Deze afdrukken:


```
name
age
```


#### `Object.waarden()`


Om over de **waarden** te lussen, gebruik je `Object.values()`:


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


Deze afdrukken:


```
Alice
30
```


#### `Object.entries()`


Als je **zowel de sleutel als de waarde** wilt, gebruik dan `Object.entries()`:


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


Deze afdrukken:


```
name is Alice
age is 30
```


Hoewel objecten niet direct iterabel zijn, geven deze methoden je volledige toegang tot hun inhoud op een manier die goed werkt met `for...of`.


Maar hoe werken iterators?


### `symbool.iterator`


Het geheim achter alle iterables is een speciaal **symbool** genaamd `Symbol.iterator`.


Dit symbool is een ingebouwde sleutel die JavaScript vertelt: "Dit object kan worden geïtereerd."


Als je `myIterable[Symbol.iterator]()` aanroept, geeft JavaScript je een **iterator object** terug met een `.next()` methode.


Laten we eens kijken hoe dat eruitziet:


```javascript
const colors = ["red", "green", "blue"]

const iterator = colors[Symbol.iterator]()

console.log(iterator.next()) // { value: 'red', done: false }
```


Elke aanroep van `.next()` geeft je de volgende waarde. Als het klaar is, keert het terug:


```javascript
{ value: undefined, done: true }
```


### `volgende()`


De `.next()` methode wordt gebruikt om het volgende item uit de reeks te krijgen.


Elke keer dat je `.next()` aanroept, krijg je een object met twee sleutels:



- `waarde`: het huidige item
- `done`: een boolean dat aangeeft of de iteratie voorbij is


Laten we een volledig voorbeeld doen:


```javascript
const names = ["Lina", "Tom", "Eva"]      // declare an array
const iterator = names[Symbol.iterator]() // use the Symbol.iterator function to get an iterator for this array

let result = iterator.next()              // get the first element of the array

while (!result.done) {                    // repeat this loop until you reach the last element of the array, which is marked with { done: true }
console.log(result.value)               // print the value of each element
result = iterator.next()                // get the next element of the array
}
```


Deze afdrukken:


```
Lina
Tom
Eva
```


Dit is hoe een `for...of` lus onder de motorkap werkt: het gebruikt dit patroon met `.next()`.


Je krijgt hetzelfde resultaat met


```javascript
const names = ["Lina", "Tom", "Eva"]

for (const result of names) {
console.log(result)
}
```


### Een klasse iterabel maken


Je kunt ook je eigen **iterator klasse** definiëren door een `[Symbol.iterator]()` methode toe te voegen.


Laten we zeggen dat we een klasse willen die een **bereik van getallen** vertegenwoordigt, bijvoorbeeld van 1 tot 5.


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


Deze afdrukken:


```
1
2
3
4
5
```


Dit is wat er gebeurt:



- We hebben een klasse `Range` gedefinieerd
- Binnen de klasse hebben we `[Symbol.iterator]()` geïmplementeerd, zodat JavaScript weet hoe het moet itereren
- De `next()` methode geeft elk getal één voor één terug
- Als we het `einde` bereiken, retourneert het `{ done: true }`


Nu werkt onze `Range` klasse als een array en kunnen we het gebruiken in elke lus die een iterable verwacht.


### Generatorfuncties en `opbrengst


Om het gemakkelijker te maken om iterators te maken, geeft JavaScript je **generatorfuncties**, door gebruik te maken van het `function*` sleutelwoord (het is `function` met een `*` aan het einde) en het `yield` sleutelwoord.


Laten we het proberen:


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


Elke `yield` geeft een waarde terug en **pauzeert** de functie tot de volgende `.next()` wordt aangeroepen.


Je kunt ook over een generator lussen met `for...of`:


```javascript
for (const num of numberGenerator()) {
console.log(num)
}
```


Deze afdrukken:


```
1
2
3
```


## Concurrentie met callbacks

<chapterId>f3fc76ca-b3ef-54eb-a06e-501007002054</chapterId>


Tot nu toe was onze code **synchroon**: het werd regel voor regel uitgevoerd, in volgorde. Maar sommige dingen in de echte wereld kosten tijd en we willen niet dat het hele programma pauzeert terwijl het wacht.


In dit hoofdstuk introduceren we een nieuw concept: **concurrency**. Hiermee kunnen we de volgorde waarin dingen gedaan worden manipuleren. Dit is handig als je te maken hebt met zaken als timers, gebruikersinvoer of het lezen van bestanden van schijf. JavaScript biedt verschillende hulpmiddelen voor het uitvoeren van concurrency.


### `setTimeout`


Met de functie `setTimeout` kun je **een functie later uitvoeren**, nadat er enige tijd is verstreken.


Voorbeeld:


```javascript
console.log("Start")

setTimeout(
() => console.log("This runs after 2 seconds"),
2000
)

console.log("End")
```


Deze afdrukken:


```
Start
End
This runs after 2 seconds
```


Hoewel `setTimeout` midden in de code staat, blokkeert het de rest niet. In plaats daarvan wordt de functie ingepland om **later** uitgevoerd te worden en wordt er direct verder gegaan.


De `2000` betekent 2000 milliseconden (dat is 2 seconden).

Hier is een meer uitgebreide en beginnersvriendelijke herschrijving van de **Callbacks** en **Promise** secties, met behulp van gegevensmanipulatie en duidelijke annotaties:


### Terugbellen


Een **callback** is gewoon een functie die we aan een andere functie geven zodat deze later** kan worden aangeroepen**.


Laten we eens kijken naar een echt voorbeeld met getallen. Stel je voor dat we een lijst met getallen hebben en we willen elk van hen verdubbelen en dan een functie (de callback) toepassen op de resulterende "verdubbelde" array, maar we willen dit doen na een kleine vertraging, alsof we wachten op iets traags (zoals het laden van gegevens van het internet).


Hier is een functie die dat doet met behulp van een **callback**:


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


Laten we proberen deze functie te gebruiken:


```javascript
const input = [1, 2, 3]

doubleNumbers(input, function(result) {
console.log("Here is the doubled array:", result)
})
```


Na 1 seconde wordt dit afgedrukt:


```
Here is the doubled array: [ 2, 4, 6 ]
```


**Wat gebeurt hier?


1. We geven `input` door als de lijst met getallen die we willen verdubbelen.

2. We geven ook een **callback-functie** door die het programma vertelt wat het moet doen *na* het verdubbelen.

3. Binnen `doubleNumbers` simuleren we een vertraging met `setTimeout`, daarna verdubbelen we.

4. Als dat gedaan is, roepen we de callback aan op de resulterende "verdubbelde" array.


Deze techniek werkt, maar stel dat je daarna **meer stappen** wilt doen, zoals kleine getallen eruit filteren en ze dan optellen. Dan zou je meer callbacks als deze moeten **nesten**:


```javascript
doubleNumbers(input, function(doubled) {
filterBigNumbers(doubled, function(filtered) {
sumNumbers(filtered, function(total) {
console.log("Final result:", total)
})
})
})
```


Dit is Hard om te lezen en rommelig. Deze stijl wordt **callback hel** genoemd, en het is precies wat `Promise` moest oplossen.


## Concurrentie met beloften

<chapterId>30fddaca-729f-5c8d-bf86-8dfc7b3c9800</chapterId>


Een `belofte` is een ingebouwd JavaScript-object dat een waarde vertegenwoordigt die **in de toekomst** klaar zal zijn.


We kunnen een Promise als volgt maken:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve("It worked!") // This means everything went OK
})
```


Het `new Promise()` gedeelte creëert de belofte.


Daarbinnen geven we het een functie met twee parameters:



- `resolve`, is een functie die we aanroepen als alles gelukt is
- `reject`, is een functie die we aanroepen als er iets fout gaat


In het bovenstaande voorbeeld lossen we het direct op met het bericht `"Het is gelukt!"`.


### `.dan()`


Om iets te doen **nadat** de belofte is gedaan, gebruiken we `.then()`:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve(100) // This means everything went OK
})

promise.then(result => {
console.log("The result is:", result)
})
```


Deze afdrukken:


```
The result is: 100
```


De waarde die we hebben doorgegeven aan `resolve()` wordt naar de functie binnen `.then()` gestuurd als `result`.


Laten we een taak simuleren die 2 seconden duurt met `setTimeout`:


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


Dit wacht 2 seconden en drukt dan af:


```
Done waiting!
```


### `verwerp()`


Laten we een belofte maken die **faalt**:


```javascript
const failingPromise = new Promise((resolve, reject) => {
reject("Something went wrong")
})
```


Als we nu `.then()` gebruiken, gebeurt er niets, omdat `.then()` alleen succes behandelt.


Om fouten af te handelen, gebruiken we `.catch()`:


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


Dit drukt alleen


```
Caught an error: Something went wrong
```


De waarde die wordt doorgegeven aan `reject()` wordt naar de `.catch()` functie gestuurd.


Laten we een belofte bouwen die **soms werkt en soms faalt**, gebaseerd op een bepaalde voorwaarde.


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


Nu kunnen we dit aanroepen en beide gevallen afhandelen:


```javascript
checkNumber(5)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Deze afdrukken:


```
Success: Positive number
```


En als we het met een ander nummer proberen:


```javascript
checkNumber(-1)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Het drukt af:


```
Failure: Not a positive number
```


### Operaties aaneenschakelen met `belofte`s



We kunnen ons eerdere voorbeeld herschrijven met `Promise`, en dan ziet het er veel netter uit.


Laten we beginnen met het schrijven van een nieuwe versie van onze verdubbelingsfunctie, maar deze keer geeft hij een **belofte** terug:


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


Nu kunnen we `.then()` gebruiken om JavaScript te vertellen wat het met het resultaat moet doen:


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


Deze afdrukken:


```
Doubled numbers: [ 2, 4, 6 ]
```


Tot nu toe werkt dit hetzelfde als de callback-versie, maar nu is de code eenvoudiger uit te breiden en te lezen.


Laten we zeggen dat we meer stappen willen toevoegen:


1. Verdubbel eerst alle getallen

2. Verwijder vervolgens getallen kleiner dan 4

3. Voeg ze ten slotte allemaal samen


We kunnen een functie schrijven voor elke stap, allemaal met behulp van beloften:


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


Nu kunnen we ze op deze manier aan elkaar **ketenen**:


```javascript
const input = [1, 2, 3]

doubleNumbers(input)
.then(filterBigNumbers)
.then(sumNumbers)
.then(
result => console.log("Final result after all steps:", result)
)
```


Deze afdrukken:


```
Final result after all steps: 10
```


Laten we eens doorlopen wat dit doet:


1. `doubleNumbers` verdubbelt de matrix: `[2, 4, 6]`

2. `filterBigNumbers` verwijdert alles ≤ 3: `[4, 6]`

3. `sumNumbers` telt de resterende getallen op: `4 + 6 = 10`

4. Ten slotte drukken we het resultaat af.


Elke `.then()` wacht tot de stap ervoor is voltooid. We kunnen dus een **keten van acties** bouwen zonder nesting. Dit maakt de code leesbaarder en makkelijker te debuggen.


## Concurrency met `async`/`await`

<chapterId>6e93d29f-c8bf-5fd1-a9c9-4e794ee6cbd0</chapterId>


We hebben gezien hoe `Promise` ketens ons helpen om callback hel te vermijden, maar ze kunnen nog steeds een beetje Hard worden om te lezen als er veel stappen bij betrokken zijn.


Dat is waar `async` en `await` om de hoek komen kijken. Ze laten ons asynchrone code schrijven **die eruit ziet als synchrone code**, wat het makkelijker te begrijpen maakt.


### Wat is `async`?


Als je het sleutelwoord `async` voor een functie schrijft, verpakt JavaScript de retourwaarde van de functie automatisch in een belofte.


Laten we een basisvoorbeeld bekijken:


```javascript
async function greet() {
return "hello"
}
```


Als je deze functie aanroept:


```javascript
const result = greet()
console.log(result)
```


Dit zul je zien:


```
Promise { 'hello' }
```


Ook al heb je zojuist een string geretourneerd, JavaScript maakt er een Promise van. Je kunt de werkelijke waarde krijgen door `.then()` op deze manier te gebruiken:


```javascript
greet().then( result => console.log(result) ) // prints "hello"
```


Of je kunt `await` gebruiken...


### Wat is `wachten`?


Het sleutelwoord `await` vertelt JavaScript: "wacht tot deze belofte is gedaan en geef me dan het resultaat"


Maar je kunt `await` alleen gebruiken **binnen een async functie**.


Laten we het voorbeeld herschrijven met `await`:


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


Nu kunnen we het resultaat gebruiken alsof het een gewone waarde is.


Laten we nu iets nuttigers doen.


### Een vertraging simuleren met `await`


We maken een eenvoudige `wait` functie die een aantal milliseconden als argument neemt en na zoveel milliseconden oplost, zonder iets anders te doen:


```javascript
function wait(ms) {
return new Promise(resolve => {
setTimeout(resolve, ms)
})
}
```


Laten we proberen het te gebruiken:


```javascript
async function test() {
console.log("waiting 2 seconds...")
await wait(2000)
console.log("done waiting")
}

test()
```


Deze afdrukken:


```
waiting 2 seconds...
done waiting
```


Je kunt `await` zien als "pauzeer hier totdat de belofte is gedaan, ga dan verder"


Hierdoor kun je code schrijven op een **top-naar-onder** manier die zich asynchroon gedraagt, zonder `.then()` aanroepen.


### In afwachting van gegevens


Laten we ons vorige voorbeeld herhalen, waar we getallen verdubbelen, dan filteren en dan optellen. Maar deze keer gebruiken we `async`/`await`.


We zullen 3 functies maken die wachten simuleren en Promises teruggeven:


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


Laten we nu een `async` functie schrijven om ze te combineren:


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


Deze afdrukken:


```
Final result: 10
```


Dit is veel eenvoudiger te lezen dan het chainen van `.then()` of het nesten van callbacks.


Het ziet eruit als een normaal stap-voor-stap programma, maar het gedraagt zich nog steeds asynchroon.


## Async Iteratoren

<chapterId>438b037d-9931-56d7-9052-7b4470f3c75b</chapterId>


Je hebt al geleerd over **iterators** en hoe we `for...of` kunnen gebruiken om over arrays en andere iterabele dingen te lussen.


Maar wat als de gegevens die we willen itereren tijd nodig hebben om aan te komen?


Soms willen we lussen over dingen die **asynchroon** aankomen, zoals berichten van een chat, regels uit een bestand of getallen van een langzame bron.


Om dat te doen, geeft JavaScript ons **async iterators**.


### Async generatorfuncties


De eenvoudigste manier om een async iterator te maken is door een **async generator functie** te gebruiken.


We schrijven het als volgt:


```javascript
async function* generateNumbers() {
yield 1
yield 2
yield 3
}
```


Dit lijkt op een gewone generator, maar dan met `async` ervoor.


We kunnen nu `for await...of` gebruiken om de waarden te consumeren:


```javascript
async function run() {
for await (const n of generateNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


Dit wordt afgedrukt:


```
Got number: 1
Got number: 2
Got number: 3
Done!
```


Wat is dan het verschil met een normale generator?


Het verschil is: we kunnen nu `await` gebruiken in de generator.


Laten we opnieuw een vertragingshelper maken:


```javascript
function wait(ms) {
return new Promise(resolve => setTimeout(resolve, ms))
}
```


Laten we nu **langzaam** getallen opleveren:


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


Probeer het te gebruiken:


```javascript
async function run() {
for await (const n of generateSlowNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


### Waarom async iterators gebruiken?


Async iterators zijn nuttig wanneer:



- De waarden komen niet allemaal tegelijk aan.
- Je wilt ze één voor één behandelen, **zoals ze komen**.
- Je werkt met beloften en wilt op een nette manier een lus maken.


Als je bijvoorbeeld berichten van een chatserver één voor één wilt laden, of een groot bestand in brokken wilt downloaden, geven async iterators je een manier om een `for` lus te schrijven die werkt met vertraagde gegevens.


### `symbool.asyncIterator`


We kunnen ook async iterators gebruiken in aangepaste klassen.


Hier is een voorbeeld dat getallen met een vertraging produceert:


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


We kunnen nu `for await...of` gebruiken, net als voorheen:


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


Hiermee kun je objecten maken waar asynchroon overheen kan worden geïtereerd


## Assignment syntaxis suiker

<chapterId>8b1ba7d8-ecfd-5470-b86e-73cb84ccc8b7</chapterId>


"Syntax suiker" betekent iets op een kortere of makkelijkere manier schrijven, zonder te veranderen wat het doet. Het is gewoon een mooiere manier om hetzelfde te zeggen.


JavaScript heeft een aantal ingebouwde syntaxisvariabelen waarmee we schonere en kortere declaraties kunnen schrijven. In dit hoofdstuk bekijken we hoe we waarden kunnen toewijzen op basis van een voorwaarde, variabelen kunnen bijwerken met wiskunde, waarden uit arrays of objecten kunnen halen en ze kunnen kopiëren of combineren met een eenvoudigere syntaxis.


### De Ternary Operator


In JavaScript kun je een waarde toewijzen op basis van een voorwaarde met behulp van de **ternary operator**, wat een korte manier is om `if...else` te schrijven.


In plaats van te doen:


```javascript
let message

if (isMorning) {
message = "Good morning"
} else {
message = "Hello"
}
```


Je kunt schrijven:


```javascript
const message = isMorning ? "Good morning" : "Hello"
```


Dit betekent:



- Als `isMorgen` waar is, gebruik dan `"Goedemorgen"`
- Gebruik anders `"Hallo"`


De algemene vorm is:


```javascript
condition ? valueIfTrue : valueIfFalse
```


Je kunt het ook binnen andere uitdrukkingen gebruiken:


```javascript
console.log(isSunny ? "Go outside" : "Stay in")
```


Zorg ervoor dat je het gebruikt voor **simpele** beslissingen. Als de logica complex is, blijf dan bij `if...else`.


### Alternatieve Assignment Exploitanten


JavaScript heeft **shortcut operators** voor het uitvoeren van opdrachten in combinatie met bewerkingen.


Laten we eens kijken naar de normale manier:


```javascript
let counter = 1
counter = counter + 1
```


Dit kan worden afgekort tot:


```javascript
let counter = 1
counter += 1 // same as counter = counter + 1
```


Hier zijn de meest voorkomende:


| Operator | Meaning             |
| -------- | ------------------- |
| `+=`     | add and assign      |
| `-=`     | subtract and assign |
| `*=`     | multiply and assign |
| `/=`     | divide and assign   |

Voorbeelden:


```javascript
let score = 10
score += 5  // now score is 15
score *= 2  // now score is 30
score -= 10 // now score is 20
```


Deze zijn handig als je een variabele wilt bijwerken met zijn eigen waarde.


### Destructurering


*met *Destructureren** kun je waarden uit arrays of objecten halen en ze eenvoudig opslaan in variabelen.


#### Rijen


Stel dat je dat hebt:


```javascript
const colors = ["red", "green", "blue"]
```


In plaats van te doen:


```javascript
const first = colors[0]
const second = colors[1]
```


Dat kun je doen:


```javascript
const [first, second] = colors
```


Dit wijst toe:



- `eerst` naar `"rood"`
- tweede` naar `"Green"`


Je kunt ook waarden overslaan:


```javascript
const [,, third] = colors
console.log(third) // blue
```


#### Objecten


Je kunt ook waarden uit objecten halen:


```javascript
const user = { name: "Alice", age: 30 }

const { name, age } = user
console.log(name) // Alice
console.log(age)  // 30
```


Als de eigenschap een andere naam heeft dan de variabele die je wilt, kun je deze hernoemen:


```javascript
const { name: username } = user
console.log(username) // Alice
```


Destructureren maakt je code schoner bij het werken met objecten en arrays.


### Syntaxis spreiding


De **spread syntaxis** gebruikt `...` om waarden uit te pakken of te kopiëren.


#### Rijen


Je kunt arrays kopiëren of samenvoegen:


```javascript
const a = [1, 2]
const b = [3, 4]

const both = [...a, ...b]
console.log(both) // [1, 2, 3, 4]
```


Je kunt ook een array klonen:


```javascript
const original = [10, 20, 30]
const clone = [...original]
```


#### Objecten


Je kunt hetzelfde doen met objecten:


```javascript
const a = { x: 1 }
const b = { y: 2 }

const merged = { ...a, ...b }
console.log(merged) // { x: 1, y: 2 }
```


Je kunt ook waarden overschrijven:


```javascript
const user = { name: "Alice", age: 30 }
const updated = { ...user, age: 31 }

console.log(updated) // { name: "Alice", age: 31 }
```


Dit is erg handig bij het bijwerken van objecten zonder het origineel te wijzigen.


# NodeJS

<partId>42fe4d49-dace-5135-bb9e-b9d75034fb2a</partId>


## Hoe kwamen we bij Node

<chapterId>0da1d60c-06c9-54e6-a181-ae7dabf6e3b8</chapterId>


In dit hoofdstuk leren we wat historische context over JavaScript en NodeJS.


Historische context is erg belangrijk bij software, omdat we vaak tools gebruiken die door andere mensen zijn gemaakt en we daarom worden beïnvloed door beslissingen die zij in het verleden hebben genomen.


Als we begrijpen waarom deze beslissingen zijn genomen en hoe de hulpmiddelen die we gebruiken zijn geworden zoals ze zijn, zullen we ons minder verward voelen over wat we doen.


### Oorsprong van JavaScript


JavaScript begon als een eenvoudige taal die was ontworpen om webpagina's interactief te maken.


In de jaren 90 voegden webbrowsers zoals Netscape Navigator JavaScript toe zodat ontwikkelaars code konden schrijven die direct in de browser werd uitgevoerd.


Het oorspronkelijke idee was om Java als kerntaal te gebruiken voor het maken van websites (met de zogenaamde "Java-applets"), en JavaScript alleen voor minder belangrijke dingen.


Het basisontwerp werd in minder dan 2 weken gemaakt door Brendan Eich, die op dat moment bij Netscape werkte.


Maar de meeste mensen gebruikten liever JavaScript dan Java, en Java applets hadden in die tijd ook wat veiligheidsproblemen, dus uiteindelijk werd Java als optie geschrapt en werd JavaScript de de facto standaard voor webontwikkeling.


### De V8-motor


JavaScript is een geïnterpreteerde taal, in tegenstelling tot gecompileerde talen zoals C.


Code die is geschreven in een gecompileerde taal wordt omgezet in een binair getal en het binaire getal wordt rechtstreeks naar de CPU van de computer gestuurd.


![](assets/en/6.webp)


Interpred-talen daarentegen zijn meestal gebruiksvriendelijker en staan dichter bij hoe mensen denken ("hoog niveau") in plaats van hoe machines werken ("laag niveau"); daarom hebben ze meestal een virtuele machine gebouwd om hun code te draaien.


Een virtuele machine is een speciaal programma dat tussen de code die jij schrijft en de CPU zit en jouw code uitvoert (omdat de CPU het niet begrijpt).


Hierdoor kun je programmeren zonder al te veel te weten over de onderliggende machine, maar het heeft ook een prijs in termen van prestaties, omdat de computer niet alleen jouw programma draait; hij draait een programma (de virtuele machine) dat jouw programma draait.


Naarmate webapplicaties complexer werden, ontstond de vraag om de prestaties van JavaScript te verbeteren. De V8-engine is de tolk die JavaScript aanstuurt in Google Chrome. Het is ontwikkeld bij Google en uitgebracht in 2008.


Terwijl de oudere JavaScript-engines meestal traditionele virtuele machines waren, is de V8-engine een JIT (just-in-time) compiler.


De JavaScript-code wordt naar de V8-engine gevoerd en de engine probeert delen ervan te compileren als native binaries. Hierdoor krijg je de ervaring van een high level taal, met prestaties die iets dichter bij low level talen liggen. Dit heeft JavaScript de snelste high level taal ter wereld gemaakt, een beetje een "best of both worlds" ding.


### De NodeJS runtime


Hoewel JavaScript eenvoudig te gebruiken en behoorlijk snel uit te voeren was, bleef het na de release van V8 een enorme beperking houden: het kon alleen in een browser worden uitgevoerd.


Waarom is dat een probleem?


Nou, omdat browsers code uitvoeren die van miljoenen verschillende bronnen op het internet is gehaald, kunnen ze gemakkelijk in malware veranderen, dus zijn ze "sandboxed" van de rest van het besturingssysteem.


![](assets/en/7.webp)


JavaScript had geen toegang tot het bestandssysteem en andere lokale bronnen op je computer (in ieder geval niet zo gemakkelijk als andere talen dat konden), dus dat was een belangrijke beperking voor het soort toepassingen dat je ermee kon bouwen.


In 2009 publiceerde Ryan Dahl NodeJS, een runtime waarmee je de V8 engine buiten de browser kunt gebruiken, direct op het native besturingssysteem van je computer. Het voegt ook veel functies toe die handig zijn voor het schrijven van server-side en commandoregelprogramma's. Je kunt NodeJS bijvoorbeeld gebruiken om een webserver te maken, bestanden te lezen en te schrijven of tools te bouwen die taken automatiseren.


![](assets/en/8.webp)


Tot nu toe hebben we in deze cursus de JavaScript-functies verkend die zowel in de browser als in NodeJS aanwezig zijn. Met deze functies kunnen we gegevens definiëren en op abstracte manieren manipuleren. In de volgende lessen verkennen we de functies die specifiek zijn voor NodeJS en ons in staat stellen om te communiceren met het besturingssysteem.


## Argumenten op de opdrachtregel

<chapterId>960d20f3-c424-5d51-a041-ef17d2e94b6d</chapterId>


Met NodeJS kunnen we onder andere CLI's (Command Line Interfaces) bouwen.


Daarvoor hebben we een manier nodig om commandoregel argumenten te ontvangen, wat in Node wordt gedaan met behulp van het ingebouwde `process` object.


### `proces`


NodeJS biedt een speciaal object genaamd `process` dat het huidige lopende programma vertegenwoordigt.


Je kunt het gebruiken om de omgeving en de huidige werkdirectory te inspecteren en zelfs om het programma af te sluiten wanneer dat nodig is.


Bijvoorbeeld:


```javascript
console.log(process.platform)
```


Dit drukt het platform van het besturingssysteem af, zoals `win32`, `linux`, of `darwin` (Mac).


### `proces.argv`


Wanneer je een NodeJS programma vanaf de terminal uitvoert, kun je extra woorden (argumenten) achter de naam van het script zetten. Deze worden opgeslagen in `process.argv`.


Als je bijvoorbeeld dit commando uitvoert:


```
node my_script.js alpha beta
```


Je kunt de argumenten als volgt afdrukken:


```javascript
console.log(process.argv)
```


De uitvoer kan er als volgt uitzien:


```
[ '/path/to/node', '/path/to/my_script.js', 'alpha', 'beta' ]
```


De eerste twee items zijn altijd het knooppuntpad en je scriptpad. Alle extra woorden die je aan het script hebt doorgegeven komen daarna.


De `process.argv` array kan worden gesneden als elke andere array met behulp van de `.slice()` methode, dus om alleen de argumenten te krijgen die zijn doorgegeven kun je het volgende doen


```javascript
const args = process.argv.slice(2)

console.log(args)
```


Toegang hebben tot de argumenten die de gebruiker doorgeeft is fundamenteel voor het ontwikkelen van commandoregelapplicaties.


## Modules

<chapterId>4e1651a5-65fd-50bc-b22a-40313d5659ca</chapterId>


JavaScript runtimes zoals NodeJS behandelen elk JavaScript-bestand meestal als een aparte module.


Zie een module als een doos. De doos heeft zijn eigen privéruimte, zodat de variabelen en functies die je erin hebt gedeclareerd niet interfereren met de code in andere dozen. In principe heeft elke module zijn eigen bereik.


Een module kan een deel van zijn inhoud exporteren en beschikbaar maken voor andere modules en kan de inhoud importeren die andere modules hebben geëxporteerd. Met JavaScript kunt u inhoud tussen modules exporteren en importeren om verschillende bestanden met elkaar te verbinden.


Een JavaScript-programma bestaat vaak uit meerdere modules die met elkaar verbonden zijn.


Waarom modules gebruiken? Door je code op te delen in modules, kan je je programma organiseren in kleinere, duidelijkere en herbruikbare delen. Elke module kan zich richten op slechts één soort taak, zoals het afhandelen van wiskundige berekeningen, het werken met bestanden of het opmaken van tekst.


### CommonJS modules


In NodeJS heet het meest gebruikte systeem om modules te beheren **CommonJS**.


In dit systeem kun je code van een module delen (exporteren) met `module.exports` en deze in een ander bestand laden (importeren) met `require()`.


Om iets beschikbaar te maken buiten een module, wijs je het toe aan `module.exports`:


```javascript
const greeting = "Hello!"

module.exports = greeting
```


Hier is de string `"Hallo!"` wat deze module exporteert.


Om de geëxporteerde code van een ander bestand te gebruiken, gebruik je de `require()` functie met het pad naar dat bestand:


```javascript
const greeting = require("./greeting.js")

console.log(greeting)
```


Deze afdrukken:


```
Hello!
```


Je kunt meerdere dingen exporteren door ze te bundelen in een anoniem object, zoals


```javascript
const greeting1 = "hello"

const greeting2 = "hi"

module.exports = {
greeting1, greeting2
}
```


CommonJS was het modulesysteem dat in eerste instantie werd overgenomen door NodeJS. Later werden ook ES modules toegevoegd.


### ES-modules


NodeJS ondersteunt ook een ander type module genaamd **ES Modules**, die populair zijn in webontwikkeling. Ze gebruiken de sleutelwoorden `export` en `import`.


ES modules zijn ontwikkeld voor de browser en pas later toegevoegd aan Node. Als je ze wilt gebruiken, moet je misschien `.mjs` als bestandsextensie gebruiken in plaats van `.js`, afhankelijk van welke Node versie je gebruikt.


In een bestand genaamd `greeting.mjs` schrijven we


```javascript
export const greeting = "Hello!"
```

Zoals je kunt zien, exporteren we de constante direct waar hij wordt gedefinieerd


In een ander bestand genaamd `index.mjs` importeren we het:


```javascript
import { greeting } from "./greeting.mjs"

console.log(greeting)
```


Je kunt verschillende declaraties exporteren in verschillende delen van het bestand, zoals


```javascript
export const num = 10

export function double (x) {
return x*2
}
```


### De NodeJS standaardbibliotheek


NodeJS bevat ook veel ingebouwde modules. Dit zijn kant-en-klare modules van NodeJS die helpen bij veelvoorkomende taken, zoals het lezen van bestanden, werken met het besturingssysteem of verbinding maken met het netwerk.


De `os` module geeft je bijvoorbeeld informatie over je besturingssysteem:


```javascript
const os = require("os")

console.log(os.platform())
```


Je hoeft deze ingebouwde modules niet te installeren, ze worden met NodeJS meegeleverd. Ze vormen de "standaardbibliotheek" van de runtime en worden door de meeste Node-applicaties gebruikt om dingen te doen zoals bestanden lezen of communiceren via het internet.


De volgende hoofdstukken tonen je enkele nuttige voorbeelden van hun gebruik.


## De module `fs

<chapterId>911e953a-35ae-5ee7-bd74-372501c32e81</chapterId>


De `fs` module (afkorting voor **file system**) maakt deel uit van de NodeJS standaardbibliotheek. Hiermee kun je werken met bestanden en mappen op je computer: je kunt bestanden lezen, schrijven, verwijderen, hernoemen en meer.


Om het te gebruiken, moet je het eerst bovenaan je bestand importeren:


```javascript
const fs = require("fs")
```


### Synchronisatie-API


De eenvoudigste manier om `fs` te gebruiken is met zijn **sync** methodes.


Deze methodes blokkeren het programma totdat ze klaar zijn (zodat de volgende regel code niet wordt uitgevoerd totdat de bewerking is voltooid).


Hier is een voorbeeld van het synchroon lezen van een bestand:


```javascript
const fs = require("fs")

const data = fs.readFileSync("example.txt", "utf8")

console.log(data)
```


Als er een bestand met de naam `voorbeeld.txt` in dezelfde map staat als je script, dan zal dit de inhoud ervan afdrukken.


Je kunt ook synchroon naar een bestand schrijven:


```javascript
const fs = require("fs")

fs.writeFileSync("output.txt", "Hello from Node!")

console.log("File written!")
```


Dit maakt (of overschrijft) een bestand genaamd `output.txt` met de tekst.


Hier zijn enkele veelvoorkomende bewerkingen die je kunt uitvoeren met deze API:


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


De Sync API is eenvoudig en goed voor kleine scripts, maar omdat het het programma blokkeert totdat het klaar is, kan het dingen vertragen als je met grote bestanden of een server werkt.


### Callback async API


De **callback API** is non-blocking: het laat NodeJS andere dingen blijven doen terwijl de bestandsoperatie plaatsvindt.


In plaats van het resultaat direct terug te geven, neemt het een functie (een **callback**) die wordt aangeroepen wanneer de bewerking klaar is.


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


Dit is wat er gebeurt:



- `fs.readFile` begint met het lezen van `voorbeeld.txt`.
- NodeJS wacht niet, het gaat verder met het uitvoeren van andere code die je misschien hebt geschreven.
- Als het bestand klaar is met lezen, wordt de callback uitgevoerd:



  - Als er een fout is opgetreden, bevat `err` de fout.
  - Anders bevat `data` de inhoud.


Zo schrijf je naar een bestand:


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


Zelfde idee: het programma stopt niet tijdens het schrijven van het bestand.


Enkele voorbeelden van dingen die je met deze API kunt doen:


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


De callback API is beter voor servers en grote taken omdat het het programma niet blokkeert, maar geneste callbacks kunnen rommelig worden als je veel bewerkingen aan elkaar rijgt. Daarom is er een op beloftes gebaseerde async API toegevoegd.


### Belofte async API


De op beloften gebaseerde API is modern en werkt geweldig met `.then()` en `async/await`. Het is beschikbaar als `fs.promises`.


Je moet de eigenschap `beloften` importeren:


```javascript
const fs = require("fs").promises
```


Met `.then()`:


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


Of nog beter, gebruik `async/await`:


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


Schrijven naar een bestand:


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


De gebruikelijke lijst met voorbeelden voor de API:


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


Wanneer je code schrijft, zul je vaak code moeten gebruiken die door andere mensen is geschreven; bijvoorbeeld bibliotheken om je te helpen werken met datums, kleuren, servers of bijna alles.


In plaats van bestanden handmatig te downloaden en te kopiëren, kun je een **packagemanager** gebruiken.


Een pakketbeheerder is een hulpmiddel dat:



- pakketten downloaden
- houdt bij welke pakketten je project nodig heeft
- zorgt ervoor dat iedereen in je team dezelfde versies van de pakketten heeft


### Wat is NPM


In de NodeJS-wereld is de populairste pakketbeheerder **NPM**, wat staat voor *Node Package Manager*.


Je krijgt NPM automatisch wanneer je NodeJS installeert.


Je kunt controleren of je NPM hebt door dit in je terminal uit te voeren:


```
npm -v
```


Dit drukt de versie van NPM af die je hebt, zoals:


```
10.2.1
```


### Een pakket maken


In NodeJS is een **package** gewoon een map met een `package.json` bestand erin.


Laten we er stap voor stap een maken.


1. Maak een nieuwe map voor je project:


```
mkdir my_project
cd my_project
```


2. Voer deze opdracht uit:


```
npm init
```


Dit start een interactieve opstelling, waarbij je vragen krijgt zoals de naam van je project, versie, beschrijving, enz.


Als je niet op alles wilt antwoorden en gewoon de standaardinstellingen wilt accepteren, kun je dit gebruiken:


```
npm init -y
```


Nadat je het hebt uitgevoerd, zie je een nieuw bestand in je map met de naam:


```
package.json
```


### `package.json`


Het `package.json` bestand is gewoon een JSON bestand dat metadata over je project opslaat.


Hier is een voorbeeld:


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


Een paar belangrijke velden:



- `naam`: de naam van je pakket
- `version`: de huidige versie
- `main`: het ingangspuntbestand (zoals `index.js`)
- `scripts`: commando's die je kunt uitvoeren (zoals `npm start`)
- `dependencies`: toont alle pakketten waarvan je project afhankelijk is


### Een pakket installeren


Laten we zeggen dat je een bepaald pakket genaamd `picocolors` wilt gebruiken om kleuren toe te voegen aan je terminaluitvoer.


Je kunt het installeren door uit te voeren:


```
npm install picocolors
```


Je kunt het nu gebruiken in je project. Maak een `index.js` bestand met


```javascript
const pico = require('picocolors')

console.log(
pico.green("This text is green!")
)
```


en probeer het uit te voeren. De terminal zou een gekleurde versie van de tekst moeten afdrukken.


Wat heeft de NPM gedaan?



- Het heeft het pakket gedownload en opgeslagen in een submap genaamd `node_modules/`
- het voegde een item toe onder `afhankelijkheden` in uw `package.json`
- het heeft het `package-lock.json` bestand bijgewerkt


Wat is `package-lock.json`?


### `pakket-slot.json`


Dit bestand wordt automatisch aangemaakt door NPM.


Je vraagt je misschien af, als we `package.json` al hebben, waarom hebben we dan nog een bestand nodig?

Dit is de reden:



- `package.json` zegt alleen welke versie **bereik** van een pakket je project nodig heeft.

Voorbeeld:


```json
"dependencies": {
"picocolors": "^1.1.0"
}
```


De `^1.1.0` betekent "elke versie die compatibel is met 1.1.x", dus het is flexibel.



- `package-lock.json` **bevriest** de exacte versies van elk pakket en hun sub-dependencies, zodat iedereen die je project installeert exact dezelfde werkende setup krijgt.


Waarom is dit belangrijk?


Als je in een team werkt, of je implementeert je project op een server, of je komt er in de toekomst op terug, dan wil je er zeker van zijn dat het nog steeds op dezelfde manier werkt.

Als de pakketten zijn bijgewerkt en je installeert opnieuw zonder een lock-bestand, dan krijg je misschien een iets andere versie die zich anders gedraagt.


Door de `package-lock.json` in je project te houden, zal NPM altijd de exacte versies installeren die daar vermeld staan, en ervoor zorgen dat iedereen dezelfde omgeving heeft.


`package-lock.json` vergrendelt alles tot een zeer specifieke versie, om het project beter reproduceerbaar te maken op andere machines.


Maar als je pakket door veel mensen gebruikt moet worden, zou je er in plaats daarvan voor kunnen kiezen om het niet vast te leggen, zodat NPM alleen het `package.json` bestand vindt en automatisch de laatste versies installeert die in dat bestand zijn toegestaan.


Maar dit zijn dingen waar je je later zorgen over moet maken, zodra je je eigen code begint te publiceren. Voor nu hebben we de basisprincipes van NPM geïntroduceerd, zodat je de bibliotheken die door andere ontwikkelaars zijn gepubliceerd, kunt vinden en gebruiken in je projecten.



## Netwerken in NodeJS

<chapterId>f2cabd8b-754b-5c97-8d6a-8412a9a184c7</chapterId>


NodeJS wordt vaak gebruikt als een taal voor backend: je kunt van je script een server maken en er ook verzoeken mee doen aan andere servers.


In dit hoofdstuk introduceren we enkele basis netwerkfuncties waarmee je dat kunt doen.


### `fetch()`


Als je wilt dat je programma gegevens download van een website of een API, dan moet je een **HTTP verzoek** doen.


In moderne versies van NodeJS kun je de ingebouwde `fetch()` functie gebruiken.


Hier is een voorbeeld van een GET-verzoek aan een API:


```javascript
const response = await fetch("https://jsonplaceholder.typicode.com/posts/1")
const data = await response.text()

console.log(data)
```


Als je dit uitvoert, zie je iets als:


```
{
"userId": 1,
"id": 1,
"title": "...",
"body": "..."
}
```


Dit is wat er gebeurt:


1. `fetch()` neemt een URL en doet een aanvraag.

2. Het retourneert een **Promise** dat resolved naar een `Response` object.

3. `response.text()` leest de inhoud van het antwoord als een tekenreeks.


Maar de string die je terugkrijgt is eigenlijk JSON. Wat is dat?


### JSON


Bij het werken met web-API's worden de gegevens vaak verzonden en ontvangen als **JSON**, wat staat voor JavaScript Object Notation.


JSON is gewoon een tekstindeling die veel lijkt op JavaScript-objecten. Bijvoorbeeld:


```json
{
"name": "Alice",
"age": 30,
"likes": ["apples", "bananas"]
}
```


Het `JSON` object is een ingebouwd hulpprogramma in JavaScript dat kan worden gebruikt om met deze gegevensindeling te werken.


Je kunt een JavaScript-object converteren naar een JSON-string met `JSON.stringify()`:


```javascript
const user = { name: "Alice", age: 30 }

const jsonString = JSON.stringify(user)

console.log(jsonString)
```


Deze afdrukken:


```
{"name":"Alice","age":30}
```


Je kunt JSON tekst ook terug converteren naar een JavaScript object met `JSON.parse()`:


```javascript
const jsonText = '{"name":"Bob","age":25}'

const obj = JSON.parse(jsonText)

console.log(obj)
```


Deze afdrukken:


```
{ name: 'Bob', age: 25 }
```


Wees voorzichtig: `JSON.parse()` geeft een fout als de string geen geldige JSON is.


```javascript
JSON.parse("not json") // ❌ Error!
```


Zorg er dus voor dat de string goed geformatteerd is.


### `http` server


Met NodeJS kun je een webserver maken zonder iets anders te installeren.


Je kunt de ingebouwde `http` module gebruiken om verzoeken van clients af te handelen en antwoorden terug te sturen.


Hier is een heel eenvoudig voorbeeld:


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


Als je dit script uitvoert en `http://localhost:3000` in je browser opent, zie je het volgende:


```
Hello from NodeJS server!
```


Dit is wat er gebeurt in de code:


1. Je hebt de `http` server geïmporteerd uit de Node standaardbibliotheek.

2. `http.createServer()` maakt een server aan. Je hebt aan `http.createServer()` een callback `(req, res) => {...}` doorgegeven die elke keer wordt uitgevoerd als iemand verbinding maakt.

3. Je hebt een statuscode van 200 (die een succesvolle bewerking aangeeft) toegewezen aan het antwoord. U kunt hier meer lezen over http-statuscodes (https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

3. `res.end()` verstuurt het antwoord en beëindigt de verbinding.

4. `server.listen(3000)` start de server op poort 3000.


Je kunt ook `req.url` en `req.method` in het verzoek aanvinken om verschillende paden of verzoektypes te behandelen.


Voorbeeld met routing:


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


Dit zijn erg eenvoudige voorbeelden. Voor het bouwen van meer geavanceerde servers zouden de meeste ontwikkelaars waarschijnlijk een kant-en-klare backend bibliotheek downloaden zoals [express](https://www.npmjs.com/package/express).


## Gegevens verwerken: buffers, gebeurtenissen, streams

<chapterId>8c9623f0-a604-51a4-8fe4-871c849d3e3b</chapterId>


In dit hoofdstuk introduceren we voornamelijk drie klassen van objecten:



- `Buffer`, die kleine brokken binaire gegevens weergeeft
- `EventEmitter`, die kan worden gebruikt om een stap per asynchroon proces te volgen door signalen uit te zenden die "events" worden genoemd
- `Stream`, waarmee we grote hoeveelheden gegevens één `Buffer` per keer kunnen verwerken, en die het proces bijhoudt door gebeurtenissen uit te zenden


Deze zijn zeer gebruikelijk in professionele NodeJS code, dus zelfs als je ze misschien niet gebruikt in je eerste projecten, is het goed om een basiskennis te krijgen voor wanneer je ermee moet werken. van hen


### Buffers


In NodeJS is een **buffer** een type object dat wordt gebruikt om te werken met binaire gegevens.


Je kunt een buffer zien als een container met een vaste grootte voor ruwe bytes.


Zo maak je een buffer van een string:


```javascript
const buf = Buffer.from("hello")
console.log(buf)
```


Dit drukt iets af als:


```
<Buffer 68 65 6c 6c 6f>
```


Deze getallen (`68`, `65`, `6c`, etc.) zijn hexadecimale representaties van de letters in `"hello"`.


Je kunt het op deze manier terug converteren naar een tekenreeks:


```javascript
console.log(buf.toString())
```


Deze afdrukken:


```
hello
```


Je kunt ook een buffer van een bepaalde grootte maken, gevuld met nullen:


```javascript
const buf = Buffer.alloc(10)
console.log(buf)
```


Dit drukt iets af als:


```
<Buffer 00 00 00 00 00 00 00 00 00 00>
```


U kunt in de buffer schrijven:


```javascript
buf.write("abc")
console.log(buf)
```


En je hebt toegang tot individuele bytes:


```javascript
console.log(buf[0]) // prints the ASCII number for 'a', which is 97
```


Buffers zijn vooral handig als je gegevens op een heel laag niveau moet manipuleren.


### Evenementen


In JavaScript is een **event** iets dat gebeurt in je programma waarop je kunt reageren.


Bijvoorbeeld:



- een bestand wordt geladen
- een timer gaat af
- een gebruiker klikt op een knop
- een netwerkverzoek retourneert gegevens


Een **event** is gewoon een signaal dat er iets is gebeurd en je kunt code schrijven om naar die events te luisteren en erop te reageren.


In NodeJS kunnen veel objecten gebeurtenissen uitzenden. Deze objecten worden **EventEmitters** genoemd.


Hier is een voorbeeld:


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


Deze afdrukken:


```
Hello! An event happened.
```


Dit is wat:


1. We maken een `EventEmitter` object.

2. We vertellen het om een callback uit te voeren wanneer de `"begroet"` gebeurtenis plaatsvindt, met behulp van `.on("begroet")`.

3. Later triggeren we de `"begroet"` gebeurtenis met `.emit()`.

4. Onze callback wordt uitgevoerd


Je kunt gegevens doorgeven samen met de gebeurtenis:


```javascript
emitter.on("greet",
(name) => console.log(`Hello, ${name}!`)
)

emitter.emit("greet", "Alice") // first argument is the type of event, second argument is the data we pass with this event
```


Deze afdrukken:


```
Hello, Alice!
```


Je kunt ook luisteraars registreren voor andere gebeurtenissen:


```javascript
emitter.on("goodbye", () => {
console.log("Goodbye!")
})

emitter.emit("goodbye")
```


Je kunt zoveel luisteraars als je wilt aan een type gebeurtenis koppelen, en je kunt veel verschillende typen gebeurtenissen afvuren vanuit dezelfde emitter.


Veel objecten in NodeJS zenden events uit om de rest van het programma te vertellen dat er iets gebeurt.



### Wat zijn stromen?


Streams combineren buffers en gebeurtenissen om ons te helpen gegevens te verwerken.


Wanneer we werken met bestanden, gegevens van het netwerk of zelfs lange tekst, hoeven (of willen) we niet altijd alles in één keer in het geheugen laden. Dat kan traag zijn of zelfs het programma laten crashen als de gegevens te groot zijn.


In plaats daarvan kunnen we de gegevens **beetje bij beetje** verwerken, terwijl ze binnenkomen of gelezen worden, een beetje zoals water drinken door een rietje in plaats van proberen het hele glas in één keer leeg te drinken. Dit wordt een **stroom** genoemd.


In NodeJS is een stream een object waarmee je gegevens van een bron kunt lezen of gegevens naar een bestemming kunt schrijven **een stukje per keer**.


NodeJS heeft vier hoofdtypen streams:



- Leesbaar**: streams waarvan je gegevens kunt lezen (zoals het lezen van een bestand)
- Writable**: streams waar je gegevens naar kunt schrijven (zoals naar een bestand)
- Duplex**: streams die zowel leesbaar als beschrijfbaar zijn
- Transformeer**: zoals duplex streams, maar ze kunnen de gegevens veranderen (transformeren) terwijl ze stromen


### Leesbare streams


Laten we zeggen dat je een `bigfile.txt` hebt om te verwerken. Je kunt een leesbare stream maken met de `fs` module om het bestand stuk voor stuk te lezen.


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


Wat gebeurt hier?


1. `fs.createReadStream()` maakt een leesbare stream.

2. Wanneer een stuk van het bestand klaar is, zendt de stream een `data` event uit en geeft ons een "brok" data (een `Buffer`). We drukken de brok af.

3. Als het hele bestand is gelezen, wordt de `end` gebeurtenis geactiveerd.

4. Als er een fout optreedt (zoals het bestand dat niet bestaat), wordt de gebeurtenis `error` geactiveerd.


Op deze manier kun je gigantische bestanden lezen zonder ze allemaal tegelijk in het geheugen te laden.


Als we willen dat de gegevens in een voor mensen leesbare vorm aankomen (in plaats van binair), kunnen we de codering van de stroom opgeven:


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


De code drukt nu het bestand af in een voor mensen leesbare vorm.


### Beschrijfbare streams


Met een beschrijfbare stream kun je gegevens ergens naartoe sturen, brok voor brok.


Hier is een voorbeeld van het schrijven naar een `target.txt` bestand met behulp van een stream:


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


Dit is wat er gebeurt:


1. `fs.createWriteStream()` maakt een schrijfbare stream.

2. We schrijven er tekst naartoe met `.write()`.

3. Als we klaar zijn, roepen we `.end()` op om de stream te sluiten.

4. Als alle gegevens zijn geschreven, wordt de `finish` gebeurtenis uitgezonden.

5. Als er iets fout gaat, wordt de gebeurtenis `error` geactiveerd.


Net als leesbare streams zijn schrijfbare streams goed voor grote gegevens omdat ze niet alles tegelijk in het geheugen hoeven te bewaren.


### Leidingstromen


Een van de coolste dingen van streams is dat je ze aan elkaar kunt **pijpen**: een leesbare stream direct verbinden met een schrijfbare stream.


```javascript
const fs = require("fs")

const readable = fs.createReadStream("bigfile.txt")
const writable = fs.createWriteStream("target.txt")

readable.pipe(writable)
```


Hier:



- De leesbare stream leest van `bigfile.txt`.
- De schrijfbare stream schrijft naar `copy.txt`.
- `.pipe()` stuurt de gegevens rechtstreeks van de leesbare naar de schrijfbare stream.


### Duplex stromen


Een duplex stream is zowel leesbaar als beschrijfbaar. Een voorbeeld is een netwerk socket: je kunt er gegevens naar toe sturen en er gegevens van ontvangen.


Hier is een heel eenvoudig voorbeeld dat de `net` module gebruikt:


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


In dit voorbeeld:



- Het `socket` object is een duplex stream.
- Je kunt er naar `schrijven()` en ook luisteren naar `data` gebeurtenissen.


### Stromen transformeren


Een transform stream is een duplex stream die ook de gegevens wijzigt die er doorheen gaan.


Je kunt bijvoorbeeld de ingebouwde `zlib` module gebruiken om gegevens te comprimeren of decomprimeren.


Zo comprimeer je een bestand met behulp van een transform stream:


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


En om het terug te decomprimeren:


```javascript
const readable = fs.createReadStream("bigfile.txt.gz")
const unzip = zlib.createGunzip()
const writable = fs.createWriteStream("bigfile.txt")

readable.pipe(unzip).pipe(writable)

writable.on("finish", () => {
console.log("File decompressed.")
})
```


Transform streams zijn erg handig voor taken zoals compressie, encryptie of het veranderen van bestandsformaten tijdens het streamen.


### Tegendruk


Soms is een schrijfbare stream traag in het verwerken van gegevens. Als we gegevens sneller naar een beschrijfbare stream blijven pushen dan deze aankan, kunnen we in de problemen komen. Dit wordt **backpressure** genoemd.


Als je de `.write()` methode aanroept op een schrijfbare stream, retourneert deze een boolean die je informeert of de stream een pauze nodig heeft; het kan zijn dat je de retourwaarde moet controleren, zoals dit:


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


Dit was een illustratief voorbeeld van het handmatig leiden van gegevens van een Readable naar een Writable en het handmatig beheren van de tegendruk.


Normaal gesproken pijpen we gegevens met de `.pipe()` methode, die automatisch tegendruk verwerkt.


Je hoeft je dus alleen zorgen te maken over tegendruk als je om de een of andere reden handmatig `.write()` aanroept.


## Eindnoot

<chapterId>139e2ab8-df67-525a-85f0-5a2fa5e478f2</chapterId>


Zo, dat was het, als je de lessen hebt gevolgd, zou je nu enkele eenvoudige programma's in NodeJS moeten kunnen schrijven.


Ik stel voor om precies dat te doen: na het leren van de basis is het bouwen van een paar persoonlijke projecten de beste manier om te oefenen en een betere programmeur te worden.


Het maakt niet echt uit wat je bouwt, waar het om gaat is dat je jezelf uitdaagt om problemen op te lossen met code.


Moderne programmeertalen zijn ongelooflijk krachtig en NodeJS is waarschijnlijk de beste gereedschapskist om mee te experimenteren in deze fase van je reis.


Veel succes!


# Laatste deel


<partId>322624d8-6fbc-11f0-a67a-5b145f10afc1</partId>


## Beoordelingen


<chapterId>3e93ac86-6fbc-11f0-8bae-9b2ed7914843</chapterId>

<isCourseReview>true</isCourseReview>

## Conclusie


<chapterId>49b3b9b2-6fbc-11f0-9870-5f5adcd3a0eb</chapterId>


<isCourseConclusion>true</isCourseConclusion>