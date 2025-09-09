---
name: JavaScript ja NodeJS alused
goal: Õppige JavaScript programmeerimise põhitõdesid ja NodeJSi arendamist, et luua praktilisi rakendusi ja tööriistu.
objectives: 

  - JavaScripti põhilise süntaksi, tüüpide ja kontrollivoogude omandamine
  - JavaScript'i funktsioonide, objektide ja klasside mõistmine
  - Õppige veakäitlus- ja veaotsingumeetodeid
  - Tutvuge NodeJS-i ja selle ökosüsteemiga

---

# Alusta oma arenguteekonda


Tere tulemast sellele JavaScript ja NodeJS kursusele.


JavaScript on maailma kõige populaarsem programmeerimiskeel: see on kaasaegsete brauserite skriptikeel, nii et põhimõtteliselt on võimatu luua kaasaegset veebirakendust ilma *jagu* JavaScript'i kirjutamata; ja NodeJSi käivitamisajaga saab seda kasutada ka väljaspool brausereid, et luua skripte ja rakendusi, mis töötavad otse teie arvutis.


See kursus on mõeldud inimestele, kes on programmeerimisega täiesti algajad või kes on varem kasutanud teisi keeli, kuid soovivad mõista, kuidas JavaScript töötab, eriti NodeJSi kontekstis.


Kursuse lõpuks peaksite olema võimeline kirjutama oma programme JavaScriptis, kasutama NodeJSi standardraamatukogu ning paigaldama ja kasutama kolmandate osapoolte pakette, et luua kasulikke tööriistu.


+++
# Põhiline JavaScript

<partId>a617327c-e5a2-52ca-9380-c63f44623dd4</partId>


## Seadistamine

<chapterId>ba05a290-1782-5268-87c9-62fd09590e05</chapterId>


Selles jaotises seadistame oma masina, et kirjutada ja käivitada meie esimene JavaScript programm.


JavaScript-programm on lihtsalt (ühe või mitme) tekstifaili kogum, mis sisaldab käske, mida JavaScripti tööprogramm täidab.


Nende tekstifailide nimed lõppevad tavaliselt faililaiendiga `.js`, näiteks `my_script.js`, `my_program.js` jne.


Neis sisalduvad käsud on kirjutatud JavaScript programmeerimiskeeles.


JavaScripti runtime on spetsiaalne programm, mis täidab neid faile.


![](assets/en/1.webp)


### NodeJS-i paigaldamine


Kõige tavalisem JavaScripti tööaeg on NodeJS.


Saate selle paigaldada, järgides [ametlikke juhiseid](https://nodejs.org/en/download).


Allalaadimislehelt leiate juhised kõigi kolme peamise operatsioonisüsteemi (operatsioonisüsteemi) jaoks: Windows, Linux ja MacOS. See eeldab, et te teate, kuidas oma operatsioonisüsteemis terminali avada.


Kuna NodeJS on saadaval kõigile kolmele operatsioonisüsteemile, saab teie kirjutatud programme kõigis neis käivitada (välja arvatud mõned äärmuslikud juhtumid).


See tähendab, et saate näiteks kirjutada lihtsa videomängu JavaScriptis oma Windows-arvutis ja anda selle oma sõbrale edasi, et ta seda oma Macil jooksutaks.


![](assets/en/2.webp)


### Teksti redigeerimine


Programmeerimise üks lahedamaid asju on see, et koodi saab kirjutada mis tahes tekstiredaktoriga, isegi oma operatsioonisüsteemi vaikimisi märkmikuga.


Siiski on olemas mõned tekstiredaktorid, mis on spetsialiseerunud koodi kirjutamisele, mõned on saadaval tasuta, teised nõuavad litsentsi eest maksmist.


Koodiredaktori valik on hiiglaslik jänesepesa, mis ületab selle kursuse ulatuse, nii et me ei räägi sellest siinkohal. Kui te ei tea, mida kasutada, siis kõige enam kasutatav tasuta toimetaja on [VSCode](https://code.visualstudio.com/).


Selle Interface on pisut paisutatud, kuid selles on kõik vajalik: failiredaktor, failiotsinguprogramm (failide ja alamkataloogide visualiseerimiseks kataloogis, kus te töötate) ja terminal oma koodi käivitamiseks. Samuti toetab see palju pluginaid ja on vaikimisi varustatud JavaScripti süntaksi esiletõstmisega.


Kui soovite olla veidi rohkem Cypherpunk-y, võite selle asemel kasutada [VSCodium](https://vscodium.com/).


### Esimene programm (hello world)


Traditsiooniliselt seisneb programmeerimiskeele õppimisel esimene programm, mille inimene kirjutab, selles, et ta trükib konsooli "hello world!".


Loo kataloog nimega `my_js_code/`, mille sees on fail nimega `main.js` (need nimed on suvalised).


Avage kataloog VSCode'iga.


Kirjutage see kood oma faili:


```javascript
console.log("hello world!")
```


Avage terminal ja käivitage see käsk, et käivitada programm:


```
node main.js
```


Tulemuseks peaks olema


```
hello world!
```


### Mis juhtus


JavaScriptis on kõik "objekt".


`console` on objekt, mida kasutatakse programmi silumiseks.


`console.log` on kõige enam kasutatav meetod `console`. See lihtsalt prindib kõik argumendid, mis te talle üle annate.


Argumendid edastate `console.log`ile, kasutades ümarsulgureid `()`.


Näiteks, kui soovite printida arvu `1000`, siis kirjutage lihtsalt


```javascript
console.log(1000)
```


Seejärel käivitage see, käivitades


```
node main.js
```


oma terminalis (edaspidi eeldatakse, et te teate, et nii käivitate programmi).


See peaks printima


```
1000
```


Saate edastada mitu asja, näiteks


```javascript
console.log(16, 8, 1993)
```


See prindib


```
16 8 1993
```


## Muutujad ja kommentaarid

<chapterId>23050ab7-343b-5edf-9d37-e4e782e27ce0</chapterId>


Programmid teostavad tavaliselt operatsioone andmetega.


Muutujad on nagu nimelised kastid, mida me kasutame andmete salvestamiseks. Need võimaldavad meil seostada andmeid konkreetse nimega, et saaksime neid hiljem selle nime abil välja otsida.


### `let` deklaratsioonid


Muutuja deklareerimiseks JavaScriptis võime kasutada võtmesõna `let`.


Pärast `let` kirjutamist kirjutame nime, mille soovime muutujale anda, seejärel `=` märgi ja seejärel väärtuse, mida soovime salvestada.


Näiteks:


```javascript
let age = 25

console.log(age)
```


Muutuja nimi (tehniliselt nimetatakse seda "identifikaatoriks") võib tavaliselt sisaldada tähti, alatähti (`_`), dollarimärki (`$`) ja numbreid, kuigi esimene märk ei tohi olla number.


Ülaltoodud koodis deklareerisime muutuja nimega "age" ja salvestasime sellesse väärtuse "25".


Seejärel printisime väärtuse, kasutades `console.log(age)`.


Kui käivitate selle koodi koos `node main.js`, siis on väljundiks:


```
25
```


Identifikaatorid on suur- ja väiketähtedest sõltuvad, mis tähendab, et identifikaatorite erinevusteks on väike- ja suurtähtedest, nii et näiteks


```javascript
let age = 25

let Age = 20

console.log(age)
```


trükib 25, sest neid peetakse kaheks täiesti eraldi muutujaks!


Muutujasse saab salvestada ka stringi (teksti):


```javascript
let message = "hello again"

console.log(message)
```


See trükib:


```
hello again
```


Nagu varemgi, kasutasime muutujasse salvestatud väärtuse printimiseks `console.log()`.


Nüüd teeme mõlemat koos:


```javascript
let age = 25

let message = "hello again"

console.log(age)

console.log(message)
```


Selle käivitamine trükib:


```
25
hello again
```

### Ümberpaigutamine


Muutujaid, mis on deklareeritud `let`ga, saab pärast nende loomist muuta.


Seda nimetatakse ümberpaigutamiseks.


```javascript
let score = 10

console.log(score)

score = 15

console.log(score)
```


Esmalt määrame `10` punktile `score`, seejärel trükime selle välja.


Seejärel muudame väärtuse `score` väärtuseks `15` ja trükime selle uuesti välja.


Väljundiks on:


```
10
15
```


See on väga kasulik, kui väärtus muutub aja jooksul, näiteks mängus, kus skoor suureneb.


Lisame siia veel ühe muutuja:


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


See trükib:


```
10
Alice
20
Bob
```


Nagu näete, muudeti nii `score` kui ka `player`.


### `const` deklaratsioonid


Enamasti ei taha me aga, et muutuja muutuks pärast selle loomist. Selleks kasutame `const`.


`const` on lühend sõnast "konstant". Kui olete kord muutujale `const` väärtuse määranud, ei saa te seda enam muuta.


```javascript
const pi = 3.14
console.log(pi)
```


See trükib:


```
3.14
```


Aga kui sa üritad seda teha:


```javascript
const pi = 3.14
console.log(pi)

pi = 99 // this line will cause an error
console.log(pi)
```


JavaScript annab teile sellise vea nagu:


```
TypeError: Assignment to constant variable.
```


Selle põhjuseks on see, et `pi` on deklareeritud kasutades `const` ja selle väärtust ei saa pärast seda muuta. Te edastate JavaScripti interpretaatorile, et te ei soovi, et see muutuja muutuks.


See on kasulik, sest see vähendab võimalust seda kogemata muuta. Kui programmid muutuvad väga suureks, tuhandete koodiridadega, on võimatu jälgida kõike korraga toimuvat (see on peamine põhjus, miks me kasutame arvuteid, et täita keerulisi protsesse, mida me ei suuda oma ajuga arvutada), seega on kasulik, kui on olemas sellised piirangud, mis muudavad programmi deterministlikumaks.


Parimaks tavaks on alati deklareerida meie väärtused `const`, välja arvatud juhul, kui me oleme kindlad, et tahame neid hiljem muuta.


### Kommentaarid JavaScriptis


Mõnikord tahame oma koodis kirjutada märkmeid, mida ei täideta. Neid nimetatakse kommentaarideks.


Kommentaarid jäetakse programmi käivitamisel tähelepanuta, kuid need on kasulikud, et selgitada asju endale või teistele inimestele.


Ühe rea pikkuse kommentaari kirjutamiseks kasutage `//`


```javascript
// This is a comment
const x = 10 // This is also a comment
console.log(x)
```


See trükitakse ikka veel välja:


```
10
```


Kommentaarid on lihtsalt selleks, et inimesed saaksid neid lugeda.


Saate kirjutada ka mitmerealisi kommentaare, kasutades `/*` ja `*/`


```javascript
/*
This is a multi-line comment.
It can span several lines.
*/
const y = 20
console.log(y)
```


See prindib


```
20
```


Ja seda kommentaari ignoreeritakse.


Sa võid kasutada kommentaare, et lisada oma koodile väikseid märkusi, et sa mäletaksid, mida see teeb ja miks see on kirjutatud teatud viisil. See võib aidata ka teistel programmeerijatel sellest aru saada.


## Põhitüübid: numbrid, stringid, boolused

<chapterId>cfdb04f6-21a8-5143-bbf9-7aaae04962f0</chapterId>


JavaScriptis ütleb "tüüp", mis liiki andmed on väärtus.


Javascriptil on mõned põhitüübid ja selles jaotises uurime mõningaid neist.


### Arvud ja aritmeetilised operatsioonid


Esimene tüüp, mida me tutvustame, on `number`.


JavaScriptis võivad arvud olla täisarvud (näiteks `5`) või kümnendarvud (näiteks `3.14`).


Nendega saab teha aritmeetikat: liitmine, lahutamine, korrutamine ja jagamine.


Siin on üks lihtne näide:


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


See trükib:


```
15
5
50
2
```


Samuti võite kasutada sulgusid `()`, et kontrollida operatsioonide järjekorda:


```javascript
const result = (2 + 3) * 4
console.log(result)
```


See trükib:


```
20
```


Ilma sulgudeta oleks see `2 + 3 * 4`, mis on:


```javascript
const result = 2 + 3 * 4
console.log(result)
```


See oleks trükitud:


```
14
```


Sest tavalises matemaatikas toimub korrutamine enne liitmist.


### Stringid ja interpolatsioon


Teine JavaScript tüüp, mida me tutvustame, on `string`.


Stringid on tekstiosad. Nende loomiseks võib kasutada lihtsaid jutumärke `"...'` või kahekordseid jutumärke `"..."`.


```javascript
const greeting = "hello"
const name = 'Bob'
console.log(greeting)
console.log(name)
```


See trükib:


```
hello
Bob
```


Stringide ühendamiseks saate kasutada operaatorit `+`:


```javascript
const greeting = "hello"
const space = " "
const name = "Bob"

const fullGreeting = greeting + space + name
console.log(fullGreeting)
```


See trükib:


```
hello Bob
```


Kuid stringide ühendamiseks on olemas kenam viis, mida nimetatakse **stringide interpolatsiooniks**. Te kasutate tagantjärgi, et deklareerida string `` `...`` ja kirjutate muutujaid kasutades `${...}` stringi sees:


```javascript
const greeting = "hello"
const name = "Bob"

const fullGreeting = `${greeting} ${name}`
console.log(fullGreeting)
```


See trükib ka:


```
hello Bob
```


Sa võid lisada mis tahes väljendi `${...}` sisse:


```javascript
const age = 30
console.log(`Next year, I will be ${age + 1} years old.`)
```


See trükib:


```
Next year, I will be 31 years old.
```


Interpolatsioon on kaasaegses JavaScriptis väga levinud.


### Boolused, võrdlus- ja loogikaoperatsioonid


Kolmas tüüp, mida me tutvustame, on `boolean`. See on nime saanud matemaatiku George Boole'i järgi, kes leiutas bool'i loogika.


Boolused on lihtsad: ainult kaks võimalikku väärtust, "õige" ja "vale".


Neid saab salvestada muutujatesse:


```javascript
const theSkyIsBlue = true
const thisCourseIsBad = false

console.log(theSkyIsBlue)
console.log(thisCourseIsBad)
```


See trükib:


```
true
false
```


Booluseid saab kombineerida loogiliste operaatorite abil:



- `&&` tähendab "ja" ja see tagastab `true` ainult siis, kui **kumbki** väärtus on `true`, vastasel juhul tagastab `false`
- `||` tähendab "või", ja see tagastab `truue`, kui **vähendalt üks** väärtustest on `truue`, vastasel juhul (kui mõlemad on false) tagastab `false`
- `!` tähendab "mitte", seda rakendatakse enne boolean'i ja see pöörab selle ümber: kui boolean on `true`, siis tagastab see `false` ja vastupidi.


![](assets/en/3.webp)


Näited:


```javascript
const isSunny = true
const isWarm = true

console.log(isSunny && isWarm)  // true
console.log(isSunny || isWarm)  // true
console.log(!isSunny)           // false
```


JavaScriptis saab väärtusi võrrelda, kasutades selliseid operaatoreid nagu `>`, `<`, `===` ja `!==`. Nende võrdluste tulemus on alati boolean.


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


Javascriptis on ka `>=`, mis tähendab "suurem või võrdne" ja `<=`, mis tähendab "väiksem või võrdne".


Booleans, võrdlus- ja loogilisi operaatoreid kombineeritakse programmides sageli keeruliste tingimuste deklareerimiseks, näiteks selleks, et tagada, et "e-kiri on saabunud JA see sisaldab vajalikku pilti VÕI e-kirja pikkus on pikem kui 10000 tähemärki". Hiljem leiate, et need on olulised ehituskivid programmi loogika ülesehitamiseks.


## Arrays, null, undefined

<chapterId>7bf18183-5eae-53ed-83d2-b04982145d81</chapterId>


Selles jaotises käsitleme veel kolme tüüpi, mis on JavaScript-programmides väga levinud:



- Arrays**: väärtuste jadad
- undefined**: eriväärtus, mis tähendab, et "midagi ei ole määratud"
- null**: teine eriväärtus, mis tähendab "tahtlikult tühi"


### Massiivid ja juurdepääs indeksitele


**Maastik** on tüüp, mis võib hoida mitut väärtust loendis.


Massiiv luuakse, kasutades nurksulgusid `[]` ja eraldades elemendid komadega.


Siin on üks lihtne näide:


```javascript
const numbers = [10, 2, 88]
console.log(numbers)
```


See trükib:


```
[ 10, 2, 88 ]
```


Massiivis saab salvestada mida tahes, mitte ainult numbreid:


```javascript
const things = ["apple", 42, true]
console.log(things)
```


See trükib:


```
[ 'apple', 42, true ]
```


Konkreetsele elemendile massiivis juurdepääsuks kasutame **indeksit**. Indeks on elemendi positsioon, alustades **0**.


Nii et selles massiivi:


```javascript
const colors = ["red", "green", "blue"]
```



- `colors[0]` on `"punane"`
- `colors[1]` on `"Green"`
- `colors[2]` on `"sinine"`


Proovime:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[0])
console.log(colors[1])
console.log(colors[2])
```


See trükib:


```
red
green
blue
```


Saate määrata väärtuse massiivi konkreetsele indeksile


```javascript
const colors = ["red", "green", "blue"]

colors[1] = "yellow"

console.log(colors)
```


See trükib:


```
[ 'red', 'yellow', 'blue' ]
```


Indeksina võib kasutada mis tahes loomulikku arvu, isegi muutujasse salvestatud numbrit


```javascript

const i = 1
const colors = ["red", "green", "blue"]
console.log(colors[i])
```


See trükib:


```
green
```


Kui aga üritate kasutada indeksit, mida ei ole olemas, saate tulemuseks `undefined`:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[3])
```


See trükib:


```
undefined
```


Mis see on?


### `undefined`


Eriväärtus `undefined` tähendab, et "väärtust ei ole määratud".


Kui te loote muutuja, kuid ei anna talle väärtust, siis on see "määratlemata":


```javascript
const name
console.log(name)
```


See trükib:


```
undefined
```


Kuna me ei määranud `nimele` midagi, seab JavaScript selle vaikimisi väärtuseks `undefined`.


Nagu varem nähtud, võite saada ka `undefined`, kui kasutate massiivi indeksit, mida ei ole olemas:


```javascript
const fruits = ["banana", "apple"]
console.log(fruits[2]) // There is no index 2
```


See trükib:


```
undefined
```


### `null` ja kuidas seda käsitleda


`null` on samuti eriline väärtus. See tähendab, et "siin ei ole midagi ja ma tegin seda meelega"


Erinevalt `undefined`, mis on automaatne, on `null` midagi, mida te ise määrate.


Näiteks:


```javascript
const currentUser = null
console.log(currentUser)
```


See trükib:


```
null
```


Miks kasutada `null`? Võib-olla ootate väärtust hiljem, kuid see ei ole veel valmis:


```javascript
let winner = null

// Later in the program:
winner = "Alice"

console.log(winner)
```


See trükib:


```
Alice
```


Nii et `null` on kasulik, kui soovite näiteks öelda: "Siin peaks hiljem midagi olema, aga praegu on see tühi."


## Blokid ja kontrollivool

<chapterId>be985168-2636-5b0d-a48f-ac1bbfbff8a7</chapterId>


Seni oleme enamasti kirjutanud koodiridu, mis käivituvad üksteise järel.


Aga kui me kodeerime, saame kontrollida selle täitmise järjekorda.


Seda nimetatakse **kontrollivooluks**.


Alustame plokkide ja ulatuse mõistmisest.


### Ülemaailmne reguleerimisala


Iga deklareeritud muutuja eksisteerib **skoopis**, mis tähendab koodi piirkonda, kus muutuja on teada.


Kui te deklareerite muutuja väljaspool mis tahes plokki, siis on see olemas **globaalses ulatuses**.


```javascript
const color = "blue"
console.log(color)
```


See muutuja `color` on globaalses ulatuses, nii et sellele on võimalik ligi pääseda ükskõik kust failist.


Kui lisate rohkem ridu:


```javascript
const color = "blue"
console.log(color)

const size = "large"
console.log(color)
console.log(size)
```


Nii `color` kui ka `size` on globaalsed muutujad. Nad on failis kõikjal kättesaadavad.


Aga mis juhtub ploki sees?


### Plokid ja kohalik ulatus


**blokk** on kooditükk, mis on ümbritsetud sulge "{}".


Muutujad, mis on ploki sees deklareeritud sõnadega `let` või `const`, eksisteerivad **ainult** selle ploki sees.


```javascript
{
const message = "inside block"
console.log(message)
}
```


See trükib:


```
inside block
```


Aga kui te proovite seda:


```javascript
{
const message = "inside block"
}
console.log(message) // Error!
```


JavaScript annab teile sellise vea nagu:


```
ReferenceError: message is not defined
```


Seda seetõttu, et `message` on deklareeritud ploki sees ja väljaspool seda ei eksisteeri.


See tähendab, et me saame kasutada plokke, et isoleerida oma koodi osi ja olla kindel, et "mis juhtub plokis, jääb plokki" (nagu Las Vegas).


Meie koodi organiseerimine plokkidesse võimaldab meil struktureerida ka programmi täitmist, kasutades kontrollivoolu konstruktsioone nagu `if`


### "kui", "kui


Mõnikord tahame käivitada koodi **ainult juhul**, kui midagi on tõene. Selleks ongi "kui" avaldis.


```javascript
const myAge = 20

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


See trükib:


```
Am I an adult?
Yes I am!
```


Nagu näete, võrdleb kood `myAge` ja `18`.

Sellisel juhul tagastab operaator `>=`true`, nii et plokk täidetakse.

Kui tingimus ei ole "tõene", siis plokki ei täideta.


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


See trükib:


```
Am I an adult?
```


Te võite lisada bloki `else`, et käsitleda vastupidist juhtumit:


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
} else {
console.log("No, I am not.")
}
```


See trükib:


```
Am I an adult?
No, I am not.
```


Nii `if` kui ka `else` plokid on ikkagi plokid - seega nende sees deklareeritud muutujad ei eksisteeri väljaspool.


Kui me tahame olla kindlad, et midagi ei ole **tõene**, mida me saame teha?


Noh, nagu eelnevalt mainitud, on JavaScriptil olemas operaator "not", mis keerab booleans'i ümber. Nii et me saame teha


```javascript
const myAge = 17

const adult = myAge >= 18

console.log("Am I an adult?")

if (!adult) {
console.log("No, I am not.")
}
```

See trükib ikka veel:


```
Am I an adult?
No, I am not.
```

Sest me kasutasime operaatorit `!`, et invertida muutuja `täiskasvanu`.


"if (!adult) {...}" tuleks lugeda kui "if not adult..."


Kasutades plokke, loogika- ja võrdlusoperaatoreid, saame struktureerida programmi täitmist, määratledes muutujaid, mis peavad olema "tõesed" (või "valed"), et midagi toimuks.


### `while`, `break`, `continue`, `continue`


"while" tsükkel kordab koodi *sellaliselt*, kui tingimus on tõene.


```javascript
let count = 0

while (count < 3) {
console.log("Count is", count)
count = count + 1
}
console.log("the loop is over!")
```


See trükib:


```
Count is 0
Count is 1
Count is 2
the loop is over!
```


Kui `count` saab 3, lõpetab tsükkel.


Loopi saab katkestada varakult, kasutades `break`:


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


See trükib:


```
0
1
2
```


Sest kui arv muutub arvuks "3", käivitub plokk "kui" ja see peatab tsükli.


Saate tsükli ülejäänud osa vahele jätta, kasutades `continue`:


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


See trükib:


```
1
2
4
5
```


Sest kui number oli `3`, siis `continue` pani programmi jätma vahele rea, mis trükkis numbri välja.


### "Sest ... of ..


Kui sul on massiivi ja sa tahad teha midagi iga elemendiga selles, võid kasutada `for ... of ... of ... {...}`.


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const fruit of fruits) {
console.log(fruit)
}
```


See trükib:


```
apple
banana
cherry
```

Plokk käivitatakse üks kord iga massiivi elemendi kohta.


`fruit` siin on uus muutuja, mis võtab iga elemendi väärtuse massiivi, et sellega ploki sees opereerida.


### "Sest ... aastal ..


Massiivi võtmete (indeksite) läbimiseks saab kasutada funktsiooni `for ... in`:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(index)
}
```


See trükib:


```
0
1
2
```


Saate kasutada indeksit ka väärtuse saamiseks:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(fruits[index])
}
```


See trükib sama, mis `for ... of`:


```
apple
banana
cherry
```


Praktikas peaksite massiivi puhul eelistama kasutada `for ... of`, kuna see on lihtsam ja puhtam.


### Piiratud silmused


Mõnikord tahame me teatud arvu kordi loopida või üldiselt kirjutada koodi, mis kordab plokki, jälgides samal ajal midagi.

Selleks ongi piiratud "for"-silmus hea.

Piiratud tsükkel võtab tavaliselt kolm tingimust, mis on eraldatud semikooloniga `;`, nagu näiteks `(... ; ... ; ....)`.


```javascript
for (let i = 0; i < 3; i = i + 1) {
console.log(i)
}
```


See trükib:


```
0
1
2
```


Selgitame seda:



- `let i = 0`: deklareerib muutuja, mida kasutatakse plokis (antud juhul on see loendur, mis algab 0-st)
- `i < 3`: deklareerib tingimuse, mis peab olema `tõene`, et plokki täidetaks ( antud juhul on "repeat while `i` is less than 3")
- `i = i + 1`: deklareerida mingi kood, mis käivitatakse pärast iga ploki täitmist (antud juhul "suurenda `i` 1 võrra")


Nagu näete, on piiratud tsükkel meil võimalik deklareerida keerulisemaid tingimusi koodi korduvaks täitmiseks, kuid enamasti ei ole see vajalik.


### Plokkide sildid


Kui teil on vaja kirjutada keerulisemat kontrollivoolu, võimaldab JavaScript teil nimetada plokki, kasutades **labelit**, mida saab kasutada `break` või `continue` abil, et määrata *kohta*, kuhu* tagasi hüpata.


Näide:


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


See trükib:


```
Inside outer block
Inside inner block
Done
```


Me kasutasime `break outer`, et täielikult väljuda `outer` plokist.


Saate ka silmuseid märgistada. Võtame selle näite:


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

See oli väga igav näide, kuid loodetavasti selgitas see (aeg-ajalt) märgistamise vajadust.


## Funktsioonide tutvustamine

<chapterId>cc324715-09c2-5cf7-9e6f-47a6f16bc04d</chapterId>


Kui teie programmid kasvavad, soovite sageli **korduvkasutada** kooditükke.


Selleks ongi **funktsioonid**: need võimaldavad teil rühmitada koodi, anda sellele nime ja käivitada seda, millal iganes soovite.


### Funktsiooni deklaratsioon


Funktsiooni deklareerimiseks võime kasutada võtmesõna `function`. Seejärel anname sellele nime, sulgudes paari `()`, mis sisaldavad argumente, mida see võtab, ja täidetava koodiploki `{}`. Alustame funktsiooniga, mis ei võta argumente:


```javascript
function sayHello () {console.log(`Hello!`) }
```


See kood **deklareerib** funktsiooni, kuid **ei** seda veel käivita.


### Funktsioonikõned


Funktsiooni käivitamiseks (või "kutsumiseks") kirjutate selle nime, millele järgnevad sulgudes:


```javascript
function sayHello () {console.log(`Hello!`) }
sayHello()
```


See trükib:


```
Hello!
```


Võite funktsiooni kutsuda nii mitu korda kui soovite:


```javascript
function sayHello() {
console.log("Hello!")
}

