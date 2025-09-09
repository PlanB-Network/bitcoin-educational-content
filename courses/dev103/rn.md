---
name: JavaScript na NodeJS ivy'ishimikiro
goal: Iga ivy’ishimikiro vyo gukora porogarama za JavaScript n’ugutegura NodeJS kugira ngo wubake ibikorwa n’ibikoresho bikora.
objectives: 

  - Insiguro y'ishimikiro ya JavaScript, ubwoko, n'ugucungera uruja n'uruza
  - Gutahura ibikorwa, ibintu, n'amashure muri JavaScript
  - Iga ubuhinga bwo gutorera umuti amakosa no kuyakosora
  - Menya neza NodeJS n'ibidukikije vyayo

---

# Tangira urugendo rwawe rwo gutera imbere


Murakaze muri iri shure ku bijanye n'inyandiko ya JavaScript na NodeJS.


JavaScript ni ururimi rwa porogarama ruzwi cane kw'isi: ni ururimi rwo kwandika rw'ibikoresho vy'ubuhinga bwa none, rero mu vy'ukuri ntibishoboka kwubaka urubuga rw'ubuhinga bwa none ata kwandika *JavaScript* imwe imwe; kandi n'igihe co gukoresha NodeJS ishobora gukoreshwa hanze y'ibikoresho navyo, kugira ngo ureme inyandiko n'ibikorwa bikora ataco bimaze kuri mudasobwa yawe.


Iryo shure ryagenewe abantu bashasha rwose mu bijanye n’ugukora porogarama, canke bakoresheje izindi ndimi mbere ariko bashaka gutahura ingene JavaScript ikora, cane cane mu bijanye na NodeJS.


Igihe amashure azoba arangiye, ukwiye kuba ushoboye kwandika porogarama zawe bwite muri JavaScript, ugakoresha ububiko bw’ibitabu bwa NodeJS, ugashiramwo no gukoresha amapaki y’abandi kugira ngo wubake ibikoresho vy’ingirakamaro.


+++
# JavaScript y'ishimikiro

<partId>a617327c-e5a2-52ca-9380-c63f44623dd4</partId>


## Gushinga

<chapterId>ba05a290-1782-5268-87c9-62fd09590e05</chapterId>


Muri iki gice turaza gutegura imashini yacu kugira ngo yandike kandi ikore porogarama yacu ya mbere ya JavaScript.


Porogarama ya JavaScript ni gusa ihuriro ry'amadosiye y'inyandiko (rimwe canke menshi), arimwo amabwirizwa azoshirwa mu ngiro n'igihe co gukoresha JavaScript.


Amazina y'izo dosiye z'inyandiko akenshi ahera n'ukwaguka kwa dosiye `.js`, nka `inyandiko_yanje.js`, `porogarama_yanje.js` n'ibindi.


Amabwirizwa arimwo yanditswe mu rurimi rwa porogarama rwa JavaScript.


Igihe co gukoresha JavaScript ni porogarama idasanzwe ikora izo dosiye.


![](assets/en/1.webp)


### Gushiramwo NodeJS


Igihe co gukoresha JavaScript gisanzwe ni NodeJS.


Ushobora kuyishiramwo ukurikije [amabwirizwa yemewe](https://nodejs.org/ru/gukuraho).


Paje yo gukuraho izoguha amabwirizwa y’ivyo bikoresho vyose bitatu bihambaye: Windows, Linux na MacOS. Bifata ko uzi gufungura terminal muri OS yawe.


Kubera ko NodeJS iboneka kuri OS zose zitatu, porogarama wanditse zizoshobora gukorwa kuri zo zose (uretse bimwe mu bibazo vyo ku ruhande).


Ivyo bisigura ko ushobora nk’akarorero kwandika urukino rworoshe rwo muri JavaScript kuri PC yawe ya Windows ukarurungikira umugenzi wawe kugira ngo arukoreshe kuri Mac yiwe.


![](assets/en/2.webp)


### Guhindura umwandiko


Kimwe mu bintu vyiza cane ku bijanye no gukora porogarama ni uko ushobora kwandika kode ukoresheje umuhinduzi w’inyandiko uwo ari we wese, mbere n’igitabu c’inyandiko ca OS yawe.


Hariho ama editors amwe amwe yihariye mu kwandika code naho, amwe araboneka ku buntu, ayandi asaba ko uriha uruhusha.


Ihitamwo ry’umuhinduzi wa kode ni ikinogo kinini c’inkwavu kirenze urugero rw’iri shure, rero ntituzobivuga hano. Niba utazi ico ukoresha, umuhinduzi w’ubuntu akoreshwa cane ni [VSCode](https://code.visualstudio.com/).


Interface yayo iravyimba gato, ariko ifise ivyo ukeneye: umuhinduzi w’amadosiye, umushakashatsi w’amadosiye (kugira ngo ubone amadosiye n’ibice biri mu bubiko uriko urakorako), n’igikoresho co gukoresha kode yawe. Ishigikira kandi ibikoresho vyinshi, kandi izana n’ugushira ahabona insiguro y’amajambo ya JavaScript ku buryo busanzwe.


Niba ushaka kuba Cypherpunk-y gatoyi, ushobora gukoresha [VSCodium](https://vscodium.com/) mu kibanza cavyo.


### Porogaramu yambere (ndabaramukije isi)


Mu migenzo, iyo umuntu yiga ururimi rwo gukora porogarama, porogarama ya mbere umuntu yandika ni ugucapura ngo "hello world!" ku nzira y’uguhoza.


Rema ububiko bwitwa `my_js_code/`, bufise imbere dosiye yitwa `main.js` (ayo mazina ni ay'ubusa).


Gufungura ububiko na VSCode.


Andika iyi kode muri dosiye yawe:


```javascript
console.log("hello world!")
```


Gufungura terminal maze ukore iri tegeko kugira ngo ukoreshe porogaramu:


```
node main.js
```


Ico bivamwo gikwiye kuba .


```
hello world!
```


### Vyagenze gute


Muri JavaScript, ikintu cose ni "ikintu".


`console` ni ikintu, gikoreshwa mu gukosora porogaramu.


`console.log` ni uburyo bukoreshwa cane bwa `konsole`. Icapura gusa imvo zose uyirungikira.


Utanga imvo kuri `console.log` ukoresheje ibifunga bizunguruka `()`.


Rero nk'akarorero, iyo ushaka gucapura umubare `1000`, wokwandika gusa


```javascript
console.log(1000)
```


Hanyuma ubishitse mu kwiruka .


```
node main.js
```


mu terminal yawe (kuva ubu, iri shure rizokwiyumvira ko uzi uko ukora porogarama).


Ibi bikwiye gucapura


```
1000
```


Ushobora guca ibintu vyinshi, nka


```javascript
console.log(16, 8, 1993)
```


Ibi bizocapura


```
16 8 1993
```


## Ibihinduka n'ibitekerezo

<chapterId>23050ab7-343b-5edf-9d37-e4e782e27ce0</chapterId>


Porogaramu akenshi zikora ibikorwa ku makuru.


Ibihinduka ni nk'amasandugu afise amazina dukoresha mu kubika amakuru. Bituma dushobora gufatanya amakuru n’izina kanaka, kugira ngo dushobore kuyaronka mu nyuma dukoresheje iryo zina.


### `reka` amatangazo


Kugira ngo tumenyeshe umuhinduzi muri JavaScript, dushobora gukoresha ijambo ry'ingenzi `let`.


Tumaze kwandika `let`, twandika izina dushaka guha umuhinduzi, hanyuma tukandika ikimenyetso `=`, hanyuma tukandika agaciro dushaka kubika.


Nk'akarorero:


```javascript
let age = 25

console.log(age)
```


Izina ry'umuhinduzi (mu buryo bw'ubuhinga ryitwa "ikimenyetso") rishobora kubamwo inyuguti, uturongo (`_`), ikimenyetso c'idolari (`$`) n'imibare, naho ikimenyetso ca mbere kidashobora kuba umubare.


Mu kode iri hejuru, twamenyesheje umuhinduzi witwa `imyaka` maze tubika agaciro `25` muri yo.


Hanyuma, ducapura agaciro dukoresheje `console.log(imyaka)`.


Niwakoresha iyi kode na `node main.js`, igisohoka kizoba:


```
25
```


Ibimenyetso bishingiye ku nyuguti nini, bisobanura ko inyuguti ntoya n'inyuguti nini ziharurwa nk'itandukaniro mu bimenyetso, rero nk'akarorero


```javascript
let age = 25

let Age = 20

console.log(age)
```


izocapura 25, kuko ivyo bifatwa nk’ibihinduka bibiri bitandukanye rwose!


Ushobora kandi kubika imirongo (umwandiko) mu mpinduka:


```javascript
let message = "hello again"

console.log(message)
```


Ibi bizocapura:


```
hello again
```


Nka kurya kwa kera, twakoresheje `console.log()` kugira ngo ducape agaciro kabitswe mu mpinduka.


None reka tubikore vyose hamwe:


```javascript
let age = 25

let message = "hello again"

console.log(age)

console.log(message)
```


Gukoresha ibi bizocapura:


```
25
hello again
```

### Gusubira guhabwa igikorwa


Ibihinduka vyamenyeshejwe na `let` bishobora guhindurwa bimaze kuremwa.


Ivyo vyitwa gusubira guhabwa igikorwa.


```javascript
let score = 10

console.log(score)

score = 15

console.log(score)
```


Mbere, dutanga `10` ku `manota`, hanyuma tukayacapura.


Hanyuma tugahindura agaciro ka `score` tukagira `15` tugacapura kandi.


Igisohoka kizoba:


```
10
15
```


Ivyo birafasha cane iyo agaciro gahinduka uko igihe kigenda kirarenga, nk’aho mu rukino aho amanota agenda arushirizaho.


Reka twongereko uwundi muhinduzi ku vyo tuvanga:


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


Ibi bizocapura:


```
10
Alice
20
Bob
```


Nk'uko mubibona, `score` na `player` vyose vyahinduwe.


### `const` amatangazo


Ariko kenshi, ntidushaka ko igihinduka gihinduka kimaze kuremwa. Ku bw'ivyo, dukoresha `const`.


`const` ni insiguro ngufi y’“ibihoraho”. Iyo umaze gutanga agaciro ku mpinduka `const`, ntushobora kuyihindura.


```javascript
const pi = 3.14
console.log(pi)
```


Ibi bicapura:


```
3.14
```


Ariko niwagerageza gukora ibi:


```javascript
const pi = 3.14
console.log(pi)

pi = 99 // this line will cause an error
console.log(pi)
```


JavaScript izoguha ikosa nka:


```
TypeError: Assignment to constant variable.
```


Ivyo ni kubera ko `pi` yatangajwe hakoreshejwe `const`, kandi ntushobora guhindura agaciro kayo inyuma y'ivyo. Uriko uramenyesha umusiguzi wa JavaScript ko udashaka ko iyo mpinduka ihinduka.


Ivyo ni ngirakamaro kuko bigabanya amahirwe yo kubihindura ku makosa. Iyo porogaramu zicitse nini cane, zifise imirongo ibihumbi n’ibihumbi, ntibishoboka ko umuntu ashobora gukurikirana ibintu vyose biriko biraba icarimwe (iyo ni yo mpamvu nyamukuru ituma dukoresha mudasobwa, kugira ngo dukore ibikorwa bikomeye tudashobora guharura n’ubwonko bwacu), rero biraba vyiza kugira amategeko nk’aya, atuma porogarama igira determini.


Ni vyiza kwama tumenyesha agaciro kacu nka `const`, kiretse iyo twizeye neza ko dushaka kubihindura mu nyuma.


### Ivyiyumviro muri JavaScript


Rimwe na rimwe turashaka kwandika amajambo muri kode yacu adashirwa mu ngiro. Ivyo vyitwa ibisobanuro.


Ivyiyumviro birarengagizwa na porogarama iyo iriko irakora, ariko ni ngirakamaro mu kwisigurira ibintu canke abandi bantu.


Kwandika igitekerezo c'umurongo umwe, koresha `//`


```javascript
// This is a comment
const x = 10 // This is also a comment
console.log(x)
```


Ibi bizoguma bicapwa:


```
10
```


Ivyo bivugwa biri ng’aho gusa kugira abantu babisome.


Ushobora kandi kwandika ibitekerezo vy'imirongo myinshi ukoresheje `/*` na `*/`


```javascript
/*
This is a multi-line comment.
It can span several lines.
*/
const y = 20
console.log(y)
```


Ibi bizocapura


```
20
```


Kandi iyo commentaire izokwirengagizwa.


Ushobora gukoresha ibivugwa kugira ngo wongereko utusobanuro dutoduto kuri kode yawe, kugira ngo ushobore kwibuka ico ikora be n’igituma yanditswe mu buryo bunaka. Bishobora kandi gufasha abandi bakora porogarama kubitahura.


## Ubwoko bw'ishimikiro: imibare, imirongo, ibiharuro

<chapterId>cfdb04f6-21a8-5143-bbf9-7aaae04962f0</chapterId>


Mu rurimi rwa JavaScript, “ubwoko” burakubwira ubwoko bw’amakuru agaciro ari.


Javascript ifise ubwoko bukeyi bw’ishimikiro, kandi muri iki gice tuzokwihweza bumwe muri bwo.


### Imibare n'imikorere y'imibare


Ubwoko bwa mbere tuzozana ni `umubare`.


Imibare muri JavaScript ishobora kuba imibare yose (nka `5`) canke imibare cumi (nka `3.14`).


Ushobora gukorana na bo imibare: kwongerako, gukurako, gukubita, no kugabanya.


Aha niho akarorero k’ishimikiro:


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


Ibi bizocapura:


```
15
5
50
2
```


Ushobora kandi gukoresha uturongo `()` kugira ngo ugenzure urutonde rw'ibikorwa:


```javascript
const result = (2 + 3) * 4
console.log(result)
```


Ibi bicapura:


```
20
```


Hatariho uturongo, vyoba ari `2 + 3 * 4`, ni ukuvuga:


```javascript
const result = 2 + 3 * 4
console.log(result)
```


Ivyo vyocapura:


```
14
```


Kuko mu biharuro bisanzwe, ugukubita bishika imbere y’uko umuntu yongerako.


### Imirongo n'ugushiramwo


Ubwoko bwa kabiri bwa JavaScript tugiye gutanga ni `urudodo`.


Imirongo ni ibice vy’ivyanditswe. Ushobora gukoresha amajambo amwe `'...'` canke amajambo abiri `"..."` kugira ngo ubireme.


```javascript
const greeting = "hello"
const name = 'Bob'
console.log(greeting)
console.log(name)
```


Ibi bicapura:


```
hello
Bob
```


Kugira ngo uhuze imirongo, ushobora gukoresha `+` umukoresha:


```javascript
const greeting = "hello"
const space = " "
const name = "Bob"

const fullGreeting = greeting + space + name
console.log(fullGreeting)
```


Ibi bizocapura:


```
hello Bob
```


Ariko hari uburyo bwiza bwo gufatanya imirongo bwitwa **ugushiramwo imirongo**. Ukoresha ibimenyetso vy'inyuma kugira ngo umenyeshe urudodo `` `...` `` kandi wandike ibihinduka ukoresheje `${...}` imbere mu rudodo:


```javascript
const greeting = "hello"
const name = "Bob"

const fullGreeting = `${greeting} ${name}`
console.log(fullGreeting)
```


Ibi navyo bicapura:


```
hello Bob
```


Ushobora gushiramwo invugo iyo ari yo yose imbere muri `${...}`:


```javascript
const age = 30
console.log(`Next year, I will be ${age + 1} years old.`)
```


Ibi bicapura:


```
Next year, I will be 31 years old.
```


Gushiramwo ibintu mu rurimi rw’ikirundi ni ikintu gisanzwe cane muri JavaScript y’ubu.


### Booleans, kugereranya n'imikorere y'ubwenge


Ubwoko bwa gatatu tuzozana ni `boolean`. Yitiriwe umuhinga mu vy'imibare George Boole, uwahinguye ubuhinga bwo gutahura ibintu.


Booleans ni yoroshe: agaciro kabiri gusa gashoboka, `ukuri` na `ikinyoma`.


Ushobora kubibika mu bihinduka:


```javascript
const theSkyIsBlue = true
const thisCourseIsBad = false

console.log(theSkyIsBlue)
console.log(thisCourseIsBad)
```


Ibi bicapura:


```
true
false
```


Ushobora gufatanya booleans ukoresheje abakozi b'ubwenge:



- `&&` bisigura “kandi”, kandi izogarura `ukuri` gusa iyo **vyompi** agaciro ari `ukuri`, ahandi ho izogarura `ikinyoma`
- `||` bisigura “canke”, kandi izogarura `ukuri` iyo **nibura kimwe** mu bipimo ari `ukuri`, ahandi ho (niba vyose ari ibinyoma) izogarura `ikinyoma`
- `!` bisigura “oya”, bikoreshwa imbere y'ibara, kandi rizorihindura: iyo ibara ari `ukuri` rizogarura `ikinyoma`, n'ibihushanye n'ivyo.


![](assets/en/3.webp)


Ingero:


```javascript
const isSunny = true
const isWarm = true

console.log(isSunny && isWarm)  // true
console.log(isSunny || isWarm)  // true
console.log(!isSunny)           // false
```


Ushobora kugereranya agaciro muri JavaScript ukoresheje ibikorwa nka `>`, `<`, `===`, na `!==`. Inyishu y’ivyo bigereranyo yama ari boolean.


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


Javascript nayo ifise `>=` bisobanura "nini canke bingana" na `<=` bisobanura "bito canke bingana.


Booleans, kugereranya n'ibikoresho vy'ubwenge akenshi bihurizwa hamwe muri porogaramu kugira ngo bimenyeshe ibintu bikomeye, nk'ukumenya neza ko "imeli yashitse KANDI irimwo ishusho nkeneye CANKE uburebure bw'imeli burenze inyuguti 10000". Uzosanga mu nyuma ivyo ari ibintu bihambaye vyo kwubaka ivyiyumviro vy’iporogarama.


## Imirongo, ubusa, itasobanuwe

<chapterId>7bf18183-5eae-53ed-83d2-b04982145d81</chapterId>


Muri iki gice, turaza kubona ubundi bwoko butatu busanzwe muri porogarama za JavaScript:



- Imirongo**: urutonde rw'agaciro
- undefined**: agaciro kadasanzwe gasobanura “nta kintu na kimwe cahawe”
- null**: akandi gaciro kadasanzwe gasobanura “ubusa n’ibigirankana”


### Ububiko n'urutonde


**array** ni ubwoko bushobora gufata agaciro kenshi mu rutonde.


Ukora urutonde ukoresheje ibifunga `[]` no gutandukanya ibintu n'ibimenyetso.


Aha niho akarorero k’ishimikiro:


```javascript
const numbers = [10, 2, 88]
console.log(numbers)
```


Ibi bicapura:


```
[ 10, 2, 88 ]
```


Ushobora kubika ikintu cose mu rutonde, atari imibare gusa:


```javascript
const things = ["apple", 42, true]
console.log(things)
```


Ibi bicapura:


```
[ 'apple', 42, true ]
```


Kugira ngo ushikire ikintu kinaka mu rutonde, dukoresha **index**. Urutonde ni ikibanza c'ikintu, guhera kuri **0**.


Rero muri iyi nzira:


```javascript
const colors = ["red", "green", "blue"]
```



- `amabara[0]` ni `"umutuku"`
- `amabara[1]` ni `"Green"`
- `amabara[2]` ni `"ubururu"`


Reka tugerageze:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[0])
console.log(colors[1])
console.log(colors[2])
```


Ibi bizocapura:


```
red
green
blue
```


Ushobora gutanga agaciro ku rutonde rwihariye rw'urutonde


```javascript
const colors = ["red", "green", "blue"]

colors[1] = "yellow"

console.log(colors)
```


Ibi bizocapura:


```
[ 'red', 'yellow', 'blue' ]
```


Ushobora gukoresha umubare uwo ariwo wose nk'urutonde, mbere n'uwo ubitswe mu mpinduka


```javascript

const i = 1
const colors = ["red", "green", "blue"]
console.log(colors[i])
```


Ibi bizocapura:


```
green
```


Ariko niwagerageza gushika ku rutonde rutariho, uzoronka `undefined`:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[3])
```


Ibi bicapura:


```
undefined
```


Ivyo ni ibiki??


### 'bitasobanuwe`


Agaciro kadasanzwe `undefined` bisigura “nta gaciro kashizweho”.


Niwakora umuhinduzi ariko ntuwuhe agaciro, uzoba `undefined`:


```javascript
const name
console.log(name)
```


Ibi bicapura:


```
undefined
```


Kubera ko ataco twahaye `izina`, JavaScript irishira ku `undefined` ku buryo busanzwe.


Nk’uko vyabonetse mbere, ushobora kandi kuronka `undefined` iyo winjiye ku rutonde rw’urutonde rutariho:


```javascript
const fruits = ["banana", "apple"]
console.log(fruits[2]) // There is no index 2
```


Ibi bicapura:


```
undefined
```


### `ubusa` n'ingene wobifata


`null` nayo ni agaciro kadasanzwe. Bisigura ngo “nta kintu kiri hano, kandi ivyo nabikoze n’ibigirankana.”


Udakunze `undefined`, ariko yikora, `null` ni ikintu wishingira.


Nk'akarorero:


```javascript
const currentUser = null
console.log(currentUser)
```


Ibi bicapura:


```
null
```


Kuki ukoresha `ubusa`? Kumbure witega agaciro mu nyuma, ariko n’ubu ntikirateguwe:


```javascript
let winner = null

// Later in the program:
winner = "Alice"

console.log(winner)
```


Ibi bicapura:


```
Alice
```


Rero `null` ni ngirakamaro iyo ushaka kuvuga, nk’akarorero, “Hazoba ikintu hano mu nyuma, ariko ubu nyene n’ubusa.”


## Amabuye n'ugucungera uruja n'uruza

<chapterId>be985168-2636-5b0d-a48f-ac1bbfbff8a7</chapterId>


Kugeza ubu, twanditse cane cane imirongo y’amakode ikurikirana.


Ariko iyo dukoze kode, turashobora kugenzura urutonde rw’ingene izoshirwa mu ngiro.


Ivyo vyitwa **ugucungera uruja n’uruza**.


Reka dutangure n’ugutahura amabuye n’urugero.


### Uburebure bw'isi yose


Ihinduka ryose dutangaza ririho mu **scope**, bisobanura akarere ka kode aho ihinduka rizwi.


Niwatangaza umuhinduzi hanze y'ibarabara iryo ari ryo ryose, ariho mu **urugero rw'isi yose**.


```javascript
const color = "blue"
console.log(color)
```


Iyi mpinduka `ibara` iri mu rwego rw'isi yose, rero ishobora gushikwako aho hose muri dosiye.


Niwongerako iyindi mirongo:


```javascript
const color = "blue"
console.log(color)

const size = "large"
console.log(color)
console.log(size)
```


`Ibara` n'ubunini` vyose ni ibihinduka kw'isi yose. Biboneka hose muri dosiye.


Ariko none imbere mu nzu y’ibarabara bigenda gute?


### Amabuye n'uburebure bw'aho hantu


**block** ni igice ca kode gikikujwe n'ibimenyetso bigoramye `{}`.


Ibihinduka vyamenyeshejwe na `let` canke `const` imbere mu gice biriho **gusa** imbere muri ico gice.


```javascript
{
const message = "inside block"
console.log(message)
}
```


Ibi bicapura:


```
inside block
```


Ariko niwagerageza ibi:


```javascript
{
const message = "inside block"
}
console.log(message) // Error!
```


JavaScript izoguha ikosa nka:


```
ReferenceError: message is not defined
```


Ivyo ni kubera ko `ubutumwa` bwamenyeshejwe imbere muri block kandi ntabwo buri hanze yayo.


Ivyo bisigura ko dushobora gukoresha amabuye kugira ngo dutandukanye ibice vya kode yacu, kandi tukamenya neza ko "ibibera mu mabuye biguma mu mabuye" (kinda nka Las Vegas).


Gutunganya kode yacu mu bice bituma kandi dushobora gutunganya ibikorwa vya porogaramu, n'inyubako z'ubugenzuzi nk'iyi 'niba`


### 'niba`, 'ahandi`


Rimwe na rimwe dushaka gukoresha code **gusa iyo** ikintu ari ukuri. Ivyo ni vyo ijambo `if` rigenewe.


```javascript
const myAge = 20

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Ibi bicapura:


```
Am I an adult?
Yes I am!
```


Nk'uko ushobora, raba kode igereranya `myAge` na `18`.

Muri iki gihe umukoresha `>=` agarura `ukuri`, rero ububiko burashirwa mu ngiro.

Iyo ivyangombwa atari `ukuri`, ububiko ntibushobora gushirwa mu ngiro.


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Ibi bicapura:


```
Am I an adult?
```


Ushobora kwongerako `ikindi` kugira ngo ukoreshe ikibazo gihushanye n'ico:


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
} else {
console.log("No, I am not.")
}
```


Ibi bicapura:


```
Am I an adult?
No, I am not.
```


Ivyo bice vyose bibiri `if` na `else` biracari ibice - rero ibihinduka vyamenyeshejwe imbere muri vyo ntibibaho hanze.


Nimba dushaka kumenya neza ko ikintu **kitari** ukuri, twokora iki?


Erega, nk'uko twabibonye mbere, JavaScript ifise umukoresha "not", uhindura booleans. Rero turashobora gukora


```javascript
const myAge = 17

const adult = myAge >= 18

console.log("Am I an adult?")

if (!adult) {
console.log("No, I am not.")
}
```

Ibi biracapura:


```
Am I an adult?
No, I am not.
```

Kuko twakoresheje umukoresha `!` kugira ngo duhindure umuhinduzi `umuntu akuze`.


`niba (!umuntu akuze) {...}` bikwiye gusomwa nk'"niba atari umuntu mukuru..."


Dukoresheje amabuye, ubuhinga bwo gutahura ibintu n’ubuhinga bwo kugereranya, turashobora gutunganya ibikorwa vya porogarama, mu gusobanura ibihinduka bitegerezwa kuba `ukuri` (canke `ikinyoma`) kugira ngo ikintu kibeho.


### `mugihe`, `akaruhuko`, `gukomeza`


Uruzitiro rwa `while` rusubiramwo kode *igihe cose* ivyangombwa ari ukuri.


```javascript
let count = 0

while (count < 3) {
console.log("Count is", count)
count = count + 1
}
console.log("the loop is over!")
```


Ibi bicapura:


```
Count is 0
Count is 1
Count is 2
the loop is over!
```


Iyo `count` ibaye 3, uruzitiro rurahagarara.


Ushobora guhagarika uruzitiro kare ukoresheje `uguhagarika`:


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


Ibi bicapura:


```
0
1
2
```


Kuko iyo umubare ubaye `3`, `if` block irakora maze igahagarika uruzitiro.


Ushobora gusimbuka igice gisigaye c'uruzitiro ukoresheje `gukomeza`:


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


Ibi bicapura:


```
1
2
4
5
```


Kuko igihe umubare wari `3`, `continue` vyatumye porogarama isimbuka umurongo ucapura umubare.


### `kubera ... wa ...`


Niba ufise urutonde, kandi ushaka gukora ikintu ku kintu cose kiri muri rwo, ushobora gukoresha `ku ... wa ... {...}`.


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const fruit of fruits) {
console.log(fruit)
}
```


Ibi bicapura:


```
apple
banana
cherry
```

Igipande kizoshirwa mu ngiro rimwe ku kintu cose c'urutonde.


`imbuto` aha ni umuhinduzi mushasha ufata agaciro k'ikintu cose kiri mu rutonde, kugira ngo ukoresheko imbere mu gice.


### `ku ... muri ...`


Ushobora gukoresha `ku ... muri` kugira ngo uzunguruke imfunguruzo (urutonde) rw'urutonde:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(index)
}
```


Ibi bicapura:


```
0
1
2
```


Ushobora gukoresha urutonde kugira ngo ubone agaciro:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(fruits[index])
}
```


Ibi bicapura kimwe na `ku ... vya`:


```
apple
banana
cherry
```


Mu bikorwa, ku mirongo, ushobora guhitamwo gukoresha `ku ... ya`, kuko vyoroshe kandi bisukuye.


### Inziga zifise imbibe


Rimwe na rimwe turashaka gucapura incuro zimwe zimwe, canke muri rusangi kwandika igice ca kode gisubiramwo igice mu gihe turiko turakurikirana ikintu.

Ivyo ni vyo uruzitiro rwa `for` rufise urubibi ruri rwiza.

Uruzitiro rufise urubibi rufata ibintu bitatu, bitandukanijwe n'akarongo `;`, nk'uko biri muri `(... ; ... ; ....)`.


```javascript
for (let i = 0; i < 3; i = i + 1) {
console.log(i)
}
```


Ibi bicapura:


```
0
1
2
```


Reka tubisigure:



- `let i = 0`: itangaza umuhinduzi uzokoreshwa mu bubiko (muri iki gihe ni umubare utangura kuri 0)
- `i < 3`: itangaza ivyangombwa ko ari `ukuri` kugira ngo ububiko bushirwe mu ngiro ( muri iki gihe ni "gusubiramwo mu gihe `i` iri munsi ya 3")
- `i = i + 1`: tangaza kode imwe imwe izokoreshwa inyuma y'ugushirwa mu ngiro kwose kw'ibarabara (muri iki gihe "wongere `i` na 1")


Nk'uko ushobora kubibona, uruzitiro rufise urubibi rwo kumenyesha ibintu bikomeye cane vyo gusubiramwo igice c'itegeko, ariko kenshi na kenshi ntibikenewe.


### Ibimenyetso vy'ububiko


Niba ugomba kwandika uruja n'uruza rw'ubugenzuzi rukomeye, JavaScript iragufasha kwita izina ry'ibara ukoresheje **ikimenyetso** gishobora gukoreshwa na `break` canke `continue` mu kugaragaza *aho* ushobora gusimbuka ugasubira inyuma.


Akarorero:


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


Ibi bicapura:


```
Inside outer block
Inside inner block
Done
```


Twakoresheje `guca hanze` kugira ngo tuve mu gice ca `inyuma` cose.


Ushobora kandi gushirako amazina y'ibizingiti. Reka dufate aka karorero:


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

Ico cari akarorero gateye ubwoba cane ariko twizigiye ko catomoye (rimwe na rimwe) ivy’ugukenera amabara.


## Gutanguza imikorere

<chapterId>cc324715-09c2-5cf7-9e6f-47a6f16bc04d</chapterId>


Uko porogarama zawe zikura, uzoshaka kenshi **gusubira gukoresha** ibice vya kode.


Ivyo ni vyo **functions** zigenewe: ziguha uburenganzira bwo gukoranya code zimwe zimwe, ukayiha izina, ukayikoresha igihe cose ushaka.


### Itangazo ry'umurimo


Kugira ngo tumenyeshe igikorwa, dushobora gukoresha ijambo ry'ingenzi `igikorwa`. Hanyuma tukayiha izina, uturongo tubiri `()` n'imvo zifata, n'igice ca kode `{}` izoshirwa mu ngiro. Reka dutangure n'igikorwa kitafata impaka:


```javascript
function sayHello () {console.log(`Hello!`) }
```


Iyi kode **imenyesha** igikorwa, ariko **ntiyikoresha**.


### Amahamagara y'imikorere


Kugira ngo ukoreshe (canke "uhamagare") igikorwa, wandika izina ryaco ukurikiwe n'ibifunga:


```javascript
function sayHello () {console.log(`Hello!`) }
sayHello()
```


Ibi bicapura:


```
Hello!
```


Ushobora guhamagara iyo nzira incuro nyinshi uko ushaka:


```javascript
function sayHello() {
console.log("Hello!")
}

