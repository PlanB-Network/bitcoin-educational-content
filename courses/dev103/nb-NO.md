---
name: Grunnleggende JavaScript og NodeJS
goal: Lær grunnleggende JavaScript-programmering og NodeJS-utvikling for å bygge praktiske applikasjoner og verktøy.
objectives: 

  - Beherske grunnleggende JavaScript-syntaks, -typer og -kontrollflyt
  - Forstå funksjoner, objekter og klasser i JavaScript
  - Lær deg teknikker for feilhåndtering og feilsøking
  - Bli introdusert til NodeJS og dets økosystem

---

# Start utviklingsreisen din


Velkommen til dette kurset i JavaScript og NodeJS.


JavaScript er det mest populære programmeringsspråket i verden: Det er skriptspråket i moderne nettlesere, så det er i utgangspunktet umulig å bygge en moderne webapplikasjon uten å skrive *noe* JavaScript, og med NodeJS-kjøretiden kan det også brukes utenfor nettlesere, for å lage skript og applikasjoner som kjører direkte på datamaskinen din.


Dette kurset er utviklet for deg som er helt ny i programmering, eller som har brukt andre språk før, men som ønsker å forstå hvordan JavaScript fungerer, spesielt i sammenheng med NodeJS.


Ved kursets slutt skal du kunne skrive dine egne programmer i JavaScript, bruke NodeJS standardbibliotek og installere og bruke tredjepartspakker til å bygge nyttige verktøy.


+++
# Grunnleggende JavaScript

<partId>a617327c-e5a2-52ca-9380-c63f44623dd4</partId>


## Oppsett

<chapterId>ba05a290-1782-5268-87c9-62fd09590e05</chapterId>




Et JavaScript-program er bare en samling av (en eller flere) tekstfiler som inneholder kommandoer som skal utføres av en JavaScript-kjøretid.


Navnene på disse tekstfilene slutter vanligvis med filtypen `.js`, for eksempel `my_script.js`, `my_program.js` osv.


Kommandoene de inneholder, er skrevet i programmeringsspråket JavaScript.


En JavaScript-kjøretid er et spesielt program som kjører disse filene.


![](assets/en/1.webp)


### NodeJS-kjøretid


Den vanligste JavaScript-kjøretiden er NodeJS.


IDE-en din kan allerede inneholde det, eller du må kanskje laste det ned fra [offisielt nettsted](https://nodejs.org/en/download).


På nedlastingssiden finner du instruksjoner for alle de tre største operativsystemene (OS): Windows, Linux og MacOS. Det forutsettes at du vet hvordan du åpner en terminal i operativsystemet ditt.


Siden NodeJS er tilgjengelig for alle tre operativsystemene, vil programmene du skriver, kunne kjøres på dem alle (med unntak av noen unntakstilfeller).


Det betyr at du for eksempel kan skrive et enkelt videospill i JavaScript på Windows-PC-en din og sende det til en venn som kjører det på Mac-en sin.


![](assets/en/2.webp)














### Første program (hello world)


Når man lærer seg et programmeringsspråk, er det vanlig at det første programmet man skriver, består i å skrive ut "hello world!" på konsollen.


Opprett en katalog som heter `my_js_code/`, med en fil som heter `main.js` (disse navnene er vilkårlige).


Åpne katalogen med kodeeditoren din.


Skriv denne koden inn i filen din:


```javascript
console.log("hello world!")
```


Åpne en terminal og kjør denne kommandoen for å kjøre programmet:


```
node main.js
```


Resultatet skal være


```
hello world!
```


### Hva skjedde


I JavaScript er alt et "objekt".


`console` er et objekt som brukes til å feilsøke programmet.


`console.log` er den mest brukte metoden i `console`. Den skriver bare ut de argumentene du sender til den.


Du sender argumenter til `console.log` ved hjelp av runde parenteser `()`.


Hvis du for eksempel vil skrive ut tallet `1000`, skriver du bare


```javascript
console.log(1000)
```


Utfør den deretter ved å kjøre


```
node main.js
```


i terminalen din (fra nå av vil dette kurset forutsette at du vet at det er slik du kjører et program).


Dette skal skrives ut


```
1000
```


Du kan sende flere ting, for eksempel


```javascript
console.log(16, 8, 1993)
```


Dette vil skrive ut


```
16 8 1993
```


## Variabler og kommentarer

<chapterId>23050ab7-343b-5edf-9d37-e4e782e27ce0</chapterId>


Programmer utfører vanligvis operasjoner på data.


Variabler er som navngitte bokser som vi bruker til å lagre data. De gjør det mulig å knytte et stykke data til et bestemt navn, slik at vi senere kan hente det frem ved hjelp av dette navnet.


### `let`-erklæringer


For å deklarere en variabel i JavaScript kan vi bruke nøkkelordet `let`.


Etter å ha skrevet `let` skriver vi navnet vi vil gi variabelen, deretter et `=`-tegn, og så verdien vi vil lagre.


For eksempel:


```javascript
let age = 25

console.log(age)
```


Navnet på en variabel (teknisk sett kalt "identifikator") kan vanligvis inneholde bokstaver, understrek (`_`), dollartegnet (`$`) og tall, selv om det første tegnet ikke kan være et tall.


I koden ovenfor har vi deklarert en variabel som heter `alder` og lagret verdien `25` i den.


Deretter skrev vi ut verdien ved hjelp av `console.log(age)`.


Hvis du kjører denne koden med `node main.js`, vil utdataene være:


```
25
```


Identifikatorer er sensitive for store og små bokstaver, noe som betyr at små og store bokstaver teller som forskjeller i identifikatorer, slik at for eksempel


```javascript
let age = 25

let Age = 20

console.log(age)
```


vil skrive ut 25, fordi de regnes som to helt separate variabler!


Du kan også lagre strenger (tekst) i en variabel:


```javascript
let message = "hello again"

console.log(message)
```


Dette vil skrives ut:


```
hello again
```


Akkurat som før brukte vi `console.log()` for å skrive ut verdien som er lagret i variabelen.


Nå gjør vi begge deler sammen:


```javascript
let age = 25

let message = "hello again"

console.log(age)

console.log(message)
```


Hvis du kjører dette, skrives det ut:


```
25
hello again
```

### Omdisponering


Variabler som er deklarert med `let`, kan endres etter at de er opprettet.


Dette kalles reassignment.


```javascript
let score = 10

console.log(score)

score = 15

console.log(score)
```


Først tilordner vi `10` til `score`, og skriver det deretter ut.


Deretter endrer vi verdien av `score` til `15` og skriver den ut på nytt.


Utdataene vil være:


```
10
15
```


Dette er svært nyttig når verdien endres over tid, for eksempel i et spill der poengsummen øker.


La oss legge til en annen variabel i miksen:


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


Dette vil skrives ut:


```
10
Alice
20
Bob
```


Som du kan se, ble både `score` og `player` endret.


### `const`-erklæringer


Men de fleste ganger ønsker vi ikke at en variabel skal endres etter at den er opprettet. Til det bruker vi `const`.


`const` er en forkortelse for "konstant". Når du har tilordnet en verdi til en `const`-variabel, kan du ikke endre den.


```javascript
const pi = 3.14
console.log(pi)
```


Dette skriver ut:


```
3.14
```


Men hvis du prøver å gjøre dette:


```javascript
const pi = 3.14
console.log(pi)

pi = 99 // this line will cause an error
console.log(pi)
```


JavaScript vil gi deg en feilmelding som:


```
TypeError: Assignment to constant variable.
```


Dette er fordi `pi` ble deklarert ved hjelp av `const`, og du kan ikke endre verdien etter det. Du kommuniserer til JavaScript-tolken at du ikke vil at variabelen skal endres.


Dette er nyttig fordi det reduserer sjansene for å endre det ved en feiltakelse. Når programmer blir veldig store, med tusenvis av kodelinjer, er det umulig å følge med på alt som skjer samtidig (det er hovedgrunnen til at vi bruker datamaskiner, for å utføre komplekse prosesser som vi ikke kan beregne med hjernen vår), så det blir nyttig å ha begrensninger som dette, som gjør programmet mer deterministisk.


Det er god praksis å alltid deklarere verdiene våre som `const`, med mindre vi er sikre på at vi ønsker å endre dem senere.


### Kommentarer i JavaScript


Noen ganger ønsker vi å skrive notater i koden vår som ikke kjøres. Disse kalles kommentarer.


Kommentarer ignoreres av programmet når det kjører, men er nyttige når vi skal forklare ting for oss selv eller andre.


For å skrive en kommentar på én linje, bruk `//`


```javascript
// This is a comment
const x = 10 // This is also a comment
console.log(x)
```


Dette vil fortsatt skrives ut:


```
10
```


Kommentarene er bare der for at mennesker skal kunne lese dem.


Du kan også skrive kommentarer på flere linjer ved hjelp av `/*` og `*/`


```javascript
/*
This is a multi-line comment.
It can span several lines.
*/
const y = 20
console.log(y)
```


Dette vil skrive ut


```
20
```


Og kommentaren vil bli ignorert.


Du kan bruke kommentarer til å legge til små merknader i koden din, slik at du kanskje husker hva den gjør og hvorfor den er skrevet på en bestemt måte. Det kan også hjelpe andre programmerere med å forstå den.


## Grunnleggende typer: tall, strenger, boolske tegn

<chapterId>cfdb04f6-21a8-5143-bbf9-7aaae04962f0</chapterId>


I JavaScript forteller en "type" deg hva slags data en verdi er.


Javascript har noen få grunnleggende typer, og i dette avsnittet skal vi se nærmere på noen av dem.


### Tall og aritmetiske operasjoner


Den første typen vi skal introdusere, er `number`.


Tall i JavaScript kan være heltall (som `5`) eller desimaltall (som `3,14`).


Du kan regne med dem: addisjon, subtraksjon, multiplikasjon og divisjon.


Her er et grunnleggende eksempel:


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


Dette vil skrives ut:


```
15
5
50
2
```


Du kan også bruke parenteser `()` for å kontrollere rekkefølgen på operasjonene:


```javascript
const result = (2 + 3) * 4
console.log(result)
```


Dette skriver ut:


```
20
```


Uten parentesen ville det vært `2 + 3 * 4`, som er:


```javascript
const result = 2 + 3 * 4
console.log(result)
```


Det ville skrevet ut:


```
14
```


I vanlig matematikk skjer nemlig multiplikasjon før addisjon.


### Strenger og interpolasjon


Den andre JavaScript-typen vi skal introdusere, er `streng`.


Strenger er tekststykker. Du kan bruke enkle anførselstegn `'...'` eller doble anførselstegn `"..."` for å lage dem.


```javascript
const greeting = "hello"
const name = 'Bob'
console.log(greeting)
console.log(name)
```


Dette skriver ut:


```
hello
Bob
```


For å kombinere strenger kan du bruke operatoren `+`:


```javascript
const greeting = "hello"
const space = " "
const name = "Bob"

const fullGreeting = greeting + space + name
console.log(fullGreeting)
```


Dette vil skrives ut:


```
hello Bob
```


Men det finnes en finere måte å kombinere strenger på, kalt **strenginterpolasjon**. Du bruker backticks for å deklarere strengen ```...``` og skriver variabler ved hjelp av `${...}` inne i strengen:


```javascript
const greeting = "hello"
const name = "Bob"

const fullGreeting = `${greeting} ${name}`
console.log(fullGreeting)
```


Dette skrives også ut:


```
hello Bob
```


Du kan inkludere et hvilket som helst uttrykk inne i `${...}`:


```javascript
const age = 30
console.log(`Next year, I will be ${age + 1} years old.`)
```


Dette skriver ut:


```
Next year, I will be 31 years old.
```


Interpolasjon er svært vanlig i moderne JavaScript.


### Boolske tall, sammenligning og logiske operasjoner


Den tredje typen vi skal introdusere, er `boolsk`. Den er oppkalt etter matematikeren George Boole, som oppfant den boolske logikken.


Booleaner er enkle: bare to mulige verdier, `sant` og `falsk`.


Du kan lagre dem i variabler:


```javascript
const theSkyIsBlue = true
const thisCourseIsBad = false

console.log(theSkyIsBlue)
console.log(thisCourseIsBad)
```


Dette skriver ut:


```
true
false
```


Du kan kombinere boolske tegn ved hjelp av logiske operatorer:



- `&&` betyr "og", og den returnerer `sant` bare hvis **begge** verdiene er `sanne`, ellers returnerer den `falsk`
- `||` betyr "eller", og den vil returnere `sant` hvis **mindst én** av verdiene er `sant`, ellers (hvis begge er falske) vil den returnere `falsk`
- `!` betyr "ikke", det brukes foran en boolsk, og det vil snu den: hvis den boolske er `sann`, vil den returnere `falsk`, og vice versa.


![](assets/en/3.webp)


Eksempler:


```javascript
const isSunny = true
const isWarm = true

console.log(isSunny && isWarm)  // true
console.log(isSunny || isWarm)  // true
console.log(!isSunny)           // false
```


Du kan sammenligne verdier i JavaScript ved hjelp av operatorer som `>`, `<`, `===` og `!==`. Resultatet av disse sammenligningene er alltid en boolsk verdi.


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


Javascript har også `>=` for å bety "større eller lik" og `<=` for å bety "mindre eller lik".


Boolske, sammenlignende og logiske operatorer kombineres ofte i programmer for å angi komplekse betingelser, for eksempel for å sikre at "e-posten er ankommet OG at den inneholder bildet jeg trenger ELLER at lengden på e-posten er lenger enn 10000 tegn". Du vil senere oppdage at dette er viktige byggesteiner for å konstruere logikken i programmet.


## Matriser, null, udefinert

<chapterId>7bf18183-5eae-53ed-83d2-b04982145d81</chapterId>


I dette avsnittet tar vi for oss ytterligere tre typer som er svært vanlige i JavaScript-programmer:



- Matriser**: sekvenser av verdier
- udefinert**: en spesiell verdi som betyr at "ingenting ble tildelt"
- null**: en annen spesiell verdi som betyr "med vilje tom"


### Matriser og indekstilgang


En **array** er en type som kan inneholde flere verdier i en liste.


Du oppretter en matrise ved å bruke hakeparenteser `[]` og skille elementene med komma.


Her er et grunnleggende eksempel:


```javascript
const numbers = [10, 2, 88]
console.log(numbers)
```


Dette skriver ut:


```
[ 10, 2, 88 ]
```


Du kan lagre hva som helst i en matrise, ikke bare tall:


```javascript
const things = ["apple", 42, true]
console.log(things)
```


Dette skriver ut:


```
[ 'apple', 42, true ]
```


For å få tilgang til et bestemt element i matrisen bruker vi en **indeks**. Indeksen er posisjonen til elementet, med start fra **0**.


Så i denne matrisen:


```javascript
const colors = ["red", "green", "blue"]
```



- `colors[0]` er `"rød"`
- `farger[1]` er `"Green"`
- `colors[2]` er `"blue"`


La oss prøve:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[0])
console.log(colors[1])
console.log(colors[2])
```


Dette vil skrives ut:


```
red
green
blue
```


Du kan tilordne en verdi til en bestemt indeks i en matrise


```javascript
const colors = ["red", "green", "blue"]

