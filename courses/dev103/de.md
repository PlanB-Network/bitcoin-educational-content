---
name: Grundlagen von JavaScript und NodeJS
goal: Lernen Sie die Grundlagen der JavaScript-Programmierung und der NodeJS-Entwicklung, um praktische Anwendungen und Tools zu erstellen.
objectives: 

  - Beherrschen der grundlegenden JavaScript-Syntax, der Typen und des Kontrollflusses
  - Verstehen von Funktionen, Objekten und Klassen in JavaScript
  - Erlernen von Fehlerbehandlung und Debugging-Techniken
  - Einführung in NodeJS und sein Ökosystem

---

# Beginnen Sie Ihre Entwicklungsreise


Willkommen zu diesem Kurs über JavaScript und NodeJS.


JavaScript ist die beliebteste Programmiersprache der Welt: Sie ist die Skriptsprache moderner Browser, so dass es praktisch unmöglich ist, eine moderne Webanwendung zu erstellen, ohne *etwas* JavaScript zu schreiben; und mit der NodeJS-Laufzeitumgebung kann sie auch außerhalb von Browsern verwendet werden, um Skripte und Anwendungen zu erstellen, die direkt auf Ihrem Computer laufen.


Dieser Kurs richtet sich an Personen, die völlig neu in der Programmierung sind oder die bereits andere Sprachen verwendet haben, aber verstehen wollen, wie JavaScript funktioniert, insbesondere im Kontext von NodeJS.


Am Ende des Kurses sollten Sie in der Lage sein, eigene Programme in JavaScript zu schreiben, die NodeJS-Standardbibliothek zu verwenden und Pakete von Drittanbietern zu installieren und zu verwenden, um nützliche Tools zu erstellen.


+++
# Grundlegendes JavaScript

<partId>a617327c-e5a2-52ca-9380-c63f44623dd4</partId>


## Einrichtung

<chapterId>ba05a290-1782-5268-87c9-62fd09590e05</chapterId>


In diesem Abschnitt werden wir unseren Rechner so einrichten, dass wir unser erstes JavaScript-Programm schreiben und ausführen können.


Ein JavaScript-Programm ist lediglich eine Sammlung von (einer oder mehreren) Textdateien, die Befehle enthalten, die von einer JavaScript-Laufzeitumgebung ausgeführt werden sollen.


Die Namen dieser Textdateien enden in der Regel mit der Dateierweiterung `.js`, wie z.B. `mein_script.js`, `mein_programm.js` usw.


Die darin enthaltenen Befehle sind in der Programmiersprache JavaScript geschrieben.


Eine JavaScript-Laufzeitumgebung ist ein spezielles Programm, das diese Dateien ausführt.


![](assets/en/1.webp)


### NodeJS-Installation


Die am weitesten verbreitete JavaScript-Laufzeitumgebung ist NodeJS.


Sie können es installieren, indem Sie die [offizielle Anleitung](https://nodejs.org/en/download) befolgen.


Auf der Download-Seite finden Sie Anleitungen für alle drei gängigen Betriebssysteme: Windows, Linux und MacOS. Es wird vorausgesetzt, dass Sie wissen, wie man ein Terminal in Ihrem Betriebssystem öffnet.


Da NodeJS für alle drei Betriebssysteme verfügbar ist, können die von Ihnen geschriebenen Programme auf allen Betriebssystemen ausgeführt werden (abgesehen von einigen Randfällen).


Das bedeutet, dass Sie zum Beispiel ein einfaches Videospiel in JavaScript auf Ihrem Windows-PC schreiben und es an Ihren Freund weitergeben können, damit er es auf seinem Mac ausführt.


![](assets/en/2.webp)


### Textbearbeitung


Das Tolle am Programmieren ist, dass man Code mit jedem beliebigen Texteditor schreiben kann, sogar mit dem Standard-Notepad des Betriebssystems.


Es gibt jedoch einige Texteditoren, die auf das Schreiben von Code spezialisiert sind. Einige sind kostenlos erhältlich, für andere müssen Sie eine Lizenz erwerben.


Die Wahl des Code-Editors ist ein riesiges Thema, das den Rahmen dieses Kurses sprengen würde, daher werden wir hier nicht darauf eingehen. Wenn Sie nicht wissen, welchen Sie verwenden sollen, ist der am häufigsten verwendete freie Editor [VSCode] (https://code.visualstudio.com/).


Sein Interface ist ein wenig aufgebläht, aber es hat alles, was Sie brauchen: einen Datei-Editor, einen Datei-Explorer (um die Dateien und Unterverzeichnisse in dem Verzeichnis zu visualisieren, in dem Sie arbeiten) und ein Terminal, um Ihren Code auszuführen. Es unterstützt auch eine Menge von Plugins, und es kommt mit JavaScript-Syntax-Highlighting standardmäßig.


Wenn Sie ein wenig mehr Cypherpunk-y sein wollen, können Sie stattdessen [VSCodium](https://vscodium.com/) verwenden.


### Erstes Programm (Hallo Welt)


Wenn man eine Programmiersprache lernt, besteht das erste Programm, das man schreibt, traditionell darin, "Hallo Welt" auf der Konsole auszugeben.


Erstellen Sie ein Verzeichnis mit dem Namen `my_js_code/` und darin eine Datei mit dem Namen `main.js` (diese Namen sind frei wählbar).


Öffnen Sie das Verzeichnis mit VSCode.


Schreiben Sie diesen Code in Ihre Datei:


```javascript
console.log("hello world!")
```


Öffnen Sie ein Terminal und führen Sie diesen Befehl aus, um das Programm zu starten:


```
node main.js
```


Das Ergebnis sollte sein


```
hello world!
```


### Was geschah


In JavaScript ist alles ein "Objekt".


konsole" ist ein Objekt, das zum Debuggen des Programms verwendet wird.


`console.log` ist die am häufigsten verwendete Methode der `console`. Sie gibt einfach die Argumente aus, die Sie ihr übergeben.


Sie übergeben Argumente an `console.log` unter Verwendung der runden Klammern `()`.


Wenn Sie also zum Beispiel die Zahl "1000" ausgeben wollen, schreiben Sie einfach


```javascript
console.log(1000)
```


Führen Sie ihn dann aus, indem Sie


```
node main.js
```


in Ihrem Terminal (von nun an wird in diesem Kurs davon ausgegangen, dass Sie wissen, wie Sie ein Programm ausführen).


Dies sollte drucken


```
1000
```


Sie können mehrere Dinge übergeben, wie


```javascript
console.log(16, 8, 1993)
```


Damit wird gedruckt


```
16 8 1993
```


## Variablen und Kommentare

<chapterId>23050ab7-343b-5edf-9d37-e4e782e27ce0</chapterId>


Programme führen in der Regel Operationen auf Daten aus.


Variablen sind wie benannte Boxen, die wir zum Speichern von Daten verwenden. Sie ermöglichen es uns, einen Teil der Daten mit einem bestimmten Namen zu verknüpfen, so dass wir sie später unter diesem Namen abrufen können.


### let"-Deklarationen


Um eine Variable in JavaScript zu deklarieren, können wir das Schlüsselwort `let` verwenden.


Nachdem wir `let` geschrieben haben, schreiben wir den Namen, den wir der Variablen geben wollen, dann ein `=` Zeichen und dann den Wert, den wir speichern wollen.


Zum Beispiel:


```javascript
let age = 25

console.log(age)
```


Der Name einer Variablen (technisch als "Bezeichner" bezeichnet) kann normalerweise Buchstaben, Unterstriche (`_`), das Dollarzeichen (`$`) und Zahlen enthalten, wobei das erste Zeichen keine Zahl sein darf.


Im obigen Code haben wir eine Variable namens "Alter" deklariert und den Wert "25" darin gespeichert.


Dann haben wir den Wert mit `console.log(age)` ausgedruckt.


Wenn Sie diesen Code mit `node main.js` ausführen, wird die Ausgabe sein:


```
25
```


Bei Bezeichnern wird die Groß- und Kleinschreibung beachtet, d. h. Klein- und Großbuchstaben zählen als Unterschiede in den Bezeichnern, z. B


```javascript
let age = 25

let Age = 20

console.log(age)
```


gibt 25 aus, da es sich um zwei völlig unterschiedliche Variablen handelt!


Sie können auch Zeichenketten (Text) in einer Variablen speichern:


```javascript
let message = "hello again"

console.log(message)
```


Dies wird gedruckt:


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


Wenn Sie dies ausführen, wird gedruckt:


```
25
hello again
```

### Neuzuweisung


Mit `let` deklarierte Variablen können nach ihrer Erstellung geändert werden.


Dies wird als Neuzuweisung bezeichnet.


```javascript
let score = 10

console.log(score)

score = 15

console.log(score)
```


Zuerst weisen wir `10` dem `Score` zu und drucken ihn dann aus.


Dann ändern wir den Wert von `score` auf `15` und drucken ihn wieder aus.


Die Ausgabe wird sein:


```
10
15
```


Dies ist sehr nützlich, wenn sich der Wert im Laufe der Zeit ändert, z. B. bei einem Spiel, bei dem die Punktzahl steigt.


Lassen Sie uns eine weitere Variable in den Mix einbeziehen:


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


Dies wird gedruckt:


```
10
Alice
20
Bob
```


Wie Sie sehen können, wurden sowohl `Score` als auch `Player` geändert.


### const"-Erklärungen


In den meisten Fällen wollen wir jedoch nicht, dass sich eine Variable nach ihrer Erstellung ändert. Dafür verwenden wir `const`.


const" ist die Abkürzung für "constant". Sobald Sie einer "const"-Variablen einen Wert zuweisen, können Sie ihn nicht mehr ändern.


```javascript
const pi = 3.14
console.log(pi)
```


Dies wird gedruckt:


```
3.14
```


Aber wenn Sie versuchen, dies zu tun:


```javascript
const pi = 3.14
console.log(pi)

pi = 99 // this line will cause an error
console.log(pi)
```


JavaScript wird Ihnen eine Fehlermeldung wie diese ausgeben:


```
TypeError: Assignment to constant variable.
```


Das liegt daran, dass `pi` mit `const` deklariert wurde und Sie seinen Wert danach nicht mehr ändern können. Damit teilen Sie dem JavaScript-Interpreter mit, dass Sie nicht wollen, dass sich die Variable ändert.


Das ist nützlich, weil es die Wahrscheinlichkeit einer versehentlichen Änderung verringert. Wenn Programme sehr groß werden, mit Tausenden von Codezeilen, ist es unmöglich, mit allem, was auf einmal passiert, Schritt zu halten (das ist der Hauptgrund, warum wir Computer benutzen, um komplexe Prozesse auszuführen, die wir mit unserem Gehirn nicht berechnen können), also ist es nützlich, Einschränkungen wie diese zu haben, die das Programm deterministischer machen.


Es gilt als beste Praxis, unsere Werte immer als `const` zu deklarieren, es sei denn, wir sind sicher, dass wir sie später ändern wollen.


### Kommentare in JavaScript


Manchmal möchten wir Notizen in unseren Code schreiben, die nicht ausgeführt werden. Diese werden Kommentare genannt.


Kommentare werden vom Programm ignoriert, wenn es läuft, sind aber nützlich, um uns selbst oder anderen etwas zu erklären.


Um einen einzeiligen Kommentar zu schreiben, verwenden Sie `//`


```javascript
// This is a comment
const x = 10 // This is also a comment
console.log(x)
```


Dies wird trotzdem gedruckt:


```
10
```


Die Kommentare sind nur für Menschen zum Lesen da.


Sie können auch mehrzeilige Kommentare mit `/*` und `*/` schreiben


```javascript
/*
This is a multi-line comment.
It can span several lines.
*/
const y = 20
console.log(y)
```


Damit wird gedruckt


```
20
```


Und der Kommentar wird ignoriert.


Mit Kommentaren können Sie kleine Anmerkungen zu Ihrem Code hinzufügen, damit Sie sich daran erinnern können, was er tut und warum er auf eine bestimmte Weise geschrieben ist. Sie können auch anderen Programmierern helfen, ihn zu verstehen.


## Grundtypen: Zahlen, Zeichenketten, Boolesche Werte

<chapterId>cfdb04f6-21a8-5143-bbf9-7aaae04962f0</chapterId>


In JavaScript gibt ein "Typ" an, um welche Art von Daten es sich bei einem Wert handelt.


Javascript hat einige Grundtypen, und in diesem Abschnitt werden wir einige von ihnen untersuchen.


### Zahlen und arithmetische Operationen


Der erste Typ, den wir einführen werden, ist `Number`.


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


Dies wird gedruckt:


```
15
5
50
2
```


Sie können auch Klammern `()` verwenden, um die Reihenfolge der Operationen zu steuern:


```javascript
const result = (2 + 3) * 4
console.log(result)
```


Dies wird gedruckt:


```
20
```


Ohne die Klammern würde es "2 + 3 * 4" lauten, das ist:


```javascript
const result = 2 + 3 * 4
console.log(result)
```


Das wird gedruckt:


```
14
```


Denn in der normalen Mathematik kommt die Multiplikation vor der Addition.


### Zeichenketten und Interpolation


Der zweite JavaScript-Typ, den wir einführen werden, ist `string`.


Zeichenketten sind Textstücke. Sie können einfache Anführungszeichen `'...'` oder doppelte Anführungszeichen `"..."` verwenden, um sie zu erstellen.


```javascript
const greeting = "hello"
const name = 'Bob'
console.log(greeting)
console.log(name)
```


Dies wird gedruckt:


```
hello
Bob
```


Um Zeichenketten zu kombinieren, können Sie den Operator "+" verwenden:


```javascript
const greeting = "hello"
const space = " "
const name = "Bob"

const fullGreeting = greeting + space + name
console.log(fullGreeting)
```


Dies wird gedruckt:


```
hello Bob
```


Aber es gibt einen schöneren Weg, Zeichenketten zu kombinieren, die **Zeichenfolgeninterpolation**. Sie verwenden Backticks, um die Zeichenkette ``...`` zu deklarieren und schreiben Variablen mit `${...}` innerhalb der Zeichenkette:


```javascript
const greeting = "hello"
const name = "Bob"

const fullGreeting = `${greeting} ${name}`
console.log(fullGreeting)
```


Dies wird auch gedruckt:


```
hello Bob
```


Sie können jeden Ausdruck innerhalb von `${...}` einschließen:


```javascript
const age = 30
console.log(`Next year, I will be ${age + 1} years old.`)
```


Dies wird gedruckt:


```
Next year, I will be 31 years old.
```


Interpolation ist in modernem JavaScript sehr verbreitet.


### Boolesche, vergleichende und logische Operationen


Der dritte Typ, den wir einführen werden, ist "boolesch". Er ist nach dem Mathematiker George Boole benannt, der die boolesche Logik erfand.


Booleans sind einfach: nur zwei mögliche Werte, "wahr" und "falsch".


Sie können sie in Variablen speichern:


```javascript
const theSkyIsBlue = true
const thisCourseIsBad = false

console.log(theSkyIsBlue)
console.log(thisCourseIsBad)
```


Dies wird gedruckt:


```
true
false
```


Sie können Boolesche Begriffe mit logischen Operatoren kombinieren:



- &&" bedeutet "und" und gibt nur dann "wahr" zurück, wenn **beide** Werte "wahr" sind, andernfalls wird "falsch" zurückgegeben
- ||" bedeutet "oder" und gibt "wahr" zurück, wenn **mindestens einer** der Werte "wahr" ist, andernfalls (wenn beide Werte "falsch" sind) gibt es "falsch" zurück
- `!` bedeutet "nicht", es wird vor einem booleschen Wert angewandt und kehrt diesen um: wenn der boolesche Wert "wahr" ist, wird "falsch" zurückgegeben und umgekehrt.


![](assets/en/3.webp)


Beispiele:


```javascript
const isSunny = true
const isWarm = true

console.log(isSunny && isWarm)  // true
console.log(isSunny || isWarm)  // true
console.log(!isSunny)           // false
```


Sie können Werte in JavaScript mit Operatoren wie `>`, `<`, `===` und `!==` vergleichen. Das Ergebnis dieser Vergleiche ist immer ein boolescher Wert.


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


Javascript hat auch `>=`, um "größer oder gleich" zu bedeuten und `<=`, um "kleiner oder gleich" zu bedeuten.


Boolesche Operatoren, Vergleichsoperatoren und logische Operatoren werden in Programmen oft kombiniert, um komplexe Bedingungen zu deklarieren, z. B. "die E-Mail ist angekommen UND sie enthält das Bild, das ich brauche ODER die Länge der E-Mail ist länger als 10000 Zeichen". Sie werden später feststellen, dass dies wichtige Bausteine sind, um die Logik des Programms zu konstruieren.


## Arrays, null, undefiniert

<chapterId>7bf18183-5eae-53ed-83d2-b04982145d81</chapterId>


In diesem Abschnitt werden wir drei weitere Typen behandeln, die in JavaScript-Programmen sehr häufig vorkommen:



- Arrays**: Folgen von Werten
- undefined**: ein spezieller Wert, der bedeutet "es wurde nichts zugewiesen"
- null**: ein weiterer spezieller Wert, der "absichtlich leer" bedeutet


### Arrays und Indexzugriff


Ein **Array** ist ein Typ, der mehrere Werte in einer Liste enthalten kann.


Sie erstellen ein Array, indem Sie eckige Klammern `[]` verwenden und die Elemente mit Kommas trennen.


Hier ist ein einfaches Beispiel:


```javascript
const numbers = [10, 2, 88]
console.log(numbers)
```


Dies wird gedruckt:


```
[ 10, 2, 88 ]
```


In einem Array können Sie alles speichern, nicht nur Zahlen:


```javascript
const things = ["apple", 42, true]
console.log(things)
```


Dies wird gedruckt:


```
[ 'apple', 42, true ]
```


Um auf ein bestimmtes Element im Array zuzugreifen, verwenden wir einen **Index**. Der Index ist die Position des Elements, beginnend mit **0**.


Also in dieser Reihe:


```javascript
const colors = ["red", "green", "blue"]
```



- `Farben[0]` ist `"rot"`
- farben[1]` ist "Green"
- `Farben[2]` ist `"blau"`


Versuchen wir es:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[0])
console.log(colors[1])
console.log(colors[2])
```


Dies wird gedruckt:


```
red
green
blue
```


Sie können einem bestimmten Index eines Arrays einen Wert zuweisen


```javascript
const colors = ["red", "green", "blue"]

colors[1] = "yellow"

console.log(colors)
```


Dies wird gedruckt:


```
[ 'red', 'yellow', 'blue' ]
```


Sie können jede natürliche Zahl als Index verwenden, auch eine, die in einer Variablen gespeichert ist


```javascript

const i = 1
const colors = ["red", "green", "blue"]
console.log(colors[i])
```


Dies wird gedruckt:


```
green
```


Wenn Sie jedoch versuchen, auf einen Index zuzugreifen, der nicht existiert, erhalten Sie `undefined`:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[3])
```


Dies wird gedruckt:


```
undefined
```


Was ist das?


### undefiniert


Der spezielle Wert `undefined` bedeutet "es wurde kein Wert zugewiesen".


Wenn Sie eine Variable erstellen, ihr aber keinen Wert zuweisen, ist sie "undefiniert":


```javascript
const name
console.log(name)
```


Dies wird gedruckt:


```
undefined
```


Da wir `name` nichts zugewiesen haben, setzt JavaScript ihn standardmäßig auf `undefined`.


Wie zuvor gesehen, kann man auch `undefined` bekommen, wenn man auf einen Array-Index zugreift, der nicht existiert:


```javascript
const fruits = ["banana", "apple"]
console.log(fruits[2]) // There is no index 2
```


Dies wird gedruckt:


```
undefined
```


### `null` und wie es zu behandeln ist


null" ist auch ein besonderer Wert. Er bedeutet "hier ist nichts, und das habe ich absichtlich gemacht"


Im Gegensatz zu `undefined`, das automatisch ist, ist `null` etwas, das Sie selbst festlegen.


Zum Beispiel:


```javascript
const currentUser = null
console.log(currentUser)
```


Dies wird gedruckt:


```
null
```


Warum `null` verwenden? Vielleicht erwarten Sie später einen Wert, aber er ist noch nicht fertig:


```javascript
let winner = null

// Later in the program:
winner = "Alice"

console.log(winner)
```


Dies wird gedruckt:


```
Alice
```


So ist `null` nützlich, wenn man z.B. sagen will: "Hier sollte später etwas stehen, aber im Moment ist es leer."


## Blöcke und Kontrollfluss

<chapterId>be985168-2636-5b0d-a48f-ac1bbfbff8a7</chapterId>


Bislang haben wir hauptsächlich Codezeilen geschrieben, die nacheinander ablaufen.


Aber wenn wir kodieren, können wir die Reihenfolge der Ausführung kontrollieren.


Dies wird als **Kontrollfluss** bezeichnet.


Beginnen wir mit dem Verständnis von Blöcken und Umfang.


### Der globale Geltungsbereich


Jede Variable, die wir deklarieren, existiert in einem **Scope**, d. h. in dem Bereich des Codes, in dem die Variable bekannt ist.


Wenn Sie eine Variable außerhalb eines Blocks deklarieren, existiert sie im **globalen Bereich**.


```javascript
const color = "blue"
console.log(color)
```


Die Variable `color` befindet sich im globalen Bereich, so dass von überall in der Datei auf sie zugegriffen werden kann.


Wenn Sie weitere Zeilen hinzufügen:


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


Ein **Block** ist ein Teil des Codes, der von geschweiften Klammern "{}" umgeben ist.


Mit `let` oder `const` deklarierte Variablen innerhalb eines Blocks existieren **nur** innerhalb dieses Blocks.


```javascript
{
const message = "inside block"
console.log(message)
}
```


Dies wird gedruckt:


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


JavaScript wird Ihnen eine Fehlermeldung wie diese ausgeben:


```
ReferenceError: message is not defined
```


Das liegt daran, dass `message` innerhalb des Blocks deklariert wurde und außerhalb des Blocks nicht existiert.


Das bedeutet, dass wir Blöcke verwenden können, um Teile unseres Codes zu isolieren und sicher zu sein, dass "was im Block passiert, im Block bleibt" (ähnlich wie in Las Vegas).


Wenn wir unseren Code in Blöcken organisieren, können wir auch die Ausführung des Programms mit Kontrollflusskonstrukten wie "wenn" strukturieren


### wenn", "sonst


Manchmal wollen wir Code **nur** ausführen, wenn etwas wahr ist. Dafür ist die "if"-Anweisung gedacht.


```javascript
const myAge = 20

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Dies wird gedruckt:


```
Am I an adult?
Yes I am!
```


Wie Sie sehen können, vergleicht der Code `myAge` und `18`.

In diesem Fall gibt der ">="-Operator "wahr" zurück, so dass der Block ausgeführt wird.

Wenn die Bedingung nicht `true` ist, wird der Block nicht ausgeführt.


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Dies wird gedruckt:


```
Am I an adult?
```


Sie können einen `else`-Block hinzufügen, um den umgekehrten Fall zu behandeln:


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
} else {
console.log("No, I am not.")
}
```


Dies wird gedruckt:


```
Am I an adult?
No, I am not.
```


Sowohl die `if`- als auch die `else`-Blöcke sind immer noch Blöcke - also existieren die darin deklarierten Variablen nicht außerhalb.


Wenn wir sicher sein wollen, dass etwas **nicht** wahr ist, was können wir dann tun?


Nun, wie bereits erwähnt, verfügt JavaScript über einen "not"-Operator, der Boolesche Werte umkehrt. Wir können also tun


```javascript
const myAge = 17

const adult = myAge >= 18

console.log("Am I an adult?")

if (!adult) {
console.log("No, I am not.")
}
```

Dies wird immer noch gedruckt:


```
Am I an adult?
No, I am not.
```

Weil wir den Operator `!` verwendet haben, um die Variable `adult` zu invertieren.


if (!adult) {...}" sollte als "if not adult..." gelesen werden


Mit Hilfe von Blöcken, Logik und Vergleichsoperatoren können wir die Ausführung des Programms strukturieren, indem wir Variablen definieren, die "wahr" (oder "falsch") sein müssen, damit etwas passiert.


### während", "unterbrechen", "fortsetzen


Eine "while"-Schleife wiederholt den Code, *so lange* eine Bedingung erfüllt ist.


```javascript
let count = 0

while (count < 3) {
console.log("Count is", count)
count = count + 1
}
console.log("the loop is over!")
```


Dies wird gedruckt:


```
Count is 0
Count is 1
Count is 2
the loop is over!
```


Wenn `count` 3 wird, stoppt die Schleife.


Sie können eine Schleife mit `break` vorzeitig beenden:


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


Dies wird gedruckt:


```
0
1
2
```


Denn wenn die Zahl `3` wird, wird der `if`-Block ausgeführt und die Schleife wird angehalten.


Sie können den Rest einer Schleife mit `continue` überspringen:


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


Dies wird gedruckt:


```
1
2
4
5
```


Denn als die Zahl `3` war, ließ `continue` das Programm die Zeile überspringen, die die Zahl ausgibt.


### "für ... von ..


Wenn Sie ein Array haben und etwas mit jedem Element darin machen wollen, können Sie `for ... of ... {...}`.


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const fruit of fruits) {
console.log(fruit)
}
```


Dies wird gedruckt:


```
apple
banana
cherry
```

Der Block wird für jedes Element des Arrays einmal ausgeführt.


fruit" ist hier eine neue Variable, die den Wert jedes Elements im Array aufnimmt, um es innerhalb des Blocks zu bearbeiten.


### für ... in ..


Sie können `for ... in` verwenden, um eine Schleife über die Schlüssel (Indizes) eines Arrays zu ziehen:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(index)
}
```


Dies wird gedruckt:


```
0
1
2
```


Sie können auch den Index verwenden, um den Wert zu erhalten:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(fruits[index])
}
```