sayHello()
sayHello()
```


Ibi bicapura:


```
Hello!
Hello!
```


Kode iri imbere muri iyo function ikora gusa iyo uyihamagaye.


### Impamvu z'imikorere (injiza mu mikorere)


Rimwe na rimwe, ushaka ko igikorwa gikora n'inyungu imwe imwe. Ivyo ushobora kubigira mu kwongerako **imvo** imbere mu bifunga.


Nk'akarorero:


```javascript
function sayHelloTo (friend) {
console.log(`Hello ${friend}!`)
}
```


None iyi nshingano ifata **impamvu imwe** yitwa `umugenzi`.


Iyo uhamagara igikorwa, ushobora gutanga agaciro:


```javascript
sayHelloTo("Tommy")
```


Ibi bicapura:


```
Hello Tommy!
```


Ushobora guhamagara igikorwa kandi n'izina ritandukanye:


```javascript
sayHelloTo("Sam")
```


Ibi bicapura:


```
Hello Sam!
```


Agaciro ushiramwo gasubirira `umugenzi` umuhinduzi imbere mu gikorwa.


Ushobora kandi gukoresha impamvu zirenga imwe:


```javascript
function greetTwoPeople(person1, person2) {
console.log(`Hello ${person1} and ${person2}!`)
}

greetTwoPeople("Lina", "Marco")
```


Ibi bicapura:


```
Hello Lina and Marco!
```


### `kugaruka` (igisohoka kiva ku bikorwa)


Imikorere ishobora kandi **kugarura** agaciro. Ivyo bisigura ko bohereza agaciro aho hose igikorwa cahamagawe.


Aha niho akarorero koroshe:


```javascript
function getNumber() {
return 42
}

const result = getNumber()
console.log(result)
```


Ibi bicapura:


```
42
```


Igikor `getNumber()` kigarura `42`, tukabibika mu `igisubizo`, hanyuma tukabicapura.


Ushobora kandi kugarura ikintu ubaze:


```javascript
function add(a, b) {
return a + b
}

const result = add(2, 3)
console.log(result)
```


Ibi bicapura:


```
5
```


Igihe agaciro kagarutse, igikorwa kirahagarara. Ico ari co cose inyuma ya `return` muri iyo block ntikiba.


```javascript
function saySomething() {

return "hi"

console.log("this never runs")

}

const message = saySomething()
console.log(message)
```


Ibi bicapura gusa:


```
hi
```


kuko `"hi"` gusa nivyo bigaruka. Umurongo wa `console.log("ibi ntivyigera bigenda")` urasimbuka.


Ushobora kwiyumvira ibikorwa nk'utugingo ngengabuzima dutoduto. Buri function ishobora gufata input, ikayikorako, ikagusubiza input.


Bigenda gute iyo tugerageje gukoresha agaciro k’igaruka k’igikorwa, ariko ico gikorwa ntikigarutse ikintu na kimwe?


```javascript
function doesNothing () {}

const x = doesNothing()

