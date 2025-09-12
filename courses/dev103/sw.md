---
name: JavaScript na NodeJS Msingi
goal: Jifunze misingi ya programu ya JavaScript na uundaji wa NodeJS ili kuunda programu na zana za vitendo.
objectives: 

  - Sintaksia msingi ya JavaScript, aina, na udhibiti mtiririko
  - Kuelewa vipengele, vipengee na madarasa katika JavaScript
  - Jifunze mbinu za kushughulikia na kurekebisha hitilafu
  - Pata taarifa kwa NodeJS na mfumo wake wa ikolojia

---

# Anza safari yako ya maendeleo


Karibu kwenye kozi hii ya JavaScript na NodeJS.


JavaScript ndiyo lugha maarufu zaidi ya programu ulimwenguni: ni lugha ya uandishi ya vivinjari vya kisasa, kwa hivyo kimsingi haiwezekani kuunda programu ya kisasa ya wavuti bila kuandika *baadhi* ya JavaScript; na kwa muda wa utekelezaji wa NodeJS inaweza kutumika nje ya vivinjari pia, kuunda hati na programu zinazoendeshwa moja kwa moja kwenye kompyuta yako.


Kozi hii imeundwa kwa watu ambao ni wapya kabisa katika upangaji programu, au ambao wametumia lugha zingine hapo awali lakini wanataka kuelewa jinsi JavaScript inavyofanya kazi, haswa katika muktadha wa NodeJS.


Kufikia mwisho wa kozi, unapaswa kuwa na uwezo wa kuandika programu zako mwenyewe katika JavaScript, kutumia maktaba ya kawaida ya NodeJS, na kusakinisha na kutumia vifurushi vya watu wengine ili kuunda zana muhimu.


+++
# JavaScript ya Msingi

<partId>a617327c-e5a2-52ca-9380-c63f44623dd4</partId>


## Sanidi

<chapterId>ba05a290-1782-5268-87c9-62fd09590e05</chapterId>




Programu ya JavaScript ni mkusanyiko wa faili za maandishi (moja au zaidi), ambazo zina amri zinazopaswa kutekelezwa na wakati wa utekelezaji wa JavaScript.


Majina ya faili hizi za maandishi kwa kawaida huisha na kiendelezi cha faili `.js`, kama vile `my_script.js`, `my_program.js` n.k.


Amri zilizomo zimeandikwa katika lugha ya programu ya JavaScript.


Muda wa utekelezaji wa JavaScript ni programu maalum ambayo hutekeleza faili hizi.


![](assets/en/1.webp)


### Muda wa utekelezaji wa NodeJS


Wakati wa utekelezaji wa JavaScript unaojulikana zaidi ni NodeJS.


IDE yako inaweza tayari kuwa nayo, au unaweza kuhitaji kuipakua kutoka kwenye [tovuti rasmi](https://nodejs.org/en/download).


Ukurasa wa upakuaji utakupa maagizo kwa OS zote tatu kuu (Mifumo ya Uendeshaji): Windows, Linux na MacOS. Inadhania unajua jinsi ya kufungua terminal katika OS yako.


Kwa kuwa NodeJS inapatikana kwa OS zote tatu, programu unazoandika zitaweza kutekelezwa kwa zote (kuzuia kesi za makali).


Hii inamaanisha kuwa unaweza, kwa mfano, kuandika mchezo rahisi wa video katika JavaScript kwenye Kompyuta yako ya Windows na kuipitisha kwa rafiki yako ili kuuendesha kwenye Mac yake.


![](assets/en/2.webp)














### Mpango wa kwanza (hello world)


Kijadi, wakati wa kusoma lugha ya programu, programu ya kwanza ambayo mtu anaandika inajumuisha uchapishaji "hello world!" kwa console.


Unda saraka iitwayo `my_js_code/`, ikiwa na ndani ya faili inayoitwa `main.js` (majina haya ni ya kiholela).


Fungua saraka kwa kutumia kihariri chako cha msimbo.


Andika nambari hii kwenye faili yako:


```javascript
console.log("hello world!")
```


Fungua terminal na utekeleze amri hii ili kuendesha programu:


```
node main.js
```


Matokeo yanapaswa kuwa


```
hello world!
```


### Nini Kimetokea


Katika JavaScript, kila kitu ni "kitu".


`console` ni kitu, ambacho kinatumika kutatua programu.


`console.log` ndiyo njia inayotumika zaidi ya `console`. Ni tu Prints yoyote hoja kupita yake.


Unapitisha hoja kwa `console.log` kwa kutumia mabano ya pande zote `()`.


Kwa hivyo kwa mfano, ikiwa ungetaka kuchapisha nambari `1000`, ungeandika tu


```javascript
console.log(1000)
```


Kisha utekeleze kwa kukimbia


```
node main.js
```


kwenye terminal yako (kuanzia sasa, kozi hii itafikiria kuwa unajua hivi ndivyo unavyofanya programu).


Hii inapaswa kuchapishwa


```
1000
```


Unaweza kupitisha vitu vingi, kama


```javascript
console.log(16, 8, 1993)
```


Hii itachapisha


```
16 8 1993
```


## Vigezo na maoni

<chapterId>23050ab7-343b-5edf-9d37-e4e782e27ce0</chapterId>


Programu kawaida hutekeleza shughuli kwenye data.


Vigezo ni kama visanduku vilivyotajwa ambavyo tunatumia kuhifadhi data. Zinaturuhusu kuhusisha kipande cha data na jina mahususi, ili tuweze kuirejesha baadaye kwa kutumia jina hilo.


### `hebu` matamko


Ili kutangaza tofauti katika JavaScript, tunaweza kutumia neno kuu la `let`.


Baada ya kuandika `hebu`, tunaandika jina tunalotaka kutoa kwa kutofautisha, kisha ishara `=`, na kisha thamani tunayotaka kuhifadhi.


Kwa mfano:


```javascript
let age = 25

console.log(age)
```


Jina la kigezo (kitaalam kinachoitwa "kitambulisho") kwa kawaida linaweza kuwa na herufi, mistari chini (`_`), ishara ya dola (`$`) na nambari, ingawa herufi ya kwanza haiwezi kuwa nambari.


Katika msimbo ulio hapo juu, tulitangaza kigezo kiitwacho `umri` na tukahifadhi thamani `25` ndani yake.


Kisha, tulichapisha thamani kwa kutumia `console.log(age)`.


Ukiendesha msimbo huu na `node main.js`, matokeo yatakuwa:


```
25
```


Vitambulisho ni nyeti kwa visasi, ambayo ina maana hesabu ya herufi ndogo na kubwa kama tofauti katika vitambulishi, kwa mfano.


```javascript
let age = 25

let Age = 20

console.log(age)
```


itachapisha 25, kwa sababu hizo huchukuliwa kuwa tofauti mbili tofauti kabisa!


Unaweza pia kuhifadhi kamba (maandishi) kwa kutofautisha:


```javascript
let message = "hello again"

console.log(message)
```


Hii itachapisha:


```
hello again
```


Kama tu hapo awali, tulitumia `console.log()` kuchapisha thamani iliyohifadhiwa kwenye kigezo.


Sasa wacha tufanye zote mbili pamoja:


```javascript
let age = 25

let message = "hello again"

console.log(age)

console.log(message)
```


Kuendesha hii kutachapisha:


```
25
hello again
```

### Kukabidhiwa upya


Vigezo vilivyotangazwa na `let` vinaweza kubadilishwa baada ya kuundwa.


Hii inaitwa reassignment.


```javascript
let score = 10

console.log(score)

score = 15

console.log(score)
```


Kwanza, tunaweka `10` kwa `alama`, kisha tuichapishe.


Kisha tunabadilisha thamani ya `alama` hadi `15` na kuichapisha tena.


Pato litakuwa:


```
10
15
```


Hii ni muhimu sana wakati thamani inabadilika kwa wakati, kama vile katika mchezo ambapo alama huongezeka.


Wacha tuongeze tofauti nyingine kwenye mchanganyiko:


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


Hii itachapisha:


```
10
Alice
20
Bob
```


Kama unavyoona, `alama` na `mchezaji` zilibadilishwa.


### matamko ya `const`


Ingawa, mara nyingi, hatutaki mabadiliko yabadilike baada ya kuundwa. Kwa hiyo, tunatumia `const`.


`const` ni kifupi cha "constant". Mara tu unapopeana thamani kwa tofauti ya `const`, huwezi kuibadilisha.


```javascript
const pi = 3.14
console.log(pi)
```


Hii inachapisha:


```
3.14
```


Lakini ukijaribu kufanya hivi:


```javascript
const pi = 3.14
console.log(pi)

pi = 99 // this line will cause an error
console.log(pi)
```


JavaScript itakupa kosa kama:


```
TypeError: Assignment to constant variable.
```


Hii ni kwa sababu `pi` ilitangazwa kwa kutumia `const`, na huwezi kubadilisha thamani yake baada ya hapo. Unawasiliana na mkalimani wa JavaScript ambaye hutaki utofauti huo ubadilike.


Hii ni muhimu kwa sababu inapunguza uwezekano wa kuibadilisha kwa makosa. Programu zinapokuwa kubwa sana, na maelfu ya mistari ya msimbo, haiwezekani kuendelea na kila kitu kinachotokea kwa wakati mmoja (ndio sababu kuu ya sisi kutumia kompyuta, kutekeleza michakato ngumu ambayo hatuwezi kuhesabu na akili zetu), kwa hivyo inakuwa muhimu kuwa na vizuizi kama hivi, ambavyo hufanya programu kuwa ya kuamua zaidi.


Inachukuliwa kuwa njia bora zaidi kutangaza thamani zetu kila wakati kama `const`, isipokuwa tuna uhakika kuwa tunataka kuzirekebisha baadaye.


### Maoni katika JavaScript


Wakati mwingine tunataka kuandika maelezo katika msimbo wetu ambayo hayajatekelezwa. Haya yanaitwa maoni.


Maoni hupuuzwa na programu inapoendeshwa, lakini ni muhimu kwa kujieleza sisi wenyewe au watu wengine mambo.


Ili kuandika maoni ya mstari mmoja, tumia `//`


```javascript
// This is a comment
const x = 10 // This is also a comment
console.log(x)
```


Hii bado itachapisha:


```
10
```


Maoni yapo tu kwa wanadamu kuyasoma.


Unaweza pia kuandika maoni ya mistari mingi kwa kutumia `/*` na `*/`


```javascript
/*
This is a multi-line comment.
It can span several lines.
*/
const y = 20
console.log(y)
```


Hii itachapisha


```
20
```


Na maoni yatapuuzwa.


Unaweza kutumia maoni kuongeza vidokezo vidogo kwenye msimbo wako, ili uweze kukumbuka inachofanya na kwa nini imeandikwa kwa njia fulani. Inaweza pia kusaidia watayarishaji programu wengine kuielewa.


## Aina za msingi: nambari, kamba, booleans

<chapterId>cfdb04f6-21a8-5143-bbf9-7aaae04962f0</chapterId>


Katika JavaScript, "aina" inakuambia thamani ni ya aina gani.


Javascript ina aina chache za msingi, na katika sehemu hii tutachunguza baadhi yao.


### Nambari na shughuli za hesabu


Aina ya kwanza tutakayoanzisha ni `nambari`.


Nambari katika JavaScript zinaweza kuwa nambari kamili (kama `5`) au desimali (kama `3.14`).


Unaweza kufanya hesabu nao: kuongeza, kutoa, kuzidisha, na kugawanya.


Hapa kuna mfano wa msingi:


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


Hii itachapisha:


```
15
5
50
2
```


Unaweza pia kutumia mabano `()` kudhibiti mpangilio wa utendakazi:


```javascript
const result = (2 + 3) * 4
console.log(result)
```


Hii inachapisha:


```
20
```


Bila mabano, itakuwa `2 + 3 * 4`, ambayo ni:


```javascript
const result = 2 + 3 * 4
console.log(result)
```


Hiyo ingechapisha:


```
14
```


Kwa sababu katika hesabu ya kawaida, kuzidisha hufanyika kabla ya kuongeza.


### Kamba na tafsiri


Aina ya pili ya JavaScript tutakayoanzisha ni `string`.


Kamba ni vipande vya maandishi. Unaweza kutumia nukuu moja `'...'` au nukuu mara mbili `"..."` ili kuziunda.


```javascript
const greeting = "hello"
const name = 'Bob'
console.log(greeting)
console.log(name)
```


Hii inachapisha:


```
hello
Bob
```


Ili kuchanganya mifuatano, unaweza kutumia opereta `+`:


```javascript
const greeting = "hello"
const space = " "
const name = "Bob"

const fullGreeting = greeting + space + name
console.log(fullGreeting)
```


Hii itachapisha:


```
hello Bob
```


Lakini kuna njia nzuri zaidi ya kuchanganya kamba inayoitwa ** tafsiri ya kamba **. Unatumia vijiti kutangaza kamba `` `...` `` na uandike vigeu ukitumia `${...}` ndani ya kamba:


```javascript
const greeting = "hello"
const name = "Bob"

const fullGreeting = `${greeting} ${name}`
console.log(fullGreeting)
```


Hii pia inachapisha:


```
hello Bob
```


Unaweza kujumuisha usemi wowote ndani ya `${...}`:


```javascript
const age = 30
console.log(`Next year, I will be ${age + 1} years old.`)
```


Hii inachapisha:


```
Next year, I will be 31 years old.
```


Ufafanuzi ni wa kawaida sana katika JavaScript ya kisasa.


### Booleans, kulinganisha na shughuli za mantiki


Aina ya tatu tutakayoanzisha ni `boolean`. Imetajwa baada ya mwanahisabati George Boole, ambaye aligundua mantiki ya boolean.


Booleans ni rahisi: thamani mbili tu zinazowezekana, `kweli` na `sivyo`.


Unaweza kuzihifadhi katika anuwai:


```javascript
const theSkyIsBlue = true
const thisCourseIsBad = false

console.log(theSkyIsBlue)
console.log(thisCourseIsBad)
```


Hii inachapisha:


```
true
false
```


Unaweza kuchanganya booleans kwa kutumia waendeshaji mantiki:



- `&&` inamaanisha "na", na itarejesha `kweli` ikiwa tu thamani za **zote** ni `kweli`, vinginevyo itarejesha `false`.
- `||` maana yake ni "au", na itarejesha `kweli` ikiwa **angalau thamani moja** ni `kweli`, vinginevyo (ikiwa zote mbili si za kweli) itarejesha `false`.
- `!` inamaanisha “sio”, inatumiwa kabla ya boolean, na itaipindua: ikiwa boolean ni `kweli` itarejesha `false`, na kinyume chake.


![](assets/en/3.webp)


Mifano:


```javascript
const isSunny = true
const isWarm = true

console.log(isSunny && isWarm)  // true
console.log(isSunny || isWarm)  // true
console.log(!isSunny)           // false
```


Unaweza kulinganisha thamani katika JavaScript kwa kutumia waendeshaji kama `>`, `<`, `===`, na `!==`. Matokeo ya ulinganisho huu daima ni boolean.


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


Javascript pia ina `>=` kumaanisha "kubwa au sawa" na `<=` kumaanisha "ndogo au sawa.


Vipuli, ulinganishaji na waendeshaji kimantiki mara nyingi hujumuishwa katika programu ili kutangaza hali ngumu, kama vile kuhakikisha "barua pepe imefika NA ina picha ninayohitaji AU urefu wa barua pepe ni mrefu zaidi ya vibambo 10000". Utapata baadaye kwamba hizi ni vitalu muhimu vya kujenga mantiki ya programu.


## Safu, null, haijafafanuliwa

<chapterId>7bf18183-5eae-53ed-83d2-b04982145d81</chapterId>


Katika sehemu hii, tutashughulikia aina tatu zaidi ambazo ni za kawaida sana katika programu za JavaScript:



- Mkusanyiko**: mfuatano wa maadili
- haijafafanuliwa**: thamani maalum ambayo inamaanisha "hakuna kilichotolewa"
- null**: thamani nyingine maalum ambayo inamaanisha "tupu kwa kukusudia"


### Mkusanyiko na ufikiaji wa faharasa


**safu** ni aina inayoweza kushikilia thamani nyingi kwenye orodha.


Unaunda safu kwa kutumia mabano ya mraba `[]` na kutenganisha vipengee kwa koma.


Hapa kuna mfano wa msingi:


```javascript
const numbers = [10, 2, 88]
console.log(numbers)
```


Hii inachapisha:


```
[ 10, 2, 88 ]
```


Unaweza kuhifadhi chochote katika safu, sio nambari tu:


```javascript
const things = ["apple", 42, true]
console.log(things)
```


Hii inachapisha:


```
[ 'apple', 42, true ]
```


Ili kufikia kipengee maalum katika safu, tunatumia **index**. Faharasa ni nafasi ya kipengee, kuanzia **0**.


Kwa hivyo katika safu hii:


```javascript
const colors = ["red", "green", "blue"]
```



- `rangi[0]` ni `"nyekundu"`
- `rangi[1]` ni `"Green"`
- `rangi[2]` ni `"bluu"`


Hebu jaribu:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[0])
console.log(colors[1])
console.log(colors[2])
```


Hii itachapisha:


```
red
green
blue
```


Unaweza kugawa thamani kwa faharasa maalum ya safu


```javascript
const colors = ["red", "green", "blue"]