colors[1] = "yellow"

console.log(colors)
```


Dette vil skrives ut:


```
[ 'red', 'yellow', 'blue' ]
```


Du kan bruke et hvilket som helst naturlig tall som indeks, til og med et som er lagret i en variabel


```javascript

const i = 1
const colors = ["red", "green", "blue"]
console.log(colors[i])
```


Dette vil skrives ut:


```
green
```


Men hvis du prøver å få tilgang til en indeks som ikke finnes, vil du få `undefined`:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[3])
```


Dette skriver ut:


```
undefined
```


Hva er det der?


### `undefinert`


Spesialverdien `undefined` betyr "ingen verdi ble tilordnet".


Hvis du oppretter en variabel uten å gi den en verdi, blir den `udefinert`:


```javascript
const name
console.log(name)
```


Dette skriver ut:


```
undefined
```


Fordi vi ikke har tilordnet noe til `name`, setter JavaScript det til `undefined` som standard.


Som vi har sett tidligere, kan du også få `undefined` når du får tilgang til en matriseindeks som ikke eksisterer:


```javascript
const fruits = ["banana", "apple"]
console.log(fruits[2]) // There is no index 2
```


Dette skriver ut:


```
undefined
```


### `null` og hvordan det skal behandles


`null` er også en spesiell verdi. Det betyr "ingenting er her, og jeg gjorde det med vilje"


I motsetning til `undefined`, som er automatisk, er `null` noe du selv må angi.


For eksempel:


```javascript
const currentUser = null
console.log(currentUser)
```


Dette skriver ut:


```
null
```


Hvorfor bruke `null`? Kanskje du forventer en verdi senere, men den er ikke klar ennå:


```javascript
let winner = null

// Later in the program:
winner = "Alice"

console.log(winner)
```


Dette skriver ut:


```
Alice
```


Så `null` er nyttig når du for eksempel vil si: "Det skal være noe her senere, men akkurat nå er det tomt."


## Blokker og kontrollflyt

<chapterId>be985168-2636-5b0d-a48f-ac1bbfbff8a7</chapterId>


Så langt har vi for det meste skrevet kodelinjer som kjøres etter hverandre.


Men når vi koder, kan vi kontrollere rekkefølgen på utførelsen av den.


Dette kalles **kontrollflyt**.


La oss begynne med å forstå blokker og omfang.


### Det globale omfanget


Hver variabel vi deklarerer, finnes i et **omfang**, det vil si den delen av koden der variabelen er kjent.


Hvis du deklarerer en variabel utenfor en blokk, eksisterer den i **global scope**.


```javascript
const color = "blue"
console.log(color)
```


Variabelen `color` er i global scope, slik at den kan nås fra hvor som helst i filen.


Hvis du legger til flere linjer:


```javascript
const color = "blue"
console.log(color)

const size = "large"
console.log(color)
console.log(size)
```


Både `color` og `size` er globale variabler. De er tilgjengelige overalt i filen.


Men hva skjer inne i en blokk?


### Blokker og lokalt omfang


En **blokk** er et stykke kode omgitt av krøllete parenteser `{}`.


Variabler som er deklarert med `let` eller `const` inne i en blokk, eksisterer **kun** inne i denne blokken.


```javascript
{
const message = "inside block"
console.log(message)
}
```


Dette skriver ut:


```
inside block
```


Men hvis du prøver dette:


```javascript
{
const message = "inside block"
}
console.log(message) // Error!
```


JavaScript vil gi deg en feilmelding som:


```
ReferenceError: message is not defined
```


Det er fordi `message` ble deklarert inne i blokken og ikke eksisterer utenfor den.


Det betyr at vi kan bruke blokker til å isolere deler av koden vår, og være sikre på at "det som skjer i blokken, forblir i blokken" (litt som Las Vegas).


Ved å organisere koden vår i blokker kan vi også strukturere kjøringen av programmet, med kontrollflytkonstruksjoner som `if`


### `if`, `else`


Noen ganger ønsker vi å kjøre kode **kun hvis** noe er sant. Det er det `if`-setningen er til for.


```javascript
const myAge = 20

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Dette skriver ut:


```
Am I an adult?
Yes I am!
```


Som du kan se, sammenligner koden `myAge` og `18`.

I dette tilfellet returnerer `>=`-operatoren `true`, slik at blokken blir kjørt.

Hvis betingelsen ikke er `true`, blir ikke blokken kjørt.


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Dette skriver ut:


```
Am I an adult?
```


Du kan legge til en `else`-blokk for å håndtere det motsatte tilfellet:


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
} else {
console.log("No, I am not.")
}
```


Dette skriver ut:


```
Am I an adult?
No, I am not.
```


Både `if`- og `else`-blokkene er fortsatt blokker - så variabler som er deklarert inne i dem, eksisterer ikke utenfor.


Hvis vi vil være sikre på at noe **ikke** er sant, hva kan vi da gjøre?


Som vi har vært inne på tidligere, har JavaScript en "not"-operator, som snur boolske verdier. Så vi kan gjøre


```javascript
const myAge = 17

const adult = myAge >= 18

console.log("Am I an adult?")

if (!adult) {
console.log("No, I am not.")
}
```

Dette skrives fortsatt ut:


```
Am I an adult?
No, I am not.
```

Fordi vi brukte operatoren `!` til å invertere variabelen `adult`.


`if (!adult) {...}` skal leses som "if not adult..."


Ved hjelp av blokker, logikk og sammenligningsoperatorer kan vi strukturere kjøringen av programmet ved å definere variabler som må være `sanne` (eller `falske`) for at noe skal skje.


### `mens`, `pause`, `fortsette`


En `while`-løkke gjentar kode *så lenge* en betingelse er sann.


```javascript
let count = 0

while (count < 3) {
console.log("Count is", count)
count = count + 1
}
console.log("the loop is over!")
```


Dette skriver ut:


```
Count is 0
Count is 1
Count is 2
the loop is over!
```


Når `count` blir 3, stopper løkken.


Du kan stoppe en løkke tidlig ved hjelp av `break`:


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


Dette skriver ut:


```
0
1
2
```


For når tallet blir `3`, blir `if`-blokken utført, og løkken stoppes.


Du kan hoppe over resten av en løkke ved hjelp av `continue`:


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


Dette skriver ut:


```
1
2
4
5
```


For da tallet var `3`, fikk `continue` programmet til å hoppe over linjen som skriver ut tallet.


### "for ... av ..


Hvis du har en matrise og ønsker å gjøre noe med hvert element i den, kan du bruke `for ... of ... {...}`.


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const fruit of fruits) {
console.log(fruit)
}
```


Dette skriver ut:


```
apple
banana
cherry
```

Blokken kjøres én gang for hvert element i matrisen.


`fruit` er en ny variabel som tar verdien av hvert element i matrisen, for å operere på den inne i blokken.


### "for ... i ..


Du kan bruke `for ... in` til å løpe over nøklene (indeksene) i en matrise:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(index)
}
```


Dette skriver ut:


```
0
1
2
```


Du kan også bruke indeksen til å finne verdien:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(fruits[index])
}
```


Dette gir samme utskrift som `for ... of`:


```
apple
banana
cherry
```


I praksis bør du foretrekke å bruke `for ... of` for matriser, da det er enklere og renere.


### Avgrensede sløyfer


Noen ganger ønsker vi å loope et bestemt antall ganger, eller generelt skrive et stykke kode som gjentar en blokk mens den holder styr på noe.

Det er det en avgrenset `for`-løkke er god til.

En avgrenset løkke har vanligvis tre betingelser, atskilt med et semikolon `;`, som i `(... ; ... ; ....)`.


```javascript
for (let i = 0; i < 3; i = i + 1) {
console.log(i)
}
```


Dette skriver ut:


```
0
1
2
```


La oss forklare det:



- `let i = 0`: deklarerer en variabel som skal brukes i blokken (i dette tilfellet er det en teller som starter på 0)
- `i < 3`: erklærer en betingelse som skal være `sann` for at blokken skal utføres (i dette tilfellet er det "gjenta mens `i` er mindre enn 3")
- `i = i + 1`: deklarerer en kode som skal kjøres etter hver kjøring av blokken (i dette tilfellet "øk `i` med 1")


Som du kan se, kan den avgrensede sløyfen brukes til å angi mer komplekse betingelser for gjentatt kjøring av et stykke kode, men de fleste ganger er det ikke nødvendig.


### Blokketiketter


Hvis du må skrive en mer kompleks kontrollflyt, kan du i JavaScript navngi en blokk ved hjelp av en **label** som kan brukes av `break` eller `continue` for å angi *hvor* du skal hoppe tilbake.


Eksempel:


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


Dette skriver ut:


```
Inside outer block
Inside inner block
Done
```


Vi brukte `break outer` for å avslutte `outer`-blokken helt.


Du kan også merke løkker. La oss ta dette eksempelet:


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

Dette var et veldig kjedelig eksempel, men forhåpentligvis har det tydeliggjort behovet for etiketter (av og til).


## Introduksjon av funksjoner

<chapterId>cc324715-09c2-5cf7-9e6f-47a6f16bc04d</chapterId>


Etter hvert som programmene dine vokser, vil du ofte ønske å **gjenbruke** deler av koden.


Det er det **funksjoner** er til for: De lar deg gruppere noe kode, gi den et navn og kjøre den når du vil.


### Funksjonsdeklarasjon


For å deklarere en funksjon kan vi bruke nøkkelordet `function`. Da gir vi den et navn, et par parenteser `()` med argumentene den tar, og en kodeblokk `{}` som skal utføres. La oss starte med en funksjon som ikke tar noen argumenter:


```javascript
function sayHello () {console.log(`Hello!`) }
```


Denne koden **deklarerer** funksjonen, men kjører den **ikke** ennå.


### Funksjonsanrop


For å kjøre (eller "kalle") funksjonen skriver du navnet på den etterfulgt av parenteser:


```javascript
function sayHello () {console.log(`Hello!`) }
sayHello()
```


Dette skriver ut:


```
Hello!
```


Du kan kalle funksjonen så mange ganger du vil:


```javascript
function sayHello() {
console.log("Hello!")
}

sayHello()
sayHello()
```


Dette skriver ut:


```
Hello!
Hello!
```


Koden i funksjonen kjører bare når du kaller den.


### Funksjonsargumenter (input til funksjoner)


Noen ganger vil du at en funksjon skal fungere med noen inndata. Det kan du gjøre ved å legge til **argumenter** innenfor parentesen.


For eksempel:


```javascript
function sayHelloTo (friend) {
console.log(`Hello ${friend}!`)
}
```


Denne funksjonen tar **ett argument** kalt `friend`.


Når du kaller funksjonen, kan du sende en verdi:


```javascript
sayHelloTo("Tommy")
```


Dette skriver ut:


```
Hello Tommy!
```


Du kan kalle opp funksjonen igjen med et annet navn:


```javascript
sayHelloTo("Sam")
```


Dette skriver ut:


```
Hello Sam!
```


Verdien du sender inn, erstatter `friend`-variabelen i funksjonen.


Du kan også bruke mer enn ett argument:


```javascript
function greetTwoPeople(person1, person2) {
console.log(`Hello ${person1} and ${person2}!`)
}

greetTwoPeople("Lina", "Marco")
```


Dette skriver ut:


```
Hello Lina and Marco!
```


### `return` (utdata fra funksjoner)


Funksjoner kan også **returnere** verdier. Det betyr at de sender en verdi tilbake til det stedet der funksjonen ble kalt.


Her er et enkelt eksempel:


```javascript
function getNumber() {
return 42
}

const result = getNumber()
console.log(result)
```


Dette skriver ut:


```
42
```


Funksjonen `getNumber()` returnerer `42`, og vi lagrer det i `result`, og skriver det ut.


Du kan også returnere noe du beregner:


```javascript
function add(a, b) {
return a + b
}

const result = add(2, 3)
console.log(result)
```


Dette skriver ut:


```
5
```


Når en verdi er `return`, stopper funksjonen. Alt etter `return` i den blokken skjer ikke.


```javascript
function saySomething() {

return "hi"

console.log("this never runs")

}

const message = saySomething()
console.log(message)
```


Denne skriver bare ut:


```
hi
```


fordi bare `"hi"` blir returnert. Linjen `console.log("this never runs")` hoppes over.


Du kan tenke på funksjoner som små underprogrammer. Hver funksjon kan ta imot noe input, bearbeide det og gi deg noe output.


Hva skjer hvis vi prøver å bruke returverdien til en funksjon som ikke returnerte noe?


```javascript
function doesNothing () {}

const x = doesNothing()

console.log(x)
```

Dette vil skrive ut `undefined`. Returverdien til en funksjon som ikke returnerte noe, er `undefined`.


## Objekter og klasser

<chapterId>26689f25-8212-5057-8c21-3a05eee0ac75</chapterId>


JavaScript kalles ofte et objektorientert språk.


Det betyr at den hjelper deg med å organisere koden din ved å gruppere verdier og funksjoner i **objekter**.


### Hva er et `objekt`?


Et objekt kan inneholde data og funksjoner som opererer på disse dataene. Når en funksjon legges inn i et objekt, sier vi at det er en metode.


Det første objektet vi har sett var `console`-objektet. Det er et objekt som inneholder flere metoder for å skrive ut ting på skjermen og feilsøke programmene våre.


Den kan til og med skrive ut seg selv; du kan gjøre


```javascript
console.log(console)
```


og den vil skrive ut en liste over metodene den inneholder. På min maskin skrev den for eksempel ut


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


Som du ser, har den mange metoder som du kan bruke til feilsøking!


Javascript gir oss ulike måter å lage nye objekter på som kan gjøre det vi ønsker at de skal gjøre.


### Opprette et objekt


Den enkleste måten å opprette et objekt på er ved å gruppere data og funksjoner ved hjelp av **krøllete klammer** `{}`.


Dette skaper det vi kaller et **anonymt objekt**


```javascript
const cat = {
name: "Whiskers",
age: 3
}
```


Dette oppretter et objekt og lagrer det i en variabel kalt `cat`.


Objektet har to **egenskaper**:



- `navn` med verdien `"Whiskers"`
- `alder` med verdien `3`


La oss skrive det ut:


```javascript
console.log(cat)
```


Dette skriver ut:


```
{ name: 'Whiskers', age: 3 }
```


Du kan hente egenskapene ut av objektet ved hjelp av et punktum, som i `objektnavn.egenskapsnavn`:


```javascript
console.log(cat.name)  // prints "Whiskers"
console.log(cat.age)   // prints 3
```


Du kan også **endre** en eiendom:


```javascript
cat.age = 4
console.log(cat.age)  // now it prints 4
```


Som du ser, kan du fortsatt endre dataene i et objekt selv om det er definert som `const`.


Når det gjelder objekter, vil `const` bare hindre deg i å overstyre hele objektet:


```javascript
const cat = {
name: "Whiskers",
age: 3
}

