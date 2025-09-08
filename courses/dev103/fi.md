---
name: JavaScriptin ja NodeJS:n perusteet
goal: Opi JavaScript-ohjelmoinnin perusteet ja NodeJS-kehitys käytännön sovellusten ja työkalujen rakentamiseksi.
objectives: 

  - JavaScriptin perussyntaksin, -tyyppien ja -ohjauksen hallitseminen
  - Ymmärtää JavaScriptin funktioita, objekteja ja luokkia
  - Opi virheenkäsittely- ja virheenkorjaustekniikoita
  - Tutustu NodeJS:ään ja sen ekosysteemiin

---

# Aloita kehitysmatkasi


Tervetuloa JavaScriptin ja NodeJS:n kurssille.


JavaScript on maailman suosituin ohjelmointikieli: se on nykyaikaisten selainten komentosarjakieli, joten on käytännössä mahdotonta rakentaa nykyaikaista verkkosovellusta kirjoittamatta *jotain* JavaScriptiä; ja NodeJS-ajoaikakoodin avulla sitä voidaan käyttää myös selainten ulkopuolella, jolloin voidaan luoda skriptejä ja sovelluksia, jotka toimivat suoraan tietokoneella.


Tämä kurssi on tarkoitettu henkilöille, jotka ovat täysin uusia ohjelmoinnin parissa tai jotka ovat käyttäneet muita kieliä aiemmin, mutta haluavat ymmärtää, miten JavaScript toimii, erityisesti NodeJS:n yhteydessä.


Kurssin lopussa sinun pitäisi osata kirjoittaa omia ohjelmia JavaScriptillä, käyttää NodeJS:n standardikirjastoa sekä asentaa ja käyttää kolmannen osapuolen paketteja hyödyllisten työkalujen rakentamiseen.


+++
# Perus JavaScript

<partId>a617327c-e5a2-52ca-9380-c63f44623dd4</partId>


## Setup

<chapterId>ba05a290-1782-5268-87c9-62fd09590e05</chapterId>


Tässä osiossa asetamme koneemme kirjoittamaan ja suorittamaan ensimmäisen JavaScript-ohjelmamme.


JavaScript-ohjelma on vain kokoelma (yhtä tai useampaa) tekstitiedostoa, jotka sisältävät komentoja, jotka JavaScript-ajoaika suorittaa.


Näiden tekstitiedostojen nimet päättyvät yleensä tiedostopäätteeseen `.js`, kuten `my_script.js`, `my_program.js` jne.


Niiden sisältämät komennot on kirjoitettu JavaScript-ohjelmointikielellä.


JavaScript-runtime on erityinen ohjelma, joka suorittaa nämä tiedostot.


![](assets/en/1.webp)


### NodeJS-asennus


Yleisin JavaScript-ajoaika on NodeJS.


Voit asentaa sen noudattamalla [virallisia ohjeita](https://nodejs.org/en/download).


Lataussivulla on ohjeet kaikille kolmelle tärkeimmälle käyttöjärjestelmälle (OS): Windows, Linux ja MacOS. Oletuksena on, että osaat avata päätelaitteen omassa käyttöjärjestelmässäsi.


Koska NodeJS on saatavilla kaikille kolmelle käyttöjärjestelmälle, kirjoittamasi ohjelmat voidaan suorittaa niillä kaikilla (lukuun ottamatta joitakin ääritapauksia).


Tämä tarkoittaa, että voit esimerkiksi kirjoittaa yksinkertaisen videopelin JavaScriptillä Windows-tietokoneellasi ja antaa sen ystävällesi, jotta hän voi ajaa sen Mac-tietokoneellaan.


![](assets/en/2.webp)


### Tekstin muokkaus


Ohjelmoinnissa on hienoa se, että voit kirjoittaa koodia millä tahansa tekstieditorilla, jopa käyttöjärjestelmäsi oletusmuistiinpanolomakkeella.


On kuitenkin olemassa joitakin koodin kirjoittamiseen erikoistuneita tekstieditoreja, joista osa on saatavilla ilmaiseksi ja osa vaatii lisenssin maksamisen.


Koodieditorin valinta on valtava kaninkolo, joka ylittää tämän kurssin laajuuden, joten emme puhu siitä tässä. Jos et tiedä mitä käyttää, käytetyin ilmainen editori on [VSCode](https://code.visualstudio.com/).


Sen Interface on hieman paisunut, mutta siinä on kaikki, mitä tarvitset: tiedostoeditori, tiedostoetsintä (joka näyttää tiedostot ja alihakemistot siinä hakemistossa, jossa työskentelet) ja pääteohjelma koodin suorittamista varten. Se tukee myös monia liitännäisohjelmia, ja siinä on oletuksena JavaScript-syntaksin korostus.


Jos haluat olla hieman enemmän Cypherpunk-y, voit sen sijaan käyttää [VSCodium](https://vscodium.com/).


### Ensimmäinen ohjelma (hello world)


Perinteisesti ohjelmointikieltä opiskeltaessa ensimmäinen ohjelma, jonka kirjoitetaan, on "hello world!" tulostaminen konsoliin.


Luo hakemisto nimeltä `my_js_code/`, jonka sisällä on tiedosto nimeltä `main.js` (nämä nimet ovat mielivaltaisia).


Avaa hakemisto VSCodella.


Kirjoita tämä koodi tiedostoon:


```javascript
console.log("hello world!")
```


Avaa pääte ja suorita tämä komento ohjelman suorittamiseksi:


```
node main.js
```


Tuloksen pitäisi olla


```
hello world!
```


### Mitä tapahtui


JavaScriptissä kaikki on "objekteja".


`console` on olio, jota käytetään ohjelman debuggaamiseen.


`console.log` on `console`:n käytetyin menetelmä. Se vain tulostaa kaikki sille annetut argumentit.


Argumentit välitetään `console.log`-tiedostolle käyttämällä pyöreitä hakasulkeita `()`.


Jos siis esimerkiksi haluat tulostaa luvun `1000`, kirjoitat vain seuraavasti


```javascript
console.log(1000)
```


Suorita se sitten suorittamalla


```
node main.js
```


päätelaitteessa (tästä eteenpäin tällä kurssilla oletetaan, että tiedät, että näin suoritetaan ohjelma).


Tämän pitäisi tulostaa


```
1000
```


Voit siirtää useita asioita, kuten


```javascript
console.log(16, 8, 1993)
```


Tämä tulostaa


```
16 8 1993
```


## Muuttujat ja kommentit

<chapterId>23050ab7-343b-5edf-9d37-e4e782e27ce0</chapterId>


Ohjelmat suorittavat yleensä operaatioita datalla.


Muuttujat ovat kuin nimettyjä laatikoita, joita käytämme tietojen tallentamiseen. Niiden avulla voimme liittää tietoon tietyn nimen, jotta voimme hakea sen myöhemmin kyseisellä nimellä.


### `let`-ilmoitukset


Voit ilmoittaa muuttujan JavaScriptissä avainsanalla `let`.


Kirjoituksen `let` jälkeen kirjoitamme nimen, jonka haluamme antaa muuttujalle, sitten `=`-merkin ja sitten arvon, jonka haluamme tallentaa.


Esimerkiksi:


```javascript
let age = 25

console.log(age)
```


Muuttujan nimi (teknisesti "tunniste") voi yleensä sisältää kirjaimia, alleviivausmerkkejä (`_`), dollarimerkkejä (`$`) ja numeroita, vaikka ensimmäinen merkki ei voi olla numero.


Yllä olevassa koodissa ilmoitimme muuttujan nimeltä `age` ja tallennimme siihen arvon `25`.


Sitten tulostimme arvon käyttämällä `console.log(age)`.


Jos suoritat tämän koodin komennolla `node main.js`, tuloste on:


```
25
```


Tunnisteet ovat suur- ja pienaakkoset huomioon ottavia, mikä tarkoittaa, että pien- ja suuraakkoset lasketaan tunnisteiden eroksi, joten esimerkiksi seuraavassa tapauksessa


```javascript
let age = 25

let Age = 20

console.log(age)
```


tulostaa 25, koska niitä pidetään kahtena täysin erillisenä muuttujana!


Voit myös tallentaa merkkijonoja (tekstiä) muuttujaan:


```javascript
let message = "hello again"

console.log(message)
```


Tämä tulostaa:


```
hello again
```


Aivan kuten aiemmin, käytimme `console.log()` tulostaaksemme muuttujaan tallennetun arvon.


Nyt tehdään molemmat yhdessä:


```javascript
let age = 25

let message = "hello again"

console.log(age)

console.log(message)
```


Tämän suorittaminen tulostaa:


```
25
hello again
```

### Uudelleensijoitus


Muuttujia, jotka on ilmoitettu `let`-merkillä, voidaan muuttaa niiden luomisen jälkeen.


Tätä kutsutaan uudelleenkohdentamiseksi.


```javascript
let score = 10

console.log(score)

score = 15

console.log(score)
```


Määritämme ensin `10` arvoon `score` ja tulostamme sen sitten.


Sitten muutamme `score`:n arvoksi `15` ja tulostamme sen uudelleen.


Tulos on:


```
10
15
```


Tämä on erittäin hyödyllistä, kun arvo muuttuu ajan myötä, kuten pelissä, jossa pisteet kasvavat.


Lisätään vielä yksi muuttuja:


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


Tämä tulostaa:


```
10
Alice
20
Bob
```


Kuten näet, sekä `score` että `player` on muutettu.


### `const`-ilmoitukset


Useimmiten emme kuitenkaan halua muuttujan muuttuvan sen luomisen jälkeen. Siihen käytämme `const`-muuttujaa.


`const` on lyhenne sanoista "vakio". Kun olet antanut arvon `const`-muuttujalle, et voi enää muuttaa sitä.


```javascript
const pi = 3.14
console.log(pi)
```


Tämä tulostuu:


```
3.14
```


Mutta jos yrität tehdä näin:


```javascript
const pi = 3.14
console.log(pi)

pi = 99 // this line will cause an error
console.log(pi)
```


JavaScript antaa sinulle virheilmoituksen kuten:


```
TypeError: Assignment to constant variable.
```


Tämä johtuu siitä, että `pi` on ilmoitettu käyttämällä `const`, etkä voi muuttaa sen arvoa sen jälkeen. Näin ilmoitat JavaScript-tulkille, ettet halua muuttujan muuttuvan.


Tämä on hyödyllistä, koska se vähentää mahdollisuuksia muuttaa sitä vahingossa. Kun ohjelmista tulee hyvin suuria, tuhansia koodirivejä sisältäviä, on mahdotonta pysyä perässä kaikessa, mitä tapahtuu kerralla (tämä on tärkein syy siihen, että käytämme tietokoneita, jotta voimme suorittaa monimutkaisia prosesseja, joita emme pysty laskemaan aivojemme avulla), joten tällaiset rajoitukset ovat hyödyllisiä, sillä ne tekevät ohjelmasta deterministisemmän.


Parhaana käytäntönä pidetään sitä, että arvot ilmoitetaan aina `const`-arvoina, paitsi jos olemme varmoja, että haluamme muuttaa niitä myöhemmin.


### Kommentit JavaScriptissä


Joskus haluamme kirjoittaa koodiin huomautuksia, joita ei suoriteta. Näitä kutsutaan kommenteiksi.


Ohjelma ei huomioi kommentteja, kun se suoritetaan, mutta niistä on hyötyä, kun selitämme asioita itsellemme tai muille ihmisille.


Jos haluat kirjoittaa yksirivisen kommentin, käytä `//`


```javascript
// This is a comment
const x = 10 // This is also a comment
console.log(x)
```


Tämä tulostuu silti:


```
10
```


Kommentit ovat vain ihmisten luettavana.


Voit myös kirjoittaa monirivisiä kommentteja käyttämällä `/*` ja `*/`


```javascript
/*
This is a multi-line comment.
It can span several lines.
*/
const y = 20
console.log(y)
```


Tämä tulostaa


```
20
```


Ja kommentti jätetään huomiotta.


Voit käyttää kommentteja lisäämällä koodiin pieniä huomautuksia, jotta muistaisit, mitä se tekee ja miksi se on kirjoitettu tietyllä tavalla. Se voi myös auttaa muita ohjelmoijia ymmärtämään sitä.


## Perustyypit: numerot, merkkijonot, booleanit

<chapterId>cfdb04f6-21a8-5143-bbf9-7aaae04962f0</chapterId>


JavaScriptissä "tyyppi" kertoo, millaista dataa arvo on.


Javascriptissä on muutamia perustyyppejä, ja tässä osiossa tutustumme joihinkin niistä.


### Luvut ja aritmeettiset operaatiot


Ensimmäinen tyyppi, jonka esittelemme, on `luku`.


JavaScriptissä luvut voivat olla kokonaislukuja (kuten `5`) tai desimaalilukuja (kuten `3.14`).


Niillä voi tehdä aritmeettisia laskutoimituksia: yhteen-, vähennys-, kerto- ja jakolaskuja.


Tässä on yksinkertainen esimerkki:


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


Tämä tulostaa:


```
15
5
50
2
```


Voit myös käyttää sulkuja `()` ohjaamaan toimintojen järjestystä:


```javascript
const result = (2 + 3) * 4
console.log(result)
```


Tämä tulostuu:


```
20
```


Ilman sulkuja se olisi `2 + 3 * 4`, joka on:


```javascript
const result = 2 + 3 * 4
console.log(result)
```


Se tulostuisi:


```
14
```


Koska tavallisessa matematiikassa kertolasku tapahtuu ennen yhteenlaskua.


### Merkkijonot ja interpolointi


Toinen JavaScript-tyyppi, jonka esittelemme, on `string`.


Merkkijonot ovat tekstikappaleita. Voit käyttää yksinkertaisia lainausmerkkejä `"...'` tai kaksinkertaisia lainausmerkkejä `"..."` niiden luomiseen.


```javascript
const greeting = "hello"
const name = 'Bob'
console.log(greeting)
console.log(name)
```


Tämä tulostuu:


```
hello
Bob
```


Voit yhdistää merkkijonoja käyttämällä `+`-operaattoria:


```javascript
const greeting = "hello"
const space = " "
const name = "Bob"

const fullGreeting = greeting + space + name
console.log(fullGreeting)
```


Tämä tulostaa:


```
hello Bob
```


Mutta on olemassa mukavampi tapa yhdistää merkkijonoja, jota kutsutaan **merkkijonojen interpoloinniksi**. Käytä takaviivoja merkkijonon `` `...`` julistamiseen ja kirjoita muuttujat käyttämällä `${...}` merkkijonon sisään:


```javascript
const greeting = "hello"
const name = "Bob"

const fullGreeting = `${greeting} ${name}`
console.log(fullGreeting)
```


Tämä tulostuu myös:


```
hello Bob
```


Voit sisällyttää minkä tahansa lausekkeen `${...}` sisään:


```javascript
const age = 30
console.log(`Next year, I will be ${age + 1} years old.`)
```


Tämä tulostuu:


```
Next year, I will be 31 years old.
```


Interpolointi on hyvin yleistä nykyaikaisessa JavaScriptissä.


### Boolet, vertailu ja logiikkaoperaatiot


Kolmas tyyppi, jonka esittelemme, on `boolean`. Se on nimetty matemaatikko George Boolen mukaan, joka keksi Boolen logiikan.


Boolet ovat yksinkertaisia: vain kaksi mahdollista arvoa, `true` ja `false`.


Voit tallentaa ne muuttujiin:


```javascript
const theSkyIsBlue = true
const thisCourseIsBad = false

console.log(theSkyIsBlue)
console.log(thisCourseIsBad)
```


Tämä tulostuu:


```
true
false
```


Voit yhdistää loogisia lausekkeita loogisilla operaattoreilla:



- `&&` tarkoittaa "ja", ja se palauttaa `true` vain jos **kumpikin** arvo on `true`, muuten se palauttaa `false`
- `||` tarkoittaa "tai", ja se palauttaa `true`, jos **vähintään toinen** arvoista on `true`, muuten (jos molemmat ovat false) se palauttaa `false`
- `!` tarkoittaa "ei", sitä käytetään ennen booleania ja se kääntää sen: jos boolean on `true`, se palauttaa `false`, ja päinvastoin.


![](assets/en/3.webp)


Esimerkkejä:


```javascript
const isSunny = true
const isWarm = true

console.log(isSunny && isWarm)  // true
console.log(isSunny || isWarm)  // true
console.log(!isSunny)           // false
```


Voit verrata arvoja JavaScriptissä käyttämällä operaattoreita kuten `>`, `<`, `===` ja `!==`. Näiden vertailujen tulos on aina boolean.


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


Javascriptissä on myös `>=` tarkoittaakseen "suurempi tai yhtä suuri" ja `<=` tarkoittaakseen "pienempi tai yhtä suuri".


Boolet, vertailu- ja loogiset operaattorit yhdistetään usein ohjelmissa monimutkaisten ehtojen ilmoittamiseen, kuten sen varmistamiseen, että "sähköposti on saapunut JA se sisältää tarvitsemani kuvan TAI sähköpostin pituus on yli 10000 merkkiä". Myöhemmin huomaat, että nämä ovat olennaisia rakennuspalikoita ohjelman logiikan rakentamisessa.


## Arrays, null, undefined

<chapterId>7bf18183-5eae-53ed-83d2-b04982145d81</chapterId>


Tässä osassa käsittelemme kolme muuta tyyppiä, jotka ovat hyvin yleisiä JavaScript-ohjelmissa:



- Array**: arvojen sarjat
- undefined**: erityisarvo, joka tarkoittaa, että "mitään ei ole annettu"
- null**: toinen erityisarvo, joka tarkoittaa "tarkoituksellisesti tyhjä"


### Asettelut ja indeksin käyttö


**Moniste** on tyyppi, joka voi sisältää useita arvoja luettelona.


Luodaan joukko käyttämällä hakasulkeita `[]` ja erottamalla kohteet toisistaan pilkuilla.


Tässä on yksinkertainen esimerkki:


```javascript
const numbers = [10, 2, 88]
console.log(numbers)
```


Tämä tulostuu:


```
[ 10, 2, 88 ]
```


Joukkoon voi tallentaa mitä tahansa, ei vain numeroita:


```javascript
const things = ["apple", 42, true]
console.log(things)
```


Tämä tulostuu:


```
[ 'apple', 42, true ]
```


Käyttääksemme tiettyä joukkoon sisältyvää kohdetta, käytämme **indeksiä**. Indeksi on kohteen sijainti alkaen **0**.


Joten tässä sarjassa:


```javascript
const colors = ["red", "green", "blue"]
```



- `colors[0]` on `"punainen"`
- `värit[1]` on `"Green"`
- `colors[2]` on `"sininen"`


Kokeillaan:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[0])
console.log(colors[1])
console.log(colors[2])
```


Tämä tulostaa:


```
red
green
blue
```


Voit määrittää arvon tietylle matriisin indeksille


```javascript
const colors = ["red", "green", "blue"]

colors[1] = "yellow"

console.log(colors)
```


Tämä tulostaa:


```
[ 'red', 'yellow', 'blue' ]
```


Voit käyttää mitä tahansa luonnollista lukua indeksinä, jopa muuttujaan tallennettua lukua


```javascript

const i = 1
const colors = ["red", "green", "blue"]
console.log(colors[i])
```


Tämä tulostaa:


```
green
```


Mutta jos yrität käyttää indeksiä, jota ei ole olemassa, saat tuloksen `undefined`:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[3])
```


Tämä tulostuu:


```
undefined
```


Mikä tuo on?


### `undefined`


Erityisarvo `undefined` tarkoittaa, että "arvoa ei ole annettu".


Jos luot muuttujan, mutta et anna sille arvoa, se on `undefined`:


```javascript
const name
console.log(name)
```


Tämä tulostuu:


```
undefined
```


Koska emme ole antaneet mitään arvoa `name`:lle, JavaScript asettaa sen oletusarvoisesti arvoksi `undefined`.


Kuten aiemmin on nähty, voit myös saada tuloksen `undefined`, kun käytät matriisi-indeksiä, jota ei ole olemassa:


```javascript
const fruits = ["banana", "apple"]
console.log(fruits[2]) // There is no index 2
```


Tämä tulostuu:


```
undefined
```


### `null` ja sen käsittely


`null` on myös erikoisarvo. Se tarkoittaa "tässä ei ole mitään, ja tein sen tarkoituksella"


Toisin kuin `undefined`, joka on automaattinen, `null` on jotain, jonka asetat itse.


Esimerkiksi:


```javascript
const currentUser = null
console.log(currentUser)
```


Tämä tulostuu:


```
null
```


Miksi käyttää `null`? Ehkä odotat arvoa myöhemmin, mutta se ei ole vielä valmis:


```javascript
let winner = null

// Later in the program:
winner = "Alice"

console.log(winner)
```


Tämä tulostuu:


```
Alice
```


Joten `null` on hyödyllinen, kun haluat esimerkiksi sanoa: "Tässä pitäisi olla jotain myöhemmin, mutta juuri nyt se on tyhjä."


## Lohkot ja ohjausvirta

<chapterId>be985168-2636-5b0d-a48f-ac1bbfbff8a7</chapterId>


Tähän mennessä olemme kirjoittaneet lähinnä koodirivejä, jotka suoritetaan peräkkäin.


Mutta kun koodaamme, voimme hallita sen suoritusjärjestystä.


Tätä kutsutaan **ohjausvirraksi**.


Aloitetaan lohkojen ja laajuuden ymmärtämisestä.


### Maailmanlaajuinen soveltamisala


Jokainen ilmoittamamme muuttuja on olemassa **scope**:ssa, joka tarkoittaa koodin aluetta, jossa muuttuja tunnetaan.


Jos ilmoitat muuttujan minkään lohkon ulkopuolella, se on olemassa **globaalialueella**.


```javascript
const color = "blue"
console.log(color)
```


Tämä muuttuja `color` on globaalissa laajuudessa, joten sitä voidaan käyttää mistä tahansa tiedostosta.


Jos lisäät lisää rivejä:


```javascript
const color = "blue"
console.log(color)

const size = "large"
console.log(color)
console.log(size)
```


Sekä `color` että `size` ovat globaaleja muuttujia. Ne ovat käytettävissä kaikkialla tiedostossa.


Mutta mitä tapahtuu lohkon sisällä?


### Lohkot ja paikallinen laajuus


**Lohko** on koodinpätkä, jota ympäröivät suljetut aaltosulkeet `{}`.


Lohkon sisällä `let`- tai `const`-merkinnällä ilmoitetut muuttujat ovat olemassa **vain** kyseisen lohkon sisällä.


```javascript
{
const message = "inside block"
console.log(message)
}
```


Tämä tulostuu:


```
inside block
```


Mutta jos kokeilet tätä:


```javascript
{
const message = "inside block"
}
console.log(message) // Error!
```


JavaScript antaa sinulle virheilmoituksen kuten:


```
ReferenceError: message is not defined
```


Tämä johtuu siitä, että `message` on ilmoitettu lohkon sisällä eikä sitä ole olemassa lohkon ulkopuolella.


Tämä tarkoittaa, että voimme käyttää lohkoja eristämään koodin osia ja olla varmoja siitä, että "mitä lohkossa tapahtuu, pysyy lohkossa" (vähän kuin Las Vegasissa).


Järjestämällä koodimme lohkoihin voimme myös jäsentää ohjelman suoritusta, kun käytämme kontrollivirran rakenteita, kuten `if`


### `if`, `else`


Joskus haluamme ajaa koodia **vain** jos** jokin on totta. Sitä varten on olemassa `if`-lauseke.


```javascript
const myAge = 20

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Tämä tulostuu:


```
Am I an adult?
Yes I am!
```


Kuten näet, koodi vertaa `myAge` ja `18`.

Tässä tapauksessa `>=`-operaattori palauttaa `true`, joten lohko suoritetaan.

Jos ehto ei ole `true`, lohkoa ei suoriteta.


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Tämä tulostuu:


```
Am I an adult?
```


Voit lisätä `else`-lohkon käsittelemään päinvastaista tapausta:


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
} else {
console.log("No, I am not.")
}
```


Tämä tulostuu:


```
Am I an adult?
No, I am not.
```


Sekä `if`- että `else`-lohkot ovat edelleen lohkoja - joten niiden sisällä ilmoitetut muuttujat eivät ole olemassa niiden ulkopuolella.


Jos haluamme olla varmoja siitä, että jokin on **ei** totta, mitä voimme tehdä?


Kuten aiemmin on todettu, JavaScriptissä on "not"-operaattori, joka kääntää boolen. Voimme siis tehdä


```javascript
const myAge = 17

const adult = myAge >= 18

console.log("Am I an adult?")

if (!adult) {
console.log("No, I am not.")
}
```

Tämä tulostuu edelleen:


```
Am I an adult?
No, I am not.
```

Koska käytimme `!`-operaattoria muuttujan `aikuinen` kääntämiseen.


`if (!adult) {...}` pitäisi lukea "if not adult..."


Lohkojen, logiikan ja vertailuoperaattoreiden avulla voimme jäsentää ohjelman suoritusta määrittelemällä muuttujia, joiden on oltava `tosi` (tai `väärin`), jotta jotain tapahtuisi.


### `while`, `break`, `continue`, `while`, `break`, `continue`, `continue`, `continue`


While-silmukka toistaa koodia *sekä niin kauan* kuin jokin ehto on tosi.


```javascript
let count = 0

while (count < 3) {
console.log("Count is", count)
count = count + 1
}
console.log("the loop is over!")
```


Tämä tulostuu:


```
Count is 0
Count is 1
Count is 2
the loop is over!
```


Kun `count` on 3, silmukka pysähtyy.


Voit pysäyttää silmukan aikaisin käyttämällä `break`:


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


Tämä tulostuu:


```
0
1
2
```


Koska kun luvusta tulee `3`, `if`-lohko suoritetaan ja se pysäyttää silmukan.


Voit ohittaa silmukan loppuosan käyttämällä `continue`:


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


Tämä tulostuu:


```
1
2
4
5
```


Koska kun luku oli `3`, `continue` sai ohjelman ohittamaan rivin, joka tulostaa luvun.


### "... varten ... of ..


Jos sinulla on joukko ja haluat tehdä jotain sen jokaiselle kohteelle, voit käyttää `for ... of ... of ... {...}`.


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const fruit of fruits) {
console.log(fruit)
}
```


Tämä tulostuu:


```
apple
banana
cherry
```

Lohko suoritetaan kerran jokaista matriisin elementtiä kohden.


`fruit` on tässä uusi muuttuja, joka ottaa kunkin rivin kohteen arvon, jotta sillä voidaan toimia lohkon sisällä.


### `for ... in ...`


Voit käyttää komentoa `for ... in` kiertääksesi joukon avaimia (indeksejä):


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(index)
}
```


Tämä tulostuu:


```
0
1
2
```


Voit käyttää indeksiä myös arvon saamiseksi:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(fruits[index])
}
```


