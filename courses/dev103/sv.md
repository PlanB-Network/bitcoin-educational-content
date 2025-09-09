---
name: Grundläggande JavaScript och NodeJS
goal: Lär dig grunderna i JavaScript-programmering och NodeJS-utveckling för att bygga praktiska applikationer och verktyg.
objectives: 

  - Behärska grundläggande JavaScript-syntax, -typer och -kontrollflöde
  - Förstå funktioner, objekt och klasser i JavaScript
  - Lär dig tekniker för felhantering och felsökning
  - Få en introduktion till NodeJS och dess ekosystem

---

# Börja din utvecklingsresa


Välkommen till denna kurs i JavaScript och NodeJS.


JavaScript är det mest populära programmeringsspråket i världen: det är skriptspråket i moderna webbläsare, så det är i princip omöjligt att bygga en modern webbapplikation utan att skriva *något* JavaScript; och med NodeJS runtime kan det användas utanför webbläsare också, för att skapa skript och applikationer som körs direkt på din dator.


Kursen vänder sig till dig som är helt nybörjare inom programmering eller som har använt andra språk tidigare men vill förstå hur JavaScript fungerar, särskilt i samband med NodeJS.


I slutet av kursen ska du kunna skriva egna program i JavaScript, använda NodeJS standardbibliotek samt installera och använda tredjepartspaket för att bygga användbara verktyg.


+++
# Grundläggande JavaScript

<partId>a617327c-e5a2-52ca-9380-c63f44623dd4</partId>


## Inställning

<chapterId>ba05a290-1782-5268-87c9-62fd09590e05</chapterId>


I det här avsnittet ska vi ställa in vår maskin så att vi kan skriva och köra vårt första JavaScript-program.


Ett JavaScript-program är bara en samling av (en eller flera) textfiler som innehåller kommandon som ska utföras av en JavaScript-körtid.


Namnen på dessa textfiler slutar vanligtvis med filändelsen `.js`, t.ex. `my_script.js`, `my_program.js` etc.


De kommandon som de innehåller är skrivna i programmeringsspråket JavaScript.


En JavaScript-körtid är ett speciellt program som kör dessa filer.


![](assets/en/1.webp)


### Installation av NodeJS


Den vanligaste JavaScript-körtiden är NodeJS.


Du kan installera det genom att följa de [officiella instruktionerna] (https://nodejs.org/en/download).


På nedladdningssidan finns instruktioner för alla de tre stora OS:en (operativsystemen): Windows, Linux och MacOS. Det förutsätter att du vet hur man öppnar en terminal i ditt operativsystem.


Eftersom NodeJS är tillgängligt för alla tre operativsystemen kommer de program som du skriver att kunna köras på dem alla (med undantag för vissa marginalfall).


Det innebär att du t.ex. kan skriva ett enkelt videospel i JavaScript på din Windows-dator och skicka det till din vän som kör det på sin Mac.


![](assets/en/2.webp)


### Textredigering


En av de häftiga sakerna med programmering är att du kan skriva kod med vilken textredigerare som helst, till och med standardanteckningsblocket i ditt operativsystem.


Det finns dock vissa texteditorer som är specialiserade på att skriva kod, vissa är tillgängliga gratis, andra kräver att du betalar för en licens.


Valet av kodredigerare är ett gigantiskt kaninhål som överskrider omfattningen av denna kurs, så vi kommer inte att prata om det här. Om du inte vet vad du ska använda är den mest använda gratisredigeraren [VSCode] (https://code.visualstudio.com/).


Dess Interface är lite uppblåst, men det har vad du behöver: en filredigerare, en filutforskare (för att visualisera filerna och underkatalogerna i den katalog du arbetar med) och en terminal för att köra din kod. Det stöder också en hel del plugins, och det levereras med JavaScript syntaxmarkering som standard.


Om du vill vara lite mer Cypherpunk-aktig kan du använda [VSCodium](https://vscodium.com/) istället.


### Första programmet (hello world)


När man studerar ett programmeringsspråk brukar det första programmet man skriver bestå i att skriva ut "hello world!" till konsolen.


Skapa en katalog som heter `my_js_code/`, med en fil som heter `main.js` (dessa namn är godtyckliga).


Öppna katalogen med VSCode.


Skriv in den här koden i din fil:


```javascript
console.log("hello world!")
```


Öppna en terminal och kör det här kommandot för att köra programmet:


```
node main.js
```


Resultatet bör vara


```
hello world!
```


### Vad hände?


I JavaScript är allt ett "objekt".


`console` är ett objekt som används för att felsöka programmet.


`console.log` är den mest använda metoden i `console`. Den skriver bara ut de argument som du skickar till den.


Du skickar argument till `console.log` med hjälp av de runda parenteserna `()`.


Så om du till exempel vill skriva ut talet `1000`, skriver du bara


```javascript
console.log(1000)
```


Exekvera sedan genom att köra


```
node main.js
```


i terminalen (från och med nu kommer kursen att utgå från att du vet att det är så här du kör ett program).


Detta ska skrivas ut


```
1000
```


Du kan skicka flera saker, t.ex


```javascript
console.log(16, 8, 1993)
```


Detta kommer att skriva ut


```
16 8 1993
```


## Variabler och kommentarer

<chapterId>23050ab7-343b-5edf-9d37-e4e782e27ce0</chapterId>


Program utför vanligtvis operationer på data.


Variabler är som namngivna lådor som vi använder för att lagra data. De gör det möjligt för oss att associera en bit data med ett specifikt namn, så att vi senare kan hämta den med hjälp av det namnet.


### `let`-deklarationer


För att deklarera en variabel i JavaScript kan vi använda nyckelordet `let`.


Efter att ha skrivit `let` skriver vi det namn vi vill ge variabeln, sedan ett `=`-tecken och sedan det värde vi vill lagra.


Till exempel:


```javascript
let age = 25

console.log(age)
```


Namnet på en variabel (tekniskt kallad "identifierare") kan vanligtvis innehålla bokstäver, understreck (`_`), dollartecken (`$`) och siffror, även om det första tecknet inte får vara en siffra.


I koden ovan deklarerade vi en variabel som heter `age` och lagrade värdet `25` i den.


Sedan skrev vi ut värdet med hjälp av `console.log(age)`.


Om du kör den här koden med `node main.js`, kommer utdata att vara:


```
25
```


Identifierare är skiftlägeskänsliga, vilket innebär att små och stora bokstäver räknas som skillnader i identifierare, så till exempel


```javascript
let age = 25

let Age = 20

console.log(age)
```


kommer att skriva ut 25, eftersom de betraktas som två helt separata variabler!


Du kan också lagra strängar (text) i en variabel:


```javascript
let message = "hello again"

console.log(message)
```


Detta kommer att skrivas ut:


```
hello again
```


Precis som tidigare använde vi `console.log()` för att skriva ut det värde som lagrats i variabeln.


Låt oss nu göra båda tillsammans:


```javascript
let age = 25

let message = "hello again"

console.log(age)

console.log(message)
```


Om du kör detta kommer det att skrivas ut:


```
25
hello again
```

### Omfördelning


Variabler som deklareras med `let` kan ändras efter att de har skapats.


Detta kallas för omplacering.


```javascript
let score = 10

console.log(score)

score = 15

console.log(score)
```


Först tilldelar vi `10` till `score` och skriver sedan ut det.


Sedan ändrar vi värdet på `score` till `15` och skriver ut det igen.


Utgången kommer att vara:


```
10
15
```


Detta är mycket användbart när värdet ändras över tid, som i ett spel där poängen ökar.


Låt oss lägga till ytterligare en variabel i mixen:


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


Detta kommer att skrivas ut:


```
10
Alice
20
Bob
```


Som du kan se har både `score` och `player` ändrats.


### `const`-deklarationer


För det mesta vill vi dock inte att en variabel ska ändras efter att den har skapats. För det använder vi `const`.


`const` är en förkortning för "konstant". När du har tilldelat ett värde till en `const`-variabel kan du inte ändra det.


```javascript
const pi = 3.14
console.log(pi)
```


Detta skriver ut:


```
3.14
```


Men om du försöker göra det här:


```javascript
const pi = 3.14
console.log(pi)

pi = 99 // this line will cause an error
console.log(pi)
```


JavaScript kommer att ge dig ett felmeddelande som:


```
TypeError: Assignment to constant variable.
```


Detta beror på att `pi` deklarerades med `const`, och du kan inte ändra dess värde efter det. Du kommunicerar till JavaScript-tolken att du inte vill att den variabeln ska ändras.


Detta är användbart eftersom det minskar risken för att ändra den av misstag. När program blir mycket stora, med tusentals rader kod, är det omöjligt att hålla jämna steg med allt som händer samtidigt (det är den främsta anledningen till att vi använder datorer, för att utföra komplexa processer som vi inte kan beräkna med våra hjärnor), så det blir användbart att ha begränsningar som detta, som gör programmet mer deterministiskt.


Det anses vara bästa praxis att alltid deklarera våra värden som `const`, såvida vi inte är säkra på att vi vill ändra dem senare.


### Kommentarer i JavaScript


Ibland vill vi skriva anteckningar i vår kod som inte exekveras. Dessa kallas för kommentarer.


Kommentarer ignoreras av programmet när det körs, men är användbara för att förklara saker för oss själva eller andra.


Om du vill skriva en kommentar på en rad använder du `//`


```javascript
// This is a comment
const x = 10 // This is also a comment
console.log(x)
```


Detta kommer fortfarande att skrivas ut:


```
10
```


Kommentarerna finns bara där för att människor ska kunna läsa dem.


Du kan också skriva kommentarer på flera rader med hjälp av `/*` och `*/`


```javascript
/*
This is a multi-line comment.
It can span several lines.
*/
const y = 20
console.log(y)
```


Detta kommer att skriva ut


```
20
```


Och kommentaren kommer att ignoreras.


Du kan använda kommentarer för att lägga till små anteckningar i din kod, så att du kanske kommer ihåg vad den gör och varför den är skriven på ett visst sätt. Det kan också hjälpa andra programmerare att förstå den.


## Grundläggande typer: tal, strängar, booleaner

<chapterId>cfdb04f6-21a8-5143-bbf9-7aaae04962f0</chapterId>


I JavaScript anger en "typ" vilken typ av data ett värde är.


Javascript har några grundläggande typer, och i det här avsnittet ska vi utforska några av dem.


### Tal och aritmetiska operationer


Den första typen vi ska introducera är `number`.


Tal i JavaScript kan vara heltal (som `5`) eller decimaltal (som `3,14`).


Du kan räkna med dem: addition, subtraktion, multiplikation och division.


Här är ett grundläggande exempel:


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


Detta kommer att skrivas ut:


```
15
5
50
2
```


Du kan också använda parenteser `()` för att styra ordningen på operationerna:


```javascript
const result = (2 + 3) * 4
console.log(result)
```


Detta skriver ut:


```
20
```


Utan parenteserna skulle det vara `2 + 3 * 4`, vilket är:


```javascript
const result = 2 + 3 * 4
console.log(result)
```


Det skulle skriva ut:


```
14
```


I vanlig matematik sker nämligen multiplikation före addition.


### Strängar och interpolation


Den andra JavaScript-typen vi ska introducera är `string`.


Strängar är textstycken. Du kan använda enkla citattecken `'...'` eller dubbla citattecken `"...'` för att skapa dem.


```javascript
const greeting = "hello"
const name = 'Bob'
console.log(greeting)
console.log(name)
```


Detta skriver ut:


```
hello
Bob
```


För att kombinera strängar kan du använda operatorn `+`:


```javascript
const greeting = "hello"
const space = " "
const name = "Bob"

const fullGreeting = greeting + space + name
console.log(fullGreeting)
```


Detta kommer att skrivas ut:


```
hello Bob
```


Men det finns ett trevligare sätt att kombinera strängar som kallas **stränginterpolation**. Du använder backticks för att deklarera strängen `` `...` `` och skriver variabler med `${...}` inuti strängen:


```javascript
const greeting = "hello"
const name = "Bob"

const fullGreeting = `${greeting} ${name}`
console.log(fullGreeting)
```


Detta skrivs också ut:


```
hello Bob
```


Du kan inkludera vilket uttryck som helst inuti `${...}`:


```javascript
const age = 30
console.log(`Next year, I will be ${age + 1} years old.`)
```


Detta skriver ut:


```
Next year, I will be 31 years old.
```


Interpolation är mycket vanligt i modern JavaScript.


### Booleaner, jämförelser och logiska operationer


Den tredje typen vi ska introducera är `boolean`. Den är uppkallad efter matematikern George Boole, som uppfann den booleska logiken.


Booleaner är enkla: bara två möjliga värden, `true` och `false`.


Du kan lagra dem i variabler:


```javascript
const theSkyIsBlue = true
const thisCourseIsBad = false

console.log(theSkyIsBlue)
console.log(thisCourseIsBad)
```


Detta skriver ut:


```
true
false
```


Du kan kombinera booleaner med hjälp av logiska operatorer:



- `&&` betyder "och", och den returnerar "sant" endast om **båda** värdena är "sanna", annars returnerar den "falskt
- `||` betyder "eller", och det kommer att returnera `true` om **mindst ett** av värdena är `true`, annars (om de båda är falska) kommer det att returnera `false`
- `!` betyder "inte", det används före en boolean och vänder på det: om booleanen är "sann" kommer den att returnera "falsk" och vice versa.


![](assets/en/3.webp)


Exempel på detta:


```javascript
const isSunny = true
const isWarm = true

console.log(isSunny && isWarm)  // true
console.log(isSunny || isWarm)  // true
console.log(!isSunny)           // false
```


Du kan jämföra värden i JavaScript med hjälp av operatorer som `>`, `<`, `===` och `!==`. Resultatet av dessa jämförelser är alltid en boolean.


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


Javascript har också `>=` för att betyda "större eller lika" och `<=` för att betyda "mindre eller lika".


Booleska, jämförande och logiska operatorer kombineras ofta i program för att deklarera komplexa villkor, som att säkerställa "e-postmeddelandet har anlänt OCH det innehåller den bild jag behöver ELLER e-postmeddelandets längd är längre än 10000 tecken". Du kommer senare att upptäcka att dessa är viktiga byggstenar för att konstruera logiken i programmet.


## Arrayer, null, odefinierad

<chapterId>7bf18183-5eae-53ed-83d2-b04982145d81</chapterId>


I det här avsnittet går vi igenom ytterligare tre typer som är mycket vanliga i JavaScript-program:



- Arrayer**: sekvenser av värden
- undefined**: ett speciellt värde som betyder "ingenting tilldelades"
- null**: ett annat specialvärde som betyder "avsiktligt tom"


### Arrayer och indexåtkomst


En **array** är en typ som kan innehålla flera värden i en lista.


Du skapar en array genom att använda hakparenteser `[]` och separera objekten med kommatecken.


Här är ett grundläggande exempel:


```javascript
const numbers = [10, 2, 88]
console.log(numbers)
```


Detta skriver ut:


```
[ 10, 2, 88 ]
```


Du kan lagra vad som helst i en array, inte bara siffror:


```javascript
const things = ["apple", 42, true]
console.log(things)
```


Detta skriver ut:


```
[ 'apple', 42, true ]
```


För att komma åt ett specifikt objekt i matrisen använder vi ett **index**. Indexet är positionen för objektet, med början från **0**.


Så i den här uppställningen:


```javascript
const colors = ["red", "green", "blue"]
```



- `färger[0]` är `"röd"`
- `färger[1]` är `"Green"`
- `färger[2]` är `"blå"`


Låt oss försöka:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[0])
console.log(colors[1])
console.log(colors[2])
```


Detta kommer att skrivas ut:


```
red
green
blue
```


Du kan tilldela ett värde till ett specifikt index i en matris


```javascript
const colors = ["red", "green", "blue"]

colors[1] = "yellow"

console.log(colors)
```


Detta kommer att skrivas ut:


```
[ 'red', 'yellow', 'blue' ]
```


Du kan använda vilket naturligt tal som helst som index, även ett som är lagrat i en variabel


```javascript

const i = 1
const colors = ["red", "green", "blue"]
console.log(colors[i])
```


Detta kommer att skrivas ut:


```
green
```


Men om du försöker komma åt ett index som inte finns, får du `undefined`:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[3])
```


Detta skriver ut:


```
undefined
```


Vad är det där?


### `undefinierad`


Specialvärdet "odefinierad" betyder "inget värde har tilldelats".


Om du skapar en variabel men inte ger den något värde blir den "odefinierad":


```javascript
const name
console.log(name)
```


Detta skriver ut:


```
undefined
```


Eftersom vi inte har tilldelat något till `name`, sätter JavaScript det till `undefined` som standard.


Som vi sett tidigare kan du också få `undefined` när du kommer åt ett arrayindex som inte existerar:


```javascript
const fruits = ["banana", "apple"]
console.log(fruits[2]) // There is no index 2
```


Detta skriver ut:


```
undefined
```


### `null` och hur man behandlar det


`null` är också ett speciellt värde. Det betyder "här finns ingenting, och det gjorde jag med flit"


Till skillnad från `undefined`, som är automatisk, är `null` något du själv ställer in.


Till exempel:


```javascript
const currentUser = null
console.log(currentUser)
```


Detta skriver ut:


```
null
```


Varför använda `null`? Du kanske förväntar dig ett värde senare, men det är inte klart än:


```javascript
let winner = null

// Later in the program:
winner = "Alice"

console.log(winner)
```


Detta skriver ut:


```
Alice
```


Så `null` är användbart när du till exempel vill säga: "Det borde finnas något här senare, men just nu är det tomt."


## Block och kontrollflöde

<chapterId>be985168-2636-5b0d-a48f-ac1bbfbff8a7</chapterId>


Hittills har vi mest skrivit kodrader som körs efter varandra.


Men när vi kodar kan vi styra i vilken ordning det ska utföras.


Detta kallas **kontrollflöde**.


Låt oss börja med att förstå block och scope.


### Den globala räckvidden


Varje variabel som vi deklarerar finns i ett **scope**, vilket innebär den del av koden där variabeln är känd.


Om du deklarerar en variabel utanför ett block finns den i det **globala omfånget**.


```javascript
const color = "blue"
console.log(color)
```


Variabeln `color` ligger i det globala omfånget, så den kan nås var som helst i filen.


Om du lägger till fler linjer:


```javascript
const color = "blue"
console.log(color)

const size = "large"
console.log(color)
console.log(size)
```


Både `color` och `size` är globala variabler. De är tillgängliga överallt i filen.


Men vad händer inne i ett block?


### Block och lokal omfattning


Ett **block** är ett stycke kod omgivet av hakparenteser `{}`.


Variabler som deklarerats med `let` eller `const` inom ett block existerar **endast** inom det blocket.


```javascript
{
const message = "inside block"
console.log(message)
}
```


Detta skriver ut:


```
inside block
```


Men om du provar det här:


```javascript
{
const message = "inside block"
}
console.log(message) // Error!
```


JavaScript kommer att ge dig ett felmeddelande som:


```
ReferenceError: message is not defined
```


Det beror på att `message` deklarerades inuti blocket och inte existerar utanför det.


Det innebär att vi kan använda block för att isolera delar av vår kod och vara säkra på att "det som händer i blocket stannar i blocket" (ungefär som i Las Vegas).


Genom att organisera vår kod i block kan vi också strukturera exekveringen av programmet, med kontrollflödeskonstruktioner som `if`


### `if`, `else`


Ibland vill vi köra kod **bara om** något är sant. Det är vad `if`-satsen är till för.


```javascript
const myAge = 20

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Detta skriver ut:


```
Am I an adult?
Yes I am!
```


Som du kan se jämför koden `myAge` och `18`.

I det här fallet returnerar operatorn `>=` `true`, så blocket exekveras.

Om villkoret inte är `true`, kommer blocket inte att utföras.


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Detta skriver ut:


```
Am I an adult?
```


Du kan lägga till ett `else`-block för att hantera det motsatta fallet:


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
} else {
console.log("No, I am not.")
}
```


Detta skriver ut:


```
Am I an adult?
No, I am not.
```


Både `if`- och `else`-blocken är fortfarande block - så variabler som deklareras inuti dem existerar inte utanför.


Om vi vill vara säkra på att något är **inte** sant, vad kan vi då göra?


Som tidigare nämnts har JavaScript en "not"-operator som vänder på booleaner. Så vi kan göra


```javascript
const myAge = 17

const adult = myAge >= 18

console.log("Am I an adult?")

if (!adult) {
console.log("No, I am not.")
}
```

Den här skrivs fortfarande ut:


```
Am I an adult?
No, I am not.
```

Eftersom vi använde operatorn `!` för att invertera variabeln `adult`.


`if (!adult) {...}` ska läsas som "if not adult..."


Med hjälp av block, logik- och jämförelseoperatorer kan vi strukturera programkörningen genom att definiera variabler som måste vara "sanna" (eller "falska") för att något ska hända.


### "under tiden", "avbryta", "fortsätta


En `while`-loop upprepar kod *så länge* ett villkor är sant.


```javascript
let count = 0

while (count < 3) {
console.log("Count is", count)
count = count + 1
}
console.log("the loop is over!")
```


Detta skriver ut:


```
Count is 0
Count is 1
Count is 2
the loop is over!
```


När `count` blir 3, stoppas loopen.


Du kan stoppa en loop i förtid med hjälp av `break`:


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


Detta skriver ut:


```
0
1
2
```


För när talet blir `3`, körs `if`-blocket och det stoppar slingan.


Du kan hoppa över resten av en loop med hjälp av `continue`:


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


Detta skriver ut:


```
1
2
4
5
```


För när talet var `3`, fick `continue` programmet att hoppa över raden som skriver ut talet.


### "för ... av ..


Om du har en array och vill göra något med varje objekt i den kan du använda `for ... of ... {...}`.


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const fruit of fruits) {
console.log(fruit)
}
```


Detta skriver ut:


```
apple
banana
cherry
```

Blocket kommer att exekveras en gång för varje element i matrisen.


`fruit` här är en ny variabel som tar värdet av varje objekt i matrisen, för att operera på den inuti blocket.


### "för ... i ..


Du kan använda `for ... in` för att loopa över nycklarna (indexen) i en array:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(index)
}
```


Detta skriver ut:


```
0
1
2
```


Du kan också använda indexet för att få fram värdet:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(fruits[index])
}
```


Detta ger samma resultat som `for ... of`:


```
apple
banana
cherry
```


I praktiken, för matriser, bör du föredra att använda `for ... of`, eftersom det är enklare och renare.


### Begränsade slingor


Ibland vill vi loopa ett visst antal gånger, eller i allmänhet skriva en kod som upprepar ett block samtidigt som den håller reda på något.

Det är vad en avgränsad `for`-loop är bra för.

En avgränsad slinga kräver vanligtvis tre villkor, åtskilda av ett semikolon `;`, som i `(... ; ... ; ....)`.


```javascript
for (let i = 0; i < 3; i = i + 1) {
console.log(i)
}
```


Detta skriver ut:


```
0
1
2
```


Låt oss förklara det:



- `let i = 0`: deklarerar en variabel som ska användas i blocket (i det här fallet är det en räknare som börjar på 0)
- `i < 3`: deklarerar ett villkor som ska vara `sant` för att blocket ska utföras (i det här fallet är det "upprepa medan `i` är mindre än 3")
- `i = i + 1`: deklarera någon kod som ska köras efter varje körning av blocket (i det här fallet "öka `i` med 1")


Som du kan se kan vi med bounded loop ange mer komplexa villkor för upprepad exekvering av en kod, men oftast är det inte nödvändigt.


### Blocketiketter


Om du måste skriva ett mer komplext kontrollflöde kan du i JavaScript namnge ett block med en **label** som kan användas av `break` eller `continue` för att ange *var* du ska hoppa tillbaka.


Exempel:


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


Detta skriver ut:


```
Inside outer block
Inside inner block
Done
```


Vi använde `break outer` för att lämna `outer`-blocket helt och hållet.


Du kan också märka slingor. Låt oss ta det här exemplet:


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

Det här var ett mycket tråkigt exempel, men förhoppningsvis klargjorde det det (ibland) förekommande behovet av etiketter.


## Introduktion av funktioner

<chapterId>cc324715-09c2-5cf7-9e6f-47a6f16bc04d</chapterId>


När dina program växer kommer du ofta att vilja **återanvända** delar av koden.


Det är det som **funktioner** är till för: de låter dig gruppera ihop lite kod, ge den ett namn och köra den när du vill.


### Funktionsdeklaration


För att deklarera en funktion kan vi använda nyckelordet `function`. Sedan ger vi den ett namn, ett par parenteser `()` med de argument den tar, och ett kodblock `{}` som ska exekveras. Låt oss börja med en funktion som inte tar några argument:


```javascript
function sayHello () {console.log(`Hello!`) }
```


Den här koden **deklarerar** funktionen, men kör den **inte** ännu.


### Funktionsanrop


För att köra (eller "anropa") funktionen skriver du dess namn följt av parenteser:


```javascript
function sayHello () {console.log(`Hello!`) }
sayHello()
```


Detta skriver ut:


```
Hello!
```


Du kan anropa funktionen hur många gånger du vill:


```javascript
function sayHello() {
console.log("Hello!")
}

