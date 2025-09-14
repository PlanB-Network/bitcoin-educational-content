---
name: JavaScriptとNodeJSの基礎
goal: JavaScriptプログラミングの基礎とNodeJS開発を学び、実用的なアプリケーションやツールを構築します。
objectives: 

  - JavaScriptの基本構文、型、制御フローをマスターする
  - JavaScriptの関数、オブジェクト、クラスを理解する
  - エラー処理とデバッグのテクニックを学ぶ
  - NodeJSとそのエコシステムの紹介

---

# 開発の旅を始めよう


JavaScriptとNodeJSのコースへようこそ。


JavaScriptは、世界で最も人気のあるプログラミング言語です。モダンブラウザのスクリプト言語なので、JavaScriptを*いくつか*書かずにモダンなウェブアプリケーションを構築することは基本的に不可能です。また、NodeJSランタイムを使えば、ブラウザ以外でも使用することができ、コンピュータ上で直接実行するスクリプトやアプリケーションを作成することができます。


このコースは、プログラミングが全く初めての方、または他の言語を使ったことはあるがJavaScriptの仕組み、特にNodeJSの文脈を理解したい方を対象としています。


コース終了時には、JavaScriptで独自のプログラムを書き、NodeJS標準ライブラリを使用し、サードパーティパッケージをインストールして使用し、便利なツールを構築できるようになっているはずです。


+++
# 基本的なJavaScript

<partId>a617327c-e5a2-52ca-9380-c63f44623dd4</partId>


## セットアップ

<chapterId>ba05a290-1782-5268-87c9-62fd09590e05</chapterId>




JavaScriptプログラムは、JavaScriptランタイムによって実行されるコマンドを含む、（1つ以上の）テキストファイルのコレクションに過ぎない。


これらのテキストファイルの名前は通常、`my_script.js`、`my_program.js`などのように、`.js`ファイル拡張子で終わる。


これらのコマンドはJavaScriptで書かれている。


JavaScriptランタイムは、これらのファイルを実行する特別なプログラムである。


![](assets/en/1.webp)


### NodeJS ランタイム


最も一般的なJavaScriptランタイムはNodeJSである。


お使いのIDEにすでに含まれている場合もありますし、[公式サイト](https://nodejs.org/en/download)からダウンロードする必要があるかもしれません。


ダウンロードページでは、主要な3つのOS（オペレーティング・システム）すべてに対応した説明書を提供しています：Windows、Linux、MacOSです。お使いのOSでターミナルを開く方法を知っていることが前提です。


NodeJSは3つのOSすべてに対応しているので、あなたが書いたプログラムは（エッジケースを除けば）すべてのOSで実行できる。


つまり、たとえばWindows PC上でJavaScriptで簡単なビデオゲームを書いて、それを友人に渡して彼のMac上で実行させることができる。


![](assets/en/2.webp)














### 最初のプログラム（hello world）


伝統的に、プログラミング言語を学ぶ場合、最初に書くプログラムはコンソールに「hello world!


my_js_code/`というディレクトリを作成し、その中に`main.js`というファイルを作成する（ファイル名は任意）。


コードエディタでディレクトリを開いてください。


このコードをファイルに書き込んでください：


```javascript
console.log("hello world!")
```


ターミナルを開き、このコマンドを実行してプログラムを実行する：


```
node main.js
```


結果は次のようになるはずだ。


```
hello world!
```


### 何が起こったか


JavaScriptでは、すべてが「オブジェクト」である。


console`はプログラムのデバッグに使用するオブジェクトである。


console.log`は`console`で最もよく使われるメソッドである。引数を渡すと、その引数を表示します。


丸括弧 `()` を使って `console.log` に引数を渡す。


つまり、例えば「1000」という数字を表示したければ、次のように書くだけだ。


```javascript
console.log(1000)
```


そして、次のように実行する。


```
node main.js
```


をターミナルに入力する（以降、このコースでは、これがプログラムの実行方法であることを知っていることを前提とする）。


次のように印刷される。


```
1000
```


のように、複数のものを渡すことができます。


```javascript
console.log(16, 8, 1993)
```


これは次のように印刷される。


```
16 8 1993
```


## 変数とコメント

<chapterId>23050ab7-343b-5edf-9d37-e4e782e27ce0</chapterId>


プログラムは通常、データに対する操作を実行する。


変数とは、データを格納するための名前付きの箱のようなものだ。変数によってデータの一部を特定の名前と関連付けることができ、後でその名前を使ってデータを取り出すことができる。


### let`宣言


JavaScriptで変数を宣言するには、`let`キーワードを使います。


let`と書いた後、変数につけたい名前を書き、次に`=`記号、そして格納したい値を書く。


例えば、こうだ：


```javascript
let age = 25

console.log(age)
```


変数名（厳密には「識別子」と呼ばれる）には通常、アルファベット、アンダースコア（`_`）、ドル記号（`$`）、数字を含めることができるが、最初の文字を数字にすることはできない。


上のコードでは、`age`という変数を宣言し、値`25`を格納した。


そして、`console.log(age)`を使ってその値を表示した。


このコードを `node main.js` で実行すると、次のように出力される：


```
25
```


識別子は大文字と小文字を区別します。つまり、小文字と大文字は識別子の違いとしてカウントされます。


```javascript
let age = 25

let Age = 20

console.log(age)
```


は25と表示される。なぜなら、これらは2つのまったく別の変数とみなされるからだ！


文字列（テキスト）を変数に格納することもできる：


```javascript
let message = "hello again"

console.log(message)
```


これが印刷される：


```
hello again
```


先ほどと同じように、`console.log()`を使って変数に格納されている値を表示した。


さあ、両方一緒にやろう：


```javascript
let age = 25

let message = "hello again"

console.log(age)

console.log(message)
```


これを実行すると印刷される：


```
25
hello again
```

### 配置転換


let`で宣言された変数は、作成後に変更することができる。


これを再指定と呼ぶ。


```javascript
let score = 10

console.log(score)

score = 15

console.log(score)
```


まず、`10`を`score`に代入し、それを表示する。


次に、`score`の値を`15`に変更し、再度表示する。


出力はこうなる：


```
10
15
```


これは、得点が伸びるゲームのように、時間とともに値が変化する場合に非常に便利である。


ミックスにもう一つの変数を加えよう：


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


これが印刷される：


```
10
Alice
20
Bob
```


ご覧のように、`score`と`player`の両方が変更されている。


### const`宣言


しかし、たいていの場合、作成後に変数を変更させたくない。そのためには`const`を使う。


const`は「定数」の略である。一度 `const` 変数に値を代入すると、それを変更することはできない。


```javascript
const pi = 3.14
console.log(pi)
```


このプリント：


```
3.14
```


しかし、これをやろうとすると


```javascript
const pi = 3.14
console.log(pi)

pi = 99 // this line will cause an error
console.log(pi)
```


JavaScriptはこのようなエラーを出す：


```
TypeError: Assignment to constant variable.
```


これは `pi` が `const` を使って宣言されたからで、それ以降は値を変更できない。あなたはJavaScriptインタープリターに、その変数を変更させたくないことを伝えているのです。


これは、間違って変更してしまう可能性を減らせるので便利だ。プログラムが非常に大きくなり、何千行ものコードが存在するようになると、一度に起こっていることすべてに対応することは不可能になる（これが我々がコンピュータを使う主な理由であり、頭脳では計算できない複雑な処理を実行するためである）。


後で変更することが確実でない限り、値は常に`const`として宣言するのがベスト・プラクティスと考えられている。


### JavaScriptでのコメント


実行されないメモをコードに書きたいことがある。これをコメントと呼ぶ。


コメントは、プログラム実行時には無視されるが、自分自身や他の人に説明するのに便利である。


一行コメントを書くには `//` を使う。


```javascript
// This is a comment
const x = 10 // This is also a comment
console.log(x)
```


これでも印刷される：


```
10
```


コメントは人間が読むためにあるだけだ。


と `*/` を使って複数行のコメントを書くこともできます。


```javascript
/*
This is a multi-line comment.
It can span several lines.
*/
const y = 20
console.log(y)
```


これは次のように印刷される。


```
20
```


そして、そのコメントは無視される。


コメントを使ってコードに小さな注釈を加えることで、そのコードが何をしているのか、なぜそのように書かれているのかを思い出すことができる。また、他のプログラマーの理解を助けることもできる。


## 基本型：数値、文字列、ブーリアン

<chapterId>cfdb04f6-21a8-5143-bbf9-7aaae04962f0</chapterId>


JavaScriptでは、「型」は値がどのようなデータであるかを示す。


Javascriptにはいくつかの基本的な型があり、このセクションではそのいくつかを紹介する。


### 数字と算術演算


最初に紹介する型は `number` である。


JavaScriptの数値には整数（`5`など）や小数（`3.14`など）がある。


足し算、引き算、掛け算、割り算ができる。


基本的な例を挙げよう：


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


これが印刷される：


```
15
5
50
2
```


また、括弧 `()` を使って操作の順番を制御することもできる：


```javascript
const result = (2 + 3) * 4
console.log(result)
```


このプリント：


```
20
```


括弧がなければ、「2 + 3 * 4」となる：


```javascript
const result = 2 + 3 * 4
console.log(result)
```


それが印刷される：


```
14
```


通常の数学では、掛け算は足し算の前に起こるからだ。


### 文字列と補間


つ目に紹介するJavaScriptの型は `string` である。


文字列はテキストの断片です。一重引用符 `'...'` または二重引用符 `"..."` を使って作成することができます。


```javascript
const greeting = "hello"
const name = 'Bob'
console.log(greeting)
console.log(name)
```


このプリント：


```
hello
Bob
```


文字列を結合するには `+` 演算子を使う：


```javascript
const greeting = "hello"
const space = " "
const name = "Bob"

const fullGreeting = greeting + space + name
console.log(fullGreeting)
```


これが印刷される：


```
hello Bob
```


しかし、文字列を組み合わせるには、**文字列補間**と呼ばれるもっといい方法がある。バックティックを使って ``...`` という文字列を宣言し、その中に `${...}` を使って変数を書きます：


```javascript
const greeting = "hello"
const name = "Bob"

const fullGreeting = `${greeting} ${name}`
console.log(fullGreeting)
```


これも印刷される：


```
hello Bob
```


...}`の中にはどんな式でも入れることができる：


```javascript
const age = 30
console.log(`Next year, I will be ${age + 1} years old.`)
```


このプリント：


```
Next year, I will be 31 years old.
```


補間は最近のJavaScriptでは非常に一般的だ。


### ブール演算、比較演算、論理演算


三つ目に紹介する型は `boolean` である。これはブール論理を発明した数学者ジョージ・ブールにちなんで名付けられた。


ブール値は単純で、取り得る値は`true`と`false`の2つだけである。


変数に格納することができる：


```javascript
const theSkyIsBlue = true
const thisCourseIsBad = false

console.log(theSkyIsBlue)
console.log(thisCourseIsBad)
```


このプリント：


```
true
false
```


論理演算子を使ってブーリアンを組み合わせることができます：



- という意味であり、**両方の**値が `true` である場合にのみ `true` を返し、そうでない場合は `false` を返します。
- ||`は "or "を意味し、**少なくとも1つ**の値が`true`であれば`true`を返し、そうでなければ（両方とも偽であれば）`false`を返す。
- もしブール値が `true` ならば `false` を返し、その逆も同様である。


![](assets/en/3.webp)


例を挙げよう：


```javascript
const isSunny = true
const isWarm = true

console.log(isSunny && isWarm)  // true
console.log(isSunny || isWarm)  // true
console.log(!isSunny)           // false
```


JavaScriptでは `>`, `<`, `===`, `!==` といった演算子を使って値を比較することができます。これらの比較の結果は常にブール値になります。


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


また、Javascriptには「大きいか等しいか」を意味する`>=`と「小さいか等しいか」を意味する`<=`がある。


ブール演算子、比較演算子、論理演算子は、複雑な条件を宣言するプログラムではよく組み合わされます。例えば、「Eメールが到着していること、そして必要な画像が含まれていること、あるいはEメールの長さが10000文字以上であること」を確認するためです。これらは、プログラムのロジックを構築するために不可欠な構成要素であることが後でわかります。


## 配列、ヌル、未定義

<chapterId>7bf18183-5eae-53ed-83d2-b04982145d81</chapterId>


このセクションでは、JavaScriptプログラムでよく使われる3つの型について説明する：



- 配列**: 値のシーケンス
- undefined**：「何も割り当てられていない」ことを意味する特別な値。
- null**: 「意図的に空である」ことを意味する特別な値。


### 配列とインデックス・アクセス


配列**は、複数の値をリストとして保持できる型である。


角括弧 `[]` を使い、カンマで区切って配列を作成する。


基本的な例を挙げよう：


```javascript
const numbers = [10, 2, 88]
console.log(numbers)
```


このプリント：


```
[ 10, 2, 88 ]
```


配列には数値だけでなく何でも格納できる：


```javascript
const things = ["apple", 42, true]
console.log(things)
```


このプリント：


```
[ 'apple', 42, true ]
```


配列中の特定の項目にアクセスするには、**インデックス**を使用する。インデックスは、**0**から始まる項目の位置である。


つまり、この配列では


```javascript
const colors = ["red", "green", "blue"]
```



- colors[0]`は`"red"`である。
- colors[1]`は`"Green"`である。
- colors[2]`は`"blue"`である。


やってみよう：


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[0])
console.log(colors[1])
console.log(colors[2])
```


これが印刷される：


```
red
green
blue
```


配列の特定のインデックスに値を割り当てることができます。


```javascript
const colors = ["red", "green", "blue"]

colors[1] = "yellow"

console.log(colors)
```


これが印刷される：