Tämä tulostaa saman kuin `for ... of`:


```
apple
banana
cherry
```


Käytännössä, kun kyseessä on joukko, kannattaa käyttää mieluummin `for ... of`, koska se on yksinkertaisempi ja siistimpi.


### Rajoitetut silmukat


Joskus haluamme tehdä silmukan tietyn määrän kertoja tai yleensä kirjoittaa koodin, joka toistaa lohkoa ja pitää samalla kirjaa jostakin asiasta.

Sitä varten on hyvä käyttää rajoitettua for-silmukkaa.

Rajoitettu silmukka sisältää yleensä kolme ehtoa, jotka erotetaan toisistaan puolipisteellä `;`, kuten esimerkiksi `(... ; ... ; ....)`.


```javascript
for (let i = 0; i < 3; i = i + 1) {
console.log(i)
}
```


Tämä tulostuu:


```
0
1
2
```


Selitetäänpä se:



- `let i = 0`: ilmoittaa muuttujan, jota käytetään lohkossa (tässä tapauksessa se on laskuri, joka alkaa 0:sta)
- `i < 3`: ilmoittaa ehdon, jonka on oltava `tosi`, jotta lohko voidaan suorittaa ( tässä tapauksessa "toista kun `i` on pienempi kuin 3")
- `i = i + 1`: ilmoitetaan jokin koodi, joka suoritetaan jokaisen lohkon suorituksen jälkeen (tässä tapauksessa "lisää `i` 1:llä")


Kuten näet, rajoitettu silmukka antaa meille mahdollisuuden ilmoittaa monimutkaisempia ehtoja koodin toistuvalle suorittamiselle, mutta useimmiten se ei ole välttämätöntä.


### Lohkon tarrat


Jos joudut kirjoittamaan monimutkaisemman ohjausvirran, JavaScript antaa sinun nimetä lohkon **labelilla**, jota voidaan käyttää `break`- tai `continue`-merkinnöissä, kun halutaan määritellä *mihin* hypätään takaisin.


Esimerkki:


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


Tämä tulostuu:


```
Inside outer block
Inside inner block
Done
```


Käytimme `break outer` -merkkiä poistuaksemme kokonaan `outer`-lohkosta.


Voit myös merkitä silmukoita. Otetaan tämä esimerkki:


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

Tämä oli hyvin tylsä esimerkki, mutta toivottavasti se selvensi (satunnaista) tarrojen tarvetta.


## Toimintojen esittely

<chapterId>cc324715-09c2-5cf7-9e6f-47a6f16bc04d</chapterId>


Kun ohjelmasi kasvavat, haluat usein **kierrättää** koodin osia.


Sitä varten **funktiot** ovat olemassa: niiden avulla voit ryhmitellä koodia, antaa sille nimen ja suorittaa sen milloin haluat.


### Toimintoilmoitus


Voimme ilmoittaa funktion käyttämällä avainsanaa `function`. Sen jälkeen annamme sille nimen, sulkeissa `()` annetaan argumentit, jotka se ottaa vastaan, ja suoritettava koodilohko `{}`. Aloitetaan funktiolla, joka ei ota argumentteja:


```javascript
function sayHello () {console.log(`Hello!`) }
```


Tämä koodi **ilmoittaa** funktion, mutta **ei** suorita sitä vielä.


### Toimintokutsut


Kun haluat suorittaa (tai "kutsua") funktion, kirjoitat sen nimen ja sen jälkeen sulut:


```javascript
function sayHello () {console.log(`Hello!`) }
sayHello()
```


Tämä tulostuu:


```
Hello!
```


Voit kutsua funktiota niin monta kertaa kuin haluat:


```javascript
function sayHello() {
console.log("Hello!")
}

sayHello()
sayHello()
```


Tämä tulostuu:


```
Hello!
Hello!
```


Funktiossa oleva koodi suoritetaan vain, kun kutsut sitä.


### Funktion argumentit (funktioiden syötteet)


Joskus haluat, että funktio toimii jollakin syötteellä. Voit tehdä sen lisäämällä **argumentit** sulkujen sisään.


Esimerkiksi:


```javascript
function sayHelloTo (friend) {
console.log(`Hello ${friend}!`)
}
```


Nyt tämä funktio ottaa **yksi argumentin** nimeltä `friend`.


Kun kutsut funktiota, voit antaa arvon:


```javascript
sayHelloTo("Tommy")
```


Tämä tulostuu:


```
Hello Tommy!
```


Voit kutsua funktiota uudelleen eri nimellä:


```javascript
sayHelloTo("Sam")
```


Tämä tulostuu:


```
Hello Sam!
```


Syöttämäsi arvo korvaa `friend`-muuttujan funktion sisällä.


Voit myös käyttää useampaa kuin yhtä argumenttia:


```javascript
function greetTwoPeople(person1, person2) {
console.log(`Hello ${person1} and ${person2}!`)
}

greetTwoPeople("Lina", "Marco")
```


Tämä tulostuu:


```
Hello Lina and Marco!
```


### `return` (funktioiden tuotos)


Funktiot voivat myös **palauttaa** arvoja. Tämä tarkoittaa, että ne lähettävät arvon takaisin sinne, missä funktiota kutsuttiin.


Tässä on yksinkertainen esimerkki:


```javascript
function getNumber() {
return 42
}

const result = getNumber()
console.log(result)
```


Tämä tulostuu:


```
42
```


Funktio `getNumber()` palauttaa arvon `42`, ja tallennamme sen `result` -kenttään ja tulostamme sen sitten.


Voit myös palauttaa jotain laskemaasi:


```javascript
function add(a, b) {
return a + b
}

const result = add(2, 3)
console.log(result)
```


Tämä tulostuu:


```
5
```


Kun arvo on `palautettu`, funktio pysähtyy. Mitään `return`:n jälkeistä ei tapahdu kyseisessä lohkossa.


```javascript
function saySomething() {

return "hi"

console.log("this never runs")

}

const message = saySomething()
console.log(message)
```


Tämä tulostaa vain:


```
hi
```


koska vain `"hi"` palautetaan. Rivi `console.log("this never runs")` jätetään väliin.


Voit ajatella funktioita pieninä aliohjelmina. Kukin funktio voi ottaa syötteen, käsitellä sitä ja antaa tulosteen.


Mitä tapahtuu, jos yritämme käyttää funktion paluuarvoa, mutta funktio ei ole palauttanut mitään?


```javascript
function doesNothing () {}

const x = doesNothing()

console.log(x)
```

Tämä tulostaa `undefined`. Sellaisen funktion paluuarvo, joka ei ole palauttanut mitään, on `undefined`.


## Esineet ja luokat

<chapterId>26689f25-8212-5057-8c21-3a05eee0ac75</chapterId>


JavaScriptiä kutsutaan usein oliopohjaiseksi kieleksi.


Tämä tarkoittaa, että se auttaa sinua järjestämään koodisi ryhmittelemällä arvot ja funktiot yhteen **objekteiksi**.


### Mikä on "objekti"?


Objekti voi sisältää dataa ja funktioita, jotka toimivat kyseisellä datalla. Kun funktio sijoitetaan objektiin, sanomme, että se on `metodi`.


Ensimmäinen näkemämme objekti oli `console`-objekti. Se on objekti, joka sisältää useita metodeja, joiden avulla voimme tulostaa asioita näytölle ja debugata ohjelmiamme.


Se voi jopa tulostaa itsensä; voit tehdä


```javascript
console.log(console)
```


ja se tulostaa luettelon sen sisältämistä metodeista. Esimerkiksi minun koneellani se tulosti


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


Kuten näet, sillä on paljon menetelmiä, joita voit käyttää debuggaamiseen!


