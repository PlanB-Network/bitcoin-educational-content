---
name: JavaScript 和 NodeJS 基础
goal: 学习 JavaScript 编程基础和 NodeJS 开发，以构建实用的应用程序和工具。
objectives: 

  - 掌握 JavaScript 的基本语法、类型和控制流
  - 了解 JavaScript 中的函数、对象和类
  - 学习错误处理和调试技术
  - 了解 NodeJS 及其生态系统

---

# 开始您的开发之旅


欢迎学习 JavaScript 和 NodeJS 课程。


JavaScript 是世界上最流行的编程语言：它是现代浏览器的脚本语言，因此，如果不编写一些 JavaScript，基本上就无法构建现代网络应用程序；有了 NodeJS 运行时，它也可以在浏览器之外使用，创建直接在计算机上运行的脚本和应用程序。


本课程专为编程新手，或以前使用过其他语言但希望了解 JavaScript 如何工作（尤其是在 NodeJS 的背景下）的人设计。


课程结束时，您应该能够用 JavaScript 编写自己的程序，使用 NodeJS 标准库，安装和使用第三方软件包来构建有用的工具。


+++
# 基础 JavaScript

<partId>a617327c-e5a2-52ca-9380-c63f44623dd4</partId>


## 设置

<chapterId>ba05a290-1782-5268-87c9-62fd09590e05</chapterId>




JavaScript 程序只是（一个或多个）文本文件的集合，其中包含要由 JavaScript 运行时执行的命令。


这些文本文件的名称通常以`.js`文件扩展名结尾，如`my_script.js`、`my_program.js`等。


其中包含的命令是用 JavaScript 编程语言编写的。


JavaScript 运行时是执行这些文件的特殊程序。


![](assets/en/1.webp)


### NodeJS 运行时


最常见的 JavaScript 运行时是 NodeJS。


您的IDE可能已经包含它，或者您可能需要从[官方网站](https://nodejs.org/en/download)下载它。


下载页面将为您提供所有三种主要操作系统（OS）的说明：Windows、Linux 和 MacOS。前提是你知道如何在自己的操作系统中打开终端。


由于 NodeJS 适用于所有三种操作系统，因此您编写的程序将能在所有操作系统上执行（某些边缘情况除外）。


举例来说，这意味着您可以在 Windows PC 上用 JavaScript 编写一个简单的视频游戏，然后将它传给您的朋友，让他在 Mac 上运行。


![](assets/en/2.webp)














### 第一个程序（hello world）


传统上，在学习编程语言时，编写的第一个程序就是向控制台打印 "hello world!"。


创建名为 `my_js_code/` 的目录，并在其中创建名为 `main.js`的文件（这些名称是任意的）。


使用代码编辑器打开目录。


将此代码写入您的文件：


```javascript
console.log("hello world!")
```


打开终端，执行此命令运行程序：


```
node main.js
```


结果应该是


```
hello world!
```


### 发生了什么


在 JavaScript 中，一切都是 "对象"。


控制台 "是一个对象，用于调试程序。


`console.log` 是 `console` 中最常用的方法。它只会打印你传给它的任何参数。


您可以使用圆括号"() "向 `console.log` 传递参数。


例如，如果要打印数字 `1000`，只需写道


```javascript
console.log(1000)
```


然后执行


```
node main.js
```


在终端中执行（从现在起，本课程将假定您知道这是执行程序的方式）。


应打印


```
1000
```


您可以传递多种信息，例如


```javascript
console.log(16, 8, 1993)
```


这将打印


```
16 8 1993
```


## 变量和注释

<chapterId>23050ab7-343b-5edf-9d37-e4e782e27ce0</chapterId>


程序通常对数据执行操作。


变量就像我们用来存储数据的命名盒。通过变量，我们可以将数据与特定名称关联起来，以便日后使用该名称检索数据。


### `let` 声明


要在 JavaScript 中声明一个变量，我们可以使用 `let` 关键字。


在写下 `let` 之后，我们写下要给变量起的名字，然后是 `=` 符号，最后是要存储的值。


例如


```javascript
let age = 25

console.log(age)
```


变量名（技术上称为 "标识符"）通常可以包含字母、下划线 (`_`)、美元符号 (`$`) 和数字，但第一个字符不能是数字。


在上面的代码中，我们声明了一个名为 `age` 的变量，并在其中存储了值 `25`。


然后，我们使用 `console.log(age)` 打印该值。


如果使用 `node main.js` 运行此代码，输出结果将是


```
25
```


标识符对大小写敏感，这意味着小写和大写算作标识符的差异，例如


```javascript
let age = 25

let Age = 20

console.log(age)
```


将打印 25，因为它们被视为两个完全独立的变量！


您还可以在变量中存储字符串（文本）：


```javascript
let message = "hello again"

console.log(message)
```


这将打印出来：


```
hello again
```


和之前一样，我们使用 `console.log()` 来打印变量中存储的值。


现在，让我们一起来做这两件事：


```javascript
let age = 25

let message = "hello again"

console.log(age)

console.log(message)
```


运行该程序将打印


```
25
hello again
```

### 改派


用 `let` 声明的变量可以在创建后更改。


这就是所谓的重新分配。


```javascript
let score = 10

console.log(score)

score = 15

console.log(score)
```


首先，我们将 `10` 赋值给 `score`，然后打印出来。


然后，我们将 `score` 的值改为 `15` 并再次打印。


输出结果将是


```
10
15
```


当数值随时间变化时，比如在游戏中分数增加时，这个功能就非常有用。


让我们再增加一个变量：


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


这将打印出来：


```
10
Alice
20
Bob
```


如您所见，"分数 "和 "玩家 "都发生了变化。


### `const` 声明


但大多数情况下，我们不希望变量在创建后发生变化。为此，我们使用 `const`。


`const` 是 "常量 "的简称。一旦给 `const` 变量赋值，就不能更改。


```javascript
const pi = 3.14
console.log(pi)
```


打印


```
3.14
```


但如果你想这样做


```javascript
const pi = 3.14
console.log(pi)

pi = 99 // this line will cause an error
console.log(pi)
```


JavaScript 会给出类似的错误信息：


```
TypeError: Assignment to constant variable.
```


这是因为 `pi` 是使用 `const` 声明的，之后就不能更改其值了。这是在向 JavaScript 解释器传达一个信息：你不希望该变量发生变化。


这样做很有用，因为可以减少错误修改的机会。当程序变得非常庞大，拥有成千上万行代码时，就不可能同时跟上所有正在发生的事情（这正是我们使用计算机的主要原因，以执行我们无法用大脑计算的复杂过程），因此，像这样的限制就变得非常有用，可以使程序更具确定性。


除非我们确定以后要修改这些值，否则最好总是将它们声明为 `const`。


### JavaScript 中的注释


有时，我们想在代码中写下不被执行的注释。这就是注释。


程序运行时，注释会被忽略，但对于向自己或其他人解释事情很有用。


要写单行注释，使用 `//`


```javascript
// This is a comment
const x = 10 // This is also a comment
console.log(x)
```


这样仍然可以打印：


```
10
```


评论只是供人阅读的。


您还可以使用 `/*` 和 `*/` 写多行注释


```javascript
/*
This is a multi-line comment.
It can span several lines.
*/
const y = 20
console.log(y)
```


这将打印


```
20
```


评论将被忽略。


您可以使用注释为代码添加小注解，这样您就可以记住代码的作用以及为什么要这样写。它还可以帮助其他程序员理解代码。


## 基本类型：数字、字符串、布尔型

<chapterId>cfdb04f6-21a8-5143-bbf9-7aaae04962f0</chapterId>


在 JavaScript 中，"类型 "会告诉你一个值是什么类型的数据。


Javascript 有几种基本类型，在本节中我们将探讨其中一些类型。


### 数字和算术运算


我们要介绍的第一个类型是 "数字"。


JavaScript 中的数字可以是整数（如 `5`）或小数（如 `3.14`）。


您可以用它们进行算术运算：加法、减法、乘法和除法。


下面是一个基本例子：


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


这将打印出来：


```
15
5
50
2
```


您还可以使用括号"() "来控制操作顺序：


```javascript
const result = (2 + 3) * 4
console.log(result)
```


打印


```
20
```


如果没有括号，就会变成 "2 + 3 * 4"，也就是 "2 + 3 * 4"：


```javascript
const result = 2 + 3 * 4
console.log(result)
```


这样就可以打印了：


```
14
```


因为在普通数学中，乘法发生在加法之前。


### 字符串和插值


我们要介绍的第二种 JavaScript 类型是 "字符串"。


字符串是文本片段。您可以使用单引号`'...'`或双引号`"..."`来创建它们。


```javascript
const greeting = "hello"
const name = 'Bob'
console.log(greeting)
console.log(name)
```


打印


```
hello
Bob
```


要组合字符串，可以使用 `+` 操作符：


```javascript
const greeting = "hello"
const space = " "
const name = "Bob"

const fullGreeting = greeting + space + name
console.log(fullGreeting)
```


这将打印出来：


```
hello Bob
```


不过，还有一种更好的组合字符串的方法，称为**字符串插值**。您可以使用反标来声明字符串 ``...`` 并在字符串内使用 `${...}` 写入变量：


```javascript
const greeting = "hello"
const name = "Bob"

const fullGreeting = `${greeting} ${name}`
console.log(fullGreeting)
```


这也会打印出来：


```
hello Bob
```


您可以在`${...}`内包含任何表达式：


```javascript
const age = 30
console.log(`Next year, I will be ${age + 1} years old.`)
```


打印


```
Next year, I will be 31 years old.
```


插值在现代 JavaScript 中非常常见。


### 布尔、比较和逻辑运算


我们要介绍的第三种类型是 "布尔"。它是以发明布尔逻辑的数学家乔治-布尔的名字命名的。


布尔值很简单：只有两个可能的值，"真 "和 "假"。


您可以将它们存储在变量中：


```javascript
const theSkyIsBlue = true
const thisCourseIsBad = false

console.log(theSkyIsBlue)
console.log(thisCourseIsBad)
```


打印


```
true
false
```


您可以使用逻辑运算符组合布尔值：



- &&`表示 "和"，只有当两个**值都为 "true "时才返回 "true"，否则返回 "false"。
- ||` 表示 "或"，如果**个值中至少有一个**是 "真"，它将返回 "true"，否则（如果它们都是假）将返回 "false"。
- !"表示 "不是"，应用于布尔值之前，会将布尔值翻转：如果布尔值为 "true"，则返回 "false"，反之亦然。


![](assets/en/3.webp)


例如


```javascript
const isSunny = true
const isWarm = true

console.log(isSunny && isWarm)  // true
console.log(isSunny || isWarm)  // true
console.log(!isSunny)           // false
```


在 JavaScript 中，您可以使用`>`、`<`、`===`和`！==`等运算符对数值进行比较。这些比较的结果总是布尔值。


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


Javascript 还用 `>=` 表示 "更大或相等"，用 `<=` 表示 "更小或相等"。


布尔运算、比较运算和逻辑运算符经常在程序中结合使用，以声明复杂的条件，例如确保 "电子邮件已到达，并且包含我需要的图片，或者电子邮件的长度超过 10000 个字符"。稍后您会发现，这些都是构建程序逻辑的基本构件。


## 数组、空、未定义

<chapterId>7bf18183-5eae-53ed-83d2-b04982145d81</chapterId>


在本节中，我们将介绍另外三种在 JavaScript 程序中非常常见的类型：



- 数组**：数值序列
- undefined**：一个特殊值，表示 "未分配任何内容"。
- null**：另一个特殊值，表示 "故意为空"。


### 数组和索引访问


数组**是一种可以在列表中保存多个值的类型。


使用方括号"[]"创建数组，并用逗号分隔项目。


下面是一个基本例子：


```javascript
const numbers = [10, 2, 88]
console.log(numbers)
```


打印


```
[ 10, 2, 88 ]
```


你可以在数组中存储任何东西，而不仅仅是数字：


```javascript
const things = ["apple", 42, true]
console.log(things)
```


打印


```
[ 'apple', 42, true ]
```


要访问数组中的特定项目，我们需要使用**索引**。索引是项目的位置，从 **0** 开始。


因此，在这个阵列中


```javascript
const colors = ["red", "green", "blue"]
```



- colors[0]`是`"red"`。
- 颜色[1]`是`"Green"`。
- colors[2]`是`"blue"`。


让我们试试：


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[0])
console.log(colors[1])
console.log(colors[2])
```


这将打印出来：


```
red
green
blue
```


您可以为数组的特定索引赋值


```javascript
const colors = ["red", "green", "blue"]

colors[1] = "yellow"

console.log(colors)
```


这将打印出来：


```
[ 'red', 'yellow', 'blue' ]
```


您可以使用任何自然数作为索引，甚至是存储在变量中的自然数


```javascript

const i = 1
const colors = ["red", "green", "blue"]
console.log(colors[i])
```


这将打印出来：


```
green
```


但如果尝试访问一个不存在的索引，就会得到`未定义`的结果：


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[3])
```


打印


```
undefined
```


那是什么？


### 未定义


特殊值 `undefined` 表示 "未赋值"。


如果创建了一个变量，但没有给它赋值，它将是 "未定义 "的：


```javascript
const name
console.log(name)
```


打印


```
undefined
```


由于我们没有为 `name` 赋值，JavaScript 默认将其设置为 `undefined`。


如前所述，当访问一个不存在的数组索引时，也会出现 "未定义 "的情况：


```javascript
const fruits = ["banana", "apple"]
console.log(fruits[2]) // There is no index 2
```


打印


```
undefined
```


### null "以及如何处理它


`null`也是一个特殊值。它的意思是 "这里什么都没有，我故意这样做的"。


与自动设置的 `undefined` 不同，`null` 是由用户自己设置的。


例如


```javascript
const currentUser = null
console.log(currentUser)
```


打印


```
null
```


为什么使用 `null`？也许你期望稍后得到一个值，但它还没有准备好：


```javascript
let winner = null