```
[ 'red', 'yellow', 'blue' ]
```


たとえ変数に格納されているものであっても、インデックスとして任意の自然数を使用することができる。


```javascript

const i = 1
const colors = ["red", "green", "blue"]
console.log(colors[i])
```


これが印刷される：


```
green
```


しかし、存在しないインデックスにアクセスしようとすると、`undefined`となる：


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[3])
```


このプリント：


```
undefined
```


それは何だ？


### 未定義


特別な値`undefined`は「値が割り当てられていない」ことを意味する。


変数を作成したが値を与えなかった場合、その変数は `undefined` となる：


```javascript
const name
console.log(name)
```


このプリント：


```
undefined
```


name`に何も代入していないので、JavaScriptはデフォルトで`undefined`に設定する。


前に見たように、存在しない配列のインデックスにアクセスしたときにも `undefined` を得ることができる：


```javascript
const fruits = ["banana", "apple"]
console.log(fruits[2]) // There is no index 2
```


このプリント：


```
undefined
```


### null`とその扱い方


null`も特別な値である。これは "ここには何もない、わざとそうした "という意味である。


自動的に設定される `undefined` とは異なり、`null` は自分で設定するものである。


例えば、こうだ：


```javascript
const currentUser = null
console.log(currentUser)
```


このプリント：


```
null
```


なぜ`null`を使うのか？もしかしたら、後で値を期待するかもしれないが、まだ準備ができていないのかもしれない：


```javascript
let winner = null

// Later in the program:
winner = "Alice"

console.log(winner)
```


このプリント：


```
Alice
```


だから`null`は、例えば "ここには後で何かあるはずだが、今は空だ "と言いたいときに便利だ。


## ブロックと制御フロー

<chapterId>be985168-2636-5b0d-a48f-ac1bbfbff8a7</chapterId>


これまでのところ、私たちはほとんど、次々と実行されるコード行を書いてきた。


しかし、コードを書くときには、その実行順序をコントロールすることができる。


これを**コントロールフロー**と呼ぶ。


まずはブロックとスコープを理解することから始めよう。


### グローバル・スコープ


宣言する変数はすべて**スコープ**の中に存在する。


ブロックの外で変数を宣言した場合、その変数は**グローバル・スコープ**に存在する。


```javascript
const color = "blue"
console.log(color)
```


この変数 `color` はグローバルスコープにあるので、ファイルのどこからでもアクセスできる。


さらに行を増やせば


```javascript
const color = "blue"
console.log(color)

const size = "large"
console.log(color)
console.log(size)
```


color`と`size`はどちらもグローバル変数である。これらはファイル中どこでも利用できる。


しかし、ブロックの中では何が起こっているのか？


### ブロックとローカルスコープ


ブロック**は中括弧`{}`で囲まれたコードの一部です。


ブロック内で `let` または `const` で宣言された変数は、そのブロック内でのみ *** 存在する。


```javascript
{
const message = "inside block"
console.log(message)
}
```


このプリント：


```
inside block
```


しかし、これを試してみてほしい：


```javascript
{
const message = "inside block"
}
console.log(message) // Error!
```


JavaScriptはこのようなエラーを出す：


```
ReferenceError: message is not defined
```


それは`message`がブロックの中で宣言され、ブロックの外には存在しないからだ。


つまり、ブロックを使ってコードの一部を分離し、「ブロックの中で起きたことはブロックの中にとどまる」（ラスベガスのようなものだ）ことを確認できるのだ。


ブロック単位でコードを構成することで、`if`のような制御フロー構造を使ってプログラムの実行を構造化することもできる。


### if`, `else`


何かが真である場合にのみ**コードを実行したいことがある。そのための`if`文である。


```javascript
const myAge = 20

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


このプリント：


```
Am I an adult?
Yes I am!
```


ご覧のように、コードは`myAge`と`18`を比較している。

この場合、`>=`演算子は`true`を返すので、ブロックは実行される。

条件が `true` でない場合、ブロックは実行されない。


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


このプリント：


```
Am I an adult?
```


else`ブロックを追加すれば、逆のケースにも対応できる：


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
} else {
console.log("No, I am not.")
}
```


このプリント：


```
Am I an adult?
No, I am not.
```


if`ブロックも`else`ブロックもブロックのままなので、その中で宣言された変数は外には存在しない。


もし、あることが**真実ではない**と確信したいなら、どうすればいいのだろう？


さて、以前説明したように、JavaScriptにはブール値を反転させる "not "演算子がある。そのため、次のようにすることができる。


```javascript
const myAge = 17

const adult = myAge >= 18

console.log("Am I an adult?")

if (!adult) {
console.log("No, I am not.")
}
```

これはまだ印刷できる：


```
Am I an adult?
No, I am not.
```

演算子 `!` を使って `adult` 変数を反転させたからだ。


if (!adult) {...}`は "if not adult... "と読むべきである。


ブロック、論理演算子、比較演算子を使うことで、何かが起こるために「真」（または「偽」）でなければならない変数を定義して、プログラムの実行を構造化することができる。


### while`、`break`、`continue`。


while`ループは、ある条件が真である限りコードを繰り返す。


```javascript
let count = 0

while (count < 3) {
console.log("Count is", count)
count = count + 1
}
console.log("the loop is over!")
```


このプリント：


```
Count is 0
Count is 1
Count is 2
the loop is over!
```


count`が3になるとループは止まる。


break`を使えばループを早めに止めることができる：


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


このプリント：


```
0
1
2
```


なぜなら、数字が`3`になったとき、`if`ブロックが実行され、ループを止めるからだ。


continue`を使えば、ループの続きをスキップすることができる：


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


このプリント：


```
1
2
4
5
```


なぜなら、数字が`3`だったとき、`continue`は数字を表示する行をスキップさせたからだ。


### の......ために......`」。


配列があり、その中のすべての項目に何かをしたい場合は、`for ... of ....{...}`.


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const fruit of fruits) {
console.log(fruit)
}
```


このプリント：


```
apple
banana
cherry
```

このブロックは、配列の各要素に対して1回ずつ実行される。


ここで`fruit`は新しい変数で、配列の各アイテムの値を取り、ブロック内でそれを操作する。


### の...ために...`」。


for ... in` を使えば、配列のキー（インデックス）をループで調べることができる：


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(index)
}
```


このプリント：


```
0
1
2
```


インデックスを使って値を取得することもできる：


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(fruits[index])
}
```


これは、`for ... of`と同じものを表示する：


```
apple
banana
cherry
```


実際には、配列の場合は、`for ... of`を使ったほうがシンプルですっきりしている。


### ループ


特定の回数だけループさせたいこともあるし、一般的には、何かを追跡しながらブロックを繰り返すコードを書きたいこともある。

それが、境界のある`for`ループの良いところだ。

境界ループは通常、`(... ; ... ; ...)` のようにセミコロン `;` で区切られた3つの条件を取ります。


```javascript
for (let i = 0; i < 3; i = i + 1) {
console.log(i)
}
```


このプリント：


```
0
1
2
```


説明しよう：



- let i = 0`: ブロック内で使用する変数を宣言する（この場合は0から始まるカウンタ）。
- i < 3`: 実行するブロックの条件が `true` であることを宣言する ( この場合は "repeat while `i` is less than 3")
- i = i + 1`: ブロックの各実行後に実行されるコードを宣言する（この場合、「`i`を1増やす」）。


ご覧のように、バウンデッド・ループでは、コードの一部を繰り返し実行するために、より複雑な条件を宣言することができる。


### ブロックラベル


もっと複雑な制御フローを書かなければならない場合、JavaScriptでは**ラベル**を使ってブロックに名前をつけることができる。


例


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


このプリント：


```
Inside outer block
Inside inner block
Done
```


アウター・ブロックを完全に抜けるには、`break outer`を使った。


ループにラベルを付けることもできる。この例を見てみよう：


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

これは非常に退屈な例だったが、ラベルの（時折の）必要性が明確になったことを願う。


## 機能紹介

<chapterId>cc324715-09c2-5cf7-9e6f-47a6f16bc04d</chapterId>


プログラムが大きくなると、コードの一部を**再利用**したくなることがよくある。


そのために**関数**がある。関数**を使えば、いくつかのコードをまとめて名前をつけ、好きなときに実行できる。


### 関数宣言


関数を宣言するには `function` キーワードを使う。そして、その関数に名前をつけ、引数を `()` で囲み、実行するコードのブロック `{}` を指定します。引数を取らない関数から始めましょう：


```javascript
function sayHello () {console.log(`Hello!`) }
```


このコードは関数を**宣言**しているが、まだ**実行していない。


### 関数呼び出し


関数を実行する（あるいは「コール」する）には、その関数の名前に続けて括弧で囲む：


```javascript
function sayHello () {console.log(`Hello!`) }
sayHello()
```


このプリント：


```
Hello!
```


この関数は何度でも呼び出すことができる：


```javascript
function sayHello() {
console.log("Hello!")
}

sayHello()
sayHello()
```


このプリント：


```
Hello!
Hello!
```


関数内のコードは、それを呼び出したときだけ実行される。


### 関数の引数（関数への入力）


ある関数に何らかの入力を与えたいことがある。その場合は、括弧の中に**引数**を追加します。


例えば、こうだ：


```javascript
function sayHelloTo (friend) {
console.log(`Hello ${friend}!`)
}
```


さて、この関数は`friend`という**一つの引数**を取る。


関数を呼び出すときに、値を渡すことができる：


```javascript
sayHelloTo("Tommy")
```


このプリント：


```
Hello Tommy!
```


この関数は、別の名前で再度呼び出すことができる：


```javascript
sayHelloTo("Sam")
```


このプリント：


```
Hello Sam!
```


渡した値は、関数内の変数 `friend` に置き換わる。


複数の引数を使うこともできる：


```javascript
function greetTwoPeople(person1, person2) {
console.log(`Hello ${person1} and ${person2}!`)
}

greetTwoPeople("Lina", "Marco")
```


このプリント：


```
Hello Lina and Marco!
```


### return` （関数からの出力）


関数は**値を返す**こともできる。これは、関数が呼び出された場所に値を送り返すことを意味する。


簡単な例を挙げよう：


```javascript
function getNumber() {
return 42
}

const result = getNumber()
console.log(result)
```


このプリント：


```
42
```


関数 `getNumber()` は `42` を返し、それを `result` に格納して表示する。


自分で計算したものを返すこともできる：


```javascript
function add(a, b) {
return a + b
}

const result = add(2, 3)
console.log(result)
```


このプリント：


```
5
```


値が `return` されると、関数は停止する。そのブロック内の `return` 以降は何も起こらない。


```javascript
function saySomething() {

return "hi"

console.log("this never runs")

}

const message = saySomething()
console.log(message)
```


これは印刷のみ：


```
hi
```


なぜなら`"hi"`だけが返されるからだ。console.log("this never runs")`の行はスキップされる。


関数は小さなサブプログラムと考えることができる。それぞれの関数は入力を受け取り、それを処理し、出力を返します。


ある関数の戻り値を使おうとして、その関数が何も返さなかった場合はどうなるのか？


```javascript
function doesNothing () {}

const x = doesNothing()

console.log(x)
```

これは `undefined` と表示される。何も返さなかった関数の戻り値は `undefined` となる。


## オブジェクトとクラス

<chapterId>26689f25-8212-5057-8c21-3a05eee0ac75</chapterId>


JavaScriptはよくオブジェクト指向言語と呼ばれる。


つまり、値や関数を**オブジェクト**にグループ化することで、コードを整理するのに役立つということだ。


### オブジェクトとは何か？


オブジェクトはデータと、そのデータを操作する関数を含むことができる。関数をオブジェクトに入れるとき、私たちはそれを`メソッド`と呼ぶ。


最初のオブジェクトは `console` オブジェクトだ。このオブジェクトは画面に表示したり、プログラムをデバッグしたりするための複数のメソッドを持っている。


自分で印刷することもできる。


```javascript
console.log(console)
```


と表示され、その中に含まれるメソッドのリストが表示される。例えば、私のマシンでは


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


ご覧のように、デバッグに使えるメソッドがたくさんある！


Javascriptは、私たちが望むことを何でもできる新しいオブジェクトを作成するさまざまな方法を提供してくれる。


### オブジェクトの作成


オブジェクトを作成する最も簡単な方法は、**中括弧** `{}` を使ってデータと関数をグループ化することです。


これにより、**匿名オブジェクト**と呼ばれるものが作成される。


```javascript
const cat = {
name: "Whiskers",
age: 3
}
```


これはオブジェクトを作成し、`cat`という変数に格納する。


このオブジェクトには2つの**プロパティ**がある：



- name`に値`"Whiskers"`を指定する。
- 年齢`に値`3`を指定する。


印刷しよう：


```javascript
console.log(cat)
```


このプリント：


```
{ name: 'Whiskers', age: 3 }
```


objectName.propertyName`のように、ドットを使ってオブジェクトからプロパティを取り出すことができます：


```javascript
console.log(cat.name)  // prints "Whiskers"
console.log(cat.age)   // prints 3
```


プロパティを**変更**することもできます：


```javascript
cat.age = 4
console.log(cat.age)  // now it prints 4
```


ご覧のように、オブジェクトが`const`として定義されていても、そのオブジェクトが含むデータを変更することができます。


オブジェクトの場合、`const`はオブジェクト全体のオーバーライドを止めるだけである：


```javascript
const cat = {
name: "Whiskers",
age: 3
}

cat.age = 5 // this works

cat = 5 // this throws an error, you're trying to reassign the whole object

```


前述したように、オブジェクトは**関数**を保持することもでき、関数がオブジェクトの一部である場合、それを**メソッド**と呼ぶ。


