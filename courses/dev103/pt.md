---
name: Fundamentos de JavaScript e NodeJS
goal: Aprenda os fundamentos da programação JavaScript e o desenvolvimento NodeJS para criar aplicações e ferramentas práticas.
objectives: 

  - Dominar a sintaxe, os tipos e o fluxo de controlo básicos do JavaScript
  - Compreender funções, objectos e classes em JavaScript
  - Aprender técnicas de tratamento de erros e de depuração
  - Introdução ao NodeJS e ao seu ecossistema

---

# Iniciar o seu percurso de desenvolvimento


Bem-vindo a este curso sobre JavaScript e NodeJS.


O JavaScript é a linguagem de programação mais popular do mundo: é a linguagem de script dos browsers modernos, pelo que é basicamente impossível construir uma aplicação Web moderna sem escrever *algum* JavaScript; e com o tempo de execução do NodeJS também pode ser utilizado fora dos browsers, para criar scripts e aplicações que correm diretamente no seu computador.


Este curso foi concebido para pessoas que são completamente novas na programação, ou que já usaram outras linguagens antes, mas querem entender como o JavaScript funciona, especialmente no contexto do NodeJS.


No final do curso, deverá ser capaz de escrever os seus próprios programas em JavaScript, utilizar a biblioteca padrão NodeJS e instalar e utilizar pacotes de terceiros para criar ferramentas úteis.


+++
# JavaScript básico

<partId>a617327c-e5a2-52ca-9380-c63f44623dd4</partId>


## Configuração

<chapterId>ba05a290-1782-5268-87c9-62fd09590e05</chapterId>




Um programa JavaScript é apenas uma coleção de (um ou mais) ficheiros de texto, que contêm comandos a serem executados por um tempo de execução JavaScript.


Os nomes desses arquivos de texto geralmente terminam com uma extensão de arquivo `.js`, como `meu_script.js`, `meu_programa.js` etc.


Os comandos que contêm são escritos na linguagem de programação JavaScript.


Um tempo de execução do JavaScript é um programa especial que executa estes ficheiros.


![](assets/en/1.webp)


### O runtime do NodeJS


O tempo de execução JavaScript mais comum é o NodeJS.


O seu IDE pode já incluí-lo, ou poderá precisar de baixá-lo no [site oficial](https://nodejs.org/en/download).


A página de transferência fornecerá instruções para os três principais SOs (Sistemas Operativos): Windows, Linux e MacOS. Pressupõe que sabe como abrir um terminal no seu sistema operativo.


Uma vez que o NodeJS está disponível para os três sistemas operativos, os programas que escrever poderão ser executados em todos eles (exceto em alguns casos extremos).


Isto significa que pode, por exemplo, escrever um jogo de vídeo simples em JavaScript no seu PC Windows e passá-lo ao seu amigo para o executar no seu Mac.


![](assets/en/2.webp)














### Primeiro programa (hello world)


Tradicionalmente, quando se estuda uma linguagem de programação, o primeiro programa que se escreve consiste em imprimir "hello world!" na consola.


Crie um diretório chamado `my_js_code/`, com dentro um arquivo chamado `main.js` (esses nomes são arbitrários).


Abra o diretório com o seu editor de código.


Escreva este código no seu ficheiro:


```javascript
console.log("hello world!")
```


Abra um terminal e execute este comando para executar o programa:


```
node main.js
```


O resultado deve ser


```
hello world!
```


### O que aconteceu


Em JavaScript, tudo é um "objeto".


`console` é um objeto, que é usado para depurar o programa.


`console.log` é o método mais utilizado do `console`. Ele apenas imprime qualquer argumento que você passar para ele.


Você passa argumentos para `console.log` usando os colchetes `()`.


Assim, por exemplo, se quisesse imprimir o número `1000`, bastava escrever


```javascript
console.log(1000)
```


Em seguida, execute-o executando


```
node main.js
```


no seu terminal (a partir de agora, este curso vai assumir que sabe que é assim que executa um programa).


Isto deve imprimir


```
1000
```


Pode passar várias coisas, como


```javascript
console.log(16, 8, 1993)
```


Isto irá imprimir


```
16 8 1993
```


## Variáveis e comentários

<chapterId>23050ab7-343b-5edf-9d37-e4e782e27ce0</chapterId>


Os programas executam normalmente operações sobre dados.


As variáveis são como caixas nomeadas que utilizamos para armazenar dados. Permitem-nos associar um dado a um nome específico, de modo a podermos recuperá-lo mais tarde utilizando esse nome.


### declarações `let


Para declarar uma variável em JavaScript, podemos usar a palavra-chave `let`.


Depois de escrever `let`, escrevemos o nome que queremos dar à variável, depois um sinal `=` e, em seguida, o valor que queremos armazenar.


Por exemplo:


```javascript
let age = 25

console.log(age)
```


O nome de uma variável (tecnicamente designado por "identificador") pode normalmente conter letras, sublinhados (`_`), o sinal de dólar (`$`) e números, embora o primeiro carácter não possa ser um número.


No código acima, declaramos uma variável chamada `idade` e armazenamos o valor `25` nela.


Depois, imprimimos o valor usando `console.log(age)`.


Se você executar este código com `node main.js`, a saída será:


```
25
```


Os identificadores são sensíveis às maiúsculas e minúsculas, o que significa que as maiúsculas e as minúsculas contam como diferenças nos identificadores, por exemplo


```javascript
let age = 25

let Age = 20

console.log(age)
```


imprimirá 25, porque estas são consideradas duas variáveis completamente separadas!


Também é possível armazenar cadeias de caracteres (texto) numa variável:


```javascript
let message = "hello again"

console.log(message)
```


Isto irá imprimir:


```
hello again
```


Assim como antes, usamos `console.log()` para imprimir o valor armazenado na variável.


Agora vamos fazer os dois juntos:


```javascript
let age = 25

let message = "hello again"

console.log(age)

console.log(message)
```


A execução desta ação imprimirá:


```
25
hello again
```

### Reafectação


Variáveis declaradas com `let` podem ser alteradas após serem criadas.


A isto chama-se reafectação.


```javascript
let score = 10

console.log(score)

score = 15

console.log(score)
```


Primeiro, atribuímos `10` a `score` e depois imprimimo-lo.


Em seguida, alteramos o valor de `score` para `15` e imprimimos novamente.


O resultado será:


```
10
15
```


Isto é muito útil quando o valor muda ao longo do tempo, como num jogo em que a pontuação aumenta.


Vamos acrescentar mais uma variável à mistura:


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


Isto irá imprimir:


```
10
Alice
20
Bob
```


Como pode ver, tanto `score` como `player` foram alterados.


### declarações `const


Na maioria das vezes, porém, não queremos que uma variável mude depois de ser criada. Para isso, usamos `const`.


`const` é a abreviação de "constante". Uma vez atribuído um valor a uma variável `const`, não é possível alterá-lo.


```javascript
const pi = 3.14
console.log(pi)
```


Isto imprime:


```
3.14
```


Mas se tentar fazer isso:


```javascript
const pi = 3.14
console.log(pi)

pi = 99 // this line will cause an error
console.log(pi)
```


O JavaScript apresentará um erro do tipo:


```
TypeError: Assignment to constant variable.
```


Isso ocorre porque `pi` foi declarada utilizando `const`, e não é possível alterar seu valor depois disso. Você está comunicando ao interpretador JavaScript que você não quer que essa variável mude.


Isto é útil porque reduz as hipóteses de o alterar por engano. Quando os programas se tornam muito grandes, com milhares de linhas de código, é impossível acompanhar tudo o que está a acontecer ao mesmo tempo (essa é a principal razão pela qual usamos computadores, para executar processos complexos que não podemos computar com os nossos cérebros), por isso torna-se útil ter restrições como esta, que tornam o programa mais determinístico.


É considerada a melhor prática declarar sempre os nossos valores como `const`, a não ser que tenhamos a certeza que os queremos modificar mais tarde.


### Comentários em JavaScript


Por vezes, queremos escrever notas no nosso código que não são executadas. São os chamados comentários.


Os comentários são ignorados pelo programa quando este é executado, mas são úteis para explicar coisas a nós próprios ou a outras pessoas.


Para escrever um comentário de linha única, use `//`


```javascript
// This is a comment
const x = 10 // This is also a comment
console.log(x)
```


Isto continua a ser impresso:


```
10
```


Os comentários estão lá apenas para os humanos lerem.


Também é possível escrever comentários de várias linhas utilizando `/*` e `*/`


```javascript
/*
This is a multi-line comment.
It can span several lines.
*/
const y = 20
console.log(y)
```


Isto irá imprimir


```
20
```


E o comentário será ignorado.


Pode utilizar comentários para adicionar pequenas anotações ao seu código, para que se possa lembrar do que faz e porque é que está escrito de uma determinada forma. Também pode ajudar outros programadores a compreendê-lo.


## Tipos básicos: números, cadeias de caracteres, booleanos

<chapterId>cfdb04f6-21a8-5143-bbf9-7aaae04962f0</chapterId>


Em JavaScript, um "tipo" diz-lhe que tipo de dados é um valor.


O Javascript tem alguns tipos básicos e, nesta secção, vamos explorar alguns deles.


### Números e operações aritméticas


O primeiro tipo que vamos introduzir é o `número`.


Números em JavaScript podem ser inteiros (como `5`) ou decimais (como `3.14`).


É possível fazer aritmética com eles: adição, subtração, multiplicação e divisão.


Eis um exemplo básico:


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


Isto irá imprimir:


```
15
5
50
2
```


Pode também utilizar parênteses `()` para controlar a ordem das operações:


```javascript
const result = (2 + 3) * 4
console.log(result)
```


Isto imprime:


```
20
```


Sem os parênteses, seria `2 + 3 * 4`, que é:


```javascript
const result = 2 + 3 * 4
console.log(result)
```


Isso seria impresso:


```
14
```


Porque na matemática normal, a multiplicação acontece antes da adição.


### Cordas e interpolação


O segundo tipo de JavaScript que vamos introduzir é o `string`.


Strings são pedaços de texto. Pode utilizar aspas simples `'...'` ou aspas duplas `"..."` para as criar.


```javascript
const greeting = "hello"
const name = 'Bob'
console.log(greeting)
console.log(name)
```


Isto imprime:


```
hello
Bob
```


Para combinar cadeias de caracteres, pode utilizar o operador `+`:


```javascript
const greeting = "hello"
const space = " "
const name = "Bob"

const fullGreeting = greeting + space + name
console.log(fullGreeting)
```


Isto irá imprimir:


```
hello Bob
```


Mas existe uma maneira mais agradável de combinar strings chamada **interpolação de strings**. Utiliza-se backticks para declarar a string `` `...` `` e escrever variáveis utilizando `${...}` dentro da string:


```javascript
const greeting = "hello"
const name = "Bob"

const fullGreeting = `${greeting} ${name}`
console.log(fullGreeting)
```


Isto também imprime:


```
hello Bob
```


Pode incluir qualquer expressão dentro de `${...}`:


```javascript
const age = 30
console.log(`Next year, I will be ${age + 1} years old.`)
```


Isto imprime:


```
Next year, I will be 31 years old.
```


A interpolação é muito comum no JavaScript moderno.


### Booleanos, comparação e operações lógicas


O terceiro tipo que vamos introduzir é o `boolean`. O seu nome vem do matemático George Boole, que inventou a lógica booleana.


Os booleanos são simples: apenas dois valores possíveis, `verdadeiro` e `falso`.


Pode armazená-los em variáveis:


```javascript
const theSkyIsBlue = true
const thisCourseIsBad = false

console.log(theSkyIsBlue)
console.log(thisCourseIsBad)
```


Isto imprime:


```
true
false
```


É possível combinar booleanos utilizando operadores lógicos:



- `&&` significa "e", e retornará `verdadeiro` somente se **ambos** os valores forem `verdadeiros`, caso contrário retornará `falso`
- `||` significa "ou", e devolverá `true` se **pelo menos um** dos valores for `true`, caso contrário (se ambos forem falsos) devolverá `false`
- `!` significa "não", é aplicado antes de um booleano e inverte-o: se o booleano for `verdadeiro`, devolverá `falso`, e vice-versa.


![](assets/en/3.webp)


Exemplos:


```javascript
const isSunny = true
const isWarm = true

console.log(isSunny && isWarm)  // true
console.log(isSunny || isWarm)  // true
console.log(!isSunny)           // false
```


É possível comparar valores em JavaScript utilizando operadores como `>`, `<`, `===` e `!==`. O resultado dessas comparações é sempre um booleano.


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


O Javascript também tem `>=` para significar "maior ou igual" e `<=` para significar "menor ou igual".


Os booleanos, os operadores de comparação e os operadores lógicos são frequentemente combinados em programas para declarar condições complexas, como garantir que "o correio eletrónico chegou E contém a imagem de que preciso OU o comprimento do correio eletrónico é superior a 10000 caracteres". Verá mais tarde que estes são blocos de construção essenciais para construir a lógica do programa.


## Matrizes, nulo, indefinido

<chapterId>7bf18183-5eae-53ed-83d2-b04982145d81</chapterId>


Nesta secção, abordaremos mais três tipos que são muito comuns em programas JavaScript:



- Arrays**: sequências de valores
- undefined**: um valor especial que significa "nada foi atribuído"
- null**: outro valor especial que significa "intencionalmente vazio"


### Matrizes e acesso a índices


Uma **matriz** é um tipo que pode conter vários valores numa lista.


Cria-se uma matriz utilizando parênteses rectos `[]` e separando os itens por vírgulas.


Eis um exemplo básico:


```javascript
const numbers = [10, 2, 88]
console.log(numbers)
```


Isto imprime:


```
[ 10, 2, 88 ]
```


É possível armazenar qualquer coisa numa matriz, não apenas números:


```javascript
const things = ["apple", 42, true]
console.log(things)
```


Isto imprime:


```
[ 'apple', 42, true ]
```


Para aceder a um item específico na matriz, utilizamos um **índice**. O índice é a posição do item, a partir de **0**.


Portanto, neste conjunto:


```javascript
const colors = ["red", "green", "blue"]
```



- `colors[0]` é `"red"`
- `cores[1]` é `"Green"`
- `cores[2]` é `"azul"`


Vamos tentar:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[0])
console.log(colors[1])
console.log(colors[2])
```


Isto irá imprimir:


```
red
green
blue
```


É possível atribuir um valor a um índice específico de uma matriz


```javascript
const colors = ["red", "green", "blue"]

