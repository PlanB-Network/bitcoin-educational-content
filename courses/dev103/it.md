---
name: Fondamenti di JavaScript e NodeJS
goal: Imparare i fondamenti della programmazione JavaScript e lo sviluppo NodeJS per costruire applicazioni e strumenti pratici.
objectives: 

  - Imparare a conoscere la sintassi, i tipi e il flusso di controllo di base di JavaScript
  - Capire le funzioni, gli oggetti e le classi in JavaScript
  - Imparare le tecniche di gestione degli errori e di debug
  - Introduzione a NodeJS e al suo ecosistema

---

# Iniziate il vostro viaggio di sviluppo


Benvenuti a questo corso su JavaScript e NodeJS.


JavaScript è il linguaggio di programmazione più diffuso al mondo: è il linguaggio di scripting dei moderni browser, quindi è praticamente impossibile costruire un'applicazione web moderna senza scrivere *un po' di JavaScript*; e con il runtime NodeJS può essere utilizzato anche al di fuori dei browser, per creare script e applicazioni che vengono eseguite direttamente sul computer.


Questo corso è pensato per chi è completamente nuovo alla programmazione o per chi ha già utilizzato altri linguaggi ma vuole capire come funziona JavaScript, soprattutto nel contesto di NodeJS.


Alla fine del corso, dovreste essere in grado di scrivere i vostri programmi in JavaScript, di utilizzare la libreria standard NodeJS e di installare e utilizzare pacchetti di terze parti per creare strumenti utili.


+++
# JavaScript di base

<partId>a617327c-e5a2-52ca-9380-c63f44623dd4</partId>


## Impostazione

<chapterId>ba05a290-1782-5268-87c9-62fd09590e05</chapterId>


In questa sezione imposteremo la nostra macchina per scrivere ed eseguire il nostro primo programma JavaScript.


Un programma JavaScript è solo un insieme di (uno o più) file di testo, che contengono comandi da eseguire da un runtime JavaScript.


I nomi di questi file di testo terminano solitamente con un'estensione `.js`, come `my_script.js`, `my_program.js` ecc.


I comandi che contengono sono scritti nel linguaggio di programmazione JavaScript.


Un runtime JavaScript è un programma speciale che esegue questi file.


![](assets/en/1.webp)


### Installazione di NodeJS


Il runtime JavaScript più comune è NodeJS.


È possibile installarlo seguendo le [istruzioni ufficiali] (https://nodejs.org/en/download).


La pagina di download contiene le istruzioni per tutti e tre i principali sistemi operativi (OS): Windows, Linux e MacOS. Si presuppone che sappiate aprire un terminale nel vostro sistema operativo.


Poiché NodeJS è disponibile per tutti e tre i sistemi operativi, i programmi che scrivete potranno essere eseguiti su tutti (salvo alcuni casi limite).


Ciò significa che potete, ad esempio, scrivere un semplice videogioco in JavaScript sul vostro PC Windows e passarlo al vostro amico perché lo esegua sul suo Mac.


![](assets/en/2.webp)


### Modifica del testo


Uno degli aspetti positivi della programmazione è che si può scrivere il codice utilizzando qualsiasi editor di testo, persino il blocco note predefinito del sistema operativo.


Esistono però alcuni editor di testo specializzati nella scrittura di codice; alcuni sono disponibili gratuitamente, altri richiedono il pagamento di una licenza.


La scelta dell'editor di codice è un'enorme tana di coniglio che trascende lo scopo di questo corso, quindi non ne parleremo qui. Se non sapete cosa usare, l'editor gratuito più usato è [VSCode](https://code.visualstudio.com/).


Il suo Interface è un po' gonfio, ma ha ciò che serve: un editor di file, un esploratore di file (per visualizzare i file e le sottodirectory della directory su cui si sta lavorando) e un terminale per eseguire il codice. Supporta anche molti plugin e viene fornito con l'evidenziazione della sintassi di JavaScript per impostazione predefinita.


Se si vuole essere un po' più Cypherpunk, si può usare invece [VSCodium](https://vscodium.com/).


### Primo programma (hello world)


Tradizionalmente, quando si studia un linguaggio di programmazione, il primo programma che si scrive consiste nello stampare "hello world!" sulla console.


Creare una cartella chiamata `my_js_code/`, con all'interno un file chiamato `main.js` (questi nomi sono arbitrari).


Aprire la directory con VSCode.


Scrivete questo codice nel vostro file:


```javascript
console.log("hello world!")
```


Aprite un terminale ed eseguite questo comando per eseguire il programma:


```
node main.js
```


Il risultato dovrebbe essere


```
hello world!
```


### Cosa è successo


In JavaScript, tutto è un "oggetto".


`console' è un oggetto che viene utilizzato per il debug del programma.


`console.log` è il metodo più usato di `console`. Si limita a stampare qualsiasi argomento gli venga passato.


Si passano gli argomenti a `console.log` usando le parentesi tonde `()`.


Quindi, ad esempio, se si volesse stampare il numero `1000`, basterebbe scrivere


```javascript
console.log(1000)
```


Quindi eseguitelo eseguendo


```
node main.js
```


nel vostro terminale (d'ora in poi, questo corso presuppone che sappiate che questo è il modo in cui si esegue un programma).


Questo dovrebbe stampare


```
1000
```


Si possono passare più cose, come


```javascript
console.log(16, 8, 1993)
```


In questo modo si stamperà


```
16 8 1993
```


## Variabili e commenti

<chapterId>23050ab7-343b-5edf-9d37-e4e782e27ce0</chapterId>


I programmi di solito eseguono operazioni sui dati.


Le variabili sono come scatole con nome che utilizziamo per memorizzare i dati. Permettono di associare un dato a un nome specifico, in modo da poterlo recuperare in seguito con quel nome.


### dichiarazioni `let


Per dichiarare una variabile in JavaScript, si può usare la parola chiave `let`.


Dopo aver scritto `let`, scriviamo il nome che vogliamo dare alla variabile, poi un segno `=` e infine il valore che vogliamo memorizzare.


Ad esempio:


```javascript
let age = 25

console.log(age)
```


Il nome di una variabile (tecnicamente chiamato "identificatore") può di solito contenere lettere, trattini bassi (`_`), il segno del dollaro (`$`) e numeri, anche se il primo carattere non può essere un numero.


Nel codice precedente, abbiamo dichiarato una variabile chiamata `age` e vi abbiamo memorizzato il valore `25`.


Quindi, si stampa il valore utilizzando `console.log(age)`.


Se si esegue questo codice con `node main.js`, l'output sarà:


```
25
```


Gli identificatori sono sensibili alle maiuscole e alle minuscole, il che significa che le minuscole e le maiuscole contano come differenze negli identificatori, quindi ad esempio


```javascript
let age = 25

let Age = 20

console.log(age)
```


stamperà 25, perché queste sono considerate due variabili completamente separate!


È anche possibile memorizzare stringhe (testo) in una variabile:


```javascript
let message = "hello again"

console.log(message)
```


Viene stampato:


```
hello again
```


Come in precedenza, abbiamo usato `console.log()` per stampare il valore memorizzato nella variabile.


Ora facciamo entrambe le cose insieme:


```javascript
let age = 25

let message = "hello again"

console.log(age)

console.log(message)
```


Eseguendo questa operazione, si otterrà la stampa:


```
25
hello again
```

### Riassegnazione


Le variabili dichiarate con `let' possono essere modificate dopo la loro creazione.


Questo si chiama riassegnazione.


```javascript
let score = 10

console.log(score)

score = 15

console.log(score)
```


Per prima cosa, assegniamo `10` a `score`, quindi lo stampiamo.


Poi cambiamo il valore di `score` in `15` e lo stampiamo di nuovo.


L'output sarà:


```
10
15
```


È molto utile quando il valore cambia nel tempo, come in un gioco in cui il punteggio aumenta.


Aggiungiamo un'altra variabile al mix:


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


Viene stampato:


```
10
Alice
20
Bob
```


Come si può vedere, sia `score` che `player` sono stati modificati.


### dichiarazioni `const


La maggior parte delle volte, però, non vogliamo che una variabile cambi dopo che è stata creata. Per questo, si usa `const`.


`const` è l'abbreviazione di "costante". Una volta assegnato un valore a una variabile `const`, non è possibile modificarlo.


```javascript
const pi = 3.14
console.log(pi)
```


Questa stampa:


```
3.14
```


Ma se si cerca di fare questo:


```javascript
const pi = 3.14
console.log(pi)

pi = 99 // this line will cause an error
console.log(pi)
```


JavaScript darà un errore del tipo:


```
TypeError: Assignment to constant variable.
```


Questo perché `pi` è stato dichiarato usando `const` e non si può cambiare il suo valore dopo. Si sta comunicando all'interprete JavaScript che non si vuole che quella variabile cambi.


Questo è utile perché riduce le possibilità di modificarlo per errore. Quando i programmi diventano molto grandi, con migliaia di righe di codice, è impossibile tenere il passo con tutto ciò che accade contemporaneamente (questo è il motivo principale per cui usiamo i computer, per eseguire processi complessi che non possiamo calcolare con il nostro cervello), quindi diventa utile avere restrizioni come questa, che rendono il programma più deterministico.


È considerata una buona pratica dichiarare sempre i valori come `const`, a meno che non si sia sicuri di volerli modificare in seguito.


### Commenti in JavaScript


A volte vogliamo scrivere nel nostro codice delle note che non vengono eseguite. Questi sono chiamati commenti.


I commenti vengono ignorati dal programma quando viene eseguito, ma sono utili per spiegare le cose a noi stessi o ad altre persone.


Per scrivere un commento su una sola riga, usare `//`


```javascript
// This is a comment
const x = 10 // This is also a comment
console.log(x)
```


La stampa viene comunque effettuata:


```
10
```


I commenti sono lì solo per essere letti dagli esseri umani.


È anche possibile scrivere commenti su più righe utilizzando `/*` e `*/`


```javascript
/*
This is a multi-line comment.
It can span several lines.
*/
const y = 20
console.log(y)
```


In questo modo si stamperà


```
20
```


E il commento sarà ignorato.


Si possono usare i commenti per aggiungere piccole annotazioni al codice, in modo da ricordare cosa fa e perché è scritto in un certo modo. Può anche aiutare gli altri programmatori a comprenderlo.


## Tipi di base: numeri, stringhe, booleani

<chapterId>cfdb04f6-21a8-5143-bbf9-7aaae04962f0</chapterId>


In JavaScript, un "tipo" indica il tipo di dati di un valore.


Javascript ha alcuni tipi di base e in questa sezione ne esploreremo alcuni.


### Numeri e operazioni aritmetiche


Il primo tipo che introdurremo è `number`.


I numeri in JavaScript possono essere interi (come `5`) o decimali (come `3,14`).


Si possono eseguire operazioni aritmetiche: addizione, sottrazione, moltiplicazione e divisione.


Ecco un esempio di base:


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


Viene stampato:


```
15
5
50
2
```


Si possono anche usare le parentesi `()` per controllare l'ordine delle operazioni:


```javascript
const result = (2 + 3) * 4
console.log(result)
```


Questa stampa:


```
20
```


Senza le parentesi, sarebbe `2 + 3 * 4`, cioè:


```javascript
const result = 2 + 3 * 4
console.log(result)
```


Questo stamperebbe:


```
14
```


Perché nella matematica normale la moltiplicazione avviene prima dell'addizione.


### Stringhe e interpolazione


Il secondo tipo di JavaScript che introdurremo è `stringa`.


Le stringhe sono pezzi di testo. Per crearle si possono usare apici singoli `'...'` o doppi apici `"..."`.


```javascript
const greeting = "hello"
const name = 'Bob'
console.log(greeting)
console.log(name)
```


Questa stampa:


```
hello
Bob
```


Per combinare le stringhe, si può usare l'operatore `+`:


```javascript
const greeting = "hello"
const space = " "
const name = "Bob"

const fullGreeting = greeting + space + name
console.log(fullGreeting)
```


Viene stampato:


```
hello Bob
```


Ma c'è un modo migliore per combinare le stringhe, chiamato **interpolazione di stringhe**. Si usano i backtick per dichiarare la stringa `` `...`` e si scrivono le variabili usando `${...}` all'interno della stringa:


```javascript
const greeting = "hello"
const name = "Bob"

const fullGreeting = `${greeting} ${name}`
console.log(fullGreeting)
```


Anche questo viene stampato:


```
hello Bob
```


È possibile includere qualsiasi espressione all'interno di `${...}`:


```javascript
const age = 30
console.log(`Next year, I will be ${age + 1} years old.`)
```


Questa stampa:


```
Next year, I will be 31 years old.
```


L'interpolazione è molto comune nel moderno JavaScript.


### Operazioni booleane, di confronto e logiche


Il terzo tipo che introdurremo è `booleano`. Prende il nome dal matematico George Boole, che inventò la logica booleana.


I booleani sono semplici: solo due valori possibili, `vero' e `falso'.


È possibile memorizzarli in variabili:


```javascript
const theSkyIsBlue = true
const thisCourseIsBad = false

console.log(theSkyIsBlue)
console.log(thisCourseIsBad)
```


Questa stampa:


```
true
false
```


È possibile combinare i booleani utilizzando gli operatori logici:



- `&&` significa "e" e restituisce `true` solo se **entrambi** i valori sono `true`, altrimenti restituisce `false`
- `||` significa "o" e restituirà `true` se **almeno uno** dei valori è `true`, altrimenti (se sono entrambi falsi) restituirà `false`
- `!` significa "non", si applica prima di un booleano e lo capovolge: se il booleano è `vero` restituirà `falso`, e viceversa.


![](assets/en/3.webp)


Esempi:


```javascript
const isSunny = true
const isWarm = true

console.log(isSunny && isWarm)  // true
console.log(isSunny || isWarm)  // true
console.log(!isSunny)           // false
```


È possibile confrontare i valori in JavaScript utilizzando operatori come `>`, `<`, `===` e `!==`. Il risultato di questi confronti è sempre un booleano.


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


Javascript ha anche `>=` per significare "più grande o uguale" e `<=` per significare "più piccolo o uguale".


Gli operatori booleani, di confronto e logici sono spesso combinati nei programmi per dichiarare condizioni complesse, come ad esempio per garantire che "l'e-mail è arrivata E contiene l'immagine di cui ho bisogno OPPURE la lunghezza dell'e-mail è superiore a 10000 caratteri". Si scoprirà in seguito che si tratta di elementi essenziali per costruire la logica del programma.


## Array, null, undefined

<chapterId>7bf18183-5eae-53ed-83d2-b04982145d81</chapterId>


In questa sezione tratteremo altri tre tipi molto comuni nei programmi JavaScript:



- Array**: sequenze di valori
- undefined**: un valore speciale che significa "non è stato assegnato nulla"
- null**: un altro valore speciale che significa "intenzionalmente vuoto"


### Array e accesso agli indici


Un **array** è un tipo che può contenere più valori in un elenco.


Si crea una matrice utilizzando le parentesi quadre `[]` e separando gli elementi con le virgole.


Ecco un esempio di base:


```javascript
const numbers = [10, 2, 88]
console.log(numbers)
```


Questa stampa:


```
[ 10, 2, 88 ]
```


In una matrice si può memorizzare qualsiasi cosa, non solo i numeri:


```javascript
const things = ["apple", 42, true]
console.log(things)
```


Questa stampa:


```
[ 'apple', 42, true ]
```


Per accedere a un elemento specifico dell'array, si utilizza un **indice**. L'indice è la posizione dell'elemento, a partire da **0**.


Quindi in questo array:


```javascript
const colors = ["red", "green", "blue"]
```



- `colori[0]` è `"rosso" `
- i `colori[1]` sono `"Green"`
- `colori[2]` è `"blu" `


Proviamo:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[0])
console.log(colors[1])
console.log(colors[2])
```


Viene stampato:


```
red
green
blue
```


È possibile assegnare un valore a un indice specifico di una matrice


```javascript
const colors = ["red", "green", "blue"]