例を挙げよう：


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log("Meow!")
}
}
```


このオブジェクトは持っている：



- name` プロパティ
- speak()`メソッド


メソッドを呼び出してみよう：


```javascript
cat.speak()
```


印刷される：


```
Meow!
```


メソッドは、キーワード `this` を通してオブジェクトが含むデータを使用することができる。

this`は現在のオブジェクトを指す。この例では、猫の名前を表示するために使われる：


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log(`${this.name} says meow!`)
}
}

cat.speak()
```


このプリント：


```
Whiskers says meow!
```


this`という単語は「このオブジェクト」を意味する...この場合は`cat`オブジェクトだ。



この種のオブジェクトは、素早くシンプルなものを作りたいときには最適です。しかし、同じ構造を持つ**多くのオブジェクト**を作成する必要がある場合は、もっと良い方法があります。


### クラスとコンストラクタ


クラス**は設計図のようなものだ。ある種のオブジェクトをどのように作成するかをJavaScriptに指示します。


クラスを定義するには、`class` キーワードを使い、その後にクラス名を続け、中括弧 `{}` で囲みます。


```javascript
class Dog {}
```


クラスは通常、慣例により大文字で始まる。


クラスの新しいオブジェクトは `new` を使って作ることができる：


```javascript
const hachiko = new Dog()
```


オブジェクトを印刷してみてください：

```javascript
class Dog {}

const myDog = new Dog()

console.log(myDog)
```


得られるもの


```
Dog {}
```


ご覧のようにDogクラスは空なので、`myDog`オブジェクトも空です。


コンストラクター`を追加することで、ドッグ・オブジェクトが持つべきプロパティを定義することができる。


コンストラクターは、新しいオブジェクトを作成（または「構築」）するときに実行される特別な関数です。


```javascript
class Dog {
constructor() { }
}
```


各ドッグに名前をつけたいので、関数に`name`パラメータを追加する：


```javascript
class Dog {
constructor(name) { }
}
```


そして、`this` を使って、`name` がビルドする `Dog` オブジェクトの `name` であることを宣言する。


```javascript
class Dog {
constructor(name) {
this.name = name
}}
```


さっそく使ってみよう：


```javascript
class Dog {
constructor(name) {
this.name = name
}
}

const myDog = new Dog("hachiko")

console.log(myDog)
```


これは次のように表示される：


```
Dog { name: 'hachiko' }
```


ご覧のように、`コンストラクタ`メソッドは `new Dog()`を実行したときにあなたがクラスに渡した引数を受け取り、それを使ってオブジェクトを構築します。


それを分解してみよう：



- class Dog` は Dog クラスを定義する。
- constructor(名前)`はオブジェクトが生成されるときに設定する。
- this.name=name`は新しいオブジェクトに値を格納する。
- new Dog("hachiko")` はクラスから新しいオブジェクトを作成し、`name` プロパティに `"hachiko"` を設定します。


では、クラスにメソッドを追加してみよう：


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


これは次のように印刷される。


```javascript
hachiko says barf!
```


同じことを2つの異なるDogのインスタンスに対して行うと、次のようになる。



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


次のようになる。


```
hachiko says barf!
bobby says barf!
```


speak()`メソッドは呼び出された `Dog` の `name` プロパティを使用する。


これは、クラスが存在する主な理由である。クラスによって、データを操作する一連のメソッドを定義し、同じデータの「形」を共有する複数のオブジェクトを作成することができる。


これらのオブジェクトの1つに対してメソッドを呼び出すと、そのメソッドは*その特定のオブジェクト*が保持しているデータを操作する。


### オブジェクトの形状を変更する


JavaScriptのオブジェクトは柔軟です。オブジェクトを作成した後でも、新しいプロパティを追加したり、既存のプロパティを削除したりすることができます。


許可はされているが、慎重に使うべきだ。


まずは単純な`Dog`クラスから始めよう：


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


この時点で、`myDog`は一つのプロパティしか持っていない：name`である。作成後も新しいプロパティを追加することができる：


```javascript
myDog.age = 5

console.log(myDog.age) // prints 5
```


新しいメソッドを追加することもできる：


```javascript
myDog.jump = function () {
console.log(`${this.name} jumps!`)
}

myDog.jump() // Fido jumps!
```


delete`キーワードを使えば、プロパティを削除することもできる。


```javascript
delete myDog.name

console.log(myDog.name) // prints 'undefined'
```


これはうまくいくが、ここで知っておくべき重要なことがある：V8のようなJavaScriptエンジン（Node.jsやChromeブラウザーで使われている）は、オブジェクトが常に同じプロパティを保持していると、より高速に動作する。オブジェクトが作成された後でプロパティを追加したり削除したりすると、動作が遅くなります。


小さなプログラムでは、これはあまり重要ではありません。しかし、大きなプロジェクト（ゲームなど）では、たとえすぐに使わなくても、最初からコンストラクタにすべてのプロパティを列挙しておいたほうがいい。こうすることでオブジェクトの形が安定し、コードの実行が速くなります。


例えば、この代わりに


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


あなたは次のことができる。


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


どちらのバージョンも機能しますが、パフォーマンス的には2番目の方が優れています。各オブジェクトが持つプロパティを前もってエンジンに伝えることで、それに応じて最適化することができる。


JavaScriptではオブジェクトの形を自由に変えることができるが、クラスを使う場合は、前もってオブジェクトの形を考えておくのがベストだ。



### extends`と`super()`による継承


他のクラスとほとんど同じで、いくつかの機能を追加したクラスを作りたいことがあります。


JavaScriptでは、オブジェクトの形状を変更したり（前述したようにパフォーマンス上最適とは言えない）、ゼロから新しいクラスを書き直したりする代わりに、**継承**というものを使うことができる。


継承とは、あるクラスが別のクラスを**拡張**できることを意味する。新しいクラスは古いクラスのすべてのプロパティとメソッドを取得し、必要なものを追加したり変更したりすることができます。


例えば、`Vehicle`という基本クラスがあるとしよう：


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


今度は`Car`クラスを作りたい。車は乗り物の一種であるが、何か特別な機能を持たせたり、発進時に別のメッセージを表示させたりしたい。すべてを書き換える代わりに、`extends` を使うことができる：


```javascript
class Car extends Vehicle {
start() {
console.log(`${this.brand} car is ready to drive!`)
}
}
```


Car` クラスは `Vehicle` のすべてを継承している。brand`プロパティを取得し、`start()`メソッドを独自のものに置き換えた。


![](assets/en/4.webp)


試してみよう：


```javascript
const myCar = new Car("Toyota")
myCar.start()
```


このプリント：


```
Toyota car is ready to drive!
```


Car`は独自のコンストラクタを持っていないが、`Vehicle`のコンストラクタを使用している。しかし、もし `Car` に独自のコンストラクタを書きたい場合は、`super()` を使って親のコンストラクタを呼び出す必要がある。


その方法はこうだ：


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



このプリント：


```
Toyota Corolla is ready to drive!
```


要約すると



- extends`は、あるクラスが別のクラスに基づいていることを意味する。
- super()`は、拡張するクラスのコンストラクタを呼び出すときに使う。
- 新しいクラスは、元のクラスのすべてのプロパティとメソッドを取得する。
- start()`のような）メソッドを**オーバーライド**して、違うことをさせることができる。


これは、（車、トラック、バイクのように）似たようなものがいくつかあり、コードを共有しながらも独自の動作をさせたい場合に役立つ。


### インスタンスオブ


instanceof`キーワードは、オブジェクトが特定のクラスから作成されたかどうかをチェックします。


例えば、`User`というクラスがあるとしよう：


```javascript
class User {
constructor(username) {
this.username = username
}
}

const regularUser = new User("julia123")

console.log(regularUser instanceof User)
```


このプリント：


```
true
```


regularUser` が `User` であることを確認する。それは `regularUser` が `User` クラスを使って作成されたからである。


継承された**クラスでも動作します。例えば、これは `User` を継承した `Admin` クラスです：


```javascript
class Admin extends User {}

const ourAdmin = new Admin("admin42")

console.log(ourAdmin instanceof Admin)   // true
console.log(ourAdmin instanceof User)    // true
```


どちらの行も `true` を返す。なぜなら `Admin` は `User` のサブクラスであり、`ourAdmin` は `Admin` でもあり `User` でもあるからである。


# 中級JavaScript

<partId>243f63ab-4f34-5c30-80cb-84ef46f6761d</partId>


## エラー処理

<chapterId>d0206bc5-d386-5e7f-9917-5803f392448c</chapterId>


より複雑なJavaScriptプログラムを書いていると、**エラー**に遭遇します。これは予期せぬ事態で、何かが間違ってしまうことです。ある変数が`未定義`なのにそれを使おうとしたとか、あるコードが間違った入力タイプを受け取ったとか。


これらのエラーを適切に処理しないと、プログラムがクラッシュしたり、予測できない動作をしたりする可能性があります。JavaScriptは、これらのエラーを検出・管理するツールを提供しているので、より優雅にエラーを処理することができます。


### 一般的なエラー: `undefined` の値へのアクセス


エラーの原因となる一般的な状況を紹介しよう：


```javascript
const user = undefined
console.log(user.name)
```


このコードを実行すると、次のようなエラーが出る：


```
TypeError: Cannot read properties of undefined (reading 'name')
```


これはJavaScriptがあなたに言っているのです：「name`プロパティを `undefined` な何かから取得しようとしました。そしておわかりのように、この種のエラーが起こると、それをキャッチして処理するコードを特別に書いていない限り、プログラムの実行は停止します。


### エラーをスローする


コードの中で手動で**エラーを発生**させたいことがある。その場合は `throw` キーワードを使います。


```javascript
throw new Error("This is a custom error message")
```


これは直ちにプログラムを停止し、印刷する：


```
Uncaught Error: This is a custom error message
```


throw`を使えば、プログラムのルールを強制することができる。例えば


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


この例ではゼロによる除算が認められていないため、2回目の呼び出しはエラーとなる。


### try...catch`でエラーをキャッチする


エラーが発生したときにプログラムをクラッシュさせたくない場合は、`try...catch`ブロックを使ってエラーをキャッチすることができる。これは、何かが失敗してもプログラムを**継続**させたい場合に便利です。


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log("Oops! Something went wrong.")
}
```


出力：


```
Oops! Something went wrong.
```


仕組みはこうだ：



- try`ブロック内のコードが最初に試行される。
- エラーが発生した場合、JavaScript は `try` ブロックの残りをスキップして、** `catch` ブロック** にジャンプする。
- catch`ブロックはエラーを受け取るので、それを表示したり、例えば次のように他の方法で処理することができます。


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log(`The message of the error was: "${error.message}"`)
}
```


出力：


```
The message of the error was: "Cannot read properties of undefined (reading 'name')"
```


### finally`ブロック


finally`ブロックを追加することもできる。これはエラーがあろうがなかろうが、**常に**実行されるコードである。


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


出力：


```
Trying something risky...
Caught the error: Uh oh!
This will run no matter what.
```


## 虫を避ける

<chapterId>db12d9f6-5806-514c-998e-0ae24805104e</chapterId>


この章では、JavaScriptでよくある落とし穴と、それを避ける方法を紹介する。


### 宣言なしの `var` と Assignment


古い JavaScript のコードでは、変数はしばしば `var` キーワードを使って宣言されていました。すでに学んだ `let` や `const` とは異なり、 `var` は混乱を招くような振る舞いをすることがあります。


例えば、こうだ：


```javascript
{
var message = "hello"
}
console.log(message)
```


message`はブロックの中だけに存在すると思うかもしれないが、そうではない。var`はブロックのスコープを無視し、関数やファイル全体で変数を利用できるようにする。


これは、特に大規模なプログラムでは、予期せぬ動作につながる可能性がある。このような理由から、最近のJavaScriptのコードでは、常に`var`の代わりに`let`または`const`を使うべきである。


さらに悪いことに、JavaScriptでは**まったく宣言せずに**変数に値を代入することができる：


```javascript
function greet() {
user = "Alice"
}
greet()
console.log(user) // prints "Alice"
```


これは宣言なしで新しいグローバル変数 `name` を作成する。これは無言で起こる可能性があり、特に単なるタイプミスであった場合は、Hardで追跡するバグにつながる可能性がある。変数は常に `let` か `const` を使って宣言してください。


### 弱い型システム


JavaScriptは弱い型付けをしており、必要に応じて値を自動的にある型から別の型に変換する。これは型強制と呼ばれ、便利ではあるが、しばしば混乱を招く結果につながる。


例えば、こうだ：


```javascript
console.log("5" + 1)    // "51"
console.log("5" - 1)    // 4
console.log(true + 1)   // 2
console.log(null + 1)   // 1
```


これらの例では、JavaScriptはあなたが何を言いたかったのかを推測しようとする。文字列を数値に、ブーリアンを数値に、文字列を文字列に変えてしまうこともある。そのため、コードが予期せぬ動作をすることがあります。


JavaScriptの弱い型付けシステムを意識することは重要だ。物事が奇妙に動き始めるとき、それは予期しない型の強制によるものかもしれない。


### use strict"`


より厳密なモードを有効にすることで、サイレントエラーを本物のエラーに変えたり、より危険な言語機能の使用を停止したりすることができる。


この厳しいモードを有効にするには、ファイルまたは関数の先頭に次の行を追加する：


```javascript
"use strict"
```


例えば、こうだ：


```javascript
"use strict"
name = "Alice" // ReferenceError: name is not defined
```


ストリクトモードがなければ、JavaScriptは黙って`name`というグローバル変数を作ってしまう。しかし、ストリクトモードを使えば、これは本当のエラーとなり、バグを早期に発見することができる。


また、ストリクトモードはJavaScriptのいくつかの古い機能を無効にし、コードの最適化と保守を容易にします。


