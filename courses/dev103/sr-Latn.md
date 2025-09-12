---
name: Osnove JavaScripta i NodeJS-a
goal: Naučite osnove programiranja u JavaScriptu i razvoj u NodeJS-u kako biste izgradili praktične aplikacije i alate.
objectives: 

  - Savladajte osnovnu sintaksu JavaScript-a, tipove i tok kontrole
  - Razumeti funkcije, objekte i klase u JavaScriptu
  - Naučite tehnike rukovanja greškama i otklanjanja grešaka
  - Upoznajte se sa NodeJS-om i njegovim ekosistemom

---

# Započni svoje razvojno putovanje


Dobrodošli na ovaj kurs o JavaScript-u i NodeJS-u.


JavaScript je najpopularniji programski jezik na svetu: to je skriptni jezik modernih pregledača, tako da je praktično nemoguće izgraditi modernu veb aplikaciju bez pisanja *nekog* JavaScripta; a sa NodeJS okruženjem može se koristiti i van pregledača, za kreiranje skripti i aplikacija koje se pokreću direktno na vašem računaru.


Ovaj kurs je dizajniran za ljude koji su potpuno novi u programiranju, ili koji su koristili druge jezike ranije, ali žele da razumeju kako JavaScript funkcioniše, posebno u kontekstu NodeJS-a.


Do kraja kursa, trebalo bi da budete u mogućnosti da pišete sopstvene programe u JavaScript-u, koristite standardnu biblioteku NodeJS-a i instalirate i koristite pakete trećih strana za izradu korisnih alata.


+++
# Osnovni JavaScript

<partId>a617327c-e5a2-52ca-9380-c63f44623dd4</partId>


## Postavljanje

<chapterId>ba05a290-1782-5268-87c9-62fd09590e05</chapterId>




JavaScript program je samo kolekcija (jedne ili više) tekstualnih datoteka, koje sadrže komande koje izvršava JavaScript okruženje za izvršavanje.


Nazivi ovih tekstualnih datoteka obično završavaju sa ekstenzijom `.js`, kao što su `my_script.js`, `my_program.js` itd.


Komande koje sadrže napisane su u programskom jeziku JavaScript.


JavaScript runtime je poseban program koji izvršava ove fajlove.


![](assets/en/1.webp)


### NodeJS okruženje za izvršavanje


Najčešći JavaScript runtime je NodeJS.


Vaše IDE ga možda već uključuje, ili ćete ga možda morati preuzeti sa [zvaničnog sajta](https://nodejs.org/en/download).


Stranica za preuzimanje će vam pružiti uputstva za sve tri glavne OS-ove (operativne sisteme): Windows, Linux i MacOS. Pretpostavlja se da znate kako otvoriti terminal u vašem OS-u.


Pošto je NodeJS dostupan za sve tri operativne sisteme, programi koje napišete moći će da se izvršavaju na svim njima (izuzev nekih specifičnih slučajeva).


To znači da možete, na primer, napisati jednostavnu video igru u JavaScript-u na vašem Windows računaru i proslediti je prijatelju da je pokrene na svom Mac-u.


![](assets/en/2.webp)














### Prvi program (zdravo svete)


Tradicionalno, kada se uči programski jezik, prvi program koji se napiše sastoji se u ispisivanju "hello world!" na konzolu.


Kreirajte direktorijum pod nazivom `my_js_code/`, sa fajlom unutra koji se zove `main.js` (ovi nazivi su proizvoljni).


Otvorite direktorijum pomoću vašeg uređivača koda.


Napiši ovaj kod u svoju datoteku:


```javascript
console.log("hello world!")
```


Otvorite terminal i izvršite ovu komandu da pokrenete program:


```
node main.js
```


Rezultat bi trebao biti


```
hello world!
```


### Šta se desilo


U JavaScriptu, sve je "objekat".


`console` je objekat, koji se koristi za debagovanje programa.


`console.log` je najčešće korišćena metoda `console`. Jednostavno ispisuje sve argumente koje prosledite.


Argumente prosleđujete u `console.log` koristeći okrugle zagrade `()`.


Dakle, na primer, ako želite da odštampate broj `1000`, jednostavno biste napisali


```javascript
console.log(1000)
```


Zatim ga izvršite pokretanjem


```
node main.js
```


u vašem terminalu (od sada, ovaj kurs će pretpostaviti da znate da je ovo način na koji izvršavate program).


Ovo bi trebalo da se ispiše


```
1000
```


Možete proći više stvari, kao


```javascript
console.log(16, 8, 1993)
```


Ovo će se ispisati


```
16 8 1993
```


## Varijable i komentari

<chapterId>23050ab7-343b-5edf-9d37-e4e782e27ce0</chapterId>


Programi obično izvršavaju operacije nad podacima.


Varijable su kao imenovane kutije koje koristimo za skladištenje podataka. Omogućavaju nam da povežemo deo podataka sa specifičnim imenom, tako da ga možemo kasnije dohvatiti koristeći to ime.


### Deklaracije `let`


Da bismo deklarisali promenljivu u JavaScript-u, možemo koristiti ključnu reč `let`.


Nakon što napišemo `let`, pišemo ime koje želimo dati promenljivoj, zatim znak `=`, i onda vrednost koju želimo da sačuvamo.


Na primer:


```javascript
let age = 25

console.log(age)
```


Ime promenljive (tehnički nazvano "identifikator") obično može sadržati slova, donje crte (`_`), znak dolara (`$`) i brojeve, iako prvi karakter ne može biti broj.


U gornjem kodu, deklarisali smo promenljivu pod nazivom `age` i u nju smo pohranili vrednost `25`.


Zatim smo odštampali vrednost koristeći `console.log(age)`.


Ako pokrenete ovaj kod sa `node main.js`, izlaz će biti:


```
25
```


Identifikatori su osetljivi na velika i mala slova, što znači da se velika i mala slova računaju kao razlike u identifikatorima, pa na primer


```javascript
let age = 25

let Age = 20

console.log(age)
```


će odštampati 25, jer se oni smatraju dvema potpuno odvojenim promenljivama!


Takođe možete čuvati stringove (tekst) u promenljivoj:


```javascript
let message = "hello again"

console.log(message)
```


Ovo će se ispisati:


```
hello again
```


Baš kao i ranije, koristili smo `console.log()` da ispišemo vrednost pohranjenu u promenljivoj.


Sada hajde da uradimo oboje zajedno:


```javascript
let age = 25

let message = "hello again"

console.log(age)

console.log(message)
```


Pokretanjem ovoga će se ispisati:


```
25
hello again
```

### Premeštaj


Promenljive deklarisane sa `let` mogu biti promenjene nakon što su kreirane.


Ovo se zove preraspodela.


```javascript
let score = 10

console.log(score)

score = 15

console.log(score)
```


Prvo, dodeljujemo `10` promenljivoj `score`, zatim je štampamo.


Zatim menjamo vrednost `score` na `15` i ponovo je štampamo.


Izlaz će biti:


```
10
15
```


Ovo je veoma korisno kada se vrednost menja tokom vremena, kao u igri gde se rezultat povećava.


Hajde da dodamo još jednu varijablu u mešavinu:


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


Ovo će se ispisati:


```
10
Alice
20
Bob
```


Kao što možete videti, i `score` i `player` su promenjeni.


### Deklaracije `const`


Većinu vremena, međutim, ne želimo da promenljiva menja vrednost nakon što je kreirana. Za to koristimo `const`.


`const` je skraćenica za „konstanta“. Kada jednom dodelite vrednost `const` varijabli, ne možete je promeniti.


```javascript
const pi = 3.14
console.log(pi)
```


Ovo štampa:


```
3.14
```


Ali ako pokušaš da uradiš ovo:


```javascript
const pi = 3.14
console.log(pi)

pi = 99 // this line will cause an error
console.log(pi)
```


JavaScript će vam dati grešku kao:


```
TypeError: Assignment to constant variable.
```


Ovo je zato što je `pi` deklarisan koristeći `const`, i ne možete promeniti njegovu vrednost nakon toga. Time komunicirate JavaScript interpreteru da ne želite da ta promenljiva bude promenjena.


Ovo je korisno jer smanjuje šanse da se promeni greškom. Kada programi postanu veoma veliki, sa hiljadama linija koda, nemoguće je pratiti sve što se dešava odjednom (to je glavni razlog zašto koristimo računare, da izvršavaju složene procese koje ne možemo izračunati našim mozgovima), tako da postaje korisno imati ovakva ograničenja, koja čine program determinističnijim.


Smatra se najboljom praksom da uvek deklarišemo naše vrednosti kao `const`, osim ako nismo sigurni da želimo da ih kasnije modifikujemo.


### Komentari u JavaScriptu


Ponekad želimo da pišemo beleške u našem kodu koje se ne izvršavaju. One se zovu komentari.


Komentari se ignorišu od strane programa kada se pokrene, ali su korisni za objašnjavanje stvari nama samima ili drugim ljudima.


Da biste napisali komentar u jednoj liniji, koristite `//`


```javascript
// This is a comment
const x = 10 // This is also a comment
console.log(x)
```


Ovo će se i dalje štampati:


```
10
```


Komentari su tu samo da ih ljudi čitaju.


Takođe možete pisati komentare u više linija koristeći `/*` i `*/`


```javascript
/*
This is a multi-line comment.
It can span several lines.
*/
const y = 20
console.log(y)
```


Ovo će se štampati


```
20
```


A komentar će biti ignorisan.


Možete koristiti komentare da dodate male napomene svom kodu, kako biste se mogli setiti šta on radi i zašto je napisan na određeni način. Takođe može pomoći drugim programerima da ga razumeju.


## Osnovni tipovi: brojevi, stringovi, booleanski tipovi

<chapterId>cfdb04f6-21a8-5143-bbf9-7aaae04962f0</chapterId>


U JavaScriptu, "tip" vam govori koje vrste podataka je neka vrednost.


Javascript ima nekoliko osnovnih tipova, i u ovom delu ćemo istražiti neke od njih.


### Brojevi i aritmetičke operacije


Prvi tip koji ćemo predstaviti je `number`.


Brojevi u JavaScriptu mogu biti celi brojevi (kao `5`) ili decimalni brojevi (kao `3.14`).


Možete raditi aritmetiku s njima: sabiranje, oduzimanje, množenje i deljenje.


Evo osnovnog primera:


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


Ovo će se ispisati:


```
15
5
50
2
```


Takođe možete koristiti zagrade `()` da kontrolišete redosled operacija:


```javascript
const result = (2 + 3) * 4
console.log(result)
```


Ovo štampa:


```
20
```


Bez zagrada, to bi bilo `2 + 3 * 4`, što je:


```javascript
const result = 2 + 3 * 4
console.log(result)
```


To bi štampalo:


```
14
```


Zato što se u regularnoj matematici množenje dešava pre sabiranja.


### Nizovi i interpolacija


Drugi tip u JavaScript-u koji ćemo predstaviti je `string`.


Stringovi su delovi teksta. Možete koristiti jednostruke navodnike `'...'` ili duple navodnike `"..."` da ih kreirate.


```javascript
const greeting = "hello"
const name = 'Bob'
console.log(greeting)
console.log(name)
```


Ovo štampa:


```
hello
Bob
```


Da biste kombinovali stringove, možete koristiti operator `+`:


```javascript
const greeting = "hello"
const space = " "
const name = "Bob"

const fullGreeting = greeting + space + name
console.log(fullGreeting)
```


Ovo će se ispisati:


```
hello Bob
```


Ali postoji lepši način za kombinovanje stringova koji se zove **interpolacija stringova**. Koristite obrnutu navodnicu da deklarisete string `` `...` `` i pišete promenljive koristeći `${...}` unutar stringa:


```javascript
const greeting = "hello"
const name = "Bob"

const fullGreeting = `${greeting} ${name}`
console.log(fullGreeting)
```


Ovo takođe štampa:


```
hello Bob
```


Možete uključiti bilo koji izraz unutar `${...}`:


```javascript
const age = 30
console.log(`Next year, I will be ${age + 1} years old.`)
```


Ovo štampa:


```
Next year, I will be 31 years old.
```


Interpolacija je veoma česta u modernom JavaScript-u.


### Buleani, poređenja i logičke operacije


Treći tip koji ćemo predstaviti je `boolean`. Ime je dobio po matematičaru Džordžu Bulu, koji je izumeo bulovu logiku.


Boolovi su jednostavni: samo dve moguće vrednosti, `true` i `false`.


Možete ih sačuvati u promenljivama:


```javascript
const theSkyIsBlue = true
const thisCourseIsBad = false

console.log(theSkyIsBlue)
console.log(thisCourseIsBad)
```


Ovo štampa:


```
true
false
```


Možete kombinovati booleove vrednosti koristeći logičke operatore:



- `&&` znači “i”, i vratiće `true` samo ako su **obe** vrednosti `true`, u suprotnom će vratiti `false`.
- `||` znači „ili“, i vratiće `true` ako je **bar jedna** od vrednosti `true`, u suprotnom (ako su obe false) vratiće `false`
- `!` znači „ne“, primenjuje se pre booleana i preokrenuće ga: ako je boolean `true` vratiće `false`, i obrnuto.


![](assets/en/3.webp)


Primeri:


```javascript
const isSunny = true
const isWarm = true

console.log(isSunny && isWarm)  // true
console.log(isSunny || isWarm)  // true
console.log(!isSunny)           // false
```


Možete upoređivati vrednosti u JavaScript-u koristeći operatore kao što su `>`, `<`, `===` i `!==`. Rezultat ovih poređenja je uvek boolean.


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


Javascript takođe ima `>=` što znači "veće ili jednako" i `<=` što znači "manje ili jednako".


Booleovi, operatori poređenja i logički operatori se često kombinuju u programima kako bi se deklarisali složeni uslovi, kao na primer da se osigura "da je email stigao I da sadrži sliku koja mi je potrebna ILI da je dužina emaila veća od 10000 karaktera". Kasnije ćete otkriti da su ovo osnovni gradivni elementi za konstruisanje logike programa.


## Nizovi, null, undefined

<chapterId>7bf18183-5eae-53ed-83d2-b04982145d81</chapterId>


U ovom odeljku ćemo pokriti još tri tipa koja su veoma česta u JavaScript programima:



- Nizovi**: sekvence vrednosti
- nedefinisano**: posebna vrednost koja znači „ništa nije dodeljeno“
- null**: još jedna posebna vrednost koja znači „namerno prazno“


### Nizovi i pristup indeksima


**Niz** je tip koji može da sadrži više vrednosti u listi.


Napravite niz koristeći uglaste zagrade `[]` i razdvajajući stavke zarezima.


Evo osnovnog primera:


```javascript
const numbers = [10, 2, 88]
console.log(numbers)
```


Ovo štampa:


```
[ 10, 2, 88 ]
```


U nizu možete čuvati bilo šta, ne samo brojeve:


```javascript
const things = ["apple", 42, true]
console.log(things)
```


Ovo štampa:


```
[ 'apple', 42, true ]
```


Da bismo pristupili određenom elementu u nizu, koristimo **indeks**. Indeks je pozicija elementa, počevši od **0**.


Dakle u ovom nizu:


```javascript
const colors = ["red", "green", "blue"]
```



- `colors[0]` je `"red"`
- `colors[1]` je `"Green"`
- `colors[2]` je `"blue"`


Hajde da probamo:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[0])
console.log(colors[1])
console.log(colors[2])
```


Ovo će se ispisati:


```
red
green
blue
```


Možete dodeliti vrednost određenom indeksu niza


```javascript
const colors = ["red", "green", "blue"]