sayHello()
sayHello()
```


Detta skriver ut:


```
Hello!
Hello!
```


Koden i funktionen körs bara när du anropar den.


### Funktionsargument (input till funktioner)


Ibland vill man att en funktion ska fungera med viss input. Det kan du göra genom att lägga till **argument** inom parentesen.


Till exempel:


```javascript
function sayHelloTo (friend) {
console.log(`Hello ${friend}!`)
}
```


Nu tar denna funktion **ett argument** som heter `friend`.


När du anropar funktionen kan du skicka ett värde:


```javascript
sayHelloTo("Tommy")
```


Detta skriver ut:


```
Hello Tommy!
```


Du kan anropa funktionen igen med ett annat namn:


```javascript
sayHelloTo("Sam")
```


Detta skriver ut:


```
Hello Sam!
```


Det värde som du skickar in ersätter variabeln `friend` i funktionen.


Du kan också använda mer än ett argument:


```javascript
function greetTwoPeople(person1, person2) {
console.log(`Hello ${person1} and ${person2}!`)
}

greetTwoPeople("Lina", "Marco")
```


Detta skriver ut:


```
Hello Lina and Marco!
```


### `return` (utdata från funktioner)


Funktioner kan också **returnera** värden. Det innebär att de skickar ett värde tillbaka till den plats där funktionen anropades.


Här är ett enkelt exempel:


```javascript
function getNumber() {
return 42
}

const result = getNumber()
console.log(result)
```


Detta skriver ut:


```
42
```


Funktionen `getNumber()` returnerar `42`, och vi lagrar den i `result` och skriver sedan ut den.


Du kan också returnera något du räknar ut:


```javascript
function add(a, b) {
return a + b
}

const result = add(2, 3)
console.log(result)
```


Detta skriver ut:


```
5
```


När ett värde har "returnerats" stoppas funktionen. Allt efter `return` i det blocket händer inte.


```javascript
function saySomething() {

return "hi"

console.log("this never runs")

}

const message = saySomething()
console.log(message)
```


Detta skrivs endast ut:


```
hi
```


eftersom bara `"hi"` returneras. Raden `console.log("det här körs aldrig")` hoppas över.


Du kan tänka på funktioner som små underprogram. Varje funktion kan ta emot en indata, bearbeta den och ge tillbaka en utdata.


Vad händer om vi försöker använda returvärdet för en funktion, men den funktionen inte returnerade någonting?


```javascript
function doesNothing () {}

const x = doesNothing()