colors[1] = "yellow"

console.log(colors)
```


Isto irá imprimir:


```
[ 'red', 'yellow', 'blue' ]
```


É possível utilizar qualquer número natural como índice, mesmo que esteja armazenado numa variável


```javascript

const i = 1
const colors = ["red", "green", "blue"]
console.log(colors[i])
```


Isto irá imprimir:


```
green
```


Mas se tentar aceder a um índice que não existe, obterá `undefined`:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[3])
```


Isto imprime:


```
undefined
```


O que é que é isso?


### `undefined`


O valor especial `undefined` significa "não foi atribuído qualquer valor".


Se criar uma variável mas não lhe atribuir um valor, esta será `undefined`:


```javascript
const name
console.log(name)
```


Isto imprime:


```
undefined
```


Como não atribuímos nada a `name`, o JavaScript define-o como `undefined` por defeito.


Como visto anteriormente, também pode obter `undefined` quando acede a um índice de array que não existe:


```javascript
const fruits = ["banana", "apple"]
console.log(fruits[2]) // There is no index 2
```


Isto imprime:


```
undefined
```


### `null` e como tratá-lo


`null` é também um valor especial. Significa "não há nada aqui, e eu fiz isso de propósito"


Ao contrário de `undefined`, que é automático, `null` é algo que você mesmo define.


Por exemplo:


```javascript
const currentUser = null
console.log(currentUser)
```


Isto imprime:


```
null
```


Porquê utilizar `null`? Talvez esteja à espera de um valor mais tarde, mas este ainda não está pronto:


```javascript
let winner = null

// Later in the program:
winner = "Alice"

console.log(winner)
```


Isto imprime:


```
Alice
```


Assim, `null` é útil quando se quer dizer, por exemplo, "Deverá haver algo aqui mais tarde, mas neste momento está vazio"


## Blocos e fluxo de controlo

<chapterId>be985168-2636-5b0d-a48f-ac1bbfbff8a7</chapterId>


Até agora, escrevemos principalmente linhas de código que são executadas uma após a outra.


Mas quando codificamos, podemos controlar a ordem de execução do código.


A isto chama-se **fluxo de controlo**.


Comecemos por compreender os blocos e o âmbito.


### O âmbito global


Cada variável que declaramos existe num **âmbito**, ou seja, a região do código onde a variável é conhecida.


Se declarar uma variável fora de qualquer bloco, ela existe no **âmbito global**.


```javascript
const color = "blue"
console.log(color)
```


Esta variável `color` está no âmbito global, pelo que pode ser acedida a partir de qualquer ponto do ficheiro.


Se adicionar mais linhas:


```javascript
const color = "blue"
console.log(color)

const size = "large"
console.log(color)
console.log(size)
```


Tanto `color` como `size` são variáveis globais. Estão disponíveis em qualquer parte do ficheiro.


Mas o que acontece dentro de um bloco?


### Blocos e âmbito local


Um **bloco** é um pedaço de código rodeado por chavetas `{}`.


As variáveis declaradas com `let` ou `const` dentro de um bloco existem **apenas** dentro desse bloco.


```javascript
{
const message = "inside block"
console.log(message)
}
```


Isto imprime:


```
inside block
```


Mas se experimentares isto:


```javascript
{
const message = "inside block"
}
console.log(message) // Error!
```


O JavaScript apresentará um erro do tipo:


```
ReferenceError: message is not defined
```


Isso acontece porque `message` foi declarada dentro do bloco e não existe fora dele.


Isto significa que podemos utilizar blocos para isolar partes do nosso código e ter a certeza de que "o que acontece no bloco fica no bloco" (um pouco como em Las Vegas).


A organização do nosso código em blocos permite-nos também estruturar a execução do programa, com construções de fluxo de controlo como `if`


### se, senão


Algumas vezes queremos executar um código **somente se** algo for verdadeiro. É para isso que serve a instrução `if`.


```javascript
const myAge = 20

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Isto imprime:


```
Am I an adult?
Yes I am!
```


Como pode ver, o código compara `myAge` e `18`.

Neste caso, o operador `>=` retorna `verdadeiro`, portanto o bloco é executado.

Se a condição não for `verdadeira`, o bloco não é executado.


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Isto imprime:


```
Am I an adult?
```


Pode adicionar um bloco `else` para lidar com o caso oposto:


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
} else {
console.log("No, I am not.")
}
```


Isto imprime:


```
Am I an adult?
No, I am not.
```


Tanto o bloco `if` quanto o `else` continuam sendo blocos - portanto, as variáveis declaradas dentro deles não existem fora.


Se quisermos ter a certeza de que algo **não** é verdade, o que é que podemos fazer?


Bem, como discutido anteriormente, o JavaScript tem um operador "not", que inverte booleanos. Então podemos fazer


```javascript
const myAge = 17

const adult = myAge >= 18

console.log("Am I an adult?")

if (!adult) {
console.log("No, I am not.")
}
```

Isto continua a imprimir:


```
Am I an adult?
No, I am not.
```

Porque utilizámos o operador `!` para inverter a variável `adulto`.


`if (!adult) {...}` deve ser lido como "if not adult..."


Utilizando blocos, operadores lógicos e de comparação, podemos estruturar a execução do programa, definindo variáveis que devem ser "verdadeiras" (ou "falsas") para que algo aconteça.


### `while`, `break`, `continue`


Um loop `while` repete o código *enquanto* uma condição for verdadeira.


```javascript
let count = 0

while (count < 3) {
console.log("Count is", count)
count = count + 1
}
console.log("the loop is over!")
```


Isto imprime:


```
Count is 0
Count is 1
Count is 2
the loop is over!
```


Quando `count` se torna 3, o ciclo pára.


Você pode parar um loop antes do tempo usando `break`:


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


Isto imprime:


```
0
1
2
```


Porque quando o número se torna `3`, o bloco `if` é executado e pára o loop.


Você pode pular o resto de um loop usando `continue`:


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


Isto imprime:


```
1
2
4
5
```


Porque quando o número era `3`, `continue` fazia o programa saltar a linha que imprimia o número.


### `para ... de ...`


Se você tem um array, e quer fazer algo para cada item nele, você pode usar `for ... of ... {...}`.


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const fruit of fruits) {
console.log(fruit)
}
```


Isto imprime:


```
apple
banana
cherry
```

O bloco será executado uma vez para cada elemento da matriz.


`fruit` aqui é uma nova variável que recebe o valor de cada item do array, para operar sobre ele dentro do bloco.


### `para ... em ...`


É possível utilizar `for ... in` para percorrer as chaves (índices) de um array:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(index)
}
```


Isto imprime:


```
0
1
2
```


Também pode utilizar o índice para obter o valor:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(fruits[index])
}
```


Isto imprime o mesmo que `for ... of`:


```
apple
banana
cherry
```


Na prática, para arrays, deve preferir utilizar `for ... of`, uma vez que é mais simples e mais limpo.


### Laços limitados


Por vezes, queremos repetir um número específico de vezes ou, em geral, escrever um pedaço de código que repete um bloco enquanto mantém um registo de algo.

É para isso que serve um loop `for` limitado.

Um laço delimitado geralmente aceita três condições, separadas por um ponto e vírgula `;`, como em `(... ; ... ; ....)`.


```javascript
for (let i = 0; i < 3; i = i + 1) {
console.log(i)
}
```


Isto imprime:


```
0
1
2
```


Vamos explicar:



- `let i = 0`: declara uma variável a ser utilizada no bloco (neste caso é um contador que começa em 0)
- `i < 3`: declara uma condição que deve ser `verdadeira` para que o bloco seja executado (neste caso é "repita enquanto `i` for menor que 3")
- `i = i + 1`: declara algum código a ser executado após cada execução do bloco (neste caso "aumentar `i` em 1")


Como pode ver, o loop delimitado permite-nos declarar condições mais complexas para a execução repetida de um pedaço de código, mas na maioria das vezes não é necessário.


### Etiquetas de blocos


Se tiver de escrever um fluxo de controlo mais complexo, o JavaScript permite-lhe nomear um bloco utilizando um **label** que pode ser utilizado por `break` ou `continue` para especificar *onde* voltar.


Exemplo:


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


Isto imprime:


```
Inside outer block
Inside inner block
Done
```


Nós usamos `break outer` para sair do bloco `outer` completamente.


Também pode rotular os loops. Vejamos este exemplo:


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

Este foi um exemplo muito aborrecido, mas espero que tenha esclarecido a necessidade (ocasional) de etiquetas.


## Introdução de funções

<chapterId>cc324715-09c2-5cf7-9e6f-47a6f16bc04d</chapterId>


À medida que os seus programas crescem, é frequente querer **reutilizar** partes de código.


É para isso que servem as **funções**: permitem-lhe agrupar algum código, dar-lhe um nome e executá-lo sempre que quiser.


### Declaração de função


Para declarar uma função, podemos utilizar a palavra-chave `function`. Depois damos-lhe um nome, um par de parênteses `()` com os argumentos que recebe, e um bloco de código `{}` para ser executado. Vamos começar com uma função que não recebe argumentos:


```javascript
function sayHello () {console.log(`Hello!`) }
```


Este código **declara** a função, mas **não** a executa ainda.


### Chamadas de função


Para executar (ou "chamar") a função, escreve-se o seu nome seguido de parênteses:


```javascript
function sayHello () {console.log(`Hello!`) }
sayHello()
```


Isto imprime:


```
Hello!
```


Pode chamar a função as vezes que quiser:


```javascript
function sayHello() {
console.log("Hello!")
}

sayHello()
sayHello()
```


Isto imprime:


```
Hello!
Hello!
```


O código dentro da função só é executado quando é chamado.


### Argumentos de funções (entrada para funções)


Por vezes, queremos que uma função funcione com algum input. Pode fazê-lo adicionando **argumentos** dentro dos parênteses.


Por exemplo:


```javascript
function sayHelloTo (friend) {
console.log(`Hello ${friend}!`)
}
```


Agora esta função recebe **um argumento** chamado `amigo`.


Quando chama a função, pode passar um valor:


```javascript
sayHelloTo("Tommy")
```


Isto imprime:


```
Hello Tommy!
```


É possível chamar novamente a função com um nome diferente:


```javascript
sayHelloTo("Sam")
```


Isto imprime:


```
Hello Sam!
```


O valor passado substitui a variável `friend` dentro da função.


Também é possível utilizar mais do que um argumento:


```javascript
function greetTwoPeople(person1, person2) {
console.log(`Hello ${person1} and ${person2}!`)
}

greetTwoPeople("Lina", "Marco")
```


Isto imprime:


```
Hello Lina and Marco!
```


### `return` (saída de funções)


As funções também podem **retornar** valores. Isto significa que enviam um valor de volta para o local onde a função foi chamada.


Eis um exemplo simples:


```javascript
function getNumber() {
return 42
}

const result = getNumber()
console.log(result)
```


Isto imprime:


```
42
```


A função `getNumber()` retorna `42`, e nós armazenamos esse valor em `result` e depois imprimimos.


Também pode devolver algo que calculou:


```javascript
function add(a, b) {
return a + b
}

const result = add(2, 3)
console.log(result)
```


Isto imprime:


```
5
```


Quando um valor é `retornado`, a função pára. Qualquer coisa depois de `return` nesse bloco não acontece.


```javascript
function saySomething() {

return "hi"

console.log("this never runs")

}

const message = saySomething()
console.log(message)
```


Este só imprime:


```
hi
```


porque apenas `"hi"` é retornado. A linha `console.log("isto nunca é executado")` é ignorada.


Pode pensar nas funções como pequenos subprogramas. Cada função pode receber um input, trabalhar sobre ele e devolver-lhe um output.


O que acontece se tentarmos utilizar o valor de retorno de uma função, mas essa função não devolveu nada?


```javascript
function doesNothing () {}

const x = doesNothing()

console.log(x)
```

Isto irá imprimir `undefined`. O valor de retorno de uma função que não retornou nada é `undefined`.


## Objectos e classes

<chapterId>26689f25-8212-5057-8c21-3a05eee0ac75</chapterId>


O JavaScript é frequentemente designado como uma linguagem orientada para objectos.


Isto significa que o ajuda a organizar o seu código agrupando valores e funções em **objectos**.


### O que é um `objeto` ?


Um objeto pode conter dados e funções que operam sobre esses dados. Quando uma função é colocada num objeto, dizemos que é um `método`.


O primeiro objeto que vimos foi o objeto `console`. É um objeto que contém vários métodos para imprimir coisas na tela e depurar nossos programas.


Pode até imprimir-se a si próprio; pode fazer


```javascript
console.log(console)
```


e ele imprimirá uma lista dos métodos que ele contém. Por exemplo, na minha máquina, imprimiu


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


Como podes ver, tem muitos métodos que podes utilizar para depurar!


O Javascript oferece-nos uma forma diferente de criar novos objectos que podem fazer o que quisermos.


### Criar um objeto


A forma mais fácil de criar um objeto é agrupar dados e funções utilizando **entre parênteses rectos** `{}`.


Isto cria aquilo a que chamamos um **objeto anónimo**


```javascript
const cat = {
name: "Whiskers",
age: 3
}
```


Isso cria um objeto e o armazena em uma variável chamada `cat`.


O objeto tem duas **propriedades**:



- `name` com o valor `"Whiskers"`
- `idade` com o valor `3`


Vamos imprimir:


```javascript
console.log(cat)
```


Isto imprime:


```
{ name: 'Whiskers', age: 3 }
```


É possível obter as propriedades do objeto utilizando um ponto, como em `objectName.propertyName`:


```javascript
console.log(cat.name)  // prints "Whiskers"
console.log(cat.age)   // prints 3
```


Também é possível **alterar** um bem:


```javascript
cat.age = 4
console.log(cat.age)  // now it prints 4
```


Como pode ver, mesmo que um objeto seja definido como `const`, é possível modificar os dados que ele contém.


No caso de objectos, `const` apenas o impedirá de sobrepor o objeto inteiro:


```javascript
const cat = {
name: "Whiskers",
age: 3
}

cat.age = 5 // this works

cat = 5 // this throws an error, you're trying to reassign the whole object

