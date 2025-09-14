---
name: Základy JavaScriptu a NodeJS
goal: Naučte se základy programování v JavaScriptu a vývoj v NodeJS, abyste mohli vytvářet praktické aplikace a nástroje.
objectives: 

  - Zvládnutí základní syntaxe, typů a toku řízení jazyka JavaScript
  - Porozumění funkcím, objektům a třídám v jazyce JavaScript
  - Naučte se techniky zpracování chyb a ladění
  - Seznámení s NodeJS a jeho ekosystémem

---

# Začněte svou cestu vývoje


Vítejte v kurzu o JavaScriptu a NodeJS.


JavaScript je nejoblíbenější programovací jazyk na světě: je to skriptovací jazyk moderních prohlížečů, takže je v podstatě nemožné vytvořit moderní webovou aplikaci bez napsání *nějakého* JavaScriptu; a díky běhovému prostředí NodeJS jej lze používat i mimo prohlížeče a vytvářet skripty a aplikace, které běží přímo na počítači.


Tento kurz je určen pro ty, kteří s programováním začínají, nebo pro ty, kteří již dříve používali jiné jazyky, ale chtějí pochopit, jak JavaScript funguje, zejména v kontextu NodeJS.


Na konci kurzu byste měli být schopni psát vlastní programy v jazyce JavaScript, používat standardní knihovnu NodeJS a instalovat a používat balíčky třetích stran k vytváření užitečných nástrojů.


+++
# Základy jazyka JavaScript

<partId>a617327c-e5a2-52ca-9380-c63f44623dd4</partId>


## Nastavení

<chapterId>ba05a290-1782-5268-87c9-62fd09590e05</chapterId>




Program v jazyce JavaScript je pouze kolekce (jednoho nebo více) textových souborů, které obsahují příkazy, jež má spustit běhové prostředí jazyka JavaScript.


Názvy těchto textových souborů obvykle končí příponou `.js`, například `my_script.js`, `my_program.js` atd.


Příkazy, které obsahují, jsou napsány v programovacím jazyce JavaScript.


Runtime JavaScriptu je speciální program, který tyto soubory spouští.


![](assets/en/1.webp)


### Prostředí NodeJS


Nejběžnějším běhovým prostředím JavaScriptu je NodeJS.


Vaše IDE ho možná již obsahuje, nebo si jej budete muset stáhnout z [oficiálních stránek](https://nodejs.org/en/download).


Na stránce ke stažení najdete pokyny pro všechny tři hlavní operační systémy: Windows, Linux a MacOS. Předpokládá se, že víte, jak otevřít terminál ve vašem operačním systému.


Protože je NodeJS k dispozici pro všechny tři operační systémy, bude možné programy, které napíšete, spustit na všech z nich (s výjimkou některých okrajových případů).


To znamená, že můžete například napsat jednoduchou videohru v JavaScriptu na svém počítači s Windows a předat ji kamarádovi, aby ji spustil na svém Macu.


![](assets/en/2.webp)














### První program (hello world)


Při studiu programovacího jazyka se tradičně první program píše tak, že se na konzoli vypíše "Hello world!".


Vytvořte adresář `my_js_code/` a v něm soubor `main.js` (tyto názvy jsou libovolné).


Otevřete adresář pomocí svého editoru kódu.


Tento kód zapište do souboru:


```javascript
console.log("hello world!")
```


Otevřete terminál a spusťte tento příkaz pro spuštění programu:


```
node main.js
```


Výsledek by měl být


```
hello world!
```


### Co se stalo


V jazyce JavaScript je vše "objekt".


`console` je objekt, který slouží k ladění programu.


`console.log` je nejpoužívanější metodou `console`. Vypisuje pouze argumenty, které jí předáte.


Argumenty předáváte souboru `console.log` pomocí kulatých závorek `()`.


Pokud tedy například chcete vypsat číslo `1000`, stačí napsat


```javascript
console.log(1000)
```


Poté jej spusťte příkazem


```
node main.js
```


v terminálu (od této chvíle budeme předpokládat, že víte, jak se program spouští).


Mělo by se vytisknout


```
1000
```


Můžete předat více věcí, např


```javascript
console.log(16, 8, 1993)
```


Tím se vytiskne


```
16 8 1993
```


## Proměnné a poznámky

<chapterId>23050ab7-343b-5edf-9d37-e4e782e27ce0</chapterId>


Programy obvykle provádějí operace s daty.


Proměnné jsou jako pojmenované boxy, které používáme k ukládání dat. Umožňují nám přiřadit části dat konkrétní jméno, abychom je mohli později pomocí tohoto jména vyhledat.


### deklarace `let`


K deklaraci proměnné v jazyce JavaScript můžeme použít klíčové slovo `let`.


Po zápisu `let` napíšeme jméno, které chceme proměnné dát, pak znak `=` a pak hodnotu, kterou chceme uložit.


Například:


```javascript
let age = 25

console.log(age)
```


Název proměnné (odborně nazývaný "identifikátor") může obvykle obsahovat písmena, podtržítka (`_`), znak dolaru (`$`) a čísla, přičemž první znak nesmí být číslo.


Ve výše uvedeném kódu jsme deklarovali proměnnou `age` a uložili do ní hodnotu `25`.


Poté jsme hodnotu vypsali pomocí `console.log(age)`.


Pokud tento kód spustíte pomocí `node main.js`, výstup bude:


```
25
```


Identifikátory rozlišují malá a velká písmena, což znamená, že malá a velká písmena se počítají jako rozdíly v identifikátorech, takže např


```javascript
let age = 25

let Age = 20

console.log(age)
```


vypíše 25, protože se jedná o dvě zcela samostatné proměnné!


Do proměnné můžete ukládat také řetězce (text):


```javascript
let message = "hello again"

console.log(message)
```


Vytiskne se:


```
hello again
```


Stejně jako předtím jsme použili `console.log()` k vypsání hodnoty uložené v proměnné.


Nyní udělejme obojí dohromady:


```javascript
let age = 25

let message = "hello again"

console.log(age)

console.log(message)
```


Při spuštění se vytiskne:


```
25
hello again
```

### Přerozdělení


Proměnné deklarované pomocí `let` lze po jejich vytvoření měnit.


Tomu se říká přerozdělení.


```javascript
let score = 10

console.log(score)

score = 15

console.log(score)
```


Nejprve přiřadíme `10` do `score` a poté jej vypíšeme.


Pak změníme hodnotu `score` na `15` a znovu ji vypíšeme.


Výstupem bude:


```
10
15
```


To je velmi užitečné, pokud se hodnota v průběhu času mění, například ve hře, kde se zvyšuje skóre.


Přidejme k tomu další proměnnou:


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


Vytiskne se:


```
10
Alice
20
Bob
```


Jak vidíte, změnilo se jak `skóre`, tak `hráč`.


### deklarace `const`


Většinou však nechceme, aby se proměnná po vytvoření měnila. K tomu používáme `const`.


`const` je zkratka pro "konstantní". Jakmile přiřadíte proměnné `const` hodnotu, nemůžete ji změnit.


```javascript
const pi = 3.14
console.log(pi)
```


Tento tisk:


```
3.14
```


Ale pokud se o to pokusíte:


```javascript
const pi = 3.14
console.log(pi)

pi = 99 // this line will cause an error
console.log(pi)
```


JavaScript zobrazí chybu, jako je:


```
TypeError: Assignment to constant variable.
```


Je to proto, že `pi` bylo deklarováno pomocí `const` a jeho hodnotu již nelze změnit. Interpretovi JavaScriptu tím sdělujete, že nechcete, aby se tato proměnná měnila.


To je užitečné, protože se tím snižuje pravděpodobnost, že by se omylem změnil. Když se programy stanou velmi rozsáhlými, s tisíci řádky kódu, je nemožné udržet krok se vším, co se děje najednou (to je hlavní důvod, proč používáme počítače, k provádění složitých procesů, které nedokážeme spočítat vlastním mozkem), takže se stává užitečným mít taková omezení, která činí program více deterministickým.


Za osvědčený postup se považuje deklarovat hodnoty vždy jako `const`, pokud si nejsme jisti, že je chceme později upravit.


### Komentáře v jazyce JavaScript


Někdy chceme v kódu psát poznámky, které se neprovádějí. Těm se říká komentáře.


Komentáře jsou při běhu programu ignorovány, ale jsou užitečné pro vysvětlení nám nebo jiným lidem.


Chcete-li napsat jednořádkový komentář, použijte `//`


```javascript
// This is a comment
const x = 10 // This is also a comment
console.log(x)
```


I tak se vytiskne:


```
10
```


Komentáře jsou tu jen proto, aby si je lidé mohli přečíst.


Víceřádkové komentáře můžete psát také pomocí `/*` a `*/`


```javascript
/*
This is a multi-line comment.
It can span several lines.
*/
const y = 20
console.log(y)
```


Tím se vytiskne


```
20
```


A komentář bude ignorován.


Pomocí komentářů můžete do kódu přidávat drobné poznámky, abyste si mohli zapamatovat, co kód dělá a proč je napsán určitým způsobem. Může to také pomoci ostatním programátorům porozumět mu.


## Základní typy: čísla, řetězce, booleany

<chapterId>cfdb04f6-21a8-5143-bbf9-7aaae04962f0</chapterId>


V JavaScriptu "typ" udává, o jaký druh dat se jedná.


Javascript má několik základních typů a v této části se budeme věnovat některým z nich.


### Čísla a aritmetické operace


Prvním typem, který si představíme, je `číslo`.


Čísla v JavaScriptu mohou být celá (jako `5`) nebo desetinná (jako `3,14`).


Můžete s nimi počítat: sčítat, odčítat, násobit a dělit.


Zde je základní příklad:


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


Vytiskne se:


```
15
5
50
2
```


K řízení pořadí operací můžete použít také závorky `()`:


```javascript
const result = (2 + 3) * 4
console.log(result)
```


Tento tisk:


```
20
```


Bez závorek by to bylo `2 + 3 * 4`, což je:


```javascript
const result = 2 + 3 * 4
console.log(result)
```


To by se vytisklo:


```
14
```


V běžné matematice se totiž násobení děje před sčítáním.


### Řetězce a interpolace


Druhým typem JavaScriptu, který si představíme, je `string`.


Řetězce jsou části textu. K jejich vytvoření můžete použít jednoduché uvozovky `'...'` nebo dvojité uvozovky `"..."`.


```javascript
const greeting = "hello"
const name = 'Bob'
console.log(greeting)
console.log(name)
```


Tento tisk:


```
hello
Bob
```


Chcete-li řetězce kombinovat, můžete použít operátor `+`:


```javascript
const greeting = "hello"
const space = " "
const name = "Bob"

const fullGreeting = greeting + space + name
console.log(fullGreeting)
```


Vytiskne se:


```
hello Bob
```


Existuje však příjemnější způsob kombinování řetězců, který se nazývá **interpolace řetězců**. Řetězec deklarujete pomocí zpětných znaků `` `...`` a proměnné zapisujete pomocí `${...}` uvnitř řetězce:


```javascript
const greeting = "hello"
const name = "Bob"

const fullGreeting = `${greeting} ${name}`
console.log(fullGreeting)
```


To se také vytiskne:


```
hello Bob
```


Uvnitř `${...}` můžete uvést libovolný výraz:


```javascript
const age = 30
console.log(`Next year, I will be ${age + 1} years old.`)
```


Tento tisk:


```
Next year, I will be 31 years old.
```


Interpolace je v moderním JavaScriptu velmi rozšířená.


### Logické, porovnávací a logické operace


Třetím typem, který si představíme, je `boolean`. Je pojmenován po matematikovi Georgi Booleovi, který vynalezl booleovskou logiku.


Logické symboly jsou jednoduché: pouze dvě možné hodnoty, `pravda` a `nepravda`.


Můžete je uložit do proměnných:


```javascript
const theSkyIsBlue = true
const thisCourseIsBad = false

console.log(theSkyIsBlue)
console.log(thisCourseIsBad)
```


Tento tisk:


```
true
false
```


Logické operátory můžete kombinovat:



- `&&` znamená "a" a vrátí `pravdu` pouze v případě, že **obě** hodnoty jsou `pravdivé`, jinak vrátí `nepravdu`
- `||` znamená "nebo" a vrátí `pravdu`, pokud je alespoň jedna** z hodnot `pravdivá`, jinak (pokud jsou obě nepravdivé) vrátí `nepravdu`
- `!` znamená "ne", aplikuje se před boolean a převrátí ho: pokud je boolean `pravdivý`, vrátí `nepravdivý` a naopak.


![](assets/en/3.webp)


Příklady:


```javascript
const isSunny = true
const isWarm = true

console.log(isSunny && isWarm)  // true
console.log(isSunny || isWarm)  // true
console.log(!isSunny)           // false
```


V jazyce JavaScript můžete porovnávat hodnoty pomocí operátorů jako `>`, `<`, `===` a `!==`. Výsledkem těchto porovnání je vždy logická hodnota.


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


Javascript má také `>=` pro označení "větší nebo stejný" a `<=` pro označení "menší nebo stejný".


V programech se často kombinují logické operátory, porovnávací operátory a logické operátory, aby bylo možné deklarovat složité podmínky, jako například "e-mail dorazil A obsahuje obrázek, který potřebuji, NEBO délka e-mailu je delší než 10000 znaků". Později zjistíte, že se jedná o základní stavební kameny pro konstrukci logiky programu.


## Pole, null, undefined

<chapterId>7bf18183-5eae-53ed-83d2-b04982145d81</chapterId>


V této části se budeme zabývat dalšími třemi typy, které jsou v programech v jazyce JavaScript velmi časté:



- Pole**: posloupnosti hodnot
- undefined**: speciální hodnota, která znamená "nic nebylo přiřazeno"
- null**: další speciální hodnota, která znamená "záměrně prázdný"


### Pole a přístup k indexům


Pole** je typ, který může obsahovat více hodnot v seznamu.


Pole vytvoříte pomocí hranatých závorek `[]` a oddělením položek čárkami.


Zde je základní příklad:


```javascript
const numbers = [10, 2, 88]
console.log(numbers)
```


Tento tisk:


```
[ 10, 2, 88 ]
```


Do pole můžete ukládat cokoli, nejen čísla:


```javascript
const things = ["apple", 42, true]
console.log(things)
```


Tento tisk:


```
[ 'apple', 42, true ]
```


Pro přístup ke konkrétní položce v poli použijeme **index**. Index je pozice položky, počínaje **0**.


Takže v tomto poli:


```javascript
const colors = ["red", "green", "blue"]
```



- `colors[0]` je `"červená"`
- `colors[1]` je `"Green"`
- `colors[2]` je `"modrá"`


Zkusme to:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[0])
console.log(colors[1])
console.log(colors[2])
```


Vytiskne se:


```
red
green
blue
```


Konkrétnímu indexu pole můžete přiřadit hodnotu


```javascript
const colors = ["red", "green", "blue"]

colors[1] = "yellow"

console.log(colors)
```


Vytiskne se:


```
[ 'red', 'yellow', 'blue' ]
```


Jako index můžete použít libovolné přirozené číslo, dokonce i číslo uložené v proměnné


```javascript

const i = 1
const colors = ["red", "green", "blue"]
console.log(colors[i])
```


Vytiskne se:


```
green
```


Pokud se však pokusíte přistoupit k neexistujícímu indexu, zobrazí se `undefined`:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[3])
```


Tento tisk:


```
undefined
```


Co je to??


### `undefined`


Zvláštní hodnota `undefined` znamená "nebyla přiřazena žádná hodnota".


Pokud vytvoříte proměnnou, ale nedáte jí hodnotu, bude `undefined`:


```javascript
const name
console.log(name)
```


Tento tisk:


```
undefined
```


Protože jsme jménu `name` nic nepřiřadili, JavaScript jej ve výchozím nastavení nastaví na hodnotu `undefined`.


Jak již bylo řečeno, můžete také získat `undefined`, když přistupujete k neexistujícímu indexu pole:


```javascript
const fruits = ["banana", "apple"]
console.log(fruits[2]) // There is no index 2
```


Tento tisk:


```
undefined
```


### `null` a jak s ním zacházet


`null` je také speciální hodnota. Znamená "nic tu není a udělal jsem to schválně"


Na rozdíl od `undefined`, které je automatické, `null` nastavujete sami.


Například:


```javascript
const currentUser = null
console.log(currentUser)
```


Tento tisk:


```
null
```


Proč používat `null`? Možná očekáváte hodnotu později, ale ještě není připravena:


```javascript
let winner = null

