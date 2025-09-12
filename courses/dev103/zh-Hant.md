---
name: JavaScript 和 NodeJS 基礎
goal: 學習 JavaScript 程式設計基礎和 NodeJS 開發，以建立實用的應用程式和工具。
objectives: 

  - 掌握 JavaScript 的基本語法、類型和控制流程
  - 瞭解 JavaScript 中的函數、物件和類別
  - 學習錯誤處理和除錯技巧
  - 了解 NodeJS 及其生態系統

---

# 開始您的開發之旅


歡迎來到 JavaScript 和 NodeJS 的課程。


JavaScript 是世界上最流行的程式語言：它是現代瀏覽器的腳本語言，因此要建立一個現代的 Web 應用程式，基本上不可能不寫一些 JavaScript；有了 NodeJS runtime，它也可以用在瀏覽器之外，建立直接在電腦上執行的腳本和應用程式。


本課程針對完全不懂程式設計的人，或之前使用過其他語言但想瞭解 JavaScript 如何運作的人，尤其是在 NodeJS 的環境下。


課程結束時，您應該能夠用 JavaScript 寫自己的程式、使用 NodeJS 標準函式庫，以及安裝和使用第三方套件來建立有用的工具。


+++
# 基本 JavaScript

<partId>a617327c-e5a2-52ca-9380-c63f44623dd4</partId>


## 設定

<chapterId>ba05a290-1782-5268-87c9-62fd09590e05</chapterId>




JavaScript 程式只是（一個或多個）文字檔的集合，其中包含要由 JavaScript runtime 執行的指令。


這些文字檔的名稱通常以 `.js` 檔案副檔名結尾，例如 `my_script.js`、`my_program.js` 等。


它們所包含的指令是以 JavaScript 程式語言撰寫的。


JavaScript runtime 是執行這些檔案的特殊程式。


![](assets/en/1.webp)


### NodeJS 執行環境


最常見的 JavaScript 運行時間是 NodeJS。


您的IDE可能已經包含它，或者您可能需要從[官方網站](https://nodejs.org/en/download)下載它。


下載頁面將為您提供所有三種主要 OS（作業系統）的說明：Windows、Linux 和 MacOS。它假設您知道如何在您的作業系統中開啟終端機。


由於 NodeJS 適用於所有三種作業系統，因此您所寫的程式將可在所有作業系統上執行 (除了某些邊緣情況)。


舉例來說，這表示您可以在 Windows PC 上以 JavaScript 寫一個簡單的電視遊戲，然後交由您的朋友在他的 Mac 上執行。


![](assets/en/2.webp)














### 第一個程式 (hello world)


傳統上，當學習程式語言時，寫的第一個程式就是在控制台列印「hello world!」。


建立一個名為 `my_js_code/` 的目錄，裡面有一個名為 `main.js` 的檔案 (這些名稱是任意的)。


使用程式碼編輯器打開目錄。


將此程式碼寫入您的檔案：


```javascript
console.log("hello world!")
```


開啟終端機並執行此指令以執行程式：


```
node main.js
```


結果應該是


```
hello world!
```


### 發生了什麼事


在 JavaScript 中，所有東西都是一個「物件」。


`console` 是一個物件，用來調試程式。


`console.log` 是 `console` 最常用的方法。它只會列印您傳給它的任何參數。


您可以使用圓括號 `()`，傳送參數給 `console.log`。


因此，舉例來說，如果您要列印數字 `1000`，您只需寫入


```javascript
console.log(1000)
```


然後執行


```
node main.js
```


在您的終端機 (從現在開始，本課程將假設您知道這是執行程式的方式)。


這應該列印


```
1000
```


您可以傳送多種東西，例如


```javascript
console.log(16, 8, 1993)
```


這將列印


```
16 8 1993
```


## 變數和注釋

<chapterId>23050ab7-343b-5edf-9d37-e4e782e27ce0</chapterId>


程式通常會執行資料上的作業。


變數就像是我們用來儲存資料的命名方塊。它們允許我們將一項資料與特定名稱相關聯，以便稍後能夠使用該名稱來擷取資料。


### `let` 聲明


要在 JavaScript 中宣告變數，我們可以使用 `let` 關鍵字。


在寫入 `let` 之後，我們寫入要賦予變數的名稱，然後是 `=` 符號，接著是要儲存的值。


例如：


```javascript
let age = 25

console.log(age)
```


變數的名稱（技術上稱為「識別符」）通常可以包含字母、下劃線 (`_`)、美元符號 (`$`)和數字，但第一個字元不能是數字。


在上面的程式碼中，我們宣告了一個名為 `age` 的變數，並在其中儲存值 `25`。


然後，我們使用 `console.log(age)` 來列印數值。


如果使用 `node main.js` 執行此程式碼，輸出將會是：


```
25
```


識別符是大小寫敏感的，這表示小寫和大寫都算為識別符的差異，因此例如


```javascript
let age = 25

let Age = 20

console.log(age)
```


將列印 25，因為這些被視為兩個完全獨立的變數！


您也可以在變數中儲存字串 (文字)：


```javascript
let message = "hello again"

console.log(message)
```


這將列印出來：


```
hello again
```


就像之前一樣，我們使用 `console.log()` 來列印儲存在變數中的值。


現在讓我們一起做這兩件事：


```javascript
let age = 25

let message = "hello again"

console.log(age)

console.log(message)
```


執行此功能將會列印：


```
25
hello again
```

### 調任


使用 `let` 宣告的變數可以在建立後更改。


這稱為重新分配。


```javascript
let score = 10

console.log(score)

score = 15

console.log(score)
```


首先，我們將 `10` 指定給 `score`，然後列印出來。


然後，我們將 `score` 的值變更為 `15` 並再次列印。


輸出將會是


```
10
15
```


當值隨時間改變時，這非常有用，例如在分數增加的遊戲中。


讓我們再加入一個變數：


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


這將列印出來：


```
10
Alice
20
Bob
```


如您所見，`score` 和 `player` 都被變更了。


### `const` 聲明


但大多數情況下，我們不希望變數在建立後改變。為此，我們使用 `const`。


`const` 是 「常數」 的縮寫。一旦您為 `const` 變數指定值，您就不能改變它。


```javascript
const pi = 3.14
console.log(pi)
```


此處列印：


```
3.14
```


但如果你想這麼做


```javascript
const pi = 3.14
console.log(pi)

pi = 99 // this line will cause an error
console.log(pi)
```


JavaScript 會給您類似這樣的錯誤：


```
TypeError: Assignment to constant variable.
```


這是因為 `pi` 是使用 `const` 宣告的，之後就不能改變它的值了。您是在向 JavaScript 解譯器傳達您不希望變數改變的訊息。


這樣做很有用，因為可以減少錯誤變更的機會。當程式變得非常大，有成千上萬行的程式碼時，就不可能一下子跟上所有正在發生的事情（這就是我們使用電腦的主要原因，來執行我們無法用腦子計算的複雜程序），所以有這樣的限制就變得很有用，可以讓程式變得更確定。


除非我們確定之後要修改這些值，否則最好的做法是將值宣告為 `const`。


### JavaScript 中的評論


有時候，我們想在程式碼中寫下不被執行的注解。這些稱為備註。


程式執行時，註解會被忽略，但對於向自己或其他人解釋事情很有用。


若要撰寫單行註解，請使用 `//`


```javascript
// This is a comment
const x = 10 // This is also a comment
console.log(x)
```


這樣仍會列印：


```
10
```


評論只是供人們閱讀。


您也可以使用 `/*` 和 `*/` 寫多行註解


```javascript
/*
This is a multi-line comment.
It can span several lines.
*/
const y = 20
console.log(y)
```


這將列印


```
20
```


而評論會被忽略。


您可以使用註解為您的程式碼加入小註解，這樣您就可以記住程式碼的作用以及為何以某種方式寫成。它也可以幫助其他程式設計師理解它。


## 基本類型：數字、字串、布林值

<chapterId>cfdb04f6-21a8-5143-bbf9-7aaae04962f0</chapterId>


在 JavaScript 中，「類型」會告訴您某個值是哪種資料。


Javascript 有幾種基本類型，本節我們將探討其中一些類型。


### 數字和算術運算


我們要介紹的第一個類型是 `number`。


JavaScript 中的數字可以是整數 (如 `5`)，也可以是小數 (如 `3.14`)。


您可以使用它們進行算術運算：加法、減法、乘法和除法。


這裡有一個基本的範例：


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


這將列印出來：


```
15
5
50
2
```


您也可以使用括號 `()` 來控制操作的順序：


```javascript
const result = (2 + 3) * 4
console.log(result)
```


此處列印：


```
20
```


如果沒有小括號，就會是 `2 + 3 * 4`，也就是：


```javascript
const result = 2 + 3 * 4
console.log(result)
```


這樣就可以列印了：


```
14
```


因為在一般的數學中，乘法發生在加法之前。


### 字串與插補


我們要介紹的第二個 JavaScript 類型是 `string`。


字串是一段一段的文字。您可以使用單引號`'...'`或雙引號`"..."`來建立它們。


```javascript
const greeting = "hello"
const name = 'Bob'
console.log(greeting)
console.log(name)
```


此處列印：


```
hello
Bob
```


若要組合字串，您可以使用 `+` 運算符號：


```javascript
const greeting = "hello"
const space = " "
const name = "Bob"

const fullGreeting = greeting + space + name
console.log(fullGreeting)
```


這將列印出來：


```
hello Bob
```


但有一種更佳的方式來組合字串，稱為 ** 字串插值**。您使用反向鍵來宣告字串 ``...`` 並在字串內使用 `${...}` 來寫變數：


```javascript
const greeting = "hello"
const name = "Bob"

const fullGreeting = `${greeting} ${name}`
console.log(fullGreeting)
```


這也會列印出來：


```
hello Bob
```


您可以在`${...}`內包含任何表達式：


```javascript
const age = 30
console.log(`Next year, I will be ${age + 1} years old.`)
```


此處列印：


```
Next year, I will be 31 years old.
```


插值在現代 JavaScript 中非常普遍。


### 布林、比較和邏輯運算


我們要介紹的第三種類型是 `boolean`。它是以數學家 George Boole 命名的，他發明了布林邏輯。


布林值很簡單：只有兩個可能的值，`true` 和`false`。


您可以將它們儲存在變數中：


```javascript
const theSkyIsBlue = true
const thisCourseIsBad = false

console.log(theSkyIsBlue)
console.log(thisCourseIsBad)
```


此處列印：


```
true
false
```


您可以使用邏輯運算符號組合布林值：



- `&&` 表示 「和」，只有當 ** 兩個**值都是`true`時，它才會返回`true`，否則會返回`false`。
- ||` 表示 「或」，如果 ** 值中至少有一個**是 "true「，它會返回 」true「，否則（如果它們都是 false），它會返回 」false"。
- `！`的意思是 「不是」，它應用在布林值之前，並會翻轉布林值：如果布林值是`true`，它會返回`false`，反之亦然。


![](assets/en/3.webp)


範例：


```javascript
const isSunny = true
const isWarm = true

console.log(isSunny && isWarm)  // true
console.log(isSunny || isWarm)  // true
console.log(!isSunny)           // false
```


您可以在 JavaScript 中使用 `>`、`<`、`===` 和 `!==` 等運算符號來比較數值。這些比較的結果永遠都是布林值。


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


Javascript 也有 `>=` 表示「較大或相等」，而 `<=` 表示「較小或相等」。


布林、比較和邏輯運算符通常會在程式中結合，以宣告複雜的條件，例如確保「電子郵件已經寄達，且包含我需要的圖片，或電子郵件的長度超過 10000 個字元」。您稍後就會發現，這些都是建構程式邏輯的重要基石。


## 陣列、null、未定義

<chapterId>7bf18183-5eae-53ed-83d2-b04982145d81</chapterId>


在本節中，我們將介紹另外三種在 JavaScript 程式中非常常見的類型：



- 陣列**：值的序列
- undefined**：一個特殊值，表示「沒有任何指派」。
- null**：另一個特殊值，表示「故意為空」。


### 陣列和索引存取


**陣列**是一種類型，可以在清單中保存多個值。


使用方括號 `[]` 並以逗號分隔項目，即可建立陣列。


這裡有一個基本的範例：


```javascript
const numbers = [10, 2, 88]
console.log(numbers)
```


此處列印：


```
[ 10, 2, 88 ]
```


您可以在陣列中儲存任何東西，不只是數字：


```javascript
const things = ["apple", 42, true]
console.log(things)
```


此處列印：


```
[ 'apple', 42, true ]
```


要存取陣列中的特定項目，我們使用 **索引**。索引是項目的位置，從 **0** 開始。


所以在這個陣列中：


```javascript
const colors = ["red", "green", "blue"]
```



- colors[0]`是`"red"`。
- colors[1]`是`"Green"`。
- colors[2]` 是`"blue"`。


試試看


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[0])
console.log(colors[1])
console.log(colors[2])
```


這將列印出來：


```
red
green
blue
```


您可以為陣列的特定索引指定值


```javascript
const colors = ["red", "green", "blue"]