```


Como já foi referido, os objectos também podem conter **funções** e quando uma função faz parte de um objeto, chamamos-lhe **método**.


Eis um exemplo:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log("Meow!")
}
}
```


Este objeto tem:



- Uma propriedade `name
- Um método `speak()`


Vamos chamar o método:


```javascript
cat.speak()
```


Imprime:


```
Meow!
```


Os métodos podem utilizar os dados que o objeto contém através da palavra-chave `this`.

`this` refere-se ao objeto atual. Neste exemplo, ele será usado para imprimir o nome do gato:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log(`${this.name} says meow!`)
}
}

cat.speak()
```


Isto imprime:


```
Whiskers says meow!
```


A palavra `this` significa "este objeto"... neste caso, o objeto `cat`.



Estes tipos de objectos são óptimos quando se pretende apenas algo rápido e simples. Mas se precisar de criar **muitos objectos** com a mesma estrutura, há uma forma melhor, e é aí que entram as **classes**.


### Classes e construtores


Uma **classe** é como um projeto. Diz ao JavaScript como criar um certo tipo de objeto.


Você define uma classe usando a palavra-chave `class`, seguida pelo nome da classe e por um bloco de chaves `{}`.


```javascript
class Dog {}
```


Por convenção, as aulas começam normalmente com uma letra maiúscula.


É possível criar um novo objeto de uma classe utilizando `new`:


```javascript
const hachiko = new Dog()
```


Tentar imprimir o objeto:

```javascript
class Dog {}

const myDog = new Dog()

console.log(myDog)
```


Receberá


```
Dog {}
```


Como pode ver, a classe Dog está vazia, por isso o objeto `myDog` também está vazio.


Podemos definir quais as propriedades que os objectos Dog devem conter, adicionando um `constructor`.


Um construtor é uma função especial que é executada quando se cria (ou "constrói") um novo objeto.


```javascript
class Dog {
constructor() { }
}
```


Queremos que cada Cão tenha um nome, por isso adicionamos um parâmetro `nome` à função:


```javascript
class Dog {
constructor(name) { }
}
```


E então usamos `this` para declarar que `name` é o `nome` do objeto `Dog` que estamos construindo


```javascript
class Dog {
constructor(name) {
this.name = name
}}
```


Vamos tentar utilizá-lo agora:


```javascript
class Dog {
constructor(name) {
this.name = name
}
}

const myDog = new Dog("hachiko")

console.log(myDog)
```


Isto imprime algo do género:


```
Dog { name: 'hachiko' }
```


Como você pode ver, o método `constructor` pega os argumentos que você passa para a classe quando você faz `new Dog()`, e os utiliza para construir o objeto.


Vamos lá ver o que se passa:



- `class Dog` define a classe Dog.
- o `constructor(nome)` define o objeto quando ele é criado.
- `this.name = name` armazena o valor no novo objeto.
- `new Dog("hachiko")` cria um novo objeto da classe, com a propriedade `name` definida como `"hachiko"`.


Agora vamos adicionar um método à nossa classe:


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


Isto irá imprimir


```javascript
hachiko says barf!
```


Se fizermos o mesmo para duas instâncias diferentes de Dog



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


obtemos


```
hachiko says barf!
bobby says barf!
```


o método `speak()` utiliza a propriedade `name` do `Dog` em que é chamado.


Esta é a principal razão da existência das classes: permitem-nos definir um conjunto de métodos que operam sobre os dados e, em seguida, criar vários objectos que partilham a mesma "forma" de dados.


Quando chamamos um método a um destes objectos, este irá operar sobre os dados que esse objeto específico detém.


### Alterar a forma de um objeto


Os objectos em JavaScript são flexíveis. Mesmo depois de o ter criado, pode adicionar novas propriedades ou remover as existentes.


É permitido, mas deve ser utilizado com cuidado.


Vamos começar com a nossa simples classe `Dog`:


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


Neste momento, `meuCão` tem apenas uma propriedade: `nome`. Nós ainda podemos adicionar novas propriedades depois que ele for criado:


```javascript
myDog.age = 5

console.log(myDog.age) // prints 5
```


Também podemos acrescentar um novo método:


```javascript
myDog.jump = function () {
console.log(`${this.name} jumps!`)
}

myDog.jump() // Fido jumps!
```


E também podemos remover propriedades, utilizando a palavra-chave `delete`.


```javascript
delete myDog.name

console.log(myDog.name) // prints 'undefined'
```


Isso funciona, mas há algo importante a saber: Os mecanismos JavaScript como o V8 (usado no Node.js e no navegador Chrome) são executados mais rapidamente quando seus objetos mantêm sempre as mesmas propriedades. Se você adicionar ou remover propriedades depois que o objeto for criado, isso pode tornar as coisas mais lentas.


Em programas pequenos, isso não tem muita importância. Mas em projectos maiores (como jogos), é melhor listar todas as propriedades no construtor desde o início, mesmo que não as utilize de imediato. Isto mantém a forma do objeto estável e ajuda o seu código a correr mais depressa.


Por exemplo, em vez disto:


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


Pode fazer


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


Ambas as versões funcionam, mas a segunda é melhor para o desempenho. O motor é informado antecipadamente das propriedades de cada objeto e pode ser optimizado em conformidade.


O JavaScript permite-lhe remodelar objectos livremente, mas quando utiliza classes, é melhor planear a forma do seu objeto com antecedência.



### Herança com `extends` e `super()`


Por vezes, é necessário criar uma classe que é *quase* igual a outra classe, mas com algumas caraterísticas extra.


Em vez de modificar a forma dos objectos (o que, como já foi referido, não é ótimo para o desempenho), ou de ter de reescrever uma nova classe a partir do zero, o JavaScript permite-lhe utilizar algo chamado **herança**.


Herança significa que uma classe pode **extender** outra. A nova classe obtém todas as propriedades e métodos da antiga e pode adicionar mais ou alterar o que precisa.


Digamos que temos uma classe base chamada `Veículo`:


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


Agora queremos criar uma classe `Carro`. Um carro é um tipo de veículo, mas nós podemos querer que ele tenha algumas caraterísticas extras ou uma mensagem diferente quando ele liga. Em vez de reescrever tudo, podemos usar `extends`:


```javascript
class Car extends Vehicle {
start() {
console.log(`${this.brand} car is ready to drive!`)
}
}
```


A classe `Carro` agora **herda** tudo de `Veículo`. Ela recebe a propriedade `brand`, e nós substituímos o método `start()` pela nossa própria versão.


![](assets/en/4.webp)


Vamos experimentar:


```javascript
const myCar = new Car("Toyota")
myCar.start()
```


Isto imprime:


```
Toyota car is ready to drive!
```


Mesmo que `Carro` não tenha seu próprio construtor, ele ainda utiliza o de `Veículo`. Mas se nós quisermos escrever um construtor personalizado em `Carro`, nós podemos, nós apenas precisamos incluir uma chamada para o construtor de seu pai usando `super()`.


Eis como:


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



Isto imprime:


```
Toyota Corolla is ready to drive!
```


Para resumir



- `extends` significa que uma classe é baseada noutra.
- `super()` é usado para chamar o construtor da classe que está sendo estendida.
- A nova classe obtém todas as propriedades e métodos da classe original.
- É possível **sobrepor** métodos (como `start()`) para que eles façam algo diferente.


Isto é útil quando se tem várias coisas semelhantes (como carros, camiões e bicicletas) e se pretende que partilhem o código, mas que se comportem à sua maneira.


### `instância de`


A palavra-chave `instanceof` verifica se um objeto foi criado a partir de uma determinada classe.


Digamos que temos uma classe chamada `Usuário`:


```javascript
class User {
constructor(username) {
this.username = username
}
}

const regularUser = new User("julia123")

console.log(regularUser instanceof User)
```


Isto imprime:


```
true
```


Confirmando que `regularUser` é um `User`. Isso porque `regularUser` foi criado utilizando a classe `User`.


Também funciona com classes **herdadas**. Por exemplo, aqui está uma classe `Admin` que estende `User`:


```javascript
class Admin extends User {}

const ourAdmin = new Admin("admin42")

console.log(ourAdmin instanceof Admin)   // true
console.log(ourAdmin instanceof User)    // true
```


Ambas as linhas retornam `verdadeiro`. Isso porque `Admin` é uma subclasse de `User`, portanto `nossoAdmin` é tanto um `Admin` quanto um `User`


# JavaScript intermédio

<partId>243f63ab-4f34-5c30-80cb-84ef46f6761d</partId>


## Tratamento de erros

<chapterId>d0206bc5-d386-5e7f-9917-5803f392448c</chapterId>


À medida que escreve programas JavaScript mais complexos, irá encontrar **erros**. Estas são situações inesperadas onde algo dá errado. Talvez uma variável esteja "indefinida" mas você tenta usá-la, ou algum código recebe o tipo errado de entrada.


Se não tratarmos estes erros corretamente, o nosso programa pode falhar ou comportar-se de formas imprevisíveis. O JavaScript fornece ferramentas para detetar e gerir estes erros, para que os possamos tratar de forma mais graciosa.


### Erro comum: aceder a um valor em `undefined`


Eis uma situação comum que provoca um erro:


```javascript
const user = undefined
console.log(user.name)
```


Se executar este código, obterá um erro com o seguinte aspeto:


```
TypeError: Cannot read properties of undefined (reading 'name')
```


Isso é o JavaScript dizendo a você: "Ei, você tentou obter a propriedade `name` de algo que está `undefined`, e isso não faz sentido" E, como você pode ver, quando esse tipo de erro acontece, o programa pára de funcionar, a menos que você tenha escrito um código específico para capturá-lo e tratá-lo.


### `jogar` um erro


Às vezes você quer manualmente **levantar um erro** no seu código. Nesse caso, usa-se a palavra-chave `throw`.


```javascript
throw new Error("This is a custom error message")
```


Isto pára imediatamente o programa e imprime:


```
Uncaught Error: This is a custom error message
```


Você pode utilizar `throw` para impor regras em seu programa. Por exemplo:


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


A segunda chamada causa um erro porque a divisão por zero não é permitida neste exemplo.


### Captura de erros com `try...catch`


Se você não quer que seu programa falhe quando um erro ocorre, você pode pegar o erro usando um bloco `try...catch`. Isso é útil quando você quer que seu programa **continuar** mesmo que algo falhe.


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log("Oops! Something went wrong.")
}
```


Saída:


```
Oops! Something went wrong.
```


Eis como funciona:



- O código dentro do bloco `try` é tentado primeiro.
- Se ocorrer um erro, o JavaScript **pula para o bloco `catch`**, pulando o resto do bloco `try`.
- O bloco `catch` recebe o erro, então você pode imprimi-lo, ou tratá-lo de alguma outra forma, como por exemplo


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log(`The message of the error was: "${error.message}"`)
}
```


Saída:


```
The message of the error was: "Cannot read properties of undefined (reading 'name')"
```


### O bloco `finally


Você também pode adicionar um bloco `finally`. Este é o código que **sempre é executado**, quer tenha havido um erro ou não.


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


Saída:


```
Trying something risky...
Caught the error: Uh oh!
This will run no matter what.
```


## Evitar os insectos

<chapterId>db12d9f6-5806-514c-998e-0ae24805104e</chapterId>


Este capítulo mostra algumas das armadilhas mais comuns em JavaScript e como evitá-las.


### `var` e Assignment sem declaração


Em código JavaScript antigo, variáveis eram frequentemente declaradas utilizando a palavra-chave `var`. Ao contrário de `let` e `const`, que você já aprendeu, `var` pode se comportar de maneiras confusas.


Por exemplo:


```javascript
{
var message = "hello"
}
console.log(message)
```


Seria de se esperar que `message` existisse apenas dentro do bloco, mas não é o caso. `var` ignora o escopo do bloco e torna a variável disponível em toda a função ou arquivo.


Isso pode levar a um comportamento inesperado, especialmente em programas maiores. Por esta razão, código JavaScript moderno deve sempre usar `let` ou `const` ao invés de `var`.


Pior ainda, o JavaScript permite-lhe atribuir valores a variáveis **sem as declarar de todo**:


```javascript
function greet() {
user = "Alice"
}
greet()
console.log(user) // prints "Alice"
```


Isso cria uma nova variável global `nome` sem qualquer declaração. Isso pode acontecer silenciosamente e levar a bugs que são Hard para rastrear, especialmente se foi apenas um erro de digitação. Sempre declare variáveis utilizando `let` ou `const`.


### Sistema de tipos fraco


O JavaScript é fracamente tipado, o que significa que ele converte automaticamente valores de um tipo para outro, se necessário. Isso é chamado de coerção de tipo e, embora possa ser conveniente, muitas vezes leva a resultados confusos.


Por exemplo:


```javascript
console.log("5" + 1)    // "51"
console.log("5" - 1)    // 4
console.log(true + 1)   // 2
console.log(null + 1)   // 1
```


Nestes exemplos, o JavaScript tenta adivinhar o que o utilizador quis dizer. Por vezes, transforma cadeias de caracteres em números, ou booleanos em números, ou cadeias de caracteres em cadeias de caracteres. Isto pode fazer com que o seu código se comporte de formas inesperadas.


É importante estar ciente do fraco sistema de tipagem do JavaScript. Quando as coisas começam a agir de forma estranha, pode ser devido a uma coerção de tipo inesperada.


### `"use strict"`


Pode ativar um modo mais rigoroso que transforma alguns erros silenciosos em erros reais e impede-o de utilizar algumas das caraterísticas mais perigosas da linguagem.


Para ativar este modo mais rigoroso, adicione esta linha no topo do seu ficheiro ou função:


```javascript
"use strict"
```


Por exemplo:


```javascript
"use strict"
name = "Alice" // ReferenceError: name is not defined
```


Sem o strict mode, o JavaScript criaria silenciosamente uma variável global chamada `nome`. Mas com o modo estrito, isso se torna um erro real, ajudando a detetar bugs mais cedo.


O modo estrito também desactiva algumas funcionalidades desactualizadas do JavaScript e torna o seu código mais fácil de otimizar e manter.


## Valor vs. Referência

<chapterId>bb898425-dc2f-5e5c-864b-0cb7a4a9aea9</chapterId>


O JavaScript trata diferentes tipos de valores de formas diferentes.


Alguns valores são **copiados** quando os atribui a uma variável.


Outras são **partilhadas** quando as atribui a uma nova variável, por isso, se alterar uma, a outra também se altera.