colors[1] = "yellow"

console.log(colors)
```


Viene stampato:


```
[ 'red', 'yellow', 'blue' ]
```


È possibile utilizzare come indice qualsiasi numero naturale, anche quello memorizzato in una variabile


```javascript

const i = 1
const colors = ["red", "green", "blue"]
console.log(colors[i])
```


Viene stampato:


```
green
```


Ma se si cerca di accedere a un indice che non esiste, si ottiene `undefined`:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[3])
```


Questa stampa:


```
undefined
```


Che cos'è?


### `indefinito`


Il valore speciale `undefined` significa "non è stato assegnato alcun valore".


Se si crea una variabile ma non le si attribuisce un valore, essa sarà "non definita":


```javascript
const name
console.log(name)
```


Questa stampa:


```
undefined
```


Poiché non abbiamo assegnato nulla a `nome`, JavaScript lo imposta a `undefined` per impostazione predefinita.


Come già visto, si può ottenere `undefined` quando si accede a un indice di array che non esiste:


```javascript
const fruits = ["banana", "apple"]
console.log(fruits[2]) // There is no index 2
```


Questa stampa:


```
undefined
```


### `null` e come trattarlo


anche `null` è un valore speciale. Significa "non c'è niente qui, e l'ho fatto apposta"


A differenza di `undefined`, che è automatico, `null` è qualcosa che si imposta da soli.


Ad esempio:


```javascript
const currentUser = null
console.log(currentUser)
```


Questa stampa:


```
null
```


Perché usare `null`? Forse ci si aspetta un valore più tardi, ma non è ancora pronto:


```javascript
let winner = null

// Later in the program:
winner = "Alice"

console.log(winner)
```


Questa stampa:


```
Alice
```


Quindi `null` è utile quando si vuole dire, ad esempio, "Più tardi dovrebbe esserci qualcosa qui, ma al momento è vuoto"


## Blocchi e flusso di controllo

<chapterId>be985168-2636-5b0d-a48f-ac1bbfbff8a7</chapterId>


Finora abbiamo scritto soprattutto righe di codice che vengono eseguite una dopo l'altra.


Ma quando scriviamo un codice, possiamo controllarne l'ordine di esecuzione.


Questo si chiama **flusso di controllo**.


Iniziamo con la comprensione dei blocchi e dell'ambito.


### L'ambito globale


Ogni variabile dichiarata esiste in un **scope**, ovvero la regione del codice in cui la variabile è nota.


Se si dichiara una variabile al di fuori di un blocco, essa esiste nell'ambito **globale**.


```javascript
const color = "blue"
console.log(color)
```


La variabile `color` è nell'ambito globale, quindi vi si può accedere da qualsiasi punto del file.


Se si aggiungono altre righe:


```javascript
const color = "blue"
console.log(color)

const size = "large"
console.log(color)
console.log(size)
```


Sia `color` che `size` sono variabili globali. Sono disponibili ovunque nel file.


Ma cosa succede all'interno di un blocco?


### Blocchi e ambito locale


Un **blocco** è un pezzo di codice circondato da parentesi graffe `{}`.


Le variabili dichiarate con `let' o `const' all'interno di un blocco esistono **solo** all'interno di quel blocco.


```javascript
{
const message = "inside block"
console.log(message)
}
```


Questa stampa:


```
inside block
```


Ma se provate questo:


```javascript
{
const message = "inside block"
}
console.log(message) // Error!
```


JavaScript darà un errore del tipo:


```
ReferenceError: message is not defined
```


Questo perché `messaggio` è stato dichiarato all'interno del blocco e non esiste al di fuori di esso.


Ciò significa che possiamo usare i blocchi per isolare porzioni di codice ed essere sicuri che "ciò che accade nel blocco rimane nel blocco" (un po' come a Las Vegas).


L'organizzazione del codice in blocchi ci permette anche di strutturare l'esecuzione del programma, con costrutti di flusso di controllo come `if`


### `if`, `else`


A volte si vuole eseguire del codice **solo se** qualcosa è vero. A questo serve l'istruzione `if`.


```javascript
const myAge = 20

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Questa stampa:


```
Am I an adult?
Yes I am!
```


Come si può vedere, il codice confronta `myAge` e `18`.

In questo caso l'operatore `>=` restituisce `true`, quindi il blocco viene eseguito.

Se la condizione non è "vera", il blocco non viene eseguito.


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Questa stampa:


```
Am I an adult?
```


È possibile aggiungere un blocco `else` per gestire il caso opposto:


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
} else {
console.log("No, I am not.")
}
```


Questa stampa:


```
Am I an adult?
No, I am not.
```


Entrambi i blocchi `if` e `else` sono ancora blocchi, quindi le variabili dichiarate al loro interno non esistono al di fuori.


Se vogliamo essere sicuri che qualcosa non sia vero, cosa possiamo fare?


Come già detto, JavaScript dispone dell'operatore "not", che inverte i booleani. Quindi possiamo fare


```javascript
const myAge = 17

const adult = myAge >= 18

console.log("Am I an adult?")

if (!adult) {
console.log("No, I am not.")
}
```

Questo viene ancora stampato:


```
Am I an adult?
No, I am not.
```

Perché abbiamo usato l'operatore `!` per invertire la variabile `adulto`.


`if (!adult) {...}` dovrebbe essere letto come "if not adult..."


Utilizzando blocchi, operatori logici e di confronto, possiamo strutturare l'esecuzione del programma, definendo variabili che devono essere `veritiere' (o `false') perché qualcosa accada.


### `mentre`, `interrompi`, `continua`


Un ciclo `while' ripete il codice *fino a quando* una condizione è vera.


```javascript
let count = 0

while (count < 3) {
console.log("Count is", count)
count = count + 1
}
console.log("the loop is over!")
```


Questa stampa:


```
Count is 0
Count is 1
Count is 2
the loop is over!
```


Quando `conteggio' diventa 3, il ciclo si interrompe.


È possibile interrompere un ciclo in anticipo utilizzando `break`:


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


Questa stampa:


```
0
1
2
```


Perché quando il numero diventa `3`, il blocco `if` viene eseguito e interrompe il ciclo.


È possibile saltare il resto di un ciclo utilizzando `continue`:


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


Questa stampa:


```
1
2
4
5
```


Perché quando il numero era `3`, `continue` faceva saltare al programma la riga che stampava il numero.


### per ... di ..."


Se si ha un array e si vuole fare qualcosa a ogni elemento in esso contenuto, si può usare `for ... of ... {...}`.


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const fruit of fruits) {
console.log(fruit)
}
```


Questa stampa:


```
apple
banana
cherry
```

Il blocco verrà eseguito una volta per ogni elemento dell'array.


`fruit` è una nuova variabile che prende il valore di ogni elemento dell'array, per operare su di esso all'interno del blocco.


### per ... in ..."


È possibile utilizzare `for ... in` per eseguire un ciclo sulle chiavi (indici) di un array:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(index)
}
```


Questa stampa:


```
0
1
2
```


È possibile utilizzare anche l'indice per ottenere il valore:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(fruits[index])
}
```


Questo stampa la stessa cosa di `per ... di`:


```
apple
banana
cherry
```


In pratica, per gli array, si dovrebbe preferire l'uso di `for ... of`, che è più semplice e pulito.


### Loop delimitati


A volte si vuole eseguire un loop per un numero specifico di volte o, in generale, scrivere un pezzo di codice che ripeta un blocco tenendo traccia di qualcosa.

Ecco a cosa serve un ciclo `for' delimitato.

Un ciclo vincolato di solito richiede tre condizioni, separate da un punto e virgola `;`, come in `(... ; ... ; ....)`.


```javascript
for (let i = 0; i < 3; i = i + 1) {
console.log(i)
}
```


Questa stampa:


```
0
1
2
```


Spieghiamolo:



- `let i = 0`: dichiara una variabile da utilizzare nel blocco (in questo caso è un contatore che inizia a 0)
- `i < 3`: dichiara una condizione che deve essere `vera` per il blocco da eseguire (in questo caso è "ripeti finché `i` è minore di 3")
- `i = i + 1`: dichiara del codice da eseguire dopo ogni esecuzione del blocco (in questo caso "aumenta `i` di 1")


Come si può notare, il ciclo vincolato ci consente di dichiarare condizioni più complesse per l'esecuzione ripetuta di un pezzo di codice, ma la maggior parte delle volte non è necessario.


### Etichette di blocco


Se si deve scrivere un flusso di controllo più complesso, JavaScript consente di dare un nome a un blocco usando una **etichetta** che può essere usata da `break` o `continue` per specificare *dove* saltare indietro.


Esempio:


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


Questa stampa:


```
Inside outer block
Inside inner block
Done
```


Abbiamo usato `break outer` per uscire completamente dal blocco `outer`.


È anche possibile etichettare i cicli. Prendiamo questo esempio:


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

È stato un esempio molto noioso, ma si spera che abbia chiarito la necessità (occasionale) delle etichette.


## Introduzione alle funzioni

<chapterId>cc324715-09c2-5cf7-9e6f-47a6f16bc04d</chapterId>


Man mano che i vostri programmi crescono, spesso vorrete **riutilizzare** pezzi di codice.


Ecco a cosa servono le **funzioni**: permettono di raggruppare del codice, dargli un nome ed eseguirlo quando si vuole.


### Dichiarazione di funzione


Per dichiarare una funzione, si può usare la parola chiave `function`. Poi le diamo un nome, una coppia di parentesi `()` con gli argomenti che accetta e un blocco di codice `{}` da eseguire. Cominciamo con una funzione che non accetta argomenti:


```javascript
function sayHello () {console.log(`Hello!`) }
```


Questo codice **dichiara** la funzione, ma non la esegue ancora.


### Chiamate di funzione


Per eseguire (o "chiamare") la funzione, si scrive il suo nome seguito da parentesi:


```javascript
function sayHello () {console.log(`Hello!`) }
sayHello()
```


Questa stampa:


```
Hello!
```


È possibile richiamare la funzione quante volte si vuole:


```javascript
function sayHello() {
console.log("Hello!")
}

sayHello()
sayHello()
```


Questa stampa:


```
Hello!
Hello!
```


Il codice all'interno della funzione viene eseguito solo quando la si chiama.


### Argomenti delle funzioni (input alle funzioni)


A volte si desidera che una funzione funzioni con alcuni input. È possibile farlo aggiungendo **argomenti** all'interno delle parentesi.


Ad esempio:


```javascript
function sayHelloTo (friend) {
console.log(`Hello ${friend}!`)
}
```


Ora questa funzione prende **un argomento** chiamato `amico`.


Quando si chiama la funzione, è possibile passare un valore:


```javascript
sayHelloTo("Tommy")
```


Questa stampa:


```
Hello Tommy!
```


È possibile richiamare la funzione con un nome diverso:


```javascript
sayHelloTo("Sam")
```


Questa stampa:


```
Hello Sam!
```


Il valore passato sostituisce la variabile `friend` all'interno della funzione.


È anche possibile utilizzare più di un argomento:


```javascript
function greetTwoPeople(person1, person2) {
console.log(`Hello ${person1} and ${person2}!`)
}

greetTwoPeople("Lina", "Marco")
```


Questa stampa:


```
Hello Lina and Marco!
```


### `ritorno` (output delle funzioni)


Le funzioni possono anche **restituire** valori. Ciò significa che inviano un valore al punto in cui la funzione è stata chiamata.


Ecco un semplice esempio:


```javascript
function getNumber() {
return 42
}

const result = getNumber()
console.log(result)
```


Questa stampa:


```
42
```


La funzione `getNumber()` restituisce `42`, lo memorizziamo in `result` e lo stampiamo.


Si può anche restituire qualcosa di calcolato:


```javascript
function add(a, b) {
return a + b
}

const result = add(2, 3)
console.log(result)
```


Questa stampa:


```
5
```


Una volta che un valore viene `ritornato', la funzione si ferma. Tutto ciò che viene dopo `return` in quel blocco non avviene.


```javascript
function saySomething() {

return "hi"

console.log("this never runs")

}

const message = saySomething()
console.log(message)
```


Questo stampa solo:


```
hi
```


perché viene restituito solo `"ciao". La riga `console.log("this never runs")` viene saltata.


Le funzioni possono essere considerate come piccoli sottoprogrammi. Ogni funzione può ricevere un input, lavorarlo e restituire un output.


Cosa succede se si cerca di utilizzare il valore di ritorno di una funzione, ma questa non ha restituito nulla?


```javascript
function doesNothing () {}

const x = doesNothing()

console.log(x)
```

Verrà stampato `undefined`. Il valore di ritorno di una funzione che non ha restituito nulla è `undefined`.


## Oggetti e classi

<chapterId>26689f25-8212-5057-8c21-3a05eee0ac75</chapterId>


JavaScript viene spesso definito un linguaggio orientato agli oggetti.


Ciò significa che aiuta a organizzare il codice raggruppando valori e funzioni in **oggetti**.


### Che cos'è un "oggetto"?


Un oggetto può contenere dati e funzioni che operano su tali dati. Quando una funzione viene inserita in un oggetto, si dice che è un "metodo".


Il primo oggetto che abbiamo visto è l'oggetto `console`. Si tratta di un oggetto che contiene diversi metodi per stampare sullo schermo e fare il debug dei nostri programmi.


Può anche stamparsi da solo; si può fare


```javascript
console.log(console)
```


e stamperà un elenco dei metodi che contiene. Per esempio, sulla mia macchina ha stampato


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


Come si può vedere, ha molti metodi che si possono usare per il debug!


Javascript ci fornisce un modo diverso per creare nuovi oggetti che possono fare tutto ciò che vogliamo.


### Creare un oggetto


Il modo più semplice per creare un oggetto è raggruppare i dati e le funzioni usando le parentesi graffe** `{}`.


Questo crea quello che chiamiamo un **oggetto anonimo**


```javascript
const cat = {
name: "Whiskers",
age: 3
}
```


Questo crea un oggetto e lo memorizza in una variabile chiamata `cat`.


L'oggetto ha due **proprietà**:



- `nome` con il valore `Bischi`
- `età` con il valore `3


Stampiamolo:


```javascript
console.log(cat)
```


Questa stampa:


```
{ name: 'Whiskers', age: 3 }
```


È possibile ottenere le proprietà dall'oggetto usando un punto, come in `objectName.propertyName`:


```javascript
console.log(cat.name)  // prints "Whiskers"
console.log(cat.age)   // prints 3
```


È anche possibile **cambiare** una proprietà:


```javascript
cat.age = 4
console.log(cat.age)  // now it prints 4
```


Come si può vedere, anche se un oggetto è definito come `const`, si possono comunque modificare i dati che contiene.


Nel caso degli oggetti, `const` impedisce solo di sovrascrivere l'intero oggetto:


```javascript
const cat = {
name: "Whiskers",
age: 3
}

cat.age = 5 // this works

cat = 5 // this throws an error, you're trying to reassign the whole object

```


Come già detto, gli oggetti possono contenere anche **funzioni** e quando una funzione fa parte di un oggetto, la chiamiamo **metodo**.


Ecco un esempio:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log("Meow!")
}
}
```


Questo oggetto ha:



- Una proprietà `name
- Un metodo `speak()


Chiamiamo il metodo:


```javascript
cat.speak()
```


Stampa:


```
Meow!
```


I metodi possono utilizzare i dati contenuti nell'oggetto attraverso la parola chiave `this`.

`this` si riferisce all'oggetto corrente. In questo esempio, verrà utilizzato per stampare il nome del gatto:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log(`${this.name} says meow!`)
}
}

cat.speak()
```