cat.age = 5 // this works

cat = 5 // this throws an error, you're trying to reassign the whole object

```


Som nevnt tidligere kan objekter også inneholde **funksjoner**, og når en funksjon er en del av et objekt, kaller vi det en **metode**.


Her er et eksempel:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log("Meow!")
}
}
```


Dette objektet har:



- En `navn`-egenskap
- En `speak()`-metode


La oss kalle metoden:


```javascript
cat.speak()
```


Den skriver ut:


```
Meow!
```


Metoder kan bruke dataene objektet inneholder gjennom nøkkelordet `this`.

`this` refererer til det aktuelle objektet. I dette eksempelet vil det bli brukt til å skrive ut navnet på katten:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log(`${this.name} says meow!`)
}
}

cat.speak()
```


Dette skriver ut:


```
Whiskers says meow!
```


Ordet "dette" betyr "dette objektet" ... i dette tilfellet "katt"-objektet.



Denne typen objekter er ypperlige når du bare vil ha noe raskt og enkelt. Men hvis du trenger å lage **mange objekter** med samme struktur, finnes det en bedre måte å gjøre det på, og det er her **klasser** kommer inn i bildet.


### Klasser og konstruktører


En **klasse** er som en blåkopi. Den forteller JavaScript hvordan et bestemt objekt skal opprettes.


Du definerer en klasse ved hjelp av nøkkelordet `class`, etterfulgt av klassens navn og en blokk med krøllete klammer `{}`.


```javascript
class Dog {}
```


Klasser begynner vanligvis med en stor bokstav, i henhold til konvensjon.


Du kan opprette et nytt objekt av en klasse ved hjelp av `new`:


```javascript
const hachiko = new Dog()
```


Prøv å skrive ut objektet:

```javascript
class Dog {}

const myDog = new Dog()

console.log(myDog)
```


Du vil få


```
Dog {}
```


Som du ser, er Dog-klassen tom, og dermed er også `myDog`-objektet tomt.


Vi kan definere hvilke egenskaper Dog-objekter skal inneholde ved å legge til en `constructor`.


En konstruktør er en spesiell funksjon som kjøres når du oppretter (eller "konstruerer") et nytt objekt.


```javascript
class Dog {
constructor() { }
}
```


Vi vil at hver hund skal ha et navn, så vi legger til en `name`-parameter i funksjonen:


```javascript
class Dog {
constructor(name) { }
}
```


Og så bruker vi `this` til å erklære at `name` er `navnet` på `Dog`-objektet vi bygger


```javascript
class Dog {
constructor(name) {
this.name = name
}}
```


La oss prøve å bruke den nå:


```javascript
class Dog {
constructor(name) {
this.name = name
}
}

const myDog = new Dog("hachiko")

console.log(myDog)
```


Dette skriver ut noe sånt som:


```
Dog { name: 'hachiko' }
```


Som du kan se, tar `constructor`-metoden argumentene du sender til klassen når du gjør `new Dog()`, og bruker dem til å bygge objektet.


La oss dele det opp:



- `class Dog` definerer klassen Dog.
- `constructor(name)` konfigurerer objektet når det opprettes.
- `this.name = name` lagrer verdien i det nye objektet.
- `new Dog("hachiko")` oppretter et nytt objekt fra klassen, med egenskapen `name` satt til `"hachiko"`.


La oss nå legge til en metode i klassen vår:


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


Dette vil skrive ut


```javascript
hachiko says barf!
```


Hvis vi gjør det samme for to forskjellige instanser av Dog



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


vi får


```
hachiko says barf!
bobby says barf!
```


metoden `speak()` bruker egenskapen `name` til `Dog` som den kalles på.


Dette er hovedgrunnen til at klasser finnes: De gjør det mulig å definere et sett med metoder som opererer på data, og deretter opprette flere objekter som deler den samme "formen" på dataene.


Når vi kaller en metode på et av disse objektene, vil den operere på dataene som *det spesifikke objektet* inneholder.


### Endre formen på et objekt


Objekter i JavaScript er fleksible. Selv etter at du har opprettet et objekt, kan du fortsatt legge til nye egenskaper eller fjerne eksisterende.


Det er lov, men det er noe du bør bruke med forsiktighet.


La oss begynne med vår enkle `Dog`-klasse:


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


På dette tidspunktet har `myDog` bare én egenskap: `name`. Vi kan fortsatt legge til nye egenskaper etter at den er opprettet:


```javascript
myDog.age = 5

console.log(myDog.age) // prints 5
```


Vi kan også legge til en ny metode:


```javascript
myDog.jump = function () {
console.log(`${this.name} jumps!`)
}

myDog.jump() // Fido jumps!
```


Og vi kan også fjerne egenskaper ved hjelp av nøkkelordet `delete`.


```javascript
delete myDog.name

console.log(myDog.name) // prints 'undefined'
```


Dette fungerer, men her er noe som er viktig å vite: JavaScript-motorer som V8 (som brukes i Node.js og i Chrome-nettleseren) kjører raskere når objektene dine alltid har de samme egenskapene. Hvis du legger til eller fjerner egenskaper etter at objektet er opprettet, kan det gjøre ting tregere.


I små programmer spiller dette ikke så stor rolle. Men i større prosjekter (som spill) er det bedre å liste opp alle egenskapene i konstruktøren fra starten av, selv om du ikke bruker dem med en gang. Dette holder objektets form stabil og gjør at koden kjører raskere.


For eksempel i stedet for dette:


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


Du kan gjøre


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


Begge versjonene fungerer, men den andre er bedre med tanke på ytelse. Du forteller motoren på forhånd hvilke egenskaper hvert objekt skal ha, og den kan optimalisere deretter.


I JavaScript kan du omforme objekter fritt, men når du bruker klasser, er det best å planlegge objektets form på forhånd.



### Arv med `extends` og `super()`


Noen ganger ønsker man å lage en klasse som er *nesten* lik en annen klasse, men med noen ekstra funksjoner.


I stedet for å endre formen på objektene (noe som som nevnt ikke er optimalt for ytelsen), eller å måtte skrive om en ny klasse fra bunnen av, kan du i JavaScript bruke noe som kalles **arv**.


Arv betyr at en klasse kan **utvide** en annen. Den nye klassen får alle egenskapene og metodene til den gamle, og du kan legge til flere eller endre det du trenger.


La oss si at vi har en basisklasse som heter `Vehicle`:


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


Nå ønsker vi å lage en bilklasse. En bil er et slags kjøretøy, men vi vil kanskje at den skal ha noen ekstra funksjoner eller en annen melding når den starter. I stedet for å skrive om alt, kan vi bruke `extends`:


```javascript
class Car extends Vehicle {
start() {
console.log(`${this.brand} car is ready to drive!`)
}
}
```


Klassen `Car` **arver** nå alt fra `Vehicle`. Den får egenskapen `brand`, og vi har erstattet `start()`-metoden med vår egen versjon.


![](assets/en/4.webp)


La oss prøve det ut:


```javascript
const myCar = new Car("Toyota")
myCar.start()
```


Dette skriver ut:


```
Toyota car is ready to drive!
```


Selv om `Car` ikke har sin egen konstruktør, bruker den fortsatt den fra `Vehicle`. Men hvis vi ønsker å skrive en egendefinert konstruktør i `Car`, kan vi gjøre det, vi trenger bare å inkludere et kall til konstruktøren til dens forelder ved hjelp av `super()`.


Slik gjør du det:


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



Dette skriver ut:


```
Toyota Corolla is ready to drive!
```


Så for å oppsummere



- `utvider` betyr at en klasse er basert på en annen.
- `super()` brukes til å kalle konstruktøren til klassen du utvider.
- Den nye klassen får alle egenskapene og metodene til den opprinnelige klassen.
- Du kan **overstyre** metoder (som `start()`) for å få dem til å gjøre noe annet.


Dette er nyttig når du har flere ting som ligner på hverandre (som biler, lastebiler og sykler), og du vil at de skal dele kode, men likevel oppføre seg på sin egen måte.


### `instanceof`


Nøkkelordet `instanceof` sjekker om et objekt er opprettet fra en bestemt klasse.


La oss si at vi har en klasse som heter `User`:


```javascript
class User {
constructor(username) {
this.username = username
}
}

const regularUser = new User("julia123")

console.log(regularUser instanceof User)
```


Dette skriver ut:


```
true
```


Bekrefter at `regularUser` er en `User`. Det er fordi `regularUser` ble opprettet ved hjelp av `User`-klassen.


Det fungerer også med **arvede** klasser. Her er for eksempel en `Admin`-klasse som utvider `User`:


```javascript
class Admin extends User {}

const ourAdmin = new Admin("admin42")

console.log(ourAdmin instanceof Admin)   // true
console.log(ourAdmin instanceof User)    // true
```


Begge linjene returnerer `true`. Det er fordi `Admin` er en underklasse av `User`, og derfor er `ourAdmin` både en `Admin` og en `User`


# JavaScript på mellomnivå

<partId>243f63ab-4f34-5c30-80cb-84ef46f6761d</partId>


## Feilhåndtering

<chapterId>d0206bc5-d386-5e7f-9917-5803f392448c</chapterId>


Etter hvert som du skriver mer komplekse JavaScript-programmer, vil du støte på **feil**. Dette er uventede situasjoner der noe går galt. Kanskje en variabel er "udefinert", men du prøver å bruke den, eller en kode mottar feil type input.


Hvis vi ikke håndterer disse feilene på riktig måte, kan programmet vårt krasje eller oppføre seg på uforutsigbare måter. JavaScript har verktøy for å oppdage og håndtere disse feilene, slik at vi kan håndtere dem på en mer elegant måte.


### Vanlig feil: tilgang til en verdi på `undefined`


Her er en vanlig situasjon som forårsaker en feil:


```javascript
const user = undefined
console.log(user.name)
```


Hvis du kjører denne koden, vil du få en feilmelding som ser slik ut:


```
TypeError: Cannot read properties of undefined (reading 'name')
```


Det er JavaScript som forteller deg det: "Hei, du prøvde å hente egenskapen `name` fra noe som er `undefined`, og det gir ikke mening." Og som du kan se, når denne typen feil oppstår, slutter programmet å kjøre, med mindre du har skrevet spesifikk kode for å fange opp og håndtere den.


### `kaster` en feil


Noen ganger ønsker du å **opprette en feil** manuelt i koden din. I så fall bruker du nøkkelordet `throw`.


```javascript
throw new Error("This is a custom error message")
```


Dette stopper programmet umiddelbart og skriver ut:


```
Uncaught Error: This is a custom error message
```


Du kan bruke `throw` til å håndheve regler i programmet ditt. For eksempel


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


Det andre anropet fører til en feil fordi det ikke er tillatt å dividere med null i dette eksempelet.


### Fange opp feil med `try...catch`


Hvis du ikke vil at programmet skal krasje når det oppstår en feil, kan du fange opp feilen ved hjelp av en `try...catch`-blokk. Dette er nyttig når du vil at programmet skal **fortsette** selv om noe mislykkes.


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log("Oops! Something went wrong.")
}
```


Produksjon:


```
Oops! Something went wrong.
```


Slik fungerer det:



- Koden inne i `try`-blokken blir forsøkt først.
- Hvis det oppstår en feil, hopper JavaScript **til `catch`-blokken**, og hopper over resten av `try`-blokken.
- `catch`-blokken mottar feilen, slik at du kan skrive den ut, eller håndtere den på en annen måte, som for eksempel


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log(`The message of the error was: "${error.message}"`)
}
```


Produksjon:


```
The message of the error was: "Cannot read properties of undefined (reading 'name')"
```


### Blokken "endelig


Du kan også legge til en `finally`-blokk. Dette er kode som **alltid kjøres**, uansett om det oppstod en feil eller ikke.


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


Produksjon:


```
Trying something risky...
Caught the error: Uh oh!
This will run no matter what.
```


## Unngå feil

<chapterId>db12d9f6-5806-514c-998e-0ae24805104e</chapterId>


Dette kapittelet viser noen av de vanligste fallgruvene i JavaScript, og hvordan du kan unngå dem.


### `var` og Assignment uten deklarasjon


I eldre JavaScript-kode ble variabler ofte deklarert ved hjelp av nøkkelordet `var`. I motsetning til `let` og `const`, som du allerede har lært om, kan `var` oppføre seg på forvirrende måter.


For eksempel:


```javascript
{
var message = "hello"
}
console.log(message)
```


Man skulle kanskje tro at `message` bare eksisterer inne i blokken, men det gjør den ikke. `var` ignorerer blokkens omfang og gjør variabelen tilgjengelig i hele funksjonen eller filen.


Dette kan føre til uventet oppførsel, spesielt i større programmer. Derfor bør moderne JavaScript-kode alltid bruke `let` eller `const` i stedet for `var`.


Enda verre er det at JavaScript lar deg tilordne verdier til variabler **uten å deklarere dem i det hele tatt**:


```javascript
function greet() {
user = "Alice"
}
greet()
console.log(user) // prints "Alice"
```


Dette oppretter en ny global variabel `name` uten noen deklarasjon. Dette kan skje i det stille og føre til feil som er vanskelige å spore opp, spesielt hvis det bare var en skrivefeil. Deklarer alltid variabler ved hjelp av `let` eller `const`.


### Svakt typesystem


JavaScript er svakt typet, noe som betyr at det automatisk konverterer verdier fra én type til en annen ved behov. Dette kalles type coercion, og selv om det kan være praktisk, fører det ofte til forvirrende resultater.


For eksempel:


```javascript
console.log("5" + 1)    // "51"
console.log("5" - 1)    // 4
console.log(true + 1)   // 2
console.log(null + 1)   // 1
```


I disse eksemplene prøver JavaScript å gjette hva du mente. Noen ganger gjør den om strenger til tall, boolske bokstaver til tall eller strenger til strenger. Dette kan få koden din til å oppføre seg på uventede måter.


Det er viktig å være klar over det svake typingssystemet i JavaScript. Når ting begynner å oppføre seg merkelig, kan det skyldes uventet typetvang.


### `"use strict"``


Du kan aktivere en strengere modus som gjør noen stille feil til ekte feil, og som hindrer deg i å bruke noen av de farligste funksjonene i språket.


For å aktivere denne strengere modusen legger du til denne linjen øverst i filen eller funksjonen:


```javascript
"use strict"
```


For eksempel:


```javascript
"use strict"
name = "Alice" // ReferenceError: name is not defined
```