### Passar por valor


Quando um valor é passado **por valor**, o JavaScript faz uma **cópia** do mesmo.


Assim, se alterarmos um, o outro não é afetado.


Isto acontece com tipos primitivos, como:



- números
- cordas
- booleanos (`verdadeiro` e `falso`)
- `nulo`
- `undefined`


Vejamos um exemplo:


```javascript
let a = 5
let b = a

b = 10

console.log(a) // 5
console.log(b) // 10
```


Demos a `b` o valor de `a`, mas depois mudámos `b` para `10`.


Como os números são passados por valor, o JavaScript copiou o `5` para `b`. O `5` em `b` é independente do `5` original em `a`, então mudar o valor de `b` não tem efeito em `a`.


Vamos tentar com uma cadeia de caracteres:


```javascript
let name1 = "Alice"
let name2 = name1

name2 = "Bob"

console.log(name1) // Alice
console.log(name2) // Bob
```


Mais uma vez, alterar `nome2` não afectou `nome1`, porque as strings também são passadas por valor.


O mesmo acontece quando passamos uma primitiva para uma função: ela é copiada. Assim, a função não pode alterar o original.


```javascript
function plusOne(x) {
x = x + 1
}

let number = 5

plusOne(number)

console.log(number) // 5
```


Mesmo que dentro da função `1` tenha sido adicionado a `x`, o `número` original não mudou.


Isso deve-se ao facto de apenas uma **cópia** ter sido passada para a função.


### Passar por referência


Os objectos são passados **por referência**.


Isso significa que, em vez de as copiar, o JavaScript passa apenas uma **referência** para a variável e, se a modificar, todas as outras variáveis que apontam para ela também verão a alteração.


Por exemplo:


```javascript
const person1 = { name: "Alice" }
const person2 = person1

person2.name = "Bob"

console.log(person1.name) // Bob
console.log(person2.name) // Bob
```


Tanto `pessoa1` como `pessoa2` apontam para o mesmo objeto na memória.


Assim, quando alterámos `pessoa2.nome`, também alterámos `pessoa1.nome`, porque ambos estão a olhar para a mesma coisa.


As matrizes são objectos, por isso vamos tentar o mesmo com uma matriz:


```javascript
const list1 = [1, 2, 3]
const list2 = list1

list2.push(4)

console.log(list1) // [1, 2, 3, 4]
console.log(list2) // [1, 2, 3, 4]
```


Empurrámos `4` para `list2`, mas `list1` também foi afetada, porque ambas se referem ao mesmo array.


Vejamos o que acontece quando passamos um objeto para uma função:


```javascript
function rename(user) {
user.name = "Charlie"
}

const person = { name: "Dana" }

rename(person)

console.log(person.name) // Charlie
```


A função alterou o objeto! Isto porque recebeu uma **referência** ao objeto `pessoa` original.


Não obteve uma cópia. Obteve acesso ao objeto original e, com isso, a capacidade de o modificar.


É importante lembrar esta distinção, porque, caso contrário, o nosso código pode comportar-se de forma diferente do que esperamos. Por exemplo, podemos escrever uma função com a expetativa de que não modificará os argumentos que recebe, e descobrir mais tarde que na verdade os estava a modificar (porque eram objectos, por isso foram passados por referência).


## Trabalhar com funções

<chapterId>e0d277a8-c642-5af7-9e53-dee27c811967</chapterId>


Já aprendeu a declarar e a utilizar funções em JavaScript. Mas o JavaScript dá-lhe mais ferramentas para trabalhar com funções de formas poderosas.


### Funções de seta


As funções de seta são uma forma mais curta de escrever funções. Em vez de usar a palavra-chave `função`, usamos uma seta (`=>`).


Eis uma função normal:


```javascript
function greet(name) {
return `Hello, ${name}!`
}
```


A versão em seta tem o seguinte aspeto:


```javascript
const greet = (name) => {
return `Hello, ${name}!`
}
```


Se a função tiver **apenas uma linha**, pode saltar as chavetas e `return`:


```javascript
const greet = (name) => `Hello, ${name}!`
```


Se a função tiver **apenas um parâmetro**, pode até saltar os parênteses à volta dos parâmetros:


```javascript
const greet = name => `Hello, ${name}!`
```


As funções de seta são muito comuns no JavaScript moderno, uma vez que permitem expressar funções simples com muito menos boilerplate.


### Parâmetros por defeito


Por vezes, pretende-se que uma função tenha um **valor predefinido** se não for passado nenhum argumento.


Pode fazer isso desta forma:


```javascript
function sayHello(name = "friend") {
console.log(`Hello, ${name}!`)
}

sayHello("Alice") // Hello, Alice!
sayHello()        // Hello, friend!
```


O valor padrão `"friend"` é usado quando nada é passado.


### Parâmetros de propagação (`...`)


E se a sua função receber um número flexível de argumentos?


Pode utilizar o **operador de dispersão** (`...`) para os reunir numa matriz:


```javascript
function logAll(...items) {
console.log(items)
}

logAll(1, 2, 3) // [1, 2, 3]
logAll("a", "b") // ["a", "b"]
```


Pode então utilizar um ciclo para processar cada item:


```javascript
function logEach(...items) {
for (const item of items) {
console.log(item)
}
}
```


O operador de dispersão é útil quando não se sabe quantos argumentos vão ser passados.


### Funções de ordem superior


Uma **função de ordem superior** é uma função que:



- recebe outra função como entrada
- e/ou devolve uma função como saída


Eis um exemplo simples:


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


Isto imprime:


```
Hello, friend!
Hello, friend!
```


Podemos passar-lhe uma função de seta:


```javascript
runTwice(
() => console.log("Hello!")
)
```


Isto imprime:


```
Hello!
Hello!
```


Também é possível escrever funções que **retornam** outras funções:


```javascript
function makeGreeter(name) {
return () => console.log(`Hi, ${name}`)
}

const greetAlice = makeGreeter("Alice")
const greetBob = makeGreeter("Bob")

greetAlice() // Hi, Alice
greetBob() // Hi, Bob
```


A função `makeGreeter` é uma função que constrói outras funções. Ela recebe uma string e retorna uma nova função que utiliza essa string em sua chamada `console.log`.


Este tipo de padrão é muito poderoso, pois permite-lhe deixar "buracos" nas suas funções que pode preencher mais tarde com o comportamento de que necessita.


### `map()`, `filter()`, `reduce()`


O JavaScript fornece-lhe alguns métodos incorporados úteis para utilizar com arrays.


Estes métodos recebem funções como argumentos, pelo que também são funções de ordem superior.


`map()` transforma cada item de um array em outra coisa.


Exemplo:


```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map(x => x * 2)

console.log(doubled) // [2, 4, 6]
```


Cada número é duplicado, e o resultado é uma nova matriz.


`filter()` remove itens do array se eles não passarem em um teste.


Exemplo:


```javascript
const numbers = [1, 2, 3, 4, 5]
const numbersGreaterThanTwo = numbers.filter(x => x > 2)

console.log(numbersGreaterThanTwo) // [3, 4, 5]
```


Apenas as entradas da matriz para as quais a condição `x > 2` retorna `verdadeiro` são mantidas.


`reduce()` é utilizado para combinar todos os itens de um array em um único valor.


Exemplo:


```javascript
const numbers = [1, 2, 3, 4]
const total = numbers.reduce((current, next) => current + next)

console.log(total) // 10
```


o `reduce` percorre o array e, neste exemplo, aplica o operador `+` entre `1` e `2`, depois entre o `3` e o `3` resultantes, depois entre o `6` e o `4` resultantes, até obter a soma de todas as entradas do array (que é 10).


Você pode usar `reduce()` para muitas coisas como totais, médias, ou construir novos valores passo a passo.


Estes métodos (`map`, `filter`, `reduce`) são ferramentas poderosas para processar dados sem escrever loops manuais.


Pode até combiná-los numa cadeia de operações, como esta:


```javascript
const numbers = [1, 2, 3, 4, 5]

const result = numbers
.map(n => n * 2)        // Double each entry, obtain [2, 4, 6, 8, 10]
.filter(n => n > 3) // Keep only the entries bigger than 3, so you get [4, 6, 8, 10]
.reduce((n1, n2) => n1 + n2) // Adds them: 4 + 6 + 8 + 10 = 28

console.log(result) // 28
```


## Trabalhar com objectos

<chapterId>7842aada-f009-5518-b8e3-1104e166a035</chapterId>


Neste capítulo, aprenderemos algumas ferramentas poderosas e um pouco mais avançadas para trabalhar com objetos em JavaScript.


### Propriedades privadas


Às vezes, queremos esconder uma propriedade de um objeto para que ela não possa ser alterada ou acessada de fora do objeto. O JavaScript nos dá uma maneira de fazer isso usando `#` antes do nome da propriedade. Isso cria uma propriedade **privada**, que só é acessível de dentro da classe.


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


As propriedades privadas são úteis quando se pretende evitar alterações acidentais.


### propriedades `estáticas


Algumas vezes, você quer que uma propriedade pertença à própria classe, e não a cada objeto que você criar a partir dessa classe. É para isso que serve o `static`. Uma propriedade `static` está contida na classe e todos os objetos dessa classe farão referência a ela.


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


Isto é útil para armazenar dados e métodos partilhados que se aplicam a todo o grupo de objectos e não apenas a um.


### `get` e `set`


Em JavaScript, `get` e `set` permitem criar propriedades que *parecem* variáveis normais, mas na verdade executam código especial em segundo plano.


Um método `get`ter é executado quando você tenta *ler* uma propriedade. Ele é declarado escrevendo `get` antes de um método com o nome da propriedade.


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


Mesmo que `fullName` não seja uma propriedade normal, podemos usá-la como uma, e nos bastidores ela executa a função `get` para construir o nome completo.


Um método `set`ter é executado quando você *atribui* um valor a uma propriedade. Ele permite que você controle o que acontece quando alguém tenta mudar esse valor. Ele é declarado escrevendo `set` antes de um método com o nome da propriedade.


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


Quando fazemos `user.fullName = "John Smith"`, ele executa o método `set` e atualiza os valores `firstName` e `lastName`.


Assim, mesmo que pareça que estamos apenas a definir uma simples variável, estamos na verdade a acionar a lógica que actualiza outras propriedades.


## Chaves e valores

<chapterId>01a397b8-c12a-5c39-82b3-6d9ebbb72a29</chapterId>


Cada propriedade de um objeto JavaScript tem uma **chave** (também designada por nome de propriedade) e um **valor**.


Por exemplo:


```javascript
const user = {
name: "Alice",
age: 30
}
```


Neste objeto, `"name"` e `"age"` são as chaves, e "Alice" e `30` são os seus valores.


### Acesso dinâmico


Por vezes, não sabemos o nome de uma propriedade antecipadamente... talvez estejamos a obtê-la a partir da entrada do utilizador, ou a lê-la a partir de uma variável. Você ainda pode acessá-la usando **notação de parênteses**, como `myObject["keyName"]`.


```javascript
const user = {
name: "Alice",
age: 30
}

console.log(user["name"]) // Alice
```


Passamos a string `nome` para o objeto de forma a obter o valor correspondente.


Podemos guardar uma chave numa variável e utilizá-la para aceder ao valor correspondente mais tarde, como


```javascript
const user = {
name: "Alice",
age: 30
}

const key = "name"

console.log(user[key]) // Alice
```


### Dinâmico Assignment


Também é possível criar ou atualizar propriedades de objectos utilizando variáveis como chaves.


```javascript
const settings = {}

const key = "theme"
settings[key] = "dark"

console.log(settings) // { theme: "dark" }
```


Isto é útil quando se pretende construir um objeto passo a passo. Por exemplo:


```javascript
const user = {}

user["username"] = "bananaFan123"
user["email"] = "banana@fruit.com"

console.log(user)
// { username: "bananaFan123", email: "banana@fruit.com" }
```


Pode até utilizar uma chave dinâmica *ao criar* o objeto utilizando parênteses rectos:


```javascript
const key = "language"
const config = {
[key]: "JavaScript"
}

console.log(config.language) // JavaScript
```


Isto é chamado de **propriedade computada**. O valor dentro dos parêntesis rectos é avaliado e o resultado é utilizado como a chave.


### tipo `Symbol


Além das strings, o JavaScript também permite utilizar um tipo especial chamado `Symbol` como uma chave de objeto.


Comecemos com um exemplo simples:


```javascript
const id = Symbol("userID")

const user = {
name: "Bob",
[id]: 12345
}

console.log(user[id]) // 12345
```


Neste exemplo, `id` é um Symbol. Não é uma string, mas ainda funciona como uma chave. Se tentar registar `user` na consola, verá isto:


```javascript
console.log(user) // { name: 'Bob', [Symbol(userID)]: 12345 }
```


Outro aspeto importante: cada símbolo que cria é único, mesmo que sejam criados utilizando a mesma cadeia de caracteres.


```javascript
const a = Symbol("label")
const b = Symbol("label")

console.log(a === b) // false
```


Os símbolos permitem-lhe definir chaves que não entram em conflito com as chaves normais. Por exemplo, digamos que você tem um objeto com uma propriedade `name`, mas o objeto será customizável por um usuário no futuro, de maneiras que você não pode prever, e esse usuário pode adicionar uma propriedade `name` também. Se a propriedade `name` original foi definida com uma string, ela seria substituída pela nova, assim:


```javascript
const obj = {
name: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy' }
```


Se, em vez disso, utilizarmos um Símbolo:


```javascript
const name = Symbol("name")

const obj = {
[name]: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy', [Symbol(name)]: 'John' }
```


Como pode ver, a propriedade original `name` é de alguma forma preservada desta forma. Isso pode ser útil em certos casos extremos.


## Objectos utilitários

<chapterId>516e74c8-2a11-545a-a4d1-c2cabb91a273</chapterId>


O JavaScript fornece-nos alguns objectos incorporados úteis que nos ajudam a fazer coisas como depuração e operações matemáticas.


### Outros métodos da consola


Você já viu o `console.log`, que imprime valores na tela.


Existem alguns outros métodos úteis disponíveis no objeto `console` que podem ajudá-lo a depurar seus programas.


#### `console.warn`


Imprime uma mensagem em amarelo (ou com um ícone de aviso em alguns ambientes):


```javascript
console.warn("This is just a warning.")
```


#### `console.error`