Dies druckt dasselbe wie `for ... of`:


```
apple
banana
cherry
```


In der Praxis sollten Sie für Arrays lieber `for ... of` verwenden, da dies einfacher und sauberer ist.


### Begrenzte Schleifen


Manchmal möchte man eine bestimmte Anzahl von Schleifen durchlaufen oder ganz allgemein einen Code schreiben, der einen Block wiederholt und dabei etwas verfolgt.

Dafür ist eine begrenzte "for"-Schleife gut.

Eine begrenzte Schleife enthält normalerweise drei Bedingungen, die durch ein Semikolon `;` getrennt sind, wie in `(... ; ... ; ....)`.


```javascript
for (let i = 0; i < 3; i = i + 1) {
console.log(i)
}
```


Dies wird gedruckt:


```
0
1
2
```


Lassen Sie es uns erklären:



- `let i = 0`: deklariert eine Variable, die im Block verwendet werden soll (in diesem Fall ist es ein Zähler, der bei 0 beginnt)
- `i < 3`: deklariert eine Bedingung, die `wahr` sein muss, damit der Block ausgeführt wird (in diesem Fall ist es "wiederholen, solange `i` kleiner als 3 ist")
- `i = i + 1`: deklariert einen Code, der nach jeder Ausführung des Blocks ausgeführt wird (in diesem Fall "erhöhe `i` um 1")


Wie Sie sehen können, können wir mit der begrenzten Schleife komplexere Bedingungen für die wiederholte Ausführung eines Codestücks deklarieren, aber meistens ist das nicht notwendig.


### Block-Etiketten


Wenn Sie einen komplexeren Kontrollfluss schreiben müssen, können Sie in JavaScript einen Block mit einem **Label** benennen, das von `break` oder `continue` verwendet werden kann, um anzugeben, *wo* zurückgesprungen werden soll.


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


Dies wird gedruckt:


```
Inside outer block
Inside inner block
Done
```


Wir haben `break outer` verwendet, um den `outer`-Block vollständig zu verlassen.


Sie können auch Schleifen beschriften. Nehmen wir dieses Beispiel:


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

Dies war ein sehr langweiliges Beispiel, aber es hat hoffentlich die (gelegentliche) Notwendigkeit von Etiketten verdeutlicht.


## Einführung von Funktionen

<chapterId>cc324715-09c2-5cf7-9e6f-47a6f16bc04d</chapterId>


Wenn Ihre Programme wachsen, werden Sie oft Teile des Codes **wiederverwenden** wollen.


Dafür sind **Funktionen** da: Sie ermöglichen es Ihnen, Code zu gruppieren, ihm einen Namen zu geben und ihn auszuführen, wann immer Sie wollen.


### Funktionserklärung


Um eine Funktion zu deklarieren, können wir das Schlüsselwort `Funktion` verwenden. Dann geben wir ihr einen Namen, ein Klammerpaar `()` mit den Argumenten, die sie benötigt, und einen Codeblock `{}`, der ausgeführt werden soll. Beginnen wir mit einer Funktion, die keine Argumente benötigt:


```javascript
function sayHello () {console.log(`Hello!`) }
```


Dieser Code **deklariert** die Funktion, führt sie aber **noch** nicht aus.


### Funktionsaufrufe


Um die Funktion auszuführen (oder "aufzurufen"), schreiben Sie ihren Namen, gefolgt von Klammern:


```javascript
function sayHello () {console.log(`Hello!`) }
sayHello()
```


Dies wird gedruckt:


```
Hello!
```


Sie können die Funktion so oft aufrufen, wie Sie wollen:


```javascript
function sayHello() {
console.log("Hello!")
}

sayHello()
sayHello()
```


Dies wird gedruckt:


```
Hello!
Hello!
```


Der Code innerhalb der Funktion wird nur ausgeführt, wenn Sie sie aufrufen.


### Funktionsargumente (Eingabe in Funktionen)


Manchmal möchte man, dass eine Funktion mit einer bestimmten Eingabe arbeitet. Das können Sie tun, indem Sie **Argumente** innerhalb der Klammern hinzufügen.


Zum Beispiel:


```javascript
function sayHelloTo (friend) {
console.log(`Hello ${friend}!`)
}
```


Diese Funktion benötigt **ein Argument** namens "Freund".


Wenn Sie die Funktion aufrufen, können Sie einen Wert übergeben:


```javascript
sayHelloTo("Tommy")
```


Dies wird gedruckt:


```
Hello Tommy!
```


Sie können die Funktion mit einem anderen Namen erneut aufrufen:


```javascript
sayHelloTo("Sam")
```


Dies wird gedruckt:


```
Hello Sam!
```


Der Wert, den Sie übergeben, ersetzt die Variable `friend` innerhalb der Funktion.


Sie können auch mehr als ein Argument verwenden:


```javascript
function greetTwoPeople(person1, person2) {
console.log(`Hello ${person1} and ${person2}!`)
}

greetTwoPeople("Lina", "Marco")
```


Dies wird gedruckt:


```
Hello Lina and Marco!
```


### return" (Ausgabe von Funktionen)


Funktionen können auch Werte **zurückgeben**. Das heißt, sie senden einen Wert zurück an den Ort, an dem die Funktion aufgerufen wurde.


Hier ist ein einfaches Beispiel:


```javascript
function getNumber() {
return 42
}

const result = getNumber()
console.log(result)
```


Dies wird gedruckt:


```
42
```


Die Funktion `getNumber()` gibt `42` zurück, und wir speichern sie in `result` und drucken sie dann aus.


Sie können auch etwas zurückgeben, das Sie berechnen:


```javascript
function add(a, b) {
return a + b
}

const result = add(2, 3)
console.log(result)
```


Dies wird gedruckt:


```
5
```


Sobald ein Wert "zurückgegeben" wird, endet die Funktion. Alles, was nach "Return" in diesem Block kommt, passiert nicht.


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


Sie können sich Funktionen als kleine Unterprogramme vorstellen. Jede Funktion kann eine Eingabe entgegennehmen, diese bearbeiten und eine Ausgabe zurückgeben.


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