sayHello()
sayHello()
```


See trükib:


```
Hello!
Hello!
```


Funktsiooni sees olev kood käivitub ainult siis, kui te seda välja kutsute.


### Funktsiooni argumendid (funktsioonide sisend)


Mõnikord soovite, et funktsioon töötaks mõne sisendiga. Seda saab teha, lisades **argumendid** sulgudes.


Näiteks:


```javascript
function sayHelloTo (friend) {
console.log(`Hello ${friend}!`)
}
```


Nüüd võtab see funktsioon **ühe argumendi** nimega `friend`.


Funktsiooni kutsudes saate edastada väärtuse:


```javascript
sayHelloTo("Tommy")
```


See trükib:


```
Hello Tommy!
```


Saate funktsiooni uuesti kutsuda teise nimega:


```javascript
sayHelloTo("Sam")
```


See trükib:


```
Hello Sam!
```


Edastatud väärtus asendab funktsiooni sees muutuja `friend`.


Võite kasutada ka rohkem kui ühte argumenti:


```javascript
function greetTwoPeople(person1, person2) {
console.log(`Hello ${person1} and ${person2}!`)
}

greetTwoPeople("Lina", "Marco")
```


See trükib:


```
Hello Lina and Marco!
```


### `return` (funktsioonide väljund)


Funktsioonid võivad ka **tagastada** väärtusi. See tähendab, et nad saadavad väärtuse tagasi sinna, kust funktsioon välja kutsuti.


Siin on lihtne näide:


```javascript
function getNumber() {
return 42
}

const result = getNumber()
console.log(result)
```


See trükib:


```
42
```


Funktsioon `getNumber()` tagastab `42` ja me salvestame selle `result`i, seejärel trükime selle välja.


Võite ka midagi arvutada tagasi:


```javascript
function add(a, b) {
return a + b
}

const result = add(2, 3)
console.log(result)
```


See trükib:


```
5
```


Kui väärtus on "tagastatud", funktsioon lõpetab. Kõike, mis järgneb `returnile` selles plokis, ei toimu.


```javascript
function saySomething() {

return "hi"

console.log("this never runs")

}

const message = saySomething()
console.log(message)
```


See prindib ainult:


```
hi
```


sest tagastatakse ainult "hi". Rida `console.log("this never runs")` jäetakse vahele.


Võite mõelda funktsioonidest kui väikestest alaprogrammidest. Iga funktsioon võib võtta mingi sisendi, töödelda seda ja anda teile tagasi mingi väljund.


Mis juhtub, kui me üritame kasutada funktsiooni tagastusväärtust, kuid see funktsioon ei tagastanud midagi?


```javascript
function doesNothing () {}

const x = doesNothing()