colors[1] = "yellow"

console.log(colors)
```


Ovo će se ispisati:


```
[ 'red', 'yellow', 'blue' ]
```


Možete koristiti bilo koji prirodan broj kao indeks, čak i onaj koji je sačuvan u promenljivoj.


```javascript

const i = 1
const colors = ["red", "green", "blue"]
console.log(colors[i])
```


Ovo će se ispisati:


```
green
```


Ali ako pokušate da pristupite indeksu koji ne postoji, dobićete `undefined`:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[3])
```


Ovo štampa:


```
undefined
```


Šta je to??


### `nedefinisano`


Posebna vrednost `undefined` znači „nijedna vrednost nije dodeljena”.


Ako kreirate promenljivu, ali joj ne dodelite vrednost, biće `undefined`:


```javascript
const name
console.log(name)
```


Ovo štampa:


```
undefined
```


Zato što nismo dodelili ništa `name`, JavaScript ga postavlja na `undefined` po defaultu.


Kao što je ranije viđeno, možete dobiti i `undefined` kada pristupite indeksu niza koji ne postoji:


```javascript
const fruits = ["banana", "apple"]
console.log(fruits[2]) // There is no index 2
```


Ovo štampa:


```
undefined
```


### `null` i kako ga tretirati


`null` je takođe posebna vrednost. Znači „ovde nema ničega, i to sam uradio namerno.”


Za razliku od `undefined`, koji je automatski, `null` je nešto što sami postavljate.


Na primer:


```javascript
const currentUser = null
console.log(currentUser)
```


Ovo štampa:


```
null
```


Zašto koristiti `null`? Možda očekujete vrednost kasnije, ali još nije spremna:


```javascript
let winner = null

// Later in the program:
winner = "Alice"

console.log(winner)
```


Ovo štampa:


```
Alice
```


Dakle, `null` je koristan kada želite reći, na primer, „Ovde bi trebalo da bude nešto kasnije, ali trenutno je prazno.”


## Blokovi i tok kontrole

<chapterId>be985168-2636-5b0d-a48f-ac1bbfbff8a7</chapterId>


Do sada smo uglavnom pisali linije koda koje se izvršavaju jedna za drugom.


Ali kada kodiramo, možemo kontrolisati redosled izvršavanja toga.


Ovo se zove **kontrola toka**.


Hajde da počnemo sa razumevanjem blokova i opsega.


### Globalni opseg


Svaka promenljiva koju deklarišemo postoji u **opsegu**, što znači oblast koda gde je promenljiva poznata.


Ako deklarirate promenljivu izvan bilo kog bloka, ona postoji u **globalnom opsegu**.


```javascript
const color = "blue"
console.log(color)
```


Ova promenljiva `color` je u globalnom opsegu, tako da joj se može pristupiti sa bilo kog mesta u fajlu.


Ako dodate više redova:


```javascript
const color = "blue"
console.log(color)

const size = "large"
console.log(color)
console.log(size)
```


I `color` i `size` su globalne promenljive. One su dostupne svuda u fajlu.


Ali šta se dešava unutar bloka?


### Blokovi i lokalni opseg


**Blok** je deo koda okružen vitičastim zagradama `{}`.


Promenljive deklarisane sa `let` ili `const` unutar bloka postoje **samo** unutar tog bloka.


```javascript
{
const message = "inside block"
console.log(message)
}
```


Ovo štampa:


```
inside block
```


Ali ako pokušaš ovo:


```javascript
{
const message = "inside block"
}
console.log(message) // Error!
```


JavaScript će vam dati grešku kao:


```
ReferenceError: message is not defined
```


To je zato što je `message` deklarisan unutar bloka i ne postoji izvan njega.


To znači da možemo koristiti blokove da izolujemo delove našeg koda, i biti sigurni da "ono što se dešava u bloku ostaje u bloku" (kao u Las Vegasu).


Organizovanje našeg koda u blokove nam takođe omogućava da strukturiramo izvršavanje programa, sa konstrukcijama kontrolnog toka kao što je `if`


### `if`, `else`


Ponekad želimo da pokrenemo kod **samo ako** je nešto tačno. Za to služi `if` naredba.


```javascript
const myAge = 20

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Ovo štampa:


```
Am I an adult?
Yes I am!
```


Kao što možeš videti, kod poredi `myAge` i `18`.

U ovom slučaju operator `>=` vraća `true`, tako da se blok izvršava.

Ako uslov nije `true`, blok se ne izvršava.


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Ovo štampa:


```
Am I an adult?
```


Možete dodati `else` blok da obradite suprotan slučaj:


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
} else {
console.log("No, I am not.")
}
```


Ovo štampa:


```
Am I an adult?
No, I am not.
```


I `if` i `else` blokovi su i dalje blokovi - tako da promenljive deklarisane unutar njih ne postoje izvan.


Ako želimo biti sigurni da nešto **nije** tačno, šta možemo učiniti?


Pa, kao što je ranije diskutovano, JavaScript ima operator "not", koji preokreće booleove vrednosti. Tako da možemo uraditi


```javascript
const myAge = 17

const adult = myAge >= 18

console.log("Am I an adult?")

if (!adult) {
console.log("No, I am not.")
}
```

Ovo i dalje štampa:


```
Am I an adult?
No, I am not.
```

Zato što smo koristili operator `!` da invertujemo promenljivu `adult`.


`if (!adult) {...}` treba čitati kao "ako nije odrasla osoba..."


Korišćenjem blokova, logičkih i operatora poređenja, možemo strukturirati izvršavanje programa, definišući promenljive koje moraju biti `true` (ili `false`) da bi se nešto dogodilo.


### `while`, `break`, `continue`


`while` petlja ponavlja kod *sve dok* je uslov tačan.


```javascript
let count = 0

while (count < 3) {
console.log("Count is", count)
count = count + 1
}
console.log("the loop is over!")
```


Ovo štampa:


```
Count is 0
Count is 1
Count is 2
the loop is over!
```


Kada `count` postane 3, petlja se zaustavlja.


Petlju možete prekinuti ranije koristeći `break`:


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


Ovo štampa:


```
0
1
2
```


Jer kada broj postane `3`, `if` blok se izvršava i zaustavlja petlju.


Možete preskočiti ostatak petlje koristeći `continue`:


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


Ovo štampa:


```
1
2
4
5
```


Zato što kada je broj bio `3`, `continue` je naterao program da preskoči liniju koja štampa broj.


### `for ... of ...`


Ako imate niz i želite da uradite nešto sa svakom stavkom u njemu, možete koristiti `for ... of ... {...}`.


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const fruit of fruits) {
console.log(fruit)
}
```


Ovo štampa:


```
apple
banana
cherry
```

Blok će biti izvršen jednom za svaki element niza.


`fruit` ovde je nova promenljiva koja uzima vrednost svake stavke u nizu, kako bi se njome upravljalo unutar bloka.


### `for ... in ...`


Možete koristiti `for ... in` za iteraciju preko ključeva (indeksa) niza:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(index)
}
```


Ovo štampa:


```
0
1
2
```


Možete koristiti indeks da biste dobili i vrednost:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(fruits[index])
}
```


Ovo ispisuje isto kao `for ... of`:


```
apple
banana
cherry
```


U praksi, za nizove, trebalo bi da preferirate korišćenje `for ... of`, jer je jednostavnije i čistije.


### Ograničene petlje


Ponekad želimo da ponovimo određeni broj puta, ili uopšteno da napišemo deo koda koji ponavlja blok dok pratimo nešto.

To je ono za šta je ograničena petlja `for` dobra.

Ograničena petlja obično uzima tri uslova, odvojena tačkom i zarezom `;`, kao u `(... ; ... ; ....)`.


```javascript
for (let i = 0; i < 3; i = i + 1) {
console.log(i)
}
```


Ovo štampa:


```
0
1
2
```


Hajde da objasnimo:



- `let i = 0`: deklariše promenljivu koja će se koristiti u bloku (u ovom slučaju to je brojač koji počinje od 0)
- `i < 3`: proglašava uslov kao `tačan` da bi se blok izvršio (u ovom slučaju je "ponavljaj dok je `i` manje od 3")
- `i = i + 1`: deklarisati neki kod koji će se izvršiti nakon svake izvršene blok (u ovom slučaju "povećati `i` za 1")


Kao što možete videti, ograničena petlja nam omogućava da deklariramo složenije uslove za ponovljeno izvršavanje dela koda, ali većinu vremena to nije neophodno.


### Oznake blokova


Ako morate napisati složeniji tok kontrole, JavaScript vam omogućava da imenujete blok koristeći **oznaku** koja se može koristiti sa `break` ili `continue` za specificiranje *gde* da se vrati.


Primer:


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


Ovo štampa:


```
Inside outer block
Inside inner block
Done
```


Koristili smo `break outer` da potpuno izađemo iz bloka `outer`.


Možete takođe označiti petlje. Hajde da uzmemo ovaj primer:


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

Ovo je bio veoma dosadan primer, ali se nadam da je razjasnio (povremenu) potrebu za oznakama.


## Uvođenje funkcija

<chapterId>cc324715-09c2-5cf7-9e6f-47a6f16bc04d</chapterId>


Kako vaši programi rastu, često ćete želeti da **ponovo koristite** delove koda.


To su **funkcije**: omogućavaju vam da grupišete neki kod zajedno, date mu ime i pokrenete ga kad god želite.


### Deklaracija funkcije


Da bismo deklarisali funkciju, možemo koristiti ključnu reč `function`. Zatim joj dajemo ime, par zagrada `()` sa argumentima koje prima, i blok koda `{}` koji će biti izvršen. Počnimo sa funkcijom koja ne prima argumente:


```javascript
function sayHello () {console.log(`Hello!`) }
```


Ovaj kod **deklarira** funkciju, ali je **još** ne pokreće.


### Pozivi funkcija


Da biste pokrenuli (ili "pozvali") funkciju, napišite njeno ime praćeno zagradama:


```javascript
function sayHello () {console.log(`Hello!`) }
sayHello()
```


Ovo štampa:


```
Hello!
```


Možete pozvati funkciju koliko god puta želite:


```javascript
function sayHello() {
console.log("Hello!")
}

sayHello()
sayHello()
```


Ovo štampa:


```
Hello!
Hello!
```


Kod unutar funkcije se izvršava samo kada je pozovete.


### Argumenti funkcije (ulaz u funkcije)


Ponekad želite da funkcija radi sa nekim unosom. To možete postići dodavanjem **argumenata** unutar zagrada.


Na primer:


```javascript
function sayHelloTo (friend) {
console.log(`Hello ${friend}!`)
}
```


Sada ova funkcija uzima **jedan argument** nazvan `friend`.


Kada pozovete funkciju, možete proslediti vrednost:


```javascript
sayHelloTo("Tommy")
```


Ovo štampa:


```
Hello Tommy!
```


Možete ponovo pozvati funkciju sa drugim imenom:


```javascript
sayHelloTo("Sam")
```


Ovo štampa:


```
Hello Sam!
```


Vrednost koju prosledite zamenjuje promenljivu `friend` unutar funkcije.


Takođe možete koristiti više od jednog argumenta:


```javascript
function greetTwoPeople(person1, person2) {
console.log(`Hello ${person1} and ${person2}!`)
}

greetTwoPeople("Lina", "Marco")
```


Ovo štampa:


```
Hello Lina and Marco!
```


### `return` (izlaz iz funkcija)


Funkcije takođe mogu **vraćati** vrednosti. To znači da šalju vrednost nazad tamo gde je funkcija pozvana.


Evo jednostavan primer:


```javascript
function getNumber() {
return 42
}

const result = getNumber()
console.log(result)
```


Ovo štampa:


```
42
```


Funkcija `getNumber()` vraća `42`, i mi je čuvamo u `result`, zatim je ispisujemo.


Takođe možete vratiti nešto što izračunate:


```javascript
function add(a, b) {
return a + b
}

const result = add(2, 3)
console.log(result)
```


Ovo štampa:


```
5
```


Jednom kada je vrednost `return`ovana, funkcija se zaustavlja. Sve nakon `return` u tom bloku se ne izvršava.


```javascript
function saySomething() {

return "hi"

console.log("this never runs")

}

const message = saySomething()
console.log(message)
```


Ovo štampa samo:


```
hi
```


jer se samo `"hi"` vraća. Linija `console.log("this never runs")` se preskače.


Funkcije možete posmatrati kao male podprograme. Svaka funkcija može primiti neki ulaz, obraditi ga i vratiti vam neki izlaz.


Šta se dešava ako pokušamo da koristimo povratnu vrednost funkcije, ali ta funkcija nije vratila ništa?


```javascript
function doesNothing () {}

const x = doesNothing()

console.log(x)
```

Ovo će ispisati `undefined`. Povratna vrednost funkcije koja nije ništa vratila je `undefined`.


## Objekti i klase

<chapterId>26689f25-8212-5057-8c21-3a05eee0ac75</chapterId>


JavaScript se često naziva objektno orijentisanim jezikom.


To znači da vam pomaže da organizujete svoj kod grupisanjem vrednosti i funkcija zajedno u **objekte**.


### Šta je `object`?


Objekat može sadržati podatke i funkcije koje rade nad tim podacima. Kada se funkcija stavi u objekat kažemo da je to `metod`.


Prvi objekat koji smo videli bio je objekat `console`. To je objekat koji sadrži više metoda za ispisivanje stvari na ekranu i debagovanje naših programa.


Može čak i da se sam štampa; možete uraditi


```javascript
console.log(console)
```


i ispisaće listu metoda koje sadrži. Na primer, na mom računaru je ispisao


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


Kao što možete videti, ima mnogo metoda koje možete koristiti za debagovanje!


JavaScript nam pruža različite načine za kreiranje novih objekata koji mogu raditi šta god želimo.


### Kreiranje objekta


Najlakši način za kreiranje objekta je jednostavno grupisanje podataka i funkcija koristeći **vitičaste zagrade** `{}`.


Ovo stvara ono što zovemo **anonimni objekat**


```javascript
const cat = {
name: "Whiskers",
age: 3
}
```


Ovo kreira objekat i čuva ga u promenljivoj pod nazivom `cat`.


Objekat ima dva **svojstva**:



- `name` sa vrednošću `"Whiskers"`
- `age` sa vrednošću `3`


Hajde da ga odštampamo:


```javascript
console.log(cat)
```


Ovo štampa:


```
{ name: 'Whiskers', age: 3 }
```


Možete dobiti svojstva iz objekta koristeći tačku, kao u `objectName.propertyName`:


```javascript
console.log(cat.name)  // prints "Whiskers"
console.log(cat.age)   // prints 3
```


Takođe možete **promeniti** svojstvo:


```javascript
cat.age = 4
console.log(cat.age)  // now it prints 4
```


Kao što možete videti, čak i ako je objekat definisan kao `const`, i dalje možete izmeniti podatke koje sadrži.


U slučaju objekata, `const` će vas samo sprečiti da prepišete ceo objekat:


```javascript
const cat = {
name: "Whiskers",
age: 3
}