Javascript tarjoaa meille erilaisia tapoja luoda uusia objekteja, jotka voivat tehdä mitä haluamme niiden tekevän.


### Objektin luominen


Helpoin tapa luoda objekti on vain ryhmitellä tietoja ja funktioita käyttämällä **juovia sulkeita** `{}`.


Tämä luo niin sanotun **anonyymin objektin**


```javascript
const cat = {
name: "Whiskers",
age: 3
}
```


Tämä luo objektin ja tallentaa sen muuttujaan nimeltä `cat`.


Objektilla on kaksi **ominaisuutta**:



- `name`, jonka arvo on `"Whiskers"`
- `age` arvolla `3`


Tulostetaan se:


```javascript
console.log(cat)
```


Tämä tulostuu:


```
{ name: 'Whiskers', age: 3 }
```


Voit hakea objektin ominaisuudet käyttämällä pistettä, kuten `objectName.propertyName`:


```javascript
console.log(cat.name)  // prints "Whiskers"
console.log(cat.age)   // prints 3
```


Voit myös **vaihtaa** ominaisuuden:


```javascript
cat.age = 4
console.log(cat.age)  // now it prints 4
```


Kuten näet, vaikka objekti olisi määritelty `const`, voit silti muuttaa sen sisältämää dataa.


Objektien tapauksessa `const` estää sinua vain ohittamasta koko objektia:


```javascript
const cat = {
name: "Whiskers",
age: 3
}

cat.age = 5 // this works

cat = 5 // this throws an error, you're trying to reassign the whole object

```


Kuten aiemmin mainittiin, oliot voivat sisältää myös **funktioita**, ja kun funktio on osa oliota, kutsumme sitä **metodiksi**.


Tässä on esimerkki:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log("Meow!")
}
}
```


Tällä esineellä on:



- Ominaisuus `name`
- Menetelmä `speak()`


Kutsutaan menetelmää:


```javascript
cat.speak()
```


Se tulostuu:


```
Meow!
```


Metodit voivat käyttää objektin sisältämiä tietoja avainsanan `this` avulla.

`this` viittaa nykyiseen objektiin. Tässä esimerkissä sitä käytetään tulostamaan kissan nimi:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log(`${this.name} says meow!`)
}
}

cat.speak()
```


Tämä tulostuu:


```
Whiskers says meow!
```


Sana `this` tarkoittaa "tätä kohdetta"... tässä tapauksessa `cat`-objektia.



Tällaiset esineet ovat hyviä, kun haluat vain jotain nopeaa ja yksinkertaista. Mutta jos sinun täytyy luoda **monia objekteja**, joilla on sama rakenne, on olemassa parempi tapa, ja siinä **luokat** tulevat kuvaan.


### Luokat ja konstruktorit


**Luokka** on kuin suunnitelma. Se kertoo JavaScriptille, miten tietynlainen objekti luodaan.


Luokka määritellään avainsanalla `class`, jota seuraa luokan nimi ja suljetut sulut `{}`.


```javascript
class Dog {}
```


Luokat alkavat tavallisesti isolla kirjaimella.


Voit luoda uuden luokan objektin käyttämällä `new`:


```javascript
const hachiko = new Dog()
```


Yritä tulostaa kohde:

```javascript
class Dog {}

const myDog = new Dog()

console.log(myDog)
```


Saat


```
Dog {}
```


Kuten näet, Dog-luokka on tyhjä, joten myös `myDog`-olio on tyhjä.


Voimme määritellä, mitä ominaisuuksia koiraobjektien tulisi sisältää lisäämällä `konstructor`.


Konstruktori on erityinen funktio, joka suoritetaan, kun luot (tai "rakennat") uuden objektin.


```javascript
class Dog {
constructor() { }
}
```


Haluamme, että jokaisella koiralla on nimi, joten lisäämme funktioon parametrin `nimi`:


```javascript
class Dog {
constructor(name) { }
}
```


Ja sitten käytämme `this`:ä ilmoittaaksemme, että `name` on `Dog`-olion `nimi`, jota olemme rakentamassa


```javascript
class Dog {
constructor(name) {
this.name = name
}}
```


Yritetään käyttää sitä nyt:


```javascript
class Dog {
constructor(name) {
this.name = name
}
}

const myDog = new Dog("hachiko")

console.log(myDog)
```


Tämä tulostaa jotakin seuraavanlaista:


```
Dog { name: 'hachiko' }
```


Kuten näet, `constructor`-metodi ottaa luokalle annetut argumentit, kun teet `new Dog()`, ja käyttää niitä objektin rakentamiseen.


Kerrotaanpa tarkemmin:



- `class Dog` määrittelee Dog-luokan.
- `constructor(name)` määrittää objektin, kun se luodaan.
- `this.name = name` tallentaa arvon uuteen objektiin.
- `new Dog("hachiko")` luo uuden objektin luokasta, jonka `name`-ominaisuudeksi on asetettu `"hachiko"`.


Lisätään nyt metodi luokkaamme:


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


Tämä tulostaa


```javascript
hachiko says barf!
```


Jos teemme saman kahdelle eri Dogin tapaukselle



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


saadaan


```
hachiko says barf!
bobby says barf!
```


metodi `speak()` käyttää sen koiran `name`-ominaisuutta, jota kutsutaan.


Tämä on tärkein syy luokkien olemassaoloon: niiden avulla voimme määritellä joukon metodeja, jotka toimivat datan kanssa, ja luoda useita objekteja, joilla on sama datan "muoto".


Kun kutsumme metodia johonkin näistä objekteista, se toimii *tämän tietyn objektin* hallussa oleviin tietoihin.


### Esineen muodon muuttaminen


JavaScriptin objektit ovat joustavia. Vaikka olet luonut objektin, voit yhä lisätä uusia ominaisuuksia tai poistaa olemassa olevia.


Se on sallittua, mutta sitä kannattaa käyttää varovasti.


Aloitetaan yksinkertaisesta `Dog`-luokasta:


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


Tässä vaiheessa `myDogilla` on vain yksi ominaisuus: `name`. Voimme silti lisätä uusia ominaisuuksia sen luomisen jälkeen:


```javascript
myDog.age = 5

console.log(myDog.age) // prints 5
```


Voimme myös lisätä uuden menetelmän:


```javascript
myDog.jump = function () {
console.log(`${this.name} jumps!`)
}

myDog.jump() // Fido jumps!
```


Voimme myös poistaa ominaisuuksia käyttämällä `delete`-avainsanaa.


```javascript
delete myDog.name

console.log(myDog.name) // prints 'undefined'
```


Tämä toimii, mutta on tärkeää tietää eräs asia: JavaScript-moottorit, kuten V8 (jota käytetään Node.js:ssä ja Chrome-selaimessa), toimivat nopeammin, kun objekteilla on aina samat ominaisuudet. Jos lisäät tai poistat ominaisuuksia objektin luomisen jälkeen, se voi hidastaa toimintaa.


Pienissä ohjelmissa tällä ei ole suurta merkitystä. Mutta isommissa projekteissa (kuten peleissä) on parempi luetella kaikki ominaisuudet konstruktorissa alusta alkaen, vaikka et käyttäisikään niitä heti. Tämä pitää objektin muodon vakaana ja auttaa koodia toimimaan nopeammin.


Esimerkiksi tämän sijasta:


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


Voisit tehdä


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


Molemmat versiot toimivat, mutta jälkimmäinen on suorituskyvyn kannalta parempi. Kerrot moottorille etukäteen, mitä ominaisuuksia kullakin objektilla on, ja se voi optimoida sen mukaan.


JavaScriptin avulla voit muokata objekteja vapaasti, mutta luokkia käytettäessä on parasta suunnitella objektin muoto etukäteen.



### Perinnöllisyys `extends`- ja `super()`-ominaisuuksilla


Joskus haluat luoda luokan, joka on *lähes* sama kuin toinen luokka, mutta jolla on muutama lisäominaisuus.


Sen sijaan, että muuttaisit objektien muotoa (mikä, kuten edellä mainittiin, ei ole optimaalista suorituskyvyn kannalta) tai kirjoittaisit uuden luokan tyhjästä, JavaScript antaa sinulle mahdollisuuden käyttää jotain, jota kutsutaan **perinnöksi**.


Perinnöllisyys tarkoittaa, että yksi luokka voi **laajentaa** toista. Uusi luokka saa kaikki vanhan luokan ominaisuudet ja metodit, ja voit lisätä niitä lisää tai muuttaa niitä, joita tarvitset.


Oletetaan, että meillä on perusluokka nimeltä `Vehicle`:


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


Nyt haluamme tehdä luokan `Auto`. Auto on eräänlainen kulkuneuvo, mutta saatamme haluta, että sillä on joitakin lisäominaisuuksia tai että se antaa erilaisen viestin, kun se käynnistyy. Sen sijaan, että kirjoittaisimme kaiken uudelleen, voimme käyttää `extends`-luokkaa:


```javascript
class Car extends Vehicle {
start() {
console.log(`${this.brand} car is ready to drive!`)
}
}
```


Luokka `Auto` perii nyt kaiken luokasta `Ajoneuvo`. Se saa `brand`-ominaisuuden, ja olemme korvanneet `start()`-metodin omalla versiollamme.


![](assets/en/4.webp)


Kokeillaan sitä:


```javascript
const myCar = new Car("Toyota")
myCar.start()
```


Tämä tulostuu:


```
Toyota car is ready to drive!
```


Vaikka `Autolla` ei ole omaa konstruktoria, se käyttää silti `Ajoneuvon` konstruktoria. Mutta jos haluamme kirjoittaa `Autoon` oman konstruktorin, voimme tehdä sen, meidän täytyy vain sisällyttää kutsu sen vanhemman konstruktoriin käyttämällä `super()`.


Näin:


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



Tämä tulostuu:


```
Toyota Corolla is ready to drive!
```


Yhteenvetona



- `extends` tarkoittaa, että yksi luokka perustuu toiseen.
- `super()` käytetään kutsumaan laajennettavan luokan konstruktoria.
- Uusi luokka saa kaikki alkuperäisen luokan ominaisuudet ja metodit.
- Voit **korjata** metodeja (kuten `start()`) saadaksesi ne tekemään jotain muuta.


Tämä on hyödyllistä, kun sinulla on useita samankaltaisia asioita (kuten autoja, kuorma-autoja ja polkupyöriä) ja haluat, että ne käyttävät samaa koodia, mutta käyttäytyvät silti omalla tavallaan.


### `instanceof`


Avainsana `instanceof` tarkistaa, onko objekti luotu tietystä luokasta.


Oletetaan, että meillä on luokka nimeltä `User`:


```javascript
class User {
constructor(username) {
this.username = username
}
}

const regularUser = new User("julia123")

console.log(regularUser instanceof User)
```


Tämä tulostuu:


```
true
```


Vahvistetaan, että `regularUser` on `User`. Tämä johtuu siitä, että `regularUser` luotiin `User`-luokalla.


Se toimii myös **perittyjen** luokkien kanssa. Esimerkiksi tässä on `Admin`-luokka, joka on `User`-luokan jatkaja:


```javascript
class Admin extends User {}

const ourAdmin = new Admin("admin42")

console.log(ourAdmin instanceof Admin)   // true
console.log(ourAdmin instanceof User)    // true
```


Molemmat rivit palauttavat `true`. Tämä johtuu siitä, että `Admin` on `User`:n aliluokka, joten `MeidänAdmin` on sekä `Admin` että `User`


# Keskitason JavaScript

<partId>243f63ab-4f34-5c30-80cb-84ef46f6761d</partId>


## Virheiden käsittely

<chapterId>d0206bc5-d386-5e7f-9917-5803f392448c</chapterId>


Kun kirjoitat monimutkaisempia JavaScript-ohjelmia, kohtaat **virheitä**. Ne ovat odottamattomia tilanteita, joissa jokin menee pieleen. Ehkä muuttuja on `undefined`, mutta yrität käyttää sitä, tai jokin koodi saa väärän tyyppisen syötteen.


Jos emme käsittele näitä virheitä oikein, ohjelmamme saattaa kaatua tai käyttäytyä arvaamattomalla tavalla. JavaScript tarjoaa työkaluja näiden virheiden havaitsemiseen ja hallitsemiseen, jotta voimme käsitellä niitä tyylikkäämmin.


### Yleinen virhe: arvon käyttäminen `undefined`-arvossa


Tässä on yleinen tilanne, joka aiheuttaa virheen:


```javascript
const user = undefined
console.log(user.name)
```


Jos suoritat tämän koodin, saat seuraavanlaisen virheilmoituksen:


```
TypeError: Cannot read properties of undefined (reading 'name')
```


Se on JavaScript, joka kertoo sinulle: "Hei, yritit hakea `name`-ominaisuutta jostain, joka on `undefined`, eikä siinä ole järkeä." Ja kuten näet, kun tällainen virhe tapahtuu, ohjelma pysähtyy, ellet ole kirjoittanut koodia, joka ottaa sen kiinni ja käsittelee sen.


### virheen heittäminen


Joskus haluat manuaalisesti **nostaa virheen** koodissasi. Tällöin käytetään `throw`-avainsanaa.


```javascript
throw new Error("This is a custom error message")
```


Tämä pysäyttää ohjelman välittömästi ja tulostaa:


```
Uncaught Error: This is a custom error message
```


Voit käyttää `throw`:ta sääntöjen noudattamiseen ohjelmassasi. Esimerkiksi:


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


Toinen kutsu aiheuttaa virheen, koska jakaminen nollalla ei ole tässä esimerkissä sallittua.


### Virheiden sieppaaminen `try...catch` -menetelmällä


Jos et halua ohjelmasi kaatuvan virheen sattuessa, voit ottaa virheen kiinni käyttämällä `try...catch`-lohkoa. Tämä on hyödyllistä silloin, kun haluat ohjelmasi **jatkavan**, vaikka jokin epäonnistuu.


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log("Oops! Something went wrong.")
}
```


Lähtö:


```
Oops! Something went wrong.
```


Näin se toimii:



- `try`-lohkon sisällä olevaa koodia yritetään käyttää ensin.
- Jos virhe tapahtuu, JavaScript **hyppää `catch`-lohkoon** ohittaen loput `try`-lohkosta.
- `catch`-lohko vastaanottaa virheen, joten voit tulostaa sen tai käsitellä sitä jollakin muulla tavalla, kuten esimerkiksi seuraavasti


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log(`The message of the error was: "${error.message}"`)
}
```


Lähtö:


```
The message of the error was: "Cannot read properties of undefined (reading 'name')"
```


### Lohko `finally`


Voit myös lisätä `finally`-lohkon. Tämä on koodia, joka **ajetaan** aina, riippumatta siitä, onko virhe tapahtunut vai ei.


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


Lähtö:


```
Trying something risky...
Caught the error: Uh oh!
This will run no matter what.
```


## Vikojen välttäminen

<chapterId>db12d9f6-5806-514c-998e-0ae24805104e</chapterId>


Tässä luvussa esitellään joitakin JavaScriptin yleisimpiä sudenkuoppia ja kerrotaan, miten niitä voi välttää.


### `var` ja Assignment ilman ilmoitusta


Vanhemmassa JavaScript-koodissa muuttujat ilmoitettiin usein avainsanalla `var`. Toisin kuin `let` ja `const`, joista olet jo oppinut, `var` voi käyttäytyä hämmentävällä tavalla.


Esimerkiksi:


```javascript
{
var message = "hello"
}
console.log(message)
```


Voisi olettaa, että `message` on olemassa vain lohkon sisällä, mutta näin ei ole. `var` ei huomioi lohkon laajuutta, ja se tekee muuttujasta käytettävissä olevan koko funktion tai tiedoston sisällä.


Tämä voi johtaa odottamattomaan käyttäytymiseen erityisesti suuremmissa ohjelmissa. Tästä syystä nykyaikaisessa JavaScript-koodissa tulisi aina käyttää `let` tai `const` `var`:n sijasta.


Vielä pahempaa on se, että JavaScriptissä voit antaa muuttujille arvoja **ilmoittamatta niitä lainkaan**:


```javascript
function greet() {
user = "Alice"
}
greet()
console.log(user) // prints "Alice"
```


Tämä luo uuden globaalin muuttujan `nimi` ilman mitään ilmoitusta. Tämä voi tapahtua äänettömästi ja johtaa virheisiin, joita on Hard jäljittää, varsinkin jos kyseessä on vain kirjoitusvirhe. Ilmoita muuttujat aina käyttämällä `let` tai `const`.


### Heikko tyyppijärjestelmä


JavaScript on heikosti tyypitetty, eli se muuntaa arvot tarvittaessa automaattisesti tyypistä toiseen. Tätä kutsutaan tyypin pakottamiseksi, ja vaikka se voi olla kätevää, se johtaa usein hämmentäviin tuloksiin.


Esimerkiksi:


```javascript
console.log("5" + 1)    // "51"
console.log("5" - 1)    // 4
console.log(true + 1)   // 2
console.log(null + 1)   // 1
```


Näissä esimerkeissä JavaScript yrittää arvata, mitä tarkoitit. Joskus se muuttaa merkkijonot numeroiksi, booleanit numeroiksi tai merkkijonot merkkijonoiksi. Tämä voi saada koodisi käyttäytymään odottamattomalla tavalla.