colors[1] = "yellow"

console.log(colors)
```


Hii itachapisha:


```
[ 'red', 'yellow', 'blue' ]
```


Unaweza kutumia nambari yoyote asilia kama faharisi, hata moja iliyohifadhiwa katika kigezo


```javascript

const i = 1
const colors = ["red", "green", "blue"]
console.log(colors[i])
```


Hii itachapisha:


```
green
```


Lakini ukijaribu kupata faharasa ambayo haipo, utapata `undefined`:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[3])
```


Hii inachapisha:


```
undefined
```


Nini hicho??


### `haijafafanuliwa`


Thamani maalum `isiyoelezewa` inamaanisha "hakuna thamani iliyokabidhiwa".


Ukiunda kigezo lakini usiyape thamani, `haitafafanuliwa`:


```javascript
const name
console.log(name)
```


Hii inachapisha:


```
undefined
```


Kwa sababu hatukukabidhi chochote kwa `jina`, JavaScript inaiweka kuwa `isiyofafanuliwa` kwa chaguomsingi.


Kama inavyoonekana hapo awali, unaweza pia kupata `undefined` unapofikia faharisi ya safu ambayo haipo:


```javascript
const fruits = ["banana", "apple"]
console.log(fruits[2]) // There is no index 2
```


Hii inachapisha:


```
undefined
```


### `null` na jinsi ya kutibu


`null` pia ni thamani maalum. Inamaanisha "hakuna kitu hapa, na nilifanya hivyo kwa makusudi."


Tofauti na `undefined`, ambayo ni otomatiki, `null` ni kitu ambacho unajiwekea.


Kwa mfano:


```javascript
const currentUser = null
console.log(currentUser)
```


Hii inachapisha:


```
null
```


Kwa nini utumie `null`? Labda unatarajia thamani baadaye, lakini bado haijawa tayari:


```javascript
let winner = null

// Later in the program:
winner = "Alice"

console.log(winner)
```


Hii inachapisha:


```
Alice
```


Kwa hivyo `null` ni muhimu unapotaka kusema, kwa mfano, "Lazima kuwe na kitu hapa baadaye, lakini sasa hivi ni tupu."


## Vizuizi na mtiririko wa udhibiti

<chapterId>be985168-2636-5b0d-a48f-ac1bbfbff8a7</chapterId>


Kufikia sasa, tumeandika zaidi mistari ya msimbo inayoendesha moja baada ya nyingine.


Lakini tunapoweka kanuni, tunaweza kudhibiti utaratibu wa utekelezaji wake.


Hii inaitwa **control flow**.


Hebu tuanze na uelewa wa vitalu na upeo.


### Upeo wa kimataifa


Kila kigezo tunachotangaza kipo katika **wigo**, ambayo inamaanisha eneo la msimbo ambapo kigezo kinajulikana.


Ukitangaza kigezo nje ya kizuizi chochote, kinapatikana katika **mawanda ya kimataifa**.


```javascript
const color = "blue"
console.log(color)
```


Tofauti hii `rangi` iko katika wigo wa kimataifa, kwa hivyo inaweza kufikiwa kutoka mahali popote kwenye faili.


Ikiwa unaongeza mistari zaidi:


```javascript
const color = "blue"
console.log(color)

const size = "large"
console.log(color)
console.log(size)
```


`Rangi` na `ukubwa` ni vigeu vya kimataifa. Zinapatikana kila mahali kwenye faili.


Lakini nini kinatokea ndani ya block?


### Vitalu na upeo wa ndani


**block** ni kipande cha msimbo kilichozungukwa na viunga vilivyopinda `{}`.


Vigezo vilivyotangazwa kwa `let` au `const` ndani ya block vipo **pekee** ndani ya kizuizi hicho.


```javascript
{
const message = "inside block"
console.log(message)
}
```


Hii inachapisha:


```
inside block
```


Lakini ukijaribu hii:


```javascript
{
const message = "inside block"
}
console.log(message) // Error!
```


JavaScript itakupa kosa kama:


```
ReferenceError: message is not defined
```


Hiyo ni kwa sababu `ujumbe` ulitangazwa ndani ya kizuizi na haupo nje yake.


Hii inamaanisha kuwa tunaweza kutumia vizuizi kutenga sehemu za msimbo wetu, na kuwa na uhakika kwamba "kile kinachotokea kwenye kizuizi kitasalia kwenye kizuizi" (kama vile Las Vegas).


Kupanga nambari yetu katika vizuizi huturuhusu pia kupanga utekelezaji wa programu, na muundo wa mtiririko wa udhibiti kama `if`.


### `kama`, `vingine`


Wakati mwingine tunataka kutekeleza msimbo ** ikiwa tu ** kitu ni kweli. Hiyo ndiyo maana ya kauli ya `if`.


```javascript
const myAge = 20

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Hii inachapisha:


```
Am I an adult?
Yes I am!
```


Unavyoweza, tazama msimbo unalinganisha `myAge` na `18`.

Katika hali hii opereta `>=` anarudisha `kweli`, kwa hivyo kizuizi kinatekelezwa.

Ikiwa hali si `kweli`, kizuizi hakitekelezwi.


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Hii inachapisha:


```
Am I an adult?
```


Unaweza kuongeza kizuizi cha `nyingine` kushughulikia kesi iliyo kinyume:


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
} else {
console.log("No, I am not.")
}
```


Hii inachapisha:


```
Am I an adult?
No, I am not.
```


Vitalu vya `ikiwa` na `vingine` bado ni vizuizi - kwa hivyo vibadala vilivyotangazwa ndani yake havipo nje.


Ikiwa tunataka kuwa na uhakika kwamba kitu **si** kweli, tunaweza kufanya nini?


Kweli, kama ilivyojadiliwa hapo awali, JavaScript ina opereta "sio", ambayo hugeuza booleans. Kwa hiyo tunaweza kufanya


```javascript
const myAge = 17

const adult = myAge >= 18

console.log("Am I an adult?")

if (!adult) {
console.log("No, I am not.")
}
```

Hii bado inachapisha:


```
Am I an adult?
No, I am not.
```

Kwa sababu tulitumia opereta `!` kugeuza kigezo cha `mtu mzima`.


`kama (!mtu mzima) {...}` inapaswa kusomwa kama "kama si mtu mzima..."


Kwa kutumia vizuizi, mantiki na waendeshaji kulinganisha, tunaweza kupanga utekelezaji wa programu, kwa kubainisha viambajengo ambavyo lazima ziwe `kweli` (au `sivyo`) ili jambo lifanyike.


### `wakati`, `vunja`, `endelea`


Kitanzi cha `wakati` kinarudia msimbo *ilimradi* hali ni kweli.


```javascript
let count = 0

while (count < 3) {
console.log("Count is", count)
count = count + 1
}
console.log("the loop is over!")
```


Hii inachapisha:


```
Count is 0
Count is 1
Count is 2
the loop is over!
```


Wakati `hesabu` inakuwa 3, kitanzi kinasimama.


Unaweza kusimamisha kitanzi mapema kwa kutumia `break`:


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


Hii inachapisha:


```
0
1
2
```


Kwa sababu wakati nambari inakuwa `3`, kizuizi cha `if` kinatekelezwa na kusimamisha kitanzi.


Unaweza kuruka kitanzi kingine ukitumia `endelea`:


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


Hii inachapisha:


```
1
2
4
5
```


Kwa sababu nambari ilipokuwa `3`, `endelea` ilifanya programu kuruka mstari unaochapisha nambari.


### `kwa ... ya ...`


Ikiwa una safu, na unataka kufanya kitu kwa kila kitu ndani yake, unaweza kutumia `kwa ... ya ... {...}`.


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const fruit of fruits) {
console.log(fruit)
}
```


Hii inachapisha:


```
apple
banana
cherry
```

Kizuizi kitatekelezwa mara moja kwa kila kipengele cha safu.


`fruit` hapa ni kigezo kipya ambacho huchukua thamani ya kila kipengee katika safu, ili kukifanyia kazi ndani ya kizuizi.


### `kwa ... katika ...`


Unaweza kutumia `kwa ... in` kuzunguka funguo (faharisi) za safu:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(index)
}
```


Hii inachapisha:


```
0
1
2
```


Unaweza kutumia faharisi kupata thamani pia:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(fruits[index])
}
```


Hii inachapisha sawa na `kwa ... ya`:


```
apple
banana
cherry
```


Kwa mazoezi, kwa safu, unapaswa kupendelea kutumia `kwa ... ya`, kwani ni rahisi na safi zaidi.


### Vitanzi vilivyofungwa


Wakati mwingine tunataka kuweka idadi maalum ya nyakati, au kwa ujumla kuandika kipande cha msimbo ambacho hurudia kizuizi huku tukifuatilia jambo fulani.

Hivyo ndivyo kitanzi cha `for` kinafaa.

Kitanzi chenye mipaka kwa kawaida huchukua masharti matatu, kikitenganishwa na nusu koloni `;`, kama katika `(... ; ... ; ....)`.


```javascript
for (let i = 0; i < 3; i = i + 1) {
console.log(i)
}
```


Hii inachapisha:


```
0
1
2
```


Hebu tufafanue:



- `let i = 0`: inatangaza kigezo cha kutumika kwenye kizuizi (katika kesi hii ni kihesabu kinachoanzia 0)
- `i <3`: inatangaza sharti kuwa `kweli` ili kizuizi kitekelezwe ( katika kesi hii ni "rudiwa wakati `i` ni chini ya 3")
- `i = i + 1`: tangaza msimbo fulani utakaoendeshwa baada ya kila utekelezaji wa kizuizi (katika kesi hii "ongeza `i` kwa 1").


Kama unavyoweza kuona kitanzi kilichowekwa ili kutangaza hali ngumu zaidi kwa utekelezaji unaorudiwa wa kipande cha nambari, lakini mara nyingi sio lazima.


### Zuia lebo


Iwapo itabidi uandike mtiririko changamano zaidi wa udhibiti, JavaScript hukuruhusu kutaja kizuizi ukitumia **lebo** inayoweza kutumiwa na `break` au `continue` kwa kubainisha *wapi* pa kuruka nyuma.


Mfano:


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


Hii inachapisha:


```
Inside outer block
Inside inner block
Done
```


Tulitumia `break outer` kuondoka kabisa kwenye kizuizi cha `nje`.


Unaweza pia kuweka lebo kwenye vitanzi. Hebu tuchukue mfano huu:


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

Huu ulikuwa mfano wa kuchosha sana lakini kwa matumaini ulifafanua hitaji (la mara kwa mara) la lebo.


## Kuanzisha vipengele

<chapterId>cc324715-09c2-5cf7-9e6f-47a6f16bc04d</chapterId>


Kadiri programu zako zinavyokua, mara nyingi utataka **kutumia tena** vipande vya msimbo.


Hivyo ndivyo **faili** ni za: zinakuwezesha kupanga msimbo fulani pamoja, uipe jina, na uiendeshe wakati wowote unapotaka.


### Tamko la kazi


Ili kutangaza chaguo za kukokotoa, tunaweza kutumia neno kuu la `kazi`. Kisha tunaipa jina, jozi ya mabano `()` pamoja na hoja zinazohitajika, na kizuizi cha msimbo `{}` cha kutekelezwa. Wacha tuanze na chaguo la kukokotoa ambalo halichukui hoja:


```javascript
function sayHello () {console.log(`Hello!`) }
```


Nambari hii ** inatangaza ** chaguo la kukokotoa, lakini ** haiiendeshi ** bado.


### Kazi wito


Ili kuendesha (au "piga simu") kazi, unaandika jina lake likifuatiwa na mabano:


```javascript
function sayHello () {console.log(`Hello!`) }
sayHello()
```


Hii inachapisha:


```
Hello!
```


Unaweza kupiga simu mara nyingi unavyotaka:


```javascript
function sayHello() {
console.log("Hello!")
}

sayHello()
sayHello()
```


Hii inachapisha:


```
Hello!
Hello!
```


Nambari iliyo ndani ya chaguo la kukokotoa hutumika tu unapoiita.


### Hoja za utendakazi (ingizo kwa vitendakazi)


Wakati mwingine, unataka chaguo za kukokotoa kufanya kazi na ingizo fulani. Unaweza kufanya hivyo kwa kuongeza **hoja** ndani ya mabano.


Kwa mfano:


```javascript
function sayHelloTo (friend) {
console.log(`Hello ${friend}!`)
}
```


Sasa chaguo hili la kukokotoa linachukua **hoja moja** inayoitwa `rafiki`.


Unapoita kazi, unaweza kupitisha thamani:


```javascript
sayHelloTo("Tommy")
```


Hii inachapisha:


```
Hello Tommy!
```


Unaweza kuita kitendakazi tena kwa jina tofauti:


```javascript
sayHelloTo("Sam")
```


Hii inachapisha:


```
Hello Sam!
```


Thamani unayopitisha inachukua nafasi ya `rafiki` tofauti ndani ya chaguo za kukokotoa.


Unaweza pia kutumia hoja zaidi ya moja:


```javascript
function greetTwoPeople(person1, person2) {
console.log(`Hello ${person1} and ${person2}!`)
}

greetTwoPeople("Lina", "Marco")
```


Hii inachapisha:


```
Hello Lina and Marco!
```


### `return` (matokeo kutoka kwa vitendaji)


Kazi zinaweza pia **kurudisha** thamani. Hii ina maana kwamba wanatuma thamani nyuma popote pale chaguo la kukokotoa lilipoitwa.


Hapa kuna mfano rahisi:


```javascript
function getNumber() {
return 42
}

const result = getNumber()
console.log(result)
```


Hii inachapisha:


```
42
```


Chaguo za kukokotoa `getNumber()` hurejesha `42`, na tunaihifadhi katika `matokeo`, kisha tuichapishe.


Unaweza pia kurudisha kitu unachohesabu:


```javascript
function add(a, b) {
return a + b
}

const result = add(2, 3)
console.log(result)
```


Hii inachapisha:


```
5
```


Mara tu thamani `imerejeshwa`, chaguo za kukokotoa husimama. Chochote baada ya `kurudi` katika kizuizi hicho hakifanyiki.


```javascript
function saySomething() {

return "hi"

console.log("this never runs")

}

const message = saySomething()
console.log(message)
```


Hii inachapisha pekee:


```
hi
```


kwa sababu `"hi"` pekee ndiye anayerejeshwa. Laini ya `console.log("hii haifanyiki kamwe")` imerukwa.


Unaweza kufikiria kazi kama programu ndogo ndogo. Kila chaguo la kukokotoa linaweza kuchukua ingizo, lifanyie kazi, na kukupa matokeo fulani.


Nini kitatokea ikiwa tutajaribu kutumia thamani ya kukokotoa, lakini chaguo la kukokotoa halikurejesha chochote?


```javascript
function doesNothing () {}

const x = doesNothing()

console.log(x)
```

Hii itachapisha `undefined`. Thamani ya kurejesha ya chaguo za kukokotoa ambayo haikurejesha chochote `haijabainishwa`.


## Vitu na madarasa

<chapterId>26689f25-8212-5057-8c21-3a05eee0ac75</chapterId>


JavaScript mara nyingi huitwa lugha inayolenga kitu.


Hiyo inamaanisha inakusaidia kupanga msimbo wako kwa kuweka thamani katika vikundi na kufanya kazi pamoja katika **vitu**.


### `kitu` ni nini?


Kipengee kinaweza kuwa na data na vitendakazi vinavyofanya kazi kwenye data hiyo. Chaguo za kukokotoa zinapowekwa kwenye kitu tunasema ni `mbinu`.


Kitu cha kwanza ambacho tumeona kilikuwa kitu cha `console`. Ni kitu ambacho kina mbinu nyingi za kuchapisha kitu kwenye skrini na kutatua programu zetu.


Inaweza hata kuchapisha yenyewe; unaweza kufanya


```javascript
console.log(console)
```


na itachapisha orodha ya njia ambazo ina. Kwa mfano, kwenye mashine yangu ilichapishwa


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


Kama unaweza kuona, ina njia nyingi ambazo unaweza kutumia kutatua hitilafu!


Javascript hutupatia njia tofauti za kuunda vitu vipya ambavyo vinaweza kufanya chochote tunachotaka wafanye.


### Kuunda kitu


Njia rahisi zaidi ya kuunda kipengee ni kwa kupanga data na vitendakazi katika vikundi kwa kutumia viunga vilivyopinda ** `{}`.


Hii inaunda kile tunachokiita **kitu kisichojulikana**


```javascript
const cat = {
name: "Whiskers",
age: 3
}
```


Hii huunda kitu na kukihifadhi katika kigezo kiitwacho `paka`.


Kitu kina sifa mbili **:



- `jina` lenye thamani `"Whiskers"`
- `umri` yenye thamani `3`


Wacha tuichapishe:


```javascript
console.log(cat)
```


Hii inachapisha:


```
{ name: 'Whiskers', age: 3 }
```


Unaweza kupata sifa kutoka kwa kitu kwa kutumia nukta, kama ilivyo `objectName.propertyName`:


```javascript
console.log(cat.name)  // prints "Whiskers"
console.log(cat.age)   // prints 3
```


Unaweza pia ** kubadilisha ** mali:


```javascript
cat.age = 4
console.log(cat.age)  // now it prints 4
```


Kama unavyoona, hata kama kitu kinafafanuliwa kama `const`, bado unaweza kurekebisha data iliyomo.


Kwa upande wa vitu, `const` itakuzuia tu kutoka juu ya kitu kizima:


```javascript
const cat = {
name: "Whiskers",
age: 3
}