Imprime uma mensagem a vermelho, como um erro:


```javascript
console.error("Something went wrong!")
```


#### `console.table`


Apresenta uma matriz ou objeto como uma tabela:


```javascript
const users = [
{ name: "Alice", age: 25 },
{ name: "Bob", age: 30 }
]

console.table(users)
```


Isto imprime uma tabela como:


```
┌─────────┬────────┬─────┐
│ (index) │  name  │ age │
├─────────┼────────┼─────┤
│    0    │ 'Alice'│  25 │
│    1    │ 'Bob'  │  30 │
└─────────┴────────┴─────┘
```


Isto pode ser útil para visualizar dados estruturados.


#### `console.time` e `console.timeEnd`


É possível medir o tempo que algo demora:


```javascript
console.time("timer")
for (let i = 0; i < 1000000; i++) {}
console.timeEnd("timer")
```


Isto imprime algo do género:


```
timer: 2.379ms
```


Útil para alguns testes de desempenho simples.


### O objeto `Math


O JavaScript fornece um objeto `Math` com métodos úteis para fazer cálculos.


#### `Math.random()`


Devolve um número aleatório entre 0 (inclusive) e 1 (exclusivo):


```javascript
const r = Math.random()
console.log(r)
```


Exemplo de saída:


```
0.4387429859
```


#### `Math.floor()` e `Math.ceil()`



- `Math.floor(n)` arredonda **para baixo** para o número inteiro mais próximo
- `Math.ceil(n)` arredonda **para cima** para o número inteiro mais próximo


```javascript
console.log(Math.floor(4.9)) // 4
console.log(Math.ceil(4.1))  // 5
```


#### `Math.round()`


Arredonda para o número inteiro mais próximo:


```javascript
console.log(Math.round(4.4)) // 4
console.log(Math.round(4.6)) // 5
```


#### `Math.max()` e `Math.min()`


Devolve o maior ou o menor valor de uma lista de números:


```javascript
console.log(Math.max(5, 9, 3)) // 9
console.log(Math.min(5, 9, 3)) // 3
```


#### `Math.pow()` e `Math.sqrt()`



- `Math.pow(a, b)` dá-lhe `a` à potência de `b`
- `Math.sqrt(n)` dá-lhe a raiz quadrada de `n`


```javascript
console.log(Math.pow(2, 3))   // 8
console.log(Math.sqrt(16))    // 4
```


# JavaScript avançado

<partId>72c30671-ca20-5617-92a5-d5ba7aa38c93</partId>


## Outras colecções

<chapterId>a9a70c6d-a343-5a46-a383-e288bc2700e3</chapterId>


JavaScript nos dá alguns tipos especiais de coleção que vão além de arrays e objetos comuns. Estes incluem `Map` e `Set`.


Ajudam-no a armazenar e gerir grupos de valores, mas funcionam de forma diferente da que viu até agora.


Um `Map` é uma coleção de **pares chave-valor**, assim como um objeto. Mas tem algumas diferenças importantes:



- As chaves podem ser **qualquer valor** e não apenas cadeias de caracteres.
- A ordem dos itens é preservada.
- Tem métodos incorporados para facilitar o trabalho com ele.


Cria-se um novo mapa como este:


```javascript
const myMap = new Map()
```


Isso cria um mapa vazio. Para adicionar entradas a ele, utilize `myMap.set(key, value)`:


```javascript
myMap.set("name", "Alice")
```


Isso adiciona uma chave `"name"` com valor `"Alice"`.


Também pode utilizar um número como chave:


```javascript
myMap.set(42, "The answer")
```


E até um objeto como chave:


```javascript
const objKey = { id: 1 }
myMap.set(objKey, "Object as key")
```


Isto não funcionaria com objectos normais, que apenas permitem chaves de cadeia de caracteres.


Para **obter um valor**, utilize `myMap.get(key)`:


```javascript
console.log(myMap.get("name"))     // Alice
console.log(myMap.get(42))         // The answer
console.log(myMap.get(objKey))     // Object as key
```


Para **verificar se uma chave existe**, use `myMap.has(key)`:


```javascript
console.log(myMap.has("name")) // true
```


Para **remover uma chave**, utilize `myMap.delete(key)`:


```javascript
myMap.delete("name")
```


Para **limpar o mapa inteiro**, use `myMap.clear()`:


```javascript
myMap.clear()
```


Os mapas são óptimos para gerir grandes colecções de valores, uma vez que o acesso a valores num mapa de grandes dimensões proporciona normalmente um desempenho muito melhor do que num objeto de grandes dimensões.


### `Set`


Um `Conjunto` é uma coleção de **valores apenas** (sem chaves), em que cada valor deve ser **único**. Isso significa que:



- Não se pode ter o mesmo valor duas vezes
- Os valores são armazenados pela ordem em que são adicionados


Cria-se um conjunto como este:


```javascript
const mySet = new Set()
```


Para **adicionar valores**, utilize `mySet.add(value)`:


```javascript
mySet.add(1)
mySet.add(2)
mySet.add(2) // duplicate, will be ignored
```


Apesar de termos tentado adicionar `2` duas vezes, o conjunto só guardará uma cópia.


Para **verificar se um valor está no conjunto**, utilize `mySet.has(value)`:


```javascript
console.log(mySet.has(2)) // true
console.log(mySet.has(3)) // false
```


Para **remover um valor**, utilize `mySet.delete(value)`:


```javascript
mySet.delete(2)
```


Para **limpar tudo**, utilize `mySet.clear()`:


```javascript
mySet.clear()
```


Um `Set` é útil quando se pretende manter uma coleção de valores únicos sem ter de verificar manualmente se existem duplicados:


```javascript
const numberArray = [1, 2, 2, 3, 4, 4, 4, 5]

const numberSet = new Set(numberArray)

console.log(numberSet) // Set(5) { 1, 2, 3, 4, 5 }
```


O `Set` evita as duplicações para si.


## Iteradores

<chapterId>61d24e5e-b7e4-541a-8322-778f61f26a72</chapterId>


A maioria das coisas em JavaScript sobre as quais se pode fazer um loop (como arrays, strings, mapas, conjuntos) são **iteráveis**: podem fornecer iteradores para o seu conteúdo.


Um **iterador** é um objeto especial em JavaScript que o ajuda a percorrer uma lista de itens **um de cada vez**.


### iteradores `Object`


Ao contrário de arrays ou mapas, objectos regulares **não são iteráveis** com `for...of`. Se você tentar isso:


```javascript
const user = {
name: "Alice",
age: 30
}

for (const value of user) {
console.log(value)
}
```


Obterá um erro:


```
TypeError: user is not iterable
```


Isso acontece porque os objectos simples não têm um iterador incorporado. Mas o JavaScript dá-lhe outras ferramentas para fazer um loop sobre eles.


#### `Objeto.chaves()`


Você pode usar `Object.keys(obj)` para obter um array das **chaves** do objeto, e então fazer um loop sobre ele:


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


Isto imprime:


```
name
age
```


#### `Objeto.valores()`


Para percorrer os **valores**, utilize `Object.values()`:


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


Isto imprime:


```
Alice
30
```


#### `Objeto.entradas()`


Se você quiser **tanto a chave quanto o valor**, use `Object.entries()`:


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


Isto imprime:


```
name is Alice
age is 30
```


Mesmo que os objectos não sejam diretamente iteráveis, estes métodos dão-lhe acesso total ao seu conteúdo de uma forma que funciona bem com `for...of`.


Mas como é que os iteradores funcionam?


### `Symbol.iterator`


O segredo por trás de todos os iteráveis é um **símbolo** especial chamado `Symbol.iterator`.


Este símbolo é uma chave incorporada que diz ao JavaScript: "Este objeto pode ser iterado"


Quando você chama `myIterable[Symbol.iterator]()`, o JavaScript devolve um **objeto iterador** com um método `.next()`.


Vamos ver como é que isso se parece:


```javascript
const colors = ["red", "green", "blue"]

const iterator = colors[Symbol.iterator]()

console.log(iterator.next()) // { value: 'red', done: false }
```


Cada chamada a `.next()` fornece o próximo valor. Quando ele termina, ele retorna:


```javascript
{ value: undefined, done: true }
```


### `próximo()`


O método `.next()` é utilizado para obter o próximo item da sequência.


Cada vez que você chama `.next()`, você recebe um objeto com duas chaves:



- `value`: o item atual
- `done`: um booleano que indica se a iteração terminou


Vamos fazer um exemplo completo:


```javascript
const names = ["Lina", "Tom", "Eva"]      // declare an array
const iterator = names[Symbol.iterator]() // use the Symbol.iterator function to get an iterator for this array

let result = iterator.next()              // get the first element of the array

while (!result.done) {                    // repeat this loop until you reach the last element of the array, which is marked with { done: true }
console.log(result.value)               // print the value of each element
result = iterator.next()                // get the next element of the array
}
```


Isto imprime:


```
Lina
Tom
Eva
```


É assim que um laço `for...of` funciona nos bastidores: ele usa esse padrão com `.next()`.


Obterá o mesmo resultado com


```javascript
const names = ["Lina", "Tom", "Eva"]

for (const result of names) {
console.log(result)
}
```


### Tornar uma classe iterável


Pode também definir a sua própria classe **iterable** adicionando um método `[Symbol.iterator]()`.


Digamos que queremos uma classe que represente um **intervalo de números**, como de 1 a 5.


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


Isto imprime:


```
1
2
3
4
5
```


Eis o que está a acontecer:



- Definimos uma classe `Range`
- Dentro da classe, implementamos `[Symbol.iterator]()`, para que o JavaScript saiba como iterar
- O método `next()` devolve cada número um a um
- Quando chegamos ao `fim`, ele retorna `{ done: true }`


Agora nossa classe `Range` funciona como um array, e podemos usá-la em qualquer loop que espere um iterável.


### Funções geradoras e `yield`


Para facilitar a criação de iteradores, o JavaScript oferece **funções geradoras**, usando a palavra-chave `function*` (é `function` com um `*` no final) e a palavra-chave `yield`.


Vamos tentar:


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


Cada `yield` devolve um valor, e **pausa** a função até que o próximo `.next()` seja chamado.


Também é possível fazer um loop sobre um gerador com `for...of`:


```javascript
for (const num of numberGenerator()) {
console.log(num)
}
```


Isto imprime:


```
1
2
3
```


## Concorrência com callbacks

<chapterId>f3fc76ca-b3ef-54eb-a06e-501007002054</chapterId>


Até agora, nosso código tem sido **síncrono**: ele executa uma linha de cada vez, em ordem. Mas algumas coisas no mundo real levam tempo, e não queremos que o programa inteiro pare enquanto espera.


Neste capítulo, vamos introduzir um novo conceito: **concurrency**. Ele nos permite manipular a ordem em que as coisas são feitas. Isto é útil quando se lida com coisas como temporizadores, entrada do utilizador ou leitura de ficheiros do disco. O JavaScript oferece diferentes ferramentas para fazer concorrência.


### `setTimeout`


A função `setTimeout` permite-lhe **executar uma função mais tarde**, após algum tempo.


Exemplo:


```javascript
console.log("Start")

setTimeout(
() => console.log("This runs after 2 seconds"),
2000
)

console.log("End")
```


Isto imprime:


```
Start
End
This runs after 2 seconds
```


Mesmo que `setTimeout` apareça no meio do código, ele não bloqueia o resto. Ao invés disso, ele agenda a função para ser executada **mais tarde**, e imediatamente segue em frente.


O `2000` significa 2000 milissegundos (ou seja, 2 segundos).

Aqui está uma reescrita mais verbosa e amigável para principiantes das secções **Callbacks** e **Promise**, utilizando manipulação de dados e anotações claras:


### Chamadas de retorno


Um **callback** é apenas uma função que damos a outra função para que possa ser **chamada mais tarde**.


Vejamos um exemplo real utilizando números. Imaginemos que temos uma lista de números e queremos duplicar cada um deles e, em seguida, aplicar uma função (a chamada de retorno) à matriz "duplicada" resultante, mas queremos fazê-lo após um pequeno atraso, como se estivéssemos à espera de algo lento (como carregar dados da Internet).


Aqui está uma função que faz isso usando um **callback**:


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


Vamos tentar utilizar esta função:


```javascript
const input = [1, 2, 3]

doubleNumbers(input, function(result) {
console.log("Here is the doubled array:", result)
})
```


Após 1 segundo, isto imprime-se:


```
Here is the doubled array: [ 2, 4, 6 ]
```


**O que é que está a acontecer aqui?


1. Passamos `input` como a lista de números que queremos duplicar.

2. Também passamos uma função **callback** que diz ao programa o que fazer *depois* de duplicar.

3. Dentro de `doubleNumbers`, simulamos um atraso utilizando `setTimeout`, depois fazemos a duplicação.

4. Uma vez feito isso, chamamos o retorno de chamada na matriz "duplicada" resultante.


Esta técnica funciona, mas imagine que quer fazer **mais passos** depois disso, como filtrar números pequenos e depois somá-los. Teria de **aninhar** mais callbacks como esta:


```javascript
doubleNumbers(input, function(doubled) {
filterBigNumbers(doubled, function(filtered) {
sumNumbers(filtered, function(total) {
console.log("Final result:", total)
})
})
})
```


Isto é Hard para ler e confuso. Este estilo é chamado de **callback hell**, e é exatamente o que o `Promise` foi criado para corrigir.


## Concorrência com promessas

<chapterId>30fddaca-729f-5c8d-bf86-8dfc7b3c9800</chapterId>


Um `Promise` é um objeto JavaScript incorporado que representa um valor que estará **pronto no futuro**.


Podemos criar uma Promessa como esta:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve("It worked!") // This means everything went OK
})
```


A parte `new Promise()` cria a promessa.


No seu interior, atribuímos-lhe uma função com dois parâmetros:



- `resolve`, é uma função que chamamos quando tudo é bem sucedido
- `reject`, é uma função que chamamos se algo correr mal


No exemplo acima, resolvemos o problema imediatamente com a mensagem `"Funcionou!"`.


### `.then()`


Para fazer algo **depois** que a promessa é feita, usamos `.then()`:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve(100) // This means everything went OK
})

promise.then(result => {
console.log("The result is:", result)
})
```


Isto imprime:


```
The result is: 100
```


O valor que passamos para `resolve()` é enviado para a função dentro de `.then()` como `result`.