console.log(x)
```

Detta kommer att skriva ut `undefined`. Returvärdet för en funktion som inte returnerar någonting är `undefined`.


## Objekt och klasser

<chapterId>26689f25-8212-5057-8c21-3a05eee0ac75</chapterId>


JavaScript kallas ofta för ett objektorienterat språk.


Det innebär att den hjälper dig att organisera din kod genom att gruppera värden och funktioner tillsammans i **objekt**.


### Vad är ett "objekt"?


Ett objekt kan innehålla data och funktioner som hanterar dessa data. När en funktion läggs in i ett objekt säger vi att det är en "metod".


Det första objektet vi har sett var `console`-objektet. Det är ett objekt som innehåller flera metoder för att skriva ut saker på skärmen och felsöka våra program.


Den kan till och med skriva ut sig själv; du kan göra


```javascript
console.log(console)
```


och den skriver ut en lista över de metoder som den innehåller. Till exempel, på min maskin skrev den ut


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


Som du kan se har den många metoder som du kan använda för att felsöka!


Javascript ger oss ett annat sätt att skapa nya objekt som kan göra vad vi vill att de ska göra.


### Skapa ett objekt


Det enklaste sättet att skapa ett objekt är genom att gruppera data och funktioner med hjälp av **klammerparenteser** `{}`.


Detta skapar vad vi kallar ett **anonymt objekt**


```javascript
const cat = {
name: "Whiskers",
age: 3
}
```


Detta skapar ett objekt och lagrar det i en variabel som heter `cat`.


Objektet har två **egenskaper**:



- `name` med värdet `"Whiskers"`
- `ålder` med värdet `3`


Låt oss skriva ut det:


```javascript
console.log(cat)
```


Detta skriver ut:


```
{ name: 'Whiskers', age: 3 }
```


Du kan få ut egenskaperna ur objektet med hjälp av en punkt, som i `objektnamn.egenskapsnamn`:


```javascript
console.log(cat.name)  // prints "Whiskers"
console.log(cat.age)   // prints 3
```


Du kan också **ändra** en fastighet:


```javascript
cat.age = 4
console.log(cat.age)  // now it prints 4
```


Även om ett objekt definieras som `const` kan du alltså fortfarande ändra de data som det innehåller.


När det gäller objekt kommer `const` bara att hindra dig från att åsidosätta hela objektet:


```javascript
const cat = {
name: "Whiskers",
age: 3
}

cat.age = 5 // this works

cat = 5 // this throws an error, you're trying to reassign the whole object

```


Som tidigare nämnts kan objekt även innehålla **funktioner**, och när en funktion är en del av ett objekt kallar vi det för en **metod**.


Här är ett exempel:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log("Meow!")
}
}
```


Detta objekt har:



- En egenskap för "namn
- En `speak()`-metod


Låt oss anropa metoden:


```javascript
cat.speak()
```


Den skriver ut:


```
Meow!
```


Metoder kan använda de data som objektet innehåller genom nyckelordet `this`.

`this` hänvisar till det aktuella objektet. I det här exemplet kommer det att användas för att skriva ut namnet på katten:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log(`${this.name} says meow!`)
}
}

cat.speak()
```


Detta skriver ut:


```
Whiskers says meow!
```


Ordet "detta" betyder "detta objekt" ... i det här fallet, "katt" -objektet.



Den här typen av objekt är bra när du bara vill ha något snabbt och enkelt. Men om du behöver skapa **många objekt** med samma struktur finns det ett bättre sätt, och det är där **klasser** kommer in i bilden.


### Klasser och konstruktörer


En **klass** är som en ritning. Den talar om för JavaScript hur man skapar en viss typ av objekt.


Du definierar en klass med nyckelordet `class`, följt av klassens namn och ett block med hakparenteser `{}`.


```javascript
class Dog {}
```


Klasser börjar vanligtvis med en versal bokstav, enligt konvention.


Du kan skapa ett nytt objekt av en klass med hjälp av `new`:


```javascript
const hachiko = new Dog()
```


Försök att skriva ut objektet:

```javascript
class Dog {}

const myDog = new Dog()

console.log(myDog)
```


Du kommer att få


```
Dog {}
```


Som du kan se är klassen Hund tom, så objektet `myDog` är också tomt.


Vi kan definiera vilka egenskaper som Dog-objekt ska innehålla genom att lägga till en `constructor`.


En konstruktor är en speciell funktion som körs när du skapar (eller "konstruerar") ett nytt objekt.


```javascript
class Dog {
constructor() { }
}
```


Vi vill att varje hund ska ha ett namn, så vi lägger till en `name`-parameter i funktionen:


```javascript
class Dog {
constructor(name) { }
}
```


Och sedan använder vi `this` för att förklara att `name` är `namnet` på `Dog`-objektet vi bygger


```javascript
class Dog {
constructor(name) {
this.name = name
}}
```


Låt oss försöka använda den nu:


```javascript
class Dog {
constructor(name) {
this.name = name
}
}

const myDog = new Dog("hachiko")

console.log(myDog)
```


Detta skriver ut något i stil med:


```
Dog { name: 'hachiko' }
```


Som du kan se tar metoden `constructor` de argument som du skickar till klassen när du gör `new Dog()`, och använder dem för att bygga objektet.


Låt oss bryta ner det:



- `class Dog` definierar klassen Dog.
- `constructor(name)` konfigurerar objektet när det skapas.
- `this.name = name` lagrar värdet i det nya objektet.
- `new Dog("hachiko")` skapar ett nytt objekt från klassen, med egenskapen `name` inställd på `"hachiko"`.


Låt oss nu lägga till en metod i vår klass:


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


Detta kommer att skriva ut


```javascript
hachiko says barf!
```


Om vi gör samma sak för två olika instanser av Dog



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


får vi


```
hachiko says barf!
bobby says barf!
```


metoden `speak()` använder egenskapen `name` för den `Dog` som den anropas på.


Detta är den främsta anledningen till att klasser finns: de gör det möjligt för oss att definiera en uppsättning metoder som fungerar på data och sedan skapa flera objekt som delar samma data "form".


När vi anropar en metod på ett av dessa objekt kommer den att arbeta med de data som *det specifika objektet* innehåller.


### Ändra formen på ett objekt


Objekt i JavaScript är flexibla. Även efter att du har skapat ett objekt kan du lägga till nya egenskaper eller ta bort befintliga.


Det är tillåtet, men det är något du bör använda försiktigt.


Låt oss börja med vår enkla klass `Dog`:


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


I det här läget har `myDog` bara en egenskap: `name`. Vi kan fortfarande lägga till nya egenskaper efter att den har skapats:


```javascript
myDog.age = 5

console.log(myDog.age) // prints 5
```


Vi kan också lägga till en ny metod:


```javascript
myDog.jump = function () {
console.log(`${this.name} jumps!`)
}

myDog.jump() // Fido jumps!
```


Och vi kan också ta bort egenskaper med hjälp av nyckelordet `delete`.


```javascript
delete myDog.name

console.log(myDog.name) // prints 'undefined'
```


Detta fungerar, men här är något viktigt att veta: JavaScript-motorer som V8 (som används i Node.js och i webbläsaren Chrome) kör snabbare när dina objekt alltid har samma egenskaper. Om du lägger till eller tar bort egenskaper efter att objektet har skapats kan det göra saker långsammare.


I små program spelar detta inte så stor roll. Men i större projekt (som spel) är det bättre att lista alla egenskaper i konstruktorn från början, även om du inte använder dem direkt. Detta håller objektformen stabil och hjälper din kod att köras snabbare.


Till exempel, istället för detta:


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


Du kan göra


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


Båda versionerna fungerar, men den andra är bättre för prestanda. Du talar om för motorn på förhand vilka egenskaper varje objekt kommer att ha, och den kan optimera därefter.


Med JavaScript kan du omforma objekt fritt, men när du använder klasser är det bäst att planera objektets form i förväg.



### Nedärvning med `extends` och `super()`


Ibland vill man skapa en klass som är *nästan* likadan som en annan klass, men med några extra funktioner.


Istället för att ändra formen på objekt (vilket som sagt inte är optimalt för prestandan), eller att behöva skriva om en ny klass från grunden, låter JavaScript dig använda något som kallas **arv**.


Arv innebär att en klass kan **utöka** en annan. Den nya klassen får alla egenskaper och metoder från den gamla, och du kan lägga till mer eller ändra det du behöver.


Låt oss säga att vi har en basklass som heter `Vehicle`:


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


Nu vill vi skapa en klass för bilar. En bil är ett slags fordon, men vi kanske vill att den ska ha några extra funktioner eller ett annat meddelande när den startar. Istället för att skriva om allt kan vi använda `extends`:


```javascript
class Car extends Vehicle {
start() {
console.log(`${this.brand} car is ready to drive!`)
}
}
```


Klassen `Car` **ärver** nu allt från `Vehicle`. Den får egenskapen `brand`, och vi har ersatt metoden `start()` med vår egen version.


![](assets/en/4.webp)


Låt oss prova det:


```javascript
const myCar = new Car("Toyota")
myCar.start()
```


Detta skriver ut:


```
Toyota car is ready to drive!
```


Även om `Car` inte har någon egen konstruktör, använder den fortfarande den från `Vehicle`. Men om vi vill skriva en egen konstruktor i `Car` kan vi göra det, vi behöver bara inkludera ett anrop till dess förälders konstruktor med `super()`.


Så här gör du:


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



Detta skriver ut:


```
Toyota Corolla is ready to drive!
```


Så för att sammanfatta



- `extenderar` betyder att en klass är baserad på en annan.
- `super()` används för att anropa konstruktören för den klass du utökar.
- Den nya klassen får alla egenskaper och metoder som den ursprungliga klassen har.
- Du kan **överskriva** metoder (som `start()`) för att få dem att göra något annat.


Detta är användbart när du har flera saker som liknar varandra (t.ex. bilar, lastbilar och cyklar) och du vill att de ska dela kod men ändå bete sig på sitt eget sätt.


### `instansav`


Nyckelordet `instanceof` kontrollerar om ett objekt har skapats från en viss klass.


Låt oss säga att vi har en klass som heter `User`:


```javascript
class User {
constructor(username) {
this.username = username
}
}

const regularUser = new User("julia123")

console.log(regularUser instanceof User)
```


Detta skriver ut:


```
true
```


Bekräftar att `regularUser` är en `User`. Det beror på att `regularUser` skapades med hjälp av klassen `User`.


Det fungerar också med **ärvda** klasser. Här är till exempel en `Admin`-klass som utvidgar `User`:


```javascript
class Admin extends User {}

const ourAdmin = new Admin("admin42")

console.log(ourAdmin instanceof Admin)   // true
console.log(ourAdmin instanceof User)    // true
```


Båda raderna returnerar `true`. Det beror på att `Admin` är en subklass av `User`, därför är `ourAdmin` både en `Admin` och en `User`


# JavaScript på mellannivå

<partId>243f63ab-4f34-5c30-80cb-84ef46f6761d</partId>


## Felhantering

<chapterId>d0206bc5-d386-5e7f-9917-5803f392448c</chapterId>


När du skriver mer komplexa JavaScript-program kommer du att stöta på **fel**. Detta är oväntade situationer där något går fel. Kanske är en variabel "odefinierad" men du försöker använda den, eller så får någon kod fel typ av indata.


Om vi inte hanterar dessa fel på rätt sätt kan vårt program krascha eller bete sig på oförutsägbara sätt. JavaScript tillhandahåller verktyg för att upptäcka och hantera dessa fel så att vi kan hantera dem på ett mer elegant sätt.


### Vanligt fel: åtkomst till ett värde på `undefined`


Här är en vanlig situation som orsakar ett fel:


```javascript
const user = undefined
console.log(user.name)
```


Om du kör den här koden kommer du att få ett fel som ser ut så här:


```
TypeError: Cannot read properties of undefined (reading 'name')
```


Det är JavaScript som säger till dig: "Hej, du försökte få egenskapen `name` från något som är `undefined`, och det är inte vettigt." Och som du kan se, när den här typen av fel inträffar, slutar programmet att köra om du inte specifikt har skrivit kod för att fånga och hantera det.


### "kastar" ett fel


Ibland vill man manuellt **uppväcka ett fel** i sin kod. I det fallet använder du nyckelordet `throw`.


```javascript
throw new Error("This is a custom error message")
```


Detta stoppar omedelbart programmet och skriver ut:


```
Uncaught Error: This is a custom error message
```


Du kan använda `throw` för att genomdriva regler i ditt program. Till exempel


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


Det andra anropet orsakar ett fel eftersom det inte är tillåtet att dela med noll i det här exemplet.


### Fånga upp fel med `try...catch`


Om du inte vill att ditt program ska krascha när ett fel inträffar kan du fånga felet med hjälp av ett `try...catch`-block. Detta är användbart när du vill att ditt program ska **fortsätta** även om något misslyckas.


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log("Oops! Something went wrong.")
}
```


Utgång:


```
Oops! Something went wrong.
```


Så här fungerar det:



- Koden inuti `try`-blocket prövas först.
- Om ett fel uppstår hoppar JavaScript **till `catch`-blocket** och hoppar över resten av `try`-blocket.
- `catch`-blocket tar emot felet, så att du kan skriva ut det eller hantera det på något annat sätt, som till exempel


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log(`The message of the error was: "${error.message}"`)
}
```


Utgång:


```
The message of the error was: "Cannot read properties of undefined (reading 'name')"
```


### Blocket "slutligen


Du kan också lägga till ett `finally`-block. Detta är kod som **alltid körs**, oavsett om det uppstod ett fel eller inte.


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


Utgång:


```
Trying something risky...
Caught the error: Uh oh!
This will run no matter what.
```


## Undvikande av buggar

<chapterId>db12d9f6-5806-514c-998e-0ae24805104e</chapterId>


I det här kapitlet beskrivs några av de vanligaste fallgroparna i JavaScript och hur du undviker dem.


### `var` och Assignment utan deklaration


I äldre JavaScript-kod deklarerades variabler ofta med hjälp av nyckelordet `var`. Till skillnad från `let` och `const`, som du redan har lärt dig om, kan `var` bete sig på förvirrande sätt.


Till exempel:


```javascript
{
var message = "hello"
}
console.log(message)
```


Du kanske förväntar dig att `message` bara ska finnas inuti blocket, men det gör den inte. `var` ignorerar blockets omfattning och gör variabeln tillgänglig i hela funktionen eller filen.


Detta kan leda till oväntade beteenden, särskilt i större program. Av denna anledning bör modern JavaScript-kod alltid använda `let` eller `const` istället för `var`.


Ännu värre är att JavaScript låter dig tilldela värden till variabler ** utan att deklarera dem alls**:


```javascript
function greet() {
user = "Alice"
}
greet()
console.log(user) // prints "Alice"
```


Detta skapar en ny global variabel `name` utan någon deklaration. Detta kan ske i tysthet och leda till buggar som är svåra att spåra, särskilt om det bara var ett skrivfel. Deklarera alltid variabler med hjälp av `let` eller `const`.


### Svagt typsystem


JavaScript är svagt typat, vilket innebär att det automatiskt konverterar värden från en typ till en annan om det behövs. Det här kallas för type coercion, och även om det kan vara praktiskt leder det ofta till förvirrande resultat.


Till exempel:


```javascript
console.log("5" + 1)    // "51"
console.log("5" - 1)    // 4
console.log(true + 1)   // 2
console.log(null + 1)   // 1
```


I de här exemplen försöker JavaScript gissa vad du menade. Ibland förvandlas strängar till siffror, booleaner till siffror eller strängar till strängar. Detta kan göra att din kod beter sig på oväntade sätt.


Det är viktigt att vara medveten om JavaScript:s svaga typsystem. När saker och ting börjar bete sig konstigt kan det bero på oväntad typ tvång.


### `"använd strikt"`


Du kan aktivera ett striktare läge som gör vissa tysta fel till riktiga fel och hindrar dig från att använda några av de farligare funktionerna i språket.


För att aktivera detta strängare läge, lägg till denna rad längst upp i filen eller funktionen:


```javascript
"use strict"
```


Till exempel:


```javascript
"use strict"
name = "Alice" // ReferenceError: name is not defined
```


Utan strikt läge skulle JavaScript i tysthet skapa en global variabel som heter `name`. Men med strikt läge blir detta ett verkligt fel, vilket hjälper dig att hitta buggar tidigare.


Strikt läge inaktiverar också vissa föråldrade funktioner i JavaScript och gör din kod enklare att optimera och underhålla.


## Värde kontra referens

<chapterId>bb898425-dc2f-5e5c-864b-0cb7a4a9aea9</chapterId>


JavaScript hanterar olika typer av värden på olika sätt.


Vissa värden **kopieras** när du tilldelar dem till en variabel.


Andra är **delade** när du tilldelar dem till en ny variabel, så om du ändrar den ena ändras den andra också.


### Passera genom värde


När ett värde skickas **by value** gör JavaScript en **kopia** av det.


Så om du ändrar den ena påverkar det inte den andra.


Detta händer med primitiva typer, t.ex:



- siffror
- strängar
- booleaner (`true` och `false`)
- `null`
- `undefinierad`


Låt oss titta på ett exempel:


```javascript
let a = 5
let b = a