// Later in the program:
winner = "Alice"

console.log(winner)
```


Tento tisk:


```
Alice
```


Proto se `null` hodí, když chcete například říct: "Později by tu mělo něco být, ale teď je to prázdné."


## Bloky a tok řízení

<chapterId>be985168-2636-5b0d-a48f-ac1bbfbff8a7</chapterId>


Dosud jsme většinou psali řádky kódu, které se spouštěly jeden po druhém.


Ale když kódujeme, můžeme kontrolovat pořadí jeho provádění.


Tomu se říká **control flow**.


Začněme pochopením bloků a rozsahu.


### Globální rozsah


Každá proměnná, kterou deklarujeme, existuje v **oblasti**, což znamená oblast kódu, kde je proměnná známa.


Pokud deklarujete proměnnou mimo jakýkoli blok, existuje v **globálním oboru**.


```javascript
const color = "blue"
console.log(color)
```


Tato proměnná `color` je v globálním oboru, takže k ní lze přistupovat odkudkoli v souboru.


Pokud přidáte další řádky:


```javascript
const color = "blue"
console.log(color)

const size = "large"
console.log(color)
console.log(size)
```


Jak `color`, tak `size` jsou globální proměnné. Jsou dostupné všude v souboru.


Co se ale děje uvnitř bloku?


### Bloky a místní rozsah


**blok** je část kódu obklopená kudrnatými závorkami `{}`.


Proměnné deklarované pomocí `let` nebo `const` uvnitř bloku existují **pouze** uvnitř tohoto bloku.


```javascript
{
const message = "inside block"
console.log(message)
}
```


Tento tisk:


```
inside block
```


Ale když zkusíte tohle:


```javascript
{
const message = "inside block"
}
console.log(message) // Error!
```


JavaScript zobrazí chybu, jako je:


```
ReferenceError: message is not defined
```


To proto, že `message` bylo deklarováno uvnitř bloku a mimo něj neexistuje.


To znamená, že pomocí bloků můžeme izolovat části kódu a mít jistotu, že "co se stane v bloku, zůstane v bloku" (něco jako Las Vegas).


Uspořádání kódu do bloků nám také umožňuje strukturovat provádění programu pomocí konstrukcí toku řízení, jako je `if`


### `if`, `else`


Někdy chceme spustit kód **pouze tehdy**, když je něco pravda. K tomu slouží příkaz `if`.


```javascript
const myAge = 20

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Tento tisk:


```
Am I an adult?
Yes I am!
```


Jak vidíte, kód porovnává `myAge` a `18`.

V tomto případě operátor `>=` vrátí `true`, takže se blok provede.

Pokud podmínka není `true`, blok se neprovede.


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Tento tisk:


```
Am I an adult?
```


Pro opačný případ můžete přidat blok `else`:


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
} else {
console.log("No, I am not.")
}
```


Tento tisk:


```
Am I an adult?
No, I am not.
```


Bloky `if` i `else` jsou stále bloky - takže proměnné deklarované uvnitř nich neexistují mimo ně.


Pokud chceme mít jistotu, že něco není pravda, co můžeme udělat?


Jak již bylo řečeno, JavaScript má operátor "not", který převrací logické hodnoty. Takže můžeme udělat


```javascript
const myAge = 17

const adult = myAge >= 18

console.log("Am I an adult?")

if (!adult) {
console.log("No, I am not.")
}
```

To se stále tiskne:


```
Am I an adult?
No, I am not.
```

Protože jsme použili operátor `!` k invertování proměnné `adult`.


`if (!adult) {...}` by se mělo číst jako "if not adult..."


Pomocí bloků, logických a porovnávacích operátorů můžeme strukturovat provádění programu definováním proměnných, které musí být `pravdivé` (nebo `nepravdivé`), aby se něco stalo.


### `while`, `break`, `continue`


Smyčka `while` opakuje kód *pokud je podmínka pravdivá*.


```javascript
let count = 0

while (count < 3) {
console.log("Count is", count)
count = count + 1
}
console.log("the loop is over!")
```


Tento tisk:


```
Count is 0
Count is 1
Count is 2
the loop is over!
```


Když `count` dosáhne hodnoty 3, smyčka se zastaví.


Smyčku můžete předčasně ukončit pomocí `break`:


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


Tento tisk:


```
0
1
2
```


Protože jakmile číslo nabývá hodnoty `3`, blok `if` se provede a cyklus se zastaví.


Zbytek smyčky můžete přeskočit pomocí `continue`:


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


Tento tisk:


```
1
2
4
5
```


Protože když bylo číslo `3`, `continue` způsobilo, že program přeskočil řádek, který vypisuje číslo.


### `pro ... z ...`


Pokud máte pole a chcete něco udělat s každou položkou v něm, můžete použít `for ... of .... {...}`.


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const fruit of fruits) {
console.log(fruit)
}
```


Tento tisk:


```
apple
banana
cherry
```

Blok se provede jednou pro každý prvek pole.


`fruit` je zde nová proměnná, která přebírá hodnotu každé položky v poli a pracuje s ní uvnitř bloku.


### `pro ... v ...`


Pomocí `for ... in` můžete procházet klíče (indexy) pole:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(index)
}
```


Tento tisk:


```
0
1
2
```


K získání hodnoty můžete použít také index:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(fruits[index])
}
```


Vytiskne se stejně jako `for ... of`:


```
apple
banana
cherry
```


V praxi byste pro pole měli raději používat `for ... of`, protože je to jednodušší a čistší.


### Ohraničené smyčky


Někdy chceme zacyklit určitý počet cyklů nebo obecně napsat kus kódu, který opakuje blok a zároveň něco sleduje.

K tomu slouží ohraničená smyčka `for`.

Omezená smyčka obvykle obsahuje tři podmínky oddělené středníkem `;`, jako například `(... ; ... ; ....)`.


```javascript
for (let i = 0; i < 3; i = i + 1) {
console.log(i)
}
```


Tento tisk:


```
0
1
2
```


Vysvětlíme si to:



- `let i = 0`: deklaruje proměnnou, která bude použita v bloku (v tomto případě je to čítač, který začíná na 0)
- `i < 3`: deklaruje podmínku, která musí být `pravdivá`, aby se blok provedl (v tomto případě je to "repeat while `i` is less than 3")
- `i = i + 1`: deklaruje kód, který se má spustit po každém provedení bloku (v tomto případě "zvýšit `i` o 1")


Jak vidíte, omezená smyčka nám umožňuje deklarovat složitější podmínky pro opakované provádění části kódu, ale většinou to není nutné.


### Blokové štítky


Pokud potřebujete napsat složitější tok řízení, JavaScript umožňuje pojmenovat blok pomocí **značky**, kterou lze použít pomocí `break` nebo `continue` pro určení místa, kam se má skočit zpět.


Příklad:


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


Tento tisk:


```
Inside outer block
Inside inner block
Done
```


Pomocí `break outer` jsme blok `outer` zcela ukončili.


Můžete také označit smyčky. Vezměme si tento příklad:


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

Byl to velmi nudný příklad, ale snad objasnil (občasnou) potřebu štítků.


## Zavedení funkcí

<chapterId>cc324715-09c2-5cf7-9e6f-47a6f16bc04d</chapterId>


Jak se vaše programy rozrůstají, často budete chtít **používat** části kódu opakovaně.


K tomu slouží **funkce**: umožňují seskupit určitý kód, pojmenovat ho a spustit, kdykoli se vám zachce.


### Deklarace funkce


Pro deklaraci funkce můžeme použít klíčové slovo `function`. Pak jí dáme jméno, dvojici závorek `()` s argumenty, které přijímá, a blok kódu `{}`, který se má vykonat. Začněme funkcí, která nepřijímá žádné argumenty:


```javascript
function sayHello () {console.log(`Hello!`) }
```


Tento kód **prohlásí** funkci, ale ještě ji **nespustí**.


### Volání funkcí


Chcete-li funkci spustit (neboli "zavolat"), napište její název následovaný závorkami:


```javascript
function sayHello () {console.log(`Hello!`) }
sayHello()
```


Tento tisk:


```
Hello!
```


Funkci můžete volat libovolně mnohokrát:


```javascript
function sayHello() {
console.log("Hello!")
}

sayHello()
sayHello()
```


Tento tisk:


```
Hello!
Hello!
```


Kód uvnitř funkce se spustí pouze tehdy, když ji zavoláte.


### Argumenty funkcí (vstupy do funkcí)


Někdy chcete, aby funkce fungovala s určitým vstupem. Toho můžete dosáhnout přidáním **argumentů** do závorek.


Například:


```javascript
function sayHelloTo (friend) {
console.log(`Hello ${friend}!`)
}
```


Nyní tato funkce přijímá **jeden argument** s názvem `přítel`.


Při volání funkce můžete předat hodnotu:


```javascript
sayHelloTo("Tommy")
```


Tento tisk:


```
Hello Tommy!
```


Funkci můžete zavolat znovu s jiným názvem:


```javascript
sayHelloTo("Sam")
```


Tento tisk:


```
Hello Sam!
```


Předaná hodnota nahradí uvnitř funkce proměnnou `friend`.


Můžete také použít více než jeden argument:


```javascript
function greetTwoPeople(person1, person2) {
console.log(`Hello ${person1} and ${person2}!`)
}

greetTwoPeople("Lina", "Marco")
```


Tento tisk:


```
Hello Lina and Marco!
```


### `return` (výstup z funkcí)


Funkce mohou také **vracet** hodnoty. To znamená, že odešlou hodnotu zpět do místa, kde byla funkce zavolána.


Zde je jednoduchý příklad:


```javascript
function getNumber() {
return 42
}

const result = getNumber()
console.log(result)
```


Tento tisk:


```
42
```


Funkce `getNumber()` vrátí `42` a my ji uložíme do `result` a vypíšeme.


Můžete také vrátit něco, co jste vypočítali:


```javascript
function add(a, b) {
return a + b
}

const result = add(2, 3)
console.log(result)
```


Tento tisk:


```
5
```


Jakmile je hodnota `vrácena`, funkce se ukončí. Cokoli po `return` v tomto bloku se již nestane.


```javascript
function saySomething() {

return "hi"

console.log("this never runs")

}

const message = saySomething()
console.log(message)
```


Toto se pouze vytiskne:


```
hi
```


protože se vrací pouze `"hi"`. Řádek `console.log("this never runs")` se přeskočí.


Funkce si můžete představit jako malé podprogramy. Každá funkce může přijmout nějaký vstup, pracovat s ním a vrátit vám nějaký výstup.


Co se stane, když se pokusíme použít návratovou hodnotu funkce, ale tato funkce nic nevrátila?


```javascript
function doesNothing () {}

const x = doesNothing()

console.log(x)
```

Vypíše se `undefined`. Návratová hodnota funkce, která nic nevrátila, je `undefined`.


## Objekty a třídy

<chapterId>26689f25-8212-5057-8c21-3a05eee0ac75</chapterId>


JavaScript je často označován za objektově orientovaný jazyk.


To znamená, že vám pomáhá organizovat kód seskupováním hodnot a funkcí do **objektů**.


### Co je to `objekt`?


Objekt může obsahovat data a funkce, které s těmito daty pracují. Když je funkce vložena do objektu, říkáme, že je to `metoda`.


Prvním objektem, který jsme viděli, byl objekt `console`. Je to objekt, který obsahuje několik metod pro vypisování na obrazovku a ladění našich programů.


Může dokonce tisknout sám; můžete


```javascript
console.log(console)
```


a vypíše seznam metod, které obsahuje. Například na mém počítači to vypsalo


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


Jak vidíte, má spoustu metod, které můžete použít k ladění!


Javascript nám nabízí různé způsoby vytváření nových objektů, které mohou dělat, cokoliv chceme.


### Vytvoření objektu


Nejjednodušší způsob, jak vytvořit objekt, je seskupit data a funkce pomocí **kudrnatých závorek** `{}`.


Tím se vytvoří tzv. **anonymní objekt**


```javascript
const cat = {
name: "Whiskers",
age: 3
}
```


Tím se vytvoří objekt a uloží se do proměnné `cat`.


Objekt má dvě **vlastnosti**:



- `name` s hodnotou `"Whiskers"`
- `age` s hodnotou `3`


Vytiskneme ji:


```javascript
console.log(cat)
```


Tento tisk:


```
{ name: 'Whiskers', age: 3 }
```


Vlastnosti můžete z objektu získat pomocí tečky, jako je `objectName.propertyName`:


```javascript
console.log(cat.name)  // prints "Whiskers"
console.log(cat.age)   // prints 3
```


Vlastnost můžete také **změnit**:


```javascript
cat.age = 4
console.log(cat.age)  // now it prints 4
```


Jak vidíte, i když je objekt definován jako `const`, můžete data, která obsahuje, upravovat.


V případě objektů vám `const` zabrání pouze v přepsání celého objektu:


```javascript
const cat = {
name: "Whiskers",
age: 3
}

cat.age = 5 // this works

cat = 5 // this throws an error, you're trying to reassign the whole object

```