Vamos simular uma tarefa que leva 2 segundos usando `setTimeout`:


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


Aguardará 2 segundos e depois imprimirá:


```
Done waiting!
```


### `rejeitar()`


Vamos criar uma promessa que **falha**:


```javascript
const failingPromise = new Promise((resolve, reject) => {
reject("Something went wrong")
})
```


Agora, se usarmos `.then()` nisso, nada acontecerá, porque `.then()` só lida com sucesso.


Para tratar erros, usamos `.catch()`:


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


Isto imprime apenas


```
Caught an error: Something went wrong
```


O valor passado para `reject()` é enviado para a função `.catch()`.


Vamos construir uma Promessa que **às vezes funciona e às vezes falha**, com base em alguma condição.


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


Agora podemos chamar isto e tratar de ambos os casos:


```javascript
checkNumber(5)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Isto imprime:


```
Success: Positive number
```


E se tentarmos com um número diferente:


```javascript
checkNumber(-1)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Imprime:


```
Failure: Not a positive number
```


### Operações de encadeamento utilizando `Promise`s



Podemos reescrever o nosso exemplo anterior usando `Promise`, e ele parecerá muito mais limpo.


Vamos começar por escrever uma nova versão da nossa função de duplicação, mas desta vez, ela devolve uma **promessa**:


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


Agora podemos usar `.then()` para dizer ao JavaScript o que fazer com o resultado:


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


Isto imprime:


```
Doubled numbers: [ 2, 4, 6 ]
```


Até agora, isto funciona da mesma forma que a versão de retorno de chamada, mas agora o código é mais fácil de estender e ler.


Digamos que queremos acrescentar mais passos:


1. Primeiro, duplicar todos os números

2. Em seguida, retire os números mais pequenos do que 4

3. Por fim, junte-os todos


Podemos escrever uma função para cada passo, todas utilizando promessas:


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


Agora podemos **cadeá-los** juntos desta forma:


```javascript
const input = [1, 2, 3]

doubleNumbers(input)
.then(filterBigNumbers)
.then(sumNumbers)
.then(
result => console.log("Final result after all steps:", result)
)
```


Isto imprime:


```
Final result after all steps: 10
```


Vamos ver o que isto faz:


1. `doubleNumbers` duplica a matriz: `[2, 4, 6]`

2. `filtroNumerosGrandes` remove qualquer coisa ≤ 3: `[4, 6]`

3. `sumNumbers` adiciona os números restantes: `4 + 6 = 10`

4. Por fim, imprimimos o resultado.


Cada `.then()` espera que o passo anterior termine. Assim, podemos construir uma **cadeia de ações** sem aninhamento. Isso torna o código mais legível e mais fácil de depurar.


## Concorrência com `async`/`await`

<chapterId>6e93d29f-c8bf-5fd1-a9c9-4e794ee6cbd0</chapterId>


Vimos como as cadeias `Promise` nos ajudam a evitar o inferno do callback, mas elas ainda podem ficar um pouco Hard para ler quando há muitos passos envolvidos.


É aí que entram `async` e `await`. Eles permitem-nos escrever código assíncrono **que se parece com código síncrono**, o que o torna mais fácil de entender.


### O que é `async`?


Quando você escreve a palavra-chave `async` antes de uma função, o JavaScript automaticamente envolve o valor de retorno da função em uma Promise.


Vejamos um exemplo básico:


```javascript
async function greet() {
return "hello"
}
```


Se esta função for chamada:


```javascript
const result = greet()
console.log(result)
```


Vais ver isto:


```
Promise { 'hello' }
```


Mesmo que você tenha retornado uma string, o JavaScript a transforma em uma Promise para você. Você pode obter o valor real usando `.then()` desta forma:


```javascript
greet().then( result => console.log(result) ) // prints "hello"
```


Ou pode utilizar `await`...


### O que é `await`?


A palavra-chave `await` diz ao JavaScript: "espere até que esta Promessa seja feita, e então me dê o resultado"


Mas só é possível utilizar `await` **dentro de uma função assíncrona**.


Vamos reescrever o exemplo usando `await`:


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


Agora podemos utilizar o resultado como se fosse um valor normal.


Vamos fazer algo um pouco mais útil agora.


### Simulando um atraso com `await`


Vamos criar uma função `wait` simples que recebe uma quantidade de milissegundos como argumento e só resolve depois desse número de milissegundos, sem fazer mais nada:


```javascript
function wait(ms) {
return new Promise(resolve => {
setTimeout(resolve, ms)
})
}
```


Vamos tentar usá-lo:


```javascript
async function test() {
console.log("waiting 2 seconds...")
await wait(2000)
console.log("done waiting")
}

test()
```


Isto imprime:


```
waiting 2 seconds...
done waiting
```


Pode pensar em `await` como "fazer uma pausa aqui até a promessa estar concluída, depois continuar"


Isto permite-lhe escrever código de uma forma **de cima para baixo** que se comporta de forma assíncrona, sem encadear chamadas `.then()`.


### A aguardar dados


Vamos reutilizar nosso exemplo anterior, onde duplicamos números, depois filtramos e depois somamos. Mas desta vez, usaremos `async`/`await`.


Vamos criar 3 funções que simulam a espera e retornam Promessas:


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


Agora vamos escrever uma função `async` para as combinar:


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


Isto imprime:


```
Final result: 10
```


Isso é muito mais fácil de ler do que encadear `.then()` ou aninhar callbacks.


Parece um programa passo-a-passo normal, mas continua a comportar-se de forma assíncrona.


## Iteradores assíncronos

<chapterId>438b037d-9931-56d7-9052-7b4470f3c75b</chapterId>


Você já aprendeu sobre **iteradores** e como podemos usar `for...of` para fazer um loop sobre arrays e outras coisas iteráveis.


Mas e se os dados que queremos iterar demorarem a chegar?


Por vezes queremos fazer um loop sobre coisas que chegam **assincronamente**, como mensagens de um chat, linhas de um ficheiro ou números de uma fonte lenta.


Para o fazer, o JavaScript dá-nos **async iterators**.


### Funções de gerador assíncrono


A forma mais fácil de criar um iterador assíncrono é utilizar uma função geradora **async**.


Escrevemo-lo assim:


```javascript
async function* generateNumbers() {
yield 1
yield 2
yield 3
}
```


Isso se parece com um gerador normal, mas com `async` antes dele.


Podemos agora utilizar `for await...of` para consumir os valores:


```javascript
async function run() {
for await (const n of generateNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


Isto irá imprimir:


```
Got number: 1
Got number: 2
Got number: 3
Done!
```


Então, qual é a diferença em relação a um gerador normal?


A diferença é: agora podemos usar `await` dentro do gerador.


Vamos voltar a fazer um ajudante de atraso:


```javascript
function wait(ms) {
return new Promise(resolve => setTimeout(resolve, ms))
}
```


Agora vamos produzir números **lentamente**:


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


Tenta usá-lo:


```javascript
async function run() {
for await (const n of generateSlowNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


### Porquê utilizar iteradores assíncronos?


Os iteradores assíncronos são úteis quando:



- Os valores não chegam todos ao mesmo tempo.
- É preciso lidar com elas uma de cada vez, **à medida que vão surgindo**.
- Está a trabalhar com Promessas e quer fazer um loop de uma forma limpa.


Por exemplo, se quiser carregar mensagens de um servidor de chat uma a uma, ou descarregar um ficheiro grande em pedaços, os iteradores assíncronos dão-lhe uma forma de escrever um ciclo `for` que funciona com dados atrasados.


### `Symbol.asyncIterator`


Também podemos utilizar iteradores assíncronos em classes personalizadas.


Aqui está um exemplo que produz números com um atraso:


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


Podemos agora utilizar `for await...of` tal como anteriormente:


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


Isto permite-lhe criar objectos que podem ser iterados de forma assíncrona


## Açúcar de sintaxe Assignment

<chapterId>8b1ba7d8-ecfd-5470-b86e-73cb84ccc8b7</chapterId>


"Açúcar sintático" significa escrever algo de uma forma mais curta ou mais fácil, sem alterar o que faz. É apenas uma forma mais agradável de dizer a mesma coisa.


O JavaScript tem alguns recursos de sintaxe incorporados que nos permitem escrever declarações mais limpas e mais curtas. Neste capítulo, veremos como atribuir valores com base numa condição, atualizar variáveis com matemática, extrair valores de arrays ou objectos e copiá-los ou combiná-los com uma sintaxe mais simples.


### O operador ternário


Em JavaScript, é possível atribuir um valor com base numa condição utilizando o **operador alternativo**, que é uma forma abreviada de escrever `se...senão`.


Em vez de fazer:


```javascript
let message

if (isMorning) {
message = "Good morning"
} else {
message = "Hello"
}
```


Pode escrever:


```javascript
const message = isMorning ? "Good morning" : "Hello"
```


Isto significa:



- Se `isMorning` for verdadeiro, usar `"Good morning"`
- Caso contrário, use `"Hello"`


A forma geral é:


```javascript
condition ? valueIfTrue : valueIfFalse
```


Também pode ser utilizada noutras expressões:


```javascript
console.log(isSunny ? "Go outside" : "Stay in")
```


Certifique-se apenas de que a utiliza para decisões **simples**. Se a lógica for complexa, utilize o `if...else`.


### Operadores alternativos do Assignment


O JavaScript tem **operadores de atalho** para fazer atribuições combinadas com operações.


Vejamos a forma normal:


```javascript
let counter = 1
counter = counter + 1
```


Isto pode ser abreviado para:


```javascript
let counter = 1
counter += 1 // same as counter = counter + 1
```


Eis as mais comuns:


| Operator | Meaning             |
| -------- | ------------------- |
| `+=`     | add and assign      |
| `-=`     | subtract and assign |
| `*=`     | multiply and assign |
| `/=`     | divide and assign   |

Exemplos:


```javascript
let score = 10
score += 5  // now score is 15
score *= 2  // now score is 30
score -= 10 // now score is 20
```


São úteis quando se pretende atualizar uma variável utilizando o seu próprio valor.


### Desestruturação


**A reestruturação** permite-lhe retirar valores de arrays ou objectos e armazená-los facilmente em variáveis.


#### Matrizes


Suponhamos que tem:


```javascript
const colors = ["red", "green", "blue"]
```


Em vez de fazer:


```javascript
const first = colors[0]
const second = colors[1]
```


Pode fazer:


```javascript
const [first, second] = colors
```


Isto atribui:



- `first` para `"red"`
- `segundo` para `"Green"`


Também é possível saltar valores:


```javascript
const [,, third] = colors
console.log(third) // blue
```


#### Objectos


Também é possível extrair valores de objectos:


```javascript
const user = { name: "Alice", age: 30 }

const { name, age } = user
console.log(name) // Alice
console.log(age)  // 30
```


Se a propriedade tiver um nome diferente da variável pretendida, pode mudar-lhe o nome:


```javascript
const { name: username } = user
console.log(username) // Alice
```


A desestruturação torna o seu código mais limpo quando trabalha com objectos e matrizes.


### Sintaxe de propagação


A sintaxe **spread** utiliza `...` para descompactar ou copiar valores.


#### Matrizes


É possível copiar ou fundir matrizes:


```javascript
const a = [1, 2]
const b = [3, 4]

const both = [...a, ...b]
console.log(both) // [1, 2, 3, 4]
```


Também é possível clonar uma matriz:


```javascript
const original = [10, 20, 30]
const clone = [...original]
```


#### Objectos


O mesmo se pode fazer com os objectos:


```javascript
const a = { x: 1 }
const b = { y: 2 }

const merged = { ...a, ...b }
console.log(merged) // { x: 1, y: 2 }
```


Também é possível substituir valores:


```javascript
const user = { name: "Alice", age: 30 }
const updated = { ...user, age: 31 }

console.log(updated) // { name: "Alice", age: 31 }
```


Isto é muito útil para atualizar objectos sem alterar o original.


# NodeJS

<partId>42fe4d49-dace-5135-bb9e-b9d75034fb2a</partId>


## Como chegámos ao Node

<chapterId>0da1d60c-06c9-54e6-a181-ae7dabf6e3b8</chapterId>


Neste capítulo, vamos aprender um pouco do contexto histórico sobre JavaScript e NodeJS.


O contexto histórico é muito importante no software, porque muitas vezes estamos a utilizar ferramentas construídas por outras pessoas e, por isso, somos influenciados por decisões tomadas por elas no passado.


Compreender a razão dessas decisões e como as ferramentas que utilizamos se tornaram o que são, ajudar-nos-á a sentirmo-nos um pouco menos confusos sobre o que estamos a fazer.


### Origens do JavaScript


O JavaScript começou por ser uma linguagem simples concebida para tornar as páginas Web interactivas.


Nos anos 90, os navegadores Web como o Netscape Navigator adicionaram o JavaScript para que os programadores pudessem escrever código que fosse executado diretamente no navegador.


A ideia original era ter o Java como linguagem principal para a criação de sítios Web (com os chamados "applets Java") e o JavaScript apenas para coisas menores.


A conceção principal foi feita por Brendan Eich, que na altura trabalhava na Netscape, em menos de duas semanas.


Mas a maioria das pessoas preferia utilizar o JavaScript em vez do Java, e os applets Java tinham alguns problemas de segurança na altura, pelo que o Java acabou por deixar de ser uma opção e o JavaScript tornou-se a norma de facto para o desenvolvimento Web.


### O motor V8


O JavaScript é uma linguagem interpretada, por oposição a linguagens compiladas como o C.


O código escrito numa linguagem compilada é transformado em binário, e o binário é enviado diretamente para a CPU do computador.


![](assets/en/6.webp)


As linguagens interpretadas, por outro lado, tendem a ser mais fáceis de utilizar e estão mais próximas da forma como os seres humanos pensam ("alto nível") do que da forma como as máquinas funcionam ("baixo nível"); por isso, normalmente, têm uma máquina virtual construída para executar o seu código.


Uma máquina virtual é um programa especial que se situa entre o código que escreve e a CPU, e executa o seu código (porque a CPU não o consegue compreender).


Isto permite-lhe programar sem saber muito sobre a máquina subjacente, mas também tem um custo em termos de desempenho, porque o computador não está a executar apenas o seu programa; está a executar um programa (a máquina virtual) que executa o seu programa.


À medida que as aplicações Web se tornaram cada vez mais complexas, houve uma procura para melhorar o desempenho do JavaScript. O motor V8 é o interpretador que alimenta o JavaScript no Google Chrome. Foi desenvolvido na Google e lançado em 2008.


Enquanto os mecanismos JavaScript mais antigos eram principalmente máquinas virtuais tradicionais, o mecanismo V8 é um compilador JIT (just-in-time).


O código JavaScript é enviado para o mecanismo V8, e o mecanismo tenta compilar partes dele como binários nativos em tempo real. Isto permite-lhe ter a experiência de uma linguagem de alto nível, com um desempenho que está um pouco mais próximo das linguagens de baixo nível. Isso fez do JavaScript a linguagem de alto nível mais rápida do mundo, uma espécie de "melhor dos dois mundos".


### O tempo de execução do NodeJS


Apesar de ser fácil de utilizar e bastante rápido de executar, após o lançamento do V8 o JavaScript continuou a ter uma enorme limitação: só podia ser executado dentro de um browser.


Porque é que isso é um problema?


Bem, uma vez que os browsers executam código obtido a partir de milhões de fontes diferentes na Internet, podem facilmente incorrer em malware, pelo que estão "protegidos" do resto do sistema operativo.


![](assets/en/7.webp)


O JavaScript não podia aceder ao sistema de ficheiros e a outros recursos locais do seu computador (pelo menos, não tão facilmente como outras linguagens), pelo que isso constituía uma limitação significativa do tipo de aplicações que podia construir com ele.


Em 2009, Ryan Dahl publicou o NodeJS, que é um tempo de execução que permite utilizar o motor V8 fora do browser, diretamente no sistema operativo nativo do computador. Ele também adiciona muitos recursos que são úteis para escrever programas do lado do servidor e de linha de comando. Por exemplo, pode utilizar o NodeJS para criar um servidor Web, ler e escrever ficheiros ou criar ferramentas que automatizam tarefas.


![](assets/en/8.webp)


Neste curso, até agora, exploramos os recursos do JavaScript que estão presentes no navegador e no NodeJS. Esses recursos nos permitiram definir dados e manipulá-los de maneiras abstratas. Nas próximas lições, exploraremos os recursos que são específicos do NodeJS e que nos permitem interagir com o sistema operacional.


## Argumentos da linha de comando

<chapterId>960d20f3-c424-5d51-a041-ef17d2e94b6d</chapterId>


O NodeJS permite-nos, entre outras coisas, construir CLIs (Command Line Interfaces).


Para isso precisamos de uma forma de receber argumentos da linha de comando, o que no Node é feito usando o objeto `process` embutido.


### `processo`


O NodeJS fornece um objeto especial chamado `process` que representa o programa atual em execução.


Pode utilizá-lo para inspecionar o ambiente, o diretório de trabalho atual e até sair do programa quando necessário.


Por exemplo:


```javascript
console.log(process.platform)
```


Isto imprime a plataforma do sistema operativo, como `win32`, `linux`, ou `darwin` (Mac).


### `process.argv`


Quando você executa um programa NodeJS a partir do terminal, você pode passar palavras extras (argumentos) após o nome do script. Estes são armazenados em `process.argv`.


Por exemplo, se executar este comando:


```
node my_script.js alpha beta
```


Pode imprimir os argumentos da seguinte forma:


```javascript
console.log(process.argv)
```


O resultado pode ter o seguinte aspeto:


```
[ '/path/to/node', '/path/to/my_script.js', 'alpha', 'beta' ]
```


Os dois primeiros itens são sempre o caminho do nó e o caminho do script. Quaisquer palavras adicionais que tenha passado para o script vêm depois disso.


O array `process.argv` pode ser cortado como qualquer outro array utilizando o método `.slice()`, então para obter apenas os argumentos que foram passados você pode fazer


```javascript
const args = process.argv.slice(2)

console.log(args)
```


Ter acesso aos argumentos que o utilizador está a passar é fundamental para desenvolver aplicações de linha de comandos.


## Módulos

<chapterId>4e1651a5-65fd-50bc-b22a-40313d5659ca</chapterId>


Os tempos de execução do JavaScript, como o NodeJS, geralmente tratam cada arquivo JavaScript como um módulo separado.


Pense num módulo como uma caixa. A caixa tem o seu próprio espaço privado, pelo que as variáveis e funções nela declaradas não interferem com o código noutras caixas. Basicamente, cada módulo tem o seu próprio âmbito.


Um módulo pode exportar parte do seu conteúdo, tornando-o disponível para outros módulos, e pode importar o conteúdo que outros módulos exportaram. O JavaScript permite-lhe exportar e importar conteúdo entre módulos, para ligar diferentes ficheiros.


Um programa JavaScript é frequentemente composto por vários módulos, que estão ligados entre si.


Porquê utilizar módulos? Ao dividir o seu código em módulos, pode organizar o seu programa em partes mais pequenas, mais claras e reutilizáveis. Cada módulo pode focar apenas um tipo de tarefa, como lidar com cálculos matemáticos, trabalhar com ficheiros ou formatar texto.


### Módulos CommonJS


No NodeJS, o sistema mais comum para gerenciar módulos é chamado de **CommonJS**.


Neste sistema, é possível partilhar (exportar) código de um módulo utilizando `module.exports` e carregá-lo (importar) noutro ficheiro utilizando `require()`.


Para tornar algo disponível fora de um módulo, você o atribui a `module.exports`:


```javascript
const greeting = "Hello!"

module.exports = greeting
```


Aqui, a string `"Hello!"` é o que este módulo exporta.


Para utilizar o código exportado de outro ficheiro, utiliza-se a função `require()` com o caminho para esse ficheiro:


```javascript
const greeting = require("./greeting.js")

console.log(greeting)
```


Isto imprime:


```
Hello!
```


É possível exportar várias coisas juntando-as num objeto anónimo, como


```javascript
const greeting1 = "hello"

const greeting2 = "hi"

module.exports = {
greeting1, greeting2
}
```


O CommonJS foi o sistema de módulos inicialmente adotado pelo NodeJS. Mais tarde, foram também adicionados módulos ES.


### Módulos ES


O NodeJS também suporta outro tipo de módulo chamado **ES Modules**, que são populares no desenvolvimento web. Eles usam as palavras-chave `export` e `import`.


Os módulos ES foram desenvolvidos para o navegador e só mais tarde adicionados ao Node. Se quiser utilizá-los, poderá ter de utilizar `.mjs` como extensão de ficheiro em vez de `.js`, dependendo da versão do Node que estiver a utilizar.


Num ficheiro chamado `greeting.mjs` escrevemos


```javascript
export const greeting = "Hello!"
```

Como pode ver, estamos a exportar a constante diretamente para o local onde é definida


Num outro ficheiro chamado `index.mjs`, importamo-lo:


```javascript
import { greeting } from "./greeting.mjs"

console.log(greeting)
```


É possível exportar diferentes declarações em diferentes partes do ficheiro, como


```javascript
export const num = 10

export function double (x) {
return x*2
}
```


### A biblioteca padrão do NodeJS


O NodeJS também inclui muitos módulos incorporados. Estes são módulos prontos fornecidos pelo NodeJS que ajudam em tarefas comuns como ler ficheiros, trabalhar com o sistema operativo ou ligar-se à rede.


Por exemplo, o módulo `os` dá-lhe informações sobre o seu sistema operativo:


```javascript
const os = require("os")

console.log(os.platform())
```


Não é preciso instalar esses módulos embutidos, eles vêm com o NodeJS. Eles formam a "biblioteca padrão" do tempo de execução e são usados pela maioria dos aplicativos Node para fazer coisas como ler arquivos ou se comunicar pela Internet.


Os próximos capítulos mostrar-lhe-ão alguns exemplos úteis da sua utilização.


## O módulo `fs

<chapterId>911e953a-35ae-5ee7-bd74-372501c32e81</chapterId>


O módulo `fs` (abreviação de **file system**) é parte da biblioteca padrão do NodeJS. Ele permite que você trabalhe com arquivos e diretórios no seu computador: você pode ler arquivos, escrever arquivos, excluí-los, renomeá-los e muito mais.


Para a utilizar, é necessário primeiro importá-la no topo do ficheiro:


```javascript
const fs = require("fs")
```


### API de sincronização


A maneira mais simples de usar `fs` é com seus métodos **sync**.


Estes métodos bloqueiam o programa até terminarem (pelo que a linha de código seguinte não é executada até a operação estar concluída).


Eis um exemplo de leitura síncrona de um ficheiro:


```javascript
const fs = require("fs")

const data = fs.readFileSync("example.txt", "utf8")

console.log(data)
```


Se existir um ficheiro chamado `exemplo.txt` no mesmo diretório que o seu script, isto irá imprimir o seu conteúdo.


Também é possível escrever num ficheiro de forma síncrona:


```javascript
const fs = require("fs")

fs.writeFileSync("output.txt", "Hello from Node!")

console.log("File written!")
```


Isso cria (ou sobrescreve) um arquivo chamado `output.txt` com o texto.


Eis algumas operações comuns que pode efetuar com esta API:


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


A API de sincronização é simples e boa para pequenos scripts, mas como bloqueia o programa até que este esteja concluído, pode tornar as coisas mais lentas se estiver a trabalhar com ficheiros grandes ou com um servidor.


### API assíncrona de chamada de retorno


A API de **callback** não é bloqueante: permite que o NodeJS continue a fazer outras coisas enquanto a operação do ficheiro acontece.


Em vez de devolver o resultado diretamente, recebe uma função (um **callback**) que é chamada quando a operação é concluída.


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


O que acontece é o seguinte:



- `fs.readFile` inicia a leitura de `exemplo.txt`.
- O NodeJS não espera, ele segue em frente para executar outro código que você possa ter escrito.
- Quando o ficheiro termina de ser lido, a chamada de retorno é executada:



  - Se houver um erro, `err` contém o erro.
  - Caso contrário, `data` contém o conteúdo.


Eis como se escreve para um ficheiro:


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


A mesma ideia: o programa não pára enquanto escreve o ficheiro.


Alguns exemplos de coisas que pode fazer com esta API:


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


A API de retorno de chamada é melhor para servidores e grandes tarefas porque não bloqueia o programa, mas retornos de chamada aninhados podem ficar confusos se você encadear muitas operações. É por isso que uma API assíncrona baseada em promessa foi adicionada.


### API assíncrona de promessa


A API baseada em promessas é moderna e funciona muito bem com `.then()` e `async/await`. Ela está disponível como `fs.promises`.


É necessário importar a propriedade `promises`:


```javascript
const fs = require("fs").promises
```


Utilizando `.then()`:


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


Ou ainda melhor, usando `async/await`:


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


Escrever para um ficheiro:


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


A lista habitual de exemplos para a API:


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


Quando escreve código, é frequente ter de utilizar código escrito por outras pessoas; por exemplo, bibliotecas para o ajudar a trabalhar com datas, cores, servidores ou quase tudo o resto.


Em vez de descarregar e copiar ficheiros manualmente, pode utilizar um **gestor de pacotes**.


Um gestor de pacotes é uma ferramenta que:



- pacotes de descarregamento
- mantém um registo dos pacotes de que o seu projeto necessita
- garante que todos os membros da sua equipa têm as mesmas versões dos pacotes


### O que é o NPM


No mundo do NodeJS, o gerenciador de pacotes mais popular é o **NPM**, que significa *Node Package Manager*.


O NPM é obtido automaticamente quando se instala o NodeJS.


Pode verificar se tem NPM executando isto no seu terminal:


```
npm -v
```


Isso imprime a versão do NPM que você tem, como:


```
10.2.1
```


### Criar um pacote


No NodeJS, um **package** é apenas um diretório com um arquivo `package.json` nele.


Vamos criar um passo a passo.


1. Crie uma nova pasta para o seu projeto:


```
mkdir my_project
cd my_project
```


2. Execute este comando:


```
npm init
```


Isto inicia uma configuração interactiva, fazendo-lhe perguntas como o nome do seu projeto, versão, descrição, etc.


Se não quiser responder a tudo e apenas aceitar as predefinições, pode utilizar:


```
npm init -y
```


Depois de o executar, verá um novo ficheiro na sua pasta chamado:


```
package.json
```


### `package.json`


O arquivo `package.json` é apenas um arquivo JSON que armazena metadados sobre seu projeto.


Eis um exemplo:


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


Alguns domínios importantes:



- `name`: o nome do seu pacote
- `version`: a versão atual
- `main`: o ficheiro de ponto de entrada (como `index.js`)
- `scripts`: comandos que podem ser executados (como `npm start`)
- `dependencies`: lista todos os pacotes dos quais seu projeto depende


### Instalar um pacote


Digamos que você queira usar um certo pacote chamado `picocolors` para adicionar cores à saída do seu terminal.


Pode instalá-lo executando:


```
npm install picocolors
```


Agora você pode usá-lo em seu projeto. Faça um arquivo `index.js` com


```javascript
const pico = require('picocolors')

console.log(
pico.green("This text is green!")
)
```


e tente executá-lo. O terminal deve imprimir uma versão colorida do texto.


O que é que a NPM fez?



- Ele baixou o pacote e o armazenou em uma subpasta chamada `node_modules/`
- ele adicionou uma entrada em `dependencies` no seu `package.json`
- ele atualizou o arquivo `package-lock.json


O que é `package-lock.json` ?


### `package-lock.json`


Este ficheiro é criado automaticamente pelo NPM.


Você pode se perguntar, se já temos `package.json`, por que precisamos de outro arquivo?

Eis a razão:



- o `package.json` apenas diz qual versão **range** de um pacote seu projeto precisa.

Exemplo:


```json
"dependencies": {
"picocolors": "^1.1.0"
}
```


O `^1.1.0` significa "qualquer versão que seja compatível com 1.1.x", por isso é flexível.



- o `package-lock.json` **congela** as versões exatas de cada pacote e suas sub-dependências, para que todos que instalarem seu projeto tenham exatamente a mesma configuração de trabalho.


Porque é que isto é importante?


Se trabalhar numa equipa, ou se implementar o seu projeto num servidor, ou se voltar a ele no futuro, quer ter a certeza de que continua a funcionar da mesma forma.

Se os pacotes tiverem sido actualizados e se reinstalar sem um ficheiro de bloqueio, poderá obter uma versão ligeiramente diferente que se comporta de forma diferente.


Ao manter o `package-lock.json` no seu projeto, o NPM sempre instalará as versões exatas listadas lá, garantindo que todos tenham o mesmo ambiente.


o `package-lock.json` bloqueia tudo para uma versão muito específica, para tornar o projeto mais reproduzível em outras máquinas.


Mas se o seu pacote precisa ser utilizado por muitas pessoas, você pode optar por não submetê-lo, para que o NPM encontre apenas o arquivo `package.json` e tenha permissão para instalar automaticamente as versões mais recentes que são permitidas nesse arquivo.


Mas essas são coisas com as quais você deve se preocupar mais tarde, quando começar a publicar seu próprio código. Por enquanto, introduzimos o básico do NPM apenas para permitir que você encontre e use as bibliotecas publicadas por outros desenvolvedores em seus projetos.



## Ligação em rede no NodeJS

<chapterId>f2cabd8b-754b-5c97-8d6a-8412a9a184c7</chapterId>


O NodeJS é frequentemente utilizado como uma linguagem para backend: pode transformar o seu script num servidor e também utilizá-lo para fazer pedidos a outros servidores.


Neste capítulo, vamos apresentar algumas funcionalidades básicas de rede que lhe permitirão fazer isso.


### `fetch()`


Se quiser que o seu programa descarregue dados de um sítio Web ou de uma API, tem de fazer um pedido **HTTP**.


Nas versões modernas do NodeJS, é possível usar a função `fetch()` incorporada.


Eis um exemplo de um pedido GET a uma API:


```javascript
const response = await fetch("https://jsonplaceholder.typicode.com/posts/1")
const data = await response.text()

console.log(data)
```


Quando o executar, verá algo como:


```
{
"userId": 1,
"id": 1,
"title": "...",
"body": "..."
}
```


Eis o que acontece:


1. `fetch()` recebe um URL e faz um pedido.

2. Devolve um **Promise** que resolve um objeto `Response`.

3. `response.text()` lê o corpo da resposta como uma string.


Mas a cadeia de caracteres que recebe é, na realidade, JSON. O que é isso?


### JSON


Ao trabalhar com APIs da Web, os dados são frequentemente enviados e recebidos como **JSON**, que significa JavaScript Object Notation.


JSON é apenas um formato de texto que se parece muito com objectos JavaScript. Por exemplo:


```json
{
"name": "Alice",
"age": 30,
"likes": ["apples", "bananas"]
}
```


O objeto `JSON` é um utilitário incorporado no JavaScript que pode ser utilizado para trabalhar com este formato de dados.


Você pode converter um objeto JavaScript em uma string JSON usando `JSON.stringify()`:


```javascript
const user = { name: "Alice", age: 30 }

const jsonString = JSON.stringify(user)

console.log(jsonString)
```


Isto imprime:


```
{"name":"Alice","age":30}
```


Também é possível converter texto JSON em um objeto JavaScript usando `JSON.parse()`:


```javascript
const jsonText = '{"name":"Bob","age":25}'

const obj = JSON.parse(jsonText)

console.log(obj)
```


Isto imprime:


```
{ name: 'Bob', age: 25 }
```


Tenha cuidado: `JSON.parse()` lançará um erro se a string não for um JSON válido.


```javascript
JSON.parse("not json") // ❌ Error!
```


Por isso, certifique-se de que a cadeia de caracteres está corretamente formatada.


### servidor `http


O NodeJS permite-lhe criar um servidor Web sem instalar mais nada.


Pode utilizar o módulo `http` incorporado para tratar os pedidos dos clientes e enviar as respostas.


Eis um exemplo muito básico:


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


Quando executar este script e abrir `http://localhost:3000` no seu browser, verá:


```
Hello from NodeJS server!
```


Isto é o que está a acontecer no código:


1. Você importou o servidor `http` da biblioteca padrão do Node.

2. `http.createServer()` cria um servidor. Você passou para `http.createServer()` um callback `(req, res) => {...}` para ser executado toda vez que alguém se conectar.

3. Atribuiu um código de estado 200 (que indica uma operação bem sucedida) à resposta. Pode ler sobre os códigos de estado http [aqui] (https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

3. `res.end()` envia a resposta e termina a ligação.

4. `server.listen(3000)` inicia o servidor na porta 3000.


Também pode verificar `req.url` e `req.method` no pedido para lidar com diferentes caminhos ou tipos de pedido.


Exemplo com encaminhamento:


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


Estes são exemplos muito básicos. Para construir servidores mais avançados, a maioria dos desenvolvedores provavelmente baixaria uma biblioteca de backend pronta para uso como [express](https://www.npmjs.com/package/express).


## Processamento de dados: buffers, eventos, fluxos

<chapterId>8c9623f0-a604-51a4-8fe4-871c849d3e3b</chapterId>


Neste capítulo, apresentaremos principalmente três classes de objectos:



- `Buffer`, que representa pequenos pedaços de dados binários
- `EventEmitter`, que pode ser usado para rastrear algum passo por processo assíncrono, emitindo sinais chamados "eventos"
- `Stream`, que nos permite processar uma grande porção de dados, um `Buffer` de cada vez, e que acompanha o processo emitindo eventos


Estes são extremamente comuns no código NodeJS profissional, por isso, mesmo que não os utilize nos seus primeiros projectos, é bom ter uma compreensão básica para quando precisar de interagir com eles


### Amortecedores


No NodeJS, um **buffer** é um tipo de objeto utilizado para trabalhar com dados binários.


Pode pensar num buffer como um contentor de tamanho fixo para bytes brutos.


Eis como criar uma memória intermédia a partir de uma cadeia de caracteres:


```javascript
const buf = Buffer.from("hello")
console.log(buf)
```


Isto imprime algo do género:


```
<Buffer 68 65 6c 6c 6f>
```


Esses números (`68`, `65`, `6c`, etc.) são representações hexadecimais das letras em `"hello"`.


Pode convertê-lo novamente numa cadeia de caracteres desta forma:


```javascript
console.log(buf.toString())
```


Isto imprime:


```
hello
```


Também é possível criar um buffer de um determinado tamanho preenchido com zeros:


```javascript
const buf = Buffer.alloc(10)
console.log(buf)
```


Isto imprime algo do género:


```
<Buffer 00 00 00 00 00 00 00 00 00 00>
```


É possível escrever na memória intermédia:


```javascript
buf.write("abc")
console.log(buf)
```


E é possível aceder a bytes individuais:


```javascript
console.log(buf[0]) // prints the ASCII number for 'a', which is 97
```


Os buffers são especialmente úteis quando é necessário manipular dados a um nível muito baixo.


### Eventos


Em JavaScript, um **evento** é algo que acontece no seu programa e ao qual pode reagir.


Por exemplo:



- um ficheiro termina de ser carregado
- um temporizador é ativado
- um utilizador clica num botão
- um pedido de rede devolve dados


Um **evento** é apenas um sinal de que algo aconteceu, e é possível escrever código para ouvir esses eventos e reagir a eles.


No NodeJS, muitos objectos podem emitir eventos. Estes objectos são chamados **EventEmitters**.


Eis um exemplo:


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


Isto imprime:


```
Hello! An event happened.
```


Eis o que acontece:


1. Criamos um objeto `EventEmitter`.

2. Dizemos a ele para executar um callback sempre que o evento `"greet"` acontecer, usando `.on("greet")`.

3. Mais tarde, acionamos o evento `"greet"` usando `.emit()`.

4. O nosso retorno de chamada é executado


É possível transmitir dados juntamente com o evento:


```javascript
emitter.on("greet",
(name) => console.log(`Hello, ${name}!`)
)

emitter.emit("greet", "Alice") // first argument is the type of event, second argument is the data we pass with this event
```


Isto imprime:


```
Hello, Alice!
```


Também é possível registar ouvintes para outros eventos:


```javascript
emitter.on("goodbye", () => {
console.log("Goodbye!")
})

emitter.emit("goodbye")
```


Pode anexar tantos ouvintes quantos quiser a um tipo de evento e pode disparar muitos tipos diferentes de eventos a partir do mesmo emissor.


Muitos objetos no NodeJS emitem eventos para informar ao resto do programa que algo está acontecendo.



### O que são os cursos de água?


Os fluxos combinam buffers e eventos para nos ajudar a processar dados.


Quando trabalhamos com ficheiros, dados da rede ou mesmo texto longo, nem sempre precisamos (ou queremos) carregar tudo na memória de uma só vez. Isso pode ser lento, ou até mesmo travar o programa se os dados forem muito grandes.


Em vez disso, podemos processar os dados **pouco a pouco**, à medida que chegam ou são lidos, como se estivéssemos a beber água por uma palhinha em vez de tentar beber o copo todo de uma vez. A isto chama-se um **stream**.


No NodeJS, um fluxo é um objeto que permite ler dados de uma fonte ou escrever dados para um destino **um pedaço de cada vez**.


O NodeJS tem quatro tipos principais de fluxos:



- Readable**: fluxos a partir dos quais se pode ler dados (como ler um ficheiro)
- Writable**: fluxos onde se pode escrever dados (como escrever num ficheiro)
- Duplex**: fluxos que são simultaneamente legíveis e graváveis
- Transform**: como os fluxos duplex, mas podem alterar (transformar) os dados à medida que estes fluem


### Fluxos legíveis


Digamos que você tenha um `bigfile.txt` para processar. Você pode criar um fluxo legível com o módulo `fs` para ler o arquivo pedaço por pedaço.


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


O que é que acontece aqui?


1. `fs.createReadStream()` cria um fluxo legível.

2. Sempre que um pedaço do ficheiro está pronto, o stream emite um evento `data` e dá-nos um "pedaço" de dados (um `Buffer`). Nós imprimimos o pedaço.

3. Quando todo o ficheiro tiver sido lido, o evento `end` é ativado.

4. Se houver um erro (como se o ficheiro não existisse), o evento `error` é ativado.


Desta forma, é possível ler ficheiros gigantes sem os carregar todos de uma só vez na memória.


Se quisermos que os dados cheguem num formato legível por humanos (em vez de binário), podemos especificar a codificação do fluxo:


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


O código imprimirá agora o ficheiro em formato legível por humanos.


### Fluxos graváveis


Um fluxo gravável permite-lhe enviar dados para algum lado, pedaço a pedaço.


Aqui está um exemplo de escrita para um arquivo `target.txt` usando um fluxo:


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


O que acontece é o seguinte:


1. `fs.createWriteStream()` cria um fluxo gravável.

2. Escrevemos algum texto nele usando `.write()`.

3. Quando terminarmos, chamamos `.end()` para fechar o fluxo.

4. Quando todos os dados tiverem sido escritos, o evento `finish` é emitido.

5. Se algo correr mal, é acionado o evento `error`.


Tal como os fluxos legíveis, os fluxos graváveis são bons para grandes volumes de dados porque não precisam de manter tudo na memória ao mesmo tempo.


### Fluxos de tubagem


Uma das coisas mais interessantes sobre os streams é que pode **pipe**-los juntos: ligar um stream legível diretamente a um stream gravável.


```javascript
const fs = require("fs")

const readable = fs.createReadStream("bigfile.txt")
const writable = fs.createWriteStream("target.txt")

readable.pipe(writable)
```


Aqui:



- O fluxo legível lê a partir de `bigfile.txt`.
- O fluxo gravável escreve em `copy.txt`.
- o `.pipe()` envia os dados diretamente do fluxo legível para o fluxo gravável.


### Fluxos duplex


Um fluxo duplex é tanto legível como gravável. Um exemplo é um socket de rede: pode enviar dados para ele e receber dados dele.


Aqui está um exemplo muito simples usando o módulo `net`:


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


Neste exemplo:



- O objeto `socket` é um fluxo duplex.
- Pode `escrever()` nele e também ouvir os eventos `data` dele.


### Transformar fluxos


Um fluxo de transformação é um fluxo duplex que também modifica os dados que passam por ele.


Por exemplo, você pode usar o módulo `zlib` embutido para comprimir ou descomprimir dados.


Eis como comprimir um ficheiro utilizando um fluxo de transformação:


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


E para o descomprimir de novo:


```javascript
const readable = fs.createReadStream("bigfile.txt.gz")
const unzip = zlib.createGunzip()
const writable = fs.createWriteStream("bigfile.txt")

readable.pipe(unzip).pipe(writable)

writable.on("finish", () => {
console.log("File decompressed.")
})
```


Os fluxos de transformação são muito úteis para tarefas como a compressão, a encriptação ou a alteração de formatos de ficheiros durante o fluxo.


### Contrapressão


Por vezes, um fluxo gravável é lento no tratamento de dados. Se continuarmos a enviar dados para um fluxo gravável mais depressa do que ele consegue suportar, podemos ter problemas. A isto chama-se **pressão de retorno**.


Se você chamar o método `.write()` em um fluxo gravável, ele retorna um booleano que informa se o fluxo precisa de uma pausa; você pode ter que verificar seu valor de retorno, assim:


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


Este foi um exemplo ilustrativo da canalização manual de dados de um Readable para um Writable, e da gestão manual da contrapressão.


Normalmente, canalizaríamos os dados usando o método `.pipe()`, que lida com a contrapressão automaticamente.


Assim, só precisa de se preocupar com a contrapressão quando, por alguma razão, estiver a chamar manualmente `.write()`.


## Nota final

<chapterId>139e2ab8-df67-525a-85f0-5a2fa5e478f2</chapterId>


Então, é isso, se você seguiu as lições, agora deve ser capaz de escrever alguns programas simples em NodeJS.


Sugiro que faça exatamente isso: depois de aprender o básico, construir alguns projectos pessoais é a melhor forma de praticar e de se tornar um programador melhor.


Não importa realmente o que constrói, o que importa é que se desafie a si próprio a resolver problemas com código.


As linguagens de programação modernas são incrivelmente poderosas, e o NodeJS é provavelmente a melhor caixa de ferramentas para experimentar nesta fase da sua jornada.


Boa sorte!


# Secção final


<partId>322624d8-6fbc-11f0-a67a-5b145f10afc1</partId>


## Comentários e classificações


<chapterId>3e93ac86-6fbc-11f0-8bae-9b2ed7914843</chapterId>

<isCourseReview>true</isCourseReview>

## Conclusão


<chapterId>49b3b9b2-6fbc-11f0-9870-5f5adcd3a0eb</chapterId>


<isCourseConclusion>true</isCourseConclusion>