colors[1] = "yellow"

console.log(colors)
```


這將列印出來：


```
[ 'red', 'yellow', 'blue' ]
```


您可以使用任何自然數作為索引，甚至是儲存在變數中的自然數。


```javascript

const i = 1
const colors = ["red", "green", "blue"]
console.log(colors[i])
```


這將列印出來：


```
green
```


但如果您嘗試存取不存在的索引，您會得到 `undefined`：


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[3])
```


此處列印：


```
undefined
```


那是什麼？


### 未定義


特殊值 `undefined` 表示 「沒有指定值」。


如果您建立一個變數，但沒有給它一個值，它將會是`未定義的`：


```javascript
const name
console.log(name)
```


此處列印：


```
undefined
```


因為我們沒有為 `name` 指定任何東西，JavaScript 預設將它設定為「未定義」。


如前所述，當您存取不存在的陣列索引時，也會得到 `undefined`：


```javascript
const fruits = ["banana", "apple"]
console.log(fruits[2]) // There is no index 2
```


此處列印：


```
undefined
```


### `null`以及如何處理它


`null`也是一個特殊的值。它的意思是 「這裡什麼都沒有，我故意這樣做的」。


與自動設定的 `undefined` 不同，`null` 是您自己設定的。


例如：


```javascript
const currentUser = null
console.log(currentUser)
```


此處列印：


```
null
```


為什麼要使用 `null`？也許您稍後期待一個值，但它還沒準備好：


```javascript
let winner = null

// Later in the program:
winner = "Alice"

console.log(winner)
```


此處列印：


```
Alice
```


因此，當您想要說：「這裡稍後應該會有東西，但現在是空的 」時，`null` 就會很有用。


## 區塊和控制流程

<chapterId>be985168-2636-5b0d-a48f-ac1bbfbff8a7</chapterId>


到目前為止，我們所寫的大多數都是一條接一條執行的程式碼。


但是當我們編碼時，我們可以控制它的執行順序。


這稱為 ** 控制流程。


讓我們從了解區塊和範圍開始。


### 全球範圍


我們宣告的每個變數都存在於**範圍**，也就是變數已知的程式碼區域。


如果您在任何區塊之外宣告變數，則該變數存在於 ** 全局範圍**。


```javascript
const color = "blue"
console.log(color)
```


這個變數 `color` 在全局範圍內，所以可以從檔案中的任何地方存取。


如果您新增更多行：


```javascript
const color = "blue"
console.log(color)

const size = "large"
console.log(color)
console.log(size)
```


`color` 和 `size` 都是全局變數。它們在檔案中隨處可用。


但在區塊內部會發生什麼事？


### 區塊和局部範圍


**block** 是由大括弧 `{}` 包圍的一段程式碼。


在區塊中以 `let` 或 `const` 宣告的變數，***只存在於該區塊中。


```javascript
{
const message = "inside block"
console.log(message)
}
```


此處列印：


```
inside block
```


但如果你試試這個


```javascript
{
const message = "inside block"
}
console.log(message) // Error!
```


JavaScript 會給您類似這樣的錯誤：


```
ReferenceError: message is not defined
```


這是因為 `message` 是在區塊內宣告的，在區塊外並不存在。


這意味著我們可以使用區塊來隔離程式碼的一部分，並確保 「發生在區塊中的事情不會在區塊中發生」（還挺像拉斯維加斯的）。


以區塊來組織程式碼，也讓我們可以結構化程式的執行，使用控制流程的結構，例如 `if


### `if`, `else`


有時候，我們只想在某些事情為真的情況下執行程式碼。這就是 `if` 語句的作用。


```javascript
const myAge = 20

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


此處列印：


```
Am I an adult?
Yes I am!
```


如您所見，代碼會比較 `myAge` 和 `18`。

在這種情況下，運算符號 `>=` 會返回 `true`，因此區塊會被執行。

如果條件不是 `true`，區塊不會被執行。


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


此處列印：


```
Am I an adult?
```


您可以新增一個 `else` 區塊來處理相反的情況：


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
} else {
console.log("No, I am not.")
}
```


此處列印：


```
Am I an adult?
No, I am not.
```


`if` 和 `else` 區塊仍然是區塊 - 因此在區塊內宣告的變數在區塊外並不存在。


如果我們想要確定某件事是***不是真的，我們可以怎麼做？


正如之前所討論的，JavaScript 有一個「not」運算元，可以翻轉布林值。所以我們可以


```javascript
const myAge = 17

const adult = myAge >= 18

console.log("Am I an adult?")

if (!adult) {
console.log("No, I am not.")
}
```

這仍然可以列印：


```
Am I an adult?
No, I am not.
```

因為我們使用了 `!` 運算子來反轉 `adult` 變數。


`if (!adult) {...}` 應該讀成 "if not adult..."


使用區塊、邏輯和比較運算符，我們可以透過定義變數的方式來組織程式的執行，這些變數必須是 `true` (或 `false`)才會發生。


### 同時」、「中斷」、「繼續


只要*條件為真，`while`迴圈就會重複執行程式碼。


```javascript
let count = 0

while (count < 3) {
console.log("Count is", count)
count = count + 1
}
console.log("the loop is over!")
```


此處列印：


```
Count is 0
Count is 1
Count is 2
the loop is over!
```


當 `count` 變為 3 時，循環停止。


您可以使用 `break` 提前停止循環：


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


此處列印：


```
0
1
2
```


因為當數字變成`3`時，`if`區塊會被執行，並停止循環。


您可以使用 `continue` 跳過循環的其餘部分：


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


此處列印：


```
1
2
4
5
```


因為當數字是 `3` 時，`continue` 會使程式跳過列印數字的那一行。


### `為...的...`


如果您有一個陣列，並且想要對陣列中的每個項目做一些事情，您可以使用 `for ... of ...{...}`.


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const fruit of fruits) {
console.log(fruit)
}
```


此處列印：


```
apple
banana
cherry
```

陣列中的每個元素都會執行一次該區塊。


這裡的 `fruit` 是一個新變數，可以取得陣列中每個項目的值，以便在區塊中對其進行操作。


### 為...在...`


您可以使用 `for ... in` 來循環陣列的 key (索引)：


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(index)
}
```


此處列印：


```
0
1
2
```


您也可以使用索引來取得數值：


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(fruits[index])
}
```


這與 `for ... of` 的列印方式相同：


```
apple
banana
cherry
```


實際上，對於陣列，您應該偏好使用 `for ... of`，因為它比較簡單乾淨。


### 有界迴圈


有時候我們想要循環特定的次數，或是在一般情況下寫一段重複區塊的程式碼，同時追蹤某些東西。

這就是有界的 `for` 環路的好處。

有界迴圈通常包含三個條件，以分號`;`分隔，如`(... ; ... ; ....)`。


```javascript
for (let i = 0; i < 3; i = i + 1) {
console.log(i)
}
```


此處列印：


```
0
1
2
```


讓我們來解釋一下：



- `let i = 0`: 宣告要在區塊中使用的變數 (在本例中是一個從 0 開始的計數器)
- `i < 3`: 宣告要執行區塊的條件為 `true` (在本例中為 "repeat while `i` is less than 3")
- `i = i + 1`：在每次執行區塊後，宣告一些要執行的程式碼 (在本例中為「將 `i` 增加 1」)


如您所見，有界迴圈讓我們可以為重複執行一段程式碼宣告更複雜的條件，但大多數時候這並非必要。


### 區塊標籤


如果您要寫更複雜的控制流程，JavaScript 可以讓您使用**標籤**來命名一個區塊，這個**標籤**可以被 `break` 或 `continue` 用來指定**跳回的位置。


範例：


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


此處列印：


```
Inside outer block
Inside inner block
Done
```


我們使用 `break outer` 來完全退出 `outer` 區塊。


您也可以標示循環。讓我們以這個範例為例：


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

這是一個非常無聊的例子，但希望它能闡明（偶爾）對標籤的需求。


## 介紹功能

<chapterId>cc324715-09c2-5cf7-9e6f-47a6f16bc04d</chapterId>


當您的程式成長時，您會經常想要**重複使用**段程式碼。


這就是**函數**的作用：它讓您將一些程式碼組合起來，給它一個名稱，並隨時執行。


### 功能聲明


要宣告函數，我們可以使用 `function` 關鍵字。然後，我們給它一個名稱、一對括號`()`表示它所接受的參數，以及要執行的程式碼區塊`{}`。讓我們從一個不需要任何參數的函數開始：


```javascript
function sayHello () {console.log(`Hello!`) }
```


此代碼**宣告**函數，但尚未***執行函數。


### 功能呼叫


若要執行 (或「呼叫」) 函式，您必須在函式名稱後加上括號：


```javascript
function sayHello () {console.log(`Hello!`) }
sayHello()
```


此處列印：


```
Hello!
```


您可以隨意多次呼叫該函數：


```javascript
function sayHello() {
console.log("Hello!")
}

sayHello()
sayHello()
```


此處列印：


```
Hello!
Hello!
```


函式內的程式碼只有在您呼叫它時才會執行。


### 函數參數 (函數的輸入)


有時候，您希望函數在某些輸入的情況下運作。您可以在括號內加入 **參數**。


例如：


```javascript
function sayHelloTo (friend) {
console.log(`Hello ${friend}!`)
}
```


現在這個函式需要 ** 個參數**，稱為 `friend`。


當您呼叫函數時，您可以傳入一個值：


```javascript
sayHelloTo("Tommy")
```


此處列印：


```
Hello Tommy!
```


您可以使用不同的名稱再次呼叫函式：


```javascript
sayHelloTo("Sam")
```


此處列印：


```
Hello Sam!
```


您傳入的值會取代函式中的 `friend` 變數。


您也可以使用多個參數：


```javascript
function greetTwoPeople(person1, person2) {
console.log(`Hello ${person1} and ${person2}!`)
}

greetTwoPeople("Lina", "Marco")
```


此處列印：


```
Hello Lina and Marco!
```


### return`（函式的輸出）


函數也可以**返回**值。這表示它們會將值傳回函式被呼叫的地方。


這裡有一個簡單的例子：


```javascript
function getNumber() {
return 42
}

const result = getNumber()
console.log(result)
```


此處列印：


```
42
```


函數 `getNumber()` 會返回 `42`，我們將它存入 `result` 中，然後將它列印出來。


您也可以返回您計算出來的東西：


```javascript
function add(a, b) {
return a + b
}

const result = add(2, 3)
console.log(result)
```


此處列印：


```
5
```


一旦`return`了一個值，函數就會停止。該區塊中 `return` 之後的任何事情都不會發生。


```javascript
function saySomething() {

return "hi"

console.log("this never runs")

}

const message = saySomething()
console.log(message)
```


僅此列印：


```
hi
```


因為只有 `"hi"` 會被傳回。會跳過`console.log("this never runs")`這一行。


您可以將函式視為小型子程式。每個函式都可以接受一些輸入、處理它，然後給您一些輸出。


如果我們嘗試使用函數的回傳值，但該函數沒有回傳任何東西，會發生什麼情況？


```javascript
function doesNothing () {}

const x = doesNothing()

console.log(x)
```

這將列印 `undefined`。沒有回傳任何東西的函數的回傳值是 `undefined`。


## 物件與類別

<chapterId>26689f25-8212-5057-8c21-3a05eee0ac75</chapterId>


JavaScript 通常被稱為物件導向語言。


這表示它可以幫助您將值和函式歸類到 ** 物件 ** 中，從而組織您的程式碼。


### 什麼是「物件」？


物件可以包含資料和操作資料的函式。當一個函數被放入物件中時，我們稱之為 `方法`。


我們看到的第一個物件是 `console` 物件。它是一個包含多種方法的物件，用來在螢幕上列印東西和調試我們的程式。


它甚至可以自行列印；您可以


```javascript
console.log(console)
```


並會列印它所包含的方法清單。例如，在我的機器上，它會列印


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


如您所見，它有許多方法可以用來除錯！


Javascript 提供我們不同的方式來建立新的物件，這些物件可以做任何我們想要他們做的事。


### 建立物件


建立物件的最簡單方法，就是使用 ** 複雜的大括弧** `{}` 將資料和函式群組起來。


這會建立我們所謂的 ** 匿名物件**。


```javascript
const cat = {
name: "Whiskers",
age: 3
}
```


這會建立一個物件，並儲存在一個名為 `cat` 的變數中。


物件有兩個 ** 屬性：



- name`的值為 `"Whiskers"`。
- 值為 `3` 的 `age`


我們來印吧


```javascript
console.log(cat)
```


此處列印：


```
{ name: 'Whiskers', age: 3 }
```


您可以使用點字從物件中取得屬性，如 `objectName.propertyName`：


```javascript
console.log(cat.name)  // prints "Whiskers"
console.log(cat.age)   // prints 3
```


您也可以**變更**屬性：


```javascript
cat.age = 4
console.log(cat.age)  // now it prints 4
```


如您所見，即使物件被定義為 `const`，您仍然可以修改它所包含的資料。


對於物件，`const` 只會阻止您覆寫整個物件：


```javascript
const cat = {
name: "Whiskers",
age: 3
}