console.log(x)
```

See trükib `undefined`. Funktsiooni tagastusväärtus, mis ei tagastanud midagi, on `undefined`.


## Objektid ja klassid

<chapterId>26689f25-8212-5057-8c21-3a05eee0ac75</chapterId>


JavaScripti nimetatakse sageli objektorienteeritud keeleks.


See tähendab, et see aitab teil organiseerida oma koodi, rühmitades väärtused ja funktsioonid kokku **objektideks**.


### Mis on "objekt"?


Objekt võib sisaldada andmeid ja funktsioone, mis toimivad nende andmetega. Kui funktsioon pannakse objekti sisse, siis ütleme, et see on "meetod".


Esimene objekt, mida me nägime, oli objekt `console`. See on objekt, mis sisaldab mitmeid meetodeid, et printida asju ekraanile ja siluda meie programme.


See võib isegi ise printida; saate teha


```javascript
console.log(console)
```


ja see väljastab nimekirja meetoditest, mida see sisaldab. Näiteks minu masina puhul printis see välja


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


Nagu näete, on sellel palju meetodeid, mida saaksite kasutada vigade kõrvaldamiseks!


Javascript pakub meile erinevaid viise uute objektide loomiseks, mis võivad teha seda, mida me tahame, et nad teeksid.


### Objekti loomine


Kõige lihtsam viis objekti loomiseks on lihtsalt andmete ja funktsioonide grupeerimine, kasutades **sõltuvaid sulgusid** `{}`.


Sellega luuakse nn **anonüümne objekt**


```javascript
const cat = {
name: "Whiskers",
age: 3
}
```


See loob objekti ja salvestab selle muutujasse nimega `cat`.


Objektil on kaks **omadust**:



- `nimi` väärtusega `"Viskid"`
- "vanus" väärtusega "3"


Trükime selle välja:


```javascript
console.log(cat)
```


See trükib:


```
{ name: 'Whiskers', age: 3 }
```


Objekti omadusi saab välja võtta punkti abil, nagu näiteks `objektiNimi.omaduseNimi`:


```javascript
console.log(cat.name)  // prints "Whiskers"
console.log(cat.age)   // prints 3
```


Saate ka **muuta** omadust:


```javascript
cat.age = 4
console.log(cat.age)  // now it prints 4
```


Nagu näete, isegi kui objekt on defineeritud kui `const`, saate ikkagi muuta selles sisalduvaid andmeid.


Objektide puhul takistab `const` ainult kogu objekti ülestähendamist:


```javascript
const cat = {
name: "Whiskers",
age: 3
}

cat.age = 5 // this works

cat = 5 // this throws an error, you're trying to reassign the whole object

```


Nagu eespool mainitud, võivad objektid sisaldada ka **funktsioone** ja kui funktsioon on osa objektist, siis nimetame seda **meetodiks**.


Siin on üks näide:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log("Meow!")
}
}
```


Sellel objektil on:



- Omadus "nimi
- Meetod `speak()`


Kutsume meetodit:


```javascript
cat.speak()
```


See trükib:


```
Meow!
```


Meetodid saavad kasutada objekti sisalduvaid andmeid võtmesõna `this` kaudu.

`this` viitab praegusele objektile. Selles näites kasutatakse seda kassi nime printimiseks:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log(`${this.name} says meow!`)
}
}

cat.speak()
```


See trükib:


```
Whiskers says meow!
```


Sõna "see" tähendab "see objekt"... antud juhul "kass" objekt.



Sellised objektid on suurepärased, kui soovite midagi kiiret ja lihtsat. Aga kui teil on vaja luua **mitmeid sama struktuuriga objekte**, siis on olemas parem viis, ja siin tulevadki mängu **klassid**.


### Klassid ja konstruktorid


**Klass** on nagu plaan. See ütleb JavaScriptile, kuidas luua teatud tüüpi objekti.


Klassi defineerimiseks kasutate võtmesõna `class`, millele järgneb klassi nimi ja sulge `{}` plokk.


```javascript
class Dog {}
```


Tavapäraselt algavad klassid suure tähega.


Saate luua uue klassi objekti, kasutades `new`:


```javascript
const hachiko = new Dog()
```


Proovige objekt välja printida:

```javascript
class Dog {}

const myDog = new Dog()

console.log(myDog)
```


Saate


```
Dog {}
```


Nagu näete, on klass Dog tühi, seega on ka objekt `myDog` tühi.


Me saame määratleda, milliseid omadusi koeraobjektid peaksid sisaldama, lisades `konstruktori`.


Konstruktor on spetsiaalne funktsioon, mis käivitub uue objekti loomisel (või "konstrueerimisel").


```javascript
class Dog {
constructor() { }
}
```


Me tahame, et igal koeral oleks nimi, seega lisame funktsioonile parameetri `nimi`:


```javascript
class Dog {
constructor(name) { }
}
```


Ja siis kasutame `this`, et deklareerida, et `nimi` on `Dog` objekti `nimi`, mida me ehitame


```javascript
class Dog {
constructor(name) {
this.name = name
}}
```


Proovime seda nüüd kasutada:


```javascript
class Dog {
constructor(name) {
this.name = name
}
}

const myDog = new Dog("hachiko")

console.log(myDog)
```


See trükib midagi sellist:


```
Dog { name: 'hachiko' }
```


Nagu näete, võtab meetod `constructor` vastu argumendid, mis te klassile üle annate, kui teete `new Dog()`, ja kasutab neid objekti loomiseks.


Jagame selle lahti:



- `class Dog` defineerib klassi Dog.
- `constructor(name)` seab objekti loomisel üles.
- `this.name = name` salvestab väärtuse uude objekti.
- `new Dog("hachiko")` loob uue objekti klassist, mille omaduseks `name` on määratud `"hachiko"`.


Nüüd lisame oma klassile meetodi:


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


See prindib


```javascript
hachiko says barf!
```


Kui me teeme sama kahe erineva Koeru eksemplari puhul



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


saame


```
hachiko says barf!
bobby says barf!
```


meetod `speak()` kasutab `Dog` omadust `name`, mille kohta seda kutsutakse.


See on peamine põhjus, miks klassid on olemas: need võimaldavad meil defineerida kogum meetodeid, mis toimivad andmetega, ja seejärel luua mitu objekti, mis jagavad sama andmete "kuju".


Kui me kutsume meetodit ühe sellise objekti kohta, siis see toimib andmete suhtes, mida *see konkreetne objekt* omab.


### Objekti kuju muutmine


Objektid JavaScriptis on paindlikud. Isegi kui olete ühe objekti loonud, saate lisada uusi omadusi või eemaldada olemasolevaid.


See on lubatud, kuid seda tuleks kasutada ettevaatlikult.


Alustame meie lihtsa `Dog` klassiga:


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


Sel hetkel on `myDog`il ainult üks omadus: `nimi`. Me saame veel lisada uusi omadusi pärast selle loomist:


```javascript
myDog.age = 5

console.log(myDog.age) // prints 5
```


Me võime lisada ka uue meetodi:


```javascript
myDog.jump = function () {
console.log(`${this.name} jumps!`)
}

myDog.jump() // Fido jumps!
```


Ja me saame ka eemaldada omadusi, kasutades võtmesõna `delete`.


```javascript
delete myDog.name

console.log(myDog.name) // prints 'undefined'
```


See toimib, kuid siin on midagi olulist, mida peaks teadma: JavaScript-mootorid, nagu V8 (mida kasutatakse Node.jsis ja Chrome'i brauseris), töötavad kiiremini, kui teie objektid säilitavad alati samad omadused. Kui lisate või eemaldate omadusi pärast objekti loomist, võib see aeglustada.


Väikeste programmide puhul ei ole see eriti oluline. Kuid suuremates projektides (näiteks mängudes) on parem kõik omadused algusest peale konstruktoris üles lugeda, isegi kui te neid kohe ei kasuta. See hoiab objekti kuju stabiilsena ja aitab koodil kiiremini töötada.


Näiteks selle asemel:


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


Sa võid teha


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


Mõlemad versioonid toimivad, kuid teine versioon on tulemuslikkuse seisukohast parem. Sa ütled mootorile ette, millised omadused igal objektil on, ja see saab vastavalt optimeerida.


JavaScript võimaldab teil objekte vabalt ümber kujundada, kuid klasside kasutamisel on parem oma objekti kuju ette planeerida.



### Pärimine koos `extends` ja `super()`ga


Mõnikord soovite luua klassi, mis on *peaaegu* samasugune nagu teine klass, kuid millel on mõned lisafunktsioonid.


Selle asemel, et muuta objektide kuju (mis, nagu eespool mainitud, ei ole jõudluse seisukohalt optimaalne) või kirjutada uus klass nullist ümber, võimaldab JavaScript kasutada midagi, mida nimetatakse **pärandiks**.


Pärimine tähendab, et üks klass võib **täiendada** teist klassi. Uus klass saab kõik vana klassi omadused ja meetodid ning sa võid lisada või muuta seda, mida sa vajad.


Oletame, et meil on baasklass nimega `Vehicle`:


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


Nüüd tahame teha klassi `Car`. Auto on mingi sõiduk, kuid me võime soovida, et sellel oleks mõned lisafunktsioonid või teistsugune sõnum, kui ta käivitub. Selle asemel, et kõike ümber kirjutada, võime kasutada `extends`:


```javascript
class Car extends Vehicle {
start() {
console.log(`${this.brand} car is ready to drive!`)
}
}
```


Klass `Auto` pärib nüüd kõik `Auto` klassist `Vehicle`. See saab omaduse `brand` ja me oleme asendanud meetodi `start()` oma versiooniga.


![](assets/en/4.webp)


Proovime seda välja:


```javascript
const myCar = new Car("Toyota")
myCar.start()
```


See trükib:


```
Toyota car is ready to drive!
```


Kuigi `Auto` ei oma konstruktorit, kasutab ta ikkagi `Auto` konstruktorit. Aga kui me tahame `Autole` kirjutada oma konstruktori, siis saame seda teha, me peame lihtsalt lisama üleskutse oma vanema konstruktorile, kasutades `super()`.


Siin on, kuidas:


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



See trükib:


```
Toyota Corolla is ready to drive!
```


Niisiis, kokkuvõtteks



- `extends` tähendab, et üks klass põhineb teisel.
- `super()` kasutatakse laiendatava klassi konstruktori kutsumiseks.
- Uus klass saab kõik algse klassi omadused ja meetodid.
- Sa võid **üleülesandida** meetodeid (nagu `start()`), et panna neid tegema midagi muud.


See on kasulik, kui teil on mitu sarnast asja (näiteks autod, veoautod ja jalgrattad) ja te soovite, et nad jagaksid koodi, kuid käituksid siiski omal viisil.


### `instanceof`


Võtmesõna `instanceof` kontrollib, kas objekt on loodud teatud klassist.


Oletame, et meil on klass nimega `User`:


```javascript
class User {
constructor(username) {
this.username = username
}
}

const regularUser = new User("julia123")

console.log(regularUser instanceof User)
```


See trükib:


```
true
```


Kinnitus, et `regularUser` on `User`. Seda seetõttu, et `regularUser` loodi klassi `User` abil.


See töötab ka **päritud** klassidega. Näiteks siin on `Admin` klass, mis on `User` klassi edasiarendus:


```javascript
class Admin extends User {}

const ourAdmin = new Admin("admin42")

console.log(ourAdmin instanceof Admin)   // true
console.log(ourAdmin instanceof User)    // true
```


Mõlemad read tagastavad `true`. Seda seetõttu, et `Admin` on `User` alamklass, seega on `MeieAdmin` nii `Admin` kui ka `User`


# Vahepealne JavaScript

<partId>243f63ab-4f34-5c30-80cb-84ef46f6761d</partId>


## Veakäitlus

<chapterId>d0206bc5-d386-5e7f-9917-5803f392448c</chapterId>


Kui kirjutate keerulisemaid JavaScript-programme, tekib teil **vead**. Need on ootamatud olukorrad, kus midagi läheb valesti. Võib-olla on mingi muutuja `defineerimata`, aga te proovite seda kasutada või mõni kood saab valet tüüpi sisendi.


Kui me neid vigu korralikult ei käsitle, võib meie programm kokku kukkuda või käituda ettearvamatul viisil. JavaScript pakub vahendeid nende vigade avastamiseks ja haldamiseks, et saaksime neid väärikalt käsitleda.


### Üldine viga: juurdepääs väärtusele `undefined`


Siin on tavaline olukord, mis põhjustab vea:


```javascript
const user = undefined
console.log(user.name)
```


Kui te käivitate selle koodi, saate vea, mis näeb välja selline:


```
TypeError: Cannot read properties of undefined (reading 'name')
```


See on JavaScript, mis ütleb teile: see tähendab, et JavaScript ütleb: "Hei, sa üritasid saada omadust "nimi" millestki, mis on "määratlemata", ja see ei ole mõttekas." Ja nagu näete, kui selline viga juhtub, peatub programmi töö, kui te pole spetsiaalselt kirjutanud koodi, et seda tabada ja käsitleda.


### vea viskamine


Mõnikord soovite oma koodis käsitsi **viga tekitada**. Sellisel juhul kasutate võtmesõna `throw`.


```javascript
throw new Error("This is a custom error message")
```


See peatab kohe programmi ja prindib:


```
Uncaught Error: This is a custom error message
```


Sa võid kasutada `throw` reeglite jõustamiseks oma programmis. Näiteks:


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


Teine üleskutse põhjustab vea, sest nulliga jagamine ei ole selles näites lubatud.


### Vigade püüdmine `try...catch` abil


Kui te ei taha, et teie programm vea ilmnemisel kokku kukub, saate vea kinni püüda, kasutades blokki `try...catch`. See on kasulik, kui soovite, et teie programm **jätkaks** isegi siis, kui midagi ei õnnestu.


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log("Oops! Something went wrong.")
}
```


Väljund:


```
Oops! Something went wrong.
```


See toimib järgmiselt:



- Esimesena proovitakse `try` ploki sees olevat koodi.
- Vea korral hüppab JavaScript **jumpi blokki `catch`**, jättes ülejäänud bloki `try` vahele.
- `catch` plokk saab vea, nii et saate selle välja trükkida või käsitleda seda mõnel muul viisil, nagu näiteks


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log(`The message of the error was: "${error.message}"`)
}
```


Väljund:


```
The message of the error was: "Cannot read properties of undefined (reading 'name')"
```


### Plokk "Lõpuks


Saate lisada ka bloki `finally`. See on kood, mis **jooksab** alati, olenemata sellest, kas oli viga või mitte.


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


Väljund:


```
Trying something risky...
Caught the error: Uh oh!
This will run no matter what.
```


## Vigade vältimine

<chapterId>db12d9f6-5806-514c-998e-0ae24805104e</chapterId>


Selles peatükis näidatakse mõningaid kõige levinumaid lõkse JavaScriptis ja kuidas neid vältida.


### `var` ja Assignment ilma deklaratsioonita


Vanemas JavaScripti koodis deklareeriti muutujaid sageli võtmesõnaga `var`. Erinevalt `let` ja `const`, mida te juba tundsite, võib `var` käituda segadusttekitavalt.


Näiteks:


```javascript
{
var message = "hello"
}
console.log(message)
```


Võiksite eeldada, et `message` eksisteerib ainult ploki sees, kuid see ei ole nii. `var` ignoreerib ploki ulatust ja muudab muutuja kättesaadavaks kogu funktsiooni või faili ulatuses.


See võib põhjustada ootamatut käitumist, eriti suuremates programmides. Sel põhjusel peaks kaasaegne JavaScript-kood alati kasutama `var` asemel `let` või `const`.


Veelgi hullem on see, et JavaScript lubab määrata muutujatele väärtusi **selliseid muutujaid üldse deklareerimata**:


```javascript
function greet() {
user = "Alice"
}
greet()
console.log(user) // prints "Alice"
```


See loob uue globaalse muutuja `nimi` ilma deklareerimiseta. See võib juhtuda vaikselt ja põhjustada vigu, mida on Hard jälgida, eriti kui tegemist oli lihtsalt trükivigaga. Deklareerige muutujaid alati, kasutades `let` või `const`.


### Nõrk tüübisüsteem


JavaScript on nõrgalt tüpiseeritud, mis tähendab, et vajaduse korral teisendab see automaatselt väärtused ühest tüübist teise. Seda nimetatakse tüübipiiranguks ja kuigi see võib olla mugav, toob see sageli kaasa segadust tekitava tulemuse.


Näiteks:


```javascript
console.log("5" + 1)    // "51"
console.log("5" - 1)    // 4
console.log(true + 1)   // 2
console.log(null + 1)   // 1
```


Nendes näidetes püüab JavaScript ära arvata, mida te mõtlesite. Mõnikord muudab ta stringid numbriteks või boole'id numbriteks või stringid stringideks. See võib panna teie koodi käituma ootamatul viisil.


Oluline on olla teadlik JavaScripti nõrgast tüübisüsteemist. Kui asjad hakkavad veidralt käituma, võib see olla tingitud ootamatust tüübipiirangust.


### `"use strict"`


Saate lubada rangemat režiimi, mis muudab mõned vaikivad vead tõelisteks vigadeks ja takistab teil kasutada mõningaid keele ohtlikumaid funktsioone.


Selle rangema režiimi lubamiseks lisage see rida oma faili või funktsiooni algusesse:


```javascript
"use strict"
```


Näiteks:


```javascript
"use strict"
name = "Alice" // ReferenceError: name is not defined
```


Ilma range režiimita looks JavaScript vaikselt globaalse muutuja nimega `nimi`. Kuid range režiimiga muutub see tõeliseks veaks, mis aitab teil vigu varem avastada.


Range režiim lülitab välja ka mõned JavaScripti vananenud funktsioonid ning muudab teie koodi lihtsamaks optimeerida ja hooldada.


## Väärtus vs viide

<chapterId>bb898425-dc2f-5e5c-864b-0cb7a4a9aea9</chapterId>


JavaScript käsitleb erinevaid väärtusi erinevalt.


Mõned väärtused **koopiate**, kui määrate need muutujale.


Teised on **jagatud**, kui määrate need uuele muutujale, nii et kui muudate ühte, muutub ka teine muutuja.


### Väärtuse järgi edasiandmine


Kui väärtus edastatakse **väärtuse järgi**, teeb JavaScript sellest **koopia**.


Nii et kui te muudate ühte, ei mõjuta see teist.


See juhtub primitiivsete tüüpidega, nagu:



- numbrid
- stringid
- booleans (`true` ja `false`)
- `null`
- `undefined`


Vaatame ühte näidet:


```javascript
let a = 5
let b = a