cat.age = 5 // this works

cat = 5 // this throws an error, you're trying to reassign the whole object

```


Kama ilivyotajwa hapo awali, vitu vinaweza pia kushikilia ** kazi **, na wakati chaguo la kukokotoa ni sehemu ya kitu, tunaiita **njia **.


Hapa kuna mfano:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log("Meow!")
}
}
```


Kipengee hiki kina:



- Mali ya `jina`
- Mbinu ya `sema()`


Wacha tuite njia:


```javascript
cat.speak()
```


Inachapa:


```
Meow!
```


Mbinu zinaweza kutumia data iliyo na kitu kupitia neno kuu `hii`.

`hii` inarejelea kitu cha sasa. Katika mfano huu, itatumika kuchapisha jina la paka:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log(`${this.name} says meow!`)
}
}

cat.speak()
```


Hii inachapisha:


```
Whiskers says meow!
```


Neno `hili` linamaanisha "kitu hiki"...katika kesi hii, kitu `paka`.



Aina hizi za vitu ni nzuri wakati unataka tu kitu cha haraka na rahisi. Lakini ikiwa unahitaji kuunda **vitu vingi** vilivyo na muundo sawa, kuna njia bora zaidi, na hapo ndipo **madarasa** yanapoingia.


### Madarasa na wajenzi


**darasa** ni kama mchoro. Inaambia JavaScript jinsi ya kuunda aina fulani ya kitu.


Unafafanua darasa kwa kutumia neno kuu la `class`, likifuatiwa na jina la darasa, na viunga vilivyopinda `{}`.


```javascript
class Dog {}
```


Madarasa kwa kawaida huanza na herufi kubwa, kwa makubaliano.


Unaweza kuunda kitu kipya cha darasa kwa kutumia `mpya`:


```javascript
const hachiko = new Dog()
```


Jaribu kuchapisha kitu:

```javascript
class Dog {}

const myDog = new Dog()

console.log(myDog)
```


Utapata


```
Dog {}
```


Kama unavyoona darasa la Mbwa ni tupu, kwa hivyo kitu cha `myDog` hakina kitu pia.


Tunaweza kufafanua ni sifa gani vitu vya Mbwa vinapaswa kuwa na kwa kuongeza `kijenzi`.


Mjenzi ni kazi maalum inayofanya kazi unapounda (au "kujenga") kitu kipya.


```javascript
class Dog {
constructor() { }
}
```


Tunataka kila Mbwa awe na jina, kwa hivyo tunaongeza parameta ya `jina` kwenye chaguo la kukokotoa:


```javascript
class Dog {
constructor(name) { }
}
```


Na kisha tunatumia `hii` kutangaza kuwa `jina` ni `jina` la kitu cha `Mbwa` tunachojenga.


```javascript
class Dog {
constructor(name) {
this.name = name
}}
```


Wacha tujaribu kuitumia sasa:


```javascript
class Dog {
constructor(name) {
this.name = name
}
}

const myDog = new Dog("hachiko")

console.log(myDog)
```


Hii inachapisha kitu kama:


```
Dog { name: 'hachiko' }
```


Kama unavyoona, njia ya `mjenzi` inachukua hoja unazopitisha kwa darasa unapofanya `new Dog()`, na huitumia kujenga kitu hicho.


Wacha tuichambue:



- `class Dog` inafafanua tabaka la Mbwa.
- `mjenzi(jina)` huweka kipengee kinapoundwa.
- `this.name = name` huhifadhi thamani katika kitu kipya.
- `new Dog("hachiko")` huunda kipengee kipya kutoka kwa darasa, na sifa ya `jina` imewekwa kuwa `"hachiko"`.


Sasa wacha tuongeze njia kwenye darasa letu:


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


Hii itachapisha


```javascript
hachiko says barf!
```


Ikiwa tutafanya vivyo hivyo kwa matukio mawili tofauti ya Mbwa



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


tunapata


```
hachiko says barf!
bobby says barf!
```


mbinu ya `speak()` hutumia `jina` sifa ya `Mbwa` inaitwa.


Hii ndiyo sababu kuu ya madarasa kuwepo: huturuhusu kufafanua seti ya mbinu zinazofanya kazi kwenye data, na kisha kuunda vitu vingi vinavyoshiriki data sawa "sura".


Tunapoita mbinu kwenye mojawapo ya vitu hivi, itafanya kazi kwenye data *hicho kitu maalum* kinashikilia.


### Kubadilisha umbo la kitu


Vipengee katika JavaScript vinaweza kunyumbulika. Hata baada ya kuunda moja, bado unaweza kuongeza sifa mpya au kuondoa zilizopo.


Inaruhusiwa, lakini ni jambo ambalo unapaswa kutumia kwa uangalifu.


Wacha tuanze na darasa letu rahisi la `Mbwa`:


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


Kwa wakati huu, `myDog` ina sifa moja pekee: `jina`. Bado tunaweza kuongeza sifa mpya baada ya kuundwa:


```javascript
myDog.age = 5

console.log(myDog.age) // prints 5
```


Tunaweza pia kuongeza mbinu mpya:


```javascript
myDog.jump = function () {
console.log(`${this.name} jumps!`)
}

myDog.jump() // Fido jumps!
```


Na tunaweza kuondoa sifa pia, kwa kutumia neno kuu la `delete`.


```javascript
delete myDog.name

console.log(myDog.name) // prints 'undefined'
```


Hili linafanya kazi, lakini hapa kuna jambo muhimu kujua: Injini za JavaScript kama V8 (inayotumiwa katika Node.js na katika kivinjari cha Chrome) hufanya kazi haraka wakati vitu vyako hudumisha sifa sawa kila wakati. Ukiongeza au kuondoa sifa baada ya kipengee kuundwa, inaweza kupunguza kasi ya mambo.


Katika programu ndogo, hii haijalishi sana. Lakini katika miradi mikubwa (kama michezo), ni bora kuorodhesha mali zote kwenye mjenzi tangu mwanzo, hata ikiwa hutumii mara moja. Hii hudumisha umbo la kitu na husaidia msimbo wako kufanya kazi haraka.


Kwa mfano, badala ya hii:


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


Unaweza kufanya


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


Matoleo yote mawili yanafanya kazi, lakini ya pili ni bora kwa utendaji. Unaiambia injini mbele ambayo kila kitu kitakuwa na mali, na inaweza kuongeza ipasavyo.


JavaScript inakuwezesha kuunda upya vitu kwa uhuru, lakini unapotumia madarasa, ni vyema kupanga umbo la kitu chako kabla ya wakati.



### Urithi wenye `extens` na `super()`


Wakati mwingine ungependa kuunda darasa ambalo *karibu* sawa na darasa lingine, lakini lenye vipengele vichache vya ziada.


Badala ya kurekebisha sura ya vitu (ambayo kama ilivyotajwa hapo awali sio sawa kwa utendakazi), au kulazimika kuandika upya darasa jipya kutoka mwanzo, JavaScript hukuruhusu kutumia kitu kinachoitwa **urithi**.


Urithi unamaanisha darasa moja linaweza **kupanua** lingine. Darasa jipya hupata sifa na mbinu zote za ile ya zamani, na unaweza kuongeza zaidi au kubadilisha unachohitaji.


Wacha tuseme tuna darasa la msingi linaloitwa `Gari`:


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


Sasa tunataka kutengeneza darasa la `Gari`. Gari ni aina ya gari, lakini tunaweza kutaka liwe na vipengele vingine vya ziada au ujumbe tofauti linapowashwa. Badala ya kuandika upya kila kitu, tunaweza kutumia `extends`:


```javascript
class Car extends Vehicle {
start() {
console.log(`${this.brand} car is ready to drive!`)
}
}
```


Darasa la `Gari` sasa **linarithi** kila kitu kutoka kwa `Gari`. Inapata sifa ya `brand`, na tumebadilisha mbinu ya `start()` kwa toleo letu.


![](assets/en/4.webp)


Hebu tujaribu:


```javascript
const myCar = new Car("Toyota")
myCar.start()
```


Hii inachapisha:


```
Toyota car is ready to drive!
```


Ingawa `Gari` haina kijenzi chake, bado kinatumia ile ya `Gari`. Lakini ikiwa tunataka kuandika kijenzi maalum katika `Gari`, tunaweza, tunahitaji tu kujumuisha simu kwa mjenzi wa mzazi wake kwa kutumia `super()`.


Hivi ndivyo jinsi:


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



Hii inachapisha:


```
Toyota Corolla is ready to drive!
```


Hivyo kwa muhtasari



- `extens` inamaanisha darasa moja linategemea lingine.
- `super()` inatumika kumwita mjenzi wa darasa unalopanua.
- Darasa jipya linapata mali na njia zote za darasa la asili.
- Unaweza ** kubatilisha ** njia (kama `start()`) ili kuwafanya wafanye kitu tofauti.


Hii inasaidia unapokuwa na vitu kadhaa vinavyofanana (kama vile magari, lori, na baiskeli) na unataka washiriki nambari ya kuthibitisha lakini bado wafanye mambo yao wenyewe.


### `mfano`


Neno kuu la `instanceof` hukagua ikiwa kitu kiliundwa kutoka kwa aina fulani.


Wacha tuseme tuna darasa linaloitwa `Mtumiaji`:


```javascript
class User {
constructor(username) {
this.username = username
}
}

const regularUser = new User("julia123")

console.log(regularUser instanceof User)
```


Hii inachapisha:


```
true
```


Inathibitisha kwamba `Mtumiaji wa kawaida` ni `Mtumiaji`. Hiyo ni kwa sababu `regularUser` iliundwa kwa kutumia darasa la `Mtumiaji`.


Pia inafanya kazi na madarasa ya **kurithi**. Kwa mfano, hapa kuna darasa la `Msimamizi` linaloongeza `Mtumiaji`:


```javascript
class Admin extends User {}

const ourAdmin = new Admin("admin42")

console.log(ourAdmin instanceof Admin)   // true
console.log(ourAdmin instanceof User)    // true
```


Mistari yote miwili inarudisha `kweli`. Hiyo ni kwa sababu `Admin` ni daraja ndogo ya `Mtumiaji`, kwa hiyo `Msimamizi wetu` ni `Msimamizi` na `Mtumiaji`.


# JavaScript ya kati

<partId>243f63ab-4f34-5c30-80cb-84ef46f6761d</partId>


## Kushughulikia Hitilafu

<chapterId>d0206bc5-d386-5e7f-9917-5803f392448c</chapterId>


Unapoandika programu ngumu zaidi za JavaScript, utakutana na **makosa**. Hizi ni hali zisizotarajiwa ambapo kitu kitaenda vibaya. Labda kigezo `hakijafafanuliwa` lakini unajaribu kukitumia, au msimbo fulani hupokea aina isiyo sahihi ya ingizo.


Ikiwa hatutashughulikia hitilafu hizi ipasavyo, programu yetu inaweza kuacha kufanya kazi au kutenda kwa njia zisizotabirika. JavaScript hutoa zana za kugundua na kudhibiti hitilafu hizi ili tuweze kuzishughulikia kwa uzuri zaidi.


### Hitilafu ya kawaida: kufikia thamani kwenye `undefined`


Hapa kuna hali ya kawaida ambayo husababisha hitilafu:


```javascript
const user = undefined
console.log(user.name)
```


Ukiendesha nambari hii, utapata hitilafu inayoonekana kama hii:


```
TypeError: Cannot read properties of undefined (reading 'name')
```


Hiyo ni JavaScript inayokuambia: "Haya, ulijaribu kupata mali ya `jina` kutoka kwa kitu ambacho `hakijafafanuliwa`, na hiyo haileti maana." Na kama unavyoona, aina hii ya hitilafu inapotokea, programu huacha kufanya kazi isipokuwa kama umeandika msimbo maalum wa kuikamata na kuishughulikia.


### `kutupa` kosa


Wakati mwingine unataka wewe mwenyewe **kuleta hitilafu** katika msimbo wako. Katika hali hiyo, unatumia neno kuu la `kutupa`.


```javascript
throw new Error("This is a custom error message")
```


Hii inasimamisha programu mara moja na kuchapisha:


```
Uncaught Error: This is a custom error message
```


Unaweza kutumia `kutupa` kutekeleza sheria katika programu yako. Kwa mfano:


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


Simu ya pili husababisha hitilafu kwa sababu kugawanya kwa sifuri hairuhusiwi katika mfano huu.


### Kunasa hitilafu kwa `jaribu...kamata`


Ikiwa hutaki programu yako ivunjike hitilafu inapotokea, unaweza kupata hitilafu kwa kutumia kizuizi cha `jaribu...kamata`. Hii ni muhimu unapotaka programu yako **iendelee** hata kama kuna kitu kitashindikana.


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log("Oops! Something went wrong.")
}
```


Pato:


```
Oops! Something went wrong.
```


Hivi ndivyo inavyofanya kazi:



- Msimbo ulio ndani ya kizuizi cha `jaribu` unajaribiwa kwanza.
- Hitilafu ikitokea, JavaScript **inaruka hadi kwenye kizuizi cha `kamata`**, na kuruka kizuizi kingine cha `jaribu`.
- Kizuizi cha `kamata` hupokea hitilafu, kwa hivyo unaweza kuichapisha, au kuishughulikia kwa njia nyingine, kama kwa mfano.


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log(`The message of the error was: "${error.message}"`)
}
```


Pato:


```
The message of the error was: "Cannot read properties of undefined (reading 'name')"
```


### Kizuizi cha `mwisho`


Unaweza pia kuongeza kizuizi cha `hatimaye`. Huu ni msimbo ambao **huendesha kila wakati**, iwe kulikuwa na hitilafu au la.


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


Pato:


```
Trying something risky...
Caught the error: Uh oh!
This will run no matter what.
```


## Kuepuka Mdudu

<chapterId>db12d9f6-5806-514c-998e-0ae24805104e</chapterId>


Sura hii inaonyesha baadhi ya mitego ya kawaida katika JavaScript, na jinsi ya kuziepuka.


### `var` na Assignment bila tamko


Katika msimbo wa zamani wa JavaScript, anuwai mara nyingi zilitangazwa kwa kutumia neno kuu la `var`. Tofauti na `let` na `const`, ambazo tayari umejifunza kuzihusu, `var` inaweza kuwa na tabia za kutatanisha.


Kwa mfano:


```javascript
{
var message = "hello"
}
console.log(message)
```


Unaweza kutarajia `ujumbe` kuwepo tu ndani ya kizuizi, lakini haipo. `var` hupuuza upeo wa kuzuia na hufanya utofauti huo upatikane katika kipengele chote cha kukokotoa au faili.


Hii inaweza kusababisha tabia zisizotarajiwa, haswa katika programu kubwa. Kwa sababu hii, msimbo wa kisasa wa JavaScript unapaswa kutumia `let` au `const` badala ya `var`.


Mbaya zaidi, JavaScript hukuruhusu kupeana maadili kwa anuwai ** bila kutangaza kabisa **:


```javascript
function greet() {
user = "Alice"
}
greet()
console.log(user) // prints "Alice"
```


Hii inaunda kibadilishaji kipya cha kimataifa `jina` bila tamko lolote. Hili linaweza kutokea kimyakimya na kusababisha hitilafu ambazo ni Hard kufuatilia, haswa ikiwa ilikuwa tu makosa ya kuandika. Tangaza vigeu kila wakati kwa kutumia `let` au `const`.


### Mfumo wa aina dhaifu


JavaScript imechapishwa kwa njia dhaifu, kumaanisha kuwa inabadilisha maadili kiotomatiki kutoka aina moja hadi nyingine ikiwa inahitajika. Hii inaitwa aina ya kulazimishwa, na ingawa inaweza kuwa rahisi, mara nyingi husababisha matokeo ya kutatanisha.


Kwa mfano:


```javascript
console.log("5" + 1)    // "51"
console.log("5" - 1)    // 4
console.log(true + 1)   // 2
console.log(null + 1)   // 1
```


Katika mifano hii, JavaScript inajaribu kukisia ulichomaanisha. Wakati mwingine hugeuza nyuzi kuwa nambari, au booleans kuwa nambari, au nyuzi kuwa nyuzi. Hii inaweza kufanya nambari yako kufanya kazi kwa njia zisizotarajiwa.


Kufahamu mfumo dhaifu wa kuandika wa JavaScript ni muhimu. Mambo yanapoanza kutenda kwa njia ya ajabu, inaweza kuwa ni kwa sababu ya shurutisho la aina isiyotarajiwa.


### `"tumia kali"`


Unaweza kuwezesha hali ngumu zaidi ambayo inabadilisha baadhi ya makosa kimya kuwa makosa halisi, na kukuzuia kutumia baadhi ya vipengele hatari zaidi vya lugha.


Ili kuwezesha hali hii kali, ongeza laini hii juu ya faili au chaguo lako la kukokotoa:


```javascript
"use strict"
```


Kwa mfano:


```javascript
"use strict"
name = "Alice" // ReferenceError: name is not defined
```


Bila hali madhubuti, JavaScript ingeunda kitofautishi cha kimataifa kiitwacho `jina` kimyakimya. Lakini kwa hali kali, hii inakuwa kosa la kweli, kukusaidia kupata mende mapema.


Hali kali pia huzima baadhi ya vipengele vilivyopitwa na wakati vya JavaScript, na hurahisisha msimbo wako kuboresha na kudumisha.


## Thamani dhidi ya Marejeleo

<chapterId>bb898425-dc2f-5e5c-864b-0cb7a4a9aea9</chapterId>


JavaScript hushughulikia aina tofauti za maadili kwa njia tofauti.


Baadhi ya thamani ** zimenakiliwa** unapozikabidhi kwa kigezo.


Nyingine **zinashirikiwa** unapozikabidhi kwa kigezo kipya, kwa hivyo ukibadilisha kimoja, kingine hubadilika pia.


### Pitia thamani


Thamani inapopitishwa **kwa thamani**, JavaScript hutengeneza **nakala** yake.


Kwa hivyo ukibadilisha moja, haiathiri nyingine.


Hii hufanyika na aina za zamani, kama vile:



- nambari
- masharti
- booleans (`kweli` na `uongo`)
- `null`
- `haijafafanuliwa`


Hebu tuangalie mfano:


```javascript
let a = 5
let b = a