Jak již bylo zmíněno, objekty mohou obsahovat také **funkce**, a pokud je funkce součástí objektu, nazýváme ji **metoda**.


Zde je příklad:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log("Meow!")
}
}
```


Tento objekt má:



- Vlastnost `name`
- Metoda `speak()`


Vyvolejme metodu:


```javascript
cat.speak()
```


Tiskne:


```
Meow!
```


Metody mohou používat data, která objekt obsahuje, prostřednictvím klíčového slova `this`.

`this` odkazuje na aktuální objekt. V tomto příkladu se použije k vypsání jména kočky:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log(`${this.name} says meow!`)
}
}

cat.speak()
```


Tento tisk:


```
Whiskers says meow!
```


Slovo `this` znamená "tento objekt"... v tomto případě objekt `cat`.



Tyto předměty se hodí, když chcete jen něco rychlého a jednoduchého. Pokud však potřebujete vytvořit **mnoho objektů** se stejnou strukturou, existuje lepší způsob, a tím jsou **třídy**.


### Třídy a konstruktory


Třída** je jako plán. Říká JavaScriptu, jak vytvořit určitý druh objektu.


Třídu definujete pomocí klíčového slova `class`, za kterým následuje název třídy a blok složených závorek `{}`.


```javascript
class Dog {}
```


Třídy obvykle začínají velkým písmenem.


Nový objekt třídy můžete vytvořit pomocí `new`:


```javascript
const hachiko = new Dog()
```


Zkuste objekt vytisknout:

```javascript
class Dog {}

const myDog = new Dog()

console.log(myDog)
```


Získáte


```
Dog {}
```


Jak vidíte, třída Dog je prázdná, takže i objekt `myDog` je prázdný.


Můžeme definovat, které vlastnosti mají objekty Dog obsahovat, přidáním `konstruktoru`.


Konstruktor je speciální funkce, která se spouští při vytváření (neboli "konstruování") nového objektu.


```javascript
class Dog {
constructor() { }
}
```


Chceme, aby každý pes měl své jméno, a proto přidáme do funkce parametr `jméno`:


```javascript
class Dog {
constructor(name) { }
}
```


A pak pomocí `this` deklarujeme, že `name` je `jméno` objektu `Dog`, který vytváříme


```javascript
class Dog {
constructor(name) {
this.name = name
}}
```


Zkusme ji nyní použít:


```javascript
class Dog {
constructor(name) {
this.name = name
}
}

const myDog = new Dog("hachiko")

console.log(myDog)
```


Vytiskne se něco jako:


```
Dog { name: 'hachiko' }
```


Jak vidíte, metoda `constructor` přebírá argumenty, které jste třídě předali při příkazu `new Dog()`, a používá je k vytvoření objektu.


Rozebereme si to:



- `class Dog` definuje třídu Dog.
- `constructor(name)` nastaví objekt při jeho vytváření.
- `this.name = name` uloží hodnotu do nového objektu.
- `new Dog("hachiko")` vytvoří nový objekt třídy s vlastností `name` nastavenou na `"hachiko"`.


Nyní přidáme do naší třídy metodu:


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


Tím se vytiskne


```javascript
hachiko says barf!
```


Pokud totéž provedeme pro dva různé případy psa



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


dostaneme


```
hachiko says barf!
bobby says barf!
```


metoda `speak()` používá vlastnost `name` psa `Dog`, na kterém je volána.


To je hlavní důvod existence tříd: umožňují definovat sadu metod, které pracují s daty, a následně vytvořit více objektů, které sdílejí stejný "tvar" dat.


Když zavoláme metodu na jednom z těchto objektů, bude pracovat s daty, která tento konkrétní objekt obsahuje.


### Změna tvaru objektu


Objekty v jazyce JavaScript jsou flexibilní. I po jejich vytvoření můžete přidávat nové vlastnosti nebo odstraňovat ty stávající.


Je to povoleno, ale měli byste to používat opatrně.


Začněme naší jednoduchou třídou `Pes`:


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


V tomto okamžiku má `myDog` pouze jednu vlastnost: `jméno`. Nové vlastnosti můžeme přidávat i po jeho vytvoření:


```javascript
myDog.age = 5

console.log(myDog.age) // prints 5
```


Můžeme také přidat novou metodu:


```javascript
myDog.jump = function () {
console.log(`${this.name} jumps!`)
}

myDog.jump() // Fido jumps!
```


Vlastnosti můžeme také odstranit pomocí klíčového slova `delete`.


```javascript
delete myDog.name

console.log(myDog.name) // prints 'undefined'
```


To funguje, ale je důležité vědět něco důležitého: JavaScriptové motory, jako je V8 (používaný v Node.js a v prohlížeči Chrome), pracují rychleji, pokud si objekty zachovávají stále stejné vlastnosti. Pokud vlastnosti přidáte nebo odstraníte až po vytvoření objektu, může to práci zpomalit.


V malých programech na tom příliš nezáleží. Ale ve větších projektech (například ve hrách) je lepší uvést všechny vlastnosti v konstruktoru hned na začátku, i když je hned nepoužijete. Udržuje to stabilní tvar objektu a pomáhá to rychlejšímu běhu kódu.


Například místo tohoto:


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


Mohli byste udělat


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


Obě verze fungují, ale druhá je z hlediska výkonu lepší. Motoru dopředu řeknete, jaké vlastnosti bude každý objekt mít, a on podle toho může optimalizovat.


JavaScript umožňuje libovolně měnit tvar objektů, ale při použití tříd je lepší plánovat tvar objektu předem.



### Dědičnost pomocí `extends` a `super()`


Někdy chcete vytvořit třídu, která je *téměř* stejná jako jiná třída, ale má několik funkcí navíc.


Namísto úpravy tvaru objektů (což, jak již bylo zmíněno, není optimální z hlediska výkonu) nebo nutnosti přepisovat novou třídu od začátku umožňuje JavaScript použít něco, čemu se říká **dědičnost**.


Dědičnost znamená, že jedna třída může **rozšířit** jinou. Nová třída získá všechny vlastnosti a metody té staré a vy můžete přidat další nebo změnit to, co potřebujete.


Řekněme, že máme základní třídu s názvem `Vehicle`:


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


Nyní chceme vytvořit třídu `Car`. Auto je druh dopravního prostředku, ale můžeme chtít, aby mělo nějaké další funkce nebo aby se po nastartování zobrazilo jiné hlášení. Místo abychom vše přepisovali, můžeme použít `rozšíření`:


```javascript
class Car extends Vehicle {
start() {
console.log(`${this.brand} car is ready to drive!`)
}
}
```


Třída `Car` nyní **dědí** vše od třídy `Vehicle`. Získává vlastnost `značka` a metodu `start()` jsme nahradili naší vlastní verzí.


![](assets/en/4.webp)


Vyzkoušejme si to:


```javascript
const myCar = new Car("Toyota")
myCar.start()
```


Tento tisk:


```
Toyota car is ready to drive!
```


Přestože `Car` nemá vlastní konstruktor, stále používá konstruktor z `Vehicle`. Pokud však chceme v `Car` napsat vlastní konstruktor, můžeme, jen musíme zahrnout volání konstruktoru jeho rodiče pomocí `super()`.


Zde je návod, jak na to:


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



Tento tisk:


```
Toyota Corolla is ready to drive!
```


Takže shrnutí



- `extends` znamená, že jedna třída vychází z jiné.
- `super()` se používá k volání konstruktoru rozšiřované třídy.
- Nová třída získá všechny vlastnosti a metody původní třídy.
- Metody (jako `start()`) můžete **přepsat** a přimět je, aby dělaly něco jiného.


To je užitečné, když máte několik podobných věcí (například osobní a nákladní auta a kola) a chcete, aby sdílely kód, ale přitom se chovaly samostatně.


### `instanceof`


Klíčové slovo `instanceof` kontroluje, zda byl objekt vytvořen z určité třídy.


Řekněme, že máme třídu `User`:


```javascript
class User {
constructor(username) {
this.username = username
}
}

const regularUser = new User("julia123")

console.log(regularUser instanceof User)
```


Tento tisk:


```
true
```


Potvrzení, že `regularUser` je `User`. To proto, že `regularUser` byl vytvořen pomocí třídy `User`.


Funguje také u **zděděných** tříd. Například zde je třída `Admin`, která rozšiřuje třídu `User`:


```javascript
class Admin extends User {}

const ourAdmin = new Admin("admin42")

console.log(ourAdmin instanceof Admin)   // true
console.log(ourAdmin instanceof User)    // true
```


Oba řádky vracejí hodnotu `true`. Je to proto, že `Admin` je podtřídou `Uživatele`, a proto `našAdmin` je jak `Admin`, tak `Uživatel`


# JavaScript pro mírně pokročilé

<partId>243f63ab-4f34-5c30-80cb-84ef46f6761d</partId>


## Zpracování chyb

<chapterId>d0206bc5-d386-5e7f-9917-5803f392448c</chapterId>


Při psaní složitějších programů v jazyce JavaScript se budete setkávat s **chybami**. Jedná se o neočekávané situace, kdy se něco pokazí. Třeba je proměnná `nedefinovaná`, ale vy se ji pokusíte použít, nebo některý kód obdrží špatný typ vstupu.


Pokud tyto chyby neošetříme správně, může náš program spadnout nebo se chovat nepředvídatelně. JavaScript poskytuje nástroje pro detekci a správu těchto chyb, abychom je mohli řešit šetrněji.


### Běžná chyba: přístup k hodnotě na `undefined`


Zde je běžná situace, která způsobuje chybu:


```javascript
const user = undefined
console.log(user.name)
```


Pokud tento kód spustíte, zobrazí se chyba, která vypadá takto:


```
TypeError: Cannot read properties of undefined (reading 'name')
```


To vám říká JavaScript: "Hej, pokusil ses získat vlastnost `name` z něčeho, co je `undefined`, a to nedává smysl." A jak vidíte, když dojde k takové chybě, program přestane běžet, pokud jste speciálně nenapsali kód, který ji zachytí a ošetří.


### `vyhodit` chybu


Někdy chcete v kódu ručně **vyvolat chybu**. V takovém případě použijete klíčové slovo `throw`.


```javascript
throw new Error("This is a custom error message")
```


Tím se program okamžitě zastaví a vytiskne:


```
Uncaught Error: This is a custom error message
```


K vynucení pravidel v programu můžete použít `throw`. Například:


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


Druhé volání způsobí chybu, protože dělení nulou není v tomto příkladu povoleno.


### Chytání chyb pomocí `try...catch`


Pokud nechcete, aby váš program při výskytu chyby spadl, můžete chybu zachytit pomocí bloku `try...catch`. To je užitečné, pokud chcete, aby váš program **pokračoval**, i když se něco nepodaří.


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log("Oops! Something went wrong.")
}
```


Výstup:


```
Oops! Something went wrong.
```


Funguje to takto:



- Kód uvnitř bloku `try` je vyzkoušen jako první.
- Pokud dojde k chybě, JavaScript **skočí do bloku `catch`** a přeskočí zbytek bloku `try`.
- Blok `catch` obdrží chybu, takže ji můžete vypsat, nebo ji zpracovat jiným způsobem, jako např


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log(`The message of the error was: "${error.message}"`)
}
```


Výstup:


```
The message of the error was: "Cannot read properties of undefined (reading 'name')"
```


### Blok `finally`


Můžete také přidat blok `finally`. To je kód, který se **vždy spustí**, ať už došlo k chybě, nebo ne.


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


Výstup:


```
Trying something risky...
Caught the error: Uh oh!
This will run no matter what.
```


## Vyhýbání se chybám

<chapterId>db12d9f6-5806-514c-998e-0ae24805104e</chapterId>


V této kapitole se dozvíte o některých nejčastějších nástrahách jazyka JavaScript a o tom, jak se jim vyhnout.


### `var` a Assignment bez deklarace


Ve starším kódu JavaScriptu se proměnné často deklarovaly pomocí klíčového slova `var`. Na rozdíl od `let` a `const`, o kterých jste se již dozvěděli, se `var` může chovat matoucím způsobem.


Například:


```javascript
{
var message = "hello"
}
console.log(message)
```


Dalo by se očekávat, že `message` bude existovat pouze uvnitř bloku, ale není tomu tak. `var` ignoruje rozsah bloku a zpřístupňuje proměnnou v celé funkci nebo souboru.


To může vést k neočekávanému chování, zejména u větších programů. Z tohoto důvodu by moderní kód v jazyce JavaScript měl vždy používat `let` nebo `const` místo `var`.


Ještě horší je, že JavaScript umožňuje přiřazovat hodnoty proměnným **bez toho, abyste je vůbec deklarovali**:


```javascript
function greet() {
user = "Alice"
}
greet()
console.log(user) // prints "Alice"
```


Tím se vytvoří nová globální proměnná `name` bez deklarace. Může se to stát v tichosti a vést k chybám, které je třeba dohledat, zejména pokud se jedná o pouhý překlep. Proměnné vždy deklarujte pomocí `let` nebo `const`.


### Slabý systém typů


JavaScript je slabě typovaný, což znamená, že v případě potřeby automaticky převádí hodnoty z jednoho typu na jiný. Tomuto postupu se říká typové vynucení, a přestože může být pohodlný, často vede k matoucím výsledkům.


Například:


```javascript
console.log("5" + 1)    // "51"
console.log("5" - 1)    // 4
console.log(true + 1)   // 2
console.log(null + 1)   // 1
```


V těchto příkladech se JavaScript snaží odhadnout, co jste měli na mysli. Někdy mění řetězce na čísla, booleany na čísla nebo řetězce na řetězce. Váš kód se tak může chovat neočekávaným způsobem.


Je důležité znát slabý systém typování jazyka JavaScript. Pokud se věci začnou chovat podivně, může to být způsobeno neočekávaným vynucením typu.


### `"use strict"`


Můžete povolit přísnější režim, který změní některé tiché chyby na skutečné chyby a zabrání vám používat některé nebezpečnější funkce jazyka.


Chcete-li tento přísnější režim povolit, přidejte na začátek souboru nebo funkce tento řádek:


```javascript
"use strict"
```


Například:


```javascript
"use strict"
name = "Alice" // ReferenceError: name is not defined
```


Bez striktního režimu by JavaScript v tichosti vytvořil globální proměnnou `jméno`. Se striktním režimem se z toho však stane skutečná chyba, což vám pomůže dříve odhalit chyby.


Striktní režim také vypíná některé zastaralé funkce JavaScriptu a usnadňuje optimalizaci a údržbu kódu.


## Hodnota vs. reference

<chapterId>bb898425-dc2f-5e5c-864b-0cb7a4a9aea9</chapterId>


JavaScript zachází s různými druhy hodnot různým způsobem.


Některé hodnoty se při přiřazení do proměnné **kopírují**.