Das bedeutet, dass es Ihnen hilft, Ihren Code zu organisieren, indem es Werte und Funktionen zu **Objekten** zusammenfasst.


### Was ist ein `Objekt`?


Ein Objekt kann Daten und Funktionen enthalten, die mit diesen Daten arbeiten. Wenn eine Funktion in ein Objekt eingefügt wird, spricht man von einer "Methode".


Das erste Objekt, das wir gesehen haben, war das Objekt "Konsole". Es ist ein Objekt, das mehrere Methoden enthält, um Dinge auf dem Bildschirm zu drucken und unsere Programme zu debuggen.


Es kann sogar selbst drucken; Sie können


```javascript
console.log(console)
```


und es wird eine Liste der darin enthaltenen Methoden ausgegeben. Auf meinem Rechner wird zum Beispiel Folgendes ausgegeben


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


Wie Sie sehen können, hat es viele Methoden, die Sie zum Debuggen verwenden können!


Javascript bietet uns verschiedene Möglichkeiten, neue Objekte zu erstellen, die alles tun können, was wir von ihnen verlangen.


### Erstellen eines Objekts


Die einfachste Art, ein Objekt zu erstellen, ist die Gruppierung von Daten und Funktionen mit **geschweiften Klammern** "{}".


Dadurch wird ein so genanntes **anonymes Objekt** geschaffen


```javascript
const cat = {
name: "Whiskers",
age: 3
}
```


Dies erzeugt ein Objekt und speichert es in einer Variablen namens `cat`.


Das Objekt hat zwei **Eigenschaften**:



- name" mit dem Wert "Whiskers"
- alter" mit dem Wert "3


Drucken wir es aus:


```javascript
console.log(cat)
```


Dies wird gedruckt:


```
{ name: 'Whiskers', age: 3 }
```


Sie können die Eigenschaften aus dem Objekt mit einem Punkt abrufen, wie in "Objektname.Eigenschaftsname":


```javascript
console.log(cat.name)  // prints "Whiskers"
console.log(cat.age)   // prints 3
```


Sie können eine Eigenschaft auch **ändern**:


```javascript
cat.age = 4
console.log(cat.age)  // now it prints 4
```


Wie Sie sehen, können Sie die darin enthaltenen Daten auch dann ändern, wenn ein Objekt als "const" definiert ist.


Im Falle von Objekten verhindert `const` nur, dass Sie das gesamte Objekt überschreiben:


```javascript
const cat = {
name: "Whiskers",
age: 3
}

cat.age = 5 // this works

cat = 5 // this throws an error, you're trying to reassign the whole object

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



- Eine Eigenschaft "Name"
- Eine "Speak()"-Methode


Rufen wir die Methode auf:


```javascript
cat.speak()
```


Er druckt:


```
Meow!
```


Methoden können die Daten, die das Objekt enthält, durch das Schlüsselwort "this" verwenden.

this" bezieht sich auf das aktuelle Objekt. In diesem Beispiel wird es verwendet, um den Namen der Katze zu drucken:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log(`${this.name} says meow!`)
}
}

cat.speak()
```


Dies wird gedruckt:


```
Whiskers says meow!
```


Das Wort "dies" bedeutet "dieses Objekt", in diesem Fall das Objekt "Katze".



Diese Art von Objekten ist ideal, wenn Sie nur etwas Schnelles und Einfaches wollen. Wenn Sie jedoch **viele Objekte** mit der gleichen Struktur erstellen müssen, gibt es einen besseren Weg, und hier kommen **Klassen** ins Spiel.


### Klassen und Konstrukteure


Eine **Klasse** ist wie eine Blaupause. Sie sagt JavaScript, wie eine bestimmte Art von Objekt zu erstellen ist.


Sie definieren eine Klasse mit dem Schlüsselwort "class", gefolgt von dem Namen der Klasse und einem Block mit geschweiften Klammern "{}".


```javascript
class Dog {}
```


Klassen beginnen in der Regel mit einem Großbuchstaben, wie es üblich ist.


Mit `new` können Sie ein neues Objekt einer Klasse erstellen:


```javascript
const hachiko = new Dog()
```


Versuchen Sie, das Objekt zu drucken:

```javascript
class Dog {}

const myDog = new Dog()

console.log(myDog)
```


Sie erhalten


```
Dog {}
```


Wie Sie sehen können, ist die Klasse Dog leer, also ist auch das Objekt "myDog" leer.


Wir können festlegen, welche Eigenschaften Hundeobjekte enthalten sollen, indem wir einen "Konstruktor" hinzufügen.


Ein Konstruktor ist eine spezielle Funktion, die ausgeführt wird, wenn Sie ein neues Objekt erstellen (oder "konstruieren").


```javascript
class Dog {
constructor() { }
}
```


Wir wollen, dass jeder Hund einen Namen hat, also fügen wir der Funktion einen Parameter "Name" hinzu:


```javascript
class Dog {
constructor(name) { }
}
```


Und dann benutzen wir `this`, um zu deklarieren, dass `name` der `Name` des `Dog`-Objekts ist, das wir erstellen


```javascript
class Dog {
constructor(name) {
this.name = name
}}
```


Versuchen wir, es jetzt zu benutzen:


```javascript
class Dog {
constructor(name) {
this.name = name
}
}

const myDog = new Dog("hachiko")

console.log(myDog)
```


Dies druckt etwas wie:


```
Dog { name: 'hachiko' }
```


Wie du siehst, nimmt die Methode "Konstruktor" die Argumente, die du der Klasse übergibst, wenn du "neuer Hund()" aufrufst, und benutzt sie, um das Objekt zu erstellen.


Schauen wir uns das mal an:



- die "Klasse Hund" definiert die Klasse Hund.
- `constructor(name)` richtet das Objekt ein, wenn es erstellt wird.
- this.name = name" speichert den Wert in dem neuen Objekt.
- new Dog("hachiko")` erzeugt ein neues Objekt der Klasse, wobei die Eigenschaft "name" auf "hachiko" gesetzt wird.


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


Damit wird gedruckt


```javascript
hachiko says barf!
```


Wenn wir das Gleiche für zwei verschiedene Instanzen von Dog tun



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


die Methode "Speak()" verwendet die Eigenschaft "Name" des "Hundes", auf den sie angewendet wird.


Das ist der Hauptgrund für die Existenz von Klassen: Sie ermöglichen es uns, eine Reihe von Methoden zu definieren, die mit Daten arbeiten, und dann mehrere Objekte zu erstellen, die dieselbe Daten-"Form" haben.


Wenn wir eine Methode für eines dieser Objekte aufrufen, wird sie mit den Daten arbeiten, die *das spezifische Objekt* enthält.


### Ändern der Form eines Objekts


Objekte in JavaScript sind flexibel. Selbst nachdem Sie ein Objekt erstellt haben, können Sie noch neue Eigenschaften hinzufügen oder vorhandene entfernen.


Es ist erlaubt, aber Sie sollten es mit Bedacht einsetzen.


Beginnen wir mit unserer einfachen Klasse "Hund":


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


Zu diesem Zeitpunkt hat `myDog` nur eine Eigenschaft: `Name`. Wir können immer noch neue Eigenschaften hinzufügen, nachdem er erstellt wurde:


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


Das funktioniert, aber es gibt etwas Wichtiges zu wissen: JavaScript-Engines wie V8 (verwendet in Node.js und im Chrome-Browser) laufen schneller, wenn Ihre Objekte immer dieselben Eigenschaften haben. Wenn Sie Eigenschaften hinzufügen oder entfernen, nachdem das Objekt erstellt wurde, kann dies die Abläufe verlangsamen.


Bei kleinen Programmen spielt das keine große Rolle. Aber bei größeren Projekten (wie Spielen) ist es besser, alle Eigenschaften von Anfang an im Konstruktor aufzulisten, auch wenn Sie sie nicht sofort verwenden. Dadurch bleibt die Form des Objekts stabil und Ihr Code läuft schneller.


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


Sie könnten Folgendes tun


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


Beide Versionen funktionieren, aber die zweite ist besser für die Leistung. Sie sagen der Engine im Voraus, welche Eigenschaften jedes Objekt haben wird, und sie kann entsprechend optimieren.


In JavaScript können Sie Objekte frei umgestalten, aber bei der Verwendung von Klassen ist es am besten, die Form Ihres Objekts im Voraus zu planen.



### Vererbung mit `extends` und `super()`


Manchmal möchte man eine Klasse erstellen, die *fast* die gleiche ist wie eine andere Klasse, aber ein paar zusätzliche Funktionen hat.


Anstatt die Form von Objekten zu ändern (was, wie bereits erwähnt, nicht optimal für die Leistung ist) oder eine neue Klasse von Grund auf neu zu schreiben, können Sie in JavaScript etwas verwenden, das **Vererbung** genannt wird.


Vererbung bedeutet, dass eine Klasse eine andere **erweitern** kann. Die neue Klasse erhält alle Eigenschaften und Methoden der alten Klasse, und Sie können weitere hinzufügen oder ändern, was Sie brauchen.


Nehmen wir an, wir haben eine Basisklasse namens "Fahrzeug":


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


Jetzt wollen wir eine Klasse `Car` erstellen. Ein Auto ist eine Art von Fahrzeug, aber wir wollen vielleicht, dass es einige zusätzliche Funktionen hat oder eine andere Nachricht, wenn es startet. Anstatt alles neu zu schreiben, können wir `extends` verwenden:


```javascript
class Car extends Vehicle {
start() {
console.log(`${this.brand} car is ready to drive!`)
}
}
```


Die Klasse "Car" **erbt** jetzt alles von "Vehicle". Sie erhält die Eigenschaft "Brand", und wir haben die Methode "Start()" durch unsere eigene Version ersetzt.


![](assets/en/4.webp)


Probieren wir es aus:


```javascript
const myCar = new Car("Toyota")
myCar.start()
```


Dies wird gedruckt:


```
Toyota car is ready to drive!
```


Auch wenn `Car` keinen eigenen Konstruktor hat, verwendet es den von `Vehicle`. Aber wenn wir einen eigenen Konstruktor in `Car` schreiben wollen, können wir das, wir müssen nur einen Aufruf an den Konstruktor seines Elternteils mit `super()` einfügen.


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



Dies wird gedruckt:


```
Toyota Corolla is ready to drive!
```


Zusammenfassend also



- erweitert" bedeutet, dass eine Klasse auf einer anderen basiert.
- mit `super()` wird der Konstruktor der zu erweiternden Klasse aufgerufen.
- Die neue Klasse erhält alle Eigenschaften und Methoden der ursprünglichen Klasse.
- Man kann Methoden (wie `start()`) **überschreiben**, damit sie etwas anderes tun.


Dies ist hilfreich, wenn Sie mehrere ähnliche Dinge haben (z. B. Autos, Lastwagen und Fahrräder) und möchten, dass sie einen gemeinsamen Code haben, sich aber dennoch auf ihre eigene Weise verhalten.


### instanz von


Das Schlüsselwort `instanceof` prüft, ob ein Objekt von einer bestimmten Klasse erzeugt wurde.


Nehmen wir an, wir haben eine Klasse namens "Benutzer":


```javascript
class User {
constructor(username) {
this.username = username
}
}

const regularUser = new User("julia123")

console.log(regularUser instanceof User)
```


Dies wird gedruckt:


```
true
```


Bestätigen, dass `regularUser` ein `User` ist. Das liegt daran, dass `regularUser` mit der Klasse `User` erstellt wurde.


Es funktioniert auch mit **vererbten** Klassen. Hier ist zum Beispiel eine "Admin"-Klasse, die "User" erweitert:


```javascript
class Admin extends User {}

const ourAdmin = new Admin("admin42")

console.log(ourAdmin instanceof Admin)   // true
console.log(ourAdmin instanceof User)    // true
```


Beide Zeilen geben `true` zurück. Das liegt daran, dass `Admin` eine Unterklasse von `User` ist, daher ist `unserAdmin` sowohl ein `Admin` als auch ein `User`


# Fortgeschrittenes JavaScript

<partId>243f63ab-4f34-5c30-80cb-84ef46f6761d</partId>


## Fehlerbehandlung

<chapterId>d0206bc5-d386-5e7f-9917-5803f392448c</chapterId>


Wenn Sie komplexere JavaScript-Programme schreiben, werden Sie auf **Fehler** stoßen. Das sind unerwartete Situationen, in denen etwas schief geht. Vielleicht ist eine Variable "undefiniert", aber Sie versuchen, sie zu verwenden, oder ein Code empfängt die falsche Art von Eingabe.


Wenn wir mit diesen Fehlern nicht richtig umgehen, kann unser Programm abstürzen oder sich auf unvorhersehbare Weise verhalten. JavaScript bietet Werkzeuge zum Erkennen und Verwalten dieser Fehler, damit wir sie besser behandeln können.


### Häufiger Fehler: Zugriff auf einen Wert auf `undefined`


Hier ist eine häufige Situation, die einen Fehler verursacht:


```javascript
const user = undefined
console.log(user.name)
```


Wenn Sie diesen Code ausführen, erhalten Sie eine Fehlermeldung, die wie folgt aussieht:


```
TypeError: Cannot read properties of undefined (reading 'name')
```


Das ist JavaScript, das Ihnen sagt: "Hey, du hast versucht, die Eigenschaft `name` von etwas zu erhalten, das `undefined` ist, und das macht keinen Sinn." Und wie Sie sehen können, wenn diese Art von Fehler auftritt, hört das Programm auf zu laufen, es sei denn, Sie haben speziellen Code geschrieben, um ihn abzufangen und zu behandeln.


### einen Fehler "auslösen


Manchmal möchten Sie in Ihrem Code manuell **einen Fehler** auslösen. In diesem Fall verwenden Sie das Schlüsselwort "throw".


```javascript
throw new Error("This is a custom error message")
```


Dadurch wird das Programm sofort angehalten und gedruckt:


```
Uncaught Error: This is a custom error message
```


Sie können `throw` verwenden, um Regeln in Ihrem Programm durchzusetzen. Zum Beispiel:


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


Wenn Sie nicht wollen, dass Ihr Programm abstürzt, wenn ein Fehler auftritt, können Sie den Fehler mit einem "try...catch"-Block abfangen. Dies ist hilfreich, wenn Sie möchten, dass Ihr Programm **weiterläuft**, auch wenn etwas fehlschlägt.


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log("Oops! Something went wrong.")
}
```


Ausgabe:


```
Oops! Something went wrong.
```


Und so funktioniert es:



- Der Code innerhalb des `try`-Blocks wird zuerst ausprobiert.
- Wenn ein Fehler auftritt, **springt JavaScript zum `catch'-Block** und überspringt den Rest des `try'-Blocks.
- Der `catch`-Block empfängt den Fehler, so dass Sie ihn ausgeben oder auf andere Weise behandeln können, wie zum Beispiel


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log(`The message of the error was: "${error.message}"`)
}
```


Ausgabe:


```
The message of the error was: "Cannot read properties of undefined (reading 'name')"
```


### Der `finally`-Block


Sie können auch einen `finally`-Block hinzufügen. Dies ist ein Code, der **immer** läuft, egal ob ein Fehler aufgetreten ist oder nicht.


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


## Vermeiden von Wanzen

<chapterId>db12d9f6-5806-514c-998e-0ae24805104e</chapterId>


Dieses Kapitel zeigt einige der häufigsten Fallstricke in JavaScript und wie man sie vermeiden kann.


### `var` und Assignment ohne Deklaration


In älterem JavaScript-Code wurden Variablen oft mit dem Schlüsselwort `var` deklariert. Im Gegensatz zu `let` und `const`, die Sie bereits kennengelernt haben, kann sich `var` auf verwirrende Weise verhalten.


Zum Beispiel:


```javascript
{
var message = "hello"
}
console.log(message)
```


Man könnte erwarten, dass `message` nur innerhalb des Blocks existiert, aber das ist nicht der Fall. die Variable "var" ignoriert den Blockbereich und macht die Variable in der gesamten Funktion oder Datei verfügbar.


Dies kann zu unerwartetem Verhalten führen, besonders in größeren Programmen. Aus diesem Grund sollte moderner JavaScript-Code immer `let` oder `const` anstelle von `var` verwenden.


Schlimmer noch, in JavaScript können Sie Variablen Werte zuweisen, **ohne sie überhaupt zu deklarieren**:


```javascript
function greet() {
user = "Alice"
}
greet()
console.log(user) // prints "Alice"
```


Dadurch wird eine neue globale Variable `name` ohne jegliche Deklaration erstellt. Dies kann unbemerkt geschehen und zu Fehlern führen, die Hard aufspüren kann, besonders wenn es nur ein Tippfehler war. Deklarieren Sie Variablen immer mit `let` oder `const`.


### Schwaches Typensystem


JavaScript ist schwach typisiert, d.h. es konvertiert bei Bedarf automatisch Werte von einem Typ in einen anderen. Dies wird Typzwang genannt, und obwohl es bequem sein kann, führt es oft zu verwirrenden Ergebnissen.


Zum Beispiel:


```javascript
console.log("5" + 1)    // "51"
console.log("5" - 1)    // 4
console.log(true + 1)   // 2
console.log(null + 1)   // 1
```


In diesen Beispielen versucht JavaScript zu erraten, was Sie gemeint haben. Manchmal verwandelt es Zeichenketten in Zahlen, Boolesche Werte in Zahlen oder Zeichenketten in Zeichenketten. Dies kann dazu führen, dass sich Ihr Code auf unerwartete Weise verhält.


Es ist wichtig, sich des schwachen Typisierungssystems von JavaScript bewusst zu sein. Wenn Dinge anfangen, sich seltsam zu verhalten, kann das an unerwarteter Typenzwangsweise liegen.


### `"use strict"`


Sie können einen strengeren Modus aktivieren, der einige stille Fehler zu echten Fehlern macht und Sie davon abhält, einige der gefährlicheren Funktionen der Sprache zu verwenden.


Um diesen strengeren Modus zu aktivieren, fügen Sie diese Zeile am Anfang Ihrer Datei oder Funktion ein:


```javascript
"use strict"
```


Zum Beispiel:


```javascript
"use strict"
name = "Alice" // ReferenceError: name is not defined
```


Ohne den Strict-Modus würde JavaScript stillschweigend eine globale Variable mit dem Namen "Name" erstellen. Im Strict-Modus wird dies jedoch zu einem echten Fehler, so dass Sie Fehler früher erkennen können.


Im strikten Modus werden auch einige veraltete JavaScript-Funktionen deaktiviert, und Ihr Code lässt sich leichter optimieren und warten.


## Wert vs. Referenz

<chapterId>bb898425-dc2f-5e5c-864b-0cb7a4a9aea9</chapterId>


JavaScript behandelt verschiedene Arten von Werten auf unterschiedliche Weise.


Einige Werte werden **kopiert**, wenn Sie sie einer Variablen zuweisen.


Andere werden **geteilt**, wenn Sie sie einer neuen Variablen zuweisen. Wenn Sie also eine Variable ändern, ändert sich auch die andere.


### Übergabe nach Wert


Wenn ein Wert **nach Wert** übergeben wird, erstellt JavaScript eine **Kopie** des Wertes.


Wenn Sie also eines ändern, hat das keine Auswirkungen auf das andere.


Dies geschieht mit primitiven Typen, wie:



- zahlen
- zeichenketten
- boolesche Werte (`true` und `false`)
- `Null`
- undefiniert


Schauen wir uns ein Beispiel an:


```javascript
let a = 5
let b = a

b = 10

console.log(a) // 5
console.log(b) // 10
```


Wir haben `b` den Wert von `a` gegeben, aber dann haben wir `b` in `10` geändert.


Da Zahlen nach Wert übergeben werden, kopiert JavaScript die "5" in "b". Die "5" in "b" ist unabhängig von der ursprünglichen "5" in "a", so dass eine Änderung des Wertes von "b" keine Auswirkungen auf "a" hat.


Versuchen wir es mit einer Zeichenkette:


```javascript
let name1 = "Alice"
let name2 = name1

name2 = "Bob"

console.log(name1) // Alice
console.log(name2) // Bob
```


Auch hier hatte die Änderung von "Name2" keine Auswirkungen auf "Name1", da Zeichenketten auch als Wert übergeben werden.


Das Gleiche passiert, wenn Sie ein Primitiv an eine Funktion übergeben: Es wird kopiert. Die Funktion kann also das Original nicht ändern.


```javascript
function plusOne(x) {
x = x + 1
}

let number = 5

plusOne(number)

console.log(number) // 5
```


Obwohl innerhalb der Funktion `1` zu `x` hinzugefügt wurde, hat sich die ursprüngliche `Zahl` nicht geändert.


Das liegt daran, dass nur eine **Kopie** an die Funktion übergeben wurde.


### Übergabe durch Referenz


Objekte werden **per Referenz** übergeben.


Das heißt, anstatt sie zu kopieren, übergibt JavaScript einfach einen **Verweis** auf sie, und wenn Sie sie ändern, sehen alle anderen Variablen, die auf sie zeigen, die Änderung ebenfalls.


Zum Beispiel:


```javascript
const person1 = { name: "Alice" }
const person2 = person1

person2.name = "Bob"

console.log(person1.name) // Bob
console.log(person2.name) // Bob
```


Sowohl `person1` als auch `person2` zeigen auf dasselbe Objekt im Speicher.


Wenn wir also `Person2.name` geändert haben, haben wir auch `Person1.name` geändert, weil sie beide dasselbe betrachten.


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


Die Funktion hat das Objekt geändert! Das liegt daran, dass sie eine **Referenz** auf das ursprüngliche Objekt "Person" erhalten hat.


Er hat keine Kopie erhalten. Es erhielt Zugriff auf das Originalobjekt und damit die Möglichkeit, es zu verändern.


Es ist wichtig, sich diese Unterscheidung zu merken, denn sonst könnte sich unser Code anders verhalten, als wir es erwarten. Wir könnten zum Beispiel eine Funktion mit der Erwartung schreiben, dass sie die Argumente, die sie erhält, nicht verändert, und später herausfinden, dass sie sie tatsächlich verändert hat (weil sie Objekte waren, also per Referenz übergeben wurden).


## Arbeiten mit Funktionen

<chapterId>e0d277a8-c642-5af7-9e53-dee27c811967</chapterId>


Sie haben bereits gelernt, wie man Funktionen in JavaScript deklariert und verwendet. Aber JavaScript gibt Ihnen noch mehr Werkzeuge an die Hand, um mit Funktionen auf leistungsstarke Weise zu arbeiten.


### Pfeil-Funktionen


Pfeilfunktionen sind eine kürzere Art, Funktionen zu schreiben. Statt des Schlüsselworts `Funktion` wird ein Pfeil (`=>`) verwendet.


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


Wenn die Funktion **nur eine Zeile** hat, können Sie die geschweiften Klammern weglassen und `return`:


```javascript
const greet = (name) => `Hello, ${name}!`
```


Wenn die Funktion **nur einen Parameter** hat, können Sie sogar die Klammern um die Parameter weglassen:


```javascript
const greet = name => `Hello, ${name}!`
```


Pfeilfunktionen sind in modernem JavaScript sehr verbreitet, da sie es erlauben, einfache Funktionen mit deutlich weniger Boilerplate auszudrücken.


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


### Verteilungsparameter (`...`)


Was, wenn Ihre Funktion eine flexible Anzahl von Argumenten benötigt?


Sie können den **Spread-Operator** (`...`) verwenden, um sie in einem Array zu sammeln:


```javascript
function logAll(...items) {
console.log(items)
}

logAll(1, 2, 3) // [1, 2, 3]
logAll("a", "b") // ["a", "b"]
```


Sie können dann eine Schleife verwenden, um jedes Element zu verarbeiten:


```javascript
function logEach(...items) {
for (const item of items) {
console.log(item)
}
}
```


Der Spread-Operator ist nützlich, wenn Sie nicht wissen, wie viele Argumente übergeben werden.


### Funktionen höherer Ordnung


Eine **Funktion höherer Ordnung** ist eine Funktion, die:



- nimmt eine andere Funktion als Eingabe
- und/oder gibt eine Funktion als Ausgabe zurück


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


Dies wird gedruckt:


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


Dies wird gedruckt:


```
Hello!
Hello!
```


Sie können auch Funktionen schreiben, die andere Funktionen **zurückgeben**:


```javascript
function makeGreeter(name) {
return () => console.log(`Hi, ${name}`)
}

const greetAlice = makeGreeter("Alice")
const greetBob = makeGreeter("Bob")

greetAlice() // Hi, Alice
greetBob() // Hi, Bob
```


Die Funktion `makeGreeter` ist eine Funktion, die andere Funktionen aufbaut. Sie empfängt eine Zeichenkette und gibt eine neue Funktion zurück, die diese Zeichenkette in ihrem `console.log`-Aufruf verwendet.


Diese Art von Muster ist sehr leistungsfähig, da sie es Ihnen ermöglicht, "Löcher" in Ihren Funktionen zu hinterlassen, die Sie später mit dem benötigten Verhalten füllen können.


### map()`, `filter()`, `reduce()`


JavaScript bietet Ihnen einige nützliche integrierte Methoden zur Verwendung mit Arrays.


Diese Methoden nehmen Funktionen als Argumente an, sie sind also auch Funktionen höherer Ordnung.


map()" wandelt jedes Element in einem Array in etwas anderes um.


Beispiel:


```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map(x => x * 2)

console.log(doubled) // [2, 4, 6]
```


Jede Zahl wird verdoppelt, und das Ergebnis ist ein neues Feld.


filter()` entfernt Elemente aus dem Array, wenn sie einen Test nicht bestehen.


Beispiel:


```javascript
const numbers = [1, 2, 3, 4, 5]
const numbersGreaterThanTwo = numbers.filter(x => x > 2)

console.log(numbersGreaterThanTwo) // [3, 4, 5]
```


Nur die Array-Einträge, für die die Bedingung "x > 2" "wahr" ist, werden beibehalten.


reduce() wird verwendet, um alle Elemente in einem Array zu einem einzigen Wert zu kombinieren.


Beispiel:


```javascript
const numbers = [1, 2, 3, 4]
const total = numbers.reduce((current, next) => current + next)

console.log(total) // 10
```


`reduce` durchläuft das Array und wendet in diesem Beispiel den `+` Operator zwischen `1` und `2` an, dann zwischen dem resultierenden `3` und `3`, dann zwischen dem resultierenden `6` und `4`, bis es die Summe aller Array-Einträge hat (was 10 ist).


Sie können `reduce()` für viele Dinge verwenden, wie z.B. Summen, Durchschnittswerte oder schrittweises Erzeugen neuer Werte.


Diese Methoden (`map`, `filter`, `reduce`) sind leistungsfähige Werkzeuge, um Daten zu verarbeiten, ohne manuelle Schleifen zu schreiben.


Sie können sie sogar in einer Kette von Vorgängen kombinieren, etwa so:


```javascript
const numbers = [1, 2, 3, 4, 5]

const result = numbers
.map(n => n * 2)        // Double each entry, obtain [2, 4, 6, 8, 10]
.filter(n => n > 3) // Keep only the entries bigger than 3, so you get [4, 6, 8, 10]
.reduce((n1, n2) => n1 + n2) // Adds them: 4 + 6 + 8 + 10 = 28

console.log(result) // 28
```


## Arbeiten mit Objekten

<chapterId>7842aada-f009-5518-b8e3-1104e166a035</chapterId>


In diesem Kapitel lernen wir einige leistungsfähige und etwas fortgeschrittenere Werkzeuge für die Arbeit mit Objekten in JavaScript kennen.


### Private Immobilien


Manchmal möchte man eine Eigenschaft eines Objekts ausblenden, damit sie nicht geändert oder von außerhalb des Objekts aufgerufen werden kann. JavaScript gibt uns eine Möglichkeit, dies zu tun, indem wir `#` vor dem Eigenschaftsnamen verwenden. Dadurch wird eine **private** Eigenschaft erzeugt, auf die nur von innerhalb der Klasse zugegriffen werden kann.


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


Private Eigenschaften sind hilfreich, wenn Sie versehentliche Änderungen verhindern wollen.


### statische" Eigenschaften


Manchmal möchte man, dass eine Eigenschaft zur Klasse selbst gehört und nicht zu jedem Objekt, das man aus dieser Klasse erstellt. Dafür ist `static` gedacht. Eine "statische" Eigenschaft ist in der Klasse enthalten und alle Objekte dieser Klasse verweisen auf sie.


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


Dies ist nützlich für die Speicherung gemeinsamer Daten und Methoden, die für die gesamte Gruppe von Objekten gelten, nicht nur für ein einzelnes.


### `get` und `set`


In JavaScript können Sie mit "get" und "set" Eigenschaften erstellen, die wie normale Variablen aussehen, aber im Hintergrund speziellen Code ausführen.


Eine `get`ter-Methode wird ausgeführt, wenn Sie versuchen, eine Eigenschaft zu *lesen*. Sie wird deklariert, indem man "get" vor eine Methode mit dem Namen der Eigenschaft schreibt.


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


Obwohl `fullName` keine reguläre Eigenschaft ist, können wir sie wie eine solche verwenden, und hinter den Kulissen wird die Funktion `get` ausgeführt, um den vollständigen Namen zu ermitteln.


Eine "Set"-Methode wird ausgeführt, wenn Sie einer Eigenschaft einen Wert *zuweisen*. Damit können Sie kontrollieren, was passiert, wenn jemand versucht, diesen Wert zu ändern. Sie wird deklariert, indem man "set" vor eine Methode mit dem Namen der Eigenschaft schreibt.


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


Wenn wir "user.fullName = "John Smith"" eingeben, wird die Methode "set" ausgeführt und die Werte "firstName" und "lastName" aktualisiert.


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


In diesem Objekt sind "Name" und "Alter" die Schlüssel, und "Alice" und "30" sind ihre Werte.


### Dynamischer Zugang


Manchmal kennen Sie den Namen einer Eigenschaft nicht im Voraus... vielleicht erhalten Sie ihn aus einer Benutzereingabe oder Sie lesen ihn aus einer Variablen. Sie können trotzdem darauf zugreifen, indem Sie die **Klammerschreibweise** verwenden, z. B. `MeinObjekt["Schlüsselname"]`.


```javascript
const user = {
name: "Alice",
age: 30
}

console.log(user["name"]) // Alice
```


Wir haben die Zeichenkette "Name" an das Objekt übergeben, um den entsprechenden Wert zu erhalten.


Wir können einen Schlüssel in einer Variablen speichern und ihn später für den Zugriff auf den entsprechenden Wert verwenden, z. B


```javascript
const user = {
name: "Alice",
age: 30
}

const key = "name"

console.log(user[key]) // Alice
```


### Dynamisch Assignment


Sie können auch Objekteigenschaften mit Variablen als Schlüssel erstellen oder aktualisieren.


```javascript
const settings = {}

const key = "theme"
settings[key] = "dark"

console.log(settings) // { theme: "dark" }
```


Dies ist hilfreich, wenn Sie ein Objekt Schritt für Schritt aufbauen wollen. Zum Beispiel:


```javascript
const user = {}

user["username"] = "bananaFan123"
user["email"] = "banana@fruit.com"

console.log(user)
// { username: "bananaFan123", email: "banana@fruit.com" }
```


Sie können sogar einen dynamischen Schlüssel *bei der Erstellung* des Objekts in eckigen Klammern verwenden:


```javascript
const key = "language"
const config = {
[key]: "JavaScript"
}

console.log(config.language) // JavaScript
```


Dies wird als **berechnete Eigenschaft** bezeichnet. Der Wert innerhalb der eckigen Klammern wird ausgewertet, und das Ergebnis wird als Schlüssel verwendet.


### symbol" Typ


Neben Zeichenketten können Sie in JavaScript auch einen speziellen Typ namens `Symbol` als Objektschlüssel verwenden.