cat.age = 5 // this works

cat = 5 // this throws an error, you're trying to reassign the whole object

```


如前所述，物件也可以容納 ** 函式**，當函式是物件的一部分時，我們稱之為 ** 方法**。


這裡有一個範例：


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log("Meow!")
}
}
```


此物件有



- 一個 `name` 屬性
- 說話() "方法


讓我們呼叫方法：


```javascript
cat.speak()
```


它會列印：


```
Meow!
```


方法可以透過關鍵字 `this` 使用物件所包含的資料。

`this` 指目前的物件。在這個範例中，它將被用來列印貓的名稱：


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log(`${this.name} says meow!`)
}
}

cat.speak()
```


此處列印：


```
Whiskers says meow!
```


this 「的意思是 」這個物件"......在這個例子中，是指 `cat` 物件。



當您只想要快速簡單的物件時，這類物件是很好的選擇。但如果您需要以相同的結構建立**多個物件**，有一個更好的方法，那就是 **類別**。


### 類和建構器


** class** 就像是一個藍圖。它告訴 JavaScript 如何建立某種物件。


您可以使用 `class` 關鍵字來定義類別，接著是類別的名稱和大括弧 `{}` 區塊。


```javascript
class Dog {}
```


按照慣例，班級通常以大寫字母開頭。


您可以使用 `new` 建立類別的新物件：


```javascript
const hachiko = new Dog()
```


嘗試列印物件：

```javascript
class Dog {}

const myDog = new Dog()

console.log(myDog)
```


您將獲得


```
Dog {}
```


您可以看到 Dog 類別是空的，所以 `myDog` 物件也是空的。


我們可以加入一個 `constructor` 來定義 Dog 物件應該包含哪些屬性。


建構器是在您建立（或「建構」）新物件時執行的特殊函式。


```javascript
class Dog {
constructor() { }
}
```


我們希望每個 Dog 都有一個名稱，因此我們在函式中加入一個 `name` 參數：


```javascript
class Dog {
constructor(name) { }
}
```


然後我們使用 `this` 來宣告 `name` 是我們要建立的 `Dog` 物件的`name`。


```javascript
class Dog {
constructor(name) {
this.name = name
}}
```


現在讓我們嘗試使用它：


```javascript
class Dog {
constructor(name) {
this.name = name
}
}

const myDog = new Dog("hachiko")

console.log(myDog)
```


這會列印出類似的內容：


```
Dog { name: 'hachiko' }
```


如您所見，`constructor` 方法會接收您在執行 `new Dog()` 時傳給類別的參數，並使用這些參數來建立物件。


我們來分析一下：



- `class Dog` 定義 Dog 類別。
- 當物件被建立時，`constructor(name)` 會設定該物件。
- `this.name = name` 將值儲存到新物件中。
- `new Dog("hachiko「)` 從這個類別建立一個新物件，並將 `name` 屬性設定為 `」hachiko"。


現在讓我們在類別中加入一個方法：


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


這將列印


```javascript
hachiko says barf!
```


如果我們對兩個不同的 Dog



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


我們得到


```
hachiko says barf!
bobby says barf!
```


speak()`方法使用被呼叫的`Dog`的`name`屬性。


這就是類別存在的主要原因：它們讓我們可以定義一組對資料進行操作的方法，然後創建多個共用相同資料「形狀」的物件。


當我們呼叫這些物件中的一個物件的方法時，它會對該特定物件*所持有的資料進行操作。


### 變更物件的形狀


JavaScript 中的物件是靈活的。即使在您建立了一個物件之後，您仍然可以新增屬性或移除現有的屬性。


這是允許的，但您應該小心使用。


讓我們從簡單的 `Dog` 類開始：


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


此時，`myDog` 只有一個屬性：`name`。我們仍可在建立後新增屬性：


```javascript
myDog.age = 5

console.log(myDog.age) // prints 5
```


我們也可以新增一個方法：


```javascript
myDog.jump = function () {
console.log(`${this.name} jumps!`)
}

myDog.jump() // Fido jumps!
```


我們也可以使用 `delete` 關鍵字來移除屬性。


```javascript
delete myDog.name

console.log(myDog.name) // prints 'undefined'
```


這方法可行，但有一點很重要：當您的物件始終維持相同的屬性時，JavaScript 引擎如 V8 (用於 Node.js 和 Chrome 瀏覽器) 會執行得更快。如果您在物件建立後才新增或移除屬性，可能會導致速度變慢。


在小型程式中，這並不重要。但在較大的專案中（如遊戲），最好一開始就在構建器中列出所有屬性，即使您不會立即使用它們。這樣可以保持物件形狀的穩定，並幫助您的程式碼執行得更快。


例如，而不是這樣：


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


您可以


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


兩個版本都可以運作，但第二個版本在效能上較好。您可以事先告訴引擎每個物件會有哪些屬性，它就可以依此進行最佳化。


JavaScript 可以讓您自由地重塑物件，但在使用類別時，最好事先規劃好物件的形狀。



### 使用`extends`和`super()`繼承


有時候，您想要建立一個與其他類別*幾乎一樣的類別，但卻有一些額外的功能。


與其修改物件的形狀 (如前所述，這對效能而言並非最佳)，或是從頭重寫一個新的類別，JavaScript 讓您使用一種稱為 ** 繼承的方式。


繼承意味著一個類別可以**延伸**另一個類別。新類別會得到舊類別的所有屬性和方法，您可以增加或變更您需要的內容。


假設我們有一個叫做 `Vehicle` 的基本類別：


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


現在我們要做一個 `Car` 類。汽車是一種交通工具，但我們可能希望它有一些額外的功能，或是在啟動時有不同的訊息。我們可以使用 `extends` 來代替重寫所有的東西：


```javascript
class Car extends Vehicle {
start() {
console.log(`${this.brand} car is ready to drive!`)
}
}
```


Car` 類現在**繼承**了 `Vehicle` 的一切。它得到了 `brand` 屬性，而且我們用自己的版本取代了 `start()` 方法。


![](assets/en/4.webp)


讓我們試試看：


```javascript
const myCar = new Car("Toyota")
myCar.start()
```


此處列印：


```
Toyota car is ready to drive!
```


即使 `Car` 沒有自己的建構子，它還是會使用 `Vehicle` 的建構子。但是如果我們想在 `Car` 中寫一個自訂的構造子，我們可以，我們只需要使用 `super()`，包含對其父代構造子的呼叫。


方法如下：


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



此處列印：


```
Toyota Corolla is ready to drive!
```


因此總結一下



- `extends` 表示一個類別以另一個類別為基礎。
- `super()` 用來呼叫您要擴充的類別的建構子。
- 新類會取得原始類別的所有屬性和方法。
- 您可以 ** 覆寫** 方法 (像是 `start()`)，讓它們做不同的事情。


當您有幾個相似的東西（如汽車、卡車和腳踏車），而您希望它們共用程式碼，但仍以各自的方式運作時，這將很有幫助。


### `instanceof`


`instanceof` 關鍵字會檢查物件是否由某個類別所建立。


假設我們有一個叫做 `User`的類別：


```javascript
class User {
constructor(username) {
this.username = username
}
}

const regularUser = new User("julia123")

console.log(regularUser instanceof User)
```


此處列印：


```
true
```


確認 `regularUser` 是一個 `User`。這是因為 `regularUser` 是使用 `User` 類建立的。


它也適用於**繼承**的類別。例如，這裡有一個擴充了 `User` 的 `Admin` 類：


```javascript
class Admin extends User {}

const ourAdmin = new Admin("admin42")

console.log(ourAdmin instanceof Admin)   // true
console.log(ourAdmin instanceof User)    // true
```


兩行都返回 `true`。這是因為 `Admin` 是 `User` 的子類，所以 `ourAdmin` 既是 `Admin` 也是 `User` 。


# 中級 JavaScript

<partId>243f63ab-4f34-5c30-80cb-84ef46f6761d</partId>


## 錯誤處理

<chapterId>d0206bc5-d386-5e7f-9917-5803f392448c</chapterId>


當您寫出更複雜的 JavaScript 程式時，您會遇到**錯誤**。這些是出錯的意外情況。也許變數是「未定義」的，但您卻試著使用它，或是某些程式碼接收到錯誤的輸入類型。


如果我們沒有正確處理這些錯誤，我們的程式可能會當機或出現不可預測的行為。JavaScript 提供了偵測和管理這些錯誤的工具，讓我們可以更優雅地處理這些錯誤。


### 常見錯誤：在 `undefined` 上存取值


以下是導致錯誤的常見情況：


```javascript
const user = undefined
console.log(user.name)
```


如果執行此程式碼，您會得到類似以下的錯誤：


```
TypeError: Cannot read properties of undefined (reading 'name')
```


這是 JavaScript 在告訴你"Hey, you tried to get the `name` property from something that's `undefined`, and that doesn't make sense.""嘿，你試圖從某個`未定義`的東西取得`name`屬性，那是不合理的。正如您所看到的，當這種錯誤發生時，程式會停止執行，除非您特別寫了程式碼來捕捉並處理它。


### 拋出錯誤


有時候您想要在程式碼中手動 ** 產生錯誤**。在這種情況下，您可以使用 `throw` 關鍵字。


```javascript
throw new Error("This is a custom error message")
```


這會立即停止程式並列印：


```
Uncaught Error: This is a custom error message
```


您可以使用 `throw` 來強制執行程式中的規則。例如


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


第二次呼叫會導致錯誤，因為在此範例中不允許除以 0。


### 使用 `try...catch` 捕捉錯誤


如果您不希望程式在發生錯誤時當機，您可以使用「try...catch」區塊來捕獲錯誤。當您希望您的程式在發生錯誤時仍能**繼續運行時，這將會很有幫助。


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log("Oops! Something went wrong.")
}
```


輸出：


```
Oops! Something went wrong.
```


工作原理如下：



- 首先嘗試`try`區塊內的程式碼。
- 如果發生錯誤，JavaScript 會**跳到`catch`區塊**，跳過剩下的`try`區塊。
- `catch` 區塊會接收錯誤，因此您可以列印它，或以其他方式處理它，例如


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log(`The message of the error was: "${error.message}"`)
}
```


輸出：


```
The message of the error was: "Cannot read properties of undefined (reading 'name')"
```


### 最終」區塊


您也可以加入一個 `finally` 區塊。無論有沒有發生錯誤，這段程式碼都會一直執行**。


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


輸出：


```
Trying something risky...
Caught the error: Uh oh!
This will run no matter what.
```


## 避免錯誤

<chapterId>db12d9f6-5806-514c-998e-0ae24805104e</chapterId>


本章介紹 JavaScript 中一些最常見的陷阱，以及如何避免這些陷阱。


### `var`和 Assignment 無聲明


在較舊的 JavaScript 程式碼中，變數通常使用 `var` 關鍵字來宣告。與您已經學過的 `let` 和 `const` 不同，`var` 可能會有混亂的行為。


例如：


```javascript
{
var message = "hello"
}
console.log(message)
```


您可能會期望 `message` 只存在於區塊內，但事實並非如此。`var` 會忽略區塊範圍，它會讓變數在整個函式或檔案中都可用。


這可能會導致意想不到的行為，尤其是在較大的程式中。因此，現代的 JavaScript 程式碼應該總是使用 `let` 或 `const` 來取代 `var`。


更糟的是，JavaScript 可以讓您在完全不宣告變數的情況下，**為變數指定值：


```javascript
function greet() {
user = "Alice"
}
greet()
console.log(user) // prints "Alice"
```


這會在沒有任何宣告的情況下建立一個新的全局變數 `name`。這可能會無聲無息地發生，並導致 Hard 要追蹤的 bug，特別是如果這只是一個錯字。請務必使用 `let` 或 `const` 來宣告變數。


### 弱型系統


JavaScript 是弱類型的，這表示如果需要的話，它會自動將值從一種類型轉換成另一種類型。這稱為類型強制，雖然很方便，但經常會導致混亂的結果。


例如：


```javascript
console.log("5" + 1)    // "51"
console.log("5" - 1)    // 4
console.log(true + 1)   // 2
console.log(null + 1)   // 1
```


在這些範例中，JavaScript 會嘗試猜測您的意思。有時候，它會將字串轉換為數字，或將布林值轉換為數字，或將字串轉換為字串。這可能會讓您的程式碼有意想不到的表現。


意識到 JavaScript 的弱類型系統是很重要的。當事情開始變得奇怪時，可能是因為意外的類型強制。


### `「嚴格使用」`


您可以啟用更嚴格的模式，將一些無聲的錯誤變成真正的錯誤，並阻止您使用一些較危險的語言功能。


若要啟用更嚴格的模式，請在檔案或函式的頂端加入這一行：


```javascript
"use strict"
```


例如：


```javascript
"use strict"
name = "Alice" // ReferenceError: name is not defined
```


如果沒有嚴格模式，JavaScript 會默默地建立一個叫做 `name` 的全局變數。但在嚴格模式下，這會變成真正的錯誤，幫助您及早發現 bug。


嚴格模式也會停用 JavaScript 的某些過時功能，讓您的程式碼更容易最佳化與維護。