## バリュー対リファレンス

<chapterId>bb898425-dc2f-5e5c-864b-0cb7a4a9aea9</chapterId>


JavaScriptは、異なる種類の値を異なる方法で扱います。


変数に代入すると、いくつかの値が**コピー**される。


他の変数は、新しい変数に代入するときに**共有**されるので、片方を変更するともう片方も変更される。


### パス・バイ・バリュー


値が**by value**で渡されると、JavaScriptはその**コピーを作成する。


だから、片方を変えてももう片方には影響しない。


これはプリミティブなタイプで起こる：



- 数字
- ストリングス
- 真偽値 (`true` と `false`)
- null`。
- 未定義


例を見てみよう：


```javascript
let a = 5
let b = a

b = 10

console.log(a) // 5
console.log(b) // 10
```


b`に`a`の値を与えたが、`b`を`10`に変更した。


数値は値で渡されるので、JavaScript は `5` を `b` にコピーした。b` の `5` は元の `a` の `5` から独立しているので、`b` の値を変更しても `a` には影響しない。


文字列で試してみよう：


```javascript
let name1 = "Alice"
let name2 = name1

name2 = "Bob"

console.log(name1) // Alice
console.log(name2) // Bob
```


文字列も値で渡されるため、`name2`を変更しても`name1`には影響しない。


プリミティブを関数に渡しても同じことが起こる。つまり、関数はオリジナルを変更できない。


```javascript
function plusOne(x) {
x = x + 1
}

let number = 5

plusOne(number)

console.log(number) // 5
```


関数内部で `x` に `1` が追加されても、元の `number` は変わらない。


コピー**だけが関数に渡されたからだ。


### 参照渡し


オブジェクトは**参照**で渡される。


つまり、JavaScriptはコピーする代わりに**参照**を渡すだけで、それを変更すると、それを指す他のすべての変数にも変更が反映されるということだ。


例えば、こうだ：


```javascript
const person1 = { name: "Alice" }
const person2 = person1

person2.name = "Bob"

console.log(person1.name) // Bob
console.log(person2.name) // Bob
```


person1`と`person2`はどちらもメモリ上の同じオブジェクトを指している。


つまり、`person2.name`を変更したとき、`person1.name`も変更したことになる。


配列はオブジェクトなので、同じことを配列でやってみよう：


```javascript
const list1 = [1, 2, 3]
const list2 = list1

list2.push(4)

console.log(list1) // [1, 2, 3, 4]
console.log(list2) // [1, 2, 3, 4]
```


4`を`list2`にプッシュしたが、`list1`も影響を受けた。


オブジェクトを関数に渡すとどうなるか見てみよう：


```javascript
function rename(user) {
user.name = "Charlie"
}

const person = { name: "Dana" }

rename(person)

console.log(person.name) // Charlie
```


関数はオブジェクトを変更した！それは、元の `person` オブジェクトへの **参照** を受け取ったからだ。


コピーを手に入れたのではない。元のオブジェクトにアクセスし、それを修正する能力を得たのだ。


この区別を覚えておくことは重要である。そうしないと、コードが期待したものと異なる動作をする可能性があるからだ。例えば、受け取った引数を変更しないことを想定して関数を書いたのに、後で実際に引数を変更していたことに気づくかもしれない（引数はオブジェクトであり、参照渡しだったからだ）。


## 関数を使う

<chapterId>e0d277a8-c642-5af7-9e53-dee27c811967</chapterId>


JavaScriptで関数を宣言し、使用する方法はすでに学びました。しかしJavaScriptには、関数をパワフルな方法で扱うためのより多くのツールが用意されています。


### アロー関数


アロー関数は関数を短く書く方法です。function`キーワードを使う代わりに、アロー（`=>`）を使います。


これが通常の機能だ：


```javascript
function greet(name) {
return `Hello, ${name}!`
}
```


矢印のバージョンはこうだ：


```javascript
const greet = (name) => {
return `Hello, ${name}!`
}
```


関数が**1行**しかない場合は、中括弧を省略して`return`することができます：


```javascript
const greet = (name) => `Hello, ${name}!`
```


関数のパラメータが**1つだけ**の場合は、パラメータを囲む括弧を省略することもできる：


```javascript
const greet = name => `Hello, ${name}!`
```


アロー関数は最近のJavaScriptでは非常によく使われている。


### デフォルト・パラメーター


引数が渡されない場合、関数に**デフォルト値**を持たせたいことがある。


こうすればいい：


```javascript
function sayHello(name = "friend") {
console.log(`Hello, ${name}!`)
}

sayHello("Alice") // Hello, Alice!
sayHello()        // Hello, friend!
```


何も渡されない場合、デフォルト値 `"friend"` が使われる。


### スプレッドパラメータ (`...`)


関数が柔軟な数の引数を取る場合は？


spread演算子**（`...`）を使って配列にまとめることができる：


```javascript
function logAll(...items) {
console.log(items)
}

logAll(1, 2, 3) // [1, 2, 3]
logAll("a", "b") // ["a", "b"]
```


そして、ループを使って各項目を処理することができる：


```javascript
function logEach(...items) {
for (const item of items) {
console.log(item)
}
}
```


スプレッド演算子は、渡される引数の数がわからない場合に便利である。


### 高次関数


高次関数**とは、次のような関数のことである：



- 別の関数を入力とする
- または関数を出力として返す


簡単な例を挙げよう：


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


このプリント：


```
Hello, friend!
Hello, friend!
```


アロー関数を渡すことができる：


```javascript
runTwice(
() => console.log("Hello!")
)
```


このプリント：


```
Hello!
Hello!
```


他の関数を**返す**関数も書くことができる：


```javascript
function makeGreeter(name) {
return () => console.log(`Hi, ${name}`)
}

const greetAlice = makeGreeter("Alice")
const greetBob = makeGreeter("Bob")

greetAlice() // Hi, Alice
greetBob() // Hi, Bob
```


makeGreeter`関数は他の関数をビルドする関数である。文字列を受け取り、その文字列を `console.log` の呼び出しに使用する新しい関数を返す。


この種のパターンは非常に強力で、関数に "穴 "を空けておき、後で必要な動作で埋めることができる。


### map()`, `filter()`, `reduce()`


JavaScriptには、配列で使える便利な組み込みメソッドがいくつかある。


これらのメソッドは関数を引数に取るので、高階関数でもある。


map()`は配列の各項目を別のものに変換する。


例


```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map(x => x * 2)

console.log(doubled) // [2, 4, 6]
```


各数値は2倍され、その結果が新しい配列となる。


filter()`は、テストにパスしないアイテムを配列から取り除く。


例


```javascript
const numbers = [1, 2, 3, 4, 5]
const numbersGreaterThanTwo = numbers.filter(x => x > 2)

console.log(numbersGreaterThanTwo) // [3, 4, 5]
```


x > 2` の条件が `true` を返す配列項目だけが保持される。


reduce()`は、配列のすべての項目を1つの値にまとめるために使われる。


例


```javascript
const numbers = [1, 2, 3, 4]
const total = numbers.reduce((current, next) => current + next)

console.log(total) // 10
```


reduce`は配列を調べて、この例では `+` 演算子を `1` と `2` の間に適用し、次に結果の `3` と `3` の間に適用し、次に結果の `6` と `4` の間に適用する。


reduce()`は、合計や平均、新しい値の段階的な構築など、さまざまなことに使うことができる。


これらのメソッド（`map`、`filter`、`reduce`）は、手動でループを書くことなくデータを処理するための強力なツールである。


このように、連鎖的に組み合わせることもできる：


```javascript
const numbers = [1, 2, 3, 4, 5]

const result = numbers
.map(n => n * 2)        // Double each entry, obtain [2, 4, 6, 8, 10]
.filter(n => n > 3) // Keep only the entries bigger than 3, so you get [4, 6, 8, 10]
.reduce((n1, n2) => n1 + n2) // Adds them: 4 + 6 + 8 + 10 = 28

console.log(result) // 28
```


## オブジェクトを扱う

<chapterId>7842aada-f009-5518-b8e3-1104e166a035</chapterId>


この章では、JavaScriptでオブジェクトを扱うための、強力で少し高度なツールを学びます。


### 私有地


オブジェクトのプロパティを非表示にして、オブジェクトの外部から変更したりアクセスしたりできないようにしたいことがあります。JavaScriptでは、プロパティ名の前に`#`をつけることで、これを実現することができます。これにより、クラス内部からのみアクセス可能な**private**プロパティが作成されます。


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


プライベート・プロパティは、偶発的な変更を防ぎたい場合に便利です。


### 静的なプロパティ


あるプロパティを、そのクラスから作成する各オブジェクトではなく、クラス自体に帰属させたいことがあります。それが `static` です。static` プロパティはクラスに含まれ、そのクラスのすべてのオブジェクトがそのプロパティを参照します。


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


これは、1つのオブジェクトだけでなく、オブジェクトのグループ全体に適用される共有データやメソッドを格納するのに便利である。


### get`と`set`。


JavaScriptでは、`get`と`set`によって、見た目は普通の変数だが、実際にはバックグラウンドで特別なコードを実行するプロパティを作ることができる。


get`terメソッドはプロパティを*読もうとするときに実行される。get`ter メソッドはプロパティの名前を持つメソッドの前に `get` と書くことで宣言される。


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


fullName`は通常のプロパティではないが、通常のプロパティのように使用することができる。


set`ter メソッドは、プロパティに値を割り当てるときに実行されます。このメソッドを使うと、誰かがその値を変更しようとしたときに何が起こるかを制御することができます。set`ter メソッドは、プロパティの名前を持つメソッドの前に `set` と書くことで宣言します。


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


user.fullName = "John Smith"` とすると、`set` メソッドが実行され、`firstName` と `lastName` の値が更新される。


つまり、単純な変数を設定しているように見えても、実際には他のプロパティを更新するロジックをトリガーしているのだ。


## キーとバリュー

<chapterId>01a397b8-c12a-5c39-82b3-6d9ebbb72a29</chapterId>


JavaScriptオブジェクトのすべてのプロパティには、**キー**（プロパティ名とも呼ばれる）と**値**があります。


例えば、こうだ：


```javascript
const user = {
name: "Alice",
age: 30
}
```


このオブジェクトでは、`"name"`と`"age"`がキーで、"Alice "と`30`がその値である。


### ダイナミック・アクセス


ユーザーの入力から取得したり、変数から読み取ったりする場合など、プロパティの名前が事前にわからないことがあります。その場合でも、`myObject["keyName"]`のように**ブラケット記法**を使ってアクセスすることができます。


```javascript
const user = {
name: "Alice",
age: 30
}

console.log(user["name"]) // Alice
```


対応する値を得るために、文字列 `name` をオブジェクトに渡した。


キーを変数に保存し、それを使って後で対応する値にアクセスすることができる。


```javascript
const user = {
name: "Alice",
age: 30
}

const key = "name"

console.log(user[key]) // Alice
```


### ダイナミックAssignment


また、変数をキーとしてオブジェクト・プロパティを作成または更新することもできます。


```javascript
const settings = {}

const key = "theme"
settings[key] = "dark"

console.log(settings) // { theme: "dark" }
```


これは、オブジェクトを段階的に作りたいときに役立つ。例えば


```javascript
const user = {}

user["username"] = "bananaFan123"
user["email"] = "banana@fruit.com"

console.log(user)
// { username: "bananaFan123", email: "banana@fruit.com" }
```


角括弧を使ってオブジェクトを作成*するときに、ダイナミック・キーを使うこともできる：


```javascript
const key = "language"
const config = {
[key]: "JavaScript"
}

console.log(config.language) // JavaScript
```


これは**計算プロパティ**と呼ばれる。角括弧内の値が評価され、その結果がキーとして使用されます。


### シンボル`タイプ


文字列に加えて、JavaScriptでは`Symbol`という特別な型をオブジェクトのキーとして使うことができる。


簡単な例から始めよう：


```javascript
const id = Symbol("userID")

const user = {
name: "Bob",
[id]: 12345
}

console.log(user[id]) // 12345
```


この例では、`id`はSymbolである。文字列ではないが、キーとして機能する。user`をコンソールに記録しようとすると、このようになる：


```javascript
console.log(user) // { name: 'Bob', [Symbol(userID)]: 12345 }
```


もうひとつ重要なことは、たとえ同じ文字列を使って作ったとしても、作成したシンボルはすべて一意であるということだ。


```javascript
const a = Symbol("label")
const b = Symbol("label")