console.log(x)
```

Ibi bizocapura `bitasobanuwe`. Agaciro k'igikorwa kitagarutse ikintu na kimwe ni `undefined`.


## Ibintu n'amashure

<chapterId>26689f25-8212-5057-8c21-3a05eee0ac75</chapterId>


JavaScript akenshi yitwa ururimi rushingiye ku bintu.


Ivyo bisigura ko bigufasha gutunganya kode yawe mu gushiramwo agaciro n'ibikorwa hamwe mu **ibintu**.


### `Ikintu` ni iki ?


Ikintu gishobora kubamwo amakuru n'ibikorwa bikora kuri ayo makuru. Iyo igikorwa gishizwe mu kintu tuvuga ko ari `uburyo`.


Ikintu ca mbere twabonye cari ikintu ca `console`. Ni ikintu kirimwo uburyo bwinshi bwo gucapura ikintu ku rubuga no gukosora porogarama zacu.


Irashobora mbere kwicapura; ushobora gukora


```javascript
console.log(console)
```


kandi izocapura urutonde rw’uburyo burimwo. Nk’akarorero, ku mashine yanje yaracapa .


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


Nk’uko mubibona, irafise uburyo bwinshi woshobora gukoresha mu gukosora!


Javascript iduha uburyo butandukanye bwo kurema ibintu bishasha bishobora gukora ivyo dushaka vyose.


### Guhingura ikintu


Uburyo bworoshe bwo kurema ikintu ni ugushiramwo amakuru n'imikorere ukoresheje **ibimenyetso bigoramye** `{}`.


Ivyo bica bituma haba ico twita **ikintu kitazwi**


```javascript
const cat = {
name: "Whiskers",
age: 3
}
```


Ivyo birema ikintu kikabika mu mpinduka yitwa `cat`.


Ikintu gifise **ibiranga** bibiri:



- `izina` n'agaciro `"Ubwoya"`
- `imyaka` n'agaciro `3`


Reka tuyicape:


```javascript
console.log(cat)
```


Ibi bicapura:


```
{ name: 'Whiskers', age: 3 }
```


Ushobora kuronka ibiranga ikintu ukoresheje akadomo, nk'uko biri muri `izina ry'ikintu.Izina ry'ikintu`:


```javascript
console.log(cat.name)  // prints "Whiskers"
console.log(cat.age)   // prints 3
```


Ushobora kandi **guhindura** umutungo:


```javascript
cat.age = 4
console.log(cat.age)  // now it prints 4
```


Nk'uko ushobora kubibona, naho ikintu coba gisobanuwe nka `const`, urashobora guhindura amakuru kirimwo.


Mu bijanye n'ibintu, `const` izoguhagarika gusa guhindura ikintu cose:


```javascript
const cat = {
name: "Whiskers",
age: 3
}

cat.age = 5 // this works

cat = 5 // this throws an error, you're trying to reassign the whole object

```


Nk'uko twabibonye mbere, ibintu birashobora kandi gufata **ibikorwa**, kandi iyo igikorwa ari igice c'ikintu, tuvyita **uburyo**.


Akira akarorero:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log("Meow!")
}
}
```


Iki kintu gifise:



- Izina ry'umutungo
- Uburyo bwo `kuvuga()`


Reka twite uburyo:


```javascript
cat.speak()
```


Icapura:


```
Meow!
```


Uburyo bushobora gukoresha amakuru ikintu kirimwo biciye mw'ijambo ry'ingenzi `iki`.

`iki` kivuga ikintu kiriho ubu. Muri aka karorero, izokoreshwa mu gucapura izina ry'akayabu:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log(`${this.name} says meow!`)
}
}

cat.speak()
```


Ibi bicapura:


```
Whiskers says meow!
```


Ijambo `iki` risobanura "iki kintu"...muri iki gihe, ikintu `cat`.



Ivyo bintu nk’ivyo ni vyiza cane iyo ushaka gusa ikintu cihuta kandi coroshe. Ariko iyo ukeneye kurema **ibintu vyinshi** bifise imiterere imwe, hari uburyo bwiza, kandi niho **amashure** yinjira.


### Amashure n'ubwubatsi


**Ishure** ni nk’igishushanyo. Ibwira JavaScript ingene yorema ubwoko bumwe bw’ikintu.


Usobanura ishure ukoresheje ijambo ry'ingenzi `class`, rikurikiwe n'izina ry'ishure, n'ibara ry'inzira `{}`.


```javascript
class Dog {}
```


Amashure akenshi atangura n’urudome runini, nk’uko bisanzwe.


Ushobora kurema ikintu gishasha c'ishure ukoresheje `gishasha`:


```javascript
const hachiko = new Dog()
```


Gerageza gucapura ikintu:

```javascript
class Dog {}

const myDog = new Dog()

console.log(myDog)
```


Uzoronka


```
Dog {}
```


Nk'uko ushobora kubibona, ishure ry'Imbwa riri ubusa, ni ko n'ikintu ca `myDog` kiri ubusa.


Turashobora gusobanura ibintu ibintu vy'imbwa bikwiye kubamwo mu kwongerako `umwubatsi`.


Uwukora ni igikorwa kidasanzwe gikora iyo uremye (canke "wubatse") ikintu gishasha.


```javascript
class Dog {
constructor() { }
}
```


Turashaka ko Imbwa yose igira izina, rero twongerako `izina` ku gikorwa:


```javascript
class Dog {
constructor(name) { }
}
```


Hanyuma dukoreshe `iki` kugira ngo tumenyeshe ko `izina` ari `izina` ry'ikintu `Imbwa` turiko turakora


```javascript
class Dog {
constructor(name) {
this.name = name
}}
```


Reka tugerageze kuyikoresha ubu:


```javascript
class Dog {
constructor(name) {
this.name = name
}
}

const myDog = new Dog("hachiko")

console.log(myDog)
```


Ibi bicapura ikintu nk'iki:


```
Dog { name: 'hachiko' }
```


Nk'uko ushobora kubibona, uburyo bwa `constructor` bufata ingingo utanga mu kigo iyo ukora `new Dog()`, maze bukabukoresha mu kwubaka ikintu.


Reka tuvyice:



- `umugwi w'Imbwa` usobanura umugwi w'Imbwa.
- `umwubatsi(izina)` ashiraho ikintu iyo kiremwe.
- `this.name = izina` ibika agaciro mu kintu gishasha.
- `Imbwa nshasha("hachiko")` irema ikintu gishasha kuva mw'ishure, n'umutungo `izina` ushizwe kuri `"hachiko"`.


None rero reka twongere uburyo mw'ishure ryacu:


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


Ibi bizocapura


```javascript
hachiko says barf!
```


Nitwakora gutyo nyene ku ngero zibiri zitandukanye z’Imbwa .



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


turaronka


```
hachiko says barf!
bobby says barf!
```


uburyo bwa `speak()` bukoresha `izina` ry'umutungo wa `Imbwa` ihamagarwako.


Iyi ni yo mpamvu nyamukuru ituma amashure abaho: atuma dushobora gusobanura uburyo bukora ku makuru, hanyuma tugahingura ibintu vyinshi bisangiye amakuru "imiterere".


Iyo duhamagaye uburyo kuri kimwe muri ivyo bintu, buzokora ku makuru *ico kintu* gifise.


### Guhindura imiterere y'ikintu


Ibintu biri muri JavaScript birahinduka. Naho umaze kuyirema, urashobora kwongerako ibintu bishasha canke ugakuraho ibisanzweho.


Biremewe, ariko ni ikintu ukwiye gukoresha witonze.


Reka dutangure n’ishure ryacu ryoroshe ry’Imbwa:


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


Kuri iyi nkuru, `Imbwa yanje` ifise umutungo umwe gusa: `izina`. Turashobora kwongerako ibintu bishasha inyuma y’aho biremwe:


```javascript
myDog.age = 5

console.log(myDog.age) // prints 5
```


Turashobora kandi kwongerako uburyo bushasha:


```javascript
myDog.jump = function () {
console.log(`${this.name} jumps!`)
}

myDog.jump() // Fido jumps!
```


Kandi turashobora gukuraho n'ibintu, dukoresheje ijambo ry'ingenzi `delete`.


```javascript
delete myDog.name

console.log(myDog.name) // prints 'undefined'
```


Ivyo birakora, ariko ng’iki ikintu gihambaye co kumenya: Moteri za JavaScript nka V8 (zikoreshwa muri Node.js no mu mucukumbuzi wa Chrome) zikora ningoga iyo ibintu vyawe vyama bifise imiterere imwe. Iyo wongeyeko canke ukuyeho ibintu inyuma y’aho ikintu kiremwe, birashobora gutuma ibintu bigenda buhoro.


Mu porogarama ntoyi, ivyo ntaco bimaze cane. Ariko mu migambi minini (nk’imikino), ni vyiza gutanga urutonde rw’ibintu vyose biri mu wubaka kuva mu ntango, naho woba utabikoresha ubwo nyene. Ivyo bituma igishushanyo c'ikintu kiguma kidahinduka kandi bifasha kode yawe gukora ningoga.


Nk’akarorero, aho kugira ibi:


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


Woshobora gukora


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


Izo verisiyo zompi zirakora, ariko iya kabiri ni nziza ku bijanye n’ugukora. Uriko urabwira moteri imbere ivyiza ikintu cose kizogira, kandi ishobora gukora neza bivanye n’ivyo.


JavaScript iragufasha guhindura ibintu mu mwidegemvyo, ariko iyo ukoresheje amashure, ni vyiza gutegura imbere y’igihe.



### Iragi rifise `raguka` na `super()`


Rimwe na rimwe ushaka gukora ikigo *hafi* kimwe n’ikindi kigo, ariko gifise ibintu bikeyi vy’inyongera.


Aho guhindura imiterere y'ibintu (ivyo nk'uko vyavuzwe imbere ntabwo ari vyiza ku bikorwa), canke gusubira kwandika ivyigwa bishasha kuva mu ntango, JavaScript iraguha uburenganzira bwo gukoresha ikintu citwa **iragi**.


Iragi bisigura ko umugwi umwe ushobora **kwagura** uwundi. Iryo shure rishasha rironka imiterere yose n’uburyo bwose bw’iryo rya kera, kandi urashobora kwongerako canke guhindura ivyo ukeneye.


Reka tuvuge ko dufise umugwi w’ishimikiro witwa `Imodoka`:


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


None rero turashaka gukora ivyigwa vya `Imodoka`. Imodoka ni ubwoko bw’ikinyabiziga, mugabo twoshobora gushaka ko igira ibintu bimwebimwe vy’inyongera canke ubutumwa butandukanye iyo itanguye. Aho kwandika vyose, dushobora gukoresha `extends`:


```javascript
class Car extends Vehicle {
start() {
console.log(`${this.brand} car is ready to drive!`)
}
}
```


Igitigiri ca `Imodoka` ubu **kirara** vyose biva ku `Imodoka`. Ironka umutungo wa `brand`, kandi twasubirije uburyo bwa `start()` na verisiyo yacu bwite.


![](assets/en/4.webp)


Reka tubigerageze:


```javascript
const myCar = new Car("Toyota")
myCar.start()
```


Ibi bicapura:


```
Toyota car is ready to drive!
```


Naho `Imodoka` idafise uwuyikora, irakoresha iyo `Imodoka`. Ariko nimba dushaka kwandika umuhinguzi mu `Car`, turashobora, dukeneye gusa gushiramwo uguhamagara umuhinguzi w'umuvyeyi wayo dukoresheje `super()`.


Uko uko bigenda:


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



Ibi bicapura:


```
Toyota Corolla is ready to drive!
```


Rero kugira ngo tuvuge mu ncamake .



- `extends` bisigura ko umugwi umwe ushingiye ku wundi.
- `super()` ikoreshwa mu guhamagara uwukora ivyigwa uriko uragwiza.
- Iryo tsinda rishasha rironka imiterere yose n’uburyo bwose bw’iryo tsinda ry’intango.
- Ushobora **guhindura** uburyo (nka `start()`) kugira ngo bukore ikintu gitandukanye.


Ivyo birafasha iyo ufise ibintu vyinshi bisa (nk’imiduga, amakamyo, n’amapikipiki) kandi ushaka ko basangira kode ariko bakaguma bitwararika mu buryo bwabo.


### `akarorero ka`


Ijambo ry'ingenzi `instanceof` risuzuma nimba ikintu caremwe kivuye mu mugwi kanaka.


Reka tuvuge ko dufise ishure ryitwa `Ukoresha`:


```javascript
class User {
constructor(username) {
this.username = username
}
}

const regularUser = new User("julia123")

console.log(regularUser instanceof User)
```


Ibi bicapura:


```
true
```


Kwemeza ko `Ukoresha asanzwe` ari `Ukoresha`. Ivyo ni kubera ko `regularUser` yaremwe hakoreshejwe umugwi wa `User`.


Ikora kandi n'amashure **yarazwe**. Akarorero, ng'iyi `Umuyobozi` ishure ryagura `Ukoresha`:


```javascript
class Admin extends User {}

const ourAdmin = new Admin("admin42")

console.log(ourAdmin instanceof Admin)   // true
console.log(ourAdmin instanceof User)    // true
```


Iyo mirongo yompi igarura `ukuri`. Ivyo ni kubera ko `Umuyobozi` ari umugwi mutoyi wa `Ukoresha`, rero `Umuyobozi wacu` ni `Umuyobozi` n'`Ukoresha`


# JavaScript yo hagati

<partId>243f63ab-4f34-5c30-80cb-84ef46f6761d</partId>


## Gufata ikosa

<chapterId>d0206bc5-d386-5e7f-9917-5803f392448c</chapterId>


Uko wandika porogarama zikomeye cane za JavaScript, uzohura n'**amakosa**. Ivyo ni ibintu bitari vyitezwe aho hari ikintu kigenda nabi. Kumbure umuhinduzi ni `undefined` ariko ugerageza kuwukoresha, canke kode imwe imwe ironka ubwoko butari bwo bw'inyungu.


Iyo tutafashe neza ayo makosa, porogarama yacu yoshobora gusenyuka canke igakora mu buryo butamenyekana. JavaScript itanga ibikoresho vyo kumenya no gucungera ayo makosa kugira ngo dushobore kuyafata neza.


### Ikosa risanzwe: gushika ku gaciro kuri `utasobanuwe`


Ehe ikintu gisanzwe gitera ikosa:


```javascript
const user = undefined
console.log(user.name)
```


Niwakoresha iyi kode, uzobona ikosa risa n’iri:


```
TypeError: Cannot read properties of undefined (reading 'name')
```


Ivyo ni JavaScript ikubwira iti: “Hey, wagerageje kuronka umutungo wa `izina` mu kintu `kitasobanuwe`, kandi ivyo nta co bimaze.” Kandi nk’uko ushobora kubibona, iyo ikosa nk’iryo ribaye, porogarama irahagarika gukora kiretse wanditse kode yo kuyifata no kuyikoresha.


### `gutera ikosa


Rimwe na rimwe ushaka gukoresha amaboko **gutera ikosa** muri kode yawe. Muri ivyo, ukoresha ijambo ry'ingenzi `gutera`.


```javascript
throw new Error("This is a custom error message")
```


Ivyo bica bihagarika porogarama maze bikacapura:


```
Uncaught Error: This is a custom error message
```


Ushobora gukoresha `gutera` kugira ngo ushire mu ngiro amategeko muri porogarama yawe. Nk'akarorero:


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


Ihamagara rya kabiri ritera ikosa kuko kugabanya na zero ntivyemewe muri aka karorero.


### Gufata amakosa na `gerageza...fata`


Niba udashaka ko porogarama yawe ihungabana iyo habaye ikosa, urashobora gufata ikosa ukoresheje `try...catch` block. Ivyo birafasha iyo ushaka ko porogarama yawe **ikomeza** naho hari ikintu conanirwa.


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log("Oops! Something went wrong.")
}
```


Igisohoka:


```
Oops! Something went wrong.
```


Ehe ingene bigenda:



- Kode iri imbere mu gice ca `try` irageragezwa ubwa mbere.
- Iyo habaye ikosa, JavaScript **isimbira ku gice ca `gufata`**, igasimbuka igice gisigaye c'igice ca `kugerageza`.
- Igipande ca `catch` kirakira ikosa, rero ushobora kuricapura, canke kurifata mu bundi buryo, nk'akarorero


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log(`The message of the error was: "${error.message}"`)
}
```


Igisohoka:


```
The message of the error was: "Cannot read properties of undefined (reading 'name')"
```


### 'Iherezo` ububiko


Ushobora kandi kwongerako `iherezo` ububiko. Iyi ni kode **yama ikora**, haba hariho ikosa canke atarivyo.


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


Igisohoka:


```
Trying something risky...
Caught the error: Uh oh!
This will run no matter what.
```


## Kwirinda ibikoko

<chapterId>db12d9f6-5806-514c-998e-0ae24805104e</chapterId>


Iki gice kirerekana imitego imwe imwe isanzwe muri JavaScript, n’ingene woyirinda.


### `var` na Assignment ata n'itangazo


Mu kode ya kera ya JavaScript, ibihinduka vyamenyeshwa kenshi hakoreshejwe ijambo ry'ingenzi `var`. Udakunze `let` na `const`, ivyo mwamaze kwiga, `var` yoshobora kwigenza mu buryo butera urujijo.


Nk'akarorero:


```javascript
{
var message = "hello"
}
console.log(message)
```


Ushobora kwitega ko `ubutumwa` buzoba buri imbere mu gice gusa, ariko ntaco buvuze. `var` yirengagiza uburebure bw'ibarabara kandi ituma umuhinduzi aboneka mu gikorwa cose canke dosiye.


Ivyo bishobora gutuma umuntu agira inyifato atari yiteze cane cane muri porogarama nini. Kubera iyo mpamvu, kode ya JavaScript ya none ikwiye kwama ikoresha `let` canke `const` aho gukoresha `var`.


N'ikibi kuruta, JavaScript iragufasha gutanga agaciro ku bihinduka **utabimenyesheje na gato**:


```javascript
function greet() {
user = "Alice"
}
greet()
console.log(user) // prints "Alice"
```


Ibi bituma haba umuhinduzi mushasha w'isi yose `izina` ata n'itangazo. Ivyo bishobora gushika mu gacerere kandi bikajana ku bikoko ari Hard vyo gukurikirana, cane cane iyo ari ikosa ryo kwandika gusa. Igihe cose umenyeshe ibihinduka ukoresheje `let` canke `const`.


### Uburyo bugoyagoya


JavaScript yandikwa nabi, bisobanura ko ihindura ubwo nyene agaciro kuva ku bwoko bumwe gushika ku bundi iyo bikenewe. Ivyo vyitwa uguhatira umuntu gukora ikintu, kandi naho bishobora kuba vyiza, akenshi bituma umuntu agira ivyo akora bitera urujijo.


Nk'akarorero:


```javascript
console.log("5" + 1)    // "51"
console.log("5" - 1)    // 4
console.log(true + 1)   // 2
console.log(null + 1)   // 1
```


