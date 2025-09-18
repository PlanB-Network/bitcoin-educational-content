---
name: JavaScript and NodeJS Fundamentals
goal: Learn JavaScript programming fundamentals and NodeJS development to build practical applications and tools.
objectives:
  - Master basic JavaScript syntax, types, and control flow
  - Understand functions, objects, and classes in JavaScript
  - Learn error handling and debugging techniques
  - Get introduced to NodeJS and its ecosystem
---

# Start your development journey

Welcome to this course on JavaScript and NodeJS.

JavaScript is the most popular programming language in the world: it is the scripting language of modern browsers, so it's basically impossible to build a modern web application without writing *some* JavaScript; and with the NodeJS runtime it can be used outside browsers too, to create scripts and applications that run directly on your computer.

This course is designed for people who are completely new to programming, or who have used other languages before but want to understand how JavaScript works, especially in the context of NodeJS. 

By the end of the course, you should be able to write your own programs in JavaScript, use the NodeJS standard library, and install and use third-party packages to build useful tools.

+++
# Basic JavaScript
<partId>a617327c-e5a2-52ca-9380-c63f44623dd4</partId>

## Setup
<chapterId>ba05a290-1782-5268-87c9-62fd09590e05</chapterId>

A JavaScript program is just a collection of (one or more) text files, that contain commands to be executed by a JavaScript runtime.

The names of these text files usually end with a `.js` file extension, like `my_script.js`, `my_program.js` etc.

The commands they contain are written in the JavaScript programming language.

A JavaScript runtime is a special program that executes these files.

![](assets/en/1.webp)

### The NodeJS runtime

The most common JavaScript runtime is NodeJS.