// Later in the program:
winner = "Alice"

console.log(winner)
```


打印


```
Alice
```


因此，"null "在你想说 "这里稍后应该会有东西，但现在是空的 "时非常有用。


## 块和控制流

<chapterId>be985168-2636-5b0d-a48f-ac1bbfbff8a7</chapterId>


到目前为止，我们编写的大部分代码都是一行接一行地运行。


但是，当我们编写代码时，我们可以控制它的执行顺序。


这就是**控制流**。


让我们从了解区块和范围开始。


### 全球范围


我们声明的每个变量都存在于一个**范围**中，这意味着代码中已知变量的区域。


如果在任何代码块之外声明变量，该变量将存在于**全局作用域**。


```javascript
const color = "blue"
console.log(color)
```


变量 `color` 位于全局作用域，因此可以从文件中的任何地方访问它。


如果添加更多行：


```javascript
const color = "blue"
console.log(color)

const size = "large"
console.log(color)
console.log(size)
```


颜色 "和 "大小 "都是全局变量。它们在文件中随处可用。


但区块内部会发生什么呢？


### 区块和局部范围


**块**是由大括号"{}"包围的一段代码。


在代码块内用 `let` 或 `const` 声明的变量只**在该代码块内存在。


```javascript
{
const message = "inside block"
console.log(message)
}
```


打印


```
inside block
```


但如果你试试这个


```javascript
{
const message = "inside block"
}
console.log(message) // Error!
```


JavaScript 会给出类似的错误信息：


```
ReferenceError: message is not defined
```


这是因为 `message` 是在代码块内声明的，在代码块外并不存在。


这意味着我们可以使用代码块来隔离部分代码，并确保 "发生在代码块中的事情将保留在代码块中"（有点像拉斯维加斯）。


用代码块来组织代码，还能让我们用控制流结构来组织程序的执行，如 "if


### 如果"、"否则


有时，我们只想在某些条件为真的情况下运行代码。这就是 `if` 语句的作用。


```javascript
const myAge = 20

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


打印


```
Am I an adult?
Yes I am!
```


可以看到，代码比较了 `myAge` 和 `18`。

在这种情况下，运算符 `>=` 返回 `true`，因此程序块被执行。

如果条件不是 "true"，程序块不会被执行。


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


打印


```
Am I an adult?
```


您可以添加一个 `else` 块来处理相反的情况：


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
} else {
console.log("No, I am not.")
}
```


打印


```
Am I an adult?
No, I am not.
```


if "和 "else "代码块仍然是代码块，因此在它们内部声明的变量在外部并不存在。


如果我们想确定某件事情***不真实，我们能做些什么呢？


正如之前所讨论的，JavaScript 有一个 "not "操作符，可以翻转布尔值。因此，我们可以使用


```javascript
const myAge = 17

const adult = myAge >= 18

console.log("Am I an adult?")

if (!adult) {
console.log("No, I am not.")
}
```

这仍然可以打印：


```
Am I an adult?
No, I am not.
```

因为我们使用了 `!` 操作符来反转 `adult` 变量。


`if (!adult) {...}` 应改为 "if not adult..."


使用块、逻辑和比较运算符，我们可以通过定义变量来组织程序的执行，这些变量必须为 "真"（或 "假"），才能发生某些事情。


### 同时"、"中断"、"继续


只要*条件为真，`while`循环就会重复代码。


```javascript
let count = 0

while (count < 3) {
console.log("Count is", count)
count = count + 1
}
console.log("the loop is over!")
```


打印


```
Count is 0
Count is 1
Count is 2
the loop is over!
```


当 `count` 变成 3 时，循环停止。


您可以使用 `break` 提前停止循环：


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


打印


```
0
1
2
```


因为当数字变为 "3 "时，"if "代码块就会被执行并停止循环。


您可以使用 `continue` 跳过循环的其余部分：


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


打印


```
1
2
4
5
```


因为当数字是 "3 "时，"继续 "会使程序跳过打印数字的那一行。


### 为......的......`


如果您有一个数组，并想对其中的每个项做一些操作，您可以使用 `for ... of ...{...}`.


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const fruit of fruits) {
console.log(fruit)
}
```


打印


```
apple
banana
cherry
```

数组中的每个元素都将执行一次该代码块。


这里的 `fruit` 是一个新变量，它获取数组中每个项目的值，以便在代码块内对其进行操作。


### 为......在......`


您可以使用 `for ... in` 循环数组的键（索引）：


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(index)
}
```


打印


```
0
1
2
```


您也可以使用索引来获取值：


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(fruits[index])
}
```


打印效果与 `for ... of` 相同：


```
apple
banana
cherry
```


实际上，对于数组，您应该更喜欢使用 `for ...of`，因为它更简单、更干净。


### 有界环路


有时，我们需要循环特定的次数，或者编写一段代码来重复一个代码块，同时跟踪某些内容。

这就是有界 "for "循环的作用。

有界循环通常包含三个条件，以分号`;`分隔，如`(... ; ... ; ....)`。


```javascript
for (let i = 0; i < 3; i = i + 1) {
console.log(i)
}
```


打印


```
0
1
2
```


让我们来解释一下：



- `let i = 0`：声明一个要在代码块中使用的变量（在本例中，它是一个从 0 开始的计数器）
- `i < 3`：声明要执行代码块的条件为 `true`（本例中为 "当 `i` 小于 3 时重复"）。
- `i = i + 1`：声明每次执行代码块后要运行的代码（本例中为 "将 `i` 增加 1"）。


正如你所看到的，有界循环可以为重复执行一段代码声明更复杂的条件，但大多数情况下并无必要。


### 区块标签


如果您需要编写更复杂的控制流，JavaScript 可以让您使用**标签**来命名一个块，该标签可以被 `break` 或 `continue` 使用，用于指定**跳回的位置。


例如


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


打印


```
Inside outer block
Inside inner block
Done
```


我们使用 `break outer` 来完全退出 `outer` 块。


您还可以给循环贴标签。举个例子


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

这是一个非常无聊的例子，但希望它能阐明（偶尔）对标签的需求。


## 功能介绍

<chapterId>cc324715-09c2-5cf7-9e6f-47a6f16bc04d</chapterId>


随着程序的发展，您经常需要**重复使用**段代码。


这就是**函数**的作用：它可以让你把一些代码组合在一起，给它一个名字，然后随时运行它。


### 功能声明


要声明一个函数，我们可以使用 `function` 关键字。然后，我们给它一个名称、一对包含参数的括号 `()` 和一个要执行的代码块 `{}`。让我们从一个不带参数的函数开始：


```javascript
function sayHello () {console.log(`Hello!`) }
```


这段代码***声明了***函数，但尚未***运行它。


### 功能调用


要运行（或 "调用"）函数，只需在函数名称后写入括号：


```javascript
function sayHello () {console.log(`Hello!`) }
sayHello()
```


打印


```
Hello!
```


您可以随意多次调用该函数：


```javascript
function sayHello() {
console.log("Hello!")
}

sayHello()
sayHello()
```


打印


```
Hello!
Hello!
```


函数内部的代码只有在你调用它时才会运行。


### 函数参数（函数的输入）


有时，您希望函数在输入某些内容后工作。为此，您可以在括号内添加**参数**。


例如


```javascript
function sayHelloTo (friend) {
console.log(`Hello ${friend}!`)
}
```


现在，这个函数需要**个参数**，名为 "friend"。


调用函数时，可以传递一个值：


```javascript
sayHelloTo("Tommy")
```


打印


```
Hello Tommy!
```


您可以用不同的名称再次调用该函数：


```javascript
sayHelloTo("Sam")
```


打印


```
Hello Sam!
```


您传入的值将替换函数内部的 `friend` 变量。


您也可以使用多个参数：


```javascript
function greetTwoPeople(person1, person2) {
console.log(`Hello ${person1} and ${person2}!`)
}

greetTwoPeople("Lina", "Marco")
```


打印


```
Hello Lina and Marco!
```


### return"（函数的输出）


函数也可以**返回**值。这意味着，无论函数被调用到哪里，都会返回一个值。


这里有一个简单的例子：


```javascript
function getNumber() {
return 42
}

const result = getNumber()
console.log(result)
```


打印


```
42
```


函数 `getNumber()` 返回 `42`，我们将其存储在 `result` 中，然后打印出来。


您也可以返回自己计算的结果：


```javascript
function add(a, b) {
return a + b
}

const result = add(2, 3)
console.log(result)
```


打印


```
5
```


一旦`return`了一个值，函数就停止了。在该代码块中，"return "之后的任何内容都不会发生。


```javascript
function saySomething() {

return "hi"

console.log("this never runs")

}

const message = saySomething()
console.log(message)
```


只能打印：


```
hi
```


因为只会返回 `"hi"。console.log（"this never runs"）"行被跳过。


你可以把函数看作是小型子程序。每个函数都可以接收一些输入，对其进行处理，并返回一些输出。


如果我们试图使用一个函数的返回值，但该函数没有返回任何内容，会发生什么情况？


```javascript
function doesNothing () {}

const x = doesNothing()

console.log(x)
```

这将打印 `undefined`。没有返回任何内容的函数的返回值是 `undefined`。


## 对象和类别

<chapterId>26689f25-8212-5057-8c21-3a05eee0ac75</chapterId>


JavaScript 通常被称为面向对象语言。


这意味着，它可以通过将值和函数归类为**对象**来帮助你组织代码。


### 什么是 "对象"？


一个对象可以包含数据和对数据进行操作的函数。当一个函数被放入一个对象时，我们称之为 "方法"。


我们看到的第一个对象是 `console` 对象。该对象包含多种方法，用于在屏幕上打印内容和调试程序。


它甚至可以自己打印；您可以


```javascript
console.log(console)
```


就会打印出其中包含的方法列表。例如，在我的机器上它会打印


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


正如你所看到的，它有很多方法可以用来调试！


Javascript 为我们提供了创建新对象的不同方法，这些对象可以做任何我们想让它们做的事情。


### 创建对象


创建对象最简单的方法就是使用**大括号** `{}`将数据和函数分组。


这就是我们所说的**匿名对象**


```javascript
const cat = {
name: "Whiskers",
age: 3
}
```


这会创建一个对象，并将其存储在名为 `cat` 的变量中。


对象有两个**属性**：



- name "的值为 "Whiskers"。
- 年龄 "值为 "3


印出来吧


```javascript
console.log(cat)
```


打印


```
{ name: 'Whiskers', age: 3 }
```


您可以使用点从对象中获取属性，如在 `objectName.propertyName` 中：


```javascript
console.log(cat.name)  // prints "Whiskers"
console.log(cat.age)   // prints 3
```


您还可以**更改**属性：


```javascript
cat.age = 4
console.log(cat.age)  // now it prints 4
```


正如你所看到的，即使一个对象被定义为 `const`，你仍然可以修改它所包含的数据。


对于对象，`const` 只会阻止你覆盖整个对象：


```javascript
const cat = {
name: "Whiskers",
age: 3
}