Muri izo ngero, JavaScript iragerageza gutekereza ku co washaka kuvuga. Rimwe na rimwe ihindura imirongo mu mibare, canke ama boolean mu mibare, canke imirongo mu mirongo. Ivyo birashobora gutuma kode yawe yigenza mu buryo utari witeze.


Kumenya uburyo bwo kwandika bwa JavaScript bugoyagoya ni ikintu gihambaye. Iyo ibintu bitanguye gukora bitangaje, bishobora kuba bivuye ku guhatirwa kw’ubwoko butategerezwa.


### `"koresha bikomeye"`


Ushobora gukoresha uburyo bukomeye cane buhindura amakosa amwe amwe acereje mu makosa nyayo, kandi bukaguhagarika gukoresha bimwe mu bintu biteye akaga cane vyo mu rurimi.


Kugira ngo ushoboze ubu buryo bukomeye, wongereko uyu murongo hejuru ya dosiye yawe canke igikorwa:


```javascript
"use strict"
```


Nk'akarorero:


```javascript
"use strict"
name = "Alice" // ReferenceError: name is not defined
```


Ata buryo bukomeye, JavaScript yoshobora kurema mu gacerere umuhinduzi w'isi yose witwa `izina`. Ariko n’uburyo bukomeye, ivyo bica bihinduka ikosa nyaryo, bikagufasha gufata ibikoko imbere y’igihe.


Uburyo bukomeye kandi burazimya ibintu bimwebimwe vya kera vya JavaScript, kandi bugatuma kode yawe yoroha guhindura no kubungabunga.


## Agaciro vs Ishingiro

<chapterId>bb898425-dc2f-5e5c-864b-0cb7a4a9aea9</chapterId>


JavaScript ifata ubwoko butandukanye bw'agaciro mu buryo butandukanye.


Hariho agaciro **kopiwa** iyo ushize umuhinduzi.


Abandi **basangizwa** iyo ubashize ku mpinduka nshasha, rero iyo uhinduye imwe, n'iyindi irahinduka.


### Guca ku gaciro


Iyo agaciro kaciye **ku gaciro**, JavaScript irakora **kopi** yayo.


Rero iyo uhinduye kimwe, ntaco bihindura ku kindi.


Ibi bishika ku bwoko bwa kera, nka:



- imibare
- imirongo
- booleans (`ukuri` n'ikinyoma`)
- 'ubusa`
- 'bitasobanuwe`


Reka turabe akarorero:


```javascript
let a = 5
let b = a

b = 10

console.log(a) // 5
console.log(b) // 10
```


Twahaye `b` agaciro ka `a`, ariko hanyuma duhindura `b` tuyigira `10`.


Kubera ko imibare iherezwa n'agaciro, JavaScript yakopiye `5` muri `b`. `5` muri `b` yigenga kuri `5` y'umwimerere muri `a` rero guhindura agaciro ka `b` ntaco vyari bimaze kuri `a`.


Reka tugerageze n’urudodo:


```javascript
let name1 = "Alice"
let name2 = name1

name2 = "Bob"

console.log(name1) // Alice
console.log(name2) // Bob
```


Na none, guhindura `izina2` ntivyagira ico bikoze kuri `izina1`, kuko imirongo nayo irenganywa n’agaciro.


Ivyo nyene bishika iyo ushizeho ivy'intango ku gikorwa: birakopwa. Rero igikorwa ntigishobora guhindura ivy’umwimerere.


```javascript
function plusOne(x) {
x = x + 1
}

let number = 5

plusOne(number)

console.log(number) // 5
```


Naho imbere mu gikorwa `1` congerewe kuri `x`, `umubare` w’intango ntiwahindutse.


Ivyo ni kubera ko **kopi** gusa ari yo yaciye mu gikorwa.


### Guca ku nsiguro


Ibintu bica **biciye ku nsiguro**.


Ivyo bisigura ko aho kubikopa, JavaScript itanga gusa **reference** kuri yo, kandi iyo uyihinduye, ibindi bihinduka vyose vyerekana kuri yo navyo bizobona ihinduka.


Nk'akarorero:


```javascript
const person1 = { name: "Alice" }
const person2 = person1

person2.name = "Bob"

console.log(person1.name) // Bob
console.log(person2.name) // Bob
```


Bompi `umuntu1` na `umuntu2` berekana ikintu kimwe kiri mu ciyumviro.


Rero igihe twahindura `umuntu2.izina`, twahinduye kandi `umuntu1.izina`, kuko bompi baraba ikintu kimwe.


Amabara ni ibintu, rero reka tugerageze ivyo nyene n’amabara:


```javascript
const list1 = [1, 2, 3]
const list2 = list1

list2.push(4)

console.log(list1) // [1, 2, 3, 4]
console.log(list2) // [1, 2, 3, 4]
```


Twasunikiye `4` muri `list2`, ariko `list1` nayo yarashikiwe, kuko zompi zivuga ku rutonde rumwe.


Reka turabe ibiba iyo dushize ikintu ku gikorwa:


```javascript
function rename(user) {
user.name = "Charlie"
}

const person = { name: "Dana" }

rename(person)

console.log(person.name) // Charlie
```


Ico gikorwa carahinduye ikintu! Ivyo ni kubera ko yaronse **reference** ku kintu c’umwimerere `umuntu`.


Nta n’imwe yaronse kopi. Yaronse uburenganzira bwo gushika ku kintu c’intango, kandi n’ivyo yararonse ubushobozi bwo kugihindura.


Ni vyiza kwibuka iyo ntandukaniro, kuko ahandi ho kode yacu yoshobora kwigenza mu buryo butandukanye n’ivyo twiteze. Nk’akarorero, twoshobora kwandika igikorwa twizigiye ko kitazohindura imvo zironka, maze tukamenya mu nyuma ko mu vy’ukuri cariko kirazihindura (kubera ko zari ibintu, rero zaciye biciye ku nsiguro).


## Gukorana n'imikorere

<chapterId>e0d277a8-c642-5af7-9e53-dee27c811967</chapterId>


Waramaze kwiga ingene womenyesha no gukoresha ibikorwa muri JavaScript. Ariko JavaScript iraguha ibikoresho vyinshi vyo gukorana n’ibikorwa mu buryo bukomeye.


### Imikorere y'umwampi


Imikorere y'umwampi ni uburyo bugufi bwo kwandika imikorere. Aho gukoresha ijambo ry'ingenzi `function`, dukoresha umwampi (`=>`).


Aha niho hari igikorwa gisanzwe:


```javascript
function greet(name) {
return `Hello, ${name}!`
}
```


Verisiyo y'umwampi isa n'iyi:


```javascript
const greet = (name) => {
return `Hello, ${name}!`
}
```


Niba umukozi ufise **umurongo umwe gusa**, ushobora gusimbuka amabara maze `ugasubire`:


```javascript
const greet = (name) => `Hello, ${name}!`
```


Niba umukozi ufise **umurongo umwe gusa**, ushobora no gusimbuka uturongo tukikuje umurongo:


```javascript
const greet = name => `Hello, ${name}!`
```


Imikorere y'umwampi irasanzwe cane muri JavaScript ya none, kuko ishobora guserura imikorere yoroshe n'ivyuma bike cane.


### Imirongo mburabuzi


Rimwe na rimwe ushaka ko igikorwa gifise **agaciro mburabuzi** iyo ata mpamvu irenga.


Ivyo ushobora kubikora gutya:


```javascript
function sayHello(name = "friend") {
console.log(`Hello, ${name}!`)
}

sayHello("Alice") // Hello, Alice!
sayHello()        // Hello, friend!
```


Agaciro mburabuzi `"umugenzi"` gakoreshwa iyo ataco kinyuze.


### Gukwirakwiza ibigenderwako (`...`)


Bimeze gute nimba igikorwa cawe gifata umubare w’imvo zihinduka?


Ushobora gukoresha **umukoresha wo gukwiragiza** (`...`) kugira ngo ubikoranirize hamwe mu rutonde:


```javascript
function logAll(...items) {
console.log(items)
}

logAll(1, 2, 3) // [1, 2, 3]
logAll("a", "b") // ["a", "b"]
```


Ushobora rero gukoresha uruzitiro kugira ngo ukoreshe ikintu cose:


```javascript
function logEach(...items) {
for (const item of items) {
console.log(item)
}
}
```


Igikoresho co gukwiragiza ni ngirakamaro iyo utazi ingene arguments zizoca.


### Urutonde rwo hejuru rw'imikorere


**Igikorwa c'urutonde rwo hejuru** ni igikorwa:



- ifata ikindi gikorwa nk'inyungu
- na/canke igarura igikorwa nk'igisohoka


Aha niho akarorero koroshe:


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


Ibi bicapura:


```
Hello, friend!
Hello, friend!
```


Turashobora kuyirungikira umwampi:


```javascript
runTwice(
() => console.log("Hello!")
)
```


Ibi bicapura:


```
Hello!
Hello!
```


Ushobora kandi kwandika ibikorwa **bigarura** ibindi bikorwa:


```javascript
function makeGreeter(name) {
return () => console.log(`Hi, ${name}`)
}

const greetAlice = makeGreeter("Alice")
const greetBob = makeGreeter("Bob")

greetAlice() // Hi, Alice
greetBob() // Hi, Bob
```


`makeGreeter` ni igikorwa cubaka izindi nshingano. Yakira urudodo maze igarura igikorwa gishasha gikoresha urwo rudodo mu guhamagara kwayo `console.log`.


Ubwo bwoko bw'akarorero burakomeye cane, kuko bugufasha gusiga "imyobo" mu bikorwa vyawe ushobora kwuzuza mu nyuma n'inyifato ukeneye.


### `ikarita()`, `akayunguruzo()`, `kugabanya()`


JavaScript iraguha uburyo ngirakamaro bushizwemwo bwo gukoresha n'amabara.


Ubu buryo bufata ibikorwa nk'imvo, rero navyo ni ibikorwa vy'urutonde rwo hejuru.


`map()` ihindura ikintu cose kiri mu rutonde mu kindi kintu.


Akarorero:


```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map(x => x * 2)

console.log(doubled) // [2, 4, 6]
```


Umubare wose urakubitwa kabiri, maze igisubizo kikaba ari urutonde rushasha.


`filter()` ikuraho ibintu mu rutonde iyo bitaciye mu kigeragezo.


Akarorero:


```javascript
const numbers = [1, 2, 3, 4, 5]
const numbersGreaterThanTwo = numbers.filter(x => x > 2)

console.log(numbersGreaterThanTwo) // [3, 4, 5]
```


Ivyinjijwe mu rutonde vyonyene aho `x > 2` ivyangombwa bigarura `ukuri` nivyo bigumwa.


`reduce()` ikoreshwa mu gufatanya ibintu vyose biri mu rutonde mu gaciro kamwe.


Akarorero:


```javascript
const numbers = [1, 2, 3, 4]
const total = numbers.reduce((current, next) => current + next)

console.log(total) // 10
```


`reduce` ica mu nzira kandi, muri aka karorero, ikoresha umukozi `+` hagati ya `1` na `2`, hanyuma hagati y'ivyavuyemwo `3` na `3`, hanyuma hagati y'ivyavuyemwo `6` na `4`, gushika ifise umubare w'ibintu vyose vyinjijwe mu nzira (ari vyo 10).


Ushobora gukoresha `reduce()` ku bintu vyinshi nk'imibare yose, imyerekano, canke kwubaka agaciro gashasha intambwe ku yindi.


Ubu buryo (`ikarita`, `akayunguruzo`, `kugabanya`) ni ibikoresho bikomeye vyo gukora amakuru ata kwandika inziga z'amaboko.


Ushobora mbere kubifatanya mu ruhererekane rw'ibikorwa, nk'ibi:


```javascript
const numbers = [1, 2, 3, 4, 5]

const result = numbers
.map(n => n * 2)        // Double each entry, obtain [2, 4, 6, 8, 10]
.filter(n => n > 3) // Keep only the entries bigger than 3, so you get [4, 6, 8, 10]
.reduce((n1, n2) => n1 + n2) // Adds them: 4 + 6 + 8 + 10 = 28

console.log(result) // 28
```


## Gukorana n'ibintu

<chapterId>7842aada-f009-5518-b8e3-1104e166a035</chapterId>


Muri iki gice, tuzokwiga ibikoresho bikomeye kandi biteye imbere gatoyi vyo gukorana n’ibintu muri JavaScript.


### Itunga ry'abantu ku giti cabo


Rimwe na rimwe, dushaka guhisha umutungo w’ikintu kugira ngo ntushobore guhindurwa canke gushikirwa hanze y’ico kintu. JavaScript iduha uburyo bwo kubikora dukoresheje `#` imbere y'izina ry'umutungo. Ivyo bituma haba **umutungo w'ibanga**, ushobora gushikwako gusa uri imbere mu kigo.


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


Ivy’abantu ku giti cabo birafasha igihe ushaka gukingira amahinduka y’impanuka.


### `ibidahinduka` imiterere


Rimwe na rimwe, ushaka ko umutungo uba uw'umugwi ubwawo, atari uw'ikintu cose urema uvuye muri uwo mugwi. Ivyo nivyo `static` igenewe. Igikoresho `static` kiri mu kigo kandi ibintu vyose vyo muri ico kigo bizokwerekeza kuri co.


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


Ivyo ni ngirakamaro ku kubika amakuru asangiye n'uburyo bujanye n'umugwi wose w'ibintu, atari kimwe gusa.


### `kuronka` na `gushinga`


Mu JavaScript, `get` na `set` biguha uburenganzira bwo gukora ibiranga *bisa* n'ibihinduka bisanzwe, ariko mu vy'ukuri bikoresha kode idasanzwe mu nyuma.


Uburyo bwa `get`ter burakora iyo ugerageje *gusoma* umutungo. Imenyeshwa mu kwandika `get` imbere y'uburyo bufise izina ry'umutungo.


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


Naho `fullName` atari umutungo usanzwe, turashobora kuyikoresha nk'imwe, kandi inyuma y'ivyo ikoresha `get` kugira ngo yubake izina ryose.


Uburyo bwa `set`ter burakora iyo *utanga* agaciro ku mutungo. Bituma ushobora kugenzura ibishika iyo umuntu agerageje guhindura ako gaciro. Imenyeshwa mu kwandika `set` imbere y'uburyo bufise izina ry'umutungo.


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


Iyo dukoze `user.fullName = "John Smith"`, ikoresha uburyo bwa `set` maze igahindura `Izina rya mbere` n'agaciro k'Izina rya nyuma.


Rero naho bimeze nk’aho turiko turashiraho umuhinduzi woroshe, mu vy’ukuri turiko turavyura ubuhinga bushasha bw’ibindi bintu.


## Urufunguzo n'agaciro

<chapterId>01a397b8-c12a-5c39-82b3-6d9ebbb72a29</chapterId>


Igikoresho cose kiri mu kintu ca JavaScript gifise **urufunguzo** (naco citwa izina ry'igikoresho) n'agaciro**.


Nk'akarorero:


```javascript
const user = {
name: "Alice",
age: 30
}
```


Muri iki kintu, `"izina"` na `"imyaka"` ni imfunguruzo, na "Alice" na `30` ni agaciro kavyo.


### Ukwinjira


Rimwe na rimwe, ntumenya izina ry’ikintu imbere y’igihe...kumbure uriko urarironka mu vyo umukoresha yinjiza, canke ukarisoma mu mpinduka. Ushobora kuyironka ukoresheje **inyandiko y'ibikingi**, nka `Ikintu canje["Izina ry'Urufunguzo"]`.


```javascript
const user = {
name: "Alice",
age: 30
}

console.log(user["name"]) // Alice
```


Twaraciye urudodo `izina` ku kintu kugira ngo turonke agaciro kahuye.


Turashobora kubika urufunguzo ku gihinduka maze tukarukoresha kugira ngo turonke agaciro kahuye mu nyuma, nka


```javascript
const user = {
name: "Alice",
age: 30
}

const key = "name"

console.log(user[key]) // Alice
```


### Inguvu Assignment


Ushobora kandi kurema canke guhindura ibintu ukoresheje ibihinduka nk'imfunguruzo.


```javascript
const settings = {}

const key = "theme"
settings[key] = "dark"

console.log(settings) // { theme: "dark" }
```


Ivyo birafasha iyo ushaka kwubaka ikintu intambwe ku yindi. Nk'akarorero:


```javascript
const user = {}

user["username"] = "bananaFan123"
user["email"] = "banana@fruit.com"

console.log(user)
// { username: "bananaFan123", email: "banana@fruit.com" }
```


Ushobora mbere gukoresha urufunguzo ruhinduka *mu gihe urema* ikintu ukoresheje ibifunga:


```javascript
const key = "language"
const config = {
[key]: "JavaScript"
}

console.log(config.language) // JavaScript
```


Ivyo vyitwa **umutungo uharuwe**. Agaciro kari mu bifunga vy'inzira karasuzumwa, maze igisubizo kigakoreshwa nk'urufunguzo.


### Ubwoko bw'ikimenyetso


Uretse imirongo, JavaScript iraguha uburenganzira bwo gukoresha ubwoko budasanzwe bwitwa `Ikimenyetso` nk'urufunguzo rw'ikintu.


Reka dutangure n’akarorero koroshe:


```javascript
const id = Symbol("userID")

const user = {
name: "Bob",
[id]: 12345
}

console.log(user[id]) // 12345
```


Muri aka karorero, `id` ni Ikimenyetso. Si umugozi, ariko uracariko urakora nk’urufunguzo. Niwagerageza kwinjira `user` kuri console, uzobona ibi:


```javascript
console.log(user) // { name: 'Bob', [Symbol(userID)]: 12345 }
```


Ikindi kintu gihambaye: ikimenyetso cose urema ni ikidasanzwe, naho coba kiremwe hakoreshejwe urudodo rumwe.


```javascript
const a = Symbol("label")
const b = Symbol("label")

console.log(a === b) // false
```


Ibimenyetso bigufasha gusobanura imfunguruzo zitazohura n'imfunguruzo zisanzwe. Nk'akarorero, reka tuvuge ko ufise ikintu gifise umutungo `izina`, ariko ico kintu kizoshobora guhindurwa n'umukoresha muri kazoza, mu buryo udashobora kumenya, kandi uwo mukoresha yoshobora kwongerako umutungo `izina` na we nyene. Iyo `izina` ry'umwimerere risobanurwa n'urudodo, ryari kwandikwa n'irishasha, nk'ibi:


```javascript
const obj = {
name: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy' }
```


Nitwakoresha ikimenyetso aho:


```javascript
const name = Symbol("name")

const obj = {
[name]: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy', [Symbol(name)]: 'John' }
```


Nk'uko ushobora kubibona, umutungo w'intango `izina` urazigama muri ubu buryo. Ivyo birashobora kuba ngirakamaro mu bihe bimwebimwe vy’urubibi.


## Ibintu vy'ingirakamaro

<chapterId>516e74c8-2a11-545a-a4d1-c2cabb91a273</chapterId>


JavaScript iduha ibintu vy’ingirakamaro vyubatswemwo bidufasha gukora ibintu nk’ugukosora n’ibikorwa vy’imibare.


### Ubundi buryo bwo `guhoza`


Waramaze kubona `console.log`, icapa agaciro ku mugaragaro.


Hariho ubundi buryo ngirakamaro buboneka ku kintu ca `console` bushobora kugufasha gukosora porogarama zawe.


#### `uguhoza.kugabisha`


Icapura ubutumwa mu muhondo (canke n'ikimenyetso c'imburi mu bidukikije bimwe bimwe):


```javascript
console.warn("This is just a warning.")
```


#### `ikosa


Icapura ubutumwa mu mutuku, nk'ikosa:


```javascript
console.error("Something went wrong!")
```


#### `imeza`


Erekana urutonde canke ikintu nk'imbonerahamwe:


```javascript
const users = [
{ name: "Alice", age: 25 },
{ name: "Bob", age: 30 }
]

console.table(users)
```


Ibi bicapura imbonerahamwe nka:


```
┌─────────┬────────┬─────┐
│ (index) │  name  │ age │
├─────────┼────────┼─────┤
│    0    │ 'Alice'│  25 │
│    1    │ 'Bob'  │  30 │
└─────────┴────────┴─────┘
```


Ivyo birashobora kuba ngirakamaro mu kubona amakuru atunganijwe.


#### `igihe.co guhoza` na `uguhoza.igiheIherezo`


Ushobora gupima igihe ikintu gifata:


```javascript
console.time("timer")
for (let i = 0; i < 1000000; i++) {}
console.timeEnd("timer")
```


Ibi bicapura ikintu nk'iki:


```
timer: 2.379ms
```


Ni ngirakamaro ku bipimo bimwe bimwe vyoroshe vy’ibikorwa.


### Ikintu `Imibare`


JavaScript iguha ikintu `Imibare` gifise uburyo ngirakamaro bwo gukora imibare.


#### `Imibare.imburakimazi()`


Igarura umubare udasanzwe hagati ya 0 (harimwo) na 1 (harimwo):


```javascript
const r = Math.random()
console.log(r)
```


Akarorero k'igisohoka:


```
0.4387429859
```


#### `Imibare.hasi()` na `Imibare.igisenge()`



- `Imibare.hasi(n)` izunguruka **hasi** ku mubare wose uri hafi
- `Imibare.igisenge(n)` izunguruka **hejuru** ku mubare wose uri hafi


```javascript
console.log(Math.floor(4.9)) // 4
console.log(Math.ceil(4.1))  // 5
```


#### `Imibare.uruziga()`


Izunguruka ku mubare wose uri hafi:


```javascript
console.log(Math.round(4.4)) // 4
console.log(Math.round(4.6)) // 5
```


#### `Imibare.max()` na `Imibare.min()`


Igarura agaciro kanini canke gato kuva ku rutonde rw'imibare:


```javascript
console.log(Math.max(5, 9, 3)) // 9
console.log(Math.min(5, 9, 3)) // 3
```


#### `Imibare.pow()` na `Imibare.sqrt()`



- `Imibare.pow(a, b)` iguha `a` ku bubasha bwa `b`
- `Imibare.sqrt(n)` iguha umuzi w'inzira ya `n`


```javascript
console.log(Math.pow(2, 3))   // 8
console.log(Math.sqrt(16))    // 4
```


# JavaScript iteye imbere

<partId>72c30671-ca20-5617-92a5-d5ba7aa38c93</partId>


## Ibindi bitabo

<chapterId>a9a70c6d-a343-5a46-a383-e288bc2700e3</chapterId>


JavaScript iduha ubwoko bumwe bumwe bw’amakoraniro budasanzwe burenze amabara n’ibintu bisanzwe. Ivyo birimwo `Ikarita` na `Igice`.


Bigufasha kubika no gucunga imigwi y’agaciro, ariko bikora mu buryo butandukanye n’ivyo wabonye gushika ubu.


`Ikarita` ni ihuriro ry'ibice bibiri vy'agaciro k'urufunguzo**, nk'ikintu. Ariko rero, hariho ibintu bihambaye bitandukanye:



- Imfunguruzo zishobora kuba **agaciro ako ari ko kose** atari imirongo gusa.
- Urutonde rw’ibintu rurazigama.
- Irafise uburyo bwubatswemwo kugira ngo gukorana na yo vyorohe.


Ushobora kurema ikarita nshasha nk'iyi:


```javascript
const myMap = new Map()
```


Ivyo bica bituma haba ikarata ata co imaze. Kugira ngo wongereko ivyinjijwe, koresha `ikarata yanje.set(urufunguzo, agaciro)`:


```javascript
myMap.set("name", "Alice")
```


Ibi vyongera urufunguzo `"izina"` n'agaciro `"Alice"`.


Ushobora kandi gukoresha umubare nk'urufunguzo:


```javascript
myMap.set(42, "The answer")
```


Kandi mbere n'ikintu nk'urufunguzo:


```javascript
const objKey = { id: 1 }
myMap.set(objKey, "Object as key")
```


Ivyo ntivyokorana n’ibintu bisanzwe, vyemera gusa imfunguruzo z’urudodo.


Kugira ngo **uronke agaciro**, koresha `ikarita yanje.kuronka(urufunguzo)`:


```javascript
console.log(myMap.get("name"))     // Alice
console.log(myMap.get(42))         // The answer
console.log(myMap.get(objKey))     // Object as key
```


Kugira ngo **usuzume nimba urufunguzo ruriho**, koresha `ikarita yanje.ifise(urufunguzo)`:


```javascript
console.log(myMap.has("name")) // true
```


Kugira ngo **ukureho urufunguzo**, koresha `ikarita yanje.gukuraho(urufunguzo)`:


```javascript
myMap.delete("name")
```


Kugira ngo **ukureho ikarita yose**, koresha `ikarita yanje.kuraho()`:


```javascript
myMap.clear()
```


Ikarata ni nziza cane mu gucunga amakoraniro manini y'agaciro, kuko gushika ku gaciro ku ikarita nini bitanga kenshi ubushobozi bwiza kurusha ku kintu kinini.


### 'Gushiraho`


`Itsinda` ni ihuriro ry'agaciro gusa** (nta mfunguruzo), aho agaciro kose gategerezwa kuba **kadasanzwe**. Ivyo bisigura:



- Ntushobora kugira agaciro kamwe incuro zibiri
- Agaciro kabitswe mu buryo ubishizeko


Ushobora kurema umugwi nk'uyu:


```javascript
const mySet = new Set()
```


Kugira ngo **wongere agaciro**, koresha `MySet.add(agaciro)`:


```javascript
mySet.add(1)
mySet.add(2)
mySet.add(2) // duplicate, will be ignored
```


Naho twagerageje kwongerako `2` incuro zibiri, iyo seti izogumana kopi imwe gusa.


Kugira ngo **ugenzure nimba agaciro kari mu mugwi**, koresha `umugwi wanje.ufise(agaciro)`:


```javascript
console.log(mySet.has(2)) // true
console.log(mySet.has(3)) // false
```


Kugira ngo **ukureho agaciro**, koresha `mySet.delete(agaciro)`:


```javascript
mySet.delete(2)
```


Kugira ngo **ukureho vyose**, koresha `Iseti yanje.kuraho()`:


```javascript
mySet.clear()
```


`Itsinda` ni ngirakamaro iyo ushaka kubika ihuriro ry'agaciro kadasanzwe udakeneye kugenzura n'amaboko ko hariho ibisubizo:


```javascript
const numberArray = [1, 2, 2, 3, 4, 4, 4, 5]

const numberSet = new Set(numberArray)

console.log(numberSet) // Set(5) { 1, 2, 3, 4, 5 }
```


`Set` irinda ivyo kwisubiriza kuri wewe.


## Abasubiramwo

<chapterId>61d24e5e-b7e4-541a-8322-778f61f26a72</chapterId>


Ibintu vyinshi muri JavaScript ushobora gucako (nk'imirongo, imirongo, amakarata, imigwi) ni **ibisubirwamwo**: bishobora gutanga ibisubirwamwo ku birimwo.


**Iterator** ni ikintu kidasanzwe muri JavaScript kigufasha guca mu rutonde rw'ibintu **kimwe ku kindi**.


### `Ikintu` abasubiramwo


Udakunze imirongo canke ikarita, ibintu bisanzwe **ntibisubirwamwo** na `ku...vya`. Niwagerageza ibi:


```javascript
const user = {
name: "Alice",
age: 30
}

for (const value of user) {
console.log(value)
}
```


Uzoronka ikosa:


```
TypeError: user is not iterable
```


Ivyo ni kubera ko ibintu bisanzwe bitagira iterator yubatswemwo. Ariko JavaScript iraguha ibindi bikoresho vyo kubizungurukako.


#### `Ikintu.imfunguruzo()`


Ushobora gukoresha `Ikintu.imfunguruzo(obj)` kugira ngo ubone urutonde rw'ikintu **imfunguruzo**, hanyuma ukagizungurukako:


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


Ibi bicapura:


```
name
age
```


#### `Ikintu.agaciro()`


Kugira ngo ukoreshe **agaciro**, koresha `Ikintu.agaciro()`:


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


Ibi bicapura:


```
Alice
30
```


#### `Ikintu.vyinjira()`


Niba ushaka **urufunguzo n'agaciro**, koresha `Ikintu.ivyinjijwe()`:


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


Ibi bicapura:


```
name is Alice
age is 30
```


Naho ibintu bidashobora gusubirwamwo, ubu buryo buraguha uburenganzira bwo kuronka ibirimwo mu buryo bukora neza na `for...of`.


Ariko none abasubiramwo bakora gute?


### `Ikimenyetso.iterateri`


Ibanga ry'inyuma y'ibisubirwamwo vyose ni **ikimenyetso** kidasanzwe citwa `Symbol.iterator`.


Ico kimenyetso ni urufunguzo rwubatswemwo rubwira JavaScript ngo: “Iki kintu gishobora gusubirwamwo.”


Iyo uhamagara `Iterable yanje[Ikimenyetso.isubiramwo]()`, JavaScript iragusubiza **ikintu gisubiramwo** gifise uburyo `.next()`.


Reka turabe uko ivyo bisa:


```javascript
const colors = ["red", "green", "blue"]

const iterator = colors[Symbol.iterator]()

console.log(iterator.next()) // { value: 'red', done: false }
```


Ihamagara ryose kuri `.next()` riguha agaciro gakurikira. Iyo birangiye, biragaruka:


```javascript
{ value: undefined, done: true }
```


### `ibikurikira()`


Uburyo `.next()` bukoreshwa kugira ngo ubone ikintu gikurikira mu rutonde.


Igihe cose uhamagara `.next()`, ubona ikintu gifise imfunguruzo zibiri:



- `agaciro`: ikintu kiriho ubu
- `vyakozwe`: boolean ikubwira nimba ugusubiramwo kwarangiye


Reka dukore akarorero kuzuye:


```javascript
const names = ["Lina", "Tom", "Eva"]      // declare an array
const iterator = names[Symbol.iterator]() // use the Symbol.iterator function to get an iterator for this array

let result = iterator.next()              // get the first element of the array

while (!result.done) {                    // repeat this loop until you reach the last element of the array, which is marked with { done: true }
console.log(result.value)               // print the value of each element
result = iterator.next()                // get the next element of the array
}
```


Ibi bicapura:


```
Lina
Tom
Eva
```


Uko ni ko uruzitiro rwa `for...of` rukora munsi y'igipfukisho: rukoresha iyi nzira na `.next()`.


Uzoronka igisubizo nk’ico nyene n’


```javascript
const names = ["Lina", "Tom", "Eva"]

for (const result of names) {
console.log(result)
}
```


### Guhindura ishure risubirwamwo


Ushobora kandi gusobanura **umugwi wawe ushobora gusubirwamwo** wongeyeko uburyo bwa `[Ikimenyetso.iterator]()`.


Reka tuvuge ko dushaka ikigo giserukira **urutonde rw’imibare**, nka kuva kuri 1 gushika kuri 5.


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


Ibi bicapura:


```
1
2
3
4
5
```


Ehe ibiriko biraba:



- Twarasobanuye ikigo `Urutonde`
- Imbere mw'ishure, twashize mu ngiro `[Ikimenyetso.iterator]()`, rero JavaScript irazi uko yoyisubiramwo
- Uburyo bwa `next()` burasubiza umubare wose umwe umwe
- Iyo tugeze ku `iherezo`, igarura `{ vyakozwe: ukuri }`


Ubu ikigo cacu ca `Range` gikora nk'urutonde, kandi turashobora kurukoresha mu nzira iyo ari yo yose yiteze iterable.


### Imikorere y'umuyagankuba n'umusaruro


Kugira ngo vyorohe gukora iterators, JavaScript iraguha **ibikorwa vy'umuhinguzi**, ikoresheje ijambo ry'ingenzi `ibikorwa*` (ni `ibikorwa` rifise `*` ku mpera) n'ijambo ry'ingenzi `umwimbu`.


Reka tugerageze:


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


Buri `umwimbu` utanga agaciro, kandi **ihagarika** igikorwa gushika ikindi `.next()` gihamagawe.


Ushobora kandi guca ku muyagankuba ufise `ku...wa`:


```javascript
for (const num of numberGenerator()) {
console.log(num)
}
```


Ibi bicapura:


```
1
2
3
```


## Guhuza n'uguhamagara

<chapterId>f3fc76ca-b3ef-54eb-a06e-501007002054</chapterId>


Gushika ubu, kode yacu yari **synchronous**: ikora umurongo umwe ku wundi, mu buryo bubereye. Ariko hari ibintu vyo mw’isi nyakuri bifata umwanya, kandi ntidushaka ko porogarama yose ihagarara mu gihe turindiriye.


Muri iki gice turaza kuzana iciyumviro gishasha: **uguhuza**. Bituma dushobora gukoresha urutonde rw’ibintu bigenda. Ivyo ni ngirakamaro iyo ukorana n'ibintu nk'ibihe, inyungu y'ukoresha, canke gusoma amadosiye kuri disiki. JavaScript itanga ibikoresho bitandukanye vyo gukora ibikorwa bihuye.


### `gushingaIgihe`


Igikorwa `setTimeout` kigufasha **gukoresha igikorwa hanyuma**, inyuma y'igihe kanaka.


Akarorero:


```javascript
console.log("Start")

setTimeout(
() => console.log("This runs after 2 seconds"),
2000
)

console.log("End")
```


Ibi bicapura:


```
Start
End
This runs after 2 seconds
```


Naho `setTimeout` iboneka hagati muri kode, ntibuza ibindi. Ahubwo, itegekanya igikorwa co gukora **mu nyuma**, maze igaca igenda.


Ico `2000` bisigura amasegonda 2000 (ni ukuvuga amasegonda 2).

Aha niho hari amajambo menshi kandi ashobora gukoreshwa n'abatanguzi mu bice vya **Callbacks** na **Promise**, hakoreshejwe ugukoresha amakuru n'ibisobanuro bitomoye muri vyose:


### Gusubira guhamagara


**Callback** ni igikorwa gusa duha uwundi murimo kugira ngo ushobore **guhamagarwa mu nyuma**.


Reka turabe akarorero nyakuri dukoresheje imibare. Ibaze ko dufise urutonde rw'imibare, maze tukaba dushaka gukubita kabiri kimwe cose muri vyo, hanyuma tugakoresha igikorwa (callback) ku vyo bivamwo "gukubita kabiri", ariko tukaba dushaka kubikora inyuma y'ugucerezwa gatoyi, nk'aho twoba turindiriye ikintu gigenda buhoro (nk'ugushira amakuru kuri internet).


Aha niho hari umurongo ukora ivyo ukoresheje **guhamagara**:


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


Reka tugerageze gukoresha iyi nzira:


```javascript
const input = [1, 2, 3]

doubleNumbers(input, function(result) {
console.log("Here is the doubled array:", result)
})
```


Inyuma y'isegonda 1, ibi bicapura:


```
Here is the doubled array: [ 2, 4, 6 ]
```


**Ni igiki kiriko kiraba hano?**


1. Duca `input` nk'urutonde rw'imibare dushaka gukubita kabiri.

2. Turaca kandi **callback function** ibwira porogarama ico ikora *inyuma* yo gutera kabiri.

3. Imbere muri `Imibare ibiri`, twigana ugucererwa dukoresheje `setTimeout`, hanyuma tugakora ugucerezwa kabiri.

4. Ivyo bimaze gushika, duhamagara callback ku nzira "doubled" array.


Ubu buhinga burakora, ariko wiyumvire ko ushaka gukora **intambwe nyinshi** inyuma y’ivyo, nk’ugucungera imibare mitoyi hanyuma ukayishiramwo. Ubwirizwa **gutera** ibindi bimenyetso nk’ibi:


```javascript
doubleNumbers(input, function(doubled) {
filterBigNumbers(doubled, function(filtered) {
sumNumbers(filtered, function(total) {
console.log("Final result:", total)
})
})
})
```


Iyi ni Hard yo gusoma no gutera umuvurungano. Uwo muco witwa **callback hell**, kandi ni co nyene `Isezerano` ryaremewe gukosora.


## Guhuza n'Imihango

<chapterId>30fddaca-729f-5c8d-bf86-8dfc7b3c9800</chapterId>


`Isezerano` ni ikintu cubatswe muri JavaScript kigereranya agaciro **kazoba gateguwe muri kazoza**.


Turashobora kurema Isezerano nk’iri:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve("It worked!") // This means everything went OK
})
```


Igice ca `Isezerano rishasha()` kirema isezerano.


Imbere muri yo, turayiha igikorwa gifise ibipimo bibiri:



- `gutorera umuti`, ni igikorwa twita iyo vyose bigenda neza
- `kwanka`, ni igikorwa twita iyo hari ikintu kigenda nabi


Mu karorero kari hejuru, turabitorera umuti ubwo nyene n'ubutumwa `"Vyarakoze!"`.


### `.hanyuma()`


Kugira ngo ukore ikintu **inyuma** y'aho umuhango ushikiriye, dukoresha `.then()`:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve(100) // This means everything went OK
})

promise.then(result => {
console.log("The result is:", result)
})
```