Your IDE might already include it, or you might need to download it from the [official website](https://nodejs.org/en/download).

The download page will provide you with instructions for all three of the major OSs (Operating Systems): Windows, Linux and MacOS. It assumes you know how to open a terminal in your OS.

Since NodeJS is available for all three OSs, the programs that you write will be able to be executed on all of them (barring some edge cases).

This means you can, for example, write a simple videogame in JavaScript on your Windows PC and pass it to your friend to run it on his Mac.

![](assets/en/2.webp)

### First program (hello world)

Traditionally, when studying a programming language, the first program one writes consists in printing "hello world!" to the console.

Create a directory called `my_js_code/`, with inside a file called `main.js` (these names are arbitrary).

Open the directory with your code editor.

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
<chapterId>23050ab7-343b-5edf-9d37-e4e782e27ce0</chapterId>

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
<chapterId>cfdb04f6-21a8-5143-bbf9-7aaae04962f0</chapterId>

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

![](assets/en/3.webp)

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
<chapterId>7bf18183-5eae-53ed-83d2-b04982145d81</chapterId>

In this section, we’ll cover three more types that are very common in JavaScript programs:

**Arrays**: sequences of values
**undefined**: a special value that means "nothing was assigned"
**null**: another special value that means "intentionally empty"

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

`colors[0]` is `"red"`
`colors[1]` is `"green"`
`colors[2]` is `"blue"`

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
<chapterId>be985168-2636-5b0d-a48f-ac1bbfbff8a7</chapterId>

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
<chapterId>cc324715-09c2-5cf7-9e6f-47a6f16bc04d</chapterId>

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
<chapterId>26689f25-8212-5057-8c21-3a05eee0ac75</chapterId>

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

`class Dog` defines the Dog class.
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

![](assets/en/4.webp)

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

![](assets/en/5.webp)


This prints:

```
Toyota Corolla is ready to drive!
```

So to summarize

* `extends` means one class is based on another.
* `super()` is used to call the constructor of the class you're extending.
*The new class gets all the properties and methods of the original class.*
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
<partId>243f63ab-4f34-5c30-80cb-84ef46f6761d</partId>

## Error Handling
<chapterId>d0206bc5-d386-5e7f-9917-5803f392448c</chapterId>

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
*If an error occurs, JavaScript **jumps to the `catch` block**, skipping the rest of the `try` block.*
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
<chapterId>db12d9f6-5806-514c-998e-0ae24805104e</chapterId>

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
<chapterId>bb898425-dc2f-5e5c-864b-0cb7a4a9aea9</chapterId>

JavaScript treats different kinds of values in different ways.

Some values are **copied** when you assign them to a variable.

Others are **shared** when you assign them to a new variable, so if you change one, the other one changes too.

### Pass by value

When a value is passed **by value**, JavaScript makes a **copy** of it.

So if you change one, it doesn’t affect the other.

This happens with primitive types, like:

*numbers*
*strings*
*booleans* (`true` and `false`)
`null`
`*undefined*`

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
<chapterId>e0d277a8-c642-5af7-9e53-dee27c811967</chapterId>

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

*takes another function as input*
*and/or* returns a function as output

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
<chapterId>7842aada-f009-5518-b8e3-1104e166a035</chapterId>

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
<chapterId>01a397b8-c12a-5c39-82b3-6d9ebbb72a29</chapterId>

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
<chapterId>516e74c8-2a11-545a-a4d1-c2cabb91a273</chapterId>

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
<partId>72c30671-ca20-5617-92a5-d5ba7aa38c93</partId>

## Other collections
<chapterId>a9a70c6d-a343-5a46-a383-e288bc2700e3</chapterId>

JavaScript gives us some special collection types that go beyond regular arrays and objects. These include `Map` and `Set`.

They help you store and manage groups of values, but they work differently from what you've seen so far.

A `Map` is a collection of **key-value pairs**, just like an object. But it has some important differences:

* The keys can be **any value** not just strings.
*The order of the items is preserved.*
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

*You can't have the same value twice*
*The values are stored in the order you add them*

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
<chapterId>61d24e5e-b7e4-541a-8322-778f61f26a72</chapterId>

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

**We defined a class `Range`**
*Inside the class, we implemented `[Symbol.iterator]()`, so JavaScript knows how to iterate it*
*The `next()` method gives back each number one by one*
When we reach the `end`, it returns `{ done: true }`

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
<chapterId>f3fc76ca-b3ef-54eb-a06e-501007002054</chapterId>

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
<chapterId>30fddaca-729f-5c8d-bf86-8dfc7b3c9800</chapterId>

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

`resolve` is a function we call when everything is successful
`reject` is a function we call if something goes wrong

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
<chapterId>6e93d29f-c8bf-5fd1-a9c9-4e794ee6cbd0</chapterId>

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
<chapterId>438b037d-9931-56d7-9052-7b4470f3c75b</chapterId>

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

*The values don't all arrive at once.*
*You want to handle them one at a time,* **as they come**.
**You're working with Promises, and want to loop in a clean way.**

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
<chapterId>8b1ba7d8-ecfd-5470-b86e-73cb84ccc8b7</chapterId>

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
*Otherwise, use `"Hello"`*

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

`*first*` to `"red"`
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

# NodeJS
<partId>42fe4d49-dace-5135-bb9e-b9d75034fb2a</partId>

## How did we get to Node
<chapterId>0da1d60c-06c9-54e6-a181-ae7dabf6e3b8</chapterId>

In this chapter we will learn a little of historical context about JavaScript and NodeJS. 

Historical context is very important in software, because we're often using tools built by other people, and we're therefore influenced by decisions taken in the past by them. 

Understanding the reason for those decisions, and how the tools we use came to be the way they are, will help us feel a little less confused about what we're doing.

### Origins of JavaScript

JavaScript started as a simple language designed to make web pages interactive. 

In the 1990s, web browsers like Netscape Navigator added JavaScript so that developers could write code that runs directly in the browser.

The original idea was to have Java as the core language for making websites (with the so called "Java applets"), and JavaScript just for minor stuff. 

The core design was done by Brendan Eich, who at the time was an employee at Netscape, in less than 2 weeks. 

But most people preferred using JavaScript to Java, and also Java applets had some security issues at the time, so eventually Java was dropped as an option and JavaScript became the de facto standard for web development.

### The V8 engine

JavaScript is an interpreted language, as opposed to compiled languages like C. 

Code written in a compiled language gets turned into a binary, and the binary gets fed directly to the CPU of the computer.

![](assets/en/6.webp)

Interpred languages, on the other hand, tend to be more user-friendly, and are closer to how humans think ("high level") rather than to how machines work ("low level"); so they usually have a virtual machine built to run their code. 

A virtual machine is a special program that sits between the code you write and the CPU, and executes your code (because the CPU cannot understand it). 

This allows you to program without knowing too much about the underlying machine, but it also has a cost in terms of performance, because the computer is not running just your program; it's running a program (the virtual machine) that runs your program.

As web applications became more and more complex, there was demand to improve the performance of JavaScript. The V8 engine is the interpreter that powers JavaScript in Google Chrome. It was developed at Google and released in 2008. 

While the older JavaScript engines were mostly traditional virtual machines, the V8 engine is a JIT (just-in-time) compiler.

The JavaScript code gets fed to the V8 engine, and the engine tries to compile parts of it as native binaries on the fly. This allows you to have the experience of a high level language, with performance that it's a little closer to low level languages. This has made JavaScript the fastest high level language in the world, bit of a "best of both worlds" thing.

### The NodeJS runtime

While being easy to use and quite fast to execute, after the release of the V8 JavaScript kept having a huge limitation: it could only run inside a browser. 

Why is that a problem? 

Well, since browsers execute code fetched from millions of different sources on the internet, they can easily incur into malware, so they're "sandboxed" from the rest of the operating system. 

![](assets/en/7.webp)

JavaScript could not access the file system and other local resources on your computer (at least not easily like other languages could), so that was a significant limitation on what kind of applications you could build with it.

In 2009, Ryan Dahl published NodeJS, which is a runtime that allows you to use the V8 engine outside the browser, directly on the native operating system of your computer. It also adds many features that are useful for writing server-side and command-line programs. For example, you can use NodeJS to create a web server, read and write files, or build tools that automate tasks. 

![](assets/en/8.webp)

In this course so far, we've explored the JavaScript features that are present in both the browser and in NodeJS. Those features allowed us to define data and manipulate it in abstract ways. In the next few lessons, we'll explore the features that are specific to NodeJS and allow us to interact with the operating system.

## Command line arguments
<chapterId>960d20f3-c424-5d51-a041-ef17d2e94b6d</chapterId>

NodeJS allows us, among other things, to build CLIs (Command Line Interfaces). 

For that we need a way to receive command line arguments, which in Node is done using the built-in `process` object.

### `process`

NodeJS provides a special object called `process` that represents the current running program.

You can use it to inspect the environment, the current working directory, and even exit the program when needed.

For example:

```javascript
console.log(process.platform)
```

This prints the operating system platform, like `win32`, `linux`, or `darwin` (Mac).

### `process.argv`

When you run a NodeJS program from the terminal, you can pass extra words (arguments) after the script name. These are stored in `process.argv`.

For example, if you run this command:

```
node my_script.js alpha beta
```

You can print the arguments like this:

```javascript
console.log(process.argv)
```

The output might look like this:

```
[ '/path/to/node', '/path/to/my_script.js', 'alpha', 'beta' ]
```

The first two items are always the Node path and your script path. Any additional words you passed to the script come after that. 

The `process.argv` array can be cut as any other array using the `.slice()` method, so to get just the arguments that were passed you can do 

```javascript
const args = process.argv.slice(2)

console.log(args)
```

Having access to the arguments that the user is passing is fundamental to develop command-line applications.

## Modules
<chapterId>4e1651a5-65fd-50bc-b22a-40313d5659ca</chapterId>

JavaScript runtimes like NodeJS usually treat each JavaScript file as a separate module.

Think of a module as a box. The box has its own private space, so the variables and functions you declared in it don’t interfere with the code in other boxes. Basically, each module has its own scope.

A module can export some of its content, making it available to other modules, and it can import the content that other modules have exported. JavaScript allows you to export and import content between modules, to connect different files.

A JavaScript program is often composed of multiple modules, that are connected with each other.

Why use modules? By splitting your code into modules, you can organize your program into smaller, clearer, and reusable parts. Each module can focus on just one type of task, like handling math calculations, working with files, or formatting text.

### CommonJS modules

In NodeJS, the most common system to manage modules is called **CommonJS**.

In this system, you can share (export) code from a module using `module.exports` and load (import) it in another file using `require()`.

To make something available outside a module, you assign it to `module.exports`:

```javascript
const greeting = "Hello!"

module.exports = greeting
```

Here, the string `"Hello!"` is what this module exports.

To use the exported code from another file, you use the `require()` function with the path to that file:

```javascript
const greeting = require("./greeting.js")

console.log(greeting)
```

This prints:

```
Hello!
```

You can export multiple things by bundling them together in an anonymous object, like

```javascript
const greeting1 = "hello"

const greeting2 = "hi"

module.exports = {
    greeting1, greeting2
}
```

CommonJS was the module system that was initially adopted by NodeJS. Later on ES modules were also added.

### ES Modules

NodeJS also supports another type of module called **ES Modules**, which are popular in web development. They use the keywords `export` and `import`.

ES modules were developed for the browser and only later added to Node. If you want to use them, you might have to use `.mjs` as a file extension instead of `.js`, depending on which Node version you're using.

In one file callled `greeting.mjs` we write

```javascript
export const greeting = "Hello!"
```
As you can see, we're exporting the constant directly where it gets defined

In another file called `index.mjs`, we import it:

```javascript
import { greeting } from "./greeting.mjs"

console.log(greeting)
```

You can export different declarations in different parts of the file, like

```javascript
export const num = 10

export function double (x) {
  return x*2
}
```

### The NodeJS standard library

NodeJS also includes many built-in modules. These are ready-made modules provided by NodeJS that help with common tasks like reading files, working with the operating system, or connecting to the network.

For example, the `os` module gives you information about your operating system:

```javascript
const os = require("os")

console.log(os.platform()) 
```

You don’t have to install these built-in modules, they come with NodeJS. They form the "standard library" of the runtime, and are used by most Node applications to do stuff like reading files or communicating via the internet. 

The next chapters will show you some useful examples of their usage.

## The `fs` module
<chapterId>911e953a-35ae-5ee7-bd74-372501c32e81</chapterId>

The `fs` module (short for **file system**) is part of the NodeJS standard library. It allows you to work with files and directories on your computer: you can read files, write files, delete them, rename them, and more.

To use it, you first need to import it at the top of your file:

```javascript
const fs = require("fs")
```

### Sync API

The simplest way to use `fs` is with its **sync** methods.

These methods block the program until they finish (so the next line of code doesn’t run until the operation is complete).

Here’s an example of reading a file synchronously:

```javascript
const fs = require("fs")

const data = fs.readFileSync("example.txt", "utf8")

console.log(data)
```

If there’s a file called `example.txt` in the same directory as your script, this will print its contents.

You can also write to a file synchronously:

```javascript
const fs = require("fs")

fs.writeFileSync("output.txt", "Hello from Node!")

console.log("File written!")
```

This creates (or overwrites) a file called `output.txt` with the text.

Here are some common operations you can do with this API:

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

The Sync API is simple and good for small scripts, but because it blocks the program until it’s done, it can slow things down if you’re working with big files or a server.

### Callback async API

The **callback API** is non-blocking: it lets NodeJS keep doing other things while the file operation happens.

Instead of returning the result directly, it takes a function (a **callback**) which gets called when the operation is done.

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

Here’s what happens:

`fs.readFile` starts reading `example.txt`.
*NodeJS does not wait, it moves on to execute other code you might have written.*
*When the file is done reading, the callback runs:*

  * If there was an error, `err` contains the error.
  * Otherwise, `data` contains the contents.

Here's how you write to a file:

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

Same idea: the program doesn’t stop while writing the file.

Some examples of things you can do with this API:

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

The callback API is better for servers and big tasks because it doesn’t block the program, but nested callbacks can get messy if you chain many operations. That's why a promise-based async API was added.

### Promise async API

The Promise-based API is modern and works great with `.then()` and `async/await`. It’s available as `fs.promises`.

You need to import the `promises` property:

```javascript
const fs = require("fs").promises
```

Using `.then()`:

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

Or even better, using `async/await`:

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

Writing to a file:

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

The usual list of examples for the API:

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

When you write code , you will often need to use code written by other people; for example, libraries to help you work with dates, colors, servers, or almost anything else.

Instead of downloading and copying files manually, you can use a **package manager**.

A package manager is a tool that:

*downloads packages*
*keeps track of which packages your project needs*
**makes sure everyone on your team has the same versions of the packages**

### What is NPM

In the NodeJS world, the most popular package manager is **NPM**, which stands for *Node Package Manager*.

You get NPM automatically when you install NodeJS.

You can check if you have NPM by running this in your terminal:

```
npm -v
```

This prints the version of NPM you have, like:

```
10.2.1
```

### Creating a package

In NodeJS, a **package** is just a directory with a `package.json` file in it.

Let’s create one step by step.

1. Make a new folder for your project:

   ```
   mkdir my_project
   cd my_project
   ```

2. Run this command:

   ```
   npm init
   ```

This starts an interactive setup, asking you questions like the name of your project, version, description, etc.

If you don’t want to answer everything and just accept the defaults, you can use:

```
npm init -y
```

After running it, you will see a new file in your folder called:

```
package.json
```

### `package.json`

The `package.json` file is just a JSON file that stores metadata about your project.

Here’s an example:

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

A few important fields:

* `name`: the name of your package
* `version`: the current version
* `main`: the entry point file (like `index.js`)
* `scripts`: commands you can run (like `npm start`)
* `dependencies`: lists all the packages your project depends on

### Installing a package

Let’s say you want to use a certain package called `picocolors` to add colors to your terminal output.

You can install it by running:

```
npm install picocolors
```

You can now use it in your project. Make a `index.js` file with 

```javascript
const pico = require('picocolors')

console.log(
  pico.green("This text is green!")
)
```

and try running it. The terminal should print a colored version of the text.

What did NPM do ?

*It downloaded the package and stored it in a subfolder called `node_modules/`*
* it added an entry under `dependencies` in your `package.json`
* it updated the `package-lock.json` file

What is `package-lock.json` ?

### `package-lock.json`

This file is automatically created by NPM.

You might wonder, if we already have `package.json`, why do we need another file?
Here is the reason:

* `package.json` just says which version **range** of a package your project needs.
  Example:

  ```json
  "dependencies": {
    "picocolors": "^1.1.0"
  }
  ```

  The `^1.1.0` means “any version that is compatible with 1.1.x”, so it’s flexible.

`package-lock.json` **freezes** the exact versions of every single package and their sub-dependencies, so that everyone who installs your project gets the exact same working setup.

Why is this important?

If you work on a team, or you deploy your project to a server, or you come back to it in the future, you want to make sure it still works the same way.
If the packages have been updated and you reinstall without a lock file, you might get a slightly different version that behaves differently.

By keeping the `package-lock.json` in your project, NPM will always install the exact versions listed there, ensuring that everyone has the same environment.

`package-lock.json` locks everything to a very specific version, to make the project more reproducible on other machines.

But if your package needs to be used by many people, you might instead choose not to commit it, so that NPM only finds the `package.json` file and it's allowed to install automatically the latest versions that are allowed in that file.

But these are things you should worry about later, once you start publishing your own code. For now, we introduced the basics of NPM just to allow you to find and use the libraries published by other developers in your projects.


## Networking in NodeJS
<chapterId>f2cabd8b-754b-5c97-8d6a-8412a9a184c7</chapterId>

NodeJS is often used as a language for backend: you can turn your script into a server, and also use it to make requests to other servers. 

In thi chapter we're gonna introduce some basic networking features that will allow you to do that.

### `fetch()`

If you want your program to download data from a website or an API, you need to make an **HTTP request**.

In modern versions of NodeJS, you can use the built-in `fetch()` function.

Here’s an example of making a GET request to an API:

```javascript
const response = await fetch("https://jsonplaceholder.typicode.com/posts/1")
const data = await response.text()

console.log(data)
```

When you run this, you’ll see something like:

```
{
  "userId": 1,
  "id": 1,
  "title": "...",
  "body": "..."
}
```

Here is what happens:

1. `fetch()` takes a URL and makes a request.
2. It returns a **Promise** that resolves to a `Response` object.
3. `response.text()` reads the response body as a string.

But the string you get back is actually JSON. What is that?

### JSON

When working with web APIs, the data is often sent and received as **JSON**, which stands for JavaScript Object Notation.

JSON is just a text format that looks a lot like JavaScript objects. For example:

```json
{
  "name": "Alice",
  "age": 30,
  "likes": ["apples", "bananas"]
}
```

The `JSON` object is a built-in utility in JavaScript that can be used to work with this data format.

You can convert a JavaScript object into a JSON string using `JSON.stringify()`:

```javascript
const user = { name: "Alice", age: 30 }

const jsonString = JSON.stringify(user)

console.log(jsonString)
```

This prints:

```
{"name":"Alice","age":30}
```

You can also convert JSON text back into a JavaScript object using `JSON.parse()`:

```javascript
const jsonText = '{"name":"Bob","age":25}'

const obj = JSON.parse(jsonText)

console.log(obj)
```

This prints:

```
{ name: 'Bob', age: 25 }
```

Be careful: `JSON.parse()` will throw an error if the string is not valid JSON.

```javascript
JSON.parse("not json") // ❌ Error!
```

So make sure the string is properly formatted.

### `http` server

NodeJS allows you to create a web server without installing anything else.

You can use the built-in `http` module to handle requests from clients and send responses back.

Here is a very basic example:

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

When you run this script and open `http://localhost:3000` in your browser, you will see:

```
Hello from NodeJS server!
```

This is what's happening in the code:

1. You imported the `http` server from the Node standard library.
2. `http.createServer()` creates a server. You passed to `http.createServer()` a callback `(req, res) => {...}` to get executed every time someone connects.
3. You assigned a status code of 200 (which indicates a successful operation) to the response. You can read about http status codes [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status) 
3. `res.end()` sends the response and ends the connection.
4. `server.listen(3000)` starts the server on port 3000.

You can also check `req.url` and `req.method` in the request to handle different paths or request types.

Example with routing:

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

These are very basic examples. For building more advanced servers, most devs would probably download a ready-made backend library like [express](https://www.npmjs.com/package/express).

## Processing data: buffers, events, streams
<chapterId>8c9623f0-a604-51a4-8fe4-871c849d3e3b</chapterId>

In this chapter we'll introduce primarily three classes of objects:

- `Buffer`, which represents small chunks of binary data
- `EventEmitter`, which can be used to track somestep by asynchronous process by emitting signals called "events"
- `Stream`, which allows us to process big portion of data one `Buffer` at the time, and which tracks the process by emitting events

These are extremely common in professional NodeJS code, so even if you might not use them in your first projects, it's good to get a basic understanding for when you'll need to interact with them. of them

### Buffers

In NodeJS, a **buffer** is a type of object used to work with binary data.

You can think of a buffer as a fixed-size container for raw bytes.

Here’s how to create a buffer from a string:

```javascript
const buf = Buffer.from("hello")
console.log(buf)
```

This prints something like:

```
<Buffer 68 65 6c 6c 6f>
```

Those numbers (`68`, `65`, `6c`, etc.) are hexadecimal representations of the letters in `"hello"`.

You can convert it back to a string like this:

```javascript
console.log(buf.toString())
```

This prints:

```
hello
```

You can also create a buffer of a certain size filled with zeros:

```javascript
const buf = Buffer.alloc(10)
console.log(buf)
```

This prints something like:

```
<Buffer 00 00 00 00 00 00 00 00 00 00>
```

You can write into the buffer:

```javascript
buf.write("abc")
console.log(buf)
```

And you can access individual bytes:

```javascript
console.log(buf[0]) // prints the ASCII number for 'a', which is 97
```

Buffers are especially useful when you need to manipulate data at a very low level.

### Events

In JavaScript, an **event** is something that happens in your program that you can react to.

For example:

*a file finishes loading*
*a timer goes off*
*a user clicks a button*
*a network request returns data*

An **event** is just a signal that something happened, and you can write code to listen for those events and react to them.

In NodeJS, many objects can emit events. These objects are called **EventEmitters**.

Here’s an example:

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

This prints:

```
Hello! An event happened.
```

Here’s what:

1. We create an `EventEmitter` object.
2. We tell it to run a callback whenever the `"greet"` event happens, using `.on("greet")`.
3. Later, we trigger the `"greet"` event using `.emit()`.
4. Our callback gets executed

You can pass data along with the event:

```javascript
emitter.on("greet", 
  (name) => console.log(`Hello, ${name}!`)
)

emitter.emit("greet", "Alice") // first argument is the type of event, second argument is the data we pass with this event
```

This prints:

```
Hello, Alice!
```

You can register listeners for other events too:

```javascript
emitter.on("goodbye", () => {
  console.log("Goodbye!")
})

emitter.emit("goodbye")
```

You can attach as many listeners as you like to a type of event, and you can fire many different types of event from the same emitter.

Many objects in NodeJS emit events to tell the rest of the program that something is happening.


### What are streams?

Streams combine buffers and events to help us process data.

When we work with files, data from the network, or even long text, we don’t always need (or want) to load everything into memory all at once. That could be slow, or even crash the program if the data is too big.

Instead, we can process the data **little by little**, as it arrives or is read, kind of like drinking water through a straw instead of trying to drink the whole glass at once. This is called a **stream**.

In NodeJS, a stream is an object that lets you read data from a source or write data to a destination **one piece at a time**.

NodeJS has four main types of streams:

* **Readable**: streams you can read data from (like reading a file)
**Writable**: streams you can write data to (like writing to a file)
**Duplex**: streams that are both readable and writable
**Transform**: like duplex streams, but they can change (transform) the data as it flows

### Readable streams

Let's say you have a `bigfile.txt` to process. You can create a readable stream with the `fs` module to read the file piece by piece.

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

What happens here?

1. `fs.createReadStream()` creates a readable stream.
2. Whenever a piece of the file is ready, the stream emits a `data` event and gives us a "chunk" of data (a `Buffer`). We print the chunk.
3. When the whole file has been read, the `end` event is triggered.
4. If there’s an error (like the file doesn’t exist), the `error` event is triggered.

This way, you can read giant files without loading them all into memory at once.

If we want the data to arrive in a human-readable form (instead of binary), we can specify the encoding of the stream:

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

The code will now print the file in human-readable form.

### Writable streams

A writable stream lets you send data somewhere, chunk by chunk.

Here’s an example of writing to a `target.txt` file using a stream:

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

Here’s what happens:

1. `fs.createWriteStream()` creates a writable stream.
2. We write some text to it using `.write()`.
3. When we’re done, we call `.end()` to close the stream.
4. When all the data has been written, the `finish` event is emitted.
5. If something goes wrong, the `error` event is triggered.

Just like readable streams, writable streams are good for big data because they don’t need to keep everything in memory at once.

### Piping streams

One of the coolest things about streams is that you can **pipe** them together: connect a readable stream directly to a writable stream.

```javascript
const fs = require("fs")

const readable = fs.createReadStream("bigfile.txt")
const writable = fs.createWriteStream("target.txt")

readable.pipe(writable)
```

Here:

*The readable stream reads from `bigfile.txt`.*
*The writable stream writes to `copy.txt`.*
* `.pipe()` sends the data directly from the readable to the writable stream.

### Duplex streams

A duplex stream is both readable and writable. One example is a network socket: you can send data to it and receive data from it.

Here’s a very simple example using the `net` module:

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

In this example:

*The `socket` object is a duplex stream.*
*You can `write()` to it and also listen for `data` events from it.*

### Transform streams

A transform stream is a duplex stream that also modifies the data that passes through it.

For example, you can use the built-in `zlib` module to compress or decompress data.

Here’s how to compress a file using a transform stream:

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

And to decompress it back:

```javascript
const readable = fs.createReadStream("bigfile.txt.gz")
const unzip = zlib.createGunzip()
const writable = fs.createWriteStream("bigfile.txt")

readable.pipe(unzip).pipe(writable)

writable.on("finish", () => {
  console.log("File decompressed.")
})
```

Transform streams are very useful for tasks like compression, encryption, or changing file formats while streaming.

### Backpressure

Sometimes a writable stream is slow at handling data. If we keep pushing data to a writable faster than it can handle, we might run into problems. This is called **backpressure**.

If you call the `.write()` method on a writable stream, it returns a boolean that informs you if the stream needs a pause; you might have to check its return value, like this:

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

This was an illustrative example of manually piping data from a Readable to a Writable, and managing backpressure manually.

Usually we would pipe data using the  `.pipe()` method, which handles backpressure automatically.

So you only need to worry about backpressure when for some reason you're manually calling `.write()`.

## Final note
<chapterId>139e2ab8-df67-525a-85f0-5a2fa5e478f2</chapterId>

So, that's it, if you followed along with the lessons, you should now be able to write some simple programs in NodeJS.

I'd suggest doing exactly that: after learning the basics, building a few personal projects is the best way to practice and become a better programmer. 

It doesn't really matter what you build, what matters is that you challenge yourself to solve problems with code. 

Modern programming languages are incredibly powerful, and NodeJS is probably the best toolbox to experiment with in this phase of your journey.

Good luck!

# Final section

<partId>322624d8-6fbc-11f0-a67a-5b145f10afc1</partId>

## Reviews & Ratings

<chapterId>3e93ac86-6fbc-11f0-8bae-9b2ed7914843</chapterId>
<isCourseReview>true</isCourseReview>

## Conclusion

<chapterId>49b3b9b2-6fbc-11f0-9870-5f5adcd3a0eb</chapterId>

<isCourseConclusion>true</isCourseConclusion>