## 價值與參考

<chapterId>bb898425-dc2f-5e5c-864b-0cb7a4a9aea9</chapterId>


JavaScript 會以不同的方式處理不同種類的值。


當您將某些值指定給變數時，這些值會被 ** 複製**。


當您將其他變數指定給新變數時，這些變數是 ** 共用的，所以如果您變更其中一個變數，另一個也會改變。


### 按值傳遞


當值被 **by 值** 傳送時，JavaScript 會對其進行 ** 複製。


因此，如果您變更其中一個，並不會影響另一個。


這種情況會發生在原始類型上，例如



- 號碼
- 字符串
- 布林值 (`真`和`假`)
- 空
- 未定義


讓我們來看一個例子：


```javascript
let a = 5
let b = a

b = 10

console.log(a) // 5
console.log(b) // 10
```


我們給了 `b` `a` 的值，但後來又將 `b` 改為 `10`。


由於數字是以值來傳遞的，JavaScript 將 `5` 複製到 `b` 中。在 `b` 中的 `5` 是獨立於在 `a` 中的原始 `5` 的，所以改變 `b` 的值對 `a` 沒有影響。


讓我們用字串來試試：


```javascript
let name1 = "Alice"
let name2 = name1

name2 = "Bob"

console.log(name1) // Alice
console.log(name2) // Bob
```


同樣地，變更 `name2` 並不會影響 `name1`，因為字串也是由值傳遞的。


當您將基元傳給函數時，也會發生同樣的事情：它會被複製。所以函數無法改變原始碼。


```javascript
function plusOne(x) {
x = x + 1
}

let number = 5

plusOne(number)

console.log(number) // 5
```


即使在函數 `1` 中加入了 `x`，原本的 `number` 並沒有改變。


那是因為只有一個 ** 副本** 傳入函式。


### 參考傳遞


物件是透過參考**傳送的。


這表示 JavaScript 並非複製它們，而只是傳遞一個 ** 參考**給它，如果您修改它，所有指向它的其他變數也會看到改變。


例如：


```javascript
const person1 = { name: "Alice" }
const person2 = person1

person2.name = "Bob"

console.log(person1.name) // Bob
console.log(person2.name) // Bob
```


`person1` 和 `person2` 都指向記憶體中的同一個物件。


因此，當我們變更「person2.name」時，我們也變更「person1.name」，因為他們都在看相同的東西。


陣列是物件，所以讓我們用陣列試試同樣的方法：


```javascript
const list1 = [1, 2, 3]
const list2 = list1

list2.push(4)

console.log(list1) // [1, 2, 3, 4]
console.log(list2) // [1, 2, 3, 4]
```


我們將 `4` 推到 `list2` 中，但 `list1` 也受到影響，因為它們都引用相同的陣列。


讓我們看看將物件傳給函數時會發生什麼事：


```javascript
function rename(user) {
user.name = "Charlie"
}

const person = { name: "Dana" }

rename(person)

console.log(person.name) // Charlie
```


函數改變了物件！那是因為它接收到原始 `person` 物件的 ** 參照。


它沒有得到副本。它取得原始物件的存取權，並藉此取得修改原始物件的能力。


記住這個區別是很重要的，否則我們的程式碼的行為可能與我們預期的不同。例如，我們在寫函數時可能期望它不會修改收到的參數，但後來發現它實際上是在修改參數（因為參數是物件，所以是以參照方式傳遞）。


## 使用函數

<chapterId>e0d277a8-c642-5af7-9e53-dee27c811967</chapterId>


您已經學習了如何在 JavaScript 中宣告和使用函數。但是 JavaScript 提供您更多的工具，讓您以強大的方式使用函數。


### 箭頭功能


箭頭函數是一種更簡短的函數寫法。我們不使用 `function` 關鍵字，而是使用箭頭 (`=>`)。


這裡有一個正常的功能：


```javascript
function greet(name) {
return `Hello, ${name}!`
}
```


箭頭版本看起來像這樣：


```javascript
const greet = (name) => {
return `Hello, ${name}!`
}
```


如果函數只有**行**，您可以跳過大括號並`return`：


```javascript
const greet = (name) => `Hello, ${name}!`
```


如果函數只有**個參數**，您甚至可以跳過參數周圍的括號：


```javascript
const greet = name => `Hello, ${name}!`
```


箭頭函數在現代 JavaScript 中非常普遍，因為它們允許以較少的模板來表達簡單的函數。


### 預設參數


有時候，如果沒有傳送參數，您希望函數有一個 ** 預設值**。


您可以這樣做：


```javascript
function sayHello(name = "friend") {
console.log(`Hello, ${name}!`)
}

sayHello("Alice") // Hello, Alice!
sayHello()        // Hello, friend!
```


當沒有傳入任何資料時，會使用預設值 `"friend"`。


### 展開參數 (`...`)


如果您的函數需要靈活的參數數目呢？


您可以使用**spread 運算符** (`...`)，將它們集合成一個陣列：


```javascript
function logAll(...items) {
console.log(items)
}

logAll(1, 2, 3) // [1, 2, 3]
logAll("a", "b") // ["a", "b"]
```


然後您可以使用循環來處理每個項目：


```javascript
function logEach(...items) {
for (const item of items) {
console.log(item)
}
}
```


當您不知道會傳入多少個參數時，擴展運算子很有用。


### 高階函數


**高階函數**是指符合下列條件的函數：



- 以另一個函數為輸入
- 和/或返回一個函數作為輸出


這裡有一個簡單的例子：


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


此處列印：


```
Hello, friend!
Hello, friend!
```


我們可以將箭頭函數傳給它：


```javascript
runTwice(
() => console.log("Hello!")
)
```


此處列印：


```
Hello!
Hello!
```


您也可以撰寫**返回**其他函數的函數：


```javascript
function makeGreeter(name) {
return () => console.log(`Hi, ${name}`)
}

const greetAlice = makeGreeter("Alice")
const greetBob = makeGreeter("Bob")

greetAlice() // Hi, Alice
greetBob() // Hi, Bob
```


`makeGreeter` 函數是一個建立其他函數的函數。它接收一個字串，並返回一個新函數，在其 `console.log` 呼叫中使用該字串。


這種模式非常強大，因為它允許您在函數中留下「洞」，讓您稍後可以用所需的行為來填補。


### map()`、`filter()`、`reduce()`。


JavaScript 提供了一些有用的內建方法來使用陣列。


這些方法以函數為參數，所以也是高階函數。


`map()`會將陣列中的每個項目轉換成其他項目。


範例：


```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map(x => x * 2)

console.log(doubled) // [2, 4, 6]
```


每個數字都加倍，結果是一個新的陣列。


`filter()`會從陣列中移除未通過測試的項目。


範例：


```javascript
const numbers = [1, 2, 3, 4, 5]
const numbersGreaterThanTwo = numbers.filter(x => x > 2)

console.log(numbersGreaterThanTwo) // [3, 4, 5]
```


只有 `x > 2` 條件回傳 `true` 的陣列項目才會被保留。


`reduce()` 用來將陣列中的所有項目合併為單一值。


範例：


```javascript
const numbers = [1, 2, 3, 4]
const total = numbers.reduce((current, next) => current + next)

console.log(total) // 10
```


`reduce` 遍歷陣列，在這個範例中，在 `1` 和 `2` 之間運用 `+` 運算子，然後在結果 `3` 和 `3` 之間運用 `+`運算子，然後在結果 `6` 和 `4` 之間運用 `+`運算子，直到得到所有陣列項目的總和 (也就是 10)。


您可以使用 `reduce()` 來做很多事情，例如總計、平均值或逐步建立新值。


這些方法 (`map`、`filter`、`reduce`) 是處理資料的強大工具，無須手動撰寫迴圈。


您甚至可以將它們結合成一連串的操作，就像這樣：


```javascript
const numbers = [1, 2, 3, 4, 5]

const result = numbers
.map(n => n * 2)        // Double each entry, obtain [2, 4, 6, 8, 10]
.filter(n => n > 3) // Keep only the entries bigger than 3, so you get [4, 6, 8, 10]
.reduce((n1, n2) => n1 + n2) // Adds them: 4 + 6 + 8 + 10 = 28

console.log(result) // 28
```


## 使用物件

<chapterId>7842aada-f009-5518-b8e3-1104e166a035</chapterId>


在本章中，我們將學習一些在 JavaScript 中使用物件的強大且稍為進階的工具。


### 私人物業


有時候，我們想要隱藏物件的某個屬性，使它無法被改變或從物件外部存取。JavaScript 提供了一個方法，讓我們在屬性名稱前使用 `#`。這會建立一個 **private** 屬性，只有在類別內部才能存取。


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


當您想要防止意外變更時，私有屬性很有幫助。


### `static` 屬性


有時候，您希望某個屬性屬於這個類別本身，而不是屬於您從這個類別所建立的每個物件。這就是 `static` 的用途。`static` 屬性包含在類別中，該類別的所有物件都會引用它。


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


這對於儲存共享資料和方法很有用，這些資料和方法適用於整組物件，而不只是其中一個。


### `get`和`set`。


在 JavaScript 中，`get` 和`set` 可以讓您建立 *look* 像一般變數的屬性，但實際上會在背景執行特殊的程式碼。


當您嘗試*讀取*一個屬性時，會執行一個 `get`ter 方法。它是透過在方法前寫入 `get` 來宣告的，方法的名稱是屬性的名稱。


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


即使 `fullName` 不是一般的屬性，我們也可以像使用一般的屬性一樣使用它，在幕後它會執行 `get` 函式來建立全名。


當您為一個屬性指定一個值時，`set`ter 方法會執行。它可以讓你控制當有人嘗試改變該值時會發生什麼。它的宣告方式是在方法前寫入 `set` 並加上屬性的名稱。


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


當我們執行 `user.fullName = "John Smith"`，它會執行 `set` 方法並更新 `firstName` 和 `lastName` 值。


因此，儘管看起來我們只是在設定一個簡單的變數，但實際上我們是在觸發更新其他屬性的邏輯。


## 鑰匙和值

<chapterId>01a397b8-c12a-5c39-82b3-6d9ebbb72a29</chapterId>


JavaScript 物件中的每個屬性都有一個 **key**（也稱為屬性名稱）和一個 **value**。


例如：


```javascript
const user = {
name: "Alice",
age: 30
}
```


在這個物件中，`"name 「和`」age 「是鍵，」Alice "和`30`是它們的值。


### 動態存取


有時候，您無法事先知道屬性的名稱...也許您是從使用者輸入取得，或是從變數讀取。您仍然可以使用**括號**存取它，例如 `myObject["keyName"]`。


```javascript
const user = {
name: "Alice",
age: 30
}

console.log(user["name"]) // Alice
```


我們將字串 `name` 傳給物件，以取得相對應的值。


我們可以將鍵儲存到變數中，然後使用它來存取相對應的值，例如


```javascript
const user = {
name: "Alice",
age: 30
}

const key = "name"

console.log(user[key]) // Alice
```


### 動態 Assignment


您也可以使用變數作為鍵來建立或更新物件屬性。


```javascript
const settings = {}

const key = "theme"
settings[key] = "dark"

console.log(settings) // { theme: "dark" }
```


當您想要逐步建立物件時，這會很有幫助。舉例來說


```javascript
const user = {}

user["username"] = "bananaFan123"
user["email"] = "banana@fruit.com"

console.log(user)
// { username: "bananaFan123", email: "banana@fruit.com" }
```


您甚至可以使用方括號在建立*物件時使用動態按鍵：


```javascript
const key = "language"
const config = {
[key]: "JavaScript"
}

console.log(config.language) // JavaScript
```


這稱為**計算的屬性**。方括號內的值會被求值，求值結果會被用作關鍵值。


### 符號類型


除了字串之外，JavaScript 也允許您使用稱為 `Symbol` 的特殊類型作為物件鍵。


讓我們從一個簡單的例子開始：


```javascript
const id = Symbol("userID")

const user = {
name: "Bob",
[id]: 12345
}

console.log(user[id]) // 12345
```


在這個範例中，`id` 是一個符號。它不是一個字串，但仍可作為一個 key。如果您嘗試記錄 `user` 到控制台，您會看到這個：


```javascript
console.log(user) // { name: 'Bob', [Symbol(userID)]: 12345 }
```


另一件重要的事：您建立的每個符號都是獨一無二的，即使它們是使用相同的字串建立的。


```javascript
const a = Symbol("label")
const b = Symbol("label")

console.log(a === b) // false
```


符號允許您定義不會與一般按鍵衝突的按鍵。例如，假設您有一個帶有 `name` 屬性的物件，但這個物件將來會被使用者以您無法預測的方式自訂，而使用者可能也會新增一個 `name` 屬性。如果原始的 `name` 屬性是以字串定義的，它會被新的覆蓋，就像這樣：


```javascript
const obj = {
name: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy' }
```


如果我們使用符號來代替：


```javascript
const name = Symbol("name")

const obj = {
[name]: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy', [Symbol(name)]: 'John' }
```


如您所見，原始的 `name` 屬性以某種方式保留。這在某些邊緣情況下可能很有用。