console.log(a === b) // false
```


シンボルを使うことで、通常のキーと衝突しないキーを定義することができます。例えば、あるオブジェクトに `name` プロパティを定義したとします。しかし、そのオブジェクトは将来ユーザーによってカスタマイズ可能になり、そのユーザーは `name` プロパティも追加するかもしれません。元の `name` プロパティが文字列で定義されていた場合、次のように新しいプロパティで上書きされます：


```javascript
const obj = {
name: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy' }
```


代わりにシンボルを使う：


```javascript
const name = Symbol("name")

const obj = {
[name]: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy', [Symbol(name)]: 'John' }
```


ご覧のように、元の`name`プロパティはこの方法で何とか保持される。これは特定のエッジケースにおいて有用である。


## ユーティリティ・オブジェクト

<chapterId>516e74c8-2a11-545a-a4d1-c2cabb91a273</chapterId>


JavaScriptには、デバッグや数学の演算などに役立つ便利な組み込みオブジェクトがいくつかある。


### その他の `console` メソッド


画面に値を表示する`console.log`はすでに見ただろう。


console`オブジェクトには、プログラムのデバッグに役立つメソッドが他にもいくつかあります。


#### `console.warn`


メッセージを黄色（環境によっては警告アイコン）で表示する：


```javascript
console.warn("This is just a warning.")
```


#### コンソール.エラー


エラーのようなメッセージを赤で表示する：


```javascript
console.error("Something went wrong!")
```


#### `console.table`


配列やオブジェクトを表として表示する：


```javascript
const users = [
{ name: "Alice", age: 25 },
{ name: "Bob", age: 30 }
]

console.table(users)
```


というような表が印刷される：


```
┌─────────┬────────┬─────┐
│ (index) │  name  │ age │
├─────────┼────────┼─────┤
│    0    │ 'Alice'│  25 │
│    1    │ 'Bob'  │  30 │
└─────────┴────────┴─────┘
```


これは構造化データを視覚化するのに便利である。


#### console.time`と`console.timeEnd`。


何かをするのにかかる時間を測ることができる：


```javascript
console.time("timer")
for (let i = 0; i < 1000000; i++) {}
console.timeEnd("timer")
```


これは次のように表示される：


```
timer: 2.379ms
```


簡単なパフォーマンステストに役立つ。


### Math`オブジェクト


JavaScriptには、計算を行うための便利なメソッドを備えた`Math`オブジェクトが用意されている。


#### `Math.random()`


0（包含）～1（排他的）の乱数を返します：


```javascript
const r = Math.random()
console.log(r)
```


出力例：


```
0.4387429859
```


#### Math.floor()`と `Math.ceil()`。



- Math.floor(n)`は最も近い整数に**切り捨て**る。
- Math.ceil(n)`は**最も近い整数に**切り上げる


```javascript
console.log(Math.floor(4.9)) // 4
console.log(Math.ceil(4.1))  // 5
```


#### `Math.round()`


最も近い整数に丸める：


```javascript
console.log(Math.round(4.4)) // 4
console.log(Math.round(4.6)) // 5
```


#### Math.max()`と `Math.min()`。


Number関数は、数値のリストから最大または最小の値を返します：


```javascript
console.log(Math.max(5, 9, 3)) // 9
console.log(Math.min(5, 9, 3)) // 3
```


#### Math.pow()`と`Math.sqrt()`。



- Math.pow(a,b)`は`a`の`b`乗`を与える。
- Math.sqrt(n)`は `n` の平方根を与える。


```javascript
console.log(Math.pow(2, 3))   // 8
console.log(Math.sqrt(16))    // 4
```


# 上級JavaScript

<partId>72c30671-ca20-5617-92a5-d5ba7aa38c93</partId>


## その他のコレクション

<chapterId>a9a70c6d-a343-5a46-a383-e288bc2700e3</chapterId>


JavaScriptには、通常の配列やオブジェクトを超えた特別なコレクション型がいくつかある。これには `Map` と `Set` がある。


これらは、値のグループを保存・管理するのに役立つが、これまで見てきたものとは動作が異なる。


Map`は**キーと値のペア**のコレクションで、オブジェクトと同じです。しかし、いくつかの重要な違いがある：



- キーは文字列だけでなく、**あらゆる値**を指定できる。
- 項目の順序は保持される。
- より簡単に作業するためのメソッドが組み込まれている。


このように新しい地図を作成する：


```javascript
const myMap = new Map()
```


これで空のマップが作成される。エントリーを追加するには `myMap.set(key, value)` を使う：


```javascript
myMap.set("name", "Alice")
```


これはキー`"name"`と値`"Alice"`を追加する。


数字をキーにすることもできる：


```javascript
myMap.set(42, "The answer")
```


さらに、オブジェクトをキーにすることもできる：


```javascript
const objKey = { id: 1 }
myMap.set(objKey, "Object as key")
```


これは、文字列キーしか使えない通常のオブジェクトでは機能しない。


値を取得するには**、`myMap.get(key)`を使う：


```javascript
console.log(myMap.get("name"))     // Alice
console.log(myMap.get(42))         // The answer
console.log(myMap.get(objKey))     // Object as key
```


キーが存在するかどうかをチェックするには**、`myMap.has(key)`を使う：


```javascript
console.log(myMap.has("name")) // true
```


キーを**削除**するには、`myMap.delete(key)`を使う：


```javascript
myMap.delete("name")
```


マップ全体をクリアするには**、`myMap.clear()`を使う：


```javascript
myMap.clear()
```


マップは、大きな値のコレクションを管理するのに適しています。なぜなら、大きなマップ上の値にアクセスすると、大きなオブジェクトにアクセスするよりもはるかに優れたパフォーマンスが得られるからです。


### セット


セット`は**値のみ**（キーはない）のコレクションであり、各値は**一意でなければならない**。つまり



- 同じ値を2度持つことはできない
- 値は追加した順に保存されます。


このようなセットを作る：


```javascript
const mySet = new Set()
```


値を追加するには**、`mySet.add(value)`を使う：


```javascript
mySet.add(1)
mySet.add(2)
mySet.add(2) // duplicate, will be ignored
```


2`を2回追加しようとしても、セットはコピーを1つしか保持しない。


値がセット**に入っているかどうかをチェックするには、`mySet.has(value)`を使う：


```javascript
console.log(mySet.has(2)) // true
console.log(mySet.has(3)) // false
```


値を**削除**するには、`mySet.delete(value)`を使います：


```javascript
mySet.delete(2)
```


すべてをクリアするには**、`mySet.clear()`を使う：


```javascript
mySet.clear()
```


セット`は、手動で重複をチェックすることなく、ユニークな値のコレクションを保持したい場合に便利です：


```javascript
const numberArray = [1, 2, 2, 3, 4, 4, 4, 5]

const numberSet = new Set(numberArray)

console.log(numberSet) // Set(5) { 1, 2, 3, 4, 5 }
```


Set`は重複を避けてくれる。


## イテレータ

<chapterId>61d24e5e-b7e4-541a-8322-778f61f26a72</chapterId>


JavaScriptでループ処理できるもの（配列、文字列、マップ、セットなど）のほとんどは**イテレート可能**です。


イテレータ**はJavaScriptの特別なオブジェクトで、アイテムのリストを**一度に**1つずつ見ていくのに役立ちます。


### オブジェクトのイテレータ


配列やマップと違って、通常のオブジェクトは**for...of`で反復可能**ではありません。これを試すと


```javascript
const user = {
name: "Alice",
age: 30
}

for (const value of user) {
console.log(value)
}
```


エラーが出ます：


```
TypeError: user is not iterable
```


それは、プレーン・オブジェクトにはイテレーターが組み込まれていないからだ。しかし、JavaScriptにはオブジェクトをループ処理するためのツールが用意されている。


#### オブジェクト.キー()`


Object.keys(obj)`を使ってオブジェクトの**keys**の配列を取得し、それをループすることができる：


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


このプリント：


```
name
age
```


#### `Object.values()`


値**をループするには、`Object.values()`を使う：


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


このプリント：


```
Alice
30
```


#### オブジェクト.エントリー()`


もし**キーと値の両方**が欲しければ、`Object.entries()`を使う：


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


このプリント：


```
name is Alice
age is 30
```


オブジェクトが直接反復可能でないとしても、これらのメソッドを使えば、`for...of`でうまく機能する方法で、オブジェクトの中身に完全にアクセスできる。


しかし、イテレーターはどのように機能するのだろうか？


### シンボル.イテレータ


すべてのイテレータブルの秘密は、`Symbol.iterator`と呼ばれる特別な**シンボル**にある。


この記号は、JavaScriptに伝える組み込みのキーである：「このオブジェクトは反復処理できる。


myIterable[Symbol.iterator]()` を呼び出すと、JavaScript は `.next()` メソッドを持つ **イテレータオブジェクト** を返します。


それがどんなものか見てみよう：


```javascript
const colors = ["red", "green", "blue"]

const iterator = colors[Symbol.iterator]()

console.log(iterator.next()) // { value: 'red', done: false }
```


.next()`を呼び出すたびに、次の値が返される。それが終わると戻る：


```javascript
{ value: undefined, done: true }
```


### next()`


.next()`メソッドは、シーケンスから次の項目を取得するために使われる。


.next()`を呼び出すたびに、2つのキーを持つオブジェクトが得られる：



- 値`: 現在のアイテム
- done`: 反復が終わったかどうかを示すブール値。


例を挙げてみよう：


```javascript
const names = ["Lina", "Tom", "Eva"]      // declare an array
const iterator = names[Symbol.iterator]() // use the Symbol.iterator function to get an iterator for this array

let result = iterator.next()              // get the first element of the array

while (!result.done) {                    // repeat this loop until you reach the last element of the array, which is marked with { done: true }
console.log(result.value)               // print the value of each element
result = iterator.next()                // get the next element of the array
}
```


このプリント：


```
Lina
Tom
Eva
```


これは、`for...of`ループがボンネットの中でどのように機能するかということで、`.next()`でこのパターンを使う。


と同じ結果になる。


```javascript
const names = ["Lina", "Tom", "Eva"]

for (const result of names) {
console.log(result)
}
```


### 反復可能なクラスの作成


また、`[Symbol.iterator]()`メソッドを追加することで、独自の**iterableクラス**を定義することもできます。


例えば、1から5までのような**数字の範囲**を表すクラスが欲しいとしよう。


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


このプリント：


```
1
2
3
4
5
```


これが現状だ：



- クラス `Range` を定義した。
- クラス内部では、`[Symbol.iterator]()`を実装しているので、JavaScriptは反復処理の方法を知っている。
- next()`メソッドは、数字を一つずつ返す。
- end` に到達すると、`{ done: true }` を返す。


これで `Range` クラスは配列のように機能するようになり、反復処理可能なループで使用できるようになった。


### ジェネレータ関数と `yield`


イテレータを簡単に作成するために、JavaScriptでは`function*`キーワード（`function`の最後に`*`をつけたもの）と`yield`キーワードを使った**ジェネレータ関数**を用意しています。


やってみよう：


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


各`yield`は値を返し、次の`.next()`が呼ばれるまで**一時停止**する。


for...of`でジェネレーターをループすることもできる：


```javascript
for (const num of numberGenerator()) {
console.log(num)
}
```


このプリント：


```
1
2
3
```


## コールバックによる並行処理

<chapterId>f3fc76ca-b3ef-54eb-a06e-501007002054</chapterId>


これまで、私たちのコードは**同期**だった。しかし、現実の世界では時間がかかるものもあり、待ち時間にプログラム全体が一時停止するのは避けたい。


この章では新しい概念を紹介する： **コンカレンシー**である。これは、物事が実行される順序を操作できるようにするものである。これはタイマーやユーザー入力、ディスクからのファイル読み込みなどを扱うときに便利です。JavaScriptには、並行処理を行うためのさまざまなツールがあります。


### setTimeout`。


関数 `setTimeout` を使うと、**ある関数を**時間が経ってから**実行することができる。


例


```javascript
console.log("Start")

setTimeout(
() => console.log("This runs after 2 seconds"),
2000
)

console.log("End")
```


このプリント：


```
Start
End
This runs after 2 seconds
```


setTimeout`がコードの途中に現れても、残りの部分をブロックすることはない。代わりに、その関数を**後で実行するようにスケジュールし、すぐに次に進む。


2000`は2000ミリ秒（2秒）を意味する。

ここでは、**コールバック**セクションと**プロミス**セクションを、データ操作と明確な注釈を駆使して、より冗長で初心者に優しいものに書き換える：


### コールバック


コールバック(**callback)**とは、他の関数に渡す関数で、後で呼び出すことができます**。


数字を使った実際の例を見てみよう。数値のリストがあり、それぞれを2倍にして、その結果の "2倍 "配列に関数（コールバック）を適用したいとします。


以下は、**コールバック**を使ってそれを行う関数である：


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


この機能を使ってみよう：


```javascript
const input = [1, 2, 3]

doubleNumbers(input, function(result) {
console.log("Here is the doubled array:", result)
})
```


1秒後に印刷される：


```
Here is the doubled array: [ 2, 4, 6 ]
```


**何が起きているんだ？


1.倍加したい数字のリストとして `input` を渡す。

2.また、**コールバック関数**も渡す。

3.doubleNumbers`の内部では、`setTimeout`を使って遅延をシミュレートし、それから倍加を行う。

4.それが完了したら、結果の "doubled "配列に対してコールバックを呼び出す。


このテクニックはうまくいくが、その後に**さらに**ステップ**を行いたい場合を想像してほしい。このようなコールバックをさらに**入れ子に**しなければならないだろう：


```javascript
doubleNumbers(input, function(doubled) {
filterBigNumbers(doubled, function(filtered) {
sumNumbers(filtered, function(total) {
console.log("Final result:", total)
})
})
})
```


これはHardで読むのが面倒だ。このスタイルは**callback hell**と呼ばれ、まさに`Promise`が修正するために作られたものだ。


## プロミスによる同時実行

<chapterId>30fddaca-729f-5c8d-bf86-8dfc7b3c9800</chapterId>


Promise`は組み込みのJavaScriptオブジェクトで、**将来**に用意される値を表します。


このようにプロミスを作ることができる：


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve("It worked!") // This means everything went OK
})
```


new Promise()`の部分はプロミスを生成する。


その中で、2つのパラメーターを持つ関数を与える：



- resolve`は、すべてが成功したときに呼び出す関数である。
- reject`は、何か問題が発生したときに呼び出す関数である。


上の例では、`"It worked!" `というメッセージとともに即座に解決している。


### .then()`


プロミスが完了した後**に何かをするには、`.then()`を使う：


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve(100) // This means everything went OK
})

promise.then(result => {
console.log("The result is:", result)
})
```


このプリント：


```
The result is: 100
```


resolve()`に渡した値は `result` として `.then()` 内の関数に送られる。


setTimeout`を使って2秒かかるタスクをシミュレートしてみよう：


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


これは2秒待ってから印刷する：


```
Done waiting!
```


### reject()`