Uten strict mode ville JavaScript stille opprette en global variabel kalt `name`. Men med strict mode blir dette en reell feil, noe som hjelper deg med å oppdage feil tidligere.


Strict-modus deaktiverer også noen utdaterte funksjoner i JavaScript, og gjør koden enklere å optimalisere og vedlikeholde.


## Verdi vs. referanse

<chapterId>bb898425-dc2f-5e5c-864b-0cb7a4a9aea9</chapterId>


JavaScript behandler ulike typer verdier på ulike måter.


Noen verdier **kopieres** når du tilordner dem til en variabel.


Andre er **delt** når du tilordner dem til en ny variabel, så hvis du endrer den ene, endres også den andre.


### Pass etter verdi


Når en verdi sendes **by value**, lager JavaScript en **kopi** av den.


Så hvis du endrer den ene, påvirker det ikke den andre.


Dette skjer med primitive typer, som f.eks:



- tall
- strenger
- boolske verdier (`sann` og `falsk`)
- `null`
- `undefinert`


La oss se på et eksempel:


```javascript
let a = 5
let b = a

b = 10

console.log(a) // 5
console.log(b) // 10
```


Vi ga `b` verdien av `a`, men så endret vi `b` til `10`.


Siden tall overføres etter verdi, kopierte JavaScript `5` inn i `b`. `5` i `b` er uavhengig av den opprinnelige `5` i `a`, så endring av verdien i `b` hadde ingen effekt på `a`.


La oss prøve med en streng:


```javascript
let name1 = "Alice"
let name2 = name1

name2 = "Bob"

console.log(name1) // Alice
console.log(name2) // Bob
```


Igjen, endring av `name2` påvirket ikke `name1`, fordi strenger også sendes med verdi.


Det samme skjer når du sender en primitiv til en funksjon: Den blir kopiert. Funksjonen kan altså ikke endre originalen.


```javascript
function plusOne(x) {
x = x + 1
}

let number = 5

plusOne(number)

console.log(number) // 5
```


Selv om `1` ble lagt til `x` inne i funksjonen, ble ikke det opprinnelige `tallet` endret.


Det er fordi bare en **kopi** ble sendt inn i funksjonen.


### Pass by referanse


Objekter sendes **ved referanse**.


Det betyr at i stedet for å kopiere dem, sender JavaScript bare en **referanse** til den, og hvis du endrer den, vil alle andre variabler som peker til den, også se endringen.


For eksempel:


```javascript
const person1 = { name: "Alice" }
const person2 = person1

person2.name = "Bob"

console.log(person1.name) // Bob
console.log(person2.name) // Bob
```


Både `person1` og `person2` peker til det samme objektet i minnet.


Så da vi endret `person2.name`, endret vi også `person1.name`, fordi de begge ser på det samme.


Matriser er objekter, så la oss prøve det samme med en matrise:


```javascript
const list1 = [1, 2, 3]
const list2 = list1

list2.push(4)

console.log(list1) // [1, 2, 3, 4]
console.log(list2) // [1, 2, 3, 4]
```


Vi skjøv `4` inn i `list2`, men `list1` ble også påvirket, fordi de begge refererer til den samme matrisen.


La oss se hva som skjer når vi sender et objekt til en funksjon:


```javascript
function rename(user) {
user.name = "Charlie"
}

const person = { name: "Dana" }

rename(person)

console.log(person.name) // Charlie
```


Funksjonen endret objektet! Det er fordi den mottok en **referanse** til det opprinnelige `person`-objektet.


Den fikk ikke en kopi. Den fikk tilgang til det opprinnelige objektet, og med det fikk den muligheten til å endre det.


Det er viktig å huske dette skillet, for ellers kan koden vår oppføre seg annerledes enn vi forventer. Vi kan for eksempel skrive en funksjon med en forventning om at den ikke skal endre argumentene den mottar, og senere finne ut at den faktisk endret dem (fordi de var objekter, så de ble sendt med referanse).


## Arbeide med funksjoner

<chapterId>e0d277a8-c642-5af7-9e53-dee27c811967</chapterId>


Du har allerede lært hvordan du deklarerer og bruker funksjoner i JavaScript. Men JavaScript gir deg flere verktøy for å jobbe med funksjoner på kraftfulle måter.


### Pilfunksjoner


Pilfunksjoner er en kortere måte å skrive funksjoner på. I stedet for å bruke nøkkelordet `function` bruker vi en pil (`=>`).


Her er en normal funksjon:


```javascript
function greet(name) {
return `Hello, ${name}!`
}
```


Pilversjonen ser slik ut:


```javascript
const greet = (name) => {
return `Hello, ${name}!`
}
```


Hvis funksjonen har **kun én linje**, kan du hoppe over parentesene og `return`:


```javascript
const greet = (name) => `Hello, ${name}!`
```


Hvis funksjonen har **kun én parameter**, kan du til og med hoppe over parentesene rundt parameterne:


```javascript
const greet = name => `Hello, ${name}!`
```


Pilfunksjoner er svært vanlige i moderne JavaScript, ettersom de gjør det mulig å uttrykke enkle funksjoner med betydelig mindre boilerplate.


### Standardparametere


Noen ganger ønsker man at en funksjon skal ha en **standardverdi** hvis det ikke sendes inn noe argument.


Du kan gjøre det slik:


```javascript
function sayHello(name = "friend") {
console.log(`Hello, ${name}!`)
}

sayHello("Alice") // Hello, Alice!
sayHello()        // Hello, friend!
```


Standardverdien `"friend"` brukes når ingenting er sendt inn.


### Spredningsparametere (`...`)


Hva om funksjonen din tar et fleksibelt antall argumenter?


Du kan bruke **spread-operatoren** (`...`) for å samle dem i en matrise:


```javascript
function logAll(...items) {
console.log(items)
}

logAll(1, 2, 3) // [1, 2, 3]
logAll("a", "b") // ["a", "b"]
```


Deretter kan du bruke en løkke til å behandle hvert element:


```javascript
function logEach(...items) {
for (const item of items) {
console.log(item)
}
}
```


Spread-operatoren er nyttig når du ikke vet hvor mange argumenter som skal sendes.


### Funksjoner av høyere orden


En **høyere ordens funksjon** er en funksjon som:



- tar en annen funksjon som input
- og/eller returnerer en funksjon som utdata


Her er et enkelt eksempel:


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


Dette skriver ut:


```
Hello, friend!
Hello, friend!
```


Vi kan sende en pilfunksjon til den:


```javascript
runTwice(
() => console.log("Hello!")
)
```


Dette skriver ut:


```
Hello!
Hello!
```


Du kan også skrive funksjoner som **returnerer** andre funksjoner:


```javascript
function makeGreeter(name) {
return () => console.log(`Hi, ${name}`)
}

const greetAlice = makeGreeter("Alice")
const greetBob = makeGreeter("Bob")

greetAlice() // Hi, Alice
greetBob() // Hi, Bob
```


Funksjonen `makeGreeter` er en funksjon som bygger andre funksjoner. Den mottar en streng og returnerer en ny funksjon som bruker denne strengen i `console.log`-kallet.


Denne typen mønster er svært effektivt, ettersom det gir deg mulighet til å legge igjen "hull" i funksjonene dine som du senere kan fylle med den atferden du trenger.


### `map()`, `filter()`, `reduce()`


JavaScript har noen nyttige innebygde metoder som du kan bruke med matriser.


Disse metodene tar funksjoner som argumenter, så de er også høyere ordens funksjoner.


`map()` forvandler hvert element i en matrise til noe annet.


Eksempel:


```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map(x => x * 2)

console.log(doubled) // [2, 4, 6]
```


Hvert tall dobles, og resultatet er en ny matrise.


`filter()` fjerner elementer fra matrisen hvis de ikke består en test.


Eksempel:


```javascript
const numbers = [1, 2, 3, 4, 5]
const numbersGreaterThanTwo = numbers.filter(x => x > 2)

console.log(numbersGreaterThanTwo) // [3, 4, 5]
```


Bare de matriseoppføringene der betingelsen `x > 2` returnerer `true`, beholdes.


`reduce()` brukes til å kombinere alle elementene i en matrise til én enkelt verdi.


Eksempel:


```javascript
const numbers = [1, 2, 3, 4]
const total = numbers.reduce((current, next) => current + next)

console.log(total) // 10
```


`reduce` går gjennom matrisen og, i dette eksemplet, bruker `+`-operatoren mellom `1` og `2`, deretter mellom det resulterende `3` og `3`, deretter mellom det resulterende `6` og `4`, helt til den har summen av alle oppføringene i matrisen (som er 10).


Du kan bruke `reduce()` til mange ting, for eksempel totalsummer, gjennomsnitt eller å bygge nye verdier trinnvis.


Disse metodene (`map`, `filter`, `reduce`) er kraftige verktøy for å behandle data uten å skrive manuelle løkker.


Du kan til og med kombinere dem i en kjede av operasjoner, slik som dette:


```javascript
const numbers = [1, 2, 3, 4, 5]

const result = numbers
.map(n => n * 2)        // Double each entry, obtain [2, 4, 6, 8, 10]
.filter(n => n > 3) // Keep only the entries bigger than 3, so you get [4, 6, 8, 10]
.reduce((n1, n2) => n1 + n2) // Adds them: 4 + 6 + 8 + 10 = 28

console.log(result) // 28
```


## Arbeide med objekter

<chapterId>7842aada-f009-5518-b8e3-1104e166a035</chapterId>


I dette kapittelet skal vi lære oss noen kraftige og litt mer avanserte verktøy for å jobbe med objekter i JavaScript.


### Private eiendommer


Noen ganger ønsker vi å skjule en egenskap i et objekt, slik at den ikke kan endres eller nås fra utsiden av objektet. JavaScript gir oss en måte å gjøre dette på ved å bruke `#` foran egenskapsnavnet. Dette skaper en **privat** egenskap, som bare er tilgjengelig fra innsiden av klassen.


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


Private egenskaper er nyttige når du vil forhindre utilsiktede endringer.


### `statiske` egenskaper


Noen ganger vil du at en egenskap skal tilhøre selve klassen, ikke hvert objekt du oppretter fra klassen. Det er det `static` er til for. En `static`-egenskap ligger i klassen, og alle objektene i klassen vil referere til den.


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


Dette er nyttig for lagring av delte data og metoder som gjelder for hele gruppen av objekter, ikke bare ett.


### `get` og `set`


I JavaScript kan du med `get` og `set` lage egenskaper som *ser* ut som vanlige variabler, men som i virkeligheten kjører spesialkode i bakgrunnen.


En `get`ter-metode kjøres når du prøver å *lese* en egenskap. Den deklareres ved å skrive `get` foran en metode med navnet på egenskapen.


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


Selv om `fullName` ikke er en vanlig egenskap, kan vi bruke den som en, og bak kulissene kjører den `get`-funksjonen for å lage det fullstendige navnet.


En `set`ter-metode kjøres når du *tildeler* en verdi til en egenskap. Den lar deg kontrollere hva som skjer når noen prøver å endre denne verdien. Den deklareres ved å skrive `set` foran en metode med navnet på egenskapen.


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


Når vi gjør `user.fullName = "John Smith"`, kjører den `set`-metoden og oppdaterer verdiene `firstName` og `lastName`.


Så selv om det føles som om vi bare setter en enkel variabel, utløser vi faktisk logikk som oppdaterer andre egenskaper.


## Nøkler og verdier

<chapterId>01a397b8-c12a-5c39-82b3-6d9ebbb72a29</chapterId>


Hver egenskap i et JavaScript-objekt har en **nøkkel** (også kalt et egenskapsnavn) og en **verdi**.


For eksempel:


```javascript
const user = {
name: "Alice",
age: 30
}
```


I dette objektet er `"name"` og `"age"` nøklene, og "Alice" og `30` er verdiene deres.


### Dynamisk tilgang


Noen ganger vet du ikke navnet på en egenskap på forhånd ... kanskje du får det fra brukerinndata eller leser det fra en variabel. Du kan likevel få tilgang til den ved hjelp av **parentesnotasjon**, som `myObject["keyName"]`.


```javascript
const user = {
name: "Alice",
age: 30
}

console.log(user["name"]) // Alice
```


Vi sendte strengen `name` til objektet for å få den tilsvarende verdien.


Vi kan lagre en nøkkel i en variabel og bruke den til å få tilgang til den tilsvarende verdien senere, for eksempel


```javascript
const user = {
name: "Alice",
age: 30
}

const key = "name"

console.log(user[key]) // Alice
```


### Dynamisk Assignment


Du kan også opprette eller oppdatere objektegenskaper ved hjelp av variabler som nøkler.


```javascript
const settings = {}

const key = "theme"
settings[key] = "dark"

console.log(settings) // { theme: "dark" }
```


Dette er nyttig når du vil bygge et objekt trinn for trinn. For eksempel:


```javascript
const user = {}

user["username"] = "bananaFan123"
user["email"] = "banana@fruit.com"

console.log(user)
// { username: "bananaFan123", email: "banana@fruit.com" }
```


Du kan til og med bruke en dynamisk nøkkel *mens du oppretter* objektet ved hjelp av hakeparenteser:


```javascript
const key = "language"
const config = {
[key]: "JavaScript"
}

console.log(config.language) // JavaScript
```


Dette kalles en **beregnet egenskap**. Verdien innenfor parentesen evalueres, og resultatet brukes som nøkkel.


### `Symbol` Type


I tillegg til strenger kan du i JavaScript også bruke en spesiell type kalt `Symbol` som objektnøkkel.


La oss begynne med et enkelt eksempel:


```javascript
const id = Symbol("userID")

const user = {
name: "Bob",
[id]: 12345
}

console.log(user[id]) // 12345
```


I dette eksempelet er `id` et symbol. Det er ikke en streng, men det fungerer likevel som en nøkkel. Hvis du prøver å logge `user` på konsollen, vil du se dette:


```javascript
console.log(user) // { name: 'Bob', [Symbol(userID)]: 12345 }
```


En annen viktig ting: Hvert symbol du oppretter, er unikt, selv om de er opprettet med samme streng.


```javascript
const a = Symbol("label")
const b = Symbol("label")

console.log(a === b) // false
```


Med symboler kan du definere nøkler som ikke kolliderer med vanlige nøkler. La oss for eksempel si at du har et objekt med egenskapen `name`, men at objektet vil kunne tilpasses av en bruker i fremtiden, på måter du ikke kan forutse, og at brukeren kanskje legger til en `name`-egenskap i tillegg. Hvis den opprinnelige egenskapen `name` var definert med en streng, ville den bli overskrevet av den nye egenskapen, slik som dette:


```javascript
const obj = {
name: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy' }
```


Hvis vi bruker et symbol i stedet:


```javascript
const name = Symbol("name")

const obj = {
[name]: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy', [Symbol(name)]: 'John' }
```