Questa stampa:


```
Whiskers says meow!
```


La parola `questo' significa "questo oggetto"... in questo caso, l'oggetto `gatto'.



Questi tipi di oggetti sono ottimi quando si vuole qualcosa di semplice e veloce. Ma se si ha bisogno di creare **molti oggetti** con la stessa struttura, c'è un modo migliore, ed è qui che entrano in gioco le **classi**.


### Classi e costruttori


Una **classe** è come un progetto. Indica a JavaScript come creare un certo tipo di oggetto.


Si definisce una classe usando la parola chiave `class`, seguita dal nome della classe e da un blocco di parentesi graffe `{}`.


```javascript
class Dog {}
```


Per convenzione, le classi iniziano con una lettera maiuscola.


È possibile creare un nuovo oggetto di una classe utilizzando `new`:


```javascript
const hachiko = new Dog()
```


Provare a stampare l'oggetto:

```javascript
class Dog {}

const myDog = new Dog()

console.log(myDog)
```


Otterrete


```
Dog {}
```


Come si può vedere, la classe Dog è vuota, quindi anche l'oggetto `myDog` è vuoto.


Possiamo definire quali proprietà devono contenere gli oggetti Dog, aggiungendo un `costruttore`.


Un costruttore è una funzione speciale che viene eseguita quando si crea (o "costruisce") un nuovo oggetto.


```javascript
class Dog {
constructor() { }
}
```


Vogliamo che ogni cane abbia un nome, quindi aggiungiamo un parametro `nome` alla funzione:


```javascript
class Dog {
constructor(name) { }
}
```


E poi usiamo `this` per dichiarare che `nome` è il `nome` dell'oggetto `Dog` che stiamo costruendo


```javascript
class Dog {
constructor(name) {
this.name = name
}}
```


Proviamo a usarlo ora:


```javascript
class Dog {
constructor(name) {
this.name = name
}
}

const myDog = new Dog("hachiko")

console.log(myDog)
```


Viene stampato qualcosa come:


```
Dog { name: 'hachiko' }
```


Come si può vedere, il metodo `costruttore` prende gli argomenti che si passano alla classe quando si fa `new Dog()` e li usa per costruire l'oggetto.


Vediamo come si articola:



- `class Dog` definisce la classe Dog.
- `costruttore(nome)` imposta l'oggetto quando viene creato.
- `this.name = name` memorizza il valore nel nuovo oggetto.
- `new Dog("hachiko")` crea un nuovo oggetto della classe, con la proprietà `name` impostata su `"hachiko"`.


Ora aggiungiamo un metodo alla nostra classe:


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


In questo modo si stamperà


```javascript
hachiko says barf!
```


Se facciamo lo stesso per due diverse istanze di Dog



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


otteniamo


```
hachiko says barf!
bobby says barf!
```


il metodo `speak()` utilizza la proprietà `name` del `Dog` su cui viene richiamato.


Questo è il motivo principale per cui esistono le classi: ci permettono di definire un insieme di metodi che operano sui dati e quindi di creare più oggetti che condividono la stessa "forma" di dati.


Quando si chiama un metodo su uno di questi oggetti, si opera sui dati che *quell'oggetto specifico* contiene.


### Modifica della forma di un oggetto


Gli oggetti in JavaScript sono flessibili. Anche dopo averne creato uno, è possibile aggiungere nuove proprietà o rimuovere quelle esistenti.


È consentito, ma va usato con attenzione.


Cominciamo con la nostra semplice classe `Dog`:


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


A questo punto, `myDog` ha solo una proprietà: `nome`. Possiamo comunque aggiungere nuove proprietà dopo la sua creazione:


```javascript
myDog.age = 5

console.log(myDog.age) // prints 5
```


Possiamo anche aggiungere un nuovo metodo:


```javascript
myDog.jump = function () {
console.log(`${this.name} jumps!`)
}

myDog.jump() // Fido jumps!
```


E possiamo anche rimuovere le proprietà, usando la parola chiave `delete`.


```javascript
delete myDog.name

console.log(myDog.name) // prints 'undefined'
```


Questo funziona, ma c'è qualcosa di importante da sapere: I motori JavaScript come il V8 (utilizzato in Node.js e nel browser Chrome) funzionano più velocemente quando gli oggetti mantengono sempre le stesse proprietà. Se si aggiungono o rimuovono proprietà dopo che l'oggetto è stato creato, ciò può rallentare le operazioni.


Nei piccoli programmi, questo non ha molta importanza. Ma in progetti più grandi (come i giochi), è meglio elencare tutte le proprietà nel costruttore fin dall'inizio, anche se non le si usa subito. In questo modo si mantiene stabile la forma dell'oggetto e si velocizza l'esecuzione del codice.


Ad esempio, invece di questo:


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


Si può fare


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


Entrambe le versioni funzionano, ma la seconda è migliore per le prestazioni. Si dice al motore in anticipo quali proprietà avrà ogni oggetto e si può ottimizzare di conseguenza.


JavaScript consente di rimodellare gli oggetti liberamente, ma quando si usano le classi è meglio pianificare in anticipo la forma dell'oggetto.



### Ereditarietà con `extends' e `super()`


A volte si vuole creare una classe che sia *quasi* uguale a un'altra classe, ma con qualche caratteristica in più.


Invece di modificare la forma degli oggetti (che, come già detto, non è ottimale per le prestazioni), o di dover riscrivere una nuova classe da zero, JavaScript consente di utilizzare una cosa chiamata **ereditarietà**.


Ereditarietà significa che una classe può **estendere** un'altra. La nuova classe ottiene tutte le proprietà e i metodi della vecchia e si può aggiungere o modificare ciò che serve.


Supponiamo di avere una classe base chiamata `Veicolo`:


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


Ora vogliamo creare una classe `Car`. Un'auto è un tipo di veicolo, ma potremmo volere che abbia alcune caratteristiche extra o un messaggio diverso quando si avvia. Invece di riscrivere tutto, possiamo usare `extends`:


```javascript
class Car extends Vehicle {
start() {
console.log(`${this.brand} car is ready to drive!`)
}
}
```


La classe `Car` ora **eredita** tutto da `Vehicle`. Ottiene la proprietà `brand` e abbiamo sostituito il metodo `start()` con una nostra versione.


![](assets/en/4.webp)


Proviamo:


```javascript
const myCar = new Car("Toyota")
myCar.start()
```


Questa stampa:


```
Toyota car is ready to drive!
```


Anche se `Car` non ha un proprio costruttore, utilizza comunque quello di `Vehicle`. Ma se vogliamo scrivere un costruttore personalizzato in `Car`, possiamo farlo, basta includere una chiamata al costruttore del suo genitore usando `super()`.


Ecco come:


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



Questa stampa:


```
Toyota Corolla is ready to drive!
```


Quindi, per riassumere



- `estende' significa che una classe si basa su un'altra.
- `super()` è usato per chiamare il costruttore della classe che si sta estendendo.
- La nuova classe ottiene tutte le proprietà e i metodi della classe originale.
- Si possono **sovrascrivere** i metodi (come `start()`) per fargli fare qualcosa di diverso.


Questo è utile quando si hanno diversi oggetti simili (come auto, camion e biciclette) e si vuole che condividano il codice, ma che si comportino comunque a modo loro.


### `istanza di`


La parola chiave `instanceof` controlla se un oggetto è stato creato da una certa classe.


Supponiamo di avere una classe chiamata `User`:


```javascript
class User {
constructor(username) {
this.username = username
}
}

const regularUser = new User("julia123")

console.log(regularUser instanceof User)
```


Questa stampa:


```
true
```


Conferma che `regularUser` è un `User`. Questo perché `regularUser` è stato creato utilizzando la classe `User`.


Funziona anche con classi **ereditate**. Per esempio, ecco una classe `Admin` che estende `User`:


```javascript
class Admin extends User {}

const ourAdmin = new Admin("admin42")

console.log(ourAdmin instanceof Admin)   // true
console.log(ourAdmin instanceof User)    // true
```


Entrambe le righe restituiscono `true`. Questo perché `Admin` è una sottoclasse di `User`, quindi `ourAdmin` è sia un `Admin` che un `User`


# JavaScript intermedio

<partId>243f63ab-4f34-5c30-80cb-84ef46f6761d</partId>


## Gestione degli errori

<chapterId>d0206bc5-d386-5e7f-9917-5803f392448c</chapterId>


Quando si scrivono programmi JavaScript più complessi, si incontrano **errori**. Si tratta di situazioni inaspettate in cui qualcosa va storto. Forse una variabile non è definita, ma si cerca di usarla, oppure un codice riceve un input sbagliato.


Se non si gestiscono correttamente questi errori, il programma potrebbe bloccarsi o comportarsi in modo imprevedibile. JavaScript fornisce strumenti per rilevare e gestire questi errori, in modo da poterli gestire con più grazia.


### Errore comune: accesso a un valore su `undefined`


Ecco una situazione comune che causa un errore:


```javascript
const user = undefined
console.log(user.name)
```


Se si esegue questo codice, si otterrà un errore simile a questo:


```
TypeError: Cannot read properties of undefined (reading 'name')
```


È JavaScript che vi dice: "Ehi, hai cercato di ottenere la proprietà `name` da qualcosa che è `undefined`, e questo non ha senso" Come si può vedere, quando si verifica questo tipo di errore, il programma smette di funzionare, a meno che non si sia scritto del codice specifico per catturarlo e gestirlo.


### lancio di un errore


A volte si vuole **rilanciare manualmente un errore** nel codice. In questo caso, si usa la parola chiave `throw`.


```javascript
throw new Error("This is a custom error message")
```


Questo arresta immediatamente il programma e lo stampa:


```
Uncaught Error: This is a custom error message
```


Si può usare `throw` per far rispettare le regole del programma. Ad esempio:


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


La seconda chiamata causa un errore perché la divisione per zero non è consentita in questo esempio.


### Catturare gli errori con `try...catch`


Se non si vuole che il programma si blocchi quando si verifica un errore, è possibile catturare l'errore utilizzando un blocco `try...catch`. Questo è utile quando si vuole che il programma continui a funzionare anche se qualcosa non funziona.


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log("Oops! Something went wrong.")
}
```


Uscita:


```
Oops! Something went wrong.
```


Ecco come funziona:



- Il codice all'interno del blocco `try` viene tentato per primo.
- Se si verifica un errore, JavaScript **salta al blocco `catch`**, saltando il resto del blocco `try`.
- Il blocco `catch` riceve l'errore, quindi è possibile stamparlo o gestirlo in un altro modo, come ad esempio


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log(`The message of the error was: "${error.message}"`)
}
```


Uscita:


```
The message of the error was: "Cannot read properties of undefined (reading 'name')"
```


### Il blocco `finalmente


Si può anche aggiungere un blocco `finalmente'. Si tratta di codice che viene **sempre eseguito**, indipendentemente dal fatto che ci sia stato o meno un errore.


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


Uscita:


```
Trying something risky...
Caught the error: Uh oh!
This will run no matter what.
```


## Evitare gli insetti

<chapterId>db12d9f6-5806-514c-998e-0ae24805104e</chapterId>


Questo capitolo mostra alcune delle insidie più comuni in JavaScript e come evitarle.


### `var` e Assignment senza dichiarazione


Nel vecchio codice JavaScript, le variabili venivano spesso dichiarate usando la parola chiave `var`. A differenza di `let` e `const`, che abbiamo già imparato a conoscere, `var` può comportarsi in modo confuso.


Ad esempio:


```javascript
{
var message = "hello"
}
console.log(message)
```


Ci si potrebbe aspettare che `messaggio` esista solo all'interno del blocco, ma non è così. `var` ignora l'ambito del blocco e rende la variabile disponibile nell'intera funzione o file.


Questo può portare a comportamenti inaspettati, soprattutto nei programmi più grandi. Per questo motivo, il codice JavaScript moderno dovrebbe sempre usare `let` o `const` invece di `var`.


Ancora peggio, JavaScript consente di assegnare valori alle variabili **senza dichiararle affatto**:


```javascript
function greet() {
user = "Alice"
}
greet()
console.log(user) // prints "Alice"
```


Questo crea una nuova variabile globale `name` senza alcuna dichiarazione. Questo può accadere silenziosamente e portare a bug che sono Hard da rintracciare, specialmente se si tratta di un semplice errore di battitura. Dichiarare sempre le variabili usando `let` o `const`.


### Sistema di tipi debole


JavaScript è debolmente tipizzato, cioè converte automaticamente i valori da un tipo all'altro, se necessario. Questa operazione è chiamata coercizione dei tipi e, sebbene possa essere comoda, spesso porta a risultati confusi.


Ad esempio:


```javascript
console.log("5" + 1)    // "51"
console.log("5" - 1)    // 4
console.log(true + 1)   // 2
console.log(null + 1)   // 1
```


In questi esempi, JavaScript cerca di indovinare cosa si intendeva. A volte trasforma le stringhe in numeri, i booleani in numeri o le stringhe in stringhe. Questo può far sì che il codice si comporti in modo inaspettato.


È importante conoscere il debole sistema di tipizzazione di JavaScript. Quando le cose iniziano a comportarsi in modo strano, potrebbero essere dovute a una coercizione di tipo inaspettata.


### `"use strict"`


È possibile attivare una modalità più severa che trasforma alcuni errori silenziosi in errori reali e impedisce l'uso di alcune delle caratteristiche più pericolose del linguaggio.


Per abilitare questa modalità più rigida, aggiungere questa riga all'inizio del file o della funzione:


```javascript
"use strict"
```


Ad esempio:


```javascript
"use strict"
name = "Alice" // ReferenceError: name is not defined
```


Senza la modalità strict, JavaScript creerebbe silenziosamente una variabile globale chiamata `nome`. Ma con la modalità rigorosa, questo diventa un vero e proprio errore, aiutando a individuare prima i bug.


La modalità Strict disabilita anche alcune funzioni obsolete di JavaScript e rende il codice più facile da ottimizzare e mantenere.


## Valore vs. Riferimento

<chapterId>bb898425-dc2f-5e5c-864b-0cb7a4a9aea9</chapterId>


JavaScript tratta diversi tipi di valori in modi diversi.


Alcuni valori vengono **copiati** quando li si assegna a una variabile.


Altre sono **condivise** quando si assegnano a una nuova variabile, quindi se si cambia una, cambia anche l'altra.


### Passaggio per valore


Quando un valore viene passato **per valore**, JavaScript ne fa una **copia**.


Quindi, se si cambia uno dei due, non si influisce sull'altro.


Questo accade con i tipi primitivi, come:



- numeri
- corde
- booleani (`vero` e `falso`)
- `null`
- `indefinito`


Vediamo un esempio:


```javascript
let a = 5
let b = a