失敗**する約束を作ろう：


```javascript
const failingPromise = new Promise((resolve, reject) => {
reject("Something went wrong")
})
```


ここで、`.then()`を使っても何も起こらない。なぜなら、`.then()`は成功だけを処理するからだ。


エラーを処理するには `.catch()`：


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


のみを印刷する。


```
Caught an error: Something went wrong
```


reject()`に渡された値は `.catch()` 関数に送られる。


ある条件に基づいて、**うまくいくこともあれば失敗することもある**プロミスを作ってみよう。


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


これで、これを呼び出して両方のケースを処理することができる：


```javascript
checkNumber(5)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


このプリント：


```
Success: Positive number
```


そして、別の番号で試してみると......：


```javascript
checkNumber(-1)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


印刷される：


```
Failure: Not a positive number
```


### 約束`を使った連鎖操作



先ほどの例を `Promise` を使って書き直せば、見た目はもっとすっきりする。


まず、倍加関数の新しいバージョンを書いてみよう。今回は、**約束**を返す：


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


これで、`.then()`を使ってJavaScriptに結果をどうするか指示できるようになった：


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


このプリント：


```
Doubled numbers: [ 2, 4, 6 ]
```


今のところ、これはコールバック・バージョンと同じように機能するが、コードが拡張しやすく、読みやすくなった。


さらにステップを増やしたいとしよう：


1.まず、すべての数字を2倍にする

2.次に、4より小さい数字を削除する。

3.最後に、それらをすべて足す


各ステップごとに1つの関数を書くことができ、すべてプロミスを使う：


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


これで、このように**チェーン**することができる：


```javascript
const input = [1, 2, 3]

doubleNumbers(input)
.then(filterBigNumbers)
.then(sumNumbers)
.then(
result => console.log("Final result after all steps:", result)
)
```


このプリント：


```
Final result after all steps: 10
```


これが何をするのか、順を追って説明しよう：


1.doubleNumbers`は配列を2倍にする：`[2, 4, 6]`

2.filterBigNumbers` は ≤ 3: `[4, 6]` を除去する。

3.sumNumbers`は残りの数字を足す：`4 + 6 = 10`

4.最後に、結果をプリントする。


各`.then()`は、その前のステップが終了するのを待つ。そのため、入れ子にすることなくアクションの**連鎖**を作ることができる。これにより、コードがより読みやすくなり、デバッグもしやすくなる。


## async`/`await`による並行処理

<chapterId>6e93d29f-c8bf-5fd1-a9c9-4e794ee6cbd0</chapterId>


プロミス・チェーンはコールバック地獄を回避するのに役立つが、多くのステップを含む場合、少しHardを読むことになる。


そこで登場するのが `async` と `await` だ。これらは、**同期コードのように見える**非同期コードを書くことを可能にしてくれる。


### async`とは？


関数の前にキーワード `async` を書くと、JavaScript は関数の戻り値を自動的に Promise でラップします。


基本的な例を見てみよう：


```javascript
async function greet() {
return "hello"
}
```


この関数を呼び出すと


```javascript
const result = greet()
console.log(result)
```


これを見てほしい：


```
Promise { 'hello' }
```


文字列を返しただけなのに、JavaScriptはそれをPromiseに変えてくれます。次のように`.then()`を使って実際の値を得ることができる：


```javascript
greet().then( result => console.log(result) ) // prints "hello"
```


あるいは、`await`を使うこともできる。


### await`とは何か？


キーワード `await` はJavaScriptにこう指示する：「このPromiseが実行されるまで待ち、それから結果を返せ。


しかし、`await`を使えるのは**非同期関数の中だけだ**。


await`を使って例を書き直してみよう：


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


これで、結果を通常の値のように使うことができる。


もう少し役に立つことをしよう。


### await`による遅延のシミュレーション


ミリ秒を引数にとり、そのミリ秒後に何もせずに解決する単純な `wait` 関数を作ることにしよう：


```javascript
function wait(ms) {
return new Promise(resolve => {
setTimeout(resolve, ms)
})
}
```


使ってみよう：


```javascript
async function test() {
console.log("waiting 2 seconds...")
await wait(2000)
console.log("done waiting")
}

test()
```


このプリント：


```
waiting 2 seconds...
done waiting
```