Ostatní jsou **sdílené**, když je přiřadíte nové proměnné, takže pokud změníte jednu, změní se i druhá.


### Předávání podle hodnoty


Když je hodnota předána **podle hodnoty**, JavaScript vytvoří její **kopii**.


Pokud tedy změníte jeden z nich, nebude to mít vliv na druhý.


K tomu dochází u primitivních typů, jako jsou:



- čísla
- struny
- logické (`true` a `false`)
- `null`
- `undefined`


Podívejme se na příklad:


```javascript
let a = 5
let b = a

b = 10

console.log(a) // 5
console.log(b) // 10
```


Přiřadili jsme `b` hodnotu `a`, ale pak jsme `b` změnili na `10`.


Protože čísla jsou předávána hodnotou, JavaScript zkopíroval `5` do `b`. Hodnota `5` v `b` je nezávislá na původní hodnotě `5` v `a`, takže změna hodnoty `b` neměla na `a` žádný vliv.


Zkusíme to s řetězcem:


```javascript
let name1 = "Alice"
let name2 = name1

name2 = "Bob"

console.log(name1) // Alice
console.log(name2) // Bob
```


Změna `name2` opět neovlivnila `name1`, protože řetězce jsou také předávány hodnotou.


Totéž se stane, když předáte primitivum funkci: zkopíruje se. Funkce tedy nemůže měnit originál.


```javascript
function plusOne(x) {
x = x + 1
}

let number = 5

plusOne(number)

console.log(number) // 5
```


Přestože uvnitř funkce `1` bylo přidáno k `x`, původní `číslo` se nezměnilo.


To proto, že do funkce byla předána pouze **kopie**.


### Předání odkazem


Objekty se předávají **odkazem**.


To znamená, že namísto kopírování na ně JavaScript pouze předává **odkaz**, a pokud je změníte, změna se projeví i u všech ostatních proměnných, které na ně ukazují.


Například:


```javascript
const person1 = { name: "Alice" }
const person2 = person1

person2.name = "Bob"

console.log(person1.name) // Bob
console.log(person2.name) // Bob
```


Oba objekty `person1` a `person2` ukazují na stejný objekt v paměti.


Takže když jsme změnili `person2.name`, změnili jsme také `person1.name`, protože oba se dívají na stejnou věc.


Pole jsou objekty, zkusme tedy totéž s polem:


```javascript
const list1 = [1, 2, 3]
const list2 = list1

list2.push(4)

console.log(list1) // [1, 2, 3, 4]
console.log(list2) // [1, 2, 3, 4]
```


Přesunuli jsme `4` do `list2`, ale ovlivnilo to i `list1`, protože oba odkazují na stejné pole.


Podívejme se, co se stane, když funkci předáme objekt:


```javascript
function rename(user) {
user.name = "Charlie"
}

const person = { name: "Dana" }

rename(person)

console.log(person.name) // Charlie
```


Funkce změnila objekt! To proto, že obdržela **odkaz** na původní objekt `osoba`.


Nedostal kopii. Získal přístup k původnímu objektu a s ním i možnost jej upravovat.


Je důležité si tento rozdíl zapamatovat, protože jinak by se náš kód mohl chovat jinak, než očekáváme. Například můžeme napsat funkci s očekáváním, že nebude modifikovat argumenty, které dostává, a později zjistíme, že je ve skutečnosti modifikovala (protože šlo o objekty, takže byly předány referencí).


## Práce s funkcemi

<chapterId>e0d277a8-c642-5af7-9e53-dee27c811967</chapterId>


Již jste se naučili deklarovat a používat funkce v jazyce JavaScript. JavaScript vám však nabízí další nástroje, které vám umožní pracovat s funkcemi výkonnými způsoby.


### Funkce šipek


Šipkové funkce představují kratší způsob zápisu funkcí. Místo klíčového slova `funkce` použijeme šipku (`=>`).


Zde je normální funkce:


```javascript
function greet(name) {
return `Hello, ${name}!`
}
```


Verze se šipkou vypadá takto:


```javascript
const greet = (name) => {
return `Hello, ${name}!`
}
```


Pokud má funkce **pouze jeden řádek**, můžete závorky vynechat a `return`:


```javascript
const greet = (name) => `Hello, ${name}!`
```


Pokud má funkce **pouze jeden parametr**, můžete závorky kolem parametrů dokonce vynechat:


```javascript
const greet = name => `Hello, ${name}!`
```


Šipkové funkce jsou v moderním JavaScriptu velmi rozšířené, protože umožňují vyjádřit jednoduché funkce s podstatně menším množstvím šablon.


### Výchozí parametry


Někdy chcete, aby funkce měla **výchozí hodnotu**, pokud není předán žádný argument.


Můžete to udělat takto:


```javascript
function sayHello(name = "friend") {
console.log(`Hello, ${name}!`)
}

sayHello("Alice") // Hello, Alice!
sayHello()        // Hello, friend!
```


Pokud není předáno nic, použije se výchozí hodnota `"friend"`.


### Parametry rozptylu (`...`)


Co když vaše funkce přijímá flexibilní počet argumentů?


Pro jejich shromáždění do pole můžete použít operátor **rozprostření** (`...`):


```javascript
function logAll(...items) {
console.log(items)
}

logAll(1, 2, 3) // [1, 2, 3]
logAll("a", "b") // ["a", "b"]
```


Každou položku pak můžete zpracovat pomocí smyčky:


```javascript
function logEach(...items) {
for (const item of items) {
console.log(item)
}
}
```


Operátor spread je užitečný, pokud nevíte, kolik argumentů bude předáno.


### Funkce vyššího řádu


Funkce **vyššího řádu** je funkce, která:



- přijímá jako vstup jinou funkci
- a/nebo vrací funkci jako výstup


Zde je jednoduchý příklad:


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


Tento tisk:


```
Hello, friend!
Hello, friend!
```


Můžeme mu předat funkci šipky:


```javascript
runTwice(
() => console.log("Hello!")
)
```


Tento tisk:


```
Hello!
Hello!
```


Můžete také psát funkce, které **vracejí** jiné funkce:


```javascript
function makeGreeter(name) {
return () => console.log(`Hi, ${name}`)
}

const greetAlice = makeGreeter("Alice")
const greetBob = makeGreeter("Bob")

greetAlice() // Hi, Alice
greetBob() // Hi, Bob
```


Funkce `makeGreeter` je funkce, která vytváří další funkce. Přijme řetězec a vrátí novou funkci, která tento řetězec použije ve svém volání `console.log`.


Tento druh vzoru je velmi účinný, protože umožňuje ponechat ve funkcích "díry", které můžete později vyplnit potřebným chováním.


### `map()`, `filter()`, `reduce()`


JavaScript nabízí několik užitečných vestavěných metod pro práci s poli.


Tyto metody přijímají jako argumenty funkce, takže jsou také funkcemi vyššího řádu.


`map()` transformuje každou položku pole na něco jiného.


Příklad:


```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map(x => x * 2)

console.log(doubled) // [2, 4, 6]
```


Každé číslo se zdvojnásobí a výsledkem je nové pole.


`filter()` odstraní položky z pole, pokud nevyhoví testu.


Příklad:


```javascript
const numbers = [1, 2, 3, 4, 5]
const numbersGreaterThanTwo = numbers.filter(x => x > 2)

console.log(numbersGreaterThanTwo) // [3, 4, 5]
```


Zachovány jsou pouze ty položky pole, pro které podmínka `x > 2` vrátí hodnotu `true`.


`reduce()` slouží ke spojení všech položek pole do jediné hodnoty.


Příklad:


```javascript
const numbers = [1, 2, 3, 4]
const total = numbers.reduce((current, next) => current + next)

console.log(total) // 10
```


`reduce` prochází pole a v tomto příkladu aplikuje operátor `+` mezi `1` a `2`, pak mezi výsledné `3` a `3`, pak mezi výsledné `6` a `4`, dokud nezíská součet všech položek pole (což je 10).


Funkci `reduce()` můžete použít k mnoha účelům, jako jsou součty, průměry nebo postupné vytváření nových hodnot.


Tyto metody (`map`, `filter`, `reduce`) jsou výkonnými nástroji pro zpracování dat bez nutnosti psát ruční smyčky.


Můžete je dokonce kombinovat v řetězci operací, jako je tento:


```javascript
const numbers = [1, 2, 3, 4, 5]

const result = numbers
.map(n => n * 2)        // Double each entry, obtain [2, 4, 6, 8, 10]
.filter(n => n > 3) // Keep only the entries bigger than 3, so you get [4, 6, 8, 10]
.reduce((n1, n2) => n1 + n2) // Adds them: 4 + 6 + 8 + 10 = 28

console.log(result) // 28
```


## Práce s objekty

<chapterId>7842aada-f009-5518-b8e3-1104e166a035</chapterId>


V této kapitole se seznámíme s některými výkonnými a poněkud pokročilejšími nástroji pro práci s objekty v jazyce JavaScript.


### Soukromé nemovitosti


Někdy chceme skrýt vlastnost objektu, aby ji nebylo možné změnit nebo k ní přistupovat zvenčí. JavaScript nám nabízí způsob, jak to provést pomocí `#` před názvem vlastnosti. Tím vytvoříme **privátní** vlastnost, která je přístupná pouze zevnitř třídy.


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


Soukromé vlastnosti jsou užitečné, pokud chcete zabránit náhodným změnám.


### `static` Vlastnosti


Někdy chcete, aby vlastnost patřila samotné třídě, nikoli každému objektu, který z této třídy vytvoříte. K tomu slouží funkce `static`. Vlastnost `static` je obsažena ve třídě a všechny objekty této třídy se na ni budou odkazovat.


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


To je užitečné pro ukládání sdílených dat a metod, které se vztahují na celou skupinu objektů, nikoli pouze na jeden.


### `get` a `set`


V jazyce JavaScript umožňují funkce `get` a `set` vytvářet vlastnosti, které se tváří jako běžné proměnné, ale ve skutečnosti na pozadí spouštějí speciální kód.


Metoda `get`ter se spustí při pokusu o *čtení* vlastnosti. Deklaruje se zápisem `get` před metodu s názvem vlastnosti.


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


Přestože `fullName` není běžná vlastnost, můžeme ji jako takovou používat a v pozadí se spustí funkce `get`, která vytvoří celý název.


Metoda `set`ter se spustí, když vlastnosti *přiřadíte* hodnotu. Umožňuje řídit, co se stane, když se někdo pokusí tuto hodnotu změnit. Deklaruje se zápisem `set` před metodu s názvem vlastnosti.


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


Když provedeme `user.fullName = "John Smith"`, spustí se metoda `set` a aktualizují se hodnoty `firstName` a `lastName`.


I když se tedy zdá, že pouze nastavujeme jednoduchou proměnnou, ve skutečnosti spouštíme logiku, která aktualizuje další vlastnosti.


## Klíče a hodnoty

<chapterId>01a397b8-c12a-5c39-82b3-6d9ebbb72a29</chapterId>


Každá vlastnost v objektu JavaScript má **klíč** (nazývaný také název vlastnosti) a **hodnotu**.


Například:


```javascript
const user = {
name: "Alice",
age: 30
}
```


V tomto objektu jsou klíče `"name"` a `"age"` a jejich hodnoty "Alice" a `30`.


### Dynamický přístup


Někdy název vlastnosti předem neznáte... možná ji získáváte ze vstupu uživatele nebo ji čtete z proměnné. Přesto k ní můžete přistupovat pomocí **zápisu v závorkách**, například `myObject["keyName"]`.


```javascript
const user = {
name: "Alice",
age: 30
}

console.log(user["name"]) // Alice
```


Objektu jsme předali řetězec `name`, abychom získali odpovídající hodnotu.


Klíč můžeme uložit do proměnné a později pomocí ní přistupovat k odpovídající hodnotě, např


```javascript
const user = {
name: "Alice",
age: 30
}

const key = "name"

console.log(user[key]) // Alice
```


### Dynamický Assignment


Vlastnosti objektů můžete také vytvářet nebo aktualizovat pomocí proměnných jako klíčů.


```javascript
const settings = {}

const key = "theme"
settings[key] = "dark"

console.log(settings) // { theme: "dark" }
```


To je užitečné, když chcete objekt sestavit krok za krokem. Například:


```javascript
const user = {}

user["username"] = "bananaFan123"
user["email"] = "banana@fruit.com"

console.log(user)
// { username: "bananaFan123", email: "banana@fruit.com" }
```


Dynamický klíč můžete použít i *při vytváření* objektu pomocí hranatých závorek:


```javascript
const key = "language"
const config = {
[key]: "JavaScript"
}

console.log(config.language) // JavaScript
```


Tato vlastnost se nazývá **vypočtená vlastnost**. Hodnota uvnitř hranatých závorek se vyhodnotí a výsledek se použije jako klíč.


### `Symbol` Typ


Kromě řetězců umožňuje JavaScript používat jako klíč objektu také speciální typ `Symbol`.


Začněme jednoduchým příkladem:


```javascript
const id = Symbol("userID")

const user = {
name: "Bob",
[id]: 12345
}

console.log(user[id]) // 12345
```


V tomto příkladu je `id` symbol. Není to řetězec, ale stále funguje jako klíč. Pokud se pokusíte do konzoly zapsat `user`, uvidíte toto:


```javascript
console.log(user) // { name: 'Bob', [Symbol(userID)]: 12345 }
```


Další důležitá věc: každý vytvořený symbol je jedinečný, i když je vytvořen pomocí stejného řetězce.


```javascript
const a = Symbol("label")
const b = Symbol("label")

console.log(a === b) // false
```


Symboly umožňují definovat klávesy, které nebudou kolidovat s běžnými klávesami. Řekněme například, že máte objekt s vlastností `jméno`, ale tento objekt bude v budoucnu uživatel upravovat způsobem, který nemůžete předvídat, a tento uživatel může přidat také vlastnost `jméno`. Pokud byla původní vlastnost `jméno` definována řetězcem, byla by přepsána novou vlastností takto:


```javascript
const obj = {
name: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy' }
```


Pokud místo toho použijeme symbol:


```javascript
const name = Symbol("name")

const obj = {
[name]: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy', [Symbol(name)]: 'John' }
```


Jak vidíte, původní vlastnost `name` je tímto způsobem zachována. To může být užitečné v některých okrajových případech.


## Užitečné objekty

<chapterId>516e74c8-2a11-545a-a4d1-c2cabb91a273</chapterId>


JavaScript nám poskytuje několik užitečných vestavěných objektů, které nám pomáhají provádět například ladění a matematické operace.


### Další metody `konzole`


Již jste viděli soubor `console.log`, který vypisuje hodnoty na obrazovku.


Objekt `console` má k dispozici několik dalších užitečných metod, které vám mohou pomoci při ladění programů.