Som du kan se, bevares den opprinnelige egenskapen `name` på en eller annen måte på denne måten. Dette kan være nyttig i visse tilfeller.


## Utility-objekter

<chapterId>516e74c8-2a11-545a-a4d1-c2cabb91a273</chapterId>


JavaScript gir oss noen nyttige innebygde objekter som hjelper oss med ting som feilsøking og matematiske operasjoner.


### Andre `konsoll`-metoder


Du har allerede sett `console.log`, som skriver ut verdier på skjermen.


Det finnes noen andre nyttige metoder i `console`-objektet som kan hjelpe deg med å feilsøke programmene dine.


#### `console.warn`


Skriver ut en melding i gult (eller med et advarselsikon i enkelte miljøer):


```javascript
console.warn("This is just a warning.")
```


#### `console.error`


Skriver ut en melding i rødt, som en feilmelding:


```javascript
console.error("Something went wrong!")
```


#### `console.table`


Viser en matrise eller et objekt som en tabell:


```javascript
const users = [
{ name: "Alice", age: 25 },
{ name: "Bob", age: 30 }
]

console.table(users)
```


Dette skriver ut en tabell som:


```
┌─────────┬────────┬─────┐
│ (index) │  name  │ age │
├─────────┼────────┼─────┤
│    0    │ 'Alice'│  25 │
│    1    │ 'Bob'  │  30 │
└─────────┴────────┴─────┘
```


Dette kan være nyttig for å visualisere strukturerte data.


#### `console.time` og `console.timeEnd`


Du kan måle hvor lang tid noe tar:


```javascript
console.time("timer")
for (let i = 0; i < 1000000; i++) {}
console.timeEnd("timer")
```


Dette skriver ut noe sånt som:


```
timer: 2.379ms
```


Nyttig for noen enkle ytelsestester.


### `Math`-objektet


JavaScript gir deg et `Math`-objekt med nyttige metoder for å utføre beregninger.


#### `Math.random()`


Returnerer et tilfeldig tall mellom 0 (inklusive) og 1 (eksklusive):


```javascript
const r = Math.random()
console.log(r)
```


Eksempel på utdata:


```
0.4387429859
```


#### `Math.floor()` og `Math.ceil()`



- `Math.floor(n)` avrunder **ned** til nærmeste heltall
- `Math.ceil(n)` runder **opp** til nærmeste heltall


```javascript
console.log(Math.floor(4.9)) // 4
console.log(Math.ceil(4.1))  // 5
```


#### `Math.round()`


Avrunder til nærmeste heltall:


```javascript
console.log(Math.round(4.4)) // 4
console.log(Math.round(4.6)) // 5
```


#### `Math.max()` og `Math.min()`


Returnerer den største eller minste verdien fra en liste med tall:


```javascript
console.log(Math.max(5, 9, 3)) // 9
console.log(Math.min(5, 9, 3)) // 3
```


#### `Math.pow()` og `Math.sqrt()`



- `Math.pow(a, b)` gir deg `a` i potens av `b`
- `Math.sqrt(n)` gir deg kvadratroten av `n`


```javascript
console.log(Math.pow(2, 3))   // 8
console.log(Math.sqrt(16))    // 4
```


# Avansert JavaScript

<partId>72c30671-ca20-5617-92a5-d5ba7aa38c93</partId>


## Andre samlinger

<chapterId>a9a70c6d-a343-5a46-a383-e288bc2700e3</chapterId>


JavaScript gir oss noen spesielle samlingstyper som går utover vanlige matriser og objekter. Disse inkluderer `Map` og `Set`.


De hjelper deg med å lagre og administrere grupper av verdier, men de fungerer på en annen måte enn det du har sett så langt.


En `Map` er en samling av **nøkkel-verdi-par**, akkurat som et objekt. Men den har noen viktige forskjeller:



- Nøklene kan være **en hvilken som helst verdi**, ikke bare strenger.
- Rekkefølgen på elementene bevares.
- Den har innebygde metoder som gjør det enklere å jobbe med den.


Du oppretter et nytt kart slik:


```javascript
const myMap = new Map()
```


Dette oppretter et tomt kart. For å legge til oppføringer i kartet bruker du `myMap.set(key, value)`:


```javascript
myMap.set("name", "Alice")
```


Dette legger til en nøkkel `"name"` med verdien `"Alice"`.


Du kan også bruke et tall som nøkkel:


```javascript
myMap.set(42, "The answer")
```


Og til og med et objekt som nøkkel:


```javascript
const objKey = { id: 1 }
myMap.set(objKey, "Object as key")
```


Det ville ikke fungert med vanlige objekter, som bare tillater strengnøkler.


For å **hente en verdi** bruker du `myMap.get(key)`:


```javascript
console.log(myMap.get("name"))     // Alice
console.log(myMap.get(42))         // The answer
console.log(myMap.get(objKey))     // Object as key
```


For å **sjekke om en nøkkel finnes**, bruker du `myMap.has(key)`:


```javascript
console.log(myMap.has("name")) // true
```


For å **fjerne en nøkkel** bruker du `myMap.delete(key)`:


```javascript
myMap.delete("name")
```


For å **tømme hele kartet** bruker du `myMap.clear()`:


```javascript
myMap.clear()
```


Kart er ypperlige til å håndtere store verdisamlinger, fordi tilgang til verdier på et stort kart vanligvis gir mye bedre ytelse enn på et stort objekt.


### `Set`


Et `Set` er en samling av kun **verdier** (ingen nøkler), der hver verdi må være **unik**. Det betyr at



- Du kan ikke ha samme verdi to ganger
- Verdiene lagres i den rekkefølgen du legger dem til


Du oppretter et sett som dette:


```javascript
const mySet = new Set()
```


For å **legge til verdier** bruker du `mySet.add(value)`:


```javascript
mySet.add(1)
mySet.add(2)
mySet.add(2) // duplicate, will be ignored
```


Selv om vi prøvde å legge til `2` to ganger, vil settet bare beholde én kopi.


For å **sjekke om en verdi finnes i settet**, bruker du `mySet.has(value)`:


```javascript
console.log(mySet.has(2)) // true
console.log(mySet.has(3)) // false
```


For å **fjerne en verdi** bruker du `mySet.delete(value)`:


```javascript
mySet.delete(2)
```


For å **tømme alt** bruker du `mySet.clear()`:


```javascript
mySet.clear()
```


Et `Set` er nyttig når du ønsker å oppbevare en samling unike verdier uten å måtte sjekke manuelt om det finnes duplikater:


```javascript
const numberArray = [1, 2, 2, 3, 4, 4, 4, 5]

const numberSet = new Set(numberArray)

console.log(numberSet) // Set(5) { 1, 2, 3, 4, 5 }
```


Med `Set` unngår du duplikater for deg.


## Iteratorer

<chapterId>61d24e5e-b7e4-541a-8322-778f61f26a72</chapterId>


De fleste ting i JavaScript som du kan loope over (som matriser, strenger, kart, sett), er **iterable**: De kan tilby iteratorer for innholdet.


En **iterator** er et spesielt objekt i JavaScript som hjelper deg med å gå gjennom en liste med elementer **ett om gangen**.


### `Objekt`-iteratorer


I motsetning til matriser eller kart, kan vanlige objekter **ikke itereres** med `for...of`. Hvis du prøver dette:


```javascript
const user = {
name: "Alice",
age: 30
}

for (const value of user) {
console.log(value)
}
```


Du vil få en feilmelding:


```
TypeError: user is not iterable
```


Det er fordi vanlige objekter ikke har en innebygd iterator. Men JavaScript gir deg andre verktøy for å loope over dem.


#### `Object.keys()`


Du kan bruke `Object.keys(obj)` til å hente en matrise med objektets **nøkler**, og deretter loope over den:


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


Dette skriver ut:


```
name
age
```


#### `Objekt.verdier()`


For å gå i en løkke over **verdiene** bruker du `Object.values()`:


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


Dette skriver ut:


```
Alice
30
```


#### `Object.entries()`


Hvis du vil ha **både nøkkelen og verdien**, bruker du `Object.entries()`:


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


Dette skriver ut:


```
name is Alice
age is 30
```


Selv om objekter ikke er iterable direkte, gir disse metodene deg full tilgang til innholdet på en måte som fungerer godt med `for...of`.


Men hvordan fungerer iteratorer?


### `Symbol.iterator`


Hemmeligheten bak alle iterabler er et spesielt **symbol** som heter `Symbol.iterator`.


Dette symbolet er en innebygd nøkkel som forteller JavaScript: "Dette objektet kan itereres."


Når du kaller `myIterable[Symbol.iterator]()`, gir JavaScript deg tilbake et **iterator-objekt** med en `.next()`-metode.


La oss se hvordan det ser ut:


```javascript
const colors = ["red", "green", "blue"]

const iterator = colors[Symbol.iterator]()

console.log(iterator.next()) // { value: 'red', done: false }
```


Hvert anrop til `.next()` gir deg den neste verdien. Når den er ferdig, returnerer den:


```javascript
{ value: undefined, done: true }
```


### `next()`


Metoden `.next()` brukes til å hente neste element fra sekvensen.


Hver gang du kaller `.next()`, får du et objekt med to nøkler:



- `verdi`: det aktuelle elementet
- `done`: en boolsk verdi som forteller deg om iterasjonen er over


La oss ta et fullstendig eksempel:


```javascript
const names = ["Lina", "Tom", "Eva"]      // declare an array
const iterator = names[Symbol.iterator]() // use the Symbol.iterator function to get an iterator for this array

let result = iterator.next()              // get the first element of the array

while (!result.done) {                    // repeat this loop until you reach the last element of the array, which is marked with { done: true }
console.log(result.value)               // print the value of each element
result = iterator.next()                // get the next element of the array
}
```


Dette skriver ut:


```
Lina
Tom
Eva
```


Slik fungerer en `for...of`-løkke under panseret: Den bruker dette mønsteret med `.next()`.


Du vil få samme resultat med


```javascript
const names = ["Lina", "Tom", "Eva"]

for (const result of names) {
console.log(result)
}
```


### Gjør en klasse iterabel


Du kan også definere din egen **iterable-klasse** ved å legge til en `[Symbol.iterator]()`-metode.


La oss si at vi vil ha en klasse som representerer et **tallområde**, for eksempel fra 1 til 5.


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


Dette skriver ut:


```
1
2
3
4
5
```


Her er hva som skjer:



- Vi har definert en klasse `Range`
- Inne i klassen har vi implementert `[Symbol.iterator]()`, slik at JavaScript vet hvordan den skal itereres
- Metoden `next()` gir tilbake hvert tall ett og ett
- Når vi når `slutt`, returnerer den `{ done: true }`


Nå fungerer `Range`-klassen vår som en matrise, og vi kan bruke den i alle løkker som forventer en iterabel.


### Generatorfunksjoner og `yield`


For å gjøre det enklere å lage iteratorer har JavaScript **generatorfunksjoner**, ved hjelp av nøkkelordet `function*` (det er `function` med en `*` på slutten) og nøkkelordet `yield`.


La oss prøve:


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


Hver `yield` gir tilbake en verdi, og **pauser** funksjonen til neste `.next()` blir kalt.


Du kan også løkke over en generator med `for...of`:


```javascript
for (const num of numberGenerator()) {
console.log(num)
}
```


Dette skriver ut:


```
1
2
3
```


## Samtidighet med tilbakekallinger

<chapterId>f3fc76ca-b3ef-54eb-a06e-501007002054</chapterId>


Frem til nå har koden vår vært **synkron**: den kjører én linje om gangen, i rekkefølge. Men noen ting i den virkelige verden tar tid, og vi vil ikke at hele programmet skal stå på pause mens vi venter.


I dette kapittelet skal vi introdusere et nytt konsept: **konkurranse**. Det lar oss manipulere rekkefølgen ting blir gjort i. Dette er nyttig når vi har å gjøre med ting som tidtakere, brukerinndata eller lesing av filer fra disken. JavaScript tilbyr ulike verktøy for samtidighet.


### `setTimeout`


Med funksjonen `setTimeout` kan du **kjøre en funksjon senere**, etter at det har gått en viss tid.


Eksempel:


```javascript
console.log("Start")

setTimeout(
() => console.log("This runs after 2 seconds"),
2000
)

console.log("End")
```


Dette skriver ut:


```
Start
End
This runs after 2 seconds
```


Selv om `setTimeout` vises midt i koden, blokkerer den ikke resten. I stedet planlegger den funksjonen til å kjøre **senere**, og går umiddelbart videre.


2000 betyr 2000 millisekunder (som er 2 sekunder).

Her er en mer ordrik og nybegynnervennlig omskriving av **Callbacks**- og **Promise**-seksjonene, med gjennomgående datamanipulering og tydelige annotasjoner:


### Tilbakekallinger


En **callback** er bare en funksjon som vi gir til en annen funksjon, slik at den kan **oppringes senere**.


La oss se på et reelt eksempel med tall. Tenk deg at vi har en liste med tall, og at vi ønsker å doble hvert av dem, og deretter bruke en funksjon (tilbakeringingen) på den resulterende "doblede" matrisen, men vi ønsker å gjøre det etter en liten forsinkelse, som om vi venter på noe tregt (som å laste inn data fra internett).


Her er en funksjon som gjør det ved hjelp av en **callback**:


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


La oss prøve å bruke denne funksjonen:


```javascript
const input = [1, 2, 3]

doubleNumbers(input, function(result) {
console.log("Here is the doubled array:", result)
})
```


Etter 1 sekund skrives dette ut:


```
Here is the doubled array: [ 2, 4, 6 ]
```


**Hva er det som skjer her?


1. Vi sender `input` som en liste over tall vi ønsker å doble.

2. Vi sender også en **callback-funksjon** som forteller programmet hva det skal gjøre *etter* doblingen.

3. Inne i `doubleNumbers` simulerer vi en forsinkelse ved hjelp av `setTimeout`, og deretter utfører vi doblingen.

4. Når det er gjort, kaller vi tilbakekallingen på den resulterende "doblede" matrisen.


Denne teknikken fungerer, men tenk deg at du vil gjøre **flere trinn** etter det, for eksempel filtrere ut små tall og deretter legge dem sammen. Da må du **neste** flere tilbakekallinger som dette:


```javascript
doubleNumbers(input, function(doubled) {
filterBigNumbers(doubled, function(filtered) {
sumNumbers(filtered, function(total) {
console.log("Final result:", total)
})
})
})
```


Dette er Hard å lese og rotete. Denne stilen kalles **callback-helvete**, og det er akkurat det `Promise` ble laget for å fikse.


## Samtidighet med løfter

<chapterId>30fddaca-729f-5c8d-bf86-8dfc7b3c9800</chapterId>


Et `Promise` er et innebygd JavaScript-objekt som representerer en verdi som vil **være klar i fremtiden**.