b = 10

console.log(a) // 5
console.log(b) // 10
```


Tulitoa `b` thamani ya `a`, lakini kisha tukabadilisha `b` hadi `10`.


Kwa kuwa nambari hupitishwa kwa thamani, JavaScript ilinakili `5` hadi `b`. `5` katika `b` ni huru kutoka kwa `5` asili katika `a` hivyo kubadilisha thamani ya `b` hakukuwa na athari kwa `a`.


Wacha tujaribu na kamba:


```javascript
let name1 = "Alice"
let name2 = name1

name2 = "Bob"

console.log(name1) // Alice
console.log(name2) // Bob
```


Tena, kubadilisha `jina2` hakujaathiri `jina1`, kwa sababu mifuatano pia hupitishwa kwa thamani.


Jambo hilo hilo hufanyika unapopitisha primitive kwa chaguo la kukokotoa: inakiliwa. Kwa hivyo kazi haiwezi kubadilisha asili.


```javascript
function plusOne(x) {
x = x + 1
}

let number = 5

plusOne(number)

console.log(number) // 5
```


Ingawa ndani ya chaguo za kukokotoa `1` iliongezwa kwa `x`, `nambari` asili haikubadilika.


Hiyo ni kwa sababu ni **nakala** pekee iliyopitishwa kwenye chaguo la kukokotoa.


### Pitia kwa kumbukumbu


Vitu hupitishwa **kwa kumbukumbu**.


Hiyo inamaanisha badala ya kuzinakili, JavaScript hupitisha tu **rejeleo** kwake, na ukiirekebisha, vijiti vingine vyote vinavyoelekeza kwake vitaona mabadiliko pia.


Kwa mfano:


```javascript
const person1 = { name: "Alice" }
const person2 = person1

person2.name = "Bob"

console.log(person1.name) // Bob
console.log(person2.name) // Bob
```


Wote `mtu1` na `mtu2` huelekeza kwenye kitu kimoja kwenye kumbukumbu.


Kwa hivyo tulipobadilisha `person2.name`, tulibadilisha pia `person1.name`, kwa sababu wote wawili wanatazama kitu kimoja.


Safu ni vitu, kwa hivyo wacha tujaribu sawa na safu:


```javascript
const list1 = [1, 2, 3]
const list2 = list1

list2.push(4)

console.log(list1) // [1, 2, 3, 4]
console.log(list2) // [1, 2, 3, 4]
```


Tulisukuma `4` kwenye `orodha2`, lakini `orodha1` iliathiriwa pia, kwa sababu zote mbili zinarejelea safu moja.


Wacha tuone kinachotokea tunapopitisha kitu kwa chaguo la kukokotoa:


```javascript
function rename(user) {
user.name = "Charlie"
}

const person = { name: "Dana" }

rename(person)

console.log(person.name) // Charlie
```


Chaguo la kukokotoa lilibadilisha kipengee! Hiyo ni kwa sababu ilipokea **rejeleo** la kitu asili cha `mtu`.


Haikupata nakala. Ilipata ufikiaji wa kitu cha asili, na kwa hiyo ilipata uwezo wa kuirekebisha.


Ni muhimu kukumbuka tofauti hii, kwa sababu vinginevyo nambari yetu inaweza kuwa tofauti na tunavyotarajia. Kwa mfano, tunaweza kuandika chaguo la kukokotoa tukitarajia kwamba halitarekebisha hoja inazopokea, na kujua baadaye kwamba ilikuwa inazirekebisha (kwa sababu zilikuwa ni vitu, kwa hivyo zilipitishwa kwa marejeleo).


## Kufanya kazi na Kazi

<chapterId>e0d277a8-c642-5af7-9e53-dee27c811967</chapterId>


Tayari umejifunza jinsi ya kutangaza na kutumia vipengele katika JavaScript. Lakini JavaScript hukupa zana zaidi za kufanya kazi na vitendaji kwa njia zenye nguvu.


### Vitendaji vya mshale


Vitendaji vya mshale ni njia fupi ya kuandika vitendaji. Badala ya kutumia neno kuu la `function`, tunatumia kishale (`=>`).


Hapa kuna kazi ya kawaida:


```javascript
function greet(name) {
return `Hello, ${name}!`
}
```


Toleo la mshale linaonekana kama hii:


```javascript
const greet = (name) => {
return `Hello, ${name}!`
}
```


Ikiwa chaguo la kukokotoa lina **mstari mmoja tu**, unaweza kuruka viunga na `kurudi`:


```javascript
const greet = (name) => `Hello, ${name}!`
```


Ikiwa chaguo la kukokotoa lina **kigezo kimoja tu**, unaweza hata kuruka mabano karibu na vigezo:


```javascript
const greet = name => `Hello, ${name}!`
```


Vitendaji vya mshale ni vya kawaida sana katika JavaScript ya kisasa, kwani huruhusu kueleza vitendaji rahisi kwa kutumia boilerplate ndogo sana.


### Vigezo chaguo-msingi


Wakati mwingine unataka chaguo la kukokotoa liwe na **thamani chaguo-msingi** ikiwa hakuna hoja itakayopitishwa.


Unaweza kufanya hivyo kama hii:


```javascript
function sayHello(name = "friend") {
console.log(`Hello, ${name}!`)
}

sayHello("Alice") // Hello, Alice!
sayHello()        // Hello, friend!
```


Thamani chaguo-msingi `"rafiki"` inatumika wakati hakuna kitu kinachopitishwa.


### Sambaza vigezo (`...`)


Je, ikiwa utendaji wako unachukua idadi inayoweza kubadilika ya hoja?


Unaweza kutumia **eneza opereta** (`...`) kuzikusanya katika safu:


```javascript
function logAll(...items) {
console.log(items)
}

logAll(1, 2, 3) // [1, 2, 3]
logAll("a", "b") // ["a", "b"]
```


Kisha unaweza kutumia kitanzi kuchakata kila kitu:


```javascript
function logEach(...items) {
for (const item of items) {
console.log(item)
}
}
```


Opereta ya kuenea ni muhimu wakati hujui ni hoja ngapi zitapitishwa.


### Vitendaji vya mpangilio wa juu


**kitendakazi cha mpangilio wa juu** ni kitendakazi ambacho:



- inachukua chaguo jingine la kukokotoa kama ingizo
- na/au hurejesha chaguo za kukokotoa kama pato


Hapa kuna mfano rahisi:


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


Hii inachapisha:


```
Hello, friend!
Hello, friend!
```


Tunaweza kupitisha kazi ya mshale kwake:


```javascript
runTwice(
() => console.log("Hello!")
)
```


Hii inachapisha:


```
Hello!
Hello!
```


Unaweza pia kuandika vitendaji ambavyo ** vinarudisha ** vitendaji vingine:


```javascript
function makeGreeter(name) {
return () => console.log(`Hi, ${name}`)
}

const greetAlice = makeGreeter("Alice")
const greetBob = makeGreeter("Bob")

greetAlice() // Hi, Alice
greetBob() // Hi, Bob
```


Kitendakazi cha `makeGreeter` ni chaguo la kukokotoa ambalo huunda vitendaji vingine. Inapokea mfuatano na kurudisha chaguo mpya la kukokotoa linalotumia mfuatano huo katika simu yake `console.log`.


Aina hii ya muundo ina nguvu sana, kwani hukuruhusu kuacha "mashimo" katika kazi zako ambazo unaweza kujaza baadaye na tabia unayohitaji.


### `ramani()`, `chujio()`, `punguza()`


JavaScript inakupa baadhi ya mbinu muhimu zilizojengewa ndani za kutumia na safu.


Njia hizi huchukua utendakazi kama hoja, kwa hivyo pia ni vitendaji vya mpangilio wa juu.


`map()` hubadilisha kila kipengee katika safu kuwa kitu kingine.


Mfano:


```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map(x => x * 2)

console.log(doubled) // [2, 4, 6]
```


Kila nambari imeongezwa mara mbili, na matokeo yake ni safu mpya.


`kichujio()` huondoa vipengee kutoka kwa safu ikiwa havijafaulu jaribio.


Mfano:


```javascript
const numbers = [1, 2, 3, 4, 5]
const numbersGreaterThanTwo = numbers.filter(x => x > 2)

console.log(numbersGreaterThanTwo) // [3, 4, 5]
```


Ni safu ya maingizo ambayo `x > 2` hurejesha hali `true` ndiyo huhifadhiwa.


`reduce()` inatumika kuchanganya vipengee vyote katika safu katika thamani moja.


Mfano:


```javascript
const numbers = [1, 2, 3, 4]
const total = numbers.reduce((current, next) => current + next)

console.log(total) // 10
```


`punguza` inapitia safu na, katika mfano huu, itatumia opereta `+` kati ya `1` na `2`, kisha kati ya `3` na `3` inayotokana, kisha kati ya `6` na `4` inayotokana, hadi iwe na jumla ya maingizo yote ya mkusanyiko (ambayo ni 10).


Unaweza kutumia `reduce()` kwa vitu vingi kama jumla, wastani, au kujenga maadili mapya hatua kwa hatua.


Mbinu hizi (`ramani`, `chujio`, `punguza`) ni zana zenye nguvu za kuchakata data bila kuandika vitanzi vya mikono.


Unaweza hata kuzichanganya katika mlolongo wa shughuli, kama hii:


```javascript
const numbers = [1, 2, 3, 4, 5]

const result = numbers
.map(n => n * 2)        // Double each entry, obtain [2, 4, 6, 8, 10]
.filter(n => n > 3) // Keep only the entries bigger than 3, so you get [4, 6, 8, 10]
.reduce((n1, n2) => n1 + n2) // Adds them: 4 + 6 + 8 + 10 = 28

console.log(result) // 28
```


## Kufanya kazi na vitu

<chapterId>7842aada-f009-5518-b8e3-1104e166a035</chapterId>


Katika sura hii, tutajifunza zana zenye nguvu na za juu zaidi za kufanya kazi na vitu katika JavaScript.


### Sifa za Kibinafsi


Wakati mwingine, tunataka kuficha sifa ya kitu ili isiweze kubadilishwa au kufikiwa kutoka nje ya kitu hicho. JavaScript inatupa njia ya kufanya hivi kwa kutumia `#` kabla ya jina la mali. Hii inaunda mali ya ** ya kibinafsi, ambayo inapatikana tu kutoka ndani ya darasa.


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


Sifa za kibinafsi zinafaa unapotaka kuzuia mabadiliko yasiyotarajiwa.


### Sifa za `tuli`


Wakati mwingine, unataka mali iwe ya darasa lenyewe, sio kwa kila kitu unachounda kutoka kwa darasa hilo. Hiyo ndiyo maana ya `static`. Mali `tuli` iko kwenye darasa na vitu vyote vya darasa hilo vitairejelea.


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


Hii ni muhimu kwa kuhifadhi data iliyoshirikiwa na mbinu zinazotumika kwa kundi zima la vitu, sio moja tu.


### `pata` na `weka`


Katika JavaScript, `get` na `set` hukuwezesha kutengeneza sifa ambazo *zinaonekana* kama vigeu vya kawaida, lakini kwa kweli endesha msimbo maalum chinichini.


Njia ya `get`ter hutumika unapojaribu *kusoma* mali. Inatangazwa kwa kuandika `pata` kabla ya mbinu iliyo na jina la mali.


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


Ijapokuwa `fullName` si sifa ya kawaida, tunaweza kuitumia kama moja, na nyuma ya pazia inaendesha kipengele cha `kupata` ili kuunda jina kamili.


Njia ya `set`ter hutumika wakati *unapokabidhi* thamani kwa mali. Inakuruhusu kudhibiti kile kinachotokea wakati mtu anajaribu kubadilisha thamani hiyo. Inatangazwa kwa kuandika `set` kabla ya mbinu iliyo na jina la mali.


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


Tunapofanya `user.fullName = "John Smith"`, huendesha mbinu ya `set` na kusasisha thamani za `firstName` na `lastName`.


Kwa hivyo ingawa inahisi kama tunaweka kitofautishi rahisi, kwa kweli tunaanzisha mantiki ambayo inasasisha mali zingine.


## Vifunguo na Maadili

<chapterId>01a397b8-c12a-5c39-82b3-6d9ebbb72a29</chapterId>


Kila mali katika kitu cha JavaScript ina **ufunguo** (pia huitwa jina la mali) na **thamani**.


Kwa mfano:


```javascript
const user = {
name: "Alice",
age: 30
}
```


Katika kifaa hiki, `"jina"` na `"umri"` ni funguo, na "Alice" na `30` ndizo thamani zake.


### Ufikiaji Nguvu


Wakati mwingine, hujui jina la mali mapema ... labda unaipata kutoka kwa pembejeo ya mtumiaji, au kuisoma kutoka kwa kutofautiana. Bado unaweza kuipata kwa kutumia **note ya mabano**, kama vile `myObject["keyName"]`.


```javascript
const user = {
name: "Alice",
age: 30
}

console.log(user["name"]) // Alice
```


Tulipitisha mfuatano `jina` kwa kitu ili kupata thamani inayolingana.


Tunaweza kuhifadhi ufunguo kwa kigezo na kuutumia kufikia thamani inayolingana baadaye, kama


```javascript
const user = {
name: "Alice",
age: 30
}

const key = "name"

console.log(user[key]) // Alice
```


### Nguvu Assignment


Unaweza pia kuunda au kusasisha sifa za kitu kwa kutumia vigeuzo kama vitufe.


```javascript
const settings = {}

const key = "theme"
settings[key] = "dark"

console.log(settings) // { theme: "dark" }
```


Hii ni muhimu unapotaka kujenga kitu hatua kwa hatua. Kwa mfano:


```javascript
const user = {}

user["username"] = "bananaFan123"
user["email"] = "banana@fruit.com"

console.log(user)
// { username: "bananaFan123", email: "banana@fruit.com" }
```


Unaweza hata kutumia kitufe cha nguvu *wakati wa kuunda* kitu kwa kutumia mabano ya mraba:


```javascript
const key = "language"
const config = {
[key]: "JavaScript"
}

console.log(config.language) // JavaScript
```


Hii inaitwa ** mali iliyohesabiwa **. Thamani iliyo ndani ya mabano ya mraba inatathminiwa, na matokeo yake hutumiwa kama ufunguo.


### Aina ya `Alama`


Kando na mifuatano, JavaScript pia hukuruhusu kutumia aina maalum inayoitwa `Alama` kama kitufe cha kitu.


Wacha tuanze na mfano rahisi:


```javascript
const id = Symbol("userID")

const user = {
name: "Bob",
[id]: 12345
}

console.log(user[id]) // 12345
```


Katika mfano huu, `id` ni Alama. Sio kamba, lakini bado inafanya kazi kama ufunguo. Ukijaribu kuweka `mtumiaji` kwenye koni, utaona hii:


```javascript
console.log(user) // { name: 'Bob', [Symbol(userID)]: 12345 }
```


Jambo lingine muhimu: kila ishara unayounda ni ya kipekee, hata ikiwa imeundwa kwa kutumia kamba sawa.


```javascript
const a = Symbol("label")
const b = Symbol("label")

console.log(a === b) // false
```


Alama hukuruhusu kufafanua funguo ambazo hazitagongana na funguo za kawaida. Kwa mfano, tuseme una kitu chenye sifa ya `jina`, lakini kipengee hicho kitabinafsishwa na mtumiaji katika siku zijazo, kwa njia ambazo huwezi kutabiri, na mtumiaji huyo anaweza kuongeza sifa ya `jina` pia. Ikiwa mali ya asili ya `jina` ilifafanuliwa kwa kamba, ingeandikwa tena na mpya, kama hii:


```javascript
const obj = {
name: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy' }
```


Ikiwa tunatumia Alama badala yake:


```javascript
const name = Symbol("name")

const obj = {
[name]: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy', [Symbol(name)]: 'John' }
```


Kama unavyoona, mali asili ya `jina` imehifadhiwa kwa njia hii. Hii inaweza kuwa na manufaa katika hali fulani za makali.


## Vitu vya Huduma

<chapterId>516e74c8-2a11-545a-a4d1-c2cabb91a273</chapterId>


JavaScript hutupatia baadhi ya vitu muhimu vilivyojengewa ndani ambavyo hutusaidia kufanya mambo kama vile utatuzi na uendeshaji wa hesabu.