Ibi bicapura:


```
The result is: 100
```


Agaciro twashize kuri `resolve()` karungikwa ku gikorwa kiri imbere `.then()` nk'`igisubizo`.


Reka twigane igikorwa gifata amasegonda 2 dukoresheje `setTimeout`:


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


Ibi bizorindira amasegonda 2 hanyuma bicape:


```
Done waiting!
```


### `kwanka()`


Reka dushireho umuhango **uzonanirwa**:


```javascript
const failingPromise = new Promise((resolve, reject) => {
reject("Something went wrong")
})
```


None nitwakoresha `.then()` kuri ivyo, ntaco bizoba, kuko `.then()` ifata gusa ukuroranirwa.


Kugira ngo dukoreshe amakosa, dukoresha `.catch()`:


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


Ibi bicapura gusa


```
Caught an error: Something went wrong
```


Agaciro kashizwe kuri `kwanka()` koherezwa ku `.catch()` igikorwa.


Reka twubake Isezerano **rimwe na rimwe rikora rimwe na rimwe rinanirwa**, rishingiye ku bintu bimwe bimwe.


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


Ubu rero turashobora guhamagara ibi maze tugakora ivyo bibazo vyose bibiri:


```javascript
checkNumber(5)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Ibi bicapura:


```
Success: Positive number
```


Kandi nitwagerageza n’umubare utandukanye:


```javascript
checkNumber(-1)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Icapura:


```
Failure: Not a positive number
```


### Gufatanya ibikorwa hakoreshejwe `Isezerano`s



Turashobora gusubira kwandika akarorero kacu ka kera dukoresheje `Isezerano`, kandi kazosa n'akasukuye cane.


Reka dutangure kwandika verisiyo nshasha y’igikorwa cacu co gusubiramwo kabiri, ariko ubu, kigarura **umuhango**:


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


Ubu dushobora gukoresha `.then()` kubwira JavaScript ico yokora ku gisubizo:


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


Ibi bicapura:


```
Doubled numbers: [ 2, 4, 6 ]
```


Kugeza ubu, ivyo bikora nk’uko nyene bikora muri verisiyo y’uguhamagara, ariko ubu iyo kode iraryoshe kwagura no gusoma.


Reka tuvuge ko dushaka kwongerako izindi ntambwe:


1. Ubwa mbere, ushire kabiri imibare yose

2. Hanyuma, ukureho imibare iri munsi ya 4 .

3. Ubwa nyuma, vyose ubishire hamwe .


Turashobora kwandika igikorwa kimwe ku ntambwe yose, vyose dukoresheje amasezerano:


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


None rero turashobora **kubifatanya** gutya:


```javascript
const input = [1, 2, 3]

doubleNumbers(input)
.then(filterBigNumbers)
.then(sumNumbers)
.then(
result => console.log("Final result after all steps:", result)
)
```


Ibi bicapura:


```
Final result after all steps: 10
```


Reka tugendere mu vyo ivyo bikora:


1. `Imibare ibiri` igwiza kabiri urutonde: `[2, 4, 6]`

2. `akayunguruzoImibareMinini` ikuraho ikintu cose ≤ 3: `[4, 6]`

3. `Imibare` yongerako imibare isigaye: `4 + 6 = 10`

4. Ubwa nyuma, turacapura igisubizo.


Buri `.then()` irindiriye intambwe imbere y'uko irangira. Turashobora rero kwubaka **uruhererekane rw’ibikorwa** ataco dutera. Ivyo bituma kode ishobora gusomwa neza kandi igakosorwa neza.


## Guhuza n'`async`/`kurindira`

<chapterId>6e93d29f-c8bf-5fd1-a9c9-4e794ee6cbd0</chapterId>


Twarabonye ingene iminyororo ya `Promise` idufasha kwirinda umuriro w’iteka, ariko irashobora kuronka Hard ntoyi yo gusoma iyo hari intambwe nyinshi zirimwo.


Aho niho `async` na `await` bishika, bituma twandika kode idahuye **isa n’iyihuye**, ivyo bikaba bituma vyoroha gutahura.


### `Async` ni iki?


Iyo wanditse ijambo ry’ingenzi `async` imbere y’igikorwa, JavaScript ihita izingira agaciro k’igikorwa mu Isezerano.


Reka turabe akarorero k’ishimikiro:


```javascript
async function greet() {
return "hello"
}
```


Niwahamagara iyi nzira:


```javascript
const result = greet()
console.log(result)
```


Uzobona ibi:


```
Promise { 'hello' }
```


Naho woba waragaruye urudodo gusa, JavaScript iraguhindura Isezerano. Ushobora kuronka agaciro nyako ukoresheje `.then()` nk'ibi:


```javascript
greet().then( result => console.log(result) ) // prints "hello"
```


Canke ushobora gukoresha `kurindira`...


### `Kurindira` ni iki?


Ijambo ry’ingenzi `rindira` ribwira JavaScript riti: “rindira gushika iri Sezerano rirangiye, hanyuma umpe igisubizo.”


Ariko ushobora gukoresha gusa `await` **imbere mu gikorwa async**.


Reka dusubire kwandika akarorero dukoresheje `rindiriye`:


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


Ubu rero turashobora gukoresha igisubizo nk’aho coba ari agaciro gasanzwe.


Reka dukore ikintu c’ingirakamaro gatoyi ubu.


### Kwigana ugucerezwa na `kurindira`


Tuzokora igikorwa coroshe co kurindira gifata umubare w’amamilisegonda nk’imvo maze kigatorera umuti inyuma y’ayo mamilisegonda menshi, ata kindi dukora:


```javascript
function wait(ms) {
return new Promise(resolve => {
setTimeout(resolve, ms)
})
}
```


Reka tugerageze kuyikoresha:


```javascript
async function test() {
console.log("waiting 2 seconds...")
await wait(2000)
console.log("done waiting")
}

test()
```


Ibi bicapura:


```
waiting 2 seconds...
done waiting
```


Ushobora kwiyumvira ko `kurindira` ari “uguhagarika hano gushika umuhango urangiye, hanyuma ubandanye.”


Ivyo bigufasha kwandika kode mu buryo **kuva hejuru gushika hasi** bwigenza mu buryo butajanye n'igihe, ata gufatanya `.then()` amahamagara.


### Twarindiriye amakuru


Reka dusubire gukoresha akarorero kacu ka kera, aho dutera kabiri imibare, hanyuma tugacungera, hanyuma tugateranya. Ariko ubu, tuzokoresha `async`/`kurindira`.


Tuzokora ibikorwa 3 vyigana kurindira, maze tugarure amasezerano:


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


None rero reka twandike igikorwa ca `async` kugira ngo tubihuze:


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


Ibi bicapura:


```
Final result: 10
```


Ivyo biroroshe cane gusoma kurusha gufatanya `.then()` canke guhamagara.


Bisa n’iporogarama isanzwe y’intambwe ku yindi, ariko iracariko yigenza mu buryo butajanye n’igihe.


## Ibisubiramwo bitagikora

<chapterId>438b037d-9931-56d7-9052-7b4470f3c75b</chapterId>


Waramaze kwiga ivyerekeye **iterators** n'ingene dushobora gukoresha `for...of` kugira ngo dukoreshe amabara n'ibindi bintu bishobora gusubirwamwo.


Ariko none iyo amakuru dushaka gusubiramwo afata umwanya kugira ngo ashike?


Rimwe na rimwe dushaka guca ku bintu bishika **asynchronously**, nk'ubutumwa buva mu kiganiro, imirongo iva muri dosiye, canke imibare iva ku nzira y'ubute.


Kugira ngo ivyo ubikore, JavaScript iraduha **ibisubiramwo bitagira aho bigarukira**.


### Imikorere y'umuyagankuba


Uburyo bworoshe bwo gukora iterator async ni ugukoresha **igikorwa c'umugenzuzi async**.


Turavyandika gutya:


```javascript
async function* generateNumbers() {
yield 1
yield 2
yield 3
}
```


Ivyo bisa n'umuyagankuba usanzwe, ariko ufise `async` imbere yawo.


Ubu dushobora gukoresha `kurindira...kwa` kugira ngo dukoreshe agaciro:


```javascript
async function run() {
for await (const n of generateNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


Ibi bizocapura:


```
Got number: 1
Got number: 2
Got number: 3
Done!
```


None ni irihe tandukaniro riri hagati y’umuyagankuba usanzwe?


Itandukaniro ni: ubu dushobora gukoresha `await` imbere muri generateur.


Reka dusubire gukora umufasha wo gutevya:


```javascript
function wait(ms) {
return new Promise(resolve => setTimeout(resolve, ms))
}
```


None rero reka dushiremwo imibare **buhoro buhoro**:


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


Gerageza kuyikoresha:


```javascript
async function run() {
for await (const n of generateSlowNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


### Ni kuki ukoresha ibisubiramwo async?


Ivyiyumviro bitari vyo ni ngirakamaro iyo:



- Ivyiza vyose ntibishika rimwe.
- Ushaka kubifata kimwe kimwe, **uko biza**.
- Ukorana n’Imihango, kandi ushaka gukora mu buryo busukuye.


Nk'akarorero, niwaba ushaka gushiramwo ubutumwa buva kuri server y'ubutumwa bumwe bumwe, canke gukuraho dosiye nini mu bice, async iterators ziguha uburyo bwo kwandika `for` loop ikorana n'amakuru atevye.


### `Ikimenyetso.Iterateri`


Turashobora kandi gukoresha async iterations mu mashure y'abantu.


Aha ni akarorero gatanga imibare itevye:


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


Ubu dushobora gukoresha `ku kurindira...kwa` nk'uko vyari kera:


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


Ibi bigufasha kurema ibintu bishobora gusubirwamwo mu buryo butajanye n'igihe


## Assignment isukari y'inyuguti

<chapterId>8b1ba7d8-ecfd-5470-b86e-73cb84ccc8b7</chapterId>


"Syntax sugar" bisigura kwandika ikintu mu buryo bugufi canke bworoshe, utahinduye ico gikora. Ni uburyo bwiza gusa bwo kuvuga ivyo nyene.


JavaScript ifise isukari y’inyuguti yubatswemwo ituma twandika amatangazo asukuye kandi magufi. Muri iki gice, turaza kuraba ingene twotanga agaciro bishingiye ku bintu, guhindura ibihinduka n’imibare, gukura agaciro mu mirongo canke ibintu, no kubikopa canke kubifatanya n’insiguro yoroshe.


### Umukoresha wa gatatu


Muri JavaScript, ushobora gutanga agaciro gashingiye ku vyo usaba ukoresheje **umukoresha wa gatatu**, ari bwo buryo bugufi bwo kwandika `if...else`.


Aho gukora:


```javascript
let message

if (isMorning) {
message = "Good morning"
} else {
message = "Hello"
}
```


Ushobora kwandika:


```javascript
const message = isMorning ? "Good morning" : "Hello"
```


Ibi bisigura:



- Niba `isMorning` ari ukuri, koresha `"Igitondo ciza"`
- Ahandiho, koresha `"Ndabaramukije"`


Uburyo rusangi ni:


```javascript
condition ? valueIfTrue : valueIfFalse
```


Ushobora kuyikoresha no mu zindi mvugo:


```javascript
console.log(isSunny ? "Go outside" : "Stay in")
```


Urabe gusa ko uyikoresha ku ngingo **zoroshe**. Niba ivyiyumviro bikomeye, ushireko `if...else`.


### Ubundi buryo bwo gukoresha Assignment


JavaScript ifise **ibikoresho vy'inzira ngufi** vyo gukora ibikorwa bifatanijwe n'ibikorwa.


Reka turabe uburyo busanzwe:


```javascript
let counter = 1
counter = counter + 1
```


Ivyo bishobora kugabanywa ngo:


```javascript
let counter = 1
counter += 1 // same as counter = counter + 1
```


Akira ivyo bikunze gukoreshwa cane:


| Operator | Meaning             |
| -------- | ------------------- |
| `+=`     | add and assign      |
| `-=`     | subtract and assign |
| `*=`     | multiply and assign |
| `/=`     | divide and assign   |

Ingero:


```javascript
let score = 10
score += 5  // now score is 15
score *= 2  // now score is 30
score -= 10 // now score is 20
```


Ivyo ni ngirakamaro iyo ushaka guhindura umuhinduzi ukoresheje agaciro kayo bwite.


### Gusambura


**Destructuring** bigufasha gukura agaciro mu ma arrays canke mu bintu ukabika mu bihinduka bitagoranye.


#### Imirongo


Twibaze ko ufise:


```javascript
const colors = ["red", "green", "blue"]
```


Aho gukora:


```javascript
const first = colors[0]
const second = colors[1]
```


Ushobora gukora:


```javascript
const [first, second] = colors
```


Ibi bitanga:



- `mbere` ku `"umutuku"`
- ubwa kabiri kuri Green


Ushobora gusimbuka agaciro kandi:


```javascript
const [,, third] = colors
console.log(third) // blue
```


#### Ibintu


Ushobora gukura agaciro mu bintu navyo:


```javascript
const user = { name: "Alice", age: 30 }

const { name, age } = user
console.log(name) // Alice
console.log(age)  // 30
```


Niba umutungo ufise izina ritandukanye n'umuhinduzi ushaka, ushobora guhindura izina:


```javascript
const { name: username } = user
console.log(username) // Alice
```


Gusenyura bituma kode yawe isukuye iyo ukorana n'ibintu n'imirongo.


### Gukwiragiza inyuguti


**Inyigisho yo gukwiragiza** ikoresha `...` gufungura canke gukopa agaciro.


#### Imirongo


Ushobora gukopa canke gufatanya amabara:


```javascript
const a = [1, 2]
const b = [3, 4]

const both = [...a, ...b]
console.log(both) // [1, 2, 3, 4]
```


Ushobora kandi gukora clone y'urutonde:


```javascript
const original = [10, 20, 30]
const clone = [...original]
```


#### Ibintu


Ushobora gukora nk'ukwo nyene ku bintu:


```javascript
const a = { x: 1 }
const b = { y: 2 }

const merged = { ...a, ...b }
console.log(merged) // { x: 1, y: 2 }
```


Ushobora kandi guhindura agaciro:


```javascript
const user = { name: "Alice", age: 30 }
const updated = { ...user, age: 31 }

console.log(updated) // { name: "Alice", age: 31 }
```


Ivyo birafasha cane iyo uriko urahindura ibintu utahinduye ivy’umwimerere.


# UrudodoJS

<partId>42fe4d49-dace-5135-bb9e-b9d75034fb2a</partId>


## Twashitse gute kuri Node .

<chapterId>0da1d60c-06c9-54e6-a181-ae7dabf6e3b8</chapterId>


Muri iki gice tuzokwiga gatoyi ku bijanye n’amateka yerekeye JavaScript na NodeJS.


Ivyerekeye amateka birahambaye cane muri porogarama, kuko akenshi dukoresha ibikoresho vyubatswe n’abandi bantu, kandi rero dukora ku ngingo zafashwe kera na bo.


Gutahura imvo y’izo ngingo, n’ingene ibikoresho dukoresha vyaje kuba uko biri, bizodufasha kwumva tudatera ubwoba gatoyi ku bijanye n’ivyo turiko turakora.


### Inkomoko ya JavaScript


JavaScript yatanguye nk’ururimi rworoshe rwagenewe gutuma amapaji y’urubuga akorana n’abandi.


Mu myaka ya 1990, amaporogarama y’urubuga nka Netscape Navigator yongeyeko JavaScript kugira ngo abahinguzi bashobore kwandika kode ikora ataco ihinduye muri iyo porogaramu.


Iciyumviro c'intango cari co kugira Java nk'ururimi nyamukuru rwo gukora imbuga (n'ivyo bita "Java applets"), na JavaScript ku bintu bitobito gusa.


Ico gishushanyo nyamukuru cakozwe na Brendan Eich, ico gihe yari umukozi wa Netscape, mu kiringo kitarenga indwi 2.


Ariko abantu benshi bakunda gukoresha JavaScript kuruta Java, kandi na Java applets zari zifise ibibazo vy’umutekano ico gihe, rero amaherezo Java yarakuweho nk’uburyo bwo guhitamwo maze JavaScript iba de facto standard mu gutegura urubuga.


### Moteri ya V8


JavaScript ni ururimi rusobanuwe, bitandukanye n'indimi zikoranijwe nka C.


Kode yanditswe mu rurimi rwakoranijwe irahinduka binaire, maze binaire igaca igaburirwa ataco ihinduye kuri CPU ya mudasobwa.


![](assets/en/6.webp)


Ku rundi ruhande, indimi zisobanurwa zikunda gukoreshwa neza, kandi zikaba ziri hafi y'ingene abantu biyumvira ("urugero rwo hejuru") aho kwegera ingene imashini zikora ("urugero ruto"); rero akenshi bafise imashini y’ivy’impwemu yubatswe kugira ngo ikoreshe kode yabo.


Imashini y’ukuri ni porogarama idasanzwe yicara hagati ya kode wanditse na CPU, igakora kode yawe (kuko CPU idashobora kuyitahura).


Ivyo bituma ushobora gukora porogarama utazi vyinshi ku mashini iri munsi yayo, ariko kandi birafise igiciro mu bijanye n’ingene ikora, kuko mudasobwa ntiriko irakoresha porogarama yawe gusa; ni ugukoresha porogarama (imashini y'ivy'impwemu) ikoresha porogarama yawe.


Uko porogarama zo ku rubuga zagenda zirushiriza kuba nyinshi, ni ko hariho ugusaba ko JavaScript ikora neza kuruta. Moteri ya V8 ni umusiguzi atanga ubushobozi bwa JavaScript muri Google Chrome. Yateguwe kuri Google isohoka muri 2008.


Naho moteri za kera za JavaScript zari ahanini imashini za kera, moteri ya V8 ni umukozi wa JIT (just-in-time).


Iryo tegeko rya JavaScript rigaburirwa moteri ya V8, maze moteri igerageza gukoranya ibice vyayo nk’ibice bibiri vy’imvukira ku nzira. Ivyo bituma ugira ubumenyi bw'ururimi rwo ku rwego rwo hejuru, n'ubushobozi bwo kuba hafi gato y'indimi zo ku rwego rwo hasi. Ivyo vyatumye JavaScript iba ururimi rwihuta kuruta izindi zose kw'isi, ikintu "ciza kuruta ibindi vyose".


### Igihe co gukora NodeJS


Naho yoroshe gukoresha kandi yihuta cane gukora, inyuma y’aho V8 JavaScript isohokeye yagumye ifise aho igarukira cane: yashobora gukoreshwa gusa imbere mu mucukumbuzi.


Ni kubera iki ivyo ari ingorane?


Erega, kubera ko ama browser akora code yavanywe mu ma miliyoni y'ibibanza bitandukanye kuri internet, arashobora gutera mu buryo bworoshe porogarama mbi, bigatuma "ashirwa mu gasandugu k'umunyota" avuye mu bindi bikoresho vyose.


![](assets/en/7.webp)


JavaScript ntiyashobora gushika ku nzira y’amadosiye n’ibindi bikoresho vyo mu karere kuri mudasobwa yawe (n’imiburiburi ntivyari vyoroshe nk’uko izindi ndimi zashobora), rero ivyo vyari bifise uburenganzira bukomeye ku bwoko bw’ibikorwa woshobora kwubaka na yo.


Mu mwaka w’2009, Ryan Dahl yarasohoye NodeJS, ariyo runtime ishobora kugufasha gukoresha moteri ya V8 hanze y’umucukumbuzi, ataco uhinduye kuri system operating kavukire ya mudasobwa yawe. Yongerako kandi ibintu vyinshi bifasha mu kwandika porogarama ziri ku ruhande rwa server n’iziri ku murongo w’amabwirizwa. Nk’akarorero, urashobora gukoresha NodeJS kugira ngo ureme urubuga, usome kandi wandike amadosiye, canke wubake ibikoresho bikora ibikorwa vy’ubuhinga.


![](assets/en/8.webp)


Muri iki cigwa gushika ubu, twasuzumye ibiranga JavaScript biri muri browser no muri NodeJS. Ivyo bintu vyatuma dushobora gusobanura amakuru no kuyakoresha mu buryo butaboneka. Mu vyigwa bikurikira, tuzoca irya n’ino ibintu vyihariye kuri NodeJS kandi bikaduha uburenganzira bwo gukorana na sisitemu ikoresha.


## Impamvu z'umurongo w'itegeko

<chapterId>960d20f3-c424-5d51-a041-ef17d2e94b6d</chapterId>


NodeJS iratwemerera, mu bindi, kwubaka CLIs (Imirongo y’Itegeko).


Ku bw'ivyo dukeneye uburyo bwo kwakira umurongo w'amabwirizwa, ivyo muri Node bikorwa hakoreshejwe ikintu `process` cubatswemwo.


### `uburyo`


NodeJS itanga ikintu kidasanzwe citwa `process` giserukira porogarama iriko irakora.


Ushobora kuyikoresha kugira ngo usuzume ibidukikije, ububiko bukora ubu, mbere no gusohoka muri porogarama iyo bikenewe.


Nk'akarorero:


```javascript
console.log(process.platform)
```


Ibi bicapura urubuga rwo gukoresha, nka `win32`, `linux`, canke `darwin` (Mac).


### `uburyo.argv`


Iyo ukoresheje porogarama ya NodeJS uhereye ku nzira, ushobora gutanga amajambo y’inyongera (imvo) inyuma y’izina ry’inyandiko. Ivyo bibikwa muri `igikorwa.argv`.


Nk'akarorero, niwakoresha iri tegeko:


```
node my_script.js alpha beta
```


Ushobora gucapura imvo nk'izi:


```javascript
console.log(process.argv)
```


Igisohoka gishobora gusa n'iki:


```
[ '/path/to/node', '/path/to/my_script.js', 'alpha', 'beta' ]
```


Ibintu bibiri vya mbere vyama ari inzira ya Node n'inzira y'inyandiko yawe. Amajambo yose y’inyongera mwashize mu nyandiko aza inyuma y’ivyo.


`Process.argv` ishobora gutemwa nk'iyindi mirongo yose ikoresheje uburyo bwa `.slice()`, kugira ngo ubone gusa imvo zashikirijwe ushobora gukora


```javascript
const args = process.argv.slice(2)

console.log(args)
```


Kugira uburenganzira bwo gushika ku mpamvu umukoresha ariko ararenga ni ngirakamaro mu gutegura ibikorwa vy'umurongo w'amabwirizwa.


## Ivyigwa

<chapterId>4e1651a5-65fd-50bc-b22a-40313d5659ca</chapterId>


Igihe co gukoresha JavaScript nka NodeJS akenshi gifata dosiye yose ya JavaScript nk'igice gitandukanye.


Iyumvire ko module ari nk’agasanduku. Ico kibanza gifise umwanya waco bwite, rero ibihinduka n’ibikorwa wamenyesheje muri co ntibibangamira kode iri mu zindi nkoko. Mu bisanzwe, igice cose gifise urugero rwaco.


Module ishobora kwohereza hanze bimwe mu birimwo, bikaboneka ku bindi bice, kandi ishobora kwinjiza ibirimwo ibindi bice vyarungitse hanze. JavaScript iragufasha kwohereza hanze no kwinjiza ibirimwo hagati y'ibice, kugira ngo uhuze amadosiye atandukanye.


Porogarama ya JavaScript akenshi igizwe n’ibice vyinshi, bihuye.


Ni kuki dukoresha amamodule? Mu gucapura kode yawe mu bice, urashobora gutunganya porogarama yawe mu bice bitobito, bitomoye kandi bishobora gusubira gukoreshwa. Igitabu cose gishobora kwibanda ku bwoko bumwe gusa bw’igikorwa, nk’ugukora imibare, gukorana n’amadosiye canke guhindura umwandiko.


### Ivyigwa vya CommonJS


Muri NodeJS, uburyo busanzwe bwo gucunga ibice bwitwa **CommonJS**.


Muri iyi sisitemu, ushobora gusangira (gusohora) kode ivuye mu gice ukoresheje `module.exports` hanyuma ukayishira mu yindi dosiye ukoresheje `require()`.


Kugira ngo ikintu kiboneke hanze y'igice, ugishire kuri `igice.exports`:


```javascript
const greeting = "Hello!"

module.exports = greeting
```


Aha, urudodo `"Muraho!"` ni co iki kiganiro cohereza hanze.


Kugira ngo ukoreshe kode yoherejwe hanze ivuye mu yindi dosiye, ukoresha `require()` igikorwa n'inzira ija kuri iyo dosiye:


```javascript
const greeting = require("./greeting.js")

console.log(greeting)
```


Ibi bicapura:


```
Hello!
```


Ushobora kwohereza ibintu vyinshi hanze mu kubifatanya mu kintu kitazwi, nka


```javascript
const greeting1 = "hello"

const greeting2 = "hi"

module.exports = {
greeting1, greeting2
}
```


CommonJS yari uburyo bw’ibice bwa mbere bwakoreshejwe na NodeJS. Mu nyuma na ho nyene hariho amamodule ya ES.


### ES ibice


NodeJS kandi ishigikira ubundi bwoko bw’ibice vyitwa **ES Modules**, bikundwa cane mu gutegura urubuga. Bakoresha amajambo y'ingenzi `gusohora` na `kwinjiza`.


ES modules zateguwe ku mucukumbuzi hanyuma gusa zongerwa kuri Node. Niba ushaka kubikoresha, ushobora gukoresha `.mjs` nk'ukwaguka kwa dosiye aho gukoresha `.js`, bivanye n'uko ukoresha verisiyo ya Node.


Mu dosiye imwe yitwa `greeting.mjs` twandika


```javascript
export const greeting = "Hello!"
```

Nk'uko ushobora kubibona, turiko turarungika hanze ikintu kidahinduka aho gisobanurwa


Muyindi dosiye yitwa `index.mjs`, turayizana:


```javascript
import { greeting } from "./greeting.mjs"

console.log(greeting)
```


Ushobora kwohereza hanze amatangazo atandukanye mu bice bitandukanye vya dosiye, nka


```javascript
export const num = 10

export function double (x) {
return x*2
}
```


### Ububiko bw'ibitabu busanzwe bwa NodeJS


NodeJS kandi irimwo ibice vyinshi vyubatswemwo. Ivyo ni ibice vyiteguwe bitangwa na NodeJS bifasha mu bikorwa rusangi nk’ugusoma amadosiye, gukorana na sisitemu ikoresha, canke kwifatanya n’urubuga.


Nk'akarorero, `os` module iguha amakuru yerekeye sisitemu yawe:


```javascript
const os = require("os")

console.log(os.platform())
```


Ntubwirizwa gushiramwo izo modules zishizwemwo, ziza na NodeJS. Bikora "ububiko busanzwe" bw'igihe co gukora, kandi bikoreshwa n'ibikoresho vyinshi vya Node kugira ngo bikore ibintu nk'ugusoma amadosiye canke guhanahana amakuru biciye kuri internet.


Ibigabane bikurikira bizokwereka ingero ngirakamaro z’ingene zikoreshwa.


## Igikoresho ca `fs`

<chapterId>911e953a-35ae-5ee7-bd74-372501c32e81</chapterId>


Igikoresho ca `fs` (mu ncamake **uburyo bwa dosiye**) ni igice c'ububiko bw'ibitabo bwa NodeJS. Iragufasha gukorana n’amadosiye n’ububiko kuri mudasobwa yawe: ushobora gusoma amadosiye, kwandika amadosiye, kuyafuta, kuyahindura izina, n’ibindi.


Kugira ngo uyikoreshe, ubanza kuyizana hejuru ya dosiye yawe:


```javascript
const fs = require("fs")
```


### Guhuza API


Uburyo bworoshe bwo gukoresha `fs` ni uburyo bwayo **sync**.


Ubwo buryo burazibira porogarama gushika irangije (rero umurongo ukurikira wa kode ntukora gushika igikorwa kirangiye).


Aha ni akarorero ko gusoma dosiye mu buryo bumwe:


```javascript
const fs = require("fs")

const data = fs.readFileSync("example.txt", "utf8")

console.log(data)
```


Niba hariho dosiye yitwa `example.txt` mu bubiko bumwe n’inyandiko yawe, ivyo bizocapura ibirimwo.


Ushobora kandi kwandika muri dosiye mu buryo buhuye:


```javascript
const fs = require("fs")

fs.writeFileSync("output.txt", "Hello from Node!")

console.log("File written!")
```


Ivyo bikora (canke bikandika) dosiye yitwa `output.txt` n'umwandiko.


Aha niho hari ibikorwa rusangi ushobora gukora n'iyi API:


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


Sync API yoroshe kandi ni nziza ku nyandiko ntoya, ariko kubera ko ibuza porogarama gushika irangiye, irashobora gutuma ibintu bigenda buhoro iyo uriko urakorana n’amadosiye manini canke server.


### Guhamagara async API


**Callback API** ntabwo ibuza: ireka NodeJS iguma ikora ibindi bintu mu gihe igikorwa ca dosiye kiriko kiraba.


Aho kugarura igisubizo, bifata igikorwa (a **callback**) gihamagarwa iyo igikorwa gikozwe.


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


Ehe ivyo bishika:



- `fs.somaDosiye` itangura gusoma `akarorero.txt`.
- NodeJS ntiririndira, ija ku gushitsa iyindi kode woba wanditse.
- Iyo dosiye ihejeje gusomwa, uguhamagara kuragenda:



  - Niba hariho ikosa, `err` irimwo ikosa.
  - Ahandi ho, `amakuru` arimwo ibirimwo.


Ehe uko wandika muri dosiye:


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


Iciyumviro kimwe: porogarama ntihagarara iyo uriko urandika dosiye.


Ingero zimwe zimwe z'ibintu ushobora gukora n'iyi API:


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


API yo guhamagara ni nziza ku ba serveri n’ibikorwa binini kuko ntibuza porogarama, ariko guhamagara bishobora gutera umuvurungano iyo ukoresheje ibikorwa vyinshi. Ni co gituma API ya async ishingiye ku masezerano yongeweko.


### Isezerano async API


API ishingiye ku masezerano ni iya none kandi ikora neza cane na `.then()` na `async/await`. Iraboneka nka `fs.amasezerano`.


Ukeneye kwinjiza `amasezerano` umutungo:


```javascript
const fs = require("fs").promises
```


Gukoresha `.hanyuma()`:


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


Canke mbere vyiza, ukoresheje `async/kurindira`:


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


Kwandika muri dosiye:


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


Urutonde rusanzwe rw'ingero za API:


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


Iyo wanditse kode , uzokenera kenshi gukoresha kode yanditswe n’abandi bantu; nk’akarorero, amasomero kugira ngo agufashe gukorana n’amatariki, amabara, amaserveri canke hafi ikindi kintu cose.


Aho gukura no gukopa amadosiye n'amaboko, ushobora gukoresha **umucungerezi w'amapaki**.


Umucungerezi w'amapaki ni igikoresho:



- Gukuraho amapaki
- ikurikirana amapaki umugambi wawe ukeneye
- urabe neza ko umuntu wese wo mu mugwi wawe afise verisiyo imwe y'amapaki


### NPM ni iki


Mu isi ya NodeJS, umuyobozi w'amapaki azwi cane ni **NPM**, bisobanura *Umucungerezi w'amapaki ya Node*.


Uronka NPM ubwo nyene iyo ushizeho NodeJS.


Ushobora kumenya nimba ufise NPM ukoresheje ibi muri terminal yawe:


```
npm -v
```


Ibi bicapura verisiyo ya NPM ufise, nka:


```
10.2.1
```


### Gukora ububiko


Muri NodeJS, **ipaki** ni ububiko gusa bufise dosiye `ipaki.json` muri bwo.


Reka tureme intambwe ku yindi.


1. Kora dosiye nshasha y'umugambi wawe:


```
mkdir my_project
cd my_project
```


2. Gukoresha iri tegeko:


```
npm init
```


Ibi bitangura gutegura, bikubaza ibibazo nk'izina ry'umugambi wawe, verisiyo, insobanuro, n'ibindi.


Niba udashaka kwishura vyose kandi ukemera gusa ivyashizweho, ushobora gukoresha:


```
npm init -y
```


Uhejeje kuyikoresha, uzobona dosiye nshasha muri dosiye yawe yitwa:


```
package.json
```


### `ububiko.json`


Dosiye `package.json` ni dosiye JSON ibika amakuru y'umugambi wawe.


Akira akarorero:


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


Ivyiyumviro bikeyi bihambaye:



- `izina`: izina ry'ibintu vyawe
- `verisiyo`: verisiyo iriho ubu
- `ikuru`: dosiye y'inzira y'injira (nk'index.js`)
- `inyandiko`: amabwirizwa ushobora gukoresha (nka `npm gutangura`)
- `ibivako`: urutonde rw'amapaki yose umugambi wawe uvako


### Gushiramwo umuzigo


Reka tuvuge ko ushaka gukoresha umugwi umwe witwa `picocolors` kugira ngo wongere amabara ku gisohoka ca terminal yawe.


Ushobora kuyishiramwo ukoresheje:


```
npm install picocolors
```


Ubu urashobora kuyikoresha mu mugambi wawe. Kora dosiye `index.js` n'


```javascript
const pico = require('picocolors')

console.log(
pico.green("This text is green!")
)
```


kandi ugerageze kuyikoresha. Ico gikoresho gikwiye gucapura ibara ry'ivyanditswe.


NPM yakoze iki ?



- Yakuyeho iyo mpapuro maze irayibika mu bubiko buto bwitwa `node_modules/`
- yongeyeko ivyinjijwe munsi y'ibishingiyeko` muri `package.json` yawe
- yahinduye dosiye ya `paki-lock.json`


`Ipaki-ugufunga.json` ni iki?


### `ububiko-bufunga.json`


Iyi dosiye ihita iremwa na NPM.


Ushobora kwibaza, nimba dusanzwe dufise `package.json`, kuki dukeneye iyindi dosiye?

Ehe imvo:



- `package.json` ivuga gusa verisiyo **urutonde** rw'impapuro umugambi wawe ukeneye.

Akarorero:


```json
"dependencies": {
"picocolors": "^1.1.0"
}
```


`^1.1.0` bisigura “verisiyo iyo ari yo yose ihuye na 1.1.x”, rero irahinduka.



- `package-lock.json` **ifunga** verisiyo nyazo za buri package n'ibiyifatanije, kugira ngo umuntu wese ashiraho umugambi wawe aronke uburyo nyabwo bwo gukora.


Ni kubera iki ivyo bihambaye?


Iyo ukora mu mugwi, canke ushize umugambi wawe kuri server, canke ukagaruka kuri wo muri kazoza, ushaka kumenya neza ko uguma ukora gutyo nyene.

Niba amapaki yahinduwe maze ugasubira gushiramwo ata dosiye y’ugufunga, ushobora kuronka verisiyo itandukanye gatoyi yigenza mu buryo butandukanye.


Mu kugumiza `package-lock.json` mu mugambi wawe, NPM izokwama ishiramwo verisiyo nyazo ziri ku rutonde ng'aho, kugira ngo umuntu wese afise ibidukikije bimwe.


`package-lock.json` ifunga vyose kuri verisiyo yihariye cane, kugira ngo umugambi ushobore gusubirwamwo ku zindi mashini.


Ariko nimba porogaramu yawe ikeneye gukoreshwa n'abantu benshi, woshobora guhitamwo kutayikora, kugira ngo NPM ironke dosiye `package.json` gusa kandi yemererwe gushiramwo ubwo nyene verisiyo za nyuma zemerewe muri iyo dosiye.


Ariko ivyo nivyo ukwiye kwitwararika mu nyuma, umaze gutangura gusohora kode yawe bwite. Ubu, twashizeho ivy’ishimikiro vya NPM kugira gusa mushobore kuronka no gukoresha amasomero yasohowe n’abandi bategura mu migambi yanyu.



## Gukorana n'abandi muri NodeJS

<chapterId>f2cabd8b-754b-5c97-8d6a-8412a9a184c7</chapterId>


NodeJS ikoreshwa kenshi nk'ururimi rw'inyuma: ushobora guhindura inyandiko yawe ngo ibe server, kandi ukayikoresha mu gusaba izindi server.


Mu gice ca thi turaza kubabwira ibintu bimwe bimwe vy’ishimikiro vyo gukorana n’abandi bizokuronsa uburenganzira bwo kubikora.


### `kuzana()`


Niba ushaka ko porogarama yawe ikura amakuru ku rubuga canke kuri API, ukeneye gukora **HTTP request**.


Mu verisiyo za none za NodeJS, ushobora gukoresha igikorwa `fetch()`.


Aha ni akarorero ko gusaba GET kuri API:


```javascript
const response = await fetch("https://jsonplaceholder.typicode.com/posts/1")
const data = await response.text()

console.log(data)
```


Iyo ukoresheje ibi, uzobona ikintu nk’iki:


```
{
"userId": 1,
"id": 1,
"title": "...",
"body": "..."
}
```


Ehe ivyo bishika:


1. `fetch()` ifata URL igasaba.

2. Igarura **Isezerano** ritorera umuti ikintu `Inyishu`.

3. `inyishu.igisomwa()` isoma umubiri w'inyishu nk'urudodo.


Ariko urudodo ubona ni JSON. Ico ni iki?


### JSON


Iyo ukorana n'urubuga APIs, amakuru akenshi yoherezwa kandi akakirwa nk'**JSON**, ihagarariye JavaScript Ikintu Notation.


JSON ni uburyo bw'inyandiko gusa busa cane n'ibintu vya JavaScript. Nk'akarorero:


```json
{
"name": "Alice",
"age": 30,
"likes": ["apples", "bananas"]
}
```


Ikintu `JSON` ni igikoresho cubatswe muri JavaScript gishobora gukoreshwa mu gukorana n'iyi nzira y'amakuru.


Ushobora guhindura ikintu ca JavaScript mu rudodo rwa JSON ukoresheje `JSON.urudodo()`:


```javascript
const user = { name: "Alice", age: 30 }

const jsonString = JSON.stringify(user)

console.log(jsonString)
```


Ibi bicapura:


```
{"name":"Alice","age":30}
```


Ushobora kandi guhindura umwandiko wa JSON ugasubira mu kintu ca JavaScript ukoresheje `JSON.parse()`:


```javascript
const jsonText = '{"name":"Bob","age":25}'

const obj = JSON.parse(jsonText)

console.log(obj)
```


Ibi bicapura:


```
{ name: 'Bob', age: 25 }
```


Urabe maso: `JSON.parse()` izotera ikosa iyo urudodo rudakora JSON.


```javascript
JSON.parse("not json") // ❌ Error!
```


Rero urabe neza ko urudodo rwateguwe neza.


### `http` umukozi


NodeJS iragufasha gukora urubuga ata kindi ushizemwo.


Ushobora gukoresha `http` yubatswemwo kugira ngo ukoreshe ibisabwa n'abaguzi no kohereza inyishu.


Aha niho hari akarorero k’ishimikiro cane:


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


Iyo ukoresheje iyi nyandiko maze ugafungura `http://localhost:3000` mu mucukumbuzi wawe, uzobona:


```
Hello from NodeJS server!
```


Ibi nivyo biriko biraba muri kode:


1. Wazanye umukozi wa `http` mu bubiko bw'ibitabu bwa Node.

2. `http.remaServeri()` irema Serveri. Waciye kuri `http.remaServer()` gusubira guhamagara `(req, res) => {...}` kugira ngo ukore igihe cose umuntu ahuye.

3. Washizeho code ya status ya 200 (yerekana ko igikorwa cakozwe neza) ku nyishu. Ushobora gusoma ivyerekeye amakode y'imiterere ya http [hano](https://umuhinguzi.mozilla.org/ru-Amerika/inyandiko/Urubuga/HTTP/Ishingiro/Imimerere)

3. `res.end()` yohereza inyishu maze irangize ihuriro.

4. `umukozi.umviriza(3000)` atangura umukozi ku cambu 3000.


Ushobora kandi gusuzuma `req.url` na `req.method` mu gusaba gukora inzira zitandukanye canke ubwoko bw'ibisabwa.


Akarorero n'inzira:


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


Izo ni ingero z’ishimikiro cane. Kugira ngo wubake ama server ateye imbere, benshi mu ba devs boshobora gukuraho ububiko bw’ibitabu bwiteguye nk’ubw’inyuma nk’ubw’inyuma.


## Gutunganya amakuru: ububiko, ivyabaye, imigezi

<chapterId>8c9623f0-a604-51a4-8fe4-871c849d3e3b</chapterId>


Muri iki gice tuzozana ahanini imigwi itatu y'ibintu:



- `Buffer`, iserukira utugingo ngengabuzima dutoduto tw'amakuru abiri
- `EventEmitter`, ishobora gukoreshwa mu gukurikirana intambwe zimwe zimwe biciye mu nzira zitajanye n'igihe mu gutanga ibimenyetso vyitwa "ibintu".
- `Stream`, ituma dushobora gukora igice kinini c'amakuru `Buffer` imwe igihe, kandi ikurikirana inzira mu gutanga ibintu


Ivyo birasanzwe cane muri kode ya NodeJS y'umwuga, rero naho woba utabikoresha mu migambi yawe ya mbere, ni vyiza kuronka ugutahura kw'ishimikiro kw'igihe uzokenera gukorana navyo. muri bo


### Ububiko


Mu NodeJS, **buffer** ni ubwoko bw'ikintu gikoreshwa mu gukorana n'amakuru abiri.


Ushobora kwiyumvira ububiko nk'igikoresho c'ingero idahinduka c'ama bytes atagiramwo ibintu.


Ehe ingene wokora ububiko buva ku rudodo:


```javascript
const buf = Buffer.from("hello")
console.log(buf)
```


Ibi bicapura ikintu nk'iki:


```
<Buffer 68 65 6c 6c 6f>
```


Iyo mibare (`68`, `65`, `6c`, n'ibindi) ni ibimenyetso vy'inyuguti ziri muri `"hello"`.


Ushobora kuyihindura ikagaruka mu murongo nk'uyu:


```javascript
console.log(buf.toString())
```


Ibi bicapura:


```
hello
```


Ushobora kandi kurema ububiko bw'ubunini bumwe bwuzuye ubusa:


```javascript
const buf = Buffer.alloc(10)
console.log(buf)
```


Ibi bicapura ikintu nk'iki:


```
<Buffer 00 00 00 00 00 00 00 00 00 00>
```


Ushobora kwandika mu buffer:


```javascript
buf.write("abc")
console.log(buf)
```


Kandi ushobora gushika ku bytes z'umuntu ku giti ciwe:


```javascript
console.log(buf[0]) // prints the ASCII number for 'a', which is 97
```


Buffers ni ngirakamaro cane cane iyo ukeneye gukoresha amakuru ku rugero ruto cane.


### Ivyabaye


Mu rurimi rwa JavaScript, **ikintu** ni ikintu kiba muri porogarama yawe ushobora gufata ingingo.


Nk'akarorero:



- dosiye iraheza kwinjira
- igihe kirazima
- umukoresha akanda kuri buto
- Igisabwa c'urubuga kigarura amakuru


**Ivyabaye** ni ikimenyetso gusa c'uko hari ikintu cabaye, kandi ushobora kwandika code kugira ngo wumvirize ivyo bintu vyabaye kandi uvyifatemwo neza.


Muri NodeJS, ibintu vyinshi birashobora gutanga ibintu. Ivyo bintu vyitwa **Ivyabaye**.


Akira akarorero:


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


Ibi bicapura:


```
Hello! An event happened.
```


Ehe iki:


1. Turarema ikintu `Ivyabaye`.

2. Turayibwira ngo ikoreshe gusubira guhamagara igihe cose ikintu `"kuramutsa"` kibaye, dukoresheje `.on("kuramutsa")`.

3. Munyuma, duca dutera `"kuramutsa"` dukoresheje `.emit()`.

4. Uguhamagara kwacu kurashirwa mu ngiro


Ushobora gutanga amakuru hamwe n'ivyo vyabaye:


```javascript
emitter.on("greet",
(name) => console.log(`Hello, ${name}!`)
)

emitter.emit("greet", "Alice") // first argument is the type of event, second argument is the data we pass with this event
```


Ibi bicapura:


```
Hello, Alice!
```


Ushobora kwandika abakwumviriza ku bindi birori navyo:


```javascript
emitter.on("goodbye", () => {
console.log("Goodbye!")
})

emitter.emit("goodbye")
```


Ushobora gufatanya abakwumviriza benshi uko ushaka ku bwoko bw’ikintu, kandi ushobora gutera ubwoko bwinshi bw’ikintu butandukanye buva ku nkuru imwe.


Ibintu vyinshi muri NodeJS bitanga ibintu kugira ngo bibwire porogarama isigaye ko hari ikintu kiriko kiraba.



### Imigezi ni iki?


Imigezi ifatanya ububiko n’ibintu kugira ngo idufashe gukora amakuru.


Iyo dukorana n’amadosiye, amakuru ava ku rubuga, canke mbere n’ivyanditswe birebire, ntitwama dukeneye (canke dushaka) gushiramwo vyose mu bwenge rimwe. Ivyo vyoshobora guteba, canke mbere bigatuma porogarama ihungabana iyo amakuru ari manini cane.


Ahubwo, turashobora gukora amakuru **bukebuke**, uko ashika canke asomwa, nk’aho wonywa amazi biciye mu nzira aho kugerageza kunywa ikirahuri cose icarimwe. Ivyo vyitwa **umugezi**.


Muri NodeJS, umugezi ni ikintu kigufasha gusoma amakuru ava ku nzira canke kwandika amakuru ku nzira **igice kimwe ku gihe**.


NodeJS ifise ubwoko bune bw'imigende:



- Ishobora gusomwa**: imigende ushobora gusoma amakuru (nk'ugusoma dosiye)
- Writable**: imigende ushobora kwandikako amakuru (nk'ukwandika muri dosiye)
- Duplex**: imigende ishobora gusomwa no kwandikwa
- Guhindura**: nk'imigezi ibiri, ariko ishobora guhindura (guhindura) amakuru uko agenda


### Imigezi isomwa


Reka tuvuge ko ufise `bigfile.txt` yo gukora. Ushobora kurema uruzi rusomwa n'umurongo wa `fs` kugira usome dosiye igice ku kindi.


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


None aha bigenda gute?


1. `fs.remaShomaUmugezi()` irema umugezi usomwa.

2. Igihe cose igice ca dosiye giteguwe, umugezi urasohora ikintu ca `data` maze ukaduha "igice" c'amakuru (`Buffer`). Turacapura igice.

3. Iyo dosiye yose isomwe, ikintu `iherezo` kiratangura.

4. Iyo hari ikosa (nk’aho dosiye itabaho), ikintu `ikosa` kiratangura.


Uko ni ko, ushobora gusoma amadosiye maninimanini utayashize yose mu ciyumviro icarimwe.


Niba dushaka ko amakuru ashika mu buryo bushobora gusomwa n'umuntu (aho kuba mu buryo bubiri), turashobora gusobanura uko uruzi rushirwa:


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


Ubu iyo kode izocapura iyo dosiye mu buryo umuntu ashobora kuyisoma.


### Imigende ishobora kwandikwa


Umugezi wandikwa uragufasha kohereza amakuru ahantu kanaka, igice ku kindi.


Aha ni akarorero ko kwandika kuri dosiye `target.txt` ukoresheje umugezi:


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


Ehe ivyo bishika:


1. `fs.remaUmugeziWandika()` irema umugezi wandikwa.

2. Turayindikako umwandiko dukoresheje `.write()`.

3. Iyo tumaze guheza, duhamagaye `.end()` kugira ngo dufunge umugezi.

4. Iyo amakuru yose yanditswe, igikorwa ca `finish` kirasohoka.

5. Iyo hari ikintu kigenda nabi, ikintu `ikosa` kiravyuka.


Nka kurya kw’imigende isomwa, imigende yandikwa ni myiza ku makuru manini kuko ntikeneye kugumiza vyose mu mutwe icarimwe.


### Inzuzi z'amazi


Kimwe mu bintu vyiza cane ku migezi ni uko ushobora kuyi **pipe** hamwe: gufatanya umugezi usomwa n'umugezi wandikwa.


```javascript
const fs = require("fs")

const readable = fs.createReadStream("bigfile.txt")
const writable = fs.createWriteStream("target.txt")

readable.pipe(writable)
```


Aha:



- Umugezi usomwa usoma kuva kuri `dosiye nini.txt`.
- Umugezi wandikwa wandika kuri `copy.txt`.
- `.pipe()` yohereza amakuru ataco akora kuva ku gusoma gushika ku kwandika.


### Inzuzi zibiri


Umugezi w’ibice bibiri urashobora gusomwa no kwandikwa. Akarorero kamwe ni socket y’urubuga: ushobora kuyirungikira amakuru no kuyironka amakuru.


Aha ni akarorero koroshe cane hakoreshejwe `net` module:


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


Muri aka karorero:



- Ikintu `socket` ni umugezi w'ibice bibiri.
- Ushobora `kwandika()` kuri yo no kwumviriza `amakuru` ibintu biva kuri yo.


### Guhindura imigezi


Umugezi w’ihindura ni umugezi w’ibice bibiri kandi uhindura amakuru aca muriwo.


Nk'akarorero, ushobora gukoresha `zlib` yubatswemwo kugira ngo ushiremwo canke ushiremwo amakuru.


Ehe ingene wofata dosiye ukoresheje umugezi wo guhindura:


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


Kandi kugira ngo uyisubize:


```javascript
const readable = fs.createReadStream("bigfile.txt.gz")
const unzip = zlib.createGunzip()
const writable = fs.createWriteStream("bigfile.txt")

readable.pipe(unzip).pipe(writable)

writable.on("finish", () => {
console.log("File decompressed.")
})
```


Guhindura imigende ni ngirakamaro cane ku bikorwa nk’ugufatanya, gupfuka, canke guhindura uburyo bwa dosiye mu gihe uriko urahindura.


### Gusubira inyuma


Rimwe na rimwe umugezi wandikwa urateba gufata amakuru. Nitwaguma dusunika amakuru ku kintu co kwandika vyihuta kuruta uko gishobora, twoshobora guhura n’ingorane. Ivyo vyitwa **ugusubira inyuma**.


Niwahamagara uburyo `.write()` ku ruzi rwanditswe, bugarukana boolean ikumenyesha nimba uruzi rukeneye guhagarara; ushobora gusuzuma agaciro kayo, nk'ibi:


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


Iyi yari akarorero k'akarorero k'ugukoresha amaboko amakuru kuva ku gisomwa gushika ku canditswe, no gucunga umuvuduko w'inyuma n'amaboko.


Kenshi na kenshi twokoresha amakuru dukoresheje uburyo bwa `.pipe()`, bukorana n'umuvuduko w'inyuma ubwabwo.


Rero ukeneye gusa kwiganyira ku bijanye n'ugusubira inyuma iyo kubera imvo zimwe zimwe uriko urahamagara `.write()`.


## Iciyumviro ca nyuma

<chapterId>139e2ab8-df67-525a-85f0-5a2fa5e478f2</chapterId>


Rero, nivyo, iyo wakurikiye ivyigwa, ubu ushobora kwandika porogarama zimwe zimwe zoroheje muri NodeJS.


Nashaka gusaba ko wokora ivyo nyene: umaze kwiga ivy’ishimikiro, kwubaka imigambi mikeyi y’umuntu ku giti ciwe ni uburyo bwiza bwo kwimenyereza no kuba umuhinga mu bijanye n’ivy’iporogarama.


Ntaco bimaze vy’ukuri ivyo wubaka, ikintu gihambaye ni uko witera ingorane zo gutorera umuti ingorane ukoresheje kode.


Indimi za porogarama zo muri iki gihe zirakomeye cane, kandi NodeJS birashoboka ko ari yo sandugu nziza cane yo kugerageza muri iki gice c’urugendo rwawe.


Amahigwe masa!


# Igice ca nyuma


<partId>322624d8-6fbc-11f0-a67a-5b145f10afc1</partId>


## Amasuzuma n'Ibipimo


<chapterId>3e93ac86-6fbc-11f0-8bae-9b2ed7914843</chapterId>

<isCourseReview>true</isCourseReview>

## Iciyumviro


<chapterId>49b3b9b2-6fbc-11f0-9870-5f5adcd3a0eb</chapterId>


<isCourseConclusion>true</isCourseConclusion>