b = 10

console.log(a) // 5
console.log(b) // 10
```


Abbiamo dato a `b` il valore di `a`, ma poi abbiamo cambiato `b` in `10`.


Poiché i numeri sono passati per valore, JavaScript ha copiato il `5` in `b`. Il `5` in `b` è indipendente dal `5` originale in `a`, quindi cambiare il valore di `b` non ha alcun effetto su `a`.


Proviamo con una stringa:


```javascript
let name1 = "Alice"
let name2 = name1

name2 = "Bob"

console.log(name1) // Alice
console.log(name2) // Bob
```


Anche in questo caso, la modifica di `nome2` non ha avuto effetto su `nome1`, perché le stringhe sono passate anche per valore.


La stessa cosa accade quando si passa una primitiva a una funzione: viene copiata. Quindi la funzione non può modificare l'originale.


```javascript
function plusOne(x) {
x = x + 1
}

let number = 5

plusOne(number)

console.log(number) // 5
```


Anche se all'interno della funzione `1` è stato aggiunto a `x`, il `numero` originale non è cambiato.


Questo perché nella funzione è stata passata solo una **copia**.


### Passaggio per riferimento


Gli oggetti vengono passati **per riferimento**.


Ciò significa che, invece di copiarle, JavaScript vi passa un **riferimento** e, se lo si modifica, anche tutte le altre variabili che vi puntano vedranno la modifica.


Ad esempio:


```javascript
const person1 = { name: "Alice" }
const person2 = person1

person2.name = "Bob"

console.log(person1.name) // Bob
console.log(person2.name) // Bob
```


Sia `persona1` che `persona2` puntano allo stesso oggetto in memoria.


Quindi, quando abbiamo cambiato `person2.name`, abbiamo cambiato anche `person1.name`, perché entrambi stanno guardando la stessa cosa.


Gli array sono oggetti, quindi proviamo a fare lo stesso con un array:


```javascript
const list1 = [1, 2, 3]
const list2 = list1

list2.push(4)

console.log(list1) // [1, 2, 3, 4]
console.log(list2) // [1, 2, 3, 4]
```


Abbiamo spinto `4` in `list2`, ma anche `list1` ne ha risentito, perché entrambi fanno riferimento allo stesso array.


Vediamo cosa succede quando passiamo un oggetto a una funzione:


```javascript
function rename(user) {
user.name = "Charlie"
}

const person = { name: "Dana" }

rename(person)

console.log(person.name) // Charlie
```


La funzione ha cambiato l'oggetto! Questo perché ha ricevuto un **riferimento** all'oggetto `persona' originale.


Non ha ottenuto una copia. Ha ottenuto l'accesso all'oggetto originale e la possibilità di modificarlo.


È importante ricordare questa distinzione, perché altrimenti il nostro codice potrebbe comportarsi in modo diverso da quello che ci aspettiamo. Ad esempio, potremmo scrivere una funzione con l'aspettativa che non modifichi gli argomenti che riceve e scoprire in seguito che in realtà li stava modificando (perché erano oggetti, quindi passati per riferimento).


## Lavorare con le funzioni

<chapterId>e0d277a8-c642-5af7-9e53-dee27c811967</chapterId>


Avete già imparato a dichiarare e utilizzare le funzioni in JavaScript. Ma JavaScript offre ulteriori strumenti per lavorare con le funzioni in modi potenti.


### Funzioni della freccia


Le funzioni a freccia sono un modo più breve di scrivere le funzioni. Invece di usare la parola chiave `funzione', si usa una freccia (`=>`).


Ecco una funzione normale:


```javascript
function greet(name) {
return `Hello, ${name}!`
}
```


La versione a freccia si presenta così:


```javascript
const greet = (name) => {
return `Hello, ${name}!`
}
```


Se la funzione ha **un'unica riga**, si possono saltare le parentesi graffe e `ritornare':


```javascript
const greet = (name) => `Hello, ${name}!`
```


Se la funzione ha **un solo parametro**, si possono anche saltare le parentesi intorno ai parametri:


```javascript
const greet = name => `Hello, ${name}!`
```


Le funzioni a freccia sono molto comuni nel moderno JavaScript, in quanto consentono di esprimere funzioni semplici con una quantità di boilerplate notevolmente inferiore.


### Parametri predefiniti


A volte si vuole che una funzione abbia un **valore predefinito** se non viene passato alcun argomento.


Si può fare in questo modo:


```javascript
function sayHello(name = "friend") {
console.log(`Hello, ${name}!`)
}

sayHello("Alice") // Hello, Alice!
sayHello()        // Hello, friend!
```


Il valore predefinito `"friend"` viene utilizzato quando non viene passato nulla.


### Parametri di diffusione (`...`)


Cosa succede se la funzione accetta un numero flessibile di argomenti?


È possibile utilizzare l'operatore **spread** (`...`) per riunirli in un array:


```javascript
function logAll(...items) {
console.log(items)
}

logAll(1, 2, 3) // [1, 2, 3]
logAll("a", "b") // ["a", "b"]
```


È quindi possibile utilizzare un ciclo per elaborare ciascun elemento:


```javascript
function logEach(...items) {
for (const item of items) {
console.log(item)
}
}
```


L'operatore spread è utile quando non si sa quanti argomenti verranno passati.


### Funzioni di ordine superiore


Una **funzione di ordine superiore** è una funzione che:



- prende in ingresso un'altra funzione
- e/o restituisce una funzione in uscita


Ecco un semplice esempio:


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


Questa stampa:


```
Hello, friend!
Hello, friend!
```


Possiamo passargli una funzione freccia:


```javascript
runTwice(
() => console.log("Hello!")
)
```


Questa stampa:


```
Hello!
Hello!
```


È anche possibile scrivere funzioni che **restituiscono** altre funzioni:


```javascript
function makeGreeter(name) {
return () => console.log(`Hi, ${name}`)
}

const greetAlice = makeGreeter("Alice")
const greetBob = makeGreeter("Bob")

greetAlice() // Hi, Alice
greetBob() // Hi, Bob
```


La funzione `makeGreeter` è una funzione che costruisce altre funzioni. Riceve una stringa e restituisce una nuova funzione che utilizza tale stringa nella sua chiamata a `console.log`.


Questo tipo di schema è molto potente, in quanto consente di lasciare dei "buchi" nelle funzioni, che possono essere riempiti in seguito con il comportamento necessario.


### `map()`, `filtro()`, `riduci()`


JavaScript fornisce alcuni utili metodi integrati da utilizzare con gli array.


Questi metodi accettano funzioni come argomenti, quindi sono anche funzioni di ordine superiore.


`map()` trasforma ogni elemento di un array in qualcos'altro.


Esempio:


```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map(x => x * 2)

console.log(doubled) // [2, 4, 6]
```


Ogni numero viene raddoppiato e il risultato è una nuova matrice.


`filtro()` rimuove gli elementi dall'array se non superano un test.


Esempio:


```javascript
const numbers = [1, 2, 3, 4, 5]
const numbersGreaterThanTwo = numbers.filter(x => x > 2)

console.log(numbersGreaterThanTwo) // [3, 4, 5]
```


Vengono mantenute solo le voci della matrice per le quali la condizione `x > 2` restituisce `true`.


`riduci()` è usato per combinare tutti gli elementi di un array in un unico valore.


Esempio:


```javascript
const numbers = [1, 2, 3, 4]
const total = numbers.reduce((current, next) => current + next)

console.log(total) // 10
```


`reduce` attraversa l'array e, in questo esempio, applica l'operatore `+` tra `1` e `2`, poi tra la risultante `3` e `3`, poi tra la risultante `6` e `4`, finché non ottiene la somma di tutte le voci dell'array (che è 10).


Si può usare `riduci()` per molte cose, come totali, medie o per costruire nuovi valori passo dopo passo.


Questi metodi (`map`, `filter`, `reduce`) sono strumenti potenti per elaborare i dati senza scrivere cicli manuali.


Si possono anche combinare in una catena di operazioni, come questa:


```javascript
const numbers = [1, 2, 3, 4, 5]

const result = numbers
.map(n => n * 2)        // Double each entry, obtain [2, 4, 6, 8, 10]
.filter(n => n > 3) // Keep only the entries bigger than 3, so you get [4, 6, 8, 10]
.reduce((n1, n2) => n1 + n2) // Adds them: 4 + 6 + 8 + 10 = 28

console.log(result) // 28
```


## Lavorare con gli oggetti

<chapterId>7842aada-f009-5518-b8e3-1104e166a035</chapterId>


In questo capitolo impareremo alcuni strumenti potenti e leggermente più avanzati per lavorare con gli oggetti in JavaScript.


### Proprietà private


A volte si vuole nascondere una proprietà di un oggetto, in modo che non possa essere modificata o accessibile dall'esterno dell'oggetto. JavaScript ci offre un modo per farlo, usando `#` prima del nome della proprietà. Questo crea una proprietà **privata**, accessibile solo dall'interno della classe.


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


Le proprietà private sono utili quando si vogliono evitare modifiche accidentali.


### proprietà `statiche


A volte, si vuole che una proprietà appartenga alla classe stessa, non a ogni oggetto creato da quella classe. Ecco a cosa serve `static`. Una proprietà `statica` è contenuta nella classe e tutti gli oggetti di quella classe vi faranno riferimento.


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


È utile per memorizzare dati e metodi condivisi che si applicano all'intero gruppo di oggetti, non solo a uno.


### `get` e `set`


In JavaScript, `get` e `set` consentono di creare proprietà che *sembrano* normali variabili, ma in realtà eseguono codice speciale in background.


Un metodo `get'ter viene eseguito quando si cerca di *leggere* una proprietà. Viene dichiarato scrivendo `get` prima di un metodo con il nome della proprietà.


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


Anche se `fullName` non è una proprietà regolare, possiamo usarla come tale e dietro le quinte viene eseguita la funzione `get` per ottenere il nome completo.


Un metodo `set'ter viene eseguito quando si *assegna* un valore a una proprietà. Permette di controllare cosa succede quando qualcuno cerca di cambiare quel valore. Viene dichiarato scrivendo `set` prima di un metodo con il nome della proprietà.


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


Quando facciamo `user.fullName = "John Smith"`, viene eseguito il metodo `set` e vengono aggiornati i valori `firstName` e `lastName`.


Quindi, anche se sembra che stiamo impostando una semplice variabile, in realtà stiamo innescando una logica che aggiorna altre proprietà.


## Chiavi e valori

<chapterId>01a397b8-c12a-5c39-82b3-6d9ebbb72a29</chapterId>


Ogni proprietà di un oggetto JavaScript ha una **chiave** (detta anche nome della proprietà) e un **valore**.


Ad esempio:


```javascript
const user = {
name: "Alice",
age: 30
}
```


In questo oggetto, `"nome"` e `"età"` sono le chiavi e "Alice" e `30` sono i loro valori.


### Accesso dinamico


A volte non si conosce in anticipo il nome di una proprietà... magari la si ottiene dall'input dell'utente o la si legge da una variabile. È comunque possibile accedervi utilizzando la **notazione parentetica**, come `myObject["keyName"]`.


```javascript
const user = {
name: "Alice",
age: 30
}

console.log(user["name"]) // Alice
```


Abbiamo passato la stringa `nome` all'oggetto per ottenere il valore corrispondente.


Possiamo salvare una chiave in una variabile e usarla per accedere al valore corrispondente in un secondo momento, come ad esempio


```javascript
const user = {
name: "Alice",
age: 30
}

const key = "name"

console.log(user[key]) // Alice
```


### Dinamico Assignment


È anche possibile creare o aggiornare le proprietà degli oggetti usando le variabili come chiavi.


```javascript
const settings = {}

const key = "theme"
settings[key] = "dark"

console.log(settings) // { theme: "dark" }
```


È utile quando si vuole costruire un oggetto passo dopo passo. Ad esempio:


```javascript
const user = {}

user["username"] = "bananaFan123"
user["email"] = "banana@fruit.com"

console.log(user)
// { username: "bananaFan123", email: "banana@fruit.com" }
```


È anche possibile utilizzare una chiave dinamica *durante la creazione* dell'oggetto, utilizzando le parentesi quadre:


```javascript
const key = "language"
const config = {
[key]: "JavaScript"
}

console.log(config.language) // JavaScript
```


Si tratta di una proprietà **computata**. Il valore all'interno delle parentesi quadre viene valutato e il risultato viene utilizzato come chiave.


### tipo `Simbolo


Oltre alle stringhe, JavaScript consente anche di utilizzare un tipo speciale chiamato `Simbolo` come chiave di un oggetto.


Cominciamo con un semplice esempio:


```javascript
const id = Symbol("userID")

const user = {
name: "Bob",
[id]: 12345
}

console.log(user[id]) // 12345
```


In questo esempio, `id' è un simbolo. Non è una stringa, ma funziona comunque come chiave. Se si prova a registrare `user` nella console, si vedrà questo:


```javascript
console.log(user) // { name: 'Bob', [Symbol(userID)]: 12345 }
```


Un'altra cosa importante: ogni simbolo creato è unico, anche se viene creato con la stessa stringa.


```javascript
const a = Symbol("label")
const b = Symbol("label")