b = 10

console.log(a) // 5
console.log(b) // 10
```


Me andsime `b` väärtuseks `a`, kuid seejärel muutsime `b` väärtuseks `10`.


Kuna numbrid antakse üle väärtuse järgi, siis kopeeris JavaScript "5" "b"-sse. `5` punktis `b` on sõltumatu algsest `5`-st `a`, nii et `b` väärtuse muutmine ei mõjuta `a`-d.


Proovime stringiga:


```javascript
let name1 = "Alice"
let name2 = name1

name2 = "Bob"

console.log(name1) // Alice
console.log(name2) // Bob
```


Jällegi, `nimi2` muutmine ei mõjutanud `nimi1`, sest ka stringid antakse üle väärtuse järgi.


Sama asi juhtub, kui annate primitiivi funktsioonile üle: see kopeeritakse. Seega ei saa funktsioon originaali muuta.


```javascript
function plusOne(x) {
x = x + 1
}

let number = 5

plusOne(number)

console.log(number) // 5
```


Kuigi funktsiooni `x` sees lisati `1`, ei muutunud algne `number`.


Seda seetõttu, et funktsioonile on edastatud ainult **koopia**.


### Viite kaudu edasiandmine


Objektid antakse üle **viidetega**.


See tähendab, et nende kopeerimise asemel edastab JavaScript lihtsalt **viite** sellele ja kui te seda muudate, näevad seda muutust ka kõik teised muutujad, mis sellele osutavad.


Näiteks:


```javascript
const person1 = { name: "Alice" }
const person2 = person1

person2.name = "Bob"

console.log(person1.name) // Bob
console.log(person2.name) // Bob
```


Nii `person1` kui ka `person2` osutavad mälus samale objektile.


Nii et kui me muutsime `person2.name`, siis muutsime ka `person1.name`, sest mõlemad vaatavad sama asja.


Massiivid on objektid, seega proovime sama massiivi abil:


```javascript
const list1 = [1, 2, 3]
const list2 = list1

list2.push(4)

console.log(list1) // [1, 2, 3, 4]
console.log(list2) // [1, 2, 3, 4]
```


Me lükkasime `4` loendisse `list2`, kuid see mõjutas ka loendit `list1`, sest mõlemad viitavad samale massiivi.


Vaatame, mis juhtub, kui anname objekti funktsioonile üle:


```javascript
function rename(user) {
user.name = "Charlie"
}

const person = { name: "Dana" }

rename(person)

console.log(person.name) // Charlie
```


Funktsioon muutis objekti! Seda seetõttu, et ta sai **viite** algsele objektile `person`.


See ei saanud koopiat. Ta sai juurdepääsu algsele objektile ja sellega koos ka võimaluse seda muuta.


On oluline seda vahet meeles pidada, sest muidu võib meie kood käituda teisiti, kui me ootame. Näiteks võime kirjutada funktsiooni ootusega, et see ei muuda saadud argumente, ja hiljem selgub, et tegelikult muutis see neid (sest need olid objektid, seega anti need üle viitega).


## Töö funktsioonidega

<chapterId>e0d277a8-c642-5af7-9e53-dee27c811967</chapterId>


Te olete juba õppinud, kuidas funktsioone JavaScriptis deklareerida ja kasutada. Kuid JavaScript annab teile rohkem vahendeid, et töötada funktsioonidega võimsalt.


### Noole funktsioonid


Noolfunktsioonid on lühem viis funktsioonide kirjutamiseks. Võtmesõna `function` asemel kasutame noolt (`=>`).


Siin on tavaline funktsioon:


```javascript
function greet(name) {
return `Hello, ${name}!`
}
```


Noolega versioon näeb välja selline:


```javascript
const greet = (name) => {
return `Hello, ${name}!`
}
```


Kui funktsioonil on **ainult üks rida**, võite sulgudes ja `return` vahele jätta:


```javascript
const greet = (name) => `Hello, ${name}!`
```


Kui funktsioonil on **ainult üks parameeter**, võite isegi sulgud ümber parameetrite vahele jätta:


```javascript
const greet = name => `Hello, ${name}!`
```


Noolefunktsioonid on tänapäevases JavaScriptis väga levinud, sest need võimaldavad väljendada lihtsaid funktsioone oluliselt väiksema mahuga.


### Vaikimisi parameetrid


Mõnikord soovite, et funktsioonil oleks **eelarveväärtus**, kui ühtegi argumenti ei edastata.


Seda saab teha nii:


```javascript
function sayHello(name = "friend") {
console.log(`Hello, ${name}!`)
}

sayHello("Alice") // Hello, Alice!
sayHello()        // Hello, friend!
```


Vaikeväärtust `"friend"` kasutatakse, kui midagi ei edastata.


### Hajutatud parameetrid (`...`)


Mis siis, kui teie funktsioon võtab vastu paindliku arvu argumente?


Nende koondamiseks massiivi saab kasutada **jaotuseoperaatorit** (`...`):


```javascript
function logAll(...items) {
console.log(items)
}

logAll(1, 2, 3) // [1, 2, 3]
logAll("a", "b") // ["a", "b"]
```


Seejärel saate iga elemendi töötlemiseks kasutada tsüklit:


```javascript
function logEach(...items) {
for (const item of items) {
console.log(item)
}
}
```


Operaator spread on kasulik, kui te ei tea, mitu argumenti edastatakse.


### Kõrgemat järku funktsioonid


**Kõrgema astme funktsioon** on funktsioon, mis:



- võtab sisendiks teise funktsiooni
- ja/või tagastab väljundina funktsiooni


Siin on lihtne näide:


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


See trükib:


```
Hello, friend!
Hello, friend!
```


Me saame sellele edastada noole funktsiooni:


```javascript
runTwice(
() => console.log("Hello!")
)
```


See trükib:


```
Hello!
Hello!
```


Võite kirjutada ka funktsioone, mis **tagastavad** teisi funktsioone:


```javascript
function makeGreeter(name) {
return () => console.log(`Hi, ${name}`)
}

const greetAlice = makeGreeter("Alice")
const greetBob = makeGreeter("Bob")

greetAlice() // Hi, Alice
greetBob() // Hi, Bob
```


Funktsioon `makeGreeter` on funktsioon, mis ehitab teisi funktsioone. See saab stringi ja tagastab uue funktsiooni, mis kasutab seda stringi oma `console.log` kutses.


Selline muster on väga võimas, sest see võimaldab teil jätta oma funktsioonidesse "auke", mida saate hiljem vajaliku käitumisega täita.


### `map()`, `filter()`, `reduce()`


JavaScript annab teile mõned kasulikud sisseehitatud meetodid massiividega kasutamiseks.


Need meetodid võtavad argumentidena funktsioone, seega on need samuti kõrgema astme funktsioonid.


`map()` muudab iga elemendi massiivi millekski muuks.


Näide:


```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map(x => x * 2)

console.log(doubled) // [2, 4, 6]
```


Iga number kahekordistatakse ja tulemuseks on uus massiivi.


`filter()` eemaldab elemendid massiivist, kui need ei läbinud testi.


Näide:


```javascript
const numbers = [1, 2, 3, 4, 5]
const numbersGreaterThanTwo = numbers.filter(x => x > 2)

console.log(numbersGreaterThanTwo) // [3, 4, 5]
```


Säilitatakse ainult need massiivi kirjed, mille puhul tingimus `x > 2` annab tagasi `true`.


`reduce()` kasutatakse kõigi massiivi elementide ühendamiseks üheks väärtuseks.


Näide:


```javascript
const numbers = [1, 2, 3, 4]
const total = numbers.reduce((current, next) => current + next)

console.log(total) // 10
```


`reduce` läbib massiiv ja rakendab antud näites operaatorit `+` vahel `1` ja `2`, seejärel saadud `3` ja `3` vahel, seejärel saadud `6` ja `4` vahel, kuni ta saab kõigi massiivide kirjete summa (mis on 10).


Saate kasutada `reduce()` paljude asjade jaoks, nagu näiteks kogusummad, keskmised või uute väärtuste loomine samm-sammult.


Need meetodid (`map`, `filter`, `reduce`) on võimsad tööriistad andmete töötlemiseks ilma manuaalsete tsüklite kirjutamiseta.


Neid saab isegi kombineerida operatsioonide ahelas, näiteks nii:


```javascript
const numbers = [1, 2, 3, 4, 5]

const result = numbers
.map(n => n * 2)        // Double each entry, obtain [2, 4, 6, 8, 10]
.filter(n => n > 3) // Keep only the entries bigger than 3, so you get [4, 6, 8, 10]
.reduce((n1, n2) => n1 + n2) // Adds them: 4 + 6 + 8 + 10 = 28

console.log(result) // 28
```


## Töötamine objektidega

<chapterId>7842aada-f009-5518-b8e3-1104e166a035</chapterId>


Selles peatükis õpime tundma mõningaid võimsaid ja veidi keerulisemaid vahendeid objektidega töötamiseks JavaScriptis.


### Erakinnisvara


Mõnikord tahame objekti omadust peita, et seda ei saaks muuta või sellele väljastpoolt objekti juurde pääseda. JavaScript annab meile võimaluse seda teha, kasutades `#` enne omaduse nime. See loob **privaatse** omaduse, millele on ligipääs ainult klassi sees.


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


Privaatsed omadused on kasulikud, kui soovite vältida juhuslikke muudatusi.


### staatilised omadused


Mõnikord soovite, et omadus kuuluks klassile endale, mitte igale objektile, mille te sellest klassist loote. Selleks ongi "static". Staatiline omadus sisaldub klassis ja kõik selle klassi objektid viitavad sellele.


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


See on kasulik ühiste andmete ja meetodite salvestamiseks, mis kehtivad kogu objektide grupile, mitte ainult ühele objektile.


### `get` ja `set`


JavaScriptis võimaldavad `get` ja `set` teha omadusi, mis *nähtavad* nagu tavalised muutujad, kuid tegelikult käivitavad taustal spetsiaalset koodi.


Meetod `get`ter käivitub, kui proovite *lugeda* omadust. See deklareeritakse, kirjutades `get` enne meetodit koos omaduse nimega.


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


Kuigi `fullName` ei ole tavaline omadus, saame seda kasutada nagu sellist ja kulisside taga käivitatakse funktsioon `get`, et luua täisnimi.


Meetod "set" käivitub siis, kui te *määrate* omadusele väärtuse. See võimaldab teil kontrollida, mis juhtub, kui keegi üritab seda väärtust muuta. See deklareeritakse kirjutades `set` enne meetodit koos omaduse nimega.


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


Kui me teeme `user.fullName = "John Smith"`, siis käivitatakse meetod `set` ja uuendatakse väärtused `firstName` ja `lastName`.


Nii et kuigi tundub, et me lihtsalt seame lihtsa muutuja, käivitame tegelikult loogika, mis uuendab teisi omadusi.


## Võtmed ja väärtused

<chapterId>01a397b8-c12a-5c39-82b3-6d9ebbb72a29</chapterId>


Igal JavaScripti objekti omadusel on **võti** (mida nimetatakse ka omaduse nimeks) ja **väärtus**.


Näiteks:


```javascript
const user = {
name: "Alice",
age: 30
}
```


Selles objektis on "nimi" ja "vanus" võtmed ning "Alice" ja "30" nende väärtused.


### Dünaamiline juurdepääs


Mõnikord ei tea sa omaduse nime ette... võib-olla saad selle kasutaja sisendist või loed seda muutujast. Saate sellele ikkagi ligi, kasutades **sulgudes märkimist**, näiteks `myObject["keyName"]`.


```javascript
const user = {
name: "Alice",
age: 30
}

console.log(user["name"]) // Alice
```


Me andsime objektile üle stringi `nimi`, et saada vastav väärtus.


Me võime salvestada võtme muutujasse ja kasutada seda, et hiljem vastava väärtuse juurde pääseda, nagu näiteks


```javascript
const user = {
name: "Alice",
age: 30
}

const key = "name"

console.log(user[key]) // Alice
```


### Dünaamiline Assignment


Samuti saate luua või uuendada objekti omadusi, kasutades muutujaid võtmetena.


```javascript
const settings = {}

const key = "theme"
settings[key] = "dark"

console.log(settings) // { theme: "dark" }
```


See on kasulik, kui soovite objekti samm-sammult ehitada. Näiteks:


```javascript
const user = {}

user["username"] = "bananaFan123"
user["email"] = "banana@fruit.com"

console.log(user)
// { username: "bananaFan123", email: "banana@fruit.com" }
```


Saate isegi kasutada dünaamilist võtit *objekti loomisel*, kasutades selleks nurksulgusid:


```javascript
const key = "language"
const config = {
[key]: "JavaScript"
}

console.log(config.language) // JavaScript
```


Seda nimetatakse **arvutatud omaduseks**. Arvutatakse nurksulgudes olevat väärtust ja tulemust kasutatakse võtmena.


### "Sümboli" tüüp


Lisaks stringidele võimaldab JavaScript kasutada objekti võtmena ka spetsiaalset tüüpi `Symbol`.


Alustame lihtsa näitega:


```javascript
const id = Symbol("userID")

const user = {
name: "Bob",
[id]: 12345
}

console.log(user[id]) // 12345
```


Selles näites on `id` sümbol. See ei ole string, kuid see toimib ikkagi võtmena. Kui te proovite `user` konsooli logida, näete seda:


```javascript
console.log(user) // { name: 'Bob', [Symbol(userID)]: 12345 }
```


Veel üks oluline asi: iga loodud sümbol on unikaalne, isegi kui need on loodud sama stringi abil.


```javascript
const a = Symbol("label")
const b = Symbol("label")

console.log(a === b) // false
```


Sümbolid võimaldavad teil määratleda võtmeid, mis ei lähe kokku tavaliste võtmetega. Oletame näiteks, et teil on objekt, millel on omadus `nimi`, kuid objekt on tulevikus kasutaja poolt kohandatav, mida te ei oska ette näha, ja see kasutaja võib lisada ka omaduse `nimi`. Kui algne `nimi` omadus oli defineeritud stringiga, siis kirjutatakse see uue omadusega üle, näiteks nii:


```javascript
const obj = {
name: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy' }
```


