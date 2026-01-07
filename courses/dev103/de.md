---
name: Grundlagen von JavaScript und NodeJS
goal: Lerne die Grundlagen der JavaScript-Programmierung und der NodeJS-Entwicklung, um praktische Anwendungen und Tools zu erstellen.
objectives: 

  - Beherrschen der grundlegenden JavaScript-Syntax, der Typen und des Kontrollflusses
  - Verstehen von Funktionen, Objekten und Klassen in JavaScript
  - Erlernen von Fehlerbehandlung und Debugging-Techniken
  - Einführung in NodeJS und sein Ökosystem

---

# Beginne deine Reise als Entwickler

Willkommen zu diesem Kurs über JavaScript und NodeJS.

JavaScript ist die beliebteste Programmiersprache der Welt: Sie ist die Skriptsprache moderner Browser, so dass es praktisch unmöglich ist, eine moderne Webanwendung zu erstellen, ohne *etwas* JavaScript zu schreiben; und mit der NodeJS-Laufzeitumgebung kann sie auch außerhalb von Browsern verwendet werden, um Skripte und Anwendungen zu erstellen, die direkt auf deinem Computer laufen.

Dieser Kurs richtet sich an Personen, die völlig neu in der Programmierung sind oder die bereits andere Sprachen verwendet haben, aber verstehen wollen, wie JavaScript funktioniert, insbesondere im Kontext von NodeJS.

Am Ende des Kurses solltest du in der Lage sein, eigene Programme in JavaScript zu schreiben, die NodeJS-Standardbibliothek zu verwenden und Pakete von Drittanbietern zu installieren und zu verwenden, um nützliche Tools zu erstellen.

+++
# Grundlegendes JavaScript
<partId>a617327c-e5a2-52ca-9380-c63f44623dd4</partId>

## Einrichtung
<chapterId>ba05a290-1782-5268-87c9-62fd09590e05</chapterId>

Ein JavaScript-Programm ist lediglich eine Sammlung von (einer oder mehreren) Textdateien, die Befehle enthalten, die von einer JavaScript-Laufzeitumgebung ausgeführt werden sollen.

Die Namen dieser Textdateien enden in der Regel mit der Dateierweiterung `.js`, wie z.B. `mein_script.js`, `mein_programm.js` usw.

Die darin enthaltenen Befehle sind in der Programmiersprache JavaScript geschrieben.

Eine JavaScript-Laufzeitumgebung ist ein spezielles Programm, das diese Dateien ausführt.

![](assets/en/001.webp)

### Die NodeJS-Laufzeitumgebung

Die am weitesten verbreitete JavaScript-Laufzeitumgebung ist NodeJS.