### Mbinu Nyingine za `console`


Tayari umeona `console.log`, ambayo huchapisha thamani kwenye skrini.


Kuna njia zingine muhimu zinazopatikana kwenye kitu cha `console` ambazo zinaweza kukusaidia kutatua programu zako.


#### `console.onya`


Huchapisha ujumbe kwa manjano (au kwa ikoni ya onyo katika baadhi ya mazingira):


```javascript
console.warn("This is just a warning.")
```


#### `kosa.kosa`


Huchapisha ujumbe kwa rangi nyekundu, kama hitilafu:


```javascript
console.error("Something went wrong!")
```


#### `console.table`


Inaonyesha safu au kitu kama jedwali:


```javascript
const users = [
{ name: "Alice", age: 25 },
{ name: "Bob", age: 30 }
]

console.table(users)
```


Hii inachapisha jedwali kama:


```
┌─────────┬────────┬─────┐
│ (index) │  name  │ age │
├─────────┼────────┼─────┤
│    0    │ 'Alice'│  25 │
│    1    │ 'Bob'  │  30 │
└─────────┴────────┴─────┘
```


Hii inaweza kuwa muhimu kuibua data iliyopangwa.


#### `console.time` na `console.timeEnd`


Unaweza kupima muda gani kitu kinachukua:


```javascript
console.time("timer")
for (let i = 0; i < 1000000; i++) {}
console.timeEnd("timer")
```


Hii inachapisha kitu kama:


```
timer: 2.379ms
```


Inafaa kwa majaribio rahisi ya utendakazi.


### Kitu cha `Hesabu`


JavaScript hukupa kitu cha `Hesabu` chenye mbinu muhimu za kufanya hesabu.


#### `Hesabu.nasibu()`


Hurejesha nambari nasibu kati ya 0 (pamoja) na 1 (isipokuwa):


```javascript
const r = Math.random()
console.log(r)
```


Pato la mfano:


```
0.4387429859
```


#### `Math.floor()` na `Math.ceil()`



- `Math.floor(n)` huzungusha **chini** hadi nambari kamili iliyo karibu zaidi
- `Math.ceil(n)` huzungusha **juu** hadi nambari kamili iliyo karibu zaidi


```javascript
console.log(Math.floor(4.9)) // 4
console.log(Math.ceil(4.1))  // 5
```


#### `Math.round()`


Mizunguko hadi nambari kamili iliyo karibu zaidi:


```javascript
console.log(Math.round(4.4)) // 4
console.log(Math.round(4.6)) // 5
```


#### `Math.max()` na `Math.min()`


Hurejesha thamani kubwa au ndogo zaidi kutoka kwa orodha ya nambari:


```javascript
console.log(Math.max(5, 9, 3)) // 9
console.log(Math.min(5, 9, 3)) // 3
```


#### `Math.pow()` na `Math.sqrt()`



- `Math.pow(a, b)` inakupa `a` kwa uwezo wa `b`
- `Math.sqrt(n)` hukupa mzizi wa mraba wa `n`


```javascript
console.log(Math.pow(2, 3))   // 8
console.log(Math.sqrt(16))    // 4
```


# JavaScript ya hali ya juu

<partId>72c30671-ca20-5617-92a5-d5ba7aa38c93</partId>


## Makusanyo mengine

<chapterId>a9a70c6d-a343-5a46-a383-e288bc2700e3</chapterId>


JavaScript inatupa baadhi ya aina maalum za mkusanyiko ambazo huenda zaidi ya safu na vitu vya kawaida. Hizi ni pamoja na `Ramani` na `Weka`.


Zinakusaidia kuhifadhi na kudhibiti vikundi vya thamani, lakini zinafanya kazi tofauti na ulivyoona kufikia sasa.


`Ramani` ni mkusanyiko wa **jozi za thamani-ufunguo**, kama tu kitu. Lakini ina tofauti kadhaa muhimu:



- Vifunguo vinaweza kuwa **thamani yoyote** sio tu kamba.
- Utaratibu wa vitu huhifadhiwa.
- Inayo njia zilizojumuishwa za kufanya kazi nayo iwe rahisi.


Unaunda ramani mpya kama hii:


```javascript
const myMap = new Map()
```


Hii inaunda ramani tupu. Ili kuongeza maingizo kwayo, tumia `myMap.set(key, value)`:


```javascript
myMap.set("name", "Alice")
```


Hii inaongeza kitufe `"jina"` chenye thamani `"Alice"`.


Unaweza pia kutumia nambari kama ufunguo:


```javascript
myMap.set(42, "The answer")
```


Na hata kitu kama ufunguo:


```javascript
const objKey = { id: 1 }
myMap.set(objKey, "Object as key")
```


Hiyo haingefanya kazi na vitu vya kawaida, ambavyo huruhusu funguo za kamba tu.


Ili **kupata thamani**, tumia `myMap.get(key)`:


```javascript
console.log(myMap.get("name"))     // Alice
console.log(myMap.get(42))         // The answer
console.log(myMap.get(objKey))     // Object as key
```


Ili **kuangalia kama ufunguo upo**, tumia `myMap.has(key)`:


```javascript
console.log(myMap.has("name")) // true
```


Ili **kuondoa ufunguo**, tumia `myMap.delete(key)`:


```javascript
myMap.delete("name")
```


Ili **kufuta ramani nzima**, tumia `myMap.clear()`:


```javascript
myMap.clear()
```


Ramani ni nzuri kwa kudhibiti mikusanyiko mikubwa ya thamani, kwa sababu kufikia thamani kwenye ramani kubwa huwapa utendaji bora zaidi kuliko kwenye kitu kikubwa.


### `Weka`


`Kuweka` ni mkusanyiko wa **thamani pekee** (hakuna funguo), ambapo kila thamani lazima iwe **kipekee**. Hiyo ina maana:



- Huwezi kuwa na thamani sawa mara mbili
- Thamani huhifadhiwa kwa mpangilio unaoziongeza


Unaunda seti kama hii:


```javascript
const mySet = new Set()
```


Ili **kuongeza thamani**, tumia `mySet.add(value)`:


```javascript
mySet.add(1)
mySet.add(2)
mySet.add(2) // duplicate, will be ignored
```


Ingawa tulijaribu kuongeza `2` mara mbili, seti itahifadhi nakala moja pekee.


Ili **kuangalia kama thamani iko kwenye seti**, tumia `mySet.has(value)`:


```javascript
console.log(mySet.has(2)) // true
console.log(mySet.has(3)) // false
```


Ili **kuondoa thamani**, tumia `mySet.delete(thamani)`:


```javascript
mySet.delete(2)
```


Ili **kufuta kila kitu**, tumia `mySet.clear()`:


```javascript
mySet.clear()
```


`Set` ni muhimu unapotaka kuweka mkusanyiko wa thamani za kipekee bila kulazimika kuangalia mwenyewe kama kuna nakala:


```javascript
const numberArray = [1, 2, 2, 3, 4, 4, 4, 5]

const numberSet = new Set(numberArray)

console.log(numberSet) // Set(5) { 1, 2, 3, 4, 5 }
```


`Set` huepuka nakala kwa ajili yako.


## Warudiaji

<chapterId>61d24e5e-b7e4-541a-8322-778f61f26a72</chapterId>


Vitu vingi katika JavaScript ambavyo unaweza kuvifunga (kama vile safu, mifuatano, ramani, seti) ni **vinavyoweza kueleweka**: vinaweza kutoa viambatanisho kwa yaliyomo.


**kirudia** ni kifaa maalum katika JavaScript ambacho hukusaidia kupitia orodha ya vipengee **kimoja kwa wakati mmoja**.


### Virudishi vya `Kitu`


Tofauti na safu au ramani, vitu vya kawaida **haviwezi kutekelezeka** kwa `for...of`. Ukijaribu hii:


```javascript
const user = {
name: "Alice",
age: 30
}

for (const value of user) {
console.log(value)
}
```


Utapata hitilafu:


```
TypeError: user is not iterable
```


Hiyo ni kwa sababu vitu vilivyo wazi havina kiboreshaji kilichojengwa ndani. Lakini JavaScript inakupa zana zingine za kuzifunga.


#### `Object.keys()`


Unaweza kutumia `Object.keys(obj)` kupata safu ya vitufe **** vya kitu, na kisha kukitanzi juu yake:


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


Hii inachapisha:


```
name
age
```


#### `Object.values()`


Ili kuzunguka **maadili**, tumia `Object.values()`:


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


Hii inachapisha:


```
Alice
30
```


#### `Object.entries()`


Ikiwa unataka **ufunguo na thamani**, tumia `Object.entries()`:


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


Hii inachapisha:


```
name is Alice
age is 30
```


Hata ingawa vitu haviwezi kutekelezeka moja kwa moja, njia hizi hukupa ufikiaji kamili wa yaliyomo kwa njia ambayo inafanya kazi vizuri na `for...of`.


Lakini warudiaji hufanyaje kazi?


### `Alama.iterator`


Siri iliyo nyuma ya vielezi vyote ni **alama** maalum inayoitwa `Symbol.iterator`.


Alama hii ni ufunguo uliojengewa ndani unaoambia JavaScript: "Kitu hiki kinaweza kurudiwa."


Unapopiga simu `myIterable[Symbol.iterator]()`, JavaScript hukupa **kipengee cha kihariri** chenye mbinu ya `.next()`.


Wacha tuone jinsi inavyoonekana:


```javascript
const colors = ["red", "green", "blue"]

const iterator = colors[Symbol.iterator]()

console.log(iterator.next()) // { value: 'red', done: false }
```


Kila simu kwa `.next()` inakupa thamani inayofuata. Ikikamilika, inarudi:


```javascript
{ value: undefined, done: true }
```


### `ijayo()`


Mbinu ya `.next()` inatumika kupata kipengee kinachofuata kutoka kwa mlolongo.


Kila wakati unapopiga simu `.next()`, unapata kitu kilicho na vitufe viwili:



- `thamani`: kipengee cha sasa
- `imekamilika`: boolean inayokuambia ikiwa marudio yamekamilika


Wacha tufanye mfano kamili:


```javascript
const names = ["Lina", "Tom", "Eva"]      // declare an array
const iterator = names[Symbol.iterator]() // use the Symbol.iterator function to get an iterator for this array

let result = iterator.next()              // get the first element of the array

while (!result.done) {                    // repeat this loop until you reach the last element of the array, which is marked with { done: true }
console.log(result.value)               // print the value of each element
result = iterator.next()                // get the next element of the array
}
```


Hii inachapisha:


```
Lina
Tom
Eva
```


Hivi ndivyo kitanzi cha `for...of` kinavyofanya kazi chini ya kofia: kinatumia muundo huu na `.next()`.


Utapata matokeo sawa na


```javascript
const names = ["Lina", "Tom", "Eva"]

for (const result of names) {
console.log(result)
}
```


### Kufanya darasa iterable


Unaweza pia kufafanua **darasa lako linaloweza kutekelezeka** kwa kuongeza mbinu ya `[Symbol.iterator]()`.


Hebu tuseme tunataka darasa linalowakilisha **anuwai mbalimbali**, kama vile kutoka 1 hadi 5.


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


Hii inachapisha:


```
1
2
3
4
5
```


Hiki ndicho kinachotokea:



- Tulifafanua darasa `Msururu`
- Ndani ya darasa, tulitekeleza `[Symbol.iterator]()`, kwa hivyo JavaScript inajua jinsi ya kuirudia.
- Mbinu ya `ifuatayo()` inarudisha kila nambari moja baada ya nyingine
- Tunapofika `mwisho`, inarejesha `{ done: true }`


Sasa darasa letu la `Msururu` hufanya kazi kama safu, na tunaweza kulitumia katika kitanzi chochote kinachotarajia kujirudia.


### Vitendaji vya jenereta na `mavuno`


Ili kurahisisha kuunda virudishio, JavaScript hukupa **vitendaji vya jenereta**, kwa kutumia neno kuu la `function*` (ni `function` yenye `*` mwishoni) na neno kuu la `yield`.


Hebu jaribu:


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


Kila `mazao` hurejesha thamani, na **kusitisha** chaguo la kukokotoa hadi `.next()` inayofuata iitwe.


Unaweza pia kuzunguka jenereta na `for...of`:


```javascript
for (const num of numberGenerator()) {
console.log(num)
}
```


Hii inachapisha:


```
1
2
3
```


## Sambamba na kupiga simu

<chapterId>f3fc76ca-b3ef-54eb-a06e-501007002054</chapterId>


Hadi sasa, msimbo wetu umekuwa **sawazisha**: inaendesha mstari mmoja kwa wakati mmoja, kwa mpangilio. Lakini baadhi ya mambo katika ulimwengu wa kweli huchukua muda, na hatutaki programu nzima kusitisha wakati wa kusubiri.


Katika sura hii tutaleta dhana mpya: **sarafu**. Inaturuhusu kudhibiti mpangilio ambao mambo hufanywa. Hii ni muhimu wakati wa kushughulika na vitu kama vipima muda, ingizo la mtumiaji, au kusoma faili kutoka kwa diski. JavaScript inatoa zana tofauti za kufanya concurrency.


### `setTimeout`


Chaguo za kukokotoa `setTimeout` hukuwezesha **kuendesha kitendakazi baadaye**, baada ya muda kupita.


Mfano:


```javascript
console.log("Start")

setTimeout(
() => console.log("This runs after 2 seconds"),
2000
)

console.log("End")
```


Hii inachapisha:


```
Start
End
This runs after 2 seconds
```


Ingawa `setTimeout` inaonekana katikati ya msimbo, haizuii mengine. Badala yake, hupanga chaguo la kukokotoa kufanya kazi **baadaye**, na kuendelea mara moja.


`2000` inamaanisha milisekunde 2000 (ambayo ni sekunde 2).

Hapa kuna maandishi zaidi ya kitenzi na ya kirafiki zaidi ya sehemu za **Piga simu** na **Ahadi**, kwa kutumia upotoshaji wa data na ufafanuzi wazi kote:


### Simu za nyuma


**kurudisha nyuma** ni chaguo la kukokotoa tunalotoa kwa chaguo la kukokotoa lingine ili liweze kuitwa **kuitwa baadaye**.


Hebu tuangalie mfano halisi kwa kutumia namba. Fikiria tuna orodha ya nambari, na tunataka kuongeza mara mbili kila moja yao, na kisha tumia kitendakazi (kurudisha nyuma) kwa safu inayotokana ya "mara mbili", lakini tunataka kuifanya baada ya kucheleweshwa kidogo, kana kwamba tunangojea kitu polepole (kama kupakia data kutoka kwa mtandao).


Hapa kuna chaguo la kukokotoa ambalo hufanya hivyo kwa kutumia **kupiga simu tena**:


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


Hebu jaribu kutumia kipengele hiki:


```javascript
const input = [1, 2, 3]

doubleNumbers(input, function(result) {
console.log("Here is the doubled array:", result)
})
```


Baada ya sekunde 1, hii inachapisha:


```
Here is the doubled array: [ 2, 4, 6 ]
```


**Ni nini kinaendelea hapa?**


1. Tunapitisha `input` kama orodha ya nambari tunazotaka kuongeza mara mbili.

2. Pia tunapitisha kipengele cha **kitendaji cha kurudi nyuma** ambacho huambia programu nini cha kufanya *baada ya* kuongezeka maradufu.

3. Ndani ya `doubleNumbers`, tunaiga ucheleweshaji kwa kutumia `setTimeout`, kisha tunaongeza mara mbili.

4. Mara baada ya hayo, tunaita simu ya kurudi kwenye safu inayotokana ya "mara mbili".


Mbinu hii inafanya kazi, lakini fikiria unataka kufanya **hatua zaidi** baada ya hapo, kama vile kuchuja nambari ndogo na kisha kuziongeza. Utalazimika **kuorodhesha** simu zingine kama hizi:


```javascript
doubleNumbers(input, function(doubled) {
filterBigNumbers(doubled, function(filtered) {
sumNumbers(filtered, function(total) {
console.log("Final result:", total)
})
})
})
```


Hii ni Hard kusoma na fujo. Mtindo huu unaitwa **callback hell**, na ndio hasa `Promise` iliundwa kurekebisha.


## Sambamba na Ahadi

<chapterId>30fddaca-729f-5c8d-bf86-8dfc7b3c9800</chapterId>


`Ahadi` ni kitu cha JavaScript kilichojengewa ndani ambacho kinawakilisha thamani ambayo ** itakuwa tayari katika siku zijazo**.


Tunaweza kuunda Ahadi kama hii:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve("It worked!") // This means everything went OK
})
```


Sehemu ya `Ahadi mpya()` inaunda ahadi.


Ndani yake, tunaipa kazi na vigezo viwili:



- `suluhisha`, ni chaguo la kukokotoa tunaloita wakati kila kitu kimefanikiwa
- `kataa`, ni chaguo la kukokotoa tunaloliita iwapo kitu kitaenda vibaya


Katika mfano hapo juu, tunasuluhisha mara moja kwa ujumbe `"Ilifanya kazi!"`.


### `.kisha()`


Kufanya kitu **baada ya** ahadi kufanywa, tunatumia `.kisha()`:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve(100) // This means everything went OK
})

promise.then(result => {
console.log("The result is:", result)
})
```


Hii inachapisha:


```
The result is: 100
```


Thamani tuliyopitisha `resolve()` hutumwa kwa chaguo za kukokotoa ndani ya `.then()` kama `matokeo`.