Lassen Sie uns mit einem einfachen Beispiel beginnen:


```javascript
const id = Symbol("userID")

const user = {
name: "Bob",
[id]: 12345
}

console.log(user[id]) // 12345
```


In diesem Beispiel ist "id" ein Symbol. Es ist keine Zeichenkette, aber es funktioniert trotzdem als Schlüssel. Wenn Sie versuchen, `user` auf der Konsole zu protokollieren, werden Sie dies sehen:


```javascript
console.log(user) // { name: 'Bob', [Symbol(userID)]: 12345 }
```


Ein weiterer wichtiger Punkt: Jedes von Ihnen erstellte Symbol ist einzigartig, auch wenn es mit derselben Zeichenfolge erstellt wird.


```javascript
const a = Symbol("label")
const b = Symbol("label")

console.log(a === b) // false
```


Mit Symbolen können Sie Schlüssel definieren, die nicht mit regulären Schlüsseln kollidieren. Nehmen wir an, Sie haben ein Objekt mit der Eigenschaft "Name", aber das Objekt wird in der Zukunft von einem Benutzer in einer für Sie nicht vorhersehbaren Weise angepasst werden können, und dieser Benutzer könnte auch eine Eigenschaft "Name" hinzufügen. Wenn die ursprüngliche Eigenschaft "Name" mit einer Zeichenkette definiert wurde, würde sie durch die neue Eigenschaft überschrieben werden, etwa so:


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


Wie Sie sehen können, bleibt die ursprüngliche Eigenschaft "Name" auf diese Weise erhalten. Dies kann in bestimmten Randfällen nützlich sein.


## Utility-Objekte

<chapterId>516e74c8-2a11-545a-a4d1-c2cabb91a273</chapterId>


JavaScript gibt uns einige nützliche eingebaute Objekte, die uns helfen, Dinge wie Debugging und mathematische Operationen durchzuführen.


### Andere `Konsolen`-Methoden


Sie haben bereits die Datei `console.log` gesehen, die Werte auf dem Bildschirm ausgibt.


Es gibt einige andere nützliche Methoden, die für das `console`-Objekt verfügbar sind und die Ihnen bei der Fehlersuche in Ihren Programmen helfen können.


#### konsole.warnen


Druckt eine Meldung in gelber Farbe (oder mit einem Warnsymbol in einigen Umgebungen):


```javascript
console.warn("This is just a warning.")
```


#### konsole.Fehler


Druckt eine Meldung in Rot, wie bei einem Fehler:


```javascript
console.error("Something went wrong!")
```


#### konsole.Tabelle


Zeigt ein Array oder Objekt als Tabelle an:


```javascript
const users = [
{ name: "Alice", age: 25 },
{ name: "Bob", age: 30 }
]

console.table(users)
```


Dies druckt eine Tabelle wie:


```
┌─────────┬────────┬─────┐
│ (index) │  name  │ age │
├─────────┼────────┼─────┤
│    0    │ 'Alice'│  25 │
│    1    │ 'Bob'  │  30 │
└─────────┴────────┴─────┘
```


Dies kann nützlich sein, um strukturierte Daten zu visualisieren.


#### konsole.Zeit" und "Konsole.ZeitEnde"


Man kann messen, wie lange etwas dauert:


```javascript
console.time("timer")
for (let i = 0; i < 1000000; i++) {}
console.timeEnd("timer")
```


Dies druckt etwas wie:


```
timer: 2.379ms
```


Nützlich für einige einfache Leistungstests.


### Das Objekt `Math`


JavaScript gibt Ihnen ein `Math`-Objekt mit nützlichen Methoden für Berechnungen.


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


#### math.floor()` und Math.ceil()`



- math.floor(n)` rundet **abwärts** auf die nächste Ganzzahl
- math.ceil(n)` rundet **auf** die nächste Ganzzahl


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



- mathe.pow(a, b)` gibt dir `a` hoch `b`
- math.sqrt(n)` liefert die Quadratwurzel aus `n`


```javascript
console.log(Math.pow(2, 3))   // 8
console.log(Math.sqrt(16))    // 4
```


# Fortgeschrittenes JavaScript

<partId>72c30671-ca20-5617-92a5-d5ba7aa38c93</partId>


## Andere Sammlungen

<chapterId>a9a70c6d-a343-5a46-a383-e288bc2700e3</chapterId>


JavaScript bietet uns einige spezielle Auflistungstypen, die über normale Arrays und Objekte hinausgehen. Dazu gehören `Map` und `Set`.


Sie helfen Ihnen bei der Speicherung und Verwaltung von Wertegruppen, funktionieren aber anders als bisher.


Eine "Map" ist eine Sammlung von **Schlüssel-Wert-Paaren**, genau wie ein Objekt. Aber sie hat einige wichtige Unterschiede:



- Die Schlüssel können **beliebige Werte** sein, nicht nur Zeichenketten.
- Die Reihenfolge der Elemente bleibt erhalten.
- Sie verfügt über eingebaute Methoden, die die Arbeit mit ihr erleichtern.


Sie erstellen eine neue Karte wie folgt:


```javascript
const myMap = new Map()
```


Dies erzeugt eine leere Karte. Um ihr Einträge hinzuzufügen, verwenden Sie `myMap.set(key, value)`:


```javascript
myMap.set("name", "Alice")
```


Dies fügt einen Schlüssel `"name"` mit dem Wert `"Alice"` hinzu.


Sie können auch eine Nummer als Schlüssel verwenden:


```javascript
myMap.set(42, "The answer")
```


Und sogar ein Objekt als Schlüssel:


```javascript
const objKey = { id: 1 }
myMap.set(objKey, "Object as key")
```


Das würde mit regulären Objekten, die nur String-Schlüssel zulassen, nicht funktionieren.


Um **einen Wert** zu erhalten, verwenden Sie `myMap.get(key)`:


```javascript
console.log(myMap.get("name"))     // Alice
console.log(myMap.get(42))         // The answer
console.log(myMap.get(objKey))     // Object as key
```


Um **zu prüfen, ob ein Schlüssel existiert**, verwenden Sie `myMap.has(key)`:


```javascript
console.log(myMap.has("name")) // true
```


Um einen Schlüssel zu **entfernen**, verwenden Sie `myMap.delete(key)`:


```javascript
myMap.delete("name")
```


Um **die gesamte Karte** zu löschen, verwenden Sie `myMap.clear()`:


```javascript
myMap.clear()
```


Maps eignen sich hervorragend für die Verwaltung großer Wertesammlungen, da der Zugriff auf Werte in einer großen Map in der Regel wesentlich leistungsfähiger ist als auf ein großes Objekt.


### setzen


Ein "Set" ist eine Sammlung von **nur** Werten (keine Schlüssel), wobei jeder Wert **einzigartig** sein muss. Das bedeutet:



- Man kann denselben Wert nicht zweimal haben
- Die Werte werden in der Reihenfolge gespeichert, in der Sie sie hinzufügen


Sie erstellen einen Satz wie diesen:


```javascript
const mySet = new Set()
```


Um **Werte** hinzuzufügen, verwenden Sie `mySet.add(value)`:


```javascript
mySet.add(1)
mySet.add(2)
mySet.add(2) // duplicate, will be ignored
```


Auch wenn wir versucht haben, `2` zweimal hinzuzufügen, wird die Menge nur eine Kopie behalten.


Um **zu prüfen, ob ein Wert in der Menge** enthalten ist, verwenden Sie `mySet.has(value)`:


```javascript
console.log(mySet.has(2)) // true
console.log(mySet.has(3)) // false
```


Zum **Entfernen eines Wertes** verwenden Sie `mySet.delete(value)`:


```javascript
mySet.delete(2)
```


Um **alles** zu löschen, verwenden Sie `mySet.clear()`:


```javascript
mySet.clear()
```


Ein "Set" ist nützlich, wenn Sie eine Sammlung eindeutiger Werte aufbewahren wollen, ohne manuell nach Duplikaten suchen zu müssen:


```javascript
const numberArray = [1, 2, 2, 3, 4, 4, 4, 5]

const numberSet = new Set(numberArray)

console.log(numberSet) // Set(5) { 1, 2, 3, 4, 5 }
```


Das `Set` vermeidet die Duplikate für Sie.


## Iteratoren

<chapterId>61d24e5e-b7e4-541a-8322-778f61f26a72</chapterId>


Die meisten Dinge in JavaScript, über die man eine Schleife ziehen kann (wie Arrays, Strings, Maps, Sets), sind **iterbar**: Sie können Iteratoren für ihren Inhalt bereitstellen.


Ein **Iterator** ist ein spezielles Objekt in JavaScript, mit dem Sie eine Liste von Elementen **einmal** durchgehen können.


### objekt"-Iteratoren


Anders als Arrays oder Maps sind reguläre Objekte **nicht iterierbar** mit `for...of`. Wenn Sie dies versuchen:


```javascript
const user = {
name: "Alice",
age: 30
}

for (const value of user) {
console.log(value)
}
```


Sie werden eine Fehlermeldung erhalten:


```
TypeError: user is not iterable
```


Das liegt daran, dass einfache Objekte keinen eingebauten Iterator haben. Aber JavaScript gibt Ihnen andere Werkzeuge, um über sie zu schleifen.


#### objekt.Schlüssel()`


Sie können `Object.keys(obj)` verwenden, um ein Array mit den **Schlüsseln** des Objekts zu erhalten, und dann eine Schleife darüber laufen lassen:


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


Dies wird gedruckt:


```
name
age
```


#### objekt.Werte()`


Um eine Schleife über die **Werte** zu ziehen, verwenden Sie `Object.values()`:


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


Dies wird gedruckt:


```
Alice
30
```


#### objekt.Einträge()`


Wenn Sie **sowohl den Schlüssel als auch den Wert** benötigen, verwenden Sie `Object.entries()`:


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


Dies wird gedruckt:


```
name is Alice
age is 30
```


Auch wenn Objekte nicht direkt iterierbar sind, geben diese Methoden vollen Zugriff auf ihren Inhalt in einer Art und Weise, die gut mit "for...of" funktioniert.


Aber wie funktionieren Iteratoren?


### symbol.Iterator


Das Geheimnis hinter allen Iterablen ist ein spezielles **Symbol** namens `Symbol.iterator`.


Dieses Symbol ist ein eingebauter Schlüssel, der JavaScript mitteilt: "Dieses Objekt kann iteriert werden"


Wenn Sie `myIterable[Symbol.iterator]()` aufrufen, erhalten Sie von JavaScript ein **Iterator-Objekt** mit einer Methode `.next()` zurück.


Schauen wir mal, wie das aussieht:


```javascript
const colors = ["red", "green", "blue"]

const iterator = colors[Symbol.iterator]()

console.log(iterator.next()) // { value: 'red', done: false }
```


Jeder Aufruf von `.next()` gibt Ihnen den nächsten Wert. Wenn er fertig ist, kehrt er zurück:


```javascript
{ value: undefined, done: true }
```


### `Nächste()`


Die Methode `.next()` wird verwendet, um das nächste Element der Sequenz zu erhalten.


Jedes Mal, wenn Sie `.next()` aufrufen, erhalten Sie ein Objekt mit zwei Schlüsseln:



- wert": das aktuelle Element
- done": ein boolescher Wert, der angibt, ob die Iteration beendet ist


Lassen Sie uns ein vollständiges Beispiel machen:


```javascript
const names = ["Lina", "Tom", "Eva"]      // declare an array
const iterator = names[Symbol.iterator]() // use the Symbol.iterator function to get an iterator for this array

let result = iterator.next()              // get the first element of the array

while (!result.done) {                    // repeat this loop until you reach the last element of the array, which is marked with { done: true }
console.log(result.value)               // print the value of each element
result = iterator.next()                // get the next element of the array
}
```


Dies wird gedruckt:


```
Lina
Tom
Eva
```


So funktioniert eine `for...of`-Schleife unter der Haube: Sie verwendet dieses Muster mit `.next()`.


Das gleiche Ergebnis erhalten Sie mit


```javascript
const names = ["Lina", "Tom", "Eva"]

for (const result of names) {
console.log(result)
}
```


### Eine Klasse iterierbar machen


Sie können auch Ihre eigene **iterable-Klasse** definieren, indem Sie eine `[Symbol.iterator]()` Methode hinzufügen.


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


Dies wird gedruckt:


```
1
2
3
4
5
```


Es geht um Folgendes:



- Wir haben eine Klasse `Range` definiert
- Innerhalb der Klasse haben wir `[Symbol.iterator]()` implementiert, damit JavaScript weiß, wie man es durchläuft
- Die Methode `next()` gibt jede Zahl einzeln zurück
- Wenn wir das "Ende" erreichen, gibt es "{ done: true }" zurück


Jetzt funktioniert unsere Klasse "Range" wie ein Array, und wir können sie in jeder Schleife verwenden, die eine Iterable erwartet.


### Generatorfunktionen und "Ertrag


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


Sie können auch mit `for...of` eine Schleife über einen Generator ziehen:


```javascript
for (const num of numberGenerator()) {
console.log(num)
}
```


Dies wird gedruckt:


```
1
2
3
```


## Gleichzeitigkeit mit Rückrufen

<chapterId>f3fc76ca-b3ef-54eb-a06e-501007002054</chapterId>


Bis jetzt war unser Code **synchron**: Er läuft eine Zeile nach der anderen ab, der Reihe nach. Aber einige Dinge in der realen Welt brauchen Zeit, und wir wollen nicht, dass das gesamte Programm während des Wartens pausiert.


In diesem Kapitel werden wir ein neues Konzept einführen: **Gleichzeitigkeit**. Es erlaubt uns, die Reihenfolge, in der Dinge erledigt werden, zu manipulieren. Das ist nützlich, wenn wir mit Dingen wie Timern, Benutzereingaben oder dem Lesen von Dateien von der Festplatte umgehen. JavaScript bietet verschiedene Werkzeuge für die Gleichzeitigkeit.


### zeitlimit setzen


Mit der Funktion `setTimeout` können Sie eine Funktion **später** ausführen, nachdem eine gewisse Zeit vergangen ist.


Beispiel:


```javascript
console.log("Start")

setTimeout(
() => console.log("This runs after 2 seconds"),
2000
)

console.log("End")
```


Dies wird gedruckt:


```
Start
End
This runs after 2 seconds
```


Obwohl `setTimeout` in der Mitte des Codes erscheint, blockiert es nicht den Rest. Stattdessen wird die Funktion für eine **spätere** Ausführung eingeplant und sofort fortgesetzt.


2000" bedeutet 2000 Millisekunden (das sind 2 Sekunden).

Hier ist eine ausführlichere und anfängerfreundliche Neufassung der Abschnitte **Rückrufe** und **Versprechen**, die durchgängig Datenmanipulation und klare Anmerkungen verwendet:


### Rückrufe


Ein **Callback** ist einfach eine Funktion, die wir einer anderen Funktion übergeben, damit sie später **aufgerufen** werden kann.


Schauen wir uns ein reales Beispiel mit Zahlen an. Stellen Sie sich vor, wir haben eine Liste von Zahlen und wollen jede einzelne verdoppeln und dann eine Funktion (den Rückruf) auf das resultierende "verdoppelte" Array anwenden, aber wir wollen dies mit einer kleinen Verzögerung tun, als ob wir auf etwas Langsames warten würden (wie das Laden von Daten aus dem Internet).


Hier ist eine Funktion, die dies mit einem **Rückruf** erledigt:


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


**Was passiert hier?*


1. Wir übergeben `input` als Liste von Zahlen, die wir verdoppeln wollen.

2. Wir übergeben auch eine **Callback-Funktion**, die dem Programm sagt, was es *nach* der Verdopplung tun soll.

3. Innerhalb von `doubleNumbers` simulieren wir eine Verzögerung mit `setTimeout`, dann führen wir die Verdopplung durch.

4. Sobald das erledigt ist, rufen wir den Callback auf dem resultierenden "verdoppelten" Array auf.