Deine IDE enthält es möglicherweise bereits, oder du musst es von der [offiziellen Website](https://nodejs.org/en/download) herunterladen.

Auf der Download-Seite findest du Anleitungen für alle drei gängigen Betriebssysteme: Windows, Linux und MacOS. Es wird vorausgesetzt, dass du weißt, wie man ein Terminal in deinem Betriebssystem öffnet.

Da NodeJS für alle drei Betriebssysteme verfügbar ist, können die von dir geschriebenen Programme auf allen Betriebssystemen ausgeführt werden (abgesehen von einigen Sonderfällen).

Das bedeutet, dass du zum Beispiel ein einfaches Videospiel in JavaScript auf deinem Windows-PC schreiben und es an einen Freund weitergeben kannst, damit er es auf seinem Mac ausführt.

![](assets/en/002.webp)

### Erstes Programm (Hallo Welt)

Wenn man eine Programmiersprache lernt, besteht das erste Programm, das man schreibt, traditionell darin, "Hallo Welt" auf der Konsole auszugeben.

Erstelle ein Verzeichnis mit dem Namen `my_js_code/` und darin eine Datei mit dem Namen `main.js` (diese Namen sind frei wählbar).

Öffne das Verzeichnis mit deinem Code-Editor.

Schreibe diesen Code in deine Datei:

```javascript
console.log("hello world!")
```

Öffne ein Terminal und führe diesen Befehl aus, um das Programm zu starten:

```
node main.js
```

Das Ergebnis sollte sein

```
hello world!
```

### Was geschah

In JavaScript ist alles ein "Objekt".

`console` ist ein Objekt, das zum Debuggen des Programms verwendet wird.

`console.log` ist die am häufigsten verwendete Methode der `console`. Sie gibt einfach die Argumente aus, die du ihr übergibst.

Du übergibst Argumente an `console.log` unter Verwendung der runden Klammern `()`.

Wenn du also zum Beispiel die Zahl "1000" ausgeben willst, schreib einfach

```javascript
console.log(1000)
```

Führe es dann aus, indem du

```
node main.js
```

in deinem Terminal eingibst (von nun an wird in diesem Kurs davon ausgegangen, dass du weißt, wie du ein Programm ausführen kannst).

Dies sollte folgendes anzeigen:

```
1000
```

Du kannst mehrere Dinge übergeben, wie

```javascript
console.log(16, 8, 1993)
```

Damit wird:

```
16 8 1993
```

ausgegeben.

## Variablen und Kommentare
<chapterId>23050ab7-343b-5edf-9d37-e4e782e27ce0</chapterId>

Programme führen in der Regel Operationen auf Daten aus.

Variablen sind wie benannte Kisten, die wir zum Speichern von Daten verwenden. Sie ermöglichen es uns, einen Teil der Daten mit einem bestimmten Namen zu verknüpfen, so dass wir sie später unter diesem Namen abrufen können.

### let-Deklarationen

Um eine Variable in JavaScript zu deklarieren, können wir das Schlüsselwort `let` verwenden.

Nachdem wir `let` geschrieben haben, schreiben wir den Namen, den wir der Variablen geben wollen, dann ein `=` Zeichen und dann den Wert, den wir speichern wollen.

Zum Beispiel:

```javascript
let age = 25

console.log(age)
```

Der Name einer Variablen (technisch als "identifier" bezeichnet) kann normalerweise Buchstaben, Unterstriche (`_`), das Dollarzeichen (`$`) und Zahlen enthalten, wobei das erste Zeichen keine Zahl sein darf.

Im obigen Code haben wir eine Variable namens `age` deklariert und den Wert `25` darin gespeichert.

Dann haben wir den Wert mit `console.log(age)` ausgegeben.

Wenn du diesen Code mit `node main.js` ausführst, wird die Ausgabe:

```
25
```
sein.

Bei Identifiern wird die Groß- und Kleinschreibung beachtet, d.h. Klein- und Großbuchstaben zählen als Unterschiede in den Identifiern, z.B.:

```javascript
let age = 25

let Age = 20

console.log(age)
```

gibt 25 aus, da es sich um zwei völlig unterschiedliche Variablen handelt!

Du kannst auch Zeichenketten (Text, engl. "strings") in einer Variablen speichern:

```javascript
let message = "hello again"

console.log(message)
```

Dies ergibt:

```
hello again
```

Genau wie zuvor haben wir `console.log()` verwendet, um den in der Variablen gespeicherten Wert auszugeben.

Jetzt wollen wir beides zusammen machen:

```javascript
let age = 25

let message = "hello again"

console.log(age)

console.log(message)
```

Wenn du dies ausführst, wird dies ausgegeben:

```
25
hello again
```

### Neuzuweisungen

Mit `let` deklarierte Variablen können nach ihrer Erstellung geändert werden.

Dies wird als Neuzuweisung bezeichnet.

```javascript
let score = 10

console.log(score)

score = 15

console.log(score)
```

Zuerst weisen wir `10` dem `score` zu und geben ihn dann aus.

Dann ändern wir den Wert von `score` auf `15` und geben ihn wieder aus.

Die Ausgabe wird sein:

```
10
15
```

Dies ist sehr nützlich, wenn sich der Wert im Laufe der Zeit ändert, z.B. bei einem Spiel, bei dem die Punktzahl steigt.

Lass uns eine weitere Variable mit einbeziehen:

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

Dies ergibt:

```
10
Alice
20
Bob
```

Wie du sehen kannst, wurden sowohl `Score` als auch `Player` geändert.

### const-Deklarationen

In den meisten Fällen wollen wir jedoch nicht, dass sich eine Variable nach ihrer Erstellung ändert. Dafür verwenden wir `const`.

`const` ist die Abkürzung für "constant". Sobald du einer `const`-Variablen einen Wert zugewiesen hast, kannst du ihn nicht mehr ändern.

```javascript
const pi = 3.14
console.log(pi)
```

Dies wird ausgegeben:

```
3.14
```

Aber wenn du versuchst, dies zu tun:

```javascript
const pi = 3.14
console.log(pi)

pi = 99 // diese Zeile löst einen Fehler aus
console.log(pi)
```

wird JavaScript dir eine Fehlermeldung wie diese ausgeben:

```
TypeError: Assignment to constant variable.
```

Das liegt daran, dass `pi` mit `const` deklariert wurde und du seinen Wert danach nicht mehr ändern kannst. Damit teilst du dem JavaScript-Interpreter mit, dass du nicht willst, dass sich die Variable ändert.

Das ist nützlich, weil es die Wahrscheinlichkeit einer versehentlichen Änderung verringert. Wenn Programme sehr groß werden, mit Tausenden von Codezeilen, ist es unmöglich, mit allem, was auf einmal passiert, Schritt zu halten (das ist der Hauptgrund, warum wir Computer benutzen, um komplexe Prozesse auszuführen, die wir mit unserem Gehirn nicht berechnen können), also ist es nützlich, Einschränkungen wie diese zu haben, die das Programm deterministischer machen.

Es gilt als Best Practice, unsere Werte immer als `const` zu deklarieren, es sei denn, wir sind sicher, dass wir sie später ändern wollen.

### Kommentare in JavaScript

Manchmal möchten wir Notizen in unseren Code schreiben, die nicht ausgeführt werden. Diese werden Kommentare genannt.

Kommentare werden vom Programm ignoriert, wenn es läuft, sind aber nützlich, um uns selbst oder anderen etwas zu erklären.

Um einen einzeiligen Kommentar zu schreiben, verwendet man `//`

```javascript
// Dies ist ein Kommentar
const x = 10 // Dies ist auch ein Kommentar
console.log(x)
```

Dies wird weiterhin ausgegeben:

```
10
```

Die Kommentare sind nur für Menschen zum Lesen da.

Du kannst auch mehrzeilige Kommentare mit `/*` und `*/` schreiben

```javascript
/*
Dies ein mehrzeiliger Kommentar.
Er erstreckt sich ueber mehere Zeilen.
*/
const y = 20
console.log(y)
```

Damit wird:

```
20
```
ausgegeben und der Kommentar wird ignoriert.

Mit Kommentaren kannst du kleine Anmerkungen zu deinem Code hinzufügen, damit du dich daran erinnern kannst, was er tut und warum er auf eine bestimmte Weise geschrieben ist. Du kannst auch anderen Programmierern helfen, ihn zu verstehen.

## Grundtypen: Zahlen, Zeichenketten, Boolesche Werte
<chapterId>cfdb04f6-21a8-5143-bbf9-7aaae04962f0</chapterId>

In JavaScript gibt ein "Typ" an, um welche Art von Daten es sich bei einem Wert handelt.

Javascript hat einige Grundtypen, und in diesem Abschnitt werden wir einige von ihnen untersuchen.

### Zahlen und arithmetische Operationen

Der erste Typ, den wir einführen werden, ist `number`.

Zahlen in JavaScript können ganze Zahlen (wie `5`) oder Dezimalzahlen (wie `3.14`) sein.

Man kann mit ihnen rechnen: Addition, Subtraktion, Multiplikation und Division.

Hier ist ein einfaches Beispiel:

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

Dies wird ausgegeben:

```
15
5
50
2
```

Du kannst auch Klammern `()` verwenden, um die Reihenfolge der Operationen zu steuern:

```javascript
const result = (2 + 3) * 4
console.log(result)
```

Dies wird ausgegeben:

```
20
```

Ohne die Klammern würde es "2 + 3 * 4" lauten, das ist:

```javascript
const result = 2 + 3 * 4
console.log(result)
```

Das wird ausgegeben:

```
14
```

Denn in der normalen Mathematik kommt die Multiplikation vor der Addition.

### Zeichenketten und Interpolation

Der zweite JavaScript-Typ, den wir einführen werden, ist die Zeichenkette (`string`).

Zeichenketten sind Textstücke. Du kannst einfache Anführungszeichen `'...'` oder doppelte Anführungszeichen `"..."` verwenden, um sie zu erstellen.

```javascript
const greeting = "hello"
const name = 'Bob'
console.log(greeting)
console.log(name)
```

Dies wird ausgegeben:

```
hello
Bob
```

Um Zeichenketten zu kombinieren, kannst du den Operator "+" verwenden:

```javascript
const greeting = "hello"
const space = " "
const name = "Bob"

const fullGreeting = greeting + space + name
console.log(fullGreeting)
```

Dies wird ausgegeben:

```
hello Bob
```

Aber es gibt einen schöneren Weg, Zeichenketten zu kombinieren, die **Zeichenketteninterpolation**. Hierzu verwendet man Backticks, um die Zeichenkette zu deklarieren `` `...` `` und schreibt Variablen mit `${...}` innerhalb der Zeichenkette:

```javascript
const greeting = "hello"
const name = "Bob"

const fullGreeting = `${greeting} ${name}`
console.log(fullGreeting)
```

Auch hierdurch wird:

```
hello Bob
```

ausgegeben.

Du kannst jeden Ausdruck innerhalb von `${...}` einschließen:

```javascript
const age = 30
console.log(`Next year, I will be ${age + 1} years old.`)
```

Dies wird ausgegeben:

```
Next year, I will be 31 years old.
```

Interpolation ist in modernem JavaScript sehr verbreitet.

### Boolesche Werte, vergleichende und logische Operationen

Der dritte Typ, den wir einführen werden, ist `boolean`. Er ist nach dem Mathematiker George Boole benannt, der die boolesche Logik erfand.

Booleans sind einfach: nur zwei mögliche Werte, "wahr" (`true`) und "falsch" (`false`).

Du kannst sie in Variablen speichern:

```javascript
const theSkyIsBlue = true
const thisCourseIsBad = false

console.log(theSkyIsBlue)
console.log(thisCourseIsBad)
```

Dies wird ausgegeben:

```
true
false
```

Du kannst Boolesche Begriffe mit logischen Operatoren kombinieren:


* `&&` bedeutet "und" und gibt nur dann "wahr" zurück, wenn **beide** Werte "wahr" sind, andernfalls wird "falsch" zurückgegeben
* `||` bedeutet "oder" und gibt "wahr" zurück, wenn **mindestens einer** der Werte "wahr" ist, andernfalls (wenn beide Werte "falsch" sind) gibt er "falsch" zurück
* `!` bedeutet "nicht", er wird vor einem booleschen Wert angewandt und kehrt diesen um: wenn der boolesche Wert "wahr" ist, wird "falsch" zurückgegeben und umgekehrt.

![](assets/en/003.webp)

Beispiele:

```javascript
const isSunny = true
const isWarm = true

console.log(isSunny && isWarm)  // true
console.log(isSunny || isWarm)  // true
console.log(!isSunny)           // false
```

Du kannst Werte in JavaScript mit Operatoren wie `>`, `<`, `===` und `!==` vergleichen. Das Ergebnis dieser Vergleiche ist immer ein boolescher Wert.

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

Javascript hat auch `>=`, um "größer oder gleich" abzufragen und `<=`, um "kleiner oder gleich" abzugrafen.

Boolesche Operatoren, Vergleichsoperatoren und logische Operatoren werden in Programmen oft kombiniert, um komplexe Bedingungen zu deklarieren, z.B. "die E-Mail ist angekommen UND sie enthält das Bild, das ich brauche ODER die Länge der E-Mail ist länger als 10000 Zeichen". Du wirst später feststellen, dass dies wichtige Bausteine sind, um die Logik des Programms zu konstruieren.

## Arrays, null, undefiniert
<chapterId>7bf18183-5eae-53ed-83d2-b04982145d81</chapterId>

In diesem Abschnitt werden wir drei weitere Typen behandeln, die in JavaScript-Programmen sehr häufig vorkommen:


* **Arrays**: Folgen von Werten
* **undefined**: ein spezieller Wert, der bedeutet "es wurde nichts zugewiesen"
* **null**: ein weiterer spezieller Wert, der "absichtlich leer" bedeutet

### Arrays und Indexzugriff

Ein **Array** ist ein Typ, der mehrere Werte in einer Liste enthalten kann.

Du erstellst ein Array, indem du eckige Klammern `[]` verwendest und die Elemente mit Kommas trennst.

Hier ist ein einfaches Beispiel:

```javascript
const numbers = [10, 2, 88]
console.log(numbers)
```

Dies wird ausgegeben:

```
[ 10, 2, 88 ]
```

In einem Array kannst du alles speichern, nicht nur Zahlen:

```javascript
const things = ["apple", 42, true]
console.log(things)
```

Dies wird ausgegeben:

```
[ 'apple', 42, true ]
```

Um auf ein bestimmtes Element im Array zuzugreifen, verwenden wir einen **Index**. Der Index ist die Position des Elements, beginnend mit **0**.

Also in dieser Reihe:

```javascript
const colors = ["red", "green", "blue"]
```

`colors[0]` ist `"red"`
`colors[1]` ist `"green"`
`colors[2]` ist `"blue"`

Versuchen wir es:

```javascript
const colors = ["red", "green", "blue"]
console.log(colors[0])
console.log(colors[1])
console.log(colors[2])
```

Dies wird ausgegeben:

```
red
green
blue
```

Du kannst einem bestimmten Index eines Arrays einen Wert zuweisen

```javascript
const colors = ["red", "green", "blue"]

colors[1] = "yellow"

console.log(colors)
```

Dies wird ausgegeben:

```
[ 'red', 'yellow', 'blue' ]
```

Du kannst jede natürliche Zahl als Index verwenden, auch eine, die in einer Variablen gespeichert ist

```javascript

const i = 1
const colors = ["red", "green", "blue"]
console.log(colors[i])
```

Dies wird ausgegeben:

```
green
```

Wenn du jedoch versuchst, auf einen Index zuzugreifen, der nicht existiert, erhältst du `undefined`:

```javascript
const colors = ["red", "green", "blue"]
console.log(colors[3])
```

Dies wird ausgegeben:

```
undefined
```

Was ist das??

### undefiniert

Der spezielle Wert `undefined` bedeutet "es wurde kein Wert zugewiesen".

Wenn du eine Variable erstellst, ihr aber keinen Wert zuweist, ist sie "undefiniert":

```javascript
const name
console.log(name)
```

Dies wird ausgegeben:

```
undefined
```

Da wir `name` nichts zugewiesen haben, setzt JavaScript ihn standardmäßig auf `undefined`.

Wie zuvor gesehen, kann man auch `undefined` bekommen, wenn man auf einen Array-Index zugreift, der nicht existiert:

```javascript
const fruits = ["banana", "apple"]
console.log(fruits[2]) // Es gibt keinen Index 2
```

Dies wird ausgegeben:

```
undefined
```

### null und wie es zu behandeln ist

`null` ist auch ein besonderer Wert. Er bedeutet "hier ist nichts, und das habe ich absichtlich gemacht"

Im Gegensatz zu `undefined`, das automatisch ist, ist `null` etwas, das du selbst festlegst.

Zum Beispiel:

```javascript
const currentUser = null
console.log(currentUser)
```

Dies wird ausgegeben:

```
null
```

Warum `null` verwenden? Vielleicht erwartest du später einen Wert, aber er ist noch nicht fertig:

```javascript
let winner = null

// Later in the program:
winner = "Alice"

console.log(winner)
```

Dies wird ausgegeben:

```
Alice
```

So ist `null` nützlich, wenn man z.B. sagen will: "Hier sollte später etwas stehen, aber im Moment ist es leer."

## Blöcke und Kontrollfluss
<chapterId>be985168-2636-5b0d-a48f-ac1bbfbff8a7</chapterId>

Bislang haben wir hauptsächlich Codezeilen geschrieben, die nacheinander ablaufen.

Aber wenn wir programmieren, können wir die Reihenfolge der Ausführung kontrollieren.

Dies wird als **Kontrollfluss** bezeichnet.

Beginnen wir mit dem Verständnis von Blöcken und Geltungsbereichen.

### Der globale Geltungsbereich

Jede Variable, die wir deklarieren, existiert in einem Geltungsbereich (engl. **Scope**). Damit wird Bereich des Codes, in dem die Variable bekannt ist bezeichnet.

Wenn du eine Variable außerhalb eines Blocks deklarierst, existiert sie im **globalen Bereich**.

```javascript
const color = "blue"
console.log(color)
```

Die Variable `color` befindet sich im globalen Bereich, so dass von überall in der Datei auf sie zugegriffen werden kann.

Wenn du weitere Zeilen hinzufügst:

```javascript
const color = "blue"
console.log(color)

const size = "large"
console.log(color)
console.log(size)
```

Sowohl `color` als auch `size` sind globale Variablen. Sie sind überall in der Datei verfügbar.

Aber was passiert innerhalb eines Blocks?

### Blöcke und lokaler Geltungsbereich

Ein **Block** ist ein Teil des Codes, der von geschweiften Klammern `{}` umgeben ist.

Mit `let` oder `const` deklarierte Variablen innerhalb eines Blocks existieren **nur** innerhalb dieses Blocks.

```javascript
{
  const message = "inside block"
  console.log(message)
}
```

Dies wird ausgegeben:

```
inside block
```

Aber wenn du das versuchst:

```javascript
{
  const message = "inside block"
}
console.log(message) // Error!
```

wird JavaScript dir eine Fehlermeldung wie diese ausgeben:

```
ReferenceError: message is not defined
```

Das liegt daran, dass `message` innerhalb des Blocks deklariert wurde und außerhalb des Blocks nicht existiert.

Das bedeutet, dass wir Blöcke verwenden können, um Teile unseres Codes zu isolieren und sicher zu sein, dass "was im Block passiert, im Block bleibt" (ähnlich wie in Las Vegas).

Wenn wir unseren Code in Blöcken organisieren, können wir auch die Ausführung des Programms mit Kontrollflusskonstrukten wie "wenn" (`if`) strukturieren

### "wenn" (`if`) , "sonst" (`else')

Manchmal wollen wir Code **nur dann** ausführen, **wenn** etwas wahr ist. Dafür ist die `if`-Anweisung gedacht.

```javascript
const myAge = 20

console.log("Am I an adult?")

if (myAge >= 18) {
  console.log("Yes I am!")
}
```

Dies wird ausgegeben:

```
Am I an adult?
Yes I am!
```

Wie du sehen kannst, vergleicht der Code `myAge` und `18`.

In diesem Fall gibt der ">="-Operator "wahr" zurück, so dass der Block ausgeführt wird.

Wenn die Bedingung nicht "wahr" ist, wird der Block nicht ausgeführt.

```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
  console.log("Yes I am!")
}
```

Dies wird ausgegeben:

```
Am I an adult?
```

Du kannst einen `else`-Block hinzufügen, um den umgekehrten Fall zu behandeln:

```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
  console.log("Yes I am!")
} else {
  console.log("No, I am not.")
}
```

Dies wird ausgegeben:

```
Am I an adult?
No, I am not.
```

Sowohl die `if`- als auch die `else`-Blöcke sind immer noch Blöcke - also existieren die darin deklarierten Variablen nicht außerhalb.

Wenn wir sicher sein wollen, dass etwas **nicht** wahr ist, was können wir dann tun?

Nun, wie bereits erwähnt, verfügt JavaScript über einen "nicht"-Operator, der Boolesche Werte umkehrt. Wir können also folgendes tun:

```javascript
const myAge = 17

const adult = myAge >= 18

console.log("Am I an adult?")

if (!adult) {
  console.log("No, I am not.")
}
```

Es wird immer noch ausgegeben:

```
Am I an adult?
No, I am not.
```

Weil wir den Operator `!` verwendet haben, um die Variable `adult` zu invertieren.

if (!adult) {...}" sollte als "wenn nicht adult..." gelesen werden

Mit Hilfe von Blöcken, Logik und Vergleichsoperatoren können wir die Ausführung des Programms strukturieren, indem wir Variablen definieren, die "wahr" (oder "falsch") sein müssen, damit etwas passiert.

### "während" (`while`), "abbrechen" (`break`), "fortsetzen" (`continue`)

Eine "während" (`while`)-Schleife wiederholt den Code, *so lange* eine Bedingung erfüllt ist.

```javascript
let count = 0

while (count < 3) {
  console.log("Count is", count)
  count = count + 1
}
console.log("the loop is over!")
```

Dies wird ausgegeben:

```
Count is 0
Count is 1
Count is 2
the loop is over!
```

Wenn `count` 3 wird, stoppt die Schleife.

Du kannst eine Schleife mit "abbrechen" (`break`) vorzeitig beenden:

```javascript
let number = 1 // Starte mit 1

while (true) { // Diese Bedingung ist immer wahr, d.h. diese Schleife läuft für immer, es sei denn, wir stoppen sie
  console.log(number) // Gib die aktuelle Zahl aus
  if (number === 3) { // Wenn die Zahl 3 ist, stoppe die Schleife
    break
  }
  number = number + 1 // Erhöhe die Zahl um 1
}
```

Dies wird ausgegeben:

```
0
1
2
```

Denn wenn die Zahl `3` wird, wird der `if`-Block ausgeführt und die Schleife wird angehalten.

Du kannst den Rest einer Schleifeniteration mit "fortsetzen" (`continue`) überspringen:

```javascript
let number = 0 // Starte mit 0

while (number < 5) { // Mache weiter solange die Zahl kleiner als 5 ist
  number = number + 1 // Erhöhe die Zahl um 1

  if (number === 3) { // Wenn die Zahl 3 ist
    continue // Überspringe den Rest des Blocks und beginne die näcshte Iteration der Schleife
  }

  console.log(number) // Gib die Zahl aus
}
```

Dies wird ausgegeben:

```
1
2
4
5
```

Denn als die Zahl `3` war, ließ `continue` das Programm die Zeile überspringen, die die Zahl ausgibt.

### "für ... aus ..." (`for ... of ...`)

Wenn du ein Array hast und etwas mit jedem Element darin machen willst, kannst du `for ... of ... {...}` verwenden.

```javascript
const fruits = ["apple", "banana", "cherry"]

for (const fruit of fruits) {
  console.log(fruit)
}
```

Dies wird ausgegeben:

```
apple
banana
cherry
```

Der Block wird für jedes Element des Arrays einmal ausgeführt.

`fruit` ist hier eine neue Variable, die den Wert jedes Elements im Array aufnimmt, um es innerhalb des Blocks zu bearbeiten.

### für ... in ... (`for ... in ...`)

Du kannst `for ... in` verwenden, um eine Schleife über die Schlüssel (Indizes) eines Arrays zu iterieren:

```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
  console.log(index)
}
```

Dies wird ausgegeben:

```
0
1
2
```

Du kannst auch den Index verwenden, um den Wert zu erhalten:

```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
  console.log(fruits[index])
}
```

Dies ergibt dasselbe wie `for ... of`:

```
apple
banana
cherry
```

In der Praxis solltest du für Arrays lieber `for ... of` verwenden, da dies einfacher und sauberer ist.

### Begrenzte Schleifen

Manchmal möchte man eine bestimmte Anzahl von Schleifen durchlaufen oder ganz allgemein Code schreiben, der einen Block wiederholt und sich dabei etwas merkt.

Dafür ist eine begrenzte "for"-Schleife gut.

Eine begrenzte Schleife enthält normalerweise drei Bedingungen, die durch ein Semikolon `;` getrennt sind, wie in `(... ; ... ; ....)`.

```javascript
for (let i = 0; i < 3; i = i + 1) {
  console.log(i)
}
```

Dies wird ausgegeben:

```
0
1
2
```

Lass uns das erklären:


* `let i = 0`: deklariert eine Variable, die im Block verwendet werden soll (in diesem Fall ist es ein Zähler, der bei 0 beginnt)
* `i < 3`: deklariert eine Bedingung, die `wahr` sein muss, damit der Block ausgeführt wird (in diesem Fall ist es "wiederholen, solange `i` kleiner als 3 ist")
* `i = i + 1`: deklariert etwas Code, der nach jeder Ausführung des Blocks ausgeführt wird (in diesem Fall "erhöhe `i` um 1")

Wie du sehen kannst, können wir mit der begrenzten Schleife komplexere Bedingungen für die wiederholte Ausführung eines Codestücks deklarieren, aber meistens ist das nicht notwendig.

### Block-Labels

Wenn du einen komplexeren Kontrollfluss schreiben musst, kannst du in JavaScript einen Block mit einem **Label** versehen, das von `break` oder `continue` verwendet werden kann, um anzugeben, *wohin* zurückgesprungen werden soll.

Beispiel:

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

Dies wird ausgegeben:

```
We're inside the outer scope
We're inside the inner scope.
Done
```

Wir haben `break outer` verwendet, um den `outer`-Block vollständig zu verlassen.

Du kannst auch Schleifen mit einem Label versehen. Nehmen wir dieses Beispiel:

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

// Deklariere ein Array, welches die Monate enthält, die 30 Tage haben
const monthsWith30Days = [
  april, june, september, november
]

// Deklariere Variablen um mitzunotieren welcher Monat und Tag es ist
let currentMonth = january
let currentDay = 1

monthsLoop: while (true) {  // Beginne eine Schleife mit dem Namen "monthsLoop" um jeden Monat zu verarbieten

    daysLoop: while (true) {  // Beginne eine Schleife mir dem Namen "daysLoop" um jeden Tag zu verarbeiten
        totalDaysInOneYear = totalDaysInOneYear + 1  // Erhöhe die Gesamtzaahl der gezählten Tage um 1

        if (                                                                   // Wir wollen prüfen, ob wir am Ende des Monats angekommen sind.
            currentDay === 31                                                  // Prüfen ob der aktuelle Tag 31 ist (für Monate mit 31 Tagen) with 31 days)...
            || currentDay === 30 && (monthsWith30Days.includes(currentMonth))  // ...oder 30  und es ist ein Monat mit 30 Tagen
            || currentDay === 28 && (currentMonth === february)                // ...oder 28, falls es Februar ist. Falls eines von den dreien zutrifft...:

        ){
            currentMonth = currentMonth + 1  // Wechsle in den nächsten Monat
            currentDay = 1                   // Setze den aktuellen Tag des Monats zurück auf 1
            break daysLoop                   // Verlasse die innere Schleife (für Tage) und gehe zurück zur äußeren Schleife (für Monate)
        }
        else { currentDay = currentDay + 1 }                                   // Andernfalls ist der Monat nicht zu Ende und wir gehen einfach einen Tag weiter

    }
    if (currentMonth > 12) {  // Wenn ein Monat zu Ende ist, prüfen wir, ob wir über Dezember hinausgelaufen sind
        break monthsLoop  // Falls ja, beende die äußere Schleife und beende die Zählung der Tage
    }
}

console.log(totalDaysInOneYear)  // Gebe die Gesamtzahl der Tage in einem Jahr aus (sollte 365 sein)
```

Dies war ein sehr langweiliges Beispiel, aber es hat hoffentlich die (gelegentliche) Notwendigkeit von Labeln verdeutlicht.

## Einführung von Funktionen
<chapterId>cc324715-09c2-5cf7-9e6f-47a6f16bc04d</chapterId>

Wenn deine Programme wachsen, wirst du oft Teile des Codes **wiederverwenden** wollen.

Dafür sind **Funktionen** da: Sie ermöglichen es dir, Code zu gruppieren, ihm einen Namen zu geben und ihn auszuführen, wann immer du willst.

### Funktions-Deklaration

Um eine Funktion zu deklarieren, können wir das Schlüsselwort `function` verwenden. Dann geben wir ihr einen Namen, ein Klammerpaar `()` mit den Argumenten, die sie benötigt, und einen Codeblock `{}`, der ausgeführt werden soll. Beginnen wir mit einer Funktion, die keine Argumente benötigt:

```javascript
function sayHello () {console.log(`Hello!`) }
```

Dieser Code **deklariert** die Funktion, führt sie aber **noch** nicht aus.

### Funktionsaufrufe

Um die Funktion auszuführen (oder "aufzurufen"), schreiben wir ihren Namen, gefolgt von Klammern:

```javascript
function sayHello () {console.log(`Hello!`) }
sayHello()
```

Dies wird ausgegeben:

```
Hello!
```

Du kannst die Funktion so oft aufrufen, wie du willst:

```javascript
function sayHello() {
  console.log("Hello!")
}

sayHello()
sayHello()
```

Dies wird ausgegeben:

```
Hello!
Hello!
```

Der Code innerhalb der Funktion wird nur ausgeführt, wenn du sie aufrufst.

### Funktionsargumente (Eingabe in Funktionen)

Manchmal möchte man, dass eine Funktion mit einer bestimmten Eingabe arbeitet. Das kannst du tun, indem du **Argumente** innerhalb der Klammern hinzufügst.

Zum Beispiel:

```javascript
function sayHelloTo (friend) {
  console.log(`Hello ${friend}!`)
}
```

Diese Funktion benötigt **ein Argument** namens `friend`.

Wenn du die Funktion aufrufst,+ kannst du einen Wert übergeben:

```javascript
sayHelloTo("Tommy")
```

Dies wird ausgegeben:

```
Hello Tommy!
```

Du kannst die Funktion mit einem anderen Namen erneut aufrufen:

```javascript
sayHelloTo("Sam")
```

Dies wird ausgegeben:

```
Hello Sam!
```

Der Wert, den du übergibst, ersetzt die Variable `friend` innerhalb der Funktion.

Du kannst auch mehr als ein Argument verwenden:

```javascript
function greetTwoPeople(person1, person2) {
  console.log(`Hello ${person1} and ${person2}!`)
}

greetTwoPeople("Lina", "Marco")
```

Dies wird ausgegeben:

```
Hello Lina and Marco!
```

### `return` (Ausgabe von Funktionen)

Funktionen können auch Werte **zurückgeben**. Das heißt, sie senden einen Wert zurück an den Ort, an dem die Funktion aufgerufen wurde.

Hier ist ein einfaches Beispiel:

```javascript
function getNumber() {
  return 42
}

const result = getNumber()
console.log(result)
```

Dies wird ausgegeben:

```
42
```

Die Funktion `getNumber()` gibt `42` zurück, und wir speichern sie in `result` und geben sie dann aus.

Du kannst auch etwas zurückgeben, das du berechnest:

```javascript
function add(a, b) {
  return a + b
}

const result = add(2, 3)
console.log(result)
```

Dies wird ausgegeben:

```
5
```

Sobald ein Wert "zurückgegeben" wird, endet die Funktion. Alles, was nach `return` in diesem Block kommt, passiert nicht.

```javascript
function saySomething() {

  return "hi"

  console.log("this never runs")

}

const message = saySomething()
console.log(message)
```

Dies wird nur gedruckt:

```
hi
```

weil nur `"hi"` zurückgegeben wird. Die Zeile `console.log("this never runs")` wird übersprungen.

Du kannst dir Funktionen als kleine Unterprogramme vorstellen. Jede Funktion kann eine Eingabe entgegennehmen, diese bearbeiten und eine Ausgabe zurückgeben.

Was passiert, wenn wir versuchen, den Rückgabewert einer Funktion zu verwenden, die aber nichts zurückgegeben hat?

```javascript
function doesNothing () {}

const x = doesNothing()

console.log(x)
```

Dies wird `undefined` ausgeben. Der Rückgabewert einer Funktion, die nichts zurückgegeben hat, ist "undefiniert".

## Objekte und Klassen
<chapterId>26689f25-8212-5057-8c21-3a05eee0ac75</chapterId>

JavaScript wird oft als objektorientierte Sprache bezeichnet.

Das bedeutet, dass es dir hilft, deinen Code zu organisieren, indem es Werte und Funktionen zu **Objekten** zusammenfasst.

### Was ist ein Objekt?

Ein Objekt (`object`) kann Daten und Funktionen enthalten, die mit diesen Daten arbeiten. Wenn eine Funktion in ein Objekt eingefügt wird, spricht man von einer "Methode" (`method`).

Das erste Objekt, das wir gesehen haben, war das Objekt `console`. Es ist ein Objekt, das mehrere Methoden enthält, um Dinge auf dem Bildschirm anzuzeigen und unsere Programme zu debuggen.

Es kann sogar sich selbst anzeigen; Du kannst

```javascript
console.log(console)
```

schreiben und es wird eine Liste seiner enthaltenen Methoden ausgegeben. Auf meinem Rechner wird zum Beispiel Folgendes ausgegeben:

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

Wie du sehen kannst, hat es viele Methoden, die du zum Debuggen verwenden kannst!

Javascript bietet uns verschiedene Möglichkeiten, neue Objekte zu erstellen, die alles tun können, was wir von ihnen verlangen.

### Erstellen eines Objekts

Die einfachste Art, ein Objekt zu erstellen, ist die Gruppierung von Daten und Funktionen mit **geschweiften Klammern** `{}`.

Dadurch wird ein so genanntes **anonymes Objekt** erschaffen

```javascript
const cat = {
  name: "Whiskers",
  age: 3
}
```

Dies erzeugt ein Objekt und speichert es in einer Variablen namens `cat`.

Das Objekt hat zwei **Eigenschaften**:


* `name` mit dem Wert `Whiskers`
* `age` mit dem Wert `3`

Zeigen wir es an:

```javascript
console.log(cat)
```

Dies wird ausgegeben:

```
{ name: 'Whiskers', age: 3 }
```

Du kannst die einzelnen Eigenschaften eines Objektes mit einem Punkt abrufen, wie in `ObjektName.EigenschaftName`:

```javascript
console.log(cat.name)  // prints "Whiskers"
console.log(cat.age)   // prints 3
```

Du kannst eine Eigenschaft auch **ändern**:

```javascript
cat.age = 4
console.log(cat.age)  // now it prints 4
```

Wie du siehst, kannst du die darin enthaltenen Daten auch dann ändern, wenn ein Objekt als `const` definiert ist.

Im Falle von Objekten verhindert `const` nur, dass du das gesamte Objekt überschreibst:

```javascript
const cat = {
  name: "Whiskers",
  age: 3
}

cat.age = 5 // Dies klappt

cat = 5 // Dies resultiert in einem Fehler, da du versuchst das ganze Objekt neu zuzuweisen

```

Wie bereits erwähnt, können Objekte auch **Funktionen** enthalten, und wenn eine Funktion Teil eines Objekts ist, nennen wir sie eine **Methode**.

Hier ist ein Beispiel:

```javascript
const cat = {
  name: "Whiskers",
  speak () {
    console.log("Meow!")
  }
}
```

Dieses Objekt hat:


* Eine Eigenschaft `name`
* Eine `speak()`-Methode

Rufen wir die Methode auf:

```javascript
cat.speak()
```

Ausgabe:

```
Meow!
```

Methoden können die Daten, die das Objekt enthält, durch das Schlüsselwort `this` verwenden.

`this` bezieht sich auf das aktuelle Objekt. In diesem Beispiel wird es verwendet, um den Namen der Katze (`cat`) auszugeben:

```javascript
const cat = {
  name: "Whiskers",
  speak () {
    console.log(`${this.name} says meow!`)
  }
}

cat.speak()
```

Dies wird ausgegeben:

```
Whiskers says meow!
```

Das Wort `this` bedeutet "dieses Objekt", in diesem Fall das Objekt `cat`.


Diese Art von Objekten ist ideal, wenn man nur etwas Schnelles und Einfaches will. Wenn man jedoch **viele Objekte** mit der gleichen Struktur erstellen muss, gibt es einen besseren Weg, und hier kommen **Klassen** ins Spiel.

### Klassen und Konstruktoren

Eine **Klasse** ist wie eine Blaupause oder Konstruktionsplan. Sie sagt JavaScript, wie eine bestimmte Art von Objekt zu erstellen ist.

Man definiert eine Klasse mit dem Schlüsselwort `class`, gefolgt von dem Namen der Klasse und einem Block mit geschweiften Klammern `{}`.

```javascript
class Dog {}
```

Es ist üblich, dass Klassenamen mit einem Großbuchstaben beginnen.

Mit `new` kannst du ein neues Objekt einer Klasse erstellen:

```javascript
const hachiko = new Dog()
```

Versuchen wir, das Objekt anzuzeigen:

```javascript
class Dog {}

const myDog = new Dog()

console.log(myDog)
```

Wir erhalten:

```
Dog {}
```

Wie du sehen kannst, ist die Klasse `Dog` (Hund) leer, also ist auch das Objekt `myDog` leer.

Wir können festlegen, welche Eigenschaften Hundeobjekte haben sollen, indem wir einen "Konstruktor" (`constructor`) hinzufügen.

Ein Konstruktor ist eine spezielle Funktion, die ausgeführt wird, wenn ein neues Objekt erstellt (oder "konstruiert") wird.

```javascript
class Dog {
  constructor() { }
}
```

Wir wollen, dass jeder Hund einen Namen hat, also fügen wir der Funktion einen Parameter `name` hinzu:

```javascript
class Dog {
  constructor(name) { }
}
```

Und dann benutzen wir `this`, um zu deklarieren, dass `name` der `name` des `Dog`-Objekts ist, das wir erstellen:

```javascript
class Dog {
  constructor(name) {
    this.name = name
  }
}
```

Versuchen wir jetzt, es zu benutzen:

```javascript
class Dog {
  constructor(name) {
    this.name = name
  }
}

const myDog = new Dog("hachiko")

console.log(myDog)
```

Dies ergibt etwas wie:

```
Dog { name: 'hachiko' }
```

Wie du siehst, nimmt die `constructor`-Methode die Argumente, die du der Klasse übergibst, wenn du `new Dog()` aufrufst, und benutzt sie, um das Objekt zu erstellen.

Schauen wir uns das mal an:

* `class Dog` definiert die Klasse Hund.
* `constructor(name)` konfiguriert das Objekt, wenn es erstellt wird.
* `this.name = name` speichert den Wert in dem neuen Objekt.
* `new Dog("hachiko")` erzeugt ein neues Objekt der Klasse, wobei die Eigenschaft `name` auf `"hachiko"` gesetzt wird.

Fügen wir nun eine Methode zu unserer Klasse hinzu:

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

Damit wird:

```javascript
hachiko says barf!
```
ausgegeben.

Wenn wir das Gleiche für zwei verschiedene Instanzen von `Dog` tun


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

erhalten wir

```
hachiko says barf!
bobby says barf!
```

Die Methode `speak()` verwendet die Eigenschaft `name` des `Dog`, auf den sie angewendet wird.

Das ist der Hauptgrund für die Existenz von Klassen: Sie ermöglichen es uns, eine Reihe von Methoden zu definieren, die mit Daten arbeiten, und dann mehrere Objekte zu erstellen, die dieselbe Daten-`Form` haben.

Wenn wir eine Methode für eines dieser Objekte aufrufen, wird sie mit den Daten arbeiten, die *das spezifische Objekt* enthält.

### Ändern der Form eines Objekts

Objekte in JavaScript sind flexibel. Selbst nachdem du ein Objekt erstellt hast, kannst du noch neue Eigenschaften hinzufügen oder vorhandene entfernen.

Es ist erlaubt, aber man sollte es mit Bedacht einsetzen.

Beginnen wir mit unserer einfachen Klasse `Dog`:

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

Zu diesem Zeitpunkt hat `myDog` nur eine Eigenschaft: `name`. Wir können immer noch neue Eigenschaften hinzufügen, nachdem er erstellt wurde:

```javascript
myDog.age = 5

console.log(myDog.age) // prints 5
```

Wir können auch eine neue Methode hinzufügen:

```javascript
myDog.jump = function () {
  console.log(`${this.name} jumps!`)
}

myDog.jump() // Fido jumps!
```

Und mit dem Schlüsselwort `delete` können wir auch Eigenschaften entfernen.

```javascript
delete myDog.name

console.log(myDog.name) // prints 'undefined'
```

Das funktioniert, aber es gibt etwas Wichtiges zu wissen: JavaScript-Engines wie V8 (wird von Node.js und im Chrome-Browser verwendet) laufen schneller, wenn Ihre Objekte immer dieselben Eigenschaften haben. Wenn du Eigenschaften hinzufügst oder entfernst, nachdem das Objekt erstellt wurde, kann dies die Abläufe verlangsamen.

Bei kleinen Programmen spielt das keine große Rolle. Aber bei größeren Projekten (wie Spielen) ist es besser, alle Eigenschaften von Anfang an im Konstruktor aufzulisten, auch wenn du sie nicht sofort verwendest. Dadurch bleibt die Form des Objekts stabil und dein Code läuft schneller.

Zum Beispiel, anstatt dies zu tun:

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

kannst du Folgendes tun

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

Beide Versionen funktionieren, aber die zweite ist besser für die Performance. Du sagst der Engine im Voraus, welche Eigenschaften jedes Objekt haben wird, und sie kann entsprechend optimieren.

In JavaScript kannst du Objekte frei umgestalten, aber bei der Verwendung von Klassen ist es am besten, die Form deines Objekts im Voraus zu planen.


### Vererbung mit extends und super()

Manchmal möchte man eine Klasse erstellen, die *fast* die gleiche ist wie eine andere Klasse, aber ein paar zusätzliche Funktionen hat.

Anstatt die Form von Objekten zu ändern (was, wie bereits erwähnt, nicht optimal für die Leistung ist) oder eine neue Klasse von Grund auf neu zu schreiben, kannst du in JavaScript etwas verwenden, das **Vererbung** genannt wird.

Vererbung bedeutet, dass eine Klasse eine andere **erweitern** kann. Die neue Klasse erhält alle Eigenschaften und Methoden der alten Klasse, und Du kannst weitere hinzufügen oder ändern, was du brauchst.

Nehmen wir an, wir haben eine Basisklasse namens "Fahrzeug" (`Vehicle`):

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

Jetzt wollen wir eine Klasse "Auto" (`Car`) erstellen. Ein Auto ist eine Art von Fahrzeug, aber wir wollen vielleicht, dass es einige zusätzliche Funktionen hat oder eine andere Nachricht, wenn es startet. Anstatt alles neu zu schreiben, können wir `extends` verwenden:

```javascript
class Car extends Vehicle {
  start() {
    console.log(`${this.brand} car is ready to drive!`)
  }
}
```

Die Klasse `Car` **erbt** jetzt alles von `Vehicle`. Sie erhält die Eigenschaft "Marke" (`brand`), und wir haben die Methode `start()` durch unsere eigene Version ersetzt.

![](assets/en/004.webp)

Probieren wir es aus:

```javascript
const myCar = new Car("Toyota")
myCar.start()
```

Dies wird ausgegeben:

```
Toyota car is ready to drive!
```

Auch wenn `Car` keinen eigenen Konstruktor hat, verwendet es den von `Vehicle`. Aber wenn wir einen eigenen Konstruktor in `Car` schreiben wollen, können wir das, wir müssen nur einen Aufruf des Konstruktors seiner Elternklasse mit `super()` einfügen.

So geht's:

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
    super(brand) // rufe den Konstruktor der Elternklasse auf und überge "brand" als Argument
    this.model = model
  }

  start() {
    console.log(`${this.brand} ${this.model} is ready to drive!`)
  }
}

const myCar = new Car("Toyota", "Corolla")
myCar.start()
```

![](assets/en/005.webp)


Dies wird ausgegeben:

```
Toyota Corolla is ready to drive!
```

Zusammenfassend:


* `extends` bedeutet, dass eine Klasse auf einer anderen basiert.
* mit `super()` wird der Konstruktor der Klasse die wir erweitern aufgerufen.
* Die neue Klasse erhält alle Eigenschaften und Methoden der ursprünglichen Klasse.
* Man kann Methoden (wie `start()`) **überschreiben**, damit sie etwas anderes tun.

Dies ist hilfreich, wenn man mehrere ähnliche Dinge hat (z. B. Autos, Lastwagen und Fahrräder) und möchte, dass diese gemeinsamen/geteilten Code haben, sich aber dennoch auf ihre eigene Weise verhalten.

### Instanz von (`instanceof`)

Das Schlüsselwort `instanceof` prüft, ob ein Objekt von einer bestimmten Klasse erzeugt wurde.

Nehmen wir an, wir haben eine Klasse namens "Benutzer" (`User`):

```javascript
class User {
  constructor(username) {
    this.username = username
  }
}

const regularUser = new User("julia123")

console.log(regularUser instanceof User)
```

Dies wird ausgegeben:

```
true
```

was bestätigt, dass `regularUser` ein `User` ist. Das liegt daran, dass `regularUser` mit der Klasse `User` erstellt wurde.

Dies funktioniert auch mit **vererbten** Klassen. Hier ist zum Beispiel eine `Admin`-Klasse, die `User` erweitert:

```javascript
class Admin extends User {}

const ourAdmin = new Admin("admin42")

console.log(ourAdmin instanceof Admin)   // true
console.log(ourAdmin instanceof User)    // true
```

Beide Zeilen geben `true` zurück. Das liegt daran, dass `Admin` eine Unterklasse von `User` ist, daher ist `ourAdmin` sowohl ein `Admin` als auch ein `User`

# Mittelschweres JavaScript
<partId>243f63ab-4f34-5c30-80cb-84ef46f6761d</partId>

## Fehlerbehandlung
<chapterId>d0206bc5-d386-5e7f-9917-5803f392448c</chapterId>

Wenn du komplexere JavaScript-Programme schreibst, wirst du auf "Fehler" (**errors**) stoßen. Das sind unerwartete Situationen, in denen etwas schief geht. Vielleicht ist eine Variable "undefiniert", aber du versuchst, sie zu verwenden, oder ein Codeteil empfängt die falsche Art von Eingabe.

Wenn wir mit diesen Fehlern nicht richtig umgehen, kann unser Programm abstürzen oder sich auf unvorhersehbare Weise verhalten. JavaScript bietet Werkzeuge zum Erkennen und Verwalten dieser Fehler, damit wir sie besser behandeln können.

### Häufiger Fehler: Zugriff auf einen Wert von undefined

Hier ist eine häufige Situation, die einen Fehler verursacht:

```javascript
const user = undefined
console.log(user.name)
```

Wenn wir diesen Code ausführen, erhalten wir eine Fehlermeldung, die wie folgt aussieht:

```
TypeError: Cannot read properties of undefined (reading 'name')
```

Das ist JavaScripts Art dir zu sagen: "Hey, du hast versucht, die Eigenschaft `name` von etwas zu lesen, das `undefined` ist, und das macht keinen Sinn." Und wie du sehen kannst, hört das Programm auf zu laufen, wenn diese Art von Fehler auftritt, es sei denn, du hast speziellen Code geschrieben, um den Fehler abzufangen und zu behandeln.

### Einen Fehler "auslösen" (`throw`)

Manchmal möchtests du in deinem Code manuell **einen Fehler** auslösen. In diesem Fall verwende das Schlüsselwort `throw`.

```javascript
throw new Error("This is a custom error message")
```

Dadurch wird das Programm sofort angehalten und gibt folgendes aus:

```
Uncaught Error: This is a custom error message
```

Du kannst `throw` verwenden, um Regeln in deinem Programm durchzusetzen. Zum Beispiel:

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

Der zweite Aufruf führt zu einem Fehler, da die Division durch Null in diesem Beispiel nicht zulässig ist.

### Auffangen von Fehlern mit `try...catch`

Wenn du nicht willst, dass dein Programm abstürzt, wenn ein Fehler auftritt, kannst du den Fehler mit einem `try...catch`-Block abfangen. Dies ist hilfreich, wenn du möchtest, dass dein Programm **weiterläuft**, auch wenn etwas fehlschlägt.

```javascript
try {
  const user = undefined
  console.log(user.name)
  console.log("End of the block") // wird nie angezeigt
} catch (error) {
  console.log("Oops! Something went wrong.")
}
```

Ausgabe:

```
Oops! Something went wrong.
```

Und so funktioniert es:


* Der Code innerhalb des `try`-Blocks wird zuerst probiert auszuführen.
* *Wenn ein Fehler auftritt, **springt JavaScript zum `catch'-Block** und überspringt den Rest des `try'-Blocks.*
* Der `catch`-Block empfängt den Fehler, so dass du ihn ausgeben oder auf andere Weise behandeln kannst, wie zum Beispiel

```javascript
try {
  const user = undefined
  console.log(user.name)
  console.log("End of the block") // wird nie angezeigt
} catch (error) {
  console.log(`The message of the error was: "${error.message}"`)
}
```

Ausgabe:

```
The message of the error was: "Cannot read properties of undefined (reading 'name')"
```

### Der finally-Block

Du kannst auch einen `finally`-Block hinzufügen. Dieser enthält Code, der **immer** läuft, egal ob ein Fehler aufgetreten ist oder nicht.

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

Ausgabe:

```
Trying something risky...
Caught the error: Uh oh!
This will run no matter what.
```

## Vermeiden von Fehlern (`bugs`)
<chapterId>db12d9f6-5806-514c-998e-0ae24805104e</chapterId>

Dieses Kapitel zeigt einige der häufigsten Fallstricke in JavaScript und wie man sie vermeiden kann.

### var und Assignment ohne Deklaration

In älterem JavaScript-Code wurden Variablen oft mit dem Schlüsselwort `var` deklariert. Im Gegensatz zu `let` und `const`, die du bereits kennengelernt hast, kann sich `var` auf verwirrende Weise verhalten.
+
Zum Beispiel:

```javascript
{
  var message = "hello"
}
console.log(message)
```

Man könnte erwarten, dass `message` nur innerhalb des Blocks existiert, aber das ist nicht der Fall. `var` ignoriert den Block-Scope und macht die Variable in der gesamten Funktion oder Datei verfügbar.

Dies kann zu unerwartetem Verhalten führen, besonders in größeren Programmen. Aus diesem Grund sollte moderner JavaScript-Code immer `let` oder `const` anstelle von `var` verwenden.

Schlimmer noch, in JavaScript kannst du Variablen Werte zuweisen, **ohne sie überhaupt zu deklarieren**:

```javascript
function greet() {
  user = "Alice"
}
greet()
console.log(user) // prints "Alice"
```

Dadurch wird eine neue globale Variable `user` ohne jegliche Deklaration erstellt. Dies kann unbemerkt geschehen und zu Fehlern führen, die schwer aufzuspüren sind, besonders wenn es nur ein Tippfehler war. Deklariere Variablen immer mit `let` oder `const`.

### Schwaches Typensystem

JavaScript ist schwach typisiert, d.h. es konvertiert bei Bedarf automatisch Werte von einem Typ in einen anderen. Dies wird Typzwang genannt, und obwohl es bequem sein kann, führt es oft zu verwirrenden Ergebnissen.

Zum Beispiel:

```javascript
console.log("5" + 1)    // "51"
console.log("5" - 1)    // 4
console.log(true + 1)   // 2
console.log(null + 1)   // 1
```

In diesen Beispielen versucht JavaScript zu erraten, was du gemeint hast. Manchmal verwandelt es Zeichenketten in Zahlen, Boolesche Werte in Zahlen oder Zahlen in Zeichenketten. Dies kann dazu führen, dass sich dein Code auf unerwartete Weise verhält.

Es ist wichtig, sich des schwachen Typisierungssystems von JavaScript bewusst zu sein. Wenn Dinge anfangen, sich seltsam zu verhalten, kann das an unerwarteter Typenkonvertierung liegen.

### "use strict"

Du kannst einen strengeren Modus aktivieren, der einige stille Fehler zu echten Fehlern macht und dich davon abhält, einige der gefährlicheren Funktionen der Sprache zu verwenden.

Um diesen strengeren Modus zu aktivieren, füge diese Zeile am Anfang deiner Datei oder Funktion ein:

```javascript
"use strict"
```

Zum Beispiel:

```javascript
"use strict"
name = "Alice" // ReferenceError: name is not defined
```

Ohne den strikten Modus würde JavaScript stillschweigend eine globale Variable mit dem Namen `name` erstellen. Im strikten Modus wird dies jedoch zu einem echten Fehler, so dass du Fehler früher erkennen kannst.

Im strikten Modus werden auch einige veraltete JavaScript-Funktionen deaktiviert, und dein Code lässt sich leichter optimieren und warten.

## Wert vs. Referenz
<chapterId>bb898425-dc2f-5e5c-864b-0cb7a4a9aea9</chapterId>

JavaScript behandelt verschiedene Arten von Werten auf unterschiedliche Weise.

Einige Werte werden **kopiert**, wenn du sie einer Variablen zuweist.

Andere werden **geteilt**, wenn du sie einer neuen Variablen zuweist. Wenn du also eine Variable änderst, ändert sich auch die andere.

### Übergabe als Wert (`pass by value`)

Wenn ein Wert **als Wert** (`by value`) übergeben wird, erstellt JavaScript eine **Kopie** des Wertes.

Wenn du also das eine änderst, hat das keine Auswirkungen auf das andere.

Dies geschieht mit primitiven Typen, wie:

* *numbers*
* *strings*
* *booleans* (`true` und `false`)
* `null`
* `*undefined*`

Schauen wir uns ein Beispiel an:

```javascript
let a = 5
let b = a

b = 10

console.log(a) // 5
console.log(b) // 10
```

Wir haben `b` den Wert von `a` gegeben, aber dann haben wir `b` in `10` geändert.

Da Zahlen nach Wert übergeben werden, kopiert JavaScript die `5` in `b`. Die `5` in `b` ist unabhängig von der ursprünglichen `5` in `a`, so dass eine Änderung des Wertes von `b` keine Auswirkungen auf `a` hat.

Versuchen wir es mit einer Zeichenkette:

```javascript
let name1 = "Alice"
let name2 = name1

name2 = "Bob"

console.log(name1) // Alice
console.log(name2) // Bob
```

Auch hier hatte die Änderung von `name2` keine Auswirkungen auf `name1`, da Zeichenketten auch als Wert übergeben werden.

Das Gleiche passiert, wenn du ein Primitiv an eine Funktion übergibst: Es wird kopiert. Die Funktion kann also das Original nicht ändern.

```javascript
function plusOne(x) {
  x = x + 1
}

let number = 5

plusOne(number)

console.log(number) // 5
```

Obwohl innerhalb der Funktion `1` zu `x` hinzugefügt wurde, hat sich die ursprüngliche `number` nicht geändert.

Das liegt daran, dass nur eine **Kopie** an die Funktion übergeben wurde.

### Übergabe als Referenz (`pass by reference`)

Objekte werden **als Referenz** (`by reference`) übergeben.

Das heißt, anstatt sie zu kopieren, übergibt JavaScript einfach einen **Verweis** auf sie, und wenn du sie änderst, sehen alle anderen Variablen, die auf sie zeigen, die Änderung ebenfalls.

Zum Beispiel:

```javascript
const person1 = { name: "Alice" }
const person2 = person1

person2.name = "Bob"

console.log(person1.name) // Bob
console.log(person2.name) // Bob
```

Sowohl `person1` als auch `person2` zeigen auf dasselbe Objekt im Speicher.

Als wir also `person2.name` geändert haben, haben wir auch `Person1.name` geändert, weil sie beide dasselbe betrachten.

Arrays sind Objekte, also versuchen wir das Gleiche mit einem Array:

```javascript
const list1 = [1, 2, 3]
const list2 = list1

list2.push(4)

console.log(list1) // [1, 2, 3, 4]
console.log(list2) // [1, 2, 3, 4]
```

Wir haben `4` in `list2` geschoben, aber `list1` war auch betroffen, weil beide auf dasselbe Array verweisen.

Schauen wir uns an, was passiert, wenn wir ein Objekt an eine Funktion übergeben:

```javascript
function rename(user) {
  user.name = "Charlie"
}

const person = { name: "Dana" }

rename(person)

console.log(person.name) // Charlie
```

Die Funktion hat das Objekt geändert! Das liegt daran, dass sie eine **Referenz** auf das ursprüngliche Objekt `person` erhalten hat.

Sie hat keine Kopie erhalten. Sie erhielt Zugriff auf das Originalobjekt und damit die Möglichkeit, es zu verändern.

Es ist wichtig, sich diese Unterscheidung zu merken, denn sonst könnte sich unser Code anders verhalten, als wir es erwarten. Wir könnten zum Beispiel eine Funktion mit der Erwartung schreiben, dass sie die Argumente, die sie erhält, nicht verändert, und später herausfinden, dass sie sie tatsächlich verändert hat (weil es Objekte waren, also per Referenz übergeben wurden).

## Arbeiten mit Funktionen
<chapterId>e0d277a8-c642-5af7-9e53-dee27c811967</chapterId>

Du hast bereits gelernt, wie man Funktionen in JavaScript deklariert und verwendet. Aber JavaScript gibt dir noch mehr Werkzeuge an die Hand, um mit Funktionen auf leistungsstarke Weise zu arbeiten.

### Pfeil-Funktionen (`arrow functions`)

Pfeilfunktionen sind eine kürzere Art, Funktionen zu schreiben. Statt des Schlüsselworts `function` wird ein Pfeil (`=>`) verwendet.

Hier ist eine normale Funktion:

```javascript
function greet(name) {
  return `Hello, ${name}!`
}
```

Die Pfeilversion sieht wie folgt aus:

```javascript
const greet = (name) => {
  return `Hello, ${name}!`
}
```

Wenn die Funktion **nur eine Zeile** hat, kannst du die geschweiften Klammern und `return` weglassen:

```javascript
const greet = (name) => `Hello, ${name}!`
```

Wenn die Funktion **nur einen Parameter** hat, kannst du sogar die Klammern um die Parameter weglassen:

```javascript
const greet = name => `Hello, ${name}!`
```

Pfeilfunktionen sind in modernem JavaScript sehr verbreitet, da sie es erlauben, einfache Funktionen mit deutlich weniger Standard-Code auszudrücken.

### Standard-Parameter

Manchmal soll eine Funktion einen **Standardwert** haben, wenn kein Argument übergeben wird.

Das kann man so machen:

```javascript
function sayHello(name = "friend") {
  console.log(`Hello, ${name}!`)
}

sayHello("Alice") // Hello, Alice!
sayHello()        // Hello, friend!
```

Der Standardwert `"friend"` wird verwendet, wenn nichts übergeben wird.

### Spread-Parameter (...)

Was, wenn Ihre Funktion eine flexible Anzahl von Argumenten benötigt?

Du kannst den **Spread-Operator** (`...`) verwenden, um sie in einem Array zu sammeln:

```javascript
function logAll(...items) {
  console.log(items)
}

logAll(1, 2, 3) // [1, 2, 3]
logAll("a", "b") // ["a", "b"]
```

Du kannst dann eine Schleife verwenden, um jedes Element zu verarbeiten:

```javascript
function logEach(...items) {
  for (const item of items) {
    console.log(item)
  }
}
```

Der Spread-Operator ist nützlich, wenn du nicht weißt, wie viele Argumente übergeben werden.

### Funktionen höherer Ordnung

Eine **Funktion höherer Ordnung** ist eine Funktion, die:


* eine andere Funktion als Eingabe nimmt *und/oder*
* eine Funktion als Ausgabe zurück gibt.

Hier ist ein einfaches Beispiel:

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

Dies wird ausgegeben:

```
Hello, friend!
Hello, friend!
```

Wir können eine Pfeilfunktion an sie übergeben:

```javascript
runTwice(
  () => console.log("Hello!")
)
```

Dies wird ausgegeben:

```
Hello!
Hello!
```

Du kannst auch Funktionen schreiben, die andere Funktionen **zurückgeben**:

```javascript
function makeGreeter(name) {
  return () => console.log(`Hi, ${name}`)
}

const greetAlice = makeGreeter("Alice")
const greetBob = makeGreeter("Bob")

greetAlice() // Hi, Alice
greetBob() // Hi, Bob
```

Die Funktion `makeGreeter` ist eine Funktion, die andere Funktionen baut. Sie empfängt eine Zeichenkette und gibt eine neue Funktion zurück, die diese Zeichenkette in ihrem `console.log`-Aufruf verwendet.

Diese Art von Muster ist sehr leistungsfähig, da sie es dir ermöglicht, "Löcher" in deinen Funktionen zu hinterlassen, die du später mit dem benötigten Verhalten füllen kannst.

### map(), filter(), reduce()

JavaScript bietet dir einige nützliche integrierte Methoden zur Verwendung mit Arrays.

Diese Methoden nehmen Funktionen als Argumente an, sie sind also auch Funktionen höherer Ordnung.

`map()` wandelt jedes Element in einem Array in etwas anderes um.

Beispiel:

```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map(x => x * 2)

console.log(doubled) // [2, 4, 6]
```

Jede Zahl wird verdoppelt, und das Ergebnis ist ein neues Feld.

`filter()` entfernt Elemente aus dem Array, wenn sie einen Test nicht bestehen.

Beispiel:

```javascript
const numbers = [1, 2, 3, 4, 5]
const numbersGreaterThanTwo = numbers.filter(x => x > 2)

console.log(numbersGreaterThanTwo) // [3, 4, 5]
```

Nur die Array-Einträge, für die die Bedingung `x > 2` "wahr" ist, werden beibehalten.

`reduce()` wird verwendet, um alle Elemente in einem Array zu einem einzigen Wert zu kombinieren.

Beispiel:

```javascript
const numbers = [1, 2, 3, 4]
const total = numbers.reduce((current, next) => current + next)

console.log(total) // 10
```

`reduce` durchläuft das Array und wendet in diesem Beispiel den `+` Operator zwischen `1` und `2` an, dann zwischen dem resultierenden `3` und `3`, dann zwischen dem resultierenden `6` und `4`, bis es die Summe aller Array-Einträge hat (was 10 ist).

Du kannst `reduce()` für viele Dinge verwenden, wie z.B. Summen, Durchschnittswerte oder schrittweises Erzeugen neuer Werte.

Diese Methoden (`map`, `filter`, `reduce`) sind leistungsfähige Werkzeuge, um Daten zu verarbeiten, ohne manuelle Schleifen zu schreiben.

Du kannst sie sogar in einer Kette von Vorgängen kombinieren, etwa so:

```javascript
const numbers = [1, 2, 3, 4, 5]

const result = numbers
  .map(n => n * 2)    // Verdoppele jeden Eintrag, ergibt [2, 4, 6, 8, 10]
  .filter(n => n > 3) // Behalte nur Werte größer 3, es bleiben also [4, 6, 8, 10]
  .reduce((n1, n2) => n1 + n2) // Addiere sie zusammen: 4 + 6 + 8 + 10 = 28

console.log(result) // 28
```

## Arbeiten mit Objekten
<chapterId>7842aada-f009-5518-b8e3-1104e166a035</chapterId>

In diesem Kapitel lernen wir einige leistungsfähige und etwas fortgeschrittenere Werkzeuge für die Arbeit mit Objekten in JavaScript kennen.

### Private Eigenschaften

Manchmal möchte man eine Eigenschaft eines Objekts ausblenden, damit sie nicht geändert oder von außerhalb des Objekts aufgerufen werden kann. JavaScript gibt uns eine Möglichkeit, dies zu tun, indem wir `#` vor dem Eigenschaftsnamen schreiben. Dadurch wird eine **private** Eigenschaft erzeugt, auf die nur von innerhalb der Klasse zugegriffen werden kann.

```javascript
class Person {
  #age // dies ist eine private Eigenschaft

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
console.log(alice.getAge())  // 30, die Methode kann auf die private Eigenschaft zugreifen
console.log(alice.#age)      // ❌ Error! Man kann auf private Eigenschaften nicht direkt zugreifen
```

Private Eigenschaften sind hilfreich, wenn man versehentliche Änderungen verhindern will.

### statische Eigenschaften

Manchmal möchte man, dass eine Eigenschaft zur Klasse selbst gehört und nicht zu jedem Objekt, das man aus dieser Klasse erstellt. Dafür ist `static` ("statisch") gedacht. Eine "statische" Eigenschaft ist in der Klasse enthalten und alle Objekte dieser Klasse verweisen auf sie.

```javascript
class User {
  static counter = 0 // dies gehört zur Klasse, nicht den Instanzen. Der gleiche Zählerwert wird zwischen allen Objekten geteilt.

  constructor() {
    User.counter++ // Ändert den Wert der statischen Eigenschaft jedes Mal wenn ein Objekt dieser Klasse erzeugt wird
  }
}

const a = new User() // der Konstruktor wird den Wert des geteilten Zählers von 0 auf 1 ändern
const b = new User() // der Konstruktor wird den Wert des geteilten Zählers von 1 auf 2 ändern

console.log(User.counter) //  gibt 2 aus
```

Dies ist nützlich für die Speicherung gemeinsamer Daten und Methoden, die für die gesamte Gruppe von Objekten gelten, nicht nur für ein einzelnes.

### get und set

In JavaScript kannst du mit `get` und `set` Eigenschaften erstellen, die wie normale Variablen aussehen, aber im Hintergrund speziellen Code ausführen.

Eine `get`ter-Methode wird ausgeführt, wenn du versuchst, eine Eigenschaft zu *lesen*. Sie wird deklariert, indem man "get" vor eine Methode mit dem Namen der Eigenschaft schreibt.

```javascript
class User {
constructor(firstName,  lastName) {
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

Obwohl `fullName` keine reguläre Eigenschaft ist, können wir sie wie eine solche verwenden, und hinter den Kulissen wird die zugehörige `get`-Funktion ausgeführt, um den vollständigen Namen zu ermitteln.

Eine `set`er-Methode wird ausgeführt, wenn du einer Eigenschaft einen Wert *zuweist*. Damit kannst du kontrollieren, was passiert, wenn jemand versucht, diesen Wert zu ändern. Sie wird deklariert, indem man `set` vor eine Methode mit dem Namen der Eigenschaft schreibt.

```javascript
class User {
  constructor() {
    this.firstName = "John"
    this.lastName = "Doe"
  }

  get fullName() {
    return `${this.firstName} ${this.lastName}`
  }

  set fullName(input) {            // nimmt den Namen der übergeben wird
    const parts = input.split(" ") // zerlegt ihn in Teile
    this.firstName = parts[0]      // nimmt den ersten Teil als firstName
    this.lastName = parts[1]       // nimmt den zweiten Teil als secondName
  }
}

const user = new User()
user.fullName = "John Smith"

console.log(user.firstName) // John
console.log(user.lastName)  // Smith
```

Wenn wir `user.fullName = "John Smith"` eingeben, wird die `set`er-Methode ausgeführt und die Werte `firstName` und `lastName` werden aktualisiert.

Auch wenn es so aussieht, als würden wir nur eine einfache Variable setzen, lösen wir tatsächlich eine Logik aus, die andere Eigenschaften aktualisiert.

## Schlüssel und Werte
<chapterId>01a397b8-c12a-5c39-82b3-6d9ebbb72a29</chapterId>

Jede Eigenschaft in einem JavaScript-Objekt hat einen **Schlüssel** (auch Eigenschaftsname genannt) und einen **Wert**.

Zum Beispiel:

```javascript
const user = {
  name: "Alice",
  age: 30
}
```

In diesem Objekt sind `name` und `age` die Schlüssel, und `Alice` und `30` sind ihre Werte.

### Dynamischer Zugriff

Manchmal kennt man den Namen einer Eigenschaft nicht im Voraus... vielleicht erhalten wir ihn aus einer Benutzereingabe oder wir lesen ihn aus einer Variablen. Du kannst trotzdem darauf zugreifen, indem du die **Klammerschreibweise** verwenden, z. B. `MeinObjekt["Schlüsselname"]`.

```javascript
const user = {
  name: "Alice",
  age: 30
}

console.log(user["name"]) // Alice
```

Wir haben die Zeichenkette `name` an das Objekt übergeben, um den entsprechenden Wert zu erhalten.

Wir können einen Schlüssel in einer Variablen speichern und ihn später für den Zugriff auf den entsprechenden Wert verwenden, z.B.:

```javascript
const user = {
  name: "Alice",
  age: 30
}

const key = "name"

console.log(user[key]) // Alice
```

### Dynamische Zuweisung

Du kannst auch Objekteigenschaften mit Variablen als Schlüssel erstellen oder aktualisieren.

```javascript
const settings = {}

const key = "theme"
settings[key] = "dark"

console.log(settings) // { theme: "dark" }
```

Dies ist hilfreich, wenn du ein Objekt Schritt für Schritt aufbauen willst. Zum Beispiel:

```javascript
const user = {}

user["username"] = "bananaFan123"
user["email"] = "banana@fruit.com"

console.log(user)
// { username: "bananaFan123", email: "banana@fruit.com" }
```

Du kannst sogar einen dynamischen Schlüssel *bei der Erstellung* des Objekts in eckigen Klammern verwenden:

```javascript
const key = "language"
const config = {
  [key]: "JavaScript"
}

console.log(config.language) // JavaScript
```

Dies wird als **berechnete Eigenschaft** (computed property) bezeichnet. Der Wert innerhalb der eckigen Klammern wird ausgewertet, und das Ergebnis wird als Schlüssel verwendet.

### Symbol Typ

Neben Zeichenketten kannst du in JavaScript auch einen speziellen Typ namens `Symbol` als Objektschlüssel verwenden.

Lass uns mit einem einfachen Beispiel beginnen:

```javascript
const id = Symbol("userID")

const user = {
  name: "Bob",
  [id]: 12345
}

console.log(user[id]) // 12345
```

In diesem Beispiel ist `id` ein Symbol. Es ist keine Zeichenkette, aber es funktioniert trotzdem als Schlüssel. Wenn du versuchst, `user` auf der Konsole auszugeben, wirst du dies sehen:

```javascript
console.log(user) // { name: 'Bob', [Symbol(userID)]: 12345 }
```

Ein weiterer wichtiger Punkt: Jedes von dir erstellte Symbol ist einzigartig, auch wenn es mit derselben Zeichenfolge erstellt wird.

```javascript
const a = Symbol("label")
const b = Symbol("label")

console.log(a === b) // false
```

Mit Symbolen kannst du Schlüssel definieren, die nicht mit regulären Schlüsseln kollidieren. Nehmen wir an, wir haben ein Objekt mit der Eigenschaft `name`, aber das Objekt wird in der Zukunft von einem Benutzer in einer für uns nicht vorhersehbaren Weise angepasst werden können, und dieser Benutzer könnte auch eine Eigenschaft `name` hinzufügen. Wenn die ursprüngliche Eigenschaft `name` mit einer Zeichenkette definiert wurde, würde sie durch die neue Eigenschaft überschrieben werden, etwa so:

```javascript
const obj = {
  name: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy' }
```

Wenn wir stattdessen ein Symbol verwenden:

```javascript
const name = Symbol("name")

const obj = {
  [name]: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy', [Symbol(name)]: 'John' }
```

Wie du sehen kannst, bleibt die ursprüngliche Eigenschaft `name` auf diese Weise erhalten. Dies kann in bestimmten Sonderfällen nützlich sein.

## Utility-Objekte
<chapterId>516e74c8-2a11-545a-a4d1-c2cabb91a273</chapterId>

JavaScript gibt uns einige nützliche eingebaute Objekte, die uns helfen, Dinge wie Debugging und mathematische Operationen durchzuführen.

### Andere Konsolen-Methoden

Du hast bereits die Datei `console.log` gesehen, die Werte auf dem Bildschirm ausgibt.

Es gibt einige andere nützliche Methoden, die für das `console`-Objekt verfügbar sind und die dir bei der Fehlersuche in deinen Programmen helfen können.

#### `console.warn`

Gibt eine Meldung in gelber Farbe aus (oder mit einem Warnsymbol in einigen Umgebungen):

```javascript
console.warn("This is just a warning.")
```

#### `console.error`

Erzeugt eine Meldung in Rot, wie bei einem Fehler:

```javascript
console.error("Something went wrong!")
```

#### `console.table`

Zeigt ein Array oder Objekt als Tabelle an:

```javascript
const users = [
  { name: "Alice", age: 25 },
  { name: "Bob", age: 30 }
]

console.table(users)
```

Dies gibt eine Tabelle aus, wie:

```
┌─────────┬────────┬─────┐
│ (index) │  name  │ age │
├─────────┼────────┼─────┤
│    0    │ 'Alice'│  25 │
│    1    │ 'Bob'  │  30 │
└─────────┴────────┴─────┘
```

Dies kann nützlich sein, um strukturierte Daten zu visualisieren.

#### `console.time` und `console.timeEnd`

Man kann messen, wie lange etwas dauert:

```javascript
console.time("timer")
for (let i = 0; i < 1000000; i++) {}
console.timeEnd("timer")
```

Dies ergibt etwas wie:

```
timer: 2.379ms
```

Nützlich für einige einfache Leistungstests.

### Das Math-Objekt 

JavaScript gibt dir ein `Math`-Objekt mit nützlichen Methoden für Berechnungen.

#### `Math.random()`

Gibt eine Zufallszahl zwischen 0 (einschließlich) und 1 (ausschließlich) zurück:

```javascript
const r = Math.random()
console.log(r)
```

Beispielhafte Ausgabe:

```
0.4387429859
```

#### `Math.floor()` und `Math.ceil()`


* math.floor(n)` rundet **abwärts** auf die nächste Ganzzahl
* math.ceil(n)` rundet **auf** die nächste Ganzzahl

```javascript
console.log(Math.floor(4.9)) // 4
console.log(Math.ceil(4.1))  // 5
```

#### `Math.round()`

Rundet auf die nächstliegende Ganzzahl:

```javascript
console.log(Math.round(4.4)) // 4
console.log(Math.round(4.6)) // 5
```

#### `Math.max()` und `Math.min()`

Gibt den größten oder kleinsten Wert aus einer Liste von Zahlen zurück:

```javascript
console.log(Math.max(5, 9, 3)) // 9
console.log(Math.min(5, 9, 3)) // 3
```

#### `Math.pow()` und `Math.sqrt()`


* `Math.pow(a, b)` gibt dir `a` hoch `b`
* `Math.sqrt(n)` liefert die Quadratwurzel aus `n`

```javascript
console.log(Math.pow(2, 3))   // 8
console.log(Math.sqrt(16))    // 4
```

# Fortgeschrittenes JavaScript
<partId>72c30671-ca20-5617-92a5-d5ba7aa38c93</partId>

## Andere Sammlungs-Typen
<chapterId>a9a70c6d-a343-5a46-a383-e288bc2700e3</chapterId>

JavaScript bietet uns einige spezielle Typen für Auflistungen von Objekten, die über normale Arrays und Objekte hinausgehen. Dazu gehören `Map` und `Set`.

Sie helfen dir bei der Speicherung und Verwaltung von Wertegruppen, funktionieren aber anders als bisher gelernt.

Eine `Map` ist eine Sammlung von **Schlüssel-Wert-Paaren**, genau wie ein Objekt. Aber es gibt einige wichtige Unterschiede:


* Die Schlüssel können **beliebige Werte** sein, nicht nur Zeichenketten.
* Die Reihenfolge der Elemente bleibt erhalten.
* Sie verfügt über eingebaute Methoden, die das Arbeiten mit ihr erleichtern.

Du erstellst eine neue `Map` wie folgt:

```javascript
const myMap = new Map()
```

Dies erzeugt eine leere `Map`. Um ihr Einträge hinzuzufügen, verwenden wir `myMap.set(key, value)`:

```javascript
myMap.set("name", "Alice")
```

Dies fügt einen Schlüssel `"name"` mit dem Wert `"Alice"` hinzu.

Du kannst auch eine Nummer als Schlüssel verwenden:

```javascript
myMap.set(42, "The answer")
```

Und sogar ein Objekt als Schlüssel:

```javascript
const objKey = { id: 1 }
myMap.set(objKey, "Object as key")
```

Das würde mit regulären Objekten, die nur String-Schlüssel zulassen, nicht funktionieren.

Um einen **Wert zu erhalten**, verwenden wir `myMap.get(key)`:

```javascript
console.log(myMap.get("name"))     // Alice
console.log(myMap.get(42))         // Die Antwort
console.log(myMap.get(objKey))     // Objekt als key
```

Um **zu prüfen, ob ein Schlüssel existiert**, verwenden wir `myMap.has(key)`:

```javascript
console.log(myMap.has("name")) // true
```

Um einen Schlüssel zu **entfernen**, verwenden wir `myMap.delete(key)`:

```javascript
myMap.delete("name")
```

Um **die gesamte Map** zu löschen, verwenden wir `myMap.clear()`:

```javascript
myMap.clear()
```

Maps eignen sich hervorragend für die Verwaltung großer Wertesammlungen, da der Zugriff auf Werte in einer großen Map in der Regel wesentlich leistungsfähiger ist als auf ein großes Objekt.

### Set

Eine Menge (`Set`) ist eine Sammlung **ausschließlich von Werten** (keine Schlüssel), wobei jeder Wert **einzigartig** sein muss. Das bedeutet:


* Man kann denselben Wert nicht zweimal haben
* Die Werte werden in der Reihenfolge gespeichert, in der du sie hinzufügst

Du erstellst eine Menge wie folgt:

```javascript
const mySet = new Set()
```

Um **Werte** hinzuzufügen, verwenden wir `mySet.add(value)`:

```javascript
mySet.add(1)
mySet.add(2)
mySet.add(2) // Duplikat, wird ignoriert
```

Auch wenn wir versucht haben, `2` zweimal hinzuzufügen, wird die Menge nur eine Kopie behalten.

Um **zu prüfen, ob ein Wert in der Menge** enthalten ist, verwenden wir `mySet.has(value)`:

```javascript
console.log(mySet.has(2)) // true
console.log(mySet.has(3)) // false
```

Zum **Entfernen eines Wertes** verwenden wir `mySet.delete(value)`:

```javascript
mySet.delete(2)
```

Um **alles** zu löschen, verwenden wir `mySet.clear()`:

```javascript
mySet.clear()
```

Eine Menge (`Set`) ist nützlich, wenn du eine Sammlung eindeutiger Werte aufbewahren willst, ohne manuell nach Duplikaten suchen zu müssen:

```javascript
const numberArray = [1, 2, 2, 3, 4, 4, 4, 5]

const numberSet = new Set(numberArray)

console.log(numberSet) // Set(5) { 1, 2, 3, 4, 5 }
```

Das `Set` vermeidet die Duplikate für dich.

## Iteratoren
<chapterId>61d24e5e-b7e4-541a-8322-778f61f26a72</chapterId>

Die meisten Dinge in JavaScript, über die man eine Schleife ziehen kann (wie Arrays, Strings, Maps, Sets), sind **iterierbar**: Du kannst Iteratoren für ihren Inhalt erstellen.

Ein **Iterator** ist ein spezielles Objekt in JavaScript, mit dem du eine Liste von Elementen **einmal** durchgehen kannst.

### Objekt-Iteratoren

Anders als Arrays oder Maps sind reguläre Objekte **nicht iterierbar** mit `for...of`. Wenn du dies versuchst:

```javascript
const user = {
  name: "Alice",
  age: 30
}

for (const value of user) {
  console.log (value)
}
```

wirst du eine Fehlermeldung erhalten:

```
TypeError: user is not iterable
```

Das liegt daran, dass einfache Objekte keinen eingebauten Iterator haben. Aber JavaScript gibt dir andere Werkzeuge, um über sie zu iterieren.

#### `Object.keys()`

Du kannst `Object.keys(obj)` verwenden, um ein Array mit den **Schlüsseln** des Objekts zu erhalten, und dann eine Schleife darüber laufen zu lassen:

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

Dies wird ausgegeben:

```
name
age
```

#### `Object.values()`

Um eine Schleife über die **Werte** zu laufen, verwende `Object.values()`:

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

Dies wird ausgegeben:

```
Alice
30
```

#### `Object.entries()`

Wenn du **sowohl den Schlüssel als auch den Wert** benötigst, verwende `Object.entries()`:

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

Dies wird ausgegeben:

```
name is Alice
age is 30
```

Auch wenn Objekte nicht direkt iterierbar sind, geben diese Methoden vollen Zugriff auf ihren Inhalt in einer Art und Weise, die gut mit `for...of` funktioniert.

Aber wie funktionieren Iteratoren?

### Symbol.Iterator

Das Geheimnis hinter allen Iterierables ist ein spezielles **Symbol** namens `Symbol.iterator`.

Dieses Symbol ist ein eingebauter Schlüssel, der JavaScript mitteilt: "Dieses Objekt kann iteriert werden"

Wenn du `myIterable[Symbol.iterator]()` aufrufst, erhältst du von JavaScript ein **Iterator-Objekt** mit einer Methode `.next()` zurück.

Schauen wir mal, wie das aussieht:

```javascript
const colors = ["red", "green", "blue"]

const iterator = colors[Symbol.iterator]()

console.log(iterator.next()) // { value: 'red', done: false }
```

Jeder Aufruf von `.next()` gibt dir den nächsten Wert. Wenn er fertig ist, gibt er:

```javascript
{ value: undefined, done: true }
```

zurück.

### next()

Die Methode `.next()` wird verwendet, um das nächste Element der Sequenz zu erhalten.

Jedes Mal, wenn du `.next()` aufrufst, erhältst du ein Objekt mit zwei Schlüsseln:


* `value`: das aktuelle Element
* `done`: ein boolescher Wert, der angibt, ob die Iteration beendet ist

Lass uns ein vollständiges Beispiel machen:

```javascript
const names = ["Lina", "Tom", "Eva"]      // Lege ein Array an
const iterator = names[Symbol.iterator]() // nutze die Symbol.iterator Funktion um einen iterator für das Array zu erhalten

let result = iterator.next()              // nimm das erste Element des Array

while (!result.done) {                    // wiederhole diese Schleife bis zum letzten Element im Array, was durch { done: true } gekennzeichnet ist
  console.log(result.value)               // gibt den Wert jeden Elementes aus
  result = iterator.next()                // nimm das nächste Array-Element
}
```

Dies wird ausgegeben:

```
Lina
Tom
Eva
```

So funktioniert eine `for...of`-Schleife unter der Haube: Sie verwendet dieses Muster mit `.next()`.

Das gleiche Ergebnis erhalten wir mit

```javascript
const names = ["Lina", "Tom", "Eva"]

for (const result of names) {
  console.log(result)
}
```

### Eine Klasse iterierbar machen

Du kannst auch deine eigene **iterable-Klasse** definieren, indem du eine `[Symbol.iterator]()` Methode hinzufügst.

Nehmen wir an, wir wollen eine Klasse, die einen **Zahlenbereich** darstellt, etwa von 1 bis 5.

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

Dies wird ausgegeben:

```
1
2
3
4
5
```

Hierbei geschieht Folgendes:


* Wir haben eine Klasse `Range` definiert
* Innerhalb der Klasse haben wir `[Symbol.iterator]()` implementiert, damit JavaScript weiß, wie man es durchläuft
* Die Methode `next()` gibt jede Zahl einzeln zurück
* Wenn wir das "Ende" (`end`) erreichen, gibt sie `{ done: true }` zurück

Jetzt funktioniert unsere Klasse `Range` wie ein Array, und wir können es in jeder Schleife verwenden, die eine Iterable erwartet.

### Generatorfunktionen und `yield`

Um die Erstellung von Iteratoren zu vereinfachen, gibt es in JavaScript **Generatorfunktionen**, die das Schlüsselwort `function*` (das ist `function` mit einem `*` am Ende) und das Schlüsselwort `yield` verwenden.

Versuchen wir es:

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

Jedes `yield` gibt einen Wert zurück und **pausiert** die Funktion, bis das nächste `.next()` aufgerufen wird.

Du kannst auch mit `for...of` eine Schleife über einen Generator ziehen:

```javascript
for (const num of numberGenerator()) {
  console.log(num)
}
```

Dies wird ausgegeben:

```
1
2
3
```

## Nebenläufigkeit mit Callbacks
<chapterId>f3fc76ca-b3ef-54eb-a06e-501007002054</chapterId>

Bis jetzt war unser Code **synchron**: Er läuft eine Zeile nach der anderen ab, der Reihe nach. Aber einige Dinge in der realen Welt brauchen Zeit, und wir wollen nicht, dass das gesamte Programm während des Wartens pausiert.

In diesem Kapitel werden wir ein neues Konzept einführen: **Nebenläufigkeit**. Es erlaubt uns, die Reihenfolge, in der Dinge erledigt werden, zu manipulieren. Das ist nützlich, wenn wir mit Dingen wie Timern, Benutzereingaben oder dem Lesen von Dateien von der Festplatte umgehen. JavaScript bietet verschiedene Werkzeuge für die Nebenläufigkeit.

### setTimeout

Mit der Funktion `setTimeout` kannst du eine Funktion **später** ausführen, nachdem eine gewisse Zeit vergangen ist.

Beispiel:

```javascript
console.log("Start")

setTimeout(
  () => console.log("This runs after 2 seconds"),
  2000
)

console.log("End")
```

Dies wird ausgegeben:

```
Start
End
This runs after 2 seconds
```

Obwohl `setTimeout` in der Mitte des Codes erscheint, blockiert es nicht den Rest. Stattdessen wird die Funktion für eine **spätere** Ausführung eingeplant und der restliche Code sofort fortgesetzt.

Die `2000` bedeuten 2000 Millisekunden (das sind 2 Sekunden).

Hier ist eine ausführliche und anfängerfreundliche Neufassung der Abschnitte **Callbacks** und **Promises**, die durchgängig Datenmanipulation und klare Anmerkungen verwendet:

### Callbacks

Ein **Callback** ist einfach eine Funktion, die wir einer anderen Funktion übergeben, damit sie später **aufgerufen** (bzw. zurückgerufen) werden kann.

Schauen wir uns ein reales Beispiel mit Zahlen an. Stell dir vor, wir haben eine Liste von Zahlen und wollen jede einzelne verdoppeln und dann eine Funktion (den Rückruf) auf das resultierende "verdoppelte" Array anwenden, aber wir wollen dies mit einer kleinen Verzögerung tun, als ob wir auf etwas Langsames warten würden (wie das Laden von Daten aus dem Internet).

Hier ist eine Funktion, die dies mit einem **Callback** erledigt:

```javascript
function doubleNumbers(numbersArray, callback) {
  // Wir tun mit setTimeout so, als ob wir eine langsame Operation ausführen
  setTimeout(() => {
    // Wir nutzen Map um ein neues Array zu erzeugen, in dem jede Zahl verdoppelt wurde
    const doubled = numbersArray.map(n => n * 2)

    // Wenn dies fertig ist, rufen die Callback-function mit dem Ergebnis auf
    callback(doubled)
  }, 1000) // Wir warten eine Sekunde bevor wir den obigen Code ausführen
}
```

Versuchen wir, diese Funktion zu nutzen:

```javascript
const input = [1, 2, 3]

doubleNumbers(input, function(result) {
  console.log("Here is the doubled array:", result)
})
```

Nach 1 Sekunde wird dies ausgedruckt:

```
Here is the doubled array: [ 2, 4, 6 ]
```

**Was passiert hier?**

1. Wir übergeben `input` als Liste von Zahlen, die wir verdoppeln wollen.
2. Wir übergeben auch eine **Callback-Funktion**, die dem Programm sagt, was es *nach* der Verdopplung tun soll.
3. Innerhalb von `doubleNumbers` simulieren wir eine Verzögerung mit `setTimeout`, dann führen wir die Verdopplung durch.
4. Sobald das erledigt ist, rufen wir den Callback auf dem resultierenden "verdoppelten" Array auf.

Diese Technik funktioniert, aber stellen Sie sich vor, Sie wollen danach **mehr Schritte** machen, z.B. kleine Zahlen herausfiltern und sie dann addieren. Dann müssten Sie mehre Rückrufe wie diesen **verschachteln**:

```javascript
doubleNumbers(input, function(doubled) {
    filterBigNumbers(doubled, function(filtered) {
      sumNumbers(filtered, function(total) {
        console.log("Final result:", total)
    })
  })
})
```

Das ist schwierig zu lesen und unübersichtlich. Dieser Stil wird **Callback-Hölle** genannt, und es ist genau das, wofür `Promise` geschaffen wurde, um es zu beheben.

## Nebenläufigkeit mit Versprechen (Promises)
<chapterId>30fddaca-729f-5c8d-bf86-8dfc7b3c9800</chapterId>

Ein Versprechen (`Promise`) ist ein eingebautes JavaScript-Objekt, das einen Wert darstellt, der **in der Zukunft bereit sein wird**.

Wir können ein Versprechen wie folgt erstellen:

```javascript
const promise = new Promise((resolve, reject) => {
  // Hier passiert etwas das lange dauert...

  resolve("It worked!") // Dies bedeutet: alles hat geklappt
})
```

Der Teil `new Promise()` erstellt das Versprechen.

Darin geben wir ihm eine Funktion mit zwei Parametern:


* `resolve` ist eine Funktion, die wir aufrufen, wenn alles erfolgreich war
* `reject` ist eine Funktion, die wir aufrufen, wenn etwas schief geht

Im obigen Beispiel lösen wir es einfach sofort mit der Meldung "Es hat geklappt" ("It worked!") auf.

### .then()

Um etwas zu tun, **nachdem** das Versprechen erfüllt ist, verwenden wir `.then()`:

```javascript
const promise = new Promise((resolve, reject) => {
  // Hier passiert etwas das lange dauert...

  resolve(100) // Dies bedeutet: alles hat geklappt
})

promise.then(result => {
  console.log("The result is:", result)
})
```

Dies wird ausgegeben:

```
The result is: 100
```

Der Wert, den wir an `resolve()` übergeben haben, wird als `result` an die Funktion in `.then()` gesendet.

Lass uns eine Aufgabe simulieren, die 2 Sekunden dauert, indem wir `setTimeout` verwenden:

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

Dieser wartet 2 Sekunden und gibt dann:

```
Done waiting!
```

aus.

### reject()

Schaffen wir ein Versprechen, das **nicht funktioniert**:

```javascript
const failingPromise = new Promise((resolve, reject) => {
  reject("Something went wrong")
})
```

Wenn wir nun `.then()` dafür verwenden, wird nichts passieren, weil `.then()` nur Erfolg behandelt.

Um Fehler zu behandeln, verwenden wir `.catch()`:

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

Dies führt zu dieser Ausgabe:

```
Caught an error: Something went wrong
```

Der an `reject()` übergebene Wert wird an die Funktion `.catch()` gesendet.

Erstellen wir ein Versprechen, das **manchmal funktioniert und manchmal nicht**, basierend auf einer Bedingung.

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

Jetzt können wir dies aufrufen und beide Fälle behandeln:

```javascript
checkNumber(5)
  .then(
    msg => console.log("Success:", msg)
  )
  .catch(
    err => console.log("Failure:", err)
  )
```

Dies wird ausgegeben:

```
Success: Positive number
```

Und wenn wir es mit einer anderen Zahl versuchen:

```javascript
checkNumber(-1)
  .then(
    msg => console.log("Success:", msg)
  )
  .catch(
    err => console.log("Failure:", err)
  )
```

wird dies ausgegeben:

```
Failure: Not a positive number
```

### Verkettung von Operationen mit Promise


Wir können unser früheres Beispiel mit `Promise` umschreiben, und es wird viel sauberer aussehen.

Beginnen wir damit, eine neue Version unserer Verdopplungsfunktion zu schreiben, aber diesmal gibt sie ein **Versprechen** (Promise) zurück:

```javascript
function doubleNumbers(numbers) {
  return new Promise(resolve => {
    // Warte 1 Sekunde vor der eigentlichen Operation
    setTimeout(() => {
      const doubled = numbers.map(n => n * 2)
      resolve(doubled) // Gib das Ergebnis mit resolve zurück
    }, 1000)
  })
}
```

Jetzt können wir mit `.then()` JavaScript mitteilen, was mit dem Ergebnis geschehen soll:

```javascript
function doubleNumbers(numbers) {
  return new Promise(resolve => {
    // Warte 1 Sekunde vor der eigentlichen Operation
    setTimeout(() => {
      const doubled = numbers.map(n => n * 2)
      resolve(doubled) // Gib das Ergebnis mit resolve zurück
    }, 1000)
  })
}

const input = [1, 2, 3]

doubleNumbers(input)
  .then(
    result => console.log("Doubled numbers:", result)
)
```

Dies wird ausgegeben:

```
Doubled numbers: [ 2, 4, 6 ]
```

Bislang funktioniert dies genauso wie die Callback-Version, aber der Code ist jetzt einfacher zu erweitern und zu lesen.

Nehmen wir an, wir wollen weitere Schritte hinzufügen:

1. Erstens: Verdoppele alle Zahlen
2. Dann werden Zahlen kleiner als 4 entfernt
3. Zum Schluss fügen wir sie alle zusammen

Wir können für jeden Schritt eine Funktion schreiben, die alle Versprechen verwendet:

```javascript
function doubleNumbers(numbers) {
  return new Promise(resolve => {
    // Warte 1 Sekunde vor der eigentlichen Operation
    setTimeout(() => {
      const doubled = numbers.map(n => n * 2)
      resolve(doubled) // Gib das Ergebnis mit resolve zurück
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

Jetzt können wir sie auf diese Weise miteinander **verketten**:

```javascript
const input = [1, 2, 3]

doubleNumbers(input)
  .then(filterBigNumbers)
  .then(sumNumbers)
  .then(
    result => console.log("Final result after all steps:", result)
  )
```

Dies wird ausgegeben:

```
Final result after all steps: 10
```

Schauen wir uns an, was hier passiert:

1. `doubleNumbers` verdoppelt das Array: `[2, 4, 6]`
2. `filterBigNumbers` entfernt alles ≤ 3: `[4, 6]`
3. `sumNumbers` addiert die verbleibenden Zahlen: `4 + 6 = 10`
4. Schließlich wird das Ergebnis ausgegeben.

Jedes `.then()` wartet, bis der Schritt vor ihm beendet ist. So können wir eine **Aktionskette** ohne Verschachtelung aufbauen. Das macht den Code lesbarer und einfacher zu debuggen.

## Nebenläufigkeit mit async/await
<chapterId>6e93d29f-c8bf-5fd1-a9c9-4e794ee6cbd0</chapterId>

Wir haben gesehen, wie `Promise`-Ketten uns helfen, die Callback-Hölle zu vermeiden, aber sie sind immer noch ein wenig schwierig zu lesen, wenn viele Schritte involviert sind.

An dieser Stelle kommen `async` und `await` ins Spiel. Sie ermöglichen es uns, asynchronen Code zu schreiben, **der wie synchroner Code aussieht**, was ihn leichter verständlich macht.

### Was ist async?

Wenn du das Schlüsselwort `async` vor eine Funktion schreibst, verpackt JavaScript den Rückgabewert der Funktion automatisch in eine Promise.

Schauen wir uns ein einfaches Beispiel an:

```javascript
async function greet() {
  return "hello"
}
```

Wenn du diese Funktion aufrufst:

```javascript
const result = greet()
console.log(result)
```

wirst du:

```
Promise { 'hello' }
```

als Ausgabe sehen.

Auch wenn wir nur eine Zeichenkette zurückgegeben haben, verwandelt JavaScript sie in ein Versprechen für uns. Du kannst den tatsächlichen Wert mit `.then()` wie folgt abrufen:

```javascript
greet().then( result => console.log(result) ) // prints "hello"
```

Oder Du kannst `await` verwenden...

### Was ist await?

Das Schlüsselwort `await` (warte ab) sagt JavaScript: "warte, bis dieses Versprechen erfüllt ist, und gib mir dann das Ergebnis."

Aber Du kannst "await" nur **innerhalb einer asynchronen Funktion** verwenden.

Lass uns das Beispiel unter Verwendung von `await` neu schreiben:

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

Jetzt können wir das Ergebnis so verwenden, als wäre es ein normaler Wert.

Lass uns jetzt etwas Nützlicheres tun.

### Simulation einer Verzögerung mit await

Wir werden eine einfache `wait`-Funktion erstellen, die eine Anzahl von Millisekunden als Argument nimmt und nach dieser Anzahl von Millisekunden einfach endet, ohne etwas anderes zu tun:

```javascript
function wait(ms) {
  return new Promise(resolve => {
    setTimeout(resolve, ms)
  })
}
```

Versuchen wir, es zu benutzen:

```javascript
async function test() {
  console.log("waiting 2 seconds...")
  await wait(2000)
  console.log("done waiting")
}

test()
```

Dies wird ausgegeben:

```
waiting 2 seconds...
done waiting
```

Du kannst dir `await` als "Pausiere hier, bis das Versprechen erfüllt ist, dann weiter" vorstellen

Dies ermöglicht es dir, Code in einer **von oben nach unten** Weise zu schreiben, der sich asynchron verhält, ohne `.then()` Aufrufe zu verketten.

### Warten auf Daten

Wiederholen wir unser vorheriges Beispiel, in dem wir Zahlen verdoppeln, dann filtern und dann summieren. Aber dieses Mal verwenden wir `async`/`await`.

Wir werden 3 Funktionen erstellen, die das Warten simulieren und Promises zurückgeben:

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

Schreiben wir nun eine `async`-Funktion, um sie zu kombinieren:

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

Dies wird ausgegeben:

```
Final result: 10
```

Dies ist viel einfacher zu lesen als die Verkettung von `.then()` oder die Verschachtelung von Rückrufen.

Es sieht aus wie ein normales Schritt-für-Schritt-Programm, verhält sich aber dennoch asynchron.

## Asynchrone Iteratoren
<chapterId>438b037d-9931-56d7-9052-7b4470f3c75b</chapterId>

Du hast bereits von **Iteratoren** gehört und wie wir `for...of` verwenden können, um über Arrays und andere iterierbare Dinge ein Schleife zu bauen.

Was aber, wenn die Daten, über die wir iterieren wollen, erst nach einiger Zeit eintreffen?

Manchmal wollen wir eine Schleife über Dinge ziehen, die **asynchron** ankommen, wie Nachrichten aus einem Chat, Zeilen aus einer Datei oder Zahlen aus einer langsamen Quelle.

Zu diesem Zweck bietet JavaScript **async-Iteratoren**.

### Asynchrone Generatorfunktionen

Der einfachste Weg, einen asynchronen Iterator zu erstellen, ist die Verwendung einer **asynchronen Generatorfunktion**.

Wir schreiben es so:

```javascript
async function* generateNumbers() {
yield 1
yield 2
yield 3
}
```

Dieser sieht genauso aus wie ein normaler Generator, nur mit `async` davor.

Wir können nun `for await...of` verwenden, um die Werte zu verbrauchen:

```javascript
async function run() {
  for await (const n of generateNumbers()) {
    console.log("Got number:", n)
  }

  console.log("Done!")
}

run()
```

Dies wird ausgegeben:

```
Got number: 1
Got number: 2
Got number: 3
Done!
```

Was ist also der Unterschied zu einem normalen Generator?

Der Unterschied ist, dass wir jetzt `await` innerhalb des Generators verwenden können.

Lass uns wieder einen Verzögerungshelfer machen:

```javascript
function wait(ms) {
  return new Promise(resolve => setTimeout(resolve, ms))
}
```

Lass uns nun **langsam** Zahlen liefern:

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

Probieren wir es aus:

```javascript
async function run() {
  for await (const n of generateSlowNumbers()) {
    console.log("Got number:", n)
  }

  console.log("Done!")
}

run()
```

### Warum sollte man asynchrone Iteratoren verwenden?

Async-Iteratoren sind nützlich, wenn:


* Die Werte nicht alle auf einmal ankommen.
* Du sie nacheinander bearbeiten willst, **sobald sie kommen**.
* **Du mit Promises arbeitest und eine saubere Schleife erstellen möchtest**.

Wenn du beispielsweise eine Nachricht nach der anderen von einem Chatserver laden oder eine große Datei in Stücken herunterladen möchtest, kannst du mit asynchronen Iteratoren eine `for`-Schleife schreiben, die mit verzögerten Daten arbeitet.

### Symbol.asyncIterator

Wir können auch asynchrone Iteratoren in benutzerdefinierten Klassen verwenden.

Hier ist ein Beispiel, das Zahlen mit einer Verzögerung erzeugt:

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

Wir können nun `for await...of` genau wie zuvor verwenden:

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

So kannst du Objekte erstellen, die asynchron durchlaufen werden können

## Syntaktischer Zucker für Assignemnts
<chapterId>8b1ba7d8-ecfd-5470-b86e-73cb84ccc8b7</chapterId>

"Syntaktischer Zucker" ermöglicht es, etwas kürzer oder einfacher zu schreiben, ohne seine Funktion zu verändern. Es ist nur eine schönere Art, das Gleiche zu sagen.

JavaScript verfügt über einiges an eingebautem Syntaktischen Zucker, mit dem wir sauberere und kürzere Deklarationen schreiben können. In diesem Kapitel sehen wir uns an, wie man Werte basierend auf einer Bedingung zuweist, Variablen mit Mathematik aktualisiert, Werte aus Arrays oder Objekten zieht und sie mit einer einfacheren Syntax kopiert oder kombiniert.

### Der ternäre Operator

In JavaScript kannst du einen Wert auf der Grundlage einer Bedingung zuweisen, indem du den **ternären Operator** verwendest, welcher eine Kurzform von `if...else` ist.

Anstatt:

```javascript
let message

if (isMorning) {
  message = "Good morning"
} else {
  message = "Hello"
}
```

kannst du:

```javascript
const message = isMorning ? "Good morning" : "Hello"
```

schreiben. Dies bedeutet:

* Wenn `isMorning` wahr ist, verwenden wir `"Good morning"`
* Andernfalls verwenden wir `"Hello"`

Die allgemeine Form ist:

```javascript
condition ? valueIfTrue : valueIfFalse
```

Du kannst ihn auch in anderen Ausdrücken verwenden:

```javascript
console.log(isSunny ? "Go outside" : "Stay in")
```

Achte nur darauf, dass du es für **einfache** Entscheidungen verwenden. Wenn die Logik komplex ist, bleibe bei `if...else`.

### Alternative Assignment-Operator

JavaScript verfügt über **Shortcut-Operatoren** für die Ausführung von Zuweisungen in Kombination mit Operationen.

Betrachten wir einmal den normalen Weg:

```javascript
let counter = 1
counter = counter + 1
```

Dies kann abgekürzt werden zu:

```javascript
let counter = 1
counter += 1 // dasselbe wie counter = counter + 1
```

Hier sind die häufigsten:

| Operator | Bedeutung                  |
| -------- | ---------------------------|
| `+=`     | addiere und weise zu       |
| `-=`     | subtrahiere und weise zu   |
| `*=`     | multipliziere und weise zu |
| `/=`     | dividiere und weise zu     |

Beispiele:

```javascript
let score = 10
score += 5  // jetzt beträgt score 15
score *= 2  // jetzt beträgt score 30
score -= 10 // jetzt beträgt score 20
```

Diese sind nützlich, wenn eine Variable mit ihrem eigenen Wert aktualisieren willst.

### Destrukturierung

Mit der **Destrukturierung** kannst du auf einfache Weise Werte aus Arrays oder Objekten entnehmen und in Variablen speichern.

#### Arrays

Angenommen, Du hast:

```javascript
const colors = ["red", "green", "blue"]
```

Anstatt:

```javascript
const first = colors[0]
const second = colors[1]
```

kannst du:

```javascript
const [first, second] = colors
```
tun. Dies weist zu:


* `first` wird `"red"`
* `second` wird `"green"`

Du kannst auch Werte weglassen:

```javascript
const [,, third] = colors
console.log(third) // blue
```

#### Objekte

Du kannst auch Werte aus Objekten extrahieren:

```javascript
const user = { name: "Alice", age: 30 }

const { name, age } = user
console.log(name) // Alice
console.log(age)  // 30
```

Wenn die Eigenschaft einen anderen Namen hat als die gewünschte Variable, kannst du sie umbenennen:

```javascript
const { name: username } = user
console.log(username) // Alice
```

Die Destrukturierung macht deinen Code bei der Arbeit mit Objekten und Arrays sauberer.

### Spread-Syntax

Die **Spread-Syntax** verwendet `...` zum Entpacken oder Kopieren von Werten.

#### Arrays

Du kannst Arrays kopieren oder zusammenführen:

```javascript
const a = [1, 2]
const b = [3, 4]

const both = [...a, ...b]
console.log(both) // [1, 2, 3, 4]
```

Du kannst auch ein Array klonen:

```javascript
const original = [10, 20, 30]
const clone = [...original]
```

#### Objekte

Du kannst dasselbe mit Objekten tun:

```javascript
const a = { x: 1 }
const b = { y: 2 }

const merged = { ...a, ...b }
console.log(merged) // { x: 1, y: 2 }
```

Du kannst die Werte auch überschreiben:

```javascript
const user = { name: "Alice", age: 30 }
const updated = { ...user, age: 31 }

console.log(updated) // { name: "Alice", age: 31 }
```

Dies ist sehr nützlich, wenn du Objekte aktualisieren willst, ohne das Original zu verändern.

# NodeJS
<partId>42fe4d49-dace-5135-bb9e-b9d75034fb2a</partId>

## Wie ist Node entstanden?
<chapterId>0da1d60c-06c9-54e6-a181-ae7dabf6e3b8</chapterId>

In diesem Kapitel erfahren wir ein wenig über den historischen Kontext von JavaScript und NodeJS.

Der historische Kontext ist bei Software sehr wichtig, weil wir oft Werkzeuge verwenden, die von anderen Menschen entwickelt wurden, und wir daher von Entscheidungen beeinflusst werden, die diese Menschen in der Vergangenheit getroffen haben.

Wenn wir die Gründe für diese Entscheidungen verstehen und wissen, wie die von uns verwendeten Werkzeuge zustande gekommen sind, werden wir weniger verwirrt sein über das, was wir tun.

### Die Ursprünge von JavaScript

JavaScript war ursprünglich eine einfache Sprache, um Webseiten interaktiv zu gestalten.

In den 1990er Jahren fügten Webbrowser wie Netscape Navigator JavaScript hinzu, so dass Entwickler Code schreiben konnten, der direkt im Browser ausgeführt wurde.

Die ursprüngliche Idee war, Java als Kernsprache für die Erstellung von Websites (mit den so genannten "Java-Applets") zu verwenden und JavaScript nur für kleinere Dinge.

Das Kerndesign wurde von Brendan Eich, der damals bei Netscape angestellt war, in weniger als 2 Wochen erstellt.

Aber die meisten Leute zogen die Verwendung von JavaScript der Verwendung von Java vor, und auch Java-Applets hatten damals einige Sicherheitsprobleme, so dass Java schließlich als Option gestrichen wurde und JavaScript zum De-facto-Standard für die Webentwicklung wurde.

### Die V8-Engine

JavaScript ist eine interpretierte Sprache, im Gegensatz zu kompilierten Sprachen wie C.

Der in einer kompilierten Sprache geschriebene Code wird in eine Binärdatei umgewandelt, und die Binärdatei wird direkt an die CPU des Computers weitergeleitet.

![](assets/en/006.webp)

Interpretersprachen hingegen sind in der Regel benutzerfreundlicher und orientieren sich eher an der menschlichen Denkweise ("high level") als an der Arbeitsweise von Maschinen ("low level"); daher verfügen sie in der Regel über eine virtuelle Maschine, die ihren Code ausführt.

Eine virtuelle Maschine ist ein spezielles Programm, das zwischen dem von dir geschriebenen Code und der CPU sitzt und deinen Code ausführt (weil die CPU ihn nicht verstehen kann).

Auf diese Weise kannst du programmieren, ohne zu viel über die zugrunde liegende Maschine zu wissen, aber es hat auch einen Preis in Bezug auf die Leistung, denn auf dem Computer läuft nicht nur dein Programm, sondern ein Programm (die virtuelle Maschine), auf dem dein Programm läuft.

Da Webanwendungen immer komplexer wurden, bestand der Bedarf, die Leistung von JavaScript zu verbessern. Die V8-Engine ist der Interpreter, der JavaScript in Google Chrome antreibt. Er wurde bei Google entwickelt und 2008 veröffentlicht.

Während die älteren JavaScript-Engines meist traditionelle virtuelle Maschinen waren, ist die V8-Engine ein JIT-Compiler (Just-in-Time).

Der JavaScript-Code wird in die V8-Engine eingespeist, und die Engine versucht, Teile davon als native Binärdateien im laufenden Betrieb zu kompilieren. Dies ermöglicht es dir, das Erlebnis einer Hochsprache zu haben, mit einer Leistung, die ein wenig näher an Low-Level-Sprachen ist. Dies hat JavaScript zur schnellsten Hochsprache der Welt gemacht, eine Art "das Beste aus beiden Welten".

### Die NodeJS-Laufzeitumgebung

Obwohl JavaScript einfach zu benutzen und recht schnell auszuführen ist, hatte es nach der Veröffentlichung von V8 eine große Einschränkung: Es konnte nur innerhalb eines Browsers ausgeführt werden.

Warum ist das ein Problem?

Nun, da Browser Code ausführen, der aus Millionen verschiedener Quellen im Internet stammt, können sie leicht sich leicht Malware einfangen, weshalb sie vom Rest des Betriebssystems getrennt sind.

![](assets/en/007.webp)

JavaScript konnte nicht auf das Dateisystem und andere lokale Ressourcen auf deinem Computer zugreifen (zumindest nicht so einfach wie andere Sprachen), so dass dies eine erhebliche Einschränkung für die Art der Anwendungen darstellte, die man damit erstellen konnte.

Im Jahr 2009 veröffentlichte Ryan Dahl NodeJS, eine Laufzeitumgebung, mit der man die V8-Engine außerhalb des Browsers direkt auf dem nativen Betriebssystem seines Computers verwenden konnte. Außerdem bietet sie viele Funktionen, die für das Schreiben von serverseitigen und Kommandozeilenprogrammen nützlich sind. So kann man mit NodeJS beispielsweise einen Webserver erstellen, Dateien lesen und schreiben oder Tools zur Automatisierung von Aufgaben erstellen.

![](assets/en/008.webp)

In diesem Kurs haben wir uns bisher mit den JavaScript-Funktionen beschäftigt, die sowohl im Browser als auch in NodeJS vorhanden sind. Mit diesen Funktionen konnten wir Daten definieren und sie auf abstrakte Weise manipulieren. In den nächsten Lektionen werden wir uns mit den NodeJS-spezifischen Funktionen befassen, die uns die Interaktion mit dem Betriebssystem ermöglichen.

## Kommandozeilenargumente
<chapterId>960d20f3-c424-5d51-a041-ef17d2e94b6d</chapterId>

NodeJS ermöglicht es uns unter anderem, CLIs (Command Line Interfaces = Kommandozeilen Schnittstellen) zu erstellen.

Dafür brauchen wir eine Möglichkeit, Kommandozeilenargumente zu erhalten, was in Node mit dem eingebauten `process`-Objekt geschieht.

### process

NodeJS bietet ein spezielles Objekt namens `process`, das das aktuell laufende Programm darstellt.

Du kannst damit die Umgebung und das aktuelle Arbeitsverzeichnis überprüfen und bei Bedarf sogar das Programm beenden.

Zum Beispiel:

```javascript
console.log(process.platform)
```

Dies gibt die Plattform des Betriebssystems aus, z.B. `win32`, `linux` oder `darwin` (Mac).

### process.argv

Wenn du ein NodeJS-Programm vom Terminal aus startest, kannst du zusätzliche Wörter (Argumente) nach dem Skriptnamen übergeben. Diese werden in `process.argv` gespeichert.

Wenn du zum Beispiel diesen Befehl ausführst:

```
node my_script.js alpha beta
```

kannst du die Argumente wie folgt ausgeben:

```javascript
console.log(process.argv)
```

Die Ausgabe könnte wie folgt aussehen:

```
[ '/path/to/node', '/path/to/my_script.js', 'alpha', 'beta' ]
```

Die ersten beiden Elemente sind immer der Node-Pfad und dein Skript-Pfad. Alle zusätzlichen Wörter, die du an das Skript übergeben hast, folgen danach.

Das `process.argv`-Array kann wie jedes andere Array mit der `.slice()`-Methode zerlegt werden. Um also nur die Argumente zu erhalten, die übergeben wurden, kannst du

```javascript
const args = process.argv.slice(2)

console.log(args)
```
schreiben.

Der Zugriff auf die Argumente, die der Benutzer übergibt, ist für die Entwicklung von Befehlszeilenanwendungen unerlässlich.

## Module
<chapterId>4e1651a5-65fd-50bc-b22a-40313d5659ca</chapterId>

JavaScript-Laufzeitsysteme wie NodeJS behandeln normalerweise jede JavaScript-Datei als separates Modul.

Stelle dir ein Modul wie eine Box vor. Die Box hat ihren eigenen privaten Bereich, so dass die darin deklarierten Variablen und Funktionen den Code in anderen Boxen nicht beeinträchtigen. Im Grunde hat jedes Modul seinen eigenen Bereich.

Ein Modul kann einen Teil seines Inhalts exportieren, um ihn anderen Modulen zur Verfügung zu stellen, und es kann den Inhalt importieren, den andere Module exportiert haben. Mit JavaScript kannst du Inhalte zwischen Modulen exportieren und importieren, um verschiedene Dateien zu verbinden.

Ein JavaScript-Programm besteht oft aus mehreren Modulen, die miteinander verbunden sind.

Warum Module verwenden? Indem du deinen Code in Module aufteilst, kannst du dein Programm in kleinere, übersichtlichere und wiederverwendbare Teile gliedern. Jedes Modul kann sich auf eine bestimmte Art von Aufgabe konzentrieren, z.B. auf mathematische Berechnungen, die Arbeit mit Dateien oder die Formatierung von Text.

### CommonJS-Module

In NodeJS wird das gängigste System zur Verwaltung von Modulen **CommonJS** genannt.

In diesem System kannst du den Code eines Moduls mit `module.exports` freigeben (exportieren) und ihn mit `require()` in eine andere Datei laden (importieren).

Um etwas außerhalb eines Moduls verfügbar zu machen, weist man es `module.exports` zu:

```javascript
const greeting = "Hello!"

module.exports = greeting
```

In diesem Fall exportiert das Modul die Zeichenkette "Hello!".

Um den exportierten Code aus einer anderen Datei zu verwenden, verwendet man die Funktion `require()` mit dem Pfad zu dieser Datei:

```javascript
const greeting = require("./greeting.js")

console.log(greeting)
```

Dies wird ausgegeben:

```
Hello!
```

Du kannst mehrere Dinge exportieren, indem Sie sie in einem anonymen Objekt zusammenfasst, z.B.:

```javascript
const greeting1 = "hello"

const greeting2 = "hi"

module.exports = {
  greeting1, greeting2
}
```

CommonJS war das Modulsystem, das zunächst von NodeJS übernommen wurde. Später wurden auch ES-Module hinzugefügt.

### ES-Module

NodeJS unterstützt auch eine andere Art von Modulen, die **ES-Module**, die in der Webentwicklung sehr beliebt sind. Sie verwenden die Schlüsselwörter `export` und `import`.

ES-Module wurden für den Browser entwickelt und erst später zu Node hinzugefügt. Wenn du sie verwenden möchten, musst du möglicherweise `.mjs` als Dateierweiterung anstelle von `.js` verwenden, je nachdem, welche Node-Version du verwendest.

In einer Datei mit dem Namen `greeting.mjs` schreiben wir

```javascript
export const greeting = "Hello!"
```

Wie du siehst, exportieren wir die Konstante direkt dort, wo sie definiert wird

In einer anderen Datei namens `index.mjs` importieren wir sie:

```javascript
import { greeting } from "./greeting.mjs"

console.log(greeting)
```

Du kannst verschiedene Deklarationen an verschiedenen Stellen der Datei exportieren, z.B.:

```javascript
export const num = 10

export function double (x) {
  return x*2
}
```

### Die NodeJS-Standardbibliothek

NodeJS enthält auch viele integrierte Module. Dabei handelt es sich um vorgefertigte Module, die von NodeJS bereitgestellt werden und bei allgemeinen Aufgaben wie dem Lesen von Dateien, der Arbeit mit dem Betriebssystem oder der Verbindung mit dem Netzwerk helfen.

Das Modul `os` zum Beispiel gibt dir Informationen über dein Betriebssystem:

```javascript
const os = require("os")

console.log(os.platform())
```

Du musst diese eingebauten Module nicht installieren, sie werden mit NodeJS geliefert. Sie bilden die "Standardbibliothek" der Laufzeitumgebung und werden von den meisten Node-Anwendungen verwendet, um Dinge wie das Lesen von Dateien oder die Kommunikation über das Internet durchzuführen.

In den nächsten Kapiteln wirst du einige nützliche Beispiele für ihre Verwendung finden.

## Das fs-Modul
<chapterId>911e953a-35ae-5ee7-bd74-372501c32e81</chapterId>

Das `fs`-Modul (kurz für **file system** = Dateisystem) ist Teil der NodeJS-Standardbibliothek. Es erlaubt dir, mit Dateien und Verzeichnissen auf deinem Computer zu arbeiten: Du kannst Dateien lesen, schreiben, löschen, umbenennen und mehr.

Um es zu verwenden, musst du es zunächst am Anfang deiner Datei importieren:

```javascript
const fs = require("fs")
```

### Sync-API

Der einfachste Weg, `fs` zu benutzen, ist mit seinen **sync** Methoden.

Diese Methoden blockieren das Programm, bis sie beendet sind (so dass die nächste Codezeile nicht ausgeführt wird, bevor der Vorgang abgeschlossen ist).

Hier ist ein Beispiel für das synchrone Lesen einer Datei:

```javascript
const fs = require("fs")

const data = fs.readFileSync("example.txt", "utf8")

console.log(data)
```

Wenn sich eine Datei mit dem Namen `example.txt` im gleichen Verzeichnis wie dein Skript befindet, wird ihr Inhalt ausgegeben.

Du kannst auch synchron in eine Datei schreiben:

```javascript
const fs = require("fs")

fs.writeFileSync("output.txt", "Hello from Node!")

console.log("File written!")
```

Dadurch wird eine Datei mit dem Namen `output.txt` mit dem Text erstellt (oder überschrieben).

Hier sind einige gängige Operationen, die man mit dieser API durchführen kann:

```javascript
const fs = require("fs")

// Liste alle Dateien und Ordner auf
const items = fs.readdirSync(".")
console.log("Items in current directory:", items)

// Erzeuge einen Ordner
fs.mkdirSync("my_folder")
console.log("Folder created")

// Lösche einen Ordner
fs.rmdirSync("my_folder")
console.log("Folder deleted")

// Erzeuge und beschreibe eine Datei
fs.writeFileSync("my_file.txt", "Hello world")
console.log("File created & written")

// Lese eine Datei
const content = fs.readFileSync("my_file.txt", "utf8")
console.log("File content:", content)

// Lösche eine Datei
fs.unlinkSync("my_file.txt")
console.log("File deleted")
```

Die Sync-API ist einfach und gut für kleine Skripte geeignet, aber da sie das Programm blockiert, bis es fertig ist, kann sie die Arbeit verlangsamen, wenn du mit großen Dateien oder einem Server arbeitest.

### Asynchrone Callback-API

Die **Callback-API** ist nicht blockierend: Sie ermöglicht es NodeJS, andere Dinge zu tun, während die Dateioperation ausgeführt wird.

Anstatt das Ergebnis direkt zurückzugeben, wird eine Funktion (ein **Callback**) verwendet, die aufgerufen wird, wenn der Vorgang abgeschlossen ist.

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

Das passiert folgendermaßen:

* `fs.readFile` beginnt mit dem Lesen von `example.txt`.
* NodeJS wartet nicht, sondern führt anderen Code aus, den du möglicherweise geschrieben hast.
* Wenn die Datei fertig gelesen ist, wird der Callback ausgeführt:
  * Wenn ein Fehler aufgetreten ist, enthält `err` den Fehler.
  * Andernfalls enthält `data` den Inhalt.

So schreibt man in eine Datei:

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

Gleiche Idee: Das Programm hält nicht an, während es die Datei schreibt.

Einige Beispiele für Dinge, die du mit dieser API tun kannst:

```javascript
const fs = require("fs")

// Liste alle Dateien und Ordner auf
fs.readdir(".", (err, items) => {
  if (err) return console.error(err)
  console.log("Items in current directory:", items)
})

// Erzeuge einen Ordner
fs.mkdir("my_folder", (err) => {
  if (err) return console.error(err)
  console.log("Folder created")
})

// Lösche einen Ordner
fs.rmdir("my_folder", (err) => {
  if (err) return console.error(err)
  console.log("Folder deleted")
})

// Erzeuge und beschreibe eine Datei
fs.writeFile("my_file.txt", "Hello world", (err) => {
  if (err) return console.error(err)
  console.log("File created & written")
})

// Lese eine Datei
fs.readFile("my_file.txt", "utf8", (err, content) => {
  if (err) return console.error(err)
  console.log("File content:", content)
})

// Lösche eine Datei
fs.unlink("my_file.txt", (err) => {
  if (err) return console.error(err)
  console.log("File deleted")
})
```

Die Callback-API ist besser für Server und große Aufgaben geeignet, da sie das Programm nicht blockiert, aber verschachtelte Callbacks können unübersichtlich werden, wenn man viele Operationen verkettet. Aus diesem Grund wurde eine auf Promises basierende asynchrone API hinzugefügt.

### Asynchrone Promise-API

Die Promise-basierte API ist modern und funktioniert hervorragend mit `.then()` und `async/await`. Sie ist als `fs.promises` verfügbar.

Du nusst die Eigenschaft `Promises` importieren:

```javascript
const fs = require("fs").promises
```

Verwendung von `.then()`:

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

Oder noch besser, mit `async/await`:

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

Schreiben in eine Datei:

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

Die übliche Liste von Beispielen für die API:

```javascript
const fs = require("fs").promises

// Benutze eine async Funktion um auf Ergebnisse zu warten
async function main() {
  // Liste alle Dateien und Ordner auf
  const items = await fs.readdir(".")
  console.log("Items in current directory:", items)

  // Erzeuge einen Ordner
  await fs.mkdir("my_folder")
  console.log("Folder created")

  // Lösche einen Ordner
  await fs.rmdir("my_folder")
  console.log("Folder deleted")

  // Erzeuge und beschreibe eine Datei
  await fs.writeFile("my_file.txt", "Hello world")
  console.log("File created & written")

  // Lese eine Datei
  const content = await fs.readFile("my_file.txt", "utf8")
  console.log("File content:", content)

  // Lösche eine Datei
  await fs.unlink("my_file.txt")
  console.log("File deleted")
}

main().catch(err => console.error(err))
```

## NPM
<chapterId>a91d9a75-55cc-51a3-a48f-0c0be6fe6e72</chapterId>

Wenn du Code schreibst, musst du oft Code verwenden, der von anderen geschrieben wurde, z.B. Bibliotheken, die dir bei der Arbeit mit Daten, Farben, Servern oder fast allem anderen helfen.

Anstatt Dateien manuell herunterzuladen und zu kopieren, kannst du einen **Paketmanager** verwenden.

Ein Paketmanager ist ein Werkzeug, das:

* Pakete herunterlädt
* den Überblick behält, welche Pakete dein Projekt benötigt
* sicherstellt, dass jeder in deinem Team über die gleichen Versionen der Pakete verfügt

### Was ist NPM?

In der NodeJS-Welt ist der beliebteste Paketmanager **NPM**, was für *Node Package Manager* steht.

Du erhältst NPM automatisch, wenn du NodeJS installierst.

Du kannst überprüfen, ob du NPM habst, indem du dies in deinem Terminal ausführst:

```
npm -v
```

Dies gibt die Version von NPM aus, die Du hast, z.B.:

```
10.2.1
```

### Ein Paket erstellen

In NodeJS ist ein **Paket** einfach ein Verzeichnis mit einer `package.json`-Datei darin.

Lass uns Schritt für Schritt eine erstellen.

1. Lege einen neuen Ordner für dein Projekt an:

```
mkdir my_project
cd my_project
```

2. Führe diesen Befehl aus:

```
npm init
```

Dadurch wird ein interaktives Setup gestartet, das dir Fragen über den Namen deines Projekts, die Version, die Beschreibung usw. stellt.

Wenn du nicht alles beantwortest und nur die Standardeinstellungen akzeptieren möchtest, kannst du dies tun:

```
npm init -y
```

Nachdem du es ausgeführt hast, siehst du in deinem Ordner eine neue Datei mit dem Namen

```
package.json
```

### package.json

Die Datei `package.json` ist einfach eine JSON-Datei, die Metadaten über dein Projekt speichert.

Hier ist ein Beispiel:

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

Ein paar wichtige Felder:


* `name`: der Name deines Pakets
* `version`: die aktuelle Version
* `main`: die Einstiegsdatei (wie `index.js`)
* `skripts`: Befehle, die du ausführen kannst (wie `npm start`)
* `dependencies`: listet alle Pakete auf, auf die dein Projekt angewiesen ist

### Installieren eines Pakets

Nehmen wir an, du willst ein bestimmtes Paket namens `picocolors` verwenden, um Farben zu deiner Terminalausgabe hinzuzufügen.

Du kannst es installieren, indem du:

```
npm install picocolors
```

ausführts.

Du kannst es nun in deinem Projekt verwenden. Erstelle eine Datei `index.js` mit

```javascript
const pico = require('picocolors')

console.log(
  pico.green("This text is green!")
)
```

und versuche, es auszuführen. Das Terminal sollte eine farbige Version des Textes ausgeben.

Was hat der NPM getan?

* Er lud das Paket herunter und speicherte es in einem Unterordner namens `node_modules/`
* Er hat einen Eintrag unter `dependencies` in deiner `package.json` hinzugefügt
* Er hat die Datei `package-lock.json` aktualisiert

Was ist `package-lock.json`?

### package-lock.json

Diese Datei wird automatisch von NPM erstellt.

Du wirst dich vielleicht fragen, warum wir eine weitere Datei brauchen, wenn wir bereits `package.json` haben?

Das ist der Grund:

* `package.json` sagt nur, welche Version **eines Pakets** dein Projekt benötigt.

Beispiel:

```json
"dependencies": {
  "picocolors": "^1.1.0"
}
```

Das `^1.1.0` bedeutet "jede Version, die mit 1.1.x kompatibel ist", also ist es flexibel.

* die Datei `package-lock.json` **friert** die exakten Versionen jedes einzelnen Pakets und seiner Unterabhängigkeiten ein, so dass jeder, der dein Projekt installiert, genau die gleiche Arbeitseinstellung erhält.

Warum ist das wichtig?

Wenn du in einem Team arbeitest, dein Projekt auf einem Server bereitstellst oder in der Zukunft weiter daran arbeiten möchtest, möchtest du sicherstellen, dass es immer noch auf die gleiche Weise funktioniert.

Wenn die Pakete aktualisiert wurden und du sie ohne Sperrdatei neu installierst, erhältst du möglicherweise eine etwas andere Version, die sich anders verhält.

Wenn du die `package-lock.json` in deinem Projekt aufbewahrst, wird NPM immer genau die dort aufgelisteten Versionen installieren, um sicherzustellen, dass jeder dieselbe Umgebung hat.

`package-lock.json` sperrt alles auf eine ganz bestimmte Version, um das Projekt auf anderen Rechnern reproduzierbar zu machen.

Wenn dein Paket jedoch von vielen Leuten benutzt werden muss, kannst du es (`package-lock.json`) auch nicht übergeben, so dass NPM nur die Datei `package.json` findet und automatisch die neuesten Versionen installieren kann, die in dieser Datei erlaubt sind.

Aber das sind Dinge, um die du dich später kümmern solltest, wenn du anfängst, deinen eigenen Code zu veröffentlichen. Für den Moment haben wir die Grundlagen von NPM vorgestellt, damit du die von anderen Entwicklern veröffentlichten Bibliotheken finden und in deinen Projekten verwenden kannst.


## Vernetzung in NodeJS
<chapterId>f2cabd8b-754b-5c97-8d6a-8412a9a184c7</chapterId>

NodeJS wird häufig als Backend-Sprache verwendet: Du kannst dein Skript in einen Server verwandeln und es auch dazu verwenden, Anfragen an andere Server zu stellen.

In diesem Kapitel werden wir einige grundlegende Netzwerkfunktionen vorstellen, die dir dies ermöglichen.

### fetch()

Wenn dein Programm Daten von einer Website oder einer API herunterladen soll, musst du eine **HTTP-Anfrage** stellen.

In modernen Versionen von NodeJS kannst du die eingebaute Funktion `fetch()` verwenden.

Hier ist ein Beispiel für eine GET-Anfrage an eine API:

```javascript
const response = await fetch("https://jsonplaceholder.typicode.com/posts/1")
const data = await response.text()

console.log(data)
```

Wenn du dies ausführst, siehst du etwas wie:

```
{
  "userId": 1,
  "id": 1,
  "title": "...",
  "body": "..."
}
```

Das geschieht folgendermaßen:

1. `fetch()` nimmt eine URL und stellt eine Anfrage.
2. Es gibt eine **Promise** zurück, das in ein `Response`-Objekt aufgelöst wird.
3. `response.text()` liest die Antwort als Zeichenkette aus.

Aber die Zeichenkette, die du zurückbekommst, ist eigentlich JSON. Was ist das?

### JSON

Bei der Arbeit mit Web-APIs werden die Daten oft als **JSON** gesendet und empfangen, was für JavaScript Object Notation steht.

JSON ist nur ein Textformat, das JavaScript-Objekten sehr ähnlich sieht. Zum Beispiel:

```json
{
  "name": "Alice",
  "age": 30,
  "likes": ["apples", "bananas"]
}
```

Das `JSON`-Objekt ist ein eingebautes Hilfsmittel in JavaScript, das für die Arbeit mit diesem Datenformat verwendet werden kann.

Du kannst ein JavaScript-Objekt in eine JSON-Zeichenkette umwandeln, indem du `JSON.stringify()` verwendest:

```javascript
const user = { name: "Alice", age: 30 }

const jsonString = JSON.stringify(user)

console.log(jsonString)
```

Dies wird ausgegeben:

```
{"name":"Alice","age":30}
```

Du kannst JSON-Text auch mit `JSON.parse()` in ein JavaScript-Objekt zurückverwandeln:

```javascript
const jsonText = '{"name":"Bob","age":25}'

const obj = JSON.parse(jsonText)

console.log(obj)
```

Dies wird ausgegeben:

```
{ name: 'Bob', age: 25 }
```

Sei vorsichtig: `JSON.parse()` gibt einen Fehler aus, wenn die Zeichenkette kein gültiges JSON ist.

```javascript
JSON.parse("not json") // ❌ Error!
```

Stelle also sicher, dass die Zeichenfolge richtig formatiert ist.

### http-Server

Mit NodeJS kannst du einen Webserver erstellen, ohne etwas anderes zu installieren.

Du kannst das eingebaute `http`-Modul verwenden, um Anfragen von Clients zu bearbeiten und Antworten zurückzusenden.

Hier ist ein sehr einfaches Beispiel:

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

Wenn du dieses Skript ausführst und `http://localhost:3000` in deinem Browser öffnest, wirst du:

```
Hello from NodeJS server!
```
sehen.
 
Das passiert im Code:

1. Du hast den `http`-Server aus der Node-Standardbibliothek importiert.
2. Mit `http.createServer()` wird ein Server erstellt. Du hast an `http.createServer()` einen Callback `(req, res) => {...}` übergeben, der jedes Mal ausgeführt wird, wenn sich jemand verbindet.
3. Du hast der Antwort den Statuscode 200 zugewiesen (was einen erfolgreichen Vorgang anzeigt). Du kannst mehr Informationen über http-Statuscodes [hier](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status) nachlesen.
4. `res.end()` sendet die Antwort und beendet die Verbindung.
5. `server.listen(3000)` startet den Server auf Port 3000.

Du kannst auch `req.url` und `req.method` in der Anfrage überprüfen, um verschiedene Pfade oder Anfragearten zu behandeln.

Beispiel mit Routing:

```javascript
const server = http.createServer((req, res) => {
  if (req.url === "/") { // behandele Anfragen für die root der Webseite
    res.statusCode = 200
    res.end("Home page")
  } else if (req.url === "/about") { // behandele Anfragen für die About-Seite
    res.statusCode = 200
    res.end("About page")
  } else {
    res.statusCode = 404 // wir senden den Statuscode 404 um anzuzeigen dass die angefragte Seite fehlt
    res.end("Not Found")
  }
})
```

Dies sind sehr einfache Beispiele. Um fortgeschrittenere Server zu bauen, würden die meisten Entwickler wahrscheinlich eine fertige Backend-Bibliothek wie [express](https://www.npmjs.com/package/express) herunterladen.

## Datenverarbeitung: Puffer (Buffer), Ereignisse (Events), Datenströme (Streams)
<chapterId>8c9623f0-a604-51a4-8fe4-871c849d3e3b</chapterId>

In diesem Kapitel werden wir hauptsächlich drei Objektklassen vorstellen:

* Puffer (Buffer), der kleine Abschnitte von Binärdaten darstellt
* `EventEmitter`, der verwendet werden kann, um einen asynchronen Prozess zu verfolgen, indem er Signale, sogenannte Ereignisse ("Events"), aussendet
* Datenstrom (`Stream`), der es uns ermöglicht, große Datenmengen in einem Puffer zu verarbeiten, und der den Prozess durch die Ausgabe von Ereignissen mitverfolgt

Diese sind in professionellem NodeJS-Code sehr verbreitet. Auch wenn du sie in deinen ersten Projekten vielleicht nicht verwenden wirst, ist es gut, ein grundlegendes Verständnis dafür zu bekommen, wenn du mit ihnen interagieren musst.

### Puffer (Buffer)

In NodeJS ist ein **Puffer** (Buffer) ein Objekttyp, der für die Arbeit mit binären Daten verwendet wird.

Man kann sich einen Buffer als einen Behälter mit fester Größe für Rohbytes vorstellen.

So erstellst du einen buffer aus einer Zeichenkette:

```javascript
const buf = Buffer.from("hello")
console.log(buf)
```

Dies druckt etwas wie:

```
<Buffer 68 65 6c 6c 6f>
```

Diese Zahlen (`68`, `65`, `6c`, usw.) sind hexadezimale Darstellungen der Buchstaben von `"hello"`.

Du kannst sie wie folgt in eine Zeichenkette zurückverwandeln:

```javascript
console.log(buf.toString())
```

Dies wird ausgegeben:

```
hello
```

Du kannst auch einen Buffer mit einer bestimmten Größe anlegen, der mit Nullen gefüllt ist:

```javascript
const buf = Buffer.alloc(10)
console.log(buf)
```

Dies druckt etwas wie:

```
<Buffer 00 00 00 00 00 00 00 00 00 00>
```

Du kannst in den Buffer schreiben:

```javascript
buf.write("abc")
console.log(buf)
```

Und Du kannst auf einzelne Bytes zugreifen:

```javascript
console.log(buf[0]) // gibt die ACII Zahl für 'a" aus, was 97 entspricht
```

Buffer sind besonders nützlich, wenn du Daten auf einer sehr niedrigen Ebene manipulieren musst.

### Ereigenisse (Events)

In JavaScript ist ein **Ereignis** (event) etwas, das in deinem Programm passiert und auf das du reagieren kannst.

Zum Beispiel:

* Das Laden einer Datei ist abgeschlossen
* Ein Timer läuft ab
* Ein Benutzer klickt auf eine Schaltfläche
* Eine Netzanfrage liefert Daten

Ein **Ereignis** ist nur ein Signal, dass etwas passiert ist, und man kann Code schreiben, um auf diese Ereignisse zu warten und darauf zu reagieren.

In NodeJS können viele Objekte Ereignisse auslösen. Diese Objekte werden **EventEmitters** genannt.

Hier ist ein Beispiel:

```javascript
const EventEmitter = require("events")

const emitter = new EventEmitter()

// Warten ("listen") auf ein Event
emitter.on("greet", () => {
  console.log("Hello! An event happened.") // dies wird ausgegeben, wenn ein "greet" event ausgelöst wird
})

// Löse das Event aus
emitter.emit("greet")
```

Dies wird ausgegeben:

```
Hello! An event happened.
```

Und zwar folgendermaßen:

1. Wir erstellen ein `EventEmitter`-Objekt.
2. Mit `.on("greet")` weisen wir es an, einen Callback auszuführen, wenn das Ereignis `"greet"` eintritt.
3. Später lösen wir das Ereignis `"greet"` mit `.emit()` aus.
4. Unser Callback wird ausgeführt

Du kannst mit dem Ereignis weitere Daten übergeben:

```javascript
emitter.on("greet",
  (name) => console.log(`Hello, ${name}!`)
)

emitter.emit("greet", "Alice") // Das erste Argument ist vom Typ Event, das zweite Argument sind die Daten die wir dem Event mitgeben
```

Dies wird ausgegeben:

```
Hello, Alice!
```

Du kannst Zuhörer (listener) auch für andere Ereignisse registrieren:

```javascript
emitter.on("goodbye", () => {
  console.log("Goodbye!")
})

emitter.emit("goodbye")
```

Du kannst einem Ereignistyp beliebig viele Zuhörer zuordnen, und Du kannst viele verschiedene Ereignistypen von ein und demselben Emitter auslösen.

Viele Objekte in NodeJS geben Ereignisse aus, um dem Rest des Programms mitzuteilen, dass etwas passiert.


### Was sind Datenströme (Streams)?

Datenströme (Streams) kombinieren Puffer und Ereignisse, um uns bei der Verarbeitung von Daten zu helfen.

Wenn wir mit Dateien, Daten aus dem Netz oder sogar langen Texten arbeiten, müssen (oder wollen) wir nicht immer alles auf einmal in den Speicher laden. Das könnte langsam sein oder sogar das Programm zum Absturz bringen, wenn die Daten zu groß sind.

Stattdessen können wir die Daten **nach und nach** verarbeiten, wenn sie ankommen oder gelesen werden, so wie man Wasser durch einen Strohhalm trinkt, anstatt zu versuchen, das ganze Glas auf einmal zu trinken. Das nennt man einen **Stream**.

In NodeJS ist ein Stream ein Objekt, mit dem man Daten von einer Quelle lesen oder an ein Ziel schreiben kann **Stück für Stück**.

NodeJS hat vier Haupttypen von Streams:

* **Readable**: Datenströme, aus denen man Daten lesen kann (wie beim Lesen einer Datei)
* **Writable**: Streams, in die man Daten schreiben kann (wie in eine Datei)
* **Duplex**: Ströme, die sowohl lesbar als auch beschreibbar sind
* **Transform**: wie Duplex-Streams, aber man kann die Daten während des Flusses verändern (transformieren)

### Lesbare Ströme

Nehmen wir an, Du hast eine `bigfile.txt` zu verarbeiten. Du kannst einen lesbaren Stream mit dem `fs`-Modul erstellen, um die Datei Stück für Stück zu lesen.

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

Was geschieht hier?

1. `fs.createReadStream()` erzeugt einen lesbaren Stream.
2. Immer wenn ein Teil der Datei fertig ist, sendet der Stream ein `data`-Ereignis und gibt uns einen "Brocken" (chunk) von Daten (einen `Buffer`). Wir geben den Brocken aus.
3. Wenn die gesamte Datei gelesen wurde, wird das Ereignis `end` ausgelöst.
4. Wenn ein Fehler auftritt (z.B. weil die Datei nicht existiert), wird das Ereignis `error` ausgelöst.

Auf diese Weise kannst du riesige Dateien lesen, ohne sie alle auf einmal in den Speicher zu laden.

Wenn wir wollen, dass die Daten in einer für den Menschen lesbaren Form (statt binär) ankommen, können wir die Kodierung des Stroms angeben:

```javascript
const fs = require("fs")

const readableStream = fs.createReadStream(
  "bigfile.txt",
  { encoding: "utf8" } // wir sagen NodeJS, dass die Datei wie ein utf8 gelesen werden soll
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

Der Code wird nun die Datei in menschenlesbarer Form ausgeben.

### Beschreibbare Ströme

Mit einem beschreibbaren Stream kannst du Daten Stück für Stück irgendwo hinschicken.

Hier ist ein Beispiel für das Schreiben in eine Datei `target.txt` unter Verwendung eines Streams:

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

Das passiert folgendermaßen:

1. `fs.createWriteStream()` erzeugt einen beschreibbaren Stream.
2. Wir schreiben einen Text mit `.write()` hinein.
3. Wenn wir fertig sind, rufen wir `.end()` auf, um den Stream zu schließen.
4. Wenn alle Daten geschrieben worden sind, wird das Ereignis "finish" ausgelöst.
5. Wenn etwas schief geht, wird das Ereignis `error` ausgelöst.

Genau wie lesbare Streams eignen sich auch beschreibbare Streams gut für große Datenmengen, da nicht alles gleichzeitig im Speicher gehalten werden muss.

### Verknüpfung (piping) von Streams

Das Beste an Streams ist, dass man sie miteinander **verknüpfen** kann: z.B. einen lesbaren Stream direkt mit einem schreibbaren Stream verbinden.

```javascript
const fs = require("fs")

const readable = fs.createReadStream("bigfile.txt")
const writable = fs.createWriteStream("target.txt")

readable.pipe(writable)
```

Hier:

* Der lesbare Stream liest von `bigfile.txt`.
* Der beschreibbare Stream schreibt in `copy.txt`.
* `.pipe()` sendet die Daten direkt vom lesbaren zum beschreibbaren Stream.

### Duplex-Streams

Ein Duplex-Stream ist sowohl lesbar als auch beschreibbar. Ein Beispiel ist ein Netzwerk-Socket: Du kannst Daten an ihn senden und von ihm empfangen.

Hier ist ein sehr einfaches Beispiel, das das Modul `net` verwendet:

```javascript
const net = require("net")

const server = net.createServer((socket) => {
  socket.write("Welcome!\n")

  socket.on("data", (chunk) => {
    console.log("Received:",
      chunk.toString()  // wir wandeln den Daten-Brocken von Buffer in eine Zeichenkette um
    )
  })
})

server.listen(3000, () => {
  console.log("Server listening on port 3000")
})
```

In diesem Beispiel:

* Ist das `socket`-Objekt ist Duplex-Stream.
* Man kann darauf "schreiben" (`write()`) und auch auf "Data"-Ereignisse warten.

### Datenströme umwandeln

Ein Transformationsstrom (transform stream) ist ein Duplexstrom, der die Daten, die ihn durchlaufen, ebenfalls verändert.

Du kannst zum Beispiel das eingebaute Modul `zlib` verwenden, um Daten zu komprimieren oder zu dekomprimieren.

So komprimierst du eine Datei mithilfe eines Transformationsstroms:

```javascript
const fs = require("fs")
const zlib = require("zlib")

const readable = fs.createReadStream("bigfile.txt")     // erzeugt einen lesbaren Steam der aus einer Datei liest
const zip = zlib.createGzip()                           // erzeugt ein Transormationsstrom der Daten komprimiert
const writable = fs.createWriteStream("bigfile.txt.gz") // erzeugt einen beschreibbaren Steam der in eine Datei schreibt

readable          // nimm denn lesbaren Stream
  .pipe(zip)      // verknüpfe in mit dem Transformationsstrom um die Daten zu komprimieren
  .pipe(writable) // dann verknüpfe den Ausgang in den beschreibbaren Stream um die Daten in eine Zip-Datei zu speichern

writable.on("finish", () => {
  console.log("File compressed.")
})
```

Und um es wieder zu dekomprimieren:

```javascript
const readable = fs.createReadStream("bigfile.txt.gz")
const unzip = zlib.createGunzip()
const writable = fs.createWriteStream("bigfile.txt")

readable.pipe(unzip).pipe(writable)

writable.on("finish", () => {
  console.log("File decompressed.")
})
```

Transform-Streams sind sehr nützlich für Aufgaben wie Komprimierung, Verschlüsselung oder Änderung von Dateiformaten während des Streamings.

### Rückstau (Backpressure)

Manchmal ist ein beschreibbarer Stream langsam bei der Verarbeitung von Daten. Wenn wir einem beschreibbaren Stream immer wieder Daten schneller zuführen, als er sie verarbeiten kann, kann es zu Problemen kommen. Dies wird **Rückstau** (Backpressure) genannt.

Wenn du die Methode `.write()` für einen beschreibbaren Stream aufrufst, gibt sie einen booleschen Wert zurück, der dich darüber informiert, ob der Stream eine Pause benötigt. Du musst eventuell den Rückgabewert überprüfen, etwa so:

```javascript
const fs = require("fs")

const readable = fs.createReadStream("example.txt")
const writable = fs.createWriteStream("copy.txt")

readable.on("data", chunk => {               // Jeden Brocken den wir vom lesbaren Stream eralten...

  const canContinue = writable.write(chunk)  // ...senden wir an den beschreibbaren Stream, der uns einen Boolean zurückgibt, ob wir weiter machen können

  if (!canContinue) { readable.pause() }     // ...falls das nicht möglich ist, machen wie eine vorübergehende Pause
})

writable.on("drain",                // Der beschreibbare Stream löst ein "drain" Event aus, wenn der Rückstau behoben ist ...

  () => { readable.resume() }       // also machen wir weiter mit dem Lesen (und Schreiben)

)
```

Dies war ein anschauliches Beispiel für die manuelle Weiterleitung von Daten von einem Readable zu einem Writable und die manuelle Verwaltung des Rückstaus.

Normalerweise würden wir Daten mit der Methode `.pipe()` weiterleiten, die den Rückstau automatisch handhabt.

Du musst dir also nur dann Gedanken über Rückstau machen, wenn du aus irgendeinem Grund manuell `.write()` aufrufst.

## Schlussbemerkung
<chapterId>139e2ab8-df67-525a-85f0-5a2fa5e478f2</chapterId>

So, das war's. Wenn du den Lektionen gefolgt bist, solltest du jetzt in der Lage sein, einige einfache Programme in NodeJS zu schreiben.

Ich würde vorschlagen, genau das zu tun: Nachdem man die Grundlagen gelernt hat, ist das Erstellen einiger persönlicher Projekte der beste Weg, um zu üben und ein besserer Programmierer zu werden.

Es ist eigentlich egal, was du baust, wichtig ist, dass du dich der Herausforderung stellst, Probleme mit Code zu lösen.

Moderne Programmiersprachen sind unglaublich leistungsfähig, und NodeJS ist wahrscheinlich der beste Werkzeugkasten, um in dieser Phase deiner Reise damit zu experimentieren.

Viel Glück!

# Letzter Abschnitt
<partId>322624d8-6fbc-11f0-a67a-5b145f10afc1</partId>

## Rezensionen und Bewertungen
<chapterId>3e93ac86-6fbc-11f0-8bae-9b2ed7914843</chapterId>

<isCourseReview>true</isCourseReview>

## Schlussfolgerung
<chapterId>49b3b9b2-6fbc-11f0-9870-5f5adcd3a0eb</chapterId>

<isCourseConclusion>true</isCourseConclusion>