cat.age = 5 // this works

cat = 5 // this throws an error, you're trying to reassign the whole object

```


Kao što je ranije pomenuto, objekti mogu takođe sadržati **funkcije**, a kada je funkcija deo objekta, nazivamo je **metodom**.


Evo primer:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log("Meow!")
}
}
```


Ovaj objekat ima:



- Svojstvo `name`
- Metoda `speak()`


Hajde da nazovemo metodu:


```javascript
cat.speak()
```


Štampa:


```
Meow!
```


Metode mogu koristiti podatke koje objekat sadrži putem ključne reči `this`.

`this` se odnosi na trenutni objekat. U ovom primeru, koristiće se za ispisivanje imena mačke:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log(`${this.name} says meow!`)
}
}

cat.speak()
```


Ovo štampa:


```
Whiskers says meow!
```


Reč `this` znači "ovaj objekat"...u ovom slučaju, objekat `cat`.



Ovakvi objekti su odlični kada želite nešto brzo i jednostavno. Ali ako treba da kreirate **mnogo objekata** sa istom strukturom, postoji bolji način, i tu na scenu stupaju **klase**.


### Klase i konstruktori


**Klasa** je kao nacrt. Ona govori JavaScriptu kako da kreira određenu vrstu objekta.


Klasa se definiše koristeći ključnu reč `class`, nakon koje sledi ime klase, a zatim blok sa vitičastim zagradama `{}`.


```javascript
class Dog {}
```


Klase obično počinju velikim slovom, po konvenciji.


Možete kreirati novi objekat klase koristeći `new`:


```javascript
const hachiko = new Dog()
```


Pokušajte da odštampate objekat:

```javascript
class Dog {}

const myDog = new Dog()

console.log(myDog)
```


Dobićeš


```
Dog {}
```


Kao što možete videti, klasa Dog je prazna, tako da je i objekat `myDog` prazan.


Možemo definisati koje osobine objekti Dog treba da sadrže dodavanjem `constructor`.


Konstruktor je posebna funkcija koja se pokreće kada kreirate (ili "konstruirate") novi objekat.


```javascript
class Dog {
constructor() { }
}
```


Želimo da svaki Pas ima ime, pa dodajemo `name` parametar funkciji:


```javascript
class Dog {
constructor(name) { }
}
```


A zatim koristimo `this` da bismo deklarisali da je `name` ime objekta `Dog` koji gradimo


```javascript
class Dog {
constructor(name) {
this.name = name
}}
```


Hajde da ga sada isprobamo:


```javascript
class Dog {
constructor(name) {
this.name = name
}
}

const myDog = new Dog("hachiko")

console.log(myDog)
```


Ovo ispisuje nešto poput:


```
Dog { name: 'hachiko' }
```


Kao što možete videti, metoda `constructor` uzima argumente koje prosleđujete klasi kada koristite `new Dog()`, i koristi ih za kreiranje objekta.


Hajde da to razložimo:



- `class Dog` definiše klasu Dog.
- `constructor(name)` postavlja objekat kada je kreiran.
- `this.name = name` čuva vrednost u novom objektu.
- `new Dog("hachiko")` kreira novi objekat iz klase, sa svojstvom `name` postavljenim na `"hachiko"`.


Sada da dodamo metodu našoj klasi:


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


Ovo će se ispisati


```javascript
hachiko says barf!
```


Ako isto uradimo za dve različite instance psa



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


mi dobijamo


```
hachiko says barf!
bobby says barf!
```


Metoda `speak()` koristi svojstvo `name` objekta `Dog` na kojem je pozvana.


Ovo je glavni razlog zašto klase postoje: omogućavaju nam da definišemo skup metoda koje rade na podacima, a zatim kreiramo više objekata koji dele isti "oblik" podataka.


Kada pozovemo metodu na jednom od ovih objekata, ona će raditi na podacima *koje taj specifični objekat* drži.


### Menjanje oblika objekta


Objekti u JavaScript-u su fleksibilni. Čak i nakon što ste kreirali jedan, i dalje možete dodavati nova svojstva ili uklanjati postojeća.


Dozvoljeno je, ali je nešto što treba koristiti pažljivo.


Hajde da počnemo sa našom jednostavnom klasom `Dog`:


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


U ovom trenutku, `myDog` ima samo jedno svojstvo: `name`. Još uvek možemo dodati nova svojstva nakon što je kreiran:


```javascript
myDog.age = 5

console.log(myDog.age) // prints 5
```


Možemo takođe dodati novu metodu:


```javascript
myDog.jump = function () {
console.log(`${this.name} jumps!`)
}

myDog.jump() // Fido jumps!
```


I možemo ukloniti svojstva takođe, koristeći ključnu reč `delete`.


```javascript
delete myDog.name

console.log(myDog.name) // prints 'undefined'
```


Ovo radi, ali evo nečega važnog što treba znati: JavaScript engine-i kao što je V8 (koristi se u Node.js i u Chrome pregledaču) rade brže kada vaši objekti uvek zadržavaju iste osobine. Ako dodate ili uklonite osobine nakon što je objekat kreiran, to može usporiti stvari.


U malim programima, ovo nije mnogo važno. Ali u većim projektima (kao što su igre), bolje je navesti sve osobine u konstruktoru od početka, čak i ako ih ne koristite odmah. Ovo održava oblik objekta stabilnim i pomaže vašem kodu da radi brže.


Na primer, umesto ovoga:


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


Mogao/la bi


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


Obe verzije rade, ali druga je bolja za performanse. Unapred govorite mašini koje će osobine svaki objekat imati, i ona može optimizovati u skladu s tim.


JavaScript vam omogućava slobodno preoblikovanje objekata, ali kada koristite klase, najbolje je unapred isplanirati oblik vašeg objekta.



### Nasleđivanje sa `extends` i `super()`


Ponekad želite da kreirate klasu koja je *gotovo* ista kao druga klasa, ali sa nekoliko dodatnih funkcija.


Umesto modifikovanja oblika objekata (što, kao što je ranije pomenuto, nije optimalno za performanse), ili potrebe da se piše nova klasa od nule, JavaScript vam omogućava da koristite nešto što se zove **nasleđivanje**.


Nasleđivanje znači da jedna klasa može **proširiti** drugu. Nova klasa dobija sva svojstva i metode stare klase, a možete dodati još ili promeniti ono što vam je potrebno.


Recimo da imamo baznu klasu pod nazivom `Vehicle`:


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


Sada želimo da napravimo klasu `Car`. Auto je vrsta vozila, ali možda želimo da ima neke dodatne karakteristike ili drugačiju poruku kada se pokrene. Umesto da sve ponovo pišemo, možemo koristiti `extends`:


```javascript
class Car extends Vehicle {
start() {
console.log(`${this.brand} car is ready to drive!`)
}
}
```


Klasa `Car` sada **nasleđuje** sve od `Vehicle`. Dobija svojstvo `brand`, a metodu `start()` smo zamenili našom verzijom.


![](assets/en/4.webp)


Hajde da probamo:


```javascript
const myCar = new Car("Toyota")
myCar.start()
```


Ovo štampa:


```
Toyota car is ready to drive!
```


Iako `Car` nema svoj konstruktor, i dalje koristi onaj iz `Vehicle`. Ali ako želimo da napišemo prilagođeni konstruktor u `Car`, možemo, samo treba da uključimo poziv konstruktoru njegovog roditelja koristeći `super()`.


Evo kako:


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



Ovo štampa:


```
Toyota Corolla is ready to drive!
```


Dakle, da rezimiramo



- `extends` znači da je jedna klasa zasnovana na drugoj.
- `super()` se koristi za pozivanje konstruktora klase koju proširujete.
- Nova klasa dobija sva svojstva i metode originalne klase.
- Možete **prepisati** metode (kao što je `start()`) da bi radile nešto drugačije.


Ovo je korisno kada imate nekoliko stvari koje su slične (kao što su automobili, kamioni i bicikli) i želite da dele kod, ali da se i dalje ponašaju na svoj način.


### `instanceof`


Ključna reč `instanceof` proverava da li je objekat kreiran iz određene klase.


Recimo da imamo klasu pod nazivom `User`:


```javascript
class User {
constructor(username) {
this.username = username
}
}

const regularUser = new User("julia123")

console.log(regularUser instanceof User)
```


Ovo štampa:


```
true
```


Potvrđivanje da je `regularUser` `User`. To je zato što je `regularUser` kreiran korišćenjem klase `User`.


Takođe radi sa **nasleđenim** klasama. Na primer, ovde je klasa `Admin` koja proširuje `User`:


```javascript
class Admin extends User {}

const ourAdmin = new Admin("admin42")

console.log(ourAdmin instanceof Admin)   // true
console.log(ourAdmin instanceof User)    // true
```


Obe linije vraćaju `true`. To je zato što je `Admin` podklasa `User`, stoga je `ourAdmin` i `Admin` i `User`.


# Srednji JavaScript

<partId>243f63ab-4f34-5c30-80cb-84ef46f6761d</partId>


## Rukovanje Greškama

<chapterId>d0206bc5-d386-5e7f-9917-5803f392448c</chapterId>


Kako budete pisali složenije JavaScript programe, susretaćete se sa **greškama**. To su neočekivane situacije u kojima nešto pođe po zlu. Možda je neka promenljiva `undefined`, ali pokušavate da je koristite, ili neki kod primi pogrešan tip ulaza.


Ako ne obradimo ove greške pravilno, naš program bi mogao da se sruši ili da se ponaša na nepredvidive načine. JavaScript pruža alate za otkrivanje i upravljanje ovim greškama kako bismo ih mogli obraditi na elegantniji način.


### Uobičajena greška: pristupanje vrednosti na `undefined`


Evo uobičajene situacije koja izaziva grešku:


```javascript
const user = undefined
console.log(user.name)
```


Ako pokrenete ovaj kod, dobićete grešku koja izgleda ovako:


```
TypeError: Cannot read properties of undefined (reading 'name')
```


To je JavaScript koji vam govori: „Hej, pokušao si da dobiješ svojstvo `name` iz nečega što je `undefined`, a to nema smisla.” I kao što možete videti, kada se desi ovakva greška, program prestaje da radi osim ako niste specifično napisali kod da je uhvati i obradi.


### `throw`anje greške


Ponekad želite ručno **pokrenuti grešku** u svom kodu. U tom slučaju koristite ključnu reč `throw`.


```javascript
throw new Error("This is a custom error message")
```


Ovo odmah zaustavlja program i ispisuje:


```
Uncaught Error: This is a custom error message
```


Možete koristiti `throw` da biste nametnuli pravila u vašem programu. Na primer:


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


Drugi poziv izaziva grešku jer deljenje nulom nije dozvoljeno u ovom primeru.


### Hvatanje grešaka sa `try...catch`


Ako ne želite da vaš program padne kada dođe do greške, možete uhvatiti grešku koristeći blok `try...catch`. Ovo je korisno kada želite da vaš program **nastavi** čak i ako nešto ne uspe.


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log("Oops! Something went wrong.")
}
```


Izlaz:


```
Oops! Something went wrong.
```


Evo kako funkcioniše:



- Kod unutar bloka `try` se prvo pokušava.
- Ako dođe do greške, JavaScript **skače na `catch` blok**, preskačući ostatak `try` bloka.
- Blok `catch` prima grešku, tako da je možete ispisati ili obraditi na neki drugi način, kao na primer


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log(`The message of the error was: "${error.message}"`)
}
```


Izlaz:


```
The message of the error was: "Cannot read properties of undefined (reading 'name')"
```


### Blok `finally`


Možete takođe dodati blok `finally`. Ovo je kod koji **uvek radi**, bilo da je došlo do greške ili ne.


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


Izlaz:


```
Trying something risky...
Caught the error: Uh oh!
This will run no matter what.
```


## Izbegavanje Bugova

<chapterId>db12d9f6-5806-514c-998e-0ae24805104e</chapterId>


Ovo poglavlje prikazuje neke od najčešćih zamki u JavaScriptu i kako ih izbeći.


### `var` i Assignment bez deklaracije


U starijem JavaScript kodu, promenljive su često bile deklarisane koristeći ključnu reč `var`. Za razliku od `let` i `const`, o kojima ste već učili, `var` može da se ponaša na zbunjujuće načine.


Na primer:


```javascript
{
var message = "hello"
}
console.log(message)
```


Možda biste očekivali da `message` postoji samo unutar bloka, ali nije tako. `var` ignoriše blok scope i čini promenljivu dostupnom kroz celu funkciju ili fajl.


Ovo može dovesti do neočekivanog ponašanja, posebno u većim programima. Iz tog razloga, moderni JavaScript kod bi uvek trebalo da koristi `let` ili `const` umesto `var`.


Još gore, JavaScript vam omogućava da dodelite vrednosti promenljivama **bez da ih uopšte deklarišete**:


```javascript
function greet() {
user = "Alice"
}
greet()
console.log(user) // prints "Alice"
```


Ovo kreira novu globalnu promenljivu `name` bez ikakve deklaracije. Ovo se može desiti tiho i dovesti do grešaka koje su Hard za praćenje, posebno ako je to bila samo greška u kucanju. Uvek deklarisite promenljive koristeći `let` ili `const`.


### Slab tipa slabi


JavaScript je slabo tipiziran, što znači da automatski konvertuje vrednosti iz jednog tipa u drugi ako je potrebno. Ovo se naziva prinuda tipa (type coercion), i iako može biti zgodno, često dovodi do zbunjujućih rezultata.


Na primer:


```javascript
console.log("5" + 1)    // "51"
console.log("5" - 1)    // 4
console.log(true + 1)   // 2
console.log(null + 1)   // 1
```


U ovim primerima, JavaScript pokušava da pogodi šta ste mislili. Ponekad pretvara stringove u brojeve, ili booleane u brojeve, ili stringove u stringove. Ovo može učiniti da se vaš kod ponaša na neočekivane načine.


Biti svestan JavaScript-ovog sistema slabe tipizacije je važno. Kada stvari počnu da se ponašaju čudno, to može biti zbog neočekivane konverzije tipova.


### `"use strict"`


Možete omogućiti stroži režim koji pretvara neke tihe greške u stvarne greške i sprečava vas da koristite neke od opasnijih funkcija jezika.


Da biste omogućili ovaj stroži režim, dodajte ovu liniju na vrh vaše datoteke ili funkcije:


```javascript
"use strict"
```


Na primer:


```javascript
"use strict"
name = "Alice" // ReferenceError: name is not defined
```


Bez strogog režima, JavaScript bi tiho kreirao globalnu promenljivu pod nazivom `name`. Ali sa strogim režimom, ovo postaje prava greška, pomažući vam da ranije uočite greške.


Strogi režim takođe onemogućava neke zastarele funkcije JavaScripta i čini vaš kod lakšim za optimizaciju i održavanje.


## Vrednost vs Referenca

<chapterId>bb898425-dc2f-5e5c-864b-0cb7a4a9aea9</chapterId>


JavaScript tretira različite vrste vrednosti na različite načine.


Neke vrednosti se **kopiraju** kada ih dodelite promenljivoj.


Drugi su **deljeni** kada ih dodelite novoj promenljivoj, tako da ako promenite jedan, menja se i drugi.


### Prolaz po vrednosti


Kada se vrednost prosledi **po vrednosti**, JavaScript pravi **kopiju** te vrednosti.


Dakle, ako promenite jedno, to ne utiče na drugo.


Ovo se dešava sa primitivnim tipovima, kao što su:



- brojevi
- stringovi
- booleans (`true` i `false`)
- `null`
- `nedefinisano`


Hajde da pogledamo primer:


```javascript
let a = 5
let b = a

