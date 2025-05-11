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