Kui me kasutame selle asemel sümbolit:


```javascript
const name = Symbol("name")

const obj = {
[name]: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy', [Symbol(name)]: 'John' }
```


Nagu näete, säilib algne omadus `nimi` kuidagi sel viisil. See võib olla kasulik teatud äärmuslikel juhtudel.


## Kasutusobjektid

<chapterId>516e74c8-2a11-545a-a4d1-c2cabb91a273</chapterId>


JavaScript annab meile mõned kasulikud sisseehitatud objektid, mis aitavad meil teha selliseid asju nagu silumine ja matemaatilised operatsioonid.


### Muud "konsooli" meetodid


Te olete juba näinud `console.log`, mis prindib väärtused ekraanile.


Objektil `console` on ka mõned muud kasulikud meetodid, mis aitavad teil oma programme siluda.


#### `console.warn`


Trükib teate kollase värviga (või mõnes keskkonnas hoiatussümboliga):


```javascript
console.warn("This is just a warning.")
```


#### `console.error`


Trükib teate punase värviga, nagu viga:


```javascript
console.error("Something went wrong!")
```


#### `console.table`


Kuvab massiivi või objekti tabelina:


```javascript
const users = [
{ name: "Alice", age: 25 },
{ name: "Bob", age: 30 }
]

console.table(users)
```


See prindib tabeli nagu:


```
┌─────────┬────────┬─────┐
│ (index) │  name  │ age │
├─────────┼────────┼─────┤
│    0    │ 'Alice'│  25 │
│    1    │ 'Bob'  │  30 │
└─────────┴────────┴─────┘
```


See võib olla kasulik struktureeritud andmete visualiseerimiseks.


#### `console.time` ja `console.timeEnd`


Saate mõõta, kui kaua midagi aega võtab:


```javascript
console.time("timer")
for (let i = 0; i < 1000000; i++) {}
console.timeEnd("timer")
```


See trükib midagi sellist:


```
timer: 2.379ms
```


Kasulik mõneks lihtsaks jõudluse testimiseks.


### Matemaatiline objekt


JavaScript annab teile objekti `Math`, millel on kasulikud meetodid arvutuste tegemiseks.


#### `Math.random()`


Tagastab juhusliku arvu vahemikus 0 (kaasa arvatud) ja 1 (välistatud):


```javascript
const r = Math.random()
console.log(r)
```


Näidisväljund:


```
0.4387429859
```


#### `Math.floor()` ja `Math.ceil()`



- `Math.floor(n)` ümardab **allapoole** lähima täisarvuni
- `Math.ceil(n)` ümardab **üles** lähima täisarvuni


```javascript
console.log(Math.floor(4.9)) // 4
console.log(Math.ceil(4.1))  // 5
```


#### `Math.round()`


Ümardab lähima täisarvuni:


```javascript
console.log(Math.round(4.4)) // 4
console.log(Math.round(4.6)) // 5
```


#### `Math.max()` ja `Math.min()`


Tagastab suurima või väikseima väärtuse numbrite loetelust:


```javascript
console.log(Math.max(5, 9, 3)) // 9
console.log(Math.min(5, 9, 3)) // 3
```


#### `Math.pow()` ja `Math.sqrt()`



- `Math.pow(a, b)` annab sulle `a` potentsile `b`
- `Math.sqrt(n)` annab sulle `n` ruutjuure


```javascript
console.log(Math.pow(2, 3))   // 8
console.log(Math.sqrt(16))    // 4
```


# Täiustatud JavaScript

<partId>72c30671-ca20-5617-92a5-d5ba7aa38c93</partId>


## Muud kollektsioonid

<chapterId>a9a70c6d-a343-5a46-a383-e288bc2700e3</chapterId>


JavaScript annab meile mõned spetsiaalsed kollektsioonitüübid, mis lähevad kaugemale tavalistest massiividest ja objektidest. Nende hulka kuuluvad `Map` ja `Set`.


Need aitavad teil väärtuste rühmi salvestada ja hallata, kuid nad töötavad teisiti kui seni nähtud.


Kaart on **võtme-väärtuse paaride** kogum, nagu objektidki. Kuid sellel on mõned olulised erinevused:



- Võtmed võivad olla **kõik millised väärtused**, mitte ainult stringid.
- Objektide järjekord säilib.
- Sellel on sisseehitatud meetodid, mis lihtsustavad sellega töötamist.


Looge uus kaart niimoodi:


```javascript
const myMap = new Map()
```


See loob tühja kaardi. Kirjete lisamiseks kasutage `myMap.set(key, value)`:


```javascript
myMap.set("name", "Alice")
```


See lisab võtme "name" väärtusega "Alice".


Võid kasutada võtmena ka numbrit:


```javascript
myMap.set(42, "The answer")
```


Ja isegi objekt kui võti:


```javascript
const objKey = { id: 1 }
myMap.set(objKey, "Object as key")
```


See ei toimiks tavaliste objektidega, mis lubavad ainult stringi võtmeid.


Väärtuse **saamiseks** kasutage `myMap.get(key)`:


```javascript
console.log(myMap.get("name"))     // Alice
console.log(myMap.get(42))         // The answer
console.log(myMap.get(objKey))     // Object as key
```


Selleks, et **kontrollida, kas võti on olemas**, kasutage `myMap.has(key)`:


```javascript
console.log(myMap.has("name")) // true
```


Võtme **eemaldamiseks** kasutage `myMap.delete(key)`:


```javascript
myMap.delete("name")
```


Kogu kaardi **tühjendamiseks** kasutage `myMap.clear()`:


```javascript
myMap.clear()
```


Kaardid on suurepärased suurte väärtuste kogumite haldamiseks, sest juurdepääs väärtustele suurel kaardil annab tavaliselt palju parema jõudluse kui suurel objektil.


### `Set`


Kogum on ainult **väärtuste** kogum (võtmed puuduvad), kus iga väärtus peab olema **üheselt mõistetav**. See tähendab:



- Sul ei saa olla sama väärtus kaks korda
- Väärtused salvestatakse sellises järjekorras, nagu te need lisate


Looge selline komplekt:


```javascript
const mySet = new Set()
```


Väärtuste **lisamiseks** kasutage `mySet.add(value)`:


```javascript
mySet.add(1)
mySet.add(2)
mySet.add(2) // duplicate, will be ignored
```


Kuigi me püüdsime lisada `2` kaks korda, säilitab komplekt ainult ühe koopia.


Selleks, et **kontrollida, kas väärtus on komplektis**, kasutage `mySet.has(value)`:


```javascript
console.log(mySet.has(2)) // true
console.log(mySet.has(3)) // false
```


Väärtuse **kustutamiseks** kasutage `mySet.delete(value)`:


```javascript
mySet.delete(2)
```


Et **tühjendada kõik**, kasutage `mySet.clear()`:


```javascript
mySet.clear()
```


`Set` on kasulik, kui soovite hoida unikaalsete väärtuste kogumit, ilma et peaksite duplikaate käsitsi kontrollima:


```javascript
const numberArray = [1, 2, 2, 3, 4, 4, 4, 5]

const numberSet = new Set(numberArray)

console.log(numberSet) // Set(5) { 1, 2, 3, 4, 5 }
```


`Set` väldib teie jaoks duplikaatide tekkimist.


## Iteraatorid

<chapterId>61d24e5e-b7e4-541a-8322-778f61f26a72</chapterId>


Enamik asju, mille üle saab JavaScriptis loopida (näiteks massiivid, stringid, kaardid, komplektid), on **iterable**: nad võivad pakkuda oma sisu jaoks iteraatoreid.


**Iteraator** on JavaScriptis spetsiaalne objekt, mis aitab teil läbida elementide nimekirja **ükshaaval**.


### "Objekti" iteraatorid


Erinevalt massiividest või kaartidest ei ole tavalised objektid **kasutatavad** funktsiooni `for...of` abil. Kui te proovite seda:


```javascript
const user = {
name: "Alice",
age: 30
}

for (const value of user) {
console.log(value)
}
```


Saate vea:


```
TypeError: user is not iterable
```


Seda seetõttu, et tavalistel objektidel ei ole sisseehitatud iteraatorit. Kuid JavaScript annab teile muid vahendeid, et nende üle loopida.


#### `Object.keys()`


Saate kasutada `Object.keys(obj)`, et saada objekti **võtmete** massiivi ja seejärel selle üle loopida:


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


See trükib:


```
name
age
```


#### `Object.values()`


**Väärtuste** läbimiseks kasutage `Object.values()`:


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


See trükib:


```
Alice
30
```


#### `Object.entries()`


Kui soovite nii võtit kui ka väärtust**, kasutage `Object.entries()`:


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


See trükib:


```
name is Alice
age is 30
```


Kuigi objektid ei ole otseselt itereeritavad, annavad need meetodid täieliku juurdepääsu nende sisule viisil, mis töötab hästi koos `for...of`-iga.


Aga kuidas iteraatorid töötavad?


### `Symbol.iterator`


Kõikide iteratiivide saladus on spetsiaalne **sümbol** nimega `Symbol.iterator`.


See sümbol on sisseehitatud võti, mis ütleb JavaScriptile: "Seda objekti saab itereerida"


Kui kutsute `myIterable[Symbol.iterator]()`, annab JavaScript teile tagasi **iteratoriobjekti** koos meetodiga `.next()`.


Vaatame, kuidas see välja näeb:


```javascript
const colors = ["red", "green", "blue"]

const iterator = colors[Symbol.iterator]()

console.log(iterator.next()) // { value: 'red', done: false }
```


Iga kõne `.next()` annab teile järgmise väärtuse. Kui see on lõpetatud, naaseb see:


```javascript
{ value: undefined, done: true }
```


### `next()`


Meetodit `.next()` kasutatakse järjestuse järgmise elemendi saamiseks.


Iga kord, kui kutsute `.next()`, saate kahe võtmega objekti:



- "väärtus": praegune objekt
- `done`: boolean, mis ütleb, kas iteratsioon on lõppenud


Teeme täieliku näite:


```javascript
const names = ["Lina", "Tom", "Eva"]      // declare an array
const iterator = names[Symbol.iterator]() // use the Symbol.iterator function to get an iterator for this array

let result = iterator.next()              // get the first element of the array

while (!result.done) {                    // repeat this loop until you reach the last element of the array, which is marked with { done: true }
console.log(result.value)               // print the value of each element
result = iterator.next()                // get the next element of the array
}
```


See trükib:


```
Lina
Tom
Eva
```


Nii töötab `for...of` tsükkel kapoti all: ta kasutab seda mustrit koos `.next()`ga.


Sama tulemus saadakse ka


```javascript
const names = ["Lina", "Tom", "Eva"]

for (const result of names) {
console.log(result)
}
```


### Klassi iteratiivseks muutmine


Sa võid ka defineerida oma **iterable klassi**, lisades meetodi `[Symbol.iterator]()`.


Oletame, et tahame klassi, mis esindab **numbrite vahemikku**, näiteks 1 kuni 5.


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


See trükib:


```
1
2
3
4
5
```


Siin on see, mis toimub:



- Me defineerisime klassi `Range`
- Klassi sees rakendasime `[Symbol.iterator]()`, nii et JavaScript teab, kuidas seda itereerida
- Meetod `next()` annab iga numbri ükshaaval tagasi
- Kui me jõuame `end`, siis tagastab see `{ done: true }`


Nüüd töötab meie `Range` klass nagu massiiv ja me saame seda kasutada mis tahes tsüklis, mis ootab iterable'i.


### Generaatori funktsioonid ja `yield`


Iteraatorite loomise lihtsustamiseks annab JavaScript teile **generaatori funktsioonid**, kasutades võtmesõna `function*` (see on `function`, mille lõpus on `*`) ja võtmesõna `yield`.


Proovime:


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


Iga `yield` annab väärtuse tagasi ja **pausib** funktsiooni kuni järgmise `.next()` kutsumiseni.


Samuti saab genereerimise üle loopida käsuga `for...of`:


```javascript
for (const num of numberGenerator()) {
console.log(num)
}
```


See trükib:


```
1
2
3
```


## Samaaegsus koos tagasilöökidega

<chapterId>f3fc76ca-b3ef-54eb-a06e-501007002054</chapterId>


Siiani on meie kood olnud **sünkroonne**: see töötab üks rida korraga, järjekorras. Kuid mõned asjad reaalses maailmas võtavad aega ja me ei taha, et kogu programm ootamise ajal peatuks.


Selles peatükis tutvustame uut mõistet: **valuuta**. See võimaldab meil manipuleerida järjekorda, milles asju tehakse. See on kasulik, kui tegeleme selliste asjadega nagu taimerid, kasutaja sisend või failide lugemine kettalt. JavaScript pakub erinevaid vahendeid samaaegsuse tegemiseks.


### `setTimeout`


Funktsioon `setTimeout` võimaldab teil **täita funktsiooni hiljem**, kui on möödunud mingi aeg.


Näide:


```javascript
console.log("Start")

setTimeout(
() => console.log("This runs after 2 seconds"),
2000
)

console.log("End")
```


See trükib:


```
Start
End
This runs after 2 seconds
```


Kuigi `setTimeout` esineb koodi keskel, ei blokeeri see ülejäänud osa. Selle asemel planeerib see funktsiooni käivitamise **kord** ja liigub kohe edasi.


2000 tähendab 2000 millisekundit (mis on 2 sekundit).

Siin on lõigete **Callbacks** ja **Promise** sõnasõnalisem ja algajatele sobivam ümberkirjutus, kasutades läbivalt andmete manipuleerimist ja selgeid märkusi:


### Tagasikutsumine


**tagasiütlus** on lihtsalt funktsioon, mille me anname teisele funktsioonile, et seda saaks **tagasi kutsuda**.


Vaatame reaalse näite numbrite abil. Kujutage ette, et meil on numbrite nimekiri ja me tahame iga numbrit kahekordistada ning seejärel rakendada funktsiooni (tagasikutsumine) saadud "kahekordistatud" massiivi suhtes, kuid me tahame seda teha väikese viivitusega, nagu ootaksime midagi aeglast (näiteks andmete laadimist internetist).


Siin on funktsioon, mis teeb seda, kasutades **tagasilööki**:


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


Proovime seda funktsiooni kasutada:


```javascript
const input = [1, 2, 3]

doubleNumbers(input, function(result) {
console.log("Here is the doubled array:", result)
})
```


Pärast 1 sekundit prinditakse see välja:


```
Here is the doubled array: [ 2, 4, 6 ]
```


**Mida siin toimub?*


1. Edastame `input` kui numbrite nimekirja, mida tahame kahekordistada.

2. Samuti anname üle **tagasivõtufunktsiooni**, mis ütleb programmile, mida teha *pärast* kahekordistamist.

3. `doubleNumbers` sees simuleerime viivituse, kasutades `setTimeout`, seejärel teeme kahekordistamise.

4. Kui see on tehtud, kutsume tagasikutsumise saadud "kahekordistunud" massiivi kohta.


See tehnika töötab, kuid kujutage ette, et soovite pärast seda teha **selliseid samme**, näiteks filtreerida väikesed numbrid välja ja seejärel liita need kokku. Sa peaksid **nähtavalt** rohkem selliseid tagasikutseid tegema:


```javascript
doubleNumbers(input, function(doubled) {
filterBigNumbers(doubled, function(filtered) {
sumNumbers(filtered, function(total) {
console.log("Final result:", total)
})
})
})
```


See on Hard lugeda ja segane. Seda stiili nimetatakse **tagasilöögi põrguks** ja see on täpselt see, mille parandamiseks `Promise` loodi.


## Samaaegsus lubadustega

<chapterId>30fddaca-729f-5c8d-bf86-8dfc7b3c9800</chapterId>


Lubadus on sisseehitatud JavaScript-objekt, mis kujutab väärtust, mis **tulevikus** valmis saab.