cat.age = 5 // this works

cat = 5 // this throws an error, you're trying to reassign the whole object

```


如前所述，对象也可以容纳**函数**，当函数是对象的一部分时，我们称之为**方法**。


这里有一个例子：


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log("Meow!")
}
}
```


该物体具有



- 名称 "属性
- 一个 "speak() "方法


让我们调用该方法：


```javascript
cat.speak()
```


它可以打印：


```
Meow!
```


方法可以通过关键字 `this` 使用对象包含的数据。

this "指当前对象。在本例中，它将用于打印猫的名字：


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log(`${this.name} says meow!`)
}
}

cat.speak()
```


打印


```
Whiskers says meow!
```


这个词 "this "的意思是 "这个对象"......在这里是指 "猫 "对象。



当你只想快速、简单地创建一些对象时，这类对象就很不错。但如果你需要创建**多具有相同结构的**个对象，还有更好的办法，这就是**类**的用武之地。


### 类和构造函数


一个**类**就像一个蓝图。它告诉 JavaScript 如何创建某种对象。


您可以使用关键字 "class"（类）定义一个类，然后是类名和大括号"{}"块。


```javascript
class Dog {}
```


按照惯例，班级通常以大写字母开头。


您可以使用 `new` 创建一个类的新对象：


```javascript
const hachiko = new Dog()
```


尝试打印对象：

```javascript
class Dog {}

const myDog = new Dog()

console.log(myDog)
```


您将获得


```
Dog {}
```


正如你所看到的，Dog 类是空的，所以 `myDog` 对象也是空的。


我们可以通过添加 "构造函数 "来定义 Dog 对象应包含的属性。


构造函数是在创建（或 "构造"）新对象时运行的特殊函数。


```javascript
class Dog {
constructor() { }
}
```


我们希望每个 Dog 都有一个名字，因此我们在函数中添加了一个 `name` 参数：


```javascript
class Dog {
constructor(name) { }
}
```


然后，我们使用 `this` 来声明 `name` 是我们正在构建的 `Dog` 对象的 `name` 名称


```javascript
class Dog {
constructor(name) {
this.name = name
}}
```


让我们现在就尝试使用它：


```javascript
class Dog {
constructor(name) {
this.name = name
}
}

const myDog = new Dog("hachiko")

console.log(myDog)
```


打印内容如下


```
Dog { name: 'hachiko' }
```


如你所见，"constructor "方法接收你在执行 "new Dog() "时传递给类的参数，并使用这些参数来构建对象。


让我们来分析一下：



- `class Dog` 定义了 Dog 类。
- `constructor(name)` 在创建对象时设置对象。
- `this.name = name` 将值存储在新对象中。
- `new Dog("hachiko")` 从类中创建一个新对象，其 `name` 属性设置为 `"hachiko"。


现在，让我们为我们的类添加一个方法：


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


这将打印


```javascript
hachiko says barf!
```


如果我们对两个不同实例的 Dog



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


我们得到


```
hachiko says barf!
bobby says barf!
```


speak()`方法使用它所调用的 "Dog "的 "name "属性。


这就是类存在的主要原因：类允许我们定义一系列对数据进行操作的方法，然后创建共享相同数据 "形状 "的多个对象。


当我们调用其中一个对象上的方法时，它将对*该特定对象*所持有的数据进行操作。


### 改变物体的形状


JavaScript 中的对象非常灵活。即使创建了一个对象，您仍然可以添加新属性或删除现有属性。


这是允许的，但要谨慎使用。


让我们从简单的 `Dog` 类开始：


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


此时，`myDog` 只有一个属性：name`。创建后，我们仍可添加新属性：


```javascript
myDog.age = 5

console.log(myDog.age) // prints 5
```


我们还可以添加一个新方法：


```javascript
myDog.jump = function () {
console.log(`${this.name} jumps!`)
}

myDog.jump() // Fido jumps!
```


我们还可以使用 `delete` 关键字删除属性。


```javascript
delete myDog.name

console.log(myDog.name) // prints 'undefined'
```


这种方法可行，但有一点很重要：当对象始终保持相同属性时，V8（用于 Node.js 和 Chrome 浏览器）等 JavaScript 引擎的运行速度会更快。如果在对象创建后添加或删除属性，运行速度会减慢。


在小型程序中，这一点并不重要。但在大型项目（如游戏）中，最好从一开始就在构造函数中列出所有属性，即使你不会马上使用它们。这样可以保持对象形状的稳定，有助于代码更快地运行。


例如，可以用以下方式代替


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


两个版本都可以使用，但第二个版本的性能更好。你可以预先告诉引擎每个对象将具有哪些属性，这样引擎就可以进行相应的优化。


JavaScript 允许您自由重塑对象，但在使用类时，最好提前规划好对象的形状。



### 使用`extends`和`super()`进行继承


有时，你想创建一个几乎与另一个类相同的类，但又有一些额外的功能。


与修改对象的形状（如前所述，这对性能并非最佳）或从头开始重写一个新类相比，JavaScript 让你可以使用一种叫做 ** 继承**的方法。


继承意味着一个类可以**扩展**另一个类。新类可以获得旧类的所有属性和方法，你还可以添加或更改你需要的内容。


假设我们有一个名为 "Vehicle "的基类：


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


现在我们要创建一个 "汽车 "类。汽车是一种交通工具，但我们可能希望它有一些额外的功能，或者在启动时发出不同的信息。我们可以使用 `extends` 来代替重写所有内容：


```javascript
class Car extends Vehicle {
start() {
console.log(`${this.brand} car is ready to drive!`)
}
}
```


汽车 "类现在**继承了 "车辆 "的所有内容。它获得了 `brand` 属性，我们还用自己的版本替换了 `start()` 方法。


![](assets/en/4.webp)


让我们试一试：


```javascript
const myCar = new Car("Toyota")
myCar.start()
```


打印


```
Toyota car is ready to drive!
```


尽管 `Car` 没有自己的构造函数，但它仍然使用 `Vehicle` 的构造函数。但如果我们想在 `Car` 中编写一个自定义构造函数，我们可以这样做，只需使用 `super()`调用其父类的构造函数即可。


方法如下


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



打印


```
Toyota Corolla is ready to drive!
```


总而言之



- 扩展 "表示一个类基于另一个类。
- super() "用于调用扩展类的构造函数。
- 新类将获得原类的所有属性和方法。
- 您可以**覆盖**方法（如 `start()`），让它们做不同的事情。


当你有几种相似的东西（如汽车、卡车和自行车），你希望它们共享代码，但仍以各自的方式运行时，这种方法很有用。


### 实例


`instanceof` 关键字会检查对象是否由某个类创建。


假设我们有一个名为 "用户 "的类：


```javascript
class User {
constructor(username) {
this.username = username
}
}

const regularUser = new User("julia123")

console.log(regularUser instanceof User)
```


打印


```
true
```


确认 `regularUser` 是一个 `User`。这是因为 `regularUser` 是使用 `User` 类创建的。


它也适用于**继承**类。例如，这里有一个扩展了 `User` 的 `Admin` 类：


```javascript
class Admin extends User {}

const ourAdmin = new Admin("admin42")

console.log(ourAdmin instanceof Admin)   // true
console.log(ourAdmin instanceof User)    // true
```


这两行都返回 `true`。这是因为 `Admin` 是 `User` 的子类，因此 `ourAdmin` 既是 `Admin` 也是 `User`


# 中级 JavaScript

<partId>243f63ab-4f34-5c30-80cb-84ef46f6761d</partId>


## 错误处理

<chapterId>d0206bc5-d386-5e7f-9917-5803f392448c</chapterId>


当你编写更复杂的 JavaScript 程序时，你会遇到**错误**。这些是出错的意外情况。也许某个变量是 "未定义 "的，但你却试图使用它，或者某些代码接收到了错误的输入类型。


如果不正确处理这些错误，我们的程序可能会崩溃或出现不可预知的行为。JavaScript 提供了检测和管理这些错误的工具，因此我们可以更优雅地处理这些错误。


### 常见错误：访问 `undefined` 上的值


以下是导致错误的常见情况：


```javascript
const user = undefined
console.log(user.name)
```


如果运行这段代码，就会出现类似下面的错误：


```
TypeError: Cannot read properties of undefined (reading 'name')
```


这是 JavaScript 在告诉你"嘿，你试图从`未定义`的东西中获取`name`属性，这不合理"。正如你所看到的，当这种错误发生时，程序就会停止运行，除非你专门编写了代码来捕捉和处理它。


### 抛出错误


有时，您想在代码中手动**出错**。在这种情况下，就需要使用`throw`关键字。


```javascript
throw new Error("This is a custom error message")
```


这将立即停止程序并打印：


```
Uncaught Error: This is a custom error message
```


您可以使用 `throw` 在程序中强制执行规则。例如


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


第二次调用会导致错误，因为本例中不允许除以零。


### 用 "try...catch "捕捉错误


如果不想让程序在出错时崩溃，可以使用 "try...catch "块来捕获错误。当你想让程序在出现故障时**继续运行**时，这很有帮助。


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log("Oops! Something went wrong.")
}
```


输出：


```
Oops! Something went wrong.
```


具体操作如下



- 首先尝试`try`代码块内的代码。
- 如果出现错误，JavaScript 会**跳转到 "catch "块**，跳过 "try "块的其余部分。
- 捕获 "块会接收到错误信息，因此您可以将其打印出来，或以其他方式进行处理，例如


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log(`The message of the error was: "${error.message}"`)
}
```


输出：


```
The message of the error was: "Cannot read properties of undefined (reading 'name')"
```


### 最后 "区块


您还可以添加一个 `finally` 块。这是**始终运行**的代码，无论是否出错。


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


输出：


```
Trying something risky...
Caught the error: Uh oh!
This will run no matter what.
```


## 避免虫子

<chapterId>db12d9f6-5806-514c-998e-0ae24805104e</chapterId>


本章将介绍 JavaScript 中一些最常见的陷阱，以及如何避免这些陷阱。


### 无声明的 `var` 和 Assignment


在较早的 JavaScript 代码中，通常使用 `var` 关键字来声明变量。与已学过的 `let` 和 `const` 不同，`var` 可能会有令人困惑的行为。


例如


```javascript
{
var message = "hello"
}
console.log(message)
```


你可能以为 `message` 只存在于代码块内部，但事实并非如此。`var` 忽略了代码块的作用域，它使变量在整个函数或文件中都可用。


这可能会导致意想不到的行为，尤其是在大型程序中。因此，现代 JavaScript 代码应始终使用 `let` 或 `const` 而不是 `var`。


更糟糕的是，JavaScript 允许你在完全不声明变量的情况下为变量赋值**：


```javascript
function greet() {
user = "Alice"
}
greet()
console.log(user) // prints "Alice"
```


这会在没有任何声明的情况下创建一个新的全局变量 `name`。这种情况可能无声无息地发生，并导致需要追踪的 bug，尤其是如果只是一个错字。请始终使用 `let` 或 `const` 声明变量。


### 弱类型系统


JavaScript 是弱类型的，也就是说，如果需要，它会自动将值从一种类型转换为另一种类型。这就是所谓的类型强制，虽然很方便，但经常会导致混乱的结果。


例如


```javascript
console.log("5" + 1)    // "51"
console.log("5" - 1)    // 4
console.log(true + 1)   // 2
console.log(null + 1)   // 1
```


在这些示例中，JavaScript 会尝试猜测你的意思。有时它会将字符串转换成数字，或将布尔值转换成数字，或将字符串转换成字符串。这会使你的代码出现意想不到的行为。


了解 JavaScript 的弱类型系统非常重要。当事情开始变得奇怪时，可能是由于意外的类型强制造成的。


### `"严格使用"`


您可以启用更严格的模式，将一些无声错误变成真正的错误，并阻止您使用语言中一些更危险的功能。


要启用这种更严格的模式，请在文件或函数的顶部添加这一行：


```javascript
"use strict"
```


例如


```javascript
"use strict"
name = "Alice" // ReferenceError: name is not defined
```


如果没有严格模式，JavaScript 会静默地创建一个名为 `name` 的全局变量。但在严格模式下，这将成为一个真正的错误，有助于您更早地发现错误。


严格模式还能禁用 JavaScript 的一些过时功能，使代码更易于优化和维护。


## 价值与参考

<chapterId>bb898425-dc2f-5e5c-864b-0cb7a4a9aea9</chapterId>