Vi kan lage et løfte som dette:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve("It worked!") // This means everything went OK
})
```


Delen `new Promise()` oppretter løftet.


Inne i den gir vi den en funksjon med to parametere:



- `resolve`, er en funksjon vi kaller når alt er vellykket
- `reject`, er en funksjon vi kaller hvis noe går galt


I eksempelet ovenfor løser vi det bare umiddelbart med meldingen "Det fungerte!".


### `.then()`


For å gjøre noe **etter** at løftet er utført, bruker vi `.then()`:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve(100) // This means everything went OK
})

promise.then(result => {
console.log("The result is:", result)
})
```


Dette skriver ut:


```
The result is: 100
```


Verdien vi sendte til `resolve()`, blir sendt til funksjonen i `.then()` som `result`.


La oss simulere en oppgave som tar 2 sekunder ved hjelp av `setTimeout`:


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


Dette vil vente i 2 sekunder og deretter skrive ut:


```
Done waiting!
```


### `avvis()`


La oss lage et løfte som **ikke lykkes**:


```javascript
const failingPromise = new Promise((resolve, reject) => {
reject("Something went wrong")
})
```


Hvis vi nå bruker `.then()` på dette, vil ingenting skje, fordi `.then()` bare håndterer suksess.


For å håndtere feil bruker vi `.catch()`:


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


Dette skriver bare ut


```
Caught an error: Something went wrong
```


Verdien som sendes til `reject()`, sendes til `.catch()`-funksjonen.


La oss lage et løfte som **av og til fungerer og av og til mislykkes**, basert på en eller annen betingelse.


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


Nå kan vi kalle dette og håndtere begge tilfellene:


```javascript
checkNumber(5)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Dette skriver ut:


```
Success: Positive number
```


Og hvis vi prøver med et annet nummer:


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


### Kjetting av operasjoner ved hjelp av `Promise`



Vi kan skrive om vårt tidligere eksempel ved å bruke `Promise`, og det vil se mye renere ut.


La oss starte med å skrive en ny versjon av doblingsfunksjonen vår, men denne gangen returnerer den et **løfte**:


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


Nå kan vi bruke `.then()` til å fortelle JavaScript hva vi skal gjøre med resultatet:


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


Dette skriver ut:


```
Doubled numbers: [ 2, 4, 6 ]
```


Så langt fungerer dette på samme måte som callback-versjonen, men nå er koden enklere å utvide og lese.


La oss si at vi ønsker å legge til flere trinn:


1. Først dobler du alle tallene

2. Fjern deretter tall som er mindre enn 4

3. Til slutt legger du dem alle sammen


Vi kan skrive én funksjon for hvert trinn, som alle bruker løfter:


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


Nå kan vi **kjede** dem sammen på denne måten:


```javascript
const input = [1, 2, 3]

doubleNumbers(input)
.then(filterBigNumbers)
.then(sumNumbers)
.then(
result => console.log("Final result after all steps:", result)
)
```


Dette skriver ut:


```
Final result after all steps: 10
```


La oss gå gjennom hva dette gjør:


1. `doubleNumbers` dobler matrisen: `[2, 4, 6]`

2. `filterBigNumbers` fjerner alt ≤ 3: `[4, 6]`

3. `sumNumbers` legger sammen de resterende tallene: `4 + 6 = 10`

4. Til slutt skriver vi ut resultatet.


Hver `.then()` venter på at trinnet før det er ferdig. Slik kan vi bygge en **kjede av handlinger** uten nesting. Dette gjør koden mer lesbar og enklere å feilsøke.


## Samtidighet med `async`/`await`

<chapterId>6e93d29f-c8bf-5fd1-a9c9-4e794ee6cbd0</chapterId>


Vi så hvordan `Promise`-kjeder hjelper oss med å unngå tilbakekallingshelvete, men de kan likevel bli litt Hard å lese når det er mange trinn involvert.


Det er her `async` og `await` kommer inn i bildet. De lar oss skrive asynkron kode **som ser ut som synkron kode**, noe som gjør den lettere å forstå.


### Hva er `async`?


Når du skriver nøkkelordet `async` foran en funksjon, pakker JavaScript automatisk inn funksjonens returverdi i et Promise.


La oss se et grunnleggende eksempel:


```javascript
async function greet() {
return "hello"
}
```


Hvis du kaller denne funksjonen:


```javascript
const result = greet()
console.log(result)
```


Du vil se dette:


```
Promise { 'hello' }
```


Selv om du bare returnerte en streng, gjør JavaScript den om til et Promise for deg. Du kan få den faktiske verdien ved å bruke `.then()` slik:


```javascript
greet().then( result => console.log(result) ) // prints "hello"
```


Eller du kan bruke `await`...


### Hva er "vente"?


Nøkkelordet `await` forteller JavaScript: "Vent til dette løftet er utført, og gi meg deretter resultatet."


Men du kan bare bruke `await` **innenfor en asynkron funksjon**.


La oss omskrive eksempelet ved hjelp av `await`:


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


Nå kan vi bruke resultatet som om det var en vanlig verdi.


La oss gjøre noe litt mer nyttig nå.


### Simulering av en forsinkelse med `await`


Vi lager en enkel `wait`-funksjon som tar et antall millisekunder som argument og bare løser opp etter så mange millisekunder, uten å gjøre noe annet:


```javascript
function wait(ms) {
return new Promise(resolve => {
setTimeout(resolve, ms)
})
}
```


La oss prøve å bruke den:


```javascript
async function test() {
console.log("waiting 2 seconds...")
await wait(2000)
console.log("done waiting")
}