Me võime luua sellise lubaduse:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve("It worked!") // This means everything went OK
})
```


Uue lubaduse()` osa loob lubaduse.


Selle sees anname sellele kahe parameetriga funktsiooni:



- `resolve`, on funktsioon, mida me kutsume, kui kõik on edukas
- `reject`, on funktsioon, mida me kutsume, kui midagi läheb valesti


Ülaltoodud näites lahendame selle kohe sõnumiga `"See töötas!".


### `.then()`


Selleks, et teha midagi **pärast** lubaduse täitmist, kasutame `.then()`:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve(100) // This means everything went OK
})

promise.then(result => {
console.log("The result is:", result)
})
```


See trükib:


```
The result is: 100
```


Väärtus, mille me edastasime `resolve()`-le, saadetakse funktsioonile `.then()` kui `result`.


Simuleerime ülesannet, mis võtab 2 sekundit, kasutades `setTimeout`:


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


See ootab 2 sekundit ja seejärel prindib:


```
Done waiting!
```


### `reject()`


Loome lubaduse, mis **ei õnnestu**:


```javascript
const failingPromise = new Promise((resolve, reject) => {
reject("Something went wrong")
})
```


Kui me nüüd kasutame `.then()`, siis ei juhtu midagi, sest `.then()` käsitleb ainult edu.


Vigade käsitlemiseks kasutame `.catch()`:


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


See prindib ainult


```
Caught an error: Something went wrong
```


Funktsioonile `reject()` edastatud väärtus saadetakse funktsioonile `.catch()`.


Ehitame lubaduse, mis **mõnikord töötab ja mõnikord ebaõnnestub**, lähtudes mõnest tingimusest.


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


Nüüd saame seda kutsuda ja käsitleda mõlemat juhtumit:


```javascript
checkNumber(5)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


See trükib:


```
Success: Positive number
```


Ja kui me proovime teise numbriga:


```javascript
checkNumber(-1)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


See trükib:


```
Failure: Not a positive number
```


### Operatsioonide aheldamine `Promise`s abil



Me võime oma varasema näite ümber kirjutada, kasutades `Promise`, ja see näeb palju puhtam välja.


Alustame meie kahekordistamisfunktsiooni uue versiooni kirjutamisega, kuid seekord tagastab see **lubadus**:


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


Nüüd saame kasutada `.then()`, et öelda JavaScriptile, mida tulemusega teha:


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


See trükib:


```
Doubled numbers: [ 2, 4, 6 ]
```


Seni töötab see samamoodi nagu tagasikutsuversioon, kuid nüüd on koodi lihtsam laiendada ja lugeda.


Oletame, et tahame lisada rohkem samme:


1. Kõigepealt kahekordistage kõik numbrid

2. Seejärel eemaldage numbrid, mis on väiksemad kui 4

3. Lõpuks lisage need kõik kokku


Me võime kirjutada iga sammu jaoks ühe funktsiooni, mis kõik kasutavad lubadusi:


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


Nüüd saame neid **kettaga** kokku siduda:


```javascript
const input = [1, 2, 3]

doubleNumbers(input)
.then(filterBigNumbers)
.then(sumNumbers)
.then(
result => console.log("Final result after all steps:", result)
)
```


See trükib:


```
Final result after all steps: 10
```


Vaatame läbi, mida see teeb:


1. `doubleNumbers` kahekordistab massiivi: `[2, 4, 6]`

2. `filterBigNumbers` eemaldab kõik ≤ 3: `[4, 6]`

3. `sumNumbers` liidab ülejäänud numbrid: `4 + 6 = 10`

4. Lõpuks trükime tulemuse välja.


Iga `.then()` ootab, et enne seda sammu lõpetataks. Seega saame luua **tegevuste ahela** ilma pesitsuseta. See muudab koodi loetavamaks ja lihtsamaks vigade kõrvaldamiseks.


## Samaaegsus koos `async`/`await`iga

<chapterId>6e93d29f-c8bf-5fd1-a9c9-4e794ee6cbd0</chapterId>


Me nägime, kuidas `Promise` ahelad aitavad meil vältida tagasikutsumise põrgut, kuid neid võib siiski veidi Hard lugeda, kui on kaasatud palju samme.


Siin tulevadki mängu `async` ja `await`. Need võimaldavad meil kirjutada asünkroonset koodi, mis näeb välja nagu sünkroonne kood**, mis teeb selle arusaadavamaks.


### Mis on `async`?


Kui kirjutate võtmesõna `async` enne funktsiooni, mähib JavaScript automaatselt funktsiooni tagastusväärtuse Promise'ile.


Vaatame lihtsat näidet:


```javascript
async function greet() {
return "hello"
}
```


Kui te kutsute seda funktsiooni:


```javascript
const result = greet()
console.log(result)
```


Sa näed seda:


```
Promise { 'hello' }
```


Kuigi te just tagastasite stringi, muudab JavaScript selle teie jaoks Promise'iks. Tegeliku väärtuse saate kätte, kasutades `.then()` näiteks nii:


```javascript
greet().then( result => console.log(result) ) // prints "hello"
```


Või võite kasutada `await`...


### Mis on "ootamine"?


Võtmesõna `await` ütleb JavaScriptile: "oota, kuni see lubadus on tehtud, ja anna mulle siis tulemus."


Kuid te saate kasutada `await` ainult **asünkroonse funktsiooni sees**.


Kirjutame näite ümber, kasutades `await`:


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


Nüüd saame tulemust kasutada nii, nagu oleks see tavaline väärtus.


Teeme nüüd midagi veidi kasulikumat.


### Viivituse simuleerimine `await`iga


Loome lihtsa `wait` funktsiooni, mis võtab argumendiks hulga millisekundeid ja lihtsalt lahendab selle hulga millisekundite järel, ilma midagi muud tegemata:


```javascript
function wait(ms) {
return new Promise(resolve => {
setTimeout(resolve, ms)
})
}
```


Proovime seda kasutada:


```javascript
async function test() {
console.log("waiting 2 seconds...")
await wait(2000)
console.log("done waiting")
}

test()
```


See trükib:


```
waiting 2 seconds...
done waiting
```


Võite mõelda "ootama" kui "peatuge siin, kuni lubadus on tehtud, siis jätkake"


See võimaldab teil kirjutada koodi **top-to-bottom** viisil, mis käitub asünkroonselt, ilma `.then()`-kutsete ahelata.


### Ootab andmeid


Kasutame uuesti meie eelmist näidet, kus me kahekordistame numbreid, seejärel filtreerime ja seejärel summeerime. Kuid seekord kasutame `async`/`await`.


Loome 3 funktsiooni, mis simuleerivad ootamist ja tagastavad Promise'i:


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


Nüüd kirjutame `async` funktsiooni nende ühendamiseks:


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


See trükib:


```
Final result: 10
```


Seda on palju lihtsam lugeda kui `.then()` ahelat või tagasikutsumise pesitsemist.


See näeb välja nagu tavaline samm-sammuline programm, kuid käitub siiski asünkroonselt.


## Asünkroonsed iteraatorid

<chapterId>438b037d-9931-56d7-9052-7b4470f3c75b</chapterId>


Te juba õppisite **iteraatoritest** ja kuidas me saame kasutada `for...of`, et teha tsüklit massiividel ja muudel iteratiivsetel asjadel.


Aga mis siis, kui andmete, mida me tahame itereerida, saabumine võtab aega?


Mõnikord tahame me loopida asju, mis saabuvad **asünkroonselt**, näiteks sõnumeid vestlusest, ridu failist või numbreid aeglasest allikast.


Selleks annab JavaScript meile **async-iteraatorid**.


### Asünkroonsed generaatori funktsioonid


Kõige lihtsam viis asünkroonse iteraatori loomiseks on kasutada **asünkroonse generaatori funktsiooni**.


Me kirjutame seda nii:


```javascript
async function* generateNumbers() {
yield 1
yield 2
yield 3
}
```


See näeb välja nagu tavaline generaator, kuid selle ees on `async`.


Nüüd saame kasutada `for await...of` väärtuste tarbimiseks:


```javascript
async function run() {
for await (const n of generateNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


See trükib:


```
Got number: 1
Got number: 2
Got number: 3
Done!
```


Mis vahe on siis tavalise generaatoriga?


Erinevus seisneb selles, et nüüd saame kasutada `await'i` generaatori sees.


Teeme jälle viivitusabi:


```javascript
function wait(ms) {
return new Promise(resolve => setTimeout(resolve, ms))
}
```


Nüüd anname numbreid **vaikselt**:


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


Proovige seda kasutada:


```javascript
async function run() {
for await (const n of generateSlowNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


### Miks kasutada asünkroonseid iteraatoreid?


Asünkroonsed iteraatorid on kasulikud, kui:



- Kõik väärtused ei saabu korraga.
- Sa tahad neid käsitleda ükshaaval, **kui nad tulevad**.
- Sa töötad Promises'iga ja soovid loopida puhtalt.


Näiteks kui soovite laadida sõnumeid vestlusserverist ükshaaval või laadida suurt faili osade kaupa, annavad asünkroonilised iteraatorid võimaluse kirjutada `for`-silmus, mis töötab hilinenud andmetega.


### `Symbol.asyncIterator`


Me võime kasutada asünkroonseid iteraatoreid ka kohandatud klassides.


Siin on näide, mis toodab numbreid viivitusega:


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


Nüüd saame kasutada `for await...of` nagu varemgi:


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


See võimaldab teil luua objekte, mida saab iteratsiooniga asünkroonselt üle vaadata


## Assignment süntaksisuhkur

<chapterId>8b1ba7d8-ecfd-5470-b86e-73cb84ccc8b7</chapterId>


"Süntaksisuhkur" tähendab, et midagi kirjutatakse lühemalt või lihtsamalt, muutmata selle toimimist. See on lihtsalt kenam viis sama asja väljendamiseks.


JavaScriptil on mõned sisseehitatud süntaksisuhkrud, mis võimaldavad meil kirjutada puhtamaid ja lühemaid deklaratsioone. Selles peatükis vaatleme, kuidas määrata väärtusi tingimuse alusel, uuendada muutujaid matemaatikaga, tõmmata väärtusi massiividest või objektidest ning kopeerida või kombineerida neid lihtsama süntaksiga.


### Ternaarne operaator


JavaScriptis saate määrata tingimuse alusel väärtuse, kasutades **ternatiivset operaatorit**, mis on lühike viis kirjutada `if...else`.


Selle asemel, et teha:


```javascript
let message

if (isMorning) {
message = "Good morning"
} else {
message = "Hello"
}
```


Võite kirjutada:


```javascript
const message = isMorning ? "Good morning" : "Hello"
```


See tähendab:



- Kui `isMorning` on true, kasuta `"Good morning"`
- Vastasel juhul kasutage `"Tere"`


Üldine vorm on järgmine:


```javascript
condition ? valueIfTrue : valueIfFalse
```


Seda saab kasutada ka teiste väljendite sees:


```javascript
console.log(isSunny ? "Go outside" : "Stay in")
```


Lihtsalt kasutage seda **ühikeste** otsuste tegemiseks. Kui loogika on keeruline, kasutage `if...else`.


### Alternatiivsed Assignment operaatorid


JavaScriptil on **sortcut-operaatorid**, millega saab teha ülesandeid koos operatsioonidega.


Vaatame tavalist viisi:


```javascript
let counter = 1
counter = counter + 1
```


Seda saab lühendada:


```javascript
let counter = 1
counter += 1 // same as counter = counter + 1
```


Siin on kõige levinumad:


| Operator | Meaning             |
| -------- | ------------------- |
| `+=`     | add and assign      |
| `-=`     | subtract and assign |
| `*=`     | multiply and assign |
| `/=`     | divide and assign   |

Näited:


```javascript
let score = 10
score += 5  // now score is 15
score *= 2  // now score is 30
score -= 10 // now score is 20
```


Need on kasulikud, kui soovite muutujat uuendada, kasutades selle enda väärtust.


### Destruktureerimine


**Destruktureerimine** võimaldab teil võtta väärtusi massiividest või objektidest ja salvestada need lihtsalt muutujatesse.


#### Arrays


Oletame, et teil on:


```javascript
const colors = ["red", "green", "blue"]
```


Selle asemel, et teha:


```javascript
const first = colors[0]
const second = colors[1]
```


Saate teha:


```javascript
const [first, second] = colors
```


See määrab:



- "esimene" kuni "punane"
- "teine" kuni "Green"


Saate ka väärtusi vahele jätta:


```javascript
const [,, third] = colors
console.log(third) // blue
```


#### Objektid


Saate ka objektidest väärtusi välja võtta:


```javascript
const user = { name: "Alice", age: 30 }

const { name, age } = user
console.log(name) // Alice
console.log(age)  // 30
```


Kui omadusel on erinev nimi kui soovitud muutuja, saate selle ümber nimetada:


```javascript
const { name: username } = user
console.log(username) // Alice
```


Destruktureerimine muudab teie koodi puhtamaks, kui töötate objektide ja massiividega.


### Levita süntaks


**spread süntaks** kasutab `...` väärtuste lahtipakkimiseks või kopeerimiseks.


#### Arrays


Saate massiive kopeerida või ühendada:


```javascript
const a = [1, 2]
const b = [3, 4]

const both = [...a, ...b]
console.log(both) // [1, 2, 3, 4]
```


Saate ka massiivi kloonida:


```javascript
const original = [10, 20, 30]
const clone = [...original]
```


#### Objektid


Sama saab teha ka objektidega:


```javascript
const a = { x: 1 }
const b = { y: 2 }

const merged = { ...a, ...b }
console.log(merged) // { x: 1, y: 2 }
```


Saate ka väärtusi tühistada:


```javascript
const user = { name: "Alice", age: 30 }
const updated = { ...user, age: 31 }