JavaScript 对不同类型的值有不同的处理方式。


有些值在赋值给变量时会被**复制**。


当你将其他变量赋值给一个新变量时，它们是**共享**的，因此如果你改变了其中一个变量，另一个变量也会随之改变。


### 按值传递


当值被**通过时，JavaScript 会对其进行**复制。


因此，如果更改其中一个，不会影响另一个。


这种情况发生在原始类型中，例如



- 人数
- 字符串
- 布尔型（`真`和`假）
- 空
- 未定义


我们来看一个例子：


```javascript
let a = 5
let b = a

b = 10

console.log(a) // 5
console.log(b) // 10
```


我们给了 `b` `a` 的值，但又把 `b` 改成了 `10`。


由于数字是按值传递的，JavaScript 将 `5` 复制到了 `b`。b` 中的 `5` 与 a` 中的原始 `5` 无关，因此更改 b` 的值对 a` 没有影响。


让我们用字符串来试试：


```javascript
let name1 = "Alice"
let name2 = name1

name2 = "Bob"

console.log(name1) // Alice
console.log(name2) // Bob
```


同样，更改 `name2` 不会影响 `name1`，因为字符串也是通过值传递的。


将基元传递给函数时也会发生同样的情况：基元会被复制。因此，函数无法改变原型。


```javascript
function plusOne(x) {
x = x + 1
}

let number = 5

plusOne(number)

console.log(number) // 5
```


尽管在函数 `x` 中添加了 `1`，但原来的 `number` 并没有改变。


这是因为函数中只传递了一个**副本。


### 通过引用传递


对象是通过引用**传递的。


这就意味着，JavaScript 不会复制变量，而只是传递一个**引用**，如果你修改了它，指向它的所有其他变量也会看到变化。


例如


```javascript
const person1 = { name: "Alice" }
const person2 = person1

person2.name = "Bob"

console.log(person1.name) // Bob
console.log(person2.name) // Bob
```


person1 "和 "person2 "都指向内存中的同一个对象。


因此，当我们更改 `person2.name` 时，我们也更改了 `person1.name` ，因为他们都在查看同一个东西。


数组是对象，所以让我们用数组来做同样的尝试：


```javascript
const list1 = [1, 2, 3]
const list2 = list1

list2.push(4)

console.log(list1) // [1, 2, 3, 4]
console.log(list2) // [1, 2, 3, 4]
```


我们把 `4` 推到了 `list2` 中，但 `list1` 也受到了影响，因为它们都引用了同一个数组。


让我们看看将对象传递给函数时会发生什么：


```javascript
function rename(user) {
user.name = "Charlie"
}

const person = { name: "Dana" }

rename(person)

console.log(person.name) // Charlie
```


函数改变了对象！这是因为它接收到了对原始 `person` 对象的**引用。


它没有得到副本。它获得了访问原始对象的权限，并因此获得了修改原始对象的能力。


记住这一区别非常重要，否则我们的代码可能会出现与预期不同的行为。例如，我们在编写函数时可能希望它不会修改接收到的参数，但后来发现它实际上修改了这些参数（因为它们是对象，所以是通过引用传递的）。


## 使用函数

<chapterId>e0d277a8-c642-5af7-9e53-dee27c811967</chapterId>


您已经学习了如何在 JavaScript 中声明和使用函数。但是，JavaScript 还为您提供了更多工具，让您能以强大的方式使用函数。


### 箭头功能


箭头函数是一种更简短的函数书写方式。我们不使用 `function` 关键字，而是使用箭头 (`=>`)。


这是一个正常功能：


```javascript
function greet(name) {
return `Hello, ${name}!`
}
```


箭头版本是这样的


```javascript
const greet = (name) => {
return `Hello, ${name}!`
}
```


如果函数只有**行**，可以跳过大括号并`return`：


```javascript
const greet = (name) => `Hello, ${name}!`
```


如果函数只有一个参数**，甚至可以省略参数周围的括号：


```javascript
const greet = name => `Hello, ${name}!`
```


箭头函数在现代 JavaScript 中非常常见，因为它们可以用更少的模板来表达简单的函数。


### 默认参数


有时，如果没有参数传递，您希望函数具有**默认值**。


你可以这样做


```javascript
function sayHello(name = "friend") {
console.log(`Hello, ${name}!`)
}

sayHello("Alice") // Hello, Alice!
sayHello()        // Hello, friend!
```


如果没有传入任何信息，则使用默认值 `"friend"。


### 展期参数 (`...`)


如果您的函数需要多个参数，该怎么办？


您可以使用 ** 分布运算符** (`...`) 将它们集中到一个数组中：


```javascript
function logAll(...items) {
console.log(items)
}

logAll(1, 2, 3) // [1, 2, 3]
logAll("a", "b") // ["a", "b"]
```


然后，您可以使用循环来处理每个项目：


```javascript
function logEach(...items) {
for (const item of items) {
console.log(item)
}
}
```


当不知道要传递多少个参数时，扩展运算符就很有用。


### 高阶函数


一个**高阶函数**是这样一个函数：



- 将另一个函数作为输入
- 和/或返回一个函数作为输出


这里有一个简单的例子：


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


打印


```
Hello, friend!
Hello, friend!
```


我们可以向它传递一个箭头函数：


```javascript
runTwice(
() => console.log("Hello!")
)
```


打印


```
Hello!
Hello!
```


您还可以编写**返回**其他函数的函数：


```javascript
function makeGreeter(name) {
return () => console.log(`Hi, ${name}`)
}

const greetAlice = makeGreeter("Alice")
const greetBob = makeGreeter("Bob")

greetAlice() // Hi, Alice
greetBob() // Hi, Bob
```


makeGreeter "函数是一个用于构建其他函数的函数。它接收一个字符串并返回一个新函数，该函数在其 `console.log` 调用中使用该字符串。


这种模式非常强大，因为它允许你在函数中留下 "漏洞"，以后再用你需要的行为来填补。


### map()`、`filter()`、`reduce()


JavaScript 为数组提供了一些有用的内置方法。


这些方法将函数作为参数，因此它们也是高阶函数。


map()`将数组中的每个项目转换成其他项目。


例如


```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map(x => x * 2)

console.log(doubled) // [2, 4, 6]
```


每个数字都加倍，结果是一个新数组。


如果数组中的项目没有通过测试，`filter()` 会将其从数组中删除。


例如


```javascript
const numbers = [1, 2, 3, 4, 5]
const numbersGreaterThanTwo = numbers.filter(x => x > 2)

console.log(numbersGreaterThanTwo) // [3, 4, 5]
```


只保留 `x > 2` 条件返回 ` true` 的数组条目。


`reduce()` 用于将数组中的所有项目合并为一个值。


例如


```javascript
const numbers = [1, 2, 3, 4]
const total = numbers.reduce((current, next) => current + next)

console.log(total) // 10
```


`reduce` 遍历数组，在本例中，在 `1` 和 `2` 之间应用 `+` 操作符，然后在结果 `3` 和 `3` 之间应用 `+` 操作符，然后在结果 `6` 和 `4` 之间应用 `+` 操作符，直到得到数组所有条目的总和（即 10）。


你可以使用 `reduce()` 来做很多事情，比如合计、平均或逐步建立新值。


这些方法（"map"、"filter"、"reduce"）是无需手动循环即可处理数据的强大工具。


您甚至可以将它们组合成一个操作链，就像这样：


```javascript
const numbers = [1, 2, 3, 4, 5]

const result = numbers
.map(n => n * 2)        // Double each entry, obtain [2, 4, 6, 8, 10]
.filter(n => n > 3) // Keep only the entries bigger than 3, so you get [4, 6, 8, 10]
.reduce((n1, n2) => n1 + n2) // Adds them: 4 + 6 + 8 + 10 = 28

console.log(result) // 28
```


## 使用对象

<chapterId>7842aada-f009-5518-b8e3-1104e166a035</chapterId>


在本章中，我们将学习一些功能强大且稍显高级的工具，用于在 JavaScript 中处理对象。


### 私人物业


有时，我们想隐藏对象的某个属性，这样就无法从对象外部更改或访问该属性。JavaScript 提供了一种在属性名称前使用 `#` 的方法。这样就创建了一个**private**属性，只有在类内部才能访问该属性。


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


当你想防止意外更改时，私有属性很有帮助。


### 静态属性


有时，您希望某个属性属于类本身，而不是属于您从该类创建的每个对象。这就是 `static` 的作用。静态 "属性包含在类中，该类的所有对象都将引用它。


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


这对于存储共享数据和方法非常有用，这些数据和方法适用于整组对象，而不仅仅是一个对象。


### get "和 "set


在 JavaScript 中，"get "和 "set "可以让你创建看起来*像普通变量的属性，但实际上是在后台运行特殊代码。


当你尝试*read*一个属性时，会运行一个`get`ter方法。在方法前写入带有属性名称的 `get` 即可声明该方法。


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


尽管 `fullName` 不是一个常规属性，但我们可以像使用常规属性一样使用它，在幕后运行 `get` 函数来生成全名。


当你为一个属性指定一个值时，就会运行一个 `set`ter 方法。它可以让你控制当有人试图更改该值时会发生什么。声明方法时，在方法前写入带有属性名称的 `set`。


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


当我们执行 `user.fullName = "John Smith "时，会运行 `set` 方法并更新 `firstName` 和 `lastName` 值。


因此，尽管感觉上我们只是在设置一个简单的变量，但实际上我们是在触发更新其他属性的逻辑。


## 关键和价值

<chapterId>01a397b8-c12a-5c39-82b3-6d9ebbb72a29</chapterId>


JavaScript 对象中的每个属性都有一个**键**（也称为属性名）和一个**值**。


例如


```javascript
const user = {
name: "Alice",
age: 30
}
```


在这个对象中，"name "和 "age "是键，"Alice "和 "30 "是它们的值。


### 动态访问


有时，您事先并不知道某个属性的名称......也许您是从用户输入或变量中读取的。你仍然可以使用**括号符号**来访问它，如`myObject["keyName"]`。


```javascript
const user = {
name: "Alice",
age: 30
}

console.log(user["name"]) // Alice
```


我们将字符串 `name` 传递给对象，以获取相应的值。


我们可以将键保存到变量中，然后使用它来访问相应的值，例如


```javascript
const user = {
name: "Alice",
age: 30
}

const key = "name"

console.log(user[key]) // Alice
```


### 动态 Assignment


您还可以使用变量作为键来创建或更新对象属性。


```javascript
const settings = {}

const key = "theme"
settings[key] = "dark"

console.log(settings) // { theme: "dark" }
```


当您想逐步构建一个对象时，这很有帮助。例如


```javascript
const user = {}

user["username"] = "bananaFan123"
user["email"] = "banana@fruit.com"

console.log(user)
// { username: "bananaFan123", email: "banana@fruit.com" }
```


您甚至可以使用方括号在创建*对象时使用动态键：


```javascript
const key = "language"
const config = {
[key]: "JavaScript"
}

console.log(config.language) // JavaScript
```


这被称为**计算属性**。对方括号内的值进行评估，并将评估结果用作键值。


### 符号 "类型


除了字符串，JavaScript 还允许使用一种名为 `Symbol` 的特殊类型作为对象键。


让我们从一个简单的例子开始：


```javascript
const id = Symbol("userID")

const user = {
name: "Bob",
[id]: 12345
}

console.log(user[id]) // 12345
```


在本例中，`id` 是一个符号。它不是字符串，但仍然可以作为键。如果尝试将 `user` 记录到控制台，会看到下面的内容：


```javascript
console.log(user) // { name: 'Bob', [Symbol(userID)]: 12345 }
```


还有一点很重要：您创建的每个符号都是独一无二的，即使它们是使用相同的字符串创建的。


```javascript
const a = Symbol("label")
const b = Symbol("label")