test()
```


Dette skriver ut:


```
waiting 2 seconds...
done waiting
```


Du kan tenke på "vent" som "ta en pause her til løftet er gjort, og fortsett deretter"


Dette gjør at du kan skrive kode på en **topp-til-bunn**-måte som oppfører seg asynkront, uten å kjede sammen `.then()`-kall.


### Venter på data


La oss gjenbruke vårt forrige eksempel, der vi dobler tall, filtrerer og summerer. Men denne gangen bruker vi `async`/`await`.


Vi skal lage tre funksjoner som simulerer venting, og som returnerer Promises:


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


La oss nå skrive en `async`-funksjon for å kombinere dem:


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


Dette skriver ut:


```
Final result: 10
```


Dette er mye enklere å lese enn å kjede `.then()` eller nesting av tilbakekallinger.


Det ser ut som et vanlig trinn-for-trinn-program, men det oppfører seg likevel asynkront.


## Asynkrone Iteratorer

<chapterId>438b037d-9931-56d7-9052-7b4470f3c75b</chapterId>


Du har allerede lært om **iteratorer** og hvordan vi kan bruke `for...of` til å loope over matriser og andre iterable ting.


Men hva om dataene vi ønsker å iterere over, tar tid å få inn?


Noen ganger ønsker vi å loope over ting som kommer **asynkront**, for eksempel meldinger fra en chat, linjer fra en fil eller tall fra en langsom kilde.


For å gjøre det har JavaScript gitt oss **async-iteratorer**.


### Asynkrone generatorfunksjoner


Den enkleste måten å lage en asynkron iterator på, er å bruke en **asynkron generatorfunksjon**.


Vi skriver det slik:


```javascript
async function* generateNumbers() {
yield 1
yield 2
yield 3
}
```


Dette ser ut som en vanlig generator, men med `async` foran.


Vi kan nå bruke `for await...of` til å konsumere verdiene:


```javascript
async function run() {
for await (const n of generateNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


Dette vil skrives ut:


```
Got number: 1
Got number: 2
Got number: 3
Done!
```


Så hva er forskjellen fra en vanlig generator?


Forskjellen er at vi nå kan bruke `await` inne i generatoren.


La oss lage en forsinkelseshjelper igjen:


```javascript
function wait(ms) {
return new Promise(resolve => setTimeout(resolve, ms))
}
```


La oss nå gi tall **langsomt**:


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


Prøv å bruke den:


```javascript
async function run() {
for await (const n of generateSlowNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


### Hvorfor bruke asynk iteratorer?


Asynkrone iteratorer er nyttige når:



- Alle verdiene kommer ikke på én gang.
- Du vil håndtere dem én om gangen, **etter hvert som de kommer**.
- Du jobber med Promises, og ønsker å loope på en ren måte.


Hvis du for eksempel vil laste inn meldinger fra en chatteserver én etter én, eller laste ned en stor fil i biter, gir asynk iteratorer deg en måte å skrive en `for`-løkke som fungerer med forsinkede data.


### `Symbol.asyncIterator`


Vi kan også bruke asynk iteratorer i egendefinerte klasser.


Her er et eksempel som produserer tall med en forsinkelse:


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


Vi kan nå bruke `for await...of` akkurat som før:


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


Dette gjør at du kan opprette objekter som kan itereres over asynkront


## Assignment syntaks sukker

<chapterId>8b1ba7d8-ecfd-5470-b86e-73cb84ccc8b7</chapterId>


"Syntaktisk sukker" betyr å skrive noe på en kortere eller enklere måte, uten å endre hva det gjør. Det er bare en finere måte å si det samme på.


JavaScript har noen innebygde syntaktiske hjelpemidler som lar oss skrive renere og kortere deklarasjoner. I dette kapittelet skal vi se på hvordan vi kan tilordne verdier basert på en betingelse, oppdatere variabler med matematikk, hente verdier fra matriser eller objekter og kopiere eller kombinere dem med enklere syntaks.


### Den ternære operatoren


I JavaScript kan du tilordne en verdi basert på en betingelse ved hjelp av **ternary-operatoren**, som er en kort måte å skrive `if...else` på.


I stedet for å gjøre:


```javascript
let message

if (isMorning) {
message = "Good morning"
} else {
message = "Hello"
}
```


Du kan skrive:


```javascript
const message = isMorning ? "Good morning" : "Hello"
```


Det betyr..:



- Hvis `isMorning` er true, bruk `"God morgen"`
- Ellers bruker du `"Hello"`


Den generelle formen er:


```javascript
condition ? valueIfTrue : valueIfFalse
```


Du kan også bruke den i andre uttrykk:


```javascript
console.log(isSunny ? "Go outside" : "Stay in")
```


Bare sørg for å bruke det til **enkle** beslutninger. Hvis logikken er kompleks, bør du holde deg til `if...else`.


### Alternative Assignment-operatører


JavaScript har **forkortelsesoperatorer** for å utføre oppgaver kombinert med operasjoner.


La oss se på den normale måten:


```javascript
let counter = 1
counter = counter + 1
```


Dette kan forkortes til:


```javascript
let counter = 1
counter += 1 // same as counter = counter + 1
```


Her er de vanligste:


| Operator | Meaning             |
| -------- | ------------------- |
| `+=`     | add and assign      |
| `-=`     | subtract and assign |
| `*=`     | multiply and assign |
| `/=`     | divide and assign   |

Eksempler:


```javascript
let score = 10
score += 5  // now score is 15
score *= 2  // now score is 30
score -= 10 // now score is 20
```


Disse er nyttige når du vil oppdatere en variabel ved hjelp av dens egen verdi.


### Destrukturering


*med *Destructuring** kan du enkelt ta verdier ut av matriser eller objekter og lagre dem i variabler.


#### Matriser


Sett at du har det:


```javascript
const colors = ["red", "green", "blue"]
```


I stedet for å gjøre:


```javascript
const first = colors[0]
const second = colors[1]
```


Det kan du gjøre:


```javascript
const [first, second] = colors
```


Dette tildeler:



- `først` til `"rød"`
- `andre` til `"Green"`


Du kan også hoppe over verdier:


```javascript
const [,, third] = colors
console.log(third) // blue
```


#### Gjenstander


Du kan også trekke ut verdier fra objekter:


```javascript
const user = { name: "Alice", age: 30 }

const { name, age } = user
console.log(name) // Alice
console.log(age)  // 30
```


Hvis egenskapen har et annet navn enn variabelen du ønsker, kan du gi den et nytt navn:


```javascript
const { name: username } = user
console.log(username) // Alice
```


Destrukturering gjør koden din renere når du arbeider med objekter og matriser.


### Spredt syntaks


Syntaksen **spread** bruker `...` til å pakke ut eller kopiere verdier.


#### Matriser


Du kan kopiere eller slå sammen matriser:


```javascript
const a = [1, 2]
const b = [3, 4]

const both = [...a, ...b]
console.log(both) // [1, 2, 3, 4]
```


Du kan også klone en matrise:


```javascript
const original = [10, 20, 30]
const clone = [...original]
```


#### Gjenstander


Du kan gjøre det samme med objekter:


```javascript
const a = { x: 1 }
const b = { y: 2 }

const merged = { ...a, ...b }
console.log(merged) // { x: 1, y: 2 }
```


Du kan også overstyre verdier:


```javascript
const user = { name: "Alice", age: 30 }
const updated = { ...user, age: 31 }

console.log(updated) // { name: "Alice", age: 31 }
```


Dette er svært nyttig når du skal oppdatere objekter uten å endre originalen.


# NodeJS

<partId>42fe4d49-dace-5135-bb9e-b9d75034fb2a</partId>


## Hvordan kom vi til Node

<chapterId>0da1d60c-06c9-54e6-a181-ae7dabf6e3b8</chapterId>


I dette kapittelet skal vi lære litt om den historiske konteksten til JavaScript og NodeJS.


Historisk kontekst er svært viktig når det gjelder programvare, fordi vi ofte bruker verktøy som er utviklet av andre, og vi blir derfor påvirket av beslutninger som er tatt av dem tidligere.


Hvis vi forstår bakgrunnen for disse beslutningene, og hvordan verktøyene vi bruker, har blitt som de er, vil vi føle oss litt mindre forvirret over hva vi gjør.


### Opprinnelsen til JavaScript


JavaScript startet som et enkelt språk utviklet for å gjøre nettsider interaktive.


På 1990-tallet la nettlesere som Netscape Navigator til JavaScript, slik at utviklere kunne skrive kode som kjørte direkte i nettleseren.


Den opprinnelige ideen var å ha Java som kjernespråk for å lage nettsteder (med de såkalte "Java-appletene"), og JavaScript bare for mindre ting.


Kjernedesignet ble laget av Brendan Eich, som på den tiden var ansatt i Netscape, på mindre enn to uker.


Men de fleste foretrakk å bruke JavaScript fremfor Java, og i tillegg hadde Java-applets en del sikkerhetsproblemer på den tiden, så etter hvert ble Java droppet som alternativ, og JavaScript ble de facto-standarden for webutvikling.


### V8-motoren


JavaScript er et tolket språk, i motsetning til kompilerte språk som C.


Kode skrevet i et kompilert språk blir omgjort til en binær fil, og den binære filen blir sendt direkte til datamaskinens CPU.


![](assets/en/6.webp)


Interpred-språk, derimot, er gjerne mer brukervennlige og ligger nærmere hvordan mennesker tenker ("høyt nivå") enn hvordan maskiner fungerer ("lavt nivå"), og de har derfor vanligvis en virtuell maskin som kjører koden deres.


En virtuell maskin er et spesialprogram som sitter mellom koden du skriver og CPU-en, og som kjører koden din (fordi CPU-en ikke kan forstå den).


Dette gjør at du kan programmere uten å vite for mye om den underliggende maskinen, men det har også en kostnad i form av ytelse, fordi datamaskinen ikke bare kjører programmet ditt; den kjører et program (den virtuelle maskinen) som kjører programmet ditt.


Etter hvert som nettapplikasjonene ble mer og mer komplekse, ble det behov for å forbedre ytelsen til JavaScript. V8-motoren er tolken som driver JavaScript i Google Chrome. Den ble utviklet hos Google og lansert i 2008.


Mens de eldre JavaScript-motorene stort sett var tradisjonelle virtuelle maskiner, er V8-motoren en JIT-kompilator (just-in-time).


JavaScript-koden mates til V8-motoren, og motoren prøver å kompilere deler av den som native binærfiler underveis. På denne måten får du opplevelsen av et høynivåspråk, samtidig som ytelsen ligger litt nærmere et lavnivåspråk. Dette har gjort JavaScript til det raskeste høynivåspråket i verden, litt av en "det beste fra begge verdener"-greie.


### NodeJS-kjøretiden


Selv om JavaScript var enkelt å bruke og ganske raskt å utføre, hadde det etter lanseringen av V8 en stor begrensning: Det kunne bare kjøres i en nettleser.


Hvorfor er det et problem?


Vel, siden nettlesere kjører kode hentet fra millioner av forskjellige kilder på Internett, kan de lett bli infisert med skadelig programvare, så de er "sandkassert" fra resten av operativsystemet.


![](assets/en/7.webp)


JavaScript hadde ikke tilgang til filsystemet og andre lokale ressurser på datamaskinen (i hvert fall ikke på samme enkle måte som andre språk), så det var en betydelig begrensning for hva slags applikasjoner du kunne bygge med det.


I 2009 publiserte Ryan Dahl NodeJS, som er en kjøretid som gjør det mulig å bruke V8-motoren utenfor nettleseren, direkte på det opprinnelige operativsystemet på datamaskinen. Den legger også til mange funksjoner som er nyttige for å skrive programmer på serversiden og kommandolinjen. Du kan for eksempel bruke NodeJS til å opprette en webserver, lese og skrive filer eller bygge verktøy som automatiserer oppgaver.


![](assets/en/8.webp)


I dette kurset har vi så langt utforsket JavaScript-funksjonene som finnes både i nettleseren og i NodeJS. Disse funksjonene har gjort det mulig for oss å definere data og manipulere dem på abstrakte måter. I de neste leksjonene skal vi utforske funksjonene som er spesifikke for NodeJS, og som gjør det mulig for oss å samhandle med operativsystemet.


## Argumenter på kommandolinjen

<chapterId>960d20f3-c424-5d51-a041-ef17d2e94b6d</chapterId>


NodeJS gir oss blant annet mulighet til å bygge CLI-er (Command Line Interfaces).


Til det trenger vi en måte å motta kommandolinjeargumenter på, noe som i Node gjøres ved hjelp av det innebygde `process`-objektet.


### `prosess`


NodeJS har et spesielt objekt kalt `process` som representerer det programmet som kjører for øyeblikket.


Du kan bruke den til å inspisere miljøet, den gjeldende arbeidskatalogen og til og med avslutte programmet når det er nødvendig.


For eksempel:


```javascript
console.log(process.platform)
```


Her skrives operativsystemets plattform ut, for eksempel `win32`, `linux` eller `darwin` (Mac).


### `prosess.argv`


Når du kjører et NodeJS-program fra terminalen, kan du sende med ekstra ord (argumenter) etter skriptnavnet. Disse lagres i `process.argv`.


Hvis du for eksempel kjører denne kommandoen:


```
node my_script.js alpha beta
```


Du kan skrive ut argumentene på denne måten:


```javascript
console.log(process.argv)
```


Utdataene kan se slik ut:


```
[ '/path/to/node', '/path/to/my_script.js', 'alpha', 'beta' ]
```


De to første elementene er alltid Node-banen og skriptbanen din. Eventuelle tilleggsord du har sendt til skriptet, kommer etter dette.


`process.argv`-arrayen kan kuttes som en hvilken som helst annen array ved hjelp av `.slice()`-metoden, så for å få bare de argumentene som ble sendt, kan du gjøre


```javascript
const args = process.argv.slice(2)

console.log(args)
```


Å ha tilgang til argumentene som brukeren sender, er grunnleggende for å utvikle kommandolinjeprogrammer.


## Moduler

<chapterId>4e1651a5-65fd-50bc-b22a-40313d5659ca</chapterId>


JavaScript-kjøretimer som NodeJS behandler vanligvis hver JavaScript-fil som en egen modul.


Tenk på en modul som en boks. Boksen har sitt eget private område, slik at variablene og funksjonene du deklarerer i den, ikke forstyrrer koden i andre bokser. I utgangspunktet har hver modul sitt eget scope.


En modul kan eksportere noe av innholdet sitt, slik at det blir tilgjengelig for andre moduler, og den kan importere innhold som andre moduler har eksportert. JavaScript gjør det mulig å eksportere og importere innhold mellom moduler, slik at ulike filer kan kobles sammen.


Et JavaScript-program består ofte av flere moduler som er koblet til hverandre.


Hvorfor bruke moduler? Ved å dele opp koden i moduler kan du organisere programmet i mindre, oversiktlige og gjenbrukbare deler. Hver modul kan fokusere på én type oppgave, for eksempel håndtering av matematiske beregninger, arbeid med filer eller formatering av tekst.


### Felles JS-moduler


I NodeJS kalles det vanligste systemet for å administrere moduler **CommonJS**.


I dette systemet kan du dele (eksportere) kode fra en modul ved hjelp av `module.exports` og laste (importere) den inn i en annen fil ved hjelp av `require()`.


Hvis du vil gjøre noe tilgjengelig utenfor en modul, tilordner du det til `module.exports`:


```javascript
const greeting = "Hello!"

module.exports = greeting
```


Her er det strengen `"Hello!"` som denne modulen eksporterer.


Hvis du vil bruke den eksporterte koden fra en annen fil, bruker du funksjonen `require()` med stien til den aktuelle filen:


```javascript
const greeting = require("./greeting.js")

console.log(greeting)
```


Dette skriver ut:


```
Hello!
```


Du kan eksportere flere ting ved å samle dem i et anonymt objekt, for eksempel


```javascript
const greeting1 = "hello"

const greeting2 = "hi"

module.exports = {
greeting1, greeting2
}
```


CommonJS var modulsystemet som opprinnelig ble tatt i bruk av NodeJS. Senere ble også ES-moduler lagt til.


### ES-moduler


NodeJS støtter også en annen type moduler som kalles **ES Modules**, som er populære innen webutvikling. De bruker nøkkelordene `export` og `import`.


ES-moduler ble utviklet for nettleseren og først senere lagt til i Node. Hvis du vil bruke dem, må du kanskje bruke `.mjs` som filtype i stedet for `.js`, avhengig av hvilken Node-versjon du bruker.


I en fil kalt `greeting.mjs` skriver vi


```javascript
export const greeting = "Hello!"
```

Som du kan se, eksporterer vi konstanten direkte dit den blir definert


Vi importerer den i en annen fil som heter `index.mjs`:


```javascript
import { greeting } from "./greeting.mjs"

console.log(greeting)
```


Du kan eksportere forskjellige deklarasjoner i forskjellige deler av filen, for eksempel


```javascript
export const num = 10

export function double (x) {
return x*2
}
```


### NodeJS standardbibliotek


NodeJS inneholder også mange innebygde moduler. Dette er ferdige moduler som leveres av NodeJS, og som hjelper deg med vanlige oppgaver som å lese filer, arbeide med operativsystemet eller koble deg til nettverket.


Modulen `os` gir deg for eksempel informasjon om operativsystemet ditt:


```javascript
const os = require("os")

console.log(os.platform())
```


Du trenger ikke å installere disse innebygde modulene, de følger med NodeJS. De utgjør "standardbiblioteket" i kjøretiden, og brukes av de fleste Node-applikasjoner til å gjøre ting som å lese filer eller kommunisere via Internett.


I de neste kapitlene får du noen nyttige eksempler på hvordan de kan brukes.


## Modulen "fs

<chapterId>911e953a-35ae-5ee7-bd74-372501c32e81</chapterId>


Modulen `fs` (forkortelse for **filsystem**) er en del av NodeJS' standardbibliotek. Den lar deg arbeide med filer og kataloger på datamaskinen din: du kan lese filer, skrive filer, slette dem, gi dem nytt navn og mye mer.


For å bruke den må du først importere den øverst i filen din:


```javascript
const fs = require("fs")
```


### Synkroniser API


Den enkleste måten å bruke `fs` på, er med **sync**-metodene.


Disse metodene blokkerer programmet til de er ferdige (slik at neste kodelinje ikke kjøres før operasjonen er fullført).


Her er et eksempel på synkron lesing av en fil:


```javascript
const fs = require("fs")

const data = fs.readFileSync("example.txt", "utf8")

console.log(data)
```


Hvis det finnes en fil som heter `example.txt` i samme katalog som skriptet ditt, vil dette skrive ut innholdet i den.


Du kan også skrive til en fil synkront:


```javascript
const fs = require("fs")

fs.writeFileSync("output.txt", "Hello from Node!")

console.log("File written!")
```


Dette oppretter (eller overskriver) en fil som heter `output.txt` med teksten.


Her er noen vanlige operasjoner du kan utføre med dette API-et:


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


Synkroniserings-API-et er enkelt og bra for små skript, men fordi det blokkerer programmet til det er ferdig, kan det gjøre ting tregere hvis du jobber med store filer eller en server.


### Tilbakekalling asynkron API


API-et **callback** er ikke-blokkerende: det lar NodeJS fortsette å gjøre andre ting mens filoperasjonen utføres.


I stedet for å returnere resultatet direkte, tar den en funksjon (en **callback**) som blir kalt når operasjonen er ferdig.


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


Dette er hva som skjer:



- `fs.readFile` begynner å lese `example.txt`.
- NodeJS venter ikke, den går videre til å utføre annen kode du måtte ha skrevet.
- Når filen er ferdig lest, kjøres tilbakekallingen:



  - Hvis det oppstod en feil, inneholder `err` feilmeldingen.
  - Ellers inneholder `data` innholdet.


Slik skriver du til en fil:


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


Samme idé: Programmet stopper ikke mens du skriver filen.


Noen eksempler på ting du kan gjøre med dette API-et:


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


Tilbakekallings-API-et er bedre for servere og store oppgaver fordi det ikke blokkerer programmet, men nestede tilbakekallinger kan bli rotete hvis du kjeder sammen mange operasjoner. Derfor ble det lagt til et løftebasert asynkron API.


### Promise asynkron API


Det Promise-baserte API-et er moderne og fungerer utmerket med `.then()` og `async/await`. Det er tilgjengelig som `fs.promises`.


Du må importere egenskapen `promises`:


```javascript
const fs = require("fs").promises
```


Ved hjelp av `.then()`:


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


Eller enda bedre, ved å bruke `async/await`:


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


Skrive til en fil:


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


Den vanlige listen med eksempler for API-et:


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


Når du skriver kode, må du ofte bruke kode som er skrevet av andre, for eksempel biblioteker som hjelper deg med å arbeide med datoer, farger, servere eller nesten hva som helst annet.


I stedet for å laste ned og kopiere filer manuelt, kan du bruke en **pakkebehandler**.


En pakkebehandler er et verktøy som:



- nedlastingspakker
- holder oversikt over hvilke pakker prosjektet ditt trenger
- sørger for at alle i teamet ditt har de samme versjonene av pakkene


### Hva er NPM?


I NodeJS-verdenen er den mest populære pakkebehandleren **NPM**, som står for *Node Package Manager*.


Du får NPM automatisk når du installerer NodeJS.


Du kan sjekke om du har NPM ved å kjøre dette i terminalen:


```
npm -v
```


Dette skriver ut hvilken versjon av NPM du har, for eksempel:


```
10.2.1
```


### Opprette en pakke


I NodeJS er en **pakke** bare en katalog med en `package.json`-fil i.


La oss lage en steg for steg.


1. Opprett en ny mappe for prosjektet ditt:


```
mkdir my_project
cd my_project
```


2. Kjør denne kommandoen:


```
npm init
```


Dette starter et interaktivt oppsett, der du blir stilt spørsmål som navn på prosjektet, versjon, beskrivelse osv.


Hvis du ikke ønsker å svare på alt og bare godta standardinnstillingene, kan du bruke :


```
npm init -y
```


Når du har kjørt den, vil du se en ny fil i mappen din som heter:


```
package.json
```


### `pakke.json`


Filen `package.json` er bare en JSON-fil som lagrer metadata om prosjektet ditt.


Her er et eksempel:


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


Noen få viktige felt:



- `name`: navnet på pakken din
- `version`: den gjeldende versjonen
- `main`: inngangsfilen (som `index.js`)
- `scripts`: kommandoer du kan kjøre (som `npm start`)
- `dependencies`: lister opp alle pakkene prosjektet ditt er avhengig av


### Installere en pakke


La oss si at du ønsker å bruke en bestemt pakke som heter `picocolors` for å legge til farger i terminalutdataene dine.


Du kan installere det ved å kjøre:


```
npm install picocolors
```


Du kan nå bruke den i prosjektet ditt. Lag en `index.js`-fil med


```javascript
const pico = require('picocolors')

console.log(
pico.green("This text is green!")
)
```


og prøv å kjøre den. Terminalen skal skrive ut en farget versjon av teksten.


Hva gjorde NPM?



- Den lastet ned pakken og lagret den i en undermappe som heter `node_modules/`
- den la til en oppføring under `dependencies` i `package.json`
- den oppdaterte filen `package-lock.json`


Hva er `package-lock.json`?


### `package-lock.json`


Denne filen opprettes automatisk av NPM.


Du lurer kanskje på hvorfor vi trenger enda en fil hvis vi allerede har `package.json`?

Her er grunnen til det:



- `package.json` sier bare hvilken versjon **range** av en pakke prosjektet ditt trenger.

Eksempel:


```json
"dependencies": {
"picocolors": "^1.1.0"
}
```


`^1.1.0` betyr "enhver versjon som er kompatibel med 1.1.x", så det er fleksibelt.



- `package-lock.json` **fryser** de nøyaktige versjonene av hver enkelt pakke og deres underavhengigheter, slik at alle som installerer prosjektet ditt får nøyaktig samme fungerende oppsett.


Hvorfor er dette viktig?


Hvis du jobber i et team, eller hvis du distribuerer prosjektet ditt til en server, eller hvis du kommer tilbake til det i fremtiden, vil du være sikker på at det fortsatt fungerer på samme måte.

Hvis pakkene har blitt oppdatert og du installerer på nytt uten en låsefil, kan det hende at du får en litt annen versjon som oppfører seg annerledes.


Ved å beholde `package-lock.json` i prosjektet ditt, vil NPM alltid installere de nøyaktige versjonene som er oppført der, slik at alle har det samme miljøet.


`package-lock.json` låser alt til en helt bestemt versjon, for å gjøre prosjektet mer reproduserbart på andre maskiner.


Men hvis pakken din skal brukes av mange mennesker, kan du i stedet velge å ikke committe den, slik at NPM bare finner filen `package.json` og får lov til å installere automatisk de nyeste versjonene som er tillatt i den filen.


Men dette er ting du bør bekymre deg for senere, når du begynner å publisere din egen kode. Foreløpig har vi bare introdusert det grunnleggende i NPM, slik at du kan finne og bruke biblioteker som er publisert av andre utviklere i prosjektene dine.



## Nettverk i NodeJS

<chapterId>f2cabd8b-754b-5c97-8d6a-8412a9a184c7</chapterId>


NodeJS brukes ofte som et språk for backend: Du kan gjøre skriptet ditt om til en server, og også bruke det til å sende forespørsler til andre servere.


I dette kapittelet skal vi introdusere noen grunnleggende nettverksfunksjoner som gjør det mulig for deg å gjøre det.


### `fetch()`


Hvis du vil at programmet ditt skal laste ned data fra et nettsted eller et API, må du sende en **HTTP-forespørsel**.


I moderne versjoner av NodeJS kan du bruke den innebygde funksjonen `fetch()`.


Her er et eksempel på en GET-forespørsel til et API:


```javascript
const response = await fetch("https://jsonplaceholder.typicode.com/posts/1")
const data = await response.text()

console.log(data)
```


Når du kjører dette, vil du se noe sånt som


```
{
"userId": 1,
"id": 1,
"title": "...",
"body": "..."
}
```


Her er hva som skjer:


1. `fetch()` tar en URL og sender en forespørsel.

2. Den returnerer et **Promise** som løses opp til et `Response`-objekt.

3. `response.text()` leser svarteksten som en streng.


Men strengen du får tilbake er faktisk JSON. Hva er det for noe?


### JSON


Når du arbeider med web-API-er, sendes og mottas dataene ofte som **JSON**, som står for JavaScript Object Notation.


JSON er bare et tekstformat som ligner mye på JavaScript-objekter. For eksempel


```json
{
"name": "Alice",
"age": 30,
"likes": ["apples", "bananas"]
}
```


Objektet `JSON` er et innebygd verktøy i JavaScript som kan brukes til å arbeide med dette dataformatet.


Du kan konvertere et JavaScript-objekt til en JSON-streng ved hjelp av `JSON.stringify()`:


```javascript
const user = { name: "Alice", age: 30 }

const jsonString = JSON.stringify(user)

console.log(jsonString)
```


Dette skriver ut:


```
{"name":"Alice","age":30}
```


Du kan også konvertere JSON-tekst tilbake til et JavaScript-objekt ved hjelp av `JSON.parse()`:


```javascript
const jsonText = '{"name":"Bob","age":25}'

const obj = JSON.parse(jsonText)

console.log(obj)
```


Dette skriver ut:


```
{ name: 'Bob', age: 25 }
```


Vær forsiktig: `JSON.parse()` vil gi en feilmelding hvis strengen ikke er gyldig JSON.


```javascript
JSON.parse("not json") // ❌ Error!
```


Så sørg for at strengen er riktig formatert.


### `http`-server


Med NodeJS kan du opprette en webserver uten å installere noe annet.


Du kan bruke den innebygde `http`-modulen til å håndtere forespørsler fra klienter og sende svar tilbake.


Her er et veldig enkelt eksempel:


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


Når du kjører dette skriptet og åpner `http://localhost:3000` i nettleseren din, vil du se:


```
Hello from NodeJS server!
```


Dette er det som skjer i koden:


1. Du har importert `http`-serveren fra Node-standardbiblioteket.

2. `http.createServer()` oppretter en server. Du sendte `http.createServer()` en tilbakekalling `(req, res) => {...}` som skal utføres hver gang noen kobler seg til.

3. Du tildelte statuskoden 200 (som indikerer en vellykket operasjon) til svaret. Du kan lese mer om http-statuskoder [her](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

3. `res.end()` sender svaret og avslutter forbindelsen.

4. `server.listen(3000)` starter serveren på port 3000.


Du kan også sjekke `req.url` og `req.method` i forespørselen for å håndtere ulike baner eller forespørselstyper.


Eksempel med ruting:


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


Dette er svært grunnleggende eksempler. For å bygge mer avanserte servere vil de fleste utviklere sannsynligvis laste ned et ferdig backend-bibliotek som [express] (https://www.npmjs.com/package/express).


## Behandling av data: buffere, hendelser, strømmer

<chapterId>8c9623f0-a604-51a4-8fe4-871c849d3e3b</chapterId>


I dette kapittelet introduserer vi først og fremst tre klasser av objekter:



- `Buffer`, som representerer små biter av binære data
- `EventEmitter`, som kan brukes til å spore en asynkron prosess ved å sende ut signaler kalt "events"
- `Stream`, som lar oss behandle store datamengder én `Buffer` om gangen, og som sporer prosessen ved å sende ut hendelser


Disse er svært vanlige i profesjonell NodeJS-kode, så selv om du kanskje ikke bruker dem i dine første prosjekter, er det bra å få en grunnleggende forståelse for når du trenger å samhandle med dem. av dem


### Buffere


I NodeJS er en **buffer** en type objekt som brukes til å arbeide med binære data.


Du kan tenke på en buffer som en beholder med fast størrelse for rå bytes.


Slik oppretter du en buffer fra en streng:


```javascript
const buf = Buffer.from("hello")
console.log(buf)
```


Dette skriver ut noe sånt som:


```
<Buffer 68 65 6c 6c 6f>
```


Disse tallene (`68`, `65`, `6c` osv.) er heksadesimale representasjoner av bokstavene i `"hallo".


Du kan konvertere den tilbake til en streng på denne måten:


```javascript
console.log(buf.toString())
```


Dette skriver ut:


```
hello
```


Du kan også opprette en buffer av en viss størrelse fylt med nuller:


```javascript
const buf = Buffer.alloc(10)
console.log(buf)
```


Dette skriver ut noe sånt som:


```
<Buffer 00 00 00 00 00 00 00 00 00 00>
```


Du kan skrive inn i bufferen:


```javascript
buf.write("abc")
console.log(buf)
```


Og du kan få tilgang til individuelle byte:


```javascript
console.log(buf[0]) // prints the ASCII number for 'a', which is 97
```


Buffere er spesielt nyttige når du trenger å manipulere data på et svært lavt nivå.


### Hendelser


I JavaScript er en **hendelse** noe som skjer i programmet ditt, og som du kan reagere på.


For eksempel:



- en fil er ferdig lastet inn
- en timer går av
- en bruker klikker på en knapp
- en nettverksforespørsel returnerer data


En **hendelse** er bare et signal om at noe har skjedd, og du kan skrive kode for å lytte etter slike hendelser og reagere på dem.


I NodeJS er det mange objekter som kan sende ut hendelser. Disse objektene kalles **EventEmitters**.


Her er et eksempel:


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


Dette skriver ut:


```
Hello! An event happened.
```


Nå skal du høre:


1. Vi oppretter et `EventEmitter`-objekt.

2. Vi forteller den at den skal kjøre en tilbakekalling hver gang hendelsen `"greet"` skjer, ved hjelp av `.on("greet")`.

3. Senere utløser vi `"greet"-hendelsen ved hjelp av `.emit()`.

4. Tilbakekallingen vår blir utført


Du kan sende data sammen med hendelsen:


```javascript
emitter.on("greet",
(name) => console.log(`Hello, ${name}!`)
)

emitter.emit("greet", "Alice") // first argument is the type of event, second argument is the data we pass with this event
```


Dette skriver ut:


```
Hello, Alice!
```


Du kan også registrere lyttere for andre arrangementer:


```javascript
emitter.on("goodbye", () => {
console.log("Goodbye!")
})

emitter.emit("goodbye")
```


Du kan knytte så mange lyttere du vil til en hendelsestype, og du kan utløse mange forskjellige hendelsestyper fra samme emitter.


Mange objekter i NodeJS sender ut hendelser for å fortelle resten av programmet at noe skjer.



### Hva er bekker?


Strømmer kombinerer buffere og hendelser for å hjelpe oss med å behandle data.


Når vi jobber med filer, data fra nettverket eller til og med lang tekst, er det ikke alltid vi trenger (eller ønsker) å laste alt inn i minnet på én gang. Det kan være tregt, eller til og med få programmet til å krasje hvis dataene er for store.


I stedet kan vi behandle dataene **bittelitt etter litt**, etter hvert som de ankommer eller leses, omtrent som å drikke vann gjennom et sugerør i stedet for å prøve å drikke hele glasset på én gang. Dette kalles en **strøm**.


I NodeJS er en strøm et objekt som lar deg lese data fra en kilde eller skrive data til en destinasjon **en bit om gangen**.


NodeJS har fire hovedtyper av strømmer:



- Readable**: strømmer du kan lese data fra (som å lese en fil)
- Writable**: strømmer du kan skrive data til (som å skrive til en fil)
- Tosidig**: strømmer som både kan leses og skrives
- Transform**: som tosidige strømmer, men de kan endre (transformere) dataene mens de flyter


### Lesbare strømmer


La oss si at du har en `bigfile.txt` å behandle. Du kan opprette en lesbar strøm med modulen `fs` for å lese filen bit for bit.


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


Hva skjer her?


1. `fs.createReadStream()` oppretter en lesbar strøm.

2. Hver gang en del av filen er klar, sender strømmen ut en `data`-hendelse og gir oss en "bit" med data (en `Buffer`). Vi skriver ut biten.

3. Når hele filen er lest, utløses hendelsen `end`.

4. Hvis det oppstår en feil (for eksempel at filen ikke finnes), utløses hendelsen `error`.


På denne måten kan du lese store filer uten å laste dem inn i minnet på én gang.


Hvis vi ønsker at dataene skal komme i en form som er lesbar for mennesker (i stedet for binær), kan vi spesifisere kodingen av strømmen:


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


Koden vil nå skrive ut filen i lesbar form.


### Skrivbare strømmer


Med en skrivbar strøm kan du sende data et sted, bit for bit.


Her er et eksempel på hvordan du skriver til en `target.txt`-fil ved hjelp av en strøm:


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


Dette er hva som skjer:


1. `fs.createWriteStream()` oppretter en skrivbar strøm.

2. Vi skriver litt tekst til den ved hjelp av `.write()`.

3. Når vi er ferdige, kaller vi `.end()` for å lukke strømmen.

4. Når alle dataene er skrevet, sendes hendelsen `finish` ut.

5. Hvis noe går galt, utløses hendelsen `error`.


På samme måte som lesbare strømmer er skrivbare strømmer gode for store datamengder, fordi de ikke trenger å holde alt i minnet samtidig.


### Rørstrømmer


Noe av det kuleste med strømmer er at du kan **pipe** dem sammen: koble en lesbar strøm direkte til en skrivbar strøm.


```javascript
const fs = require("fs")

const readable = fs.createReadStream("bigfile.txt")
const writable = fs.createWriteStream("target.txt")

readable.pipe(writable)
```


Her:



- Den lesbare strømmen leser fra `bigfile.txt`.
- Den skrivbare strømmen skriver til `copy.txt`.
- `.pipe()` sender dataene direkte fra den lesbare til den skrivbare strømmen.


### Tosidige strømmer


En dupleks strøm er både lesbar og skrivbar. Et eksempel er en nettverkssocket: Du kan sende data til den og motta data fra den.


Her er et veldig enkelt eksempel ved hjelp av `net`-modulen:


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


I dette eksempelet:



- `socket`-objektet er en tosidig strøm.
- Du kan `skrive()` til den og også lytte etter `data`-hendelser fra den.


### Transformere strømmer


En transformasjonsstrøm er en tosidig strøm som også modifiserer dataene som passerer gjennom den.


Du kan for eksempel bruke den innebygde `zlib`-modulen til å komprimere eller dekomprimere data.


Slik komprimerer du en fil ved hjelp av en transformasjonsstrøm:


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


Og for å dekomprimere den tilbake:


```javascript
const readable = fs.createReadStream("bigfile.txt.gz")
const unzip = zlib.createGunzip()
const writable = fs.createWriteStream("bigfile.txt")

readable.pipe(unzip).pipe(writable)

writable.on("finish", () => {
console.log("File decompressed.")
})
```


Transformstrømmer er svært nyttige for oppgaver som komprimering, kryptering eller endring av filformater under strømming.


### Mottrykk


Noen ganger er en skrivbar strøm treg til å håndtere data. Hvis vi fortsetter å sende data til en skrivbar strøm raskere enn den kan håndtere, kan vi få problemer. Dette kalles **tilbaketrykk**.


Hvis du kaller metoden `.write()` på en skrivbar strøm, returnerer den en boolsk verdi som forteller deg om strømmen trenger en pause:


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


Dette var et illustrerende eksempel på manuell overføring av data fra en Readable til en Writable, og manuell håndtering av mottrykk.


Vanligvis bruker vi `.pipe()`-metoden, som håndterer mottrykk automatisk.


Du trenger altså bare å bekymre deg for mottrykk når du av en eller annen grunn kaller `.write()` manuelt.


## Sluttnote

<chapterId>139e2ab8-df67-525a-85f0-5a2fa5e478f2</chapterId>


Hvis du har fulgt med på leksjonene, bør du nå være i stand til å skrive noen enkle programmer i NodeJS.


Jeg foreslår at du gjør akkurat det: Etter å ha lært deg det grunnleggende, er den beste måten å øve seg på og bli en bedre programmerer på å bygge noen personlige prosjekter.


Det spiller egentlig ingen rolle hva du bygger, det viktige er at du utfordrer deg selv til å løse problemer med kode.


Moderne programmeringsspråk er utrolig kraftige, og NodeJS er sannsynligvis det beste verktøyet å eksperimentere med i denne fasen av reisen.


Lykke til!


# Siste del


<partId>322624d8-6fbc-11f0-a67a-5b145f10afc1</partId>


## Anmeldelser og rangeringer


<chapterId>3e93ac86-6fbc-11f0-8bae-9b2ed7914843</chapterId>

<isCourseReview>true</isCourseReview>

## Konklusjon


<chapterId>49b3b9b2-6fbc-11f0-9870-5f5adcd3a0eb</chapterId>


<isCourseConclusion>true</isCourseConclusion>