console.log(updated) // { name: "Alice", age: 31 }
```


See on väga kasulik objektide uuendamisel ilma originaali muutmata.


# NodeJS

<partId>42fe4d49-dace-5135-bb9e-b9d75034fb2a</partId>


## Kuidas me jõudsime Node'ile

<chapterId>0da1d60c-06c9-54e6-a181-ae7dabf6e3b8</chapterId>


Selles peatükis õpime veidi ajaloolist konteksti JavaSi ja NodeJSi kohta.


Ajalooline kontekst on tarkvara puhul väga oluline, sest me kasutame sageli teiste inimeste loodud vahendeid ja seega mõjutavad meid nende poolt minevikus tehtud otsused.


Nende otsuste põhjuste mõistmine ja see, kuidas meie kasutatavad vahendid on saanud selliseks, nagu nad on, aitab meil end veidi vähem segaduses tunda, mida me teeme.


### JavaScripti päritolu


JavaScript sai alguse lihtsa keelena, mille eesmärk oli muuta veebilehed interaktiivseks.


1990ndatel lisasid veebibrauserid, nagu Netscape Navigator, JavaScripti, et arendajad saaksid kirjutada koodi, mis töötab otse brauseris.


Esialgne idee oli, et Java oleks põhikeeleks veebilehtede tegemiseks (nn Java-apletid) ja JavaScript vaid vähemtähtsate asjade jaoks.


Põhidisaini tegi Brendan Eich, kes sel ajal oli Netscape'i töötaja, vähem kui kahe nädalaga.


Kuid enamik inimesi eelistas Java asemel kasutada Java't. Lisaks olid Java-aplettidel tol ajal mõned turvaprobleemid, nii et lõpuks loobuti Java valikust ja JavaScriptist sai de facto veebiarenduse standard.


### V8 mootor


JavaScript on interpreteeritud keel, erinevalt kompileeritud keeltest nagu C.


Kompileerimiskeeles kirjutatud kood muudetakse binaarseks ja binaarskeem suunatakse otse arvuti protsessorisse.


![](assets/en/6.webp)


Teisalt kipuvad interpreed keeled olema kasutajasõbralikumad ja on lähemal sellele, kuidas inimesed mõtlevad ("kõrge tase") kui sellele, kuidas masinad töötavad ("madal tase"); seega on nende koodide käivitamiseks tavaliselt ehitatud virtuaalmasin.


Virtuaalmasin on spetsiaalne programm, mis asub teie kirjutatud koodi ja protsessori vahel ning täidab teie koodi (kuna protsessor ei saa sellest aru).


See võimaldab teil programmeerida, teadmata liiga palju aluseks olevast masinast, kuid sellel on ka oma hind, mis puudutab jõudlust, sest arvuti ei käivita ainult teie programmi; ta käivitab programmi (virtuaalmasinat), mis käivitab teie programmi.


Kuna veebirakendused muutusid üha keerulisemaks, tekkis vajadus parandada JavaScripti jõudlust. V8-mootor on Google Chrome'i JavaScripti interpretaator. See töötati välja Google'is ja avaldati 2008. aastal.


Kui vanemad JavaScripti mootorid olid enamasti traditsioonilised virtuaalmasinad, siis V8 mootor on JIT (just-in-time) kompilaator.


JavaScript-kood suunatakse V8-mootorile ja mootor püüab osa sellest kompileerida jooksvalt emakeelsete binaarsete failidena. See võimaldab teil saada kõrgtaseme keele kogemust, kuid jõudlus on veidi lähemal madala taseme keeltele. See on muutnud JavaScripti maailma kiireimaks kõrgtasemeliseks keeleks, mis on justkui "mõlema maailma parim".


### NodeJSi tööaeg


Kuigi JavaScripti oli lihtne kasutada ja see oli üsna kiire, oli pärast V8 JavaScript'i ilmumist üks suur piirang: see võis töötada ainult brauseris.


Miks on see probleem?


Kuna veebilehitsejad täidavad miljonitest erinevatest internetiallikatest hangitud koodi, võivad nad kergesti sattuda pahavara hulka, seega on nad ülejäänud operatsioonisüsteemist "liivakastis".


![](assets/en/7.webp)


JavaScript ei saanud juurdepääsu failisüsteemile ja muudele arvuti kohalikele ressurssidele (vähemalt mitte nii lihtsalt nagu teised keeled), nii et see oli oluline piirang selle abil loodavate rakenduste osas.


2009. aastal avaldas Ryan Dahl NodeJSi, mis on runtime, mis võimaldab kasutada V8 mootorit väljaspool brauserit, otse arvuti emakeelses operatsioonisüsteemis. See lisab ka palju funktsioone, mis on kasulikud serveripoolsete ja käsurea programmide kirjutamiseks. Näiteks saab NodeJS-i kasutada veebiserveri loomiseks, failide lugemiseks ja kirjutamiseks või ülesannete automatiseerimiseks mõeldud tööriistade loomiseks.


![](assets/en/8.webp)


Selles kursuses oleme seni uurinud JavaScripti funktsioone, mis on olemas nii brauseris kui ka NodeJSis. Need funktsioonid võimaldasid meil andmeid defineerida ja nendega abstraktselt manipuleerida. Järgmistes õppetundides uurime funktsioone, mis on NodeJS-i spetsiifilised ja võimaldavad meil suhelda operatsioonisüsteemiga.


## Käsurea argumendid

<chapterId>960d20f3-c424-5d51-a041-ef17d2e94b6d</chapterId>


NodeJS võimaldab meil muu hulgas ehitada CLI-sid (Command Line Interfaces).


Selleks on meil vaja võimalust saada käsurea argumente, mida Node'is tehakse sisseehitatud `process` objekti abil.


### `process`


NodeJS pakub spetsiaalset objekti nimega `process`, mis kujutab jooksvat programmi.


Selle abil saate kontrollida keskkonda, praegust töökataloogi ja vajaduse korral isegi programmist väljuda.


Näiteks:


```javascript
console.log(process.platform)
```


See väljastab operatsioonisüsteemi platvormi, näiteks `win32`, `linux` või `darwin` (Mac).


### `process.argv`


Kui käivitate NodeJS-programmi terminalist, saate skripti nime järel edastada täiendavaid sõnu (argumente). Need salvestatakse faili `process.argv`.


Näiteks kui käivitate selle käsu:


```
node my_script.js alpha beta
```


Argumente saab välja trükkida nii:


```javascript
console.log(process.argv)
```


Väljund võib välja näha selline:


```
[ '/path/to/node', '/path/to/my_script.js', 'alpha', 'beta' ]
```


Esimesed kaks elementi on alati Node'i tee ja teie skripti tee. Kõik täiendavad sõnad, mida te skriptile edastasite, tulevad pärast seda.


Massiivi `process.argv` saab lõigata nagu mis tahes muud massiivi, kasutades meetodit `.slice()`, nii et saada ainult need argumendid, mis on edastatud, võite teha järgmist


```javascript
const args = process.argv.slice(2)

console.log(args)
```


Juurdepääs kasutaja poolt edastatavatele argumentidele on käsurea rakenduste arendamiseks hädavajalik.


## Moodulid

<chapterId>4e1651a5-65fd-50bc-b22a-40313d5659ca</chapterId>


JavaScripti töörežiimid, nagu NodeJS, käsitlevad tavaliselt iga JavaScript-faili eraldi moodulina.


Mõelge moodulist kui kastist. Kastil on oma privaatne ruum, nii et selles deklareeritud muutujad ja funktsioonid ei sega teiste kastide koodi. Põhimõtteliselt on igal moodulil oma ulatus.


Moodul võib eksportida osa oma sisust, muutes selle teistele moodulitele kättesaadavaks, ning importida teiste moodulite poolt eksporditud sisu. JavaScript võimaldab eksportida ja importida sisu moodulite vahel, et ühendada erinevaid faile.


JavaScript-programm koosneb sageli mitmest moodulist, mis on omavahel seotud.


Miks kasutada mooduleid? Jagades oma koodi mooduliteks, saate oma programmi organiseerida väiksemateks, selgemateks ja taaskasutatavateks osadeks. Iga moodul võib keskenduda vaid ühte tüüpi ülesandele, näiteks matemaatiliste arvutuste käsitlemisele, failidega töötamisele või teksti vormindamisele.


### CommonJS moodulid


NodeJSis on moodulite haldamiseks kõige levinum süsteem nimega **CommonJS**.


Selles süsteemis saate jagada (eksportida) koodi moodulist, kasutades `module.exports` ja laadida (importida) seda teise faili, kasutades `require()`.


Et midagi väljaspool moodulit kättesaadavaks teha, määrate selle moodulisse `module.exports`:


```javascript
const greeting = "Hello!"

module.exports = greeting
```


Siin on string `"Hello!"` see, mida see moodul ekspordib.


Teisest failist eksporditud koodi kasutamiseks kasutate funktsiooni `require()` koos selle faili teekonnaga:


```javascript
const greeting = require("./greeting.js")

console.log(greeting)
```


See trükib:


```
Hello!
```


Saate eksportida mitu asja, koondades need anonüümsesse objekti, näiteks


```javascript
const greeting1 = "hello"

const greeting2 = "hi"

module.exports = {
greeting1, greeting2
}
```


CommonJS oli moodulisüsteem, mille NodeJS algselt üle võttis. Hiljem lisandusid ka ES-moodulid.


### ES moodulid


NodeJS toetab ka teist tüüpi mooduleid, mida nimetatakse **ES-mooduliteks** ja mis on veebiarenduses populaarsed. Nad kasutavad võtmesõnu `export` ja `import`.


ES-moodulid töötati välja brauseri jaoks ja lisati alles hiljem Node'ile. Kui soovite neid kasutada, peate võib-olla kasutama faililaiendina `.mjs` asemel `.js`, sõltuvalt sellest, millist Node'i versiooni te kasutate.


Ühes failis nimega `greeting.mjs` kirjutame me järgmist


```javascript
export const greeting = "Hello!"
```

Nagu näete, ekspordime konstanti otse sinna, kus see defineeritakse


Teises failis nimega `index.mjs` impordime selle:


```javascript
import { greeting } from "./greeting.mjs"

console.log(greeting)
```


Saate eksportida erinevaid deklaratsioone faili erinevatesse osadesse, näiteks


```javascript
export const num = 10

export function double (x) {
return x*2
}
```


### NodeJSi standardraamatukogu


NodeJS sisaldab ka palju sisseehitatud mooduleid. Need on NodeJSi poolt pakutavad valmismoodulid, mis aitavad tavaliste ülesannete täitmisel, näiteks failide lugemisel, operatsioonisüsteemiga töötamisel või võrguga ühendamisel.


Näiteks annab moodul `os` teavet teie operatsioonisüsteemi kohta:


```javascript
const os = require("os")

console.log(os.platform())
```


Sa ei pea neid sisseehitatud mooduleid paigaldama, need tulevad koos NodeJSiga. Need moodustavad tööaja "standardraamatukogu" ja neid kasutab enamik Node'i rakendusi selliste asjade tegemiseks nagu failide lugemine või suhtlemine interneti kaudu.


Järgmistes peatükkides tuuakse mõned kasulikud näited nende kasutamise kohta.


## Moodul `fs`

<chapterId>911e953a-35ae-5ee7-bd74-372501c32e81</chapterId>


Moodul `fs` (lühend **failisüsteemist**) on osa NodeJSi standardraamatukogust. See võimaldab teil töötada oma arvutis olevate failide ja kataloogidega: saate lugeda faile, kirjutada faile, kustutada neid, ümber nimetada neid ja palju muud.


Selle kasutamiseks peate kõigepealt importima selle oma faili ülaosas:


```javascript
const fs = require("fs")
```


### Sünkroonimise API


Lihtsaim viis `fs` kasutamiseks on selle **sync** meetodid.


Need meetodid blokeerivad programmi, kuni nad lõpetavad (nii et järgmine koodirida ei käivitata enne, kui operatsioon on lõpetatud).


Siin on näide faili sünkroonsest lugemisest:


```javascript
const fs = require("fs")

const data = fs.readFileSync("example.txt", "utf8")

console.log(data)
```


Kui teie skriptiga samas kataloogis on olemas fail nimega `example.txt`, siis trükib see selle sisu.


Faili saab kirjutada ka sünkroonselt:


```javascript
const fs = require("fs")

fs.writeFileSync("output.txt", "Hello from Node!")

console.log("File written!")
```


See loob (või kirjutab üle) teksti faili nimega `output.txt`.


Siin on mõned tavalised operatsioonid, mida saate selle APIga teha:


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


Sync API on lihtne ja hea väikeste skriptide jaoks, kuid kuna see blokeerib programmi, kuni see on valmis, võib see aeglustada asju, kui töötate suurte failide või serveriga.


### Tagasikutsumise asünkroonne API


**tagasivõtu API** ei ole blokeeriv: see võimaldab NodeJSil jätkata muude asjade tegemist, samal ajal kui failioperatsioon toimub.


Selle asemel, et tagastada tulemus otse, võtab see funktsiooni (**tagasilöögi**), mida kutsutakse üles, kui operatsioon on lõpetatud.


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


See juhtub järgmiselt:



- `fs.readFile` alustab lugemist `example.txt`.
- NodeJS ei oota, vaid liigub edasi, et täita muud koodi, mille olete võib-olla kirjutanud.
- Kui faili lugemine on lõpetatud, käivitub tagasikutsumine:



  - Kui ilmnes viga, sisaldab `err` veateadet.
  - Vastasel juhul sisaldab `data` sisu.


Nii kirjutate faili:


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


Sama mõte: programm ei peatu faili kirjutamise ajal.


Mõned näited asjadest, mida saate selle APIga teha:


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


Tagasikutsumise API on parem serverite ja suurte ülesannete jaoks, sest see ei blokeeri programmi, kuid sisseehitatud tagasikutsumised võivad muutuda segaseks, kui teete palju operatsioone ahelatult. Seepärast lisati lubadusel põhinev asünkroonne API.


### Promise asünkroonne API


Promise-põhine API on kaasaegne ja töötab suurepäraselt koos `.then()` ja `async/await`iga. See on saadaval kui `fs.promises`.


Teil on vaja importida omadus `promises`:


```javascript
const fs = require("fs").promises
```


Kasutades `.then()`:


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


Või veelgi parem, kasutades `async/await`:


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


Kirjutamine faili:


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


Tavapärane API näidete loetelu:


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


Kui te kirjutate koodi, peate sageli kasutama teiste inimeste kirjutatud koodi; näiteks raamatukogusid, mis aitavad teil töötada kuupäevade, värvide, serverite või peaaegu kõigega muuga.


Failide käsitsi allalaadimise ja kopeerimise asemel võite kasutada **pakettide haldurit**.


Paketihaldur on vahend, mis:



- allalaadimispaketid
- jälgib, milliseid pakette teie projekt vajab
- tagab, et kõigil teie meeskonnaliikmetel on samad pakettide versioonid


### Mis on NPM


NodeJS-i maailmas on kõige populaarsem paketihaldur **NPM**, mis tähendab *Node Package Manager*.


NodeJSi installimisel saate NPMi automaatselt.


Saate kontrollida, kas teil on NPM olemas, käivitades selle oma terminalis:


```
npm -v
```


See prindib teie NPM-i versiooni, näiteks:


```
10.2.1
```


### Paketi loomine


NodeJSis on **pakett** lihtsalt kataloog, milles on fail "package.json".


Loome ühe samm-sammult.


1. Tehke oma projekti jaoks uus kaust:


```
mkdir my_project
cd my_project
```


2. Käivita see käsk:


```
npm init
```


See käivitab interaktiivse seadistuse, mis esitab teile küsimusi nagu projekti nimi, versioon, kirjeldus jne.


Kui te ei soovi kõigele vastata ja nõustute lihtsalt vaikimisi seadistustega, võite kasutada:


```
npm init -y
```


Pärast selle käivitamist näete oma kaustas uut faili nimega:


```
package.json
```


### `pakett.json`


Fail "package.json" on lihtsalt JSON-fail, mis salvestab metaandmeid teie projekti kohta.


Siin on üks näide:


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


Mõned olulised valdkonnad:



- `nimi`: teie paketi nimi
- `version`: praegune versioon
- `main`: alguspunkti fail (nagu `index.js`)
- `skriptid`: käsud, mida saab käivitada (nagu `npm start`)
- `dependencies`: loetleb kõik paketid, millest teie projekt sõltub


### Paketi paigaldamine


Oletame, et soovite kasutada teatud paketti nimega `picocolors`, et lisada oma terminali väljundile värve.


Saate selle paigaldada, käivitades:


```
npm install picocolors
```


Nüüd saate seda oma projektis kasutada. Tehke `index.js` fail koos


```javascript
const pico = require('picocolors')

console.log(
pico.green("This text is green!")
)
```


ja proovige seda käivitada. Terminal peaks trükkima teksti värvilise versiooni.


Mida tegi NPM ?



- See laadis paketi alla ja salvestas selle alamkausta `node_modules/`
- see lisas teie `package.json'ile` kirje `dependencies` alla
- see uuendas faili `package-lock.json`


Mis on `package-lock.json` ?


### `pakett-lukk.json`


Selle faili loob NPM automaatselt.


Te võite küsida, et kui meil on juba olemas `package.json`, siis milleks meile veel üks fail?

Siin on põhjus:



- `package.json` ütleb lihtsalt, millist paketi versiooni **vahemikku** teie projekt vajab.

Näide:


```json
"dependencies": {
"picocolors": "^1.1.0"
}
```


`^1.1.0` tähendab "mis tahes versiooni, mis ühildub versiooniga 1.1.x", seega on see paindlik.



- `package-lock.json` **külmutab** iga üksiku paketi ja nende allsõltuvuste täpsed versioonid, nii et igaüks, kes teie projekti installeerib, saab täpselt sama toimiva seadistuse.