await`は "約束が完了するまでここで一時停止し、それから続ける "と考えることができる。


これにより、`.then()`コールを連鎖させることなく、非同期で動作する**上から下***の方法でコードを書くことができる。


### データ待ち


前の例を再利用してみよう。ここでは、数値を2倍にして、フィルターをかけて、合計する。しかし、今回は `async`/`await` を使う。


待ち時間をシミュレートし、プロミスを返す関数を3つ作る：


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


では、これらを組み合わせるための`async`関数を書いてみよう：


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


このプリント：


```
Final result: 10
```


これは、`.then()`を連鎖させたり、コールバックを入れ子にしたりするよりもずっと読みやすい。


通常のステップ・バイ・ステップのプログラムのように見えるが、やはり非同期的に動作する。


## 非同期イテレータ

<chapterId>438b037d-9931-56d7-9052-7b4470f3c75b</chapterId>


すでに**イテレータ**について学び、`for...of`を使って配列やその他のイテレート可能なものをループする方法を学んだだろう。


しかし、反復処理したいデータが到着するまでに時間がかかるとしたらどうだろう？


チャットからのメッセージ、ファイルからの行、遅いソースからの数字など、**非同期**に到着するものをループ処理したいことがある。


そのために、JavaScriptは**asyncイテレータ**を用意している。


### 非同期ジェネレーター関数


非同期イテレータを作成する最も簡単な方法は、**非同期ジェネレータ関数**を使用することである。


私たちはこう書いている：


```javascript
async function* generateNumbers() {
yield 1
yield 2
yield 3
}
```


これは通常のジェネレーターと同じように見えるが、その前に`async`がついている。


これで、`for await...of`を使って値を消費できるようになった：


```javascript
async function run() {
for await (const n of generateNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


これが印刷される：


```
Got number: 1
Got number: 2
Got number: 3
Done!
```


では、通常の発電機と何が違うのか？


違いは、ジェネレーターの内部で`await`が使えるようになったことだ。


またディレイヘルパーを作ろう：


```javascript
function wait(ms) {
return new Promise(resolve => setTimeout(resolve, ms))
}
```


では、**ゆっくりと**数字を出してみよう：


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


使ってみてください：


```javascript
async function run() {
for await (const n of generateSlowNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


### なぜ非同期イテレータを使うのか？


非同期イテレーターは、以下のような場合に役立つ：



- 価値は一度にすべて届くわけではない。
- 一度に一つずつ、**来るたびに**処理したい。
- あなたはプロミスで仕事をしていて、きれいな方法でループさせたいと思っている。


例えば、チャット・サーバーからメッセージを1つずつ読み込んだり、大きなファイルをチャンク単位でダウンロードしたい場合、非同期イテレータを使えば、遅延データで動作する`for`ループを書くことができる。


### シンボル.asyncIterator`。


カスタム・クラスで非同期イテレーターを使うこともできる。


これは、遅延を伴う数字を生成する例である：


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


以前と同じように`for await...of`が使えるようになった：


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


これにより、非同期に反復処理できるオブジェクトを作成できる。


## Assignmentシンタックスシュガー

<chapterId>8b1ba7d8-ecfd-5470-b86e-73cb84ccc8b7</chapterId>


「シンタックス・シュガー（Syntax Sugar）」とは、何かをより短く、より簡単に書くことを意味する。同じことを言うのにより良い方法だ。


JavaScriptには、よりすっきりと短い宣言を書くためのシンタックス・シュガーが組み込まれています。この章では、条件に基づいて値を代入する方法、数式を使って変数を更新する方法、配列やオブジェクトから値を取り出す方法、よりシンプルな構文でコピーや結合を行う方法を見ていきます。


### 三項演算子


JavaScriptでは、`if...else`の短い書き方である**三項演算子**を使って、条件に基づいて値を代入することができます。


そうする代わりに


```javascript
let message

if (isMorning) {
message = "Good morning"
} else {
message = "Hello"
}
```


と書くことができる：


```javascript
const message = isMorning ? "Good morning" : "Hello"
```


ということだ：



- もし `isMorning` が真なら、`"Good morning"`を使う。
- そうでない場合は、`"Hello"` を使用する。


一般的な形はこうだ：


```javascript
condition ? valueIfTrue : valueIfFalse
```


他の式の中でも使える：


```javascript
console.log(isSunny ? "Go outside" : "Stay in")
```


ただ、**単純な**判断に使うようにしてください。ロジックが複雑な場合は、`if...else`にこだわること。


### 代替Assignmentオペレーター


JavaScriptには、演算と組み合わせた代入を行うための**ショートカット演算子**がある。


通常の方法を見てみよう：


```javascript
let counter = 1
counter = counter + 1
```


これは短縮できる：


```javascript
let counter = 1
counter += 1 // same as counter = counter + 1
```


最も一般的なものを紹介しよう：


| Operator | Meaning             |
| -------- | ------------------- |
| `+=`     | add and assign      |
| `-=`     | subtract and assign |
| `*=`     | multiply and assign |
| `/=`     | divide and assign   |

例を挙げよう：


```javascript
let score = 10
score += 5  // now score is 15
score *= 2  // now score is 30
score -= 10 // now score is 20
```


これらは、変数自身の値を使って変数を更新したい場合に便利である。


### 構造改革


**デストラクチャリング**を使えば、配列やオブジェクトから値を取り出して変数に簡単に格納できる。


#### 配列


仮にそうだとしよう：


```javascript
const colors = ["red", "green", "blue"]
```


そうする代わりに


```javascript
const first = colors[0]
const second = colors[1]
```


あなたならできる：


```javascript
const [first, second] = colors
```


これは割り当てである：



- first`を`"red"`に変更する。
- 秒`から`"Green"`へ


値をスキップすることもできる：


```javascript
const [,, third] = colors
console.log(third) // blue
```


#### 対象物


オブジェクトから値を抽出することもできる：


```javascript
const user = { name: "Alice", age: 30 }

const { name, age } = user
console.log(name) // Alice
console.log(age)  // 30
```


プロパティの名前が目的の変数と異なる場合は、名前を変更することができます：


```javascript
const { name: username } = user
console.log(username) // Alice
```


デストラクチャリングは、オブジェクトや配列を扱うときにコードをすっきりさせる。


### スプレッド構文


spread構文**は `...` を使って値を展開またはコピーする。


#### 配列


アレイのコピーやマージができる：


```javascript
const a = [1, 2]
const b = [3, 4]

const both = [...a, ...b]
console.log(both) // [1, 2, 3, 4]
```


配列のクローンを作ることもできる：


```javascript
const original = [10, 20, 30]
const clone = [...original]
```


#### 対象物


オブジェクトでも同じことができる：


```javascript
const a = { x: 1 }
const b = { y: 2 }

const merged = { ...a, ...b }
console.log(merged) // { x: 1, y: 2 }
```


値を上書きすることもできる：


```javascript
const user = { name: "Alice", age: 30 }
const updated = { ...user, age: 31 }

console.log(updated) // { name: "Alice", age: 31 }
```


これは、オリジナルを変更せずにオブジェクトを更新する場合に非常に便利です。


# ノードJS

<partId>42fe4d49-dace-5135-bb9e-b9d75034fb2a</partId>


## ノードへの道

<chapterId>0da1d60c-06c9-54e6-a181-ae7dabf6e3b8</chapterId>


この章では、JavaScriptとNodeJSについての歴史的背景を少し学びます。


歴史的な背景はソフトウェアにおいて非常に重要で、私たちはしばしば他の人が作ったツールを使っているため、その人が過去に下した決断の影響を受けてしまう。


その決断の理由や、私たちが使っている道具がどのようにして今の形になったのかを理解することで、自分たちがやっていることへの戸惑いが少しは減るだろう。


### JavaScriptの起源


JavaScriptは、ウェブページをインタラクティブにするために設計されたシンプルな言語として始まった。


1990年代には、ネットスケープ・ナビゲーターのようなウェブ・ブラウザがJavaScriptを追加し、開発者がブラウザで直接実行するコードを書けるようになった。


もともとのアイデアは、Javaをウェブサイト制作の中核言語（いわゆる "Javaアプレット"）とし、JavaScriptはマイナーなものだけに使うというものだった。


コアデザインは、当時ネットスケープの社員だったブレンダン・アイヒが2週間足らずで行った。


しかし、ほとんどの人はJavaよりもJavaScriptを使うことを好み、またJavaアプレットには当時セキュリティ上の問題があったため、最終的にJavaは選択肢から外され、JavaScriptがウェブ開発のデファクト・スタンダードとなった。


### V8エンジン


JavaScriptは、C言語のようなコンパイル言語とは対照的に、インタプリタ言語である。


コンパイル言語で書かれたコードはバイナリ化され、バイナリはコンピューターのCPUに直接供給される。


![](assets/en/6.webp)


一方、インタープレード言語は、よりユーザーフレンドリーになる傾向があり、機械がどのように動くか（「ローレベル」）よりも、人間がどのように考えるか（「ハイレベル」）に近い。


仮想マシンは、あなたが書いたコードとCPUの間に位置し、あなたのコードを実行する特別なプログラムである（CPUはそれを理解できないため）。


なぜなら、コンピュータはあなたのプログラムだけを実行しているのではなく、あなたのプログラムを実行するプログラム（仮想マシン）を実行しているからだ。


ウェブ・アプリケーションがますます複雑になるにつれ、JavaScriptのパフォーマンス向上が求められるようになった。V8エンジンは、Google ChromeのJavaScriptを動かすインタプリタである。Googleで開発され、2008年にリリースされた。


旧来のJavaScriptエンジンは伝統的な仮想マシンが主流だったが、V8エンジンはJIT（ジャスト・イン・タイム）コンパイラだ。


JavaScriptのコードはV8エンジンに送られ、エンジンはその一部をネイティブ・バイナリとしてオンザフライでコンパイルしようとする。これにより、低レベル言語に少し近いパフォーマンスで、高レベル言語の経験を持つことができる。これによって、JavaScriptは世界最速の高級言語となった。


### NodeJSランタイム


使いやすく、実行速度もかなり速いJavaScriptだが、V8がリリースされた後は、ブラウザーの中でしか実行できないという大きな制約があった。


なぜそれが問題なのか？


ブラウザーはインターネット上の何百万もの異なるソースから取得したコードを実行するため、マルウェアに簡単に感染する可能性がある。


![](assets/en/7.webp)


JavaScriptは、コンピュータ上のファイルシステムやその他のローカルリソースにアクセスできない（少なくとも、他の言語のように簡単にはアクセスできない）ため、JavaScriptで構築できるアプリケーションの種類には大きな制限があった。


2009年、ライアン・ダールはNodeJSを発表した。NodeJSはランタイムであり、V8エンジンをブラウザーの外で、コンピューターのネイティブ・オペレーティング・システム上で直接使うことができる。また、サーバーサイドやコマンドライン・プログラムを書くのに便利な多くの機能が追加されている。例えば、NodeJSを使用してWebサーバーを作成したり、ファイルを読み書きしたり、タスクを自動化するツールを構築したりすることができます。


![](assets/en/8.webp)


このコースではこれまで、ブラウザとNodeJSの両方に存在するJavaScriptの機能を探ってきた。これらの機能によって、データを定義し、抽象的な方法で操作できるようになりました。次の数回のレッスンでは、NodeJSに特有で、オペレーティング・システムと対話できる機能を探ります。


## コマンドライン引数

<chapterId>960d20f3-c424-5d51-a041-ef17d2e94b6d</chapterId>


NodeJSは、とりわけCLI（コマンドライン・インターフェース）を構築することを可能にしてくれる。


そのためには、コマンドライン引数を受け取る方法が必要で、Nodeでは組み込みの `process` オブジェクトを使用する。


### プロセス


NodeJSは、現在実行中のプログラムを表す`process`という特別なオブジェクトを提供する。


環境、カレント・ワーキング・ディレクトリーの検査、そして必要に応じてプログラムの終了にも使用できる。


例えば、こうだ：


```javascript
console.log(process.platform)
```


これは、`win32`、`linux`、`darwin`（Mac）のように、オペレーティングシステムのプラットフォームを表示する。


### `process.argv`


ターミナルからNodeJSプログラムを実行するとき、スクリプト名の後に余分な単語（引数）を渡すことができる。これらは `process.argv` に格納される。


例えば、次のコマンドを実行する：


```
node my_script.js alpha beta
```


このように引数を表示することができる：


```javascript
console.log(process.argv)
```


出力は次のようになる：


```
[ '/path/to/node', '/path/to/my_script.js', 'alpha', 'beta' ]
```


最初の2つの項目は常にノードパスとスクリプトパスです。スクリプトに渡した追加の単語はその後に続く。


process.argv`配列は、`.slice()`メソッドを使って他の配列と同じように切り出すことができるので、渡された引数だけを取得するには次のようにする。


```javascript
const args = process.argv.slice(2)

console.log(args)
```


ユーザーが渡す引数にアクセスできることは、コマンドライン・アプリケーションを開発する上で基本的なことである。


## モジュール

<chapterId>4e1651a5-65fd-50bc-b22a-40313d5659ca</chapterId>


NodeJSのようなJavaScriptランタイムは通常、各JavaScriptファイルを個別のモジュールとして扱う。


モジュールを箱だと考えてください。ボックスには独自のプライベート・スペースがあり、そこで宣言した変数や関数が他のボックスのコードに干渉することはない。基本的に、各モジュールは独自のスコープを持っています。


モジュールはそのコンテンツの一部をエクスポートして、他のモジュールで利用できるようにしたり、他のモジュールがエクスポートしたコンテンツをインポートしたりすることができます。JavaScript では、モジュール間でコンテンツをエクスポートしたりインポートしたり、異なるファイルを接続したりすることができます。


JavaScriptのプログラムは多くの場合、複数のモジュールで構成され、それらは互いに接続されている。


なぜモジュールを使うのか？コードをモジュールに分割することで、プログラムをより小さく、より明確で、再利用可能な部分に整理することができます。各モジュールは、数学の計算処理、ファイルの操作、テキストの書式設定など、1種類のタスクだけに集中することができます。


### CommonJSモジュール


NodeJSでは、モジュールを管理する最も一般的なシステムは**CommonJS**と呼ばれる。


このシステムでは、`module.exports`を使ってモジュールからコードを共有（エクスポート）し、`require()`を使って別のファイルにロード（インポート）することができる。


モジュールの外で何かを利用できるようにするには、`module.exports`にそれを代入する：


```javascript
const greeting = "Hello!"

module.exports = greeting
```


ここで、文字列 `"Hello!"` はこのモジュールがエクスポートするものである。


別のファイルからエクスポートされたコードを使用するには、そのファイルへのパスを指定して `require()` 関数を使用します：


```javascript
const greeting = require("./greeting.js")

console.log(greeting)
```


このプリント：


```
Hello!
```


のように、匿名オブジェクトにまとめて複数のものをエクスポートできます。


```javascript
const greeting1 = "hello"

const greeting2 = "hi"

module.exports = {
greeting1, greeting2
}
```


CommonJSは、NodeJSが最初に採用したモジュール・システムである。後にESモジュールも追加された。


### ESモジュール


NodeJSは**ESモジュール**と呼ばれる別のタイプのモジュールもサポートしている。これらは `export` と `import` というキーワードを使用する。


ESモジュールはブラウザ用に開発され、後にNodeに追加されました。ESモジュールを使いたい場合は、使用しているNodeのバージョンによって、拡張子として`.js`の代わりに`.mjs`を使う必要があるかもしれません。


あるファイル`greeting.mjs`では次のように書いている。


```javascript
export const greeting = "Hello!"
```

ご覧のように、定数が定義されている場所に直接エクスポートしています。


index.mjs`という別のファイルで、これをインポートする：


```javascript
import { greeting } from "./greeting.mjs"

console.log(greeting)
```


のように、ファイルの異なる部分に異なる宣言を書き出すことができる。


```javascript
export const num = 10

export function double (x) {
return x*2
}
```


### NodeJS標準ライブラリ


NodeJSには多くの組み込みモジュールも含まれています。これらはNodeJSが提供する既製のモジュールで、ファイルの読み込み、オペレーティングシステムとの連携、ネットワークへの接続などの一般的なタスクを支援します。


例えば、`os`モジュールはオペレーティング・システムに関する情報を提供する：


```javascript
const os = require("os")

console.log(os.platform())
```


これらの組み込みモジュールはインストールする必要はなく、NodeJSに付属しています。これらはランタイムの "標準ライブラリ "を形成し、ファイルの読み込みやインターネット経由の通信など、ほとんどのNodeアプリケーションで使用されます。


次の章では、その有用な使用例をいくつか紹介する。


## fs` モジュール

<chapterId>911e953a-35ae-5ee7-bd74-372501c32e81</chapterId>


fs` モジュール (**ファイルシステム** の略) は NodeJS 標準ライブラリの一部です。このモジュールを使うと、コンピュータ上のファイルやディレクトリを操作することができます。ファイルを読んだり、ファイルを書き込んだり、ファイルを削除したり、ファイル名を変更したりすることができます。


これを使うには、まずファイルの先頭にインポートする必要がある：


```javascript
const fs = require("fs")
```


### 同期API


fs` を使う最も簡単な方法は、**sync** メソッドを使うことである。


これらのメソッドは、終了するまでプログラムをブロックする（そのため、操作が完了するまで次のコード行は実行されない）。


以下は、同期的にファイルを読み込む例である：


```javascript
const fs = require("fs")

const data = fs.readFileSync("example.txt", "utf8")

console.log(data)
```


スクリプトと同じディレクトリに`example.txt`というファイルがあれば、その内容を表示します。


同期的にファイルに書き込むこともできる：


```javascript
const fs = require("fs")

fs.writeFileSync("output.txt", "Hello from Node!")

console.log("File written!")
```


これにより、`output.txt`というファイルがテキストで作成（または上書き）される。


このAPIでできる一般的な操作をいくつか紹介しよう：


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


Sync APIはシンプルで、小さなスクリプトには適しているが、それが完了するまでプログラムをブロックするため、大きなファイルやサーバーを扱う場合は動作が遅くなることがある。


### コールバック非同期API


コールバックAPI**はノンブロッキングである。


結果を直接返す代わりに、操作が完了したときに呼び出される関数（**コールバック**）を受け取ります。


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


こうなる：



- `fs.readFile` が `example.txt` の読み込みを開始する。
- NodeJSは待たずに、あなたが書いたかもしれない他のコードの実行に移る。
- ファイルの読み込みが終わると、コールバックが実行される：



  - エラーがあった場合は、`err`にエラーが格納される。
  - そうでない場合は、`data`に内容が格納される。


ファイルに書き込む方法を説明しよう：


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


同じ考えだ。ファイルを書いている間、プログラムは止まらない。


このAPIでできることの例をいくつか挙げよう：


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


コールバックAPIはプログラムをブロックしないので、サーバーや大きなタスクに適しているが、ネストされたコールバックは、多くの処理を連鎖させると面倒なことになる。そのため、プロミス・ベースの非同期APIが追加された。


### プロミス非同期API


PromiseベースのAPIはモダンで、`.then()`や`async/await`と相性が良い。これは `fs.promises` として提供されている。


promises`プロパティをインポートする必要がある：


```javascript
const fs = require("fs").promises
```


.then()`を使用する：


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


あるいは、`async/await`を使うのもいい：


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


ファイルへの書き込み：


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


APIの通常の例のリスト：


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



## エヌピーエム

<chapterId>a91d9a75-55cc-51a3-a48f-0c0be6fe6e72</chapterId>


例えば、日付、色、サーバー、その他ほとんどのものを扱うのに役立つライブラリなどだ。


手動でファイルをダウンロードしてコピーする代わりに、**パッケージマネージャ**を使用することができます。


パッケージ・マネージャーとは、以下のようなツールである：



- ダウンロードパッケージ
- プロジェクトが必要とするパッケージを追跡
- チーム全員が同じバージョンのパッケージを持っていることを確認する。


### NPMとは


NodeJSの世界では、最も人気のあるパッケージ・マネージャーは**NPM**で、**Node Package Manager*の略です。


NodeJSをインストールすると、NPMが自動的にインストールされます。


NPMがあるかどうかは、ターミナルでこれを実行すれば確認できる：


```
npm -v
```


のように、NPMのバージョンを表示する：


```
10.2.1
```


### パッケージの作成


NodeJSでは、**パッケージ**は、`package.json`ファイルを含むディレクトリに過ぎない。


ステップ・バイ・ステップで作っていこう。


1.プロジェクト用の新しいフォルダを作成する：


```
mkdir my_project
cd my_project
```


2.このコマンドを実行する：


```
npm init
```


インタラクティブなセットアップが始まり、プロジェクト名、バージョン、説明などの質問をします。


すべてに答えずに、デフォルトを受け入れるだけでいいのなら、これを使うことができる：


```
npm init -y
```


これを実行すると、フォルダ内に新しいファイルが作成されます：


```
package.json
```


### `package.json`


package.json`ファイルは、プロジェクトのメタデータを格納するJSONファイルです。


例を挙げよう：


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


いくつかの重要な分野



- name`: パッケージ名
- バージョン`: 現在のバージョン
- `main`: エントリポイントファイル（`index.js` のようなもの）。
- スクリプト`: 実行可能なコマンド（`npm start`など）。
- dependencies`: プロジェクトが依存しているパッケージの一覧を表示する。


### パッケージのインストール


例えば、`picocolors`というパッケージを使って端末の出力に色を付けたいとしよう。


を実行すればインストールできる：


```
npm install picocolors
```


これでプロジェクトで使用できる。で `index.js` ファイルを作成する。


```javascript
const pico = require('picocolors')

console.log(
pico.green("This text is green!")
)
```


を実行する。ターミナルに色つきのテキストが表示されるはずだ。


故宮は何をしたのか？



- パッケージをダウンロードし、`node_modules/`というサブフォルダーに格納する。
- すると、`package.json`の`dependencies`の下にエントリが追加されます。
- それは `package-lock.json` ファイルを更新した。


package-lock.json`とは何ですか？


### `package-lock.json`


このファイルはNPMによって自動的に作成されます。


すでに`package.json`があるのに、なぜ別のファイルが必要なのかと思うかもしれない。

その理由はこうだ：



- `package.json`は、プロジェクトが必要とするパッケージのバージョン**範囲**を示すだけである。

例


```json
"dependencies": {
"picocolors": "^1.1.0"
}
```


1.1.0`は「1.1.xと互換性のあるすべてのバージョン」を意味するので、柔軟性がある。



- `package-lock.json` は、すべてのパッケージとそのサブ依存パッケージの正確なバージョンを **凍結** して、あなたのプロジェクトをインストールするすべての人がまったく同じセットアップを使えるようにします。


なぜこれが重要なのか？


チームで仕事をする場合、プロジェクトをサーバーにデプロイする場合、将来また戻ってくる場合、同じように動作することを確認したい。

パッケージがアップデートされ、ロックファイルなしで再インストールした場合、動作が若干異なるバージョンが入手できるかもしれません。


package-lock.json`をプロジェクト内に保持することで、NPMは常にそこに記載されている正確なバージョンをインストールし、すべての人が同じ環境を利用できるようになる。


`package-lock.json`は、プロジェクトを他のマシンでも再現できるようにするため、すべてを特定のバージョンにロックする。


しかし、あなたのパッケージが多くの人に使われる必要がある場合、代わりにコミットしないことを選択することもできます。そうすることで、NPMは`package.json`ファイルだけを見つけ、そのファイルで許可されている最新バージョンを自動的にインストールすることができます。


しかし、これらのことは、自分のコードを公開するようになってから、後で心配すればいいことだ。今のところ、NPMの基本を紹介したのは、他の開発者が公開しているライブラリをあなたのプロジェクトで見つけて使えるようにするためだけだ。



## NodeJSでのネットワーキング

<chapterId>f2cabd8b-754b-5c97-8d6a-8412a9a184c7</chapterId>


NodeJSはバックエンドの言語としてよく使われる。スクリプトをサーバーに変えたり、他のサーバーにリクエストするのに使うことができる。


この章では、それを可能にする基本的なネットワーク機能を紹介する。


### fetch()`


あなたのプログラムがウェブサイトやAPIからデータをダウンロードしたい場合、**HTTPリクエスト**を行う必要があります。


最近のバージョンのNodeJSでは、組み込みの `fetch()` 関数を使うことができます。


APIへのGETリクエストの例である：


```javascript
const response = await fetch("https://jsonplaceholder.typicode.com/posts/1")
const data = await response.text()

console.log(data)
```


これを実行すると、次のように表示される：


```
{
"userId": 1,
"id": 1,
"title": "...",
"body": "..."
}
```


こうなる：


1.fetch()`はURLを受け取り、リクエストを行う。

2.これは `Response` オブジェクトを解決する **Promise** を返す。

3.`response.text()` はレスポンス本文を文字列として読み込む。


しかし、戻ってくる文字列は実際にはJSONだ。それは何なのか？


### JSON


ウェブAPIで作業する場合、データはしばしば**JSON**（JavaScript Object Notationの略）として送受信される。


JSONは、JavaScriptのオブジェクトによく似たテキスト形式だ。例えば


```json
{
"name": "Alice",
"age": 30,
"likes": ["apples", "bananas"]
}
```


JSON`オブジェクトはJavaScriptの組み込みユーティリティであり、このデータフォーマットを扱うために使用できる。


JSON.stringify()`を使ってJavaScriptオブジェクトをJSON文字列に変換することができます：


```javascript
const user = { name: "Alice", age: 30 }

const jsonString = JSON.stringify(user)

console.log(jsonString)
```


このプリント：


```
{"name":"Alice","age":30}
```


JSON.parse()`を使って、JSONテキストをJavaScriptオブジェクトに変換することもできます：


```javascript
const jsonText = '{"name":"Bob","age":25}'

const obj = JSON.parse(jsonText)

console.log(obj)
```


このプリント：


```
{ name: 'Bob', age: 25 }
```


注意してください：JSON.parse()`は、文字列が有効なJSONでない場合、エラーをスローします。


```javascript
JSON.parse("not json") // ❌ Error!
```


そのため、文字列が適切にフォーマットされていることを確認する。


### httpサーバー


NodeJSを使えば、何もインストールすることなくウェブサーバーを作成できる。


組み込みの `http` モジュールを使って、クライアントからのリクエストを処理し、レスポンスを送り返すことができる。


非常に基本的な例を挙げよう：


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


このスクリプトを実行し、ブラウザで`http://localhost:3000`を開くと、次のように表示される：


```
Hello from NodeJS server!
```


これがコードで起きていることだ：


1.Node 標準ライブラリから `http` サーバをインポートした。

2.http.createServer()`はサーバを作成します。誰かが接続するたびに実行されるコールバック `(req, res) => {...}` を `http.createServer()` に渡しました。

3.あなたはレスポンスにステータスコード200（操作の成功を示す）を割り当てました。httpステータスコードについては[こちら](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)を参照してください。

3.res.end()`はレスポンスを送信し、接続を終了する。

4.server.listen(3000)`はポート3000でサーバーを起動する。


リクエストの `req.url` と `req.method` をチェックして、異なるパスやリクエストタイプを扱うこともできる。


ルーティングの例：


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


これらは非常に基本的な例である。より高度なサーバーを構築する場合、ほとんどの開発者は[express](https://www.npmjs.com/package/express)のような既製のバックエンドライブラリをダウンロードするだろう。


## データの処理：バッファ、イベント、ストリーム

<chapterId>8c9623f0-a604-51a4-8fe4-871c849d3e3b</chapterId>


この章では、主に3つのクラスのオブジェクトを紹介する：



- バイナリデータの小さなチャンクを表す `Buffer` 。
- EventEmitter`は、"event "と呼ばれるシグナルを発信することで、非同期処理で何らかのステップを追跡するために使用できる。
- ストリーム `Stream` は、一度に大きなデータ`バッファ`を処理することができる。


これらは、プロのNodeJSコードでは非常に一般的なものなので、最初のプロジェクトでは使用しないかもしれませんが、これらを使用する必要がある場合のために、基本的な理解をしておくとよいでしょう。


### バッファ


NodeJSでは、**バッファ**はバイナリ・データを扱うために使用されるオブジェクトの一種です。


バッファは、生のバイトを入れる固定サイズの入れ物と考えることができる。


ここでは、文字列からバッファを作成する方法を説明する：


```javascript
const buf = Buffer.from("hello")
console.log(buf)
```


これは次のように表示される：


```
<Buffer 68 65 6c 6c 6f>
```


これらの数字（`68`、`65`、`6c`など）は`"hello"`の文字を16進数で表したものである。


このように文字列に戻すことができる：


```javascript
console.log(buf.toString())
```


このプリント：


```
hello
```


また、ゼロで埋め尽くされた一定サイズのバッファを作成することもできる：


```javascript
const buf = Buffer.alloc(10)
console.log(buf)
```


これは次のように表示される：


```
<Buffer 00 00 00 00 00 00 00 00 00 00>
```


バッファに書き込むことができる：


```javascript
buf.write("abc")
console.log(buf)
```


また、個々のバイトにアクセスすることもできる：


```javascript
console.log(buf[0]) // prints the ASCII number for 'a', which is 97
```


バッファは、非常に低いレベルでデータを操作する必要がある場合に特に役立つ。


### イベント


JavaScriptでは、**イベント**とは、プログラムの中で起こる何かで、それに反応することができるものである。


例えば、こうだ：



- ファイルの読み込み終了
- タイマーが切れる
- ユーザーがボタンをクリックする
- ネットワーク要求がデータを返す


イベント**は、何かが起こったというシグナルに過ぎず、そのイベントをリッスンし、それに反応するコードを書くことができる。


NodeJSでは、多くのオブジェクトがイベントを発することができます。これらのオブジェクトは **EventEmitters** と呼ばれます。


例を挙げよう：


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


このプリント：


```
Hello! An event happened.
```


こういうことだ：


1.EventEmitter`オブジェクトを作成する。

2..on("greet")`を使って、`"greet"`イベントが発生するたびにコールバックを実行するように指示します。

3.後で、`.emit()`を使って `"greet"` イベントをトリガーする。

4.コールバックが実行される


イベントと一緒にデータを渡すことができる：


```javascript
emitter.on("greet",
(name) => console.log(`Hello, ${name}!`)
)

emitter.emit("greet", "Alice") // first argument is the type of event, second argument is the data we pass with this event
```


このプリント：


```
Hello, Alice!
```


他のイベントのリスナーも登録できる：


```javascript
emitter.on("goodbye", () => {
console.log("Goodbye!")
})

emitter.emit("goodbye")
```


また、同じエミッターから多くの異なるタイプのイベントを発生させることができます。


NodeJSの多くのオブジェクトは、何かが起こっていることをプログラムの残りの部分に伝えるためにイベントを発行します。



### ストリームとは何か？


ストリームはバッファとイベントを組み合わせて、データ処理を支援する。


ファイルやネットワークからのデータ、あるいは長いテキストを扱うとき、必ずしもすべてを一度にメモリにロードする必要はない（したくない）。それでは時間がかかるし、データが大きすぎるとプログラムがクラッシュすることさえある。


一度にコップ全部を飲もうとするのではなく、ストローで水を飲むようなものだ。これを**ストリーム**と呼ぶ。


NodeJSでは、ストリームは、ソースからデータを読み込んだり、宛先に**一度に**データを書き込むことができるオブジェクトです。


NodeJSには主に4種類のストリームがある：



- Readable**: データを読めるストリーム（ファイルを読むようなもの）
- Writable**：データを書き込めるストリーム（ファイルに書き込むようなもの）
- 二重**：読み取りと書き込みの両方が可能なストリーム
- トランスフォーム**：二重ストリームのようなものだが、流れながらデータを変化（トランスフォーム）させることができる。


### 読み取り可能なストリーム


例えば、`bigfile.txt` を処理するとしよう。fs` モジュールを使って読み取り可能なストリームを作成し、ファイルを少しずつ読み取ることができる。


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


ここで何が起こるのか？


1.fs.createReadStream()` は読み取り可能なストリームを作成します。

2.ファイルの一部が準備できると、ストリームは `data` イベントを発行し、データの「チャンク」（`Buffer`）を私たちに渡す。そのチャンクを表示する。

3.ファイル全体が読み込まれると、`end`イベントが発生する。

4.エラー（ファイルが存在しないなど）があると、`error`イベントが発生する。


こうすれば、巨大なファイルを一度にメモリに読み込むことなく読むことができる。


データを（バイナリではなく）人間が読める形式で送りたい場合は、ストリームのエンコーディングを指定することができる：


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


このコードは、ファイルを人間が読める形で印刷する。


### 書き込み可能なストリーム


書き込み可能なストリームは、データをチャンクごとにどこかに送ることができる。


以下はストリームを使って`target.txt`ファイルに書き込む例である：


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


こうなる：


1.fs.createWriteStream()` は書き込み可能なストリームを作成します。

2..write()`を使ってテキストを書き込む。

3.終わったら `.end()` を呼んでストリームを閉じる。

4.すべてのデータが書き込まれると、`finish`イベントが発生する。

5.何か問題が発生すると `error` イベントが発生する。


読み込み可能なストリームと同様、書き込み可能なストリームも、すべてを一度にメモリに保持する必要がないため、ビッグデータに適している。


### パイピング・ストリーム


ストリームの最もクールな点の1つは、**パイプ**でつなぐことができることだ。


```javascript
const fs = require("fs")

const readable = fs.createReadStream("bigfile.txt")
const writable = fs.createWriteStream("target.txt")

readable.pipe(writable)
```


ここだよ：



- 読み取り可能なストリームは `bigfile.txt` から読み取る。
- 書き込み可能なストリームは`copy.txt`に書き込む。
- .pipe()`は読み取り可能なストリームから書き込み可能なストリームに直接データを送る。


### 二重ストリーム


二重ストリームは読み書きの両方が可能である。一例として、ネットワークソケットがある。


net` モジュールを使った非常に簡単な例である：


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


この例では



- socket`オブジェクトは二重ストリームである。
- また、`write()`することもできるし、`data`イベントをリッスンすることもできる。


### ストリームを変換する


トランスフォーム・ストリームは、それを通過するデータも変更する二重ストリームである。


例えば、内蔵の `zlib` モジュールを使ってデータを圧縮したり解凍したりすることができる。


ここでは、トランスフォームストリームを使ってファイルを圧縮する方法を説明する：


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


そして減圧して戻す：


```javascript
const readable = fs.createReadStream("bigfile.txt.gz")
const unzip = zlib.createGunzip()
const writable = fs.createWriteStream("bigfile.txt")

readable.pipe(unzip).pipe(writable)

writable.on("finish", () => {
console.log("File decompressed.")
})
```


トランスフォームストリームは、圧縮、暗号化、ストリーミング中にファイルフォーマットを変更するなどのタスクに非常に便利です。


### 背圧


書き込み可能なストリームがデータ処理に時間がかかることがある。書き込み可能なストリームが処理できる速度よりも速くデータを書き込み可能なストリームにプッシュし続けると、問題が発生する可能性がある。これを**背圧**と呼ぶ。


書き込み可能なストリームで `.write()` メソッドを呼び出すと、ストリームに一時停止が必要かどうかを示すブール値が返される：


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


これは、リーダブルからライタブルへデータを手動でパイプし、背圧を手動で管理する例である。


通常は、背圧を自動的に処理する `.pipe()` メソッドを使ってデータをパイプする。


つまり、背圧を心配する必要があるのは、何らかの理由で`.write()`を手動で呼び出すときだけだ。


## 最終ノート

<chapterId>139e2ab8-df67-525a-85f0-5a2fa5e478f2</chapterId>


さて、レッスンに沿って進めば、NodeJSで簡単なプログラムを書けるようになるはずだ。


基本を学んだ後、いくつかの個人的なプロジェクトを作ることは、練習してより良いプログラマーになるための最良の方法だ。


重要なのは、コードを使って問題を解決することに挑戦することだ。


現代のプログラミング言語は信じられないほど強力であり、NodeJSはおそらく、あなたの旅のこの段階で実験するのに最適なツールボックスだろう。


幸運を祈る！


# 最終節


<partId>322624d8-6fbc-11f0-a67a-5b145f10afc1</partId>


## レビュー＆評価


<chapterId>3e93ac86-6fbc-11f0-8bae-9b2ed7914843</chapterId>

<isCourseReview>true</isCourseReview>

## 結論


<chapterId>49b3b9b2-6fbc-11f0-9870-5f5adcd3a0eb</chapterId>


<isCourseConclusion>true</isCourseConclusion>