b = 10

console.log(a) // 5
console.log(b) // 10
```


Dali smo promenljivu `b` vrednost `a`, ali smo onda promenili `b` na `10`.


Pošto se brojevi prenose po vrednosti, JavaScript je kopirao `5` u `b`. `5` u `b` je nezavisna od originalne `5` u `a`, tako da promena vrednosti `b` nije imala efekta na `a`.


Hajde da probamo sa stringom:


```javascript
let name1 = "Alice"
let name2 = name1

name2 = "Bob"

console.log(name1) // Alice
console.log(name2) // Bob
```


Opet, promena `name2` nije uticala na `name1`, jer se stringovi takođe prosleđuju po vrednosti.


Isto se isto dešava kada prosledite primitivnu vrednost funkciji: ona se kopira. Tako funkcija ne može promeniti original.


```javascript
function plusOne(x) {
x = x + 1
}

let number = 5

plusOne(number)

console.log(number) // 5
```


Iako je unutar funkcije `1` dodato `x`, originalni `number` se nije promenio.


To je zato što je samo **kopija** prosleđena u funkciju.


### Proslijedi po referenci


Objekti se prosleđuju **po referenci**.


To znači da umesto da ih kopira, JavaScript samo prosleđuje **referencu** na njih, i ako ih modifikujete, sve druge promenljive koje upućuju na njih će takođe videti promenu.


Na primer:


```javascript
const person1 = { name: "Alice" }
const person2 = person1

person2.name = "Bob"

console.log(person1.name) // Bob
console.log(person2.name) // Bob
```


Oba, `person1` i `person2`, pokazuju na isti objekat u memoriji.


Dakle, kada smo promenili `person2.name`, promenili smo i `person1.name`, jer oba gledaju u istu stvar.


Nizovi su objekti, pa hajde da pokušamo isto sa nizom:


```javascript
const list1 = [1, 2, 3]
const list2 = list1

list2.push(4)

console.log(list1) // [1, 2, 3, 4]
console.log(list2) // [1, 2, 3, 4]
```


Ubacili smo `4` u `list2`, ali `list1` je takođe bio pogođen, jer se oba odnose na isti niz.


Hajde da vidimo šta se dešava kada prosledimo objekat funkciji:


```javascript
function rename(user) {
user.name = "Charlie"
}

const person = { name: "Dana" }

rename(person)

console.log(person.name) // Charlie
```


Funkcija je promenila objekat! To je zato što je primila **referencu** na originalni objekat `person`.


Nije dobio kopiju. Dobio je pristup originalnom objektu, i time je dobio mogućnost da ga modifikuje.


Važno je zapamtiti ovu razliku, jer inače naš kod može da se ponaša drugačije od onoga što očekujemo. Na primer, možemo napisati funkciju sa očekivanjem da neće menjati argumente koje prima, a kasnije otkriti da ih je zapravo menjala (jer su bili objekti, pa su prosleđeni po referenci).


## Rad sa funkcijama

<chapterId>e0d277a8-c642-5af7-9e53-dee27c811967</chapterId>


Već ste naučili kako da deklarišete i koristite funkcije u JavaScriptu. Ali JavaScript vam daje više alata za rad sa funkcijama na moćne načine.


### Funkcije strelice


Arrow funkcije su kraći način za pisanje funkcija. Umesto korišćenja ključne reči `function`, koristimo strelicu (`=>`).


Evo normalne funkcije:


```javascript
function greet(name) {
return `Hello, ${name}!`
}
```


Streličasta verzija izgleda ovako:


```javascript
const greet = (name) => {
return `Hello, ${name}!`
}
```


Ako funkcija ima **samo jednu liniju**, možete preskočiti zagrade i `return`:


```javascript
const greet = (name) => `Hello, ${name}!`
```


Ako funkcija ima **samo jedan parametar**, možete čak izostaviti zagrade oko parametara:


```javascript
const greet = name => `Hello, ${name}!`
```


Streličaste funkcije su veoma uobičajene u modernom JavaScript-u, jer omogućavaju izražavanje jednostavnih funkcija sa značajno manje šablonskog koda.


### Podrazumevani parametri


Ponekad želite da funkcija ima **podrazumevanu vrednost** ako nije prosleđen argument.


To možeš uraditi ovako:


```javascript
function sayHello(name = "friend") {
console.log(`Hello, ${name}!`)
}

sayHello("Alice") // Hello, Alice!
sayHello()        // Hello, friend!
```


Podrazumevana vrednost `"friend"` se koristi kada ništa nije prosleđeno.


### Prosledi parametre (`...`)


Šta ako vaša funkcija prima promenljiv broj argumenata?


Možete koristiti **operator širenja** (`...`) da ih sakupite u niz:


```javascript
function logAll(...items) {
console.log(items)
}

logAll(1, 2, 3) // [1, 2, 3]
logAll("a", "b") // ["a", "b"]
```


Zatim možete koristiti petlju za obradu svake stavke:


```javascript
function logEach(...items) {
for (const item of items) {
console.log(item)
}
}
```


Operator širenja je koristan kada ne znate koliko će argumenata biti prosleđeno.


### Funkcije višeg reda


**funkcija višeg reda** je funkcija koja:



- uzima drugu funkciju kao ulaz
- i/ili vraća funkciju kao izlaz


Evo jednostavan primer:


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


Ovo štampa:


```
Hello, friend!
Hello, friend!
```


Možemo proslediti arrow funkciju:


```javascript
runTwice(
() => console.log("Hello!")
)
```


Ovo štampa:


```
Hello!
Hello!
```


Takođe možete pisati funkcije koje **vraćaju** druge funkcije:


```javascript
function makeGreeter(name) {
return () => console.log(`Hi, ${name}`)
}

const greetAlice = makeGreeter("Alice")
const greetBob = makeGreeter("Bob")

greetAlice() // Hi, Alice
greetBob() // Hi, Bob
```


Funkcija `makeGreeter` je funkcija koja kreira druge funkcije. Prima string i vraća novu funkciju koja koristi taj string u svom pozivu `console.log`.


Ovakav obrazac je veoma moćan, jer vam omogućava da ostavite "rupe" u vašim funkcijama koje možete kasnije popuniti ponašanjem koje vam je potrebno.


### `map()`, `filter()`, `reduce()`


JavaScript vam daje neke korisne ugrađene metode za korišćenje sa nizovima.


Ove metode uzimaju funkcije kao argumente, tako da su i one funkcije višeg reda.


`map()` transformiše svaku stavku u nizu u nešto drugo.


Primer:


```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map(x => x * 2)

console.log(doubled) // [2, 4, 6]
```


Svaki broj se udvostručuje, a rezultat je novi niz.


`filter()` uklanja stavke iz niza ako ne prođu test.


Primer:


```javascript
const numbers = [1, 2, 3, 4, 5]
const numbersGreaterThanTwo = numbers.filter(x => x > 2)

console.log(numbersGreaterThanTwo) // [3, 4, 5]
```


Samo unosi niza za koje uslov `x > 2` vraća `true` se zadržavaju.


`reduce()` se koristi za kombinovanje svih elemenata u nizu u jednu vrednost.


Primer:


```javascript
const numbers = [1, 2, 3, 4]
const total = numbers.reduce((current, next) => current + next)

console.log(total) // 10
```


`reduce` prolazi kroz niz i, u ovom primeru, primenjuje operator `+` između `1` i `2`, zatim između rezultujućeg `3` i `3`, zatim između rezultujućeg `6` i `4`, sve dok ne dobije zbir svih elemenata niza (koji je 10).


Možete koristiti `reduce()` za mnoge stvari kao što su ukupni iznosi, proseci ili postepeno kreiranje novih vrednosti.


Ove metode (`map`, `filter`, `reduce`) su moćni alati za obradu podataka bez pisanja ručnih petlji.


Možete ih čak kombinovati u lanac operacija, ovako:


```javascript
const numbers = [1, 2, 3, 4, 5]

const result = numbers
.map(n => n * 2)        // Double each entry, obtain [2, 4, 6, 8, 10]
.filter(n => n > 3) // Keep only the entries bigger than 3, so you get [4, 6, 8, 10]
.reduce((n1, n2) => n1 + n2) // Adds them: 4 + 6 + 8 + 10 = 28

console.log(result) // 28
```


## Rad sa objektima

<chapterId>7842aada-f009-5518-b8e3-1104e166a035</chapterId>


U ovom poglavlju ćemo naučiti neke moćne i malo naprednije alate za rad sa objektima u JavaScriptu.


### Privatna Svojstva


Ponekad želimo sakriti svojstvo objekta tako da ne može biti promenjeno ili pristupljeno spolja. JavaScript nam daje način da to uradimo koristeći `#` pre imena svojstva. Ovo kreira **privatno** svojstvo, kojem se može pristupiti samo unutar klase.


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


Privatna svojstva su korisna kada želite da sprečite slučajne promene.


### `static` Properties


Ponekad želite da svojstvo pripada samoj klasi, a ne svakom objektu koji kreirate iz te klase. Za to služi `static`. `Static` svojstvo je sadržano u klasi i svi objekti te klase će se na njega odnositi.


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


Ovo je korisno za čuvanje zajedničkih podataka i metoda koje se primenjuju na celu grupu objekata, a ne samo na jedan.


### `get` i `set`


U JavaScript-u, `get` i `set` vam omogućavaju da kreirate svojstva koja *izgledaju* kao normalne promenljive, ali zapravo pokreću poseban kod u pozadini.


Metoda `get` se pokreće kada pokušate *pročitati* svojstvo. Deklariše se pisanjem `get` pre metode sa imenom svojstva.


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


Iako `fullName` nije regularna svojina, možemo je koristiti kao takvu, a u pozadini se pokreće funkcija `get` da bi se izgradilo puno ime.


Metod `set`ter se pokreće kada *dodelite* vrednost svojstvu. Omogućava vam da kontrolišete šta se dešava kada neko pokuša da promeni tu vrednost. Deklariše se pisanjem `set` pre metode sa imenom svojstva.


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


Kada izvršimo `user.fullName = "John Smith"`, pokreće se `set` metoda i ažuriraju se vrednosti `firstName` i `lastName`.


Dakle, iako se čini kao da samo postavljamo jednostavnu varijablu, zapravo pokrećemo logiku koja ažurira druge osobine.


## Ključevi i Vrednosti

<chapterId>01a397b8-c12a-5c39-82b3-6d9ebbb72a29</chapterId>


Svako svojstvo u JavaScript objektu ima **ključ** (takođe nazvan ime svojstva) i **vrednost**.


Na primer:


```javascript
const user = {
name: "Alice",
age: 30
}
```


U ovom objektu, `"name"` i `"age"` su ključevi, a "Alice" i `30` su njihove vrednosti.


### Dinamički Pristup


Ponekad ne znate ime svojstva unapred...možda ga dobijate od korisničkog unosa ili ga čitate iz promenljive. I dalje možete pristupiti koristeći **notaciju zagrada**, kao `myObject["keyName"]`.


```javascript
const user = {
name: "Alice",
age: 30
}

console.log(user["name"]) // Alice
```


Prosledili smo niz `name` objektu kako bismo dobili odgovarajuću vrednost.


Možemo sačuvati ključ u promenljivu i koristiti ga za pristup odgovarajućoj vrednosti kasnije, kao


```javascript
const user = {
name: "Alice",
age: 30
}

const key = "name"

console.log(user[key]) // Alice
```


### Dinamički Assignment


Takođe možete kreirati ili ažurirati svojstva objekta koristeći promenljive kao ključeve.


```javascript
const settings = {}

const key = "theme"
settings[key] = "dark"

console.log(settings) // { theme: "dark" }
```


Ovo je korisno kada želite da izgradite objekat korak po korak. Na primer:


```javascript
const user = {}

user["username"] = "bananaFan123"
user["email"] = "banana@fruit.com"

console.log(user)
// { username: "bananaFan123", email: "banana@fruit.com" }
```


Možete čak koristiti dinamički ključ *tokom kreiranja* objekta koristeći uglaste zagrade:


```javascript
const key = "language"
const config = {
[key]: "JavaScript"
}

console.log(config.language) // JavaScript
```


Ovo se zove **izračunato svojstvo**. Vrednost unutar uglastih zagrada se procenjuje, a rezultat se koristi kao ključ.


### `Symbol` Tip


Pored stringova, JavaScript vam takođe omogućava korišćenje posebnog tipa nazvanog `Symbol` kao ključa objekta.


Hajde da počnemo sa jednostavnim primerom:


```javascript
const id = Symbol("userID")

const user = {
name: "Bob",
[id]: 12345
}

console.log(user[id]) // 12345
```


U ovom primeru, `id` je Symbol. Nije string, ali i dalje funkcioniše kao ključ. Ako pokušate da prikažete `user` u konzoli, videćete sledeće:


```javascript
console.log(user) // { name: 'Bob', [Symbol(userID)]: 12345 }
```


Još jedna važna stvar: svaki simbol koji kreirate je jedinstven, čak i ako su kreirani koristeći isti string.


```javascript
const a = Symbol("label")
const b = Symbol("label")

console.log(a === b) // false
```


Simboli vam omogućavaju da definišete ključeve koji se neće sukobiti sa regularnim ključevima. Na primer, recimo da imate objekat sa `name` svojstvom, ali objekat će biti prilagodljiv od strane korisnika u budućnosti, na načine koje ne možete predvideti, i taj korisnik bi mogao dodati `name` svojstvo takođe. Ako je originalno `name` svojstvo definisano sa stringom, bilo bi prepisano novim, ovako:


```javascript
const obj = {
name: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy' }
```


Ako umesto toga koristimo simbol:


```javascript
const name = Symbol("name")

const obj = {
[name]: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy', [Symbol(name)]: 'John' }
```


Kao što možete videti, originalna `name` svojina je na neki način sačuvana na ovaj način. Ovo može biti korisno u određenim graničnim slučajevima.


## Objekti Uslužnosti

<chapterId>516e74c8-2a11-545a-a4d1-c2cabb91a273</chapterId>