On tärkeää olla tietoinen JavaScriptin heikosta tyypitysjärjestelmästä. Kun asiat alkavat käyttäytyä oudosti, se voi johtua odottamattomasta tyyppipakosta.


### `"use strict"`


Voit ottaa käyttöön tiukemman tilan, joka muuttaa jotkut hiljaiset virheet oikeiksi virheiksi ja estää sinua käyttämästä joitakin kielen vaarallisimpia ominaisuuksia.


Jos haluat ottaa tämän tiukemman tilan käyttöön, lisää tämä rivi tiedoston tai funktion alkuun:


```javascript
"use strict"
```


Esimerkiksi:


```javascript
"use strict"
name = "Alice" // ReferenceError: name is not defined
```


Ilman strict-tilaa JavaScript loisi hiljaa globaalin muuttujan nimeltä `nimi`. Mutta strict-tilassa tästä tulee todellinen virhe, joka auttaa sinua havaitsemaan virheet aikaisemmin.


Strict-tila poistaa käytöstä myös joitakin JavaScriptin vanhentuneita ominaisuuksia ja tekee koodistasi helpommin optimoitavaa ja ylläpidettävää.


## Arvo vs. viitearvo

<chapterId>bb898425-dc2f-5e5c-864b-0cb7a4a9aea9</chapterId>


JavaScript käsittelee erilaisia arvoja eri tavoin.


Jotkin arvot **kopioidaan**, kun osoitat ne muuttujaan.


Toiset muuttujat ovat **jakautuneita**, kun osoitat ne uudelle muuttujalle, joten jos muutat yhtä muuttujaa, myös toinen muuttuu.


### Pass by value


Kun arvo siirretään **arvon mukaan**, JavaScript tekee siitä **kopion**.


Jos siis muutat toista, se ei vaikuta toiseen.


Tämä tapahtuu primitiivisille tyypeille, kuten:



- numerot
- jouset
- booleanit (`true` ja `false`)
- `null`
- `undefined`


Katsotaanpa esimerkkiä:


```javascript
let a = 5
let b = a

b = 10

console.log(a) // 5
console.log(b) // 10
```


Annoimme `b`:lle arvon `a`, mutta sitten muutimme `b`:n arvoksi `10`.


Koska numerot välitetään arvon mukaan, JavaScript kopioi `5`:n `b`:hen. `b`:ssä oleva `5` on riippumaton alkuperäisestä `a`:ssa olevasta `5`:stä, joten `b`:n arvon muuttaminen ei vaikuttanut `a`:aan.


Kokeillaan merkkijonon kanssa:


```javascript
let name1 = "Alice"
let name2 = name1

name2 = "Bob"

console.log(name1) // Alice
console.log(name2) // Bob
```


Jälleen kerran `nimi2`:n muuttaminen ei vaikuttanut `nimi1`:een, koska merkkijonot välitetään myös arvon mukaan.


Sama tapahtuu, kun primitiivin siirtää funktiolle: se kopioidaan. Funktio ei siis voi muuttaa alkuperäistä.


```javascript
function plusOne(x) {
x = x + 1
}

let number = 5

plusOne(number)

console.log(number) // 5
```


Vaikka funktion sisällä `x`:ään lisättiin `1`, alkuperäinen `luku` ei muuttunut.


Tämä johtuu siitä, että funktioon syötettiin vain **kopio**.


### Pass by reference


Objektit siirretään **viittauksella**.


Se tarkoittaa, että sen sijaan, että JavaScript kopioisi niitä, se vain siirtää **viittauksen** siihen, ja jos muutat sitä, kaikki muut muuttujat, jotka osoittavat siihen, näkevät muutoksen myös.


Esimerkiksi:


```javascript
const person1 = { name: "Alice" }
const person2 = person1

person2.name = "Bob"

console.log(person1.name) // Bob
console.log(person2.name) // Bob
```


Sekä `person1` että `person2` viittaavat samaan objektiin muistissa.


Kun siis muutimme `person2.name`, muutimme myös `person1.name`, koska molemmat katsovat samaa asiaa.


Joukot ovat objekteja, joten kokeillaan samaa joukon kanssa:


```javascript
const list1 = [1, 2, 3]
const list2 = list1

list2.push(4)

console.log(list1) // [1, 2, 3, 4]
console.log(list2) // [1, 2, 3, 4]
```


Työnsimme `4` listaan `list2`, mutta se vaikutti myös listaan `list1`, koska molemmat viittaavat samaan arrayyn.


Katsotaan, mitä tapahtuu, kun välitämme objektin funktiolle:


```javascript
function rename(user) {
user.name = "Charlie"
}

const person = { name: "Dana" }

rename(person)

console.log(person.name) // Charlie
```


Funktio muutti objektin! Tämä johtuu siitä, että se sai **viittauksen** alkuperäiseen `person`-objektiin.


Se ei saanut kopiota. Se sai pääsyn alkuperäiseen objektiin, ja sen myötä se sai kyvyn muokata sitä.


On tärkeää muistaa tämä ero, koska muuten koodimme saattaa käyttäytyä eri tavalla kuin odotamme. Saatamme esimerkiksi kirjoittaa funktion odottaen, että se ei muokkaa vastaanottamiaan argumentteja, ja huomata myöhemmin, että se itse asiassa muokkaa niitä (koska ne ovat objekteja, joten ne on välitetty viitteenä).


## Työskentely funktioiden kanssa

<chapterId>e0d277a8-c642-5af7-9e53-dee27c811967</chapterId>


Olet jo oppinut, miten funktioita voi ilmoittaa ja käyttää JavaScriptissä. Mutta JavaScript antaa sinulle lisää työkaluja, joilla voit työskennellä funktioiden kanssa tehokkailla tavoilla.


### Nuolitoiminnot


Nuolifunktiot ovat lyhyempi tapa kirjoittaa funktioita. Avainsanan `function` sijasta käytetään nuolta (`=>`).


Tässä on normaali toiminto:


```javascript
function greet(name) {
return `Hello, ${name}!`
}
```


Nuoliversio näyttää tältä:


```javascript
const greet = (name) => {
return `Hello, ${name}!`
}
```


Jos funktiossa on **vain yksi rivi**, voit ohittaa sulkeet ja `return`:


```javascript
const greet = (name) => `Hello, ${name}!`
```


Jos funktiolla on **vain yksi parametri**, voit jopa jättää sulkeet parametrien ympäriltä pois:


```javascript
const greet = name => `Hello, ${name}!`
```


Nuolifunktiot ovat hyvin yleisiä nykyaikaisessa JavaScriptissä, sillä niiden avulla voidaan ilmaista yksinkertaisia funktioita huomattavasti vähemmällä määrittelyllä.


### Oletusparametrit


Joskus haluat, että funktiolla on **esiarvo**, jos mitään argumenttia ei anneta.


Voit tehdä sen näin:


```javascript
function sayHello(name = "friend") {
console.log(`Hello, ${name}!`)
}

sayHello("Alice") // Hello, Alice!
sayHello()        // Hello, friend!
```


Oletusarvoa `"friend"` käytetään, kun mitään ei anneta.


### Levitysparametrit (`...`)


Entä jos funktiosi ottaa joustavasti useita argumentteja?


Voit käyttää **hajontaoperaattoria** (`...`) koota ne joukkoon:


```javascript
function logAll(...items) {
console.log(items)
}

logAll(1, 2, 3) // [1, 2, 3]
logAll("a", "b") // ["a", "b"]
```


Tämän jälkeen voit käyttää silmukkaa jokaisen kohteen käsittelyyn:


```javascript
function logEach(...items) {
for (const item of items) {
console.log(item)
}
}
```


Operaattori spread on hyödyllinen, kun et tiedä, kuinka monta argumenttia välitetään.


### Korkeamman asteen funktiot


**Korkeamman asteen funktio** on funktio, joka:



- ottaa syötteenä toisen funktion
- ja/tai palauttaa funktion tulosteena


Tässä on yksinkertainen esimerkki:


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


Tämä tulostuu:


```
Hello, friend!
Hello, friend!
```


Voimme siirtää sille nuolifunktion:


```javascript
runTwice(
() => console.log("Hello!")
)
```


Tämä tulostuu:


```
Hello!
Hello!
```


Voit myös kirjoittaa funktioita, jotka **palauttavat** muita funktioita:


```javascript
function makeGreeter(name) {
return () => console.log(`Hi, ${name}`)
}

const greetAlice = makeGreeter("Alice")
const greetBob = makeGreeter("Bob")

greetAlice() // Hi, Alice
greetBob() // Hi, Bob
```


Funktio `makeGreeter` on funktio, joka rakentaa muita funktioita. Se vastaanottaa merkkijonon ja palauttaa uuden funktion, joka käyttää tätä merkkijonoa `console.log`-kutsussaan.


Tällainen malli on erittäin tehokas, sillä sen avulla voit jättää funktioihin "aukkoja", jotka voit täyttää myöhemmin haluamallasi käyttäytymisellä.


### `map()`, `filter()`, `reduce()`


JavaScript antaa sinulle joitakin hyödyllisiä sisäänrakennettuja menetelmiä, joita voit käyttää matriisien kanssa.


Nämä metodit ottavat argumentteina funktioita, joten ne ovat myös korkeamman asteen funktioita.


`map()` muuttaa jokaisen matriisin kohteen joksikin muuksi.


Esimerkki:


```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map(x => x * 2)

console.log(doubled) // [2, 4, 6]
```


Jokainen luku kaksinkertaistetaan, ja tuloksena on uusi joukko.


`filter()` poistaa kohteita joukosta, jos ne eivät läpäise testiä.


Esimerkki:


```javascript
const numbers = [1, 2, 3, 4, 5]
const numbersGreaterThanTwo = numbers.filter(x => x > 2)

console.log(numbersGreaterThanTwo) // [3, 4, 5]
```


Ainoastaan ne tietueet, joiden kohdalla `x > 2`-ehto palauttaa `true`, säilytetään.


`reduce()`:tä käytetään yhdistämään kaikki matriisin kohteet yhdeksi arvoksi.


Esimerkki:


```javascript
const numbers = [1, 2, 3, 4]
const total = numbers.reduce((current, next) => current + next)

console.log(total) // 10
```


`reduce` käy läpi matriisin ja tässä esimerkissä soveltaa operaattoria `+` välillä `1` ja `2`, sitten tuloksena olevan `3` ja `3` välillä, sitten tuloksena olevan `6` ja `4` välillä, kunnes se saa kaikkien matriisin merkintöjen summan (joka on 10).


Voit käyttää `reduce()` -toimintoa moniin asioihin, kuten yhteenlaskuihin, keskiarvoihin tai uusien arvojen muodostamiseen askel askeleelta.


Nämä menetelmät (`map`, `filter`, `reduce`) ovat tehokkaita työkaluja tietojen käsittelyyn ilman manuaalisten silmukoiden kirjoittamista.


Voit jopa yhdistää ne toimintojen ketjuksi, esimerkiksi näin:


```javascript
const numbers = [1, 2, 3, 4, 5]

const result = numbers
.map(n => n * 2)        // Double each entry, obtain [2, 4, 6, 8, 10]
.filter(n => n > 3) // Keep only the entries bigger than 3, so you get [4, 6, 8, 10]
.reduce((n1, n2) => n1 + n2) // Adds them: 4 + 6 + 8 + 10 = 28

console.log(result) // 28
```


## Työskentely objektien kanssa

<chapterId>7842aada-f009-5518-b8e3-1104e166a035</chapterId>


Tässä luvussa opettelemme muutamia tehokkaita ja hieman edistyneempiä työkaluja objektien kanssa työskentelyyn JavaScriptissä.


### Yksityiset kiinteistöt


Joskus haluamme piilottaa objektin ominaisuuden, jotta sitä ei voi muuttaa tai käyttää objektin ulkopuolelta. JavaScript tarjoaa tähän keinon käyttämällä `#` ennen ominaisuuden nimeä. Näin luodaan **private**-ominaisuus, johon pääsee käsiksi vain luokan sisältä.


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


Yksityiset ominaisuudet ovat hyödyllisiä, kun haluat estää tahattomat muutokset.


### `static` Ominaisuudet


Joskus ominaisuuden halutaan kuuluvan luokalle itselleen, ei jokaiselle luokasta luotavalle objektille. Sitä varten on `static`. Staattinen ominaisuus sisältyy luokkaan, ja kaikki kyseisen luokan objektit viittaavat siihen.


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


Tämä on hyödyllistä jaettujen tietojen ja menetelmien tallentamisessa, jotka koskevat koko objektiryhmää, ei vain yhtä objektia.


### `get` ja `set`


JavaScriptissä `get`- ja `set`-ominaisuuksien avulla voit luoda ominaisuuksia, jotka *näyttävät* tavallisilta muuttujilta, mutta jotka itse asiassa suorittavat erikoiskoodia taustalla.


Get-metodi suoritetaan, kun yrität *lukea* ominaisuutta. Se ilmoitetaan kirjoittamalla `get` ennen metodia, jossa on ominaisuuden nimi.


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


Vaikka `fullName` ei olekaan tavallinen ominaisuus, voimme käyttää sitä kuin sellaista, ja kulissien takana se käyttää `get`-funktiota koko nimen muodostamiseksi.


Set-menetelmä suoritetaan, kun ominaisuudelle *annetaan* arvo. Sen avulla voit hallita, mitä tapahtuu, kun joku yrittää muuttaa arvoa. Se ilmoitetaan kirjoittamalla `set` ennen metodia, jossa on ominaisuuden nimi.


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


Kun teemme `user.fullName = "John Smith"`, se suorittaa `set`-metodin ja päivittää `firstName`- ja `lastName`-arvot.


Vaikka tuntuu siltä, että asetamme vain yksinkertaisen muuttujan, käynnistämme itse asiassa logiikan, joka päivittää muita ominaisuuksia.


## Avaimet ja arvot

<chapterId>01a397b8-c12a-5c39-82b3-6d9ebbb72a29</chapterId>


Jokaisella JavaScript-objektin ominaisuudella on **avain** (jota kutsutaan myös ominaisuuden nimeksi) ja **arvo**.


Esimerkiksi:


```javascript
const user = {
name: "Alice",
age: 30
}
```


Tässä objektissa `"nimi"` ja `"ikä"` ovat avaimet, ja "Alice" ja `30` ovat niiden arvot.


### Dynaaminen pääsy


Joskus ominaisuuden nimeä ei tiedetä etukäteen... ehkä se saadaan käyttäjän syötteestä tai luetaan muuttujasta. Voit silti käyttää sitä käyttämällä **sulkeisnotaatiota**, kuten `myObject["keyName"]`.


```javascript
const user = {
name: "Alice",
age: 30
}

console.log(user["name"]) // Alice
```


Välitimme objektille merkkijonon `nimi` saadaksemme vastaavan arvon.


Voimme tallentaa avaimen muuttujaan ja käyttää sitä myöhemmin vastaavaan arvoon, kuten seuraavalla tavalla


```javascript
const user = {
name: "Alice",
age: 30
}

const key = "name"

console.log(user[key]) // Alice
```


### Dynaaminen Assignment


Voit myös luoda tai päivittää kohteen ominaisuuksia käyttämällä muuttujia avaimina.


```javascript
const settings = {}

const key = "theme"
settings[key] = "dark"

console.log(settings) // { theme: "dark" }
```


Tämä on hyödyllistä, kun haluat rakentaa kohteen vaiheittain. Esimerkiksi:


```javascript
const user = {}

user["username"] = "bananaFan123"
user["email"] = "banana@fruit.com"

console.log(user)
// { username: "bananaFan123", email: "banana@fruit.com" }
```


Voit jopa käyttää dynaamista avainta *objektin luomisen* aikana käyttämällä hakasulkeita:


```javascript
const key = "language"
const config = {
[key]: "JavaScript"
}

console.log(config.language) // JavaScript
```


Tätä kutsutaan **laskennalliseksi ominaisuudeksi**. Arvioidaan hakasulkeiden sisällä oleva arvo, ja tulosta käytetään avaimena.


### `Symboli` Tyyppi


Merkkijonojen lisäksi JavaScript sallii myös käyttää objektin avaimena erityistä tyyppiä nimeltä `Symbol`.


Aloitetaan yksinkertaisella esimerkillä:


```javascript
const id = Symbol("userID")

const user = {
name: "Bob",
[id]: 12345
}

console.log(user[id]) // 12345
```


Tässä esimerkissä `id` on Symbol. Se ei ole merkkijono, mutta toimii silti avaimena. Jos yrität kirjautua `user`-konsoliin, näet tämän:


```javascript
console.log(user) // { name: 'Bob', [Symbol(userID)]: 12345 }
```


Toinen tärkeä asia: jokainen luomaasi symboli on yksilöllinen, vaikka ne olisi luotu käyttäen samaa merkkijonoa.


```javascript
const a = Symbol("label")
const b = Symbol("label")

console.log(a === b) // false
```


Symbolien avulla voit määritellä näppäimiä, jotka eivät ole ristiriidassa tavallisten näppäinten kanssa. Oletetaan esimerkiksi, että sinulla on objekti, jolla on ominaisuus `nimi`, mutta käyttäjä muokkaa objektia tulevaisuudessa tavalla, jota et voi ennustaa, ja tämä käyttäjä saattaa lisätä myös ominaisuuden `nimi`. Jos alkuperäinen `name`-ominaisuus oli määritelty merkkijonolla, se korvattaisiin uudella ominaisuudella, esimerkiksi näin:


```javascript
const obj = {
name: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy' }
```


Jos sen sijaan käytämme Symbolia:


```javascript
const name = Symbol("name")

const obj = {
[name]: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy', [Symbol(name)]: 'John' }
```


Kuten näet, alkuperäinen `name`-ominaisuus säilyy jotenkin tällä tavalla. Tämä voi olla hyödyllistä tietyissä ääritapauksissa.


## Hyötyobjektit

<chapterId>516e74c8-2a11-545a-a4d1-c2cabb91a273</chapterId>


JavaScript antaa meille joitakin hyödyllisiä sisäänrakennettuja objekteja, jotka auttavat meitä tekemään esimerkiksi virheenkorjausta ja matemaattisia operaatioita.


### Muut "konsoli"-menetelmät


Olet jo nähnyt `console.log`-tiedoston, joka tulostaa arvot näytölle.


`console`-oliolla on myös muita hyödyllisiä metodeja, jotka voivat auttaa sinua ohjelmiesi debuggaamisessa.


#### `console.warn`


Tulostaa viestin keltaisella värillä (tai varoituskuvakkeella joissakin ympäristöissä):


```javascript
console.warn("This is just a warning.")
```


#### `console.error`


Tulostaa punaisella viestin, kuten virheen:


```javascript
console.error("Something went wrong!")
```


#### `console.table`


Näyttää joukon tai objektin taulukkona:


```javascript
const users = [
{ name: "Alice", age: 25 },
{ name: "Bob", age: 30 }
]

console.table(users)
```


Tämä tulostaa taulukon seuraavasti:


```
┌─────────┬────────┬─────┐
│ (index) │  name  │ age │
├─────────┼────────┼─────┤
│    0    │ 'Alice'│  25 │
│    1    │ 'Bob'  │  30 │
└─────────┴────────┴─────┘
```


Tämä voi olla hyödyllistä strukturoitujen tietojen visualisoinnissa.


#### `console.time` ja `console.timeEnd`


Voit mitata, kuinka kauan jokin kestää:


```javascript
console.time("timer")
for (let i = 0; i < 1000000; i++) {}
console.timeEnd("timer")
```


Tämä tulostaa jotakin seuraavanlaista:


```
timer: 2.379ms
```


Hyödyllinen yksinkertaiseen suorituskykytestaukseen.


### `Math`-objekti


JavaScript antaa sinulle `Math`-olion, jossa on hyödyllisiä laskutoimituksia varten tarkoitettuja metodeja.


#### `Math.random()`


Palauttaa satunnaisluvun väliltä 0 (mukaan lukien) ja 1 (pois lukien):


```javascript
const r = Math.random()
console.log(r)
```


Esimerkkitulos:


```
0.4387429859
```


#### `Math.floor()` ja `Math.ceil()`



- `Math.floor(n)` pyöristää **alaspäin** lähimpään kokonaislukuun
- `Math.ceil(n)` pyöristää **ympäri** lähimpään kokonaislukuun


```javascript
console.log(Math.floor(4.9)) // 4
console.log(Math.ceil(4.1))  // 5
```


#### `Math.round()`


Pyöristää lähimpään kokonaislukuun:


```javascript
console.log(Math.round(4.4)) // 4
console.log(Math.round(4.6)) // 5
```


#### `Math.max()` ja `Math.min()`


Palauttaa suurimman tai pienimmän arvon numeroiden luettelosta:


```javascript
console.log(Math.max(5, 9, 3)) // 9
console.log(Math.min(5, 9, 3)) // 3
```


#### `Math.pow()` ja `Math.sqrt()`



- `Math.pow(a, b)` antaa sinulle `a` potenssiin `b`
- `Math.sqrt(n)` antaa sinulle neliöjuuren arvosta `n`


```javascript
console.log(Math.pow(2, 3))   // 8
console.log(Math.sqrt(16))    // 4
```


# Edistynyt JavaScript

<partId>72c30671-ca20-5617-92a5-d5ba7aa38c93</partId>


## Muut kokoelmat

<chapterId>a9a70c6d-a343-5a46-a383-e288bc2700e3</chapterId>


JavaScript antaa meille joitakin erityisiä kokoelmatyyppejä, jotka menevät tavallisia matriiseja ja objekteja pidemmälle. Näitä ovat `Map` ja `Set`.


Ne auttavat sinua tallentamaan ja hallitsemaan arvoryhmiä, mutta ne toimivat eri tavalla kuin tähän asti.


`Map` on kokoelma **avain-arvopareja**, aivan kuten objekti. Sillä on kuitenkin joitakin tärkeitä eroja:



- Avaimet voivat olla **mitä tahansa arvoja**, eivät vain merkkijonoja.
- Kohteiden järjestys säilyy.
- Siinä on sisäänrakennettuja menetelmiä, jotka helpottavat työskentelyä sen kanssa.


Luodaan uusi kartta näin:


```javascript
const myMap = new Map()
```


Tämä luo tyhjän kartan. Voit lisätä siihen merkintöjä käyttämällä `myMap.set(key, value)`:


```javascript
myMap.set("name", "Alice")
```


Tämä lisää avaimen `"name"` ja arvon `"Alice"`.


Voit myös käyttää numeroa avaimena:


```javascript
myMap.set(42, "The answer")
```


Ja jopa objekti avaimena:


```javascript
const objKey = { id: 1 }
myMap.set(objKey, "Object as key")
```


Tämä ei toimisi tavallisten objektien kanssa, jotka sallivat vain merkkijonoavaimet.


Jos haluat **ottaa arvon**, käytä `myMap.get(key)`:


```javascript
console.log(myMap.get("name"))     // Alice
console.log(myMap.get(42))         // The answer
console.log(myMap.get(objKey))     // Object as key
```


Jos haluat **tarkistaa, onko avain olemassa**, käytä `myMap.has(key)`:


```javascript
console.log(myMap.has("name")) // true
```


Voit **poistaa avaimen** käyttämällä `myMap.delete(key)`:


```javascript
myMap.delete("name")
```


Jos haluat **tyhjentää koko kartan**, käytä `myMap.clear()`:


```javascript
myMap.clear()
```


Kartat soveltuvat erinomaisesti suurten arvokokoelmien hallintaan, koska arvojen käyttäminen suuressa kartassa on yleensä paljon suorituskykyisempää kuin suuressa objektissa.


### `Set`


`Set` on kokoelma **arvoja** (ei avaimia), joissa jokaisen arvon on oltava **yksilöllinen**. Tämä tarkoittaa:



- Samaa arvoa ei voi saada kahdesti
- Arvot tallennetaan siinä järjestyksessä kuin lisäät ne


Luodaan tällainen sarja:


```javascript
const mySet = new Set()
```


Jos haluat **lisätä arvoja**, käytä `mySet.add(value)`:


```javascript
mySet.add(1)
mySet.add(2)
mySet.add(2) // duplicate, will be ignored
```


Vaikka yritimme lisätä `2` kahdesti, joukko säilyttää vain yhden kopion.


Jos haluat **tarkistaa, onko arvo joukossa**, käytä `mySet.has(value)`:


```javascript
console.log(mySet.has(2)) // true
console.log(mySet.has(3)) // false
```


Jos haluat **poistaa arvon**, käytä `mySet.delete(value)`:


```javascript
mySet.delete(2)
```


Jos haluat **tyhjentää kaiken**, käytä `mySet.clear()`:


```javascript
mySet.clear()
```


`Set` on hyödyllinen, kun haluat säilyttää ainutlaatuisten arvojen kokoelman ilman, että sinun tarvitsee tarkistaa manuaalisesti kaksoiskappaleet:


```javascript
const numberArray = [1, 2, 2, 3, 4, 4, 4, 5]

const numberSet = new Set(numberArray)

console.log(numberSet) // Set(5) { 1, 2, 3, 4, 5 }
```


`Set` välttää päällekkäisyydet puolestasi.


## Iteraattorit

<chapterId>61d24e5e-b7e4-541a-8322-778f61f26a72</chapterId>


Useimmat JavaScriptissä olevat asiat, joiden yli voi tehdä silmukoita (kuten matriisit, merkkijonot, kartat, joukot), ovat **iteraattoreita**: ne voivat tarjota iteraattoreita sisällölleen.


**Iteraattori** on JavaScriptissä erityinen objekti, jonka avulla voit käydä läpi listan kohteita **yksi kerrallaan**.


### `Object`-iteraattorit


Toisin kuin matriisit tai kartat, tavalliset objektit eivät **ole iteroitavissa** komennolla `for...of`. Jos yrität tätä:


```javascript
const user = {
name: "Alice",
age: 30
}

for (const value of user) {
console.log(value)
}
```


Saat virheilmoituksen:


```
TypeError: user is not iterable
```


Tämä johtuu siitä, että tavallisilla objekteilla ei ole sisäänrakennettua iteraattoria. Mutta JavaScript antaa sinulle muita työkaluja, joilla voit tehdä silmukoita niiden yli.


#### `Object.keys()`


Voit käyttää `Object.keys(obj)` saadaksesi objektin **avainten** joukon ja käydä sen jälkeen silmukassa sen läpi:


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


Tämä tulostuu:


```
name
age
```


#### `Object.values()`


Jos haluat käydä läpi **arvot**, käytä `Object.values()`:


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


Tämä tulostuu:


```
Alice
30
```


#### `Object.entries()`


Jos haluat sekä avaimen että arvon**, käytä `Object.entries()`:


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


Tämä tulostuu:


```
name is Alice
age is 30
```


Vaikka objektit eivät ole suoraan iteroitavissa, nämä metodit antavat sinulle täyden pääsyn niiden sisältöön tavalla, joka toimii hyvin `for...of`:n kanssa.


Mutta miten iteraattorit toimivat?


### `Symbol.iterator`


Kaikkien iteraattorien salaisuus on erityinen **symboli** nimeltä `Symbol.iterator`.


Tämä symboli on sisäänrakennettu avain, joka kertoo JavaScriptille: "Tämä objekti voidaan iteroida."


Kun kutsut `myIterable[Symbol.iterator]()`, JavaScript antaa sinulle takaisin **iteratoriobjektin**, jossa on `.next()`-metodi.


Katsotaanpa, miltä se näyttää:


```javascript
const colors = ["red", "green", "blue"]

const iterator = colors[Symbol.iterator]()

console.log(iterator.next()) // { value: 'red', done: false }
```


Jokainen `.next()`-kutsu antaa sinulle seuraavan arvon. Kun se on valmis, se palaa:


```javascript
{ value: undefined, done: true }
```


### `next()`


Metodia `.next()` käytetään hakemaan sarjan seuraava kohde.


Joka kerta kun kutsut `.next()`, saat objektin, jossa on kaksi avainta:



- `value`: nykyinen kohde
- `done`: boolean, joka kertoo, onko iteraatio päättynyt


Tehdään täydellinen esimerkki:


```javascript
const names = ["Lina", "Tom", "Eva"]      // declare an array
const iterator = names[Symbol.iterator]() // use the Symbol.iterator function to get an iterator for this array

let result = iterator.next()              // get the first element of the array

while (!result.done) {                    // repeat this loop until you reach the last element of the array, which is marked with { done: true }
console.log(result.value)               // print the value of each element
result = iterator.next()                // get the next element of the array
}
```


Tämä tulostuu:


```
Lina
Tom
Eva
```


Näin `for...of`-silmukka toimii konepellin alla: se käyttää tätä mallia `.next()`:n kanssa.


Saat saman tuloksen käyttämällä


```javascript
const names = ["Lina", "Tom", "Eva"]

for (const result of names) {
console.log(result)
}
```


### Luokan tekeminen iteroitavaksi


Voit myös määritellä oman **iterable-luokan** lisäämällä `[Symbol.iterator]()`-metodin.


Sanotaan, että haluamme luokan, joka edustaa **lukualuetta**, esimerkiksi 1:stä 5:een.


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


Tämä tulostuu:


```
1
2
3
4
5
```


Näin tapahtuu:



- Määritimme luokan `Range`
- Luokan sisällä toteutimme `[Symbol.iterator]()`, jotta JavaScript tietää, miten sitä voidaan kerrata
- Menetelmä `next()` palauttaa jokaisen numeron yksi kerrallaan
- Kun saavutamme "lopun", se palauttaa "{ done: true }"


Nyt `Range`-luokkamme toimii kuin array, ja voimme käyttää sitä missä tahansa silmukassa, joka odottaa iterablea.


### Generaattorifunktiot ja `yield`


Jotta iteraattoreiden luominen olisi helpompaa, JavaScript tarjoaa **generaattorifunktioita**, joissa käytetään `function*`-avainsanaa (se on `function`, jonka lopussa on `*`) ja `yield`-avainsanaa.


Kokeillaan:


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


Jokainen `yield` antaa takaisin arvon ja **tauottaa** funktion, kunnes seuraavaa `.next()` kutsutaan.


Voit myös kiertää generaattorin läpi komennolla `for...of`:


```javascript
for (const num of numberGenerator()) {
console.log(num)
}
```


Tämä tulostuu:


```
1
2
3
```


## Samanaikaisuus takaisinsoittojen kanssa

<chapterId>f3fc76ca-b3ef-54eb-a06e-501007002054</chapterId>


Tähän asti koodimme on ollut **synkronista**: se suoritetaan rivi kerrallaan, järjestyksessä. Mutta jotkut asiat reaalimaailmassa vievät aikaa, emmekä halua koko ohjelman pysähtyvän odottamaan.


Tässä luvussa esittelemme uuden käsitteen: **valuutta**. Sen avulla voimme manipuloida järjestystä, jossa asiat tehdään. Tämä on hyödyllistä, kun käsitellään esimerkiksi ajastimia, käyttäjän syötteitä tai tiedostojen lukemista levyltä. JavaScript tarjoaa erilaisia työkaluja samanaikaisuuden toteuttamiseen.


### `setTimeout`


Toiminnolla `setTimeout` voit **suorittaa toiminnon myöhemmin**, kun jokin aika on kulunut.


Esimerkki:


```javascript
console.log("Start")

setTimeout(
() => console.log("This runs after 2 seconds"),
2000
)

console.log("End")
```


Tämä tulostuu:


```
Start
End
This runs after 2 seconds
```


Vaikka `setTimeout` on keskellä koodia, se ei estä muuta. Sen sijaan se aikatauluttaa toiminnon suoritettavaksi **myöhemmin** ja siirtyy välittömästi eteenpäin.


"2000" tarkoittaa 2000 millisekuntia (eli 2 sekuntia).

Tässä on **Callbacks**- ja **Promise**-osiot, jotka on kirjoitettu uudelleen ja jotka ovat aloittelijoille helpommin ymmärrettävissä, käyttäen datan manipulointia ja selkeitä huomautuksia kauttaaltaan:


### Takaisinkutsut


**Palautus** on vain funktio, jonka annamme toiselle funktiolle, jotta sitä voidaan **kutsua myöhemmin**.


Katsotaanpa todellista esimerkkiä numeroiden avulla. Kuvitellaan, että meillä on lista numeroita ja haluamme kaksinkertaistaa jokaisen niistä ja soveltaa sitten funktiota (takaisinkutsu) tuloksena olevaan "kaksinkertaistettuun" joukkoon, mutta haluamme tehdä sen pienen viiveen jälkeen, ikään kuin odottaisimme jotain hidasta (kuten tietojen lataamista internetistä).


Tässä on funktio, joka tekee sen käyttämällä **palautetta**:


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


Yritetään käyttää tätä toimintoa:


```javascript
const input = [1, 2, 3]

doubleNumbers(input, function(result) {
console.log("Here is the doubled array:", result)
})
```


Tämä tulostuu 1 sekunnin kuluttua:


```
Here is the doubled array: [ 2, 4, 6 ]
```


**Mitä täällä tapahtuu?*


1. Luettelo numeroista, jotka haluamme kaksinkertaistaa, annetaan `input`.

2. Välitämme myös **palautusfunktion**, joka kertoo ohjelmalle, mitä tehdä *tuplauksen* jälkeen.

3. Sisällä `doubleNumbers` simuloimme viiveen käyttämällä `setTimeout`, sitten teemme tuplauksen.

4. Kun tämä on tehty, kutsumme takaisinkutsua tuloksena syntyvälle "kaksinkertaistetulle" arraylle.


Tämä tekniikka toimii, mutta kuvittele, että haluat tehdä **lisävaiheita** tämän jälkeen, kuten suodattaa pienet luvut pois ja laskea ne sitten yhteen. Sinun pitäisi **pesäyttää** lisää tällaisia takaisinkutsuja:


```javascript
doubleNumbers(input, function(doubled) {
filterBigNumbers(doubled, function(filtered) {
sumNumbers(filtered, function(total) {
console.log("Final result:", total)
})
})
})
```


Tämä on Hard luettavaa ja sotkuista. Tätä tyyliä kutsutaan nimellä **callback hell**, ja juuri sen korjaamiseksi `Promise` luotiin.


## Samanaikaisuus lupausten kanssa

<chapterId>30fddaca-729f-5c8d-bf86-8dfc7b3c9800</chapterId>


Lupaus on sisäänrakennettu JavaScript-objekti, joka edustaa arvoa, joka on **valmis tulevaisuudessa**.