b = 10

console.log(a) // 5
console.log(b) // 10
```


Vi gav `b` värdet av `a`, men sedan ändrade vi `b` till `10`.


Eftersom siffror skickas med värde kopierade JavaScript `5` till `b`. `5` i `b` är oberoende av den ursprungliga `5` i `a` så att ändra värdet på `b` hade ingen effekt på `a`.


Låt oss försöka med en sträng:


```javascript
let name1 = "Alice"
let name2 = name1

name2 = "Bob"

console.log(name1) // Alice
console.log(name2) // Bob
```


Återigen, att ändra `namn2` påverkade inte `namn1`, eftersom strängar också skickas med värde.


Samma sak händer när man skickar en primitive till en funktion: den kopieras. Funktionen kan alltså inte ändra originalet.


```javascript
function plusOne(x) {
x = x + 1
}

let number = 5

plusOne(number)

console.log(number) // 5
```


Även om funktionen "1" lades till i "x", ändrades inte det ursprungliga "talet".


Det beror på att endast en **kopia** skickades in i funktionen.


### Passera genom referens


Objekt skickas **med referens**.


Det betyder att istället för att kopiera dem skickar JavaScript bara en **referens** till den, och om du ändrar den kommer alla andra variabler som pekar på den också att se ändringen.


Till exempel:


```javascript
const person1 = { name: "Alice" }
const person2 = person1

person2.name = "Bob"

console.log(person1.name) // Bob
console.log(person2.name) // Bob
```


Både `person1` och `person2` pekar på samma objekt i minnet.


Så när vi ändrade `person2.name`, ändrade vi också `person1.name`, eftersom de båda tittar på samma sak.


Arrayer är objekt, så låt oss prova samma sak med en array:


```javascript
const list1 = [1, 2, 3]
const list2 = list1

list2.push(4)

console.log(list1) // [1, 2, 3, 4]
console.log(list2) // [1, 2, 3, 4]
```


Vi flyttade `4` till `list2`, men `list1` påverkades också, eftersom de båda hänvisar till samma array.


Låt oss se vad som händer när vi skickar ett objekt till en funktion:


```javascript
function rename(user) {
user.name = "Charlie"
}

const person = { name: "Dana" }

rename(person)

console.log(person.name) // Charlie
```


Funktionen ändrade objektet! Det beror på att den fick en **referens** till det ursprungliga `person`-objektet.


Den fick inte en kopia. Den fick tillgång till originalobjektet och därmed möjlighet att modifiera det.


Det är viktigt att komma ihåg denna distinktion, eftersom vår kod annars kan bete sig annorlunda än vad vi förväntar oss. Vi kan till exempel skriva en funktion med förväntningen att den inte ska ändra de argument den tar emot, och senare upptäcka att den faktiskt ändrade dem (eftersom de var objekt, så de skickades med referens).


## Arbeta med funktioner

<chapterId>e0d277a8-c642-5af7-9e53-dee27c811967</chapterId>


Du har redan lärt dig hur du deklarerar och använder funktioner i JavaScript. Men JavaScript ger dig fler verktyg för att arbeta med funktioner på kraftfulla sätt.


### Funktioner för pilar


Arrow functions är ett kortare sätt att skriva funktioner. I stället för att använda nyckelordet `function` använder vi en pil (`=>`).


Här är en normal funktion:


```javascript
function greet(name) {
return `Hello, ${name}!`
}
```


Pilversionen ser ut så här:


```javascript
const greet = (name) => {
return `Hello, ${name}!`
}
```


Om funktionen har **en enda rad** kan du hoppa över parenteserna och `return`:


```javascript
const greet = (name) => `Hello, ${name}!`
```


Om funktionen har **enbart en parameter** kan du till och med hoppa över parenteserna runt parametrarna:


```javascript
const greet = name => `Hello, ${name}!`
```


Pilfunktioner är mycket vanliga i modern JavaScript, eftersom de gör det möjligt att uttrycka enkla funktioner med betydligt mindre boilerplate.


### Standardparametrar


Ibland vill man att en funktion ska ha ett **standardvärde** om inget argument skickas med.


Du kan göra det så här:


```javascript
function sayHello(name = "friend") {
console.log(`Hello, ${name}!`)
}

sayHello("Alice") // Hello, Alice!
sayHello()        // Hello, friend!
```


Standardvärdet `"friend"` används när inget skickas in.


### Spreadparametrar (`...`)


Vad händer om din funktion tar ett flexibelt antal argument?


Du kan använda **spridningsoperatorn** (`...`) för att samla dem i en matris:


```javascript
function logAll(...items) {
console.log(items)
}

logAll(1, 2, 3) // [1, 2, 3]
logAll("a", "b") // ["a", "b"]
```


Du kan sedan använda en loop för att bearbeta varje objekt:


```javascript
function logEach(...items) {
for (const item of items) {
console.log(item)
}
}
```


Spread-operatorn är användbar när du inte vet hur många argument som ska skickas.


### Funktioner av högre ordning


En **högre ordningens funktion** är en funktion som:



- tar en annan funktion som indata
- och/eller returnerar en funktion som utdata


Här är ett enkelt exempel:


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


Detta skriver ut:


```
Hello, friend!
Hello, friend!
```


Vi kan skicka en pilfunktion till den:


```javascript
runTwice(
() => console.log("Hello!")
)
```


Detta skriver ut:


```
Hello!
Hello!
```


Du kan också skriva funktioner som **återlämnar** andra funktioner:


```javascript
function makeGreeter(name) {
return () => console.log(`Hi, ${name}`)
}

const greetAlice = makeGreeter("Alice")
const greetBob = makeGreeter("Bob")

greetAlice() // Hi, Alice
greetBob() // Hi, Bob
```


Funktionen `makeGreeter` är en funktion som bygger upp andra funktioner. Den tar emot en sträng och returnerar en ny funktion som använder den strängen i sitt anrop till `console.log`.


Den här typen av mönster är mycket kraftfullt, eftersom det gör att du kan lämna "hål" i dina funktioner som du senare kan fylla med det beteende du behöver.


### `map()`, `filter()`, `reduce()`


JavaScript ger dig några användbara inbyggda metoder som du kan använda med arrayer.


Dessa metoder tar funktioner som argument, så de är också funktioner av högre ordning.


`map()` omvandlar varje objekt i en array till något annat.


Exempel:


```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map(x => x * 2)

console.log(doubled) // [2, 4, 6]
```


Varje tal dubbleras och resultatet blir en ny matris.


`filter()` tar bort objekt från matrisen om de inte klarar ett test.


Exempel:


```javascript
const numbers = [1, 2, 3, 4, 5]
const numbersGreaterThanTwo = numbers.filter(x => x > 2)

console.log(numbersGreaterThanTwo) // [3, 4, 5]
```


Endast de matrisposter för vilka villkoret `x > 2` returnerar `true` sparas.


`reduce()` används för att kombinera alla objekt i en array till ett enda värde.


Exempel:


```javascript
const numbers = [1, 2, 3, 4]
const total = numbers.reduce((current, next) => current + next)

console.log(total) // 10
```


`reduce` går igenom matrisen och, i det här exemplet, använder operatorn `+` mellan `1` och `2`, sedan mellan det resulterande `3` och `3`, sedan mellan det resulterande `6` och `4`, tills den har summan av alla matrisposter (vilket är 10).


Du kan använda `reduce()` för många saker, t.ex. totalsummor, medelvärden eller för att bygga upp nya värden steg för steg.


Dessa metoder (`map`, `filter`, `reduce`) är kraftfulla verktyg för att bearbeta data utan att skriva manuella loopar.


Du kan till och med kombinera dem i en kedja av operationer, så här:


```javascript
const numbers = [1, 2, 3, 4, 5]

const result = numbers
.map(n => n * 2)        // Double each entry, obtain [2, 4, 6, 8, 10]
.filter(n => n > 3) // Keep only the entries bigger than 3, so you get [4, 6, 8, 10]
.reduce((n1, n2) => n1 + n2) // Adds them: 4 + 6 + 8 + 10 = 28

console.log(result) // 28
```


## Arbeta med objekt

<chapterId>7842aada-f009-5518-b8e3-1104e166a035</chapterId>


I det här kapitlet lär vi oss några kraftfulla och lite mer avancerade verktyg för att arbeta med objekt i JavaScript.


### Privata fastigheter


Ibland vill vi dölja en egenskap hos ett objekt så att den inte kan ändras eller nås från utsidan av objektet. JavaScript ger oss ett sätt att göra detta genom att använda `#` före egenskapsnamnet. Detta skapar en **privat** egenskap, som endast är tillgänglig inifrån klassen.


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


Privata egenskaper är användbara när du vill förhindra oavsiktliga ändringar.


### `statisk` Egenskaper


Ibland vill man att en egenskap ska tillhöra själva klassen, inte varje objekt man skapar från den klassen. Det är vad `static` är till för. En `static`-egenskap finns i klassen och alla objekt i den klassen kommer att hänvisa till den.


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


Detta är användbart för att lagra delade data och metoder som gäller för hela gruppen av objekt, inte bara ett.


### `get` och `set`


I JavaScript kan du med `get` och `set` skapa egenskaper som *ser* ut som vanliga variabler, men som faktiskt kör specialkod i bakgrunden.


En `get`ter-metod körs när man försöker *läsa* en egenskap. Den deklareras genom att skriva `get` före en metod med namnet på egenskapen.


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


Även om `fullName` inte är en vanlig egenskap kan vi använda den som en, och bakom kulisserna kör den funktionen `get` för att bygga upp det fullständiga namnet.


En `set`ter-metod körs när du *tilldelar* ett värde till en egenskap. Den låter dig kontrollera vad som händer när någon försöker ändra det värdet. Den deklareras genom att skriva `set` före en metod med namnet på egenskapen.


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


När vi gör `user.fullName = "John Smith"` körs metoden `set` och värdena `firstName` och `lastName` uppdateras.


Så även om det känns som om vi bara ställer in en enkel variabel, utlöser vi faktiskt logik som uppdaterar andra egenskaper.


## Nycklar och värden

<chapterId>01a397b8-c12a-5c39-82b3-6d9ebbb72a29</chapterId>


Varje egenskap i ett JavaScript-objekt har en **nyckel** (även kallat egenskapsnamn) och ett **värde**.


Till exempel:


```javascript
const user = {
name: "Alice",
age: 30
}
```


I det här objektet är "namn" och "ålder" nycklar och "Alice" och "30" är värden.


### Dynamisk åtkomst


Ibland vet du inte namnet på en egenskap i förväg ... kanske får du det från användarinmatning eller läser det från en variabel. Du kan fortfarande komma åt den genom att använda **parentesnotation**, som `myObject["keyName"]`.


```javascript
const user = {
name: "Alice",
age: 30
}

console.log(user["name"]) // Alice
```


Vi skickade strängen `name` till objektet för att få motsvarande värde.


Vi kan spara en nyckel i en variabel och använda den för att komma åt motsvarande värde senare, t.ex


```javascript
const user = {
name: "Alice",
age: 30
}

const key = "name"

console.log(user[key]) // Alice
```


### Dynamisk Assignment


Du kan också skapa eller uppdatera objektets egenskaper med hjälp av variabler som nycklar.


```javascript
const settings = {}

const key = "theme"
settings[key] = "dark"

console.log(settings) // { theme: "dark" }
```


Detta är användbart när du vill bygga ett objekt steg för steg. Till exempel:


```javascript
const user = {}

user["username"] = "bananaFan123"
user["email"] = "banana@fruit.com"

console.log(user)
// { username: "bananaFan123", email: "banana@fruit.com" }
```


Du kan till och med använda en dynamisk nyckel *när du skapar* objektet med hjälp av hakparenteser:


```javascript
const key = "language"
const config = {
[key]: "JavaScript"
}

console.log(config.language) // JavaScript
```


Detta kallas för en **beräknad egenskap**. Värdet inom hakparenteserna utvärderas och resultatet används som nyckel.


### `Symbol` Typ


Förutom strängar kan du i JavaScript också använda en speciell typ som heter "Symbol" som objektnyckel.


Låt oss börja med ett enkelt exempel:


```javascript
const id = Symbol("userID")

const user = {
name: "Bob",
[id]: 12345
}

console.log(user[id]) // 12345
```


I det här exemplet är `id` en symbol. Det är inte en sträng, men den fungerar ändå som en nyckel. Om du försöker logga `user` till konsolen kommer du att se det här:


```javascript
console.log(user) // { name: 'Bob', [Symbol(userID)]: 12345 }
```


En annan viktig sak: varje symbol som du skapar är unik, även om de skapas med samma sträng.


```javascript
const a = Symbol("label")
const b = Symbol("label")

console.log(a === b) // false
```