## 實用物件

<chapterId>516e74c8-2a11-545a-a4d1-c2cabb91a273</chapterId>


JavaScript 提供了一些有用的內建物件，可以幫助我們進行除錯和數學運算等工作。


### 其他「控制台」方法


您已經看過 `console.log`，它會將值列印到螢幕上。


在 `console` 物件上還有其他一些有用的方法，可以幫助您除錯程式。


#### `console.warn`


以黃色列印訊息（或在某些環境中以警告圖示列印）：


```javascript
console.warn("This is just a warning.")
```


#### `console.error`


以紅色列印訊息，就像錯誤一樣：


```javascript
console.error("Something went wrong!")
```


#### 控制台.表


將陣列或物件顯示為表格：


```javascript
const users = [
{ name: "Alice", age: 25 },
{ name: "Bob", age: 30 }
]

console.table(users)
```


這會列印出類似的表格：


```
┌─────────┬────────┬─────┐
│ (index) │  name  │ age │
├─────────┼────────┼─────┤
│    0    │ 'Alice'│  25 │
│    1    │ 'Bob'  │  30 │
└─────────┴────────┴─────┘
```


這對結構化資料的可視化非常有用。


#### `console.time` 和 `console.timeEnd`


您可以測量某件事需要花多少時間：


```javascript
console.time("timer")
for (let i = 0; i < 1000000; i++) {}
console.timeEnd("timer")
```


這會列印出類似的內容：


```
timer: 2.379ms
```


對於一些簡單的效能測試非常有用。


### 數學物件


JavaScript 提供了一個 `Math` 物件，裡面有許多有用的計算方法。


#### `Math.random()`數學隨機()


返回介於 0 (包含) 和 1 (不包含) 之間的隨機數：


```javascript
const r = Math.random()
console.log(r)
```


輸出範例：


```
0.4387429859
```


#### `Math.floor()`和`Math.ceil()`。



- `Math.floor(n)`向下**至最接近的整數
- Math.ceil(n)` 向上取整到最接近的整數。


```javascript
console.log(Math.floor(4.9)) // 4
console.log(Math.ceil(4.1))  // 5
```


#### `Math.round()`。


取整至最接近的整數：


```javascript
console.log(Math.round(4.4)) // 4
console.log(Math.round(4.6)) // 5
```


#### `Math.max()`和`Math.min()`。


返回數字清單中最大或最小的值：


```javascript
console.log(Math.max(5, 9, 3)) // 9
console.log(Math.min(5, 9, 3)) // 3
```


#### Math.pow()`和`Math.sqrt()`。



- `Math.pow(a,b)`給出`a`的幂`b`。
- `Math.sqrt(n)`給你`n`的平方根


```javascript
console.log(Math.pow(2, 3))   // 8
console.log(Math.sqrt(16))    // 4
```


# 進階 JavaScript

<partId>72c30671-ca20-5617-92a5-d5ba7aa38c93</partId>


## 其他收藏

<chapterId>a9a70c6d-a343-5a46-a383-e288bc2700e3</chapterId>


JavaScript 提供了一些特殊的集合類型，超越了一般的陣列和物件。這些類型包括 `Map` 和 `Set`。


它們可以幫助您儲存和管理數值群組，但它們的運作方式與您目前所看到的不同。


與物件一樣，`Map` 是 **key-value 對的集合。但它有一些重要的差異：



- 鍵可以是 ** 任何值**，而不只是字串。
- 保留項目順序。
- 它有內建的方法，讓工作更容易。


您可以像這樣建立新的地圖：


```javascript
const myMap = new Map()
```


這會建立一個空的 map。若要新增項目，請使用 `myMap.set(key,value)`：


```javascript
myMap.set("name", "Alice")
```


這會新增一個 key `"name「`，值為 `」Alice"`。


您也可以使用數字作為按鍵：


```javascript
myMap.set(42, "The answer")
```


甚至以物件作為鑰匙：


```javascript
const objKey = { id: 1 }
myMap.set(objKey, "Object as key")
```


這對一般物件是行不通的，因為一般物件只允許字串鍵。


若要 ** 取得值**，請使用 `myMap.get(key)`：


```javascript
console.log(myMap.get("name"))     // Alice
console.log(myMap.get(42))         // The answer
console.log(myMap.get(objKey))     // Object as key
```


若要 ** 檢查鍵是否存在**，請使用 `myMap.has(key)`：


```javascript
console.log(myMap.has("name")) // true
```


若要**移除關鍵**，請使用 `myMap.delete(key)`：


```javascript
myMap.delete("name")
```


若要 ** 清除整個地圖**，請使用 `myMap.clear()`：


```javascript
myMap.clear()
```


映射非常適合管理大型的值集合，因為存取大型映射上的值通常會比存取大型物件的效能好得多。


### 設定


一個 `Set` 是 ** 個值的集合 (沒有鍵)，其中每個值都必須是 ** 唯一的 **。這表示



- 相同的值不能有兩次
- 值會依您新增的順序儲存


您可以像這樣建立一個集合：


```javascript
const mySet = new Set()
```


若要 ** 新增值**，請使用 `mySet.add(value)`：


```javascript
mySet.add(1)
mySet.add(2)
mySet.add(2) // duplicate, will be ignored
```


即使我們嘗試加入 `2` 兩次，集合也只會保留一份。


若要 ** 檢查值是否在集**中，請使用 `mySet.has(value)`：


```javascript
console.log(mySet.has(2)) // true
console.log(mySet.has(3)) // false
```


若要**移除值**，請使用 `mySet.delete(value)`：


```javascript
mySet.delete(2)
```


若要 ** 清除所有內容**，請使用 `mySet.clear()`：


```javascript
mySet.clear()
```


當您想要保存唯一值的集合，而不需要手動檢查重複值時，`Set` 就很有用：


```javascript
const numberArray = [1, 2, 2, 3, 4, 4, 4, 5]

const numberSet = new Set(numberArray)

console.log(numberSet) // Set(5) { 1, 2, 3, 4, 5 }
```


設定」可幫您避免重複。


## 迭代器

<chapterId>61d24e5e-b7e4-541a-8322-778f61f26a72</chapterId>


JavaScript 中大多數可以迴圈的東西 (像是陣列、字串、映射、集合) 都是 ** 可iterable**：它們可以為其內容提供迭代器。


在 JavaScript 中，**iterator** 是一個特殊的物件，可以幫助您一次**一個項目。


### 物件」迭代器


與陣列或映射不同，一般物件 ** 並不能使用 `for...of` 進行迭代。如果您嘗試這樣做


```javascript
const user = {
name: "Alice",
age: 30
}

for (const value of user) {
console.log(value)
}
```


您會得到一個錯誤：


```
TypeError: user is not iterable
```


這是因為普通物件沒有內建的迭代器。但是 JavaScript 提供了其他工具讓您在物件上進行循環。


#### 物件.鍵()"。


您可以使用 `Object.keys(obj)` 取得物件的**keys**陣列，然後在陣列中循環：


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


此處列印：


```
name
age
```


#### 物件.值()`


若要循環**值**，請使用 `Object.values()`：


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


此處列印：


```
Alice
30
```


#### 物件.項目()`


如果您想要**鍵和值**，請使用 `Object.entries()`：


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


此處列印：


```
name is Alice
age is 30
```


即使物件無法直接迭代，這些方法仍能讓您以與 `for...of` 配合使用的方式，完全存取物件的內容。


但是，迭代器如何運作？


### 符號迭代器


所有 iterables 背後的秘密是一個特殊的 ** 符號**，稱為 `Symbol.iterator`。


這個符號是一個內建的關鍵，它告訴 JavaScript：「此物件可以迭代」。


當您呼叫`myIterable[Symbol.iterator]()`時，JavaScript 會回給您一個**iterator 物件**與`.next()`方法。


讓我們看看是什麼樣子：


```javascript
const colors = ["red", "green", "blue"]

const iterator = colors[Symbol.iterator]()

console.log(iterator.next()) // { value: 'red', done: false }
```


每次呼叫 `.next()` 都會得到下一個值。當它完成時，它會返回：


```javascript
{ value: undefined, done: true }
```


### 下一個


`.next()` 方法用來從序列中取得下一個項目。


每次您呼叫 `.next()`，都會得到一個有兩個 key 的物件：



- `value`：目前的項目
- `done`：一個布林值，告訴你迭代是否已經結束


我們來做一個完整的範例：


```javascript
const names = ["Lina", "Tom", "Eva"]      // declare an array
const iterator = names[Symbol.iterator]() // use the Symbol.iterator function to get an iterator for this array

let result = iterator.next()              // get the first element of the array

while (!result.done) {                    // repeat this loop until you reach the last element of the array, which is marked with { done: true }
console.log(result.value)               // print the value of each element
result = iterator.next()                // get the next element of the array
}
```


此處列印：


```
Lina
Tom
Eva
```


在引擎蓋下，`for...of` 環路是這樣運作的：它使用這個模式與 `.next()`。


您可以使用


```javascript
const names = ["Lina", "Tom", "Eva"]

for (const result of names) {
console.log(result)
}
```


### 製作可迭代的類別


您也可以透過新增 `[Symbol.iterator]()`方法，定義自己的 **iterable 類別**。


比方說，我們想要一個代表**數字範圍**的類別，例如從 1 到 5。


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


此處列印：


```
1
2
3
4
5
```


事情是這樣的



- 我們定義了一個類別 `Range
- 在類別中，我們實作了`[Symbol.iterator]()`，因此 JavaScript 知道如何遍歷它
- next()`方法會逐一回傳每個數字
- 當我們到達 `end` 時，它會回傳 `{ done: true }`


現在，我們的 `Range` 類別就像陣列一樣運作，我們可以在任何需要可迭代的循環中使用它。


### 產生器函數和 `yield


為了讓您更容易建立迭代器，JavaScript 提供了**產生器函數**，使用 `function*` 關鍵字（就是 `function` 後面加了一個 `*`）和 `yield` 關鍵字。


試試看


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


每個 `yield` 都會回傳一個值，並**暫停**函數，直到下一個 `.next()` 被呼叫。


您也可以使用 `for...of` 在產生器上循環：


```javascript
for (const num of numberGenerator()) {
console.log(num)
}
```


此處列印：


```
1
2
3
```


## 使用回撥的並發性

<chapterId>f3fc76ca-b3ef-54eb-a06e-501007002054</chapterId>


到現在為止，我們的程式碼都是**同步的**：一次一行，依序執行。但現實世界中有些事情需要時間，我們不希望整個程式在等待時暫停。


在本章中，我們將介紹一個新的概念： **並發**。它允許我們操控事情完成的順序。這在處理像是計時器、使用者輸入或從磁碟讀取檔案時非常有用。JavaScript 提供了不同的並發工具。


### `setTimeout`


函數 `setTimeout` 可讓您在經過一段時間後，**稍後執行函數。


範例：


```javascript
console.log("Start")

setTimeout(
() => console.log("This runs after 2 seconds"),
2000
)

console.log("End")
```


此處列印：


```
Start
End
This runs after 2 seconds
```


即使 `setTimeout` 出現在程式碼的中間，它也不會阻擋其他部分。相反地，它會安排函式在**後執行，然後馬上繼續。


`2000` 表示 2000 毫秒 (也就是 2 秒)。

以下是**Callbacks** 和 **Promise**部分的重寫，較為冗長且適合初學者，全程使用資料處理和清楚的註解：


### 回撥


**callback** 只是一個函數，我們將它給予另一個函數，以便稍後可以 **callback**。


讓我們看一個使用數字的真實例子。假設我們有一個數字列表，我們想要將每個數字加倍，然後應用一個函數 (回呼) 到結果「加倍」的陣列，但我們想要在一個小延遲之後執行，就像我們在等待一些緩慢的東西 (像是從網際網路載入資料)。


這裡有一個函式，可以使用 ** 回傳 *** 來做到這一點：


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


讓我們嘗試使用此功能：


```javascript
const input = [1, 2, 3]

doubleNumbers(input, function(result) {
console.log("Here is the doubled array:", result)
})
```


1 秒鐘之後，會列印出來：


```
Here is the doubled array: [ 2, 4, 6 ]
```


**What's happening here? **


1.我們傳入 `input` 作為我們要加倍的數字清單。

2.我們也會傳送一個 ** 回傳函數**，告訴程式在 ** 倍增之後要做什麼。

3.在 `doubleNumbers` 中，我們使用 `setTimeout` 模擬延遲，然後進行加倍。

4.一旦完成，我們就會在結果「加倍」陣列上呼叫 callback。


此技術可行，但假設您想在此之後執行更多步驟，例如篩選出小數字，然後將它們相加。您就必須像這樣**窩**更多的回呼：


```javascript
doubleNumbers(input, function(doubled) {
filterBigNumbers(doubled, function(filtered) {
sumNumbers(filtered, function(total) {
console.log("Final result:", total)
})
})
})
```


這是 Hard 的閱讀方式，而且很亂。這種風格被稱為 ** 回呼地獄 **，而這正是 `Promise` 被創造出來要修正的。


## 使用承諾的並發