Voimme luoda lupauksen näin:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve("It worked!") // This means everything went OK
})
```


`new Promise()` -osa luo lupauksen.


Sen sisällä annetaan funktio, jolla on kaksi parametria:



- `resolve`, on funktio, jota kutsumme, kun kaikki on onnistunut
- `reject`, on funktio, jota kutsumme, jos jokin menee pieleen


Yllä olevassa esimerkissä se vain ratkaistaan välittömästi viestillä `"Se toimi!"`.


### `.then()`


Jos haluat tehdä jotain **jälkeen**, kun lupaus on tehty, käytämme komentoa `.then()`:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve(100) // This means everything went OK
})

promise.then(result => {
console.log("The result is:", result)
})
```


Tämä tulostuu:


```
The result is: 100
```


Arvo, jonka annoimme funktiolle `resolve()`, lähetetään funktiolle `.then()` tuloksena.


Simuloidaan tehtävä, joka kestää 2 sekuntia, käyttämällä `setTimeout`:


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


Tämä odottaa 2 sekuntia ja tulostaa sitten:


```
Done waiting!
```


### `reject()`


Luodaan lupaus, joka **epäonnistuu**:


```javascript
const failingPromise = new Promise((resolve, reject) => {
reject("Something went wrong")
})
```


Jos nyt käytämme `.then()`:tä tähän, mitään ei tapahdu, koska `.then()` käsittelee vain onnistumisia.


Virheiden käsittelyyn käytetään `.catch()`:


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


Tämä tulostaa vain


```
Caught an error: Something went wrong
```


`reject()` -funktiolle annettu arvo lähetetään `.catch()`-funktiolle.


Rakennetaan lupaus, joka **toisin toimii ja toisinaan epäonnistuu** jonkin ehdon perusteella.


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


Nyt voimme kutsua tätä ja käsitellä molemmat tapaukset:


```javascript
checkNumber(5)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Tämä tulostuu:


```
Success: Positive number
```


Ja jos yritämme eri numerolla:


```javascript
checkNumber(-1)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Se tulostuu:


```
Failure: Not a positive number
```


### Operaatioiden ketjuttaminen `Promise`:n avulla



Voimme kirjoittaa aikaisemman esimerkkimme uudelleen käyttäen `Promise`, ja se näyttää paljon siistimmältä.


Aloitetaan kirjoittamalla uusi versio tuplausfunktiostamme, mutta tällä kertaa se palauttaa **lupauksen**:


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


Nyt voimme käyttää komentoa `.then()` kertoaksemme JavaScriptille, mitä tulokselle tehdään:


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


Tämä tulostuu:


```
Doubled numbers: [ 2, 4, 6 ]
```


Toistaiseksi tämä toimii samoin kuin callback-versio, mutta nyt koodia on helpompi laajentaa ja lukea.


Sanotaan, että haluamme lisätä lisää vaiheita:


1. Kaksinkertaista ensin kaikki numerot

2. Poista sitten numerot, jotka ovat pienempiä kuin 4

3. Lisää ne lopuksi kaikki yhteen


Voimme kirjoittaa yhden funktion jokaista vaihetta varten, ja kaikki käyttävät lupauksia:


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


Nyt voimme **ketjuttaa** ne yhteen näin:


```javascript
const input = [1, 2, 3]

doubleNumbers(input)
.then(filterBigNumbers)
.then(sumNumbers)
.then(
result => console.log("Final result after all steps:", result)
)
```


Tämä tulostuu:


```
Final result after all steps: 10
```


Käydään läpi, mitä tämä tekee:


1. `doubleNumbers` tuplaa joukon: `[2, 4, 6]`

2. `filterBigNumbers` poistaa kaiken ≤ 3: `[4, 6]`

3. `sumNumbers` lisää loput numerot: `4 + 6 = 10`

4. Lopuksi tulostetaan tulos.


Jokainen `.then()` odottaa, että sitä edeltävä vaihe päättyy. Voimme siis muodostaa **toimintaketjun** ilman sisäkkäisyyttä. Tämä tekee koodista luettavampaa ja helpommin korjattavaa.


## Samanaikaisuus `async`/`await`-ohjelmilla

<chapterId>6e93d29f-c8bf-5fd1-a9c9-4e794ee6cbd0</chapterId>


Näimme, miten `Promise`-ketjut auttavat meitä välttämään takaisinkutsuhelvetin, mutta niitä voi silti olla hieman hankala lukea, kun niihin liittyy monia vaiheita.


Tässä kohtaa `async` ja `await` tulevat kuvaan. Niiden avulla voimme kirjoittaa asynkronista koodia, joka näyttää synkroniselta koodilta**, mikä tekee siitä helpommin ymmärrettävää.


### Mikä on `async`?


Kun kirjoitat avainsanan `async` ennen funktiota, JavaScript kietoo funktion paluuarvon automaattisesti Promiseen.


Katsotaanpa perusesimerkki:


```javascript
async function greet() {
return "hello"
}
```


Jos kutsut tätä funktiota:


```javascript
const result = greet()
console.log(result)
```


Näet tämän:


```
Promise { 'hello' }
```


Vaikka palautit juuri merkkijonon, JavaScript muuttaa sen Promise-merkiksi. Voit saada todellisen arvon käyttämällä `.then()` seuraavasti:


```javascript
greet().then( result => console.log(result) ) // prints "hello"
```


Tai voit käyttää `await`...


### Mikä on `await`?


Avainsana `await` kertoo JavaScriptille: "Odota, kunnes tämä lupaus on tehty, ja anna minulle sitten tulos."


Mutta voit käyttää `await`-ominaisuutta vain **asynkronisen funktion** sisällä.


Kirjoitetaan esimerkki uudelleen käyttäen `await`:


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


Nyt voimme käyttää tulosta ikään kuin se olisi tavallinen arvo.


Tehdään nyt jotain hieman hyödyllisempää.


### Viiveen simulointi `await`:lla


Luomme yksinkertaisen `wait`-funktion, joka ottaa argumenttina millisekuntien määrän ja ratkaisee vain tämän määrän millisekuntien jälkeen tekemättä mitään muuta:


```javascript
function wait(ms) {
return new Promise(resolve => {
setTimeout(resolve, ms)
})
}
```


Yritetään käyttää sitä:


```javascript
async function test() {
console.log("waiting 2 seconds...")
await wait(2000)
console.log("done waiting")
}

test()
```


Tämä tulostuu:


```
waiting 2 seconds...
done waiting
```


Voit ajatella, että `await` tarkoittaa "pysähdy tähän, kunnes lupaus on tehty, ja jatka sitten"


Näin voit kirjoittaa koodia **ylhäältä alaspäin** tavalla, joka käyttäytyy asynkronisesti, ilman `.then()`-kutsujen ketjuttamista.


### Odotetaan tietoja


Käyttäkäämme uudelleen edellistä esimerkkiä, jossa kaksinkertaistimme numerot, suodatimme ja laskimme yhteen. Mutta tällä kertaa käytämme `async`/`await`-menetelmää.


Luomme 3 funktiota, jotka simuloivat odottamista ja palauttavat Promises-toimintoja:


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


Kirjoitetaan nyt `async`-funktio niiden yhdistämiseksi:


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


Tämä tulostuu:


```
Final result: 10
```


Tämä on paljon helpompaa lukea kuin `.then()`-ketjujen ketjuttaminen tai takaisinkutsujen yhdistäminen.


Se näyttää tavalliselta vaiheittaiselta ohjelmalta, mutta käyttäytyy silti asynkronisesti.


## Asynkiset Iteraattorit

<chapterId>438b037d-9931-56d7-9052-7b4470f3c75b</chapterId>


Olet jo oppinut **iteraattoreista** ja siitä, miten voimme käyttää `for...of`:ia kiertääksemme matriiseja ja muita iteroitavia asioita.


Mutta entä jos iteroitavien tietojen saapuminen vie aikaa?


Joskus haluamme kiertää asioita, jotka saapuvat **asynkronisesti**, kuten viestejä chatista, rivejä tiedostosta tai numeroita hitaasta lähteestä.


Tätä varten JavaScript antaa meille **async-iteraattorit**.


### Asynkroniset generaattoritoiminnot


Helpoin tapa luoda asynkroninen iteraattori on käyttää **asynkronista generaattorifunktiota**.


Kirjoitamme sen näin:


```javascript
async function* generateNumbers() {
yield 1
yield 2
yield 3
}
```


Tämä näyttää aivan tavalliselta generaattorilta, mutta sen edessä on `async`.


Voimme nyt käyttää `for await...of` -merkkiä arvojen kuluttamiseen:


```javascript
async function run() {
for await (const n of generateNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


Tämä tulostaa:


```
Got number: 1
Got number: 2
Got number: 3
Done!
```


Mitä eroa on tavalliseen generaattoriin?


Erona on se, että voimme nyt käyttää `await`-ominaisuutta generaattorin sisällä.


Tehdään taas viiveapulainen:


```javascript
function wait(ms) {
return new Promise(resolve => setTimeout(resolve, ms))
}
```


Nyt saadaan numerot **hitaasti**:


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


Kokeile käyttää sitä:


```javascript
async function run() {
for await (const n of generateSlowNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


### Miksi käyttää asynkkiä iteraattoreita?


Asynkiset iteraattorit ovat hyödyllisiä, kun:



- Kaikki arvot eivät saavu kerralla.
- Haluat käsitellä niitä yksi kerrallaan, ** sitä mukaa kuin niitä tulee**.
- Työskentelet lupausten kanssa ja haluat tehdä silmukan puhtaasti.


Jos esimerkiksi haluat ladata viestejä chat-palvelimelta yksi kerrallaan tai ladata suuren tiedoston pätkittäin, asynkiset iteraattorit antavat sinulle tavan kirjoittaa `for`-silmukka, joka toimii viivästetyllä datalla.


### `Symbol.asyncIterator`


Voimme käyttää asynkronisia iteraattoreita myös mukautetuissa luokissa.


Tässä on esimerkki, joka tuottaa numeroita viiveellä:


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


Voimme nyt käyttää `for await...of` aivan kuten ennenkin:


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


Näin voit luoda objekteja, joita voidaan iteroida asynkronisesti


## Assignment syntaksisokeri

<chapterId>8b1ba7d8-ecfd-5470-b86e-73cb84ccc8b7</chapterId>


"Syntaksisokerilla" tarkoitetaan jonkin asian kirjoittamista lyhyemmällä tai helpommalla tavalla muuttamatta sen toimintaa. Se on vain kauniimpi tapa sanoa sama asia.


JavaScriptissä on sisäänrakennettuja syntaksisokereita, joiden avulla voimme kirjoittaa puhtaampia ja lyhyempiä deklaraatioita. Tässä luvussa tarkastelemme, miten voit antaa arvoja ehdon perusteella, päivittää muuttujia matematiikan avulla, ottaa arvoja matriiseista tai objekteista ja kopioida tai yhdistää niitä yksinkertaisemmalla syntaksilla.


### Ternaarinen operaattori


JavaScriptissä voit määrittää arvon ehdon perusteella käyttämällä **ternary-operaattoria**, joka on lyhyt tapa kirjoittaa `if...else`.


Tekemisen sijaan:


```javascript
let message

if (isMorning) {
message = "Good morning"
} else {
message = "Hello"
}
```


Voit kirjoittaa:


```javascript
const message = isMorning ? "Good morning" : "Hello"
```


Tämä tarkoittaa:



- Jos `isMorning` on true, käytä `"Good morning"`
- Muussa tapauksessa käytä `"Hello"`


Yleinen muoto on:


```javascript
condition ? valueIfTrue : valueIfFalse
```


Voit käyttää sitä myös muiden lausekkeiden sisällä:


```javascript
console.log(isSunny ? "Go outside" : "Stay in")
```


Varmista vain, että käytät sitä **yksinkertaisiin** päätöksiin. Jos logiikka on monimutkainen, käytä `if...else`.


### Vaihtoehtoiset Assignment-toimijat


JavaScriptissä on **shortcut-operaattoreita**, joiden avulla voidaan tehdä tehtäviä yhdistettynä operaatioihin.


Tarkastellaan normaalia tapaa:


```javascript
let counter = 1
counter = counter + 1
```


Tämä voidaan lyhentää seuraavasti:


```javascript
let counter = 1
counter += 1 // same as counter = counter + 1
```


Tässä ovat yleisimmät:


| Operator | Meaning             |
| -------- | ------------------- |
| `+=`     | add and assign      |
| `-=`     | subtract and assign |
| `*=`     | multiply and assign |
| `/=`     | divide and assign   |

Esimerkkejä:


```javascript
let score = 10
score += 5  // now score is 15
score *= 2  // now score is 30
score -= 10 // now score is 20
```


Nämä ovat hyödyllisiä, kun haluat päivittää muuttujan käyttämällä sen omaa arvoa.


### Rakenneuudistus


**Destrukturoinnin** avulla voit ottaa arvoja matriiseista tai objekteista ja tallentaa ne helposti muuttujiin.


#### Sarjat


Oletetaan, että sinulla on:


```javascript
const colors = ["red", "green", "blue"]
```


Tekemisen sijaan:


```javascript
const first = colors[0]
const second = colors[1]
```


Voit tehdä:


```javascript
const [first, second] = colors
```


Tämä osoittaa:



- `Ensimmäinen` kohteeseen `"punainen"`
- "toinen" kohtaan "Green"


Voit myös ohittaa arvoja:


```javascript
const [,, third] = colors
console.log(third) // blue
```


#### Esineet


Voit myös poimia arvoja objekteista:


```javascript
const user = { name: "Alice", age: 30 }

const { name, age } = user
console.log(name) // Alice
console.log(age)  // 30
```


Jos ominaisuudella on eri nimi kuin haluamallasi muuttujalla, voit nimetä sen uudelleen:


```javascript
const { name: username } = user
console.log(username) // Alice
```


Strukturointi tekee koodistasi siistimpää, kun työskentelet objektien ja matriisien kanssa.


### Levitä syntaksi


**spread-syntaksi** käyttää `...` arvojen purkamiseen tai kopioimiseen.


#### Sarjat


Voit kopioida tai yhdistää matriiseja:


```javascript
const a = [1, 2]
const b = [3, 4]

const both = [...a, ...b]
console.log(both) // [1, 2, 3, 4]
```


Voit myös kloonata joukon:


```javascript
const original = [10, 20, 30]
const clone = [...original]
```


#### Esineet


Voit tehdä saman esineiden kanssa:


```javascript
const a = { x: 1 }
const b = { y: 2 }

const merged = { ...a, ...b }
console.log(merged) // { x: 1, y: 2 }
```


Voit myös ohittaa arvot:


```javascript
const user = { name: "Alice", age: 30 }
const updated = { ...user, age: 31 }

console.log(updated) // { name: "Alice", age: 31 }
```


Tämä on erittäin hyödyllistä, kun kohteita päivitetään muuttamatta alkuperäistä.


# NodeJS

<partId>42fe4d49-dace-5135-bb9e-b9d75034fb2a</partId>


## Miten pääsimme Nodeen

<chapterId>0da1d60c-06c9-54e6-a181-ae7dabf6e3b8</chapterId>


Tässä luvussa opimme hieman historiallista taustaa JavaScriptistä ja NodeJS:stä.


Historiallinen konteksti on hyvin tärkeä ohjelmistojen alalla, koska käytämme usein muiden ihmisten rakentamia työkaluja, ja siksi heidän aiemmin tekemänsä päätökset vaikuttavat meihin.


Jos ymmärrämme näiden päätösten syyn ja sen, miten käyttämämme työkalut ovat tulleet sellaisiksi kuin ne ovat, voimme olla hieman vähemmän hämmentyneitä siitä, mitä teemme.


### JavaScriptin alkuperä


JavaScript aloitti yksinkertaisena kielenä, jonka tarkoituksena oli tehdä verkkosivuista vuorovaikutteisia.


1990-luvulla Netscape Navigatorin kaltaiset verkkoselaimet lisäsivät JavaScriptin, jotta kehittäjät voisivat kirjoittaa koodia, joka toimii suoraan selaimessa.


Alkuperäisenä ajatuksena oli, että Java olisi verkkosivujen tekemisen ydinkieli (niin sanottujen "Java-sovelmien" avulla), ja JavaScript vain pienempiä asioita varten.


Ydinsuunnittelun teki Brendan Eich, joka tuolloin työskenteli Netscapessa, alle kahdessa viikossa.


Useimmat ihmiset käyttivät kuitenkin mieluummin Java- kuin JavaScriptia, ja Java-sovelmien tietoturvaongelmiin liittyi tuolloin myös ongelmia, joten lopulta Java poistettiin vaihtoehdosta ja JavaScriptistä tuli web-kehityksen de facto-standardi.


### V8-moottori


JavaScript on tulkattu kieli, toisin kuin C:n kaltaiset käännetyt kielet.


Käännetyllä kielellä kirjoitettu koodi muutetaan binääriksi, ja binääri syötetään suoraan tietokoneen suorittimelle.


![](assets/en/6.webp)


Interpred-kielet taas ovat yleensä käyttäjäystävällisempiä ja lähempänä ihmisten ajattelua ("korkean tason") kuin koneiden toimintaa ("matalan tason"), joten niihin on yleensä rakennettu virtuaalikone niiden koodin suorittamista varten.


Virtuaalikone on erityinen ohjelma, joka on kirjoittamasi koodin ja suorittimen välissä ja suorittaa koodisi (koska suoritin ei ymmärrä sitä).


Tämän ansiosta voit ohjelmoida tietämättä liikaa taustalla olevasta koneesta, mutta sillä on myös suorituskykyä heikentävä vaikutus, koska tietokone ei suorita vain sinun ohjelmaasi, vaan se suorittaa ohjelmaa (virtuaalikonetta), joka suorittaa sinun ohjelmasi.


Kun verkkosovelluksista tuli yhä monimutkaisempia, JavaScriptin suorituskykyä haluttiin parantaa. V8-moottori on Google Chromen JavaScript-tulkki. Se kehitettiin Googlessa ja julkaistiin vuonna 2008.


Vanhemmat JavaScript-moottorit olivat enimmäkseen perinteisiä virtuaalikoneita, mutta V8-moottori on JIT-kääntäjä (just-in-time).


JavaScript-koodi syötetään V8-moottorille, ja moottori yrittää kääntää osia siitä natiiviksi binäärikoodiksi lennossa. Näin saat korkean tason kielen kokemuksen, mutta suorituskyky on hieman lähempänä matalan tason kieliä. Tämä on tehnyt JavaScriptistä maailman nopeimman korkean tason kielen, mikä on vähän kuin "molempien maailmojen parhaat puolet".


### NodeJS-runtime


Vaikka JavaScript oli helppokäyttöinen ja melko nopea toteuttaa, V8:n julkaisun jälkeen sillä oli valtava rajoitus: se pystyi toimimaan vain selaimen sisällä.


Miksi se on ongelma?


Koska selaimet suorittavat koodia, joka on haettu miljoonista eri lähteistä internetistä, ne voivat helposti joutua haittaohjelmiksi, joten ne on "hiekkalaatikoitu" muusta käyttöjärjestelmästä.


![](assets/en/7.webp)


JavaScriptillä ei voinut käyttää tietokoneen tiedostojärjestelmää ja muita paikallisia resursseja (ainakaan niin helposti kuin muilla kielillä), joten se rajoitti merkittävästi sitä, millaisia sovelluksia sillä pystyi rakentamaan.


Vuonna 2009 Ryan Dahl julkaisi NodeJS:n, joka on ajoaika, jonka avulla voit käyttää V8-moottoria selaimen ulkopuolella, suoraan tietokoneen natiivissa käyttöjärjestelmässä. Se lisää myös monia ominaisuuksia, jotka ovat hyödyllisiä palvelinpuolen ja komentorivin ohjelmien kirjoittamisessa. NodeJS:n avulla voit esimerkiksi luoda verkkopalvelimen, lukea ja kirjoittaa tiedostoja tai rakentaa työkaluja, jotka automatisoivat tehtäviä.


![](assets/en/8.webp)


Tällä kurssilla olemme tähän mennessä tutustuneet JavaScript-ominaisuuksiin, joita on sekä selaimessa että NodeJS:ssä. Näiden ominaisuuksien avulla olemme voineet määritellä tietoja ja käsitellä niitä abstrakteilla tavoilla. Seuraavilla oppitunneilla tutustumme ominaisuuksiin, jotka ovat NodeJS:lle ominaisia ja joiden avulla voimme olla vuorovaikutuksessa käyttöjärjestelmän kanssa.


## Komentorivin argumentit

<chapterId>960d20f3-c424-5d51-a041-ef17d2e94b6d</chapterId>


NodeJS mahdollistaa muun muassa CLI:n (Command Line Interfaces) rakentamisen.


Sitä varten tarvitsemme tavan ottaa vastaan komentoriviargumentteja, mikä Nodessa tapahtuu sisäänrakennetun `process`-olion avulla.


### `prosessi`


NodeJS tarjoaa erityisen objektin nimeltä `process`, joka edustaa käynnissä olevaa ohjelmaa.


Sen avulla voit tutkia ympäristöä, nykyistä työhakemistoa ja jopa lopettaa ohjelman tarvittaessa.


Esimerkiksi:


```javascript
console.log(process.platform)
```


Tämä tulostaa käyttöjärjestelmän alustan, kuten `win32`, `linux` tai `darwin` (Mac).


### `process.argv`


Kun suoritat NodeJS-ohjelmaa terminaalista, voit antaa komentosarjan nimen perään ylimääräisiä sanoja (argumentteja). Nämä tallennetaan `process.argv`-tiedostoon.


Jos esimerkiksi suoritat tämän komennon:


```
node my_script.js alpha beta
```


Voit tulostaa argumentit näin:


```javascript
console.log(process.argv)
```


Tulos voi näyttää tältä:


```
[ '/path/to/node', '/path/to/my_script.js', 'alpha', 'beta' ]
```


Kaksi ensimmäistä kohtaa ovat aina solmupolku ja skriptipolku. Tämän jälkeen tulevat kaikki komentosarjalle antamasi lisäsanat.


`process.argv`-joukko voidaan leikata kuten mikä tahansa muu joukko käyttämällä `.slice()`-metodia, joten saadaksesi vain välitetyt argumentit voit tehdä seuraavasti


```javascript
const args = process.argv.slice(2)

console.log(args)
```


Käyttäjän välittämien argumenttien hallinta on olennaisen tärkeää komentorivisovellusten kehittämisessä.


## Moduulit

<chapterId>4e1651a5-65fd-50bc-b22a-40313d5659ca</chapterId>


NodeJS:n kaltaiset JavaScript-ajoympäristöt käsittelevät yleensä jokaista JavaScript-tiedostoa erillisenä moduulina.


Ajattele moduulia laatikkona. Laatikolla on oma yksityinen tilansa, joten siinä ilmoittamasi muuttujat ja funktiot eivät häiritse muissa laatikoissa olevaa koodia. Periaatteessa jokaisella moduulilla on oma scope.


Moduuli voi viedä osan sisällöstään, jolloin se on muiden moduulien käytettävissä, ja se voi tuoda muiden moduulien viemää sisältöä. JavaScriptin avulla voit viedä ja tuoda sisältöä moduulien välillä ja yhdistää eri tiedostoja.


JavaScript-ohjelma koostuu usein useista moduuleista, jotka ovat yhteydessä toisiinsa.


Miksi käyttää moduuleja? Jakamalla koodisi moduuleihin voit järjestää ohjelmasi pienempiin, selkeämpiin ja uudelleenkäytettäviin osiin. Kukin moduuli voi keskittyä vain yhdenlaiseen tehtävään, kuten matemaattisten laskutoimitusten käsittelyyn, tiedostojen käsittelyyn tai tekstin muotoiluun.


### CommonJS-moduulit


NodeJS:ssä yleisin järjestelmä moduulien hallintaan on nimeltään **CommonJS**.


Tässä järjestelmässä voit jakaa (viedä) koodia moduulista käyttäen `module.exports` ja ladata (tuoda) sen toiseen tiedostoon käyttäen `require()`.


Jos haluat tehdä jonkin asian saataville moduulin ulkopuolella, määritä se moduuliin `module.exports`:


```javascript
const greeting = "Hello!"

module.exports = greeting
```


Tässä moduuli vie merkkijonon `"Hello!".


Jos haluat käyttää toisesta tiedostosta vietyjä koodeja, käytä `require()`-funktiota ja tiedoston polkua:


```javascript
const greeting = require("./greeting.js")

console.log(greeting)
```


Tämä tulostuu:


```
Hello!
```


Voit viedä useita asioita niputtamalla ne yhteen anonyymiin objektiin, kuten esim


```javascript
const greeting1 = "hello"

const greeting2 = "hi"

module.exports = {
greeting1, greeting2
}
```


CommonJS oli moduulijärjestelmä, jonka NodeJS alun perin otti käyttöön. Myöhemmin järjestelmään lisättiin myös ES-moduulit.


### ES-moduulit


NodeJS tukee myös toisenlaista moduulityyppiä nimeltä **ES-moduulit**, jotka ovat suosittuja web-kehityksessä. Ne käyttävät avainsanoja `export` ja `import`.


ES-moduulit kehitettiin selainta varten ja lisättiin vasta myöhemmin Nodeen. Jos haluat käyttää niitä, saatat joutua käyttämään tiedostopäätteenä `.mjs` tiedostoa `.js` sijasta, riippuen siitä, mitä Node-versiota käytät.


Eräässä tiedostossa nimeltä `greeting.mjs` kirjoitamme seuraavasti


```javascript
export const greeting = "Hello!"
```

Kuten näet, viemme vakion suoraan sinne, missä se on määritelty


Tuomme sen toiseen tiedostoon nimeltä `index.mjs`:


```javascript
import { greeting } from "./greeting.mjs"

console.log(greeting)
```


Voit viedä erilaisia ilmoituksia tiedoston eri osiin, kuten esimerkiksi seuraavasti


```javascript
export const num = 10

export function double (x) {
return x*2
}
```


### NodeJS:n standardikirjasto


NodeJS sisältää myös monia sisäänrakennettuja moduuleja. Nämä ovat NodeJS:n tarjoamia valmiita moduuleja, jotka auttavat yleisissä tehtävissä, kuten tiedostojen lukemisessa, käyttöjärjestelmän kanssa työskentelyssä tai verkkoon liittymisessä.


Esimerkiksi `os`-moduuli antaa tietoja käyttöjärjestelmästäsi:


```javascript
const os = require("os")

console.log(os.platform())
```


Sinun ei tarvitse asentaa näitä sisäänrakennettuja moduuleja, ne tulevat NodeJS:n mukana. Ne muodostavat ajoajan "standardikirjaston", ja useimmat Node-sovellukset käyttävät niitä esimerkiksi tiedostojen lukemiseen tai yhteydenpitoon internetin kautta.


Seuraavissa luvuissa esitellään joitakin hyödyllisiä esimerkkejä niiden käytöstä.


## `fs`-moduuli

<chapterId>911e953a-35ae-5ee7-bd74-372501c32e81</chapterId>


`fs`-moduuli (lyhenne sanoista **tiedostojärjestelmä**) on osa NodeJS:n standardikirjastoa. Sen avulla voit työskennellä tietokoneen tiedostojen ja hakemistojen kanssa: voit lukea tiedostoja, kirjoittaa tiedostoja, poistaa niitä, nimetä niitä uudelleen ja paljon muuta.


Jos haluat käyttää sitä, sinun on ensin tuotava se tiedostosi alkuun:


```javascript
const fs = require("fs")
```


### Synkronointi API


Yksinkertaisin tapa käyttää `fs`:ää on sen **sync**-metodit.


Nämä metodit estävät ohjelman, kunnes ne on suoritettu loppuun (joten seuraava koodirivi ei suoritu, ennen kuin operaatio on suoritettu loppuun).


Tässä on esimerkki tiedoston lukemisesta synkronisesti:


```javascript
const fs = require("fs")

const data = fs.readFileSync("example.txt", "utf8")

console.log(data)
```


Jos samassa hakemistossa kuin skriptisi on tiedosto nimeltä `example.txt`, tämä tulostaa sen sisällön.


Voit kirjoittaa tiedostoon myös synkronisesti:


```javascript
const fs = require("fs")

fs.writeFileSync("output.txt", "Hello from Node!")

console.log("File written!")
```


Tämä luo (tai korvaa) tiedoston nimeltä `output.txt` tekstillä.


Seuraavassa on joitakin yleisiä toimintoja, joita voit tehdä tämän API:n avulla:


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


Sync API on yksinkertainen ja hyvä pienille skripteille, mutta koska se estää ohjelman, kunnes se on valmis, se voi hidastaa toimintaa, jos työskentelet suurten tiedostojen tai palvelimen kanssa.


### Asynkroninen takaisinsoitto API


**callback-API** ei ole lukkiutuva: sen avulla NodeJS voi jatkaa muiden asioiden tekemistä tiedosto-operaation aikana.


Sen sijaan, että se palauttaisi tuloksen suoraan, se ottaa toiminnon (**callback**), jota kutsutaan, kun operaatio on suoritettu.


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


Näin tapahtuu:



- `fs.readFile` alkaa lukea `example.txt`.
- NodeJS ei odota, vaan siirtyy suorittamaan muuta kirjoittamaasi koodia.
- Kun tiedoston lukeminen on päättynyt, takaisinkutsu suoritetaan:



  - Jos tapahtui virhe, `err` sisältää virheen.
  - Muussa tapauksessa `data` sisältää sisällön.


Näin kirjoitat tiedostoon:


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


Sama ajatus: ohjelma ei pysähdy tiedoston kirjoittamisen aikana.


Joitakin esimerkkejä asioista, joita voit tehdä tämän API:n avulla:


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


Takaisinkutsu-API on parempi palvelimille ja suurille tehtäville, koska se ei estä ohjelman toimintaa, mutta sisäkkäiset takaisinkutsut voivat olla sotkuisia, jos ketjutat monia toimintoja. Siksi lisättiin lupauksiin perustuva asynkroninen API.


### Promise async API


Promise-pohjainen sovellusliittymä on nykyaikainen ja toimii erinomaisesti `.then()` ja `async/await` -ohjelmien kanssa. Se on saatavilla nimellä `fs.promises`.


Sinun on tuotava `promises`-ominaisuus:


```javascript
const fs = require("fs").promises
```


Käyttämällä `.then()`:


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


Tai vielä parempi, käyttämällä `async/await`:


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


Kirjoittaminen tiedostoon:


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


Tavallinen luettelo API:n esimerkeistä:


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


Kun kirjoitat koodia, joudut usein käyttämään muiden kirjoittamaa koodia, esimerkiksi kirjastoja, jotka auttavat sinua työskentelemään päivämäärien, värien, palvelimien tai lähes minkä tahansa muun kanssa.


Sen sijaan, että lataat ja kopioit tiedostoja manuaalisesti, voit käyttää **paketinhallintaohjelmaa**.


Paketinhallinta on työkalu, joka:



- lataa paketteja
- pitää kirjaa siitä, mitä paketteja projektisi tarvitsee
- varmistaa, että kaikilla tiimissäsi on samat versiot paketeista


### Mikä on NPM


NodeJS-maailmassa suosituin paketinhallinta on **NPM**, joka tarkoittaa *Node Package Manager*.


Saat NPM:n automaattisesti, kun asennat NodeJS:n.


Voit tarkistaa, onko sinulla NPM, suorittamalla tämän terminaalissa:


```
npm -v
```


Tämä tulostaa käytössäsi olevan NPM:n version, esimerkiksi:


```
10.2.1
```


### Paketin luominen


NodeJS:ssä **paketti** on vain hakemisto, jossa on `package.json`-tiedosto.


Luodaan sellainen askel askeleelta.


1. Tee uusi kansio projektillesi:


```
mkdir my_project
cd my_project
```


2. Suorita tämä komento:


```
npm init
```


Tämä käynnistää vuorovaikutteisen asennuksen, jossa kysytään kysymyksiä, kuten projektin nimi, versio, kuvaus jne.


Jos et halua vastata kaikkeen ja haluat vain hyväksyä oletusasetukset, voit käyttää:


```
npm init -y
```


Kun olet ajanut sen, näet kansiossasi uuden tiedoston nimeltä:


```
package.json
```


### `package.json`


Package.json-tiedosto on vain JSON-tiedosto, joka tallentaa metatietoja projektistasi.


Tässä on esimerkki:


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


Muutamia tärkeitä aloja:



- `name`: paketin nimi
- `version`: nykyinen versio
- `main`: aloituskohdan tiedosto (kuten `index.js`)
- `scripts`: komennot, jotka voit suorittaa (kuten `npm start`)
- `dependencies`: listaa kaikki paketit, joista projektisi on riippuvainen


### Paketin asentaminen


Oletetaan, että haluat käyttää tiettyä pakettia nimeltä `picocolors` lisätäksesi värejä terminaalin tulosteeseen.


Voit asentaa sen suorittamalla:


```
npm install picocolors
```


Voit nyt käyttää sitä projektissasi. Tee tiedosto `index.js`, jossa on komentoarvo


```javascript
const pico = require('picocolors')

console.log(
pico.green("This text is green!")
)
```


ja yritä ajaa se. Terminaalin pitäisi tulostaa värillinen versio tekstistä.


Mitä NPM teki?



- Se latasi paketin ja talletti sen alikansioon nimeltä `node_modules/`
- se lisäsi merkinnän `dependencies` kohtaan `package.json`
- se päivitti tiedoston `package-lock.json`


Mikä on `package-lock.json` ?


### `package-lock.json`


NPM luo tämän tiedoston automaattisesti.


Saatat ihmetellä, että jos meillä on jo `package.json`, miksi tarvitsemme toisen tiedoston?

Tässä on syy:



- `package.json` kertoo vain, minkä version **alueen** paketin projekti tarvitsee.

Esimerkki:


```json
"dependencies": {
"picocolors": "^1.1.0"
}
```


`^1.1.0` tarkoittaa "mitä tahansa versiota, joka on yhteensopiva 1.1.x:n kanssa", joten se on joustava.



- `package-lock.json` **jäädyttää** jokaisen yksittäisen paketin ja niiden aliriippuvuuksien tarkat versiot, jotta jokainen, joka asentaa projektisi, saa täsmälleen samat toimivat asetukset.


Miksi tämä on tärkeää?


Jos työskentelet tiimissä, otat projektin käyttöön palvelimella tai palaat siihen tulevaisuudessa, haluat varmistaa, että se toimii edelleen samalla tavalla.

Jos paketteja on päivitetty ja asennat ne uudelleen ilman lukitustiedostoa, saatat saada hieman erilaisen version, joka käyttäytyy eri tavalla.


Pitämällä `package-lock.json`-tiedoston projektissasi NPM asentaa aina täsmälleen samat versiot, jotka on lueteltu siinä, varmistaen, että kaikilla on sama ympäristö.


`package-lock.json` lukitsee kaiken tiettyyn versioon, jotta projekti olisi helpommin toistettavissa muilla koneilla.


Mutta jos pakettisi on monien ihmisten käytössä, voit sen sijaan jättää sen toimittamatta, jotta NPM löytää vain `package.json`-tiedoston ja saa asentaa automaattisesti viimeisimmät versiot, jotka on sallittu kyseisessä tiedostossa.


Mutta näistä asioista kannattaa huolehtia myöhemmin, kun alat julkaista omaa koodiasi. Toistaiseksi esittelimme NPM:n perusteet vain siksi, että voit löytää ja käyttää muiden kehittäjien julkaisemia kirjastoja projekteissasi.



## Verkottuminen NodeJS:ssä

<chapterId>f2cabd8b-754b-5c97-8d6a-8412a9a184c7</chapterId>


NodeJS:ää käytetään usein backend-kielenä: voit tehdä skriptistäsi palvelimen ja käyttää sitä myös pyyntöjen tekemiseen muille palvelimille.


Tässä luvussa esittelemme joitakin perusverkko-ominaisuuksia, joiden avulla voit tehdä sen.


### `fetch()`


Jos haluat ohjelmasi lataavan tietoja verkkosivustolta tai API:sta, sinun on tehtävä **HTTP-pyyntö**.


NodeJS:n nykyaikaisissa versioissa voit käyttää sisäänrakennettua `fetch()`-funktiota.


Tässä on esimerkki GET-pyynnön tekemisestä API:lle:


```javascript
const response = await fetch("https://jsonplaceholder.typicode.com/posts/1")
const data = await response.text()

console.log(data)
```


Kun suoritat tämän, näet jotain seuraavanlaista:


```
{
"userId": 1,
"id": 1,
"title": "...",
"body": "..."
}
```


Näin tapahtuu:


1. `fetch()` ottaa URL-osoitteen ja tekee pyynnön.

2. Se palauttaa **Promise**-olion, joka vastaa `Response`-oliota.

3. `response.text()` lukee vastausrungon merkkijonona.


Takaisin saamasi merkkijono on kuitenkin itse asiassa JSON. Mitä se on?


### JSON


Kun työskentelet web-rajapintojen kanssa, tiedot lähetetään ja vastaanotetaan usein **JSON**-muodossa, joka tarkoittaa JavaScript Object Notation -nimitystä.


JSON on vain tekstiformaatti, joka muistuttaa paljon JavaScript-objekteja. Esimerkiksi:


```json
{
"name": "Alice",
"age": 30,
"likes": ["apples", "bananas"]
}
```


`JSON`-objekti on JavaScriptin sisäänrakennettu apuohjelma, jota voidaan käyttää tämän tietomuodon kanssa työskentelyyn.


Voit muuntaa JavaScript-olion JSON-merkkijonoksi käyttämällä `JSON.stringify()`:


```javascript
const user = { name: "Alice", age: 30 }

const jsonString = JSON.stringify(user)

console.log(jsonString)
```


Tämä tulostuu:


```
{"name":"Alice","age":30}
```


Voit myös muuntaa JSON-tekstin takaisin JavaScript-olioksi käyttämällä `JSON.parse()`:


```javascript
const jsonText = '{"name":"Bob","age":25}'

const obj = JSON.parse(jsonText)

console.log(obj)
```


Tämä tulostuu:


```
{ name: 'Bob', age: 25 }
```


Ole varovainen: `JSON.parse()` heittää virheen, jos merkkijono ei ole kelvollinen JSON.


```javascript
JSON.parse("not json") // ❌ Error!
```


Varmista siis, että merkkijono on muotoiltu oikein.


### `http`-palvelin


NodeJS:n avulla voit luoda verkkopalvelimen asentamatta mitään muuta.


Voit käyttää sisäänrakennettua `http`-moduulia käsittelemään asiakkaiden pyyntöjä ja lähettämään vastauksia.


Tässä on hyvin yksinkertainen esimerkki:


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


Kun suoritat tämän komentosarjan ja avaat selaimessasi `http://localhost:3000`, näet:


```
Hello from NodeJS server!
```


Koodissa tapahtuu näin:


1. Olet tuonut `http`-palvelimen Noden standardikirjastosta.

2. `http.createServer()` luo palvelimen. Annoit `http.createServer()`:lle takaisinkutsun `(req, res) => {...}`, joka suoritetaan joka kerta, kun joku muodostaa yhteyden.

3. Annoit vastaukselle tilakoodin 200 (joka osoittaa, että toiminto onnistui). Voit lukea http-tilakoodeista [täältä](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

3. `res.end()` lähettää vastauksen ja päättää yhteyden.

4. `server.listen(3000)` käynnistää palvelimen portissa 3000.


Voit myös tarkistaa pyynnön `req.url` ja `req.method`, jos haluat käsitellä eri polkuja tai pyyntöjen tyyppejä.


Esimerkki reitityksestä:


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


Nämä ovat hyvin yksinkertaisia esimerkkejä. Kehittyneempien palvelimien rakentamiseen useimmat kehittäjät todennäköisesti lataavat valmiin backend-kirjaston, kuten [express](https://www.npmjs.com/package/express).


## Tietojen käsittely: puskurit, tapahtumat, virrat

<chapterId>8c9623f0-a604-51a4-8fe4-871c849d3e3b</chapterId>


Tässä luvussa esitellään pääasiassa kolme objektiluokkaa:



- `Buffer`, joka edustaa pieniä binääridatan kappaleita
- `EventEmitter`, jota voidaan käyttää asynkronisen prosessin seuraamiseen lähettämällä signaaleja, joita kutsutaan "tapahtumiksi"
- `Stream`, jonka avulla voimme käsitellä suuria datamääriä yksi `Buffer` kerrallaan ja joka seuraa prosessia lähettämällä tapahtumia


Nämä ovat erittäin yleisiä ammattimaisessa NodeJS-koodissa, joten vaikka et ehkä käyttäisikään niitä ensimmäisissä projekteissasi, on hyvä hankkia perusymmärrys siitä, milloin joudut olemaan vuorovaikutuksessa niiden kanssa. niistä


### Puskurit


NodeJS:ssä **puskuri** on objektityyppi, jota käytetään binääridatan käsittelyyn.


Voit ajatella puskuria kiinteän kokoisena säiliönä raaoille tavuille.


Näin luot puskurin merkkijonosta:


```javascript
const buf = Buffer.from("hello")
console.log(buf)
```


Tämä tulostaa jotakin seuraavanlaista:


```
<Buffer 68 65 6c 6c 6f>
```


Nämä numerot (`68`, `65`, `6c` jne.) ovat heksadesimaalisia esityksiä kirjaimista sanassa `"hello"`.


Voit muuntaa sen takaisin merkkijonoksi näin:


```javascript
console.log(buf.toString())
```


Tämä tulostuu:


```
hello
```


Voit myös luoda tietyn kokoisen puskurin, joka on täynnä nollia:


```javascript
const buf = Buffer.alloc(10)
console.log(buf)
```


Tämä tulostaa jotakin seuraavanlaista:


```
<Buffer 00 00 00 00 00 00 00 00 00 00>
```


Voit kirjoittaa puskuriin:


```javascript
buf.write("abc")
console.log(buf)
```


Ja voit käyttää yksittäisiä tavuja:


```javascript
console.log(buf[0]) // prints the ASCII number for 'a', which is 97
```


Puskurit ovat erityisen hyödyllisiä silloin, kun tietoja on käsiteltävä hyvin matalalla tasolla.


### Tapahtumat


JavaScriptissä **tapahtuma** on jotain, joka tapahtuu ohjelmassasi ja johon voit reagoida.


Esimerkiksi:



- tiedoston lataaminen päättyy
- ajastin käynnistyy
- käyttäjä napsauttaa painiketta
- verkkopyyntö palauttaa tietoja


**Tapahtuma** on vain signaali siitä, että jotain on tapahtunut, ja voit kirjoittaa koodia, joka kuuntelee näitä tapahtumia ja reagoi niihin.


NodeJS:ssä monet objektit voivat lähettää tapahtumia. Näitä objekteja kutsutaan nimellä **EventEmitters**.


Tässä on esimerkki:


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


Tämä tulostuu:


```
Hello! An event happened.
```


Tässä on mitä:


1. Luomme `EventEmitter`-olion.

2. Käskemme sitä suorittamaan takaisinkutsun aina kun `"greet"-tapahtuma tapahtuu, käyttämällä `.on("greet")`.

3. Myöhemmin käynnistämme `"greet"-tapahtuman käyttämällä `.emit()`.

4. Meidän takaisinkutsumme suoritetaan


Voit siirtää tietoja tapahtuman mukana:


```javascript
emitter.on("greet",
(name) => console.log(`Hello, ${name}!`)
)

emitter.emit("greet", "Alice") // first argument is the type of event, second argument is the data we pass with this event
```


Tämä tulostuu:


```
Hello, Alice!
```


Voit rekisteröidä kuuntelijoita myös muita tapahtumia varten:


```javascript
emitter.on("goodbye", () => {
console.log("Goodbye!")
})

emitter.emit("goodbye")
```


Voit liittää tapahtumatyyppiin niin monta kuuntelijaa kuin haluat, ja voit laukaista useita erityyppisiä tapahtumia samasta emitteristä.


Monet NodeJS:n objektit lähettävät tapahtumia kertoakseen muulle ohjelmalle, että jotain tapahtuu.



### Mitä purot ovat?


Virrat yhdistävät puskureita ja tapahtumia auttaakseen meitä käsittelemään tietoja.


Kun työskentelemme tiedostojen, verkkotietojen tai jopa pitkän tekstin kanssa, emme aina tarvitse (tai halua) ladata kaikkea kerralla muistiin. Se voi olla hidasta tai jopa kaataa ohjelman, jos tiedot ovat liian suuria.


Sen sijaan voimme käsitellä dataa **pikku hiljaa**, sitä mukaa kun sitä saapuu tai sitä luetaan, ikään kuin joisimme vettä pillin läpi sen sijaan, että yrittäisimme juoda koko lasin kerralla. Tätä kutsutaan **virraksi**.


NodeJS:ssä stream on objekti, jonka avulla voit lukea dataa lähteestä tai kirjoittaa dataa määränpäähän **yksi kappale kerrallaan**.


NodeJS:ssä on neljä päätyyppiä virtoja:



- Readable**: virrat, joista voit lukea dataa (kuten tiedoston lukeminen)
- Writable**: virrat, joihin voit kirjoittaa dataa (kuten tiedostoon)
- Duplex**: virrat, jotka ovat sekä luettavissa että kirjoitettavissa
- Transform**: kuten duplex-virrat, mutta ne voivat muuttaa (transformoida) dataa sen kulkiessa


### Luettavat virrat


Oletetaan, että sinulla on tiedosto `bigfile.txt` käsiteltävänä. Voit luoda luettavan virran `fs`-moduulilla lukeaksesi tiedoston pala palalta.


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


Mitä täällä tapahtuu?


1. `fs.createReadStream()` luo luettavan virran.

2. Aina kun tiedoston osa on valmis, stream lähettää `data`-tapahtuman ja antaa meille datan "palan" (`Buffer`). Me tulostamme palan.

3. Kun koko tiedosto on luettu, käynnistetään tapahtuma `end`.

4. Jos tapahtuu virhe (esimerkiksi tiedostoa ei ole olemassa), käynnistyy `error`-tapahtuma.


Näin voit lukea jättimäisiä tiedostoja lataamatta niitä kaikkia kerralla muistiin.


Jos haluamme tietojen saapuvan ihmiselle luettavassa muodossa (binäärimuodon sijaan), voimme määrittää virran koodauksen:


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


Koodi tulostaa nyt tiedoston ihmisen luettavassa muodossa.


### Kirjoitettavat virrat


Kirjoitettavan virran avulla voit lähettää dataa jonnekin pala palalta.


Tässä on esimerkki kirjoittamisesta `target.txt`-tiedostoon streamia käyttäen:


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


Näin tapahtuu:


1. `fs.createWriteStream()` luo kirjoitettavan virran.

2. Kirjoitamme siihen tekstiä käyttämällä `.write()`.

3. Kun olemme valmiit, kutsumme `.end()` sulkeaksemme virran.

4. Kun kaikki tiedot on kirjoitettu, lähetetään tapahtuma "finish".

5. Jos jokin menee pieleen, käynnistyy `error`-tapahtuma.


Samoin kuin luettavissa olevat, myös kirjoitettavissa olevat virrat ovat hyviä suurille tietomäärille, koska niiden ei tarvitse pitää kaikkea kerralla muistissa.


### Putkistovirrat


Yksi streamien hienoimmista puolista on, että voit **putkea** ne yhteen: yhdistää luettavan streamin suoraan kirjoitettavaan streamiin.


```javascript
const fs = require("fs")

const readable = fs.createReadStream("bigfile.txt")
const writable = fs.createWriteStream("target.txt")

readable.pipe(writable)
```


Tässä:



- Luettava virta lukee tiedostosta `bigfile.txt`.
- Kirjoitettava virta kirjoittaa tiedostoon `copy.txt`.
- `.pipe()` lähettää datan suoraan luettavasta virrasta kirjoitettavaan virtaan.


### Duplex-virrat


Dupleksivirta on sekä luettavissa että kirjoitettavissa. Yksi esimerkki on verkon pistorasia: voit lähettää siihen dataa ja vastaanottaa siitä dataa.


Tässä on hyvin yksinkertainen esimerkki, jossa käytetään `net`-moduulia:


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


Tässä esimerkissä:



- `socket`-objekti on duplex-virta.
- Voit `kirjoittaa()` siihen ja myös kuunnella `data`-tapahtumia siitä.


### Muunna virrat


Muunnosvirta on kaksisuuntainen virta, joka myös muuttaa sen läpi kulkevaa dataa.


Voit esimerkiksi käyttää sisäänrakennettua `zlib`-moduulia tietojen pakkaamiseen tai purkamiseen.


Näin pakataan tiedosto muunnosvirran avulla:


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


Ja purkaa se takaisin:


```javascript
const readable = fs.createReadStream("bigfile.txt.gz")
const unzip = zlib.createGunzip()
const writable = fs.createWriteStream("bigfile.txt")

readable.pipe(unzip).pipe(writable)

writable.on("finish", () => {
console.log("File decompressed.")
})
```


Muunnosvirrat ovat erittäin hyödyllisiä tehtävissä, kuten pakkaamisessa, salaamisessa tai tiedostomuotojen muuttamisessa suoratoiston aikana.


### Vastapaine


Joskus kirjoitettava virta on hidas tietojen käsittelyssä. Jos siirrämme dataa kirjoitettavaan virtaan nopeammin kuin se pystyy käsittelemään, saatamme joutua ongelmiin. Tätä kutsutaan **takapaineeksi**.


Jos kutsut `.write()`-metodia kirjoitettavalle virralle, se palauttaa boolean-arvon, joka kertoo, tarvitseeko virta tauon; sinun on ehkä tarkistettava sen palautusarvo, kuten tässä:


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


Tämä oli havainnollistava esimerkki tietojen manuaalisesta siirtämisestä luettavasta laitteesta kirjoitettavaan laitteeseen ja vastapaineen hallinnasta manuaalisesti.


Tavallisesti putkitamme datan käyttämällä `.pipe()`-metodia, joka käsittelee vastapaineen automaattisesti.


Sinun tarvitsee siis huolehtia vastapaineesta vain silloin, kun jostain syystä kutsut manuaalisesti `.write()`.


## Loppuhuomautus

<chapterId>139e2ab8-df67-525a-85f0-5a2fa5e478f2</chapterId>


Siinä kaikki, jos olet seurannut oppitunteja, sinun pitäisi nyt pystyä kirjoittamaan yksinkertaisia ohjelmia NodeJS:ssä.


Suosittelen tekemään juuri niin: kun olet oppinut perusteet, muutaman henkilökohtaisen projektin rakentaminen on paras tapa harjoitella ja kehittyä paremmaksi ohjelmoijaksi.


Sillä ei ole väliä, mitä rakennat, vaan sillä, että haastat itsesi ratkaisemaan ongelmia koodin avulla.


Nykyaikaiset ohjelmointikielet ovat uskomattoman tehokkaita, ja NodeJS on luultavasti paras työkalupakki, jota voit kokeilla matkasi tässä vaiheessa.


Onnea!


# Viimeinen osa


<partId>322624d8-6fbc-11f0-a67a-5b145f10afc1</partId>


## Arvostelut & arvostelut


<chapterId>3e93ac86-6fbc-11f0-8bae-9b2ed7914843</chapterId>

<isCourseReview>true</isCourseReview>

## Päätelmä


<chapterId>49b3b9b2-6fbc-11f0-9870-5f5adcd3a0eb</chapterId>


<isCourseConclusion>true</isCourseConclusion>