Med hjälp av symboler kan du definiera nycklar som inte krockar med vanliga nycklar. Låt oss till exempel säga att du har ett objekt med egenskapen `name`, men att objektet kommer att kunna anpassas av en användare i framtiden, på sätt som du inte kan förutse, och att den användaren kan lägga till egenskapen `name` också. Om den ursprungliga `name`-egenskapen definierades med en sträng skulle den skrivas över av den nya, så här:


```javascript
const obj = {
name: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy' }
```


Om vi använder en symbol istället:


```javascript
const name = Symbol("name")

const obj = {
[name]: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy', [Symbol(name)]: 'John' }
```


Som du kan se bevaras den ursprungliga egenskapen `name` på något sätt på detta sätt. Detta kan vara användbart i vissa undantagsfall.


## Verktygsobjekt

<chapterId>516e74c8-2a11-545a-a4d1-c2cabb91a273</chapterId>


JavaScript ger oss några användbara inbyggda objekt som hjälper oss att göra saker som felsökning och matematiska operationer.


### Andra "konsol"-metoder


Du har redan sett `console.log`, som skriver ut värden på skärmen.


Det finns några andra användbara metoder tillgängliga för objektet `console` som kan hjälpa dig att felsöka dina program.


#### `konsol.varning`


Skriver ut ett meddelande i gult (eller med en varningsikon i vissa miljöer):


```javascript
console.warn("This is just a warning.")
```


#### `konsol.fel`


Skriver ut ett meddelande i rött, som ett fel:


```javascript
console.error("Something went wrong!")
```


#### `konsol.tabell`


Visar en array eller ett objekt som en tabell:


```javascript
const users = [
{ name: "Alice", age: 25 },
{ name: "Bob", age: 30 }
]

console.table(users)
```


Detta skriver ut en tabell som:


```
┌─────────┬────────┬─────┐
│ (index) │  name  │ age │
├─────────┼────────┼─────┤
│    0    │ 'Alice'│  25 │
│    1    │ 'Bob'  │  30 │
└─────────┴────────┴─────┘
```


Detta kan vara användbart för att visualisera strukturerad data.


#### `console.time` och `console.timeEnd`


Man kan mäta hur lång tid något tar:


```javascript
console.time("timer")
for (let i = 0; i < 1000000; i++) {}
console.timeEnd("timer")
```


Detta skriver ut något i stil med:


```
timer: 2.379ms
```


Användbart för enkla prestandatester.


### Objektet `Math


JavaScript ger dig ett `Math`-objekt med användbara metoder för att göra beräkningar.


#### `Math.random()`


Returnerar ett slumpmässigt tal mellan 0 (inkluderande) och 1 (exkluderande):


```javascript
const r = Math.random()
console.log(r)
```


Exempel på utdata:


```
0.4387429859
```


#### `Math.floor()` och `Math.ceil()`



- `Math.floor(n)` avrundar **nedåt** till närmaste heltal
- `Math.ceil(n)` avrundar **upp** till närmaste heltal


```javascript
console.log(Math.floor(4.9)) // 4
console.log(Math.ceil(4.1))  // 5
```


#### `Math.round()`


Avrundas till närmaste heltal:


```javascript
console.log(Math.round(4.4)) // 4
console.log(Math.round(4.6)) // 5
```


#### `Math.max()` och `Math.min()`


Returnerar det största eller minsta värdet från en lista med tal:


```javascript
console.log(Math.max(5, 9, 3)) // 9
console.log(Math.min(5, 9, 3)) // 3
```


#### `Math.pow()` och `Math.sqrt()`



- `Math.pow(a, b)` ger dig `a` i potens med `b`
- `Math.sqrt(n)` ger dig kvadratroten av `n`


```javascript
console.log(Math.pow(2, 3))   // 8
console.log(Math.sqrt(16))    // 4
```


# Avancerad JavaScript

<partId>72c30671-ca20-5617-92a5-d5ba7aa38c93</partId>


## Övriga samlingar

<chapterId>a9a70c6d-a343-5a46-a383-e288bc2700e3</chapterId>


JavaScript ger oss några speciella samlingstyper som går utöver vanliga arrayer och objekt. Dessa inkluderar `Map` och `Set`.


De hjälper dig att lagra och hantera grupper av värden, men de fungerar på ett annat sätt än vad du har sett hittills.


En `Map` är en samling av **nyckel-värde-par**, precis som ett objekt. Men det har några viktiga skillnader:



- Nycklarna kan vara **valfritt värde**, inte bara strängar.
- Artiklarnas ordning bevaras.
- Den har inbyggda metoder som gör det enklare att arbeta med den.


Du skapar en ny karta så här:


```javascript
const myMap = new Map()
```


Detta skapar en tom karta. Om du vill lägga till poster i den använder du `myMap.set(key, value)`:


```javascript
myMap.set("name", "Alice")
```


Detta lägger till en nyckel `"name"` med värdet `"Alice"`.


Du kan också använda ett nummer som nyckel:


```javascript
myMap.set(42, "The answer")
```


Och till och med ett objekt som nyckel:


```javascript
const objKey = { id: 1 }
myMap.set(objKey, "Object as key")
```


Det skulle inte fungera med vanliga objekt, som bara tillåter strängnycklar.


För att **hämta ett värde** använder du `myMap.get(key)`:


```javascript
console.log(myMap.get("name"))     // Alice
console.log(myMap.get(42))         // The answer
console.log(myMap.get(objKey))     // Object as key
```


För att **kontrollera om en nyckel finns**, använd `myMap.has(key)`:


```javascript
console.log(myMap.has("name")) // true
```


Om du vill **ta bort en nyckel** använder du `myMap.delete(key)`:


```javascript
myMap.delete("name")
```


För att **rensa hela kartan** använder du `myMap.clear()`:


```javascript
myMap.clear()
```


Kartor är utmärkta för att hantera stora samlingar av värden, eftersom åtkomst till värden på en stor karta vanligtvis ger mycket bättre prestanda än på ett stort objekt.


### `Set`


En `Set` är en samling av enbart **värden** (inga nycklar), där varje värde måste vara **unikt**. Det betyder att:



- Du kan inte ha samma värde två gånger
- Värdena lagras i den ordning du lägger till dem


Du skapar ett set så här:


```javascript
const mySet = new Set()
```


För att **lägga till värden** använder du `mySet.add(value)`:


```javascript
mySet.add(1)
mySet.add(2)
mySet.add(2) // duplicate, will be ignored
```


Även om vi försökte lägga till `2` två gånger, kommer uppsättningen bara att behålla en kopia.


För att **kontrollera om ett värde finns i uppsättningen**, använd `mySet.has(value)`:


```javascript
console.log(mySet.has(2)) // true
console.log(mySet.has(3)) // false
```


Om du vill **ta bort ett värde** använder du `mySet.delete(value)`:


```javascript
mySet.delete(2)
```


För att **rensa allt**, använd `mySet.clear()`:


```javascript
mySet.clear()
```


En `Set` är användbar när du vill behålla en samling unika värden utan att manuellt behöva kontrollera om det finns dubbletter:


```javascript
const numberArray = [1, 2, 2, 3, 4, 4, 4, 5]

const numberSet = new Set(numberArray)

console.log(numberSet) // Set(5) { 1, 2, 3, 4, 5 }
```


Med `Set` undviker du dubbletter åt dig.


## Iteratorer

<chapterId>61d24e5e-b7e4-541a-8322-778f61f26a72</chapterId>


De flesta saker i JavaScript som du kan loopa över (t.ex. arrayer, strängar, maps, set) är **iterabla**: de kan tillhandahålla iteratorer för sitt innehåll.


En **iterator** är ett speciellt objekt i JavaScript som hjälper dig att gå igenom en lista med objekt **ett i taget**.


### `Objekt` iteratorer


Till skillnad från matriser eller kartor är vanliga objekt **inte itererbara** med `for...of`. Om du försöker detta:


```javascript
const user = {
name: "Alice",
age: 30
}

for (const value of user) {
console.log(value)
}
```


Du kommer att få ett felmeddelande:


```
TypeError: user is not iterable
```


Det beror på att vanliga objekt inte har någon inbyggd iterator. Men JavaScript ger dig andra verktyg för att loopa över dem.


#### `Objekt.nycklar()`


Du kan använda `Object.keys(obj)` för att få en array av objektets **nycklar** och sedan loopa över den:


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


Detta skriver ut:


```
name
age
```


#### `Objekt.värden()`


För att loopa över **värdena** använder du `Object.values()`:


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


Detta skriver ut:


```
Alice
30
```


#### `Objekt.poster()`


Om du vill ha **både nyckeln och värdet** använder du `Object.entries()`:


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


Detta skriver ut:


```
name is Alice
age is 30
```


Även om objekt inte är itererbara direkt ger dessa metoder dig full tillgång till deras innehåll på ett sätt som fungerar bra med `for...of`.


Men hur fungerar iteratorer?


### `Symbol.iterator`


Hemligheten bakom alla iteratorer är en speciell **symbol** som heter `Symbol.iterator`.


Den här symbolen är en inbyggd nyckel som säger till JavaScript: "Det här objektet kan itereras."


När du anropar `myIterable[Symbol.iterator]()`, ger JavaScript dig tillbaka ett **iteratorobjekt** med en `.next()`-metod.


Låt oss se hur det ser ut:


```javascript
const colors = ["red", "green", "blue"]

const iterator = colors[Symbol.iterator]()

console.log(iterator.next()) // { value: 'red', done: false }
```


Varje anrop till `.next()` ger dig nästa värde. När det är klart returneras det:


```javascript
{ value: undefined, done: true }
```


### `nästa()`


Metoden `.next()` används för att hämta nästa objekt från sekvensen.


Varje gång du anropar `.next()` får du ett objekt med två nycklar:



- `värde`: det aktuella objektet
- `done`: en boolean som talar om ifall iterationen är över


Låt oss göra ett fullständigt exempel:


```javascript
const names = ["Lina", "Tom", "Eva"]      // declare an array
const iterator = names[Symbol.iterator]() // use the Symbol.iterator function to get an iterator for this array

let result = iterator.next()              // get the first element of the array

while (!result.done) {                    // repeat this loop until you reach the last element of the array, which is marked with { done: true }
console.log(result.value)               // print the value of each element
result = iterator.next()                // get the next element of the array
}
```


Detta skriver ut:


```
Lina
Tom
Eva
```


Det är så här en `for...of`-loop fungerar under huven: den använder detta mönster med `.next()`.


Du kommer att få samma resultat med


```javascript
const names = ["Lina", "Tom", "Eva"]

for (const result of names) {
console.log(result)
}
```


### Att göra en klass iterabel


Du kan också definiera din egen **iteratorklass** genom att lägga till en metod `[Symbol.iterator]()`.


Låt oss säga att vi vill ha en klass som representerar ett **talintervall**, t.ex. från 1 till 5.


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


Detta skriver ut:


```
1
2
3
4
5
```


Det här är vad som händer:



- Vi definierade en klass `Range`
- Inuti klassen implementerade vi `[Symbol.iterator]()`, så att JavaScript vet hur man itererar den
- Metoden `next()` ger tillbaka varje nummer ett efter ett
- När vi når `slutet` returneras `{ done: true }`


Nu fungerar vår `Range`-klass som en array, och vi kan använda den i alla loopar som förväntar sig en iterabel.


### Generatorfunktioner och "avkastning


För att göra det enklare att skapa iteratorer ger JavaScript dig **generatorfunktioner**, med hjälp av nyckelordet `function*` (det är `function` med en `*` i slutet) och nyckelordet `yield`.


Låt oss försöka:


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


Varje `yield` ger tillbaka ett värde och **pausar** funktionen tills nästa `.next()` anropas.


Du kan också loopa över en generator med `for...of`:


```javascript
for (const num of numberGenerator()) {
console.log(num)
}
```


Detta skriver ut:


```
1
2
3
```


## Samtidighet med callbacks

<chapterId>f3fc76ca-b3ef-54eb-a06e-501007002054</chapterId>


Hittills har vår kod varit **synkron**: den kör en rad i taget, i tur och ordning. Men vissa saker i den verkliga världen tar tid, och vi vill inte att hela programmet ska pausa medan vi väntar.


I det här kapitlet ska vi introducera ett nytt begrepp: **konkurrens**. Det gör att vi kan manipulera den ordning i vilken saker och ting görs. Detta är användbart när man hanterar saker som timers, användarinmatning eller läsning av filer från disk. JavaScript erbjuder olika verktyg för att hantera samtidighet.


### `setTimeout`


Med funktionen `setTimeout` kan du **köra en funktion senare**, efter att en viss tid har gått.


Exempel:


```javascript
console.log("Start")

setTimeout(
() => console.log("This runs after 2 seconds"),
2000
)

console.log("End")
```


Detta skriver ut:


```
Start
End
This runs after 2 seconds
```


Även om `setTimeout` dyker upp mitt i koden blockerar den inte resten. Istället schemalägger den funktionen för att köras **senare**, och går omedelbart vidare.


`2000` betyder 2000 millisekunder (vilket är 2 sekunder).

Här är en mer utförlig och nybörjarvänlig omskrivning av avsnitten **Callbacks** och **Promise**, med hjälp av datamanipulation och tydliga kommentarer hela tiden:


### Återkallelser


En **callback** är bara en funktion som vi ger till en annan funktion så att den kan **kallas senare**.


Låt oss titta på ett verkligt exempel med siffror. Tänk dig att vi har en lista med siffror och att vi vill dubbla var och en av dem och sedan tillämpa en funktion (återuppringningen) på den resulterande "fördubblade" matrisen, men vi vill göra det efter en liten fördröjning, som om vi väntar på något långsamt (som att ladda data från internet).


Här är en funktion som gör det med hjälp av en **callback**:


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


Låt oss försöka använda den här funktionen:


```javascript
const input = [1, 2, 3]

doubleNumbers(input, function(result) {
console.log("Here is the doubled array:", result)
})
```


Efter 1 sekund skrivs detta ut:


```
Here is the doubled array: [ 2, 4, 6 ]
```


**Vad är det som händer här?


1. Vi skickar `input` som en lista med siffror som vi vill fördubbla.

2. Vi skickar också en **callback-funktion** som talar om för programmet vad det ska göra *efter* dubbleringen.

3. I `doubleNumbers` simulerar vi en fördröjning med hjälp av `setTimeout`, sedan gör vi dubbleringen.

4. När det är gjort anropar vi återuppringningen på den resulterande "fördubblade" matrisen.


Den här tekniken fungerar, men tänk dig att du vill göra **fler steg** efter det, som att filtrera bort små tal och sedan lägga ihop dem. Du skulle behöva **nest** fler callbacks som denna:


```javascript
doubleNumbers(input, function(doubled) {
filterBigNumbers(doubled, function(filtered) {
sumNumbers(filtered, function(total) {
console.log("Final result:", total)
})
})
})
```


Detta är Hard att läsa och rörigt. Den här stilen kallas **callback hell**, och det är precis vad `Promise` skapades för att åtgärda.


## Samtidighet med löften

<chapterId>30fddaca-729f-5c8d-bf86-8dfc7b3c9800</chapterId>


Ett `Promise` är ett inbyggt JavaScript-objekt som representerar ett värde som **kommer att vara klart i framtiden**.


Vi kan skapa ett Promise så här:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve("It worked!") // This means everything went OK
})
```


Delen `new Promise()` skapar ett löfte.


Inuti den ger vi den en funktion med två parametrar:



- `resolve`, är en funktion som vi anropar när allt är framgångsrikt
- `reject`, är en funktion som vi anropar om något går fel


I exemplet ovan löser vi det bara omedelbart med meddelandet "Det fungerade!".


### `.then()`


Om du vill göra något **efter** att löftet har uppfyllts använder du `.then()`:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve(100) // This means everything went OK
})

promise.then(result => {
console.log("The result is:", result)
})
```


Detta skriver ut:


```
The result is: 100
```


Det värde som vi skickade till `resolve()` skickas till funktionen i `.then()` som `result`.


Låt oss simulera en uppgift som tar 2 sekunder med hjälp av `setTimeout`:


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


Detta väntar 2 sekunder och skriver sedan ut:


```
Done waiting!
```


### `avvisa()`


Låt oss skapa ett löfte som **felar**:


```javascript
const failingPromise = new Promise((resolve, reject) => {
reject("Something went wrong")
})
```


Om vi nu använder `.then()` på detta kommer ingenting att hända, eftersom `.then()` bara hanterar framgång.


För att hantera fel använder vi `.catch()`:


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


Detta skriver endast ut


```
Caught an error: Something went wrong
```


Det värde som skickas till `reject()` skickas till funktionen `.catch()`.


Låt oss bygga ett löfte som ** ibland fungerar och ibland misslyckas**, baserat på vissa villkor.


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


Nu kan vi kalla detta och hantera båda fallen:


```javascript
checkNumber(5)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Detta skriver ut:


```
Success: Positive number
```


Och om vi försöker med ett annat nummer:


```javascript
checkNumber(-1)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Den skriver ut:


```
Failure: Not a positive number
```


### Kedja operationer med hjälp av `Promise`



Vi kan skriva om vårt tidigare exempel med hjälp av `Promise`, och det kommer att se mycket renare ut.


Låt oss börja med att skriva en ny version av vår dubbleringsfunktion, men den här gången returnerar den ett **löfte**:


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


Nu kan vi använda `.then()` för att tala om för JavaScript vad som ska göras med resultatet:


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


Detta skriver ut:


```
Doubled numbers: [ 2, 4, 6 ]
```


Än så länge fungerar detta på samma sätt som callback-versionen, men nu är koden enklare att utöka och läsa.


Låt oss säga att vi vill lägga till fler steg:


1. Först ska du dubbla alla siffror

2. Ta sedan bort tal som är mindre än 4

3. Lägg slutligen ihop dem alla


Vi kan skriva en funktion för varje steg, alla med hjälp av löften:


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


Nu kan vi **kedja** ihop dem på det här sättet:


```javascript
const input = [1, 2, 3]

doubleNumbers(input)
.then(filterBigNumbers)
.then(sumNumbers)
.then(
result => console.log("Final result after all steps:", result)
)
```


Detta skriver ut:


```
Final result after all steps: 10
```


Låt oss gå igenom vad detta gör:


1. `doubleNumbers` fördubblar matrisen: `[2, 4, 6]`

2. `filterBigNumbers` tar bort allt ≤ 3: `[4, 6]`

3. `sumNumbers` lägger till de återstående talen: `4 + 6 = 10`

4. Slutligen skriver vi ut resultatet.


Varje `.then()` väntar på att steget före det ska avslutas. På så sätt kan vi bygga en **kedja av åtgärder** utan nestning. Detta gör koden mer läsbar och lättare att felsöka.


## Samtidighet med "async" och "await

<chapterId>6e93d29f-c8bf-5fd1-a9c9-4e794ee6cbd0</chapterId>


Vi såg hur `Promise`-kedjor hjälper oss att undvika callback-helvetet, men de kan fortfarande bli lite Hard att läsa när det är många steg inblandade.


Det är där `async` och `await` kommer in i bilden. De låter oss skriva asynkron kod **som ser ut som synkron kod**, vilket gör den lättare att förstå.


### Vad är "async"?


När du skriver nyckelordet `async` före en funktion, paketerar JavaScript automatiskt funktionens returvärde i ett Promise.


Låt oss se ett grundläggande exempel:


```javascript
async function greet() {
return "hello"
}
```


Om du anropar den här funktionen:


```javascript
const result = greet()
console.log(result)
```


Du kommer att få se det här:


```
Promise { 'hello' }
```


Även om du bara returnerade en sträng förvandlar JavaScript den till ett Promise åt dig. Du kan få det faktiska värdet med hjälp av `.then()` så här:


```javascript
greet().then( result => console.log(result) ) // prints "hello"
```


Eller så kan du använda `await`...


### Vad är `await`?


Nyckelordet `await` säger till JavaScript: "Vänta tills detta löfte har utförts, och ge mig sedan resultatet."


Men du kan bara använda `await` **inom en asynkron funktion**.


Låt oss skriva om exemplet med hjälp av `await`:


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


Nu kan vi använda resultatet som om det vore ett vanligt värde.


Låt oss göra något lite mer användbart nu.


### Simulering av en fördröjning med `await`


Vi ska skapa en enkel "vänta"-funktion som tar ett antal millisekunder som argument och bara löser upp efter så många millisekunder, utan att göra något annat:


```javascript
function wait(ms) {
return new Promise(resolve => {
setTimeout(resolve, ms)
})
}
```


Låt oss försöka använda den:


```javascript
async function test() {
console.log("waiting 2 seconds...")
await wait(2000)
console.log("done waiting")
}

test()
```


Detta skriver ut:


```
waiting 2 seconds...
done waiting
```


Du kan tänka på `await` som "pausa här tills löftet är gjort, fortsätt sedan"


Detta gör att du kan skriva kod på ett **top-to-bottom** sätt som beter sig asynkront, utan att kedja `.then()`-anrop.


### Inväntar data


Låt oss återanvända vårt tidigare exempel, där vi dubblar siffror, sedan filtrerar och sedan summerar. Men den här gången använder vi `async`/`await`.


Vi kommer att skapa 3 funktioner som simulerar väntan och returnerar Promises:


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


Låt oss nu skriva en "async"-funktion för att kombinera dem:


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


Detta skriver ut:


```
Final result: 10
```


Detta är mycket lättare att läsa än att kedja `.then()` eller nesta callbacks.


Det ser ut som ett vanligt steg-för-steg-program, men det beter sig fortfarande asynkront.


## Asynkrona Iteratorer

<chapterId>438b037d-9931-56d7-9052-7b4470f3c75b</chapterId>


Du har redan lärt dig om **iteratorer** och hur vi kan använda `for...of` för att loopa över arrayer och andra itererbara saker.


Men vad händer om det tar tid att få fram de data som vi vill iterera över?


Ibland vill vi loopa över saker som kommer **asynkront**, som meddelanden från en chatt, rader från en fil eller siffror från en långsam källa.


För att göra det ger JavaScript oss **async iteratorer**.


### Asynkrona generatorfunktioner


Det enklaste sättet att skapa en asynkron iterator är att använda en **asynkron generatorfunktion**.


Vi skriver det så här:


```javascript
async function* generateNumbers() {
yield 1
yield 2
yield 3
}
```


Det här ser ut som en vanlig generator, men med `async` före.


Vi kan nu använda `for await...of` för att konsumera värdena:


```javascript
async function run() {
for await (const n of generateNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


Detta kommer att skrivas ut:


```
Got number: 1
Got number: 2
Got number: 3
Done!
```


Vad är då skillnaden mot en vanlig generator?


Skillnaden är att vi nu kan använda `await` inuti generatorn.


Låt oss göra en fördröjningshjälpare igen:


```javascript
function wait(ms) {
return new Promise(resolve => setTimeout(resolve, ms))
}
```


Låt oss nu ge siffror **långsamt**:


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


Försök att använda den:


```javascript
async function run() {
for await (const n of generateSlowNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


### Varför använda asynkrona iteratorer?


Asynkrona iteratorer är användbara när:



- Alla värden kommer inte på en gång.
- Du vill hantera dem en i taget, **som de kommer**.
- Du arbetar med Promises och vill göra loopar på ett rent sätt.


Om du till exempel vill läsa in meddelanden från en chatt-server ett i taget eller ladda ner en stor fil i omgångar, ger asynkrona iteratorer dig ett sätt att skriva en `for`-loop som arbetar med fördröjda data.


### `Symbol.asyncIterator`


Vi kan också använda asynkrona iteratorer i anpassade klasser.


Här är ett exempel som producerar siffror med en fördröjning:


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


Vi kan nu använda `for await...of` precis som tidigare:


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


Detta gör att du kan skapa objekt som kan itereras över asynkront


## Assignment syntax socker

<chapterId>8b1ba7d8-ecfd-5470-b86e-73cb84ccc8b7</chapterId>


"Syntax sugar" betyder att man skriver något på ett kortare eller enklare sätt, utan att ändra vad det gör. Det är bara ett trevligare sätt att säga samma sak.


JavaScript har en del inbyggda syntaxsocker som gör att vi kan skriva renare och kortare deklarationer. I det här kapitlet tittar vi på hur man tilldelar värden baserat på ett villkor, uppdaterar variabler med matematik, hämtar värden från arrayer eller objekt och kopierar eller kombinerar dem med enklare syntax.


### Den ternära operatorn


I JavaScript kan du tilldela ett värde baserat på ett villkor med hjälp av **ternary operator**, vilket är ett kort sätt att skriva `if...else`.


Istället för att göra:


```javascript
let message

if (isMorning) {
message = "Good morning"
} else {
message = "Hello"
}
```


Du kan skriva:


```javascript
const message = isMorning ? "Good morning" : "Hello"
```


Det betyder..:



- Om `isMorning` är sant, använd `"God morgon"`
- Annars använder du `"Hello"`


Den allmänna formen är:


```javascript
condition ? valueIfTrue : valueIfFalse
```


Du kan också använda det i andra uttryck:


```javascript
console.log(isSunny ? "Go outside" : "Stay in")
```


Se bara till att använda det för **enkla** beslut. Om logiken är komplex, håll dig till `if...else`.


### Alternativa Assignment-operatörer


JavaScript har **snabboperatorer** för att utföra uppdrag i kombination med operationer.


Låt oss titta på det normala sättet:


```javascript
let counter = 1
counter = counter + 1
```


Detta kan förkortas till:


```javascript
let counter = 1
counter += 1 // same as counter = counter + 1
```


Här är de vanligaste:


| Operator | Meaning             |
| -------- | ------------------- |
| `+=`     | add and assign      |
| `-=`     | subtract and assign |
| `*=`     | multiply and assign |
| `/=`     | divide and assign   |

Exempel på detta:


```javascript
let score = 10
score += 5  // now score is 15
score *= 2  // now score is 30
score -= 10 // now score is 20
```


Dessa är användbara när du vill uppdatera en variabel med hjälp av dess eget värde.


### Destrukturering


*med *Destructuring** kan du enkelt ta värden från matriser eller objekt och lagra dem i variabler.


#### Arrayer


Anta att du har det:


```javascript
const colors = ["red", "green", "blue"]
```


Istället för att göra:


```javascript
const first = colors[0]
const second = colors[1]
```


Du kan göra det:


```javascript
const [first, second] = colors
```


Detta tilldelar:



- `först` till `"röd"`
- `andra` till `"Green"``


Du kan också hoppa över värden:


```javascript
const [,, third] = colors
console.log(third) // blue
```


#### Föremål


Du kan också extrahera värden från objekt:


```javascript
const user = { name: "Alice", age: 30 }

const { name, age } = user
console.log(name) // Alice
console.log(age)  // 30
```


Om egenskapen har ett annat namn än den variabel du vill ha kan du byta namn på den:


```javascript
const { name: username } = user
console.log(username) // Alice
```


Destrukturering gör din kod renare när du arbetar med objekt och matriser.


### Spread Syntax


Syntaxen **spread** använder `...` för att packa upp eller kopiera värden.


#### Arrayer


Du kan kopiera eller slå samman matriser:


```javascript
const a = [1, 2]
const b = [3, 4]

const both = [...a, ...b]
console.log(both) // [1, 2, 3, 4]
```


Du kan också klona en array:


```javascript
const original = [10, 20, 30]
const clone = [...original]
```


#### Föremål


Du kan göra samma sak med objekt:


```javascript
const a = { x: 1 }
const b = { y: 2 }

const merged = { ...a, ...b }
console.log(merged) // { x: 1, y: 2 }
```


Du kan också åsidosätta värden:


```javascript
const user = { name: "Alice", age: 30 }
const updated = { ...user, age: 31 }

console.log(updated) // { name: "Alice", age: 31 }
```


Detta är mycket användbart när du uppdaterar objekt utan att ändra originalet.


# NodeJS

<partId>42fe4d49-dace-5135-bb9e-b9d75034fb2a</partId>


## Hur kom vi till Node

<chapterId>0da1d60c-06c9-54e6-a181-ae7dabf6e3b8</chapterId>


I det här kapitlet ska vi lära oss lite om den historiska bakgrunden till JavaScript och NodeJS.


Historiska sammanhang är mycket viktiga när det gäller programvara, eftersom vi ofta använder verktyg som har byggts av andra människor och därför påverkas av beslut som de har fattat tidigare.


Genom att förstå bakgrunden till dessa beslut och hur de verktyg vi använder blev som de blev kan vi känna oss lite mindre förvirrade över vad vi håller på med.


### Ursprunget till JavaScript


JavaScript började som ett enkelt språk som var utformat för att göra webbsidor interaktiva.


På 1990-talet lade webbläsare som Netscape Navigator till JavaScript så att utvecklare kunde skriva kod som körs direkt i webbläsaren.


Den ursprungliga tanken var att Java skulle vara huvudspråket för att skapa webbplatser (med så kallade "Java-applets"), och JavaScript bara för mindre saker.


Grunddesignen gjordes av Brendan Eich, som vid den tiden var anställd på Netscape, på mindre än två veckor.


Men de flesta föredrog att använda JavaScript framför Java, och dessutom hade Java-applets en del säkerhetsproblem på den tiden, så så småningom togs Java bort som alternativ och JavaScript blev de facto-standarden för webbutveckling.


### V8-motorn


JavaScript är ett tolkat språk, i motsats till kompilerade språk som C.


Kod som skrivs i ett kompilerat språk omvandlas till en binär fil och den binära filen matas direkt till datorns CPU.


![](assets/en/6.webp)


Interpredspråk, å andra sidan, tenderar att vara mer användarvänliga och ligger närmare hur människor tänker ("hög nivå") snarare än hur maskiner fungerar ("låg nivå"); så de har vanligtvis en virtuell maskin byggd för att köra sin kod.


En virtuell maskin är ett specialprogram som sitter mellan den kod du skriver och CPU:n och exekverar din kod (eftersom CPU:n inte kan förstå den).


Detta gör att du kan programmera utan att veta för mycket om den underliggande maskinen, men det har också en kostnad när det gäller prestanda, eftersom datorn inte bara kör ditt program; den kör ett program (den virtuella maskinen) som kör ditt program.


I takt med att webbapplikationerna blev allt mer komplexa uppstod en efterfrågan på att förbättra prestandan i JavaScript. V8-motorn är den tolk som driver JavaScript i Google Chrome. Den utvecklades av Google och lanserades 2008.


Medan de äldre JavaScript-motorerna mestadels var traditionella virtuella maskiner, är V8-motorn en JIT-kompilator (just-in-time).


JavaScript-koden skickas till V8-motorn, som försöker kompilera delar av den som inbyggda binärfiler i farten. Detta gör att du kan få upplevelsen av ett högnivåspråk, med prestanda som ligger lite närmare lågnivåspråk. Detta har gjort JavaScript till det snabbaste högnivåspråket i världen, lite av en "bästa av två världar"-grej.


### NodeJS körtid


JavaScript är lätt att använda och ganska snabbt att köra, men efter lanseringen av V8 hade det en stor begränsning: det kunde bara köras i en webbläsare.


Varför är det ett problem?


Eftersom webbläsare exekverar kod som hämtas från miljontals olika källor på internet kan de lätt bli skadlig kod, så de är "sandboxade" från resten av operativsystemet.


![](assets/en/7.webp)


JavaScript kunde inte komma åt filsystemet och andra lokala resurser på din dator (åtminstone inte lika enkelt som andra språk), så det var en betydande begränsning för vilken typ av applikationer du kunde bygga med det.


År 2009 publicerade Ryan Dahl NodeJS, som är en runtime som gör att du kan använda V8-motorn utanför webbläsaren, direkt på datorns inbyggda operativsystem. Det lägger också till många funktioner som är användbara för att skriva program på serversidan och kommandoraden. Du kan t.ex. använda NodeJS för att skapa en webbserver, läsa och skriva filer eller bygga verktyg som automatiserar uppgifter.


![](assets/en/8.webp)


I den här kursen har vi hittills utforskat de JavaScript-funktioner som finns i både webbläsaren och i NodeJS. Dessa funktioner gjorde det möjligt för oss att definiera data och manipulera dem på abstrakta sätt. Under de kommande lektionerna kommer vi att utforska de funktioner som är specifika för NodeJS och som gör att vi kan interagera med operativsystemet.


## Argument på kommandoraden

<chapterId>960d20f3-c424-5d51-a041-ef17d2e94b6d</chapterId>


NodeJS ger oss bland annat möjlighet att bygga CLI:er (Command Line Interfaces).


För det behöver vi ett sätt att ta emot kommandoradsargument, vilket i Node görs med hjälp av det inbyggda `process`-objektet.


### `process`


NodeJS tillhandahåller ett speciellt objekt som heter `process` som representerar det program som körs för tillfället.


Du kan använda den för att inspektera miljön, den aktuella arbetskatalogen och till och med avsluta programmet när det behövs.


Till exempel:


```javascript
console.log(process.platform)
```


Här anges operativsystemets plattform, t.ex. `win32`, `linux` eller `darwin` (Mac).


### `process.argv`


När du kör ett NodeJS-program från terminalen kan du skicka extra ord (argument) efter skriptnamnet. Dessa lagras i `process.argv`.


Om du t.ex. kör det här kommandot:


```
node my_script.js alpha beta
```


Du kan skriva ut argumenten så här:


```javascript
console.log(process.argv)
```


Utmatningen kan se ut så här:


```
[ '/path/to/node', '/path/to/my_script.js', 'alpha', 'beta' ]
```


De två första posterna är alltid sökvägen till noden och sökvägen till ditt skript. Eventuella ytterligare ord som du skickat till skriptet kommer efter det.


Arrayen `process.argv` kan klippas som vilken annan array som helst med metoden `.slice()`, så för att bara få de argument som skickades kan du göra


```javascript
const args = process.argv.slice(2)

console.log(args)
```


Att ha tillgång till de argument som användaren skickar är grundläggande för att utveckla kommandoradsapplikationer.


## Moduler

<chapterId>4e1651a5-65fd-50bc-b22a-40313d5659ca</chapterId>


JavaScript-runtimes som NodeJS behandlar vanligtvis varje JavaScript-fil som en separat modul.


Tänk på en modul som en låda. Lådan har sitt eget privata utrymme, så de variabler och funktioner som du deklarerar i den påverkar inte koden i andra lådor. I princip har varje modul sitt eget scope.


En modul kan exportera en del av sitt innehåll och göra det tillgängligt för andra moduler, och den kan importera det innehåll som andra moduler har exporterat. Med JavaScript kan du exportera och importera innehåll mellan moduler, för att koppla ihop olika filer.


Ett JavaScript-program består ofta av flera moduler som är kopplade till varandra.


Varför använda moduler? Genom att dela upp din kod i moduler kan du organisera ditt program i mindre, tydligare och återanvändbara delar. Varje modul kan fokusera på bara en typ av uppgift, till exempel att hantera matematiska beräkningar, arbeta med filer eller formatera text.


### Gemensamma JS-moduler


I NodeJS kallas det vanligaste systemet för att hantera moduler för **CommonJS**.


I det här systemet kan du dela (exportera) kod från en modul med hjälp av `module.exports` och ladda (importera) den i en annan fil med hjälp av `require()`.


Om du vill göra något tillgängligt utanför en modul tilldelar du det till `module.exports`:


```javascript
const greeting = "Hello!"

module.exports = greeting
```


Här är det strängen `"Hello!"` som den här modulen exporterar.


För att använda den exporterade koden från en annan fil använder du funktionen `require()` med sökvägen till den filen:


```javascript
const greeting = require("./greeting.js")

console.log(greeting)
```


Detta skriver ut:


```
Hello!
```


Du kan exportera flera saker genom att samla ihop dem i ett anonymt objekt, till exempel


```javascript
const greeting1 = "hello"

const greeting2 = "hi"

module.exports = {
greeting1, greeting2
}
```


CommonJS var det modulsystem som ursprungligen antogs av NodeJS. Senare lades även ES-moduler till.


### ES-moduler


NodeJS stöder också en annan typ av moduler som kallas **ES Modules**, som är populära inom webbutveckling. De använder nyckelorden `export` och `import`.


ES-moduler utvecklades för webbläsaren och lades till i Node först senare. Om du vill använda dem kan du behöva använda `.mjs` som filtillägg i stället för `.js`, beroende på vilken Node-version du använder.


I en fil som heter `greeting.mjs` skriver vi


```javascript
export const greeting = "Hello!"
```

Som du kan se exporterar vi konstanten direkt där den definieras


I en annan fil som heter `index.mjs` importerar vi den:


```javascript
import { greeting } from "./greeting.mjs"

console.log(greeting)
```


Du kan exportera olika deklarationer i olika delar av filen, t.ex


```javascript
export const num = 10

export function double (x) {
return x*2
}
```


### NodeJS standardbibliotek


NodeJS innehåller också många inbyggda moduler. Dessa är färdiga moduler som tillhandahålls av NodeJS och som hjälper till med vanliga uppgifter som att läsa filer, arbeta med operativsystemet eller ansluta till nätverket.


Modulen `os` ger dig t.ex. information om ditt operativsystem:


```javascript
const os = require("os")

console.log(os.platform())
```


Du behöver inte installera dessa inbyggda moduler, de kommer med NodeJS. De utgör "standardbiblioteket" för körtiden och används av de flesta Node-applikationer för att göra saker som att läsa filer eller kommunicera via internet.


I de kommande kapitlen kommer du att få se några användbara exempel på hur de kan användas.


## Modulen `fs

<chapterId>911e953a-35ae-5ee7-bd74-372501c32e81</chapterId>


Modulen `fs` (förkortning för **filsystem**) är en del av NodeJS standardbibliotek. Den gör att du kan arbeta med filer och kataloger på din dator: du kan läsa filer, skriva filer, radera dem, byta namn på dem och mycket mer.


För att använda den måste du först importera den längst upp i din fil:


```javascript
const fs = require("fs")
```


### API för synkronisering


Det enklaste sättet att använda `fs` är med dess **sync**-metoder.


Dessa metoder blockerar programmet tills de är klara (så att nästa kodrad inte körs förrän operationen är klar).


Här följer ett exempel på synkron läsning av en fil:


```javascript
const fs = require("fs")

const data = fs.readFileSync("example.txt", "utf8")

console.log(data)
```


Om det finns en fil som heter `example.txt` i samma katalog som ditt skript, kommer detta att skriva ut dess innehåll.


Du kan också skriva till en fil synkront:


```javascript
const fs = require("fs")

fs.writeFileSync("output.txt", "Hello from Node!")

console.log("File written!")
```


Detta skapar (eller skriver över) en fil som heter `output.txt` med texten.


Här är några vanliga operationer som du kan göra med detta API:


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


Sync API är enkelt och bra för små skript, men eftersom det blockerar programmet tills det är klart kan det göra saker långsammare om du arbetar med stora filer eller en server.


### API för asynkrona återuppringningar


API:et **callback** är icke-blockerande: det låter NodeJS fortsätta att göra andra saker medan filoperationen sker.


I stället för att returnera resultatet direkt tar den en funktion (en **callback**) som anropas när operationen är klar.


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


Så här går det till:



- `fs.readFile` börjar läsa `example.txt`.
- NodeJS väntar inte, utan går vidare för att exekvera annan kod som du kanske har skrivit.
- När filen är färdigläst körs återuppringningen:



  - Om det uppstod ett fel, innehåller `err` felet.
  - I annat fall innehåller `data` innehållet.


Så här skriver du till en fil:


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


Samma idé: programmet stannar inte medan filen skrivs.


Några exempel på saker du kan göra med detta API:


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


Callback-API:t är bättre för servrar och stora uppgifter eftersom det inte blockerar programmet, men nästlade callbacks kan bli röriga om du kedjar många operationer. Det är därför ett löftesbaserat async-API har lagts till.


### Promise async API


Det promisebaserade API:et är modernt och fungerar utmärkt med `.then()` och `async/await`. Det är tillgängligt som `fs.promises`.


Du måste importera egenskapen `promises`:


```javascript
const fs = require("fs").promises
```


Använda `.then()`:


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


Eller ännu bättre, med hjälp av `async/await`:


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


Skriva till en fil:


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


Den vanliga listan med exempel för API:et:


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


När du skriver kod behöver du ofta använda kod som skrivits av andra, till exempel bibliotek som hjälper dig att arbeta med datum, färger, servrar eller nästan vad som helst annat.


I stället för att ladda ner och kopiera filer manuellt kan du använda en **package manager**.


En pakethanterare är ett verktyg som:



- nedladdningsbara paket
- håller reda på vilka paket ditt projekt behöver
- ser till att alla i ditt team har samma versioner av paketen


### Vad är NPM?


I NodeJS-världen är den mest populära pakethanteraren **NPM**, som står för *Node Package Manager*.


Du får NPM automatiskt när du installerar NodeJS.


Du kan kontrollera om du har NPM genom att köra detta i din terminal:


```
npm -v
```


Detta skriver ut den version av NPM som du har, t.ex:


```
10.2.1
```


### Skapa ett paket


I NodeJS är ett **package** bara en katalog med en `package.json`-fil i den.


Låt oss skapa en steg för steg.


1. Skapa en ny mapp för ditt projekt:


```
mkdir my_project
cd my_project
```


2. Kör det här kommandot:


```
npm init
```


Detta startar en interaktiv installation där du får frågor som namn på projektet, version, beskrivning etc.


Om du inte vill svara på allt och bara acceptera standardvärdena kan du använda:


```
npm init -y
```


När du har kört den kommer du att se en ny fil i din mapp som heter:


```
package.json
```


### `paket.json`


Filen `package.json` är bara en JSON-fil som lagrar metadata om ditt projekt.


Här är ett exempel:


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


Några viktiga områden:



- `namn`: namnet på ditt paket
- `version`: den aktuella versionen
- `main`: filen för startpunkten (som `index.js`)
- `scripts`: kommandon som du kan köra (t.ex. `npm start`)
- `dependencies`: listar alla paket som ditt projekt är beroende av


### Installera ett paket


Låt oss säga att du vill använda ett visst paket som heter `picocolors` för att lägga till färger i din terminalutmatning.


Du kan installera det genom att köra:


```
npm install picocolors
```


Du kan nu använda den i ditt projekt. Skapa en `index.js`-fil med


```javascript
const pico = require('picocolors')

console.log(
pico.green("This text is green!")
)
```


och försök att köra den. Terminalen bör skriva ut en färgad version av texten.


Vad gjorde NPM?



- Paketet hämtades och lagrades i en undermapp med namnet `node_modules/`
- det lade till en post under `dependencies` i ditt `package.json`
- den uppdaterade filen `package-lock.json`


Vad är `package-lock.json` ?


### `package-lock.json`


Den här filen skapas automatiskt av NPM.


Du kanske undrar, om vi redan har `package.json`, varför behöver vi en annan fil?

Här är skälet till detta:



- `package.json` anger bara vilken version **intervall** av ett paket som ditt projekt behöver.

Exempel:


```json
"dependencies": {
"picocolors": "^1.1.0"
}
```


`^1.1.0` betyder "vilken version som helst som är kompatibel med 1.1.x", så det är flexibelt.



- `package-lock.json` **fryser** de exakta versionerna av varje enskilt paket och deras underberoenden, så att alla som installerar ditt projekt får exakt samma fungerande installation.


Varför är detta viktigt?


Om du arbetar i ett team, om du distribuerar ditt projekt till en server eller om du återkommer till det i framtiden vill du vara säker på att det fortfarande fungerar på samma sätt.

Om paketen har uppdaterats och du installerar om utan en låsfil kan du få en något annorlunda version som beter sig annorlunda.


Genom att behålla `package-lock.json` i ditt projekt kommer NPM alltid att installera de exakta versioner som anges där, vilket säkerställer att alla har samma miljö.


`package-lock.json` låser allt till en mycket specifik version, för att göra projektet mer reproducerbart på andra maskiner.


Men om ditt paket behöver användas av många människor kan du istället välja att inte överföra det, så att NPM bara hittar filen `package.json` och det får installera automatiskt de senaste versionerna som tillåts i den filen.


Men det här är saker som du bör oroa dig för senare, när du börjar publicera din egen kod. För tillfället introducerade vi grunderna i NPM bara för att du ska kunna hitta och använda de bibliotek som publiceras av andra utvecklare i dina projekt.



## Nätverk i NodeJS

<chapterId>f2cabd8b-754b-5c97-8d6a-8412a9a184c7</chapterId>


NodeJS används ofta som ett språk för backend: du kan förvandla ditt skript till en server och även använda det för att göra förfrågningar till andra servrar.


I det här kapitlet introducerar vi några grundläggande nätverksfunktioner som gör det möjligt för dig att göra det.


### `hämtning()`


Om du vill att ditt program ska hämta data från en webbplats eller ett API måste du göra en **HTTP-begäran**.


I moderna versioner av NodeJS kan du använda den inbyggda funktionen `fetch()`.


Här är ett exempel på hur du gör en GET-begäran till ett API:


```javascript
const response = await fetch("https://jsonplaceholder.typicode.com/posts/1")
const data = await response.text()

console.log(data)
```


När du kör detta kommer du att se något liknande:


```
{
"userId": 1,
"id": 1,
"title": "...",
"body": "..."
}
```


Det här är vad som händer:


1. `fetch()` tar en URL och gör en förfrågan.

2. Den returnerar ett **Promise** som löses upp till ett `Response`-objekt.

3. `response.text()` läser upp svarstexten som en sträng.


Men den sträng du får tillbaka är faktiskt JSON. Vad är det för något?


### JSON


När man arbetar med webb-API:er skickas och tas data ofta emot i form av **JSON**, vilket står för JavaScript Object Notation.


JSON är bara ett textformat som ser ut ungefär som JavaScript-objekt. Till exempel:


```json
{
"name": "Alice",
"age": 30,
"likes": ["apples", "bananas"]
}
```


Objektet `JSON` är ett inbyggt verktyg i JavaScript som kan användas för att arbeta med detta dataformat.


Du kan konvertera ett JavaScript-objekt till en JSON-sträng med hjälp av `JSON.stringify()`:


```javascript
const user = { name: "Alice", age: 30 }

const jsonString = JSON.stringify(user)

console.log(jsonString)
```


Detta skriver ut:


```
{"name":"Alice","age":30}
```


Du kan också konvertera JSON-text tillbaka till ett JavaScript-objekt med hjälp av `JSON.parse()`:


```javascript
const jsonText = '{"name":"Bob","age":25}'

const obj = JSON.parse(jsonText)

console.log(obj)
```


Detta skriver ut:


```
{ name: 'Bob', age: 25 }
```


Var försiktig med detta: `JSON.parse()` kommer att ge ett felmeddelande om strängen inte är giltig JSON.


```javascript
JSON.parse("not json") // ❌ Error!
```


Se därför till att strängen är korrekt formaterad.


### `http`-server


NodeJS gör att du kan skapa en webbserver utan att installera något annat.


Du kan använda den inbyggda modulen `http` för att hantera förfrågningar från klienter och skicka svar tillbaka.


Här följer ett mycket enkelt exempel:


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


När du kör detta skript och öppnar `http://localhost:3000` i din webbläsare, kommer du att se:


```
Hello from NodeJS server!
```


Det här är vad som händer i koden:


1. Du har importerat `http`-servern från Node standardbibliotek.

2. `http.createServer()` skapar en server. Du skickade till `http.createServer()` ett callback `(req, res) => {...}` som ska utföras varje gång någon ansluter.

3. Du tilldelade svaret en statuskod på 200 (vilket indikerar en lyckad operation). Du kan läsa mer om http-statuskoder [här](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

3. `res.end()` skickar svaret och avslutar anslutningen.

4. `server.listen(3000)` startar servern på port 3000.


Du kan också kontrollera `req.url` och `req.method` i begäran för att hantera olika sökvägar eller begärandetyper.


Exempel med routing:


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


Det här är mycket grundläggande exempel. För att bygga mer avancerade servrar skulle de flesta utvecklare förmodligen ladda ner ett färdigt backend-bibliotek som [express] (https://www.npmjs.com/package/express).


## Bearbetning av data: buffertar, händelser, strömmar

<chapterId>8c9623f0-a604-51a4-8fe4-871c849d3e3b</chapterId>


I det här kapitlet introducerar vi främst tre klasser av objekt:



- `Buffer`, som representerar små bitar av binär data
- `EventEmitter`, som kan användas för att spåra ett steg i en asynkron process genom att sända ut signaler som kallas "events"
- `Stream`, som gör att vi kan bearbeta stora datamängder en `Buffer` i taget, och som spårar processen genom att avge händelser


Dessa är extremt vanliga i professionell NodeJS-kod, så även om du kanske inte använder dem i dina första projekt är det bra att få en grundläggande förståelse för när du behöver interagera med dem. av dem


### Buffertar


I NodeJS är en **buffer** en typ av objekt som används för att arbeta med binära data.


Du kan se en buffert som en behållare med fast storlek för råa bytes.


Så här skapar du en buffert från en sträng:


```javascript
const buf = Buffer.from("hello")
console.log(buf)
```


Detta skriver ut något i stil med:


```
<Buffer 68 65 6c 6c 6f>
```


Dessa siffror (`68`, `65`, `6c`, etc.) är hexadecimala representationer av bokstäverna i `"hello"`.


Du kan konvertera tillbaka den till en sträng så här:


```javascript
console.log(buf.toString())
```


Detta skriver ut:


```
hello
```


Du kan också skapa en buffert av en viss storlek som är fylld med nollor:


```javascript
const buf = Buffer.alloc(10)
console.log(buf)
```


Detta skriver ut något i stil med:


```
<Buffer 00 00 00 00 00 00 00 00 00 00>
```


Du kan skriva in i bufferten:


```javascript
buf.write("abc")
console.log(buf)
```


Och du kan komma åt enskilda bytes:


```javascript
console.log(buf[0]) // prints the ASCII number for 'a', which is 97
```


Buffertar är särskilt användbara när du behöver manipulera data på en mycket låg nivå.


### Händelser


I JavaScript är en **händelse** något som händer i ditt program och som du kan reagera på.


Till exempel:



- en fil laddas färdigt
- en timer går av
- en användare klickar på en knapp
- en nätverksbegäran returnerar data


En **händelse** är bara en signal om att något har hänt, och du kan skriva kod för att lyssna efter dessa händelser och reagera på dem.


I NodeJS kan många objekt avge händelser. Dessa objekt kallas **EventEmitters**.


Här är ett exempel:


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


Detta skriver ut:


```
Hello! An event happened.
```


Så här gör vi:


1. Vi skapar ett `EventEmitter`-objekt.

2. Vi säger till den att köra en återuppringning när händelsen "greet" inträffar, med hjälp av `.on("greet")`.

3. Senare utlöser vi händelsen `"greet"` med hjälp av `.emit()`.

4. Vårt återuppringningsprogram körs


Du kan skicka data tillsammans med händelsen:


```javascript
emitter.on("greet",
(name) => console.log(`Hello, ${name}!`)
)

emitter.emit("greet", "Alice") // first argument is the type of event, second argument is the data we pass with this event
```


Detta skriver ut:


```
Hello, Alice!
```


Du kan registrera lyssnare för andra händelser också:


```javascript
emitter.on("goodbye", () => {
console.log("Goodbye!")
})

emitter.emit("goodbye")
```


Du kan koppla så många lyssnare du vill till en typ av händelse, och du kan utlösa många olika typer av händelser från samma emitter.


Många objekt i NodeJS avger händelser för att tala om för resten av programmet att något händer.



### Vad är strömmar?


Streams kombinerar buffertar och händelser för att hjälpa oss att bearbeta data.


När vi arbetar med filer, data från nätverket eller till och med lång text behöver (eller vill) vi inte alltid ladda in allt i minnet på en gång. Det kan gå långsamt, eller till och med krascha programmet om datan är för stor.


I stället kan vi bearbeta data **lite i taget**, allteftersom de anländer eller läses, ungefär som att dricka vatten genom ett sugrör i stället för att försöka dricka hela glaset på en gång. Detta kallas för en **ström**.


I NodeJS är en stream ett objekt som låter dig läsa data från en källa eller skriva data till en destination **en bit i taget**.


NodeJS har fyra huvudtyper av strömmar:



- Readable**: strömmar som du kan läsa data från (som att läsa en fil)
- Writable**: strömmar som du kan skriva data till (som att skriva till en fil)
- Duplex**: strömmar som är både läsbara och skrivbara
- Transform**: som duplexströmmar, men de kan ändra (transformera) datan när den flödar


### Läsbara strömmar


Låt oss säga att du har en `bigfile.txt` att bearbeta. Du kan skapa en läsbar ström med modulen `fs` för att läsa filen bit för bit.


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


Vad händer här?


1. `fs.createReadStream()` skapar en läsbar ström.

2. När en del av filen är klar skickar strömmen ut en `data`-händelse och ger oss en "bit" data (en `Buffer`). Vi skriver ut delen.

3. När hela filen har lästs ut utlöses händelsen `end`.

4. Om det uppstår ett fel (t.ex. att filen inte finns) utlöses händelsen `error`.


På så sätt kan du läsa stora filer utan att ladda dem alla i minnet på en gång.


Om vi vill att data ska komma i en läsbar form (i stället för binär) kan vi ange kodningen av strömmen:


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


Koden kommer nu att skriva ut filen i mänskligt läsbar form.


### Skrivbara strömmar


Med en skrivbar ström kan du skicka data någonstans, bit för bit.


Här är ett exempel på hur man skriver till filen `target.txt` med hjälp av en ström:


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


Så här går det till:


1. `fs.createWriteStream()` skapar en skrivbar ström.

2. Vi skriver lite text till den med hjälp av `.write()`.

3. När vi är klara anropar vi `.end()` för att stänga strömmen.

4. När all data har skrivits ut skickas eventet "Finish".

5. Om något går fel utlöses händelsen `error`.


Precis som läsbara strömmar är skrivbara strömmar bra för stora datamängder eftersom de inte behöver hålla allt i minnet på en gång.


### Rörledningsflöden


En av de häftigaste sakerna med strömmar är att du kan **pipa** dem tillsammans: koppla en läsbar ström direkt till en skrivbar ström.


```javascript
const fs = require("fs")

const readable = fs.createReadStream("bigfile.txt")
const writable = fs.createWriteStream("target.txt")

readable.pipe(writable)
```


Här:



- Den läsbara strömmen läser från `bigfile.txt`.
- Den skrivbara strömmen skriver till `copy.txt`.
- `.pipe()` skickar data direkt från den läsbara till den skrivbara strömmen.


### Duplex-strömmar


En duplexström är både läsbar och skrivbar. Ett exempel är en nätverkssocket: du kan skicka data till den och ta emot data från den.


Här följer ett mycket enkelt exempel med modulen `net`:


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


I detta exempel:



- Objektet `socket` är en duplexström.
- Du kan `skriva()` till den och även lyssna efter `data`-händelser från den.


### Transformera strömmar


En transformström är en duplexström som också modifierar de data som passerar genom den.


Du kan t.ex. använda den inbyggda modulen `zlib` för att komprimera eller dekomprimera data.


Så här komprimerar du en fil med hjälp av en transformström:


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


Och för att dekomprimera den tillbaka:


```javascript
const readable = fs.createReadStream("bigfile.txt.gz")
const unzip = zlib.createGunzip()
const writable = fs.createWriteStream("bigfile.txt")

readable.pipe(unzip).pipe(writable)

writable.on("finish", () => {
console.log("File decompressed.")
})
```


Transform streams är mycket användbara för uppgifter som komprimering, kryptering eller ändring av filformat under streaming.


### Bakåtsträvande


Ibland är en skrivbar ström långsam när det gäller att hantera data. Om vi fortsätter att skicka data till en skrivbar ström snabbare än den kan hantera, kan vi få problem. Detta kallas **backpressure**.


Om du anropar metoden `.write()` på en skrivbar ström returnerar den en boolean som informerar dig om strömmen behöver en paus; du kan behöva kontrollera dess returvärde, så här:


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


Detta var ett illustrativt exempel på manuell piping av data från en läsbar till en skrivbar enhet och manuell hantering av mottrycket.


Vanligtvis använder vi metoden `.pipe()` för att överföra data, eftersom den hanterar mottryck automatiskt.


Så du behöver bara oroa dig för baktryck när du av någon anledning manuellt anropar `.write()`.


## Slutord

<chapterId>139e2ab8-df67-525a-85f0-5a2fa5e478f2</chapterId>


Så, det var det, om du följde med i lektionerna bör du nu kunna skriva några enkla program i NodeJS.


Jag skulle föreslå att du gör just det: efter att ha lärt dig grunderna är det bästa sättet att öva och bli en bättre programmerare att bygga några personliga projekt.


Det spelar egentligen ingen roll vad du bygger, det viktiga är att du utmanar dig själv att lösa problem med kod.


Moderna programmeringsspråk är otroligt kraftfulla, och NodeJS är förmodligen den bästa verktygslådan att experimentera med i den här fasen av din resa.


Lycka till!


# Sista avsnittet


<partId>322624d8-6fbc-11f0-a67a-5b145f10afc1</partId>


## Recensioner & betyg


<chapterId>3e93ac86-6fbc-11f0-8bae-9b2ed7914843</chapterId>

<isCourseReview>true</isCourseReview>

## Slutsats


<chapterId>49b3b9b2-6fbc-11f0-9870-5f5adcd3a0eb</chapterId>


<isCourseConclusion>true</isCourseConclusion>