<chapterId>30fddaca-729f-5c8d-bf86-8dfc7b3c9800</chapterId>


一個 `Promise` 是內建的 JavaScript 物件，代表一個將於未來**準備好的值。


我們可以建立這樣的 Promise：


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve("It worked!") // This means everything went OK
})
```


`new Promise()` 部分會建立承諾。


在它的內部，我們給它一個有兩個參數的函數：



- `resolve`，是我們在一切成功時呼叫的函數
- `reject`，是我們在出錯時呼叫的函數


在上面的範例中，我們只需立即解決，並傳送訊息 `「成功了！」`。


### `.then()`


要在承諾完成之後***做某些事情，我們使用 `.then()`：


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve(100) // This means everything went OK
})

promise.then(result => {
console.log("The result is:", result)
})
```


此處列印：


```
The result is: 100
```


我們傳給`resolve()`的值會以`result`的形式傳送到`.then()`內的函數。


讓我們使用 `setTimeout` 模擬一個需要 2 秒的任務：


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


這會等待 2 秒鐘，然後列印：


```
Done waiting!
```


### 拒絕()`


讓我們創造一個**失敗的承諾：


```javascript
const failingPromise = new Promise((resolve, reject) => {
reject("Something went wrong")
})
```


現在，如果我們在這上面使用 `.then()`，什麼都不會發生，因為 `.then()` 只會處理成功。


要處理錯誤，我們使用 `.catch()`：


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


這只列印


```
Caught an error: Something went wrong
```


傳給 `reject()` 的值會傳送到 `.catch()` 函式。


讓我們建立一個 Promise，它會依據某些條件，**有時工作，有時失敗。


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


現在我們可以呼叫此功能並處理兩種情況：


```javascript
checkNumber(5)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


此處列印：


```
Success: Positive number
```


如果我們試著用不同的號碼


```javascript
checkNumber(-1)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


它會列印：


```
Failure: Not a positive number
```


### 使用 `Promise`s 進行連鎖操作



我們可以使用 `Promise` 重寫先前的範例，這樣看起來會乾淨許多。


讓我們先寫一個新版本的加倍函數，但這一次，它會回傳一個 **promise** ：


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


現在我們可以使用 `.then()` 來告訴 JavaScript 如何處理結果：


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


此處列印：


```
Doubled numbers: [ 2, 4, 6 ]
```


到目前為止，這與 callback 版本的運作方式相同，但現在的程式碼更容易擴充與讀取。


比方說，我們想要增加更多步驟：


1.首先，將所有數字加倍

2.然後，移除小於 4 的數字

3.最後，把它們加在一起


我們可以為每個步驟寫一個函數，全部使用承諾：


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


現在我們可以像這樣將它們 ** 鎖在一起：


```javascript
const input = [1, 2, 3]

doubleNumbers(input)
.then(filterBigNumbers)
.then(sumNumbers)
.then(
result => console.log("Final result after all steps:", result)
)
```


此處列印：


```
Final result after all steps: 10
```


讓我們來瞭解一下它的作用：


1.`doubleNumbers` 將陣列加倍：`[2, 4, 6]`

2.刪除小於 3 的項目： `[4, 6]`

3.`sumNumbers`將餘下的數字相加：`4 + 6 = 10`

4.最後，我們列印結果。


每個 `.then()` 都會等待之前的步驟完成。因此，我們可以建立一個沒有嵌套的**動作鏈**。這讓程式碼更易於閱讀，也更容易除錯。


## 與 `async`/`await` 並發

<chapterId>6e93d29f-c8bf-5fd1-a9c9-4e794ee6cbd0</chapterId>


我們看到 `Promise` 鏈如何幫助我們避免回呼地獄，但當涉及許多步驟時，讀起來還是會有點 Hard。


這就是 `async` 和 `await` 的用處。它們讓我們寫出看起來像同步程式碼**的非同步程式碼，這讓我們更容易理解。


### 什麼是 `async`?


當您在函數前寫入關鍵字 `async` 時，JavaScript 會自動將函數的回傳值包裝成 Promise。


讓我們來看看一個基本的範例：


```javascript
async function greet() {
return "hello"
}
```


如果您呼叫此功能：


```javascript
const result = greet()
console.log(result)
```


你會看到這個


```
Promise { 'hello' }
```


即使您只是傳回一個字串，JavaScript 也會為您將它轉換成 Promise。您可以像這樣使用 `.then()` 取得實際的值：


```javascript
greet().then( result => console.log(result) ) // prints "hello"
```


或者您可以使用 `await`...


### 什麼是 `await`?


關鍵字 `await` 告訴 JavaScript：「等待這個 Promise 完成，然後給我結果」。


但您只能在同步函數**內使用 `await` 。


讓我們使用 `await` 重寫範例：


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


現在我們可以像使用一般值一樣使用結果。


現在讓我們來做一些更有用的事情。


### 使用 `await` 模擬延遲


我們將建立一個簡單的 `wait` 函式，以毫秒數作為參數，並在毫秒數後解決問題，而不做其他任何事情：


```javascript
function wait(ms) {
return new Promise(resolve => {
setTimeout(resolve, ms)
})
}
```


讓我們試著使用它：


```javascript
async function test() {
console.log("waiting 2 seconds...")
await wait(2000)
console.log("done waiting")
}

test()
```


此處列印：


```
waiting 2 seconds...
done waiting
```


您可以將 `await` 理解為 「在這裡暫停，直到承諾完成，然後繼續」。


這可讓您以**從上至下**的方式編寫程式碼，而不需要連續呼叫 `.then()`。


### 等待資料


讓我們重複之前的範例，先將數字加倍，然後過濾，再求和。但這次我們要使用 `async`/`await`。


我們將建立 3 個模擬等待的函數，並返回 Promises：


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


現在讓我們寫一個 `async` 函式來結合它們：


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


此處列印：


```
Final result: 10
```


這比鏈結 `.then()` 或巢狀回呼更容易閱讀。


它看起來像一般的步進式程式，但它的行為仍然是非同步的。


## 同步迭代器

<chapterId>438b037d-9931-56d7-9052-7b4470f3c75b</chapterId>


您已經學習了 **iterators** 以及我們如何使用 `for...of` 來迴圈數組和其他可迭代的東西。


但是，如果我們要迭代的資料需要時間才能到達呢？


有時候，我們想要迴圈**非同步傳送的東西，像是聊天中的訊息、檔案中的行數，或是慢速來源中的數字。


為此，JavaScript 提供了 **async 迭代器**。


### 同步產生器函數


建立同步迭代器的最簡單方法是使用 **async 產生函式**。


我們這樣寫：


```javascript
async function* generateNumbers() {
yield 1
yield 2
yield 3
}
```


這看起來就像一般的產生器，只是前面加上了 `async`。


現在我們可以使用 `for await...of` 來消耗數值：


