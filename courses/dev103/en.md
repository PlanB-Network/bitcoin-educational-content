# Basic JavaScript

## Setup

In this section we're gonna setup our machine to write and execute our first JavaScript program.

A JavaScript program is just a collection of (one or more) text files, that contain commands to be executed by a JavaScript runtime.

The names of these text files usually end with a `.js` file extension, like `my_script.js`, `my_program.js` etc.

The commands they contain are written in the JavaScript programming language.

A JavaScript runtime is a special program that executes these files.

### NodeJS installation

The most common JavaScript runtime is NodeJS.

You can install it by following the [official instructions](https://nodejs.org/en/download).

The download page will provide you with instructions for all three of the major OSs (Operating Systems): Windows, Linux and MacOS. It assumes you know how to open a terminal in your OS.

Since NodeJS is available for all three OSs, the programs that you write will be able to be executed on all of them (barring some edge cases).

This means you can, for example, write a simple videogame in JavaScript on your Windows PC and pass it to your friend to run it on his Mac.

### Text editing

One of the cool things about programming is that you can write code using any text editor, even the default notepad of your OS.

There are some text editors that are specialized for writing code though, some are available for free, others require you to pay for a license. 

The choice of code editor is a giant rabbit hole that transcends the scope of this course, so we're not gonna talk about it here. If you don't know what to use, the most used free editor is [VSCode](https://code.visualstudio.com/). 

Its interface is a little bloated, but it has what you need: a file editor, a file explorer (to visualize the files and subdirectories in the directory you're working on), and a terminal to run your code. It also supports a lot of plugins, and it comes with JavaScript syntax highlighting by default.

If you want to be a little more cypherpunk-y, you can use [VSCodium](https://vscodium.com/) instead.

### First program (hello world)

Traditionally, when studying a programming language, the first program one writes consists in printing "hello world!" to the console.

Create a directory called `my_js_code/`, with inside a file called `main.js` (these names are arbitrary).

Open the directory with VSCode.

Write this code into your file:

```javascript
console.log("hello world!")
```

Open a terminal and execute this command to run the program:

```
node main.js
```

The result should be 

```
hello world!
```

### What Happened

In JavaScript, everything is an "object".

`console` is an object, which is used to debug the program.

`console.log` is the most used method of the `console`. It just prints whatever arguments you pass to it.

You pass arguments to `console.log` using the round brackets `()`.

So for example, if you wanted to print the number `1000`, you'd just write

```javascript
console.log(1000)
```

Then execute it by running 

```
node main.js
```

in your terminal (from now on, this course will assume that you know this is how you execute a program).

This should print

```
1000
```

You can pass multiple things, like

```javascript
console.log(16, 8, 1993)
```

This will print

```
16 8 1993
```

## Variables and comments

Programs usually execute operations on data.

Variables are like named boxes that we use to store data. They allow us to associate a piece of data with a specific name, so that we can retrieve it later using that name.

### `let` declarations

To declare a variable in JavaScript, we can use the `let` keyword.

After writing `let`, we write the name we want to give to the variable, then an `=` sign, and then the value we want to store.

For example:

```javascript
let age = 25

console.log(age)
```

The name of a variable (technically called the "identifier") can usually contain letters, underscores (`_`), the dollar sign (`$`) and numbers, although the first character cannot be a number.

In the code above, we declared a variable called `age` and stored the value `25` in it.

Then, we printed the value using `console.log(age)`.

If you run this code with `node main.js`, the output will be:

```
25
```

Identifers are case-sensitive, which means lower and upper-case count as differences in identifiers, so for example

```javascript
let age = 25

let Age = 20

console.log(age)
```

will print 25, because those are considered two completely separate variables!

You can also store strings (text) in a variable:

```javascript
let message = "hello again"

console.log(message)
```

This will print:

```
hello again
```

Just like before, we used `console.log()` to print the value stored in the variable.

Now let’s do both together:

```javascript
let age = 25

let message = "hello again"

console.log(age)

console.log(message)
```

Running this will print:

```
25
hello again
```
### Reassignment

Variables declared with `let` can be changed after they are created. 

This is called reassignment.

```javascript
let score = 10

console.log(score)

score = 15

console.log(score)
```

First, we assign `10` to `score`, then print it. 

Then we change the value of `score` to `15` and print it again.

The output will be:

```
10
15
```

This is very useful when the value changes over time, like in a game where the score increases.

Let’s add another variable to the mix:

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

This will print:

```
10
Alice
20
Bob
```

As you can see, both `score` and `player` were changed.

### `const` declarations

Most of the times though, we don’t want a variable to change after it is created. For that, we use `const`.

`const` is short for “constant”. Once you assign a value to a `const` variable, you cannot change it.

```javascript
const pi = 3.14
console.log(pi)
```

This prints:

```
3.14
```

But if you try to do this:

```javascript
const pi = 3.14
console.log(pi)

pi = 99 // this line will cause an error
console.log(pi)
```

JavaScript will give you an error like:

```
TypeError: Assignment to constant variable.
```

This is because `pi` was declared using `const`, and you cannot change its value after that. You're communicating to the JavaScript interpreter that you don't want that variable to change.

This is useful because it reduces the chances of changing it by mistake. When programs become very big, with thousands of lines of code, it's impossible to keep up with everything that is happening all at once (that's the main reason we use computers, to execute complex processes that we cannot compute with our brains), so it becomes useful to have restrictions like this, that make the program more deterministic.

It is considered best practice to always declare our values as `const`, unless we're sure we want to modify them later.

### Comments in JavaScript

Sometimes we want to write notes in our code that are not executed. These are called comments.

Comments are ignored by the program when it runs, but are useful for explaining things to ourselves or other people.

To write a single-line comment, use `//`

```javascript
// This is a comment
const x = 10 // This is also a comment
console.log(x)
```

This will still print:

```
10
```

The comments are just there for humans to read.

You can also write multi-line comments using `/*` and `*/`

```javascript
/*
  This is a multi-line comment.
  It can span several lines.
*/
const y = 20
console.log(y)
```

This will print

```
20
```

And the comment will be ignored.

You can use comments to add small annotations to your code, so that you might remember what it does and why is it written in a certain way. It can also help other programmers understand it.

## Basic types: numbers, strings, booleans

In JavaScript, a “type” tells you what kind of data a value is.

Javascript has a few basic types, and in this section we'll explore some of them.

### Numbers and arithmetic operations

The first type we're gonna introduce is `number`.

Numbers in JavaScript can be integers (like `5`) or decimals (like `3.14`). 

You can do arithmetic with them: addition, subtraction, multiplication, and division.

Here’s a basic example:

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

This will print:

```
15
5
50
2
```

You can also use parentheses `()` to control the order of operations:

```javascript
const result = (2 + 3) * 4
console.log(result)
```

This prints:

```
20
```

Without the parentheses, it would be `2 + 3 * 4`, which is:

```javascript
const result = 2 + 3 * 4
console.log(result)
```

That would print:

```
14
```

Because in regular math, multiplication happens before addition.

### Strings and interpolation

The second JavaScript type we're gonna introduce is `string`.

Strings are pieces of text. You can use single quotes `'...'` or double quotes `"..."` to create them.

```javascript
const greeting = "hello"
const name = 'Bob'
console.log(greeting)
console.log(name)
```

This prints:

```
hello
Bob
```

To combine strings, you can use the `+` operator:

```javascript
const greeting = "hello"
const space = " "
const name = "Bob"

const fullGreeting = greeting + space + name 
console.log(fullGreeting)
```

This will print:

```
hello Bob
```

But there is a nicer way to combine strings called **string interpolation**. You use backticks to declare the string `` `...` `` and write variables using `${...}` inside the string:

```javascript
const greeting = "hello"
const name = "Bob"

const fullGreeting = `${greeting} ${name}`
console.log(fullGreeting)
```

This also prints:

```
hello Bob
```

You can include any expression inside `${...}`:

```javascript
const age = 30
console.log(`Next year, I will be ${age + 1} years old.`)
```

This prints:

```
Next year, I will be 31 years old.
```

Interpolation is very common in modern JavaScript.

### Booleans, comparison and logic operations

The third type we're gonna introduce is `boolean`. It is named after the mathematician George Boole, who invented boolean logic.

Booleans are simple: only two possible values, `true` and `false`.

You can store them in variables:

```javascript
const theSkyIsBlue = true
const thisCourseIsBad = false

console.log(theSkyIsBlue)
console.log(thisCourseIsBad)
```

This prints:

```
true
false
```

You can combine booleans using logic operators:

* `&&` means “and”, and it will return `true` only if **both** values are `true`, otherwise it will return `false`
* `||` means “or”, and it will return `true` if **at least one** of the values is `true`, otherwise (if they're both false) it will return `false`
* `!` means “not”, it's applied before a boolean,  and it will flip it: if the boolean it's `true` it will return `false`, and vice versa.

Examples:

```javascript
const isSunny = true
const isWarm = true

console.log(isSunny && isWarm)  // true
console.log(isSunny || isWarm)  // true
console.log(!isSunny)           // false
```

You can compare values in JavaScript using operators like `>`, `<`, `===`, and `!==`. The result of these comparisons is always a boolean.

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

Javascript also has `>=` to mean "bigger or equal" and `<=` to mean "smaller or equal.

Booleans, comparison and logical operators are often combined in programs to declare complex conditions, like to ensure "the email has arrived AND it contains the image I need OR the length of the email is longer than 10000 characters". You will find later that these are essential building blocks to construct the logic of the program.

## Arrays, null, undefined

In this section, we’ll cover three more types that are very common in JavaScript programs:

* **Arrays**: sequences of values
* **undefined**: a special value that means “nothing was assigned”
* **null**: another special value that means “intentionally empty”

### Arrays and index access

An **array** is a type that can hold multiple values in a list.

You create an array by using square brackets `[]` and separating the items with commas.

Here’s a basic example:

```javascript
const numbers = [10, 2, 88]
console.log(numbers)
```

This prints:

```
[ 10, 2, 88 ]
```

You can store anything in an array, not just numbers:

```javascript
const things = ["apple", 42, true]
console.log(things)
```

This prints:

```
[ 'apple', 42, true ]
```

To access a specific item in the array, we use an **index**. The index is the position of the item, starting from **0**.

So in this array:

```javascript
const colors = ["red", "green", "blue"]
```

* `colors[0]` is `"red"`
* `colors[1]` is `"green"`
* `colors[2]` is `"blue"`

Let’s try:

```javascript
const colors = ["red", "green", "blue"]
console.log(colors[0])
console.log(colors[1])
console.log(colors[2])
```

This will print:

```
red
green
blue
```

You can assign a value to a specific index of an array

```javascript
const colors = ["red", "green", "blue"]

colors[1] = "yellow"

console.log(colors)
```

This will print:

```
[ 'red', 'yellow', 'blue' ]
```

You can use any natural number as an index, even one stored in a variable

```javascript

const i = 1
const colors = ["red", "green", "blue"]
console.log(colors[i])
```

This will print:

```
green
```

But if you try to access an index that doesn’t exist, you will get `undefined`:

```javascript
const colors = ["red", "green", "blue"]
console.log(colors[3])
```

This prints:

```
undefined
```

What's that??

### `undefined`

The special value `undefined` means “no value was assigned”.

If you create a variable but don’t give it a value, it will be `undefined`:

```javascript
const name
console.log(name)
```

This prints:

```
undefined
```

Because we didn’t assign anything to `name`, JavaScript sets it to `undefined` by default.

As seen before, you can also get `undefined` when you access an array index that doesn’t exist:

```javascript
const fruits = ["banana", "apple"]
console.log(fruits[2]) // There is no index 2
```

This prints:

```
undefined
```

### `null` and how to treat it

`null` is also a special value. It means “nothing is here, and I did that on purpose.”

Unlike `undefined`, which is automatic, `null` is something you set yourself.

For example:

```javascript
const currentUser = null
console.log(currentUser)
```

This prints:

```
null
```

Why use `null`? Maybe you expect a value later, but it’s not ready yet:

```javascript
let winner = null

// Later in the program:
winner = "Alice"

console.log(winner)
```

This prints:

```
Alice
```

So `null` is useful when you want to say, for example, “There should be something here later, but right now it’s empty.”

## Blocks and control flow

So far, we’ve mostly written lines of code that run one after the other. 

But when we code, we can control the order of execution of it.

This is called **control flow**.

Let’s start with understanding blocks and scope.

### The global scope

Every variable we declare exists in a **scope**, which means the region of the code where the variable is known.

If you declare a variable outside of any block, it exists in the **global scope**.

```javascript
const color = "blue"
console.log(color)
```

This variable `color` is in the global scope, so it can be accessed from anywhere in the file.

If you add more lines:

```javascript
const color = "blue"
console.log(color)

const size = "large"
console.log(color)
console.log(size)
```

Both `color` and `size` are global variables. They are available everywhere in the file.

But what happens inside a block?

### Blocks and local scope

A **block** is a piece of code surrounded by curly braces `{}`.

Variables declared with `let` or `const` inside a block exist **only** inside that block.

```javascript
{
  const message = "inside block"
  console.log(message)
}
```

This prints:

```
inside block
```

But if you try this:

```javascript
{
  const message = "inside block"
}
console.log(message) // Error!
```

JavaScript will give you an error like:

```
ReferenceError: message is not defined
```

That’s because `message` was declared inside the block and doesn’t exist outside of it.

This means we can use blocks to isolate portions of our code, and be sure that "what happens in the block stays in the block" (kinda like Las Vegas).

Organizing our code in blocks allow us also to structure the execution of the program, with control flow constructs like `if`

### `if`, `else`

Sometimes we want to run code **only if** something is true. That’s what the `if` statement is for.

```javascript
const myAge = 20

console.log("Am I an adult?")

if (myAge >= 18) {
  console.log("Yes I am!")
}
```

This prints:

```
Am I an adult?
Yes I am!
```

As you can, see the code compares `myAge` and `18`. 
In this case the `>=` operator returns `true`, so the block gets executed.
If the condition is not `true`, the block doesn't get executed.

```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
  console.log("Yes I am!")
}
```

This prints:

```
Am I an adult?
```

You can add an `else` block to handle the opposite case:

```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
  console.log("Yes I am!")
} else {
  console.log("No, I am not.")
}
```

This prints:

```
Am I an adult?
No, I am not.
```

Both the `if` and `else` blocks are still blocks - so variables declared inside them don’t exist outside.

If we want to be sure that something is **not** true, what can we do?

Well, as previously discussed, JavaScript has a "not" operator, which flips booleans. So we can do

```javascript
const myAge = 17

const adult = myAge >= 18

console.log("Am I an adult?")

if (!adult) {
  console.log("No, I am not.")
}
```
This still prints:

```
Am I an adult?
No, I am not.
```
Because we used the `!` operator to invert the `adult` variable. 

`if (!adult) {...}` should be read as "if not adult..."

Using blocks, logic and comparison operators, we can structure the execution of the program, by defining variables that must be `true` (or `false`) for something to happen.

### `while`, `break`, `continue`

A `while` loop repeats code *as long as* a condition is true.

```javascript
let count = 0

while (count < 3) {
  console.log("Count is", count)
  count = count + 1
}
console.log("the loop is over!")
```

This prints:

```
Count is 0
Count is 1
Count is 2
the loop is over!
```

When `count` becomes 3, the loop stops.

You can stop a loop early using `break`:

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

This prints:

```
0
1
2
```

Because when the number becomes `3`, the `if` block gets executed and it stops the loop.

You can skip the rest of a loop using `continue`:

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

This prints:

```
1
2
4
5
```

Because when the number was `3`, `continue` made the program skip the line that prints the number.

### `for ... of ...`

If you have an array, and want to do something to every item in it, you can use `for ... of ... {...}`.

```javascript
const fruits = ["apple", "banana", "cherry"]

for (const fruit of fruits) { 
  console.log(fruit)
}
```

This prints:

```
apple
banana
cherry
```
The block will get executed once for each element of the array. 

`fruit` here is a new variable that takes the value of each item in the array, to operate on it inside the block.

### `for ... in ...`

You can use `for ... in` to loop over the keys (indexes) of an array:

```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
  console.log(index)
}
```

This prints:

```
0
1
2
```

You can use the index to get the value too:

```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
  console.log(fruits[index])
}
```

This prints the same as `for ... of`:

```
apple
banana
cherry
```

In practice, for arrays, you should prefer using `for ... of`, as it's simpler and cleaner. 

### Bounded loops

Sometimes we want to loop a specific number of times, or in general write a piece of code that repeats a block while keeping track of something. 
That’s what a bounded `for` loop is good for.
A bounded loop usually takes three conditions, separated by a semicolon `;`, as in `(... ; ... ; ....)`.

```javascript
for (let i = 0; i < 3; i = i + 1) {
  console.log(i)
}
```

This prints:

```
0
1
2
```

Let’s explain it:

* `let i = 0`: declares a variable to be used in the block (in this case it's a counter that starts at 0)
* `i < 3`: declares a condition to be `true` for the block to be executed ( in this case is "repeat while `i` is less than 3")
* `i = i + 1`: declare some code to be run after each execution of the block (in this case  "increase `i` by 1")

As you can see the bounded loop us to declare more complex conditions for the repeated execution of a piece of code, but most of the times it's not necessary.

### Block labels

If you have to write more complex control flow, JavaScript lets you name a block using a **label** that can be used by `break` or `continue` for specifying *where* to jump back.

Example:

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

This prints:

```
Inside outer block
Inside inner block
Done
```

We used `break outer` to exit the `outer` block entirely.

You can also label loops. Let's take this example:

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
This was a very boring example but hopefully it clarified the (occasional) need for labels.

## Introducing functions

As your programs grow, you'll often want to **reuse** pieces of code.

That’s what **functions** are for: they let you group some code together, give it a name, and run it whenever you want.

### Function declaration

To declare a function, we can use the `function` keyword. Then  we give it a name, a pair of parentheses `()` with the arguments it takes, and a block of code `{}` to be executed. Let's start with a function that takes no arguments:

```javascript
function sayHello () {console.log(`Hello!`) }
```

This code **declares** the function, but does **not** run it yet.

### Function calls

To run (or "call") the function, you write its name followed by parentheses:

```javascript
function sayHello () {console.log(`Hello!`) }
sayHello()
```

This prints:

```
Hello!
```

You can call the function as many times as you want:

```javascript
function sayHello() {
  console.log("Hello!")
}

sayHello()
sayHello()
```

This prints:

```
Hello!
Hello!
```

The code inside the function only runs when you call it.

### Function arguments (input to functions)

Sometimes, you want a function to work with some input. You can do that by adding **arguments** inside the parentheses.

For example:

```javascript
function sayHelloTo (friend) {
  console.log(`Hello ${friend}!`)
}
```

Now this function takes **one argument** called `friend`.

When you call the function, you can pass a value:

```javascript
sayHelloTo("Tommy")
```

This prints:

```
Hello Tommy!
```

You can call the function again with a different name:

```javascript
sayHelloTo("Sam")
```

This prints:

```
Hello Sam!
```

The value you pass in replaces the `friend` variable inside the function.

You can also use more than one argument:

```javascript
function greetTwoPeople(person1, person2) {
  console.log(`Hello ${person1} and ${person2}!`)
}

greetTwoPeople("Lina", "Marco")
```

This prints:

```
Hello Lina and Marco!
```

### `return` (output from functions)

Functions can also **return** values. This means they send a value back to wherever the function was called.

Here’s a simple example:

```javascript
function getNumber() {
  return 42
}

const result = getNumber()
console.log(result)
```

This prints:

```
42
```

The function `getNumber()` returns `42`, and we store it in `result`, then print it.

You can also return something you calculate:

```javascript
function add(a, b) {
  return a + b
}

const result = add(2, 3)
console.log(result)
```

This prints:

```
5
```

Once a value is `return`ed, the function stops. Anything after `return` in that block doesn’t happen.

```javascript
function saySomething() {

  return "hi"
  
  console.log("this never runs")

}

const message = saySomething()
console.log(message)
```

This prints only:

```
hi
```

because only `"hi"` gets returned. The `console.log("this never runs")` line is skipped.

You can think of functions as small sub-programs. Each function can take some input, work on it, and give you back some output. 

What happens if  we try to use the return value of a function, but that function didn't return anything?

```javascript
function doesNothing () {}

const x = doesNothing()

console.log(x)
```
This will print `undefined`. The return value of a function that didn't return anything is `undefined`.

## Objects and classes

JavaScript is often called an object-oriented language. 

That means it helps you organize your code by grouping values and functions together into **objects**.

### What is an `object` ?

An object can contain data and functions that operate on that data. When a function is put into an object we say it's a `method`.

The first object we've seen was the `console` object. It's an object that contains multiple methods to print thing on the screen and debug our programs. 

It can even print itself; you can do

```javascript
console.log(console)
```

and it will print a list of the methods that it contains. For example, on my machine it printed

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

As you can see, it has a lot of methods that you could use to debug!

Javascript provides us with different way to create new objects that can do whatever we want them to do. 

### Creating an object

The easiest way to create an object is just by grouping data and functions using **curly braces** `{}`. 

This creates what we call an **anonymous object**

```javascript
const cat = {
  name: "Whiskers",
  age: 3
}
```

This creates an object and stores it in a variable called `cat`.

The object has two **properties**:

* `name` with the value `"Whiskers"`
* `age` with the value `3`

Let’s print it:

```javascript
console.log(cat)
```

This prints:

```
{ name: 'Whiskers', age: 3 }
```

You can get the properties out of the object using a dot, as in `objectName.propertyName`:

```javascript
console.log(cat.name)  // prints "Whiskers"
console.log(cat.age)   // prints 3
```

You can also **change** a property:

```javascript
cat.age = 4
console.log(cat.age)  // now it prints 4
```

As you can see, even if an object is defined as `const`, you can still modify the data it contains. 

In the case of objects, `const` will only stop you from overriding the whole object:

```javascript
const cat = {
  name: "Whiskers",
  age: 3
}

cat.age = 5 // this works

cat = 5 // this throws an error, you're trying to reassign the whole object

```

As mentioned before, objects can also hold **functions**, and when a function is part of an object, we call it a **method**.

Here’s an example:

```javascript
const cat = {
  name: "Whiskers",
  speak () {
    console.log("Meow!")
  }
}
```

This object has:

* A `name` property
* A `speak()` method

Let’s call the method:

```javascript
cat.speak()
```

It prints:

```
Meow!
```

Methods can use the data the object contains through the keyword `this`.
`this` refers to the current object. In this example, it will be used to print the name of the cat:

```javascript
const cat = {
  name: "Whiskers",
  speak () {
    console.log(`${this.name} says meow!`)
  }
}

cat.speak()
```

This prints:

```
Whiskers says meow!
```

The word `this` means "this object"...in this case, the `cat` object.


These kinds of objects are great when you just want something quick and simple. But if you need to create **many objects** with the same structure, there’s a better way, and that’s where **classes** come in.

### Classes and constructors

A **class** is like a blueprint. It tells JavaScript how to create a certain kind of object.

You define a class using the `class` keyword, followed by the name of the class, and by a curly braces `{}` block.

```javascript
class Dog {}
```

Classes usually start with an upper case letter, by convention.

You can create a new object of a class using `new`:

```javascript
const hachiko = new Dog()
```

Try to print the object:
```javascript
class Dog {}

const myDog = new Dog()

console.log(myDog)
```

You'll get

```
Dog {}
```

As you can see the Dog class is empty, so the `myDog` object is empty too.

We can define which properties Dog objects should contain by adding a `constructor`.

A constructor is a special function that runs when you create (or "construct") a new object.

```javascript
class Dog {
  constructor() { }
}
```

We want each Dog to have a name, so we add a `name` parameter to the function:

```javascript
class Dog {
  constructor(name) { }
}
```

And then we use `this` to declare that `name` is the `name` of the `Dog` object we're building

```javascript
class Dog {
  constructor(name) {
    this.name = name
  }}
```

Let's try to use it now:

```javascript
class Dog {
  constructor(name) {
    this.name = name
  }
}

const myDog = new Dog("hachiko")

console.log(myDog)
```

This prints something like:

```
Dog { name: 'hachiko' }
```

As you can see, the `constructor` method takes the arguments you pass to the class when you do `new Dog()`, and it uses it to build the object.

Let’s break it down:

* `class Dog` defines the Dog class.
* `constructor(name)` sets up the object when it’s created.
* `this.name = name` stores the value in the new object.
* `new Dog("hachiko")` creates a new object from the class, with the `name` property set to `"hachiko"`.

Now let's add a method to our class:

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

This will print

```javascript
hachiko says barf!
```

If we do the same for two different instances of Dog


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

we get

```
hachiko says barf!
bobby says barf!
```

the `speak()` method uses the `name` property of the `Dog` it's called on.

This is the main reason classes exist: they allow us to define a set of methods that operate on data, and then create multiple objects that share the same data "shape".

When we call a method on one of these objects, it will operate on the data *that specific object* holds.

### Changing the shape of an object

Objects in JavaScript are flexible. Even after you've created one, you can still add new properties or remove existing ones.

It's allowed, but it's something you should use carefully.

Let’s start with our simple `Dog` class:

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

At this point, `myDog` only has one property: `name`. We can still add new properties after it’s created:

```javascript
myDog.age = 5

console.log(myDog.age) // prints 5
```

We can also add a new method:

```javascript
myDog.jump = function () {
  console.log(`${this.name} jumps!`)
}

myDog.jump() // Fido jumps!
```

And we can remove properties too, using the `delete` keyword.

```javascript
delete myDog.name

console.log(myDog.name) // prints 'undefined'
```

This works, but here's something important to know: JavaScript engines like the V8 (used in Node.js and in the Chrome browser) run faster when your objects always maintain the same properties. If you add or remove properties after the object is created, it can slow things down.

In small programs, this doesn’t matter much. But in bigger projects (like games), it’s better to list all the properties in the constructor from the start, even if you don’t use them right away. This keeps the object shape stable and helps your code run faster.

For example, instead of this:

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

You could do

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

Both versions work, but the second one is better for performance. You're telling the engine up front which properties each object will have, and it can optimize accordingly. 

JavaScript lets you reshape objects freely, but when using classes, it’s best to plan your object’s shape ahead of time.


### Inheritance with `extends` and `super()`

Sometimes you want to create a class that’s *almost* the same as another class, but with a few extra features. 

Instead of modifying the shape of objects (which as mentioned before it's not optimal for performance), or having to rewrite a new class from scratch, JavaScript lets you use something called **inheritance**.

Inheritance means one class can **extend** another. The new class gets all the properties and methods of the old one, and you can add more or change what you need.

Let’s say we have a base class called `Vehicle`:

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

Now we want to make a `Car` class. A car is a kind of vehicle, but we might want it to have some extra features or a different message when it starts. Instead of rewriting everything, we can use `extends`:

```javascript
class Car extends Vehicle {
  start() {
    console.log(`${this.brand} car is ready to drive!`)
  }
}
```

The `Car` class now **inherits** everything from `Vehicle`. It gets the `brand` property, and we’ve replaced the `start()` method with our own version.

Let’s try it out:

```javascript
const myCar = new Car("Toyota")
myCar.start()
```

This prints:

```
Toyota car is ready to drive!
```

Even though `Car` doesn’t have its own constructor, it still uses the one from `Vehicle`. But if we want to write a custom constructor in `Car`, we can, we just need to include a call to the constructor of its parent using `super()`.

Here’s how:

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

This prints:

```
Toyota Corolla is ready to drive!
```

So to summarize

* `extends` means one class is based on another.
* `super()` is used to call the constructor of the class you're extending.
* The new class gets all the properties and methods of the original class.
* You can **override** methods (like `start()`) to make them do something different.

This is helpful when you have several things that are similar (like cars, trucks, and bikes) and you want them to share code but still behave in their own way.

### `instanceof`

The `instanceof` keyword checks if an object was created from a certain class.

Let’s say we have a class called `User`:

```javascript
class User {
  constructor(username) {
    this.username = username
  }
}

const regularUser = new User("julia123")

console.log(regularUser instanceof User)
```

This prints:

```
true
```

Confirming that `regularUser` is a `User`. That’s because `regularUser` was created using the `User` class.

It also works with **inherited** classes. For example, here’s an `Admin` class that extends `User`:

```javascript
class Admin extends User {}

const ourAdmin = new Admin("admin42")

console.log(ourAdmin instanceof Admin)   // true
console.log(ourAdmin instanceof User)    // true
```

Both lines return `true`. That’s because `Admin` is a subclass of `User`, therefore `ourAdmin` is both an `Admin` and a `User`

# Intermediate JavaScript

## Error Handling

As you write more complex JavaScript programs, you'll encounter **errors**. These are unexpected situations where something goes wrong. Maybe a variable is `undefined` but you try to use it, or some code receives the wrong type of input.

If we don’t handle these errors properly, our program might crash or behave in unpredictable ways. JavaScript provides tools to detect and manage these errors so we can handle them more gracefully.

### Common error: accessing a value on `undefined`

Here’s a common situation that causes an error:

```javascript
const user = undefined
console.log(user.name)
```

If you run this code, you’ll get an error that looks like this:

```
TypeError: Cannot read properties of undefined (reading 'name')
```

That’s JavaScript telling you: “Hey, you tried to get the `name` property from something that’s `undefined`, and that doesn't make sense.” And as you can see, when this kind of error happens, the program stops running unless you’ve specifically written code to catch and handle it.

### `throw`ing an error

Sometimes you want to manually **raise an error** in your code. In that case, you use the `throw` keyword.

```javascript
throw new Error("This is a custom error message")
```

This immediately stops the program and prints:

```
Uncaught Error: This is a custom error message
```

You can use `throw` to enforce rules in your program. For example:

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

The second call causes an error because dividing by zero is not allowed in this example.

### Catching errors with `try...catch`

If you don’t want your program to crash when an error occurs, you can catch the error using a `try...catch` block. This is helpful when you want your program to **keep going** even if something fails.

```javascript
try {
  const user = undefined
  console.log(user.name)
  console.log("End of the block") // this will never get printed
} catch (error) {
  console.log("Oops! Something went wrong.")
}
```

Output:

```
Oops! Something went wrong.
```

Here’s how it works:

* The code inside the `try` block is attempted first.
* If an error occurs, JavaScript **jumps to the `catch` block**, skipping the rest of the `try` block.
* The `catch` block receives the error, so you can print it, or handle it in some other way, like for example

```javascript
try {
  const user = undefined
  console.log(user.name)
  console.log("End of the block") // this will never get printed
} catch (error) {
  console.log(`The message of the error was: "${error.message}"`)
}
```

Output:

```
The message of the error was: "Cannot read properties of undefined (reading 'name')"
```

### The `finally` block

You can also add a `finally` block. This is code that **always runs**, whether there was an error or not.

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

Output:

```
Trying something risky...
Caught the error: Uh oh!
This will run no matter what.
```

## Avoiding Bugs

This chapter shows some of the most common pitfalls in JavaScript, and how to avoid them.

### `var` and assignment without declaration

In older JavaScript code, variables were often declared using the `var` keyword. Unlike `let` and `const`, which you've already learned about, `var` might behave in confusing ways.

For example:

```javascript
{
  var message = "hello"
}
console.log(message)
```

You might expect `message` to only exist inside the block, but it doesn’t. `var` ignores block scope and it makes the variable available throughout the entire function or file.

This can lead to unexpected behavior, especially in larger programs. For this reason, modern JavaScript code should always use `let` or `const` instead of `var`.

Even worse, JavaScript lets you assign values to variables **without declaring them at all**:

```javascript
function greet() {
  user = "Alice"
}
greet()
console.log(user) // prints "Alice"
```

This creates a new global variable `name` without any declaration. This can happen silently and lead to bugs that are hard to track down, especially if it was just a typo. Always declare variables using `let` or `const`.

### Weak type system

JavaScript is weakly typed, meaning it automatically converts values from one type to another if needed. This is called type coercion, and while it can be convenient, it often leads to confusing results.

For example:

```javascript
console.log("5" + 1)    // "51"
console.log("5" - 1)    // 4
console.log(true + 1)   // 2
console.log(null + 1)   // 1
```

In these examples, JavaScript tries to guess what you meant. Sometimes it turns strings into numbers, or booleans into numbers, or strings into strings. This can make your code behave in unexpected ways.

Being aware of JavaScript's weak typing system is important. When things start acting strangely, it might be due to unexpected type coercion.

### `"use strict"`

You can enable a stricter mode that turns some silent errors into real errors, and stops you from using some of the more dangerous features of the language.

To enable this stricter mode, add this line at the top of your file or function:

```javascript
"use strict"
```

For example:

```javascript
"use strict"
name = "Alice" // ReferenceError: name is not defined
```

Without strict mode, JavaScript would silently create a global variable called `name`. But with strict mode, this becomes a real error, helping you catch bugs earlier.

Strict mode also disables some outdated features of JavaScript, and makes your code easier to optimize and maintain.

## Value vs Reference

JavaScript treats different kinds of values in different ways.

Some values are **copied** when you assign them to a variable.

Others are **shared** when you assign them to a new variable, so if you change one, the other one changes too.

### Pass by value

When a value is passed **by value**, JavaScript makes a **copy** of it.

So if you change one, it doesn’t affect the other.

This happens with primitive types, like:

* numbers
* strings
* booleans (`true` and `false`)
* `null`
* `undefined`

Let’s look at an example:

```javascript
let a = 5
let b = a

b = 10

console.log(a) // 5
console.log(b) // 10
```

We gave `b` the value of `a`, but then we changed `b` to `10`.

Since numbers are passed by value, JavaScript copied the `5` into `b`. The `5` in `b` is independent from the original `5` in `a` so changing the value of `b` had no effect on `a`.

Let’s try with a string:

```javascript
let name1 = "Alice"
let name2 = name1

name2 = "Bob"

console.log(name1) // Alice
console.log(name2) // Bob
```

Again, changing `name2` didn’t affect `name1`, because strings are also passed by value.

The same thing happens when you pass a primitive to a function: it gets copied. So the function can’t change the original.

```javascript
function plusOne(x) {
  x = x + 1
}

let number = 5

plusOne(number)

console.log(number) // 5
```

Even though inside the function `1` was added to `x`, the original `number` didn’t change.

That’s because only a **copy** was passed into the function.

### Pass by reference

Objects are passed **by reference**.

That means instead of copying them, JavaScript just passes a **reference** to it, and if you modify it, all other variables that point to it will see the change too.

For example:

```javascript
const person1 = { name: "Alice" }
const person2 = person1

person2.name = "Bob"

console.log(person1.name) // Bob
console.log(person2.name) // Bob
```

Both `person1` and `person2` point to the same object in memory.

So when we changed `person2.name`, we also changed `person1.name`, because they’re both looking at the same thing.

Arrays are objects, so let’s try the same with an array:

```javascript
const list1 = [1, 2, 3]
const list2 = list1

list2.push(4)

console.log(list1) // [1, 2, 3, 4]
console.log(list2) // [1, 2, 3, 4]
```

We pushed `4` into `list2`, but `list1` was affected too, because they both refer to the same array.

Let’s see what happens when we pass an object to a function:

```javascript
function rename(user) {
  user.name = "Charlie"
}

const person = { name: "Dana" }

rename(person)

console.log(person.name) // Charlie
```

The function changed the object! That’s because it received a **reference** to the original `person` object.

It didn’t get a copy. It got access to the original object, and with that it got the ability to modify it.

It's important to remember this distinction, because otherwise our code might behave differently from what we expect. For example, we might write a function with the expectation that it will not modify the arguments it receives, and find out later that it was actually modifying them (because they were objects, so they were passed by reference).

## Working with Functions

You’ve already learned how to declare and use functions in JavaScript. But JavaScript gives you more tools to work with functions in powerful ways.

### Arrow functions

Arrow functions are a shorter way to write functions. Instead of using the `function` keyword, we use an arrow (`=>`).

Here’s a normal function:

```javascript
function greet(name) {
  return `Hello, ${name}!`
}
```

The arrow version looks like this:

```javascript
const greet = (name) => {
  return `Hello, ${name}!`
}
```

If the function has **only one line**, you can skip the braces and `return`:

```javascript
const greet = (name) => `Hello, ${name}!`
```

If the function has **only one parameter**, you can even skip the parentheses around the parameters:

```javascript
const greet = name => `Hello, ${name}!`
```

Arrow functions are very common in modern JavaScript, as they allow to express simple functions with significantly less boilerplate.

### Default parameters

Sometimes you want a function to have a **default value** if no argument is passed.

You can do that like this:

```javascript
function sayHello(name = "friend") {
  console.log(`Hello, ${name}!`)
}

sayHello("Alice") // Hello, Alice!
sayHello()        // Hello, friend!
```

The default value `"friend"` is used when nothing is passed in.

### Spread parameters (`...`)

What if your function takes a flexible number of arguments?

You can use the **spread operator** (`...`) to gather them into an array:

```javascript
function logAll(...items) {
  console.log(items)
}

logAll(1, 2, 3) // [1, 2, 3]
logAll("a", "b") // ["a", "b"]
```

You can then use a loop to process each item:

```javascript
function logEach(...items) {
  for (const item of items) {
    console.log(item)
  }
}
```

The spread operator is useful when you don’t know how many arguments will be passed.

### Higher-order functions

A **higher-order function** is a function that:

* takes another function as input
* and/or returns a function as output

Here’s a simple example:

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

This prints:

```
Hello, friend!
Hello, friend!
```

We can pass an arrow function to it:

```javascript
runTwice(
  () => console.log("Hello!") 
)
```

This prints:

```
Hello!
Hello!
```

You can also write functions that **return** other functions:

```javascript
function makeGreeter(name) {
  return () => console.log(`Hi, ${name}`)
}

const greetAlice = makeGreeter("Alice")
const greetBob = makeGreeter("Bob")

greetAlice() // Hi, Alice
greetBob() // Hi, Bob
```

The `makeGreeter` function is a function that builds other functions. It receives a string and returns a new function that uses that string in its `console.log` call.

This kind of pattern is very powerful, as it allows you to leave "holes" in your functions that you can fill later with the behavior you need.

### `map()`, `filter()`, `reduce()`

JavaScript gives you some useful built-in methods to use with arrays.

These methods take functions as arguments, so they are also higher-order functions.

`map()` transforms each item in an array into something else.

Example:

```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map(x => x * 2)

console.log(doubled) // [2, 4, 6]
```

Each number is doubled, and the result is a new array.

`filter()` removes items from the array if they don’t pass a test.

Example:

```javascript
const numbers = [1, 2, 3, 4, 5]
const numbersGreaterThanTwo = numbers.filter(x => x > 2)

console.log(numbersGreaterThanTwo) // [3, 4, 5]
```

Only the array entries for which the `x > 2` condition returns `true` are kept.

`reduce()` is used to combine all the items in an array into a single value.

Example:

```javascript
const numbers = [1, 2, 3, 4]
const total = numbers.reduce((current, next) => current + next)

console.log(total) // 10
```

`reduce` goes through the array and, in this example, applies the `+` operator between `1` and `2`, then between the resulting `3` and `3`, then between the resulting `6` and `4`, until it has the sum of all the array entries (which is 10).

You can use `reduce()` for many things like totals, averages, or building new values step by step.

These methods (`map`, `filter`, `reduce`) are powerful tools to process data without writing manual loops.

You can even combine them in a chain of operations, like this:

```javascript
const numbers = [1, 2, 3, 4, 5]

const result = numbers
  .map(n => n * 2)        // Double each entry, obtain [2, 4, 6, 8, 10]
  .filter(n => n > 3) // Keep only the entries bigger than 3, so you get [4, 6, 8, 10]
  .reduce((n1, n2) => n1 + n2) // Adds them: 4 + 6 + 8 + 10 = 28

console.log(result) // 28
```

## Working with Objects

In this chapter, we'll learn some powerful and slightly more advanced tools for working with objects in JavaScript.

### Private Properties

Sometimes, we want to hide a property of an object so that it can't be changed or accessed from outside the object. JavaScript gives us a way to do this using `#` before the property name. This creates a **private** property, which is only accessible from inside the class.

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

Private properties are helpful when you want to prevent accidental changes.

### `static` Properties

Sometimes, you want a property to belong to the class itself, not to each object you create from that class. That's what `static` is for. A `static` property is contained in the class and all of the objects of that class will refer to it.

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

This is useful for for storing shared data and methods that applies to the whole group of objects, not just one.

### `get` and `set`

In JavaScript, `get` and `set` let you make properties that *look* like normal variables, but actually run special code in the background.

A `get`ter method runs when you try to *read* a property. It is declared by writing `get` before a method with the name of the property. 

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

Even though `fullName` is not a regular property, we can use it like one, and behind the scenes it runs the `get` function to build the full name.

A `set`ter method runs when you *assign* a value to a property. It lets you control what happens when someone tries to change that value. It is declared by writing `set` before a method with the name of the property. 

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

When we do `user.fullName = "John Smith"`, it runs the `set` method and updates the `firstName` and `lastName` values.

So even though it feels like we’re just setting a simple variable, we’re actually triggering logic that updates other properties.

## Keys and Values

Every property in a JavaScript object has a **key** (also called a property name) and a **value**.

For example:

```javascript
const user = {
  name: "Alice",
  age: 30
}
```

In this object, `"name"` and `"age"` are the keys, and "Alice" and `30` are their values.

### Dynamic Access

Sometimes, you don’t know the name of a property in advance...maybe you’re getting it from user input, or reading it from a variable. You can still access it using **bracket notation**, like `myObject["keyName"]`.

```javascript
const user = {
  name: "Alice",
  age: 30
}

console.log(user["name"]) // Alice
```

We passed the string `name` to the object in order to get the corresponding value. 

We can save a key to a variable and use it to access the corresponding value later, like

```javascript
const user = {
  name: "Alice",
  age: 30
}

const key = "name"

console.log(user[key]) // Alice
```

### Dynamic Assignment

You can also create or update object properties using variables as keys.

```javascript
const settings = {}

const key = "theme"
settings[key] = "dark"

console.log(settings) // { theme: "dark" }
```

This is helpful when you want to build an object step by step. For example:

```javascript
const user = {}

user["username"] = "bananaFan123"
user["email"] = "banana@fruit.com"

console.log(user)
// { username: "bananaFan123", email: "banana@fruit.com" }
```

You can even use a dynamic key *while creating* the object using square brackets:

```javascript
const key = "language"
const config = {
  [key]: "JavaScript"
}

console.log(config.language) // JavaScript
```

This is called a **computed property**. The value inside the square brackets is evaluated, and the result is used as the key.

### `Symbol` Type

In addition to strings, JavaScript also lets you use a special type called `Symbol` as an object key.

Let’s start with a simple example:

```javascript
const id = Symbol("userID")

const user = {
  name: "Bob",
  [id]: 12345
}

console.log(user[id]) // 12345
```

In this example, `id` is a Symbol. It’s not a string, but it still works as a key. If you try to log `user` to the console, you will see this:

```javascript
console.log(user) // { name: 'Bob', [Symbol(userID)]: 12345 }
```

Another important thing: every symbol you create is unique, even if they are created using the same string.

```javascript
const a = Symbol("label")
const b = Symbol("label")

console.log(a === b) // false
```

Symbols allow you to define keys that will not clash with regular keys. For example, let's say you have an object with a `name` property, but the object will be customizable by a user in the future, in ways you cannot predict, and that user might add a `name` property as well. If the original `name` property was defined with a string, it would be overwritten by the new one, like this:

```javascript
const obj = {
  name: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy' }
```

If we use a Symbol instead:

```javascript
const name = Symbol("name")

const obj = {
  [name]: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy', [Symbol(name)]: 'John' }
```

As you can see, the original `name` property is somehow preserved this way. This can be useful in certain edge cases.

## Utility Objects

JavaScript gives us some useful built-in objects that help us do things like debugging and math operations.

### Other `console` Methods

You've already seen `console.log`, which prints values to the screen.

There are some other useful methods available on the `console` object that can help you debug your programs.

#### `console.warn`

Prints a message in yellow (or with a warning icon in some environments):

```javascript
console.warn("This is just a warning.")
```

#### `console.error`

Prints a message in red, like an error:

```javascript
console.error("Something went wrong!")
```

#### `console.table`

Displays an array or object as a table:

```javascript
const users = [
  { name: "Alice", age: 25 },
  { name: "Bob", age: 30 }
]

console.table(users)
```

This prints a table like:

```
┌─────────┬────────┬─────┐
│ (index) │  name  │ age │
├─────────┼────────┼─────┤
│    0    │ 'Alice'│  25 │
│    1    │ 'Bob'  │  30 │
└─────────┴────────┴─────┘
```

This can be useful to visualize structured data.

#### `console.time` and `console.timeEnd`

You can measure how long something takes:

```javascript
console.time("timer")
for (let i = 0; i < 1000000; i++) {}
console.timeEnd("timer")
```

This prints something like:

```
timer: 2.379ms
```

Useful for some simple performance testing.

### The `Math` Object

JavaScript gives you a `Math` object with useful methods for doing calculations.

#### `Math.random()`

Returns a random number between 0 (inclusive) and 1 (exclusive):

```javascript
const r = Math.random()
console.log(r)
```

Example output:

```
0.4387429859
```

#### `Math.floor()` and `Math.ceil()`

* `Math.floor(n)` rounds **down** to the nearest integer
* `Math.ceil(n)` rounds **up** to the nearest integer

```javascript
console.log(Math.floor(4.9)) // 4
console.log(Math.ceil(4.1))  // 5
```

#### `Math.round()`

Rounds to the nearest integer:

```javascript
console.log(Math.round(4.4)) // 4
console.log(Math.round(4.6)) // 5
```

#### `Math.max()` and `Math.min()`

Returns the largest or smallest value from a list of numbers:

```javascript
console.log(Math.max(5, 9, 3)) // 9
console.log(Math.min(5, 9, 3)) // 3
```

#### `Math.pow()` and `Math.sqrt()`

* `Math.pow(a, b)` gives you `a` to the power of `b`
* `Math.sqrt(n)` gives you the square root of `n`

```javascript
console.log(Math.pow(2, 3))   // 8
console.log(Math.sqrt(16))    // 4
```

# Advanced JavaScript

## Other collections

JavaScript gives us some special collection types that go beyond regular arrays and objects. These include `Map` and `Set`.

They help you store and manage groups of values, but they work differently from what you've seen so far.

A `Map` is a collection of **key-value pairs**, just like an object. But it has some important differences:

* The keys can be **any value** not just strings.
* The order of the items is preserved.
* It has built-in methods to make working with it easier.

You create a new map like this:

```javascript
const myMap = new Map()
```

This creates an empty map. To add entries to it, use `myMap.set(key, value)`:

```javascript
myMap.set("name", "Alice")
```

This adds a key `"name"` with value `"Alice"`.

You can also use a number as a key:

```javascript
myMap.set(42, "The answer")
```

And even an object as a key:

```javascript
const objKey = { id: 1 }
myMap.set(objKey, "Object as key")
```

That would not work with regular objects, which only allow string keys.

To **get a value**, use `myMap.get(key)`:

```javascript
console.log(myMap.get("name"))     // Alice
console.log(myMap.get(42))         // The answer
console.log(myMap.get(objKey))     // Object as key
```

To **check if a key exists**, use `myMap.has(key)`:

```javascript
console.log(myMap.has("name")) // true
```

To **remove a key**, use `myMap.delete(key)`:

```javascript
myMap.delete("name")
```

To **clear the whole map**, use `myMap.clear()`:

```javascript
myMap.clear()
```

Maps are great for managing large collections of values, because accessing values on a large map gives usually much better performance than on a large object.

### `Set`

A `Set` is a collection of **values only** (no keys), where each value must be **unique**. That means:

* You can't have the same value twice
* The values are stored in the order you add them

You create a set like this:

```javascript
const mySet = new Set()
```

To **add values**, use `mySet.add(value)`:

```javascript
mySet.add(1)
mySet.add(2)
mySet.add(2) // duplicate, will be ignored
```

Even though we tried to add `2` twice, the set will only keep one copy.

To **check if a value is in the set**, use `mySet.has(value)`:

```javascript
console.log(mySet.has(2)) // true
console.log(mySet.has(3)) // false
```

To **remove a value**, use `mySet.delete(value)`:

```javascript
mySet.delete(2)
```

To **clear everything**, use `mySet.clear()`:

```javascript
mySet.clear()
```

A `Set` is useful when you want to keep a collection of unique values without having to manually check for duplicates:

```javascript
const numberArray = [1, 2, 2, 3, 4, 4, 4, 5]

const numberSet = new Set(numberArray)

console.log(numberSet) // Set(5) { 1, 2, 3, 4, 5 }
```

The `Set` avoids the duplicates for you.

## Iterators

Most things in JavaScript that you can loop over (like arrays, strings, maps, sets) are **iterable**: they can provide iterators for their contents.

An **iterator** is a special object in JavaScript that helps you go through a list of items **one at a time**.

### `Object` iterators

Unlike arrays or maps, regular objects **are not iterable** with `for...of`. If you try this:

```javascript
const user = {
  name: "Alice",
  age: 30
}

for (const value of user) {
  console.log(value)
}
```

You’ll get an error:

```
TypeError: user is not iterable
```

That’s because plain objects don’t have a built-in iterator. But JavaScript gives you other tools to loop over them.

#### `Object.keys()`

You can use `Object.keys(obj)` to get an array of the object’s **keys**, and then loop over it:

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

This prints:

```
name
age
```

#### `Object.values()`

To loop over the **values**, use `Object.values()`:

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

This prints:

```
Alice
30
```

#### `Object.entries()`

If you want **both the key and the value**, use `Object.entries()`:

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

This prints:

```
name is Alice
age is 30
```

Even though objects aren't iterable directly, these methods give you full access to their contents in a way that works well with `for...of`.

But how do iterators work?

### `Symbol.iterator`

The secret behind all iterables is a special **symbol** called `Symbol.iterator`.

This symbol is a built-in key that tells JavaScript: “This object can be iterated.”

When you call `myIterable[Symbol.iterator]()`, JavaScript gives you back an **iterator object** with a `.next()` method.

Let’s see what that looks like:

```javascript
const colors = ["red", "green", "blue"]

const iterator = colors[Symbol.iterator]()

console.log(iterator.next()) // { value: 'red', done: false }
```

Every call to `.next()` gives you the next value. When it’s done, it returns:

```javascript
{ value: undefined, done: true }
```

### `next()`

The `.next()` method is used to get the next item from the sequence.

Each time you call `.next()`, you get an object with two keys:

* `value`: the current item
* `done`: a boolean that tells you if the iteration is over

Let’s do a full example:

```javascript
const names = ["Lina", "Tom", "Eva"]      // declare an array
const iterator = names[Symbol.iterator]() // use the Symbol.iterator function to get an iterator for this array

let result = iterator.next()              // get the first element of the array

while (!result.done) {                    // repeat this loop until you reach the last element of the array, which is marked with { done: true }
  console.log(result.value)               // print the value of each element
  result = iterator.next()                // get the next element of the array
}
```

This prints:

```
Lina
Tom
Eva
```

This is how a `for...of` loop works under the hood: it uses this pattern with `.next()`.

You will get the same result with

```javascript
const names = ["Lina", "Tom", "Eva"]

for (const result of names) {
  console.log(result)
}
```

### Making a class iterable

You can also define your own **iterable class** by adding a `[Symbol.iterator]()` method.

Let’s say we want a class that represents a **range of numbers**, like from 1 to 5.

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

This prints:

```
1
2
3
4
5
```

Here’s what’s happening:

* We defined a class `Range`
* Inside the class, we implemented `[Symbol.iterator]()`, so JavaScript knows how to iterate it
* The `next()` method gives back each number one by one
* When we reach the `end`, it returns `{ done: true }`

Now our `Range` class works like an array, and we can use it in any loop that expects an iterable.

### Generator functions and `yield`

To make it easier to create iterators, JavaScript gives you **generator functions**, using the `function*` keyword (it's `function` with a `*` at the end) and the `yield` keyword.

Let’s try:

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

Each `yield` gives back a value, and **pauses** the function until the next `.next()` is called.

You can also loop over a generator with `for...of`:

```javascript
for (const num of numberGenerator()) {
  console.log(num)
}
```

This prints:

```
1
2
3
```

## Concurrency with callbacks

Until now, our code has been **synchronous**: it runs one line at a time, in order. But some things in the real world take time, and we don’t want the entire program to pause while waiting.

In this chapter we’re going to introduce a new concept: **concurrency**. It allows us to manipulate the order in which things gets done. This is useful when dealing with things like timers, user input, or reading files from disk. JavaScript offers different tools for doing concurrency.

### `setTimeout`

The function `setTimeout` lets you **run a function later**, after some time has passed.

Example:

```javascript
console.log("Start")

setTimeout(
   () => console.log("This runs after 2 seconds"), 
   2000
)

console.log("End")
```

This prints:

```
Start
End
This runs after 2 seconds
```

Even though `setTimeout` appears in the middle of the code, it doesn't block the rest. Instead, it schedules the function to run **later**, and immediately moves on.

The `2000` means 2000 milliseconds (which is 2 seconds).
Here's a more verbose and beginner-friendly rewrite of the **Callbacks** and **Promise** sections, using data manipulation and clear annotations throughout:

### Callbacks

A **callback** is just a function that we give to another function so it can be **called later**.

Let’s look at a real example using numbers. Imagine we have a list of numbers, and we want to double each one of them, and then apply a function (the callback) to the resulting "doubled" array, but we want to do it after a small delay, as if we were waiting for something slow (like loading data from the internet).

Here’s a function that does that using a **callback**:

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

Let’s try to use this function:

```javascript
const input = [1, 2, 3]

doubleNumbers(input, function(result) {
  console.log("Here is the doubled array:", result)
})
```

After 1 second, this prints:

```
Here is the doubled array: [ 2, 4, 6 ]
```

**What’s happening here?**

1. We pass `input` as the list of numbers we want to double.
2. We also pass a **callback function** that tells the program what to do *after* doubling.
3. Inside `doubleNumbers`, we simulate a delay using `setTimeout`, then we do the doubling.
4. Once that’s done, we call the callback on the resulting "doubled" array.

This technique works, but imagine you want to do **more steps** after that, like filter out small numbers and then add them up. You’d have to **nest** more callbacks like this:

```javascript
doubleNumbers(input, function(doubled) {
  filterBigNumbers(doubled, function(filtered) {
    sumNumbers(filtered, function(total) {
      console.log("Final result:", total)
    })
  })
})
```

This is hard to read and messy. This style is called **callback hell**, and it’s exactly what `Promise` was created to fix.

## Concurrency with Promises

A `Promise` is a built-in JavaScript object that represents a value that will **be ready in the future**.

We can create a Promise like this:

```javascript
const promise = new Promise((resolve, reject) => {
  // Do something that takes time here...

  resolve("It worked!") // This means everything went OK
})
```

The `new Promise()` part creates the promise.

Inside it, we give it a function with two parameters:

* `resolve`, is a function we call when everything is successful
* `reject`, is a function we call if something goes wrong

In the example above, we just resolve it immediately with the message `"It worked!"`.

### `.then()`

To do something **after** the promise is done, we use `.then()`:

```javascript
const promise = new Promise((resolve, reject) => {
  // Do something that takes time here...

  resolve(100) // This means everything went OK
})

promise.then(result => {
  console.log("The result is:", result)
})
```

This prints:

```
The result is: 100
```

The value we passed to `resolve()` gets sent to the function inside `.then()` as `result`.

Let’s simulate a task that takes 2 seconds using `setTimeout`:

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

This will wait 2 seconds and then print:

```
Done waiting!
```

### `reject()`

Let’s create a promise that **fails**:

```javascript
const failingPromise = new Promise((resolve, reject) => {
  reject("Something went wrong")
})
```

Now if we use `.then()` on this, nothing will happen, because `.then()` only handles success.

To handle errors, we use `.catch()`:

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

This prints only

```
Caught an error: Something went wrong
```

The value passed to `reject()` is sent to the `.catch()` function.

Let’s build a Promise that **sometimes works and sometimes fails**, based on some condition.

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

Now we can call this and handle both cases:

```javascript
checkNumber(5)
  .then(
    msg => console.log("Success:", msg)
  )
  .catch(
    err => console.log("Failure:", err)
  )
```

This prints:

```
Success: Positive number
```

And if we try with a different number:

```javascript
checkNumber(-1)
  .then(
    msg => console.log("Success:", msg)
  )
  .catch(
    err => console.log("Failure:", err)
  )
```

It prints:

```
Failure: Not a positive number
```

### Chaining operations using `Promise`s


We can rewrite our earlier example using `Promise`, and it will look much cleaner.

Let’s start by writing a new version of our doubling function, but this time, it returns a **promise**:

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

Now we can use `.then()` to tell JavaScript what to do with the result:

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

This prints:

```
Doubled numbers: [ 2, 4, 6 ]
```

So far, this works the same as the callback version, but now the code is easier to extend and read.

Let’s say we want to add more steps:

1. First, double all the numbers
2. Then, remove numbers smaller than 4
3. Finally, add them all together

We can write one function for each step, all using promises:

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

Now we can **chain** them together like this:

```javascript
const input = [1, 2, 3]

doubleNumbers(input)
  .then(filterBigNumbers)
  .then(sumNumbers)
  .then(
    result => console.log("Final result after all steps:", result)
  )
```

This prints:

```
Final result after all steps: 10
```

Let’s walk through what this does:

1. `doubleNumbers` doubles the array: `[2, 4, 6]`
2. `filterBigNumbers` removes anything ≤ 3: `[4, 6]`
3. `sumNumbers` adds the remaining numbers: `4 + 6 = 10`
4. Finally, we print the result.

Each `.then()` waits for the step before it to finish. So we can build a **chain of actions** without nesting. This makes the code more readable and easier to debug.

## Concurrency with `async`/`await`

We saw how `Promise` chains help us avoid callback hell, but they can still get a little hard to read when there are many steps involved.

That’s where `async` and `await` come in. They let us write asynchronous code **that looks like synchronous code**, which makes it easier to understand.

### What is `async`?

When you write the keyword `async` before a function, JavaScript automatically wraps the function’s return value in a Promise.

Let’s see a basic example:

```javascript
async function greet() {
  return "hello"
}
```

If you call this function:

```javascript
const result = greet()
console.log(result)
```

You’ll see this:

```
Promise { 'hello' }
```

Even though you just returned a string, JavaScript turns it into a Promise for you. You can get the actual value using `.then()` like this:

```javascript
greet().then( result => console.log(result) ) // prints "hello"
```

Or you can use `await`...

### What is `await`?

The keyword `await` tells JavaScript: “wait until this Promise is done, and then give me the result.”

But you can only use `await` **inside an async function**.

Let’s rewrite the example using `await`:

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

Now we can use the result as if it was a regular value.

Let’s do something a little more useful now.

### Simulating a delay with `await`

We’ll create a simple `wait` function that takes a quantity of milliseconds as argument and just resolves after that many milliseconds, without doing anything else:

```javascript
function wait(ms) {
  return new Promise(resolve => {
    setTimeout(resolve, ms)
  })
}
```

Let’s try using it:

```javascript
async function test() {
  console.log("waiting 2 seconds...")
  await wait(2000)
  console.log("done waiting")
}

test()
```

This prints:

```
waiting 2 seconds...
done waiting
```

You can think of `await` as “pause here until the promise is done, then continue.”

This allows you to write code in a **top-to-bottom** fashion that behaves asynchronously, without chaining `.then()` calls.

### Awaiting data

Let’s reuse our previous example, where we double numbers, then filter, then sum. But this time, we’ll use `async`/`await`.

We’ll create 3 functions that simulate waiting, and return Promises:

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

Now let’s write an `async` function to combine them:

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

This prints:

```
Final result: 10
```

This is much easier to read than chaining `.then()` or nesting callbacks.

It looks like a regular step-by-step program, but it still behaves asynchronously.

## Async Iterators

You already learned about **iterators** and how we can use `for...of` to loop over arrays and other iterable things.

But what if the data we want to iterate over takes time to arrive?

Sometimes we want to loop over things that arrive **asynchronously**, like messages from a chat, lines from a file, or numbers from a slow source.

To do that, JavaScript gives us **async iterators**.

### Async generator functions

The easiest way to create an async iterator is to use an **async generator function**.

We write it like this:

```javascript
async function* generateNumbers() {
  yield 1
  yield 2
  yield 3
}
```

This looks just like a regular generator, but with `async` before it.

We can now use `for await...of` to consume the values:

```javascript
async function run() {
  for await (const n of generateNumbers()) {
    console.log("Got number:", n)
  }

  console.log("Done!")
}

run()
```

This will print:

```
Got number: 1
Got number: 2
Got number: 3
Done!
```

So what’s the difference with a normal generator?

The difference is: we can now use `await` inside the generator.

Let’s make a delay helper again:

```javascript
function wait(ms) {
  return new Promise(resolve => setTimeout(resolve, ms))
}
```

Now let’s yield numbers **slowly**:

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

Try using it:

```javascript
async function run() {
  for await (const n of generateSlowNumbers()) {
    console.log("Got number:", n)
  }

  console.log("Done!")
}

run()
```

### Why use async iterators?

Async iterators are useful when:

* The values don’t all arrive at once.
* You want to handle them one at a time, **as they come**.
* You’re working with Promises, and want to loop in a clean way.

For example, if you want to load messages from a chat server one by one, or download a large file in chunks, async iterators give you a way to write a `for` loop that works with delayed data.

### `Symbol.asyncIterator`

We can also use async iterators in custom classes.

Here’s an example that produces numbers with a delay:

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

We can now use `for await...of` just like before:

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

This allows you to create objects that can be iterated over asynchronously 

## Assignment syntax sugar

"Syntax sugar" means writing something in a shorter or easier way, without changing what it does. It’s just a nicer way to say the same thing. 

JavaScript has some built-in syntax sugar that let us write cleaner and shorter declarations. In this chapter, we’ll look at how to assign values based on a condition, update variables with math, pull values from arrays or objects, and copy or combine them with simpler syntax.

### The Ternary Operator

In JavaScript, you can assign a value based on a condition using the **ternary operator**, which is a short way of writing `if...else`.

Instead of doing:

```javascript
let message

if (isMorning) {
  message = "Good morning"
} else {
  message = "Hello"
}
```

You can write:

```javascript
const message = isMorning ? "Good morning" : "Hello"
```

This means:

* If `isMorning` is true, use `"Good morning"`
* Otherwise, use `"Hello"`

The general form is:

```javascript
condition ? valueIfTrue : valueIfFalse
```

You can use it inside other expressions too:

```javascript
console.log(isSunny ? "Go outside" : "Stay in")
```

Just make sure to use it for **simple** decisions. If the logic is complex, stick with `if...else`.

### Alternative Assignment Operators

JavaScript has **shortcut operators** for doing assignments combined with operations.

Let’s look at the normal way:

```javascript
let counter = 1
counter = counter + 1
```

This can be shortened to:

```javascript
let counter = 1
counter += 1 // same as counter = counter + 1
```

Here are the most common ones:

| Operator | Meaning             |
| -------- | ------------------- |
| `+=`     | add and assign      |
| `-=`     | subtract and assign |
| `*=`     | multiply and assign |
| `/=`     | divide and assign   |

Examples:

```javascript
let score = 10
score += 5  // now score is 15
score *= 2  // now score is 30
score -= 10 // now score is 20
```

These are useful when you want to update a variable using its own value.

### Destructuring

**Destructuring** lets you take values out of arrays or objects and store them into variables easily.

#### Arrays

Suppose you have:

```javascript
const colors = ["red", "green", "blue"]
```

Instead of doing:

```javascript
const first = colors[0]
const second = colors[1]
```

You can do:

```javascript
const [first, second] = colors
```

This assigns:

* `first` to `"red"`
* `second` to `"green"`

You can skip values too:

```javascript
const [,, third] = colors
console.log(third) // blue
```

#### Objects

You can extract values from objects too:

```javascript
const user = { name: "Alice", age: 30 }

const { name, age } = user
console.log(name) // Alice
console.log(age)  // 30
```

If the property has a different name than the variable you want, you can rename it:

```javascript
const { name: username } = user
console.log(username) // Alice
```

Destructuring makes your code cleaner when working with objects and arrays.

### Spread Syntax

The **spread syntax** uses `...` to unpack or copy values.

#### Arrays

You can copy or merge arrays:

```javascript
const a = [1, 2]
const b = [3, 4]

const both = [...a, ...b]
console.log(both) // [1, 2, 3, 4]
```

You can also clone an array:

```javascript
const original = [10, 20, 30]
const clone = [...original]
```

#### Objects

You can do the same with objects:

```javascript
const a = { x: 1 }
const b = { y: 2 }

const merged = { ...a, ...b }
console.log(merged) // { x: 1, y: 2 }
```

You can also override values:

```javascript
const user = { name: "Alice", age: 30 }
const updated = { ...user, age: 31 }

console.log(updated) // { name: "Alice", age: 31 }
```

This is very useful when updating objects without changing the original.