JavaScript nam daje neke korisne ugrađene objekte koji nam pomažu u stvarima kao što su debagovanje i matematičke operacije.


### Druge metode `console`


Već ste videli `console.log`, koji ispisuje vrednosti na ekran.


Postoje neki drugi korisni metodi dostupni na objektu `console` koji vam mogu pomoći da otklonite greške u svojim programima.


#### `console.warn`


Štampa poruku žutom bojom (ili sa ikonom upozorenja u nekim okruženjima):


```javascript
console.warn("This is just a warning.")
```


#### `console.error`


Štampa poruku crvenom bojom, kao grešku:


```javascript
console.error("Something went wrong!")
```


#### `console.table`


Prikazuje niz ili objekat kao tabelu:


```javascript
const users = [
{ name: "Alice", age: 25 },
{ name: "Bob", age: 30 }
]

console.table(users)
```


Ovo ispisuje tabelu kao:


```
┌─────────┬────────┬─────┐
│ (index) │  name  │ age │
├─────────┼────────┼─────┤
│    0    │ 'Alice'│  25 │
│    1    │ 'Bob'  │  30 │
└─────────┴────────┴─────┘
```


Ovo može biti korisno za vizualizaciju strukturiranih podataka.


#### `console.time` i `console.timeEnd`


Možete izmeriti koliko nešto traje:


```javascript
console.time("timer")
for (let i = 0; i < 1000000; i++) {}
console.timeEnd("timer")
```


Ovo štampa nešto kao:


```
timer: 2.379ms
```


Korisno za neka jednostavna testiranja performansi.


### Objekat `Math`


JavaScript vam daje objekat `Math` sa korisnim metodama za izvođenje proračuna.


#### `Math.random()`


Vraća nasumičan broj između 0 (uključivo) i 1 (isključivo):


```javascript
const r = Math.random()
console.log(r)
```


Primer izlaz:


```
0.4387429859
```


#### `Math.floor()` i `Math.ceil()`



- `Math.floor(n)` zaokružuje **nadole** na najbliži ceo broj
- `Math.ceil(n)` zaokružuje **na gore** do najbližeg celog broja


```javascript
console.log(Math.floor(4.9)) // 4
console.log(Math.ceil(4.1))  // 5
```


#### `Math.round()`


Zaokružuje se na najbliži ceo broj:


```javascript
console.log(Math.round(4.4)) // 4
console.log(Math.round(4.6)) // 5
```


#### `Math.max()` i `Math.min()`


Vraća najveću ili najmanju vrednost iz liste brojeva:


```javascript
console.log(Math.max(5, 9, 3)) // 9
console.log(Math.min(5, 9, 3)) // 3
```


#### `Math.pow()` i `Math.sqrt()`



- `Math.pow(a, b)` daje vam `a` na stepen `b`
- `Math.sqrt(n)` daje kvadratni koren od `n`


```javascript
console.log(Math.pow(2, 3))   // 8
console.log(Math.sqrt(16))    // 4
```


# Napredni JavaScript

<partId>72c30671-ca20-5617-92a5-d5ba7aa38c93</partId>


## Druge kolekcije

<chapterId>a9a70c6d-a343-5a46-a383-e288bc2700e3</chapterId>


JavaScript nam pruža neke posebne tipove kolekcija koji prevazilaze regularne nizove i objekte. Ovi uključuju `Map` i `Set`.


Oni vam pomažu da skladištite i upravljate grupama vrednosti, ali funkcionišu drugačije od onoga što ste do sada videli.


`Map` je kolekcija **parova ključ-vrednost**, baš kao i objekat. Ali ima neke važne razlike:



- Ključevi mogu biti **bilo koje vrednosti**, ne samo stringovi.
- Redosled stavki je očuvan.
- Ima ugrađene metode koje olakšavaju rad s njim.


Kreirate novu mapu ovako:


```javascript
const myMap = new Map()
```


Ovo kreira praznu mapu. Da biste dodali unose u nju, koristite `myMap.set(key, value)`:


```javascript
myMap.set("name", "Alice")
```


Ovo dodaje ključ `"name"` sa vrednošću `"Alice"`.


Takođe možete koristiti broj kao ključ:


```javascript
myMap.set(42, "The answer")
```


Čak i objekat kao ključ:


```javascript
const objKey = { id: 1 }
myMap.set(objKey, "Object as key")
```


To ne bi radilo sa regularnim objektima, koji dozvoljavaju samo string ključeve.


Da biste **dobili vrednost**, koristite `myMap.get(key)`:


```javascript
console.log(myMap.get("name"))     // Alice
console.log(myMap.get(42))         // The answer
console.log(myMap.get(objKey))     // Object as key
```


Da biste **proverili da li ključ postoji**, koristite `myMap.has(key)`:


```javascript
console.log(myMap.has("name")) // true
```


Da **uklonite ključ**, koristite `myMap.delete(key)`:


```javascript
myMap.delete("name")
```


Da biste **očistili celu mapu**, koristite `myMap.clear()`:


```javascript
myMap.clear()
```


Mape su odlične za upravljanje velikim kolekcijama vrednosti, jer pristup vrednostima na velikoj mapi obično daje mnogo bolje performanse nego na velikom objektu.


### `Skup`


`Set` je kolekcija **samo vrednosti** (bez ključeva), gde svaka vrednost mora biti **jedinstvena**. To znači:



- Ne možete imati istu vrednost dva puta
- Vrednosti su sačuvane redosledom kojim ih dodajete


Kreirate skup kao ovaj:


```javascript
const mySet = new Set()
```


Da **dodate vrednosti**, koristite `mySet.add(value)`:


```javascript
mySet.add(1)
mySet.add(2)
mySet.add(2) // duplicate, will be ignored
```


Iako smo pokušali da dodamo `2` dva puta, skup će zadržati samo jednu kopiju.


Da **proverite da li je vrednost u skupu**, koristite `mySet.has(value)`:


```javascript
console.log(mySet.has(2)) // true
console.log(mySet.has(3)) // false
```


Da **uklonite vrednost**, koristite `mySet.delete(value)`:


```javascript
mySet.delete(2)
```


Da biste **očistili sve**, koristite `mySet.clear()`:


```javascript
mySet.clear()
```


`Set` je koristan kada želite da sačuvate kolekciju jedinstvenih vrednosti bez potrebe za ručnim proveravanjem duplikata:


```javascript
const numberArray = [1, 2, 2, 3, 4, 4, 4, 5]

const numberSet = new Set(numberArray)

console.log(numberSet) // Set(5) { 1, 2, 3, 4, 5 }
```


`Set` izbegava duplikate za vas.


## Iteratori

<chapterId>61d24e5e-b7e4-541a-8322-778f61f26a72</chapterId>


Većina stvari u JavaScriptu koje možete iterirati (kao što su nizovi, stringovi, mape, skupovi) su **iterable**: mogu obezbediti iteratore za njihov sadržaj.


Iterator je poseban objekat u JavaScript-u koji vam pomaže da prolazite kroz listu stavki **jednu po jednu**.


### `Object` iteratori


Za razliku od nizova ili mapa, regularni objekti **nisu iterabilni** sa `for...of`. Ako probate ovo:


```javascript
const user = {
name: "Alice",
age: 30
}

for (const value of user) {
console.log(value)
}
```


Dobićete grešku:


```
TypeError: user is not iterable
```


To je zato što obični objekti nemaju ugrađen iterator. Ali JavaScript vam daje druge alate za iteraciju preko njih.


#### `Object.keys()`


Možete koristiti `Object.keys(obj)` da dobijete niz **ključeva** objekta, a zatim iterirajte preko njega:


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


Ovo štampa:


```
name
age
```


#### `Object.values()`


Da biste iterirali preko **vrednosti**, koristite `Object.values()`:


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


Ovo štampa:


```
Alice
30
```


#### `Object.entries()`


Ako želite **i ključ i vrednost**, koristite `Object.entries()`:


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


Ovo štampa:


```
name is Alice
age is 30
```


Iako objekti nisu direktno iterabilni, ove metode vam omogućavaju potpuni pristup njihovom sadržaju na način koji dobro funkcioniše sa `for...of`.


Ali kako rade iteratori?


### `Symbol.iterator`


Tajna svih iterables je poseban **simbol** nazvan `Symbol.iterator`.


Ovaj simbol je ugrađeni ključ koji govori JavaScriptu: „Ovaj objekat se može iterirati.”


Kada pozovete `myIterable[Symbol.iterator]()`, JavaScript vam vraća **iterator objekat** sa `.next()` metodom.


Hajde da vidimo kako to izgleda:


```javascript
const colors = ["red", "green", "blue"]

const iterator = colors[Symbol.iterator]()

console.log(iterator.next()) // { value: 'red', done: false }
```


Svaki poziv `.next()` daje vam sledeću vrednost. Kada završi, vraća:


```javascript
{ value: undefined, done: true }
```


### `next()`


Metoda `.next()` se koristi za dobijanje sledeće stavke iz sekvence.


Svaki put kada pozovete `.next()`, dobijate objekat sa dva ključa:



- `value`: trenutna stavka
- `done`: boolean koji vam govori da li je iteracija završena


Hajde da uradimo ceo primer:


```javascript
const names = ["Lina", "Tom", "Eva"]      // declare an array
const iterator = names[Symbol.iterator]() // use the Symbol.iterator function to get an iterator for this array

let result = iterator.next()              // get the first element of the array

while (!result.done) {                    // repeat this loop until you reach the last element of the array, which is marked with { done: true }
console.log(result.value)               // print the value of each element
result = iterator.next()                // get the next element of the array
}
```


Ovo štampa:


```
Lina
Tom
Eva
```


Ovako `for...of` petlja radi ispod haube: koristi ovaj obrazac sa `.next()`.


Dobijate isti rezultat sa


```javascript
const names = ["Lina", "Tom", "Eva"]

for (const result of names) {
console.log(result)
}
```


### Pravljenje klase iterabilnom


Možete takođe definisati svoju **iterabilnu klasu** dodavanjem metode `[Symbol.iterator]()`.


Recimo da želimo klasu koja predstavlja **opseg brojeva**, kao od 1 do 5.


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


Ovo štampa:


```
1
2
3
4
5
```


Evo šta se dešava:



- Definisali smo klasu `Range`
- Unutar klase, implementirali smo `[Symbol.iterator]()`, tako da JavaScript zna kako da iterira kroz nju
- Metoda `next()` vraća svaki broj jedan po jedan
- Kada dostignemo `kraj`, vraća `{ done: true }`


Sada naša klasa `Range` radi kao niz, i možemo je koristiti u bilo kojoj petlji koja očekuje iterabilni objekat.


### Funkcije generatora i `yield`


Da bi olakšao kreiranje iteratora, JavaScript pruža **generator funkcije**, koristeći ključnu reč `function*` (to je `function` sa `*` na kraju) i ključnu reč `yield`.


Hajde da probamo:


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


Svaki `yield` vraća vrednost i **pauzira** funkciju dok se ne pozove sledeći `.next()`.


Takođe možete iterirati preko generatora sa `for...of`:


```javascript
for (const num of numberGenerator()) {
console.log(num)
}
```


Ovo štampa:


```
1
2
3
```


## Istovremenost sa povratnim pozivima

<chapterId>f3fc76ca-b3ef-54eb-a06e-501007002054</chapterId>


Do sada je naš kod bio **sinhroni**: izvršava se liniju po liniju, redom. Ali neke stvari u stvarnom svetu zahtevaju vreme, i ne želimo da ceo program pauzira dok čeka.


U ovom poglavlju ćemo uvesti novi koncept: **konkurentnost**. Omogućava nam da manipulišemo redosledom u kojem se stvari obavljaju. Ovo je korisno kada se bavimo stvarima kao što su tajmeri, korisnički unos ili čitanje fajlova sa diska. JavaScript nudi različite alate za ostvarivanje konkurentnosti.


### `setTimeout`


Funkcija `setTimeout` vam omogućava da **pokrenete funkciju kasnije**, nakon što prođe određeno vreme.


Primer:


```javascript
console.log("Start")

setTimeout(
() => console.log("This runs after 2 seconds"),
2000
)

console.log("End")
```


Ovo štampa:


```
Start
End
This runs after 2 seconds
```


Iako se `setTimeout` pojavljuje u sredini koda, on ne blokira ostatak. Umesto toga, zakazuje funkciju da se izvrši **kasnije**, i odmah nastavlja dalje.


`2000` znači 2000 milisekundi (što je 2 sekunde).

Evo detaljnijeg i početnicima prilagođenog prepisivanja odeljaka **Callbacks** i **Promise**, koristeći manipulaciju podacima i jasne napomene tokom celog teksta:


### Povratni pozivi


**Povratni poziv** je samo funkcija koju dajemo drugoj funkciji kako bi mogla biti **pozvana kasnije**.


Hajde da pogledamo pravi primer koristeći brojeve. Zamislimo da imamo listu brojeva i želimo da udvostručimo svaki od njih, a zatim da primenimo funkciju (povratni poziv) na rezultujući "udvostručeni" niz, ali želimo to da uradimo nakon malog kašnjenja, kao da čekamo nešto sporo (poput učitavanja podataka sa interneta).


Evo funkcije koja to radi koristeći **callback**:


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


Hajde da pokušamo da koristimo ovu funkciju:


```javascript
const input = [1, 2, 3]

doubleNumbers(input, function(result) {
console.log("Here is the doubled array:", result)
})
```


Nakon 1 sekunde, ovo se ispisuje:


```
Here is the doubled array: [ 2, 4, 6 ]
```


**Šta se ovde dešava?**


1. Prosleđujemo `input` kao listu brojeva koje želimo da udvostručimo.

2. Takođe prosleđujemo **callback funkciju** koja govori programu šta da uradi *nakon* udvostručavanja.

3. Unutar `doubleNumbers`, simuliramo kašnjenje koristeći `setTimeout`, zatim vršimo udvostručavanje.

4. Kada je to završeno, pozivamo povratni poziv na rezultujući "udvostručeni" niz.


Ova tehnika funkcioniše, ali zamislite da želite da uradite **više koraka** nakon toga, kao što je filtriranje malih brojeva i zatim njihovo sabiranje. Morali biste da **ugnjezdite** više povratnih poziva ovako:


```javascript
doubleNumbers(input, function(doubled) {
filterBigNumbers(doubled, function(filtered) {
sumNumbers(filtered, function(total) {
console.log("Final result:", total)
})
})
})
```


Ovo je Hard za čitanje i neuredno. Ovaj stil se zove **callback hell**, i upravo je to ono što je `Promise` stvoren da popravi.


## Istovremenost sa Promisima

<chapterId>30fddaca-729f-5c8d-bf86-8dfc7b3c9800</chapterId>


`Promise` je ugrađeni JavaScript objekat koji predstavlja vrednost koja će **biti spremna u budućnosti**.