```javascript
async function run() {
for await (const n of generateNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


這將列印出來：


```
Got number: 1
Got number: 2
Got number: 3
Done!
```


那麼和一般的發電機有什麼不同呢？


不同之處在：我們現在可以在產生器內部使用 `await` 。


讓我們再次製作延遲助手：


```javascript
function wait(ms) {
return new Promise(resolve => setTimeout(resolve, ms))
}
```


現在讓我們慢慢***數字：


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


試著使用它：


```javascript
async function run() {
for await (const n of generateSlowNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


### 為什麼要使用同步迭代器？


在下列情況下，同步迭代器非常有用：



- 數值不會一次到達。
- 您要一次處理一個，***隨它們來。
- 您正在使用 Promises，並希望以乾淨的方式進行循環。


舉例來說，如果您要從聊天伺服器逐一載入訊息，或是分塊下載大型檔案，async iterators 會提供您一種方法，讓您可以寫出可處理延遲資料的 `for` 環路。


### 符號.asyncIterator`符號.asyncIterator`迭代器


我們也可以在自訂類別中使用 async iterators。


下面是一個產生延遲數字的範例：


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


現在我們可以像以前一樣使用 `for await...of`：


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


這允許您建立可以異步迭代的物件


## Assignment 語法糖

<chapterId>8b1ba7d8-ecfd-5470-b86e-73cb84ccc8b7</chapterId>


「語法糖 」是指在不改變其功能的情況下，以更簡短或更容易的方式來寫某個東西。它只是用一種更好的方式來表達同樣的事情。


JavaScript 有一些內建的語法糖，可以讓我們寫出更乾淨、更簡短的宣告。在本章中，我們將探討如何根據條件來指定值、使用數學來更新變數、從陣列或物件中取得值，以及使用更簡單的語法來複製或合併它們。


### 三元運算符號


在 JavaScript 中，您可以使用**ternary 運算符**依據條件來指定值，這是`if...else`的簡短寫法。


而不是做：


```javascript
let message

if (isMorning) {
message = "Good morning"
} else {
message = "Hello"
}
```


您可以寫：


```javascript
const message = isMorning ? "Good morning" : "Hello"
```


這表示



- 如果 `isMorning` 為 true，則使用 `「早安」。
- 否則，使用 `"Hello"`


一般形式為：


```javascript
condition ? valueIfTrue : valueIfFalse
```


您也可以在其他表達式中使用：


```javascript
console.log(isSunny ? "Go outside" : "Stay in")
```


只需確保將其用於**簡單的**決策。如果邏輯很複雜，請堅持使用 `if...else`。


### 替代 Assignment 操作員


JavaScript 有 ** 捷徑運算符**，用來進行結合操作的指定。


我們來看看正常的方式：


```javascript
let counter = 1
counter = counter + 1
```


可簡化為


```javascript
let counter = 1
counter += 1 // same as counter = counter + 1
```


以下是最常見的幾種：


| Operator | Meaning             |
| -------- | ------------------- |
| `+=`     | add and assign      |
| `-=`     | subtract and assign |
| `*=`     | multiply and assign |
| `/=`     | divide and assign   |

範例：


```javascript
let score = 10
score += 5  // now score is 15
score *= 2  // now score is 30
score -= 10 // now score is 20
```


當您要使用變數本身的值更新變數時，這些變數很有用。


### 重組


**Destructuring** 可讓您從陣列或物件中取出值，並輕鬆將其儲存在變數中。


#### 陣列


假設您有：


```javascript
const colors = ["red", "green", "blue"]
```


而不是做：


```javascript
const first = colors[0]
const second = colors[1]
```


你可以做到


```javascript
const [first, second] = colors
```


此指派：



- 將 `first` 改為 `"red"。
- `第二`至`"Green"`


您也可以跳過數值：


```javascript
const [,, third] = colors
console.log(third) // blue
```


#### 物件


您也可以從物件中抽取數值：


```javascript
const user = { name: "Alice", age: 30 }

const { name, age } = user
console.log(name) // Alice
console.log(age)  // 30
```


如果屬性的名稱與您想要的變數不同，您可以重新命名：


```javascript
const { name: username } = user
console.log(username) // Alice
```


在處理物件和陣列時，Destructuring 會讓您的程式碼更乾淨。


### 展開語法


**spread語法**使用`...`來拆封或複製值。


#### 陣列


您可以複製或合併陣列：


```javascript
const a = [1, 2]
const b = [3, 4]

const both = [...a, ...b]
console.log(both) // [1, 2, 3, 4]
```


您也可以複製陣列：


```javascript
const original = [10, 20, 30]
const clone = [...original]
```


#### 物件


您也可以對物件做同樣的處理：


```javascript
const a = { x: 1 }
const b = { y: 2 }

const merged = { ...a, ...b }
console.log(merged) // { x: 1, y: 2 }
```


您也可以覆寫數值：


```javascript
const user = { name: "Alice", age: 30 }
const updated = { ...user, age: 31 }

console.log(updated) // { name: "Alice", age: 31 }
```


這在更新物件而不改變原始物件時非常有用。


# NodeJS

<partId>42fe4d49-dace-5135-bb9e-b9d75034fb2a</partId>


## 我們如何進入 Node

<chapterId>0da1d60c-06c9-54e6-a181-ae7dabf6e3b8</chapterId>


在本章中，我們將學習一點關於 JavaScript 和 NodeJS 的歷史背景。


歷史背景對軟體來說非常重要，因為我們經常使用其他人建立的工具，因此我們會受到他們過去所做決定的影響。


了解這些決策的原因，以及我們使用的工具是如何形成的，會讓我們對自己的所作所為不再感到困惑。


### JavaScript 的起源


JavaScript 一開始只是一種簡單的語言，旨在使網頁具有互動性。


1990 年代，Netscape Navigator 等網路瀏覽器加入了 JavaScript，讓開發人員可以編寫直接在瀏覽器中執行的程式碼。


最初的構想是以 Java 作為製作網站的核心語言 (使用所謂的「Java applets」)，而 JavaScript 只用於次要的東西。


核心設計是由 Brendan Eich 在不到兩週的時間內完成的，他當時還是 Netscape 的員工。


但相較於 Java，大多數人更喜歡使用 JavaScript，而且 Java applets 在當時也有一些安全問題，所以最後 Java 被排除在外，JavaScript 成為網頁開發的事實標準。


### V8 引擎


JavaScript 是一種解釋型語言，有別於 C 語言等編譯型語言。


以編譯語言寫成的程式碼會變成二進位，而二進位程式碼會直接送入電腦的 CPU。


![](assets/en/6.webp)


另一方面，Interpred 語言傾向於對使用者更友善，而且更接近人類的思考方式 (「高層級」)，而非機器的工作方式 (「低層級」)；因此它們通常會建立虛擬機器來執行其程式碼。


虛擬機器是一個特殊的程式，它位於您所寫的程式碼與 CPU 之間，並執行您的程式碼 (因為 CPU 無法理解)。


這可讓您在不太了解底層機器的情況下進行編程，但也會在效能方面付出代價，因為電腦並非只在執行您的程式，而是在執行一個執行您程式的程式（虛擬機器）。


隨著網路應用程式變得越來越複雜，人們要求改善 JavaScript 的效能。V8 引擎是 Google Chrome 瀏覽器中為 JavaScript 提供動力的解釋器。它由 Google 開發，並於 2008 年推出。


舊版的 JavaScript 引擎大多是傳統的虛擬機，而 V8 引擎則是 JIT (just-in-time) 編譯器。


JavaScript 程式碼會被送入 V8 引擎，而引擎會嘗試將其編譯成原生的二進位檔案。這可讓您擁有高階語言的體驗，而效能則稍微接近低階語言。這使得 JavaScript 成為世界上最快的高階語言，有點像「兩個世界最好的東西」。


### NodeJS 執行時


雖然 JavaScript 易於使用且執行速度相當快，但在 V8 發表之後，JavaScript 一直有一個很大的限制：它只能在瀏覽器中執行。


為什麼會有問題？


由於瀏覽器會執行從網際網路上數百萬個不同來源取得的程式碼，因此很容易入侵惡意軟體，所以瀏覽器與作業系統的其他部分是「沙盒」隔離的。


![](assets/en/7.webp)


JavaScript 無法存取電腦上的檔案系統和其他本機資源 (至少不像其他語言可以輕易存取)，因此對於使用 JavaScript 建立什麼樣的應用程式造成很大的限制。


2009 年，Ryan Dahl 發表了 NodeJS，這是一個運行時，讓您可以在瀏覽器之外，直接在電腦的原生作業系統上使用 V8 引擎。它還增加了許多對於撰寫伺服器端和命令列程式非常有用的功能。例如，您可以使用 NodeJS 建立網頁伺服器、讀寫檔案或建立自動執行任務的工具。


![](assets/en/8.webp)


在本課程中，到目前為止，我們已經探索了瀏覽器和 NodeJS 中的 JavaScript 功能。這些功能讓我們可以定義資料，並以抽象的方式來操作資料。在接下來的幾課中，我們將探討 NodeJS 特有的功能，讓我們可以與作業系統互動。


## 指令行參數

<chapterId>960d20f3-c424-5d51-a041-ef17d2e94b6d</chapterId>


NodeJS 除其他功能外，還允許我們建立 CLI（命令列介面）。


為此，我們需要一種接收命令列參數的方式，在 Node 中，這是使用內建的 `process` 物件來完成的。


### 處理


NodeJS 提供了一個稱為 `process` 的特殊物件，代表目前正在執行的程式。


您可以使用它來檢查環境、目前的工作目錄，甚至在需要時退出程式。


例如：


```javascript
console.log(process.platform)
```


這會列印作業系統平台，如 `win32`、`linux` 或 `darwin` (Mac)。


### `進程.argv`。


當您從終端執行 NodeJS 程式時，您可以在腳本名稱後傳入額外的文字 (參數)。這些會儲存在 `process.argv`。


例如，如果執行此指令：


```
node my_script.js alpha beta
```


您可以像這樣列印參數：


```javascript
console.log(process.argv)
```


輸出結果可能如下所示：


```
[ '/path/to/node', '/path/to/my_script.js', 'alpha', 'beta' ]
```


前兩項永遠是 Node 路徑和您的指令碼路徑。您傳給腳本的任何其他字元都會出現在這之後。


process.argv 「陣列可以像其他陣列一樣使用」.slice() "方法切分，所以要只得到傳過來的參數，您可以這樣做


```javascript
const args = process.argv.slice(2)

console.log(args)
```


存取使用者傳送的參數是開發命令列應用程式的基本。


## 模組

<chapterId>4e1651a5-65fd-50bc-b22a-40313d5659ca</chapterId>


JavaScript 執行時，例如 NodeJS，通常會將每個 JavaScript 檔案視為獨立的模組。


將模組視為一個方塊。這個方塊有自己的私有空間，因此您在其中宣告的變數和函式不會干擾到其他方塊中的程式碼。基本上，每個模組都有自己的範圍。


一個模組可以匯出它的一些內容，讓其他模組可以使用，它也可以匯入其他模組匯出的內容。JavaScript 允許您在模組間匯出和匯入內容，連接不同的檔案。


JavaScript 程式通常由多個模組組成，這些模組彼此相連。


為什麼要使用模組？透過將代碼分割成模組，您可以將程式組織成更小、更清楚且可重複使用的部分。每個模組可以只專注於一種任務，例如處理數學計算、處理檔案或格式化文字。


### CommonJS 模組


在 NodeJS 中，管理模組的最常見系統稱為 **CommonJS**。


在這個系統中，您可以使用 `module.exports` 從一個模組分享 (匯出) 程式碼，並使用 `require()` 在另一個檔案中載入 (匯入)。


若要讓某個東西在模組外可用，您可以將它指定給 `module.export`：


```javascript
const greeting = "Hello!"

module.exports = greeting
```


這裡，字串 `"Hello!"` 就是這個模組匯出的內容。


若要使用從其他檔案匯出的程式碼，您可以使用包含該檔案路徑的 `require()` 函式：


```javascript
const greeting = require("./greeting.js")

console.log(greeting)
```


此處列印：


```
Hello!
```


您可以匯出多個東西，方法是將它們捆綁在一個匿名物件中，例如


```javascript
const greeting1 = "hello"

const greeting2 = "hi"

module.exports = {
greeting1, greeting2
}
```


CommonJS 是 NodeJS 最初採用的模組系統。後來也加入了 ES 模組。


### ES 模組


NodeJS 也支援另一種模組，稱為 **ES 模組**，在網頁開發中很受歡迎。它們使用關鍵字 `export` 和 `import`。


ES 模組是為瀏覽器開發的，後來才加入 Node。如果您要使用它們，您可能必須使用 `.mjs` 作為檔案副檔名，而不是 `.js`，這取決於您使用的 Node 版本。


在一個名為 `greeting.mjs` 的檔案中，我們寫道


```javascript
export const greeting = "Hello!"
```

如您所見，我們直接匯出常數的定義位置


在另一個名為 `index.mjs` 的檔案中，我們匯入它：


```javascript
import { greeting } from "./greeting.mjs"

console.log(greeting)
```


您可以在檔案的不同部分輸出不同的聲明，例如


```javascript
export const num = 10

export function double (x) {
return x*2
}
```


### NodeJS 標準函式庫


NodeJS 還包含許多內建模組。這些是 NodeJS 提供的現成模組，可協助執行讀取檔案、使用作業系統或連線網路等常見任務。


例如，`os` 模組會提供您作業系統的相關資訊：


```javascript
const os = require("os")

console.log(os.platform())
```


您不需要安裝這些內建模組，它們是 NodeJS 隨附的。它們構成執行時的「標準函式庫」，大部分的 Node 應用程式都使用它們來做讀取檔案或透過網際網路通訊等事情。


接下來的章節將為您介紹一些有用的使用範例。


## fs」模組

<chapterId>911e953a-35ae-5ee7-bd74-372501c32e81</chapterId>


fs`模組（**檔案系統**的縮寫）是 NodeJS 標準函式庫的一部分。它允許您處理電腦上的檔案和目錄：您可以讀取檔案、寫入檔案、刪除檔案、重新命名檔案等。


要使用它，您首先需要在檔案頂端匯入它：


```javascript
const fs = require("fs")
```


### 同步 API


使用 `fs` 的最簡單方法是使用它的 **sync** 方法。


這些方法會阻塞程式，直到完成為止（因此下一行程式碼不會執行，直到操作完成為止）。


以下是同步讀取檔案的範例：


```javascript
const fs = require("fs")

const data = fs.readFileSync("example.txt", "utf8")

console.log(data)
```


如果在與腳本相同的目錄下有一個名為 `example.txt` 的檔案，這將會列印其內容。


您也可以同步寫入檔案：


```javascript
const fs = require("fs")

fs.writeFileSync("output.txt", "Hello from Node!")

console.log("File written!")
```


這會以文字建立（或覆寫）一個名為 `output.txt` 的檔案。


以下是您可以使用此 API 進行的一些常見操作：


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


Sync API 很簡單，適合小型腳本使用，但由於它會阻擋程式直到完成為止，如果您要處理大型檔案或伺服器，它可能會拖慢速度。


### 回呼異步 API


**callback API** 是非阻塞的：它可讓 NodeJS 在檔案操作發生時，繼續做其他事情。


它不會直接回傳結果，而是在操作完成時，會呼叫一個函數 (**回傳**)。


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


事情是這樣的



- `fs.readFile` 開始讀取 `example.txt`。
- NodeJS 不會等待，它會繼續執行您可能寫的其他程式碼。
- 當檔案讀取完成時，會執行回呼：



  - 如果有錯誤，`err` 包含錯誤內容。
  - 否則，`data` 會包含內容。


以下是寫入檔案的方式：


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


相同的想法：寫檔時程式不會停止。


您可以使用此 API 的一些範例：


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


回呼 API 更適合伺服器和大型任務，因為它不會阻塞程式，但如果您連鎖進行許多操作，巢狀回呼可能會變得亂七八糟。這就是新增基於承諾的 async API 的原因。


### Promise 异步 API


基於 Promise 的 API 是現代化的，與 `.then()` 和 `async/await` 搭配使用效果極佳。它可用於 `fs.promises`。


您需要匯入 `promises` 屬性：


```javascript
const fs = require("fs").promises
```


使用 `.then()`：


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


或者使用 `async/await` 更好：


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


寫入檔案：


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


API 的常見範例清單：


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


當您寫程式碼時，您經常需要使用其他人寫的程式碼；例如，可以幫助您處理日期、顏色、伺服器或幾乎任何其他東西的函式庫。


您可以使用 ** 套件管理器**，而不必手動下載和複製檔案。


套件管理員是一種工具，可



- 下載套件
- 記錄專案所需的套件
- 確保團隊中的每個人都擁有相同版本的套件


### 什麼是 NPM


在 NodeJS 世界中，最流行的套件管理器是 **NPM**，代表 *Node Package Manager*。


當您安裝 NodeJS 時，您會自動獲得 NPM。


您可以在終端機執行此指令來檢查是否有 NPM：


```
npm -v
```


這會列印出您所使用的 NPM 版本，例如：


```
10.2.1
```


### 建立套件


在 NodeJS 中，**package** 只是一個包含 `package.json` 檔案的目錄。


讓我們逐步建立一個。


1.為專案建立新資料夾：


```
mkdir my_project
cd my_project
```


2.執行此指令：


```
npm init
```


這會啟動互動設定，詢問您專案名稱、版本、描述等問題。


如果您不想回答所有問題，只想接受預設值，您可以使用：


```
npm init -y
```


執行之後，您會在資料夾中看到一個新檔案，名稱為：


```
package.json
```


### `package.json`。


`package.json` 檔案只是儲存專案相關元資料的 JSON 檔案。


這裡有一個範例：


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


幾個重要的領域：



- name`：套件名稱
- 版本」： 目前版本
- main`：入口點檔案 (如 `index.js`)
- scripts`：您可以執行的指令 (如 `npm start`)
- dependencies`：列出專案依賴的所有套件


### 安裝套件


假設您要使用某個叫做 `picocolors` 的套件來為您的終端機輸出加入顏色。


您可以執行下列步驟來安裝：


```
npm install picocolors
```


現在您可以在專案中使用它。製作一個 `index.js` 檔案，其中包含


```javascript
const pico = require('picocolors')

console.log(
pico.green("This text is green!")
)
```


並嘗試執行。終端機應該會列印出彩色版本的文字。


NPM 做了什麼？



- 它會下載套件，並將其儲存在稱為 `node_modules/` 的子資料夾中。
- 它在您的 `package.json` 中的 `dependencies` 下新增了一個項目
- 它更新了 `package-lock.json` 檔案


什麼是 `package-lock.json` ?


### `package-lock.json`。


NPM 會自動建立此檔案。


您可能會問，如果我們已經有了 `package.json`，為什麼還要另一個檔案？

原因就在這裡：



- `package.json`只說明您的專案需要哪個版本**範圍**的套件。

範例：


```json
"dependencies": {
"picocolors": "^1.1.0"
}
```


`^1.1.0` 表示「任何與 1.1.x 相容的版本」，所以很有彈性。



- `package-lock.json` **凍結**每個套件及其次依賴項目的精確版本，讓每個安裝您專案的人都能獲得完全相同的工作設定。


為什麼這很重要？


如果您在團隊中工作，或是將專案部署到伺服器上，或是將來再回到專案上，您都希望確保它仍能以相同的方式運作。

如果套件已經更新，而您在沒有鎖定檔案的情況下重新安裝，您可能會得到行為略有不同的版本。


將 `package-lock.json` 保留在專案中，NPM 將永遠安裝其中列出的精確版本，確保每個人都有相同的環境。


`package-lock.json` 將所有東西鎖定在一個非常特定的版本，讓專案在其他機器上更容易重複。


但如果您的套件需要被許多人使用，您可以選擇不提交，這樣 NPM 只會找到 `package.json` 檔案，並允許它自動安裝該檔案允許的最新版本。


但這些都是您日後應該擔心的事情，一旦您開始發佈自己的程式碼。目前，我們介紹 NPM 的基本原理只是為了讓您在專案中找到並使用其他開發人員所發佈的函式庫。



## NodeJS 中的網路

<chapterId>f2cabd8b-754b-5c97-8d6a-8412a9a184c7</chapterId>


NodeJS 常常被用作後端的語言：您可以將腳本變成伺服器，也可以使用它向其他伺服器提出請求。


在本章中，我們將介紹一些基本的網路功能，讓您可以做到這一點。


### 撷取()`


如果您希望您的程式從網站或 API 下載資料，您需要提出 **HTTP 請求**。


在現代版本的 NodeJS 中，您可以使用內建的「fetch()」函式。


以下是向 API 提出 GET 請求的範例：


```javascript
const response = await fetch("https://jsonplaceholder.typicode.com/posts/1")
const data = await response.text()

console.log(data)
```


當您執行此功能時，您會看到類似的內容：


```
{
"userId": 1,
"id": 1,
"title": "...",
"body": "..."
}
```


下面是發生的事情：


1.`fetch()` 接收 URL 並提出請求。

2.它會傳回一個**Promise**，解析為一個 `Response` 物件。

3.`response.text()` 以字串形式讀取回應正文。


但您得到的字串實際上是 JSON。那是什麼？


### JSON


使用 Web API 時，資料通常會以 **JSON**（JavaScript Object Notation 的縮寫）的形式傳送和接收。


JSON 只是一種文字格式，看起來很像 JavaScript 物件。舉例來說


```json
{
"name": "Alice",
"age": 30,
"likes": ["apples", "bananas"]
}
```


JavaScript 中的 `JSON` 物件是內建的工具，可用來處理這種資料格式。


您可以使用 `JSON.stringify()` 將 JavaScript 物件轉換成 JSON 字串：


```javascript
const user = { name: "Alice", age: 30 }

const jsonString = JSON.stringify(user)

console.log(jsonString)
```


此處列印：


```
{"name":"Alice","age":30}
```


您也可以使用 `JSON.parse()` 將 JSON 文字轉換回 JavaScript 物件：


```javascript
const jsonText = '{"name":"Bob","age":25}'

const obj = JSON.parse(jsonText)

console.log(obj)
```


此處列印：


```
{ name: 'Bob', age: 25 }
```


請小心：如果字串不是有效的 JSON，`JSON.parse()` 會產生錯誤。


```javascript
JSON.parse("not json") // ❌ Error!
```


因此請確定字串格式正確。


### `http`伺服器


NodeJS 可讓您在不安裝任何其他東西的情況下建立網頁伺服器。


您可以使用內建的 `http` 模組來處理客戶端的要求，並傳送回應。


這裡有一個非常基本的範例：


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


當您執行此指令碼並在瀏覽器中開啟 `http://localhost:3000` 時，您將會看到：


```
Hello from NodeJS server!
```


這就是代碼中發生的事情：


1.您從 Node 標準函式庫匯入了 `http` 伺服器。

2.`http.createServer()`會建立一個伺服器。您傳給`http.createServer()`一則回呼`(req, res) => {...}` 以在每次有人連線時執行。

3.您為回應指定了狀態代碼 200（表示操作成功）。您可以閱讀關於 http 狀態代碼的資訊 [這裡](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

3.`res.end()` 傳送回應並結束連線。

4.`server.listen(3000)`啟動連接埠 3000 上的伺服器。


您也可以檢查請求中的「req.url」和「req.method」，以處理不同的路徑或請求類型。


有路由的範例：


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


這些都是非常基本的範例。若要建立更進階的伺服器，大多數開發人員可能會下載現成的後端函式庫，例如 [express](https://www.npmjs.com/package/express)。


## 處理資料：緩衝區、事件、串流

<chapterId>8c9623f0-a604-51a4-8fe4-871c849d3e3b</chapterId>


在本章中，我們主要介紹三類物件：



- 表示二進位資料小塊的 `Buffer
- EventEmitter」，可用來追蹤異步進程中的某個步驟，並發出稱為「事件」的訊號。
- Stream「，它允許我們一次處理一個 」Buffer "的大部份資料，並透過發出事件來追蹤過程。


這些在專業的 NodeJS 程式碼中極為常見，因此即使您可能不會在第一個專案中使用這些程式碼，但對於何時需要與這些程式碼互動，有一個基本的了解也是好的。 其中包括


### 緩衝區


在 NodeJS 中，**buffer** 是一種用來處理二進位資料的物件類型。


您可以將緩衝區視為固定大小的原始位元組容器。


以下是如何從字串建立緩衝區：


```javascript
const buf = Buffer.from("hello")
console.log(buf)
```


這會列印出類似的內容：


```
<Buffer 68 65 6c 6c 6f>
```


這些數字 (`68`、`65`、`6c` 等) 是 `"hello"` 中字母的十六進位表示。


您可以像這樣將它轉換回字串：


```javascript
console.log(buf.toString())
```


此處列印：


```
hello
```


您也可以建立一個一定大小的緩衝區，裡面填滿零：


```javascript
const buf = Buffer.alloc(10)
console.log(buf)
```


這會列印出類似的內容：


```
<Buffer 00 00 00 00 00 00 00 00 00 00>
```


您可以寫入緩衝區：


```javascript
buf.write("abc")
console.log(buf)
```


而且您可以存取個別的位元組：


```javascript
console.log(buf[0]) // prints the ASCII number for 'a', which is 97
```


當您需要在非常低的層級操作資料時，緩衝區尤其有用。


### 活動


在 JavaScript 中，**事件**是發生在您程式中、您可以對其做出反應的事情。


例如：



- 檔案載入完成
- 計時器響起
- 使用者按一下按鈕
- 網路要求傳回資料


**事件**只是發生某件事情的信號，您可以寫程式碼來監聽這些事件，並對它們做出反應。


在 NodeJS 中，許多物件都可以發射事件。這些物件稱為 **EventEmitters**。


這裡有一個範例：


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


此處列印：


```
Hello! An event happened.
```


是這樣的


1.我們建立一個 `EventEmitter` 物件。

2.我們使用 `.on("greet「)`，告訴它每當`」greet"` 事件發生時，就執行回呼。

3.之後，我們使用 `.emit()` 觸發 `"greet"` 事件。

4.我們的回呼會被執行


您可以在傳送事件的同時傳送資料：


```javascript
emitter.on("greet",
(name) => console.log(`Hello, ${name}!`)
)

emitter.emit("greet", "Alice") // first argument is the type of event, second argument is the data we pass with this event
```


此處列印：


```
Hello, Alice!
```


您也可以為其他事件註冊監聽者：


```javascript
emitter.on("goodbye", () => {
console.log("Goodbye!")
})

emitter.emit("goodbye")
```


您可以隨心所欲地為某種類型的事件附加許多監聽器，也可以從同一個發射器發射許多不同類型的事件。


NodeJS 中的許多物件會發出事件，告訴程式的其他部分有事情正在發生。



### 什麼是溪流？


Streams 結合了緩衝區和事件來幫助我們處理資料。


當我們處理檔案、網路資料，甚至是較長的文字時，並不總是需要（或想要）一次過將所有資料載入記憶體。這可能會很慢，如果資料太大，甚至會導致程式當機。


相反地，我們可以在資料到達或被讀取時，一點一滴地處理資料，有點像是用吸管喝水，而不是一次喝下整杯水。這就是所謂的**流。


在 NodeJS 中，流是一種物件，可讓您一次**從一個來源讀取資料，或一次**將資料寫入一個目的地。


NodeJS 有四種主要的串流類型：



- 可讀**：您可以讀取資料的串流（就像讀取檔案一樣）
- Writable**: 可以寫入資料的串流 (就像寫入檔案一樣)
- 雙重**：既可讀又可寫的串流
- 轉換**：類似雙工串流，但可以在資料流動時改變（轉換）資料


### 可讀流


假設您有一個 `bigfile.txt` 檔案要處理。您可以使用 `fs` 模組建立一個可讀取的串流，逐段讀取檔案。


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


這裡會發生什麼？


1.`fs.createReadStream()` 建立一個可讀取的串流。

2.每當檔案的一部分準備好時，串流就會發佈一個 `data` 事件，並給我們一個資料「chunk」（一個 `Buffer`）。我們列印該資料塊。

3.當讀取整個檔案後，會觸發 `end` 事件。

4.如果有錯誤 (例如檔案不存在)，就會觸發 `error` 事件。


如此一來，您就可以讀取巨大的檔案，而不需要一次將它們全部載入記憶體。


如果我們希望資料以人類可讀的形式 (而非二進位) 傳達，我們可以指定串流的編碼：


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


現在程式碼會以人類可讀的形式列印檔案。


### 可寫串流


可寫串流可讓您將資料逐塊傳送至某處。


以下是使用串流寫入 `target.txt` 檔案的範例：


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


事情是這樣的


1.`fs.createWriteStream()`會建立一個可寫的串流。

2.我們使用 `.write()` 寫入一些文字。

3.完成後，我們呼叫 `.end()` 關閉串流。

4.當所有資料都寫完後，就會發佈 `finish` 事件。

5.如果出錯，就會觸發 `error` 事件。


就像可讀取串流一樣，可寫入串流也很適合大數據，因為它們不需要一次將所有東西都保存在記憶體中。


### 管道流


串流最酷的地方之一，就是您可以將它們**管道**在一起：將可讀的串流直接連接到可寫的串流。


```javascript
const fs = require("fs")

const readable = fs.createReadStream("bigfile.txt")
const writable = fs.createWriteStream("target.txt")

readable.pipe(writable)
```


這裡



- 可讀串流讀取自 `bigfile.txt`。
- 可寫串流會寫入 `copy.txt`。
- `.pipe()`直接將資料從可讀取的串流傳送到可寫入的串流。


### 雙重串流


雙重串流既可讀又可寫。其中一個例子就是網路套接字：您可以向它傳送資料，也可以從它接收資料。


下面是一個使用 `net` 模組的簡單範例：


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


在這個範例中：



- `socket` 物件是雙工串流。
- 您可以對其進行 `write()` 並監聽其中的 `data` 事件。


### 轉換串流


轉換串流是一種雙工串流，也會修改通過它的資料。


例如，您可以使用內建的 `zlib` 模組來壓縮或解壓資料。


以下是使用轉換串流壓縮檔案的方法：


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


並將其減壓回來：


```javascript
const readable = fs.createReadStream("bigfile.txt.gz")
const unzip = zlib.createGunzip()
const writable = fs.createWriteStream("bigfile.txt")

readable.pipe(unzip).pipe(writable)

writable.on("finish", () => {
console.log("File decompressed.")
})
```


變換串流對於壓縮、加密或在串流時變更檔案格式等工作非常有用。


### 背壓


有時候，可寫串流處理資料的速度很慢。如果我們不斷地將資料推送到可寫入裝置，速度超過它的處理能力，就可能會發生問題。這稱為 ** 回壓 **。


如果您在可寫的串流上呼叫 `.write()` 方法，它會回傳一個布林值，告知您串流是否需要暫停；您可能必須檢查它的回傳值，就像這樣：


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


這是一個手動將資料從可讀取裝置傳送至可寫入裝置，以及手動管理背壓的示例。


通常我們會使用`.pipe()`方法來傳送資料，這個方法會自動處理背壓。


因此，只有當您因為某些原因手動呼叫 `.write()`時，才需要擔心背壓的問題。


## 最後附註

<chapterId>139e2ab8-df67-525a-85f0-5a2fa5e478f2</chapterId>


所以，就是這樣，如果您跟著上課，現在應該可以用 NodeJS 寫一些簡單的程式了。


我建議這麼做：在學習了基礎知識之後，建立一些個人專案是練習並成為更好的程式設計師的最佳方式。


您建立什麼並不重要，重要的是您挑戰自己，用程式碼解決問題。


現代程式語言的功能強大得令人難以置信，而 NodeJS 可能是您在這個階段最值得嘗試的工具箱。


祝您好運！


# 最後部分


<partId>322624d8-6fbc-11f0-a67a-5b145f10afc1</partId>


## 評論與評分


<chapterId>3e93ac86-6fbc-11f0-8bae-9b2ed7914843</chapterId>

<isCourseReview>true</isCourseReview>

## 總結


<chapterId>49b3b9b2-6fbc-11f0-9870-5f5adcd3a0eb</chapterId>


<isCourseConclusion>true</isCourseConclusion>