#### `console.warn`


Vytiskne žlutou zprávu (nebo v některých prostředích s varovnou ikonou):


```javascript
console.warn("This is just a warning.")
```


#### `console.error`


Vypíše červenou zprávu, jako by šlo o chybu:


```javascript
console.error("Something went wrong!")
```


#### `console.table`


Zobrazí pole nebo objekt jako tabulku:


```javascript
const users = [
{ name: "Alice", age: 25 },
{ name: "Bob", age: 30 }
]

console.table(users)
```


Vytiskne se tabulka, jako je:


```
┌─────────┬────────┬─────┐
│ (index) │  name  │ age │
├─────────┼────────┼─────┤
│    0    │ 'Alice'│  25 │
│    1    │ 'Bob'  │  30 │
└─────────┴────────┴─────┘
```


To může být užitečné pro vizualizaci strukturovaných dat.


#### `console.time` a `console.timeEnd`


Můžete změřit, jak dlouho něco trvá:


```javascript
console.time("timer")
for (let i = 0; i < 1000000; i++) {}
console.timeEnd("timer")
```


Vytiskne se něco jako:


```
timer: 2.379ms
```


Užitečné pro jednoduché testování výkonu.


### Objekt `Math`


JavaScript vám nabízí objekt `Math` s užitečnými metodami pro provádění výpočtů.


#### `Math.random()`


Vrátí náhodné číslo v rozsahu 0 (včetně) až 1 (výlučně):


```javascript
const r = Math.random()
console.log(r)
```


Příklad výstupu:


```
0.4387429859
```


#### `Math.floor()` a `Math.ceil()`



- `Math.floor(n)` zaokrouhluje **dolů** na nejbližší celé číslo
- `Math.ceil(n)` zaokrouhluje **nahoru** na nejbližší celé číslo


```javascript
console.log(Math.floor(4.9)) // 4
console.log(Math.ceil(4.1))  // 5
```


#### `Math.round()`


Zaokrouhluje na nejbližší celé číslo:


```javascript
console.log(Math.round(4.4)) // 4
console.log(Math.round(4.6)) // 5
```


#### `Math.max()` a `Math.min()`


Vrátí největší nebo nejmenší hodnotu ze seznamu čísel:


```javascript
console.log(Math.max(5, 9, 3)) // 9
console.log(Math.min(5, 9, 3)) // 3
```


#### `Math.pow()` a `Math.sqrt()`



- `Math.pow(a, b)` vám dá `a` na mocninu `b`
- `Math.sqrt(n)` vám dá druhou odmocninu z `n`


```javascript
console.log(Math.pow(2, 3))   // 8
console.log(Math.sqrt(16))    // 4
```


# Pokročilý JavaScript

<partId>72c30671-ca20-5617-92a5-d5ba7aa38c93</partId>


## Ostatní sbírky

<chapterId>a9a70c6d-a343-5a46-a383-e288bc2700e3</chapterId>


JavaScript nám poskytuje některé speciální typy kolekcí, které přesahují rámec běžných polí a objektů. Patří mezi ně `Map` a `Set`.


Pomáhají ukládat a spravovat skupiny hodnot, ale fungují jinak než dosud.


`Mapa` je kolekce dvojic klíč-hodnota**, stejně jako objekt. Má však několik důležitých rozdílů:



- Klíčem může být **jakákoli hodnota**, nejen řetězce.
- Pořadí položek je zachováno.
- Má zabudované metody, které usnadňují práci s ním.


Novou mapu vytvoříte takto:


```javascript
const myMap = new Map()
```


Tím se vytvoří prázdná mapa. Chcete-li do ní přidat položky, použijte `myMap.set(key, value)`:


```javascript
myMap.set("name", "Alice")
```


Tím se přidá klíč `"name"` s hodnotou `"Alice"`.


Jako klíč můžete použít také číslo:


```javascript
myMap.set(42, "The answer")
```


A dokonce i objekt jako klíč:


```javascript
const objKey = { id: 1 }
myMap.set(objKey, "Object as key")
```


To by nefungovalo u běžných objektů, které umožňují pouze řetězcové klíče.


Chcete-li **získat hodnotu**, použijte `myMap.get(key)`:


```javascript
console.log(myMap.get("name"))     // Alice
console.log(myMap.get(42))         // The answer
console.log(myMap.get(objKey))     // Object as key
```


Chcete-li **zkontrolovat, zda klíč existuje**, použijte `myMap.has(key)`:


```javascript
console.log(myMap.has("name")) // true
```


Chcete-li **odstranit klíč**, použijte `myMap.delete(key)`:


```javascript
myMap.delete("name")
```


Chcete-li **vymazat celou mapu**, použijte `myMap.clear()`:


```javascript
myMap.clear()
```


Mapy jsou skvělé pro správu velkých kolekcí hodnot, protože přístup k hodnotám na velké mapě je obvykle mnohem výkonnější než na velkém objektu.


### `Set`


`Sada` je kolekce **pouze hodnot** (bez klíčů), přičemž každá hodnota musí být **jedinečná**. To znamená:



- Nemůžete mít dvakrát stejnou hodnotu
- Hodnoty se ukládají v pořadí, v jakém je přidáváte


Sadu vytvoříte takto:


```javascript
const mySet = new Set()
```


Chcete-li **přidat hodnoty**, použijte `mySet.add(value)`:


```javascript
mySet.add(1)
mySet.add(2)
mySet.add(2) // duplicate, will be ignored
```


Přestože jsme se pokusili přidat `2` dvakrát, sada si ponechá pouze jednu kopii.


Chcete-li **zkontrolovat, zda je hodnota v sadě**, použijte příkaz `mySet.has(value)`:


```javascript
console.log(mySet.has(2)) // true
console.log(mySet.has(3)) // false
```


Chcete-li hodnotu **odstranit**, použijte příkaz `mySet.delete(value)`:


```javascript
mySet.delete(2)
```


Chcete-li vše **vymazat**, použijte `mySet.clear()`:


```javascript
mySet.clear()
```


Sada `Set` je užitečná, pokud chcete uchovávat kolekci jedinečných hodnot, aniž byste museli ručně kontrolovat duplicity:


```javascript
const numberArray = [1, 2, 2, 3, 4, 4, 4, 5]

const numberSet = new Set(numberArray)

console.log(numberSet) // Set(5) { 1, 2, 3, 4, 5 }
```


Funkce `Set` se vyhne duplicitám.


## Iterátory

<chapterId>61d24e5e-b7e4-541a-8322-778f61f26a72</chapterId>


Většina věcí v JavaScriptu, nad kterými lze pracovat ve smyčce (např. pole, řetězce, mapy, množiny), je **iterovatelná**: mohou poskytovat iterátory pro svůj obsah.


**iterátor** je v jazyce JavaScript speciální objekt, který vám pomůže procházet seznam položek **jednou po druhé**.


### iterátory `Object`


Na rozdíl od polí nebo map nejsou běžné objekty ** iterovatelné** pomocí `for...of`. Pokud zkusíte toto:


```javascript
const user = {
name: "Alice",
age: 30
}

for (const value of user) {
console.log(value)
}
```


Zobrazí se chyba:


```
TypeError: user is not iterable
```


To proto, že obyčejné objekty nemají vestavěný iterátor. Ale JavaScript vám dává jiné nástroje, jak nad nimi vytvořit smyčku.


#### `Object.keys()`


Pomocí `Object.keys(obj)` získáte pole **klíčů** objektu a pak nad ním vytvoříte smyčku:


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


Tento tisk:


```
name
age
```


#### `Object.values()`


Chcete-li procházet **hodnoty**, použijte `Object.values()`:


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


Tento tisk:


```
Alice
30
```


#### `Object.entries()`


Pokud chcete **zjistit klíč i hodnotu**, použijte `Object.entries()`:


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


Tento tisk:


```
name is Alice
age is 30
```


Přestože objekty nejsou přímo iterovatelné, tyto metody umožňují plný přístup k jejich obsahu způsobem, který dobře funguje s `for...of`.


Jak ale iterátory fungují?


### `Symbol.iterator`


Tajemstvím všech iterátorů je speciální **symbol** zvaný `Symbol.iterator`.


Tento symbol je vestavěný klíč, který říká JavaScriptu: "Tento objekt lze iterovat."


Když zavoláte `myIterable[Symbol.iterator]()`, JavaScript vám vrátí objekt **iterátoru** s metodou `.next()`.


Podívejme se, jak to vypadá:


```javascript
const colors = ["red", "green", "blue"]

const iterator = colors[Symbol.iterator]()

console.log(iterator.next()) // { value: 'red', done: false }
```


Každé volání `.next()` vám poskytne další hodnotu. Po dokončení se vrátí:


```javascript
{ value: undefined, done: true }
```


### `next()`


Metoda `.next()` slouží k získání další položky z posloupnosti.


Při každém volání `.next()` získáte objekt se dvěma klíči:



- `value`: aktuální položka
- `done`: boolean, který říká, zda iterace skončila


Uveďme si úplný příklad:


```javascript
const names = ["Lina", "Tom", "Eva"]      // declare an array
const iterator = names[Symbol.iterator]() // use the Symbol.iterator function to get an iterator for this array

let result = iterator.next()              // get the first element of the array

while (!result.done) {                    // repeat this loop until you reach the last element of the array, which is marked with { done: true }
console.log(result.value)               // print the value of each element
result = iterator.next()                // get the next element of the array
}
```


Tento tisk:


```
Lina
Tom
Eva
```


Takto funguje smyčka `for...of` pod kapotou: používá tento vzor s `.next()`.


Stejného výsledku dosáhnete, když


```javascript
const names = ["Lina", "Tom", "Eva"]

for (const result of names) {
console.log(result)
}
```


### Vytvoření iterovatelné třídy


Můžete si také definovat vlastní třídu **iterable** přidáním metody `[Symbol.iterator]()`.


Řekněme, že chceme třídu, která reprezentuje **rozsah čísel**, například od 1 do 5.


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


Tento tisk:


```
1
2
3
4
5
```


Děje se toto:



- Definovali jsme třídu `Range`
- Uvnitř třídy jsme implementovali `[Symbol.iterator]()`, takže JavaScript ví, jak iterovat
- Metoda `next()` vrátí každé číslo po jednom
- Po dosažení `konce` vrátí `{ done: true }`


Nyní naše třída `Range` funguje jako pole a můžeme ji použít v libovolném cyklu, který očekává iterovatelný soubor.


### Funkce generátoru a `yield`


Pro usnadnění vytváření iterátorů vám JavaScript nabízí **generátorové funkce**, které používají klíčové slovo `function*` (je to `function` s `*` na konci) a klíčové slovo `yield`.


Zkusme to:


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


Každý `yield` vrátí hodnotu a **pozastaví** funkci až do dalšího volání `.next()`.


Generátor můžete také zacyklit pomocí `for...of`:


```javascript
for (const num of numberGenerator()) {
console.log(num)
}
```


Tento tisk:


```
1
2
3
```


## Souběžnost pomocí zpětných volání

<chapterId>f3fc76ca-b3ef-54eb-a06e-501007002054</chapterId>


Až dosud byl náš kód **synchronní**: spouštěl se postupně po jednotlivých řádcích. Některé věci v reálném světě však vyžadují čas a my nechceme, aby se celý program při čekání zastavil.


V této kapitole představíme nový koncept: **měna**. Umožňuje nám manipulovat s pořadím, v jakém se věci provádějí. To je užitečné při práci s věcmi, jako jsou časovače, uživatelský vstup nebo čtení souborů z disku. JavaScript nabízí různé nástroje pro provádění souběhu.


### `setTimeout`


Funkce `setTimeout` umožňuje **spustit funkci později**, po uplynutí určitého času.


Příklad:


```javascript
console.log("Start")

setTimeout(
() => console.log("This runs after 2 seconds"),
2000
)

console.log("End")
```


Tento tisk:


```
Start
End
This runs after 2 seconds
```


Přestože se `setTimeout` objevuje uprostřed kódu, neblokuje zbytek. Místo toho naplánuje spuštění funkce na **pozdější dobu** a okamžitě pokračuje dál.


Hodnota `2000` znamená 2000 milisekund (což jsou 2 sekundy).

Zde je stručnější a pro začátečníky přívětivější přepis částí **Callbacks** a **Promise** s použitím manipulace s daty a jasných poznámek:


### Zpětná volání


Zpětná vazba** je pouze funkce, kterou předáme jiné funkci, aby mohla být později **vyvolána**.


Podívejme se na skutečný příklad s použitím čísel. Představme si, že máme seznam čísel a chceme každé z nich zdvojnásobit a na výsledné "zdvojené" pole aplikovat funkci (zpětné volání), ale chceme to provést s malým zpožděním, jako kdybychom čekali na něco pomalého (například načítání dat z internetu).


Zde je funkce, která to dělá pomocí **zpětné vazby**:


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


Zkusme tuto funkci použít:


```javascript
const input = [1, 2, 3]

doubleNumbers(input, function(result) {
console.log("Here is the doubled array:", result)
})
```


Po 1 sekundě se vytiskne:


```
Here is the doubled array: [ 2, 4, 6 ]
```


**Co se to tu děje?**


1. Předáváme `vstup` jako seznam čísel, která chceme zdvojnásobit.

2. Předáváme také **zpětnou funkci**, která programu říká, co má udělat *po* zdvojnásobení.

3. Uvnitř `doubleNumbers` simulujeme zpoždění pomocí `setTimeout` a poté provedeme zdvojnásobení.

4. Po dokončení zavoláme zpětné volání na výsledné "zdvojené" pole.


Tato technika funguje, ale představte si, že chcete provést **další kroky**, například odfiltrovat malá čísla a pak je sečíst. Museli byste takto **zahnízdit** více zpětných volání:


```javascript
doubleNumbers(input, function(doubled) {
filterBigNumbers(doubled, function(filtered) {
sumNumbers(filtered, function(total) {
console.log("Final result:", total)
})
})
})
```


Je to Hard na čtení a nepřehledné. Tomuto stylu se říká **peklo zpětných vazeb** a je to přesně to, k čemu byl vytvořen `Promise`.


## Současnost pomocí slibů

<chapterId>30fddaca-729f-5c8d-bf86-8dfc7b3c9800</chapterId>


`Promise` je vestavěný objekt jazyka JavaScript, který představuje hodnotu, která bude **připravena v budoucnu**.


Příslib můžeme vytvořit takto:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve("It worked!") // This means everything went OK
})
```


Část `new Promise()` vytvoří slib.


Uvnitř ní zadáme funkci se dvěma parametry:



- `resolve` je funkce, kterou voláme, když se vše podaří
- `reject` je funkce, kterou voláme, když se něco pokazí


Ve výše uvedeném příkladu to prostě okamžitě vyřešíme zprávou `"Funguje to!"`.


### `.then()`


Chceme-li něco udělat **po** splnění slibu, použijeme `.then()`:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve(100) // This means everything went OK
})

promise.then(result => {
console.log("The result is:", result)
})
```