Možemo kreirati Promise ovako:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve("It worked!") // This means everything went OK
})
```


Deo `new Promise()` kreira obećanje.


Unutar njega, dajemo mu funkciju sa dva parametra:



- `resolve`, je funkcija koju pozivamo kada je sve uspešno
- `reject`, je funkcija koju pozivamo ako nešto pođe po zlu


U gornjem primeru, jednostavno ga odmah rešavamo porukom `"It worked!"`.


### `.then()`


Da bismo uradili nešto **nakon** što je obećanje ispunjeno, koristimo `.then()`:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve(100) // This means everything went OK
})

promise.then(result => {
console.log("The result is:", result)
})
```


Ovo štampa:


```
The result is: 100
```


Vrednost koju smo prosledili u `resolve()` se šalje funkciji unutar `.then()` kao `result`.


Hajde da simuliramo zadatak koji traje 2 sekunde koristeći `setTimeout`:


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


Ovo će čekati 2 sekunde, a zatim ispisati:


```
Done waiting!
```


### `reject()`


Hajde da kreiramo obećanje koje **ne uspeva**:


```javascript
const failingPromise = new Promise((resolve, reject) => {
reject("Something went wrong")
})
```


Sada, ako koristimo `.then()` na ovome, ništa se neće desiti, jer `.then()` obrađuje samo uspeh.


Da bismo obradili greške, koristimo `.catch()`:


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


Ovo se samo štampa


```
Caught an error: Something went wrong
```


Vrednost prosleđena u `reject()` se šalje funkciji `.catch()`.


Hajde da napravimo Promise koji **ponekad radi, a ponekad ne**, na osnovu nekog uslova.


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


Sada možemo pozvati ovo i obraditi oba slučaja:


```javascript
checkNumber(5)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Ovo štampa:


```
Success: Positive number
```


A ako pokušamo sa drugim brojem:


```javascript
checkNumber(-1)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Štampa:


```
Failure: Not a positive number
```


### Ulančavanje operacija koristeći `Promise`e



Možemo prepisati naš raniji primer koristeći `Promise`, i izgledaće mnogo čistije.


Hajde da započnemo pisanjem nove verzije naše funkcije za udvostručavanje, ali ovaj put, ona vraća **obećanje**:


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


Sada možemo koristiti `.then()` da kažemo JavaScript-u šta da uradi sa rezultatom:


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


Ovo štampa:


```
Doubled numbers: [ 2, 4, 6 ]
```


Do sada, ovo funkcioniše isto kao verzija sa povratnim pozivom, ali sada je kod lakši za proširenje i čitanje.


Hajde da kažemo da želimo dodati više koraka:


1. Prvo, udvostručite sve brojeve

2. Zatim, uklonite brojeve manje od 4

3. Na kraju, sve ih saberite zajedno


Možemo napisati jednu funkciju za svaki korak, sve koristeći obećanja:


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


Sada ih možemo **povezati** zajedno ovako:


```javascript
const input = [1, 2, 3]

doubleNumbers(input)
.then(filterBigNumbers)
.then(sumNumbers)
.then(
result => console.log("Final result after all steps:", result)
)
```


Ovo štampa:


```
Final result after all steps: 10
```


Hajde da prođemo kroz to šta ovo radi:


1. `doubleNumbers` udvostručuje niz: `[2, 4, 6]`

2. `filterBigNumbers` uklanja sve što je ≤ 3: `[4, 6]`

3. `sumNumbers` sabira preostale brojeve: `4 + 6 = 10`

4. Na kraju, štampamo rezultat.


Svaki `.then()` čeka da se prethodni korak završi. Tako možemo izgraditi **lanac akcija** bez ugnježđivanja. Ovo čini kod čitljivijim i lakšim za debagovanje.


## Istovremenost sa `async`/`await`

<chapterId>6e93d29f-c8bf-5fd1-a9c9-4e794ee6cbd0</chapterId>


Videli smo kako `Promise` lanci pomažu da izbegnemo callback hell, ali i dalje mogu postati malo Hard za čitanje kada je uključeno mnogo koraka.


Tu dolaze `async` i `await`. Oni nam omogućavaju da pišemo asinhroni kod **koji izgleda kao sinhroni kod**, što ga čini lakšim za razumevanje.


### Šta je `async`?


Kada napišete ključnu reč `async` pre funkcije, JavaScript automatski obavija povratnu vrednost funkcije u Promise.


Hajde da vidimo osnovni primer:


```javascript
async function greet() {
return "hello"
}
```


Ako pozovete ovu funkciju:


```javascript
const result = greet()
console.log(result)
```


Videćeš ovo:


```
Promise { 'hello' }
```


Iako ste upravo vratili string, JavaScript ga pretvara u Promise za vas. Pravu vrednost možete dobiti koristeći `.then()` na sledeći način:


```javascript
greet().then( result => console.log(result) ) // prints "hello"
```


Ili možete koristiti `await`...


### Šta je `await`?


Ključna reč `await` govori JavaScript-u: „sačekaj dok se ovaj Promise ne završi, a zatim mi daj rezultat.”


Ali možete koristiti samo `await` **unutar asinhrone funkcije**.


Hajde da prepišemo primer koristeći `await`:


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


Sada možemo koristiti rezultat kao da je to regularna vrednost.


Hajde da sada uradimo nešto malo korisnije.


### Simulacija kašnjenja sa `await`


Napravićemo jednostavnu funkciju `wait` koja uzima količinu milisekundi kao argument i samo se razrešava nakon tog broja milisekundi, bez obavljanja bilo čega drugog:


```javascript
function wait(ms) {
return new Promise(resolve => {
setTimeout(resolve, ms)
})
}
```


Hajde da pokušamo da ga koristimo:


```javascript
async function test() {
console.log("waiting 2 seconds...")
await wait(2000)
console.log("done waiting")
}

test()
```


Ovo štampa:


```
waiting 2 seconds...
done waiting
```


Možete zamisliti `await` kao „zaustavi se ovde dok se obećanje ne završi, zatim nastavi.”


Ovo vam omogućava da pišete kod u **od vrha ka dnu** maniru koji se ponaša asinhrono, bez ulančavanja poziva `.then()`.


### Čekanje podataka


Hajde da ponovo iskoristimo naš prethodni primer, gde dupliramo brojeve, zatim filtriramo, pa sumiramo. Ali ovog puta, koristićemo `async`/`await`.


Napravićemo 3 funkcije koje simuliraju čekanje i vraćaju Promise objekte:


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


Sada napišimo `async` funkciju da ih kombinujemo:


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


Ovo štampa:


```
Final result: 10
```


Ovo je mnogo lakše za čitanje nego povezivanje `.then()` ili ugnježđivanje povratnih poziva.


Izgleda kao regularan program korak-po-korak, ali se i dalje ponaša asinhrono.


## Asinhroni iteratori

<chapterId>438b037d-9931-56d7-9052-7b4470f3c75b</chapterId>


Već ste naučili o **iteratorima** i kako možemo koristiti `for...of` za iteraciju kroz nizove i druge iterabilne stvari.


Ali šta ako podaci koje želimo da iteriramo stižu sa zakašnjenjem?


Ponekad želimo da iteriramo preko stvari koje stižu **asinhrono**, kao što su poruke iz četa, linije iz fajla ili brojevi iz sporog izvora.


Da bismo to uradili, JavaScript nam daje **asinhrone iteratore**.


### Asinhrone generator funkcije


Najlakši način za kreiranje asinhronog iteratora je korišćenje **asinhrone generator funkcije**.


Pišemo ovako:


```javascript
async function* generateNumbers() {
yield 1
yield 2
yield 3
}
```


Ovo izgleda kao običan generator, ali sa `async` ispred njega.


Sada možemo koristiti `for await...of` za konzumiranje vrednosti:


```javascript
async function run() {
for await (const n of generateNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


Ovo će se ispisati:


```
Got number: 1
Got number: 2
Got number: 3
Done!
```


Pa čemu se razlikuje od običnog generatora?


Razlika je: sada možemo koristiti `await` unutar generatora.


Hajde da ponovo napravimo pomoćnika za kašnjenje:


```javascript
function wait(ms) {
return new Promise(resolve => setTimeout(resolve, ms))
}
```


Sada da prinosimo brojeve **polako**:


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


Pokušaj koristiti:


```javascript
async function run() {
for await (const n of generateSlowNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


### Zašto koristiti asinhrone iteratore?


Asinhroni iteratori su korisni kada:



- Vrednosti ne stižu sve odjednom.
- Želite da ih rešavate jednog po jednog, **kako dolaze**.
- Radite sa Promisima i želite da iterirate na čist način.


Na primer, ako želite da učitavate poruke sa servera za ćaskanje jednu po jednu, ili da preuzmete veliku datoteku u delovima, asinhroni iteratori vam omogućavaju da napišete `for` petlju koja radi sa odloženim podacima.


### `Symbol.asyncIterator`


Takođe možemo koristiti asinhrone iteratore u prilagođenim klasama.


Evo primera koji proizvodi brojeve sa zakašnjenjem:


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


Sada možemo koristiti `for await...of` kao i ranije:


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


Ovo vam omogućava da kreirate objekte koji se mogu iterirati asinhrono.


## Assignment sintaksni šećer

<chapterId>8b1ba7d8-ecfd-5470-b86e-73cb84ccc8b7</chapterId>


"Sintaksni šećer" znači pisanje nečega na kraći ili lakši način, bez promene onoga što radi. To je samo lepši način da se kaže ista stvar.


JavaScript ima ugrađeni sintaksni šećer koji nam omogućava da pišemo čistije i kraće deklaracije. U ovom poglavlju, pogledaćemo kako da dodelimo vrednosti na osnovu uslova, ažuriramo promenljive pomoću matematike, izvučemo vrednosti iz nizova ili objekata, i kopiramo ili kombinujemo ih sa jednostavnijom sintaksom.


### Ternarni operator


U JavaScript-u, možete dodeliti vrednost na osnovu uslova koristeći **ternarni operator**, što je kratak način pisanja `if...else`.


Umesto da radiš:


```javascript
let message

if (isMorning) {
message = "Good morning"
} else {
message = "Hello"
}
```


Možete pisati:


```javascript
const message = isMorning ? "Good morning" : "Hello"
```


Ovo znači:



- Ako je `isMorning` tačno, koristi `"Dobro jutro"`
- Inače, koristi `"Hello"`


Opšti oblik je:


```javascript
condition ? valueIfTrue : valueIfFalse
```


Možete ga koristiti i unutar drugih izraza:


```javascript
console.log(isSunny ? "Go outside" : "Stay in")
```


Samo se pobrini da ga koristiš za **jednostavne** odluke. Ako je logika složena, drži se `if...else`.


### Alternativni Assignment Operateri


JavaScript ima **skraćene operatore** za dodelu u kombinaciji sa operacijama.


Hajde da pogledamo normalan način:


```javascript
let counter = 1
counter = counter + 1
```


Ovo se može skratiti na:


```javascript
let counter = 1
counter += 1 // same as counter = counter + 1
```


Evo najčešćih:


| Operator | Meaning             |
| -------- | ------------------- |
| `+=`     | add and assign      |
| `-=`     | subtract and assign |
| `*=`     | multiply and assign |
| `/=`     | divide and assign   |

Primeri:


```javascript
let score = 10
score += 5  // now score is 15
score *= 2  // now score is 30
score -= 10 // now score is 20
```


Ovo je korisno kada želite da ažurirate promenljivu koristeći njenu sopstvenu vrednost.


### Destrukturiranje


**Destrukturiranje** vam omogućava da lako uzimate vrednosti iz nizova ili objekata i skladištite ih u promenljive.


#### Nizovi


Pretpostavimo da imate:


```javascript
const colors = ["red", "green", "blue"]
```


Umesto da radiš:


```javascript
const first = colors[0]
const second = colors[1]
```


Možete uraditi:


```javascript
const [first, second] = colors
```


Ovo dodeljuje:



- `first` do `"red"`
- `drugi` do `"Green"`


Možete preskočiti i vrednosti:


```javascript
const [,, third] = colors
console.log(third) // blue
```


#### Objekti


Možete izdvojiti vrednosti iz objekata takođe:


```javascript
const user = { name: "Alice", age: 30 }

const { name, age } = user
console.log(name) // Alice
console.log(age)  // 30
```


Ako nekretnina ima drugačije ime od promenljive koju želite, možete je preimenovati:


```javascript
const { name: username } = user
console.log(username) // Alice
```


Destrukturiranje čini vaš kod čistijim prilikom rada sa objektima i nizovima.


### Sintaksa širenja


**Sintaksa širenja** koristi `...` za raspakivanje ili kopiranje vrednosti.


#### Nizovi


Možete kopirati ili spojiti nizove:


```javascript
const a = [1, 2]
const b = [3, 4]

const both = [...a, ...b]
console.log(both) // [1, 2, 3, 4]
```


Možete takođe klonirati niz:


```javascript
const original = [10, 20, 30]
const clone = [...original]
```


#### Objekti


Možete učiniti isto sa objektima:


```javascript
const a = { x: 1 }
const b = { y: 2 }

const merged = { ...a, ...b }
console.log(merged) // { x: 1, y: 2 }
```


Takođe možete nadjačati vrednosti:


```javascript
const user = { name: "Alice", age: 30 }
const updated = { ...user, age: 31 }

console.log(updated) // { name: "Alice", age: 31 }
```


Ovo je veoma korisno kada se ažuriraju objekti bez promene originala.


# NodeJS

<partId>42fe4d49-dace-5135-bb9e-b9d75034fb2a</partId>


## Kako smo došli do Node

<chapterId>0da1d60c-06c9-54e6-a181-ae7dabf6e3b8</chapterId>


U ovom poglavlju ćemo naučiti malo o istorijskom kontekstu JavaScript-a i NodeJS-a.


Istorijski kontekst je veoma važan u softveru, jer često koristimo alate koje su napravili drugi ljudi, i stoga smo pod uticajem odluka koje su oni doneli u prošlosti.


Razumevanje razloga za te odluke i kako su alati koje koristimo postali takvi kakvi jesu pomoći će nam da se osećamo malo manje zbunjeno u vezi s onim što radimo.


### Poreklo JavaScripta


JavaScript je započeo kao jednostavan jezik dizajniran da učini web stranice interaktivnim.


Tokom 1990-ih, web pregledači poput Netscape Navigator-a dodali su JavaScript kako bi programeri mogli pisati kod koji se izvršava direktno u pregledaču.


Originalna ideja je bila da Java bude osnovni jezik za pravljenje veb-sajtova (sa takozvanim "Java apletima"), a JavaScript samo za manje stvari.


Osnovni dizajn je uradio Brendan Eich, koji je u to vreme bio zaposlen u Netscape-u, za manje od 2 nedelje.


Ali većina ljudi je više volela koristiti JavaScript nego Javu, a takođe su Java apleti imali neke sigurnosne probleme u to vreme, pa je na kraju Java odbačena kao opcija i JavaScript je postao de facto standard za web razvoj.


### V8 motor


JavaScript je interpretirani jezik, za razliku od kompajliranih jezika kao što je C.


Kod napisan u kompajliranom jeziku pretvara se u binarni kod, a taj binarni kod se direktno šalje CPU računara.


![](assets/en/6.webp)


Interpredirani jezici, s druge strane, teže da budu više prilagođeni korisnicima i bliži su načinu na koji ljudi razmišljaju ("visok nivo") nego načinu na koji mašine rade ("nizak nivo"); tako da obično imaju virtuelnu mašinu napravljenu za pokretanje njihovog koda.


Virtuelna mašina je poseban program koji se nalazi između koda koji pišete i CPU-a, i izvršava vaš kod (jer ga CPU ne može razumeti).


Ovo vam omogućava da programirate bez previše znanja o osnovnoj mašini, ali takođe ima cenu u smislu performansi, jer računar ne pokreće samo vaš program; pokreće program (virtuelnu mašinu) koja pokreće vaš program.


Kako su veb aplikacije postajale sve složenije, postojala je potreba za poboljšanjem performansi JavaScripta. V8 engine je interpreter koji pokreće JavaScript u Google Chrome-u. Razvijen je u Google-u i objavljen 2008. godine.


Dok su stariji JavaScript motori uglavnom bili tradicionalne virtuelne mašine, V8 motor je JIT (just-in-time) kompajler.


JavaScript kod se prosleđuje V8 endžinu, a endžin pokušava da kompajlira delove koda kao izvorne binarne datoteke u hodu. Ovo vam omogućava da imate iskustvo rada sa jezikom visokog nivoa, uz performanse koje su malo bliže jezicima niskog nivoa. Ovo je učinilo JavaScript najbržim jezikom visokog nivoa na svetu, pomalo kao "najbolje iz oba sveta".


### NodeJS runtime


Iako je jednostavan za korišćenje i prilično brz za izvršavanje, nakon objavljivanja V8 JavaScript je imao veliko ograničenje: mogao je da radi samo unutar pregledača.


Zašto je to problem?


Pa, pošto pregledači izvršavaju kod preuzet sa miliona različitih izvora na internetu, lako mogu naići na malver, pa su "sandboxovani" od ostatka operativnog sistema.


![](assets/en/7.webp)


JavaScript nije mogao pristupiti sistemu datoteka i drugim lokalnim resursima na vašem računaru (barem ne lako kao što su to mogli drugi jezici), tako da je to bila značajna ograničenja u pogledu vrsta aplikacija koje ste mogli izraditi s njim.


2009. godine, Ryan Dahl je objavio NodeJS, koji je okruženje za izvršavanje koje omogućava korišćenje V8 engine-a van pregledača, direktno na matičnom operativnom sistemu vašeg računara. Takođe dodaje mnoge funkcije koje su korisne za pisanje server-side i command-line programa. Na primer, možete koristiti NodeJS za kreiranje web servera, čitanje i pisanje fajlova, ili izradu alata koji automatizuju zadatke.


![](assets/en/8.webp)


U ovom kursu do sada smo istraživali JavaScript funkcije koje su prisutne i u pregledaču i u NodeJS-u. Te funkcije su nam omogućile da definišemo podatke i manipulišemo njima na apstraktne načine. U narednih nekoliko lekcija istražićemo funkcije koje su specifične za NodeJS i omogućavaju nam interakciju sa operativnim sistemom.


## Argumenti komandne linije

<chapterId>960d20f3-c424-5d51-a041-ef17d2e94b6d</chapterId>


NodeJS nam omogućava, između ostalog, da pravimo CLI-jeve (Command Line Interfaces).


Za to nam je potreban način za primanje argumenata komandne linije, što se u Node-u radi korišćenjem ugrađenog objekta `process`.


### `proces`


NodeJS pruža poseban objekat pod nazivom `process` koji predstavlja trenutno pokrenut program.


Možete ga koristiti za pregled okruženja, trenutnog radnog direktorijuma, pa čak i za izlazak iz programa kada je to potrebno.


Na primer:


```javascript
console.log(process.platform)
```


Ovo ispisuje platformu operativnog sistema, kao što su `win32`, `linux` ili `darwin` (Mac).


### `process.argv`


Kada pokrenete NodeJS program iz terminala, možete proslediti dodatne reči (argumente) nakon imena skripte. Oni se čuvaju u `process.argv`.


Na primer, ako pokrenete ovu komandu:


```
node my_script.js alpha beta
```


Možete odštampati argumente ovako:


```javascript
console.log(process.argv)
```


Izlaz može izgledati ovako:


```
[ '/path/to/node', '/path/to/my_script.js', 'alpha', 'beta' ]
```


Prve dve stavke su uvek putanja do Node-a i putanja do vašeg skripta. Sve dodatne reči koje prosledite skriptu dolaze nakon toga.


Niz `process.argv` može se skratiti kao i bilo koji drugi niz koristeći metodu `.slice()`, tako da možete dobiti samo argumente koji su prosleđeni.


```javascript
const args = process.argv.slice(2)

console.log(args)
```


Imati pristup argumentima koje korisnik prosleđuje je od suštinskog značaja za razvoj aplikacija komandne linije.


## Moduli

<chapterId>4e1651a5-65fd-50bc-b22a-40313d5659ca</chapterId>


JavaScript okruženja kao što je NodeJS obično tretiraju svaku JavaScript datoteku kao poseban modul.


Zamislite modul kao kutiju. Kutija ima svoj privatni prostor, tako da promenljive i funkcije koje ste u njoj deklarisali ne ometaju kod u drugim kutijama. U suštini, svaki modul ima svoj opseg.


Modul može da izvozi deo svog sadržaja, čineći ga dostupnim drugim modulima, i može da uvozi sadržaj koji su drugi moduli izvezli. JavaScript omogućava izvoz i uvoz sadržaja između modula, kako bi se povezali različiti fajlovi.


JavaScript program je često sastavljen od više modula, koji su međusobno povezani.


Zašto koristiti module? Deljenjem vašeg koda na module, možete organizovati vaš program u manje, jasnije i ponovo upotrebljive delove. Svaki modul može se fokusirati samo na jednu vrstu zadatka, kao što je rukovanje matematičkim proračunima, rad sa fajlovima ili formatiranje teksta.


### CommonJS moduli


U NodeJS-u, najčešći sistem za upravljanje modulima zove se **CommonJS**.


U ovom sistemu, možete deliti (izvoziti) kod iz modula koristeći `module.exports` i učitati (uvoziti) ga u drugu datoteku koristeći `require()`.


Da biste nešto učinili dostupnim izvan modula, dodelite to `module.exports`:


```javascript
const greeting = "Hello!"

module.exports = greeting
```


Ovde, niz `"Hello!"` je ono što ovaj modul izvozi.


Da biste koristili izvezeni kod iz druge datoteke, koristite funkciju `require()` sa putanjom do te datoteke:


```javascript
const greeting = require("./greeting.js")

console.log(greeting)
```


Ovo štampa:


```
Hello!
```


Možete izvesti više stvari tako što ćete ih spojiti u anonimni objekat, kao


```javascript
const greeting1 = "hello"

const greeting2 = "hi"

module.exports = {
greeting1, greeting2
}
```


CommonJS je bio sistem modula koji je inicijalno usvojen od strane NodeJS-a. Kasnije su dodati i ES moduli.


### ES moduli


NodeJS takođe podržava drugi tip modula nazvan **ES moduli**, koji su popularni u veb razvoju. Oni koriste ključne reči `export` i `import`.


ES moduli su razvijeni za pregledač i tek kasnije dodati u Node. Ako želite da ih koristite, možda ćete morati koristiti `.mjs` kao ekstenziju fajla umesto `.js`, u zavisnosti od verzije Node-a koju koristite.


U jednoj datoteci nazvanoj `greeting.mjs` pišemo


```javascript
export const greeting = "Hello!"
```

Kao što možete videti, izvozimo konstantu direktno tamo gde je definisana.


U drugoj datoteci pod nazivom `index.mjs`, uvozimo ga:


```javascript
import { greeting } from "./greeting.mjs"

console.log(greeting)
```


Možete izvesti različite deklaracije u različitim delovima fajla, kao


```javascript
export const num = 10

export function double (x) {
return x*2
}
```


### NodeJS standardna biblioteka


NodeJS takođe uključuje mnoge ugrađene module. Ovo su gotovi moduli koje pruža NodeJS i koji pomažu sa uobičajenim zadacima kao što su čitanje fajlova, rad sa operativnim sistemom ili povezivanje na mrežu.


Na primer, modul `os` vam daje informacije o vašem operativnom sistemu:


```javascript
const os = require("os")

console.log(os.platform())
```


Ne morate instalirati ove ugrađene module, oni dolaze sa NodeJS-om. Oni čine "standardnu biblioteku" okruženja za izvršavanje i koriste ih većina Node aplikacija za obavljanje zadataka kao što su čitanje datoteka ili komunikacija putem interneta.


Sledeća poglavlja će vam pokazati neke korisne primere njihove upotrebe.


## Modul `fs`

<chapterId>911e953a-35ae-5ee7-bd74-372501c32e81</chapterId>


Modul `fs` (skraćeno za **file system**) je deo standardne biblioteke NodeJS-a. Omogućava vam rad sa fajlovima i direktorijumima na vašem računaru: možete čitati fajlove, pisati fajlove, brisati ih, preimenovati ih i još mnogo toga.


Da biste ga koristili, prvo ga morate uvesti na vrh vaše datoteke:


```javascript
const fs = require("fs")
```


### Sync API


Najjednostavniji način korišćenja `fs` je sa njegovim **sync** metodama.


Ove metode blokiraju program dok se ne završe (tako da sledeća linija koda ne radi dok operacija nije završena).


Evo primer čitanja datoteke sinhrono:


```javascript
const fs = require("fs")

const data = fs.readFileSync("example.txt", "utf8")

console.log(data)
```


Ako postoji datoteka pod nazivom `example.txt` u istom direktorijumu kao vaš skript, ovo će ispisati njen sadržaj.


Takođe možete pisati u datoteku sinhrono:


```javascript
const fs = require("fs")

fs.writeFileSync("output.txt", "Hello from Node!")

console.log("File written!")
```


Ovo kreira (ili prepisuje) fajl pod nazivom `output.txt` sa tekstom.


Evo nekoliko uobičajenih operacija koje možete izvršiti pomoću ovog API-ja:


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


Sync API je jednostavan i dobar za male skripte, ali zato što blokira program dok se ne završi, može usporiti stvari ako radite sa velikim fajlovima ili serverom.


### Povratni poziv asinhroni API


**Callback API** je neblokirajući: omogućava NodeJS-u da nastavi sa drugim radnjama dok se operacija nad fajlom odvija.


Umesto da direktno vrati rezultat, uzima funkciju (**povratni poziv**) koja se poziva kada je operacija završena.


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


Evo šta se dešava:



- `fs.readFile` počinje čitati `example.txt`.
- NodeJS ne čeka, već prelazi na izvršavanje drugog koda koji ste možda napisali.
- Kada se datoteka završi sa čitanjem, pokreće se povratni poziv:



  - Ako je došlo do greške, `err` sadrži grešku.
  - Inače, `data` sadrži sadržaj.


Evo kako se piše u datoteku:


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


Ista ideja: program ne prestaje dok piše datoteku.


Neki primeri stvari koje možete uraditi sa ovim API-jem:


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


Callback API je bolji za servere i velike zadatke jer ne blokira program, ali ugnježđeni povratni pozivi mogu postati neuredni ako povežete mnogo operacija. Zato je dodat asinhroni API zasnovan na obećanjima.


### Obećaj asinhroni API


API zasnovan na Promise je moderan i odlično funkcioniše sa `.then()` i `async/await`. Dostupan je kao `fs.promises`.


Morate da uvezete svojstvo `promises`:


```javascript
const fs = require("fs").promises
```


Korišćenje `.then()`:


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


Ili još bolje, koristeći `async/await`:


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


Pisanje u datoteku:


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


Uobičajena lista primera za API:


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


Kada pišete kod, često ćete morati koristiti kod koji su napisali drugi ljudi; na primer, biblioteke koje vam pomažu da radite sa datumima, bojama, serverima ili gotovo bilo čim drugim.


Umesto preuzimanja i kopiranja fajlova ručno, možete koristiti **package manager**.


Upravitelj paketa je alat koji:



- preuzimanja paketa
- prati koji paketi su potrebni vašem projektu
- osigurava da svi u vašem timu imaju iste verzije paketa


### Šta je NPM


U NodeJS svetu, najpopularniji upravitelj paketa je **NPM**, što znači *Node Package Manager*.


NPM dobijate automatski kada instalirate NodeJS.


Možete proveriti da li imate NPM pokretanjem ovoga u vašem terminalu:


```
npm -v
```


Ovo ispisuje verziju NPM-a koju imate, kao:


```
10.2.1
```


### Kreiranje paketa


U NodeJS-u, **paket** je samo direktorijum sa `package.json` fajlom u njemu.


Hajde da napravimo jedan korak po korak.


1. Napravite novi folder za vaš projekat:


```
mkdir my_project
cd my_project
```


2. Pokreni ovu komandu:


```
npm init
```


Ovo pokreće interaktivno podešavanje, postavljajući vam pitanja kao što su ime vašeg projekta, verzija, opis, itd.


Ako ne želite da odgovorite na sve i samo prihvatite podrazumevane vrednosti, možete koristiti:


```
npm init -y
```


Nakon pokretanja, videćete novu datoteku u vašem folderu pod nazivom:


```
package.json
```


### `package.json`


Datoteka `package.json` je samo JSON datoteka koja čuva metapodatke o vašem projektu.


Evo primer:


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


Nekoliko važnih polja:



- `name`: ime vašeg paketa
- `version`: trenutna verzija
- `main`: ulazna tačka fajl (kao `index.js`)
- `scripts`: komande koje možete pokrenuti (kao `npm start`)
- `dependencies`: navodi sve pakete od kojih vaš projekat zavisi


### Instaliranje paketa


Recimo da želite koristiti određeni paket pod nazivom `picocolors` za dodavanje boja vašem terminalskom izlazu.


Možete ga instalirati pokretanjem:


```
npm install picocolors
```


Sada ga možete koristiti u svom projektu. Napravite datoteku `index.js` sa


```javascript
const pico = require('picocolors')

console.log(
pico.green("This text is green!")
)
```


i pokušajte da ga pokrenete. Terminal bi trebalo da prikaže obojenu verziju teksta.


Šta je NPM uradio?



- Preuzeo je paket i sačuvao ga u podfolderu pod nazivom `node_modules/`
- dodao je unos pod `dependencies` u vašem `package.json`
- ažurirao je datoteku `package-lock.json`


Šta je `package-lock.json`?


### `package-lock.json`


Ovu datoteku automatski kreira NPM.


Možda se pitate, ako već imamo `package.json`, zašto nam treba još jedan fajl?

Evo razloga:



- `package.json` samo kaže koji **opseg** verzija paketa vaš projekat zahteva.

Primer:


```json
"dependencies": {
"picocolors": "^1.1.0"
}
```


`^1.1.0` znači „bilo koja verzija koja je kompatibilna sa 1.1.x“, tako da je fleksibilno.



- Datoteka `package-lock.json` **zamrzava** tačne verzije svakog paketa i njihovih podzavisnosti, tako da svako ko instalira vaš projekat dobija potpuno isto radno okruženje.


Zašto je ovo važno?


Ako radite u timu, ili postavljate svoj projekat na server, ili mu se vratite u budućnosti, želite da budete sigurni da i dalje funkcioniše na isti način.

Ako su paketi ažurirani i ponovo instalirate bez lock datoteke, možete dobiti malo drugačiju verziju koja se ponaša drugačije.


Čuvanjem datoteke `package-lock.json` u vašem projektu, NPM će uvek instalirati tačne verzije navedene u njoj, osiguravajući da svi imaju isto okruženje.


`package-lock.json` zaključava sve na vrlo specifičnu verziju, kako bi projekat bio lakše reprodukovan na drugim mašinama.


Ali ako vaš paket treba da koristi mnogo ljudi, možda ćete odlučiti da ga ne komitujete, tako da NPM pronađe samo datoteku `package.json` i dozvoljeno mu je da automatski instalira najnovije verzije koje su dozvoljene u toj datoteci.


Ali ovo su stvari o kojima treba da brinete kasnije, kada počnete da objavljujete svoj kod. Za sada smo uveli osnove NPM-a samo da bismo vam omogućili da pronađete i koristite biblioteke koje su objavili drugi programeri u vašim projektima.



## Umrežavanje u NodeJS

<chapterId>f2cabd8b-754b-5c97-8d6a-8412a9a184c7</chapterId>


NodeJS se često koristi kao jezik za backend: možete pretvoriti svoj skript u server, a takođe ga koristiti za slanje zahteva drugim serverima.


U ovom poglavlju ćemo predstaviti neke osnovne mrežne funkcije koje će vam to omogućiti.


### `fetch()`


Ako želite da vaš program preuzme podatke sa veb-sajta ili API-ja, potrebno je da napravite **HTTP zahtev**.


U modernim verzijama NodeJS-a, možete koristiti ugrađenu funkciju `fetch()`.


Evo primera kako napraviti GET zahtev ka API-ju:


```javascript
const response = await fetch("https://jsonplaceholder.typicode.com/posts/1")
const data = await response.text()

console.log(data)
```


Kada pokrenete ovo, videćete nešto poput:


```
{
"userId": 1,
"id": 1,
"title": "...",
"body": "..."
}
```


Evo šta se dešava:


1. `fetch()` uzima URL i pravi zahtev.

2. Vraća **Promise** koji se rešava u objekat tipa `Response`.

3. `response.text()` čita telo odgovora kao string.


Ali niz koji dobiješ nazad je zapravo JSON. Šta je to?


### JSON


Kada radite sa web API-jima, podaci se često šalju i primaju kao **JSON**, što je skraćenica za JavaScript Object Notation.


JSON je samo tekstualni format koji veoma liči na JavaScript objekte. Na primer:


```json
{
"name": "Alice",
"age": 30,
"likes": ["apples", "bananas"]
}
```


`JSON` objekat je ugrađeni alat u JavaScriptu koji se može koristiti za rad sa ovim formatom podataka.


Možete konvertovati JavaScript objekat u JSON string koristeći `JSON.stringify()`:


```javascript
const user = { name: "Alice", age: 30 }

const jsonString = JSON.stringify(user)

console.log(jsonString)
```


Ovo štampa:


```
{"name":"Alice","age":30}
```


Takođe možete konvertovati JSON tekst nazad u JavaScript objekat koristeći `JSON.parse()`:


```javascript
const jsonText = '{"name":"Bob","age":25}'

const obj = JSON.parse(jsonText)

console.log(obj)
```


Ovo štampa:


```
{ name: 'Bob', age: 25 }
```


Budite pažljivi: `JSON.parse()` će baciti grešku ako string nije validan JSON.


```javascript
JSON.parse("not json") // ❌ Error!
```


Dakle, uverite se da je string pravilno formatiran.


### `http` server


NodeJS vam omogućava da kreirate veb server bez instaliranja bilo čega drugog.


Možete koristiti ugrađeni modul `http` za obradu zahteva od klijenata i slanje odgovora nazad.


Evo vrlo osnovnog primera:


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


Kada pokrenete ovaj skript i otvorite `http://localhost:3000` u svom pregledaču, videćete:


```
Hello from NodeJS server!
```


Ovo se dešava u kodu:


1. Uvezli ste `http` server iz Node standardne biblioteke.

2. `http.createServer()` kreira server. Prosledili ste `http.createServer()` povratni poziv `(req, res) => {...}` koji će se izvršiti svaki put kada se neko poveže.

3. Dodelili ste status kod 200 (što označava uspešnu operaciju) odgovoru. Možete pročitati o http status kodovima [ovde](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

3. `res.end()` šalje odgovor i završava vezu.

4. `server.listen(3000)` pokreće server na portu 3000.


Takođe možete proveriti `req.url` i `req.method` u zahtevu kako biste obradili različite putanje ili tipove zahteva.


Primer sa usmeravanjem:


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


Ovo su veoma osnovni primeri. Za izgradnju naprednijih servera, većina programera bi verovatno preuzela gotovu biblioteku za backend kao što je [express](https://www.npmjs.com/package/express).


## Obrada podataka: baferi, događaji, tokovi

<chapterId>8c9623f0-a604-51a4-8fe4-871c849d3e3b</chapterId>


U ovom poglavlju ćemo predstaviti prvenstveno tri klase objekata:



- `Buffer`, koji predstavlja male delove binarnih podataka
- `EventEmitter`, koji se može koristiti za praćenje nekog koraka asinhronog procesa emitovanjem signala nazvanih "događaji"
- `Stream`, koji nam omogućava da obradimo veliki deo podataka jedan po jedan `Buffer`, i koji prati proces emitovanjem događaja


Ovo su izuzetno česti u profesionalnom NodeJS kodu, tako da čak i ako ih možda nećete koristiti u svojim prvim projektima, dobro je steći osnovno razumevanje za trenutak kada ćete morati da radite sa njima.


### Baferi


U NodeJS-u, **bafer** je tip objekta koji se koristi za rad sa binarnim podacima.


Možete misliti o baferu kao o kontejneru fiksne veličine za sirove bajtove.


Evo kako da kreirate bafer iz stringa:


```javascript
const buf = Buffer.from("hello")
console.log(buf)
```


Ovo štampa nešto kao:


```
<Buffer 68 65 6c 6c 6f>
```


Ti brojevi (`68`, `65`, `6c`, itd.) su heksadecimalni prikazi slova u reči `"hello"`.


Možete ga ponovo pretvoriti u string ovako:


```javascript
console.log(buf.toString())
```


Ovo štampa:


```
hello
```


Takođe možete kreirati bafer određene veličine ispunjen nulama:


```javascript
const buf = Buffer.alloc(10)
console.log(buf)
```


Ovo ispisuje nešto poput:


```
<Buffer 00 00 00 00 00 00 00 00 00 00>
```


Možete pisati u bafer:


```javascript
buf.write("abc")
console.log(buf)
```


I možete pristupiti pojedinačnim bajtovima:


```javascript
console.log(buf[0]) // prints the ASCII number for 'a', which is 97
```


Baferi su posebno korisni kada treba da manipulišete podacima na veoma niskom nivou.


### Događaji


U JavaScript-u, **događaj** je nešto što se dešava u vašem programu na šta možete reagovati.


Na primer:



- datoteka je završila učitavanje
- tajmer se uključuje
- korisnik klikne dugme
- mreža vraća podatke


**Događaj** je samo signal da se nešto dogodilo, i možete napisati kod da osluškuje te događaje i reaguje na njih.


U NodeJS-u, mnogi objekti mogu emitovati događaje. Ovi objekti se nazivaju **EventEmitters**.


Evo primer:


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


Ovo štampa:


```
Hello! An event happened.
```


Evo šta:


1. Kreiramo objekat `EventEmitter`.

2. Kažemo mu da pokrene povratni poziv kad god se dogodi događaj `"greet"`, koristeći `.on("greet")`.

3. Kasnije, pokrećemo događaj `"greet"` koristeći `.emit()`.

4. Naš povratni poziv se izvršava


Možete proslediti podatke zajedno sa događajem:


```javascript
emitter.on("greet",
(name) => console.log(`Hello, ${name}!`)
)

emitter.emit("greet", "Alice") // first argument is the type of event, second argument is the data we pass with this event
```


Ovo štampa:


```
Hello, Alice!
```


Možete registrovati osluškivače i za druge događaje:


```javascript
emitter.on("goodbye", () => {
console.log("Goodbye!")
})

emitter.emit("goodbye")
```


Možete prikačiti onoliko slušalaca koliko želite na jednu vrstu događaja, i možete pokrenuti mnogo različitih vrsta događaja iz istog emita.


Mnogi objekti u NodeJS emituju događaje kako bi obavestili ostatak programa da se nešto dešava.



### Šta su tokovi?


Streamovi kombinuju bafer i događaje kako bi nam pomogli u obradi podataka.


Kada radimo sa fajlovima, podacima sa mreže ili čak dugim tekstom, ne moramo (niti želimo) da učitamo sve u memoriju odjednom. To može biti sporo, ili čak srušiti program ako su podaci preveliki.


Umesto toga, možemo obrađivati podatke **malo po malo**, kako stižu ili se čitaju, slično kao što pijemo vodu kroz slamku umesto da pokušavamo da popijemo celu čašu odjednom. Ovo se zove **tok**.


U NodeJS-u, tok je objekat koji vam omogućava da čitate podatke iz izvora ili pišete podatke na odredište **jedan po jedan deo**.


NodeJS ima četiri glavne vrste tokova:



- Čitljivi**: tokovi iz kojih možete čitati podatke (kao čitanje datoteke)
- Zapisivi**: tokovi u koje možete upisivati podatke (kao što je upisivanje u datoteku)
- Duplex**: tokovi koji su i čitljivi i upisivi
- Transform**: kao dupleks strimovi, ali mogu menjati (transformisati) podatke dok teku


### Čitljivi tokovi


Recimo da imate `bigfile.txt` za obradu. Možete kreirati čitljiv tok sa `fs` modulom da biste čitali fajl deo po deo.


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


Šta se ovde dešava?


1. `fs.createReadStream()` kreira čitajući tok.

2. Kad god je deo fajla spreman, tok emituje događaj `data` i daje nam "komad" podataka (`Buffer`). Ispisujemo taj komad.

3. Kada je cela datoteka pročitana, `end` događaj se pokreće.

4. Ako dođe do greške (kao što je nepostojanje datoteke), `error` događaj se pokreće.


Na ovaj način, možete čitati ogromne datoteke bez učitavanja svih u memoriju odjednom.


Ako želimo da podaci stignu u obliku čitljivom za ljude (umesto u binarnom obliku), možemo odrediti kodiranje toka:


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


Kod će sada štampati datoteku u formi koja je čitljiva za ljude.


### Tokovi za pisanje


Upisivi tok vam omogućava da šaljete podatke negde, deo po deo.


Evo primer pisanja u datoteku `target.txt` koristeći tok:


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


Evo šta se dešava:


1. `fs.createWriteStream()` kreira tok za pisanje.

2. Napišemo neki tekst u njega koristeći `.write()`.

3. Kada završimo, pozivamo `.end()` da zatvorimo tok.

4. Kada su svi podaci zapisani, emituje se događaj `finish`.

5. Ako nešto pođe po zlu, `error` događaj se pokreće.


Baš kao i čitljivi tokovi, tokovi za pisanje su dobri za velike podatke jer ne moraju sve držati u memoriji odjednom.


### Prenos tokova


Jedna od najzanimljivijih stvari kod tokova je da ih možete **povezati** zajedno: povezati tok za čitanje direktno sa tokom za pisanje.


```javascript
const fs = require("fs")

const readable = fs.createReadStream("bigfile.txt")
const writable = fs.createWriteStream("target.txt")

readable.pipe(writable)
```


Ovde:



- Čitljivi tok čita iz `bigfile.txt`.
- Tok pisanja piše u `copy.txt`.
- `.pipe()` šalje podatke direktno iz čitljivog u upisivi tok.


### Duplex tokovi


Duplex tok je i čitljiv i upisiv. Jedan primer je mrežni soket: možete slati podatke ka njemu i primati podatke od njega.


Evo vrlo jednostavan primer korišćenja `net` modula:


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


U ovom primeru:



- Objekat `socket` je duplexni tok.
- Možete da koristite `write()` za pisanje i takođe da osluškujete `data` događaje iz njega.


### Transformiši tokove


Transform stream je dupleksni tok koji takođe modifikuje podatke koji prolaze kroz njega.


Na primer, možete koristiti ugrađeni modul `zlib` za kompresiju ili dekompresiju podataka.


Evo kako da kompresujete fajl koristeći transform stream:


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


I da ga dekompresujete nazad:


```javascript
const readable = fs.createReadStream("bigfile.txt.gz")
const unzip = zlib.createGunzip()
const writable = fs.createWriteStream("bigfile.txt")

readable.pipe(unzip).pipe(writable)

writable.on("finish", () => {
console.log("File decompressed.")
})
```


Transform streamovi su veoma korisni za zadatke kao što su kompresija, enkripcija ili promena formata fajlova tokom strimovanja.


### Pritisak unazad


Ponekad je tok za pisanje spor u obradi podataka. Ako nastavimo da šaljemo podatke u tok za pisanje brže nego što on može da ih obradi, možemo naići na probleme. Ovo se zove **backpressure**.


Ako pozovete metodu `.write()` na upisivom toku, ona vraća boolean koji vas obaveštava da li je toku potrebna pauza; možda ćete morati da proverite njenu povratnu vrednost, ovako:


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


Ovo je bio ilustrativni primer ručnog preusmeravanja podataka iz Readable u Writable, i ručnog upravljanja povratnim pritiskom.


Obično bismo prosleđivali podatke koristeći metodu `.pipe()`, koja automatski upravlja povratnim pritiskom.


Dakle, treba da brinete o backpressure samo kada iz nekog razloga ručno pozivate `.write()`.


## Konačna beleška

<chapterId>139e2ab8-df67-525a-85f0-5a2fa5e478f2</chapterId>


Dakle, to je to, ako ste pratili lekcije, sada biste trebali biti u mogućnosti da napišete neke jednostavne programe u NodeJS-u.


Predlažem da uradite upravo to: nakon što naučite osnove, izgradnja nekoliko ličnih projekata je najbolji način da vežbate i postanete bolji programer.


Nije važno šta gradiš, važno je da izazoveš sebe da rešavaš probleme pomoću koda.


Moderni programski jezici su neverovatno moćni, a NodeJS je verovatno najbolji alat za eksperimentisanje u ovoj fazi vašeg putovanja.


Srećno!


# Završni deo


<partId>322624d8-6fbc-11f0-a67a-5b145f10afc1</partId>


## Recenzije i Ocene


<chapterId>3e93ac86-6fbc-11f0-8bae-9b2ed7914843</chapterId>

<isCourseReview>true</isCourseReview>

## Zaključak


<chapterId>49b3b9b2-6fbc-11f0-9870-5f5adcd3a0eb</chapterId>


<isCourseConclusion>true</isCourseConclusion>