Diese Technik funktioniert, aber stellen Sie sich vor, Sie wollen danach **mehr Schritte** machen, z. B. kleine Zahlen herausfiltern und sie dann addieren. Dann müssten Sie mehr Rückrufe wie diesen **einnesten**:


```javascript
doubleNumbers(input, function(doubled) {
filterBigNumbers(doubled, function(filtered) {
sumNumbers(filtered, function(total) {
console.log("Final result:", total)
})
})
})
```


Das ist Hard zu lesen und unübersichtlich. Dieser Stil wird **Callback-Hölle** genannt, und es ist genau das, was `Promise` geschaffen wurde, um das zu beheben.


## Gleichzeitigkeit mit Versprechen

<chapterId>30fddaca-729f-5c8d-bf86-8dfc7b3c9800</chapterId>


Ein "Promise" ist ein eingebautes JavaScript-Objekt, das einen Wert darstellt, der **in der Zukunft bereit sein wird**.


Wir können ein Versprechen wie folgt erstellen:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve("It worked!") // This means everything went OK
})
```


Der Teil `new Promise()` erstellt das Versprechen.


Darin geben wir ihm eine Funktion mit zwei Parametern:



- `resolve`, ist eine Funktion, die wir aufrufen, wenn alles erfolgreich war
- ablehnen" ist eine Funktion, die wir aufrufen, wenn etwas schief geht


Im obigen Beispiel lösen wir es einfach sofort mit der Meldung "Es hat geklappt" auf.


### `.then()`


Um etwas zu tun, **nachdem** das Versprechen erfüllt ist, verwenden wir `.then()`:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve(100) // This means everything went OK
})

promise.then(result => {
console.log("The result is:", result)
})
```


Dies wird gedruckt:


```
The result is: 100
```


Der Wert, den wir an `resolve()` übergeben haben, wird als `Result` an die Funktion in `.then()` gesendet.


Lassen Sie uns eine Aufgabe simulieren, die 2 Sekunden dauert, indem wir `setTimeout` verwenden:


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


Dieser wartet 2 Sekunden und druckt dann:


```
Done waiting!
```


### ablehnen()`


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


Dies druckt nur


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


Dies wird gedruckt:


```
Success: Positive number
```


Und wenn wir es mit einer anderen Nummer versuchen:


```javascript
checkNumber(-1)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Er druckt:


```
Failure: Not a positive number
```


### Verkettung von Operationen mit `Promise`



Wir können unser früheres Beispiel mit `Promise` umschreiben, und es wird viel sauberer aussehen.


Beginnen wir damit, eine neue Version unserer Verdopplungsfunktion zu schreiben, aber diesmal gibt sie ein **Versprechen** zurück:


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


Jetzt können wir mit `.then()` JavaScript mitteilen, was mit dem Ergebnis geschehen soll:


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


Dies wird gedruckt:


```
Doubled numbers: [ 2, 4, 6 ]
```


Bislang funktioniert dies genauso wie die Callback-Version, aber der Code ist jetzt einfacher zu erweitern und zu lesen.


Nehmen wir an, wir wollen weitere Schritte hinzufügen:


1. Erstens: Verdoppeln Sie alle Zahlen

2. Dann werden Zahlen kleiner als 4 entfernt

3. Zum Schluss fügen Sie sie alle zusammen


Wir können für jeden Schritt eine Funktion schreiben, die alle Versprechen verwendet:


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


Dies wird gedruckt:


```
Final result after all steps: 10
```


Schauen wir uns an, was das bedeutet:


1. `doubleNumbers` verdoppelt das Array: `[2, 4, 6]`

2. filterBigNumbers`entfernt alles ≤ 3: `[4, 6]`

3. `sumNumbers` addiert die verbleibenden Zahlen: `4 + 6 = 10`

4. Schließlich wird das Ergebnis ausgedruckt.


Jedes `.then()` wartet, bis der Schritt vor ihm beendet ist. So können wir eine **Aktionskette** ohne Verschachtelung aufbauen. Das macht den Code lesbarer und einfacher zu debuggen.


## Gleichzeitigkeit mit `async`/`await`

<chapterId>6e93d29f-c8bf-5fd1-a9c9-4e794ee6cbd0</chapterId>


Wir haben gesehen, wie `Promise`-Ketten uns helfen, die Rückrufhölle zu vermeiden, aber sie können immer noch ein wenig Hard zu lesen, wenn viele Schritte involviert sind.


An dieser Stelle kommen `async` und `await` ins Spiel. Sie ermöglichen es uns, asynchronen Code zu schreiben, **der wie synchroner Code aussieht**, was ihn leichter verständlich macht.


### Was ist "async"?


Wenn Sie das Schlüsselwort `async` vor eine Funktion schreiben, verpackt JavaScript den Rückgabewert der Funktion automatisch in ein Promise.


Schauen wir uns ein einfaches Beispiel an:


```javascript
async function greet() {
return "hello"
}
```


Wenn Sie diese Funktion aufrufen:


```javascript
const result = greet()
console.log(result)
```


Das werden Sie sehen:


```
Promise { 'hello' }
```


Auch wenn Sie nur eine Zeichenkette zurückgegeben haben, verwandelt JavaScript sie in ein Versprechen für Sie. Sie können den tatsächlichen Wert mit `.then()` wie folgt abrufen:


```javascript
greet().then( result => console.log(result) ) // prints "hello"
```


Oder Sie können `await` verwenden...


### Was bedeutet "erwarten"?


Das Schlüsselwort `await` sagt JavaScript: "warte, bis dieses Versprechen erfüllt ist, und gib mir dann das Ergebnis."


Aber Sie können "await" nur **innerhalb einer asynchronen Funktion** verwenden.


Lassen Sie uns das Beispiel unter Verwendung von "await" neu schreiben:


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


Lassen Sie uns jetzt etwas Nützlicheres tun.


### Simulation einer Verzögerung mit `await`


Wir werden eine einfache `wait`-Funktion erstellen, die eine Anzahl von Millisekunden als Argument nimmt und nach dieser Anzahl von Millisekunden einfach auflöst, ohne etwas anderes zu tun:


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


Dies wird gedruckt:


```
waiting 2 seconds...
done waiting
```


Sie können sich `await` als "Pause hier, bis das Versprechen erfüllt ist, dann weiter" vorstellen


Dies ermöglicht es Ihnen, Code in einer **von oben nach unten** Weise zu schreiben, der sich asynchron verhält, ohne `.then()` Aufrufe zu verketten.


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


Schreiben wir nun eine "async"-Funktion, um sie zu kombinieren:


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


Dies wird gedruckt:


```
Final result: 10
```


Dies ist viel einfacher zu lesen als die Verkettung von `.then()` oder die Verschachtelung von Rückrufen.


Es sieht aus wie ein normales Schritt-für-Schritt-Programm, verhält sich aber dennoch asynchron.


## Asynchrone Iteratoren

<chapterId>438b037d-9931-56d7-9052-7b4470f3c75b</chapterId>


Sie haben bereits über **Zitatoren** gelernt und wie wir `for...of` verwenden können, um über Arrays und andere iterierbare Dinge zu schleifen.


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


Wir können nun "for await...of" verwenden, um die Werte zu verbrauchen:


```javascript
async function run() {
for await (const n of generateNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


Dies wird gedruckt:


```
Got number: 1
Got number: 2
Got number: 3
Done!
```


Was ist also der Unterschied zu einem normalen Generator?


Der Unterschied ist, dass wir jetzt `await` innerhalb des Generators verwenden können.


Lassen Sie uns wieder einen Verzögerungshelfer machen:


```javascript
function wait(ms) {
return new Promise(resolve => setTimeout(resolve, ms))
}
```


Lassen Sie uns nun **langsam** Zahlen liefern:


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


Probieren Sie es aus:


```javascript
async function run() {
for await (const n of generateSlowNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


### Warum asynchrone Iteratoren verwenden?


Async-Iteratoren sind nützlich, wenn:



- Die Werte kommen nicht alle auf einmal an.
- Sie wollen sie nacheinander bearbeiten, **wenn sie kommen**.
- Sie arbeiten mit Promises und möchten eine saubere Schleife erstellen.


Wenn Sie beispielsweise eine Nachricht nach der anderen von einem Chatserver laden oder eine große Datei in Stücken herunterladen möchten, können Sie mit asynchronen Iteratoren eine "for"-Schleife schreiben, die mit verzögerten Daten arbeitet.


### symbol.asyncIterator


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


Wir können nun "for await...of" genau wie zuvor verwenden:


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


So können Sie Objekte erstellen, die asynchron durchlaufen werden können


## Assignment-Syntaxzucker

<chapterId>8b1ba7d8-ecfd-5470-b86e-73cb84ccc8b7</chapterId>


"Syntaxzucker" bedeutet, etwas kürzer oder einfacher zu schreiben, ohne seine Funktion zu verändern. Es ist nur eine schönere Art, das Gleiche zu sagen.


JavaScript verfügt über einige eingebaute Syntaxzucker, mit denen wir sauberere und kürzere Deklarationen schreiben können. In diesem Kapitel sehen wir uns an, wie man Werte basierend auf einer Bedingung zuweist, Variablen mit Mathematik aktualisiert, Werte aus Arrays oder Objekten zieht und sie mit einer einfacheren Syntax kopiert oder kombiniert.


### Der ternäre Operator


In JavaScript können Sie einen Wert auf der Grundlage einer Bedingung zuweisen, indem Sie den **Nebenoperator** verwenden, was eine Kurzform von "if...else" ist.


Anstatt zu tun:


```javascript
let message

if (isMorning) {
message = "Good morning"
} else {
message = "Hello"
}
```


Sie können schreiben:


```javascript
const message = isMorning ? "Good morning" : "Hello"
```


Dies bedeutet:



- Wenn "isMorning" wahr ist, verwenden Sie "Guten Morgen"
- Andernfalls verwenden Sie `"Hallo"`


Die allgemeine Form ist:


```javascript
condition ? valueIfTrue : valueIfFalse
```


Sie können ihn auch in anderen Ausdrücken verwenden:


```javascript
console.log(isSunny ? "Go outside" : "Stay in")
```


Achten Sie nur darauf, dass Sie es für **einfache** Entscheidungen verwenden. Wenn die Logik komplex ist, bleiben Sie bei "if...else".


### Alternative Assignment-Betreiber


JavaScript verfügt über **Kurzbefehlsoperatoren** für die Ausführung von Zuweisungen in Kombination mit Operationen.


Betrachten wir einmal den normalen Weg:


```javascript
let counter = 1
counter = counter + 1
```


Dies kann abgekürzt werden zu:


```javascript
let counter = 1
counter += 1 // same as counter = counter + 1
```


Hier sind die häufigsten:


| Operator | Meaning             |
| -------- | ------------------- |
| `+=`     | add and assign      |
| `-=`     | subtract and assign |
| `*=`     | multiply and assign |
| `/=`     | divide and assign   |

Beispiele:


```javascript
let score = 10
score += 5  // now score is 15
score *= 2  // now score is 30
score -= 10 // now score is 20
```


Diese sind nützlich, wenn Sie eine Variable mit ihrem eigenen Wert aktualisieren wollen.


### Umstrukturierung


*mit der *Destrukturierung** können Sie auf einfache Weise Werte aus Arrays oder Objekten entnehmen und in Variablen speichern.


#### Arrays


Angenommen, Sie haben:


```javascript
const colors = ["red", "green", "blue"]
```


Anstatt zu tun:


```javascript
const first = colors[0]
const second = colors[1]
```


Das können Sie tun:


```javascript
const [first, second] = colors
```


Dieser weist zu:



- zuerst" auf "rot
- zweiter" zu "Green


Sie können auch Werte weglassen:


```javascript
const [,, third] = colors
console.log(third) // blue
```


#### Objekte


Sie können auch Werte aus Objekten extrahieren:


```javascript
const user = { name: "Alice", age: 30 }

const { name, age } = user
console.log(name) // Alice
console.log(age)  // 30
```


Wenn die Eigenschaft einen anderen Namen hat als die gewünschte Variable, können Sie sie umbenennen:


```javascript
const { name: username } = user
console.log(username) // Alice
```


Die Destrukturierung macht Ihren Code bei der Arbeit mit Objekten und Arrays sauberer.


### Spread-Syntax


Die **spread-Syntax** verwendet `...` zum Entpacken oder Kopieren von Werten.


#### Arrays


Sie können Arrays kopieren oder zusammenführen:


```javascript
const a = [1, 2]
const b = [3, 4]

const both = [...a, ...b]
console.log(both) // [1, 2, 3, 4]
```


Sie können auch ein Array klonen:


```javascript
const original = [10, 20, 30]
const clone = [...original]
```


#### Objekte


Sie können dasselbe mit Objekten tun:


```javascript
const a = { x: 1 }
const b = { y: 2 }

const merged = { ...a, ...b }
console.log(merged) // { x: 1, y: 2 }
```


Sie können die Werte auch überschreiben:


```javascript
const user = { name: "Alice", age: 30 }
const updated = { ...user, age: 31 }

console.log(updated) // { name: "Alice", age: 31 }
```


Dies ist sehr nützlich, wenn Sie Objekte aktualisieren wollen, ohne das Original zu verändern.


# NodeJS

<partId>42fe4d49-dace-5135-bb9e-b9d75034fb2a</partId>


## Wie sind wir zu Node gekommen?

<chapterId>0da1d60c-06c9-54e6-a181-ae7dabf6e3b8</chapterId>


In diesem Kapitel erfahren wir ein wenig über den historischen Kontext von JavaScript und NodeJS.


Der historische Kontext ist bei Software sehr wichtig, weil wir oft Werkzeuge verwenden, die von anderen Menschen entwickelt wurden, und wir daher von Entscheidungen beeinflusst werden, die diese Menschen in der Vergangenheit getroffen haben.


Wenn wir die Gründe für diese Entscheidungen verstehen und wissen, wie die von uns verwendeten Instrumente zustande gekommen sind, werden wir weniger verwirrt sein über das, was wir tun.


### Die Ursprünge von JavaScript


JavaScript war ursprünglich eine einfache Sprache, um Webseiten interaktiv zu gestalten.


In den 1990er Jahren fügten Webbrowser wie Netscape Navigator JavaScript hinzu, so dass Entwickler Code schreiben konnten, der direkt im Browser ausgeführt wurde.


Die ursprüngliche Idee war, Java als Kernsprache für die Erstellung von Websites (mit den so genannten "Java-Applets") zu verwenden und JavaScript nur für kleinere Dinge.


Das Kerndesign wurde von Brendan Eich, der damals bei Netscape angestellt war, in weniger als 2 Wochen erstellt.


Aber die meisten Leute zogen die Verwendung von JavaScript der Verwendung von Java vor, und auch Java-Applets hatten damals einige Sicherheitsprobleme, so dass Java schließlich als Option gestrichen wurde und JavaScript zum De-facto-Standard für die Webentwicklung wurde.


### Der V8-Motor


JavaScript ist eine interpretierte Sprache, im Gegensatz zu kompilierten Sprachen wie C.


Der in einer kompilierten Sprache geschriebene Code wird in eine Binärdatei umgewandelt, und die Binärdatei wird direkt an die CPU des Computers weitergeleitet.


![](assets/en/6.webp)


Interpretensprachen hingegen sind in der Regel benutzerfreundlicher und orientieren sich eher an der menschlichen Denkweise ("high level") als an der Arbeitsweise von Maschinen ("low level"); daher verfügen sie in der Regel über eine virtuelle Maschine, die ihren Code ausführt.


Eine virtuelle Maschine ist ein spezielles Programm, das zwischen dem von Ihnen geschriebenen Code und der CPU sitzt und Ihren Code ausführt (weil die CPU ihn nicht verstehen kann).


Auf diese Weise können Sie programmieren, ohne zu viel über die zugrunde liegende Maschine zu wissen, aber es hat auch einen Preis in Bezug auf die Leistung, denn auf dem Computer läuft nicht nur Ihr Programm, sondern ein Programm (die virtuelle Maschine), auf dem Ihr Programm läuft.


Da die Webanwendungen immer komplexer wurden, bestand der Bedarf, die Leistung von JavaScript zu verbessern. Die V8-Engine ist der Interpreter, der JavaScript in Google Chrome antreibt. Er wurde bei Google entwickelt und 2008 veröffentlicht.


Während die älteren JavaScript-Engines meist traditionelle virtuelle Maschinen waren, ist die V8-Engine ein JIT-Compiler (Just-in-Time).


Der JavaScript-Code wird in die V8-Engine eingespeist, und die Engine versucht, Teile davon als native Binärdateien im laufenden Betrieb zu kompilieren. Dies ermöglicht es Ihnen, die Erfahrung einer Hochsprache zu haben, mit einer Leistung, die ein wenig näher an Low-Level-Sprachen ist. Dies hat JavaScript zur schnellsten Hochsprache der Welt gemacht, eine Art "das Beste aus beiden Welten".


### Die NodeJS-Laufzeitumgebung


Obwohl JavaScript einfach zu benutzen und recht schnell auszuführen ist, hatte es nach der Veröffentlichung von V8 eine große Einschränkung: Es konnte nur innerhalb eines Browsers ausgeführt werden.


Warum ist das ein Problem?


Da Browser Code ausführen, der aus Millionen verschiedener Quellen im Internet stammt, können sie leicht zu Malware werden, weshalb sie vom Rest des Betriebssystems getrennt sind.


![](assets/en/7.webp)


JavaScript konnte nicht auf das Dateisystem und andere lokale Ressourcen auf Ihrem Computer zugreifen (zumindest nicht so einfach wie andere Sprachen), so dass dies eine erhebliche Einschränkung für die Art der Anwendungen darstellte, die Sie damit erstellen konnten.


Im Jahr 2009 veröffentlichte Ryan Dahl NodeJS, eine Laufzeitumgebung, mit der Sie die V8-Engine außerhalb des Browsers direkt auf dem nativen Betriebssystem Ihres Computers verwenden können. Außerdem bietet sie viele Funktionen, die für das Schreiben von serverseitigen und Befehlszeilenprogrammen nützlich sind. So können Sie mit NodeJS beispielsweise einen Webserver erstellen, Dateien lesen und schreiben oder Tools zur Automatisierung von Aufgaben erstellen.


![](assets/en/8.webp)


In diesem Kurs haben wir uns bisher mit den JavaScript-Funktionen beschäftigt, die sowohl im Browser als auch in NodeJS vorhanden sind. Mit diesen Funktionen konnten wir Daten definieren und sie auf abstrakte Weise manipulieren. In den nächsten Lektionen werden wir uns mit den NodeJS-spezifischen Funktionen befassen, die uns die Interaktion mit dem Betriebssystem ermöglichen.


## Argumente für die Befehlszeile

<chapterId>960d20f3-c424-5d51-a041-ef17d2e94b6d</chapterId>


NodeJS ermöglicht es uns unter anderem, CLIs (Command Line Interfaces) zu erstellen.


Dafür brauchen wir eine Möglichkeit, Kommandozeilenargumente zu erhalten, was in Node mit dem eingebauten `process`-Objekt geschieht.


### prozess


NodeJS bietet ein spezielles Objekt namens `process`, das das aktuell laufende Programm darstellt.


Sie können damit die Umgebung und das aktuelle Arbeitsverzeichnis überprüfen und bei Bedarf sogar das Programm beenden.


Zum Beispiel:


```javascript
console.log(process.platform)
```


Dies gibt die Plattform des Betriebssystems aus, z. B. `win32`, `linux` oder `darwin` (Mac).


### prozess.argv


Wenn Sie ein NodeJS-Programm vom Terminal aus starten, können Sie zusätzliche Wörter (Argumente) nach dem Skriptnamen übergeben. Diese werden in `process.argv` gespeichert.


Wenn Sie zum Beispiel diesen Befehl ausführen:


```
node my_script.js alpha beta
```


Sie können die Argumente wie folgt ausdrucken:


```javascript
console.log(process.argv)
```


Die Ausgabe könnte wie folgt aussehen:


```
[ '/path/to/node', '/path/to/my_script.js', 'alpha', 'beta' ]
```


Die ersten beiden Elemente sind immer der Knotenpfad und Ihr Skriptpfad. Alle zusätzlichen Wörter, die Sie an das Skript übergeben haben, folgen danach.


Das `process.argv`-Array kann wie jedes andere Array mit der `.slice()`-Methode zerlegt werden. Um also nur die Argumente zu erhalten, die übergeben wurden, können Sie


```javascript
const args = process.argv.slice(2)

console.log(args)
```


Der Zugriff auf die Argumente, die der Benutzer übergibt, ist für die Entwicklung von Befehlszeilenanwendungen unerlässlich.


## Module

<chapterId>4e1651a5-65fd-50bc-b22a-40313d5659ca</chapterId>


JavaScript-Laufzeitsysteme wie NodeJS behandeln normalerweise jede JavaScript-Datei als separates Modul.


Stellen Sie sich ein Modul wie eine Box vor. Die Box hat ihren eigenen privaten Bereich, so dass die darin deklarierten Variablen und Funktionen den Code in anderen Boxen nicht beeinträchtigen. Im Grunde hat jedes Modul seinen eigenen Bereich.


Ein Modul kann einen Teil seines Inhalts exportieren, um ihn anderen Modulen zur Verfügung zu stellen, und es kann den Inhalt importieren, den andere Module exportiert haben. Mit JavaScript können Sie Inhalte zwischen Modulen exportieren und importieren, um verschiedene Dateien zu verbinden.


Ein JavaScript-Programm besteht oft aus mehreren Modulen, die miteinander verbunden sind.


Warum Module verwenden? Indem Sie Ihren Code in Module aufteilen, können Sie Ihr Programm in kleinere, übersichtlichere und wiederverwendbare Teile gliedern. Jedes Modul kann sich auf eine bestimmte Art von Aufgabe konzentrieren, z. B. auf mathematische Berechnungen, die Arbeit mit Dateien oder die Formatierung von Text.


### CommonJS-Module


In NodeJS wird das gängigste System zur Verwaltung von Modulen **CommonJS** genannt.


In diesem System können Sie den Code eines Moduls mit `module.exports` freigeben (exportieren) und ihn mit `require()` in eine andere Datei laden (importieren).


Um etwas außerhalb eines Moduls verfügbar zu machen, weist man es `module.exports` zu:


```javascript
const greeting = "Hello!"

module.exports = greeting
```


In diesem Fall exportiert das Modul die Zeichenkette "Hello!".


Um den exportierten Code aus einer anderen Datei zu verwenden, verwenden Sie die Funktion `require()` mit dem Pfad zu dieser Datei:


```javascript
const greeting = require("./greeting.js")

console.log(greeting)
```


Dies wird gedruckt:


```
Hello!
```


Sie können mehrere Dinge exportieren, indem Sie sie in einem anonymen Objekt zusammenfassen, z. B


```javascript
const greeting1 = "hello"

const greeting2 = "hi"

module.exports = {
greeting1, greeting2
}
```


CommonJS war das Modulsystem, das zunächst von NodeJS übernommen wurde. Später wurden auch ES-Module hinzugefügt.


### ES-Module


NodeJS unterstützt auch eine andere Art von Modulen, die **ES-Module**, die in der Webentwicklung sehr beliebt sind. Sie verwenden die Schlüsselwörter "exportieren" und "importieren".


ES-Module wurden für den Browser entwickelt und erst später zu Node hinzugefügt. Wenn Sie sie verwenden möchten, müssen Sie möglicherweise `.mjs` als Dateierweiterung anstelle von `.js` verwenden, je nachdem, welche Node-Version Sie verwenden.


In einer Datei mit dem Namen `greeting.mjs` schreiben wir


```javascript
export const greeting = "Hello!"
```

Wie Sie sehen können, exportieren wir die Konstante direkt dorthin, wo sie definiert wird


In einer anderen Datei namens "index.mjs" importieren wir sie:


```javascript
import { greeting } from "./greeting.mjs"

console.log(greeting)
```


Sie können verschiedene Deklarationen in verschiedene Teile der Datei exportieren, z. B


```javascript
export const num = 10

export function double (x) {
return x*2
}
```


### Die NodeJS-Standardbibliothek


NodeJS enthält auch viele integrierte Module. Dabei handelt es sich um vorgefertigte Module, die von NodeJS bereitgestellt werden und bei allgemeinen Aufgaben wie dem Lesen von Dateien, der Arbeit mit dem Betriebssystem oder der Verbindung mit dem Netzwerk helfen.


Das Modul `os` zum Beispiel gibt Ihnen Informationen über Ihr Betriebssystem:


```javascript
const os = require("os")

console.log(os.platform())
```


Sie müssen diese eingebauten Module nicht installieren, sie werden mit NodeJS geliefert. Sie bilden die "Standardbibliothek" der Laufzeitumgebung und werden von den meisten Node-Anwendungen verwendet, um Dinge wie das Lesen von Dateien oder die Kommunikation über das Internet durchzuführen.


In den nächsten Kapiteln werden Sie einige nützliche Beispiele für ihre Verwendung finden.


## Das Modul `fs`

<chapterId>911e953a-35ae-5ee7-bd74-372501c32e81</chapterId>


Das `fs`-Modul (kurz für **Dateisystem**) ist Teil der NodeJS-Standardbibliothek. Es erlaubt Ihnen, mit Dateien und Verzeichnissen auf Ihrem Computer zu arbeiten: Sie können Dateien lesen, schreiben, löschen, umbenennen und mehr.


Um sie zu verwenden, müssen Sie sie zunächst am Anfang Ihrer Datei importieren:


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


Wenn sich eine Datei mit dem Namen `example.txt` im gleichen Verzeichnis wie Ihr Skript befindet, wird ihr Inhalt ausgegeben.


Sie können auch synchron in eine Datei schreiben:


```javascript
const fs = require("fs")

fs.writeFileSync("output.txt", "Hello from Node!")

console.log("File written!")
```


Dadurch wird eine Datei mit dem Namen `output.txt` mit dem Text erstellt (oder überschrieben).


Hier sind einige gängige Operationen, die Sie mit dieser API durchführen können:


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


Die Sync-API ist einfach und gut für kleine Skripte geeignet, aber da sie das Programm blockiert, bis es fertig ist, kann sie die Arbeit verlangsamen, wenn Sie mit großen Dateien oder einem Server arbeiten.


### Asynchroner Rückruf API


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



- fs.readFile` beginnt mit dem Lesen von `example.txt`.
- NodeJS wartet nicht, sondern führt anderen Code aus, den Sie möglicherweise geschrieben haben.
- Wenn die Datei fertig gelesen ist, wird der Rückruf ausgeführt:



  - Wenn ein Fehler aufgetreten ist, enthält `err` den Fehler.
  - Andernfalls enthält `data` den Inhalt.


So schreiben Sie in eine Datei:


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


Einige Beispiele für Dinge, die Sie mit dieser API tun können:


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


Die Callback-API ist besser für Server und große Aufgaben geeignet, da sie das Programm nicht blockiert, aber verschachtelte Callbacks können unübersichtlich werden, wenn man viele Operationen verkettet. Aus diesem Grund wurde eine auf Versprechen basierende asynchrone API hinzugefügt.


### Asynchrones Versprechen API


Die Promise-basierte API ist modern und funktioniert hervorragend mit `.then()` und `async/await`. Sie ist als `fs.promises` verfügbar.


Sie müssen die Eigenschaft `Promises` importieren:


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


Oder noch besser, mit "async/await":


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


Wenn Sie Code schreiben, müssen Sie oft Code verwenden, der von anderen geschrieben wurde, z. B. Bibliotheken, die Ihnen bei der Arbeit mit Daten, Farben, Servern oder fast allem anderen helfen.


Anstatt Dateien manuell herunterzuladen und zu kopieren, können Sie einen **Paketmanager** verwenden.


Ein Paketmanager ist ein Werkzeug, das:



- download-Pakete
- behält den Überblick, welche Pakete Ihr Projekt benötigt
- stellt sicher, dass jeder in Ihrem Team über die gleichen Versionen der Pakete verfügt


### Was ist NPM?


In der NodeJS-Welt ist der beliebteste Paketmanager **NPM**, was für *Node Package Manager* steht.


Sie erhalten NPM automatisch, wenn Sie NodeJS installieren.


Sie können überprüfen, ob Sie NPM haben, indem Sie dies in Ihrem Terminal ausführen:


```
npm -v
```


Dies gibt die Version von NPM aus, die Sie haben, z. B.:


```
10.2.1
```


### Ein Paket erstellen


In NodeJS ist ein **Paket** einfach ein Verzeichnis mit einer `package.json`-Datei darin.


Lassen Sie uns Schritt für Schritt eine erstellen.


1. Legen Sie einen neuen Ordner für Ihr Projekt an:


```
mkdir my_project
cd my_project
```


2. Führen Sie diesen Befehl aus:


```
npm init
```


Dadurch wird ein interaktives Setup gestartet, das Ihnen Fragen wie den Namen Ihres Projekts, die Version, die Beschreibung usw. stellt.


Wenn Sie nicht alles beantworten und nur die Standardeinstellungen akzeptieren möchten, können Sie dies tun:


```
npm init -y
```


Nachdem Sie es ausgeführt haben, sehen Sie in Ihrem Ordner eine neue Datei mit dem Namen


```
package.json
```


### `Paket.json`


Die Datei `package.json` ist einfach eine JSON-Datei, die Metadaten über Ihr Projekt speichert.


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



- name": der Name Ihres Pakets
- version": die aktuelle Version
- main": die Einstiegsdatei (wie "index.js")
- skripte": Befehle, die Sie ausführen können (wie "npm start")
- abhängigkeiten": listet alle Pakete auf, von denen Ihr Projekt abhängt


### Installieren eines Pakets


Nehmen wir an, Sie wollen ein bestimmtes Paket namens `picocolors` verwenden, um Farben zu Ihrer Terminalausgabe hinzuzufügen.


Sie können es installieren, indem Sie es ausführen:


```
npm install picocolors
```


Sie können es nun in Ihrem Projekt verwenden. Erstellen Sie eine Datei "index.js" mit


```javascript
const pico = require('picocolors')

console.log(
pico.green("This text is green!")
)
```


und versuchen Sie, es auszuführen. Das Terminal sollte eine farbige Version des Textes ausgeben.


Was hat der NPM getan?



- Es lud das Paket herunter und speicherte es in einem Unterordner namens `node_modules/`
- es hat einen Eintrag unter `dependencies` in Ihrer `package.json` hinzugefügt
- er hat die Datei "package-lock.json" aktualisiert


Was ist `package-lock.json`?


### paket-lock.json


Diese Datei wird automatisch von NPM erstellt.


Sie werden sich vielleicht fragen, warum wir eine weitere Datei brauchen, wenn wir bereits `package.json` haben?

Das ist der Grund:



- package.json" sagt nur, welche Version **eines Pakets** Ihr Projekt benötigt.

Beispiel:


```json
"dependencies": {
"picocolors": "^1.1.0"
}
```


Das `^1.1.0` bedeutet "jede Version, die mit 1.1.x kompatibel ist", also ist es flexibel.



- die Datei `package-lock.json` **friert** die exakten Versionen jedes einzelnen Pakets und seiner Unterabhängigkeiten ein, so dass jeder, der Ihr Projekt installiert, genau die gleiche Arbeitseinstellung erhält.


Warum ist das wichtig?


Wenn Sie in einem Team arbeiten, Ihr Projekt auf einem Server bereitstellen oder in der Zukunft darauf zurückkommen, möchten Sie sicherstellen, dass es immer noch auf die gleiche Weise funktioniert.

Wenn die Pakete aktualisiert wurden und Sie sie ohne Sperrdatei neu installieren, erhalten Sie möglicherweise eine etwas andere Version, die sich anders verhält.


Wenn Sie die `package-lock.json` in Ihrem Projekt aufbewahren, wird NPM immer genau die dort aufgelisteten Versionen installieren, um sicherzustellen, dass jeder dieselbe Umgebung hat.


`package-lock.json` sperrt alles auf eine ganz bestimmte Version, um das Projekt auf anderen Rechnern reproduzierbar zu machen.


Wenn Ihr Paket jedoch von vielen Leuten benutzt werden muss, können Sie es auch nicht übergeben, so dass NPM nur die Datei `package.json` findet und automatisch die neuesten Versionen installieren kann, die in dieser Datei erlaubt sind.


Aber das sind Dinge, um die Sie sich später kümmern sollten, wenn Sie anfangen, Ihren eigenen Code zu veröffentlichen. Für den Moment haben wir die Grundlagen von NPM vorgestellt, damit Sie die von anderen Entwicklern veröffentlichten Bibliotheken finden und in Ihren Projekten verwenden können.



## Vernetzung in NodeJS

<chapterId>f2cabd8b-754b-5c97-8d6a-8412a9a184c7</chapterId>


NodeJS wird häufig als Backend-Sprache verwendet: Sie können Ihr Skript in einen Server verwandeln und es auch dazu verwenden, Anfragen an andere Server zu stellen.


In diesem Kapitel werden wir einige grundlegende Netzwerkfunktionen vorstellen, die Ihnen dies ermöglichen.


### fetch()


Wenn Ihr Programm Daten von einer Website oder einer API herunterladen soll, müssen Sie eine **HTTP-Anfrage** stellen.


In modernen Versionen von NodeJS können Sie die eingebaute Funktion "fetch()" verwenden.


Hier ist ein Beispiel für eine GET-Anforderung an eine API:


```javascript
const response = await fetch("https://jsonplaceholder.typicode.com/posts/1")
const data = await response.text()

console.log(data)
```


Wenn Sie dies ausführen, sehen Sie etwas wie:


```
{
"userId": 1,
"id": 1,
"title": "...",
"body": "..."
}
```


Das geschieht folgendermaßen:


1. fetch()` nimmt eine URL und stellt eine Anfrage.

2. Sie gibt ein **Promise** zurück, das in ein `Response`-Objekt aufgelöst wird.

3. `response.text()` liest den Antwortkörper als Zeichenkette.


Aber die Zeichenkette, die Sie zurückbekommen, ist eigentlich JSON. Was ist das?


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


Das "JSON"-Objekt ist ein eingebautes Dienstprogramm in JavaScript, das für die Arbeit mit diesem Datenformat verwendet werden kann.


Sie können ein JavaScript-Objekt in eine JSON-Zeichenkette umwandeln, indem Sie `JSON.stringify()` verwenden:


```javascript
const user = { name: "Alice", age: 30 }

const jsonString = JSON.stringify(user)

console.log(jsonString)
```


Dies wird gedruckt:


```
{"name":"Alice","age":30}
```


Sie können JSON-Text auch mit `JSON.parse()` in ein JavaScript-Objekt zurückverwandeln:


```javascript
const jsonText = '{"name":"Bob","age":25}'

const obj = JSON.parse(jsonText)

console.log(obj)
```


Dies wird gedruckt:


```
{ name: 'Bob', age: 25 }
```


Seien Sie vorsichtig: jSON.parse()" gibt einen Fehler aus, wenn die Zeichenkette kein gültiges JSON ist.


```javascript
JSON.parse("not json") // ❌ Error!
```


Stellen Sie also sicher, dass die Zeichenfolge richtig formatiert ist.


### http"-Server


Mit NodeJS können Sie einen Webserver erstellen, ohne etwas anderes zu installieren.


Sie können das eingebaute `http`-Modul verwenden, um Anfragen von Clients zu bearbeiten und Antworten zurückzusenden.


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


Wenn Sie dieses Skript ausführen und `http://localhost:3000` in Ihrem Browser öffnen, werden Sie sehen:


```
Hello from NodeJS server!
```


Das passiert im Code:


1. Sie haben den `http`-Server aus der Node-Standardbibliothek importiert.

2. mit `http.createServer()` wird ein Server erstellt. Sie haben an `http.createServer()` einen Callback `(req, res) => {...}` übergeben, der jedes Mal ausgeführt wird, wenn sich jemand verbindet.

3. Sie haben der Antwort den Statuscode 200 zugewiesen (was einen erfolgreichen Vorgang anzeigt). Sie können über http-Statuscodes [hier] lesen (https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

3. `res.end()` sendet die Antwort und beendet die Verbindung.

4. `server.listen(3000)` startet den Server auf Port 3000.


Sie können auch `req.url` und `req.method` in der Anfrage überprüfen, um verschiedene Pfade oder Anfragearten zu behandeln.


Beispiel mit Routing:


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


Dies sind sehr einfache Beispiele. Um fortgeschrittenere Server zu bauen, würden die meisten Entwickler wahrscheinlich eine fertige Backend-Bibliothek wie [express](https://www.npmjs.com/package/express) herunterladen.


## Datenverarbeitung: Puffer, Ereignisse, Ströme

<chapterId>8c9623f0-a604-51a4-8fe4-871c849d3e3b</chapterId>


In diesem Kapitel werden wir hauptsächlich drei Objektklassen vorstellen:



- puffer", der kleine Abschnitte von Binärdaten darstellt
- `EventEmitter`, der verwendet werden kann, um einen asynchronen Prozess zu verfolgen, indem er Signale, sogenannte "Events", aussendet
- stream", der es uns ermöglicht, große Datenmengen in einem Puffer zu verarbeiten, und der den Prozess durch die Ausgabe von Ereignissen verfolgt


Diese sind in professionellem NodeJS-Code sehr verbreitet. Auch wenn Sie sie in Ihren ersten Projekten vielleicht nicht verwenden, ist es gut, ein grundlegendes Verständnis dafür zu bekommen, wann Sie mit ihnen interagieren müssen


### Puffer


In NodeJS ist ein **Puffer** ein Objekttyp, der für die Arbeit mit binären Daten verwendet wird.


Man kann sich einen Puffer als einen Behälter mit fester Größe für Rohbytes vorstellen.


So erstellen Sie einen Puffer aus einer Zeichenkette:


```javascript
const buf = Buffer.from("hello")
console.log(buf)
```


Dies druckt etwas wie:


```
<Buffer 68 65 6c 6c 6f>
```


Diese Zahlen (`68`, `65`, `6c`, usw.) sind hexadezimale Darstellungen der Buchstaben von `Hallo`.


Sie können sie wie folgt in eine Zeichenkette zurückverwandeln:


```javascript
console.log(buf.toString())
```


Dies wird gedruckt:


```
hello
```


Sie können auch einen Puffer mit einer bestimmten Größe anlegen, der mit Nullen gefüllt ist:


```javascript
const buf = Buffer.alloc(10)
console.log(buf)
```


Dies druckt etwas wie:


```
<Buffer 00 00 00 00 00 00 00 00 00 00>
```


Sie können in den Puffer schreiben:


```javascript
buf.write("abc")
console.log(buf)
```


Und Sie können auf einzelne Bytes zugreifen:


```javascript
console.log(buf[0]) // prints the ASCII number for 'a', which is 97
```


Puffer sind besonders nützlich, wenn Sie Daten auf einer sehr niedrigen Ebene manipulieren müssen.


### Veranstaltungen


In JavaScript ist ein **Ereignis** etwas, das in Ihrem Programm passiert und auf das Sie reagieren können.


Zum Beispiel:



- das Laden einer Datei abgeschlossen ist
- ein Timer läuft ab
- ein Benutzer klickt auf eine Schaltfläche
- eine Netzanfrage liefert Daten


Ein **Ereignis** ist nur ein Signal, dass etwas passiert ist, und man kann Code schreiben, um auf diese Ereignisse zu warten und darauf zu reagieren.


In NodeJS können viele Objekte Ereignisse auslösen. Diese Objekte werden **EventEmitters** genannt.


Hier ist ein Beispiel:


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


Dies wird gedruckt:


```
Hello! An event happened.
```


Und zwar folgendermaßen:


1. Wir erstellen ein `EventEmitter`-Objekt.

2. Mit `.on("greet")` weisen wir sie an, einen Callback auszuführen, wenn das Ereignis `"greet" eintritt.

3. Später lösen wir das Ereignis `Gruß` mit `.emit()` aus.

4. Unser Callback wird ausgeführt


Sie können Daten mit dem Ereignis übergeben:


```javascript
emitter.on("greet",
(name) => console.log(`Hello, ${name}!`)
)

emitter.emit("greet", "Alice") // first argument is the type of event, second argument is the data we pass with this event
```


Dies wird gedruckt:


```
Hello, Alice!
```


Sie können Zuhörer auch für andere Ereignisse registrieren:


```javascript
emitter.on("goodbye", () => {
console.log("Goodbye!")
})

emitter.emit("goodbye")
```


Sie können einem Ereignistyp beliebig viele Zuhörer zuordnen, und Sie können viele verschiedene Ereignistypen von ein und demselben Emitter auslösen.


Viele Objekte in NodeJS geben Ereignisse aus, um dem Rest des Programms mitzuteilen, dass etwas passiert.



### Was sind Ströme?


Streams kombinieren Puffer und Ereignisse, um uns bei der Verarbeitung von Daten zu helfen.


Wenn wir mit Dateien, Daten aus dem Netz oder sogar langen Texten arbeiten, müssen (oder wollen) wir nicht immer alles auf einmal in den Speicher laden. Das könnte langsam sein oder sogar das Programm zum Absturz bringen, wenn die Daten zu groß sind.


Stattdessen können wir die Daten **nach und nach** verarbeiten, wenn sie ankommen oder gelesen werden, so wie man Wasser durch einen Strohhalm trinkt, anstatt zu versuchen, das ganze Glas auf einmal zu trinken. Das nennt man einen **Stream**.


In NodeJS ist ein Stream ein Objekt, mit dem man Daten von einer Quelle lesen oder an ein Ziel schreiben kann **ein Stück auf einmal**.


NodeJS hat vier Haupttypen von Streams:



- Lesbar**: Datenströme, aus denen Sie Daten lesen können (wie beim Lesen einer Datei)
- Writable**: Streams, in die Sie Daten schreiben können (wie in eine Datei)
- Duplex**: Ströme, die sowohl lesbar als auch beschreibbar sind
- Transform**: wie Duplex-Streams, aber sie können die Daten während des Flusses verändern (transformieren)


### Lesbare Ströme


Nehmen wir an, Sie haben eine `bigfile.txt` zu verarbeiten. Sie können einen lesbaren Stream mit dem `fs`-Modul erstellen, um die Datei Stück für Stück zu lesen.


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


1. fs.createReadStream()` erzeugt einen lesbaren Stream.

2. Immer wenn ein Teil der Datei fertig ist, sendet der Stream ein "Daten"-Ereignis und gibt uns einen "Brocken" von Daten (einen "Puffer"). Wir drucken den Brocken aus.

3. Wenn die gesamte Datei gelesen wurde, wird das Ereignis "Ende" ausgelöst.

4. Wenn ein Fehler auftritt (z. B. weil die Datei nicht existiert), wird das Ereignis "error" ausgelöst.


Auf diese Weise können Sie riesige Dateien lesen, ohne sie alle auf einmal in den Speicher zu laden.


Wenn wir wollen, dass die Daten in einer für den Menschen lesbaren Form (statt binär) ankommen, können wir die Kodierung des Stroms angeben:


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


Der Code wird nun die Datei in menschenlesbarer Form ausgeben.


### Beschreibbare Ströme


Mit einem beschreibbaren Stream können Sie Daten Stück für Stück irgendwo hinschicken.


Hier ist ein Beispiel für das Schreiben in eine Datei "target.txt" unter Verwendung eines Streams:


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


1. fs.createWriteStream()` erzeugt einen beschreibbaren Stream.

2. Wir schreiben einen Text mit `.write()` hinein.

3. Wenn wir fertig sind, rufen wir `.end()` auf, um den Stream zu schließen.

4. Wenn alle Daten geschrieben worden sind, wird das Ereignis "finish" ausgelöst.

5. Wenn etwas schief geht, wird das Ereignis "Fehler" ausgelöst.


Genau wie lesbare Streams eignen sich auch beschreibbare Streams gut für große Datenmengen, da nicht alles gleichzeitig im Speicher gehalten werden muss.


### Rohrleitungsströme


Das Beste an Streams ist, dass man sie miteinander **verknüpfen** kann: einen lesbaren Stream direkt mit einem schreibbaren Stream verbinden.


```javascript
const fs = require("fs")

const readable = fs.createReadStream("bigfile.txt")
const writable = fs.createWriteStream("target.txt")

readable.pipe(writable)
```


Hier:



- Der lesbare Stream liest von "bigfile.txt".
- Der beschreibbare Stream schreibt in `copy.txt`.
- .pipe()` sendet die Daten direkt vom lesbaren zum beschreibbaren Stream.


### Duplex-Ströme


Ein Duplex-Stream ist sowohl lesbar als auch beschreibbar. Ein Beispiel ist ein Netzwerk-Socket: Sie können Daten an ihn senden und von ihm empfangen.


Hier ist ein sehr einfaches Beispiel, das das Modul `net` verwendet:


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


In diesem Beispiel:



- Das `socket`-Objekt ist ein Duplex-Stream.
- Man kann darauf "schreiben" und auch auf "Daten"-Ereignisse warten.


### Ströme umwandeln


Ein Transformationsstrom ist ein Duplexstrom, der die Daten, die ihn durchlaufen, ebenfalls verändert.


Sie können zum Beispiel das eingebaute Modul `zlib` verwenden, um Daten zu komprimieren oder zu dekomprimieren.


So komprimieren Sie eine Datei mithilfe eines Transformationsstroms:


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


### Gegendruck


Manchmal ist ein beschreibbarer Stream langsam bei der Verarbeitung von Daten. Wenn wir einem beschreibbaren Stream immer wieder Daten schneller zuführen, als er sie verarbeiten kann, kann es zu Problemen kommen. Dies wird **Rückstau** genannt.


Wenn Sie die Methode `.write()` für einen beschreibbaren Stream aufrufen, gibt sie einen booleschen Wert zurück, der Sie darüber informiert, ob der Stream eine Pause benötigt. Sie müssen eventuell den Rückgabewert überprüfen, etwa so:


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


Dies war ein anschauliches Beispiel für die manuelle Weiterleitung von Daten von einem Readable zu einem Writable und die manuelle Verwaltung des Gegendrucks.


Normalerweise würden wir Daten mit der Methode `.pipe()` weiterleiten, die den Gegendruck automatisch behandelt.


Sie müssen sich also nur dann Gedanken über Gegendruck machen, wenn Sie aus irgendeinem Grund manuell `.write()` aufrufen.


## Schlussbemerkung

<chapterId>139e2ab8-df67-525a-85f0-5a2fa5e478f2</chapterId>


So, das war's. Wenn Sie den Lektionen gefolgt sind, sollten Sie jetzt in der Lage sein, einige einfache Programme in NodeJS zu schreiben.


Ich würde vorschlagen, genau das zu tun: Nachdem man die Grundlagen gelernt hat, ist das Erstellen einiger persönlicher Projekte der beste Weg, um zu üben und ein besserer Programmierer zu werden.


Es ist eigentlich egal, was Sie bauen, wichtig ist, dass Sie sich der Herausforderung stellen, Probleme mit Code zu lösen.


Moderne Programmiersprachen sind unglaublich leistungsfähig, und NodeJS ist wahrscheinlich der beste Werkzeugkasten, um in dieser Phase Ihrer Reise damit zu experimentieren.


Viel Glück!


# Letzter Abschnitt


<partId>322624d8-6fbc-11f0-a67a-5b145f10afc1</partId>


## Rezensionen und Bewertungen


<chapterId>3e93ac86-6fbc-11f0-8bae-9b2ed7914843</chapterId>

<isCourseReview>true</isCourseReview>

## Schlussfolgerung


<chapterId>49b3b9b2-6fbc-11f0-9870-5f5adcd3a0eb</chapterId>


<isCourseConclusion>true</isCourseConclusion>