Miks on see oluline?


Kui te töötate meeskonnas või kui te juurutate oma projekti serverisse või kui te tuled selle juurde tulevikus tagasi, siis tahate veenduda, et see töötab endiselt samamoodi.

Kui paketid on uuendatud ja te installidate uuesti ilma lukustusfailita, võite saada veidi erineva versiooni, mis käitub teisiti.


Hoides "package-lock.json" oma projektis, installib NPM alati täpselt seal loetletud versioonid, tagades, et kõigil on sama keskkond.


`package-lock.json` lukustab kõik väga spetsiifilise versiooni, et projekt oleks teistel masinatel paremini reprodutseeritav.


Aga kui teie paketti peavad kasutama paljud inimesed, võite selle asemel otsustada seda mitte kinnitada, nii et NPM leiab ainult faili `package.json` ja tal lubatakse automaatselt paigaldada viimased versioonid, mis on selles failis lubatud.


Kuid need on asjad, mille pärast peaksite muretsema hiljem, kui hakkate oma koodi avaldama. Praegu tutvustasime NPM-i põhitõdesid lihtsalt selleks, et te saaksite leida ja kasutada teiste arendajate poolt avaldatud raamatukogusid oma projektides.



## Võrgustik NodeJSis

<chapterId>f2cabd8b-754b-5c97-8d6a-8412a9a184c7</chapterId>


NodeJS-i kasutatakse sageli backend-keelena: saate oma skripti muuta serveriks ja kasutada seda ka päringute tegemiseks teistele serveritele.


Selles peatükis tutvustame mõningaid põhilisi võrgufunktsioone, mis võimaldavad seda teha.


### `fetch()`


Kui soovite, et teie programm laadiks alla andmeid veebisaidilt või API-lt, peate tegema **HTTP päringu**.


NodeJSi kaasaegsetes versioonides saab kasutada sisseehitatud funktsiooni `fetch()`.


Siin on näide GET päringu tegemisest API-le:


```javascript
const response = await fetch("https://jsonplaceholder.typicode.com/posts/1")
const data = await response.text()

console.log(data)
```


Kui te seda käivitate, näete midagi sellist:


```
{
"userId": 1,
"id": 1,
"title": "...",
"body": "..."
}
```


See juhtub järgmiselt:


1. `fetch()` võtab URL-i ja teeb päringu.

2. See tagastab **Promise**, mis vastab `Response` objektile.

3. `response.text()` loeb vastuse keha stringina.


Kuid tagasi saadav string on tegelikult JSON. Mis see on?


### JSON


Veebipõhiste rakendusliidestega töötades saadetakse ja saadetakse andmeid sageli **JSONina**, mis tähendab JavaScript Object Notation.


JSON on lihtsalt tekstivorming, mis näeb välja nagu JavaScripti objektid. Näiteks:


```json
{
"name": "Alice",
"age": 30,
"likes": ["apples", "bananas"]
}
```


Objekt `JSON` on JavaScriptis sisseehitatud abivahend, mida saab kasutada selle andmeformaadiga töötamiseks.


JavaScript-objekti saab teisendada JSON-stringiks, kasutades `JSON.stringify()`:


```javascript
const user = { name: "Alice", age: 30 }

const jsonString = JSON.stringify(user)

console.log(jsonString)
```


See trükib:


```
{"name":"Alice","age":30}
```


JSON-teksti saab teisendada ka tagasi JavaScript-objektiks, kasutades `JSON.parse()`:


```javascript
const jsonText = '{"name":"Bob","age":25}'

const obj = JSON.parse(jsonText)

console.log(obj)
```


See trükib:


```
{ name: 'Bob', age: 25 }
```


Olge ettevaatlik: `JSON.parse()` viskab vea, kui string ei ole kehtiv JSON.


```javascript
JSON.parse("not json") // ❌ Error!
```


Seega veenduge, et string on õigesti vormindatud.


### `http` server


NodeJS võimaldab luua veebiserveri ilma midagi muud paigaldamata.


Saate kasutada sisseehitatud `http` moodulit, et käsitleda klientide päringuid ja saata vastuseid tagasi.


Siin on väga lihtne näide:


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


Kui käivitate selle skripti ja avate brauseris `http://localhost:3000`, näete:


```
Hello from NodeJS server!
```


See on see, mis toimub koodis:


1. Sa importisid `http` serveri Node'i standardraamatukogust.

2. `http.createServer()` loob serveri. Te andsite `http.createServer()`-le tagasikutsumise `(req, res) => {...}`, mis käivitatakse iga kord, kui keegi ühendub.

3. Sa määrasid vastusele staatuskoodi 200 (mis näitab edukat toimingut). Te võite lugeda http staatuskoodide kohta [siin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

3. `res.end()` saadab vastuse ja lõpetab ühenduse.

4. `server.listen(3000)` käivitab serveri pordil 3000.


Võite kontrollida ka `req.url` ja `req.method` päringus, et käsitleda erinevaid teekondi või päringutüüpe.


Näide marsruutimisega:


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


Need on väga lihtsad näited. Arenenumate serverite ehitamiseks laeb enamik arendajaid tõenäoliselt alla valmis backend library'd nagu [express](https://www.npmjs.com/package/express).


## Andmete töötlemine: puhvrid, sündmused, voogud

<chapterId>8c9623f0-a604-51a4-8fe4-871c849d3e3b</chapterId>


Selles peatükis tutvustame peamiselt kolme objektiklassi:



- `Buffer`, mis kujutab endast väikseid binaarsete andmete tükke
- `EventEmitter`, mida saab kasutada asünkroonse protsessi jälgimiseks, edastades signaale, mida nimetatakse "sündmusteks"
- `Stream`, mis võimaldab meil töödelda suurt osa andmetest ühe `Buffer` kaupa ja mis jälgib protsessi sündmuste saatmise kaudu


Need on professionaalses NodeJS-koodis äärmiselt levinud, nii et isegi kui te ei pruugi neid oma esimestes projektides kasutada, on hea saada põhiteadmised, kui teil on vaja nendega suhelda. neist


### Puhvrid


NodeJSis on **puhver** objektitüüp, mida kasutatakse binaarsete andmetega töötamiseks.


Puhvrist võib mõelda kui fikseeritud suurusega konteinerist toorainebaitide jaoks.


Siin on, kuidas luua stringist puhver:


```javascript
const buf = Buffer.from("hello")
console.log(buf)
```


See trükib midagi sellist:


```
<Buffer 68 65 6c 6c 6f>
```


Need numbrid (`68`, `65`, `6c` jne) on "hello" tähtede heksadetsimaalsed esitused.


Saate konverteerida selle tagasi stringiks näiteks nii:


```javascript
console.log(buf.toString())
```


See trükib:


```
hello
```


Saate luua ka teatud suurusega puhvri, mis on täidetud nullidega:


```javascript
const buf = Buffer.alloc(10)
console.log(buf)
```


See trükib midagi sellist:


```
<Buffer 00 00 00 00 00 00 00 00 00 00>
```


Saate kirjutada puhvrisse:


```javascript
buf.write("abc")
console.log(buf)
```


Ja te saate juurdepääsu üksikutele baitidele:


```javascript
console.log(buf[0]) // prints the ASCII number for 'a', which is 97
```


Puhvrid on eriti kasulikud, kui on vaja andmeid väga madalal tasemel manipuleerida.


### Sündmused


JavaScriptis on **sündmus** midagi, mis juhtub teie programmis ja millele saab reageerida.


Näiteks:



- faili laadimise lõpetamine
- taimer käivitub
- kasutaja klõpsab nupule
- võrgupäring tagastab andmed


**Sündmus** on lihtsalt signaal, et midagi on juhtunud, ja te saate kirjutada koodi, et neid sündmusi kuulata ja neile reageerida.


NodeJSis võivad paljud objektid sündmusi välja saata. Neid objekte nimetatakse **EventEmitteriteks**.


Siin on üks näide:


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


See trükib:


```
Hello! An event happened.
```


Siin on see, mis:


1. Loome objekti `EventEmitter`.

2. Me ütleme talle, et ta peab käivitama tagasilöögi iga kord, kui juhtub sündmus `"greet", kasutades `.on("greet")`.

3. Hiljem käivitame sündmuse `"greet"`, kasutades `.emit()`.

4. Meie tagasikutsumine täidetakse


Saate sündmusega koos edastada andmeid:


```javascript
emitter.on("greet",
(name) => console.log(`Hello, ${name}!`)
)

emitter.emit("greet", "Alice") // first argument is the type of event, second argument is the data we pass with this event
```


See trükib:


```
Hello, Alice!
```


Te saate registreerida kuulajaid ka teistele sündmustele:


```javascript
emitter.on("goodbye", () => {
console.log("Goodbye!")
})

emitter.emit("goodbye")
```


Te võite kinnitada sündmuse tüübile nii palju kuulajaid kui soovite ja te võite samast saatjast vallandada palju erinevaid sündmusi.


Paljud NodeJS-i objektid saadavad sündmusi, et teatada ülejäänud programmile, et midagi toimub.



### Mis on voolud?


Andmevood ühendavad puhvreid ja sündmusi, et aidata meil andmeid töödelda.


Kui me töötame failide, võrguandmete või isegi pika tekstiga, ei pea (või ei taha) me alati kõike korraga mällu laadida. See võib olla aeglane või isegi programmi kokkuvarisemine, kui andmed on liiga suured.


Selle asemel saame töödelda andmeid **pisut**, kui need saabuvad või neid loetakse, nagu joome vett läbi kõrre, selle asemel, et püüda kogu klaas korraga ära juua. Seda nimetatakse **vooluks**.


NodeJSis on voog objekt, mis võimaldab teil lugeda andmeid allikast või kirjutada andmeid sihtkohta **ühes tükis**.


NodeJSil on neli peamist voogude tüüpi:



- Readable**: voogude, millest saab andmeid lugeda (nagu faili lugemine)
- Writable**: voogud, kuhu saab andmeid kirjutada (nagu faili kirjutamine)
- Duplex**: voogude puhul on võimalik nii lugeda kui ka kirjutada
- Transform**: nagu dupleksvooge, kuid nad võivad andmete liikumise ajal neid muuta (transformeerida)


### Loetavad voolud


Oletame, et teil on töötlemiseks `bigfile.txt`. Saate luua lugemisvoo mooduli `fs` abil, et lugeda faili tükkhaaval.


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


Mis toimub siin?


1. `fs.createReadStream()` loob loetava voo.

2. Iga kord, kui faili osa on valmis, saadab voog sündmuse `data` ja annab meile "andmepalati" (puhver). Me trükime selle tükikese välja.

3. Kui kogu fail on loetud, käivitub sündmus `end`.

4. Kui esineb viga (näiteks faili ei ole olemas), käivitub sündmus `error`.


Nii saate lugeda hiiglaslikke faile ilma neid kõiki korraga mällu laadimata.


Kui soovime, et andmed jõuaksid kohale inimesele loetavas vormis (mitte binaarses), saame määrata voo kodeeringu:


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


Kood trükib nüüd faili inimloetaval kujul.


### Kirjutatavad voolud


Kirjutatav voog võimaldab saata andmeid kuhugi, tükkide kaupa.


Siin on näide kirjutamisest faili `target.txt` voo abil:


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


See juhtub järgmiselt:


1. `fs.createWriteStream()` loob kirjutatava voo.

2. Kirjutame sinna teksti, kasutades `.write()`.

3. Kui oleme lõpetanud, kutsume `.end()`, et voog sulgeda.

4. Kui kõik andmed on kirjutatud, saadetakse sündmus "finish".

5. Kui midagi läheb valesti, käivitub sündmus `error`.


Nii nagu loetavad, on ka kirjutatavad andmevood head suurte andmete jaoks, sest nad ei pea kõike korraga mälus hoidma.


### Torustikuvoolud


Üks kõige lahedamaid asju voogude puhul on see, et neid saab **toruga** ühendada: ühendada loetav voog otse kirjutatava vooga.


```javascript
const fs = require("fs")

const readable = fs.createReadStream("bigfile.txt")
const writable = fs.createWriteStream("target.txt")

readable.pipe(writable)
```


Siin:



- Loetav voog loeb failist `bigfile.txt`.
- Kirjutatav voog kirjutab faili `copy.txt`.
- `.pipe()` saadab andmed otse loetavast voost kirjutatavasse voogu.


### Dupleksvoolud


Dupleksvoog on nii loetav kui ka kirjutatav. Üks näide on võrgupesa: sinna saab andmeid saata ja sealt andmeid vastu võtta.


Siin on väga lihtne näide, mis kasutab moodulit `net`:


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


Selles näites:



- Objekt `socket` on kahepoolne voog.
- Sellesse saab `write()` kirjutada ja ka `data` sündmusi kuulata.


### Transformeerige voogusid


Transformatsioonivoog on kahesuunaline voog, mis muudab ka seda läbivaid andmeid.


Näiteks saate kasutada sisseehitatud `zlib` moodulit andmete pakkimiseks või dekompressiooniks.


Järgnevalt on kirjeldatud, kuidas faili transformeeriva voo abil kokku suruda:


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


Ja selle dekompressiooni tagasi:


```javascript
const readable = fs.createReadStream("bigfile.txt.gz")
const unzip = zlib.createGunzip()
const writable = fs.createWriteStream("bigfile.txt")

readable.pipe(unzip).pipe(writable)

writable.on("finish", () => {
console.log("File decompressed.")
})
```


Transformatsioonivood on väga kasulikud selliste ülesannete puhul nagu pakkimine, krüpteerimine või failiformaatide muutmine voogedastuse ajal.


### Vasturõhk


Mõnikord on kirjutatav andmevoog aeglane andmete töötlemisel. Kui surume andmeid kirjutatavasse andmevooga kiiremini, kui see suudab töödelda, võib tekkida probleeme. Seda nimetatakse **tagasilöögiks**.


Kui te kutsute meetodit `.write()` kirjutatavale voogule, siis see tagastab booleani, mis teatab teile, kas voog vajab pausi; te peate võib-olla kontrollima selle tagastusväärtust, näiteks nii:


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


See oli illustratiivne näide andmete manuaalsest suunamisest Readable'ist Writable'ile ja vasturõhu manuaalsest haldamisest.


Tavaliselt kasutame andmete edastamiseks meetodit `.pipe()`, mis käitleb vasturõhku automaatselt.


Nii et te peate tagasilöögi pärast muretsema ainult siis, kui te mingil põhjusel manuaalselt `.write()` kutsute.


## Lõppmärkus

<chapterId>139e2ab8-df67-525a-85f0-5a2fa5e478f2</chapterId>


Nii, see ongi kõik, kui sa järgisid õppetunde, siis peaksid nüüd suutma kirjutada mõned lihtsad programmid NodeJSis.


Ma soovitan teha täpselt seda: pärast põhitõdede õppimist on mõne isikliku projekti ehitamine parim viis harjutada ja saada paremaks programmeerijaks.


Tegelikult ei ole oluline, mida sa ehitad, oluline on see, et sa esitad endale väljakutse lahendada probleeme koodiga.


Kaasaegsed programmeerimiskeeled on uskumatult võimsad ja NodeJS on tõenäoliselt parim tööriistakast, millega oma teekonna selles etapis katsetada.


Palju õnne!


# Lõpposa


<partId>322624d8-6fbc-11f0-a67a-5b145f10afc1</partId>


## Arvamused ja hinnangud


<chapterId>3e93ac86-6fbc-11f0-8bae-9b2ed7914843</chapterId>

<isCourseReview>true</isCourseReview>

## Kokkuvõte


<chapterId>49b3b9b2-6fbc-11f0-9870-5f5adcd3a0eb</chapterId>


<isCourseConclusion>true</isCourseConclusion>