Hebu tuige kazi inayochukua sekunde 2 kwa kutumia `setTimeout`:


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


Hii itasubiri sekunde 2 na kisha kuchapisha:


```
Done waiting!
```


### `kataa()`


Wacha tuunde ahadi ambayo **inashindwa**:


```javascript
const failingPromise = new Promise((resolve, reject) => {
reject("Something went wrong")
})
```


Sasa tukitumia `.basi()` kwa hili, hakuna kitakachofanyika, kwa sababu `.basi()` hushughulikia mafanikio pekee.


Ili kushughulikia makosa, tunatumia `.catch()`:


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


Hii inachapisha pekee


```
Caught an error: Something went wrong
```


Thamani iliyopitishwa kwa `reject()` inatumwa kwa chaguo za kukokotoa `.catch()`.


Hebu tujenge Ahadi ambayo **wakati fulani hufanya kazi na wakati mwingine inashindwa**, kwa kuzingatia hali fulani.


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


Sasa tunaweza kuita hii na kushughulikia kesi zote mbili:


```javascript
checkNumber(5)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Hii inachapisha:


```
Success: Positive number
```


Na ikiwa tutajaribu na nambari tofauti:


```javascript
checkNumber(-1)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Inachapa:


```
Failure: Not a positive number
```


### Uendeshaji wa minyororo kwa kutumia `Promise`s



Tunaweza kuandika upya mfano wetu wa awali kwa kutumia `Promise`, na itaonekana kuwa safi zaidi.


Wacha tuanze kwa kuandika toleo jipya la utendaji wetu wa kurudia mara mbili, lakini wakati huu, inarudisha **ahadi**:


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


Sasa tunaweza kutumia `.then()` kuwaambia JavaScript nini cha kufanya na matokeo:


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


Hii inachapisha:


```
Doubled numbers: [ 2, 4, 6 ]
```


Kufikia sasa, hii inafanya kazi sawa na toleo la kurudi nyuma, lakini sasa msimbo ni rahisi kupanua na kusoma.


Wacha tuseme tunataka kuongeza hatua zaidi:


1. Kwanza, mara mbili nambari zote

2. Kisha, ondoa nambari ndogo kuliko 4

3. Hatimaye, ongeza zote pamoja


Tunaweza kuandika kazi moja kwa kila hatua, zote kwa kutumia ahadi:


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


Sasa tunaweza **minyororo** pamoja kama hii:


```javascript
const input = [1, 2, 3]

doubleNumbers(input)
.then(filterBigNumbers)
.then(sumNumbers)
.then(
result => console.log("Final result after all steps:", result)
)
```


Hii inachapisha:


```
Final result after all steps: 10
```


Wacha tuchunguze kile ambacho hii inafanya:


1. `doubleNumbers` huongeza safu mara mbili: `[2, 4, 6]`

2. `chujioBigNumbers` huondoa chochote ≤ 3: `[4, 6]`

3. `Nambari` huongeza nambari zilizobaki: `4 + 6 = 10`

4. Hatimaye, tunachapisha matokeo.


Kila `.basi()` husubiri hatua kabla ya kumaliza. Ili tuweze kujenga **msururu wa vitendo** bila kuatamia. Hii inafanya msimbo kusomeka zaidi na rahisi kutatua.


## Sambamba na `async`/` await`

<chapterId>6e93d29f-c8bf-5fd1-a9c9-4e794ee6cbd0</chapterId>


Tuliona jinsi minyororo ya `Promise` inavyotusaidia kuepuka kuzimu ya kurudi nyuma, lakini bado wanaweza kupata Hard kidogo ya kusoma wakati kuna hatua nyingi zinazohusika.


Hapo ndipo `async` na `ait` huingia. Zinaturuhusu tuandike msimbo usiolingana **unaoonekana kama msimbo unaosawazishwa**, ambao hurahisisha kuelewa.


### `async` ni nini?


Unapoandika neno kuu `async` kabla ya chaguo za kukokotoa, JavaScript hufunga kiotomatiki thamani ya kurejesha kipengele cha kukokotoa kwenye Ahadi.


Hebu tuone mfano wa msingi:


```javascript
async function greet() {
return "hello"
}
```


Ukiita kipengele hiki:


```javascript
const result = greet()
console.log(result)
```


Utaona hii:


```
Promise { 'hello' }
```


Ingawa umerudisha tu kamba, JavaScript inakugeuza kuwa Ahadi kwako. Unaweza kupata thamani halisi kwa kutumia `.then()` kama hii:


```javascript
greet().then( result => console.log(result) ) // prints "hello"
```


Au unaweza kutumia `kusubiri`...


### `kusubiri` ni nini?


Neno kuu `kusubiri` linaambia JavaScript: "subiri hadi Ahadi hii ikamilike, kisha unipe matokeo."


Lakini unaweza tu kutumia `kusubiri` **ndani ya kitendakazi kisichosawazisha**.


Hebu tuandike tena mfano kwa kutumia `kusubiri`:


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


Sasa tunaweza kutumia matokeo kana kwamba ni thamani ya kawaida.


Hebu tufanye jambo la manufaa zaidi sasa.


### Inaiga ucheleweshaji kwa `await`


Tutaunda kitendakazi rahisi cha `kusubiri` ambacho huchukua wingi wa milisekunde kama hoja na kusuluhisha tu baada ya milisekunde nyingi, bila kufanya chochote kingine:


```javascript
function wait(ms) {
return new Promise(resolve => {
setTimeout(resolve, ms)
})
}
```


Wacha tujaribu kuitumia:


```javascript
async function test() {
console.log("waiting 2 seconds...")
await wait(2000)
console.log("done waiting")
}

test()
```


Hii inachapisha:


```
waiting 2 seconds...
done waiting
```


Unaweza kufikiria `kungoja` kama "tulia hapa hadi ahadi ikamilike, kisha uendelee."


Hii hukuruhusu kuandika msimbo kwa mtindo wa **juu-hadi-chini** ambao hufanya kazi kwa usawa, bila kuunganisha simu za `.then()`.


### Inasubiri data


Hebu tutumie tena mfano wetu wa awali, ambapo tunaweka nambari mara mbili, kisha tuchuje, kisha tujumlishe. Lakini wakati huu, tutatumia `async`/`await`.


Tutaunda vipengele 3 vinavyoiga kusubiri, na kurudisha Ahadi:


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


Sasa hebu tuandike kitendakazi cha `async` ili kuzichanganya:


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


Hii inachapisha:


```
Final result: 10
```


Hii ni rahisi kusoma kuliko kuweka minyororo `.then()` au kurudisha nyuma kiota.


Inaonekana kama mpango wa hatua kwa hatua wa kawaida, lakini bado unafanya kazi kwa usawa.


## Async Iterators

<chapterId>438b037d-9931-56d7-9052-7b4470f3c75b</chapterId>


Tayari umejifunza kuhusu **virudishi** na jinsi tunavyoweza kutumia `kwa...ya` kuzunguka safu na vitu vingine vinavyoweza kutekelezeka.


Lakini vipi ikiwa data tunayotaka kurudia itachukua muda kufika?


Wakati mwingine tunataka kuzunguka mambo yanayofika **asynchronously**, kama vile ujumbe kutoka kwa gumzo, mistari kutoka kwa faili, au nambari kutoka kwa chanzo polepole.


Ili kufanya hivyo, JavaScript inatupa **virudishi vya async**.


### Kazi za jenereta za Async


Njia rahisi zaidi ya kuunda kiboreshaji kisichosawazisha ni kutumia **kazi ya jenereta isiyosawazishwa**.


Tunaandika hivi:


```javascript
async function* generateNumbers() {
yield 1
yield 2
yield 3
}
```


Hii inaonekana kama jenereta ya kawaida, lakini ikiwa na `async` kabla yake.


Sasa tunaweza kutumia `for wait...of` kutumia maadili:


```javascript
async function run() {
for await (const n of generateNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


Hii itachapisha:


```
Got number: 1
Got number: 2
Got number: 3
Done!
```


Kwa hivyo ni tofauti gani na jenereta ya kawaida?


Tofauti ni: sasa tunaweza kutumia `await` ndani ya jenereta.


Wacha tufanye msaidizi wa kuchelewesha tena:


```javascript
function wait(ms) {
return new Promise(resolve => setTimeout(resolve, ms))
}
```


Sasa hebu tutoe nambari **polepole**:


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


Jaribu kuitumia:


```javascript
async function run() {
for await (const n of generateSlowNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


### Kwa nini utumie viboreshaji vya async?


Async iterators ni muhimu wakati:



- Thamani hazifiki zote mara moja.
- Unataka kuzishughulikia moja baada ya nyingine, **zinapokuja**.
- Unafanya kazi na Ahadi, na unataka kuzunguka kwa njia safi.


Kwa mfano, ikiwa ungependa kupakia ujumbe kutoka kwa seva ya gumzo moja baada ya nyingine, au kupakua faili kubwa katika vipande, viambatanisho vya async hukupa njia ya kuandika kitanzi cha `for` kinachofanya kazi na data iliyochelewa.


### `Symbol.asyncIterator`


Tunaweza pia kutumia viboreshaji vya async katika madarasa maalum.


Hapa kuna mfano ambao hutoa nambari kwa kucheleweshwa:


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


Sasa tunaweza kutumia `kwa kusubiri...ya` kama hapo awali:


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


Hii hukuruhusu kuunda vitu ambavyo vinaweza kurudiwa kwa usawa


## Assignment sukari ya syntax

<chapterId>8b1ba7d8-ecfd-5470-b86e-73cb84ccc8b7</chapterId>


"Sukari ya sintaksia" inamaanisha kuandika kitu kwa njia fupi au rahisi, bila kubadilisha kile kinachofanya. Ni njia nzuri zaidi ya kusema kitu sawa.


JavaScript ina sukari ya sintaksia iliyojengewa ndani ambayo inaturuhusu tuandike matamko safi na mafupi. Katika sura hii, tutaangalia jinsi ya kugawa maadili kulingana na hali, kusasisha vigezo na hesabu, kuvuta maadili kutoka kwa safu au vitu, na kunakili au kuchanganya na syntax rahisi.


### Opereta wa Ternary


Katika JavaScript, unaweza kupeana thamani kulingana na hali kwa kutumia **opereta wa tatu**, ambayo ni njia fupi ya kuandika `kama...ingine`.


Badala ya kufanya:


```javascript
let message

if (isMorning) {
message = "Good morning"
} else {
message = "Hello"
}
```


Unaweza kuandika:


```javascript
const message = isMorning ? "Good morning" : "Hello"
```


Hii ina maana:



- Ikiwa `isMorning` ni kweli, tumia `"Habari za asubuhi"`
- Vinginevyo, tumia `"Hujambo"`


Fomu ya jumla ni:


```javascript
condition ? valueIfTrue : valueIfFalse
```


Unaweza kuitumia ndani ya misemo mingine pia:


```javascript
console.log(isSunny ? "Go outside" : "Stay in")
```


Hakikisha unaitumia kwa maamuzi **rahisi**. Ikiwa mantiki ni changamano, shikilia na `kama...ingine`.


### Waendeshaji Mbadala wa Assignment


JavaScript ina **viendeshaji vya njia ya mkato** vya kufanya kazi pamoja na uendeshaji.


Wacha tuangalie njia ya kawaida:


```javascript
let counter = 1
counter = counter + 1
```


Hii inaweza kufupishwa kwa:


```javascript
let counter = 1
counter += 1 // same as counter = counter + 1
```


Hapa kuna zile za kawaida zaidi:


| Operator | Meaning             |
| -------- | ------------------- |
| `+=`     | add and assign      |
| `-=`     | subtract and assign |
| `*=`     | multiply and assign |
| `/=`     | divide and assign   |

Mifano:


```javascript
let score = 10
score += 5  // now score is 15
score *= 2  // now score is 30
score -= 10 // now score is 20
```


Hizi ni muhimu unapotaka kusasisha kigezo kwa kutumia thamani yake.


### Kuharibu


**Kuharibu** hukuruhusu kuchukua thamani kutoka kwa safu au vitu na kuzihifadhi katika vigeuzo kwa urahisi.


#### Safu


Tuseme una:


```javascript
const colors = ["red", "green", "blue"]
```


Badala ya kufanya:


```javascript
const first = colors[0]
const second = colors[1]
```


Unaweza kufanya:


```javascript
const [first, second] = colors
```


Hii inapeana:



- `kwanza` hadi `"nyekundu"`
- `pili` hadi `"Green"`


Unaweza kuruka maadili pia:


```javascript
const [,, third] = colors
console.log(third) // blue
```


#### Vitu


Unaweza kutoa maadili kutoka kwa vitu pia:


```javascript
const user = { name: "Alice", age: 30 }

const { name, age } = user
console.log(name) // Alice
console.log(age)  // 30
```


Ikiwa mali hiyo ina jina tofauti na lahaja unayotaka, unaweza kuipatia jina:


```javascript
const { name: username } = user
console.log(username) // Alice
```


Uharibifu hufanya msimbo wako kuwa safi wakati wa kufanya kazi na vitu na safu.


### Sambaza Sintaksia


**Sintaksia iliyoenea** hutumia `...` kufungua au kunakili thamani.


#### Safu


Unaweza kunakili au kuunganisha safu:


```javascript
const a = [1, 2]
const b = [3, 4]

const both = [...a, ...b]
console.log(both) // [1, 2, 3, 4]
```


Unaweza pia kuunda safu:


```javascript
const original = [10, 20, 30]
const clone = [...original]
```


#### Vitu


Unaweza kufanya vivyo hivyo na vitu:


```javascript
const a = { x: 1 }
const b = { y: 2 }

const merged = { ...a, ...b }
console.log(merged) // { x: 1, y: 2 }
```


Unaweza pia kubatilisha maadili:


```javascript
const user = { name: "Alice", age: 30 }
const updated = { ...user, age: 31 }

console.log(updated) // { name: "Alice", age: 31 }
```


Hii ni muhimu sana wakati wa kusasisha vitu bila kubadilisha asili.


# NodeJS

<partId>42fe4d49-dace-5135-bb9e-b9d75034fb2a</partId>


## Tulifikaje kwenye Node

<chapterId>0da1d60c-06c9-54e6-a181-ae7dabf6e3b8</chapterId>


Katika sura hii tutajifunza muktadha mdogo wa kihistoria kuhusu JavaScript na NodeJS.


Muktadha wa kihistoria ni muhimu sana katika programu, kwa sababu mara nyingi tunatumia zana zilizoundwa na watu wengine, na kwa hivyo tunaathiriwa na maamuzi waliyochukua hapo awali.


Kuelewa sababu ya maamuzi hayo, na jinsi zana tunazotumia zilivyokuja kuwa jinsi zilivyo, kutatusaidia kuhisi kuchanganyikiwa kidogo kuhusu kile tunachofanya.


### Asili ya JavaScript


JavaScript ilianza kama lugha rahisi iliyoundwa kufanya kurasa za wavuti kuingiliana.


Katika miaka ya 1990, vivinjari vya wavuti kama vile Netscape Navigator viliongeza JavaScript ili wasanidi programu waweze kuandika msimbo unaoendeshwa moja kwa moja kwenye kivinjari.


Wazo la asili lilikuwa kuwa na Java kama lugha ya msingi ya kutengeneza tovuti (na ile inayoitwa "applet za Java"), na JavaScript kwa vitu vidogo tu.


Muundo wa kimsingi ulifanywa na Brendan Eich, ambaye wakati huo alikuwa mfanyakazi katika Netscape, chini ya wiki 2.


Lakini watu wengi walipendelea kutumia JavaScript hadi Java, na pia programu-jalizi za Java zilikuwa na maswala kadhaa ya usalama wakati huo, kwa hivyo hatimaye Java iliondolewa kama chaguo na JavaScript ikawa kiwango cha ukweli cha ukuzaji wa wavuti.


### Injini ya V8


JavaScript ni lugha iliyotafsiriwa, tofauti na lugha zilizokusanywa kama C.


Nambari iliyoandikwa katika lugha iliyokusanywa hubadilishwa kuwa ya jozi, na binary hulishwa moja kwa moja kwa CPU ya kompyuta.


![](assets/en/6.webp)


Lugha zinazofasiriwa, kwa upande mwingine, zinaelekea kuwa rafiki zaidi kwa watumiaji, na ziko karibu na jinsi wanadamu wanavyofikiri ("kiwango cha juu") badala ya jinsi mashine zinavyofanya kazi ("kiwango cha chini"); kwa hivyo huwa na mashine ya kawaida iliyojengwa ili kuendesha nambari zao.


Mashine pepe ni programu maalum ambayo hukaa kati ya msimbo unaoandika na CPU, na kutekeleza msimbo wako (kwa sababu CPU haiwezi kuuelewa).


Hii inakuwezesha kupanga bila kujua mengi kuhusu mashine ya msingi, lakini pia ina gharama katika suala la utendaji, kwa sababu kompyuta haifanyi programu yako tu; inaendesha programu (mashine pepe) inayoendesha programu yako.


Kadiri programu za wavuti zilivyozidi kuwa ngumu, kulikuwa na mahitaji ya kuboresha utendaji wa JavaScript. Injini ya V8 ndiyo mkalimani anayewezesha JavaScript katika Google Chrome. Iliundwa huko Google na kutolewa mnamo 2008.


Ingawa injini za zamani za JavaScript zilikuwa mashine pepe za kitamaduni, injini ya V8 ni mkusanyaji wa JIT (kwa wakati tu).


Nambari ya JavaScript inalishwa kwa injini ya V8, na injini inajaribu kukusanya sehemu zake kama jozi asili kwenye nzi. Hii hukuruhusu kuwa na matumizi ya lugha ya kiwango cha juu, yenye utendakazi unaokaribiana kidogo na lugha za kiwango cha chini. Hii imefanya JavaScript kuwa lugha ya kiwango cha juu zaidi ulimwenguni, kitu "bora zaidi ya walimwengu wote".


### Wakati wa kukimbia wa NodeJS


Ingawa ilikuwa rahisi kutumia na haraka sana kutekeleza, baada ya kutolewa kwa JavaScript ya V8 iliendelea kuwa na kizuizi kikubwa: inaweza tu kukimbia ndani ya kivinjari.


Kwa nini hilo ni tatizo?


Naam, kwa kuwa vivinjari hutekeleza msimbo ulioletwa kutoka kwa mamilioni ya vyanzo tofauti kwenye mtandao, vinaweza kujiingiza kwa urahisi kwenye programu hasidi, kwa hivyo "zimesasishwa" kutoka kwa mfumo mwingine wa uendeshaji.


![](assets/en/7.webp)


JavaScript haikuweza kufikia mfumo wa faili na rasilimali zingine za ndani kwenye kompyuta yako (angalau si kwa urahisi kama lugha zingine zingeweza), kwa hivyo hiyo ilikuwa kizuizi kikubwa juu ya aina ya programu ambazo unaweza kuunda nayo.


Mnamo 2009, Ryan Dahl alichapisha NodeJS, ambayo ni wakati wa kukimbia ambao hukuruhusu kutumia injini ya V8 nje ya kivinjari, moja kwa moja kwenye mfumo asili wa uendeshaji wa kompyuta yako. Pia inaongeza vipengele vingi ambavyo ni muhimu kwa kuandika programu za upande wa seva na mstari wa amri. Kwa mfano, unaweza kutumia NodeJS kuunda seva ya wavuti, kusoma na kuandika faili, au kuunda zana zinazofanya kazi kiotomatiki.


![](assets/en/8.webp)


Katika kozi hii hadi sasa, tumechunguza vipengele vya JavaScript ambavyo vipo kwenye kivinjari na katika NodeJS. Vipengele hivyo vilituruhusu kufafanua data na kuibadilisha kwa njia dhahania. Katika masomo machache yanayofuata, tutachunguza vipengele ambavyo ni mahususi kwa NodeJS na kuturuhusu kuingiliana na mfumo wa uendeshaji.


## Hoja za mstari wa amri

<chapterId>960d20f3-c424-5d51-a041-ef17d2e94b6d</chapterId>


NodeJS inaturuhusu, kati ya mambo mengine, kujenga CLIs (Violesura vya Mstari wa Amri).


Kwa hilo tunahitaji njia ya kupokea hoja za mstari wa amri, ambayo katika Node hufanywa kwa kutumia kitu cha `process` kilichojengwa.


### `mchakato`


NodeJS hutoa kitu maalum kinachoitwa `mchakato` ambacho kinawakilisha programu inayoendesha sasa.


Unaweza kuitumia kukagua mazingira, saraka ya sasa ya kufanya kazi, na hata kutoka kwa programu inapohitajika.


Kwa mfano:


```javascript
console.log(process.platform)
```


Hii huchapisha jukwaa la mfumo wa uendeshaji, kama vile `win32`, `linux`, au `darwin` (Mac).


### `mchakato.argv`


Unapoendesha programu ya NodeJS kutoka kwa terminal, unaweza kupitisha maneno ya ziada (hoja) baada ya jina la hati. Hizi zimehifadhiwa katika `process.argv`.


Kwa mfano, ikiwa utaendesha amri hii:


```
node my_script.js alpha beta
```


Unaweza kuchapisha hoja kama hii:


```javascript
console.log(process.argv)
```


Matokeo yanaweza kuonekana kama hii:


```
[ '/path/to/node', '/path/to/my_script.js', 'alpha', 'beta' ]
```


Vitu viwili vya kwanza daima ni njia ya Node na njia yako ya hati. Maneno yoyote ya ziada uliyopitisha kwenye hati huja baada ya hapo.


Safu ya `process.argv` inaweza kukatwa kama safu nyingine yoyote kwa kutumia mbinu ya `.slice()`, kwa hivyo ili kupata tu hoja zilizopitishwa unaweza kufanya.


```javascript
const args = process.argv.slice(2)

console.log(args)
```


Kuwa na idhini ya kufikia hoja ambazo mtumiaji anapitisha ni jambo la msingi katika kutengeneza programu za mstari wa amri.


## Moduli

<chapterId>4e1651a5-65fd-50bc-b22a-40313d5659ca</chapterId>


Nyakati za utekelezaji za JavaScript kama NodeJS kawaida huchukulia kila faili ya JavaScript kama moduli tofauti.


Fikiria moduli kama sanduku. Sanduku lina nafasi yake ya kibinafsi, hivyo vigezo na kazi ulizotangaza ndani yake haziingiliani na msimbo katika masanduku mengine. Kimsingi, kila moduli ina wigo wake mwenyewe.


Moduli inaweza kuhamisha baadhi ya maudhui yake, na kuifanya ipatikane kwa moduli nyingine, na inaweza kuagiza maudhui ambayo moduli nyingine zimesafirisha. JavaScript hukuruhusu kusafirisha na kuagiza yaliyomo kati ya moduli, ili kuunganisha faili tofauti.


Programu ya JavaScript mara nyingi huundwa na moduli nyingi, ambazo zimeunganishwa na kila mmoja.


Kwa nini utumie moduli? Kwa kugawanya msimbo wako katika moduli, unaweza kupanga programu yako katika sehemu ndogo zaidi, zilizo wazi zaidi na zinazoweza kutumika tena. Kila sehemu inaweza kuzingatia aina moja tu ya kazi, kama vile kushughulikia hesabu za hesabu, kufanya kazi na faili au kupanga maandishi.


### Moduli za CommonJS


Katika NodeJS, mfumo wa kawaida wa kudhibiti moduli unaitwa **CommonJS**.


Katika mfumo huu, unaweza kushiriki (kusafirisha) msimbo kutoka kwa moduli kwa kutumia `module.exports` na kuipakia (kuagiza) katika faili nyingine kwa kutumia `require()`.


Ili kufanya kitu kipatikane nje ya moduli, unaikabidhi kwa `module.exports`:


```javascript
const greeting = "Hello!"

module.exports = greeting
```


Hapa, mfuatano `"Hujambo!"` ndio moduli hii inasafirisha.


Ili kutumia nambari iliyosafirishwa kutoka kwa faili nyingine, unatumia `require()` kazi na njia ya faili hiyo:


```javascript
const greeting = require("./greeting.js")

console.log(greeting)
```


Hii inachapisha:


```
Hello!
```


Unaweza kuhamisha vitu vingi kwa kuviunganisha pamoja katika kitu kisichojulikana, kama vile


```javascript
const greeting1 = "hello"

const greeting2 = "hi"

module.exports = {
greeting1, greeting2
}
```


CommonJS ulikuwa mfumo wa moduli ambao hapo awali ulipitishwa na NodeJS. Baadaye moduli za ES pia ziliongezwa.


### Moduli za ES


NodeJS pia inasaidia aina nyingine ya moduli inayoitwa **Moduli za ES**, ambazo ni maarufu katika ukuzaji wa wavuti. Wanatumia maneno muhimu `export` na `import`.


Moduli za ES zilitengenezwa kwa ajili ya kivinjari na baadaye ziliongezwa kwenye Node. Ukitaka kuzitumia, huenda ukalazimika kutumia `.mjs` kama kiendelezi cha faili badala ya `.js`, kulingana na toleo la Node unalotumia.


Katika faili moja inayoitwa `greeting.mjs` tunaandika


```javascript
export const greeting = "Hello!"
```

Kama unavyoona, tunasafirisha mara kwa mara moja kwa moja pale inapofafanuliwa


Katika faili nyingine inayoitwa `index.mjs`, tunaiingiza:


```javascript
import { greeting } from "./greeting.mjs"

console.log(greeting)
```


Unaweza kuhamisha matamko tofauti katika sehemu tofauti za faili, kama


```javascript
export const num = 10

export function double (x) {
return x*2
}
```


### Maktaba ya kawaida ya NodeJS


NodeJS pia inajumuisha moduli nyingi zilizojengwa. Hizi ni moduli zilizotengenezwa tayari zinazotolewa na NodeJS ambazo husaidia kwa kazi za kawaida kama vile kusoma faili, kufanya kazi na mfumo wa uendeshaji, au kuunganisha kwenye mtandao.


Kwa mfano, moduli ya `os` hukupa taarifa kuhusu mfumo wako wa uendeshaji:


```javascript
const os = require("os")

console.log(os.platform())
```


Sio lazima usakinishe moduli hizi zilizojengwa, zinakuja na NodeJS. Zinaunda "maktaba ya kawaida" ya wakati wa kutekelezwa, na hutumiwa na programu nyingi za Node kufanya mambo kama vile kusoma faili au kuwasiliana kupitia mtandao.


Sura zinazofuata zitakuonyesha baadhi ya mifano muhimu ya matumizi yao.


## Moduli ya `fs`

<chapterId>911e953a-35ae-5ee7-bd74-372501c32e81</chapterId>


Moduli ya `fs` (fupi kwa **mfumo wa faili**) ni sehemu ya maktaba ya kawaida ya NodeJS. Inakuruhusu kufanya kazi na faili na saraka kwenye kompyuta yako: unaweza kusoma faili, kuandika faili, kuzifuta, kuzibadilisha, na zaidi.


Ili kuitumia, kwanza unahitaji kuiingiza juu ya faili yako:


```javascript
const fs = require("fs")
```


### API ya Usawazishaji


Njia rahisi zaidi ya kutumia `fs` ni kwa njia zake **sync**.


Njia hizi huzuia programu hadi kumaliza (kwa hivyo mstari unaofuata wa nambari haifanyi kazi hadi operesheni imekamilika).


Hapa kuna mfano wa kusoma faili kwa usawa:


```javascript
const fs = require("fs")

const data = fs.readFileSync("example.txt", "utf8")

console.log(data)
```


Ikiwa kuna faili inayoitwa `example.txt` katika saraka sawa na hati yako, hii itachapisha yaliyomo.


Unaweza pia kuandika kwa faili kwa usawa:


```javascript
const fs = require("fs")

fs.writeFileSync("output.txt", "Hello from Node!")

console.log("File written!")
```


Hii huunda (au kubatilisha) faili inayoitwa `output.txt` yenye maandishi.


Hapa kuna shughuli za kawaida unaweza kufanya na API hii:


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


API ya Usawazishaji ni rahisi na nzuri kwa hati ndogo, lakini kwa sababu inazuia programu hadi ikamilike, inaweza kupunguza kasi ikiwa unafanya kazi na faili kubwa au seva.


### Callback async API


**API ya kurudi nyuma** haizuii: inairuhusu NodeJS kuendelea kufanya mambo mengine wakati operesheni ya faili inafanyika.


Badala ya kurudisha matokeo moja kwa moja, inachukua kitendakazi (****) ambayo huitwa operesheni inapofanywa.


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


Hiki ndicho kinachotokea:



- `fs.readFile` inaanza kusoma `example.txt`.
- NodeJS haisubiri, inasonga mbele ili kutekeleza nambari nyingine ambayo unaweza kuwa umeandika.
- Wakati faili imekamilika kusoma, kurudi nyuma huendesha:



  - Ikiwa kulikuwa na hitilafu, `err` ina hitilafu.
  - Vinginevyo, `data` ina yaliyomo.


Hivi ndivyo unavyoandika kwa faili:


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


Wazo sawa: mpango hauacha wakati wa kuandika faili.


Baadhi ya mifano ya mambo unaweza kufanya na API hii:


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


API ya kurudisha nyuma ni bora kwa seva na kazi kubwa kwa sababu haizuii programu, lakini urejeshaji simu uliowekwa kwenye kiota unaweza kupata fujo ikiwa utaratibu shughuli nyingi. Ndio maana API ya async yenye msingi wa ahadi iliongezwa.


### Promise async API


API ya Promise-based ni ya kisasa na inafanya kazi vizuri na `.then()` na `async/await`. Inapatikana kama `fs.promises`.


Unahitaji kuingiza mali ya `ahadi`:


```javascript
const fs = require("fs").promises
```


Kwa kutumia `.kisha()`:


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


Au bora zaidi, kwa kutumia `async/ait`:


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


Kuandika kwa faili:


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


Orodha ya kawaida ya mifano ya API:


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


Unapoandika msimbo , mara nyingi utahitaji kutumia msimbo ulioandikwa na watu wengine; kwa mfano, maktaba za kukusaidia kufanya kazi na tarehe, rangi, seva, au karibu kitu kingine chochote.


Badala ya kupakua na kunakili faili mwenyewe, unaweza kutumia **kidhibiti kifurushi**.


Meneja wa kifurushi ni zana ambayo:



- vifurushi vya kupakua
- hufuatilia ni vifurushi vipi ambavyo mradi wako unahitaji
- huhakikisha kuwa kila mtu kwenye timu yako ana matoleo sawa ya vifurushi


### NPM ni nini


Katika ulimwengu wa NodeJS, meneja maarufu wa kifurushi ni **NPM**, ambayo inawakilisha *Kidhibiti cha Kifurushi cha Node*.


Unapata NPM kiotomatiki unaposakinisha NodeJS.


Unaweza kuangalia ikiwa unayo NPM kwa kuendesha hii kwenye terminal yako:


```
npm -v
```


Hii inachapisha toleo la NPM ulilonalo, kama vile:


```
10.2.1
```


### Kuunda kifurushi


Katika NodeJS, **furushi** ni saraka tu iliyo na faili ya `package.json` ndani yake.


Wacha tuunde hatua moja kwa hatua.


1. Tengeneza folda mpya ya mradi wako:


```
mkdir my_project
cd my_project
```


2. Tekeleza amri hii:


```
npm init
```


Hii itaanzisha usanidi shirikishi, ikikuuliza maswali kama vile jina la mradi wako, toleo, maelezo, n.k.


Ikiwa hutaki kujibu kila kitu na ukubali tu chaguo-msingi, unaweza kutumia:


```
npm init -y
```


Baada ya kuiendesha, utaona faili mpya kwenye folda yako inayoitwa:


```
package.json
```


### `kifurushi.json`


Faili ya `package.json` ni faili ya JSON inayohifadhi metadata kuhusu mradi wako.


Hapa kuna mfano:


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


Maeneo machache muhimu:



- `jina`: jina la kifurushi chako
- `toleo`: toleo la sasa
- `kuu`: faili ya mahali pa kuingilia (kama `index.js`)
- `scripts`: amri unaweza kuendesha (kama `npm start`)
- `dependencies`: huorodhesha vifurushi vyote ambavyo mradi wako unategemea


### Kufunga kifurushi


Hebu tuseme unataka kutumia kifurushi fulani kiitwacho `picocolors` kuongeza rangi kwenye toleo lako la mwisho.


Unaweza kuisakinisha kwa kuendesha:


```
npm install picocolors
```


Sasa unaweza kuitumia katika mradi wako. Tengeneza faili ya `index.js` na


```javascript
const pico = require('picocolors')

console.log(
pico.green("This text is green!")
)
```


na jaribu kuiendesha. Terminal inapaswa kuchapisha toleo la rangi la maandishi.


NPM ilifanya nini?



- Ilipakua kifurushi na kukihifadhi kwenye folda ndogo inayoitwa `node_modules/`
- iliongeza ingizo chini ya `dependencies` kwenye `package.json` yako
- ilisasisha faili ya `package-lock.json`


`Package-lock.json` ni nini?


### `kifurushi-kufuli.json`


Faili hii imeundwa kiotomatiki na NPM.


Unaweza kujiuliza, ikiwa tayari tuna `package.json`, kwa nini tunahitaji faili nyingine?

Hii ndio sababu:



- `package.json` inasema tu ni toleo gani **masafa** ya kifurushi kinachohitaji mradi wako.

Mfano:


```json
"dependencies": {
"picocolors": "^1.1.0"
}
```


`^1.1.0` inamaanisha "toleo lolote linalooana na 1.1.x", kwa hivyo linaweza kunyumbulika.



- `package-lock.json` **husimamisha** matoleo kamili ya kila kifurushi kimoja na vitegemezi vyake vidogo, ili kila mtu anayesakinisha mradi wako apate usanidi sawa wa kufanya kazi.


Kwa nini hili ni muhimu?


Ikiwa unafanya kazi kwenye timu, au utapeleka mradi wako kwa seva, au utakuja tena katika siku zijazo, ungependa kuhakikisha kuwa bado unafanya kazi kwa njia ile ile.

Ikiwa vifurushi vimesasishwa na ukisakinisha tena bila faili ya kufuli, unaweza kupata toleo tofauti kidogo ambalo linafanya kazi kwa njia tofauti.


Kwa kuweka `package-lock.json` katika mradi wako, NPM itasakinisha matoleo kamili yaliyoorodheshwa hapo kila wakati, na kuhakikisha kuwa kila mtu ana mazingira sawa.


`package-lock.json` hufunga kila kitu kwa toleo mahususi, ili kufanya mradi uweze kuzaliana zaidi kwenye mashine zingine.


Lakini ikiwa kifurushi chako kinahitaji kutumiwa na watu wengi, badala yake unaweza kuchagua kutokifanya, ili NPM ipate faili ya `package.json` tu na inaruhusiwa kusakinisha matoleo mapya zaidi ambayo yanaruhusiwa katika faili hiyo kiotomatiki.


Lakini haya ni mambo unapaswa kuwa na wasiwasi kuhusu baadaye, mara tu unapoanza kuchapisha msimbo wako mwenyewe. Kwa sasa, tulianzisha misingi ya NPM ili kukuruhusu kupata na kutumia maktaba zilizochapishwa na wasanidi programu wengine katika miradi yako.



## Mtandao katika NodeJS

<chapterId>f2cabd8b-754b-5c97-8d6a-8412a9a184c7</chapterId>


NodeJS hutumiwa mara nyingi kama lugha ya nyuma: unaweza kubadilisha hati yako kuwa seva, na pia kuitumia kufanya maombi kwa seva zingine.


Katika sura hii tutaanzisha vipengele vya msingi vya mtandao ambavyo vitakuruhusu kufanya hivyo.


### `chota()`


Ikiwa unataka programu yako kupakua data kutoka kwa tovuti au API, unahitaji kutuma ombi la **HTTP**.


Katika matoleo ya kisasa ya NodeJS, unaweza kutumia kitendakazi cha `fetch()` kilichojengewa ndani.


Hapa kuna mfano wa kufanya ombi la GET kwa API:


```javascript
const response = await fetch("https://jsonplaceholder.typicode.com/posts/1")
const data = await response.text()

console.log(data)
```


Unapoendesha hii, utaona kitu kama:


```
{
"userId": 1,
"id": 1,
"title": "...",
"body": "..."
}
```


Hiki ndicho kinachotokea:


1. `chota()` huchukua URL na kutuma ombi.

2. Hurejesha **Ahadi** ambayo hutatuliwa kwa kitu cha `Jibu`.

3. `response.text()` husoma mwili wa majibu kama mfuatano.


Lakini kamba unapata nyuma ni JSON. Hiyo ni nini?


### JSON


Unapofanya kazi na API za wavuti, data mara nyingi hutumwa na kupokewa kama **JSON**, ambayo inawakilisha Hati ya Kitu cha JavaScript.


JSON ni umbizo la maandishi linalofanana sana na vipengee vya JavaScript. Kwa mfano:


```json
{
"name": "Alice",
"age": 30,
"likes": ["apples", "bananas"]
}
```


Kitu cha `JSON` ni matumizi yaliyojengewa ndani katika JavaScript ambayo yanaweza kutumika kufanya kazi na umbizo hili la data.


Unaweza kubadilisha kitu cha JavaScript kuwa mfuatano wa JSON ukitumia `JSON.stringify()`:


```javascript
const user = { name: "Alice", age: 30 }

const jsonString = JSON.stringify(user)

console.log(jsonString)
```


Hii inachapisha:


```
{"name":"Alice","age":30}
```


Unaweza pia kubadilisha maandishi ya JSON kuwa kitu cha JavaScript kwa kutumia `JSON.parse()`:


```javascript
const jsonText = '{"name":"Bob","age":25}'

const obj = JSON.parse(jsonText)

console.log(obj)
```


Hii inachapisha:


```
{ name: 'Bob', age: 25 }
```


Kuwa mwangalifu: `JSON.parse()` itatupa hitilafu ikiwa mfuatano si sahihi wa JSON.


```javascript
JSON.parse("not json") // ❌ Error!
```


Kwa hivyo hakikisha kuwa kamba imeumbizwa vizuri.


### Seva ya `http`


NodeJS hukuruhusu kuunda seva ya wavuti bila kusakinisha kitu kingine chochote.


Unaweza kutumia moduli iliyojengewa ndani ya `http` kushughulikia maombi kutoka kwa wateja na kutuma majibu tena.


Hapa kuna mfano wa msingi sana:


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


Unapoendesha hati hii na kufungua `http://localhost:3000` kwenye kivinjari chako, utaona:


```
Hello from NodeJS server!
```


Hiki ndicho kinachotokea katika kanuni:


1. Umeingiza seva ya `http` kutoka kwa maktaba ya kawaida ya Node.

2. `http.createServer()` huunda seva. Umepitisha hadi `http.createServer()` mwito wa kupiga simu `(req, res) => {...}` ili kutekelezwa kila mtu anapounganisha.

3. Umeweka msimbo wa hali ya 200 (ambayo inaonyesha operesheni iliyofanikiwa) kwa jibu. Unaweza kusoma kuhusu misimbo ya hali ya http [hapa](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

3. `res.end()` hutuma jibu na kutamatisha muunganisho.

4. `server.sikiliza(3000)` huanzisha seva kwenye mlango wa 3000.


Unaweza pia kuangalia `req.url` na `req.method` katika ombi la kushughulikia njia tofauti au aina za ombi.


Mfano na uelekezaji:


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


Hii ni mifano ya msingi sana. Ili kuunda seva za hali ya juu zaidi, watengenezaji wengi huenda wangepakua maktaba ya hali ya nyuma iliyotengenezwa tayari kama vile [express](https://www.npmjs.com/package/express).


## Inachakata data: bafa, matukio, mitiririko

<chapterId>8c9623f0-a604-51a4-8fe4-871c849d3e3b</chapterId>


Katika sura hii, tutaanzisha aina tatu za vitu:



- `Bafa`, ambayo inawakilisha vipande vidogo vya data ya jozi
- `EventEmitter`, ambayo inaweza kutumika kufuatilia hatua fulani kwa mchakato usio na usawa kwa kutoa ishara zinazoitwa "matukio"
- `Tiririsha`, ambayo huturuhusu kuchakata sehemu kubwa ya data `Buffer` moja kwa wakati huo, na ambayo hufuatilia mchakato kwa kutoa matukio.


Haya ni ya kawaida sana katika msimbo wa kitaalamu wa NodeJS, kwa hivyo hata kama huwezi kuzitumia katika miradi yako ya kwanza, ni vizuri kupata uelewa wa kimsingi wa wakati utahitaji kuingiliana nao. wao


### Vibafa


Katika NodeJS, **bafa** ni aina ya kitu kinachotumiwa kufanya kazi na data ya binary.


Unaweza kufikiria bafa kama chombo cha saizi isiyobadilika kwa baiti mbichi.


Hapa kuna jinsi ya kuunda buffer kutoka kwa kamba:


```javascript
const buf = Buffer.from("hello")
console.log(buf)
```


Hii inachapisha kitu kama:


```
<Buffer 68 65 6c 6c 6f>
```


Nambari hizo (`68`, `65`, `6c`, n.k.) ni viwakilishi vya hexadecimal vya herufi katika `"hello"`.


Unaweza kuibadilisha kuwa kamba kama hii:


```javascript
console.log(buf.toString())
```


Hii inachapisha:


```
hello
```


Unaweza pia kuunda bafa ya saizi fulani iliyojazwa na sufuri:


```javascript
const buf = Buffer.alloc(10)
console.log(buf)
```


Hii inachapisha kitu kama:


```
<Buffer 00 00 00 00 00 00 00 00 00 00>
```


Unaweza kuandika kwenye buffer:


```javascript
buf.write("abc")
console.log(buf)
```


Na unaweza kufikia baiti za kibinafsi:


```javascript
console.log(buf[0]) // prints the ASCII number for 'a', which is 97
```


Vibafa ni muhimu hasa unapohitaji kuchezea data kwa kiwango cha chini sana.


### Matukio


Katika JavaScript, **tukio** ni jambo linalofanyika katika programu yako ambalo unaweza kuitikia.


Kwa mfano:



- faili inamaliza kupakia
- kipima muda kinazimwa
- mtumiaji anabofya kitufe
- ombi la mtandao hurejesha data


**tukio** ni ishara tu kwamba jambo fulani limetokea, na unaweza kuandika msimbo ili kusikiliza matukio hayo na kuyajibu.


Katika NodeJS, vitu vingi vinaweza kutoa matukio. Vitu hivi huitwa **EventEmitters**.


Hapa kuna mfano:


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


Hii inachapisha:


```
Hello! An event happened.
```


Hapa kuna nini:


1. Tunaunda kipengee cha `EventEmitter`.

2. Tunaiambia ifanye upigaji simu wakati wowote tukio la `"salamu"` linapotokea, kwa kutumia `.on("greet")`.

3. Baadaye, tunaanzisha tukio la `"salamu"` kwa kutumia `.emit()`.

4. Callback yetu anapata kutekelezwa


Unaweza kupitisha data pamoja na tukio:


```javascript
emitter.on("greet",
(name) => console.log(`Hello, ${name}!`)
)

emitter.emit("greet", "Alice") // first argument is the type of event, second argument is the data we pass with this event
```


Hii inachapisha:


```
Hello, Alice!
```


Unaweza kusajili wasikilizaji kwa matukio mengine pia:


```javascript
emitter.on("goodbye", () => {
console.log("Goodbye!")
})

emitter.emit("goodbye")
```


Unaweza kuambatisha wasikilizaji wengi unavyopenda kwa aina ya tukio, na unaweza kurusha aina nyingi tofauti za tukio kutoka kwa mtoaji sawa.


Vitu vingi katika NodeJS hutoa matukio ili kuwaambia wengine wa programu kuwa kuna kitu kinatokea.



### Mito ni nini?


Mitiririko huchanganya bafa na matukio ili kutusaidia kuchakata data.


Tunapofanya kazi na faili, data kutoka kwa mtandao, au hata maandishi marefu, hatuhitaji kila wakati (au kutaka) kupakia kila kitu kwenye kumbukumbu mara moja. Hiyo inaweza kuwa polepole, au hata kuvuruga programu ikiwa data ni kubwa sana.


Badala yake, tunaweza kuchakata data **kidogo kidogo**, inapofika au inasomwa, kama vile kunywa maji kupitia mrija badala ya kujaribu kunywa glasi nzima mara moja. Hii inaitwa **mkondo**.


Katika NodeJS, mtiririko ni kitu ambacho hukuruhusu kusoma data kutoka kwa chanzo au kuandika data hadi lengwa ** kipande kimoja kwa wakati mmoja**.


NodeJS ina aina nne kuu za mitiririko:



- Inasomeka**: mitiririko unayoweza kusoma data kutoka (kama vile kusoma faili)
- Inaweza kuandikwa**: mitiririko ambayo unaweza kuandikia data (kama kuandika kwa faili)
- Duplex**: mitiririko ambayo inaweza kusomeka na kuandikwa
- Badilisha**: kama mitiririko ya duplex, lakini inaweza kubadilisha (kubadilisha) data inapotiririka


### Mitiririko inayosomeka


Hebu tuseme una `bigfile.txt` ya kuchakata. Unaweza kuunda mtiririko unaosomeka na moduli ya `fs` ili kusoma faili kipande kwa kipande.


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


Nini kinatokea hapa?


1. `fs.createReadStream()` huunda mtiririko unaoweza kusomeka.

2. Wakati wowote kipande cha faili kiko tayari, mtiririko hutoa tukio la `data` na kutupa "kipande" cha data (`Bafa`). Tunachapisha kipande.

3. Wakati faili nzima imesomwa, tukio la `mwisho` linaanzishwa.

4. Ikiwa kuna hitilafu (kama vile faili haipo), tukio la `kosa` limeanzishwa.


Kwa njia hii, unaweza kusoma faili kubwa bila kuzipakia zote kwenye kumbukumbu mara moja.


Ikiwa tunataka data ifike katika muundo unaoweza kusomeka na binadamu (badala ya mfumo wa jozi), tunaweza kubainisha usimbaji wa mtiririko:


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


Msimbo sasa utachapisha faili katika umbo linaloweza kusomeka na binadamu.


### Mitiririko inayoweza kuandikwa


Mtiririko unaoweza kuandikwa hukuruhusu kutuma data mahali fulani, kukatwa kwa sehemu.


Huu hapa ni mfano wa kuandikia faili `target.txt` kwa kutumia mtiririko:


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


Hiki ndicho kinachotokea:


1. `fs.createWriteStream()` huunda mtiririko unaoweza kuandikwa.

2. Tunaiandikia maandishi kwa kutumia `.write()`.

3. Tunapomaliza, tunaita `.end()` ili kufunga mtiririko.

4. Wakati data yote imeandikwa, tukio la `kumaliza` hutolewa.

5. Ikiwa kitu kitaenda vibaya, tukio la `error` linaanzishwa.


Kama vile mitiririko inayoweza kusomeka, mitiririko inayoweza kuandikwa ni nzuri kwa data kubwa kwa sababu haihitaji kuweka kila kitu kwenye kumbukumbu mara moja.


### Mito ya mabomba


Mojawapo ya mambo mazuri kuhusu mitiririko ni kwamba unaweza **kuibofya** pamoja: kuunganisha mtiririko unaosomeka moja kwa moja kwenye mtiririko unaoweza kuandikwa.


```javascript
const fs = require("fs")

const readable = fs.createReadStream("bigfile.txt")
const writable = fs.createWriteStream("target.txt")

readable.pipe(writable)
```


Hapa:



- Mtiririko unaosomeka unasoma kutoka `bigfile.txt`.
- Mtiririko unaoweza kuandikwa huandika kwa `copy.txt`.
- `.pipe()` hutuma data moja kwa moja kutoka inayoweza kusomeka hadi kwenye mtiririko unaoweza kuandikwa.


### Mito ya Duplex


Mtiririko wa duplex unaweza kusomeka na kuandikwa. Mfano mmoja ni tundu la mtandao: unaweza kutuma data kwake na kupokea data kutoka kwake.


Hapa kuna mfano rahisi sana kwa kutumia moduli ya `net`:


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


Katika mfano huu:



- Kipengee cha `soketi` ni mkondo wa duplex.
- Unaweza `kuandika()` kwake na pia kusikiliza matukio ya `data` kutoka kwayo.


### Badilisha mitiririko


Mtiririko wa kubadilisha ni mkondo wa duplex ambao pia hurekebisha data inayopita ndani yake.


Kwa mfano, unaweza kutumia moduli iliyojengewa ndani ya `zlib` kubana au kubana data.


Hapa kuna jinsi ya kukandamiza faili kwa kutumia mkondo wa kubadilisha:


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


Na kuipunguza nyuma:


```javascript
const readable = fs.createReadStream("bigfile.txt.gz")
const unzip = zlib.createGunzip()
const writable = fs.createWriteStream("bigfile.txt")

readable.pipe(unzip).pipe(writable)

writable.on("finish", () => {
console.log("File decompressed.")
})
```


Geuza mitiririko ni muhimu sana kwa kazi kama vile kubana, usimbaji fiche, au kubadilisha fomati za faili unapotiririsha.


### Shinikizo la nyuma


Wakati mwingine mtiririko unaoweza kuandikwa ni polepole katika kushughulikia data. Ikiwa tutaendelea kusukuma data kwa kasi ya kuandikika kuliko inavyoweza kushughulikia, tunaweza kukumbwa na matatizo. Hii inaitwa **backpressure**.


Ukiita mbinu ya `.write()` kwenye mtiririko unaoweza kuandikwa, italeta boolean ambayo inakufahamisha ikiwa mtiririko unahitaji kusitisha; unaweza kulazimika kuangalia thamani yake ya kurudi, kama hii:


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


Huu ulikuwa mfano wa kielelezo wa kusambaza data kwa mikono kutoka kwa Inayosomeka hadi Inayoweza Kuandikwa, na kudhibiti shinikizo la nyuma mwenyewe.


Kwa kawaida tungesambaza data kwa kutumia mbinu ya `.pipe()`, ambayo hushughulikia shinikizo la nyuma kiotomatiki.


Kwa hivyo unahitaji tu kuwa na wasiwasi kuhusu shinikizo la nyuma wakati kwa sababu fulani unapiga simu `.write()`.


## Ujumbe wa mwisho

<chapterId>139e2ab8-df67-525a-85f0-5a2fa5e478f2</chapterId>


Kwa hivyo, ndivyo ilivyo, ikiwa ulifuata pamoja na masomo, unapaswa kuwa na uwezo wa kuandika programu rahisi katika NodeJS.


Ningependekeza kufanya hivyo hasa: baada ya kujifunza misingi, kujenga miradi michache ya kibinafsi ndiyo njia bora ya kufanya mazoezi na kuwa mpangaji programu bora.


Haijalishi unaunda nini, cha muhimu ni kwamba unajipa changamoto kutatua shida na nambari.


Lugha za kisasa za upangaji zina nguvu sana, na NodeJS labda ndicho kisanduku bora zaidi cha kufanya majaribio katika awamu hii ya safari yako.


Bahati nzuri!


# Sehemu ya mwisho


<partId>322624d8-6fbc-11f0-a67a-5b145f10afc1</partId>


## Ukaguzi na Ukadiriaji


<chapterId>3e93ac86-6fbc-11f0-8bae-9b2ed7914843</chapterId>

<isCourseReview>true</isCourseReview>

## Hitimisho


<chapterId>49b3b9b2-6fbc-11f0-9870-5f5adcd3a0eb</chapterId>


<isCourseConclusion>true</isCourseConclusion>