console.log(a === b) // false
```


I simboli consentono di definire chiavi che non si scontrano con le chiavi normali. Per esempio, supponiamo di avere un oggetto con una proprietà `name`, ma l'oggetto sarà personalizzabile da un utente in futuro, in modi che non possiamo prevedere, e tale utente potrebbe aggiungere anche una proprietà `name`. Se la proprietà `name` originale fosse definita con una stringa, verrebbe sovrascritta da quella nuova, in questo modo:


```javascript
const obj = {
name: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy' }
```


Se invece utilizziamo un simbolo:


```javascript
const name = Symbol("name")

const obj = {
[name]: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy', [Symbol(name)]: 'John' }
```


Come si può vedere, la proprietà `name` originale viene in qualche modo preservata in questo modo. Questo può essere utile in alcuni casi limite.


## Oggetti di utilità

<chapterId>516e74c8-2a11-545a-a4d1-c2cabb91a273</chapterId>


JavaScript ci fornisce alcuni utili oggetti incorporati che ci aiutano a fare cose come il debug e le operazioni matematiche.


### Altri metodi della `console


Si è già visto `console.log`, che stampa i valori sullo schermo.


Ci sono altri metodi utili disponibili sull'oggetto `console` che possono aiutare a eseguire il debug dei programmi.


#### `console.warn`


Stampa un messaggio in giallo (o con un'icona di avviso in alcuni ambienti):


```javascript
console.warn("This is just a warning.")
```


#### `console.error`


Stampa un messaggio in rosso, come un errore:


```javascript
console.error("Something went wrong!")
```


#### `console.table`


Visualizza una matrice o un oggetto come tabella:


```javascript
const users = [
{ name: "Alice", age: 25 },
{ name: "Bob", age: 30 }
]

console.table(users)
```


Viene stampata una tabella del tipo:


```
┌─────────┬────────┬─────┐
│ (index) │  name  │ age │
├─────────┼────────┼─────┤
│    0    │ 'Alice'│  25 │
│    1    │ 'Bob'  │  30 │
└─────────┴────────┴─────┘
```


Può essere utile per visualizzare i dati strutturati.


#### `console.time` e `console.timeEnd`


È possibile misurare il tempo necessario per ottenere qualcosa:


```javascript
console.time("timer")
for (let i = 0; i < 1000000; i++) {}
console.timeEnd("timer")
```


Viene stampato qualcosa come:


```
timer: 2.379ms
```


Utile per alcuni semplici test sulle prestazioni.


### L'oggetto `Math


JavaScript mette a disposizione un oggetto `Math` con metodi utili per eseguire calcoli.


#### `Math.random()`


Restituisce un numero casuale compreso tra 0 (incluso) e 1 (esclusivo):


```javascript
const r = Math.random()
console.log(r)
```


Esempio di uscita:


```
0.4387429859
```


#### `Math.floor()` e `Math.ceil()`



- `Math.floor(n)` arrotonda **per difetto** al numero intero più vicino
- `Math.ceil(n)` arrotonda **su** al numero intero più vicino


```javascript
console.log(Math.floor(4.9)) // 4
console.log(Math.ceil(4.1))  // 5
```


#### `Math.round()`


Arrotonda al numero intero più vicino:


```javascript
console.log(Math.round(4.4)) // 4
console.log(Math.round(4.6)) // 5
```


#### `Math.max()` e `Math.min()`


Restituisce il valore più grande o più piccolo da un elenco di numeri:


```javascript
console.log(Math.max(5, 9, 3)) // 9
console.log(Math.min(5, 9, 3)) // 3
```


#### `Math.pow()` e `Math.sqrt()`



- `Math.pow(a, b)` dà `a' alla potenza di `b
- `Math.sqrt(n)` fornisce la radice quadrata di `n`


```javascript
console.log(Math.pow(2, 3))   // 8
console.log(Math.sqrt(16))    // 4
```


# JavaScript avanzato

<partId>72c30671-ca20-5617-92a5-d5ba7aa38c93</partId>


## Altre collezioni

<chapterId>a9a70c6d-a343-5a46-a383-e288bc2700e3</chapterId>


JavaScript offre alcuni tipi speciali di collezione che vanno oltre i normali array e oggetti. Questi includono `Map` e `Set`.


Aiutano a memorizzare e gestire gruppi di valori, ma funzionano in modo diverso da quanto visto finora.


Una `Map' è un insieme di coppie **chiave-valore**, proprio come un oggetto. Ma ha alcune importanti differenze:



- Le chiavi possono essere **qualsiasi valore**, non solo stringhe.
- L'ordine degli elementi viene conservato.
- Dispone di metodi integrati per facilitare il lavoro.


Si crea una nuova mappa in questo modo:


```javascript
const myMap = new Map()
```


Questo crea una mappa vuota. Per aggiungere voci alla mappa, utilizzare `myMap.set(key, value)`:


```javascript
myMap.set("name", "Alice")
```


Si aggiunge una chiave `"name"` con valore `"Alice"`.


È anche possibile utilizzare un numero come chiave:


```javascript
myMap.set(42, "The answer")
```


E persino un oggetto come chiave:


```javascript
const objKey = { id: 1 }
myMap.set(objKey, "Object as key")
```


Questo non funzionerebbe con gli oggetti regolari, che consentono solo chiavi stringa.


Per **ottenere un valore**, utilizzare `myMap.get(key)`:


```javascript
console.log(myMap.get("name"))     // Alice
console.log(myMap.get(42))         // The answer
console.log(myMap.get(objKey))     // Object as key
```


Per **verificare se una chiave esiste**, usare `myMap.has(key)`:


```javascript
console.log(myMap.has("name")) // true
```


Per **eliminare una chiave**, usare `myMap.delete(key)`:


```javascript
myMap.delete("name")
```


Per **cancellare l'intera mappa**, usare `myMap.clear()`:


```javascript
myMap.clear()
```


Le mappe sono ottime per gestire grandi collezioni di valori, perché l'accesso ai valori su una mappa di grandi dimensioni offre di solito prestazioni migliori rispetto a un oggetto di grandi dimensioni.


### `Set`


Un `Set` è un insieme di **valori** (senza chiavi), dove ogni valore deve essere **unico**. Ciò significa che:



- Non si può avere lo stesso valore due volte
- I valori vengono memorizzati nell'ordine in cui vengono aggiunti


Si crea un set come questo:


```javascript
const mySet = new Set()
```


Per **aggiungere valori**, utilizzare `mySet.add(value)`:


```javascript
mySet.add(1)
mySet.add(2)
mySet.add(2) // duplicate, will be ignored
```


Anche se abbiamo cercato di aggiungere `2` due volte, l'insieme manterrà solo una copia.


Per **verificare se un valore è presente nell'insieme**, utilizzare `mySet.has(value)`:


```javascript
console.log(mySet.has(2)) // true
console.log(mySet.has(3)) // false
```


Per **rimuovere un valore**, utilizzare `mySet.delete(valore)`:


```javascript
mySet.delete(2)
```


Per **cancellare tutto**, usare `mySet.clear()`:


```javascript
mySet.clear()
```


Un `Set` è utile quando si vuole mantenere una collezione di valori unici senza dover controllare manualmente i duplicati:


```javascript
const numberArray = [1, 2, 2, 3, 4, 4, 4, 5]

const numberSet = new Set(numberArray)

console.log(numberSet) // Set(5) { 1, 2, 3, 4, 5 }
```


La funzione `Set` evita i duplicati.


## Iteratori

<chapterId>61d24e5e-b7e4-541a-8322-778f61f26a72</chapterId>


La maggior parte delle cose in JavaScript su cui è possibile eseguire il loop (come array, stringhe, mappe, set) sono **iterabili**: possono fornire iteratori per il loro contenuto.


Un **iteratore** è un oggetto speciale in JavaScript che aiuta a scorrere un elenco di elementi **uno alla volta**.


### iteratori di `oggetti


A differenza degli array o delle mappe, gli oggetti regolari **non sono iterabili** con `for...of`. Se si prova questo:


```javascript
const user = {
name: "Alice",
age: 30
}

for (const value of user) {
console.log(value)
}
```


Si otterrà un errore:


```
TypeError: user is not iterable
```


Questo perché gli oggetti semplici non hanno un iteratore incorporato. Ma JavaScript offre altri strumenti per eseguire un ciclo su di essi.


#### `Oggetto.chiavi()`


Si può usare `Object.keys(obj)` per ottenere un array di **chiavi** dell'oggetto e quindi eseguire un ciclo su di esso:


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


Questa stampa:


```
name
age
```


#### `Oggetto.valori()`


Per passare in loop i **valori**, utilizzare `Object.values()`:


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


Questa stampa:


```
Alice
30
```


#### `Oggetto.voci()`


Se si vogliono **sia la chiave che il valore**, usare `Object.entries()`:


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


Questa stampa:


```
name is Alice
age is 30
```


Anche se gli oggetti non sono direttamente iterabili, questi metodi danno pieno accesso al loro contenuto in un modo che funziona bene con `for...of`.


Ma come funzionano gli iteratori?


### simbolo.iteratore


Il segreto di tutti gli iterabili è uno speciale **simbolo** chiamato `Symbol.iterator`.


Questo simbolo è una chiave incorporata che indica a JavaScript: "Questo oggetto può essere iterato"


Quando si chiama `myIterable[Symbol.iterator]()`, JavaScript restituisce un oggetto **iteratore** con un metodo `.next()`.


Vediamo come si presenta:


```javascript
const colors = ["red", "green", "blue"]

const iterator = colors[Symbol.iterator]()

console.log(iterator.next()) // { value: 'red', done: false }
```


Ogni chiamata a `.next()` fornisce il valore successivo. Quando ha finito, ritorna:


```javascript
{ value: undefined, done: true }
```


### `next()`


Il metodo `.next()` viene utilizzato per ottenere l'elemento successivo della sequenza.


Ogni volta che si chiama `.next()`, si ottiene un oggetto con due chiavi:



- `valore`: l'elemento corrente
- `done`: un booleano che dice se l'iterazione è terminata


Facciamo un esempio completo:


```javascript
const names = ["Lina", "Tom", "Eva"]      // declare an array
const iterator = names[Symbol.iterator]() // use the Symbol.iterator function to get an iterator for this array

let result = iterator.next()              // get the first element of the array

while (!result.done) {                    // repeat this loop until you reach the last element of the array, which is marked with { done: true }
console.log(result.value)               // print the value of each element
result = iterator.next()                // get the next element of the array
}
```


Questa stampa:


```
Lina
Tom
Eva
```


Ecco come funziona un ciclo `for...of': utilizza questo schema con `.next()`.


Si otterrà lo stesso risultato con


```javascript
const names = ["Lina", "Tom", "Eva"]

for (const result of names) {
console.log(result)
}
```


### Rendere una classe iterabile


È anche possibile definire una propria classe **iterabile** aggiungendo un metodo `[Symbol.iterator]()`.


Diciamo che vogliamo una classe che rappresenti una **gamma di numeri**, come da 1 a 5.


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


Questa stampa:


```
1
2
3
4
5
```


Ecco cosa sta succedendo:



- Abbiamo definito una classe `Range
- All'interno della classe, abbiamo implementato `[Symbol.iterator]()`, in modo che JavaScript sappia come iterarlo
- Il metodo `next()` restituisce ogni numero uno alla volta
- Quando si raggiunge la `fine`, restituisce `{ done: true }`


Ora la nostra classe `Range` funziona come un array e possiamo usarla in qualsiasi ciclo che si aspetta un iterabile.


### Funzioni del generatore e `rendimento


Per facilitare la creazione di iteratori, JavaScript mette a disposizione **funzioni generatrici**, utilizzando la parola chiave `function*` (è `function` con una `*` alla fine) e la parola chiave `yield`.


Proviamo:


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


Ogni `sconto' restituisce un valore e **promette** la funzione fino a quando non viene chiamato il successivo `.next()`.


È anche possibile eseguire un ciclo su un generatore con `for...of`:


```javascript
for (const num of numberGenerator()) {
console.log(num)
}
```


Questa stampa:


```
1
2
3
```


## Concorrenza con callback

<chapterId>f3fc76ca-b3ef-54eb-a06e-501007002054</chapterId>


Finora il nostro codice è stato **sincrono**: viene eseguito una riga alla volta, in ordine. Ma alcune cose nel mondo reale richiedono tempo e non vogliamo che l'intero programma si fermi in attesa.


In questo capitolo introdurremo un nuovo concetto: *la *valuta**. Permette di manipolare l'ordine in cui le cose vengono eseguite. Questo è utile quando si ha a che fare con cose come timer, input dell'utente o lettura di file dal disco. JavaScript offre diversi strumenti per la concomitanza.


### `setTimeout`


La funzione `setTimeout` consente di **eseguire una funzione in un secondo momento**, dopo che è trascorso un certo tempo.


Esempio:


```javascript
console.log("Start")

setTimeout(
() => console.log("This runs after 2 seconds"),
2000
)

console.log("End")
```


Questa stampa:


```
Start
End
This runs after 2 seconds
```


Anche se `setTimeout` appare nel mezzo del codice, non blocca il resto. Al contrario, pianifica l'esecuzione della funzione **più tardi** e passa immediatamente oltre.


Il valore `2000` significa 2000 millisecondi (cioè 2 secondi).

Ecco una riscrittura più verbosa e adatta ai principianti delle sezioni **Callback** e **Promise**, utilizzando la manipolazione dei dati e annotazioni chiare:


### Richiami


Un **callback** è solo una funzione che diamo a un'altra funzione in modo che possa essere **richiamata in seguito**.


Vediamo un esempio reale utilizzando i numeri. Immaginiamo di avere un elenco di numeri e di voler raddoppiare ciascuno di essi, per poi applicare una funzione (il callback) all'array "raddoppiato" risultante, ma di volerlo fare con un piccolo ritardo, come se stessimo aspettando qualcosa di lento (come il caricamento di dati da Internet).


Ecco una funzione che lo fa utilizzando un **callback**:


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


Proviamo a utilizzare questa funzione:


```javascript
const input = [1, 2, 3]

doubleNumbers(input, function(result) {
console.log("Here is the doubled array:", result)
})
```


Dopo 1 secondo, viene stampato:


```
Here is the doubled array: [ 2, 4, 6 ]
```


**Che cosa sta succedendo qui?


1. Passiamo `input' come elenco di numeri che vogliamo raddoppiare.

2. Passiamo anche una funzione **callback** che dice al programma cosa fare *dopo* il raddoppio.

3. All'interno di `doubleNumbers`, simuliamo un ritardo utilizzando `setTimeout`, quindi eseguiamo il raddoppio.

4. Una volta fatto questo, chiamiamo il callback sull'array "raddoppiato" risultante.


Questa tecnica funziona, ma immaginate di voler fare **altri passi** dopo questo, come filtrare i numeri piccoli e poi sommarli. Si dovrebbero **annidare** altri callback come questo:


```javascript
doubleNumbers(input, function(doubled) {
filterBigNumbers(doubled, function(filtered) {
sumNumbers(filtered, function(total) {
console.log("Final result:", total)
})
})
})
```


Questo è Hard da leggere e disordinato. Questo stile è chiamato **callback hell**, ed è esattamente ciò che `Promise` è stato creato per risolvere.


## Concorrenza con le promesse

<chapterId>30fddaca-729f-5c8d-bf86-8dfc7b3c9800</chapterId>


Una `Promessa' è un oggetto JavaScript integrato che rappresenta un valore che **sarà pronto in futuro**.


Possiamo creare una Promessa come questa:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve("It worked!") // This means everything went OK
})
```


La parte `new Promise()` crea la promessa.


Al suo interno, gli diamo una funzione con due parametri:



- `resolve`, è una funzione che chiamiamo quando tutto è andato a buon fine
- `reject`, è una funzione che chiamiamo se qualcosa va storto


Nell'esempio precedente, lo risolviamo immediatamente con il messaggio `"Ha funzionato!


### `.then()`


Per fare qualcosa **dopo** che la promessa è stata fatta, si usa `.then()`:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve(100) // This means everything went OK
})

promise.then(result => {
console.log("The result is:", result)
})
```


Questa stampa:


```
The result is: 100
```


Il valore passato a `resolve()` viene inviato alla funzione all'interno di `.then()` come `risultato`.


Simuliamo un compito che richiede 2 secondi utilizzando `setTimeout`:


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


Attendere 2 secondi e poi stampare:


```
Done waiting!
```


### `rifiutare()`


Creiamo una promessa che **fallisce**:


```javascript
const failingPromise = new Promise((resolve, reject) => {
reject("Something went wrong")
})
```


Ora, se usiamo `.then()` su questo, non succederà nulla, perché `.then()` gestisce solo i successi.


Per gestire gli errori, si usa `.catch()`:


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


Questo stampa solo


```
Caught an error: Something went wrong
```


Il valore passato a `reject()` viene inviato alla funzione `.catch()`.


Costruiamo una Promessa che **a volte funziona e a volte fallisce**, in base a qualche condizione.


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


Ora possiamo chiamarlo e gestire entrambi i casi:


```javascript
checkNumber(5)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Questa stampa:


```
Success: Positive number
```


E se proviamo con un numero diverso:


```javascript
checkNumber(-1)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Stampa:


```
Failure: Not a positive number
```


### Concatenamento di operazioni tramite `Promessa



Possiamo riscrivere il nostro esempio precedente usando `Promise`, e il risultato sarà molto più pulito.


Iniziamo scrivendo una nuova versione della nostra funzione di raddoppio, ma questa volta restituisce una **promessa**:


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


Ora possiamo usare `.then()` per dire a JavaScript cosa fare con il risultato:


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


Questa stampa:


```
Doubled numbers: [ 2, 4, 6 ]
```


Finora funziona come la versione con callback, ma ora il codice è più facile da estendere e da leggere.


Supponiamo di voler aggiungere altri passaggi:


1. Per prima cosa, raddoppiare tutti i numeri

2. Quindi, rimuovere i numeri inferiori a 4

3. Infine, aggiungeteli tutti insieme


Possiamo scrivere una funzione per ogni fase, utilizzando tutte le promesse:


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


Ora possiamo **catenarli** insieme in questo modo:


```javascript
const input = [1, 2, 3]

doubleNumbers(input)
.then(filterBigNumbers)
.then(sumNumbers)
.then(
result => console.log("Final result after all steps:", result)
)
```


Questa stampa:


```
Final result after all steps: 10
```


Vediamo come funziona:


1. `DoubleNumbers` raddoppia l'array: `[2, 4, 6]`

2. il `filtroBigNumbers` rimuove qualsiasi cosa ≤ 3: `[4, 6]`

3. `sumNumbers` somma i numeri rimanenti: `4 + 6 = 10`

4. Infine, stampiamo il risultato.


Ogni `.then()` attende che il passo precedente finisca. In questo modo possiamo costruire una **catena di azioni** senza annidarsi. Questo rende il codice più leggibile e più facile da debuggare.


## Concorrenza con `async`/`await`

<chapterId>6e93d29f-c8bf-5fd1-a9c9-4e794ee6cbd0</chapterId>


Abbiamo visto come le catene di `Promise` ci aiutino a evitare l'inferno dei callback, ma possono comunque diventare un po' Hard da leggere quando ci sono molti passaggi coinvolti.


È qui che entrano in gioco `async` e `await`. Ci permettono di scrivere codice asincrono **che assomiglia a codice sincrono**, il che lo rende più facile da capire.


### Che cos'è `async`?


Quando si scrive la parola chiave `async` prima di una funzione, JavaScript avvolge automaticamente il valore di ritorno della funzione in una Promessa.


Vediamo un esempio di base:


```javascript
async function greet() {
return "hello"
}
```


Se si chiama questa funzione:


```javascript
const result = greet()
console.log(result)
```


Vedrete questo:


```
Promise { 'hello' }
```


Anche se è stata restituita una stringa, JavaScript la trasforma in una Promessa. È possibile ottenere il valore effettivo utilizzando `.then()` in questo modo:


```javascript
greet().then( result => console.log(result) ) // prints "hello"
```


Oppure si può usare `await`...


### Che cos'è l'"attesa"?


La parola chiave `await` dice a JavaScript: "aspetta che questa Promessa venga eseguita e poi dammi il risultato"


Ma si può usare `await` solo **all'interno di una funzione asincrona**.


Riscriviamo l'esempio usando `await`:


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


Ora possiamo utilizzare il risultato come se fosse un valore normale.


Ora facciamo qualcosa di più utile.


### Simulazione di un ritardo con `await


Creeremo una semplice funzione `wait` che prende come parametro una quantità di millisecondi e si limita a risolvere dopo quel numero di millisecondi, senza fare nient'altro:


```javascript
function wait(ms) {
return new Promise(resolve => {
setTimeout(resolve, ms)
})
}
```


Proviamo a usarlo:


```javascript
async function test() {
console.log("waiting 2 seconds...")
await wait(2000)
console.log("done waiting")
}

test()
```


Questa stampa:


```
waiting 2 seconds...
done waiting
```


Si può pensare ad `aspettare` come a "fermarsi qui finché la promessa non è stata fatta, poi continuare"


Ciò consente di scrivere codice in modo **top-to-bottom** che si comporta in modo asincrono, senza concatenare chiamate `.then()`.


### In attesa di dati


Riprendiamo l'esempio precedente, in cui abbiamo raddoppiato i numeri, poi filtrato e quindi sommato. Ma questa volta useremo `async`/`await`.


Creeremo 3 funzioni che simulano l'attesa e restituiscono Promesse:


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


Ora scriviamo una funzione `async` per combinarli:


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


Questa stampa:


```
Final result: 10
```


Questo è molto più facile da leggere rispetto al concatenamento di `.then()` o all'annidamento di callback.


Sembra un normale programma passo-passo, ma si comporta comunque in modo asincrono.


## Iteratori asincroni

<chapterId>438b037d-9931-56d7-9052-7b4470f3c75b</chapterId>


Abbiamo già imparato a conoscere gli **iteratori** e a usare `for...of` per fare un loop su array e altre cose iterabili.


Ma cosa succede se i dati che vogliamo iterare richiedono tempo per arrivare?


A volte si desidera eseguire un loop su elementi che arrivano in modo **asincrono**, come i messaggi di una chat, le righe di un file o i numeri di una fonte lenta.


Per farlo, JavaScript ci mette a disposizione **itineratori asincroni**.


### Funzioni del generatore asincrono


Il modo più semplice per creare un iteratore asincrono è utilizzare una funzione **generatore asincrono**.


Scriviamo così:


```javascript
async function* generateNumbers() {
yield 1
yield 2
yield 3
}
```


Sembra proprio un generatore normale, ma con `async` prima di esso.


Ora possiamo usare `for await...of` per consumare i valori:


```javascript
async function run() {
for await (const n of generateNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


Viene stampato:


```
Got number: 1
Got number: 2
Got number: 3
Done!
```


Qual è la differenza con un normale generatore?


La differenza è che ora possiamo usare `await` all'interno del generatore.


Creiamo di nuovo un aiuto per il ritardo:


```javascript
function wait(ms) {
return new Promise(resolve => setTimeout(resolve, ms))
}
```


Ora diamo i numeri **lentamente**:


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


Provate a usarlo:


```javascript
async function run() {
for await (const n of generateSlowNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


### Perché usare gli iteratori asincroni?


Gli iteratori asincroni sono utili quando:



- I valori non arrivano tutti insieme.
- È meglio gestirli uno alla volta, **come vengono**.
- Si lavora con le promesse e si vuole eseguire il loop in modo pulito.


Per esempio, se si vogliono caricare i messaggi da un server di chat uno alla volta o scaricare un file di grandi dimensioni in pezzi, gli iteratori asincroni consentono di scrivere un ciclo `for' che funziona con dati ritardati.


### `Simbolo.asyncIteratore`


Possiamo anche usare gli iteratori asincroni nelle classi personalizzate.


Ecco un esempio che produce numeri con un ritardo:


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


Ora possiamo usare `for await...of` proprio come prima:


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


Questo consente di creare oggetti che possono essere iterati in modo asincrono


## Zucchero di sintassi Assignment

<chapterId>8b1ba7d8-ecfd-5470-b86e-73cb84ccc8b7</chapterId>


"Zucchero sintattico" significa scrivere qualcosa in modo più breve o più semplice, senza cambiare le sue funzioni. È solo un modo più carino per dire la stessa cosa.


JavaScript dispone di alcuni zuccheri sintattici incorporati che ci permettono di scrivere dichiarazioni più pulite e più brevi. In questo capitolo vedremo come assegnare valori in base a una condizione, aggiornare variabili con la matematica, estrarre valori da array o oggetti e copiarli o combinarli con una sintassi più semplice.


### L'operatore ternario


In JavaScript, è possibile assegnare un valore in base a una condizione utilizzando l'operatore **ternativo**, che è un modo breve per scrivere `if...else`.


Invece di fare:


```javascript
let message

if (isMorning) {
message = "Good morning"
} else {
message = "Hello"
}
```


Si può scrivere:


```javascript
const message = isMorning ? "Good morning" : "Hello"
```


Questo significa che:



- Se `isMorning` è vero, utilizzare `"Buongiorno"`
- Altrimenti, utilizzare `"Ciao"`


La forma generale è:


```javascript
condition ? valueIfTrue : valueIfFalse
```


Si può usare anche all'interno di altre espressioni:


```javascript
console.log(isSunny ? "Go outside" : "Stay in")
```


Assicuratevi di usarlo per decisioni **semplici**. Se la logica è complessa, si consiglia di usare `if...else`.


### Operatori alternativi Assignment


JavaScript dispone di **operatori di scelta rapida** per eseguire assegnazioni combinate con operazioni.


Vediamo il modo normale:


```javascript
let counter = 1
counter = counter + 1
```


Questo può essere abbreviato in:


```javascript
let counter = 1
counter += 1 // same as counter = counter + 1
```


Ecco i più comuni:


| Operator | Meaning             |
| -------- | ------------------- |
| `+=`     | add and assign      |
| `-=`     | subtract and assign |
| `*=`     | multiply and assign |
| `/=`     | divide and assign   |

Esempi:


```javascript
let score = 10
score += 5  // now score is 15
score *= 2  // now score is 30
score -= 10 // now score is 20
```


Sono utili quando si vuole aggiornare una variabile utilizzando il suo stesso valore.


### Destrutturazione


*la *distrutturazione** consente di estrarre i valori da array o oggetti e di memorizzarli facilmente in variabili.


#### Array


Supponiamo di avere:


```javascript
const colors = ["red", "green", "blue"]
```


Invece di fare:


```javascript
const first = colors[0]
const second = colors[1]
```


Si può fare:


```javascript
const [first, second] = colors
```


Questo assegna:



- da "primo" a "rosso"
- da "Green" a "Green"


È possibile anche saltare i valori:


```javascript
const [,, third] = colors
console.log(third) // blue
```


#### Oggetti


È possibile estrarre valori anche dagli oggetti:


```javascript
const user = { name: "Alice", age: 30 }

const { name, age } = user
console.log(name) // Alice
console.log(age)  // 30
```


Se la proprietà ha un nome diverso dalla variabile desiderata, è possibile rinominarla:


```javascript
const { name: username } = user
console.log(username) // Alice
```


La destrutturazione rende il codice più pulito quando si lavora con oggetti e array.


### Sintassi dello spread


La sintassi **spread** utilizza `...` per scompattare o copiare i valori.


#### Array


È possibile copiare o unire gli array:


```javascript
const a = [1, 2]
const b = [3, 4]

const both = [...a, ...b]
console.log(both) // [1, 2, 3, 4]
```


È anche possibile clonare una matrice:


```javascript
const original = [10, 20, 30]
const clone = [...original]
```


#### Oggetti


È possibile fare lo stesso con gli oggetti:


```javascript
const a = { x: 1 }
const b = { y: 2 }

const merged = { ...a, ...b }
console.log(merged) // { x: 1, y: 2 }
```


È anche possibile sovrascrivere i valori:


```javascript
const user = { name: "Alice", age: 30 }
const updated = { ...user, age: 31 }

console.log(updated) // { name: "Alice", age: 31 }
```


È molto utile per aggiornare gli oggetti senza modificare l'originale.


# NodeJS

<partId>42fe4d49-dace-5135-bb9e-b9d75034fb2a</partId>


## Come siamo arrivati a Node

<chapterId>0da1d60c-06c9-54e6-a181-ae7dabf6e3b8</chapterId>


In questo capitolo impareremo un po' di contesto storico su JavaScript e NodeJS.


Il contesto storico è molto importante nel software, perché spesso utilizziamo strumenti costruiti da altre persone e siamo quindi influenzati dalle decisioni prese in passato da queste ultime.


Capire il motivo di queste decisioni e come gli strumenti che utilizziamo sono diventati così come sono, ci aiuterà a sentirci un po' meno confusi su ciò che stiamo facendo.


### Origini di JavaScript


JavaScript è nato come un semplice linguaggio progettato per rendere interattive le pagine web.


Negli anni '90, i browser web come Netscape Navigator hanno aggiunto JavaScript in modo che gli sviluppatori potessero scrivere codice da eseguire direttamente nel browser.


L'idea originale era di avere Java come linguaggio principale per la creazione di siti web (con le cosiddette "applet Java") e JavaScript solo per le cose minori.


Il progetto di base è stato realizzato da Brendan Eich, all'epoca dipendente di Netscape, in meno di due settimane.


Ma la maggior parte delle persone preferiva l'uso di JavaScript a quello di Java, e anche le applet Java avevano qualche problema di sicurezza all'epoca, così alla fine Java è stato abbandonato come opzione e JavaScript è diventato lo standard de facto per lo sviluppo web.


### Il motore V8


JavaScript è un linguaggio interpretato, a differenza dei linguaggi compilati come il C.


Il codice scritto in un linguaggio compilato viene trasformato in un binario, che viene trasmesso direttamente alla CPU del computer.


![](assets/en/6.webp)


I linguaggi interpred, invece, tendono a essere più facili da usare e sono più vicini al modo in cui gli esseri umani pensano ("alto livello") piuttosto che al modo in cui le macchine funzionano ("basso livello"); quindi di solito hanno una macchina virtuale costruita per eseguire il loro codice.


Una macchina virtuale è un programma speciale che si frappone tra il codice scritto dall'utente e la CPU ed esegue il codice (perché la CPU non è in grado di comprenderlo).


Questo permette di programmare senza conoscere troppo la macchina sottostante, ma ha anche un costo in termini di prestazioni, perché il computer non esegue solo il vostro programma, ma un programma (la macchina virtuale) che esegue il vostro programma.


Man mano che le applicazioni web diventavano sempre più complesse, c'era la necessità di migliorare le prestazioni di JavaScript. Il motore V8 è l'interprete che alimenta JavaScript in Google Chrome. È stato sviluppato da Google e rilasciato nel 2008.


Mentre i vecchi motori JavaScript erano per lo più macchine virtuali tradizionali, il motore V8 è un compilatore JIT (just-in-time).


Il codice JavaScript viene dato in pasto al motore V8, che cerca di compilare al volo parti di esso come binari nativi. Questo permette di avere l'esperienza di un linguaggio di alto livello, con prestazioni che si avvicinano un po' di più ai linguaggi di basso livello. Questo ha reso JavaScript il linguaggio di alto livello più veloce al mondo, un po' come il "meglio dei due mondi".


### Il runtime NodeJS


Pur essendo facile da usare e abbastanza veloce da eseguire, dopo il rilascio del V8 JavaScript ha continuato ad avere un'enorme limitazione: poteva essere eseguito solo all'interno di un browser.


Perché è un problema?


Dal momento che i browser eseguono codice prelevato da milioni di fonti diverse su Internet, possono facilmente incorrere in malware, quindi sono "sandboxati" dal resto del sistema operativo.


![](assets/en/7.webp)


JavaScript non poteva accedere al file system e ad altre risorse locali del computer (almeno non facilmente come altri linguaggi), per cui questo rappresentava un limite significativo al tipo di applicazioni che si potevano creare con esso.


Nel 2009, Ryan Dahl ha pubblicato NodeJS, un runtime che consente di utilizzare il motore V8 al di fuori del browser, direttamente sul sistema operativo nativo del computer. Aggiunge inoltre molte funzionalità utili per la scrittura di programmi lato server e a riga di comando. Ad esempio, è possibile utilizzare NodeJS per creare un server web, leggere e scrivere file o creare strumenti per automatizzare le attività.


![](assets/en/8.webp)


In questo corso abbiamo esplorato le caratteristiche di JavaScript presenti sia nel browser che in NodeJS. Queste caratteristiche ci hanno permesso di definire i dati e di manipolarli in modo astratto. Nelle prossime lezioni esploreremo le funzionalità specifiche di NodeJS che ci permettono di interagire con il sistema operativo.


## Argomenti della riga di comando

<chapterId>960d20f3-c424-5d51-a041-ef17d2e94b6d</chapterId>


NodeJS ci permette, tra le altre cose, di costruire CLI (Command Line Interfaces).


Per questo abbiamo bisogno di un modo per ricevere gli argomenti della riga di comando, cosa che in Node viene fatta usando l'oggetto built-in `process`.


### `processo`


NodeJS fornisce un oggetto speciale chiamato `process` che rappresenta il programma in esecuzione.


Può essere utilizzato per ispezionare l'ambiente, la directory di lavoro corrente e persino per uscire dal programma quando necessario.


Ad esempio:


```javascript
console.log(process.platform)
```


Stampa la piattaforma del sistema operativo, come `win32`, `linux` o `darwin` (Mac).


### processo.argv


Quando si esegue un programma NodeJS dal terminale, si possono passare parole extra (argomenti) dopo il nome dello script. Questi sono memorizzati in `process.argv`.


Ad esempio, se si esegue questo comando:


```
node my_script.js alpha beta
```


È possibile stampare gli argomenti in questo modo:


```javascript
console.log(process.argv)
```


L'output potrebbe essere simile a questo:


```
[ '/path/to/node', '/path/to/my_script.js', 'alpha', 'beta' ]
```


I primi due elementi sono sempre il percorso del nodo e il percorso dello script. Qualsiasi parola aggiuntiva passata allo script viene dopo.


L'array `process.argv` può essere tagliato come qualsiasi altro array usando il metodo `.slice()`, quindi per ottenere solo gli argomenti che sono stati passati si può fare


```javascript
const args = process.argv.slice(2)

console.log(args)
```


Avere accesso agli argomenti che l'utente passa è fondamentale per sviluppare applicazioni a riga di comando.


## Moduli

<chapterId>4e1651a5-65fd-50bc-b22a-40313d5659ca</chapterId>


I runtime JavaScript come NodeJS di solito trattano ogni file JavaScript come un modulo separato.


Pensate a un modulo come a una scatola. La scatola ha il suo spazio privato, per cui le variabili e le funzioni dichiarate in essa non interferiscono con il codice di altre scatole. In pratica, ogni modulo ha il proprio ambito.


Un modulo può esportare alcuni dei suoi contenuti, rendendoli disponibili ad altri moduli, e può importare i contenuti che altri moduli hanno esportato. JavaScript consente di esportare e importare contenuti tra moduli, per collegare file diversi.


Un programma JavaScript è spesso composto da più moduli, collegati tra loro.


Perché usare i moduli? Suddividendo il codice in moduli, è possibile organizzare il programma in parti più piccole, chiare e riutilizzabili. Ogni modulo può concentrarsi su un solo tipo di attività, come la gestione di calcoli matematici, il lavoro con i file o la formattazione del testo.


### Moduli CommonJS


In NodeJS, il sistema più comune per gestire i moduli si chiama **CommonJS**.


In questo sistema, si può condividere (esportare) il codice da un modulo usando `module.exports` e caricarlo (importare) in un altro file usando `require()`.


Per rendere disponibile qualcosa al di fuori di un modulo, lo si assegna a `module.exports`:


```javascript
const greeting = "Hello!"

module.exports = greeting
```


Qui, la stringa `"Hello!"` è ciò che questo modulo esporta.


Per utilizzare il codice esportato da un altro file, si usa la funzione `require()` con il percorso del file:


```javascript
const greeting = require("./greeting.js")

console.log(greeting)
```


Questa stampa:


```
Hello!
```


Si possono esportare più cose raggruppandole in un oggetto anonimo, come


```javascript
const greeting1 = "hello"

const greeting2 = "hi"

module.exports = {
greeting1, greeting2
}
```


CommonJS era il sistema di moduli inizialmente adottato da NodeJS. In seguito sono stati aggiunti anche i moduli ES.


### Moduli ES


NodeJS supporta anche un altro tipo di moduli, chiamati **Moduli ES**, molto diffusi nello sviluppo web. Utilizzano le parole chiave `export` e `import`.


I moduli ES sono stati sviluppati per il browser e solo successivamente aggiunti a Node. Se si desidera utilizzarli, potrebbe essere necessario usare `.mjs` come estensione del file invece di `.js`, a seconda della versione di Node utilizzata.


In un file chiamato `greeting.mjs` si scrive


```javascript
export const greeting = "Hello!"
```

Come si può vedere, stiamo esportando la costante direttamente dove viene definita


In un altro file chiamato `index.mjs`, lo importiamo:


```javascript
import { greeting } from "./greeting.mjs"

console.log(greeting)
```


È possibile esportare dichiarazioni diverse in parti diverse del file, come ad esempio


```javascript
export const num = 10

export function double (x) {
return x*2
}
```


### La libreria standard di NodeJS


NodeJS include anche molti moduli integrati. Si tratta di moduli già pronti forniti da NodeJS che aiutano a svolgere compiti comuni come la lettura di file, il lavoro con il sistema operativo o la connessione alla rete.


Ad esempio, il modulo `os` fornisce informazioni sul sistema operativo in uso:


```javascript
const os = require("os")

console.log(os.platform())
```


Non è necessario installare questi moduli integrati, vengono forniti con NodeJS. Essi costituiscono la "libreria standard" del runtime e sono utilizzati dalla maggior parte delle applicazioni Node per eseguire operazioni come la lettura di file o la comunicazione via Internet.


Nei prossimi capitoli verranno mostrati alcuni esempi utili del loro utilizzo.


## Il modulo `fs

<chapterId>911e953a-35ae-5ee7-bd74-372501c32e81</chapterId>


Il modulo `fs` (abbreviazione di **file system**) fa parte della libreria standard di NodeJS. Permette di lavorare con i file e le directory del computer: si possono leggere i file, scrivere i file, cancellarli, rinominarli e altro ancora.


Per utilizzarlo, è necessario prima importarlo all'inizio del file:


```javascript
const fs = require("fs")
```


### API di sincronizzazione


Il modo più semplice di usare `fs` è con i suoi metodi **sync**.


Questi metodi bloccano il programma fino alla loro conclusione (quindi la riga di codice successiva non viene eseguita fino al completamento dell'operazione).


Ecco un esempio di lettura sincrona di un file:


```javascript
const fs = require("fs")

const data = fs.readFileSync("example.txt", "utf8")

console.log(data)
```


Se esiste un file chiamato `example.txt` nella stessa directory dello script, questo stamperà il suo contenuto.


È anche possibile scrivere su un file in modo sincrono:


```javascript
const fs = require("fs")

fs.writeFileSync("output.txt", "Hello from Node!")

console.log("File written!")
```


Questo crea (o sovrascrive) un file chiamato `output.txt` con il testo.


Ecco alcune operazioni comuni che si possono fare con questa API:


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


L'API Sync è semplice e va bene per piccoli script, ma poiché blocca il programma finché non ha finito, può rallentare le cose se si lavora con file di grandi dimensioni o con un server.


### API asincrona di callback


L'API **callback** non è bloccante: consente a NodeJS di continuare a fare altre cose mentre avviene l'operazione sul file.


Invece di restituire direttamente il risultato, prende una funzione (un **callback**) che viene chiamata quando l'operazione è terminata.


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


Ecco cosa succede:



- `fs.readFile` inizia a leggere `esempio.txt`.
- NodeJS non aspetta, passa all'esecuzione di altro codice che potreste aver scritto.
- Quando il file viene letto, viene eseguito il callback:



  - Se c'è stato un errore, `err` contiene l'errore.
  - Altrimenti, `data` contiene il contenuto.


Ecco come si scrive su un file:


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


Stessa idea: il programma non si ferma durante la scrittura del file.


Alcuni esempi di cose che si possono fare con questa API:


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


L'API di callback è migliore per i server e per le attività di grandi dimensioni, perché non blocca il programma, ma i callback annidati possono diventare disordinati se si concatenano molte operazioni. Per questo motivo è stata aggiunta un'API asincrona basata su promesse.


### API asincrona Promise


L'API basata sulle promesse è moderna e funziona benissimo con `.then()` e `async/await`. È disponibile come `fs.promises`.


È necessario importare la proprietà `promises`:


```javascript
const fs = require("fs").promises
```


Utilizzando `.then()`:


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


O ancora meglio, utilizzando `async/await`:


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


Scrivere su un file:


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


Il solito elenco di esempi per l'API:


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


Quando si scrive codice, spesso è necessario utilizzare codice scritto da altre persone; ad esempio, librerie che aiutano a lavorare con date, colori, server o qualsiasi altra cosa.


Invece di scaricare e copiare i file manualmente, è possibile utilizzare un **gestore di pacchetti**.


Un gestore di pacchetti è uno strumento che:



- pacchetti di download
- tiene traccia dei pacchetti di cui il progetto ha bisogno
- si assicura che tutti i membri del team abbiano le stesse versioni dei pacchetti


### Che cos'è l'NPM


Nel mondo NodeJS, il gestore di pacchetti più popolare è **NPM**, che sta per *Node Package Manager*.


NPM si ottiene automaticamente quando si installa NodeJS.


È possibile verificare se si dispone di NPM eseguendo questo comando nel terminale:


```
npm -v
```


Stampa la versione di NPM che si possiede, ad esempio:


```
10.2.1
```


### Creazione di un pacchetto


In NodeJS, un **pacchetto** è solo una cartella con un file `package.json` al suo interno.


Creiamone uno passo dopo passo.


1. Creare una nuova cartella per il progetto:


```
mkdir my_project
cd my_project
```


2. Eseguite questo comando:


```
npm init
```


Si avvia una configurazione interattiva, con domande come il nome del progetto, la versione, la descrizione, ecc.


Se non si vuole rispondere a tutto e ci si limita ad accettare le impostazioni predefinite, si può usare:


```
npm init -y
```


Dopo averla eseguita, nella cartella verrà visualizzato un nuovo file chiamato:


```
package.json
```


### `package.json`


Il file `package.json` è solo un file JSON che memorizza i metadati del progetto.


Ecco un esempio:


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


Alcuni campi importanti:



- `nome`: il nome del pacchetto
- `version`: la versione corrente
- `main`: il file di ingresso (come `index.js`)
- `scripts`: comandi che si possono eseguire (come `npm start`)
- `dependencies`: elenca tutti i pacchetti da cui il progetto dipende


### Installazione di un pacchetto


Supponiamo di voler usare un certo pacchetto chiamato `picocolors' per aggiungere colori all'output del terminale.


È possibile installarlo eseguendo:


```
npm install picocolors
```


Ora è possibile utilizzarlo nel proprio progetto. Creare un file `index.js` con


```javascript
const pico = require('picocolors')

console.log(
pico.green("This text is green!")
)
```


e provare a eseguirlo. Il terminale dovrebbe stampare una versione colorata del testo.


Cosa ha fatto NPM?



- Ha scaricato il pacchetto e lo ha memorizzato in una sottocartella chiamata `node_modules/`
- ha aggiunto una voce sotto `dependencies` nel file `package.json`
- ha aggiornato il file `package-lock.json


Cos'è `package-lock.json`?


### `package-lock.json


Questo file viene creato automaticamente da NPM.


Ci si potrebbe chiedere: se abbiamo già `package.json`, perché abbiamo bisogno di un altro file?

Ecco il motivo:



- `package.json` dice solo di quale versione **gamma** di un pacchetto ha bisogno il progetto.

Esempio:


```json
"dependencies": {
"picocolors": "^1.1.0"
}
```


`^1.1.0` significa "qualsiasi versione compatibile con 1.1.x", quindi è flessibile.



- `package-lock.json` **congela** le versioni esatte di ogni singolo pacchetto e delle sue sottodipendenze, in modo che chiunque installi il vostro progetto abbia la stessa configurazione di lavoro.


Perché è importante?


Se lavorate in un team, se distribuite il vostro progetto su un server o se ci tornate in futuro, volete essere sicuri che funzioni ancora allo stesso modo.

Se i pacchetti sono stati aggiornati e si reinstalla senza un file di blocco, si potrebbe ottenere una versione leggermente diversa che si comporta in modo diverso.


Mantenendo il file `package-lock.json` nel progetto, NPM installerà sempre le versioni esatte elencate, assicurando che tutti abbiano lo stesso ambiente.


`package-lock.json` blocca tutto a una versione molto specifica, per rendere il progetto più riproducibile su altre macchine.


Ma se il pacchetto deve essere usato da molte persone, si può scegliere di non fare il commit, in modo che NPM trovi solo il file `package.json` e possa installare automaticamente le ultime versioni consentite in quel file.


Ma queste sono cose di cui ci si dovrà preoccupare più avanti, quando si inizierà a pubblicare il proprio codice. Per ora, abbiamo introdotto le basi di NPM solo per permettervi di trovare e utilizzare le librerie pubblicate da altri sviluppatori nei vostri progetti.



## Collegamento in rete in NodeJS

<chapterId>f2cabd8b-754b-5c97-8d6a-8412a9a184c7</chapterId>


NodeJS è spesso utilizzato come linguaggio per il backend: è possibile trasformare il proprio script in un server e utilizzarlo per effettuare richieste ad altri server.


In questo capitolo introdurremo alcune funzioni di rete di base che vi permetteranno di farlo.


### `fetch()`


Se si desidera che il programma scarichi dati da un sito web o da un'API, è necessario effettuare una richiesta **HTTP**.


Nelle versioni moderne di NodeJS, è possibile utilizzare la funzione integrata `fetch()`.


Ecco un esempio di richiesta GET a un'API:


```javascript
const response = await fetch("https://jsonplaceholder.typicode.com/posts/1")
const data = await response.text()

console.log(data)
```


Quando lo si esegue, si vedrà qualcosa di simile:


```
{
"userId": 1,
"id": 1,
"title": "...",
"body": "..."
}
```


Ecco cosa succede:


1. `fetch()` prende un URL ed effettua una richiesta.

2. Restituisce una **Promessa** che si risolve in un oggetto `Response`.

3. `response.text()` legge il corpo della risposta come una stringa.


Ma la stringa che si ottiene è in realtà JSON. Che cos'è?


### JSON


Quando si lavora con le API web, i dati vengono spesso inviati e ricevuti come **JSON**, acronimo di JavaScript Object Notation.


JSON è solo un formato di testo che assomiglia molto agli oggetti JavaScript. Ad esempio:


```json
{
"name": "Alice",
"age": 30,
"likes": ["apples", "bananas"]
}
```


L'oggetto `JSON` è un'utilità integrata in JavaScript che può essere utilizzata per lavorare con questo formato di dati.


È possibile convertire un oggetto JavaScript in una stringa JSON utilizzando `JSON.stringify()`:


```javascript
const user = { name: "Alice", age: 30 }

const jsonString = JSON.stringify(user)

console.log(jsonString)
```


Questa stampa:


```
{"name":"Alice","age":30}
```


È anche possibile convertire il testo JSON in un oggetto JavaScript usando `JSON.parse()`:


```javascript
const jsonText = '{"name":"Bob","age":25}'

const obj = JSON.parse(jsonText)

console.log(obj)
```


Questa stampa:


```
{ name: 'Bob', age: 25 }
```


Attenzione: `JSON.parse()` lancia un errore se la stringa non è JSON valida.


```javascript
JSON.parse("not json") // ❌ Error!
```


Assicuratevi quindi che la stringa sia formattata correttamente.


### server `http


NodeJS consente di creare un server web senza installare nient'altro.


Si può usare il modulo integrato `http` per gestire le richieste dei client e inviare le risposte.


Ecco un esempio molto elementare:


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


Quando si esegue questo script e si apre `http://localhost:3000` nel browser, si vedrà:


```
Hello from NodeJS server!
```


Ecco cosa succede nel codice:


1. È stato importato il server `http` dalla libreria standard di Node.

2. `http.createServer()` crea un server. Si è passato a `http.createServer()` un callback `(req, res) => {...}` da eseguire ogni volta che qualcuno si connette.

3. Alla risposta è stato assegnato un codice di stato 200 (che indica un'operazione riuscita). È possibile leggere i codici di stato http [qui](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

3. `res.end()` invia la risposta e termina la connessione.

4. `server.listen(3000)` avvia il server sulla porta 3000.


Si può anche controllare `req.url` e `req.method` nella richiesta per gestire percorsi o tipi di richiesta diversi.


Esempio di instradamento:


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


Questi sono esempi molto semplici. Per costruire server più avanzati, la maggior parte degli sviluppatori probabilmente scaricherà una libreria di backend già pronta, come [express](https://www.npmjs.com/package/express).


## Elaborazione dei dati: buffer, eventi, flussi

<chapterId>8c9623f0-a604-51a4-8fe4-871c849d3e3b</chapterId>


In questo capitolo verranno introdotte principalmente tre classi di oggetti:



- `Buffer`, che rappresenta piccoli pezzi di dati binari
- `EventEmitter`, che può essere usato per tracciare un processo asincrono di qualche passo, emettendo segnali chiamati "eventi"
- `Stream`, che ci permette di elaborare grandi porzioni di dati un `Buffer` alla volta e che tiene traccia del processo emettendo eventi


Sono estremamente comuni nel codice NodeJS professionale, quindi anche se non li userete nei vostri primi progetti, è bene avere una conoscenza di base per capire quando dovrete interagire con loro. di loro


### Buffer


In NodeJS, un **buffer** è un tipo di oggetto utilizzato per lavorare con i dati binari.


Si può pensare a un buffer come a un contenitore di dimensioni fisse per i byte grezzi.


Ecco come creare un buffer da una stringa:


```javascript
const buf = Buffer.from("hello")
console.log(buf)
```


Viene stampato qualcosa come:


```
<Buffer 68 65 6c 6c 6f>
```


Questi numeri (`68`, `65`, `6c`, ecc.) sono rappresentazioni esadecimali delle lettere di `"ciao"`.


È possibile convertirlo in una stringa in questo modo:


```javascript
console.log(buf.toString())
```


Questa stampa:


```
hello
```


È anche possibile creare un buffer di una certa dimensione riempito di zeri:


```javascript
const buf = Buffer.alloc(10)
console.log(buf)
```


Viene stampato qualcosa come:


```
<Buffer 00 00 00 00 00 00 00 00 00 00>
```


È possibile scrivere nel buffer:


```javascript
buf.write("abc")
console.log(buf)
```


E si può accedere ai singoli byte:


```javascript
console.log(buf[0]) // prints the ASCII number for 'a', which is 97
```


I buffer sono particolarmente utili quando è necessario manipolare i dati a un livello molto basso.


### Eventi


In JavaScript, un **evento** è qualcosa che accade nel programma e a cui si può reagire.


Ad esempio:



- un file finisce di essere caricato
- un timer scatta
- un utente fa clic su un pulsante
- una richiesta di rete restituisce i dati


Un **evento** è solo un segnale che indica che è successo qualcosa e si può scrivere del codice per ascoltare questi eventi e reagire ad essi.


In NodeJS, molti oggetti possono emettere eventi. Questi oggetti sono chiamati **EventEmitters**.


Ecco un esempio:


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


Questa stampa:


```
Hello! An event happened.
```


Ecco cosa:


1. Creiamo un oggetto `EventEmitter`.

2. Gli diciamo di eseguire un callback ogni volta che si verifica l'evento `"greet", usando `.on("greet")`.

3. In seguito, si attiva l'evento `"greet" utilizzando `.emit()`.

4. Il nostro callback viene eseguito


È possibile passare i dati insieme all'evento:


```javascript
emitter.on("greet",
(name) => console.log(`Hello, ${name}!`)
)

emitter.emit("greet", "Alice") // first argument is the type of event, second argument is the data we pass with this event
```


Questa stampa:


```
Hello, Alice!
```


È possibile registrare ascoltatori anche per altri eventi:


```javascript
emitter.on("goodbye", () => {
console.log("Goodbye!")
})

emitter.emit("goodbye")
```


Si possono collegare tutti gli ascoltatori che si desidera a un tipo di evento e si possono lanciare diversi tipi di eventi dallo stesso emettitore.


Molti oggetti in NodeJS emettono eventi per comunicare al resto del programma che sta accadendo qualcosa.



### Cosa sono i flussi?


Gli stream combinano buffer ed eventi per aiutarci a elaborare i dati.


Quando lavoriamo con file, dati provenienti dalla rete o anche testi lunghi, non sempre abbiamo bisogno (o vogliamo) caricare tutto in una volta nella memoria. Questo potrebbe essere lento o addirittura bloccare il programma se i dati sono troppo grandi.


Invece, possiamo elaborare i dati **poco alla volta**, man mano che arrivano o vengono letti, un po' come bere acqua con una cannuccia invece di cercare di bere tutto il bicchiere in una volta. Questo si chiama **flusso**.


In NodeJS, uno stream è un oggetto che consente di leggere dati da una sorgente o di scrivere dati su una destinazione **un pezzo alla volta**.


NodeJS ha quattro tipi principali di flussi:



- Readable**: flussi da cui è possibile leggere i dati (come la lettura di un file)
- Writable**: flussi su cui è possibile scrivere dati (come la scrittura su un file)
- Duplex**: flussi che sono sia leggibili che scrivibili
- Transform**: come i flussi duplex, ma possono modificare (trasformare) i dati durante il flusso


### Flussi leggibili


Supponiamo di avere un `bigfile.txt` da elaborare. Si può creare un flusso leggibile con il modulo `fs` per leggere il file pezzo per pezzo.


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


Cosa succede qui?


1. `fs.createReadStream()` crea un flusso leggibile.

2. Ogni volta che una parte del file è pronta, lo stream emette un evento `data` e ci fornisce un "pezzo" di dati (un `Buffer`). Stampiamo il pezzo.

3. Quando l'intero file è stato letto, viene attivato l'evento `end`.

4. Se c'è un errore (ad esempio, il file non esiste), viene attivato l'evento `error`.


In questo modo è possibile leggere file giganteschi senza caricarli tutti in memoria in una sola volta.


Se si vuole che i dati arrivino in forma leggibile (anziché binaria), si può specificare la codifica del flusso:


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


Il codice ora stamperà il file in forma leggibile.


### Flussi scrivibili


Un flusso scrivibile consente di inviare i dati da qualche parte, pezzo per pezzo.


Ecco un esempio di scrittura su un file `target.txt` utilizzando un flusso:


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


Ecco cosa succede:


1. `fs.createWriteStream()` crea un flusso scrivibile.

2. Scriviamo del testo su di esso usando `.write()`.

3. Quando abbiamo finito, chiamiamo `.end()` per chiudere lo stream.

4. Quando tutti i dati sono stati scritti, viene emesso l'evento `finish`.

5. Se qualcosa va storto, viene attivato l'evento `error`.


Proprio come gli stream leggibili, gli stream scrivibili sono ottimi per i grandi dati, perché non hanno bisogno di tenere tutto in memoria contemporaneamente.


### Flussi di tubazioni


Una delle cose più interessanti dei flussi è che è possibile collegarli insieme: collegare un flusso leggibile direttamente a un flusso scrivibile.


```javascript
const fs = require("fs")

const readable = fs.createReadStream("bigfile.txt")
const writable = fs.createWriteStream("target.txt")

readable.pipe(writable)
```


Qui:



- Il flusso leggibile legge da `bigfile.txt`.
- Il flusso scrivibile scrive su `copy.txt`.
- `.pipe()` invia i dati direttamente dal flusso leggibile a quello scrivibile.


### Flussi duplex


Un flusso duplex è sia leggibile che scrivibile. Un esempio è un socket di rete: si possono inviare dati ad esso e riceverne da esso.


Ecco un esempio molto semplice che utilizza il modulo `net`:


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


In questo esempio:



- L'oggetto `socket` è un flusso duplex.
- È possibile `scrivere()` su di esso e anche ascoltare gli eventi `data` da esso.


### Trasformare i flussi


Un flusso di trasformazione è un flusso duplex che modifica anche i dati che lo attraversano.


Ad esempio, è possibile utilizzare il modulo integrato `zlib` per comprimere o decomprimere i dati.


Ecco come comprimere un file utilizzando un flusso di trasformazione:


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


E per decomprimerlo di nuovo:


```javascript
const readable = fs.createReadStream("bigfile.txt.gz")
const unzip = zlib.createGunzip()
const writable = fs.createWriteStream("bigfile.txt")

readable.pipe(unzip).pipe(writable)

writable.on("finish", () => {
console.log("File decompressed.")
})
```


I flussi di trasformazione sono molto utili per operazioni come la compressione, la crittografia o la modifica dei formati dei file durante lo streaming.


### Retropressione


A volte un flusso scrivibile è lento nel gestire i dati. Se si continua a inviare dati a un flusso scrivibile più velocemente di quanto possa gestire, si potrebbero verificare dei problemi. Questo fenomeno è chiamato **pressione di ritorno**.


Se si chiama il metodo `.write()` su un flusso scrivibile, esso restituisce un booleano che informa se il flusso ha bisogno di una pausa; potrebbe essere necessario controllare il suo valore di ritorno, come in questo caso:


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


Si trattava di un esempio illustrativo di convogliamento manuale dei dati da un Readable a un Writable e di gestione manuale della contropressione.


Di solito si inviano i dati con il metodo `.pipe()`, che gestisce automaticamente la contropressione.


Quindi ci si deve preoccupare della contropressione solo quando, per qualche motivo, si chiama manualmente `.write()`.


## Nota finale

<chapterId>139e2ab8-df67-525a-85f0-5a2fa5e478f2</chapterId>


Se avete seguito le lezioni, dovreste essere in grado di scrivere alcuni semplici programmi in NodeJS.


Suggerisco di fare proprio questo: dopo aver imparato le basi, costruire alcuni progetti personali è il modo migliore per esercitarsi e diventare un programmatore migliore.


Non è importante cosa costruite, l'importante è che vi mettiate alla prova per risolvere i problemi con il codice.


I moderni linguaggi di programmazione sono incredibilmente potenti e NodeJS è probabilmente la migliore cassetta degli attrezzi con cui sperimentare in questa fase del vostro percorso.


Buona fortuna!


# Sezione finale


<partId>322624d8-6fbc-11f0-a67a-5b145f10afc1</partId>


## Recensioni e valutazioni


<chapterId>3e93ac86-6fbc-11f0-8bae-9b2ed7914843</chapterId>

<isCourseReview>true</isCourseReview>

## Conclusione


<chapterId>49b3b9b2-6fbc-11f0-9870-5f5adcd3a0eb</chapterId>


<isCourseConclusion>true</isCourseConclusion>