console.log(a === b) // false
```


使用符号可以定义不会与常规键冲突的键。例如，假设您有一个带有 `name` 属性的对象，但该对象将来会被用户自定义，这是您无法预料的，而且该用户可能还会添加一个 `name` 属性。如果原来的 `name` 属性是用字符串定义的，那么它就会被新的字符串覆盖，就像这样：


```javascript
const obj = {
name: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy' }
```


如果用符号来代替


```javascript
const name = Symbol("name")

const obj = {
[name]: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy', [Symbol(name)]: 'John' }
```


正如您所看到的，原始的 `name` 属性以某种方式保留了下来。这在某些边缘情况下很有用。


## 实用工具

<chapterId>516e74c8-2a11-545a-a4d1-c2cabb91a273</chapterId>


JavaScript 提供了一些有用的内置对象，可以帮助我们完成调试和数学运算等工作。


### 其他 "控制台 "方法


您已经看过 `console.log`，它会将数值打印到屏幕上。


控制台 "对象上还有其他一些有用的方法，可以帮助你调试程序。


#### `console.warn`


打印黄色信息（或在某些环境中带有警告图标）：


```javascript
console.warn("This is just a warning.")
```


#### `console.error`


打印红色信息，就像出错一样：


```javascript
console.error("Something went wrong!")
```


#### 控制台表格


以表格形式显示数组或对象：


```javascript
const users = [
{ name: "Alice", age: 25 },
{ name: "Bob", age: 30 }
]

console.table(users)
```


这将打印出一张表格，如


```
┌─────────┬────────┬─────┐
│ (index) │  name  │ age │
├─────────┼────────┼─────┤
│    0    │ 'Alice'│  25 │
│    1    │ 'Bob'  │  30 │
└─────────┴────────┴─────┘
```


这对结构化数据的可视化非常有用。


#### console.time "和 "console.timeEnd"。


你可以测量一件事需要多长时间：


```javascript
console.time("timer")
for (let i = 0; i < 1000000; i++) {}
console.timeEnd("timer")
```


打印内容如下


```
timer: 2.379ms
```


可用于一些简单的性能测试。


### 数学对象


JavaScript 为您提供了一个 `Math` 对象，其中包含用于进行计算的实用方法。


#### Math.random()"。


返回介于 0（包含）和 1（不包含）之间的随机数：


```javascript
const r = Math.random()
console.log(r)
```


输出示例


```
0.4387429859
```


#### Math.floor()`和`Math.ceil()`。



- Math.floor(n)`向下**舍入到最接近的整数
- Math.ceil(n)`向上舍入***到最接近的整数


```javascript
console.log(Math.floor(4.9)) // 4
console.log(Math.ceil(4.1))  // 5
```


#### `Math.round()`


取整到最接近的整数：


```javascript
console.log(Math.round(4.4)) // 4
console.log(Math.round(4.6)) // 5
```


#### Math.max()`和`Math.min()`。


从数字列表中返回最大或最小值：


```javascript
console.log(Math.max(5, 9, 3)) // 9
console.log(Math.min(5, 9, 3)) // 3
```


#### Math.pow()`和`Math.sqrt()`。



- Math.pow(a,b) "可以将 "a "乘以 "b "的幂
- 通过`Math.sqrt(n)`可以求出`n`的平方根


```javascript
console.log(Math.pow(2, 3))   // 8
console.log(Math.sqrt(16))    // 4
```


# 高级 JavaScript

<partId>72c30671-ca20-5617-92a5-d5ba7aa38c93</partId>


## 其他收藏

<chapterId>a9a70c6d-a343-5a46-a383-e288bc2700e3</chapterId>


JavaScript 提供了一些超出普通数组和对象的特殊集合类型。其中包括 `Map` 和 `Set`。


它们可以帮助你存储和管理数值组，但它们的工作方式与你目前看到的不同。


Map" 是**键值对**的集合，就像对象一样。但它有一些重要的区别：



- 键可以是**任何值**，而不仅仅是字符串。
- 项目顺序保持不变。
- 它有内置的方法，使工作变得更容易。


您可以像这样创建一张新地图：


```javascript
const myMap = new Map()
```


这将创建一个空地图。要向其中添加条目，请使用 `myMap.set(key,value)`：


```javascript
myMap.set("name", "Alice")
```


这将添加一个键`"name"`和值`"Alice"`。


您也可以使用数字作为按键：


```javascript
myMap.set(42, "The answer")
```


甚至可以将一个对象作为密钥：


```javascript
const objKey = { id: 1 }
myMap.set(objKey, "Object as key")
```


这对普通对象不起作用，因为普通对象只允许字符串键。


要**获取值**，请使用 `myMap.get(key)`：


```javascript
console.log(myMap.get("name"))     // Alice
console.log(myMap.get(42))         // The answer
console.log(myMap.get(objKey))     // Object as key
```


要**检查键是否存在**，请使用 `myMap.has(key)`：


```javascript
console.log(myMap.has("name")) // true
```


要**删除键**，请使用 `myMap.delete(key)`：


```javascript
myMap.delete("name")
```


要**清除整个地图**，请使用 `myMap.clear()`：


```javascript
myMap.clear()
```


地图非常适合管理大型值集合，因为访问大型地图上的值通常比访问大型对象的性能要好得多。


### 设置


集合 "是一个只有**个值**（没有键）的集合，其中每个值都必须是**独一无二的**。也就是说



- 相同的值不能有两次
- 值将按照添加的顺序存储


你可以这样创建一个集合：


```javascript
const mySet = new Set()
```


要**添加值**，请使用 `mySet.add(value)`：


```javascript
mySet.add(1)
mySet.add(2)
mySet.add(2) // duplicate, will be ignored
```


即使我们尝试添加两次 `2`，集合也只会保留一个副本。


要**检查某个值是否在集合中**，请使用 `mySet.has(value)` ：


```javascript
console.log(mySet.has(2)) // true
console.log(mySet.has(3)) // false
```


要**删除一个值**，请使用 `mySet.delete(value)` ：


```javascript
mySet.delete(2)
```


要**清除所有内容**，请使用 `mySet.clear()`：


```javascript
mySet.clear()
```


当您想保存一个唯一值集合，而无需手动检查是否有重复值时，`Set` 就非常有用：


```javascript
const numberArray = [1, 2, 2, 3, 4, 4, 4, 5]

const numberSet = new Set(numberArray)

console.log(numberSet) // Set(5) { 1, 2, 3, 4, 5 }
```


设置 "可以避免重复。


## 迭代器

<chapterId>61d24e5e-b7e4-541a-8322-778f61f26a72</chapterId>


JavaScript 中大多数可以循环的东西（如数组、字符串、映射、集合）都是**可迭代的：它们可以为其内容提供迭代器。


在 JavaScript 中，**iterator** 是一个特殊的对象，它可以帮助你一次**地浏览一个项目列表。


### 对象 "迭代器


与数组或地图不同，常规对象**不能使用`for...of`进行迭代**。如果你尝试这样做


```javascript
const user = {
name: "Alice",
age: 30
}

for (const value of user) {
console.log(value)
}
```


您会收到一条错误信息：


```
TypeError: user is not iterable
```


这是因为普通对象没有内置迭代器。但 JavaScript 提供了其他工具来对它们进行循环。


#### `Object.keys()`


您可以使用 `Object.keys(obj)` 获取对象的**键**数组，然后对其进行循环：


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


打印


```
name
age
```


#### `Object.values()`


要循环**值**，请使用 `Object.values()`：


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


打印


```
Alice
30
```


#### 对象.条目()"。


如果需要**键和值**，请使用 `Object.entries()`：


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


打印


```
name is Alice
age is 30
```


尽管对象不是直接可迭代的，但这些方法可以让你以一种与 `for...of` 配合使用的方式完全访问对象的内容。


但迭代器是如何工作的呢？


### 符号迭代器


所有迭代器背后的秘密都是一个特殊的**符号**，名为 "Symbol.iterator"。


这个符号是一个内置键，它告诉 JavaScript："此对象可以被迭代"。


当你调用`myIterable[Symbol.iterator]()`时，JavaScript会返回一个**iterator对象**和`.next()`方法。


让我们看看会是什么样子：


```javascript
const colors = ["red", "green", "blue"]

const iterator = colors[Symbol.iterator]()

console.log(iterator.next()) // { value: 'red', done: false }
```


每次调用 `.next()` 都会得到下一个值。调用完成后，它会返回：


```javascript
{ value: undefined, done: true }
```


### 下一个


.next() "方法用于从序列中获取下一个项目。


每次调用 `.next()` 时，都会得到一个包含两个键的对象：



- value"：当前项目
- done"：布尔值，表示迭代是否结束


让我们举一个完整的例子：


```javascript
const names = ["Lina", "Tom", "Eva"]      // declare an array
const iterator = names[Symbol.iterator]() // use the Symbol.iterator function to get an iterator for this array

let result = iterator.next()              // get the first element of the array

while (!result.done) {                    // repeat this loop until you reach the last element of the array, which is marked with { done: true }
console.log(result.value)               // print the value of each element
result = iterator.next()                // get the next element of the array
}
```


打印


```
Lina
Tom
Eva
```


这就是 "for...of "循环在引擎盖下的工作原理：它与".next() "一起使用这种模式。


使用


```javascript
const names = ["Lina", "Tom", "Eva"]

for (const result of names) {
console.log(result)
}
```


### 使类可迭代


您还可以通过添加 `[Symbol.iterator]()`方法，定义自己的**iterable 类**。


比方说，我们想要一个表示数字**范围的类，比如从 1 到 5。


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


打印


```
1
2
3
4
5
```


事情是这样的



- 我们定义了一个类 `Range
- 在类中，我们实现了"[Symbol.iterator]()"，因此 JavaScript 知道如何遍历它
- next() "方法会逐一返回每个数字
- 当我们到达 `end` 时，它会返回 `{ done: true }`。


现在，我们的 `Range` 类就像数组一样工作，我们可以在任何需要可迭代的循环中使用它。


### 生成器函数和 "产量


为了更方便地创建迭代器，JavaScript 提供了**生成器函数**，使用`function*`关键字（即`function`，末尾加上`*`）和`yield`关键字。


让我们试试：


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


每个 `yield` 返回一个值，并**暂停**函数，直到下一个 `.next()`被调用。


您也可以使用 `for...of` 在生成器上循环：


```javascript
for (const num of numberGenerator()) {
console.log(num)
}
```


打印


```
1
2
3
```


## 回调的并发性

<chapterId>f3fc76ca-b3ef-54eb-a06e-501007002054</chapterId>


到目前为止，我们的代码都是**同步**：按顺序一行一行地运行。但现实世界中有些事情需要时间，我们不希望整个程序在等待时暂停。


在本章中，我们将介绍一个新概念： **并发**。它允许我们操纵事情完成的顺序。这在处理计时器、用户输入或从磁盘读取文件等事务时非常有用。JavaScript 提供了不同的并发工具。


### setTimeout


函数 `setTimeout` 可以让你在一段时间过后**运行函数。


例如


```javascript
console.log("Start")

setTimeout(
() => console.log("This runs after 2 seconds"),
2000
)

console.log("End")
```


打印


```
Start
End
This runs after 2 seconds
```


虽然 `setTimeout` 出现在代码的中间，但它并没有阻塞其他部分。相反，它会安排函数在**后运行，然后立即继续。


2000 "表示 2000 毫秒（即 2 秒）。

下面是对 **Callbacks** 和 **Promise** 部分的重写，整个过程中使用了数据操作和清晰的注释，更加简洁，也更便于初学者理解：


### 回调


回调**只是一个函数，我们把它交给另一个函数，以便以后可以**调用。


让我们来看一个使用数字的真实例子。想象一下，我们有一个数字列表，我们想把每个数字加倍，然后对得到的 "加倍 "数组应用一个函数（回调函数），但我们想在稍作延迟后进行，就像我们在等待一些缓慢的事情（比如从互联网加载数据）一样。


下面是一个使用**回调**来实现这一功能的函数：


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


让我们试着使用这个功能：


```javascript
const input = [1, 2, 3]

doubleNumbers(input, function(result) {
console.log("Here is the doubled array:", result)
})
```


1 秒钟后，打印出来：


```
Here is the doubled array: [ 2, 4, 6 ]
```


**这里发生了什么事？


1.我们将 `input` 作为要加倍的数字列表。

2.我们还传递了一个**回调函数**，告诉程序在加倍后**要做什么。

3.在 `doubleNumbers` 中，我们使用 `setTimeout` 模拟延迟，然后进行加倍。

4.一旦完成，我们就会调用结果 "加倍 "数组的回调。


这种方法是可行的，但试想一下，如果您想在此之后执行更多步骤，比如过滤掉小数字，然后将它们相加。你就必须像这样**嵌套**更多的回调：


```javascript
doubleNumbers(input, function(doubled) {
filterBigNumbers(doubled, function(filtered) {
sumNumbers(filtered, function(total) {
console.log("Final result:", total)
})
})
})
```


这是 Hard 的读取方式，而且杂乱无章。这种风格被称为 "回调地狱"（**callback hell**），而 "承诺"（`Promise`）正是为了解决这一问题而诞生的。


## 承诺并发

<chapterId>30fddaca-729f-5c8d-bf86-8dfc7b3c9800</chapterId>


Promise "是一个内置的 JavaScript 对象，它代表一个将在未来**准备好的值。


我们可以这样创建一个 "承诺"：


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve("It worked!") // This means everything went OK
})
```


`new Promise()` 部分创建承诺。


在它的内部，我们给它一个带有两个参数的函数：



- resolve"，是我们在一切顺利时调用的函数
- reject"，是我们在出错时调用的函数


在上面的示例中，我们只需立即解决这个问题，并显示信息 `"成功了！"。


### `.then()`


要在承诺完成后***做某事，我们使用 `.then()`：


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve(100) // This means everything went OK
})

promise.then(result => {
console.log("The result is:", result)
})
```


打印


```
The result is: 100
```


我们传给`resolve()`的值会以`result`的形式发送到`.then()`内部的函数。


让我们使用 `setTimeout` 模拟一个耗时 2 秒的任务：


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


这会等待 2 秒钟，然后打印：


```
Done waiting!
```


### 拒绝()`


让我们创造一个***失败的承诺：


```javascript
const failingPromise = new Promise((resolve, reject) => {
reject("Something went wrong")
})
```


现在，如果我们对此使用 `.then()`，什么也不会发生，因为 `.then()` 只处理成功。


要处理错误，我们使用 `.catch()`：


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


仅打印


```
Caught an error: Something went wrong
```


传递给 `reject()` 的值将被发送到 `.catch()` 函数。


让我们创建一个 "承诺"（Promise），根据某些条件，它**时工作，时**失败。


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


现在我们可以调用它来处理这两种情况：


```javascript
checkNumber(5)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


打印


```
Success: Positive number
```


如果我们换一个数字试试：


```javascript
checkNumber(-1)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


它可以打印：


```
Failure: Not a positive number
```


### 使用 `Promise`s 进行连锁操作



我们可以使用 `Promise` 重写之前的示例，这样看起来会更简洁。


让我们先编写一个新版本的加倍函数，但这次它返回的是一个 **promise** ：


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


现在，我们可以使用 `.then()` 来告诉 JavaScript 如何处理结果：


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


打印


```
Doubled numbers: [ 2, 4, 6 ]
```


到目前为止，它的工作原理与回调版本相同，但现在代码更易于扩展和阅读。


比方说，我们想增加更多的步骤：


1.首先，将所有数字加倍

2.然后，删除小于 4 的数字

3.最后，将它们加在一起


我们可以为每一步编写一个函数，全部使用承诺：


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


现在，我们可以像这样把它们**链**在一起：


```javascript
const input = [1, 2, 3]

doubleNumbers(input)
.then(filterBigNumbers)
.then(sumNumbers)
.then(
result => console.log("Final result after all steps:", result)
)
```


打印


```
Final result after all steps: 10
```


让我们来了解一下它的作用：


1.`doubleNumbers` 将数组加倍：`[2, 4, 6]`

2.过滤大数 "会移除 ≤ 3 的内容： "[4，6]"。

3.将剩余的数字相加：`4 + 6 = 10`

4.最后，我们打印结果。


每个 `.then()`都会等待它之前的步骤完成。因此，我们可以构建一个**动作链**，而无需嵌套。这使得代码更具可读性，也更容易调试。


## 使用 "async"/"await "的并发性

<chapterId>6e93d29f-c8bf-5fd1-a9c9-4e794ee6cbd0</chapterId>


我们看到了 `Promise` 链是如何帮助我们避免回调地狱的，但当涉及许多步骤时，读起来还是会有些费劲。


这就是 `async` 和 `await` 的用武之地。它们让我们编写的异步代码**看起来像同步代码**，这让我们更容易理解。


### 什么是 `async`？


在函数前写入关键字 "async "时，JavaScript 会自动用 Promise 封装函数的返回值。


让我们来看一个基本的例子：


```javascript
async function greet() {
return "hello"
}
```


如果调用该函数


```javascript
const result = greet()
console.log(result)
```


你会看到这个：


```
Promise { 'hello' }
```


虽然您只是返回了一个字符串，但 JavaScript 会将其转化为一个 Promise。您可以像这样使用 `.then()` 获取实际值：


```javascript
greet().then( result => console.log(result) ) // prints "hello"
```


或者您可以使用 `await`...


### 什么是 "等待"？


关键字 `await` 告诉 JavaScript："等待这个 Promise 完成，然后给我结果"。


但只能在异步函数**内使用`await`。


让我们使用 `await` 重写这个例子：


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


现在，我们可以像使用常规值一样使用结果。


现在让我们做点更有用的事情吧。


### 用 "等待 "模拟延迟


我们将创建一个简单的 `wait` 函数，该函数以毫秒为参数，只在毫秒后进行解析，而不做任何其他操作：


```javascript
function wait(ms) {
return new Promise(resolve => {
setTimeout(resolve, ms)
})
}
```


让我们试着使用它：


```javascript
async function test() {
console.log("waiting 2 seconds...")
await wait(2000)
console.log("done waiting")
}

test()
```


打印


```
waiting 2 seconds...
done waiting
```


你可以把 "等待 "理解为 "在这里暂停，直到承诺完成，然后继续"。


这样，您就可以以**从上到下**的方式编写代码，而无需链式调用`.then()`。


### 等待数据


让我们重用之前的例子，先将数字加倍，然后过滤，最后求和。但这次，我们将使用 `async`/`await`.


我们将创建 3 个模拟等待并返回 Promises 的函数：


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


现在，让我们编写一个 `async` 函数来组合它们：


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


打印


```
Final result: 10
```


这比连锁使用 `.then()` 或嵌套回调函数更易于阅读。


它看起来像一个普通的分步程序，但仍然是异步运行的。


## 异步迭代器

<chapterId>438b037d-9931-56d7-9052-7b4470f3c75b</chapterId>


我们已经了解了 **iterators** 以及如何使用 `for...of` 来循环数组和其他可迭代的东西。


但如果我们要迭代的数据需要一段时间才能到达呢？


有时，我们想循环播放**异步**到达的内容，如聊天中的信息、文件中的行数或慢速数据源中的数字。


为此，JavaScript 为我们提供了 **async iterators**。


### 异步发生器功能


创建异步迭代器的最简单方法是使用**异步生成器函数**。


我们这样写


```javascript
async function* generateNumbers() {
yield 1
yield 2
yield 3
}
```


这看起来就像一个普通的生成器，只是在它前面加上了 `async`。


现在我们可以使用 `for await...of` 来消耗这些值：


```javascript
async function run() {
for await (const n of generateNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


这将打印出来：


```
Got number: 1
Got number: 2
Got number: 3
Done!
```


那么，与普通发电机有什么区别呢？


不同之处在于：我们现在可以在生成器中使用 `await` 了。


让我们再做一次延迟助手吧：


```javascript
function wait(ms) {
return new Promise(resolve => setTimeout(resolve, ms))
}
```


现在，让我们***缓慢地得出数字：


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


试着使用它：


```javascript
async function run() {
for await (const n of generateSlowNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


### 为什么要使用异步迭代器？


异步迭代器在以下情况下非常有用



- 价值不会一下子全部到来。
- 你要一个一个地处理，**它们来的时候**。
- 您正在使用 "承诺"，并希望以简洁的方式循环。


例如，如果您想从聊天服务器上逐条加载消息，或分块下载大文件，那么异步迭代器为您提供了一种方法，可以编写一个可处理延迟数据的 `for` 循环。


### 符号.异步迭代器


我们还可以在自定义类中使用异步迭代器。


下面是一个产生延迟数字的示例：


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


现在我们可以像以前一样使用 `for await...of` 了：


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


这样就可以创建可以异步迭代的对象


## Assignment 语法糖

<chapterId>8b1ba7d8-ecfd-5470-b86e-73cb84ccc8b7</chapterId>


"语法糖 "指的是在不改变其功能的前提下，以更简短或更容易的方式编写某些内容。它只是用一种更好的方式来表达同样的意思。


JavaScript 内置了一些语法糖，可以让我们编写更简洁的声明。在本章中，我们将学习如何根据条件赋值、使用数学方法更新变量、从数组或对象中提取值，以及使用更简单的语法复制或组合它们。


### 三元运算符


在 JavaScript 中，您可以使用**辅助运算符**根据条件赋值，这是 "if...else "的简写。


而不是做：


```javascript
let message

if (isMorning) {
message = "Good morning"
} else {
message = "Hello"
}
```


你可以写


```javascript
const message = isMorning ? "Good morning" : "Hello"
```


这意味着



- 如果 `isMorning` 为 true，则使用 `"早上好"。
- 否则，使用 `"Hello"`


一般格式为


```javascript
condition ? valueIfTrue : valueIfFalse
```


您也可以在其他表达式中使用它：


```javascript
console.log(isSunny ? "Go outside" : "Stay in")
```


只需确保将其用于**简单**的决策。如果逻辑复杂，请坚持使用 `if...else`。


### Assignment 运营商备选方案


JavaScript 具有**快捷操作符**，用于结合操作进行赋值。


让我们看看正常的方法：


```javascript
let counter = 1
counter = counter + 1
```


这可以缩短为


```javascript
let counter = 1
counter += 1 // same as counter = counter + 1
```


以下是最常见的几种：


| Operator | Meaning             |
| -------- | ------------------- |
| `+=`     | add and assign      |
| `-=`     | subtract and assign |
| `*=`     | multiply and assign |
| `/=`     | divide and assign   |

例如


```javascript
let score = 10
score += 5  // now score is 15
score *= 2  // now score is 30
score -= 10 // now score is 20
```


当您想使用变量自身的值更新变量时，这些参数非常有用。


### 结构调整


**重构**可让你轻松地从数组或对象中提取数值并将其存储到变量中。


#### 数组


假设你有


```javascript
const colors = ["red", "green", "blue"]
```


而不是做：


```javascript
const first = colors[0]
const second = colors[1]
```


你能做到


```javascript
const [first, second] = colors
```


这意味着



- 将`first`改为`"red"。
- 将 "second "改为 "Green"。


您也可以跳过数值：


```javascript
const [,, third] = colors
console.log(third) // blue
```


#### 对象


您还可以从对象中提取值：


```javascript
const user = { name: "Alice", age: 30 }

const { name, age } = user
console.log(name) // Alice
console.log(age)  // 30
```


如果属性的名称与您想要的变量不同，您可以重新命名它：


```javascript
const { name: username } = user
console.log(username) // Alice
```


在处理对象和数组时，重构可使代码更加简洁。


### 传播语法


**spread 语法**使用"... "来解包或复制值。


#### 数组


您可以复制或合并数组：


```javascript
const a = [1, 2]
const b = [3, 4]

const both = [...a, ...b]
console.log(both) // [1, 2, 3, 4]
```


您还可以克隆一个数组：


```javascript
const original = [10, 20, 30]
const clone = [...original]
```


#### 对象


对物体也可以这样做：


```javascript
const a = { x: 1 }
const b = { y: 2 }

const merged = { ...a, ...b }
console.log(merged) // { x: 1, y: 2 }
```


您还可以覆盖数值：


```javascript
const user = { name: "Alice", age: 30 }
const updated = { ...user, age: 31 }

console.log(updated) // { name: "Alice", age: 31 }
```


这在更新对象而不改变原始对象时非常有用。


# NodeJS

<partId>42fe4d49-dace-5135-bb9e-b9d75034fb2a</partId>


## 我们如何进入节点

<chapterId>0da1d60c-06c9-54e6-a181-ae7dabf6e3b8</chapterId>


在本章中，我们将了解一些有关 JavaScript 和 NodeJS 的历史背景。


在软件领域，历史背景非常重要，因为我们经常使用的工具是由其他人制作的，因此我们会受到他们过去所做决定的影响。


了解做出这些决定的原因，以及我们所使用的工具是如何形成的，会让我们对自己正在做的事情不再感到困惑。


### JavaScript 的起源


JavaScript 起初是一种简单的语言，旨在使网页具有交互性。


20 世纪 90 年代，网景浏览器（Netscape Navigator）等网络浏览器增加了 JavaScript，这样开发人员就可以编写直接在浏览器中运行的代码。


最初的想法是将 Java 作为制作网站的核心语言（使用所谓的 "Java applets"），而 JavaScript 则只用于次要用途。


核心设计由当时还是网景公司雇员的布伦丹-艾奇在不到两周的时间内完成。


但与 Java 相比，大多数人更喜欢使用 JavaScript，而且 Java 小程序当时还存在一些安全问题，因此 Java 最终被放弃，JavaScript 成为网络开发的事实标准。


### V8 发动机


JavaScript 是一种解释型语言，与 C 语言等编译型语言不同。


用编译语言编写的代码会变成二进制代码，二进制代码会直接输入计算机的中央处理器。


![](assets/en/6.webp)


另一方面，互斥语言往往对用户更友好，更接近人类的思维方式（"高级"），而不是机器的工作方式（"低级"）；因此，它们通常内置虚拟机来运行代码。


虚拟机是一个特殊的程序，它位于你编写的代码和 CPU 之间，并执行你的代码（因为 CPU 无法理解）。


这样，你就可以在不太了解底层机器的情况下进行编程，但这也会在性能方面产生代价，因为计算机运行的不仅仅是你的程序，而是运行你的程序的程序（虚拟机）。


随着网络应用变得越来越复杂，人们要求提高 JavaScript 的性能。V8 引擎是谷歌浏览器中支持 JavaScript 的解释器。它由谷歌开发，于 2008 年发布。


旧版 JavaScript 引擎大多是传统的虚拟机，而 V8 引擎则是一个 JIT（即时）编译器。


JavaScript 代码会被送入 V8 引擎，然后引擎会尝试将其中的一部分编译为本地二进制文件。这样，你就能获得高级语言的体验，而性能却更接近低级语言。这使得 JavaScript 成为世界上速度最快的高级语言，有点 "两全其美 "的感觉。


### NodeJS 运行时


虽然 JavaScript 易于使用，执行速度也相当快，但在 V8 发布后，它一直存在一个巨大的限制：只能在浏览器中运行。


为什么会有这样的问题？


由于浏览器执行的代码来自互联网上数以百万计的不同来源，它们很容易感染恶意软件，因此它们被 "沙盒化"，与操作系统的其他部分隔离开来。


![](assets/en/7.webp)


JavaScript 无法访问计算机上的文件系统和其他本地资源（至少无法像其他语言那样轻松访问），因此这对使用 JavaScript 构建应用程序造成了很大的限制。


2009 年，Ryan Dahl 发布了 NodeJS，它是一个运行时，可以让你在浏览器之外直接在计算机的本地操作系统上使用 V8 引擎。它还增加了许多对编写服务器端和命令行程序有用的功能。例如，您可以使用 NodeJS 创建网络服务器、读写文件或构建自动执行任务的工具。


![](assets/en/8.webp)


在本课程中，我们已经探索了浏览器和 NodeJS 中的 JavaScript 功能。这些特性使我们能够定义数据并以抽象的方式对其进行操作。在接下来的几课中，我们将探索 NodeJS 特有的功能，这些功能允许我们与操作系统进行交互。


## 命令行参数

<chapterId>960d20f3-c424-5d51-a041-ef17d2e94b6d</chapterId>


NodeJS 除其他功能外，还允许我们构建 CLI（命令行接口）。


为此，我们需要一种接收命令行参数的方法，这在 Node 中是通过内置的 `process` 对象来实现的。


### 进程


NodeJS 提供了一个名为 "进程 "的特殊对象，它代表当前正在运行的程序。


你可以用它来检查环境、当前工作目录，甚至在需要时退出程序。


例如


```javascript
console.log(process.platform)
```


这将打印操作系统平台，如 "win32"、"linux "或 "darwin"（Mac）。


### 进程参数


从终端运行 NodeJS 程序时，可以在脚本名称后传递额外的字（参数）。这些参数存储在 `process.argv` 中。


例如，如果运行此命令


```
node my_script.js alpha beta
```


您可以这样打印参数


```javascript
console.log(process.argv)
```


输出结果可能是这样的


```
[ '/path/to/node', '/path/to/my_script.js', 'alpha', 'beta' ]
```


前两项始终是节点路径和脚本路径。之后才是脚本传递的其他字词。


process.argv "数组可以像其他数组一样使用".slice() "方法进行剪切，因此，如果只想获得传递的参数，可以这样做


```javascript
const args = process.argv.slice(2)

console.log(args)
```


获取用户传递的参数是开发命令行应用程序的基础。


## 模块

<chapterId>4e1651a5-65fd-50bc-b22a-40313d5659ca</chapterId>


JavaScript 运行时（如 NodeJS）通常将每个 JavaScript 文件视为一个单独的模块。


把模块想象成一个盒子。盒子有自己的私有空间，因此你在其中声明的变量和函数不会干扰其他盒子中的代码。基本上，每个模块都有自己的作用域。


一个模块可以导出其部分内容，供其他模块使用，也可以导入其他模块导出的内容。JavaScript 允许在模块之间导出和导入内容，连接不同的文件。


JavaScript 程序通常由多个模块组成，这些模块之间相互连接。


为什么要使用模块？通过将代码分割成模块，可以将程序组织成更小、更清晰和可重复使用的部分。每个模块可以只专注于一种任务，如处理数学计算、处理文件或格式化文本。


### CommonJS 模块


在 NodeJS 中，最常用的模块管理系统称为**CommonJS**。


在这个系统中，你可以使用 `module.exports` 从一个模块共享（导出）代码，并使用 `require()` 在另一个文件中加载（导入）它。


要使模块外的内容可用，可将其分配给 `module.exports`：


```javascript
const greeting = "Hello!"

module.exports = greeting
```


这里，该模块输出的是字符串 `"Hello！"。


要使用从另一个文件导出的代码，需要使用带有该文件路径的 `require()` 函数：


```javascript
const greeting = require("./greeting.js")

console.log(greeting)
```


打印


```
Hello!
```


您可以将多个内容捆绑在一个匿名对象中导出，例如


```javascript
const greeting1 = "hello"

const greeting2 = "hi"

module.exports = {
greeting1, greeting2
}
```


CommonJS 是 NodeJS 最初采用的模块系统。后来还增加了 ES 模块。


### ES 模块


NodeJS 还支持另一种模块，称为 **ES Modules**，这种模块在网络开发中非常流行。它们使用关键字 "导出 "和 "导入"。


ES 模块是为浏览器开发的，后来才添加到 Node 中。如果您想使用它们，可能必须使用 `.mjs` 作为文件扩展名，而不是 `.js`，这取决于您使用的 Node 版本。


在一个名为 "greeting.mjs "的文件中，我们写道


```javascript
export const greeting = "Hello!"
```

正如你所看到的，我们直接导出了常量的定义位置


在另一个名为 `index.mjs` 的文件中，我们导入它：


```javascript
import { greeting } from "./greeting.mjs"

console.log(greeting)
```


您可以在文件的不同部分导出不同的声明，例如


```javascript
export const num = 10

export function double (x) {
return x*2
}
```


### NodeJS 标准库


NodeJS 还包含许多内置模块。这些模块是 NodeJS 提供的现成模块，可帮助完成读取文件、使用操作系统或连接网络等常见任务。


例如，"os "模块可提供有关操作系统的信息：


```javascript
const os = require("os")

console.log(os.platform())
```


您无需安装这些内置模块，它们是 NodeJS 的自带模块。它们构成了运行时的 "标准库"，大多数 Node 应用程序都使用它们来完成读取文件或通过互联网通信等操作。


接下来的章节将向你展示一些有用的使用示例。


## fs "模块

<chapterId>911e953a-35ae-5ee7-bd74-372501c32e81</chapterId>


fs "模块（**文件系统**的缩写）是 NodeJS 标准库的一部分。它允许您处理计算机上的文件和目录：您可以读取文件、写入文件、删除文件、重命名文件等。


要使用它，首先需要在文件顶部导入：


```javascript
const fs = require("fs")
```


### 同步 API


使用 `fs` 的最简单方法是使用其 **sync** 方法。


这些方法会阻塞程序，直到完成为止（因此，在操作完成之前，下一行代码不会运行）。


下面是一个同步读取文件的示例：


```javascript
const fs = require("fs")

const data = fs.readFileSync("example.txt", "utf8")

console.log(data)
```


如果与脚本位于同一目录下的文件名为 `example.txt`，则将打印该文件的内容。


您也可以同步写入文件：


```javascript
const fs = require("fs")

fs.writeFileSync("output.txt", "Hello from Node!")

console.log("File written!")
```


这会用文本创建（或覆盖）一个名为 `output.txt` 的文件。


以下是您可以使用此 API 进行的一些常见操作：


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


同步 API 非常简单，适合小型脚本，但由于它会阻止程序运行直至完成，因此如果要处理大文件或服务器，它可能会拖慢运行速度。


### 回调异步 API


**callback API** 是非阻塞的：它允许 NodeJS 在文件操作发生时继续做其他事情。


它不直接返回结果，而是在操作完成后调用一个函数（**回调**）。


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


事情是这样的



- fs.readFile "开始读取 "example.txt"。
- NodeJS 不会等待，它会继续执行您可能编写的其他代码。
- 文件读取完成后，回调将运行：



  - 如果出现错误，`err` 包含错误信息。
  - 否则，`data` 包含内容。


下面是写入文件的方法：


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


想法相同：写文件时程序不会停止。


使用此 API 的一些示例：


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


回调应用程序接口更适合服务器和大型任务，因为它不会阻塞程序，但嵌套回调可能会让你的许多操作变得混乱。这就是添加基于承诺的异步 API 的原因。


### Promise 异步应用程序接口


基于 Promise 的 API 非常现代，与 `.then()` 和 `async/await` 配合得天衣无缝。它以 `fs.promises` 的形式提供。


您需要导入 `promises` 属性：


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


写入文件


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


应用程序接口的常规示例列表：


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


在编写代码时，您经常需要使用其他人编写的代码，例如，帮助您处理日期、颜色、服务器或几乎任何其他内容的库。


您可以使用**软件包管理器**来代替手动下载和复制文件。


软件包管理器是一种工具：



- 下载软件包
- 跟踪项目所需的软件包
- 确保团队中的每个人都拥有相同版本的软件包


### 什么是故宫博物院


在 NodeJS 领域，最流行的软件包管理器是 **NPM**，即 *Node Package Manager*（节点软件包管理器）。


安装 NodeJS 时会自动获得 NPM。


您可以在终端运行此程序，检查是否有 NPM：


```
npm -v
```


这将打印出您使用的 NPM 版本，例如


```
10.2.1
```


### 创建软件包


在 NodeJS 中，**package** 只是一个目录，其中包含一个 `package.json` 文件。


让我们一步步来创建一个。


1.为项目新建一个文件夹：


```
mkdir my_project
cd my_project
```


2.运行此命令：


```
npm init
```


这将启动一个交互式设置，向你询问项目名称、版本、描述等问题。


如果不想回答所有问题，只想接受默认值，可以使用


```
npm init -y
```


运行后，您将在文件夹中看到一个名为"...... "的新文件：


```
package.json
```


### `软件包.json`。


package.json` 文件只是一个 JSON 文件，其中存储了有关项目的元数据。


这里有一个例子：


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


几个重要领域：



- name`：软件包名称
- version"：当前版本
- main`：入口点文件（如 `index.js`）。
- 脚本"：可以运行的命令（如 "npm start）
- 依赖项"：列出项目依赖的所有软件包


### 安装软件包


假设你想使用某个名为 `picocolors` 的软件包为终端输出添加颜色。


运行


```
npm install picocolors
```


现在您可以在项目中使用它了。创建一个 `index.js` 文件，其中包含


```javascript
const pico = require('picocolors')

console.log(
pico.green("This text is green!")
)
```


并尝试运行它。终端应该会打印出彩色文本。


故宫博物院做了什么？



- 它下载了软件包，并将其存储在名为 `node_modules/` 的子文件夹中。
- 它在你的 `package.json` 中的 `dependencies` 下添加了一个条目
- 它更新了 `package-lock.json` 文件


什么是 `package-lock.json`?


### `package-lock.json`。


该文件由 NPM 自动创建。


你可能会问，既然我们已经有了 `package.json`，为什么还需要另一个文件呢？

原因就在这里：



- package.json "只说明项目需要哪个版本**范围**的软件包。

例如


```json
"dependencies": {
"picocolors": "^1.1.0"
}
```


^1.1.0` 表示 "与 1.1.x 兼容的任何版本"，因此很灵活。



- `package-lock.json` **冻结**每个软件包及其子依赖项的准确版本，这样每个安装项目的人都能获得完全相同的工作设置。


为什么这很重要？


如果你在一个团队中工作，或者你将项目部署到服务器上，或者你将来回到这个项目，你要确保它仍然以同样的方式运行。

如果软件包已经更新，而你重新安装时没有锁定文件，你可能会得到一个行为略有不同的版本。


通过在项目中保留`package-lock.json`，NPM 将始终安装其中列出的确切版本，确保每个人都拥有相同的环境。


package-lock.json "会将所有内容锁定为一个非常特定的版本，以使项目在其他机器上的可重复性更高。


但如果你的软件包需要被很多人使用，你可以选择不提交它，这样 NPM 就只能找到 `package.json` 文件，并允许它自动安装该文件允许安装的最新版本。


但这些都是你以后应该担心的事情，一旦你开始发布自己的代码。现在，我们介绍 NPM 的基础知识只是为了让你能在你的项目中找到并使用其他开发者发布的库。



## NodeJS 中的联网

<chapterId>f2cabd8b-754b-5c97-8d6a-8412a9a184c7</chapterId>


NodeJS 通常用作后台语言：您可以将脚本变成服务器，也可以用它向其他服务器发出请求。


在本章中，我们将介绍一些基本的网络功能，让你能够做到这一点。


### 获取


如果想让程序从网站或 API 下载数据，就需要发出 **HTTP 请求**。


在现代版本的 NodeJS 中，您可以使用内置的 `fetch()` 函数。


下面是一个向应用程序接口发出 GET 请求的示例：


```javascript
const response = await fetch("https://jsonplaceholder.typicode.com/posts/1")
const data = await response.text()

console.log(data)
```


运行此程序时，您会看到类似的内容：


```
{
"userId": 1,
"id": 1,
"title": "...",
"body": "..."
}
```


情况是这样的：


1.`fetch()` 获取 URL 并发出请求。

2.它返回一个**Promise**，解析为一个`Response`对象。

3.response.text()`以字符串形式读取响应正文。


但你得到的字符串实际上是 JSON。这是什么？


### JSON


在使用网络应用程序接口时，数据通常以**JSON**（JavaScript Object Notation）的形式发送和接收。


JSON 只是一种文本格式，看起来很像 JavaScript 对象。例如


```json
{
"name": "Alice",
"age": 30,
"likes": ["apples", "bananas"]
}
```


JSON "对象是 JavaScript 中的一个内置工具，可用于处理这种数据格式。


您可以使用 `JSON.stringify()` 将 JavaScript 对象转换为 JSON 字符串：


```javascript
const user = { name: "Alice", age: 30 }

const jsonString = JSON.stringify(user)

console.log(jsonString)
```


打印


```
{"name":"Alice","age":30}
```


您还可以使用 `JSON.parse()` 将 JSON 文本转换回 JavaScript 对象：


```javascript
const jsonText = '{"name":"Bob","age":25}'

const obj = JSON.parse(jsonText)

console.log(obj)
```


打印


```
{ name: 'Bob', age: 25 }
```


请小心：如果字符串不是有效的 JSON，`JSON.parse()` 将抛出错误。


```javascript
JSON.parse("not json") // ❌ Error!
```


因此，请确保字符串格式正确。


### http 服务器


通过 NodeJS，您无需安装任何其他设备即可创建网络服务器。


您可以使用内置的 `http` 模块来处理客户端的请求并发送响应。


下面是一个非常基本的例子：


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


运行该脚本并在浏览器中打开 `http://localhost:3000` 时，您将看到


```
Hello from NodeJS server!
```


这就是代码中发生的事情：


1.您从 Node 标准库中导入了 `http` 服务器。

2.http.createServer()` 创建服务器。您向 `http.createServer()` 传递了一个回调函数 `(req, res) => {...}`，以便每次有人连接时执行。

3.您为响应指定了 200 状态代码（表示操作成功）。您可以阅读有关 http 状态代码的信息 [此处](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

3.`res.end()` 发送响应并结束连接。

4.server.listen(3000)`在端口 3000 上启动服务器。


您还可以检查请求中的 `req.url` 和 `req.method` 以处理不同的路径或请求类型。


带路由的示例：


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


这些都是非常基本的示例。如果要构建更高级的服务器，大多数开发人员可能会下载一个现成的后台库，如 [express](https://www.npmjs.com/package/express)。


## 处理数据：缓冲区、事件、数据流

<chapterId>8c9623f0-a604-51a4-8fe4-871c849d3e3b</chapterId>


在本章中，我们将主要介绍三类对象：



- 缓冲区"，表示小块二进制数据
- EventEmitter"，可用于通过发射称为 "事件 "的信号，跟踪异步进程的某一步
- 流"，它允许我们一次处理一个 "缓冲区 "中的大量数据，并通过发出事件来跟踪处理过程


这些代码在专业的 NodeJS 代码中极为常见，因此，即使您可能不会在第一个项目中使用它们，也最好对何时需要与它们交互有一个基本的了解。 它们是


### 缓冲区


在 NodeJS 中，**缓冲区**是一种用于处理二进制数据的对象类型。


你可以把缓冲区看作一个固定大小的原始字节容器。


下面介绍如何从字符串创建缓冲区：


```javascript
const buf = Buffer.from("hello")
console.log(buf)
```


打印内容如下


```
<Buffer 68 65 6c 6c 6f>
```


这些数字（"68"、"65"、"6c "等）是 "hello "中字母的十六进制表示。


您可以像这样将其转换回字符串：


```javascript
console.log(buf.toString())
```


打印


```
hello
```


您还可以创建一个一定大小的缓冲区，缓冲区中填满 0：


```javascript
const buf = Buffer.alloc(10)
console.log(buf)
```


打印内容如下


```
<Buffer 00 00 00 00 00 00 00 00 00 00>
```


您可以将数据写入缓冲区：


```javascript
buf.write("abc")
console.log(buf)
```


您还可以访问单个字节：


```javascript
console.log(buf[0]) // prints the ASCII number for 'a', which is 97
```


当你需要在很低的级别上操作数据时，缓冲区尤其有用。


### 活动


在 JavaScript 中，"事件"（**event）是指在程序中发生的、您可以做出反应的事情。


例如



- 文件加载完毕
- 计时器启动
- 用户点击按钮
- 网络请求返回数据


**事件**只是发生了某件事的信号，你可以编写代码来监听这些事件，并对它们做出反应。


在 NodeJS 中，许多对象都可以发出事件。这些对象被称为 **EventEmitters**。


这里有一个例子：


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


打印


```
Hello! An event happened.
```


是这样的


1.我们创建一个 `EventEmitter` 对象。

2.我们使用 `.on("greet")`告诉它每当发生`"greet"`事件时就运行一个回调。

3.随后，我们使用 `.emit()` 触发 `"greet"` 事件。

4.我们的回调被执行


您可以将数据与事件一起传递：


```javascript
emitter.on("greet",
(name) => console.log(`Hello, ${name}!`)
)

emitter.emit("greet", "Alice") // first argument is the type of event, second argument is the data we pass with this event
```


打印


```
Hello, Alice!
```


您也可以为其他事件注册监听器：


```javascript
emitter.on("goodbye", () => {
console.log("Goodbye!")
})

emitter.emit("goodbye")
```


您可以为一种事件类型附加任意数量的监听器，也可以从同一个发射器触发多种不同类型的事件。


NodeJS 中的许多对象都会发出事件，告诉程序的其他部分正在发生某些事情。



### 什么是溪流？


数据流将缓冲区和事件结合起来，帮助我们处理数据。


当我们处理文件、网络数据甚至长文本时，并不总是需要（或想要）一次性将所有内容加载到内存中。这样做可能会很慢，如果数据量太大，甚至会导致程序崩溃。


相反，我们可以在数据到达或被读取时，一点一点地处理数据，就像用吸管喝水，而不是一次喝下整杯水。这就是所谓的**流**。


在 NodeJS 中，流是一种对象，它可以让你一次**从一个源读取数据或向一个目标写入数据。


NodeJS 有四种主要的流类型：



- 可读**：可以读取数据的数据流（如读取文件）
- 可写**：可以写入数据的数据流（就像写入文件一样）
- 双工**：既可读又可写的数据流
- 转换**：与双工数据流类似，但可以在数据流动时改变（转换）数据


### 可读流


比方说，你有一个 `bigfile.txt` 需要处理。你可以使用 `fs` 模块创建一个可读流，逐段读取文件。


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


这里发生了什么？


1.fs.createReadStream()`创建一个可读流。

2.每当文件的某个部分准备就绪，流就会发出一个 `data` 事件，并给出一个数据 "块"（一个 `Buffer`）。我们打印该数据块。

3.当读完整个文件后，就会触发 "结束 "事件。

4.如果出现错误（如文件不存在），就会触发 `error` 事件。


这样，您就可以读取巨型文件，而无需一次性将它们全部加载到内存中。


如果我们希望数据以人类可读的形式（而不是二进制）到达，我们可以指定数据流的编码：


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


现在，代码将以人类可读的形式打印文件。


### 可写流


可写入流可让你将数据逐块发送到某个地方。


下面是一个使用流写入`target.txt`文件的示例：


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


事情是这样的


1.fs.createWriteStream()`创建一个可写流。

2.我们使用 `.write()`向其写入一些文本。

3.完成后，我们调用 `.end()` 关闭数据流。

4.当写入所有数据后，就会发出 "完成 "事件。

5.如果出错，就会触发 "error "事件。


与可读流一样，可写流也适用于大数据，因为它们不需要同时将所有内容保存在内存中。


### 管道流


流最酷的一点是，你可以将它们**管道**在一起：将可读流直接连接到可写流。


```javascript
const fs = require("fs")

const readable = fs.createReadStream("bigfile.txt")
const writable = fs.createWriteStream("target.txt")

readable.pipe(writable)
```


给你



- 可读取流从 `bigfile.txt` 中读取。
- 可写流写入 `copy.txt`。
- .pipe()`直接将数据从可读流发送到可写流。


### 双向流


双工流既可读又可写。网络套接字就是一个例子：你可以向它发送数据，也可以从它接收数据。


下面是一个使用 `net` 模块的简单示例：


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


在这个例子中



- socket` 对象是一个双工流。
- 您可以对其进行 "写入() "操作，也可以监听其中的 "数据 "事件。


### 转换流


转换数据流是一种双工数据流，它还能修改通过它的数据。


例如，您可以使用内置的 `zlib` 模块来压缩或解压数据。


下面介绍如何使用转换流压缩文件：


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


并把它减压回去：


```javascript
const readable = fs.createReadStream("bigfile.txt.gz")
const unzip = zlib.createGunzip()
const writable = fs.createWriteStream("bigfile.txt")

readable.pipe(unzip).pipe(writable)

writable.on("finish", () => {
console.log("File decompressed.")
})
```


转换流对于压缩、加密或在流式传输过程中更改文件格式等任务非常有用。


### 背压


有时，可写流处理数据的速度很慢。如果我们不断向可写数据流推送数据的速度超过了它的处理速度，就可能会出现问题。这就是所谓的**回压**。


如果在可写数据流上调用 `.write()`方法，它会返回一个布尔值，告诉你数据流是否需要暂停；你可能需要检查它的返回值，就像这样：


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


这是一个手动将数据从可读管道输送到可写管道并手动管理背压的示例。


通常，我们会使用 `.pipe()`方法来传输数据，该方法会自动处理背压。


因此，只有在出于某种原因手动调用 `.write()`时，才需要担心背压问题。


## 最后说明

<chapterId>139e2ab8-df67-525a-85f0-5a2fa5e478f2</chapterId>


就这样，如果你跟上了课程，现在应该能用 NodeJS 编写一些简单的程序了。


我建议你这样做：在学习了基础知识后，建立一些个人项目是练习并成为一名更好的程序员的最佳方式。


构建什么并不重要，重要的是你要挑战自己，用代码解决问题。


现代编程语言的功能非常强大，而 NodeJS 可能是您在这一阶段进行尝试的最佳工具箱。


祝你好运


# 最后一节


<partId>322624d8-6fbc-11f0-a67a-5b145f10afc1</partId>


## 评论与评级


<chapterId>3e93ac86-6fbc-11f0-8bae-9b2ed7914843</chapterId>

<isCourseReview>true</isCourseReview>

## 结论


<chapterId>49b3b9b2-6fbc-11f0-9870-5f5adcd3a0eb</chapterId>


<isCourseConclusion>true</isCourseConclusion>