Tento tisk:


```
The result is: 100
```


Hodnota, kterou jsme předali funkci `resolve()`, se odešle do funkce uvnitř `.then()` jako `result`.


Simulujme úlohu, která trvá 2 sekundy, pomocí `setTimeout`:


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


Počkáte 2 sekundy a poté vytisknete:


```
Done waiting!
```


### `odmítnout()`


Vytvořme slib, který **neplní**:


```javascript
const failingPromise = new Promise((resolve, reject) => {
reject("Something went wrong")
})
```


Pokud nyní použijeme `.then()`, nic se nestane, protože `.then()` zpracovává pouze úspěch.


Pro ošetření chyb se používá `.catch()`:


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


Vytiskne se pouze


```
Caught an error: Something went wrong
```


Hodnota předaná funkci `reject()` je odeslána funkci `.catch()`.


Vytvořme slib, který **někdy funguje a někdy selže** na základě nějaké podmínky.


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


Nyní můžeme zavolat tuto funkci a řešit oba případy:


```javascript
checkNumber(5)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Tento tisk:


```
Success: Positive number
```


A pokud to zkusíme s jiným číslem:


```javascript
checkNumber(-1)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Tiskne:


```
Failure: Not a positive number
```


### Řetězení operací pomocí `Promise`



Náš předchozí příklad můžeme přepsat pomocí `Promise` a bude vypadat mnohem čistěji.


Začněme tím, že napíšeme novou verzi naší funkce zdvojení, která však tentokrát vrací **slib**:


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


Nyní můžeme pomocí `.then()` říci JavaScriptu, co má s výsledkem udělat:


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


Tento tisk:


```
Doubled numbers: [ 2, 4, 6 ]
```


Zatím to funguje stejně jako verze se zpětným voláním, ale kód je nyní jednodušší na rozšíření a čtení.


Řekněme, že chceme přidat další kroky:


1. Nejprve zdvojnásobte všechna čísla

2. Pak odstraňte čísla menší než 4

3. Nakonec je všechny sečtěte dohromady


Pro každý krok můžeme napsat jednu funkci a všechny používat sliby:


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


Nyní je můžeme **spojit** takto:


```javascript
const input = [1, 2, 3]

doubleNumbers(input)
.then(filterBigNumbers)
.then(sumNumbers)
.then(
result => console.log("Final result after all steps:", result)
)
```


Tento tisk:


```
Final result after all steps: 10
```


Projděme si, co to dělá:


1. `doubleNumbers` zdvojnásobí pole: `[2, 4, 6]`

2. `filterBigNumbers` odstraní cokoli ≤ 3: `[4, 6]`

3. `sumNumbers` sečte zbývající čísla: `4 + 6 = 10`

4. Nakonec vytiskneme výsledek.


Každý krok `.then()` čeká na dokončení kroku, který mu předchází. Můžeme tedy vytvořit **řetězec akcí** bez vnořování. Díky tomu je kód čitelnější a snadněji se ladí.


## Souběh s `async`/`await`

<chapterId>6e93d29f-c8bf-5fd1-a9c9-4e794ee6cbd0</chapterId>


Viděli jsme, jak nám řetězce `Promise` pomáhají vyhnout se peklu zpětných volání, ale i tak mohou být trochu obtížně čitelné, pokud je v nich zahrnuto mnoho kroků.


K tomu slouží `async` a `await`. Umožňují nám psát asynchronní kód, **který vypadá jako synchronní**, což usnadňuje jeho pochopení.


### Co je `async`?


Pokud před funkci napíšete klíčové slovo `async`, JavaScript automaticky zabalí návratovou hodnotu funkce do slibu.


Podívejme se na základní příklad:


```javascript
async function greet() {
return "hello"
}
```


Pokud zavoláte tuto funkci:


```javascript
const result = greet()
console.log(result)
```


Uvidíte to:


```
Promise { 'hello' }
```


Přestože jste právě vrátili řetězec, JavaScript jej za vás převede na slib. Skutečnou hodnotu můžete získat pomocí `.then()` takto:


```javascript
greet().then( result => console.log(result) ) // prints "hello"
```


Nebo můžete použít `await`...


### Co je to "čekat"?


Klíčové slovo `await` říká JavaScriptu: "počkej, až bude tento slib dokončen, a pak mi dej výsledek."


Funkci `await` však můžete použít pouze **vnitř asynchronní funkce**.


Napišme příklad znovu pomocí `await`:


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


Nyní můžeme výsledek použít, jako by to byla běžná hodnota.


Pojďme teď udělat něco užitečnějšího.


### Simulace zpoždění pomocí `await`


Vytvoříme jednoduchou funkci `wait`, která jako argument přijme počet milisekund a po uplynutí tohoto počtu milisekund se prostě ukončí, aniž by dělala cokoli dalšího:


```javascript
function wait(ms) {
return new Promise(resolve => {
setTimeout(resolve, ms)
})
}
```


Zkusme ji použít:


```javascript
async function test() {
console.log("waiting 2 seconds...")
await wait(2000)
console.log("done waiting")
}

test()
```


Tento tisk:


```
waiting 2 seconds...
done waiting
```


Můžete si představit `čekat` jako "pozastavit se zde, dokud nebude slib splněn, a pak pokračovat"


To umožňuje psát kód způsobem **od shora dolů**, který se chová asynchronně, bez řetězení volání `.then()`.


### Čeká se na údaje


Zopakujme si náš předchozí příklad, kdy jsme zdvojili čísla, pak filtrovali a pak sčítali. Tentokrát však použijeme `async`/`await`.


Vytvoříme 3 funkce, které simulují čekání a vracejí příkazy Promises:


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


Nyní napíšeme funkci `async`, která je spojí:


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


Tento tisk:


```
Final result: 10
```


Je to mnohem přehlednější než řetězení `.then()` nebo vnořování zpětných volání.


Vypadá to jako běžný postupný program, ale přesto se chová asynchronně.


## Asynchronní iterátory

<chapterId>438b037d-9931-56d7-9052-7b4470f3c75b</chapterId>


Již jste se naučili o **iterátorech** a o tom, jak můžeme používat `for...of` k cyklování polí a dalších iterovatelných věcí.


Co když ale trvá, než se data, která chceme iterovat, objeví?


Někdy chceme procházet smyčkou věci, které přicházejí **asynchronně**, například zprávy z chatu, řádky ze souboru nebo čísla z pomalého zdroje.


K tomu nám JavaScript nabízí **asynchronní iterátory**.


### Asynchronní funkce generátoru


Nejjednodušší způsob, jak vytvořit asynchronní iterátor, je použít funkci **async generator**.


Píšeme to takto:


```javascript
async function* generateNumbers() {
yield 1
yield 2
yield 3
}
```


Vypadá stejně jako běžný generátor, ale před ním je `async`.


Nyní můžeme použít `for await...of` pro konzumaci hodnot:


```javascript
async function run() {
for await (const n of generateNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


Vytiskne se:


```
Got number: 1
Got number: 2
Got number: 3
Done!
```


Jaký je tedy rozdíl oproti běžnému generátoru?


Rozdíl je v tom, že nyní můžeme uvnitř generátoru použít `await`.


Znovu vytvoříme pomocníka pro zpoždění:


```javascript
function wait(ms) {
return new Promise(resolve => setTimeout(resolve, ms))
}
```


Nyní se pomalu** věnujme číslům:


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


Zkuste ji použít:


```javascript
async function run() {
for await (const n of generateSlowNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


### Proč používat asynchronní iterátory?


Asynchronní iterátory jsou užitečné, když:



- Všechny hodnoty nepřicházejí najednou.
- Chcete je řešit postupně, **jak přicházejí**.
- Pracujete se službou Promises a chcete čistě zacyklit.


Pokud například chcete načítat zprávy ze serveru chatu jednu po druhé nebo stahovat velký soubor po částech, asynchronní iterátory vám umožní napsat cyklus `for`, který pracuje se zpožděnými daty.


### `Symbol.asyncIterator`


Asynchronní iterátory můžeme používat i ve vlastních třídách.


Zde je příklad, který vytváří čísla se zpožděním:


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


Nyní můžeme používat `for await...of` stejně jako dříve:


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


To umožňuje vytvářet objekty, které lze iterovat asynchronně


## Syntaxe cukru Assignment

<chapterId>8b1ba7d8-ecfd-5470-b86e-73cb84ccc8b7</chapterId>


"Syntaktický cukr" znamená, že něco napíšete kratším nebo jednodušším způsobem, aniž byste změnili to, co to dělá. Je to jen hezčí způsob, jak říci stejnou věc.


JavaScript má některé vestavěné syntaktické cukry, které nám umožňují psát čistší a kratší deklarace. V této kapitole se podíváme na to, jak přiřazovat hodnoty na základě podmínky, aktualizovat proměnné pomocí matematiky, vytahovat hodnoty z polí nebo objektů a kopírovat je nebo kombinovat pomocí jednodušší syntaxe.


### Ternární operátor


V jazyce JavaScript můžete přiřadit hodnotu na základě podmínky pomocí operátoru **ternary**, což je zkrácený způsob zápisu `if...else`.


Místo toho, abyste dělali:


```javascript
let message

if (isMorning) {
message = "Good morning"
} else {
message = "Hello"
}
```


Můžete napsat:


```javascript
const message = isMorning ? "Good morning" : "Hello"
```


To znamená:



- Pokud je `isMorning` true, použijte `"Dobré ráno"`
- V opačném případě použijte `"Hello"`


Obecný tvar je:


```javascript
condition ? valueIfTrue : valueIfFalse
```


Můžete jej použít i uvnitř jiných výrazů:


```javascript
console.log(isSunny ? "Go outside" : "Stay in")
```


Jen se ujistěte, že ji používáte pro **jednoduchá** rozhodnutí. Pokud je logika složitá, zůstaňte u `if...else`.


### Alternativní operátoři Assignment


JavaScript má operátory **zkratek** pro provádění přiřazení v kombinaci s operacemi.


Podívejme se na běžný způsob:


```javascript
let counter = 1
counter = counter + 1
```


To lze zkrátit na:


```javascript
let counter = 1
counter += 1 // same as counter = counter + 1
```


Zde jsou ty nejčastější:


| Operator | Meaning             |
| -------- | ------------------- |
| `+=`     | add and assign      |
| `-=`     | subtract and assign |
| `*=`     | multiply and assign |
| `/=`     | divide and assign   |

Příklady:


```javascript
let score = 10
score += 5  // now score is 15
score *= 2  // now score is 30
score -= 10 // now score is 20
```


Ty jsou užitečné, když chcete aktualizovat proměnnou pomocí její vlastní hodnoty.


### Destrukturalizace


**Destrukturování** umožňuje snadno vyjmout hodnoty z polí nebo objektů a uložit je do proměnných.


#### Pole


Předpokládejme, že máte:


```javascript
const colors = ["red", "green", "blue"]
```


Místo toho, abyste dělali:


```javascript
const first = colors[0]
const second = colors[1]
```


Můžete udělat:


```javascript
const [first, second] = colors
```


Tímto se přiřazuje:



- `first` na `"red"`
- `druhá` na `"Green"`


Hodnoty můžete také vynechat:


```javascript
const [,, third] = colors
console.log(third) // blue
```


#### Objekty


Hodnoty můžete získávat i z objektů:


```javascript
const user = { name: "Alice", age: 30 }

const { name, age } = user
console.log(name) // Alice
console.log(age)  // 30
```


Pokud má vlastnost jiný název než požadovaná proměnná, můžete ji přejmenovat:


```javascript
const { name: username } = user
console.log(username) // Alice
```


Destrukturování zpřehledňuje kód při práci s objekty a poli.


### Syntaxe spreadu


Syntaxe **rozbalování** používá `...` k rozbalování nebo kopírování hodnot.


#### Pole


Pole můžete kopírovat nebo slučovat:


```javascript
const a = [1, 2]
const b = [3, 4]

const both = [...a, ...b]
console.log(both) // [1, 2, 3, 4]
```


Pole můžete také klonovat:


```javascript
const original = [10, 20, 30]
const clone = [...original]
```


#### Objekty


Stejně můžete postupovat i u objektů:


```javascript
const a = { x: 1 }
const b = { y: 2 }

const merged = { ...a, ...b }
console.log(merged) // { x: 1, y: 2 }
```


Hodnoty můžete také přepsat:


```javascript
const user = { name: "Alice", age: 30 }
const updated = { ...user, age: 31 }

console.log(updated) // { name: "Alice", age: 31 }
```


To je velmi užitečné při aktualizaci objektů beze změny původního stavu.


# NodeJS

<partId>42fe4d49-dace-5135-bb9e-b9d75034fb2a</partId>


## Jak jsme se dostali k uzlu

<chapterId>0da1d60c-06c9-54e6-a181-ae7dabf6e3b8</chapterId>


V této kapitole se dozvíme něco málo z historických souvislostí o JavaScriptu a NodeJS.


Historický kontext je v oblasti softwaru velmi důležitý, protože často používáme nástroje, které vytvořili jiní lidé, a jsme proto ovlivněni rozhodnutími, která v minulosti učinili.


Pochopení důvodů těchto rozhodnutí a toho, jak se nástroje, které používáme, staly takovými, jaké jsou, nám pomůže cítit se méně zmateně v tom, co děláme.


### Původ jazyka JavaScript


JavaScript vznikl jako jednoduchý jazyk určený k vytváření interaktivních webových stránek.


V 90. letech 20. století přidaly webové prohlížeče jako Netscape Navigator JavaScript, takže vývojáři mohli psát kód spouštěný přímo v prohlížeči.


Původní myšlenka byla, že základním jazykem pro tvorbu webových stránek bude Java (s tzv. "Java applety") a JavaScript bude určen pouze pro drobné věci.


Základní návrh vytvořil Brendan Eich, který byl v té době zaměstnancem společnosti Netscape, za méně než dva týdny.


Většina lidí však dávala přednost JavaScriptu před Javou a také applety v Javě měly v té době určité problémy s bezpečností, takže nakonec byla Java jako možnost vypuštěna a JavaScript se stal de facto standardem pro vývoj webových stránek.


### Motor V8


JavaScript je interpretovaný jazyk, na rozdíl od kompilovaných jazyků, jako je C.


Kód napsaný v kompilovaném jazyce se změní na binární kód a ten se přenese přímo do procesoru počítače.


![](assets/en/6.webp)


Interpredové jazyky jsou naopak uživatelsky přívětivější a mají blíže k tomu, jak myslí lidé ("high level"), než jak pracují stroje ("low level"); proto je pro jejich kód obvykle vytvořen virtuální stroj.


Virtuální stroj je speciální program, který se nachází mezi kódem, který napíšete, a procesorem a provádí váš kód (protože procesor mu nerozumí).


To vám umožňuje programovat, aniž byste věděli příliš mnoho o základním stroji, ale má to také své náklady z hlediska výkonu, protože na počítači neběží jen váš program, ale program (virtuální stroj), na kterém běží váš program.


Jak se webové aplikace stávaly stále složitějšími, vznikl požadavek na zlepšení výkonu jazyka JavaScript. Interpretem jazyka JavaScript v prohlížeči Google Chrome je engine V8. Byl vyvinut ve společnosti Google a vydán v roce 2008.


Zatímco starší enginy JavaScriptu byly většinou tradiční virtuální stroje, engine V8 je kompilátor JIT (just-in-time).


Kód JavaScriptu se předá enginu V8 a ten se pokusí zkompilovat jeho části jako nativní binární soubory za běhu. To umožňuje získat zkušenost vysokoúrovňového jazyka s výkonem, který je o něco bližší nízkoúrovňovým jazykům. Díky tomu se JavaScript stal nejrychlejším vysokoúrovňovým jazykem na světě, tak trochu "to nejlepší z obou světů".


### Běhové prostředí NodeJS


JavaScript se sice snadno používá a poměrně rychle vykonává, ale po vydání V8 měl stále jedno velké omezení: mohl běžet pouze v prohlížeči.


Proč je to problém?


Vzhledem k tomu, že prohlížeče spouštějí kód získaný z milionů různých zdrojů na internetu, mohou se snadno stát škodlivým softwarem, a proto jsou "sandboxovány" od zbytku operačního systému.


![](assets/en/7.webp)


JavaScript neuměl přistupovat k souborovému systému a dalším místním zdrojům v počítači (alespoň ne tak snadno jako jiné jazyky), takže to představovalo významné omezení pro to, jaké aplikace jste s ním mohli vytvářet.


V roce 2009 vydal Ryan Dahl knihu NodeJS, což je runtime, který umožňuje používat engine V8 mimo prohlížeč, přímo v nativním operačním systému počítače. Přidává také mnoho funkcí, které jsou užitečné pro psaní programů na straně serveru a příkazového řádku. Pomocí NodeJS můžete například vytvořit webový server, číst a zapisovat soubory nebo vytvářet nástroje pro automatizaci úloh.


![](assets/en/8.webp)


V tomto kurzu jsme se zatím zabývali funkcemi JavaScriptu, které jsou přítomny jak v prohlížeči, tak v NodeJS. Tyto funkce nám umožnily definovat data a manipulovat s nimi abstraktním způsobem. V několika příštích lekcích prozkoumáme funkce, které jsou specifické pro NodeJS a umožňují nám komunikovat s operačním systémem.


## Argumenty příkazového řádku

<chapterId>960d20f3-c424-5d51-a041-ef17d2e94b6d</chapterId>


NodeJS nám mimo jiné umožňuje vytvářet CLI (Command Line Interfaces).


K tomu potřebujeme způsob, jak přijímat argumenty příkazového řádku, což se v Node děje pomocí vestavěného objektu `process`.


### `process`


NodeJS poskytuje speciální objekt `process`, který představuje aktuálně běžící program.


Můžete jej použít ke kontrole prostředí, aktuálního pracovního adresáře a v případě potřeby i k ukončení programu.


Například:


```javascript
console.log(process.platform)
```


Vypíše platformu operačního systému, například `win32`, `linux` nebo `darwin` (Mac).


### `process.argv`


Při spouštění programu NodeJS z terminálu můžete za název skriptu zadat další slova (argumenty). Ty jsou uloženy v souboru `process.argv`.


Pokud například spustíte tento příkaz:


```
node my_script.js alpha beta
```


Argumenty můžete vypsat takto:


```javascript
console.log(process.argv)
```


Výstup může vypadat takto:


```
[ '/path/to/node', '/path/to/my_script.js', 'alpha', 'beta' ]
```


První dvě položky jsou vždy cesta k uzlu a cesta ke skriptu. Jakákoli další slova, která jste skriptu předali, následují za nimi.


Pole `process.argv` lze rozřezat jako jakékoli jiné pole pomocí metody `.slice()`, takže pro získání pouze těch argumentů, které byly předány, můžete provést následující příkaz


```javascript
const args = process.argv.slice(2)

console.log(args)
```


Přístup k argumentům, které uživatel předává, je pro vývoj aplikací pro příkazový řádek zásadní.


## Moduly

<chapterId>4e1651a5-65fd-50bc-b22a-40313d5659ca</chapterId>


Běhové prostředí JavaScriptu, jako je NodeJS, obvykle považuje každý soubor JavaScriptu za samostatný modul.


Představte si modul jako krabici. Modul má svůj vlastní soukromý prostor, takže proměnné a funkce, které v něm deklarujete, nezasahují do kódu v jiných modulech. V podstatě má každý modul svůj vlastní obor.


Modul může exportovat část svého obsahu a zpřístupnit jej ostatním modulům a může importovat obsah, který exportovaly jiné moduly. JavaScript umožňuje exportovat a importovat obsah mezi moduly, propojovat různé soubory.


Program v jazyce JavaScript se často skládá z několika modulů, které jsou vzájemně propojeny.


Proč používat moduly? Rozdělením kódu do modulů můžete svůj program uspořádat do menších, přehlednějších a opakovaně použitelných částí. Každý modul se může zaměřit pouze na jeden typ úlohy, například na zpracování matematických výpočtů, práci se soubory nebo formátování textu.


### Moduly CommonJS


V NodeJS se nejběžnější systém pro správu modulů nazývá **CommonJS**.


V tomto systému můžete sdílet (exportovat) kód z modulu pomocí `module.exports` a načíst (importovat) jej do jiného souboru pomocí `require()`.


Chcete-li něco zpřístupnit mimo modul, přiřadíte to do souboru `module.exports`:


```javascript
const greeting = "Hello!"

module.exports = greeting
```


V tomto případě modul exportuje řetězec `"Hello!"`.


Chcete-li použít exportovaný kód z jiného souboru, použijte funkci `require()` s cestou k tomuto souboru:


```javascript
const greeting = require("./greeting.js")

console.log(greeting)
```


Tento tisk:


```
Hello!
```


Více věcí můžete exportovat tak, že je spojíte do anonymního objektu, např


```javascript
const greeting1 = "hello"

const greeting2 = "hi"

module.exports = {
greeting1, greeting2
}
```


CommonJS byl systém modulů, který byl původně převzat do NodeJS. Později byly přidány také moduly ES.


### Moduly ES


NodeJS podporuje také další typ modulů, které se nazývají **ES Modules** a jsou oblíbené při vývoji webových stránek. Používají klíčová slova `export` a `import`.


Moduly ES byly vyvinuty pro prohlížeč a teprve později přidány do Node. Pokud je chcete používat, budete možná muset jako příponu souboru použít `.mjs` místo `.js`, v závislosti na verzi Node, kterou používáte.


V jednom souboru nazvaném `greeting.mjs` píšeme


```javascript
export const greeting = "Hello!"
```

Jak vidíte, exportujeme konstantu přímo tam, kde je definována


V dalším souboru nazvaném `index.mjs` jej importujeme:


```javascript
import { greeting } from "./greeting.mjs"

console.log(greeting)
```


V různých částech souboru můžete exportovat různé deklarace, např


```javascript
export const num = 10

export function double (x) {
return x*2
}
```


### Standardní knihovna NodeJS


NodeJS obsahuje také mnoho vestavěných modulů. Jedná se o hotové moduly poskytované NodeJS, které pomáhají s běžnými úlohami, jako je čtení souborů, práce s operačním systémem nebo připojení k síti.


Například modul `os` poskytuje informace o operačním systému:


```javascript
const os = require("os")

console.log(os.platform())
```


Tyto vestavěné moduly nemusíte instalovat, jsou součástí NodeJS. Tvoří "standardní knihovnu" běhového prostředí a většina aplikací Node je používá k činnostem, jako je čtení souborů nebo komunikace přes internet.


V dalších kapitolách si ukážeme několik užitečných příkladů jejich použití.


## Modul `fs`

<chapterId>911e953a-35ae-5ee7-bd74-372501c32e81</chapterId>


Modul `fs` (zkratka pro **souborový systém**) je součástí standardní knihovny NodeJS. Umožňuje pracovat se soubory a adresáři v počítači: můžete soubory číst, zapisovat, mazat, přejmenovávat a další.


Chcete-li ji použít, musíte ji nejprve importovat na začátek souboru:


```javascript
const fs = require("fs")
```


### Rozhraní API pro synchronizaci


Nejjednodušší způsob použití `fs` je pomocí jeho metod **sync**.


Tyto metody blokují program, dokud nejsou dokončeny (takže další řádek kódu se nespustí, dokud není operace dokončena).


Zde je příklad synchronního čtení souboru:


```javascript
const fs = require("fs")

const data = fs.readFileSync("example.txt", "utf8")

console.log(data)
```


Pokud je ve stejném adresáři jako váš skript soubor s názvem `example.txt`, vypíše se jeho obsah.


Do souboru můžete zapisovat také synchronně:


```javascript
const fs = require("fs")

fs.writeFileSync("output.txt", "Hello from Node!")

console.log("File written!")
```


Tím se vytvoří (nebo přepíše) soubor s názvem `output.txt` s textem.


Zde jsou uvedeny některé běžné operace, které lze pomocí tohoto rozhraní API provádět:


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


Rozhraní API Sync je jednoduché a vhodné pro malé skripty, ale protože blokuje program, dokud není dokončen, může zpomalit práci, pokud pracujete s velkými soubory nebo serverem.


### Asynchronní zpětné volání API


API **callback** je neblokující: umožňuje NodeJS pokračovat v jiných činnostech, zatímco probíhá operace se souborem.


Místo přímého vrácení výsledku přebírá funkci (**callback**), která se zavolá po dokončení operace.


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


Děje se toto:



- `fs.readFile` začne číst soubor `example.txt`.
- NodeJS nečeká, ale přejde k provádění dalšího kódu, který jste případně napsali.
- Po dokončení čtení souboru se spustí zpětné volání:



  - Pokud došlo k chybě, `err` obsahuje chybu.
  - V opačném případě obsahuje `data` obsah.


Zde je uveden postup zápisu do souboru:


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


Stejná myšlenka: program se během zápisu souboru nezastaví.


Některé příklady činností, které lze s tímto rozhraním API provádět:


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


Rozhraní API zpětných volání je lepší pro servery a velké úlohy, protože neblokuje program, ale vnořené zpětné volání může být nepřehledné, pokud zřetězíte mnoho operací. Proto bylo přidáno asynchronní API založené na slibech.


### Asynchronní rozhraní API Promise


Rozhraní API založené na slibech je moderní a skvěle funguje s `.then()` a `async/await`. Je k dispozici jako `fs.promises`.


Je třeba importovat vlastnost `promises`:


```javascript
const fs = require("fs").promises
```


Použití `.then()`:


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


Nebo ještě lépe pomocí `async/await`:


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


Zápis do souboru:


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


Obvyklý seznam příkladů pro rozhraní API:


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


Při psaní kódu budete často potřebovat použít kód napsaný jinými lidmi; například knihovny, které vám pomohou pracovat s daty, barvami, servery nebo téměř čímkoli jiným.


Místo ručního stahování a kopírování souborů můžete použít **správce balíčků**.


Správce balíčků je nástroj, který:



- balíčky ke stažení
- sleduje, které balíčky váš projekt potřebuje
- zajistí, aby všichni členové týmu měli stejné verze balíčků


### Co je NPM


Ve světě NodeJS je nejpopulárnějším správcem balíčků **NPM**, což je zkratka pro *Node Package Manager*.


NPM získáte automaticky při instalaci NodeJS.


Zda máte NPM, můžete zkontrolovat spuštěním tohoto příkazu v terminálu:


```
npm -v
```


Vypíše se verze NPM, kterou máte, například:


```
10.2.1
```


### Vytvoření balíčku


V NodeJS je **balíček** pouze adresář se souborem `package.json`.


Pojďme si ho vytvořit krok za krokem.


1. Vytvořte novou složku pro svůj projekt:


```
mkdir my_project
cd my_project
```


2. Spusťte tento příkaz:


```
npm init
```


Spustí se interaktivní nastavení, které vám položí otázky, jako je název projektu, verze, popis atd.


Pokud nechcete odpovídat na všechny otázky a pouze přijmout výchozí nastavení, můžete použít:


```
npm init -y
```


Po jeho spuštění se ve složce objeví nový soubor s názvem:


```
package.json
```


### `package.json`


Soubor `package.json` je pouze soubor JSON, který uchovává metadata o vašem projektu.


Zde je příklad:


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


Několik důležitých oblastí:



- `name`: název vašeho balíčku
- `version`: aktuální verze
- `main`: vstupní soubor (jako `index.js`)
- `scripts`: příkazy, které můžete spouštět (například `npm start`)
- `dependencies`: seznam všech balíčků, na kterých váš projekt závisí


### Instalace balíčku


Řekněme, že chcete použít určitý balíček s názvem `picocolors` pro přidání barev na výstup terminálu.


Můžete jej nainstalovat spuštěním:


```
npm install picocolors
```


Nyní jej můžete použít ve svém projektu. Vytvořte soubor `index.js` s příkazem


```javascript
const pico = require('picocolors')

console.log(
pico.green("This text is green!")
)
```


a zkuste jej spustit. Terminál by měl vypsat barevnou verzi textu.


Co udělal NPM ?



- Stáhl balíček a uložil jej do podsložky s názvem `node_modules/`
- přidalo to položku `závislosti` do vašeho souboru `package.json`
- aktualizoval soubor `package-lock.json`


Co je to `package-lock.json` ?


### `package-lock.json`


Tento soubor je automaticky vytvořen pomocí NPM.


Možná si říkáte, že když už máme `package.json`, proč potřebujeme další soubor?

Zde je důvod:



- `package.json` pouze říká, jakou verzi **rozsahu** balíčku váš projekt potřebuje.

Příklad:


```json
"dependencies": {
"picocolors": "^1.1.0"
}
```


`^1.1.0` znamená "jakákoli verze, která je kompatibilní s verzí 1.1.x", takže je flexibilní.



- `package-lock.json` **zamrazuje** přesné verze všech balíčků a jejich dílčích závislostí, takže každý, kdo si nainstaluje váš projekt, získá přesně stejné funkční nastavení.


Proč je to důležité?


Pokud pracujete v týmu, nasazujete svůj projekt na server nebo se k němu v budoucnu vrátíte, chcete mít jistotu, že bude fungovat stále stejně.

Pokud byly balíčky aktualizovány a vy je znovu nainstalujete bez souboru zámku, můžete získat mírně odlišnou verzi, která se bude chovat jinak.


Pokud budete mít v projektu soubor `package-lock.json`, NPM vždy nainstaluje přesně ty verze, které jsou v něm uvedeny, a zajistí, že všichni budou mít stejné prostředí.


`package-lock.json` uzamkne vše na konkrétní verzi, aby byl projekt lépe reprodukovatelný na jiných počítačích.


Pokud však váš balíček potřebuje používat mnoho lidí, můžete se raději rozhodnout jej neodevzdávat, aby NPM našel pouze soubor `package.json` a mohl automaticky instalovat nejnovější verze, které jsou v tomto souboru povoleny.


Těmito záležitostmi byste se však měli zabývat později, až začnete publikovat svůj vlastní kód. Prozatím jsme vám představili základy NPM jen proto, abyste mohli ve svých projektech najít a používat knihovny publikované jinými vývojáři.



## Síťování v NodeJS

<chapterId>f2cabd8b-754b-5c97-8d6a-8412a9a184c7</chapterId>


NodeJS se často používá jako jazyk pro backend: můžete svůj skript proměnit v server a také jej použít k zadávání požadavků jiným serverům.


V této kapitole si představíme některé základní síťové funkce, které vám to umožní.


### `fetch()`


Pokud chcete, aby váš program stahoval data z webové stránky nebo rozhraní API, musíte provést požadavek **HTTP**.


V moderních verzích NodeJS můžete použít vestavěnou funkci `fetch()`.


Zde je příklad požadavku GET na rozhraní API:


```javascript
const response = await fetch("https://jsonplaceholder.typicode.com/posts/1")
const data = await response.text()

console.log(data)
```


Po spuštění se zobrazí něco jako:


```
{
"userId": 1,
"id": 1,
"title": "...",
"body": "..."
}
```


Děje se toto:


1. `fetch()` přijme adresu URL a provede požadavek.

2. Vrací objekt **Promise**, který je přeložen na objekt `Response`.

3. `response.text()` načte tělo odpovědi jako řetězec.


Řetězec, který se vám vrátí, je ve skutečnosti JSON. Co to je?


### JSON


Při práci s webovými rozhraními API se data často odesílají a přijímají ve formátu **JSON**, což je zkratka pro JavaScript Object Notation.


JSON je pouze textový formát, který vypadá podobně jako objekty JavaScriptu. Například:


```json
{
"name": "Alice",
"age": 30,
"likes": ["apples", "bananas"]
}
```


Objekt `JSON` je vestavěný nástroj v jazyce JavaScript, který lze použít pro práci s tímto datovým formátem.


Objekt JavaScriptu můžete převést na řetězec JSON pomocí funkce `JSON.stringify()`:


```javascript
const user = { name: "Alice", age: 30 }

const jsonString = JSON.stringify(user)

console.log(jsonString)
```


Tento tisk:


```
{"name":"Alice","age":30}
```


Text JSON můžete také převést zpět na objekt JavaScriptu pomocí `JSON.parse()`:


```javascript
const jsonText = '{"name":"Bob","age":25}'

const obj = JSON.parse(jsonText)

console.log(obj)
```


Tento tisk:


```
{ name: 'Bob', age: 25 }
```


Buďte opatrní: `JSON.parse()` vyhodí chybu, pokud řetězec není platný JSON.


```javascript
JSON.parse("not json") // ❌ Error!
```


Ujistěte se, že je řetězec správně naformátován.


### server `http`


NodeJS umožňuje vytvořit webový server, aniž byste museli instalovat cokoli dalšího.


Ke zpracování požadavků od klientů a odesílání odpovědí můžete použít vestavěný modul `http`.


Zde je velmi jednoduchý příklad:


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


Po spuštění tohoto skriptu a otevření `http://localhost:3000` v prohlížeči se zobrazí:


```
Hello from NodeJS server!
```


Toto se děje v kódu:


1. Importovali jste server `http` ze standardní knihovny Node.

2. `http.createServer()` vytvoří server. Předali jste `http.createServer()` zpětné volání `(req, res) => {...}`, které se provede pokaždé, když se někdo připojí.

3. Odpovědi jste přiřadili stavový kód 200 (který označuje úspěšnou operaci). O stavových kódech http si můžete přečíst [zde](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

3. `res.end()` odešle odpověď a ukončí spojení.

4. `server.listen(3000)` spustí server na portu 3000.


V požadavku můžete také zaškrtnout `req.url` a `req.method` a zpracovat tak různé cesty nebo typy požadavků.


Příklad se směrováním:


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


Jedná se o velmi základní příklady. Pro stavbu pokročilejších serverů si většina vývojářů pravděpodobně stáhne hotovou backendovou knihovnu, jako je [express](https://www.npmjs.com/package/express).


## Zpracování dat: vyrovnávací paměti, události, toky

<chapterId>8c9623f0-a604-51a4-8fe4-871c849d3e3b</chapterId>


V této kapitole si představíme především tři třídy objektů:



- `Buffer`, který představuje malé kousky binárních dat
- `EventEmitter`, který lze použít ke sledování některých kroků asynchronního procesu vysíláním signálů zvaných "události"
- `Stream`, který umožňuje zpracovávat velkou část dat po jednom `Bufferu` a který sleduje proces vysíláním událostí


V profesionálním kódu NodeJS jsou velmi časté, takže i když je ve svých prvních projektech nepoužijete, je dobré získat základní znalosti pro případy, kdy s nimi budete muset pracovat. z nich


### Nárazníky


V NodeJS je **buffer** typ objektu používaný pro práci s binárními daty.


Vyrovnávací paměť si můžete představit jako kontejner s pevnou velikostí pro surové bajty.


Zde se dozvíte, jak vytvořit vyrovnávací paměť z řetězce:


```javascript
const buf = Buffer.from("hello")
console.log(buf)
```


Vytiskne se něco jako:


```
<Buffer 68 65 6c 6c 6f>
```


Tato čísla (`68`, `65`, `6c` atd.) jsou hexadecimální reprezentací písmen ve slově `"ahoj`".


Můžete jej převést zpět na řetězec takto:


```javascript
console.log(buf.toString())
```


Tento tisk:


```
hello
```


Můžete také vytvořit vyrovnávací paměť určité velikosti vyplněnou nulami:


```javascript
const buf = Buffer.alloc(10)
console.log(buf)
```


Vytiskne se něco jako:


```
<Buffer 00 00 00 00 00 00 00 00 00 00>
```


Do vyrovnávací paměti můžete zapisovat:


```javascript
buf.write("abc")
console.log(buf)
```


A můžete přistupovat k jednotlivým bajtům:


```javascript
console.log(buf[0]) // prints the ASCII number for 'a', which is 97
```


Buffery jsou užitečné zejména tehdy, když potřebujete manipulovat s daty na velmi nízké úrovni.


### Události


V jazyce JavaScript je **událost** něco, co se stane ve vašem programu a na co můžete reagovat.


Například:



- soubor dokončí načítání
- vypne se časovač
- uživatel klikne na tlačítko
- síťový požadavek vrací data


Událost** je pouze signál, že se něco stalo, a vy můžete napsat kód, který bude těmto událostem naslouchat a reagovat na ně.


V NodeJS může mnoho objektů vysílat události. Tyto objekty se nazývají **EventEmitters**.


Zde je příklad:


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


Tento tisk:


```
Hello! An event happened.
```


Tady je to:


1. Vytvoříme objekt `EventEmitter`.

2. Pomocí příkazu `.on("greet")` mu řekneme, aby spustil zpětné volání vždy, když nastane událost `"greet"`.

3. Později spustíme událost `"greet"` pomocí `.emit()`.

4. Naše zpětné volání se provede


Spolu s událostí můžete předat data:


```javascript
emitter.on("greet",
(name) => console.log(`Hello, ${name}!`)
)

emitter.emit("greet", "Alice") // first argument is the type of event, second argument is the data we pass with this event
```


Tento tisk:


```
Hello, Alice!
```


Posluchače můžete registrovat i pro jiné události:


```javascript
emitter.on("goodbye", () => {
console.log("Goodbye!")
})

emitter.emit("goodbye")
```


K jednomu typu události můžete připojit libovolný počet posluchačů a ze stejného vysílače můžete vyvolat mnoho různých typů událostí.


Mnoho objektů v NodeJS vysílá události, které informují zbytek programu o tom, že se něco děje.



### Co jsou to proudy?


Proudy kombinují vyrovnávací paměť a události, které nám pomáhají zpracovávat data.


Při práci se soubory, daty ze sítě nebo dokonce s dlouhým textem nepotřebujeme (nebo nechceme) vždy načítat vše do paměti najednou. To by mohlo být pomalé, nebo by dokonce mohlo dojít k pádu programu, pokud jsou data příliš velká.


Namísto toho můžeme data zpracovávat **po částech**, jak přicházejí nebo jsou čtena, jako když pijete vodu brčkem, místo abyste se snažili vypít celou sklenici najednou. Tomu se říká **proud**.


V NodeJS je stream objekt, který umožňuje číst data ze zdroje nebo zapisovat data do cíle **po jednom kuse**.


NodeJS má čtyři hlavní typy streamů:



- Readable**: proudy, ze kterých lze číst data (jako při čtení souboru)
- Writable**: proudy, do kterých lze zapisovat data (jako zápis do souboru)
- Duplexní**: toky, které lze číst i zapisovat
- Transformace**: jako duplexní toky, ale mohou měnit (transformovat) data v průběhu jejich toku


### Čitelné proudy


Řekněme, že máte ke zpracování soubor `bigfile.txt`. Pomocí modulu `fs` můžete vytvořit čitelný datový tok a číst soubor po částech.


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


Co se zde děje?


1. `fs.createReadStream()` vytvoří čitelný datový tok.

2. Kdykoli je část souboru připravena, stream vyšle událost `data` a předá nám "kus" dat (`Buffer`). Tuto část vytiskneme.

3. Po přečtení celého souboru se spustí událost `konec`.

4. Pokud dojde k chybě (např. soubor neexistuje), spustí se událost `error`.


Tímto způsobem můžete číst obří soubory, aniž byste je všechny najednou načítali do paměti.


Pokud chceme, aby data přicházela v podobě čitelné pro člověka (místo v binární podobě), můžeme zadat kódování datového toku:


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


Kód nyní vytiskne soubor v podobě čitelné pro člověka.


### Zapisovatelné proudy


Zapisovatelný datový tok umožňuje posílat data někam po částech.


Zde je příklad zápisu do souboru `target.txt` pomocí proudu:


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


Děje se toto:


1. `fs.createWriteStream()` vytvoří zapisovatelný datový tok.

2. Pomocí `.write()` do něj zapíšeme nějaký text.

3. Po dokončení zavoláme `.end()`, čímž se datový tok uzavře.

4. Po zapsání všech dat je vyslána událost `finish`.

5. Pokud se něco pokazí, spustí se událost `error`.


Stejně jako čitelné datové proudy jsou i zapisovatelné datové proudy vhodné pro velká data, protože nepotřebují uchovávat vše v paměti najednou.


### Potrubní toky


Jednou z nejúžasnějších věcí na proudech je, že je můžete **propojit** dohromady: připojit čitelný proud přímo k zapisovatelnému proudu.


```javascript
const fs = require("fs")

const readable = fs.createReadStream("bigfile.txt")
const writable = fs.createWriteStream("target.txt")

readable.pipe(writable)
```


Zde:



- Čitelný proud čte z `bigfile.txt`.
- Zapisovatelný proud zapisuje do souboru `copy.txt`.
- `.pipe()` odešle data přímo z readable do writable streamu.


### Duplexní proudy


Oboustranný datový tok je čitelný i zapisovatelný. Příkladem je síťový soket: můžete do něj posílat data a přijímat je z něj.


Zde je velmi jednoduchý příklad s použitím modulu `net`:


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


V tomto příkladu:



- Objekt `socket` je duplexní datový tok.
- Můžete do něj `zapisovat()` a také z něj poslouchat události `dat`.


### Transformační proudy


Transformační proud je duplexní proud, který také upravuje data, která jím procházejí.


Ke kompresi nebo dekompresi dat můžete například použít vestavěný modul `zlib`.


Zde se dozvíte, jak komprimovat soubor pomocí transformačního proudu:


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


A dekomprese zpět:


```javascript
const readable = fs.createReadStream("bigfile.txt.gz")
const unzip = zlib.createGunzip()
const writable = fs.createWriteStream("bigfile.txt")

readable.pipe(unzip).pipe(writable)

writable.on("finish", () => {
console.log("File decompressed.")
})
```


Transformační proudy jsou velmi užitečné pro úlohy, jako je komprese, šifrování nebo změna formátů souborů během streamování.


### Protitlak


Někdy je zapisovatelný datový tok pomalý při zpracování dat. Pokud budeme do zapisovatelného proudu posílat data rychleji, než je schopen zpracovat, můžeme se dostat do problémů. Tomu se říká **zpětný tlak**.


Pokud zavoláte metodu `.write()` na zapisovatelný datový tok, vrátí vám boolean, který vás informuje o tom, zda datový tok potřebuje pauzu; možná budete muset zkontrolovat její návratovou hodnotu, například takto:


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


Toto byl názorný příklad ručního přenášení dat z Readable do Writable a ruční správy zpětného tlaku.


Obvykle bychom data přenášeli pomocí metody `.pipe()`, která automaticky zpracovává zpětný tlak.


Zpětného tlaku se tedy musíte obávat pouze tehdy, když z nějakého důvodu voláte `.write()` ručně.


## Závěrečná poznámka

<chapterId>139e2ab8-df67-525a-85f0-5a2fa5e478f2</chapterId>


Tak, to je vše, pokud jste postupovali podle lekcí, měli byste být nyní schopni napsat několik jednoduchých programů v NodeJS.


Přesně to bych doporučoval: po zvládnutí základů je nejlepším způsobem, jak se procvičit a stát se lepším programátorem, vytvoření několika osobních projektů.


Nezáleží na tom, co vytváříte, důležité je, že se snažíte řešit problémy pomocí kódu.


Moderní programovací jazyky jsou neuvěřitelně výkonné a NodeJS je pravděpodobně nejlepší sada nástrojů, se kterými můžete v této fázi své cesty experimentovat.


Hodně štěstí!


# Závěrečná část


<partId>322624d8-6fbc-11f0-a67a-5b145f10afc1</partId>


## Recenze a hodnocení


<chapterId>3e93ac86-6fbc-11f0-8bae-9b2ed7914843</chapterId>

<isCourseReview>true</isCourseReview>

## Závěr


<chapterId>49b3b9b2-6fbc-11f0-9870-5f5adcd3a0eb</chapterId>


<isCourseConclusion>true</isCourseConclusion>